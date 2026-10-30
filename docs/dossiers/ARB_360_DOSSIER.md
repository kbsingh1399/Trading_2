# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 15:24:08 IST` (`2026-10-30 09:54:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1620` | `0.1623` | `0.1616` | `0.1620` | `1,928,911` | 312,445.43 USD | 80,167.01 USD | `+25.66%` | -8,002,048.22 USD | `+1.98` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.1620` | `0.1621` | `0.1615` | `0.1620` | `576,482` | 93,233.07 USD | -19,114.48 USD | `-20.50%` | -8,021,162.71 USD | `+0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.1620` | `0.1620` | `0.1619` | `0.1619` | `25,783` | 4,175.75 USD | -2,362.39 USD | `-56.57%` | -8,023,525.10 USD | `+0.52` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1620` | `0.1624` | `0.1615` | `0.1620` | `3,475,906` | 562,907.20 USD | -115,540.88 USD | `-20.53%` | -7,976,499.90 USD | `-0.26` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1620` | `0.1623` | `0.1611` | `0.1620` | `4,822,290` | 779,913.00 USD | -34,929.06 USD | `-4.48%` | -8,011,428.96 USD | `+0.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1620` | `0.1621` | `0.1615` | `0.1619` | `602,539` | 97,453.17 USD | -21,448.81 USD | `-22.01%` | -8,032,877.78 USD | `-0.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1646` | `0.1657` | `0.1633` | `0.1649` | `22,323,310` | 3,671,078.25 USD | 439,965.29 USD | `+11.98%` | -7,388,117.42 USD | `+0.77` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1650` | `0.1657` | `0.1623` | `0.1629` | `29,928,265` | 4,911,959.21 USD | -315,580.46 USD | `-6.42%` | -7,703,697.88 USD | `+0.04` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1629` | `0.1632` | `0.1611` | `0.1619` | `13,674,939` | 2,216,176.33 USD | -329,179.90 USD | `-14.85%` | -8,032,877.78 USD | `+0.02` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -6,780,748.83 USD | `+0.90` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1665` | `0.1577` | `0.1649` | `114,713,582` | 18,773,815.61 USD | -66,765.80 USD | `-0.36%` | -6,847,514.63 USD | `+1.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1650` | `0.1657` | `0.1611` | `0.1619` | `43,608,489` | 7,128,991.34 USD | -645,043.70 USD | `-9.05%` | -7,492,558.33 USD | `+0.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -2,435,586.34 USD | `+1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -6,159,810.32 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -6,780,748.83 USD | `+0.90` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1665` | `0.1577` | `0.1649` | `114,713,582` | 18,773,815.61 USD | -66,765.80 USD | `-0.36%` | -6,847,514.63 USD | `+1.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1650` | `0.1657` | `0.1611` | `0.1619` | `43,608,489` | 7,128,991.34 USD | -645,043.70 USD | `-9.05%` | -7,492,558.33 USD | `+0.51` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:20:42 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1625` | 4,182.60 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 4.18K USD at 0.1625 USD [API] | `2026-10-29 07:16:16` |
| `ANNOUNCEMENT` | `INFO` | `0.1684` | 5,823.61 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale BUY: 5.82K USD at 0.1684 USD [API] | `2026-10-29 10:57:33` |
| `ANNOUNCEMENT` | `INFO` | `0.1770` | 709.13 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.71K USD at 0.1770 USD [API] | `2026-10-28 20:01:24` |
| `ANNOUNCEMENT` | `INFO` | `0.1730` | 1,220.98 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 1.22K USD at 0.1730 USD [API] | `2026-10-26 08:46:55` |
| `ANNOUNCEMENT` | `INFO` | `0.2105` | 227.00 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.23K USD at 0.2105 USD [API] | `2026-09-19 03:39:36` |
| `ANNOUNCEMENT` | `INFO` | `0.1708` | 6,077.79 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale BUY: 6.08K USD at 0.1708 USD [API] | `2026-10-29 13:59:02` |


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
| `Live` | `Long Liquidation` | `0.0345` | 105.57 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0365` | 356.31 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0375` | 242.53 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0385` | 1,490.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 110.22 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 170.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0465` | 4,650.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 109.52 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 100.47 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 156.28 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 924.32 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 2,270.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 16,160.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 205,030.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 1,110.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,250.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 11,240.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 99,790.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 313.22 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 976.14 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 2,970.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 5,840.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 111.58 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 3,000.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 226.17 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 79,110.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 4,630.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 14,220.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 4,980.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 19,460.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 280.45 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 362.62 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 4,780.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 2,180.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 2,040.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 814.24 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 1,510.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 2,750.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 1,600.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 396.66 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 13,020.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 7,670.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 3,860.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1015` | 8,870.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 414.83 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 802.14 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 13,280.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 8,190.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 1,620.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 2,230.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 11,210.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 13,820.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 425.50 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1125` | 118,120.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 281.48 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 8,950.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 1,450.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 14,280.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 25,800.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 1,830.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 1,240.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 19,220.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 50,430.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 377.05 USD | 995,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 348.01 USD | 995,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 16,720.00 USD | 994,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 10,250.00 USD | 978,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,010.00 USD | 968,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 17,000.00 USD | 966,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1310` | 8,460,000.00 USD | 8,460,000.00 USD | 6,470.00 USD | 4,610.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1313` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 4,010.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1315` | 19,580.00 USD | 949,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1316` | 8,440,000.00 USD | 8,440,000.00 USD | 9,620.00 USD | 4,840.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1319` | 8,420,000.00 USD | 8,420,000.00 USD | 4,630.00 USD | 0.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1322` | 8,400,000.00 USD | 8,400,000.00 USD | 5,580.00 USD | 2,780.00 USD | 17,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1325` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 5,550.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1325` | 4,640.00 USD | 929,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1328` | 8,360,000.00 USD | 8,360,000.00 USD | 19,000.00 USD | 7,370.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1331` | 8,320,000.00 USD | 8,320,000.00 USD | 13,420.00 USD | 4,240.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1334` | 8,300,000.00 USD | 8,300,000.00 USD | 3,580.00 USD | 3,230.00 USD | 7,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1335` | 51,860.00 USD | 924,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1337` | 8,280,000.00 USD | 8,280,000.00 USD | 2,830.00 USD | 4,520.00 USD | 19,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1340` | 8,260,000.00 USD | 8,260,000.00 USD | 6,330.00 USD | 5,970.00 USD | 13,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1343` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 5,790.00 USD | 13,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1345` | 39,090.00 USD | 872,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1346` | 8,210,000.00 USD | 8,210,000.00 USD | 33,130.00 USD | 5,000.00 USD | 21,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1349` | 8,150,000.00 USD | 8,150,000.00 USD | 4,450.00 USD | 2,140.00 USD | 19,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1352` | 8,130,000.00 USD | 8,130,000.00 USD | 11,390.00 USD | 6,290.00 USD | 13,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1355` | 8,100,000.00 USD | 8,100,000.00 USD | 7,540.00 USD | 9,000.00 USD | 6,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1355` | 1,440.00 USD | 833,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1358` | 8,070,000.00 USD | 8,070,000.00 USD | 25,150.00 USD | 9,870.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1361` | 8,030,000.00 USD | 8,030,000.00 USD | 8,700.00 USD | 1,930.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1364` | 8,020,000.00 USD | 8,020,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 10,320.00 USD | 832,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1367` | 7,990,000.00 USD | 7,990,000.00 USD | 4,500.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1370` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1373` | 7,980,000.00 USD | 7,980,000.00 USD | 4,620.00 USD | 0.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1375` | 18,260.00 USD | 822,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1379` | 7,940,000.00 USD | 7,940,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1385` | 7,920,000.00 USD | 7,920,000.00 USD | 11,880.00 USD | 0.00 USD | 42,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 4,330.00 USD | 803,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1388` | 7,870,000.00 USD | 7,870,000.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1391` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1394` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 9,210.00 USD | 799,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1397` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1400` | 7,770,000.00 USD | 7,770,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1403` | 7,750,000.00 USD | 7,750,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 14,550.00 USD | 790,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 16,540.00 USD | 775,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1418` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 0.00 USD | 14,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1421` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 499,030.00 USD | 759,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 19,140.00 USD | 260,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1436` | 7,710,000.00 USD | 7,710,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1439` | 7,680,000.00 USD | 7,680,000.00 USD | 14,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1442` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 9,510.00 USD | 241,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1447` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 5,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1451` | 4,780,000.00 USD | 4,780,000.00 USD | 16,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1451` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 8,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1453` | 4,760,000.00 USD | 4,760,000.00 USD | 12,460.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1455` | 4,750,000.00 USD | 4,750,000.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 92,080.00 USD | 231,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1457` | 4,740,000.00 USD | 4,740,000.00 USD | 2,050.00 USD | 1,610.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1459` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 4,870.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1461` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 3,000.00 USD | 1,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1463` | 4,720,000.00 USD | 4,720,000.00 USD | 9,940.00 USD | 2,690.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1465` | 4,710,000.00 USD | 4,710,000.00 USD | 11,020.00 USD | 5,840.00 USD | 10,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 28,360.00 USD | 139,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1466` | 7,650,000.00 USD | 7,650,000.00 USD | 9,720.00 USD | 5,520.00 USD | 93,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1467` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 1,110.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1469` | 4,680,000.00 USD | 4,680,000.00 USD | 4,430.00 USD | 1,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1469` | 7,540,000.00 USD | 7,540,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1471` | 4,670,000.00 USD | 4,670,000.00 USD | 10,000.00 USD | 7,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1472` | 7,530,000.00 USD | 7,530,000.00 USD | 12,940.00 USD | 3,390.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1473` | 4,650,000.00 USD | 4,650,000.00 USD | 24,360.00 USD | 26,350.00 USD | 78,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1475` | 4,520,000.00 USD | 4,520,000.00 USD | 19,070.00 USD | 7,230.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1475` | 7,500,000.00 USD | 7,500,000.00 USD | 24,840.00 USD | 13,040.00 USD | 10,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 83,410.00 USD | 111,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1477` | 4,490,000.00 USD | 4,490,000.00 USD | 101,700.00 USD | 18,420.00 USD | 158,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1478` | 7,450,000.00 USD | 7,450,000.00 USD | 110,850.00 USD | 33,410.00 USD | 125,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1479` | 4,210,000.00 USD | 4,210,000.00 USD | 71,170.00 USD | 13,530.00 USD | 29,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1481` | 4,100,000.00 USD | 4,100,000.00 USD | 45,520.00 USD | 1,650.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1481` | 7,180,000.00 USD | 7,180,000.00 USD | 41,960.00 USD | 31,150.00 USD | 25,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1483` | 4,050,000.00 USD | 4,050,000.00 USD | 28,260.00 USD | 8,210.00 USD | 125,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1484` | 7,090,000.00 USD | 7,090,000.00 USD | 12,060.00 USD | 3,040.00 USD | 194,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1485` | 3,890,000.00 USD | 3,890,000.00 USD | 45,800.00 USD | 1,040.00 USD | 66,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 3,340.00 USD | 27,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1487` | 3,770,000.00 USD | 3,770,000.00 USD | 8,840.00 USD | 3,580.00 USD | 13,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1487` | 6,880,000.00 USD | 6,880,000.00 USD | 61,970.00 USD | 10,470.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1489` | 3,750,000.00 USD | 3,750,000.00 USD | 24,850.00 USD | 0.00 USD | 5,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1490` | 6,770,000.00 USD | 6,770,000.00 USD | 38,870.00 USD | 14,820.00 USD | 77,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1491` | 3,720,000.00 USD | 3,720,000.00 USD | 23,780.00 USD | 15,530.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1493` | 3,670,000.00 USD | 3,670,000.00 USD | 20,150.00 USD | 9,030.00 USD | 8,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1493` | 6,640,000.00 USD | 6,640,000.00 USD | 27,770.00 USD | 17,120.00 USD | 20,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1495` | 3,630,000.00 USD | 3,630,000.00 USD | 57,850.00 USD | 0.00 USD | 28,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 937.17 USD | 24,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1496` | 6,580,000.00 USD | 6,580,000.00 USD | 29,430.00 USD | 13,380.00 USD | 195,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1497` | 3,540,000.00 USD | 3,540,000.00 USD | 8,630.00 USD | 0.00 USD | 347.81 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1499` | 3,530,000.00 USD | 3,530,000.00 USD | 5,920.00 USD | 7,890.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1499` | 6,340,000.00 USD | 6,340,000.00 USD | 60,500.00 USD | 9,610.00 USD | 17,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1501` | 3,520,000.00 USD | 3,520,000.00 USD | 11,460.00 USD | 13,130.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1502` | 6,250,000.00 USD | 6,250,000.00 USD | 2,610.00 USD | 9,860.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1503` | 3,490,000.00 USD | 3,490,000.00 USD | 48,710.00 USD | 4,400.00 USD | 154,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1505` | 3,280,000.00 USD | 3,280,000.00 USD | 35,380.00 USD | 1,940.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1505` | 6,230,000.00 USD | 6,230,000.00 USD | 67,080.00 USD | 21,620.00 USD | 52,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1507` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 1,150.00 USD | 304,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1508` | 6,090,000.00 USD | 6,090,000.00 USD | 151,240.00 USD | 4,870.00 USD | 248,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1509` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 6,130.00 USD | 49,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1511` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1511` | 5,690,000.00 USD | 5,690,000.00 USD | 86,820.00 USD | 11,590.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1513` | 2,880,000.00 USD | 2,880,000.00 USD | 11,750.00 USD | 3,900.00 USD | 249,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1514` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 15,050.00 USD | 367,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1515` | 2,610,000.00 USD | 2,610,000.00 USD | 7,040.00 USD | 0.00 USD | 122,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 945.33 USD | 23,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1517` | 2,480,000.00 USD | 2,480,000.00 USD | 12,390.00 USD | 6,150.00 USD | 24,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1517` | 5,170,000.00 USD | 5,170,000.00 USD | 96,310.00 USD | 4,290.00 USD | 119,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1519` | 2,440,000.00 USD | 2,440,000.00 USD | 40,200.00 USD | 7,220.00 USD | 28,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1520` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 22,600.00 USD | 156,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1521` | 2,360,000.00 USD | 2,360,000.00 USD | 33,890.00 USD | 4,770.00 USD | 13,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1523` | 2,310,000.00 USD | 2,310,000.00 USD | 8,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1523` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 15,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1525` | 2,300,000.00 USD | 2,300,000.00 USD | 40,210.00 USD | 0.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1526` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 38,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1527` | 2,260,000.00 USD | 2,260,000.00 USD | 12,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1529` | 2,240,000.00 USD | 2,240,000.00 USD | 23,440.00 USD | 9,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1529` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1531` | 2,210,000.00 USD | 2,210,000.00 USD | 6,490.00 USD | 9,650.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1532` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 14,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1533` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 1,760.00 USD | 11,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1535` | 2,180,000.00 USD | 2,180,000.00 USD | 10,930.00 USD | 3,970.00 USD | 7,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1535` | 4,690,000.00 USD | 4,690,000.00 USD | 35,470.00 USD | 8,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 8,620.00 USD | 22,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1537` | 2,160,000.00 USD | 2,160,000.00 USD | 4,040.00 USD | 14,200.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1538` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 14,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1539` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1541` | 2,130,000.00 USD | 2,130,000.00 USD | 32,370.00 USD | 1,730.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1541` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1544` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1545` | 2,090,000.00 USD | 2,090,000.00 USD | 20,110.00 USD | 7,790.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1547` | 2,060,000.00 USD | 2,060,000.00 USD | 14,430.00 USD | 0.00 USD | 4,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1547` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 12,560.00 USD | 89,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1549` | 2,040,000.00 USD | 2,040,000.00 USD | 5,820.00 USD | 17,930.00 USD | 25,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1550` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 16,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1551` | 1,990,000.00 USD | 1,990,000.00 USD | 11,600.00 USD | 10,490.00 USD | 5,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1553` | 1,960,000.00 USD | 1,960,000.00 USD | 7,900.00 USD | 4,020.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1553` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 7,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1555` | 1,940,000.00 USD | 1,940,000.00 USD | 38,090.00 USD | 1,660.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1555` | 4,150.00 USD | 13,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1556` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1557` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 11,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1559` | 1,880,000.00 USD | 1,880,000.00 USD | 14,470.00 USD | 2,970.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1559` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1561` | 1,860,000.00 USD | 1,860,000.00 USD | 12,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1562` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1563` | 1,850,000.00 USD | 1,850,000.00 USD | 11,460.00 USD | 19,080.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1565` | 1,820,000.00 USD | 1,820,000.00 USD | 54,610.00 USD | 19,210.00 USD | 16,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1565` | 4,280,000.00 USD | 4,280,000.00 USD | 70,940.00 USD | 28,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1565` | 9,660.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1567` | 1,730,000.00 USD | 1,730,000.00 USD | 21,860.00 USD | 1,850.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1568` | 4,180,000.00 USD | 4,180,000.00 USD | 111,700.00 USD | 10,060.00 USD | 151,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1569` | 1,690,000.00 USD | 1,690,000.00 USD | 24,170.00 USD | 0.00 USD | 105,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1571` | 1,560,000.00 USD | 1,560,000.00 USD | 54,580.00 USD | 7,000.00 USD | 49,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1571` | 3,910,000.00 USD | 3,910,000.00 USD | 194,660.00 USD | 13,570.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1573` | 1,450,000.00 USD | 1,450,000.00 USD | 20,000.00 USD | 3,460.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1574` | 3,640,000.00 USD | 3,640,000.00 USD | 77,250.00 USD | 79,780.00 USD | 34,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1575` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 4,810.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1577` | 1,380,000.00 USD | 1,380,000.00 USD | 28,900.00 USD | 29,200.00 USD | 14,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1577` | 3,450,000.00 USD | 3,450,000.00 USD | 31,130.00 USD | 118,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1579` | 1,310,000.00 USD | 1,310,000.00 USD | 11,910.00 USD | 0.00 USD | 12,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1580` | 3,300,000.00 USD | 3,300,000.00 USD | 216,490.00 USD | 46,710.00 USD | 22,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1581` | 1,280,000.00 USD | 1,280,000.00 USD | 19,190.00 USD | 8,040.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1583` | 1,250,000.00 USD | 1,250,000.00 USD | 86,410.00 USD | 25,280.00 USD | 29,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1583` | 3,020,000.00 USD | 3,020,000.00 USD | 70,150.00 USD | 17,610.00 USD | 24,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1585` | 1,110,000.00 USD | 1,110,000.00 USD | 16,540.00 USD | 17,270.00 USD | 6,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1586` | 2,910,000.00 USD | 2,910,000.00 USD | 59,180.00 USD | 0.00 USD | 23,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1587` | 1,070,000.00 USD | 1,070,000.00 USD | 42,230.00 USD | 26,600.00 USD | 49,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1589` | 954,650.00 USD | 954,650.00 USD | 9,280.00 USD | 10,830.00 USD | 38,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1589` | 2,820,000.00 USD | 2,820,000.00 USD | 59,670.00 USD | 12,590.00 USD | 89,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1591` | 895,830.00 USD | 895,830.00 USD | 15,370.00 USD | 19,200.00 USD | 38,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1592` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1593` | 822,760.00 USD | 822,760.00 USD | 14,950.00 USD | 32,920.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1595` | 744,750.00 USD | 744,750.00 USD | 10,260.00 USD | 1,210.00 USD | 3,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1595` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 37,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1597` | 729,790.00 USD | 729,790.00 USD | 11,790.00 USD | 0.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1598` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 86,680.00 USD | 75,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1599` | 711,970.00 USD | 711,970.00 USD | 0.00 USD | 7,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1601` | 704,390.00 USD | 704,390.00 USD | 21,340.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1601` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 47,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1603` | 680,740.00 USD | 680,740.00 USD | 28,500.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1604` | 2,400,000.00 USD | 2,400,000.00 USD | 98,670.00 USD | 21,760.00 USD | 273,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1605` | 638,240.00 USD | 638,240.00 USD | 16,510.00 USD | 0.00 USD | 36,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1607` | 585,600.00 USD | 585,600.00 USD | 5,090.00 USD | 17,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1607` | 2,000,000.00 USD | 2,000,000.00 USD | 166,880.00 USD | 0.00 USD | 370,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1609` | 563,100.00 USD | 563,100.00 USD | 57,710.00 USD | 0.00 USD | 90,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1610` | 1,460,000.00 USD | 1,460,000.00 USD | 178,210.00 USD | 11,640.00 USD | 178,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1611` | 415,070.00 USD | 415,070.00 USD | 61,340.00 USD | 69,930.00 USD | 44,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1613` | 239,520.00 USD | 239,520.00 USD | 18,100.00 USD | 30,050.00 USD | 15,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1613` | 1,100,000.00 USD | 1,100,000.00 USD | 321,740.00 USD | 10,980.00 USD | 415,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1615` | 176,150.00 USD | 176,150.00 USD | 0.00 USD | 41,050.00 USD | 21,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1616` | 348,490.00 USD | 348,490.00 USD | 187,590.00 USD | 35,210.00 USD | 49,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1617` | 113,840.00 USD | 113,840.00 USD | 0.00 USD | 8,790.00 USD | 25,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1619` | 79,360.00 USD | 79,360.00 USD | 0.00 USD | 17,910.00 USD | 30,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1619` | 76,670.00 USD | 76,670.00 USD | 29,070.00 USD | 0.00 USD | 47,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1621` | 30,470.00 USD | 30,470.00 USD | 0.00 USD | 5,660.00 USD | 24,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1622` | 155,220.00 USD | 155,220.00 USD | 49,670.00 USD | 105,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1623` | 64,310.00 USD | 64,310.00 USD | 28,240.00 USD | 17,020.00 USD | 19,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1625` | 149,760.00 USD | 149,760.00 USD | 38,240.00 USD | 0.00 USD | 47,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1625` | 414,410.00 USD | 414,410.00 USD | 0.00 USD | 122,430.00 USD | 136,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1627` | 211,230.00 USD | 211,230.00 USD | 0.00 USD | 20,350.00 USD | 41,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1628` | 491,190.00 USD | 491,190.00 USD | 76,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1629` | 316,370.00 USD | 316,370.00 USD | 0.00 USD | 3,520.00 USD | 101,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1631` | 562,130.00 USD | 562,130.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1635` | 325,060.00 USD | 325,060.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1635` | 1,980.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1637` | 339,930.00 USD | 339,930.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1649` | 345,860.00 USD | 345,860.00 USD | 5,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1651` | 362,000.00 USD | 362,000.00 USD | 16,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1653` | 367,980.00 USD | 367,980.00 USD | 5,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1657` | 382,930.00 USD | 382,930.00 USD | 14,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1661` | 665,870.00 USD | 665,870.00 USD | 103,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1663` | 464,020.00 USD | 464,020.00 USD | 11,790.00 USD | 14,550.00 USD | 54,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1664` | 827,710.00 USD | 827,710.00 USD | 104,470.00 USD | 0.00 USD | 57,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1665` | 501,360.00 USD | 501,360.00 USD | 0.00 USD | 3,710.00 USD | 33,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1667` | 543,260.00 USD | 543,260.00 USD | 21,340.00 USD | 5,340.00 USD | 15,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1667` | 882,960.00 USD | 882,960.00 USD | 42,580.00 USD | 12,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1669` | 571,030.00 USD | 571,030.00 USD | 4,600.00 USD | 15,730.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1670` | 1,220,000.00 USD | 1,220,000.00 USD | 141,080.00 USD | 108,010.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1671` | 633,060.00 USD | 633,060.00 USD | 25,900.00 USD | 0.00 USD | 36,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1673` | 717,310.00 USD | 717,310.00 USD | 51,000.00 USD | 13,590.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1673` | 1,330,000.00 USD | 1,330,000.00 USD | 20,540.00 USD | 23,800.00 USD | 68,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1675` | 750,600.00 USD | 750,600.00 USD | 8,930.00 USD | 1,990.00 USD | 22,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1675` | 4,640.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1676` | 1,570,000.00 USD | 1,570,000.00 USD | 84,020.00 USD | 153,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1677` | 940,750.00 USD | 940,750.00 USD | 86,210.00 USD | 58,400.00 USD | 45,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1679` | 998,420.00 USD | 998,420.00 USD | 20,840.00 USD | 14,460.00 USD | 22,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1679` | 1,780,000.00 USD | 1,780,000.00 USD | 52,340.00 USD | 72,840.00 USD | 80,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1681` | 1,150,000.00 USD | 1,150,000.00 USD | 91,660.00 USD | 34,810.00 USD | 21,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1682` | 2,020,000.00 USD | 2,020,000.00 USD | 130,480.00 USD | 53,630.00 USD | 64,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1683` | 1,270,000.00 USD | 1,270,000.00 USD | 56,920.00 USD | 12,810.00 USD | 49,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1685` | 1,410,000.00 USD | 1,410,000.00 USD | 38,450.00 USD | 48,480.00 USD | 52,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1685` | 2,110,000.00 USD | 2,110,000.00 USD | 29,070.00 USD | 14,000.00 USD | 47,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1687` | 1,490,000.00 USD | 1,490,000.00 USD | 4,160.00 USD | 8,320.00 USD | 69,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1688` | 2,200,000.00 USD | 2,200,000.00 USD | 49,670.00 USD | 25,190.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1689` | 1,590,000.00 USD | 1,590,000.00 USD | 51,500.00 USD | 26,970.00 USD | 23,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1691` | 1,830,000.00 USD | 1,830,000.00 USD | 69,010.00 USD | 69,050.00 USD | 101,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1691` | 2,380,000.00 USD | 2,380,000.00 USD | 33,660.00 USD | 38,670.00 USD | 104,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1693` | 1,970,000.00 USD | 1,970,000.00 USD | 57,220.00 USD | 29,120.00 USD | 59,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1694` | 2,500,000.00 USD | 2,500,000.00 USD | 17,360.00 USD | 62,560.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1695` | 2,030,000.00 USD | 2,030,000.00 USD | 18,340.00 USD | 17,530.00 USD | 19,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1697` | 2,090,000.00 USD | 2,090,000.00 USD | 23,730.00 USD | 37,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1697` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 56,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1699` | 2,190,000.00 USD | 2,190,000.00 USD | 24,020.00 USD | 22,050.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1700` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1701` | 2,230,000.00 USD | 2,230,000.00 USD | 9,960.00 USD | 7,000.00 USD | 24,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1703` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 14,420.00 USD | 16,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1703` | 2,800,000.00 USD | 2,800,000.00 USD | 68,360.00 USD | 55,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1705` | 2,310,000.00 USD | 2,310,000.00 USD | 31,680.00 USD | 6,390.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1705` | 448.16 USD | 7,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1706` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 57,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1707` | 2,450,000.00 USD | 2,450,000.00 USD | 46,300.00 USD | 71,240.00 USD | 26,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1709` | 2,530,000.00 USD | 2,530,000.00 USD | 28,900.00 USD | 29,200.00 USD | 17,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1709` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 31,310.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1711` | 2,570,000.00 USD | 2,570,000.00 USD | 17,400.00 USD | 4,910.00 USD | 17,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1712` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 5,490.00 USD | 22,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1713` | 2,600,000.00 USD | 2,600,000.00 USD | 7,010.00 USD | 20,450.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1715` | 2,680,000.00 USD | 2,680,000.00 USD | 11,710.00 USD | 40,520.00 USD | 32,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1715` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 59,620.00 USD | 24,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1715` | 1,150.00 USD | 8,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1717` | 2,720,000.00 USD | 2,720,000.00 USD | 10,610.00 USD | 18,050.00 USD | 10,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1718` | 3,120,000.00 USD | 3,120,000.00 USD | 14,540.00 USD | 0.00 USD | 38,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1719` | 2,790,000.00 USD | 2,790,000.00 USD | 39,720.00 USD | 5,950.00 USD | 20,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1721` | 2,910,000.00 USD | 2,910,000.00 USD | 53,810.00 USD | 19,690.00 USD | 47,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1721` | 3,460,000.00 USD | 3,460,000.00 USD | 68,850.00 USD | 12,590.00 USD | 266,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1723` | 3,000,000.00 USD | 3,000,000.00 USD | 29,070.00 USD | 9,300.00 USD | 54,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1724` | 3,660,000.00 USD | 3,660,000.00 USD | 74,040.00 USD | 0.00 USD | 120,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1725` | 3,060,000.00 USD | 3,060,000.00 USD | 8,230.00 USD | 13,360.00 USD | 37,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1725` | 10,550.00 USD | 18,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1727` | 3,080,000.00 USD | 3,080,000.00 USD | 10,260.00 USD | 0.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1729` | 3,090,000.00 USD | 3,090,000.00 USD | 8,220.00 USD | 0.00 USD | 6,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1730` | 3,970,000.00 USD | 3,970,000.00 USD | 299,490.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1733` | 3,110,000.00 USD | 3,110,000.00 USD | 7,950.00 USD | 1,560.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1733` | 4,110,000.00 USD | 4,110,000.00 USD | 145,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1735` | 3,140,000.00 USD | 3,140,000.00 USD | 16,980.00 USD | 9,510.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1735` | 1,190.00 USD | 19,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1737` | 3,170,000.00 USD | 3,170,000.00 USD | 15,900.00 USD | 2,310.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1739` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 2,270.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1739` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1741` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 3,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1743` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1745` | 3,200,000.00 USD | 3,200,000.00 USD | 3,500.00 USD | 2,460.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1745` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1747` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 25,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1748` | 4,310,000.00 USD | 4,310,000.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1749` | 3,330,000.00 USD | 3,330,000.00 USD | 80,070.00 USD | 2,280.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1751` | 3,360,000.00 USD | 3,360,000.00 USD | 16,950.00 USD | 0.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1751` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 171,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1753` | 3,400,000.00 USD | 3,400,000.00 USD | 17,770.00 USD | 0.00 USD | 21,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1754` | 4,700,000.00 USD | 4,700,000.00 USD | 37,610.00 USD | 0.00 USD | 176,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1755` | 3,440,000.00 USD | 3,440,000.00 USD | 16,760.00 USD | 8,430.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1757` | 3,510,000.00 USD | 3,510,000.00 USD | 6,850.00 USD | 14,210.00 USD | 49,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1757` | 4,870,000.00 USD | 4,870,000.00 USD | 124,250.00 USD | 38,670.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1759` | 3,590,000.00 USD | 3,590,000.00 USD | 58,360.00 USD | 11,020.00 USD | 11,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1760` | 5,130,000.00 USD | 5,130,000.00 USD | 209,280.00 USD | 15,550.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1761` | 3,730,000.00 USD | 3,730,000.00 USD | 33,150.00 USD | 66,160.00 USD | 40,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1763` | 3,800,000.00 USD | 3,800,000.00 USD | 17,320.00 USD | 10,910.00 USD | 33,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1763` | 5,380,000.00 USD | 5,380,000.00 USD | 142,420.00 USD | 101,270.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1765` | 3,870,000.00 USD | 3,870,000.00 USD | 15,830.00 USD | 20,220.00 USD | 35,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1766` | 5,720,000.00 USD | 5,720,000.00 USD | 163,180.00 USD | 138,030.00 USD | 36,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1767` | 3,960,000.00 USD | 3,960,000.00 USD | 19,860.00 USD | 41,430.00 USD | 34,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1769` | 4,050,000.00 USD | 4,050,000.00 USD | 21,060.00 USD | 35,020.00 USD | 32,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1769` | 5,920,000.00 USD | 5,920,000.00 USD | 113,280.00 USD | 60,410.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1771` | 4,080,000.00 USD | 4,080,000.00 USD | 16,140.00 USD | 5,670.00 USD | 2,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1772` | 6,130,000.00 USD | 6,130,000.00 USD | 77,840.00 USD | 112,520.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1773` | 4,120,000.00 USD | 4,120,000.00 USD | 5,720.00 USD | 23,730.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1775` | 4,160,000.00 USD | 4,160,000.00 USD | 20,860.00 USD | 6,390.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1775` | 6,320,000.00 USD | 6,320,000.00 USD | 164,290.00 USD | 30,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1777` | 4,270,000.00 USD | 4,270,000.00 USD | 27,230.00 USD | 68,360.00 USD | 20,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1778` | 6,530,000.00 USD | 6,530,000.00 USD | 63,990.00 USD | 71,060.00 USD | 72,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1779` | 4,300,000.00 USD | 4,300,000.00 USD | 7,310.00 USD | 8,710.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1781` | 4,300,000.00 USD | 4,300,000.00 USD | 2,050.00 USD | 1,610.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1781` | 6,580,000.00 USD | 6,580,000.00 USD | 11,220.00 USD | 4,590.00 USD | 33,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1783` | 4,360,000.00 USD | 4,360,000.00 USD | 27,640.00 USD | 15,680.00 USD | 18,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1784` | 6,810,000.00 USD | 6,810,000.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1785` | 4,410,000.00 USD | 4,410,000.00 USD | 12,390.00 USD | 27,370.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1785` | 1,980.00 USD | 21,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1787` | 4,440,000.00 USD | 4,440,000.00 USD | 7,560.00 USD | 21,410.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1787` | 6,980,000.00 USD | 6,980,000.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1789` | 4,450,000.00 USD | 4,450,000.00 USD | 9,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1790` | 7,100,000.00 USD | 7,100,000.00 USD | 103,860.00 USD | 17,360.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1791` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1793` | 4,470,000.00 USD | 4,470,000.00 USD | 9,190.00 USD | 4,600.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1793` | 7,230,000.00 USD | 7,230,000.00 USD | 78,950.00 USD | 42,780.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1795` | 4,530,000.00 USD | 4,530,000.00 USD | 16,300.00 USD | 33,080.00 USD | 12,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1796` | 7,300,000.00 USD | 7,300,000.00 USD | 17,130.00 USD | 12,930.00 USD | 35,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1797` | 4,560,000.00 USD | 4,560,000.00 USD | 10,870.00 USD | 4,390.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1799` | 4,580,000.00 USD | 4,580,000.00 USD | 3,780.00 USD | 8,790.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1799` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 11,280.00 USD | 68,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1801` | 4,620,000.00 USD | 4,620,000.00 USD | 3,730.00 USD | 17,760.00 USD | 13,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1802` | 7,490,000.00 USD | 7,490,000.00 USD | 48,220.00 USD | 36,020.00 USD | 33,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1803` | 4,650,000.00 USD | 4,650,000.00 USD | 2,390.00 USD | 10,580.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1805` | 4,660,000.00 USD | 4,660,000.00 USD | 4,010.00 USD | 4,760.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1805` | 7,550,000.00 USD | 7,550,000.00 USD | 11,410.00 USD | 38,130.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1807` | 4,690,000.00 USD | 4,690,000.00 USD | 11,560.00 USD | 11,500.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1808` | 7,700,000.00 USD | 7,700,000.00 USD | 23,650.00 USD | 52,750.00 USD | 73,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1809` | 4,710,000.00 USD | 4,710,000.00 USD | 2,490.00 USD | 7,210.00 USD | 1,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1811` | 4,730,000.00 USD | 4,730,000.00 USD | 13,300.00 USD | 4,850.00 USD | 3,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1811` | 7,810,000.00 USD | 7,810,000.00 USD | 64,990.00 USD | 26,860.00 USD | 18,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1813` | 4,780,000.00 USD | 4,780,000.00 USD | 7,950.00 USD | 35,640.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1814` | 7,930,000.00 USD | 7,930,000.00 USD | 28,070.00 USD | 26,510.00 USD | 65,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1815` | 4,800,000.00 USD | 4,800,000.00 USD | 7,040.00 USD | 1,040.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1815` | 135.29 USD | 22,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1817` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 9,410.00 USD | 9,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1817` | 8,040,000.00 USD | 8,040,000.00 USD | 64,770.00 USD | 10,470.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1819` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 2,620.00 USD | 5,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1820` | 8,180,000.00 USD | 8,180,000.00 USD | 52,150.00 USD | 54,880.00 USD | 38,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1821` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 10,520.00 USD | 2,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1823` | 4,860,000.00 USD | 4,860,000.00 USD | 10,830.00 USD | 7,660.00 USD | 5,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1823` | 8,310,000.00 USD | 8,310,000.00 USD | 62,540.00 USD | 18,340.00 USD | 50,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1825` | 4,880,000.00 USD | 4,880,000.00 USD | 3,290.00 USD | 3,020.00 USD | 8,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1826` | 8,380,000.00 USD | 8,380,000.00 USD | 45,250.00 USD | 9,890.00 USD | 14,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1827` | 4,880,000.00 USD | 4,880,000.00 USD | 5,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1829` | 8,480,000.00 USD | 8,480,000.00 USD | 20,880.00 USD | 28,120.00 USD | 51,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1832` | 8,620,000.00 USD | 8,620,000.00 USD | 79,470.00 USD | 18,130.00 USD | 35,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1835` | 8,650,000.00 USD | 8,650,000.00 USD | 13,840.00 USD | 7,930.00 USD | 16,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1838` | 8,830,000.00 USD | 8,830,000.00 USD | 54,990.00 USD | 11,590.00 USD | 106,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1841` | 8,900,000.00 USD | 8,900,000.00 USD | 28,940.00 USD | 12,910.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1844` | 8,980,000.00 USD | 8,980,000.00 USD | 20,990.00 USD | 3,900.00 USD | 56,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1845` | 2,390.00 USD | 24,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1847` | 9,020,000.00 USD | 9,020,000.00 USD | 5,770.00 USD | 11,590.00 USD | 20,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1850` | 9,200,000.00 USD | 9,200,000.00 USD | 77,110.00 USD | 51,400.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1853` | 9,300,000.00 USD | 9,300,000.00 USD | 46,730.00 USD | 0.00 USD | 56,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1854` | 9,310,000.00 USD | 9,310,000.00 USD | 4,750.00 USD | 4,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1855` | 616.01 USD | 25,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1875` | 1,450.00 USD | 26,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1945` | 4,010.00 USD | 30,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1975` | 150.10 USD | 30,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2055` | 11,590.00 USD | 42,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2075` | 13,570.00 USD | 55,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2085` | 474.40 USD | 56,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2095` | 164.23 USD | 56,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2105` | 190.73 USD | 56,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2135` | 15,690.00 USD | 72,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2145` | 4,320.00 USD | 76,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 41,330.00 USD | 118,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2175` | 213.22 USD | 118,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2195` | 87,800.00 USD | 206,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 114.52 USD | 206,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2245` | 338.64 USD | 206,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2255` | 154.78 USD | 206,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 6,980.00 USD | 213,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 15,930.00 USD | 229,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 102.62 USD | 229,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 22,000.00 USD | 251,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 49,300.00 USD | 300,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2455` | 231.97 USD | 301,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2545` | 546.54 USD | 301,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 3,870.00 USD | 305,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2575` | 26,570.00 USD | 332,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 54,960.00 USD | 387,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 154.94 USD | 387,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2685` | 226.51 USD | 387,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2695` | 11,830.00 USD | 399,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 201,290.00 USD | 600,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 214.21 USD | 600,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 11,600.00 USD | 612,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2795` | 482.84 USD | 612,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2835` | 2,160.00 USD | 615,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 187.26 USD | 615,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2925` | 794.52 USD | 616,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2985` | 287,090.00 USD | 903,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3015` | 1,910.00 USD | 905,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3055` | 485.90 USD | 905,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3075` | 6,290.00 USD | 911,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3085` | 603.06 USD | 912,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 11,930.00 USD | 924,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3125` | 1,530.00 USD | 925,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3155` | 649.11 USD | 926,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3175` | 227.49 USD | 926,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0345` | 1,820,000.00 USD | 0.00 USD | 105.57 USD | `-78.75%` | `3,060,100,000,000.00` |
| `Live` | `Long` | `0.0365` | 1,820,000.00 USD | 0.00 USD | 356.31 USD | `-77.52%` | `9,761,800,000,000.00` |
| `Live` | `Long` | `0.0375` | 1,820,000.00 USD | 0.00 USD | 242.53 USD | `-76.90%` | `6,467,400,000,000.00` |
| `Live` | `Long` | `0.0385` | 1,820,000.00 USD | 0.00 USD | 1,490.00 USD | `-76.29%` | `38,823,900,000,000.00` |
| `Live` | `Long` | `0.0415` | 1,820,000.00 USD | 0.00 USD | 110.22 USD | `-74.44%` | `2,655,800,000,000.00` |
| `Live` | `Long` | `0.0425` | 1,820,000.00 USD | 0.00 USD | 170.00 USD | `-73.82%` | `4,000,000,000,000.00` |
| `Live` | `Long` | `0.0465` | 1,820,000.00 USD | 0.00 USD | 4,650.00 USD | `-71.36%` | `100,000,000,000,000.00` |
| `Live` | `Long` | `0.0495` | 1,810,000.00 USD | 0.00 USD | 109.52 USD | `-69.51%` | `2,212,600,000,000.00` |
| `Live` | `Long` | `0.0505` | 1,810,000.00 USD | 0.00 USD | 100.47 USD | `-68.90%` | `1,989,600,000,000.00` |
| `Live` | `Long` | `0.0515` | 1,810,000.00 USD | 0.00 USD | 156.28 USD | `-68.28%` | `3,034,600,000,000.00` |
| `Live` | `Long` | `0.0525` | 1,810,000.00 USD | 0.00 USD | 924.32 USD | `-67.66%` | `17,606,000,000,000.00` |
| `Live` | `Long` | `0.0545` | 1,810,000.00 USD | 0.00 USD | 2,270.00 USD | `-66.43%` | `41,635,000,000,000.00` |
| `Live` | `Long` | `0.0565` | 1,810,000.00 USD | 0.00 USD | 16,160.00 USD | `-65.20%` | `285,941,000,000,000.00` |
| `Live` | `Long` | `0.0575` | 1,790,000.00 USD | 0.00 USD | 205,030.00 USD | `-64.58%` | `3,565,715,900,000,000.00` |
| `Live` | `Long` | `0.0595` | 1,590,000.00 USD | 0.00 USD | 1,110.00 USD | `-63.35%` | `18,731,100,000,000.00` |
| `Live` | `Long` | `0.0625` | 1,590,000.00 USD | 0.00 USD | 1,250.00 USD | `-61.51%` | `20,000,000,000,000.00` |
| `Live` | `Long` | `0.0665` | 1,590,000.00 USD | 0.00 USD | 11,240.00 USD | `-59.04%` | `169,053,400,000,000.00` |
| `Live` | `Long` | `0.0675` | 1,580,000.00 USD | 0.00 USD | 99,790.00 USD | `-58.43%` | `1,478,385,900,000,000.00` |
| `Live` | `Long` | `0.0685` | 1,480,000.00 USD | 0.00 USD | 313.22 USD | `-57.81%` | `4,572,600,000,000.00` |
| `Live` | `Long` | `0.0695` | 1,470,000.00 USD | 0.00 USD | 976.14 USD | `-57.19%` | `14,045,200,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,470,000.00 USD | 0.00 USD | 2,970.00 USD | `-56.58%` | `42,142,800,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,470,000.00 USD | 0.00 USD | 5,840.00 USD | `-55.96%` | `81,674,400,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,470,000.00 USD | 0.00 USD | 111.58 USD | `-55.35%` | `1,539,100,000,000.00` |
| `Live` | `Long` | `0.0735` | 1,470,000.00 USD | 0.00 USD | 3,000.00 USD | `-54.73%` | `40,770,800,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,460,000.00 USD | 0.00 USD | 226.17 USD | `-54.11%` | `3,035,900,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,460,000.00 USD | 0.00 USD | 79,110.00 USD | `-52.88%` | `1,034,100,300,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,380,000.00 USD | 0.00 USD | 4,630.00 USD | `-51.03%` | `58,261,800,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,380,000.00 USD | 0.00 USD | 14,220.00 USD | `-49.19%` | `172,303,200,000,000.00` |
| `Live` | `Long` | `0.0835` | 1,360,000.00 USD | 0.00 USD | 4,980.00 USD | `-48.57%` | `59,604,600,000,000.00` |
| `Live` | `Long` | `0.0865` | 1,360,000.00 USD | 0.00 USD | 19,460.00 USD | `-46.72%` | `224,937,400,000,000.00` |
| `Live` | `Long` | `0.0875` | 1,340,000.00 USD | 0.00 USD | 280.45 USD | `-46.11%` | `3,205,200,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,340,000.00 USD | 0.00 USD | 362.62 USD | `-45.49%` | `4,097,400,000,000.00` |
| `Live` | `Long` | `0.0895` | 1,340,000.00 USD | 0.00 USD | 4,780.00 USD | `-44.88%` | `53,365,600,000,000.00` |
| `Live` | `Long` | `0.0915` | 1,330,000.00 USD | 0.00 USD | 2,180.00 USD | `-43.64%` | `23,867,500,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,330,000.00 USD | 0.00 USD | 2,040.00 USD | `-43.03%` | `22,044,300,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,330,000.00 USD | 0.00 USD | 814.24 USD | `-42.41%` | `8,708,500,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,330,000.00 USD | 0.00 USD | 1,510.00 USD | `-41.80%` | `16,031,700,000,000.00` |
| `Live` | `Long` | `0.0955` | 1,330,000.00 USD | 0.00 USD | 2,750.00 USD | `-41.18%` | `28,821,700,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,320,000.00 USD | 0.00 USD | 1,600.00 USD | `-40.56%` | `16,620,400,000,000.00` |
| `Live` | `Long` | `0.0975` | 1,320,000.00 USD | 0.00 USD | 396.66 USD | `-39.95%` | `4,068,300,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,320,000.00 USD | 0.00 USD | 13,020.00 USD | `-39.33%` | `132,186,200,000,000.02` |
| `Live` | `Long` | `0.0995` | 1,310,000.00 USD | 0.00 USD | 7,670.00 USD | `-38.72%` | `77,071,300,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,300,000.00 USD | 0.00 USD | 3,860.00 USD | `-38.10%` | `38,436,400,000,000.00` |
| `Live` | `Long` | `0.1015` | 1,300,000.00 USD | 0.00 USD | 8,870.00 USD | `-37.48%` | `87,419,000,000,000.00` |
| `Live` | `Long` | `0.1025` | 1,290,000.00 USD | 0.00 USD | 414.83 USD | `-36.87%` | `4,047,100,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,290,000.00 USD | 0.00 USD | 802.14 USD | `-36.25%` | `7,750,100,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,290,000.00 USD | 0.00 USD | 13,280.00 USD | `-35.64%` | `127,068,000,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,270,000.00 USD | 0.00 USD | 8,190.00 USD | `-35.02%` | `77,610,300,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,270,000.00 USD | 0.00 USD | 1,620.00 USD | `-34.41%` | `15,202,300,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,260,000.00 USD | 0.00 USD | 2,230.00 USD | `-33.79%` | `20,784,700,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,260,000.00 USD | 0.00 USD | 11,210.00 USD | `-33.17%` | `103,322,500,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,250,000.00 USD | 0.00 USD | 13,820.00 USD | `-31.94%` | `125,027,000,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,240,000.00 USD | 0.00 USD | 425.50 USD | `-31.33%` | `3,816,100,000,000.00` |
| `Live` | `Long` | `0.1125` | 1,240,000.00 USD | 0.00 USD | 118,120.00 USD | `-30.71%` | `1,050,000,000,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,120,000.00 USD | 0.00 USD | 281.48 USD | `-30.09%` | `2,480,000,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,120,000.00 USD | 0.00 USD | 8,950.00 USD | `-29.48%` | `78,144,100,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,110,000.00 USD | 0.00 USD | 1,450.00 USD | `-28.86%` | `12,552,800,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,110,000.00 USD | 0.00 USD | 14,280.00 USD | `-27.63%` | `121,510,100,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,090,000.00 USD | 0.00 USD | 25,800.00 USD | `-27.01%` | `217,694,900,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,070,000.00 USD | 0.00 USD | 1,830.00 USD | `-26.40%` | `15,286,200,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,070,000.00 USD | 0.00 USD | 1,240.00 USD | `-25.17%` | `10,238,400,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,070,000.00 USD | 0.00 USD | 19,220.00 USD | `-24.55%` | `156,903,900,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,050,000.00 USD | 0.00 USD | 50,430.00 USD | `-23.93%` | `408,338,300,000,000.00` |
| `Live` | `Long` | `0.1245` | 995,710.00 USD | 0.00 USD | 377.05 USD | `-23.32%` | `3,028,500,000,000.00` |
| `Live` | `Long` | `0.1255` | 995,340.00 USD | 0.00 USD | 348.01 USD | `-22.70%` | `2,773,000,000,000.00` |
| `Live` | `Long` | `0.1265` | 994,990.00 USD | 0.00 USD | 16,720.00 USD | `-22.09%` | `132,151,600,000,000.00` |
| `Live` | `Long` | `0.1275` | 978,270.00 USD | 0.00 USD | 10,250.00 USD | `-21.47%` | `80,425,800,000,000.00` |
| `Live` | `Long` | `0.1295` | 968,020.00 USD | 0.00 USD | 2,010.00 USD | `-20.24%` | `15,486,600,000,000.00` |
| `Live` | `Long` | `0.1305` | 966,010.00 USD | 0.00 USD | 17,000.00 USD | `-19.62%` | `130,296,400,000,000.00` |
| `Live` | `Long` | `0.1315` | 949,010.00 USD | 0.00 USD | 19,580.00 USD | `-19.01%` | `148,881,700,000,000.00` |
| `Live` | `Long` | `0.1325` | 929,430.00 USD | 0.00 USD | 4,640.00 USD | `-18.39%` | `35,013,800,000,000.00` |
| `Live` | `Long` | `0.1335` | 924,790.00 USD | 0.00 USD | 51,860.00 USD | `-17.78%` | `388,489,900,000,000.00` |
| `Live` | `Long` | `0.1345` | 872,930.00 USD | 0.00 USD | 39,090.00 USD | `-17.16%` | `290,617,800,000,000.00` |
| `Live` | `Long` | `0.1355` | 833,840.00 USD | 0.00 USD | 1,440.00 USD | `-16.54%` | `10,635,400,000,000.00` |
| `Live` | `Long` | `0.1365` | 832,400.00 USD | 0.00 USD | 10,320.00 USD | `-15.93%` | `75,610,600,000,000.00` |
| `Live` | `Long` | `0.1375` | 822,080.00 USD | 0.00 USD | 18,260.00 USD | `-15.31%` | `132,828,700,000,000.02` |
| `Live` | `Long` | `0.1385` | 803,810.00 USD | 0.00 USD | 4,330.00 USD | `-14.70%` | `31,259,100,000,000.00` |
| `Live` | `Long` | `0.1395` | 799,480.00 USD | 0.00 USD | 9,210.00 USD | `-14.08%` | `66,000,700,000,000.00` |
| `Live` | `Long` | `0.1405` | 790,280.00 USD | 0.00 USD | 14,550.00 USD | `-13.46%` | `103,574,900,000,000.00` |
| `Live` | `Long` | `0.1415` | 775,720.00 USD | 0.00 USD | 16,540.00 USD | `-12.85%` | `116,879,900,000,000.00` |
| `Live` | `Long` | `0.1425` | 759,190.00 USD | 0.00 USD | 499,030.00 USD | `-12.23%` | `3,501,939,200,000,000.00` |
| `Live` | `Long` | `0.1435` | 260,160.00 USD | 0.00 USD | 19,140.00 USD | `-11.62%` | `133,388,500,000,000.00` |
| `Live` | `Long` | `0.1445` | 241,020.00 USD | 0.00 USD | 9,510.00 USD | `-11.00%` | `65,841,200,000,000.00` |
| `Live` | `Long` | `0.1455` | 231,500.00 USD | 0.00 USD | 92,080.00 USD | `-10.38%` | `632,843,200,000,000.00` |
| `Live` | `Long` | `0.1465` | 139,430.00 USD | 0.00 USD | 28,360.00 USD | `-9.77%` | `193,592,500,000,000.00` |
| `Live` | `Long` | `0.1475` | 111,060.00 USD | 0.00 USD | 83,410.00 USD | `-9.15%` | `565,466,200,000,000.00` |
| `Live` | `Long` | `0.1485` | 27,660.00 USD | 0.00 USD | 3,340.00 USD | `-8.54%` | `22,502,000,000,000.00` |
| `Live` | `Long` | `0.1495` | 24,320.00 USD | 0.00 USD | 937.17 USD | `-7.92%` | `6,268,700,000,000.00` |
| `Live` | `Long` | `0.1515` | 23,380.00 USD | 0.00 USD | 945.33 USD | `-6.69%` | `6,239,800,000,000.00` |
| `Live` | `Long` | `0.1535` | 22,430.00 USD | 0.00 USD | 8,620.00 USD | `-5.46%` | `56,165,700,000,000.00` |
| `Live` | `Long` | `0.1555` | 13,810.00 USD | 0.00 USD | 4,150.00 USD | `-4.23%` | `26,689,100,000,000.00` |
| `Live` | `Long` | `0.1565` | 9,660.00 USD | 0.00 USD | 9,660.00 USD | `-3.61%` | `61,740,200,000,000.00` |
| `Live` | `Short` | `0.1635` | 1,980.00 USD | 1,980.00 USD | 0.00 USD | `+0.70%` | `12,093,900,000,000.00` |
| `Live` | `Short` | `0.1675` | 6,620.00 USD | 4,640.00 USD | 0.00 USD | `+3.17%` | `27,726,400,000,000.00` |
| `Live` | `Short` | `0.1705` | 7,070.00 USD | 448.16 USD | 0.00 USD | `+5.01%` | `2,628,500,000,000.00` |
| `Live` | `Short` | `0.1715` | 8,220.00 USD | 1,150.00 USD | 0.00 USD | `+5.63%` | `6,703,900,000,000.00` |
| `Live` | `Short` | `0.1725` | 18,770.00 USD | 10,550.00 USD | 0.00 USD | `+6.25%` | `61,173,800,000,000.00` |
| `Live` | `Short` | `0.1735` | 19,970.00 USD | 1,190.00 USD | 0.00 USD | `+6.86%` | `6,881,100,000,000.00` |
| `Live` | `Short` | `0.1785` | 21,950.00 USD | 1,980.00 USD | 0.00 USD | `+9.94%` | `11,107,700,000,000.00` |
| `Live` | `Short` | `0.1815` | 22,080.00 USD | 135.29 USD | 0.00 USD | `+11.79%` | `745,400,000,000.00` |
| `Live` | `Short` | `0.1845` | 24,470.00 USD | 2,390.00 USD | 0.00 USD | `+13.64%` | `12,933,500,000,000.00` |
| `Live` | `Short` | `0.1855` | 25,090.00 USD | 616.01 USD | 0.00 USD | `+14.25%` | `3,320,800,000,000.00` |
| `Live` | `Short` | `0.1875` | 26,540.00 USD | 1,450.00 USD | 0.00 USD | `+15.48%` | `7,754,100,000,000.00` |
| `Live` | `Short` | `0.1945` | 30,550.00 USD | 4,010.00 USD | 0.00 USD | `+19.80%` | `20,600,200,000,000.00` |
| `Live` | `Short` | `0.1975` | 30,700.00 USD | 150.10 USD | 0.00 USD | `+21.64%` | `760,000,000,000.00` |
| `Live` | `Short` | `0.2055` | 42,290.00 USD | 11,590.00 USD | 0.00 USD | `+26.57%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2075` | 55,860.00 USD | 13,570.00 USD | 0.00 USD | `+27.80%` | `65,394,900,000,000.00` |
| `Live` | `Short` | `0.2085` | 56,330.00 USD | 474.40 USD | 0.00 USD | `+28.42%` | `2,275,300,000,000.00` |
| `Live` | `Short` | `0.2095` | 56,500.00 USD | 164.23 USD | 0.00 USD | `+29.03%` | `783,900,000,000.00` |
| `Live` | `Short` | `0.2105` | 56,690.00 USD | 190.73 USD | 0.00 USD | `+29.65%` | `906,100,000,000.00` |
| `Live` | `Short` | `0.2135` | 72,380.00 USD | 15,690.00 USD | 0.00 USD | `+31.50%` | `73,505,600,000,000.00` |
| `Live` | `Short` | `0.2145` | 76,700.00 USD | 4,320.00 USD | 0.00 USD | `+32.11%` | `20,150,900,000,000.00` |
| `Live` | `Short` | `0.2155` | 118,040.00 USD | 41,330.00 USD | 0.00 USD | `+32.73%` | `191,801,700,000,000.00` |
| `Live` | `Short` | `0.2175` | 118,250.00 USD | 213.22 USD | 0.00 USD | `+33.96%` | `980,300,000,000.00` |
| `Live` | `Short` | `0.2195` | 206,050.00 USD | 87,800.00 USD | 0.00 USD | `+35.19%` | `400,000,000,000,000.00` |
| `Live` | `Short` | `0.2235` | 206,160.00 USD | 114.52 USD | 0.00 USD | `+37.66%` | `512,400,000,000.00` |
| `Live` | `Short` | `0.2245` | 206,500.00 USD | 338.64 USD | 0.00 USD | `+38.27%` | `1,508,400,000,000.00` |
| `Live` | `Short` | `0.2255` | 206,660.00 USD | 154.78 USD | 0.00 USD | `+38.89%` | `686,400,000,000.00` |
| `Live` | `Short` | `0.2295` | 213,640.00 USD | 6,980.00 USD | 0.00 USD | `+41.35%` | `30,426,900,000,000.00` |
| `Live` | `Short` | `0.2355` | 229,570.00 USD | 15,930.00 USD | 0.00 USD | `+45.05%` | `67,638,800,000,000.00` |
| `Live` | `Short` | `0.2375` | 229,670.00 USD | 102.62 USD | 0.00 USD | `+46.28%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2405` | 251,670.00 USD | 22,000.00 USD | 0.00 USD | `+48.13%` | `91,476,700,000,000.00` |
| `Live` | `Short` | `0.2425` | 300,970.00 USD | 49,300.00 USD | 0.00 USD | `+49.36%` | `203,286,500,000,000.00` |
| `Live` | `Short` | `0.2455` | 301,200.00 USD | 231.97 USD | 0.00 USD | `+51.21%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2545` | 301,750.00 USD | 546.54 USD | 0.00 USD | `+56.75%` | `2,147,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 305,610.00 USD | 3,870.00 USD | 0.00 USD | `+57.98%` | `15,070,700,000,000.00` |
| `Live` | `Short` | `0.2575` | 332,190.00 USD | 26,570.00 USD | 0.00 USD | `+58.60%` | `103,191,700,000,000.00` |
| `Live` | `Short` | `0.2585` | 387,150.00 USD | 54,960.00 USD | 0.00 USD | `+59.21%` | `212,629,500,000,000.00` |
| `Live` | `Short` | `0.2615` | 387,310.00 USD | 154.94 USD | 0.00 USD | `+61.06%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2685` | 387,530.00 USD | 226.51 USD | 0.00 USD | `+65.37%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2695` | 399,360.00 USD | 11,830.00 USD | 0.00 USD | `+65.99%` | `43,905,000,000,000.00` |
| `Live` | `Short` | `0.2715` | 600,660.00 USD | 201,290.00 USD | 0.00 USD | `+67.22%` | `741,414,900,000,000.00` |
| `Live` | `Short` | `0.2725` | 600,870.00 USD | 214.21 USD | 0.00 USD | `+67.84%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 612,470.00 USD | 11,600.00 USD | 0.00 USD | `+69.07%` | `42,249,200,000,000.00` |
| `Live` | `Short` | `0.2795` | 612,950.00 USD | 482.84 USD | 0.00 USD | `+72.15%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2835` | 615,110.00 USD | 2,160.00 USD | 0.00 USD | `+74.61%` | `7,608,100,000,000.00` |
| `Live` | `Short` | `0.2915` | 615,300.00 USD | 187.26 USD | 0.00 USD | `+79.54%` | `642,400,000,000.00` |
| `Live` | `Short` | `0.2925` | 616,090.00 USD | 794.52 USD | 0.00 USD | `+80.16%` | `2,716,300,000,000.00` |
| `Live` | `Short` | `0.2985` | 903,180.00 USD | 287,090.00 USD | 0.00 USD | `+83.85%` | `961,767,500,000,000.00` |
| `Live` | `Short` | `0.3015` | 905,090.00 USD | 1,910.00 USD | 0.00 USD | `+85.70%` | `6,328,900,000,000.00` |
| `Live` | `Short` | `0.3055` | 905,570.00 USD | 485.90 USD | 0.00 USD | `+88.16%` | `1,590,500,000,000.00` |
| `Live` | `Short` | `0.3075` | 911,860.00 USD | 6,290.00 USD | 0.00 USD | `+89.39%` | `20,460,400,000,000.00` |
| `Live` | `Short` | `0.3085` | 912,470.00 USD | 603.06 USD | 0.00 USD | `+90.01%` | `1,954,800,000,000.00` |
| `Live` | `Short` | `0.3105` | 924,390.00 USD | 11,930.00 USD | 0.00 USD | `+91.24%` | `38,407,000,000,000.00` |
| `Live` | `Short` | `0.3125` | 925,920.00 USD | 1,530.00 USD | 0.00 USD | `+92.47%` | `4,897,100,000,000.00` |
| `Live` | `Short` | `0.3155` | 926,570.00 USD | 649.11 USD | 0.00 USD | `+94.32%` | `2,057,400,000,000.00` |
| `Live` | `Short` | `0.3175` | 926,800.00 USD | 227.49 USD | 0.00 USD | `+95.55%` | `716,500,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0355` | 758,380.00 USD | 0.00 USD | 355.00 USD | `-78.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 758,020.00 USD | 0.00 USD | 297.50 USD | `-73.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 757,720.00 USD | 0.00 USD | 353.50 USD | `-68.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0545` | 757,370.00 USD | 0.00 USD | 276.53 USD | `-66.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 757,090.00 USD | 0.00 USD | 4,310.00 USD | `-65.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 752,780.00 USD | 0.00 USD | 475.11 USD | `-60.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 752,310.00 USD | 0.00 USD | 131.16 USD | `-59.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 752,170.00 USD | 0.00 USD | 881.45 USD | `-59.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 751,290.00 USD | 0.00 USD | 1,070.00 USD | `-58.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 750,220.00 USD | 0.00 USD | 1,050.00 USD | `-57.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 749,170.00 USD | 0.00 USD | 1,010.00 USD | `-57.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 748,160.00 USD | 0.00 USD | 4,100.00 USD | `-56.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 744,060.00 USD | 0.00 USD | 529.04 USD | `-55.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 743,530.00 USD | 0.00 USD | 2,390.00 USD | `-55.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 741,140.00 USD | 0.00 USD | 757.39 USD | `-53.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 740,380.00 USD | 0.00 USD | 1,490.00 USD | `-51.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 738,900.00 USD | 0.00 USD | 255.36 USD | `-47.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 738,640.00 USD | 0.00 USD | 277.37 USD | `-46.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 738,360.00 USD | 0.00 USD | 262.50 USD | `-46.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 738,100.00 USD | 0.00 USD | 795.57 USD | `-45.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 737,300.00 USD | 0.00 USD | 181.00 USD | `-44.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 737,120.00 USD | 0.00 USD | 3,810.00 USD | `-38.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 733,310.00 USD | 0.00 USD | 1,550.00 USD | `-36.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 731,760.00 USD | 0.00 USD | 116.07 USD | `-33.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 731,650.00 USD | 0.00 USD | 19,070.00 USD | `-33.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 712,580.00 USD | 0.00 USD | 577.22 USD | `-31.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 712,000.00 USD | 0.00 USD | 343.50 USD | `-29.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 711,660.00 USD | 0.00 USD | 26,280.00 USD | `-28.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 685,380.00 USD | 0.00 USD | 4,870.00 USD | `-25.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 680,510.00 USD | 0.00 USD | 83,620.00 USD | `-25.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1225` | 596,880.00 USD | 0.00 USD | 487.10 USD | `-24.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 596,400.00 USD | 0.00 USD | 14,940.00 USD | `-23.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1255` | 581,460.00 USD | 0.00 USD | 129,320.00 USD | `-22.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 452,140.00 USD | 0.00 USD | 2,670.00 USD | `-22.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 449,470.00 USD | 0.00 USD | 473.27 USD | `-21.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 449,000.00 USD | 0.00 USD | 203,210.00 USD | `-20.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 245,790.00 USD | 0.00 USD | 1,670.00 USD | `-19.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1315` | 244,120.00 USD | 0.00 USD | 1,590.00 USD | `-19.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 242,520.00 USD | 0.00 USD | 6,000.00 USD | `-18.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 236,520.00 USD | 0.00 USD | 625.78 USD | `-17.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 235,890.00 USD | 0.00 USD | 502.28 USD | `-17.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 235,390.00 USD | 0.00 USD | 162.60 USD | `-16.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 235,230.00 USD | 0.00 USD | 700.86 USD | `-15.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 234,530.00 USD | 0.00 USD | 13,710.00 USD | `-15.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 220,820.00 USD | 0.00 USD | 108.57 USD | `-14.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 220,710.00 USD | 0.00 USD | 4,210.00 USD | `-13.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 216,500.00 USD | 0.00 USD | 127.35 USD | `-12.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 216,370.00 USD | 0.00 USD | 24,850.00 USD | `-12.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 191,520.00 USD | 0.00 USD | 1,300.00 USD | `-11.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 190,220.00 USD | 0.00 USD | 25,960.00 USD | `-11.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 164,260.00 USD | 0.00 USD | 46,010.00 USD | `-10.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 118,260.00 USD | 0.00 USD | 16,980.00 USD | `-9.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 101,280.00 USD | 0.00 USD | 2,400.00 USD | `-9.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 98,870.00 USD | 0.00 USD | 2,610.00 USD | `-8.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 96,260.00 USD | 0.00 USD | 1,540.00 USD | `-7.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 94,720.00 USD | 0.00 USD | 3,010.00 USD | `-7.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 91,710.00 USD | 0.00 USD | 401.02 USD | `-6.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 91,310.00 USD | 0.00 USD | 2,990.00 USD | `-6.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1535` | 88,320.00 USD | 0.00 USD | 34,840.00 USD | `-5.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 53,470.00 USD | 0.00 USD | 5,420.00 USD | `-4.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 48,060.00 USD | 0.00 USD | 656.37 USD | `-4.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 47,400.00 USD | 0.00 USD | 14,540.00 USD | `-3.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1575` | 32,850.00 USD | 0.00 USD | 499.16 USD | `-2.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 32,350.00 USD | 0.00 USD | 9,980.00 USD | `-2.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 22,370.00 USD | 0.00 USD | 2,570.00 USD | `-1.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 19,810.00 USD | 0.00 USD | 19,290.00 USD | `-1.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 516.91 USD | 0.00 USD | 516.91 USD | `-0.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1625` | 107.35 USD | 107.35 USD | 0.00 USD | `+0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 1,150.00 USD | 1,040.00 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1645` | 11,430.00 USD | 10,280.00 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1655` | 14,620.00 USD | 3,190.00 USD | 0.00 USD | `+1.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1665` | 59,090.00 USD | 44,470.00 USD | 0.00 USD | `+2.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1675` | 61,250.00 USD | 2,160.00 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1685` | 62,390.00 USD | 1,150.00 USD | 0.00 USD | `+3.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 64,420.00 USD | 2,030.00 USD | 0.00 USD | `+4.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 64,990.00 USD | 564.90 USD | 0.00 USD | `+5.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 66,790.00 USD | 1,800.00 USD | 0.00 USD | `+5.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 67,500.00 USD | 706.39 USD | 0.00 USD | `+6.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 68,160.00 USD | 661.31 USD | 0.00 USD | `+6.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 68,380.00 USD | 219.54 USD | 0.00 USD | `+7.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 69,470.00 USD | 1,100.00 USD | 0.00 USD | `+8.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 70,260.00 USD | 790.28 USD | 0.00 USD | `+8.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 70,600.00 USD | 336.40 USD | 0.00 USD | `+9.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 71,500.00 USD | 898.02 USD | 0.00 USD | `+9.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 76,530.00 USD | 5,030.00 USD | 0.00 USD | `+10.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 88,190.00 USD | 11,660.00 USD | 0.00 USD | `+11.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 99,030.00 USD | 10,840.00 USD | 0.00 USD | `+11.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 99,890.00 USD | 864.12 USD | 0.00 USD | `+12.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 102,420.00 USD | 2,520.00 USD | 0.00 USD | `+13.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 102,700.00 USD | 276.75 USD | 0.00 USD | `+13.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 102,830.00 USD | 128.68 USD | 0.00 USD | `+14.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 106,200.00 USD | 3,370.00 USD | 0.00 USD | `+14.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 109,900.00 USD | 3,700.00 USD | 0.00 USD | `+15.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 110,140.00 USD | 245.50 USD | 0.00 USD | `+16.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 110,680.00 USD | 531.47 USD | 0.00 USD | `+16.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 111,370.00 USD | 697.34 USD | 0.00 USD | `+17.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 111,590.00 USD | 222.24 USD | 0.00 USD | `+17.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 140,720.00 USD | 29,130.00 USD | 0.00 USD | `+18.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 147,790.00 USD | 7,070.00 USD | 0.00 USD | `+19.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 147,990.00 USD | 194.50 USD | 0.00 USD | `+19.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 148,130.00 USD | 137.77 USD | 0.00 USD | `+20.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 148,260.00 USD | 133.19 USD | 0.00 USD | `+21.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 152,010.00 USD | 3,750.00 USD | 0.00 USD | `+22.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 152,500.00 USD | 492.19 USD | 0.00 USD | `+22.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 175,250.00 USD | 22,750.00 USD | 0.00 USD | `+23.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 175,810.00 USD | 560.96 USD | 0.00 USD | `+24.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 197,150.00 USD | 21,340.00 USD | 0.00 USD | `+24.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 197,530.00 USD | 371.35 USD | 0.00 USD | `+25.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 283,420.00 USD | 85,900.00 USD | 0.00 USD | `+25.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 284,890.00 USD | 1,470.00 USD | 0.00 USD | `+26.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 285,060.00 USD | 174.20 USD | 0.00 USD | `+27.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 287,140.00 USD | 2,080.00 USD | 0.00 USD | `+27.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 287,390.00 USD | 252.51 USD | 0.00 USD | `+29.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 289,760.00 USD | 2,370.00 USD | 0.00 USD | `+29.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 290,120.00 USD | 356.72 USD | 0.00 USD | `+30.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 290,480.00 USD | 360.08 USD | 0.00 USD | `+32.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 290,840.00 USD | 361.76 USD | 0.00 USD | `+32.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 291,200.00 USD | 363.44 USD | 0.00 USD | `+33.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2175` | 291,570.00 USD | 365.12 USD | 0.00 USD | `+33.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 297,840.00 USD | 6,280.00 USD | 0.00 USD | `+34.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 298,210.00 USD | 368.47 USD | 0.00 USD | `+35.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 320,700.00 USD | 22,490.00 USD | 0.00 USD | `+35.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 321,040.00 USD | 333.91 USD | 0.00 USD | `+37.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 325,010.00 USD | 3,980.00 USD | 0.00 USD | `+37.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 325,390.00 USD | 378.55 USD | 0.00 USD | `+38.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 325,770.00 USD | 380.23 USD | 0.00 USD | `+39.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 329,610.00 USD | 3,840.00 USD | 0.00 USD | `+40.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 359,940.00 USD | 30,340.00 USD | 0.00 USD | `+41.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 364,210.00 USD | 4,260.00 USD | 0.00 USD | `+43.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 365,720.00 USD | 1,520.00 USD | 0.00 USD | `+43.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 386,950.00 USD | 21,230.00 USD | 0.00 USD | `+46.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 389,480.00 USD | 2,530.00 USD | 0.00 USD | `+46.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 409,200.00 USD | 19,720.00 USD | 0.00 USD | `+48.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 418,500.00 USD | 9,300.00 USD | 0.00 USD | `+48.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 420,410.00 USD | 1,910.00 USD | 0.00 USD | `+51.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 440,240.00 USD | 19,820.00 USD | 0.00 USD | `+51.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 440,790.00 USD | 551.23 USD | 0.00 USD | `+52.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 441,190.00 USD | 397.90 USD | 0.00 USD | `+53.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 445,520.00 USD | 4,330.00 USD | 0.00 USD | `+54.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 445,840.00 USD | 320.66 USD | 0.00 USD | `+54.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 461,720.00 USD | 15,880.00 USD | 0.00 USD | `+56.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 463,720.00 USD | 2,000.00 USD | 0.00 USD | `+56.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 466,270.00 USD | 2,550.00 USD | 0.00 USD | `+57.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 478,010.00 USD | 11,730.00 USD | 0.00 USD | `+57.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 483,160.00 USD | 5,160.00 USD | 0.00 USD | `+58.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 500,030.00 USD | 16,870.00 USD | 0.00 USD | `+59.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 526,820.00 USD | 26,790.00 USD | 0.00 USD | `+60.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 527,090.00 USD | 272.88 USD | 0.00 USD | `+66.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2755` | 527,210.00 USD | 114.99 USD | 0.00 USD | `+69.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 527,600.00 USD | 394.01 USD | 0.00 USD | `+70.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 527,980.00 USD | 375.53 USD | 0.00 USD | `+72.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 530,110.00 USD | 2,130.00 USD | 0.00 USD | `+75.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 530,690.00 USD | 579.27 USD | 0.00 USD | `+76.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 532,440.00 USD | 1,750.00 USD | 0.00 USD | `+78.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 532,540.00 USD | 101.21 USD | 0.00 USD | `+82.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 532,800.00 USD | 262.73 USD | 0.00 USD | `+82.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 534,240.00 USD | 1,440.00 USD | 0.00 USD | `+83.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 539,670.00 USD | 5,430.00 USD | 0.00 USD | `+85.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 545,100.00 USD | 5,430.00 USD | 0.00 USD | `+85.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 545,390.00 USD | 289.61 USD | 0.00 USD | `+88.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3065` | 545,880.00 USD | 487.09 USD | 0.00 USD | `+88.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3095` | 552,450.00 USD | 6,570.00 USD | 0.00 USD | `+90.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 557,630.00 USD | 5,180.00 USD | 0.00 USD | `+93.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3185` | 575,140.00 USD | 17,520.00 USD | 0.00 USD | `+96.17%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1310` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 6,470.00 USD | 4,610.00 USD | 5,180.00 USD |
| `7D` | `0.1313` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 0.00 USD | 4,010.00 USD | 2,660.00 USD |
| `7D` | `0.1316` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 9,620.00 USD | 4,840.00 USD | 2,140.00 USD |
| `7D` | `0.1319` | 8,420,000.00 USD | 0.00 USD | 8,420,000.00 USD | 4,630.00 USD | 0.00 USD | 18,380.00 USD |
| `7D` | `0.1322` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 5,580.00 USD | 2,780.00 USD | 17,750.00 USD |
| `7D` | `0.1325` | 8,370,000.00 USD | 0.00 USD | 8,370,000.00 USD | 0.00 USD | 5,550.00 USD | 4,560.00 USD |
| `7D` | `0.1328` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 19,000.00 USD | 7,370.00 USD | 8,920.00 USD |
| `7D` | `0.1331` | 8,320,000.00 USD | 0.00 USD | 8,320,000.00 USD | 13,420.00 USD | 4,240.00 USD | 7,210.00 USD |
| `7D` | `0.1334` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 3,580.00 USD | 3,230.00 USD | 7,810.00 USD |
| `7D` | `0.1337` | 8,280,000.00 USD | 0.00 USD | 8,280,000.00 USD | 2,830.00 USD | 4,520.00 USD | 19,560.00 USD |
| `7D` | `0.1340` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 6,330.00 USD | 5,970.00 USD | 13,100.00 USD |
| `7D` | `0.1343` | 8,230,000.00 USD | 0.00 USD | 8,230,000.00 USD | 0.00 USD | 5,790.00 USD | 13,540.00 USD |
| `7D` | `0.1346` | 8,210,000.00 USD | 0.00 USD | 8,210,000.00 USD | 33,130.00 USD | 5,000.00 USD | 21,650.00 USD |
| `7D` | `0.1349` | 8,150,000.00 USD | 0.00 USD | 8,150,000.00 USD | 4,450.00 USD | 2,140.00 USD | 19,300.00 USD |
| `7D` | `0.1352` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 11,390.00 USD | 6,290.00 USD | 13,140.00 USD |
| `7D` | `0.1355` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 7,540.00 USD | 9,000.00 USD | 6,460.00 USD |
| `7D` | `0.1358` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 25,150.00 USD | 9,870.00 USD | 5,370.00 USD |
| `7D` | `0.1361` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 8,700.00 USD | 1,930.00 USD | 6,320.00 USD |
| `7D` | `0.1364` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD |
| `7D` | `0.1367` | 7,990,000.00 USD | 0.00 USD | 7,990,000.00 USD | 4,500.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `0.1370` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD |
| `7D` | `0.1373` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 4,620.00 USD | 0.00 USD | 35,720.00 USD |
| `7D` | `0.1379` | 7,940,000.00 USD | 0.00 USD | 7,940,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD |
| `7D` | `0.1385` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 11,880.00 USD | 0.00 USD | 42,090.00 USD |
| `7D` | `0.1388` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1391` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD |
| `7D` | `0.1394` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD |
| `7D` | `0.1397` | 7,790,000.00 USD | 0.00 USD | 7,790,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD |
| `7D` | `0.1400` | 7,770,000.00 USD | 0.00 USD | 7,770,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD |
| `7D` | `0.1403` | 7,750,000.00 USD | 0.00 USD | 7,750,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1418` | 7,750,000.00 USD | 0.00 USD | 7,750,000.00 USD | 0.00 USD | 0.00 USD | 14,680.00 USD |
| `7D` | `0.1421` | 7,730,000.00 USD | 0.00 USD | 7,730,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD |
| `7D` | `0.1436` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD |
| `7D` | `0.1439` | 7,680,000.00 USD | 0.00 USD | 7,680,000.00 USD | 14,190.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1442` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 0.00 USD | 0.00 USD | 6,160.00 USD |
| `1D` | `0.1447` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 0.00 USD | 5,160.00 USD | 0.00 USD |
| `1D` | `0.1451` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 16,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1451` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 0.00 USD | 8,120.00 USD | 0.00 USD |
| `1D` | `0.1453` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 12,460.00 USD | 2,310.00 USD | 0.00 USD |
| `1D` | `0.1455` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1457` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 2,050.00 USD | 1,610.00 USD | 2,080.00 USD |
| `1D` | `0.1459` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 0.00 USD | 4,870.00 USD | 3,350.00 USD |
| `1D` | `0.1461` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 0.00 USD | 3,000.00 USD | 1,760.00 USD |
| `1D` | `0.1463` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 9,940.00 USD | 2,690.00 USD | 3,130.00 USD |
| `1D` | `0.1465` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 11,020.00 USD | 5,840.00 USD | 10,350.00 USD |
| `7D` | `0.1466` | 7,650,000.00 USD | 0.00 USD | 7,650,000.00 USD | 9,720.00 USD | 5,520.00 USD | 93,240.00 USD |
| `1D` | `0.1467` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 0.00 USD | 1,110.00 USD | 2,660.00 USD |
| `1D` | `0.1469` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 4,430.00 USD | 1,420.00 USD | 0.00 USD |
| `7D` | `0.1469` | 7,540,000.00 USD | 0.00 USD | 7,540,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD |
| `1D` | `0.1471` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 10,000.00 USD | 7,170.00 USD | 0.00 USD |
| `7D` | `0.1472` | 7,530,000.00 USD | 0.00 USD | 7,530,000.00 USD | 12,940.00 USD | 3,390.00 USD | 14,170.00 USD |
| `1D` | `0.1473` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 24,360.00 USD | 26,350.00 USD | 78,410.00 USD |
| `1D` | `0.1475` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 19,070.00 USD | 7,230.00 USD | 4,670.00 USD |
| `7D` | `0.1475` | 7,500,000.00 USD | 0.00 USD | 7,500,000.00 USD | 24,840.00 USD | 13,040.00 USD | 10,360.00 USD |
| `1D` | `0.1477` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 101,700.00 USD | 18,420.00 USD | 158,990.00 USD |
| `7D` | `0.1478` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 110,850.00 USD | 33,410.00 USD | 125,110.00 USD |
| `1D` | `0.1479` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 71,170.00 USD | 13,530.00 USD | 29,040.00 USD |
| `1D` | `0.1481` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 45,520.00 USD | 1,650.00 USD | 3,880.00 USD |
| `7D` | `0.1481` | 7,180,000.00 USD | 0.00 USD | 7,180,000.00 USD | 41,960.00 USD | 31,150.00 USD | 25,160.00 USD |
| `1D` | `0.1483` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 28,260.00 USD | 8,210.00 USD | 125,420.00 USD |
| `7D` | `0.1484` | 7,090,000.00 USD | 0.00 USD | 7,090,000.00 USD | 12,060.00 USD | 3,040.00 USD | 194,160.00 USD |
| `1D` | `0.1485` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 45,800.00 USD | 1,040.00 USD | 66,840.00 USD |
| `1D` | `0.1487` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 8,840.00 USD | 3,580.00 USD | 13,500.00 USD |
| `7D` | `0.1487` | 6,880,000.00 USD | 0.00 USD | 6,880,000.00 USD | 61,970.00 USD | 10,470.00 USD | 29,600.00 USD |
| `1D` | `0.1489` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 24,850.00 USD | 0.00 USD | 5,520.00 USD |
| `7D` | `0.1490` | 6,770,000.00 USD | 0.00 USD | 6,770,000.00 USD | 38,870.00 USD | 14,820.00 USD | 77,920.00 USD |
| `1D` | `0.1491` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 23,780.00 USD | 15,530.00 USD | 11,460.00 USD |
| `1D` | `0.1493` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 20,150.00 USD | 9,030.00 USD | 8,810.00 USD |
| `7D` | `0.1493` | 6,640,000.00 USD | 0.00 USD | 6,640,000.00 USD | 27,770.00 USD | 17,120.00 USD | 20,270.00 USD |
| `1D` | `0.1495` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 57,850.00 USD | 0.00 USD | 28,520.00 USD |
| `7D` | `0.1496` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 29,430.00 USD | 13,380.00 USD | 195,710.00 USD |
| `1D` | `0.1497` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 8,630.00 USD | 0.00 USD | 347.81 USD |
| `1D` | `0.1499` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 5,920.00 USD | 7,890.00 USD | 2,340.00 USD |
| `7D` | `0.1499` | 6,340,000.00 USD | 0.00 USD | 6,340,000.00 USD | 60,500.00 USD | 9,610.00 USD | 17,350.00 USD |
| `1D` | `0.1501` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 11,460.00 USD | 13,130.00 USD | 2,490.00 USD |
| `7D` | `0.1502` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 2,610.00 USD | 9,860.00 USD | 4,600.00 USD |
| `1D` | `0.1503` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 48,710.00 USD | 4,400.00 USD | 154,490.00 USD |
| `1D` | `0.1505` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 35,380.00 USD | 1,940.00 USD | 6,750.00 USD |
| `7D` | `0.1505` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 67,080.00 USD | 21,620.00 USD | 52,590.00 USD |
| `1D` | `0.1507` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 0.00 USD | 1,150.00 USD | 304,230.00 USD |
| `7D` | `0.1508` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 151,240.00 USD | 4,870.00 USD | 248,410.00 USD |
| `1D` | `0.1509` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 0.00 USD | 6,130.00 USD | 49,580.00 USD |
| `1D` | `0.1511` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 2,500.00 USD |
| `7D` | `0.1511` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 86,820.00 USD | 11,590.00 USD | 38,070.00 USD |
| `1D` | `0.1513` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 11,750.00 USD | 3,900.00 USD | 249,020.00 USD |
| `7D` | `0.1514` | 5,550,000.00 USD | 0.00 USD | 5,550,000.00 USD | 0.00 USD | 15,050.00 USD | 367,590.00 USD |
| `1D` | `0.1515` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 7,040.00 USD | 0.00 USD | 122,820.00 USD |
| `1D` | `0.1517` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 12,390.00 USD | 6,150.00 USD | 24,910.00 USD |
| `7D` | `0.1517` | 5,170,000.00 USD | 0.00 USD | 5,170,000.00 USD | 96,310.00 USD | 4,290.00 USD | 119,870.00 USD |
| `1D` | `0.1519` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 40,200.00 USD | 7,220.00 USD | 28,700.00 USD |
| `7D` | `0.1520` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 0.00 USD | 22,600.00 USD | 156,830.00 USD |
| `1D` | `0.1521` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 33,890.00 USD | 4,770.00 USD | 13,640.00 USD |
| `1D` | `0.1523` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 8,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1523` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 0.00 USD | 15,080.00 USD | 0.00 USD |
| `1D` | `0.1525` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 40,210.00 USD | 0.00 USD | 3,130.00 USD |
| `7D` | `0.1526` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 0.00 USD | 38,870.00 USD | 0.00 USD |
| `1D` | `0.1527` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 12,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1529` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 23,440.00 USD | 9,270.00 USD | 0.00 USD |
| `7D` | `0.1529` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD |
| `1D` | `0.1531` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 6,490.00 USD | 9,650.00 USD | 4,670.00 USD |
| `7D` | `0.1532` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 0.00 USD | 14,780.00 USD | 0.00 USD |
| `1D` | `0.1533` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 0.00 USD | 1,760.00 USD | 11,690.00 USD |
| `1D` | `0.1535` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 10,930.00 USD | 3,970.00 USD | 7,470.00 USD |
| `7D` | `0.1535` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 35,470.00 USD | 8,570.00 USD | 0.00 USD |
| `1D` | `0.1537` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 4,040.00 USD | 14,200.00 USD | 3,100.00 USD |
| `7D` | `0.1538` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 0.00 USD | 14,700.00 USD | 0.00 USD |
| `1D` | `0.1539` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD |
| `1D` | `0.1541` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 32,370.00 USD | 1,730.00 USD | 7,440.00 USD |
| `7D` | `0.1541` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD |
| `7D` | `0.1544` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD |
| `1D` | `0.1545` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 20,110.00 USD | 7,790.00 USD | 5,850.00 USD |
| `1D` | `0.1547` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 14,430.00 USD | 0.00 USD | 4,630.00 USD |
| `7D` | `0.1547` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 0.00 USD | 12,560.00 USD | 89,090.00 USD |
| `1D` | `0.1549` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 5,820.00 USD | 17,930.00 USD | 25,090.00 USD |
| `7D` | `0.1550` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 0.00 USD | 16,530.00 USD | 0.00 USD |
| `1D` | `0.1551` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 11,600.00 USD | 10,490.00 USD | 5,050.00 USD |
| `1D` | `0.1553` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 7,900.00 USD | 4,020.00 USD | 5,190.00 USD |
| `7D` | `0.1553` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 0.00 USD | 7,730.00 USD | 0.00 USD |
| `1D` | `0.1555` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 38,090.00 USD | 1,660.00 USD | 8,390.00 USD |
| `7D` | `0.1556` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD |
| `1D` | `0.1557` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 0.00 USD | 11,690.00 USD | 0.00 USD |
| `1D` | `0.1559` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 14,470.00 USD | 2,970.00 USD | 4,410.00 USD |
| `7D` | `0.1559` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD |
| `1D` | `0.1561` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 12,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1562` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD |
| `1D` | `0.1563` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 11,460.00 USD | 19,080.00 USD | 2,050.00 USD |
| `1D` | `0.1565` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 54,610.00 USD | 19,210.00 USD | 16,410.00 USD |
| `7D` | `0.1565` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 70,940.00 USD | 28,480.00 USD | 0.00 USD |
| `1D` | `0.1567` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 21,860.00 USD | 1,850.00 USD | 9,250.00 USD |
| `7D` | `0.1568` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 111,700.00 USD | 10,060.00 USD | 151,620.00 USD |
| `1D` | `0.1569` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 24,170.00 USD | 0.00 USD | 105,410.00 USD |
| `1D` | `0.1571` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 54,580.00 USD | 7,000.00 USD | 49,580.00 USD |
| `7D` | `0.1571` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 194,660.00 USD | 13,570.00 USD | 58,840.00 USD |
| `1D` | `0.1573` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 20,000.00 USD | 3,460.00 USD | 32,940.00 USD |
| `7D` | `0.1574` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 77,250.00 USD | 79,780.00 USD | 34,380.00 USD |
| `1D` | `0.1575` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | 4,810.00 USD | 11,190.00 USD |
| `1D` | `0.1577` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 28,900.00 USD | 29,200.00 USD | 14,400.00 USD |
| `7D` | `0.1577` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 31,130.00 USD | 118,000.00 USD | 0.00 USD |
| `1D` | `0.1579` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 11,910.00 USD | 0.00 USD | 12,500.00 USD |
| `7D` | `0.1580` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 216,490.00 USD | 46,710.00 USD | 22,580.00 USD |
| `1D` | `0.1581` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 19,190.00 USD | 8,040.00 USD | 2,850.00 USD |
| `1D` | `0.1583` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 86,410.00 USD | 25,280.00 USD | 29,500.00 USD |
| `7D` | `0.1583` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 70,150.00 USD | 17,610.00 USD | 24,510.00 USD |
| `1D` | `0.1585` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 16,540.00 USD | 17,270.00 USD | 6,620.00 USD |
| `7D` | `0.1586` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 59,180.00 USD | 0.00 USD | 23,800.00 USD |
| `1D` | `0.1587` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 42,230.00 USD | 26,600.00 USD | 49,230.00 USD |
| `1D` | `0.1589` | 954,650.00 USD | 0.00 USD | 954,650.00 USD | 9,280.00 USD | 10,830.00 USD | 38,700.00 USD |
| `7D` | `0.1589` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 59,670.00 USD | 12,590.00 USD | 89,310.00 USD |
| `1D` | `0.1591` | 895,830.00 USD | 0.00 USD | 895,830.00 USD | 15,370.00 USD | 19,200.00 USD | 38,490.00 USD |
| `7D` | `0.1592` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 16,720.00 USD |
| `1D` | `0.1593` | 822,760.00 USD | 0.00 USD | 822,760.00 USD | 14,950.00 USD | 32,920.00 USD | 30,140.00 USD |
| `1D` | `0.1595` | 744,750.00 USD | 0.00 USD | 744,750.00 USD | 10,260.00 USD | 1,210.00 USD | 3,490.00 USD |
| `7D` | `0.1595` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 0.00 USD | 37,130.00 USD | 0.00 USD |
| `1D` | `0.1597` | 729,790.00 USD | 0.00 USD | 729,790.00 USD | 11,790.00 USD | 0.00 USD | 6,030.00 USD |
| `7D` | `0.1598` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 0.00 USD | 86,680.00 USD | 75,810.00 USD |
| `1D` | `0.1599` | 711,970.00 USD | 0.00 USD | 711,970.00 USD | 0.00 USD | 7,580.00 USD | 0.00 USD |
| `1D` | `0.1601` | 704,390.00 USD | 0.00 USD | 704,390.00 USD | 21,340.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.1601` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 0.00 USD | 47,500.00 USD | 0.00 USD |
| `1D` | `0.1603` | 680,740.00 USD | 0.00 USD | 680,740.00 USD | 28,500.00 USD | 14,000.00 USD | 0.00 USD |
| `7D` | `0.1604` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 98,670.00 USD | 21,760.00 USD | 273,670.00 USD |
| `1D` | `0.1605` | 638,240.00 USD | 0.00 USD | 638,240.00 USD | 16,510.00 USD | 0.00 USD | 36,130.00 USD |
| `1D` | `0.1607` | 585,600.00 USD | 0.00 USD | 585,600.00 USD | 5,090.00 USD | 17,410.00 USD | 0.00 USD |
| `7D` | `0.1607` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 166,880.00 USD | 0.00 USD | 370,770.00 USD |
| `1D` | `0.1609` | 563,100.00 USD | 0.00 USD | 563,100.00 USD | 57,710.00 USD | 0.00 USD | 90,310.00 USD |
| `7D` | `0.1610` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 178,210.00 USD | 11,640.00 USD | 178,270.00 USD |
| `1D` | `0.1611` | 415,070.00 USD | 0.00 USD | 415,070.00 USD | 61,340.00 USD | 69,930.00 USD | 44,280.00 USD |
| `1D` | `0.1613` | 239,520.00 USD | 0.00 USD | 239,520.00 USD | 18,100.00 USD | 30,050.00 USD | 15,220.00 USD |
| `7D` | `0.1613` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 321,740.00 USD | 10,980.00 USD | 415,640.00 USD |
| `1D` | `0.1615` | 176,150.00 USD | 0.00 USD | 176,150.00 USD | 0.00 USD | 41,050.00 USD | 21,260.00 USD |
| `7D` | `0.1616` | 348,490.00 USD | 0.00 USD | 348,490.00 USD | 187,590.00 USD | 35,210.00 USD | 49,020.00 USD |
| `1D` | `0.1617` | 113,840.00 USD | 0.00 USD | 113,840.00 USD | 0.00 USD | 8,790.00 USD | 25,700.00 USD |
| `1D` | `0.1619` | 79,360.00 USD | 0.00 USD | 79,360.00 USD | 0.00 USD | 17,910.00 USD | 30,970.00 USD |
| `7D` | `0.1619` | 76,670.00 USD | 0.00 USD | 76,670.00 USD | 29,070.00 USD | 0.00 USD | 47,590.00 USD |
| `7D` | `0.1620` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1621` | 30,470.00 USD | 0.00 USD | 30,470.00 USD | 0.00 USD | 5,660.00 USD | 24,810.00 USD |
| `1D` | `0.1622` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1622` | 155,220.00 USD | 155,220.00 USD | 0.00 USD | 49,670.00 USD | 105,540.00 USD | 0.00 USD |
| `1D` | `0.1623` | 64,310.00 USD | 64,310.00 USD | 0.00 USD | 28,240.00 USD | 17,020.00 USD | 19,050.00 USD |
| `1D` | `0.1625` | 149,760.00 USD | 149,760.00 USD | 0.00 USD | 38,240.00 USD | 0.00 USD | 47,210.00 USD |
| `7D` | `0.1625` | 414,410.00 USD | 414,410.00 USD | 0.00 USD | 0.00 USD | 122,430.00 USD | 136,760.00 USD |
| `1D` | `0.1627` | 211,230.00 USD | 211,230.00 USD | 0.00 USD | 0.00 USD | 20,350.00 USD | 41,120.00 USD |
| `7D` | `0.1628` | 491,190.00 USD | 491,190.00 USD | 0.00 USD | 76,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1629` | 316,370.00 USD | 316,370.00 USD | 0.00 USD | 0.00 USD | 3,520.00 USD | 101,620.00 USD |
| `7D` | `0.1631` | 562,130.00 USD | 562,130.00 USD | 0.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1635` | 325,060.00 USD | 325,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD |
| `1D` | `0.1637` | 339,930.00 USD | 339,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD |
| `1D` | `0.1649` | 345,860.00 USD | 345,860.00 USD | 0.00 USD | 5,930.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1651` | 362,000.00 USD | 362,000.00 USD | 0.00 USD | 16,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1653` | 367,980.00 USD | 367,980.00 USD | 0.00 USD | 5,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1657` | 382,930.00 USD | 382,930.00 USD | 0.00 USD | 14,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1661` | 665,870.00 USD | 665,870.00 USD | 0.00 USD | 103,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1663` | 464,020.00 USD | 464,020.00 USD | 0.00 USD | 11,790.00 USD | 14,550.00 USD | 54,750.00 USD |
| `7D` | `0.1664` | 827,710.00 USD | 827,710.00 USD | 0.00 USD | 104,470.00 USD | 0.00 USD | 57,360.00 USD |
| `1D` | `0.1665` | 501,360.00 USD | 501,360.00 USD | 0.00 USD | 0.00 USD | 3,710.00 USD | 33,630.00 USD |
| `1D` | `0.1667` | 543,260.00 USD | 543,260.00 USD | 0.00 USD | 21,340.00 USD | 5,340.00 USD | 15,220.00 USD |
| `7D` | `0.1667` | 882,960.00 USD | 882,960.00 USD | 0.00 USD | 42,580.00 USD | 12,670.00 USD | 0.00 USD |
| `1D` | `0.1669` | 571,030.00 USD | 571,030.00 USD | 0.00 USD | 4,600.00 USD | 15,730.00 USD | 7,440.00 USD |
| `7D` | `0.1670` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 141,080.00 USD | 108,010.00 USD | 87,160.00 USD |
| `1D` | `0.1671` | 633,060.00 USD | 633,060.00 USD | 0.00 USD | 25,900.00 USD | 0.00 USD | 36,130.00 USD |
| `1D` | `0.1673` | 717,310.00 USD | 717,310.00 USD | 0.00 USD | 51,000.00 USD | 13,590.00 USD | 19,670.00 USD |
| `7D` | `0.1673` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 20,540.00 USD | 23,800.00 USD | 68,760.00 USD |
| `1D` | `0.1675` | 750,600.00 USD | 750,600.00 USD | 0.00 USD | 8,930.00 USD | 1,990.00 USD | 22,370.00 USD |
| `7D` | `0.1676` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 84,020.00 USD | 153,400.00 USD | 0.00 USD |
| `1D` | `0.1677` | 940,750.00 USD | 940,750.00 USD | 0.00 USD | 86,210.00 USD | 58,400.00 USD | 45,540.00 USD |
| `1D` | `0.1679` | 998,420.00 USD | 998,420.00 USD | 0.00 USD | 20,840.00 USD | 14,460.00 USD | 22,370.00 USD |
| `7D` | `0.1679` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 52,340.00 USD | 72,840.00 USD | 80,890.00 USD |
| `1D` | `0.1681` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 91,660.00 USD | 34,810.00 USD | 21,260.00 USD |
| `7D` | `0.1682` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 130,480.00 USD | 53,630.00 USD | 64,330.00 USD |
| `1D` | `0.1683` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 56,920.00 USD | 12,810.00 USD | 49,630.00 USD |
| `1D` | `0.1685` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 38,450.00 USD | 48,480.00 USD | 52,800.00 USD |
| `7D` | `0.1685` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 29,070.00 USD | 14,000.00 USD | 47,590.00 USD |
| `1D` | `0.1687` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 4,160.00 USD | 8,320.00 USD | 69,240.00 USD |
| `7D` | `0.1688` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 49,670.00 USD | 25,190.00 USD | 14,830.00 USD |
| `1D` | `0.1689` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 51,500.00 USD | 26,970.00 USD | 23,460.00 USD |
| `1D` | `0.1691` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 69,010.00 USD | 69,050.00 USD | 101,270.00 USD |
| `7D` | `0.1691` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 33,660.00 USD | 38,670.00 USD | 104,450.00 USD |
| `1D` | `0.1693` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 57,220.00 USD | 29,120.00 USD | 59,710.00 USD |
| `7D` | `0.1694` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 17,360.00 USD | 62,560.00 USD | 39,780.00 USD |
| `1D` | `0.1695` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 18,340.00 USD | 17,530.00 USD | 19,580.00 USD |
| `1D` | `0.1697` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 23,730.00 USD | 37,380.00 USD | 0.00 USD |
| `7D` | `0.1697` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 56,860.00 USD | 0.00 USD |
| `1D` | `0.1699` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 24,020.00 USD | 22,050.00 USD | 48,960.00 USD |
| `7D` | `0.1700` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD |
| `1D` | `0.1701` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 9,960.00 USD | 7,000.00 USD | 24,300.00 USD |
| `1D` | `0.1703` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 14,420.00 USD | 16,630.00 USD |
| `7D` | `0.1703` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 68,360.00 USD | 55,360.00 USD | 0.00 USD |
| `1D` | `0.1705` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 31,680.00 USD | 6,390.00 USD | 11,670.00 USD |
| `7D` | `0.1706` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 57,200.00 USD |
| `1D` | `0.1707` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 46,300.00 USD | 71,240.00 USD | 26,650.00 USD |
| `1D` | `0.1709` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 28,900.00 USD | 29,200.00 USD | 17,110.00 USD |
| `7D` | `0.1709` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 31,310.00 USD | 64,690.00 USD |
| `1D` | `0.1711` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 17,400.00 USD | 4,910.00 USD | 17,830.00 USD |
| `7D` | `0.1712` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 5,490.00 USD | 22,580.00 USD |
| `1D` | `0.1713` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 7,010.00 USD | 20,450.00 USD | 2,850.00 USD |
| `1D` | `0.1715` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 11,710.00 USD | 40,520.00 USD | 32,850.00 USD |
| `7D` | `0.1715` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 59,620.00 USD | 24,510.00 USD |
| `1D` | `0.1717` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 10,610.00 USD | 18,050.00 USD | 10,190.00 USD |
| `7D` | `0.1718` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 14,540.00 USD | 0.00 USD | 38,960.00 USD |
| `1D` | `0.1719` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 39,720.00 USD | 5,950.00 USD | 20,520.00 USD |
| `1D` | `0.1721` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 53,810.00 USD | 19,690.00 USD | 47,610.00 USD |
| `7D` | `0.1721` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 68,850.00 USD | 12,590.00 USD | 266,220.00 USD |
| `1D` | `0.1723` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 29,070.00 USD | 9,300.00 USD | 54,900.00 USD |
| `7D` | `0.1724` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 74,040.00 USD | 0.00 USD | 120,740.00 USD |
| `1D` | `0.1725` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 8,230.00 USD | 13,360.00 USD | 37,590.00 USD |
| `1D` | `0.1727` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 10,260.00 USD | 0.00 USD | 7,360.00 USD |
| `1D` | `0.1729` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 6,720.00 USD |
| `7D` | `0.1730` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 299,490.00 USD | 0.00 USD | 9,420.00 USD |
| `1D` | `0.1733` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 7,950.00 USD | 1,560.00 USD | 10,060.00 USD |
| `7D` | `0.1733` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 145,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1735` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 16,980.00 USD | 9,510.00 USD | 1,170.00 USD |
| `1D` | `0.1737` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 15,900.00 USD | 2,310.00 USD | 6,410.00 USD |
| `1D` | `0.1739` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 2,270.00 USD | 5,180.00 USD |
| `7D` | `0.1739` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD |
| `1D` | `0.1741` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD | 0.00 USD |
| `1D` | `0.1743` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD |
| `1D` | `0.1745` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 3,500.00 USD | 2,460.00 USD | 6,240.00 USD |
| `7D` | `0.1745` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1747` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25,680.00 USD |
| `7D` | `0.1748` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `0.1749` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 80,070.00 USD | 2,280.00 USD | 17,280.00 USD |
| `1D` | `0.1751` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 16,950.00 USD | 0.00 USD | 10,700.00 USD |
| `7D` | `0.1751` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 171,280.00 USD |
| `1D` | `0.1753` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 17,770.00 USD | 0.00 USD | 21,630.00 USD |
| `7D` | `0.1754` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 37,610.00 USD | 0.00 USD | 176,480.00 USD |
| `1D` | `0.1755` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 16,760.00 USD | 8,430.00 USD | 21,420.00 USD |
| `1D` | `0.1757` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 6,850.00 USD | 14,210.00 USD | 49,080.00 USD |
| `7D` | `0.1757` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 124,250.00 USD | 38,670.00 USD | 8,600.00 USD |
| `1D` | `0.1759` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 58,360.00 USD | 11,020.00 USD | 11,640.00 USD |
| `7D` | `0.1760` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 209,280.00 USD | 15,550.00 USD | 32,350.00 USD |
| `1D` | `0.1761` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 33,150.00 USD | 66,160.00 USD | 40,780.00 USD |
| `1D` | `0.1763` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 17,320.00 USD | 10,910.00 USD | 33,930.00 USD |
| `7D` | `0.1763` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 142,420.00 USD | 101,270.00 USD | 12,330.00 USD |
| `1D` | `0.1765` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 15,830.00 USD | 20,220.00 USD | 35,570.00 USD |
| `7D` | `0.1766` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 163,180.00 USD | 138,030.00 USD | 36,540.00 USD |
| `1D` | `0.1767` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 19,860.00 USD | 41,430.00 USD | 34,410.00 USD |
| `1D` | `0.1769` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 21,060.00 USD | 35,020.00 USD | 32,820.00 USD |
| `7D` | `0.1769` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 113,280.00 USD | 60,410.00 USD | 23,040.00 USD |
| `1D` | `0.1771` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 16,140.00 USD | 5,670.00 USD | 2,400.00 USD |
| `7D` | `0.1772` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 77,840.00 USD | 112,520.00 USD | 21,360.00 USD |
| `1D` | `0.1773` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 5,720.00 USD | 23,730.00 USD | 18,830.00 USD |
| `1D` | `0.1775` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 20,860.00 USD | 6,390.00 USD | 5,300.00 USD |
| `7D` | `0.1775` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 164,290.00 USD | 30,480.00 USD | 0.00 USD |
| `1D` | `0.1777` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 27,230.00 USD | 68,360.00 USD | 20,580.00 USD |
| `7D` | `0.1778` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 63,990.00 USD | 71,060.00 USD | 72,190.00 USD |
| `1D` | `0.1779` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 7,310.00 USD | 8,710.00 USD | 7,340.00 USD |
| `1D` | `0.1781` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 2,050.00 USD | 1,610.00 USD | 2,080.00 USD |
| `7D` | `0.1781` | 6,580,000.00 USD | 6,580,000.00 USD | 0.00 USD | 11,220.00 USD | 4,590.00 USD | 33,810.00 USD |
| `1D` | `0.1783` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 27,640.00 USD | 15,680.00 USD | 18,910.00 USD |
| `7D` | `0.1784` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD |
| `1D` | `0.1785` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 12,390.00 USD | 27,370.00 USD | 4,440.00 USD |
| `1D` | `0.1787` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 7,560.00 USD | 21,410.00 USD | 5,900.00 USD |
| `7D` | `0.1787` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD |
| `1D` | `0.1789` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 9,350.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1790` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 103,860.00 USD | 17,360.00 USD | 3,940.00 USD |
| `1D` | `0.1791` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,290.00 USD |
| `1D` | `0.1793` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 9,190.00 USD | 4,600.00 USD | 2,660.00 USD |
| `7D` | `0.1793` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 78,950.00 USD | 42,780.00 USD | 8,910.00 USD |
| `1D` | `0.1795` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 16,300.00 USD | 33,080.00 USD | 12,260.00 USD |
| `7D` | `0.1796` | 7,300,000.00 USD | 7,300,000.00 USD | 0.00 USD | 17,130.00 USD | 12,930.00 USD | 35,530.00 USD |
| `1D` | `0.1797` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 10,870.00 USD | 4,390.00 USD | 8,820.00 USD |
| `1D` | `0.1799` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 3,780.00 USD | 8,790.00 USD | 11,410.00 USD |
| `7D` | `0.1799` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 0.00 USD | 11,280.00 USD | 68,230.00 USD |
| `1D` | `0.1801` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 3,730.00 USD | 17,760.00 USD | 13,800.00 USD |
| `7D` | `0.1802` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 48,220.00 USD | 36,020.00 USD | 33,890.00 USD |
| `1D` | `0.1803` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 2,390.00 USD | 10,580.00 USD | 14,430.00 USD |
| `1D` | `0.1805` | 4,660,000.00 USD | 4,660,000.00 USD | 0.00 USD | 4,010.00 USD | 4,760.00 USD | 6,870.00 USD |
| `7D` | `0.1805` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 11,410.00 USD | 38,130.00 USD | 5,320.00 USD |
| `1D` | `0.1807` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 11,560.00 USD | 11,500.00 USD | 9,360.00 USD |
| `7D` | `0.1808` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 23,650.00 USD | 52,750.00 USD | 73,440.00 USD |
| `1D` | `0.1809` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 2,490.00 USD | 7,210.00 USD | 1,970.00 USD |
| `1D` | `0.1811` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 13,300.00 USD | 4,850.00 USD | 3,980.00 USD |
| `7D` | `0.1811` | 7,810,000.00 USD | 7,810,000.00 USD | 0.00 USD | 64,990.00 USD | 26,860.00 USD | 18,880.00 USD |
| `1D` | `0.1813` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 7,950.00 USD | 35,640.00 USD | 8,750.00 USD |
| `7D` | `0.1814` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 28,070.00 USD | 26,510.00 USD | 65,950.00 USD |
| `1D` | `0.1815` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 7,040.00 USD | 1,040.00 USD | 9,760.00 USD |
| `1D` | `0.1817` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 9,410.00 USD | 9,530.00 USD |
| `7D` | `0.1817` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 64,770.00 USD | 10,470.00 USD | 29,600.00 USD |
| `1D` | `0.1819` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 2,620.00 USD | 5,520.00 USD |
| `7D` | `0.1820` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 52,150.00 USD | 54,880.00 USD | 38,610.00 USD |
| `1D` | `0.1821` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD | 2,390.00 USD |
| `1D` | `0.1823` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 10,830.00 USD | 7,660.00 USD | 5,380.00 USD |
| `7D` | `0.1823` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 62,540.00 USD | 18,340.00 USD | 50,880.00 USD |
| `1D` | `0.1825` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 3,290.00 USD | 3,020.00 USD | 8,810.00 USD |
| `7D` | `0.1826` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 45,250.00 USD | 9,890.00 USD | 14,210.00 USD |
| `1D` | `0.1827` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 5,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1829` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 20,880.00 USD | 28,120.00 USD | 51,250.00 USD |
| `7D` | `0.1832` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 79,470.00 USD | 18,130.00 USD | 35,210.00 USD |
| `7D` | `0.1835` | 8,650,000.00 USD | 8,650,000.00 USD | 0.00 USD | 13,840.00 USD | 7,930.00 USD | 16,530.00 USD |
| `7D` | `0.1838` | 8,830,000.00 USD | 8,830,000.00 USD | 0.00 USD | 54,990.00 USD | 11,590.00 USD | 106,440.00 USD |
| `7D` | `0.1841` | 8,900,000.00 USD | 8,900,000.00 USD | 0.00 USD | 28,940.00 USD | 12,910.00 USD | 30,500.00 USD |
| `7D` | `0.1844` | 8,980,000.00 USD | 8,980,000.00 USD | 0.00 USD | 20,990.00 USD | 3,900.00 USD | 56,660.00 USD |
| `7D` | `0.1847` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 5,770.00 USD | 11,590.00 USD | 20,400.00 USD |
| `7D` | `0.1850` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 77,110.00 USD | 51,400.00 USD | 51,650.00 USD |
| `7D` | `0.1853` | 9,300,000.00 USD | 9,300,000.00 USD | 0.00 USD | 46,730.00 USD | 0.00 USD | 56,290.00 USD |
| `7D` | `0.1854` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 4,750.00 USD | 4,290.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `183.01M` | Total OI Tokens: `1,130,704,046.1 ARB`
  * 1h OI Change: `-0.79%` | 4h OI Change: `-2.55%` | 24h OI Change: `-14.26%`
  * Exchange Breakdown: Binance=`40.30M` | Bybit=`25.70M` | OKX=`13.85M` | Hyperliquid=`12.87M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `7.94K` | Last 24h: `11.04K` | Last 3d: `13.14K` | Last 7d: `51.59K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0001%` | **USDT Bitget** | `-0.0029%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `58.91%` | `41.09%` | `1.43` | 2,290,000.00 USD |
