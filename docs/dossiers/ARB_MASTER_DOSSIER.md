# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 00:02:04 IST` (`2026-10-29 18:32:04 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1695` | `0.1698` | `0.1691` | `0.1694` | `1,054,977` | 178,571.48 USD | -7,824.31 USD | `-4.38%` | -5,451,758.10 USD | `+0.29` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `0.1694` | `0.1698` | `0.1688` | `0.1688` | `1,049,726` | 177,732.46 USD | 46,317.62 USD | `+26.06%` | -5,405,440.48 USD | `+0.70` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1689` | `0.1689` | `0.1688` | `0.1689` | `210,643` | 35,569.64 USD | 18,496.34 USD | `+52.00%` | -5,386,944.15 USD | `+0.39` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1694` | `0.1697` | `0.1681` | `0.1696` | `7,652,937` | 1,292,914.43 USD | 131,222.13 USD | `+10.15%` | -5,349,676.57 USD | `+1.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1696` | `0.1704` | `0.1689` | `0.1695` | `5,610,985` | 952,197.22 USD | -94,257.22 USD | `-9.90%` | -5,443,933.79 USD | `+0.15` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1695` | `0.1698` | `0.1688` | `0.1689` | `2,315,346` | 391,873.58 USD | 56,989.65 USD | `+14.54%` | -5,386,944.15 USD | `+1.08` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1745` | `0.1759` | `0.1714` | `0.1724` | `28,115,276` | 4,875,921.02 USD | -1,037,219.52 USD | `-21.27%` | -4,109,099.99 USD | `-2.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1724` | `0.1727` | `0.1681` | `0.1696` | `26,281,427` | 4,477,475.52 USD | -441,479.21 USD | `-9.86%` | -4,550,579.20 USD | `-0.59` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1696` | `0.1704` | `0.1688` | `0.1689` | `7,926,331` | 1,344,070.79 USD | -37,267.58 USD | `-2.77%` | -4,587,846.78 USD | `+0.38` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,634,787.89 USD | `-0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,872,916.24 USD | `-1.36` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1681` | `0.1689` | `62,319,741` | 10,696,911.02 USD | -1,516,522.62 USD | `-14.18%` | -4,389,438.86 USD | `-1.39` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1721` | `0.1729` | `0.1635` | `0.1652` | `91,809,989` | 15,344,891.97 USD | 203,909.29 USD | `+1.33%` | -294,464.16 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1652` | `0.1687` | `0.1623` | `0.1631` | `68,085,678` | 11,252,816.65 USD | -909,329.92 USD | `-8.08%` | -1,203,794.08 USD | `-1.11` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,634,787.89 USD | `-0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,872,916.24 USD | `-1.36` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1681` | `0.1689` | `62,319,741` | 10,696,911.02 USD | -1,516,522.62 USD | `-14.18%` | -4,389,438.86 USD | `-1.39` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:55:43 IST` |

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
  * 24H Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+5.71%`) | Long MP=`0.1598` (Vol: 141,700.00 USD, Dist: `--5.32%`)
  * 48H Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+5.71%`) | Long MP=`0.1598` (Vol: 154,300.00 USD, Dist: `--5.32%`)
  * 3D Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+5.71%`) | Long MP=`0.1598` (Vol: 205,900.00 USD, Dist: `--5.32%`)
  * 7D Horizon: Short MP=`0.1834` (Vol: 181,500.00 USD, Dist: `+8.64%`) | Long MP=`0.1616` (Vol: 292,500.00 USD, Dist: `--4.24%`)
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
| `7D` | `Long Liquidation` | `0.1461` | 10,780,000.00 USD | 10,780,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1464` | 10,780,000.00 USD | 10,780,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 193,660.00 USD | 814,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1467` | 10,770,000.00 USD | 10,770,000.00 USD | 9,720.00 USD | 9,180.00 USD | 4,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1470` | 10,750,000.00 USD | 10,750,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1473` | 10,740,000.00 USD | 10,740,000.00 USD | 6,490.00 USD | 5,400.00 USD | 5,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 73,750.00 USD | 620,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1476` | 10,720,000.00 USD | 10,720,000.00 USD | 0.00 USD | 14,780.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1479` | 10,700,000.00 USD | 10,700,000.00 USD | 0.00 USD | 39,730.00 USD | 14,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1482` | 10,650,000.00 USD | 10,650,000.00 USD | 41,960.00 USD | 20,720.00 USD | 27,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1485` | 10,560,000.00 USD | 10,560,000.00 USD | 16,180.00 USD | 7,340.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,890.00 USD | 546,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1488` | 10,490,000.00 USD | 10,490,000.00 USD | 20,860.00 USD | 3,130.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1491` | 10,460,000.00 USD | 10,460,000.00 USD | 33,540.00 USD | 17,020.00 USD | 20,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1494` | 10,390,000.00 USD | 10,390,000.00 USD | 34,220.00 USD | 9,890.00 USD | 14,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 35,380.00 USD | 543,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1497` | 10,330,000.00 USD | 10,330,000.00 USD | 20,880.00 USD | 17,180.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1500` | 10,280,000.00 USD | 10,280,000.00 USD | 46,820.00 USD | 5,810.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1503` | 10,210,000.00 USD | 10,210,000.00 USD | 11,490.00 USD | 13,450.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1505` | 102,290.00 USD | 508,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1506` | 10,170,000.00 USD | 10,170,000.00 USD | 33,170.00 USD | 18,020.00 USD | 65,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1509` | 10,060,000.00 USD | 10,060,000.00 USD | 17,340.00 USD | 9,550.00 USD | 24,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1511` | 4,460,000.00 USD | 4,460,000.00 USD | 5,640.00 USD | 9,380.00 USD | 5,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1512` | 10,010,000.00 USD | 10,010,000.00 USD | 18,600.00 USD | 8,620.00 USD | 26,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1514` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 1,730.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1515` | 9,950,000.00 USD | 9,950,000.00 USD | 53,430.00 USD | 13,330.00 USD | 53,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 4,180.00 USD | 406,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1517` | 4,440,000.00 USD | 4,440,000.00 USD | 4,860.00 USD | 1,690.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1518` | 9,830,000.00 USD | 9,830,000.00 USD | 46,830.00 USD | 15,160.00 USD | 64,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1520` | 4,420,000.00 USD | 4,420,000.00 USD | 7,500.00 USD | 4,100.00 USD | 5,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1521` | 9,710,000.00 USD | 9,710,000.00 USD | 38,960.00 USD | 6,920.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1523` | 4,410,000.00 USD | 4,410,000.00 USD | 5,860.00 USD | 2,970.00 USD | 3,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1524` | 9,620,000.00 USD | 9,620,000.00 USD | 37,550.00 USD | 13,950.00 USD | 11,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1525` | 45,320.00 USD | 401,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1526` | 4,390,000.00 USD | 4,390,000.00 USD | 5,170.00 USD | 0.00 USD | 11,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1527` | 9,560,000.00 USD | 9,560,000.00 USD | 56,950.00 USD | 30,410.00 USD | 33,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1529` | 4,380,000.00 USD | 4,380,000.00 USD | 4,960.00 USD | 1,740.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1530` | 9,440,000.00 USD | 9,440,000.00 USD | 54,790.00 USD | 9,880.00 USD | 16,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1532` | 4,360,000.00 USD | 4,360,000.00 USD | 12,350.00 USD | 5,200.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1533` | 9,360,000.00 USD | 9,360,000.00 USD | 10,760.00 USD | 16,570.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1535` | 4,340,000.00 USD | 4,340,000.00 USD | 4,630.00 USD | 5,590.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 19,400.00 USD | 356,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1536` | 9,310,000.00 USD | 9,310,000.00 USD | 37,160.00 USD | 2,910.00 USD | 13,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1538` | 4,320,000.00 USD | 4,320,000.00 USD | 4,530.00 USD | 3,160.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1539` | 9,250,000.00 USD | 9,250,000.00 USD | 22,990.00 USD | 18,230.00 USD | 5,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1541` | 4,310,000.00 USD | 4,310,000.00 USD | 4,630.00 USD | 4,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1542` | 9,210,000.00 USD | 9,210,000.00 USD | 0.00 USD | 3,590.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1544` | 4,300,000.00 USD | 4,300,000.00 USD | 17,310.00 USD | 5,370.00 USD | 6,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1545` | 9,200,000.00 USD | 9,200,000.00 USD | 9,250.00 USD | 0.00 USD | 5,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1545` | 26,170.00 USD | 337,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1547` | 4,270,000.00 USD | 4,270,000.00 USD | 1,140.00 USD | 6,820.00 USD | 7,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1548` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1550` | 4,250,000.00 USD | 4,250,000.00 USD | 4,810.00 USD | 4,460.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1551` | 9,180,000.00 USD | 9,180,000.00 USD | 34,670.00 USD | 11,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1553` | 4,240,000.00 USD | 4,240,000.00 USD | 11,770.00 USD | 20,800.00 USD | 6,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1554` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 0.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1555` | 40,060.00 USD | 311,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1556` | 4,200,000.00 USD | 4,200,000.00 USD | 6,890.00 USD | 3,410.00 USD | 6,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1557` | 9,130,000.00 USD | 9,130,000.00 USD | 0.00 USD | 4,510.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1559` | 4,190,000.00 USD | 4,190,000.00 USD | 2,490.00 USD | 8,320.00 USD | 7,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1560` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 6,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1562` | 4,170,000.00 USD | 4,170,000.00 USD | 6,020.00 USD | 4,020.00 USD | 10,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1563` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 19,950.00 USD | 9,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1565` | 4,150,000.00 USD | 4,150,000.00 USD | 24,770.00 USD | 11,570.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1565` | 21,460.00 USD | 271,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1566` | 9,080,000.00 USD | 9,080,000.00 USD | 50,480.00 USD | 29,160.00 USD | 26,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1568` | 4,100,000.00 USD | 4,100,000.00 USD | 34,400.00 USD | 26,770.00 USD | 17,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1569` | 8,970,000.00 USD | 8,970,000.00 USD | 15,590.00 USD | 5,100.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1571` | 4,020,000.00 USD | 4,020,000.00 USD | 32,670.00 USD | 11,300.00 USD | 10,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1572` | 8,940,000.00 USD | 8,940,000.00 USD | 40,760.00 USD | 34,450.00 USD | 17,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1574` | 3,960,000.00 USD | 3,960,000.00 USD | 34,240.00 USD | 13,520.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1575` | 8,850,000.00 USD | 8,850,000.00 USD | 23,310.00 USD | 88,960.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1575` | 4,940.00 USD | 249,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1577` | 3,910,000.00 USD | 3,910,000.00 USD | 54,010.00 USD | 54,680.00 USD | 19,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1578` | 8,710,000.00 USD | 8,710,000.00 USD | 58,590.00 USD | 84,670.00 USD | 67,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1580` | 3,780,000.00 USD | 3,780,000.00 USD | 47,010.00 USD | 22,460.00 USD | 28,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1581` | 8,500,000.00 USD | 8,500,000.00 USD | 92,720.00 USD | 58,880.00 USD | 57,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1583` | 3,680,000.00 USD | 3,680,000.00 USD | 27,790.00 USD | 12,250.00 USD | 16,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1584` | 8,290,000.00 USD | 8,290,000.00 USD | 80,450.00 USD | 35,780.00 USD | 123,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1585` | 2,660.00 USD | 244,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1586` | 3,620,000.00 USD | 3,620,000.00 USD | 20,430.00 USD | 18,430.00 USD | 15,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1587` | 8,050,000.00 USD | 8,050,000.00 USD | 69,180.00 USD | 22,370.00 USD | 31,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1589` | 3,570,000.00 USD | 3,570,000.00 USD | 13,490.00 USD | 19,490.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1590` | 7,930,000.00 USD | 7,930,000.00 USD | 71,200.00 USD | 44,110.00 USD | 51,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1592` | 3,530,000.00 USD | 3,530,000.00 USD | 26,740.00 USD | 20,480.00 USD | 13,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1593` | 7,760,000.00 USD | 7,760,000.00 USD | 69,430.00 USD | 56,020.00 USD | 68,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1595` | 3,470,000.00 USD | 3,470,000.00 USD | 43,860.00 USD | 14,560.00 USD | 34,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1595` | 66,110.00 USD | 241,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1596` | 7,570,000.00 USD | 7,570,000.00 USD | 161,460.00 USD | 85,250.00 USD | 120,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1598` | 3,380,000.00 USD | 3,380,000.00 USD | 67,640.00 USD | 21,610.00 USD | 40,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1599` | 7,200,000.00 USD | 7,200,000.00 USD | 219,060.00 USD | 55,380.00 USD | 87,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1601` | 3,250,000.00 USD | 3,250,000.00 USD | 47,450.00 USD | 33,200.00 USD | 11,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1602` | 6,840,000.00 USD | 6,840,000.00 USD | 44,770.00 USD | 46,490.00 USD | 40,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1604` | 3,150,000.00 USD | 3,150,000.00 USD | 39,480.00 USD | 20,230.00 USD | 17,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1605` | 6,710,000.00 USD | 6,710,000.00 USD | 177,720.00 USD | 136,660.00 USD | 217,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1605` | 20,460.00 USD | 175,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1607` | 3,080,000.00 USD | 3,080,000.00 USD | 54,740.00 USD | 24,450.00 USD | 26,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1608` | 6,180,000.00 USD | 6,180,000.00 USD | 129,610.00 USD | 174,940.00 USD | 131,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1610` | 2,970,000.00 USD | 2,970,000.00 USD | 112,000.00 USD | 113,820.00 USD | 47,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1611` | 5,740,000.00 USD | 5,740,000.00 USD | 148,170.00 USD | 227,820.00 USD | 233,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1613` | 2,700,000.00 USD | 2,700,000.00 USD | 85,600.00 USD | 54,580.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1614` | 5,130,000.00 USD | 5,130,000.00 USD | 330,910.00 USD | 194,680.00 USD | 282,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1615` | 17,950.00 USD | 155,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1616` | 2,500,000.00 USD | 2,500,000.00 USD | 55,580.00 USD | 29,990.00 USD | 37,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1617` | 4,320,000.00 USD | 4,320,000.00 USD | 346,150.00 USD | 101,810.00 USD | 410,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1619` | 2,370,000.00 USD | 2,370,000.00 USD | 61,900.00 USD | 38,790.00 USD | 51,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1620` | 3,460,000.00 USD | 3,460,000.00 USD | 282,000.00 USD | 134,660.00 USD | 271,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1622` | 2,220,000.00 USD | 2,220,000.00 USD | 62,190.00 USD | 52,780.00 USD | 31,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1623` | 2,780,000.00 USD | 2,780,000.00 USD | 304,460.00 USD | 125,080.00 USD | 208,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1625` | 2,070,000.00 USD | 2,070,000.00 USD | 19,000.00 USD | 48,390.00 USD | 20,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1625` | 98,470.00 USD | 137,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1626` | 2,140,000.00 USD | 2,140,000.00 USD | 234,280.00 USD | 71,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1628` | 1,990,000.00 USD | 1,990,000.00 USD | 14,220.00 USD | 29,880.00 USD | 22,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1629` | 1,830,000.00 USD | 1,830,000.00 USD | 171,310.00 USD | 0.00 USD | 20,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1631` | 1,920,000.00 USD | 1,920,000.00 USD | 12,400.00 USD | 15,310.00 USD | 18,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1632` | 1,640,000.00 USD | 1,640,000.00 USD | 9,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1634` | 1,870,000.00 USD | 1,870,000.00 USD | 32,300.00 USD | 13,860.00 USD | 13,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1635` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 13,670.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1635` | 5,930.00 USD | 38,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1637` | 1,810,000.00 USD | 1,810,000.00 USD | 7,630.00 USD | 22,520.00 USD | 19,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1638` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 62,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1640` | 1,760,000.00 USD | 1,760,000.00 USD | 14,040.00 USD | 6,090.00 USD | 37,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1641` | 1,530,000.00 USD | 1,530,000.00 USD | 22,480.00 USD | 29,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1643` | 1,710,000.00 USD | 1,710,000.00 USD | 25,590.00 USD | 20,340.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1644` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 8,990.00 USD | 26,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1645` | 14,520.00 USD | 33,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1646` | 1,660,000.00 USD | 1,660,000.00 USD | 40,030.00 USD | 24,740.00 USD | 34,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1647` | 1,450,000.00 USD | 1,450,000.00 USD | 34,760.00 USD | 0.00 USD | 7,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1649` | 1,560,000.00 USD | 1,560,000.00 USD | 4,570.00 USD | 23,390.00 USD | 19,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1650` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 7,000.00 USD | 22,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1652` | 1,510,000.00 USD | 1,510,000.00 USD | 19,770.00 USD | 8,470.00 USD | 34,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1653` | 1,370,000.00 USD | 1,370,000.00 USD | 33,810.00 USD | 12,460.00 USD | 28,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1655` | 1,450,000.00 USD | 1,450,000.00 USD | 32,370.00 USD | 31,080.00 USD | 29,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1655` | 12,410.00 USD | 18,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1656` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 19,330.00 USD | 33,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1658` | 1,360,000.00 USD | 1,360,000.00 USD | 54,340.00 USD | 47,930.00 USD | 45,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1659` | 1,250,000.00 USD | 1,250,000.00 USD | 40,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1661` | 1,210,000.00 USD | 1,210,000.00 USD | 22,630.00 USD | 11,150.00 USD | 60,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1662` | 1,210,000.00 USD | 1,210,000.00 USD | 48,590.00 USD | 62,020.00 USD | 81,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1664` | 1,110,000.00 USD | 1,110,000.00 USD | 48,150.00 USD | 59,110.00 USD | 67,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1665` | 1,010,000.00 USD | 1,010,000.00 USD | 87,050.00 USD | 32,780.00 USD | 57,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1667` | 938,790.00 USD | 938,790.00 USD | 105,350.00 USD | 72,210.00 USD | 53,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1668` | 837,670.00 USD | 837,670.00 USD | 11,410.00 USD | 39,630.00 USD | 42,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1670` | 708,020.00 USD | 708,020.00 USD | 64,200.00 USD | 29,020.00 USD | 27,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1671` | 743,910.00 USD | 743,910.00 USD | 70,540.00 USD | 62,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1673` | 587,670.00 USD | 587,670.00 USD | 42,030.00 USD | 31,130.00 USD | 18,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1674` | 610,890.00 USD | 610,890.00 USD | 44,960.00 USD | 88,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1675` | 6,100.00 USD | 6,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1676` | 496,100.00 USD | 496,100.00 USD | 14,620.00 USD | 33,240.00 USD | 23,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1677` | 476,980.00 USD | 476,980.00 USD | 59,010.00 USD | 64,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1679` | 424,730.00 USD | 424,730.00 USD | 6,270.00 USD | 5,070.00 USD | 22,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1680` | 353,120.00 USD | 353,120.00 USD | 101,910.00 USD | 68,430.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1682` | 390,970.00 USD | 390,970.00 USD | 144,140.00 USD | 38,540.00 USD | 32,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1683` | 167,470.00 USD | 167,470.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1685` | 176,050.00 USD | 176,050.00 USD | 13,810.00 USD | 26,600.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1688` | 123,820.00 USD | 123,820.00 USD | 0.00 USD | 0.00 USD | 8,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1689` | 92,520.00 USD | 92,520.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1691` | 115,250.00 USD | 115,250.00 USD | 42,110.00 USD | 73,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1692` | 53,850.00 USD | 53,850.00 USD | 21,780.00 USD | 32,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1694` | 35,510.00 USD | 35,510.00 USD | 13,210.00 USD | 22,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1694` | 71,010.00 USD | 71,010.00 USD | 13,210.00 USD | 22,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1695` | 58,500.00 USD | 58,500.00 USD | 0.00 USD | 30,490.00 USD | 28,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1695` | 116,990.00 USD | 116,990.00 USD | 0.00 USD | 30,490.00 USD | 28,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1697` | 121,560.00 USD | 121,560.00 USD | 15,020.00 USD | 35,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1698` | 192,680.00 USD | 192,680.00 USD | 0.00 USD | 56,860.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1700` | 142,720.00 USD | 142,720.00 USD | 0.00 USD | 21,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1701` | 240,830.00 USD | 240,830.00 USD | 22,820.00 USD | 25,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1703` | 167,380.00 USD | 167,380.00 USD | 0.00 USD | 14,420.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1704` | 287,710.00 USD | 287,710.00 USD | 0.00 USD | 46,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1706` | 199,980.00 USD | 199,980.00 USD | 22,060.00 USD | 6,390.00 USD | 4,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1707` | 347,230.00 USD | 347,230.00 USD | 0.00 USD | 0.00 USD | 59,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1709` | 278,150.00 USD | 278,150.00 USD | 15,910.00 USD | 62,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1710` | 377,900.00 USD | 377,900.00 USD | 0.00 USD | 25,490.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1712` | 288,280.00 USD | 288,280.00 USD | 0.00 USD | 10,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1713` | 419,920.00 USD | 419,920.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1715` | 309,320.00 USD | 309,320.00 USD | 0.00 USD | 21,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1718` | 327,190.00 USD | 327,190.00 USD | 9,350.00 USD | 8,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1721` | 403,680.00 USD | 403,680.00 USD | 63,350.00 USD | 13,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1722` | 819,940.00 USD | 819,940.00 USD | 74,150.00 USD | 0.00 USD | 325,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1724` | 414,870.00 USD | 414,870.00 USD | 0.00 USD | 0.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1727` | 419,570.00 USD | 419,570.00 USD | 0.00 USD | 0.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1730` | 426,300.00 USD | 426,300.00 USD | 0.00 USD | 0.00 USD | 6,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1731` | 1,310,000.00 USD | 1,310,000.00 USD | 493,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1733` | 436,360.00 USD | 436,360.00 USD | 0.00 USD | 0.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1735` | 6,900.00 USD | 6,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1736` | 460,840.00 USD | 460,840.00 USD | 14,970.00 USD | 9,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1737` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 52,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1739` | 485,070.00 USD | 485,070.00 USD | 14,580.00 USD | 0.00 USD | 9,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1740` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 31,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1742` | 495,030.00 USD | 495,030.00 USD | 0.00 USD | 0.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1743` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1745` | 509,800.00 USD | 509,800.00 USD | 8,530.00 USD | 0.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1748` | 604,690.00 USD | 604,690.00 USD | 55,280.00 USD | 0.00 USD | 39,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1749` | 1,490,000.00 USD | 1,490,000.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1751` | 653,230.00 USD | 653,230.00 USD | 37,840.00 USD | 0.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1752` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 263,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1754` | 703,240.00 USD | 703,240.00 USD | 9,790.00 USD | 6,570.00 USD | 33,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1755` | 1,970,000.00 USD | 1,970,000.00 USD | 37,610.00 USD | 0.00 USD | 169,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1757` | 797,450.00 USD | 797,450.00 USD | 8,970.00 USD | 40,160.00 USD | 45,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1758` | 2,190,000.00 USD | 2,190,000.00 USD | 173,440.00 USD | 38,670.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1760` | 976,520.00 USD | 976,520.00 USD | 85,150.00 USD | 76,400.00 USD | 17,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1761` | 2,720,000.00 USD | 2,720,000.00 USD | 373,120.00 USD | 131,090.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1763` | 1,150,000.00 USD | 1,150,000.00 USD | 84,560.00 USD | 20,760.00 USD | 66,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1764` | 3,120,000.00 USD | 3,120,000.00 USD | 144,160.00 USD | 215,620.00 USD | 40,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1765` | 339.06 USD | 7,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1766` | 1,260,000.00 USD | 1,260,000.00 USD | 24,650.00 USD | 20,220.00 USD | 68,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1767` | 3,450,000.00 USD | 3,450,000.00 USD | 176,410.00 USD | 143,320.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1769` | 1,450,000.00 USD | 1,450,000.00 USD | 53,350.00 USD | 91,810.00 USD | 44,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1770` | 3,700,000.00 USD | 3,700,000.00 USD | 61,490.00 USD | 147,940.00 USD | 44,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1772` | 1,520,000.00 USD | 1,520,000.00 USD | 22,380.00 USD | 20,220.00 USD | 28,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1773` | 3,910,000.00 USD | 3,910,000.00 USD | 103,820.00 USD | 105,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1775` | 1,630,000.00 USD | 1,630,000.00 USD | 74,270.00 USD | 27,710.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1775` | 151.67 USD | 7,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1776` | 4,120,000.00 USD | 4,120,000.00 USD | 135,140.00 USD | 69,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1778` | 1,800,000.00 USD | 1,800,000.00 USD | 58,020.00 USD | 87,510.00 USD | 24,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1779` | 4,350,000.00 USD | 4,350,000.00 USD | 52,730.00 USD | 46,410.00 USD | 131,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1781` | 1,900,000.00 USD | 1,900,000.00 USD | 50,570.00 USD | 1,060.00 USD | 45,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1782` | 4,420,000.00 USD | 4,420,000.00 USD | 20,690.00 USD | 13,990.00 USD | 31,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1784` | 2,050,000.00 USD | 2,050,000.00 USD | 92,690.00 USD | 38,240.00 USD | 23,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1785` | 4,660,000.00 USD | 4,660,000.00 USD | 153,160.00 USD | 78,850.00 USD | 16,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1785` | 421.28 USD | 7,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1787` | 2,200,000.00 USD | 2,200,000.00 USD | 37,680.00 USD | 54,820.00 USD | 51,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1788` | 4,770,000.00 USD | 4,770,000.00 USD | 73,130.00 USD | 18,250.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1790` | 2,300,000.00 USD | 2,300,000.00 USD | 53,220.00 USD | 22,930.00 USD | 21,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1791` | 4,950,000.00 USD | 4,950,000.00 USD | 155,720.00 USD | 17,360.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1793` | 2,370,000.00 USD | 2,370,000.00 USD | 32,720.00 USD | 20,810.00 USD | 20,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1794` | 5,050,000.00 USD | 5,050,000.00 USD | 27,100.00 USD | 42,780.00 USD | 36,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1795` | 682.60 USD | 8,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1796` | 2,520,000.00 USD | 2,520,000.00 USD | 48,060.00 USD | 66,080.00 USD | 41,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1797` | 5,090,000.00 USD | 5,090,000.00 USD | 17,130.00 USD | 12,930.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1799` | 2,570,000.00 USD | 2,570,000.00 USD | 16,820.00 USD | 14,880.00 USD | 15,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1800` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 34,680.00 USD | 64,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1802` | 2,650,000.00 USD | 2,650,000.00 USD | 15,140.00 USD | 34,770.00 USD | 28,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1803` | 5,270,000.00 USD | 5,270,000.00 USD | 35,280.00 USD | 25,700.00 USD | 18,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1805` | 2,710,000.00 USD | 2,710,000.00 USD | 22,680.00 USD | 9,380.00 USD | 27,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1805` | 4,320.00 USD | 12,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1806` | 5,360,000.00 USD | 5,360,000.00 USD | 11,410.00 USD | 56,850.00 USD | 19,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1808` | 2,800,000.00 USD | 2,800,000.00 USD | 24,170.00 USD | 27,870.00 USD | 35,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1809` | 5,500,000.00 USD | 5,500,000.00 USD | 53,670.00 USD | 30,810.00 USD | 58,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1811` | 2,880,000.00 USD | 2,880,000.00 USD | 39,150.00 USD | 16,000.00 USD | 24,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1812` | 5,600,000.00 USD | 5,600,000.00 USD | 34,960.00 USD | 16,640.00 USD | 50,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1814` | 2,970,000.00 USD | 2,970,000.00 USD | 27,380.00 USD | 36,930.00 USD | 28,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1815` | 5,730,000.00 USD | 5,730,000.00 USD | 60,010.00 USD | 30,810.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1817` | 3,040,000.00 USD | 3,040,000.00 USD | 31,330.00 USD | 11,020.00 USD | 30,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1818` | 5,840,000.00 USD | 5,840,000.00 USD | 75,040.00 USD | 24,140.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1820` | 3,100,000.00 USD | 3,100,000.00 USD | 32,520.00 USD | 18,550.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1821` | 5,960,000.00 USD | 5,960,000.00 USD | 40,950.00 USD | 33,870.00 USD | 41,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1823` | 3,150,000.00 USD | 3,150,000.00 USD | 16,740.00 USD | 19,980.00 USD | 17,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1824` | 6,110,000.00 USD | 6,110,000.00 USD | 39,400.00 USD | 17,880.00 USD | 95,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1825` | 48,910.00 USD | 61,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1826` | 3,190,000.00 USD | 3,190,000.00 USD | 24,740.00 USD | 6,860.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1827` | 6,270,000.00 USD | 6,270,000.00 USD | 79,610.00 USD | 18,690.00 USD | 65,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1829` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 1,640.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1830` | 6,410,000.00 USD | 6,410,000.00 USD | 64,890.00 USD | 20,550.00 USD | 52,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1832` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 2,880.00 USD | 9,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1833` | 6,680,000.00 USD | 6,680,000.00 USD | 186,730.00 USD | 49,740.00 USD | 26,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1835` | 3,210,000.00 USD | 3,210,000.00 USD | 3,610.00 USD | 0.00 USD | 728.16 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1835` | 837.27 USD | 62,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1836` | 6,840,000.00 USD | 6,840,000.00 USD | 29,580.00 USD | 83,110.00 USD | 52,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1838` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 2,640.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1839` | 7,130,000.00 USD | 7,130,000.00 USD | 129,950.00 USD | 41,230.00 USD | 114,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1841` | 3,240,000.00 USD | 3,240,000.00 USD | 13,150.00 USD | 1,090.00 USD | 7,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1842` | 7,320,000.00 USD | 7,320,000.00 USD | 71,550.00 USD | 26,100.00 USD | 97,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1844` | 3,270,000.00 USD | 3,270,000.00 USD | 2,690.00 USD | 5,540.00 USD | 15,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1845` | 7,460,000.00 USD | 7,460,000.00 USD | 34,630.00 USD | 33,340.00 USD | 66,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1845` | 8,800.00 USD | 71,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1847` | 3,290,000.00 USD | 3,290,000.00 USD | 7,630.00 USD | 7,150.00 USD | 11,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1848` | 7,710,000.00 USD | 7,710,000.00 USD | 47,730.00 USD | 75,080.00 USD | 135,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1850` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 1,730.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1851` | 8,060,000.00 USD | 8,060,000.00 USD | 94,780.00 USD | 28,290.00 USD | 220,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1853` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 1,690.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1854` | 8,230,000.00 USD | 8,230,000.00 USD | 105,210.00 USD | 4,290.00 USD | 63,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1856` | 3,320,000.00 USD | 3,320,000.00 USD | 8,770.00 USD | 2,630.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1857` | 8,510,000.00 USD | 8,510,000.00 USD | 116,320.00 USD | 32,070.00 USD | 127,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1859` | 3,340,000.00 USD | 3,340,000.00 USD | 9,450.00 USD | 1,470.00 USD | 5,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1860` | 8,740,000.00 USD | 8,740,000.00 USD | 87,180.00 USD | 72,430.00 USD | 74,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1862` | 3,350,000.00 USD | 3,350,000.00 USD | 1,870.00 USD | 2,970.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1863` | 8,930,000.00 USD | 8,930,000.00 USD | 71,330.00 USD | 56,440.00 USD | 61,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1865` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 6,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1866` | 9,100,000.00 USD | 9,100,000.00 USD | 101,070.00 USD | 33,740.00 USD | 39,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1868` | 3,370,000.00 USD | 3,370,000.00 USD | 3,300.00 USD | 0.00 USD | 7,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1869` | 9,420,000.00 USD | 9,420,000.00 USD | 169,650.00 USD | 66,330.00 USD | 78,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1871` | 3,390,000.00 USD | 3,390,000.00 USD | 11,950.00 USD | 6,940.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1872` | 9,730,000.00 USD | 9,730,000.00 USD | 80,790.00 USD | 132,480.00 USD | 93,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1874` | 3,410,000.00 USD | 3,410,000.00 USD | 7,320.00 USD | 2,820.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1875` | 9,870,000.00 USD | 9,870,000.00 USD | 68,250.00 USD | 37,700.00 USD | 36,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1875` | 21,190.00 USD | 92,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1877` | 3,410,000.00 USD | 3,410,000.00 USD | 2,670.00 USD | 2,760.00 USD | 918.24 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1878` | 10,020,000.00 USD | 10,020,000.00 USD | 66,470.00 USD | 37,330.00 USD | 48,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1880` | 3,430,000.00 USD | 3,430,000.00 USD | 4,530.00 USD | 3,160.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1881` | 10,110,000.00 USD | 10,110,000.00 USD | 29,820.00 USD | 44,080.00 USD | 13,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1883` | 3,440,000.00 USD | 3,440,000.00 USD | 4,630.00 USD | 4,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1884` | 10,210,000.00 USD | 10,210,000.00 USD | 10,560.00 USD | 36,820.00 USD | 58,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1885` | 477.23 USD | 93,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1886` | 3,460,000.00 USD | 3,460,000.00 USD | 13,740.00 USD | 2,220.00 USD | 6,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1887` | 10,260,000.00 USD | 10,260,000.00 USD | 22,970.00 USD | 0.00 USD | 25,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1889` | 3,480,000.00 USD | 3,480,000.00 USD | 3,580.00 USD | 3,150.00 USD | 7,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1890` | 10,390,000.00 USD | 10,390,000.00 USD | 36,740.00 USD | 17,330.00 USD | 75,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1892` | 3,490,000.00 USD | 3,490,000.00 USD | 1,140.00 USD | 8,660.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1893` | 10,450,000.00 USD | 10,450,000.00 USD | 32,450.00 USD | 6,940.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1895` | 3,500,000.00 USD | 3,500,000.00 USD | 4,810.00 USD | 4,140.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1896` | 10,560,000.00 USD | 10,560,000.00 USD | 62,730.00 USD | 27,440.00 USD | 18,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1898` | 3,520,000.00 USD | 3,520,000.00 USD | 7,030.00 USD | 16,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1899` | 10,630,000.00 USD | 10,630,000.00 USD | 11,530.00 USD | 38,530.00 USD | 20,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1901` | 3,550,000.00 USD | 3,550,000.00 USD | 11,640.00 USD | 4,150.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1902` | 10,650,000.00 USD | 10,650,000.00 USD | 14,330.00 USD | 0.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1904` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 1,660.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1905` | 10,710,000.00 USD | 10,710,000.00 USD | 8,720.00 USD | 24,800.00 USD | 24,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1907` | 3,580,000.00 USD | 3,580,000.00 USD | 2,490.00 USD | 11,300.00 USD | 6,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1908` | 10,810,000.00 USD | 10,810,000.00 USD | 25,220.00 USD | 43,160.00 USD | 28,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1910` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 1,050.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1911` | 10,820,000.00 USD | 10,820,000.00 USD | 0.00 USD | 9,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1913` | 3,590,000.00 USD | 3,590,000.00 USD | 4,910.00 USD | 2,880.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1914` | 10,830,000.00 USD | 10,830,000.00 USD | 7,460.00 USD | 11,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1916` | 3,620,000.00 USD | 3,620,000.00 USD | 12,220.00 USD | 16,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1917` | 10,860,000.00 USD | 10,860,000.00 USD | 0.00 USD | 11,840.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1923` | 10,880,000.00 USD | 10,880,000.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1926` | 10,900,000.00 USD | 10,900,000.00 USD | 11,600.00 USD | 13,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1944` | 10,910,000.00 USD | 10,910,000.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.1461` | 10,690,000.00 USD | 0.00 USD | 10,690,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD |
| `7D` | `0.1464` | 10,680,000.00 USD | 0.00 USD | 10,680,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD |
| `7D` | `0.1467` | 10,680,000.00 USD | 0.00 USD | 10,680,000.00 USD | 9,720.00 USD | 9,180.00 USD | 4,840.00 USD |
| `7D` | `0.1470` | 10,650,000.00 USD | 0.00 USD | 10,650,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD |
| `7D` | `0.1473` | 10,640,000.00 USD | 0.00 USD | 10,640,000.00 USD | 6,490.00 USD | 5,400.00 USD | 5,280.00 USD |
| `7D` | `0.1476` | 10,630,000.00 USD | 0.00 USD | 10,630,000.00 USD | 0.00 USD | 14,780.00 USD | 5,320.00 USD |
| `7D` | `0.1479` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 0.00 USD | 39,730.00 USD | 14,560.00 USD |
| `7D` | `0.1482` | 10,550,000.00 USD | 0.00 USD | 10,550,000.00 USD | 41,960.00 USD | 20,720.00 USD | 27,030.00 USD |
| `7D` | `0.1485` | 10,460,000.00 USD | 0.00 USD | 10,460,000.00 USD | 16,180.00 USD | 7,340.00 USD | 38,270.00 USD |
| `7D` | `0.1488` | 10,400,000.00 USD | 0.00 USD | 10,400,000.00 USD | 20,860.00 USD | 3,130.00 USD | 10,390.00 USD |
| `7D` | `0.1491` | 10,370,000.00 USD | 0.00 USD | 10,370,000.00 USD | 33,540.00 USD | 17,020.00 USD | 20,270.00 USD |
| `7D` | `0.1494` | 10,300,000.00 USD | 0.00 USD | 10,300,000.00 USD | 34,220.00 USD | 9,890.00 USD | 14,210.00 USD |
| `7D` | `0.1497` | 10,240,000.00 USD | 0.00 USD | 10,240,000.00 USD | 20,880.00 USD | 17,180.00 USD | 9,710.00 USD |
| `7D` | `0.1500` | 10,190,000.00 USD | 0.00 USD | 10,190,000.00 USD | 46,820.00 USD | 5,810.00 USD | 21,940.00 USD |
| `7D` | `0.1503` | 10,120,000.00 USD | 0.00 USD | 10,120,000.00 USD | 11,490.00 USD | 13,450.00 USD | 9,950.00 USD |
| `7D` | `0.1506` | 10,080,000.00 USD | 0.00 USD | 10,080,000.00 USD | 33,170.00 USD | 18,020.00 USD | 65,400.00 USD |
| `7D` | `0.1509` | 9,960,000.00 USD | 0.00 USD | 9,960,000.00 USD | 17,340.00 USD | 9,550.00 USD | 24,150.00 USD |
| `1D` | `0.1511` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 5,640.00 USD | 7,210.00 USD | 2,500.00 USD |
| `7D` | `0.1512` | 9,910,000.00 USD | 0.00 USD | 9,910,000.00 USD | 18,600.00 USD | 8,620.00 USD | 26,910.00 USD |
| `1D` | `0.1514` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 0.00 USD | 1,730.00 USD | 1,300.00 USD |
| `7D` | `0.1515` | 9,860,000.00 USD | 0.00 USD | 9,860,000.00 USD | 53,430.00 USD | 13,330.00 USD | 53,490.00 USD |
| `1D` | `0.1517` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 7,630.00 USD | 1,690.00 USD | 7,420.00 USD |
| `7D` | `0.1518` | 9,740,000.00 USD | 0.00 USD | 9,740,000.00 USD | 46,830.00 USD | 15,160.00 USD | 64,360.00 USD |
| `1D` | `0.1520` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 7,500.00 USD | 4,100.00 USD | 5,910.00 USD |
| `7D` | `0.1521` | 9,610,000.00 USD | 0.00 USD | 9,610,000.00 USD | 38,960.00 USD | 6,920.00 USD | 38,800.00 USD |
| `1D` | `0.1523` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 5,860.00 USD | 2,970.00 USD | 3,900.00 USD |
| `7D` | `0.1524` | 9,530,000.00 USD | 0.00 USD | 9,530,000.00 USD | 37,550.00 USD | 13,950.00 USD | 11,280.00 USD |
| `1D` | `0.1526` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 5,170.00 USD | 0.00 USD | 11,650.00 USD |
| `7D` | `0.1527` | 9,470,000.00 USD | 0.00 USD | 9,470,000.00 USD | 56,950.00 USD | 30,410.00 USD | 33,080.00 USD |
| `1D` | `0.1529` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 4,960.00 USD | 1,740.00 USD | 9,730.00 USD |
| `7D` | `0.1530` | 9,340,000.00 USD | 0.00 USD | 9,340,000.00 USD | 54,790.00 USD | 9,880.00 USD | 16,070.00 USD |
| `1D` | `0.1532` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 12,350.00 USD | 5,200.00 USD | 5,320.00 USD |
| `7D` | `0.1533` | 9,260,000.00 USD | 0.00 USD | 9,260,000.00 USD | 10,760.00 USD | 16,570.00 USD | 21,560.00 USD |
| `1D` | `0.1535` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 4,630.00 USD | 5,590.00 USD | 3,210.00 USD |
| `7D` | `0.1536` | 9,220,000.00 USD | 0.00 USD | 9,220,000.00 USD | 37,160.00 USD | 2,910.00 USD | 13,450.00 USD |
| `1D` | `0.1538` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 4,530.00 USD | 3,160.00 USD | 8,370.00 USD |
| `7D` | `0.1539` | 9,160,000.00 USD | 0.00 USD | 9,160,000.00 USD | 22,990.00 USD | 18,230.00 USD | 5,070.00 USD |
| `1D` | `0.1541` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 4,630.00 USD | 4,960.00 USD | 0.00 USD |
| `7D` | `0.1542` | 9,120,000.00 USD | 0.00 USD | 9,120,000.00 USD | 0.00 USD | 3,590.00 USD | 4,670.00 USD |
| `1D` | `0.1544` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 17,310.00 USD | 5,370.00 USD | 6,220.00 USD |
| `7D` | `0.1545` | 9,110,000.00 USD | 0.00 USD | 9,110,000.00 USD | 9,250.00 USD | 0.00 USD | 5,620.00 USD |
| `1D` | `0.1547` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 1,140.00 USD | 6,820.00 USD | 7,640.00 USD |
| `7D` | `0.1548` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD |
| `1D` | `0.1550` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 4,810.00 USD | 4,460.00 USD | 2,030.00 USD |
| `7D` | `0.1551` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 34,670.00 USD | 11,820.00 USD | 0.00 USD |
| `1D` | `0.1553` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 11,770.00 USD | 20,800.00 USD | 6,590.00 USD |
| `7D` | `0.1554` | 9,040,000.00 USD | 0.00 USD | 9,040,000.00 USD | 0.00 USD | 0.00 USD | 6,470.00 USD |
| `1D` | `0.1556` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 6,890.00 USD | 3,410.00 USD | 6,780.00 USD |
| `7D` | `0.1557` | 9,040,000.00 USD | 0.00 USD | 9,040,000.00 USD | 0.00 USD | 4,510.00 USD | 10,800.00 USD |
| `1D` | `0.1559` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 2,490.00 USD | 8,320.00 USD | 7,790.00 USD |
| `7D` | `0.1560` | 9,020,000.00 USD | 0.00 USD | 9,020,000.00 USD | 0.00 USD | 6,480.00 USD | 0.00 USD |
| `1D` | `0.1562` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 6,020.00 USD | 4,020.00 USD | 10,350.00 USD |
| `7D` | `0.1563` | 9,010,000.00 USD | 0.00 USD | 9,010,000.00 USD | 0.00 USD | 19,950.00 USD | 9,840.00 USD |
| `1D` | `0.1565` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 24,770.00 USD | 11,570.00 USD | 15,030.00 USD |
| `7D` | `0.1566` | 8,980,000.00 USD | 0.00 USD | 8,980,000.00 USD | 50,480.00 USD | 29,160.00 USD | 26,780.00 USD |
| `1D` | `0.1568` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 34,400.00 USD | 26,770.00 USD | 17,010.00 USD |
| `7D` | `0.1569` | 8,880,000.00 USD | 0.00 USD | 8,880,000.00 USD | 15,590.00 USD | 5,100.00 USD | 11,900.00 USD |
| `1D` | `0.1571` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 32,670.00 USD | 11,300.00 USD | 10,840.00 USD |
| `7D` | `0.1572` | 8,850,000.00 USD | 0.00 USD | 8,850,000.00 USD | 40,760.00 USD | 34,450.00 USD | 17,760.00 USD |
| `1D` | `0.1574` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 34,240.00 USD | 13,520.00 USD | 8,660.00 USD |
| `7D` | `0.1575` | 8,750,000.00 USD | 0.00 USD | 8,750,000.00 USD | 23,310.00 USD | 88,960.00 USD | 21,360.00 USD |
| `1D` | `0.1577` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 54,010.00 USD | 54,680.00 USD | 19,410.00 USD |
| `7D` | `0.1578` | 8,620,000.00 USD | 0.00 USD | 8,620,000.00 USD | 58,590.00 USD | 84,670.00 USD | 67,670.00 USD |
| `1D` | `0.1580` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 47,010.00 USD | 22,460.00 USD | 28,230.00 USD |
| `7D` | `0.1581` | 8,410,000.00 USD | 0.00 USD | 8,410,000.00 USD | 92,720.00 USD | 58,880.00 USD | 57,600.00 USD |
| `1D` | `0.1583` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 27,790.00 USD | 12,250.00 USD | 16,200.00 USD |
| `7D` | `0.1584` | 8,200,000.00 USD | 0.00 USD | 8,200,000.00 USD | 80,450.00 USD | 35,780.00 USD | 123,970.00 USD |
| `1D` | `0.1586` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 20,430.00 USD | 18,430.00 USD | 15,100.00 USD |
| `7D` | `0.1587` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 69,180.00 USD | 22,370.00 USD | 31,060.00 USD |
| `1D` | `0.1589` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 13,490.00 USD | 19,490.00 USD | 8,270.00 USD |
| `7D` | `0.1590` | 7,840,000.00 USD | 0.00 USD | 7,840,000.00 USD | 71,200.00 USD | 44,110.00 USD | 51,290.00 USD |
| `1D` | `0.1592` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 26,740.00 USD | 20,480.00 USD | 13,210.00 USD |
| `7D` | `0.1593` | 7,670,000.00 USD | 0.00 USD | 7,670,000.00 USD | 69,430.00 USD | 56,020.00 USD | 68,480.00 USD |
| `1D` | `0.1595` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 43,860.00 USD | 14,560.00 USD | 34,370.00 USD |
| `7D` | `0.1596` | 7,480,000.00 USD | 0.00 USD | 7,480,000.00 USD | 161,460.00 USD | 85,250.00 USD | 120,230.00 USD |
| `1D` | `0.1598` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 67,640.00 USD | 21,610.00 USD | 40,820.00 USD |
| `7D` | `0.1599` | 7,110,000.00 USD | 0.00 USD | 7,110,000.00 USD | 219,060.00 USD | 55,380.00 USD | 87,990.00 USD |
| `1D` | `0.1601` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 47,450.00 USD | 33,200.00 USD | 11,300.00 USD |
| `7D` | `0.1602` | 6,750,000.00 USD | 0.00 USD | 6,750,000.00 USD | 44,770.00 USD | 46,490.00 USD | 40,380.00 USD |
| `1D` | `0.1604` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 39,480.00 USD | 20,230.00 USD | 17,830.00 USD |
| `7D` | `0.1605` | 6,610,000.00 USD | 0.00 USD | 6,610,000.00 USD | 177,720.00 USD | 136,660.00 USD | 217,140.00 USD |
| `1D` | `0.1607` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 54,740.00 USD | 24,450.00 USD | 26,290.00 USD |
| `7D` | `0.1608` | 6,080,000.00 USD | 0.00 USD | 6,080,000.00 USD | 129,610.00 USD | 174,940.00 USD | 131,300.00 USD |
| `1D` | `0.1610` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 112,000.00 USD | 111,110.00 USD | 41,420.00 USD |
| `7D` | `0.1611` | 5,650,000.00 USD | 0.00 USD | 5,650,000.00 USD | 148,170.00 USD | 227,820.00 USD | 233,470.00 USD |
| `1D` | `0.1613` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 85,600.00 USD | 54,580.00 USD | 61,970.00 USD |
| `7D` | `0.1614` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 330,910.00 USD | 194,680.00 USD | 282,150.00 USD |
| `1D` | `0.1616` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 55,580.00 USD | 29,990.00 USD | 37,640.00 USD |
| `7D` | `0.1617` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 346,150.00 USD | 101,810.00 USD | 410,900.00 USD |
| `1D` | `0.1619` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 68,840.00 USD | 38,790.00 USD | 51,430.00 USD |
| `7D` | `0.1620` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 282,000.00 USD | 134,660.00 USD | 271,570.00 USD |
| `1D` | `0.1622` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 66,240.00 USD | 54,640.00 USD | 31,270.00 USD |
| `7D` | `0.1623` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 304,460.00 USD | 125,080.00 USD | 208,070.00 USD |
| `1D` | `0.1625` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 19,000.00 USD | 48,390.00 USD | 22,530.00 USD |
| `7D` | `0.1626` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 234,280.00 USD | 71,120.00 USD | 0.00 USD |
| `1D` | `0.1628` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 18,330.00 USD | 29,880.00 USD | 22,020.00 USD |
| `7D` | `0.1629` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 171,310.00 USD | 0.00 USD | 20,860.00 USD |
| `1D` | `0.1631` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 12,400.00 USD | 15,310.00 USD | 18,720.00 USD |
| `7D` | `0.1632` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 9,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1634` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 32,300.00 USD | 13,860.00 USD | 13,290.00 USD |
| `7D` | `0.1635` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 0.00 USD | 13,670.00 USD | 21,360.00 USD |
| `1D` | `0.1637` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 7,630.00 USD | 22,520.00 USD | 19,410.00 USD |
| `7D` | `0.1638` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 62,410.00 USD |
| `1D` | `0.1640` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 14,040.00 USD | 6,090.00 USD | 37,730.00 USD |
| `7D` | `0.1641` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 22,480.00 USD | 29,240.00 USD | 0.00 USD |
| `1D` | `0.1643` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 25,590.00 USD | 20,340.00 USD | 3,370.00 USD |
| `7D` | `0.1644` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 0.00 USD | 8,990.00 USD | 26,230.00 USD |
| `1D` | `0.1646` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 40,030.00 USD | 24,740.00 USD | 34,550.00 USD |
| `7D` | `0.1647` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 34,760.00 USD | 0.00 USD | 7,650.00 USD |
| `1D` | `0.1649` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 4,570.00 USD | 23,390.00 USD | 19,090.00 USD |
| `7D` | `0.1650` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 0.00 USD | 7,000.00 USD | 22,660.00 USD |
| `1D` | `0.1652` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 33,640.00 USD | 8,470.00 USD | 34,610.00 USD |
| `7D` | `0.1653` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 33,810.00 USD | 12,460.00 USD | 28,440.00 USD |
| `1D` | `0.1655` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 40,490.00 USD | 34,800.00 USD | 29,550.00 USD |
| `7D` | `0.1656` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 0.00 USD | 19,330.00 USD | 33,380.00 USD |
| `1D` | `0.1658` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 54,340.00 USD | 47,930.00 USD | 45,640.00 USD |
| `7D` | `0.1659` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 40,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1661` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 30,850.00 USD | 11,150.00 USD | 64,080.00 USD |
| `7D` | `0.1662` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 48,590.00 USD | 62,020.00 USD | 81,010.00 USD |
| `1D` | `0.1664` | 989,470.00 USD | 0.00 USD | 989,470.00 USD | 48,150.00 USD | 59,110.00 USD | 67,240.00 USD |
| `7D` | `0.1665` | 922,350.00 USD | 0.00 USD | 922,350.00 USD | 87,050.00 USD | 32,780.00 USD | 57,360.00 USD |
| `1D` | `0.1667` | 814,970.00 USD | 0.00 USD | 814,970.00 USD | 105,350.00 USD | 72,210.00 USD | 53,200.00 USD |
| `7D` | `0.1668` | 745,150.00 USD | 0.00 USD | 745,150.00 USD | 11,410.00 USD | 39,630.00 USD | 42,720.00 USD |
| `1D` | `0.1670` | 584,200.00 USD | 0.00 USD | 584,200.00 USD | 64,200.00 USD | 29,020.00 USD | 27,120.00 USD |
| `7D` | `0.1671` | 651,400.00 USD | 0.00 USD | 651,400.00 USD | 70,540.00 USD | 62,490.00 USD | 0.00 USD |
| `1D` | `0.1673` | 463,850.00 USD | 0.00 USD | 463,850.00 USD | 42,030.00 USD | 31,130.00 USD | 18,410.00 USD |
| `7D` | `0.1674` | 518,370.00 USD | 0.00 USD | 518,370.00 USD | 44,960.00 USD | 88,950.00 USD | 0.00 USD |
| `1D` | `0.1676` | 372,280.00 USD | 0.00 USD | 372,280.00 USD | 14,620.00 USD | 33,240.00 USD | 23,510.00 USD |
| `7D` | `0.1677` | 384,460.00 USD | 0.00 USD | 384,460.00 USD | 59,010.00 USD | 64,850.00 USD | 0.00 USD |
| `1D` | `0.1679` | 300,900.00 USD | 0.00 USD | 300,900.00 USD | 6,270.00 USD | 5,070.00 USD | 22,430.00 USD |
| `7D` | `0.1680` | 260,600.00 USD | 0.00 USD | 260,600.00 USD | 101,910.00 USD | 68,430.00 USD | 15,310.00 USD |
| `1D` | `0.1682` | 267,150.00 USD | 0.00 USD | 267,150.00 USD | 144,140.00 USD | 38,540.00 USD | 32,240.00 USD |
| `7D` | `0.1683` | 74,950.00 USD | 0.00 USD | 74,950.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD |
| `1D` | `0.1685` | 52,230.00 USD | 0.00 USD | 52,230.00 USD | 13,810.00 USD | 26,600.00 USD | 11,810.00 USD |
| `1D` | `0.1686` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1688` | 8,570.00 USD | 8,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,570.00 USD |
| `7D` | `0.1688` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1689` | 38,670.00 USD | 38,670.00 USD | 0.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD |
| `1D` | `0.1691` | 123,820.00 USD | 123,820.00 USD | 0.00 USD | 42,110.00 USD | 73,140.00 USD | 0.00 USD |
| `7D` | `0.1692` | 92,520.00 USD | 92,520.00 USD | 0.00 USD | 21,780.00 USD | 32,070.00 USD | 0.00 USD |
| `1D` | `0.1694` | 159,330.00 USD | 159,330.00 USD | 0.00 USD | 13,210.00 USD | 22,300.00 USD | 0.00 USD |
| `7D` | `0.1695` | 151,020.00 USD | 151,020.00 USD | 0.00 USD | 0.00 USD | 30,490.00 USD | 28,010.00 USD |
| `1D` | `0.1697` | 202,310.00 USD | 202,310.00 USD | 0.00 USD | 7,460.00 USD | 35,530.00 USD | 0.00 USD |
| `7D` | `0.1698` | 226,700.00 USD | 226,700.00 USD | 0.00 USD | 0.00 USD | 56,860.00 USD | 18,830.00 USD |
| `1D` | `0.1700` | 223,470.00 USD | 223,470.00 USD | 0.00 USD | 0.00 USD | 21,160.00 USD | 0.00 USD |
| `7D` | `0.1701` | 274,850.00 USD | 274,850.00 USD | 0.00 USD | 22,820.00 USD | 25,330.00 USD | 0.00 USD |
| `1D` | `0.1703` | 248,130.00 USD | 248,130.00 USD | 0.00 USD | 0.00 USD | 14,420.00 USD | 10,240.00 USD |
| `7D` | `0.1704` | 321,740.00 USD | 321,740.00 USD | 0.00 USD | 0.00 USD | 46,880.00 USD | 0.00 USD |
| `1D` | `0.1706` | 280,730.00 USD | 280,730.00 USD | 0.00 USD | 22,060.00 USD | 6,390.00 USD | 4,150.00 USD |
| `7D` | `0.1707` | 381,260.00 USD | 381,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 59,520.00 USD |
| `1D` | `0.1709` | 358,900.00 USD | 358,900.00 USD | 0.00 USD | 15,910.00 USD | 62,270.00 USD | 0.00 USD |
| `7D` | `0.1710` | 411,920.00 USD | 411,920.00 USD | 0.00 USD | 0.00 USD | 25,490.00 USD | 5,180.00 USD |
| `1D` | `0.1712` | 369,030.00 USD | 369,030.00 USD | 0.00 USD | 0.00 USD | 10,130.00 USD | 0.00 USD |
| `7D` | `0.1713` | 453,940.00 USD | 453,940.00 USD | 0.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD |
| `1D` | `0.1715` | 390,070.00 USD | 390,070.00 USD | 0.00 USD | 0.00 USD | 21,040.00 USD | 0.00 USD |
| `1D` | `0.1718` | 407,940.00 USD | 407,940.00 USD | 0.00 USD | 9,350.00 USD | 8,520.00 USD | 0.00 USD |
| `1D` | `0.1721` | 502,020.00 USD | 502,020.00 USD | 0.00 USD | 77,220.00 USD | 16,860.00 USD | 0.00 USD |
| `7D` | `0.1722` | 853,960.00 USD | 853,960.00 USD | 0.00 USD | 74,150.00 USD | 0.00 USD | 325,870.00 USD |
| `1D` | `0.1724` | 521,330.00 USD | 521,330.00 USD | 0.00 USD | 8,110.00 USD | 0.00 USD | 11,190.00 USD |
| `1D` | `0.1727` | 529,890.00 USD | 529,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,570.00 USD |
| `1D` | `0.1730` | 544,840.00 USD | 544,840.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 6,720.00 USD |
| `7D` | `0.1731` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 493,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1733` | 554,910.00 USD | 554,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,060.00 USD |
| `1D` | `0.1736` | 579,390.00 USD | 579,390.00 USD | 0.00 USD | 14,970.00 USD | 9,510.00 USD | 0.00 USD |
| `7D` | `0.1737` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 52,610.00 USD |
| `1D` | `0.1739` | 603,610.00 USD | 603,610.00 USD | 0.00 USD | 14,580.00 USD | 0.00 USD | 9,640.00 USD |
| `7D` | `0.1740` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,200.00 USD |
| `1D` | `0.1742` | 613,580.00 USD | 613,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,960.00 USD |
| `7D` | `0.1743` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1745` | 628,350.00 USD | 628,350.00 USD | 0.00 USD | 8,530.00 USD | 0.00 USD | 6,240.00 USD |
| `1D` | `0.1748` | 723,240.00 USD | 723,240.00 USD | 0.00 USD | 55,280.00 USD | 0.00 USD | 39,610.00 USD |
| `7D` | `0.1749` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `0.1751` | 771,780.00 USD | 771,780.00 USD | 0.00 USD | 37,840.00 USD | 0.00 USD | 10,700.00 USD |
| `7D` | `0.1752` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 263,630.00 USD |
| `1D` | `0.1754` | 830,590.00 USD | 830,590.00 USD | 0.00 USD | 16,720.00 USD | 8,430.00 USD | 33,650.00 USD |
| `7D` | `0.1755` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 37,610.00 USD | 0.00 USD | 169,120.00 USD |
| `1D` | `0.1757` | 928,850.00 USD | 928,850.00 USD | 0.00 USD | 13,030.00 USD | 40,160.00 USD | 45,080.00 USD |
| `7D` | `0.1758` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 173,440.00 USD | 38,670.00 USD | 8,600.00 USD |
| `1D` | `0.1760` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 85,150.00 USD | 76,400.00 USD | 17,520.00 USD |
| `7D` | `0.1761` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 373,120.00 USD | 131,090.00 USD | 32,350.00 USD |
| `1D` | `0.1763` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 88,670.00 USD | 20,760.00 USD | 68,500.00 USD |
| `7D` | `0.1764` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 144,160.00 USD | 215,620.00 USD | 40,340.00 USD |
| `1D` | `0.1766` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 24,650.00 USD | 20,220.00 USD | 68,390.00 USD |
| `7D` | `0.1767` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 176,410.00 USD | 143,320.00 USD | 8,530.00 USD |
| `1D` | `0.1769` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 53,350.00 USD | 91,810.00 USD | 44,210.00 USD |
| `7D` | `0.1770` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 61,490.00 USD | 147,940.00 USD | 44,400.00 USD |
| `1D` | `0.1772` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 22,380.00 USD | 20,220.00 USD | 28,530.00 USD |
| `7D` | `0.1773` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 103,820.00 USD | 105,810.00 USD | 0.00 USD |
| `1D` | `0.1775` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 74,270.00 USD | 27,710.00 USD | 7,600.00 USD |
| `7D` | `0.1776` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 135,140.00 USD | 69,570.00 USD | 0.00 USD |
| `1D` | `0.1778` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 58,020.00 USD | 87,510.00 USD | 24,860.00 USD |
| `7D` | `0.1779` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 52,730.00 USD | 46,410.00 USD | 131,820.00 USD |
| `1D` | `0.1781` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 50,570.00 USD | 1,060.00 USD | 45,750.00 USD |
| `7D` | `0.1782` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 20,690.00 USD | 13,990.00 USD | 31,180.00 USD |
| `1D` | `0.1784` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 92,690.00 USD | 38,240.00 USD | 23,260.00 USD |
| `7D` | `0.1785` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 153,160.00 USD | 78,850.00 USD | 16,420.00 USD |
| `1D` | `0.1787` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 37,680.00 USD | 54,820.00 USD | 51,690.00 USD |
| `7D` | `0.1788` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 73,130.00 USD | 18,250.00 USD | 14,040.00 USD |
| `1D` | `0.1790` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 53,220.00 USD | 22,930.00 USD | 21,120.00 USD |
| `7D` | `0.1791` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 155,720.00 USD | 17,360.00 USD | 3,940.00 USD |
| `1D` | `0.1793` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 32,720.00 USD | 20,810.00 USD | 20,480.00 USD |
| `7D` | `0.1794` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 27,100.00 USD | 42,780.00 USD | 36,780.00 USD |
| `1D` | `0.1796` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 48,060.00 USD | 66,080.00 USD | 41,280.00 USD |
| `7D` | `0.1797` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 17,130.00 USD | 12,930.00 USD | 7,670.00 USD |
| `1D` | `0.1799` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 16,820.00 USD | 14,880.00 USD | 15,390.00 USD |
| `7D` | `0.1800` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 34,680.00 USD | 64,620.00 USD |
| `1D` | `0.1802` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 15,140.00 USD | 34,770.00 USD | 28,710.00 USD |
| `7D` | `0.1803` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 35,280.00 USD | 25,700.00 USD | 18,250.00 USD |
| `1D` | `0.1805` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 22,680.00 USD | 9,380.00 USD | 27,960.00 USD |
| `7D` | `0.1806` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 11,410.00 USD | 56,850.00 USD | 19,880.00 USD |
| `1D` | `0.1808` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 24,170.00 USD | 27,870.00 USD | 35,880.00 USD |
| `7D` | `0.1809` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 53,670.00 USD | 30,810.00 USD | 58,890.00 USD |
| `1D` | `0.1811` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 39,150.00 USD | 16,000.00 USD | 24,930.00 USD |
| `7D` | `0.1812` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 34,960.00 USD | 16,640.00 USD | 50,510.00 USD |
| `1D` | `0.1814` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 27,380.00 USD | 36,930.00 USD | 28,610.00 USD |
| `7D` | `0.1815` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 60,010.00 USD | 30,810.00 USD | 38,270.00 USD |
| `1D` | `0.1817` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 31,330.00 USD | 11,020.00 USD | 30,640.00 USD |
| `7D` | `0.1818` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 75,040.00 USD | 24,140.00 USD | 10,390.00 USD |
| `1D` | `0.1820` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 32,520.00 USD | 18,550.00 USD | 4,990.00 USD |
| `7D` | `0.1821` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 40,950.00 USD | 33,870.00 USD | 41,820.00 USD |
| `1D` | `0.1823` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 16,740.00 USD | 19,980.00 USD | 17,470.00 USD |
| `7D` | `0.1824` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 39,400.00 USD | 17,880.00 USD | 95,310.00 USD |
| `1D` | `0.1826` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 24,740.00 USD | 6,860.00 USD | 4,500.00 USD |
| `7D` | `0.1827` | 6,310,000.00 USD | 6,310,000.00 USD | 0.00 USD | 79,610.00 USD | 18,690.00 USD | 65,670.00 USD |
| `1D` | `0.1829` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 1,640.00 USD | 2,530.00 USD |
| `7D` | `0.1830` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 64,890.00 USD | 20,550.00 USD | 52,010.00 USD |
| `1D` | `0.1832` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 2,880.00 USD | 9,980.00 USD |
| `7D` | `0.1833` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 186,730.00 USD | 49,740.00 USD | 26,350.00 USD |
| `1D` | `0.1835` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 3,610.00 USD | 0.00 USD | 728.16 USD |
| `7D` | `0.1836` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 29,580.00 USD | 83,110.00 USD | 52,650.00 USD |
| `1D` | `0.1838` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 2,640.00 USD | 5,780.00 USD |
| `7D` | `0.1839` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 129,950.00 USD | 41,230.00 USD | 114,190.00 USD |
| `1D` | `0.1841` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 13,150.00 USD | 1,090.00 USD | 7,910.00 USD |
| `7D` | `0.1842` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 71,550.00 USD | 26,100.00 USD | 97,700.00 USD |
| `1D` | `0.1844` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 2,690.00 USD | 4,460.00 USD | 12,790.00 USD |
| `7D` | `0.1845` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 34,630.00 USD | 33,340.00 USD | 66,720.00 USD |
| `1D` | `0.1847` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 7,630.00 USD | 7,150.00 USD | 11,230.00 USD |
| `7D` | `0.1848` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 47,730.00 USD | 75,080.00 USD | 135,290.00 USD |
| `1D` | `0.1850` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD | 1,300.00 USD |
| `7D` | `0.1851` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 94,780.00 USD | 28,290.00 USD | 220,580.00 USD |
| `1D` | `0.1853` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 1,690.00 USD | 4,440.00 USD |
| `7D` | `0.1854` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 105,210.00 USD | 4,290.00 USD | 63,060.00 USD |
| `1D` | `0.1856` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 11,550.00 USD | 2,630.00 USD | 7,420.00 USD |
| `7D` | `0.1857` | 8,540,000.00 USD | 8,540,000.00 USD | 0.00 USD | 116,320.00 USD | 32,070.00 USD | 127,480.00 USD |
| `1D` | `0.1859` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 9,450.00 USD | 1,470.00 USD | 5,910.00 USD |
| `7D` | `0.1860` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 87,180.00 USD | 72,430.00 USD | 74,870.00 USD |
| `1D` | `0.1862` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 1,870.00 USD | 2,970.00 USD | 7,150.00 USD |
| `7D` | `0.1863` | 8,960,000.00 USD | 8,960,000.00 USD | 0.00 USD | 71,330.00 USD | 56,440.00 USD | 61,380.00 USD |
| `1D` | `0.1865` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,510.00 USD |
| `7D` | `0.1866` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 101,070.00 USD | 33,740.00 USD | 39,240.00 USD |
| `1D` | `0.1868` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 3,300.00 USD | 0.00 USD | 7,070.00 USD |
| `7D` | `0.1869` | 9,450,000.00 USD | 9,450,000.00 USD | 0.00 USD | 169,650.00 USD | 66,330.00 USD | 78,120.00 USD |
| `1D` | `0.1871` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 11,950.00 USD | 6,940.00 USD | 9,870.00 USD |
| `7D` | `0.1872` | 9,760,000.00 USD | 9,760,000.00 USD | 0.00 USD | 80,790.00 USD | 132,480.00 USD | 93,980.00 USD |
| `1D` | `0.1874` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 7,320.00 USD | 2,820.00 USD | 2,290.00 USD |
| `7D` | `0.1875` | 9,900,000.00 USD | 9,900,000.00 USD | 0.00 USD | 68,250.00 USD | 37,700.00 USD | 36,560.00 USD |
| `1D` | `0.1877` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 2,670.00 USD | 2,760.00 USD | 918.24 USD |
| `7D` | `0.1878` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 66,470.00 USD | 37,330.00 USD | 48,000.00 USD |
| `1D` | `0.1880` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 4,530.00 USD | 3,160.00 USD | 8,370.00 USD |
| `7D` | `0.1881` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 29,820.00 USD | 44,080.00 USD | 13,200.00 USD |
| `1D` | `0.1883` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 4,630.00 USD | 4,960.00 USD | 0.00 USD |
| `7D` | `0.1884` | 10,250,000.00 USD | 10,250,000.00 USD | 0.00 USD | 10,560.00 USD | 36,820.00 USD | 58,860.00 USD |
| `1D` | `0.1886` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 13,740.00 USD | 2,220.00 USD | 6,220.00 USD |
| `7D` | `0.1887` | 10,300,000.00 USD | 10,300,000.00 USD | 0.00 USD | 22,970.00 USD | 0.00 USD | 25,760.00 USD |
| `1D` | `0.1889` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 3,580.00 USD | 3,150.00 USD | 7,640.00 USD |
| `7D` | `0.1890` | 10,420,000.00 USD | 10,420,000.00 USD | 0.00 USD | 36,740.00 USD | 17,330.00 USD | 75,130.00 USD |
| `1D` | `0.1892` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 1,140.00 USD | 8,660.00 USD | 1,070.00 USD |
| `7D` | `0.1893` | 10,480,000.00 USD | 10,480,000.00 USD | 0.00 USD | 32,450.00 USD | 6,940.00 USD | 16,820.00 USD |
| `1D` | `0.1895` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 4,810.00 USD | 4,140.00 USD | 3,890.00 USD |
| `7D` | `0.1896` | 10,590,000.00 USD | 10,590,000.00 USD | 0.00 USD | 62,730.00 USD | 27,440.00 USD | 18,680.00 USD |
| `1D` | `0.1898` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 7,030.00 USD | 16,880.00 USD | 0.00 USD |
| `7D` | `0.1899` | 10,660,000.00 USD | 10,660,000.00 USD | 0.00 USD | 11,530.00 USD | 38,530.00 USD | 20,420.00 USD |
| `1D` | `0.1901` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 11,640.00 USD | 4,150.00 USD | 7,190.00 USD |
| `7D` | `0.1902` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 14,330.00 USD | 0.00 USD | 10,800.00 USD |
| `1D` | `0.1904` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 1,660.00 USD | 8,830.00 USD |
| `7D` | `0.1905` | 10,740,000.00 USD | 10,740,000.00 USD | 0.00 USD | 8,720.00 USD | 24,800.00 USD | 24,210.00 USD |
| `1D` | `0.1907` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 2,490.00 USD | 11,300.00 USD | 6,450.00 USD |
| `7D` | `0.1908` | 10,840,000.00 USD | 10,840,000.00 USD | 0.00 USD | 25,220.00 USD | 43,160.00 USD | 28,600.00 USD |
| `1D` | `0.1910` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 1,050.00 USD | 1,140.00 USD |
| `7D` | `0.1911` | 10,850,000.00 USD | 10,850,000.00 USD | 0.00 USD | 0.00 USD | 9,380.00 USD | 0.00 USD |
| `7D` | `0.1914` | 10,870,000.00 USD | 10,870,000.00 USD | 0.00 USD | 7,460.00 USD | 11,160.00 USD | 0.00 USD |
| `7D` | `0.1917` | 10,890,000.00 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 11,840.00 USD | 11,900.00 USD |
| `7D` | `0.1923` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD |
| `7D` | `0.1926` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 11,600.00 USD | 13,630.00 USD | 0.00 USD |
| `7D` | `0.1944` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `207.94M` | Total OI Tokens: `1,233,363,857.3 ARB`
  * 1h OI Change: `-2.02%` | 4h OI Change: `-2.41%` | 24h OI Change: `-12.65%`
  * Exchange Breakdown: Binance=`47.57M` | Bybit=`28.87M` | OKX=`16.81M` | Hyperliquid=`15.03M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `9.33K` | Last 24h: `10.97K` | Last 3d: `22.34K` | Last 7d: `43.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `45.69%` | `54.31%` | `0.84` | 730,190.00 USD |
