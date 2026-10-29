# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 02:21:35 IST` (`2026-10-29 20:51:35 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1650` | `0.1656` | `0.1615` | `0.1622` | `13,253,947` | 2,164,357.49 USD | -536,857.98 USD | `-24.80%` | -5,102,110.88 USD | `-3.12` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1622` | `0.1623` | `0.1593` | `0.1600` | `15,948,526` | 2,561,145.51 USD | -608,859.34 USD | `-23.77%` | -5,710,970.22 USD | `-2.67` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1600` | `0.1600` | `0.1541` | `0.1552` | `30,618,544` | 4,802,945.76 USD | -1,216,543.68 USD | `-25.33%` | -6,927,513.90 USD | `-3.36` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1683` | `0.1684` | `0.1640` | `0.1657` | `15,315,777` | 2,535,332.38 USD | -237,581.36 USD | `-9.37%` | -4,675,846.63 USD | `-0.97` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1657` | `0.1661` | `0.1649` | `0.1650` | `4,340,197` | 718,046.47 USD | 110,593.73 USD | `+15.40%` | -4,565,252.91 USD | `+1.11` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1650` | `0.1656` | `0.1541` | `0.1552` | `58,985,144` | 9,398,938.53 USD | -2,274,131.72 USD | `-24.20%` | -6,839,384.63 USD | `-4.12` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1696` | `0.1704` | `0.1673` | `0.1687` | `18,975,463` | 3,201,824.26 USD | -35,947.57 USD | `-1.12%` | -4,720,262.78 USD | `+0.39` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1686` | `0.1693` | `0.1678` | `0.1683` | `12,478,051` | 2,101,814.57 USD | 317,188.30 USD | `+15.09%` | -4,403,074.48 USD | `+1.26` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1683` | `0.1684` | `0.1541` | `0.1548` | `79,625,635` | 12,804,853.34 USD | -2,498,647.57 USD | `-19.51%` | -6,901,722.05 USD | `-3.44` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,374,542.78 USD | `-1.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,572,000.78 USD | `-0.89` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1541` | `0.1550` | `79,551,796` | 12,793,419.67 USD | -2,493,672.88 USD | `-19.49%` | -6,065,673.67 USD | `-1.79` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1652` | `0.1687` | `0.1623` | `0.1631` | `68,085,678` | 11,252,816.65 USD | -909,329.92 USD | `-8.08%` | -705,420.63 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,136,414.44 USD | `-0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,374,542.78 USD | `-1.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,572,000.78 USD | `-0.89` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1541` | `0.1550` | `79,551,796` | 12,793,419.67 USD | -2,493,672.88 USD | `-19.49%` | -6,065,673.67 USD | `-1.79` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:14:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1704` | 7,480.04 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 7.48K USD at 0.1704 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1704` | 99.93 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.10K USD at 0.1704 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1704` | 455.89 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.46K USD at 0.1704 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1704` | 455.89 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.46K USD at 0.1704 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1704` | 1,816.80 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 1.82K USD at 0.1704 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1704` | 394.95 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.39K USD at 0.1704 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1704` | 1,816.80 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 1.82K USD at 0.1704 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1704` | 394.95 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.39K USD at 0.1704 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1704` | 1,274.59 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 1.27K USD at 0.1704 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1695` | 7,870.81 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale BUY: 7.87K USD at 0.1695 USD [API] | `2026-10-28 02:08:38` |
| `ANNOUNCEMENT` | `INFO` | `0.1952` | 1,892.80 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 1.89K USD at 0.1952 USD [API] | `2026-10-02 18:39:18` |
| `ANNOUNCEMENT` | `INFO` | `0.1972` | 32.77 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.03K USD at 0.1972 USD [API] | `2026-10-01 10:02:44` |
| `ANNOUNCEMENT` | `INFO` | `0.2130` | 263.28 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.26K USD at 0.2130 USD [API] | `2026-09-24 08:27:05` |
| `ANNOUNCEMENT` | `INFO` | `0.1607` | 125.43 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.13K USD at 0.1607 USD [API] | `2026-09-16 14:22:29` |
| `ANNOUNCEMENT` | `INFO` | `0.1608` | 997.00 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 1.00K USD at 0.1608 USD [API] | `2026-09-16 14:22:29` |
| `ANNOUNCEMENT` | `INFO` | `0.1608` | 400.00 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.40K USD at 0.1608 USD [API] | `2026-09-16 14:22:29` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.1784` (Vol: 124,200.00 USD, Dist: `+7.91%`) | Long MP=`0.1622` (Vol: 145,200.00 USD, Dist: `--1.94%`)
  * 48H Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+7.88%`) | Long MP=`0.1598` (Vol: 154,300.00 USD, Dist: `--3.38%`)
  * 3D Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+7.88%`) | Long MP=`0.1598` (Vol: 205,900.00 USD, Dist: `--3.38%`)
  * 7D Horizon: Short MP=`0.1834` (Vol: 181,500.00 USD, Dist: `+10.87%`) | Long MP=`0.1616` (Vol: 292,500.00 USD, Dist: `--2.27%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0345` | 1,180.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0375` | 2,200.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0385` | 1,490.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0395` | 138,900.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 408.10 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 170.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0445` | 8,100.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0455` | 3,090.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0475` | 4,840.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 400.94 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 289.43 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0535` | 668.38 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 7,100.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 18,660.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 148.49 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 187.50 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 283.15 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 100,530.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 590.45 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 77,980.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 3,260.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 5,840.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 111.58 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,440.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 2,370.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 368.95 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 14,690.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 27,480.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 6,180.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 6,040.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 7,840.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 13,950.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 751.50 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 19,010.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 22,430.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 362.62 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 12,960.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 1,320.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 4,130.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 814.24 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 4,090.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 589.63 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 145.24 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 5,970.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 9,200.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 12,790.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 811.82 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 802.14 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 6,700.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 12,770.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 181.20 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 1,650.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 342.59 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 534.49 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 425.50 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1125` | 2,190.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 1,360.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 8,950.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 16,170.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 11,120.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 1,760.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 26,260.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 6,210.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 14,190.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 8,920.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 34,620.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 3,110.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 4,960.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 1,200.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 4,190.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 11,100.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 4,010.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 13,600.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 10,500.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 8,090.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 26,200.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 2,970.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1365` | 2,740.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1375` | 13,750.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1385` | 5,340.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1395` | 6,710.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 2,800.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 75,150.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 490,800.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1432` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 19,330.00 USD | 921,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1438` | 5,060,000.00 USD | 5,060,000.00 USD | 13,180.00 USD | 0.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1441` | 5,040,000.00 USD | 5,040,000.00 USD | 3,450.00 USD | 5,260.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 53,790.00 USD | 902,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1450` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 5,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1453` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 106.39 USD | 848,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1456` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1459` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1465` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 3,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1465` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 47,190.00 USD | 848,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1468` | 1,790,000.00 USD | 1,790,000.00 USD | 12,090.00 USD | 2,700.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1468` | 4,990,000.00 USD | 4,990,000.00 USD | 9,720.00 USD | 9,180.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1471` | 1,770,000.00 USD | 1,770,000.00 USD | 4,400.00 USD | 5,970.00 USD | 1,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1471` | 4,960,000.00 USD | 4,960,000.00 USD | 6,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1474` | 1,760,000.00 USD | 1,760,000.00 USD | 7,230.00 USD | 3,000.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1474` | 4,960,000.00 USD | 4,960,000.00 USD | 19,430.00 USD | 9,220.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 73,750.00 USD | 801,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1477` | 1,740,000.00 USD | 1,740,000.00 USD | 11,250.00 USD | 2,820.00 USD | 5,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1477` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 25,460.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1480` | 1,720,000.00 USD | 1,720,000.00 USD | 14,790.00 USD | 17,450.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1480` | 4,880,000.00 USD | 4,880,000.00 USD | 6,990.00 USD | 29,300.00 USD | 20,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1483` | 1,690,000.00 USD | 1,690,000.00 USD | 4,550.00 USD | 4,230.00 USD | 11,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1483` | 4,820,000.00 USD | 4,820,000.00 USD | 42,230.00 USD | 16,640.00 USD | 33,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,650.00 USD | 727,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1486` | 1,670,000.00 USD | 1,670,000.00 USD | 13,550.00 USD | 0.00 USD | 9,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1486` | 4,730,000.00 USD | 4,730,000.00 USD | 18,610.00 USD | 10,470.00 USD | 25,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1489` | 1,640,000.00 USD | 1,640,000.00 USD | 6,740.00 USD | 7,050.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1489` | 4,680,000.00 USD | 4,680,000.00 USD | 11,170.00 USD | 3,710.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1492` | 1,620,000.00 USD | 1,620,000.00 USD | 10,170.00 USD | 8,610.00 USD | 8,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1492` | 4,650,000.00 USD | 4,650,000.00 USD | 40,320.00 USD | 17,880.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1495` | 1,600,000.00 USD | 1,600,000.00 USD | 10,900.00 USD | 5,270.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1495` | 4,560,000.00 USD | 4,560,000.00 USD | 34,650.00 USD | 18,690.00 USD | 12,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 35,860.00 USD | 724,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1498` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 347.81 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1498` | 4,490,000.00 USD | 4,490,000.00 USD | 42,100.00 USD | 9,610.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1501` | 1,580,000.00 USD | 1,580,000.00 USD | 6,280.00 USD | 0.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1501` | 4,430,000.00 USD | 4,430,000.00 USD | 21,010.00 USD | 7,930.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1504` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 2,640.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1504` | 4,390,000.00 USD | 4,390,000.00 USD | 17,800.00 USD | 11,590.00 USD | 44,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1505` | 102,290.00 USD | 689,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1507` | 1,560,000.00 USD | 1,560,000.00 USD | 5,430.00 USD | 1,730.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1507` | 4,310,000.00 USD | 4,310,000.00 USD | 28,940.00 USD | 12,910.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1510` | 1,550,000.00 USD | 1,550,000.00 USD | 5,640.00 USD | 2,850.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1510` | 4,240,000.00 USD | 4,240,000.00 USD | 12,660.00 USD | 12,930.00 USD | 29,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1513` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 5,200.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1513` | 4,180,000.00 USD | 4,180,000.00 USD | 32,900.00 USD | 17,610.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 9,900.00 USD | 586,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1516` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 2,580.00 USD | 1,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1516` | 4,090,000.00 USD | 4,090,000.00 USD | 54,550.00 USD | 0.00 USD | 43,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1519` | 1,530,000.00 USD | 1,530,000.00 USD | 14,340.00 USD | 2,630.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1519` | 4,000,000.00 USD | 4,000,000.00 USD | 46,220.00 USD | 19,520.00 USD | 70,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1522` | 1,490,000.00 USD | 1,490,000.00 USD | 9,450.00 USD | 4,440.00 USD | 5,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1522` | 3,860,000.00 USD | 3,860,000.00 USD | 49,800.00 USD | 9,640.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1525` | 1,480,000.00 USD | 1,480,000.00 USD | 1,870.00 USD | 0.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1525` | 3,780,000.00 USD | 3,780,000.00 USD | 25,790.00 USD | 13,700.00 USD | 19,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1525` | 42,800.00 USD | 576,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1528` | 1,460,000.00 USD | 1,460,000.00 USD | 3,300.00 USD | 0.00 USD | 10,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1528` | 3,720,000.00 USD | 3,720,000.00 USD | 75,690.00 USD | 27,110.00 USD | 27,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1531` | 1,450,000.00 USD | 1,450,000.00 USD | 11,950.00 USD | 6,940.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1531` | 3,590,000.00 USD | 3,590,000.00 USD | 35,030.00 USD | 8,400.00 USD | 16,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1534` | 1,420,000.00 USD | 1,420,000.00 USD | 7,320.00 USD | 2,820.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1534` | 3,530,000.00 USD | 3,530,000.00 USD | 15,780.00 USD | 17,430.00 USD | 20,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 189,960.00 USD | 534,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1537` | 1,410,000.00 USD | 1,410,000.00 USD | 4,320.00 USD | 5,200.00 USD | 2,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1537` | 3,470,000.00 USD | 3,470,000.00 USD | 37,050.00 USD | 11,700.00 USD | 10,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1540` | 1,400,000.00 USD | 1,400,000.00 USD | 4,630.00 USD | 4,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1540` | 3,410,000.00 USD | 3,410,000.00 USD | 14,000.00 USD | 6,530.00 USD | 5,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1543` | 1,390,000.00 USD | 1,390,000.00 USD | 9,690.00 USD | 2,220.00 USD | 6,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1543` | 3,390,000.00 USD | 3,390,000.00 USD | 9,250.00 USD | 3,590.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1545` | 26,170.00 USD | 344,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1546` | 1,370,000.00 USD | 1,370,000.00 USD | 3,580.00 USD | 7,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1546` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 5,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1549` | 1,360,000.00 USD | 1,360,000.00 USD | 5,950.00 USD | 3,490.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1549` | 3,360,000.00 USD | 3,360,000.00 USD | 11,570.00 USD | 6,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1552` | 1,350,000.00 USD | 1,350,000.00 USD | 4,500.00 USD | 2,500.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1552` | 3,350,000.00 USD | 3,350,000.00 USD | 23,110.00 USD | 7,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1555` | 1,340,000.00 USD | 1,340,000.00 USD | 9,910.00 USD | 17,380.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1555` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1555` | 39,570.00 USD | 317,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1558` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 1,660.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1558` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 10,990.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1561` | 1,290,000.00 USD | 1,290,000.00 USD | 2,970.00 USD | 11,300.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1561` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 5,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1564` | 1,270,000.00 USD | 1,270,000.00 USD | 6,180.00 USD | 6,250.00 USD | 14,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1564` | 3,280,000.00 USD | 3,280,000.00 USD | 24,300.00 USD | 28,690.00 USD | 21,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1565` | 23,920.00 USD | 278,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1567` | 1,240,000.00 USD | 1,240,000.00 USD | 53,880.00 USD | 9,160.00 USD | 19,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1567` | 3,210,000.00 USD | 3,210,000.00 USD | 41,770.00 USD | 15,360.00 USD | 15,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1570` | 1,160,000.00 USD | 1,160,000.00 USD | 23,260.00 USD | 35,190.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1570` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 5,100.00 USD | 34,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1573` | 1,090,000.00 USD | 1,090,000.00 USD | 36,490.00 USD | 9,280.00 USD | 8,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1573` | 3,100,000.00 USD | 3,100,000.00 USD | 91,190.00 USD | 56,100.00 USD | 25,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1575` | 4,940.00 USD | 254,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1576` | 1,040,000.00 USD | 1,040,000.00 USD | 34,470.00 USD | 30,350.00 USD | 23,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1576` | 2,920,000.00 USD | 2,920,000.00 USD | 26,600.00 USD | 102,190.00 USD | 54,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1579` | 951,470.00 USD | 951,470.00 USD | 77,110.00 USD | 51,020.00 USD | 30,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1579` | 2,740,000.00 USD | 2,740,000.00 USD | 101,500.00 USD | 95,190.00 USD | 42,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1582` | 792,990.00 USD | 792,990.00 USD | 24,610.00 USD | 14,530.00 USD | 15,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1582` | 2,500,000.00 USD | 2,500,000.00 USD | 56,130.00 USD | 13,480.00 USD | 89,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1585` | 738,740.00 USD | 738,740.00 USD | 33,880.00 USD | 5,120.00 USD | 26,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1585` | 2,340,000.00 USD | 2,340,000.00 USD | 87,110.00 USD | 50,340.00 USD | 75,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1585` | 5,760.00 USD | 249,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1588` | 673,390.00 USD | 673,390.00 USD | 20,120.00 USD | 28,750.00 USD | 15,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1588` | 2,130,000.00 USD | 2,130,000.00 USD | 34,830.00 USD | 30,030.00 USD | 48,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1591` | 608,790.00 USD | 608,790.00 USD | 15,380.00 USD | 26,120.00 USD | 27,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1591` | 2,010,000.00 USD | 2,010,000.00 USD | 110,640.00 USD | 49,670.00 USD | 80,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1594` | 539,900.00 USD | 539,900.00 USD | 63,660.00 USD | 13,170.00 USD | 19,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1594` | 1,770,000.00 USD | 1,770,000.00 USD | 85,560.00 USD | 39,260.00 USD | 102,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1595` | 63,000.00 USD | 243,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1597` | 443,160.00 USD | 443,160.00 USD | 39,740.00 USD | 28,580.00 USD | 45,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1597` | 1,550,000.00 USD | 1,550,000.00 USD | 228,850.00 USD | 96,110.00 USD | 102,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1600` | 329,250.00 USD | 329,250.00 USD | 73,200.00 USD | 22,650.00 USD | 37,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1600` | 1,120,000.00 USD | 1,120,000.00 USD | 105,580.00 USD | 38,830.00 USD | 76,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1603` | 195,560.00 USD | 195,560.00 USD | 55,830.00 USD | 30,780.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1603` | 896,560.00 USD | 896,560.00 USD | 126,950.00 USD | 54,840.00 USD | 126,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1605` | 37,640.00 USD | 180,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1606` | 102,160.00 USD | 102,160.00 USD | 50,480.00 USD | 17,670.00 USD | 34,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1606` | 588,480.00 USD | 588,480.00 USD | 211,140.00 USD | 149,480.00 USD | 227,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1609` | 184,610.00 USD | 184,610.00 USD | 66,290.00 USD | 61,130.00 USD | 57,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1609` | 504,410.00 USD | 504,410.00 USD | 92,990.00 USD | 229,060.00 USD | 182,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1612` | 526,190.00 USD | 526,190.00 USD | 164,000.00 USD | 115,390.00 USD | 62,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1612` | 1,190,000.00 USD | 1,190,000.00 USD | 281,220.00 USD | 247,430.00 USD | 159,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1615` | 613,650.00 USD | 613,650.00 USD | 40,780.00 USD | 35,650.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1615` | 1,700,000.00 USD | 1,700,000.00 USD | 293,210.00 USD | 107,900.00 USD | 108,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1615` | 17,290.00 USD | 143,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1618` | 713,270.00 USD | 713,270.00 USD | 86,250.00 USD | 13,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1618` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 128,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1621` | 878,900.00 USD | 878,900.00 USD | 92,470.00 USD | 73,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1621` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 148,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1624` | 969,380.00 USD | 969,380.00 USD | 30,810.00 USD | 59,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1624` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 135,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1625` | 106,340.00 USD | 125,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1627` | 995,260.00 USD | 995,260.00 USD | 25,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1635` | 1,230.00 USD | 19,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1636` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 9,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1636` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 13,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1639` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 13,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1642` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 27,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1642` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1645` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 7,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1645` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 8,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1645` | 6,190.00 USD | 18,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1648` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1654` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1654` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 31,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1655` | 12,070.00 USD | 12,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1657` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 55,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1657` | 2,220,000.00 USD | 2,220,000.00 USD | 10,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1660` | 1,140,000.00 USD | 1,140,000.00 USD | 8,220.00 USD | 11,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1660` | 2,260,000.00 USD | 2,260,000.00 USD | 29,890.00 USD | 11,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1663` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 5,570.00 USD | 44,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1663` | 2,450,000.00 USD | 2,450,000.00 USD | 86,050.00 USD | 51,000.00 USD | 51,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1666` | 1,280,000.00 USD | 1,280,000.00 USD | 22,170.00 USD | 0.00 USD | 73,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1666` | 2,560,000.00 USD | 2,560,000.00 USD | 49,590.00 USD | 32,780.00 USD | 28,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1669` | 2,780,000.00 USD | 2,780,000.00 USD | 76,120.00 USD | 64,050.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1672` | 1,320,000.00 USD | 1,320,000.00 USD | 42,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1672` | 2,890,000.00 USD | 2,890,000.00 USD | 70,540.00 USD | 38,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1675` | 1,360,000.00 USD | 1,360,000.00 USD | 20,040.00 USD | 0.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1675` | 3,060,000.00 USD | 3,060,000.00 USD | 64,490.00 USD | 105,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1678` | 1,380,000.00 USD | 1,380,000.00 USD | 14,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1678` | 3,220,000.00 USD | 3,220,000.00 USD | 71,860.00 USD | 79,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1681` | 1,500,000.00 USD | 1,500,000.00 USD | 120,850.00 USD | 4,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1681` | 3,340,000.00 USD | 3,340,000.00 USD | 69,520.00 USD | 36,390.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1684` | 1,620,000.00 USD | 1,620,000.00 USD | 54,020.00 USD | 26,600.00 USD | 32,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1684` | 3,410,000.00 USD | 3,410,000.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1685` | 5,550.00 USD | 5,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1687` | 1,640,000.00 USD | 1,640,000.00 USD | 6,560.00 USD | 3,180.00 USD | 14,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1687` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1690` | 1,680,000.00 USD | 1,680,000.00 USD | 18,380.00 USD | 6,980.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1690` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 38,670.00 USD | 40,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1693` | 1,810,000.00 USD | 1,810,000.00 USD | 53,390.00 USD | 74,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1693` | 3,560,000.00 USD | 3,560,000.00 USD | 21,780.00 USD | 32,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1696` | 1,840,000.00 USD | 1,840,000.00 USD | 11,080.00 USD | 16,310.00 USD | 6,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1696` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 87,350.00 USD | 28,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1699` | 1,920,000.00 USD | 1,920,000.00 USD | 20,810.00 USD | 56,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1699` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 25,330.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1702` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1702` | 3,840,000.00 USD | 3,840,000.00 USD | 55,170.00 USD | 46,880.00 USD | 22,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1705` | 1,960,000.00 USD | 1,960,000.00 USD | 14,190.00 USD | 20,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1708` | 2,080,000.00 USD | 2,080,000.00 USD | 33,800.00 USD | 65,470.00 USD | 13,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1708` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1711` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 4,910.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1714` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 12,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1714` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1717` | 2,170,000.00 USD | 2,170,000.00 USD | 9,570.00 USD | 34,120.00 USD | 19,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1717` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 15,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1720` | 2,250,000.00 USD | 2,250,000.00 USD | 80,090.00 USD | 1,590.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1720` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 161,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1723` | 2,390,000.00 USD | 2,390,000.00 USD | 54,130.00 USD | 16,860.00 USD | 66,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1723` | 4,480,000.00 USD | 4,480,000.00 USD | 118,060.00 USD | 0.00 USD | 208,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1726` | 2,410,000.00 USD | 2,410,000.00 USD | 8,230.00 USD | 0.00 USD | 12,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1729` | 2,430,000.00 USD | 2,430,000.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1729` | 4,620,000.00 USD | 4,620,000.00 USD | 137,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1732` | 2,450,000.00 USD | 2,450,000.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1732` | 4,960,000.00 USD | 4,960,000.00 USD | 338,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1735` | 2,470,000.00 USD | 2,470,000.00 USD | 14,970.00 USD | 9,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1738` | 2,490,000.00 USD | 2,490,000.00 USD | 14,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1738` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 83,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1741` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 1,600.00 USD | 9,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1744` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 2,460.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1744` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1747` | 2,550,000.00 USD | 2,550,000.00 USD | 8,530.00 USD | 0.00 USD | 31,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1750` | 2,660,000.00 USD | 2,660,000.00 USD | 80,070.00 USD | 2,280.00 USD | 22,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1750` | 5,300,000.00 USD | 5,300,000.00 USD | 69,520.00 USD | 0.00 USD | 175,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1753` | 2,720,000.00 USD | 2,720,000.00 USD | 28,350.00 USD | 0.00 USD | 33,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1753` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 191,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1755` | 600.46 USD | 6,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1756` | 2,820,000.00 USD | 2,820,000.00 USD | 23,610.00 USD | 27,640.00 USD | 52,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1756` | 5,690,000.00 USD | 5,690,000.00 USD | 97,570.00 USD | 0.00 USD | 106,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1759` | 2,960,000.00 USD | 2,960,000.00 USD | 67,780.00 USD | 28,370.00 USD | 36,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1759` | 5,950,000.00 USD | 5,950,000.00 USD | 217,800.00 USD | 38,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1762` | 3,180,000.00 USD | 3,180,000.00 USD | 72,450.00 USD | 80,960.00 USD | 66,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1762` | 6,450,000.00 USD | 6,450,000.00 USD | 289,660.00 USD | 180,810.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1765` | 3,270,000.00 USD | 3,270,000.00 USD | 20,220.00 USD | 28,990.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1765` | 6,820,000.00 USD | 6,820,000.00 USD | 154,540.00 USD | 166,180.00 USD | 48,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1765` | 339.06 USD | 6,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1768` | 3,440,000.00 USD | 3,440,000.00 USD | 19,860.00 USD | 83,210.00 USD | 62,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1768` | 7,130,000.00 USD | 7,130,000.00 USD | 161,560.00 USD | 128,410.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1771` | 3,520,000.00 USD | 3,520,000.00 USD | 43,430.00 USD | 19,520.00 USD | 24,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1771` | 7,320,000.00 USD | 7,320,000.00 USD | 69,030.00 USD | 99,310.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1774` | 3,600,000.00 USD | 3,600,000.00 USD | 17,210.00 USD | 30,630.00 USD | 26,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1774` | 7,550,000.00 USD | 7,550,000.00 USD | 148,780.00 USD | 80,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1777` | 3,770,000.00 USD | 3,770,000.00 USD | 62,080.00 USD | 81,500.00 USD | 24,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1777` | 7,720,000.00 USD | 7,720,000.00 USD | 67,350.00 USD | 40,700.00 USD | 59,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1780` | 3,800,000.00 USD | 3,800,000.00 USD | 11,580.00 USD | 9,760.00 USD | 13,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1780` | 7,910,000.00 USD | 7,910,000.00 USD | 52,730.00 USD | 38,910.00 USD | 97,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1783` | 3,940,000.00 USD | 3,940,000.00 USD | 96,550.00 USD | 18,740.00 USD | 23,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1783` | 8,110,000.00 USD | 8,110,000.00 USD | 117,540.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1786` | 4,050,000.00 USD | 4,050,000.00 USD | 51,250.00 USD | 42,320.00 USD | 18,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1786` | 8,300,000.00 USD | 8,300,000.00 USD | 129,440.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1789` | 4,140,000.00 USD | 4,140,000.00 USD | 15,890.00 USD | 45,400.00 USD | 30,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1789` | 8,360,000.00 USD | 8,360,000.00 USD | 48,810.00 USD | 7,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1792` | 4,220,000.00 USD | 4,220,000.00 USD | 35,030.00 USD | 19,650.00 USD | 22,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1792` | 8,540,000.00 USD | 8,540,000.00 USD | 134,000.00 USD | 39,820.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1795` | 4,350,000.00 USD | 4,350,000.00 USD | 53,160.00 USD | 52,210.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1795` | 8,620,000.00 USD | 8,620,000.00 USD | 17,130.00 USD | 19,870.00 USD | 44,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1795` | 48,610.00 USD | 55,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1798` | 4,410,000.00 USD | 4,410,000.00 USD | 15,420.00 USD | 17,120.00 USD | 25,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1798` | 8,650,000.00 USD | 8,650,000.00 USD | 0.00 USD | 6,240.00 USD | 27,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1801` | 4,460,000.00 USD | 4,460,000.00 USD | 12,470.00 USD | 23,820.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1801` | 8,770,000.00 USD | 8,770,000.00 USD | 19,430.00 USD | 40,090.00 USD | 55,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1804` | 4,510,000.00 USD | 4,510,000.00 USD | 10,530.00 USD | 16,830.00 USD | 19,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1804` | 8,840,000.00 USD | 8,840,000.00 USD | 28,790.00 USD | 27,450.00 USD | 14,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1805` | 3,130.00 USD | 58,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1807` | 4,560,000.00 USD | 4,560,000.00 USD | 16,640.00 USD | 20,670.00 USD | 9,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1807` | 8,980,000.00 USD | 8,980,000.00 USD | 11,410.00 USD | 63,170.00 USD | 67,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1810` | 4,610,000.00 USD | 4,610,000.00 USD | 22,880.00 USD | 21,430.00 USD | 12,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1810` | 9,100,000.00 USD | 9,100,000.00 USD | 79,380.00 USD | 30,940.00 USD | 12,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1813` | 4,690,000.00 USD | 4,690,000.00 USD | 14,660.00 USD | 37,850.00 USD | 25,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1813` | 9,210,000.00 USD | 9,210,000.00 USD | 32,530.00 USD | 15,780.00 USD | 56,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1815` | 8,150.00 USD | 66,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1816` | 4,740,000.00 USD | 4,740,000.00 USD | 36,710.00 USD | 0.00 USD | 15,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1816` | 9,300,000.00 USD | 9,300,000.00 USD | 46,430.00 USD | 21,200.00 USD | 25,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1819` | 4,800,000.00 USD | 4,800,000.00 USD | 28,010.00 USD | 19,050.00 USD | 8,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1819` | 9,440,000.00 USD | 9,440,000.00 USD | 65,350.00 USD | 24,720.00 USD | 43,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1822` | 4,840,000.00 USD | 4,840,000.00 USD | 7,170.00 USD | 21,610.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1822` | 9,610,000.00 USD | 9,610,000.00 USD | 46,760.00 USD | 36,230.00 USD | 92,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1825` | 4,890,000.00 USD | 4,890,000.00 USD | 29,450.00 USD | 8,890.00 USD | 11,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1825` | 9,710,000.00 USD | 9,710,000.00 USD | 61,720.00 USD | 17,120.00 USD | 20,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1828` | 4,910,000.00 USD | 4,910,000.00 USD | 6,840.00 USD | 6,860.00 USD | 4,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1828` | 9,860,000.00 USD | 9,860,000.00 USD | 51,470.00 USD | 24,320.00 USD | 69,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1831` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 4,510.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1831` | 10,030,000.00 USD | 10,030,000.00 USD | 85,970.00 USD | 21,930.00 USD | 63,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1834` | 4,930,000.00 USD | 4,930,000.00 USD | 2,670.00 USD | 0.00 USD | 5,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1834` | 10,290,000.00 USD | 10,290,000.00 USD | 165,640.00 USD | 47,980.00 USD | 51,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1837` | 4,930,000.00 USD | 4,930,000.00 USD | 3,610.00 USD | 2,640.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1837` | 10,520,000.00 USD | 10,520,000.00 USD | 72,930.00 USD | 76,140.00 USD | 83,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1840` | 4,950,000.00 USD | 4,950,000.00 USD | 5,430.00 USD | 640.88 USD | 7,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1840` | 10,750,000.00 USD | 10,750,000.00 USD | 98,270.00 USD | 47,250.00 USD | 80,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1843` | 4,950,000.00 USD | 4,950,000.00 USD | 1,030.00 USD | 3,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1843` | 10,920,000.00 USD | 10,920,000.00 USD | 86,180.00 USD | 18,570.00 USD | 69,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1846` | 4,960,000.00 USD | 4,960,000.00 USD | 4,610.00 USD | 4,630.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1846` | 10,970,000.00 USD | 10,970,000.00 USD | 8,330.00 USD | 10,850.00 USD | 27,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1849` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 5,200.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1849` | 11,130,000.00 USD | 11,130,000.00 USD | 40,900.00 USD | 79,580.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1852` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 2,580.00 USD | 1,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1852` | 11,530,000.00 USD | 11,530,000.00 USD | 153,970.00 USD | 9,590.00 USD | 234,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1855` | 4,990,000.00 USD | 4,990,000.00 USD | 7,630.00 USD | 0.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1855` | 11,690,000.00 USD | 11,690,000.00 USD | 58,210.00 USD | 10,160.00 USD | 94,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1858` | 5,020,000.00 USD | 5,020,000.00 USD | 10,290.00 USD | 4,100.00 USD | 14,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1858` | 11,940,000.00 USD | 11,940,000.00 USD | 83,950.00 USD | 46,830.00 USD | 118,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1861` | 5,030,000.00 USD | 5,030,000.00 USD | 5,860.00 USD | 2,970.00 USD | 5,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1861` | 12,070,000.00 USD | 12,070,000.00 USD | 62,500.00 USD | 44,630.00 USD | 21,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1864` | 5,040,000.00 USD | 5,040,000.00 USD | 1,870.00 USD | 0.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1864` | 12,200,000.00 USD | 12,200,000.00 USD | 29,120.00 USD | 40,910.00 USD | 61,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1867` | 5,050,000.00 USD | 5,050,000.00 USD | 3,300.00 USD | 0.00 USD | 8,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1867` | 12,400,000.00 USD | 12,400,000.00 USD | 102,440.00 USD | 43,150.00 USD | 52,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1870` | 5,070,000.00 USD | 5,070,000.00 USD | 4,960.00 USD | 5,040.00 USD | 8,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1870` | 12,740,000.00 USD | 12,740,000.00 USD | 165,360.00 USD | 76,080.00 USD | 101,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1871` | 5,080,000.00 USD | 5,080,000.00 USD | 6,990.00 USD | 1,900.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1873` | 13,000,000.00 USD | 13,000,000.00 USD | 72,410.00 USD | 96,100.00 USD | 90,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1875` | 21,190.00 USD | 87,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1876` | 13,090,000.00 USD | 13,090,000.00 USD | 48,680.00 USD | 29,240.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1879` | 13,210,000.00 USD | 13,210,000.00 USD | 57,250.00 USD | 32,940.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1882` | 13,240,000.00 USD | 13,240,000.00 USD | 14,000.00 USD | 6,530.00 USD | 5,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1885` | 13,280,000.00 USD | 13,280,000.00 USD | 9,250.00 USD | 31,900.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1888` | 13,400,000.00 USD | 13,400,000.00 USD | 13,720.00 USD | 17,330.00 USD | 83,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1891` | 13,450,000.00 USD | 13,450,000.00 USD | 36,740.00 USD | 0.00 USD | 17,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1894` | 13,540,000.00 USD | 13,540,000.00 USD | 58,980.00 USD | 12,420.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1895` | 3,550.00 USD | 91,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1897` | 13,600,000.00 USD | 13,600,000.00 USD | 6,950.00 USD | 33,930.00 USD | 25,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1900` | 13,630,000.00 USD | 13,630,000.00 USD | 0.00 USD | 12,490.00 USD | 14,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1903` | 13,670,000.00 USD | 13,670,000.00 USD | 14,330.00 USD | 11,220.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1906` | 13,750,000.00 USD | 13,750,000.00 USD | 18,470.00 USD | 27,580.00 USD | 33,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1909` | 13,810,000.00 USD | 13,810,000.00 USD | 15,470.00 USD | 29,160.00 USD | 19,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1912` | 13,830,000.00 USD | 13,830,000.00 USD | 0.00 USD | 15,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1915` | 13,840,000.00 USD | 13,840,000.00 USD | 7,460.00 USD | 5,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1918` | 13,860,000.00 USD | 13,860,000.00 USD | 0.00 USD | 11,840.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1924` | 13,880,000.00 USD | 13,880,000.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1927` | 13,910,000.00 USD | 13,910,000.00 USD | 11,600.00 USD | 13,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1945` | 13,910,000.00 USD | 13,910,000.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1945` | 1,310.00 USD | 92,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1951` | 13,920,000.00 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1955` | 860.20 USD | 93,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1975` | 150.10 USD | 93,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1995` | 135.22 USD | 93,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2025` | 764.66 USD | 94,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2045` | 399.22 USD | 94,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2055` | 11,590.00 USD | 106,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2085` | 198.08 USD | 106,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2095` | 1,060.00 USD | 107,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2135` | 16,070.00 USD | 123,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 41,330.00 USD | 164,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2195` | 131,700.00 USD | 296,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 26,940.00 USD | 323,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2255` | 154.78 USD | 323,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 6,820.00 USD | 330,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 16,250.00 USD | 346,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 102.62 USD | 346,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 361.66 USD | 347,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 869.00 USD | 348,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2445` | 231.03 USD | 348,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2465` | 9,360.00 USD | 357,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2485` | 21,600.00 USD | 379,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2545` | 546.54 USD | 379,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 3,870.00 USD | 383,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2575` | 29,500.00 USD | 413,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 52,030.00 USD | 465,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 154.94 USD | 465,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2685` | 226.51 USD | 465,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 13,510.00 USD | 479,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 214.21 USD | 479,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 27,890.00 USD | 507,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2755` | 438.18 USD | 507,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2795` | 482.84 USD | 508,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 187.26 USD | 508,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2925` | 2,230.00 USD | 510,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 574.36 USD | 511,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2985` | 17,550.00 USD | 528,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 225.42 USD | 529,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3165` | 63,300.00 USD | 592,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 9,540.00 USD | 601,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3305` | 192.68 USD | 602,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3325` | 148.36 USD | 602,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3335` | 258.73 USD | 602,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3365` | 63,220.00 USD | 665,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0345` | 2,320,000.00 USD | 0.00 USD | 1,180.00 USD | `-79.50%` | `34,249,500,000,000.00` |
| `Live` | `Long` | `0.0375` | 2,320,000.00 USD | 0.00 USD | 2,200.00 USD | `-77.72%` | `58,778,900,000,000.00` |
| `Live` | `Long` | `0.0385` | 2,310,000.00 USD | 0.00 USD | 1,490.00 USD | `-77.13%` | `38,823,900,000,000.00` |
| `Live` | `Long` | `0.0395` | 2,310,000.00 USD | 0.00 USD | 138,900.00 USD | `-76.53%` | `3,516,409,800,000,000.00` |
| `Live` | `Long` | `0.0415` | 2,170,000.00 USD | 0.00 USD | 408.10 USD | `-75.34%` | `9,833,800,000,000.00` |
| `Live` | `Long` | `0.0425` | 2,170,000.00 USD | 0.00 USD | 170.00 USD | `-74.75%` | `4,000,000,000,000.00` |
| `Live` | `Long` | `0.0445` | 2,170,000.00 USD | 0.00 USD | 8,100.00 USD | `-73.56%` | `181,960,400,000,000.00` |
| `Live` | `Long` | `0.0455` | 2,160,000.00 USD | 0.00 USD | 3,090.00 USD | `-72.97%` | `67,875,300,000,000.00` |
| `Live` | `Long` | `0.0475` | 2,160,000.00 USD | 0.00 USD | 4,840.00 USD | `-71.78%` | `101,831,000,000,000.00` |
| `Live` | `Long` | `0.0495` | 2,160,000.00 USD | 0.00 USD | 400.94 USD | `-70.59%` | `8,099,700,000,000.00` |
| `Live` | `Long` | `0.0525` | 2,160,000.00 USD | 0.00 USD | 289.43 USD | `-68.81%` | `5,513,000,000,000.00` |
| `Live` | `Long` | `0.0535` | 2,160,000.00 USD | 0.00 USD | 668.38 USD | `-68.22%` | `12,493,000,000,000.00` |
| `Live` | `Long` | `0.0545` | 2,160,000.00 USD | 0.00 USD | 7,100.00 USD | `-67.62%` | `130,366,100,000,000.00` |
| `Live` | `Long` | `0.0565` | 2,150,000.00 USD | 0.00 USD | 18,660.00 USD | `-66.43%` | `330,349,600,000,000.00` |
| `Live` | `Long` | `0.0605` | 2,130,000.00 USD | 0.00 USD | 148.49 USD | `-64.06%` | `2,454,400,000,000.00` |
| `Live` | `Long` | `0.0625` | 2,130,000.00 USD | 0.00 USD | 187.50 USD | `-62.87%` | `3,000,000,000,000.00` |
| `Live` | `Long` | `0.0645` | 2,130,000.00 USD | 0.00 USD | 283.15 USD | `-61.68%` | `4,389,900,000,000.00` |
| `Live` | `Long` | `0.0675` | 2,130,000.00 USD | 0.00 USD | 100,530.00 USD | `-59.90%` | `1,489,314,300,000,000.00` |
| `Live` | `Long` | `0.0685` | 2,030,000.00 USD | 0.00 USD | 590.45 USD | `-59.30%` | `8,619,700,000,000.00` |
| `Live` | `Long` | `0.0695` | 2,030,000.00 USD | 0.00 USD | 77,980.00 USD | `-58.71%` | `1,122,070,000,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,950,000.00 USD | 0.00 USD | 3,260.00 USD | `-58.12%` | `46,211,100,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,950,000.00 USD | 0.00 USD | 5,840.00 USD | `-57.52%` | `81,674,400,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,940,000.00 USD | 0.00 USD | 111.58 USD | `-56.93%` | `1,539,100,000,000.00` |
| `Live` | `Long` | `0.0735` | 1,940,000.00 USD | 0.00 USD | 2,440.00 USD | `-56.33%` | `33,161,800,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,940,000.00 USD | 0.00 USD | 2,370.00 USD | `-55.74%` | `31,857,600,000,000.00` |
| `Live` | `Long` | `0.0755` | 1,940,000.00 USD | 0.00 USD | 368.95 USD | `-55.14%` | `4,886,800,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,940,000.00 USD | 0.00 USD | 14,690.00 USD | `-54.55%` | `192,029,300,000,000.00` |
| `Live` | `Long` | `0.0785` | 1,920,000.00 USD | 0.00 USD | 27,480.00 USD | `-53.36%` | `350,000,000,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,890,000.00 USD | 0.00 USD | 6,180.00 USD | `-52.77%` | `77,676,300,000,000.00` |
| `Live` | `Long` | `0.0805` | 1,890,000.00 USD | 0.00 USD | 6,040.00 USD | `-52.17%` | `75,000,000,000,000.00` |
| `Live` | `Long` | `0.0815` | 1,880,000.00 USD | 0.00 USD | 7,840.00 USD | `-51.58%` | `96,199,600,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,870,000.00 USD | 0.00 USD | 13,950.00 USD | `-50.99%` | `169,093,500,000,000.00` |
| `Live` | `Long` | `0.0835` | 1,860,000.00 USD | 0.00 USD | 751.50 USD | `-50.39%` | `9,000,000,000,000.00` |
| `Live` | `Long` | `0.0845` | 1,860,000.00 USD | 0.00 USD | 19,010.00 USD | `-49.80%` | `224,937,400,000,000.00` |
| `Live` | `Long` | `0.0875` | 1,840,000.00 USD | 0.00 USD | 22,430.00 USD | `-48.02%` | `256,311,700,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,820,000.00 USD | 0.00 USD | 362.62 USD | `-47.42%` | `4,097,400,000,000.00` |
| `Live` | `Long` | `0.0895` | 1,820,000.00 USD | 0.00 USD | 12,960.00 USD | `-46.83%` | `144,809,100,000,000.00` |
| `Live` | `Long` | `0.0905` | 1,800,000.00 USD | 0.00 USD | 1,320.00 USD | `-46.23%` | `14,542,300,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,800,000.00 USD | 0.00 USD | 4,130.00 USD | `-45.05%` | `44,668,100,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,800,000.00 USD | 0.00 USD | 814.24 USD | `-44.45%` | `8,708,500,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,800,000.00 USD | 0.00 USD | 4,090.00 USD | `-43.86%` | `43,276,200,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,790,000.00 USD | 0.00 USD | 589.63 USD | `-42.67%` | `6,110,200,000,000.00` |
| `Live` | `Long` | `0.0975` | 1,790,000.00 USD | 0.00 USD | 145.24 USD | `-42.07%` | `1,489,600,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,790,000.00 USD | 0.00 USD | 5,970.00 USD | `-41.48%` | `60,604,700,000,000.00` |
| `Live` | `Long` | `0.0995` | 1,790,000.00 USD | 0.00 USD | 9,200.00 USD | `-40.89%` | `92,500,600,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,780,000.00 USD | 0.00 USD | 12,790.00 USD | `-40.29%` | `127,282,000,000,000.00` |
| `Live` | `Long` | `0.1025` | 1,760,000.00 USD | 0.00 USD | 811.82 USD | `-39.10%` | `7,920,200,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,760,000.00 USD | 0.00 USD | 802.14 USD | `-38.51%` | `7,750,100,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,760,000.00 USD | 0.00 USD | 6,700.00 USD | `-37.92%` | `64,126,500,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,760,000.00 USD | 0.00 USD | 12,770.00 USD | `-37.32%` | `121,051,500,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,740,000.00 USD | 0.00 USD | 181.20 USD | `-36.73%` | `1,701,400,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,740,000.00 USD | 0.00 USD | 1,650.00 USD | `-36.13%` | `15,369,200,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,740,000.00 USD | 0.00 USD | 342.59 USD | `-35.54%` | `3,157,500,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,740,000.00 USD | 0.00 USD | 534.49 USD | `-34.35%` | `4,837,000,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,740,000.00 USD | 0.00 USD | 425.50 USD | `-33.76%` | `3,816,100,000,000.00` |
| `Live` | `Long` | `0.1125` | 1,740,000.00 USD | 0.00 USD | 2,190.00 USD | `-33.16%` | `19,462,500,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,740,000.00 USD | 0.00 USD | 1,360.00 USD | `-32.57%` | `11,975,200,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,740,000.00 USD | 0.00 USD | 8,950.00 USD | `-31.97%` | `78,144,100,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,730,000.00 USD | 0.00 USD | 16,170.00 USD | `-31.38%` | `140,005,200,000,000.02` |
| `Live` | `Long` | `0.1165` | 1,710,000.00 USD | 0.00 USD | 11,120.00 USD | `-30.79%` | `95,487,400,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,700,000.00 USD | 0.00 USD | 1,760.00 USD | `-30.19%` | `14,957,100,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,700,000.00 USD | 0.00 USD | 26,260.00 USD | `-29.60%` | `221,634,600,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,670,000.00 USD | 0.00 USD | 6,210.00 USD | `-29.00%` | `51,981,200,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,670,000.00 USD | 0.00 USD | 14,190.00 USD | `-27.82%` | `116,753,600,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,650,000.00 USD | 0.00 USD | 8,920.00 USD | `-27.22%` | `72,830,700,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,640,000.00 USD | 0.00 USD | 34,620.00 USD | `-26.63%` | `280,295,400,000,000.03` |
| `Live` | `Long` | `0.1245` | 1,610,000.00 USD | 0.00 USD | 3,110.00 USD | `-26.03%` | `24,990,900,000,000.00` |
| `Live` | `Long` | `0.1255` | 1,610,000.00 USD | 0.00 USD | 4,960.00 USD | `-25.44%` | `39,542,400,000,000.00` |
| `Live` | `Long` | `0.1265` | 1,600,000.00 USD | 0.00 USD | 1,200.00 USD | `-24.85%` | `9,489,700,000,000.00` |
| `Live` | `Long` | `0.1275` | 1,600,000.00 USD | 0.00 USD | 4,190.00 USD | `-24.25%` | `32,824,800,000,000.00` |
| `Live` | `Long` | `0.1285` | 1,600,000.00 USD | 0.00 USD | 11,100.00 USD | `-23.66%` | `86,356,500,000,000.00` |
| `Live` | `Long` | `0.1295` | 1,580,000.00 USD | 0.00 USD | 4,010.00 USD | `-23.06%` | `30,998,800,000,000.00` |
| `Live` | `Long` | `0.1305` | 1,580,000.00 USD | 0.00 USD | 13,600.00 USD | `-22.47%` | `104,183,100,000,000.00` |
| `Live` | `Long` | `0.1315` | 1,570,000.00 USD | 0.00 USD | 10,500.00 USD | `-21.87%` | `79,839,800,000,000.00` |
| `Live` | `Long` | `0.1325` | 1,560,000.00 USD | 0.00 USD | 8,090.00 USD | `-21.28%` | `61,058,900,000,000.00` |
| `Live` | `Long` | `0.1335` | 1,550,000.00 USD | 0.00 USD | 26,200.00 USD | `-20.69%` | `196,263,500,000,000.00` |
| `Live` | `Long` | `0.1345` | 1,520,000.00 USD | 0.00 USD | 2,970.00 USD | `-20.09%` | `22,103,800,000,000.00` |
| `Live` | `Long` | `0.1365` | 1,520,000.00 USD | 0.00 USD | 2,740.00 USD | `-18.90%` | `20,075,400,000,000.00` |
| `Live` | `Long` | `0.1375` | 1,520,000.00 USD | 0.00 USD | 13,750.00 USD | `-18.31%` | `100,000,000,000,000.00` |
| `Live` | `Long` | `0.1385` | 1,500,000.00 USD | 0.00 USD | 5,340.00 USD | `-17.72%` | `38,544,200,000,000.00` |
| `Live` | `Long` | `0.1395` | 1,500,000.00 USD | 0.00 USD | 6,710.00 USD | `-17.12%` | `48,115,200,000,000.00` |
| `Live` | `Long` | `0.1405` | 1,490,000.00 USD | 0.00 USD | 2,800.00 USD | `-16.53%` | `19,894,100,000,000.00` |
| `Live` | `Long` | `0.1415` | 1,490,000.00 USD | 0.00 USD | 75,150.00 USD | `-15.93%` | `531,086,900,000,000.00` |
| `Live` | `Long` | `0.1425` | 1,410,000.00 USD | 0.00 USD | 490,800.00 USD | `-15.34%` | `3,444,196,100,000,000.00` |
| `Live` | `Long` | `0.1435` | 921,750.00 USD | 0.00 USD | 19,330.00 USD | `-14.75%` | `134,671,900,000,000.00` |
| `Live` | `Long` | `0.1445` | 902,420.00 USD | 0.00 USD | 53,790.00 USD | `-14.15%` | `372,262,000,000,000.00` |
| `Live` | `Long` | `0.1455` | 848,630.00 USD | 0.00 USD | 106.39 USD | `-13.56%` | `731,200,000,000.00` |
| `Live` | `Long` | `0.1465` | 848,520.00 USD | 0.00 USD | 47,190.00 USD | `-12.96%` | `322,108,600,000,000.00` |
| `Live` | `Long` | `0.1475` | 801,340.00 USD | 0.00 USD | 73,750.00 USD | `-12.37%` | `500,000,000,000,000.00` |
| `Live` | `Long` | `0.1485` | 727,590.00 USD | 0.00 USD | 2,650.00 USD | `-11.78%` | `17,872,100,000,000.00` |
| `Live` | `Long` | `0.1495` | 724,930.00 USD | 0.00 USD | 35,860.00 USD | `-11.18%` | `239,861,300,000,000.00` |
| `Live` | `Long` | `0.1505` | 689,070.00 USD | 0.00 USD | 102,290.00 USD | `-10.59%` | `679,673,200,000,000.00` |
| `Live` | `Long` | `0.1515` | 586,780.00 USD | 0.00 USD | 9,900.00 USD | `-9.99%` | `65,345,600,000,000.00` |
| `Live` | `Long` | `0.1525` | 576,880.00 USD | 0.00 USD | 42,800.00 USD | `-9.40%` | `280,626,000,000,000.00` |
| `Live` | `Long` | `0.1535` | 534,090.00 USD | 0.00 USD | 189,960.00 USD | `-8.80%` | `1,237,517,800,000,000.00` |
| `Live` | `Long` | `0.1545` | 344,130.00 USD | 0.00 USD | 26,170.00 USD | `-8.21%` | `169,378,600,000,000.00` |
| `Live` | `Long` | `0.1555` | 317,960.00 USD | 0.00 USD | 39,570.00 USD | `-7.62%` | `254,462,900,000,000.00` |
| `Live` | `Long` | `0.1565` | 278,390.00 USD | 0.00 USD | 23,920.00 USD | `-7.02%` | `152,866,400,000,000.00` |
| `Live` | `Long` | `0.1575` | 254,470.00 USD | 0.00 USD | 4,940.00 USD | `-6.43%` | `31,351,900,000,000.00` |
| `Live` | `Long` | `0.1585` | 249,530.00 USD | 0.00 USD | 5,760.00 USD | `-5.83%` | `36,335,900,000,000.00` |
| `Live` | `Long` | `0.1595` | 243,770.00 USD | 0.00 USD | 63,000.00 USD | `-5.24%` | `395,011,700,000,000.00` |
| `Live` | `Long` | `0.1605` | 180,760.00 USD | 0.00 USD | 37,640.00 USD | `-4.65%` | `234,510,900,000,000.00` |
| `Live` | `Long` | `0.1615` | 143,120.00 USD | 0.00 USD | 17,290.00 USD | `-4.05%` | `107,085,500,000,000.00` |
| `Live` | `Long` | `0.1625` | 125,830.00 USD | 0.00 USD | 106,340.00 USD | `-3.46%` | `654,420,200,000,000.00` |
| `Live` | `Long` | `0.1635` | 19,490.00 USD | 0.00 USD | 1,230.00 USD | `-2.86%` | `7,496,400,000,000.00` |
| `Live` | `Long` | `0.1645` | 18,260.00 USD | 0.00 USD | 6,190.00 USD | `-2.27%` | `37,630,200,000,000.00` |
| `Live` | `Long` | `0.1655` | 12,070.00 USD | 0.00 USD | 12,070.00 USD | `-1.68%` | `72,938,600,000,000.00` |
| `Live` | `Short` | `0.1685` | 5,550.00 USD | 5,550.00 USD | 0.00 USD | `+0.11%` | `32,933,400,000,000.00` |
| `Live` | `Short` | `0.1755` | 6,150.00 USD | 600.46 USD | 0.00 USD | `+4.27%` | `3,421,400,000,000.00` |
| `Live` | `Short` | `0.1765` | 6,490.00 USD | 339.06 USD | 0.00 USD | `+4.86%` | `1,921,000,000,000.00` |
| `Live` | `Short` | `0.1795` | 55,100.00 USD | 48,610.00 USD | 0.00 USD | `+6.64%` | `270,803,800,000,000.00` |
| `Live` | `Short` | `0.1805` | 58,220.00 USD | 3,130.00 USD | 0.00 USD | `+7.24%` | `17,317,400,000,000.00` |
| `Live` | `Short` | `0.1815` | 66,380.00 USD | 8,150.00 USD | 0.00 USD | `+7.83%` | `44,917,400,000,000.00` |
| `Live` | `Short` | `0.1875` | 87,560.00 USD | 21,190.00 USD | 0.00 USD | `+11.39%` | `112,997,300,000,000.00` |
| `Live` | `Short` | `0.1895` | 91,110.00 USD | 3,550.00 USD | 0.00 USD | `+12.58%` | `18,740,300,000,000.00` |
| `Live` | `Short` | `0.1945` | 92,430.00 USD | 1,310.00 USD | 0.00 USD | `+15.55%` | `6,741,400,000,000.00` |
| `Live` | `Short` | `0.1955` | 93,290.00 USD | 860.20 USD | 0.00 USD | `+16.15%` | `4,400,000,000,000.00` |
| `Live` | `Short` | `0.1975` | 93,440.00 USD | 150.10 USD | 0.00 USD | `+17.34%` | `760,000,000,000.00` |
| `Live` | `Short` | `0.1995` | 93,570.00 USD | 135.22 USD | 0.00 USD | `+18.52%` | `677,800,000,000.00` |
| `Live` | `Short` | `0.2025` | 94,340.00 USD | 764.66 USD | 0.00 USD | `+20.31%` | `3,776,100,000,000.00` |
| `Live` | `Short` | `0.2045` | 94,740.00 USD | 399.22 USD | 0.00 USD | `+21.49%` | `1,952,200,000,000.00` |
| `Live` | `Short` | `0.2055` | 106,330.00 USD | 11,590.00 USD | 0.00 USD | `+22.09%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2085` | 106,530.00 USD | 198.08 USD | 0.00 USD | `+23.87%` | `950,000,000,000.00` |
| `Live` | `Short` | `0.2095` | 107,580.00 USD | 1,060.00 USD | 0.00 USD | `+24.47%` | `5,056,300,000,000.00` |
| `Live` | `Short` | `0.2135` | 123,660.00 USD | 16,070.00 USD | 0.00 USD | `+26.84%` | `75,287,100,000,000.00` |
| `Live` | `Short` | `0.2155` | 164,990.00 USD | 41,330.00 USD | 0.00 USD | `+28.03%` | `191,801,700,000,000.00` |
| `Live` | `Short` | `0.2195` | 296,690.00 USD | 131,700.00 USD | 0.00 USD | `+30.41%` | `600,003,000,000,000.00` |
| `Live` | `Short` | `0.2235` | 323,630.00 USD | 26,940.00 USD | 0.00 USD | `+32.78%` | `120,527,600,000,000.00` |
| `Live` | `Short` | `0.2255` | 323,790.00 USD | 154.78 USD | 0.00 USD | `+33.97%` | `686,400,000,000.00` |
| `Live` | `Short` | `0.2295` | 330,610.00 USD | 6,820.00 USD | 0.00 USD | `+36.35%` | `29,727,000,000,000.00` |
| `Live` | `Short` | `0.2355` | 346,860.00 USD | 16,250.00 USD | 0.00 USD | `+39.91%` | `69,017,500,000,000.00` |
| `Live` | `Short` | `0.2375` | 346,960.00 USD | 102.62 USD | 0.00 USD | `+41.10%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2405` | 347,330.00 USD | 361.66 USD | 0.00 USD | `+42.88%` | `1,503,800,000,000.00` |
| `Live` | `Short` | `0.2425` | 348,190.00 USD | 869.00 USD | 0.00 USD | `+44.07%` | `3,583,500,000,000.00` |
| `Live` | `Short` | `0.2445` | 348,430.00 USD | 231.03 USD | 0.00 USD | `+45.26%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2465` | 357,790.00 USD | 9,360.00 USD | 0.00 USD | `+46.45%` | `37,972,200,000,000.00` |
| `Live` | `Short` | `0.2485` | 379,380.00 USD | 21,600.00 USD | 0.00 USD | `+47.64%` | `86,908,000,000,000.00` |
| `Live` | `Short` | `0.2545` | 379,930.00 USD | 546.54 USD | 0.00 USD | `+51.20%` | `2,147,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 383,790.00 USD | 3,870.00 USD | 0.00 USD | `+52.39%` | `15,070,700,000,000.00` |
| `Live` | `Short` | `0.2575` | 413,290.00 USD | 29,500.00 USD | 0.00 USD | `+52.98%` | `114,561,100,000,000.00` |
| `Live` | `Short` | `0.2585` | 465,320.00 USD | 52,030.00 USD | 0.00 USD | `+53.58%` | `201,260,100,000,000.00` |
| `Live` | `Short` | `0.2615` | 465,470.00 USD | 154.94 USD | 0.00 USD | `+55.36%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2685` | 465,700.00 USD | 226.51 USD | 0.00 USD | `+59.52%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2715` | 479,210.00 USD | 13,510.00 USD | 0.00 USD | `+61.30%` | `49,773,600,000,000.00` |
| `Live` | `Short` | `0.2725` | 479,430.00 USD | 214.21 USD | 0.00 USD | `+61.89%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 507,320.00 USD | 27,890.00 USD | 0.00 USD | `+63.08%` | `101,607,700,000,000.00` |
| `Live` | `Short` | `0.2755` | 507,760.00 USD | 438.18 USD | 0.00 USD | `+63.68%` | `1,590,500,000,000.00` |
| `Live` | `Short` | `0.2795` | 508,240.00 USD | 482.84 USD | 0.00 USD | `+66.05%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2915` | 508,430.00 USD | 187.26 USD | 0.00 USD | `+73.18%` | `642,400,000,000.00` |
| `Live` | `Short` | `0.2925` | 510,650.00 USD | 2,230.00 USD | 0.00 USD | `+73.78%` | `7,608,100,000,000.00` |
| `Live` | `Short` | `0.2955` | 511,230.00 USD | 574.36 USD | 0.00 USD | `+75.56%` | `1,943,700,000,000.00` |
| `Live` | `Short` | `0.2985` | 528,780.00 USD | 17,550.00 USD | 0.00 USD | `+77.34%` | `58,786,700,000,000.00` |
| `Live` | `Short` | `0.3105` | 529,000.00 USD | 225.42 USD | 0.00 USD | `+84.47%` | `726,000,000,000.00` |
| `Live` | `Short` | `0.3165` | 592,300.00 USD | 63,300.00 USD | 0.00 USD | `+88.03%` | `200,000,000,000,000.00` |
| `Live` | `Short` | `0.3295` | 601,840.00 USD | 9,540.00 USD | 0.00 USD | `+95.76%` | `28,943,600,000,000.00` |
| `Live` | `Short` | `0.3305` | 602,030.00 USD | 192.68 USD | 0.00 USD | `+96.35%` | `583,000,000,000.00` |
| `Live` | `Short` | `0.3325` | 602,180.00 USD | 148.36 USD | 0.00 USD | `+97.54%` | `446,200,000,000.00` |
| `Live` | `Short` | `0.3335` | 602,440.00 USD | 258.73 USD | 0.00 USD | `+98.13%` | `775,800,000,000.00` |
| `Live` | `Short` | `0.3365` | 665,660.00 USD | 63,220.00 USD | 0.00 USD | `+99.92%` | `187,887,700,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.1341` | 653,470.00 USD | 0.00 USD | 653,470.00 USD | 3,550.00 USD | 1,460.00 USD | 3,640.00 USD |
| `7D` | `0.1341` | 694,940.00 USD | 0.00 USD | 694,940.00 USD | 3,550.00 USD | 1,460.00 USD | 3,640.00 USD |
| `1D` | `0.1344` | 644,820.00 USD | 0.00 USD | 644,820.00 USD | 0.00 USD | 691.54 USD | 598.60 USD |
| `7D` | `0.1344` | 686,280.00 USD | 0.00 USD | 686,280.00 USD | 0.00 USD | 691.54 USD | 598.60 USD |
| `1D` | `0.1347` | 643,530.00 USD | 0.00 USD | 643,530.00 USD | 0.00 USD | 0.00 USD | 670.19 USD |
| `7D` | `0.1347` | 684,990.00 USD | 0.00 USD | 684,990.00 USD | 0.00 USD | 0.00 USD | 670.19 USD |
| `1D` | `0.1350` | 642,860.00 USD | 0.00 USD | 642,860.00 USD | 5,030.00 USD | 1,310.00 USD | 6,250.00 USD |
| `7D` | `0.1350` | 684,320.00 USD | 0.00 USD | 684,320.00 USD | 5,030.00 USD | 1,310.00 USD | 6,250.00 USD |
| `1D` | `0.1353` | 630,270.00 USD | 0.00 USD | 630,270.00 USD | 3,530.00 USD | 1,430.00 USD | 2,910.00 USD |
| `7D` | `0.1353` | 671,730.00 USD | 0.00 USD | 671,730.00 USD | 3,530.00 USD | 1,430.00 USD | 2,910.00 USD |
| `1D` | `0.1356` | 622,410.00 USD | 0.00 USD | 622,410.00 USD | 932.52 USD | 0.00 USD | 4,150.00 USD |
| `7D` | `0.1356` | 663,870.00 USD | 0.00 USD | 663,870.00 USD | 932.52 USD | 0.00 USD | 4,150.00 USD |
| `1D` | `0.1359` | 617,330.00 USD | 0.00 USD | 617,330.00 USD | 2,480.00 USD | 869.31 USD | 4,230.00 USD |
| `7D` | `0.1359` | 658,790.00 USD | 0.00 USD | 658,790.00 USD | 2,480.00 USD | 869.31 USD | 4,230.00 USD |
| `1D` | `0.1362` | 609,750.00 USD | 0.00 USD | 609,750.00 USD | 4,890.00 USD | 950.53 USD | 2,660.00 USD |
| `7D` | `0.1362` | 651,210.00 USD | 0.00 USD | 651,210.00 USD | 4,890.00 USD | 950.53 USD | 2,660.00 USD |
| `1D` | `0.1365` | 601,250.00 USD | 0.00 USD | 601,250.00 USD | 1,340.00 USD | 1,900.00 USD | 1,150.00 USD |
| `7D` | `0.1365` | 642,710.00 USD | 0.00 USD | 642,710.00 USD | 1,340.00 USD | 1,900.00 USD | 1,150.00 USD |
| `1D` | `0.1368` | 596,870.00 USD | 0.00 USD | 596,870.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD |
| `7D` | `0.1368` | 638,330.00 USD | 0.00 USD | 638,330.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD |
| `1D` | `0.1371` | 595,130.00 USD | 0.00 USD | 595,130.00 USD | 3,680.00 USD | 1,110.00 USD | 2,240.00 USD |
| `7D` | `0.1371` | 636,590.00 USD | 0.00 USD | 636,590.00 USD | 3,680.00 USD | 1,110.00 USD | 2,240.00 USD |
| `1D` | `0.1374` | 588,090.00 USD | 0.00 USD | 588,090.00 USD | 1,790.00 USD | 2,220.00 USD | 0.00 USD |
| `7D` | `0.1374` | 629,560.00 USD | 0.00 USD | 629,560.00 USD | 1,790.00 USD | 2,220.00 USD | 0.00 USD |
| `1D` | `0.1377` | 584,090.00 USD | 0.00 USD | 584,090.00 USD | 936.88 USD | 821.64 USD | 536.58 USD |
| `7D` | `0.1377` | 625,550.00 USD | 0.00 USD | 625,550.00 USD | 936.88 USD | 821.64 USD | 536.58 USD |
| `1D` | `0.1380` | 581,790.00 USD | 0.00 USD | 581,790.00 USD | 3,510.00 USD | 7,310.00 USD | 1,020.00 USD |
| `7D` | `0.1380` | 623,260.00 USD | 0.00 USD | 623,260.00 USD | 3,510.00 USD | 7,310.00 USD | 1,020.00 USD |
| `1D` | `0.1383` | 569,960.00 USD | 0.00 USD | 569,960.00 USD | 2,370.00 USD | 640.93 USD | 5,220.00 USD |
| `7D` | `0.1383` | 611,420.00 USD | 0.00 USD | 611,420.00 USD | 2,370.00 USD | 640.93 USD | 5,220.00 USD |
| `1D` | `0.1386` | 561,720.00 USD | 0.00 USD | 561,720.00 USD | 0.00 USD | 2,090.00 USD | 2,250.00 USD |
| `7D` | `0.1386` | 603,190.00 USD | 0.00 USD | 603,190.00 USD | 0.00 USD | 2,090.00 USD | 2,250.00 USD |
| `1D` | `0.1389` | 557,380.00 USD | 0.00 USD | 557,380.00 USD | 5,190.00 USD | 524.77 USD | 0.00 USD |
| `7D` | `0.1389` | 598,840.00 USD | 0.00 USD | 598,840.00 USD | 5,190.00 USD | 524.77 USD | 0.00 USD |
| `1D` | `0.1392` | 551,660.00 USD | 0.00 USD | 551,660.00 USD | 0.00 USD | 1,440.00 USD | 1,020.00 USD |
| `7D` | `0.1392` | 593,120.00 USD | 0.00 USD | 593,120.00 USD | 0.00 USD | 1,440.00 USD | 1,020.00 USD |
| `1D` | `0.1395` | 549,200.00 USD | 0.00 USD | 549,200.00 USD | 0.00 USD | 6,230.00 USD | 0.00 USD |
| `7D` | `0.1395` | 590,660.00 USD | 0.00 USD | 590,660.00 USD | 0.00 USD | 6,230.00 USD | 0.00 USD |
| `1D` | `0.1398` | 542,970.00 USD | 0.00 USD | 542,970.00 USD | 6,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1398` | 584,430.00 USD | 0.00 USD | 584,430.00 USD | 6,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1401` | 536,080.00 USD | 0.00 USD | 536,080.00 USD | 1,990.00 USD | 2,100.00 USD | 0.00 USD |
| `7D` | `0.1401` | 577,540.00 USD | 0.00 USD | 577,540.00 USD | 1,990.00 USD | 2,100.00 USD | 0.00 USD |
| `1D` | `0.1404` | 531,980.00 USD | 0.00 USD | 531,980.00 USD | 0.00 USD | 966.86 USD | 2,000.00 USD |
| `7D` | `0.1404` | 573,440.00 USD | 0.00 USD | 573,440.00 USD | 0.00 USD | 966.86 USD | 2,000.00 USD |
| `1D` | `0.1410` | 529,010.00 USD | 0.00 USD | 529,010.00 USD | 0.00 USD | 0.00 USD | 1,070.00 USD |
| `7D` | `0.1410` | 570,480.00 USD | 0.00 USD | 570,480.00 USD | 0.00 USD | 0.00 USD | 1,070.00 USD |
| `1D` | `0.1413` | 527,950.00 USD | 0.00 USD | 527,950.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD |
| `7D` | `0.1413` | 569,410.00 USD | 0.00 USD | 569,410.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD |
| `1D` | `0.1422` | 525,540.00 USD | 0.00 USD | 525,540.00 USD | 4,030.00 USD | 2,310.00 USD | 6,410.00 USD |
| `7D` | `0.1422` | 567,000.00 USD | 0.00 USD | 567,000.00 USD | 4,030.00 USD | 2,310.00 USD | 6,410.00 USD |
| `1D` | `0.1434` | 512,790.00 USD | 0.00 USD | 512,790.00 USD | 3,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1434` | 554,260.00 USD | 0.00 USD | 554,260.00 USD | 3,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1443` | 508,900.00 USD | 0.00 USD | 508,900.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD |
| `7D` | `0.1443` | 550,360.00 USD | 0.00 USD | 550,360.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD |
| `1D` | `0.1452` | 506,760.00 USD | 0.00 USD | 506,760.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1452` | 548,230.00 USD | 0.00 USD | 548,230.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1464` | 503,770.00 USD | 0.00 USD | 503,770.00 USD | 0.00 USD | 0.00 USD | 1,990.00 USD |
| `7D` | `0.1464` | 545,230.00 USD | 0.00 USD | 545,230.00 USD | 0.00 USD | 0.00 USD | 1,990.00 USD |
| `1D` | `0.1467` | 501,780.00 USD | 0.00 USD | 501,780.00 USD | 3,740.00 USD | 2,700.00 USD | 5,670.00 USD |
| `7D` | `0.1467` | 543,250.00 USD | 0.00 USD | 543,250.00 USD | 3,740.00 USD | 2,700.00 USD | 5,670.00 USD |
| `1D` | `0.1470` | 489,670.00 USD | 0.00 USD | 489,670.00 USD | 8,350.00 USD | 4,180.00 USD | 5,200.00 USD |
| `7D` | `0.1470` | 531,140.00 USD | 0.00 USD | 531,140.00 USD | 8,350.00 USD | 4,180.00 USD | 5,200.00 USD |
| `1D` | `0.1473` | 471,940.00 USD | 0.00 USD | 471,940.00 USD | 9,360.00 USD | 10,370.00 USD | 0.00 USD |
| `7D` | `0.1473` | 513,400.00 USD | 0.00 USD | 513,400.00 USD | 9,360.00 USD | 10,370.00 USD | 0.00 USD |
| `1D` | `0.1476` | 452,210.00 USD | 0.00 USD | 452,210.00 USD | 10,530.00 USD | 1,060.00 USD | 6,730.00 USD |
| `7D` | `0.1476` | 493,680.00 USD | 0.00 USD | 493,680.00 USD | 10,530.00 USD | 1,060.00 USD | 6,730.00 USD |
| `1D` | `0.1479` | 433,890.00 USD | 0.00 USD | 433,890.00 USD | 16,640.00 USD | 14,840.00 USD | 3,930.00 USD |
| `7D` | `0.1479` | 475,350.00 USD | 0.00 USD | 475,350.00 USD | 24,790.00 USD | 14,840.00 USD | 3,930.00 USD |
| `1D` | `0.1482` | 398,480.00 USD | 0.00 USD | 398,480.00 USD | 18,660.00 USD | 6,350.00 USD | 12,260.00 USD |
| `7D` | `0.1482` | 431,790.00 USD | 0.00 USD | 431,790.00 USD | 18,660.00 USD | 6,350.00 USD | 12,260.00 USD |
| `1D` | `0.1485` | 361,210.00 USD | 0.00 USD | 361,210.00 USD | 13,550.00 USD | 3,320.00 USD | 7,830.00 USD |
| `7D` | `0.1485` | 394,520.00 USD | 0.00 USD | 394,520.00 USD | 13,550.00 USD | 3,320.00 USD | 7,830.00 USD |
| `1D` | `0.1488` | 336,500.00 USD | 0.00 USD | 336,500.00 USD | 2,660.00 USD | 5,180.00 USD | 7,250.00 USD |
| `7D` | `0.1488` | 369,810.00 USD | 0.00 USD | 369,810.00 USD | 2,660.00 USD | 5,180.00 USD | 7,250.00 USD |
| `1D` | `0.1491` | 321,400.00 USD | 0.00 USD | 321,400.00 USD | 7,650.00 USD | 10,490.00 USD | 6,890.00 USD |
| `7D` | `0.1491` | 354,720.00 USD | 0.00 USD | 354,720.00 USD | 7,650.00 USD | 10,490.00 USD | 6,890.00 USD |
| `1D` | `0.1494` | 296,380.00 USD | 0.00 USD | 296,380.00 USD | 25,050.00 USD | 5,270.00 USD | 2,510.00 USD |
| `7D` | `0.1494` | 329,690.00 USD | 0.00 USD | 329,690.00 USD | 25,050.00 USD | 5,270.00 USD | 2,510.00 USD |
| `1D` | `0.1497` | 263,550.00 USD | 0.00 USD | 263,550.00 USD | 0.00 USD | 0.00 USD | 2,530.00 USD |
| `7D` | `0.1497` | 296,870.00 USD | 0.00 USD | 296,870.00 USD | 0.00 USD | 0.00 USD | 2,530.00 USD |
| `1D` | `0.1500` | 261,020.00 USD | 0.00 USD | 261,020.00 USD | 2,670.00 USD | 0.00 USD | 3,370.00 USD |
| `7D` | `0.1500` | 294,340.00 USD | 0.00 USD | 294,340.00 USD | 2,670.00 USD | 0.00 USD | 3,370.00 USD |
| `1D` | `0.1503` | 254,990.00 USD | 0.00 USD | 254,990.00 USD | 3,610.00 USD | 15,920.00 USD | 1,360.00 USD |
| `7D` | `0.1503` | 288,300.00 USD | 0.00 USD | 288,300.00 USD | 3,610.00 USD | 15,920.00 USD | 1,360.00 USD |
| `1D` | `0.1506` | 234,100.00 USD | 0.00 USD | 234,100.00 USD | 5,430.00 USD | 6,660.00 USD | 7,720.00 USD |
| `7D` | `0.1506` | 267,420.00 USD | 0.00 USD | 267,420.00 USD | 5,430.00 USD | 6,660.00 USD | 7,720.00 USD |
| `1D` | `0.1509` | 214,290.00 USD | 0.00 USD | 214,290.00 USD | 5,640.00 USD | 3,940.00 USD | 0.00 USD |
| `7D` | `0.1509` | 247,600.00 USD | 0.00 USD | 247,600.00 USD | 21,930.00 USD | 3,940.00 USD | 0.00 USD |
| `1D` | `0.1512` | 204,710.00 USD | 0.00 USD | 204,710.00 USD | 25,970.00 USD | 4,360.00 USD | 2,500.00 USD |
| `7D` | `0.1512` | 221,720.00 USD | 0.00 USD | 221,720.00 USD | 25,970.00 USD | 4,360.00 USD | 2,500.00 USD |
| `1D` | `0.1515` | 171,880.00 USD | 0.00 USD | 171,880.00 USD | 0.00 USD | 1,730.00 USD | 2,640.00 USD |
| `7D` | `0.1515` | 188,900.00 USD | 0.00 USD | 188,900.00 USD | 0.00 USD | 1,730.00 USD | 2,640.00 USD |
| `1D` | `0.1518` | 167,520.00 USD | 0.00 USD | 167,520.00 USD | 24,410.00 USD | 10,080.00 USD | 24,730.00 USD |
| `7D` | `0.1518` | 184,530.00 USD | 0.00 USD | 184,530.00 USD | 24,410.00 USD | 10,080.00 USD | 24,730.00 USD |
| `1D` | `0.1521` | 108,300.00 USD | 0.00 USD | 108,300.00 USD | 9,450.00 USD | 1,470.00 USD | 11,330.00 USD |
| `7D` | `0.1521` | 125,310.00 USD | 0.00 USD | 125,310.00 USD | 9,450.00 USD | 1,470.00 USD | 11,330.00 USD |
| `1D` | `0.1524` | 86,050.00 USD | 0.00 USD | 86,050.00 USD | 1,870.00 USD | 2,970.00 USD | 7,150.00 USD |
| `7D` | `0.1524` | 103,060.00 USD | 0.00 USD | 103,060.00 USD | 1,870.00 USD | 2,970.00 USD | 7,150.00 USD |
| `1D` | `0.1527` | 74,070.00 USD | 0.00 USD | 74,070.00 USD | 18,400.00 USD | 0.00 USD | 11,570.00 USD |
| `7D` | `0.1527` | 91,080.00 USD | 0.00 USD | 91,080.00 USD | 18,400.00 USD | 0.00 USD | 11,570.00 USD |
| `1D` | `0.1530` | 44,100.00 USD | 0.00 USD | 44,100.00 USD | 14,690.00 USD | 0.00 USD | 8,740.00 USD |
| `7D` | `0.1530` | 61,110.00 USD | 0.00 USD | 61,110.00 USD | 14,690.00 USD | 0.00 USD | 8,740.00 USD |
| `1D` | `0.1533` | 20,660.00 USD | 0.00 USD | 20,660.00 USD | 14,310.00 USD | 0.00 USD | 3,140.00 USD |
| `7D` | `0.1533` | 37,670.00 USD | 0.00 USD | 37,670.00 USD | 14,310.00 USD | 0.00 USD | 3,140.00 USD |
| `1D` | `0.1536` | 3,210.00 USD | 0.00 USD | 3,210.00 USD | 0.00 USD | 0.00 USD | 3,210.00 USD |
| `7D` | `0.1536` | 20,230.00 USD | 0.00 USD | 20,230.00 USD | 0.00 USD | 0.00 USD | 3,210.00 USD |
| `1D` | `0.1539` | 5,580.00 USD | 5,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,580.00 USD |
| `1D` | `0.1539` | 11,170.00 USD | 11,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,580.00 USD |
| `7D` | `0.1539` | 17,020.00 USD | 0.00 USD | 17,020.00 USD | 0.00 USD | 0.00 USD | 5,580.00 USD |
| `1D` | `0.1542` | 15,650.00 USD | 15,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,490.00 USD |
| `7D` | `0.1542` | 11,430.00 USD | 0.00 USD | 11,430.00 USD | 0.00 USD | 0.00 USD | 4,490.00 USD |
| `1D` | `0.1545` | 22,600.00 USD | 22,600.00 USD | 0.00 USD | 0.00 USD | 5,210.00 USD | 1,730.00 USD |
| `7D` | `0.1545` | 6,950.00 USD | 0.00 USD | 6,950.00 USD | 0.00 USD | 5,210.00 USD | 1,730.00 USD |
| `7D` | `0.1546` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1548` | 77,900.00 USD | 77,900.00 USD | 0.00 USD | 0.00 USD | 22,180.00 USD | 33,130.00 USD |
| `7D` | `0.1548` | 55,300.00 USD | 55,300.00 USD | 0.00 USD | 0.00 USD | 22,180.00 USD | 33,130.00 USD |
| `1D` | `0.1551` | 85,940.00 USD | 85,940.00 USD | 0.00 USD | 0.00 USD | 4,140.00 USD | 3,890.00 USD |
| `7D` | `0.1551` | 63,340.00 USD | 63,340.00 USD | 0.00 USD | 0.00 USD | 4,140.00 USD | 3,890.00 USD |
| `1D` | `0.1554` | 93,130.00 USD | 93,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,190.00 USD |
| `7D` | `0.1554` | 70,530.00 USD | 70,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,190.00 USD |
| `1D` | `0.1557` | 100,400.00 USD | 100,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,270.00 USD |
| `7D` | `0.1557` | 77,800.00 USD | 77,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,270.00 USD |
| `1D` | `0.1560` | 105,980.00 USD | 105,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,580.00 USD |
| `7D` | `0.1560` | 83,380.00 USD | 83,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,580.00 USD |
| `1D` | `0.1563` | 122,030.00 USD | 122,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,050.00 USD |
| `7D` | `0.1563` | 99,430.00 USD | 99,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,050.00 USD |
| `1D` | `0.1566` | 205,920.00 USD | 205,920.00 USD | 0.00 USD | 48,900.00 USD | 13,270.00 USD | 21,710.00 USD |
| `7D` | `0.1566` | 183,320.00 USD | 183,320.00 USD | 0.00 USD | 48,900.00 USD | 13,270.00 USD | 21,710.00 USD |
| `1D` | `0.1569` | 217,060.00 USD | 217,060.00 USD | 0.00 USD | 4,110.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `0.1569` | 194,460.00 USD | 194,460.00 USD | 0.00 USD | 4,110.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `0.1572` | 210,760.00 USD | 210,760.00 USD | 0.00 USD | 16,300.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1575` | 243,030.00 USD | 243,030.00 USD | 0.00 USD | 25,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1575` | 236,720.00 USD | 236,720.00 USD | 0.00 USD | 25,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1587` | 302,580.00 USD | 302,580.00 USD | 0.00 USD | 15,100.00 USD | 22,970.00 USD | 21,480.00 USD |
| `7D` | `0.1587` | 296,280.00 USD | 296,280.00 USD | 0.00 USD | 15,100.00 USD | 22,970.00 USD | 21,480.00 USD |
| `1D` | `0.1590` | 346,840.00 USD | 346,840.00 USD | 0.00 USD | 0.00 USD | 27,950.00 USD | 16,310.00 USD |
| `7D` | `0.1590` | 340,540.00 USD | 340,540.00 USD | 0.00 USD | 0.00 USD | 27,950.00 USD | 16,310.00 USD |
| `1D` | `0.1593` | 383,960.00 USD | 383,960.00 USD | 0.00 USD | 0.00 USD | 6,320.00 USD | 30,800.00 USD |
| `7D` | `0.1593` | 377,660.00 USD | 377,660.00 USD | 0.00 USD | 0.00 USD | 6,320.00 USD | 30,800.00 USD |
| `1D` | `0.1596` | 406,450.00 USD | 406,450.00 USD | 0.00 USD | 0.00 USD | 19,800.00 USD | 2,690.00 USD |
| `7D` | `0.1596` | 400,150.00 USD | 400,150.00 USD | 0.00 USD | 0.00 USD | 19,800.00 USD | 2,690.00 USD |
| `1D` | `0.1599` | 418,490.00 USD | 418,490.00 USD | 0.00 USD | 0.00 USD | 12,040.00 USD | 0.00 USD |
| `7D` | `0.1599` | 412,190.00 USD | 412,190.00 USD | 0.00 USD | 0.00 USD | 12,040.00 USD | 0.00 USD |
| `1D` | `0.1602` | 474,040.00 USD | 474,040.00 USD | 0.00 USD | 55,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1602` | 475,880.00 USD | 475,880.00 USD | 0.00 USD | 63,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1605` | 510,190.00 USD | 510,190.00 USD | 0.00 USD | 36,160.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1605` | 512,040.00 USD | 512,040.00 USD | 0.00 USD | 36,160.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1608` | 526,350.00 USD | 526,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,160.00 USD |
| `7D` | `0.1608` | 528,200.00 USD | 528,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,160.00 USD |
| `1D` | `0.1611` | 641,810.00 USD | 641,810.00 USD | 0.00 USD | 20,140.00 USD | 11,530.00 USD | 83,790.00 USD |
| `7D` | `0.1611` | 643,660.00 USD | 643,660.00 USD | 0.00 USD | 20,140.00 USD | 11,530.00 USD | 83,790.00 USD |
| `1D` | `0.1614` | 681,330.00 USD | 681,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39,510.00 USD |
| `7D` | `0.1614` | 683,170.00 USD | 683,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39,510.00 USD |
| `1D` | `0.1617` | 720,230.00 USD | 720,230.00 USD | 0.00 USD | 31,470.00 USD | 7,430.00 USD | 0.00 USD |
| `7D` | `0.1617` | 722,070.00 USD | 722,070.00 USD | 0.00 USD | 31,470.00 USD | 7,430.00 USD | 0.00 USD |
| `1D` | `0.1620` | 863,390.00 USD | 863,390.00 USD | 0.00 USD | 85,250.00 USD | 57,920.00 USD | 0.00 USD |
| `7D` | `0.1620` | 865,240.00 USD | 865,240.00 USD | 0.00 USD | 85,250.00 USD | 57,920.00 USD | 0.00 USD |
| `1D` | `0.1623` | 984,290.00 USD | 984,290.00 USD | 0.00 USD | 53,880.00 USD | 67,020.00 USD | 0.00 USD |
| `7D` | `0.1623` | 986,140.00 USD | 986,140.00 USD | 0.00 USD | 53,880.00 USD | 67,020.00 USD | 0.00 USD |
| `1D` | `0.1626` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 51,630.00 USD | 12,640.00 USD | 0.00 USD |
| `7D` | `0.1626` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 51,630.00 USD | 12,640.00 USD | 0.00 USD |
| `1D` | `0.1632` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD |
| `7D` | `0.1632` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD |
| `1D` | `0.1635` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 10,690.00 USD | 8,690.00 USD |
| `7D` | `0.1635` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 10,690.00 USD | 8,690.00 USD |
| `1D` | `0.1638` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 22,520.00 USD | 0.00 USD |
| `7D` | `0.1638` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 22,520.00 USD | 0.00 USD |
| `1D` | `0.1641` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 9,110.00 USD | 13,330.00 USD | 0.00 USD |
| `7D` | `0.1641` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 9,110.00 USD | 13,330.00 USD | 0.00 USD |
| `1D` | `0.1644` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 25,030.00 USD | 35,000.00 USD | 16,030.00 USD |
| `7D` | `0.1644` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 25,030.00 USD | 35,000.00 USD | 16,030.00 USD |
| `1D` | `0.1656` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 9,730.00 USD | 40,450.00 USD | 8,050.00 USD |
| `7D` | `0.1656` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 9,730.00 USD | 40,450.00 USD | 8,050.00 USD |
| `1D` | `0.1659` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 19,240.00 USD | 0.00 USD |
| `7D` | `0.1659` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 19,240.00 USD | 0.00 USD |
| `1D` | `0.1662` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 8,220.00 USD | 6,760.00 USD | 20,710.00 USD |
| `7D` | `0.1662` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 8,220.00 USD | 6,760.00 USD | 20,710.00 USD |
| `1D` | `0.1665` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 22,170.00 USD | 5,570.00 USD | 80,390.00 USD |
| `7D` | `0.1665` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 22,170.00 USD | 5,570.00 USD | 80,390.00 USD |
| `1D` | `0.1668` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 5,340.00 USD | 21,290.00 USD |
| `7D` | `0.1668` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 5,340.00 USD | 21,290.00 USD |
| `1D` | `0.1671` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 20,720.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1671` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 20,720.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1674` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 45,910.00 USD | 2,010.00 USD | 19,670.00 USD |
| `7D` | `0.1674` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 45,910.00 USD | 2,010.00 USD | 19,670.00 USD |
| `1D` | `0.1677` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 22,100.00 USD | 1,990.00 USD | 0.00 USD |
| `7D` | `0.1677` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 22,100.00 USD | 1,990.00 USD | 0.00 USD |
| `1D` | `0.1680` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 75,420.00 USD | 4,560.00 USD | 0.00 USD |
| `7D` | `0.1680` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 75,420.00 USD | 4,560.00 USD | 0.00 USD |
| `1D` | `0.1683` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 99,440.00 USD | 3,200.00 USD | 18,740.00 USD |
| `7D` | `0.1683` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 99,440.00 USD | 3,200.00 USD | 18,740.00 USD |
| `1D` | `0.1686` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 6,560.00 USD | 29,250.00 USD | 23,510.00 USD |
| `7D` | `0.1686` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 6,560.00 USD | 29,250.00 USD | 23,510.00 USD |
| `1D` | `0.1689` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 6,980.00 USD | 4,020.00 USD |
| `7D` | `0.1689` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 6,980.00 USD | 4,020.00 USD |
| `1D` | `0.1692` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 71,770.00 USD | 66,160.00 USD | 14,290.00 USD |
| `7D` | `0.1692` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 71,770.00 USD | 66,160.00 USD | 14,290.00 USD |
| `1D` | `0.1695` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 25,080.00 USD | 6,650.00 USD |
| `7D` | `0.1695` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 25,080.00 USD | 6,650.00 USD |
| `1D` | `0.1698` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 37,080.00 USD | 56,690.00 USD | 0.00 USD |
| `7D` | `0.1698` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 37,080.00 USD | 56,690.00 USD | 0.00 USD |
| `1D` | `0.1704` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 14,420.00 USD | 10,240.00 USD |
| `7D` | `0.1704` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 14,420.00 USD | 10,240.00 USD |
| `1D` | `0.1707` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 47,980.00 USD | 71,860.00 USD | 13,990.00 USD |
| `7D` | `0.1707` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 47,980.00 USD | 71,860.00 USD | 13,990.00 USD |
| `1D` | `0.1710` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,040.00 USD |
| `7D` | `0.1710` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,040.00 USD |
| `1D` | `0.1713` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 17,320.00 USD | 0.00 USD |
| `7D` | `0.1713` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 17,320.00 USD | 0.00 USD |
| `1D` | `0.1716` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 9,570.00 USD | 25,600.00 USD | 16,070.00 USD |
| `7D` | `0.1716` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 9,570.00 USD | 25,600.00 USD | 16,070.00 USD |
| `1D` | `0.1719` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 34,230.00 USD | 10,110.00 USD | 8,520.00 USD |
| `7D` | `0.1719` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 34,230.00 USD | 10,110.00 USD | 8,520.00 USD |
| `1D` | `0.1722` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 100,000.00 USD | 16,860.00 USD | 45,350.00 USD |
| `7D` | `0.1722` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 100,000.00 USD | 16,860.00 USD | 45,350.00 USD |
| `1D` | `0.1725` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 8,230.00 USD | 2,410.00 USD | 33,410.00 USD |
| `7D` | `0.1725` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 8,230.00 USD | 2,410.00 USD | 33,410.00 USD |
| `1D` | `0.1728` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD |
| `7D` | `0.1728` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD |
| `1D` | `0.1734` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD |
| `7D` | `0.1734` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD |
| `1D` | `0.1737` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 33,580.00 USD | 11,810.00 USD | 6,410.00 USD |
| `7D` | `0.1737` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 33,580.00 USD | 11,810.00 USD | 6,410.00 USD |
| `1D` | `0.1740` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 1,600.00 USD | 9,640.00 USD |
| `7D` | `0.1740` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 1,600.00 USD | 9,640.00 USD |
| `1D` | `0.1743` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD |
| `7D` | `0.1743` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD |
| `1D` | `0.1746` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 8,530.00 USD | 2,460.00 USD | 9,500.00 USD |
| `7D` | `0.1746` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 8,530.00 USD | 2,460.00 USD | 9,500.00 USD |
| `1D` | `0.1749` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 80,070.00 USD | 2,280.00 USD | 39,700.00 USD |
| `7D` | `0.1749` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 80,070.00 USD | 2,280.00 USD | 39,700.00 USD |
| `1D` | `0.1752` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 27,740.00 USD | 0.00 USD | 32,640.00 USD |
| `7D` | `0.1752` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 27,740.00 USD | 0.00 USD | 32,640.00 USD |
| `1D` | `0.1755` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 21,260.00 USD | 16,650.00 USD | 35,390.00 USD |
| `7D` | `0.1755` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 21,260.00 USD | 16,650.00 USD | 35,390.00 USD |
| `1D` | `0.1758` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 71,330.00 USD | 31,940.00 USD | 51,130.00 USD |
| `7D` | `0.1758` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 71,330.00 USD | 31,940.00 USD | 51,130.00 USD |
| `1D` | `0.1761` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 53,970.00 USD | 88,390.00 USD | 50,220.00 USD |
| `7D` | `0.1761` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 53,970.00 USD | 88,390.00 USD | 50,220.00 USD |
| `1D` | `0.1764` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 34,410.00 USD | 27,980.00 USD | 61,480.00 USD |
| `7D` | `0.1764` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 34,410.00 USD | 27,980.00 USD | 61,480.00 USD |
| `1D` | `0.1767` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 27,430.00 USD | 52,820.00 USD | 52,230.00 USD |
| `7D` | `0.1767` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 27,430.00 USD | 52,820.00 USD | 52,230.00 USD |
| `1D` | `0.1770` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 36,140.00 USD | 47,810.00 USD | 38,500.00 USD |
| `7D` | `0.1770` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 36,140.00 USD | 47,810.00 USD | 38,500.00 USD |
| `1D` | `0.1773` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 15,040.00 USD | 28,980.00 USD | 22,840.00 USD |
| `7D` | `0.1773` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 15,040.00 USD | 28,980.00 USD | 22,840.00 USD |
| `1D` | `0.1776` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 38,630.00 USD | 19,390.00 USD | 21,010.00 USD |
| `7D` | `0.1776` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 38,630.00 USD | 19,390.00 USD | 21,010.00 USD |
| `1D` | `0.1779` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 27,480.00 USD | 77,730.00 USD | 25,130.00 USD |
| `7D` | `0.1779` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 27,480.00 USD | 77,730.00 USD | 25,130.00 USD |
| `1D` | `0.1782` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 46,310.00 USD | 14,240.00 USD | 14,970.00 USD |
| `7D` | `0.1782` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 46,310.00 USD | 14,240.00 USD | 14,970.00 USD |
| `1D` | `0.1785` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 96,920.00 USD | 46,180.00 USD | 14,990.00 USD |
| `7D` | `0.1785` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 96,920.00 USD | 46,180.00 USD | 14,990.00 USD |
| `1D` | `0.1788` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 18,550.00 USD | 42,480.00 USD | 36,930.00 USD |
| `7D` | `0.1788` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 18,550.00 USD | 42,480.00 USD | 36,930.00 USD |
| `1D` | `0.1791` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 36,940.00 USD | 15,630.00 USD | 18,080.00 USD |
| `7D` | `0.1791` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 36,940.00 USD | 15,630.00 USD | 18,080.00 USD |
| `1D` | `0.1794` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 41,300.00 USD | 49,090.00 USD | 15,390.00 USD |
| `7D` | `0.1794` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 41,300.00 USD | 49,090.00 USD | 15,390.00 USD |
| `1D` | `0.1797` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 27,280.00 USD | 22,110.00 USD | 36,970.00 USD |
| `7D` | `0.1797` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 27,280.00 USD | 22,110.00 USD | 36,970.00 USD |
| `1D` | `0.1800` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 5,820.00 USD | 8,690.00 USD | 25,360.00 USD |
| `7D` | `0.1800` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 5,820.00 USD | 8,690.00 USD | 25,360.00 USD |
| `1D` | `0.1803` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 10,270.00 USD | 35,880.00 USD | 12,560.00 USD |
| `7D` | `0.1803` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 10,270.00 USD | 35,880.00 USD | 12,560.00 USD |
| `1D` | `0.1806` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 9,910.00 USD | 14,370.00 USD | 15,820.00 USD |
| `7D` | `0.1806` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 9,910.00 USD | 14,370.00 USD | 15,820.00 USD |
| `1D` | `0.1809` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 17,680.00 USD | 27,370.00 USD | 7,030.00 USD |
| `7D` | `0.1809` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 17,680.00 USD | 27,370.00 USD | 7,030.00 USD |
| `1D` | `0.1812` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 23,530.00 USD | 37,720.00 USD | 28,530.00 USD |
| `7D` | `0.1812` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 23,530.00 USD | 37,720.00 USD | 28,530.00 USD |
| `1D` | `0.1815` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 13,550.00 USD | 3,320.00 USD | 14,670.00 USD |
| `7D` | `0.1815` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 13,550.00 USD | 3,320.00 USD | 14,670.00 USD |
| `1D` | `0.1818` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 37,120.00 USD | 11,780.00 USD | 11,110.00 USD |
| `7D` | `0.1818` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 37,120.00 USD | 11,780.00 USD | 11,110.00 USD |
| `1D` | `0.1821` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 21,220.00 USD | 19,510.00 USD | 9,370.00 USD |
| `7D` | `0.1821` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 21,220.00 USD | 19,510.00 USD | 9,370.00 USD |
| `1D` | `0.1824` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 14,850.00 USD | 18,270.00 USD | 16,470.00 USD |
| `7D` | `0.1824` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 14,850.00 USD | 18,270.00 USD | 16,470.00 USD |
| `1D` | `0.1827` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 21,440.00 USD | 6,860.00 USD | 4,170.00 USD |
| `7D` | `0.1827` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 21,440.00 USD | 6,860.00 USD | 4,170.00 USD |
| `1D` | `0.1830` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 4,510.00 USD | 5,690.00 USD |
| `7D` | `0.1830` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 4,510.00 USD | 5,690.00 USD |
| `1D` | `0.1833` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 2,670.00 USD | 0.00 USD | 4,630.00 USD |
| `7D` | `0.1833` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 2,670.00 USD | 0.00 USD | 4,630.00 USD |
| `1D` | `0.1836` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 3,610.00 USD | 0.00 USD | 728.16 USD |
| `7D` | `0.1836` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 3,610.00 USD | 0.00 USD | 728.16 USD |
| `1D` | `0.1839` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 2,640.00 USD | 7,830.00 USD |
| `7D` | `0.1839` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 2,640.00 USD | 7,830.00 USD |
| `1D` | `0.1842` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 5,430.00 USD | 4,660.00 USD | 1,250.00 USD |
| `7D` | `0.1842` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 5,430.00 USD | 4,660.00 USD | 1,250.00 USD |
| `1D` | `0.1845` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 5,640.00 USD | 5,640.00 USD | 1,890.00 USD |
| `7D` | `0.1845` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 5,640.00 USD | 5,640.00 USD | 1,890.00 USD |
| `1D` | `0.1848` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 4,360.00 USD | 4,500.00 USD |
| `7D` | `0.1848` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 4,360.00 USD | 4,500.00 USD |
| `1D` | `0.1851` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD | 2,640.00 USD |
| `7D` | `0.1851` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD | 2,640.00 USD |
| `1D` | `0.1854` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 4,290.00 USD | 1,690.00 USD | 4,220.00 USD |
| `7D` | `0.1854` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 4,290.00 USD | 1,690.00 USD | 4,220.00 USD |
| `1D` | `0.1857` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 10,050.00 USD | 2,630.00 USD | 12,090.00 USD |
| `7D` | `0.1857` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 10,050.00 USD | 2,630.00 USD | 12,090.00 USD |
| `1D` | `0.1860` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 9,450.00 USD | 4,440.00 USD | 5,820.00 USD |
| `7D` | `0.1860` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 9,450.00 USD | 4,440.00 USD | 5,820.00 USD |
| `1D` | `0.1863` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD | 8,320.00 USD |
| `7D` | `0.1863` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD | 8,320.00 USD |
| `1D` | `0.1866` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 3,300.00 USD | 0.00 USD | 5,140.00 USD |
| `7D` | `0.1866` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 3,300.00 USD | 0.00 USD | 5,140.00 USD |
| `1D` | `0.1869` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 4,960.00 USD | 1,740.00 USD | 9,730.00 USD |
| `7D` | `0.1869` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 4,960.00 USD | 1,740.00 USD | 9,730.00 USD |
| `1D` | `0.1872` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 12,350.00 USD | 5,200.00 USD | 5,320.00 USD |
| `7D` | `0.1872` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 12,350.00 USD | 5,200.00 USD | 5,320.00 USD |
| `1D` | `0.1875` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 1,960.00 USD | 2,820.00 USD | 2,290.00 USD |
| `7D` | `0.1875` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 1,960.00 USD | 2,820.00 USD | 2,290.00 USD |
| `1D` | `0.1878` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 4,320.00 USD | 2,760.00 USD | 918.24 USD |
| `7D` | `0.1878` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 4,320.00 USD | 2,760.00 USD | 918.24 USD |
| `1D` | `0.1881` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 2,920.00 USD | 6,640.00 USD | 1,240.00 USD |
| `7D` | `0.1881` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 2,920.00 USD | 6,640.00 USD | 1,240.00 USD |
| `1D` | `0.1883` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 1,710.00 USD | 1,200.00 USD | 0.00 USD |
| `7D` | `0.1883` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 1,710.00 USD | 1,200.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `185.68M` | Total OI Tokens: `1,217,643,415.6 ARB`
  * 1h OI Change: `-10.92%` | 4h OI Change: `-13.25%` | 24h OI Change: `-21.46%`
  * Exchange Breakdown: Binance=`42.23M` | Bybit=`26.27M` | OKX=`14.95M` | Hyperliquid=`12.73M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.94K` | Last 24h: `10.97K` | Last 3d: `22.34K` | Last 7d: `43.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0014%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0061%` | **USDT KuCoin** | `0.0077%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0040%` | **USDT Bitget** | `0.0044%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `42.08%` | `57.92%` | `0.73` | 15,940,000.00 USD |
| `15M` | `Binance` | `41.8%` | `58.2%` | `0.72` | 6,380,000.00 USD |
| `15M` | `OKX` | `42.56%` | `57.44%` | `0.74` | 2,520,000.00 USD |
| `15M` | `Bybit` | `40.22%` | `59.78%` | `0.67` | 2,680,000.00 USD |
| `15M` | `KuCoin` | `44.92%` | `55.08%` | `0.82` | 277,700.00 USD |
| `15M` | `Gate` | `37.83%` | `62.17%` | `0.61` | 116,090.00 USD |
| `15M` | `Bitget` | `46.2%` | `53.8%` | `0.86` | 843,920.00 USD |
| `15M` | `BingX` | `39.84%` | `60.16%` | `0.66` | 302,230.00 USD |
| `15M` | `MEXC` | `40%` | `60%` | `0.67` | 612,450.00 USD |
| `15M` | `Bitunix` | `44.13%` | `55.87%` | `0.79` | 205,410.00 USD |
| `15M` | `Hyperliquid` | `32.07%` | `67.93%` | `0.47` | 425,820.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.85%` | `53.15%` | `0.88` | 1,380,000.00 USD |
| `15M` | `Crypto.com` | `28.18%` | `71.82%` | `0.39` | 17,820.00 USD |
| `15M` | `WhiteBIT` | `53.89%` | `46.11%` | `1.17` | 66,370.00 USD |
| `15M` | `HTX` | `51.9%` | `48.1%` | `1.08` | 22,950.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `46.52%` | `53.48%` | `0.87` | 23,450.00 USD |
| `15M` | `Aster` | `37.78%` | `62.22%` | `0.61` | 30,490.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `51.15%` | `48.85%` | `1.05` | 35,900.00 USD |
| `15M` | `Whale Positions` | `41.8%` | `58.2%` | `0.72` | 6,380,000.00 USD |
| `15M` | `Global Accounts` | `42.08%` | `57.92%` | `0.73` | 15,940,000.00 USD |
| `1H` | `ARB` | `44.32%` | `55.68%` | `0.80` | 24,170,000.00 USD |
| `1H` | `Binance` | `43.28%` | `56.72%` | `0.76` | 9,290,000.00 USD |
| `1H` | `OKX` | `44.6%` | `55.4%` | `0.81` | 3,400,000.00 USD |
| `1H` | `Bybit` | `42.48%` | `57.52%` | `0.74` | 4,000,000.00 USD |
| `1H` | `KuCoin` | `46.85%` | `53.15%` | `0.88` | 339,960.00 USD |
| `1H` | `Gate` | `43.61%` | `56.39%` | `0.77` | 243,950.00 USD |
| `1H` | `Bitget` | `51.52%` | `48.48%` | `1.06` | 1,490,000.00 USD |
| `1H` | `BingX` | `44.75%` | `55.25%` | `0.81` | 686,250.00 USD |
| `1H` | `MEXC` | `35.18%` | `64.82%` | `0.54` | 915,330.00 USD |
| `1H` | `Bitunix` | `43.9%` | `56.1%` | `0.78` | 293,720.00 USD |
| `1H` | `Hyperliquid` | `33.16%` | `66.84%` | `0.50` | 456,760.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.01%` | `50.99%` | `0.96` | 2,730,000.00 USD |
| `1H` | `Crypto.com` | `19.58%` | `80.42%` | `0.24` | 12,580.00 USD |
| `1H` | `WhiteBIT` | `75.28%` | `24.72%` | `3.05` | 187,380.00 USD |
| `1H` | `HTX` | `43.43%` | `56.57%` | `0.77` | 19,920.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `48.64%` | `51.36%` | `0.95` | 30,610.00 USD |
| `1H` | `Aster` | `29.93%` | `70.07%` | `0.43` | 42,130.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `47.04%` | `52.96%` | `0.89` | 44,770.00 USD |
| `1H` | `Whale Positions` | `43.28%` | `56.72%` | `0.76` | 9,290,000.00 USD |
| `1H` | `Global Accounts` | `44.32%` | `55.68%` | `0.80` | 24,170,000.00 USD |
| `4H` | `ARB` | `43.60%` | `56.40%` | `0.77` | 75,800,000.00 USD |
| `4H` | `Binance` | `43.23%` | `56.77%` | `0.76` | 29,840,000.00 USD |
| `4H` | `OKX` | `41.12%` | `58.88%` | `0.70` | 11,970,000.00 USD |
| `4H` | `Bybit` | `43.03%` | `56.97%` | `0.76` | 8,040,000.00 USD |
| `4H` | `KuCoin` | `44.4%` | `55.6%` | `0.80` | 684,380.00 USD |
| `4H` | `Gate` | `45.46%` | `54.54%` | `0.83` | 2,680,000.00 USD |
| `4H` | `Bitget` | `41.93%` | `58.07%` | `0.72` | 3,340,000.00 USD |
| `4H` | `BingX` | `42.42%` | `57.58%` | `0.74` | 3,350,000.00 USD |
| `4H` | `MEXC` | `45.12%` | `54.88%` | `0.82` | 7,330,000.00 USD |
| `4H` | `Bitunix` | `48.83%` | `51.17%` | `0.95` | 1,380,000.00 USD |
| `4H` | `Hyperliquid` | `35.72%` | `64.28%` | `0.56` | 2,500,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.51%` | `49.49%` | `1.02` | 2,790,000.00 USD |
| `4H` | `Crypto.com` | `55.95%` | `44.05%` | `1.27` | 26,560.00 USD |
| `4H` | `WhiteBIT` | `76.84%` | `23.16%` | `3.32` | 1,170,000.00 USD |
| `4H` | `HTX` | `49.68%` | `50.32%` | `0.99` | 39,590.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `29.04%` | `70.96%` | `0.41` | 325,890.00 USD |
| `4H` | `Aster` | `32.1%` | `67.9%` | `0.47` | 123,080.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `35.33%` | `64.67%` | `0.55` | 215,900.00 USD |
| `4H` | `Whale Positions` | `43.23%` | `56.77%` | `0.76` | 29,840,000.00 USD |
| `4H` | `Global Accounts` | `43.60%` | `56.40%` | `0.77` | 75,800,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1686` | `0.1691` | `0.1686` | `0.1698` | `0.1685` | 581,095.74 USD | 286,225.77 USD | 294,869.97 USD | -8,644.20 USD | `-1.49%` | `37B / 26S` |
| `0:00 UTC` | `0.1678` | `0.1678` | `0.1678` | `0.1689` | `0.1673` | 1,127,023.46 USD | 573,365.61 USD | 553,657.86 USD | 19,707.75 USD | `+1.75%` | `27B / 19S` |
| `5:00 UTC` | `0.1687` | `0.1687` | `0.1687` | `0.1691` | `0.1680` | 541,507.84 USD | 294,376.97 USD | 247,130.87 USD | 47,246.11 USD | `+8.72%` | `31B / 8S` |
| `0:00 UTC` | `0.1684` | `0.1682` | `0.1684` | `0.1688` | `0.1678` | 593,121.43 USD | 297,803.46 USD | 295,317.97 USD | 2,485.50 USD | `+0.42%` | `13B / 13S` |
| `5:00 UTC` | `0.1683` | `0.1683` | `0.1683` | `0.1688` | `0.1678` | 375,189.89 USD | 244,846.62 USD | 130,343.28 USD | 114,503.34 USD | `+30.52%` | `33B / 4S` |
| `0:00 UTC` | `0.1688` | `0.1688` | `0.1688` | `0.1693` | `0.1682` | 680,766.88 USD | 453,606.46 USD | 227,160.42 USD | 226,446.04 USD | `+33.26%` | `32B / 8S` |
| `5:00 UTC` | `0.1682` | `0.1683` | `0.1682` | `0.1688` | `0.1681` | 452,736.37 USD | 213,244.89 USD | 239,491.48 USD | -26,246.58 USD | `-5.80%` | `7B / 12S` |
| `0:00 UTC` | `0.1667` | `0.1655` | `0.1667` | `0.1684` | `0.1640` | 2,535,332.38 USD | 1,148,875.51 USD | 1,386,456.87 USD | -237,581.36 USD | `-9.37%` | `2B / 23S` |
| `5:00 UTC` | `0.1650` | `0.1654` | `0.1650` | `0.1661` | `0.1649` | 718,046.47 USD | 414,320.10 USD | 303,726.37 USD | 110,593.73 USD | `+15.40%` | `33B / 14S` |
| `0:00 UTC` | `0.1593` | `0.1616` | `0.1593` | `0.1656` | `0.1592` | 5,157,943.67 USD | 2,008,790.11 USD | 3,149,153.56 USD | -1,140,363.46 USD | `-22.11%` | `4B / 28S` |

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
| `5m` | -518,150.00 USD | -2,550,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,090,000.00 USD | -3,840,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,050,000.00 USD | -3,580,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,270,000.00 USD | -4,090,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,560,000.00 USD | -3,450,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,600,000.00 USD | -5,370,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,530,000.00 USD | -6,630,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,560,000.00 USD | -7,130,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,120,000.00 USD | -7,840,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,360,000.00 USD | -9,570,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,290,000.00 USD | -33,670,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,630,000.00 USD | -166,790,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-518.15K` | 15m=`-1.09M` | 1h=`-1.27M` | 24h=`-2.36M`
* Futures Capital Netflows: 5m=`-2.55M` | 15m=`-3.84M` | 1h=`-4.09M` | 24h=`-9.57M`
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
  * `2026-10-30 01:35:25 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:09:25 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:09:25 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:09:25 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:08:25 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:08:25 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:25 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:25 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:25 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:25 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:25 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