| `15M` | `Binance` | `47.51%` | `52.49%` | `0.91` | 710,090.00 USD |
| `15M` | `OKX` | `55.47%` | `44.53%` | `1.25` | 281,540.00 USD |
| `15M` | `Bybit` | `56.59%` | `43.41%` | `1.30` | 103,420.00 USD |
| `15M` | `KuCoin` | `54.15%` | `45.85%` | `1.18` | 42,490.00 USD |
| `15M` | `Gate` | `56.17%` | `43.83%` | `1.28` | 127,350.00 USD |
| `15M` | `Bitget` | `55.01%` | `44.99%` | `1.22` | 172,200.00 USD |
| `15M` | `BingX` | `61.91%` | `38.09%` | `1.63` | 45,470.00 USD |
| `15M` | `MEXC` | `87.19%` | `12.81%` | `6.81` | 317,340.00 USD |
| `15M` | `Bitunix` | `65.91%` | `34.09%` | `1.93` | 35,410.00 USD |
| `15M` | `Hyperliquid` | `38.01%` | `61.99%` | `0.61` | 40,410.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `67.92%` | `32.08%` | `2.12` | 99,300.00 USD |
| `15M` | `Crypto.com` | `40.01%` | `59.99%` | `0.67` | 2,300.00 USD |
| `15M` | `WhiteBIT` | `64.37%` | `35.63%` | `1.81` | 291,340.00 USD |
| `15M` | `HTX` | `15.81%` | `84.19%` | `0.19` | 334.47 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `83.51%` | `16.49%` | `5.06` | 5,410.00 USD |
| `15M` | `Aster` | `85.94%` | `14.06%` | `6.11` | 39.23 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `14.09%` | `85.91%` | `0.16` | 12,470.00 USD |
| `15M` | `Whale Positions` | `47.51%` | `52.49%` | `0.91` | 710,090.00 USD |
| `15M` | `Global Accounts` | `58.91%` | `41.09%` | `1.43` | 2,290,000.00 USD |
| `1H` | `ARB` | `48.27%` | `51.73%` | `0.93` | 9,470,000.00 USD |
| `1H` | `Binance` | `43.19%` | `56.81%` | `0.76` | 3,150,000.00 USD |
| `1H` | `OKX` | `45.1%` | `54.9%` | `0.82` | 1,220,000.00 USD |
| `1H` | `Bybit` | `46.14%` | `53.86%` | `0.86` | 1,010,000.00 USD |
| `1H` | `KuCoin` | `52.12%` | `47.88%` | `1.09` | 160,970.00 USD |
| `1H` | `Gate` | `51.34%` | `48.66%` | `1.06` | 247,650.00 USD |
| `1H` | `Bitget` | `54.68%` | `45.32%` | `1.21` | 590,630.00 USD |
| `1H` | `BingX` | `37.22%` | `62.78%` | `0.59` | 743,930.00 USD |
| `1H` | `MEXC` | `52.87%` | `47.13%` | `1.12` | 973,420.00 USD |
| `1H` | `Bitunix` | `50.12%` | `49.88%` | `1.00` | 134,110.00 USD |
| `1H` | `Hyperliquid` | `38.92%` | `61.08%` | `0.64` | 137,780.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.22%` | `50.78%` | `0.97` | 322,380.00 USD |
| `1H` | `Crypto.com` | `54.47%` | `45.53%` | `1.20` | 5,100.00 USD |
| `1H` | `WhiteBIT` | `82.33%` | `17.67%` | `4.66` | 678,470.00 USD |
| `1H` | `HTX` | `47.16%` | `52.84%` | `0.89` | 2,310.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `20.29%` | `79.71%` | `0.25` | 38,700.00 USD |
| `1H` | `Aster` | `6.67%` | `93.33%` | `0.07` | 4,660.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `37.73%` | `62.27%` | `0.61` | 45,800.00 USD |
| `1H` | `Whale Positions` | `43.19%` | `56.81%` | `0.76` | 3,150,000.00 USD |
| `1H` | `Global Accounts` | `48.27%` | `51.73%` | `0.93` | 9,470,000.00 USD |
| `4H` | `ARB` | `45.96%` | `54.04%` | `0.85` | 14,690,000.00 USD |
| `4H` | `Binance` | `52.14%` | `47.86%` | `1.09` | 4,470,000.00 USD |
| `4H` | `OKX` | `49.24%` | `50.76%` | `0.97` | 1,840,000.00 USD |
| `4H` | `Bybit` | `45.48%` | `54.52%` | `0.83` | 1,530,000.00 USD |
| `4H` | `KuCoin` | `50.1%` | `49.9%` | `1.00` | 615,600.00 USD |
| `4H` | `Gate` | `44.74%` | `55.26%` | `0.81` | 164,540.00 USD |
| `4H` | `Bitget` | `62.29%` | `37.71%` | `1.65` | 301,760.00 USD |
| `4H` | `BingX` | `18.63%` | `81.37%` | `0.23` | 1,970,000.00 USD |
| `4H` | `MEXC` | `46.65%` | `53.35%` | `0.87` | 758,630.00 USD |
| `4H` | `Bitunix` | `32.83%` | `67.17%` | `0.49` | 188,750.00 USD |
| `4H` | `Hyperliquid` | `40.38%` | `59.62%` | `0.68` | 112,020.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.99%` | `50.01%` | `1.00` | 2,280,000.00 USD |
| `4H` | `Crypto.com` | `3.16%` | `96.84%` | `0.03` | 120.77 USD |
| `4H` | `WhiteBIT` | `59.61%` | `40.39%` | `1.48` | 384,190.00 USD |
| `4H` | `HTX` | `37.41%` | `62.59%` | `0.60` | 5,820.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `92.56%` | `7.44%` | `12.44` | 7,650.00 USD |
| `4H` | `Aster` | `84.68%` | `15.32%` | `5.53` | 1,030.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `61.45%` | `38.55%` | `1.59` | 80,790.00 USD |
| `4H` | `Whale Positions` | `52.14%` | `47.86%` | `1.09` | 4,470,000.00 USD |
| `4H` | `Global Accounts` | `45.96%` | `54.04%` | `0.85` | 14,690,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1638` | `0.1644` | `0.1638` | `0.1657` | `0.1634` | 1,167,470.68 USD | 690,008.18 USD | 477,462.51 USD | 212,545.67 USD | `+18.21%` | `32B / 3S` |
| `5:00 UTC` | `0.1650` | `0.1648` | `0.1650` | `0.1651` | `0.1640` | 1,330,863.86 USD | 714,476.79 USD | 616,387.06 USD | 98,089.73 USD | `+7.37%` | `15B / 7S` |
| `0:00 UTC` | `0.1641` | `0.1647` | `0.1641` | `0.1657` | `0.1639` | 2,406,571.88 USD | 1,201,675.03 USD | 1,204,896.84 USD | -3,221.81 USD | `-0.13%` | `31B / 55S` |
| `5:00 UTC` | `0.1641` | `0.1639` | `0.1641` | `0.1647` | `0.1634` | 780,398.32 USD | 282,316.37 USD | 498,081.96 USD | -215,765.59 USD | `-27.65%` | `7B / 50S` |
| `0:00 UTC` | `0.1639` | `0.1637` | `0.1639` | `0.1646` | `0.1631` | 946,588.03 USD | 498,466.74 USD | 448,121.29 USD | 50,345.45 USD | `+5.32%` | `36B / 23S` |
| `5:00 UTC` | `0.1625` | `0.1631` | `0.1625` | `0.1640` | `0.1624` | 778,400.97 USD | 315,731.23 USD | 462,669.74 USD | -146,938.51 USD | `-18.88%` | `22B / 62S` |
| `0:00 UTC` | `0.1629` | `0.1625` | `0.1629` | `0.1632` | `0.1619` | 775,902.97 USD | 309,320.91 USD | 466,582.05 USD | -157,261.14 USD | `-20.27%` | `13B / 34S` |
| `5:00 UTC` | `0.1623` | `0.1620` | `0.1623` | `0.1624` | `0.1615` | 562,907.20 USD | 223,683.16 USD | 339,224.04 USD | -115,540.88 USD | `-20.53%` | `7B / 21S` |
| `0:00 UTC` | `0.1620` | `0.1617` | `0.1620` | `0.1623` | `0.1611` | 779,913.00 USD | 372,491.97 USD | 407,421.03 USD | -34,929.06 USD | `-4.48%` | `22B / 23S` |
| `5:00 UTC` | `0.1616` | `0.1617` | `0.1616` | `0.1621` | `0.1615` | 48,893.95 USD | 16,673.49 USD | 32,220.46 USD | -15,546.98 USD | `-31.80%` | `7B / 14S` |

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
| `5m` | 5,660.00 USD | 96,080.00 USD | **`ACCUMULATION`** |
| `15m` | -4,360.00 USD | -93,890.00 USD | **`DISTRIBUTION`** |
| `30m` | -79,930.00 USD | -229,810.00 USD | **`DISTRIBUTION`** |
| `1h` | -411,690.00 USD | -771,700.00 USD | **`DISTRIBUTION`** |
| `2h` | -286,240.00 USD | -1,170,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -588,880.00 USD | -1,390,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -544,510.00 USD | -3,360,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -380,600.00 USD | -1,580,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -586,920.00 USD | -2,370,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,110,000.00 USD | -11,530,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,620,000.00 USD | -37,800,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,630,000.00 USD | -165,910,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+5.66K` | 15m=`-4.36K` | 1h=`-411.69K` | 24h=`-2.11M`
* Futures Capital Netflows: 5m=`+96.08K` | 15m=`-93.89K` | 1h=`-771.70K` | 24h=`-11.53M`
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
  * `2026-10-30 15:12:05 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:05 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:05 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:34:05 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:05 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:15:05 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:15:05 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)


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
