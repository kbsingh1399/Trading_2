# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 00:32:19 IST` (`2026-10-29 19:02:19 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1678` | `0.1686` | `0.1674` | `0.1685` | `1,072,219` | 180,112.23 USD | 64,358.66 USD | `+35.73%` | -4,678,878.21 USD | `+0.78` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.1685` | `0.1688` | `0.1680` | `0.1684` | `1,229,900` | 207,132.41 USD | -2,312.69 USD | `-1.12%` | -4,681,190.90 USD | `+0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `0.1684` | `0.1691` | `0.1684` | `0.1689` | `1,116,638` | 188,495.83 USD | 11,669.35 USD | `+6.19%` | -4,669,521.55 USD | `+0.19` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1695` | `0.1698` | `0.1685` | `0.1687` | `3,437,206` | 581,095.74 USD | -8,644.20 USD | `-1.49%` | -4,653,480.63 USD | `+0.70` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1687` | `0.1689` | `0.1673` | `0.1685` | `6,716,601` | 1,127,023.46 USD | 19,707.75 USD | `+1.75%` | -4,633,772.88 USD | `+0.86` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1685` | `0.1691` | `0.1680` | `0.1689` | `2,346,538` | 395,628.24 USD | 9,356.66 USD | `+2.37%` | -4,624,416.22 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1745` | `0.1759` | `0.1714` | `0.1724` | `28,115,276` | 4,875,921.02 USD | -1,037,219.52 USD | `-21.27%` | -4,109,099.99 USD | `-2.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1724` | `0.1727` | `0.1681` | `0.1696` | `26,281,427` | 4,477,475.52 USD | -441,479.21 USD | `-9.86%` | -4,550,579.20 USD | `-0.59` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1696` | `0.1704` | `0.1673` | `0.1689` | `18,125,790` | 3,058,386.95 USD | -71,394.73 USD | `-2.33%` | -4,621,973.94 USD | `+0.30` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,634,787.89 USD | `-0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,872,916.24 USD | `-1.36` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1689` | `72,499,824` | 12,407,954.23 USD | -1,553,355.19 USD | `-12.52%` | -4,426,271.43 USD | `-1.42` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1721` | `0.1729` | `0.1635` | `0.1652` | `91,809,989` | 15,344,891.97 USD | 203,909.29 USD | `+1.33%` | -294,464.16 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1652` | `0.1687` | `0.1623` | `0.1631` | `68,085,678` | 11,252,816.65 USD | -909,329.92 USD | `-8.08%` | -1,203,794.08 USD | `-1.11` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,634,787.89 USD | `-0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,872,916.24 USD | `-1.36` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1689` | `72,499,824` | 12,407,954.23 USD | -1,553,355.19 USD | `-12.52%` | -4,426,271.43 USD | `-1.42` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:25:14 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+5.81%`) | Long MP=`0.1598` (Vol: 141,700.00 USD, Dist: `--5.23%`)
  * 48H Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+5.81%`) | Long MP=`0.1598` (Vol: 154,300.00 USD, Dist: `--5.23%`)
  * 3D Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+5.81%`) | Long MP=`0.1598` (Vol: 205,900.00 USD, Dist: `--5.23%`)
  * 7D Horizon: Short MP=`0.1834` (Vol: 181,500.00 USD, Dist: `+8.74%`) | Long MP=`0.1616` (Vol: 292,500.00 USD, Dist: `--4.15%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0365` | 8,790.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0385` | 4,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 408.10 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 170.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0435` | 125.08 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0455` | 4,630.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 400.94 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 6,350.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 289.43 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0535` | 1,670.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 2,270.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 15,650.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 141.13 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 252.94 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 988.03 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 170,670.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 591.90 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 5,010.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 2,970.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 8,250.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 4,010.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,440.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 226.17 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 16,420.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 27,120.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 1,520.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 4,630.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 13,780.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 13,840.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 112.78 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 41,430.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 611.76 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 7,650.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 362.62 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 116.06 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 683.50 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 2,040.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 814.24 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 42,840.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 477.50 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 874.69 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 145.24 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 5,970.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 8,410.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 1,850.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 811.82 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 802.14 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 24,500.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 6,860.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 181.20 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 1,060.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 342.59 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 534.49 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 425.50 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1125` | 107.92 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 3,570.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 20,830.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 5,440.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 13,260.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 1,560.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 25,940.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 15,480.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 4,790.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 406.25 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 8,920.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 33,070.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 1,040.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 4,850.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 1,200.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 6,310.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 9,900.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 7,140.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 15,040.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 10,500.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 6,620.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 23,230.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 2,970.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1365` | 19,420.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1375` | 1,090.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1385` | 4,400.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1395` | 69,250.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 8,420.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 11,550.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 496,690.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 19,330.00 USD | 891,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 53,790.00 USD | 871,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 3,880.00 USD | 817,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 193,660.00 USD | 814,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1468` | 10,660,000.00 USD | 10,660,000.00 USD | 9,720.00 USD | 9,180.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1471` | 10,630,000.00 USD | 10,630,000.00 USD | 6,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1474` | 10,630,000.00 USD | 10,630,000.00 USD | 6,490.00 USD | 9,220.00 USD | 5,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 73,750.00 USD | 620,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1477` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 25,460.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1480` | 10,580,000.00 USD | 10,580,000.00 USD | 6,990.00 USD | 29,300.00 USD | 20,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1483` | 10,520,000.00 USD | 10,520,000.00 USD | 42,230.00 USD | 16,640.00 USD | 33,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,890.00 USD | 546,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1486` | 10,430,000.00 USD | 10,430,000.00 USD | 18,610.00 USD | 10,470.00 USD | 25,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1489` | 10,370,000.00 USD | 10,370,000.00 USD | 11,170.00 USD | 3,710.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1492` | 10,350,000.00 USD | 10,350,000.00 USD | 40,320.00 USD | 17,880.00 USD | 27,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1495` | 10,260,000.00 USD | 10,260,000.00 USD | 34,650.00 USD | 18,690.00 USD | 12,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 35,380.00 USD | 543,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1498` | 10,200,000.00 USD | 10,200,000.00 USD | 42,100.00 USD | 9,610.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1501` | 10,130,000.00 USD | 10,130,000.00 USD | 21,010.00 USD | 7,930.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1503` | 4,310,000.00 USD | 4,310,000.00 USD | 3,610.00 USD | 2,640.00 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1504` | 10,090,000.00 USD | 10,090,000.00 USD | 17,800.00 USD | 11,590.00 USD | 44,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1505` | 102,290.00 USD | 508,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1506` | 4,300,000.00 USD | 4,300,000.00 USD | 5,430.00 USD | 0.00 USD | 7,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1507` | 10,010,000.00 USD | 10,010,000.00 USD | 28,940.00 USD | 12,910.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1509` | 4,290,000.00 USD | 4,290,000.00 USD | 5,640.00 USD | 3,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1510` | 9,940,000.00 USD | 9,940,000.00 USD | 12,660.00 USD | 12,930.00 USD | 29,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1512` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 4,360.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1513` | 9,890,000.00 USD | 9,890,000.00 USD | 32,900.00 USD | 17,610.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1515` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 1,730.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 4,180.00 USD | 406,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1516` | 9,800,000.00 USD | 9,800,000.00 USD | 54,550.00 USD | 0.00 USD | 43,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1518` | 4,270,000.00 USD | 4,270,000.00 USD | 11,550.00 USD | 4,320.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1519` | 9,700,000.00 USD | 9,700,000.00 USD | 37,430.00 USD | 19,520.00 USD | 70,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1521` | 4,250,000.00 USD | 4,250,000.00 USD | 9,450.00 USD | 1,470.00 USD | 9,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1522` | 9,570,000.00 USD | 9,570,000.00 USD | 49,800.00 USD | 9,640.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1524` | 4,230,000.00 USD | 4,230,000.00 USD | 1,870.00 USD | 2,970.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1525` | 9,490,000.00 USD | 9,490,000.00 USD | 25,790.00 USD | 13,700.00 USD | 19,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1525` | 45,320.00 USD | 401,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1527` | 4,220,000.00 USD | 4,220,000.00 USD | 3,300.00 USD | 0.00 USD | 11,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1528` | 9,430,000.00 USD | 9,430,000.00 USD | 75,690.00 USD | 27,110.00 USD | 27,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1530` | 4,200,000.00 USD | 4,200,000.00 USD | 4,960.00 USD | 5,040.00 USD | 8,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1531` | 9,300,000.00 USD | 9,300,000.00 USD | 35,030.00 USD | 8,400.00 USD | 16,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1533` | 4,180,000.00 USD | 4,180,000.00 USD | 14,310.00 USD | 1,900.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1534` | 9,240,000.00 USD | 9,240,000.00 USD | 15,780.00 USD | 17,430.00 USD | 20,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 19,400.00 USD | 356,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1536` | 4,170,000.00 USD | 4,170,000.00 USD | 4,320.00 USD | 5,590.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1537` | 9,180,000.00 USD | 9,180,000.00 USD | 37,050.00 USD | 11,700.00 USD | 10,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1539` | 4,150,000.00 USD | 4,150,000.00 USD | 2,920.00 USD | 6,640.00 USD | 1,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1540` | 9,120,000.00 USD | 9,120,000.00 USD | 14,000.00 USD | 6,530.00 USD | 5,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1542` | 4,140,000.00 USD | 4,140,000.00 USD | 1,710.00 USD | 0.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1543` | 9,100,000.00 USD | 9,100,000.00 USD | 9,250.00 USD | 3,590.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1545` | 4,140,000.00 USD | 4,140,000.00 USD | 13,270.00 USD | 5,370.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1545` | 26,170.00 USD | 337,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1546` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 0.00 USD | 5,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1548` | 4,110,000.00 USD | 4,110,000.00 USD | 1,140.00 USD | 8,660.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1549` | 9,080,000.00 USD | 9,080,000.00 USD | 11,570.00 USD | 6,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1551` | 4,100,000.00 USD | 4,100,000.00 USD | 4,810.00 USD | 4,140.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1552` | 9,060,000.00 USD | 9,060,000.00 USD | 23,110.00 USD | 7,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1554` | 4,090,000.00 USD | 4,090,000.00 USD | 18,660.00 USD | 19,270.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1555` | 9,030,000.00 USD | 9,030,000.00 USD | 0.00 USD | 0.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1555` | 40,060.00 USD | 311,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1557` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 3,410.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1558` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 10,990.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1560` | 4,040,000.00 USD | 4,040,000.00 USD | 5,460.00 USD | 11,300.00 USD | 7,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1561` | 9,000,000.00 USD | 9,000,000.00 USD | 0.00 USD | 5,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1563` | 4,010,000.00 USD | 4,010,000.00 USD | 3,050.00 USD | 1,050.00 USD | 20,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1564` | 8,990,000.00 USD | 8,990,000.00 USD | 24,300.00 USD | 28,690.00 USD | 21,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1565` | 21,460.00 USD | 271,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1566` | 3,990,000.00 USD | 3,990,000.00 USD | 45,560.00 USD | 11,570.00 USD | 15,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1567` | 8,920,000.00 USD | 8,920,000.00 USD | 41,770.00 USD | 15,360.00 USD | 15,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1569` | 3,920,000.00 USD | 3,920,000.00 USD | 24,600.00 USD | 31,270.00 USD | 7,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1570` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 5,100.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1572` | 3,850,000.00 USD | 3,850,000.00 USD | 34,670.00 USD | 14,240.00 USD | 17,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1573` | 8,830,000.00 USD | 8,830,000.00 USD | 58,830.00 USD | 56,100.00 USD | 25,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1575` | 3,790,000.00 USD | 3,790,000.00 USD | 34,430.00 USD | 19,170.00 USD | 6,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1575` | 4,940.00 USD | 249,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1576` | 8,690,000.00 USD | 8,690,000.00 USD | 26,600.00 USD | 102,190.00 USD | 54,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1578` | 3,730,000.00 USD | 3,730,000.00 USD | 62,820.00 USD | 64,050.00 USD | 24,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1579` | 8,500,000.00 USD | 8,500,000.00 USD | 101,500.00 USD | 95,190.00 USD | 42,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1581` | 3,570,000.00 USD | 3,570,000.00 USD | 31,970.00 USD | 3,940.00 USD | 22,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1582` | 8,260,000.00 USD | 8,260,000.00 USD | 56,130.00 USD | 13,480.00 USD | 89,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1584` | 3,520,000.00 USD | 3,520,000.00 USD | 34,630.00 USD | 11,050.00 USD | 13,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1585` | 8,110,000.00 USD | 8,110,000.00 USD | 87,110.00 USD | 50,340.00 USD | 75,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1585` | 2,660.00 USD | 244,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1587` | 3,460,000.00 USD | 3,460,000.00 USD | 6,650.00 USD | 21,380.00 USD | 12,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1588` | 7,890,000.00 USD | 7,890,000.00 USD | 34,830.00 USD | 30,030.00 USD | 41,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1590` | 3,410,000.00 USD | 3,410,000.00 USD | 13,490.00 USD | 27,950.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1591` | 7,790,000.00 USD | 7,790,000.00 USD | 110,640.00 USD | 49,670.00 USD | 60,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1593` | 3,370,000.00 USD | 3,370,000.00 USD | 47,380.00 USD | 6,320.00 USD | 23,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1594` | 7,570,000.00 USD | 7,570,000.00 USD | 85,560.00 USD | 39,260.00 USD | 102,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1595` | 66,110.00 USD | 241,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1596` | 3,290,000.00 USD | 3,290,000.00 USD | 29,470.00 USD | 19,190.00 USD | 35,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1597` | 7,340,000.00 USD | 7,340,000.00 USD | 228,850.00 USD | 96,110.00 USD | 102,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1599` | 3,200,000.00 USD | 3,200,000.00 USD | 69,610.00 USD | 16,990.00 USD | 33,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1600` | 6,910,000.00 USD | 6,910,000.00 USD | 105,580.00 USD | 38,830.00 USD | 76,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1602` | 3,080,000.00 USD | 3,080,000.00 USD | 55,540.00 USD | 46,820.00 USD | 7,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1603` | 6,690,000.00 USD | 6,690,000.00 USD | 62,240.00 USD | 54,840.00 USD | 81,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1605` | 2,970,000.00 USD | 2,970,000.00 USD | 34,500.00 USD | 18,980.00 USD | 37,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1605` | 20,460.00 USD | 175,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1606` | 6,490,000.00 USD | 6,490,000.00 USD | 211,140.00 USD | 149,480.00 USD | 227,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1608` | 2,880,000.00 USD | 2,880,000.00 USD | 66,600.00 USD | 34,180.00 USD | 21,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1609` | 5,900,000.00 USD | 5,900,000.00 USD | 92,990.00 USD | 229,060.00 USD | 182,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1611` | 2,760,000.00 USD | 2,760,000.00 USD | 132,780.00 USD | 132,510.00 USD | 51,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1612` | 5,400,000.00 USD | 5,400,000.00 USD | 281,220.00 USD | 247,430.00 USD | 159,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1614` | 2,440,000.00 USD | 2,440,000.00 USD | 55,510.00 USD | 25,790.00 USD | 53,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1615` | 4,710,000.00 USD | 4,710,000.00 USD | 293,210.00 USD | 107,900.00 USD | 374,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1615` | 17,950.00 USD | 155,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1617` | 2,310,000.00 USD | 2,310,000.00 USD | 73,170.00 USD | 27,450.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1618` | 3,930,000.00 USD | 3,930,000.00 USD | 310,070.00 USD | 132,060.00 USD | 310,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1620` | 2,180,000.00 USD | 2,180,000.00 USD | 57,510.00 USD | 54,730.00 USD | 62,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1621` | 3,180,000.00 USD | 3,180,000.00 USD | 228,220.00 USD | 148,260.00 USD | 314,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1623` | 2,010,000.00 USD | 2,010,000.00 USD | 53,880.00 USD | 67,020.00 USD | 26,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1624` | 2,490,000.00 USD | 2,490,000.00 USD | 375,170.00 USD | 135,840.00 USD | 119,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1625` | 98,470.00 USD | 137,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1626` | 1,860,000.00 USD | 1,860,000.00 USD | 19,820.00 USD | 12,640.00 USD | 27,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1627` | 1,860,000.00 USD | 1,860,000.00 USD | 291,760.00 USD | 0.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1629` | 1,800,000.00 USD | 1,800,000.00 USD | 14,220.00 USD | 33,030.00 USD | 19,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1630` | 1,560,000.00 USD | 1,560,000.00 USD | 9,210.00 USD | 0.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1632` | 1,740,000.00 USD | 1,740,000.00 USD | 12,400.00 USD | 19,630.00 USD | 17,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1635` | 1,690,000.00 USD | 1,690,000.00 USD | 37,200.00 USD | 6,390.00 USD | 11,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1635` | 5,930.00 USD | 38,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1636` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 13,670.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1638` | 1,630,000.00 USD | 1,630,000.00 USD | 9,410.00 USD | 22,520.00 USD | 42,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1639` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 62,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1641` | 1,560,000.00 USD | 1,560,000.00 USD | 7,360.00 USD | 6,090.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1642` | 1,440,000.00 USD | 1,440,000.00 USD | 22,480.00 USD | 29,240.00 USD | 26,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1644` | 1,530,000.00 USD | 1,530,000.00 USD | 25,590.00 USD | 25,250.00 USD | 32,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1645` | 1,360,000.00 USD | 1,360,000.00 USD | 34,760.00 USD | 8,990.00 USD | 7,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1645` | 14,520.00 USD | 33,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1647` | 1,450,000.00 USD | 1,450,000.00 USD | 40,030.00 USD | 36,560.00 USD | 24,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1648` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1650` | 1,350,000.00 USD | 1,350,000.00 USD | 12,400.00 USD | 24,600.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1651` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 51,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1653` | 1,310,000.00 USD | 1,310,000.00 USD | 57,990.00 USD | 16,860.00 USD | 34,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1654` | 1,250,000.00 USD | 1,250,000.00 USD | 33,810.00 USD | 31,800.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1655` | 12,410.00 USD | 18,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1656` | 1,200,000.00 USD | 1,200,000.00 USD | 46,590.00 USD | 51,020.00 USD | 52,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1657` | 1,170,000.00 USD | 1,170,000.00 USD | 10,890.00 USD | 0.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1659` | 1,050,000.00 USD | 1,050,000.00 USD | 43,890.00 USD | 19,240.00 USD | 62,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1660` | 1,140,000.00 USD | 1,140,000.00 USD | 29,890.00 USD | 11,020.00 USD | 33,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1662` | 920,750.00 USD | 920,750.00 USD | 28,530.00 USD | 18,480.00 USD | 64,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1663` | 1,070,000.00 USD | 1,070,000.00 USD | 86,050.00 USD | 51,000.00 USD | 75,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1665` | 809,060.00 USD | 809,060.00 USD | 64,660.00 USD | 59,180.00 USD | 67,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1666` | 856,340.00 USD | 856,340.00 USD | 49,590.00 USD | 32,780.00 USD | 28,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1668` | 618,140.00 USD | 618,140.00 USD | 111,120.00 USD | 67,630.00 USD | 37,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1669` | 745,150.00 USD | 745,150.00 USD | 11,410.00 USD | 64,050.00 USD | 42,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1671` | 401,620.00 USD | 401,620.00 USD | 46,140.00 USD | 21,810.00 USD | 24,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1672` | 626,980.00 USD | 626,980.00 USD | 70,540.00 USD | 38,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1674` | 309,600.00 USD | 309,600.00 USD | 21,310.00 USD | 31,130.00 USD | 16,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1675` | 518,370.00 USD | 518,370.00 USD | 64,490.00 USD | 105,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1675` | 6,100.00 USD | 6,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1677` | 240,820.00 USD | 240,820.00 USD | 14,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1678` | 347,970.00 USD | 347,970.00 USD | 71,860.00 USD | 79,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1680` | 226,200.00 USD | 226,200.00 USD | 75,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1681` | 196,180.00 USD | 196,180.00 USD | 69,520.00 USD | 36,390.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1683` | 150,780.00 USD | 150,780.00 USD | 88,790.00 USD | 3,200.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1684` | 74,950.00 USD | 74,950.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1686` | 29,870.00 USD | 29,870.00 USD | 0.00 USD | 23,410.00 USD | 6,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1689` | 15,550.00 USD | 15,550.00 USD | 0.00 USD | 6,980.00 USD | 8,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1690` | 38,670.00 USD | 38,670.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1692` | 137,030.00 USD | 137,030.00 USD | 55,320.00 USD | 66,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1693` | 92,520.00 USD | 92,520.00 USD | 21,780.00 USD | 32,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1695` | 159,330.00 USD | 159,330.00 USD | 0.00 USD | 22,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1696` | 207,880.00 USD | 207,880.00 USD | 0.00 USD | 87,350.00 USD | 28,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1698` | 223,470.00 USD | 223,470.00 USD | 7,460.00 USD | 56,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1699` | 252,030.00 USD | 252,030.00 USD | 0.00 USD | 25,330.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1702` | 321,740.00 USD | 321,740.00 USD | 22,820.00 USD | 46,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1704` | 248,130.00 USD | 248,130.00 USD | 0.00 USD | 14,420.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1707` | 358,900.00 USD | 358,900.00 USD | 37,960.00 USD | 68,660.00 USD | 4,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1708` | 411,920.00 USD | 411,920.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1710` | 364,230.00 USD | 364,230.00 USD | 0.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1713` | 379,270.00 USD | 379,270.00 USD | 0.00 USD | 15,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1714` | 453,940.00 USD | 453,940.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1716` | 404,880.00 USD | 404,880.00 USD | 0.00 USD | 25,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1719` | 436,620.00 USD | 436,620.00 USD | 23,230.00 USD | 8,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1720` | 608,300.00 USD | 608,300.00 USD | 0.00 USD | 0.00 USD | 154,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1722` | 553,600.00 USD | 553,600.00 USD | 80,460.00 USD | 16,860.00 USD | 19,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1723` | 853,960.00 USD | 853,960.00 USD | 74,150.00 USD | 0.00 USD | 171,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1725` | 569,490.00 USD | 569,490.00 USD | 0.00 USD | 0.00 USD | 15,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1728` | 588,300.00 USD | 588,300.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1729` | 991,550.00 USD | 991,550.00 USD | 137,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1732` | 1,330,000.00 USD | 1,330,000.00 USD | 338,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1734` | 598,370.00 USD | 598,370.00 USD | 0.00 USD | 0.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1735` | 6,900.00 USD | 6,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1737` | 637,430.00 USD | 637,430.00 USD | 29,560.00 USD | 9,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1738` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 83,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1740` | 647,070.00 USD | 647,070.00 USD | 0.00 USD | 0.00 USD | 9,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1743` | 659,700.00 USD | 659,700.00 USD | 0.00 USD | 0.00 USD | 12,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1744` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1746` | 680,190.00 USD | 680,190.00 USD | 8,530.00 USD | 2,460.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1749` | 798,890.00 USD | 798,890.00 USD | 80,070.00 USD | 2,280.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1750` | 1,660,000.00 USD | 1,660,000.00 USD | 69,520.00 USD | 0.00 USD | 167,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1752` | 851,510.00 USD | 851,510.00 USD | 19,990.00 USD | 0.00 USD | 32,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1753` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 191,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1755` | 904,990.00 USD | 904,990.00 USD | 14,290.00 USD | 16,650.00 USD | 22,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1756` | 2,030,000.00 USD | 2,030,000.00 USD | 75,620.00 USD | 0.00 USD | 97,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1758` | 1,060,000.00 USD | 1,060,000.00 USD | 77,350.00 USD | 31,940.00 USD | 45,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1759` | 2,290,000.00 USD | 2,290,000.00 USD | 217,800.00 USD | 38,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1761` | 1,250,000.00 USD | 1,250,000.00 USD | 53,970.00 USD | 88,390.00 USD | 50,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1762` | 2,800,000.00 USD | 2,800,000.00 USD | 289,660.00 USD | 196,430.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1764` | 1,410,000.00 USD | 1,410,000.00 USD | 72,600.00 USD | 25,840.00 USD | 61,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1765` | 3,180,000.00 USD | 3,180,000.00 USD | 154,540.00 USD | 175,970.00 USD | 48,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1765` | 339.06 USD | 7,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1767` | 1,560,000.00 USD | 1,560,000.00 USD | 39,860.00 USD | 52,820.00 USD | 52,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1768` | 3,510,000.00 USD | 3,510,000.00 USD | 161,560.00 USD | 138,440.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1770` | 1,680,000.00 USD | 1,680,000.00 USD | 36,140.00 USD | 47,810.00 USD | 38,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1771` | 3,740,000.00 USD | 3,740,000.00 USD | 69,030.00 USD | 138,810.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1773` | 1,760,000.00 USD | 1,760,000.00 USD | 30,810.00 USD | 28,980.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1774` | 4,000,000.00 USD | 4,000,000.00 USD | 148,780.00 USD | 115,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1775` | 151.67 USD | 7,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1776` | 1,890,000.00 USD | 1,890,000.00 USD | 85,560.00 USD | 19,390.00 USD | 21,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1777` | 4,170,000.00 USD | 4,170,000.00 USD | 67,350.00 USD | 40,700.00 USD | 59,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1779` | 2,020,000.00 USD | 2,020,000.00 USD | 27,480.00 USD | 77,730.00 USD | 25,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1780` | 4,360,000.00 USD | 4,360,000.00 USD | 52,730.00 USD | 38,910.00 USD | 97,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1782` | 2,130,000.00 USD | 2,130,000.00 USD | 46,310.00 USD | 14,240.00 USD | 47,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1783` | 4,550,000.00 USD | 4,550,000.00 USD | 117,540.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1785` | 2,290,000.00 USD | 2,290,000.00 USD | 96,920.00 USD | 51,600.00 USD | 14,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1785` | 421.28 USD | 7,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1786` | 4,750,000.00 USD | 4,750,000.00 USD | 129,440.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1788` | 2,410,000.00 USD | 2,410,000.00 USD | 35,520.00 USD | 42,480.00 USD | 45,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1789` | 4,810,000.00 USD | 4,810,000.00 USD | 48,810.00 USD | 7,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1791` | 2,490,000.00 USD | 2,490,000.00 USD | 41,020.00 USD | 19,320.00 USD | 18,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1792` | 4,980,000.00 USD | 4,980,000.00 USD | 134,000.00 USD | 39,820.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1794` | 2,620,000.00 USD | 2,620,000.00 USD | 45,400.00 USD | 60,380.00 USD | 20,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1795` | 5,070,000.00 USD | 5,070,000.00 USD | 17,130.00 USD | 19,870.00 USD | 44,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1795` | 682.60 USD | 8,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1797` | 2,720,000.00 USD | 2,720,000.00 USD | 41,960.00 USD | 22,110.00 USD | 36,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1798` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 6,240.00 USD | 27,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1800` | 2,760,000.00 USD | 2,760,000.00 USD | 10,230.00 USD | 8,690.00 USD | 25,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1801` | 5,190,000.00 USD | 5,190,000.00 USD | 6,490.00 USD | 40,090.00 USD | 46,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1803` | 2,840,000.00 USD | 2,840,000.00 USD | 16,490.00 USD | 35,880.00 USD | 28,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1804` | 5,260,000.00 USD | 5,260,000.00 USD | 28,790.00 USD | 27,450.00 USD | 14,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1805` | 4,320.00 USD | 12,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1806` | 2,900,000.00 USD | 2,900,000.00 USD | 21,330.00 USD | 14,370.00 USD | 21,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1807` | 5,410,000.00 USD | 5,410,000.00 USD | 11,410.00 USD | 63,170.00 USD | 67,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1809` | 2,990,000.00 USD | 2,990,000.00 USD | 27,060.00 USD | 27,370.00 USD | 32,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1810` | 5,530,000.00 USD | 5,530,000.00 USD | 79,380.00 USD | 30,940.00 USD | 12,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1812` | 3,130,000.00 USD | 3,130,000.00 USD | 56,360.00 USD | 44,030.00 USD | 38,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1813` | 5,630,000.00 USD | 5,630,000.00 USD | 32,530.00 USD | 15,780.00 USD | 56,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1815` | 3,150,000.00 USD | 3,150,000.00 USD | 12,800.00 USD | 3,320.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1816` | 5,730,000.00 USD | 5,730,000.00 USD | 46,430.00 USD | 21,200.00 USD | 25,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1818` | 3,240,000.00 USD | 3,240,000.00 USD | 37,120.00 USD | 11,780.00 USD | 32,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1819` | 5,860,000.00 USD | 5,860,000.00 USD | 65,350.00 USD | 24,720.00 USD | 43,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1821` | 3,290,000.00 USD | 3,290,000.00 USD | 21,220.00 USD | 19,510.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1822` | 6,030,000.00 USD | 6,030,000.00 USD | 46,760.00 USD | 36,230.00 USD | 92,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1824` | 3,340,000.00 USD | 3,340,000.00 USD | 20,050.00 USD | 18,270.00 USD | 13,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1825` | 6,130,000.00 USD | 6,130,000.00 USD | 61,720.00 USD | 17,120.00 USD | 12,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1825` | 48,910.00 USD | 61,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1827` | 3,370,000.00 USD | 3,370,000.00 USD | 21,440.00 USD | 6,860.00 USD | 4,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1828` | 6,270,000.00 USD | 6,270,000.00 USD | 51,470.00 USD | 24,320.00 USD | 69,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1830` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 4,510.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1831` | 6,440,000.00 USD | 6,440,000.00 USD | 85,970.00 USD | 21,930.00 USD | 63,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1833` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 4,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1834` | 6,710,000.00 USD | 6,710,000.00 USD | 165,640.00 USD | 47,980.00 USD | 51,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1835` | 837.27 USD | 62,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1836` | 3,390,000.00 USD | 3,390,000.00 USD | 3,610.00 USD | 0.00 USD | 728.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1837` | 6,940,000.00 USD | 6,940,000.00 USD | 72,930.00 USD | 76,140.00 USD | 83,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1839` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 2,640.00 USD | 7,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1840` | 7,170,000.00 USD | 7,170,000.00 USD | 98,270.00 USD | 47,250.00 USD | 80,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1842` | 3,420,000.00 USD | 3,420,000.00 USD | 13,150.00 USD | 2,690.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1843` | 7,380,000.00 USD | 7,380,000.00 USD | 86,180.00 USD | 18,570.00 USD | 105,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1845` | 3,450,000.00 USD | 3,450,000.00 USD | 5,640.00 USD | 5,640.00 USD | 14,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1845` | 8,800.00 USD | 71,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1846` | 7,570,000.00 USD | 7,570,000.00 USD | 8,330.00 USD | 45,450.00 USD | 135,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1848` | 3,470,000.00 USD | 3,470,000.00 USD | 4,680.00 USD | 4,360.00 USD | 9,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1849` | 7,750,000.00 USD | 7,750,000.00 USD | 62,030.00 USD | 79,580.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1851` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 1,730.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1852` | 8,140,000.00 USD | 8,140,000.00 USD | 153,970.00 USD | 9,590.00 USD | 234,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1854` | 3,480,000.00 USD | 3,480,000.00 USD | 4,290.00 USD | 1,690.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1855` | 8,310,000.00 USD | 8,310,000.00 USD | 58,210.00 USD | 10,160.00 USD | 94,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1857` | 3,500,000.00 USD | 3,500,000.00 USD | 7,260.00 USD | 2,630.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1858` | 8,570,000.00 USD | 8,570,000.00 USD | 96,280.00 USD | 46,830.00 USD | 118,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1860` | 3,520,000.00 USD | 3,520,000.00 USD | 9,450.00 USD | 4,440.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1861` | 8,740,000.00 USD | 8,740,000.00 USD | 99,880.00 USD | 55,030.00 USD | 21,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1863` | 3,530,000.00 USD | 3,530,000.00 USD | 1,870.00 USD | 0.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1864` | 8,920,000.00 USD | 8,920,000.00 USD | 52,190.00 USD | 58,680.00 USD | 61,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1866` | 3,540,000.00 USD | 3,540,000.00 USD | 3,300.00 USD | 0.00 USD | 5,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1867` | 9,120,000.00 USD | 9,120,000.00 USD | 102,440.00 USD | 43,150.00 USD | 52,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1869` | 3,550,000.00 USD | 3,550,000.00 USD | 4,960.00 USD | 1,740.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1870` | 9,470,000.00 USD | 9,470,000.00 USD | 165,360.00 USD | 83,890.00 USD | 101,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1872` | 3,580,000.00 USD | 3,580,000.00 USD | 12,350.00 USD | 5,200.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1873` | 9,730,000.00 USD | 9,730,000.00 USD | 72,410.00 USD | 101,000.00 USD | 90,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1875` | 3,580,000.00 USD | 3,580,000.00 USD | 1,960.00 USD | 2,820.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1875` | 21,190.00 USD | 92,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1876` | 9,830,000.00 USD | 9,830,000.00 USD | 59,490.00 USD | 34,260.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1878` | 3,590,000.00 USD | 3,590,000.00 USD | 4,320.00 USD | 2,760.00 USD | 918.24 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1879` | 9,990,000.00 USD | 9,990,000.00 USD | 57,250.00 USD | 52,690.00 USD | 48,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1881` | 3,600,000.00 USD | 3,600,000.00 USD | 2,920.00 USD | 6,640.00 USD | 1,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1882` | 10,090,000.00 USD | 10,090,000.00 USD | 14,000.00 USD | 23,830.00 USD | 59,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1884` | 3,610,000.00 USD | 3,610,000.00 USD | 1,710.00 USD | 0.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1885` | 10,150,000.00 USD | 10,150,000.00 USD | 19,810.00 USD | 31,900.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1885` | 477.23 USD | 93,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1887` | 3,630,000.00 USD | 3,630,000.00 USD | 13,270.00 USD | 4,390.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1888` | 10,260,000.00 USD | 10,260,000.00 USD | 13,720.00 USD | 17,330.00 USD | 83,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1890` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 7,790.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1891` | 10,310,000.00 USD | 10,310,000.00 USD | 36,740.00 USD | 0.00 USD | 17,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1893` | 3,650,000.00 USD | 3,650,000.00 USD | 5,950.00 USD | 3,490.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1894` | 10,410,000.00 USD | 10,410,000.00 USD | 69,540.00 USD | 12,420.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1896` | 3,660,000.00 USD | 3,660,000.00 USD | 4,500.00 USD | 2,500.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1897` | 10,500,000.00 USD | 10,500,000.00 USD | 25,640.00 USD | 39,120.00 USD | 25,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1899` | 3,690,000.00 USD | 3,690,000.00 USD | 7,270.00 USD | 19,270.00 USD | 3,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1900` | 10,550,000.00 USD | 10,550,000.00 USD | 11,530.00 USD | 21,370.00 USD | 14,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1902` | 3,710,000.00 USD | 3,710,000.00 USD | 6,890.00 USD | 3,410.00 USD | 6,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1903` | 10,590,000.00 USD | 10,590,000.00 USD | 14,330.00 USD | 11,220.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1905` | 3,730,000.00 USD | 3,730,000.00 USD | 2,490.00 USD | 8,320.00 USD | 7,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1906` | 10,670,000.00 USD | 10,670,000.00 USD | 18,470.00 USD | 27,580.00 USD | 33,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1909` | 10,730,000.00 USD | 10,730,000.00 USD | 15,470.00 USD | 29,160.00 USD | 19,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1912` | 10,750,000.00 USD | 10,750,000.00 USD | 0.00 USD | 15,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1915` | 10,760,000.00 USD | 10,760,000.00 USD | 7,460.00 USD | 5,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1918` | 10,780,000.00 USD | 10,780,000.00 USD | 0.00 USD | 11,840.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1924` | 10,800,000.00 USD | 10,800,000.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1927` | 10,830,000.00 USD | 10,830,000.00 USD | 11,600.00 USD | 13,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1945` | 10,830,000.00 USD | 10,830,000.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1945` | 4,270.00 USD | 97,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1955` | 860.20 USD | 98,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1975` | 150.10 USD | 98,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1995` | 135.22 USD | 98,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2025` | 764.66 USD | 99,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2045` | 399.22 USD | 99,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2055` | 11,590.00 USD | 111,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2065` | 611.10 USD | 111,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2085` | 198.08 USD | 112,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2095` | 1,060.00 USD | 113,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2135` | 16,070.00 USD | 129,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 41,230.00 USD | 170,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2195` | 87,800.00 USD | 258,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2205` | 44,100.00 USD | 302,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 343.77 USD | 302,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2245` | 26,710.00 USD | 329,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2255` | 154.78 USD | 329,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 6,820.00 USD | 336,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 16,250.00 USD | 352,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 102.62 USD | 352,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 361.66 USD | 353,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 869.00 USD | 353,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2445` | 231.03 USD | 354,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2465` | 9,360.00 USD | 363,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2545` | 21,010.00 USD | 384,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 4,360.00 USD | 388,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2575` | 29,500.00 USD | 418,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 52,030.00 USD | 470,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 154.94 USD | 470,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2685` | 226.51 USD | 470,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 13,510.00 USD | 484,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 214.21 USD | 484,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 27,890.00 USD | 512,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2765` | 439.77 USD | 512,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2795` | 482.84 USD | 513,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 187.26 USD | 513,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2925` | 2,230.00 USD | 515,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 574.36 USD | 516,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2985` | 17,550.00 USD | 533,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 225.42 USD | 534,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3135` | 62,700.00 USD | 596,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 9,540.00 USD | 606,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3305` | 192.68 USD | 606,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3325` | 148.36 USD | 606,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3355` | 260.28 USD | 606,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3365` | 63,220.00 USD | 670,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3385` | 108.46 USD | 670,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0365` | 2,190,000.00 USD | 0.00 USD | 8,790.00 USD | `-78.49%` | `240,739,300,000,000.00` |
| `Live` | `Long` | `0.0385` | 2,180,000.00 USD | 0.00 USD | 4,000.00 USD | `-77.32%` | `103,823,900,000,000.00` |
| `Live` | `Long` | `0.0415` | 2,180,000.00 USD | 0.00 USD | 408.10 USD | `-75.55%` | `9,833,800,000,000.00` |
| `Live` | `Long` | `0.0425` | 2,180,000.00 USD | 0.00 USD | 170.00 USD | `-74.96%` | `4,000,000,000,000.00` |
| `Live` | `Long` | `0.0435` | 2,180,000.00 USD | 0.00 USD | 125.08 USD | `-74.37%` | `2,875,300,000,000.00` |
| `Live` | `Long` | `0.0455` | 2,180,000.00 USD | 0.00 USD | 4,630.00 USD | `-73.19%` | `101,831,000,000,000.00` |
| `Live` | `Long` | `0.0495` | 2,170,000.00 USD | 0.00 USD | 400.94 USD | `-70.83%` | `8,099,700,000,000.00` |
| `Live` | `Long` | `0.0515` | 2,170,000.00 USD | 0.00 USD | 6,350.00 USD | `-69.66%` | `123,365,600,000,000.00` |
| `Live` | `Long` | `0.0525` | 2,170,000.00 USD | 0.00 USD | 289.43 USD | `-69.07%` | `5,513,000,000,000.00` |
| `Live` | `Long` | `0.0535` | 2,170,000.00 USD | 0.00 USD | 1,670.00 USD | `-68.48%` | `31,224,100,000,000.00` |
| `Live` | `Long` | `0.0545` | 2,160,000.00 USD | 0.00 USD | 2,270.00 USD | `-67.89%` | `41,635,000,000,000.00` |
| `Live` | `Long` | `0.0565` | 2,160,000.00 USD | 0.00 USD | 15,650.00 USD | `-66.71%` | `276,984,000,000,000.00` |
| `Live` | `Long` | `0.0575` | 2,150,000.00 USD | 0.00 USD | 141.13 USD | `-66.12%` | `2,454,400,000,000.00` |
| `Live` | `Long` | `0.0625` | 2,150,000.00 USD | 0.00 USD | 252.94 USD | `-63.17%` | `4,047,100,000,000.00` |
| `Live` | `Long` | `0.0645` | 2,150,000.00 USD | 0.00 USD | 988.03 USD | `-62.00%` | `15,318,300,000,000.00` |
| `Live` | `Long` | `0.0675` | 2,150,000.00 USD | 0.00 USD | 170,670.00 USD | `-60.23%` | `2,528,385,900,000,000.00` |
| `Live` | `Long` | `0.0685` | 1,970,000.00 USD | 0.00 USD | 591.90 USD | `-59.64%` | `8,640,900,000,000.00` |
| `Live` | `Long` | `0.0695` | 1,970,000.00 USD | 0.00 USD | 5,010.00 USD | `-59.05%` | `72,070,000,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,970,000.00 USD | 0.00 USD | 2,970.00 USD | `-58.46%` | `42,142,800,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,970,000.00 USD | 0.00 USD | 8,250.00 USD | `-57.87%` | `115,382,900,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,960,000.00 USD | 0.00 USD | 4,010.00 USD | `-57.28%` | `55,272,300,000,000.00` |
| `Live` | `Long` | `0.0735` | 1,950,000.00 USD | 0.00 USD | 2,440.00 USD | `-56.69%` | `33,161,800,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,950,000.00 USD | 0.00 USD | 226.17 USD | `-56.10%` | `3,035,900,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,950,000.00 USD | 0.00 USD | 16,420.00 USD | `-54.93%` | `214,653,100,000,000.00` |
| `Live` | `Long` | `0.0775` | 1,930,000.00 USD | 0.00 USD | 27,120.00 USD | `-54.34%` | `350,000,000,000,000.00` |
| `Live` | `Long` | `0.0785` | 1,910,000.00 USD | 0.00 USD | 1,520.00 USD | `-53.75%` | `19,414,500,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,910,000.00 USD | 0.00 USD | 4,630.00 USD | `-53.16%` | `58,261,800,000,000.00` |
| `Live` | `Long` | `0.0805` | 1,900,000.00 USD | 0.00 USD | 13,780.00 USD | `-52.57%` | `171,199,600,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,890,000.00 USD | 0.00 USD | 13,840.00 USD | `-51.39%` | `167,742,900,000,000.00` |
| `Live` | `Long` | `0.0835` | 1,870,000.00 USD | 0.00 USD | 112.78 USD | `-50.80%` | `1,350,600,000,000.00` |
| `Live` | `Long` | `0.0845` | 1,870,000.00 USD | 0.00 USD | 41,430.00 USD | `-50.21%` | `490,249,100,000,000.00` |
| `Live` | `Long` | `0.0865` | 1,830,000.00 USD | 0.00 USD | 611.76 USD | `-49.03%` | `7,072,400,000,000.00` |
| `Live` | `Long` | `0.0875` | 1,830,000.00 USD | 0.00 USD | 7,650.00 USD | `-48.44%` | `87,419,000,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,820,000.00 USD | 0.00 USD | 362.62 USD | `-47.86%` | `4,097,400,000,000.00` |
| `Live` | `Long` | `0.0895` | 1,820,000.00 USD | 0.00 USD | 116.06 USD | `-47.27%` | `1,296,800,000,000.00` |
| `Live` | `Long` | `0.0915` | 1,820,000.00 USD | 0.00 USD | 683.50 USD | `-46.09%` | `7,469,900,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,820,000.00 USD | 0.00 USD | 2,040.00 USD | `-45.50%` | `22,044,300,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,820,000.00 USD | 0.00 USD | 814.24 USD | `-44.91%` | `8,708,500,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,820,000.00 USD | 0.00 USD | 42,840.00 USD | `-44.32%` | `453,385,500,000,000.00` |
| `Live` | `Long` | `0.0955` | 1,780,000.00 USD | 0.00 USD | 477.50 USD | `-43.73%` | `5,000,000,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,780,000.00 USD | 0.00 USD | 874.69 USD | `-43.14%` | `9,064,100,000,000.00` |
| `Live` | `Long` | `0.0975` | 1,780,000.00 USD | 0.00 USD | 145.24 USD | `-42.55%` | `1,489,600,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,780,000.00 USD | 0.00 USD | 5,970.00 USD | `-41.96%` | `60,604,700,000,000.00` |
| `Live` | `Long` | `0.0995` | 1,770,000.00 USD | 0.00 USD | 8,410.00 USD | `-41.37%` | `84,546,700,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,760,000.00 USD | 0.00 USD | 1,850.00 USD | `-40.78%` | `18,436,400,000,000.00` |
| `Live` | `Long` | `0.1025` | 1,760,000.00 USD | 0.00 USD | 811.82 USD | `-39.61%` | `7,920,200,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,760,000.00 USD | 0.00 USD | 802.14 USD | `-39.02%` | `7,750,100,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,760,000.00 USD | 0.00 USD | 24,500.00 USD | `-38.43%` | `234,490,200,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,730,000.00 USD | 0.00 USD | 6,860.00 USD | `-37.84%` | `65,046,300,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,730,000.00 USD | 0.00 USD | 181.20 USD | `-37.25%` | `1,701,400,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,730,000.00 USD | 0.00 USD | 1,060.00 USD | `-36.66%` | `9,856,300,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,730,000.00 USD | 0.00 USD | 342.59 USD | `-36.07%` | `3,157,500,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,730,000.00 USD | 0.00 USD | 534.49 USD | `-34.89%` | `4,837,000,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,720,000.00 USD | 0.00 USD | 425.50 USD | `-34.30%` | `3,816,100,000,000.00` |
| `Live` | `Long` | `0.1125` | 1,720,000.00 USD | 0.00 USD | 107.92 USD | `-33.71%` | `959,300,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,720,000.00 USD | 0.00 USD | 3,570.00 USD | `-33.13%` | `31,437,700,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,720,000.00 USD | 0.00 USD | 20,830.00 USD | `-32.54%` | `181,880,700,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,700,000.00 USD | 0.00 USD | 5,440.00 USD | `-31.95%` | `47,089,900,000,000.00` |
| `Live` | `Long` | `0.1165` | 1,690,000.00 USD | 0.00 USD | 13,260.00 USD | `-31.36%` | `113,787,400,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,680,000.00 USD | 0.00 USD | 1,560.00 USD | `-30.77%` | `13,261,500,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,680,000.00 USD | 0.00 USD | 25,940.00 USD | `-30.18%` | `218,884,900,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,650,000.00 USD | 0.00 USD | 15,480.00 USD | `-29.59%` | `129,539,800,000,000.00` |
| `Live` | `Long` | `0.1205` | 1,640,000.00 USD | 0.00 USD | 4,790.00 USD | `-29.00%` | `39,776,900,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,630,000.00 USD | 0.00 USD | 406.25 USD | `-28.41%` | `3,343,600,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,630,000.00 USD | 0.00 USD | 8,920.00 USD | `-27.82%` | `72,830,700,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,620,000.00 USD | 0.00 USD | 33,070.00 USD | `-27.23%` | `267,745,800,000,000.00` |
| `Live` | `Long` | `0.1245` | 1,590,000.00 USD | 0.00 USD | 1,040.00 USD | `-26.64%` | `8,332,800,000,000.00` |
| `Live` | `Long` | `0.1255` | 1,590,000.00 USD | 0.00 USD | 4,850.00 USD | `-26.05%` | `38,646,100,000,000.00` |
| `Live` | `Long` | `0.1265` | 1,580,000.00 USD | 0.00 USD | 1,200.00 USD | `-25.47%` | `9,489,700,000,000.00` |
| `Live` | `Long` | `0.1275` | 1,580,000.00 USD | 0.00 USD | 6,310.00 USD | `-24.88%` | `49,482,900,000,000.00` |
| `Live` | `Long` | `0.1285` | 1,580,000.00 USD | 0.00 USD | 9,900.00 USD | `-24.29%` | `77,071,500,000,000.00` |
| `Live` | `Long` | `0.1295` | 1,570,000.00 USD | 0.00 USD | 7,140.00 USD | `-23.70%` | `55,124,400,000,000.00` |
| `Live` | `Long` | `0.1305` | 1,560,000.00 USD | 0.00 USD | 15,040.00 USD | `-23.11%` | `115,242,000,000,000.00` |
| `Live` | `Long` | `0.1315` | 1,550,000.00 USD | 0.00 USD | 10,500.00 USD | `-22.52%` | `79,839,800,000,000.00` |
| `Live` | `Long` | `0.1325` | 1,530,000.00 USD | 0.00 USD | 6,620.00 USD | `-21.93%` | `50,000,000,000,000.00` |
| `Live` | `Long` | `0.1335` | 1,530,000.00 USD | 0.00 USD | 23,230.00 USD | `-21.34%` | `174,014,300,000,000.00` |
| `Live` | `Long` | `0.1345` | 1,500,000.00 USD | 0.00 USD | 2,970.00 USD | `-20.75%` | `22,103,800,000,000.00` |
| `Live` | `Long` | `0.1365` | 1,500,000.00 USD | 0.00 USD | 19,420.00 USD | `-19.57%` | `142,251,900,000,000.00` |
| `Live` | `Long` | `0.1375` | 1,480,000.00 USD | 0.00 USD | 1,090.00 USD | `-18.98%` | `7,959,900,000,000.00` |
| `Live` | `Long` | `0.1385` | 1,480,000.00 USD | 0.00 USD | 4,400.00 USD | `-18.40%` | `31,766,700,000,000.00` |
| `Live` | `Long` | `0.1395` | 1,480,000.00 USD | 0.00 USD | 69,250.00 USD | `-17.81%` | `496,401,400,000,000.00` |
| `Live` | `Long` | `0.1405` | 1,410,000.00 USD | 0.00 USD | 8,420.00 USD | `-17.22%` | `59,894,100,000,000.00` |
| `Live` | `Long` | `0.1415` | 1,400,000.00 USD | 0.00 USD | 11,550.00 USD | `-16.63%` | `81,618,300,000,000.00` |
| `Live` | `Long` | `0.1425` | 1,390,000.00 USD | 0.00 USD | 496,690.00 USD | `-16.04%` | `3,485,542,300,000,000.00` |
| `Live` | `Long` | `0.1435` | 891,110.00 USD | 0.00 USD | 19,330.00 USD | `-15.45%` | `134,671,900,000,000.00` |
| `Live` | `Long` | `0.1445` | 871,780.00 USD | 0.00 USD | 53,790.00 USD | `-14.86%` | `372,262,000,000,000.00` |
| `Live` | `Long` | `0.1455` | 817,990.00 USD | 0.00 USD | 3,880.00 USD | `-14.27%` | `26,687,900,000,000.00` |
| `Live` | `Long` | `0.1465` | 814,110.00 USD | 0.00 USD | 193,660.00 USD | `-13.68%` | `1,321,878,600,000,000.00` |
| `Live` | `Long` | `0.1475` | 620,450.00 USD | 0.00 USD | 73,750.00 USD | `-13.09%` | `500,000,000,000,000.00` |
| `Live` | `Long` | `0.1485` | 546,700.00 USD | 0.00 USD | 2,890.00 USD | `-12.50%` | `19,472,100,000,000.00` |
| `Live` | `Long` | `0.1495` | 543,810.00 USD | 0.00 USD | 35,380.00 USD | `-11.91%` | `236,635,500,000,000.00` |
| `Live` | `Long` | `0.1505` | 508,430.00 USD | 0.00 USD | 102,290.00 USD | `-11.32%` | `679,673,200,000,000.00` |
| `Live` | `Long` | `0.1515` | 406,140.00 USD | 0.00 USD | 4,180.00 USD | `-10.74%` | `27,590,100,000,000.00` |
| `Live` | `Long` | `0.1525` | 401,960.00 USD | 0.00 USD | 45,320.00 USD | `-10.15%` | `297,158,600,000,000.00` |
| `Live` | `Long` | `0.1535` | 356,640.00 USD | 0.00 USD | 19,400.00 USD | `-9.56%` | `126,406,800,000,000.00` |
| `Live` | `Long` | `0.1545` | 337,240.00 USD | 0.00 USD | 26,170.00 USD | `-8.97%` | `169,378,600,000,000.00` |
| `Live` | `Long` | `0.1555` | 311,070.00 USD | 0.00 USD | 40,060.00 USD | `-8.38%` | `257,609,900,000,000.00` |
| `Live` | `Long` | `0.1565` | 271,010.00 USD | 0.00 USD | 21,460.00 USD | `-7.79%` | `137,118,700,000,000.02` |
| `Live` | `Long` | `0.1575` | 249,550.00 USD | 0.00 USD | 4,940.00 USD | `-7.20%` | `31,351,900,000,000.00` |
| `Live` | `Long` | `0.1585` | 244,620.00 USD | 0.00 USD | 2,660.00 USD | `-6.61%` | `16,779,500,000,000.00` |
| `Live` | `Long` | `0.1595` | 241,960.00 USD | 0.00 USD | 66,110.00 USD | `-6.02%` | `414,489,500,000,000.00` |
| `Live` | `Long` | `0.1605` | 175,850.00 USD | 0.00 USD | 20,460.00 USD | `-5.43%` | `127,458,000,000,000.00` |
| `Live` | `Long` | `0.1615` | 155,390.00 USD | 0.00 USD | 17,950.00 USD | `-4.84%` | `111,158,400,000,000.00` |
| `Live` | `Long` | `0.1625` | 137,440.00 USD | 0.00 USD | 98,470.00 USD | `-4.25%` | `605,947,100,000,000.00` |
| `Live` | `Long` | `0.1635` | 38,970.00 USD | 0.00 USD | 5,930.00 USD | `-3.66%` | `36,266,300,000,000.00` |
| `Live` | `Long` | `0.1645` | 33,040.00 USD | 0.00 USD | 14,520.00 USD | `-3.08%` | `88,293,000,000,000.00` |
| `Live` | `Long` | `0.1655` | 18,520.00 USD | 0.00 USD | 12,410.00 USD | `-2.49%` | `75,000,000,000,000.00` |
| `Live` | `Long` | `0.1675` | 6,100.00 USD | 0.00 USD | 6,100.00 USD | `-1.31%` | `36,440,800,000,000.00` |
| `Live` | `Short` | `0.1735` | 6,900.00 USD | 6,900.00 USD | 0.00 USD | `+2.23%` | `39,797,200,000,000.00` |
| `Live` | `Short` | `0.1765` | 7,240.00 USD | 339.06 USD | 0.00 USD | `+3.99%` | `1,921,000,000,000.00` |
| `Live` | `Short` | `0.1775` | 7,400.00 USD | 151.67 USD | 0.00 USD | `+4.58%` | `854,500,000,000.00` |
| `Live` | `Short` | `0.1785` | 7,820.00 USD | 421.28 USD | 0.00 USD | `+5.17%` | `2,360,100,000,000.00` |
| `Live` | `Short` | `0.1795` | 8,500.00 USD | 682.60 USD | 0.00 USD | `+5.76%` | `3,802,800,000,000.00` |
| `Live` | `Short` | `0.1805` | 12,820.00 USD | 4,320.00 USD | 0.00 USD | `+6.35%` | `23,915,200,000,000.00` |
| `Live` | `Short` | `0.1825` | 61,730.00 USD | 48,910.00 USD | 0.00 USD | `+7.53%` | `268,015,200,000,000.00` |
| `Live` | `Short` | `0.1835` | 62,570.00 USD | 837.27 USD | 0.00 USD | `+8.12%` | `4,562,800,000,000.00` |
| `Live` | `Short` | `0.1845` | 71,370.00 USD | 8,800.00 USD | 0.00 USD | `+8.71%` | `47,719,700,000,000.00` |
| `Live` | `Short` | `0.1875` | 92,560.00 USD | 21,190.00 USD | 0.00 USD | `+10.48%` | `112,997,300,000,000.00` |
| `Live` | `Short` | `0.1885` | 93,030.00 USD | 477.23 USD | 0.00 USD | `+11.07%` | `2,531,700,000,000.00` |
| `Live` | `Short` | `0.1945` | 97,300.00 USD | 4,270.00 USD | 0.00 USD | `+14.60%` | `21,946,900,000,000.00` |
| `Live` | `Short` | `0.1955` | 98,160.00 USD | 860.20 USD | 0.00 USD | `+15.19%` | `4,400,000,000,000.00` |
| `Live` | `Short` | `0.1975` | 98,310.00 USD | 150.10 USD | 0.00 USD | `+16.37%` | `760,000,000,000.00` |
| `Live` | `Short` | `0.1995` | 98,450.00 USD | 135.22 USD | 0.00 USD | `+17.55%` | `677,800,000,000.00` |
| `Live` | `Short` | `0.2025` | 99,210.00 USD | 764.66 USD | 0.00 USD | `+19.31%` | `3,776,100,000,000.00` |
| `Live` | `Short` | `0.2045` | 99,610.00 USD | 399.22 USD | 0.00 USD | `+20.49%` | `1,952,200,000,000.00` |
| `Live` | `Short` | `0.2055` | 111,200.00 USD | 11,590.00 USD | 0.00 USD | `+21.08%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2065` | 111,820.00 USD | 611.10 USD | 0.00 USD | `+21.67%` | `2,959,300,000,000.00` |
| `Live` | `Short` | `0.2085` | 112,010.00 USD | 198.08 USD | 0.00 USD | `+22.85%` | `950,000,000,000.00` |
| `Live` | `Short` | `0.2095` | 113,070.00 USD | 1,060.00 USD | 0.00 USD | `+23.44%` | `5,056,300,000,000.00` |
| `Live` | `Short` | `0.2135` | 129,150.00 USD | 16,070.00 USD | 0.00 USD | `+25.80%` | `75,287,100,000,000.00` |
| `Live` | `Short` | `0.2155` | 170,380.00 USD | 41,230.00 USD | 0.00 USD | `+26.97%` | `191,330,600,000,000.00` |
| `Live` | `Short` | `0.2195` | 258,180.00 USD | 87,800.00 USD | 0.00 USD | `+29.33%` | `400,000,000,000,000.00` |
| `Live` | `Short` | `0.2205` | 302,280.00 USD | 44,100.00 USD | 0.00 USD | `+29.92%` | `200,003,000,000,000.00` |
| `Live` | `Short` | `0.2235` | 302,620.00 USD | 343.77 USD | 0.00 USD | `+31.69%` | `1,538,100,000,000.00` |
| `Live` | `Short` | `0.2245` | 329,340.00 USD | 26,710.00 USD | 0.00 USD | `+32.28%` | `118,989,500,000,000.00` |
| `Live` | `Short` | `0.2255` | 329,490.00 USD | 154.78 USD | 0.00 USD | `+32.87%` | `686,400,000,000.00` |
| `Live` | `Short` | `0.2295` | 336,310.00 USD | 6,820.00 USD | 0.00 USD | `+35.22%` | `29,727,000,000,000.00` |
| `Live` | `Short` | `0.2355` | 352,570.00 USD | 16,250.00 USD | 0.00 USD | `+38.76%` | `69,017,500,000,000.00` |
| `Live` | `Short` | `0.2375` | 352,670.00 USD | 102.62 USD | 0.00 USD | `+39.94%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2405` | 353,030.00 USD | 361.66 USD | 0.00 USD | `+41.70%` | `1,503,800,000,000.00` |
| `Live` | `Short` | `0.2425` | 353,900.00 USD | 869.00 USD | 0.00 USD | `+42.88%` | `3,583,500,000,000.00` |
| `Live` | `Short` | `0.2445` | 354,130.00 USD | 231.03 USD | 0.00 USD | `+44.06%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2465` | 363,490.00 USD | 9,360.00 USD | 0.00 USD | `+45.24%` | `37,972,200,000,000.00` |
| `Live` | `Short` | `0.2545` | 384,500.00 USD | 21,010.00 USD | 0.00 USD | `+49.95%` | `82,547,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 388,860.00 USD | 4,360.00 USD | 0.00 USD | `+51.13%` | `17,014,200,000,000.00` |
| `Live` | `Short` | `0.2575` | 418,360.00 USD | 29,500.00 USD | 0.00 USD | `+51.72%` | `114,561,100,000,000.00` |
| `Live` | `Short` | `0.2585` | 470,390.00 USD | 52,030.00 USD | 0.00 USD | `+52.31%` | `201,260,100,000,000.00` |
| `Live` | `Short` | `0.2615` | 470,540.00 USD | 154.94 USD | 0.00 USD | `+54.08%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2685` | 470,770.00 USD | 226.51 USD | 0.00 USD | `+58.20%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2715` | 484,280.00 USD | 13,510.00 USD | 0.00 USD | `+59.97%` | `49,773,600,000,000.00` |
| `Live` | `Short` | `0.2725` | 484,500.00 USD | 214.21 USD | 0.00 USD | `+60.56%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 512,390.00 USD | 27,890.00 USD | 0.00 USD | `+61.74%` | `101,607,700,000,000.00` |
| `Live` | `Short` | `0.2765` | 512,830.00 USD | 439.77 USD | 0.00 USD | `+62.92%` | `1,590,500,000,000.00` |
| `Live` | `Short` | `0.2795` | 513,310.00 USD | 482.84 USD | 0.00 USD | `+64.68%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2915` | 513,500.00 USD | 187.26 USD | 0.00 USD | `+71.75%` | `642,400,000,000.00` |
| `Live` | `Short` | `0.2925` | 515,730.00 USD | 2,230.00 USD | 0.00 USD | `+72.34%` | `7,608,100,000,000.00` |
| `Live` | `Short` | `0.2955` | 516,300.00 USD | 574.36 USD | 0.00 USD | `+74.11%` | `1,943,700,000,000.00` |
| `Live` | `Short` | `0.2985` | 533,850.00 USD | 17,550.00 USD | 0.00 USD | `+75.88%` | `58,786,700,000,000.00` |
| `Live` | `Short` | `0.3105` | 534,070.00 USD | 225.42 USD | 0.00 USD | `+82.95%` | `726,000,000,000.00` |
| `Live` | `Short` | `0.3135` | 596,770.00 USD | 62,700.00 USD | 0.00 USD | `+84.72%` | `200,000,000,000,000.00` |
| `Live` | `Short` | `0.3295` | 606,310.00 USD | 9,540.00 USD | 0.00 USD | `+94.14%` | `28,943,600,000,000.00` |
| `Live` | `Short` | `0.3305` | 606,500.00 USD | 192.68 USD | 0.00 USD | `+94.73%` | `583,000,000,000.00` |
| `Live` | `Short` | `0.3325` | 606,650.00 USD | 148.36 USD | 0.00 USD | `+95.91%` | `446,200,000,000.00` |
| `Live` | `Short` | `0.3355` | 606,910.00 USD | 260.28 USD | 0.00 USD | `+97.68%` | `775,800,000,000.00` |
| `Live` | `Short` | `0.3365` | 670,140.00 USD | 63,220.00 USD | 0.00 USD | `+98.27%` | `187,887,700,000,000.00` |
| `Live` | `Short` | `0.3385` | 670,240.00 USD | 108.46 USD | 0.00 USD | `+99.45%` | `320,400,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0355` | 900,960.00 USD | 0.00 USD | 355.00 USD | `-79.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 900,600.00 USD | 0.00 USD | 589.71 USD | `-74.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 900,010.00 USD | 0.00 USD | 353.50 USD | `-70.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 899,660.00 USD | 0.00 USD | 4,310.00 USD | `-67.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 895,350.00 USD | 0.00 USD | 475.11 USD | `-62.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 894,870.00 USD | 0.00 USD | 131.16 USD | `-61.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 894,740.00 USD | 0.00 USD | 881.45 USD | `-60.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 893,860.00 USD | 0.00 USD | 1,070.00 USD | `-60.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 892,790.00 USD | 0.00 USD | 1,400.00 USD | `-59.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 891,390.00 USD | 0.00 USD | 1,010.00 USD | `-59.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 890,380.00 USD | 0.00 USD | 4,490.00 USD | `-58.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 885,890.00 USD | 0.00 USD | 529.04 USD | `-57.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 885,360.00 USD | 0.00 USD | 2,390.00 USD | `-57.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 882,970.00 USD | 0.00 USD | 757.39 USD | `-55.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 882,210.00 USD | 0.00 USD | 1,490.00 USD | `-53.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 880,730.00 USD | 0.00 USD | 277.37 USD | `-49.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 880,450.00 USD | 0.00 USD | 262.50 USD | `-48.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 880,190.00 USD | 0.00 USD | 795.57 USD | `-47.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 879,390.00 USD | 0.00 USD | 181.00 USD | `-46.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 879,210.00 USD | 0.00 USD | 1,020.00 USD | `-40.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 878,190.00 USD | 0.00 USD | 1,550.00 USD | `-39.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 876,640.00 USD | 0.00 USD | 116.07 USD | `-36.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 876,530.00 USD | 0.00 USD | 19,070.00 USD | `-36.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 857,450.00 USD | 0.00 USD | 577.22 USD | `-34.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 856,880.00 USD | 0.00 USD | 343.50 USD | `-32.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 856,530.00 USD | 0.00 USD | 26,280.00 USD | `-31.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1175` | 830,250.00 USD | 0.00 USD | 105.75 USD | `-30.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 830,150.00 USD | 0.00 USD | 120.50 USD | `-29.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 830,030.00 USD | 0.00 USD | 83,620.00 USD | `-28.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 746,400.00 USD | 0.00 USD | 14,940.00 USD | `-26.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 731,460.00 USD | 0.00 USD | 3,010.00 USD | `-25.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 728,460.00 USD | 0.00 USD | 473.27 USD | `-24.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 727,980.00 USD | 0.00 USD | 220,940.00 USD | `-24.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 507,050.00 USD | 0.00 USD | 25,060.00 USD | `-23.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 481,990.00 USD | 0.00 USD | 5,560.00 USD | `-21.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 476,420.00 USD | 0.00 USD | 625.78 USD | `-21.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 475,800.00 USD | 0.00 USD | 7,960.00 USD | `-20.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 467,840.00 USD | 0.00 USD | 16,260.00 USD | `-20.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 451,570.00 USD | 0.00 USD | 700.86 USD | `-19.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 450,870.00 USD | 0.00 USD | 108.57 USD | `-18.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 450,770.00 USD | 0.00 USD | 349.74 USD | `-17.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 450,420.00 USD | 0.00 USD | 3,520.00 USD | `-17.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 446,890.00 USD | 0.00 USD | 127.35 USD | `-16.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 446,770.00 USD | 0.00 USD | 24,850.00 USD | `-16.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 421,920.00 USD | 0.00 USD | 702.55 USD | `-15.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 421,220.00 USD | 0.00 USD | 1,960.00 USD | `-14.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 419,260.00 USD | 0.00 USD | 27,090.00 USD | `-14.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 392,170.00 USD | 0.00 USD | 119.66 USD | `-13.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 392,050.00 USD | 0.00 USD | 2,290.00 USD | `-13.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 389,750.00 USD | 0.00 USD | 4,550.00 USD | `-12.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 385,210.00 USD | 0.00 USD | 2,420.00 USD | `-11.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 382,790.00 USD | 0.00 USD | 4,360.00 USD | `-11.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 378,430.00 USD | 0.00 USD | 702.05 USD | `-10.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 377,720.00 USD | 0.00 USD | 1,000.00 USD | `-10.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1535` | 376,720.00 USD | 0.00 USD | 9,210.00 USD | `-9.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 367,510.00 USD | 0.00 USD | 18,770.00 USD | `-8.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 348,740.00 USD | 0.00 USD | 84,400.00 USD | `-8.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 264,350.00 USD | 0.00 USD | 718.79 USD | `-7.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1575` | 263,630.00 USD | 0.00 USD | 443.71 USD | `-7.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 263,190.00 USD | 0.00 USD | 17,200.00 USD | `-6.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 245,980.00 USD | 0.00 USD | 70,970.00 USD | `-6.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 175,010.00 USD | 0.00 USD | 16,890.00 USD | `-5.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 158,130.00 USD | 0.00 USD | 16,870.00 USD | `-4.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 141,260.00 USD | 0.00 USD | 1,140.00 USD | `-4.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 140,120.00 USD | 0.00 USD | 18,130.00 USD | `-3.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 121,990.00 USD | 0.00 USD | 2,850.00 USD | `-3.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 119,140.00 USD | 0.00 USD | 7,240.00 USD | `-2.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 111,900.00 USD | 0.00 USD | 763.67 USD | `-1.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 111,140.00 USD | 0.00 USD | 386.67 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1685` | 110,750.00 USD | 0.00 USD | 168.50 USD | `-0.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 110,580.00 USD | 0.00 USD | 110,580.00 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 1,110.00 USD | 1,110.00 USD | 0.00 USD | `+0.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 2,140.00 USD | 1,030.00 USD | 0.00 USD | `+1.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 3,480.00 USD | 1,330.00 USD | 0.00 USD | `+1.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 24,300.00 USD | 20,830.00 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 30,950.00 USD | 6,650.00 USD | 0.00 USD | `+2.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 31,620.00 USD | 673.32 USD | 0.00 USD | `+3.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 37,060.00 USD | 5,440.00 USD | 0.00 USD | `+3.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 37,280.00 USD | 213.30 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 138,050.00 USD | 100,770.00 USD | 0.00 USD | `+5.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 165,880.00 USD | 27,840.00 USD | 0.00 USD | `+5.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 168,230.00 USD | 2,350.00 USD | 0.00 USD | `+6.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 178,590.00 USD | 10,360.00 USD | 0.00 USD | `+6.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 179,450.00 USD | 864.12 USD | 0.00 USD | `+7.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 181,980.00 USD | 2,520.00 USD | 0.00 USD | `+8.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 182,260.00 USD | 276.75 USD | 0.00 USD | `+8.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 182,410.00 USD | 149.79 USD | 0.00 USD | `+9.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 186,450.00 USD | 4,040.00 USD | 0.00 USD | `+9.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 186,600.00 USD | 147.11 USD | 0.00 USD | `+10.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 186,840.00 USD | 245.50 USD | 0.00 USD | `+11.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 187,500.00 USD | 660.73 USD | 0.00 USD | `+11.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 194,640.00 USD | 7,130.00 USD | 0.00 USD | `+12.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 195,030.00 USD | 396.42 USD | 0.00 USD | `+12.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 196,070.00 USD | 1,040.00 USD | 0.00 USD | `+13.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 203,140.00 USD | 7,070.00 USD | 0.00 USD | `+14.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 203,890.00 USD | 742.45 USD | 0.00 USD | `+14.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 208,400.00 USD | 4,520.00 USD | 0.00 USD | `+15.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 208,540.00 USD | 133.19 USD | 0.00 USD | `+15.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 208,670.00 USD | 134.20 USD | 0.00 USD | `+16.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 210,130.00 USD | 1,460.00 USD | 0.00 USD | `+16.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 210,620.00 USD | 492.19 USD | 0.00 USD | `+17.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 233,590.00 USD | 22,970.00 USD | 0.00 USD | `+18.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 234,450.00 USD | 863.97 USD | 0.00 USD | `+18.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 259,090.00 USD | 24,640.00 USD | 0.00 USD | `+19.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 259,270.00 USD | 182.72 USD | 0.00 USD | `+19.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 345,170.00 USD | 85,900.00 USD | 0.00 USD | `+20.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 346,580.00 USD | 1,410.00 USD | 0.00 USD | `+21.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 346,760.00 USD | 174.20 USD | 0.00 USD | `+21.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 348,830.00 USD | 2,080.00 USD | 0.00 USD | `+22.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 349,080.00 USD | 252.51 USD | 0.00 USD | `+23.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 384,170.00 USD | 35,090.00 USD | 0.00 USD | `+24.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 384,300.00 USD | 126.50 USD | 0.00 USD | `+24.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 384,490.00 USD | 190.80 USD | 0.00 USD | `+25.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 385,200.00 USD | 713.94 USD | 0.00 USD | `+25.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 385,420.00 USD | 213.00 USD | 0.00 USD | `+26.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 387,870.00 USD | 2,460.00 USD | 0.00 USD | `+27.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 394,150.00 USD | 6,280.00 USD | 0.00 USD | `+28.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 530,750.00 USD | 136,590.00 USD | 0.00 USD | `+29.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 531,080.00 USD | 333.91 USD | 0.00 USD | `+31.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 535,060.00 USD | 3,980.00 USD | 0.00 USD | `+31.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 535,440.00 USD | 378.55 USD | 0.00 USD | `+32.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 535,820.00 USD | 380.23 USD | 0.00 USD | `+33.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 536,000.00 USD | 185.87 USD | 0.00 USD | `+34.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 536,190.00 USD | 192.69 USD | 0.00 USD | `+34.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2295` | 536,380.00 USD | 187.50 USD | 0.00 USD | `+35.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 581,030.00 USD | 44,650.00 USD | 0.00 USD | `+35.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 581,220.00 USD | 189.14 USD | 0.00 USD | `+36.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 585,480.00 USD | 4,260.00 USD | 0.00 USD | `+36.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 587,000.00 USD | 1,520.00 USD | 0.00 USD | `+37.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 587,190.00 USD | 191.59 USD | 0.00 USD | `+38.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 608,510.00 USD | 21,320.00 USD | 0.00 USD | `+39.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 611,040.00 USD | 2,530.00 USD | 0.00 USD | `+40.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 611,240.00 USD | 195.67 USD | 0.00 USD | `+41.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 633,480.00 USD | 22,240.00 USD | 0.00 USD | `+41.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 642,780.00 USD | 9,300.00 USD | 0.00 USD | `+42.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 644,380.00 USD | 1,600.00 USD | 0.00 USD | `+44.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 663,130.00 USD | 18,750.00 USD | 0.00 USD | `+45.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 663,680.00 USD | 551.23 USD | 0.00 USD | `+45.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 664,710.00 USD | 1,030.00 USD | 0.00 USD | `+47.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 671,900.00 USD | 7,190.00 USD | 0.00 USD | `+47.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 672,190.00 USD | 289.23 USD | 0.00 USD | `+48.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 677,200.00 USD | 5,010.00 USD | 0.00 USD | `+48.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 693,080.00 USD | 15,880.00 USD | 0.00 USD | `+49.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 694,860.00 USD | 1,780.00 USD | 0.00 USD | `+49.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 697,600.00 USD | 2,740.00 USD | 0.00 USD | `+50.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 709,330.00 USD | 11,730.00 USD | 0.00 USD | `+51.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 714,490.00 USD | 5,160.00 USD | 0.00 USD | `+51.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 731,360.00 USD | 16,870.00 USD | 0.00 USD | `+52.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 760,490.00 USD | 29,130.00 USD | 0.00 USD | `+53.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2655` | 840,270.00 USD | 79,780.00 USD | 0.00 USD | `+56.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 840,550.00 USD | 272.88 USD | 0.00 USD | `+59.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 840,940.00 USD | 394.01 USD | 0.00 USD | `+62.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 860,540.00 USD | 19,600.00 USD | 0.00 USD | `+65.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 862,670.00 USD | 2,130.00 USD | 0.00 USD | `+68.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 863,250.00 USD | 579.27 USD | 0.00 USD | `+68.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 866,260.00 USD | 3,010.00 USD | 0.00 USD | `+71.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 866,360.00 USD | 101.21 USD | 0.00 USD | `+74.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 866,630.00 USD | 262.73 USD | 0.00 USD | `+74.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 868,060.00 USD | 1,440.00 USD | 0.00 USD | `+75.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 873,720.00 USD | 5,660.00 USD | 0.00 USD | `+77.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 879,150.00 USD | 5,430.00 USD | 0.00 USD | `+77.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 879,440.00 USD | 289.61 USD | 0.00 USD | `+80.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3095` | 918,130.00 USD | 38,690.00 USD | 0.00 USD | `+82.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 923,300.00 USD | 5,180.00 USD | 0.00 USD | `+85.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 923,660.00 USD | 357.85 USD | 0.00 USD | `+96.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3355` | 923,910.00 USD | 251.29 USD | 0.00 USD | `+97.68%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1468` | 10,660,000.00 USD | 0.00 USD | 10,660,000.00 USD | 9,720.00 USD | 9,180.00 USD | 8,720.00 USD |
| `7D` | `0.1471` | 10,630,000.00 USD | 0.00 USD | 10,630,000.00 USD | 6,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1474` | 10,630,000.00 USD | 0.00 USD | 10,630,000.00 USD | 6,490.00 USD | 9,220.00 USD | 5,280.00 USD |
| `7D` | `0.1477` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 0.00 USD | 25,460.00 USD | 5,320.00 USD |
| `7D` | `0.1480` | 10,580,000.00 USD | 0.00 USD | 10,580,000.00 USD | 6,990.00 USD | 29,300.00 USD | 20,830.00 USD |
| `7D` | `0.1483` | 10,520,000.00 USD | 0.00 USD | 10,520,000.00 USD | 42,230.00 USD | 16,640.00 USD | 33,050.00 USD |
| `7D` | `0.1486` | 10,430,000.00 USD | 0.00 USD | 10,430,000.00 USD | 18,610.00 USD | 10,470.00 USD | 25,980.00 USD |
| `7D` | `0.1489` | 10,370,000.00 USD | 0.00 USD | 10,370,000.00 USD | 11,170.00 USD | 3,710.00 USD | 10,390.00 USD |
| `7D` | `0.1492` | 10,350,000.00 USD | 0.00 USD | 10,350,000.00 USD | 40,320.00 USD | 17,880.00 USD | 27,100.00 USD |
| `7D` | `0.1495` | 10,260,000.00 USD | 0.00 USD | 10,260,000.00 USD | 34,650.00 USD | 18,690.00 USD | 12,930.00 USD |
| `7D` | `0.1498` | 10,200,000.00 USD | 0.00 USD | 10,200,000.00 USD | 42,100.00 USD | 9,610.00 USD | 10,480.00 USD |
| `7D` | `0.1501` | 10,130,000.00 USD | 0.00 USD | 10,130,000.00 USD | 21,010.00 USD | 7,930.00 USD | 15,630.00 USD |
| `1D` | `0.1503` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 3,610.00 USD | 2,640.00 USD | 2,090.00 USD |
| `7D` | `0.1504` | 10,090,000.00 USD | 0.00 USD | 10,090,000.00 USD | 17,800.00 USD | 11,590.00 USD | 44,850.00 USD |
| `1D` | `0.1506` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 5,430.00 USD | 0.00 USD | 7,720.00 USD |
| `7D` | `0.1507` | 10,010,000.00 USD | 0.00 USD | 10,010,000.00 USD | 28,940.00 USD | 12,910.00 USD | 30,500.00 USD |
| `1D` | `0.1509` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 5,640.00 USD | 3,940.00 USD | 0.00 USD |
| `7D` | `0.1510` | 9,940,000.00 USD | 0.00 USD | 9,940,000.00 USD | 12,660.00 USD | 12,930.00 USD | 29,700.00 USD |
| `1D` | `0.1512` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 0.00 USD | 4,360.00 USD | 2,500.00 USD |
| `7D` | `0.1513` | 9,890,000.00 USD | 0.00 USD | 9,890,000.00 USD | 32,900.00 USD | 17,610.00 USD | 38,800.00 USD |
| `1D` | `0.1515` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 0.00 USD | 1,730.00 USD | 1,300.00 USD |
| `7D` | `0.1516` | 9,800,000.00 USD | 0.00 USD | 9,800,000.00 USD | 54,550.00 USD | 0.00 USD | 43,840.00 USD |
| `1D` | `0.1518` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 11,550.00 USD | 4,320.00 USD | 4,220.00 USD |
| `7D` | `0.1519` | 9,700,000.00 USD | 0.00 USD | 9,700,000.00 USD | 37,430.00 USD | 19,520.00 USD | 70,660.00 USD |
| `1D` | `0.1521` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 9,450.00 USD | 1,470.00 USD | 9,840.00 USD |
| `7D` | `0.1522` | 9,570,000.00 USD | 0.00 USD | 9,570,000.00 USD | 49,800.00 USD | 9,640.00 USD | 24,710.00 USD |
| `1D` | `0.1524` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 1,870.00 USD | 2,970.00 USD | 7,150.00 USD |
| `7D` | `0.1525` | 9,490,000.00 USD | 0.00 USD | 9,490,000.00 USD | 25,790.00 USD | 13,700.00 USD | 19,910.00 USD |
| `1D` | `0.1527` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 3,300.00 USD | 0.00 USD | 11,570.00 USD |
| `7D` | `0.1528` | 9,430,000.00 USD | 0.00 USD | 9,430,000.00 USD | 75,690.00 USD | 27,110.00 USD | 27,860.00 USD |
| `1D` | `0.1530` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 4,960.00 USD | 5,040.00 USD | 8,740.00 USD |
| `7D` | `0.1531` | 9,300,000.00 USD | 0.00 USD | 9,300,000.00 USD | 35,030.00 USD | 8,400.00 USD | 16,920.00 USD |
| `1D` | `0.1533` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 14,310.00 USD | 1,900.00 USD | 3,140.00 USD |
| `7D` | `0.1534` | 9,240,000.00 USD | 0.00 USD | 9,240,000.00 USD | 15,780.00 USD | 17,430.00 USD | 20,220.00 USD |
| `1D` | `0.1536` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 4,320.00 USD | 5,590.00 USD | 3,210.00 USD |
| `7D` | `0.1537` | 9,180,000.00 USD | 0.00 USD | 9,180,000.00 USD | 37,050.00 USD | 11,700.00 USD | 10,520.00 USD |
| `1D` | `0.1539` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 2,920.00 USD | 6,640.00 USD | 1,240.00 USD |
| `7D` | `0.1540` | 9,120,000.00 USD | 0.00 USD | 9,120,000.00 USD | 14,000.00 USD | 6,530.00 USD | 5,070.00 USD |
| `1D` | `0.1542` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 1,710.00 USD | 0.00 USD | 4,490.00 USD |
| `7D` | `0.1543` | 9,100,000.00 USD | 0.00 USD | 9,100,000.00 USD | 9,250.00 USD | 3,590.00 USD | 4,670.00 USD |
| `1D` | `0.1545` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 13,270.00 USD | 5,370.00 USD | 5,030.00 USD |
| `7D` | `0.1546` | 9,080,000.00 USD | 0.00 USD | 9,080,000.00 USD | 0.00 USD | 0.00 USD | 5,620.00 USD |
| `1D` | `0.1548` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 1,140.00 USD | 8,660.00 USD | 1,070.00 USD |
| `7D` | `0.1549` | 9,080,000.00 USD | 0.00 USD | 9,080,000.00 USD | 11,570.00 USD | 6,940.00 USD | 0.00 USD |
| `1D` | `0.1551` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 4,810.00 USD | 4,140.00 USD | 3,890.00 USD |
| `7D` | `0.1552` | 9,060,000.00 USD | 0.00 USD | 9,060,000.00 USD | 23,110.00 USD | 7,730.00 USD | 0.00 USD |
| `1D` | `0.1554` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 18,660.00 USD | 19,270.00 USD | 7,190.00 USD |
| `7D` | `0.1555` | 9,030,000.00 USD | 0.00 USD | 9,030,000.00 USD | 0.00 USD | 0.00 USD | 6,470.00 USD |
| `1D` | `0.1557` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 0.00 USD | 3,410.00 USD | 3,250.00 USD |
| `7D` | `0.1558` | 9,020,000.00 USD | 0.00 USD | 9,020,000.00 USD | 0.00 USD | 10,990.00 USD | 10,800.00 USD |
| `1D` | `0.1560` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 5,460.00 USD | 11,300.00 USD | 7,790.00 USD |
| `7D` | `0.1561` | 9,000,000.00 USD | 0.00 USD | 9,000,000.00 USD | 0.00 USD | 5,070.00 USD | 0.00 USD |
| `1D` | `0.1563` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 3,050.00 USD | 1,050.00 USD | 20,290.00 USD |
| `7D` | `0.1564` | 8,990,000.00 USD | 0.00 USD | 8,990,000.00 USD | 24,300.00 USD | 28,690.00 USD | 21,180.00 USD |
| `1D` | `0.1566` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 45,560.00 USD | 11,570.00 USD | 15,060.00 USD |
| `7D` | `0.1567` | 8,920,000.00 USD | 0.00 USD | 8,920,000.00 USD | 41,770.00 USD | 15,360.00 USD | 15,440.00 USD |
| `1D` | `0.1569` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 24,600.00 USD | 31,270.00 USD | 7,030.00 USD |
| `7D` | `0.1570` | 8,850,000.00 USD | 0.00 USD | 8,850,000.00 USD | 0.00 USD | 5,100.00 USD | 11,900.00 USD |
| `1D` | `0.1572` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 34,670.00 USD | 14,240.00 USD | 17,830.00 USD |
| `7D` | `0.1573` | 8,830,000.00 USD | 0.00 USD | 8,830,000.00 USD | 58,830.00 USD | 56,100.00 USD | 25,810.00 USD |
| `1D` | `0.1575` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 34,430.00 USD | 19,170.00 USD | 6,610.00 USD |
| `7D` | `0.1576` | 8,690,000.00 USD | 0.00 USD | 8,690,000.00 USD | 26,600.00 USD | 102,190.00 USD | 54,870.00 USD |
| `1D` | `0.1578` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 62,820.00 USD | 64,050.00 USD | 24,570.00 USD |
| `7D` | `0.1579` | 8,500,000.00 USD | 0.00 USD | 8,500,000.00 USD | 101,500.00 USD | 95,190.00 USD | 42,790.00 USD |
| `1D` | `0.1581` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 31,970.00 USD | 3,940.00 USD | 22,540.00 USD |
| `7D` | `0.1582` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 56,130.00 USD | 13,480.00 USD | 89,190.00 USD |
| `1D` | `0.1584` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 34,630.00 USD | 11,050.00 USD | 13,920.00 USD |
| `7D` | `0.1585` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 87,110.00 USD | 50,340.00 USD | 75,690.00 USD |
| `1D` | `0.1587` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 6,650.00 USD | 21,380.00 USD | 12,960.00 USD |
| `7D` | `0.1588` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 34,830.00 USD | 30,030.00 USD | 41,060.00 USD |
| `1D` | `0.1590` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 13,490.00 USD | 27,950.00 USD | 8,270.00 USD |
| `7D` | `0.1591` | 7,790,000.00 USD | 0.00 USD | 7,790,000.00 USD | 110,640.00 USD | 49,670.00 USD | 60,600.00 USD |
| `1D` | `0.1593` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 47,380.00 USD | 6,320.00 USD | 23,650.00 USD |
| `7D` | `0.1594` | 7,570,000.00 USD | 0.00 USD | 7,570,000.00 USD | 85,560.00 USD | 39,260.00 USD | 102,800.00 USD |
| `1D` | `0.1596` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 29,470.00 USD | 19,190.00 USD | 35,060.00 USD |
| `7D` | `0.1597` | 7,340,000.00 USD | 0.00 USD | 7,340,000.00 USD | 228,850.00 USD | 96,110.00 USD | 102,580.00 USD |
| `1D` | `0.1599` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 69,610.00 USD | 16,990.00 USD | 33,120.00 USD |
| `7D` | `0.1600` | 6,910,000.00 USD | 0.00 USD | 6,910,000.00 USD | 105,580.00 USD | 38,830.00 USD | 76,540.00 USD |
| `1D` | `0.1602` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 55,540.00 USD | 46,820.00 USD | 7,880.00 USD |
| `7D` | `0.1603` | 6,690,000.00 USD | 0.00 USD | 6,690,000.00 USD | 62,240.00 USD | 54,840.00 USD | 81,850.00 USD |
| `1D` | `0.1605` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 34,500.00 USD | 18,980.00 USD | 37,670.00 USD |
| `7D` | `0.1606` | 6,490,000.00 USD | 0.00 USD | 6,490,000.00 USD | 211,140.00 USD | 149,480.00 USD | 227,860.00 USD |
| `1D` | `0.1608` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 66,600.00 USD | 34,180.00 USD | 21,260.00 USD |
| `7D` | `0.1609` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 92,990.00 USD | 229,060.00 USD | 182,360.00 USD |
| `1D` | `0.1611` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 132,780.00 USD | 132,510.00 USD | 51,740.00 USD |
| `7D` | `0.1612` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 281,220.00 USD | 247,430.00 USD | 159,570.00 USD |
| `1D` | `0.1614` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 55,510.00 USD | 25,790.00 USD | 53,590.00 USD |
| `7D` | `0.1615` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 293,210.00 USD | 107,900.00 USD | 374,650.00 USD |
| `1D` | `0.1617` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 73,170.00 USD | 27,450.00 USD | 23,560.00 USD |
| `7D` | `0.1618` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 310,070.00 USD | 132,060.00 USD | 310,430.00 USD |
| `1D` | `0.1620` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 57,510.00 USD | 54,730.00 USD | 62,440.00 USD |
| `7D` | `0.1621` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 228,220.00 USD | 148,260.00 USD | 314,360.00 USD |
| `1D` | `0.1623` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 53,880.00 USD | 67,020.00 USD | 26,290.00 USD |
| `7D` | `0.1624` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 375,170.00 USD | 135,840.00 USD | 119,380.00 USD |
| `1D` | `0.1626` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 19,820.00 USD | 12,640.00 USD | 27,510.00 USD |
| `7D` | `0.1627` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 291,760.00 USD | 0.00 USD | 12,330.00 USD |
| `1D` | `0.1629` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 14,220.00 USD | 33,030.00 USD | 19,620.00 USD |
| `7D` | `0.1630` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 9,210.00 USD | 0.00 USD | 8,530.00 USD |
| `1D` | `0.1632` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 12,400.00 USD | 19,630.00 USD | 17,370.00 USD |
| `1D` | `0.1635` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 37,200.00 USD | 6,390.00 USD | 11,860.00 USD |
| `7D` | `0.1636` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 0.00 USD | 13,670.00 USD | 21,360.00 USD |
| `1D` | `0.1638` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 9,410.00 USD | 22,520.00 USD | 42,790.00 USD |
| `7D` | `0.1639` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 62,410.00 USD |
| `1D` | `0.1641` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 7,360.00 USD | 6,090.00 USD | 10,340.00 USD |
| `7D` | `0.1642` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 22,480.00 USD | 29,240.00 USD | 26,230.00 USD |
| `1D` | `0.1644` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 25,590.00 USD | 25,250.00 USD | 32,410.00 USD |
| `7D` | `0.1645` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 34,760.00 USD | 8,990.00 USD | 7,650.00 USD |
| `1D` | `0.1647` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 40,030.00 USD | 36,560.00 USD | 24,030.00 USD |
| `7D` | `0.1648` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD |
| `1D` | `0.1650` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 12,400.00 USD | 24,600.00 USD | 5,900.00 USD |
| `7D` | `0.1651` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 51,100.00 USD |
| `1D` | `0.1653` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 57,990.00 USD | 16,860.00 USD | 34,610.00 USD |
| `7D` | `0.1654` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 33,810.00 USD | 31,800.00 USD | 17,210.00 USD |
| `1D` | `0.1656` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 46,590.00 USD | 51,020.00 USD | 52,960.00 USD |
| `7D` | `0.1657` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 10,890.00 USD | 0.00 USD | 16,170.00 USD |
| `1D` | `0.1659` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 43,890.00 USD | 19,240.00 USD | 62,000.00 USD |
| `7D` | `0.1660` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 29,890.00 USD | 11,020.00 USD | 33,680.00 USD |
| `1D` | `0.1662` | 920,750.00 USD | 0.00 USD | 920,750.00 USD | 28,530.00 USD | 18,480.00 USD | 64,680.00 USD |
| `7D` | `0.1663` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 86,050.00 USD | 51,000.00 USD | 75,880.00 USD |
| `1D` | `0.1665` | 809,060.00 USD | 0.00 USD | 809,060.00 USD | 64,660.00 USD | 59,180.00 USD | 67,090.00 USD |
| `7D` | `0.1666` | 856,340.00 USD | 0.00 USD | 856,340.00 USD | 49,590.00 USD | 32,780.00 USD | 28,810.00 USD |
| `1D` | `0.1668` | 618,140.00 USD | 0.00 USD | 618,140.00 USD | 111,120.00 USD | 67,630.00 USD | 37,760.00 USD |
| `7D` | `0.1669` | 745,150.00 USD | 0.00 USD | 745,150.00 USD | 11,410.00 USD | 64,050.00 USD | 42,720.00 USD |
| `1D` | `0.1671` | 401,620.00 USD | 0.00 USD | 401,620.00 USD | 46,140.00 USD | 21,810.00 USD | 24,080.00 USD |
| `7D` | `0.1672` | 626,980.00 USD | 0.00 USD | 626,980.00 USD | 70,540.00 USD | 38,070.00 USD | 0.00 USD |
| `1D` | `0.1674` | 309,600.00 USD | 0.00 USD | 309,600.00 USD | 21,310.00 USD | 31,130.00 USD | 16,330.00 USD |
| `7D` | `0.1675` | 518,370.00 USD | 0.00 USD | 518,370.00 USD | 64,490.00 USD | 105,910.00 USD | 0.00 USD |
| `1D` | `0.1677` | 240,820.00 USD | 0.00 USD | 240,820.00 USD | 14,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1678` | 347,970.00 USD | 0.00 USD | 347,970.00 USD | 71,860.00 USD | 79,930.00 USD | 0.00 USD |
| `1D` | `0.1680` | 226,200.00 USD | 0.00 USD | 226,200.00 USD | 75,420.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1681` | 196,180.00 USD | 0.00 USD | 196,180.00 USD | 69,520.00 USD | 36,390.00 USD | 15,310.00 USD |
| `1D` | `0.1683` | 150,780.00 USD | 0.00 USD | 150,780.00 USD | 88,790.00 USD | 3,200.00 USD | 28,910.00 USD |
| `7D` | `0.1684` | 74,950.00 USD | 0.00 USD | 74,950.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD |
| `1D` | `0.1686` | 29,870.00 USD | 0.00 USD | 29,870.00 USD | 0.00 USD | 23,410.00 USD | 6,460.00 USD |
| `1D` | `0.1687` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1687` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1689` | 15,550.00 USD | 15,550.00 USD | 0.00 USD | 0.00 USD | 6,980.00 USD | 8,570.00 USD |
| `7D` | `0.1690` | 38,670.00 USD | 38,670.00 USD | 0.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD |
| `1D` | `0.1692` | 137,030.00 USD | 137,030.00 USD | 0.00 USD | 55,320.00 USD | 66,160.00 USD | 0.00 USD |
| `7D` | `0.1693` | 92,520.00 USD | 92,520.00 USD | 0.00 USD | 21,780.00 USD | 32,070.00 USD | 0.00 USD |
| `1D` | `0.1695` | 159,330.00 USD | 159,330.00 USD | 0.00 USD | 0.00 USD | 22,300.00 USD | 0.00 USD |
| `7D` | `0.1696` | 207,880.00 USD | 207,880.00 USD | 0.00 USD | 0.00 USD | 87,350.00 USD | 28,010.00 USD |
| `1D` | `0.1698` | 223,470.00 USD | 223,470.00 USD | 0.00 USD | 7,460.00 USD | 56,690.00 USD | 0.00 USD |
| `7D` | `0.1699` | 252,030.00 USD | 252,030.00 USD | 0.00 USD | 0.00 USD | 25,330.00 USD | 18,830.00 USD |
| `7D` | `0.1702` | 321,740.00 USD | 321,740.00 USD | 0.00 USD | 22,820.00 USD | 46,880.00 USD | 0.00 USD |
| `1D` | `0.1704` | 248,130.00 USD | 248,130.00 USD | 0.00 USD | 0.00 USD | 14,420.00 USD | 10,240.00 USD |
| `1D` | `0.1707` | 358,900.00 USD | 358,900.00 USD | 0.00 USD | 37,960.00 USD | 68,660.00 USD | 4,150.00 USD |
| `7D` | `0.1708` | 411,920.00 USD | 411,920.00 USD | 0.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD |
| `1D` | `0.1710` | 364,230.00 USD | 364,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,330.00 USD |
| `1D` | `0.1713` | 379,270.00 USD | 379,270.00 USD | 0.00 USD | 0.00 USD | 15,040.00 USD | 0.00 USD |
| `7D` | `0.1714` | 453,940.00 USD | 453,940.00 USD | 0.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD |
| `1D` | `0.1716` | 404,880.00 USD | 404,880.00 USD | 0.00 USD | 0.00 USD | 25,600.00 USD | 0.00 USD |
| `1D` | `0.1719` | 436,620.00 USD | 436,620.00 USD | 0.00 USD | 23,230.00 USD | 8,520.00 USD | 0.00 USD |
| `7D` | `0.1720` | 608,300.00 USD | 608,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 154,360.00 USD |
| `1D` | `0.1722` | 553,600.00 USD | 553,600.00 USD | 0.00 USD | 80,460.00 USD | 16,860.00 USD | 19,660.00 USD |
| `7D` | `0.1723` | 853,960.00 USD | 853,960.00 USD | 0.00 USD | 74,150.00 USD | 0.00 USD | 171,510.00 USD |
| `1D` | `0.1725` | 569,490.00 USD | 569,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,890.00 USD |
| `1D` | `0.1728` | 588,300.00 USD | 588,300.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD |
| `7D` | `0.1729` | 991,550.00 USD | 991,550.00 USD | 0.00 USD | 137,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1732` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 338,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1734` | 598,370.00 USD | 598,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,060.00 USD |
| `1D` | `0.1737` | 637,430.00 USD | 637,430.00 USD | 0.00 USD | 29,560.00 USD | 9,510.00 USD | 0.00 USD |
| `7D` | `0.1738` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 83,810.00 USD |
| `1D` | `0.1740` | 647,070.00 USD | 647,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,640.00 USD |
| `1D` | `0.1743` | 659,700.00 USD | 659,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,630.00 USD |
| `7D` | `0.1744` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1746` | 680,190.00 USD | 680,190.00 USD | 0.00 USD | 8,530.00 USD | 2,460.00 USD | 9,500.00 USD |
| `1D` | `0.1749` | 798,890.00 USD | 798,890.00 USD | 0.00 USD | 80,070.00 USD | 2,280.00 USD | 36,350.00 USD |
| `7D` | `0.1750` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 167,500.00 USD |
| `1D` | `0.1752` | 851,510.00 USD | 851,510.00 USD | 0.00 USD | 19,990.00 USD | 0.00 USD | 32,640.00 USD |
| `7D` | `0.1753` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 191,160.00 USD |
| `1D` | `0.1755` | 904,990.00 USD | 904,990.00 USD | 0.00 USD | 14,290.00 USD | 16,650.00 USD | 22,550.00 USD |
| `7D` | `0.1756` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 75,620.00 USD | 0.00 USD | 97,990.00 USD |
| `1D` | `0.1758` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 77,350.00 USD | 31,940.00 USD | 45,950.00 USD |
| `7D` | `0.1759` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 217,800.00 USD | 38,670.00 USD | 0.00 USD |
| `1D` | `0.1761` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 53,970.00 USD | 88,390.00 USD | 50,220.00 USD |
| `7D` | `0.1762` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 289,660.00 USD | 196,430.00 USD | 32,350.00 USD |
| `1D` | `0.1764` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 72,600.00 USD | 25,840.00 USD | 61,480.00 USD |
| `7D` | `0.1765` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 154,540.00 USD | 175,970.00 USD | 48,870.00 USD |
| `1D` | `0.1767` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 39,860.00 USD | 52,820.00 USD | 52,230.00 USD |
| `7D` | `0.1768` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 161,560.00 USD | 138,440.00 USD | 23,040.00 USD |
| `1D` | `0.1770` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 36,140.00 USD | 47,810.00 USD | 38,500.00 USD |
| `7D` | `0.1771` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 69,030.00 USD | 138,810.00 USD | 21,360.00 USD |
| `1D` | `0.1773` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 30,810.00 USD | 28,980.00 USD | 22,840.00 USD |
| `7D` | `0.1774` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 148,780.00 USD | 115,280.00 USD | 0.00 USD |
| `1D` | `0.1776` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 85,560.00 USD | 19,390.00 USD | 21,010.00 USD |
| `7D` | `0.1777` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 67,350.00 USD | 40,700.00 USD | 59,520.00 USD |
| `1D` | `0.1779` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 27,480.00 USD | 77,730.00 USD | 25,130.00 USD |
| `7D` | `0.1780` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 52,730.00 USD | 38,910.00 USD | 97,990.00 USD |
| `1D` | `0.1782` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 46,310.00 USD | 14,240.00 USD | 47,040.00 USD |
| `7D` | `0.1783` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 117,540.00 USD | 56,000.00 USD | 21,910.00 USD |
| `1D` | `0.1785` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 96,920.00 USD | 51,600.00 USD | 14,990.00 USD |
| `7D` | `0.1786` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 129,440.00 USD | 55,090.00 USD | 14,040.00 USD |
| `1D` | `0.1788` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 35,520.00 USD | 42,480.00 USD | 45,180.00 USD |
| `7D` | `0.1789` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 48,810.00 USD | 7,150.00 USD | 0.00 USD |
| `1D` | `0.1791` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 41,020.00 USD | 19,320.00 USD | 18,080.00 USD |
| `7D` | `0.1792` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 134,000.00 USD | 39,820.00 USD | 3,940.00 USD |
| `1D` | `0.1794` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 45,400.00 USD | 60,380.00 USD | 20,780.00 USD |
| `7D` | `0.1795` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 17,130.00 USD | 19,870.00 USD | 44,450.00 USD |
| `1D` | `0.1797` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 41,960.00 USD | 22,110.00 USD | 36,970.00 USD |
| `7D` | `0.1798` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 6,240.00 USD | 27,010.00 USD |
| `1D` | `0.1800` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 10,230.00 USD | 8,690.00 USD | 25,360.00 USD |
| `7D` | `0.1801` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 6,490.00 USD | 40,090.00 USD | 46,450.00 USD |
| `1D` | `0.1803` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 16,490.00 USD | 35,880.00 USD | 28,690.00 USD |
| `7D` | `0.1804` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 28,790.00 USD | 27,450.00 USD | 14,740.00 USD |
| `1D` | `0.1806` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 21,330.00 USD | 14,370.00 USD | 21,090.00 USD |
| `7D` | `0.1807` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 11,410.00 USD | 63,170.00 USD | 67,160.00 USD |
| `1D` | `0.1809` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 27,060.00 USD | 27,370.00 USD | 32,600.00 USD |
| `7D` | `0.1810` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 79,380.00 USD | 30,940.00 USD | 12,950.00 USD |
| `1D` | `0.1812` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 56,360.00 USD | 44,030.00 USD | 38,190.00 USD |
| `7D` | `0.1813` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 32,530.00 USD | 15,780.00 USD | 56,130.00 USD |
| `1D` | `0.1815` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 12,800.00 USD | 3,320.00 USD | 11,550.00 USD |
| `7D` | `0.1816` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 46,430.00 USD | 21,200.00 USD | 25,980.00 USD |
| `1D` | `0.1818` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 37,120.00 USD | 11,780.00 USD | 32,620.00 USD |
| `7D` | `0.1819` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 65,350.00 USD | 24,720.00 USD | 43,100.00 USD |
| `1D` | `0.1821` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 21,220.00 USD | 19,510.00 USD | 9,370.00 USD |
| `7D` | `0.1822` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 46,760.00 USD | 36,230.00 USD | 92,280.00 USD |
| `1D` | `0.1824` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 20,050.00 USD | 18,270.00 USD | 13,610.00 USD |
| `7D` | `0.1825` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 61,720.00 USD | 17,120.00 USD | 12,140.00 USD |
| `1D` | `0.1827` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 21,440.00 USD | 6,860.00 USD | 4,170.00 USD |
| `7D` | `0.1828` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 51,470.00 USD | 24,320.00 USD | 69,840.00 USD |
| `1D` | `0.1830` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 4,510.00 USD | 5,690.00 USD |
| `7D` | `0.1831` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 85,970.00 USD | 21,930.00 USD | 63,170.00 USD |
| `1D` | `0.1833` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,630.00 USD |
| `7D` | `0.1834` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 165,640.00 USD | 47,980.00 USD | 51,750.00 USD |
| `1D` | `0.1836` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 3,610.00 USD | 0.00 USD | 728.16 USD |
| `7D` | `0.1837` | 6,940,000.00 USD | 6,940,000.00 USD | 0.00 USD | 72,930.00 USD | 76,140.00 USD | 83,480.00 USD |
| `1D` | `0.1839` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 2,640.00 USD | 7,830.00 USD |
| `7D` | `0.1840` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 98,270.00 USD | 47,250.00 USD | 80,190.00 USD |
| `1D` | `0.1842` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 13,150.00 USD | 2,690.00 USD | 5,850.00 USD |
| `7D` | `0.1843` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 86,180.00 USD | 18,570.00 USD | 105,350.00 USD |
| `1D` | `0.1845` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 5,640.00 USD | 5,640.00 USD | 14,680.00 USD |
| `7D` | `0.1846` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 8,330.00 USD | 45,450.00 USD | 135,450.00 USD |
| `1D` | `0.1848` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 4,680.00 USD | 4,360.00 USD | 9,340.00 USD |
| `7D` | `0.1849` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 62,030.00 USD | 79,580.00 USD | 38,800.00 USD |
| `1D` | `0.1851` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD | 1,300.00 USD |
| `7D` | `0.1852` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 153,970.00 USD | 9,590.00 USD | 234,380.00 USD |
| `1D` | `0.1854` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 4,290.00 USD | 1,690.00 USD | 8,660.00 USD |
| `7D` | `0.1855` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 58,210.00 USD | 10,160.00 USD | 94,330.00 USD |
| `1D` | `0.1857` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 7,260.00 USD | 2,630.00 USD | 7,600.00 USD |
| `7D` | `0.1858` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 96,280.00 USD | 46,830.00 USD | 118,720.00 USD |
| `1D` | `0.1860` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 9,450.00 USD | 4,440.00 USD | 4,330.00 USD |
| `7D` | `0.1861` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 99,880.00 USD | 55,030.00 USD | 21,120.00 USD |
| `1D` | `0.1863` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD | 8,320.00 USD |
| `7D` | `0.1864` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 52,190.00 USD | 58,680.00 USD | 61,380.00 USD |
| `1D` | `0.1866` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 3,300.00 USD | 0.00 USD | 5,140.00 USD |
| `7D` | `0.1867` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 102,440.00 USD | 43,150.00 USD | 52,870.00 USD |
| `1D` | `0.1869` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 4,960.00 USD | 1,740.00 USD | 9,730.00 USD |
| `7D` | `0.1870` | 9,470,000.00 USD | 9,470,000.00 USD | 0.00 USD | 165,360.00 USD | 83,890.00 USD | 101,310.00 USD |
| `1D` | `0.1872` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 12,350.00 USD | 5,200.00 USD | 5,320.00 USD |
| `7D` | `0.1873` | 9,730,000.00 USD | 9,730,000.00 USD | 0.00 USD | 72,410.00 USD | 101,000.00 USD | 90,790.00 USD |
| `1D` | `0.1875` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 1,960.00 USD | 2,820.00 USD | 2,290.00 USD |
| `7D` | `0.1876` | 9,830,000.00 USD | 9,830,000.00 USD | 0.00 USD | 59,490.00 USD | 34,260.00 USD | 10,330.00 USD |
| `1D` | `0.1878` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 4,320.00 USD | 2,760.00 USD | 918.24 USD |
| `7D` | `0.1879` | 9,990,000.00 USD | 9,990,000.00 USD | 0.00 USD | 57,250.00 USD | 52,690.00 USD | 48,730.00 USD |
| `1D` | `0.1881` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 2,920.00 USD | 6,640.00 USD | 1,240.00 USD |
| `7D` | `0.1882` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 14,000.00 USD | 23,830.00 USD | 59,250.00 USD |
| `1D` | `0.1884` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 1,710.00 USD | 0.00 USD | 4,490.00 USD |
| `7D` | `0.1885` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 19,810.00 USD | 31,900.00 USD | 4,670.00 USD |
| `1D` | `0.1887` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 13,270.00 USD | 4,390.00 USD | 1,730.00 USD |
| `7D` | `0.1888` | 10,260,000.00 USD | 10,260,000.00 USD | 0.00 USD | 13,720.00 USD | 17,330.00 USD | 83,540.00 USD |
| `1D` | `0.1890` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 7,790.00 USD | 3,300.00 USD |
| `7D` | `0.1891` | 10,310,000.00 USD | 10,310,000.00 USD | 0.00 USD | 36,740.00 USD | 0.00 USD | 17,340.00 USD |
| `1D` | `0.1893` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 5,950.00 USD | 3,490.00 USD | 1,070.00 USD |
| `7D` | `0.1894` | 10,410,000.00 USD | 10,410,000.00 USD | 0.00 USD | 69,540.00 USD | 12,420.00 USD | 16,820.00 USD |
| `1D` | `0.1896` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 4,500.00 USD | 2,500.00 USD | 3,890.00 USD |
| `7D` | `0.1897` | 10,500,000.00 USD | 10,500,000.00 USD | 0.00 USD | 25,640.00 USD | 39,120.00 USD | 25,080.00 USD |
| `1D` | `0.1899` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 7,270.00 USD | 19,270.00 USD | 3,660.00 USD |
| `7D` | `0.1900` | 10,550,000.00 USD | 10,550,000.00 USD | 0.00 USD | 11,530.00 USD | 21,370.00 USD | 14,020.00 USD |
| `1D` | `0.1902` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 6,890.00 USD | 3,410.00 USD | 6,780.00 USD |
| `7D` | `0.1903` | 10,590,000.00 USD | 10,590,000.00 USD | 0.00 USD | 14,330.00 USD | 11,220.00 USD | 10,800.00 USD |
| `1D` | `0.1905` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 2,490.00 USD | 8,320.00 USD | 7,790.00 USD |
| `7D` | `0.1906` | 10,670,000.00 USD | 10,670,000.00 USD | 0.00 USD | 18,470.00 USD | 27,580.00 USD | 33,590.00 USD |
| `7D` | `0.1909` | 10,730,000.00 USD | 10,730,000.00 USD | 0.00 USD | 15,470.00 USD | 29,160.00 USD | 19,220.00 USD |
| `7D` | `0.1912` | 10,750,000.00 USD | 10,750,000.00 USD | 0.00 USD | 0.00 USD | 15,240.00 USD | 0.00 USD |
| `7D` | `0.1915` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 7,460.00 USD | 5,300.00 USD | 0.00 USD |
| `7D` | `0.1918` | 10,780,000.00 USD | 10,780,000.00 USD | 0.00 USD | 0.00 USD | 11,840.00 USD | 11,900.00 USD |
| `7D` | `0.1924` | 10,800,000.00 USD | 10,800,000.00 USD | 0.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD |
| `7D` | `0.1927` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 11,600.00 USD | 13,630.00 USD | 0.00 USD |
| `7D` | `0.1945` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `208.36M` | Total OI Tokens: `1,233,672,360.2 ARB`
  * 1h OI Change: `+0.11%` | 4h OI Change: `-2.92%` | 24h OI Change: `-13.79%`
  * Exchange Breakdown: Binance=`47.26M` | Bybit=`28.85M` | OKX=`16.68M` | Hyperliquid=`15.02M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `8.21K` | Last 24h: `10.97K` | Last 3d: `22.34K` | Last 7d: `43.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0092%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0074%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0079%` | **USDT Bitget** | `0.0093%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `58.00%` | `42.00%` | `1.38` | 865,800.00 USD |
| `15M` | `Binance` | `62.83%` | `37.17%` | `1.69` | 308,470.00 USD |
| `15M` | `OKX` | `41.64%` | `58.36%` | `0.71` | 85,450.00 USD |
| `15M` | `Bybit` | `62.45%` | `37.55%` | `1.66` | 74,660.00 USD |
| `15M` | `KuCoin` | `59.22%` | `40.78%` | `1.45` | 1,390.00 USD |
| `15M` | `Gate` | `37.44%` | `62.56%` | `0.60` | 1,550.00 USD |
| `15M` | `Bitget` | `55.76%` | `44.24%` | `1.26` | 78,440.00 USD |
| `15M` | `BingX` | `53.27%` | `46.73%` | `1.14` | 78,350.00 USD |
| `15M` | `MEXC` | `89.59%` | `10.41%` | `8.61` | 28,460.00 USD |
| `15M` | `Bitunix` | `68.62%` | `31.38%` | `2.19` | 8,740.00 USD |
| `15M` | `Hyperliquid` | `52.02%` | `47.98%` | `1.08` | 3,290.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.14%` | `53.86%` | `0.86` | 157,890.00 USD |
| `15M` | `Crypto.com` | `0%` | `100%` | `0.00` | 0.22 USD |
| `15M` | `WhiteBIT` | `86.62%` | `13.38%` | `6.47` | 38,350.00 USD |
| `15M` | `HTX` | `84.76%` | `15.24%` | `5.56` | 1.16 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `100%` | `0.00` | 473.20 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 5.06 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 263.98 USD |
| `15M` | `Whale Positions` | `62.83%` | `37.17%` | `1.69` | 308,470.00 USD |
| `15M` | `Global Accounts` | `58.00%` | `42.00%` | `1.38` | 865,800.00 USD |
| `1H` | `ARB` | `52.68%` | `47.32%` | `1.11` | 4,140,000.00 USD |
| `1H` | `Binance` | `51.91%` | `48.09%` | `1.08` | 1,590,000.00 USD |
| `1H` | `OKX` | `48.02%` | `51.98%` | `0.92` | 372,020.00 USD |
| `1H` | `Bybit` | `50.71%` | `49.29%` | `1.03` | 403,650.00 USD |
| `1H` | `KuCoin` | `57.94%` | `42.06%` | `1.38` | 12,420.00 USD |
| `1H` | `Gate` | `52.79%` | `47.21%` | `1.12` | 39,280.00 USD |
| `1H` | `Bitget` | `66.39%` | `33.61%` | `1.98` | 184,530.00 USD |
| `1H` | `BingX` | `52.41%` | `47.59%` | `1.10` | 307,390.00 USD |
| `1H` | `MEXC` | `49.64%` | `50.36%` | `0.99` | 198,650.00 USD |
| `1H` | `Bitunix` | `56.22%` | `43.78%` | `1.28` | 38,390.00 USD |
| `1H` | `Hyperliquid` | `35.07%` | `64.93%` | `0.54` | 14,890.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.67%` | `52.33%` | `0.91` | 819,940.00 USD |
| `1H` | `Crypto.com` | `0%` | `100%` | `0.00` | 0.44 USD |
| `1H` | `WhiteBIT` | `94.03%` | `5.97%` | `15.75` | 148,550.00 USD |
| `1H` | `HTX` | `14.02%` | `85.98%` | `0.16` | 232.62 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `48.93%` | `51.07%` | `0.96` | 3,560.00 USD |
| `1H` | `Aster` | `0%` | `100%` | `0.00` | 5.06 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `17.6%` | `82.4%` | `0.21` | 1,600.00 USD |
| `1H` | `Whale Positions` | `51.91%` | `48.09%` | `1.08` | 1,590,000.00 USD |
| `1H` | `Global Accounts` | `52.68%` | `47.32%` | `1.11` | 4,140,000.00 USD |
| `4H` | `ARB` | `49.79%` | `50.21%` | `0.99` | 22,250,000.00 USD |
| `4H` | `Binance` | `48.12%` | `51.88%` | `0.93` | 8,120,000.00 USD |
| `4H` | `OKX` | `48.68%` | `51.32%` | `0.95` | 2,600,000.00 USD |
| `4H` | `Bybit` | `49.45%` | `50.55%` | `0.98` | 2,280,000.00 USD |
| `4H` | `KuCoin` | `30.97%` | `69.03%` | `0.45` | 84,870.00 USD |
| `4H` | `Gate` | `51.93%` | `48.07%` | `1.08` | 230,120.00 USD |
| `4H` | `Bitget` | `53.95%` | `46.05%` | `1.17` | 573,690.00 USD |
| `4H` | `BingX` | `41.71%` | `58.29%` | `0.72` | 1,660,000.00 USD |
| `4H` | `MEXC` | `48.84%` | `51.16%` | `0.95` | 1,520,000.00 USD |
| `4H` | `Bitunix` | `53.29%` | `46.71%` | `1.14` | 208,290.00 USD |
| `4H` | `Hyperliquid` | `74.34%` | `25.66%` | `2.90` | 260,610.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.9%` | `51.1%` | `0.96` | 4,070,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `100%` | `0.00` | 3.02 USD |
| `4H` | `WhiteBIT` | `94.28%` | `5.72%` | `16.48` | 622,980.00 USD |
| `4H` | `HTX` | `45.42%` | `54.58%` | `0.83` | 3,540.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `25.71%` | `74.29%` | `0.35` | 11,310.00 USD |
| `4H` | `Aster` | `8.34%` | `91.66%` | `0.09` | 2,430.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `49.86%` | `50.14%` | `0.99` | 12,480.00 USD |
| `4H` | `Whale Positions` | `48.12%` | `51.88%` | `0.93` | 8,120,000.00 USD |
| `4H` | `Global Accounts` | `49.79%` | `50.21%` | `0.99` | 22,250,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1722` | `0.1719` | `0.1722` | `0.1724` | `0.1714` | 868,922.61 USD | 333,299.44 USD | 535,623.17 USD | -202,323.73 USD | `-23.28%` | `11B / 37S` |
| `0:00 UTC` | `0.1715` | `0.1718` | `0.1715` | `0.1727` | `0.1712` | 1,082,802.27 USD | 363,691.86 USD | 719,110.40 USD | -355,418.54 USD | `-32.82%` | `13B / 48S` |
| `5:00 UTC` | `0.1711` | `0.1711` | `0.1711` | `0.1716` | `0.1708` | 800,876.04 USD | 410,736.84 USD | 390,139.20 USD | 20,597.64 USD | `+2.57%` | `7B / 12S` |
| `0:00 UTC` | `0.1710` | `0.1702` | `0.1710` | `0.1719` | `0.1689` | 1,300,882.78 USD | 531,501.17 USD | 769,381.61 USD | -237,880.44 USD | `-18.29%` | `17B / 38S` |
| `5:00 UTC` | `0.1689` | `0.1689` | `0.1689` | `0.1697` | `0.1682` | 1,292,914.43 USD | 712,068.28 USD | 580,846.15 USD | 131,222.13 USD | `+10.15%` | `38B / 24S` |
| `0:00 UTC` | `0.1690` | `0.1697` | `0.1690` | `0.1704` | `0.1690` | 952,197.22 USD | 428,970.00 USD | 523,227.22 USD | -94,257.22 USD | `-9.90%` | `28B / 31S` |
| `5:00 UTC` | `0.1686` | `0.1691` | `0.1686` | `0.1698` | `0.1685` | 581,095.74 USD | 286,225.77 USD | 294,869.97 USD | -8,644.20 USD | `-1.49%` | `37B / 26S` |
| `0:00 UTC` | `0.1678` | `0.1678` | `0.1678` | `0.1689` | `0.1673` | 1,127,023.46 USD | 573,365.61 USD | 553,657.86 USD | 19,707.75 USD | `+1.75%` | `27B / 19S` |
| `5:00 UTC` | `0.1687` | `0.1687` | `0.1687` | `0.1691` | `0.1680` | 541,507.84 USD | 294,376.97 USD | 247,130.87 USD | 47,246.11 USD | `+8.72%` | `31B / 8S` |
| `0:00 UTC` | `0.1687` | `0.1684` | `0.1687` | `0.1688` | `0.1681` | 84,278.10 USD | 36,792.21 USD | 47,485.88 USD | -10,693.67 USD | `-12.69%` | `18B / 16S` |

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
| `5m` | 1,390.00 USD | 92,290.00 USD | **`ACCUMULATION`** |
| `15m` | -30,850.00 USD | 273,260.00 USD | **`ACCUMULATION`** |
| `30m` | -63,130.00 USD | -52,410.00 USD | **`DISTRIBUTION`** |
| `1h` | 3,890.00 USD | 281,500.00 USD | **`ACCUMULATION`** |
| `2h` | -185,090.00 USD | -1,070,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 65,100.00 USD | -2,190,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 55,830.00 USD | -3,410,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 7,000.00 USD | -4,210,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 174,570.00 USD | -4,770,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -392,030.00 USD | -6,070,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -4,650,000.00 USD | -29,400,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -31,970,000.00 USD | -163,480,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+1.39K` | 15m=`-30.85K` | 1h=`+3.89K` | 24h=`-392.03K`
* Futures Capital Netflows: 5m=`+92.29K` | 15m=`+273.26K` | 1h=`+281.50K` | 24h=`-6.07M`
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
  * `2026-10-30 00:17:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:29:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
