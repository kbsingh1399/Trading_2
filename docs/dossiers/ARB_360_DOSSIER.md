# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 03:46:30 IST` (`2026-10-29 22:16:30 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1535` | `0.1549` | `0.1527` | `0.1546` | `9,702,226` | 1,493,571.42 USD | 46,384.72 USD | `+3.11%` | -7,925,504.42 USD | `+0.55` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.1546` | `0.1561` | `0.1539` | `0.1543` | `7,395,561` | 1,146,301.28 USD | 17,998.31 USD | `+1.57%` | -7,907,506.11 USD | `+0.43` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1543` | `0.1543` | `0.1540` | `0.1542` | `301,976` | 46,545.57 USD | -2,465.92 USD | `-5.30%` | -7,909,972.02 USD | `+0.32` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1576` | `0.1586` | `0.1556` | `0.1556` | `10,403,893` | 1,633,700.68 USD | -130,771.91 USD | `-8.00%` | -7,638,750.84 USD | `+0.11` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1556` | `0.1566` | `0.1527` | `0.1543` | `27,306,448` | 4,221,220.85 USD | -236,417.24 USD | `-5.60%` | -7,875,168.08 USD | `-0.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1543` | `0.1543` | `0.1540` | `0.1542` | `301,976` | 46,545.57 USD | -2,465.92 USD | `-5.30%` | -7,877,634.00 USD | `+0.29` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1683` | `0.1684` | `0.1508` | `0.1534` | `152,241,290` | 23,969,202.69 USD | -4,416,609.68 USD | `-18.43%` | -7,801,776.00 USD | `-4.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1534` | `0.1603` | `0.1528` | `0.1556` | `102,506,063` | 16,106,228.03 USD | 395,467.12 USD | `+2.46%` | -7,406,308.88 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1556` | `0.1566` | `0.1527` | `0.1542` | `27,608,423` | 4,267,766.42 USD | -238,883.16 USD | `-5.60%` | -7,645,192.04 USD | `+0.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,374,542.78 USD | `-1.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,572,000.78 USD | `-0.89` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `282,355,777` | 44,343,197.14 USD | -4,260,025.72 USD | `-9.61%` | -7,832,026.51 USD | `-2.09` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1652` | `0.1687` | `0.1623` | `0.1631` | `68,085,678` | 11,252,816.65 USD | -909,329.92 USD | `-8.08%` | -705,420.63 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,136,414.44 USD | `-0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,374,542.78 USD | `-1.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,572,000.78 USD | `-0.89` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `282,355,777` | 44,343,197.14 USD | -4,260,025.72 USD | `-9.61%` | -7,832,026.51 USD | `-2.09` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:45:41 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1617` | 11,754.43 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 11.75K USD at 0.1617 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `0.1715` | 8,431.67 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale SELL: 8.43K USD at 0.1715 USD [API] | `2026-10-28 18:42:13` |
| `ANNOUNCEMENT` | `INFO` | `0.1719` | 6,013.83 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale SELL: 6.01K USD at 0.1719 USD [API] | `2026-10-28 18:43:59` |


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
| `7D` | `Long Liquidation` | `0.1336` | 2,720,000.00 USD | 2,720,000.00 USD | 3,580.00 USD | 5,990.00 USD | 16,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1340` | 2,700,000.00 USD | 2,700,000.00 USD | 9,160.00 USD | 7,730.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1344` | 2,650,000.00 USD | 2,650,000.00 USD | 6,410.00 USD | 5,790.00 USD | 19,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1345` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 691.54 USD | 598.60 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1345` | 741.71 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1348` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1348` | 2,620,000.00 USD | 2,620,000.00 USD | 31,170.00 USD | 7,150.00 USD | 23,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1351` | 2,040,000.00 USD | 2,040,000.00 USD | 6,820.00 USD | 2,050.00 USD | 5,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1352` | 2,560,000.00 USD | 2,560,000.00 USD | 11,390.00 USD | 6,290.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1354` | 2,030,000.00 USD | 2,030,000.00 USD | 2,670.00 USD | 688.99 USD | 4,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1355` | 38,490.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1356` | 2,520,000.00 USD | 2,520,000.00 USD | 16,150.00 USD | 12,180.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1357` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 2,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1360` | 2,020,000.00 USD | 2,020,000.00 USD | 2,480.00 USD | 869.31 USD | 4,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1360` | 2,480,000.00 USD | 2,480,000.00 USD | 25,240.00 USD | 8,630.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1363` | 2,010,000.00 USD | 2,010,000.00 USD | 4,890.00 USD | 2,360.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1364` | 2,440,000.00 USD | 2,440,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 53,980.00 USD | 965,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1366` | 2,000,000.00 USD | 2,000,000.00 USD | 1,340.00 USD | 484.70 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1368` | 2,410,000.00 USD | 2,410,000.00 USD | 4,500.00 USD | 7,610.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1369` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1372` | 2,000,000.00 USD | 2,000,000.00 USD | 5,470.00 USD | 1,110.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1372` | 2,400,000.00 USD | 2,400,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1375` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 2,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1378` | 1,990,000.00 USD | 1,990,000.00 USD | 936.88 USD | 1,590.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1380` | 2,390,000.00 USD | 2,390,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1381` | 1,980,000.00 USD | 1,980,000.00 USD | 5,890.00 USD | 7,190.00 USD | 27,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1384` | 1,940,000.00 USD | 1,940,000.00 USD | 17,120.00 USD | 2,890.00 USD | 38,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1384` | 2,380,000.00 USD | 2,380,000.00 USD | 11,880.00 USD | 0.00 USD | 30,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 22,700.00 USD | 911,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1387` | 1,880,000.00 USD | 1,880,000.00 USD | 33,240.00 USD | 2,090.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1388` | 2,340,000.00 USD | 2,340,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1390` | 1,850,000.00 USD | 1,850,000.00 USD | 5,190.00 USD | 1,970.00 USD | 23,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1392` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 4,690.00 USD | 28,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1393` | 1,820,000.00 USD | 1,820,000.00 USD | 9,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 6,570.00 USD | 888,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1396` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 6,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1396` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1399` | 1,800,000.00 USD | 1,800,000.00 USD | 5,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1400` | 2,270,000.00 USD | 2,270,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1402` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 2,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1404` | 2,250,000.00 USD | 2,250,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 8,880.00 USD | 881,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1411` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1415` | 6,590.00 USD | 872,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1416` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1420` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1423` | 1,790,000.00 USD | 1,790,000.00 USD | 4,030.00 USD | 2,310.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 484,730.00 USD | 866,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1432` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1435` | 1,780,000.00 USD | 1,780,000.00 USD | 3,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 28,290.00 USD | 381,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1436` | 2,220,000.00 USD | 2,220,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1438` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 3,590.00 USD | 20,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1440` | 2,190,000.00 USD | 2,190,000.00 USD | 13,180.00 USD | 5,260.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1441` | 1,750,000.00 USD | 1,750,000.00 USD | 17,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1444` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1444` | 2,160,000.00 USD | 2,160,000.00 USD | 3,450.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 16,220.00 USD | 353,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1452` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 5,660.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1453` | 1,730,000.00 USD | 1,730,000.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 2,110.00 USD | 337,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1456` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1460` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1464` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1465` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 3,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 39,940.00 USD | 335,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1468` | 1,720,000.00 USD | 1,720,000.00 USD | 12,090.00 USD | 2,700.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1468` | 2,120,000.00 USD | 2,120,000.00 USD | 9,720.00 USD | 9,180.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1471` | 1,700,000.00 USD | 1,700,000.00 USD | 4,400.00 USD | 5,970.00 USD | 1,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1472` | 2,090,000.00 USD | 2,090,000.00 USD | 19,180.00 USD | 0.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1474` | 1,690,000.00 USD | 1,690,000.00 USD | 34,610.00 USD | 9,630.00 USD | 67,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 95,530.00 USD | 295,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1476` | 2,060,000.00 USD | 2,060,000.00 USD | 68,180.00 USD | 20,180.00 USD | 81,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1477` | 1,580,000.00 USD | 1,580,000.00 USD | 102,190.00 USD | 16,230.00 USD | 93,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1480` | 1,360,000.00 USD | 1,360,000.00 USD | 64,200.00 USD | 17,450.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1480` | 1,890,000.00 USD | 1,890,000.00 USD | 74,500.00 USD | 43,810.00 USD | 50,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1483` | 1,280,000.00 USD | 1,280,000.00 USD | 17,530.00 USD | 4,230.00 USD | 66,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1484` | 1,720,000.00 USD | 1,720,000.00 USD | 47,020.00 USD | 16,640.00 USD | 115,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 9,220.00 USD | 199,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1486` | 1,190,000.00 USD | 1,190,000.00 USD | 38,460.00 USD | 0.00 USD | 9,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1488` | 1,540,000.00 USD | 1,540,000.00 USD | 48,650.00 USD | 10,470.00 USD | 25,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1489` | 1,140,000.00 USD | 1,140,000.00 USD | 6,740.00 USD | 7,050.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1492` | 1,120,000.00 USD | 1,120,000.00 USD | 24,480.00 USD | 8,610.00 USD | 8,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1492` | 1,460,000.00 USD | 1,460,000.00 USD | 40,320.00 USD | 21,590.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1495` | 1,080,000.00 USD | 1,080,000.00 USD | 18,450.00 USD | 5,270.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 35,480.00 USD | 190,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1496` | 1,360,000.00 USD | 1,360,000.00 USD | 34,650.00 USD | 18,690.00 USD | 17,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1498` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 347.81 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1500` | 1,290,000.00 USD | 1,290,000.00 USD | 60,500.00 USD | 9,610.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1501` | 1,060,000.00 USD | 1,060,000.00 USD | 6,280.00 USD | 0.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1504` | 1,050,000.00 USD | 1,050,000.00 USD | 54,760.00 USD | 15,920.00 USD | 135,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1504` | 1,200,000.00 USD | 1,200,000.00 USD | 20,410.00 USD | 19,520.00 USD | 44,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1505` | 148,730.00 USD | 154,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1507` | 840,730.00 USD | 840,730.00 USD | 93,360.00 USD | 28,420.00 USD | 178,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1508` | 1,110,000.00 USD | 1,110,000.00 USD | 200,530.00 USD | 16,820.00 USD | 256,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1510` | 540,600.00 USD | 540,600.00 USD | 208,430.00 USD | 9,010.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1512` | 638,350.00 USD | 638,350.00 USD | 86,820.00 USD | 13,310.00 USD | 59,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1513` | 321,970.00 USD | 321,970.00 USD | 25,970.00 USD | 5,200.00 USD | 112,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 6,130.00 USD | 6,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1516` | 177,970.00 USD | 177,970.00 USD | 59,890.00 USD | 8,340.00 USD | 17,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1516` | 478,790.00 USD | 478,790.00 USD | 0.00 USD | 13,330.00 USD | 205,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1519` | 92,370.00 USD | 92,370.00 USD | 14,340.00 USD | 2,630.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1520` | 260,340.00 USD | 260,340.00 USD | 47,340.00 USD | 22,090.00 USD | 87,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1522` | 59,100.00 USD | 59,100.00 USD | 38,050.00 USD | 4,440.00 USD | 5,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1524` | 103,860.00 USD | 103,860.00 USD | 0.00 USD | 13,950.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1525` | 10,790.00 USD | 10,790.00 USD | 0.00 USD | 0.00 USD | 1,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1528` | 81,590.00 USD | 81,590.00 USD | 0.00 USD | 33,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1532` | 47,650.00 USD | 47,650.00 USD | 0.00 USD | 17,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1534` | 8,980.00 USD | 8,980.00 USD | 0.00 USD | 8,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1536` | 30,390.00 USD | 30,390.00 USD | 0.00 USD | 8,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1540` | 21,820.00 USD | 21,820.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1544` | 3,590.00 USD | 3,590.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1548` | 2,860.00 USD | 2,860.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1548` | 5,720.00 USD | 5,720.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1549` | 17,000.00 USD | 17,000.00 USD | 0.00 USD | 17,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1552` | 19,510.00 USD | 19,510.00 USD | 0.00 USD | 2,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1552` | 17,540.00 USD | 17,540.00 USD | 0.00 USD | 11,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1560` | 28,520.00 USD | 28,520.00 USD | 0.00 USD | 10,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1561` | 24,480.00 USD | 24,480.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1564` | 286,390.00 USD | 286,390.00 USD | 3,130.00 USD | 13,270.00 USD | 245,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1564` | 62,280.00 USD | 62,280.00 USD | 0.00 USD | 33,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1567` | 411,380.00 USD | 411,380.00 USD | 72,650.00 USD | 32,420.00 USD | 19,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1568` | 340,960.00 USD | 340,960.00 USD | 111,700.00 USD | 15,360.00 USD | 151,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1570` | 604,120.00 USD | 604,120.00 USD | 0.00 USD | 12,360.00 USD | 180,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1572` | 674,760.00 USD | 674,760.00 USD | 235,420.00 USD | 39,540.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1573` | 624,430.00 USD | 624,430.00 USD | 20,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1576` | 760,620.00 USD | 760,620.00 USD | 25,970.00 USD | 0.00 USD | 110,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1576` | 987,120.00 USD | 987,120.00 USD | 44,680.00 USD | 123,840.00 USD | 143,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1579` | 810,440.00 USD | 810,440.00 USD | 49,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1580` | 1,270,000.00 USD | 1,270,000.00 USD | 177,280.00 USD | 101,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1584` | 1,390,000.00 USD | 1,390,000.00 USD | 80,450.00 USD | 43,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1585` | 849,670.00 USD | 849,670.00 USD | 28,600.00 USD | 2,370.00 USD | 8,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1588` | 909,240.00 USD | 909,240.00 USD | 15,100.00 USD | 28,750.00 USD | 15,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1588` | 1,500,000.00 USD | 1,500,000.00 USD | 69,180.00 USD | 44,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1591` | 962,750.00 USD | 962,750.00 USD | 0.00 USD | 26,120.00 USD | 27,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1592` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 64,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1594` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 39,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1596` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 98,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1597` | 1,020,000.00 USD | 1,020,000.00 USD | 16,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1600` | 1,100,000.00 USD | 1,100,000.00 USD | 20,040.00 USD | 0.00 USD | 57,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1600` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 60,710.00 USD | 75,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1603` | 1,170,000.00 USD | 1,170,000.00 USD | 74,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1604` | 2,380,000.00 USD | 2,380,000.00 USD | 188,060.00 USD | 112,090.00 USD | 273,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1605` | 2,500.00 USD | 2,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1606` | 1,250,000.00 USD | 1,250,000.00 USD | 27,640.00 USD | 0.00 USD | 55,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1608` | 3,070,000.00 USD | 3,070,000.00 USD | 208,080.00 USD | 240,680.00 USD | 243,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1609` | 1,310,000.00 USD | 1,310,000.00 USD | 24,910.00 USD | 0.00 USD | 34,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1612` | 1,440,000.00 USD | 1,440,000.00 USD | 20,140.00 USD | 11,530.00 USD | 94,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1612` | 4,010,000.00 USD | 4,010,000.00 USD | 328,640.00 USD | 328,050.00 USD | 287,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1615` | 1,460,000.00 USD | 1,460,000.00 USD | 14,300.00 USD | 0.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1616` | 4,550,000.00 USD | 4,550,000.00 USD | 293,210.00 USD | 131,180.00 USD | 108,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1618` | 1,530,000.00 USD | 1,530,000.00 USD | 53,600.00 USD | 12,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1620` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 196,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1621` | 1,700,000.00 USD | 1,700,000.00 USD | 92,470.00 USD | 73,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1624` | 1,810,000.00 USD | 1,810,000.00 USD | 50,280.00 USD | 59,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1624` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 193,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1627` | 1,830,000.00 USD | 1,830,000.00 USD | 25,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1628` | 5,120,000.00 USD | 5,120,000.00 USD | 76,780.00 USD | 0.00 USD | 103,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1630` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 17,970.00 USD | 101,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1633` | 2,060,000.00 USD | 2,060,000.00 USD | 98,410.00 USD | 6,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1635` | 380.25 USD | 2,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1636` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 19,990.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1636` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 13,670.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1639` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 13,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1640` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1642` | 2,170,000.00 USD | 2,170,000.00 USD | 19,180.00 USD | 36,980.00 USD | 16,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1644` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 8,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1645` | 2,200,000.00 USD | 2,200,000.00 USD | 14,950.00 USD | 11,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1645` | 2,480.00 USD | 5,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1648` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1654` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1655` | 909.51 USD | 6,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1656` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 31,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1657` | 2,270,000.00 USD | 2,270,000.00 USD | 9,730.00 USD | 55,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1660` | 2,340,000.00 USD | 2,340,000.00 USD | 8,220.00 USD | 11,150.00 USD | 50,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1660` | 5,370,000.00 USD | 5,370,000.00 USD | 79,170.00 USD | 11,020.00 USD | 51,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1663` | 2,440,000.00 USD | 2,440,000.00 USD | 44,200.00 USD | 14,550.00 USD | 44,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1664` | 5,630,000.00 USD | 5,630,000.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1665` | 26,250.00 USD | 32,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1666` | 2,550,000.00 USD | 2,550,000.00 USD | 22,170.00 USD | 5,340.00 USD | 78,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1668` | 5,810,000.00 USD | 5,810,000.00 USD | 42,580.00 USD | 52,290.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1672` | 2,600,000.00 USD | 2,600,000.00 USD | 46,590.00 USD | 2,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1672` | 6,010,000.00 USD | 6,010,000.00 USD | 135,250.00 USD | 62,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1675` | 2,640,000.00 USD | 2,640,000.00 USD | 20,040.00 USD | 1,990.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1675` | 636.75 USD | 33,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1676` | 6,230,000.00 USD | 6,230,000.00 USD | 84,020.00 USD | 141,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1678` | 2,660,000.00 USD | 2,660,000.00 USD | 22,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1680` | 6,450,000.00 USD | 6,450,000.00 USD | 121,860.00 USD | 80,270.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1681` | 2,790,000.00 USD | 2,790,000.00 USD | 120,850.00 USD | 4,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1684` | 2,900,000.00 USD | 2,900,000.00 USD | 54,020.00 USD | 26,600.00 USD | 32,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1684` | 6,530,000.00 USD | 6,530,000.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1687` | 2,950,000.00 USD | 2,950,000.00 USD | 6,560.00 USD | 5,840.00 USD | 39,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1688` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1690` | 3,000,000.00 USD | 3,000,000.00 USD | 25,050.00 USD | 9,870.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1692` | 6,720,000.00 USD | 6,720,000.00 USD | 33,660.00 USD | 70,740.00 USD | 71,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1693` | 3,190,000.00 USD | 3,190,000.00 USD | 84,630.00 USD | 74,940.00 USD | 35,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1696` | 3,240,000.00 USD | 3,240,000.00 USD | 23,530.00 USD | 16,310.00 USD | 6,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1696` | 6,860,000.00 USD | 6,860,000.00 USD | 17,360.00 USD | 87,350.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1699` | 3,350,000.00 USD | 3,350,000.00 USD | 26,000.00 USD | 56,690.00 USD | 22,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1700` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 25,330.00 USD | 69,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1702` | 3,370,000.00 USD | 3,370,000.00 USD | 9,960.00 USD | 0.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1704` | 7,060,000.00 USD | 7,060,000.00 USD | 55,170.00 USD | 46,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1705` | 3,400,000.00 USD | 3,400,000.00 USD | 14,190.00 USD | 20,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1705` | 8,020.00 USD | 41,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1708` | 3,520,000.00 USD | 3,520,000.00 USD | 39,520.00 USD | 65,470.00 USD | 13,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1708` | 7,150,000.00 USD | 7,150,000.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1711` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 4,910.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1714` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 12,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1716` | 7,210,000.00 USD | 7,210,000.00 USD | 0.00 USD | 42,020.00 USD | 15,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1717` | 3,610,000.00 USD | 3,610,000.00 USD | 9,570.00 USD | 34,120.00 USD | 19,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1720` | 3,700,000.00 USD | 3,700,000.00 USD | 80,090.00 USD | 1,590.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1720` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 161,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1723` | 3,830,000.00 USD | 3,830,000.00 USD | 54,130.00 USD | 16,860.00 USD | 66,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1724` | 7,690,000.00 USD | 7,690,000.00 USD | 118,060.00 USD | 0.00 USD | 208,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1726` | 3,860,000.00 USD | 3,860,000.00 USD | 8,230.00 USD | 2,410.00 USD | 12,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1729` | 3,870,000.00 USD | 3,870,000.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1732` | 3,890,000.00 USD | 3,890,000.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1732` | 8,180,000.00 USD | 8,180,000.00 USD | 476,430.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1735` | 3,920,000.00 USD | 3,920,000.00 USD | 14,970.00 USD | 9,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1738` | 3,940,000.00 USD | 3,940,000.00 USD | 18,610.00 USD | 2,310.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1740` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 0.00 USD | 83,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1741` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 1,600.00 USD | 5,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1744` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 2,460.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1744` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1745` | 14,600.00 USD | 55,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1747` | 4,010,000.00 USD | 4,010,000.00 USD | 8,530.00 USD | 0.00 USD | 31,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1748` | 8,360,000.00 USD | 8,360,000.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1750` | 4,110,000.00 USD | 4,110,000.00 USD | 80,070.00 USD | 2,280.00 USD | 22,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1752` | 8,650,000.00 USD | 8,650,000.00 USD | 0.00 USD | 0.00 USD | 291,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1753` | 4,180,000.00 USD | 4,180,000.00 USD | 32,240.00 USD | 0.00 USD | 33,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1756` | 4,300,000.00 USD | 4,300,000.00 USD | 23,610.00 USD | 27,640.00 USD | 73,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1756` | 8,950,000.00 USD | 8,950,000.00 USD | 112,930.00 USD | 0.00 USD | 186,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1759` | 4,460,000.00 USD | 4,460,000.00 USD | 85,450.00 USD | 31,960.00 USD | 36,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1760` | 9,320,000.00 USD | 9,320,000.00 USD | 268,160.00 USD | 71,260.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1762` | 4,680,000.00 USD | 4,680,000.00 USD | 72,450.00 USD | 83,100.00 USD | 66,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1764` | 9,990,000.00 USD | 9,990,000.00 USD | 353,950.00 USD | 270,450.00 USD | 40,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1765` | 4,770,000.00 USD | 4,770,000.00 USD | 20,220.00 USD | 28,990.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1765` | 3,900.00 USD | 59,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1768` | 4,940,000.00 USD | 4,940,000.00 USD | 19,860.00 USD | 83,210.00 USD | 62,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1768` | 10,370,000.00 USD | 10,370,000.00 USD | 191,690.00 USD | 154,100.00 USD | 31,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1771` | 5,020,000.00 USD | 5,020,000.00 USD | 43,430.00 USD | 19,520.00 USD | 24,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1772` | 10,640,000.00 USD | 10,640,000.00 USD | 98,390.00 USD | 153,480.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1774` | 5,100,000.00 USD | 5,100,000.00 USD | 20,200.00 USD | 30,630.00 USD | 26,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1776` | 10,890,000.00 USD | 10,890,000.00 USD | 186,770.00 USD | 59,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1777` | 5,250,000.00 USD | 5,250,000.00 USD | 42,080.00 USD | 81,500.00 USD | 24,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1780` | 5,280,000.00 USD | 5,280,000.00 USD | 11,580.00 USD | 9,760.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1780` | 11,140,000.00 USD | 11,140,000.00 USD | 52,730.00 USD | 46,410.00 USD | 157,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1783` | 5,340,000.00 USD | 5,340,000.00 USD | 27,640.00 USD | 15,680.00 USD | 19,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1784` | 11,370,000.00 USD | 11,370,000.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1786` | 5,400,000.00 USD | 5,400,000.00 USD | 16,960.00 USD | 31,510.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1788` | 11,540,000.00 USD | 11,540,000.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1789` | 5,450,000.00 USD | 5,450,000.00 USD | 15,890.00 USD | 31,190.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1792` | 5,500,000.00 USD | 5,500,000.00 USD | 13,950.00 USD | 16,470.00 USD | 18,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1792` | 11,770,000.00 USD | 11,770,000.00 USD | 182,810.00 USD | 46,960.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1795` | 5,620,000.00 USD | 5,620,000.00 USD | 53,160.00 USD | 43,180.00 USD | 18,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1796` | 11,860,000.00 USD | 11,860,000.00 USD | 17,130.00 USD | 26,110.00 USD | 44,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1798` | 5,670,000.00 USD | 5,670,000.00 USD | 15,420.00 USD | 17,120.00 USD | 21,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1800` | 11,980,000.00 USD | 11,980,000.00 USD | 12,940.00 USD | 34,680.00 USD | 73,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1801` | 5,720,000.00 USD | 5,720,000.00 USD | 12,470.00 USD | 23,820.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1804` | 5,770,000.00 USD | 5,770,000.00 USD | 10,530.00 USD | 16,830.00 USD | 19,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1804` | 12,070,000.00 USD | 12,070,000.00 USD | 35,280.00 USD | 32,850.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1807` | 5,810,000.00 USD | 5,810,000.00 USD | 16,640.00 USD | 17,460.00 USD | 9,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1808` | 12,250,000.00 USD | 12,250,000.00 USD | 35,050.00 USD | 67,250.00 USD | 73,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1810` | 5,850,000.00 USD | 5,850,000.00 USD | 12,880.00 USD | 15,840.00 USD | 8,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1812` | 12,390,000.00 USD | 12,390,000.00 USD | 64,990.00 USD | 29,900.00 USD | 50,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1813` | 5,920,000.00 USD | 5,920,000.00 USD | 14,660.00 USD | 37,850.00 USD | 15,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1816` | 5,940,000.00 USD | 5,940,000.00 USD | 13,550.00 USD | 0.00 USD | 12,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1816` | 12,530,000.00 USD | 12,530,000.00 USD | 69,700.00 USD | 33,940.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1819` | 5,970,000.00 USD | 5,970,000.00 USD | 6,740.00 USD | 12,120.00 USD | 6,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1820` | 12,700,000.00 USD | 12,700,000.00 USD | 65,350.00 USD | 54,880.00 USD | 43,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1822` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 21,610.00 USD | 1,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1824` | 12,910,000.00 USD | 12,910,000.00 USD | 80,350.00 USD | 17,880.00 USD | 112,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1825` | 6,020,000.00 USD | 6,020,000.00 USD | 18,910.00 USD | 1,780.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1828` | 6,030,000.00 USD | 6,030,000.00 USD | 6,840.00 USD | 5,270.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1828` | 13,090,000.00 USD | 13,090,000.00 USD | 79,610.00 USD | 29,630.00 USD | 69,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1832` | 13,300,000.00 USD | 13,300,000.00 USD | 108,540.00 USD | 31,590.00 USD | 74,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1834` | 6,040,000.00 USD | 6,040,000.00 USD | 2,670.00 USD | 0.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1835` | 748.51 USD | 60,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1836` | 13,640,000.00 USD | 13,640,000.00 USD | 172,660.00 USD | 110,870.00 USD | 52,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1837` | 6,050,000.00 USD | 6,050,000.00 USD | 3,610.00 USD | 2,640.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1840` | 6,070,000.00 USD | 6,070,000.00 USD | 5,430.00 USD | 1,970.00 USD | 12,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1840` | 13,980,000.00 USD | 13,980,000.00 USD | 141,620.00 USD | 50,840.00 USD | 151,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1843` | 6,070,000.00 USD | 6,070,000.00 USD | 1,030.00 USD | 3,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1844` | 14,190,000.00 USD | 14,190,000.00 USD | 94,510.00 USD | 20,390.00 USD | 97,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1845` | 777.21 USD | 61,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1848` | 14,340,000.00 USD | 14,340,000.00 USD | 35,280.00 USD | 69,910.00 USD | 41,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1852` | 14,790,000.00 USD | 14,790,000.00 USD | 168,270.00 USD | 28,290.00 USD | 251,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1856` | 15,030,000.00 USD | 15,030,000.00 USD | 100,160.00 USD | 21,030.00 USD | 120,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1860` | 15,270,000.00 USD | 15,270,000.00 USD | 64,600.00 USD | 48,330.00 USD | 127,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1864` | 15,430,000.00 USD | 15,430,000.00 USD | 48,260.00 USD | 44,140.00 USD | 61,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1868` | 15,670,000.00 USD | 15,670,000.00 USD | 133,990.00 USD | 51,510.00 USD | 56,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1872` | 16,130,000.00 USD | 16,130,000.00 USD | 169,490.00 USD | 133,380.00 USD | 155,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1876` | 16,260,000.00 USD | 16,260,000.00 USD | 65,910.00 USD | 23,180.00 USD | 43,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1880` | 16,380,000.00 USD | 16,380,000.00 USD | 57,250.00 USD | 35,940.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1884` | 16,440,000.00 USD | 16,440,000.00 USD | 14,000.00 USD | 35,430.00 USD | 9,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1888` | 16,560,000.00 USD | 16,560,000.00 USD | 22,970.00 USD | 4,800.00 USD | 88,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1892` | 16,650,000.00 USD | 16,650,000.00 USD | 49,980.00 USD | 2,860.00 USD | 34,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1896` | 16,720,000.00 USD | 16,720,000.00 USD | 42,320.00 USD | 11,820.00 USD | 18,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1900` | 16,770,000.00 USD | 16,770,000.00 USD | 0.00 USD | 29,650.00 USD | 20,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1904` | 16,810,000.00 USD | 16,810,000.00 USD | 14,330.00 USD | 17,690.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1908` | 16,930,000.00 USD | 16,930,000.00 USD | 24,190.00 USD | 37,870.00 USD | 52,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1912` | 16,950,000.00 USD | 16,950,000.00 USD | 0.00 USD | 9,380.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1916` | 16,980,000.00 USD | 16,980,000.00 USD | 7,460.00 USD | 12,040.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1920` | 16,980,000.00 USD | 16,980,000.00 USD | 0.00 USD | 5,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1924` | 17,000,000.00 USD | 17,000,000.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1928` | 17,020,000.00 USD | 17,020,000.00 USD | 11,600.00 USD | 7,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1944` | 17,030,000.00 USD | 17,030,000.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1945` | 623.68 USD | 61,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1952` | 17,040,000.00 USD | 17,040,000.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1955` | 860.20 USD | 62,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1956` | 17,050,000.00 USD | 17,050,000.00 USD | 4,860.00 USD | 2,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1960` | 17,050,000.00 USD | 17,050,000.00 USD | 5,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1964` | 17,070,000.00 USD | 17,070,000.00 USD | 6,470.00 USD | 2,700.00 USD | 10,990.00 USD | `Tier 1 CEX` |
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
| `Sell Stop` | `0.0355` | 576,130.00 USD | 0.00 USD | 355.00 USD | `-77.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 575,770.00 USD | 0.00 USD | 3,510.00 USD | `-72.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 572,260.00 USD | 0.00 USD | 6,830.00 USD | `-67.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 565,430.00 USD | 0.00 USD | 4,310.00 USD | `-64.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 561,120.00 USD | 0.00 USD | 475.11 USD | `-59.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 560,640.00 USD | 0.00 USD | 131.16 USD | `-57.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 560,510.00 USD | 0.00 USD | 881.45 USD | `-57.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 559,630.00 USD | 0.00 USD | 1,070.00 USD | `-56.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 558,560.00 USD | 0.00 USD | 1,400.00 USD | `-56.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 557,160.00 USD | 0.00 USD | 1,010.00 USD | `-55.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 556,150.00 USD | 0.00 USD | 4,100.00 USD | `-54.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 552,050.00 USD | 0.00 USD | 529.04 USD | `-54.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 551,520.00 USD | 0.00 USD | 2,390.00 USD | `-53.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 549,130.00 USD | 0.00 USD | 757.39 USD | `-51.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 548,370.00 USD | 0.00 USD | 1,490.00 USD | `-49.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 546,890.00 USD | 0.00 USD | 277.37 USD | `-44.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 546,610.00 USD | 0.00 USD | 262.50 USD | `-43.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 546,350.00 USD | 0.00 USD | 795.57 USD | `-43.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 545,550.00 USD | 0.00 USD | 181.00 USD | `-41.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 545,370.00 USD | 0.00 USD | 798.65 USD | `-35.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 544,570.00 USD | 0.00 USD | 1,550.00 USD | `-34.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 543,020.00 USD | 0.00 USD | 116.07 USD | `-30.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 542,910.00 USD | 0.00 USD | 19,070.00 USD | `-30.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 523,840.00 USD | 0.00 USD | 577.22 USD | `-29.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 523,260.00 USD | 0.00 USD | 343.50 USD | `-26.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 522,920.00 USD | 0.00 USD | 26,280.00 USD | `-25.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1175` | 496,640.00 USD | 0.00 USD | 105.75 USD | `-24.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 496,530.00 USD | 0.00 USD | 120.50 USD | `-22.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 496,410.00 USD | 0.00 USD | 83,620.00 USD | `-21.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 412,780.00 USD | 0.00 USD | 14,940.00 USD | `-20.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 397,850.00 USD | 0.00 USD | 2,670.00 USD | `-18.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 395,180.00 USD | 0.00 USD | 473.27 USD | `-18.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 394,710.00 USD | 0.00 USD | 216,060.00 USD | `-17.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 178,650.00 USD | 0.00 USD | 23,890.00 USD | `-16.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1315` | 154,760.00 USD | 0.00 USD | 1,590.00 USD | `-15.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 153,170.00 USD | 0.00 USD | 5,560.00 USD | `-14.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 147,600.00 USD | 0.00 USD | 625.78 USD | `-14.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 146,980.00 USD | 0.00 USD | 502.28 USD | `-13.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 146,480.00 USD | 0.00 USD | 3,350.00 USD | `-13.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 143,130.00 USD | 0.00 USD | 700.86 USD | `-12.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 142,430.00 USD | 0.00 USD | 1,070.00 USD | `-11.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 141,360.00 USD | 0.00 USD | 108.57 USD | `-11.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 141,250.00 USD | 0.00 USD | 349.74 USD | `-10.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 140,900.00 USD | 0.00 USD | 4,940.00 USD | `-9.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 135,970.00 USD | 0.00 USD | 127.35 USD | `-9.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 135,840.00 USD | 0.00 USD | 32,670.00 USD | `-8.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 103,170.00 USD | 0.00 USD | 2,820.00 USD | `-7.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 100,360.00 USD | 0.00 USD | 23,330.00 USD | `-7.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 77,020.00 USD | 0.00 USD | 27,670.00 USD | `-6.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 49,350.00 USD | 0.00 USD | 21,580.00 USD | `-5.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 27,770.00 USD | 0.00 USD | 9,940.00 USD | `-5.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 17,830.00 USD | 0.00 USD | 2,340.00 USD | `-4.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 15,490.00 USD | 0.00 USD | 2,090.00 USD | `-4.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 13,410.00 USD | 0.00 USD | 6,750.00 USD | `-3.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 6,660.00 USD | 0.00 USD | 490.33 USD | `-2.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 6,170.00 USD | 0.00 USD | 195.54 USD | `-2.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1535` | 5,970.00 USD | 0.00 USD | 204.57 USD | `-1.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 5,770.00 USD | 0.00 USD | 213.35 USD | `-0.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 5,560.00 USD | 0.00 USD | 5,560.00 USD | `-0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 150.19 USD | 150.19 USD | 0.00 USD | `+0.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 441.27 USD | 291.08 USD | 0.00 USD | `+1.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1585` | 4,480.00 USD | 4,040.00 USD | 0.00 USD | `+1.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1595` | 5,570.00 USD | 1,090.00 USD | 0.00 USD | `+2.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1605` | 58,560.00 USD | 52,990.00 USD | 0.00 USD | `+3.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1615` | 59,930.00 USD | 1,380.00 USD | 0.00 USD | `+3.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1625` | 61,330.00 USD | 1,400.00 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 61,640.00 USD | 308.10 USD | 0.00 USD | `+4.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1645` | 66,090.00 USD | 4,450.00 USD | 0.00 USD | `+5.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1655` | 67,150.00 USD | 1,060.00 USD | 0.00 USD | `+6.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1665` | 78,320.00 USD | 11,170.00 USD | 0.00 USD | `+6.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1675` | 78,450.00 USD | 130.26 USD | 0.00 USD | `+7.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1685` | 79,600.00 USD | 1,150.00 USD | 0.00 USD | `+8.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 79,920.00 USD | 317.95 USD | 0.00 USD | `+8.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 83,350.00 USD | 3,430.00 USD | 0.00 USD | `+9.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 85,150.00 USD | 1,800.00 USD | 0.00 USD | `+10.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 85,380.00 USD | 229.89 USD | 0.00 USD | `+10.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 94,220.00 USD | 8,840.00 USD | 0.00 USD | `+11.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 100,860.00 USD | 6,650.00 USD | 0.00 USD | `+12.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 102,220.00 USD | 1,350.00 USD | 0.00 USD | `+12.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 102,660.00 USD | 439.36 USD | 0.00 USD | `+13.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 102,990.00 USD | 336.40 USD | 0.00 USD | `+13.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 103,890.00 USD | 898.02 USD | 0.00 USD | `+14.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 130,280.00 USD | 26,390.00 USD | 0.00 USD | `+15.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 131,560.00 USD | 1,280.00 USD | 0.00 USD | `+15.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 141,800.00 USD | 10,240.00 USD | 0.00 USD | `+16.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 142,670.00 USD | 864.12 USD | 0.00 USD | `+17.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 145,190.00 USD | 2,520.00 USD | 0.00 USD | `+17.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 145,470.00 USD | 276.75 USD | 0.00 USD | `+18.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 145,620.00 USD | 149.79 USD | 0.00 USD | `+19.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 148,810.00 USD | 3,190.00 USD | 0.00 USD | `+19.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 148,950.00 USD | 147.11 USD | 0.00 USD | `+20.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 149,200.00 USD | 245.50 USD | 0.00 USD | `+21.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 149,860.00 USD | 660.73 USD | 0.00 USD | `+21.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 157,460.00 USD | 7,600.00 USD | 0.00 USD | `+22.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 157,860.00 USD | 396.42 USD | 0.00 USD | `+22.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 186,880.00 USD | 29,020.00 USD | 0.00 USD | `+23.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 193,950.00 USD | 7,070.00 USD | 0.00 USD | `+24.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 197,480.00 USD | 3,530.00 USD | 0.00 USD | `+24.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 197,620.00 USD | 137.77 USD | 0.00 USD | `+25.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 197,750.00 USD | 133.19 USD | 0.00 USD | `+26.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 197,890.00 USD | 134.20 USD | 0.00 USD | `+26.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 201,770.00 USD | 3,880.00 USD | 0.00 USD | `+27.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 202,260.00 USD | 492.19 USD | 0.00 USD | `+28.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 225,170.00 USD | 22,900.00 USD | 0.00 USD | `+28.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 226,030.00 USD | 863.97 USD | 0.00 USD | `+29.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 247,370.00 USD | 21,340.00 USD | 0.00 USD | `+30.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 247,550.00 USD | 182.72 USD | 0.00 USD | `+30.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 333,450.00 USD | 85,900.00 USD | 0.00 USD | `+31.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 334,920.00 USD | 1,470.00 USD | 0.00 USD | `+31.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 335,090.00 USD | 174.20 USD | 0.00 USD | `+32.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 337,170.00 USD | 2,080.00 USD | 0.00 USD | `+33.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 337,420.00 USD | 252.51 USD | 0.00 USD | `+34.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 339,790.00 USD | 2,370.00 USD | 0.00 USD | `+35.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 339,910.00 USD | 126.50 USD | 0.00 USD | `+35.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 340,100.00 USD | 190.80 USD | 0.00 USD | `+36.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 340,820.00 USD | 713.94 USD | 0.00 USD | `+37.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 341,030.00 USD | 213.00 USD | 0.00 USD | `+38.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 347,310.00 USD | 6,280.00 USD | 0.00 USD | `+40.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 347,680.00 USD | 368.47 USD | 0.00 USD | `+40.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 370,170.00 USD | 22,490.00 USD | 0.00 USD | `+41.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 370,500.00 USD | 333.91 USD | 0.00 USD | `+42.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 374,480.00 USD | 3,980.00 USD | 0.00 USD | `+43.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 374,860.00 USD | 378.55 USD | 0.00 USD | `+44.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 375,240.00 USD | 380.23 USD | 0.00 USD | `+45.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 375,420.00 USD | 185.87 USD | 0.00 USD | `+46.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 375,620.00 USD | 192.69 USD | 0.00 USD | `+46.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2295` | 375,800.00 USD | 187.50 USD | 0.00 USD | `+47.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 420,450.00 USD | 44,650.00 USD | 0.00 USD | `+48.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 420,640.00 USD | 189.14 USD | 0.00 USD | `+48.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 424,900.00 USD | 4,260.00 USD | 0.00 USD | `+49.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 426,420.00 USD | 1,520.00 USD | 0.00 USD | `+49.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 447,650.00 USD | 21,230.00 USD | 0.00 USD | `+52.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 450,170.00 USD | 2,530.00 USD | 0.00 USD | `+53.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 450,370.00 USD | 195.67 USD | 0.00 USD | `+53.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 472,070.00 USD | 21,700.00 USD | 0.00 USD | `+54.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 481,380.00 USD | 9,300.00 USD | 0.00 USD | `+55.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 687,250.00 USD | 205,870.00 USD | 0.00 USD | `+57.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 706,000.00 USD | 18,750.00 USD | 0.00 USD | `+58.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 706,550.00 USD | 551.23 USD | 0.00 USD | `+58.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 706,950.00 USD | 397.90 USD | 0.00 USD | `+60.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 711,280.00 USD | 4,330.00 USD | 0.00 USD | `+60.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 711,570.00 USD | 289.23 USD | 0.00 USD | `+61.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 716,580.00 USD | 5,010.00 USD | 0.00 USD | `+62.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 732,460.00 USD | 15,880.00 USD | 0.00 USD | `+62.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 734,240.00 USD | 1,780.00 USD | 0.00 USD | `+63.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 736,790.00 USD | 2,550.00 USD | 0.00 USD | `+64.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 748,520.00 USD | 11,730.00 USD | 0.00 USD | `+64.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 753,680.00 USD | 5,160.00 USD | 0.00 USD | `+65.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 770,550.00 USD | 16,870.00 USD | 0.00 USD | `+66.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 799,680.00 USD | 29,130.00 USD | 0.00 USD | `+67.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2655` | 879,470.00 USD | 79,780.00 USD | 0.00 USD | `+70.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 879,740.00 USD | 272.88 USD | 0.00 USD | `+73.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 880,130.00 USD | 394.01 USD | 0.00 USD | `+77.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 880,510.00 USD | 375.53 USD | 0.00 USD | `+80.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 882,640.00 USD | 2,130.00 USD | 0.00 USD | `+83.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 883,220.00 USD | 579.27 USD | 0.00 USD | `+83.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 884,970.00 USD | 1,750.00 USD | 0.00 USD | `+86.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 885,070.00 USD | 101.21 USD | 0.00 USD | `+89.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 885,340.00 USD | 262.73 USD | 0.00 USD | `+90.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 886,780.00 USD | 1,440.00 USD | 0.00 USD | `+91.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 892,940.00 USD | 6,160.00 USD | 0.00 USD | `+92.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 898,360.00 USD | 5,430.00 USD | 0.00 USD | `+93.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 898,650.00 USD | 289.61 USD | 0.00 USD | `+96.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3065` | 899,140.00 USD | 487.09 USD | 0.00 USD | `+96.80%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1336` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 3,580.00 USD | 5,990.00 USD | 16,000.00 USD |
| `7D` | `0.1340` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 9,160.00 USD | 7,730.00 USD | 28,910.00 USD |
| `7D` | `0.1344` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 6,410.00 USD | 5,790.00 USD | 19,420.00 USD |
| `1D` | `0.1345` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 0.00 USD | 691.54 USD | 598.60 USD |
| `1D` | `0.1348` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 2,170.00 USD |
| `7D` | `0.1348` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 31,170.00 USD | 7,150.00 USD | 23,510.00 USD |
| `1D` | `0.1351` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 6,820.00 USD | 2,050.00 USD | 5,870.00 USD |
| `7D` | `0.1352` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 11,390.00 USD | 6,290.00 USD | 24,710.00 USD |
| `1D` | `0.1354` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 2,670.00 USD | 688.99 USD | 4,320.00 USD |
| `7D` | `0.1356` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 16,150.00 USD | 12,180.00 USD | 9,380.00 USD |
| `1D` | `0.1357` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 2,570.00 USD |
| `1D` | `0.1360` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 2,480.00 USD | 869.31 USD | 4,370.00 USD |
| `7D` | `0.1360` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 25,240.00 USD | 8,630.00 USD | 8,770.00 USD |
| `1D` | `0.1363` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 4,890.00 USD | 2,360.00 USD | 2,720.00 USD |
| `7D` | `0.1364` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD |
| `1D` | `0.1366` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 1,340.00 USD | 484.70 USD | 0.00 USD |
| `7D` | `0.1368` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 4,500.00 USD | 7,610.00 USD | 2,530.00 USD |
| `1D` | `0.1369` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD |
| `1D` | `0.1372` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 5,470.00 USD | 1,110.00 USD | 2,240.00 USD |
| `7D` | `0.1372` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1375` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 0.00 USD | 2,220.00 USD | 0.00 USD |
| `1D` | `0.1378` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 936.88 USD | 1,590.00 USD | 1,550.00 USD |
| `7D` | `0.1380` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD |
| `1D` | `0.1381` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 5,890.00 USD | 7,190.00 USD | 27,690.00 USD |
| `1D` | `0.1384` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 17,120.00 USD | 2,890.00 USD | 38,400.00 USD |
| `7D` | `0.1384` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 11,880.00 USD | 0.00 USD | 30,320.00 USD |
| `1D` | `0.1387` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 33,240.00 USD | 2,090.00 USD | 2,250.00 USD |
| `7D` | `0.1388` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD |
| `1D` | `0.1390` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 5,190.00 USD | 1,970.00 USD | 23,070.00 USD |
| `7D` | `0.1392` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 0.00 USD | 4,690.00 USD | 28,770.00 USD |
| `1D` | `0.1393` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 9,960.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1396` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 0.00 USD | 6,230.00 USD | 0.00 USD |
| `7D` | `0.1396` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD |
| `1D` | `0.1399` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 5,720.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1400` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD |
| `1D` | `0.1402` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 0.00 USD | 2,100.00 USD | 0.00 USD |
| `7D` | `0.1404` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1411` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD |
| `7D` | `0.1416` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD |
| `7D` | `0.1420` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD |
| `1D` | `0.1423` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 4,030.00 USD | 2,310.00 USD | 6,410.00 USD |
| `7D` | `0.1432` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 10,760.00 USD |
| `1D` | `0.1435` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 3,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1436` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD |
| `1D` | `0.1438` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | 3,590.00 USD | 20,320.00 USD |
| `7D` | `0.1440` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 13,180.00 USD | 5,260.00 USD | 3,610.00 USD |
| `1D` | `0.1441` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 17,680.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1444` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD |
| `7D` | `0.1444` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 3,450.00 USD | 0.00 USD | 6,160.00 USD |
| `7D` | `0.1452` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 0.00 USD | 5,660.00 USD | 14,180.00 USD |
| `1D` | `0.1453` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1456` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD |
| `7D` | `0.1460` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD |
| `7D` | `0.1464` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD |
| `1D` | `0.1465` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 3,590.00 USD |
| `1D` | `0.1468` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 12,090.00 USD | 2,700.00 USD | 8,060.00 USD |
| `7D` | `0.1468` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 9,720.00 USD | 9,180.00 USD | 8,720.00 USD |
| `1D` | `0.1471` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 4,400.00 USD | 5,970.00 USD | 1,210.00 USD |
| `7D` | `0.1472` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 19,180.00 USD | 0.00 USD | 14,170.00 USD |
| `1D` | `0.1474` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 34,610.00 USD | 9,630.00 USD | 67,450.00 USD |
| `7D` | `0.1476` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 68,180.00 USD | 20,180.00 USD | 81,130.00 USD |
| `1D` | `0.1477` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 102,190.00 USD | 16,230.00 USD | 93,440.00 USD |
| `1D` | `0.1480` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 64,200.00 USD | 17,450.00 USD | 5,190.00 USD |
| `7D` | `0.1480` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 74,500.00 USD | 43,810.00 USD | 50,250.00 USD |
| `1D` | `0.1483` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 17,530.00 USD | 4,230.00 USD | 66,200.00 USD |
| `7D` | `0.1484` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 47,020.00 USD | 16,640.00 USD | 115,360.00 USD |
| `1D` | `0.1486` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 38,460.00 USD | 0.00 USD | 9,060.00 USD |
| `7D` | `0.1488` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 48,650.00 USD | 10,470.00 USD | 25,980.00 USD |
| `1D` | `0.1489` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 6,740.00 USD | 7,050.00 USD | 4,950.00 USD |
| `1D` | `0.1492` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 24,480.00 USD | 8,610.00 USD | 8,400.00 USD |
| `7D` | `0.1492` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 40,320.00 USD | 21,590.00 USD | 35,230.00 USD |
| `1D` | `0.1495` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 18,450.00 USD | 5,270.00 USD | 2,180.00 USD |
| `7D` | `0.1496` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 34,650.00 USD | 18,690.00 USD | 17,090.00 USD |
| `1D` | `0.1498` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 347.81 USD |
| `7D` | `0.1500` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 60,500.00 USD | 9,610.00 USD | 21,940.00 USD |
| `1D` | `0.1501` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 6,280.00 USD | 0.00 USD | 3,370.00 USD |
| `1D` | `0.1504` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 54,760.00 USD | 15,920.00 USD | 135,080.00 USD |
| `7D` | `0.1504` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 20,410.00 USD | 19,520.00 USD | 44,850.00 USD |
| `1D` | `0.1507` | 840,730.00 USD | 0.00 USD | 840,730.00 USD | 93,360.00 USD | 28,420.00 USD | 178,360.00 USD |
| `7D` | `0.1508` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 200,530.00 USD | 16,820.00 USD | 256,150.00 USD |
| `1D` | `0.1510` | 540,600.00 USD | 0.00 USD | 540,600.00 USD | 208,430.00 USD | 9,010.00 USD | 1,200.00 USD |
| `7D` | `0.1512` | 638,350.00 USD | 0.00 USD | 638,350.00 USD | 86,820.00 USD | 13,310.00 USD | 59,430.00 USD |
| `1D` | `0.1513` | 321,970.00 USD | 0.00 USD | 321,970.00 USD | 25,970.00 USD | 5,200.00 USD | 112,830.00 USD |
| `1D` | `0.1516` | 177,970.00 USD | 0.00 USD | 177,970.00 USD | 59,890.00 USD | 8,340.00 USD | 17,370.00 USD |
| `7D` | `0.1516` | 478,790.00 USD | 0.00 USD | 478,790.00 USD | 0.00 USD | 13,330.00 USD | 205,120.00 USD |
| `1D` | `0.1519` | 92,370.00 USD | 0.00 USD | 92,370.00 USD | 14,340.00 USD | 2,630.00 USD | 16,310.00 USD |
| `7D` | `0.1520` | 260,340.00 USD | 0.00 USD | 260,340.00 USD | 47,340.00 USD | 22,090.00 USD | 87,060.00 USD |
| `1D` | `0.1522` | 59,100.00 USD | 0.00 USD | 59,100.00 USD | 38,050.00 USD | 4,440.00 USD | 5,820.00 USD |
| `7D` | `0.1524` | 103,860.00 USD | 0.00 USD | 103,860.00 USD | 0.00 USD | 13,950.00 USD | 8,320.00 USD |
| `1D` | `0.1525` | 10,790.00 USD | 0.00 USD | 10,790.00 USD | 0.00 USD | 0.00 USD | 1,800.00 USD |
| `7D` | `0.1528` | 81,590.00 USD | 0.00 USD | 81,590.00 USD | 0.00 USD | 33,940.00 USD | 0.00 USD |
| `7D` | `0.1532` | 47,650.00 USD | 0.00 USD | 47,650.00 USD | 0.00 USD | 17,260.00 USD | 0.00 USD |
| `1D` | `0.1534` | 8,980.00 USD | 0.00 USD | 8,980.00 USD | 0.00 USD | 8,980.00 USD | 0.00 USD |
| `7D` | `0.1536` | 30,390.00 USD | 0.00 USD | 30,390.00 USD | 0.00 USD | 8,570.00 USD | 0.00 USD |
| `7D` | `0.1540` | 21,820.00 USD | 0.00 USD | 21,820.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD |
| `7D` | `0.1544` | 3,590.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD |
| `1D` | `0.1548` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1548` | 2,860.00 USD | 2,860.00 USD | 0.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD |
| `7D` | `0.1548` | 5,720.00 USD | 5,720.00 USD | 0.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD |
| `1D` | `0.1549` | 17,000.00 USD | 17,000.00 USD | 0.00 USD | 0.00 USD | 17,000.00 USD | 0.00 USD |
| `1D` | `0.1552` | 19,510.00 USD | 19,510.00 USD | 0.00 USD | 0.00 USD | 2,500.00 USD | 0.00 USD |
| `7D` | `0.1552` | 17,540.00 USD | 17,540.00 USD | 0.00 USD | 0.00 USD | 11,820.00 USD | 0.00 USD |
| `7D` | `0.1560` | 28,520.00 USD | 28,520.00 USD | 0.00 USD | 0.00 USD | 10,990.00 USD | 0.00 USD |
| `1D` | `0.1561` | 24,480.00 USD | 24,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `1D` | `0.1564` | 286,390.00 USD | 286,390.00 USD | 0.00 USD | 3,130.00 USD | 13,270.00 USD | 245,520.00 USD |
| `7D` | `0.1564` | 62,280.00 USD | 62,280.00 USD | 0.00 USD | 0.00 USD | 33,750.00 USD | 0.00 USD |
| `1D` | `0.1567` | 411,380.00 USD | 411,380.00 USD | 0.00 USD | 72,650.00 USD | 32,420.00 USD | 19,910.00 USD |
| `7D` | `0.1568` | 340,960.00 USD | 340,960.00 USD | 0.00 USD | 111,700.00 USD | 15,360.00 USD | 151,620.00 USD |
| `1D` | `0.1570` | 604,120.00 USD | 604,120.00 USD | 0.00 USD | 0.00 USD | 12,360.00 USD | 180,370.00 USD |
| `7D` | `0.1572` | 674,760.00 USD | 674,760.00 USD | 0.00 USD | 235,420.00 USD | 39,540.00 USD | 58,840.00 USD |
| `1D` | `0.1573` | 624,430.00 USD | 624,430.00 USD | 0.00 USD | 20,310.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1576` | 760,620.00 USD | 760,620.00 USD | 0.00 USD | 25,970.00 USD | 0.00 USD | 110,230.00 USD |
| `7D` | `0.1576` | 987,120.00 USD | 987,120.00 USD | 0.00 USD | 44,680.00 USD | 123,840.00 USD | 143,850.00 USD |
| `1D` | `0.1579` | 810,440.00 USD | 810,440.00 USD | 0.00 USD | 49,820.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1580` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 177,280.00 USD | 101,090.00 USD | 0.00 USD |
| `7D` | `0.1584` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 80,450.00 USD | 43,370.00 USD | 0.00 USD |
| `1D` | `0.1585` | 849,670.00 USD | 849,670.00 USD | 0.00 USD | 28,600.00 USD | 2,370.00 USD | 8,250.00 USD |
| `1D` | `0.1588` | 909,240.00 USD | 909,240.00 USD | 0.00 USD | 15,100.00 USD | 28,750.00 USD | 15,730.00 USD |
| `7D` | `0.1588` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 69,180.00 USD | 44,590.00 USD | 0.00 USD |
| `1D` | `0.1591` | 962,750.00 USD | 962,750.00 USD | 0.00 USD | 0.00 USD | 26,120.00 USD | 27,390.00 USD |
| `7D` | `0.1592` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 64,620.00 USD | 0.00 USD |
| `1D` | `0.1594` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39,910.00 USD |
| `7D` | `0.1596` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 98,530.00 USD | 0.00 USD |
| `1D` | `0.1597` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 16,680.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1600` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 20,040.00 USD | 0.00 USD | 57,820.00 USD |
| `7D` | `0.1600` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 60,710.00 USD | 75,810.00 USD |
| `1D` | `0.1603` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 74,240.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1604` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 188,060.00 USD | 112,090.00 USD | 273,670.00 USD |
| `1D` | `0.1606` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 27,640.00 USD | 0.00 USD | 55,110.00 USD |
| `7D` | `0.1608` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 208,080.00 USD | 240,680.00 USD | 243,930.00 USD |
| `1D` | `0.1609` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 24,910.00 USD | 0.00 USD | 34,180.00 USD |
| `1D` | `0.1612` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 20,140.00 USD | 11,530.00 USD | 94,250.00 USD |
| `7D` | `0.1612` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 328,640.00 USD | 328,050.00 USD | 287,340.00 USD |
| `1D` | `0.1615` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 14,300.00 USD | 0.00 USD | 11,030.00 USD |
| `7D` | `0.1616` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 293,210.00 USD | 131,180.00 USD | 108,800.00 USD |
| `1D` | `0.1618` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 53,600.00 USD | 12,180.00 USD | 0.00 USD |
| `7D` | `0.1620` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 0.00 USD | 196,620.00 USD | 0.00 USD |
| `1D` | `0.1621` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 92,470.00 USD | 73,150.00 USD | 0.00 USD |
| `1D` | `0.1624` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 50,280.00 USD | 59,670.00 USD | 0.00 USD |
| `7D` | `0.1624` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 193,150.00 USD | 0.00 USD |
| `1D` | `0.1627` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 25,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1628` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 76,780.00 USD | 0.00 USD | 103,330.00 USD |
| `1D` | `0.1630` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 17,970.00 USD | 101,620.00 USD |
| `1D` | `0.1633` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 98,410.00 USD | 6,020.00 USD | 0.00 USD |
| `1D` | `0.1636` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 19,990.00 USD | 8,690.00 USD |
| `7D` | `0.1636` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 13,670.00 USD | 23,560.00 USD |
| `1D` | `0.1639` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 13,220.00 USD | 0.00 USD |
| `7D` | `0.1640` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD |
| `1D` | `0.1642` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 19,180.00 USD | 36,980.00 USD | 16,030.00 USD |
| `7D` | `0.1644` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 8,990.00 USD | 0.00 USD |
| `1D` | `0.1645` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 14,950.00 USD | 11,350.00 USD | 0.00 USD |
| `7D` | `0.1648` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD |
| `1D` | `0.1654` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,050.00 USD |
| `7D` | `0.1656` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 31,800.00 USD | 0.00 USD |
| `1D` | `0.1657` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 9,730.00 USD | 55,300.00 USD | 0.00 USD |
| `1D` | `0.1660` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 8,220.00 USD | 11,150.00 USD | 50,810.00 USD |
| `7D` | `0.1660` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 79,170.00 USD | 11,020.00 USD | 51,660.00 USD |
| `1D` | `0.1663` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 44,200.00 USD | 14,550.00 USD | 44,100.00 USD |
| `7D` | `0.1664` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD |
| `1D` | `0.1666` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 22,170.00 USD | 5,340.00 USD | 78,290.00 USD |
| `7D` | `0.1668` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 42,580.00 USD | 52,290.00 USD | 87,160.00 USD |
| `1D` | `0.1672` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 46,590.00 USD | 2,010.00 USD | 0.00 USD |
| `7D` | `0.1672` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 135,250.00 USD | 62,490.00 USD | 0.00 USD |
| `1D` | `0.1675` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 20,040.00 USD | 1,990.00 USD | 19,670.00 USD |
| `7D` | `0.1676` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 84,020.00 USD | 141,950.00 USD | 0.00 USD |
| `1D` | `0.1678` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 22,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1680` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 121,860.00 USD | 80,270.00 USD | 15,310.00 USD |
| `1D` | `0.1681` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 120,850.00 USD | 4,560.00 USD | 0.00 USD |
| `1D` | `0.1684` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 54,020.00 USD | 26,600.00 USD | 32,180.00 USD |
| `7D` | `0.1684` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD |
| `1D` | `0.1687` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 6,560.00 USD | 5,840.00 USD | 39,950.00 USD |
| `7D` | `0.1688` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD |
| `1D` | `0.1690` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 25,050.00 USD | 9,870.00 USD | 14,290.00 USD |
| `7D` | `0.1692` | 6,720,000.00 USD | 6,720,000.00 USD | 0.00 USD | 33,660.00 USD | 70,740.00 USD | 71,020.00 USD |
| `1D` | `0.1693` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 84,630.00 USD | 74,940.00 USD | 35,010.00 USD |
| `1D` | `0.1696` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 23,530.00 USD | 16,310.00 USD | 6,650.00 USD |
| `7D` | `0.1696` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 17,360.00 USD | 87,350.00 USD | 39,780.00 USD |
| `1D` | `0.1699` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 26,000.00 USD | 56,690.00 USD | 22,050.00 USD |
| `7D` | `0.1700` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 0.00 USD | 25,330.00 USD | 69,820.00 USD |
| `1D` | `0.1702` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 9,960.00 USD | 0.00 USD | 10,240.00 USD |
| `7D` | `0.1704` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 55,170.00 USD | 46,880.00 USD | 0.00 USD |
| `1D` | `0.1705` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 14,190.00 USD | 20,810.00 USD | 0.00 USD |
| `1D` | `0.1708` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 39,520.00 USD | 65,470.00 USD | 13,990.00 USD |
| `7D` | `0.1708` | 7,150,000.00 USD | 7,150,000.00 USD | 0.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD |
| `1D` | `0.1711` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 4,910.00 USD | 8,040.00 USD |
| `1D` | `0.1714` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 12,410.00 USD | 0.00 USD |
| `7D` | `0.1716` | 7,210,000.00 USD | 7,210,000.00 USD | 0.00 USD | 0.00 USD | 42,020.00 USD | 15,160.00 USD |
| `1D` | `0.1717` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 9,570.00 USD | 34,120.00 USD | 19,560.00 USD |
| `1D` | `0.1720` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 80,090.00 USD | 1,590.00 USD | 5,030.00 USD |
| `7D` | `0.1720` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 161,770.00 USD |
| `1D` | `0.1723` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 54,130.00 USD | 16,860.00 USD | 66,630.00 USD |
| `7D` | `0.1724` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 118,060.00 USD | 0.00 USD | 208,480.00 USD |
| `1D` | `0.1726` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 8,230.00 USD | 2,410.00 USD | 12,130.00 USD |
| `1D` | `0.1729` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD |
| `1D` | `0.1732` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD |
| `7D` | `0.1732` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 476,430.00 USD | 0.00 USD | 9,420.00 USD |
| `1D` | `0.1735` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 14,970.00 USD | 9,510.00 USD | 0.00 USD |
| `1D` | `0.1738` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 18,610.00 USD | 2,310.00 USD | 6,410.00 USD |
| `7D` | `0.1740` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 83,810.00 USD |
| `1D` | `0.1741` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 1,600.00 USD | 5,860.00 USD |
| `1D` | `0.1744` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 2,460.00 USD | 13,980.00 USD |
| `7D` | `0.1744` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1747` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 8,530.00 USD | 0.00 USD | 31,930.00 USD |
| `7D` | `0.1748` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `0.1750` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 80,070.00 USD | 2,280.00 USD | 22,640.00 USD |
| `7D` | `0.1752` | 8,650,000.00 USD | 8,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 291,880.00 USD |
| `1D` | `0.1753` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 32,240.00 USD | 0.00 USD | 33,630.00 USD |
| `1D` | `0.1756` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 23,610.00 USD | 27,640.00 USD | 73,180.00 USD |
| `7D` | `0.1756` | 8,950,000.00 USD | 8,950,000.00 USD | 0.00 USD | 112,930.00 USD | 0.00 USD | 186,030.00 USD |
| `1D` | `0.1759` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 85,450.00 USD | 31,960.00 USD | 36,770.00 USD |
| `7D` | `0.1760` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 268,160.00 USD | 71,260.00 USD | 32,350.00 USD |
| `1D` | `0.1762` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 72,450.00 USD | 83,100.00 USD | 66,600.00 USD |
| `7D` | `0.1764` | 9,990,000.00 USD | 9,990,000.00 USD | 0.00 USD | 353,950.00 USD | 270,450.00 USD | 40,340.00 USD |
| `1D` | `0.1765` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 20,220.00 USD | 28,990.00 USD | 43,560.00 USD |
| `1D` | `0.1768` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 19,860.00 USD | 83,210.00 USD | 62,630.00 USD |
| `7D` | `0.1768` | 10,370,000.00 USD | 10,370,000.00 USD | 0.00 USD | 191,690.00 USD | 154,100.00 USD | 31,570.00 USD |
| `1D` | `0.1771` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 43,430.00 USD | 19,520.00 USD | 24,210.00 USD |
| `7D` | `0.1772` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 98,390.00 USD | 153,480.00 USD | 21,360.00 USD |
| `1D` | `0.1774` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 20,200.00 USD | 30,630.00 USD | 26,430.00 USD |
| `7D` | `0.1776` | 10,890,000.00 USD | 10,890,000.00 USD | 0.00 USD | 186,770.00 USD | 59,720.00 USD | 0.00 USD |
| `1D` | `0.1777` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 42,080.00 USD | 81,500.00 USD | 24,860.00 USD |
| `1D` | `0.1780` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 11,580.00 USD | 9,760.00 USD | 7,340.00 USD |
| `7D` | `0.1780` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 52,730.00 USD | 46,410.00 USD | 157,510.00 USD |
| `1D` | `0.1783` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 27,640.00 USD | 15,680.00 USD | 19,300.00 USD |
| `7D` | `0.1784` | 11,370,000.00 USD | 11,370,000.00 USD | 0.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD |
| `1D` | `0.1786` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 16,960.00 USD | 31,510.00 USD | 5,350.00 USD |
| `7D` | `0.1788` | 11,540,000.00 USD | 11,540,000.00 USD | 0.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD |
| `1D` | `0.1789` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 15,890.00 USD | 31,190.00 USD | 10,060.00 USD |
| `1D` | `0.1792` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 13,950.00 USD | 16,470.00 USD | 18,160.00 USD |
| `7D` | `0.1792` | 11,770,000.00 USD | 11,770,000.00 USD | 0.00 USD | 182,810.00 USD | 46,960.00 USD | 3,940.00 USD |
| `1D` | `0.1795` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 53,160.00 USD | 43,180.00 USD | 18,910.00 USD |
| `7D` | `0.1796` | 11,860,000.00 USD | 11,860,000.00 USD | 0.00 USD | 17,130.00 USD | 26,110.00 USD | 44,450.00 USD |
| `1D` | `0.1798` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 15,420.00 USD | 17,120.00 USD | 21,440.00 USD |
| `7D` | `0.1800` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 12,940.00 USD | 34,680.00 USD | 73,510.00 USD |
| `1D` | `0.1801` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 12,470.00 USD | 23,820.00 USD | 13,950.00 USD |
| `1D` | `0.1804` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 10,530.00 USD | 16,830.00 USD | 19,340.00 USD |
| `7D` | `0.1804` | 12,070,000.00 USD | 12,070,000.00 USD | 0.00 USD | 35,280.00 USD | 32,850.00 USD | 23,570.00 USD |
| `1D` | `0.1807` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 16,640.00 USD | 17,460.00 USD | 9,040.00 USD |
| `7D` | `0.1808` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 35,050.00 USD | 67,250.00 USD | 73,440.00 USD |
| `1D` | `0.1810` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 12,880.00 USD | 15,840.00 USD | 8,290.00 USD |
| `7D` | `0.1812` | 12,390,000.00 USD | 12,390,000.00 USD | 0.00 USD | 64,990.00 USD | 29,900.00 USD | 50,510.00 USD |
| `1D` | `0.1813` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 14,660.00 USD | 37,850.00 USD | 15,990.00 USD |
| `1D` | `0.1816` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 13,550.00 USD | 0.00 USD | 12,730.00 USD |
| `7D` | `0.1816` | 12,530,000.00 USD | 12,530,000.00 USD | 0.00 USD | 69,700.00 USD | 33,940.00 USD | 38,270.00 USD |
| `1D` | `0.1819` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 6,740.00 USD | 12,120.00 USD | 6,830.00 USD |
| `7D` | `0.1820` | 12,700,000.00 USD | 12,700,000.00 USD | 0.00 USD | 65,350.00 USD | 54,880.00 USD | 43,100.00 USD |
| `1D` | `0.1822` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 0.00 USD | 21,610.00 USD | 1,930.00 USD |
| `7D` | `0.1824` | 12,910,000.00 USD | 12,910,000.00 USD | 0.00 USD | 80,350.00 USD | 17,880.00 USD | 112,550.00 USD |
| `1D` | `0.1825` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 18,910.00 USD | 1,780.00 USD | 6,470.00 USD |
| `1D` | `0.1828` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 6,840.00 USD | 5,270.00 USD | 2,530.00 USD |
| `7D` | `0.1828` | 13,090,000.00 USD | 13,090,000.00 USD | 0.00 USD | 79,610.00 USD | 29,630.00 USD | 69,840.00 USD |
| `7D` | `0.1832` | 13,300,000.00 USD | 13,300,000.00 USD | 0.00 USD | 108,540.00 USD | 31,590.00 USD | 74,200.00 USD |
| `1D` | `0.1834` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 2,670.00 USD | 0.00 USD | 3,370.00 USD |
| `7D` | `0.1836` | 13,640,000.00 USD | 13,640,000.00 USD | 0.00 USD | 172,660.00 USD | 110,870.00 USD | 52,650.00 USD |
| `1D` | `0.1837` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 3,610.00 USD | 2,640.00 USD | 1,360.00 USD |
| `1D` | `0.1840` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 5,430.00 USD | 1,970.00 USD | 12,670.00 USD |
| `7D` | `0.1840` | 13,980,000.00 USD | 13,980,000.00 USD | 0.00 USD | 141,620.00 USD | 50,840.00 USD | 151,740.00 USD |
| `1D` | `0.1843` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 1,030.00 USD | 3,550.00 USD | 0.00 USD |
| `7D` | `0.1844` | 14,190,000.00 USD | 14,190,000.00 USD | 0.00 USD | 94,510.00 USD | 20,390.00 USD | 97,510.00 USD |
| `7D` | `0.1848` | 14,340,000.00 USD | 14,340,000.00 USD | 0.00 USD | 35,280.00 USD | 69,910.00 USD | 41,760.00 USD |
| `7D` | `0.1852` | 14,790,000.00 USD | 14,790,000.00 USD | 0.00 USD | 168,270.00 USD | 28,290.00 USD | 251,810.00 USD |
| `7D` | `0.1856` | 15,030,000.00 USD | 15,030,000.00 USD | 0.00 USD | 100,160.00 USD | 21,030.00 USD | 120,950.00 USD |
| `7D` | `0.1860` | 15,270,000.00 USD | 15,270,000.00 USD | 0.00 USD | 64,600.00 USD | 48,330.00 USD | 127,610.00 USD |
| `7D` | `0.1864` | 15,430,000.00 USD | 15,430,000.00 USD | 0.00 USD | 48,260.00 USD | 44,140.00 USD | 61,380.00 USD |
| `7D` | `0.1868` | 15,670,000.00 USD | 15,670,000.00 USD | 0.00 USD | 133,990.00 USD | 51,510.00 USD | 56,290.00 USD |
| `7D` | `0.1872` | 16,130,000.00 USD | 16,130,000.00 USD | 0.00 USD | 169,490.00 USD | 133,380.00 USD | 155,060.00 USD |
| `7D` | `0.1876` | 16,260,000.00 USD | 16,260,000.00 USD | 0.00 USD | 65,910.00 USD | 23,180.00 USD | 43,960.00 USD |
| `7D` | `0.1880` | 16,380,000.00 USD | 16,380,000.00 USD | 0.00 USD | 57,250.00 USD | 35,940.00 USD | 30,950.00 USD |
| `7D` | `0.1884` | 16,440,000.00 USD | 16,440,000.00 USD | 0.00 USD | 14,000.00 USD | 35,430.00 USD | 9,740.00 USD |
| `7D` | `0.1888` | 16,560,000.00 USD | 16,560,000.00 USD | 0.00 USD | 22,970.00 USD | 4,800.00 USD | 88,260.00 USD |
| `7D` | `0.1892` | 16,650,000.00 USD | 16,650,000.00 USD | 0.00 USD | 49,980.00 USD | 2,860.00 USD | 34,160.00 USD |
| `7D` | `0.1896` | 16,720,000.00 USD | 16,720,000.00 USD | 0.00 USD | 42,320.00 USD | 11,820.00 USD | 18,680.00 USD |
| `7D` | `0.1900` | 16,770,000.00 USD | 16,770,000.00 USD | 0.00 USD | 0.00 USD | 29,650.00 USD | 20,420.00 USD |
| `7D` | `0.1904` | 16,810,000.00 USD | 16,810,000.00 USD | 0.00 USD | 14,330.00 USD | 17,690.00 USD | 10,800.00 USD |
| `7D` | `0.1908` | 16,930,000.00 USD | 16,930,000.00 USD | 0.00 USD | 24,190.00 USD | 37,870.00 USD | 52,810.00 USD |
| `7D` | `0.1912` | 16,950,000.00 USD | 16,950,000.00 USD | 0.00 USD | 0.00 USD | 9,380.00 USD | 10,330.00 USD |
| `7D` | `0.1916` | 16,980,000.00 USD | 16,980,000.00 USD | 0.00 USD | 7,460.00 USD | 12,040.00 USD | 11,900.00 USD |
| `7D` | `0.1920` | 16,980,000.00 USD | 16,980,000.00 USD | 0.00 USD | 0.00 USD | 5,100.00 USD | 0.00 USD |
| `7D` | `0.1924` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD |
| `7D` | `0.1928` | 17,020,000.00 USD | 17,020,000.00 USD | 0.00 USD | 11,600.00 USD | 7,370.00 USD | 0.00 USD |
| `7D` | `0.1944` | 17,030,000.00 USD | 17,030,000.00 USD | 0.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1952` | 17,040,000.00 USD | 17,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD |
| `7D` | `0.1956` | 17,050,000.00 USD | 17,050,000.00 USD | 0.00 USD | 4,860.00 USD | 2,760.00 USD | 0.00 USD |
| `7D` | `0.1960` | 17,050,000.00 USD | 17,050,000.00 USD | 0.00 USD | 5,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1964` | 17,070,000.00 USD | 17,070,000.00 USD | 0.00 USD | 6,470.00 USD | 2,700.00 USD | 10,990.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `186.09M` | Total OI Tokens: `1,210,950,062.1 ARB`
  * 1h OI Change: `-1.77%` | 4h OI Change: `-11.00%` | 24h OI Change: `-20.73%`
  * Exchange Breakdown: Binance=`42.63M` | Bybit=`26.98M` | OKX=`14.35M` | Hyperliquid=`12.59M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-1.83K` | Last 24h: `10.97K` | Last 3d: `22.34K` | Last 7d: `43.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0076%` | **USDT OKX** | `0.0013%` |
| **USDT Bybit** | `0.0028%` | **USDT KuCoin** | `-0.0007%` |
| **USDT MEXC** | `0.0015%` | **USDT BingX** | `0.0034%` |
| **USDT Gate** | `-0.0124%` | **USDT Bitget** | `-0.0037%` |
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
| `4H` | `ARB` | `46.81%` | `53.19%` | `0.88` | 55,900,000.00 USD |
| `4H` | `Binance` | `46.12%` | `53.88%` | `0.86` | 21,420,000.00 USD |
| `4H` | `OKX` | `46.45%` | `53.55%` | `0.87` | 6,820,000.00 USD |
| `4H` | `Bybit` | `45.47%` | `54.53%` | `0.83` | 8,910,000.00 USD |
| `4H` | `KuCoin` | `46.74%` | `53.26%` | `0.88` | 508,640.00 USD |
| `4H` | `Gate` | `53.68%` | `46.32%` | `1.16` | 631,620.00 USD |
| `4H` | `Bitget` | `48.87%` | `51.13%` | `0.96` | 3,690,000.00 USD |
| `4H` | `BingX` | `45.96%` | `54.04%` | `0.85` | 1,820,000.00 USD |
| `4H` | `MEXC` | `42.7%` | `57.3%` | `0.75` | 2,500,000.00 USD |
| `4H` | `Bitunix` | `45.77%` | `54.23%` | `0.84` | 678,220.00 USD |
| `4H` | `Hyperliquid` | `37.84%` | `62.16%` | `0.61` | 757,250.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.03%` | `51.97%` | `0.92` | 7,200,000.00 USD |
| `4H` | `Crypto.com` | `23.33%` | `76.67%` | `0.30` | 23,230.00 USD |
| `4H` | `WhiteBIT` | `87.69%` | `12.31%` | `7.12` | 689,310.00 USD |
| `4H` | `HTX` | `47.5%` | `52.5%` | `0.90` | 47,110.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `56.74%` | `43.26%` | `1.31` | 67,130.00 USD |
| `4H` | `Aster` | `33.18%` | `66.82%` | `0.50` | 54,630.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.52%` | `49.48%` | `1.02` | 76,980.00 USD |
| `4H` | `Whale Positions` | `46.12%` | `53.88%` | `0.86` | 21,420,000.00 USD |
| `4H` | `Global Accounts` | `46.81%` | `53.19%` | `0.88` | 55,900,000.00 USD |


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
| `0:00 UTC` | `0.1538` | `0.1545` | `0.1538` | `0.1566` | `0.1527` | 3,617,846.96 USD | 1,695,709.87 USD | 1,922,137.10 USD | -226,427.23 USD | `-6.26%` | `8B / 16S` |

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
| `5m` | -15,440.00 USD | -783,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -4,870.00 USD | -933,370.00 USD | **`DISTRIBUTION`** |
| `30m` | -65,510.00 USD | -1,680,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 22,730.00 USD | 729,490.00 USD | **`ACCUMULATION`** |
| `2h` | -1,660,000.00 USD | -5,690,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -2,080,000.00 USD | -6,170,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -2,330,000.00 USD | -8,200,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,050,000.00 USD | -9,810,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,660,000.00 USD | -10,310,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,970,000.00 USD | -10,970,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,000,000.00 USD | -37,050,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -34,260,000.00 USD | -168,290,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-15.44K` | 15m=`-4.87K` | 1h=`+22.73K` | 24h=`-2.97M`
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
  * `2026-10-30 03:29:57 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:57 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:40:57 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:41:57 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:41:57 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:57 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
