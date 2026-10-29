# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 03:31:21 IST` (`2026-10-29 22:01:21 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1576` | `0.1586` | `0.1572` | `0.1575` | `3,547,433` | 559,773.11 USD | 9,892.97 USD | `+1.77%` | -7,803,020.44 USD | `+0.40` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1575` | `0.1578` | `0.1560` | `0.1570` | `3,319,997` | 520,461.74 USD | -30,735.13 USD | `-5.91%` | -7,833,755.57 USD | `+0.33` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.1570` | `0.1572` | `0.1564` | `0.1564` | `229,335` | 35,969.78 USD | -15,725.72 USD | `-43.72%` | -7,849,481.29 USD | `+0.36` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1565` | `0.1599` | `0.1565` | `0.1580` | `23,334,245` | 3,702,564.80 USD | -87,462.01 USD | `-2.36%` | -7,559,595.65 USD | `+0.18` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1580` | `0.1603` | `0.1573` | `0.1576` | `30,414,514` | 4,839,053.12 USD | -253,317.77 USD | `-5.23%` | -7,812,913.41 USD | `-0.06` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1576` | `0.1586` | `0.1560` | `0.1566` | `7,127,407` | 1,121,001.22 USD | -36,062.92 USD | `-3.22%` | -7,848,976.34 USD | `+0.24` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1686` | `0.1693` | `0.1678` | `0.1683` | `12,478,051` | 2,101,814.57 USD | 317,188.30 USD | `+15.09%` | -3,922,542.75 USD | `+1.26` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1683` | `0.1684` | `0.1508` | `0.1534` | `152,241,290` | 23,969,202.69 USD | -4,416,609.68 USD | `-18.43%` | -8,339,152.44 USD | `-4.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1534` | `0.1603` | `0.1528` | `0.1566` | `99,239,616` | 15,595,100.69 USD | 489,311.72 USD | `+3.14%` | -7,849,840.72 USD | `+0.82` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,374,542.78 USD | `-1.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,572,000.78 USD | `-0.89` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1566` | `251,480,907` | 39,564,303.38 USD | -3,927,297.97 USD | `-9.93%` | -7,499,298.75 USD | `-2.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1652` | `0.1687` | `0.1623` | `0.1631` | `68,085,678` | 11,252,816.65 USD | -909,329.92 USD | `-8.08%` | -705,420.63 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,136,414.44 USD | `-0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,374,542.78 USD | `-1.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,572,000.78 USD | `-0.89` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1566` | `251,480,907` | 39,564,303.38 USD | -3,927,297.97 USD | `-9.93%` | -7,499,298.75 USD | `-2.07` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:25:41 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1617` | 11,754.43 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 11.75K USD at 0.1617 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `0.1715` | 8,431.67 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale SELL: 8.43K USD at 0.1715 USD [API] | `2026-10-28 18:42:13` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.1785` (Vol: 158,900.00 USD, Dist: `+13.10%`) | Long MP=`0.1511` (Vol: 173,700.00 USD, Dist: `--4.26%`)
  * 48H Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+13.06%`) | Long MP=`0.1510` (Vol: 141,400.00 USD, Dist: `--4.33%`)
  * 3D Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+13.06%`) | Long MP=`0.1510` (Vol: 141,400.00 USD, Dist: `--4.33%`)
  * 7D Horizon: Short MP=`0.1791` (Vol: 196,100.00 USD, Dist: `+13.51%`) | Long MP=`0.1511` (Vol: 173,700.00 USD, Dist: `--4.27%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0385` | 1,490.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 1,630.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 170.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0435` | 2,350.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0445` | 156,480.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0465` | 278.62 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 9,700.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 109.52 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 1,860.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 622.79 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 289.43 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0535` | 479.20 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 3,360.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0555` | 463.38 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 15,650.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 3,740.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 730.84 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 7,510.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 655.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 6,770.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 99,790.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 313.22 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 143.87 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 2,970.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 5,840.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 111.58 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,440.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 664.76 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 2,320.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 14,690.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 973.20 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 10,650.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 4,630.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 2,480.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 18,190.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 185.57 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 627.22 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 19,460.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 514.04 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 2,890.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 372.25 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 2,040.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 98,990.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 1,510.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 5,100.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 9,870.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 145.24 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 28,030.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 12,040.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 1,850.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1015` | 10,540.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 773.66 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,530.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 9,820.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 6,860.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 181.20 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 2,230.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 2,200.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 863.60 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 813.89 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 425.50 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 3,850.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 10,210.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 8,840.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 8,930.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 7,840.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 34,090.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 4,880.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 12,580.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 1,530.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 34,400.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 467.81 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 4,850.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 870.65 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 4,190.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 9,780.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 4,010.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 15,950.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 3,930.00 USD | 999,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 6,620.00 USD | 995,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 9,690.00 USD | 988,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1336` | 3,040,000.00 USD | 3,040,000.00 USD | 3,580.00 USD | 5,990.00 USD | 16,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1340` | 3,010,000.00 USD | 3,010,000.00 USD | 9,160.00 USD | 7,730.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1342` | 2,300,000.00 USD | 2,300,000.00 USD | 830.00 USD | 918.48 USD | 3,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1344` | 2,970,000.00 USD | 2,970,000.00 USD | 6,410.00 USD | 5,790.00 USD | 19,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1345` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 691.54 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1345` | 158.59 USD | 979,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1348` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1348` | 2,940,000.00 USD | 2,940,000.00 USD | 31,170.00 USD | 7,150.00 USD | 23,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1351` | 2,290,000.00 USD | 2,290,000.00 USD | 6,820.00 USD | 2,050.00 USD | 5,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1352` | 2,870,000.00 USD | 2,870,000.00 USD | 11,390.00 USD | 6,290.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1354` | 2,280,000.00 USD | 2,280,000.00 USD | 2,670.00 USD | 688.99 USD | 4,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1355` | 3,760.00 USD | 979,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1356` | 2,830,000.00 USD | 2,830,000.00 USD | 16,150.00 USD | 12,180.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1357` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 2,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1360` | 2,260,000.00 USD | 2,260,000.00 USD | 2,480.00 USD | 869.31 USD | 4,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1360` | 2,790,000.00 USD | 2,790,000.00 USD | 25,240.00 USD | 8,630.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1363` | 2,260,000.00 USD | 2,260,000.00 USD | 4,890.00 USD | 2,360.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1364` | 2,750,000.00 USD | 2,750,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 79,260.00 USD | 975,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1366` | 2,250,000.00 USD | 2,250,000.00 USD | 1,340.00 USD | 484.70 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1368` | 2,730,000.00 USD | 2,730,000.00 USD | 4,500.00 USD | 7,610.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1369` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1372` | 2,240,000.00 USD | 2,240,000.00 USD | 5,470.00 USD | 1,110.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1372` | 2,710,000.00 USD | 2,710,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1375` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 2,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1375` | 24,260.00 USD | 896,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1378` | 2,230,000.00 USD | 2,230,000.00 USD | 936.88 USD | 1,590.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1380` | 2,710,000.00 USD | 2,710,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1381` | 2,230,000.00 USD | 2,230,000.00 USD | 5,890.00 USD | 7,190.00 USD | 11,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1384` | 2,200,000.00 USD | 2,200,000.00 USD | 10,450.00 USD | 2,890.00 USD | 15,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1384` | 2,690,000.00 USD | 2,690,000.00 USD | 11,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 7,490.00 USD | 871,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1387` | 2,180,000.00 USD | 2,180,000.00 USD | 33,240.00 USD | 2,090.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1388` | 2,680,000.00 USD | 2,680,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1390` | 2,140,000.00 USD | 2,140,000.00 USD | 5,190.00 USD | 1,970.00 USD | 1,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1392` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 4,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 7,980.00 USD | 864,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1396` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 6,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1396` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1399` | 2,120,000.00 USD | 2,120,000.00 USD | 5,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1400` | 2,640,000.00 USD | 2,640,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1402` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 2,100.00 USD | 995.35 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1404` | 2,630,000.00 USD | 2,630,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 1,250.00 USD | 856,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1411` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1415` | 11,550.00 USD | 855,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1416` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1420` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1423` | 2,110,000.00 USD | 2,110,000.00 USD | 4,030.00 USD | 2,310.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 484,730.00 USD | 843,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1432` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1435` | 2,100,000.00 USD | 2,100,000.00 USD | 3,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 19,330.00 USD | 358,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1436` | 2,600,000.00 USD | 2,600,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1438` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 3,590.00 USD | 20,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1440` | 2,560,000.00 USD | 2,560,000.00 USD | 13,180.00 USD | 5,260.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1441` | 2,070,000.00 USD | 2,070,000.00 USD | 17,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1444` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1444` | 2,540,000.00 USD | 2,540,000.00 USD | 3,450.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 6,510.00 USD | 339,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1452` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 5,660.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1453` | 2,050,000.00 USD | 2,050,000.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 18,480.00 USD | 332,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1456` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1460` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1464` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1465` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 3,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 28,260.00 USD | 314,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1468` | 2,040,000.00 USD | 2,040,000.00 USD | 12,090.00 USD | 2,700.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1468` | 2,490,000.00 USD | 2,490,000.00 USD | 9,720.00 USD | 9,180.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1471` | 2,020,000.00 USD | 2,020,000.00 USD | 4,400.00 USD | 5,970.00 USD | 1,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1472` | 2,470,000.00 USD | 2,470,000.00 USD | 19,180.00 USD | 0.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1474` | 2,010,000.00 USD | 2,010,000.00 USD | 17,930.00 USD | 9,630.00 USD | 27,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 74,850.00 USD | 286,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1476` | 2,430,000.00 USD | 2,430,000.00 USD | 68,180.00 USD | 20,180.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1477` | 1,960,000.00 USD | 1,960,000.00 USD | 102,190.00 USD | 16,230.00 USD | 35,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1480` | 1,800,000.00 USD | 1,800,000.00 USD | 54,050.00 USD | 17,450.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1480` | 2,340,000.00 USD | 2,340,000.00 USD | 50,400.00 USD | 43,810.00 USD | 50,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1483` | 1,720,000.00 USD | 1,720,000.00 USD | 17,530.00 USD | 4,230.00 USD | 11,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1484` | 2,200,000.00 USD | 2,200,000.00 USD | 47,020.00 USD | 16,640.00 USD | 43,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 20,690.00 USD | 211,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1486` | 1,690,000.00 USD | 1,690,000.00 USD | 13,550.00 USD | 0.00 USD | 9,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1488` | 2,090,000.00 USD | 2,090,000.00 USD | 24,980.00 USD | 10,470.00 USD | 25,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1489` | 1,670,000.00 USD | 1,670,000.00 USD | 6,740.00 USD | 7,050.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1492` | 1,650,000.00 USD | 1,650,000.00 USD | 24,480.00 USD | 8,610.00 USD | 8,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1492` | 2,030,000.00 USD | 2,030,000.00 USD | 40,320.00 USD | 21,590.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1495` | 1,610,000.00 USD | 1,610,000.00 USD | 18,450.00 USD | 5,270.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 31,670.00 USD | 190,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1496` | 1,930,000.00 USD | 1,930,000.00 USD | 34,650.00 USD | 18,690.00 USD | 17,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1498` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 347.81 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1500` | 1,860,000.00 USD | 1,860,000.00 USD | 60,500.00 USD | 9,610.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1501` | 1,580,000.00 USD | 1,580,000.00 USD | 6,280.00 USD | 0.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1504` | 1,570,000.00 USD | 1,570,000.00 USD | 21,400.00 USD | 15,920.00 USD | 55,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1504` | 1,770,000.00 USD | 1,770,000.00 USD | 20,410.00 USD | 19,520.00 USD | 44,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1505` | 113,080.00 USD | 158,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1507` | 1,480,000.00 USD | 1,480,000.00 USD | 83,340.00 USD | 28,420.00 USD | 62,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1508` | 1,680,000.00 USD | 1,680,000.00 USD | 152,330.00 USD | 16,820.00 USD | 104,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1510` | 1,310,000.00 USD | 1,310,000.00 USD | 188,120.00 USD | 9,010.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1512` | 1,410,000.00 USD | 1,410,000.00 USD | 86,820.00 USD | 13,310.00 USD | 59,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1513` | 1,110,000.00 USD | 1,110,000.00 USD | 25,970.00 USD | 5,200.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 45,890.00 USD | 45,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1516` | 1,070,000.00 USD | 1,070,000.00 USD | 10,070.00 USD | 8,340.00 USD | 17,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1516` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 13,330.00 USD | 61,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1519` | 1,040,000.00 USD | 1,040,000.00 USD | 14,340.00 USD | 2,630.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1520` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 22,090.00 USD | 87,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1522` | 1,000,000.00 USD | 1,000,000.00 USD | 38,050.00 USD | 4,440.00 USD | 5,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1524` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 13,950.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1525` | 956,560.00 USD | 956,560.00 USD | 0.00 USD | 0.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1528` | 948,240.00 USD | 948,240.00 USD | 0.00 USD | 0.00 USD | 5,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1528` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 33,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1532` | 1,010,000.00 USD | 1,010,000.00 USD | 38,390.00 USD | 17,260.00 USD | 51,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1534` | 943,100.00 USD | 943,100.00 USD | 0.00 USD | 8,980.00 USD | 50,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1536` | 901,570.00 USD | 901,570.00 USD | 0.00 USD | 8,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1537` | 883,310.00 USD | 883,310.00 USD | 44,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1540` | 893,000.00 USD | 893,000.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1544` | 874,780.00 USD | 874,780.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1548` | 871,180.00 USD | 871,180.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1549` | 839,110.00 USD | 839,110.00 USD | 0.00 USD | 17,000.00 USD | 33,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1552` | 788,980.00 USD | 788,980.00 USD | 0.00 USD | 2,500.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1552` | 868,320.00 USD | 868,320.00 USD | 0.00 USD | 11,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1555` | 782,590.00 USD | 782,590.00 USD | 0.00 USD | 0.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1558` | 775,400.00 USD | 775,400.00 USD | 0.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1560` | 856,500.00 USD | 856,500.00 USD | 0.00 USD | 10,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1561` | 762,540.00 USD | 762,540.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1564` | 757,570.00 USD | 757,570.00 USD | 3,130.00 USD | 13,270.00 USD | 165,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1564` | 845,520.00 USD | 845,520.00 USD | 101,070.00 USD | 33,750.00 USD | 103,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1565` | 354.32 USD | 354.32 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1567` | 575,470.00 USD | 575,470.00 USD | 159,670.00 USD | 32,420.00 USD | 19,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1568` | 607,360.00 USD | 607,360.00 USD | 137,880.00 USD | 15,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1570` | 363,470.00 USD | 363,470.00 USD | 181,880.00 USD | 12,360.00 USD | 64,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1572` | 454,120.00 USD | 454,120.00 USD | 187,220.00 USD | 39,540.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1573` | 104,490.00 USD | 104,490.00 USD | 78,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1575` | 2,270.00 USD | 2,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1576` | 25,970.00 USD | 25,970.00 USD | 25,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1576` | 168,520.00 USD | 168,520.00 USD | 44,680.00 USD | 123,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1580` | 231,030.00 USD | 231,030.00 USD | 129,940.00 USD | 101,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1584` | 354,850.00 USD | 354,850.00 USD | 80,450.00 USD | 43,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1585` | 39,220.00 USD | 39,220.00 USD | 28,600.00 USD | 2,370.00 USD | 8,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1588` | 98,800.00 USD | 98,800.00 USD | 15,100.00 USD | 28,750.00 USD | 15,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1588` | 468,620.00 USD | 468,620.00 USD | 69,180.00 USD | 44,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1591` | 152,310.00 USD | 152,310.00 USD | 0.00 USD | 26,120.00 USD | 27,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1592` | 533,250.00 USD | 533,250.00 USD | 0.00 USD | 64,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1596` | 631,780.00 USD | 631,780.00 USD | 0.00 USD | 98,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1600` | 692,490.00 USD | 692,490.00 USD | 0.00 USD | 60,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1603` | 216,400.00 USD | 216,400.00 USD | 64,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1604` | 1,240,000.00 USD | 1,240,000.00 USD | 163,960.00 USD | 112,090.00 USD | 273,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1605` | 4,930.00 USD | 7,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1606` | 244,040.00 USD | 244,040.00 USD | 27,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1608` | 1,860,000.00 USD | 1,860,000.00 USD | 208,080.00 USD | 240,680.00 USD | 172,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1609` | 278,220.00 USD | 278,220.00 USD | 0.00 USD | 0.00 USD | 34,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1612` | 404,140.00 USD | 404,140.00 USD | 20,140.00 USD | 11,530.00 USD | 94,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1612` | 2,780,000.00 USD | 2,780,000.00 USD | 304,970.00 USD | 328,050.00 USD | 287,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1615` | 429,470.00 USD | 429,470.00 USD | 14,300.00 USD | 0.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1616` | 3,320,000.00 USD | 3,320,000.00 USD | 293,210.00 USD | 131,180.00 USD | 108,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1618` | 495,240.00 USD | 495,240.00 USD | 53,600.00 USD | 12,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1620` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 196,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1621` | 660,870.00 USD | 660,870.00 USD | 92,470.00 USD | 73,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1624` | 770,820.00 USD | 770,820.00 USD | 50,280.00 USD | 59,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1624` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 193,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1625` | 8,640.00 USD | 16,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1627` | 796,690.00 USD | 796,690.00 USD | 25,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1628` | 3,890,000.00 USD | 3,890,000.00 USD | 76,780.00 USD | 0.00 USD | 103,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1630` | 916,280.00 USD | 916,280.00 USD | 0.00 USD | 17,970.00 USD | 101,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1633` | 1,010,000.00 USD | 1,010,000.00 USD | 88,400.00 USD | 6,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1635` | 9,360.00 USD | 25,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1636` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 19,990.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1636` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 13,670.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1639` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 13,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1640` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1642` | 1,120,000.00 USD | 1,120,000.00 USD | 19,180.00 USD | 36,980.00 USD | 16,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1644` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 8,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1645` | 1,150,000.00 USD | 1,150,000.00 USD | 14,950.00 USD | 11,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1645` | 2,060.00 USD | 27,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1648` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1654` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1656` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 31,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1657` | 1,220,000.00 USD | 1,220,000.00 USD | 9,730.00 USD | 55,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1660` | 1,290,000.00 USD | 1,290,000.00 USD | 8,220.00 USD | 11,150.00 USD | 50,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1660` | 4,140,000.00 USD | 4,140,000.00 USD | 79,170.00 USD | 11,020.00 USD | 51,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1663` | 1,400,000.00 USD | 1,400,000.00 USD | 44,200.00 USD | 14,550.00 USD | 44,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1664` | 4,400,000.00 USD | 4,400,000.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1666` | 1,500,000.00 USD | 1,500,000.00 USD | 22,170.00 USD | 5,340.00 USD | 78,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1668` | 4,580,000.00 USD | 4,580,000.00 USD | 42,580.00 USD | 52,290.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1672` | 1,550,000.00 USD | 1,550,000.00 USD | 46,590.00 USD | 2,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1672` | 4,780,000.00 USD | 4,780,000.00 USD | 135,250.00 USD | 62,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1675` | 1,590,000.00 USD | 1,590,000.00 USD | 20,040.00 USD | 1,990.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1676` | 5,000,000.00 USD | 5,000,000.00 USD | 84,020.00 USD | 141,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1678` | 1,620,000.00 USD | 1,620,000.00 USD | 22,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1680` | 5,220,000.00 USD | 5,220,000.00 USD | 121,860.00 USD | 80,270.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1681` | 1,740,000.00 USD | 1,740,000.00 USD | 120,850.00 USD | 4,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1684` | 1,850,000.00 USD | 1,850,000.00 USD | 54,020.00 USD | 26,600.00 USD | 32,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1684` | 5,300,000.00 USD | 5,300,000.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1687` | 1,890,000.00 USD | 1,890,000.00 USD | 6,560.00 USD | 5,840.00 USD | 23,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1688` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1690` | 1,930,000.00 USD | 1,930,000.00 USD | 18,380.00 USD | 9,870.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1692` | 5,460,000.00 USD | 5,460,000.00 USD | 33,660.00 USD | 70,740.00 USD | 40,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1693` | 2,100,000.00 USD | 2,100,000.00 USD | 84,630.00 USD | 74,940.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1695` | 394.60 USD | 28,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1696` | 2,150,000.00 USD | 2,150,000.00 USD | 23,530.00 USD | 16,310.00 USD | 6,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1696` | 5,600,000.00 USD | 5,600,000.00 USD | 17,360.00 USD | 87,350.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1699` | 2,230,000.00 USD | 2,230,000.00 USD | 26,000.00 USD | 56,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1700` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 25,330.00 USD | 41,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1702` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1704` | 5,770,000.00 USD | 5,770,000.00 USD | 55,170.00 USD | 46,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1705` | 2,280,000.00 USD | 2,280,000.00 USD | 14,190.00 USD | 20,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1708` | 2,400,000.00 USD | 2,400,000.00 USD | 39,520.00 USD | 65,470.00 USD | 13,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1708` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1711` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 4,910.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1714` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 12,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1716` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 42,020.00 USD | 15,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1717` | 2,490,000.00 USD | 2,490,000.00 USD | 9,570.00 USD | 34,120.00 USD | 19,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1720` | 2,570,000.00 USD | 2,570,000.00 USD | 80,090.00 USD | 1,590.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1720` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 161,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1723` | 2,710,000.00 USD | 2,710,000.00 USD | 54,130.00 USD | 16,860.00 USD | 66,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1724` | 6,400,000.00 USD | 6,400,000.00 USD | 118,060.00 USD | 0.00 USD | 208,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1726` | 2,730,000.00 USD | 2,730,000.00 USD | 8,230.00 USD | 2,410.00 USD | 12,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1729` | 2,750,000.00 USD | 2,750,000.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1732` | 2,770,000.00 USD | 2,770,000.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1732` | 6,890,000.00 USD | 6,890,000.00 USD | 476,430.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1735` | 2,790,000.00 USD | 2,790,000.00 USD | 14,970.00 USD | 9,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1738` | 2,820,000.00 USD | 2,820,000.00 USD | 18,610.00 USD | 2,310.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1740` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 0.00 USD | 83,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1741` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 1,600.00 USD | 5,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1744` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 2,460.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1744` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1747` | 2,880,000.00 USD | 2,880,000.00 USD | 8,530.00 USD | 0.00 USD | 31,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1748` | 7,070,000.00 USD | 7,070,000.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1750` | 2,990,000.00 USD | 2,990,000.00 USD | 80,070.00 USD | 2,280.00 USD | 22,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1752` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 0.00 USD | 291,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1753` | 3,060,000.00 USD | 3,060,000.00 USD | 32,240.00 USD | 0.00 USD | 33,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1756` | 3,180,000.00 USD | 3,180,000.00 USD | 23,610.00 USD | 27,640.00 USD | 73,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1756` | 7,660,000.00 USD | 7,660,000.00 USD | 112,930.00 USD | 0.00 USD | 186,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1759` | 3,330,000.00 USD | 3,330,000.00 USD | 85,450.00 USD | 31,960.00 USD | 36,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1760` | 8,050,000.00 USD | 8,050,000.00 USD | 277,910.00 USD | 77,870.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1762` | 3,560,000.00 USD | 3,560,000.00 USD | 72,450.00 USD | 83,100.00 USD | 66,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1764` | 8,720,000.00 USD | 8,720,000.00 USD | 353,950.00 USD | 270,450.00 USD | 40,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1765` | 3,650,000.00 USD | 3,650,000.00 USD | 20,220.00 USD | 28,990.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1765` | 3,240.00 USD | 31,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1768` | 3,810,000.00 USD | 3,810,000.00 USD | 19,860.00 USD | 83,210.00 USD | 62,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1768` | 9,090,000.00 USD | 9,090,000.00 USD | 191,690.00 USD | 154,100.00 USD | 31,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1771` | 3,900,000.00 USD | 3,900,000.00 USD | 43,430.00 USD | 19,520.00 USD | 24,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1772` | 9,370,000.00 USD | 9,370,000.00 USD | 98,390.00 USD | 153,480.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1774` | 3,980,000.00 USD | 3,980,000.00 USD | 20,200.00 USD | 30,630.00 USD | 26,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1776` | 9,610,000.00 USD | 9,610,000.00 USD | 186,770.00 USD | 59,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1777` | 4,130,000.00 USD | 4,130,000.00 USD | 42,080.00 USD | 81,500.00 USD | 24,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1780` | 4,160,000.00 USD | 4,160,000.00 USD | 11,580.00 USD | 9,760.00 USD | 13,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1780` | 9,870,000.00 USD | 9,870,000.00 USD | 52,730.00 USD | 46,410.00 USD | 157,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1783` | 4,230,000.00 USD | 4,230,000.00 USD | 27,640.00 USD | 15,680.00 USD | 19,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1784` | 10,100,000.00 USD | 10,100,000.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1786` | 4,280,000.00 USD | 4,280,000.00 USD | 16,960.00 USD | 31,510.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1788` | 10,260,000.00 USD | 10,260,000.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1789` | 4,350,000.00 USD | 4,350,000.00 USD | 15,890.00 USD | 31,190.00 USD | 20,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1792` | 4,390,000.00 USD | 4,390,000.00 USD | 13,950.00 USD | 16,470.00 USD | 18,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1792` | 10,500,000.00 USD | 10,500,000.00 USD | 182,810.00 USD | 46,960.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1795` | 4,520,000.00 USD | 4,520,000.00 USD | 53,160.00 USD | 48,930.00 USD | 18,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1795` | 525.67 USD | 31,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1796` | 10,590,000.00 USD | 10,590,000.00 USD | 17,130.00 USD | 26,110.00 USD | 44,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1798` | 4,570,000.00 USD | 4,570,000.00 USD | 15,420.00 USD | 17,120.00 USD | 25,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1800` | 10,710,000.00 USD | 10,710,000.00 USD | 12,940.00 USD | 34,680.00 USD | 73,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1801` | 4,620,000.00 USD | 4,620,000.00 USD | 12,470.00 USD | 23,820.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1804` | 4,670,000.00 USD | 4,670,000.00 USD | 10,530.00 USD | 16,830.00 USD | 19,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1804` | 10,800,000.00 USD | 10,800,000.00 USD | 35,280.00 USD | 32,850.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1807` | 4,710,000.00 USD | 4,710,000.00 USD | 16,640.00 USD | 17,460.00 USD | 9,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1808` | 10,970,000.00 USD | 10,970,000.00 USD | 35,050.00 USD | 67,250.00 USD | 73,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1810` | 4,750,000.00 USD | 4,750,000.00 USD | 12,880.00 USD | 15,840.00 USD | 8,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1812` | 11,120,000.00 USD | 11,120,000.00 USD | 64,990.00 USD | 29,900.00 USD | 50,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1813` | 4,820,000.00 USD | 4,820,000.00 USD | 14,660.00 USD | 37,850.00 USD | 15,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1816` | 4,850,000.00 USD | 4,850,000.00 USD | 13,550.00 USD | 0.00 USD | 15,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1816` | 11,260,000.00 USD | 11,260,000.00 USD | 69,700.00 USD | 33,940.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1819` | 4,870,000.00 USD | 4,870,000.00 USD | 6,740.00 USD | 12,120.00 USD | 6,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1820` | 11,420,000.00 USD | 11,420,000.00 USD | 65,350.00 USD | 54,880.00 USD | 43,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1822` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 21,610.00 USD | 1,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1824` | 11,640,000.00 USD | 11,640,000.00 USD | 80,350.00 USD | 17,880.00 USD | 112,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1825` | 4,930,000.00 USD | 4,930,000.00 USD | 18,910.00 USD | 1,780.00 USD | 11,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1828` | 4,940,000.00 USD | 4,940,000.00 USD | 6,840.00 USD | 5,270.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1828` | 11,810,000.00 USD | 11,810,000.00 USD | 79,610.00 USD | 29,630.00 USD | 69,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1831` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 2,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1832` | 12,030,000.00 USD | 12,030,000.00 USD | 108,540.00 USD | 31,590.00 USD | 74,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1834` | 4,960,000.00 USD | 4,960,000.00 USD | 2,670.00 USD | 0.00 USD | 5,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1836` | 12,360,000.00 USD | 12,360,000.00 USD | 172,660.00 USD | 110,870.00 USD | 52,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1837` | 4,960,000.00 USD | 4,960,000.00 USD | 3,610.00 USD | 2,640.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1840` | 4,980,000.00 USD | 4,980,000.00 USD | 5,430.00 USD | 1,970.00 USD | 12,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1840` | 12,710,000.00 USD | 12,710,000.00 USD | 141,620.00 USD | 50,840.00 USD | 151,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1843` | 4,990,000.00 USD | 4,990,000.00 USD | 1,030.00 USD | 3,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1844` | 12,910,000.00 USD | 12,910,000.00 USD | 94,510.00 USD | 20,390.00 USD | 82,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1845` | 752.59 USD | 32,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1846` | 5,010,000.00 USD | 5,010,000.00 USD | 9,830.00 USD | 1,840.00 USD | 7,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1848` | 13,050,000.00 USD | 13,050,000.00 USD | 35,280.00 USD | 69,910.00 USD | 41,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1849` | 5,030,000.00 USD | 5,030,000.00 USD | 12,130.00 USD | 5,200.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1852` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 2,580.00 USD | 1,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1852` | 13,500,000.00 USD | 13,500,000.00 USD | 168,270.00 USD | 28,290.00 USD | 251,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1855` | 5,040,000.00 USD | 5,040,000.00 USD | 7,630.00 USD | 0.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1856` | 13,730,000.00 USD | 13,730,000.00 USD | 100,160.00 USD | 21,030.00 USD | 106,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1858` | 5,070,000.00 USD | 5,070,000.00 USD | 10,290.00 USD | 4,100.00 USD | 14,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1860` | 13,970,000.00 USD | 13,970,000.00 USD | 64,600.00 USD | 48,330.00 USD | 127,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1861` | 5,090,000.00 USD | 5,090,000.00 USD | 5,860.00 USD | 2,970.00 USD | 5,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1864` | 5,090,000.00 USD | 5,090,000.00 USD | 1,870.00 USD | 0.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1864` | 14,120,000.00 USD | 14,120,000.00 USD | 48,260.00 USD | 44,140.00 USD | 61,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1867` | 5,110,000.00 USD | 5,110,000.00 USD | 3,300.00 USD | 0.00 USD | 8,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1868` | 14,370,000.00 USD | 14,370,000.00 USD | 133,990.00 USD | 51,510.00 USD | 56,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1870` | 5,120,000.00 USD | 5,120,000.00 USD | 4,960.00 USD | 5,040.00 USD | 8,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1872` | 14,860,000.00 USD | 14,860,000.00 USD | 188,990.00 USD | 146,600.00 USD | 155,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1873` | 5,140,000.00 USD | 5,140,000.00 USD | 14,310.00 USD | 1,900.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1876` | 14,990,000.00 USD | 14,990,000.00 USD | 65,910.00 USD | 23,180.00 USD | 43,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1880` | 15,110,000.00 USD | 15,110,000.00 USD | 57,250.00 USD | 35,940.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1884` | 15,170,000.00 USD | 15,170,000.00 USD | 14,000.00 USD | 35,430.00 USD | 9,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1888` | 15,290,000.00 USD | 15,290,000.00 USD | 22,970.00 USD | 4,800.00 USD | 88,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1892` | 15,380,000.00 USD | 15,380,000.00 USD | 49,980.00 USD | 2,860.00 USD | 34,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1896` | 15,450,000.00 USD | 15,450,000.00 USD | 42,320.00 USD | 11,820.00 USD | 18,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1900` | 15,500,000.00 USD | 15,500,000.00 USD | 0.00 USD | 29,650.00 USD | 20,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1904` | 15,540,000.00 USD | 15,540,000.00 USD | 14,330.00 USD | 17,690.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1908` | 15,670,000.00 USD | 15,670,000.00 USD | 33,940.00 USD | 44,480.00 USD | 52,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1912` | 15,690,000.00 USD | 15,690,000.00 USD | 0.00 USD | 9,380.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1916` | 15,720,000.00 USD | 15,720,000.00 USD | 7,460.00 USD | 12,040.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1920` | 15,730,000.00 USD | 15,730,000.00 USD | 0.00 USD | 5,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1924` | 15,750,000.00 USD | 15,750,000.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1928` | 15,770,000.00 USD | 15,770,000.00 USD | 11,600.00 USD | 7,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1944` | 15,770,000.00 USD | 15,770,000.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1945` | 623.68 USD | 33,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1952` | 15,780,000.00 USD | 15,780,000.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1955` | 860.20 USD | 34,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1956` | 15,790,000.00 USD | 15,790,000.00 USD | 4,860.00 USD | 2,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1960` | 15,800,000.00 USD | 15,800,000.00 USD | 5,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1964` | 15,820,000.00 USD | 15,820,000.00 USD | 6,470.00 USD | 2,700.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1975` | 150.10 USD | 34,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1995` | 135.22 USD | 34,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2055` | 11,590.00 USD | 45,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2085` | 198.08 USD | 46,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2095` | 164.23 USD | 46,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2135` | 16,070.00 USD | 62,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 41,330.00 USD | 103,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2185` | 26,000.00 USD | 129,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2195` | 87,800.00 USD | 217,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 229.15 USD | 217,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2255` | 271.01 USD | 217,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2265` | 26,840.00 USD | 244,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 6,820.00 USD | 251,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 16,250.00 USD | 267,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 47,600.00 USD | 315,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 361.66 USD | 315,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 796.25 USD | 316,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2445` | 231.03 USD | 316,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2465` | 9,360.00 USD | 326,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2485` | 394.92 USD | 326,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2545` | 546.54 USD | 327,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 3,870.00 USD | 331,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2575` | 28,910.00 USD | 359,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 52,620.00 USD | 412,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 154.94 USD | 412,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2675` | 790.30 USD | 413,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2685` | 226.51 USD | 413,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 13,510.00 USD | 427,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 214.21 USD | 427,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 27,890.00 USD | 455,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2795` | 482.84 USD | 455,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2885` | 16,960.00 USD | 472,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 2,810.00 USD | 475,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 1,040.00 USD | 476,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3015` | 2,290.00 USD | 478,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0385` | 1,770,000.00 USD | 0.00 USD | 1,490.00 USD | `-74.90%` | `38,823,900,000,000.00` |
| `Live` | `Long` | `0.0415` | 1,770,000.00 USD | 0.00 USD | 1,630.00 USD | `-72.94%` | `39,298,600,000,000.00` |
| `Live` | `Long` | `0.0425` | 1,760,000.00 USD | 0.00 USD | 170.00 USD | `-72.29%` | `4,000,000,000,000.00` |
| `Live` | `Long` | `0.0435` | 1,760,000.00 USD | 0.00 USD | 2,350.00 USD | `-71.64%` | `53,914,500,000,000.00` |
| `Live` | `Long` | `0.0445` | 1,760,000.00 USD | 0.00 USD | 156,480.00 USD | `-70.98%` | `3,516,409,800,000,000.00` |
| `Live` | `Long` | `0.0465` | 1,610,000.00 USD | 0.00 USD | 278.62 USD | `-69.68%` | `5,991,900,000,000.00` |
| `Live` | `Long` | `0.0485` | 1,600,000.00 USD | 0.00 USD | 9,700.00 USD | `-68.38%` | `200,000,000,000,000.00` |
| `Live` | `Long` | `0.0495` | 1,600,000.00 USD | 0.00 USD | 109.52 USD | `-67.72%` | `2,212,600,000,000.00` |
| `Live` | `Long` | `0.0505` | 1,590,000.00 USD | 0.00 USD | 1,860.00 USD | `-67.07%` | `36,813,100,000,000.00` |
| `Live` | `Long` | `0.0515` | 1,590,000.00 USD | 0.00 USD | 622.79 USD | `-66.42%` | `12,093,000,000,000.00` |
| `Live` | `Long` | `0.0525` | 1,590,000.00 USD | 0.00 USD | 289.43 USD | `-65.77%` | `5,513,000,000,000.00` |
| `Live` | `Long` | `0.0535` | 1,590,000.00 USD | 0.00 USD | 479.20 USD | `-65.11%` | `8,957,000,000,000.00` |
| `Live` | `Long` | `0.0545` | 1,590,000.00 USD | 0.00 USD | 3,360.00 USD | `-64.46%` | `61,635,000,000,000.00` |
| `Live` | `Long` | `0.0555` | 1,590,000.00 USD | 0.00 USD | 463.38 USD | `-63.81%` | `8,349,200,000,000.00` |
| `Live` | `Long` | `0.0565` | 1,590,000.00 USD | 0.00 USD | 15,650.00 USD | `-63.16%` | `276,984,000,000,000.00` |
| `Live` | `Long` | `0.0575` | 1,570,000.00 USD | 0.00 USD | 3,740.00 USD | `-62.51%` | `65,000,000,000,000.00` |
| `Live` | `Long` | `0.0585` | 1,570,000.00 USD | 0.00 USD | 730.84 USD | `-61.85%` | `12,493,000,000,000.00` |
| `Live` | `Long` | `0.0605` | 1,570,000.00 USD | 0.00 USD | 7,510.00 USD | `-60.55%` | `124,110,700,000,000.00` |
| `Live` | `Long` | `0.0655` | 1,560,000.00 USD | 0.00 USD | 655.00 USD | `-57.29%` | `10,000,000,000,000.00` |
| `Live` | `Long` | `0.0665` | 1,560,000.00 USD | 0.00 USD | 6,770.00 USD | `-56.64%` | `101,831,000,000,000.00` |
| `Live` | `Long` | `0.0675` | 1,550,000.00 USD | 0.00 USD | 99,790.00 USD | `-55.99%` | `1,478,385,900,000,000.00` |
| `Live` | `Long` | `0.0685` | 1,450,000.00 USD | 0.00 USD | 313.22 USD | `-55.33%` | `4,572,600,000,000.00` |
| `Live` | `Long` | `0.0695` | 1,450,000.00 USD | 0.00 USD | 143.87 USD | `-54.68%` | `2,070,000,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,450,000.00 USD | 0.00 USD | 2,970.00 USD | `-54.03%` | `42,142,800,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,450,000.00 USD | 0.00 USD | 5,840.00 USD | `-53.38%` | `81,674,400,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,440,000.00 USD | 0.00 USD | 111.58 USD | `-52.73%` | `1,539,100,000,000.00` |
| `Live` | `Long` | `0.0735` | 1,440,000.00 USD | 0.00 USD | 2,440.00 USD | `-52.07%` | `33,161,800,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,440,000.00 USD | 0.00 USD | 664.76 USD | `-51.42%` | `8,923,000,000,000.00` |
| `Live` | `Long` | `0.0755` | 1,440,000.00 USD | 0.00 USD | 2,320.00 USD | `-50.77%` | `30,720,900,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,440,000.00 USD | 0.00 USD | 14,690.00 USD | `-50.12%` | `192,029,300,000,000.00` |
| `Live` | `Long` | `0.0775` | 1,420,000.00 USD | 0.00 USD | 973.20 USD | `-49.47%` | `12,557,400,000,000.00` |
| `Live` | `Long` | `0.0785` | 1,420,000.00 USD | 0.00 USD | 10,650.00 USD | `-48.81%` | `135,660,000,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,410,000.00 USD | 0.00 USD | 4,630.00 USD | `-48.16%` | `58,261,800,000,000.00` |
| `Live` | `Long` | `0.0815` | 1,410,000.00 USD | 0.00 USD | 2,480.00 USD | `-46.86%` | `30,424,100,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,400,000.00 USD | 0.00 USD | 18,190.00 USD | `-46.21%` | `220,497,300,000,000.00` |
| `Live` | `Long` | `0.0835` | 1,390,000.00 USD | 0.00 USD | 185.57 USD | `-45.55%` | `2,222,400,000,000.00` |
| `Live` | `Long` | `0.0845` | 1,390,000.00 USD | 0.00 USD | 627.22 USD | `-44.90%` | `7,422,700,000,000.00` |
| `Live` | `Long` | `0.0865` | 1,390,000.00 USD | 0.00 USD | 19,460.00 USD | `-43.60%` | `224,937,400,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,370,000.00 USD | 0.00 USD | 514.04 USD | `-42.29%` | `5,808,400,000,000.00` |
| `Live` | `Long` | `0.0895` | 1,370,000.00 USD | 0.00 USD | 2,890.00 USD | `-41.64%` | `32,316,000,000,000.00` |
| `Live` | `Long` | `0.0915` | 1,360,000.00 USD | 0.00 USD | 372.25 USD | `-40.34%` | `4,068,300,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,360,000.00 USD | 0.00 USD | 2,040.00 USD | `-39.68%` | `22,044,300,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,360,000.00 USD | 0.00 USD | 98,990.00 USD | `-39.03%` | `1,058,708,500,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,260,000.00 USD | 0.00 USD | 1,510.00 USD | `-38.38%` | `16,031,700,000,000.00` |
| `Live` | `Long` | `0.0955` | 1,260,000.00 USD | 0.00 USD | 5,100.00 USD | `-37.73%` | `53,365,600,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,250,000.00 USD | 0.00 USD | 9,870.00 USD | `-37.08%` | `102,309,800,000,000.00` |
| `Live` | `Long` | `0.0975` | 1,250,000.00 USD | 0.00 USD | 145.24 USD | `-36.42%` | `1,489,600,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,240,000.00 USD | 0.00 USD | 28,030.00 USD | `-35.77%` | `284,524,200,000,000.00` |
| `Live` | `Long` | `0.0995` | 1,220,000.00 USD | 0.00 USD | 12,040.00 USD | `-35.12%` | `120,971,400,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,200,000.00 USD | 0.00 USD | 1,850.00 USD | `-34.47%` | `18,436,400,000,000.00` |
| `Live` | `Long` | `0.1015` | 1,200,000.00 USD | 0.00 USD | 10,540.00 USD | `-33.82%` | `103,888,900,000,000.00` |
| `Live` | `Long` | `0.1025` | 1,190,000.00 USD | 0.00 USD | 773.66 USD | `-33.16%` | `7,547,900,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,190,000.00 USD | 0.00 USD | 1,530.00 USD | `-32.51%` | `14,822,500,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,190,000.00 USD | 0.00 USD | 9,820.00 USD | `-31.86%` | `94,015,100,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,180,000.00 USD | 0.00 USD | 6,860.00 USD | `-31.21%` | `65,046,300,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,170,000.00 USD | 0.00 USD | 181.20 USD | `-30.56%` | `1,701,400,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,170,000.00 USD | 0.00 USD | 2,230.00 USD | `-29.90%` | `20,784,700,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,170,000.00 USD | 0.00 USD | 2,200.00 USD | `-29.25%` | `20,256,400,000,000.00` |
| `Live` | `Long` | `0.1095` | 1,170,000.00 USD | 0.00 USD | 863.60 USD | `-28.60%` | `7,886,800,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,170,000.00 USD | 0.00 USD | 813.89 USD | `-27.95%` | `7,365,500,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,170,000.00 USD | 0.00 USD | 425.50 USD | `-27.30%` | `3,816,100,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,170,000.00 USD | 0.00 USD | 3,850.00 USD | `-25.99%` | `33,939,200,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,160,000.00 USD | 0.00 USD | 10,210.00 USD | `-25.34%` | `89,203,000,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,150,000.00 USD | 0.00 USD | 8,840.00 USD | `-24.69%` | `76,548,300,000,000.00` |
| `Live` | `Long` | `0.1165` | 1,140,000.00 USD | 0.00 USD | 8,930.00 USD | `-24.03%` | `76,688,500,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,130,000.00 USD | 0.00 USD | 7,840.00 USD | `-23.38%` | `66,738,200,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,130,000.00 USD | 0.00 USD | 34,090.00 USD | `-22.73%` | `287,694,900,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,090,000.00 USD | 0.00 USD | 4,880.00 USD | `-22.08%` | `40,848,300,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,090,000.00 USD | 0.00 USD | 12,580.00 USD | `-20.77%` | `103,541,000,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,080,000.00 USD | 0.00 USD | 1,530.00 USD | `-20.12%` | `12,465,900,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,070,000.00 USD | 0.00 USD | 34,400.00 USD | `-19.47%` | `278,503,500,000,000.00` |
| `Live` | `Long` | `0.1245` | 1,040,000.00 USD | 0.00 USD | 467.81 USD | `-18.82%` | `3,757,500,000,000.00` |
| `Live` | `Long` | `0.1255` | 1,040,000.00 USD | 0.00 USD | 4,850.00 USD | `-18.17%` | `38,646,100,000,000.00` |
| `Live` | `Long` | `0.1265` | 1,030,000.00 USD | 0.00 USD | 870.65 USD | `-17.51%` | `6,882,600,000,000.00` |
| `Live` | `Long` | `0.1275` | 1,030,000.00 USD | 0.00 USD | 4,190.00 USD | `-16.86%` | `32,824,800,000,000.00` |
| `Live` | `Long` | `0.1285` | 1,030,000.00 USD | 0.00 USD | 9,780.00 USD | `-16.21%` | `76,071,500,000,000.00` |
| `Live` | `Long` | `0.1295` | 1,020,000.00 USD | 0.00 USD | 4,010.00 USD | `-15.56%` | `30,998,800,000,000.00` |
| `Live` | `Long` | `0.1305` | 1,020,000.00 USD | 0.00 USD | 15,950.00 USD | `-14.91%` | `122,242,400,000,000.00` |
| `Live` | `Long` | `0.1315` | 999,430.00 USD | 0.00 USD | 3,930.00 USD | `-14.25%` | `29,871,600,000,000.00` |
| `Live` | `Long` | `0.1325` | 995,510.00 USD | 0.00 USD | 6,620.00 USD | `-13.60%` | `50,000,000,000,000.00` |
| `Live` | `Long` | `0.1335` | 988,880.00 USD | 0.00 USD | 9,690.00 USD | `-12.95%` | `72,616,800,000,000.00` |
| `Live` | `Long` | `0.1345` | 979,190.00 USD | 0.00 USD | 158.59 USD | `-12.30%` | `1,179,100,000,000.00` |
| `Live` | `Long` | `0.1355` | 979,030.00 USD | 0.00 USD | 3,760.00 USD | `-11.65%` | `27,775,500,000,000.00` |
| `Live` | `Long` | `0.1365` | 975,270.00 USD | 0.00 USD | 79,260.00 USD | `-10.99%` | `580,658,700,000,000.00` |
| `Live` | `Long` | `0.1375` | 896,010.00 USD | 0.00 USD | 24,260.00 USD | `-10.34%` | `176,463,000,000,000.00` |
| `Live` | `Long` | `0.1385` | 871,740.00 USD | 0.00 USD | 7,490.00 USD | `-9.69%` | `54,084,300,000,000.00` |
| `Live` | `Long` | `0.1395` | 864,250.00 USD | 0.00 USD | 7,980.00 USD | `-9.04%` | `57,175,800,000,000.00` |
| `Live` | `Long` | `0.1405` | 856,270.00 USD | 0.00 USD | 1,250.00 USD | `-8.39%` | `8,897,000,000,000.00` |
| `Live` | `Long` | `0.1415` | 855,020.00 USD | 0.00 USD | 11,550.00 USD | `-7.73%` | `81,618,300,000,000.00` |
| `Live` | `Long` | `0.1425` | 843,480.00 USD | 0.00 USD | 484,730.00 USD | `-7.08%` | `3,401,615,000,000,000.00` |
| `Live` | `Long` | `0.1435` | 358,750.00 USD | 0.00 USD | 19,330.00 USD | `-6.43%` | `134,671,900,000,000.00` |
| `Live` | `Long` | `0.1445` | 339,420.00 USD | 0.00 USD | 6,510.00 USD | `-5.78%` | `45,018,800,000,000.00` |
| `Live` | `Long` | `0.1455` | 332,920.00 USD | 0.00 USD | 18,480.00 USD | `-5.13%` | `126,976,400,000,000.00` |
| `Live` | `Long` | `0.1465` | 314,440.00 USD | 0.00 USD | 28,260.00 USD | `-4.47%` | `192,887,600,000,000.00` |
| `Live` | `Long` | `0.1475` | 286,180.00 USD | 0.00 USD | 74,850.00 USD | `-3.82%` | `507,483,300,000,000.00` |
| `Live` | `Long` | `0.1485` | 211,330.00 USD | 0.00 USD | 20,690.00 USD | `-3.17%` | `139,308,299,999,999.98` |
| `Live` | `Long` | `0.1495` | 190,640.00 USD | 0.00 USD | 31,670.00 USD | `-2.52%` | `211,828,000,000,000.00` |
| `Live` | `Long` | `0.1505` | 158,970.00 USD | 0.00 USD | 113,080.00 USD | `-1.86%` | `751,386,100,000,000.00` |
| `Live` | `Long` | `0.1515` | 45,890.00 USD | 0.00 USD | 45,890.00 USD | `-1.21%` | `302,898,000,000,000.00` |
| `Live` | `Short` | `0.1565` | 354.32 USD | 354.32 USD | 0.00 USD | `+2.05%` | `2,264,000,000,000.00` |
| `Live` | `Short` | `0.1575` | 2,630.00 USD | 2,270.00 USD | 0.00 USD | `+2.70%` | `14,425,500,000,000.00` |
| `Live` | `Short` | `0.1605` | 7,550.00 USD | 4,930.00 USD | 0.00 USD | `+4.66%` | `30,686,700,000,000.00` |
| `Live` | `Short` | `0.1625` | 16,190.00 USD | 8,640.00 USD | 0.00 USD | `+5.96%` | `53,166,300,000,000.00` |
| `Live` | `Short` | `0.1635` | 25,550.00 USD | 9,360.00 USD | 0.00 USD | `+6.61%` | `57,268,700,000,000.00` |
| `Live` | `Short` | `0.1645` | 27,620.00 USD | 2,060.00 USD | 0.00 USD | `+7.26%` | `12,547,200,000,000.00` |
| `Live` | `Short` | `0.1695` | 28,010.00 USD | 394.60 USD | 0.00 USD | `+10.52%` | `2,328,000,000,000.00` |
| `Live` | `Short` | `0.1765` | 31,260.00 USD | 3,240.00 USD | 0.00 USD | `+15.09%` | `18,375,600,000,000.00` |
| `Live` | `Short` | `0.1795` | 31,780.00 USD | 525.67 USD | 0.00 USD | `+17.04%` | `2,928,500,000,000.00` |
| `Live` | `Short` | `0.1845` | 32,530.00 USD | 752.59 USD | 0.00 USD | `+20.31%` | `4,079,100,000,000.00` |
| `Live` | `Short` | `0.1945` | 33,160.00 USD | 623.68 USD | 0.00 USD | `+26.83%` | `3,206,600,000,000.00` |
| `Live` | `Short` | `0.1955` | 34,020.00 USD | 860.20 USD | 0.00 USD | `+27.48%` | `4,400,000,000,000.00` |
| `Live` | `Short` | `0.1975` | 34,170.00 USD | 150.10 USD | 0.00 USD | `+28.78%` | `760,000,000,000.00` |
| `Live` | `Short` | `0.1995` | 34,300.00 USD | 135.22 USD | 0.00 USD | `+30.09%` | `677,800,000,000.00` |
| `Live` | `Short` | `0.2055` | 45,900.00 USD | 11,590.00 USD | 0.00 USD | `+34.00%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2085` | 46,090.00 USD | 198.08 USD | 0.00 USD | `+35.95%` | `950,000,000,000.00` |
| `Live` | `Short` | `0.2095` | 46,260.00 USD | 164.23 USD | 0.00 USD | `+36.61%` | `783,900,000,000.00` |
| `Live` | `Short` | `0.2135` | 62,330.00 USD | 16,070.00 USD | 0.00 USD | `+39.21%` | `75,287,100,000,000.00` |
| `Live` | `Short` | `0.2155` | 103,670.00 USD | 41,330.00 USD | 0.00 USD | `+40.52%` | `191,801,700,000,000.00` |
| `Live` | `Short` | `0.2185` | 129,660.00 USD | 26,000.00 USD | 0.00 USD | `+42.48%` | `118,989,500,000,000.00` |
| `Live` | `Short` | `0.2195` | 217,460.00 USD | 87,800.00 USD | 0.00 USD | `+43.13%` | `400,000,000,000,000.00` |
| `Live` | `Short` | `0.2235` | 217,690.00 USD | 229.15 USD | 0.00 USD | `+45.74%` | `1,025,300,000,000.00` |
| `Live` | `Short` | `0.2255` | 217,960.00 USD | 271.01 USD | 0.00 USD | `+47.04%` | `1,201,800,000,000.00` |
| `Live` | `Short` | `0.2265` | 244,800.00 USD | 26,840.00 USD | 0.00 USD | `+47.69%` | `118,481,200,000,000.00` |
| `Live` | `Short` | `0.2295` | 251,620.00 USD | 6,820.00 USD | 0.00 USD | `+49.65%` | `29,727,000,000,000.00` |
| `Live` | `Short` | `0.2355` | 267,880.00 USD | 16,250.00 USD | 0.00 USD | `+53.56%` | `69,017,500,000,000.00` |
| `Live` | `Short` | `0.2375` | 315,480.00 USD | 47,600.00 USD | 0.00 USD | `+54.86%` | `200,435,100,000,000.00` |
| `Live` | `Short` | `0.2405` | 315,840.00 USD | 361.66 USD | 0.00 USD | `+56.82%` | `1,503,800,000,000.00` |
| `Live` | `Short` | `0.2425` | 316,640.00 USD | 796.25 USD | 0.00 USD | `+58.12%` | `3,283,500,000,000.00` |
| `Live` | `Short` | `0.2445` | 316,870.00 USD | 231.03 USD | 0.00 USD | `+59.43%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2465` | 326,230.00 USD | 9,360.00 USD | 0.00 USD | `+60.73%` | `37,972,200,000,000.00` |
| `Live` | `Short` | `0.2485` | 326,620.00 USD | 394.92 USD | 0.00 USD | `+62.04%` | `1,589,200,000,000.00` |
| `Live` | `Short` | `0.2545` | 327,170.00 USD | 546.54 USD | 0.00 USD | `+65.95%` | `2,147,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 331,040.00 USD | 3,870.00 USD | 0.00 USD | `+67.25%` | `15,070,700,000,000.00` |
| `Live` | `Short` | `0.2575` | 359,950.00 USD | 28,910.00 USD | 0.00 USD | `+67.91%` | `112,272,400,000,000.00` |
| `Live` | `Short` | `0.2585` | 412,560.00 USD | 52,620.00 USD | 0.00 USD | `+68.56%` | `203,548,800,000,000.00` |
| `Live` | `Short` | `0.2615` | 412,720.00 USD | 154.94 USD | 0.00 USD | `+70.51%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2675` | 413,510.00 USD | 790.30 USD | 0.00 USD | `+74.43%` | `2,954,400,000,000.00` |
| `Live` | `Short` | `0.2685` | 413,740.00 USD | 226.51 USD | 0.00 USD | `+75.08%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2715` | 427,250.00 USD | 13,510.00 USD | 0.00 USD | `+77.03%` | `49,773,600,000,000.00` |
| `Live` | `Short` | `0.2725` | 427,460.00 USD | 214.21 USD | 0.00 USD | `+77.69%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 455,350.00 USD | 27,890.00 USD | 0.00 USD | `+78.99%` | `101,607,700,000,000.00` |
| `Live` | `Short` | `0.2795` | 455,840.00 USD | 482.84 USD | 0.00 USD | `+82.25%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2885` | 472,800.00 USD | 16,960.00 USD | 0.00 USD | `+88.12%` | `58,786,700,000,000.00` |
| `Live` | `Short` | `0.2915` | 475,610.00 USD | 2,810.00 USD | 0.00 USD | `+90.08%` | `9,642,400,000,000.00` |
| `Live` | `Short` | `0.2955` | 476,650.00 USD | 1,040.00 USD | 0.00 USD | `+92.68%` | `3,534,200,000,000.00` |
| `Live` | `Short` | `0.3015` | 478,950.00 USD | 2,290.00 USD | 0.00 USD | `+96.60%` | `7,608,100,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0355` | 527,370.00 USD | 0.00 USD | 355.00 USD | `-76.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 527,010.00 USD | 0.00 USD | 600.79 USD | `-72.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 526,410.00 USD | 0.00 USD | 353.50 USD | `-67.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 526,060.00 USD | 0.00 USD | 4,310.00 USD | `-63.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 521,750.00 USD | 0.00 USD | 475.11 USD | `-58.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 521,270.00 USD | 0.00 USD | 131.16 USD | `-57.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 521,140.00 USD | 0.00 USD | 881.45 USD | `-56.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 520,260.00 USD | 0.00 USD | 1,070.00 USD | `-55.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 519,190.00 USD | 0.00 USD | 1,400.00 USD | `-55.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 517,790.00 USD | 0.00 USD | 1,010.00 USD | `-54.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 516,780.00 USD | 0.00 USD | 4,100.00 USD | `-54.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 512,670.00 USD | 0.00 USD | 529.04 USD | `-53.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 512,150.00 USD | 0.00 USD | 2,390.00 USD | `-52.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 509,760.00 USD | 0.00 USD | 757.39 USD | `-50.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 509,000.00 USD | 0.00 USD | 1,490.00 USD | `-48.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 507,510.00 USD | 0.00 USD | 277.37 USD | `-43.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 507,240.00 USD | 0.00 USD | 262.50 USD | `-42.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 506,970.00 USD | 0.00 USD | 795.57 USD | `-42.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 506,180.00 USD | 0.00 USD | 181.00 USD | `-40.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 506,000.00 USD | 0.00 USD | 798.65 USD | `-34.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 505,200.00 USD | 0.00 USD | 1,550.00 USD | `-33.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 503,650.00 USD | 0.00 USD | 116.07 USD | `-29.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 503,540.00 USD | 0.00 USD | 19,070.00 USD | `-29.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 484,470.00 USD | 0.00 USD | 577.22 USD | `-27.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 483,890.00 USD | 0.00 USD | 343.50 USD | `-25.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 483,540.00 USD | 0.00 USD | 26,280.00 USD | `-24.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1175` | 457,260.00 USD | 0.00 USD | 105.75 USD | `-23.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 457,160.00 USD | 0.00 USD | 120.50 USD | `-21.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 457,040.00 USD | 0.00 USD | 83,620.00 USD | `-20.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 373,410.00 USD | 0.00 USD | 14,940.00 USD | `-18.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 358,480.00 USD | 0.00 USD | 2,670.00 USD | `-17.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 355,810.00 USD | 0.00 USD | 1,540.00 USD | `-16.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 354,270.00 USD | 0.00 USD | 220,940.00 USD | `-16.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 133,330.00 USD | 0.00 USD | 25,060.00 USD | `-14.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1315` | 108,280.00 USD | 0.00 USD | 1,590.00 USD | `-14.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 106,690.00 USD | 0.00 USD | 5,560.00 USD | `-13.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 101,120.00 USD | 0.00 USD | 625.78 USD | `-12.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 100,490.00 USD | 0.00 USD | 502.28 USD | `-12.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 99,990.00 USD | 0.00 USD | 3,350.00 USD | `-11.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 96,640.00 USD | 0.00 USD | 700.86 USD | `-10.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 95,940.00 USD | 0.00 USD | 1,070.00 USD | `-10.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 94,880.00 USD | 0.00 USD | 108.57 USD | `-9.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 94,770.00 USD | 0.00 USD | 349.74 USD | `-9.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 94,420.00 USD | 0.00 USD | 9,780.00 USD | `-8.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 84,640.00 USD | 0.00 USD | 127.35 USD | `-7.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 84,510.00 USD | 0.00 USD | 24,850.00 USD | `-7.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 59,660.00 USD | 0.00 USD | 1,620.00 USD | `-6.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 58,040.00 USD | 0.00 USD | 2,530.00 USD | `-5.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 55,520.00 USD | 0.00 USD | 27,670.00 USD | `-5.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 27,850.00 USD | 0.00 USD | 14,210.00 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 13,630.00 USD | 0.00 USD | 2,560.00 USD | `-3.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 11,070.00 USD | 0.00 USD | 2,720.00 USD | `-3.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 8,350.00 USD | 0.00 USD | 515.43 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 7,830.00 USD | 0.00 USD | 6,750.00 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 1,090.00 USD | 0.00 USD | 490.33 USD | `-1.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 595.04 USD | 0.00 USD | 595.04 USD | `-0.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1535` | 204.57 USD | 204.57 USD | 0.00 USD | `+0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1545` | 19,480.00 USD | 19,280.00 USD | 0.00 USD | `+0.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 25,040.00 USD | 5,560.00 USD | 0.00 USD | `+1.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 25,360.00 USD | 323.31 USD | 0.00 USD | `+2.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 25,580.00 USD | 217.63 USD | 0.00 USD | `+2.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1585` | 29,620.00 USD | 4,040.00 USD | 0.00 USD | `+3.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1595` | 30,380.00 USD | 757.59 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1605` | 40,780.00 USD | 10,410.00 USD | 0.00 USD | `+4.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1615` | 57,650.00 USD | 16,870.00 USD | 0.00 USD | `+5.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1625` | 57,920.00 USD | 271.34 USD | 0.00 USD | `+5.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 78,180.00 USD | 20,260.00 USD | 0.00 USD | `+6.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1645` | 82,630.00 USD | 4,450.00 USD | 0.00 USD | `+7.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1655` | 83,690.00 USD | 1,060.00 USD | 0.00 USD | `+7.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1665` | 85,350.00 USD | 1,670.00 USD | 0.00 USD | `+8.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1675` | 85,740.00 USD | 386.67 USD | 0.00 USD | `+9.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1685` | 85,910.00 USD | 168.50 USD | 0.00 USD | `+9.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 87,380.00 USD | 1,470.00 USD | 0.00 USD | `+10.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 88,600.00 USD | 1,210.00 USD | 0.00 USD | `+11.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 90,390.00 USD | 1,800.00 USD | 0.00 USD | `+11.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 90,620.00 USD | 229.89 USD | 0.00 USD | `+12.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 99,460.00 USD | 8,840.00 USD | 0.00 USD | `+13.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 106,110.00 USD | 6,650.00 USD | 0.00 USD | `+13.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 107,460.00 USD | 1,350.00 USD | 0.00 USD | `+14.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 107,900.00 USD | 439.36 USD | 0.00 USD | `+15.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 108,240.00 USD | 336.40 USD | 0.00 USD | `+15.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 109,140.00 USD | 898.02 USD | 0.00 USD | `+16.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 135,530.00 USD | 26,390.00 USD | 0.00 USD | `+17.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 136,800.00 USD | 1,280.00 USD | 0.00 USD | `+17.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 147,280.00 USD | 10,480.00 USD | 0.00 USD | `+18.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 148,150.00 USD | 864.12 USD | 0.00 USD | `+19.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 150,670.00 USD | 2,520.00 USD | 0.00 USD | `+19.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 150,950.00 USD | 276.75 USD | 0.00 USD | `+20.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 151,100.00 USD | 149.79 USD | 0.00 USD | `+20.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 154,290.00 USD | 3,190.00 USD | 0.00 USD | `+21.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 154,430.00 USD | 147.11 USD | 0.00 USD | `+22.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 154,680.00 USD | 245.50 USD | 0.00 USD | `+22.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 155,340.00 USD | 660.73 USD | 0.00 USD | `+23.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 162,940.00 USD | 7,600.00 USD | 0.00 USD | `+24.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 163,340.00 USD | 396.42 USD | 0.00 USD | `+24.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 164,240.00 USD | 902.34 USD | 0.00 USD | `+25.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 171,310.00 USD | 7,070.00 USD | 0.00 USD | `+26.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 174,840.00 USD | 3,530.00 USD | 0.00 USD | `+26.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 174,980.00 USD | 137.77 USD | 0.00 USD | `+27.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 175,110.00 USD | 133.19 USD | 0.00 USD | `+28.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 175,250.00 USD | 134.20 USD | 0.00 USD | `+28.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 179,140.00 USD | 3,900.00 USD | 0.00 USD | `+29.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 179,970.00 USD | 827.09 USD | 0.00 USD | `+30.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 202,880.00 USD | 22,900.00 USD | 0.00 USD | `+30.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 203,740.00 USD | 863.97 USD | 0.00 USD | `+31.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 225,440.00 USD | 21,700.00 USD | 0.00 USD | `+32.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 225,620.00 USD | 182.72 USD | 0.00 USD | `+32.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 311,520.00 USD | 85,900.00 USD | 0.00 USD | `+33.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 312,990.00 USD | 1,470.00 USD | 0.00 USD | `+34.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 313,160.00 USD | 174.20 USD | 0.00 USD | `+34.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 315,230.00 USD | 2,080.00 USD | 0.00 USD | `+35.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 315,490.00 USD | 252.51 USD | 0.00 USD | `+36.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 317,860.00 USD | 2,370.00 USD | 0.00 USD | `+37.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 317,980.00 USD | 126.50 USD | 0.00 USD | `+37.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 318,170.00 USD | 190.80 USD | 0.00 USD | `+38.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 318,890.00 USD | 713.94 USD | 0.00 USD | `+39.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 319,100.00 USD | 213.00 USD | 0.00 USD | `+40.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 325,380.00 USD | 6,280.00 USD | 0.00 USD | `+42.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 347,870.00 USD | 22,490.00 USD | 0.00 USD | `+43.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 348,200.00 USD | 333.91 USD | 0.00 USD | `+45.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 352,180.00 USD | 3,980.00 USD | 0.00 USD | `+45.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 352,560.00 USD | 378.55 USD | 0.00 USD | `+47.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 352,940.00 USD | 380.23 USD | 0.00 USD | `+47.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 353,120.00 USD | 185.87 USD | 0.00 USD | `+48.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 353,320.00 USD | 192.69 USD | 0.00 USD | `+49.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2295` | 353,500.00 USD | 187.50 USD | 0.00 USD | `+49.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 398,150.00 USD | 44,650.00 USD | 0.00 USD | `+50.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 398,340.00 USD | 189.14 USD | 0.00 USD | `+50.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 402,600.00 USD | 4,260.00 USD | 0.00 USD | `+51.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 404,120.00 USD | 1,520.00 USD | 0.00 USD | `+52.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 404,310.00 USD | 191.59 USD | 0.00 USD | `+52.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 425,540.00 USD | 21,230.00 USD | 0.00 USD | `+54.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 428,070.00 USD | 2,530.00 USD | 0.00 USD | `+55.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 428,260.00 USD | 195.67 USD | 0.00 USD | `+56.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 452,050.00 USD | 23,790.00 USD | 0.00 USD | `+56.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 461,350.00 USD | 9,300.00 USD | 0.00 USD | `+57.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 612,120.00 USD | 150,770.00 USD | 0.00 USD | `+60.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 630,870.00 USD | 18,750.00 USD | 0.00 USD | `+60.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 631,420.00 USD | 551.23 USD | 0.00 USD | `+61.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 631,820.00 USD | 397.90 USD | 0.00 USD | `+62.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 636,150.00 USD | 4,330.00 USD | 0.00 USD | `+63.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 636,440.00 USD | 289.23 USD | 0.00 USD | `+63.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 641,450.00 USD | 5,010.00 USD | 0.00 USD | `+64.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 657,330.00 USD | 15,880.00 USD | 0.00 USD | `+65.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 659,110.00 USD | 1,780.00 USD | 0.00 USD | `+65.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 661,670.00 USD | 2,550.00 USD | 0.00 USD | `+66.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 673,400.00 USD | 11,730.00 USD | 0.00 USD | `+67.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 678,560.00 USD | 5,160.00 USD | 0.00 USD | `+67.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 695,420.00 USD | 16,870.00 USD | 0.00 USD | `+69.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 724,560.00 USD | 29,130.00 USD | 0.00 USD | `+69.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2655` | 804,340.00 USD | 79,780.00 USD | 0.00 USD | `+73.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 804,610.00 USD | 272.88 USD | 0.00 USD | `+76.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 805,010.00 USD | 394.01 USD | 0.00 USD | `+80.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 805,380.00 USD | 375.53 USD | 0.00 USD | `+82.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 807,520.00 USD | 2,130.00 USD | 0.00 USD | `+86.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 808,090.00 USD | 579.27 USD | 0.00 USD | `+86.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 809,850.00 USD | 1,750.00 USD | 0.00 USD | `+89.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 809,950.00 USD | 101.21 USD | 0.00 USD | `+92.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 810,210.00 USD | 262.73 USD | 0.00 USD | `+93.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 811,650.00 USD | 1,440.00 USD | 0.00 USD | `+93.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 817,810.00 USD | 6,160.00 USD | 0.00 USD | `+95.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 823,240.00 USD | 5,430.00 USD | 0.00 USD | `+96.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 823,530.00 USD | 289.61 USD | 0.00 USD | `+99.20%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1336` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 3,580.00 USD | 5,990.00 USD | 16,000.00 USD |
| `7D` | `0.1340` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 9,160.00 USD | 7,730.00 USD | 28,910.00 USD |
| `1D` | `0.1342` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 830.00 USD | 918.48 USD | 3,560.00 USD |
| `7D` | `0.1344` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 6,410.00 USD | 5,790.00 USD | 19,420.00 USD |
| `1D` | `0.1345` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 0.00 USD | 691.54 USD | 0.00 USD |
| `1D` | `0.1348` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 2,170.00 USD |
| `7D` | `0.1348` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 31,170.00 USD | 7,150.00 USD | 23,510.00 USD |
| `1D` | `0.1351` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 6,820.00 USD | 2,050.00 USD | 5,870.00 USD |
| `7D` | `0.1352` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 11,390.00 USD | 6,290.00 USD | 24,710.00 USD |
| `1D` | `0.1354` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 2,670.00 USD | 688.99 USD | 4,320.00 USD |
| `7D` | `0.1356` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 16,150.00 USD | 12,180.00 USD | 9,380.00 USD |
| `1D` | `0.1357` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 2,570.00 USD |
| `1D` | `0.1360` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 2,480.00 USD | 869.31 USD | 4,370.00 USD |
| `7D` | `0.1360` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 25,240.00 USD | 8,630.00 USD | 8,770.00 USD |
| `1D` | `0.1363` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 4,890.00 USD | 2,360.00 USD | 2,720.00 USD |
| `7D` | `0.1364` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD |
| `1D` | `0.1366` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 1,340.00 USD | 484.70 USD | 0.00 USD |
| `7D` | `0.1368` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 4,500.00 USD | 7,610.00 USD | 2,530.00 USD |
| `1D` | `0.1369` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD |
| `1D` | `0.1372` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 5,470.00 USD | 1,110.00 USD | 2,240.00 USD |
| `7D` | `0.1372` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1375` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 0.00 USD | 2,220.00 USD | 0.00 USD |
| `1D` | `0.1378` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 936.88 USD | 1,590.00 USD | 1,550.00 USD |
| `7D` | `0.1380` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD |
| `1D` | `0.1381` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 5,890.00 USD | 7,190.00 USD | 11,730.00 USD |
| `1D` | `0.1384` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 10,450.00 USD | 2,890.00 USD | 15,270.00 USD |
| `7D` | `0.1384` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 11,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1387` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 33,240.00 USD | 2,090.00 USD | 2,250.00 USD |
| `7D` | `0.1388` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD |
| `1D` | `0.1390` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 5,190.00 USD | 1,970.00 USD | 1,020.00 USD |
| `7D` | `0.1392` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 0.00 USD | 4,690.00 USD | 0.00 USD |
| `1D` | `0.1396` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 0.00 USD | 6,230.00 USD | 0.00 USD |
| `7D` | `0.1396` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD |
| `1D` | `0.1399` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 5,720.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1400` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD |
| `1D` | `0.1402` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 0.00 USD | 2,100.00 USD | 995.35 USD |
| `7D` | `0.1404` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1411` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD |
| `7D` | `0.1416` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD |
| `7D` | `0.1420` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD |
| `1D` | `0.1423` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 4,030.00 USD | 2,310.00 USD | 6,410.00 USD |
| `7D` | `0.1432` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 10,760.00 USD |
| `1D` | `0.1435` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 3,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1436` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD |
| `1D` | `0.1438` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 0.00 USD | 3,590.00 USD | 20,320.00 USD |
| `7D` | `0.1440` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 13,180.00 USD | 5,260.00 USD | 3,610.00 USD |
| `1D` | `0.1441` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 17,680.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1444` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD |
| `7D` | `0.1444` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 3,450.00 USD | 0.00 USD | 6,160.00 USD |
| `7D` | `0.1452` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 0.00 USD | 5,660.00 USD | 14,180.00 USD |
| `1D` | `0.1453` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1456` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD |
| `7D` | `0.1460` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD |
| `7D` | `0.1464` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD |
| `1D` | `0.1465` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 3,590.00 USD |
| `1D` | `0.1468` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 12,090.00 USD | 2,700.00 USD | 8,060.00 USD |
| `7D` | `0.1468` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 9,720.00 USD | 9,180.00 USD | 8,720.00 USD |
| `1D` | `0.1471` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 4,400.00 USD | 5,970.00 USD | 1,210.00 USD |
| `7D` | `0.1472` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 19,180.00 USD | 0.00 USD | 14,170.00 USD |
| `1D` | `0.1474` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 17,930.00 USD | 9,630.00 USD | 27,540.00 USD |
| `7D` | `0.1476` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 68,180.00 USD | 20,180.00 USD | 5,320.00 USD |
| `1D` | `0.1477` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 102,190.00 USD | 16,230.00 USD | 35,620.00 USD |
| `1D` | `0.1480` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 54,050.00 USD | 17,450.00 USD | 5,190.00 USD |
| `7D` | `0.1480` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 50,400.00 USD | 43,810.00 USD | 50,250.00 USD |
| `1D` | `0.1483` | 979,320.00 USD | 0.00 USD | 979,320.00 USD | 17,530.00 USD | 4,230.00 USD | 11,090.00 USD |
| `7D` | `0.1484` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 47,020.00 USD | 16,640.00 USD | 43,440.00 USD |
| `1D` | `0.1486` | 946,460.00 USD | 0.00 USD | 946,460.00 USD | 13,550.00 USD | 0.00 USD | 9,060.00 USD |
| `7D` | `0.1488` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 24,980.00 USD | 10,470.00 USD | 25,980.00 USD |
| `1D` | `0.1489` | 923,850.00 USD | 0.00 USD | 923,850.00 USD | 6,740.00 USD | 7,050.00 USD | 4,950.00 USD |
| `1D` | `0.1492` | 905,110.00 USD | 0.00 USD | 905,110.00 USD | 24,480.00 USD | 8,610.00 USD | 8,400.00 USD |
| `7D` | `0.1492` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 40,320.00 USD | 21,590.00 USD | 35,230.00 USD |
| `1D` | `0.1495` | 863,620.00 USD | 0.00 USD | 863,620.00 USD | 18,450.00 USD | 5,270.00 USD | 2,180.00 USD |
| `7D` | `0.1496` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 34,650.00 USD | 18,690.00 USD | 17,090.00 USD |
| `1D` | `0.1498` | 837,730.00 USD | 0.00 USD | 837,730.00 USD | 0.00 USD | 0.00 USD | 347.81 USD |
| `7D` | `0.1500` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 60,500.00 USD | 9,610.00 USD | 21,940.00 USD |
| `1D` | `0.1501` | 837,380.00 USD | 0.00 USD | 837,380.00 USD | 6,280.00 USD | 0.00 USD | 3,370.00 USD |
| `1D` | `0.1504` | 827,740.00 USD | 0.00 USD | 827,740.00 USD | 21,400.00 USD | 15,920.00 USD | 55,270.00 USD |
| `7D` | `0.1504` | 910,350.00 USD | 0.00 USD | 910,350.00 USD | 20,410.00 USD | 19,520.00 USD | 44,850.00 USD |
| `1D` | `0.1507` | 735,150.00 USD | 0.00 USD | 735,150.00 USD | 93,360.00 USD | 28,420.00 USD | 62,720.00 USD |
| `7D` | `0.1508` | 825,560.00 USD | 0.00 USD | 825,560.00 USD | 152,330.00 USD | 16,820.00 USD | 104,530.00 USD |
| `1D` | `0.1510` | 550,650.00 USD | 0.00 USD | 550,650.00 USD | 188,120.00 USD | 9,010.00 USD | 1,200.00 USD |
| `7D` | `0.1512` | 551,890.00 USD | 0.00 USD | 551,890.00 USD | 86,820.00 USD | 13,310.00 USD | 59,430.00 USD |
| `1D` | `0.1513` | 352,330.00 USD | 0.00 USD | 352,330.00 USD | 25,970.00 USD | 5,200.00 USD | 2,600.00 USD |
| `1D` | `0.1516` | 318,560.00 USD | 0.00 USD | 318,560.00 USD | 10,070.00 USD | 8,340.00 USD | 17,370.00 USD |
| `7D` | `0.1516` | 392,330.00 USD | 0.00 USD | 392,330.00 USD | 0.00 USD | 13,330.00 USD | 61,270.00 USD |
| `1D` | `0.1519` | 282,780.00 USD | 0.00 USD | 282,780.00 USD | 14,340.00 USD | 2,630.00 USD | 16,310.00 USD |
| `7D` | `0.1520` | 317,730.00 USD | 0.00 USD | 317,730.00 USD | 0.00 USD | 22,090.00 USD | 87,060.00 USD |
| `1D` | `0.1522` | 249,510.00 USD | 0.00 USD | 249,510.00 USD | 38,050.00 USD | 4,440.00 USD | 5,820.00 USD |
| `7D` | `0.1524` | 208,590.00 USD | 0.00 USD | 208,590.00 USD | 0.00 USD | 13,950.00 USD | 8,320.00 USD |
| `1D` | `0.1525` | 201,200.00 USD | 0.00 USD | 201,200.00 USD | 0.00 USD | 0.00 USD | 8,320.00 USD |
| `1D` | `0.1528` | 192,880.00 USD | 0.00 USD | 192,880.00 USD | 0.00 USD | 0.00 USD | 5,140.00 USD |
| `7D` | `0.1528` | 186,320.00 USD | 0.00 USD | 186,320.00 USD | 0.00 USD | 33,940.00 USD | 0.00 USD |
| `7D` | `0.1532` | 152,380.00 USD | 0.00 USD | 152,380.00 USD | 38,390.00 USD | 17,260.00 USD | 51,660.00 USD |
| `1D` | `0.1534` | 187,740.00 USD | 0.00 USD | 187,740.00 USD | 0.00 USD | 8,980.00 USD | 50,810.00 USD |
| `7D` | `0.1536` | 45,070.00 USD | 0.00 USD | 45,070.00 USD | 0.00 USD | 8,570.00 USD | 0.00 USD |
| `1D` | `0.1537` | 127,950.00 USD | 0.00 USD | 127,950.00 USD | 44,200.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1540` | 83,750.00 USD | 0.00 USD | 83,750.00 USD | 20,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1540` | 36,500.00 USD | 0.00 USD | 36,500.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD |
| `7D` | `0.1544` | 18,270.00 USD | 0.00 USD | 18,270.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD |
| `7D` | `0.1548` | 14,680.00 USD | 0.00 USD | 14,680.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD |
| `1D` | `0.1549` | 63,710.00 USD | 0.00 USD | 63,710.00 USD | 0.00 USD | 17,000.00 USD | 33,130.00 USD |
| `1D` | `0.1552` | 13,580.00 USD | 0.00 USD | 13,580.00 USD | 0.00 USD | 2,500.00 USD | 3,890.00 USD |
| `7D` | `0.1552` | 11,820.00 USD | 0.00 USD | 11,820.00 USD | 0.00 USD | 11,820.00 USD | 0.00 USD |
| `1D` | `0.1555` | 7,190.00 USD | 0.00 USD | 7,190.00 USD | 0.00 USD | 0.00 USD | 7,190.00 USD |
| `1D` | `0.1557` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1558` | 12,860.00 USD | 12,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,860.00 USD |
| `7D` | `0.1560` | 10,990.00 USD | 10,990.00 USD | 0.00 USD | 0.00 USD | 10,990.00 USD | 0.00 USD |
| `7D` | `0.1560` | 21,980.00 USD | 21,980.00 USD | 0.00 USD | 0.00 USD | 10,990.00 USD | 0.00 USD |
| `1D` | `0.1561` | 17,820.00 USD | 17,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `1D` | `0.1564` | 199,930.00 USD | 199,930.00 USD | 0.00 USD | 3,130.00 USD | 13,270.00 USD | 165,700.00 USD |
| `7D` | `0.1564` | 260,130.00 USD | 260,130.00 USD | 0.00 USD | 101,070.00 USD | 33,750.00 USD | 103,330.00 USD |
| `1D` | `0.1567` | 291,550.00 USD | 291,550.00 USD | 0.00 USD | 39,290.00 USD | 32,420.00 USD | 19,910.00 USD |
| `7D` | `0.1568` | 413,380.00 USD | 413,380.00 USD | 0.00 USD | 137,880.00 USD | 15,360.00 USD | 0.00 USD |
| `1D` | `0.1570` | 368,660.00 USD | 368,660.00 USD | 0.00 USD | 0.00 USD | 12,360.00 USD | 64,740.00 USD |
| `7D` | `0.1572` | 698,980.00 USD | 698,980.00 USD | 0.00 USD | 187,220.00 USD | 39,540.00 USD | 58,840.00 USD |
| `1D` | `0.1576` | 394,630.00 USD | 394,630.00 USD | 0.00 USD | 25,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1576` | 867,490.00 USD | 867,490.00 USD | 0.00 USD | 44,680.00 USD | 123,840.00 USD | 0.00 USD |
| `7D` | `0.1580` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 129,940.00 USD | 101,090.00 USD | 0.00 USD |
| `7D` | `0.1584` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 80,450.00 USD | 43,370.00 USD | 0.00 USD |
| `1D` | `0.1585` | 433,850.00 USD | 433,850.00 USD | 0.00 USD | 28,600.00 USD | 2,370.00 USD | 8,250.00 USD |
| `1D` | `0.1588` | 493,420.00 USD | 493,420.00 USD | 0.00 USD | 15,100.00 USD | 28,750.00 USD | 15,730.00 USD |
| `7D` | `0.1588` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 69,180.00 USD | 44,590.00 USD | 0.00 USD |
| `1D` | `0.1591` | 546,930.00 USD | 546,930.00 USD | 0.00 USD | 0.00 USD | 26,120.00 USD | 27,390.00 USD |
| `7D` | `0.1592` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 64,620.00 USD | 0.00 USD |
| `7D` | `0.1596` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 98,530.00 USD | 0.00 USD |
| `1D` | `0.1600` | 566,970.00 USD | 566,970.00 USD | 0.00 USD | 20,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1600` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 60,710.00 USD | 0.00 USD |
| `1D` | `0.1603` | 631,060.00 USD | 631,060.00 USD | 0.00 USD | 64,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1604` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 163,960.00 USD | 112,090.00 USD | 273,670.00 USD |
| `1D` | `0.1606` | 658,700.00 USD | 658,700.00 USD | 0.00 USD | 27,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1608` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 208,080.00 USD | 240,680.00 USD | 172,000.00 USD |
| `1D` | `0.1609` | 692,880.00 USD | 692,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 34,180.00 USD |
| `1D` | `0.1612` | 818,800.00 USD | 818,800.00 USD | 0.00 USD | 20,140.00 USD | 11,530.00 USD | 94,250.00 USD |
| `7D` | `0.1612` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 304,970.00 USD | 328,050.00 USD | 287,340.00 USD |
| `1D` | `0.1615` | 844,130.00 USD | 844,130.00 USD | 0.00 USD | 14,300.00 USD | 0.00 USD | 11,030.00 USD |
| `7D` | `0.1616` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 293,210.00 USD | 131,180.00 USD | 108,800.00 USD |
| `1D` | `0.1618` | 909,900.00 USD | 909,900.00 USD | 0.00 USD | 53,600.00 USD | 12,180.00 USD | 0.00 USD |
| `7D` | `0.1620` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 196,620.00 USD | 0.00 USD |
| `1D` | `0.1621` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 92,470.00 USD | 73,150.00 USD | 0.00 USD |
| `1D` | `0.1624` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 50,280.00 USD | 59,670.00 USD | 0.00 USD |
| `7D` | `0.1624` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 193,150.00 USD | 0.00 USD |
| `1D` | `0.1627` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 25,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1628` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 76,780.00 USD | 0.00 USD | 103,330.00 USD |
| `1D` | `0.1630` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 17,970.00 USD | 101,620.00 USD |
| `1D` | `0.1633` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 98,410.00 USD | 6,020.00 USD | 0.00 USD |
| `1D` | `0.1636` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 19,990.00 USD | 8,690.00 USD |
| `7D` | `0.1636` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 0.00 USD | 13,670.00 USD | 23,560.00 USD |
| `1D` | `0.1639` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 13,220.00 USD | 0.00 USD |
| `7D` | `0.1640` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD |
| `1D` | `0.1642` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 19,180.00 USD | 36,980.00 USD | 16,030.00 USD |
| `7D` | `0.1644` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 8,990.00 USD | 0.00 USD |
| `1D` | `0.1645` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 14,950.00 USD | 11,350.00 USD | 0.00 USD |
| `7D` | `0.1648` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD |
| `1D` | `0.1654` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,050.00 USD |
| `7D` | `0.1656` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 31,800.00 USD | 0.00 USD |
| `1D` | `0.1657` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 9,730.00 USD | 55,300.00 USD | 0.00 USD |
| `1D` | `0.1660` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 8,220.00 USD | 11,150.00 USD | 50,810.00 USD |
| `7D` | `0.1660` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 79,170.00 USD | 11,020.00 USD | 51,660.00 USD |
| `1D` | `0.1663` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 44,200.00 USD | 14,550.00 USD | 44,100.00 USD |
| `7D` | `0.1664` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD |
| `1D` | `0.1666` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 22,170.00 USD | 5,340.00 USD | 78,290.00 USD |
| `7D` | `0.1668` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 42,580.00 USD | 52,290.00 USD | 87,160.00 USD |
| `1D` | `0.1672` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 46,590.00 USD | 2,010.00 USD | 0.00 USD |
| `7D` | `0.1672` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 135,250.00 USD | 62,490.00 USD | 0.00 USD |
| `1D` | `0.1675` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 20,040.00 USD | 1,990.00 USD | 19,670.00 USD |
| `7D` | `0.1676` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 84,020.00 USD | 141,950.00 USD | 0.00 USD |
| `1D` | `0.1678` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 22,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1680` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 121,860.00 USD | 80,270.00 USD | 15,310.00 USD |
| `1D` | `0.1681` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 120,850.00 USD | 4,560.00 USD | 0.00 USD |
| `1D` | `0.1684` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 54,020.00 USD | 26,600.00 USD | 32,180.00 USD |
| `7D` | `0.1684` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD |
| `1D` | `0.1687` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 6,560.00 USD | 5,840.00 USD | 23,990.00 USD |
| `7D` | `0.1688` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD |
| `1D` | `0.1690` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 18,380.00 USD | 9,870.00 USD | 14,290.00 USD |
| `7D` | `0.1692` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 33,660.00 USD | 70,740.00 USD | 40,690.00 USD |
| `1D` | `0.1693` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 84,630.00 USD | 74,940.00 USD | 11,880.00 USD |
| `1D` | `0.1696` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 23,530.00 USD | 16,310.00 USD | 6,650.00 USD |
| `7D` | `0.1696` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 17,360.00 USD | 87,350.00 USD | 39,780.00 USD |
| `1D` | `0.1699` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 26,000.00 USD | 56,690.00 USD | 0.00 USD |
| `7D` | `0.1700` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 0.00 USD | 25,330.00 USD | 41,050.00 USD |
| `1D` | `0.1702` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,240.00 USD |
| `7D` | `0.1704` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 55,170.00 USD | 46,880.00 USD | 0.00 USD |
| `1D` | `0.1705` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 14,190.00 USD | 20,810.00 USD | 0.00 USD |
| `1D` | `0.1708` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 39,520.00 USD | 65,470.00 USD | 13,990.00 USD |
| `7D` | `0.1708` | 6,730,000.00 USD | 6,730,000.00 USD | 0.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD |
| `1D` | `0.1711` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 4,910.00 USD | 8,040.00 USD |
| `1D` | `0.1714` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 12,410.00 USD | 0.00 USD |
| `7D` | `0.1716` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 42,020.00 USD | 15,160.00 USD |
| `1D` | `0.1717` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 9,570.00 USD | 34,120.00 USD | 19,560.00 USD |
| `1D` | `0.1720` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 80,090.00 USD | 1,590.00 USD | 5,030.00 USD |
| `7D` | `0.1720` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 161,770.00 USD |
| `1D` | `0.1723` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 54,130.00 USD | 16,860.00 USD | 66,630.00 USD |
| `7D` | `0.1724` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 118,060.00 USD | 0.00 USD | 208,480.00 USD |
| `1D` | `0.1726` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 8,230.00 USD | 2,410.00 USD | 12,130.00 USD |
| `1D` | `0.1729` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD |
| `1D` | `0.1732` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD |
| `7D` | `0.1732` | 7,760,000.00 USD | 7,760,000.00 USD | 0.00 USD | 476,430.00 USD | 0.00 USD | 9,420.00 USD |
| `1D` | `0.1735` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 14,970.00 USD | 9,510.00 USD | 0.00 USD |
| `1D` | `0.1738` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 18,610.00 USD | 2,310.00 USD | 6,410.00 USD |
| `7D` | `0.1740` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 83,810.00 USD |
| `1D` | `0.1741` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 1,600.00 USD | 5,860.00 USD |
| `1D` | `0.1744` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 2,460.00 USD | 13,980.00 USD |
| `7D` | `0.1744` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1747` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 8,530.00 USD | 0.00 USD | 31,930.00 USD |
| `7D` | `0.1748` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `0.1750` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 80,070.00 USD | 2,280.00 USD | 22,640.00 USD |
| `7D` | `0.1752` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 291,880.00 USD |
| `1D` | `0.1753` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 32,240.00 USD | 0.00 USD | 33,630.00 USD |
| `1D` | `0.1756` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 23,610.00 USD | 27,640.00 USD | 73,180.00 USD |
| `7D` | `0.1756` | 8,530,000.00 USD | 8,530,000.00 USD | 0.00 USD | 112,930.00 USD | 0.00 USD | 186,030.00 USD |
| `1D` | `0.1759` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 85,450.00 USD | 31,960.00 USD | 36,770.00 USD |
| `7D` | `0.1760` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 277,910.00 USD | 77,870.00 USD | 32,350.00 USD |
| `1D` | `0.1762` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 72,450.00 USD | 83,100.00 USD | 66,600.00 USD |
| `7D` | `0.1764` | 9,580,000.00 USD | 9,580,000.00 USD | 0.00 USD | 353,950.00 USD | 270,450.00 USD | 40,340.00 USD |
| `1D` | `0.1765` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 20,220.00 USD | 28,990.00 USD | 43,560.00 USD |
| `1D` | `0.1768` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 19,860.00 USD | 83,210.00 USD | 62,630.00 USD |
| `7D` | `0.1768` | 9,960,000.00 USD | 9,960,000.00 USD | 0.00 USD | 191,690.00 USD | 154,100.00 USD | 31,570.00 USD |
| `1D` | `0.1771` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 43,430.00 USD | 19,520.00 USD | 24,210.00 USD |
| `7D` | `0.1772` | 10,230,000.00 USD | 10,230,000.00 USD | 0.00 USD | 98,390.00 USD | 153,480.00 USD | 21,360.00 USD |
| `1D` | `0.1774` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 20,200.00 USD | 30,630.00 USD | 26,430.00 USD |
| `7D` | `0.1776` | 10,480,000.00 USD | 10,480,000.00 USD | 0.00 USD | 186,770.00 USD | 59,720.00 USD | 0.00 USD |
| `1D` | `0.1777` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 42,080.00 USD | 81,500.00 USD | 24,860.00 USD |
| `1D` | `0.1780` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 11,580.00 USD | 9,760.00 USD | 13,680.00 USD |
| `7D` | `0.1780` | 10,740,000.00 USD | 10,740,000.00 USD | 0.00 USD | 52,730.00 USD | 46,410.00 USD | 157,510.00 USD |
| `1D` | `0.1783` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 27,640.00 USD | 15,680.00 USD | 19,300.00 USD |
| `7D` | `0.1784` | 10,960,000.00 USD | 10,960,000.00 USD | 0.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD |
| `1D` | `0.1786` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 16,960.00 USD | 31,510.00 USD | 5,350.00 USD |
| `7D` | `0.1788` | 11,130,000.00 USD | 11,130,000.00 USD | 0.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD |
| `1D` | `0.1789` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 15,890.00 USD | 31,190.00 USD | 20,020.00 USD |
| `1D` | `0.1792` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 13,950.00 USD | 16,470.00 USD | 18,160.00 USD |
| `7D` | `0.1792` | 11,370,000.00 USD | 11,370,000.00 USD | 0.00 USD | 182,810.00 USD | 46,960.00 USD | 3,940.00 USD |
| `1D` | `0.1795` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 53,160.00 USD | 43,180.00 USD | 18,910.00 USD |
| `7D` | `0.1796` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 17,130.00 USD | 26,110.00 USD | 44,450.00 USD |
| `1D` | `0.1798` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 15,420.00 USD | 17,120.00 USD | 21,440.00 USD |
| `7D` | `0.1800` | 11,570,000.00 USD | 11,570,000.00 USD | 0.00 USD | 12,940.00 USD | 34,680.00 USD | 73,510.00 USD |
| `1D` | `0.1801` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 12,470.00 USD | 23,820.00 USD | 13,950.00 USD |
| `1D` | `0.1804` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 10,530.00 USD | 16,830.00 USD | 19,340.00 USD |
| `7D` | `0.1804` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 35,280.00 USD | 32,850.00 USD | 23,570.00 USD |
| `1D` | `0.1807` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 16,640.00 USD | 17,460.00 USD | 9,040.00 USD |
| `7D` | `0.1808` | 11,840,000.00 USD | 11,840,000.00 USD | 0.00 USD | 35,050.00 USD | 67,250.00 USD | 73,440.00 USD |
| `1D` | `0.1810` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 12,880.00 USD | 15,840.00 USD | 8,290.00 USD |
| `7D` | `0.1812` | 11,990,000.00 USD | 11,990,000.00 USD | 0.00 USD | 64,990.00 USD | 29,900.00 USD | 50,510.00 USD |
| `1D` | `0.1813` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 14,660.00 USD | 37,850.00 USD | 15,990.00 USD |
| `1D` | `0.1816` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 13,550.00 USD | 0.00 USD | 15,900.00 USD |
| `7D` | `0.1816` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 69,700.00 USD | 33,940.00 USD | 38,270.00 USD |
| `1D` | `0.1819` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 6,740.00 USD | 12,120.00 USD | 6,830.00 USD |
| `7D` | `0.1820` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 65,350.00 USD | 54,880.00 USD | 43,100.00 USD |
| `1D` | `0.1822` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 21,610.00 USD | 1,930.00 USD |
| `7D` | `0.1824` | 12,500,000.00 USD | 12,500,000.00 USD | 0.00 USD | 80,350.00 USD | 17,880.00 USD | 112,550.00 USD |
| `1D` | `0.1825` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 18,910.00 USD | 1,780.00 USD | 11,450.00 USD |
| `1D` | `0.1828` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 6,840.00 USD | 5,270.00 USD | 2,530.00 USD |
| `7D` | `0.1828` | 12,680,000.00 USD | 12,680,000.00 USD | 0.00 USD | 79,610.00 USD | 29,630.00 USD | 69,840.00 USD |
| `7D` | `0.1832` | 12,900,000.00 USD | 12,900,000.00 USD | 0.00 USD | 108,540.00 USD | 31,590.00 USD | 74,200.00 USD |
| `1D` | `0.1834` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 2,670.00 USD | 0.00 USD | 3,370.00 USD |
| `7D` | `0.1836` | 13,230,000.00 USD | 13,230,000.00 USD | 0.00 USD | 172,660.00 USD | 110,870.00 USD | 52,650.00 USD |
| `1D` | `0.1837` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 3,610.00 USD | 2,640.00 USD | 1,360.00 USD |
| `1D` | `0.1840` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 5,430.00 USD | 1,970.00 USD | 12,670.00 USD |
| `7D` | `0.1840` | 13,580,000.00 USD | 13,580,000.00 USD | 0.00 USD | 141,620.00 USD | 50,840.00 USD | 151,740.00 USD |
| `1D` | `0.1843` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 1,030.00 USD | 3,550.00 USD | 0.00 USD |
| `7D` | `0.1844` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 94,510.00 USD | 20,390.00 USD | 82,350.00 USD |
| `1D` | `0.1846` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 9,830.00 USD | 1,840.00 USD | 7,140.00 USD |
| `7D` | `0.1848` | 13,920,000.00 USD | 13,920,000.00 USD | 0.00 USD | 35,280.00 USD | 69,910.00 USD | 41,760.00 USD |
| `1D` | `0.1849` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 12,130.00 USD | 5,200.00 USD | 2,600.00 USD |
| `1D` | `0.1852` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 2,580.00 USD | 1,340.00 USD |
| `7D` | `0.1852` | 14,370,000.00 USD | 14,370,000.00 USD | 0.00 USD | 168,270.00 USD | 28,290.00 USD | 251,810.00 USD |
| `1D` | `0.1855` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 7,630.00 USD | 0.00 USD | 4,220.00 USD |
| `7D` | `0.1856` | 14,600,000.00 USD | 14,600,000.00 USD | 0.00 USD | 100,160.00 USD | 21,030.00 USD | 106,560.00 USD |
| `1D` | `0.1858` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 10,290.00 USD | 4,100.00 USD | 14,330.00 USD |
| `7D` | `0.1860` | 14,840,000.00 USD | 14,840,000.00 USD | 0.00 USD | 64,600.00 USD | 48,330.00 USD | 127,610.00 USD |
| `1D` | `0.1861` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 5,860.00 USD | 2,970.00 USD | 5,390.00 USD |
| `1D` | `0.1864` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD | 6,520.00 USD |
| `7D` | `0.1864` | 14,990,000.00 USD | 14,990,000.00 USD | 0.00 USD | 48,260.00 USD | 44,140.00 USD | 61,380.00 USD |
| `1D` | `0.1867` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 3,300.00 USD | 0.00 USD | 8,300.00 USD |
| `7D` | `0.1868` | 15,230,000.00 USD | 15,230,000.00 USD | 0.00 USD | 133,990.00 USD | 51,510.00 USD | 56,290.00 USD |
| `1D` | `0.1870` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 4,960.00 USD | 5,040.00 USD | 8,740.00 USD |
| `1D` | `0.1872` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 12,350.00 USD | 1,900.00 USD | 3,140.00 USD |
| `7D` | `0.1872` | 15,720,000.00 USD | 15,720,000.00 USD | 0.00 USD | 188,990.00 USD | 146,600.00 USD | 155,060.00 USD |
| `7D` | `0.1876` | 15,860,000.00 USD | 15,860,000.00 USD | 0.00 USD | 65,910.00 USD | 23,180.00 USD | 43,960.00 USD |
| `7D` | `0.1880` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 57,250.00 USD | 35,940.00 USD | 30,950.00 USD |
| `7D` | `0.1884` | 16,040,000.00 USD | 16,040,000.00 USD | 0.00 USD | 14,000.00 USD | 35,430.00 USD | 9,740.00 USD |
| `7D` | `0.1888` | 16,160,000.00 USD | 16,160,000.00 USD | 0.00 USD | 22,970.00 USD | 4,800.00 USD | 88,260.00 USD |
| `7D` | `0.1892` | 16,240,000.00 USD | 16,240,000.00 USD | 0.00 USD | 49,980.00 USD | 2,860.00 USD | 34,160.00 USD |
| `7D` | `0.1896` | 16,320,000.00 USD | 16,320,000.00 USD | 0.00 USD | 42,320.00 USD | 11,820.00 USD | 18,680.00 USD |
| `7D` | `0.1900` | 16,370,000.00 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 29,650.00 USD | 20,420.00 USD |
| `7D` | `0.1904` | 16,410,000.00 USD | 16,410,000.00 USD | 0.00 USD | 14,330.00 USD | 17,690.00 USD | 10,800.00 USD |
| `7D` | `0.1908` | 16,540,000.00 USD | 16,540,000.00 USD | 0.00 USD | 33,940.00 USD | 44,480.00 USD | 52,810.00 USD |
| `7D` | `0.1912` | 16,560,000.00 USD | 16,560,000.00 USD | 0.00 USD | 0.00 USD | 9,380.00 USD | 10,330.00 USD |
| `7D` | `0.1916` | 16,590,000.00 USD | 16,590,000.00 USD | 0.00 USD | 7,460.00 USD | 12,040.00 USD | 11,900.00 USD |
| `7D` | `0.1920` | 16,600,000.00 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 5,100.00 USD | 0.00 USD |
| `7D` | `0.1924` | 16,620,000.00 USD | 16,620,000.00 USD | 0.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD |
| `7D` | `0.1928` | 16,640,000.00 USD | 16,640,000.00 USD | 0.00 USD | 11,600.00 USD | 7,370.00 USD | 0.00 USD |
| `7D` | `0.1944` | 16,640,000.00 USD | 16,640,000.00 USD | 0.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1952` | 16,650,000.00 USD | 16,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD |
| `7D` | `0.1956` | 16,660,000.00 USD | 16,660,000.00 USD | 0.00 USD | 4,860.00 USD | 2,760.00 USD | 0.00 USD |
| `7D` | `0.1960` | 16,670,000.00 USD | 16,670,000.00 USD | 0.00 USD | 5,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1964` | 16,690,000.00 USD | 16,690,000.00 USD | 0.00 USD | 6,470.00 USD | 2,700.00 USD | 10,990.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `189.04M` | Total OI Tokens: `1,205,252,703.9 ARB`
  * 1h OI Change: `+0.63%` | 4h OI Change: `-9.20%` | 24h OI Change: `-20.74%`
  * Exchange Breakdown: Binance=`43.24M` | Bybit=`26.13M` | OKX=`14.77M` | Hyperliquid=`12.93M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-1.31K` | Last 24h: `10.97K` | Last 3d: `22.34K` | Last 7d: `43.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0064%` | **USDT OKX** | `0.0027%` |
| **USDT Bybit** | `0.0031%` | **USDT KuCoin** | `-0.0006%` |
| **USDT MEXC** | `0.0029%` | **USDT BingX** | `0.0045%` |
| **USDT Gate** | `-0.0116%` | **USDT Bitget** | `-0.0019%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `47.49%` | `52.51%` | `0.90` | 7,470,000.00 USD |
| `15M` | `Binance` | `45.23%` | `54.77%` | `0.83` | 2,430,000.00 USD |
| `15M` | `OKX` | `49.02%` | `50.98%` | `0.96` | 1,240,000.00 USD |
| `15M` | `Bybit` | `53.18%` | `46.82%` | `1.14` | 1,620,000.00 USD |
| `15M` | `KuCoin` | `46.2%` | `53.8%` | `0.86` | 39,440.00 USD |
| `15M` | `Gate` | `43.34%` | `56.66%` | `0.76` | 289,980.00 USD |
| `15M` | `Bitget` | `28.65%` | `71.35%` | `0.40` | 274,420.00 USD |
| `15M` | `BingX` | `57.11%` | `42.89%` | `1.33` | 174,820.00 USD |
| `15M` | `MEXC` | `31.37%` | `68.63%` | `0.46` | 442,280.00 USD |
| `15M` | `Bitunix` | `44.98%` | `55.02%` | `0.82` | 131,120.00 USD |
| `15M` | `Hyperliquid` | `50.16%` | `49.84%` | `1.01` | 288,910.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.42%` | `50.58%` | `0.98` | 275,290.00 USD |
| `15M` | `Crypto.com` | `82.35%` | `17.65%` | `4.67` | 1,640.00 USD |
| `15M` | `WhiteBIT` | `87.63%` | `12.37%` | `7.08` | 164,710.00 USD |
| `15M` | `HTX` | `30.17%` | `69.83%` | `0.43` | 1,020.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `47.73%` | `52.27%` | `0.91` | 19,550.00 USD |
| `15M` | `Aster` | `88.26%` | `11.74%` | `7.52` | 3,180.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `23.82%` | `76.18%` | `0.31` | 65,110.00 USD |
| `15M` | `Whale Positions` | `45.23%` | `54.77%` | `0.83` | 2,430,000.00 USD |
| `15M` | `Global Accounts` | `47.49%` | `52.51%` | `0.90` | 7,470,000.00 USD |
| `1H` | `ARB` | `53.08%` | `46.92%` | `1.13` | 43,850,000.00 USD |
| `1H` | `Binance` | `51.49%` | `48.51%` | `1.06` | 18,220,000.00 USD |
| `1H` | `OKX` | `60.51%` | `39.49%` | `1.53` | 6,630,000.00 USD |
| `1H` | `Bybit` | `48.9%` | `51.1%` | `0.96` | 7,500,000.00 USD |
| `1H` | `KuCoin` | `53.1%` | `46.9%` | `1.13` | 289,890.00 USD |
| `1H` | `Gate` | `57.72%` | `42.28%` | `1.37` | 1,220,000.00 USD |
| `1H` | `Bitget` | `52.44%` | `47.56%` | `1.10` | 1,550,000.00 USD |
| `1H` | `BingX` | `47.31%` | `52.69%` | `0.90` | 775,540.00 USD |
| `1H` | `MEXC` | `52.72%` | `47.28%` | `1.12` | 2,310,000.00 USD |
| `1H` | `Bitunix` | `50.91%` | `49.09%` | `1.04` | 650,500.00 USD |
| `1H` | `Hyperliquid` | `58.82%` | `41.18%` | `1.43` | 1,480,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.24%` | `49.76%` | `1.01` | 2,370,000.00 USD |
| `1H` | `Crypto.com` | `51.53%` | `48.47%` | `1.06` | 15,180.00 USD |
| `1H` | `WhiteBIT` | `81.15%` | `18.85%` | `4.31` | 452,160.00 USD |
| `1H` | `HTX` | `55.52%` | `44.48%` | `1.25` | 9,100.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `43.15%` | `56.85%` | `0.76` | 165,790.00 USD |
| `1H` | `Aster` | `63.9%` | `36.1%` | `1.77` | 99,240.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `47.28%` | `52.72%` | `0.90` | 126,480.00 USD |
| `1H` | `Whale Positions` | `51.49%` | `48.51%` | `1.06` | 18,220,000.00 USD |
| `1H` | `Global Accounts` | `53.08%` | `46.92%` | `1.13` | 43,850,000.00 USD |
| `4H` | `ARB` | `47.71%` | `52.29%` | `0.91` | 121,560,000.00 USD |
| `4H` | `Binance` | `46.1%` | `53.9%` | `0.86` | 50,000,000.00 USD |
| `4H` | `OKX` | `50.35%` | `49.65%` | `1.01` | 17,850,000.00 USD |
| `4H` | `Bybit` | `46.77%` | `53.23%` | `0.88` | 16,530,000.00 USD |
| `4H` | `KuCoin` | `47.47%` | `52.53%` | `0.90` | 923,880.00 USD |
| `4H` | `Gate` | `49.54%` | `50.46%` | `0.98` | 4,040,000.00 USD |
| `4H` | `Bitget` | `45.82%` | `54.18%` | `0.85` | 5,090,000.00 USD |
| `4H` | `BingX` | `48.59%` | `51.41%` | `0.95` | 3,640,000.00 USD |
| `4H` | `MEXC` | `48.12%` | `51.88%` | `0.93` | 9,430,000.00 USD |
| `4H` | `Bitunix` | `51.57%` | `48.43%` | `1.06` | 2,190,000.00 USD |
| `4H` | `Hyperliquid` | `45.68%` | `54.32%` | `0.84` | 4,200,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.43%` | `49.57%` | `1.02` | 5,060,000.00 USD |
| `4H` | `Crypto.com` | `46.96%` | `53.04%` | `0.89` | 39,460.00 USD |
| `4H` | `WhiteBIT` | `75.04%` | `24.96%` | `3.01` | 1,330,000.00 USD |
| `4H` | `HTX` | `53.45%` | `46.55%` | `1.15` | 64,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `34.89%` | `65.11%` | `0.54` | 500,530.00 USD |
| `4H` | `Aster` | `52.52%` | `47.48%` | `1.11` | 307,390.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `43.22%` | `56.78%` | `0.76` | 358,580.00 USD |
| `4H` | `Whale Positions` | `46.1%` | `53.9%` | `0.86` | 50,000,000.00 USD |
| `4H` | `Global Accounts` | `47.71%` | `52.29%` | `0.91` | 121,560,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1688` | `0.1688` | `0.1688` | `0.1693` | `0.1682` | 680,766.88 USD | 453,606.46 USD | 227,160.42 USD | 226,446.04 USD | `+33.26%` | `32B / 8S` |
| `5:00 UTC` | `0.1682` | `0.1683` | `0.1682` | `0.1688` | `0.1681` | 452,736.37 USD | 213,244.89 USD | 239,491.48 USD | -26,246.58 USD | `-5.80%` | `7B / 12S` |
| `0:00 UTC` | `0.1667` | `0.1655` | `0.1667` | `0.1684` | `0.1640` | 2,535,332.38 USD | 1,148,875.51 USD | 1,386,456.87 USD | -237,581.36 USD | `-9.37%` | `2B / 23S` |
| `5:00 UTC` | `0.1650` | `0.1654` | `0.1650` | `0.1661` | `0.1649` | 718,046.47 USD | 414,320.10 USD | 303,726.37 USD | 110,593.73 USD | `+15.40%` | `33B / 14S` |
| `0:00 UTC` | `0.1592` | `0.1590` | `0.1592` | `0.1655` | `0.1541` | 10,418,999.97 USD | 3,996,711.76 USD | 6,422,288.21 USD | -2,425,576.45 USD | `-23.28%` | `2B / 33S` |
| `5:00 UTC` | `0.1535` | `0.1536` | `0.1535` | `0.1560` | `0.1508` | 10,296,961.64 USD | 4,216,389.14 USD | 6,080,572.50 USD | -1,864,183.37 USD | `-18.10%` | `2B / 11S` |
| `0:00 UTC` | `0.1558` | `0.1546` | `0.1558` | `0.1572` | `0.1528` | 5,930,771.66 USD | 3,398,964.11 USD | 2,531,807.55 USD | 867,156.57 USD | `+14.62%` | `22B / 10S` |
| `5:00 UTC` | `0.1590` | `0.1587` | `0.1590` | `0.1599` | `0.1565` | 3,702,564.80 USD | 1,807,551.39 USD | 1,895,013.41 USD | -87,462.01 USD | `-2.36%` | `26B / 13S` |
| `0:00 UTC` | `0.1596` | `0.1591` | `0.1596` | `0.1603` | `0.1573` | 4,839,053.12 USD | 2,292,867.68 USD | 2,546,185.45 USD | -253,317.77 USD | `-5.23%` | `10B / 17S` |
| `5:00 UTC` | `0.1575` | `0.1576` | `0.1575` | `0.1586` | `0.1564` | 822,801.85 USD | 404,641.82 USD | 418,160.03 USD | -13,518.21 USD | `-1.64%` | `19B / 21S` |

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
| `5m` | -159,100.00 USD | -69,820.00 USD | **`DISTRIBUTION`** |
| `15m` | -122,100.00 USD | -209,250.00 USD | **`DISTRIBUTION`** |
| `30m` | 30,740.00 USD | -176,630.00 USD | **`DISTRIBUTION`** |
| `1h` | 4,760.00 USD | 1,500,000.00 USD | **`ACCUMULATION`** |
| `2h` | -2,030,000.00 USD | -5,720,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,840,000.00 USD | -4,910,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -2,120,000.00 USD | -7,540,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,950,000.00 USD | -8,870,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,770,000.00 USD | -9,470,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,890,000.00 USD | -10,420,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,790,000.00 USD | -36,410,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -34,180,000.00 USD | -166,990,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-159.10K` | 15m=`-122.10K` | 1h=`+4.76K` | 24h=`-2.89M`
* Futures Capital Netflows: 5m=`-69.82K` | 15m=`-209.25K` | 1h=`+1.50M` | 24h=`-10.42M`
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
  * `2026-10-30 02:54:14 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:21:14 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:21:14 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:20:14 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:20:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:14 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:14 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:14 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:14 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:22:14 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:14 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
