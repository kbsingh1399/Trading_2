# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 01:51:15 IST` (`2026-10-29 20:21:15 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1683` | `0.1684` | `0.1646` | `0.1648` | `7,502,001` | 1,247,002.97 USD | -447,537.00 USD | `-35.89%` | -4,748,446.18 USD | `-3.83` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1648` | `0.1658` | `0.1640` | `0.1651` | `5,669,565` | 933,848.71 USD | 115,865.79 USD | `+12.41%` | -4,632,580.39 USD | `+0.96` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1651` | `0.1659` | `0.1645` | `0.1655` | `1,938,794` | 320,452.50 USD | 77,498.93 USD | `+24.18%` | -4,555,081.46 USD | `+0.56` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1682` | `0.1693` | `0.1682` | `0.1688` | `4,032,710` | 680,766.88 USD | 226,446.04 USD | `+33.26%` | -4,274,662.59 USD | `+1.73` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1688` | `0.1688` | `0.1681` | `0.1683` | `2,689,604` | 452,736.37 USD | -26,246.58 USD | `-5.80%` | -4,300,909.18 USD | `+0.23` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1683` | `0.1684` | `0.1640` | `0.1654` | `15,114,009` | 2,501,908.01 USD | -254,776.11 USD | `-10.18%` | -4,555,685.28 USD | `-1.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1696` | `0.1704` | `0.1673` | `0.1687` | `18,975,463` | 3,201,824.26 USD | -35,947.57 USD | `-1.12%` | -4,720,262.78 USD | `+0.39` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1686` | `0.1693` | `0.1678` | `0.1683` | `12,478,051` | 2,101,814.57 USD | 317,188.30 USD | `+15.09%` | -4,403,074.48 USD | `+1.26` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1683` | `0.1684` | `0.1640` | `0.1654` | `15,114,009` | 2,501,908.01 USD | -254,776.11 USD | `-10.18%` | -4,657,850.59 USD | `-0.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,374,542.78 USD | `-1.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,572,000.78 USD | `-0.89` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1640` | `0.1654` | `15,114,009` | 2,501,908.01 USD | -254,776.11 USD | `-10.18%` | -3,826,776.89 USD | `+0.73` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1652` | `0.1687` | `0.1623` | `0.1631` | `68,085,678` | 11,252,816.65 USD | -909,329.92 USD | `-8.08%` | -705,420.63 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,136,414.44 USD | `-0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,374,542.78 USD | `-1.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,572,000.78 USD | `-0.89` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1640` | `0.1654` | `15,114,009` | 2,501,908.01 USD | -254,776.11 USD | `-10.18%` | -3,826,776.89 USD | `+0.73` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:44:44 IST` |

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
| `7D` | `Long Liquidation` | `0.1467` | 9,440,000.00 USD | 9,440,000.00 USD | 9,720.00 USD | 9,180.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1470` | 9,410,000.00 USD | 9,410,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1473` | 3,220,000.00 USD | 3,220,000.00 USD | 9,360.00 USD | 7,910.00 USD | 1,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1473` | 9,400,000.00 USD | 9,400,000.00 USD | 6,490.00 USD | 5,400.00 USD | 5,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 73,750.00 USD | 801,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1476` | 3,200,000.00 USD | 3,200,000.00 USD | 6,530.00 USD | 1,060.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1476` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 14,780.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1479` | 3,190,000.00 USD | 3,190,000.00 USD | 16,640.00 USD | 14,840.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1479` | 9,370,000.00 USD | 9,370,000.00 USD | 0.00 USD | 39,730.00 USD | 14,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1482` | 3,150,000.00 USD | 3,150,000.00 USD | 5,680.00 USD | 6,350.00 USD | 12,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1482` | 9,310,000.00 USD | 9,310,000.00 USD | 41,960.00 USD | 20,720.00 USD | 27,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1485` | 3,130,000.00 USD | 3,130,000.00 USD | 9,730.00 USD | 3,320.00 USD | 4,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1485` | 9,220,000.00 USD | 9,220,000.00 USD | 16,180.00 USD | 7,340.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,650.00 USD | 727,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1488` | 3,110,000.00 USD | 3,110,000.00 USD | 2,660.00 USD | 5,180.00 USD | 3,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1488` | 9,160,000.00 USD | 9,160,000.00 USD | 20,860.00 USD | 3,130.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1491` | 3,100,000.00 USD | 3,100,000.00 USD | 7,650.00 USD | 10,490.00 USD | 4,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1491` | 9,130,000.00 USD | 9,130,000.00 USD | 33,540.00 USD | 17,020.00 USD | 20,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1494` | 3,080,000.00 USD | 3,080,000.00 USD | 14,210.00 USD | 5,270.00 USD | 2,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1494` | 9,060,000.00 USD | 9,060,000.00 USD | 34,220.00 USD | 9,890.00 USD | 14,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 35,860.00 USD | 724,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1497` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1497` | 9,000,000.00 USD | 9,000,000.00 USD | 20,880.00 USD | 17,180.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1500` | 3,050,000.00 USD | 3,050,000.00 USD | 2,670.00 USD | 0.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1500` | 8,950,000.00 USD | 8,950,000.00 USD | 46,820.00 USD | 5,810.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1503` | 3,040,000.00 USD | 3,040,000.00 USD | 3,610.00 USD | 2,640.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1503` | 8,880,000.00 USD | 8,880,000.00 USD | 11,490.00 USD | 13,450.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1505` | 102,290.00 USD | 689,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1506` | 3,040,000.00 USD | 3,040,000.00 USD | 5,430.00 USD | 640.88 USD | 7,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1506` | 8,840,000.00 USD | 8,840,000.00 USD | 33,170.00 USD | 18,020.00 USD | 65,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1509` | 3,020,000.00 USD | 3,020,000.00 USD | 5,640.00 USD | 3,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1509` | 8,720,000.00 USD | 8,720,000.00 USD | 17,340.00 USD | 9,550.00 USD | 24,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1512` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 4,360.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1512` | 8,670,000.00 USD | 8,670,000.00 USD | 18,600.00 USD | 8,620.00 USD | 26,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1515` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 1,730.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1515` | 8,620,000.00 USD | 8,620,000.00 USD | 53,430.00 USD | 13,330.00 USD | 53,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 9,900.00 USD | 586,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1518` | 3,000,000.00 USD | 3,000,000.00 USD | 14,340.00 USD | 4,320.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1518` | 8,500,000.00 USD | 8,500,000.00 USD | 46,830.00 USD | 15,160.00 USD | 64,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1521` | 2,980,000.00 USD | 2,980,000.00 USD | 9,450.00 USD | 1,470.00 USD | 11,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1521` | 8,370,000.00 USD | 8,370,000.00 USD | 47,740.00 USD | 6,920.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1524` | 2,950,000.00 USD | 2,950,000.00 USD | 1,870.00 USD | 2,970.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1524` | 8,280,000.00 USD | 8,280,000.00 USD | 37,550.00 USD | 13,950.00 USD | 11,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1525` | 42,800.00 USD | 576,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1527` | 2,940,000.00 USD | 2,940,000.00 USD | 3,300.00 USD | 0.00 USD | 11,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1527` | 8,220,000.00 USD | 8,220,000.00 USD | 56,950.00 USD | 30,410.00 USD | 33,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1530` | 2,930,000.00 USD | 2,930,000.00 USD | 4,960.00 USD | 5,040.00 USD | 8,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1530` | 8,100,000.00 USD | 8,100,000.00 USD | 54,790.00 USD | 9,880.00 USD | 16,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1533` | 2,910,000.00 USD | 2,910,000.00 USD | 14,310.00 USD | 1,900.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1533` | 8,010,000.00 USD | 8,010,000.00 USD | 10,760.00 USD | 16,570.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 189,960.00 USD | 534,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1536` | 2,890,000.00 USD | 2,890,000.00 USD | 4,320.00 USD | 5,590.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1536` | 7,970,000.00 USD | 7,970,000.00 USD | 37,160.00 USD | 2,910.00 USD | 13,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1539` | 2,870,000.00 USD | 2,870,000.00 USD | 2,920.00 USD | 6,640.00 USD | 1,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1539` | 7,910,000.00 USD | 7,910,000.00 USD | 22,990.00 USD | 18,230.00 USD | 5,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1542` | 2,860,000.00 USD | 2,860,000.00 USD | 1,710.00 USD | 0.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1542` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 3,590.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1545` | 2,860,000.00 USD | 2,860,000.00 USD | 13,270.00 USD | 3,200.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1545` | 7,860,000.00 USD | 7,860,000.00 USD | 9,250.00 USD | 0.00 USD | 5,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1545` | 26,170.00 USD | 344,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1548` | 2,840,000.00 USD | 2,840,000.00 USD | 1,140.00 USD | 8,660.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1548` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1551` | 2,830,000.00 USD | 2,830,000.00 USD | 4,810.00 USD | 4,140.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1551` | 7,840,000.00 USD | 7,840,000.00 USD | 34,670.00 USD | 11,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1554` | 2,820,000.00 USD | 2,820,000.00 USD | 14,410.00 USD | 15,630.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1554` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 0.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1555` | 39,570.00 USD | 317,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1557` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 3,410.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1557` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 4,510.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1560` | 2,770,000.00 USD | 2,770,000.00 USD | 2,970.00 USD | 11,300.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1560` | 7,770,000.00 USD | 7,770,000.00 USD | 0.00 USD | 6,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1563` | 2,750,000.00 USD | 2,750,000.00 USD | 3,050.00 USD | 1,050.00 USD | 16,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1563` | 7,770,000.00 USD | 7,770,000.00 USD | 0.00 USD | 19,950.00 USD | 9,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1565` | 23,920.00 USD | 278,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1566` | 2,730,000.00 USD | 2,730,000.00 USD | 45,560.00 USD | 11,570.00 USD | 15,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1566` | 7,740,000.00 USD | 7,740,000.00 USD | 50,480.00 USD | 29,160.00 USD | 26,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1569` | 2,660,000.00 USD | 2,660,000.00 USD | 24,600.00 USD | 31,270.00 USD | 7,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1569` | 7,630,000.00 USD | 7,630,000.00 USD | 15,590.00 USD | 5,100.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1572` | 2,600,000.00 USD | 2,600,000.00 USD | 34,670.00 USD | 14,240.00 USD | 17,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1572` | 7,600,000.00 USD | 7,600,000.00 USD | 40,760.00 USD | 34,450.00 USD | 17,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1575` | 2,530,000.00 USD | 2,530,000.00 USD | 34,430.00 USD | 19,170.00 USD | 6,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1575` | 7,500,000.00 USD | 7,500,000.00 USD | 23,310.00 USD | 88,960.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1575` | 4,940.00 USD | 254,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1578` | 2,470,000.00 USD | 2,470,000.00 USD | 59,420.00 USD | 64,050.00 USD | 24,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1578` | 7,370,000.00 USD | 7,370,000.00 USD | 58,590.00 USD | 84,670.00 USD | 67,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1581` | 2,320,000.00 USD | 2,320,000.00 USD | 31,970.00 USD | 6,220.00 USD | 22,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1581` | 7,160,000.00 USD | 7,160,000.00 USD | 92,720.00 USD | 58,880.00 USD | 57,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1584` | 2,260,000.00 USD | 2,260,000.00 USD | 34,630.00 USD | 11,050.00 USD | 15,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1584` | 6,950,000.00 USD | 6,950,000.00 USD | 80,450.00 USD | 35,780.00 USD | 123,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1585` | 5,760.00 USD | 249,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1587` | 2,200,000.00 USD | 2,200,000.00 USD | 6,650.00 USD | 21,380.00 USD | 12,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1587` | 6,710,000.00 USD | 6,710,000.00 USD | 69,180.00 USD | 22,370.00 USD | 31,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1590` | 2,160,000.00 USD | 2,160,000.00 USD | 13,490.00 USD | 27,950.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1590` | 6,590,000.00 USD | 6,590,000.00 USD | 71,200.00 USD | 44,110.00 USD | 51,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1593` | 2,110,000.00 USD | 2,110,000.00 USD | 44,300.00 USD | 6,320.00 USD | 23,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1593` | 6,420,000.00 USD | 6,420,000.00 USD | 69,430.00 USD | 56,020.00 USD | 68,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1595` | 63,000.00 USD | 243,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1596` | 2,040,000.00 USD | 2,040,000.00 USD | 29,470.00 USD | 19,190.00 USD | 35,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1596` | 6,230,000.00 USD | 6,230,000.00 USD | 161,460.00 USD | 85,250.00 USD | 120,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1599` | 1,950,000.00 USD | 1,950,000.00 USD | 76,280.00 USD | 16,990.00 USD | 33,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1599` | 5,860,000.00 USD | 5,860,000.00 USD | 219,060.00 USD | 55,380.00 USD | 87,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1602` | 1,830,000.00 USD | 1,830,000.00 USD | 55,540.00 USD | 46,820.00 USD | 7,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1602` | 5,500,000.00 USD | 5,500,000.00 USD | 44,770.00 USD | 46,490.00 USD | 40,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1605` | 1,710,000.00 USD | 1,710,000.00 USD | 34,500.00 USD | 18,980.00 USD | 37,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1605` | 5,370,000.00 USD | 5,370,000.00 USD | 177,720.00 USD | 136,660.00 USD | 217,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1605` | 37,640.00 USD | 180,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1608` | 1,620,000.00 USD | 1,620,000.00 USD | 66,600.00 USD | 35,780.00 USD | 22,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1608` | 4,830,000.00 USD | 4,830,000.00 USD | 129,610.00 USD | 174,940.00 USD | 131,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1611` | 1,500,000.00 USD | 1,500,000.00 USD | 132,780.00 USD | 132,510.00 USD | 51,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1611` | 4,400,000.00 USD | 4,400,000.00 USD | 148,170.00 USD | 227,820.00 USD | 233,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1614` | 1,180,000.00 USD | 1,180,000.00 USD | 55,510.00 USD | 30,350.00 USD | 53,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1614` | 3,790,000.00 USD | 3,790,000.00 USD | 323,670.00 USD | 194,680.00 USD | 282,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1615` | 17,290.00 USD | 143,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1617` | 1,040,000.00 USD | 1,040,000.00 USD | 73,170.00 USD | 27,450.00 USD | 30,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1617` | 2,990,000.00 USD | 2,990,000.00 USD | 346,150.00 USD | 98,680.00 USD | 418,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1620` | 911,510.00 USD | 911,510.00 USD | 71,140.00 USD | 54,730.00 USD | 75,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1620` | 2,120,000.00 USD | 2,120,000.00 USD | 303,960.00 USD | 134,660.00 USD | 279,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1623` | 710,360.00 USD | 710,360.00 USD | 53,880.00 USD | 67,020.00 USD | 31,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1623` | 1,410,000.00 USD | 1,410,000.00 USD | 297,830.00 USD | 122,030.00 USD | 208,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1625` | 106,340.00 USD | 125,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1626` | 557,980.00 USD | 557,980.00 USD | 19,820.00 USD | 12,640.00 USD | 27,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1626` | 778,400.00 USD | 778,400.00 USD | 234,280.00 USD | 71,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1629` | 498,020.00 USD | 498,020.00 USD | 14,220.00 USD | 33,030.00 USD | 19,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1629` | 473,000.00 USD | 473,000.00 USD | 171,310.00 USD | 0.00 USD | 20,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1632` | 431,150.00 USD | 431,150.00 USD | 25,750.00 USD | 19,630.00 USD | 17,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1632` | 280,830.00 USD | 280,830.00 USD | 9,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1635` | 368,390.00 USD | 368,390.00 USD | 37,200.00 USD | 6,390.00 USD | 11,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1635` | 271,620.00 USD | 271,620.00 USD | 0.00 USD | 13,670.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1635` | 1,230.00 USD | 19,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1638` | 312,940.00 USD | 312,940.00 USD | 9,410.00 USD | 22,520.00 USD | 42,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1638` | 236,590.00 USD | 236,590.00 USD | 0.00 USD | 0.00 USD | 62,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1641` | 238,220.00 USD | 238,220.00 USD | 7,360.00 USD | 9,300.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1641` | 174,180.00 USD | 174,180.00 USD | 22,480.00 USD | 29,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1644` | 211,210.00 USD | 211,210.00 USD | 25,590.00 USD | 25,250.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1644` | 122,460.00 USD | 122,460.00 USD | 0.00 USD | 8,990.00 USD | 26,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1645` | 6,190.00 USD | 18,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1647` | 148,960.00 USD | 148,960.00 USD | 40,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1647` | 87,240.00 USD | 87,240.00 USD | 34,760.00 USD | 0.00 USD | 7,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1650` | 108,930.00 USD | 108,930.00 USD | 12,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1650` | 44,820.00 USD | 44,820.00 USD | 0.00 USD | 7,000.00 USD | 37,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1653` | 96,530.00 USD | 96,530.00 USD | 79,670.00 USD | 16,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1653` | 91,340.00 USD | 91,340.00 USD | 33,810.00 USD | 12,460.00 USD | 45,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1653` | 182,680.00 USD | 182,680.00 USD | 33,810.00 USD | 12,460.00 USD | 45,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1655` | 12,070.00 USD | 12,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1656` | 128,500.00 USD | 128,500.00 USD | 52,180.00 USD | 51,020.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1656` | 257,000.00 USD | 257,000.00 USD | 52,180.00 USD | 51,020.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1656` | 279,310.00 USD | 279,310.00 USD | 43,910.00 USD | 19,330.00 USD | 33,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1659` | 382,130.00 USD | 382,130.00 USD | 43,890.00 USD | 19,240.00 USD | 62,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1659` | 320,090.00 USD | 320,090.00 USD | 40,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1662` | 461,800.00 USD | 461,800.00 USD | 8,220.00 USD | 6,760.00 USD | 64,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1662` | 511,720.00 USD | 511,720.00 USD | 48,590.00 USD | 62,020.00 USD | 81,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1665` | 528,890.00 USD | 528,890.00 USD | 0.00 USD | 0.00 USD | 67,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1665` | 688,910.00 USD | 688,910.00 USD | 87,050.00 USD | 32,780.00 USD | 57,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1668` | 545,830.00 USD | 545,830.00 USD | 0.00 USD | 0.00 USD | 16,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1668` | 782,670.00 USD | 782,670.00 USD | 11,410.00 USD | 39,630.00 USD | 42,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1671` | 566,550.00 USD | 566,550.00 USD | 20,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1671` | 915,690.00 USD | 915,690.00 USD | 70,540.00 USD | 62,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1674` | 587,860.00 USD | 587,860.00 USD | 21,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1674` | 1,050,000.00 USD | 1,050,000.00 USD | 44,960.00 USD | 88,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1677` | 602,480.00 USD | 602,480.00 USD | 14,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1677` | 1,170,000.00 USD | 1,170,000.00 USD | 59,010.00 USD | 64,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1680` | 682,470.00 USD | 682,470.00 USD | 75,420.00 USD | 4,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1680` | 1,360,000.00 USD | 1,360,000.00 USD | 101,910.00 USD | 68,430.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1683` | 769,100.00 USD | 769,100.00 USD | 80,310.00 USD | 3,200.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1683` | 1,430,000.00 USD | 1,430,000.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1685` | 5,550.00 USD | 5,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1686` | 798,970.00 USD | 798,970.00 USD | 0.00 USD | 23,410.00 USD | 6,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1689` | 805,950.00 USD | 805,950.00 USD | 0.00 USD | 6,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1689` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1692` | 927,430.00 USD | 927,430.00 USD | 55,320.00 USD | 66,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1692` | 1,530,000.00 USD | 1,530,000.00 USD | 21,780.00 USD | 32,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1695` | 949,730.00 USD | 949,730.00 USD | 0.00 USD | 22,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1695` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 30,490.00 USD | 28,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1698` | 1,030,000.00 USD | 1,030,000.00 USD | 20,810.00 USD | 56,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1698` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 56,860.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1701` | 1,710,000.00 USD | 1,710,000.00 USD | 22,820.00 USD | 25,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1704` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 14,420.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1704` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 46,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1707` | 1,170,000.00 USD | 1,170,000.00 USD | 37,960.00 USD | 71,860.00 USD | 4,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1707` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 59,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1710` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1710` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 25,490.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1713` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 17,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1713` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1716` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 25,600.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1716` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 15,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1719` | 1,260,000.00 USD | 1,260,000.00 USD | 30,950.00 USD | 8,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1722` | 1,430,000.00 USD | 1,430,000.00 USD | 100,000.00 USD | 16,860.00 USD | 45,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1722` | 2,360,000.00 USD | 2,360,000.00 USD | 118,060.00 USD | 0.00 USD | 342,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1725` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 26,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1728` | 1,470,000.00 USD | 1,470,000.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1731` | 2,840,000.00 USD | 2,840,000.00 USD | 476,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1734` | 1,490,000.00 USD | 1,490,000.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1737` | 1,530,000.00 USD | 1,530,000.00 USD | 29,560.00 USD | 9,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1737` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 52,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1740` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 1,600.00 USD | 9,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1740` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 31,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1743` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1743` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1746` | 1,570,000.00 USD | 1,570,000.00 USD | 8,530.00 USD | 2,460.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1749` | 1,700,000.00 USD | 1,700,000.00 USD | 80,070.00 USD | 2,280.00 USD | 39,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1749` | 3,030,000.00 USD | 3,030,000.00 USD | 69,520.00 USD | 0.00 USD | 22,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1752` | 1,750,000.00 USD | 1,750,000.00 USD | 23,850.00 USD | 0.00 USD | 32,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1752` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 263,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1755` | 1,830,000.00 USD | 1,830,000.00 USD | 21,260.00 USD | 16,650.00 USD | 35,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1755` | 3,510,000.00 USD | 3,510,000.00 USD | 37,610.00 USD | 0.00 USD | 177,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1755` | 600.46 USD | 6,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1758` | 1,980,000.00 USD | 1,980,000.00 USD | 71,330.00 USD | 31,940.00 USD | 51,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1758` | 3,750,000.00 USD | 3,750,000.00 USD | 195,390.00 USD | 38,670.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1761` | 2,170,000.00 USD | 2,170,000.00 USD | 53,970.00 USD | 88,390.00 USD | 50,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1761` | 4,250,000.00 USD | 4,250,000.00 USD | 352,270.00 USD | 115,470.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1764` | 2,290,000.00 USD | 2,290,000.00 USD | 34,410.00 USD | 25,840.00 USD | 61,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1764` | 4,640,000.00 USD | 4,640,000.00 USD | 144,160.00 USD | 205,820.00 USD | 40,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1765` | 339.06 USD | 6,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1767` | 2,430,000.00 USD | 2,430,000.00 USD | 27,430.00 USD | 52,820.00 USD | 52,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1767` | 4,950,000.00 USD | 4,950,000.00 USD | 176,410.00 USD | 128,100.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1770` | 2,550,000.00 USD | 2,550,000.00 USD | 36,140.00 USD | 47,810.00 USD | 38,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1770` | 5,160,000.00 USD | 5,160,000.00 USD | 61,490.00 USD | 98,420.00 USD | 44,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1773` | 2,630,000.00 USD | 2,630,000.00 USD | 30,810.00 USD | 28,980.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1773` | 5,340,000.00 USD | 5,340,000.00 USD | 103,820.00 USD | 81,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1776` | 2,760,000.00 USD | 2,760,000.00 USD | 85,560.00 USD | 19,390.00 USD | 21,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1776` | 5,540,000.00 USD | 5,540,000.00 USD | 135,140.00 USD | 59,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1779` | 2,890,000.00 USD | 2,890,000.00 USD | 27,480.00 USD | 77,730.00 USD | 25,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1779` | 5,770,000.00 USD | 5,770,000.00 USD | 52,730.00 USD | 46,410.00 USD | 131,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1782` | 3,000,000.00 USD | 3,000,000.00 USD | 46,310.00 USD | 14,240.00 USD | 47,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1782` | 5,840,000.00 USD | 5,840,000.00 USD | 20,690.00 USD | 13,990.00 USD | 31,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1785` | 3,150,000.00 USD | 3,150,000.00 USD | 96,920.00 USD | 46,180.00 USD | 14,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1785` | 6,080,000.00 USD | 6,080,000.00 USD | 153,160.00 USD | 78,850.00 USD | 16,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1788` | 3,250,000.00 USD | 3,250,000.00 USD | 18,550.00 USD | 42,480.00 USD | 36,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1788` | 6,190,000.00 USD | 6,190,000.00 USD | 73,130.00 USD | 18,250.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1791` | 3,320,000.00 USD | 3,320,000.00 USD | 36,940.00 USD | 15,630.00 USD | 18,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1791` | 6,370,000.00 USD | 6,370,000.00 USD | 155,720.00 USD | 17,360.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1794` | 3,420,000.00 USD | 3,420,000.00 USD | 36,860.00 USD | 47,980.00 USD | 12,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1794` | 6,470,000.00 USD | 6,470,000.00 USD | 27,100.00 USD | 42,780.00 USD | 36,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1795` | 48,610.00 USD | 55,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1797` | 3,510,000.00 USD | 3,510,000.00 USD | 27,280.00 USD | 22,110.00 USD | 36,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1797` | 6,510,000.00 USD | 6,510,000.00 USD | 17,130.00 USD | 12,930.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1800` | 3,550,000.00 USD | 3,550,000.00 USD | 5,820.00 USD | 8,690.00 USD | 25,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1800` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 34,680.00 USD | 64,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1803` | 3,600,000.00 USD | 3,600,000.00 USD | 10,270.00 USD | 35,880.00 USD | 12,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1803` | 6,690,000.00 USD | 6,690,000.00 USD | 35,280.00 USD | 25,700.00 USD | 18,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1805` | 3,130.00 USD | 58,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1806` | 3,640,000.00 USD | 3,640,000.00 USD | 5,900.00 USD | 14,370.00 USD | 11,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1806` | 6,780,000.00 USD | 6,780,000.00 USD | 11,410.00 USD | 56,850.00 USD | 19,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1809` | 3,710,000.00 USD | 3,710,000.00 USD | 27,060.00 USD | 27,370.00 USD | 23,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1809` | 6,920,000.00 USD | 6,920,000.00 USD | 53,670.00 USD | 30,810.00 USD | 58,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1812` | 3,850,000.00 USD | 3,850,000.00 USD | 56,360.00 USD | 44,940.00 USD | 38,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1812` | 7,020,000.00 USD | 7,020,000.00 USD | 34,960.00 USD | 16,640.00 USD | 50,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1815` | 3,880,000.00 USD | 3,880,000.00 USD | 9,730.00 USD | 3,320.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1815` | 7,150,000.00 USD | 7,150,000.00 USD | 60,010.00 USD | 30,810.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1815` | 8,150.00 USD | 66,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1818` | 3,950,000.00 USD | 3,950,000.00 USD | 37,120.00 USD | 11,780.00 USD | 23,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1818` | 7,260,000.00 USD | 7,260,000.00 USD | 75,040.00 USD | 24,140.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1821` | 4,000,000.00 USD | 4,000,000.00 USD | 21,220.00 USD | 19,510.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1821` | 7,380,000.00 USD | 7,380,000.00 USD | 40,950.00 USD | 33,870.00 USD | 41,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1824` | 4,040,000.00 USD | 4,040,000.00 USD | 11,560.00 USD | 18,270.00 USD | 13,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1824` | 7,530,000.00 USD | 7,530,000.00 USD | 39,400.00 USD | 17,880.00 USD | 95,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1827` | 4,080,000.00 USD | 4,080,000.00 USD | 21,440.00 USD | 6,860.00 USD | 4,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1827` | 7,690,000.00 USD | 7,690,000.00 USD | 79,610.00 USD | 18,690.00 USD | 65,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1830` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 4,510.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1830` | 7,830,000.00 USD | 7,830,000.00 USD | 64,890.00 USD | 20,550.00 USD | 52,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1833` | 4,090,000.00 USD | 4,090,000.00 USD | 2,670.00 USD | 0.00 USD | 4,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1833` | 8,090,000.00 USD | 8,090,000.00 USD | 186,730.00 USD | 49,740.00 USD | 26,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1836` | 4,100,000.00 USD | 4,100,000.00 USD | 3,610.00 USD | 0.00 USD | 728.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1836` | 8,260,000.00 USD | 8,260,000.00 USD | 29,580.00 USD | 83,110.00 USD | 52,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1839` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 2,640.00 USD | 7,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1839` | 8,550,000.00 USD | 8,550,000.00 USD | 129,950.00 USD | 41,230.00 USD | 114,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1842` | 4,120,000.00 USD | 4,120,000.00 USD | 5,430.00 USD | 3,330.00 USD | 1,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1842` | 8,710,000.00 USD | 8,710,000.00 USD | 71,550.00 USD | 26,100.00 USD | 62,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1845` | 4,140,000.00 USD | 4,140,000.00 USD | 5,640.00 USD | 5,640.00 USD | 9,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1845` | 8,820,000.00 USD | 8,820,000.00 USD | 34,630.00 USD | 8,590.00 USD | 66,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1848` | 4,160,000.00 USD | 4,160,000.00 USD | 4,680.00 USD | 4,360.00 USD | 9,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1848` | 8,930,000.00 USD | 8,930,000.00 USD | 26,600.00 USD | 65,230.00 USD | 26,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1851` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 1,730.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1851` | 9,280,000.00 USD | 9,280,000.00 USD | 94,780.00 USD | 28,290.00 USD | 220,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1854` | 4,170,000.00 USD | 4,170,000.00 USD | 4,290.00 USD | 1,690.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1854` | 9,450,000.00 USD | 9,450,000.00 USD | 105,210.00 USD | 4,290.00 USD | 63,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1857` | 4,200,000.00 USD | 4,200,000.00 USD | 10,050.00 USD | 2,630.00 USD | 12,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1857` | 9,730,000.00 USD | 9,730,000.00 USD | 125,100.00 USD | 32,070.00 USD | 127,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1860` | 4,220,000.00 USD | 4,220,000.00 USD | 9,450.00 USD | 4,440.00 USD | 5,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1860` | 9,970,000.00 USD | 9,970,000.00 USD | 87,180.00 USD | 72,430.00 USD | 74,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1863` | 4,230,000.00 USD | 4,230,000.00 USD | 1,870.00 USD | 0.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1863` | 10,160,000.00 USD | 10,160,000.00 USD | 71,330.00 USD | 56,440.00 USD | 61,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1866` | 4,240,000.00 USD | 4,240,000.00 USD | 3,300.00 USD | 0.00 USD | 5,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1866` | 10,310,000.00 USD | 10,310,000.00 USD | 82,960.00 USD | 29,050.00 USD | 39,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1869` | 4,250,000.00 USD | 4,250,000.00 USD | 4,960.00 USD | 1,740.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1869` | 10,610,000.00 USD | 10,610,000.00 USD | 159,230.00 USD | 58,520.00 USD | 78,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1872` | 4,280,000.00 USD | 4,280,000.00 USD | 12,350.00 USD | 5,200.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1872` | 10,910,000.00 USD | 10,910,000.00 USD | 80,790.00 USD | 127,580.00 USD | 93,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1875` | 4,280,000.00 USD | 4,280,000.00 USD | 1,960.00 USD | 2,820.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1875` | 11,030,000.00 USD | 11,030,000.00 USD | 51,690.00 USD | 30,090.00 USD | 36,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1875` | 21,190.00 USD | 87,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1878` | 11,120,000.00 USD | 11,120,000.00 USD | 55,660.00 USD | 12,570.00 USD | 30,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1881` | 11,200,000.00 USD | 11,200,000.00 USD | 29,820.00 USD | 31,710.00 USD | 13,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1884` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 31,900.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1887` | 11,280,000.00 USD | 11,280,000.00 USD | 22,970.00 USD | 0.00 USD | 25,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1890` | 11,410,000.00 USD | 11,410,000.00 USD | 36,740.00 USD | 17,330.00 USD | 75,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1893` | 11,470,000.00 USD | 11,470,000.00 USD | 32,450.00 USD | 6,940.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1895` | 3,550.00 USD | 91,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1896` | 11,580,000.00 USD | 11,580,000.00 USD | 62,730.00 USD | 27,440.00 USD | 18,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1899` | 11,650,000.00 USD | 11,650,000.00 USD | 11,530.00 USD | 38,530.00 USD | 20,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1902` | 11,670,000.00 USD | 11,670,000.00 USD | 14,330.00 USD | 0.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1905` | 11,730,000.00 USD | 11,730,000.00 USD | 8,720.00 USD | 24,800.00 USD | 24,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1908` | 11,830,000.00 USD | 11,830,000.00 USD | 25,220.00 USD | 43,160.00 USD | 28,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1911` | 11,840,000.00 USD | 11,840,000.00 USD | 0.00 USD | 9,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1914` | 11,860,000.00 USD | 11,860,000.00 USD | 7,460.00 USD | 11,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1917` | 11,880,000.00 USD | 11,880,000.00 USD | 0.00 USD | 11,840.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1923` | 11,900,000.00 USD | 11,900,000.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1926` | 11,930,000.00 USD | 11,930,000.00 USD | 11,600.00 USD | 13,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1944` | 11,930,000.00 USD | 11,930,000.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.1467` | 9,530,000.00 USD | 0.00 USD | 9,530,000.00 USD | 9,720.00 USD | 9,180.00 USD | 8,780.00 USD |
| `7D` | `0.1470` | 9,510,000.00 USD | 0.00 USD | 9,510,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD |
| `1D` | `0.1473` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 9,360.00 USD | 7,910.00 USD | 1,210.00 USD |
| `7D` | `0.1473` | 9,500,000.00 USD | 0.00 USD | 9,500,000.00 USD | 6,490.00 USD | 5,400.00 USD | 5,280.00 USD |
| `1D` | `0.1476` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 6,530.00 USD | 1,060.00 USD | 2,800.00 USD |
| `7D` | `0.1476` | 9,480,000.00 USD | 0.00 USD | 9,480,000.00 USD | 0.00 USD | 14,780.00 USD | 5,320.00 USD |
| `1D` | `0.1479` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 16,640.00 USD | 14,840.00 USD | 3,930.00 USD |
| `7D` | `0.1479` | 9,460,000.00 USD | 0.00 USD | 9,460,000.00 USD | 0.00 USD | 39,730.00 USD | 14,560.00 USD |
| `1D` | `0.1482` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 5,680.00 USD | 6,350.00 USD | 12,260.00 USD |
| `7D` | `0.1482` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 41,960.00 USD | 20,720.00 USD | 27,030.00 USD |
| `1D` | `0.1485` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 9,730.00 USD | 3,320.00 USD | 4,710.00 USD |
| `7D` | `0.1485` | 9,320,000.00 USD | 0.00 USD | 9,320,000.00 USD | 16,180.00 USD | 7,340.00 USD | 38,270.00 USD |
| `1D` | `0.1488` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 2,660.00 USD | 5,180.00 USD | 7,250.00 USD |
| `7D` | `0.1488` | 9,250,000.00 USD | 0.00 USD | 9,250,000.00 USD | 20,860.00 USD | 3,130.00 USD | 10,390.00 USD |
| `1D` | `0.1491` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 7,650.00 USD | 10,490.00 USD | 6,890.00 USD |
| `7D` | `0.1491` | 9,220,000.00 USD | 0.00 USD | 9,220,000.00 USD | 33,540.00 USD | 17,020.00 USD | 28,410.00 USD |
| `1D` | `0.1494` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 14,210.00 USD | 5,270.00 USD | 2,510.00 USD |
| `7D` | `0.1494` | 9,140,000.00 USD | 0.00 USD | 9,140,000.00 USD | 34,220.00 USD | 9,890.00 USD | 14,210.00 USD |
| `1D` | `0.1497` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 2,530.00 USD |
| `7D` | `0.1497` | 9,080,000.00 USD | 0.00 USD | 9,080,000.00 USD | 20,880.00 USD | 17,180.00 USD | 9,710.00 USD |
| `1D` | `0.1500` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 2,670.00 USD | 0.00 USD | 3,370.00 USD |
| `7D` | `0.1500` | 9,030,000.00 USD | 0.00 USD | 9,030,000.00 USD | 46,820.00 USD | 5,810.00 USD | 21,940.00 USD |
| `1D` | `0.1503` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 3,610.00 USD | 2,640.00 USD | 1,360.00 USD |
| `7D` | `0.1503` | 8,960,000.00 USD | 0.00 USD | 8,960,000.00 USD | 11,490.00 USD | 13,450.00 USD | 9,950.00 USD |
| `1D` | `0.1506` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 5,430.00 USD | 640.88 USD | 7,720.00 USD |
| `7D` | `0.1506` | 8,920,000.00 USD | 0.00 USD | 8,920,000.00 USD | 33,170.00 USD | 18,020.00 USD | 65,400.00 USD |
| `1D` | `0.1509` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 5,640.00 USD | 3,940.00 USD | 0.00 USD |
| `7D` | `0.1509` | 8,810,000.00 USD | 0.00 USD | 8,810,000.00 USD | 17,340.00 USD | 9,550.00 USD | 24,150.00 USD |
| `1D` | `0.1512` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 0.00 USD | 4,360.00 USD | 2,500.00 USD |
| `7D` | `0.1512` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 18,600.00 USD | 8,620.00 USD | 26,910.00 USD |
| `1D` | `0.1515` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 0.00 USD | 1,730.00 USD | 2,640.00 USD |
| `7D` | `0.1515` | 8,700,000.00 USD | 0.00 USD | 8,700,000.00 USD | 53,430.00 USD | 13,330.00 USD | 53,490.00 USD |
| `1D` | `0.1518` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 14,340.00 USD | 4,320.00 USD | 8,700.00 USD |
| `7D` | `0.1518` | 8,580,000.00 USD | 0.00 USD | 8,580,000.00 USD | 46,830.00 USD | 15,160.00 USD | 64,360.00 USD |
| `1D` | `0.1521` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 9,450.00 USD | 1,470.00 USD | 11,330.00 USD |
| `7D` | `0.1521` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 47,740.00 USD | 6,920.00 USD | 38,800.00 USD |
| `1D` | `0.1524` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 1,870.00 USD | 2,970.00 USD | 7,150.00 USD |
| `7D` | `0.1524` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 37,550.00 USD | 13,950.00 USD | 11,280.00 USD |
| `1D` | `0.1527` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 3,300.00 USD | 0.00 USD | 11,570.00 USD |
| `7D` | `0.1527` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 56,950.00 USD | 30,410.00 USD | 33,080.00 USD |
| `1D` | `0.1530` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 4,960.00 USD | 5,040.00 USD | 8,740.00 USD |
| `7D` | `0.1530` | 8,180,000.00 USD | 0.00 USD | 8,180,000.00 USD | 54,790.00 USD | 9,880.00 USD | 16,070.00 USD |
| `1D` | `0.1533` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 14,310.00 USD | 1,900.00 USD | 3,140.00 USD |
| `7D` | `0.1533` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 10,760.00 USD | 16,570.00 USD | 21,560.00 USD |
| `1D` | `0.1536` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 4,320.00 USD | 5,590.00 USD | 3,210.00 USD |
| `7D` | `0.1536` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 37,160.00 USD | 2,910.00 USD | 13,450.00 USD |
| `1D` | `0.1539` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 2,920.00 USD | 6,640.00 USD | 1,240.00 USD |
| `7D` | `0.1539` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 22,990.00 USD | 18,230.00 USD | 5,070.00 USD |
| `1D` | `0.1542` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 1,710.00 USD | 0.00 USD | 4,490.00 USD |
| `7D` | `0.1542` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 0.00 USD | 3,590.00 USD | 4,670.00 USD |
| `1D` | `0.1545` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 13,270.00 USD | 3,200.00 USD | 1,730.00 USD |
| `7D` | `0.1545` | 7,940,000.00 USD | 0.00 USD | 7,940,000.00 USD | 9,250.00 USD | 0.00 USD | 5,620.00 USD |
| `1D` | `0.1548` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 1,140.00 USD | 8,660.00 USD | 1,070.00 USD |
| `7D` | `0.1548` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD |
| `1D` | `0.1551` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 4,810.00 USD | 4,140.00 USD | 3,890.00 USD |
| `7D` | `0.1551` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 34,670.00 USD | 11,820.00 USD | 0.00 USD |
| `1D` | `0.1554` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 14,410.00 USD | 15,630.00 USD | 7,190.00 USD |
| `7D` | `0.1554` | 7,880,000.00 USD | 0.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 6,470.00 USD |
| `1D` | `0.1557` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 0.00 USD | 3,410.00 USD | 3,250.00 USD |
| `7D` | `0.1557` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 0.00 USD | 4,510.00 USD | 10,800.00 USD |
| `1D` | `0.1560` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 2,970.00 USD | 11,300.00 USD | 5,580.00 USD |
| `7D` | `0.1560` | 7,860,000.00 USD | 0.00 USD | 7,860,000.00 USD | 0.00 USD | 6,480.00 USD | 0.00 USD |
| `1D` | `0.1563` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 3,050.00 USD | 1,050.00 USD | 16,050.00 USD |
| `7D` | `0.1563` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 0.00 USD | 19,950.00 USD | 9,840.00 USD |
| `1D` | `0.1566` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 45,560.00 USD | 11,570.00 USD | 15,060.00 USD |
| `7D` | `0.1566` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 50,480.00 USD | 29,160.00 USD | 26,780.00 USD |
| `1D` | `0.1569` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 24,600.00 USD | 31,270.00 USD | 7,030.00 USD |
| `7D` | `0.1569` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 15,590.00 USD | 5,100.00 USD | 11,900.00 USD |
| `1D` | `0.1572` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 34,670.00 USD | 14,240.00 USD | 17,830.00 USD |
| `7D` | `0.1572` | 7,680,000.00 USD | 0.00 USD | 7,680,000.00 USD | 40,760.00 USD | 34,450.00 USD | 17,760.00 USD |
| `1D` | `0.1575` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 34,430.00 USD | 19,170.00 USD | 6,610.00 USD |
| `7D` | `0.1575` | 7,590,000.00 USD | 0.00 USD | 7,590,000.00 USD | 23,310.00 USD | 88,960.00 USD | 21,360.00 USD |
| `1D` | `0.1578` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 59,420.00 USD | 64,050.00 USD | 24,570.00 USD |
| `7D` | `0.1578` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 58,590.00 USD | 84,670.00 USD | 67,670.00 USD |
| `1D` | `0.1581` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 31,970.00 USD | 6,220.00 USD | 22,540.00 USD |
| `7D` | `0.1581` | 7,240,000.00 USD | 0.00 USD | 7,240,000.00 USD | 92,720.00 USD | 58,880.00 USD | 57,600.00 USD |
| `1D` | `0.1584` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 34,630.00 USD | 11,050.00 USD | 15,490.00 USD |
| `7D` | `0.1584` | 7,030,000.00 USD | 0.00 USD | 7,030,000.00 USD | 80,450.00 USD | 35,780.00 USD | 123,970.00 USD |
| `1D` | `0.1587` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 9,930.00 USD | 21,380.00 USD | 21,480.00 USD |
| `7D` | `0.1587` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 69,180.00 USD | 22,370.00 USD | 38,480.00 USD |
| `1D` | `0.1590` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 13,490.00 USD | 27,950.00 USD | 8,270.00 USD |
| `7D` | `0.1590` | 6,660,000.00 USD | 0.00 USD | 6,660,000.00 USD | 71,200.00 USD | 44,110.00 USD | 71,640.00 USD |
| `1D` | `0.1593` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 44,300.00 USD | 6,320.00 USD | 30,800.00 USD |
| `7D` | `0.1593` | 6,480,000.00 USD | 0.00 USD | 6,480,000.00 USD | 69,430.00 USD | 56,020.00 USD | 68,480.00 USD |
| `1D` | `0.1596` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 29,470.00 USD | 19,190.00 USD | 31,820.00 USD |
| `7D` | `0.1596` | 6,280,000.00 USD | 0.00 USD | 6,280,000.00 USD | 161,460.00 USD | 85,250.00 USD | 120,230.00 USD |
| `1D` | `0.1599` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 76,280.00 USD | 16,990.00 USD | 33,120.00 USD |
| `7D` | `0.1599` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 219,060.00 USD | 55,380.00 USD | 87,990.00 USD |
| `1D` | `0.1602` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 55,540.00 USD | 46,820.00 USD | 7,880.00 USD |
| `7D` | `0.1602` | 5,550,000.00 USD | 0.00 USD | 5,550,000.00 USD | 44,770.00 USD | 46,490.00 USD | 40,380.00 USD |
| `1D` | `0.1605` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 34,500.00 USD | 18,980.00 USD | 37,670.00 USD |
| `7D` | `0.1605` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 177,720.00 USD | 136,660.00 USD | 217,140.00 USD |
| `1D` | `0.1608` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 66,600.00 USD | 35,780.00 USD | 22,620.00 USD |
| `7D` | `0.1608` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 129,610.00 USD | 174,940.00 USD | 131,300.00 USD |
| `1D` | `0.1611` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 132,780.00 USD | 132,510.00 USD | 51,740.00 USD |
| `7D` | `0.1611` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 148,170.00 USD | 227,820.00 USD | 233,470.00 USD |
| `1D` | `0.1614` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 55,510.00 USD | 30,350.00 USD | 53,590.00 USD |
| `7D` | `0.1614` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 323,670.00 USD | 194,680.00 USD | 282,150.00 USD |
| `1D` | `0.1617` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 73,170.00 USD | 27,450.00 USD | 30,050.00 USD |
| `7D` | `0.1617` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 346,150.00 USD | 98,680.00 USD | 418,480.00 USD |
| `1D` | `0.1620` | 908,360.00 USD | 0.00 USD | 908,360.00 USD | 77,700.00 USD | 54,730.00 USD | 92,330.00 USD |
| `7D` | `0.1620` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 303,960.00 USD | 134,660.00 USD | 294,710.00 USD |
| `1D` | `0.1623` | 683,600.00 USD | 0.00 USD | 683,600.00 USD | 53,880.00 USD | 67,020.00 USD | 31,480.00 USD |
| `7D` | `0.1623` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 297,830.00 USD | 122,030.00 USD | 248,770.00 USD |
| `1D` | `0.1626` | 531,220.00 USD | 0.00 USD | 531,220.00 USD | 19,820.00 USD | 12,640.00 USD | 41,800.00 USD |
| `7D` | `0.1626` | 779,190.00 USD | 0.00 USD | 779,190.00 USD | 234,280.00 USD | 71,120.00 USD | 0.00 USD |
| `1D` | `0.1629` | 456,970.00 USD | 0.00 USD | 456,970.00 USD | 14,220.00 USD | 33,030.00 USD | 19,620.00 USD |
| `7D` | `0.1629` | 473,790.00 USD | 0.00 USD | 473,790.00 USD | 171,310.00 USD | 0.00 USD | 20,860.00 USD |
| `1D` | `0.1632` | 390,100.00 USD | 0.00 USD | 390,100.00 USD | 25,750.00 USD | 19,630.00 USD | 17,370.00 USD |
| `7D` | `0.1632` | 281,630.00 USD | 0.00 USD | 281,630.00 USD | 9,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1635` | 327,340.00 USD | 0.00 USD | 327,340.00 USD | 37,200.00 USD | 6,390.00 USD | 11,860.00 USD |
| `7D` | `0.1635` | 272,420.00 USD | 0.00 USD | 272,420.00 USD | 0.00 USD | 13,670.00 USD | 21,360.00 USD |
| `1D` | `0.1638` | 271,890.00 USD | 0.00 USD | 271,890.00 USD | 9,410.00 USD | 22,520.00 USD | 42,790.00 USD |
| `7D` | `0.1638` | 237,380.00 USD | 0.00 USD | 237,380.00 USD | 0.00 USD | 0.00 USD | 62,410.00 USD |
| `1D` | `0.1641` | 197,170.00 USD | 0.00 USD | 197,170.00 USD | 7,360.00 USD | 9,300.00 USD | 10,340.00 USD |
| `7D` | `0.1641` | 174,980.00 USD | 0.00 USD | 174,980.00 USD | 22,480.00 USD | 29,240.00 USD | 0.00 USD |
| `1D` | `0.1644` | 170,170.00 USD | 0.00 USD | 170,170.00 USD | 25,590.00 USD | 25,250.00 USD | 11,410.00 USD |
| `7D` | `0.1644` | 123,260.00 USD | 0.00 USD | 123,260.00 USD | 0.00 USD | 8,990.00 USD | 26,230.00 USD |
| `1D` | `0.1647` | 107,910.00 USD | 0.00 USD | 107,910.00 USD | 40,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1647` | 88,040.00 USD | 0.00 USD | 88,040.00 USD | 34,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1650` | 53,280.00 USD | 0.00 USD | 53,280.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD |
| `1D` | `0.1653` | 67,880.00 USD | 0.00 USD | 67,880.00 USD | 0.00 USD | 16,860.00 USD | 0.00 USD |
| `7D` | `0.1653` | 46,280.00 USD | 0.00 USD | 46,280.00 USD | 33,810.00 USD | 12,460.00 USD | 0.00 USD |
| `7D` | `0.1654` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1656` | 51,020.00 USD | 0.00 USD | 51,020.00 USD | 0.00 USD | 51,020.00 USD | 0.00 USD |
| `7D` | `0.1656` | 63,240.00 USD | 63,240.00 USD | 0.00 USD | 43,910.00 USD | 19,330.00 USD | 0.00 USD |
| `1D` | `0.1657` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1659` | 44,690.00 USD | 44,690.00 USD | 0.00 USD | 25,450.00 USD | 19,240.00 USD | 0.00 USD |
| `7D` | `0.1659` | 104,020.00 USD | 104,020.00 USD | 0.00 USD | 40,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1662` | 80,380.00 USD | 80,380.00 USD | 0.00 USD | 8,220.00 USD | 6,760.00 USD | 20,710.00 USD |
| `7D` | `0.1662` | 237,310.00 USD | 237,310.00 USD | 0.00 USD | 48,590.00 USD | 62,020.00 USD | 22,670.00 USD |
| `1D` | `0.1665` | 147,470.00 USD | 147,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 67,090.00 USD |
| `7D` | `0.1665` | 414,510.00 USD | 414,510.00 USD | 0.00 USD | 87,050.00 USD | 32,780.00 USD | 57,360.00 USD |
| `1D` | `0.1668` | 164,410.00 USD | 164,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,940.00 USD |
| `7D` | `0.1668` | 508,260.00 USD | 508,260.00 USD | 0.00 USD | 11,410.00 USD | 39,630.00 USD | 42,720.00 USD |
| `1D` | `0.1671` | 185,130.00 USD | 185,130.00 USD | 0.00 USD | 20,720.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1671` | 641,290.00 USD | 641,290.00 USD | 0.00 USD | 70,540.00 USD | 62,490.00 USD | 0.00 USD |
| `1D` | `0.1674` | 206,440.00 USD | 206,440.00 USD | 0.00 USD | 21,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1674` | 775,200.00 USD | 775,200.00 USD | 0.00 USD | 44,960.00 USD | 88,950.00 USD | 0.00 USD |
| `1D` | `0.1677` | 221,060.00 USD | 221,060.00 USD | 0.00 USD | 14,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1677` | 899,050.00 USD | 899,050.00 USD | 0.00 USD | 59,010.00 USD | 64,850.00 USD | 0.00 USD |
| `1D` | `0.1680` | 301,050.00 USD | 301,050.00 USD | 0.00 USD | 75,420.00 USD | 4,560.00 USD | 0.00 USD |
| `7D` | `0.1680` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 101,910.00 USD | 68,430.00 USD | 15,310.00 USD |
| `1D` | `0.1683` | 387,680.00 USD | 387,680.00 USD | 0.00 USD | 80,310.00 USD | 3,200.00 USD | 3,130.00 USD |
| `7D` | `0.1683` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD |
| `1D` | `0.1686` | 441,160.00 USD | 441,160.00 USD | 0.00 USD | 6,560.00 USD | 23,410.00 USD | 23,510.00 USD |
| `7D` | `0.1686` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD |
| `1D` | `0.1689` | 448,140.00 USD | 448,140.00 USD | 0.00 USD | 0.00 USD | 6,980.00 USD | 0.00 USD |
| `7D` | `0.1689` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 38,670.00 USD | 40,690.00 USD |
| `1D` | `0.1692` | 583,900.00 USD | 583,900.00 USD | 0.00 USD | 55,320.00 USD | 66,160.00 USD | 14,290.00 USD |
| `7D` | `0.1692` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 21,780.00 USD | 32,070.00 USD | 0.00 USD |
| `1D` | `0.1695` | 606,200.00 USD | 606,200.00 USD | 0.00 USD | 0.00 USD | 22,300.00 USD | 0.00 USD |
| `7D` | `0.1695` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 30,490.00 USD | 28,010.00 USD |
| `1D` | `0.1698` | 683,690.00 USD | 683,690.00 USD | 0.00 USD | 20,810.00 USD | 56,690.00 USD | 0.00 USD |
| `7D` | `0.1698` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 56,860.00 USD | 18,830.00 USD |
| `7D` | `0.1701` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 22,820.00 USD | 25,330.00 USD | 0.00 USD |
| `1D` | `0.1704` | 708,350.00 USD | 708,350.00 USD | 0.00 USD | 0.00 USD | 14,420.00 USD | 10,240.00 USD |
| `7D` | `0.1704` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 46,880.00 USD | 0.00 USD |
| `1D` | `0.1707` | 822,330.00 USD | 822,330.00 USD | 0.00 USD | 37,960.00 USD | 71,860.00 USD | 4,150.00 USD |
| `7D` | `0.1707` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 59,520.00 USD |
| `1D` | `0.1710` | 830,360.00 USD | 830,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,040.00 USD |
| `7D` | `0.1710` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 25,490.00 USD | 5,180.00 USD |
| `1D` | `0.1713` | 847,690.00 USD | 847,690.00 USD | 0.00 USD | 0.00 USD | 17,320.00 USD | 0.00 USD |
| `7D` | `0.1713` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD |
| `1D` | `0.1716` | 881,560.00 USD | 881,560.00 USD | 0.00 USD | 0.00 USD | 25,600.00 USD | 8,270.00 USD |
| `7D` | `0.1716` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,160.00 USD |
| `1D` | `0.1719` | 932,820.00 USD | 932,820.00 USD | 0.00 USD | 34,230.00 USD | 8,520.00 USD | 8,520.00 USD |
| `7D` | `0.1719` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,410.00 USD |
| `1D` | `0.1722` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 100,000.00 USD | 16,860.00 USD | 45,350.00 USD |
| `7D` | `0.1722` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 118,060.00 USD | 0.00 USD | 362,840.00 USD |
| `1D` | `0.1725` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33,410.00 USD |
| `1D` | `0.1728` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD |
| `7D` | `0.1731` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 476,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1734` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD |
| `1D` | `0.1737` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 29,560.00 USD | 9,510.00 USD | 0.00 USD |
| `7D` | `0.1737` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 52,610.00 USD |
| `1D` | `0.1740` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 1,600.00 USD | 9,640.00 USD |
| `7D` | `0.1740` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,200.00 USD |
| `1D` | `0.1743` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD |
| `7D` | `0.1743` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1746` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 8,530.00 USD | 2,460.00 USD | 9,500.00 USD |
| `1D` | `0.1749` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 80,070.00 USD | 2,280.00 USD | 39,700.00 USD |
| `7D` | `0.1749` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 22,890.00 USD |
| `1D` | `0.1752` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 23,850.00 USD | 0.00 USD | 32,640.00 USD |
| `7D` | `0.1752` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 263,630.00 USD |
| `1D` | `0.1755` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 21,260.00 USD | 16,650.00 USD | 35,390.00 USD |
| `7D` | `0.1755` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 37,610.00 USD | 0.00 USD | 177,430.00 USD |
| `1D` | `0.1758` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 71,330.00 USD | 31,940.00 USD | 51,130.00 USD |
| `7D` | `0.1758` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 195,390.00 USD | 38,670.00 USD | 8,600.00 USD |
| `1D` | `0.1761` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 53,970.00 USD | 88,390.00 USD | 50,220.00 USD |
| `7D` | `0.1761` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 352,270.00 USD | 115,470.00 USD | 32,350.00 USD |
| `1D` | `0.1764` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 34,410.00 USD | 25,840.00 USD | 61,480.00 USD |
| `7D` | `0.1764` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 144,160.00 USD | 205,820.00 USD | 40,340.00 USD |
| `1D` | `0.1767` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 27,430.00 USD | 52,820.00 USD | 52,230.00 USD |
| `7D` | `0.1767` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 176,410.00 USD | 128,100.00 USD | 8,530.00 USD |
| `1D` | `0.1770` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 36,140.00 USD | 47,810.00 USD | 38,500.00 USD |
| `7D` | `0.1770` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 61,490.00 USD | 98,420.00 USD | 44,400.00 USD |
| `1D` | `0.1773` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 30,810.00 USD | 28,980.00 USD | 22,840.00 USD |
| `7D` | `0.1773` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 103,820.00 USD | 81,060.00 USD | 0.00 USD |
| `1D` | `0.1776` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 85,560.00 USD | 19,390.00 USD | 21,010.00 USD |
| `7D` | `0.1776` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 135,140.00 USD | 59,720.00 USD | 0.00 USD |
| `1D` | `0.1779` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 27,480.00 USD | 77,730.00 USD | 25,130.00 USD |
| `7D` | `0.1779` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 52,730.00 USD | 46,410.00 USD | 131,820.00 USD |
| `1D` | `0.1782` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 46,310.00 USD | 14,240.00 USD | 47,040.00 USD |
| `7D` | `0.1782` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 20,690.00 USD | 13,990.00 USD | 31,180.00 USD |
| `1D` | `0.1785` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 96,920.00 USD | 46,180.00 USD | 14,990.00 USD |
| `7D` | `0.1785` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 153,160.00 USD | 78,850.00 USD | 16,420.00 USD |
| `1D` | `0.1788` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 18,550.00 USD | 42,480.00 USD | 36,930.00 USD |
| `7D` | `0.1788` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 73,130.00 USD | 18,250.00 USD | 14,040.00 USD |
| `1D` | `0.1791` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 36,940.00 USD | 15,630.00 USD | 18,080.00 USD |
| `7D` | `0.1791` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 155,720.00 USD | 17,360.00 USD | 3,940.00 USD |
| `1D` | `0.1794` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 36,860.00 USD | 47,980.00 USD | 12,730.00 USD |
| `7D` | `0.1794` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 27,100.00 USD | 42,780.00 USD | 36,780.00 USD |
| `1D` | `0.1797` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 27,280.00 USD | 22,110.00 USD | 36,970.00 USD |
| `7D` | `0.1797` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 17,130.00 USD | 12,930.00 USD | 7,670.00 USD |
| `1D` | `0.1800` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 5,820.00 USD | 8,690.00 USD | 25,360.00 USD |
| `7D` | `0.1800` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 0.00 USD | 34,680.00 USD | 64,620.00 USD |
| `1D` | `0.1803` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 10,270.00 USD | 35,880.00 USD | 12,560.00 USD |
| `7D` | `0.1803` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 35,280.00 USD | 25,700.00 USD | 18,250.00 USD |
| `1D` | `0.1806` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 5,900.00 USD | 14,370.00 USD | 11,890.00 USD |
| `7D` | `0.1806` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 11,410.00 USD | 56,850.00 USD | 19,880.00 USD |
| `1D` | `0.1809` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 27,060.00 USD | 27,370.00 USD | 7,030.00 USD |
| `7D` | `0.1809` | 6,730,000.00 USD | 6,730,000.00 USD | 0.00 USD | 53,670.00 USD | 30,810.00 USD | 58,890.00 USD |
| `1D` | `0.1812` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 46,990.00 USD | 44,940.00 USD | 28,530.00 USD |
| `7D` | `0.1812` | 6,830,000.00 USD | 6,830,000.00 USD | 0.00 USD | 34,960.00 USD | 16,640.00 USD | 50,510.00 USD |
| `1D` | `0.1815` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 9,730.00 USD | 3,320.00 USD | 11,550.00 USD |
| `7D` | `0.1815` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 60,010.00 USD | 30,810.00 USD | 38,270.00 USD |
| `1D` | `0.1818` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 37,120.00 USD | 11,780.00 USD | 27,150.00 USD |
| `7D` | `0.1818` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 75,040.00 USD | 24,140.00 USD | 10,390.00 USD |
| `1D` | `0.1821` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 21,220.00 USD | 19,510.00 USD | 9,370.00 USD |
| `7D` | `0.1821` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 40,950.00 USD | 33,870.00 USD | 41,820.00 USD |
| `1D` | `0.1824` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 11,560.00 USD | 18,270.00 USD | 16,470.00 USD |
| `7D` | `0.1824` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 39,400.00 USD | 17,880.00 USD | 103,440.00 USD |
| `1D` | `0.1827` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 21,440.00 USD | 6,860.00 USD | 4,170.00 USD |
| `7D` | `0.1827` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 79,610.00 USD | 18,690.00 USD | 65,670.00 USD |
| `1D` | `0.1830` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 4,510.00 USD | 5,690.00 USD |
| `7D` | `0.1830` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 64,890.00 USD | 20,550.00 USD | 52,010.00 USD |
| `1D` | `0.1833` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 2,670.00 USD | 0.00 USD | 4,630.00 USD |
| `7D` | `0.1833` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 186,730.00 USD | 49,740.00 USD | 26,350.00 USD |
| `1D` | `0.1836` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 3,610.00 USD | 0.00 USD | 728.16 USD |
| `7D` | `0.1836` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 29,580.00 USD | 83,110.00 USD | 52,650.00 USD |
| `1D` | `0.1839` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 2,640.00 USD | 7,830.00 USD |
| `7D` | `0.1839` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 129,950.00 USD | 41,230.00 USD | 114,190.00 USD |
| `1D` | `0.1842` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 5,430.00 USD | 3,330.00 USD | 1,250.00 USD |
| `7D` | `0.1842` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 71,550.00 USD | 26,100.00 USD | 62,140.00 USD |
| `1D` | `0.1845` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 5,640.00 USD | 5,640.00 USD | 1,890.00 USD |
| `7D` | `0.1845` | 8,630,000.00 USD | 8,630,000.00 USD | 0.00 USD | 34,630.00 USD | 8,590.00 USD | 66,720.00 USD |
| `1D` | `0.1848` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 4,360.00 USD | 4,500.00 USD |
| `7D` | `0.1848` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 26,600.00 USD | 65,230.00 USD | 26,910.00 USD |
| `1D` | `0.1851` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD | 2,640.00 USD |
| `7D` | `0.1851` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 94,780.00 USD | 28,290.00 USD | 220,580.00 USD |
| `1D` | `0.1854` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 4,290.00 USD | 1,690.00 USD | 4,220.00 USD |
| `7D` | `0.1854` | 9,270,000.00 USD | 9,270,000.00 USD | 0.00 USD | 105,210.00 USD | 4,290.00 USD | 63,060.00 USD |
| `1D` | `0.1857` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 10,050.00 USD | 2,630.00 USD | 12,090.00 USD |
| `7D` | `0.1857` | 9,530,000.00 USD | 9,530,000.00 USD | 0.00 USD | 103,990.00 USD | 32,070.00 USD | 127,480.00 USD |
| `1D` | `0.1860` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 9,450.00 USD | 4,440.00 USD | 5,820.00 USD |
| `7D` | `0.1860` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 87,180.00 USD | 72,430.00 USD | 74,870.00 USD |
| `1D` | `0.1863` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD | 8,320.00 USD |
| `7D` | `0.1863` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 71,330.00 USD | 56,440.00 USD | 61,380.00 USD |
| `1D` | `0.1866` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 3,300.00 USD | 0.00 USD | 5,140.00 USD |
| `7D` | `0.1866` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 82,960.00 USD | 29,050.00 USD | 39,240.00 USD |
| `1D` | `0.1869` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 4,960.00 USD | 1,740.00 USD | 9,730.00 USD |
| `7D` | `0.1869` | 10,400,000.00 USD | 10,400,000.00 USD | 0.00 USD | 159,230.00 USD | 58,520.00 USD | 78,120.00 USD |
| `1D` | `0.1872` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 12,350.00 USD | 5,200.00 USD | 5,320.00 USD |
| `7D` | `0.1872` | 10,700,000.00 USD | 10,700,000.00 USD | 0.00 USD | 80,790.00 USD | 127,580.00 USD | 93,980.00 USD |
| `1D` | `0.1874` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 1,960.00 USD | 2,820.00 USD | 0.00 USD |
| `7D` | `0.1875` | 10,820,000.00 USD | 10,820,000.00 USD | 0.00 USD | 51,690.00 USD | 30,090.00 USD | 36,560.00 USD |
| `7D` | `0.1878` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 55,660.00 USD | 12,570.00 USD | 30,220.00 USD |
| `7D` | `0.1881` | 11,000,000.00 USD | 11,000,000.00 USD | 0.00 USD | 29,820.00 USD | 31,710.00 USD | 13,200.00 USD |
| `7D` | `0.1884` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 0.00 USD | 31,900.00 USD | 4,670.00 USD |
| `7D` | `0.1887` | 11,080,000.00 USD | 11,080,000.00 USD | 0.00 USD | 22,970.00 USD | 0.00 USD | 25,760.00 USD |
| `7D` | `0.1890` | 11,210,000.00 USD | 11,210,000.00 USD | 0.00 USD | 36,740.00 USD | 17,330.00 USD | 75,130.00 USD |
| `7D` | `0.1893` | 11,270,000.00 USD | 11,270,000.00 USD | 0.00 USD | 32,450.00 USD | 6,940.00 USD | 16,820.00 USD |
| `7D` | `0.1896` | 11,360,000.00 USD | 11,360,000.00 USD | 0.00 USD | 52,170.00 USD | 27,440.00 USD | 18,680.00 USD |
| `7D` | `0.1899` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 11,530.00 USD | 38,530.00 USD | 20,420.00 USD |
| `7D` | `0.1902` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 14,330.00 USD | 0.00 USD | 10,800.00 USD |
| `7D` | `0.1905` | 11,520,000.00 USD | 11,520,000.00 USD | 0.00 USD | 8,720.00 USD | 24,800.00 USD | 24,210.00 USD |
| `7D` | `0.1908` | 11,610,000.00 USD | 11,610,000.00 USD | 0.00 USD | 25,220.00 USD | 43,160.00 USD | 28,600.00 USD |
| `7D` | `0.1911` | 11,620,000.00 USD | 11,620,000.00 USD | 0.00 USD | 0.00 USD | 9,380.00 USD | 0.00 USD |
| `7D` | `0.1914` | 11,640,000.00 USD | 11,640,000.00 USD | 0.00 USD | 7,460.00 USD | 11,160.00 USD | 0.00 USD |
| `7D` | `0.1917` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 0.00 USD | 11,840.00 USD | 11,900.00 USD |
| `7D` | `0.1923` | 11,690,000.00 USD | 11,690,000.00 USD | 0.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD |
| `7D` | `0.1926` | 11,710,000.00 USD | 11,710,000.00 USD | 0.00 USD | 11,600.00 USD | 13,630.00 USD | 0.00 USD |
| `7D` | `0.1944` | 11,720,000.00 USD | 11,720,000.00 USD | 0.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `202.74M` | Total OI Tokens: `1,224,328,401.8 ARB`
  * 1h OI Change: `-2.26%` | 4h OI Change: `-6.79%` | 24h OI Change: `-15.56%`
  * Exchange Breakdown: Binance=`46.02M` | Bybit=`28.36M` | OKX=`16.21M` | Hyperliquid=`14.60M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `5.20K` | Last 24h: `10.97K` | Last 3d: `22.34K` | Last 7d: `43.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0049%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0039%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0015%` | **USDT Bitget** | `0.0069%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `45.00%` | `55.00%` | `0.82` | 8,400,000.00 USD |
