# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 04:38:03 IST` (`2026-10-29 23:08:03 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1543` | `0.1547` | `0.1540` | `0.1544` | `1,801,685` | 277,928.27 USD | 27,957.37 USD | `+10.06%` | -7,364,574.12 USD | `+0.30` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1544` | `0.1545` | `0.1527` | `0.1534` | `4,992,738` | 766,314.68 USD | -116,166.36 USD | `-15.16%` | -7,480,740.48 USD | `-0.59` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1534` | `0.1537` | `0.1533` | `0.1535` | `609,947` | 93,621.26 USD | 14,755.64 USD | `+15.76%` | -7,465,984.84 USD | `+0.21` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1547` | `0.1565` | `0.1545` | `0.1551` | `7,794,455` | 1,212,948.28 USD | 71,177.47 USD | `+5.87%` | -7,452,026.16 USD | `+0.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1551` | `0.1552` | `0.1540` | `0.1544` | `7,261,182` | 1,122,592.32 USD | 113,507.08 USD | `+10.11%` | -7,338,519.08 USD | `+0.42` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1544` | `0.1545` | `0.1527` | `0.1534` | `5,565,331` | 854,203.84 USD | -106,505.87 USD | `-12.47%` | -7,445,024.96 USD | `+0.11` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1534` | `0.1603` | `0.1528` | `0.1556` | `102,506,063` | 16,106,228.03 USD | 395,467.12 USD | `+2.46%` | -7,593,143.35 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1556` | `0.1566` | `0.1527` | `0.1544` | `63,673,529` | 9,862,477.37 USD | 134,988.54 USD | `+1.37%` | -7,458,154.81 USD | `+0.47` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1544` | `0.1545` | `0.1527` | `0.1535` | `5,602,686` | 859,935.94 USD | -101,410.72 USD | `-11.79%` | -7,559,565.53 USD | `+0.29` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,374,542.78 USD | `-1.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,572,000.78 USD | `-0.89` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1535` | `324,023,568` | 50,797,844.03 USD | -3,987,564.74 USD | `-7.85%` | -7,559,565.53 USD | `-2.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1652` | `0.1687` | `0.1623` | `0.1631` | `68,085,678` | 11,252,816.65 USD | -909,329.92 USD | `-8.08%` | -705,420.63 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,136,414.44 USD | `-0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,374,542.78 USD | `-1.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,572,000.78 USD | `-0.89` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1535` | `324,023,568` | 50,797,844.03 USD | -3,987,564.74 USD | `-7.85%` | -7,559,565.53 USD | `-2.07` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:36:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1715` | 8,431.67 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale SELL: 8.43K USD at 0.1715 USD [API] | `2026-10-28 18:42:13` |
| `ANNOUNCEMENT` | `INFO` | `0.1719` | 6,013.83 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale SELL: 6.01K USD at 0.1719 USD [API] | `2026-10-28 18:43:59` |
| `ANNOUNCEMENT` | `INFO` | `0.1775` | 9,056.78 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale SELL: 9.06K USD at 0.1775 USD [API] | `2026-10-28 20:06:33` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.1629` (Vol: 153,600.00 USD, Dist: `+5.28%`) | Long MP=`0.1511` (Vol: 173,700.00 USD, Dist: `--2.36%`)
  * 48H Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+15.28%`) | Long MP=`0.1510` (Vol: 189,600.00 USD, Dist: `--2.44%`)
  * 3D Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+15.28%`) | Long MP=`0.1510` (Vol: 189,600.00 USD, Dist: `--2.44%`)
  * 7D Horizon: Short MP=`0.1791` (Vol: 196,100.00 USD, Dist: `+15.75%`) | Long MP=`0.1511` (Vol: 221,900.00 USD, Dist: `--2.38%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0345` | 345.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0385` | 1,490.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0405` | 157.95 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 1,220.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 424.66 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0455` | 910.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0475` | 167,030.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 109.52 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 610.70 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 170.28 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 289.43 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 2,270.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 16,160.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 718.35 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 2,000.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 3,870.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 9,180.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 6,570.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 99,790.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 313.22 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 57,970.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 3,390.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 5,840.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 111.58 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,760.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 2,190.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 948.08 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 14,690.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 172.24 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 19,440.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 11,060.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 13,840.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 112.78 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 4,970.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 19,460.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 5,240.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 2,940.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 1,360.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 2,040.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 814.24 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 1,510.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 10,260.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 145.24 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 5,490.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 17,930.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 12,910.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 773.66 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 112,680.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 7,480.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 9,340.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 906.89 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 1,060.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 11,830.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 605.37 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 534.49 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 425.50 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 3,850.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 10,720.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 9,880.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 6,230.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 5,420.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 25,800.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 2,180.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 11,970.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 303.75 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 19,200.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 39,990.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 844.86 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 4,850.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 870.65 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 9,780.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 4,010.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 16,660.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 5,300.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 13,320.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 9,690.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1336` | 3,260,000.00 USD | 3,260,000.00 USD | 3,580.00 USD | 5,990.00 USD | 16,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1340` | 3,240,000.00 USD | 3,240,000.00 USD | 9,160.00 USD | 7,730.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1344` | 3,190,000.00 USD | 3,190,000.00 USD | 6,410.00 USD | 5,790.00 USD | 19,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1345` | 741.71 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1348` | 3,160,000.00 USD | 3,160,000.00 USD | 31,170.00 USD | 7,150.00 USD | 23,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1352` | 3,100,000.00 USD | 3,100,000.00 USD | 11,390.00 USD | 6,290.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1355` | 38,490.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1356` | 3,050,000.00 USD | 3,050,000.00 USD | 16,150.00 USD | 12,180.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1360` | 3,020,000.00 USD | 3,020,000.00 USD | 25,240.00 USD | 8,630.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1364` | 2,970,000.00 USD | 2,970,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 53,980.00 USD | 965,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1368` | 2,950,000.00 USD | 2,950,000.00 USD | 4,500.00 USD | 7,610.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1370` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 1,740.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1372` | 2,940,000.00 USD | 2,940,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1373` | 2,670,000.00 USD | 2,670,000.00 USD | 5,470.00 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1376` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 1,730.00 USD | 536.58 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1379` | 2,660,000.00 USD | 2,660,000.00 USD | 3,190.00 USD | 1,590.00 USD | 1,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1380` | 2,930,000.00 USD | 2,930,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1382` | 2,650,000.00 USD | 2,650,000.00 USD | 10,310.00 USD | 10,080.00 USD | 29,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1384` | 2,920,000.00 USD | 2,920,000.00 USD | 11,880.00 USD | 0.00 USD | 30,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1385` | 2,600,000.00 USD | 2,600,000.00 USD | 31,240.00 USD | 0.00 USD | 55,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 22,700.00 USD | 911,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1388` | 2,510,000.00 USD | 2,510,000.00 USD | 12,440.00 USD | 1,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1388` | 2,870,000.00 USD | 2,870,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1391` | 2,500,000.00 USD | 2,500,000.00 USD | 15,160.00 USD | 1,440.00 USD | 71,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1392` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1394` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 6,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 6,570.00 USD | 888,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1396` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 28,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1397` | 2,410,000.00 USD | 2,410,000.00 USD | 12,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1400` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 2,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1400` | 2,760,000.00 USD | 2,760,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1404` | 2,750,000.00 USD | 2,750,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 8,880.00 USD | 881,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1412` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1415` | 6,590.00 USD | 872,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1416` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1420` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1421` | 2,390,000.00 USD | 2,390,000.00 USD | 4,030.00 USD | 2,310.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 484,730.00 USD | 866,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1432` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1433` | 2,380,000.00 USD | 2,380,000.00 USD | 3,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 28,290.00 USD | 381,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1436` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 20,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1436` | 2,720,000.00 USD | 2,720,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1439` | 2,350,000.00 USD | 2,350,000.00 USD | 17,680.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1440` | 2,680,000.00 USD | 2,680,000.00 USD | 13,180.00 USD | 5,260.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1442` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1444` | 2,660,000.00 USD | 2,660,000.00 USD | 3,450.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 16,220.00 USD | 353,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1451` | 2,330,000.00 USD | 2,330,000.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1452` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 5,660.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 2,110.00 USD | 337,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1456` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1460` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1463` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1464` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 39,940.00 USD | 335,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1466` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1468` | 2,610,000.00 USD | 2,610,000.00 USD | 9,720.00 USD | 9,180.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1469` | 2,320,000.00 USD | 2,320,000.00 USD | 12,090.00 USD | 2,700.00 USD | 6,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1472` | 2,300,000.00 USD | 2,300,000.00 USD | 6,430.00 USD | 14,550.00 USD | 65,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1472` | 2,590,000.00 USD | 2,590,000.00 USD | 19,180.00 USD | 0.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1475` | 2,210,000.00 USD | 2,210,000.00 USD | 33,920.00 USD | 8,290.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 95,530.00 USD | 295,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1476` | 2,560,000.00 USD | 2,560,000.00 USD | 68,180.00 USD | 20,180.00 USD | 81,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1478` | 2,170,000.00 USD | 2,170,000.00 USD | 129,340.00 USD | 11,890.00 USD | 136,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1480` | 2,390,000.00 USD | 2,390,000.00 USD | 74,500.00 USD | 43,810.00 USD | 50,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1481` | 1,890,000.00 USD | 1,890,000.00 USD | 60,660.00 USD | 14,570.00 USD | 10,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1484` | 1,800,000.00 USD | 1,800,000.00 USD | 45,680.00 USD | 4,230.00 USD | 185,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1484` | 2,220,000.00 USD | 2,220,000.00 USD | 47,020.00 USD | 16,640.00 USD | 201,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 9,220.00 USD | 199,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1487` | 1,570,000.00 USD | 1,570,000.00 USD | 8,170.00 USD | 4,430.00 USD | 5,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1488` | 1,950,000.00 USD | 1,950,000.00 USD | 73,140.00 USD | 10,470.00 USD | 25,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1490` | 1,550,000.00 USD | 1,550,000.00 USD | 35,320.00 USD | 9,450.00 USD | 4,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1492` | 1,840,000.00 USD | 1,840,000.00 USD | 40,320.00 USD | 21,590.00 USD | 92,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1493` | 1,500,000.00 USD | 1,500,000.00 USD | 14,230.00 USD | 1,780.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 35,480.00 USD | 190,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1496` | 1,480,000.00 USD | 1,480,000.00 USD | 14,390.00 USD | 5,270.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1496` | 1,690,000.00 USD | 1,690,000.00 USD | 34,650.00 USD | 18,690.00 USD | 17,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1499` | 1,460,000.00 USD | 1,460,000.00 USD | 2,670.00 USD | 0.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1500` | 1,620,000.00 USD | 1,620,000.00 USD | 60,500.00 USD | 9,610.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1502` | 1,450,000.00 USD | 1,450,000.00 USD | 3,610.00 USD | 13,270.00 USD | 130,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1504` | 1,530,000.00 USD | 1,530,000.00 USD | 20,410.00 USD | 19,520.00 USD | 44,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1505` | 1,300,000.00 USD | 1,300,000.00 USD | 54,760.00 USD | 23,120.00 USD | 7,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1505` | 148,730.00 USD | 154,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1508` | 1,220,000.00 USD | 1,220,000.00 USD | 200,020.00 USD | 16,950.00 USD | 259,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1508` | 1,440,000.00 USD | 1,440,000.00 USD | 200,530.00 USD | 16,820.00 USD | 256,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1511` | 740,620.00 USD | 740,620.00 USD | 122,160.00 USD | 4,360.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1512` | 969,940.00 USD | 969,940.00 USD | 86,820.00 USD | 13,310.00 USD | 59,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1514` | 611,600.00 USD | 611,600.00 USD | 25,970.00 USD | 1,730.00 USD | 232,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 6,130.00 USD | 6,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1516` | 810,380.00 USD | 810,380.00 USD | 48,970.00 USD | 13,330.00 USD | 377,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1517` | 351,020.00 USD | 351,020.00 USD | 87,420.00 USD | 7,460.00 USD | 141,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1520` | 114,410.00 USD | 114,410.00 USD | 44,180.00 USD | 4,100.00 USD | 14,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1520` | 370,870.00 USD | 370,870.00 USD | 47,340.00 USD | 22,090.00 USD | 201,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1523` | 51,800.00 USD | 51,800.00 USD | 34,460.00 USD | 2,970.00 USD | 5,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1524` | 100,260.00 USD | 100,260.00 USD | 0.00 USD | 13,950.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1528` | 78,000.00 USD | 78,000.00 USD | 0.00 USD | 33,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1532` | 44,060.00 USD | 44,060.00 USD | 0.00 USD | 17,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1535` | 8,980.00 USD | 8,980.00 USD | 0.00 USD | 8,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1536` | 26,790.00 USD | 26,790.00 USD | 0.00 USD | 8,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1540` | 18,230.00 USD | 18,230.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1544` | 3,590.00 USD | 3,590.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1547` | 13,520.00 USD | 13,520.00 USD | 0.00 USD | 13,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1548` | 6,450.00 USD | 6,450.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1550` | 17,980.00 USD | 17,980.00 USD | 0.00 USD | 4,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1552` | 18,270.00 USD | 18,270.00 USD | 0.00 USD | 11,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1553` | 19,510.00 USD | 19,510.00 USD | 0.00 USD | 1,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1560` | 29,260.00 USD | 29,260.00 USD | 0.00 USD | 10,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1562` | 24,480.00 USD | 24,480.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1564` | 63,020.00 USD | 63,020.00 USD | 0.00 USD | 33,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1565` | 331,620.00 USD | 331,620.00 USD | 41,260.00 USD | 13,270.00 USD | 252,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1568` | 619,440.00 USD | 619,440.00 USD | 33,360.00 USD | 38,630.00 USD | 215,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1568` | 341,690.00 USD | 341,690.00 USD | 111,700.00 USD | 15,360.00 USD | 151,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1571` | 725,710.00 USD | 725,710.00 USD | 40,700.00 USD | 6,150.00 USD | 59,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1572` | 675,490.00 USD | 675,490.00 USD | 235,420.00 USD | 39,540.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1574` | 751,680.00 USD | 751,680.00 USD | 25,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1576` | 1,160,000.00 USD | 1,160,000.00 USD | 44,680.00 USD | 123,840.00 USD | 315,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1577` | 1,170,000.00 USD | 1,170,000.00 USD | 69,720.00 USD | 0.00 USD | 351,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1580` | 1,490,000.00 USD | 1,490,000.00 USD | 226,250.00 USD | 101,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1583` | 1,240,000.00 USD | 1,240,000.00 USD | 62,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1584` | 1,730,000.00 USD | 1,730,000.00 USD | 80,450.00 USD | 43,370.00 USD | 114,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1586` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 17,270.00 USD | 16,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1588` | 1,840,000.00 USD | 1,840,000.00 USD | 69,180.00 USD | 44,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1589` | 1,320,000.00 USD | 1,320,000.00 USD | 15,100.00 USD | 19,490.00 USD | 13,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1592` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 20,480.00 USD | 21,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1592` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 64,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1595` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 39,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1596` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 98,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1598` | 1,520,000.00 USD | 1,520,000.00 USD | 16,680.00 USD | 0.00 USD | 99,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1600` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 60,710.00 USD | 75,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1601` | 1,540,000.00 USD | 1,540,000.00 USD | 20,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1604` | 1,630,000.00 USD | 1,630,000.00 USD | 99,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1604` | 2,710,000.00 USD | 2,710,000.00 USD | 188,060.00 USD | 112,090.00 USD | 273,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1605` | 2,500.00 USD | 2,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1607` | 1,760,000.00 USD | 1,760,000.00 USD | 12,980.00 USD | 0.00 USD | 115,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1608` | 3,490,000.00 USD | 3,490,000.00 USD | 208,080.00 USD | 240,680.00 USD | 329,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1610` | 1,900,000.00 USD | 1,900,000.00 USD | 34,860.00 USD | 0.00 USD | 106,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1612` | 4,460,000.00 USD | 4,460,000.00 USD | 353,120.00 USD | 328,050.00 USD | 287,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1613` | 2,050,000.00 USD | 2,050,000.00 USD | 37,090.00 USD | 11,530.00 USD | 94,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1616` | 2,060,000.00 USD | 2,060,000.00 USD | 14,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1616` | 5,050,000.00 USD | 5,050,000.00 USD | 293,210.00 USD | 131,180.00 USD | 165,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1619` | 2,190,000.00 USD | 2,190,000.00 USD | 91,300.00 USD | 41,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1620` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 196,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1622` | 2,320,000.00 USD | 2,320,000.00 USD | 76,010.00 USD | 54,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1624` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 193,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1625` | 2,430,000.00 USD | 2,430,000.00 USD | 54,920.00 USD | 48,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1628` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 101,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1628` | 5,620,000.00 USD | 5,620,000.00 USD | 76,780.00 USD | 0.00 USD | 103,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1631` | 2,640,000.00 USD | 2,640,000.00 USD | 88,400.00 USD | 23,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1634` | 2,670,000.00 USD | 2,670,000.00 USD | 10,020.00 USD | 10,690.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1635` | 380.25 USD | 2,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1636` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 13,670.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1637` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 22,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1640` | 2,720,000.00 USD | 2,720,000.00 USD | 9,110.00 USD | 13,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1640` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1643` | 2,780,000.00 USD | 2,780,000.00 USD | 10,070.00 USD | 35,000.00 USD | 16,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1644` | 5,700,000.00 USD | 5,700,000.00 USD | 0.00 USD | 8,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1645` | 2,480.00 USD | 5,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1646` | 2,790,000.00 USD | 2,790,000.00 USD | 14,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1648` | 5,700,000.00 USD | 5,700,000.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1655` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 7,370.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1655` | 909.51 USD | 6,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1656` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 31,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1658` | 2,870,000.00 USD | 2,870,000.00 USD | 9,730.00 USD | 47,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1660` | 5,880,000.00 USD | 5,880,000.00 USD | 79,170.00 USD | 11,020.00 USD | 51,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1661` | 2,940,000.00 USD | 2,940,000.00 USD | 8,220.00 USD | 11,150.00 USD | 50,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1664` | 3,100,000.00 USD | 3,100,000.00 USD | 66,370.00 USD | 14,550.00 USD | 80,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1664` | 6,130,000.00 USD | 6,130,000.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1665` | 26,250.00 USD | 32,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1667` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 5,340.00 USD | 41,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1668` | 6,310,000.00 USD | 6,310,000.00 USD | 42,580.00 USD | 52,290.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1672` | 6,510,000.00 USD | 6,510,000.00 USD | 135,250.00 USD | 62,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1673` | 3,230,000.00 USD | 3,230,000.00 USD | 66,630.00 USD | 2,010.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1675` | 636.75 USD | 33,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1676` | 3,260,000.00 USD | 3,260,000.00 USD | 22,100.00 USD | 1,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1676` | 6,740,000.00 USD | 6,740,000.00 USD | 84,020.00 USD | 141,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1679` | 3,260,000.00 USD | 3,260,000.00 USD | 6,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1680` | 6,950,000.00 USD | 6,950,000.00 USD | 121,860.00 USD | 80,270.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1682` | 3,440,000.00 USD | 3,440,000.00 USD | 154,780.00 USD | 4,560.00 USD | 18,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1684` | 7,030,000.00 USD | 7,030,000.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1685` | 3,500,000.00 USD | 3,500,000.00 USD | 20,370.00 USD | 29,790.00 USD | 13,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1688` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 2,650.00 USD | 39,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1688` | 7,040,000.00 USD | 7,040,000.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1691` | 3,750,000.00 USD | 3,750,000.00 USD | 75,680.00 USD | 76,030.00 USD | 54,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1692` | 7,220,000.00 USD | 7,220,000.00 USD | 33,660.00 USD | 70,740.00 USD | 71,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1694` | 3,820,000.00 USD | 3,820,000.00 USD | 34,000.00 USD | 22,300.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1696` | 7,360,000.00 USD | 7,360,000.00 USD | 17,360.00 USD | 87,350.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1697` | 3,900,000.00 USD | 3,900,000.00 USD | 36,180.00 USD | 38,310.00 USD | 6,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1700` | 3,980,000.00 USD | 3,980,000.00 USD | 13,350.00 USD | 21,160.00 USD | 46,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1700` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1703` | 4,040,000.00 USD | 4,040,000.00 USD | 9,960.00 USD | 14,420.00 USD | 34,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1704` | 7,580,000.00 USD | 7,580,000.00 USD | 55,170.00 USD | 46,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1705` | 8,020.00 USD | 41,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1706` | 4,100,000.00 USD | 4,100,000.00 USD | 38,860.00 USD | 9,590.00 USD | 13,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1708` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 25,490.00 USD | 87,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1709` | 4,190,000.00 USD | 4,190,000.00 USD | 21,630.00 USD | 62,270.00 USD | 2,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1712` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 15,040.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1715` | 4,260,000.00 USD | 4,260,000.00 USD | 9,570.00 USD | 27,880.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1716` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 42,020.00 USD | 15,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1718` | 4,290,000.00 USD | 4,290,000.00 USD | 12,630.00 USD | 10,110.00 USD | 10,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1720` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 161,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1721` | 4,450,000.00 USD | 4,450,000.00 USD | 107,900.00 USD | 16,860.00 USD | 30,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1724` | 4,520,000.00 USD | 4,520,000.00 USD | 21,930.00 USD | 0.00 USD | 48,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1724` | 8,240,000.00 USD | 8,240,000.00 USD | 118,060.00 USD | 0.00 USD | 208,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1727` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 2,410.00 USD | 8,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1730` | 4,540,000.00 USD | 4,540,000.00 USD | 8,220.00 USD | 0.00 USD | 6,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1732` | 8,730,000.00 USD | 8,730,000.00 USD | 476,430.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1733` | 4,560,000.00 USD | 4,560,000.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1736` | 4,580,000.00 USD | 4,580,000.00 USD | 14,970.00 USD | 9,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1739` | 4,620,000.00 USD | 4,620,000.00 USD | 18,610.00 USD | 2,310.00 USD | 12,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1740` | 8,810,000.00 USD | 8,810,000.00 USD | 0.00 USD | 0.00 USD | 83,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1742` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 1,600.00 USD | 11,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1744` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1745` | 4,650,000.00 USD | 4,650,000.00 USD | 8,530.00 USD | 2,460.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1745` | 14,600.00 USD | 55,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1748` | 4,750,000.00 USD | 4,750,000.00 USD | 55,280.00 USD | 2,280.00 USD | 39,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1748` | 8,910,000.00 USD | 8,910,000.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1751` | 4,800,000.00 USD | 4,800,000.00 USD | 41,730.00 USD | 0.00 USD | 14,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1752` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 0.00 USD | 291,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1754` | 4,890,000.00 USD | 4,890,000.00 USD | 32,060.00 USD | 8,430.00 USD | 46,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1756` | 9,500,000.00 USD | 9,500,000.00 USD | 112,930.00 USD | 0.00 USD | 186,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1757` | 5,020,000.00 USD | 5,020,000.00 USD | 15,820.00 USD | 40,160.00 USD | 76,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1760` | 5,220,000.00 USD | 5,220,000.00 USD | 94,020.00 USD | 79,990.00 USD | 21,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1760` | 9,870,000.00 USD | 9,870,000.00 USD | 268,160.00 USD | 71,260.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1763` | 5,370,000.00 USD | 5,370,000.00 USD | 59,300.00 USD | 22,900.00 USD | 68,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1764` | 10,540,000.00 USD | 10,540,000.00 USD | 353,950.00 USD | 270,450.00 USD | 40,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1765` | 3,900.00 USD | 59,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1766` | 5,470,000.00 USD | 5,470,000.00 USD | 15,830.00 USD | 20,220.00 USD | 62,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1768` | 10,910,000.00 USD | 10,910,000.00 USD | 191,690.00 USD | 147,360.00 USD | 31,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1769` | 5,630,000.00 USD | 5,630,000.00 USD | 40,920.00 USD | 78,870.00 USD | 44,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1772` | 5,660,000.00 USD | 5,660,000.00 USD | 22,380.00 USD | 5,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1772` | 11,180,000.00 USD | 11,180,000.00 USD | 98,390.00 USD | 153,480.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1776` | 11,430,000.00 USD | 11,430,000.00 USD | 186,770.00 USD | 59,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1780` | 11,680,000.00 USD | 11,680,000.00 USD | 52,730.00 USD | 46,410.00 USD | 157,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1784` | 11,910,000.00 USD | 11,910,000.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1788` | 12,080,000.00 USD | 12,080,000.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1792` | 12,310,000.00 USD | 12,310,000.00 USD | 182,810.00 USD | 46,960.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1796` | 12,400,000.00 USD | 12,400,000.00 USD | 17,130.00 USD | 26,110.00 USD | 44,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1800` | 12,520,000.00 USD | 12,520,000.00 USD | 12,940.00 USD | 34,680.00 USD | 73,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1804` | 12,610,000.00 USD | 12,610,000.00 USD | 35,280.00 USD | 32,850.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1808` | 12,790,000.00 USD | 12,790,000.00 USD | 35,050.00 USD | 67,250.00 USD | 73,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1812` | 12,930,000.00 USD | 12,930,000.00 USD | 64,990.00 USD | 29,900.00 USD | 50,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1816` | 13,070,000.00 USD | 13,070,000.00 USD | 69,700.00 USD | 33,940.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1820` | 13,240,000.00 USD | 13,240,000.00 USD | 65,350.00 USD | 54,880.00 USD | 43,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1824` | 13,450,000.00 USD | 13,450,000.00 USD | 80,350.00 USD | 17,880.00 USD | 112,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1828` | 13,630,000.00 USD | 13,630,000.00 USD | 79,610.00 USD | 29,630.00 USD | 69,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1832` | 13,840,000.00 USD | 13,840,000.00 USD | 108,540.00 USD | 31,590.00 USD | 74,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1835` | 748.51 USD | 60,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1836` | 14,180,000.00 USD | 14,180,000.00 USD | 172,660.00 USD | 110,870.00 USD | 52,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1840` | 14,520,000.00 USD | 14,520,000.00 USD | 141,620.00 USD | 50,840.00 USD | 151,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1844` | 14,740,000.00 USD | 14,740,000.00 USD | 94,510.00 USD | 20,390.00 USD | 97,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1845` | 777.21 USD | 61,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1848` | 14,880,000.00 USD | 14,880,000.00 USD | 35,280.00 USD | 69,910.00 USD | 41,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1852` | 15,330,000.00 USD | 15,330,000.00 USD | 168,270.00 USD | 28,290.00 USD | 251,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1856` | 15,570,000.00 USD | 15,570,000.00 USD | 100,160.00 USD | 21,030.00 USD | 120,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1860` | 15,810,000.00 USD | 15,810,000.00 USD | 64,600.00 USD | 48,330.00 USD | 127,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1864` | 15,970,000.00 USD | 15,970,000.00 USD | 48,260.00 USD | 44,140.00 USD | 61,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1868` | 16,200,000.00 USD | 16,200,000.00 USD | 133,990.00 USD | 38,100.00 USD | 56,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1872` | 16,580,000.00 USD | 16,580,000.00 USD | 169,490.00 USD | 133,380.00 USD | 86,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1876` | 16,720,000.00 USD | 16,720,000.00 USD | 65,910.00 USD | 23,180.00 USD | 43,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1880` | 16,830,000.00 USD | 16,830,000.00 USD | 57,250.00 USD | 22,460.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1884` | 16,890,000.00 USD | 16,890,000.00 USD | 14,000.00 USD | 35,430.00 USD | 9,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1888` | 17,000,000.00 USD | 17,000,000.00 USD | 22,970.00 USD | 4,800.00 USD | 88,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1892` | 17,090,000.00 USD | 17,090,000.00 USD | 49,980.00 USD | 2,860.00 USD | 34,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1896` | 17,160,000.00 USD | 17,160,000.00 USD | 42,320.00 USD | 11,820.00 USD | 18,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1900` | 17,210,000.00 USD | 17,210,000.00 USD | 0.00 USD | 29,650.00 USD | 20,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1904` | 17,250,000.00 USD | 17,250,000.00 USD | 14,330.00 USD | 10,990.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1908` | 17,330,000.00 USD | 17,330,000.00 USD | 24,190.00 USD | 37,870.00 USD | 18,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1912` | 17,350,000.00 USD | 17,350,000.00 USD | 0.00 USD | 9,380.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1916` | 17,380,000.00 USD | 17,380,000.00 USD | 7,460.00 USD | 5,300.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1920` | 17,380,000.00 USD | 17,380,000.00 USD | 0.00 USD | 5,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1924` | 17,400,000.00 USD | 17,400,000.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1928` | 17,420,000.00 USD | 17,420,000.00 USD | 11,600.00 USD | 7,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1944` | 17,430,000.00 USD | 17,430,000.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1945` | 623.68 USD | 61,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1952` | 17,440,000.00 USD | 17,440,000.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1955` | 860.20 USD | 62,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1956` | 17,440,000.00 USD | 17,440,000.00 USD | 4,860.00 USD | 2,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1960` | 17,450,000.00 USD | 17,450,000.00 USD | 5,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1964` | 17,470,000.00 USD | 17,470,000.00 USD | 6,470.00 USD | 2,700.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1975` | 150.10 USD | 62,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1995` | 1,550.00 USD | 64,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2055` | 11,590.00 USD | 75,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2085` | 198.08 USD | 76,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2095` | 164.23 USD | 76,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2135` | 16,620.00 USD | 92,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 41,330.00 USD | 134,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2195` | 113,920.00 USD | 248,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 229.15 USD | 248,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2255` | 154.78 USD | 248,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2275` | 100.30 USD | 248,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2285` | 1,090.00 USD | 249,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 6,820.00 USD | 256,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2335` | 25,000.00 USD | 281,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 63,350.00 USD | 344,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 102.62 USD | 345,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 361.66 USD | 345,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 796.25 USD | 346,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2445` | 231.03 USD | 346,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2465` | 728.26 USD | 347,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2545` | 546.54 USD | 347,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 3,870.00 USD | 351,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2575` | 28,910.00 USD | 380,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 52,620.00 USD | 433,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 154.94 USD | 433,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2685` | 226.51 USD | 433,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 13,510.00 USD | 447,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 214.21 USD | 447,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2735` | 3,310.00 USD | 450,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 27,890.00 USD | 478,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2795` | 482.84 USD | 478,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2905` | 17,080.00 USD | 496,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 187.26 USD | 496,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2925` | 464.84 USD | 496,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 2,640.00 USD | 499,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2945` | 468.40 USD | 499,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 574.36 USD | 500,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2995` | 2,280.00 USD | 502,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 225.42 USD | 502,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0365` | 2,030,000.00 USD | 0.00 USD | 515.81 USD | `-76.36%` | `14,131,900,000,000.00` |
| `Live` | `Long` | `0.0385` | 2,030,000.00 USD | 0.00 USD | 1,880.00 USD | `-75.06%` | `48,823,900,000,000.00` |
| `Live` | `Long` | `0.0405` | 2,030,000.00 USD | 0.00 USD | 562.95 USD | `-73.77%` | `13,900,000,000,000.00` |
| `Live` | `Long` | `0.0415` | 2,030,000.00 USD | 0.00 USD | 110.22 USD | `-73.12%` | `2,655,800,000,000.00` |
| `Live` | `Long` | `0.0425` | 2,030,000.00 USD | 0.00 USD | 170.00 USD | `-72.47%` | `4,000,000,000,000.00` |
| `Live` | `Long` | `0.0465` | 2,030,000.00 USD | 0.00 USD | 397.83 USD | `-69.88%` | `8,555,500,000,000.00` |
| `Live` | `Long` | `0.0485` | 2,030,000.00 USD | 0.00 USD | 970.00 USD | `-68.59%` | `20,000,000,000,000.00` |
| `Live` | `Long` | `0.0495` | 2,030,000.00 USD | 0.00 USD | 269.69 USD | `-67.94%` | `5,448,200,000,000.00` |
| `Live` | `Long` | `0.0525` | 2,030,000.00 USD | 0.00 USD | 289.43 USD | `-66.00%` | `5,513,000,000,000.00` |
| `Live` | `Long` | `0.0535` | 2,030,000.00 USD | 0.00 USD | 176.68 USD | `-65.35%` | `3,302,400,000,000.00` |
| `Live` | `Long` | `0.0545` | 2,030,000.00 USD | 0.00 USD | 194,570.00 USD | `-64.70%` | `3,570,137,800,000,000.00` |
| `Live` | `Long` | `0.0555` | 1,830,000.00 USD | 0.00 USD | 11,100.00 USD | `-64.05%` | `200,000,000,000,000.00` |
| `Live` | `Long` | `0.0565` | 1,820,000.00 USD | 0.00 USD | 15,650.00 USD | `-63.40%` | `276,984,000,000,000.00` |
| `Live` | `Long` | `0.0575` | 1,810,000.00 USD | 0.00 USD | 1,660.00 USD | `-62.76%` | `28,900,000,000,000.00` |
| `Live` | `Long` | `0.0585` | 1,810,000.00 USD | 0.00 USD | 2,080.00 USD | `-62.11%` | `35,600,700,000,000.00` |
| `Live` | `Long` | `0.0595` | 1,800,000.00 USD | 0.00 USD | 743.33 USD | `-61.46%` | `12,493,000,000,000.00` |
| `Live` | `Long` | `0.0635` | 1,800,000.00 USD | 0.00 USD | 1,190.00 USD | `-58.87%` | `18,731,100,000,000.00` |
| `Live` | `Long` | `0.0655` | 1,800,000.00 USD | 0.00 USD | 1,720.00 USD | `-57.57%` | `26,331,000,000,000.00` |
| `Live` | `Long` | `0.0675` | 1,800,000.00 USD | 0.00 USD | 99,790.00 USD | `-56.28%` | `1,478,385,900,000,000.00` |
| `Live` | `Long` | `0.0685` | 1,700,000.00 USD | 0.00 USD | 7,110.00 USD | `-55.63%` | `103,822,100,000,000.00` |
| `Live` | `Long` | `0.0695` | 1,690,000.00 USD | 0.00 USD | 143.87 USD | `-54.98%` | `2,070,000,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,690,000.00 USD | 0.00 USD | 10,150.00 USD | `-54.34%` | `143,973,800,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,680,000.00 USD | 0.00 USD | 6,260.00 USD | `-53.69%` | `87,561,500,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,680,000.00 USD | 0.00 USD | 111.58 USD | `-53.04%` | `1,539,100,000,000.00` |
| `Live` | `Long` | `0.0735` | 1,680,000.00 USD | 0.00 USD | 2,440.00 USD | `-52.39%` | `33,161,800,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,670,000.00 USD | 0.00 USD | 226.17 USD | `-51.75%` | `3,035,900,000,000.00` |
| `Live` | `Long` | `0.0755` | 1,670,000.00 USD | 0.00 USD | 331.44 USD | `-51.10%` | `4,389,900,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,670,000.00 USD | 0.00 USD | 14,690.00 USD | `-50.45%` | `192,029,300,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,660,000.00 USD | 0.00 USD | 4,630.00 USD | `-48.51%` | `58,261,800,000,000.00` |
| `Live` | `Long` | `0.0815` | 1,650,000.00 USD | 0.00 USD | 70,470.00 USD | `-47.21%` | `864,694,800,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,580,000.00 USD | 0.00 USD | 14,050.00 USD | `-46.56%` | `170,330,300,000,000.00` |
| `Live` | `Long` | `0.0835` | 1,570,000.00 USD | 0.00 USD | 1,050.00 USD | `-45.92%` | `12,557,400,000,000.00` |
| `Live` | `Long` | `0.0845` | 1,570,000.00 USD | 0.00 USD | 1,890.00 USD | `-45.27%` | `22,422,700,000,000.00` |
| `Live` | `Long` | `0.0855` | 1,570,000.00 USD | 0.00 USD | 190.02 USD | `-44.62%` | `2,222,400,000,000.00` |
| `Live` | `Long` | `0.0865` | 1,570,000.00 USD | 0.00 USD | 19,460.00 USD | `-43.97%` | `224,937,400,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,550,000.00 USD | 0.00 USD | 514.04 USD | `-42.68%` | `5,808,400,000,000.00` |
| `Live` | `Long` | `0.0895` | 1,550,000.00 USD | 0.00 USD | 4,780.00 USD | `-42.03%` | `53,365,600,000,000.00` |
| `Live` | `Long` | `0.0915` | 1,540,000.00 USD | 0.00 USD | 17,040.00 USD | `-40.73%` | `186,229,100,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,530,000.00 USD | 0.00 USD | 7,550.00 USD | `-40.09%` | `81,648,900,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,520,000.00 USD | 0.00 USD | 814.24 USD | `-39.44%` | `8,708,500,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,520,000.00 USD | 0.00 USD | 14,330.00 USD | `-38.79%` | `151,691,700,000,000.00` |
| `Live` | `Long` | `0.0955` | 1,500,000.00 USD | 0.00 USD | 535.45 USD | `-38.14%` | `5,606,800,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,500,000.00 USD | 0.00 USD | 9,870.00 USD | `-37.50%` | `102,309,800,000,000.00` |
| `Live` | `Long` | `0.0975` | 1,490,000.00 USD | 0.00 USD | 2,960.00 USD | `-36.85%` | `30,311,300,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,490,000.00 USD | 0.00 USD | 2,810.00 USD | `-36.20%` | `28,516,700,000,000.00` |
| `Live` | `Long` | `0.0995` | 1,490,000.00 USD | 0.00 USD | 11,640.00 USD | `-35.55%` | `116,999,600,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,470,000.00 USD | 0.00 USD | 1,850.00 USD | `-34.91%` | `18,436,400,000,000.00` |
| `Live` | `Long` | `0.1025` | 1,470,000.00 USD | 0.00 USD | 1,700.00 USD | `-33.61%` | `16,547,900,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,470,000.00 USD | 0.00 USD | 802.14 USD | `-32.96%` | `7,750,100,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,470,000.00 USD | 0.00 USD | 23,980.00 USD | `-32.31%` | `229,461,900,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,450,000.00 USD | 0.00 USD | 8,190.00 USD | `-31.67%` | `77,610,300,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,440,000.00 USD | 0.00 USD | 1,090.00 USD | `-31.02%` | `10,190,500,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,440,000.00 USD | 0.00 USD | 1,490.00 USD | `-30.37%` | `13,903,400,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,440,000.00 USD | 0.00 USD | 129,250.00 USD | `-29.72%` | `1,191,226,800,000,000.00` |
| `Live` | `Long` | `0.1095` | 1,310,000.00 USD | 0.00 USD | 774.43 USD | `-29.08%` | `7,072,400,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,310,000.00 USD | 0.00 USD | 14,360.00 USD | `-28.43%` | `129,913,800,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,290,000.00 USD | 0.00 USD | 707.42 USD | `-27.78%` | `6,344,600,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,290,000.00 USD | 0.00 USD | 2,520.00 USD | `-26.48%` | `22,204,700,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,290,000.00 USD | 0.00 USD | 8,950.00 USD | `-25.84%` | `78,144,100,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,280,000.00 USD | 0.00 USD | 10,050.00 USD | `-25.19%` | `87,016,100,000,000.00` |
| `Live` | `Long` | `0.1165` | 1,270,000.00 USD | 0.00 USD | 1,270.00 USD | `-24.54%` | `10,928,400,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,270,000.00 USD | 0.00 USD | 5,420.00 USD | `-23.89%` | `46,086,300,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,260,000.00 USD | 0.00 USD | 27,460.00 USD | `-23.25%` | `231,707,700,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,240,000.00 USD | 0.00 USD | 8,570.00 USD | `-22.60%` | `71,701,200,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,230,000.00 USD | 0.00 USD | 303.75 USD | `-21.30%` | `2,500,000,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,230,000.00 USD | 0.00 USD | 18,510.00 USD | `-20.66%` | `151,121,900,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,210,000.00 USD | 0.00 USD | 35,660.00 USD | `-20.01%` | `288,762,700,000,000.00` |
| `Live` | `Long` | `0.1245` | 1,170,000.00 USD | 0.00 USD | 1,060.00 USD | `-19.36%` | `8,486,000,000,000.00` |
| `Live` | `Long` | `0.1255` | 1,170,000.00 USD | 0.00 USD | 4,850.00 USD | `-18.71%` | `38,646,100,000,000.00` |
| `Live` | `Long` | `0.1265` | 1,170,000.00 USD | 0.00 USD | 3,860.00 USD | `-18.06%` | `30,524,300,000,000.00` |
| `Live` | `Long` | `0.1275` | 1,160,000.00 USD | 0.00 USD | 1,710.00 USD | `-17.42%` | `13,387,800,000,000.00` |
| `Live` | `Long` | `0.1285` | 1,160,000.00 USD | 0.00 USD | 9,780.00 USD | `-16.77%` | `76,071,500,000,000.00` |
| `Live` | `Long` | `0.1295` | 1,150,000.00 USD | 0.00 USD | 4,010.00 USD | `-16.12%` | `30,998,800,000,000.00` |
| `Live` | `Long` | `0.1305` | 1,150,000.00 USD | 0.00 USD | 16,660.00 USD | `-15.47%` | `127,649,400,000,000.00` |
| `Live` | `Long` | `0.1315` | 1,130,000.00 USD | 0.00 USD | 3,670.00 USD | `-14.83%` | `27,897,900,000,000.00` |
| `Live` | `Long` | `0.1325` | 1,130,000.00 USD | 0.00 USD | 13,480.00 USD | `-14.18%` | `101,767,800,000,000.00` |
| `Live` | `Long` | `0.1335` | 1,110,000.00 USD | 0.00 USD | 50,870.00 USD | `-13.53%` | `381,026,700,000,000.00` |
| `Live` | `Long` | `0.1345` | 1,060,000.00 USD | 0.00 USD | 583.12 USD | `-12.88%` | `4,335,500,000,000.00` |
| `Live` | `Long` | `0.1355` | 1,060,000.00 USD | 0.00 USD | 3,920.00 USD | `-12.24%` | `28,954,600,000,000.00` |
| `Live` | `Long` | `0.1365` | 1,060,000.00 USD | 0.00 USD | 16,680.00 USD | `-11.59%` | `122,220,100,000,000.00` |
| `Live` | `Long` | `0.1375` | 1,040,000.00 USD | 0.00 USD | 13,750.00 USD | `-10.94%` | `100,000,000,000,000.00` |
| `Live` | `Long` | `0.1385` | 1,030,000.00 USD | 0.00 USD | 8,610.00 USD | `-10.29%` | `62,191,400,000,000.00` |
| `Live` | `Long` | `0.1395` | 1,020,000.00 USD | 0.00 USD | 6,340.00 USD | `-9.64%` | `45,425,500,000,000.00` |
| `Live` | `Long` | `0.1405` | 1,010,000.00 USD | 0.00 USD | 885.87 USD | `-9.00%` | `6,305,100,000,000.00` |
| `Live` | `Long` | `0.1415` | 1,010,000.00 USD | 0.00 USD | 5,130.00 USD | `-8.35%` | `36,281,800,000,000.00` |
| `Live` | `Long` | `0.1425` | 1,010,000.00 USD | 0.00 USD | 524,000.00 USD | `-7.70%` | `3,677,167,600,000,000.00` |
| `Live` | `Long` | `0.1435` | 482,110.00 USD | 0.00 USD | 53,570.00 USD | `-7.05%` | `373,304,500,000,000.00` |
| `Live` | `Long` | `0.1445` | 428,540.00 USD | 0.00 USD | 16,220.00 USD | `-6.41%` | `112,262,000,000,000.00` |
| `Live` | `Long` | `0.1455` | 412,320.00 USD | 0.00 USD | 92,950.00 USD | `-5.76%` | `638,827,600,000,000.00` |
| `Live` | `Long` | `0.1465` | 319,370.00 USD | 0.00 USD | 38,590.00 USD | `-5.11%` | `263,384,700,000,000.00` |
| `Live` | `Long` | `0.1475` | 280,780.00 USD | 0.00 USD | 98,050.00 USD | `-4.46%` | `664,750,600,000,000.00` |
| `Live` | `Long` | `0.1485` | 182,730.00 USD | 0.00 USD | 9,200.00 USD | `-3.82%` | `61,967,100,000,000.00` |
| `Live` | `Long` | `0.1495` | 173,530.00 USD | 0.00 USD | 7,770.00 USD | `-3.17%` | `51,993,900,000,000.00` |
| `Live` | `Long` | `0.1505` | 165,760.00 USD | 0.00 USD | 159,210.00 USD | `-2.52%` | `1,057,904,800,000,000.00` |
| `Live` | `Long` | `0.1515` | 6,540.00 USD | 0.00 USD | 6,540.00 USD | `-1.87%` | `43,189,700,000,000.00` |
| `Live` | `Short` | `0.1615` | 4,950.00 USD | 4,950.00 USD | 0.00 USD | `+4.61%` | `30,659,400,000,000.00` |
| `Live` | `Short` | `0.1625` | 8,670.00 USD | 3,720.00 USD | 0.00 USD | `+5.25%` | `22,881,100,000,000.00` |
| `Live` | `Short` | `0.1635` | 16,100.00 USD | 7,430.00 USD | 0.00 USD | `+5.90%` | `45,440,000,000,000.00` |
| `Live` | `Short` | `0.1645` | 23,100.00 USD | 7,000.00 USD | 0.00 USD | `+6.55%` | `42,573,600,000,000.00` |
| `Live` | `Short` | `0.1665` | 29,380.00 USD | 6,270.00 USD | 0.00 USD | `+7.84%` | `37,682,700,000,000.00` |
| `Live` | `Short` | `0.1675` | 29,880.00 USD | 508.23 USD | 0.00 USD | `+8.49%` | `3,034,200,000,000.00` |
| `Live` | `Short` | `0.1705` | 30,000.00 USD | 110.74 USD | 0.00 USD | `+10.43%` | `649,500,000,000.00` |
| `Live` | `Short` | `0.1735` | 32,970.00 USD | 2,970.00 USD | 0.00 USD | `+12.38%` | `17,130,400,000,000.00` |
| `Live` | `Short` | `0.1745` | 33,730.00 USD | 758.99 USD | 0.00 USD | `+13.03%` | `4,349,500,000,000.00` |
| `Live` | `Short` | `0.1765` | 34,480.00 USD | 748.62 USD | 0.00 USD | `+14.32%` | `4,241,500,000,000.00` |
| `Live` | `Short` | `0.1785` | 34,610.00 USD | 138.82 USD | 0.00 USD | `+15.62%` | `777,700,000,000.00` |
| `Live` | `Short` | `0.1845` | 35,390.00 USD | 777.21 USD | 0.00 USD | `+19.50%` | `4,212,500,000,000.00` |
| `Live` | `Short` | `0.1915` | 39,980.00 USD | 4,590.00 USD | 0.00 USD | `+24.04%` | `23,985,700,000,000.00` |
| `Live` | `Short` | `0.1945` | 40,610.00 USD | 623.68 USD | 0.00 USD | `+25.98%` | `3,206,600,000,000.00` |
| `Live` | `Short` | `0.1975` | 42,320.00 USD | 1,710.00 USD | 0.00 USD | `+27.92%` | `8,658,500,000,000.00` |
| `Live` | `Short` | `0.2055` | 53,910.00 USD | 11,590.00 USD | 0.00 USD | `+33.10%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2085` | 54,110.00 USD | 198.08 USD | 0.00 USD | `+35.05%` | `950,000,000,000.00` |
| `Live` | `Short` | `0.2095` | 54,270.00 USD | 164.23 USD | 0.00 USD | `+35.70%` | `783,900,000,000.00` |
| `Live` | `Short` | `0.2135` | 69,970.00 USD | 15,690.00 USD | 0.00 USD | `+38.29%` | `73,505,600,000,000.00` |
| `Live` | `Short` | `0.2155` | 111,300.00 USD | 41,330.00 USD | 0.00 USD | `+39.58%` | `191,801,700,000,000.00` |
| `Live` | `Short` | `0.2175` | 137,180.00 USD | 25,880.00 USD | 0.00 USD | `+40.88%` | `118,989,500,000,000.00` |
| `Live` | `Short` | `0.2195` | 224,980.00 USD | 87,800.00 USD | 0.00 USD | `+42.17%` | `400,000,000,000,000.00` |
| `Live` | `Short` | `0.2235` | 225,210.00 USD | 229.15 USD | 0.00 USD | `+44.76%` | `1,025,300,000,000.00` |
| `Live` | `Short` | `0.2255` | 225,360.00 USD | 154.78 USD | 0.00 USD | `+46.06%` | `686,400,000,000.00` |
| `Live` | `Short` | `0.2285` | 251,060.00 USD | 25,700.00 USD | 0.00 USD | `+48.00%` | `112,460,500,000,000.00` |
| `Live` | `Short` | `0.2295` | 287,320.00 USD | 36,260.00 USD | 0.00 USD | `+48.65%` | `157,981,400,000,000.00` |
| `Live` | `Short` | `0.2355` | 303,250.00 USD | 15,930.00 USD | 0.00 USD | `+52.54%` | `67,638,800,000,000.00` |
| `Live` | `Short` | `0.2375` | 303,350.00 USD | 102.62 USD | 0.00 USD | `+53.83%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2385` | 351,050.00 USD | 47,700.00 USD | 0.00 USD | `+54.48%` | `200,003,000,000,000.00` |
| `Live` | `Short` | `0.2405` | 351,410.00 USD | 361.66 USD | 0.00 USD | `+55.77%` | `1,503,800,000,000.00` |
| `Live` | `Short` | `0.2425` | 352,210.00 USD | 796.25 USD | 0.00 USD | `+57.07%` | `3,283,500,000,000.00` |
| `Live` | `Short` | `0.2445` | 352,440.00 USD | 231.03 USD | 0.00 USD | `+58.37%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2545` | 352,990.00 USD | 546.54 USD | 0.00 USD | `+64.84%` | `2,147,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 356,850.00 USD | 3,870.00 USD | 0.00 USD | `+66.14%` | `15,070,700,000,000.00` |
| `Live` | `Short` | `0.2575` | 385,760.00 USD | 28,910.00 USD | 0.00 USD | `+66.79%` | `112,272,400,000,000.00` |
| `Live` | `Short` | `0.2585` | 438,380.00 USD | 52,620.00 USD | 0.00 USD | `+67.43%` | `203,548,800,000,000.00` |
| `Live` | `Short` | `0.2615` | 438,530.00 USD | 154.94 USD | 0.00 USD | `+69.38%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2685` | 438,760.00 USD | 226.51 USD | 0.00 USD | `+73.91%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2715` | 452,270.00 USD | 13,510.00 USD | 0.00 USD | `+75.85%` | `49,773,600,000,000.00` |
| `Live` | `Short` | `0.2725` | 452,490.00 USD | 214.21 USD | 0.00 USD | `+76.50%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 480,380.00 USD | 27,890.00 USD | 0.00 USD | `+77.80%` | `101,607,700,000,000.00` |
| `Live` | `Short` | `0.2755` | 793,580.00 USD | 313,200.00 USD | 0.00 USD | `+78.44%` | `1,136,837,700,000,000.00` |
| `Live` | `Short` | `0.2795` | 794,060.00 USD | 482.84 USD | 0.00 USD | `+81.04%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2815` | 796,590.00 USD | 2,530.00 USD | 0.00 USD | `+82.33%` | `9,000,000,000,000.00` |
| `Live` | `Short` | `0.2835` | 796,850.00 USD | 253.85 USD | 0.00 USD | `+83.63%` | `895,400,000,000.00` |
| `Live` | `Short` | `0.2915` | 797,040.00 USD | 187.26 USD | 0.00 USD | `+88.81%` | `642,400,000,000.00` |
| `Live` | `Short` | `0.2925` | 797,500.00 USD | 464.84 USD | 0.00 USD | `+89.46%` | `1,589,200,000,000.00` |
| `Live` | `Short` | `0.2955` | 798,540.00 USD | 1,040.00 USD | 0.00 USD | `+91.40%` | `3,534,200,000,000.00` |
| `Live` | `Short` | `0.2995` | 800,820.00 USD | 2,280.00 USD | 0.00 USD | `+93.99%` | `7,608,100,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0355` | 581,290.00 USD | 0.00 USD | 355.00 USD | `-77.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 580,930.00 USD | 0.00 USD | 600.79 USD | `-72.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 580,330.00 USD | 0.00 USD | 353.50 USD | `-67.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 579,980.00 USD | 0.00 USD | 4,310.00 USD | `-64.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 575,670.00 USD | 0.00 USD | 475.11 USD | `-58.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 575,190.00 USD | 0.00 USD | 131.16 USD | `-57.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 575,060.00 USD | 0.00 USD | 881.45 USD | `-56.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 574,180.00 USD | 0.00 USD | 1,070.00 USD | `-56.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 573,110.00 USD | 0.00 USD | 1,400.00 USD | `-55.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 571,710.00 USD | 0.00 USD | 1,010.00 USD | `-54.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 570,700.00 USD | 0.00 USD | 4,100.00 USD | `-54.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 566,590.00 USD | 0.00 USD | 529.04 USD | `-53.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 566,070.00 USD | 0.00 USD | 2,390.00 USD | `-53.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 563,680.00 USD | 0.00 USD | 757.39 USD | `-51.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 562,920.00 USD | 0.00 USD | 1,490.00 USD | `-49.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 561,430.00 USD | 0.00 USD | 277.37 USD | `-43.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 561,160.00 USD | 0.00 USD | 262.50 USD | `-43.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 560,890.00 USD | 0.00 USD | 795.57 USD | `-42.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 560,100.00 USD | 0.00 USD | 181.00 USD | `-41.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 559,920.00 USD | 0.00 USD | 798.65 USD | `-34.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 559,120.00 USD | 0.00 USD | 1,550.00 USD | `-33.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 557,570.00 USD | 0.00 USD | 116.07 USD | `-30.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 557,460.00 USD | 0.00 USD | 19,070.00 USD | `-29.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 538,390.00 USD | 0.00 USD | 577.22 USD | `-28.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 537,810.00 USD | 0.00 USD | 343.50 USD | `-25.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 537,460.00 USD | 0.00 USD | 26,280.00 USD | `-24.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1175` | 511,180.00 USD | 0.00 USD | 105.75 USD | `-23.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 511,080.00 USD | 0.00 USD | 120.50 USD | `-21.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 510,960.00 USD | 0.00 USD | 83,620.00 USD | `-21.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1225` | 427,330.00 USD | 0.00 USD | 487.10 USD | `-20.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 426,850.00 USD | 0.00 USD | 14,940.00 USD | `-19.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 411,910.00 USD | 0.00 USD | 2,670.00 USD | `-18.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 409,240.00 USD | 0.00 USD | 473.27 USD | `-17.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 408,770.00 USD | 0.00 USD | 216,060.00 USD | `-16.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 192,710.00 USD | 0.00 USD | 25,700.00 USD | `-15.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1315` | 167,010.00 USD | 0.00 USD | 1,590.00 USD | `-14.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 165,420.00 USD | 0.00 USD | 5,560.00 USD | `-14.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 159,860.00 USD | 0.00 USD | 625.78 USD | `-13.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 159,230.00 USD | 0.00 USD | 502.28 USD | `-12.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 158,730.00 USD | 0.00 USD | 162.60 USD | `-12.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 158,570.00 USD | 0.00 USD | 8,190.00 USD | `-11.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 150,380.00 USD | 0.00 USD | 1,070.00 USD | `-10.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 149,310.00 USD | 0.00 USD | 108.57 USD | `-10.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 149,200.00 USD | 0.00 USD | 349.74 USD | `-9.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 148,850.00 USD | 0.00 USD | 4,520.00 USD | `-9.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 144,330.00 USD | 0.00 USD | 127.35 USD | `-8.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 144,200.00 USD | 0.00 USD | 24,850.00 USD | `-7.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 119,360.00 USD | 0.00 USD | 1,150.00 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 118,200.00 USD | 0.00 USD | 23,330.00 USD | `-6.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 94,870.00 USD | 0.00 USD | 27,760.00 USD | `-5.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 67,110.00 USD | 0.00 USD | 18,210.00 USD | `-5.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 48,900.00 USD | 0.00 USD | 9,670.00 USD | `-4.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 39,230.00 USD | 0.00 USD | 6,500.00 USD | `-3.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 32,730.00 USD | 0.00 USD | 1,340.00 USD | `-3.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 31,390.00 USD | 0.00 USD | 8,750.00 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 22,630.00 USD | 0.00 USD | 20,020.00 USD | `-1.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 2,610.00 USD | 0.00 USD | 1,510.00 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1535` | 1,100.00 USD | 0.00 USD | 1,100.00 USD | `-0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1545` | 213.35 USD | 213.35 USD | 0.00 USD | `+0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 21,680.00 USD | 21,460.00 USD | 0.00 USD | `+0.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 22,600.00 USD | 927.84 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 23,460.00 USD | 861.71 USD | 0.00 USD | `+2.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1585` | 27,270.00 USD | 3,800.00 USD | 0.00 USD | `+2.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1595` | 27,390.00 USD | 124.14 USD | 0.00 USD | `+3.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1605` | 50,340.00 USD | 22,950.00 USD | 0.00 USD | `+3.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1615` | 51,890.00 USD | 1,550.00 USD | 0.00 USD | `+4.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1625` | 52,360.00 USD | 472.32 USD | 0.00 USD | `+5.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 53,400.00 USD | 1,040.00 USD | 0.00 USD | `+5.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1645` | 57,860.00 USD | 4,450.00 USD | 0.00 USD | `+6.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1655` | 58,780.00 USD | 927.93 USD | 0.00 USD | `+7.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1665` | 108,990.00 USD | 50,210.00 USD | 0.00 USD | `+7.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1675` | 110,260.00 USD | 1,270.00 USD | 0.00 USD | `+8.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1685` | 111,410.00 USD | 1,150.00 USD | 0.00 USD | `+9.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 111,730.00 USD | 317.95 USD | 0.00 USD | `+9.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 113,160.00 USD | 1,430.00 USD | 0.00 USD | `+10.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 114,960.00 USD | 1,800.00 USD | 0.00 USD | `+11.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 115,190.00 USD | 229.89 USD | 0.00 USD | `+11.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 124,030.00 USD | 8,840.00 USD | 0.00 USD | `+12.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 130,670.00 USD | 6,650.00 USD | 0.00 USD | `+13.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 132,030.00 USD | 1,350.00 USD | 0.00 USD | `+13.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 132,470.00 USD | 439.36 USD | 0.00 USD | `+14.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 132,800.00 USD | 336.40 USD | 0.00 USD | `+14.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 133,700.00 USD | 898.02 USD | 0.00 USD | `+15.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 160,090.00 USD | 26,390.00 USD | 0.00 USD | `+16.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 161,370.00 USD | 1,280.00 USD | 0.00 USD | `+16.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 171,610.00 USD | 10,240.00 USD | 0.00 USD | `+17.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 172,480.00 USD | 864.12 USD | 0.00 USD | `+18.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 175,000.00 USD | 2,520.00 USD | 0.00 USD | `+18.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 175,280.00 USD | 276.75 USD | 0.00 USD | `+19.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 175,430.00 USD | 149.79 USD | 0.00 USD | `+20.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 178,620.00 USD | 3,190.00 USD | 0.00 USD | `+20.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 178,760.00 USD | 147.11 USD | 0.00 USD | `+21.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 179,010.00 USD | 245.50 USD | 0.00 USD | `+22.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 179,670.00 USD | 660.73 USD | 0.00 USD | `+22.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 187,270.00 USD | 7,600.00 USD | 0.00 USD | `+23.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 187,670.00 USD | 396.42 USD | 0.00 USD | `+24.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 216,690.00 USD | 29,020.00 USD | 0.00 USD | `+24.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 223,760.00 USD | 7,070.00 USD | 0.00 USD | `+25.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 227,290.00 USD | 3,530.00 USD | 0.00 USD | `+25.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 227,430.00 USD | 137.77 USD | 0.00 USD | `+26.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 227,560.00 USD | 133.19 USD | 0.00 USD | `+27.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 227,700.00 USD | 134.20 USD | 0.00 USD | `+27.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 231,580.00 USD | 3,880.00 USD | 0.00 USD | `+28.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 232,070.00 USD | 492.19 USD | 0.00 USD | `+29.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 254,980.00 USD | 22,900.00 USD | 0.00 USD | `+29.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 255,840.00 USD | 863.97 USD | 0.00 USD | `+30.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 277,180.00 USD | 21,340.00 USD | 0.00 USD | `+31.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 277,360.00 USD | 182.72 USD | 0.00 USD | `+31.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 363,260.00 USD | 85,900.00 USD | 0.00 USD | `+32.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 364,730.00 USD | 1,470.00 USD | 0.00 USD | `+33.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 364,900.00 USD | 174.20 USD | 0.00 USD | `+33.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 366,980.00 USD | 2,080.00 USD | 0.00 USD | `+34.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 367,230.00 USD | 252.51 USD | 0.00 USD | `+35.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 369,600.00 USD | 2,370.00 USD | 0.00 USD | `+36.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 369,720.00 USD | 126.50 USD | 0.00 USD | `+36.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 369,910.00 USD | 190.80 USD | 0.00 USD | `+37.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 370,630.00 USD | 713.94 USD | 0.00 USD | `+38.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 370,840.00 USD | 213.00 USD | 0.00 USD | `+39.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2175` | 371,210.00 USD | 365.12 USD | 0.00 USD | `+40.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 377,480.00 USD | 6,280.00 USD | 0.00 USD | `+41.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 377,850.00 USD | 368.47 USD | 0.00 USD | `+42.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 400,340.00 USD | 22,490.00 USD | 0.00 USD | `+42.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 400,680.00 USD | 333.91 USD | 0.00 USD | `+44.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 404,650.00 USD | 3,980.00 USD | 0.00 USD | `+44.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 405,030.00 USD | 378.55 USD | 0.00 USD | `+46.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 405,410.00 USD | 380.23 USD | 0.00 USD | `+46.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 405,600.00 USD | 185.87 USD | 0.00 USD | `+47.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 405,790.00 USD | 192.69 USD | 0.00 USD | `+48.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2295` | 405,980.00 USD | 187.50 USD | 0.00 USD | `+48.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 450,630.00 USD | 44,650.00 USD | 0.00 USD | `+49.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 454,890.00 USD | 4,260.00 USD | 0.00 USD | `+50.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 456,400.00 USD | 1,520.00 USD | 0.00 USD | `+51.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 477,630.00 USD | 21,230.00 USD | 0.00 USD | `+53.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 480,160.00 USD | 2,530.00 USD | 0.00 USD | `+54.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 480,360.00 USD | 195.67 USD | 0.00 USD | `+55.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 502,060.00 USD | 21,700.00 USD | 0.00 USD | `+55.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 511,360.00 USD | 9,300.00 USD | 0.00 USD | `+56.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 513,120.00 USD | 1,750.00 USD | 0.00 USD | `+59.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 531,870.00 USD | 18,750.00 USD | 0.00 USD | `+59.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 532,420.00 USD | 551.23 USD | 0.00 USD | `+60.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 532,820.00 USD | 397.90 USD | 0.00 USD | `+61.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 537,150.00 USD | 4,330.00 USD | 0.00 USD | `+62.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 537,440.00 USD | 289.23 USD | 0.00 USD | `+62.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 542,450.00 USD | 5,010.00 USD | 0.00 USD | `+63.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 558,330.00 USD | 15,880.00 USD | 0.00 USD | `+64.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 560,110.00 USD | 1,780.00 USD | 0.00 USD | `+64.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 562,670.00 USD | 2,550.00 USD | 0.00 USD | `+65.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 574,400.00 USD | 11,730.00 USD | 0.00 USD | `+66.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 579,560.00 USD | 5,160.00 USD | 0.00 USD | `+66.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 596,420.00 USD | 16,870.00 USD | 0.00 USD | `+68.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 625,560.00 USD | 29,130.00 USD | 0.00 USD | `+68.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 625,830.00 USD | 272.88 USD | 0.00 USD | `+75.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 626,220.00 USD | 394.01 USD | 0.00 USD | `+79.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 626,600.00 USD | 375.53 USD | 0.00 USD | `+81.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 628,730.00 USD | 2,130.00 USD | 0.00 USD | `+84.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 629,310.00 USD | 579.27 USD | 0.00 USD | `+85.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 631,060.00 USD | 1,750.00 USD | 0.00 USD | `+88.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 631,160.00 USD | 101.21 USD | 0.00 USD | `+91.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 631,430.00 USD | 262.73 USD | 0.00 USD | `+92.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 632,860.00 USD | 1,440.00 USD | 0.00 USD | `+92.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 639,030.00 USD | 6,160.00 USD | 0.00 USD | `+94.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 644,450.00 USD | 5,430.00 USD | 0.00 USD | `+95.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 644,740.00 USD | 289.61 USD | 0.00 USD | `+97.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3065` | 645,230.00 USD | 487.09 USD | 0.00 USD | `+98.52%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1336` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 3,580.00 USD | 5,990.00 USD | 16,000.00 USD |
| `7D` | `0.1340` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 9,160.00 USD | 7,730.00 USD | 28,910.00 USD |
| `7D` | `0.1344` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 6,410.00 USD | 5,790.00 USD | 19,420.00 USD |
| `7D` | `0.1348` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 31,170.00 USD | 7,150.00 USD | 23,510.00 USD |
| `7D` | `0.1352` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 11,390.00 USD | 6,290.00 USD | 24,710.00 USD |
| `7D` | `0.1356` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 16,150.00 USD | 12,180.00 USD | 9,380.00 USD |
| `7D` | `0.1360` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 25,240.00 USD | 8,630.00 USD | 8,770.00 USD |
| `7D` | `0.1364` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD |
| `7D` | `0.1368` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 4,500.00 USD | 7,610.00 USD | 2,530.00 USD |
| `1D` | `0.1370` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 0.00 USD | 1,740.00 USD | 2,240.00 USD |
| `7D` | `0.1372` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1373` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 5,470.00 USD | 1,600.00 USD | 0.00 USD |
| `1D` | `0.1376` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 0.00 USD | 1,730.00 USD | 536.58 USD |
| `1D` | `0.1379` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 3,190.00 USD | 1,590.00 USD | 1,020.00 USD |
| `7D` | `0.1380` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD |
| `1D` | `0.1382` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 10,310.00 USD | 10,080.00 USD | 29,450.00 USD |
| `7D` | `0.1384` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 11,880.00 USD | 0.00 USD | 30,320.00 USD |
| `1D` | `0.1385` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 31,240.00 USD | 0.00 USD | 55,520.00 USD |
| `1D` | `0.1388` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 12,440.00 USD | 1,490.00 USD | 0.00 USD |
| `7D` | `0.1388` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD |
| `1D` | `0.1391` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 15,160.00 USD | 1,440.00 USD | 71,370.00 USD |
| `7D` | `0.1392` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD |
| `1D` | `0.1394` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 0.00 USD | 6,230.00 USD | 0.00 USD |
| `7D` | `0.1396` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 28,780.00 USD |
| `1D` | `0.1397` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 12,500.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1400` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 0.00 USD | 2,100.00 USD | 0.00 USD |
| `7D` | `0.1400` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD |
| `7D` | `0.1404` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1412` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD |
| `7D` | `0.1416` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD |
| `7D` | `0.1420` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD |
| `1D` | `0.1421` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 4,030.00 USD | 2,310.00 USD | 6,410.00 USD |
| `7D` | `0.1432` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 10,760.00 USD |
| `1D` | `0.1433` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 3,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1436` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 20,320.00 USD |
| `7D` | `0.1436` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD |
| `1D` | `0.1439` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 17,680.00 USD | 3,590.00 USD | 0.00 USD |
| `7D` | `0.1440` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 13,180.00 USD | 5,260.00 USD | 3,610.00 USD |
| `1D` | `0.1442` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD |
| `7D` | `0.1444` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 3,450.00 USD | 0.00 USD | 6,160.00 USD |
| `1D` | `0.1451` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1452` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 0.00 USD | 5,660.00 USD | 14,180.00 USD |
| `7D` | `0.1456` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD |
| `7D` | `0.1460` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD |
| `1D` | `0.1463` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 1,990.00 USD |
| `7D` | `0.1464` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD |
| `1D` | `0.1466` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 3,010.00 USD |
| `7D` | `0.1468` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 9,720.00 USD | 9,180.00 USD | 3,880.00 USD |
| `1D` | `0.1469` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 12,090.00 USD | 2,700.00 USD | 6,650.00 USD |
| `1D` | `0.1472` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 6,430.00 USD | 14,550.00 USD | 65,860.00 USD |
| `7D` | `0.1472` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 19,180.00 USD | 0.00 USD | 14,170.00 USD |
| `1D` | `0.1475` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 33,920.00 USD | 8,290.00 USD | 2,800.00 USD |
| `7D` | `0.1476` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 68,180.00 USD | 20,180.00 USD | 81,130.00 USD |
| `1D` | `0.1478` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 129,340.00 USD | 11,890.00 USD | 136,980.00 USD |
| `7D` | `0.1480` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 74,500.00 USD | 43,810.00 USD | 50,250.00 USD |
| `1D` | `0.1481` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 60,660.00 USD | 14,570.00 USD | 10,490.00 USD |
| `1D` | `0.1484` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 45,680.00 USD | 4,230.00 USD | 185,460.00 USD |
| `7D` | `0.1484` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 47,020.00 USD | 16,640.00 USD | 201,410.00 USD |
| `1D` | `0.1487` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 8,170.00 USD | 4,430.00 USD | 5,240.00 USD |
| `7D` | `0.1488` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 73,140.00 USD | 10,470.00 USD | 25,980.00 USD |
| `1D` | `0.1490` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 35,320.00 USD | 9,450.00 USD | 4,940.00 USD |
| `7D` | `0.1492` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 40,320.00 USD | 21,590.00 USD | 92,290.00 USD |
| `1D` | `0.1493` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 14,230.00 USD | 1,780.00 USD | 6,470.00 USD |
| `1D` | `0.1496` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 14,390.00 USD | 5,270.00 USD | 2,530.00 USD |
| `7D` | `0.1496` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 34,650.00 USD | 18,690.00 USD | 17,090.00 USD |
| `1D` | `0.1499` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 2,670.00 USD | 0.00 USD | 2,640.00 USD |
| `7D` | `0.1500` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 60,500.00 USD | 9,610.00 USD | 21,940.00 USD |
| `1D` | `0.1502` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 3,610.00 USD | 13,270.00 USD | 130,030.00 USD |
| `7D` | `0.1504` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 20,410.00 USD | 19,520.00 USD | 44,850.00 USD |
| `1D` | `0.1505` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 54,760.00 USD | 23,120.00 USD | 7,830.00 USD |
| `1D` | `0.1508` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 200,020.00 USD | 16,950.00 USD | 259,490.00 USD |
| `7D` | `0.1508` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 200,530.00 USD | 16,820.00 USD | 256,150.00 USD |
| `1D` | `0.1511` | 740,620.00 USD | 0.00 USD | 740,620.00 USD | 122,160.00 USD | 4,360.00 USD | 2,500.00 USD |
| `7D` | `0.1512` | 969,940.00 USD | 0.00 USD | 969,940.00 USD | 86,820.00 USD | 13,310.00 USD | 59,430.00 USD |
| `1D` | `0.1514` | 611,600.00 USD | 0.00 USD | 611,600.00 USD | 25,970.00 USD | 1,730.00 USD | 232,880.00 USD |
| `7D` | `0.1516` | 810,380.00 USD | 0.00 USD | 810,380.00 USD | 48,970.00 USD | 13,330.00 USD | 377,220.00 USD |
| `1D` | `0.1517` | 351,020.00 USD | 0.00 USD | 351,020.00 USD | 87,420.00 USD | 7,460.00 USD | 141,720.00 USD |
| `1D` | `0.1520` | 114,410.00 USD | 0.00 USD | 114,410.00 USD | 44,180.00 USD | 4,100.00 USD | 14,330.00 USD |
| `7D` | `0.1520` | 370,870.00 USD | 0.00 USD | 370,870.00 USD | 47,340.00 USD | 22,090.00 USD | 201,180.00 USD |
| `1D` | `0.1523` | 51,800.00 USD | 0.00 USD | 51,800.00 USD | 34,460.00 USD | 2,970.00 USD | 5,390.00 USD |
| `7D` | `0.1524` | 100,260.00 USD | 0.00 USD | 100,260.00 USD | 0.00 USD | 13,950.00 USD | 8,320.00 USD |
| `7D` | `0.1528` | 78,000.00 USD | 0.00 USD | 78,000.00 USD | 0.00 USD | 33,940.00 USD | 0.00 USD |
| `7D` | `0.1532` | 44,060.00 USD | 0.00 USD | 44,060.00 USD | 0.00 USD | 17,260.00 USD | 0.00 USD |
| `1D` | `0.1535` | 8,980.00 USD | 0.00 USD | 8,980.00 USD | 0.00 USD | 8,980.00 USD | 0.00 USD |
| `7D` | `0.1536` | 26,790.00 USD | 0.00 USD | 26,790.00 USD | 0.00 USD | 8,570.00 USD | 0.00 USD |
| `7D` | `0.1540` | 18,230.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD |
| `7D` | `0.1542` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1544` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1544` | 3,590.00 USD | 3,590.00 USD | 0.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD |
| `1D` | `0.1547` | 13,520.00 USD | 13,520.00 USD | 0.00 USD | 0.00 USD | 13,520.00 USD | 0.00 USD |
| `7D` | `0.1548` | 6,450.00 USD | 6,450.00 USD | 0.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD |
| `1D` | `0.1550` | 17,980.00 USD | 17,980.00 USD | 0.00 USD | 0.00 USD | 4,460.00 USD | 0.00 USD |
| `7D` | `0.1552` | 18,270.00 USD | 18,270.00 USD | 0.00 USD | 0.00 USD | 11,820.00 USD | 0.00 USD |
| `1D` | `0.1553` | 19,510.00 USD | 19,510.00 USD | 0.00 USD | 0.00 USD | 1,530.00 USD | 0.00 USD |
| `7D` | `0.1560` | 29,260.00 USD | 29,260.00 USD | 0.00 USD | 0.00 USD | 10,990.00 USD | 0.00 USD |
| `1D` | `0.1562` | 24,480.00 USD | 24,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `0.1564` | 63,020.00 USD | 63,020.00 USD | 0.00 USD | 0.00 USD | 33,750.00 USD | 0.00 USD |
| `1D` | `0.1565` | 331,620.00 USD | 331,620.00 USD | 0.00 USD | 41,260.00 USD | 13,270.00 USD | 252,610.00 USD |
| `1D` | `0.1568` | 619,440.00 USD | 619,440.00 USD | 0.00 USD | 33,360.00 USD | 38,630.00 USD | 215,830.00 USD |
| `7D` | `0.1568` | 341,690.00 USD | 341,690.00 USD | 0.00 USD | 111,700.00 USD | 15,360.00 USD | 151,620.00 USD |
| `1D` | `0.1571` | 725,710.00 USD | 725,710.00 USD | 0.00 USD | 40,700.00 USD | 6,150.00 USD | 59,420.00 USD |
| `7D` | `0.1572` | 675,490.00 USD | 675,490.00 USD | 0.00 USD | 235,420.00 USD | 39,540.00 USD | 58,840.00 USD |
| `1D` | `0.1574` | 751,680.00 USD | 751,680.00 USD | 0.00 USD | 25,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1576` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 44,680.00 USD | 123,840.00 USD | 315,950.00 USD |
| `1D` | `0.1577` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 69,720.00 USD | 0.00 USD | 351,730.00 USD |
| `7D` | `0.1580` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 226,250.00 USD | 101,090.00 USD | 0.00 USD |
| `1D` | `0.1583` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 62,490.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1584` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 80,450.00 USD | 43,370.00 USD | 114,120.00 USD |
| `1D` | `0.1586` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 17,270.00 USD | 16,450.00 USD |
| `7D` | `0.1588` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 69,180.00 USD | 44,590.00 USD | 0.00 USD |
| `1D` | `0.1589` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 15,100.00 USD | 19,490.00 USD | 13,300.00 USD |
| `1D` | `0.1592` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 20,480.00 USD | 21,620.00 USD |
| `7D` | `0.1592` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 64,620.00 USD | 0.00 USD |
| `1D` | `0.1595` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39,910.00 USD |
| `7D` | `0.1596` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 98,530.00 USD | 0.00 USD |
| `1D` | `0.1598` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 16,680.00 USD | 0.00 USD | 99,410.00 USD |
| `7D` | `0.1600` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 60,710.00 USD | 75,810.00 USD |
| `1D` | `0.1601` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 20,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1604` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 99,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1604` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 188,060.00 USD | 112,090.00 USD | 273,670.00 USD |
| `1D` | `0.1607` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 12,980.00 USD | 0.00 USD | 115,120.00 USD |
| `7D` | `0.1608` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 208,080.00 USD | 240,680.00 USD | 329,980.00 USD |
| `1D` | `0.1610` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 34,860.00 USD | 0.00 USD | 106,180.00 USD |
| `7D` | `0.1612` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 353,120.00 USD | 328,050.00 USD | 287,340.00 USD |
| `1D` | `0.1613` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 37,090.00 USD | 11,530.00 USD | 94,020.00 USD |
| `1D` | `0.1616` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 14,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1616` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 293,210.00 USD | 131,180.00 USD | 165,860.00 USD |
| `1D` | `0.1619` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 91,300.00 USD | 41,970.00 USD | 0.00 USD |
| `7D` | `0.1620` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 0.00 USD | 196,620.00 USD | 0.00 USD |
| `1D` | `0.1622` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 76,010.00 USD | 54,640.00 USD | 0.00 USD |
| `7D` | `0.1624` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 193,150.00 USD | 0.00 USD |
| `1D` | `0.1625` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 54,920.00 USD | 48,390.00 USD | 0.00 USD |
| `1D` | `0.1628` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 101,620.00 USD |
| `7D` | `0.1628` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 76,780.00 USD | 0.00 USD | 103,330.00 USD |
| `1D` | `0.1631` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 88,400.00 USD | 23,990.00 USD | 0.00 USD |
| `1D` | `0.1634` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 10,020.00 USD | 10,690.00 USD | 8,690.00 USD |
| `7D` | `0.1636` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 13,670.00 USD | 23,560.00 USD |
| `1D` | `0.1637` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 22,520.00 USD | 0.00 USD |
| `1D` | `0.1640` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 9,110.00 USD | 13,330.00 USD | 0.00 USD |
| `7D` | `0.1640` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD |
| `1D` | `0.1643` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 10,070.00 USD | 35,000.00 USD | 16,030.00 USD |
| `7D` | `0.1644` | 5,700,000.00 USD | 5,700,000.00 USD | 0.00 USD | 0.00 USD | 8,990.00 USD | 0.00 USD |
| `1D` | `0.1646` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 14,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1648` | 5,700,000.00 USD | 5,700,000.00 USD | 0.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD |
| `1D` | `0.1655` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 7,370.00 USD | 8,050.00 USD |
| `7D` | `0.1656` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 0.00 USD | 31,800.00 USD | 0.00 USD |
| `1D` | `0.1658` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 9,730.00 USD | 47,930.00 USD | 0.00 USD |
| `7D` | `0.1660` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 79,170.00 USD | 11,020.00 USD | 51,660.00 USD |
| `1D` | `0.1661` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 8,220.00 USD | 11,150.00 USD | 50,810.00 USD |
| `1D` | `0.1664` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 66,370.00 USD | 14,550.00 USD | 80,540.00 USD |
| `7D` | `0.1664` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD |
| `1D` | `0.1667` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 5,340.00 USD | 41,840.00 USD |
| `7D` | `0.1668` | 6,310,000.00 USD | 6,310,000.00 USD | 0.00 USD | 42,580.00 USD | 52,290.00 USD | 87,160.00 USD |
| `7D` | `0.1672` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 135,250.00 USD | 62,490.00 USD | 0.00 USD |
| `1D` | `0.1673` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 66,630.00 USD | 2,010.00 USD | 19,670.00 USD |
| `1D` | `0.1676` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 22,100.00 USD | 1,990.00 USD | 0.00 USD |
| `7D` | `0.1676` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 84,020.00 USD | 141,950.00 USD | 0.00 USD |
| `1D` | `0.1679` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 6,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1680` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 121,860.00 USD | 80,270.00 USD | 15,310.00 USD |
| `1D` | `0.1682` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 154,780.00 USD | 4,560.00 USD | 18,740.00 USD |
| `7D` | `0.1684` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD |
| `1D` | `0.1685` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 20,370.00 USD | 29,790.00 USD | 13,450.00 USD |
| `1D` | `0.1688` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 2,650.00 USD | 39,950.00 USD |
| `7D` | `0.1688` | 7,040,000.00 USD | 7,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD |
| `1D` | `0.1691` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 75,680.00 USD | 76,030.00 USD | 54,060.00 USD |
| `7D` | `0.1692` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 33,660.00 USD | 70,740.00 USD | 71,020.00 USD |
| `1D` | `0.1694` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 34,000.00 USD | 22,300.00 USD | 11,880.00 USD |
| `7D` | `0.1696` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 17,360.00 USD | 87,350.00 USD | 39,780.00 USD |
| `1D` | `0.1697` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 36,180.00 USD | 38,310.00 USD | 6,650.00 USD |
| `1D` | `0.1700` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 13,350.00 USD | 21,160.00 USD | 46,050.00 USD |
| `7D` | `0.1700` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD |
| `1D` | `0.1703` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 9,960.00 USD | 14,420.00 USD | 34,530.00 USD |
| `7D` | `0.1704` | 7,580,000.00 USD | 7,580,000.00 USD | 0.00 USD | 55,170.00 USD | 46,880.00 USD | 0.00 USD |
| `1D` | `0.1706` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 38,860.00 USD | 9,590.00 USD | 13,990.00 USD |
| `7D` | `0.1708` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 0.00 USD | 25,490.00 USD | 87,520.00 USD |
| `1D` | `0.1709` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 21,630.00 USD | 62,270.00 USD | 2,710.00 USD |
| `1D` | `0.1712` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 15,040.00 USD | 5,330.00 USD |
| `1D` | `0.1715` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 9,570.00 USD | 27,880.00 USD | 9,370.00 USD |
| `7D` | `0.1716` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 0.00 USD | 42,020.00 USD | 15,160.00 USD |
| `1D` | `0.1718` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 12,630.00 USD | 10,110.00 USD | 10,190.00 USD |
| `7D` | `0.1720` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 161,770.00 USD |
| `1D` | `0.1721` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 107,900.00 USD | 16,860.00 USD | 30,720.00 USD |
| `1D` | `0.1724` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 21,930.00 USD | 0.00 USD | 48,370.00 USD |
| `7D` | `0.1724` | 8,240,000.00 USD | 8,240,000.00 USD | 0.00 USD | 118,060.00 USD | 0.00 USD | 208,480.00 USD |
| `1D` | `0.1727` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 2,410.00 USD | 8,570.00 USD |
| `1D` | `0.1730` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 6,720.00 USD |
| `7D` | `0.1732` | 8,730,000.00 USD | 8,730,000.00 USD | 0.00 USD | 476,430.00 USD | 0.00 USD | 9,420.00 USD |
| `1D` | `0.1733` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD |
| `1D` | `0.1736` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 14,970.00 USD | 9,510.00 USD | 0.00 USD |
| `1D` | `0.1739` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 18,610.00 USD | 2,310.00 USD | 12,270.00 USD |
| `7D` | `0.1740` | 8,810,000.00 USD | 8,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 83,810.00 USD |
| `1D` | `0.1742` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 1,600.00 USD | 11,320.00 USD |
| `7D` | `0.1744` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1745` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 8,530.00 USD | 2,460.00 USD | 8,910.00 USD |
| `1D` | `0.1748` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 55,280.00 USD | 2,280.00 USD | 39,610.00 USD |
| `7D` | `0.1748` | 8,910,000.00 USD | 8,910,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `0.1751` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 41,730.00 USD | 0.00 USD | 14,050.00 USD |
| `7D` | `0.1752` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 291,880.00 USD |
| `1D` | `0.1754` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 32,060.00 USD | 8,430.00 USD | 46,490.00 USD |
| `7D` | `0.1756` | 9,500,000.00 USD | 9,500,000.00 USD | 0.00 USD | 112,930.00 USD | 0.00 USD | 186,030.00 USD |
| `1D` | `0.1757` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 15,820.00 USD | 40,160.00 USD | 76,710.00 USD |
| `1D` | `0.1760` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 94,020.00 USD | 79,990.00 USD | 21,230.00 USD |
| `7D` | `0.1760` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 268,160.00 USD | 71,260.00 USD | 32,350.00 USD |
| `1D` | `0.1763` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 59,300.00 USD | 22,900.00 USD | 68,500.00 USD |
| `7D` | `0.1764` | 10,540,000.00 USD | 10,540,000.00 USD | 0.00 USD | 353,950.00 USD | 270,450.00 USD | 40,340.00 USD |
| `1D` | `0.1766` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 15,830.00 USD | 20,220.00 USD | 62,960.00 USD |
| `7D` | `0.1768` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 191,690.00 USD | 147,360.00 USD | 31,570.00 USD |
| `1D` | `0.1769` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 40,920.00 USD | 78,870.00 USD | 44,210.00 USD |
| `1D` | `0.1772` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 22,380.00 USD | 5,670.00 USD | 0.00 USD |
| `7D` | `0.1772` | 11,180,000.00 USD | 11,180,000.00 USD | 0.00 USD | 98,390.00 USD | 153,480.00 USD | 21,360.00 USD |
| `7D` | `0.1776` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 186,770.00 USD | 59,720.00 USD | 0.00 USD |
| `7D` | `0.1780` | 11,680,000.00 USD | 11,680,000.00 USD | 0.00 USD | 52,730.00 USD | 46,410.00 USD | 157,510.00 USD |
| `7D` | `0.1784` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD |
| `7D` | `0.1788` | 12,080,000.00 USD | 12,080,000.00 USD | 0.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD |
| `7D` | `0.1792` | 12,310,000.00 USD | 12,310,000.00 USD | 0.00 USD | 182,810.00 USD | 46,960.00 USD | 3,940.00 USD |
| `7D` | `0.1796` | 12,400,000.00 USD | 12,400,000.00 USD | 0.00 USD | 17,130.00 USD | 26,110.00 USD | 44,450.00 USD |
| `7D` | `0.1800` | 12,520,000.00 USD | 12,520,000.00 USD | 0.00 USD | 12,940.00 USD | 34,680.00 USD | 73,510.00 USD |
| `7D` | `0.1804` | 12,610,000.00 USD | 12,610,000.00 USD | 0.00 USD | 35,280.00 USD | 32,850.00 USD | 23,570.00 USD |
| `7D` | `0.1808` | 12,790,000.00 USD | 12,790,000.00 USD | 0.00 USD | 35,050.00 USD | 67,250.00 USD | 73,440.00 USD |
| `7D` | `0.1812` | 12,930,000.00 USD | 12,930,000.00 USD | 0.00 USD | 64,990.00 USD | 29,900.00 USD | 50,510.00 USD |
| `7D` | `0.1816` | 13,070,000.00 USD | 13,070,000.00 USD | 0.00 USD | 69,700.00 USD | 33,940.00 USD | 38,270.00 USD |
| `7D` | `0.1820` | 13,240,000.00 USD | 13,240,000.00 USD | 0.00 USD | 65,350.00 USD | 54,880.00 USD | 43,100.00 USD |
| `7D` | `0.1824` | 13,450,000.00 USD | 13,450,000.00 USD | 0.00 USD | 80,350.00 USD | 17,880.00 USD | 112,550.00 USD |
| `7D` | `0.1828` | 13,630,000.00 USD | 13,630,000.00 USD | 0.00 USD | 79,610.00 USD | 29,630.00 USD | 69,840.00 USD |
| `7D` | `0.1832` | 13,840,000.00 USD | 13,840,000.00 USD | 0.00 USD | 108,540.00 USD | 31,590.00 USD | 74,200.00 USD |
| `7D` | `0.1836` | 14,180,000.00 USD | 14,180,000.00 USD | 0.00 USD | 172,660.00 USD | 110,870.00 USD | 52,650.00 USD |
| `7D` | `0.1840` | 14,520,000.00 USD | 14,520,000.00 USD | 0.00 USD | 141,620.00 USD | 50,840.00 USD | 151,740.00 USD |
| `7D` | `0.1844` | 14,740,000.00 USD | 14,740,000.00 USD | 0.00 USD | 94,510.00 USD | 20,390.00 USD | 97,510.00 USD |
| `7D` | `0.1848` | 14,880,000.00 USD | 14,880,000.00 USD | 0.00 USD | 35,280.00 USD | 69,910.00 USD | 41,760.00 USD |
| `7D` | `0.1852` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 168,270.00 USD | 28,290.00 USD | 251,810.00 USD |
| `7D` | `0.1856` | 15,570,000.00 USD | 15,570,000.00 USD | 0.00 USD | 100,160.00 USD | 21,030.00 USD | 120,950.00 USD |
| `7D` | `0.1860` | 15,810,000.00 USD | 15,810,000.00 USD | 0.00 USD | 64,600.00 USD | 48,330.00 USD | 127,610.00 USD |
| `7D` | `0.1864` | 15,970,000.00 USD | 15,970,000.00 USD | 0.00 USD | 48,260.00 USD | 44,140.00 USD | 61,380.00 USD |
| `7D` | `0.1868` | 16,200,000.00 USD | 16,200,000.00 USD | 0.00 USD | 133,990.00 USD | 38,100.00 USD | 56,290.00 USD |
| `7D` | `0.1872` | 16,580,000.00 USD | 16,580,000.00 USD | 0.00 USD | 169,490.00 USD | 133,380.00 USD | 86,910.00 USD |
| `7D` | `0.1876` | 16,720,000.00 USD | 16,720,000.00 USD | 0.00 USD | 65,910.00 USD | 23,180.00 USD | 43,960.00 USD |
| `7D` | `0.1880` | 16,830,000.00 USD | 16,830,000.00 USD | 0.00 USD | 57,250.00 USD | 22,460.00 USD | 30,950.00 USD |
| `7D` | `0.1884` | 16,890,000.00 USD | 16,890,000.00 USD | 0.00 USD | 14,000.00 USD | 35,430.00 USD | 9,740.00 USD |
| `7D` | `0.1888` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 22,970.00 USD | 4,800.00 USD | 88,260.00 USD |
| `7D` | `0.1892` | 17,090,000.00 USD | 17,090,000.00 USD | 0.00 USD | 49,980.00 USD | 2,860.00 USD | 34,160.00 USD |
| `7D` | `0.1896` | 17,160,000.00 USD | 17,160,000.00 USD | 0.00 USD | 42,320.00 USD | 11,820.00 USD | 18,680.00 USD |
| `7D` | `0.1900` | 17,210,000.00 USD | 17,210,000.00 USD | 0.00 USD | 0.00 USD | 29,650.00 USD | 20,420.00 USD |
| `7D` | `0.1904` | 17,250,000.00 USD | 17,250,000.00 USD | 0.00 USD | 14,330.00 USD | 10,990.00 USD | 10,800.00 USD |
| `7D` | `0.1908` | 17,330,000.00 USD | 17,330,000.00 USD | 0.00 USD | 24,190.00 USD | 37,870.00 USD | 18,740.00 USD |
| `7D` | `0.1912` | 17,350,000.00 USD | 17,350,000.00 USD | 0.00 USD | 0.00 USD | 9,380.00 USD | 10,330.00 USD |
| `7D` | `0.1916` | 17,380,000.00 USD | 17,380,000.00 USD | 0.00 USD | 7,460.00 USD | 5,300.00 USD | 11,900.00 USD |
| `7D` | `0.1920` | 17,380,000.00 USD | 17,380,000.00 USD | 0.00 USD | 0.00 USD | 5,100.00 USD | 0.00 USD |
| `7D` | `0.1924` | 17,400,000.00 USD | 17,400,000.00 USD | 0.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD |
| `7D` | `0.1928` | 17,420,000.00 USD | 17,420,000.00 USD | 0.00 USD | 11,600.00 USD | 7,370.00 USD | 0.00 USD |
| `7D` | `0.1944` | 17,430,000.00 USD | 17,430,000.00 USD | 0.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1952` | 17,440,000.00 USD | 17,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD |
| `7D` | `0.1956` | 17,440,000.00 USD | 17,440,000.00 USD | 0.00 USD | 4,860.00 USD | 2,760.00 USD | 0.00 USD |
| `7D` | `0.1960` | 17,450,000.00 USD | 17,450,000.00 USD | 0.00 USD | 5,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1964` | 17,470,000.00 USD | 17,470,000.00 USD | 0.00 USD | 6,470.00 USD | 2,700.00 USD | 10,990.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `187.04M` | Total OI Tokens: `1,213,321,497.7 ARB`
  * 1h OI Change: `-1.17%` | 4h OI Change: `-10.17%` | 24h OI Change: `-19.59%`
  * Exchange Breakdown: Binance=`42.64M` | Bybit=`27.67M` | OKX=`13.85M` | Hyperliquid=`12.47M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-5.44K` | Last 24h: `10.97K` | Last 3d: `22.34K` | Last 7d: `43.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0080%` | **USDT OKX** | `-0.0031%` |
