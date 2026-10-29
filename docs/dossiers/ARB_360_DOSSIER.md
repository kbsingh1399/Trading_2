# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-29 23:40:50 IST` (`2026-10-29 18:10:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1688` | `0.1697` | `0.1687` | `0.1696` | `1,999,550` | 338,579.08 USD | 151,636.22 USD | `+44.79%` | -5,450,623.82 USD | `+1.73` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.1696` | `0.1702` | `0.1695` | `0.1701` | `1,671,637` | 283,751.08 USD | 20,981.80 USD | `+7.39%` | -5,429,642.02 USD | `+0.54` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1701` | `0.1704` | `0.1701` | `0.1704` | `207,070` | 35,249.72 USD | 10,840.79 USD | `+30.75%` | -5,418,801.23 USD | `+0.45` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1713` | `0.1719` | `0.1689` | `0.1694` | `7,644,654` | 1,300,882.78 USD | -237,880.44 USD | `-18.29%` | -5,567,651.19 USD | `-0.62` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1694` | `0.1697` | `0.1681` | `0.1696` | `7,652,937` | 1,292,914.43 USD | 131,222.13 USD | `+10.15%` | -5,436,429.07 USD | `+1.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1696` | `0.1703` | `0.1695` | `0.1703` | `1,798,578` | 305,350.81 USD | 26,154.88 USD | `+8.57%` | -5,410,274.18 USD | `+0.88` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1745` | `0.1759` | `0.1714` | `0.1724` | `28,115,276` | 4,875,921.02 USD | -1,037,219.52 USD | `-21.27%` | -4,109,099.99 USD | `-2.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1724` | `0.1727` | `0.1681` | `0.1696` | `26,281,427` | 4,477,475.52 USD | -441,479.21 USD | `-9.86%` | -4,550,579.20 USD | `-0.59` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1696` | `0.1703` | `0.1695` | `0.1703` | `1,798,578` | 305,350.81 USD | 26,154.88 USD | `+8.57%` | -4,524,424.32 USD | `+0.54` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,634,787.89 USD | `-0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,872,916.24 USD | `-1.36` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1681` | `0.1702` | `56,192,216` | 9,658,225.49 USD | -1,453,065.71 USD | `-15.04%` | -4,325,981.95 USD | `-1.33` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1721` | `0.1729` | `0.1635` | `0.1652` | `91,809,989` | 15,344,891.97 USD | 203,909.29 USD | `+1.33%` | -294,464.16 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1652` | `0.1687` | `0.1623` | `0.1631` | `68,085,678` | 11,252,816.65 USD | -909,329.92 USD | `-8.08%` | -1,203,794.08 USD | `-1.11` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,634,787.89 USD | `-0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,872,916.24 USD | `-1.36` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1681` | `0.1702` | `56,192,216` | 9,658,225.49 USD | -1,453,065.71 USD | `-15.04%` | -4,325,981.95 USD | `-1.33` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:36:01 IST` |

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
  * 24H Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+5.11%`) | Long MP=`0.1598` (Vol: 147,500.00 USD, Dist: `--5.85%`)
  * 48H Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+5.11%`) | Long MP=`0.1598` (Vol: 154,300.00 USD, Dist: `--5.85%`)
  * 3D Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+5.11%`) | Long MP=`0.1598` (Vol: 205,900.00 USD, Dist: `--5.85%`)
  * 7D Horizon: Short MP=`0.1834` (Vol: 181,500.00 USD, Dist: `+8.03%`) | Long MP=`0.1616` (Vol: 292,500.00 USD, Dist: `--4.78%`)
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
| `Live` | `Long Liquidation` | `0.1455` | 111.10 USD | 644,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1459` | 10,900,000.00 USD | 10,900,000.00 USD | 0.00 USD | 3,430.00 USD | 7,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1465` | 10,890,000.00 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 30,880.00 USD | 644,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1468` | 10,890,000.00 USD | 10,890,000.00 USD | 9,720.00 USD | 9,180.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1471` | 10,860,000.00 USD | 10,860,000.00 USD | 6,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1474` | 10,850,000.00 USD | 10,850,000.00 USD | 6,490.00 USD | 9,220.00 USD | 5,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 73,930.00 USD | 613,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1477` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 25,460.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1480` | 10,800,000.00 USD | 10,800,000.00 USD | 6,990.00 USD | 29,300.00 USD | 20,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1483` | 10,740,000.00 USD | 10,740,000.00 USD | 42,230.00 USD | 16,640.00 USD | 33,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,720.00 USD | 539,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1486` | 10,650,000.00 USD | 10,650,000.00 USD | 18,610.00 USD | 10,470.00 USD | 25,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1489` | 10,600,000.00 USD | 10,600,000.00 USD | 11,170.00 USD | 3,710.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1492` | 10,570,000.00 USD | 10,570,000.00 USD | 40,320.00 USD | 17,880.00 USD | 27,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1495` | 10,490,000.00 USD | 10,490,000.00 USD | 34,650.00 USD | 18,690.00 USD | 12,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 35,380.00 USD | 537,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1498` | 10,420,000.00 USD | 10,420,000.00 USD | 42,100.00 USD | 9,610.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1501` | 10,360,000.00 USD | 10,360,000.00 USD | 21,010.00 USD | 7,930.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1504` | 10,310,000.00 USD | 10,310,000.00 USD | 17,800.00 USD | 11,590.00 USD | 44,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1505` | 102,290.00 USD | 501,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1507` | 10,240,000.00 USD | 10,240,000.00 USD | 28,940.00 USD | 12,910.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1509` | 4,500,000.00 USD | 4,500,000.00 USD | 11,070.00 USD | 6,000.00 USD | 5,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1510` | 10,170,000.00 USD | 10,170,000.00 USD | 12,660.00 USD | 12,930.00 USD | 29,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1512` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 5,780.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1513` | 10,110,000.00 USD | 10,110,000.00 USD | 32,900.00 USD | 17,610.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1515` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 1,730.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 3,930.00 USD | 399,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1516` | 10,020,000.00 USD | 10,020,000.00 USD | 54,550.00 USD | 0.00 USD | 43,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1518` | 4,470,000.00 USD | 4,470,000.00 USD | 8,770.00 USD | 4,320.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1519` | 9,920,000.00 USD | 9,920,000.00 USD | 37,430.00 USD | 19,520.00 USD | 70,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1521` | 4,450,000.00 USD | 4,450,000.00 USD | 9,450.00 USD | 1,470.00 USD | 5,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1522` | 9,800,000.00 USD | 9,800,000.00 USD | 49,800.00 USD | 9,640.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1524` | 4,430,000.00 USD | 4,430,000.00 USD | 1,870.00 USD | 2,970.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1525` | 9,710,000.00 USD | 9,710,000.00 USD | 25,790.00 USD | 13,700.00 USD | 19,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1525` | 42,800.00 USD | 395,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1527` | 4,420,000.00 USD | 4,420,000.00 USD | 3,300.00 USD | 0.00 USD | 11,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1528` | 9,650,000.00 USD | 9,650,000.00 USD | 75,690.00 USD | 27,110.00 USD | 27,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1530` | 4,400,000.00 USD | 4,400,000.00 USD | 4,960.00 USD | 5,040.00 USD | 8,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1531` | 9,520,000.00 USD | 9,520,000.00 USD | 35,030.00 USD | 8,400.00 USD | 16,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1533` | 4,380,000.00 USD | 4,380,000.00 USD | 11,310.00 USD | 0.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1534` | 9,460,000.00 USD | 9,460,000.00 USD | 15,780.00 USD | 17,430.00 USD | 20,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 19,400.00 USD | 352,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1536` | 4,370,000.00 USD | 4,370,000.00 USD | 4,320.00 USD | 5,590.00 USD | 6,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1537` | 9,410,000.00 USD | 9,410,000.00 USD | 37,050.00 USD | 11,700.00 USD | 10,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1539` | 4,350,000.00 USD | 4,350,000.00 USD | 5,810.00 USD | 8,110.00 USD | 5,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1540` | 9,350,000.00 USD | 9,350,000.00 USD | 14,000.00 USD | 6,530.00 USD | 5,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1542` | 4,330,000.00 USD | 4,330,000.00 USD | 5,750.00 USD | 0.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1543` | 9,320,000.00 USD | 9,320,000.00 USD | 9,250.00 USD | 3,590.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1545` | 4,320,000.00 USD | 4,320,000.00 USD | 13,270.00 USD | 5,370.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1545` | 26,170.00 USD | 333,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1546` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 0.00 USD | 5,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1548` | 4,290,000.00 USD | 4,290,000.00 USD | 1,140.00 USD | 8,660.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1549` | 9,300,000.00 USD | 9,300,000.00 USD | 11,570.00 USD | 6,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1551` | 4,280,000.00 USD | 4,280,000.00 USD | 4,810.00 USD | 4,140.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1552` | 9,280,000.00 USD | 9,280,000.00 USD | 23,110.00 USD | 7,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1554` | 4,270,000.00 USD | 4,270,000.00 USD | 18,660.00 USD | 19,270.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1555` | 9,250,000.00 USD | 9,250,000.00 USD | 0.00 USD | 0.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1555` | 40,060.00 USD | 307,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1557` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 3,410.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1558` | 9,240,000.00 USD | 9,240,000.00 USD | 0.00 USD | 10,990.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1560` | 4,220,000.00 USD | 4,220,000.00 USD | 5,460.00 USD | 11,300.00 USD | 7,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1561` | 9,220,000.00 USD | 9,220,000.00 USD | 0.00 USD | 5,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1563` | 4,190,000.00 USD | 4,190,000.00 USD | 3,050.00 USD | 1,050.00 USD | 20,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1564` | 9,220,000.00 USD | 9,220,000.00 USD | 24,300.00 USD | 28,690.00 USD | 21,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1565` | 21,460.00 USD | 267,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1566` | 4,170,000.00 USD | 4,170,000.00 USD | 45,560.00 USD | 11,570.00 USD | 15,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1567` | 9,140,000.00 USD | 9,140,000.00 USD | 41,770.00 USD | 15,360.00 USD | 15,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1569` | 4,100,000.00 USD | 4,100,000.00 USD | 24,600.00 USD | 31,270.00 USD | 7,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1570` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 5,100.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1572` | 4,040,000.00 USD | 4,040,000.00 USD | 34,670.00 USD | 14,240.00 USD | 17,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1573` | 9,050,000.00 USD | 9,050,000.00 USD | 58,830.00 USD | 56,100.00 USD | 25,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1575` | 3,970,000.00 USD | 3,970,000.00 USD | 34,430.00 USD | 19,170.00 USD | 6,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1575` | 4,940.00 USD | 245,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1576` | 8,910,000.00 USD | 8,910,000.00 USD | 26,600.00 USD | 102,190.00 USD | 54,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1578` | 3,910,000.00 USD | 3,910,000.00 USD | 62,820.00 USD | 64,050.00 USD | 24,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1579` | 8,730,000.00 USD | 8,730,000.00 USD | 101,500.00 USD | 95,190.00 USD | 42,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1581` | 3,760,000.00 USD | 3,760,000.00 USD | 31,970.00 USD | 3,940.00 USD | 22,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1582` | 8,490,000.00 USD | 8,490,000.00 USD | 56,130.00 USD | 13,480.00 USD | 89,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1584` | 3,700,000.00 USD | 3,700,000.00 USD | 34,630.00 USD | 11,050.00 USD | 13,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1585` | 8,330,000.00 USD | 8,330,000.00 USD | 87,110.00 USD | 50,340.00 USD | 75,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1585` | 5,650.00 USD | 240,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1587` | 3,640,000.00 USD | 3,640,000.00 USD | 6,650.00 USD | 21,380.00 USD | 12,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1588` | 8,120,000.00 USD | 8,120,000.00 USD | 34,830.00 USD | 30,030.00 USD | 41,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1590` | 3,600,000.00 USD | 3,600,000.00 USD | 13,490.00 USD | 27,950.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1591` | 8,010,000.00 USD | 8,010,000.00 USD | 110,640.00 USD | 49,670.00 USD | 60,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1593` | 3,550,000.00 USD | 3,550,000.00 USD | 47,380.00 USD | 6,320.00 USD | 23,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1594` | 7,790,000.00 USD | 7,790,000.00 USD | 85,560.00 USD | 39,260.00 USD | 102,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1595` | 64,950.00 USD | 235,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1596` | 3,470,000.00 USD | 3,470,000.00 USD | 29,470.00 USD | 19,190.00 USD | 35,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1597` | 7,560,000.00 USD | 7,560,000.00 USD | 228,850.00 USD | 96,110.00 USD | 102,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1599` | 3,390,000.00 USD | 3,390,000.00 USD | 69,610.00 USD | 21,270.00 USD | 37,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1600` | 7,140,000.00 USD | 7,140,000.00 USD | 105,580.00 USD | 38,830.00 USD | 76,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1602` | 3,260,000.00 USD | 3,260,000.00 USD | 55,540.00 USD | 46,820.00 USD | 7,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1603` | 6,910,000.00 USD | 6,910,000.00 USD | 62,240.00 USD | 54,840.00 USD | 81,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1605` | 3,150,000.00 USD | 3,150,000.00 USD | 34,500.00 USD | 18,980.00 USD | 37,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1605` | 20,620.00 USD | 170,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1606` | 6,720,000.00 USD | 6,720,000.00 USD | 211,140.00 USD | 149,480.00 USD | 227,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1608` | 3,060,000.00 USD | 3,060,000.00 USD | 66,600.00 USD | 40,820.00 USD | 21,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1609` | 6,130,000.00 USD | 6,130,000.00 USD | 92,990.00 USD | 229,060.00 USD | 182,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1611` | 2,930,000.00 USD | 2,930,000.00 USD | 135,640.00 USD | 131,510.00 USD | 55,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1612` | 5,620,000.00 USD | 5,620,000.00 USD | 281,220.00 USD | 247,430.00 USD | 159,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1614` | 2,610,000.00 USD | 2,610,000.00 USD | 55,510.00 USD | 27,060.00 USD | 53,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1615` | 4,930,000.00 USD | 4,930,000.00 USD | 300,450.00 USD | 107,900.00 USD | 374,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1615` | 17,950.00 USD | 149,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1617` | 2,470,000.00 USD | 2,470,000.00 USD | 73,170.00 USD | 27,450.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1618` | 4,150,000.00 USD | 4,150,000.00 USD | 310,070.00 USD | 132,060.00 USD | 310,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1620` | 2,350,000.00 USD | 2,350,000.00 USD | 42,020.00 USD | 52,870.00 USD | 60,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1621` | 3,400,000.00 USD | 3,400,000.00 USD | 228,220.00 USD | 148,260.00 USD | 314,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1623` | 2,190,000.00 USD | 2,190,000.00 USD | 53,880.00 USD | 67,020.00 USD | 26,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1624` | 2,710,000.00 USD | 2,710,000.00 USD | 381,800.00 USD | 138,890.00 USD | 119,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1625` | 98,470.00 USD | 131,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1626` | 2,040,000.00 USD | 2,040,000.00 USD | 15,710.00 USD | 12,640.00 USD | 25,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1627` | 2,070,000.00 USD | 2,070,000.00 USD | 291,760.00 USD | 0.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1629` | 1,990,000.00 USD | 1,990,000.00 USD | 14,220.00 USD | 33,030.00 USD | 19,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1630` | 1,760,000.00 USD | 1,760,000.00 USD | 9,210.00 USD | 0.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1632` | 1,920,000.00 USD | 1,920,000.00 USD | 12,400.00 USD | 25,710.00 USD | 17,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1635` | 1,870,000.00 USD | 1,870,000.00 USD | 29,710.00 USD | 1,640.00 USD | 11,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1635` | 251.51 USD | 33,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1636` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 13,670.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1638` | 1,820,000.00 USD | 1,820,000.00 USD | 9,410.00 USD | 22,520.00 USD | 42,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1639` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 62,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1641` | 1,750,000.00 USD | 1,750,000.00 USD | 7,360.00 USD | 6,090.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1642` | 1,650,000.00 USD | 1,650,000.00 USD | 22,480.00 USD | 29,240.00 USD | 26,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1644` | 1,730,000.00 USD | 1,730,000.00 USD | 25,590.00 USD | 20,340.00 USD | 27,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1645` | 1,570,000.00 USD | 1,570,000.00 USD | 34,760.00 USD | 8,990.00 USD | 7,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1645` | 18,010.00 USD | 32,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1647` | 1,650,000.00 USD | 1,650,000.00 USD | 40,030.00 USD | 32,000.00 USD | 24,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1648` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1650` | 1,560,000.00 USD | 1,560,000.00 USD | 12,400.00 USD | 24,600.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1651` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 51,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1653` | 1,510,000.00 USD | 1,510,000.00 USD | 35,120.00 USD | 13,140.00 USD | 34,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1654` | 1,460,000.00 USD | 1,460,000.00 USD | 33,810.00 USD | 31,800.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1655` | 14,870.00 USD | 14,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1656` | 1,430,000.00 USD | 1,430,000.00 USD | 38,480.00 USD | 51,020.00 USD | 33,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1657` | 1,380,000.00 USD | 1,380,000.00 USD | 10,890.00 USD | 0.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1659` | 1,310,000.00 USD | 1,310,000.00 USD | 43,890.00 USD | 19,240.00 USD | 58,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1660` | 1,350,000.00 USD | 1,350,000.00 USD | 29,890.00 USD | 11,020.00 USD | 33,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1662` | 1,190,000.00 USD | 1,190,000.00 USD | 20,300.00 USD | 18,480.00 USD | 64,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1663` | 1,280,000.00 USD | 1,280,000.00 USD | 86,050.00 USD | 51,000.00 USD | 75,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1665` | 1,080,000.00 USD | 1,080,000.00 USD | 64,660.00 USD | 59,180.00 USD | 67,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1666` | 1,060,000.00 USD | 1,060,000.00 USD | 49,590.00 USD | 32,780.00 USD | 28,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1668` | 892,010.00 USD | 892,010.00 USD | 96,150.00 USD | 58,130.00 USD | 37,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1669` | 953,030.00 USD | 953,030.00 USD | 11,410.00 USD | 64,050.00 USD | 42,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1671` | 699,970.00 USD | 699,970.00 USD | 46,140.00 USD | 21,810.00 USD | 24,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1672` | 834,850.00 USD | 834,850.00 USD | 70,540.00 USD | 38,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1674` | 607,950.00 USD | 607,950.00 USD | 21,310.00 USD | 46,960.00 USD | 39,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1675` | 726,240.00 USD | 726,240.00 USD | 64,490.00 USD | 105,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1677` | 499,830.00 USD | 499,830.00 USD | 14,620.00 USD | 22,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1678` | 555,840.00 USD | 555,840.00 USD | 71,860.00 USD | 79,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1680` | 462,730.00 USD | 462,730.00 USD | 75,420.00 USD | 21,620.00 USD | 31,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1681` | 404,060.00 USD | 404,060.00 USD | 69,520.00 USD | 36,390.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1683` | 334,580.00 USD | 334,580.00 USD | 88,790.00 USD | 20,110.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1684` | 282,830.00 USD | 282,830.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1686` | 196,770.00 USD | 196,770.00 USD | 0.00 USD | 23,410.00 USD | 6,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1689` | 166,890.00 USD | 166,890.00 USD | 0.00 USD | 6,980.00 USD | 8,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1690` | 207,880.00 USD | 207,880.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1692` | 151,340.00 USD | 151,340.00 USD | 55,320.00 USD | 66,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1693` | 169,210.00 USD | 169,210.00 USD | 21,780.00 USD | 32,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1695` | 29,860.00 USD | 29,860.00 USD | 7,570.00 USD | 22,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1696` | 115,360.00 USD | 115,360.00 USD | 0.00 USD | 87,350.00 USD | 28,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1698` | 64,150.00 USD | 64,150.00 USD | 7,460.00 USD | 56,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1699` | 44,160.00 USD | 44,160.00 USD | 0.00 USD | 25,330.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1701` | 69,810.00 USD | 69,810.00 USD | 0.00 USD | 5,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1702` | 113,860.00 USD | 113,860.00 USD | 22,820.00 USD | 46,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1704` | 94,470.00 USD | 94,470.00 USD | 0.00 USD | 14,420.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1707` | 205,240.00 USD | 205,240.00 USD | 37,960.00 USD | 68,660.00 USD | 4,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1708` | 204,050.00 USD | 204,050.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1713` | 215,370.00 USD | 215,370.00 USD | 0.00 USD | 10,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1714` | 246,060.00 USD | 246,060.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1716` | 236,410.00 USD | 236,410.00 USD | 0.00 USD | 21,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1719` | 254,280.00 USD | 254,280.00 USD | 9,350.00 USD | 8,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1720` | 400,420.00 USD | 400,420.00 USD | 0.00 USD | 0.00 USD | 154,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1722` | 330,770.00 USD | 330,770.00 USD | 63,350.00 USD | 13,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1723` | 646,080.00 USD | 646,080.00 USD | 74,150.00 USD | 0.00 USD | 171,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1725` | 346,660.00 USD | 346,660.00 USD | 0.00 USD | 0.00 USD | 15,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1728` | 353,380.00 USD | 353,380.00 USD | 0.00 USD | 0.00 USD | 6,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1729` | 783,670.00 USD | 783,670.00 USD | 137,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1732` | 1,140,000.00 USD | 1,140,000.00 USD | 355,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1734` | 363,450.00 USD | 363,450.00 USD | 0.00 USD | 0.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1737` | 378,030.00 USD | 378,030.00 USD | 14,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1738` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 83,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1740` | 387,680.00 USD | 387,680.00 USD | 0.00 USD | 0.00 USD | 9,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1743` | 397,640.00 USD | 397,640.00 USD | 0.00 USD | 0.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1744` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1746` | 415,670.00 USD | 415,670.00 USD | 8,530.00 USD | 0.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1749` | 532,090.00 USD | 532,090.00 USD | 80,070.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1750` | 1,470,000.00 USD | 1,470,000.00 USD | 69,520.00 USD | 0.00 USD | 167,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1752` | 577,780.00 USD | 577,780.00 USD | 13,050.00 USD | 0.00 USD | 32,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1753` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 191,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1755` | 624,900.00 USD | 624,900.00 USD | 9,790.00 USD | 14,790.00 USD | 22,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1756` | 1,840,000.00 USD | 1,840,000.00 USD | 75,620.00 USD | 0.00 USD | 97,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1758` | 766,260.00 USD | 766,260.00 USD | 73,290.00 USD | 31,940.00 USD | 36,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1759` | 2,120,000.00 USD | 2,120,000.00 USD | 238,650.00 USD | 38,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1761` | 956,910.00 USD | 956,910.00 USD | 53,970.00 USD | 88,390.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1762` | 2,650,000.00 USD | 2,650,000.00 USD | 310,130.00 USD | 196,430.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1764` | 1,110,000.00 USD | 1,110,000.00 USD | 68,490.00 USD | 25,840.00 USD | 61,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1765` | 3,040,000.00 USD | 3,040,000.00 USD | 154,540.00 USD | 185,180.00 USD | 48,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1765` | 339.06 USD | 339.06 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1767` | 1,260,000.00 USD | 1,260,000.00 USD | 39,860.00 USD | 52,820.00 USD | 52,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1768` | 3,380,000.00 USD | 3,380,000.00 USD | 161,560.00 USD | 153,660.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1770` | 1,370,000.00 USD | 1,370,000.00 USD | 28,650.00 USD | 43,060.00 USD | 38,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1771` | 3,610,000.00 USD | 3,610,000.00 USD | 69,030.00 USD | 138,810.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1773` | 1,450,000.00 USD | 1,450,000.00 USD | 30,810.00 USD | 28,980.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1774` | 3,870,000.00 USD | 3,870,000.00 USD | 148,780.00 USD | 115,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1776` | 1,580,000.00 USD | 1,580,000.00 USD | 85,560.00 USD | 19,390.00 USD | 21,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1777` | 4,040,000.00 USD | 4,040,000.00 USD | 67,350.00 USD | 40,700.00 USD | 59,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1779` | 1,710,000.00 USD | 1,710,000.00 USD | 27,480.00 USD | 81,410.00 USD | 25,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1780` | 4,230,000.00 USD | 4,230,000.00 USD | 52,730.00 USD | 38,910.00 USD | 97,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1782` | 1,830,000.00 USD | 1,830,000.00 USD | 56,420.00 USD | 14,240.00 USD | 47,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1783` | 4,430,000.00 USD | 4,430,000.00 USD | 117,540.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1785` | 1,990,000.00 USD | 1,990,000.00 USD | 96,920.00 USD | 51,600.00 USD | 14,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1786` | 4,630,000.00 USD | 4,630,000.00 USD | 129,440.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1788` | 2,130,000.00 USD | 2,130,000.00 USD | 35,520.00 USD | 42,480.00 USD | 56,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1789` | 4,680,000.00 USD | 4,680,000.00 USD | 48,810.00 USD | 7,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1791` | 2,200,000.00 USD | 2,200,000.00 USD | 41,020.00 USD | 19,320.00 USD | 18,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1792` | 4,860,000.00 USD | 4,860,000.00 USD | 134,000.00 USD | 39,820.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1794` | 2,330,000.00 USD | 2,330,000.00 USD | 45,400.00 USD | 60,380.00 USD | 20,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1795` | 4,940,000.00 USD | 4,940,000.00 USD | 17,130.00 USD | 19,870.00 USD | 44,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1795` | 156.94 USD | 495.99 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1797` | 2,430,000.00 USD | 2,430,000.00 USD | 41,960.00 USD | 22,110.00 USD | 36,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1798` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 6,240.00 USD | 27,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1800` | 2,480,000.00 USD | 2,480,000.00 USD | 10,230.00 USD | 8,690.00 USD | 25,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1801` | 5,070,000.00 USD | 5,070,000.00 USD | 6,490.00 USD | 40,090.00 USD | 46,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1803` | 2,560,000.00 USD | 2,560,000.00 USD | 16,490.00 USD | 35,880.00 USD | 28,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1804` | 5,140,000.00 USD | 5,140,000.00 USD | 28,790.00 USD | 27,450.00 USD | 14,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1805` | 10,970.00 USD | 11,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1806` | 2,610,000.00 USD | 2,610,000.00 USD | 21,330.00 USD | 14,370.00 USD | 21,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1807` | 5,280,000.00 USD | 5,280,000.00 USD | 11,410.00 USD | 63,170.00 USD | 67,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1809` | 2,700,000.00 USD | 2,700,000.00 USD | 27,060.00 USD | 27,370.00 USD | 32,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1810` | 5,400,000.00 USD | 5,400,000.00 USD | 79,380.00 USD | 30,940.00 USD | 12,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1812` | 2,840,000.00 USD | 2,840,000.00 USD | 56,360.00 USD | 44,030.00 USD | 38,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1813` | 5,510,000.00 USD | 5,510,000.00 USD | 32,530.00 USD | 15,780.00 USD | 56,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1815` | 2,870,000.00 USD | 2,870,000.00 USD | 12,800.00 USD | 3,320.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1815` | 9,530.00 USD | 21,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1816` | 5,600,000.00 USD | 5,600,000.00 USD | 46,430.00 USD | 21,200.00 USD | 25,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1818` | 2,950,000.00 USD | 2,950,000.00 USD | 37,120.00 USD | 11,780.00 USD | 32,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1819` | 5,730,000.00 USD | 5,730,000.00 USD | 65,350.00 USD | 24,720.00 USD | 43,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1821` | 3,000,000.00 USD | 3,000,000.00 USD | 21,220.00 USD | 19,510.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1822` | 5,910,000.00 USD | 5,910,000.00 USD | 46,760.00 USD | 36,230.00 USD | 92,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1824` | 3,050,000.00 USD | 3,050,000.00 USD | 20,050.00 USD | 18,270.00 USD | 13,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1825` | 6,000,000.00 USD | 6,000,000.00 USD | 61,720.00 USD | 17,120.00 USD | 12,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1825` | 185.09 USD | 21,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1827` | 3,080,000.00 USD | 3,080,000.00 USD | 21,440.00 USD | 6,860.00 USD | 4,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1828` | 6,150,000.00 USD | 6,150,000.00 USD | 51,470.00 USD | 24,320.00 USD | 69,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1830` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 5,730.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1831` | 6,320,000.00 USD | 6,320,000.00 USD | 85,970.00 USD | 21,930.00 USD | 63,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1833` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 4,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1834` | 6,580,000.00 USD | 6,580,000.00 USD | 165,640.00 USD | 47,980.00 USD | 51,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1835` | 49,830.00 USD | 71,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1836` | 3,110,000.00 USD | 3,110,000.00 USD | 3,610.00 USD | 0.00 USD | 728.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1837` | 6,810,000.00 USD | 6,810,000.00 USD | 72,930.00 USD | 76,140.00 USD | 83,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1839` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 2,640.00 USD | 7,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1840` | 7,040,000.00 USD | 7,040,000.00 USD | 98,270.00 USD | 47,250.00 USD | 80,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1842` | 3,140,000.00 USD | 3,140,000.00 USD | 13,150.00 USD | 3,670.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1843` | 7,250,000.00 USD | 7,250,000.00 USD | 86,180.00 USD | 18,570.00 USD | 105,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1845` | 3,170,000.00 USD | 3,170,000.00 USD | 5,640.00 USD | 6,730.00 USD | 17,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1846` | 7,440,000.00 USD | 7,440,000.00 USD | 8,330.00 USD | 45,450.00 USD | 135,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1848` | 3,190,000.00 USD | 3,190,000.00 USD | 4,680.00 USD | 5,780.00 USD | 9,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1849` | 7,620,000.00 USD | 7,620,000.00 USD | 62,030.00 USD | 79,580.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1851` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 1,730.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1852` | 8,020,000.00 USD | 8,020,000.00 USD | 153,970.00 USD | 9,590.00 USD | 234,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1854` | 3,210,000.00 USD | 3,210,000.00 USD | 1,510.00 USD | 1,690.00 USD | 11,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1855` | 8,180,000.00 USD | 8,180,000.00 USD | 58,210.00 USD | 10,160.00 USD | 94,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1857` | 3,220,000.00 USD | 3,220,000.00 USD | 7,260.00 USD | 2,630.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1858` | 8,440,000.00 USD | 8,440,000.00 USD | 96,280.00 USD | 46,830.00 USD | 118,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1860` | 3,240,000.00 USD | 3,240,000.00 USD | 9,450.00 USD | 4,440.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1861` | 8,620,000.00 USD | 8,620,000.00 USD | 99,880.00 USD | 55,030.00 USD | 21,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1863` | 3,250,000.00 USD | 3,250,000.00 USD | 1,870.00 USD | 0.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1864` | 8,790,000.00 USD | 8,790,000.00 USD | 52,190.00 USD | 58,680.00 USD | 61,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1866` | 3,260,000.00 USD | 3,260,000.00 USD | 3,300.00 USD | 0.00 USD | 5,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1867` | 9,020,000.00 USD | 9,020,000.00 USD | 130,970.00 USD | 47,840.00 USD | 52,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1869` | 3,270,000.00 USD | 3,270,000.00 USD | 4,960.00 USD | 1,740.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1870` | 9,380,000.00 USD | 9,380,000.00 USD | 175,600.00 USD | 83,890.00 USD | 101,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1872` | 3,290,000.00 USD | 3,290,000.00 USD | 9,350.00 USD | 3,300.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1873` | 9,650,000.00 USD | 9,650,000.00 USD | 72,410.00 USD | 105,600.00 USD | 90,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1875` | 3,300,000.00 USD | 3,300,000.00 USD | 1,960.00 USD | 2,820.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1875` | 21,190.00 USD | 92,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1876` | 9,780,000.00 USD | 9,780,000.00 USD | 76,050.00 USD | 41,870.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1878` | 3,310,000.00 USD | 3,310,000.00 USD | 4,320.00 USD | 2,760.00 USD | 4,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1879` | 9,940,000.00 USD | 9,940,000.00 USD | 57,250.00 USD | 52,690.00 USD | 48,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1881` | 3,330,000.00 USD | 3,330,000.00 USD | 5,810.00 USD | 8,110.00 USD | 5,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1882` | 10,040,000.00 USD | 10,040,000.00 USD | 14,000.00 USD | 23,830.00 USD | 59,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1884` | 3,340,000.00 USD | 3,340,000.00 USD | 5,750.00 USD | 0.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1885` | 10,090,000.00 USD | 10,090,000.00 USD | 19,810.00 USD | 31,900.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1885` | 477.23 USD | 92,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1887` | 3,360,000.00 USD | 3,360,000.00 USD | 13,270.00 USD | 4,390.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1888` | 10,210,000.00 USD | 10,210,000.00 USD | 13,720.00 USD | 17,330.00 USD | 83,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1890` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 7,790.00 USD | 7,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1891` | 10,260,000.00 USD | 10,260,000.00 USD | 36,740.00 USD | 0.00 USD | 17,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1893` | 3,380,000.00 USD | 3,380,000.00 USD | 5,950.00 USD | 3,490.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1894` | 10,360,000.00 USD | 10,360,000.00 USD | 69,540.00 USD | 12,420.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1896` | 3,390,000.00 USD | 3,390,000.00 USD | 4,500.00 USD | 2,500.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1897` | 10,450,000.00 USD | 10,450,000.00 USD | 25,640.00 USD | 39,120.00 USD | 25,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1899` | 3,420,000.00 USD | 3,420,000.00 USD | 7,270.00 USD | 19,270.00 USD | 3,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1900` | 10,500,000.00 USD | 10,500,000.00 USD | 11,530.00 USD | 21,370.00 USD | 14,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1902` | 3,440,000.00 USD | 3,440,000.00 USD | 6,890.00 USD | 3,410.00 USD | 6,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1903` | 10,530,000.00 USD | 10,530,000.00 USD | 14,330.00 USD | 11,220.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1905` | 3,460,000.00 USD | 3,460,000.00 USD | 2,490.00 USD | 8,320.00 USD | 7,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1906` | 10,610,000.00 USD | 10,610,000.00 USD | 18,470.00 USD | 27,580.00 USD | 33,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1908` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 2,970.00 USD | 4,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1909` | 10,680,000.00 USD | 10,680,000.00 USD | 15,470.00 USD | 29,160.00 USD | 19,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1911` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 1,050.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1912` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 15,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1914` | 3,490,000.00 USD | 3,490,000.00 USD | 11,740.00 USD | 2,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1915` | 10,700,000.00 USD | 10,700,000.00 USD | 7,460.00 USD | 5,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1917` | 3,510,000.00 USD | 3,510,000.00 USD | 5,390.00 USD | 16,330.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1918` | 10,730,000.00 USD | 10,730,000.00 USD | 0.00 USD | 11,840.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1920` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 2,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1923` | 3,540,000.00 USD | 3,540,000.00 USD | 13,780.00 USD | 2,030.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1924` | 10,750,000.00 USD | 10,750,000.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1926` | 3,550,000.00 USD | 3,550,000.00 USD | 6,860.00 USD | 5,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1927` | 10,770,000.00 USD | 10,770,000.00 USD | 11,600.00 USD | 13,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1929` | 3,560,000.00 USD | 3,560,000.00 USD | 3,390.00 USD | 1,930.00 USD | 4,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1932` | 3,560,000.00 USD | 3,560,000.00 USD | 4,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1938` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 1,150.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1945` | 10,780,000.00 USD | 10,780,000.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1945` | 4,270.00 USD | 96,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `7D` | `0.1461` | 10,840,000.00 USD | 0.00 USD | 10,840,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD |
| `7D` | `0.1464` | 10,830,000.00 USD | 0.00 USD | 10,830,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD |
| `7D` | `0.1467` | 10,830,000.00 USD | 0.00 USD | 10,830,000.00 USD | 9,720.00 USD | 9,180.00 USD | 4,840.00 USD |
| `7D` | `0.1470` | 10,810,000.00 USD | 0.00 USD | 10,810,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD |
| `7D` | `0.1473` | 10,800,000.00 USD | 0.00 USD | 10,800,000.00 USD | 6,490.00 USD | 5,400.00 USD | 5,280.00 USD |
| `7D` | `0.1476` | 10,780,000.00 USD | 0.00 USD | 10,780,000.00 USD | 0.00 USD | 14,780.00 USD | 5,320.00 USD |
| `7D` | `0.1479` | 10,760,000.00 USD | 0.00 USD | 10,760,000.00 USD | 0.00 USD | 39,730.00 USD | 14,560.00 USD |
| `7D` | `0.1482` | 10,700,000.00 USD | 0.00 USD | 10,700,000.00 USD | 41,960.00 USD | 20,720.00 USD | 27,030.00 USD |
| `7D` | `0.1485` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 16,180.00 USD | 7,340.00 USD | 38,270.00 USD |
| `7D` | `0.1488` | 10,550,000.00 USD | 0.00 USD | 10,550,000.00 USD | 20,860.00 USD | 3,130.00 USD | 10,390.00 USD |
| `7D` | `0.1491` | 10,520,000.00 USD | 0.00 USD | 10,520,000.00 USD | 33,540.00 USD | 17,020.00 USD | 20,270.00 USD |
| `7D` | `0.1494` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 34,220.00 USD | 9,890.00 USD | 14,210.00 USD |
| `7D` | `0.1497` | 10,390,000.00 USD | 0.00 USD | 10,390,000.00 USD | 20,880.00 USD | 17,180.00 USD | 9,710.00 USD |
| `7D` | `0.1500` | 10,340,000.00 USD | 0.00 USD | 10,340,000.00 USD | 46,820.00 USD | 5,810.00 USD | 21,940.00 USD |
| `7D` | `0.1503` | 10,270,000.00 USD | 0.00 USD | 10,270,000.00 USD | 11,490.00 USD | 13,450.00 USD | 9,950.00 USD |
| `7D` | `0.1506` | 10,230,000.00 USD | 0.00 USD | 10,230,000.00 USD | 33,170.00 USD | 18,020.00 USD | 65,400.00 USD |
| `1D` | `0.1509` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 11,070.00 USD | 5,020.00 USD | 3,750.00 USD |
| `7D` | `0.1509` | 10,120,000.00 USD | 0.00 USD | 10,120,000.00 USD | 17,340.00 USD | 9,550.00 USD | 24,150.00 USD |
| `1D` | `0.1512` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 0.00 USD | 4,360.00 USD | 2,500.00 USD |
| `7D` | `0.1512` | 10,060,000.00 USD | 0.00 USD | 10,060,000.00 USD | 18,600.00 USD | 8,620.00 USD | 26,910.00 USD |
| `1D` | `0.1515` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 0.00 USD | 1,730.00 USD | 1,300.00 USD |
| `7D` | `0.1515` | 10,010,000.00 USD | 0.00 USD | 10,010,000.00 USD | 53,430.00 USD | 13,330.00 USD | 53,490.00 USD |
| `1D` | `0.1518` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 8,770.00 USD | 4,320.00 USD | 7,420.00 USD |
| `7D` | `0.1518` | 9,890,000.00 USD | 0.00 USD | 9,890,000.00 USD | 46,830.00 USD | 15,160.00 USD | 64,360.00 USD |
| `1D` | `0.1521` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 9,450.00 USD | 1,470.00 USD | 5,910.00 USD |
| `7D` | `0.1521` | 9,760,000.00 USD | 0.00 USD | 9,760,000.00 USD | 38,960.00 USD | 6,920.00 USD | 38,800.00 USD |
| `1D` | `0.1524` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 1,870.00 USD | 2,970.00 USD | 7,150.00 USD |
| `7D` | `0.1524` | 9,680,000.00 USD | 0.00 USD | 9,680,000.00 USD | 37,550.00 USD | 13,950.00 USD | 11,280.00 USD |
| `1D` | `0.1527` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 3,300.00 USD | 0.00 USD | 11,570.00 USD |
| `7D` | `0.1527` | 9,620,000.00 USD | 0.00 USD | 9,620,000.00 USD | 56,950.00 USD | 30,410.00 USD | 33,080.00 USD |
| `1D` | `0.1530` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 4,960.00 USD | 5,040.00 USD | 8,740.00 USD |
| `7D` | `0.1530` | 9,500,000.00 USD | 0.00 USD | 9,500,000.00 USD | 54,790.00 USD | 9,880.00 USD | 16,070.00 USD |
| `1D` | `0.1533` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 14,310.00 USD | 1,900.00 USD | 3,140.00 USD |
| `7D` | `0.1533` | 9,420,000.00 USD | 0.00 USD | 9,420,000.00 USD | 10,760.00 USD | 16,570.00 USD | 21,560.00 USD |
| `1D` | `0.1536` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 4,320.00 USD | 5,590.00 USD | 6,380.00 USD |
| `7D` | `0.1536` | 9,370,000.00 USD | 0.00 USD | 9,370,000.00 USD | 37,160.00 USD | 2,910.00 USD | 13,450.00 USD |
| `1D` | `0.1539` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 5,810.00 USD | 8,110.00 USD | 5,200.00 USD |
| `7D` | `0.1539` | 9,310,000.00 USD | 0.00 USD | 9,310,000.00 USD | 22,990.00 USD | 18,230.00 USD | 5,070.00 USD |
| `1D` | `0.1542` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 5,750.00 USD | 0.00 USD | 4,490.00 USD |
| `7D` | `0.1542` | 9,270,000.00 USD | 0.00 USD | 9,270,000.00 USD | 0.00 USD | 3,590.00 USD | 4,670.00 USD |
| `1D` | `0.1545` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 13,270.00 USD | 5,370.00 USD | 9,370.00 USD |
| `7D` | `0.1545` | 9,260,000.00 USD | 0.00 USD | 9,260,000.00 USD | 9,250.00 USD | 0.00 USD | 5,620.00 USD |
| `1D` | `0.1548` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 1,140.00 USD | 8,660.00 USD | 1,070.00 USD |
| `7D` | `0.1548` | 9,240,000.00 USD | 0.00 USD | 9,240,000.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD |
| `1D` | `0.1551` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 4,810.00 USD | 4,140.00 USD | 3,890.00 USD |
| `7D` | `0.1551` | 9,240,000.00 USD | 0.00 USD | 9,240,000.00 USD | 34,670.00 USD | 11,820.00 USD | 0.00 USD |
| `1D` | `0.1554` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 18,660.00 USD | 19,270.00 USD | 7,190.00 USD |
| `7D` | `0.1554` | 9,190,000.00 USD | 0.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 6,470.00 USD |
| `1D` | `0.1557` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 0.00 USD | 3,410.00 USD | 3,250.00 USD |
| `7D` | `0.1557` | 9,190,000.00 USD | 0.00 USD | 9,190,000.00 USD | 0.00 USD | 4,510.00 USD | 10,800.00 USD |
| `1D` | `0.1560` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 5,460.00 USD | 11,300.00 USD | 7,790.00 USD |
| `7D` | `0.1560` | 9,170,000.00 USD | 0.00 USD | 9,170,000.00 USD | 0.00 USD | 6,480.00 USD | 0.00 USD |
| `1D` | `0.1563` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 3,050.00 USD | 1,050.00 USD | 20,290.00 USD |
| `7D` | `0.1563` | 9,170,000.00 USD | 0.00 USD | 9,170,000.00 USD | 0.00 USD | 19,950.00 USD | 9,840.00 USD |
| `1D` | `0.1566` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 45,560.00 USD | 11,570.00 USD | 15,060.00 USD |
| `7D` | `0.1566` | 9,140,000.00 USD | 0.00 USD | 9,140,000.00 USD | 50,480.00 USD | 29,160.00 USD | 26,780.00 USD |
| `1D` | `0.1569` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 24,600.00 USD | 31,270.00 USD | 7,030.00 USD |
| `7D` | `0.1569` | 9,030,000.00 USD | 0.00 USD | 9,030,000.00 USD | 15,590.00 USD | 5,100.00 USD | 11,900.00 USD |
| `1D` | `0.1572` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 34,670.00 USD | 14,240.00 USD | 17,830.00 USD |
| `7D` | `0.1572` | 9,000,000.00 USD | 0.00 USD | 9,000,000.00 USD | 40,760.00 USD | 34,450.00 USD | 17,760.00 USD |
| `1D` | `0.1575` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 34,430.00 USD | 19,170.00 USD | 6,610.00 USD |
| `7D` | `0.1575` | 8,900,000.00 USD | 0.00 USD | 8,900,000.00 USD | 23,310.00 USD | 88,960.00 USD | 21,360.00 USD |
| `1D` | `0.1578` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 62,820.00 USD | 64,050.00 USD | 24,570.00 USD |
| `7D` | `0.1578` | 8,770,000.00 USD | 0.00 USD | 8,770,000.00 USD | 58,590.00 USD | 84,670.00 USD | 67,670.00 USD |
| `1D` | `0.1581` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 31,970.00 USD | 3,940.00 USD | 22,540.00 USD |
| `7D` | `0.1581` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 92,720.00 USD | 58,880.00 USD | 57,600.00 USD |
| `1D` | `0.1584` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 34,630.00 USD | 11,050.00 USD | 13,920.00 USD |
| `7D` | `0.1584` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 80,450.00 USD | 35,780.00 USD | 123,970.00 USD |
| `1D` | `0.1587` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 6,650.00 USD | 21,380.00 USD | 12,960.00 USD |
| `7D` | `0.1587` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 69,180.00 USD | 22,370.00 USD | 31,060.00 USD |
| `1D` | `0.1590` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 13,490.00 USD | 27,950.00 USD | 8,270.00 USD |
| `7D` | `0.1590` | 7,990,000.00 USD | 0.00 USD | 7,990,000.00 USD | 71,200.00 USD | 44,110.00 USD | 51,290.00 USD |
| `1D` | `0.1593` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 47,380.00 USD | 6,320.00 USD | 23,650.00 USD |
| `7D` | `0.1593` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 69,430.00 USD | 56,020.00 USD | 68,480.00 USD |
| `1D` | `0.1596` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 29,470.00 USD | 19,190.00 USD | 35,060.00 USD |
| `7D` | `0.1596` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 161,460.00 USD | 85,250.00 USD | 120,230.00 USD |
| `1D` | `0.1599` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 69,610.00 USD | 16,990.00 USD | 33,120.00 USD |
| `7D` | `0.1599` | 7,260,000.00 USD | 0.00 USD | 7,260,000.00 USD | 219,060.00 USD | 55,380.00 USD | 87,990.00 USD |
| `1D` | `0.1602` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 55,540.00 USD | 46,820.00 USD | 7,880.00 USD |
| `7D` | `0.1602` | 6,900,000.00 USD | 0.00 USD | 6,900,000.00 USD | 44,770.00 USD | 46,490.00 USD | 40,380.00 USD |
| `1D` | `0.1605` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 34,500.00 USD | 18,980.00 USD | 37,670.00 USD |
| `7D` | `0.1605` | 6,770,000.00 USD | 0.00 USD | 6,770,000.00 USD | 177,720.00 USD | 136,660.00 USD | 217,140.00 USD |
| `1D` | `0.1608` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 66,600.00 USD | 38,390.00 USD | 21,260.00 USD |
| `7D` | `0.1608` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 129,610.00 USD | 174,940.00 USD | 131,300.00 USD |
| `1D` | `0.1611` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 135,640.00 USD | 130,060.00 USD | 55,320.00 USD |
| `7D` | `0.1611` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 148,170.00 USD | 227,820.00 USD | 233,470.00 USD |
| `1D` | `0.1614` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 55,510.00 USD | 23,510.00 USD | 53,590.00 USD |
| `7D` | `0.1614` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 330,910.00 USD | 194,680.00 USD | 282,150.00 USD |
| `1D` | `0.1617` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 73,170.00 USD | 27,450.00 USD | 23,560.00 USD |
| `7D` | `0.1617` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 346,150.00 USD | 101,810.00 USD | 410,900.00 USD |
| `1D` | `0.1620` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 42,020.00 USD | 52,870.00 USD | 60,610.00 USD |
| `7D` | `0.1620` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 282,000.00 USD | 134,660.00 USD | 271,570.00 USD |
| `1D` | `0.1623` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 53,880.00 USD | 67,020.00 USD | 26,290.00 USD |
| `7D` | `0.1623` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 304,460.00 USD | 125,080.00 USD | 208,070.00 USD |
| `1D` | `0.1626` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 15,710.00 USD | 12,640.00 USD | 25,570.00 USD |
| `7D` | `0.1626` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 234,280.00 USD | 71,120.00 USD | 0.00 USD |
| `1D` | `0.1629` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 14,220.00 USD | 33,030.00 USD | 19,620.00 USD |
| `7D` | `0.1629` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 171,310.00 USD | 0.00 USD | 20,860.00 USD |
| `1D` | `0.1632` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 12,400.00 USD | 19,630.00 USD | 17,370.00 USD |
| `7D` | `0.1632` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 9,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1635` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 37,200.00 USD | 6,390.00 USD | 11,860.00 USD |
| `7D` | `0.1635` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 0.00 USD | 13,670.00 USD | 21,360.00 USD |
| `1D` | `0.1638` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 9,410.00 USD | 22,520.00 USD | 42,790.00 USD |
| `7D` | `0.1638` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 62,410.00 USD |
| `1D` | `0.1641` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 7,360.00 USD | 6,090.00 USD | 10,340.00 USD |
| `7D` | `0.1641` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 22,480.00 USD | 29,240.00 USD | 0.00 USD |
| `1D` | `0.1644` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 25,590.00 USD | 20,340.00 USD | 27,080.00 USD |
| `7D` | `0.1644` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 0.00 USD | 8,990.00 USD | 26,230.00 USD |
| `1D` | `0.1647` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 40,030.00 USD | 32,000.00 USD | 24,030.00 USD |
| `7D` | `0.1647` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 34,760.00 USD | 0.00 USD | 7,650.00 USD |
| `1D` | `0.1650` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 12,400.00 USD | 24,600.00 USD | 5,900.00 USD |
| `7D` | `0.1650` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 7,000.00 USD | 22,660.00 USD |
| `1D` | `0.1653` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 35,120.00 USD | 13,140.00 USD | 34,610.00 USD |
| `7D` | `0.1653` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 33,810.00 USD | 12,460.00 USD | 28,440.00 USD |
| `1D` | `0.1656` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 38,480.00 USD | 51,020.00 USD | 33,300.00 USD |
| `7D` | `0.1656` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 0.00 USD | 19,330.00 USD | 33,380.00 USD |
| `1D` | `0.1659` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 43,890.00 USD | 19,240.00 USD | 58,130.00 USD |
| `7D` | `0.1659` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 40,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1662` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 20,300.00 USD | 18,480.00 USD | 64,680.00 USD |
| `7D` | `0.1662` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 48,590.00 USD | 62,020.00 USD | 81,010.00 USD |
| `1D` | `0.1665` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 64,660.00 USD | 59,180.00 USD | 67,090.00 USD |
| `7D` | `0.1665` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 87,050.00 USD | 32,780.00 USD | 57,360.00 USD |
| `1D` | `0.1668` | 980,630.00 USD | 0.00 USD | 980,630.00 USD | 111,120.00 USD | 67,630.00 USD | 37,760.00 USD |
| `7D` | `0.1668` | 896,170.00 USD | 0.00 USD | 896,170.00 USD | 11,410.00 USD | 39,630.00 USD | 42,720.00 USD |
| `1D` | `0.1671` | 764,120.00 USD | 0.00 USD | 764,120.00 USD | 46,140.00 USD | 21,810.00 USD | 24,080.00 USD |
| `7D` | `0.1671` | 802,410.00 USD | 0.00 USD | 802,410.00 USD | 70,540.00 USD | 62,490.00 USD | 0.00 USD |
| `1D` | `0.1674` | 672,090.00 USD | 0.00 USD | 672,090.00 USD | 21,310.00 USD | 46,960.00 USD | 39,840.00 USD |
| `7D` | `0.1674` | 669,380.00 USD | 0.00 USD | 669,380.00 USD | 44,960.00 USD | 88,950.00 USD | 0.00 USD |
| `1D` | `0.1677` | 563,980.00 USD | 0.00 USD | 563,980.00 USD | 14,620.00 USD | 22,480.00 USD | 0.00 USD |
| `7D` | `0.1677` | 535,470.00 USD | 0.00 USD | 535,470.00 USD | 59,010.00 USD | 64,850.00 USD | 0.00 USD |
| `1D` | `0.1680` | 526,880.00 USD | 0.00 USD | 526,880.00 USD | 75,420.00 USD | 21,620.00 USD | 31,100.00 USD |
| `7D` | `0.1680` | 411,620.00 USD | 0.00 USD | 411,620.00 USD | 101,910.00 USD | 68,430.00 USD | 15,310.00 USD |
| `1D` | `0.1683` | 398,730.00 USD | 0.00 USD | 398,730.00 USD | 88,790.00 USD | 20,110.00 USD | 28,910.00 USD |
| `7D` | `0.1683` | 225,970.00 USD | 0.00 USD | 225,970.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD |
| `1D` | `0.1686` | 260,910.00 USD | 0.00 USD | 260,910.00 USD | 0.00 USD | 23,410.00 USD | 6,460.00 USD |
| `1D` | `0.1689` | 231,040.00 USD | 0.00 USD | 231,040.00 USD | 0.00 USD | 6,980.00 USD | 8,570.00 USD |
| `7D` | `0.1689` | 151,020.00 USD | 0.00 USD | 151,020.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD |
| `1D` | `0.1692` | 215,480.00 USD | 0.00 USD | 215,480.00 USD | 55,320.00 USD | 66,160.00 USD | 0.00 USD |
| `7D` | `0.1692` | 112,350.00 USD | 0.00 USD | 112,350.00 USD | 21,780.00 USD | 32,070.00 USD | 0.00 USD |
| `1D` | `0.1695` | 94,010.00 USD | 0.00 USD | 94,010.00 USD | 7,570.00 USD | 22,300.00 USD | 0.00 USD |
| `7D` | `0.1695` | 58,500.00 USD | 0.00 USD | 58,500.00 USD | 0.00 USD | 30,490.00 USD | 28,010.00 USD |
| `1D` | `0.1698` | 64,150.00 USD | 0.00 USD | 64,150.00 USD | 7,460.00 USD | 56,690.00 USD | 0.00 USD |
| `7D` | `0.1698` | 75,680.00 USD | 75,680.00 USD | 0.00 USD | 0.00 USD | 56,860.00 USD | 18,830.00 USD |
| `7D` | `0.1698` | 151,370.00 USD | 151,370.00 USD | 0.00 USD | 0.00 USD | 56,860.00 USD | 18,830.00 USD |
| `1D` | `0.1699` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1701` | 199,520.00 USD | 199,520.00 USD | 0.00 USD | 22,820.00 USD | 25,330.00 USD | 0.00 USD |
| `1D` | `0.1704` | 24,660.00 USD | 24,660.00 USD | 0.00 USD | 0.00 USD | 14,420.00 USD | 10,240.00 USD |
| `7D` | `0.1704` | 246,400.00 USD | 246,400.00 USD | 0.00 USD | 0.00 USD | 46,880.00 USD | 0.00 USD |
| `1D` | `0.1707` | 135,430.00 USD | 135,430.00 USD | 0.00 USD | 37,960.00 USD | 68,660.00 USD | 4,150.00 USD |
| `7D` | `0.1707` | 305,920.00 USD | 305,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 59,520.00 USD |
| `7D` | `0.1710` | 336,590.00 USD | 336,590.00 USD | 0.00 USD | 0.00 USD | 25,490.00 USD | 5,180.00 USD |
| `1D` | `0.1713` | 145,560.00 USD | 145,560.00 USD | 0.00 USD | 0.00 USD | 10,130.00 USD | 0.00 USD |
| `7D` | `0.1713` | 378,610.00 USD | 378,610.00 USD | 0.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD |
| `1D` | `0.1716` | 166,600.00 USD | 166,600.00 USD | 0.00 USD | 0.00 USD | 21,040.00 USD | 0.00 USD |
| `1D` | `0.1719` | 184,470.00 USD | 184,470.00 USD | 0.00 USD | 9,350.00 USD | 8,520.00 USD | 0.00 USD |
| `1D` | `0.1722` | 260,960.00 USD | 260,960.00 USD | 0.00 USD | 63,350.00 USD | 13,140.00 USD | 0.00 USD |
| `7D` | `0.1722` | 778,630.00 USD | 778,630.00 USD | 0.00 USD | 74,150.00 USD | 0.00 USD | 325,870.00 USD |
| `1D` | `0.1725` | 276,850.00 USD | 276,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,890.00 USD |
| `1D` | `0.1728` | 283,570.00 USD | 283,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,720.00 USD |
| `7D` | `0.1731` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 493,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1734` | 293,640.00 USD | 293,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,060.00 USD |
| `1D` | `0.1737` | 332,700.00 USD | 332,700.00 USD | 0.00 USD | 29,560.00 USD | 9,510.00 USD | 0.00 USD |
| `7D` | `0.1737` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 52,610.00 USD |
| `1D` | `0.1740` | 342,340.00 USD | 342,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,640.00 USD |
| `7D` | `0.1740` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,200.00 USD |
| `1D` | `0.1743` | 352,310.00 USD | 352,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,960.00 USD |
| `7D` | `0.1743` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1746` | 370,340.00 USD | 370,340.00 USD | 0.00 USD | 8,530.00 USD | 0.00 USD | 9,500.00 USD |
| `1D` | `0.1749` | 486,760.00 USD | 486,760.00 USD | 0.00 USD | 80,070.00 USD | 0.00 USD | 36,350.00 USD |
| `7D` | `0.1749` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `0.1752` | 532,450.00 USD | 532,450.00 USD | 0.00 USD | 13,050.00 USD | 0.00 USD | 32,640.00 USD |
| `7D` | `0.1752` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 263,630.00 USD |
| `1D` | `0.1755` | 579,570.00 USD | 579,570.00 USD | 0.00 USD | 9,790.00 USD | 14,790.00 USD | 22,550.00 USD |
| `7D` | `0.1755` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 37,610.00 USD | 0.00 USD | 169,120.00 USD |
| `1D` | `0.1758` | 720,920.00 USD | 720,920.00 USD | 0.00 USD | 73,290.00 USD | 31,940.00 USD | 36,120.00 USD |
| `7D` | `0.1758` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 173,440.00 USD | 38,670.00 USD | 8,600.00 USD |
| `1D` | `0.1761` | 911,570.00 USD | 911,570.00 USD | 0.00 USD | 53,970.00 USD | 88,390.00 USD | 48,290.00 USD |
| `7D` | `0.1761` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 373,120.00 USD | 131,090.00 USD | 32,350.00 USD |
| `1D` | `0.1764` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 68,490.00 USD | 25,840.00 USD | 61,480.00 USD |
| `7D` | `0.1764` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 144,160.00 USD | 215,620.00 USD | 40,340.00 USD |
| `1D` | `0.1767` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 39,860.00 USD | 52,820.00 USD | 52,230.00 USD |
| `7D` | `0.1767` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 176,410.00 USD | 152,530.00 USD | 8,530.00 USD |
| `1D` | `0.1770` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 36,140.00 USD | 47,810.00 USD | 38,500.00 USD |
| `7D` | `0.1770` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 61,490.00 USD | 147,940.00 USD | 44,400.00 USD |
| `1D` | `0.1773` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 30,810.00 USD | 28,980.00 USD | 22,840.00 USD |
| `7D` | `0.1773` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 103,820.00 USD | 105,810.00 USD | 0.00 USD |
| `1D` | `0.1776` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 85,560.00 USD | 19,390.00 USD | 21,010.00 USD |
| `7D` | `0.1776` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 135,140.00 USD | 69,570.00 USD | 0.00 USD |
| `1D` | `0.1779` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 27,480.00 USD | 81,410.00 USD | 25,130.00 USD |
| `7D` | `0.1779` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 52,730.00 USD | 46,410.00 USD | 131,820.00 USD |
| `1D` | `0.1782` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 56,420.00 USD | 14,240.00 USD | 47,040.00 USD |
| `7D` | `0.1782` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 20,690.00 USD | 13,990.00 USD | 31,180.00 USD |
| `1D` | `0.1785` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 96,920.00 USD | 51,600.00 USD | 14,990.00 USD |
| `7D` | `0.1785` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 153,160.00 USD | 78,850.00 USD | 16,420.00 USD |
| `1D` | `0.1788` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 35,520.00 USD | 42,480.00 USD | 56,030.00 USD |
| `7D` | `0.1788` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 73,130.00 USD | 18,250.00 USD | 14,040.00 USD |
| `1D` | `0.1791` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 41,020.00 USD | 19,320.00 USD | 18,080.00 USD |
| `7D` | `0.1791` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 155,720.00 USD | 17,360.00 USD | 3,940.00 USD |
| `1D` | `0.1794` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 45,400.00 USD | 60,380.00 USD | 20,780.00 USD |
| `7D` | `0.1794` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 27,100.00 USD | 42,780.00 USD | 36,780.00 USD |
| `1D` | `0.1797` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 41,960.00 USD | 22,110.00 USD | 36,970.00 USD |
| `7D` | `0.1797` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 17,130.00 USD | 12,930.00 USD | 7,670.00 USD |
| `1D` | `0.1800` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 10,230.00 USD | 8,690.00 USD | 25,360.00 USD |
| `7D` | `0.1800` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 34,680.00 USD | 64,620.00 USD |
| `1D` | `0.1803` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 16,490.00 USD | 35,880.00 USD | 28,690.00 USD |
| `7D` | `0.1803` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 35,280.00 USD | 25,700.00 USD | 18,250.00 USD |
| `1D` | `0.1806` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 21,330.00 USD | 14,370.00 USD | 21,090.00 USD |
| `7D` | `0.1806` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 11,410.00 USD | 56,850.00 USD | 19,880.00 USD |
| `1D` | `0.1809` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 27,060.00 USD | 27,370.00 USD | 32,600.00 USD |
| `7D` | `0.1809` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 53,670.00 USD | 30,810.00 USD | 58,890.00 USD |
| `1D` | `0.1812` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 56,360.00 USD | 44,030.00 USD | 38,190.00 USD |
| `7D` | `0.1812` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 34,960.00 USD | 16,640.00 USD | 50,510.00 USD |
| `1D` | `0.1815` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 12,800.00 USD | 3,320.00 USD | 11,550.00 USD |
| `7D` | `0.1815` | 5,700,000.00 USD | 5,700,000.00 USD | 0.00 USD | 60,010.00 USD | 30,810.00 USD | 38,270.00 USD |
| `1D` | `0.1818` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 37,120.00 USD | 11,780.00 USD | 32,620.00 USD |
| `7D` | `0.1818` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 75,040.00 USD | 24,140.00 USD | 10,390.00 USD |
| `1D` | `0.1821` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 21,220.00 USD | 19,510.00 USD | 9,370.00 USD |
| `7D` | `0.1821` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 40,950.00 USD | 33,870.00 USD | 41,820.00 USD |
| `1D` | `0.1824` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 20,050.00 USD | 18,270.00 USD | 13,610.00 USD |
| `7D` | `0.1824` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 39,400.00 USD | 17,880.00 USD | 95,310.00 USD |
| `1D` | `0.1827` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 21,440.00 USD | 6,860.00 USD | 4,170.00 USD |
| `7D` | `0.1827` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 79,610.00 USD | 18,690.00 USD | 65,670.00 USD |
| `1D` | `0.1830` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 4,510.00 USD | 5,690.00 USD |
| `7D` | `0.1830` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 64,890.00 USD | 20,550.00 USD | 52,010.00 USD |
| `1D` | `0.1833` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,630.00 USD |
| `7D` | `0.1833` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 186,730.00 USD | 49,740.00 USD | 26,350.00 USD |
| `1D` | `0.1836` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 3,610.00 USD | 0.00 USD | 728.16 USD |
| `7D` | `0.1836` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 29,580.00 USD | 83,110.00 USD | 52,650.00 USD |
| `1D` | `0.1839` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 2,640.00 USD | 7,830.00 USD |
| `7D` | `0.1839` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 129,950.00 USD | 41,230.00 USD | 114,190.00 USD |
| `1D` | `0.1842` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 13,150.00 USD | 2,690.00 USD | 5,850.00 USD |
| `7D` | `0.1842` | 7,290,000.00 USD | 7,290,000.00 USD | 0.00 USD | 71,550.00 USD | 26,100.00 USD | 97,700.00 USD |
| `1D` | `0.1845` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 5,640.00 USD | 6,730.00 USD | 17,180.00 USD |
| `7D` | `0.1845` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 34,630.00 USD | 33,340.00 USD | 66,720.00 USD |
| `1D` | `0.1848` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 4,680.00 USD | 4,360.00 USD | 9,340.00 USD |
| `7D` | `0.1848` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 47,730.00 USD | 75,080.00 USD | 135,290.00 USD |
| `1D` | `0.1851` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD | 1,300.00 USD |
| `7D` | `0.1851` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 94,780.00 USD | 28,290.00 USD | 220,580.00 USD |
| `1D` | `0.1854` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 1,510.00 USD | 1,690.00 USD | 11,860.00 USD |
| `7D` | `0.1854` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 105,210.00 USD | 4,290.00 USD | 63,060.00 USD |
| `1D` | `0.1857` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 7,260.00 USD | 2,630.00 USD | 3,670.00 USD |
| `7D` | `0.1857` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 116,320.00 USD | 32,070.00 USD | 127,480.00 USD |
| `1D` | `0.1860` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 9,450.00 USD | 4,440.00 USD | 4,330.00 USD |
| `7D` | `0.1860` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 87,180.00 USD | 72,430.00 USD | 74,870.00 USD |
| `1D` | `0.1863` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD | 8,320.00 USD |
| `7D` | `0.1863` | 8,900,000.00 USD | 8,900,000.00 USD | 0.00 USD | 71,330.00 USD | 56,440.00 USD | 61,380.00 USD |
| `1D` | `0.1866` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 3,300.00 USD | 0.00 USD | 5,140.00 USD |
| `7D` | `0.1866` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 101,070.00 USD | 33,740.00 USD | 39,240.00 USD |
| `1D` | `0.1869` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 4,960.00 USD | 1,740.00 USD | 9,730.00 USD |
| `7D` | `0.1869` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 169,650.00 USD | 66,330.00 USD | 78,120.00 USD |
| `1D` | `0.1872` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 12,350.00 USD | 5,200.00 USD | 5,320.00 USD |
| `7D` | `0.1872` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 80,790.00 USD | 132,480.00 USD | 93,980.00 USD |
| `1D` | `0.1875` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 1,960.00 USD | 2,820.00 USD | 2,290.00 USD |
| `7D` | `0.1875` | 9,840,000.00 USD | 9,840,000.00 USD | 0.00 USD | 68,250.00 USD | 42,310.00 USD | 36,560.00 USD |
| `1D` | `0.1878` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 4,320.00 USD | 2,760.00 USD | 4,090.00 USD |
| `7D` | `0.1878` | 9,990,000.00 USD | 9,990,000.00 USD | 0.00 USD | 66,470.00 USD | 37,330.00 USD | 48,000.00 USD |
| `1D` | `0.1881` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 5,810.00 USD | 8,110.00 USD | 5,200.00 USD |
| `7D` | `0.1881` | 10,080,000.00 USD | 10,080,000.00 USD | 0.00 USD | 29,820.00 USD | 44,080.00 USD | 13,200.00 USD |
| `1D` | `0.1884` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 5,750.00 USD | 0.00 USD | 4,490.00 USD |
| `7D` | `0.1884` | 10,190,000.00 USD | 10,190,000.00 USD | 0.00 USD | 10,560.00 USD | 36,820.00 USD | 58,860.00 USD |
| `1D` | `0.1887` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 13,270.00 USD | 4,390.00 USD | 1,730.00 USD |
| `7D` | `0.1887` | 10,230,000.00 USD | 10,230,000.00 USD | 0.00 USD | 22,970.00 USD | 0.00 USD | 25,760.00 USD |
| `1D` | `0.1890` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 7,790.00 USD | 7,640.00 USD |
| `7D` | `0.1890` | 10,360,000.00 USD | 10,360,000.00 USD | 0.00 USD | 36,740.00 USD | 17,330.00 USD | 75,130.00 USD |
| `1D` | `0.1893` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 5,950.00 USD | 3,490.00 USD | 1,070.00 USD |
| `7D` | `0.1893` | 10,420,000.00 USD | 10,420,000.00 USD | 0.00 USD | 32,450.00 USD | 6,940.00 USD | 16,820.00 USD |
| `1D` | `0.1896` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 4,500.00 USD | 2,500.00 USD | 3,890.00 USD |
| `7D` | `0.1896` | 10,530,000.00 USD | 10,530,000.00 USD | 0.00 USD | 62,730.00 USD | 27,440.00 USD | 18,680.00 USD |
| `1D` | `0.1899` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 7,270.00 USD | 19,270.00 USD | 3,660.00 USD |
| `7D` | `0.1899` | 10,600,000.00 USD | 10,600,000.00 USD | 0.00 USD | 11,530.00 USD | 38,530.00 USD | 20,420.00 USD |
| `1D` | `0.1902` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 6,890.00 USD | 3,410.00 USD | 6,780.00 USD |
| `7D` | `0.1902` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 14,330.00 USD | 0.00 USD | 10,800.00 USD |
| `1D` | `0.1905` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 2,490.00 USD | 8,320.00 USD | 7,790.00 USD |
| `7D` | `0.1905` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 8,720.00 USD | 24,800.00 USD | 24,210.00 USD |
| `1D` | `0.1908` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 2,970.00 USD | 4,240.00 USD |
| `7D` | `0.1908` | 10,780,000.00 USD | 10,780,000.00 USD | 0.00 USD | 25,220.00 USD | 43,160.00 USD | 28,600.00 USD |
| `1D` | `0.1911` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 1,050.00 USD | 3,180.00 USD |
| `7D` | `0.1911` | 10,790,000.00 USD | 10,790,000.00 USD | 0.00 USD | 0.00 USD | 9,380.00 USD | 0.00 USD |
| `1D` | `0.1914` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 11,740.00 USD | 2,880.00 USD | 0.00 USD |
| `7D` | `0.1914` | 10,810,000.00 USD | 10,810,000.00 USD | 0.00 USD | 7,460.00 USD | 11,160.00 USD | 0.00 USD |
| `1D` | `0.1917` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 5,390.00 USD | 16,330.00 USD | 2,290.00 USD |
| `7D` | `0.1917` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 0.00 USD | 11,840.00 USD | 11,900.00 USD |
| `1D` | `0.1920` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,740.00 USD |
| `1D` | `0.1923` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 13,780.00 USD | 2,030.00 USD | 6,410.00 USD |
| `7D` | `0.1923` | 10,850,000.00 USD | 10,850,000.00 USD | 0.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD |
| `1D` | `0.1926` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 6,860.00 USD | 5,630.00 USD | 0.00 USD |
| `7D` | `0.1926` | 10,880,000.00 USD | 10,880,000.00 USD | 0.00 USD | 11,600.00 USD | 13,630.00 USD | 0.00 USD |
| `1D` | `0.1929` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 3,390.00 USD | 1,930.00 USD | 4,000.00 USD |
| `1D` | `0.1932` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 4,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1938` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 1,150.00 USD | 2,140.00 USD |
| `7D` | `0.1944` | 10,880,000.00 USD | 10,880,000.00 USD | 0.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `209.08M` | Total OI Tokens: `1,230,413,609.4 ARB`
  * 1h OI Change: `-1.90%` | 4h OI Change: `-2.23%` | 24h OI Change: `-12.45%`
  * Exchange Breakdown: Binance=`47.95M` | Bybit=`29.20M` | OKX=`17.00M` | Hyperliquid=`15.15M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `9.42K` | Last 24h: `10.97K` | Last 3d: `22.34K` | Last 7d: `43.06K`
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
| `15M` | `ARB` | `61.26%` | `38.74%` | `1.58` | 2,510,000.00 USD |
| `15M` | `Binance` | `61.25%` | `38.75%` | `1.58` | 1,070,000.00 USD |
| `15M` | `OKX` | `60.61%` | `39.39%` | `1.54` | 492,040.00 USD |
| `15M` | `Bybit` | `70.38%` | `29.62%` | `2.38` | 224,920.00 USD |
| `15M` | `KuCoin` | `42.51%` | `57.49%` | `0.74` | 40,550.00 USD |
| `15M` | `Gate` | `66.23%` | `33.77%` | `1.96` | 56,830.00 USD |
| `15M` | `Bitget` | `54.45%` | `45.55%` | `1.20` | 121,860.00 USD |
| `15M` | `BingX` | `30.2%` | `69.8%` | `0.43` | 103,230.00 USD |
| `15M` | `MEXC` | `73.22%` | `26.78%` | `2.73` | 179,600.00 USD |
| `15M` | `Bitunix` | `56.42%` | `43.58%` | `1.29` | 39,510.00 USD |
| `15M` | `Hyperliquid` | `64.99%` | `35.01%` | `1.86` | 47,950.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `56.99%` | `43.01%` | `1.33` | 53,530.00 USD |
| `15M` | `Crypto.com` | `0.18%` | `99.82%` | `0.00` | 969.61 USD |
| `15M` | `WhiteBIT` | `69.14%` | `30.86%` | `2.24` | 72,040.00 USD |
| `15M` | `HTX` | `28.53%` | `71.47%` | `0.40` | 164.94 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `96.89%` | `3.11%` | `31.15` | 6,880.00 USD |
| `15M` | `Aster` | `53.51%` | `46.49%` | `1.15` | 235.49 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `97.47%` | `2.53%` | `38.53` | 3,950.00 USD |
| `15M` | `Whale Positions` | `61.25%` | `38.75%` | `1.58` | 1,070,000.00 USD |
| `15M` | `Global Accounts` | `61.26%` | `38.74%` | `1.58` | 2,510,000.00 USD |
| `1H` | `ARB` | `45.35%` | `54.65%` | `0.83` | 11,880,000.00 USD |
| `1H` | `Binance` | `46.49%` | `53.51%` | `0.87` | 4,880,000.00 USD |
| `1H` | `OKX` | `43.16%` | `56.84%` | `0.76` | 1,830,000.00 USD |
| `1H` | `Bybit` | `44.21%` | `55.79%` | `0.79` | 936,750.00 USD |
| `1H` | `KuCoin` | `46.68%` | `53.32%` | `0.88` | 134,650.00 USD |
| `1H` | `Gate` | `53.83%` | `46.17%` | `1.17` | 432,650.00 USD |
| `1H` | `Bitget` | `44.3%` | `55.7%` | `0.80` | 508,560.00 USD |
| `1H` | `BingX` | `15.83%` | `84.17%` | `0.19` | 663,420.00 USD |
| `1H` | `MEXC` | `45.91%` | `54.09%` | `0.85` | 1,070,000.00 USD |
| `1H` | `Bitunix` | `45.48%` | `54.52%` | `0.83` | 167,140.00 USD |
| `1H` | `Hyperliquid` | `54.56%` | `45.44%` | `1.20` | 243,480.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.62%` | `50.38%` | `0.98` | 684,090.00 USD |
| `1H` | `Crypto.com` | `76.9%` | `23.1%` | `3.33` | 6,330.00 USD |
| `1H` | `WhiteBIT` | `83.33%` | `16.67%` | `5.00` | 278,850.00 USD |
| `1H` | `HTX` | `6.02%` | `93.98%` | `0.06` | 2,320.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `42.51%` | `57.49%` | `0.74` | 23,570.00 USD |
| `1H` | `Aster` | `18.34%` | `81.66%` | `0.22` | 1,630.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `19.92%` | `80.08%` | `0.25` | 23,640.00 USD |
| `1H` | `Whale Positions` | `46.49%` | `53.51%` | `0.87` | 4,880,000.00 USD |
| `1H` | `Global Accounts` | `45.35%` | `54.65%` | `0.83` | 11,880,000.00 USD |
| `4H` | `ARB` | `47.54%` | `52.46%` | `0.91` | 60,140,000.00 USD |
| `4H` | `Binance` | `45.49%` | `54.51%` | `0.83` | 22,140,000.00 USD |
| `4H` | `OKX` | `48.28%` | `51.72%` | `0.93` | 11,810,000.00 USD |
| `4H` | `Bybit` | `49.88%` | `50.12%` | `1.00` | 4,910,000.00 USD |
| `4H` | `KuCoin` | `48.46%` | `51.54%` | `0.94` | 591,400.00 USD |
| `4H` | `Gate` | `50.6%` | `49.4%` | `1.02` | 1,540,000.00 USD |
| `4H` | `Bitget` | `49.76%` | `50.24%` | `0.99` | 3,530,000.00 USD |
| `4H` | `BingX` | `32.94%` | `67.06%` | `0.49` | 3,040,000.00 USD |
| `4H` | `MEXC` | `44.82%` | `55.18%` | `0.81` | 5,040,000.00 USD |
| `4H` | `Bitunix` | `49.07%` | `50.93%` | `0.96` | 1,350,000.00 USD |
| `4H` | `Hyperliquid` | `53.18%` | `46.82%` | `1.14` | 1,840,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.33%` | `50.67%` | `0.97` | 2,700,000.00 USD |
| `4H` | `Crypto.com` | `53.1%` | `46.9%` | `1.13` | 26,670.00 USD |
| `4H` | `WhiteBIT` | `84.86%` | `15.14%` | `5.61` | 1,290,000.00 USD |
| `4H` | `HTX` | `49.82%` | `50.18%` | `0.99` | 15,470.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `62.54%` | `37.46%` | `1.67` | 146,440.00 USD |
| `4H` | `Aster` | `88.84%` | `11.16%` | `7.96` | 64,630.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `45.74%` | `54.26%` | `0.84` | 126,610.00 USD |
| `4H` | `Whale Positions` | `45.49%` | `54.51%` | `0.83` | 22,140,000.00 USD |
| `4H` | `Global Accounts` | `47.54%` | `52.46%` | `0.91` | 60,140,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1743` | `0.1742` | `0.1743` | `0.1749` | `0.1731` | 1,329,025.77 USD | 664,234.01 USD | 664,791.75 USD | -557.74 USD | `-0.04%` | `35B / 34S` |
| `0:00 UTC` | `0.1740` | `0.1746` | `0.1740` | `0.1759` | `0.1738` | 1,727,950.91 USD | 719,456.36 USD | 1,008,494.54 USD | -289,038.18 USD | `-16.73%` | `12B / 27S` |
| `5:00 UTC` | `0.1735` | `0.1735` | `0.1735` | `0.1745` | `0.1727` | 1,465,256.89 USD | 552,173.71 USD | 913,083.17 USD | -360,909.46 USD | `-24.63%` | `12B / 58S` |
| `0:00 UTC` | `0.1724` | `0.1726` | `0.1724` | `0.1732` | `0.1721` | 813,790.61 USD | 314,421.23 USD | 499,369.38 USD | -184,948.15 USD | `-22.73%` | `12B / 32S` |
| `5:00 UTC` | `0.1722` | `0.1719` | `0.1722` | `0.1724` | `0.1714` | 868,922.61 USD | 333,299.44 USD | 535,623.17 USD | -202,323.73 USD | `-23.28%` | `11B / 37S` |
| `0:00 UTC` | `0.1715` | `0.1718` | `0.1715` | `0.1727` | `0.1712` | 1,082,802.27 USD | 363,691.86 USD | 719,110.40 USD | -355,418.54 USD | `-32.82%` | `13B / 48S` |
| `5:00 UTC` | `0.1711` | `0.1711` | `0.1711` | `0.1716` | `0.1708` | 800,876.04 USD | 410,736.84 USD | 390,139.20 USD | 20,597.64 USD | `+2.57%` | `7B / 12S` |
| `0:00 UTC` | `0.1710` | `0.1702` | `0.1710` | `0.1719` | `0.1689` | 1,300,882.78 USD | 531,501.17 USD | 769,381.61 USD | -237,880.44 USD | `-18.29%` | `17B / 38S` |
| `5:00 UTC` | `0.1689` | `0.1689` | `0.1689` | `0.1697` | `0.1682` | 1,292,914.43 USD | 712,068.28 USD | 580,846.15 USD | 131,222.13 USD | `+10.15%` | `38B / 24S` |
| `0:00 UTC` | `0.1698` | `0.1697` | `0.1698` | `0.1699` | `0.1695` | 193,614.43 USD | 100,780.49 USD | 92,833.94 USD | 7,946.55 USD | `+4.10%` | `16B / 8S` |

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
| `5m` | -12,160.00 USD | 78,960.00 USD | **`ACCUMULATION`** |
| `15m` | 160,390.00 USD | 425,120.00 USD | **`ACCUMULATION`** |
| `30m` | 17,400.00 USD | -171,050.00 USD | **`DISTRIBUTION`** |
| `1h` | -50,060.00 USD | -836,370.00 USD | **`DISTRIBUTION`** |
| `2h` | -27,500.00 USD | -1,980,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 209,790.00 USD | -2,400,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 109,390.00 USD | -3,400,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 497,000.00 USD | -4,010,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 119,300.00 USD | -4,790,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -373,880.00 USD | -7,540,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -4,560,000.00 USD | -29,220,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -31,940,000.00 USD | -163,300,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-12.16K` | 15m=`+160.39K` | 1h=`-50.06K` | 24h=`-373.88K`
* Futures Capital Netflows: 5m=`+78.96K` | 15m=`+425.12K` | 1h=`-836.37K` | 24h=`-7.54M`
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
  * `2026-10-29 23:31:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:35 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:35 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:35 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:35 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:35 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:35 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