| `15M` | `Binance` | `44.68%` | `55.32%` | `0.81` | 2,820,000.00 USD |
| `15M` | `OKX` | `44.49%` | `55.51%` | `0.80` | 1,250,000.00 USD |
| `15M` | `Bybit` | `45.42%` | `54.58%` | `0.83` | 665,740.00 USD |
| `15M` | `KuCoin` | `44.23%` | `55.77%` | `0.79` | 68,350.00 USD |
| `15M` | `Gate` | `52.78%` | `47.22%` | `1.12` | 444,290.00 USD |
| `15M` | `Bitget` | `41.14%` | `58.86%` | `0.70` | 442,680.00 USD |
| `15M` | `BingX` | `54.94%` | `45.06%` | `1.22` | 385,530.00 USD |
| `15M` | `MEXC` | `45.2%` | `54.8%` | `0.82` | 1,140,000.00 USD |
| `15M` | `Bitunix` | `47.92%` | `52.08%` | `0.92` | 307,540.00 USD |
| `15M` | `Hyperliquid` | `16.55%` | `83.45%` | `0.20` | 267,460.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.02%` | `48.98%` | `1.04` | 470,980.00 USD |
| `15M` | `Crypto.com` | `28.12%` | `71.88%` | `0.39` | 3,380.00 USD |
| `15M` | `WhiteBIT` | `60.2%` | `39.8%` | `1.51` | 68,020.00 USD |
| `15M` | `HTX` | `50.36%` | `49.64%` | `1.01` | 1,660.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `46.44%` | `53.56%` | `0.87` | 28,330.00 USD |
| `15M` | `Aster` | `2.39%` | `97.61%` | `0.02` | 5,130.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `5.31%` | `94.69%` | `0.06` | 36,290.00 USD |
| `15M` | `Whale Positions` | `44.68%` | `55.32%` | `0.81` | 2,820,000.00 USD |
| `15M` | `Global Accounts` | `45.00%` | `55.00%` | `0.82` | 8,400,000.00 USD |
| `1H` | `ARB` | `47.44%` | `52.56%` | `0.90` | 12,610,000.00 USD |
| `1H` | `Binance` | `50.22%` | `49.78%` | `1.01` | 4,440,000.00 USD |
| `1H` | `OKX` | `49.13%` | `50.87%` | `0.97` | 1,650,000.00 USD |
| `1H` | `Bybit` | `49.7%` | `50.3%` | `0.99` | 1,030,000.00 USD |
| `1H` | `KuCoin` | `46.38%` | `53.62%` | `0.86` | 109,420.00 USD |
| `1H` | `Gate` | `49.03%` | `50.97%` | `0.96` | 534,860.00 USD |
| `1H` | `Bitget` | `39.61%` | `60.39%` | `0.66` | 812,380.00 USD |
| `1H` | `BingX` | `33.32%` | `66.68%` | `0.50` | 867,440.00 USD |
| `1H` | `MEXC` | `47.69%` | `52.31%` | `0.91` | 1,380,000.00 USD |
| `1H` | `Bitunix` | `49.57%` | `50.43%` | `0.98` | 386,460.00 USD |
| `1H` | `Hyperliquid` | `17.51%` | `82.49%` | `0.21` | 362,910.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.7%` | `49.3%` | `1.03` | 606,430.00 USD |
| `1H` | `Crypto.com` | `35.27%` | `64.73%` | `0.54` | 4,190.00 USD |
| `1H` | `WhiteBIT` | `78.02%` | `21.98%` | `3.55` | 306,280.00 USD |
| `1H` | `HTX` | `46.42%` | `53.58%` | `0.87` | 1,990.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `53.97%` | `46.03%` | `1.17` | 37,140.00 USD |
| `1H` | `Aster` | `7.73%` | `92.27%` | `0.08` | 5,770.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `27.99%` | `72.01%` | `0.39` | 63,340.00 USD |
| `1H` | `Whale Positions` | `50.22%` | `49.78%` | `1.01` | 4,440,000.00 USD |
| `1H` | `Global Accounts` | `47.44%` | `52.56%` | `0.90` | 12,610,000.00 USD |
| `4H` | `ARB` | `45.99%` | `54.01%` | `0.85` | 45,320,000.00 USD |
| `4H` | `Binance` | `46.58%` | `53.42%` | `0.87` | 16,830,000.00 USD |
| `4H` | `OKX` | `42.56%` | `57.44%` | `0.74` | 7,870,000.00 USD |
| `4H` | `Bybit` | `48.95%` | `51.05%` | `0.96` | 3,660,000.00 USD |
| `4H` | `KuCoin` | `49.23%` | `50.77%` | `0.97` | 456,650.00 USD |
| `4H` | `Gate` | `48.36%` | `51.64%` | `0.94` | 1,860,000.00 USD |
| `4H` | `Bitget` | `39.37%` | `60.63%` | `0.65` | 2,320,000.00 USD |
| `4H` | `BingX` | `34.78%` | `65.22%` | `0.53` | 2,410,000.00 USD |
| `4H` | `MEXC` | `45.11%` | `54.89%` | `0.82` | 4,460,000.00 USD |
| `4H` | `Bitunix` | `48.78%` | `51.22%` | `0.95` | 876,200.00 USD |
| `4H` | `Hyperliquid` | `38.62%` | `61.38%` | `0.63` | 872,200.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.18%` | `49.82%` | `1.01` | 2,120,000.00 USD |
| `4H` | `Crypto.com` | `56.26%` | `43.74%` | `1.29` | 23,090.00 USD |
| `4H` | `WhiteBIT` | `81.68%` | `18.32%` | `4.46` | 1,260,000.00 USD |
| `4H` | `HTX` | `42.29%` | `57.71%` | `0.73` | 9,260.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `30.46%` | `69.54%` | `0.44` | 134,550.00 USD |
| `4H` | `Aster` | `48.14%` | `51.86%` | `0.93` | 21,420.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `35.08%` | `64.92%` | `0.54` | 147,440.00 USD |
| `4H` | `Whale Positions` | `46.58%` | `53.42%` | `0.87` | 16,830,000.00 USD |
| `4H` | `Global Accounts` | `45.99%` | `54.01%` | `0.85` | 45,320,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1689` | `0.1689` | `0.1689` | `0.1697` | `0.1682` | 1,292,914.43 USD | 712,068.28 USD | 580,846.15 USD | 131,222.13 USD | `+10.15%` | `38B / 24S` |
| `0:00 UTC` | `0.1690` | `0.1697` | `0.1690` | `0.1704` | `0.1690` | 952,197.22 USD | 428,970.00 USD | 523,227.22 USD | -94,257.22 USD | `-9.90%` | `28B / 31S` |
| `5:00 UTC` | `0.1686` | `0.1691` | `0.1686` | `0.1698` | `0.1685` | 581,095.74 USD | 286,225.77 USD | 294,869.97 USD | -8,644.20 USD | `-1.49%` | `37B / 26S` |
| `0:00 UTC` | `0.1678` | `0.1678` | `0.1678` | `0.1689` | `0.1673` | 1,127,023.46 USD | 573,365.61 USD | 553,657.86 USD | 19,707.75 USD | `+1.75%` | `27B / 19S` |
| `5:00 UTC` | `0.1687` | `0.1687` | `0.1687` | `0.1691` | `0.1680` | 541,507.84 USD | 294,376.97 USD | 247,130.87 USD | 47,246.11 USD | `+8.72%` | `31B / 8S` |
| `0:00 UTC` | `0.1684` | `0.1682` | `0.1684` | `0.1688` | `0.1678` | 593,121.43 USD | 297,803.46 USD | 295,317.97 USD | 2,485.50 USD | `+0.42%` | `13B / 13S` |
| `5:00 UTC` | `0.1683` | `0.1683` | `0.1683` | `0.1688` | `0.1678` | 375,189.89 USD | 244,846.62 USD | 130,343.28 USD | 114,503.34 USD | `+30.52%` | `33B / 4S` |
| `0:00 UTC` | `0.1688` | `0.1688` | `0.1688` | `0.1693` | `0.1682` | 680,766.88 USD | 453,606.46 USD | 227,160.42 USD | 226,446.04 USD | `+33.26%` | `32B / 8S` |
| `5:00 UTC` | `0.1682` | `0.1683` | `0.1682` | `0.1688` | `0.1681` | 452,736.37 USD | 213,244.89 USD | 239,491.48 USD | -26,246.58 USD | `-5.80%` | `7B / 12S` |
| `0:00 UTC` | `0.1667` | `0.1655` | `0.1667` | `0.1684` | `0.1640` | 2,312,571.42 USD | 997,254.34 USD | 1,315,317.08 USD | -318,062.75 USD | `-13.75%` | `2B / 25S` |

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
| `5m` | 44,390.00 USD | 272,760.00 USD | **`ACCUMULATION`** |
| `15m` | -293,130.00 USD | -569,870.00 USD | **`DISTRIBUTION`** |
| `30m` | -341,920.00 USD | -506,450.00 USD | **`DISTRIBUTION`** |
| `1h` | -302,060.00 USD | -97,520.00 USD | **`DISTRIBUTION`** |
| `2h` | -460,410.00 USD | -211,430.00 USD | **`DISTRIBUTION`** |
| `4h` | -477,900.00 USD | -2,240,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -350,170.00 USD | -2,640,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -322,630.00 USD | -4,660,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 123,660.00 USD | -3,940,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,090,000.00 USD | -6,420,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,100,000.00 USD | -30,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -32,400,000.00 USD | -163,120,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+44.39K` | 15m=`-293.13K` | 1h=`-302.06K` | 24h=`-1.09M`
* Futures Capital Netflows: 5m=`+272.76K` | 15m=`-569.87K` | 1h=`-97.52K` | 24h=`-6.42M`
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
  * `2026-10-30 01:36:09 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:09 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:51:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