| **USDT Bybit** | `-0.0064%` | **USDT KuCoin** | `0.0001%` |
| **USDT MEXC** | `-0.0031%` | **USDT BingX** | `-0.0023%` |
| **USDT Gate** | `-0.0075%` | **USDT Bitget** | `-0.0035%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `57.53%` | `42.47%` | `1.35` | 3,130,000.00 USD |
| `15M` | `Binance` | `45.4%` | `54.6%` | `0.83` | 1,010,000.00 USD |
| `15M` | `OKX` | `39.88%` | `60.12%` | `0.66` | 293,690.00 USD |
| `15M` | `Bybit` | `59.31%` | `40.69%` | `1.46` | 212,510.00 USD |
| `15M` | `KuCoin` | `52.96%` | `47.04%` | `1.13` | 176,940.00 USD |
| `15M` | `Gate` | `44.29%` | `55.71%` | `0.80` | 101,830.00 USD |
| `15M` | `Bitget` | `44.14%` | `55.86%` | `0.79` | 41,270.00 USD |
| `15M` | `BingX` | `97.19%` | `2.81%` | `34.59` | 769,100.00 USD |
| `15M` | `MEXC` | `47.92%` | `52.08%` | `0.92` | 63,730.00 USD |
| `15M` | `Bitunix` | `38.9%` | `61.1%` | `0.64` | 36,270.00 USD |
| `15M` | `Hyperliquid` | `13.05%` | `86.95%` | `0.15` | 218,250.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.34%` | `49.66%` | `1.01` | 80,770.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `65.24%` | `34.76%` | `1.88` | 121,640.00 USD |
| `15M` | `HTX` | `54.29%` | `45.71%` | `1.19` | 356.55 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `26.2%` | `73.8%` | `0.36` | 3,400.00 USD |
| `15M` | `Aster` | `3.2%` | `96.8%` | `0.03` | 173.32 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `38.35%` | `61.65%` | `0.62` | 16.04 USD |
| `15M` | `Whale Positions` | `45.4%` | `54.6%` | `0.83` | 1,010,000.00 USD |
| `15M` | `Global Accounts` | `57.53%` | `42.47%` | `1.35` | 3,130,000.00 USD |
| `1H` | `ARB` | `50.34%` | `49.66%` | `1.01` | 7,810,000.00 USD |
| `1H` | `Binance` | `55.99%` | `44.01%` | `1.27` | 2,700,000.00 USD |
| `1H` | `OKX` | `44.33%` | `55.67%` | `0.80` | 710,190.00 USD |
| `1H` | `Bybit` | `50.96%` | `49.04%` | `1.04` | 848,580.00 USD |
| `1H` | `KuCoin` | `47.18%` | `52.82%` | `0.89` | 33,620.00 USD |
| `1H` | `Gate` | `54.8%` | `45.2%` | `1.21` | 142,710.00 USD |
| `1H` | `Bitget` | `53.3%` | `46.7%` | `1.14` | 248,030.00 USD |
| `1H` | `BingX` | `23.9%` | `76.1%` | `0.31` | 500,360.00 USD |
| `1H` | `MEXC` | `54.04%` | `45.96%` | `1.18` | 637,420.00 USD |
| `1H` | `Bitunix` | `51.38%` | `48.62%` | `1.06` | 59,530.00 USD |
| `1H` | `Hyperliquid` | `47.78%` | `52.22%` | `0.91` | 293,540.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.91%` | `51.09%` | `0.96` | 1,270,000.00 USD |
| `1H` | `Crypto.com` | `19.68%` | `80.32%` | `0.25` | 11.33 USD |
| `1H` | `WhiteBIT` | `52.61%` | `47.39%` | `1.11` | 338,590.00 USD |
| `1H` | `HTX` | `35.09%` | `64.91%` | `0.54` | 1,830.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `54.07%` | `45.93%` | `1.18` | 3,570.00 USD |
| `1H` | `Aster` | `26.04%` | `73.96%` | `0.35` | 13,900.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `65.2%` | `34.8%` | `1.87` | 13,830.00 USD |
| `1H` | `Whale Positions` | `55.99%` | `44.01%` | `1.27` | 2,700,000.00 USD |
| `1H` | `Global Accounts` | `50.34%` | `49.66%` | `1.01` | 7,810,000.00 USD |
| `4H` | `ARB` | `47.16%` | `52.84%` | `0.89` | 58,930,000.00 USD |
| `4H` | `Binance` | `47.02%` | `52.98%` | `0.89` | 22,420,000.00 USD |
| `4H` | `OKX` | `46.3%` | `53.7%` | `0.86` | 7,100,000.00 USD |
| `4H` | `Bybit` | `45.88%` | `54.12%` | `0.85` | 9,310,000.00 USD |
| `4H` | `KuCoin` | `46.45%` | `53.55%` | `0.87` | 527,560.00 USD |
| `4H` | `Gate` | `53.26%` | `46.74%` | `1.14` | 717,650.00 USD |
| `4H` | `Bitget` | `48.56%` | `51.44%` | `0.94` | 3,690,000.00 USD |
| `4H` | `BingX` | `44.81%` | `55.19%` | `0.81` | 1,800,000.00 USD |
| `4H` | `MEXC` | `45.33%` | `54.67%` | `0.83` | 2,920,000.00 USD |
| `4H` | `Bitunix` | `45.64%` | `54.36%` | `0.84` | 694,930.00 USD |
| `4H` | `Hyperliquid` | `38.76%` | `61.24%` | `0.63` | 967,720.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.22%` | `51.78%` | `0.93` | 7,610,000.00 USD |
| `4H` | `Crypto.com` | `23.33%` | `76.67%` | `0.30` | 23,230.00 USD |
| `4H` | `WhiteBIT` | `73.28%` | `26.72%` | `2.74` | 878,200.00 USD |
| `4H` | `HTX` | `47.62%` | `52.38%` | `0.91` | 47,580.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `57.54%` | `42.46%` | `1.36` | 66,650.00 USD |
| `4H` | `Aster` | `28.97%` | `71.03%` | `0.41` | 65,850.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `53.67%` | `46.33%` | `1.16` | 88,580.00 USD |
| `4H` | `Whale Positions` | `47.02%` | `52.98%` | `0.89` | 22,420,000.00 USD |
| `4H` | `Global Accounts` | `47.16%` | `52.84%` | `0.89` | 58,930,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1535` | `0.1536` | `0.1535` | `0.1560` | `0.1508` | 10,296,961.64 USD | 4,216,389.14 USD | 6,080,572.50 USD | -1,864,183.37 USD | `-18.10%` | `2B / 11S` |
| `0:00 UTC` | `0.1558` | `0.1546` | `0.1558` | `0.1572` | `0.1528` | 5,930,771.66 USD | 3,398,964.11 USD | 2,531,807.55 USD | 867,156.57 USD | `+14.62%` | `22B / 10S` |
| `5:00 UTC` | `0.1590` | `0.1587` | `0.1590` | `0.1599` | `0.1565` | 3,702,564.80 USD | 1,807,551.39 USD | 1,895,013.41 USD | -87,462.01 USD | `-2.36%` | `26B / 13S` |
| `0:00 UTC` | `0.1596` | `0.1591` | `0.1596` | `0.1603` | `0.1573` | 4,839,053.12 USD | 2,292,867.68 USD | 2,546,185.45 USD | -253,317.77 USD | `-5.23%` | `10B / 17S` |
| `5:00 UTC` | `0.1575` | `0.1570` | `0.1575` | `0.1586` | `0.1556` | 1,633,700.68 USD | 751,464.39 USD | 882,236.29 USD | -130,771.91 USD | `-8.00%` | `12B / 24S` |
| `0:00 UTC` | `0.1538` | `0.1546` | `0.1538` | `0.1566` | `0.1527` | 4,221,220.85 USD | 1,992,401.80 USD | 2,228,819.05 USD | -236,417.24 USD | `-5.60%` | `9B / 15S` |
| `5:00 UTC` | `0.1558` | `0.1551` | `0.1558` | `0.1566` | `0.1531` | 3,305,715.92 USD | 1,746,218.57 USD | 1,559,497.34 USD | 186,721.23 USD | `+5.65%` | `15B / 16S` |
| `0:00 UTC` | `0.1554` | `0.1556` | `0.1554` | `0.1566` | `0.1545` | 1,212,948.28 USD | 642,062.88 USD | 570,885.41 USD | 71,177.47 USD | `+5.87%` | `14B / 5S` |
| `5:00 UTC` | `0.1549` | `0.1546` | `0.1549` | `0.1552` | `0.1540` | 1,122,592.32 USD | 618,049.70 USD | 504,542.62 USD | 113,507.08 USD | `+10.11%` | `10B / 12S` |
| `0:00 UTC` | `0.1540` | `0.1539` | `0.1540` | `0.1545` | `0.1534` | 337,802.09 USD | 186,096.97 USD | 151,705.12 USD | 34,391.85 USD | `+10.18%` | `25B / 23S` |

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
| `5m` | -97,690.00 USD | -175,990.00 USD | **`DISTRIBUTION`** |
| `15m` | -76,310.00 USD | 16,010.00 USD | **`DISTRIBUTION`** |
| `30m` | 51,080.00 USD | 261,480.00 USD | **`ACCUMULATION`** |
| `1h` | 424,910.00 USD | 1,170,000.00 USD | **`ACCUMULATION`** |
| `2h` | 321,340.00 USD | 1,010,000.00 USD | **`ACCUMULATION`** |
| `4h` | -1,650,000.00 USD | -4,770,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,790,000.00 USD | -5,730,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,570,000.00 USD | -7,180,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,610,000.00 USD | -8,700,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,460,000.00 USD | -9,060,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,330,000.00 USD | -35,020,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,810,000.00 USD | -163,390,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-97.69K` | 15m=`-76.31K` | 1h=`+424.91K` | 24h=`-2.46M`
* Futures Capital Netflows: 5m=`-175.99K` | 15m=`+16.01K` | 1h=`+1.17M` | 24h=`-9.06M`
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
  * `2026-10-30 04:14:42 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:42 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
