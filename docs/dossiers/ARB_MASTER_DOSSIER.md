# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 02:06:25 IST` (`2026-10-29 20:36:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1657` | `0.1660` | `0.1649` | `0.1652` | `1,647,744` | 272,655.07 USD | 69,287.84 USD | `+25.41%` | -4,464,954.35 USD | `+0.49` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1652` | `0.1656` | `0.1649` | `0.1650` | `1,169,148` | 193,098.43 USD | -1,020.51 USD | `-0.53%` | -4,465,974.86 USD | `-0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `0.1650` | `0.1656` | `0.1620` | `0.1621` | `10,284,180` | 1,683,375.69 USD | -461,993.20 USD | `-27.44%` | -4,927,968.06 USD | `-2.89` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1683` | `0.1684` | `0.1640` | `0.1657` | `15,315,777` | 2,535,332.38 USD | -237,581.36 USD | `-9.37%` | -4,675,846.63 USD | `-0.97` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1657` | `0.1661` | `0.1649` | `0.1650` | `4,340,197` | 718,046.47 USD | 110,593.73 USD | `+15.40%` | -4,565,252.91 USD | `+1.11` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1650` | `0.1656` | `0.1619` | `0.1620` | `10,496,048` | 1,717,698.38 USD | -462,647.73 USD | `-26.93%` | -5,027,900.64 USD | `-2.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1696` | `0.1704` | `0.1673` | `0.1687` | `18,975,463` | 3,201,824.26 USD | -35,947.57 USD | `-1.12%` | -4,720,262.78 USD | `+0.39` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1686` | `0.1693` | `0.1678` | `0.1683` | `12,478,051` | 2,101,814.57 USD | 317,188.30 USD | `+15.09%` | -4,403,074.48 USD | `+1.26` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1683` | `0.1684` | `0.1617` | `0.1618` | `30,480,959` | 5,024,298.83 USD | -633,214.10 USD | `-12.60%` | -5,036,288.58 USD | `-1.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,374,542.78 USD | `-1.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,572,000.78 USD | `-0.89` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1623` | `0.1624` | `29,043,305` | 4,791,388.29 USD | -475,713.73 USD | `-9.93%` | -4,047,714.52 USD | `+0.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1652` | `0.1687` | `0.1623` | `0.1631` | `68,085,678` | 11,252,816.65 USD | -909,329.92 USD | `-8.08%` | -705,420.63 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,136,414.44 USD | `-0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,374,542.78 USD | `-1.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,572,000.78 USD | `-0.89` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1623` | `0.1624` | `29,043,305` | 4,791,388.29 USD | -475,713.73 USD | `-9.93%` | -4,047,714.52 USD | `+0.40` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:04:34 IST` |

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
| `Live` | `Long Liquidation` | `0.1435` | 19,330.00 USD | 921,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 53,790.00 USD | 902,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 106.39 USD | 848,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 47,190.00 USD | 848,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1467` | 9,480,000.00 USD | 9,480,000.00 USD | 9,720.00 USD | 9,180.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1470` | 9,450,000.00 USD | 9,450,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1473` | 3,180,000.00 USD | 3,180,000.00 USD | 9,360.00 USD | 3,730.00 USD | 1,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1473` | 9,440,000.00 USD | 9,440,000.00 USD | 6,490.00 USD | 5,400.00 USD | 5,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1475` | 3,160,000.00 USD | 3,160,000.00 USD | 3,610.00 USD | 1,060.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 73,750.00 USD | 801,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1476` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 14,780.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1477` | 3,150,000.00 USD | 3,150,000.00 USD | 5,900.00 USD | 2,820.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1479` | 3,140,000.00 USD | 3,140,000.00 USD | 13,660.00 USD | 12,020.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1479` | 9,410,000.00 USD | 9,410,000.00 USD | 0.00 USD | 39,730.00 USD | 14,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1481` | 3,120,000.00 USD | 3,120,000.00 USD | 2,900.00 USD | 5,440.00 USD | 10,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1482` | 9,350,000.00 USD | 9,350,000.00 USD | 41,960.00 USD | 20,720.00 USD | 27,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1483` | 3,100,000.00 USD | 3,100,000.00 USD | 2,780.00 USD | 4,230.00 USD | 3,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1485` | 3,090,000.00 USD | 3,090,000.00 USD | 9,730.00 USD | 0.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1485` | 9,260,000.00 USD | 9,260,000.00 USD | 16,180.00 USD | 7,340.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,650.00 USD | 727,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1487` | 3,070,000.00 USD | 3,070,000.00 USD | 2,660.00 USD | 4,430.00 USD | 5,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1488` | 9,200,000.00 USD | 9,200,000.00 USD | 20,860.00 USD | 3,130.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1489` | 3,060,000.00 USD | 3,060,000.00 USD | 4,080.00 USD | 2,620.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1491` | 3,050,000.00 USD | 3,050,000.00 USD | 3,580.00 USD | 8,610.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1491` | 9,170,000.00 USD | 9,170,000.00 USD | 33,540.00 USD | 17,020.00 USD | 28,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1493` | 3,030,000.00 USD | 3,030,000.00 USD | 10,660.00 USD | 0.00 USD | 2,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1494` | 9,090,000.00 USD | 9,090,000.00 USD | 34,220.00 USD | 9,890.00 USD | 14,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1495` | 3,020,000.00 USD | 3,020,000.00 USD | 6,840.00 USD | 5,270.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 35,860.00 USD | 724,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1497` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 347.81 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1497` | 9,030,000.00 USD | 9,030,000.00 USD | 20,880.00 USD | 17,180.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1499` | 3,010,000.00 USD | 3,010,000.00 USD | 2,670.00 USD | 0.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1500` | 8,980,000.00 USD | 8,980,000.00 USD | 46,820.00 USD | 5,810.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1501` | 3,000,000.00 USD | 3,000,000.00 USD | 3,610.00 USD | 0.00 USD | 728.16 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1503` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 2,640.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1503` | 8,910,000.00 USD | 8,910,000.00 USD | 11,490.00 USD | 13,450.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1505` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1505` | 102,290.00 USD | 689,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1506` | 8,870,000.00 USD | 8,870,000.00 USD | 33,170.00 USD | 18,020.00 USD | 65,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1507` | 2,990,000.00 USD | 2,990,000.00 USD | 5,430.00 USD | 1,730.00 USD | 1,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1509` | 2,980,000.00 USD | 2,980,000.00 USD | 5,640.00 USD | 2,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1509` | 8,750,000.00 USD | 8,750,000.00 USD | 17,340.00 USD | 9,550.00 USD | 24,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1511` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 4,360.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1512` | 8,700,000.00 USD | 8,700,000.00 USD | 18,600.00 USD | 8,620.00 USD | 26,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1513` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 839.14 USD | 1,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1515` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 886.43 USD | 1,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1515` | 8,650,000.00 USD | 8,650,000.00 USD | 53,430.00 USD | 13,330.00 USD | 53,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 9,900.00 USD | 586,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1517` | 2,960,000.00 USD | 2,960,000.00 USD | 7,630.00 USD | 1,690.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1518` | 8,530,000.00 USD | 8,530,000.00 USD | 46,830.00 USD | 15,160.00 USD | 64,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1519` | 2,940,000.00 USD | 2,940,000.00 USD | 6,710.00 USD | 2,630.00 USD | 12,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1521` | 2,920,000.00 USD | 2,920,000.00 USD | 9,450.00 USD | 1,470.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1521` | 8,400,000.00 USD | 8,400,000.00 USD | 47,740.00 USD | 6,920.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1523` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 2,970.00 USD | 3,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1524` | 8,310,000.00 USD | 8,310,000.00 USD | 37,550.00 USD | 13,950.00 USD | 11,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1525` | 2,900,000.00 USD | 2,900,000.00 USD | 1,870.00 USD | 0.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1525` | 42,800.00 USD | 576,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1527` | 2,890,000.00 USD | 2,890,000.00 USD | 3,300.00 USD | 0.00 USD | 8,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1527` | 8,250,000.00 USD | 8,250,000.00 USD | 56,950.00 USD | 30,410.00 USD | 33,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1529` | 2,880,000.00 USD | 2,880,000.00 USD | 4,960.00 USD | 1,740.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1530` | 8,130,000.00 USD | 8,130,000.00 USD | 54,790.00 USD | 9,880.00 USD | 16,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1531` | 2,870,000.00 USD | 2,870,000.00 USD | 6,990.00 USD | 5,200.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1533` | 2,850,000.00 USD | 2,850,000.00 USD | 7,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1533` | 8,050,000.00 USD | 8,050,000.00 USD | 10,760.00 USD | 16,570.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1535` | 2,840,000.00 USD | 2,840,000.00 USD | 2,670.00 USD | 5,590.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 189,960.00 USD | 534,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1536` | 8,000,000.00 USD | 8,000,000.00 USD | 37,160.00 USD | 2,910.00 USD | 13,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1537` | 2,830,000.00 USD | 2,830,000.00 USD | 1,650.00 USD | 2,440.00 USD | 1,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1539` | 2,830,000.00 USD | 2,830,000.00 USD | 2,920.00 USD | 4,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1539` | 7,940,000.00 USD | 7,940,000.00 USD | 22,990.00 USD | 18,230.00 USD | 5,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1541` | 2,820,000.00 USD | 2,820,000.00 USD | 1,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1542` | 7,900,000.00 USD | 7,900,000.00 USD | 0.00 USD | 3,590.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1543` | 2,820,000.00 USD | 2,820,000.00 USD | 9,690.00 USD | 2,220.00 USD | 6,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1545` | 2,800,000.00 USD | 2,800,000.00 USD | 3,580.00 USD | 978.10 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1545` | 7,890,000.00 USD | 7,890,000.00 USD | 9,250.00 USD | 0.00 USD | 5,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1545` | 26,170.00 USD | 344,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1547` | 2,790,000.00 USD | 2,790,000.00 USD | 1,140.00 USD | 6,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1548` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1549` | 2,790,000.00 USD | 2,790,000.00 USD | 4,810.00 USD | 3,490.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1551` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 2,500.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1551` | 7,870,000.00 USD | 7,870,000.00 USD | 34,670.00 USD | 11,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1553` | 2,770,000.00 USD | 2,770,000.00 USD | 11,770.00 USD | 15,630.00 USD | 3,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1554` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1555` | 2,740,000.00 USD | 2,740,000.00 USD | 2,640.00 USD | 1,760.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1555` | 39,570.00 USD | 317,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1557` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 1,660.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1557` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 4,510.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1559` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 8,320.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1560` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 6,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1561` | 2,710,000.00 USD | 2,710,000.00 USD | 2,970.00 USD | 2,970.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1563` | 2,700,000.00 USD | 2,700,000.00 USD | 3,050.00 USD | 1,050.00 USD | 11,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1563` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 19,950.00 USD | 9,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1565` | 2,690,000.00 USD | 2,690,000.00 USD | 24,770.00 USD | 11,570.00 USD | 5,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1565` | 23,920.00 USD | 278,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1566` | 7,770,000.00 USD | 7,770,000.00 USD | 50,480.00 USD | 29,160.00 USD | 26,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1567` | 2,650,000.00 USD | 2,650,000.00 USD | 24,900.00 USD | 0.00 USD | 11,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1569` | 2,610,000.00 USD | 2,610,000.00 USD | 15,110.00 USD | 28,380.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1569` | 7,660,000.00 USD | 7,660,000.00 USD | 15,590.00 USD | 5,100.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1571` | 2,560,000.00 USD | 2,560,000.00 USD | 21,680.00 USD | 6,810.00 USD | 4,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1572` | 7,630,000.00 USD | 7,630,000.00 USD | 40,760.00 USD | 34,450.00 USD | 17,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1573` | 2,530,000.00 USD | 2,530,000.00 USD | 22,970.00 USD | 9,280.00 USD | 6,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1575` | 2,490,000.00 USD | 2,490,000.00 USD | 24,450.00 USD | 17,320.00 USD | 6,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1575` | 7,530,000.00 USD | 7,530,000.00 USD | 23,310.00 USD | 88,960.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1575` | 4,940.00 USD | 254,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1577` | 2,440,000.00 USD | 2,440,000.00 USD | 37,440.00 USD | 41,600.00 USD | 14,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1578` | 7,400,000.00 USD | 7,400,000.00 USD | 58,590.00 USD | 84,670.00 USD | 67,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1579` | 2,350,000.00 USD | 2,350,000.00 USD | 39,660.00 USD | 22,460.00 USD | 22,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1581` | 2,260,000.00 USD | 2,260,000.00 USD | 14,290.00 USD | 6,220.00 USD | 9,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1581` | 7,190,000.00 USD | 7,190,000.00 USD | 92,720.00 USD | 58,880.00 USD | 57,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1583` | 2,230,000.00 USD | 2,230,000.00 USD | 20,850.00 USD | 8,310.00 USD | 13,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1584` | 6,980,000.00 USD | 6,980,000.00 USD | 80,450.00 USD | 35,780.00 USD | 123,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1585` | 2,190,000.00 USD | 2,190,000.00 USD | 13,780.00 USD | 5,120.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1585` | 5,760.00 USD | 249,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1587` | 2,160,000.00 USD | 2,160,000.00 USD | 9,930.00 USD | 19,010.00 USD | 13,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1587` | 6,740,000.00 USD | 6,740,000.00 USD | 69,180.00 USD | 22,370.00 USD | 38,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1589` | 2,120,000.00 USD | 2,120,000.00 USD | 13,490.00 USD | 13,790.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1590` | 6,610,000.00 USD | 6,610,000.00 USD | 71,200.00 USD | 44,110.00 USD | 51,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1591` | 2,080,000.00 USD | 2,080,000.00 USD | 12,080.00 USD | 20,480.00 USD | 13,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1593` | 2,040,000.00 USD | 2,040,000.00 USD | 40,440.00 USD | 0.00 USD | 17,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1593` | 6,440,000.00 USD | 6,440,000.00 USD | 69,430.00 USD | 56,020.00 USD | 88,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1595` | 1,980,000.00 USD | 1,980,000.00 USD | 23,220.00 USD | 14,560.00 USD | 23,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1595` | 63,000.00 USD | 243,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1596` | 6,230,000.00 USD | 6,230,000.00 USD | 161,460.00 USD | 85,250.00 USD | 120,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1597` | 1,920,000.00 USD | 1,920,000.00 USD | 39,740.00 USD | 21,610.00 USD | 11,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1599` | 1,840,000.00 USD | 1,840,000.00 USD | 42,800.00 USD | 0.00 USD | 29,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1599` | 5,860,000.00 USD | 5,860,000.00 USD | 219,060.00 USD | 55,380.00 USD | 87,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1601` | 1,770,000.00 USD | 1,770,000.00 USD | 39,230.00 USD | 33,200.00 USD | 7,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1602` | 5,500,000.00 USD | 5,500,000.00 USD | 44,770.00 USD | 46,490.00 USD | 40,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1603` | 1,690,000.00 USD | 1,690,000.00 USD | 24,830.00 USD | 20,230.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1605` | 1,640,000.00 USD | 1,640,000.00 USD | 25,980.00 USD | 12,370.00 USD | 30,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1605` | 5,370,000.00 USD | 5,370,000.00 USD | 177,720.00 USD | 136,660.00 USD | 217,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1605` | 37,640.00 USD | 180,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1607` | 1,570,000.00 USD | 1,570,000.00 USD | 43,410.00 USD | 13,680.00 USD | 6,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1608` | 4,840,000.00 USD | 4,840,000.00 USD | 129,610.00 USD | 174,940.00 USD | 131,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1609` | 1,510,000.00 USD | 1,510,000.00 USD | 27,340.00 USD | 52,760.00 USD | 34,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1611` | 1,390,000.00 USD | 1,390,000.00 USD | 128,630.00 USD | 101,860.00 USD | 33,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1611` | 4,400,000.00 USD | 4,400,000.00 USD | 148,170.00 USD | 227,820.00 USD | 233,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1613` | 1,130,000.00 USD | 1,130,000.00 USD | 41,630.00 USD | 13,530.00 USD | 39,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1614` | 3,790,000.00 USD | 3,790,000.00 USD | 323,670.00 USD | 194,680.00 USD | 282,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1615` | 1,030,000.00 USD | 1,030,000.00 USD | 34,520.00 USD | 35,650.00 USD | 27,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1615` | 17,290.00 USD | 143,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1617` | 934,420.00 USD | 934,420.00 USD | 52,540.00 USD | 8,620.00 USD | 16,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1617` | 2,990,000.00 USD | 2,990,000.00 USD | 346,150.00 USD | 98,680.00 USD | 418,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1619` | 856,940.00 USD | 856,940.00 USD | 52,280.00 USD | 31,360.00 USD | 50,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1620` | 2,130,000.00 USD | 2,130,000.00 USD | 303,960.00 USD | 134,660.00 USD | 294,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1621` | 722,890.00 USD | 722,890.00 USD | 54,770.00 USD | 43,350.00 USD | 53,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1623` | 570,790.00 USD | 570,790.00 USD | 24,530.00 USD | 47,040.00 USD | 19,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1623` | 1,390,000.00 USD | 1,390,000.00 USD | 297,830.00 USD | 122,030.00 USD | 208,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1625` | 479,800.00 USD | 479,800.00 USD | 32,160.00 USD | 12,640.00 USD | 32,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1625` | 106,340.00 USD | 125,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1626` | 766,610.00 USD | 766,610.00 USD | 234,280.00 USD | 71,120.00 USD | 40,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1627` | 402,380.00 USD | 402,380.00 USD | 10,070.00 USD | 26,330.00 USD | 17,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1629` | 348,690.00 USD | 348,690.00 USD | 8,260.00 USD | 6,700.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1629` | 420,520.00 USD | 420,520.00 USD | 171,310.00 USD | 0.00 USD | 20,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1631` | 322,220.00 USD | 322,220.00 USD | 12,400.00 USD | 12,160.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1632` | 228,350.00 USD | 228,350.00 USD | 9,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1633` | 285,720.00 USD | 285,720.00 USD | 34,400.00 USD | 13,860.00 USD | 13,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1635` | 224,170.00 USD | 224,170.00 USD | 16,140.00 USD | 0.00 USD | 4,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1635` | 219,140.00 USD | 219,140.00 USD | 0.00 USD | 13,670.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1635` | 1,230.00 USD | 19,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1637` | 204,020.00 USD | 204,020.00 USD | 2,730.00 USD | 22,520.00 USD | 15,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1638` | 184,110.00 USD | 184,110.00 USD | 0.00 USD | 0.00 USD | 62,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1639` | 163,360.00 USD | 163,360.00 USD | 6,680.00 USD | 0.00 USD | 32,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1641` | 123,930.00 USD | 123,930.00 USD | 7,360.00 USD | 9,300.00 USD | 4,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1641` | 121,700.00 USD | 121,700.00 USD | 22,480.00 USD | 29,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1643` | 102,290.00 USD | 102,290.00 USD | 25,590.00 USD | 25,250.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1644` | 69,980.00 USD | 69,980.00 USD | 0.00 USD | 8,990.00 USD | 26,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1645` | 40,030.00 USD | 40,030.00 USD | 27,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1645` | 6,190.00 USD | 18,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1647` | 12,390.00 USD | 12,390.00 USD | 12,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1647` | 34,760.00 USD | 34,760.00 USD | 34,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1650` | 7,000.00 USD | 7,000.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1653` | 16,860.00 USD | 16,860.00 USD | 0.00 USD | 16,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1653` | 33,720.00 USD | 33,720.00 USD | 0.00 USD | 16,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1653` | 53,280.00 USD | 53,280.00 USD | 33,810.00 USD | 12,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1655` | 51,660.00 USD | 51,660.00 USD | 0.00 USD | 17,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1655` | 12,070.00 USD | 12,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1656` | 116,520.00 USD | 116,520.00 USD | 43,910.00 USD | 19,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1657` | 99,590.00 USD | 99,590.00 USD | 0.00 USD | 47,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1659` | 103,980.00 USD | 103,980.00 USD | 0.00 USD | 4,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1659` | 157,300.00 USD | 157,300.00 USD | 40,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1661` | 118,960.00 USD | 118,960.00 USD | 8,220.00 USD | 6,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1662` | 290,590.00 USD | 290,590.00 USD | 48,590.00 USD | 62,020.00 USD | 22,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1663` | 149,760.00 USD | 149,760.00 USD | 0.00 USD | 0.00 USD | 30,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1665` | 206,760.00 USD | 206,760.00 USD | 0.00 USD | 0.00 USD | 57,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1665` | 467,780.00 USD | 467,780.00 USD | 87,050.00 USD | 32,780.00 USD | 57,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1667` | 223,700.00 USD | 223,700.00 USD | 0.00 USD | 0.00 USD | 16,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1668` | 561,540.00 USD | 561,540.00 USD | 11,410.00 USD | 39,630.00 USD | 42,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1671` | 244,420.00 USD | 244,420.00 USD | 20,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1671` | 694,570.00 USD | 694,570.00 USD | 70,540.00 USD | 62,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1673` | 265,730.00 USD | 265,730.00 USD | 21,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1674` | 828,480.00 USD | 828,480.00 USD | 44,960.00 USD | 88,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1677` | 280,350.00 USD | 280,350.00 USD | 14,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1677` | 952,330.00 USD | 952,330.00 USD | 59,010.00 USD | 64,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1679` | 286,620.00 USD | 286,620.00 USD | 6,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1680` | 1,140,000.00 USD | 1,140,000.00 USD | 101,910.00 USD | 68,430.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1681` | 405,760.00 USD | 405,760.00 USD | 114,580.00 USD | 4,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1683` | 446,970.00 USD | 446,970.00 USD | 34,880.00 USD | 3,200.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1683` | 1,210,000.00 USD | 1,210,000.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1685` | 490,380.00 USD | 490,380.00 USD | 6,560.00 USD | 23,410.00 USD | 13,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1685` | 5,550.00 USD | 5,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1686` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1687` | 500,440.00 USD | 500,440.00 USD | 0.00 USD | 0.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1689` | 507,420.00 USD | 507,420.00 USD | 0.00 USD | 6,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1689` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1691` | 646,440.00 USD | 646,440.00 USD | 58,560.00 USD | 66,160.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1692` | 1,360,000.00 USD | 1,360,000.00 USD | 21,780.00 USD | 32,070.00 USD | 40,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1693` | 668,420.00 USD | 668,420.00 USD | 13,210.00 USD | 8,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1695` | 681,950.00 USD | 681,950.00 USD | 0.00 USD | 13,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1695` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 30,490.00 USD | 28,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1697` | 724,930.00 USD | 724,930.00 USD | 7,460.00 USD | 35,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1698` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 56,860.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1699` | 759,440.00 USD | 759,440.00 USD | 13,350.00 USD | 21,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1701` | 1,540,000.00 USD | 1,540,000.00 USD | 22,820.00 USD | 25,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1703` | 784,100.00 USD | 784,100.00 USD | 0.00 USD | 14,420.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1704` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 46,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1705` | 804,670.00 USD | 804,670.00 USD | 14,190.00 USD | 6,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1707` | 898,070.00 USD | 898,070.00 USD | 23,780.00 USD | 65,470.00 USD | 4,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1707` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 59,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1709` | 900,780.00 USD | 900,780.00 USD | 0.00 USD | 0.00 USD | 2,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1710` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 25,490.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1711` | 911,020.00 USD | 911,020.00 USD | 0.00 USD | 4,910.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1713` | 923,430.00 USD | 923,430.00 USD | 0.00 USD | 12,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1713` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1715` | 950,600.00 USD | 950,600.00 USD | 0.00 USD | 25,600.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1716` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 15,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1717` | 969,310.00 USD | 969,310.00 USD | 0.00 USD | 8,520.00 USD | 10,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1719` | 1,010,000.00 USD | 1,010,000.00 USD | 34,230.00 USD | 0.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1719` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 7,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1721` | 1,140,000.00 USD | 1,140,000.00 USD | 86,300.00 USD | 16,860.00 USD | 25,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1722` | 2,210,000.00 USD | 2,210,000.00 USD | 118,060.00 USD | 0.00 USD | 342,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1723` | 1,190,000.00 USD | 1,190,000.00 USD | 13,700.00 USD | 0.00 USD | 40,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1725` | 1,210,000.00 USD | 1,210,000.00 USD | 8,230.00 USD | 0.00 USD | 12,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1725` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 20,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1727` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1729` | 1,230,000.00 USD | 1,230,000.00 USD | 8,220.00 USD | 0.00 USD | 6,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1731` | 2,700,000.00 USD | 2,700,000.00 USD | 476,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1733` | 1,250,000.00 USD | 1,250,000.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1735` | 1,270,000.00 USD | 1,270,000.00 USD | 14,970.00 USD | 9,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1737` | 1,290,000.00 USD | 1,290,000.00 USD | 14,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1737` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 52,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1739` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 9,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1740` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 31,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1741` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1743` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1743` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1745` | 1,330,000.00 USD | 1,330,000.00 USD | 8,530.00 USD | 2,460.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1747` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 25,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1749` | 1,450,000.00 USD | 1,450,000.00 USD | 80,070.00 USD | 2,280.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1749` | 2,890,000.00 USD | 2,890,000.00 USD | 69,520.00 USD | 0.00 USD | 22,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1751` | 1,480,000.00 USD | 1,480,000.00 USD | 13,050.00 USD | 0.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1752` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 263,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1753` | 1,520,000.00 USD | 1,520,000.00 USD | 15,300.00 USD | 0.00 USD | 28,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1755` | 1,580,000.00 USD | 1,580,000.00 USD | 16,760.00 USD | 16,650.00 USD | 29,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1755` | 3,370,000.00 USD | 3,370,000.00 USD | 37,610.00 USD | 0.00 USD | 177,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1755` | 600.46 USD | 6,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1757` | 1,680,000.00 USD | 1,680,000.00 USD | 15,820.00 USD | 31,940.00 USD | 45,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1758` | 3,610,000.00 USD | 3,610,000.00 USD | 195,390.00 USD | 38,670.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1759` | 1,760,000.00 USD | 1,760,000.00 USD | 58,810.00 USD | 7,430.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1761` | 1,930,000.00 USD | 1,930,000.00 USD | 50,680.00 USD | 80,960.00 USD | 40,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1761` | 4,110,000.00 USD | 4,110,000.00 USD | 352,270.00 USD | 115,470.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1763` | 2,000,000.00 USD | 2,000,000.00 USD | 26,150.00 USD | 8,780.00 USD | 33,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1764` | 4,500,000.00 USD | 4,500,000.00 USD | 144,160.00 USD | 205,820.00 USD | 40,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1765` | 2,070,000.00 USD | 2,070,000.00 USD | 15,830.00 USD | 20,220.00 USD | 35,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1765` | 339.06 USD | 6,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1767` | 2,190,000.00 USD | 2,190,000.00 USD | 19,860.00 USD | 49,670.00 USD | 44,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1767` | 4,820,000.00 USD | 4,820,000.00 USD | 176,410.00 USD | 128,100.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1769` | 2,280,000.00 USD | 2,280,000.00 USD | 21,060.00 USD | 42,140.00 USD | 32,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1770` | 5,020,000.00 USD | 5,020,000.00 USD | 61,490.00 USD | 98,420.00 USD | 44,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1771` | 2,320,000.00 USD | 2,320,000.00 USD | 22,380.00 USD | 10,910.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1773` | 2,390,000.00 USD | 2,390,000.00 USD | 23,520.00 USD | 23,730.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1773` | 5,210,000.00 USD | 5,210,000.00 USD | 103,820.00 USD | 81,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1775` | 2,460,000.00 USD | 2,460,000.00 USD | 50,760.00 USD | 13,290.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1776` | 5,400,000.00 USD | 5,400,000.00 USD | 135,140.00 USD | 59,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1777` | 2,590,000.00 USD | 2,590,000.00 USD | 23,780.00 USD | 75,120.00 USD | 24,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1779` | 2,620,000.00 USD | 2,620,000.00 USD | 11,580.00 USD | 8,710.00 USD | 13,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1779` | 5,630,000.00 USD | 5,630,000.00 USD | 52,730.00 USD | 46,410.00 USD | 131,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1781` | 2,670,000.00 USD | 2,670,000.00 USD | 46,310.00 USD | 1,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1782` | 5,700,000.00 USD | 5,700,000.00 USD | 20,690.00 USD | 13,990.00 USD | 31,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1783` | 2,760,000.00 USD | 2,760,000.00 USD | 50,250.00 USD | 18,740.00 USD | 23,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1785` | 2,850,000.00 USD | 2,850,000.00 USD | 46,680.00 USD | 40,630.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1785` | 5,950,000.00 USD | 5,950,000.00 USD | 153,160.00 USD | 78,850.00 USD | 16,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1787` | 2,910,000.00 USD | 2,910,000.00 USD | 6,350.00 USD | 28,270.00 USD | 25,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1788` | 6,050,000.00 USD | 6,050,000.00 USD | 73,130.00 USD | 18,250.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1789` | 2,960,000.00 USD | 2,960,000.00 USD | 14,110.00 USD | 18,820.00 USD | 15,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1791` | 3,020,000.00 USD | 3,020,000.00 USD | 35,030.00 USD | 11,020.00 USD | 13,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1791` | 6,230,000.00 USD | 6,230,000.00 USD | 155,720.00 USD | 17,360.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1793` | 3,070,000.00 USD | 3,070,000.00 USD | 24,180.00 USD | 10,220.00 USD | 8,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1794` | 6,330,000.00 USD | 6,330,000.00 USD | 27,100.00 USD | 42,780.00 USD | 36,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1795` | 3,170,000.00 USD | 3,170,000.00 USD | 24,550.00 USD | 49,510.00 USD | 26,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1795` | 48,610.00 USD | 55,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1797` | 3,210,000.00 USD | 3,210,000.00 USD | 15,420.00 USD | 10,360.00 USD | 14,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1797` | 6,370,000.00 USD | 6,370,000.00 USD | 17,130.00 USD | 12,930.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1799` | 3,230,000.00 USD | 3,230,000.00 USD | 5,820.00 USD | 8,690.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1800` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 34,680.00 USD | 64,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1801` | 3,270,000.00 USD | 3,270,000.00 USD | 6,660.00 USD | 21,890.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1803` | 3,300,000.00 USD | 3,300,000.00 USD | 3,610.00 USD | 13,990.00 USD | 12,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1803` | 6,550,000.00 USD | 6,550,000.00 USD | 35,280.00 USD | 25,700.00 USD | 18,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1805` | 3,320,000.00 USD | 3,320,000.00 USD | 5,900.00 USD | 8,280.00 USD | 4,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1805` | 3,130.00 USD | 58,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1806` | 6,640,000.00 USD | 6,640,000.00 USD | 11,410.00 USD | 56,850.00 USD | 19,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1807` | 3,360,000.00 USD | 3,360,000.00 USD | 13,660.00 USD | 15,220.00 USD | 7,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1809` | 3,400,000.00 USD | 3,400,000.00 USD | 13,400.00 USD | 18,230.00 USD | 7,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1809` | 6,780,000.00 USD | 6,780,000.00 USD | 53,670.00 USD | 30,810.00 USD | 58,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1811` | 3,440,000.00 USD | 3,440,000.00 USD | 22,800.00 USD | 3,190.00 USD | 11,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1812` | 6,880,000.00 USD | 6,880,000.00 USD | 34,960.00 USD | 16,640.00 USD | 50,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1813` | 3,500,000.00 USD | 3,500,000.00 USD | 10,730.00 USD | 37,850.00 USD | 19,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1815` | 3,520,000.00 USD | 3,520,000.00 USD | 9,730.00 USD | 0.00 USD | 9,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1815` | 7,010,000.00 USD | 7,010,000.00 USD | 60,010.00 USD | 30,810.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1815` | 8,150.00 USD | 66,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1817` | 3,570,000.00 USD | 3,570,000.00 USD | 25,810.00 USD | 11,020.00 USD | 7,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1818` | 7,120,000.00 USD | 7,120,000.00 USD | 75,040.00 USD | 24,140.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1819` | 3,610,000.00 USD | 3,610,000.00 USD | 25,350.00 USD | 8,030.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1821` | 3,630,000.00 USD | 3,630,000.00 USD | 7,170.00 USD | 12,230.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1821` | 7,240,000.00 USD | 7,240,000.00 USD | 40,950.00 USD | 33,870.00 USD | 41,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1823` | 3,670,000.00 USD | 3,670,000.00 USD | 8,250.00 USD | 18,270.00 USD | 13,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1824` | 7,400,000.00 USD | 7,400,000.00 USD | 39,400.00 USD | 17,880.00 USD | 103,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1825` | 3,700,000.00 USD | 3,700,000.00 USD | 21,190.00 USD | 0.00 USD | 2,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1827` | 3,720,000.00 USD | 3,720,000.00 USD | 6,840.00 USD | 6,860.00 USD | 4,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1827` | 7,560,000.00 USD | 7,560,000.00 USD | 79,610.00 USD | 18,690.00 USD | 65,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1829` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 1,640.00 USD | 347.81 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1830` | 7,700,000.00 USD | 7,700,000.00 USD | 64,890.00 USD | 20,550.00 USD | 52,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1831` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 2,880.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1833` | 3,730,000.00 USD | 3,730,000.00 USD | 2,670.00 USD | 0.00 USD | 4,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1833` | 7,960,000.00 USD | 7,960,000.00 USD | 186,730.00 USD | 49,740.00 USD | 26,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1835` | 3,740,000.00 USD | 3,740,000.00 USD | 3,610.00 USD | 0.00 USD | 728.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1836` | 8,130,000.00 USD | 8,130,000.00 USD | 29,580.00 USD | 83,110.00 USD | 52,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1837` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 2,640.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1839` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1839` | 8,420,000.00 USD | 8,420,000.00 USD | 129,950.00 USD | 41,230.00 USD | 114,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1841` | 3,760,000.00 USD | 3,760,000.00 USD | 5,430.00 USD | 1,730.00 USD | 1,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1842` | 8,580,000.00 USD | 8,580,000.00 USD | 71,550.00 USD | 26,100.00 USD | 62,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1843` | 3,760,000.00 USD | 3,760,000.00 USD | 1,030.00 USD | 2,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1845` | 3,770,000.00 USD | 3,770,000.00 USD | 4,610.00 USD | 4,630.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1845` | 8,690,000.00 USD | 8,690,000.00 USD | 34,630.00 USD | 8,590.00 USD | 66,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1847` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 4,360.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1848` | 8,800,000.00 USD | 8,800,000.00 USD | 26,600.00 USD | 65,230.00 USD | 26,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1849` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 839.14 USD | 1,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1851` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 886.43 USD | 1,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1851` | 9,150,000.00 USD | 9,150,000.00 USD | 94,780.00 USD | 28,290.00 USD | 220,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1853` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 1,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1854` | 9,320,000.00 USD | 9,320,000.00 USD | 105,210.00 USD | 4,290.00 USD | 63,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1855` | 3,800,000.00 USD | 3,800,000.00 USD | 7,630.00 USD | 0.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1857` | 3,820,000.00 USD | 3,820,000.00 USD | 6,710.00 USD | 2,630.00 USD | 12,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1857` | 9,580,000.00 USD | 9,580,000.00 USD | 103,990.00 USD | 32,070.00 USD | 127,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1859` | 3,830,000.00 USD | 3,830,000.00 USD | 9,450.00 USD | 1,470.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1860` | 9,770,000.00 USD | 9,770,000.00 USD | 49,800.00 USD | 62,030.00 USD | 74,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1861` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 2,970.00 USD | 3,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1863` | 3,850,000.00 USD | 3,850,000.00 USD | 1,870.00 USD | 0.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1863` | 9,960,000.00 USD | 9,960,000.00 USD | 71,330.00 USD | 56,440.00 USD | 61,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1865` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 3,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1866` | 10,110,000.00 USD | 10,110,000.00 USD | 82,960.00 USD | 29,050.00 USD | 39,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1867` | 3,860,000.00 USD | 3,860,000.00 USD | 3,300.00 USD | 0.00 USD | 5,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1869` | 10,410,000.00 USD | 10,410,000.00 USD | 159,230.00 USD | 58,520.00 USD | 78,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1872` | 10,710,000.00 USD | 10,710,000.00 USD | 80,790.00 USD | 127,580.00 USD | 93,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1875` | 10,830,000.00 USD | 10,830,000.00 USD | 51,690.00 USD | 30,090.00 USD | 36,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1875` | 21,190.00 USD | 87,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1878` | 10,930,000.00 USD | 10,930,000.00 USD | 55,660.00 USD | 12,570.00 USD | 30,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1881` | 11,000,000.00 USD | 11,000,000.00 USD | 29,820.00 USD | 31,710.00 USD | 13,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1884` | 11,040,000.00 USD | 11,040,000.00 USD | 0.00 USD | 31,900.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1887` | 11,090,000.00 USD | 11,090,000.00 USD | 22,970.00 USD | 0.00 USD | 25,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1890` | 11,220,000.00 USD | 11,220,000.00 USD | 36,740.00 USD | 17,330.00 USD | 75,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1893` | 11,270,000.00 USD | 11,270,000.00 USD | 32,450.00 USD | 6,940.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1895` | 3,550.00 USD | 91,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1896` | 11,350,000.00 USD | 11,350,000.00 USD | 33,480.00 USD | 22,250.00 USD | 18,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1899` | 11,420,000.00 USD | 11,420,000.00 USD | 11,530.00 USD | 38,530.00 USD | 20,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1902` | 11,440,000.00 USD | 11,440,000.00 USD | 14,330.00 USD | 0.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1905` | 11,500,000.00 USD | 11,500,000.00 USD | 8,720.00 USD | 24,800.00 USD | 24,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1908` | 11,600,000.00 USD | 11,600,000.00 USD | 25,220.00 USD | 43,160.00 USD | 28,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1911` | 11,610,000.00 USD | 11,610,000.00 USD | 0.00 USD | 9,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1914` | 11,620,000.00 USD | 11,620,000.00 USD | 7,460.00 USD | 11,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1917` | 11,650,000.00 USD | 11,650,000.00 USD | 0.00 USD | 11,840.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1923` | 11,670,000.00 USD | 11,670,000.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1926` | 11,690,000.00 USD | 11,690,000.00 USD | 11,600.00 USD | 13,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1944` | 11,700,000.00 USD | 11,700,000.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1945` | 1,310.00 USD | 92,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Sell Stop` | `0.0355` | 784,250.00 USD | 0.00 USD | 355.00 USD | `-78.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 783,890.00 USD | 0.00 USD | 600.79 USD | `-74.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 783,290.00 USD | 0.00 USD | 353.50 USD | `-70.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 782,940.00 USD | 0.00 USD | 4,310.00 USD | `-67.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 778,630.00 USD | 0.00 USD | 475.11 USD | `-62.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 778,150.00 USD | 0.00 USD | 131.16 USD | `-61.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 778,020.00 USD | 0.00 USD | 881.45 USD | `-60.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 777,140.00 USD | 0.00 USD | 1,070.00 USD | `-59.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 776,060.00 USD | 0.00 USD | 1,400.00 USD | `-59.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 774,660.00 USD | 0.00 USD | 1,010.00 USD | `-58.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 773,660.00 USD | 0.00 USD | 4,490.00 USD | `-58.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 769,160.00 USD | 0.00 USD | 529.04 USD | `-57.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 768,640.00 USD | 0.00 USD | 2,390.00 USD | `-56.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 766,250.00 USD | 0.00 USD | 757.39 USD | `-55.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 765,490.00 USD | 0.00 USD | 1,490.00 USD | `-53.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 764,000.00 USD | 0.00 USD | 277.37 USD | `-48.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 763,730.00 USD | 0.00 USD | 262.50 USD | `-48.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 763,460.00 USD | 0.00 USD | 795.57 USD | `-47.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 762,670.00 USD | 0.00 USD | 181.00 USD | `-46.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 762,490.00 USD | 0.00 USD | 1,270.00 USD | `-40.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 761,210.00 USD | 0.00 USD | 1,550.00 USD | `-39.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 759,670.00 USD | 0.00 USD | 116.07 USD | `-36.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 759,550.00 USD | 0.00 USD | 19,070.00 USD | `-35.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 740,480.00 USD | 0.00 USD | 577.22 USD | `-34.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 739,900.00 USD | 0.00 USD | 343.50 USD | `-31.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 739,560.00 USD | 0.00 USD | 26,280.00 USD | `-30.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1175` | 713,280.00 USD | 0.00 USD | 105.75 USD | `-30.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 713,170.00 USD | 0.00 USD | 120.50 USD | `-28.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 713,050.00 USD | 0.00 USD | 83,620.00 USD | `-27.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 629,430.00 USD | 0.00 USD | 14,940.00 USD | `-26.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 614,490.00 USD | 0.00 USD | 3,010.00 USD | `-24.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 611,480.00 USD | 0.00 USD | 473.27 USD | `-24.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 611,010.00 USD | 0.00 USD | 220,940.00 USD | `-23.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 390,070.00 USD | 0.00 USD | 25,060.00 USD | `-22.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 365,010.00 USD | 0.00 USD | 5,560.00 USD | `-21.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 359,450.00 USD | 0.00 USD | 625.78 USD | `-20.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 358,820.00 USD | 0.00 USD | 9,090.00 USD | `-20.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 349,730.00 USD | 0.00 USD | 16,260.00 USD | `-19.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 333,470.00 USD | 0.00 USD | 700.86 USD | `-18.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 332,770.00 USD | 0.00 USD | 108.57 USD | `-17.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 332,660.00 USD | 0.00 USD | 349.74 USD | `-17.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 332,310.00 USD | 0.00 USD | 3,520.00 USD | `-16.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 328,790.00 USD | 0.00 USD | 127.35 USD | `-15.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 328,660.00 USD | 0.00 USD | 24,850.00 USD | `-15.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 303,810.00 USD | 0.00 USD | 702.55 USD | `-14.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 303,110.00 USD | 0.00 USD | 1,960.00 USD | `-14.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 301,150.00 USD | 0.00 USD | 27,090.00 USD | `-13.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 274,060.00 USD | 0.00 USD | 119.66 USD | `-12.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 273,940.00 USD | 0.00 USD | 2,290.00 USD | `-12.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 271,650.00 USD | 0.00 USD | 4,550.00 USD | `-11.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 267,100.00 USD | 0.00 USD | 2,420.00 USD | `-11.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 264,680.00 USD | 0.00 USD | 4,360.00 USD | `-10.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 260,320.00 USD | 0.00 USD | 702.05 USD | `-9.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1535` | 259,620.00 USD | 0.00 USD | 204.57 USD | `-8.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 259,410.00 USD | 0.00 USD | 19,280.00 USD | `-8.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 240,140.00 USD | 0.00 USD | 82,840.00 USD | `-7.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 157,300.00 USD | 0.00 USD | 718.79 USD | `-7.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1575` | 156,580.00 USD | 0.00 USD | 443.71 USD | `-6.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 156,130.00 USD | 0.00 USD | 17,200.00 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 138,930.00 USD | 0.00 USD | 70,970.00 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 67,960.00 USD | 0.00 USD | 16,890.00 USD | `-4.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 51,070.00 USD | 0.00 USD | 16,870.00 USD | `-4.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 34,210.00 USD | 0.00 USD | 877.65 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 33,330.00 USD | 0.00 USD | 20,260.00 USD | `-2.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 13,070.00 USD | 0.00 USD | 4,450.00 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 8,620.00 USD | 0.00 USD | 6,570.00 USD | `-1.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 2,050.00 USD | 0.00 USD | 1,670.00 USD | `-1.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 386.67 USD | 0.00 USD | 386.67 USD | `-0.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1685` | 168.50 USD | 168.50 USD | 0.00 USD | `+0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 296.98 USD | 128.48 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 1,210.00 USD | 913.37 USD | 0.00 USD | `+1.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 3,010.00 USD | 1,800.00 USD | 0.00 USD | `+1.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 3,240.00 USD | 229.89 USD | 0.00 USD | `+2.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 12,080.00 USD | 8,840.00 USD | 0.00 USD | `+3.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 18,720.00 USD | 6,650.00 USD | 0.00 USD | `+3.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 20,080.00 USD | 1,350.00 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 28,310.00 USD | 8,230.00 USD | 0.00 USD | `+4.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 28,650.00 USD | 336.40 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 125,100.00 USD | 96,460.00 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 152,030.00 USD | 26,930.00 USD | 0.00 USD | `+6.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 153,160.00 USD | 1,130.00 USD | 0.00 USD | `+7.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 163,520.00 USD | 10,360.00 USD | 0.00 USD | `+7.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 164,390.00 USD | 864.12 USD | 0.00 USD | `+8.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 166,910.00 USD | 2,520.00 USD | 0.00 USD | `+9.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 167,190.00 USD | 276.75 USD | 0.00 USD | `+9.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 167,340.00 USD | 149.79 USD | 0.00 USD | `+10.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 170,530.00 USD | 3,190.00 USD | 0.00 USD | `+10.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 170,680.00 USD | 147.11 USD | 0.00 USD | `+11.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 170,920.00 USD | 245.50 USD | 0.00 USD | `+11.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 171,580.00 USD | 660.73 USD | 0.00 USD | `+12.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 178,720.00 USD | 7,130.00 USD | 0.00 USD | `+13.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 179,110.00 USD | 396.42 USD | 0.00 USD | `+13.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 180,150.00 USD | 1,040.00 USD | 0.00 USD | `+14.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 187,220.00 USD | 7,070.00 USD | 0.00 USD | `+14.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 187,960.00 USD | 742.45 USD | 0.00 USD | `+15.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 192,480.00 USD | 4,520.00 USD | 0.00 USD | `+16.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 192,620.00 USD | 133.19 USD | 0.00 USD | `+16.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 192,750.00 USD | 134.20 USD | 0.00 USD | `+17.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 197,210.00 USD | 4,460.00 USD | 0.00 USD | `+17.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 197,700.00 USD | 492.19 USD | 0.00 USD | `+18.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 232,030.00 USD | 34,330.00 USD | 0.00 USD | `+19.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 232,890.00 USD | 863.97 USD | 0.00 USD | `+19.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 257,530.00 USD | 24,640.00 USD | 0.00 USD | `+20.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 257,710.00 USD | 182.72 USD | 0.00 USD | `+20.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 343,610.00 USD | 85,900.00 USD | 0.00 USD | `+21.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 345,080.00 USD | 1,470.00 USD | 0.00 USD | `+22.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 345,250.00 USD | 174.20 USD | 0.00 USD | `+22.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 347,320.00 USD | 2,080.00 USD | 0.00 USD | `+23.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 347,580.00 USD | 252.51 USD | 0.00 USD | `+24.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 363,390.00 USD | 15,810.00 USD | 0.00 USD | `+25.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 363,510.00 USD | 126.50 USD | 0.00 USD | `+25.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 363,700.00 USD | 190.80 USD | 0.00 USD | `+26.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 364,420.00 USD | 713.94 USD | 0.00 USD | `+26.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 364,630.00 USD | 213.00 USD | 0.00 USD | `+28.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 370,910.00 USD | 6,280.00 USD | 0.00 USD | `+29.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 395,570.00 USD | 24,660.00 USD | 0.00 USD | `+31.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 395,910.00 USD | 333.91 USD | 0.00 USD | `+32.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 399,880.00 USD | 3,980.00 USD | 0.00 USD | `+32.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 400,260.00 USD | 378.55 USD | 0.00 USD | `+33.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 400,640.00 USD | 380.23 USD | 0.00 USD | `+34.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 400,830.00 USD | 185.87 USD | 0.00 USD | `+35.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 401,020.00 USD | 192.69 USD | 0.00 USD | `+35.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2295` | 401,210.00 USD | 187.50 USD | 0.00 USD | `+36.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 445,860.00 USD | 44,650.00 USD | 0.00 USD | `+36.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 446,050.00 USD | 189.14 USD | 0.00 USD | `+37.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 450,310.00 USD | 4,260.00 USD | 0.00 USD | `+38.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 451,820.00 USD | 1,520.00 USD | 0.00 USD | `+38.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 452,020.00 USD | 191.59 USD | 0.00 USD | `+39.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 473,340.00 USD | 21,320.00 USD | 0.00 USD | `+41.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 475,870.00 USD | 2,530.00 USD | 0.00 USD | `+41.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 476,060.00 USD | 195.67 USD | 0.00 USD | `+42.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 498,310.00 USD | 22,240.00 USD | 0.00 USD | `+42.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 507,610.00 USD | 9,300.00 USD | 0.00 USD | `+43.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 658,380.00 USD | 150,770.00 USD | 0.00 USD | `+45.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 677,130.00 USD | 18,750.00 USD | 0.00 USD | `+46.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 677,680.00 USD | 551.23 USD | 0.00 USD | `+47.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 678,710.00 USD | 1,030.00 USD | 0.00 USD | `+48.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 685,900.00 USD | 7,190.00 USD | 0.00 USD | `+48.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 686,190.00 USD | 289.23 USD | 0.00 USD | `+49.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 691,200.00 USD | 5,010.00 USD | 0.00 USD | `+50.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 707,080.00 USD | 15,880.00 USD | 0.00 USD | `+50.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 708,860.00 USD | 1,780.00 USD | 0.00 USD | `+51.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 712,440.00 USD | 3,580.00 USD | 0.00 USD | `+51.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 724,170.00 USD | 11,730.00 USD | 0.00 USD | `+52.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 729,330.00 USD | 5,160.00 USD | 0.00 USD | `+52.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 746,200.00 USD | 16,870.00 USD | 0.00 USD | `+54.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 775,330.00 USD | 29,130.00 USD | 0.00 USD | `+54.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2655` | 855,120.00 USD | 79,780.00 USD | 0.00 USD | `+57.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 855,390.00 USD | 272.88 USD | 0.00 USD | `+60.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 855,780.00 USD | 394.01 USD | 0.00 USD | `+64.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 875,380.00 USD | 19,600.00 USD | 0.00 USD | `+66.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 877,520.00 USD | 2,130.00 USD | 0.00 USD | `+69.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 878,100.00 USD | 579.27 USD | 0.00 USD | `+70.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 881,100.00 USD | 3,010.00 USD | 0.00 USD | `+72.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 881,210.00 USD | 101.21 USD | 0.00 USD | `+75.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 881,470.00 USD | 262.73 USD | 0.00 USD | `+76.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 882,910.00 USD | 1,440.00 USD | 0.00 USD | `+76.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 888,570.00 USD | 5,660.00 USD | 0.00 USD | `+78.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 893,990.00 USD | 5,430.00 USD | 0.00 USD | `+79.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 894,280.00 USD | 289.61 USD | 0.00 USD | `+81.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 899,460.00 USD | 5,180.00 USD | 0.00 USD | `+86.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 899,820.00 USD | 357.85 USD | 0.00 USD | `+98.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3355` | 900,070.00 USD | 251.29 USD | 0.00 USD | `+99.32%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1467` | 9,480,000.00 USD | 0.00 USD | 9,480,000.00 USD | 9,720.00 USD | 9,180.00 USD | 8,780.00 USD |
| `7D` | `0.1470` | 9,450,000.00 USD | 0.00 USD | 9,450,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD |
| `1D` | `0.1473` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 9,360.00 USD | 3,730.00 USD | 1,210.00 USD |
| `7D` | `0.1473` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 6,490.00 USD | 5,400.00 USD | 5,280.00 USD |
| `1D` | `0.1475` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 3,610.00 USD | 1,060.00 USD | 2,800.00 USD |
| `7D` | `0.1476` | 9,430,000.00 USD | 0.00 USD | 9,430,000.00 USD | 0.00 USD | 14,780.00 USD | 5,320.00 USD |
| `1D` | `0.1477` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 5,900.00 USD | 2,820.00 USD | 1,980.00 USD |
| `1D` | `0.1479` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 13,660.00 USD | 12,020.00 USD | 1,950.00 USD |
| `7D` | `0.1479` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 0.00 USD | 39,730.00 USD | 14,560.00 USD |
| `1D` | `0.1481` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 2,900.00 USD | 5,440.00 USD | 10,490.00 USD |
| `7D` | `0.1482` | 9,350,000.00 USD | 0.00 USD | 9,350,000.00 USD | 41,960.00 USD | 20,720.00 USD | 27,030.00 USD |
| `1D` | `0.1483` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 2,780.00 USD | 4,230.00 USD | 3,840.00 USD |
| `1D` | `0.1485` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 9,730.00 USD | 0.00 USD | 2,640.00 USD |
| `7D` | `0.1485` | 9,260,000.00 USD | 0.00 USD | 9,260,000.00 USD | 16,180.00 USD | 7,340.00 USD | 38,270.00 USD |
| `1D` | `0.1487` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 2,660.00 USD | 4,430.00 USD | 5,240.00 USD |
| `7D` | `0.1488` | 9,200,000.00 USD | 0.00 USD | 9,200,000.00 USD | 20,860.00 USD | 3,130.00 USD | 10,390.00 USD |
| `1D` | `0.1489` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 4,080.00 USD | 2,620.00 USD | 3,010.00 USD |
| `1D` | `0.1491` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 3,580.00 USD | 8,610.00 USD | 5,890.00 USD |
| `7D` | `0.1491` | 9,170,000.00 USD | 0.00 USD | 9,170,000.00 USD | 33,540.00 USD | 17,020.00 USD | 28,410.00 USD |
| `1D` | `0.1493` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 10,660.00 USD | 0.00 USD | 2,510.00 USD |
| `7D` | `0.1494` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 34,220.00 USD | 9,890.00 USD | 14,210.00 USD |
| `1D` | `0.1495` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 6,840.00 USD | 5,270.00 USD | 2,180.00 USD |
| `1D` | `0.1497` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 347.81 USD |
| `7D` | `0.1497` | 9,030,000.00 USD | 0.00 USD | 9,030,000.00 USD | 20,880.00 USD | 17,180.00 USD | 9,710.00 USD |
| `1D` | `0.1499` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 2,670.00 USD | 0.00 USD | 2,640.00 USD |
| `7D` | `0.1500` | 8,980,000.00 USD | 0.00 USD | 8,980,000.00 USD | 46,820.00 USD | 5,810.00 USD | 21,940.00 USD |
| `1D` | `0.1501` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 3,610.00 USD | 0.00 USD | 728.16 USD |
| `1D` | `0.1503` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 0.00 USD | 2,640.00 USD | 1,360.00 USD |
| `7D` | `0.1503` | 8,910,000.00 USD | 0.00 USD | 8,910,000.00 USD | 11,490.00 USD | 13,450.00 USD | 9,950.00 USD |
| `1D` | `0.1505` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 6,470.00 USD |
| `7D` | `0.1506` | 8,870,000.00 USD | 0.00 USD | 8,870,000.00 USD | 33,170.00 USD | 18,020.00 USD | 65,400.00 USD |
| `1D` | `0.1507` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 5,430.00 USD | 1,730.00 USD | 1,250.00 USD |
| `1D` | `0.1509` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 5,640.00 USD | 2,850.00 USD | 0.00 USD |
| `7D` | `0.1509` | 8,750,000.00 USD | 0.00 USD | 8,750,000.00 USD | 17,340.00 USD | 9,550.00 USD | 24,150.00 USD |
| `1D` | `0.1511` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 0.00 USD | 4,360.00 USD | 2,500.00 USD |
| `7D` | `0.1512` | 8,700,000.00 USD | 0.00 USD | 8,700,000.00 USD | 18,600.00 USD | 8,620.00 USD | 26,910.00 USD |
| `1D` | `0.1513` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 0.00 USD | 839.14 USD | 1,300.00 USD |
| `1D` | `0.1515` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 0.00 USD | 886.43 USD | 1,340.00 USD |
| `7D` | `0.1515` | 8,650,000.00 USD | 0.00 USD | 8,650,000.00 USD | 53,430.00 USD | 13,330.00 USD | 53,490.00 USD |
| `1D` | `0.1517` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 7,630.00 USD | 1,690.00 USD | 4,220.00 USD |
| `7D` | `0.1518` | 8,530,000.00 USD | 0.00 USD | 8,530,000.00 USD | 46,830.00 USD | 15,160.00 USD | 64,360.00 USD |
| `1D` | `0.1519` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 6,710.00 USD | 2,630.00 USD | 12,090.00 USD |
| `1D` | `0.1521` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 9,450.00 USD | 1,470.00 USD | 3,720.00 USD |
| `7D` | `0.1521` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 47,740.00 USD | 6,920.00 USD | 38,800.00 USD |
| `1D` | `0.1523` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 0.00 USD | 2,970.00 USD | 3,900.00 USD |
| `7D` | `0.1524` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 37,550.00 USD | 13,950.00 USD | 11,280.00 USD |
| `1D` | `0.1525` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 1,870.00 USD | 0.00 USD | 6,520.00 USD |
| `1D` | `0.1527` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 3,300.00 USD | 0.00 USD | 8,300.00 USD |
| `7D` | `0.1527` | 8,250,000.00 USD | 0.00 USD | 8,250,000.00 USD | 56,950.00 USD | 30,410.00 USD | 33,080.00 USD |
| `1D` | `0.1529` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 4,960.00 USD | 1,740.00 USD | 6,570.00 USD |
| `7D` | `0.1530` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 54,790.00 USD | 9,880.00 USD | 16,070.00 USD |
| `1D` | `0.1531` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 6,990.00 USD | 5,200.00 USD | 5,320.00 USD |
| `1D` | `0.1533` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 7,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1533` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 10,760.00 USD | 16,570.00 USD | 21,560.00 USD |
| `1D` | `0.1535` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 2,670.00 USD | 5,590.00 USD | 3,210.00 USD |
| `7D` | `0.1536` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 37,160.00 USD | 2,910.00 USD | 13,450.00 USD |
| `1D` | `0.1537` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 1,650.00 USD | 2,440.00 USD | 1,240.00 USD |
| `1D` | `0.1539` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 2,920.00 USD | 4,200.00 USD | 0.00 USD |
| `7D` | `0.1539` | 7,940,000.00 USD | 0.00 USD | 7,940,000.00 USD | 22,990.00 USD | 18,230.00 USD | 5,070.00 USD |
| `1D` | `0.1541` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 1,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1542` | 7,900,000.00 USD | 0.00 USD | 7,900,000.00 USD | 0.00 USD | 3,590.00 USD | 4,670.00 USD |
| `1D` | `0.1543` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 9,690.00 USD | 2,220.00 USD | 6,220.00 USD |
| `1D` | `0.1545` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 3,580.00 USD | 978.10 USD | 0.00 USD |
| `7D` | `0.1545` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 9,250.00 USD | 0.00 USD | 5,620.00 USD |
| `1D` | `0.1547` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 1,140.00 USD | 6,820.00 USD | 0.00 USD |
| `7D` | `0.1548` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD |
| `1D` | `0.1549` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 4,810.00 USD | 3,490.00 USD | 1,070.00 USD |
| `1D` | `0.1551` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 2,500.00 USD | 3,890.00 USD |
| `7D` | `0.1551` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 34,670.00 USD | 11,820.00 USD | 0.00 USD |
| `1D` | `0.1553` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 11,770.00 USD | 15,630.00 USD | 3,660.00 USD |
| `7D` | `0.1554` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 6,470.00 USD |
| `1D` | `0.1555` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 2,640.00 USD | 1,760.00 USD | 3,530.00 USD |
| `1D` | `0.1557` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 0.00 USD | 1,660.00 USD | 3,250.00 USD |
| `7D` | `0.1557` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 0.00 USD | 4,510.00 USD | 10,800.00 USD |
| `1D` | `0.1559` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 0.00 USD | 8,320.00 USD | 5,580.00 USD |
| `7D` | `0.1560` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 0.00 USD | 6,480.00 USD | 0.00 USD |
| `1D` | `0.1561` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 2,970.00 USD | 2,970.00 USD | 4,970.00 USD |
| `1D` | `0.1563` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 3,050.00 USD | 1,050.00 USD | 11,080.00 USD |
| `7D` | `0.1563` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 0.00 USD | 19,950.00 USD | 9,840.00 USD |
| `1D` | `0.1565` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 24,770.00 USD | 11,570.00 USD | 5,090.00 USD |
| `7D` | `0.1566` | 7,770,000.00 USD | 0.00 USD | 7,770,000.00 USD | 50,480.00 USD | 29,160.00 USD | 26,780.00 USD |
| `1D` | `0.1567` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 24,900.00 USD | 0.00 USD | 11,680.00 USD |
| `1D` | `0.1569` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 15,110.00 USD | 28,380.00 USD | 5,320.00 USD |
| `7D` | `0.1569` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 15,590.00 USD | 5,100.00 USD | 11,900.00 USD |
| `1D` | `0.1571` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 21,680.00 USD | 6,810.00 USD | 4,430.00 USD |
| `7D` | `0.1572` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 40,760.00 USD | 34,450.00 USD | 17,760.00 USD |
| `1D` | `0.1573` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 22,970.00 USD | 9,280.00 USD | 6,990.00 USD |
| `1D` | `0.1575` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 24,450.00 USD | 17,320.00 USD | 6,610.00 USD |
| `7D` | `0.1575` | 7,530,000.00 USD | 0.00 USD | 7,530,000.00 USD | 23,310.00 USD | 88,960.00 USD | 21,360.00 USD |
| `1D` | `0.1577` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 37,440.00 USD | 41,600.00 USD | 14,470.00 USD |
| `7D` | `0.1578` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 58,590.00 USD | 84,670.00 USD | 67,670.00 USD |
| `1D` | `0.1579` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 39,660.00 USD | 22,460.00 USD | 22,710.00 USD |
| `1D` | `0.1581` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 14,290.00 USD | 6,220.00 USD | 9,930.00 USD |
| `7D` | `0.1581` | 7,190,000.00 USD | 0.00 USD | 7,190,000.00 USD | 92,720.00 USD | 58,880.00 USD | 57,600.00 USD |
| `1D` | `0.1583` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 20,850.00 USD | 8,310.00 USD | 13,350.00 USD |
| `7D` | `0.1584` | 6,980,000.00 USD | 0.00 USD | 6,980,000.00 USD | 80,450.00 USD | 35,780.00 USD | 123,970.00 USD |
| `1D` | `0.1585` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 13,780.00 USD | 5,120.00 USD | 10,390.00 USD |
| `1D` | `0.1587` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 9,930.00 USD | 19,010.00 USD | 13,230.00 USD |
| `7D` | `0.1587` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 69,180.00 USD | 22,370.00 USD | 38,480.00 USD |
| `1D` | `0.1589` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 13,490.00 USD | 13,790.00 USD | 8,270.00 USD |
| `7D` | `0.1590` | 6,610,000.00 USD | 0.00 USD | 6,610,000.00 USD | 71,200.00 USD | 44,110.00 USD | 51,290.00 USD |
| `1D` | `0.1591` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 12,080.00 USD | 20,480.00 USD | 13,570.00 USD |
| `1D` | `0.1593` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 40,440.00 USD | 0.00 USD | 17,230.00 USD |
| `7D` | `0.1593` | 6,440,000.00 USD | 0.00 USD | 6,440,000.00 USD | 69,430.00 USD | 56,020.00 USD | 88,830.00 USD |
| `1D` | `0.1595` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 23,220.00 USD | 14,560.00 USD | 23,930.00 USD |
| `7D` | `0.1596` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 161,460.00 USD | 85,250.00 USD | 120,230.00 USD |
| `1D` | `0.1597` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 39,740.00 USD | 21,610.00 USD | 11,040.00 USD |
| `1D` | `0.1599` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 42,800.00 USD | 0.00 USD | 29,970.00 USD |
| `7D` | `0.1599` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 219,060.00 USD | 55,380.00 USD | 87,990.00 USD |
| `1D` | `0.1601` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 39,230.00 USD | 33,200.00 USD | 7,880.00 USD |
| `7D` | `0.1602` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 44,770.00 USD | 46,490.00 USD | 40,380.00 USD |
| `1D` | `0.1603` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 24,830.00 USD | 20,230.00 USD | 6,790.00 USD |
| `1D` | `0.1605` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 25,980.00 USD | 12,370.00 USD | 30,880.00 USD |
| `7D` | `0.1605` | 5,370,000.00 USD | 0.00 USD | 5,370,000.00 USD | 177,720.00 USD | 136,660.00 USD | 217,140.00 USD |
| `1D` | `0.1607` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 43,410.00 USD | 13,680.00 USD | 6,460.00 USD |
| `7D` | `0.1608` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 129,610.00 USD | 174,940.00 USD | 131,300.00 USD |
| `1D` | `0.1609` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 27,340.00 USD | 52,760.00 USD | 34,180.00 USD |
| `1D` | `0.1611` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 128,630.00 USD | 101,860.00 USD | 33,720.00 USD |
| `7D` | `0.1611` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 148,170.00 USD | 227,820.00 USD | 233,470.00 USD |
| `1D` | `0.1613` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 41,630.00 USD | 13,530.00 USD | 39,510.00 USD |
| `7D` | `0.1614` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 323,670.00 USD | 194,680.00 USD | 282,150.00 USD |
| `1D` | `0.1615` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 34,520.00 USD | 35,650.00 USD | 27,800.00 USD |
| `1D` | `0.1617` | 934,420.00 USD | 0.00 USD | 934,420.00 USD | 52,540.00 USD | 8,620.00 USD | 16,330.00 USD |
| `7D` | `0.1617` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 346,150.00 USD | 98,680.00 USD | 418,480.00 USD |
| `1D` | `0.1619` | 856,940.00 USD | 0.00 USD | 856,940.00 USD | 52,280.00 USD | 31,360.00 USD | 50,410.00 USD |
| `7D` | `0.1620` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 303,960.00 USD | 134,660.00 USD | 294,710.00 USD |
| `1D` | `0.1621` | 722,890.00 USD | 0.00 USD | 722,890.00 USD | 54,770.00 USD | 43,350.00 USD | 53,980.00 USD |
| `1D` | `0.1623` | 570,790.00 USD | 0.00 USD | 570,790.00 USD | 24,530.00 USD | 47,040.00 USD | 19,420.00 USD |
| `7D` | `0.1623` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 297,830.00 USD | 122,030.00 USD | 208,070.00 USD |
| `1D` | `0.1625` | 479,800.00 USD | 0.00 USD | 479,800.00 USD | 32,160.00 USD | 12,640.00 USD | 32,620.00 USD |
| `7D` | `0.1626` | 766,610.00 USD | 0.00 USD | 766,610.00 USD | 234,280.00 USD | 71,120.00 USD | 40,690.00 USD |
| `1D` | `0.1627` | 402,380.00 USD | 0.00 USD | 402,380.00 USD | 10,070.00 USD | 26,330.00 USD | 17,290.00 USD |
| `1D` | `0.1629` | 348,690.00 USD | 0.00 USD | 348,690.00 USD | 8,260.00 USD | 6,700.00 USD | 11,520.00 USD |
| `7D` | `0.1629` | 420,520.00 USD | 0.00 USD | 420,520.00 USD | 171,310.00 USD | 0.00 USD | 20,860.00 USD |
| `1D` | `0.1631` | 322,220.00 USD | 0.00 USD | 322,220.00 USD | 12,400.00 USD | 12,160.00 USD | 11,940.00 USD |
| `7D` | `0.1632` | 228,350.00 USD | 0.00 USD | 228,350.00 USD | 9,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1633` | 285,720.00 USD | 0.00 USD | 285,720.00 USD | 34,400.00 USD | 13,860.00 USD | 13,290.00 USD |
| `1D` | `0.1635` | 224,170.00 USD | 0.00 USD | 224,170.00 USD | 16,140.00 USD | 0.00 USD | 4,010.00 USD |
| `7D` | `0.1635` | 219,140.00 USD | 0.00 USD | 219,140.00 USD | 0.00 USD | 13,670.00 USD | 21,360.00 USD |
| `1D` | `0.1637` | 204,020.00 USD | 0.00 USD | 204,020.00 USD | 2,730.00 USD | 22,520.00 USD | 15,400.00 USD |
| `7D` | `0.1638` | 184,110.00 USD | 0.00 USD | 184,110.00 USD | 0.00 USD | 0.00 USD | 62,410.00 USD |
| `1D` | `0.1639` | 163,360.00 USD | 0.00 USD | 163,360.00 USD | 6,680.00 USD | 0.00 USD | 32,750.00 USD |
| `1D` | `0.1641` | 123,930.00 USD | 0.00 USD | 123,930.00 USD | 7,360.00 USD | 9,300.00 USD | 4,980.00 USD |
| `7D` | `0.1641` | 121,700.00 USD | 0.00 USD | 121,700.00 USD | 22,480.00 USD | 29,240.00 USD | 0.00 USD |
| `1D` | `0.1643` | 102,290.00 USD | 0.00 USD | 102,290.00 USD | 25,590.00 USD | 25,250.00 USD | 11,410.00 USD |
| `7D` | `0.1644` | 69,980.00 USD | 0.00 USD | 69,980.00 USD | 0.00 USD | 8,990.00 USD | 26,230.00 USD |
| `1D` | `0.1645` | 40,030.00 USD | 0.00 USD | 40,030.00 USD | 27,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1647` | 12,390.00 USD | 0.00 USD | 12,390.00 USD | 12,390.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1647` | 34,760.00 USD | 0.00 USD | 34,760.00 USD | 34,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1649` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1650` | 7,000.00 USD | 7,000.00 USD | 0.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD |
| `1D` | `0.1653` | 16,860.00 USD | 16,860.00 USD | 0.00 USD | 0.00 USD | 16,860.00 USD | 0.00 USD |
| `1D` | `0.1653` | 33,720.00 USD | 33,720.00 USD | 0.00 USD | 0.00 USD | 16,860.00 USD | 0.00 USD |
| `7D` | `0.1653` | 53,280.00 USD | 53,280.00 USD | 0.00 USD | 33,810.00 USD | 12,460.00 USD | 0.00 USD |
| `1D` | `0.1655` | 51,660.00 USD | 51,660.00 USD | 0.00 USD | 0.00 USD | 17,940.00 USD | 0.00 USD |
| `7D` | `0.1656` | 116,520.00 USD | 116,520.00 USD | 0.00 USD | 43,910.00 USD | 19,330.00 USD | 0.00 USD |
| `1D` | `0.1657` | 99,590.00 USD | 99,590.00 USD | 0.00 USD | 0.00 USD | 47,930.00 USD | 0.00 USD |
| `1D` | `0.1659` | 103,980.00 USD | 103,980.00 USD | 0.00 USD | 0.00 USD | 4,390.00 USD | 0.00 USD |
| `7D` | `0.1659` | 157,300.00 USD | 157,300.00 USD | 0.00 USD | 40,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1661` | 118,960.00 USD | 118,960.00 USD | 0.00 USD | 8,220.00 USD | 6,760.00 USD | 0.00 USD |
| `7D` | `0.1662` | 290,590.00 USD | 290,590.00 USD | 0.00 USD | 48,590.00 USD | 62,020.00 USD | 22,670.00 USD |
| `1D` | `0.1663` | 149,760.00 USD | 149,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 30,790.00 USD |
| `1D` | `0.1665` | 206,760.00 USD | 206,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 57,000.00 USD |
| `7D` | `0.1665` | 467,780.00 USD | 467,780.00 USD | 0.00 USD | 87,050.00 USD | 32,780.00 USD | 57,360.00 USD |
| `1D` | `0.1667` | 223,700.00 USD | 223,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,940.00 USD |
| `7D` | `0.1668` | 561,540.00 USD | 561,540.00 USD | 0.00 USD | 11,410.00 USD | 39,630.00 USD | 42,720.00 USD |
| `1D` | `0.1671` | 244,420.00 USD | 244,420.00 USD | 0.00 USD | 20,720.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1671` | 694,570.00 USD | 694,570.00 USD | 0.00 USD | 70,540.00 USD | 62,490.00 USD | 0.00 USD |
| `1D` | `0.1673` | 265,730.00 USD | 265,730.00 USD | 0.00 USD | 21,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1674` | 828,480.00 USD | 828,480.00 USD | 0.00 USD | 44,960.00 USD | 88,950.00 USD | 0.00 USD |
| `1D` | `0.1677` | 280,350.00 USD | 280,350.00 USD | 0.00 USD | 14,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1677` | 952,330.00 USD | 952,330.00 USD | 0.00 USD | 59,010.00 USD | 64,850.00 USD | 0.00 USD |
| `1D` | `0.1679` | 286,620.00 USD | 286,620.00 USD | 0.00 USD | 6,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1680` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 101,910.00 USD | 68,430.00 USD | 15,310.00 USD |
| `1D` | `0.1681` | 405,760.00 USD | 405,760.00 USD | 0.00 USD | 114,580.00 USD | 4,560.00 USD | 0.00 USD |
| `1D` | `0.1683` | 446,970.00 USD | 446,970.00 USD | 0.00 USD | 34,880.00 USD | 3,200.00 USD | 3,130.00 USD |
| `7D` | `0.1683` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD |
| `1D` | `0.1685` | 490,380.00 USD | 490,380.00 USD | 0.00 USD | 6,560.00 USD | 23,410.00 USD | 13,450.00 USD |
| `7D` | `0.1686` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD |
| `1D` | `0.1687` | 500,440.00 USD | 500,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,060.00 USD |
| `1D` | `0.1689` | 507,420.00 USD | 507,420.00 USD | 0.00 USD | 0.00 USD | 6,980.00 USD | 0.00 USD |
| `7D` | `0.1689` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD |
| `1D` | `0.1691` | 646,440.00 USD | 646,440.00 USD | 0.00 USD | 58,560.00 USD | 66,160.00 USD | 14,290.00 USD |
| `7D` | `0.1692` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 21,780.00 USD | 32,070.00 USD | 40,690.00 USD |
| `1D` | `0.1693` | 668,420.00 USD | 668,420.00 USD | 0.00 USD | 13,210.00 USD | 8,780.00 USD | 0.00 USD |
| `1D` | `0.1695` | 681,950.00 USD | 681,950.00 USD | 0.00 USD | 0.00 USD | 13,520.00 USD | 0.00 USD |
| `7D` | `0.1695` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 30,490.00 USD | 28,010.00 USD |
| `1D` | `0.1697` | 724,930.00 USD | 724,930.00 USD | 0.00 USD | 7,460.00 USD | 35,530.00 USD | 0.00 USD |
| `7D` | `0.1698` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 56,860.00 USD | 18,830.00 USD |
| `1D` | `0.1699` | 759,440.00 USD | 759,440.00 USD | 0.00 USD | 13,350.00 USD | 21,160.00 USD | 0.00 USD |
| `7D` | `0.1701` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 22,820.00 USD | 25,330.00 USD | 0.00 USD |
| `1D` | `0.1703` | 784,100.00 USD | 784,100.00 USD | 0.00 USD | 0.00 USD | 14,420.00 USD | 10,240.00 USD |
| `7D` | `0.1704` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 46,880.00 USD | 0.00 USD |
| `1D` | `0.1705` | 804,670.00 USD | 804,670.00 USD | 0.00 USD | 14,190.00 USD | 6,390.00 USD | 0.00 USD |
| `1D` | `0.1707` | 898,070.00 USD | 898,070.00 USD | 0.00 USD | 23,780.00 USD | 65,470.00 USD | 4,150.00 USD |
| `7D` | `0.1707` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 59,520.00 USD |
| `1D` | `0.1709` | 900,780.00 USD | 900,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,710.00 USD |
| `7D` | `0.1710` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 25,490.00 USD | 5,180.00 USD |
| `1D` | `0.1711` | 911,020.00 USD | 911,020.00 USD | 0.00 USD | 0.00 USD | 4,910.00 USD | 5,330.00 USD |
| `1D` | `0.1713` | 923,430.00 USD | 923,430.00 USD | 0.00 USD | 0.00 USD | 12,410.00 USD | 0.00 USD |
| `7D` | `0.1713` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD |
| `1D` | `0.1715` | 950,600.00 USD | 950,600.00 USD | 0.00 USD | 0.00 USD | 25,600.00 USD | 1,570.00 USD |
| `7D` | `0.1716` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,160.00 USD |
| `1D` | `0.1717` | 969,310.00 USD | 969,310.00 USD | 0.00 USD | 0.00 USD | 8,520.00 USD | 10,190.00 USD |
| `1D` | `0.1719` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 34,230.00 USD | 0.00 USD | 5,030.00 USD |
| `7D` | `0.1719` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,410.00 USD |
| `1D` | `0.1721` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 86,300.00 USD | 16,860.00 USD | 25,690.00 USD |
| `7D` | `0.1722` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 118,060.00 USD | 0.00 USD | 342,490.00 USD |
| `1D` | `0.1723` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 13,700.00 USD | 0.00 USD | 40,940.00 USD |
| `1D` | `0.1725` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 8,230.00 USD | 0.00 USD | 12,130.00 USD |
| `7D` | `0.1725` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,350.00 USD |
| `1D` | `0.1727` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,870.00 USD |
| `1D` | `0.1729` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 6,720.00 USD |
| `7D` | `0.1731` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 476,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1733` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD |
| `1D` | `0.1735` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 14,970.00 USD | 9,510.00 USD | 0.00 USD |
| `1D` | `0.1737` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 14,580.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1737` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 52,610.00 USD |
| `1D` | `0.1739` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,640.00 USD |
| `7D` | `0.1740` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,200.00 USD |
| `1D` | `0.1741` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD |
| `1D` | `0.1743` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD |
| `7D` | `0.1743` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1745` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 8,530.00 USD | 2,460.00 USD | 6,240.00 USD |
| `1D` | `0.1747` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25,680.00 USD |
| `1D` | `0.1749` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 80,070.00 USD | 2,280.00 USD | 17,280.00 USD |
| `7D` | `0.1749` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 22,890.00 USD |
| `1D` | `0.1751` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 13,050.00 USD | 0.00 USD | 10,700.00 USD |
| `7D` | `0.1752` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 263,630.00 USD |
| `1D` | `0.1753` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 15,300.00 USD | 0.00 USD | 28,290.00 USD |
| `1D` | `0.1755` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 16,760.00 USD | 16,650.00 USD | 29,040.00 USD |
| `7D` | `0.1755` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 37,610.00 USD | 0.00 USD | 177,430.00 USD |
| `1D` | `0.1757` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 15,820.00 USD | 31,940.00 USD | 45,550.00 USD |
| `7D` | `0.1758` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 195,390.00 USD | 38,670.00 USD | 8,600.00 USD |
| `1D` | `0.1759` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 58,810.00 USD | 7,430.00 USD | 15,030.00 USD |
| `1D` | `0.1761` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 50,680.00 USD | 80,960.00 USD | 40,780.00 USD |
| `7D` | `0.1761` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 352,270.00 USD | 115,470.00 USD | 32,350.00 USD |
| `1D` | `0.1763` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 26,150.00 USD | 8,780.00 USD | 33,930.00 USD |
| `7D` | `0.1764` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 144,160.00 USD | 205,820.00 USD | 40,340.00 USD |
| `1D` | `0.1765` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 15,830.00 USD | 20,220.00 USD | 35,450.00 USD |
| `1D` | `0.1767` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 19,860.00 USD | 49,670.00 USD | 44,330.00 USD |
| `7D` | `0.1767` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 176,410.00 USD | 128,100.00 USD | 8,530.00 USD |
| `1D` | `0.1769` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 21,060.00 USD | 42,140.00 USD | 32,820.00 USD |
| `7D` | `0.1770` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 61,490.00 USD | 98,420.00 USD | 44,400.00 USD |
| `1D` | `0.1771` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 22,380.00 USD | 10,910.00 USD | 9,700.00 USD |
| `1D` | `0.1773` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 23,520.00 USD | 23,730.00 USD | 18,830.00 USD |
| `7D` | `0.1773` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 103,820.00 USD | 81,060.00 USD | 0.00 USD |
| `1D` | `0.1775` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 50,760.00 USD | 13,290.00 USD | 7,600.00 USD |
| `7D` | `0.1776` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 135,140.00 USD | 59,720.00 USD | 0.00 USD |
| `1D` | `0.1777` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 23,780.00 USD | 75,120.00 USD | 24,860.00 USD |
| `1D` | `0.1779` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 11,580.00 USD | 8,710.00 USD | 13,680.00 USD |
| `7D` | `0.1779` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 52,730.00 USD | 46,410.00 USD | 131,820.00 USD |
| `1D` | `0.1781` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 46,310.00 USD | 1,060.00 USD | 0.00 USD |
| `7D` | `0.1782` | 5,700,000.00 USD | 5,700,000.00 USD | 0.00 USD | 20,690.00 USD | 13,990.00 USD | 31,180.00 USD |
| `1D` | `0.1783` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 50,250.00 USD | 18,740.00 USD | 23,260.00 USD |
| `1D` | `0.1785` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 46,680.00 USD | 40,630.00 USD | 6,690.00 USD |
| `7D` | `0.1785` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 153,160.00 USD | 78,850.00 USD | 16,420.00 USD |
| `1D` | `0.1787` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 6,350.00 USD | 28,270.00 USD | 25,910.00 USD |
| `7D` | `0.1788` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 73,130.00 USD | 18,250.00 USD | 14,040.00 USD |
| `1D` | `0.1789` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 14,110.00 USD | 18,820.00 USD | 15,700.00 USD |
| `1D` | `0.1791` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 35,030.00 USD | 11,020.00 USD | 13,410.00 USD |
| `7D` | `0.1791` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 155,720.00 USD | 17,360.00 USD | 3,940.00 USD |
| `1D` | `0.1793` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 24,180.00 USD | 10,220.00 USD | 8,740.00 USD |
| `7D` | `0.1794` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 27,100.00 USD | 42,780.00 USD | 36,780.00 USD |
| `1D` | `0.1795` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 24,550.00 USD | 49,510.00 USD | 26,940.00 USD |
| `1D` | `0.1797` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 15,420.00 USD | 10,360.00 USD | 14,020.00 USD |
| `7D` | `0.1797` | 6,370,000.00 USD | 6,370,000.00 USD | 0.00 USD | 17,130.00 USD | 12,930.00 USD | 7,670.00 USD |
| `1D` | `0.1799` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 5,820.00 USD | 8,690.00 USD | 11,410.00 USD |
| `7D` | `0.1800` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 34,680.00 USD | 64,620.00 USD |
| `1D` | `0.1801` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 6,660.00 USD | 21,890.00 USD | 13,950.00 USD |
| `1D` | `0.1803` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 3,610.00 USD | 13,990.00 USD | 12,560.00 USD |
| `7D` | `0.1803` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 35,280.00 USD | 25,700.00 USD | 18,250.00 USD |
| `1D` | `0.1805` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 5,900.00 USD | 8,280.00 USD | 4,820.00 USD |
| `7D` | `0.1806` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 11,410.00 USD | 56,850.00 USD | 19,880.00 USD |
| `1D` | `0.1807` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 13,660.00 USD | 15,220.00 USD | 7,070.00 USD |
| `1D` | `0.1809` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 13,400.00 USD | 18,230.00 USD | 7,030.00 USD |
| `7D` | `0.1809` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 53,670.00 USD | 30,810.00 USD | 58,890.00 USD |
| `1D` | `0.1811` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 22,800.00 USD | 3,190.00 USD | 11,470.00 USD |
| `7D` | `0.1812` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 34,960.00 USD | 16,640.00 USD | 50,510.00 USD |
| `1D` | `0.1813` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 10,730.00 USD | 37,850.00 USD | 19,130.00 USD |
| `1D` | `0.1815` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 9,730.00 USD | 0.00 USD | 9,480.00 USD |
| `7D` | `0.1815` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 60,010.00 USD | 30,810.00 USD | 38,270.00 USD |
| `1D` | `0.1817` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 25,810.00 USD | 11,020.00 USD | 7,120.00 USD |
| `7D` | `0.1818` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 75,040.00 USD | 24,140.00 USD | 10,390.00 USD |
| `1D` | `0.1819` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 25,350.00 USD | 8,030.00 USD | 4,990.00 USD |
| `1D` | `0.1821` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 7,170.00 USD | 12,230.00 USD | 8,370.00 USD |
| `7D` | `0.1821` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 40,950.00 USD | 33,870.00 USD | 41,820.00 USD |
| `1D` | `0.1823` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 8,250.00 USD | 18,270.00 USD | 13,960.00 USD |
| `7D` | `0.1824` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 39,400.00 USD | 17,880.00 USD | 103,440.00 USD |
| `1D` | `0.1825` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 21,190.00 USD | 0.00 USD | 2,510.00 USD |
| `1D` | `0.1827` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 6,840.00 USD | 6,860.00 USD | 4,170.00 USD |
| `7D` | `0.1827` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 79,610.00 USD | 18,690.00 USD | 65,670.00 USD |
| `1D` | `0.1829` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 1,640.00 USD | 347.81 USD |
| `7D` | `0.1830` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 64,890.00 USD | 20,550.00 USD | 52,010.00 USD |
| `1D` | `0.1831` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 2,880.00 USD | 5,340.00 USD |
| `1D` | `0.1833` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 2,670.00 USD | 0.00 USD | 4,630.00 USD |
| `7D` | `0.1833` | 7,960,000.00 USD | 7,960,000.00 USD | 0.00 USD | 186,730.00 USD | 49,740.00 USD | 26,350.00 USD |
| `1D` | `0.1835` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 3,610.00 USD | 0.00 USD | 728.16 USD |
| `7D` | `0.1836` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 29,580.00 USD | 83,110.00 USD | 52,650.00 USD |
| `1D` | `0.1837` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 2,640.00 USD | 1,360.00 USD |
| `1D` | `0.1839` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,470.00 USD |
| `7D` | `0.1839` | 8,420,000.00 USD | 8,420,000.00 USD | 0.00 USD | 129,950.00 USD | 41,230.00 USD | 114,190.00 USD |
| `1D` | `0.1841` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 5,430.00 USD | 1,730.00 USD | 1,250.00 USD |
| `7D` | `0.1842` | 8,580,000.00 USD | 8,580,000.00 USD | 0.00 USD | 71,550.00 USD | 26,100.00 USD | 62,140.00 USD |
| `1D` | `0.1843` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 1,030.00 USD | 2,620.00 USD | 0.00 USD |
| `1D` | `0.1845` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 4,610.00 USD | 4,630.00 USD | 1,890.00 USD |
| `7D` | `0.1845` | 8,690,000.00 USD | 8,690,000.00 USD | 0.00 USD | 34,630.00 USD | 8,590.00 USD | 66,720.00 USD |
| `1D` | `0.1847` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 4,360.00 USD | 4,500.00 USD |
| `7D` | `0.1848` | 8,800,000.00 USD | 8,800,000.00 USD | 0.00 USD | 26,600.00 USD | 65,230.00 USD | 26,910.00 USD |
| `1D` | `0.1849` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 839.14 USD | 1,300.00 USD |
| `1D` | `0.1851` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 886.43 USD | 1,340.00 USD |
| `7D` | `0.1851` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 94,780.00 USD | 28,290.00 USD | 220,580.00 USD |
| `1D` | `0.1853` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 1,690.00 USD | 0.00 USD |
| `7D` | `0.1854` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 105,210.00 USD | 4,290.00 USD | 63,060.00 USD |
| `1D` | `0.1855` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 7,630.00 USD | 0.00 USD | 4,220.00 USD |
| `1D` | `0.1857` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 6,710.00 USD | 2,630.00 USD | 12,090.00 USD |
| `7D` | `0.1857` | 9,580,000.00 USD | 9,580,000.00 USD | 0.00 USD | 103,990.00 USD | 32,070.00 USD | 127,480.00 USD |
| `1D` | `0.1859` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 9,450.00 USD | 1,470.00 USD | 3,720.00 USD |
| `7D` | `0.1860` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 49,800.00 USD | 62,030.00 USD | 74,870.00 USD |
| `1D` | `0.1861` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 2,970.00 USD | 3,900.00 USD |
| `1D` | `0.1863` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD | 6,520.00 USD |
| `7D` | `0.1863` | 9,960,000.00 USD | 9,960,000.00 USD | 0.00 USD | 71,330.00 USD | 56,440.00 USD | 61,380.00 USD |
| `1D` | `0.1865` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,240.00 USD |
| `7D` | `0.1866` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 82,960.00 USD | 29,050.00 USD | 39,240.00 USD |
| `1D` | `0.1867` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 3,300.00 USD | 0.00 USD | 5,050.00 USD |
| `7D` | `0.1869` | 10,410,000.00 USD | 10,410,000.00 USD | 0.00 USD | 159,230.00 USD | 58,520.00 USD | 78,120.00 USD |
| `7D` | `0.1872` | 10,710,000.00 USD | 10,710,000.00 USD | 0.00 USD | 80,790.00 USD | 127,580.00 USD | 93,980.00 USD |
| `7D` | `0.1875` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 51,690.00 USD | 30,090.00 USD | 36,560.00 USD |
| `7D` | `0.1878` | 10,930,000.00 USD | 10,930,000.00 USD | 0.00 USD | 55,660.00 USD | 12,570.00 USD | 30,220.00 USD |
| `7D` | `0.1881` | 11,000,000.00 USD | 11,000,000.00 USD | 0.00 USD | 29,820.00 USD | 31,710.00 USD | 13,200.00 USD |
| `7D` | `0.1884` | 11,040,000.00 USD | 11,040,000.00 USD | 0.00 USD | 0.00 USD | 31,900.00 USD | 4,670.00 USD |
| `7D` | `0.1887` | 11,090,000.00 USD | 11,090,000.00 USD | 0.00 USD | 22,970.00 USD | 0.00 USD | 25,760.00 USD |
| `7D` | `0.1890` | 11,220,000.00 USD | 11,220,000.00 USD | 0.00 USD | 36,740.00 USD | 17,330.00 USD | 75,130.00 USD |
| `7D` | `0.1893` | 11,270,000.00 USD | 11,270,000.00 USD | 0.00 USD | 32,450.00 USD | 6,940.00 USD | 16,820.00 USD |
| `7D` | `0.1896` | 11,350,000.00 USD | 11,350,000.00 USD | 0.00 USD | 33,480.00 USD | 22,250.00 USD | 18,680.00 USD |
| `7D` | `0.1899` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 11,530.00 USD | 38,530.00 USD | 20,420.00 USD |
| `7D` | `0.1902` | 11,440,000.00 USD | 11,440,000.00 USD | 0.00 USD | 14,330.00 USD | 0.00 USD | 10,800.00 USD |
| `7D` | `0.1905` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 8,720.00 USD | 24,800.00 USD | 24,210.00 USD |
| `7D` | `0.1908` | 11,600,000.00 USD | 11,600,000.00 USD | 0.00 USD | 25,220.00 USD | 43,160.00 USD | 28,600.00 USD |
| `7D` | `0.1911` | 11,610,000.00 USD | 11,610,000.00 USD | 0.00 USD | 0.00 USD | 9,380.00 USD | 0.00 USD |
| `7D` | `0.1914` | 11,620,000.00 USD | 11,620,000.00 USD | 0.00 USD | 7,460.00 USD | 11,160.00 USD | 0.00 USD |
| `7D` | `0.1917` | 11,650,000.00 USD | 11,650,000.00 USD | 0.00 USD | 0.00 USD | 11,840.00 USD | 11,900.00 USD |
| `7D` | `0.1923` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD |
| `7D` | `0.1926` | 11,690,000.00 USD | 11,690,000.00 USD | 0.00 USD | 11,600.00 USD | 13,630.00 USD | 0.00 USD |
| `7D` | `0.1944` | 11,700,000.00 USD | 11,700,000.00 USD | 0.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `202.90M` | Total OI Tokens: `1,227,509,024.5 ARB`
  * 1h OI Change: `-2.54%` | 4h OI Change: `-6.28%` | 24h OI Change: `-14.43%`
  * Exchange Breakdown: Binance=`45.93M` | Bybit=`28.40M` | OKX=`16.19M` | Hyperliquid=`14.55M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `5.10K` | Last 24h: `10.97K` | Last 3d: `22.34K` | Last 7d: `43.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0037%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0054%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0005%` | **USDT Bitget** | `0.0059%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `39.96%` | `60.04%` | `0.67` | 8,180,000.00 USD |
