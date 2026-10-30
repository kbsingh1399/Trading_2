# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 10:34:49 IST` (`2026-10-30 05:04:49 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1627` | `0.1638` | `0.1626` | `0.1636` | `3,821,207` | 624,120.05 USD | -214,015.92 USD | `-34.29%` | -8,240,963.23 USD | `-1.87` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.1636` | `0.1639` | `0.1633` | `0.1637` | `3,613,833` | 591,211.60 USD | -270,951.99 USD | `-45.83%` | -8,511,915.22 USD | `-1.98` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.1637` | `0.1648` | `0.1635` | `0.1640` | `3,452,437` | 567,035.86 USD | -29,718.72 USD | `-5.24%` | -8,541,633.94 USD | `-0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1605` | `0.1625` | `0.1603` | `0.1623` | `10,414,481` | 1,684,179.28 USD | -162,133.53 USD | `-9.63%` | -7,851,834.07 USD | `-0.43` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1623` | `0.1639` | `0.1618` | `0.1637` | `11,341,584` | 1,849,966.09 USD | -639,400.43 USD | `-34.56%` | -8,491,234.50 USD | `-1.53` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1637` | `0.1648` | `0.1635` | `0.1640` | `3,452,437` | 567,035.86 USD | -29,718.72 USD | `-5.24%` | -8,520,953.22 USD | `+0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1560` | `0.1585` | `0.1553` | `0.1580` | `20,448,591` | 3,216,248.24 USD | 252,196.82 USD | `+7.84%` | -7,911,945.27 USD | `+0.61` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1580` | `0.1639` | `0.1577` | `0.1637` | `36,120,104` | 5,820,548.12 USD | -303,641.20 USD | `-5.22%` | -8,215,586.47 USD | `+0.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1637` | `0.1648` | `0.1635` | `0.1640` | `3,439,400` | 564,898.01 USD | -31,306.44 USD | `-5.54%` | -8,246,892.91 USD | `+0.35` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -6,590,804.13 USD | `-1.67` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -7,211,742.64 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1648` | `0.1577` | `0.1640` | `39,572,541` | 6,387,583.99 USD | -333,359.92 USD | `-5.22%` | -7,545,102.56 USD | `+0.80` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -1,669,122.15 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -2,866,580.15 USD | `-0.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -6,590,804.13 USD | `-1.67` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -7,211,742.64 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1648` | `0.1577` | `0.1640` | `39,572,541` | 6,387,583.99 USD | -333,359.92 USD | `-5.22%` | -7,545,102.56 USD | `+0.80` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:34:32 IST` |

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
| `Live` | `Long Liquidation` | `0.0355` | 107.73 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0385` | 5,590.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0395` | 385.59 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 110.22 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 170.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0475` | 167,030.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 109.52 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 289.43 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 3,420.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0555` | 1,900.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 15,650.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 865.75 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 2,300.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 3,930.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 373.83 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 106,660.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 313.22 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 976.14 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 2,970.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 6,000.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 111.58 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,760.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 226.17 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 63,580.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 14,940.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 4,630.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 20,720.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 627.22 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 2,460.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 19,570.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 162.28 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 362.62 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 4,830.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 626.82 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 2,420.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 814.24 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 1,510.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 1,990.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 873.55 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 3,960.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 9,660.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 1,850.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1015` | 9,760.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 8,960.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 4,570.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 9,470.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 8,600.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 1,230.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 1,060.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 12,400.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 115,850.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 14,360.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 425.50 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1125` | 284.46 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 281.48 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 8,950.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 1,450.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 1,480.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 6,120.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 32,130.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 1,830.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 537.83 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 303.75 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 17,890.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 50,790.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 1,060.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 134.66 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 29,370.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 11,500.00 USD | 976,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,130.00 USD | 964,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1304` | 8,390,000.00 USD | 8,390,000.00 USD | 4,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1305` | 16,660.00 USD | 962,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1310` | 8,390,000.00 USD | 8,390,000.00 USD | 6,470.00 USD | 4,610.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1313` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 4,010.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1315` | 9,010.00 USD | 945,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1316` | 8,370,000.00 USD | 8,370,000.00 USD | 9,620.00 USD | 4,840.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1319` | 8,350,000.00 USD | 8,350,000.00 USD | 4,630.00 USD | 0.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1322` | 8,330,000.00 USD | 8,330,000.00 USD | 5,580.00 USD | 2,780.00 USD | 12,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1325` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 3,040.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1325` | 4,810.00 USD | 936,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1328` | 8,300,000.00 USD | 8,300,000.00 USD | 19,000.00 USD | 7,370.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1331` | 8,260,000.00 USD | 8,260,000.00 USD | 13,420.00 USD | 4,240.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1334` | 8,240,000.00 USD | 8,240,000.00 USD | 3,580.00 USD | 3,230.00 USD | 7,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1335` | 72,590.00 USD | 932,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1337` | 8,220,000.00 USD | 8,220,000.00 USD | 2,830.00 USD | 4,520.00 USD | 19,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1340` | 8,200,000.00 USD | 8,200,000.00 USD | 6,330.00 USD | 5,970.00 USD | 13,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1343` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 5,790.00 USD | 13,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1345` | 29,490.00 USD | 859,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1346` | 8,150,000.00 USD | 8,150,000.00 USD | 33,130.00 USD | 5,000.00 USD | 21,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1349` | 8,090,000.00 USD | 8,090,000.00 USD | 4,450.00 USD | 2,140.00 USD | 19,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1352` | 8,070,000.00 USD | 8,070,000.00 USD | 11,390.00 USD | 6,290.00 USD | 13,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1355` | 8,030,000.00 USD | 8,030,000.00 USD | 7,540.00 USD | 9,000.00 USD | 6,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1355` | 3,540.00 USD | 829,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1358` | 8,010,000.00 USD | 8,010,000.00 USD | 25,150.00 USD | 9,870.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1361` | 7,970,000.00 USD | 7,970,000.00 USD | 8,700.00 USD | 1,930.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1364` | 7,950,000.00 USD | 7,950,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 10,630.00 USD | 826,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1367` | 7,930,000.00 USD | 7,930,000.00 USD | 4,500.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1370` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1373` | 7,920,000.00 USD | 7,920,000.00 USD | 4,620.00 USD | 0.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1375` | 13,710.00 USD | 815,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1379` | 7,880,000.00 USD | 7,880,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1385` | 7,860,000.00 USD | 7,860,000.00 USD | 11,880.00 USD | 0.00 USD | 42,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 5,580.00 USD | 802,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1388` | 7,810,000.00 USD | 7,810,000.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1391` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1393` | 4,440,000.00 USD | 4,440,000.00 USD | 9,960.00 USD | 2,340.00 USD | 74,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1394` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 17,790.00 USD | 796,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1396` | 4,360,000.00 USD | 4,360,000.00 USD | 13,480.00 USD | 6,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1397` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1399` | 4,340,000.00 USD | 4,340,000.00 USD | 5,720.00 USD | 953.16 USD | 1,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1400` | 7,710,000.00 USD | 7,710,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1402` | 4,330,000.00 USD | 4,330,000.00 USD | 9,130.00 USD | 2,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1403` | 7,690,000.00 USD | 7,690,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1405` | 4,320,000.00 USD | 4,320,000.00 USD | 2,140.00 USD | 3,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 1,360.00 USD | 778,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1411` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 3,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1415` | 22,710.00 USD | 777,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1418` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 0.00 USD | 14,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1420` | 4,310,000.00 USD | 4,310,000.00 USD | 3,280.00 USD | 1,560.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1421` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1423` | 4,300,000.00 USD | 4,300,000.00 USD | 6,100.00 USD | 4,580.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 499,000.00 USD | 754,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1426` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1429` | 4,280,000.00 USD | 4,280,000.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1430` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 0.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1433` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 0.00 USD | 5,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1435` | 4,280,000.00 USD | 4,280,000.00 USD | 6,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 19,630.00 USD | 255,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1436` | 7,640,000.00 USD | 7,640,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1438` | 4,270,000.00 USD | 4,270,000.00 USD | 4,370.00 USD | 3,590.00 USD | 23,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1439` | 7,610,000.00 USD | 7,610,000.00 USD | 23,950.00 USD | 0.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1441` | 4,240,000.00 USD | 4,240,000.00 USD | 17,680.00 USD | 0.00 USD | 1,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1442` | 7,580,000.00 USD | 7,580,000.00 USD | 3,450.00 USD | 5,260.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1444` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 9,660.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 9,510.00 USD | 236,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1447` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 5,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1450` | 4,200,000.00 USD | 4,200,000.00 USD | 13,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1451` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 10,680.00 USD | 5,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1453` | 4,190,000.00 USD | 4,190,000.00 USD | 15,450.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1454` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 9,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 91,680.00 USD | 226,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1456` | 4,170,000.00 USD | 4,170,000.00 USD | 3,450.00 USD | 1,610.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1459` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 4,870.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1462` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 5,690.00 USD | 1,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1465` | 4,150,000.00 USD | 4,150,000.00 USD | 17,970.00 USD | 5,840.00 USD | 17,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 35,140.00 USD | 134,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1466` | 7,540,000.00 USD | 7,540,000.00 USD | 9,720.00 USD | 5,520.00 USD | 93,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1468` | 4,110,000.00 USD | 4,110,000.00 USD | 12,090.00 USD | 2,700.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1469` | 7,430,000.00 USD | 7,430,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1471` | 4,080,000.00 USD | 4,080,000.00 USD | 10,130.00 USD | 14,560.00 USD | 1,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1472` | 7,420,000.00 USD | 7,420,000.00 USD | 12,940.00 USD | 3,400.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1474` | 4,060,000.00 USD | 4,060,000.00 USD | 45,330.00 USD | 27,310.00 USD | 76,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1475` | 7,390,000.00 USD | 7,390,000.00 USD | 24,840.00 USD | 13,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 84,080.00 USD | 99,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1477` | 3,910,000.00 USD | 3,910,000.00 USD | 108,940.00 USD | 23,730.00 USD | 158,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1478` | 7,350,000.00 USD | 7,350,000.00 USD | 110,850.00 USD | 33,410.00 USD | 125,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1480` | 3,620,000.00 USD | 3,620,000.00 USD | 96,250.00 USD | 11,170.00 USD | 25,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1481` | 7,080,000.00 USD | 7,080,000.00 USD | 41,960.00 USD | 31,150.00 USD | 19,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1483` | 3,490,000.00 USD | 3,490,000.00 USD | 41,250.00 USD | 4,610.00 USD | 126,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1484` | 6,990,000.00 USD | 6,990,000.00 USD | 12,060.00 USD | 3,040.00 USD | 188,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,290.00 USD | 15,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1486` | 3,310,000.00 USD | 3,310,000.00 USD | 46,070.00 USD | 0.00 USD | 65,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1487` | 6,790,000.00 USD | 6,790,000.00 USD | 61,970.00 USD | 10,470.00 USD | 20,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1489` | 3,200,000.00 USD | 3,200,000.00 USD | 33,690.00 USD | 0.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1490` | 6,690,000.00 USD | 6,690,000.00 USD | 28,940.00 USD | 9,780.00 USD | 77,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1492` | 3,160,000.00 USD | 3,160,000.00 USD | 24,040.00 USD | 18,130.00 USD | 9,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1493` | 6,580,000.00 USD | 6,580,000.00 USD | 27,770.00 USD | 17,120.00 USD | 20,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1495` | 3,110,000.00 USD | 3,110,000.00 USD | 71,540.00 USD | 0.00 USD | 28,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 7,610.00 USD | 13,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1496` | 6,510,000.00 USD | 6,510,000.00 USD | 29,430.00 USD | 13,380.00 USD | 195,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1498` | 3,010,000.00 USD | 3,010,000.00 USD | 8,630.00 USD | 4,640.00 USD | 347.81 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1499` | 6,270,000.00 USD | 6,270,000.00 USD | 60,500.00 USD | 9,610.00 USD | 17,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1501` | 2,990,000.00 USD | 2,990,000.00 USD | 20,980.00 USD | 16,380.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1502` | 6,190,000.00 USD | 6,190,000.00 USD | 2,610.00 USD | 9,860.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1504` | 2,950,000.00 USD | 2,950,000.00 USD | 84,100.00 USD | 6,340.00 USD | 160,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1505` | 6,170,000.00 USD | 6,170,000.00 USD | 67,080.00 USD | 21,620.00 USD | 52,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1507` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 1,150.00 USD | 307,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1508` | 6,030,000.00 USD | 6,030,000.00 USD | 151,240.00 USD | 4,870.00 USD | 248,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1510` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 6,130.00 USD | 50,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1511` | 5,620,000.00 USD | 5,620,000.00 USD | 86,820.00 USD | 11,590.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1513` | 2,330,000.00 USD | 2,330,000.00 USD | 11,750.00 USD | 3,900.00 USD | 250,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1514` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 15,050.00 USD | 367,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1516` | 2,070,000.00 USD | 2,070,000.00 USD | 12,230.00 USD | 0.00 USD | 141,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1517` | 5,100,000.00 USD | 5,100,000.00 USD | 96,310.00 USD | 4,290.00 USD | 119,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1519` | 1,920,000.00 USD | 1,920,000.00 USD | 47,400.00 USD | 13,370.00 USD | 35,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1520` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 22,600.00 USD | 156,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1522` | 1,820,000.00 USD | 1,820,000.00 USD | 33,890.00 USD | 4,770.00 USD | 13,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1523` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 15,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1525` | 1,770,000.00 USD | 1,770,000.00 USD | 48,970.00 USD | 0.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1526` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 38,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1528` | 1,710,000.00 USD | 1,710,000.00 USD | 29,740.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1529` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1531` | 1,680,000.00 USD | 1,680,000.00 USD | 12,670.00 USD | 18,920.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1532` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 14,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1534` | 1,650,000.00 USD | 1,650,000.00 USD | 10,930.00 USD | 1,760.00 USD | 11,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1535` | 4,630,000.00 USD | 4,630,000.00 USD | 35,470.00 USD | 8,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1537` | 1,620,000.00 USD | 1,620,000.00 USD | 4,040.00 USD | 18,160.00 USD | 10,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1538` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 14,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1540` | 1,590,000.00 USD | 1,590,000.00 USD | 27,770.00 USD | 4,030.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1541` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1543` | 1,550,000.00 USD | 1,550,000.00 USD | 4,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1544` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1545` | 5,720.00 USD | 5,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1546` | 1,550,000.00 USD | 1,550,000.00 USD | 24,160.00 USD | 7,790.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1547` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 12,560.00 USD | 89,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1549` | 1,510,000.00 USD | 1,510,000.00 USD | 16,200.00 USD | 17,930.00 USD | 29,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1550` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 16,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1552` | 1,450,000.00 USD | 1,450,000.00 USD | 8,630.00 USD | 10,490.00 USD | 5,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1553` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 7,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1555` | 1,420,000.00 USD | 1,420,000.00 USD | 34,930.00 USD | 5,680.00 USD | 13,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1556` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1558` | 1,370,000.00 USD | 1,370,000.00 USD | 6,990.00 USD | 11,690.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1559` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1561` | 1,340,000.00 USD | 1,340,000.00 USD | 12,360.00 USD | 2,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1562` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1564` | 1,330,000.00 USD | 1,330,000.00 USD | 14,590.00 USD | 38,290.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1565` | 4,220,000.00 USD | 4,220,000.00 USD | 70,940.00 USD | 28,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1567` | 1,270,000.00 USD | 1,270,000.00 USD | 87,320.00 USD | 1,850.00 USD | 25,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1568` | 4,120,000.00 USD | 4,120,000.00 USD | 111,700.00 USD | 10,060.00 USD | 151,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1570` | 1,150,000.00 USD | 1,150,000.00 USD | 27,380.00 USD | 0.00 USD | 105,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1571` | 3,850,000.00 USD | 3,850,000.00 USD | 194,660.00 USD | 13,600.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1573` | 1,020,000.00 USD | 1,020,000.00 USD | 49,900.00 USD | 5,380.00 USD | 64,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1574` | 3,580,000.00 USD | 3,580,000.00 USD | 64,070.00 USD | 79,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1577` | 3,440,000.00 USD | 3,440,000.00 USD | 31,130.00 USD | 112,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1580` | 3,290,000.00 USD | 3,290,000.00 USD | 216,490.00 USD | 41,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1582` | 899,150.00 USD | 899,150.00 USD | 49,700.00 USD | 0.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1583` | 3,030,000.00 USD | 3,030,000.00 USD | 70,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1585` | 843,430.00 USD | 843,430.00 USD | 52,520.00 USD | 22,800.00 USD | 6,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1586` | 2,960,000.00 USD | 2,960,000.00 USD | 44,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1588` | 761,480.00 USD | 761,480.00 USD | 20,600.00 USD | 31,780.00 USD | 53,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1589` | 2,920,000.00 USD | 2,920,000.00 USD | 34,830.00 USD | 0.00 USD | 89,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1591` | 656,090.00 USD | 656,090.00 USD | 0.00 USD | 19,870.00 USD | 33,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1594` | 603,150.00 USD | 603,150.00 USD | 0.00 USD | 23,960.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1595` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 37,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1597` | 574,520.00 USD | 574,520.00 USD | 0.00 USD | 0.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1598` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 86,680.00 USD | 75,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1600` | 568,490.00 USD | 568,490.00 USD | 0.00 USD | 9,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1601` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 47,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1603` | 558,600.00 USD | 558,600.00 USD | 44,810.00 USD | 3,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1604` | 2,550,000.00 USD | 2,550,000.00 USD | 72,300.00 USD | 21,810.00 USD | 273,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1605` | 3,930.00 USD | 3,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1607` | 2,180,000.00 USD | 2,180,000.00 USD | 166,880.00 USD | 0.00 USD | 312,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1609` | 509,950.00 USD | 509,950.00 USD | 48,780.00 USD | 7,790.00 USD | 82,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1610` | 1,700,000.00 USD | 1,700,000.00 USD | 178,210.00 USD | 0.00 USD | 178,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1612` | 370,630.00 USD | 370,630.00 USD | 0.00 USD | 23,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1613` | 1,340,000.00 USD | 1,340,000.00 USD | 321,740.00 USD | 0.00 USD | 381,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1615` | 346,800.00 USD | 346,800.00 USD | 0.00 USD | 18,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1615` | 4,130.00 USD | 8,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1616` | 641,420.00 USD | 641,420.00 USD | 187,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1622` | 453,830.00 USD | 453,830.00 USD | 0.00 USD | 80,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1624` | 328,690.00 USD | 328,690.00 USD | 60,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1625` | 373,470.00 USD | 373,470.00 USD | 0.00 USD | 122,430.00 USD | 103,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1625` | 1,810.00 USD | 9,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1627` | 268,170.00 USD | 268,170.00 USD | 38,240.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1628` | 147,720.00 USD | 147,720.00 USD | 76,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1630` | 227,440.00 USD | 227,440.00 USD | 23,880.00 USD | 3,520.00 USD | 101,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1631` | 70,940.00 USD | 70,940.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1633` | 98,410.00 USD | 98,410.00 USD | 98,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1635` | 1,630.00 USD | 11,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1636` | 34,250.00 USD | 34,250.00 USD | 0.00 USD | 10,690.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1637` | 23,560.00 USD | 23,560.00 USD | 0.00 USD | 0.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1639` | 51,420.00 USD | 51,420.00 USD | 14,240.00 USD | 0.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1640` | 52,800.00 USD | 52,800.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1642` | 138,140.00 USD | 138,140.00 USD | 31,400.00 USD | 36,980.00 USD | 18,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1643` | 122,450.00 USD | 122,450.00 USD | 0.00 USD | 25,110.00 USD | 44,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1645` | 191,760.00 USD | 191,760.00 USD | 17,870.00 USD | 24,710.00 USD | 11,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1645` | 118.90 USD | 11,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1646` | 136,230.00 USD | 136,230.00 USD | 0.00 USD | 13,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1648` | 220,930.00 USD | 220,930.00 USD | 17,270.00 USD | 3,360.00 USD | 8,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1649` | 148,000.00 USD | 148,000.00 USD | 0.00 USD | 11,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1651` | 272,270.00 USD | 272,270.00 USD | 32,910.00 USD | 8,040.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1654` | 304,940.00 USD | 304,940.00 USD | 3,500.00 USD | 4,350.00 USD | 24,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1655` | 184,620.00 USD | 184,620.00 USD | 0.00 USD | 36,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1657` | 392,980.00 USD | 392,980.00 USD | 15,910.00 USD | 63,310.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1658` | 247,170.00 USD | 247,170.00 USD | 10,890.00 USD | 0.00 USD | 51,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1660` | 464,920.00 USD | 464,920.00 USD | 8,220.00 USD | 12,910.00 USD | 50,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1661` | 361,940.00 USD | 361,940.00 USD | 103,750.00 USD | 11,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1663` | 596,050.00 USD | 596,050.00 USD | 55,130.00 USD | 14,550.00 USD | 61,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1664` | 617,570.00 USD | 617,570.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1665` | 547.98 USD | 12,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1666` | 705,560.00 USD | 705,560.00 USD | 22,170.00 USD | 9,050.00 USD | 78,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1667` | 672,810.00 USD | 672,810.00 USD | 42,580.00 USD | 12,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1669` | 723,170.00 USD | 723,170.00 USD | 4,600.00 USD | 5,570.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1670` | 982,750.00 USD | 982,750.00 USD | 114,710.00 USD | 108,060.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1672` | 773,720.00 USD | 773,720.00 USD | 46,590.00 USD | 3,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1673` | 1,030,000.00 USD | 1,030,000.00 USD | 20,540.00 USD | 23,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1675` | 815,420.00 USD | 815,420.00 USD | 20,040.00 USD | 1,990.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1676` | 1,250,000.00 USD | 1,250,000.00 USD | 84,020.00 USD | 141,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1678` | 848,420.00 USD | 848,420.00 USD | 27,610.00 USD | 0.00 USD | 5,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1679` | 1,400,000.00 USD | 1,400,000.00 USD | 52,340.00 USD | 61,850.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1681` | 954,980.00 USD | 954,980.00 USD | 94,970.00 USD | 8,580.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1682` | 1,570,000.00 USD | 1,570,000.00 USD | 130,480.00 USD | 18,420.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1684` | 1,070,000.00 USD | 1,070,000.00 USD | 50,170.00 USD | 30,620.00 USD | 37,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1685` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1687` | 1,150,000.00 USD | 1,150,000.00 USD | 13,000.00 USD | 9,810.00 USD | 52,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1688` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1690` | 1,210,000.00 USD | 1,210,000.00 USD | 25,050.00 USD | 12,840.00 USD | 18,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1691` | 1,740,000.00 USD | 1,740,000.00 USD | 33,660.00 USD | 38,670.00 USD | 71,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1693` | 1,430,000.00 USD | 1,430,000.00 USD | 87,330.00 USD | 74,940.00 USD | 60,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1694` | 1,860,000.00 USD | 1,860,000.00 USD | 17,360.00 USD | 62,560.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1696` | 1,490,000.00 USD | 1,490,000.00 USD | 23,530.00 USD | 19,390.00 USD | 19,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1697` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 56,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1699` | 1,620,000.00 USD | 1,620,000.00 USD | 26,000.00 USD | 57,580.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1700` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1702` | 1,670,000.00 USD | 1,670,000.00 USD | 9,960.00 USD | 1,920.00 USD | 34,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1703` | 2,140,000.00 USD | 2,140,000.00 USD | 55,170.00 USD | 55,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1705` | 1,710,000.00 USD | 1,710,000.00 USD | 20,880.00 USD | 20,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1706` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1708` | 1,840,000.00 USD | 1,840,000.00 USD | 46,300.00 USD | 66,430.00 USD | 15,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1709` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1711` | 1,860,000.00 USD | 1,860,000.00 USD | 5,500.00 USD | 4,910.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1714` | 1,870,000.00 USD | 1,870,000.00 USD | 3,630.00 USD | 12,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1715` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1715` | 2,370.00 USD | 14,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1717` | 1,940,000.00 USD | 1,940,000.00 USD | 11,710.00 USD | 37,270.00 USD | 19,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1718` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 15,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1720` | 2,000,000.00 USD | 2,000,000.00 USD | 47,600.00 USD | 1,590.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1721` | 2,620,000.00 USD | 2,620,000.00 USD | 44,020.00 USD | 0.00 USD | 266,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1723` | 2,140,000.00 USD | 2,140,000.00 USD | 54,130.00 USD | 17,650.00 USD | 66,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1724` | 2,800,000.00 USD | 2,800,000.00 USD | 74,040.00 USD | 0.00 USD | 104,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1726` | 2,160,000.00 USD | 2,160,000.00 USD | 8,230.00 USD | 3,180.00 USD | 12,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1729` | 2,180,000.00 USD | 2,180,000.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1730` | 3,140,000.00 USD | 3,140,000.00 USD | 330,670.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1732` | 2,190,000.00 USD | 2,190,000.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1733` | 3,290,000.00 USD | 3,290,000.00 USD | 145,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1735` | 2,230,000.00 USD | 2,230,000.00 USD | 18,250.00 USD | 11,060.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1738` | 2,250,000.00 USD | 2,250,000.00 USD | 15,900.00 USD | 3,450.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1739` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1741` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 4,490.00 USD | 8,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1744` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 2,460.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1745` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1745` | 4,260.00 USD | 18,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1747` | 2,320,000.00 USD | 2,320,000.00 USD | 3,500.00 USD | 0.00 USD | 31,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1748` | 3,490,000.00 USD | 3,490,000.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1750` | 2,420,000.00 USD | 2,420,000.00 USD | 80,070.00 USD | 2,280.00 USD | 22,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1751` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 226,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1753` | 2,480,000.00 USD | 2,480,000.00 USD | 34,710.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1754` | 3,980,000.00 USD | 3,980,000.00 USD | 37,610.00 USD | 0.00 USD | 229,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1756` | 2,580,000.00 USD | 2,580,000.00 USD | 23,610.00 USD | 11,970.00 USD | 60,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1757` | 4,150,000.00 USD | 4,150,000.00 USD | 124,250.00 USD | 38,670.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1759` | 2,680,000.00 USD | 2,680,000.00 USD | 58,360.00 USD | 21,690.00 USD | 21,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1760` | 4,430,000.00 USD | 4,430,000.00 USD | 224,680.00 USD | 25,210.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1762` | 2,870,000.00 USD | 2,870,000.00 USD | 50,470.00 USD | 68,300.00 USD | 66,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1763` | 4,830,000.00 USD | 4,830,000.00 USD | 240,020.00 USD | 139,590.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1765` | 2,950,000.00 USD | 2,950,000.00 USD | 15,830.00 USD | 28,990.00 USD | 43,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1766` | 5,230,000.00 USD | 5,230,000.00 USD | 163,180.00 USD | 200,720.00 USD | 36,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1768` | 3,100,000.00 USD | 3,100,000.00 USD | 19,860.00 USD | 70,050.00 USD | 52,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1769` | 5,470,000.00 USD | 5,470,000.00 USD | 113,280.00 USD | 105,160.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1771` | 3,160,000.00 USD | 3,160,000.00 USD | 37,200.00 USD | 12,060.00 USD | 16,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1772` | 5,680,000.00 USD | 5,680,000.00 USD | 77,840.00 USD | 112,520.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1774` | 3,220,000.00 USD | 3,220,000.00 USD | 12,400.00 USD | 23,730.00 USD | 24,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1775` | 5,870,000.00 USD | 5,870,000.00 USD | 164,290.00 USD | 30,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1775` | 316.07 USD | 19,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1777` | 3,360,000.00 USD | 3,360,000.00 USD | 41,420.00 USD | 74,750.00 USD | 20,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1778` | 6,130,000.00 USD | 6,130,000.00 USD | 63,990.00 USD | 71,060.00 USD | 123,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1780` | 3,390,000.00 USD | 3,390,000.00 USD | 7,310.00 USD | 10,310.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1781` | 6,180,000.00 USD | 6,180,000.00 USD | 11,220.00 USD | 4,590.00 USD | 33,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1783` | 3,450,000.00 USD | 3,450,000.00 USD | 27,640.00 USD | 15,680.00 USD | 18,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1784` | 6,410,000.00 USD | 6,410,000.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1785` | 138.82 USD | 19,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1786` | 3,500,000.00 USD | 3,500,000.00 USD | 16,960.00 USD | 28,560.00 USD | 7,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1787` | 6,580,000.00 USD | 6,580,000.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1789` | 3,540,000.00 USD | 3,540,000.00 USD | 9,350.00 USD | 20,220.00 USD | 5,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1790` | 6,700,000.00 USD | 6,700,000.00 USD | 103,860.00 USD | 17,360.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1792` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 3,490.00 USD | 7,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1793` | 6,830,000.00 USD | 6,830,000.00 USD | 78,950.00 USD | 42,780.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1795` | 3,630,000.00 USD | 3,630,000.00 USD | 33,150.00 USD | 35,780.00 USD | 18,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1796` | 6,900,000.00 USD | 6,900,000.00 USD | 17,130.00 USD | 12,930.00 USD | 35,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1798` | 3,680,000.00 USD | 3,680,000.00 USD | 11,000.00 USD | 17,120.00 USD | 21,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1799` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 11,280.00 USD | 68,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1801` | 3,730,000.00 USD | 3,730,000.00 USD | 9,540.00 USD | 19,700.00 USD | 11,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1802` | 7,080,000.00 USD | 7,080,000.00 USD | 48,220.00 USD | 36,030.00 USD | 23,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1804` | 3,760,000.00 USD | 3,760,000.00 USD | 10,530.00 USD | 14,470.00 USD | 14,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1805` | 7,140,000.00 USD | 7,140,000.00 USD | 11,410.00 USD | 38,130.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1807` | 3,790,000.00 USD | 3,790,000.00 USD | 10,730.00 USD | 9,130.00 USD | 7,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1808` | 7,290,000.00 USD | 7,290,000.00 USD | 23,650.00 USD | 52,750.00 USD | 73,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1810` | 3,810,000.00 USD | 3,810,000.00 USD | 8,220.00 USD | 11,640.00 USD | 2,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1811` | 3,820,000.00 USD | 3,820,000.00 USD | 3,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1811` | 7,390,000.00 USD | 7,390,000.00 USD | 64,990.00 USD | 26,860.00 USD | 13,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1814` | 7,510,000.00 USD | 7,510,000.00 USD | 28,070.00 USD | 26,510.00 USD | 60,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1817` | 7,600,000.00 USD | 7,600,000.00 USD | 64,770.00 USD | 10,470.00 USD | 20,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1820` | 7,740,000.00 USD | 7,740,000.00 USD | 42,210.00 USD | 54,880.00 USD | 38,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1823` | 7,920,000.00 USD | 7,920,000.00 USD | 62,540.00 USD | 13,300.00 USD | 105,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1826` | 8,090,000.00 USD | 8,090,000.00 USD | 90,200.00 USD | 9,890.00 USD | 66,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1829` | 8,190,000.00 USD | 8,190,000.00 USD | 20,880.00 USD | 28,120.00 USD | 51,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1832` | 8,360,000.00 USD | 8,360,000.00 USD | 94,870.00 USD | 27,790.00 USD | 50,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1835` | 8,570,000.00 USD | 8,570,000.00 USD | 111,430.00 USD | 46,260.00 USD | 52,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1838` | 8,900,000.00 USD | 8,900,000.00 USD | 144,340.00 USD | 74,280.00 USD | 106,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1841` | 9,060,000.00 USD | 9,060,000.00 USD | 56,160.00 USD | 57,660.00 USD | 45,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1844` | 9,180,000.00 USD | 9,180,000.00 USD | 48,920.00 USD | 3,900.00 USD | 72,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1847` | 9,220,000.00 USD | 9,220,000.00 USD | 5,770.00 USD | 11,590.00 USD | 20,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1850` | 9,480,000.00 USD | 9,480,000.00 USD | 77,110.00 USD | 77,020.00 USD | 103,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1853` | 9,700,000.00 USD | 9,700,000.00 USD | 62,090.00 USD | 9,590.00 USD | 146,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1856` | 9,840,000.00 USD | 9,840,000.00 USD | 31,410.00 USD | 21,030.00 USD | 87,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1859` | 9,970,000.00 USD | 9,970,000.00 USD | 47,740.00 USD | 6,920.00 USD | 77,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1862` | 10,080,000.00 USD | 10,080,000.00 USD | 60,020.00 USD | 13,950.00 USD | 37,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1865` | 10,160,000.00 USD | 10,160,000.00 USD | 22,320.00 USD | 18,650.00 USD | 40,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1868` | 10,310,000.00 USD | 10,310,000.00 USD | 88,110.00 USD | 31,750.00 USD | 24,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1871` | 10,450,000.00 USD | 10,450,000.00 USD | 83,830.00 USD | 27,560.00 USD | 34,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1874` | 10,620,000.00 USD | 10,620,000.00 USD | 71,850.00 USD | 48,780.00 USD | 51,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1877` | 10,690,000.00 USD | 10,690,000.00 USD | 27,840.00 USD | 22,370.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1880` | 10,750,000.00 USD | 10,750,000.00 USD | 36,800.00 USD | 14,700.00 USD | 8,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1883` | 10,780,000.00 USD | 10,780,000.00 USD | 14,000.00 USD | 3,530.00 USD | 9,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1886` | 10,820,000.00 USD | 10,820,000.00 USD | 9,250.00 USD | 31,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1915` | 1,600.00 USD | 20,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1925` | 543.50 USD | 21,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1945` | 623.68 USD | 22,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1975` | 150.10 USD | 22,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2005` | 2,940.00 USD | 25,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2045` | 184.58 USD | 25,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2055` | 11,590.00 USD | 36,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2085` | 198.08 USD | 37,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2095` | 164.23 USD | 37,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2135` | 15,690.00 USD | 52,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 41,330.00 USD | 94,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2175` | 213.22 USD | 94,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2195` | 87,800.00 USD | 182,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2205` | 26,240.00 USD | 208,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 114.52 USD | 208,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2255` | 154.78 USD | 208,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 6,820.00 USD | 215,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2325` | 24,460.00 USD | 240,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 15,930.00 USD | 256,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 102.62 USD | 256,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 796.25 USD | 256,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2445` | 4,930.00 USD | 261,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2455` | 231.97 USD | 262,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2465` | 49,300.00 USD | 311,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2545` | 546.54 USD | 311,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 3,870.00 USD | 315,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2575` | 28,910.00 USD | 344,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 52,620.00 USD | 397,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 154.94 USD | 397,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2685` | 226.51 USD | 397,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 13,240.00 USD | 410,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 214.21 USD | 411,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 11,600.00 USD | 422,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2795` | 482.84 USD | 423,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2895` | 295,560.00 USD | 718,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 187.26 USD | 718,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2925` | 794.52 USD | 719,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3035` | 482.72 USD | 720,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3045` | 2,320.00 USD | 722,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3075` | 6,290.00 USD | 728,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3085` | 363.72 USD | 729,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 11,930.00 USD | 741,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3145` | 482.22 USD | 741,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

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
| `7D` | `0.1304` | 8,390,000.00 USD | 0.00 USD | 8,390,000.00 USD | 4,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1310` | 8,390,000.00 USD | 0.00 USD | 8,390,000.00 USD | 6,470.00 USD | 4,610.00 USD | 4,440.00 USD |
| `7D` | `0.1313` | 8,370,000.00 USD | 0.00 USD | 8,370,000.00 USD | 0.00 USD | 4,010.00 USD | 2,660.00 USD |
| `7D` | `0.1316` | 8,370,000.00 USD | 0.00 USD | 8,370,000.00 USD | 9,620.00 USD | 4,840.00 USD | 2,140.00 USD |
| `7D` | `0.1319` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 4,630.00 USD | 0.00 USD | 18,380.00 USD |
| `7D` | `0.1322` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 5,580.00 USD | 2,780.00 USD | 12,990.00 USD |
| `7D` | `0.1325` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 0.00 USD | 3,040.00 USD | 4,560.00 USD |
| `7D` | `0.1328` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 19,000.00 USD | 7,370.00 USD | 8,920.00 USD |
| `7D` | `0.1331` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 13,420.00 USD | 4,240.00 USD | 7,210.00 USD |
| `7D` | `0.1334` | 8,240,000.00 USD | 0.00 USD | 8,240,000.00 USD | 3,580.00 USD | 3,230.00 USD | 7,810.00 USD |
| `7D` | `0.1337` | 8,220,000.00 USD | 0.00 USD | 8,220,000.00 USD | 2,830.00 USD | 4,520.00 USD | 19,560.00 USD |
| `7D` | `0.1340` | 8,200,000.00 USD | 0.00 USD | 8,200,000.00 USD | 6,330.00 USD | 5,970.00 USD | 13,100.00 USD |
| `7D` | `0.1343` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 0.00 USD | 5,790.00 USD | 13,540.00 USD |
| `7D` | `0.1346` | 8,150,000.00 USD | 0.00 USD | 8,150,000.00 USD | 33,130.00 USD | 5,000.00 USD | 21,650.00 USD |
| `7D` | `0.1349` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 4,450.00 USD | 2,140.00 USD | 19,300.00 USD |
| `7D` | `0.1352` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 11,390.00 USD | 6,290.00 USD | 13,140.00 USD |
| `7D` | `0.1355` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 7,540.00 USD | 9,000.00 USD | 6,460.00 USD |
| `7D` | `0.1358` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 25,150.00 USD | 9,870.00 USD | 5,370.00 USD |
| `7D` | `0.1361` | 7,970,000.00 USD | 0.00 USD | 7,970,000.00 USD | 8,700.00 USD | 1,930.00 USD | 6,320.00 USD |
| `7D` | `0.1364` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD |
| `7D` | `0.1367` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 4,500.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `0.1370` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD |
| `7D` | `0.1373` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 4,620.00 USD | 0.00 USD | 35,720.00 USD |
| `7D` | `0.1379` | 7,880,000.00 USD | 0.00 USD | 7,880,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD |
| `7D` | `0.1385` | 7,860,000.00 USD | 0.00 USD | 7,860,000.00 USD | 11,880.00 USD | 0.00 USD | 42,090.00 USD |
| `7D` | `0.1388` | 7,810,000.00 USD | 0.00 USD | 7,810,000.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1391` | 7,790,000.00 USD | 0.00 USD | 7,790,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD |
| `1D` | `0.1393` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 9,960.00 USD | 2,340.00 USD | 74,280.00 USD |
| `7D` | `0.1394` | 7,730,000.00 USD | 0.00 USD | 7,730,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD |
| `1D` | `0.1396` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 13,480.00 USD | 6,230.00 USD | 0.00 USD |
| `7D` | `0.1397` | 7,730,000.00 USD | 0.00 USD | 7,730,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD |
| `1D` | `0.1399` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 5,720.00 USD | 953.16 USD | 1,480.00 USD |
| `7D` | `0.1400` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD |
| `1D` | `0.1402` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 9,130.00 USD | 2,100.00 USD | 0.00 USD |
| `7D` | `0.1403` | 7,690,000.00 USD | 0.00 USD | 7,690,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1405` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 2,140.00 USD | 3,150.00 USD | 0.00 USD |
| `1D` | `0.1411` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 0.00 USD | 3,980.00 USD | 0.00 USD |
| `7D` | `0.1418` | 7,690,000.00 USD | 0.00 USD | 7,690,000.00 USD | 0.00 USD | 0.00 USD | 14,680.00 USD |
| `1D` | `0.1420` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 3,280.00 USD | 1,560.00 USD | 1,170.00 USD |
| `7D` | `0.1421` | 7,670,000.00 USD | 0.00 USD | 7,670,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD |
| `1D` | `0.1423` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 6,100.00 USD | 4,580.00 USD | 8,910.00 USD |
| `1D` | `0.1426` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD |
| `1D` | `0.1429` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1430` | 7,650,000.00 USD | 0.00 USD | 7,650,000.00 USD | 0.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `0.1433` | 7,650,000.00 USD | 0.00 USD | 7,650,000.00 USD | 0.00 USD | 0.00 USD | 5,270.00 USD |
| `1D` | `0.1435` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 6,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1436` | 7,640,000.00 USD | 0.00 USD | 7,640,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD |
| `1D` | `0.1438` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 4,370.00 USD | 3,590.00 USD | 23,000.00 USD |
| `7D` | `0.1439` | 7,610,000.00 USD | 0.00 USD | 7,610,000.00 USD | 23,950.00 USD | 0.00 USD | 3,610.00 USD |
| `1D` | `0.1441` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 17,680.00 USD | 0.00 USD | 1,850.00 USD |
| `7D` | `0.1442` | 7,580,000.00 USD | 0.00 USD | 7,580,000.00 USD | 3,450.00 USD | 5,260.00 USD | 6,160.00 USD |
| `1D` | `0.1444` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 0.00 USD | 9,660.00 USD | 2,970.00 USD |
| `1D` | `0.1447` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 0.00 USD | 5,160.00 USD | 0.00 USD |
| `1D` | `0.1450` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 13,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1451` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 0.00 USD | 10,680.00 USD | 5,150.00 USD |
| `1D` | `0.1453` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 15,450.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.1454` | 7,550,000.00 USD | 0.00 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 9,030.00 USD |
| `1D` | `0.1456` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 3,450.00 USD | 1,610.00 USD | 2,080.00 USD |
| `1D` | `0.1459` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 0.00 USD | 4,870.00 USD | 3,350.00 USD |
| `1D` | `0.1462` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 0.00 USD | 5,690.00 USD | 1,760.00 USD |
| `1D` | `0.1465` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 17,970.00 USD | 5,840.00 USD | 17,070.00 USD |
| `7D` | `0.1466` | 7,540,000.00 USD | 0.00 USD | 7,540,000.00 USD | 9,720.00 USD | 5,520.00 USD | 93,240.00 USD |
| `1D` | `0.1468` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 12,090.00 USD | 2,700.00 USD | 8,060.00 USD |
| `7D` | `0.1469` | 7,430,000.00 USD | 0.00 USD | 7,430,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD |
| `1D` | `0.1471` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 10,130.00 USD | 14,560.00 USD | 1,210.00 USD |
| `7D` | `0.1472` | 7,420,000.00 USD | 0.00 USD | 7,420,000.00 USD | 12,940.00 USD | 3,400.00 USD | 14,170.00 USD |
| `1D` | `0.1474` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 45,330.00 USD | 27,310.00 USD | 76,930.00 USD |
| `7D` | `0.1475` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 24,840.00 USD | 13,040.00 USD | 0.00 USD |
| `1D` | `0.1477` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 108,940.00 USD | 23,730.00 USD | 158,030.00 USD |
| `7D` | `0.1478` | 7,350,000.00 USD | 0.00 USD | 7,350,000.00 USD | 110,850.00 USD | 33,410.00 USD | 125,110.00 USD |
| `1D` | `0.1480` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 96,250.00 USD | 11,170.00 USD | 25,870.00 USD |
| `7D` | `0.1481` | 7,080,000.00 USD | 0.00 USD | 7,080,000.00 USD | 41,960.00 USD | 31,150.00 USD | 19,470.00 USD |
| `1D` | `0.1483` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 41,250.00 USD | 4,610.00 USD | 126,170.00 USD |
| `7D` | `0.1484` | 6,990,000.00 USD | 0.00 USD | 6,990,000.00 USD | 12,060.00 USD | 3,040.00 USD | 188,220.00 USD |
| `1D` | `0.1486` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 46,070.00 USD | 0.00 USD | 65,260.00 USD |
| `7D` | `0.1487` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 61,970.00 USD | 10,470.00 USD | 20,080.00 USD |
| `1D` | `0.1489` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 33,690.00 USD | 0.00 USD | 8,920.00 USD |
| `7D` | `0.1490` | 6,690,000.00 USD | 0.00 USD | 6,690,000.00 USD | 28,940.00 USD | 9,780.00 USD | 77,920.00 USD |
| `1D` | `0.1492` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 24,040.00 USD | 18,130.00 USD | 9,580.00 USD |
| `7D` | `0.1493` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 27,770.00 USD | 17,120.00 USD | 20,270.00 USD |
| `1D` | `0.1495` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 71,540.00 USD | 0.00 USD | 28,520.00 USD |
| `7D` | `0.1496` | 6,510,000.00 USD | 0.00 USD | 6,510,000.00 USD | 29,430.00 USD | 13,380.00 USD | 195,710.00 USD |
| `1D` | `0.1498` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 8,630.00 USD | 4,640.00 USD | 347.81 USD |
| `7D` | `0.1499` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 60,500.00 USD | 9,610.00 USD | 17,350.00 USD |
| `1D` | `0.1501` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 20,980.00 USD | 16,380.00 USD | 5,560.00 USD |
| `7D` | `0.1502` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 2,610.00 USD | 9,860.00 USD | 4,600.00 USD |
| `1D` | `0.1504` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 84,100.00 USD | 6,340.00 USD | 160,460.00 USD |
| `7D` | `0.1505` | 6,170,000.00 USD | 0.00 USD | 6,170,000.00 USD | 67,080.00 USD | 21,620.00 USD | 52,590.00 USD |
| `1D` | `0.1507` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 0.00 USD | 1,150.00 USD | 307,540.00 USD |
| `7D` | `0.1508` | 6,030,000.00 USD | 0.00 USD | 6,030,000.00 USD | 151,240.00 USD | 4,870.00 USD | 248,410.00 USD |
| `1D` | `0.1510` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 0.00 USD | 6,130.00 USD | 50,780.00 USD |
| `7D` | `0.1511` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 86,820.00 USD | 11,590.00 USD | 38,070.00 USD |
| `1D` | `0.1513` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 11,750.00 USD | 3,900.00 USD | 250,320.00 USD |
| `7D` | `0.1514` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 0.00 USD | 15,050.00 USD | 367,590.00 USD |
| `1D` | `0.1516` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 12,230.00 USD | 0.00 USD | 141,160.00 USD |
| `7D` | `0.1517` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 96,310.00 USD | 4,290.00 USD | 119,870.00 USD |
| `1D` | `0.1519` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 47,400.00 USD | 13,370.00 USD | 35,270.00 USD |
| `7D` | `0.1520` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 0.00 USD | 22,600.00 USD | 156,830.00 USD |
| `1D` | `0.1522` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 33,890.00 USD | 4,770.00 USD | 13,640.00 USD |
| `7D` | `0.1523` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 0.00 USD | 15,080.00 USD | 0.00 USD |
| `1D` | `0.1525` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 48,970.00 USD | 0.00 USD | 3,130.00 USD |
| `7D` | `0.1526` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 0.00 USD | 38,870.00 USD | 0.00 USD |
| `1D` | `0.1528` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 29,740.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1529` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD |
| `1D` | `0.1531` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 12,670.00 USD | 18,920.00 USD | 4,670.00 USD |
| `7D` | `0.1532` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 0.00 USD | 14,780.00 USD | 0.00 USD |
| `1D` | `0.1534` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 10,930.00 USD | 1,760.00 USD | 11,690.00 USD |
| `7D` | `0.1535` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 35,470.00 USD | 8,570.00 USD | 0.00 USD |
| `1D` | `0.1537` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 4,040.00 USD | 18,160.00 USD | 10,570.00 USD |
| `7D` | `0.1538` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 0.00 USD | 14,700.00 USD | 0.00 USD |
| `1D` | `0.1540` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 27,770.00 USD | 4,030.00 USD | 7,440.00 USD |
| `7D` | `0.1541` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD |
| `1D` | `0.1543` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 4,600.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1544` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD |
| `1D` | `0.1546` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 24,160.00 USD | 7,790.00 USD | 5,850.00 USD |
| `7D` | `0.1547` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 0.00 USD | 12,560.00 USD | 89,090.00 USD |
| `1D` | `0.1549` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 16,200.00 USD | 17,930.00 USD | 29,710.00 USD |
| `7D` | `0.1550` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 0.00 USD | 16,530.00 USD | 0.00 USD |
| `1D` | `0.1552` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 8,630.00 USD | 10,490.00 USD | 5,050.00 USD |
| `7D` | `0.1553` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 0.00 USD | 7,730.00 USD | 0.00 USD |
| `1D` | `0.1555` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 34,930.00 USD | 5,680.00 USD | 13,580.00 USD |
| `7D` | `0.1556` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD |
| `1D` | `0.1558` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 6,990.00 USD | 11,690.00 USD | 4,410.00 USD |
| `7D` | `0.1559` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD |
| `1D` | `0.1561` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 12,360.00 USD | 2,970.00 USD | 0.00 USD |
| `7D` | `0.1562` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD |
| `1D` | `0.1564` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 14,590.00 USD | 38,290.00 USD | 9,940.00 USD |
| `7D` | `0.1565` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 70,940.00 USD | 28,480.00 USD | 0.00 USD |
| `1D` | `0.1567` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 87,320.00 USD | 1,850.00 USD | 25,660.00 USD |
| `7D` | `0.1568` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 111,700.00 USD | 10,060.00 USD | 151,620.00 USD |
| `1D` | `0.1570` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 27,380.00 USD | 0.00 USD | 105,410.00 USD |
| `7D` | `0.1571` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 194,660.00 USD | 13,600.00 USD | 58,840.00 USD |
| `1D` | `0.1573` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 49,900.00 USD | 5,380.00 USD | 64,460.00 USD |
| `7D` | `0.1574` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 64,070.00 USD | 79,780.00 USD | 0.00 USD |
| `7D` | `0.1577` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 31,130.00 USD | 112,180.00 USD | 0.00 USD |
| `7D` | `0.1580` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 216,490.00 USD | 41,220.00 USD | 0.00 USD |
| `1D` | `0.1582` | 899,150.00 USD | 0.00 USD | 899,150.00 USD | 49,700.00 USD | 0.00 USD | 6,020.00 USD |
| `7D` | `0.1583` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 70,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1585` | 843,430.00 USD | 0.00 USD | 843,430.00 USD | 52,520.00 USD | 22,800.00 USD | 6,620.00 USD |
| `7D` | `0.1586` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 44,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1588` | 761,480.00 USD | 0.00 USD | 761,480.00 USD | 20,600.00 USD | 31,780.00 USD | 53,020.00 USD |
| `7D` | `0.1589` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 34,830.00 USD | 0.00 USD | 89,310.00 USD |
| `1D` | `0.1591` | 656,090.00 USD | 0.00 USD | 656,090.00 USD | 0.00 USD | 19,870.00 USD | 33,060.00 USD |
| `1D` | `0.1594` | 603,150.00 USD | 0.00 USD | 603,150.00 USD | 0.00 USD | 23,960.00 USD | 4,670.00 USD |
| `7D` | `0.1595` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 0.00 USD | 37,130.00 USD | 0.00 USD |
| `1D` | `0.1597` | 574,520.00 USD | 0.00 USD | 574,520.00 USD | 0.00 USD | 0.00 USD | 6,030.00 USD |
| `7D` | `0.1598` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 0.00 USD | 86,680.00 USD | 75,810.00 USD |
| `1D` | `0.1600` | 568,490.00 USD | 0.00 USD | 568,490.00 USD | 0.00 USD | 9,890.00 USD | 0.00 USD |
| `7D` | `0.1601` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 0.00 USD | 47,500.00 USD | 0.00 USD |
| `1D` | `0.1603` | 558,600.00 USD | 0.00 USD | 558,600.00 USD | 44,810.00 USD | 3,850.00 USD | 0.00 USD |
| `7D` | `0.1604` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 72,300.00 USD | 21,810.00 USD | 273,670.00 USD |
| `7D` | `0.1607` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 166,880.00 USD | 0.00 USD | 312,980.00 USD |
| `1D` | `0.1609` | 509,950.00 USD | 0.00 USD | 509,950.00 USD | 48,780.00 USD | 7,790.00 USD | 82,750.00 USD |
| `7D` | `0.1610` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 178,210.00 USD | 0.00 USD | 178,270.00 USD |
| `1D` | `0.1612` | 370,630.00 USD | 0.00 USD | 370,630.00 USD | 0.00 USD | 23,830.00 USD | 0.00 USD |
| `7D` | `0.1613` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 321,740.00 USD | 0.00 USD | 381,020.00 USD |
| `1D` | `0.1615` | 346,800.00 USD | 0.00 USD | 346,800.00 USD | 0.00 USD | 18,110.00 USD | 0.00 USD |
| `7D` | `0.1616` | 641,420.00 USD | 0.00 USD | 641,420.00 USD | 187,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1622` | 453,830.00 USD | 0.00 USD | 453,830.00 USD | 0.00 USD | 80,360.00 USD | 0.00 USD |
| `1D` | `0.1624` | 328,690.00 USD | 0.00 USD | 328,690.00 USD | 60,520.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1625` | 373,470.00 USD | 0.00 USD | 373,470.00 USD | 0.00 USD | 122,430.00 USD | 103,330.00 USD |
| `1D` | `0.1627` | 268,170.00 USD | 0.00 USD | 268,170.00 USD | 38,240.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `0.1628` | 147,720.00 USD | 0.00 USD | 147,720.00 USD | 76,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1630` | 227,440.00 USD | 0.00 USD | 227,440.00 USD | 23,880.00 USD | 3,520.00 USD | 101,620.00 USD |
| `7D` | `0.1631` | 70,940.00 USD | 0.00 USD | 70,940.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1633` | 98,410.00 USD | 0.00 USD | 98,410.00 USD | 98,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1635` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1635` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1636` | 34,250.00 USD | 34,250.00 USD | 0.00 USD | 0.00 USD | 10,690.00 USD | 23,560.00 USD |
| `7D` | `0.1637` | 23,560.00 USD | 23,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23,560.00 USD |
| `1D` | `0.1639` | 51,420.00 USD | 51,420.00 USD | 0.00 USD | 14,240.00 USD | 0.00 USD | 2,920.00 USD |
| `7D` | `0.1640` | 52,800.00 USD | 52,800.00 USD | 0.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD |
| `1D` | `0.1642` | 138,140.00 USD | 138,140.00 USD | 0.00 USD | 31,400.00 USD | 36,980.00 USD | 18,340.00 USD |
| `7D` | `0.1643` | 122,450.00 USD | 122,450.00 USD | 0.00 USD | 0.00 USD | 25,110.00 USD | 44,540.00 USD |
| `1D` | `0.1645` | 191,760.00 USD | 191,760.00 USD | 0.00 USD | 17,870.00 USD | 24,710.00 USD | 11,040.00 USD |
| `7D` | `0.1646` | 136,230.00 USD | 136,230.00 USD | 0.00 USD | 0.00 USD | 13,780.00 USD | 0.00 USD |
| `1D` | `0.1648` | 220,930.00 USD | 220,930.00 USD | 0.00 USD | 17,270.00 USD | 3,360.00 USD | 8,550.00 USD |
| `7D` | `0.1649` | 148,000.00 USD | 148,000.00 USD | 0.00 USD | 0.00 USD | 11,770.00 USD | 0.00 USD |
| `1D` | `0.1651` | 272,270.00 USD | 272,270.00 USD | 0.00 USD | 32,910.00 USD | 8,040.00 USD | 10,390.00 USD |
| `1D` | `0.1654` | 304,940.00 USD | 304,940.00 USD | 0.00 USD | 3,500.00 USD | 4,350.00 USD | 24,820.00 USD |
| `7D` | `0.1655` | 184,620.00 USD | 184,620.00 USD | 0.00 USD | 0.00 USD | 36,620.00 USD | 0.00 USD |
| `1D` | `0.1657` | 392,980.00 USD | 392,980.00 USD | 0.00 USD | 15,910.00 USD | 63,310.00 USD | 8,820.00 USD |
| `7D` | `0.1658` | 247,170.00 USD | 247,170.00 USD | 0.00 USD | 10,890.00 USD | 0.00 USD | 51,660.00 USD |
| `1D` | `0.1660` | 464,920.00 USD | 464,920.00 USD | 0.00 USD | 8,220.00 USD | 12,910.00 USD | 50,810.00 USD |
| `7D` | `0.1661` | 361,940.00 USD | 361,940.00 USD | 0.00 USD | 103,750.00 USD | 11,020.00 USD | 0.00 USD |
| `1D` | `0.1663` | 596,050.00 USD | 596,050.00 USD | 0.00 USD | 55,130.00 USD | 14,550.00 USD | 61,450.00 USD |
| `7D` | `0.1664` | 617,570.00 USD | 617,570.00 USD | 0.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD |
| `1D` | `0.1666` | 705,560.00 USD | 705,560.00 USD | 0.00 USD | 22,170.00 USD | 9,050.00 USD | 78,290.00 USD |
| `7D` | `0.1667` | 672,810.00 USD | 672,810.00 USD | 0.00 USD | 42,580.00 USD | 12,670.00 USD | 0.00 USD |
| `1D` | `0.1669` | 723,170.00 USD | 723,170.00 USD | 0.00 USD | 4,600.00 USD | 5,570.00 USD | 7,440.00 USD |
| `7D` | `0.1670` | 982,750.00 USD | 982,750.00 USD | 0.00 USD | 114,710.00 USD | 108,060.00 USD | 87,160.00 USD |
| `1D` | `0.1672` | 773,720.00 USD | 773,720.00 USD | 0.00 USD | 46,590.00 USD | 3,960.00 USD | 0.00 USD |
| `7D` | `0.1673` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 20,540.00 USD | 23,800.00 USD | 0.00 USD |
| `1D` | `0.1675` | 815,420.00 USD | 815,420.00 USD | 0.00 USD | 20,040.00 USD | 1,990.00 USD | 19,670.00 USD |
| `7D` | `0.1676` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 84,020.00 USD | 141,760.00 USD | 0.00 USD |
| `1D` | `0.1678` | 848,420.00 USD | 848,420.00 USD | 0.00 USD | 27,610.00 USD | 0.00 USD | 5,390.00 USD |
| `7D` | `0.1679` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 52,340.00 USD | 61,850.00 USD | 35,720.00 USD |
| `1D` | `0.1681` | 954,980.00 USD | 954,980.00 USD | 0.00 USD | 94,970.00 USD | 8,580.00 USD | 3,010.00 USD |
| `7D` | `0.1682` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 130,480.00 USD | 18,420.00 USD | 15,310.00 USD |
| `1D` | `0.1684` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 50,170.00 USD | 30,620.00 USD | 37,380.00 USD |
| `7D` | `0.1685` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 14,000.00 USD | 0.00 USD |
| `1D` | `0.1687` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 13,000.00 USD | 9,810.00 USD | 52,820.00 USD |
| `7D` | `0.1688` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD |
| `1D` | `0.1690` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 25,050.00 USD | 12,840.00 USD | 18,700.00 USD |
| `7D` | `0.1691` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 33,660.00 USD | 38,670.00 USD | 71,020.00 USD |
| `1D` | `0.1693` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 87,330.00 USD | 74,940.00 USD | 60,850.00 USD |
| `7D` | `0.1694` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 17,360.00 USD | 62,560.00 USD | 39,780.00 USD |
| `1D` | `0.1696` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 23,530.00 USD | 19,390.00 USD | 19,580.00 USD |
| `7D` | `0.1697` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 56,860.00 USD | 0.00 USD |
| `1D` | `0.1699` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 26,000.00 USD | 57,580.00 USD | 48,960.00 USD |
| `7D` | `0.1700` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD |
| `1D` | `0.1702` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 9,960.00 USD | 1,920.00 USD | 34,530.00 USD |
| `7D` | `0.1703` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 55,170.00 USD | 55,390.00 USD | 0.00 USD |
| `1D` | `0.1705` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 20,880.00 USD | 20,810.00 USD | 0.00 USD |
| `7D` | `0.1706` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD |
| `1D` | `0.1708` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 46,300.00 USD | 66,430.00 USD | 15,460.00 USD |
| `7D` | `0.1709` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD |
| `1D` | `0.1711` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 5,500.00 USD | 4,910.00 USD | 8,040.00 USD |
| `1D` | `0.1714` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 3,630.00 USD | 12,410.00 USD | 0.00 USD |
| `7D` | `0.1715` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD |
| `1D` | `0.1717` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 11,710.00 USD | 37,270.00 USD | 19,560.00 USD |
| `7D` | `0.1718` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,160.00 USD |
| `1D` | `0.1720` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 47,600.00 USD | 1,590.00 USD | 5,030.00 USD |
| `7D` | `0.1721` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 44,020.00 USD | 0.00 USD | 266,220.00 USD |
| `1D` | `0.1723` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 54,130.00 USD | 17,650.00 USD | 66,630.00 USD |
| `7D` | `0.1724` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 74,040.00 USD | 0.00 USD | 104,030.00 USD |
| `1D` | `0.1726` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 8,230.00 USD | 3,180.00 USD | 12,130.00 USD |
| `1D` | `0.1729` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD |
| `7D` | `0.1730` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 330,670.00 USD | 0.00 USD | 9,420.00 USD |
| `1D` | `0.1732` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD |
| `7D` | `0.1733` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 145,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1735` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 18,250.00 USD | 11,060.00 USD | 1,170.00 USD |
| `1D` | `0.1738` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 15,900.00 USD | 3,450.00 USD | 6,410.00 USD |
| `7D` | `0.1739` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD |
| `1D` | `0.1741` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 4,490.00 USD | 8,360.00 USD |
| `1D` | `0.1744` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 2,460.00 USD | 13,980.00 USD |
| `7D` | `0.1745` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1747` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 3,500.00 USD | 0.00 USD | 31,930.00 USD |
| `7D` | `0.1748` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `0.1750` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 80,070.00 USD | 2,280.00 USD | 22,640.00 USD |
| `7D` | `0.1751` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 226,130.00 USD |
| `1D` | `0.1753` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 34,710.00 USD | 0.00 USD | 26,970.00 USD |
| `7D` | `0.1754` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 37,610.00 USD | 0.00 USD | 229,230.00 USD |
| `1D` | `0.1756` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 23,610.00 USD | 11,970.00 USD | 60,750.00 USD |
| `7D` | `0.1757` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 124,250.00 USD | 38,670.00 USD | 8,600.00 USD |
| `1D` | `0.1759` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 58,360.00 USD | 21,690.00 USD | 21,380.00 USD |
| `7D` | `0.1760` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 224,680.00 USD | 25,210.00 USD | 32,350.00 USD |
| `1D` | `0.1762` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 50,470.00 USD | 68,300.00 USD | 66,600.00 USD |
| `7D` | `0.1763` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 240,020.00 USD | 139,590.00 USD | 12,330.00 USD |
| `1D` | `0.1765` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 15,830.00 USD | 28,990.00 USD | 43,670.00 USD |
| `7D` | `0.1766` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 163,180.00 USD | 200,720.00 USD | 36,540.00 USD |
| `1D` | `0.1768` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 19,860.00 USD | 70,050.00 USD | 52,710.00 USD |
| `7D` | `0.1769` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 113,280.00 USD | 105,160.00 USD | 23,040.00 USD |
| `1D` | `0.1771` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 37,200.00 USD | 12,060.00 USD | 16,920.00 USD |
| `7D` | `0.1772` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 77,840.00 USD | 112,520.00 USD | 21,360.00 USD |
| `1D` | `0.1774` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 12,400.00 USD | 23,730.00 USD | 24,140.00 USD |
| `7D` | `0.1775` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 164,290.00 USD | 30,480.00 USD | 0.00 USD |
| `1D` | `0.1777` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 41,420.00 USD | 74,750.00 USD | 20,580.00 USD |
| `7D` | `0.1778` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 63,990.00 USD | 71,060.00 USD | 123,700.00 USD |
| `1D` | `0.1780` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 7,310.00 USD | 10,310.00 USD | 9,410.00 USD |
| `7D` | `0.1781` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 11,220.00 USD | 4,590.00 USD | 33,810.00 USD |
| `1D` | `0.1783` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 27,640.00 USD | 15,680.00 USD | 18,910.00 USD |
| `7D` | `0.1784` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD |
| `1D` | `0.1786` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 16,960.00 USD | 28,560.00 USD | 7,120.00 USD |
| `7D` | `0.1787` | 6,580,000.00 USD | 6,580,000.00 USD | 0.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD |
| `1D` | `0.1789` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 9,350.00 USD | 20,220.00 USD | 5,220.00 USD |
| `7D` | `0.1790` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 103,860.00 USD | 17,360.00 USD | 3,940.00 USD |
| `1D` | `0.1792` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 3,490.00 USD | 7,300.00 USD |
| `7D` | `0.1793` | 6,830,000.00 USD | 6,830,000.00 USD | 0.00 USD | 78,950.00 USD | 42,780.00 USD | 8,910.00 USD |
| `1D` | `0.1795` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 33,150.00 USD | 35,780.00 USD | 18,910.00 USD |
| `7D` | `0.1796` | 6,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 17,130.00 USD | 12,930.00 USD | 35,530.00 USD |
| `1D` | `0.1798` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 11,000.00 USD | 17,120.00 USD | 21,440.00 USD |
| `7D` | `0.1799` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 0.00 USD | 11,280.00 USD | 68,230.00 USD |
| `1D` | `0.1801` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 9,540.00 USD | 19,700.00 USD | 11,240.00 USD |
| `7D` | `0.1802` | 7,080,000.00 USD | 7,080,000.00 USD | 0.00 USD | 48,220.00 USD | 36,030.00 USD | 23,530.00 USD |
| `1D` | `0.1804` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 10,530.00 USD | 14,470.00 USD | 14,770.00 USD |
| `7D` | `0.1805` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 11,410.00 USD | 38,130.00 USD | 5,320.00 USD |
| `1D` | `0.1807` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 10,730.00 USD | 9,130.00 USD | 7,090.00 USD |
| `7D` | `0.1808` | 7,290,000.00 USD | 7,290,000.00 USD | 0.00 USD | 23,650.00 USD | 52,750.00 USD | 73,440.00 USD |
| `1D` | `0.1810` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 8,220.00 USD | 11,640.00 USD | 2,770.00 USD |
| `1D` | `0.1811` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 3,940.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1811` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 64,990.00 USD | 26,860.00 USD | 13,200.00 USD |
| `7D` | `0.1814` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 28,070.00 USD | 26,510.00 USD | 60,000.00 USD |
| `7D` | `0.1817` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 64,770.00 USD | 10,470.00 USD | 20,080.00 USD |
| `7D` | `0.1820` | 7,740,000.00 USD | 7,740,000.00 USD | 0.00 USD | 42,210.00 USD | 54,880.00 USD | 38,610.00 USD |
| `7D` | `0.1823` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 62,540.00 USD | 13,300.00 USD | 105,730.00 USD |
| `7D` | `0.1826` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 90,200.00 USD | 9,890.00 USD | 66,950.00 USD |
| `7D` | `0.1829` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 20,880.00 USD | 28,120.00 USD | 51,250.00 USD |
| `7D` | `0.1832` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 94,870.00 USD | 27,790.00 USD | 50,530.00 USD |
| `7D` | `0.1835` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 111,430.00 USD | 46,260.00 USD | 52,650.00 USD |
| `7D` | `0.1838` | 8,900,000.00 USD | 8,900,000.00 USD | 0.00 USD | 144,340.00 USD | 74,280.00 USD | 106,440.00 USD |
| `7D` | `0.1841` | 9,060,000.00 USD | 9,060,000.00 USD | 0.00 USD | 56,160.00 USD | 57,660.00 USD | 45,300.00 USD |
| `7D` | `0.1844` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 48,920.00 USD | 3,900.00 USD | 72,920.00 USD |
| `7D` | `0.1847` | 9,220,000.00 USD | 9,220,000.00 USD | 0.00 USD | 5,770.00 USD | 11,590.00 USD | 20,400.00 USD |
| `7D` | `0.1850` | 9,480,000.00 USD | 9,480,000.00 USD | 0.00 USD | 77,110.00 USD | 77,020.00 USD | 103,160.00 USD |
| `7D` | `0.1853` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 62,090.00 USD | 9,590.00 USD | 146,560.00 USD |
| `7D` | `0.1856` | 9,840,000.00 USD | 9,840,000.00 USD | 0.00 USD | 31,410.00 USD | 21,030.00 USD | 87,320.00 USD |
| `7D` | `0.1859` | 9,970,000.00 USD | 9,970,000.00 USD | 0.00 USD | 47,740.00 USD | 6,920.00 USD | 77,460.00 USD |
| `7D` | `0.1862` | 10,080,000.00 USD | 10,080,000.00 USD | 0.00 USD | 60,020.00 USD | 13,950.00 USD | 37,650.00 USD |
| `7D` | `0.1865` | 10,160,000.00 USD | 10,160,000.00 USD | 0.00 USD | 22,320.00 USD | 18,650.00 USD | 40,190.00 USD |
| `7D` | `0.1868` | 10,310,000.00 USD | 10,310,000.00 USD | 0.00 USD | 88,110.00 USD | 31,750.00 USD | 24,730.00 USD |
| `7D` | `0.1871` | 10,450,000.00 USD | 10,450,000.00 USD | 0.00 USD | 83,830.00 USD | 27,560.00 USD | 34,980.00 USD |
| `7D` | `0.1874` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 71,850.00 USD | 48,780.00 USD | 51,010.00 USD |
| `7D` | `0.1877` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 27,840.00 USD | 22,370.00 USD | 17,920.00 USD |
| `7D` | `0.1880` | 10,750,000.00 USD | 10,750,000.00 USD | 0.00 USD | 36,800.00 USD | 14,700.00 USD | 8,130.00 USD |
| `7D` | `0.1883` | 10,780,000.00 USD | 10,780,000.00 USD | 0.00 USD | 14,000.00 USD | 3,530.00 USD | 9,740.00 USD |
| `7D` | `0.1886` | 10,820,000.00 USD | 10,820,000.00 USD | 0.00 USD | 9,250.00 USD | 31,900.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `188.85M` | Total OI Tokens: `1,154,829,530.5 ARB`
  * 1h OI Change: `+3.49%` | 4h OI Change: `+5.11%` | 24h OI Change: `-14.04%`
  * Exchange Breakdown: Binance=`42.60M` | Bybit=`26.50M` | OKX=`14.52M` | Hyperliquid=`13.19M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.37K` | Last 24h: `-1.51K` | Last 3d: `12.63K` | Last 7d: `45.15K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0030%` | **USDT OKX** | `-0.0013%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0012%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `-0.0106%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `47.80%` | `52.20%` | `0.92` | 2,110,000.00 USD |
