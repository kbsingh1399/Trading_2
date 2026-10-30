# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 10:19:40 IST` (`2026-10-30 04:49:40 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1605` | `0.1620` | `0.1603` | `0.1618` | `4,372,628` | 705,283.52 USD | 6,006.60 USD | `+0.85%` | -7,669,077.45 USD | `-0.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.1618` | `0.1625` | `0.1614` | `0.1622` | `3,761,069` | 609,231.08 USD | -5,312.44 USD | `-0.87%` | -7,674,389.89 USD | `-0.47` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.1622` | `0.1623` | `0.1617` | `0.1623` | `1,703,879` | 275,991.11 USD | -130,654.12 USD | `-47.34%` | -7,805,044.01 USD | `-1.62` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1580` | `0.1590` | `0.1577` | `0.1590` | `5,407,236` | 855,410.94 USD | 172,509.34 USD | `+20.17%` | -8,000,467.47 USD | `+0.50` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1590` | `0.1608` | `0.1587` | `0.1605` | `8,956,803` | 1,430,991.81 USD | 325,383.42 USD | `+22.74%` | -7,675,084.05 USD | `+0.87` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1605` | `0.1625` | `0.1603` | `0.1623` | `9,839,769` | 1,590,861.63 USD | -130,315.89 USD | `-8.19%` | -7,805,399.94 USD | `-0.35` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1533` | `0.1563` | `0.1526` | `0.1560` | `24,694,709` | 3,828,145.62 USD | 314,402.05 USD | `+8.21%` | -8,433,124.58 USD | `+0.72` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1560` | `0.1585` | `0.1553` | `0.1580` | `20,448,591` | 3,216,248.24 USD | 252,196.82 USD | `+7.84%` | -8,180,927.76 USD | `+0.61` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1580` | `0.1625` | `0.1577` | `0.1623` | `24,225,236` | 3,880,742.68 USD | 368,994.54 USD | `+9.51%` | -7,811,933.23 USD | `+0.70` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -6,590,804.13 USD | `-1.67` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -7,211,742.64 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1625` | `0.1577` | `0.1623` | `24,225,236` | 3,880,742.68 USD | 368,994.54 USD | `+9.51%` | -6,842,748.10 USD | `+1.18` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -1,669,122.15 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -2,866,580.15 USD | `-0.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -6,590,804.13 USD | `-1.67` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -7,211,742.64 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1625` | `0.1577` | `0.1623` | `24,225,236` | 3,880,742.68 USD | 368,994.54 USD | `+9.51%` | -6,842,748.10 USD | `+1.18` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:14:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1709` | 7,729.41 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale BUY: 7.73K USD at 0.1709 USD [API] | `2026-10-29 01:05:08` |
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
| `Live` | `Long Liquidation` | `0.1305` | 16,660.00 USD | 962,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 9,010.00 USD | 945,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 4,810.00 USD | 936,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 72,590.00 USD | 932,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1336` | 3,280,000.00 USD | 3,280,000.00 USD | 3,580.00 USD | 5,990.00 USD | 16,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1340` | 3,250,000.00 USD | 3,250,000.00 USD | 9,160.00 USD | 7,730.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1344` | 3,200,000.00 USD | 3,200,000.00 USD | 6,410.00 USD | 5,790.00 USD | 19,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1345` | 29,490.00 USD | 859,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1348` | 3,170,000.00 USD | 3,170,000.00 USD | 31,170.00 USD | 7,150.00 USD | 23,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1352` | 3,110,000.00 USD | 3,110,000.00 USD | 11,390.00 USD | 6,290.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1355` | 3,540.00 USD | 829,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1356` | 3,070,000.00 USD | 3,070,000.00 USD | 16,150.00 USD | 12,180.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1360` | 3,030,000.00 USD | 3,030,000.00 USD | 25,240.00 USD | 8,630.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1364` | 2,990,000.00 USD | 2,990,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 10,630.00 USD | 826,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1368` | 2,970,000.00 USD | 2,970,000.00 USD | 4,500.00 USD | 7,610.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1370` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 1,740.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1372` | 2,950,000.00 USD | 2,950,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1373` | 2,710,000.00 USD | 2,710,000.00 USD | 5,470.00 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1375` | 13,710.00 USD | 815,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1376` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 1,730.00 USD | 536.58 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1379` | 2,700,000.00 USD | 2,700,000.00 USD | 2,250.00 USD | 821.64 USD | 1,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1380` | 2,950,000.00 USD | 2,950,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1382` | 2,690,000.00 USD | 2,690,000.00 USD | 10,310.00 USD | 9,440.00 USD | 29,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1384` | 2,930,000.00 USD | 2,930,000.00 USD | 11,880.00 USD | 0.00 USD | 30,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1385` | 2,640,000.00 USD | 2,640,000.00 USD | 31,240.00 USD | 0.00 USD | 55,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 5,580.00 USD | 802,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1388` | 2,560,000.00 USD | 2,560,000.00 USD | 12,440.00 USD | 1,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1388` | 2,890,000.00 USD | 2,890,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1391` | 2,540,000.00 USD | 2,540,000.00 USD | 15,160.00 USD | 1,440.00 USD | 71,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1392` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1394` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 6,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 17,790.00 USD | 796,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1396` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 28,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1397` | 2,450,000.00 USD | 2,450,000.00 USD | 12,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1400` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 2,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1400` | 2,780,000.00 USD | 2,780,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1404` | 2,760,000.00 USD | 2,760,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 1,360.00 USD | 778,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1412` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1415` | 22,710.00 USD | 777,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1416` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1420` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1421` | 2,430,000.00 USD | 2,430,000.00 USD | 4,030.00 USD | 2,310.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 499,000.00 USD | 754,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1432` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1433` | 2,420,000.00 USD | 2,420,000.00 USD | 3,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 19,630.00 USD | 255,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1436` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 20,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1436` | 2,730,000.00 USD | 2,730,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1439` | 2,390,000.00 USD | 2,390,000.00 USD | 17,680.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1440` | 2,690,000.00 USD | 2,690,000.00 USD | 13,180.00 USD | 5,260.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1442` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1444` | 2,670,000.00 USD | 2,670,000.00 USD | 3,450.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 9,510.00 USD | 236,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1451` | 2,370,000.00 USD | 2,370,000.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1452` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 5,660.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 91,680.00 USD | 226,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1456` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1460` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1463` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1464` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 35,140.00 USD | 134,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1466` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1468` | 2,630,000.00 USD | 2,630,000.00 USD | 9,720.00 USD | 5,520.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1469` | 2,360,000.00 USD | 2,360,000.00 USD | 12,090.00 USD | 2,700.00 USD | 6,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1472` | 2,340,000.00 USD | 2,340,000.00 USD | 6,430.00 USD | 14,550.00 USD | 65,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1472` | 2,610,000.00 USD | 2,610,000.00 USD | 19,180.00 USD | 0.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1475` | 2,250,000.00 USD | 2,250,000.00 USD | 33,920.00 USD | 8,290.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 84,080.00 USD | 99,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1476` | 2,580,000.00 USD | 2,580,000.00 USD | 68,180.00 USD | 20,180.00 USD | 81,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1478` | 2,210,000.00 USD | 2,210,000.00 USD | 129,340.00 USD | 11,890.00 USD | 136,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1480` | 2,410,000.00 USD | 2,410,000.00 USD | 74,500.00 USD | 43,810.00 USD | 50,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1481` | 1,930,000.00 USD | 1,930,000.00 USD | 60,660.00 USD | 14,570.00 USD | 10,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1484` | 1,850,000.00 USD | 1,850,000.00 USD | 45,680.00 USD | 4,230.00 USD | 185,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1484` | 2,240,000.00 USD | 2,240,000.00 USD | 47,020.00 USD | 16,640.00 USD | 201,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,290.00 USD | 15,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1487` | 1,610,000.00 USD | 1,610,000.00 USD | 8,170.00 USD | 4,430.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1488` | 1,970,000.00 USD | 1,970,000.00 USD | 73,140.00 USD | 10,470.00 USD | 25,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1490` | 1,590,000.00 USD | 1,590,000.00 USD | 38,650.00 USD | 9,450.00 USD | 4,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1492` | 1,860,000.00 USD | 1,860,000.00 USD | 40,320.00 USD | 21,590.00 USD | 92,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1493` | 1,540,000.00 USD | 1,540,000.00 USD | 14,230.00 USD | 3,520.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 7,610.00 USD | 13,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long Liquidation` | `0.1545` | 5,720.00 USD | 5,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `0.1605` | 3,930.00 USD | 3,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1607` | 1,760,000.00 USD | 1,760,000.00 USD | 12,980.00 USD | 0.00 USD | 115,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1608` | 3,470,000.00 USD | 3,470,000.00 USD | 208,080.00 USD | 240,680.00 USD | 329,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1610` | 1,900,000.00 USD | 1,900,000.00 USD | 34,860.00 USD | 0.00 USD | 106,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1612` | 4,440,000.00 USD | 4,440,000.00 USD | 353,120.00 USD | 328,050.00 USD | 287,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1613` | 2,050,000.00 USD | 2,050,000.00 USD | 37,090.00 USD | 11,530.00 USD | 97,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1615` | 4,130.00 USD | 8,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1616` | 2,070,000.00 USD | 2,070,000.00 USD | 17,630.00 USD | 1,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1616` | 5,030,000.00 USD | 5,030,000.00 USD | 293,210.00 USD | 131,180.00 USD | 165,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1619` | 2,200,000.00 USD | 2,200,000.00 USD | 91,300.00 USD | 41,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1620` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 196,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1622` | 2,330,000.00 USD | 2,330,000.00 USD | 76,010.00 USD | 54,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1624` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 193,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1625` | 2,440,000.00 USD | 2,440,000.00 USD | 54,920.00 USD | 48,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1625` | 1,810.00 USD | 9,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1628` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 101,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1628` | 5,600,000.00 USD | 5,600,000.00 USD | 76,780.00 USD | 0.00 USD | 103,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1631` | 2,650,000.00 USD | 2,650,000.00 USD | 88,400.00 USD | 23,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1634` | 2,680,000.00 USD | 2,680,000.00 USD | 10,020.00 USD | 10,690.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1635` | 1,630.00 USD | 11,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1636` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 13,670.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1637` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 22,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1640` | 2,720,000.00 USD | 2,720,000.00 USD | 9,110.00 USD | 13,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1640` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1643` | 2,780,000.00 USD | 2,780,000.00 USD | 10,070.00 USD | 35,000.00 USD | 16,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1644` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 8,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1645` | 118.90 USD | 11,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1646` | 2,800,000.00 USD | 2,800,000.00 USD | 14,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1648` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1655` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 7,370.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1656` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 31,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1658` | 2,870,000.00 USD | 2,870,000.00 USD | 9,730.00 USD | 47,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1660` | 5,860,000.00 USD | 5,860,000.00 USD | 79,170.00 USD | 11,020.00 USD | 51,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1661` | 2,940,000.00 USD | 2,940,000.00 USD | 8,220.00 USD | 11,150.00 USD | 50,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1664` | 3,100,000.00 USD | 3,100,000.00 USD | 66,370.00 USD | 14,550.00 USD | 80,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1664` | 6,110,000.00 USD | 6,110,000.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1665` | 547.98 USD | 12,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `0.1715` | 2,370.00 USD | 14,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `1D` | `Short Liquidation` | `0.1736` | 4,590,000.00 USD | 4,590,000.00 USD | 14,970.00 USD | 9,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1739` | 4,620,000.00 USD | 4,620,000.00 USD | 18,610.00 USD | 2,310.00 USD | 12,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1740` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 83,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1742` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 1,600.00 USD | 11,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1744` | 8,810,000.00 USD | 8,810,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1745` | 4,660,000.00 USD | 4,660,000.00 USD | 8,530.00 USD | 2,460.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1745` | 4,260.00 USD | 18,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `0.1775` | 316.07 USD | 19,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1776` | 11,370,000.00 USD | 11,370,000.00 USD | 186,770.00 USD | 59,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1780` | 11,620,000.00 USD | 11,620,000.00 USD | 52,730.00 USD | 46,410.00 USD | 157,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1784` | 11,850,000.00 USD | 11,850,000.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1785` | 138.82 USD | 19,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `0.1915` | 1,600.00 USD | 20,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1916` | 17,140,000.00 USD | 17,140,000.00 USD | 7,460.00 USD | 5,300.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1920` | 17,150,000.00 USD | 17,150,000.00 USD | 0.00 USD | 5,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1924` | 17,170,000.00 USD | 17,170,000.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1925` | 543.50 USD | 21,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1928` | 17,190,000.00 USD | 17,190,000.00 USD | 11,600.00 USD | 7,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1944` | 17,190,000.00 USD | 17,190,000.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1945` | 623.68 USD | 22,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1952` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1956` | 17,210,000.00 USD | 17,210,000.00 USD | 4,860.00 USD | 2,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1960` | 17,220,000.00 USD | 17,220,000.00 USD | 5,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1964` | 17,240,000.00 USD | 17,240,000.00 USD | 6,470.00 USD | 2,700.00 USD | 10,990.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.0355` | 1,790,000.00 USD | 0.00 USD | 107.73 USD | `-77.51%` | `3,034,600,000,000.00` |
| `Live` | `Long` | `0.0385` | 1,790,000.00 USD | 0.00 USD | 5,590.00 USD | `-75.61%` | `145,291,300,000,000.00` |
| `Live` | `Long` | `0.0395` | 1,790,000.00 USD | 0.00 USD | 385.59 USD | `-74.97%` | `9,761,800,000,000.00` |
| `Live` | `Long` | `0.0415` | 1,790,000.00 USD | 0.00 USD | 110.22 USD | `-73.70%` | `2,655,800,000,000.00` |
| `Live` | `Long` | `0.0425` | 1,790,000.00 USD | 0.00 USD | 170.00 USD | `-73.07%` | `4,000,000,000,000.00` |
| `Live` | `Long` | `0.0475` | 1,790,000.00 USD | 0.00 USD | 167,030.00 USD | `-69.90%` | `3,516,409,800,000,000.00` |
| `Live` | `Long` | `0.0495` | 1,620,000.00 USD | 0.00 USD | 109.52 USD | `-68.64%` | `2,212,600,000,000.00` |
| `Live` | `Long` | `0.0525` | 1,620,000.00 USD | 0.00 USD | 289.43 USD | `-66.73%` | `5,513,000,000,000.00` |
| `Live` | `Long` | `0.0545` | 1,620,000.00 USD | 0.00 USD | 3,420.00 USD | `-65.47%` | `62,685,000,000,000.00` |
| `Live` | `Long` | `0.0555` | 1,620,000.00 USD | 0.00 USD | 1,900.00 USD | `-64.83%` | `34,249,500,000,000.00` |
| `Live` | `Long` | `0.0565` | 1,610,000.00 USD | 0.00 USD | 15,650.00 USD | `-64.20%` | `276,984,000,000,000.00` |
| `Live` | `Long` | `0.0575` | 1,600,000.00 USD | 0.00 USD | 865.75 USD | `-63.57%` | `15,056,600,000,000.00` |
| `Live` | `Long` | `0.0595` | 1,600,000.00 USD | 0.00 USD | 2,300.00 USD | `-62.30%` | `38,731,100,000,000.00` |
| `Live` | `Long` | `0.0605` | 1,600,000.00 USD | 0.00 USD | 3,930.00 USD | `-61.67%` | `65,000,000,000,000.00` |
| `Live` | `Long` | `0.0635` | 1,590,000.00 USD | 0.00 USD | 373.83 USD | `-59.76%` | `5,887,100,000,000.00` |
| `Live` | `Long` | `0.0675` | 1,590,000.00 USD | 0.00 USD | 106,660.00 USD | `-57.23%` | `1,580,216,900,000,000.00` |
| `Live` | `Long` | `0.0685` | 1,480,000.00 USD | 0.00 USD | 313.22 USD | `-56.60%` | `4,572,600,000,000.00` |
| `Live` | `Long` | `0.0695` | 1,480,000.00 USD | 0.00 USD | 976.14 USD | `-55.96%` | `14,045,200,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,480,000.00 USD | 0.00 USD | 2,970.00 USD | `-55.33%` | `42,142,800,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,480,000.00 USD | 0.00 USD | 6,000.00 USD | `-54.70%` | `83,896,800,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,470,000.00 USD | 0.00 USD | 111.58 USD | `-54.06%` | `1,539,100,000,000.00` |
| `Live` | `Long` | `0.0735` | 1,470,000.00 USD | 0.00 USD | 2,760.00 USD | `-53.43%` | `37,551,700,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,470,000.00 USD | 0.00 USD | 226.17 USD | `-52.79%` | `3,035,900,000,000.00` |
| `Live` | `Long` | `0.0755` | 1,470,000.00 USD | 0.00 USD | 63,580.00 USD | `-52.16%` | `842,071,000,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,410,000.00 USD | 0.00 USD | 14,940.00 USD | `-51.53%` | `195,248,400,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,390,000.00 USD | 0.00 USD | 4,630.00 USD | `-49.63%` | `58,261,800,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,390,000.00 USD | 0.00 USD | 20,720.00 USD | `-47.73%` | `251,208,100,000,000.00` |
| `Live` | `Long` | `0.0845` | 1,370,000.00 USD | 0.00 USD | 627.22 USD | `-46.46%` | `7,422,700,000,000.00` |
| `Live` | `Long` | `0.0855` | 1,370,000.00 USD | 0.00 USD | 2,460.00 USD | `-45.82%` | `28,821,700,000,000.00` |
| `Live` | `Long` | `0.0865` | 1,360,000.00 USD | 0.00 USD | 19,570.00 USD | `-45.19%` | `226,288,000,000,000.00` |
| `Live` | `Long` | `0.0875` | 1,340,000.00 USD | 0.00 USD | 162.28 USD | `-44.56%` | `1,854,600,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,340,000.00 USD | 0.00 USD | 362.62 USD | `-43.92%` | `4,097,400,000,000.00` |
| `Live` | `Long` | `0.0905` | 1,340,000.00 USD | 0.00 USD | 4,830.00 USD | `-42.66%` | `53,365,600,000,000.00` |
| `Live` | `Long` | `0.0915` | 1,340,000.00 USD | 0.00 USD | 626.82 USD | `-42.02%` | `6,850,500,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,340,000.00 USD | 0.00 USD | 2,420.00 USD | `-41.39%` | `26,112,600,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,340,000.00 USD | 0.00 USD | 814.24 USD | `-40.76%` | `8,708,500,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,340,000.00 USD | 0.00 USD | 1,510.00 USD | `-40.12%` | `16,031,700,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,330,000.00 USD | 0.00 USD | 1,990.00 USD | `-38.85%` | `20,667,500,000,000.00` |
| `Live` | `Long` | `0.0975` | 1,330,000.00 USD | 0.00 USD | 873.55 USD | `-38.22%` | `8,959,500,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,330,000.00 USD | 0.00 USD | 3,960.00 USD | `-37.59%` | `40,251,200,000,000.00` |
| `Live` | `Long` | `0.0995` | 1,330,000.00 USD | 0.00 USD | 9,660.00 USD | `-36.95%` | `97,071,300,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,320,000.00 USD | 0.00 USD | 1,850.00 USD | `-36.32%` | `18,436,400,000,000.00` |
| `Live` | `Long` | `0.1015` | 1,320,000.00 USD | 0.00 USD | 9,760.00 USD | `-35.69%` | `96,199,600,000,000.00` |
| `Live` | `Long` | `0.1025` | 1,310,000.00 USD | 0.00 USD | 8,960.00 USD | `-35.05%` | `87,419,000,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,300,000.00 USD | 0.00 USD | 4,570.00 USD | `-34.42%` | `44,179,000,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,290,000.00 USD | 0.00 USD | 9,470.00 USD | `-33.79%` | `90,639,100,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,280,000.00 USD | 0.00 USD | 8,600.00 USD | `-33.15%` | `81,510,300,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,270,000.00 USD | 0.00 USD | 1,230.00 USD | `-32.52%` | `11,505,500,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,270,000.00 USD | 0.00 USD | 1,060.00 USD | `-31.88%` | `9,856,300,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,270,000.00 USD | 0.00 USD | 12,400.00 USD | `-31.25%` | `114,250,900,000,000.00` |
| `Live` | `Long` | `0.1095` | 1,260,000.00 USD | 0.00 USD | 115,850.00 USD | `-30.62%` | `1,058,035,100,000,000.12` |
| `Live` | `Long` | `0.1105` | 1,140,000.00 USD | 0.00 USD | 14,360.00 USD | `-29.98%` | `129,913,800,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,130,000.00 USD | 0.00 USD | 425.50 USD | `-29.35%` | `3,816,100,000,000.00` |
| `Live` | `Long` | `0.1125` | 1,130,000.00 USD | 0.00 USD | 284.46 USD | `-28.72%` | `2,528,500,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,130,000.00 USD | 0.00 USD | 281.48 USD | `-28.08%` | `2,480,000,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,130,000.00 USD | 0.00 USD | 8,950.00 USD | `-27.45%` | `78,144,100,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,120,000.00 USD | 0.00 USD | 1,450.00 USD | `-26.82%` | `12,552,800,000,000.00` |
| `Live` | `Long` | `0.1165` | 1,120,000.00 USD | 0.00 USD | 1,480.00 USD | `-26.18%` | `12,734,000,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,120,000.00 USD | 0.00 USD | 6,120.00 USD | `-25.55%` | `52,087,700,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,110,000.00 USD | 0.00 USD | 32,130.00 USD | `-24.91%` | `271,171,599,999,999.97` |
| `Live` | `Long` | `0.1195` | 1,080,000.00 USD | 0.00 USD | 1,830.00 USD | `-24.28%` | `15,286,200,000,000.00` |
| `Live` | `Long` | `0.1205` | 1,080,000.00 USD | 0.00 USD | 537.83 USD | `-23.65%` | `4,463,300,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,080,000.00 USD | 0.00 USD | 303.75 USD | `-23.01%` | `2,500,000,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,080,000.00 USD | 0.00 USD | 17,890.00 USD | `-22.38%` | `146,077,300,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,060,000.00 USD | 0.00 USD | 50,790.00 USD | `-21.75%` | `411,276,600,000,000.00` |
| `Live` | `Long` | `0.1245` | 1,010,000.00 USD | 0.00 USD | 1,060.00 USD | `-21.11%` | `8,486,000,000,000.00` |
| `Live` | `Long` | `0.1255` | 1,010,000.00 USD | 0.00 USD | 134.66 USD | `-20.48%` | `1,073,000,000,000.00` |
| `Live` | `Long` | `0.1265` | 1,010,000.00 USD | 0.00 USD | 29,370.00 USD | `-19.85%` | `232,151,600,000,000.00` |
| `Live` | `Long` | `0.1285` | 976,160.00 USD | 0.00 USD | 11,500.00 USD | `-18.58%` | `89,517,400,000,000.00` |
| `Live` | `Long` | `0.1295` | 964,660.00 USD | 0.00 USD | 2,130.00 USD | `-17.94%` | `16,434,900,000,000.00` |
| `Live` | `Long` | `0.1305` | 962,530.00 USD | 0.00 USD | 16,660.00 USD | `-17.31%` | `127,649,400,000,000.00` |
| `Live` | `Long` | `0.1315` | 945,870.00 USD | 0.00 USD | 9,010.00 USD | `-16.68%` | `68,542,899,999,999.99` |
| `Live` | `Long` | `0.1325` | 936,860.00 USD | 0.00 USD | 4,810.00 USD | `-16.04%` | `36,288,800,000,000.00` |
| `Live` | `Long` | `0.1335` | 932,050.00 USD | 0.00 USD | 72,590.00 USD | `-15.41%` | `543,725,300,000,000.06` |
| `Live` | `Long` | `0.1345` | 859,460.00 USD | 0.00 USD | 29,490.00 USD | `-14.78%` | `219,238,900,000,000.00` |
| `Live` | `Long` | `0.1355` | 829,980.00 USD | 0.00 USD | 3,540.00 USD | `-14.14%` | `26,114,400,000,000.00` |
| `Live` | `Long` | `0.1365` | 826,440.00 USD | 0.00 USD | 10,630.00 USD | `-13.51%` | `77,872,500,000,000.00` |
| `Live` | `Long` | `0.1375` | 815,810.00 USD | 0.00 USD | 13,710.00 USD | `-12.88%` | `99,721,600,000,000.00` |
| `Live` | `Long` | `0.1385` | 802,100.00 USD | 0.00 USD | 5,580.00 USD | `-12.24%` | `40,282,400,000,000.00` |
| `Live` | `Long` | `0.1395` | 796,520.00 USD | 0.00 USD | 17,790.00 USD | `-11.61%` | `127,514,300,000,000.00` |
| `Live` | `Long` | `0.1405` | 778,730.00 USD | 0.00 USD | 1,360.00 USD | `-10.97%` | `9,649,700,000,000.00` |
| `Live` | `Long` | `0.1415` | 777,370.00 USD | 0.00 USD | 22,710.00 USD | `-10.34%` | `160,521,200,000,000.00` |
| `Live` | `Long` | `0.1425` | 754,660.00 USD | 0.00 USD | 499,000.00 USD | `-9.71%` | `3,501,785,500,000,000.00` |
| `Live` | `Long` | `0.1435` | 255,650.00 USD | 0.00 USD | 19,630.00 USD | `-9.07%` | `136,775,600,000,000.00` |
| `Live` | `Long` | `0.1445` | 236,030.00 USD | 0.00 USD | 9,510.00 USD | `-8.44%` | `65,841,200,000,000.00` |
| `Live` | `Long` | `0.1455` | 226,510.00 USD | 0.00 USD | 91,680.00 USD | `-7.81%` | `630,101,100,000,000.00` |
| `Live` | `Long` | `0.1465` | 134,830.00 USD | 0.00 USD | 35,140.00 USD | `-7.17%` | `239,864,000,000,000.00` |
| `Live` | `Long` | `0.1475` | 99,690.00 USD | 0.00 USD | 84,080.00 USD | `-6.54%` | `570,006,200,000,000.00` |
| `Live` | `Long` | `0.1485` | 15,620.00 USD | 0.00 USD | 2,290.00 USD | `-5.91%` | `15,410,500,000,000.00` |
| `Live` | `Long` | `0.1495` | 13,330.00 USD | 0.00 USD | 7,610.00 USD | `-5.27%` | `50,915,500,000,000.00` |
| `Live` | `Long` | `0.1545` | 5,720.00 USD | 0.00 USD | 5,720.00 USD | `-2.10%` | `37,000,000,000,000.00` |
| `Live` | `Short` | `0.1605` | 3,930.00 USD | 3,930.00 USD | 0.00 USD | `+1.70%` | `24,462,100,000,000.00` |
| `Live` | `Short` | `0.1615` | 8,050.00 USD | 4,130.00 USD | 0.00 USD | `+2.33%` | `25,565,100,000,000.00` |
| `Live` | `Short` | `0.1625` | 9,870.00 USD | 1,810.00 USD | 0.00 USD | `+2.97%` | `11,163,300,000,000.00` |
| `Live` | `Short` | `0.1635` | 11,500.00 USD | 1,630.00 USD | 0.00 USD | `+3.60%` | `9,980,600,000,000.00` |
| `Live` | `Short` | `0.1645` | 11,620.00 USD | 118.90 USD | 0.00 USD | `+4.23%` | `722,800,000,000.00` |
| `Live` | `Short` | `0.1665` | 12,170.00 USD | 547.98 USD | 0.00 USD | `+5.50%` | `3,291,200,000,000.00` |
| `Live` | `Short` | `0.1715` | 14,540.00 USD | 2,370.00 USD | 0.00 USD | `+8.67%` | `13,821,800,000,000.00` |
| `Live` | `Short` | `0.1745` | 18,800.00 USD | 4,260.00 USD | 0.00 USD | `+10.57%` | `24,413,200,000,000.00` |
| `Live` | `Short` | `0.1775` | 19,110.00 USD | 316.07 USD | 0.00 USD | `+12.47%` | `1,780,700,000,000.00` |
| `Live` | `Short` | `0.1785` | 19,250.00 USD | 138.82 USD | 0.00 USD | `+13.10%` | `777,700,000,000.00` |
| `Live` | `Short` | `0.1915` | 20,850.00 USD | 1,600.00 USD | 0.00 USD | `+21.34%` | `8,339,400,000,000.00` |
| `Live` | `Short` | `0.1925` | 21,390.00 USD | 543.50 USD | 0.00 USD | `+21.97%` | `2,823,400,000,000.00` |
| `Live` | `Short` | `0.1945` | 22,020.00 USD | 623.68 USD | 0.00 USD | `+23.24%` | `3,206,600,000,000.00` |
| `Live` | `Short` | `0.1975` | 22,170.00 USD | 150.10 USD | 0.00 USD | `+25.14%` | `760,000,000,000.00` |
| `Live` | `Short` | `0.2005` | 25,100.00 USD | 2,940.00 USD | 0.00 USD | `+27.04%` | `14,639,700,000,000.00` |
| `Live` | `Short` | `0.2045` | 25,290.00 USD | 184.58 USD | 0.00 USD | `+29.58%` | `902,600,000,000.00` |
| `Live` | `Short` | `0.2055` | 36,880.00 USD | 11,590.00 USD | 0.00 USD | `+30.21%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2085` | 37,080.00 USD | 198.08 USD | 0.00 USD | `+32.11%` | `950,000,000,000.00` |
| `Live` | `Short` | `0.2095` | 37,240.00 USD | 164.23 USD | 0.00 USD | `+32.75%` | `783,900,000,000.00` |
| `Live` | `Short` | `0.2135` | 52,940.00 USD | 15,690.00 USD | 0.00 USD | `+35.28%` | `73,505,600,000,000.00` |
| `Live` | `Short` | `0.2155` | 94,270.00 USD | 41,330.00 USD | 0.00 USD | `+36.55%` | `191,801,700,000,000.00` |
| `Live` | `Short` | `0.2175` | 94,480.00 USD | 213.22 USD | 0.00 USD | `+37.82%` | `980,300,000,000.00` |
| `Live` | `Short` | `0.2195` | 182,280.00 USD | 87,800.00 USD | 0.00 USD | `+39.08%` | `400,000,000,000,000.00` |
| `Live` | `Short` | `0.2205` | 208,520.00 USD | 26,240.00 USD | 0.00 USD | `+39.72%` | `118,989,500,000,000.00` |
| `Live` | `Short` | `0.2235` | 208,630.00 USD | 114.52 USD | 0.00 USD | `+41.62%` | `512,400,000,000.00` |
| `Live` | `Short` | `0.2255` | 208,790.00 USD | 154.78 USD | 0.00 USD | `+42.88%` | `686,400,000,000.00` |
| `Live` | `Short` | `0.2295` | 215,610.00 USD | 6,820.00 USD | 0.00 USD | `+45.42%` | `29,727,000,000,000.00` |
| `Live` | `Short` | `0.2325` | 240,070.00 USD | 24,460.00 USD | 0.00 USD | `+47.32%` | `105,188,200,000,000.00` |
| `Live` | `Short` | `0.2355` | 256,000.00 USD | 15,930.00 USD | 0.00 USD | `+49.22%` | `67,638,800,000,000.00` |
| `Live` | `Short` | `0.2375` | 256,100.00 USD | 102.62 USD | 0.00 USD | `+50.49%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2425` | 256,890.00 USD | 796.25 USD | 0.00 USD | `+53.66%` | `3,283,500,000,000.00` |
| `Live` | `Short` | `0.2445` | 261,820.00 USD | 4,930.00 USD | 0.00 USD | `+54.92%` | `20,150,900,000,000.00` |
| `Live` | `Short` | `0.2455` | 262,050.00 USD | 231.97 USD | 0.00 USD | `+55.56%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2465` | 311,350.00 USD | 49,300.00 USD | 0.00 USD | `+56.19%` | `200,003,000,000,000.00` |
| `Live` | `Short` | `0.2545` | 311,900.00 USD | 546.54 USD | 0.00 USD | `+61.26%` | `2,147,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 315,770.00 USD | 3,870.00 USD | 0.00 USD | `+62.53%` | `15,070,700,000,000.00` |
| `Live` | `Short` | `0.2575` | 344,680.00 USD | 28,910.00 USD | 0.00 USD | `+63.16%` | `112,272,400,000,000.00` |
| `Live` | `Short` | `0.2585` | 397,290.00 USD | 52,620.00 USD | 0.00 USD | `+63.79%` | `203,548,800,000,000.00` |
| `Live` | `Short` | `0.2615` | 397,450.00 USD | 154.94 USD | 0.00 USD | `+65.70%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2685` | 397,680.00 USD | 226.51 USD | 0.00 USD | `+70.13%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2715` | 410,920.00 USD | 13,240.00 USD | 0.00 USD | `+72.03%` | `48,778,100,000,000.00` |
| `Live` | `Short` | `0.2725` | 411,130.00 USD | 214.21 USD | 0.00 USD | `+72.67%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 422,730.00 USD | 11,600.00 USD | 0.00 USD | `+73.93%` | `42,249,200,000,000.00` |
| `Live` | `Short` | `0.2795` | 423,210.00 USD | 482.84 USD | 0.00 USD | `+77.10%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2895` | 718,770.00 USD | 295,560.00 USD | 0.00 USD | `+83.44%` | `1,020,921,300,000,000.00` |
| `Live` | `Short` | `0.2915` | 718,960.00 USD | 187.26 USD | 0.00 USD | `+84.70%` | `642,400,000,000.00` |
| `Live` | `Short` | `0.2925` | 719,750.00 USD | 794.52 USD | 0.00 USD | `+85.34%` | `2,716,300,000,000.00` |
| `Live` | `Short` | `0.3035` | 720,230.00 USD | 482.72 USD | 0.00 USD | `+92.31%` | `1,590,500,000,000.00` |
| `Live` | `Short` | `0.3045` | 722,550.00 USD | 2,320.00 USD | 0.00 USD | `+92.94%` | `7,608,100,000,000.00` |
| `Live` | `Short` | `0.3075` | 728,840.00 USD | 6,290.00 USD | 0.00 USD | `+94.84%` | `20,460,400,000,000.00` |
| `Live` | `Short` | `0.3085` | 729,210.00 USD | 363.72 USD | 0.00 USD | `+95.48%` | `1,179,000,000,000.00` |
| `Live` | `Short` | `0.3105` | 741,130.00 USD | 11,930.00 USD | 0.00 USD | `+96.74%` | `38,407,000,000,000.00` |
| `Live` | `Short` | `0.3145` | 741,610.00 USD | 482.22 USD | 0.00 USD | `+99.28%` | `1,533,300,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0355` | 704,290.00 USD | 0.00 USD | 355.00 USD | `-77.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 703,930.00 USD | 0.00 USD | 297.50 USD | `-73.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 703,630.00 USD | 0.00 USD | 353.50 USD | `-68.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0545` | 703,280.00 USD | 0.00 USD | 276.53 USD | `-65.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 703,000.00 USD | 0.00 USD | 4,310.00 USD | `-64.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 698,690.00 USD | 0.00 USD | 475.11 USD | `-59.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 698,220.00 USD | 0.00 USD | 131.16 USD | `-58.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 698,080.00 USD | 0.00 USD | 881.45 USD | `-57.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 697,200.00 USD | 0.00 USD | 1,070.00 USD | `-57.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 696,130.00 USD | 0.00 USD | 1,050.00 USD | `-56.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 695,080.00 USD | 0.00 USD | 1,010.00 USD | `-55.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 694,070.00 USD | 0.00 USD | 4,100.00 USD | `-55.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 689,970.00 USD | 0.00 USD | 529.04 USD | `-54.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 689,440.00 USD | 0.00 USD | 2,390.00 USD | `-54.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 687,050.00 USD | 0.00 USD | 757.39 USD | `-52.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 686,290.00 USD | 0.00 USD | 1,490.00 USD | `-50.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 684,810.00 USD | 0.00 USD | 277.37 USD | `-45.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 684,530.00 USD | 0.00 USD | 262.50 USD | `-44.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 684,270.00 USD | 0.00 USD | 795.57 USD | `-43.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 683,470.00 USD | 0.00 USD | 181.00 USD | `-42.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 683,290.00 USD | 0.00 USD | 3,810.00 USD | `-36.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 679,480.00 USD | 0.00 USD | 1,550.00 USD | `-35.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 677,930.00 USD | 0.00 USD | 116.07 USD | `-31.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 677,810.00 USD | 0.00 USD | 19,070.00 USD | `-31.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 658,740.00 USD | 0.00 USD | 577.22 USD | `-29.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 658,160.00 USD | 0.00 USD | 343.50 USD | `-27.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 657,820.00 USD | 0.00 USD | 26,280.00 USD | `-26.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1175` | 631,540.00 USD | 0.00 USD | 105.75 USD | `-25.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 631,440.00 USD | 0.00 USD | 24,280.00 USD | `-23.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 607,150.00 USD | 0.00 USD | 83,620.00 USD | `-23.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1225` | 523,530.00 USD | 0.00 USD | 487.10 USD | `-22.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 523,040.00 USD | 0.00 USD | 14,940.00 USD | `-21.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1255` | 508,100.00 USD | 0.00 USD | 129,320.00 USD | `-20.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 378,780.00 USD | 0.00 USD | 2,670.00 USD | `-19.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 376,110.00 USD | 0.00 USD | 473.27 USD | `-19.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 375,640.00 USD | 0.00 USD | 203,210.00 USD | `-18.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 172,430.00 USD | 0.00 USD | 2,800.00 USD | `-17.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1315` | 169,630.00 USD | 0.00 USD | 1,590.00 USD | `-16.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 168,040.00 USD | 0.00 USD | 6,000.00 USD | `-16.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 162,040.00 USD | 0.00 USD | 795.99 USD | `-15.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 161,240.00 USD | 0.00 USD | 502.28 USD | `-14.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 160,740.00 USD | 0.00 USD | 162.60 USD | `-14.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 160,580.00 USD | 0.00 USD | 700.86 USD | `-13.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 159,870.00 USD | 0.00 USD | 13,710.00 USD | `-12.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 146,160.00 USD | 0.00 USD | 108.57 USD | `-12.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 146,050.00 USD | 0.00 USD | 3,520.00 USD | `-10.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 142,530.00 USD | 0.00 USD | 127.35 USD | `-10.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 142,400.00 USD | 0.00 USD | 24,850.00 USD | `-9.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 117,560.00 USD | 0.00 USD | 1,300.00 USD | `-9.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 116,250.00 USD | 0.00 USD | 25,960.00 USD | `-8.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 90,300.00 USD | 0.00 USD | 46,480.00 USD | `-7.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 43,820.00 USD | 0.00 USD | 14,830.00 USD | `-7.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 28,990.00 USD | 0.00 USD | 3,470.00 USD | `-6.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 25,520.00 USD | 0.00 USD | 3,610.00 USD | `-5.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 21,910.00 USD | 0.00 USD | 2,390.00 USD | `-5.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 19,520.00 USD | 0.00 USD | 3,010.00 USD | `-4.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 16,510.00 USD | 0.00 USD | 192.48 USD | `-4.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 16,320.00 USD | 0.00 USD | 4,890.00 USD | `-3.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1535` | 11,430.00 USD | 0.00 USD | 175.79 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 11,250.00 USD | 0.00 USD | 197.87 USD | `-2.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 11,050.00 USD | 0.00 USD | 10,670.00 USD | `-1.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 384.42 USD | 0.00 USD | 182.71 USD | `-0.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1575` | 201.71 USD | 0.00 USD | 201.71 USD | `-0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1585` | 1,350.00 USD | 1,350.00 USD | 0.00 USD | `+0.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1595` | 4,210.00 USD | 2,860.00 USD | 0.00 USD | `+1.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1605` | 6,660.00 USD | 2,450.00 USD | 0.00 USD | `+1.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1615` | 8,270.00 USD | 1,620.00 USD | 0.00 USD | `+2.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1625` | 8,520.00 USD | 249.16 USD | 0.00 USD | `+2.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 9,570.00 USD | 1,040.00 USD | 0.00 USD | `+3.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1645` | 72,300.00 USD | 62,730.00 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1655` | 75,490.00 USD | 3,190.00 USD | 0.00 USD | `+4.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1665` | 114,530.00 USD | 39,040.00 USD | 0.00 USD | `+5.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1675` | 115,120.00 USD | 589.50 USD | 0.00 USD | `+6.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1685` | 116,260.00 USD | 1,150.00 USD | 0.00 USD | `+6.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 116,580.00 USD | 317.95 USD | 0.00 USD | `+7.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 117,150.00 USD | 564.90 USD | 0.00 USD | `+8.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 118,950.00 USD | 1,800.00 USD | 0.00 USD | `+8.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 119,520.00 USD | 571.13 USD | 0.00 USD | `+9.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 128,350.00 USD | 8,840.00 USD | 0.00 USD | `+9.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 128,570.00 USD | 219.54 USD | 0.00 USD | `+10.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 129,930.00 USD | 1,350.00 USD | 0.00 USD | `+11.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 130,610.00 USD | 683.00 USD | 0.00 USD | `+11.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 130,950.00 USD | 336.40 USD | 0.00 USD | `+12.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 133,410.00 USD | 2,470.00 USD | 0.00 USD | `+13.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 159,800.00 USD | 26,390.00 USD | 0.00 USD | `+13.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 171,340.00 USD | 11,540.00 USD | 0.00 USD | `+14.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 181,580.00 USD | 10,240.00 USD | 0.00 USD | `+15.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 182,450.00 USD | 864.12 USD | 0.00 USD | `+15.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 184,970.00 USD | 2,520.00 USD | 0.00 USD | `+16.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 185,250.00 USD | 276.75 USD | 0.00 USD | `+16.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 185,380.00 USD | 128.68 USD | 0.00 USD | `+17.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 188,750.00 USD | 3,370.00 USD | 0.00 USD | `+18.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 192,450.00 USD | 3,700.00 USD | 0.00 USD | `+18.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 192,700.00 USD | 245.50 USD | 0.00 USD | `+19.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 193,230.00 USD | 531.47 USD | 0.00 USD | `+20.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 193,920.00 USD | 697.34 USD | 0.00 USD | `+20.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 194,150.00 USD | 222.24 USD | 0.00 USD | `+21.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 223,270.00 USD | 29,130.00 USD | 0.00 USD | `+21.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 230,340.00 USD | 7,070.00 USD | 0.00 USD | `+22.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 230,540.00 USD | 194.50 USD | 0.00 USD | `+23.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 230,680.00 USD | 137.77 USD | 0.00 USD | `+23.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 230,810.00 USD | 133.19 USD | 0.00 USD | `+24.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 234,560.00 USD | 3,750.00 USD | 0.00 USD | `+25.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 235,050.00 USD | 492.19 USD | 0.00 USD | `+26.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 257,810.00 USD | 22,750.00 USD | 0.00 USD | `+27.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 258,370.00 USD | 560.96 USD | 0.00 USD | `+27.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 279,710.00 USD | 21,340.00 USD | 0.00 USD | `+28.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 365,600.00 USD | 85,900.00 USD | 0.00 USD | `+29.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 367,070.00 USD | 1,470.00 USD | 0.00 USD | `+30.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 367,240.00 USD | 174.20 USD | 0.00 USD | `+30.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 369,320.00 USD | 2,080.00 USD | 0.00 USD | `+31.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 369,570.00 USD | 252.51 USD | 0.00 USD | `+32.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 371,940.00 USD | 2,370.00 USD | 0.00 USD | `+33.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 372,070.00 USD | 126.50 USD | 0.00 USD | `+34.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 372,420.00 USD | 356.72 USD | 0.00 USD | `+34.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 372,780.00 USD | 361.76 USD | 0.00 USD | `+36.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2175` | 373,150.00 USD | 365.12 USD | 0.00 USD | `+37.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 379,430.00 USD | 6,280.00 USD | 0.00 USD | `+38.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 379,800.00 USD | 368.47 USD | 0.00 USD | `+39.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 402,290.00 USD | 22,490.00 USD | 0.00 USD | `+39.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 402,620.00 USD | 333.91 USD | 0.00 USD | `+40.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 406,600.00 USD | 3,980.00 USD | 0.00 USD | `+41.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 406,980.00 USD | 378.55 USD | 0.00 USD | `+42.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 407,360.00 USD | 380.23 USD | 0.00 USD | `+43.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 407,540.00 USD | 185.87 USD | 0.00 USD | `+44.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 411,380.00 USD | 3,840.00 USD | 0.00 USD | `+44.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 445,200.00 USD | 33,820.00 USD | 0.00 USD | `+46.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 449,460.00 USD | 4,260.00 USD | 0.00 USD | `+47.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 450,970.00 USD | 1,520.00 USD | 0.00 USD | `+47.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 472,200.00 USD | 21,230.00 USD | 0.00 USD | `+50.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 474,730.00 USD | 2,530.00 USD | 0.00 USD | `+51.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 494,450.00 USD | 19,720.00 USD | 0.00 USD | `+52.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 503,750.00 USD | 9,300.00 USD | 0.00 USD | `+53.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 505,660.00 USD | 1,910.00 USD | 0.00 USD | `+55.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 524,410.00 USD | 18,750.00 USD | 0.00 USD | `+56.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 524,960.00 USD | 551.23 USD | 0.00 USD | `+56.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 525,360.00 USD | 397.90 USD | 0.00 USD | `+58.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 529,700.00 USD | 4,330.00 USD | 0.00 USD | `+58.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 530,020.00 USD | 320.66 USD | 0.00 USD | `+59.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 545,900.00 USD | 15,880.00 USD | 0.00 USD | `+60.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 547,900.00 USD | 2,000.00 USD | 0.00 USD | `+61.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 550,450.00 USD | 2,550.00 USD | 0.00 USD | `+61.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 562,180.00 USD | 11,730.00 USD | 0.00 USD | `+62.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 567,340.00 USD | 5,160.00 USD | 0.00 USD | `+63.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 584,210.00 USD | 16,870.00 USD | 0.00 USD | `+64.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 611,000.00 USD | 26,790.00 USD | 0.00 USD | `+65.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 611,270.00 USD | 272.88 USD | 0.00 USD | `+71.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2755` | 611,380.00 USD | 114.99 USD | 0.00 USD | `+74.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 611,780.00 USD | 394.01 USD | 0.00 USD | `+75.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 612,150.00 USD | 375.53 USD | 0.00 USD | `+77.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 614,290.00 USD | 2,130.00 USD | 0.00 USD | `+80.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 614,870.00 USD | 579.27 USD | 0.00 USD | `+81.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 616,620.00 USD | 1,750.00 USD | 0.00 USD | `+84.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 616,720.00 USD | 101.21 USD | 0.00 USD | `+87.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 616,980.00 USD | 262.73 USD | 0.00 USD | `+87.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 618,420.00 USD | 1,440.00 USD | 0.00 USD | `+88.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 623,850.00 USD | 5,430.00 USD | 0.00 USD | `+90.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 629,280.00 USD | 5,430.00 USD | 0.00 USD | `+91.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 629,570.00 USD | 289.61 USD | 0.00 USD | `+93.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3065` | 630,060.00 USD | 487.09 USD | 0.00 USD | `+94.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3095` | 636,630.00 USD | 6,570.00 USD | 0.00 USD | `+96.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 641,800.00 USD | 5,180.00 USD | 0.00 USD | `+99.28%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1304` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 4,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1310` | 8,290,000.00 USD | 0.00 USD | 8,290,000.00 USD | 6,470.00 USD | 4,610.00 USD | 4,440.00 USD |
| `7D` | `0.1313` | 8,280,000.00 USD | 0.00 USD | 8,280,000.00 USD | 0.00 USD | 4,010.00 USD | 2,660.00 USD |
| `7D` | `0.1316` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 9,620.00 USD | 4,840.00 USD | 2,140.00 USD |
| `7D` | `0.1319` | 8,250,000.00 USD | 0.00 USD | 8,250,000.00 USD | 4,630.00 USD | 0.00 USD | 18,380.00 USD |
| `7D` | `0.1322` | 8,230,000.00 USD | 0.00 USD | 8,230,000.00 USD | 5,580.00 USD | 2,780.00 USD | 12,990.00 USD |
| `7D` | `0.1325` | 8,210,000.00 USD | 0.00 USD | 8,210,000.00 USD | 0.00 USD | 3,040.00 USD | 4,560.00 USD |
| `7D` | `0.1328` | 8,200,000.00 USD | 0.00 USD | 8,200,000.00 USD | 19,000.00 USD | 7,370.00 USD | 8,920.00 USD |
| `7D` | `0.1331` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 13,420.00 USD | 4,240.00 USD | 7,210.00 USD |
| `7D` | `0.1334` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 3,580.00 USD | 3,230.00 USD | 7,810.00 USD |
| `7D` | `0.1337` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 2,830.00 USD | 4,520.00 USD | 19,560.00 USD |
| `7D` | `0.1340` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 6,330.00 USD | 5,970.00 USD | 13,100.00 USD |
| `7D` | `0.1343` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 0.00 USD | 5,790.00 USD | 13,540.00 USD |
| `7D` | `0.1346` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 33,130.00 USD | 5,000.00 USD | 21,650.00 USD |
| `7D` | `0.1349` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 4,450.00 USD | 2,140.00 USD | 19,300.00 USD |
| `7D` | `0.1352` | 7,970,000.00 USD | 0.00 USD | 7,970,000.00 USD | 11,390.00 USD | 6,290.00 USD | 13,140.00 USD |
| `7D` | `0.1355` | 7,940,000.00 USD | 0.00 USD | 7,940,000.00 USD | 7,540.00 USD | 9,000.00 USD | 6,460.00 USD |
| `7D` | `0.1358` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 25,150.00 USD | 9,870.00 USD | 5,370.00 USD |
| `7D` | `0.1361` | 7,880,000.00 USD | 0.00 USD | 7,880,000.00 USD | 8,700.00 USD | 1,930.00 USD | 6,320.00 USD |
| `7D` | `0.1364` | 7,860,000.00 USD | 0.00 USD | 7,860,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD |
| `7D` | `0.1367` | 7,840,000.00 USD | 0.00 USD | 7,840,000.00 USD | 4,500.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `0.1370` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD |
| `7D` | `0.1373` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 4,620.00 USD | 0.00 USD | 35,720.00 USD |
| `7D` | `0.1379` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD |
| `7D` | `0.1385` | 7,760,000.00 USD | 0.00 USD | 7,760,000.00 USD | 11,880.00 USD | 0.00 USD | 42,090.00 USD |
| `7D` | `0.1388` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1391` | 7,690,000.00 USD | 0.00 USD | 7,690,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD |
| `1D` | `0.1393` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 9,960.00 USD | 2,340.00 USD | 74,280.00 USD |
| `7D` | `0.1394` | 7,640,000.00 USD | 0.00 USD | 7,640,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD |
| `1D` | `0.1396` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 13,480.00 USD | 6,230.00 USD | 0.00 USD |
| `7D` | `0.1397` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD |
| `1D` | `0.1399` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 5,720.00 USD | 953.16 USD | 1,480.00 USD |
| `7D` | `0.1400` | 7,610,000.00 USD | 0.00 USD | 7,610,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD |
| `1D` | `0.1402` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 9,130.00 USD | 2,100.00 USD | 0.00 USD |
| `7D` | `0.1403` | 7,600,000.00 USD | 0.00 USD | 7,600,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1405` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 2,140.00 USD | 3,150.00 USD | 0.00 USD |
| `1D` | `0.1411` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 0.00 USD | 3,980.00 USD | 0.00 USD |
| `7D` | `0.1418` | 7,590,000.00 USD | 0.00 USD | 7,590,000.00 USD | 0.00 USD | 0.00 USD | 14,680.00 USD |
| `1D` | `0.1420` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 3,280.00 USD | 1,560.00 USD | 1,170.00 USD |
| `7D` | `0.1421` | 7,570,000.00 USD | 0.00 USD | 7,570,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD |
| `1D` | `0.1423` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 6,100.00 USD | 4,580.00 USD | 8,910.00 USD |
| `1D` | `0.1426` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD |
| `1D` | `0.1429` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1430` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `0.1433` | 7,550,000.00 USD | 0.00 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 5,270.00 USD |
| `1D` | `0.1435` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 6,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1436` | 7,550,000.00 USD | 0.00 USD | 7,550,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD |
| `1D` | `0.1438` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 4,370.00 USD | 3,590.00 USD | 23,000.00 USD |
| `7D` | `0.1439` | 7,510,000.00 USD | 0.00 USD | 7,510,000.00 USD | 27,370.00 USD | 0.00 USD | 3,610.00 USD |
| `1D` | `0.1441` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 17,680.00 USD | 0.00 USD | 1,850.00 USD |
| `7D` | `0.1442` | 7,480,000.00 USD | 0.00 USD | 7,480,000.00 USD | 3,450.00 USD | 5,260.00 USD | 6,160.00 USD |
| `1D` | `0.1444` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 0.00 USD | 9,660.00 USD | 2,970.00 USD |
| `1D` | `0.1447` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 0.00 USD | 5,160.00 USD | 0.00 USD |
| `1D` | `0.1450` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 13,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1451` | 7,460,000.00 USD | 0.00 USD | 7,460,000.00 USD | 0.00 USD | 10,680.00 USD | 5,150.00 USD |
| `1D` | `0.1453` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 15,450.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.1454` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 9,030.00 USD |
| `1D` | `0.1456` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 3,450.00 USD | 1,610.00 USD | 2,080.00 USD |
| `1D` | `0.1459` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 0.00 USD | 4,870.00 USD | 3,350.00 USD |
| `1D` | `0.1462` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 0.00 USD | 5,690.00 USD | 1,760.00 USD |
| `1D` | `0.1465` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 17,970.00 USD | 5,840.00 USD | 17,070.00 USD |
| `7D` | `0.1466` | 7,440,000.00 USD | 0.00 USD | 7,440,000.00 USD | 9,720.00 USD | 5,520.00 USD | 93,240.00 USD |
| `1D` | `0.1468` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 12,090.00 USD | 2,700.00 USD | 8,060.00 USD |
| `7D` | `0.1469` | 7,330,000.00 USD | 0.00 USD | 7,330,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD |
| `1D` | `0.1471` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 10,130.00 USD | 14,560.00 USD | 1,210.00 USD |
| `7D` | `0.1472` | 7,320,000.00 USD | 0.00 USD | 7,320,000.00 USD | 12,940.00 USD | 0.00 USD | 14,170.00 USD |
| `1D` | `0.1474` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 45,330.00 USD | 27,310.00 USD | 76,930.00 USD |
| `7D` | `0.1475` | 7,290,000.00 USD | 0.00 USD | 7,290,000.00 USD | 24,840.00 USD | 13,040.00 USD | 0.00 USD |
| `1D` | `0.1477` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 108,940.00 USD | 23,730.00 USD | 158,030.00 USD |
| `7D` | `0.1478` | 7,260,000.00 USD | 0.00 USD | 7,260,000.00 USD | 110,850.00 USD | 33,410.00 USD | 125,110.00 USD |
| `1D` | `0.1480` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 96,250.00 USD | 11,170.00 USD | 25,870.00 USD |
| `7D` | `0.1481` | 6,990,000.00 USD | 0.00 USD | 6,990,000.00 USD | 41,960.00 USD | 31,150.00 USD | 19,470.00 USD |
| `1D` | `0.1483` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 41,250.00 USD | 4,610.00 USD | 126,170.00 USD |
| `7D` | `0.1484` | 6,890,000.00 USD | 0.00 USD | 6,890,000.00 USD | 12,060.00 USD | 3,040.00 USD | 188,220.00 USD |
| `1D` | `0.1486` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 46,070.00 USD | 0.00 USD | 65,260.00 USD |
| `7D` | `0.1487` | 6,690,000.00 USD | 0.00 USD | 6,690,000.00 USD | 61,970.00 USD | 10,470.00 USD | 20,080.00 USD |
| `1D` | `0.1489` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 33,690.00 USD | 0.00 USD | 8,920.00 USD |
| `7D` | `0.1490` | 6,600,000.00 USD | 0.00 USD | 6,600,000.00 USD | 28,940.00 USD | 9,780.00 USD | 77,920.00 USD |
| `1D` | `0.1492` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 24,040.00 USD | 18,130.00 USD | 9,580.00 USD |
| `7D` | `0.1493` | 6,480,000.00 USD | 0.00 USD | 6,480,000.00 USD | 27,770.00 USD | 17,120.00 USD | 20,270.00 USD |
| `1D` | `0.1495` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 71,540.00 USD | 0.00 USD | 28,520.00 USD |
| `7D` | `0.1496` | 6,420,000.00 USD | 0.00 USD | 6,420,000.00 USD | 29,430.00 USD | 13,380.00 USD | 195,710.00 USD |
| `1D` | `0.1498` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 8,630.00 USD | 4,640.00 USD | 347.81 USD |
| `7D` | `0.1499` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 60,500.00 USD | 9,610.00 USD | 17,350.00 USD |
| `1D` | `0.1501` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 20,980.00 USD | 16,380.00 USD | 5,560.00 USD |
| `7D` | `0.1502` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 2,610.00 USD | 9,860.00 USD | 4,600.00 USD |
| `1D` | `0.1504` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 84,100.00 USD | 6,340.00 USD | 160,460.00 USD |
| `7D` | `0.1505` | 6,070,000.00 USD | 0.00 USD | 6,070,000.00 USD | 67,080.00 USD | 21,620.00 USD | 52,590.00 USD |
| `1D` | `0.1507` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 0.00 USD | 1,150.00 USD | 307,540.00 USD |
| `7D` | `0.1508` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 151,240.00 USD | 4,870.00 USD | 248,410.00 USD |
| `1D` | `0.1510` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 0.00 USD | 6,130.00 USD | 50,780.00 USD |
| `7D` | `0.1511` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 86,820.00 USD | 11,590.00 USD | 38,070.00 USD |
| `1D` | `0.1513` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 11,750.00 USD | 3,900.00 USD | 250,320.00 USD |
| `7D` | `0.1514` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 0.00 USD | 15,050.00 USD | 367,590.00 USD |
| `1D` | `0.1516` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 12,230.00 USD | 0.00 USD | 141,160.00 USD |
| `7D` | `0.1517` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 96,310.00 USD | 4,290.00 USD | 119,870.00 USD |
| `1D` | `0.1519` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 47,400.00 USD | 13,370.00 USD | 35,270.00 USD |
| `7D` | `0.1520` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 0.00 USD | 22,600.00 USD | 156,830.00 USD |
| `1D` | `0.1522` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 33,890.00 USD | 4,770.00 USD | 13,640.00 USD |
| `7D` | `0.1523` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 0.00 USD | 15,080.00 USD | 0.00 USD |
| `1D` | `0.1525` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 48,970.00 USD | 0.00 USD | 3,130.00 USD |
| `7D` | `0.1526` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 0.00 USD | 38,870.00 USD | 0.00 USD |
| `1D` | `0.1528` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 29,740.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1529` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD |
| `1D` | `0.1531` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 12,670.00 USD | 18,920.00 USD | 4,670.00 USD |
| `7D` | `0.1532` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 0.00 USD | 14,780.00 USD | 0.00 USD |
| `1D` | `0.1534` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 10,930.00 USD | 1,760.00 USD | 11,690.00 USD |
| `7D` | `0.1535` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 35,470.00 USD | 8,570.00 USD | 0.00 USD |
| `1D` | `0.1537` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 4,040.00 USD | 18,160.00 USD | 10,570.00 USD |
| `7D` | `0.1538` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 0.00 USD | 14,700.00 USD | 0.00 USD |
| `1D` | `0.1540` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 27,770.00 USD | 4,030.00 USD | 7,440.00 USD |
| `7D` | `0.1541` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD |
| `1D` | `0.1543` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 4,600.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1544` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD |
| `1D` | `0.1546` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 24,160.00 USD | 7,790.00 USD | 5,850.00 USD |
| `7D` | `0.1547` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 0.00 USD | 12,560.00 USD | 89,090.00 USD |
| `1D` | `0.1549` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 16,200.00 USD | 17,930.00 USD | 29,710.00 USD |
| `7D` | `0.1550` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 0.00 USD | 16,530.00 USD | 0.00 USD |
| `1D` | `0.1552` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 8,630.00 USD | 10,490.00 USD | 5,050.00 USD |
| `7D` | `0.1553` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 0.00 USD | 7,730.00 USD | 0.00 USD |
| `1D` | `0.1555` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 34,930.00 USD | 5,680.00 USD | 13,580.00 USD |
| `7D` | `0.1556` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD |
| `1D` | `0.1558` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 6,990.00 USD | 11,690.00 USD | 4,410.00 USD |
| `7D` | `0.1559` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD |
| `1D` | `0.1561` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 12,360.00 USD | 2,970.00 USD | 0.00 USD |
| `7D` | `0.1562` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD |
| `1D` | `0.1564` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 14,590.00 USD | 38,290.00 USD | 9,940.00 USD |
| `7D` | `0.1565` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 70,940.00 USD | 28,480.00 USD | 0.00 USD |
| `1D` | `0.1567` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 87,320.00 USD | 0.00 USD | 22,640.00 USD |
| `7D` | `0.1568` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 111,700.00 USD | 10,060.00 USD | 151,620.00 USD |
| `1D` | `0.1570` | 912,710.00 USD | 0.00 USD | 912,710.00 USD | 27,380.00 USD | 0.00 USD | 105,410.00 USD |
| `7D` | `0.1571` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 194,660.00 USD | 5,100.00 USD | 58,840.00 USD |
| `1D` | `0.1573` | 779,910.00 USD | 0.00 USD | 779,910.00 USD | 49,900.00 USD | 3,460.00 USD | 64,460.00 USD |
| `7D` | `0.1574` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 64,070.00 USD | 79,780.00 USD | 0.00 USD |
| `7D` | `0.1577` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 31,130.00 USD | 112,180.00 USD | 0.00 USD |
| `7D` | `0.1580` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 216,490.00 USD | 41,220.00 USD | 0.00 USD |
| `1D` | `0.1582` | 662,100.00 USD | 0.00 USD | 662,100.00 USD | 49,700.00 USD | 0.00 USD | 6,020.00 USD |
| `7D` | `0.1583` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 70,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1585` | 606,380.00 USD | 0.00 USD | 606,380.00 USD | 52,520.00 USD | 22,800.00 USD | 6,620.00 USD |
| `7D` | `0.1586` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 44,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1588` | 524,440.00 USD | 0.00 USD | 524,440.00 USD | 20,600.00 USD | 31,780.00 USD | 53,020.00 USD |
| `7D` | `0.1589` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 34,830.00 USD | 0.00 USD | 89,310.00 USD |
| `1D` | `0.1591` | 419,050.00 USD | 0.00 USD | 419,050.00 USD | 0.00 USD | 23,850.00 USD | 33,060.00 USD |
| `1D` | `0.1594` | 362,130.00 USD | 0.00 USD | 362,130.00 USD | 0.00 USD | 23,960.00 USD | 4,670.00 USD |
| `7D` | `0.1595` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 0.00 USD | 37,130.00 USD | 0.00 USD |
| `7D` | `0.1598` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 0.00 USD | 86,680.00 USD | 75,810.00 USD |
| `1D` | `0.1600` | 333,500.00 USD | 0.00 USD | 333,500.00 USD | 0.00 USD | 6,180.00 USD | 0.00 USD |
| `7D` | `0.1601` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 0.00 USD | 47,500.00 USD | 0.00 USD |
| `1D` | `0.1603` | 327,320.00 USD | 0.00 USD | 327,320.00 USD | 44,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1604` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 72,300.00 USD | 4,810.00 USD | 273,670.00 USD |
| `7D` | `0.1607` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 166,880.00 USD | 0.00 USD | 312,980.00 USD |
| `1D` | `0.1609` | 282,510.00 USD | 0.00 USD | 282,510.00 USD | 48,780.00 USD | 7,790.00 USD | 82,750.00 USD |
| `7D` | `0.1610` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 178,210.00 USD | 0.00 USD | 178,270.00 USD |
| `1D` | `0.1612` | 143,190.00 USD | 0.00 USD | 143,190.00 USD | 0.00 USD | 23,830.00 USD | 0.00 USD |
| `7D` | `0.1613` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 321,740.00 USD | 0.00 USD | 381,020.00 USD |
| `1D` | `0.1615` | 119,360.00 USD | 0.00 USD | 119,360.00 USD | 0.00 USD | 18,110.00 USD | 0.00 USD |
| `7D` | `0.1616` | 570,480.00 USD | 0.00 USD | 570,480.00 USD | 187,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1622` | 382,890.00 USD | 0.00 USD | 382,890.00 USD | 0.00 USD | 80,360.00 USD | 0.00 USD |
| `1D` | `0.1624` | 101,250.00 USD | 0.00 USD | 101,250.00 USD | 60,520.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1625` | 302,530.00 USD | 0.00 USD | 302,530.00 USD | 0.00 USD | 122,430.00 USD | 103,330.00 USD |
| `1D` | `0.1627` | 40,740.00 USD | 0.00 USD | 40,740.00 USD | 38,240.00 USD | 0.00 USD | 2,490.00 USD |
| `1D` | `0.1628` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1628` | 76,780.00 USD | 0.00 USD | 76,780.00 USD | 76,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1629` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1630` | 167,290.00 USD | 167,290.00 USD | 0.00 USD | 23,880.00 USD | 25,410.00 USD | 118,000.00 USD |
| `7D` | `0.1631` | 70,940.00 USD | 70,940.00 USD | 0.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1633` | 282,120.00 USD | 282,120.00 USD | 0.00 USD | 98,410.00 USD | 7,170.00 USD | 9,250.00 USD |
| `7D` | `0.1634` | 79,030.00 USD | 79,030.00 USD | 0.00 USD | 0.00 USD | 8,090.00 USD | 0.00 USD |
| `1D` | `0.1636` | 329,130.00 USD | 329,130.00 USD | 0.00 USD | 0.00 USD | 23,450.00 USD | 23,560.00 USD |
| `7D` | `0.1637` | 108,170.00 USD | 108,170.00 USD | 0.00 USD | 0.00 USD | 5,580.00 USD | 23,560.00 USD |
| `1D` | `0.1639` | 363,410.00 USD | 363,410.00 USD | 0.00 USD | 14,240.00 USD | 17,110.00 USD | 2,920.00 USD |
| `7D` | `0.1640` | 137,410.00 USD | 137,410.00 USD | 0.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD |
| `1D` | `0.1642` | 450,140.00 USD | 450,140.00 USD | 0.00 USD | 31,400.00 USD | 36,980.00 USD | 18,340.00 USD |
| `7D` | `0.1643` | 207,060.00 USD | 207,060.00 USD | 0.00 USD | 0.00 USD | 25,110.00 USD | 44,540.00 USD |
| `1D` | `0.1645` | 503,750.00 USD | 503,750.00 USD | 0.00 USD | 17,870.00 USD | 24,710.00 USD | 11,040.00 USD |
| `7D` | `0.1646` | 220,850.00 USD | 220,850.00 USD | 0.00 USD | 0.00 USD | 13,780.00 USD | 0.00 USD |
| `1D` | `0.1648` | 532,930.00 USD | 532,930.00 USD | 0.00 USD | 17,270.00 USD | 3,360.00 USD | 8,550.00 USD |
| `7D` | `0.1649` | 232,610.00 USD | 232,610.00 USD | 0.00 USD | 0.00 USD | 11,770.00 USD | 0.00 USD |
| `1D` | `0.1651` | 584,270.00 USD | 584,270.00 USD | 0.00 USD | 32,910.00 USD | 8,040.00 USD | 10,390.00 USD |
| `1D` | `0.1654` | 616,940.00 USD | 616,940.00 USD | 0.00 USD | 3,500.00 USD | 4,350.00 USD | 24,820.00 USD |
| `7D` | `0.1655` | 269,230.00 USD | 269,230.00 USD | 0.00 USD | 0.00 USD | 36,620.00 USD | 0.00 USD |
| `1D` | `0.1657` | 704,980.00 USD | 704,980.00 USD | 0.00 USD | 15,910.00 USD | 63,310.00 USD | 8,820.00 USD |
| `7D` | `0.1658` | 331,780.00 USD | 331,780.00 USD | 0.00 USD | 10,890.00 USD | 0.00 USD | 51,660.00 USD |
| `1D` | `0.1660` | 776,920.00 USD | 776,920.00 USD | 0.00 USD | 8,220.00 USD | 12,910.00 USD | 50,810.00 USD |
| `7D` | `0.1661` | 446,550.00 USD | 446,550.00 USD | 0.00 USD | 103,750.00 USD | 11,020.00 USD | 0.00 USD |
| `1D` | `0.1663` | 902,020.00 USD | 902,020.00 USD | 0.00 USD | 55,130.00 USD | 14,550.00 USD | 55,420.00 USD |
| `7D` | `0.1664` | 702,180.00 USD | 702,180.00 USD | 0.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD |
| `1D` | `0.1666` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 22,170.00 USD | 5,340.00 USD | 78,290.00 USD |
| `7D` | `0.1667` | 757,430.00 USD | 757,430.00 USD | 0.00 USD | 42,580.00 USD | 12,670.00 USD | 0.00 USD |
| `1D` | `0.1669` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 4,600.00 USD | 1,730.00 USD | 7,440.00 USD |
| `7D` | `0.1670` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 114,710.00 USD | 91,060.00 USD | 87,160.00 USD |
| `1D` | `0.1672` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 46,590.00 USD | 3,960.00 USD | 0.00 USD |
| `7D` | `0.1673` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 20,540.00 USD | 23,800.00 USD | 0.00 USD |
| `1D` | `0.1675` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 20,040.00 USD | 1,990.00 USD | 19,670.00 USD |
| `7D` | `0.1676` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 84,020.00 USD | 141,760.00 USD | 0.00 USD |
| `1D` | `0.1678` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 27,610.00 USD | 0.00 USD | 5,390.00 USD |
| `7D` | `0.1679` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 52,340.00 USD | 61,850.00 USD | 35,720.00 USD |
| `1D` | `0.1681` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 94,970.00 USD | 8,580.00 USD | 3,010.00 USD |
| `7D` | `0.1682` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 130,480.00 USD | 18,420.00 USD | 15,310.00 USD |
| `1D` | `0.1684` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 50,170.00 USD | 30,620.00 USD | 37,380.00 USD |
| `7D` | `0.1685` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 14,000.00 USD | 0.00 USD |
| `1D` | `0.1687` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 13,000.00 USD | 9,810.00 USD | 52,820.00 USD |
| `7D` | `0.1688` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD |
| `1D` | `0.1690` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 25,050.00 USD | 12,840.00 USD | 18,700.00 USD |
| `7D` | `0.1691` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 33,660.00 USD | 38,670.00 USD | 71,020.00 USD |
| `1D` | `0.1693` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 87,330.00 USD | 74,940.00 USD | 60,850.00 USD |
| `7D` | `0.1694` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 17,360.00 USD | 62,560.00 USD | 39,780.00 USD |
| `1D` | `0.1696` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 23,530.00 USD | 17,530.00 USD | 16,570.00 USD |
| `7D` | `0.1697` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 56,860.00 USD | 0.00 USD |
| `1D` | `0.1699` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 26,000.00 USD | 57,580.00 USD | 48,960.00 USD |
| `7D` | `0.1700` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD |
| `1D` | `0.1702` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 9,960.00 USD | 0.00 USD | 34,530.00 USD |
| `7D` | `0.1703` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 55,170.00 USD | 46,880.00 USD | 0.00 USD |
| `1D` | `0.1705` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 20,880.00 USD | 20,810.00 USD | 0.00 USD |
| `7D` | `0.1706` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD |
| `1D` | `0.1708` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 46,300.00 USD | 66,430.00 USD | 15,460.00 USD |
| `7D` | `0.1709` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD |
| `1D` | `0.1711` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 5,500.00 USD | 4,910.00 USD | 8,040.00 USD |
| `1D` | `0.1714` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 3,630.00 USD | 12,410.00 USD | 0.00 USD |
| `7D` | `0.1715` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD |
| `1D` | `0.1717` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 11,710.00 USD | 37,270.00 USD | 19,560.00 USD |
| `7D` | `0.1718` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,160.00 USD |
| `1D` | `0.1720` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 47,600.00 USD | 1,590.00 USD | 5,030.00 USD |
| `7D` | `0.1721` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 44,020.00 USD | 0.00 USD | 266,220.00 USD |
| `1D` | `0.1723` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 54,130.00 USD | 17,650.00 USD | 66,630.00 USD |
| `7D` | `0.1724` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 74,040.00 USD | 0.00 USD | 104,030.00 USD |
| `1D` | `0.1726` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 8,230.00 USD | 3,180.00 USD | 12,130.00 USD |
| `1D` | `0.1729` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD |
| `7D` | `0.1730` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 330,670.00 USD | 0.00 USD | 9,420.00 USD |
| `1D` | `0.1732` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD |
| `7D` | `0.1733` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 145,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1735` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 18,250.00 USD | 11,060.00 USD | 1,170.00 USD |
| `1D` | `0.1738` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 15,900.00 USD | 3,450.00 USD | 6,410.00 USD |
| `7D` | `0.1739` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD |
| `1D` | `0.1741` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 4,490.00 USD | 8,360.00 USD |
| `1D` | `0.1744` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 2,460.00 USD | 13,980.00 USD |
| `7D` | `0.1745` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1747` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 3,500.00 USD | 0.00 USD | 31,930.00 USD |
| `7D` | `0.1748` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `0.1750` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 80,070.00 USD | 2,280.00 USD | 22,640.00 USD |
| `7D` | `0.1751` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 226,130.00 USD |
| `1D` | `0.1753` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 34,710.00 USD | 0.00 USD | 26,970.00 USD |
| `7D` | `0.1754` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 37,610.00 USD | 0.00 USD | 229,230.00 USD |
| `1D` | `0.1756` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 23,610.00 USD | 11,970.00 USD | 60,750.00 USD |
| `7D` | `0.1757` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 124,250.00 USD | 38,670.00 USD | 8,600.00 USD |
| `1D` | `0.1759` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 58,360.00 USD | 21,690.00 USD | 21,380.00 USD |
| `7D` | `0.1760` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 224,680.00 USD | 25,210.00 USD | 32,350.00 USD |
| `1D` | `0.1762` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 50,470.00 USD | 68,300.00 USD | 66,600.00 USD |
| `7D` | `0.1763` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 274,260.00 USD | 139,590.00 USD | 12,330.00 USD |
| `1D` | `0.1765` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 15,830.00 USD | 28,990.00 USD | 43,670.00 USD |
| `7D` | `0.1766` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 163,180.00 USD | 200,720.00 USD | 36,540.00 USD |
| `1D` | `0.1768` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 19,860.00 USD | 70,050.00 USD | 52,710.00 USD |
| `7D` | `0.1769` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 113,280.00 USD | 105,160.00 USD | 23,040.00 USD |
| `1D` | `0.1771` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 37,200.00 USD | 12,060.00 USD | 16,920.00 USD |
| `7D` | `0.1772` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 77,840.00 USD | 112,520.00 USD | 21,360.00 USD |
| `1D` | `0.1774` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 12,400.00 USD | 23,730.00 USD | 24,140.00 USD |
| `7D` | `0.1775` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 164,290.00 USD | 30,480.00 USD | 0.00 USD |
| `1D` | `0.1777` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 41,420.00 USD | 74,750.00 USD | 20,580.00 USD |
| `7D` | `0.1778` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 63,990.00 USD | 71,060.00 USD | 123,700.00 USD |
| `1D` | `0.1780` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 7,310.00 USD | 10,310.00 USD | 9,410.00 USD |
| `7D` | `0.1781` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 11,220.00 USD | 4,590.00 USD | 33,810.00 USD |
| `1D` | `0.1783` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 27,640.00 USD | 15,680.00 USD | 18,910.00 USD |
| `7D` | `0.1784` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD |
| `1D` | `0.1786` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 16,960.00 USD | 28,560.00 USD | 7,120.00 USD |
| `7D` | `0.1787` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD |
| `1D` | `0.1789` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 9,350.00 USD | 20,220.00 USD | 5,220.00 USD |
| `7D` | `0.1790` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 103,860.00 USD | 17,360.00 USD | 3,940.00 USD |
| `1D` | `0.1792` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 3,490.00 USD | 7,300.00 USD |
| `7D` | `0.1793` | 6,930,000.00 USD | 6,930,000.00 USD | 0.00 USD | 78,950.00 USD | 42,780.00 USD | 8,910.00 USD |
| `1D` | `0.1795` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 33,150.00 USD | 35,780.00 USD | 18,910.00 USD |
| `7D` | `0.1796` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 17,130.00 USD | 12,930.00 USD | 35,530.00 USD |
| `1D` | `0.1798` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 11,000.00 USD | 17,120.00 USD | 21,440.00 USD |
| `1D` | `0.1799` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 5,820.00 USD | 1,930.00 USD | 0.00 USD |
| `7D` | `0.1799` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 0.00 USD | 11,280.00 USD | 68,230.00 USD |
| `7D` | `0.1802` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 48,220.00 USD | 32,630.00 USD | 23,530.00 USD |
| `7D` | `0.1805` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 11,410.00 USD | 38,130.00 USD | 5,320.00 USD |
| `7D` | `0.1808` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 23,650.00 USD | 52,750.00 USD | 73,440.00 USD |
| `7D` | `0.1811` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 64,990.00 USD | 26,860.00 USD | 13,200.00 USD |
| `7D` | `0.1814` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 28,070.00 USD | 26,510.00 USD | 60,000.00 USD |
| `7D` | `0.1817` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 64,770.00 USD | 10,470.00 USD | 20,080.00 USD |
| `7D` | `0.1820` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 42,210.00 USD | 54,880.00 USD | 38,610.00 USD |
| `7D` | `0.1823` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 62,540.00 USD | 13,300.00 USD | 105,730.00 USD |
| `7D` | `0.1826` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 90,200.00 USD | 9,890.00 USD | 66,950.00 USD |
| `7D` | `0.1829` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 20,880.00 USD | 28,120.00 USD | 51,250.00 USD |
| `7D` | `0.1832` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 94,870.00 USD | 27,790.00 USD | 50,530.00 USD |
| `7D` | `0.1835` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 145,680.00 USD | 46,260.00 USD | 52,650.00 USD |
| `7D` | `0.1838` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 144,340.00 USD | 74,280.00 USD | 106,440.00 USD |
| `7D` | `0.1841` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 56,160.00 USD | 57,660.00 USD | 45,300.00 USD |
| `7D` | `0.1844` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 48,920.00 USD | 3,900.00 USD | 72,920.00 USD |
| `7D` | `0.1847` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 5,770.00 USD | 11,590.00 USD | 20,400.00 USD |
| `7D` | `0.1850` | 9,600,000.00 USD | 9,600,000.00 USD | 0.00 USD | 77,110.00 USD | 77,020.00 USD | 103,160.00 USD |
| `7D` | `0.1853` | 9,820,000.00 USD | 9,820,000.00 USD | 0.00 USD | 62,090.00 USD | 9,590.00 USD | 146,560.00 USD |
| `7D` | `0.1856` | 9,960,000.00 USD | 9,960,000.00 USD | 0.00 USD | 31,410.00 USD | 21,030.00 USD | 87,320.00 USD |
| `7D` | `0.1859` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 47,740.00 USD | 6,920.00 USD | 77,460.00 USD |
| `7D` | `0.1862` | 10,200,000.00 USD | 10,200,000.00 USD | 0.00 USD | 60,020.00 USD | 13,950.00 USD | 37,650.00 USD |
| `7D` | `0.1865` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 22,320.00 USD | 18,650.00 USD | 40,190.00 USD |
| `7D` | `0.1868` | 10,430,000.00 USD | 10,430,000.00 USD | 0.00 USD | 88,110.00 USD | 31,750.00 USD | 24,730.00 USD |
| `7D` | `0.1871` | 10,590,000.00 USD | 10,590,000.00 USD | 0.00 USD | 100,950.00 USD | 27,560.00 USD | 34,980.00 USD |
| `7D` | `0.1874` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 71,850.00 USD | 48,780.00 USD | 51,010.00 USD |
| `7D` | `0.1877` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 27,840.00 USD | 22,370.00 USD | 17,920.00 USD |
| `7D` | `0.1880` | 10,890,000.00 USD | 10,890,000.00 USD | 0.00 USD | 36,800.00 USD | 14,700.00 USD | 8,130.00 USD |
| `7D` | `0.1883` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 14,000.00 USD | 3,530.00 USD | 9,740.00 USD |
| `7D` | `0.1886` | 10,960,000.00 USD | 10,960,000.00 USD | 0.00 USD | 9,250.00 USD | 31,900.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `188.57M` | Total OI Tokens: `1,162,954,231.8 ARB`
  * 1h OI Change: `+2.54%` | 4h OI Change: `+5.55%` | 24h OI Change: `-14.07%`
  * Exchange Breakdown: Binance=`42.38M` | Bybit=`26.28M` | OKX=`14.43M` | Hyperliquid=`13.06M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.82K` | Last 24h: `-1.51K` | Last 3d: `12.63K` | Last 7d: `45.15K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0019%` | **USDT OKX** | `-0.0023%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0022%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0099%` | **USDT Bitget** | `-0.0107%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `47.80%` | `52.20%` | `0.92` | 1,000,000.00 USD |