| `15M` | `Binance` | `41.99%` | `58.01%` | `0.72` | 3,170,000.00 USD |
| `15M` | `OKX` | `42.43%` | `57.57%` | `0.74` | 1,150,000.00 USD |
| `15M` | `Bybit` | `40.07%` | `59.93%` | `0.67` | 1,070,000.00 USD |
| `15M` | `KuCoin` | `42.55%` | `57.45%` | `0.74` | 84,470.00 USD |
| `15M` | `Gate` | `38.38%` | `61.62%` | `0.62` | 252,600.00 USD |
| `15M` | `Bitget` | `39.05%` | `60.95%` | `0.64` | 582,000.00 USD |
| `15M` | `BingX` | `43.71%` | `56.29%` | `0.78` | 174,800.00 USD |
| `15M` | `MEXC` | `33.67%` | `66.33%` | `0.51` | 939,610.00 USD |
| `15M` | `Bitunix` | `34.83%` | `65.17%` | `0.53` | 132,120.00 USD |
| `15M` | `Hyperliquid` | `21.38%` | `78.62%` | `0.27` | 263,360.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.93%` | `49.07%` | `1.04` | 227,620.00 USD |
| `15M` | `Crypto.com` | `93.06%` | `6.94%` | `13.41` | 2,010.00 USD |
| `15M` | `WhiteBIT` | `53.06%` | `46.94%` | `1.13` | 53,750.00 USD |
| `15M` | `HTX` | `45.18%` | `54.82%` | `0.82` | 1,480.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `29.33%` | `70.67%` | `0.42` | 56,570.00 USD |
| `15M` | `Aster` | `10.72%` | `89.28%` | `0.12` | 12,540.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `14.78%` | `85.22%` | `0.17` | 9,960.00 USD |
| `15M` | `Whale Positions` | `41.99%` | `58.01%` | `0.72` | 3,170,000.00 USD |
| `15M` | `Global Accounts` | `39.96%` | `60.04%` | `0.67` | 8,180,000.00 USD |
| `1H` | `ARB` | `45.75%` | `54.25%` | `0.84` | 19,650,000.00 USD |
| `1H` | `Binance` | `46.43%` | `53.57%` | `0.87` | 7,040,000.00 USD |
| `1H` | `OKX` | `46.47%` | `53.53%` | `0.87` | 2,710,000.00 USD |
| `1H` | `Bybit` | `45.48%` | `54.52%` | `0.83` | 2,070,000.00 USD |
| `1H` | `KuCoin` | `45.43%` | `54.57%` | `0.83` | 210,100.00 USD |
| `1H` | `Gate` | `46.28%` | `53.72%` | `0.86` | 795,900.00 USD |
| `1H` | `Bitget` | `37.07%` | `62.93%` | `0.59` | 1,190,000.00 USD |
| `1H` | `BingX` | `66.35%` | `33.65%` | `1.97` | 944,980.00 USD |
| `1H` | `MEXC` | `42.72%` | `57.28%` | `0.75` | 2,310,000.00 USD |
| `1H` | `Bitunix` | `45.58%` | `54.42%` | `0.84` | 461,560.00 USD |
| `1H` | `Hyperliquid` | `18.33%` | `81.67%` | `0.22` | 638,930.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51%` | `49%` | `1.04` | 826,500.00 USD |
| `1H` | `Crypto.com` | `53.87%` | `46.13%` | `1.17` | 6,130.00 USD |
| `1H` | `WhiteBIT` | `70.29%` | `29.71%` | `2.37` | 261,360.00 USD |
| `1H` | `HTX` | `43.54%` | `56.46%` | `0.77` | 5,870.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `39.74%` | `60.26%` | `0.66` | 92,990.00 USD |
| `1H` | `Aster` | `9.31%` | `90.69%` | `0.10` | 18,990.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `37.25%` | `62.75%` | `0.59` | 72,980.00 USD |
| `1H` | `Whale Positions` | `46.43%` | `53.57%` | `0.87` | 7,040,000.00 USD |
| `1H` | `Global Accounts` | `45.75%` | `54.25%` | `0.84` | 19,650,000.00 USD |
| `4H` | `ARB` | `45.91%` | `54.09%` | `0.85` | 50,190,000.00 USD |
| `4H` | `Binance` | `46.54%` | `53.46%` | `0.87` | 18,720,000.00 USD |
| `4H` | `OKX` | `42.79%` | `57.21%` | `0.75` | 8,090,000.00 USD |
| `4H` | `Bybit` | `46.4%` | `53.6%` | `0.87` | 4,490,000.00 USD |
| `4H` | `KuCoin` | `47.24%` | `52.76%` | `0.90` | 507,720.00 USD |
| `4H` | `Gate` | `47.99%` | `52.01%` | `0.92` | 1,960,000.00 USD |
| `4H` | `Bitget` | `41.55%` | `58.45%` | `0.71` | 2,590,000.00 USD |
| `4H` | `BingX` | `41.2%` | `58.8%` | `0.70` | 2,770,000.00 USD |
| `4H` | `MEXC` | `45.2%` | `54.8%` | `0.82` | 5,070,000.00 USD |
| `4H` | `Bitunix` | `48.55%` | `51.45%` | `0.94` | 946,730.00 USD |
| `4H` | `Hyperliquid` | `33%` | `67%` | `0.49` | 1,100,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.37%` | `49.63%` | `1.01` | 2,320,000.00 USD |
| `4H` | `Crypto.com` | `58.15%` | `41.85%` | `1.39` | 23,850.00 USD |
| `4H` | `WhiteBIT` | `79.02%` | `20.98%` | `3.77` | 1,200,000.00 USD |
| `4H` | `HTX` | `35.22%` | `64.78%` | `0.54` | 10,220.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `31.53%` | `68.47%` | `0.46` | 183,700.00 USD |
| `4H` | `Aster` | `33.55%` | `66.45%` | `0.50` | 35,050.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `37.15%` | `62.85%` | `0.59` | 158,780.00 USD |
| `4H` | `Whale Positions` | `46.54%` | `53.46%` | `0.87` | 18,720,000.00 USD |
| `4H` | `Global Accounts` | `45.91%` | `54.09%` | `0.85` | 50,190,000.00 USD |


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
| `0:00 UTC` | `0.1652` | `0.1652` | `0.1652` | `0.1655` | `0.1650` | 53,848.32 USD | 34,595.04 USD | 19,253.28 USD | 15,341.76 USD | `+28.49%` | `17B / 6S` |

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
| `5m` | -178,830.00 USD | 66,930.00 USD | **`DISTRIBUTION`** |
| `15m` | -183,100.00 USD | 158,680.00 USD | **`DISTRIBUTION`** |
| `30m` | -97,810.00 USD | 369,720.00 USD | **`ACCUMULATION`** |
| `1h` | -466,670.00 USD | 7,510.00 USD | **`DISTRIBUTION`** |
| `2h` | -426,300.00 USD | 764,470.00 USD | **`ACCUMULATION`** |
| `4h` | -551,290.00 USD | -1,680,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -621,970.00 USD | -2,220,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -418,180.00 USD | -3,600,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -48,780.00 USD | -3,960,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,370,000.00 USD | -5,850,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,240,000.00 USD | -29,780,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -32,590,000.00 USD | -162,900,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-178.83K` | 15m=`-183.10K` | 1h=`-466.67K` | 24h=`-1.37M`
* Futures Capital Netflows: 5m=`+66.93K` | 15m=`+158.68K` | 1h=`+7.51K` | 24h=`-5.85M`
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
  * `2026-10-30 01:35:49 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:00:49 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