| `15M` | `Binance` | `40.35%` | `59.65%` | `0.68` | 631,880.00 USD |
| `15M` | `OKX` | `38.44%` | `61.56%` | `0.62` | 188,890.00 USD |
| `15M` | `Bybit` | `35.92%` | `64.08%` | `0.56` | 116,340.00 USD |
| `15M` | `KuCoin` | `51.7%` | `48.3%` | `1.07` | 137,190.00 USD |
| `15M` | `Gate` | `34.74%` | `65.26%` | `0.53` | 20,060.00 USD |
| `15M` | `Bitget` | `53.21%` | `46.79%` | `1.14` | 511,870.00 USD |
| `15M` | `BingX` | `58.71%` | `41.29%` | `1.42` | 294,120.00 USD |
| `15M` | `MEXC` | `77.96%` | `22.04%` | `3.54` | 62,240.00 USD |
| `15M` | `Bitunix` | `48.07%` | `51.93%` | `0.93` | 27,770.00 USD |
| `15M` | `Hyperliquid` | `91.18%` | `8.82%` | `10.34` | 16,380.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.78%` | `50.22%` | `0.99` | 56,890.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `42.27%` | `57.73%` | `0.73` | 12,930.00 USD |
| `15M` | `HTX` | `57.55%` | `42.45%` | `1.36` | 350.64 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `7.82%` | `92.18%` | `0.08` | 26,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `100%` | `0%` | `1.00` | 20.10 USD |
| `15M` | `Whale Positions` | `40.35%` | `59.65%` | `0.68` | 631,880.00 USD |
| `15M` | `Global Accounts` | `47.80%` | `52.20%` | `0.92` | 2,110,000.00 USD |
| `1H` | `ARB` | `48.01%` | `51.99%` | `0.92` | 5,480,000.00 USD |
| `1H` | `Binance` | `47.3%` | `52.7%` | `0.90` | 1,670,000.00 USD |
| `1H` | `OKX` | `47.21%` | `52.79%` | `0.89` | 476,490.00 USD |
| `1H` | `Bybit` | `41.62%` | `58.38%` | `0.71` | 531,420.00 USD |
| `1H` | `KuCoin` | `50.65%` | `49.35%` | `1.03` | 502,710.00 USD |
| `1H` | `Gate` | `41.32%` | `58.68%` | `0.70` | 73,210.00 USD |
| `1H` | `Bitget` | `49.09%` | `50.91%` | `0.96` | 930,240.00 USD |
| `1H` | `BingX` | `49.32%` | `50.68%` | `0.97` | 644,080.00 USD |
| `1H` | `MEXC` | `60.82%` | `39.18%` | `1.55` | 247,680.00 USD |
| `1H` | `Bitunix` | `41.56%` | `58.44%` | `0.71` | 75,440.00 USD |
| `1H` | `Hyperliquid` | `83.36%` | `16.64%` | `5.01` | 63,220.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.55%` | `49.45%` | `1.02` | 170,380.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `27.19%` | `72.81%` | `0.37` | 54,500.00 USD |
| `1H` | `HTX` | `82.85%` | `17.15%` | `4.83` | 1,020.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `6.57%` | `93.43%` | `0.07` | 42,050.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `5.52%` | `94.48%` | `0.06` | 5,870.00 USD |
| `1H` | `Whale Positions` | `47.3%` | `52.7%` | `0.90` | 1,670,000.00 USD |
| `1H` | `Global Accounts` | `48.01%` | `51.99%` | `0.92` | 5,480,000.00 USD |
| `4H` | `ARB` | `47.54%` | `52.46%` | `0.91` | 22,250,000.00 USD |
| `4H` | `Binance` | `52.84%` | `47.16%` | `1.12` | 8,120,000.00 USD |
| `4H` | `OKX` | `51.48%` | `48.52%` | `1.06` | 2,310,000.00 USD |
| `4H` | `Bybit` | `54.12%` | `45.88%` | `1.18` | 2,380,000.00 USD |
| `4H` | `KuCoin` | `50.57%` | `49.43%` | `1.02` | 1,700,000.00 USD |
| `4H` | `Gate` | `50.65%` | `49.35%` | `1.03` | 670,780.00 USD |
| `4H` | `Bitget` | `50.64%` | `49.36%` | `1.03` | 1,460,000.00 USD |
| `4H` | `BingX` | `21.49%` | `78.51%` | `0.27` | 2,920,000.00 USD |
| `4H` | `MEXC` | `53.11%` | `46.89%` | `1.13` | 825,070.00 USD |
| `4H` | `Bitunix` | `43.09%` | `56.91%` | `0.76` | 400,000.00 USD |
| `4H` | `Hyperliquid` | `55.87%` | `44.13%` | `1.27` | 293,050.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.12%` | `49.88%` | `1.00` | 762,480.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `19.74%` | `80.26%` | `0.25` | 286,370.00 USD |
| `4H` | `HTX` | `26.5%` | `73.5%` | `0.36` | 12,650.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `40.34%` | `59.66%` | `0.68` | 46,010.00 USD |
| `4H` | `Aster` | `20.7%` | `79.3%` | `0.26` | 60,600.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `24.29%` | `75.71%` | `0.32` | 18,060.00 USD |
| `4H` | `Whale Positions` | `52.84%` | `47.16%` | `1.12` | 8,120,000.00 USD |
| `4H` | `Global Accounts` | `47.54%` | `52.46%` | `0.91` | 22,250,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1560` | `0.1557` | `0.1560` | `0.1561` | `0.1552` | 724,500.45 USD | 382,680.28 USD | 341,820.18 USD | 40,860.10 USD | `+5.64%` | `10B / 13S` |
| `0:00 UTC` | `0.1560` | `0.1561` | `0.1560` | `0.1567` | `0.1555` | 659,096.24 USD | 362,345.04 USD | 296,751.20 USD | 65,593.84 USD | `+9.95%` | `17B / 13S` |
| `5:00 UTC` | `0.1568` | `0.1562` | `0.1568` | `0.1570` | `0.1554` | 510,482.89 USD | 331,670.18 USD | 178,812.71 USD | 152,857.47 USD | `+29.94%` | `56B / 25S` |
| `0:00 UTC` | `0.1575` | `0.1578` | `0.1575` | `0.1585` | `0.1566` | 1,225,850.60 USD | 572,636.93 USD | 653,213.67 USD | -80,576.74 USD | `-6.57%` | `41B / 29S` |
| `5:00 UTC` | `0.1581` | `0.1581` | `0.1581` | `0.1585` | `0.1579` | 820,818.50 USD | 467,570.37 USD | 353,248.12 USD | 114,322.25 USD | `+13.93%` | `9B / 5S` |
| `0:00 UTC` | `0.1580` | `0.1582` | `0.1580` | `0.1590` | `0.1577` | 855,410.94 USD | 513,960.14 USD | 341,450.80 USD | 172,509.34 USD | `+20.17%` | `35B / 24S` |
| `5:00 UTC` | `0.1601` | `0.1598` | `0.1601` | `0.1608` | `0.1587` | 1,430,991.81 USD | 878,187.62 USD | 552,804.19 USD | 325,383.42 USD | `+22.74%` | `24B / 14S` |
| `0:00 UTC` | `0.1620` | `0.1617` | `0.1620` | `0.1625` | `0.1603` | 1,684,179.28 USD | 761,022.88 USD | 923,156.41 USD | -162,133.53 USD | `-9.63%` | `12B / 13S` |
| `5:00 UTC` | `0.1637` | `0.1631` | `0.1637` | `0.1639` | `0.1618` | 1,849,966.09 USD | 605,282.83 USD | 1,244,683.26 USD | -639,400.43 USD | `-34.56%` | `9B / 30S` |
| `0:00 UTC` | `0.1641` | `0.1639` | `0.1641` | `0.1642` | `0.1635` | 128,007.30 USD | 62,618.09 USD | 65,389.21 USD | -2,771.12 USD | `-2.16%` | `15B / 12S` |

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
| `5m` | 60,090.00 USD | -378,670.00 USD | **`DISTRIBUTION`** |
| `15m` | 40,430.00 USD | -774,810.00 USD | **`DISTRIBUTION`** |
| `30m` | 79,750.00 USD | -549,560.00 USD | **`DISTRIBUTION`** |
| `1h` | 9,600.00 USD | -20,950.00 USD | **`DISTRIBUTION`** |
| `2h` | 25,710.00 USD | 612,210.00 USD | **`ACCUMULATION`** |
| `4h` | 129,060.00 USD | 1,670,000.00 USD | **`ACCUMULATION`** |
| `6h` | -315,490.00 USD | 828,920.00 USD | **`ACCUMULATION`** |
| `8h` | -10,840.00 USD | -4,180,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,060,000.00 USD | -4,960,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,000,000.00 USD | -8,850,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,460,000.00 USD | -35,860,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,570,000.00 USD | -162,130,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+60.09K` | 15m=`+40.43K` | 1h=`+9.60K` | 24h=`-2.00M`
* Futures Capital Netflows: 5m=`-378.67K` | 15m=`-774.81K` | 1h=`-20.95K` | 24h=`-8.85M`
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
  * `2026-10-30 09:51:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:29:10 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
