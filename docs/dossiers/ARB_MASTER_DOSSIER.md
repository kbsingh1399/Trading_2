# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 03:37:25 IST` (`2026-10-29 22:07:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1570` | `0.1573` | `0.1556` | `0.1556` | `3,536,463` | 553,465.84 USD | -109,929.75 USD | `-19.86%` | -7,811,899.71 USD | `+0.17` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1556` | `0.1566` | `0.1533` | `0.1535` | `10,208,660` | 1,581,348.15 USD | -300,800.27 USD | `-19.02%` | -8,112,699.98 USD | `-0.20` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1535` | `0.1538` | `0.1535` | `0.1535` | `563,931` | 86,649.00 USD | 18,565.24 USD | `+21.43%` | -8,094,134.75 USD | `+0.49` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1580` | `0.1603` | `0.1573` | `0.1576` | `30,414,514` | 4,839,053.12 USD | -253,317.77 USD | `-5.23%` | -7,606,990.78 USD | `-0.06` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1576` | `0.1586` | `0.1556` | `0.1556` | `10,403,893` | 1,633,700.68 USD | -130,771.91 USD | `-8.00%` | -7,737,762.69 USD | `+0.11` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1556` | `0.1566` | `0.1533` | `0.1535` | `10,772,591` | 1,667,997.15 USD | -282,235.04 USD | `-16.92%` | -8,019,997.73 USD | `-0.11` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1683` | `0.1684` | `0.1508` | `0.1534` | `152,241,290` | 23,969,202.69 USD | -4,416,609.68 USD | `-18.43%` | -7,801,776.00 USD | `-4.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1534` | `0.1603` | `0.1528` | `0.1556` | `102,506,063` | 16,106,228.03 USD | 395,467.12 USD | `+2.46%` | -7,406,308.88 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1556` | `0.1566` | `0.1533` | `0.1538` | `10,874,345` | 1,683,634.41 USD | -276,270.22 USD | `-16.41%` | -7,682,579.10 USD | `+0.09` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,374,542.78 USD | `-1.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,572,000.78 USD | `-0.89` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1535` | `265,519,944` | 41,743,427.88 USD | -4,303,377.60 USD | `-10.31%` | -7,875,378.39 USD | `-2.10` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1652` | `0.1687` | `0.1623` | `0.1631` | `68,085,678` | 11,252,816.65 USD | -909,329.92 USD | `-8.08%` | -705,420.63 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,136,414.44 USD | `-0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,374,542.78 USD | `-1.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,572,000.78 USD | `-0.89` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1535` | `265,519,944` | 41,743,427.88 USD | -4,303,377.60 USD | `-10.31%` | -7,875,378.39 USD | `-2.10` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:35:39 IST` |

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
| `7D` | `Long Liquidation` | `0.1336` | 2,180,000.00 USD | 2,180,000.00 USD | 3,580.00 USD | 5,990.00 USD | 16,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1340` | 2,160,000.00 USD | 2,160,000.00 USD | 9,160.00 USD | 7,730.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1342` | 1,550,000.00 USD | 1,550,000.00 USD | 830.00 USD | 918.48 USD | 3,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1344` | 2,110,000.00 USD | 2,110,000.00 USD | 6,410.00 USD | 5,790.00 USD | 19,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1345` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 691.54 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1345` | 158.59 USD | 979,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1348` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1348` | 2,080,000.00 USD | 2,080,000.00 USD | 31,170.00 USD | 7,150.00 USD | 23,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1351` | 1,540,000.00 USD | 1,540,000.00 USD | 6,820.00 USD | 2,050.00 USD | 5,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1352` | 2,020,000.00 USD | 2,020,000.00 USD | 11,390.00 USD | 6,290.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1354` | 1,530,000.00 USD | 1,530,000.00 USD | 2,670.00 USD | 688.99 USD | 4,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1355` | 3,760.00 USD | 979,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1356` | 1,980,000.00 USD | 1,980,000.00 USD | 16,150.00 USD | 12,180.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1357` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 2,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1360` | 1,520,000.00 USD | 1,520,000.00 USD | 2,480.00 USD | 869.31 USD | 4,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1360` | 1,940,000.00 USD | 1,940,000.00 USD | 25,240.00 USD | 8,630.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1363` | 1,510,000.00 USD | 1,510,000.00 USD | 4,890.00 USD | 2,360.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1364` | 1,890,000.00 USD | 1,890,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 79,260.00 USD | 975,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1366` | 1,500,000.00 USD | 1,500,000.00 USD | 1,340.00 USD | 484.70 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1368` | 1,870,000.00 USD | 1,870,000.00 USD | 4,500.00 USD | 7,610.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1369` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1372` | 1,500,000.00 USD | 1,500,000.00 USD | 5,470.00 USD | 1,110.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1372` | 1,860,000.00 USD | 1,860,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1375` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 2,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1375` | 24,260.00 USD | 896,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1378` | 1,490,000.00 USD | 1,490,000.00 USD | 936.88 USD | 1,590.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1380` | 1,850,000.00 USD | 1,850,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1381` | 1,480,000.00 USD | 1,480,000.00 USD | 5,890.00 USD | 7,190.00 USD | 11,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1384` | 1,460,000.00 USD | 1,460,000.00 USD | 10,450.00 USD | 2,890.00 USD | 15,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1384` | 1,840,000.00 USD | 1,840,000.00 USD | 11,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 7,490.00 USD | 871,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1387` | 1,430,000.00 USD | 1,430,000.00 USD | 33,240.00 USD | 2,090.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1388` | 1,820,000.00 USD | 1,820,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1390` | 1,390,000.00 USD | 1,390,000.00 USD | 5,190.00 USD | 1,970.00 USD | 1,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1392` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 4,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 7,980.00 USD | 864,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1396` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 6,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1396` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1399` | 1,380,000.00 USD | 1,380,000.00 USD | 5,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1400` | 1,780,000.00 USD | 1,780,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1402` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 2,100.00 USD | 995.35 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1404` | 1,770,000.00 USD | 1,770,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 1,250.00 USD | 856,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1411` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1415` | 11,550.00 USD | 855,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1416` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1420` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1423` | 1,370,000.00 USD | 1,370,000.00 USD | 4,030.00 USD | 2,310.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 484,730.00 USD | 843,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1432` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1435` | 1,350,000.00 USD | 1,350,000.00 USD | 3,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 19,330.00 USD | 358,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1436` | 1,740,000.00 USD | 1,740,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1438` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 3,590.00 USD | 20,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1440` | 1,700,000.00 USD | 1,700,000.00 USD | 13,180.00 USD | 5,260.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1441` | 1,330,000.00 USD | 1,330,000.00 USD | 17,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1444` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1444` | 1,680,000.00 USD | 1,680,000.00 USD | 3,450.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 6,510.00 USD | 339,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1452` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 5,660.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1453` | 1,310,000.00 USD | 1,310,000.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 18,480.00 USD | 332,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1456` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1460` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1464` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1465` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 3,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 28,260.00 USD | 314,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1468` | 1,300,000.00 USD | 1,300,000.00 USD | 12,090.00 USD | 2,700.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1468` | 1,640,000.00 USD | 1,640,000.00 USD | 9,720.00 USD | 9,180.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1471` | 1,280,000.00 USD | 1,280,000.00 USD | 4,400.00 USD | 5,970.00 USD | 1,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1472` | 1,610,000.00 USD | 1,610,000.00 USD | 19,180.00 USD | 0.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1474` | 1,270,000.00 USD | 1,270,000.00 USD | 17,930.00 USD | 9,630.00 USD | 27,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 74,850.00 USD | 286,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1476` | 1,580,000.00 USD | 1,580,000.00 USD | 68,180.00 USD | 20,180.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1477` | 1,210,000.00 USD | 1,210,000.00 USD | 102,190.00 USD | 16,230.00 USD | 35,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1480` | 1,060,000.00 USD | 1,060,000.00 USD | 54,050.00 USD | 17,450.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1480` | 1,480,000.00 USD | 1,480,000.00 USD | 50,400.00 USD | 43,810.00 USD | 50,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1483` | 979,320.00 USD | 979,320.00 USD | 17,530.00 USD | 4,230.00 USD | 11,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1484` | 1,340,000.00 USD | 1,340,000.00 USD | 47,020.00 USD | 16,640.00 USD | 43,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 20,690.00 USD | 211,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1486` | 946,460.00 USD | 946,460.00 USD | 13,550.00 USD | 0.00 USD | 9,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1488` | 1,230,000.00 USD | 1,230,000.00 USD | 24,980.00 USD | 10,470.00 USD | 25,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1489` | 923,850.00 USD | 923,850.00 USD | 6,740.00 USD | 7,050.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1492` | 905,110.00 USD | 905,110.00 USD | 24,480.00 USD | 8,610.00 USD | 8,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1492` | 1,170,000.00 USD | 1,170,000.00 USD | 40,320.00 USD | 21,590.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1495` | 863,620.00 USD | 863,620.00 USD | 18,450.00 USD | 5,270.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 31,670.00 USD | 190,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1496` | 1,070,000.00 USD | 1,070,000.00 USD | 34,650.00 USD | 18,690.00 USD | 17,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1498` | 837,730.00 USD | 837,730.00 USD | 0.00 USD | 0.00 USD | 347.81 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1500` | 1,000,000.00 USD | 1,000,000.00 USD | 60,500.00 USD | 9,610.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1501` | 837,380.00 USD | 837,380.00 USD | 6,280.00 USD | 0.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1504` | 827,740.00 USD | 827,740.00 USD | 21,400.00 USD | 15,920.00 USD | 55,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1504` | 910,350.00 USD | 910,350.00 USD | 20,410.00 USD | 19,520.00 USD | 44,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1505` | 113,080.00 USD | 158,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1507` | 735,150.00 USD | 735,150.00 USD | 93,360.00 USD | 28,420.00 USD | 62,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1508` | 825,560.00 USD | 825,560.00 USD | 152,330.00 USD | 16,820.00 USD | 104,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1510` | 550,650.00 USD | 550,650.00 USD | 188,120.00 USD | 9,010.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1512` | 551,890.00 USD | 551,890.00 USD | 86,820.00 USD | 13,310.00 USD | 59,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1513` | 352,330.00 USD | 352,330.00 USD | 25,970.00 USD | 5,200.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 45,890.00 USD | 45,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1516` | 318,560.00 USD | 318,560.00 USD | 10,070.00 USD | 8,340.00 USD | 17,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1516` | 392,330.00 USD | 392,330.00 USD | 0.00 USD | 13,330.00 USD | 61,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1519` | 282,780.00 USD | 282,780.00 USD | 14,340.00 USD | 2,630.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1520` | 317,730.00 USD | 317,730.00 USD | 0.00 USD | 22,090.00 USD | 87,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1522` | 249,510.00 USD | 249,510.00 USD | 38,050.00 USD | 4,440.00 USD | 5,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1524` | 208,590.00 USD | 208,590.00 USD | 0.00 USD | 13,950.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1525` | 201,200.00 USD | 201,200.00 USD | 0.00 USD | 0.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1528` | 192,880.00 USD | 192,880.00 USD | 0.00 USD | 0.00 USD | 5,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1528` | 186,320.00 USD | 186,320.00 USD | 0.00 USD | 33,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1532` | 152,380.00 USD | 152,380.00 USD | 38,390.00 USD | 17,260.00 USD | 51,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1534` | 187,740.00 USD | 187,740.00 USD | 0.00 USD | 8,980.00 USD | 50,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1536` | 45,070.00 USD | 45,070.00 USD | 0.00 USD | 8,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1537` | 127,950.00 USD | 127,950.00 USD | 44,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1540` | 83,750.00 USD | 83,750.00 USD | 20,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1540` | 36,500.00 USD | 36,500.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1544` | 18,270.00 USD | 18,270.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1548` | 14,680.00 USD | 14,680.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1549` | 63,710.00 USD | 63,710.00 USD | 0.00 USD | 17,000.00 USD | 33,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1552` | 13,580.00 USD | 13,580.00 USD | 0.00 USD | 2,500.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1552` | 11,820.00 USD | 11,820.00 USD | 0.00 USD | 11,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1555` | 7,190.00 USD | 7,190.00 USD | 0.00 USD | 0.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1558` | 12,860.00 USD | 12,860.00 USD | 0.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1560` | 10,990.00 USD | 10,990.00 USD | 0.00 USD | 10,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1560` | 21,980.00 USD | 21,980.00 USD | 0.00 USD | 10,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1561` | 17,820.00 USD | 17,820.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1564` | 199,930.00 USD | 199,930.00 USD | 3,130.00 USD | 13,270.00 USD | 165,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1564` | 260,130.00 USD | 260,130.00 USD | 101,070.00 USD | 33,750.00 USD | 103,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1565` | 354.32 USD | 354.32 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1567` | 291,550.00 USD | 291,550.00 USD | 39,290.00 USD | 32,420.00 USD | 19,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1568` | 413,380.00 USD | 413,380.00 USD | 137,880.00 USD | 15,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1570` | 368,660.00 USD | 368,660.00 USD | 0.00 USD | 12,360.00 USD | 64,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1572` | 698,980.00 USD | 698,980.00 USD | 187,220.00 USD | 39,540.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1575` | 2,270.00 USD | 2,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1576` | 394,630.00 USD | 394,630.00 USD | 25,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1576` | 867,490.00 USD | 867,490.00 USD | 44,680.00 USD | 123,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1580` | 1,100,000.00 USD | 1,100,000.00 USD | 129,940.00 USD | 101,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1584` | 1,220,000.00 USD | 1,220,000.00 USD | 80,450.00 USD | 43,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1585` | 433,850.00 USD | 433,850.00 USD | 28,600.00 USD | 2,370.00 USD | 8,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1588` | 493,420.00 USD | 493,420.00 USD | 15,100.00 USD | 28,750.00 USD | 15,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1588` | 1,340,000.00 USD | 1,340,000.00 USD | 69,180.00 USD | 44,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1591` | 546,930.00 USD | 546,930.00 USD | 0.00 USD | 26,120.00 USD | 27,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1592` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 64,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1596` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 98,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1600` | 566,970.00 USD | 566,970.00 USD | 20,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1600` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 60,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1603` | 631,060.00 USD | 631,060.00 USD | 64,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1604` | 2,110,000.00 USD | 2,110,000.00 USD | 163,960.00 USD | 112,090.00 USD | 273,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1605` | 4,930.00 USD | 7,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1606` | 658,700.00 USD | 658,700.00 USD | 27,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1608` | 2,730,000.00 USD | 2,730,000.00 USD | 208,080.00 USD | 240,680.00 USD | 172,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1609` | 692,880.00 USD | 692,880.00 USD | 0.00 USD | 0.00 USD | 34,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1612` | 818,800.00 USD | 818,800.00 USD | 20,140.00 USD | 11,530.00 USD | 94,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1612` | 3,650,000.00 USD | 3,650,000.00 USD | 304,970.00 USD | 328,050.00 USD | 287,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1615` | 844,130.00 USD | 844,130.00 USD | 14,300.00 USD | 0.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1616` | 4,180,000.00 USD | 4,180,000.00 USD | 293,210.00 USD | 131,180.00 USD | 108,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1618` | 909,900.00 USD | 909,900.00 USD | 53,600.00 USD | 12,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1620` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 196,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1621` | 1,080,000.00 USD | 1,080,000.00 USD | 92,470.00 USD | 73,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1624` | 1,190,000.00 USD | 1,190,000.00 USD | 50,280.00 USD | 59,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1624` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 193,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1625` | 8,640.00 USD | 16,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1627` | 1,210,000.00 USD | 1,210,000.00 USD | 25,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1628` | 4,750,000.00 USD | 4,750,000.00 USD | 76,780.00 USD | 0.00 USD | 103,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1630` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 17,970.00 USD | 101,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1633` | 1,440,000.00 USD | 1,440,000.00 USD | 98,410.00 USD | 6,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1635` | 9,360.00 USD | 25,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1636` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 19,990.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1636` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 13,670.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1639` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 13,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1640` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1642` | 1,550,000.00 USD | 1,550,000.00 USD | 19,180.00 USD | 36,980.00 USD | 16,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1644` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 8,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1645` | 1,580,000.00 USD | 1,580,000.00 USD | 14,950.00 USD | 11,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1645` | 2,060.00 USD | 27,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1648` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1654` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1656` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 31,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1657` | 1,650,000.00 USD | 1,650,000.00 USD | 9,730.00 USD | 55,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1660` | 1,720,000.00 USD | 1,720,000.00 USD | 8,220.00 USD | 11,150.00 USD | 50,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1660` | 5,010,000.00 USD | 5,010,000.00 USD | 79,170.00 USD | 11,020.00 USD | 51,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1663` | 1,820,000.00 USD | 1,820,000.00 USD | 44,200.00 USD | 14,550.00 USD | 44,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1664` | 5,270,000.00 USD | 5,270,000.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1666` | 1,930,000.00 USD | 1,930,000.00 USD | 22,170.00 USD | 5,340.00 USD | 78,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1668` | 5,450,000.00 USD | 5,450,000.00 USD | 42,580.00 USD | 52,290.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1672` | 1,980,000.00 USD | 1,980,000.00 USD | 46,590.00 USD | 2,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1672` | 5,650,000.00 USD | 5,650,000.00 USD | 135,250.00 USD | 62,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1675` | 2,020,000.00 USD | 2,020,000.00 USD | 20,040.00 USD | 1,990.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1676` | 5,870,000.00 USD | 5,870,000.00 USD | 84,020.00 USD | 141,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1678` | 2,040,000.00 USD | 2,040,000.00 USD | 22,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1680` | 6,090,000.00 USD | 6,090,000.00 USD | 121,860.00 USD | 80,270.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1681` | 2,170,000.00 USD | 2,170,000.00 USD | 120,850.00 USD | 4,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1684` | 2,280,000.00 USD | 2,280,000.00 USD | 54,020.00 USD | 26,600.00 USD | 32,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1684` | 6,160,000.00 USD | 6,160,000.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1687` | 2,310,000.00 USD | 2,310,000.00 USD | 6,560.00 USD | 5,840.00 USD | 23,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1688` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1690` | 2,360,000.00 USD | 2,360,000.00 USD | 18,380.00 USD | 9,870.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1692` | 6,320,000.00 USD | 6,320,000.00 USD | 33,660.00 USD | 70,740.00 USD | 40,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1693` | 2,530,000.00 USD | 2,530,000.00 USD | 84,630.00 USD | 74,940.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1695` | 394.60 USD | 28,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1696` | 2,580,000.00 USD | 2,580,000.00 USD | 23,530.00 USD | 16,310.00 USD | 6,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1696` | 6,470,000.00 USD | 6,470,000.00 USD | 17,360.00 USD | 87,350.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1699` | 2,660,000.00 USD | 2,660,000.00 USD | 26,000.00 USD | 56,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1700` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 25,330.00 USD | 41,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1702` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1704` | 6,640,000.00 USD | 6,640,000.00 USD | 55,170.00 USD | 46,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1705` | 2,700,000.00 USD | 2,700,000.00 USD | 14,190.00 USD | 20,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1708` | 2,820,000.00 USD | 2,820,000.00 USD | 39,520.00 USD | 65,470.00 USD | 13,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1708` | 6,730,000.00 USD | 6,730,000.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1711` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 4,910.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1714` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 12,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1716` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 42,020.00 USD | 15,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1717` | 2,910,000.00 USD | 2,910,000.00 USD | 9,570.00 USD | 34,120.00 USD | 19,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1720` | 3,000,000.00 USD | 3,000,000.00 USD | 80,090.00 USD | 1,590.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1720` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 0.00 USD | 161,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1723` | 3,130,000.00 USD | 3,130,000.00 USD | 54,130.00 USD | 16,860.00 USD | 66,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1724` | 7,270,000.00 USD | 7,270,000.00 USD | 118,060.00 USD | 0.00 USD | 208,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1726` | 3,160,000.00 USD | 3,160,000.00 USD | 8,230.00 USD | 2,410.00 USD | 12,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1729` | 3,180,000.00 USD | 3,180,000.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1732` | 3,190,000.00 USD | 3,190,000.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1732` | 7,760,000.00 USD | 7,760,000.00 USD | 476,430.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1735` | 3,220,000.00 USD | 3,220,000.00 USD | 14,970.00 USD | 9,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1738` | 3,250,000.00 USD | 3,250,000.00 USD | 18,610.00 USD | 2,310.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1740` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 0.00 USD | 83,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1741` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 1,600.00 USD | 5,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1744` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 2,460.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1744` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1747` | 3,310,000.00 USD | 3,310,000.00 USD | 8,530.00 USD | 0.00 USD | 31,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1748` | 7,940,000.00 USD | 7,940,000.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1750` | 3,410,000.00 USD | 3,410,000.00 USD | 80,070.00 USD | 2,280.00 USD | 22,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1752` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 0.00 USD | 291,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1753` | 3,480,000.00 USD | 3,480,000.00 USD | 32,240.00 USD | 0.00 USD | 33,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1756` | 3,600,000.00 USD | 3,600,000.00 USD | 23,610.00 USD | 27,640.00 USD | 73,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1756` | 8,530,000.00 USD | 8,530,000.00 USD | 112,930.00 USD | 0.00 USD | 186,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1759` | 3,760,000.00 USD | 3,760,000.00 USD | 85,450.00 USD | 31,960.00 USD | 36,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1760` | 8,920,000.00 USD | 8,920,000.00 USD | 277,910.00 USD | 77,870.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1762` | 3,980,000.00 USD | 3,980,000.00 USD | 72,450.00 USD | 83,100.00 USD | 66,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1764` | 9,580,000.00 USD | 9,580,000.00 USD | 353,950.00 USD | 270,450.00 USD | 40,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1765` | 4,070,000.00 USD | 4,070,000.00 USD | 20,220.00 USD | 28,990.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1765` | 3,240.00 USD | 31,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1768` | 4,240,000.00 USD | 4,240,000.00 USD | 19,860.00 USD | 83,210.00 USD | 62,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1768` | 9,960,000.00 USD | 9,960,000.00 USD | 191,690.00 USD | 154,100.00 USD | 31,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1771` | 4,330,000.00 USD | 4,330,000.00 USD | 43,430.00 USD | 19,520.00 USD | 24,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1772` | 10,230,000.00 USD | 10,230,000.00 USD | 98,390.00 USD | 153,480.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1774` | 4,400,000.00 USD | 4,400,000.00 USD | 20,200.00 USD | 30,630.00 USD | 26,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1776` | 10,480,000.00 USD | 10,480,000.00 USD | 186,770.00 USD | 59,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1777` | 4,550,000.00 USD | 4,550,000.00 USD | 42,080.00 USD | 81,500.00 USD | 24,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1780` | 4,590,000.00 USD | 4,590,000.00 USD | 11,580.00 USD | 9,760.00 USD | 13,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1780` | 10,740,000.00 USD | 10,740,000.00 USD | 52,730.00 USD | 46,410.00 USD | 157,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1783` | 4,650,000.00 USD | 4,650,000.00 USD | 27,640.00 USD | 15,680.00 USD | 19,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1784` | 10,960,000.00 USD | 10,960,000.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1786` | 4,700,000.00 USD | 4,700,000.00 USD | 16,960.00 USD | 31,510.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1788` | 11,130,000.00 USD | 11,130,000.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1789` | 4,770,000.00 USD | 4,770,000.00 USD | 15,890.00 USD | 31,190.00 USD | 20,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1792` | 4,820,000.00 USD | 4,820,000.00 USD | 13,950.00 USD | 16,470.00 USD | 18,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1792` | 11,370,000.00 USD | 11,370,000.00 USD | 182,810.00 USD | 46,960.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1795` | 4,930,000.00 USD | 4,930,000.00 USD | 53,160.00 USD | 43,180.00 USD | 18,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1795` | 525.67 USD | 31,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1796` | 11,450,000.00 USD | 11,450,000.00 USD | 17,130.00 USD | 26,110.00 USD | 44,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1798` | 4,990,000.00 USD | 4,990,000.00 USD | 15,420.00 USD | 17,120.00 USD | 21,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1800` | 11,570,000.00 USD | 11,570,000.00 USD | 12,940.00 USD | 34,680.00 USD | 73,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1801` | 5,040,000.00 USD | 5,040,000.00 USD | 12,470.00 USD | 23,820.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1804` | 5,090,000.00 USD | 5,090,000.00 USD | 10,530.00 USD | 16,830.00 USD | 19,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1804` | 11,670,000.00 USD | 11,670,000.00 USD | 35,280.00 USD | 32,850.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1807` | 5,130,000.00 USD | 5,130,000.00 USD | 16,640.00 USD | 17,460.00 USD | 9,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1808` | 11,840,000.00 USD | 11,840,000.00 USD | 35,050.00 USD | 67,250.00 USD | 73,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1810` | 5,170,000.00 USD | 5,170,000.00 USD | 12,880.00 USD | 15,840.00 USD | 8,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1812` | 11,990,000.00 USD | 11,990,000.00 USD | 64,990.00 USD | 29,900.00 USD | 50,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1813` | 5,230,000.00 USD | 5,230,000.00 USD | 14,660.00 USD | 37,850.00 USD | 15,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1816` | 5,260,000.00 USD | 5,260,000.00 USD | 13,550.00 USD | 0.00 USD | 15,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1816` | 12,130,000.00 USD | 12,130,000.00 USD | 69,700.00 USD | 33,940.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1819` | 5,290,000.00 USD | 5,290,000.00 USD | 6,740.00 USD | 12,120.00 USD | 6,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1820` | 12,290,000.00 USD | 12,290,000.00 USD | 65,350.00 USD | 54,880.00 USD | 43,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1822` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 21,610.00 USD | 1,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1824` | 12,500,000.00 USD | 12,500,000.00 USD | 80,350.00 USD | 17,880.00 USD | 112,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1825` | 5,350,000.00 USD | 5,350,000.00 USD | 18,910.00 USD | 1,780.00 USD | 11,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1828` | 5,360,000.00 USD | 5,360,000.00 USD | 6,840.00 USD | 5,270.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1828` | 12,680,000.00 USD | 12,680,000.00 USD | 79,610.00 USD | 29,630.00 USD | 69,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1832` | 12,900,000.00 USD | 12,900,000.00 USD | 108,540.00 USD | 31,590.00 USD | 74,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1834` | 5,370,000.00 USD | 5,370,000.00 USD | 2,670.00 USD | 0.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1836` | 13,230,000.00 USD | 13,230,000.00 USD | 172,660.00 USD | 110,870.00 USD | 52,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1837` | 5,370,000.00 USD | 5,370,000.00 USD | 3,610.00 USD | 2,640.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1840` | 5,390,000.00 USD | 5,390,000.00 USD | 5,430.00 USD | 1,970.00 USD | 12,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1840` | 13,580,000.00 USD | 13,580,000.00 USD | 141,620.00 USD | 50,840.00 USD | 151,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1843` | 5,400,000.00 USD | 5,400,000.00 USD | 1,030.00 USD | 3,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1844` | 13,770,000.00 USD | 13,770,000.00 USD | 94,510.00 USD | 20,390.00 USD | 82,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1845` | 752.59 USD | 32,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1846` | 5,420,000.00 USD | 5,420,000.00 USD | 9,830.00 USD | 1,840.00 USD | 7,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1848` | 13,920,000.00 USD | 13,920,000.00 USD | 35,280.00 USD | 69,910.00 USD | 41,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1849` | 5,440,000.00 USD | 5,440,000.00 USD | 12,130.00 USD | 5,200.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1852` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 2,580.00 USD | 1,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1852` | 14,370,000.00 USD | 14,370,000.00 USD | 168,270.00 USD | 28,290.00 USD | 251,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1855` | 5,450,000.00 USD | 5,450,000.00 USD | 7,630.00 USD | 0.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1856` | 14,600,000.00 USD | 14,600,000.00 USD | 100,160.00 USD | 21,030.00 USD | 106,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1858` | 5,480,000.00 USD | 5,480,000.00 USD | 10,290.00 USD | 4,100.00 USD | 14,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1860` | 14,840,000.00 USD | 14,840,000.00 USD | 64,600.00 USD | 48,330.00 USD | 127,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1861` | 5,500,000.00 USD | 5,500,000.00 USD | 5,860.00 USD | 2,970.00 USD | 5,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1864` | 5,500,000.00 USD | 5,500,000.00 USD | 1,870.00 USD | 0.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1864` | 14,990,000.00 USD | 14,990,000.00 USD | 48,260.00 USD | 44,140.00 USD | 61,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1867` | 5,520,000.00 USD | 5,520,000.00 USD | 3,300.00 USD | 0.00 USD | 8,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1868` | 15,230,000.00 USD | 15,230,000.00 USD | 133,990.00 USD | 51,510.00 USD | 56,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1870` | 5,530,000.00 USD | 5,530,000.00 USD | 4,960.00 USD | 5,040.00 USD | 8,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1872` | 5,550,000.00 USD | 5,550,000.00 USD | 12,350.00 USD | 1,900.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1872` | 15,720,000.00 USD | 15,720,000.00 USD | 188,990.00 USD | 146,600.00 USD | 155,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1876` | 15,860,000.00 USD | 15,860,000.00 USD | 65,910.00 USD | 23,180.00 USD | 43,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1880` | 15,980,000.00 USD | 15,980,000.00 USD | 57,250.00 USD | 35,940.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1884` | 16,040,000.00 USD | 16,040,000.00 USD | 14,000.00 USD | 35,430.00 USD | 9,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1888` | 16,160,000.00 USD | 16,160,000.00 USD | 22,970.00 USD | 4,800.00 USD | 88,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1892` | 16,240,000.00 USD | 16,240,000.00 USD | 49,980.00 USD | 2,860.00 USD | 34,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1896` | 16,320,000.00 USD | 16,320,000.00 USD | 42,320.00 USD | 11,820.00 USD | 18,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1900` | 16,370,000.00 USD | 16,370,000.00 USD | 0.00 USD | 29,650.00 USD | 20,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1904` | 16,410,000.00 USD | 16,410,000.00 USD | 14,330.00 USD | 17,690.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1908` | 16,540,000.00 USD | 16,540,000.00 USD | 33,940.00 USD | 44,480.00 USD | 52,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1912` | 16,560,000.00 USD | 16,560,000.00 USD | 0.00 USD | 9,380.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1916` | 16,590,000.00 USD | 16,590,000.00 USD | 7,460.00 USD | 12,040.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1920` | 16,600,000.00 USD | 16,600,000.00 USD | 0.00 USD | 5,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1924` | 16,620,000.00 USD | 16,620,000.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1928` | 16,640,000.00 USD | 16,640,000.00 USD | 11,600.00 USD | 7,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1944` | 16,640,000.00 USD | 16,640,000.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1945` | 623.68 USD | 33,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1952` | 16,650,000.00 USD | 16,650,000.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1955` | 860.20 USD | 34,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1956` | 16,660,000.00 USD | 16,660,000.00 USD | 4,860.00 USD | 2,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1960` | 16,670,000.00 USD | 16,670,000.00 USD | 5,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1964` | 16,690,000.00 USD | 16,690,000.00 USD | 6,470.00 USD | 2,700.00 USD | 10,990.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.0345` | 1,880,000.00 USD | 0.00 USD | 345.00 USD | `-77.85%` | `10,000,000,000,000.00` |
| `Live` | `Long` | `0.0385` | 1,880,000.00 USD | 0.00 USD | 1,490.00 USD | `-75.28%` | `38,823,900,000,000.00` |
| `Live` | `Long` | `0.0405` | 1,880,000.00 USD | 0.00 USD | 157.95 USD | `-74.00%` | `3,900,000,000,000.00` |
| `Live` | `Long` | `0.0415` | 1,880,000.00 USD | 0.00 USD | 1,220.00 USD | `-73.35%` | `29,299,500,000,000.00` |
| `Live` | `Long` | `0.0425` | 1,880,000.00 USD | 0.00 USD | 424.66 USD | `-72.71%` | `9,991,900,000,000.00` |
| `Live` | `Long` | `0.0455` | 1,880,000.00 USD | 0.00 USD | 910.00 USD | `-70.78%` | `20,000,000,000,000.00` |
| `Live` | `Long` | `0.0475` | 1,880,000.00 USD | 0.00 USD | 167,030.00 USD | `-69.50%` | `3,516,409,800,000,000.00` |
| `Live` | `Long` | `0.0495` | 1,710,000.00 USD | 0.00 USD | 109.52 USD | `-68.22%` | `2,212,600,000,000.00` |
| `Live` | `Long` | `0.0505` | 1,710,000.00 USD | 0.00 USD | 610.70 USD | `-67.57%` | `12,093,000,000,000.00` |
| `Live` | `Long` | `0.0515` | 1,710,000.00 USD | 0.00 USD | 170.28 USD | `-66.93%` | `3,306,500,000,000.00` |
| `Live` | `Long` | `0.0525` | 1,710,000.00 USD | 0.00 USD | 289.43 USD | `-66.29%` | `5,513,000,000,000.00` |
| `Live` | `Long` | `0.0545` | 1,710,000.00 USD | 0.00 USD | 2,270.00 USD | `-65.01%` | `41,635,000,000,000.00` |
| `Live` | `Long` | `0.0565` | 1,710,000.00 USD | 0.00 USD | 16,160.00 USD | `-63.72%` | `285,941,000,000,000.00` |
| `Live` | `Long` | `0.0575` | 1,690,000.00 USD | 0.00 USD | 718.35 USD | `-63.08%` | `12,493,000,000,000.00` |
| `Live` | `Long` | `0.0585` | 1,690,000.00 USD | 0.00 USD | 2,000.00 USD | `-62.44%` | `34,249,500,000,000.00` |
| `Live` | `Long` | `0.0595` | 1,690,000.00 USD | 0.00 USD | 3,870.00 USD | `-61.80%` | `65,000,000,000,000.00` |
| `Live` | `Long` | `0.0625` | 1,680,000.00 USD | 0.00 USD | 9,180.00 USD | `-59.87%` | `146,916,000,000,000.00` |
| `Live` | `Long` | `0.0645` | 1,680,000.00 USD | 0.00 USD | 6,570.00 USD | `-58.58%` | `101,831,000,000,000.00` |
| `Live` | `Long` | `0.0675` | 1,670,000.00 USD | 0.00 USD | 99,790.00 USD | `-56.66%` | `1,478,385,900,000,000.00` |
| `Live` | `Long` | `0.0685` | 1,570,000.00 USD | 0.00 USD | 313.22 USD | `-56.02%` | `4,572,600,000,000.00` |
| `Live` | `Long` | `0.0695` | 1,570,000.00 USD | 0.00 USD | 57,970.00 USD | `-55.37%` | `834,132,000,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,510,000.00 USD | 0.00 USD | 3,390.00 USD | `-54.73%` | `48,029,900,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,510,000.00 USD | 0.00 USD | 5,840.00 USD | `-54.09%` | `81,674,400,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,500,000.00 USD | 0.00 USD | 111.58 USD | `-53.45%` | `1,539,100,000,000.00` |
| `Live` | `Long` | `0.0735` | 1,500,000.00 USD | 0.00 USD | 2,760.00 USD | `-52.81%` | `37,551,700,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,500,000.00 USD | 0.00 USD | 2,190.00 USD | `-52.16%` | `29,366,900,000,000.00` |
| `Live` | `Long` | `0.0755` | 1,500,000.00 USD | 0.00 USD | 948.08 USD | `-51.52%` | `12,557,400,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,500,000.00 USD | 0.00 USD | 14,690.00 USD | `-50.88%` | `192,029,300,000,000.00` |
| `Live` | `Long` | `0.0775` | 1,480,000.00 USD | 0.00 USD | 172.24 USD | `-50.24%` | `2,222,400,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,480,000.00 USD | 0.00 USD | 19,440.00 USD | `-48.95%` | `244,490,900,000,000.00` |
| `Live` | `Long` | `0.0815` | 1,460,000.00 USD | 0.00 USD | 11,060.00 USD | `-47.67%` | `135,660,000,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,450,000.00 USD | 0.00 USD | 13,840.00 USD | `-47.03%` | `167,742,900,000,000.00` |
| `Live` | `Long` | `0.0835` | 1,440,000.00 USD | 0.00 USD | 112.78 USD | `-46.39%` | `1,350,600,000,000.00` |
| `Live` | `Long` | `0.0845` | 1,440,000.00 USD | 0.00 USD | 4,970.00 USD | `-45.74%` | `58,826,500,000,000.00` |
| `Live` | `Long` | `0.0865` | 1,430,000.00 USD | 0.00 USD | 19,460.00 USD | `-44.46%` | `224,937,400,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,410,000.00 USD | 0.00 USD | 5,240.00 USD | `-43.17%` | `59,174,000,000,000.00` |
| `Live` | `Long` | `0.0895` | 1,410,000.00 USD | 0.00 USD | 2,940.00 USD | `-42.53%` | `32,890,000,000,000.00` |
| `Live` | `Long` | `0.0905` | 1,400,000.00 USD | 0.00 USD | 1,360.00 USD | `-41.89%` | `15,000,000,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,400,000.00 USD | 0.00 USD | 2,040.00 USD | `-40.61%` | `22,044,300,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,400,000.00 USD | 0.00 USD | 814.24 USD | `-39.96%` | `8,708,500,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,400,000.00 USD | 0.00 USD | 1,510.00 USD | `-39.32%` | `16,031,700,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,400,000.00 USD | 0.00 USD | 10,260.00 USD | `-38.04%` | `106,356,900,000,000.00` |
| `Live` | `Long` | `0.0975` | 1,390,000.00 USD | 0.00 USD | 145.24 USD | `-37.40%` | `1,489,600,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,390,000.00 USD | 0.00 USD | 5,490.00 USD | `-36.75%` | `55,761,200,000,000.00` |
| `Live` | `Long` | `0.0995` | 1,380,000.00 USD | 0.00 USD | 17,930.00 USD | `-36.11%` | `180,196,800,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,360,000.00 USD | 0.00 USD | 12,910.00 USD | `-35.47%` | `128,479,200,000,000.00` |
| `Live` | `Long` | `0.1025` | 1,350,000.00 USD | 0.00 USD | 773.66 USD | `-34.19%` | `7,547,900,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,350,000.00 USD | 0.00 USD | 112,680.00 USD | `-33.54%` | `1,088,726,000,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,240,000.00 USD | 0.00 USD | 7,480.00 USD | `-32.90%` | `71,622,400,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,230,000.00 USD | 0.00 USD | 9,340.00 USD | `-32.26%` | `88,538,700,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,220,000.00 USD | 0.00 USD | 906.89 USD | `-31.62%` | `8,515,400,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,220,000.00 USD | 0.00 USD | 1,060.00 USD | `-30.97%` | `9,856,300,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,220,000.00 USD | 0.00 USD | 11,830.00 USD | `-30.33%` | `109,049,400,000,000.00` |
| `Live` | `Long` | `0.1095` | 1,210,000.00 USD | 0.00 USD | 605.37 USD | `-29.69%` | `5,528,500,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,210,000.00 USD | 0.00 USD | 534.49 USD | `-29.05%` | `4,837,000,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,210,000.00 USD | 0.00 USD | 425.50 USD | `-28.41%` | `3,816,100,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,210,000.00 USD | 0.00 USD | 3,850.00 USD | `-27.12%` | `33,939,200,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,200,000.00 USD | 0.00 USD | 10,720.00 USD | `-26.48%` | `93,666,300,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,190,000.00 USD | 0.00 USD | 9,880.00 USD | `-25.84%` | `85,506,700,000,000.00` |
| `Live` | `Long` | `0.1165` | 1,180,000.00 USD | 0.00 USD | 6,230.00 USD | `-25.20%` | `53,476,700,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,170,000.00 USD | 0.00 USD | 5,420.00 USD | `-24.55%` | `46,086,300,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,170,000.00 USD | 0.00 USD | 25,800.00 USD | `-23.91%` | `217,694,900,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,140,000.00 USD | 0.00 USD | 2,180.00 USD | `-23.27%` | `18,224,500,000,000.00` |
| `Live` | `Long` | `0.1205` | 1,140,000.00 USD | 0.00 USD | 11,970.00 USD | `-22.63%` | `99,341,000,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,130,000.00 USD | 0.00 USD | 303.75 USD | `-21.99%` | `2,500,000,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,130,000.00 USD | 0.00 USD | 19,200.00 USD | `-21.34%` | `156,730,200,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,110,000.00 USD | 0.00 USD | 39,990.00 USD | `-20.70%` | `323,846,100,000,000.00` |
| `Live` | `Long` | `0.1245` | 1,070,000.00 USD | 0.00 USD | 844.86 USD | `-20.06%` | `6,786,000,000,000.00` |
| `Live` | `Long` | `0.1255` | 1,070,000.00 USD | 0.00 USD | 4,850.00 USD | `-19.42%` | `38,646,100,000,000.00` |
| `Live` | `Long` | `0.1265` | 1,060,000.00 USD | 0.00 USD | 870.65 USD | `-18.77%` | `6,882,600,000,000.00` |
| `Live` | `Long` | `0.1285` | 1,060,000.00 USD | 0.00 USD | 9,780.00 USD | `-17.49%` | `76,071,500,000,000.00` |
| `Live` | `Long` | `0.1295` | 1,050,000.00 USD | 0.00 USD | 4,010.00 USD | `-16.85%` | `30,998,800,000,000.00` |
| `Live` | `Long` | `0.1305` | 1,050,000.00 USD | 0.00 USD | 16,660.00 USD | `-16.21%` | `127,649,400,000,000.00` |
| `Live` | `Long` | `0.1315` | 1,030,000.00 USD | 0.00 USD | 5,300.00 USD | `-15.56%` | `40,289,000,000,000.00` |
| `Live` | `Long` | `0.1325` | 1,030,000.00 USD | 0.00 USD | 13,320.00 USD | `-14.92%` | `100,492,800,000,000.00` |
| `Live` | `Long` | `0.1335` | 1,010,000.00 USD | 0.00 USD | 9,690.00 USD | `-14.28%` | `72,616,800,000,000.00` |
| `Live` | `Long` | `0.1345` | 1,000,000.00 USD | 0.00 USD | 741.71 USD | `-13.64%` | `5,514,600,000,000.00` |
| `Live` | `Long` | `0.1355` | 1,000,000.00 USD | 0.00 USD | 38,490.00 USD | `-13.00%` | `284,087,200,000,000.00` |
| `Live` | `Long` | `0.1365` | 965,090.00 USD | 0.00 USD | 53,980.00 USD | `-12.35%` | `395,435,300,000,000.00` |
| `Live` | `Long` | `0.1385` | 911,110.00 USD | 0.00 USD | 22,700.00 USD | `-11.07%` | `163,887,000,000,000.00` |
| `Live` | `Long` | `0.1395` | 888,410.00 USD | 0.00 USD | 6,570.00 USD | `-10.43%` | `47,074,500,000,000.00` |
| `Live` | `Long` | `0.1405` | 881,850.00 USD | 0.00 USD | 8,880.00 USD | `-9.79%` | `63,201,300,000,000.00` |
| `Live` | `Long` | `0.1415` | 872,970.00 USD | 0.00 USD | 6,590.00 USD | `-9.14%` | `46,604,500,000,000.00` |
| `Live` | `Long` | `0.1425` | 866,370.00 USD | 0.00 USD | 484,730.00 USD | `-8.50%` | `3,401,615,000,000,000.00` |
| `Live` | `Long` | `0.1435` | 381,640.00 USD | 0.00 USD | 28,290.00 USD | `-7.86%` | `197,141,900,000,000.00` |
| `Live` | `Long` | `0.1445` | 353,350.00 USD | 0.00 USD | 16,220.00 USD | `-7.22%` | `112,262,000,000,000.00` |
| `Live` | `Long` | `0.1455` | 337,130.00 USD | 0.00 USD | 2,110.00 USD | `-6.58%` | `14,479,100,000,000.00` |
| `Live` | `Long` | `0.1465` | 335,020.00 USD | 0.00 USD | 39,940.00 USD | `-5.93%` | `272,604,500,000,000.00` |
| `Live` | `Long` | `0.1475` | 295,090.00 USD | 0.00 USD | 95,530.00 USD | `-5.29%` | `647,688,600,000,000.00` |
| `Live` | `Long` | `0.1485` | 199,550.00 USD | 0.00 USD | 9,220.00 USD | `-4.65%` | `62,064,400,000,000.00` |
| `Live` | `Long` | `0.1495` | 190,340.00 USD | 0.00 USD | 35,480.00 USD | `-4.01%` | `237,301,800,000,000.00` |
| `Live` | `Long` | `0.1505` | 154,860.00 USD | 0.00 USD | 148,730.00 USD | `-3.36%` | `988,222,600,000,000.00` |
| `Live` | `Long` | `0.1515` | 6,130.00 USD | 0.00 USD | 6,130.00 USD | `-2.72%` | `40,475,500,000,000.00` |
| `Live` | `Short` | `0.1605` | 2,500.00 USD | 2,500.00 USD | 0.00 USD | `+3.06%` | `15,570,100,000,000.00` |
| `Live` | `Short` | `0.1635` | 2,880.00 USD | 380.25 USD | 0.00 USD | `+4.98%` | `2,325,700,000,000.00` |
| `Live` | `Short` | `0.1645` | 5,360.00 USD | 2,480.00 USD | 0.00 USD | `+5.62%` | `15,106,200,000,000.00` |
| `Live` | `Short` | `0.1655` | 6,270.00 USD | 909.51 USD | 0.00 USD | `+6.27%` | `5,495,500,000,000.00` |
| `Live` | `Short` | `0.1665` | 32,530.00 USD | 26,250.00 USD | 0.00 USD | `+6.91%` | `157,687,300,000,000.00` |
| `Live` | `Short` | `0.1675` | 33,170.00 USD | 636.75 USD | 0.00 USD | `+7.55%` | `3,801,500,000,000.00` |
| `Live` | `Short` | `0.1705` | 41,180.00 USD | 8,020.00 USD | 0.00 USD | `+9.48%` | `47,030,700,000,000.00` |
| `Live` | `Short` | `0.1745` | 55,780.00 USD | 14,600.00 USD | 0.00 USD | `+12.05%` | `83,658,700,000,000.00` |
| `Live` | `Short` | `0.1765` | 59,680.00 USD | 3,900.00 USD | 0.00 USD | `+13.33%` | `22,103,900,000,000.00` |
| `Live` | `Short` | `0.1835` | 60,430.00 USD | 748.51 USD | 0.00 USD | `+17.82%` | `4,079,100,000,000.00` |
| `Live` | `Short` | `0.1845` | 61,210.00 USD | 777.21 USD | 0.00 USD | `+18.47%` | `4,212,500,000,000.00` |
| `Live` | `Short` | `0.1945` | 61,830.00 USD | 623.68 USD | 0.00 USD | `+24.89%` | `3,206,600,000,000.00` |
| `Live` | `Short` | `0.1955` | 62,690.00 USD | 860.20 USD | 0.00 USD | `+25.53%` | `4,400,000,000,000.00` |
| `Live` | `Short` | `0.1975` | 62,840.00 USD | 150.10 USD | 0.00 USD | `+26.81%` | `760,000,000,000.00` |
| `Live` | `Short` | `0.1995` | 64,400.00 USD | 1,550.00 USD | 0.00 USD | `+28.10%` | `7,794,100,000,000.00` |
| `Live` | `Short` | `0.2055` | 75,990.00 USD | 11,590.00 USD | 0.00 USD | `+31.95%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2085` | 76,190.00 USD | 198.08 USD | 0.00 USD | `+33.88%` | `950,000,000,000.00` |
| `Live` | `Short` | `0.2095` | 76,350.00 USD | 164.23 USD | 0.00 USD | `+34.52%` | `783,900,000,000.00` |
| `Live` | `Short` | `0.2135` | 92,980.00 USD | 16,620.00 USD | 0.00 USD | `+37.09%` | `77,855,100,000,000.00` |
| `Live` | `Short` | `0.2155` | 134,310.00 USD | 41,330.00 USD | 0.00 USD | `+38.37%` | `191,801,700,000,000.00` |
| `Live` | `Short` | `0.2195` | 248,230.00 USD | 113,920.00 USD | 0.00 USD | `+40.94%` | `518,989,500,000,000.00` |
| `Live` | `Short` | `0.2235` | 248,460.00 USD | 229.15 USD | 0.00 USD | `+43.51%` | `1,025,300,000,000.00` |
| `Live` | `Short` | `0.2255` | 248,610.00 USD | 154.78 USD | 0.00 USD | `+44.79%` | `686,400,000,000.00` |
| `Live` | `Short` | `0.2275` | 248,710.00 USD | 100.30 USD | 0.00 USD | `+46.08%` | `440,900,000,000.00` |
| `Live` | `Short` | `0.2285` | 249,800.00 USD | 1,090.00 USD | 0.00 USD | `+46.72%` | `4,754,900,000,000.00` |
| `Live` | `Short` | `0.2295` | 256,620.00 USD | 6,820.00 USD | 0.00 USD | `+47.36%` | `29,727,000,000,000.00` |
| `Live` | `Short` | `0.2335` | 281,620.00 USD | 25,000.00 USD | 0.00 USD | `+49.93%` | `107,049,400,000,000.00` |
| `Live` | `Short` | `0.2355` | 344,970.00 USD | 63,350.00 USD | 0.00 USD | `+51.21%` | `269,020,500,000,000.00` |
| `Live` | `Short` | `0.2375` | 345,070.00 USD | 102.62 USD | 0.00 USD | `+52.50%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2405` | 345,430.00 USD | 361.66 USD | 0.00 USD | `+54.42%` | `1,503,800,000,000.00` |
| `Live` | `Short` | `0.2425` | 346,230.00 USD | 796.25 USD | 0.00 USD | `+55.71%` | `3,283,500,000,000.00` |
| `Live` | `Short` | `0.2445` | 346,460.00 USD | 231.03 USD | 0.00 USD | `+56.99%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2465` | 347,190.00 USD | 728.26 USD | 0.00 USD | `+58.28%` | `2,954,400,000,000.00` |
| `Live` | `Short` | `0.2545` | 347,740.00 USD | 546.54 USD | 0.00 USD | `+63.41%` | `2,147,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 351,600.00 USD | 3,870.00 USD | 0.00 USD | `+64.70%` | `15,070,700,000,000.00` |
| `Live` | `Short` | `0.2575` | 380,510.00 USD | 28,910.00 USD | 0.00 USD | `+65.34%` | `112,272,400,000,000.00` |
| `Live` | `Short` | `0.2585` | 433,130.00 USD | 52,620.00 USD | 0.00 USD | `+65.98%` | `203,548,800,000,000.00` |
| `Live` | `Short` | `0.2615` | 433,280.00 USD | 154.94 USD | 0.00 USD | `+67.91%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2685` | 433,510.00 USD | 226.51 USD | 0.00 USD | `+72.40%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2715` | 447,020.00 USD | 13,510.00 USD | 0.00 USD | `+74.33%` | `49,773,600,000,000.00` |
| `Live` | `Short` | `0.2725` | 447,240.00 USD | 214.21 USD | 0.00 USD | `+74.97%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2735` | 450,550.00 USD | 3,310.00 USD | 0.00 USD | `+75.61%` | `12,102,000,000,000.00` |
| `Live` | `Short` | `0.2745` | 478,440.00 USD | 27,890.00 USD | 0.00 USD | `+76.26%` | `101,607,700,000,000.00` |
| `Live` | `Short` | `0.2795` | 478,920.00 USD | 482.84 USD | 0.00 USD | `+79.47%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2905` | 496,000.00 USD | 17,080.00 USD | 0.00 USD | `+86.53%` | `58,786,700,000,000.00` |
| `Live` | `Short` | `0.2915` | 496,190.00 USD | 187.26 USD | 0.00 USD | `+87.17%` | `642,400,000,000.00` |
| `Live` | `Short` | `0.2925` | 496,650.00 USD | 464.84 USD | 0.00 USD | `+87.81%` | `1,589,200,000,000.00` |
| `Live` | `Short` | `0.2935` | 499,290.00 USD | 2,640.00 USD | 0.00 USD | `+88.46%` | `9,000,000,000,000.00` |
| `Live` | `Short` | `0.2945` | 499,760.00 USD | 468.40 USD | 0.00 USD | `+89.10%` | `1,590,500,000,000.00` |
| `Live` | `Short` | `0.2955` | 500,340.00 USD | 574.36 USD | 0.00 USD | `+89.74%` | `1,943,700,000,000.00` |
| `Live` | `Short` | `0.2995` | 502,620.00 USD | 2,280.00 USD | 0.00 USD | `+92.31%` | `7,608,100,000,000.00` |
| `Live` | `Short` | `0.3105` | 502,840.00 USD | 225.42 USD | 0.00 USD | `+99.37%` | `726,000,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

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
| `15M` | `ARB` | `46.82%` | `53.18%` | `0.88` | 2,240,000.00 USD |
| `15M` | `Binance` | `47.41%` | `52.59%` | `0.90` | 851,170.00 USD |
| `15M` | `OKX` | `51.58%` | `48.42%` | `1.07` | 197,060.00 USD |
| `15M` | `Bybit` | `44.55%` | `55.45%` | `0.80` | 319,810.00 USD |
| `15M` | `KuCoin` | `16.22%` | `83.78%` | `0.19` | 9,250.00 USD |
| `15M` | `Gate` | `43.76%` | `56.24%` | `0.78` | 51,430.00 USD |
| `15M` | `Bitget` | `18.72%` | `81.28%` | `0.23` | 59,870.00 USD |
| `15M` | `BingX` | `44.46%` | `55.54%` | `0.80` | 68,720.00 USD |
| `15M` | `MEXC` | `34.61%` | `65.39%` | `0.53` | 200,110.00 USD |
| `15M` | `Bitunix` | `49.85%` | `50.15%` | `0.99` | 25,800.00 USD |
| `15M` | `Hyperliquid` | `41.47%` | `58.53%` | `0.71` | 37,150.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `52.01%` | `47.99%` | `1.08` | 357,610.00 USD |
| `15M` | `Crypto.com` | `13.99%` | `86.01%` | `0.16` | 4.29 USD |
| `15M` | `WhiteBIT` | `93.35%` | `6.65%` | `14.04` | 52,250.00 USD |
| `15M` | `HTX` | `20.86%` | `79.14%` | `0.26` | 437.20 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `12.54%` | `87.46%` | `0.14` | 3,420.00 USD |
| `15M` | `Aster` | `16.41%` | `83.59%` | `0.20` | 112.61 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `32.88%` | `67.12%` | `0.49` | 982.03 USD |
| `15M` | `Whale Positions` | `47.41%` | `52.59%` | `0.90` | 851,170.00 USD |
| `15M` | `Global Accounts` | `46.82%` | `53.18%` | `0.88` | 2,240,000.00 USD |
| `1H` | `ARB` | `50.46%` | `49.54%` | `1.02` | 9,260,000.00 USD |
| `1H` | `Binance` | `48.81%` | `51.19%` | `0.95` | 3,550,000.00 USD |
| `1H` | `OKX` | `53.72%` | `46.28%` | `1.16` | 881,720.00 USD |
| `1H` | `Bybit` | `54.92%` | `45.08%` | `1.22` | 1,300,000.00 USD |
| `1H` | `KuCoin` | `35.47%` | `64.53%` | `0.55` | 26,210.00 USD |
| `1H` | `Gate` | `60.48%` | `39.52%` | `1.53` | 144,730.00 USD |
| `1H` | `Bitget` | `45.22%` | `54.78%` | `0.83` | 287,330.00 USD |
| `1H` | `BingX` | `56.91%` | `43.09%` | `1.32` | 314,280.00 USD |
| `1H` | `MEXC` | `45.1%` | `54.9%` | `0.82` | 632,400.00 USD |
| `1H` | `Bitunix` | `44.05%` | `55.95%` | `0.79` | 115,840.00 USD |
| `1H` | `Hyperliquid` | `52.83%` | `47.17%` | `1.12` | 130,880.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `45.26%` | `54.74%` | `0.83` | 1,670,000.00 USD |
| `1H` | `Crypto.com` | `7.19%` | `92.81%` | `0.08` | 4,060.00 USD |
| `1H` | `WhiteBIT` | `96.74%` | `3.26%` | `29.67` | 183,210.00 USD |
| `1H` | `HTX` | `20.99%` | `79.01%` | `0.27` | 1,580.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `48.19%` | `51.81%` | `0.93` | 5,810.00 USD |
| `1H` | `Aster` | `37.74%` | `62.26%` | `0.61` | 222.74 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `27.9%` | `72.1%` | `0.39` | 3,590.00 USD |
| `1H` | `Whale Positions` | `48.81%` | `51.19%` | `0.95` | 3,550,000.00 USD |
| `1H` | `Global Accounts` | `50.46%` | `49.54%` | `1.02` | 9,260,000.00 USD |
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
| `5:00 UTC` | `0.1682` | `0.1683` | `0.1682` | `0.1688` | `0.1681` | 452,736.37 USD | 213,244.89 USD | 239,491.48 USD | -26,246.58 USD | `-5.80%` | `7B / 12S` |
| `0:00 UTC` | `0.1667` | `0.1655` | `0.1667` | `0.1684` | `0.1640` | 2,535,332.38 USD | 1,148,875.51 USD | 1,386,456.87 USD | -237,581.36 USD | `-9.37%` | `2B / 23S` |
| `5:00 UTC` | `0.1650` | `0.1654` | `0.1650` | `0.1661` | `0.1649` | 718,046.47 USD | 414,320.10 USD | 303,726.37 USD | 110,593.73 USD | `+15.40%` | `33B / 14S` |
| `0:00 UTC` | `0.1592` | `0.1590` | `0.1592` | `0.1655` | `0.1541` | 10,418,999.97 USD | 3,996,711.76 USD | 6,422,288.21 USD | -2,425,576.45 USD | `-23.28%` | `2B / 33S` |
| `5:00 UTC` | `0.1535` | `0.1536` | `0.1535` | `0.1560` | `0.1508` | 10,296,961.64 USD | 4,216,389.14 USD | 6,080,572.50 USD | -1,864,183.37 USD | `-18.10%` | `2B / 11S` |
| `0:00 UTC` | `0.1558` | `0.1546` | `0.1558` | `0.1572` | `0.1528` | 5,930,771.66 USD | 3,398,964.11 USD | 2,531,807.55 USD | 867,156.57 USD | `+14.62%` | `22B / 10S` |
| `5:00 UTC` | `0.1590` | `0.1587` | `0.1590` | `0.1599` | `0.1565` | 3,702,564.80 USD | 1,807,551.39 USD | 1,895,013.41 USD | -87,462.01 USD | `-2.36%` | `26B / 13S` |
| `0:00 UTC` | `0.1596` | `0.1591` | `0.1596` | `0.1603` | `0.1573` | 4,839,053.12 USD | 2,292,867.68 USD | 2,546,185.45 USD | -253,317.77 USD | `-5.23%` | `10B / 17S` |
| `5:00 UTC` | `0.1575` | `0.1570` | `0.1575` | `0.1586` | `0.1556` | 1,633,700.68 USD | 751,464.39 USD | 882,236.29 USD | -130,771.91 USD | `-8.00%` | `12B / 24S` |
| `0:00 UTC` | `0.1558` | `0.1559` | `0.1558` | `0.1566` | `0.1556` | 289,149.69 USD | 172,265.39 USD | 116,884.30 USD | 55,381.09 USD | `+19.15%` | `24B / 13S` |

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
| `5m` | -56,680.00 USD | -783,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -161,030.00 USD | -933,370.00 USD | **`DISTRIBUTION`** |
| `30m` | -15,510.00 USD | -1,680,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 41,300.00 USD | 729,490.00 USD | **`ACCUMULATION`** |
| `2h` | -1,610,000.00 USD | -5,690,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -2,060,000.00 USD | -6,170,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -2,220,000.00 USD | -8,200,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,020,000.00 USD | -9,810,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,680,000.00 USD | -10,310,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,880,000.00 USD | -10,970,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,030,000.00 USD | -37,050,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -34,240,000.00 USD | -168,290,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-56.68K` | 15m=`-161.03K` | 1h=`+41.30K` | 24h=`-2.88M`
* Futures Capital Netflows: 5m=`-783.00K` | 15m=`-933.37K` | 1h=`+729.49K` | 24h=`-10.97M`
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
  * `2026-10-30 03:29:54 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:54 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:31:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