| `15M` | `Binance` | `41.99%` | `58.01%` | `0.72` | 271,220.00 USD |
| `15M` | `OKX` | `53.28%` | `46.72%` | `1.14` | 77,890.00 USD |
| `15M` | `Bybit` | `44.15%` | `55.85%` | `0.79` | 86,910.00 USD |
| `15M` | `KuCoin` | `49.71%` | `50.29%` | `0.99` | 1,540.00 USD |
| `15M` | `Gate` | `36.54%` | `63.46%` | `0.58` | 5,040.00 USD |
| `15M` | `Bitget` | `28.33%` | `71.67%` | `0.40` | 9,140.00 USD |
| `15M` | `BingX` | `49.5%` | `50.5%` | `0.98` | 75,230.00 USD |
| `15M` | `MEXC` | `60.14%` | `39.86%` | `1.51` | 5,950.00 USD |
| `15M` | `Bitunix` | `42.15%` | `57.85%` | `0.73` | 6,270.00 USD |
| `15M` | `Hyperliquid` | `66.26%` | `33.74%` | `1.96` | 3,350.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `47.9%` | `52.1%` | `0.92` | 152,050.00 USD |
| `15M` | `Crypto.com` | `64.4%` | `35.6%` | `1.81` | 0.00 USD |
| `15M` | `WhiteBIT` | `81.39%` | `18.61%` | `4.37` | 35,140.00 USD |
| `15M` | `HTX` | `62.95%` | `37.05%` | `1.70` | 42.21 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `1%` | `99%` | `0.01` | 15.53 USD |
| `15M` | `Aster` | `0.88%` | `99.12%` | `0.01` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `74%` | `26%` | `2.85` | 426.38 USD |
| `15M` | `Whale Positions` | `41.99%` | `58.01%` | `0.72` | 271,220.00 USD |
| `15M` | `Global Accounts` | `45.69%` | `54.31%` | `0.84` | 730,190.00 USD |
| `1H` | `ARB` | `45.97%` | `54.03%` | `0.85` | 10,570,000.00 USD |
| `1H` | `Binance` | `48.19%` | `51.81%` | `0.93` | 4,340,000.00 USD |
| `1H` | `OKX` | `45.65%` | `54.35%` | `0.84` | 1,730,000.00 USD |
| `1H` | `Bybit` | `50.3%` | `49.7%` | `1.01` | 813,220.00 USD |
| `1H` | `KuCoin` | `46.47%` | `53.53%` | `0.87` | 133,710.00 USD |
| `1H` | `Gate` | `48.07%` | `51.93%` | `0.93` | 456,300.00 USD |
| `1H` | `Bitget` | `37.11%` | `62.89%` | `0.59` | 447,640.00 USD |
| `1H` | `BingX` | `15.34%` | `84.66%` | `0.18` | 623,740.00 USD |
| `1H` | `MEXC` | `46.75%` | `53.25%` | `0.88` | 818,170.00 USD |
| `1H` | `Bitunix` | `45.47%` | `54.53%` | `0.83` | 168,360.00 USD |
| `1H` | `Hyperliquid` | `41.44%` | `58.56%` | `0.71` | 196,730.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.6%` | `50.4%` | `0.98` | 495,440.00 USD |
| `1H` | `Crypto.com` | `67.78%` | `32.22%` | `2.10` | 7,570.00 USD |
| `1H` | `WhiteBIT` | `83.42%` | `16.58%` | `5.03` | 264,070.00 USD |
| `1H` | `HTX` | `10.14%` | `89.86%` | `0.11` | 2,260.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `19.1%` | `80.9%` | `0.24` | 56,200.00 USD |
| `1H` | `Aster` | `9.84%` | `90.16%` | `0.11` | 2,790.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `32.35%` | `67.65%` | `0.48` | 30,370.00 USD |
| `1H` | `Whale Positions` | `48.19%` | `51.81%` | `0.93` | 4,340,000.00 USD |
| `1H` | `Global Accounts` | `45.97%` | `54.03%` | `0.85` | 10,570,000.00 USD |
| `4H` | `ARB` | `47.20%` | `52.80%` | `0.89` | 59,740,000.00 USD |
| `4H` | `Binance` | `45.44%` | `54.56%` | `0.83` | 22,220,000.00 USD |
| `4H` | `OKX` | `48.24%` | `51.76%` | `0.93` | 11,940,000.00 USD |
| `4H` | `Bybit` | `48.69%` | `51.31%` | `0.95` | 4,990,000.00 USD |
| `4H` | `KuCoin` | `48.44%` | `51.56%` | `0.94` | 599,310.00 USD |
| `4H` | `Gate` | `49.86%` | `50.14%` | `0.99` | 1,630,000.00 USD |
| `4H` | `Bitget` | `48.4%` | `51.6%` | `0.94` | 3,020,000.00 USD |
| `4H` | `BingX` | `32.65%` | `67.35%` | `0.48` | 3,020,000.00 USD |
| `4H` | `MEXC` | `44.61%` | `55.39%` | `0.81` | 4,840,000.00 USD |
| `4H` | `Bitunix` | `48.79%` | `51.21%` | `0.95` | 1,350,000.00 USD |
| `4H` | `Hyperliquid` | `52.72%` | `47.28%` | `1.12` | 1,820,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.22%` | `50.78%` | `0.97` | 2,640,000.00 USD |
| `4H` | `Crypto.com` | `54.38%` | `45.62%` | `1.19` | 30,100.00 USD |
| `4H` | `WhiteBIT` | `84.67%` | `15.33%` | `5.52` | 1,240,000.00 USD |
| `4H` | `HTX` | `48.23%` | `51.77%` | `0.93` | 14,770.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.12%` | `50.88%` | `0.97` | 183,760.00 USD |
| `4H` | `Aster` | `87.22%` | `12.78%` | `6.82` | 65,910.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.29%` | `52.71%` | `0.90` | 133,630.00 USD |
| `4H` | `Whale Positions` | `45.44%` | `54.56%` | `0.83` | 22,220,000.00 USD |
| `4H` | `Global Accounts` | `47.20%` | `52.80%` | `0.89` | 59,740,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1740` | `0.1746` | `0.1740` | `0.1759` | `0.1738` | 1,727,950.91 USD | 719,456.36 USD | 1,008,494.54 USD | -289,038.18 USD | `-16.73%` | `12B / 27S` |
| `5:00 UTC` | `0.1735` | `0.1735` | `0.1735` | `0.1745` | `0.1727` | 1,465,256.89 USD | 552,173.71 USD | 913,083.17 USD | -360,909.46 USD | `-24.63%` | `12B / 58S` |
| `0:00 UTC` | `0.1724` | `0.1726` | `0.1724` | `0.1732` | `0.1721` | 813,790.61 USD | 314,421.23 USD | 499,369.38 USD | -184,948.15 USD | `-22.73%` | `12B / 32S` |
| `5:00 UTC` | `0.1722` | `0.1719` | `0.1722` | `0.1724` | `0.1714` | 868,922.61 USD | 333,299.44 USD | 535,623.17 USD | -202,323.73 USD | `-23.28%` | `11B / 37S` |
| `0:00 UTC` | `0.1715` | `0.1718` | `0.1715` | `0.1727` | `0.1712` | 1,082,802.27 USD | 363,691.86 USD | 719,110.40 USD | -355,418.54 USD | `-32.82%` | `13B / 48S` |
| `5:00 UTC` | `0.1711` | `0.1711` | `0.1711` | `0.1716` | `0.1708` | 800,876.04 USD | 410,736.84 USD | 390,139.20 USD | 20,597.64 USD | `+2.57%` | `7B / 12S` |
| `0:00 UTC` | `0.1710` | `0.1702` | `0.1710` | `0.1719` | `0.1689` | 1,300,882.78 USD | 531,501.17 USD | 769,381.61 USD | -237,880.44 USD | `-18.29%` | `17B / 38S` |
| `5:00 UTC` | `0.1689` | `0.1689` | `0.1689` | `0.1697` | `0.1682` | 1,292,914.43 USD | 712,068.28 USD | 580,846.15 USD | 131,222.13 USD | `+10.15%` | `38B / 24S` |
| `0:00 UTC` | `0.1690` | `0.1697` | `0.1690` | `0.1704` | `0.1690` | 952,197.22 USD | 428,970.00 USD | 523,227.22 USD | -94,257.22 USD | `-9.90%` | `28B / 31S` |
| `5:00 UTC` | `0.1692` | `0.1694` | `0.1692` | `0.1698` | `0.1691` | 294,508.25 USD | 163,512.58 USD | 130,995.68 USD | 32,516.90 USD | `+11.04%` | `23B / 15S` |

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
| `5m` | -4,330.00 USD | 58,390.00 USD | **`ACCUMULATION`** |
| `15m` | -188,020.00 USD | -139,800.00 USD | **`DISTRIBUTION`** |
| `30m` | 70,280.00 USD | 337,430.00 USD | **`ACCUMULATION`** |
| `1h` | 21,460.00 USD | -384,960.00 USD | **`DISTRIBUTION`** |
| `2h` | -16,170.00 USD | -1,910,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 68,910.00 USD | -2,410,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 110,820.00 USD | -3,480,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 387,910.00 USD | -4,180,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 64,980.00 USD | -4,700,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -346,630.00 USD | -7,510,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -4,520,000.00 USD | -29,360,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -32,110,000.00 USD | -163,440,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-4.33K` | 15m=`-188.02K` | 1h=`+21.46K` | 24h=`-346.63K`
* Futures Capital Netflows: 5m=`+58.39K` | 15m=`-139.80K` | 1h=`-384.96K` | 24h=`-7.51M`
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
  * `2026-10-29 23:31:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:51:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:51:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:52:26 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:52:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
