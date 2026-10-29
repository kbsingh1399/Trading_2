# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 01:14:46 IST` (`2026-10-29 19:44:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1682` | `0.1693` | `0.1682` | `0.1690` | `1,346,540` | 227,416.55 USD | 1,264.47 USD | `+0.56%` | -4,179,803.33 USD | `-0.16` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.1690` | `0.1690` | `0.1684` | `0.1688` | `1,705,590` | 287,802.27 USD | 170,122.12 USD | `+59.11%` | -4,009,681.21 USD | `+2.40` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1688` | `0.1690` | `0.1687` | `0.1687` | `523,447` | 88,380.04 USD | 6,423.19 USD | `+7.27%` | -4,003,258.02 USD | `-0.08` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1686` | `0.1688` | `0.1678` | `0.1679` | `3,525,890` | 593,121.43 USD | 2,485.50 USD | `+0.42%` | -4,295,571.14 USD | `+0.67` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1679` | `0.1688` | `0.1678` | `0.1682` | `2,229,848` | 375,189.89 USD | 114,503.34 USD | `+30.52%` | -4,181,067.80 USD | `+1.23` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1682` | `0.1693` | `0.1682` | `0.1687` | `3,575,577` | 603,598.87 USD | 177,809.78 USD | `+29.46%` | -4,003,258.02 USD | `+1.51` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.1724` | `0.1727` | `0.1681` | `0.1696` | `26,281,427` | 4,477,475.52 USD | -441,479.21 USD | `-9.86%` | -4,351,614.96 USD | `-0.59` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1696` | `0.1704` | `0.1673` | `0.1687` | `18,975,463` | 3,201,824.26 USD | -35,947.57 USD | `-1.12%` | -4,387,562.54 USD | `+0.39` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1686` | `0.1693` | `0.1678` | `0.1687` | `9,331,760` | 1,571,985.23 USD | 294,842.41 USD | `+18.76%` | -4,092,720.12 USD | `+1.21` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,634,787.89 USD | `-0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,872,916.24 USD | `-1.36` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1687` | `82,702,953` | 14,127,041.75 USD | -1,219,758.44 USD | `-8.63%` | -4,092,674.67 USD | `-1.06` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1721` | `0.1729` | `0.1635` | `0.1652` | `91,809,989` | 15,344,891.97 USD | 203,909.29 USD | `+1.33%` | -294,464.16 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1652` | `0.1687` | `0.1623` | `0.1631` | `68,085,678` | 11,252,816.65 USD | -909,329.92 USD | `-8.08%` | -1,203,794.08 USD | `-1.11` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,634,787.89 USD | `-0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,872,916.24 USD | `-1.36` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1687` | `82,702,953` | 14,127,041.75 USD | -1,219,758.44 USD | `-8.63%` | -4,092,674.67 USD | `-1.06` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:14:07 IST` |

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
| `Live` | `Long Liquidation` | `0.0365` | 2,370.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0375` | 1,750.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0385` | 2,080.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0405` | 142,410.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 110.22 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 170.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0435` | 7,920.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0465` | 333.78 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 4,940.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 251.85 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 297.30 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 289.43 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 3,970.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 19,600.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 3,070.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 256.99 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 287.54 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 99,790.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 1,340.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 314.45 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 2,970.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 5,840.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 111.58 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,440.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 80,600.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 5,290.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 14,690.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 378.73 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 1,520.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 4,630.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 7,860.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 21,780.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 112.78 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 49,160.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 787.50 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 362.62 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 8,150.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 640.05 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 2,730.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 24,780.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 40,270.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 7,730.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 589.63 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 253.67 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 2,810.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 11,490.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 2,150.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 1,320.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 802.14 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 6,230.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 19,080.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 5,880.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 1,060.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 342.59 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 534.49 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 425.50 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1125` | 620.20 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 1,360.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 8,950.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 19,210.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 11,120.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 3,850.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 26,040.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 2,380.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 569.45 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 631.80 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 526.95 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 32,960.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 2,710.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 27,900.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 1,200.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 6,160.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 11,450.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 6,090.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 13,600.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 3,530.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 14,880.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 9,690.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 16,420.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1365` | 2,550.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1375` | 3,430.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1385` | 22,460.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1395` | 6,100.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 3,410.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 11,550.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 485,270.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 25,070.00 USD | 984,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 66,020.00 USD | 959,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 31,380.00 USD | 893,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1474` | 10,690,000.00 USD | 10,690,000.00 USD | 6,490.00 USD | 9,220.00 USD | 5,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 73,750.00 USD | 862,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1477` | 10,670,000.00 USD | 10,670,000.00 USD | 0.00 USD | 25,460.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1480` | 10,640,000.00 USD | 10,640,000.00 USD | 6,990.00 USD | 29,300.00 USD | 20,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1483` | 10,580,000.00 USD | 10,580,000.00 USD | 42,230.00 USD | 16,640.00 USD | 33,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 6,110.00 USD | 788,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1486` | 10,490,000.00 USD | 10,490,000.00 USD | 18,610.00 USD | 10,470.00 USD | 25,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1489` | 10,430,000.00 USD | 10,430,000.00 USD | 11,170.00 USD | 3,710.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1492` | 10,410,000.00 USD | 10,410,000.00 USD | 40,320.00 USD | 17,880.00 USD | 27,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1495` | 10,320,000.00 USD | 10,320,000.00 USD | 34,650.00 USD | 18,690.00 USD | 12,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 35,380.00 USD | 782,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1498` | 10,260,000.00 USD | 10,260,000.00 USD | 42,100.00 USD | 9,610.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1501` | 10,190,000.00 USD | 10,190,000.00 USD | 21,010.00 USD | 7,930.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1504` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 2,640.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1504` | 10,150,000.00 USD | 10,150,000.00 USD | 17,800.00 USD | 11,590.00 USD | 44,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1505` | 170,000.00 USD | 746,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1506` | 4,330,000.00 USD | 4,330,000.00 USD | 5,430.00 USD | 0.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1507` | 10,080,000.00 USD | 10,080,000.00 USD | 28,940.00 USD | 12,910.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1508` | 4,320,000.00 USD | 4,320,000.00 USD | 2,690.00 USD | 3,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1510` | 4,310,000.00 USD | 4,310,000.00 USD | 2,950.00 USD | 0.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1510` | 10,000,000.00 USD | 10,000,000.00 USD | 12,660.00 USD | 12,930.00 USD | 29,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1512` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 4,360.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1513` | 9,950,000.00 USD | 9,950,000.00 USD | 32,900.00 USD | 17,610.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1514` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 1,730.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 3,930.00 USD | 576,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1516` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 1,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1516` | 9,860,000.00 USD | 9,860,000.00 USD | 54,550.00 USD | 0.00 USD | 43,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1518` | 4,300,000.00 USD | 4,300,000.00 USD | 11,550.00 USD | 2,630.00 USD | 5,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1519` | 9,760,000.00 USD | 9,760,000.00 USD | 37,430.00 USD | 19,520.00 USD | 70,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1520` | 4,280,000.00 USD | 4,280,000.00 USD | 3,590.00 USD | 1,470.00 USD | 9,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1522` | 4,260,000.00 USD | 4,260,000.00 USD | 5,860.00 USD | 2,970.00 USD | 3,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1522` | 9,630,000.00 USD | 9,630,000.00 USD | 49,800.00 USD | 9,640.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1524` | 4,250,000.00 USD | 4,250,000.00 USD | 1,870.00 USD | 0.00 USD | 5,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1525` | 9,550,000.00 USD | 9,550,000.00 USD | 25,790.00 USD | 13,700.00 USD | 19,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1525` | 42,800.00 USD | 572,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1526` | 4,240,000.00 USD | 4,240,000.00 USD | 3,300.00 USD | 0.00 USD | 8,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1528` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1528` | 9,490,000.00 USD | 9,490,000.00 USD | 75,690.00 USD | 27,110.00 USD | 27,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1530` | 4,230,000.00 USD | 4,230,000.00 USD | 4,960.00 USD | 5,040.00 USD | 6,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1531` | 9,360,000.00 USD | 9,360,000.00 USD | 35,030.00 USD | 8,400.00 USD | 16,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1532` | 4,210,000.00 USD | 4,210,000.00 USD | 12,350.00 USD | 1,900.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1534` | 4,190,000.00 USD | 4,190,000.00 USD | 1,960.00 USD | 2,820.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1534` | 9,300,000.00 USD | 9,300,000.00 USD | 15,780.00 USD | 17,430.00 USD | 20,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 190,210.00 USD | 530,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1536` | 4,190,000.00 USD | 4,190,000.00 USD | 4,320.00 USD | 2,760.00 USD | 918.24 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1537` | 9,240,000.00 USD | 9,240,000.00 USD | 37,050.00 USD | 11,700.00 USD | 10,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1538` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 3,160.00 USD | 1,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1540` | 4,170,000.00 USD | 4,170,000.00 USD | 4,630.00 USD | 3,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1540` | 9,190,000.00 USD | 9,190,000.00 USD | 14,000.00 USD | 6,530.00 USD | 5,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1542` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1543` | 9,160,000.00 USD | 9,160,000.00 USD | 9,250.00 USD | 3,590.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1544` | 4,160,000.00 USD | 4,160,000.00 USD | 13,270.00 USD | 3,200.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1545` | 26,170.00 USD | 339,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1546` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 6,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1546` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 0.00 USD | 5,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1548` | 4,140,000.00 USD | 4,140,000.00 USD | 1,140.00 USD | 1,840.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1549` | 9,140,000.00 USD | 9,140,000.00 USD | 11,570.00 USD | 6,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1550` | 4,130,000.00 USD | 4,130,000.00 USD | 4,810.00 USD | 2,620.00 USD | 959.69 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1552` | 4,120,000.00 USD | 4,120,000.00 USD | 4,500.00 USD | 1,530.00 USD | 2,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1552` | 9,120,000.00 USD | 9,120,000.00 USD | 23,110.00 USD | 7,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1554` | 4,110,000.00 USD | 4,110,000.00 USD | 9,910.00 USD | 19,270.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1555` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 0.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1555` | 42,630.00 USD | 313,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1556` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 3,410.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1558` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1558` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 10,990.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1560` | 4,070,000.00 USD | 4,070,000.00 USD | 5,460.00 USD | 11,300.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1561` | 9,060,000.00 USD | 9,060,000.00 USD | 0.00 USD | 5,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1562` | 4,050,000.00 USD | 4,050,000.00 USD | 3,050.00 USD | 1,050.00 USD | 6,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1564` | 4,040,000.00 USD | 4,040,000.00 USD | 6,880.00 USD | 5,200.00 USD | 13,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1564` | 9,050,000.00 USD | 9,050,000.00 USD | 24,300.00 USD | 28,690.00 USD | 21,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1565` | 20,840.00 USD | 271,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1566` | 4,010,000.00 USD | 4,010,000.00 USD | 38,690.00 USD | 6,370.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1567` | 8,980,000.00 USD | 8,980,000.00 USD | 41,770.00 USD | 15,360.00 USD | 15,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1568` | 3,950,000.00 USD | 3,950,000.00 USD | 13,610.00 USD | 26,770.00 USD | 7,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1570` | 3,910,000.00 USD | 3,910,000.00 USD | 19,150.00 USD | 11,300.00 USD | 2,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1570` | 8,910,000.00 USD | 8,910,000.00 USD | 0.00 USD | 5,100.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1572` | 3,870,000.00 USD | 3,870,000.00 USD | 26,510.00 USD | 7,430.00 USD | 15,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1573` | 8,890,000.00 USD | 8,890,000.00 USD | 58,830.00 USD | 56,100.00 USD | 25,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1574` | 3,830,000.00 USD | 3,830,000.00 USD | 21,250.00 USD | 6,090.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1575` | 4,940.00 USD | 250,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1576` | 3,800,000.00 USD | 3,800,000.00 USD | 13,180.00 USD | 26,110.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1576` | 8,750,000.00 USD | 8,750,000.00 USD | 26,600.00 USD | 102,190.00 USD | 54,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1578` | 3,750,000.00 USD | 3,750,000.00 USD | 62,820.00 USD | 51,020.00 USD | 17,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1579` | 8,570,000.00 USD | 8,570,000.00 USD | 101,500.00 USD | 95,190.00 USD | 42,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1580` | 3,610,000.00 USD | 3,610,000.00 USD | 25,030.00 USD | 0.00 USD | 18,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1582` | 3,570,000.00 USD | 3,570,000.00 USD | 17,260.00 USD | 12,250.00 USD | 9,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1582` | 8,330,000.00 USD | 8,330,000.00 USD | 56,130.00 USD | 13,480.00 USD | 89,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1584` | 3,530,000.00 USD | 3,530,000.00 USD | 24,310.00 USD | 2,750.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1585` | 8,170,000.00 USD | 8,170,000.00 USD | 87,110.00 USD | 50,340.00 USD | 75,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1585` | 5,770.00 USD | 245,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1586` | 3,500,000.00 USD | 3,500,000.00 USD | 6,650.00 USD | 15,680.00 USD | 12,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1588` | 3,460,000.00 USD | 3,460,000.00 USD | 10,190.00 USD | 13,850.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1588` | 7,950,000.00 USD | 7,950,000.00 USD | 34,830.00 USD | 30,030.00 USD | 41,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1590` | 3,430,000.00 USD | 3,430,000.00 USD | 3,300.00 USD | 19,810.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1591` | 7,850,000.00 USD | 7,850,000.00 USD | 110,640.00 USD | 49,670.00 USD | 60,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1592` | 3,400,000.00 USD | 3,400,000.00 USD | 26,740.00 USD | 6,320.00 USD | 13,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1594` | 3,360,000.00 USD | 3,360,000.00 USD | 43,860.00 USD | 13,170.00 USD | 13,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1594` | 7,630,000.00 USD | 7,630,000.00 USD | 85,560.00 USD | 39,260.00 USD | 102,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1595` | 63,000.00 USD | 239,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1596` | 3,290,000.00 USD | 3,290,000.00 USD | 6,250.00 USD | 6,020.00 USD | 32,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1597` | 7,400,000.00 USD | 7,400,000.00 USD | 228,850.00 USD | 96,110.00 USD | 102,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1598` | 3,240,000.00 USD | 3,240,000.00 USD | 61,390.00 USD | 16,990.00 USD | 29,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1600` | 3,140,000.00 USD | 3,140,000.00 USD | 16,450.00 USD | 22,650.00 USD | 11,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1600` | 6,970,000.00 USD | 6,970,000.00 USD | 105,580.00 USD | 38,830.00 USD | 76,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1602` | 3,090,000.00 USD | 3,090,000.00 USD | 47,310.00 USD | 24,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1603` | 6,750,000.00 USD | 6,750,000.00 USD | 62,240.00 USD | 54,840.00 USD | 81,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1604` | 3,010,000.00 USD | 3,010,000.00 USD | 23,170.00 USD | 6,610.00 USD | 17,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1605` | 32,770.00 USD | 176,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1606` | 2,970,000.00 USD | 2,970,000.00 USD | 35,830.00 USD | 16,070.00 USD | 22,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1606` | 6,550,000.00 USD | 6,550,000.00 USD | 211,140.00 USD | 149,480.00 USD | 227,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1608` | 2,890,000.00 USD | 2,890,000.00 USD | 42,100.00 USD | 30,480.00 USD | 18,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1609` | 5,960,000.00 USD | 5,960,000.00 USD | 92,990.00 USD | 229,060.00 USD | 182,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1610` | 2,800,000.00 USD | 2,800,000.00 USD | 88,820.00 USD | 91,470.00 USD | 29,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1612` | 2,590,000.00 USD | 2,590,000.00 USD | 79,330.00 USD | 54,580.00 USD | 50,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1612` | 5,460,000.00 USD | 5,460,000.00 USD | 281,220.00 USD | 247,430.00 USD | 159,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1614` | 2,410,000.00 USD | 2,410,000.00 USD | 20,150.00 USD | 12,260.00 USD | 25,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1615` | 4,770,000.00 USD | 4,770,000.00 USD | 293,210.00 USD | 107,900.00 USD | 374,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1615` | 17,290.00 USD | 143,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1616` | 2,350,000.00 USD | 2,350,000.00 USD | 41,700.00 USD | 20,020.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1618` | 2,260,000.00 USD | 2,260,000.00 USD | 46,050.00 USD | 12,180.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1618` | 4,000,000.00 USD | 4,000,000.00 USD | 310,070.00 USD | 128,930.00 USD | 310,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1620` | 2,180,000.00 USD | 2,180,000.00 USD | 46,800.00 USD | 49,990.00 USD | 43,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1621` | 3,250,000.00 USD | 3,250,000.00 USD | 241,340.00 USD | 148,260.00 USD | 322,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1622` | 2,040,000.00 USD | 2,040,000.00 USD | 50,590.00 USD | 31,260.00 USD | 27,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1624` | 1,930,000.00 USD | 1,930,000.00 USD | 9,570.00 USD | 48,390.00 USD | 11,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1624` | 2,530,000.00 USD | 2,530,000.00 USD | 375,170.00 USD | 135,840.00 USD | 119,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1625` | 106,340.00 USD | 126,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1626` | 1,860,000.00 USD | 1,860,000.00 USD | 13,530.00 USD | 0.00 USD | 20,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1627` | 1,900,000.00 USD | 1,900,000.00 USD | 291,760.00 USD | 0.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1628` | 1,830,000.00 USD | 1,830,000.00 USD | 14,220.00 USD | 29,880.00 USD | 12,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1630` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 3,150.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1630` | 1,600,000.00 USD | 1,600,000.00 USD | 9,210.00 USD | 0.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1632` | 1,760,000.00 USD | 1,760,000.00 USD | 12,400.00 USD | 19,630.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1634` | 1,710,000.00 USD | 1,710,000.00 USD | 32,300.00 USD | 6,390.00 USD | 7,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1635` | 971.58 USD | 20,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1636` | 1,670,000.00 USD | 1,670,000.00 USD | 4,900.00 USD | 9,310.00 USD | 12,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1636` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 13,670.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1638` | 1,640,000.00 USD | 1,640,000.00 USD | 9,410.00 USD | 13,220.00 USD | 34,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1639` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 62,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1640` | 1,580,000.00 USD | 1,580,000.00 USD | 7,360.00 USD | 6,090.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1642` | 1,560,000.00 USD | 1,560,000.00 USD | 20,760.00 USD | 17,890.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1642` | 1,480,000.00 USD | 1,480,000.00 USD | 22,480.00 USD | 29,240.00 USD | 26,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1644` | 1,510,000.00 USD | 1,510,000.00 USD | 4,830.00 USD | 7,360.00 USD | 23,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1645` | 1,410,000.00 USD | 1,410,000.00 USD | 34,760.00 USD | 8,990.00 USD | 7,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1645` | 6,740.00 USD | 19,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1646` | 1,480,000.00 USD | 1,480,000.00 USD | 40,030.00 USD | 24,740.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1648` | 1,400,000.00 USD | 1,400,000.00 USD | 4,570.00 USD | 16,250.00 USD | 15,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1648` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1650` | 1,360,000.00 USD | 1,360,000.00 USD | 7,830.00 USD | 20,170.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1651` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 51,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1652` | 1,330,000.00 USD | 1,330,000.00 USD | 42,530.00 USD | 0.00 USD | 34,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1654` | 1,260,000.00 USD | 1,260,000.00 USD | 31,300.00 USD | 27,430.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1654` | 1,300,000.00 USD | 1,300,000.00 USD | 60,050.00 USD | 31,800.00 USD | 33,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1655` | 12,410.00 USD | 12,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1656` | 1,150,000.00 USD | 1,150,000.00 USD | 38,480.00 USD | 40,450.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1657` | 1,170,000.00 USD | 1,170,000.00 USD | 10,890.00 USD | 0.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1658` | 1,050,000.00 USD | 1,050,000.00 USD | 25,050.00 USD | 14,850.00 USD | 41,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1660` | 964,090.00 USD | 964,090.00 USD | 27,070.00 USD | 11,150.00 USD | 47,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1660` | 1,140,000.00 USD | 1,140,000.00 USD | 29,890.00 USD | 11,020.00 USD | 33,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1662` | 878,010.00 USD | 878,010.00 USD | 20,300.00 USD | 11,720.00 USD | 36,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1663` | 1,070,000.00 USD | 1,070,000.00 USD | 86,050.00 USD | 51,000.00 USD | 75,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1664` | 809,060.00 USD | 809,060.00 USD | 31,630.00 USD | 47,390.00 USD | 46,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1666` | 683,510.00 USD | 683,510.00 USD | 41,260.00 USD | 50,440.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1666` | 856,340.00 USD | 856,340.00 USD | 49,590.00 USD | 32,780.00 USD | 28,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1668` | 554,310.00 USD | 554,310.00 USD | 102,890.00 USD | 28,980.00 USD | 20,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1669` | 745,150.00 USD | 745,150.00 USD | 11,410.00 USD | 64,050.00 USD | 42,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1670` | 401,620.00 USD | 401,620.00 USD | 25,410.00 USD | 21,810.00 USD | 22,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1672` | 332,390.00 USD | 332,390.00 USD | 42,030.00 USD | 31,130.00 USD | 18,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1672` | 626,980.00 USD | 626,980.00 USD | 70,540.00 USD | 38,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1675` | 518,370.00 USD | 518,370.00 USD | 64,490.00 USD | 105,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1676` | 240,820.00 USD | 240,820.00 USD | 14,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1678` | 347,970.00 USD | 347,970.00 USD | 71,860.00 USD | 79,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1680` | 226,200.00 USD | 226,200.00 USD | 75,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1681` | 196,180.00 USD | 196,180.00 USD | 69,520.00 USD | 36,390.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1682` | 150,780.00 USD | 150,780.00 USD | 74,980.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1684` | 52,230.00 USD | 52,230.00 USD | 13,810.00 USD | 26,600.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1684` | 74,950.00 USD | 74,950.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1690` | 25,360.00 USD | 25,360.00 USD | 18,380.00 USD | 6,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1690` | 38,670.00 USD | 38,670.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1692` | 128,460.00 USD | 128,460.00 USD | 36,940.00 USD | 66,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1693` | 92,520.00 USD | 92,520.00 USD | 21,780.00 USD | 32,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1694` | 150,750.00 USD | 150,750.00 USD | 0.00 USD | 22,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1696` | 207,880.00 USD | 207,880.00 USD | 0.00 USD | 87,350.00 USD | 28,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1698` | 214,900.00 USD | 214,900.00 USD | 7,460.00 USD | 56,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1699` | 252,030.00 USD | 252,030.00 USD | 0.00 USD | 25,330.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1702` | 225,130.00 USD | 225,130.00 USD | 0.00 USD | 0.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1702` | 321,740.00 USD | 321,740.00 USD | 22,820.00 USD | 46,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1704` | 239,550.00 USD | 239,550.00 USD | 0.00 USD | 14,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1706` | 272,150.00 USD | 272,150.00 USD | 22,060.00 USD | 6,390.00 USD | 4,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1708` | 350,330.00 USD | 350,330.00 USD | 15,910.00 USD | 62,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1708` | 411,920.00 USD | 411,920.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1710` | 355,660.00 USD | 355,660.00 USD | 0.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1712` | 370,700.00 USD | 370,700.00 USD | 0.00 USD | 15,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1714` | 453,940.00 USD | 453,940.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1716` | 396,300.00 USD | 396,300.00 USD | 0.00 USD | 25,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1718` | 414,170.00 USD | 414,170.00 USD | 9,350.00 USD | 8,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1720` | 481,630.00 USD | 481,630.00 USD | 67,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1720` | 608,300.00 USD | 608,300.00 USD | 0.00 USD | 0.00 USD | 154,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1722` | 561,190.00 USD | 561,190.00 USD | 34,600.00 USD | 16,860.00 USD | 28,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1723` | 896,750.00 USD | 896,750.00 USD | 100,390.00 USD | 0.00 USD | 188,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1724` | 582,750.00 USD | 582,750.00 USD | 0.00 USD | 0.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1726` | 587,450.00 USD | 587,450.00 USD | 0.00 USD | 0.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1728` | 606,270.00 USD | 606,270.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1729` | 1,030,000.00 USD | 1,030,000.00 USD | 137,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1732` | 616,330.00 USD | 616,330.00 USD | 0.00 USD | 0.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1732` | 1,370,000.00 USD | 1,370,000.00 USD | 338,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1736` | 640,810.00 USD | 640,810.00 USD | 14,970.00 USD | 9,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1738` | 655,390.00 USD | 655,390.00 USD | 14,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1738` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 83,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1740` | 665,040.00 USD | 665,040.00 USD | 0.00 USD | 0.00 USD | 9,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1742` | 675,000.00 USD | 675,000.00 USD | 0.00 USD | 0.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1744` | 680,120.00 USD | 680,120.00 USD | 0.00 USD | 2,460.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1744` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1746` | 698,150.00 USD | 698,150.00 USD | 8,530.00 USD | 0.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1748` | 792,060.00 USD | 792,060.00 USD | 55,280.00 USD | 2,280.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1750` | 822,210.00 USD | 822,210.00 USD | 24,790.00 USD | 0.00 USD | 5,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1750` | 1,710,000.00 USD | 1,710,000.00 USD | 69,520.00 USD | 0.00 USD | 167,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1752` | 873,340.00 USD | 873,340.00 USD | 23,850.00 USD | 0.00 USD | 27,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1753` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 191,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1754` | 911,990.00 USD | 911,990.00 USD | 14,290.00 USD | 8,430.00 USD | 15,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1756` | 969,910.00 USD | 969,910.00 USD | 4,060.00 USD | 19,210.00 USD | 34,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1756` | 2,090,000.00 USD | 2,090,000.00 USD | 88,730.00 USD | 0.00 USD | 106,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1758` | 1,080,000.00 USD | 1,080,000.00 USD | 64,490.00 USD | 20,940.00 USD | 27,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1759` | 2,350,000.00 USD | 2,350,000.00 USD | 217,800.00 USD | 38,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1760` | 1,200,000.00 USD | 1,200,000.00 USD | 20,820.00 USD | 76,400.00 USD | 15,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1762` | 1,320,000.00 USD | 1,320,000.00 USD | 54,910.00 USD | 11,990.00 USD | 60,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1762` | 2,850,000.00 USD | 2,850,000.00 USD | 289,660.00 USD | 180,810.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1764` | 1,400,000.00 USD | 1,400,000.00 USD | 12,650.00 USD | 25,840.00 USD | 35,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1765` | 3,220,000.00 USD | 3,220,000.00 USD | 154,540.00 USD | 166,180.00 USD | 48,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1765` | 1,260.00 USD | 1,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1766` | 1,450,000.00 USD | 1,450,000.00 USD | 7,570.00 USD | 3,150.00 USD | 40,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1768` | 1,590,000.00 USD | 1,590,000.00 USD | 32,300.00 USD | 83,210.00 USD | 29,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1768` | 3,550,000.00 USD | 3,550,000.00 USD | 161,560.00 USD | 138,440.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1770` | 1,660,000.00 USD | 1,660,000.00 USD | 36,140.00 USD | 14,270.00 USD | 20,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1771` | 3,770,000.00 USD | 3,770,000.00 USD | 69,030.00 USD | 138,810.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1772` | 1,710,000.00 USD | 1,710,000.00 USD | 7,290.00 USD | 14,560.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1774` | 1,770,000.00 USD | 1,770,000.00 USD | 35,970.00 USD | 21,330.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1774` | 4,010,000.00 USD | 4,010,000.00 USD | 148,780.00 USD | 90,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1776` | 1,870,000.00 USD | 1,870,000.00 USD | 73,100.00 USD | 12,480.00 USD | 13,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1777` | 4,180,000.00 USD | 4,180,000.00 USD | 67,350.00 USD | 40,700.00 USD | 59,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1778` | 1,990,000.00 USD | 1,990,000.00 USD | 23,220.00 USD | 77,730.00 USD | 11,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1780` | 2,000,000.00 USD | 2,000,000.00 USD | 4,270.00 USD | 1,060.00 USD | 13,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1780` | 4,370,000.00 USD | 4,370,000.00 USD | 52,730.00 USD | 38,910.00 USD | 97,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1782` | 2,110,000.00 USD | 2,110,000.00 USD | 46,310.00 USD | 13,190.00 USD | 47,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1783` | 4,570,000.00 USD | 4,570,000.00 USD | 117,540.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1784` | 2,220,000.00 USD | 2,220,000.00 USD | 82,580.00 USD | 19,630.00 USD | 8,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1786` | 2,290,000.00 USD | 2,290,000.00 USD | 18,920.00 USD | 28,240.00 USD | 18,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1786` | 4,760,000.00 USD | 4,760,000.00 USD | 129,440.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1788` | 2,380,000.00 USD | 2,380,000.00 USD | 30,950.00 USD | 40,790.00 USD | 25,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1789` | 4,820,000.00 USD | 4,820,000.00 USD | 48,810.00 USD | 7,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1790` | 2,440,000.00 USD | 2,440,000.00 USD | 36,940.00 USD | 8,720.00 USD | 10,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1792` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 15,540.00 USD | 20,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1792` | 5,000,000.00 USD | 5,000,000.00 USD | 134,000.00 USD | 39,820.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1794` | 2,560,000.00 USD | 2,560,000.00 USD | 36,860.00 USD | 48,460.00 USD | 3,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1795` | 5,080,000.00 USD | 5,080,000.00 USD | 17,130.00 USD | 19,870.00 USD | 44,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1795` | 48,610.00 USD | 49,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1796` | 2,630,000.00 USD | 2,630,000.00 USD | 20,690.00 USD | 15,920.00 USD | 32,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1798` | 2,670,000.00 USD | 2,670,000.00 USD | 6,590.00 USD | 12,950.00 USD | 15,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1798` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 6,240.00 USD | 27,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1800` | 2,690,000.00 USD | 2,690,000.00 USD | 5,820.00 USD | 1,930.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1801` | 5,210,000.00 USD | 5,210,000.00 USD | 6,490.00 USD | 40,090.00 USD | 46,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1802` | 2,760,000.00 USD | 2,760,000.00 USD | 15,140.00 USD | 34,770.00 USD | 14,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1804` | 2,780,000.00 USD | 2,780,000.00 USD | 4,260.00 USD | 3,940.00 USD | 15,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1804` | 5,280,000.00 USD | 5,280,000.00 USD | 28,790.00 USD | 27,450.00 USD | 14,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1805` | 3,130.00 USD | 53,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1806` | 2,820,000.00 USD | 2,820,000.00 USD | 18,420.00 USD | 11,530.00 USD | 9,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1807` | 5,420,000.00 USD | 5,420,000.00 USD | 11,410.00 USD | 63,170.00 USD | 67,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1808` | 2,890,000.00 USD | 2,890,000.00 USD | 24,170.00 USD | 21,780.00 USD | 28,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1810` | 2,930,000.00 USD | 2,930,000.00 USD | 21,750.00 USD | 8,780.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1810` | 5,540,000.00 USD | 5,540,000.00 USD | 79,380.00 USD | 30,940.00 USD | 12,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1812` | 3,040,000.00 USD | 3,040,000.00 USD | 37,500.00 USD | 40,830.00 USD | 33,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1813` | 5,650,000.00 USD | 5,650,000.00 USD | 32,530.00 USD | 15,780.00 USD | 56,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1814` | 3,070,000.00 USD | 3,070,000.00 USD | 7,290.00 USD | 3,320.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1815` | 8,170.00 USD | 61,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1816` | 3,110,000.00 USD | 3,110,000.00 USD | 28,660.00 USD | 0.00 USD | 17,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1816` | 5,740,000.00 USD | 5,740,000.00 USD | 46,430.00 USD | 21,200.00 USD | 25,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1818` | 3,150,000.00 USD | 3,150,000.00 USD | 13,970.00 USD | 11,780.00 USD | 14,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1819` | 5,870,000.00 USD | 5,870,000.00 USD | 65,350.00 USD | 24,720.00 USD | 43,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1820` | 3,200,000.00 USD | 3,200,000.00 USD | 21,220.00 USD | 17,800.00 USD | 3,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1822` | 3,230,000.00 USD | 3,230,000.00 USD | 8,490.00 USD | 11,090.00 USD | 11,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1822` | 6,050,000.00 USD | 6,050,000.00 USD | 46,760.00 USD | 36,230.00 USD | 92,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1824` | 3,260,000.00 USD | 3,260,000.00 USD | 11,560.00 USD | 8,890.00 USD | 8,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1825` | 6,140,000.00 USD | 6,140,000.00 USD | 61,720.00 USD | 17,120.00 USD | 12,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1825` | 185.09 USD | 61,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1826` | 3,290,000.00 USD | 3,290,000.00 USD | 21,440.00 USD | 6,860.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1828` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1828` | 6,290,000.00 USD | 6,290,000.00 USD | 51,470.00 USD | 24,320.00 USD | 69,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1830` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 4,510.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1831` | 6,460,000.00 USD | 6,460,000.00 USD | 85,970.00 USD | 21,930.00 USD | 63,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1832` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 4,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1834` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 728.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1834` | 6,720,000.00 USD | 6,720,000.00 USD | 165,640.00 USD | 47,980.00 USD | 51,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1836` | 3,310,000.00 USD | 3,310,000.00 USD | 3,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1837` | 6,950,000.00 USD | 6,950,000.00 USD | 72,930.00 USD | 76,140.00 USD | 83,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1838` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 2,640.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1840` | 3,330,000.00 USD | 3,330,000.00 USD | 5,430.00 USD | 0.00 USD | 7,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1840` | 7,180,000.00 USD | 7,180,000.00 USD | 98,270.00 USD | 47,250.00 USD | 80,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1842` | 3,340,000.00 USD | 3,340,000.00 USD | 7,720.00 USD | 2,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1843` | 7,390,000.00 USD | 7,390,000.00 USD | 86,180.00 USD | 18,570.00 USD | 105,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1844` | 3,360,000.00 USD | 3,360,000.00 USD | 2,690.00 USD | 2,850.00 USD | 12,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1846` | 3,370,000.00 USD | 3,370,000.00 USD | 2,950.00 USD | 2,790.00 USD | 7,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1846` | 7,500,000.00 USD | 7,500,000.00 USD | 8,330.00 USD | 20,700.00 USD | 81,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1848` | 3,380,000.00 USD | 3,380,000.00 USD | 4,680.00 USD | 4,360.00 USD | 3,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1849` | 7,660,000.00 USD | 7,660,000.00 USD | 40,900.00 USD | 79,580.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1850` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 1,730.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1852` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 1,690.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1852` | 8,060,000.00 USD | 8,060,000.00 USD | 153,970.00 USD | 9,590.00 USD | 234,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1854` | 3,400,000.00 USD | 3,400,000.00 USD | 4,290.00 USD | 0.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1855` | 8,220,000.00 USD | 8,220,000.00 USD | 58,210.00 USD | 10,160.00 USD | 94,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1856` | 3,410,000.00 USD | 3,410,000.00 USD | 7,260.00 USD | 2,630.00 USD | 1,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1858` | 3,430,000.00 USD | 3,430,000.00 USD | 3,590.00 USD | 1,470.00 USD | 9,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1858` | 8,480,000.00 USD | 8,480,000.00 USD | 96,280.00 USD | 46,830.00 USD | 118,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1860` | 3,440,000.00 USD | 3,440,000.00 USD | 5,860.00 USD | 2,970.00 USD | 3,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1861` | 8,660,000.00 USD | 8,660,000.00 USD | 99,880.00 USD | 55,030.00 USD | 21,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1862` | 3,450,000.00 USD | 3,450,000.00 USD | 1,870.00 USD | 0.00 USD | 5,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1864` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 3,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1864` | 8,830,000.00 USD | 8,830,000.00 USD | 52,190.00 USD | 58,680.00 USD | 61,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1866` | 3,460,000.00 USD | 3,460,000.00 USD | 3,300.00 USD | 0.00 USD | 5,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1867` | 9,030,000.00 USD | 9,030,000.00 USD | 102,440.00 USD | 43,150.00 USD | 52,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1868` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1870` | 3,480,000.00 USD | 3,480,000.00 USD | 4,960.00 USD | 5,040.00 USD | 6,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1870` | 9,370,000.00 USD | 9,370,000.00 USD | 165,360.00 USD | 76,080.00 USD | 101,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1872` | 3,500,000.00 USD | 3,500,000.00 USD | 12,350.00 USD | 1,900.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1873` | 9,630,000.00 USD | 9,630,000.00 USD | 72,410.00 USD | 96,100.00 USD | 90,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1874` | 3,500,000.00 USD | 3,500,000.00 USD | 1,960.00 USD | 2,820.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1875` | 22,030.00 USD | 83,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1876` | 9,740,000.00 USD | 9,740,000.00 USD | 59,490.00 USD | 34,260.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1878` | 3,510,000.00 USD | 3,510,000.00 USD | 4,320.00 USD | 2,760.00 USD | 918.24 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1879` | 9,890,000.00 USD | 9,890,000.00 USD | 57,250.00 USD | 52,690.00 USD | 48,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1880` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 3,160.00 USD | 1,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1882` | 3,530,000.00 USD | 3,530,000.00 USD | 4,630.00 USD | 3,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1882` | 9,950,000.00 USD | 9,950,000.00 USD | 14,000.00 USD | 11,450.00 USD | 32,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1884` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1885` | 10,000,000.00 USD | 10,000,000.00 USD | 9,250.00 USD | 31,900.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1886` | 3,540,000.00 USD | 3,540,000.00 USD | 9,690.00 USD | 2,220.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1888` | 10,110,000.00 USD | 10,110,000.00 USD | 13,720.00 USD | 17,330.00 USD | 83,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1891` | 10,170,000.00 USD | 10,170,000.00 USD | 36,740.00 USD | 0.00 USD | 17,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1894` | 10,270,000.00 USD | 10,270,000.00 USD | 69,540.00 USD | 12,420.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1895` | 3,550.00 USD | 86,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1897` | 10,350,000.00 USD | 10,350,000.00 USD | 25,640.00 USD | 39,120.00 USD | 25,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1900` | 10,400,000.00 USD | 10,400,000.00 USD | 11,530.00 USD | 21,370.00 USD | 14,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1903` | 10,440,000.00 USD | 10,440,000.00 USD | 14,330.00 USD | 11,220.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1906` | 10,520,000.00 USD | 10,520,000.00 USD | 18,470.00 USD | 27,580.00 USD | 33,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1909` | 10,580,000.00 USD | 10,580,000.00 USD | 15,470.00 USD | 29,160.00 USD | 19,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1912` | 10,600,000.00 USD | 10,600,000.00 USD | 0.00 USD | 15,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1915` | 10,610,000.00 USD | 10,610,000.00 USD | 7,460.00 USD | 5,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1918` | 10,630,000.00 USD | 10,630,000.00 USD | 0.00 USD | 11,840.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1924` | 10,650,000.00 USD | 10,650,000.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1927` | 10,680,000.00 USD | 10,680,000.00 USD | 11,600.00 USD | 13,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1945` | 10,690,000.00 USD | 10,690,000.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1945` | 623.68 USD | 87,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1955` | 860.20 USD | 88,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1975` | 150.10 USD | 88,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1995` | 135.22 USD | 88,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2025` | 764.66 USD | 89,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2045` | 399.22 USD | 89,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2055` | 11,590.00 USD | 101,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2085` | 198.08 USD | 101,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2095` | 1,060.00 USD | 102,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2135` | 16,070.00 USD | 118,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 41,330.00 USD | 160,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2195` | 87,800.00 USD | 247,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2225` | 70,980.00 USD | 318,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 343.77 USD | 319,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2255` | 154.78 USD | 319,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 6,820.00 USD | 326,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 16,250.00 USD | 342,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 102.62 USD | 342,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 361.66 USD | 342,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 869.00 USD | 343,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2445` | 231.03 USD | 344,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2465` | 9,360.00 USD | 353,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2525` | 21,030.00 USD | 374,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2545` | 546.54 USD | 374,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 4,050.00 USD | 379,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2575` | 29,500.00 USD | 408,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 52,030.00 USD | 460,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 154.94 USD | 460,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2685` | 226.51 USD | 460,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 13,510.00 USD | 474,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 214.21 USD | 474,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 27,890.00 USD | 502,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2775` | 441.36 USD | 503,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2795` | 482.84 USD | 503,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 187.26 USD | 503,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 2,230.00 USD | 505,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 574.36 USD | 506,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2975` | 17,490.00 USD | 523,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 225.42 USD | 524,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3145` | 62,900.00 USD | 587,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 9,540.00 USD | 596,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3305` | 192.68 USD | 596,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3325` | 148.36 USD | 596,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3345` | 259.51 USD | 597,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3375` | 63,410.00 USD | 660,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0365` | 2,370,000.00 USD | 0.00 USD | 2,370.00 USD | `-78.38%` | `65,000,000,000,000.00` |
| `Live` | `Long` | `0.0375` | 2,370,000.00 USD | 0.00 USD | 1,750.00 USD | `-77.78%` | `46,685,900,000,000.00` |
| `Live` | `Long` | `0.0385` | 2,360,000.00 USD | 0.00 USD | 2,080.00 USD | `-77.19%` | `53,916,900,000,000.00` |
| `Live` | `Long` | `0.0405` | 2,360,000.00 USD | 0.00 USD | 142,410.00 USD | `-76.01%` | `3,516,409,800,000,000.00` |
| `Live` | `Long` | `0.0415` | 2,220,000.00 USD | 0.00 USD | 110.22 USD | `-75.41%` | `2,655,800,000,000.00` |
| `Live` | `Long` | `0.0425` | 2,220,000.00 USD | 0.00 USD | 170.00 USD | `-74.82%` | `4,000,000,000,000.00` |
| `Live` | `Long` | `0.0435` | 2,220,000.00 USD | 0.00 USD | 7,920.00 USD | `-74.23%` | `181,960,400,000,000.00` |
| `Live` | `Long` | `0.0465` | 2,210,000.00 USD | 0.00 USD | 333.78 USD | `-72.45%` | `7,178,000,000,000.00` |
| `Live` | `Long` | `0.0485` | 2,210,000.00 USD | 0.00 USD | 4,940.00 USD | `-71.27%` | `101,831,000,000,000.00` |
| `Live` | `Long` | `0.0495` | 2,210,000.00 USD | 0.00 USD | 251.85 USD | `-70.67%` | `5,087,900,000,000.00` |
| `Live` | `Long` | `0.0505` | 2,210,000.00 USD | 0.00 USD | 297.30 USD | `-70.08%` | `5,887,100,000,000.00` |
| `Live` | `Long` | `0.0525` | 2,210,000.00 USD | 0.00 USD | 289.43 USD | `-68.90%` | `5,513,000,000,000.00` |
| `Live` | `Long` | `0.0545` | 2,210,000.00 USD | 0.00 USD | 3,970.00 USD | `-67.71%` | `72,859,100,000,000.00` |
| `Live` | `Long` | `0.0565` | 2,200,000.00 USD | 0.00 USD | 19,600.00 USD | `-66.53%` | `346,984,000,000,000.00` |
| `Live` | `Long` | `0.0575` | 2,180,000.00 USD | 0.00 USD | 3,070.00 USD | `-65.93%` | `53,365,600,000,000.00` |
| `Live` | `Long` | `0.0635` | 2,180,000.00 USD | 0.00 USD | 256.99 USD | `-62.38%` | `4,047,100,000,000.00` |
| `Live` | `Long` | `0.0655` | 2,180,000.00 USD | 0.00 USD | 287.54 USD | `-61.19%` | `4,389,900,000,000.00` |
| `Live` | `Long` | `0.0675` | 2,180,000.00 USD | 0.00 USD | 99,790.00 USD | `-60.01%` | `1,478,385,900,000,000.00` |
| `Live` | `Long` | `0.0685` | 2,080,000.00 USD | 0.00 USD | 1,340.00 USD | `-59.42%` | `19,569,300,000,000.00` |
| `Live` | `Long` | `0.0695` | 2,080,000.00 USD | 0.00 USD | 314.45 USD | `-58.82%` | `4,524,400,000,000.00` |
| `Live` | `Long` | `0.0705` | 2,080,000.00 USD | 0.00 USD | 2,970.00 USD | `-58.23%` | `42,142,800,000,000.00` |
| `Live` | `Long` | `0.0715` | 2,070,000.00 USD | 0.00 USD | 5,840.00 USD | `-57.64%` | `81,674,400,000,000.00` |
| `Live` | `Long` | `0.0725` | 2,070,000.00 USD | 0.00 USD | 111.58 USD | `-57.05%` | `1,539,100,000,000.00` |
| `Live` | `Long` | `0.0735` | 2,070,000.00 USD | 0.00 USD | 2,440.00 USD | `-56.45%` | `33,161,800,000,000.00` |
| `Live` | `Long` | `0.0745` | 2,070,000.00 USD | 0.00 USD | 80,600.00 USD | `-55.86%` | `1,081,857,600,000,000.12` |
| `Live` | `Long` | `0.0755` | 1,980,000.00 USD | 0.00 USD | 5,290.00 USD | `-55.27%` | `70,000,000,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,980,000.00 USD | 0.00 USD | 14,690.00 USD | `-54.68%` | `192,029,300,000,000.00` |
| `Live` | `Long` | `0.0775` | 1,970,000.00 USD | 0.00 USD | 378.73 USD | `-54.08%` | `4,886,800,000,000.00` |
| `Live` | `Long` | `0.0785` | 1,960,000.00 USD | 0.00 USD | 1,520.00 USD | `-53.49%` | `19,414,500,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,960,000.00 USD | 0.00 USD | 4,630.00 USD | `-52.90%` | `58,261,800,000,000.00` |
| `Live` | `Long` | `0.0805` | 1,960,000.00 USD | 0.00 USD | 7,860.00 USD | `-52.31%` | `97,623,800,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,950,000.00 USD | 0.00 USD | 21,780.00 USD | `-51.12%` | `263,942,500,000,000.00` |
| `Live` | `Long` | `0.0835` | 1,930,000.00 USD | 0.00 USD | 112.78 USD | `-50.53%` | `1,350,600,000,000.00` |
| `Live` | `Long` | `0.0855` | 1,930,000.00 USD | 0.00 USD | 49,160.00 USD | `-49.35%` | `574,937,400,000,000.00` |
| `Live` | `Long` | `0.0875` | 1,880,000.00 USD | 0.00 USD | 787.50 USD | `-48.16%` | `9,000,000,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,880,000.00 USD | 0.00 USD | 362.62 USD | `-47.57%` | `4,097,400,000,000.00` |
| `Live` | `Long` | `0.0895` | 1,880,000.00 USD | 0.00 USD | 8,150.00 USD | `-46.98%` | `91,075,900,000,000.00` |
| `Live` | `Long` | `0.0905` | 1,870,000.00 USD | 0.00 USD | 640.05 USD | `-46.38%` | `7,072,400,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,870,000.00 USD | 0.00 USD | 2,730.00 USD | `-45.20%` | `29,514,200,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,870,000.00 USD | 0.00 USD | 24,780.00 USD | `-44.61%` | `265,020,200,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,840,000.00 USD | 0.00 USD | 40,270.00 USD | `-44.01%` | `426,141,000,000,000.00` |
| `Live` | `Long` | `0.0955` | 1,800,000.00 USD | 0.00 USD | 7,730.00 USD | `-43.42%` | `80,977,700,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,790,000.00 USD | 0.00 USD | 589.63 USD | `-42.83%` | `6,110,200,000,000.00` |
| `Live` | `Long` | `0.0975` | 1,790,000.00 USD | 0.00 USD | 253.67 USD | `-42.24%` | `2,601,700,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,790,000.00 USD | 0.00 USD | 2,810.00 USD | `-41.64%` | `28,516,700,000,000.00` |
| `Live` | `Long` | `0.0995` | 1,790,000.00 USD | 0.00 USD | 11,490.00 USD | `-41.05%` | `115,522,600,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,780,000.00 USD | 0.00 USD | 2,150.00 USD | `-40.46%` | `21,390,300,000,000.00` |
| `Live` | `Long` | `0.1025` | 1,780,000.00 USD | 0.00 USD | 1,320.00 USD | `-39.27%` | `12,920,200,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,780,000.00 USD | 0.00 USD | 802.14 USD | `-38.68%` | `7,750,100,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,770,000.00 USD | 0.00 USD | 6,230.00 USD | `-38.09%` | `59,663,200,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,770,000.00 USD | 0.00 USD | 19,080.00 USD | `-37.50%` | `180,883,700,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,750,000.00 USD | 0.00 USD | 5,880.00 USD | `-36.90%` | `55,178,100,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,740,000.00 USD | 0.00 USD | 1,060.00 USD | `-36.31%` | `9,856,300,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,740,000.00 USD | 0.00 USD | 342.59 USD | `-35.72%` | `3,157,500,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,740,000.00 USD | 0.00 USD | 534.49 USD | `-34.53%` | `4,837,000,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,740,000.00 USD | 0.00 USD | 425.50 USD | `-33.94%` | `3,816,100,000,000.00` |
| `Live` | `Long` | `0.1125` | 1,740,000.00 USD | 0.00 USD | 620.20 USD | `-33.35%` | `5,512,900,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,740,000.00 USD | 0.00 USD | 1,360.00 USD | `-32.76%` | `11,975,200,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,740,000.00 USD | 0.00 USD | 8,950.00 USD | `-32.16%` | `78,144,100,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,730,000.00 USD | 0.00 USD | 19,210.00 USD | `-31.57%` | `166,336,200,000,000.00` |
| `Live` | `Long` | `0.1165` | 1,710,000.00 USD | 0.00 USD | 11,120.00 USD | `-30.98%` | `95,487,400,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,700,000.00 USD | 0.00 USD | 3,850.00 USD | `-30.39%` | `32,724,000,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,700,000.00 USD | 0.00 USD | 26,040.00 USD | `-29.79%` | `219,739,400,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,670,000.00 USD | 0.00 USD | 2,380.00 USD | `-29.20%` | `19,920,100,000,000.00` |
| `Live` | `Long` | `0.1205` | 1,670,000.00 USD | 0.00 USD | 569.45 USD | `-28.61%` | `4,725,700,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,670,000.00 USD | 0.00 USD | 631.80 USD | `-28.02%` | `5,200,000,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,670,000.00 USD | 0.00 USD | 526.95 USD | `-27.42%` | `4,301,600,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,670,000.00 USD | 0.00 USD | 32,960.00 USD | `-26.83%` | `266,849,500,000,000.00` |
| `Live` | `Long` | `0.1245` | 1,630,000.00 USD | 0.00 USD | 2,710.00 USD | `-26.24%` | `21,778,700,000,000.00` |
| `Live` | `Long` | `0.1255` | 1,630,000.00 USD | 0.00 USD | 27,900.00 USD | `-25.65%` | `222,325,100,000,000.00` |
| `Live` | `Long` | `0.1265` | 1,600,000.00 USD | 0.00 USD | 1,200.00 USD | `-25.05%` | `9,489,700,000,000.00` |
| `Live` | `Long` | `0.1275` | 1,600,000.00 USD | 0.00 USD | 6,160.00 USD | `-24.46%` | `48,303,800,000,000.00` |
| `Live` | `Long` | `0.1285` | 1,590,000.00 USD | 0.00 USD | 11,450.00 USD | `-23.87%` | `89,089,700,000,000.00` |
| `Live` | `Long` | `0.1295` | 1,580,000.00 USD | 0.00 USD | 6,090.00 USD | `-23.28%` | `47,018,500,000,000.00` |
| `Live` | `Long` | `0.1305` | 1,580,000.00 USD | 0.00 USD | 13,600.00 USD | `-22.68%` | `104,183,100,000,000.00` |
| `Live` | `Long` | `0.1315` | 1,560,000.00 USD | 0.00 USD | 3,530.00 USD | `-22.09%` | `26,843,100,000,000.00` |
| `Live` | `Long` | `0.1325` | 1,560,000.00 USD | 0.00 USD | 14,880.00 USD | `-21.50%` | `112,281,700,000,000.00` |
| `Live` | `Long` | `0.1335` | 1,550,000.00 USD | 0.00 USD | 9,690.00 USD | `-20.91%` | `72,616,800,000,000.00` |
| `Live` | `Long` | `0.1345` | 1,540,000.00 USD | 0.00 USD | 16,420.00 USD | `-20.32%` | `122,103,800,000,000.00` |
| `Live` | `Long` | `0.1365` | 1,520,000.00 USD | 0.00 USD | 2,550.00 USD | `-19.13%` | `18,677,900,000,000.00` |
| `Live` | `Long` | `0.1375` | 1,520,000.00 USD | 0.00 USD | 3,430.00 USD | `-18.54%` | `24,971,500,000,000.00` |
| `Live` | `Long` | `0.1385` | 1,510,000.00 USD | 0.00 USD | 22,460.00 USD | `-17.95%` | `162,190,900,000,000.00` |
| `Live` | `Long` | `0.1395` | 1,490,000.00 USD | 0.00 USD | 6,100.00 USD | `-17.35%` | `43,729,900,000,000.00` |
| `Live` | `Long` | `0.1405` | 1,480,000.00 USD | 0.00 USD | 3,410.00 USD | `-16.76%` | `24,279,400,000,000.00` |
| `Live` | `Long` | `0.1415` | 1,480,000.00 USD | 0.00 USD | 11,550.00 USD | `-16.17%` | `81,618,300,000,000.00` |
| `Live` | `Long` | `0.1425` | 1,470,000.00 USD | 0.00 USD | 485,270.00 USD | `-15.58%` | `3,405,378,500,000,000.00` |
| `Live` | `Long` | `0.1435` | 984,530.00 USD | 0.00 USD | 25,070.00 USD | `-14.98%` | `174,671,900,000,000.00` |
| `Live` | `Long` | `0.1445` | 959,460.00 USD | 0.00 USD | 66,020.00 USD | `-14.39%` | `456,915,100,000,000.00` |
| `Live` | `Long` | `0.1465` | 893,440.00 USD | 0.00 USD | 31,380.00 USD | `-13.21%` | `214,196,300,000,000.00` |
| `Live` | `Long` | `0.1475` | 862,060.00 USD | 0.00 USD | 73,750.00 USD | `-12.61%` | `500,000,000,000,000.00` |
| `Live` | `Long` | `0.1485` | 788,310.00 USD | 0.00 USD | 6,110.00 USD | `-12.02%` | `41,131,300,000,000.00` |
| `Live` | `Long` | `0.1495` | 782,200.00 USD | 0.00 USD | 35,380.00 USD | `-11.43%` | `236,635,500,000,000.00` |
| `Live` | `Long` | `0.1505` | 746,820.00 USD | 0.00 USD | 170,000.00 USD | `-10.84%` | `1,129,559,400,000,000.00` |
| `Live` | `Long` | `0.1515` | 576,820.00 USD | 0.00 USD | 3,930.00 USD | `-10.24%` | `25,964,300,000,000.00` |
| `Live` | `Long` | `0.1525` | 572,890.00 USD | 0.00 USD | 42,800.00 USD | `-9.65%` | `280,626,000,000,000.00` |
| `Live` | `Long` | `0.1535` | 530,090.00 USD | 0.00 USD | 190,210.00 USD | `-9.06%` | `1,239,143,600,000,000.00` |
| `Live` | `Long` | `0.1545` | 339,890.00 USD | 0.00 USD | 26,170.00 USD | `-8.47%` | `169,378,600,000,000.00` |
| `Live` | `Long` | `0.1555` | 313,720.00 USD | 0.00 USD | 42,630.00 USD | `-7.87%` | `274,142,500,000,000.00` |
| `Live` | `Long` | `0.1565` | 271,090.00 USD | 0.00 USD | 20,840.00 USD | `-7.28%` | `133,186,799,999,999.98` |
| `Live` | `Long` | `0.1575` | 250,240.00 USD | 0.00 USD | 4,940.00 USD | `-6.69%` | `31,351,900,000,000.00` |
| `Live` | `Long` | `0.1585` | 245,310.00 USD | 0.00 USD | 5,770.00 USD | `-6.10%` | `36,412,700,000,000.00` |
| `Live` | `Long` | `0.1595` | 239,530.00 USD | 0.00 USD | 63,000.00 USD | `-5.50%` | `395,011,700,000,000.00` |
| `Live` | `Long` | `0.1605` | 176,530.00 USD | 0.00 USD | 32,770.00 USD | `-4.91%` | `204,171,400,000,000.00` |
| `Live` | `Long` | `0.1615` | 143,760.00 USD | 0.00 USD | 17,290.00 USD | `-4.32%` | `107,085,500,000,000.00` |
| `Live` | `Long` | `0.1625` | 126,470.00 USD | 0.00 USD | 106,340.00 USD | `-3.73%` | `654,420,200,000,000.00` |
| `Live` | `Long` | `0.1635` | 20,120.00 USD | 0.00 USD | 971.58 USD | `-3.13%` | `5,942,400,000,000.00` |
| `Live` | `Long` | `0.1645` | 19,150.00 USD | 0.00 USD | 6,740.00 USD | `-2.54%` | `40,963,500,000,000.00` |
| `Live` | `Long` | `0.1655` | 12,410.00 USD | 0.00 USD | 12,410.00 USD | `-1.95%` | `75,000,000,000,000.00` |
| `Live` | `Short` | `0.1765` | 1,260.00 USD | 1,260.00 USD | 0.00 USD | `+4.57%` | `7,145,900,000,000.00` |
| `Live` | `Short` | `0.1795` | 49,870.00 USD | 48,610.00 USD | 0.00 USD | `+6.35%` | `270,803,800,000,000.00` |
| `Live` | `Short` | `0.1805` | 53,000.00 USD | 3,130.00 USD | 0.00 USD | `+6.94%` | `17,317,400,000,000.00` |
| `Live` | `Short` | `0.1815` | 61,160.00 USD | 8,170.00 USD | 0.00 USD | `+7.53%` | `44,994,400,000,000.00` |
| `Live` | `Short` | `0.1825` | 61,350.00 USD | 185.09 USD | 0.00 USD | `+8.12%` | `1,014,200,000,000.00` |
| `Live` | `Short` | `0.1875` | 83,380.00 USD | 22,030.00 USD | 0.00 USD | `+11.08%` | `117,509,500,000,000.00` |
| `Live` | `Short` | `0.1895` | 86,930.00 USD | 3,550.00 USD | 0.00 USD | `+12.27%` | `18,740,300,000,000.00` |
| `Live` | `Short` | `0.1945` | 87,560.00 USD | 623.68 USD | 0.00 USD | `+15.23%` | `3,206,600,000,000.00` |
| `Live` | `Short` | `0.1955` | 88,420.00 USD | 860.20 USD | 0.00 USD | `+15.82%` | `4,400,000,000,000.00` |
| `Live` | `Short` | `0.1975` | 88,570.00 USD | 150.10 USD | 0.00 USD | `+17.01%` | `760,000,000,000.00` |
| `Live` | `Short` | `0.1995` | 88,700.00 USD | 135.22 USD | 0.00 USD | `+18.19%` | `677,800,000,000.00` |
| `Live` | `Short` | `0.2025` | 89,470.00 USD | 764.66 USD | 0.00 USD | `+19.97%` | `3,776,100,000,000.00` |
| `Live` | `Short` | `0.2045` | 89,870.00 USD | 399.22 USD | 0.00 USD | `+21.16%` | `1,952,200,000,000.00` |
| `Live` | `Short` | `0.2055` | 101,460.00 USD | 11,590.00 USD | 0.00 USD | `+21.75%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2085` | 101,660.00 USD | 198.08 USD | 0.00 USD | `+23.53%` | `950,000,000,000.00` |
| `Live` | `Short` | `0.2095` | 102,710.00 USD | 1,060.00 USD | 0.00 USD | `+24.12%` | `5,056,300,000,000.00` |
| `Live` | `Short` | `0.2135` | 118,790.00 USD | 16,070.00 USD | 0.00 USD | `+26.49%` | `75,287,100,000,000.00` |
| `Live` | `Short` | `0.2155` | 160,120.00 USD | 41,330.00 USD | 0.00 USD | `+27.67%` | `191,801,700,000,000.00` |
| `Live` | `Short` | `0.2195` | 247,920.00 USD | 87,800.00 USD | 0.00 USD | `+30.04%` | `400,000,000,000,000.00` |
| `Live` | `Short` | `0.2225` | 318,900.00 USD | 70,980.00 USD | 0.00 USD | `+31.82%` | `318,992,500,000,000.00` |
| `Live` | `Short` | `0.2235` | 319,240.00 USD | 343.77 USD | 0.00 USD | `+32.41%` | `1,538,100,000,000.00` |
| `Live` | `Short` | `0.2255` | 319,400.00 USD | 154.78 USD | 0.00 USD | `+33.60%` | `686,400,000,000.00` |
| `Live` | `Short` | `0.2295` | 326,220.00 USD | 6,820.00 USD | 0.00 USD | `+35.97%` | `29,727,000,000,000.00` |
| `Live` | `Short` | `0.2355` | 342,470.00 USD | 16,250.00 USD | 0.00 USD | `+39.52%` | `69,017,500,000,000.00` |
| `Live` | `Short` | `0.2375` | 342,570.00 USD | 102.62 USD | 0.00 USD | `+40.71%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2405` | 342,940.00 USD | 361.66 USD | 0.00 USD | `+42.48%` | `1,503,800,000,000.00` |
| `Live` | `Short` | `0.2425` | 343,810.00 USD | 869.00 USD | 0.00 USD | `+43.67%` | `3,583,500,000,000.00` |
| `Live` | `Short` | `0.2445` | 344,040.00 USD | 231.03 USD | 0.00 USD | `+44.85%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2465` | 353,400.00 USD | 9,360.00 USD | 0.00 USD | `+46.04%` | `37,972,200,000,000.00` |
| `Live` | `Short` | `0.2525` | 374,430.00 USD | 21,030.00 USD | 0.00 USD | `+49.59%` | `83,299,600,000,000.00` |
| `Live` | `Short` | `0.2545` | 374,980.00 USD | 546.54 USD | 0.00 USD | `+50.78%` | `2,147,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 379,030.00 USD | 4,050.00 USD | 0.00 USD | `+51.96%` | `15,798,700,000,000.00` |
| `Live` | `Short` | `0.2575` | 408,530.00 USD | 29,500.00 USD | 0.00 USD | `+52.56%` | `114,561,100,000,000.00` |
| `Live` | `Short` | `0.2585` | 460,550.00 USD | 52,030.00 USD | 0.00 USD | `+53.15%` | `201,260,100,000,000.00` |
| `Live` | `Short` | `0.2615` | 460,710.00 USD | 154.94 USD | 0.00 USD | `+54.93%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2685` | 460,940.00 USD | 226.51 USD | 0.00 USD | `+59.07%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2715` | 474,450.00 USD | 13,510.00 USD | 0.00 USD | `+60.85%` | `49,773,600,000,000.00` |
| `Live` | `Short` | `0.2725` | 474,660.00 USD | 214.21 USD | 0.00 USD | `+61.44%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 502,550.00 USD | 27,890.00 USD | 0.00 USD | `+62.63%` | `101,607,700,000,000.00` |
| `Live` | `Short` | `0.2775` | 503,000.00 USD | 441.36 USD | 0.00 USD | `+64.41%` | `1,590,500,000,000.00` |
| `Live` | `Short` | `0.2795` | 503,480.00 USD | 482.84 USD | 0.00 USD | `+65.59%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2915` | 503,670.00 USD | 187.26 USD | 0.00 USD | `+72.70%` | `642,400,000,000.00` |
| `Live` | `Short` | `0.2935` | 505,900.00 USD | 2,230.00 USD | 0.00 USD | `+73.88%` | `7,608,100,000,000.00` |
| `Live` | `Short` | `0.2955` | 506,470.00 USD | 574.36 USD | 0.00 USD | `+75.07%` | `1,943,700,000,000.00` |
| `Live` | `Short` | `0.2975` | 523,960.00 USD | 17,490.00 USD | 0.00 USD | `+76.25%` | `58,786,700,000,000.00` |
| `Live` | `Short` | `0.3105` | 524,190.00 USD | 225.42 USD | 0.00 USD | `+83.96%` | `726,000,000,000.00` |
| `Live` | `Short` | `0.3145` | 587,090.00 USD | 62,900.00 USD | 0.00 USD | `+86.33%` | `200,000,000,000,000.00` |
| `Live` | `Short` | `0.3295` | 596,620.00 USD | 9,540.00 USD | 0.00 USD | `+95.21%` | `28,943,600,000,000.00` |
| `Live` | `Short` | `0.3305` | 596,820.00 USD | 192.68 USD | 0.00 USD | `+95.81%` | `583,000,000,000.00` |
| `Live` | `Short` | `0.3325` | 596,970.00 USD | 148.36 USD | 0.00 USD | `+96.99%` | `446,200,000,000.00` |
| `Live` | `Short` | `0.3345` | 597,230.00 USD | 259.51 USD | 0.00 USD | `+98.18%` | `775,800,000,000.00` |
| `Live` | `Short` | `0.3375` | 660,640.00 USD | 63,410.00 USD | 0.00 USD | `+99.95%` | `187,887,700,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0355` | 783,020.00 USD | 0.00 USD | 355.00 USD | `-78.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 782,670.00 USD | 0.00 USD | 600.79 USD | `-74.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 782,070.00 USD | 0.00 USD | 353.50 USD | `-70.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 781,710.00 USD | 0.00 USD | 4,310.00 USD | `-67.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 777,400.00 USD | 0.00 USD | 475.11 USD | `-62.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 776,920.00 USD | 0.00 USD | 131.16 USD | `-61.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 776,790.00 USD | 0.00 USD | 881.45 USD | `-60.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 775,910.00 USD | 0.00 USD | 1,070.00 USD | `-60.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 774,840.00 USD | 0.00 USD | 1,400.00 USD | `-59.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 773,440.00 USD | 0.00 USD | 1,010.00 USD | `-58.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 772,430.00 USD | 0.00 USD | 4,490.00 USD | `-58.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 767,940.00 USD | 0.00 USD | 529.04 USD | `-57.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 767,410.00 USD | 0.00 USD | 2,390.00 USD | `-57.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 765,020.00 USD | 0.00 USD | 757.39 USD | `-55.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 764,260.00 USD | 0.00 USD | 1,490.00 USD | `-53.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 762,780.00 USD | 0.00 USD | 277.37 USD | `-48.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 762,500.00 USD | 0.00 USD | 262.50 USD | `-48.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 762,240.00 USD | 0.00 USD | 795.57 USD | `-47.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 761,440.00 USD | 0.00 USD | 181.00 USD | `-46.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 761,260.00 USD | 0.00 USD | 1,270.00 USD | `-40.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 759,990.00 USD | 0.00 USD | 1,550.00 USD | `-39.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 758,440.00 USD | 0.00 USD | 116.07 USD | `-36.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 758,330.00 USD | 0.00 USD | 19,070.00 USD | `-35.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 739,250.00 USD | 0.00 USD | 577.22 USD | `-34.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 738,680.00 USD | 0.00 USD | 343.50 USD | `-32.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 738,330.00 USD | 0.00 USD | 26,280.00 USD | `-30.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1175` | 712,050.00 USD | 0.00 USD | 105.75 USD | `-30.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 711,950.00 USD | 0.00 USD | 120.50 USD | `-28.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 711,830.00 USD | 0.00 USD | 83,620.00 USD | `-28.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 628,200.00 USD | 0.00 USD | 14,940.00 USD | `-26.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 613,260.00 USD | 0.00 USD | 3,010.00 USD | `-25.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 610,260.00 USD | 0.00 USD | 473.27 USD | `-24.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 609,780.00 USD | 0.00 USD | 220,940.00 USD | `-23.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 388,850.00 USD | 0.00 USD | 25,060.00 USD | `-22.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 363,790.00 USD | 0.00 USD | 5,560.00 USD | `-21.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 358,220.00 USD | 0.00 USD | 625.78 USD | `-20.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 357,600.00 USD | 0.00 USD | 8,570.00 USD | `-20.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 349,020.00 USD | 0.00 USD | 16,260.00 USD | `-19.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 332,760.00 USD | 0.00 USD | 700.86 USD | `-19.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 332,060.00 USD | 0.00 USD | 108.57 USD | `-17.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 331,950.00 USD | 0.00 USD | 349.74 USD | `-17.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 331,600.00 USD | 0.00 USD | 3,520.00 USD | `-16.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 328,080.00 USD | 0.00 USD | 127.35 USD | `-16.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 327,950.00 USD | 0.00 USD | 24,850.00 USD | `-15.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 303,100.00 USD | 0.00 USD | 702.55 USD | `-14.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 302,400.00 USD | 0.00 USD | 1,960.00 USD | `-14.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 300,440.00 USD | 0.00 USD | 27,090.00 USD | `-13.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 273,350.00 USD | 0.00 USD | 119.66 USD | `-13.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 273,230.00 USD | 0.00 USD | 2,290.00 USD | `-12.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 270,940.00 USD | 0.00 USD | 4,550.00 USD | `-12.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 266,390.00 USD | 0.00 USD | 2,420.00 USD | `-11.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 263,970.00 USD | 0.00 USD | 4,360.00 USD | `-10.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 259,610.00 USD | 0.00 USD | 702.05 USD | `-10.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1535` | 258,910.00 USD | 0.00 USD | 204.57 USD | `-9.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 258,700.00 USD | 0.00 USD | 19,280.00 USD | `-8.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 239,430.00 USD | 0.00 USD | 82,840.00 USD | `-7.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 156,580.00 USD | 0.00 USD | 718.79 USD | `-7.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1575` | 155,870.00 USD | 0.00 USD | 443.71 USD | `-6.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 155,420.00 USD | 0.00 USD | 17,200.00 USD | `-6.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 138,220.00 USD | 0.00 USD | 70,970.00 USD | `-5.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 67,250.00 USD | 0.00 USD | 16,890.00 USD | `-4.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 50,360.00 USD | 0.00 USD | 16,870.00 USD | `-4.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 33,490.00 USD | 0.00 USD | 1,730.00 USD | `-3.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 31,770.00 USD | 0.00 USD | 19,390.00 USD | `-3.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 12,380.00 USD | 0.00 USD | 3,820.00 USD | `-2.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 8,560.00 USD | 0.00 USD | 6,570.00 USD | `-1.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 1,990.00 USD | 0.00 USD | 1,440.00 USD | `-1.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 555.17 USD | 0.00 USD | 386.67 USD | `-0.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1685` | 168.50 USD | 0.00 USD | 168.50 USD | `-0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 128.48 USD | 128.48 USD | 0.00 USD | `+0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 1,920.00 USD | 1,790.00 USD | 0.00 USD | `+1.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 3,720.00 USD | 1,800.00 USD | 0.00 USD | `+1.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 13,210.00 USD | 9,490.00 USD | 0.00 USD | `+2.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 14,340.00 USD | 1,130.00 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 20,990.00 USD | 6,650.00 USD | 0.00 USD | `+3.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 22,340.00 USD | 1,350.00 USD | 0.00 USD | `+3.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 27,780.00 USD | 5,440.00 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 28,000.00 USD | 213.30 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 123,590.00 USD | 95,590.00 USD | 0.00 USD | `+5.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 150,700.00 USD | 27,110.00 USD | 0.00 USD | `+6.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 151,830.00 USD | 1,130.00 USD | 0.00 USD | `+6.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 162,190.00 USD | 10,360.00 USD | 0.00 USD | `+7.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 163,050.00 USD | 864.12 USD | 0.00 USD | `+8.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 165,580.00 USD | 2,520.00 USD | 0.00 USD | `+8.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 165,860.00 USD | 276.75 USD | 0.00 USD | `+9.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 166,010.00 USD | 149.79 USD | 0.00 USD | `+9.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 170,050.00 USD | 4,040.00 USD | 0.00 USD | `+10.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 170,200.00 USD | 147.11 USD | 0.00 USD | `+11.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 170,440.00 USD | 245.50 USD | 0.00 USD | `+11.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 171,100.00 USD | 660.73 USD | 0.00 USD | `+12.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 178,240.00 USD | 7,130.00 USD | 0.00 USD | `+12.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 178,630.00 USD | 396.42 USD | 0.00 USD | `+13.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 179,670.00 USD | 1,040.00 USD | 0.00 USD | `+14.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 186,740.00 USD | 7,070.00 USD | 0.00 USD | `+14.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 187,490.00 USD | 742.45 USD | 0.00 USD | `+15.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 192,000.00 USD | 4,520.00 USD | 0.00 USD | `+15.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 192,140.00 USD | 133.19 USD | 0.00 USD | `+16.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 192,270.00 USD | 134.20 USD | 0.00 USD | `+17.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 196,730.00 USD | 4,460.00 USD | 0.00 USD | `+17.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 197,220.00 USD | 492.19 USD | 0.00 USD | `+18.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 220,190.00 USD | 22,970.00 USD | 0.00 USD | `+18.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 221,060.00 USD | 863.97 USD | 0.00 USD | `+19.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 245,690.00 USD | 24,640.00 USD | 0.00 USD | `+19.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 245,880.00 USD | 182.72 USD | 0.00 USD | `+20.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 331,770.00 USD | 85,900.00 USD | 0.00 USD | `+21.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 333,240.00 USD | 1,470.00 USD | 0.00 USD | `+21.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 333,410.00 USD | 174.20 USD | 0.00 USD | `+22.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 335,490.00 USD | 2,080.00 USD | 0.00 USD | `+22.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 335,740.00 USD | 252.51 USD | 0.00 USD | `+24.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 350,740.00 USD | 15,000.00 USD | 0.00 USD | `+24.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 350,870.00 USD | 126.50 USD | 0.00 USD | `+25.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 351,060.00 USD | 190.80 USD | 0.00 USD | `+25.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 351,780.00 USD | 713.94 USD | 0.00 USD | `+26.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 351,990.00 USD | 213.00 USD | 0.00 USD | `+27.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 354,450.00 USD | 2,460.00 USD | 0.00 USD | `+28.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 360,720.00 USD | 6,280.00 USD | 0.00 USD | `+29.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 385,390.00 USD | 24,660.00 USD | 0.00 USD | `+30.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 385,720.00 USD | 333.91 USD | 0.00 USD | `+31.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 389,700.00 USD | 3,980.00 USD | 0.00 USD | `+32.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 390,080.00 USD | 378.55 USD | 0.00 USD | `+33.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 390,460.00 USD | 380.23 USD | 0.00 USD | `+34.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 390,640.00 USD | 185.87 USD | 0.00 USD | `+34.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 390,840.00 USD | 192.69 USD | 0.00 USD | `+35.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2295` | 391,020.00 USD | 187.50 USD | 0.00 USD | `+35.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 435,670.00 USD | 44,650.00 USD | 0.00 USD | `+36.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 435,860.00 USD | 189.14 USD | 0.00 USD | `+37.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 440,120.00 USD | 4,260.00 USD | 0.00 USD | `+37.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 441,640.00 USD | 1,520.00 USD | 0.00 USD | `+38.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 441,830.00 USD | 191.59 USD | 0.00 USD | `+38.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 463,160.00 USD | 21,320.00 USD | 0.00 USD | `+40.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 465,680.00 USD | 2,530.00 USD | 0.00 USD | `+41.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 465,880.00 USD | 195.67 USD | 0.00 USD | `+41.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 488,120.00 USD | 22,240.00 USD | 0.00 USD | `+42.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 497,420.00 USD | 9,300.00 USD | 0.00 USD | `+43.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 648,190.00 USD | 150,770.00 USD | 0.00 USD | `+45.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 666,940.00 USD | 18,750.00 USD | 0.00 USD | `+46.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 667,490.00 USD | 551.23 USD | 0.00 USD | `+46.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 668,520.00 USD | 1,030.00 USD | 0.00 USD | `+47.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 675,720.00 USD | 7,190.00 USD | 0.00 USD | `+48.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 676,010.00 USD | 289.23 USD | 0.00 USD | `+49.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 681,010.00 USD | 5,010.00 USD | 0.00 USD | `+49.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 696,900.00 USD | 15,880.00 USD | 0.00 USD | `+50.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 698,680.00 USD | 1,780.00 USD | 0.00 USD | `+50.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 702,260.00 USD | 3,580.00 USD | 0.00 USD | `+51.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 713,990.00 USD | 11,730.00 USD | 0.00 USD | `+51.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 719,150.00 USD | 5,160.00 USD | 0.00 USD | `+52.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 736,020.00 USD | 16,870.00 USD | 0.00 USD | `+53.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 765,150.00 USD | 29,130.00 USD | 0.00 USD | `+54.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2655` | 844,930.00 USD | 79,780.00 USD | 0.00 USD | `+57.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 845,210.00 USD | 272.88 USD | 0.00 USD | `+60.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 845,600.00 USD | 394.01 USD | 0.00 USD | `+63.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 865,200.00 USD | 19,600.00 USD | 0.00 USD | `+66.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 867,330.00 USD | 2,130.00 USD | 0.00 USD | `+69.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 867,910.00 USD | 579.27 USD | 0.00 USD | `+69.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 870,920.00 USD | 3,010.00 USD | 0.00 USD | `+72.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 871,020.00 USD | 101.21 USD | 0.00 USD | `+75.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 871,280.00 USD | 262.73 USD | 0.00 USD | `+75.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 872,720.00 USD | 1,440.00 USD | 0.00 USD | `+76.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 878,380.00 USD | 5,660.00 USD | 0.00 USD | `+78.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 883,810.00 USD | 5,430.00 USD | 0.00 USD | `+78.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 884,100.00 USD | 289.61 USD | 0.00 USD | `+80.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 889,270.00 USD | 5,180.00 USD | 0.00 USD | `+86.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 889,630.00 USD | 357.85 USD | 0.00 USD | `+97.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3355` | 889,880.00 USD | 251.29 USD | 0.00 USD | `+98.77%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1474` | 10,690,000.00 USD | 0.00 USD | 10,690,000.00 USD | 6,490.00 USD | 9,220.00 USD | 5,280.00 USD |
| `7D` | `0.1477` | 10,670,000.00 USD | 0.00 USD | 10,670,000.00 USD | 0.00 USD | 25,460.00 USD | 5,320.00 USD |
| `7D` | `0.1480` | 10,640,000.00 USD | 0.00 USD | 10,640,000.00 USD | 6,990.00 USD | 29,300.00 USD | 20,830.00 USD |
| `7D` | `0.1483` | 10,580,000.00 USD | 0.00 USD | 10,580,000.00 USD | 42,230.00 USD | 16,640.00 USD | 33,050.00 USD |
| `7D` | `0.1486` | 10,490,000.00 USD | 0.00 USD | 10,490,000.00 USD | 18,610.00 USD | 10,470.00 USD | 25,980.00 USD |
| `7D` | `0.1489` | 10,430,000.00 USD | 0.00 USD | 10,430,000.00 USD | 11,170.00 USD | 3,710.00 USD | 10,390.00 USD |
| `7D` | `0.1492` | 10,410,000.00 USD | 0.00 USD | 10,410,000.00 USD | 40,320.00 USD | 17,880.00 USD | 27,100.00 USD |
| `7D` | `0.1495` | 10,320,000.00 USD | 0.00 USD | 10,320,000.00 USD | 34,650.00 USD | 18,690.00 USD | 12,930.00 USD |
| `7D` | `0.1498` | 10,260,000.00 USD | 0.00 USD | 10,260,000.00 USD | 42,100.00 USD | 9,610.00 USD | 10,480.00 USD |
| `7D` | `0.1501` | 10,190,000.00 USD | 0.00 USD | 10,190,000.00 USD | 21,010.00 USD | 7,930.00 USD | 15,630.00 USD |
| `1D` | `0.1504` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 0.00 USD | 2,640.00 USD | 5,780.00 USD |
| `7D` | `0.1504` | 10,150,000.00 USD | 0.00 USD | 10,150,000.00 USD | 17,800.00 USD | 11,590.00 USD | 44,850.00 USD |
| `1D` | `0.1506` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 5,430.00 USD | 0.00 USD | 3,300.00 USD |
| `7D` | `0.1507` | 10,080,000.00 USD | 0.00 USD | 10,080,000.00 USD | 28,940.00 USD | 12,910.00 USD | 30,500.00 USD |
| `1D` | `0.1508` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 2,690.00 USD | 3,940.00 USD | 0.00 USD |
| `1D` | `0.1510` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 2,950.00 USD | 0.00 USD | 1,200.00 USD |
| `7D` | `0.1510` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 12,660.00 USD | 12,930.00 USD | 29,700.00 USD |
| `1D` | `0.1512` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 0.00 USD | 4,360.00 USD | 1,300.00 USD |
| `7D` | `0.1513` | 9,950,000.00 USD | 0.00 USD | 9,950,000.00 USD | 32,900.00 USD | 17,610.00 USD | 38,800.00 USD |
| `1D` | `0.1514` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 0.00 USD | 1,730.00 USD | 1,300.00 USD |
| `1D` | `0.1516` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 0.00 USD | 1,690.00 USD | 0.00 USD |
| `7D` | `0.1516` | 9,860,000.00 USD | 0.00 USD | 9,860,000.00 USD | 54,550.00 USD | 0.00 USD | 43,840.00 USD |
| `1D` | `0.1518` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 11,550.00 USD | 2,630.00 USD | 5,910.00 USD |
| `7D` | `0.1519` | 9,760,000.00 USD | 0.00 USD | 9,760,000.00 USD | 37,430.00 USD | 19,520.00 USD | 70,660.00 USD |
| `1D` | `0.1520` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 3,590.00 USD | 1,470.00 USD | 9,840.00 USD |
| `1D` | `0.1522` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 5,860.00 USD | 2,970.00 USD | 3,580.00 USD |
| `7D` | `0.1522` | 9,630,000.00 USD | 0.00 USD | 9,630,000.00 USD | 49,800.00 USD | 9,640.00 USD | 24,710.00 USD |
| `1D` | `0.1524` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 1,870.00 USD | 0.00 USD | 5,050.00 USD |
| `7D` | `0.1525` | 9,550,000.00 USD | 0.00 USD | 9,550,000.00 USD | 25,790.00 USD | 13,700.00 USD | 19,910.00 USD |
| `1D` | `0.1526` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 3,300.00 USD | 0.00 USD | 8,410.00 USD |
| `1D` | `0.1528` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `0.1528` | 9,490,000.00 USD | 0.00 USD | 9,490,000.00 USD | 75,690.00 USD | 27,110.00 USD | 27,860.00 USD |
| `1D` | `0.1530` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 4,960.00 USD | 5,040.00 USD | 6,730.00 USD |
| `7D` | `0.1531` | 9,360,000.00 USD | 0.00 USD | 9,360,000.00 USD | 35,030.00 USD | 8,400.00 USD | 16,920.00 USD |
| `1D` | `0.1532` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 12,350.00 USD | 1,900.00 USD | 3,140.00 USD |
| `1D` | `0.1534` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 1,960.00 USD | 2,820.00 USD | 2,290.00 USD |
| `7D` | `0.1534` | 9,300,000.00 USD | 0.00 USD | 9,300,000.00 USD | 15,780.00 USD | 17,430.00 USD | 20,220.00 USD |
| `1D` | `0.1536` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 4,320.00 USD | 2,760.00 USD | 918.24 USD |
| `7D` | `0.1537` | 9,240,000.00 USD | 0.00 USD | 9,240,000.00 USD | 37,050.00 USD | 11,700.00 USD | 10,520.00 USD |
| `1D` | `0.1538` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 0.00 USD | 3,160.00 USD | 1,240.00 USD |
| `1D` | `0.1540` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 4,630.00 USD | 3,480.00 USD | 0.00 USD |
| `7D` | `0.1540` | 9,190,000.00 USD | 0.00 USD | 9,190,000.00 USD | 14,000.00 USD | 6,530.00 USD | 5,070.00 USD |
| `1D` | `0.1542` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 4,490.00 USD |
| `7D` | `0.1543` | 9,160,000.00 USD | 0.00 USD | 9,160,000.00 USD | 9,250.00 USD | 3,590.00 USD | 4,670.00 USD |
| `1D` | `0.1544` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 13,270.00 USD | 3,200.00 USD | 1,730.00 USD |
| `1D` | `0.1546` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 0.00 USD | 6,820.00 USD | 0.00 USD |
| `7D` | `0.1546` | 9,140,000.00 USD | 0.00 USD | 9,140,000.00 USD | 0.00 USD | 0.00 USD | 5,620.00 USD |
| `1D` | `0.1548` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 1,140.00 USD | 1,840.00 USD | 1,070.00 USD |
| `7D` | `0.1549` | 9,140,000.00 USD | 0.00 USD | 9,140,000.00 USD | 11,570.00 USD | 6,940.00 USD | 0.00 USD |
| `1D` | `0.1550` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 4,810.00 USD | 2,620.00 USD | 959.69 USD |
| `1D` | `0.1552` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 4,500.00 USD | 1,530.00 USD | 2,930.00 USD |
| `7D` | `0.1552` | 9,120,000.00 USD | 0.00 USD | 9,120,000.00 USD | 23,110.00 USD | 7,730.00 USD | 0.00 USD |
| `1D` | `0.1554` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 9,910.00 USD | 19,270.00 USD | 7,190.00 USD |
| `7D` | `0.1555` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 0.00 USD | 0.00 USD | 6,470.00 USD |
| `1D` | `0.1556` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 0.00 USD | 3,410.00 USD | 3,250.00 USD |
| `1D` | `0.1558` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 5,580.00 USD |
| `7D` | `0.1558` | 9,080,000.00 USD | 0.00 USD | 9,080,000.00 USD | 0.00 USD | 10,990.00 USD | 10,800.00 USD |
| `1D` | `0.1560` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 5,460.00 USD | 11,300.00 USD | 2,210.00 USD |
| `7D` | `0.1561` | 9,060,000.00 USD | 0.00 USD | 9,060,000.00 USD | 0.00 USD | 5,070.00 USD | 0.00 USD |
| `1D` | `0.1562` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 3,050.00 USD | 1,050.00 USD | 6,110.00 USD |
| `1D` | `0.1564` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 6,880.00 USD | 5,200.00 USD | 13,450.00 USD |
| `7D` | `0.1564` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 24,300.00 USD | 28,690.00 USD | 21,180.00 USD |
| `1D` | `0.1566` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 38,690.00 USD | 6,370.00 USD | 11,550.00 USD |
| `7D` | `0.1567` | 8,980,000.00 USD | 0.00 USD | 8,980,000.00 USD | 41,770.00 USD | 15,360.00 USD | 15,440.00 USD |
| `1D` | `0.1568` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 13,610.00 USD | 26,770.00 USD | 7,030.00 USD |
| `1D` | `0.1570` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 19,150.00 USD | 11,300.00 USD | 2,740.00 USD |
| `7D` | `0.1570` | 8,910,000.00 USD | 0.00 USD | 8,910,000.00 USD | 0.00 USD | 5,100.00 USD | 11,900.00 USD |
| `1D` | `0.1572` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 26,510.00 USD | 7,430.00 USD | 15,100.00 USD |
| `7D` | `0.1573` | 8,890,000.00 USD | 0.00 USD | 8,890,000.00 USD | 58,830.00 USD | 56,100.00 USD | 25,810.00 USD |
| `1D` | `0.1574` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 21,250.00 USD | 6,090.00 USD | 1,670.00 USD |
| `1D` | `0.1576` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 13,180.00 USD | 26,110.00 USD | 11,770.00 USD |
| `7D` | `0.1576` | 8,750,000.00 USD | 0.00 USD | 8,750,000.00 USD | 26,600.00 USD | 102,190.00 USD | 54,870.00 USD |
| `1D` | `0.1578` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 62,820.00 USD | 51,020.00 USD | 17,730.00 USD |
| `7D` | `0.1579` | 8,570,000.00 USD | 0.00 USD | 8,570,000.00 USD | 101,500.00 USD | 95,190.00 USD | 42,790.00 USD |
| `1D` | `0.1580` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 25,030.00 USD | 0.00 USD | 18,130.00 USD |
| `1D` | `0.1582` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 17,260.00 USD | 12,250.00 USD | 9,600.00 USD |
| `7D` | `0.1582` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 56,130.00 USD | 13,480.00 USD | 89,190.00 USD |
| `1D` | `0.1584` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 24,310.00 USD | 2,750.00 USD | 8,730.00 USD |
| `7D` | `0.1585` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 87,110.00 USD | 50,340.00 USD | 75,690.00 USD |
| `1D` | `0.1586` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 6,650.00 USD | 15,680.00 USD | 12,960.00 USD |
| `1D` | `0.1588` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 10,190.00 USD | 13,850.00 USD | 2,500.00 USD |
| `7D` | `0.1588` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 34,830.00 USD | 30,030.00 USD | 41,060.00 USD |
| `1D` | `0.1590` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 3,300.00 USD | 19,810.00 USD | 5,770.00 USD |
| `7D` | `0.1591` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 110,640.00 USD | 49,670.00 USD | 60,600.00 USD |
| `1D` | `0.1592` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 26,740.00 USD | 6,320.00 USD | 13,210.00 USD |
| `1D` | `0.1594` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 43,860.00 USD | 13,170.00 USD | 13,130.00 USD |
| `7D` | `0.1594` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 85,560.00 USD | 39,260.00 USD | 102,800.00 USD |
| `1D` | `0.1596` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 6,250.00 USD | 6,020.00 USD | 32,370.00 USD |
| `7D` | `0.1597` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 228,850.00 USD | 96,110.00 USD | 102,580.00 USD |
| `1D` | `0.1598` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 61,390.00 USD | 16,990.00 USD | 29,700.00 USD |
| `1D` | `0.1600` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 16,450.00 USD | 22,650.00 USD | 11,300.00 USD |
| `7D` | `0.1600` | 6,970,000.00 USD | 0.00 USD | 6,970,000.00 USD | 105,580.00 USD | 38,830.00 USD | 76,540.00 USD |
| `1D` | `0.1602` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 47,310.00 USD | 24,170.00 USD | 0.00 USD |
| `7D` | `0.1603` | 6,750,000.00 USD | 0.00 USD | 6,750,000.00 USD | 62,240.00 USD | 54,840.00 USD | 81,850.00 USD |
| `1D` | `0.1604` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 23,170.00 USD | 6,610.00 USD | 17,830.00 USD |
| `1D` | `0.1606` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 35,830.00 USD | 16,070.00 USD | 22,960.00 USD |
| `7D` | `0.1606` | 6,550,000.00 USD | 0.00 USD | 6,550,000.00 USD | 211,140.00 USD | 149,480.00 USD | 227,860.00 USD |
| `1D` | `0.1608` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 42,100.00 USD | 30,480.00 USD | 18,140.00 USD |
| `7D` | `0.1609` | 5,960,000.00 USD | 0.00 USD | 5,960,000.00 USD | 92,990.00 USD | 229,060.00 USD | 182,360.00 USD |
| `1D` | `0.1610` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 88,820.00 USD | 91,470.00 USD | 29,280.00 USD |
| `1D` | `0.1612` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 79,330.00 USD | 54,580.00 USD | 50,940.00 USD |
| `7D` | `0.1612` | 5,460,000.00 USD | 0.00 USD | 5,460,000.00 USD | 281,220.00 USD | 247,430.00 USD | 159,570.00 USD |
| `1D` | `0.1614` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 20,150.00 USD | 12,260.00 USD | 25,110.00 USD |
| `7D` | `0.1615` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 293,210.00 USD | 107,900.00 USD | 374,650.00 USD |
| `1D` | `0.1616` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 41,700.00 USD | 20,020.00 USD | 23,560.00 USD |
| `1D` | `0.1618` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 46,050.00 USD | 12,180.00 USD | 22,820.00 USD |
| `7D` | `0.1618` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 310,070.00 USD | 128,930.00 USD | 310,430.00 USD |
| `1D` | `0.1620` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 46,800.00 USD | 49,990.00 USD | 43,840.00 USD |
| `7D` | `0.1621` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 241,340.00 USD | 148,260.00 USD | 322,640.00 USD |
| `1D` | `0.1622` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 50,590.00 USD | 31,260.00 USD | 27,280.00 USD |
| `1D` | `0.1624` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 9,570.00 USD | 48,390.00 USD | 11,450.00 USD |
| `7D` | `0.1624` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 375,170.00 USD | 135,840.00 USD | 119,380.00 USD |
| `1D` | `0.1626` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 13,530.00 USD | 0.00 USD | 20,260.00 USD |
| `7D` | `0.1627` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 291,760.00 USD | 0.00 USD | 12,330.00 USD |
| `1D` | `0.1628` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 14,220.00 USD | 29,880.00 USD | 12,840.00 USD |
| `1D` | `0.1630` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | 3,150.00 USD | 11,810.00 USD |
| `7D` | `0.1630` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 9,210.00 USD | 0.00 USD | 8,530.00 USD |
| `1D` | `0.1632` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 12,400.00 USD | 19,630.00 USD | 12,340.00 USD |
| `1D` | `0.1634` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 32,300.00 USD | 6,390.00 USD | 7,850.00 USD |
| `1D` | `0.1636` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 4,900.00 USD | 9,310.00 USD | 12,610.00 USD |
| `7D` | `0.1636` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 0.00 USD | 13,670.00 USD | 21,360.00 USD |
| `1D` | `0.1638` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 9,410.00 USD | 13,220.00 USD | 34,190.00 USD |
| `7D` | `0.1639` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 62,410.00 USD |
| `1D` | `0.1640` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 7,360.00 USD | 6,090.00 USD | 10,340.00 USD |
| `1D` | `0.1642` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 20,760.00 USD | 17,890.00 USD | 8,700.00 USD |
| `7D` | `0.1642` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 22,480.00 USD | 29,240.00 USD | 26,230.00 USD |
| `1D` | `0.1644` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 4,830.00 USD | 7,360.00 USD | 23,700.00 USD |
| `7D` | `0.1645` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 34,760.00 USD | 8,990.00 USD | 7,650.00 USD |
| `1D` | `0.1646` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 40,030.00 USD | 24,740.00 USD | 10,850.00 USD |
| `1D` | `0.1648` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 4,570.00 USD | 16,250.00 USD | 15,850.00 USD |
| `7D` | `0.1648` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD |
| `1D` | `0.1650` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 7,830.00 USD | 20,170.00 USD | 3,230.00 USD |
| `7D` | `0.1651` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 51,100.00 USD |
| `1D` | `0.1652` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 42,530.00 USD | 0.00 USD | 34,610.00 USD |
| `1D` | `0.1654` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 31,300.00 USD | 27,430.00 USD | 46,470.00 USD |
| `7D` | `0.1654` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 60,050.00 USD | 31,800.00 USD | 33,760.00 USD |
| `1D` | `0.1656` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 38,480.00 USD | 40,450.00 USD | 25,300.00 USD |
| `7D` | `0.1657` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 10,890.00 USD | 0.00 USD | 16,170.00 USD |
| `1D` | `0.1658` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 25,050.00 USD | 14,850.00 USD | 41,900.00 USD |
| `1D` | `0.1660` | 964,090.00 USD | 0.00 USD | 964,090.00 USD | 27,070.00 USD | 11,150.00 USD | 47,860.00 USD |
| `7D` | `0.1660` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 29,890.00 USD | 11,020.00 USD | 33,680.00 USD |
| `1D` | `0.1662` | 878,010.00 USD | 0.00 USD | 878,010.00 USD | 20,300.00 USD | 11,720.00 USD | 36,920.00 USD |
| `7D` | `0.1663` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 86,050.00 USD | 51,000.00 USD | 75,880.00 USD |
| `1D` | `0.1664` | 809,060.00 USD | 0.00 USD | 809,060.00 USD | 31,630.00 USD | 47,390.00 USD | 46,530.00 USD |
| `1D` | `0.1666` | 683,510.00 USD | 0.00 USD | 683,510.00 USD | 41,260.00 USD | 50,440.00 USD | 37,490.00 USD |
| `7D` | `0.1666` | 856,340.00 USD | 0.00 USD | 856,340.00 USD | 49,590.00 USD | 32,780.00 USD | 28,810.00 USD |
| `1D` | `0.1668` | 554,310.00 USD | 0.00 USD | 554,310.00 USD | 102,890.00 USD | 28,980.00 USD | 20,820.00 USD |
| `7D` | `0.1669` | 745,150.00 USD | 0.00 USD | 745,150.00 USD | 11,410.00 USD | 64,050.00 USD | 42,720.00 USD |
| `1D` | `0.1670` | 401,620.00 USD | 0.00 USD | 401,620.00 USD | 25,410.00 USD | 21,810.00 USD | 22,000.00 USD |
| `1D` | `0.1672` | 332,390.00 USD | 0.00 USD | 332,390.00 USD | 42,030.00 USD | 31,130.00 USD | 18,410.00 USD |
| `7D` | `0.1672` | 626,980.00 USD | 0.00 USD | 626,980.00 USD | 70,540.00 USD | 38,070.00 USD | 0.00 USD |
| `7D` | `0.1675` | 518,370.00 USD | 0.00 USD | 518,370.00 USD | 64,490.00 USD | 105,910.00 USD | 0.00 USD |
| `1D` | `0.1676` | 240,820.00 USD | 0.00 USD | 240,820.00 USD | 14,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1678` | 347,970.00 USD | 0.00 USD | 347,970.00 USD | 71,860.00 USD | 79,930.00 USD | 0.00 USD |
| `1D` | `0.1680` | 226,200.00 USD | 0.00 USD | 226,200.00 USD | 75,420.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1681` | 196,180.00 USD | 0.00 USD | 196,180.00 USD | 69,520.00 USD | 36,390.00 USD | 15,310.00 USD |
| `1D` | `0.1682` | 150,780.00 USD | 0.00 USD | 150,780.00 USD | 74,980.00 USD | 0.00 USD | 23,570.00 USD |
| `1D` | `0.1684` | 52,230.00 USD | 0.00 USD | 52,230.00 USD | 13,810.00 USD | 26,600.00 USD | 11,810.00 USD |
| `7D` | `0.1684` | 74,950.00 USD | 0.00 USD | 74,950.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD |
| `7D` | `0.1686` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1688` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1690` | 25,360.00 USD | 25,360.00 USD | 0.00 USD | 18,380.00 USD | 6,980.00 USD | 0.00 USD |
| `7D` | `0.1690` | 38,670.00 USD | 38,670.00 USD | 0.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD |
| `1D` | `0.1692` | 128,460.00 USD | 128,460.00 USD | 0.00 USD | 36,940.00 USD | 66,160.00 USD | 0.00 USD |
| `7D` | `0.1693` | 92,520.00 USD | 92,520.00 USD | 0.00 USD | 21,780.00 USD | 32,070.00 USD | 0.00 USD |
| `1D` | `0.1694` | 150,750.00 USD | 150,750.00 USD | 0.00 USD | 0.00 USD | 22,300.00 USD | 0.00 USD |
| `7D` | `0.1696` | 207,880.00 USD | 207,880.00 USD | 0.00 USD | 0.00 USD | 87,350.00 USD | 28,010.00 USD |
| `1D` | `0.1698` | 214,900.00 USD | 214,900.00 USD | 0.00 USD | 7,460.00 USD | 56,690.00 USD | 0.00 USD |
| `7D` | `0.1699` | 252,030.00 USD | 252,030.00 USD | 0.00 USD | 0.00 USD | 25,330.00 USD | 18,830.00 USD |
| `1D` | `0.1702` | 225,130.00 USD | 225,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,240.00 USD |
| `7D` | `0.1702` | 321,740.00 USD | 321,740.00 USD | 0.00 USD | 22,820.00 USD | 46,880.00 USD | 0.00 USD |
| `1D` | `0.1704` | 239,550.00 USD | 239,550.00 USD | 0.00 USD | 0.00 USD | 14,420.00 USD | 0.00 USD |
| `1D` | `0.1706` | 272,150.00 USD | 272,150.00 USD | 0.00 USD | 22,060.00 USD | 6,390.00 USD | 4,150.00 USD |
| `1D` | `0.1708` | 350,330.00 USD | 350,330.00 USD | 0.00 USD | 15,910.00 USD | 62,270.00 USD | 0.00 USD |
| `7D` | `0.1708` | 411,920.00 USD | 411,920.00 USD | 0.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD |
| `1D` | `0.1710` | 355,660.00 USD | 355,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,330.00 USD |
| `1D` | `0.1712` | 370,700.00 USD | 370,700.00 USD | 0.00 USD | 0.00 USD | 15,040.00 USD | 0.00 USD |
| `7D` | `0.1714` | 453,940.00 USD | 453,940.00 USD | 0.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD |
| `1D` | `0.1716` | 396,300.00 USD | 396,300.00 USD | 0.00 USD | 0.00 USD | 25,600.00 USD | 0.00 USD |
| `1D` | `0.1718` | 414,170.00 USD | 414,170.00 USD | 0.00 USD | 9,350.00 USD | 8,520.00 USD | 0.00 USD |
| `1D` | `0.1720` | 481,630.00 USD | 481,630.00 USD | 0.00 USD | 67,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1720` | 608,300.00 USD | 608,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 154,360.00 USD |
| `1D` | `0.1722` | 561,190.00 USD | 561,190.00 USD | 0.00 USD | 34,600.00 USD | 16,860.00 USD | 28,100.00 USD |
| `7D` | `0.1723` | 896,750.00 USD | 896,750.00 USD | 0.00 USD | 100,390.00 USD | 0.00 USD | 188,060.00 USD |
| `1D` | `0.1724` | 582,750.00 USD | 582,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21,560.00 USD |
| `1D` | `0.1726` | 587,450.00 USD | 587,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,700.00 USD |
| `1D` | `0.1728` | 606,270.00 USD | 606,270.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD |
| `7D` | `0.1729` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 137,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1732` | 616,330.00 USD | 616,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,060.00 USD |
| `7D` | `0.1732` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 338,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1736` | 640,810.00 USD | 640,810.00 USD | 0.00 USD | 14,970.00 USD | 9,510.00 USD | 0.00 USD |
| `1D` | `0.1738` | 655,390.00 USD | 655,390.00 USD | 0.00 USD | 14,580.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1738` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 83,810.00 USD |
| `1D` | `0.1740` | 665,040.00 USD | 665,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,640.00 USD |
| `1D` | `0.1742` | 675,000.00 USD | 675,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,960.00 USD |
| `1D` | `0.1744` | 680,120.00 USD | 680,120.00 USD | 0.00 USD | 0.00 USD | 2,460.00 USD | 2,660.00 USD |
| `7D` | `0.1744` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1746` | 698,150.00 USD | 698,150.00 USD | 0.00 USD | 8,530.00 USD | 0.00 USD | 9,500.00 USD |
| `1D` | `0.1748` | 792,060.00 USD | 792,060.00 USD | 0.00 USD | 55,280.00 USD | 2,280.00 USD | 36,350.00 USD |
| `1D` | `0.1750` | 822,210.00 USD | 822,210.00 USD | 0.00 USD | 24,790.00 USD | 0.00 USD | 5,360.00 USD |
| `7D` | `0.1750` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 167,500.00 USD |
| `1D` | `0.1752` | 873,340.00 USD | 873,340.00 USD | 0.00 USD | 23,850.00 USD | 0.00 USD | 27,280.00 USD |
| `7D` | `0.1753` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 191,160.00 USD |
| `1D` | `0.1754` | 911,990.00 USD | 911,990.00 USD | 0.00 USD | 14,290.00 USD | 8,430.00 USD | 15,940.00 USD |
| `1D` | `0.1756` | 969,910.00 USD | 969,910.00 USD | 0.00 USD | 4,060.00 USD | 19,210.00 USD | 34,640.00 USD |
| `7D` | `0.1756` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 88,730.00 USD | 0.00 USD | 106,270.00 USD |
| `1D` | `0.1758` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 64,490.00 USD | 20,940.00 USD | 27,320.00 USD |
| `7D` | `0.1759` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 217,800.00 USD | 38,670.00 USD | 0.00 USD |
| `1D` | `0.1760` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 20,820.00 USD | 76,400.00 USD | 15,650.00 USD |
| `1D` | `0.1762` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 54,910.00 USD | 11,990.00 USD | 60,400.00 USD |
| `7D` | `0.1762` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 289,660.00 USD | 180,810.00 USD | 32,350.00 USD |
| `1D` | `0.1764` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 12,650.00 USD | 25,840.00 USD | 35,660.00 USD |
| `7D` | `0.1765` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 154,540.00 USD | 166,180.00 USD | 48,870.00 USD |
| `1D` | `0.1766` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 7,570.00 USD | 3,150.00 USD | 40,840.00 USD |
| `1D` | `0.1768` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 32,300.00 USD | 83,210.00 USD | 29,690.00 USD |
| `7D` | `0.1768` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 161,560.00 USD | 138,440.00 USD | 23,040.00 USD |
| `1D` | `0.1770` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 36,140.00 USD | 14,270.00 USD | 20,210.00 USD |
| `7D` | `0.1771` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 69,030.00 USD | 138,810.00 USD | 21,360.00 USD |
| `1D` | `0.1772` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 7,290.00 USD | 14,560.00 USD | 22,840.00 USD |
| `1D` | `0.1774` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 35,970.00 USD | 21,330.00 USD | 7,600.00 USD |
| `7D` | `0.1774` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 148,780.00 USD | 90,530.00 USD | 0.00 USD |
| `1D` | `0.1776` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 73,100.00 USD | 12,480.00 USD | 13,410.00 USD |
| `7D` | `0.1777` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 67,350.00 USD | 40,700.00 USD | 59,520.00 USD |
| `1D` | `0.1778` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 23,220.00 USD | 77,730.00 USD | 11,450.00 USD |
| `1D` | `0.1780` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 4,270.00 USD | 1,060.00 USD | 13,680.00 USD |
| `7D` | `0.1780` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 52,730.00 USD | 38,910.00 USD | 97,990.00 USD |
| `1D` | `0.1782` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 46,310.00 USD | 13,190.00 USD | 47,040.00 USD |
| `7D` | `0.1783` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 117,540.00 USD | 56,000.00 USD | 21,910.00 USD |
| `1D` | `0.1784` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 82,580.00 USD | 19,630.00 USD | 8,300.00 USD |
| `1D` | `0.1786` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 18,920.00 USD | 28,240.00 USD | 18,250.00 USD |
| `7D` | `0.1786` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 129,440.00 USD | 55,090.00 USD | 14,040.00 USD |
| `1D` | `0.1788` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 30,950.00 USD | 40,790.00 USD | 25,380.00 USD |
| `7D` | `0.1789` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 48,810.00 USD | 7,150.00 USD | 0.00 USD |
| `1D` | `0.1790` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 36,940.00 USD | 8,720.00 USD | 10,090.00 USD |
| `1D` | `0.1792` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 15,540.00 USD | 20,480.00 USD |
| `7D` | `0.1792` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 134,000.00 USD | 39,820.00 USD | 3,940.00 USD |
| `1D` | `0.1794` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 36,860.00 USD | 48,460.00 USD | 3,990.00 USD |
| `7D` | `0.1795` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 17,130.00 USD | 19,870.00 USD | 44,450.00 USD |
| `1D` | `0.1796` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 20,690.00 USD | 15,920.00 USD | 32,990.00 USD |
| `1D` | `0.1798` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 6,590.00 USD | 12,950.00 USD | 15,390.00 USD |
| `7D` | `0.1798` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 6,240.00 USD | 27,010.00 USD |
| `1D` | `0.1800` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 5,820.00 USD | 1,930.00 USD | 13,950.00 USD |
| `7D` | `0.1801` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 6,490.00 USD | 40,090.00 USD | 46,450.00 USD |
| `1D` | `0.1802` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 15,140.00 USD | 34,770.00 USD | 14,760.00 USD |
| `1D` | `0.1804` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 4,260.00 USD | 3,940.00 USD | 15,380.00 USD |
| `7D` | `0.1804` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 28,790.00 USD | 27,450.00 USD | 14,740.00 USD |
| `1D` | `0.1806` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 18,420.00 USD | 11,530.00 USD | 9,040.00 USD |
| `7D` | `0.1807` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 11,410.00 USD | 63,170.00 USD | 67,160.00 USD |
| `1D` | `0.1808` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 24,170.00 USD | 21,780.00 USD | 28,810.00 USD |
| `1D` | `0.1810` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 21,750.00 USD | 8,780.00 USD | 8,830.00 USD |
| `7D` | `0.1810` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 79,380.00 USD | 30,940.00 USD | 12,950.00 USD |
| `1D` | `0.1812` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 37,500.00 USD | 40,830.00 USD | 33,150.00 USD |
| `7D` | `0.1813` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 32,530.00 USD | 15,780.00 USD | 56,130.00 USD |
| `1D` | `0.1814` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 7,290.00 USD | 3,320.00 USD | 11,550.00 USD |
| `1D` | `0.1816` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 28,660.00 USD | 0.00 USD | 17,940.00 USD |
| `7D` | `0.1816` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 46,430.00 USD | 21,200.00 USD | 25,980.00 USD |
| `1D` | `0.1818` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 13,970.00 USD | 11,780.00 USD | 14,690.00 USD |
| `7D` | `0.1819` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 65,350.00 USD | 24,720.00 USD | 43,100.00 USD |
| `1D` | `0.1820` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 21,220.00 USD | 17,800.00 USD | 3,000.00 USD |
| `1D` | `0.1822` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 8,490.00 USD | 11,090.00 USD | 11,390.00 USD |
| `7D` | `0.1822` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 46,760.00 USD | 36,230.00 USD | 92,280.00 USD |
| `1D` | `0.1824` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 11,560.00 USD | 8,890.00 USD | 8,590.00 USD |
| `7D` | `0.1825` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 61,720.00 USD | 17,120.00 USD | 12,140.00 USD |
| `1D` | `0.1826` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 21,440.00 USD | 6,860.00 USD | 1,990.00 USD |
| `1D` | `0.1828` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,530.00 USD |
| `7D` | `0.1828` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 51,470.00 USD | 24,320.00 USD | 69,840.00 USD |
| `1D` | `0.1830` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 4,510.00 USD | 5,340.00 USD |
| `7D` | `0.1831` | 6,460,000.00 USD | 6,460,000.00 USD | 0.00 USD | 85,970.00 USD | 21,930.00 USD | 63,170.00 USD |
| `1D` | `0.1832` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,630.00 USD |
| `1D` | `0.1834` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 728.16 USD |
| `7D` | `0.1834` | 6,720,000.00 USD | 6,720,000.00 USD | 0.00 USD | 165,640.00 USD | 47,980.00 USD | 51,750.00 USD |
| `1D` | `0.1836` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 3,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1837` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 72,930.00 USD | 76,140.00 USD | 83,480.00 USD |
| `1D` | `0.1838` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 0.00 USD | 2,640.00 USD | 5,780.00 USD |
| `1D` | `0.1840` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 5,430.00 USD | 0.00 USD | 7,910.00 USD |
| `7D` | `0.1840` | 7,180,000.00 USD | 7,180,000.00 USD | 0.00 USD | 98,270.00 USD | 47,250.00 USD | 80,190.00 USD |
| `1D` | `0.1842` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 7,720.00 USD | 2,690.00 USD | 0.00 USD |
| `7D` | `0.1843` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 86,180.00 USD | 18,570.00 USD | 105,350.00 USD |
| `1D` | `0.1844` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 2,690.00 USD | 2,850.00 USD | 12,790.00 USD |
| `1D` | `0.1846` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 2,950.00 USD | 2,790.00 USD | 7,930.00 USD |
| `7D` | `0.1846` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 8,330.00 USD | 20,700.00 USD | 81,550.00 USD |
| `1D` | `0.1848` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 4,680.00 USD | 4,360.00 USD | 3,310.00 USD |
| `7D` | `0.1849` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 40,900.00 USD | 79,580.00 USD | 38,800.00 USD |
| `1D` | `0.1850` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD | 1,300.00 USD |
| `1D` | `0.1852` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 1,690.00 USD | 4,440.00 USD |
| `7D` | `0.1852` | 8,060,000.00 USD | 8,060,000.00 USD | 0.00 USD | 153,970.00 USD | 9,590.00 USD | 234,380.00 USD |
| `1D` | `0.1854` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 4,290.00 USD | 0.00 USD | 4,220.00 USD |
| `7D` | `0.1855` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 58,210.00 USD | 10,160.00 USD | 94,330.00 USD |
| `1D` | `0.1856` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 7,260.00 USD | 2,630.00 USD | 1,690.00 USD |
| `1D` | `0.1858` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 3,590.00 USD | 1,470.00 USD | 9,840.00 USD |
| `7D` | `0.1858` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 96,280.00 USD | 46,830.00 USD | 118,720.00 USD |
| `1D` | `0.1860` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 5,860.00 USD | 2,970.00 USD | 3,580.00 USD |
| `7D` | `0.1861` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 99,880.00 USD | 55,030.00 USD | 21,120.00 USD |
| `1D` | `0.1862` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD | 5,050.00 USD |
| `1D` | `0.1864` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,270.00 USD |
| `7D` | `0.1864` | 8,830,000.00 USD | 8,830,000.00 USD | 0.00 USD | 52,190.00 USD | 58,680.00 USD | 61,380.00 USD |
| `1D` | `0.1866` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 3,300.00 USD | 0.00 USD | 5,140.00 USD |
| `7D` | `0.1867` | 9,030,000.00 USD | 9,030,000.00 USD | 0.00 USD | 102,440.00 USD | 43,150.00 USD | 52,870.00 USD |
| `1D` | `0.1868` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,170.00 USD |
| `1D` | `0.1870` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 4,960.00 USD | 5,040.00 USD | 6,730.00 USD |
| `7D` | `0.1870` | 9,370,000.00 USD | 9,370,000.00 USD | 0.00 USD | 165,360.00 USD | 76,080.00 USD | 101,310.00 USD |
| `1D` | `0.1872` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 12,350.00 USD | 1,900.00 USD | 3,140.00 USD |
| `7D` | `0.1873` | 9,630,000.00 USD | 9,630,000.00 USD | 0.00 USD | 72,410.00 USD | 96,100.00 USD | 90,790.00 USD |
| `1D` | `0.1874` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 1,960.00 USD | 2,820.00 USD | 2,290.00 USD |
| `7D` | `0.1876` | 9,740,000.00 USD | 9,740,000.00 USD | 0.00 USD | 59,490.00 USD | 34,260.00 USD | 10,330.00 USD |
| `1D` | `0.1878` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 4,320.00 USD | 2,760.00 USD | 918.24 USD |
| `7D` | `0.1879` | 9,890,000.00 USD | 9,890,000.00 USD | 0.00 USD | 57,250.00 USD | 52,690.00 USD | 48,730.00 USD |
| `1D` | `0.1880` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 3,160.00 USD | 1,240.00 USD |
| `1D` | `0.1882` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 4,630.00 USD | 3,480.00 USD | 0.00 USD |
| `7D` | `0.1882` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 14,000.00 USD | 11,450.00 USD | 32,300.00 USD |
| `1D` | `0.1884` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,490.00 USD |
| `7D` | `0.1885` | 10,000,000.00 USD | 10,000,000.00 USD | 0.00 USD | 9,250.00 USD | 31,900.00 USD | 4,670.00 USD |
| `1D` | `0.1886` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 9,690.00 USD | 2,220.00 USD | 1,730.00 USD |
| `7D` | `0.1888` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 13,720.00 USD | 17,330.00 USD | 83,540.00 USD |
| `7D` | `0.1891` | 10,170,000.00 USD | 10,170,000.00 USD | 0.00 USD | 36,740.00 USD | 0.00 USD | 17,340.00 USD |
| `7D` | `0.1894` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 69,540.00 USD | 12,420.00 USD | 16,820.00 USD |
| `7D` | `0.1897` | 10,350,000.00 USD | 10,350,000.00 USD | 0.00 USD | 25,640.00 USD | 39,120.00 USD | 25,080.00 USD |
| `7D` | `0.1900` | 10,400,000.00 USD | 10,400,000.00 USD | 0.00 USD | 11,530.00 USD | 21,370.00 USD | 14,020.00 USD |
| `7D` | `0.1903` | 10,440,000.00 USD | 10,440,000.00 USD | 0.00 USD | 14,330.00 USD | 11,220.00 USD | 10,800.00 USD |
| `7D` | `0.1906` | 10,520,000.00 USD | 10,520,000.00 USD | 0.00 USD | 18,470.00 USD | 27,580.00 USD | 33,590.00 USD |
| `7D` | `0.1909` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 15,470.00 USD | 29,160.00 USD | 19,220.00 USD |
| `7D` | `0.1912` | 10,600,000.00 USD | 10,600,000.00 USD | 0.00 USD | 0.00 USD | 15,240.00 USD | 0.00 USD |
| `7D` | `0.1915` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 7,460.00 USD | 5,300.00 USD | 0.00 USD |
| `7D` | `0.1918` | 10,630,000.00 USD | 10,630,000.00 USD | 0.00 USD | 0.00 USD | 11,840.00 USD | 11,900.00 USD |
| `7D` | `0.1924` | 10,650,000.00 USD | 10,650,000.00 USD | 0.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD |
| `7D` | `0.1927` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 11,600.00 USD | 13,630.00 USD | 0.00 USD |
| `7D` | `0.1945` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `208.56M` | Total OI Tokens: `1,236,546,888.6 ARB`
  * 1h OI Change: `+0.93%` | 4h OI Change: `-4.52%` | 24h OI Change: `-13.14%`
  * Exchange Breakdown: Binance=`47.02M` | Bybit=`28.82M` | OKX=`16.60M` | Hyperliquid=`15.00M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.58K` | Last 24h: `10.97K` | Last 3d: `22.34K` | Last 7d: `43.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0087%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0027%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0049%` | **USDT Bitget** | `0.0082%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `62.02%` | `37.98%` | `1.63` | 1,240,000.00 USD |
| `15M` | `Binance` | `57.99%` | `42.01%` | `1.38` | 530,060.00 USD |
| `15M` | `OKX` | `67.79%` | `32.21%` | `2.10` | 157,590.00 USD |
| `15M` | `Bybit` | `70.17%` | `29.83%` | `2.35` | 144,280.00 USD |
| `15M` | `KuCoin` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Gate` | `80.95%` | `19.05%` | `4.25` | 16,270.00 USD |
| `15M` | `Bitget` | `61.43%` | `38.57%` | `1.59` | 22,640.00 USD |
| `15M` | `BingX` | `49.66%` | `50.34%` | `0.99` | 63,910.00 USD |
| `15M` | `MEXC` | `61.96%` | `38.04%` | `1.63` | 92,990.00 USD |
| `15M` | `Bitunix` | `56.52%` | `43.48%` | `1.30` | 44,480.00 USD |
| `15M` | `Hyperliquid` | `69.54%` | `30.46%` | `2.28` | 8,900.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `52.12%` | `47.88%` | `1.09` | 41,670.00 USD |
| `15M` | `Crypto.com` | `76.03%` | `23.97%` | `3.17` | 57.60 USD |
| `15M` | `WhiteBIT` | `80.75%` | `19.25%` | `4.19` | 98,970.00 USD |
| `15M` | `HTX` | `32.41%` | `67.59%` | `0.48` | 185.11 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `100%` | `0.00` | 1,920.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 323.03 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `14.31%` | `85.69%` | `0.17` | 12,650.00 USD |
| `15M` | `Whale Positions` | `57.99%` | `42.01%` | `1.38` | 530,060.00 USD |
| `15M` | `Global Accounts` | `62.02%` | `37.98%` | `1.63` | 1,240,000.00 USD |
| `1H` | `ARB` | `55.31%` | `44.69%` | `1.24` | 2,960,000.00 USD |
| `1H` | `Binance` | `57.7%` | `42.3%` | `1.36` | 1,110,000.00 USD |
| `1H` | `OKX` | `60.41%` | `39.59%` | `1.53` | 280,760.00 USD |
| `1H` | `Bybit` | `59.35%` | `40.65%` | `1.46` | 285,430.00 USD |
| `1H` | `KuCoin` | `51.37%` | `48.63%` | `1.06` | 2,860.00 USD |
| `1H` | `Gate` | `49.64%` | `50.36%` | `0.99` | 15,690.00 USD |
| `1H` | `Bitget` | `43.97%` | `56.03%` | `0.78` | 105,820.00 USD |
| `1H` | `BingX` | `28.56%` | `71.44%` | `0.40` | 290,250.00 USD |
| `1H` | `MEXC` | `66.61%` | `33.39%` | `1.99` | 99,770.00 USD |
| `1H` | `Bitunix` | `63.27%` | `36.73%` | `1.72` | 72,190.00 USD |
| `1H` | `Hyperliquid` | `65.1%` | `34.9%` | `1.87` | 7,600.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.04%` | `48.96%` | `1.04` | 548,650.00 USD |
| `1H` | `Crypto.com` | `56.52%` | `43.48%` | `1.30` | 548.60 USD |
| `1H` | `WhiteBIT` | `78.11%` | `21.89%` | `3.57` | 135,690.00 USD |
| `1H` | `HTX` | `37.13%` | `62.87%` | `0.59` | 5.05 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `40.45%` | `59.55%` | `0.68` | 3,900.00 USD |
| `1H` | `Aster` | `59.66%` | `40.34%` | `1.48` | 29.99 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `41.51%` | `58.49%` | `0.71` | 1,320.00 USD |
| `1H` | `Whale Positions` | `57.7%` | `42.3%` | `1.36` | 1,110,000.00 USD |
| `1H` | `Global Accounts` | `55.31%` | `44.69%` | `1.24` | 2,960,000.00 USD |
| `4H` | `ARB` | `46.24%` | `53.76%` | `0.86` | 47,750,000.00 USD |
| `4H` | `Binance` | `45.24%` | `54.76%` | `0.83` | 17,060,000.00 USD |
| `4H` | `OKX` | `46.29%` | `53.71%` | `0.86` | 9,330,000.00 USD |
| `4H` | `Bybit` | `47.96%` | `52.04%` | `0.92` | 3,710,000.00 USD |
| `4H` | `KuCoin` | `48.95%` | `51.05%` | `0.96` | 445,830.00 USD |
| `4H` | `Gate` | `50.84%` | `49.16%` | `1.03` | 1,650,000.00 USD |
| `4H` | `Bitget` | `41.76%` | `58.24%` | `0.72` | 2,130,000.00 USD |
| `4H` | `BingX` | `29.46%` | `70.54%` | `0.42` | 2,780,000.00 USD |
| `4H` | `MEXC` | `44.54%` | `55.46%` | `0.80` | 4,040,000.00 USD |
| `4H` | `Bitunix` | `49.29%` | `50.71%` | `0.97` | 1,180,000.00 USD |
| `4H` | `Hyperliquid` | `45.49%` | `54.51%` | `0.83` | 1,400,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.65%` | `50.35%` | `0.99` | 2,280,000.00 USD |
| `4H` | `Crypto.com` | `52.55%` | `47.45%` | `1.11` | 26,720.00 USD |
| `4H` | `WhiteBIT` | `84.14%` | `15.86%` | `5.31` | 1,330,000.00 USD |
| `4H` | `HTX` | `44.93%` | `55.07%` | `0.82` | 10,020.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.52%` | `50.48%` | `0.98` | 154,270.00 USD |
| `4H` | `Aster` | `88.59%` | `11.41%` | `7.76` | 69,710.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `44.32%` | `55.68%` | `0.80` | 144,780.00 USD |
| `4H` | `Whale Positions` | `45.24%` | `54.76%` | `0.83` | 17,060,000.00 USD |
| `4H` | `Global Accounts` | `46.24%` | `53.76%` | `0.86` | 47,750,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1711` | `0.1711` | `0.1711` | `0.1716` | `0.1708` | 800,876.04 USD | 410,736.84 USD | 390,139.20 USD | 20,597.64 USD | `+2.57%` | `7B / 12S` |
| `0:00 UTC` | `0.1710` | `0.1702` | `0.1710` | `0.1719` | `0.1689` | 1,300,882.78 USD | 531,501.17 USD | 769,381.61 USD | -237,880.44 USD | `-18.29%` | `17B / 38S` |
| `5:00 UTC` | `0.1689` | `0.1689` | `0.1689` | `0.1697` | `0.1682` | 1,292,914.43 USD | 712,068.28 USD | 580,846.15 USD | 131,222.13 USD | `+10.15%` | `38B / 24S` |
| `0:00 UTC` | `0.1690` | `0.1697` | `0.1690` | `0.1704` | `0.1690` | 952,197.22 USD | 428,970.00 USD | 523,227.22 USD | -94,257.22 USD | `-9.90%` | `28B / 31S` |
| `5:00 UTC` | `0.1686` | `0.1691` | `0.1686` | `0.1698` | `0.1685` | 581,095.74 USD | 286,225.77 USD | 294,869.97 USD | -8,644.20 USD | `-1.49%` | `37B / 26S` |
| `0:00 UTC` | `0.1678` | `0.1678` | `0.1678` | `0.1689` | `0.1673` | 1,127,023.46 USD | 573,365.61 USD | 553,657.86 USD | 19,707.75 USD | `+1.75%` | `27B / 19S` |
| `5:00 UTC` | `0.1687` | `0.1687` | `0.1687` | `0.1691` | `0.1680` | 541,507.84 USD | 294,376.97 USD | 247,130.87 USD | 47,246.11 USD | `+8.72%` | `31B / 8S` |
| `0:00 UTC` | `0.1684` | `0.1682` | `0.1684` | `0.1688` | `0.1678` | 593,121.43 USD | 297,803.46 USD | 295,317.97 USD | 2,485.50 USD | `+0.42%` | `13B / 13S` |
| `5:00 UTC` | `0.1683` | `0.1683` | `0.1683` | `0.1688` | `0.1678` | 375,189.89 USD | 244,846.62 USD | 130,343.28 USD | 114,503.34 USD | `+30.52%` | `33B / 4S` |
| `0:00 UTC` | `0.1687` | `0.1688` | `0.1687` | `0.1693` | `0.1682` | 534,761.88 USD | 349,100.95 USD | 185,660.93 USD | 163,440.02 USD | `+30.56%` | `36B / 9S` |

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
| `5m` | 929.68 USD | 86,640.00 USD | **`ACCUMULATION`** |
| `15m` | 25,000.00 USD | 205,880.00 USD | **`ACCUMULATION`** |
| `30m` | 3,960.00 USD | 323,250.00 USD | **`ACCUMULATION`** |
| `1h` | -14,590.00 USD | 735,850.00 USD | **`ACCUMULATION`** |
| `2h` | 11,340.00 USD | -172,770.00 USD | **`DISTRIBUTION`** |
| `4h` | -17,220.00 USD | -2,110,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -27,500.00 USD | -1,970,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,390.00 USD | -3,980,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 445,200.00 USD | -3,400,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -437,510.00 USD | -5,280,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -4,660,000.00 USD | -30,110,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -32,120,000.00 USD | -161,740,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+929.68` | 15m=`+25.00K` | 1h=`-14.59K` | 24h=`-437.51K`
* Futures Capital Netflows: 5m=`+86.64K` | 15m=`+205.88K` | 1h=`+735.85K` | 24h=`-5.28M`
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
  * `2026-10-30 00:58:08 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:08 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:17:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:09:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:09:08 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:08 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:08 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