| `15M` | `Binance` | `46%` | `54%` | `0.85` | 355,740.00 USD |
| `15M` | `OKX` | `43.23%` | `56.77%` | `0.76` | 85,640.00 USD |
| `15M` | `Bybit` | `57%` | `43%` | `1.33` | 108,630.00 USD |
| `15M` | `KuCoin` | `49.75%` | `50.25%` | `0.99` | 150,000.00 USD |
| `15M` | `Gate` | `50.15%` | `49.85%` | `1.01` | 22,330.00 USD |
| `15M` | `Bitget` | `45.58%` | `54.42%` | `0.84` | 7,700.00 USD |
| `15M` | `BingX` | `57.16%` | `42.84%` | `1.33` | 116,640.00 USD |
| `15M` | `MEXC` | `37.31%` | `62.69%` | `0.60` | 57,860.00 USD |
| `15M` | `Bitunix` | `49.69%` | `50.31%` | `0.99` | 10,950.00 USD |
| `15M` | `Hyperliquid` | `85.29%` | `14.71%` | `5.80` | 2,910.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.59%` | `50.41%` | `0.98` | 52,030.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `29.55%` | `70.45%` | `0.42` | 12,700.00 USD |
| `15M` | `HTX` | `42.7%` | `57.3%` | `0.75` | 165.14 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `10.24%` | `89.76%` | `0.11` | 20,250.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `15.55%` | `84.45%` | `0.18` | 215.52 USD |
| `15M` | `Whale Positions` | `46%` | `54%` | `0.85` | 355,740.00 USD |
| `15M` | `Global Accounts` | `47.80%` | `52.20%` | `0.92` | 1,000,000.00 USD |
| `1H` | `ARB` | `47.48%` | `52.52%` | `0.90` | 4,570,000.00 USD |
| `1H` | `Binance` | `51.38%` | `48.62%` | `1.06` | 1,440,000.00 USD |
| `1H` | `OKX` | `49.65%` | `50.35%` | `0.99` | 443,710.00 USD |
| `1H` | `Bybit` | `46.31%` | `53.69%` | `0.86` | 514,530.00 USD |
| `1H` | `KuCoin` | `49.9%` | `50.1%` | `1.00` | 461,460.00 USD |
| `1H` | `Gate` | `40.6%` | `59.4%` | `0.68` | 107,870.00 USD |
| `1H` | `Bitget` | `40.82%` | `59.18%` | `0.69` | 459,220.00 USD |
| `1H` | `BingX` | `40.75%` | `59.25%` | `0.69` | 535,280.00 USD |
| `1H` | `MEXC` | `53.77%` | `46.23%` | `1.16` | 228,590.00 USD |
| `1H` | `Bitunix` | `38.57%` | `61.43%` | `0.63` | 61,370.00 USD |
| `1H` | `Hyperliquid` | `83.6%` | `16.4%` | `5.10` | 62,200.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.23%` | `49.77%` | `1.01` | 158,110.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `16.81%` | `83.19%` | `0.20` | 60,620.00 USD |
| `1H` | `HTX` | `30.28%` | `69.72%` | `0.43` | 2,330.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `11.04%` | `88.96%` | `0.12` | 30,530.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `5.86%` | `94.14%` | `0.06` | 6,180.00 USD |
| `1H` | `Whale Positions` | `51.38%` | `48.62%` | `1.06` | 1,440,000.00 USD |
| `1H` | `Global Accounts` | `47.48%` | `52.52%` | `0.90` | 4,570,000.00 USD |
| `4H` | `ARB` | `48.90%` | `51.10%` | `0.96` | 60,140,000.00 USD |
| `4H` | `Binance` | `45.76%` | `54.24%` | `0.84` | 20,040,000.00 USD |
| `4H` | `OKX` | `49.87%` | `50.13%` | `0.99` | 8,140,000.00 USD |
| `4H` | `Bybit` | `53.52%` | `46.48%` | `1.15` | 5,030,000.00 USD |
| `4H` | `KuCoin` | `46.86%` | `53.14%` | `0.88` | 493,820.00 USD |
| `4H` | `Gate` | `47.57%` | `52.43%` | `0.91` | 4,770,000.00 USD |
| `4H` | `Bitget` | `54.17%` | `45.83%` | `1.18` | 1,920,000.00 USD |
| `4H` | `BingX` | `41.5%` | `58.5%` | `0.71` | 9,810,000.00 USD |
| `4H` | `MEXC` | `52.23%` | `47.77%` | `1.09` | 2,740,000.00 USD |
| `4H` | `Bitunix` | `56.15%` | `43.85%` | `1.28` | 1,820,000.00 USD |
| `4H` | `Hyperliquid` | `44.18%` | `55.82%` | `0.79` | 1,480,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.33%` | `49.67%` | `1.01` | 1,810,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `96.3%` | `3.7%` | `26.03` | 1,680,000.00 USD |
| `4H` | `HTX` | `55.27%` | `44.73%` | `1.24` | 134,400.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `56.86%` | `43.14%` | `1.32` | 67,860.00 USD |
| `4H` | `Aster` | `63.73%` | `36.27%` | `1.76` | 148,440.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `69.15%` | `30.85%` | `2.24` | 23,920.00 USD |
| `4H` | `Whale Positions` | `45.76%` | `54.24%` | `0.84` | 20,040,000.00 USD |
| `4H` | `Global Accounts` | `48.90%` | `51.10%` | `0.96` | 60,140,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1552` | `0.1554` | `0.1552` | `0.1563` | `0.1546` | 1,015,146.23 USD | 599,871.34 USD | 415,274.89 USD | 184,596.46 USD | `+18.18%` | `40B / 13S` |
| `0:00 UTC` | `0.1560` | `0.1561` | `0.1560` | `0.1563` | `0.1557` | 778,824.29 USD | 403,907.68 USD | 374,916.61 USD | 28,991.07 USD | `+3.72%` | `13B / 12S` |
| `5:00 UTC` | `0.1560` | `0.1557` | `0.1560` | `0.1561` | `0.1552` | 724,500.45 USD | 382,680.28 USD | 341,820.18 USD | 40,860.10 USD | `+5.64%` | `10B / 13S` |
| `0:00 UTC` | `0.1560` | `0.1561` | `0.1560` | `0.1567` | `0.1555` | 659,096.24 USD | 362,345.04 USD | 296,751.20 USD | 65,593.84 USD | `+9.95%` | `17B / 13S` |
| `5:00 UTC` | `0.1568` | `0.1562` | `0.1568` | `0.1570` | `0.1554` | 510,482.89 USD | 331,670.18 USD | 178,812.71 USD | 152,857.47 USD | `+29.94%` | `56B / 25S` |
| `0:00 UTC` | `0.1575` | `0.1578` | `0.1575` | `0.1585` | `0.1566` | 1,225,850.60 USD | 572,636.93 USD | 653,213.67 USD | -80,576.74 USD | `-6.57%` | `41B / 29S` |
| `5:00 UTC` | `0.1581` | `0.1581` | `0.1581` | `0.1585` | `0.1579` | 820,818.50 USD | 467,570.37 USD | 353,248.12 USD | 114,322.25 USD | `+13.93%` | `9B / 5S` |
| `0:00 UTC` | `0.1580` | `0.1582` | `0.1580` | `0.1590` | `0.1577` | 855,410.94 USD | 513,960.14 USD | 341,450.80 USD | 172,509.34 USD | `+20.17%` | `35B / 24S` |
| `5:00 UTC` | `0.1601` | `0.1598` | `0.1601` | `0.1608` | `0.1587` | 1,430,991.81 USD | 878,187.62 USD | 552,804.19 USD | 325,383.42 USD | `+22.74%` | `24B / 14S` |
| `0:00 UTC` | `0.1620` | `0.1617` | `0.1620` | `0.1625` | `0.1603` | 1,437,040.31 USD | 684,580.38 USD | 752,459.93 USD | -67,879.56 USD | `-4.72%` | `13B / 11S` |

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
| `5m` | -19,110.00 USD | -223,860.00 USD | **`DISTRIBUTION`** |
| `15m` | -5,410.00 USD | -208,240.00 USD | **`DISTRIBUTION`** |
| `30m` | 100,590.00 USD | 433,690.00 USD | **`ACCUMULATION`** |
| `1h` | 29,820.00 USD | 744,070.00 USD | **`ACCUMULATION`** |
| `2h` | -20,630.00 USD | 1,370,000.00 USD | **`ACCUMULATION`** |
| `4h` | 107,010.00 USD | 2,720,000.00 USD | **`ACCUMULATION`** |
| `6h` | -256,340.00 USD | 1,720,000.00 USD | **`ACCUMULATION`** |
| `8h` | -745,290.00 USD | -3,320,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,010,000.00 USD | -4,920,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,060,000.00 USD | -8,090,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,450,000.00 USD | -35,140,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,590,000.00 USD | -161,410,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-19.11K` | 15m=`-5.41K` | 1h=`+29.82K` | 24h=`-2.06M`
* Futures Capital Netflows: 5m=`-223.86K` | 15m=`-208.24K` | 1h=`+744.07K` | 24h=`-8.09M`
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
  * `2026-10-30 09:50:55 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:09:55 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:09:55 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:09:55 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:08:55 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:08:55 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:55 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:10:55 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
