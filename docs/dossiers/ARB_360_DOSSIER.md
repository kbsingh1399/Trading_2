# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-29 22:52:02 IST` (`2026-10-29 17:22:02 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1724` | `0.1727` | `0.1720` | `0.1723` | `1,463,409` | 252,357.83 USD | 10,857.02 USD | `+4.30%` | -4,556,699.44 USD | `+0.68` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1723` | `0.1723` | `0.1712` | `0.1715` | `3,102,669` | 532,450.71 USD | -265,720.95 USD | `-49.91%` | -4,822,420.40 USD | `-1.83` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1715` | `0.1716` | `0.1713` | `0.1716` | `1,475,262` | 252,912.51 USD | -103,012.85 USD | `-40.73%` | -4,925,433.25 USD | `-0.24` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1728` | `0.1731` | `0.1721` | `0.1723` | `4,715,996` | 813,790.61 USD | -184,948.15 USD | `-22.73%` | -4,365,232.73 USD | `-0.55` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1723` | `0.1724` | `0.1714` | `0.1724` | `5,054,136` | 868,922.61 USD | -202,323.73 USD | `-23.28%` | -4,567,556.46 USD | `-0.59` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1724` | `0.1727` | `0.1712` | `0.1716` | `6,052,886` | 1,039,702.25 USD | -355,960.34 USD | `-34.24%` | -4,923,516.80 USD | `-1.44` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1718` | `0.1749` | `0.1711` | `0.1745` | `29,066,557` | 5,034,866.28 USD | -62,899.27 USD | `-1.25%` | -3,873,851.47 USD | `+0.22` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1745` | `0.1759` | `0.1714` | `0.1724` | `28,115,276` | 4,875,921.02 USD | -1,037,219.52 USD | `-21.27%` | -4,911,070.99 USD | `-2.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1724` | `0.1727` | `0.1712` | `0.1716` | `6,041,339` | 1,037,721.05 USD | -357,876.79 USD | `-34.49%` | -5,268,947.78 USD | `-0.39` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,634,787.89 USD | `-0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,872,916.24 USD | `-1.36` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1712` | `0.1716` | `34,156,616` | 5,913,642.07 USD | -1,395,096.31 USD | `-23.59%` | -4,268,012.54 USD | `-1.27` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1721` | `0.1729` | `0.1635` | `0.1652` | `91,809,989` | 15,344,891.97 USD | 203,909.29 USD | `+1.33%` | -294,464.16 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1652` | `0.1687` | `0.1623` | `0.1631` | `68,085,678` | 11,252,816.65 USD | -909,329.92 USD | `-8.08%` | -1,203,794.08 USD | `-1.11` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,634,787.89 USD | `-0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,872,916.24 USD | `-1.36` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1712` | `0.1716` | `34,156,616` | 5,913,642.07 USD | -1,395,096.31 USD | `-23.59%` | -4,268,012.54 USD | `-1.27` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:44:58 IST` |

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
  * 24H Horizon: Short MP=`0.1784` (Vol: 147,300.00 USD, Dist: `+4.30%`) | Long MP=`0.1598` (Vol: 147,500.00 USD, Dist: `--6.58%`)
  * 48H Horizon: Short MP=`0.1784` (Vol: 147,300.00 USD, Dist: `+4.30%`) | Long MP=`0.1598` (Vol: 154,300.00 USD, Dist: `--6.58%`)
  * 3D Horizon: Short MP=`0.1784` (Vol: 147,300.00 USD, Dist: `+4.30%`) | Long MP=`0.1598` (Vol: 205,900.00 USD, Dist: `--6.58%`)
  * 7D Horizon: Short MP=`0.1834` (Vol: 181,500.00 USD, Dist: `+7.20%`) | Long MP=`0.1616` (Vol: 292,500.00 USD, Dist: `--5.51%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0365` | 2,370.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0375` | 1,750.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0385` | 1,490.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 9,460.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 170.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0465` | 273.75 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 109.52 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 204.38 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 964.65 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 945.32 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 6,080.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 15,970.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 628.38 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 3,140.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 242.06 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 86,100.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 579.79 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 99,790.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 2,290.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 143.87 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 2,970.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 24,170.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 111.58 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,440.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 226.17 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 1,470.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 23,780.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 4,630.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 6,040.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 576.40 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 32,510.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 751.50 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 7,810.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 238.28 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 362.62 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 784.62 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 498.92 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 2,040.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 3,360.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 40,270.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 589.63 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 3,170.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 2,810.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 10,350.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 2,490.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1015` | 5,700.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 12,430.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,060.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 36,970.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 6,860.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 181.20 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 1,060.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 342.59 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 2,890.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 534.49 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 425.50 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1125` | 7,710.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 14,160.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 8,950.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 4,890.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 22,240.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 3,570.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 25,940.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 1,830.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 1,120.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 54,870.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 636.74 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 32,960.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 3,110.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 4,850.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 1,200.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 4,490.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 9,780.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 4,010.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 20,510.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 18,500.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 6,620.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 23,200.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 6,510.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 3,570.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1365` | 159,680.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1375` | 1,700.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1385` | 4,240.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1395` | 17,910.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 2,800.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 15,030.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 487,940.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 19,330.00 USD | 717,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 53,070.00 USD | 697,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1452` | 11,150,000.00 USD | 11,150,000.00 USD | 0.00 USD | 5,660.00 USD | 25,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1455` | 11,110,000.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 111.10 USD | 644,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1458` | 11,110,000.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 3,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1461` | 11,110,000.00 USD | 11,110,000.00 USD | 0.00 USD | 3,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1464` | 11,100,000.00 USD | 11,100,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 30,880.00 USD | 644,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1467` | 11,100,000.00 USD | 11,100,000.00 USD | 9,720.00 USD | 9,180.00 USD | 4,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1470` | 11,080,000.00 USD | 11,080,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1473` | 11,070,000.00 USD | 11,070,000.00 USD | 6,490.00 USD | 5,400.00 USD | 5,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 73,930.00 USD | 613,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1476` | 11,050,000.00 USD | 11,050,000.00 USD | 0.00 USD | 14,780.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1479` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 39,730.00 USD | 14,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1482` | 10,970,000.00 USD | 10,970,000.00 USD | 41,960.00 USD | 20,720.00 USD | 27,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1485` | 10,880,000.00 USD | 10,880,000.00 USD | 16,180.00 USD | 7,340.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,720.00 USD | 539,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1488` | 10,820,000.00 USD | 10,820,000.00 USD | 20,860.00 USD | 3,130.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1491` | 10,790,000.00 USD | 10,790,000.00 USD | 33,540.00 USD | 17,020.00 USD | 20,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1494` | 10,720,000.00 USD | 10,720,000.00 USD | 34,220.00 USD | 9,890.00 USD | 14,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 35,380.00 USD | 537,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1497` | 10,660,000.00 USD | 10,660,000.00 USD | 20,880.00 USD | 17,180.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1500` | 10,610,000.00 USD | 10,610,000.00 USD | 46,820.00 USD | 5,810.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1503` | 10,540,000.00 USD | 10,540,000.00 USD | 11,490.00 USD | 13,450.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1505` | 102,290.00 USD | 501,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1506` | 10,500,000.00 USD | 10,500,000.00 USD | 33,170.00 USD | 18,020.00 USD | 65,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1509` | 10,390,000.00 USD | 10,390,000.00 USD | 17,340.00 USD | 9,550.00 USD | 24,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1512` | 10,330,000.00 USD | 10,330,000.00 USD | 18,600.00 USD | 8,620.00 USD | 26,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1515` | 10,280,000.00 USD | 10,280,000.00 USD | 53,430.00 USD | 13,330.00 USD | 53,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 3,930.00 USD | 399,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1518` | 10,160,000.00 USD | 10,160,000.00 USD | 46,830.00 USD | 15,160.00 USD | 64,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1521` | 10,030,000.00 USD | 10,030,000.00 USD | 38,960.00 USD | 6,920.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1524` | 9,950,000.00 USD | 9,950,000.00 USD | 37,550.00 USD | 13,950.00 USD | 11,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1525` | 42,800.00 USD | 395,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1527` | 9,890,000.00 USD | 9,890,000.00 USD | 56,950.00 USD | 30,410.00 USD | 33,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1530` | 9,770,000.00 USD | 9,770,000.00 USD | 54,790.00 USD | 9,880.00 USD | 16,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1533` | 9,690,000.00 USD | 9,690,000.00 USD | 10,760.00 USD | 16,570.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1535` | 4,730,000.00 USD | 4,730,000.00 USD | 9,990.00 USD | 5,590.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 19,400.00 USD | 352,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1536` | 9,640,000.00 USD | 9,640,000.00 USD | 37,160.00 USD | 2,910.00 USD | 13,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1538` | 4,710,000.00 USD | 4,710,000.00 USD | 4,530.00 USD | 3,160.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1539` | 9,580,000.00 USD | 9,580,000.00 USD | 22,990.00 USD | 18,230.00 USD | 5,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1541` | 4,690,000.00 USD | 4,690,000.00 USD | 4,630.00 USD | 4,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1542` | 9,540,000.00 USD | 9,540,000.00 USD | 0.00 USD | 3,590.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1544` | 4,680,000.00 USD | 4,680,000.00 USD | 17,310.00 USD | 5,370.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1545` | 9,530,000.00 USD | 9,530,000.00 USD | 9,250.00 USD | 0.00 USD | 5,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1545` | 26,170.00 USD | 333,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1547` | 4,660,000.00 USD | 4,660,000.00 USD | 1,140.00 USD | 6,820.00 USD | 7,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1548` | 9,510,000.00 USD | 9,510,000.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1550` | 4,640,000.00 USD | 4,640,000.00 USD | 4,810.00 USD | 4,460.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1551` | 9,510,000.00 USD | 9,510,000.00 USD | 34,670.00 USD | 11,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1553` | 4,630,000.00 USD | 4,630,000.00 USD | 11,770.00 USD | 20,800.00 USD | 6,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1554` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 0.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1555` | 40,060.00 USD | 307,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1556` | 4,590,000.00 USD | 4,590,000.00 USD | 6,890.00 USD | 3,410.00 USD | 6,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1557` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 4,510.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1559` | 4,570,000.00 USD | 4,570,000.00 USD | 2,490.00 USD | 8,320.00 USD | 7,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1560` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 6,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1562` | 4,550,000.00 USD | 4,550,000.00 USD | 6,020.00 USD | 4,020.00 USD | 10,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1563` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 19,950.00 USD | 9,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1565` | 4,530,000.00 USD | 4,530,000.00 USD | 24,770.00 USD | 11,570.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1565` | 21,460.00 USD | 267,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1566` | 9,410,000.00 USD | 9,410,000.00 USD | 50,480.00 USD | 29,160.00 USD | 26,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1568` | 4,480,000.00 USD | 4,480,000.00 USD | 34,400.00 USD | 26,770.00 USD | 17,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1569` | 9,300,000.00 USD | 9,300,000.00 USD | 15,590.00 USD | 5,100.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1571` | 4,400,000.00 USD | 4,400,000.00 USD | 32,670.00 USD | 11,300.00 USD | 10,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1572` | 9,270,000.00 USD | 9,270,000.00 USD | 40,760.00 USD | 34,450.00 USD | 17,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1574` | 4,350,000.00 USD | 4,350,000.00 USD | 34,240.00 USD | 13,520.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1575` | 9,170,000.00 USD | 9,170,000.00 USD | 23,310.00 USD | 88,960.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1575` | 4,940.00 USD | 245,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1577` | 4,290,000.00 USD | 4,290,000.00 USD | 54,010.00 USD | 54,680.00 USD | 19,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1578` | 9,040,000.00 USD | 9,040,000.00 USD | 58,590.00 USD | 84,670.00 USD | 67,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1580` | 4,160,000.00 USD | 4,160,000.00 USD | 47,010.00 USD | 22,460.00 USD | 28,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1581` | 8,830,000.00 USD | 8,830,000.00 USD | 92,720.00 USD | 58,880.00 USD | 57,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1583` | 4,070,000.00 USD | 4,070,000.00 USD | 30,310.00 USD | 15,040.00 USD | 16,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1584` | 8,620,000.00 USD | 8,620,000.00 USD | 80,450.00 USD | 35,780.00 USD | 123,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1585` | 5,650.00 USD | 240,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1586` | 4,010,000.00 USD | 4,010,000.00 USD | 21,980.00 USD | 20,660.00 USD | 20,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1587` | 8,380,000.00 USD | 8,380,000.00 USD | 69,180.00 USD | 22,370.00 USD | 31,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1589` | 3,940,000.00 USD | 3,940,000.00 USD | 17,680.00 USD | 19,490.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1590` | 8,260,000.00 USD | 8,260,000.00 USD | 71,200.00 USD | 44,110.00 USD | 51,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1592` | 3,900,000.00 USD | 3,900,000.00 USD | 26,740.00 USD | 20,480.00 USD | 13,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1593` | 8,090,000.00 USD | 8,090,000.00 USD | 69,430.00 USD | 56,020.00 USD | 68,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1595` | 3,840,000.00 USD | 3,840,000.00 USD | 51,370.00 USD | 15,690.00 USD | 34,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1595` | 64,950.00 USD | 235,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1596` | 7,900,000.00 USD | 7,900,000.00 USD | 161,460.00 USD | 85,250.00 USD | 120,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1598` | 3,730,000.00 USD | 3,730,000.00 USD | 76,370.00 USD | 25,620.00 USD | 48,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1599` | 7,530,000.00 USD | 7,530,000.00 USD | 219,060.00 USD | 55,380.00 USD | 87,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1601` | 3,580,000.00 USD | 3,580,000.00 USD | 51,010.00 USD | 36,090.00 USD | 11,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1602` | 7,170,000.00 USD | 7,170,000.00 USD | 44,770.00 USD | 46,490.00 USD | 40,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1604` | 3,490,000.00 USD | 3,490,000.00 USD | 39,480.00 USD | 20,230.00 USD | 17,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1605` | 7,040,000.00 USD | 7,040,000.00 USD | 177,720.00 USD | 136,660.00 USD | 217,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1605` | 20,620.00 USD | 170,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1607` | 3,410,000.00 USD | 3,410,000.00 USD | 54,740.00 USD | 26,880.00 USD | 26,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1608` | 6,500,000.00 USD | 6,500,000.00 USD | 129,610.00 USD | 174,940.00 USD | 131,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1610` | 3,300,000.00 USD | 3,300,000.00 USD | 114,870.00 USD | 116,770.00 USD | 47,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1611` | 6,070,000.00 USD | 6,070,000.00 USD | 148,170.00 USD | 230,750.00 USD | 233,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1613` | 3,020,000.00 USD | 3,020,000.00 USD | 85,600.00 USD | 58,130.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1614` | 5,460,000.00 USD | 5,460,000.00 USD | 330,910.00 USD | 194,680.00 USD | 282,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1615` | 17,950.00 USD | 149,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1616` | 2,820,000.00 USD | 2,820,000.00 USD | 60,630.00 USD | 35,580.00 USD | 37,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1617` | 4,650,000.00 USD | 4,650,000.00 USD | 346,150.00 USD | 101,810.00 USD | 410,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1619` | 2,680,000.00 USD | 2,680,000.00 USD | 64,990.00 USD | 43,250.00 USD | 62,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1620` | 3,790,000.00 USD | 3,790,000.00 USD | 282,000.00 USD | 134,660.00 USD | 262,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1622` | 2,510,000.00 USD | 2,510,000.00 USD | 60,790.00 USD | 46,210.00 USD | 25,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1623` | 3,110,000.00 USD | 3,110,000.00 USD | 304,460.00 USD | 125,080.00 USD | 208,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1625` | 2,380,000.00 USD | 2,380,000.00 USD | 19,000.00 USD | 48,390.00 USD | 18,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1625` | 98,470.00 USD | 131,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1626` | 2,470,000.00 USD | 2,470,000.00 USD | 234,280.00 USD | 71,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1628` | 2,290,000.00 USD | 2,290,000.00 USD | 14,220.00 USD | 29,880.00 USD | 18,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1629` | 2,170,000.00 USD | 2,170,000.00 USD | 171,310.00 USD | 0.00 USD | 20,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1631` | 2,230,000.00 USD | 2,230,000.00 USD | 12,400.00 USD | 21,390.00 USD | 13,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1632` | 1,970,000.00 USD | 1,970,000.00 USD | 9,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1634` | 2,180,000.00 USD | 2,180,000.00 USD | 24,810.00 USD | 9,110.00 USD | 13,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1635` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 13,670.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1635` | 251.51 USD | 33,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1637` | 2,130,000.00 USD | 2,130,000.00 USD | 7,630.00 USD | 22,520.00 USD | 19,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1638` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 62,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1640` | 2,080,000.00 USD | 2,080,000.00 USD | 14,040.00 USD | 6,090.00 USD | 32,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1641` | 1,870,000.00 USD | 1,870,000.00 USD | 22,480.00 USD | 29,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1643` | 2,030,000.00 USD | 2,030,000.00 USD | 25,590.00 USD | 20,340.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1644` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 8,990.00 USD | 26,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1645` | 18,010.00 USD | 32,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1646` | 1,980,000.00 USD | 1,980,000.00 USD | 40,030.00 USD | 24,740.00 USD | 29,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1647` | 1,780,000.00 USD | 1,780,000.00 USD | 34,760.00 USD | 0.00 USD | 7,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1649` | 1,890,000.00 USD | 1,890,000.00 USD | 4,570.00 USD | 23,390.00 USD | 19,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1650` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 7,000.00 USD | 22,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1652` | 1,840,000.00 USD | 1,840,000.00 USD | 19,770.00 USD | 8,470.00 USD | 34,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1653` | 1,710,000.00 USD | 1,710,000.00 USD | 33,810.00 USD | 12,460.00 USD | 28,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1655` | 1,780,000.00 USD | 1,780,000.00 USD | 12,800.00 USD | 17,940.00 USD | 18,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1655` | 14,870.00 USD | 14,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1656` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 19,330.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1658` | 1,730,000.00 USD | 1,730,000.00 USD | 54,340.00 USD | 47,930.00 USD | 40,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1659` | 1,600,000.00 USD | 1,600,000.00 USD | 40,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1661` | 1,590,000.00 USD | 1,590,000.00 USD | 22,630.00 USD | 11,150.00 USD | 53,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1662` | 1,560,000.00 USD | 1,560,000.00 USD | 48,590.00 USD | 62,020.00 USD | 81,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1664` | 1,500,000.00 USD | 1,500,000.00 USD | 48,150.00 USD | 59,110.00 USD | 57,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1665` | 1,370,000.00 USD | 1,370,000.00 USD | 87,050.00 USD | 32,780.00 USD | 57,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1667` | 1,330,000.00 USD | 1,330,000.00 USD | 90,380.00 USD | 62,710.00 USD | 53,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1668` | 1,190,000.00 USD | 1,190,000.00 USD | 11,410.00 USD | 39,630.00 USD | 42,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1670` | 1,130,000.00 USD | 1,130,000.00 USD | 64,200.00 USD | 29,020.00 USD | 27,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1671` | 1,100,000.00 USD | 1,100,000.00 USD | 70,540.00 USD | 62,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1673` | 1,010,000.00 USD | 1,010,000.00 USD | 42,030.00 USD | 31,130.00 USD | 18,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1674` | 962,640.00 USD | 962,640.00 USD | 44,960.00 USD | 88,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1676` | 916,010.00 USD | 916,010.00 USD | 14,620.00 USD | 33,240.00 USD | 13,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1677` | 828,730.00 USD | 828,730.00 USD | 59,010.00 USD | 64,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1679` | 854,600.00 USD | 854,600.00 USD | 6,270.00 USD | 5,070.00 USD | 12,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1680` | 704,870.00 USD | 704,870.00 USD | 101,910.00 USD | 68,430.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1682` | 830,300.00 USD | 830,300.00 USD | 149,180.00 USD | 38,540.00 USD | 32,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1683` | 519,230.00 USD | 519,230.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1685` | 610,340.00 USD | 610,340.00 USD | 13,810.00 USD | 53,220.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1688` | 531,500.00 USD | 531,500.00 USD | 0.00 USD | 0.00 USD | 8,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1689` | 444,270.00 USD | 444,270.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1691` | 522,930.00 USD | 522,930.00 USD | 42,110.00 USD | 73,140.00 USD | 24,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1692` | 405,610.00 USD | 405,610.00 USD | 21,780.00 USD | 32,070.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1694` | 383,160.00 USD | 383,160.00 USD | 13,210.00 USD | 22,300.00 USD | 40,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1695` | 319,410.00 USD | 319,410.00 USD | 0.00 USD | 30,490.00 USD | 28,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1697` | 307,190.00 USD | 307,190.00 USD | 15,020.00 USD | 35,530.00 USD | 22,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1698` | 260,910.00 USD | 260,910.00 USD | 0.00 USD | 56,860.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1700` | 234,160.00 USD | 234,160.00 USD | 0.00 USD | 26,820.00 USD | 19,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1701` | 185,220.00 USD | 185,220.00 USD | 22,820.00 USD | 25,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1703` | 187,810.00 USD | 187,810.00 USD | 0.00 USD | 14,420.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1704` | 137,070.00 USD | 137,070.00 USD | 0.00 USD | 46,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1706` | 163,160.00 USD | 163,160.00 USD | 22,060.00 USD | 6,390.00 USD | 4,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1707` | 90,190.00 USD | 90,190.00 USD | 0.00 USD | 0.00 USD | 59,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1709` | 130,560.00 USD | 130,560.00 USD | 15,910.00 USD | 62,270.00 USD | 52,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1710` | 30,670.00 USD | 30,670.00 USD | 0.00 USD | 25,490.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1712` | 10,130.00 USD | 10,130.00 USD | 0.00 USD | 10,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1713` | 42,020.00 USD | 42,020.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1715` | 31,170.00 USD | 31,170.00 USD | 0.00 USD | 21,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1718` | 49,040.00 USD | 49,040.00 USD | 9,350.00 USD | 8,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1721` | 92,820.00 USD | 92,820.00 USD | 43,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1722` | 424,830.00 USD | 424,830.00 USD | 74,150.00 USD | 0.00 USD | 308,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1731` | 917,820.00 USD | 917,820.00 USD | 493,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1737` | 970,430.00 USD | 970,430.00 USD | 0.00 USD | 0.00 USD | 52,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1739` | 117,050.00 USD | 117,050.00 USD | 14,580.00 USD | 0.00 USD | 9,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1740` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 31,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1743` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1745` | 131,820.00 USD | 131,820.00 USD | 8,530.00 USD | 0.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1748` | 217,250.00 USD | 217,250.00 USD | 55,280.00 USD | 0.00 USD | 30,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1749` | 1,100,000.00 USD | 1,100,000.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1751` | 265,790.00 USD | 265,790.00 USD | 37,840.00 USD | 0.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1752` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 263,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1754` | 299,440.00 USD | 299,440.00 USD | 0.00 USD | 0.00 USD | 33,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1755` | 1,570,000.00 USD | 1,570,000.00 USD | 37,610.00 USD | 0.00 USD | 169,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1757` | 388,050.00 USD | 388,050.00 USD | 8,970.00 USD | 40,160.00 USD | 39,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1758` | 1,780,000.00 USD | 1,780,000.00 USD | 173,440.00 USD | 38,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1760` | 564,770.00 USD | 564,770.00 USD | 85,150.00 USD | 76,400.00 USD | 15,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1761` | 2,320,000.00 USD | 2,320,000.00 USD | 373,120.00 USD | 131,090.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1763` | 733,300.00 USD | 733,300.00 USD | 84,560.00 USD | 20,760.00 USD | 63,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1764` | 2,740,000.00 USD | 2,740,000.00 USD | 164,630.00 USD | 215,620.00 USD | 40,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1765` | 339.06 USD | 339.06 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1766` | 841,520.00 USD | 841,520.00 USD | 24,650.00 USD | 20,220.00 USD | 63,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1767` | 3,080,000.00 USD | 3,080,000.00 USD | 176,410.00 USD | 152,530.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1769` | 1,020,000.00 USD | 1,020,000.00 USD | 45,860.00 USD | 87,060.00 USD | 44,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1770` | 3,330,000.00 USD | 3,330,000.00 USD | 61,490.00 USD | 147,940.00 USD | 44,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1772` | 1,090,000.00 USD | 1,090,000.00 USD | 22,380.00 USD | 20,220.00 USD | 28,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1773` | 3,540,000.00 USD | 3,540,000.00 USD | 103,820.00 USD | 105,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1775` | 1,200,000.00 USD | 1,200,000.00 USD | 74,270.00 USD | 27,710.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1776` | 3,740,000.00 USD | 3,740,000.00 USD | 135,140.00 USD | 69,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1778` | 1,360,000.00 USD | 1,360,000.00 USD | 58,020.00 USD | 87,510.00 USD | 19,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1779` | 3,980,000.00 USD | 3,980,000.00 USD | 52,730.00 USD | 46,410.00 USD | 131,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1781` | 1,460,000.00 USD | 1,460,000.00 USD | 50,570.00 USD | 1,060.00 USD | 45,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1782` | 4,040,000.00 USD | 4,040,000.00 USD | 20,690.00 USD | 13,990.00 USD | 31,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1784` | 1,610,000.00 USD | 1,610,000.00 USD | 92,690.00 USD | 38,240.00 USD | 18,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1785` | 4,290,000.00 USD | 4,290,000.00 USD | 153,160.00 USD | 78,850.00 USD | 16,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1787` | 1,760,000.00 USD | 1,760,000.00 USD | 37,680.00 USD | 54,820.00 USD | 51,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1788` | 4,400,000.00 USD | 4,400,000.00 USD | 73,130.00 USD | 18,250.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1790` | 1,850,000.00 USD | 1,850,000.00 USD | 53,220.00 USD | 22,930.00 USD | 21,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1791` | 4,570,000.00 USD | 4,570,000.00 USD | 155,720.00 USD | 17,360.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1793` | 1,930,000.00 USD | 1,930,000.00 USD | 32,720.00 USD | 20,810.00 USD | 20,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1794` | 4,680,000.00 USD | 4,680,000.00 USD | 27,100.00 USD | 42,780.00 USD | 36,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1795` | 156.94 USD | 495.99 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1796` | 2,080,000.00 USD | 2,080,000.00 USD | 48,060.00 USD | 66,080.00 USD | 41,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1797` | 4,720,000.00 USD | 4,720,000.00 USD | 17,130.00 USD | 12,930.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1799` | 2,130,000.00 USD | 2,130,000.00 USD | 16,820.00 USD | 14,880.00 USD | 15,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1800` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 34,680.00 USD | 64,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1802` | 2,210,000.00 USD | 2,210,000.00 USD | 15,140.00 USD | 34,770.00 USD | 28,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1803` | 4,900,000.00 USD | 4,900,000.00 USD | 35,280.00 USD | 25,700.00 USD | 18,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1805` | 2,270,000.00 USD | 2,270,000.00 USD | 22,680.00 USD | 9,380.00 USD | 27,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1805` | 10,970.00 USD | 11,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1806` | 4,980,000.00 USD | 4,980,000.00 USD | 11,410.00 USD | 56,850.00 USD | 19,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1808` | 2,360,000.00 USD | 2,360,000.00 USD | 24,170.00 USD | 27,870.00 USD | 35,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1809` | 5,130,000.00 USD | 5,130,000.00 USD | 53,670.00 USD | 30,810.00 USD | 58,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1811` | 2,440,000.00 USD | 2,440,000.00 USD | 39,150.00 USD | 16,000.00 USD | 24,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1812` | 5,230,000.00 USD | 5,230,000.00 USD | 34,960.00 USD | 16,640.00 USD | 50,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1814` | 2,530,000.00 USD | 2,530,000.00 USD | 28,390.00 USD | 38,050.00 USD | 28,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1815` | 5,360,000.00 USD | 5,360,000.00 USD | 60,010.00 USD | 30,810.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1815` | 9,530.00 USD | 21,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1817` | 2,600,000.00 USD | 2,600,000.00 USD | 31,330.00 USD | 11,020.00 USD | 30,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1818` | 5,470,000.00 USD | 5,470,000.00 USD | 75,040.00 USD | 24,140.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1820` | 2,660,000.00 USD | 2,660,000.00 USD | 34,200.00 USD | 18,550.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1821` | 5,580,000.00 USD | 5,580,000.00 USD | 40,950.00 USD | 33,870.00 USD | 41,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1823` | 2,720,000.00 USD | 2,720,000.00 USD | 16,740.00 USD | 19,980.00 USD | 17,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1824` | 5,740,000.00 USD | 5,740,000.00 USD | 39,400.00 USD | 17,880.00 USD | 95,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1825` | 185.09 USD | 21,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1826` | 2,760,000.00 USD | 2,760,000.00 USD | 27,750.00 USD | 6,860.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1827` | 5,900,000.00 USD | 5,900,000.00 USD | 79,610.00 USD | 18,690.00 USD | 65,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1829` | 2,760,000.00 USD | 2,760,000.00 USD | 3,490.00 USD | 1,640.00 USD | 3,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1830` | 6,040,000.00 USD | 6,040,000.00 USD | 64,890.00 USD | 20,550.00 USD | 52,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1832` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 4,090.00 USD | 11,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1833` | 6,300,000.00 USD | 6,300,000.00 USD | 186,730.00 USD | 49,740.00 USD | 26,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1835` | 2,790,000.00 USD | 2,790,000.00 USD | 5,030.00 USD | 655.16 USD | 728.16 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1835` | 49,830.00 USD | 71,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1836` | 6,470,000.00 USD | 6,470,000.00 USD | 29,580.00 USD | 83,110.00 USD | 52,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1838` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 2,640.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1839` | 6,750,000.00 USD | 6,750,000.00 USD | 129,950.00 USD | 41,230.00 USD | 114,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1841` | 2,820,000.00 USD | 2,820,000.00 USD | 13,150.00 USD | 2,060.00 USD | 7,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1842` | 6,950,000.00 USD | 6,950,000.00 USD | 71,550.00 USD | 26,100.00 USD | 97,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1844` | 2,840,000.00 USD | 2,840,000.00 USD | 2,690.00 USD | 5,540.00 USD | 15,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1845` | 7,080,000.00 USD | 7,080,000.00 USD | 34,630.00 USD | 33,340.00 USD | 66,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1847` | 2,870,000.00 USD | 2,870,000.00 USD | 7,630.00 USD | 7,150.00 USD | 11,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1848` | 7,340,000.00 USD | 7,340,000.00 USD | 47,730.00 USD | 75,080.00 USD | 135,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1850` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 3,150.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1851` | 7,680,000.00 USD | 7,680,000.00 USD | 94,780.00 USD | 28,290.00 USD | 220,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1853` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 1,690.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1854` | 7,860,000.00 USD | 7,860,000.00 USD | 105,210.00 USD | 4,290.00 USD | 63,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1856` | 2,890,000.00 USD | 2,890,000.00 USD | 4,860.00 USD | 0.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1857` | 8,130,000.00 USD | 8,130,000.00 USD | 116,320.00 USD | 32,070.00 USD | 127,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1859` | 2,910,000.00 USD | 2,910,000.00 USD | 9,450.00 USD | 1,470.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1860` | 8,370,000.00 USD | 8,370,000.00 USD | 87,180.00 USD | 76,610.00 USD | 74,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1862` | 2,920,000.00 USD | 2,920,000.00 USD | 1,870.00 USD | 2,970.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1863` | 8,580,000.00 USD | 8,580,000.00 USD | 80,860.00 USD | 63,750.00 USD | 61,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1865` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1866` | 8,750,000.00 USD | 8,750,000.00 USD | 101,070.00 USD | 33,740.00 USD | 39,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1868` | 2,930,000.00 USD | 2,930,000.00 USD | 3,300.00 USD | 0.00 USD | 5,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1869` | 9,060,000.00 USD | 9,060,000.00 USD | 169,650.00 USD | 66,330.00 USD | 78,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1871` | 2,950,000.00 USD | 2,950,000.00 USD | 8,950.00 USD | 5,040.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1872` | 9,390,000.00 USD | 9,390,000.00 USD | 91,030.00 USD | 132,480.00 USD | 105,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1874` | 2,970,000.00 USD | 2,970,000.00 USD | 7,320.00 USD | 2,820.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1875` | 9,540,000.00 USD | 9,540,000.00 USD | 68,250.00 USD | 42,310.00 USD | 36,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1875` | 21,190.00 USD | 92,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1877` | 2,970,000.00 USD | 2,970,000.00 USD | 2,670.00 USD | 2,760.00 USD | 918.24 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1878` | 9,690,000.00 USD | 9,690,000.00 USD | 66,470.00 USD | 37,330.00 USD | 48,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1880` | 2,990,000.00 USD | 2,990,000.00 USD | 4,530.00 USD | 3,160.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1881` | 9,780,000.00 USD | 9,780,000.00 USD | 29,820.00 USD | 44,080.00 USD | 13,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1883` | 3,000,000.00 USD | 3,000,000.00 USD | 4,630.00 USD | 4,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1884` | 9,890,000.00 USD | 9,890,000.00 USD | 10,560.00 USD | 36,820.00 USD | 58,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1885` | 477.23 USD | 92,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1886` | 3,020,000.00 USD | 3,020,000.00 USD | 13,740.00 USD | 2,220.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1887` | 9,940,000.00 USD | 9,940,000.00 USD | 22,970.00 USD | 0.00 USD | 25,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1889` | 3,030,000.00 USD | 3,030,000.00 USD | 3,580.00 USD | 3,150.00 USD | 7,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1890` | 10,060,000.00 USD | 10,060,000.00 USD | 36,740.00 USD | 17,330.00 USD | 75,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1892` | 3,040,000.00 USD | 3,040,000.00 USD | 1,140.00 USD | 8,660.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1893` | 10,120,000.00 USD | 10,120,000.00 USD | 32,450.00 USD | 6,940.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1895` | 3,060,000.00 USD | 3,060,000.00 USD | 4,810.00 USD | 4,140.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1896` | 10,230,000.00 USD | 10,230,000.00 USD | 62,730.00 USD | 27,440.00 USD | 18,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1898` | 3,080,000.00 USD | 3,080,000.00 USD | 7,030.00 USD | 16,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1899` | 10,300,000.00 USD | 10,300,000.00 USD | 11,530.00 USD | 38,530.00 USD | 20,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1901` | 3,100,000.00 USD | 3,100,000.00 USD | 11,640.00 USD | 4,150.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1902` | 10,330,000.00 USD | 10,330,000.00 USD | 14,330.00 USD | 0.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1904` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 1,660.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1905` | 10,380,000.00 USD | 10,380,000.00 USD | 8,720.00 USD | 24,800.00 USD | 24,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1907` | 3,130,000.00 USD | 3,130,000.00 USD | 2,490.00 USD | 11,300.00 USD | 6,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1908` | 10,480,000.00 USD | 10,480,000.00 USD | 25,220.00 USD | 43,160.00 USD | 28,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1910` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 1,050.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1911` | 10,490,000.00 USD | 10,490,000.00 USD | 0.00 USD | 9,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1913` | 3,150,000.00 USD | 3,150,000.00 USD | 4,910.00 USD | 2,880.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1914` | 10,510,000.00 USD | 10,510,000.00 USD | 7,460.00 USD | 11,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1916` | 3,180,000.00 USD | 3,180,000.00 USD | 12,220.00 USD | 16,330.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1917` | 10,530,000.00 USD | 10,530,000.00 USD | 0.00 USD | 11,840.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1919` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 2,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1922` | 3,200,000.00 USD | 3,200,000.00 USD | 9,260.00 USD | 2,030.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1923` | 10,550,000.00 USD | 10,550,000.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1925` | 3,210,000.00 USD | 3,210,000.00 USD | 11,380.00 USD | 5,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1926` | 10,580,000.00 USD | 10,580,000.00 USD | 11,600.00 USD | 13,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1928` | 3,220,000.00 USD | 3,220,000.00 USD | 3,390.00 USD | 1,930.00 USD | 4,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1931` | 3,230,000.00 USD | 3,230,000.00 USD | 4,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1937` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 1,150.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1944` | 10,580,000.00 USD | 10,580,000.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1945` | 4,270.00 USD | 96,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1950` | 10,590,000.00 USD | 10,590,000.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1955` | 860.20 USD | 97,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1975` | 1,190.00 USD | 98,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1995` | 135.22 USD | 99,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2025` | 764.66 USD | 99,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2045` | 399.22 USD | 100,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2055` | 11,590.00 USD | 111,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2085` | 198.08 USD | 112,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2095` | 1,060.00 USD | 113,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2135` | 16,070.00 USD | 129,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 41,230.00 USD | 170,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2165` | 43,300.00 USD | 213,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2195` | 88,300.00 USD | 302,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 343.77 USD | 302,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2245` | 26,710.00 USD | 329,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2255` | 154.78 USD | 329,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 6,820.00 USD | 336,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 16,250.00 USD | 352,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 102.62 USD | 352,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 361.66 USD | 352,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 869.00 USD | 353,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2445` | 231.03 USD | 353,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2465` | 9,360.00 USD | 363,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2545` | 20,480.00 USD | 383,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 3,870.00 USD | 387,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2575` | 29,500.00 USD | 417,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 52,030.00 USD | 469,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 154.94 USD | 469,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2685` | 226.51 USD | 469,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 13,950.00 USD | 483,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 214.21 USD | 483,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 27,890.00 USD | 511,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2795` | 482.84 USD | 512,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2905` | 2,210.00 USD | 514,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 187.26 USD | 514,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 574.36 USD | 515,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2975` | 59,500.00 USD | 574,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 225.42 USD | 574,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3225` | 18,200.00 USD | 592,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 9,540.00 USD | 602,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3305` | 192.68 USD | 602,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3325` | 148.36 USD | 602,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3335` | 221.81 USD | 603,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3345` | 78,600.00 USD | 681,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3385` | 108.46 USD | 681,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3395` | 263.38 USD | 682,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3445` | 1,710.00 USD | 683,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0365` | 2,170,000.00 USD | 0.00 USD | 2,370.00 USD | `-78.83%` | `65,000,000,000,000.00` |
| `Live` | `Long` | `0.0375` | 2,160,000.00 USD | 0.00 USD | 1,750.00 USD | `-78.25%` | `46,685,900,000,000.00` |
| `Live` | `Long` | `0.0385` | 2,160,000.00 USD | 0.00 USD | 1,490.00 USD | `-77.67%` | `38,823,900,000,000.00` |
| `Live` | `Long` | `0.0415` | 2,160,000.00 USD | 0.00 USD | 9,460.00 USD | `-75.93%` | `227,852,400,000,000.00` |
| `Live` | `Long` | `0.0425` | 2,150,000.00 USD | 0.00 USD | 170.00 USD | `-75.35%` | `4,000,000,000,000.00` |
| `Live` | `Long` | `0.0465` | 2,150,000.00 USD | 0.00 USD | 273.75 USD | `-73.02%` | `5,887,100,000,000.00` |
| `Live` | `Long` | `0.0495` | 2,150,000.00 USD | 0.00 USD | 109.52 USD | `-71.28%` | `2,212,600,000,000.00` |
| `Live` | `Long` | `0.0505` | 2,150,000.00 USD | 0.00 USD | 204.38 USD | `-70.70%` | `4,047,100,000,000.00` |
| `Live` | `Long` | `0.0515` | 2,150,000.00 USD | 0.00 USD | 964.65 USD | `-70.12%` | `18,731,100,000,000.00` |
| `Live` | `Long` | `0.0525` | 2,150,000.00 USD | 0.00 USD | 945.32 USD | `-69.54%` | `18,006,000,000,000.00` |
| `Live` | `Long` | `0.0545` | 2,150,000.00 USD | 0.00 USD | 6,080.00 USD | `-68.38%` | `111,635,000,000,000.00` |
| `Live` | `Long` | `0.0565` | 2,140,000.00 USD | 0.00 USD | 15,970.00 USD | `-67.22%` | `282,726,500,000,000.00` |
| `Live` | `Long` | `0.0575` | 2,130,000.00 USD | 0.00 USD | 628.38 USD | `-66.64%` | `10,928,400,000,000.00` |
| `Live` | `Long` | `0.0585` | 2,130,000.00 USD | 0.00 USD | 3,140.00 USD | `-66.06%` | `53,733,200,000,000.00` |
| `Live` | `Long` | `0.0595` | 2,120,000.00 USD | 0.00 USD | 242.06 USD | `-65.48%` | `4,068,300,000,000.00` |
| `Live` | `Long` | `0.0615` | 2,120,000.00 USD | 0.00 USD | 86,100.00 USD | `-64.32%` | `1,400,000,000,000,000.00` |
| `Live` | `Long` | `0.0625` | 2,040,000.00 USD | 0.00 USD | 579.79 USD | `-63.74%` | `9,276,700,000,000.00` |
| `Live` | `Long` | `0.0675` | 2,040,000.00 USD | 0.00 USD | 99,790.00 USD | `-60.84%` | `1,478,385,900,000,000.00` |
| `Live` | `Long` | `0.0685` | 1,940,000.00 USD | 0.00 USD | 2,290.00 USD | `-60.26%` | `33,394,300,000,000.00` |
| `Live` | `Long` | `0.0695` | 1,930,000.00 USD | 0.00 USD | 143.87 USD | `-59.68%` | `2,070,000,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,930,000.00 USD | 0.00 USD | 2,970.00 USD | `-59.10%` | `42,142,800,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,930,000.00 USD | 0.00 USD | 24,170.00 USD | `-58.52%` | `337,986,100,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,910,000.00 USD | 0.00 USD | 111.58 USD | `-57.94%` | `1,539,100,000,000.00` |
| `Live` | `Long` | `0.0735` | 1,910,000.00 USD | 0.00 USD | 2,440.00 USD | `-57.36%` | `33,161,800,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,900,000.00 USD | 0.00 USD | 226.17 USD | `-56.78%` | `3,035,900,000,000.00` |
| `Live` | `Long` | `0.0755` | 1,900,000.00 USD | 0.00 USD | 1,470.00 USD | `-56.20%` | `19,414,500,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,900,000.00 USD | 0.00 USD | 23,780.00 USD | `-55.62%` | `310,852,700,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,880,000.00 USD | 0.00 USD | 4,630.00 USD | `-53.88%` | `58,261,800,000,000.00` |
| `Live` | `Long` | `0.0805` | 1,870,000.00 USD | 0.00 USD | 6,040.00 USD | `-53.30%` | `75,000,000,000,000.00` |
| `Live` | `Long` | `0.0815` | 1,870,000.00 USD | 0.00 USD | 576.40 USD | `-52.72%` | `7,072,400,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,870,000.00 USD | 0.00 USD | 32,510.00 USD | `-52.14%` | `394,030,900,000,000.00` |
| `Live` | `Long` | `0.0835` | 1,840,000.00 USD | 0.00 USD | 751.50 USD | `-51.56%` | `9,000,000,000,000.00` |
| `Live` | `Long` | `0.0845` | 1,830,000.00 USD | 0.00 USD | 7,810.00 USD | `-50.98%` | `92,419,000,000,000.00` |
| `Live` | `Long` | `0.0855` | 1,830,000.00 USD | 0.00 USD | 238.28 USD | `-50.40%` | `2,786,900,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,830,000.00 USD | 0.00 USD | 362.62 USD | `-48.66%` | `4,097,400,000,000.00` |
| `Live` | `Long` | `0.0895` | 1,830,000.00 USD | 0.00 USD | 784.62 USD | `-48.08%` | `8,766,700,000,000.00` |
| `Live` | `Long` | `0.0905` | 1,830,000.00 USD | 0.00 USD | 498.92 USD | `-47.50%` | `5,512,900,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,830,000.00 USD | 0.00 USD | 2,040.00 USD | `-46.34%` | `22,044,300,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,820,000.00 USD | 0.00 USD | 3,360.00 USD | `-45.76%` | `35,953,000,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,820,000.00 USD | 0.00 USD | 40,270.00 USD | `-45.18%` | `426,141,000,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,780,000.00 USD | 0.00 USD | 589.63 USD | `-44.02%` | `6,110,200,000,000.00` |
| `Live` | `Long` | `0.0975` | 1,780,000.00 USD | 0.00 USD | 3,170.00 USD | `-43.44%` | `32,465,500,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,780,000.00 USD | 0.00 USD | 2,810.00 USD | `-42.86%` | `28,516,700,000,000.00` |
| `Live` | `Long` | `0.0995` | 1,770,000.00 USD | 0.00 USD | 10,350.00 USD | `-42.28%` | `104,009,200,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,760,000.00 USD | 0.00 USD | 2,490.00 USD | `-41.70%` | `24,815,000,000,000.00` |
| `Live` | `Long` | `0.1015` | 1,760,000.00 USD | 0.00 USD | 5,700.00 USD | `-41.12%` | `56,176,700,000,000.00` |
| `Live` | `Long` | `0.1025` | 1,750,000.00 USD | 0.00 USD | 12,430.00 USD | `-40.54%` | `121,229,100,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,740,000.00 USD | 0.00 USD | 1,060.00 USD | `-39.96%` | `10,278,600,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,740,000.00 USD | 0.00 USD | 36,970.00 USD | `-39.38%` | `353,738,000,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,700,000.00 USD | 0.00 USD | 6,860.00 USD | `-38.80%` | `65,046,300,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,700,000.00 USD | 0.00 USD | 181.20 USD | `-38.22%` | `1,701,400,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,700,000.00 USD | 0.00 USD | 1,060.00 USD | `-37.64%` | `9,856,300,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,700,000.00 USD | 0.00 USD | 342.59 USD | `-37.06%` | `3,157,500,000,000.00` |
| `Live` | `Long` | `0.1095` | 1,700,000.00 USD | 0.00 USD | 2,890.00 USD | `-36.48%` | `26,421,300,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,690,000.00 USD | 0.00 USD | 534.49 USD | `-35.90%` | `4,837,000,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,690,000.00 USD | 0.00 USD | 425.50 USD | `-35.32%` | `3,816,100,000,000.00` |
| `Live` | `Long` | `0.1125` | 1,690,000.00 USD | 0.00 USD | 7,710.00 USD | `-34.74%` | `68,529,100,000,000.01` |
| `Live` | `Long` | `0.1135` | 1,680,000.00 USD | 0.00 USD | 14,160.00 USD | `-34.16%` | `124,762,100,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,670,000.00 USD | 0.00 USD | 8,950.00 USD | `-33.58%` | `78,144,100,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,660,000.00 USD | 0.00 USD | 4,890.00 USD | `-33.00%` | `42,364,200,000,000.00` |
| `Live` | `Long` | `0.1165` | 1,660,000.00 USD | 0.00 USD | 22,240.00 USD | `-32.42%` | `190,942,100,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,630,000.00 USD | 0.00 USD | 3,570.00 USD | `-31.84%` | `30,360,400,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,630,000.00 USD | 0.00 USD | 25,940.00 USD | `-31.26%` | `218,884,900,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,600,000.00 USD | 0.00 USD | 1,830.00 USD | `-30.68%` | `15,286,200,000,000.00` |
| `Live` | `Long` | `0.1205` | 1,600,000.00 USD | 0.00 USD | 1,120.00 USD | `-30.10%` | `9,285,000,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,600,000.00 USD | 0.00 USD | 54,870.00 USD | `-29.52%` | `451,629,800,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,550,000.00 USD | 0.00 USD | 636.74 USD | `-28.94%` | `5,197,900,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,550,000.00 USD | 0.00 USD | 32,960.00 USD | `-28.36%` | `266,849,500,000,000.00` |
| `Live` | `Long` | `0.1245` | 1,510,000.00 USD | 0.00 USD | 3,110.00 USD | `-27.78%` | `24,990,900,000,000.00` |
| `Live` | `Long` | `0.1255` | 1,510,000.00 USD | 0.00 USD | 4,850.00 USD | `-27.20%` | `38,646,100,000,000.00` |
| `Live` | `Long` | `0.1265` | 1,500,000.00 USD | 0.00 USD | 1,200.00 USD | `-26.62%` | `9,489,700,000,000.00` |
| `Live` | `Long` | `0.1275` | 1,500,000.00 USD | 0.00 USD | 4,490.00 USD | `-26.04%` | `35,222,300,000,000.00` |
| `Live` | `Long` | `0.1285` | 1,500,000.00 USD | 0.00 USD | 9,780.00 USD | `-25.46%` | `76,071,500,000,000.00` |
| `Live` | `Long` | `0.1295` | 1,490,000.00 USD | 0.00 USD | 4,010.00 USD | `-24.88%` | `30,998,800,000,000.00` |
| `Live` | `Long` | `0.1305` | 1,490,000.00 USD | 0.00 USD | 20,510.00 USD | `-24.30%` | `157,179,800,000,000.00` |
| `Live` | `Long` | `0.1315` | 1,460,000.00 USD | 0.00 USD | 18,500.00 USD | `-23.72%` | `140,680,500,000,000.00` |
| `Live` | `Long` | `0.1325` | 1,450,000.00 USD | 0.00 USD | 6,620.00 USD | `-23.13%` | `50,000,000,000,000.00` |
| `Live` | `Long` | `0.1335` | 1,440,000.00 USD | 0.00 USD | 23,200.00 USD | `-22.55%` | `173,799,200,000,000.00` |
| `Live` | `Long` | `0.1345` | 1,420,000.00 USD | 0.00 USD | 6,510.00 USD | `-21.97%` | `48,413,200,000,000.00` |
| `Live` | `Long` | `0.1355` | 1,410,000.00 USD | 0.00 USD | 3,570.00 USD | `-21.39%` | `26,331,000,000,000.00` |
| `Live` | `Long` | `0.1365` | 1,410,000.00 USD | 0.00 USD | 159,680.00 USD | `-20.81%` | `1,169,788,900,000,000.00` |
| `Live` | `Long` | `0.1375` | 1,250,000.00 USD | 0.00 USD | 1,700.00 USD | `-20.23%` | `12,345,200,000,000.00` |
| `Live` | `Long` | `0.1385` | 1,250,000.00 USD | 0.00 USD | 4,240.00 USD | `-19.65%` | `30,584,300,000,000.00` |
| `Live` | `Long` | `0.1395` | 1,240,000.00 USD | 0.00 USD | 17,910.00 USD | `-19.07%` | `128,383,000,000,000.00` |
| `Live` | `Long` | `0.1405` | 1,220,000.00 USD | 0.00 USD | 2,800.00 USD | `-18.49%` | `19,894,100,000,000.00` |
| `Live` | `Long` | `0.1415` | 1,220,000.00 USD | 0.00 USD | 15,030.00 USD | `-17.91%` | `106,185,800,000,000.00` |
| `Live` | `Long` | `0.1425` | 1,210,000.00 USD | 0.00 USD | 487,940.00 USD | `-17.33%` | `3,424,148,400,000,000.00` |
| `Live` | `Long` | `0.1435` | 717,220.00 USD | 0.00 USD | 19,330.00 USD | `-16.75%` | `134,671,900,000,000.00` |
| `Live` | `Long` | `0.1445` | 697,890.00 USD | 0.00 USD | 53,070.00 USD | `-16.17%` | `367,290,700,000,000.00` |
| `Live` | `Long` | `0.1455` | 644,820.00 USD | 0.00 USD | 111.10 USD | `-15.59%` | `763,600,000,000.00` |
| `Live` | `Long` | `0.1465` | 644,710.00 USD | 0.00 USD | 30,880.00 USD | `-15.01%` | `210,767,600,000,000.00` |
| `Live` | `Long` | `0.1475` | 613,830.00 USD | 0.00 USD | 73,930.00 USD | `-14.43%` | `501,196,600,000,000.00` |
| `Live` | `Long` | `0.1485` | 539,900.00 USD | 0.00 USD | 2,720.00 USD | `-13.85%` | `18,301,300,000,000.00` |
| `Live` | `Long` | `0.1495` | 537,190.00 USD | 0.00 USD | 35,380.00 USD | `-13.27%` | `236,635,500,000,000.00` |
| `Live` | `Long` | `0.1505` | 501,810.00 USD | 0.00 USD | 102,290.00 USD | `-12.69%` | `679,673,200,000,000.00` |
| `Live` | `Long` | `0.1515` | 399,520.00 USD | 0.00 USD | 3,930.00 USD | `-12.11%` | `25,964,300,000,000.00` |
| `Live` | `Long` | `0.1525` | 395,580.00 USD | 0.00 USD | 42,800.00 USD | `-11.53%` | `280,626,000,000,000.00` |
| `Live` | `Long` | `0.1535` | 352,790.00 USD | 0.00 USD | 19,400.00 USD | `-10.95%` | `126,406,800,000,000.00` |
| `Live` | `Long` | `0.1545` | 333,390.00 USD | 0.00 USD | 26,170.00 USD | `-10.37%` | `169,378,600,000,000.00` |
| `Live` | `Long` | `0.1555` | 307,220.00 USD | 0.00 USD | 40,060.00 USD | `-9.79%` | `257,609,900,000,000.00` |
| `Live` | `Long` | `0.1565` | 267,160.00 USD | 0.00 USD | 21,460.00 USD | `-9.21%` | `137,118,700,000,000.02` |
| `Live` | `Long` | `0.1575` | 245,700.00 USD | 0.00 USD | 4,940.00 USD | `-8.63%` | `31,351,900,000,000.00` |
| `Live` | `Long` | `0.1585` | 240,760.00 USD | 0.00 USD | 5,650.00 USD | `-8.05%` | `35,646,900,000,000.00` |
| `Live` | `Long` | `0.1595` | 235,110.00 USD | 0.00 USD | 64,950.00 USD | `-7.47%` | `407,194,700,000,000.00` |
| `Live` | `Long` | `0.1605` | 170,160.00 USD | 0.00 USD | 20,620.00 USD | `-6.89%` | `128,458,000,000,000.00` |
| `Live` | `Long` | `0.1615` | 149,550.00 USD | 0.00 USD | 17,950.00 USD | `-6.31%` | `111,158,400,000,000.00` |
| `Live` | `Long` | `0.1625` | 131,590.00 USD | 0.00 USD | 98,470.00 USD | `-5.73%` | `605,947,100,000,000.00` |
| `Live` | `Long` | `0.1635` | 33,130.00 USD | 0.00 USD | 251.51 USD | `-5.15%` | `1,538,300,000,000.00` |
| `Live` | `Long` | `0.1645` | 32,880.00 USD | 0.00 USD | 18,010.00 USD | `-4.57%` | `109,468,500,000,000.00` |
| `Live` | `Long` | `0.1655` | 14,870.00 USD | 0.00 USD | 14,870.00 USD | `-3.99%` | `89,840,600,000,000.00` |
| `Live` | `Short` | `0.1765` | 339.06 USD | 339.06 USD | 0.00 USD | `+2.39%` | `1,921,000,000,000.00` |
| `Live` | `Short` | `0.1795` | 495.99 USD | 156.94 USD | 0.00 USD | `+4.13%` | `874,300,000,000.00` |
| `Live` | `Short` | `0.1805` | 11,470.00 USD | 10,970.00 USD | 0.00 USD | `+4.71%` | `60,770,700,000,000.00` |
| `Live` | `Short` | `0.1815` | 21,000.00 USD | 9,530.00 USD | 0.00 USD | `+5.29%` | `52,508,000,000,000.00` |
| `Live` | `Short` | `0.1825` | 21,180.00 USD | 185.09 USD | 0.00 USD | `+5.87%` | `1,014,200,000,000.00` |
| `Live` | `Short` | `0.1835` | 71,010.00 USD | 49,830.00 USD | 0.00 USD | `+6.45%` | `271,563,800,000,000.00` |
| `Live` | `Short` | `0.1875` | 92,200.00 USD | 21,190.00 USD | 0.00 USD | `+8.77%` | `112,997,300,000,000.00` |
| `Live` | `Short` | `0.1885` | 92,680.00 USD | 477.23 USD | 0.00 USD | `+9.35%` | `2,531,700,000,000.00` |
| `Live` | `Short` | `0.1945` | 96,950.00 USD | 4,270.00 USD | 0.00 USD | `+12.83%` | `21,946,900,000,000.00` |
| `Live` | `Short` | `0.1955` | 97,810.00 USD | 860.20 USD | 0.00 USD | `+13.41%` | `4,400,000,000,000.00` |
| `Live` | `Short` | `0.1975` | 98,990.00 USD | 1,190.00 USD | 0.00 USD | `+14.57%` | `6,002,200,000,000.00` |
| `Live` | `Short` | `0.1995` | 99,130.00 USD | 135.22 USD | 0.00 USD | `+15.73%` | `677,800,000,000.00` |
| `Live` | `Short` | `0.2025` | 99,890.00 USD | 764.66 USD | 0.00 USD | `+17.47%` | `3,776,100,000,000.00` |
| `Live` | `Short` | `0.2045` | 100,290.00 USD | 399.22 USD | 0.00 USD | `+18.63%` | `1,952,200,000,000.00` |
| `Live` | `Short` | `0.2055` | 111,880.00 USD | 11,590.00 USD | 0.00 USD | `+19.21%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2085` | 112,080.00 USD | 198.08 USD | 0.00 USD | `+20.95%` | `950,000,000,000.00` |
| `Live` | `Short` | `0.2095` | 113,140.00 USD | 1,060.00 USD | 0.00 USD | `+21.53%` | `5,056,300,000,000.00` |
| `Live` | `Short` | `0.2135` | 129,210.00 USD | 16,070.00 USD | 0.00 USD | `+23.85%` | `75,287,100,000,000.00` |
| `Live` | `Short` | `0.2155` | 170,450.00 USD | 41,230.00 USD | 0.00 USD | `+25.01%` | `191,330,600,000,000.00` |
| `Live` | `Short` | `0.2165` | 213,750.00 USD | 43,300.00 USD | 0.00 USD | `+25.59%` | `200,003,000,000,000.00` |
| `Live` | `Short` | `0.2195` | 302,050.00 USD | 88,300.00 USD | 0.00 USD | `+27.33%` | `402,290,200,000,000.00` |
| `Live` | `Short` | `0.2235` | 302,390.00 USD | 343.77 USD | 0.00 USD | `+29.66%` | `1,538,100,000,000.00` |
| `Live` | `Short` | `0.2245` | 329,110.00 USD | 26,710.00 USD | 0.00 USD | `+30.24%` | `118,989,500,000,000.00` |
| `Live` | `Short` | `0.2255` | 329,260.00 USD | 154.78 USD | 0.00 USD | `+30.82%` | `686,400,000,000.00` |
| `Live` | `Short` | `0.2295` | 336,080.00 USD | 6,820.00 USD | 0.00 USD | `+33.14%` | `29,727,000,000,000.00` |
| `Live` | `Short` | `0.2355` | 352,340.00 USD | 16,250.00 USD | 0.00 USD | `+36.62%` | `69,017,500,000,000.00` |
| `Live` | `Short` | `0.2375` | 352,440.00 USD | 102.62 USD | 0.00 USD | `+37.78%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2405` | 352,800.00 USD | 361.66 USD | 0.00 USD | `+39.52%` | `1,503,800,000,000.00` |
| `Live` | `Short` | `0.2425` | 353,670.00 USD | 869.00 USD | 0.00 USD | `+40.68%` | `3,583,500,000,000.00` |
| `Live` | `Short` | `0.2445` | 353,900.00 USD | 231.03 USD | 0.00 USD | `+41.84%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2465` | 363,260.00 USD | 9,360.00 USD | 0.00 USD | `+43.00%` | `37,972,200,000,000.00` |
| `Live` | `Short` | `0.2545` | 383,740.00 USD | 20,480.00 USD | 0.00 USD | `+47.64%` | `80,464,000,000,000.00` |
| `Live` | `Short` | `0.2565` | 387,600.00 USD | 3,870.00 USD | 0.00 USD | `+48.80%` | `15,070,700,000,000.00` |
| `Live` | `Short` | `0.2575` | 417,100.00 USD | 29,500.00 USD | 0.00 USD | `+49.38%` | `114,561,100,000,000.00` |
| `Live` | `Short` | `0.2585` | 469,130.00 USD | 52,030.00 USD | 0.00 USD | `+49.96%` | `201,260,100,000,000.00` |
| `Live` | `Short` | `0.2615` | 469,280.00 USD | 154.94 USD | 0.00 USD | `+51.70%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2685` | 469,510.00 USD | 226.51 USD | 0.00 USD | `+55.76%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2715` | 483,460.00 USD | 13,950.00 USD | 0.00 USD | `+57.50%` | `51,364,100,000,000.00` |
| `Live` | `Short` | `0.2725` | 483,670.00 USD | 214.21 USD | 0.00 USD | `+58.08%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 511,560.00 USD | 27,890.00 USD | 0.00 USD | `+59.24%` | `101,607,700,000,000.00` |
| `Live` | `Short` | `0.2795` | 512,040.00 USD | 482.84 USD | 0.00 USD | `+62.14%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2905` | 514,250.00 USD | 2,210.00 USD | 0.00 USD | `+68.52%` | `7,608,100,000,000.00` |
| `Live` | `Short` | `0.2915` | 514,440.00 USD | 187.26 USD | 0.00 USD | `+69.10%` | `642,400,000,000.00` |
| `Live` | `Short` | `0.2955` | 515,020.00 USD | 574.36 USD | 0.00 USD | `+71.42%` | `1,943,700,000,000.00` |
| `Live` | `Short` | `0.2975` | 574,520.00 USD | 59,500.00 USD | 0.00 USD | `+72.58%` | `200,000,000,000,000.00` |
| `Live` | `Short` | `0.3105` | 574,740.00 USD | 225.42 USD | 0.00 USD | `+80.13%` | `726,000,000,000.00` |
| `Live` | `Short` | `0.3225` | 592,940.00 USD | 18,200.00 USD | 0.00 USD | `+87.09%` | `56,430,200,000,000.00` |
| `Live` | `Short` | `0.3295` | 602,480.00 USD | 9,540.00 USD | 0.00 USD | `+91.15%` | `28,943,600,000,000.00` |
| `Live` | `Short` | `0.3305` | 602,670.00 USD | 192.68 USD | 0.00 USD | `+91.73%` | `583,000,000,000.00` |
| `Live` | `Short` | `0.3325` | 602,820.00 USD | 148.36 USD | 0.00 USD | `+92.89%` | `446,200,000,000.00` |
| `Live` | `Short` | `0.3335` | 603,040.00 USD | 221.81 USD | 0.00 USD | `+93.47%` | `665,100,000,000.00` |
| `Live` | `Short` | `0.3345` | 681,640.00 USD | 78,600.00 USD | 0.00 USD | `+94.05%` | `234,988,100,000,000.00` |
| `Live` | `Short` | `0.3385` | 681,750.00 USD | 108.46 USD | 0.00 USD | `+96.37%` | `320,400,000,000.00` |
| `Live` | `Short` | `0.3395` | 682,020.00 USD | 263.38 USD | 0.00 USD | `+96.95%` | `775,800,000,000.00` |
| `Live` | `Short` | `0.3445` | 683,720.00 USD | 1,710.00 USD | 0.00 USD | `+99.85%` | `4,950,000,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1452` | 11,150,000.00 USD | 0.00 USD | 11,150,000.00 USD | 0.00 USD | 5,660.00 USD | 25,020.00 USD |
| `7D` | `0.1455` | 11,110,000.00 USD | 0.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD |
| `7D` | `0.1458` | 11,110,000.00 USD | 0.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 3,740.00 USD |
| `7D` | `0.1461` | 11,110,000.00 USD | 0.00 USD | 11,110,000.00 USD | 0.00 USD | 3,430.00 USD | 0.00 USD |
| `7D` | `0.1464` | 11,100,000.00 USD | 0.00 USD | 11,100,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD |
| `7D` | `0.1467` | 11,100,000.00 USD | 0.00 USD | 11,100,000.00 USD | 9,720.00 USD | 9,180.00 USD | 4,840.00 USD |
| `7D` | `0.1470` | 11,080,000.00 USD | 0.00 USD | 11,080,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD |
| `7D` | `0.1473` | 11,070,000.00 USD | 0.00 USD | 11,070,000.00 USD | 6,490.00 USD | 5,400.00 USD | 5,280.00 USD |
| `7D` | `0.1476` | 11,050,000.00 USD | 0.00 USD | 11,050,000.00 USD | 0.00 USD | 14,780.00 USD | 5,320.00 USD |
| `7D` | `0.1479` | 11,030,000.00 USD | 0.00 USD | 11,030,000.00 USD | 0.00 USD | 39,730.00 USD | 14,560.00 USD |
| `7D` | `0.1482` | 10,970,000.00 USD | 0.00 USD | 10,970,000.00 USD | 41,960.00 USD | 20,720.00 USD | 27,030.00 USD |
| `7D` | `0.1485` | 10,880,000.00 USD | 0.00 USD | 10,880,000.00 USD | 16,180.00 USD | 7,340.00 USD | 38,270.00 USD |
| `7D` | `0.1488` | 10,820,000.00 USD | 0.00 USD | 10,820,000.00 USD | 20,860.00 USD | 3,130.00 USD | 10,390.00 USD |
| `7D` | `0.1491` | 10,790,000.00 USD | 0.00 USD | 10,790,000.00 USD | 33,540.00 USD | 17,020.00 USD | 20,270.00 USD |
| `7D` | `0.1494` | 10,720,000.00 USD | 0.00 USD | 10,720,000.00 USD | 34,220.00 USD | 9,890.00 USD | 14,210.00 USD |
| `7D` | `0.1497` | 10,660,000.00 USD | 0.00 USD | 10,660,000.00 USD | 20,880.00 USD | 17,180.00 USD | 9,710.00 USD |
| `7D` | `0.1500` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 46,820.00 USD | 5,810.00 USD | 21,940.00 USD |
| `7D` | `0.1503` | 10,540,000.00 USD | 0.00 USD | 10,540,000.00 USD | 11,490.00 USD | 13,450.00 USD | 9,950.00 USD |
| `7D` | `0.1506` | 10,500,000.00 USD | 0.00 USD | 10,500,000.00 USD | 33,170.00 USD | 18,020.00 USD | 65,400.00 USD |
| `7D` | `0.1509` | 10,390,000.00 USD | 0.00 USD | 10,390,000.00 USD | 17,340.00 USD | 9,550.00 USD | 24,150.00 USD |
| `7D` | `0.1512` | 10,330,000.00 USD | 0.00 USD | 10,330,000.00 USD | 18,600.00 USD | 8,620.00 USD | 26,910.00 USD |
| `7D` | `0.1515` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 53,430.00 USD | 13,330.00 USD | 53,490.00 USD |
| `7D` | `0.1518` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 46,830.00 USD | 15,160.00 USD | 64,360.00 USD |
| `7D` | `0.1521` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 38,960.00 USD | 6,920.00 USD | 38,800.00 USD |
| `7D` | `0.1524` | 9,950,000.00 USD | 0.00 USD | 9,950,000.00 USD | 37,550.00 USD | 13,950.00 USD | 11,280.00 USD |
| `7D` | `0.1527` | 9,890,000.00 USD | 0.00 USD | 9,890,000.00 USD | 56,950.00 USD | 30,410.00 USD | 33,080.00 USD |
| `7D` | `0.1530` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 54,790.00 USD | 9,880.00 USD | 16,070.00 USD |
| `7D` | `0.1533` | 9,690,000.00 USD | 0.00 USD | 9,690,000.00 USD | 10,760.00 USD | 16,570.00 USD | 21,560.00 USD |
| `1D` | `0.1535` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 9,990.00 USD | 5,590.00 USD | 3,210.00 USD |
| `7D` | `0.1536` | 9,640,000.00 USD | 0.00 USD | 9,640,000.00 USD | 37,160.00 USD | 2,910.00 USD | 13,450.00 USD |
| `1D` | `0.1538` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 4,530.00 USD | 3,160.00 USD | 7,130.00 USD |
| `7D` | `0.1539` | 9,580,000.00 USD | 0.00 USD | 9,580,000.00 USD | 22,990.00 USD | 18,230.00 USD | 5,070.00 USD |
| `1D` | `0.1541` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 4,630.00 USD | 4,960.00 USD | 0.00 USD |
| `7D` | `0.1542` | 9,540,000.00 USD | 0.00 USD | 9,540,000.00 USD | 0.00 USD | 3,590.00 USD | 4,670.00 USD |
| `1D` | `0.1544` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 17,310.00 USD | 5,370.00 USD | 4,330.00 USD |
| `7D` | `0.1545` | 9,530,000.00 USD | 0.00 USD | 9,530,000.00 USD | 9,250.00 USD | 0.00 USD | 5,620.00 USD |
| `1D` | `0.1547` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 1,140.00 USD | 6,820.00 USD | 7,640.00 USD |
| `7D` | `0.1548` | 9,510,000.00 USD | 0.00 USD | 9,510,000.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD |
| `1D` | `0.1550` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 4,810.00 USD | 4,460.00 USD | 2,030.00 USD |
| `7D` | `0.1551` | 9,510,000.00 USD | 0.00 USD | 9,510,000.00 USD | 34,670.00 USD | 11,820.00 USD | 0.00 USD |
| `1D` | `0.1553` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 11,770.00 USD | 20,800.00 USD | 6,590.00 USD |
| `7D` | `0.1554` | 9,460,000.00 USD | 0.00 USD | 9,460,000.00 USD | 0.00 USD | 0.00 USD | 6,470.00 USD |
| `1D` | `0.1556` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 6,890.00 USD | 3,410.00 USD | 6,780.00 USD |
| `7D` | `0.1557` | 9,460,000.00 USD | 0.00 USD | 9,460,000.00 USD | 0.00 USD | 4,510.00 USD | 10,800.00 USD |
| `1D` | `0.1559` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 2,490.00 USD | 8,320.00 USD | 7,790.00 USD |
| `7D` | `0.1560` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 0.00 USD | 6,480.00 USD | 0.00 USD |
| `1D` | `0.1562` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 6,020.00 USD | 4,020.00 USD | 10,350.00 USD |
| `7D` | `0.1563` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 0.00 USD | 19,950.00 USD | 9,840.00 USD |
| `1D` | `0.1565` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 24,770.00 USD | 11,570.00 USD | 15,030.00 USD |
| `7D` | `0.1566` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 50,480.00 USD | 29,160.00 USD | 26,780.00 USD |
| `1D` | `0.1568` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 34,400.00 USD | 26,770.00 USD | 17,010.00 USD |
| `7D` | `0.1569` | 9,300,000.00 USD | 0.00 USD | 9,300,000.00 USD | 15,590.00 USD | 5,100.00 USD | 11,900.00 USD |
| `1D` | `0.1571` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 32,670.00 USD | 11,300.00 USD | 10,840.00 USD |
| `7D` | `0.1572` | 9,270,000.00 USD | 0.00 USD | 9,270,000.00 USD | 40,760.00 USD | 34,450.00 USD | 17,760.00 USD |
| `1D` | `0.1574` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 34,240.00 USD | 13,520.00 USD | 8,660.00 USD |
| `7D` | `0.1575` | 9,170,000.00 USD | 0.00 USD | 9,170,000.00 USD | 23,310.00 USD | 88,960.00 USD | 21,360.00 USD |
| `1D` | `0.1577` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 54,010.00 USD | 54,680.00 USD | 19,410.00 USD |
| `7D` | `0.1578` | 9,040,000.00 USD | 0.00 USD | 9,040,000.00 USD | 58,590.00 USD | 84,670.00 USD | 67,670.00 USD |
| `1D` | `0.1580` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 47,010.00 USD | 22,460.00 USD | 28,230.00 USD |
| `7D` | `0.1581` | 8,830,000.00 USD | 0.00 USD | 8,830,000.00 USD | 92,720.00 USD | 58,880.00 USD | 57,600.00 USD |
| `1D` | `0.1583` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 30,310.00 USD | 15,040.00 USD | 16,200.00 USD |
| `7D` | `0.1584` | 8,620,000.00 USD | 0.00 USD | 8,620,000.00 USD | 80,450.00 USD | 35,780.00 USD | 123,970.00 USD |
| `1D` | `0.1586` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 21,980.00 USD | 20,660.00 USD | 20,840.00 USD |
| `7D` | `0.1587` | 8,380,000.00 USD | 0.00 USD | 8,380,000.00 USD | 69,180.00 USD | 22,370.00 USD | 31,060.00 USD |
| `1D` | `0.1589` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 17,680.00 USD | 19,490.00 USD | 8,270.00 USD |
| `7D` | `0.1590` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 71,200.00 USD | 44,110.00 USD | 51,290.00 USD |
| `1D` | `0.1592` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 26,740.00 USD | 20,480.00 USD | 13,210.00 USD |
| `7D` | `0.1593` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 69,430.00 USD | 56,020.00 USD | 68,480.00 USD |
| `1D` | `0.1595` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 51,370.00 USD | 15,690.00 USD | 34,370.00 USD |
| `7D` | `0.1596` | 7,900,000.00 USD | 0.00 USD | 7,900,000.00 USD | 161,460.00 USD | 85,250.00 USD | 120,230.00 USD |
| `1D` | `0.1598` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 76,370.00 USD | 25,620.00 USD | 48,520.00 USD |
| `7D` | `0.1599` | 7,530,000.00 USD | 0.00 USD | 7,530,000.00 USD | 219,060.00 USD | 55,380.00 USD | 87,990.00 USD |
| `1D` | `0.1601` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 51,010.00 USD | 36,090.00 USD | 11,300.00 USD |
| `7D` | `0.1602` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 44,770.00 USD | 46,490.00 USD | 40,380.00 USD |
| `1D` | `0.1604` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 39,480.00 USD | 20,230.00 USD | 17,830.00 USD |
| `7D` | `0.1605` | 7,040,000.00 USD | 0.00 USD | 7,040,000.00 USD | 177,720.00 USD | 136,660.00 USD | 217,140.00 USD |
| `1D` | `0.1607` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 54,740.00 USD | 26,880.00 USD | 26,290.00 USD |
| `7D` | `0.1608` | 6,500,000.00 USD | 0.00 USD | 6,500,000.00 USD | 129,610.00 USD | 174,940.00 USD | 131,300.00 USD |
| `1D` | `0.1610` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 114,870.00 USD | 116,770.00 USD | 47,670.00 USD |
| `7D` | `0.1611` | 6,070,000.00 USD | 0.00 USD | 6,070,000.00 USD | 148,170.00 USD | 230,750.00 USD | 233,470.00 USD |
| `1D` | `0.1613` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 85,600.00 USD | 58,130.00 USD | 61,970.00 USD |
| `7D` | `0.1614` | 5,460,000.00 USD | 0.00 USD | 5,460,000.00 USD | 330,910.00 USD | 194,680.00 USD | 282,150.00 USD |
| `1D` | `0.1616` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 60,630.00 USD | 35,580.00 USD | 37,640.00 USD |
| `7D` | `0.1617` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 346,150.00 USD | 101,810.00 USD | 410,900.00 USD |
| `1D` | `0.1619` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 64,990.00 USD | 43,250.00 USD | 62,910.00 USD |
| `7D` | `0.1620` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 282,000.00 USD | 134,660.00 USD | 262,970.00 USD |
| `1D` | `0.1622` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 60,790.00 USD | 46,210.00 USD | 25,680.00 USD |
| `7D` | `0.1623` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 304,460.00 USD | 125,080.00 USD | 208,070.00 USD |
| `1D` | `0.1625` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 19,000.00 USD | 48,390.00 USD | 18,240.00 USD |
| `7D` | `0.1626` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 234,280.00 USD | 71,120.00 USD | 0.00 USD |
| `1D` | `0.1628` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 14,220.00 USD | 29,880.00 USD | 18,660.00 USD |
| `7D` | `0.1629` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 171,310.00 USD | 0.00 USD | 20,860.00 USD |
| `1D` | `0.1631` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 12,400.00 USD | 21,390.00 USD | 13,680.00 USD |
| `7D` | `0.1632` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 9,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1634` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 24,810.00 USD | 9,110.00 USD | 13,290.00 USD |
| `7D` | `0.1635` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 0.00 USD | 13,670.00 USD | 21,360.00 USD |
| `1D` | `0.1637` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 7,630.00 USD | 22,520.00 USD | 19,410.00 USD |
| `7D` | `0.1638` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 62,410.00 USD |
| `1D` | `0.1640` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 14,040.00 USD | 6,090.00 USD | 32,750.00 USD |
| `7D` | `0.1641` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 22,480.00 USD | 29,240.00 USD | 0.00 USD |
| `1D` | `0.1643` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 25,590.00 USD | 20,340.00 USD | 3,370.00 USD |
| `7D` | `0.1644` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 0.00 USD | 8,990.00 USD | 26,230.00 USD |
| `1D` | `0.1646` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 40,030.00 USD | 24,740.00 USD | 29,820.00 USD |
| `7D` | `0.1647` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 34,760.00 USD | 0.00 USD | 7,650.00 USD |
| `1D` | `0.1649` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 4,570.00 USD | 23,390.00 USD | 19,090.00 USD |
| `7D` | `0.1650` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 0.00 USD | 7,000.00 USD | 22,660.00 USD |
| `1D` | `0.1652` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 19,770.00 USD | 8,470.00 USD | 34,610.00 USD |
| `7D` | `0.1653` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 33,810.00 USD | 12,460.00 USD | 28,440.00 USD |
| `1D` | `0.1655` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 12,800.00 USD | 17,940.00 USD | 18,360.00 USD |
| `7D` | `0.1656` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 0.00 USD | 19,330.00 USD | 16,170.00 USD |
| `1D` | `0.1658` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 54,340.00 USD | 47,930.00 USD | 40,940.00 USD |
| `7D` | `0.1659` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 40,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1661` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 22,630.00 USD | 11,150.00 USD | 53,490.00 USD |
| `7D` | `0.1662` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 48,590.00 USD | 62,020.00 USD | 81,010.00 USD |
| `1D` | `0.1664` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 48,150.00 USD | 59,110.00 USD | 57,170.00 USD |
| `7D` | `0.1665` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 87,050.00 USD | 32,780.00 USD | 57,360.00 USD |
| `1D` | `0.1667` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 90,380.00 USD | 62,710.00 USD | 53,200.00 USD |
| `7D` | `0.1668` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 11,410.00 USD | 39,630.00 USD | 42,720.00 USD |
| `1D` | `0.1670` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 64,200.00 USD | 29,020.00 USD | 27,120.00 USD |
| `7D` | `0.1671` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 70,540.00 USD | 62,490.00 USD | 0.00 USD |
| `1D` | `0.1673` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 42,030.00 USD | 31,130.00 USD | 18,410.00 USD |
| `7D` | `0.1674` | 962,640.00 USD | 0.00 USD | 962,640.00 USD | 44,960.00 USD | 88,950.00 USD | 0.00 USD |
| `1D` | `0.1676` | 916,010.00 USD | 0.00 USD | 916,010.00 USD | 14,620.00 USD | 33,240.00 USD | 13,550.00 USD |
| `7D` | `0.1677` | 828,730.00 USD | 0.00 USD | 828,730.00 USD | 59,010.00 USD | 64,850.00 USD | 0.00 USD |
| `1D` | `0.1679` | 854,600.00 USD | 0.00 USD | 854,600.00 USD | 6,270.00 USD | 5,070.00 USD | 12,960.00 USD |
| `7D` | `0.1680` | 704,870.00 USD | 0.00 USD | 704,870.00 USD | 101,910.00 USD | 68,430.00 USD | 15,310.00 USD |
| `1D` | `0.1682` | 830,300.00 USD | 0.00 USD | 830,300.00 USD | 149,180.00 USD | 38,540.00 USD | 32,240.00 USD |
| `7D` | `0.1683` | 519,230.00 USD | 0.00 USD | 519,230.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD |
| `1D` | `0.1685` | 610,340.00 USD | 0.00 USD | 610,340.00 USD | 13,810.00 USD | 53,220.00 USD | 11,810.00 USD |
| `1D` | `0.1688` | 531,500.00 USD | 0.00 USD | 531,500.00 USD | 0.00 USD | 0.00 USD | 8,570.00 USD |
| `7D` | `0.1689` | 444,270.00 USD | 0.00 USD | 444,270.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD |
| `1D` | `0.1691` | 522,930.00 USD | 0.00 USD | 522,930.00 USD | 42,110.00 USD | 73,140.00 USD | 24,520.00 USD |
| `7D` | `0.1692` | 405,610.00 USD | 0.00 USD | 405,610.00 USD | 21,780.00 USD | 32,070.00 USD | 32,350.00 USD |
| `1D` | `0.1694` | 383,160.00 USD | 0.00 USD | 383,160.00 USD | 13,210.00 USD | 22,300.00 USD | 40,460.00 USD |
| `7D` | `0.1695` | 319,410.00 USD | 0.00 USD | 319,410.00 USD | 0.00 USD | 30,490.00 USD | 28,010.00 USD |
| `1D` | `0.1697` | 307,190.00 USD | 0.00 USD | 307,190.00 USD | 15,020.00 USD | 35,530.00 USD | 22,480.00 USD |
| `7D` | `0.1698` | 260,910.00 USD | 0.00 USD | 260,910.00 USD | 0.00 USD | 56,860.00 USD | 18,830.00 USD |
| `1D` | `0.1700` | 234,160.00 USD | 0.00 USD | 234,160.00 USD | 0.00 USD | 26,820.00 USD | 19,520.00 USD |
| `7D` | `0.1701` | 185,220.00 USD | 0.00 USD | 185,220.00 USD | 22,820.00 USD | 25,330.00 USD | 0.00 USD |
| `1D` | `0.1703` | 187,810.00 USD | 0.00 USD | 187,810.00 USD | 0.00 USD | 14,420.00 USD | 10,240.00 USD |
| `7D` | `0.1704` | 137,070.00 USD | 0.00 USD | 137,070.00 USD | 0.00 USD | 46,880.00 USD | 0.00 USD |
| `1D` | `0.1706` | 163,160.00 USD | 0.00 USD | 163,160.00 USD | 22,060.00 USD | 6,390.00 USD | 4,150.00 USD |
| `7D` | `0.1707` | 90,190.00 USD | 0.00 USD | 90,190.00 USD | 0.00 USD | 0.00 USD | 59,520.00 USD |
| `1D` | `0.1709` | 130,560.00 USD | 0.00 USD | 130,560.00 USD | 15,910.00 USD | 62,270.00 USD | 52,380.00 USD |
| `1D` | `0.1710` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1710` | 30,670.00 USD | 0.00 USD | 30,670.00 USD | 0.00 USD | 25,490.00 USD | 5,180.00 USD |
| `1D` | `0.1712` | 10,130.00 USD | 10,130.00 USD | 0.00 USD | 0.00 USD | 10,130.00 USD | 0.00 USD |
| `7D` | `0.1712` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1713` | 42,020.00 USD | 42,020.00 USD | 0.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD |
| `1D` | `0.1715` | 31,170.00 USD | 31,170.00 USD | 0.00 USD | 0.00 USD | 21,040.00 USD | 0.00 USD |
| `1D` | `0.1718` | 49,040.00 USD | 49,040.00 USD | 0.00 USD | 9,350.00 USD | 8,520.00 USD | 0.00 USD |
| `1D` | `0.1721` | 92,820.00 USD | 92,820.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1722` | 424,830.00 USD | 424,830.00 USD | 0.00 USD | 74,150.00 USD | 0.00 USD | 308,660.00 USD |
| `7D` | `0.1731` | 917,820.00 USD | 917,820.00 USD | 0.00 USD | 493,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1737` | 970,430.00 USD | 970,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 52,610.00 USD |
| `1D` | `0.1739` | 117,050.00 USD | 117,050.00 USD | 0.00 USD | 14,580.00 USD | 0.00 USD | 9,640.00 USD |
| `7D` | `0.1740` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,200.00 USD |
| `7D` | `0.1743` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1745` | 131,820.00 USD | 131,820.00 USD | 0.00 USD | 8,530.00 USD | 0.00 USD | 6,240.00 USD |
| `1D` | `0.1748` | 217,250.00 USD | 217,250.00 USD | 0.00 USD | 55,280.00 USD | 0.00 USD | 30,150.00 USD |
| `7D` | `0.1749` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `0.1751` | 265,790.00 USD | 265,790.00 USD | 0.00 USD | 37,840.00 USD | 0.00 USD | 10,700.00 USD |
| `7D` | `0.1752` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 263,630.00 USD |
| `1D` | `0.1754` | 299,440.00 USD | 299,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33,650.00 USD |
| `7D` | `0.1755` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 37,610.00 USD | 0.00 USD | 169,120.00 USD |
| `1D` | `0.1757` | 388,050.00 USD | 388,050.00 USD | 0.00 USD | 8,970.00 USD | 40,160.00 USD | 39,490.00 USD |
| `7D` | `0.1758` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 173,440.00 USD | 38,670.00 USD | 0.00 USD |
| `1D` | `0.1760` | 564,770.00 USD | 564,770.00 USD | 0.00 USD | 85,150.00 USD | 76,400.00 USD | 15,170.00 USD |
| `7D` | `0.1761` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 373,120.00 USD | 131,090.00 USD | 32,350.00 USD |
| `1D` | `0.1763` | 733,300.00 USD | 733,300.00 USD | 0.00 USD | 84,560.00 USD | 20,760.00 USD | 63,210.00 USD |
| `7D` | `0.1764` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 164,630.00 USD | 215,620.00 USD | 40,340.00 USD |
| `1D` | `0.1766` | 841,520.00 USD | 841,520.00 USD | 0.00 USD | 24,650.00 USD | 20,220.00 USD | 63,360.00 USD |
| `7D` | `0.1767` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 176,410.00 USD | 152,530.00 USD | 8,530.00 USD |
| `1D` | `0.1769` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 45,860.00 USD | 87,060.00 USD | 44,210.00 USD |
| `7D` | `0.1770` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 61,490.00 USD | 147,940.00 USD | 44,400.00 USD |
| `1D` | `0.1772` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 22,380.00 USD | 20,220.00 USD | 28,530.00 USD |
| `7D` | `0.1773` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 103,820.00 USD | 105,810.00 USD | 0.00 USD |
| `1D` | `0.1775` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 74,270.00 USD | 27,710.00 USD | 7,600.00 USD |
| `7D` | `0.1776` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 135,140.00 USD | 69,570.00 USD | 0.00 USD |
| `1D` | `0.1778` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 58,020.00 USD | 87,510.00 USD | 19,880.00 USD |
| `7D` | `0.1779` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 52,730.00 USD | 46,410.00 USD | 131,820.00 USD |
| `1D` | `0.1781` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 50,570.00 USD | 1,060.00 USD | 45,750.00 USD |
| `7D` | `0.1782` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 20,690.00 USD | 13,990.00 USD | 31,180.00 USD |
| `1D` | `0.1784` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 92,690.00 USD | 38,240.00 USD | 18,530.00 USD |
| `7D` | `0.1785` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 153,160.00 USD | 78,850.00 USD | 16,420.00 USD |
| `1D` | `0.1787` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 37,680.00 USD | 54,820.00 USD | 51,690.00 USD |
| `7D` | `0.1788` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 73,130.00 USD | 18,250.00 USD | 14,040.00 USD |
| `1D` | `0.1790` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 53,220.00 USD | 22,930.00 USD | 21,120.00 USD |
| `7D` | `0.1791` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 155,720.00 USD | 17,360.00 USD | 3,940.00 USD |
| `1D` | `0.1793` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 32,720.00 USD | 20,810.00 USD | 20,480.00 USD |
| `7D` | `0.1794` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 27,100.00 USD | 42,780.00 USD | 36,780.00 USD |
| `1D` | `0.1796` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 48,060.00 USD | 66,080.00 USD | 41,280.00 USD |
| `7D` | `0.1797` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 17,130.00 USD | 12,930.00 USD | 7,670.00 USD |
| `1D` | `0.1799` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 16,820.00 USD | 14,880.00 USD | 15,390.00 USD |
| `7D` | `0.1800` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 34,680.00 USD | 64,620.00 USD |
| `1D` | `0.1802` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 15,140.00 USD | 34,770.00 USD | 28,710.00 USD |
| `7D` | `0.1803` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 35,280.00 USD | 25,700.00 USD | 18,250.00 USD |
| `1D` | `0.1805` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 22,680.00 USD | 9,380.00 USD | 27,960.00 USD |
| `7D` | `0.1806` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 11,410.00 USD | 56,850.00 USD | 19,880.00 USD |
| `1D` | `0.1808` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 24,170.00 USD | 27,870.00 USD | 35,880.00 USD |
| `7D` | `0.1809` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 53,670.00 USD | 30,810.00 USD | 58,890.00 USD |
| `1D` | `0.1811` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 39,150.00 USD | 16,000.00 USD | 24,930.00 USD |
| `7D` | `0.1812` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 34,960.00 USD | 16,640.00 USD | 50,510.00 USD |
| `1D` | `0.1814` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 28,390.00 USD | 38,050.00 USD | 28,610.00 USD |
| `7D` | `0.1815` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 60,010.00 USD | 30,810.00 USD | 38,270.00 USD |
| `1D` | `0.1817` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 31,330.00 USD | 11,020.00 USD | 30,640.00 USD |
| `7D` | `0.1818` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 75,040.00 USD | 24,140.00 USD | 10,390.00 USD |
| `1D` | `0.1820` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 34,200.00 USD | 18,550.00 USD | 4,990.00 USD |
| `7D` | `0.1821` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 40,950.00 USD | 33,870.00 USD | 41,820.00 USD |
| `1D` | `0.1823` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 16,740.00 USD | 19,980.00 USD | 17,470.00 USD |
| `7D` | `0.1824` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 39,400.00 USD | 17,880.00 USD | 95,310.00 USD |
| `1D` | `0.1826` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 27,750.00 USD | 6,860.00 USD | 4,500.00 USD |
| `7D` | `0.1827` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 79,610.00 USD | 18,690.00 USD | 65,670.00 USD |
| `1D` | `0.1829` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 3,490.00 USD | 1,640.00 USD | 3,980.00 USD |
| `7D` | `0.1830` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 64,890.00 USD | 20,550.00 USD | 52,010.00 USD |
| `1D` | `0.1832` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 4,090.00 USD | 11,600.00 USD |
| `7D` | `0.1833` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 186,730.00 USD | 49,740.00 USD | 26,350.00 USD |
| `1D` | `0.1835` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 5,030.00 USD | 655.16 USD | 728.16 USD |
| `7D` | `0.1836` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 29,580.00 USD | 83,110.00 USD | 52,650.00 USD |
| `1D` | `0.1838` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 2,640.00 USD | 5,780.00 USD |
| `7D` | `0.1839` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 129,950.00 USD | 41,230.00 USD | 114,190.00 USD |
| `1D` | `0.1841` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 13,150.00 USD | 2,060.00 USD | 7,910.00 USD |
| `7D` | `0.1842` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 71,550.00 USD | 26,100.00 USD | 97,700.00 USD |
| `1D` | `0.1844` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 2,690.00 USD | 5,540.00 USD | 15,280.00 USD |
| `7D` | `0.1845` | 7,080,000.00 USD | 7,080,000.00 USD | 0.00 USD | 34,630.00 USD | 33,340.00 USD | 66,720.00 USD |
| `1D` | `0.1847` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 7,630.00 USD | 7,150.00 USD | 11,230.00 USD |
| `7D` | `0.1848` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 47,730.00 USD | 75,080.00 USD | 135,290.00 USD |
| `1D` | `0.1850` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 3,150.00 USD | 1,300.00 USD |
| `7D` | `0.1851` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 94,780.00 USD | 28,290.00 USD | 220,580.00 USD |
| `1D` | `0.1853` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 1,690.00 USD | 4,440.00 USD |
| `7D` | `0.1854` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 105,210.00 USD | 4,290.00 USD | 63,060.00 USD |
| `1D` | `0.1856` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 4,860.00 USD | 0.00 USD | 7,420.00 USD |
| `7D` | `0.1857` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 116,320.00 USD | 32,070.00 USD | 127,480.00 USD |
| `1D` | `0.1859` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 9,450.00 USD | 1,470.00 USD | 3,670.00 USD |
| `7D` | `0.1860` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 87,180.00 USD | 76,610.00 USD | 74,870.00 USD |
| `1D` | `0.1862` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 1,870.00 USD | 2,970.00 USD | 7,150.00 USD |
| `7D` | `0.1863` | 8,580,000.00 USD | 8,580,000.00 USD | 0.00 USD | 80,860.00 USD | 63,750.00 USD | 61,380.00 USD |
| `1D` | `0.1865` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `0.1866` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 101,070.00 USD | 33,740.00 USD | 39,240.00 USD |
| `1D` | `0.1868` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 3,300.00 USD | 0.00 USD | 5,050.00 USD |
| `7D` | `0.1869` | 9,060,000.00 USD | 9,060,000.00 USD | 0.00 USD | 169,650.00 USD | 66,330.00 USD | 78,120.00 USD |
| `1D` | `0.1871` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 8,950.00 USD | 5,040.00 USD | 9,870.00 USD |
| `7D` | `0.1872` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 91,030.00 USD | 132,480.00 USD | 105,840.00 USD |
| `1D` | `0.1874` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 7,320.00 USD | 2,820.00 USD | 2,290.00 USD |
| `7D` | `0.1875` | 9,540,000.00 USD | 9,540,000.00 USD | 0.00 USD | 68,250.00 USD | 42,310.00 USD | 36,560.00 USD |
| `1D` | `0.1877` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 2,670.00 USD | 2,760.00 USD | 918.24 USD |
| `7D` | `0.1878` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 66,470.00 USD | 37,330.00 USD | 48,000.00 USD |
| `1D` | `0.1880` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 4,530.00 USD | 3,160.00 USD | 7,130.00 USD |
| `7D` | `0.1881` | 9,780,000.00 USD | 9,780,000.00 USD | 0.00 USD | 29,820.00 USD | 44,080.00 USD | 13,200.00 USD |
| `1D` | `0.1883` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 4,630.00 USD | 4,960.00 USD | 0.00 USD |
| `7D` | `0.1884` | 9,890,000.00 USD | 9,890,000.00 USD | 0.00 USD | 10,560.00 USD | 36,820.00 USD | 58,860.00 USD |
| `1D` | `0.1886` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 13,740.00 USD | 2,220.00 USD | 4,330.00 USD |
| `7D` | `0.1887` | 9,940,000.00 USD | 9,940,000.00 USD | 0.00 USD | 22,970.00 USD | 0.00 USD | 25,760.00 USD |
| `1D` | `0.1889` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 3,580.00 USD | 3,150.00 USD | 7,640.00 USD |
| `7D` | `0.1890` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 36,740.00 USD | 17,330.00 USD | 75,130.00 USD |
| `1D` | `0.1892` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 1,140.00 USD | 8,660.00 USD | 1,070.00 USD |
| `7D` | `0.1893` | 10,120,000.00 USD | 10,120,000.00 USD | 0.00 USD | 32,450.00 USD | 6,940.00 USD | 16,820.00 USD |
| `1D` | `0.1895` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 4,810.00 USD | 4,140.00 USD | 3,890.00 USD |
| `7D` | `0.1896` | 10,230,000.00 USD | 10,230,000.00 USD | 0.00 USD | 62,730.00 USD | 27,440.00 USD | 18,680.00 USD |
| `1D` | `0.1898` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 7,030.00 USD | 16,880.00 USD | 0.00 USD |
| `7D` | `0.1899` | 10,300,000.00 USD | 10,300,000.00 USD | 0.00 USD | 11,530.00 USD | 38,530.00 USD | 20,420.00 USD |
| `1D` | `0.1901` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 11,640.00 USD | 4,150.00 USD | 7,190.00 USD |
| `7D` | `0.1902` | 10,330,000.00 USD | 10,330,000.00 USD | 0.00 USD | 14,330.00 USD | 0.00 USD | 10,800.00 USD |
| `1D` | `0.1904` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 1,660.00 USD | 8,830.00 USD |
| `7D` | `0.1905` | 10,380,000.00 USD | 10,380,000.00 USD | 0.00 USD | 8,720.00 USD | 24,800.00 USD | 24,210.00 USD |
| `1D` | `0.1907` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 2,490.00 USD | 11,300.00 USD | 6,450.00 USD |
| `7D` | `0.1908` | 10,480,000.00 USD | 10,480,000.00 USD | 0.00 USD | 25,220.00 USD | 43,160.00 USD | 28,600.00 USD |
| `1D` | `0.1910` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 1,050.00 USD | 1,140.00 USD |
| `7D` | `0.1911` | 10,490,000.00 USD | 10,490,000.00 USD | 0.00 USD | 0.00 USD | 9,380.00 USD | 0.00 USD |
| `1D` | `0.1913` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 4,910.00 USD | 2,880.00 USD | 2,050.00 USD |
| `7D` | `0.1914` | 10,510,000.00 USD | 10,510,000.00 USD | 0.00 USD | 7,460.00 USD | 11,160.00 USD | 0.00 USD |
| `1D` | `0.1916` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 12,220.00 USD | 16,330.00 USD | 2,290.00 USD |
| `7D` | `0.1917` | 10,530,000.00 USD | 10,530,000.00 USD | 0.00 USD | 0.00 USD | 11,840.00 USD | 11,900.00 USD |
| `1D` | `0.1919` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,740.00 USD |
| `1D` | `0.1922` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 9,260.00 USD | 2,030.00 USD | 6,410.00 USD |
| `7D` | `0.1923` | 10,550,000.00 USD | 10,550,000.00 USD | 0.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD |
| `1D` | `0.1925` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 11,380.00 USD | 5,630.00 USD | 0.00 USD |
| `7D` | `0.1926` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 11,600.00 USD | 13,630.00 USD | 0.00 USD |
| `1D` | `0.1928` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 3,390.00 USD | 1,930.00 USD | 4,000.00 USD |
| `1D` | `0.1931` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 4,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1937` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 1,150.00 USD | 2,140.00 USD |
| `7D` | `0.1944` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1950` | 10,590,000.00 USD | 10,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `212.63M` | Total OI Tokens: `1,242,084,805.4 ARB`
  * 1h OI Change: `-2.25%` | 4h OI Change: `-1.80%` | 24h OI Change: `-9.63%`
  * Exchange Breakdown: Binance=`48.80M` | Bybit=`29.44M` | OKX=`17.29M` | Hyperliquid=`15.25M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `9.56K` | Last 24h: `10.97K` | Last 3d: `22.34K` | Last 7d: `43.06K`
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
| `15M` | `ARB` | `42.55%` | `57.45%` | `0.74` | 1,210,000.00 USD |
| `15M` | `Binance` | `43.49%` | `56.51%` | `0.77` | 364,750.00 USD |
| `15M` | `OKX` | `51.07%` | `48.93%` | `1.04` | 244,190.00 USD |
| `15M` | `Bybit` | `29.7%` | `70.3%` | `0.42` | 138,610.00 USD |
| `15M` | `KuCoin` | `49.01%` | `50.99%` | `0.96` | 9,940.00 USD |
| `15M` | `Gate` | `18.89%` | `81.11%` | `0.23` | 5,790.00 USD |
| `15M` | `Bitget` | `55.35%` | `44.65%` | `1.24` | 40,430.00 USD |
| `15M` | `BingX` | `45.56%` | `54.44%` | `0.84` | 51,390.00 USD |
| `15M` | `MEXC` | `25.35%` | `74.65%` | `0.34` | 113,330.00 USD |
| `15M` | `Bitunix` | `53.26%` | `46.74%` | `1.14` | 9,910.00 USD |
| `15M` | `Hyperliquid` | `10.86%` | `89.14%` | `0.12` | 6,900.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `34.55%` | `65.45%` | `0.53` | 185,430.00 USD |
| `15M` | `Crypto.com` | `0%` | `100%` | `0.00` | 0.11 USD |
| `15M` | `WhiteBIT` | `98.97%` | `1.03%` | `96.09` | 42,100.00 USD |
| `15M` | `HTX` | `1.09%` | `98.91%` | `0.01` | 41.39 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `68.25%` | `31.75%` | `2.15` | 157.56 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 317.02 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 1,430.00 USD |
| `15M` | `Whale Positions` | `43.49%` | `56.51%` | `0.77` | 364,750.00 USD |
| `15M` | `Global Accounts` | `42.55%` | `57.45%` | `0.74` | 1,210,000.00 USD |
| `1H` | `ARB` | `40.62%` | `59.38%` | `0.68` | 12,580,000.00 USD |
| `1H` | `Binance` | `37.47%` | `62.53%` | `0.60` | 4,490,000.00 USD |
| `1H` | `OKX` | `35.47%` | `64.53%` | `0.55` | 2,990,000.00 USD |
| `1H` | `Bybit` | `49.43%` | `50.57%` | `0.98` | 1,030,000.00 USD |
| `1H` | `KuCoin` | `52.33%` | `47.67%` | `1.10` | 139,130.00 USD |
| `1H` | `Gate` | `48.04%` | `51.96%` | `0.92` | 380,970.00 USD |
| `1H` | `Bitget` | `37.78%` | `62.22%` | `0.61` | 673,870.00 USD |
| `1H` | `BingX` | `54.21%` | `45.79%` | `1.18` | 418,970.00 USD |
| `1H` | `MEXC` | `31.32%` | `68.68%` | `0.46` | 1,270,000.00 USD |
| `1H` | `Bitunix` | `42.75%` | `57.25%` | `0.75` | 194,560.00 USD |
| `1H` | `Hyperliquid` | `60.52%` | `39.48%` | `1.53` | 170,120.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.94%` | `50.06%` | `1.00` | 406,890.00 USD |
| `1H` | `Crypto.com` | `54.47%` | `45.53%` | `1.20` | 5,420.00 USD |
| `1H` | `WhiteBIT` | `88.97%` | `11.03%` | `8.07` | 340,390.00 USD |
| `1H` | `HTX` | `56.03%` | `43.97%` | `1.27` | 4,340.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `24.56%` | `75.44%` | `0.33` | 31,910.00 USD |
| `1H` | `Aster` | `82.55%` | `17.45%` | `4.73` | 10,660.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `34.5%` | `65.5%` | `0.53` | 14,750.00 USD |
| `1H` | `Whale Positions` | `37.47%` | `62.53%` | `0.60` | 4,490,000.00 USD |
| `1H` | `Global Accounts` | `40.62%` | `59.38%` | `0.68` | 12,580,000.00 USD |
| `4H` | `ARB` | `51.25%` | `48.75%` | `1.05` | 24,260,000.00 USD |
| `4H` | `Binance` | `50.72%` | `49.28%` | `1.03` | 8,510,000.00 USD |
| `4H` | `OKX` | `52.8%` | `47.2%` | `1.12` | 3,030,000.00 USD |
| `4H` | `Bybit` | `51.16%` | `48.84%` | `1.05` | 2,400,000.00 USD |
| `4H` | `KuCoin` | `31.58%` | `68.42%` | `0.46` | 124,890.00 USD |
| `4H` | `Gate` | `53.65%` | `46.35%` | `1.16` | 316,670.00 USD |
| `4H` | `Bitget` | `57.33%` | `42.67%` | `1.34` | 818,920.00 USD |
| `4H` | `BingX` | `38.91%` | `61.09%` | `0.64` | 2,010,000.00 USD |
| `4H` | `MEXC` | `48.93%` | `51.07%` | `0.96` | 1,620,000.00 USD |
| `4H` | `Bitunix` | `49.78%` | `50.22%` | `0.99` | 264,460.00 USD |
| `4H` | `Hyperliquid` | `81.34%` | `18.66%` | `4.36` | 331,450.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.55%` | `51.45%` | `0.94` | 4,140,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `100%` | `0.00` | 2.92 USD |
| `4H` | `WhiteBIT` | `95.99%` | `4.01%` | `23.94` | 616,940.00 USD |
| `4H` | `HTX` | `66.73%` | `33.27%` | `2.01` | 9,200.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `31.6%` | `68.4%` | `0.46` | 18,710.00 USD |
| `4H` | `Aster` | `2.51%` | `97.49%` | `0.03` | 9,190.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.67%` | `48.33%` | `1.07` | 26,900.00 USD |
| `4H` | `Whale Positions` | `50.72%` | `49.28%` | `1.03` | 8,510,000.00 USD |
| `4H` | `Global Accounts` | `51.25%` | `48.75%` | `1.05` | 24,260,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1719` | `0.1724` | `0.1719` | `0.1738` | `0.1711` | 1,417,466.81 USD | 785,073.10 USD | 632,393.70 USD | 152,679.40 USD | `+10.77%` | `25B / 12S` |
| `5:00 UTC` | `0.1726` | `0.1727` | `0.1726` | `0.1738` | `0.1722` | 1,207,079.68 USD | 553,041.78 USD | 654,037.90 USD | -100,996.12 USD | `-8.37%` | `23B / 52S` |
| `0:00 UTC` | `0.1745` | `0.1737` | `0.1745` | `0.1745` | `0.1722` | 1,081,294.02 USD | 483,634.60 USD | 597,659.42 USD | -114,024.81 USD | `-10.55%` | `11B / 18S` |
| `5:00 UTC` | `0.1743` | `0.1742` | `0.1743` | `0.1749` | `0.1731` | 1,329,025.77 USD | 664,234.01 USD | 664,791.75 USD | -557.74 USD | `-0.04%` | `35B / 34S` |
| `0:00 UTC` | `0.1740` | `0.1746` | `0.1740` | `0.1759` | `0.1738` | 1,727,950.91 USD | 719,456.36 USD | 1,008,494.54 USD | -289,038.18 USD | `-16.73%` | `12B / 27S` |
| `5:00 UTC` | `0.1735` | `0.1735` | `0.1735` | `0.1745` | `0.1727` | 1,465,256.89 USD | 552,173.71 USD | 913,083.17 USD | -360,909.46 USD | `-24.63%` | `12B / 58S` |
| `0:00 UTC` | `0.1724` | `0.1726` | `0.1724` | `0.1732` | `0.1721` | 813,790.61 USD | 314,421.23 USD | 499,369.38 USD | -184,948.15 USD | `-22.73%` | `12B / 32S` |
| `5:00 UTC` | `0.1722` | `0.1719` | `0.1722` | `0.1724` | `0.1714` | 868,922.61 USD | 333,299.44 USD | 535,623.17 USD | -202,323.73 USD | `-23.28%` | `11B / 37S` |
| `0:00 UTC` | `0.1715` | `0.1718` | `0.1715` | `0.1727` | `0.1712` | 1,082,802.27 USD | 363,691.86 USD | 719,110.40 USD | -355,418.54 USD | `-32.82%` | `13B / 48S` |
| `5:00 UTC` | `0.1711` | `0.1711` | `0.1711` | `0.1715` | `0.1708` | 573,349.20 USD | 294,300.06 USD | 279,049.14 USD | 15,250.92 USD | `+2.66%` | `8B / 17S` |

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
| `5m` | 17,900.00 USD | -108,330.00 USD | **`DISTRIBUTION`** |
| `15m` | -156,680.00 USD | -669,560.00 USD | **`DISTRIBUTION`** |
| `30m` | -55,540.00 USD | -1,220,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -131,610.00 USD | -2,040,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -145,530.00 USD | -1,930,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -89,260.00 USD | -2,390,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -7,230.00 USD | -3,390,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 383,880.00 USD | -3,330,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -124,560.00 USD | -4,820,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -516,110.00 USD | -6,280,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -4,650,000.00 USD | -29,400,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -32,070,000.00 USD | -160,110,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+17.90K` | 15m=`-156.68K` | 1h=`-131.61K` | 24h=`-516.11K`
* Futures Capital Netflows: 5m=`-108.33K` | 15m=`-669.56K` | 1h=`-2.04M` | 24h=`-6.28M`
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
  * `2026-10-29 22:45:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:14 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [dol.gov] - (Sentiment: `Neutral`)


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
