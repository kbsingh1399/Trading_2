# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-29 21:43:08 IST` (`2026-10-29 16:13:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1699` | `0.1705` | `0.1695` | `0.1703` | `1,527,674` | 259,555.91 USD | -74,466.33 USD | `-28.69%` | -3,439,464.10 USD | `-0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.1702` | `0.1707` | `0.1701` | `0.1702` | `1,928,417` | 328,477.41 USD | 30,004.15 USD | `+9.13%` | -3,409,459.95 USD | `+0.72` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1702` | `0.1706` | `0.1699` | `0.1706` | `640,916` | 109,118.46 USD | -8,695.54 USD | `-7.97%` | -3,418,155.49 USD | `+0.31` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1703` | `0.1704` | `0.1685` | `0.1695` | `8,495,311` | 1,438,333.93 USD | -27,169.77 USD | `-1.89%` | -3,306,300.42 USD | `+0.19` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1695` | `0.1709` | `0.1692` | `0.1699` | `5,194,934` | 883,684.54 USD | -58,697.35 USD | `-6.64%` | -3,364,997.77 USD | `-0.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1699` | `0.1707` | `0.1695` | `0.1705` | `4,088,605` | 695,719.06 USD | -54,420.04 USD | `-7.82%` | -3,419,417.80 USD | `+0.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1679` | `0.1710` | `0.1674` | `0.1710` | `20,153,799` | 3,413,798.22 USD | -137,463.54 USD | `-4.03%` | -2,805,262.29 USD | `-0.05` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1710` | `0.1721` | `0.1685` | `0.1699` | `31,149,077` | 5,311,624.45 USD | -446,111.27 USD | `-8.40%` | -3,251,373.56 USD | `-0.76` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1699` | `0.1707` | `0.1695` | `0.1705` | `4,088,605` | 695,719.06 USD | -54,420.04 USD | `-7.82%` | -3,305,793.59 USD | `+0.20` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1652` | `0.1687` | `0.1623` | `0.1631` | `68,085,678` | 11,252,816.65 USD | -909,329.92 USD | `-8.08%` | -1,808,589.83 USD | `-1.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -2,239,583.64 USD | `+0.05` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1721` | `0.1674` | `0.1705` | `55,390,990` | 9,421,058.07 USD | -637,911.18 USD | `-6.77%` | -2,877,494.82 USD | `-0.47` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1746` | `0.1786` | `0.1714` | `0.1721` | `102,259,485` | 17,888,371.07 USD | -498,373.45 USD | `-2.79%` | -1,103,169.20 USD | `+1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1721` | `0.1729` | `0.1635` | `0.1652` | `91,809,989` | 15,344,891.97 USD | 203,909.29 USD | `+1.33%` | -899,259.91 USD | `+1.40` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1652` | `0.1687` | `0.1623` | `0.1631` | `68,085,678` | 11,252,816.65 USD | -909,329.92 USD | `-8.08%` | -1,808,589.83 USD | `-1.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -2,239,583.64 USD | `+0.05` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1721` | `0.1674` | `0.1705` | `55,390,990` | 9,421,058.07 USD | -637,911.18 USD | `-6.77%` | -2,877,494.82 USD | `-0.47` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 19:44:05 IST` |

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
  * 24H Horizon: Short MP=`0.1784` (Vol: 147,300.00 USD, Dist: `+4.64%`) | Long MP=`0.1598` (Vol: 147,500.00 USD, Dist: `--6.28%`)
  * 48H Horizon: Short MP=`0.1784` (Vol: 147,300.00 USD, Dist: `+4.64%`) | Long MP=`0.1598` (Vol: 154,300.00 USD, Dist: `--6.28%`)
  * 3D Horizon: Short MP=`0.1784` (Vol: 147,300.00 USD, Dist: `+4.64%`) | Long MP=`0.1598` (Vol: 205,900.00 USD, Dist: `--6.28%`)
  * 7D Horizon: Short MP=`0.1875` (Vol: 158,800.00 USD, Dist: `+9.98%`) | Long MP=`0.1613` (Vol: 344,500.00 USD, Dist: `--5.38%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0365` | 1,700.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0375` | 453.49 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0385` | 1,490.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 287.82 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 170.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0445` | 2,890.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0455` | 27,650.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0465` | 8,460.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0475` | 4,840.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 348.13 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 2,750.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 1,730.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 289.43 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0535` | 668.38 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 3,290.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 15,650.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 4,030.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,210.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 69,060.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 99,790.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 481.35 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 143.87 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 2,970.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 6,620.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 111.58 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,540.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 4,290.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 14,690.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 7,550.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 5,020.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 12,000.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 576.40 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 13,950.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 19,230.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 362.62 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 39,150.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 23,870.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 2,040.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 13,450.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 40,270.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 106.21 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 589.63 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 145.24 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 3,700.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 13,750.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 1,850.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 1,890.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 3,620.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 6,500.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 12,500.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 181.20 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 1,060.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 826.86 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 534.49 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 425.50 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1125` | 584.94 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 3,490.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 20,630.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 4,700.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 9,150.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 1,560.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 26,700.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 1,830.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 3,970.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 3,410.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 636.74 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 32,960.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 1,040.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 4,850.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 1,200.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 7,340.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 154,540.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 4,010.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 24,110.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 10,500.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 19,880.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 24,250.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 4,720.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 13,550.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1365` | 2,550.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1375` | 1,410.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1385` | 4,360.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1395` | 6,100.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 16,610.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 12,560.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 484,630.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 19,330.00 USD | 747,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 52,350.00 USD | 727,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1453` | 10,360,000.00 USD | 10,360,000.00 USD | 0.00 USD | 5,660.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 2,500.00 USD | 675,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1456` | 10,340,000.00 USD | 10,340,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1459` | 10,340,000.00 USD | 10,340,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1465` | 10,330,000.00 USD | 10,330,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 34,280.00 USD | 673,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1468` | 10,330,000.00 USD | 10,330,000.00 USD | 9,720.00 USD | 9,180.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1471` | 10,300,000.00 USD | 10,300,000.00 USD | 6,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1474` | 10,290,000.00 USD | 10,290,000.00 USD | 6,490.00 USD | 9,220.00 USD | 5,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 78,150.00 USD | 638,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1477` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 25,460.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1480` | 10,240,000.00 USD | 10,240,000.00 USD | 6,990.00 USD | 29,300.00 USD | 20,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1483` | 10,180,000.00 USD | 10,180,000.00 USD | 42,230.00 USD | 16,640.00 USD | 33,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,650.00 USD | 560,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1486` | 10,090,000.00 USD | 10,090,000.00 USD | 18,610.00 USD | 10,470.00 USD | 25,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1489` | 10,040,000.00 USD | 10,040,000.00 USD | 11,170.00 USD | 3,710.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1492` | 10,010,000.00 USD | 10,010,000.00 USD | 40,320.00 USD | 17,880.00 USD | 27,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1495` | 9,930,000.00 USD | 9,930,000.00 USD | 34,650.00 USD | 18,690.00 USD | 12,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 66,380.00 USD | 557,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1498` | 9,860,000.00 USD | 9,860,000.00 USD | 42,100.00 USD | 9,610.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1501` | 9,800,000.00 USD | 9,800,000.00 USD | 21,010.00 USD | 7,930.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1504` | 9,750,000.00 USD | 9,750,000.00 USD | 17,800.00 USD | 11,590.00 USD | 44,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1505` | 102,290.00 USD | 491,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1507` | 9,680,000.00 USD | 9,680,000.00 USD | 28,940.00 USD | 12,910.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1509` | 4,030,000.00 USD | 4,030,000.00 USD | 5,640.00 USD | 6,000.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1510` | 9,610,000.00 USD | 9,610,000.00 USD | 12,660.00 USD | 12,930.00 USD | 29,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1511` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 4,360.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1513` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 2,260.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1513` | 9,550,000.00 USD | 9,550,000.00 USD | 32,900.00 USD | 17,610.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1515` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 886.43 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 5,420.00 USD | 389,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1516` | 9,460,000.00 USD | 9,460,000.00 USD | 54,550.00 USD | 0.00 USD | 43,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1517` | 4,000,000.00 USD | 4,000,000.00 USD | 4,860.00 USD | 1,690.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1519` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1519` | 9,360,000.00 USD | 9,360,000.00 USD | 37,430.00 USD | 19,520.00 USD | 70,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1521` | 3,980,000.00 USD | 3,980,000.00 USD | 9,450.00 USD | 1,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1522` | 9,240,000.00 USD | 9,240,000.00 USD | 49,800.00 USD | 9,640.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1523` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 2,970.00 USD | 3,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1525` | 3,960,000.00 USD | 3,960,000.00 USD | 1,870.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1525` | 9,150,000.00 USD | 9,150,000.00 USD | 25,790.00 USD | 13,700.00 USD | 19,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1525` | 41,470.00 USD | 383,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1527` | 3,960,000.00 USD | 3,960,000.00 USD | 3,300.00 USD | 0.00 USD | 8,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1528` | 9,090,000.00 USD | 9,090,000.00 USD | 75,690.00 USD | 27,110.00 USD | 27,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1529` | 3,950,000.00 USD | 3,950,000.00 USD | 4,960.00 USD | 1,740.00 USD | 1,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1531` | 3,940,000.00 USD | 3,940,000.00 USD | 3,990.00 USD | 3,300.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1531` | 8,960,000.00 USD | 8,960,000.00 USD | 35,030.00 USD | 8,400.00 USD | 16,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1533` | 3,930,000.00 USD | 3,930,000.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1534` | 8,900,000.00 USD | 8,900,000.00 USD | 15,780.00 USD | 17,430.00 USD | 20,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1535` | 3,920,000.00 USD | 3,920,000.00 USD | 2,670.00 USD | 2,760.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 19,400.00 USD | 342,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1537` | 3,920,000.00 USD | 3,920,000.00 USD | 1,650.00 USD | 2,440.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1537` | 8,850,000.00 USD | 8,850,000.00 USD | 28,060.00 USD | 5,880.00 USD | 10,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1539` | 3,900,000.00 USD | 3,900,000.00 USD | 5,810.00 USD | 5,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1540` | 8,800,000.00 USD | 8,800,000.00 USD | 14,000.00 USD | 6,530.00 USD | 5,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1541` | 3,890,000.00 USD | 3,890,000.00 USD | 1,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1543` | 3,890,000.00 USD | 3,890,000.00 USD | 8,050.00 USD | 0.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1543` | 8,780,000.00 USD | 8,780,000.00 USD | 9,250.00 USD | 3,590.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1545` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 3,150.00 USD | 7,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1545` | 26,170.00 USD | 322,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1546` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 0.00 USD | 5,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1547` | 3,870,000.00 USD | 3,870,000.00 USD | 1,140.00 USD | 4,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1549` | 3,870,000.00 USD | 3,870,000.00 USD | 4,810.00 USD | 3,490.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1549` | 8,760,000.00 USD | 8,760,000.00 USD | 11,570.00 USD | 6,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1551` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 2,500.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1552` | 8,740,000.00 USD | 8,740,000.00 USD | 23,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1553` | 3,850,000.00 USD | 3,850,000.00 USD | 7,030.00 USD | 6,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1555` | 3,840,000.00 USD | 3,840,000.00 USD | 4,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1555` | 40,060.00 USD | 296,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1558` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 4,510.00 USD | 5,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1559` | 3,830,000.00 USD | 3,830,000.00 USD | 2,490.00 USD | 1,210.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1561` | 3,830,000.00 USD | 3,830,000.00 USD | 2,970.00 USD | 0.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1563` | 3,810,000.00 USD | 3,810,000.00 USD | 3,050.00 USD | 1,050.00 USD | 9,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1564` | 8,700,000.00 USD | 8,700,000.00 USD | 24,300.00 USD | 19,310.00 USD | 21,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1565` | 3,800,000.00 USD | 3,800,000.00 USD | 24,770.00 USD | 8,680.00 USD | 5,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1565` | 33,750.00 USD | 256,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1567` | 3,760,000.00 USD | 3,760,000.00 USD | 27,450.00 USD | 2,890.00 USD | 11,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1567` | 8,640,000.00 USD | 8,640,000.00 USD | 41,770.00 USD | 15,360.00 USD | 15,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1569` | 3,720,000.00 USD | 3,720,000.00 USD | 15,110.00 USD | 21,230.00 USD | 13,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1570` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 0.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1571` | 3,670,000.00 USD | 3,670,000.00 USD | 21,680.00 USD | 6,810.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1573` | 3,630,000.00 USD | 3,630,000.00 USD | 26,560.00 USD | 21,710.00 USD | 14,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1573` | 8,560,000.00 USD | 8,560,000.00 USD | 58,830.00 USD | 47,690.00 USD | 25,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1575` | 3,570,000.00 USD | 3,570,000.00 USD | 24,450.00 USD | 13,110.00 USD | 6,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1575` | 6,040.00 USD | 222,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1576` | 8,420,000.00 USD | 8,420,000.00 USD | 26,600.00 USD | 102,190.00 USD | 54,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1577` | 3,520,000.00 USD | 3,520,000.00 USD | 40,840.00 USD | 41,600.00 USD | 27,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1579` | 3,410,000.00 USD | 3,410,000.00 USD | 39,660.00 USD | 22,460.00 USD | 22,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1579` | 8,240,000.00 USD | 8,240,000.00 USD | 101,500.00 USD | 95,190.00 USD | 42,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1581` | 3,330,000.00 USD | 3,330,000.00 USD | 14,290.00 USD | 8,570.00 USD | 17,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1582` | 8,000,000.00 USD | 8,000,000.00 USD | 56,130.00 USD | 13,480.00 USD | 89,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1583` | 3,290,000.00 USD | 3,290,000.00 USD | 23,370.00 USD | 14,430.00 USD | 24,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1585` | 3,230,000.00 USD | 3,230,000.00 USD | 13,780.00 USD | 10,140.00 USD | 13,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1585` | 7,840,000.00 USD | 7,840,000.00 USD | 87,110.00 USD | 50,340.00 USD | 75,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1585` | 2,870.00 USD | 216,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1587` | 3,190,000.00 USD | 3,190,000.00 USD | 8,200.00 USD | 21,130.00 USD | 17,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1588` | 7,630,000.00 USD | 7,630,000.00 USD | 34,830.00 USD | 30,030.00 USD | 41,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1589` | 3,140,000.00 USD | 3,140,000.00 USD | 19,760.00 USD | 15,390.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1591` | 3,100,000.00 USD | 3,100,000.00 USD | 17,020.00 USD | 23,990.00 USD | 19,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1591` | 7,520,000.00 USD | 7,520,000.00 USD | 110,640.00 USD | 49,670.00 USD | 60,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1593` | 3,040,000.00 USD | 3,040,000.00 USD | 38,070.00 USD | 1,580.00 USD | 22,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1594` | 7,300,000.00 USD | 7,300,000.00 USD | 85,560.00 USD | 39,260.00 USD | 102,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1595` | 2,980,000.00 USD | 2,980,000.00 USD | 30,500.00 USD | 15,690.00 USD | 37,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1595` | 65,110.00 USD | 214,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1597` | 2,890,000.00 USD | 2,890,000.00 USD | 48,470.00 USD | 25,620.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1597` | 7,070,000.00 USD | 7,070,000.00 USD | 228,850.00 USD | 96,110.00 USD | 102,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1599` | 2,790,000.00 USD | 2,790,000.00 USD | 36,120.00 USD | 10,360.00 USD | 38,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1600` | 6,650,000.00 USD | 6,650,000.00 USD | 105,580.00 USD | 38,830.00 USD | 76,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1601` | 2,710,000.00 USD | 2,710,000.00 USD | 42,790.00 USD | 46,180.00 USD | 31,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1603` | 2,590,000.00 USD | 2,590,000.00 USD | 27,870.00 USD | 20,230.00 USD | 10,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1603` | 6,420,000.00 USD | 6,420,000.00 USD | 62,240.00 USD | 54,840.00 USD | 81,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1605` | 2,530,000.00 USD | 2,530,000.00 USD | 33,160.00 USD | 27,190.00 USD | 52,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1605` | 20,630.00 USD | 148,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1606` | 6,230,000.00 USD | 6,230,000.00 USD | 211,140.00 USD | 149,480.00 USD | 227,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1607` | 2,420,000.00 USD | 2,420,000.00 USD | 43,410.00 USD | 28,600.00 USD | 6,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1609` | 2,340,000.00 USD | 2,340,000.00 USD | 30,200.00 USD | 56,960.00 USD | 49,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1609` | 5,640,000.00 USD | 5,640,000.00 USD | 92,990.00 USD | 229,060.00 USD | 182,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1611` | 2,200,000.00 USD | 2,200,000.00 USD | 128,630.00 USD | 100,850.00 USD | 46,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1612` | 5,130,000.00 USD | 5,130,000.00 USD | 291,500.00 USD | 250,360.00 USD | 159,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1613` | 1,920,000.00 USD | 1,920,000.00 USD | 41,630.00 USD | 17,080.00 USD | 54,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1615` | 1,810,000.00 USD | 1,810,000.00 USD | 39,560.00 USD | 50,320.00 USD | 50,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1615` | 4,430,000.00 USD | 4,430,000.00 USD | 300,450.00 USD | 107,900.00 USD | 374,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1615` | 16,530.00 USD | 128,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1617` | 1,670,000.00 USD | 1,670,000.00 USD | 52,540.00 USD | 8,620.00 USD | 13,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1618` | 3,650,000.00 USD | 3,650,000.00 USD | 310,070.00 USD | 132,060.00 USD | 318,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1619` | 1,600,000.00 USD | 1,600,000.00 USD | 33,520.00 USD | 41,410.00 USD | 75,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1621` | 1,450,000.00 USD | 1,450,000.00 USD | 39,550.00 USD | 42,370.00 USD | 20,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1621` | 2,890,000.00 USD | 2,890,000.00 USD | 228,220.00 USD | 154,980.00 USD | 316,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1623` | 1,340,000.00 USD | 1,340,000.00 USD | 28,670.00 USD | 50,760.00 USD | 13,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1624` | 2,190,000.00 USD | 2,190,000.00 USD | 381,800.00 USD | 138,890.00 USD | 119,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1625` | 1,250,000.00 USD | 1,250,000.00 USD | 15,710.00 USD | 19,100.00 USD | 16,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1625` | 108,300.00 USD | 111,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1627` | 1,200,000.00 USD | 1,200,000.00 USD | 5,960.00 USD | 26,330.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1627` | 1,550,000.00 USD | 1,550,000.00 USD | 291,760.00 USD | 0.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1629` | 1,150,000.00 USD | 1,150,000.00 USD | 8,260.00 USD | 6,700.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1630` | 1,240,000.00 USD | 1,240,000.00 USD | 9,210.00 USD | 0.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1631` | 1,130,000.00 USD | 1,130,000.00 USD | 12,400.00 USD | 18,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1633` | 1,100,000.00 USD | 1,100,000.00 USD | 9,980.00 USD | 9,110.00 USD | 5,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1635` | 1,070,000.00 USD | 1,070,000.00 USD | 6,580.00 USD | 0.00 USD | 8,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1635` | 3,610.00 USD | 3,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1636` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 13,670.00 USD | 12,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1637` | 1,060,000.00 USD | 1,060,000.00 USD | 2,730.00 USD | 13,220.00 USD | 15,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1639` | 1,030,000.00 USD | 1,030,000.00 USD | 6,680.00 USD | 0.00 USD | 32,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1639` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 62,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1641` | 986,810.00 USD | 986,810.00 USD | 7,360.00 USD | 6,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1642` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 14,690.00 USD | 26,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1643` | 973,350.00 USD | 973,350.00 USD | 25,590.00 USD | 20,340.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1645` | 924,050.00 USD | 924,050.00 USD | 10,010.00 USD | 15,920.00 USD | 23,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1645` | 1,100,000.00 USD | 1,100,000.00 USD | 23,120.00 USD | 8,990.00 USD | 7,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1645` | 548.33 USD | 3,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1647` | 874,770.00 USD | 874,770.00 USD | 0.00 USD | 7,260.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1649` | 857,010.00 USD | 857,010.00 USD | 0.00 USD | 10,520.00 USD | 2,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1651` | 843,820.00 USD | 843,820.00 USD | 15,390.00 USD | 8,470.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1651` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 51,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1653` | 793,350.00 USD | 793,350.00 USD | 7,990.00 USD | 0.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1654` | 1,010,000.00 USD | 1,010,000.00 USD | 33,810.00 USD | 12,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1655` | 781,650.00 USD | 781,650.00 USD | 0.00 USD | 14,450.00 USD | 18,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1657` | 748,840.00 USD | 748,840.00 USD | 35,870.00 USD | 14,850.00 USD | 7,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1659` | 690,660.00 USD | 690,660.00 USD | 18,840.00 USD | 0.00 USD | 28,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1660` | 959,700.00 USD | 959,700.00 USD | 29,890.00 USD | 11,020.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1661` | 643,180.00 USD | 643,180.00 USD | 0.00 USD | 0.00 USD | 25,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1663` | 617,340.00 USD | 617,340.00 USD | 16,520.00 USD | 30,760.00 USD | 19,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1663` | 899,110.00 USD | 899,110.00 USD | 86,050.00 USD | 27,600.00 USD | 75,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1665` | 550,500.00 USD | 550,500.00 USD | 60,930.00 USD | 11,790.00 USD | 23,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1666` | 709,570.00 USD | 709,570.00 USD | 49,590.00 USD | 20,110.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1667` | 454,410.00 USD | 454,410.00 USD | 50,170.00 USD | 48,080.00 USD | 16,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1669` | 339,210.00 USD | 339,210.00 USD | 38,000.00 USD | 0.00 USD | 4,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1669` | 620,460.00 USD | 620,460.00 USD | 0.00 USD | 40,610.00 USD | 25,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1671` | 296,410.00 USD | 296,410.00 USD | 16,790.00 USD | 0.00 USD | 17,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1672` | 554,510.00 USD | 554,510.00 USD | 70,540.00 USD | 38,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1673` | 262,420.00 USD | 262,420.00 USD | 13,360.00 USD | 0.00 USD | 10,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1675` | 238,460.00 USD | 238,460.00 USD | 0.00 USD | 15,830.00 USD | 9,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1675` | 445,900.00 USD | 445,900.00 USD | 19,540.00 USD | 64,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1675` | 2,960.00 USD | 2,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1677` | 212,750.00 USD | 212,750.00 USD | 14,620.00 USD | 17,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1678` | 362,300.00 USD | 362,300.00 USD | 71,860.00 USD | 58,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1679` | 180,720.00 USD | 180,720.00 USD | 6,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1681` | 174,450.00 USD | 174,450.00 USD | 59,580.00 USD | 0.00 USD | 8,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1681` | 231,520.00 USD | 231,520.00 USD | 46,250.00 USD | 36,390.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1683` | 106,200.00 USD | 106,200.00 USD | 29,560.00 USD | 9,320.00 USD | 23,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1684` | 133,570.00 USD | 133,570.00 USD | 60,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1685` | 43,760.00 USD | 43,760.00 USD | 0.00 USD | 38,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1693` | 72,620.00 USD | 72,620.00 USD | 0.00 USD | 32,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1696` | 40,550.00 USD | 40,550.00 USD | 0.00 USD | 40,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1705` | 4,970.00 USD | 4,970.00 USD | 0.00 USD | 4,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1705` | 70,320.00 USD | 70,320.00 USD | 70,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1707` | 4,940.00 USD | 4,940.00 USD | 0.00 USD | 0.00 USD | 4,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1708` | 168,190.00 USD | 168,190.00 USD | 33,170.00 USD | 0.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1709` | 33,600.00 USD | 33,600.00 USD | 0.00 USD | 0.00 USD | 28,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1711` | 94,210.00 USD | 94,210.00 USD | 0.00 USD | 0.00 USD | 60,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1713` | 125,210.00 USD | 125,210.00 USD | 0.00 USD | 31,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1715` | 144,330.00 USD | 144,330.00 USD | 0.00 USD | 19,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1720` | 322,550.00 USD | 322,550.00 USD | 0.00 USD | 0.00 USD | 154,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1721` | 204,770.00 USD | 204,770.00 USD | 43,780.00 USD | 0.00 USD | 16,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1723` | 294,510.00 USD | 294,510.00 USD | 30,020.00 USD | 34,930.00 USD | 24,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1723` | 608,420.00 USD | 608,420.00 USD | 74,150.00 USD | 32,300.00 USD | 179,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1725` | 396,730.00 USD | 396,730.00 USD | 62,140.00 USD | 14,850.00 USD | 25,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1726` | 668,280.00 USD | 668,280.00 USD | 48,420.00 USD | 11,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1727` | 488,010.00 USD | 488,010.00 USD | 35,950.00 USD | 14,560.00 USD | 40,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1729` | 517,740.00 USD | 517,740.00 USD | 0.00 USD | 0.00 USD | 29,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1729` | 1,070,000.00 USD | 1,070,000.00 USD | 290,020.00 USD | 61,150.00 USD | 48,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1731` | 581,570.00 USD | 581,570.00 USD | 16,520.00 USD | 16,530.00 USD | 30,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1732` | 1,690,000.00 USD | 1,690,000.00 USD | 550,580.00 USD | 49,950.00 USD | 17,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1733` | 633,740.00 USD | 633,740.00 USD | 24,810.00 USD | 11,790.00 USD | 15,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1735` | 705,370.00 USD | 705,370.00 USD | 32,530.00 USD | 26,400.00 USD | 12,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1735` | 1,960,000.00 USD | 1,960,000.00 USD | 222,370.00 USD | 32,580.00 USD | 19,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1735` | 653.37 USD | 4,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1737` | 749,040.00 USD | 749,040.00 USD | 25,640.00 USD | 6,610.00 USD | 11,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1738` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 27,350.00 USD | 109,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1739` | 835,630.00 USD | 835,630.00 USD | 9,520.00 USD | 7,150.00 USD | 69,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1741` | 910,010.00 USD | 910,010.00 USD | 39,520.00 USD | 16,530.00 USD | 18,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1743` | 948,090.00 USD | 948,090.00 USD | 6,720.00 USD | 24,740.00 USD | 6,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1744` | 2,180,000.00 USD | 2,180,000.00 USD | 9,550.00 USD | 64,970.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1745` | 1,010,000.00 USD | 1,010,000.00 USD | 32,930.00 USD | 18,640.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1745` | 1,390.00 USD | 5,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1747` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 15,640.00 USD | 3,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1747` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 56,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1749` | 1,060,000.00 USD | 1,060,000.00 USD | 20,020.00 USD | 4,310.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1750` | 2,480,000.00 USD | 2,480,000.00 USD | 46,250.00 USD | 0.00 USD | 196,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1751` | 1,090,000.00 USD | 1,090,000.00 USD | 3,910.00 USD | 19,820.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1753` | 1,170,000.00 USD | 1,170,000.00 USD | 26,370.00 USD | 24,890.00 USD | 21,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1753` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 191,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1755` | 1,220,000.00 USD | 1,220,000.00 USD | 33,530.00 USD | 17,440.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1756` | 2,900,000.00 USD | 2,900,000.00 USD | 75,620.00 USD | 56,810.00 USD | 89,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1757` | 1,290,000.00 USD | 1,290,000.00 USD | 8,970.00 USD | 24,960.00 USD | 28,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1759` | 1,350,000.00 USD | 1,350,000.00 USD | 49,230.00 USD | 7,430.00 USD | 8,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1759` | 3,240,000.00 USD | 3,240,000.00 USD | 238,650.00 USD | 105,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1761` | 1,410,000.00 USD | 1,410,000.00 USD | 26,950.00 USD | 14,800.00 USD | 14,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1762` | 3,730,000.00 USD | 3,730,000.00 USD | 288,350.00 USD | 196,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1763` | 1,460,000.00 USD | 1,460,000.00 USD | 38,200.00 USD | 0.00 USD | 12,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1765` | 1,500,000.00 USD | 1,500,000.00 USD | 17,080.00 USD | 6,700.00 USD | 12,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1765` | 4,120,000.00 USD | 4,120,000.00 USD | 154,540.00 USD | 218,770.00 USD | 20,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1765` | 495.68 USD | 6,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1767` | 1,540,000.00 USD | 1,540,000.00 USD | 24,840.00 USD | 14,140.00 USD | 9,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1768` | 4,390,000.00 USD | 4,390,000.00 USD | 161,560.00 USD | 106,860.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1769` | 1,580,000.00 USD | 1,580,000.00 USD | 9,980.00 USD | 16,230.00 USD | 5,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1771` | 1,600,000.00 USD | 1,600,000.00 USD | 12,820.00 USD | 5,250.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1771` | 4,560,000.00 USD | 4,560,000.00 USD | 46,210.00 USD | 113,470.00 USD | 12,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1773` | 1,640,000.00 USD | 1,640,000.00 USD | 23,520.00 USD | 0.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1774` | 4,790,000.00 USD | 4,790,000.00 USD | 148,780.00 USD | 79,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1775` | 1,690,000.00 USD | 1,690,000.00 USD | 36,570.00 USD | 6,900.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1775` | 339.98 USD | 6,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1777` | 1,730,000.00 USD | 1,730,000.00 USD | 26,930.00 USD | 12,850.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1777` | 4,920,000.00 USD | 4,920,000.00 USD | 44,880.00 USD | 26,150.00 USD | 59,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1779` | 1,760,000.00 USD | 1,760,000.00 USD | 11,580.00 USD | 12,390.00 USD | 6,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1780` | 5,090,000.00 USD | 5,090,000.00 USD | 52,730.00 USD | 13,420.00 USD | 97,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1781` | 1,840,000.00 USD | 1,840,000.00 USD | 46,310.00 USD | 1,060.00 USD | 32,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1783` | 1,900,000.00 USD | 1,900,000.00 USD | 42,740.00 USD | 3,060.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1783` | 5,230,000.00 USD | 5,230,000.00 USD | 105,900.00 USD | 13,990.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1785` | 1,960,000.00 USD | 1,960,000.00 USD | 34,280.00 USD | 21,740.00 USD | 4,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1785` | 10,490.00 USD | 16,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1786` | 5,420,000.00 USD | 5,420,000.00 USD | 129,440.00 USD | 48,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1787` | 2,030,000.00 USD | 2,030,000.00 USD | 18,760.00 USD | 14,140.00 USD | 41,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1789` | 2,070,000.00 USD | 2,070,000.00 USD | 4,760.00 USD | 18,820.00 USD | 15,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1789` | 5,480,000.00 USD | 5,480,000.00 USD | 48,810.00 USD | 7,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1791` | 2,140,000.00 USD | 2,140,000.00 USD | 39,110.00 USD | 14,710.00 USD | 9,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1792` | 5,640,000.00 USD | 5,640,000.00 USD | 134,000.00 USD | 20,480.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1793` | 2,180,000.00 USD | 2,180,000.00 USD | 23,530.00 USD | 6,730.00 USD | 12,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1795` | 2,240,000.00 USD | 2,240,000.00 USD | 12,690.00 USD | 28,830.00 USD | 18,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1795` | 5,690,000.00 USD | 5,690,000.00 USD | 6,230.00 USD | 19,870.00 USD | 28,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1797` | 2,280,000.00 USD | 2,280,000.00 USD | 23,500.00 USD | 8,090.00 USD | 9,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1798` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 6,240.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1799` | 2,290,000.00 USD | 2,290,000.00 USD | 6,440.00 USD | 1,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1801` | 2,310,000.00 USD | 2,310,000.00 USD | 9,150.00 USD | 5,580.00 USD | 8,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1801` | 5,780,000.00 USD | 5,780,000.00 USD | 6,490.00 USD | 16,690.00 USD | 46,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1803` | 2,340,000.00 USD | 2,340,000.00 USD | 3,610.00 USD | 6,910.00 USD | 16,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1804` | 5,830,000.00 USD | 5,830,000.00 USD | 28,790.00 USD | 14,780.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1805` | 2,380,000.00 USD | 2,380,000.00 USD | 21,330.00 USD | 5,440.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1805` | 48,190.00 USD | 65,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1807` | 2,420,000.00 USD | 2,420,000.00 USD | 13,660.00 USD | 15,220.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1807` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 39,730.00 USD | 67,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1809` | 2,470,000.00 USD | 2,470,000.00 USD | 13,400.00 USD | 11,020.00 USD | 32,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1810` | 6,060,000.00 USD | 6,060,000.00 USD | 79,380.00 USD | 30,940.00 USD | 12,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1811` | 2,530,000.00 USD | 2,530,000.00 USD | 25,240.00 USD | 7,220.00 USD | 22,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1813` | 2,570,000.00 USD | 2,570,000.00 USD | 16,220.00 USD | 9,370.00 USD | 18,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1813` | 6,150,000.00 USD | 6,150,000.00 USD | 32,530.00 USD | 3,040.00 USD | 56,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1815` | 2,590,000.00 USD | 2,590,000.00 USD | 9,730.00 USD | 0.00 USD | 5,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1816` | 6,240,000.00 USD | 6,240,000.00 USD | 46,430.00 USD | 21,200.00 USD | 25,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1817` | 2,650,000.00 USD | 2,650,000.00 USD | 25,810.00 USD | 7,070.00 USD | 33,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1819` | 2,690,000.00 USD | 2,690,000.00 USD | 27,030.00 USD | 8,880.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1819` | 6,360,000.00 USD | 6,360,000.00 USD | 65,350.00 USD | 3,710.00 USD | 43,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1821` | 2,710,000.00 USD | 2,710,000.00 USD | 7,170.00 USD | 1,710.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1822` | 6,530,000.00 USD | 6,530,000.00 USD | 46,760.00 USD | 36,230.00 USD | 92,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1823` | 2,750,000.00 USD | 2,750,000.00 USD | 12,060.00 USD | 14,010.00 USD | 14,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1825` | 2,770,000.00 USD | 2,770,000.00 USD | 19,010.00 USD | 0.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1825` | 6,620,000.00 USD | 6,620,000.00 USD | 61,720.00 USD | 17,120.00 USD | 12,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1827` | 2,800,000.00 USD | 2,800,000.00 USD | 8,740.00 USD | 6,860.00 USD | 7,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1828` | 6,770,000.00 USD | 6,770,000.00 USD | 51,470.00 USD | 24,320.00 USD | 69,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1829` | 2,800,000.00 USD | 2,800,000.00 USD | 3,490.00 USD | 1,640.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1831` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 4,090.00 USD | 6,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1831` | 6,940,000.00 USD | 6,940,000.00 USD | 85,970.00 USD | 21,930.00 USD | 63,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1833` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 3,640.00 USD | 7,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1834` | 7,200,000.00 USD | 7,200,000.00 USD | 165,640.00 USD | 47,980.00 USD | 51,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1835` | 2,830,000.00 USD | 2,830,000.00 USD | 5,030.00 USD | 0.00 USD | 728.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1837` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 2,640.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1837` | 7,440,000.00 USD | 7,440,000.00 USD | 72,930.00 USD | 76,140.00 USD | 83,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1839` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 9,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1840` | 7,660,000.00 USD | 7,660,000.00 USD | 98,270.00 USD | 47,250.00 USD | 80,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1841` | 2,870,000.00 USD | 2,870,000.00 USD | 13,150.00 USD | 2,060.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1843` | 2,870,000.00 USD | 2,870,000.00 USD | 1,030.00 USD | 3,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1843` | 7,870,000.00 USD | 7,870,000.00 USD | 86,180.00 USD | 18,570.00 USD | 105,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1845` | 2,900,000.00 USD | 2,900,000.00 USD | 4,610.00 USD | 4,630.00 USD | 17,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1846` | 8,140,000.00 USD | 8,140,000.00 USD | 8,330.00 USD | 56,460.00 USD | 199,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1847` | 2,920,000.00 USD | 2,920,000.00 USD | 4,680.00 USD | 4,360.00 USD | 9,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1849` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 2,260.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1849` | 8,360,000.00 USD | 8,360,000.00 USD | 104,530.00 USD | 79,580.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1851` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 886.43 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1852` | 8,760,000.00 USD | 8,760,000.00 USD | 153,970.00 USD | 9,590.00 USD | 234,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1853` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 1,690.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1855` | 2,940,000.00 USD | 2,940,000.00 USD | 4,860.00 USD | 0.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1855` | 8,920,000.00 USD | 8,920,000.00 USD | 58,210.00 USD | 10,160.00 USD | 94,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1857` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1858` | 9,200,000.00 USD | 9,200,000.00 USD | 96,280.00 USD | 51,010.00 USD | 133,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1859` | 2,950,000.00 USD | 2,950,000.00 USD | 9,450.00 USD | 1,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1861` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 2,970.00 USD | 3,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1861` | 9,380,000.00 USD | 9,380,000.00 USD | 99,880.00 USD | 55,030.00 USD | 21,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1863` | 2,970,000.00 USD | 2,970,000.00 USD | 1,870.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1864` | 9,590,000.00 USD | 9,590,000.00 USD | 87,420.00 USD | 65,980.00 USD | 61,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1865` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 3,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1867` | 2,980,000.00 USD | 2,980,000.00 USD | 3,300.00 USD | 0.00 USD | 5,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1867` | 9,840,000.00 USD | 9,840,000.00 USD | 130,970.00 USD | 47,840.00 USD | 73,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1869` | 2,990,000.00 USD | 2,990,000.00 USD | 4,960.00 USD | 1,740.00 USD | 1,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1870` | 10,220,000.00 USD | 10,220,000.00 USD | 175,600.00 USD | 83,890.00 USD | 113,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1871` | 3,000,000.00 USD | 3,000,000.00 USD | 3,990.00 USD | 3,300.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1873` | 3,000,000.00 USD | 3,000,000.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1873` | 10,530,000.00 USD | 10,530,000.00 USD | 72,410.00 USD | 122,400.00 USD | 116,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1875` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1875` | 21,190.00 USD | 86,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1876` | 10,660,000.00 USD | 10,660,000.00 USD | 76,050.00 USD | 41,870.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1877` | 3,010,000.00 USD | 3,010,000.00 USD | 2,670.00 USD | 2,760.00 USD | 918.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1879` | 3,020,000.00 USD | 3,020,000.00 USD | 1,650.00 USD | 2,440.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1879` | 10,800,000.00 USD | 10,800,000.00 USD | 48,260.00 USD | 46,860.00 USD | 48,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1881` | 3,030,000.00 USD | 3,030,000.00 USD | 5,810.00 USD | 5,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1882` | 10,930,000.00 USD | 10,930,000.00 USD | 14,000.00 USD | 29,330.00 USD | 91,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1883` | 3,030,000.00 USD | 3,030,000.00 USD | 1,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1885` | 3,040,000.00 USD | 3,040,000.00 USD | 8,050.00 USD | 0.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1885` | 11,010,000.00 USD | 11,010,000.00 USD | 41,060.00 USD | 31,900.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1885` | 329.74 USD | 86,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1887` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 2,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1888` | 11,130,000.00 USD | 11,130,000.00 USD | 13,720.00 USD | 17,330.00 USD | 83,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1889` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 978.10 USD | 7,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1891` | 3,060,000.00 USD | 3,060,000.00 USD | 1,140.00 USD | 4,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1891` | 11,180,000.00 USD | 11,180,000.00 USD | 36,740.00 USD | 0.00 USD | 17,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1893` | 3,070,000.00 USD | 3,070,000.00 USD | 4,810.00 USD | 3,490.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1894` | 11,280,000.00 USD | 11,280,000.00 USD | 69,540.00 USD | 12,420.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1895` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 2,500.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1897` | 3,080,000.00 USD | 3,080,000.00 USD | 4,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1897` | 11,360,000.00 USD | 11,360,000.00 USD | 25,640.00 USD | 31,390.00 USD | 25,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1898` | 3,090,000.00 USD | 3,090,000.00 USD | 2,530.00 USD | 3,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1900` | 11,400,000.00 USD | 11,400,000.00 USD | 11,530.00 USD | 21,370.00 USD | 7,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1903` | 11,430,000.00 USD | 11,430,000.00 USD | 14,330.00 USD | 11,220.00 USD | 5,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1905` | 26,440.00 USD | 113,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1925` | 665.28 USD | 113,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1945` | 623.68 USD | 114,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1955` | 4,390.00 USD | 118,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1975` | 150.10 USD | 118,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1985` | 1,950.00 USD | 120,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1995` | 135.22 USD | 121,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2055` | 35,020.00 USD | 156,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2085` | 198.08 USD | 156,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2095` | 1,060.00 USD | 157,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2125` | 42,670.00 USD | 199,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2135` | 16,070.00 USD | 216,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 41,230.00 USD | 257,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2205` | 26,240.00 USD | 283,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2225` | 656.06 USD | 284,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 343.77 USD | 284,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2255` | 154.78 USD | 284,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 6,820.00 USD | 291,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2335` | 304.11 USD | 291,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 16,250.00 USD | 308,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 102.62 USD | 308,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 361.66 USD | 308,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 869.00 USD | 309,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2445` | 231.03 USD | 309,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2465` | 9,360.00 USD | 318,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2495` | 19,910.00 USD | 338,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2545` | 546.54 USD | 339,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 3,870.00 USD | 343,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2575` | 29,500.00 USD | 372,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 52,030.00 USD | 424,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 154.94 USD | 424,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2685` | 226.51 USD | 425,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 13,510.00 USD | 438,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 214.21 USD | 438,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 27,890.00 USD | 466,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2795` | 482.84 USD | 467,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2825` | 449.32 USD | 467,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 187.26 USD | 467,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 2,230.00 USD | 470,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 574.36 USD | 470,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3025` | 8,970.00 USD | 479,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 225.42 USD | 479,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3175` | 376.84 USD | 480,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3215` | 64,300.00 USD | 544,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3255` | 252.52 USD | 544,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 11,590.00 USD | 556,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3305` | 192.68 USD | 556,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3325` | 15,810.00 USD | 572,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3335` | 221.81 USD | 572,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3385` | 108.46 USD | 572,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3395` | 63,790.00 USD | 636,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0365` | 2,160,000.00 USD | 0.00 USD | 1,700.00 USD | `-78.54%` | `46,685,900,000,000.00` |
| `Live` | `Long` | `0.0375` | 2,160,000.00 USD | 0.00 USD | 453.49 USD | `-77.96%` | `12,093,000,000,000.00` |
| `Live` | `Long` | `0.0385` | 2,160,000.00 USD | 0.00 USD | 1,490.00 USD | `-77.37%` | `38,823,900,000,000.00` |
| `Live` | `Long` | `0.0415` | 2,160,000.00 USD | 0.00 USD | 287.82 USD | `-75.60%` | `6,935,500,000,000.00` |
| `Live` | `Long` | `0.0425` | 2,150,000.00 USD | 0.00 USD | 170.00 USD | `-75.02%` | `4,000,000,000,000.00` |
| `Live` | `Long` | `0.0445` | 2,150,000.00 USD | 0.00 USD | 2,890.00 USD | `-73.84%` | `65,000,000,000,000.00` |
| `Live` | `Long` | `0.0455` | 2,150,000.00 USD | 0.00 USD | 27,650.00 USD | `-73.25%` | `607,616,100,000,000.00` |
| `Live` | `Long` | `0.0465` | 2,120,000.00 USD | 0.00 USD | 8,460.00 USD | `-72.66%` | `181,960,400,000,000.00` |
| `Live` | `Long` | `0.0475` | 2,120,000.00 USD | 0.00 USD | 4,840.00 USD | `-72.08%` | `101,831,000,000,000.00` |
| `Live` | `Long` | `0.0485` | 2,110,000.00 USD | 0.00 USD | 348.13 USD | `-71.49%` | `7,178,000,000,000.00` |
| `Live` | `Long` | `0.0495` | 2,110,000.00 USD | 0.00 USD | 2,750.00 USD | `-70.90%` | `55,578,200,000,000.00` |
| `Live` | `Long` | `0.0505` | 2,110,000.00 USD | 0.00 USD | 1,730.00 USD | `-70.31%` | `34,249,500,000,000.00` |
| `Live` | `Long` | `0.0525` | 2,110,000.00 USD | 0.00 USD | 289.43 USD | `-69.14%` | `5,513,000,000,000.00` |
| `Live` | `Long` | `0.0535` | 2,110,000.00 USD | 0.00 USD | 668.38 USD | `-68.55%` | `12,493,000,000,000.00` |
| `Live` | `Long` | `0.0545` | 2,110,000.00 USD | 0.00 USD | 3,290.00 USD | `-67.96%` | `60,366,100,000,000.00` |
| `Live` | `Long` | `0.0565` | 2,100,000.00 USD | 0.00 USD | 15,650.00 USD | `-66.79%` | `276,984,000,000,000.00` |
| `Live` | `Long` | `0.0575` | 2,090,000.00 USD | 0.00 USD | 4,030.00 USD | `-66.20%` | `70,000,000,000,000.00` |
| `Live` | `Long` | `0.0625` | 2,080,000.00 USD | 0.00 USD | 1,210.00 USD | `-63.26%` | `19,414,500,000,000.00` |
| `Live` | `Long` | `0.0655` | 2,080,000.00 USD | 0.00 USD | 69,060.00 USD | `-61.50%` | `1,054,389,899,999,999.88` |
| `Live` | `Long` | `0.0675` | 2,010,000.00 USD | 0.00 USD | 99,790.00 USD | `-60.32%` | `1,478,385,900,000,000.00` |
| `Live` | `Long` | `0.0685` | 1,910,000.00 USD | 0.00 USD | 481.35 USD | `-59.73%` | `7,027,000,000,000.00` |
| `Live` | `Long` | `0.0695` | 1,910,000.00 USD | 0.00 USD | 143.87 USD | `-59.14%` | `2,070,000,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,910,000.00 USD | 0.00 USD | 2,970.00 USD | `-58.56%` | `42,142,800,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,910,000.00 USD | 0.00 USD | 6,620.00 USD | `-57.97%` | `92,602,800,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,900,000.00 USD | 0.00 USD | 111.58 USD | `-57.38%` | `1,539,100,000,000.00` |
| `Live` | `Long` | `0.0735` | 1,900,000.00 USD | 0.00 USD | 2,540.00 USD | `-56.79%` | `34,571,000,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,900,000.00 USD | 0.00 USD | 4,290.00 USD | `-56.20%` | `57,635,200,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,890,000.00 USD | 0.00 USD | 14,690.00 USD | `-55.03%` | `192,029,300,000,000.00` |
| `Live` | `Long` | `0.0785` | 1,880,000.00 USD | 0.00 USD | 7,550.00 USD | `-53.85%` | `96,199,600,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,870,000.00 USD | 0.00 USD | 5,020.00 USD | `-53.27%` | `63,148,600,000,000.00` |
| `Live` | `Long` | `0.0805` | 1,870,000.00 USD | 0.00 USD | 12,000.00 USD | `-52.68%` | `149,068,300,000,000.00` |
| `Live` | `Long` | `0.0815` | 1,860,000.00 USD | 0.00 USD | 576.40 USD | `-52.09%` | `7,072,400,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,860,000.00 USD | 0.00 USD | 13,950.00 USD | `-51.50%` | `169,093,500,000,000.00` |
| `Live` | `Long` | `0.0855` | 1,840,000.00 USD | 0.00 USD | 19,230.00 USD | `-49.74%` | `224,937,400,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,820,000.00 USD | 0.00 USD | 362.62 USD | `-47.97%` | `4,097,400,000,000.00` |
| `Live` | `Long` | `0.0895` | 1,820,000.00 USD | 0.00 USD | 39,150.00 USD | `-47.39%` | `437,419,000,000,000.00` |
| `Live` | `Long` | `0.0905` | 1,780,000.00 USD | 0.00 USD | 23,870.00 USD | `-46.80%` | `263,781,599,999,999.97` |
| `Live` | `Long` | `0.0925` | 1,760,000.00 USD | 0.00 USD | 2,040.00 USD | `-45.62%` | `22,044,300,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,760,000.00 USD | 0.00 USD | 13,450.00 USD | `-45.04%` | `143,885,100,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,740,000.00 USD | 0.00 USD | 40,270.00 USD | `-44.45%` | `426,141,000,000,000.00` |
| `Live` | `Long` | `0.0955` | 1,700,000.00 USD | 0.00 USD | 106.21 USD | `-43.86%` | `1,112,100,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,700,000.00 USD | 0.00 USD | 589.63 USD | `-43.27%` | `6,110,200,000,000.00` |
| `Live` | `Long` | `0.0975` | 1,700,000.00 USD | 0.00 USD | 145.24 USD | `-42.68%` | `1,489,600,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,700,000.00 USD | 0.00 USD | 3,700.00 USD | `-42.10%` | `37,516,700,000,000.00` |
| `Live` | `Long` | `0.0995` | 1,700,000.00 USD | 0.00 USD | 13,750.00 USD | `-41.51%` | `138,146,400,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,680,000.00 USD | 0.00 USD | 1,850.00 USD | `-40.92%` | `18,436,400,000,000.00` |
| `Live` | `Long` | `0.1025` | 1,680,000.00 USD | 0.00 USD | 1,890.00 USD | `-39.74%` | `18,433,100,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,680,000.00 USD | 0.00 USD | 3,620.00 USD | `-39.16%` | `34,994,600,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,680,000.00 USD | 0.00 USD | 6,500.00 USD | `-38.57%` | `62,191,700,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,670,000.00 USD | 0.00 USD | 12,500.00 USD | `-37.98%` | `118,523,000,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,660,000.00 USD | 0.00 USD | 181.20 USD | `-37.39%` | `1,701,400,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,660,000.00 USD | 0.00 USD | 1,060.00 USD | `-36.81%` | `9,856,300,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,660,000.00 USD | 0.00 USD | 826.86 USD | `-36.22%` | `7,620,800,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,660,000.00 USD | 0.00 USD | 534.49 USD | `-35.04%` | `4,837,000,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,660,000.00 USD | 0.00 USD | 425.50 USD | `-34.45%` | `3,816,100,000,000.00` |
| `Live` | `Long` | `0.1125` | 1,650,000.00 USD | 0.00 USD | 584.94 USD | `-33.87%` | `5,199,500,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,650,000.00 USD | 0.00 USD | 3,490.00 USD | `-33.28%` | `30,769,700,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,650,000.00 USD | 0.00 USD | 20,630.00 USD | `-32.69%` | `180,185,100,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,630,000.00 USD | 0.00 USD | 4,700.00 USD | `-32.10%` | `40,664,200,000,000.00` |
| `Live` | `Long` | `0.1165` | 1,630,000.00 USD | 0.00 USD | 9,150.00 USD | `-31.51%` | `78,498,000,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,620,000.00 USD | 0.00 USD | 1,560.00 USD | `-30.93%` | `13,261,500,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,610,000.00 USD | 0.00 USD | 26,700.00 USD | `-30.34%` | `225,310,600,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,590,000.00 USD | 0.00 USD | 1,830.00 USD | `-29.75%` | `15,286,200,000,000.00` |
| `Live` | `Long` | `0.1205` | 1,590,000.00 USD | 0.00 USD | 3,970.00 USD | `-29.16%` | `32,908,400,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,580,000.00 USD | 0.00 USD | 3,410.00 USD | `-28.58%` | `28,041,500,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,580,000.00 USD | 0.00 USD | 636.74 USD | `-27.99%` | `5,197,900,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,580,000.00 USD | 0.00 USD | 32,960.00 USD | `-27.40%` | `266,849,500,000,000.00` |
| `Live` | `Long` | `0.1245` | 1,550,000.00 USD | 0.00 USD | 1,040.00 USD | `-26.81%` | `8,332,800,000,000.00` |
| `Live` | `Long` | `0.1255` | 1,540,000.00 USD | 0.00 USD | 4,850.00 USD | `-26.22%` | `38,646,100,000,000.00` |
| `Live` | `Long` | `0.1265` | 1,540,000.00 USD | 0.00 USD | 1,200.00 USD | `-25.64%` | `9,489,700,000,000.00` |
| `Live` | `Long` | `0.1275` | 1,540,000.00 USD | 0.00 USD | 7,340.00 USD | `-25.05%` | `57,568,800,000,000.00` |
| `Live` | `Long` | `0.1285` | 1,530,000.00 USD | 0.00 USD | 154,540.00 USD | `-24.46%` | `1,202,661,500,000,000.00` |
| `Live` | `Long` | `0.1295` | 1,380,000.00 USD | 0.00 USD | 4,010.00 USD | `-23.87%` | `30,998,800,000,000.00` |
| `Live` | `Long` | `0.1305` | 1,370,000.00 USD | 0.00 USD | 24,110.00 USD | `-23.28%` | `184,736,500,000,000.00` |
| `Live` | `Long` | `0.1315` | 1,350,000.00 USD | 0.00 USD | 10,500.00 USD | `-22.70%` | `79,839,800,000,000.00` |
| `Live` | `Long` | `0.1325` | 1,340,000.00 USD | 0.00 USD | 19,880.00 USD | `-22.11%` | `150,000,000,000,000.00` |
| `Live` | `Long` | `0.1335` | 1,320,000.00 USD | 0.00 USD | 24,250.00 USD | `-21.52%` | `181,670,900,000,000.00` |
| `Live` | `Long` | `0.1345` | 1,290,000.00 USD | 0.00 USD | 4,720.00 USD | `-20.93%` | `35,089,000,000,000.00` |
| `Live` | `Long` | `0.1355` | 1,290,000.00 USD | 0.00 USD | 13,550.00 USD | `-20.35%` | `100,000,000,000,000.00` |
| `Live` | `Long` | `0.1365` | 1,280,000.00 USD | 0.00 USD | 2,550.00 USD | `-19.76%` | `18,677,900,000,000.00` |
| `Live` | `Long` | `0.1375` | 1,270,000.00 USD | 0.00 USD | 1,410.00 USD | `-19.17%` | `10,241,800,000,000.00` |
| `Live` | `Long` | `0.1385` | 1,270,000.00 USD | 0.00 USD | 4,360.00 USD | `-18.58%` | `31,491,000,000,000.00` |
| `Live` | `Long` | `0.1395` | 1,270,000.00 USD | 0.00 USD | 6,100.00 USD | `-17.99%` | `43,729,900,000,000.00` |
| `Live` | `Long` | `0.1405` | 1,260,000.00 USD | 0.00 USD | 16,610.00 USD | `-17.41%` | `118,217,500,000,000.00` |
| `Live` | `Long` | `0.1415` | 1,240,000.00 USD | 0.00 USD | 12,560.00 USD | `-16.82%` | `88,763,500,000,000.00` |
| `Live` | `Long` | `0.1425` | 1,230,000.00 USD | 0.00 USD | 484,630.00 USD | `-16.23%` | `3,400,889,200,000,000.00` |
| `Live` | `Long` | `0.1435` | 747,190.00 USD | 0.00 USD | 19,330.00 USD | `-15.64%` | `134,671,900,000,000.00` |
| `Live` | `Long` | `0.1445` | 727,860.00 USD | 0.00 USD | 52,350.00 USD | `-15.05%` | `362,262,000,000,000.00` |
| `Live` | `Long` | `0.1455` | 675,520.00 USD | 0.00 USD | 2,500.00 USD | `-14.47%` | `17,203,400,000,000.00` |
| `Live` | `Long` | `0.1465` | 673,010.00 USD | 0.00 USD | 34,280.00 USD | `-13.88%` | `234,026,800,000,000.00` |
| `Live` | `Long` | `0.1475` | 638,730.00 USD | 0.00 USD | 78,150.00 USD | `-13.29%` | `529,836,199,999,999.94` |
| `Live` | `Long` | `0.1485` | 560,580.00 USD | 0.00 USD | 2,650.00 USD | `-12.70%` | `17,872,100,000,000.00` |
| `Live` | `Long` | `0.1495` | 557,930.00 USD | 0.00 USD | 66,380.00 USD | `-12.12%` | `443,992,300,000,000.00` |
| `Live` | `Long` | `0.1505` | 491,550.00 USD | 0.00 USD | 102,290.00 USD | `-11.53%` | `679,673,200,000,000.00` |
| `Live` | `Long` | `0.1515` | 389,260.00 USD | 0.00 USD | 5,420.00 USD | `-10.94%` | `35,745,500,000,000.00` |
| `Live` | `Long` | `0.1525` | 383,840.00 USD | 0.00 USD | 41,470.00 USD | `-10.35%` | `271,941,200,000,000.00` |
| `Live` | `Long` | `0.1535` | 342,370.00 USD | 0.00 USD | 19,400.00 USD | `-9.76%` | `126,406,800,000,000.00` |
| `Live` | `Long` | `0.1545` | 322,970.00 USD | 0.00 USD | 26,170.00 USD | `-9.18%` | `169,378,600,000,000.00` |
| `Live` | `Long` | `0.1555` | 296,800.00 USD | 0.00 USD | 40,060.00 USD | `-8.59%` | `257,609,900,000,000.00` |
| `Live` | `Long` | `0.1565` | 256,740.00 USD | 0.00 USD | 33,750.00 USD | `-8.00%` | `215,633,400,000,000.00` |
| `Live` | `Long` | `0.1575` | 222,990.00 USD | 0.00 USD | 6,040.00 USD | `-7.41%` | `38,366,100,000,000.00` |
| `Live` | `Long` | `0.1585` | 216,950.00 USD | 0.00 USD | 2,870.00 USD | `-6.82%` | `18,120,500,000,000.00` |
| `Live` | `Long` | `0.1595` | 214,080.00 USD | 0.00 USD | 65,110.00 USD | `-6.24%` | `408,207,100,000,000.00` |
| `Live` | `Long` | `0.1605` | 148,970.00 USD | 0.00 USD | 20,630.00 USD | `-5.65%` | `128,516,700,000,000.00` |
| `Live` | `Long` | `0.1615` | 128,340.00 USD | 0.00 USD | 16,530.00 USD | `-5.06%` | `102,342,800,000,000.00` |
| `Live` | `Long` | `0.1625` | 111,810.00 USD | 0.00 USD | 108,300.00 USD | `-4.47%` | `666,476,700,000,000.00` |
| `Live` | `Short` | `0.1635` | 3,610.00 USD | 3,610.00 USD | 0.00 USD | `-3.89%` | `22,084,800,000,000.00` |
| `Live` | `Long` | `0.1645` | 3,510.00 USD | 0.00 USD | 548.33 USD | `-3.30%` | `3,333,300,000,000.00` |
| `Live` | `Long` | `0.1675` | 2,960.00 USD | 0.00 USD | 2,960.00 USD | `-1.53%` | `17,693,200,000,000.00` |
| `Live` | `Short` | `0.1735` | 4,260.00 USD | 653.37 USD | 0.00 USD | `+1.99%` | `3,765,800,000,000.00` |
| `Live` | `Short` | `0.1745` | 5,650.00 USD | 1,390.00 USD | 0.00 USD | `+2.58%` | `7,950,800,000,000.00` |
| `Live` | `Short` | `0.1765` | 6,150.00 USD | 495.68 USD | 0.00 USD | `+3.76%` | `2,808,400,000,000.00` |
| `Live` | `Short` | `0.1775` | 6,490.00 USD | 339.98 USD | 0.00 USD | `+4.34%` | `1,915,400,000,000.00` |
| `Live` | `Short` | `0.1785` | 16,980.00 USD | 10,490.00 USD | 0.00 USD | `+4.93%` | `58,789,100,000,000.00` |
| `Live` | `Short` | `0.1805` | 65,170.00 USD | 48,190.00 USD | 0.00 USD | `+6.11%` | `267,001,000,000,000.00` |
| `Live` | `Short` | `0.1875` | 86,360.00 USD | 21,190.00 USD | 0.00 USD | `+10.22%` | `112,997,300,000,000.00` |
| `Live` | `Short` | `0.1885` | 86,690.00 USD | 329.74 USD | 0.00 USD | `+10.81%` | `1,749,300,000,000.00` |
| `Live` | `Short` | `0.1905` | 113,130.00 USD | 26,440.00 USD | 0.00 USD | `+11.99%` | `138,772,200,000,000.02` |
| `Live` | `Short` | `0.1925` | 113,790.00 USD | 665.28 USD | 0.00 USD | `+13.16%` | `3,456,000,000,000.00` |
| `Live` | `Short` | `0.1945` | 114,420.00 USD | 623.68 USD | 0.00 USD | `+14.34%` | `3,206,600,000,000.00` |
| `Live` | `Short` | `0.1955` | 118,810.00 USD | 4,390.00 USD | 0.00 USD | `+14.93%` | `22,449,900,000,000.00` |
| `Live` | `Short` | `0.1975` | 118,960.00 USD | 150.10 USD | 0.00 USD | `+16.10%` | `760,000,000,000.00` |
| `Live` | `Short` | `0.1985` | 120,900.00 USD | 1,950.00 USD | 0.00 USD | `+16.69%` | `9,803,600,000,000.00` |
| `Live` | `Short` | `0.1995` | 121,040.00 USD | 135.22 USD | 0.00 USD | `+17.28%` | `677,800,000,000.00` |
| `Live` | `Short` | `0.2055` | 156,050.00 USD | 35,020.00 USD | 0.00 USD | `+20.80%` | `170,390,000,000,000.00` |
| `Live` | `Short` | `0.2085` | 156,250.00 USD | 198.08 USD | 0.00 USD | `+22.57%` | `950,000,000,000.00` |
| `Live` | `Short` | `0.2095` | 157,310.00 USD | 1,060.00 USD | 0.00 USD | `+23.16%` | `5,056,300,000,000.00` |
| `Live` | `Short` | `0.2125` | 199,980.00 USD | 42,670.00 USD | 0.00 USD | `+24.92%` | `200,790,000,000,000.00` |
| `Live` | `Short` | `0.2135` | 216,050.00 USD | 16,070.00 USD | 0.00 USD | `+25.51%` | `75,287,100,000,000.00` |
| `Live` | `Short` | `0.2155` | 257,280.00 USD | 41,230.00 USD | 0.00 USD | `+26.68%` | `191,330,600,000,000.00` |
| `Live` | `Short` | `0.2205` | 283,520.00 USD | 26,240.00 USD | 0.00 USD | `+29.62%` | `118,989,500,000,000.00` |
| `Live` | `Short` | `0.2225` | 284,180.00 USD | 656.06 USD | 0.00 USD | `+30.80%` | `2,948,600,000,000.00` |
| `Live` | `Short` | `0.2235` | 284,520.00 USD | 343.77 USD | 0.00 USD | `+31.39%` | `1,538,100,000,000.00` |
| `Live` | `Short` | `0.2255` | 284,670.00 USD | 154.78 USD | 0.00 USD | `+32.56%` | `686,400,000,000.00` |
| `Live` | `Short` | `0.2295` | 291,500.00 USD | 6,820.00 USD | 0.00 USD | `+34.91%` | `29,727,000,000,000.00` |
| `Live` | `Short` | `0.2335` | 291,800.00 USD | 304.11 USD | 0.00 USD | `+37.26%` | `1,302,400,000,000.00` |
| `Live` | `Short` | `0.2355` | 308,050.00 USD | 16,250.00 USD | 0.00 USD | `+38.44%` | `69,017,500,000,000.00` |
| `Live` | `Short` | `0.2375` | 308,160.00 USD | 102.62 USD | 0.00 USD | `+39.62%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2405` | 308,520.00 USD | 361.66 USD | 0.00 USD | `+41.38%` | `1,503,800,000,000.00` |
| `Live` | `Short` | `0.2425` | 309,390.00 USD | 869.00 USD | 0.00 USD | `+42.55%` | `3,583,500,000,000.00` |
| `Live` | `Short` | `0.2445` | 309,620.00 USD | 231.03 USD | 0.00 USD | `+43.73%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2465` | 318,980.00 USD | 9,360.00 USD | 0.00 USD | `+44.91%` | `37,972,200,000,000.00` |
| `Live` | `Short` | `0.2495` | 338,890.00 USD | 19,910.00 USD | 0.00 USD | `+46.67%` | `79,816,900,000,000.00` |
| `Live` | `Short` | `0.2545` | 339,440.00 USD | 546.54 USD | 0.00 USD | `+49.61%` | `2,147,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 343,310.00 USD | 3,870.00 USD | 0.00 USD | `+50.78%` | `15,070,700,000,000.00` |
| `Live` | `Short` | `0.2575` | 372,810.00 USD | 29,500.00 USD | 0.00 USD | `+51.37%` | `114,561,100,000,000.00` |
| `Live` | `Short` | `0.2585` | 424,830.00 USD | 52,030.00 USD | 0.00 USD | `+51.96%` | `201,260,100,000,000.00` |
| `Live` | `Short` | `0.2615` | 424,990.00 USD | 154.94 USD | 0.00 USD | `+53.72%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2685` | 425,210.00 USD | 226.51 USD | 0.00 USD | `+57.84%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2715` | 438,730.00 USD | 13,510.00 USD | 0.00 USD | `+59.60%` | `49,773,600,000,000.00` |
| `Live` | `Short` | `0.2725` | 438,940.00 USD | 214.21 USD | 0.00 USD | `+60.19%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 466,830.00 USD | 27,890.00 USD | 0.00 USD | `+61.37%` | `101,607,700,000,000.00` |
| `Live` | `Short` | `0.2795` | 467,310.00 USD | 482.84 USD | 0.00 USD | `+64.31%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2825` | 467,760.00 USD | 449.32 USD | 0.00 USD | `+66.07%` | `1,590,500,000,000.00` |
| `Live` | `Short` | `0.2915` | 467,950.00 USD | 187.26 USD | 0.00 USD | `+71.36%` | `642,400,000,000.00` |
| `Live` | `Short` | `0.2935` | 470,180.00 USD | 2,230.00 USD | 0.00 USD | `+72.54%` | `7,608,100,000,000.00` |
| `Live` | `Short` | `0.2955` | 470,760.00 USD | 574.36 USD | 0.00 USD | `+73.71%` | `1,943,700,000,000.00` |
| `Live` | `Short` | `0.3025` | 479,730.00 USD | 8,970.00 USD | 0.00 USD | `+77.83%` | `29,666,400,000,000.00` |
| `Live` | `Short` | `0.3105` | 479,960.00 USD | 225.42 USD | 0.00 USD | `+82.53%` | `726,000,000,000.00` |
| `Live` | `Short` | `0.3175` | 480,330.00 USD | 376.84 USD | 0.00 USD | `+86.64%` | `1,186,900,000,000.00` |
| `Live` | `Short` | `0.3215` | 544,630.00 USD | 64,300.00 USD | 0.00 USD | `+89.00%` | `200,000,000,000,000.00` |
| `Live` | `Short` | `0.3255` | 544,890.00 USD | 252.52 USD | 0.00 USD | `+91.35%` | `775,800,000,000.00` |
| `Live` | `Short` | `0.3295` | 556,480.00 USD | 11,590.00 USD | 0.00 USD | `+93.70%` | `35,183,300,000,000.00` |
| `Live` | `Short` | `0.3305` | 556,670.00 USD | 192.68 USD | 0.00 USD | `+94.29%` | `583,000,000,000.00` |
| `Live` | `Short` | `0.3325` | 572,480.00 USD | 15,810.00 USD | 0.00 USD | `+95.46%` | `47,546,600,000,000.00` |
| `Live` | `Short` | `0.3335` | 572,700.00 USD | 221.81 USD | 0.00 USD | `+96.05%` | `665,100,000,000.00` |
| `Live` | `Short` | `0.3385` | 572,810.00 USD | 108.46 USD | 0.00 USD | `+98.99%` | `320,400,000,000.00` |
| `Live` | `Short` | `0.3395` | 636,600.00 USD | 63,790.00 USD | 0.00 USD | `+99.58%` | `187,887,700,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0355` | 744,980.00 USD | 0.00 USD | 355.00 USD | `-79.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 744,620.00 USD | 0.00 USD | 453.00 USD | `-75.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 744,170.00 USD | 0.00 USD | 353.50 USD | `-70.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 743,820.00 USD | 0.00 USD | 4,310.00 USD | `-67.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 739,500.00 USD | 0.00 USD | 475.11 USD | `-62.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 739,030.00 USD | 0.00 USD | 131.16 USD | `-61.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 738,900.00 USD | 0.00 USD | 881.45 USD | `-60.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 738,010.00 USD | 0.00 USD | 1,070.00 USD | `-60.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 736,940.00 USD | 0.00 USD | 1,400.00 USD | `-59.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 735,540.00 USD | 0.00 USD | 1,010.00 USD | `-59.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 734,530.00 USD | 0.00 USD | 4,490.00 USD | `-58.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 730,040.00 USD | 0.00 USD | 529.04 USD | `-57.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 729,510.00 USD | 0.00 USD | 2,390.00 USD | `-57.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 727,120.00 USD | 0.00 USD | 757.39 USD | `-55.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 726,370.00 USD | 0.00 USD | 1,490.00 USD | `-53.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 724,880.00 USD | 0.00 USD | 277.37 USD | `-49.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 724,600.00 USD | 0.00 USD | 262.50 USD | `-48.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 724,340.00 USD | 0.00 USD | 795.57 USD | `-47.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 723,550.00 USD | 0.00 USD | 181.00 USD | `-46.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 723,360.00 USD | 0.00 USD | 1,020.00 USD | `-40.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 722,340.00 USD | 0.00 USD | 1,550.00 USD | `-39.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 720,800.00 USD | 0.00 USD | 3,260.00 USD | `-36.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 717,530.00 USD | 0.00 USD | 19,070.00 USD | `-36.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 698,460.00 USD | 0.00 USD | 577.22 USD | `-35.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 697,890.00 USD | 0.00 USD | 343.50 USD | `-32.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 697,540.00 USD | 0.00 USD | 26,280.00 USD | `-31.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1175` | 671,260.00 USD | 0.00 USD | 105.75 USD | `-30.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 671,160.00 USD | 0.00 USD | 120.50 USD | `-29.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 671,040.00 USD | 0.00 USD | 83,620.00 USD | `-28.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 587,410.00 USD | 0.00 USD | 14,940.00 USD | `-26.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 572,470.00 USD | 0.00 USD | 3,010.00 USD | `-25.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 569,470.00 USD | 0.00 USD | 473.27 USD | `-25.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 568,990.00 USD | 0.00 USD | 220,940.00 USD | `-24.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 348,060.00 USD | 0.00 USD | 26,290.00 USD | `-23.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 321,770.00 USD | 0.00 USD | 5,560.00 USD | `-22.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 316,200.00 USD | 0.00 USD | 625.78 USD | `-21.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 315,580.00 USD | 0.00 USD | 8,480.00 USD | `-20.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 307,100.00 USD | 0.00 USD | 16,260.00 USD | `-20.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 290,830.00 USD | 0.00 USD | 700.86 USD | `-19.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 290,130.00 USD | 0.00 USD | 108.57 USD | `-18.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 290,020.00 USD | 0.00 USD | 349.74 USD | `-17.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 289,670.00 USD | 0.00 USD | 6,330.00 USD | `-17.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 283,340.00 USD | 0.00 USD | 127.35 USD | `-16.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 283,210.00 USD | 0.00 USD | 24,850.00 USD | `-16.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 258,370.00 USD | 0.00 USD | 702.55 USD | `-15.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 257,670.00 USD | 0.00 USD | 1,960.00 USD | `-15.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 255,710.00 USD | 0.00 USD | 27,350.00 USD | `-14.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 228,360.00 USD | 0.00 USD | 8,910.00 USD | `-13.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 219,450.00 USD | 0.00 USD | 4,590.00 USD | `-13.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 214,860.00 USD | 0.00 USD | 3,950.00 USD | `-12.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 210,910.00 USD | 0.00 USD | 2,420.00 USD | `-12.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 208,490.00 USD | 0.00 USD | 7,860.00 USD | `-11.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 200,630.00 USD | 0.00 USD | 702.05 USD | `-10.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 199,920.00 USD | 0.00 USD | 1,000.00 USD | `-10.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1535` | 198,920.00 USD | 0.00 USD | 9,210.00 USD | `-9.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 189,710.00 USD | 0.00 USD | 19,690.00 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 170,020.00 USD | 0.00 USD | 2,020.00 USD | `-8.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 168,000.00 USD | 0.00 USD | 718.79 USD | `-8.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1575` | 167,290.00 USD | 0.00 USD | 443.71 USD | `-7.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 166,840.00 USD | 0.00 USD | 17,200.00 USD | `-6.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 149,640.00 USD | 0.00 USD | 70,970.00 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 78,670.00 USD | 0.00 USD | 32,950.00 USD | `-5.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 45,720.00 USD | 0.00 USD | 8,120.00 USD | `-5.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 37,600.00 USD | 0.00 USD | 877.65 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 36,730.00 USD | 0.00 USD | 18,190.00 USD | `-3.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 18,540.00 USD | 0.00 USD | 124.77 USD | `-3.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 18,410.00 USD | 0.00 USD | 12,990.00 USD | `-2.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 5,430.00 USD | 0.00 USD | 1,410.00 USD | `-2.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 4,010.00 USD | 0.00 USD | 671.24 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1685` | 3,340.00 USD | 0.00 USD | 2,060.00 USD | `-0.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 1,280.00 USD | 0.00 USD | 1,280.00 USD | `-0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 12,710.00 USD | 12,710.00 USD | 0.00 USD | `+0.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 14,850.00 USD | 2,140.00 USD | 0.00 USD | `+0.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 25,200.00 USD | 10,350.00 USD | 0.00 USD | `+1.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 46,030.00 USD | 20,830.00 USD | 0.00 USD | `+1.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 61,170.00 USD | 15,140.00 USD | 0.00 USD | `+2.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 81,840.00 USD | 20,680.00 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 82,700.00 USD | 857.10 USD | 0.00 USD | `+3.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 82,910.00 USD | 213.30 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 83,960.00 USD | 1,040.00 USD | 0.00 USD | `+4.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 92,790.00 USD | 8,830.00 USD | 0.00 USD | `+5.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 94,210.00 USD | 1,420.00 USD | 0.00 USD | `+6.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 107,300.00 USD | 13,080.00 USD | 0.00 USD | `+6.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 116,180.00 USD | 8,880.00 USD | 0.00 USD | `+7.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 123,690.00 USD | 7,510.00 USD | 0.00 USD | `+7.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 123,970.00 USD | 276.75 USD | 0.00 USD | `+8.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 124,120.00 USD | 149.79 USD | 0.00 USD | `+9.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 129,050.00 USD | 4,930.00 USD | 0.00 USD | `+9.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 129,190.00 USD | 147.11 USD | 0.00 USD | `+10.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 129,610.00 USD | 416.42 USD | 0.00 USD | `+10.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 130,270.00 USD | 660.73 USD | 0.00 USD | `+11.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 137,400.00 USD | 7,130.00 USD | 0.00 USD | `+11.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 137,800.00 USD | 396.42 USD | 0.00 USD | `+12.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 138,840.00 USD | 1,040.00 USD | 0.00 USD | `+13.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 145,910.00 USD | 7,070.00 USD | 0.00 USD | `+13.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 146,650.00 USD | 742.45 USD | 0.00 USD | `+14.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 151,170.00 USD | 4,520.00 USD | 0.00 USD | `+14.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 151,300.00 USD | 133.19 USD | 0.00 USD | `+15.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 151,440.00 USD | 134.20 USD | 0.00 USD | `+16.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 156,010.00 USD | 4,570.00 USD | 0.00 USD | `+16.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 156,500.00 USD | 492.19 USD | 0.00 USD | `+17.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 189,610.00 USD | 33,110.00 USD | 0.00 USD | `+17.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 190,470.00 USD | 863.97 USD | 0.00 USD | `+18.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 215,110.00 USD | 24,640.00 USD | 0.00 USD | `+19.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 215,290.00 USD | 182.72 USD | 0.00 USD | `+19.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 301,180.00 USD | 85,900.00 USD | 0.00 USD | `+20.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 301,940.00 USD | 751.90 USD | 0.00 USD | `+20.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 302,110.00 USD | 174.20 USD | 0.00 USD | `+21.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 304,190.00 USD | 2,080.00 USD | 0.00 USD | `+21.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 304,440.00 USD | 252.51 USD | 0.00 USD | `+23.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 340,340.00 USD | 35,900.00 USD | 0.00 USD | `+23.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 340,470.00 USD | 126.50 USD | 0.00 USD | `+24.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 340,660.00 USD | 190.80 USD | 0.00 USD | `+24.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 341,370.00 USD | 713.94 USD | 0.00 USD | `+25.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 341,580.00 USD | 213.00 USD | 0.00 USD | `+26.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 344,040.00 USD | 2,460.00 USD | 0.00 USD | `+27.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 350,320.00 USD | 6,280.00 USD | 0.00 USD | `+28.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 486,910.00 USD | 136,590.00 USD | 0.00 USD | `+29.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 487,250.00 USD | 333.91 USD | 0.00 USD | `+30.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 491,220.00 USD | 3,980.00 USD | 0.00 USD | `+31.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 491,410.00 USD | 184.23 USD | 0.00 USD | `+32.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 491,590.00 USD | 185.05 USD | 0.00 USD | `+33.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 491,780.00 USD | 185.87 USD | 0.00 USD | `+33.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 492,010.00 USD | 231.24 USD | 0.00 USD | `+34.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2295` | 492,200.00 USD | 187.50 USD | 0.00 USD | `+34.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 536,850.00 USD | 44,650.00 USD | 0.00 USD | `+35.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 537,040.00 USD | 189.14 USD | 0.00 USD | `+36.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 541,300.00 USD | 4,260.00 USD | 0.00 USD | `+36.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 542,810.00 USD | 1,520.00 USD | 0.00 USD | `+37.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 543,000.00 USD | 191.59 USD | 0.00 USD | `+37.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 564,330.00 USD | 21,320.00 USD | 0.00 USD | `+39.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 566,860.00 USD | 2,530.00 USD | 0.00 USD | `+40.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 567,050.00 USD | 195.67 USD | 0.00 USD | `+40.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 589,290.00 USD | 22,240.00 USD | 0.00 USD | `+41.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 598,600.00 USD | 9,300.00 USD | 0.00 USD | `+41.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 600,190.00 USD | 1,600.00 USD | 0.00 USD | `+44.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 618,950.00 USD | 18,750.00 USD | 0.00 USD | `+44.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 619,500.00 USD | 551.23 USD | 0.00 USD | `+45.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 620,530.00 USD | 1,030.00 USD | 0.00 USD | `+46.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 628,300.00 USD | 7,770.00 USD | 0.00 USD | `+47.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 633,300.00 USD | 5,010.00 USD | 0.00 USD | `+48.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 649,190.00 USD | 15,880.00 USD | 0.00 USD | `+49.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 650,970.00 USD | 1,780.00 USD | 0.00 USD | `+49.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 655,230.00 USD | 4,260.00 USD | 0.00 USD | `+50.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 666,960.00 USD | 11,730.00 USD | 0.00 USD | `+50.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 672,120.00 USD | 5,160.00 USD | 0.00 USD | `+51.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 688,990.00 USD | 16,870.00 USD | 0.00 USD | `+52.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 718,120.00 USD | 29,130.00 USD | 0.00 USD | `+53.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2655` | 797,900.00 USD | 79,780.00 USD | 0.00 USD | `+56.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 798,170.00 USD | 272.88 USD | 0.00 USD | `+59.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 798,570.00 USD | 394.01 USD | 0.00 USD | `+62.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 818,170.00 USD | 19,600.00 USD | 0.00 USD | `+64.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 820,300.00 USD | 2,130.00 USD | 0.00 USD | `+67.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 820,880.00 USD | 579.27 USD | 0.00 USD | `+68.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 823,890.00 USD | 3,010.00 USD | 0.00 USD | `+70.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 823,990.00 USD | 101.21 USD | 0.00 USD | `+73.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 824,250.00 USD | 262.73 USD | 0.00 USD | `+74.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 825,690.00 USD | 1,440.00 USD | 0.00 USD | `+74.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 831,350.00 USD | 5,660.00 USD | 0.00 USD | `+76.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 836,780.00 USD | 5,430.00 USD | 0.00 USD | `+77.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 837,070.00 USD | 289.61 USD | 0.00 USD | `+79.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3095` | 875,760.00 USD | 38,690.00 USD | 0.00 USD | `+81.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 876,110.00 USD | 357.85 USD | 0.00 USD | `+96.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3355` | 876,360.00 USD | 251.29 USD | 0.00 USD | `+97.23%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1453` | 10,390,000.00 USD | 0.00 USD | 10,390,000.00 USD | 0.00 USD | 5,660.00 USD | 14,180.00 USD |
| `7D` | `0.1456` | 10,370,000.00 USD | 0.00 USD | 10,370,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD |
| `7D` | `0.1459` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD |
| `7D` | `0.1465` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD |
| `7D` | `0.1468` | 10,350,000.00 USD | 0.00 USD | 10,350,000.00 USD | 9,720.00 USD | 9,180.00 USD | 8,720.00 USD |
| `7D` | `0.1471` | 10,330,000.00 USD | 0.00 USD | 10,330,000.00 USD | 6,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1474` | 10,320,000.00 USD | 0.00 USD | 10,320,000.00 USD | 6,490.00 USD | 9,220.00 USD | 5,280.00 USD |
| `7D` | `0.1477` | 10,300,000.00 USD | 0.00 USD | 10,300,000.00 USD | 0.00 USD | 25,460.00 USD | 5,320.00 USD |
| `7D` | `0.1480` | 10,270,000.00 USD | 0.00 USD | 10,270,000.00 USD | 6,990.00 USD | 29,300.00 USD | 20,830.00 USD |
| `7D` | `0.1483` | 10,210,000.00 USD | 0.00 USD | 10,210,000.00 USD | 42,230.00 USD | 16,640.00 USD | 33,050.00 USD |
| `7D` | `0.1486` | 10,120,000.00 USD | 0.00 USD | 10,120,000.00 USD | 18,610.00 USD | 10,470.00 USD | 25,980.00 USD |
| `7D` | `0.1489` | 10,060,000.00 USD | 0.00 USD | 10,060,000.00 USD | 11,170.00 USD | 3,710.00 USD | 10,390.00 USD |
| `7D` | `0.1492` | 10,040,000.00 USD | 0.00 USD | 10,040,000.00 USD | 40,320.00 USD | 17,880.00 USD | 27,100.00 USD |
| `7D` | `0.1495` | 9,950,000.00 USD | 0.00 USD | 9,950,000.00 USD | 34,650.00 USD | 18,690.00 USD | 12,930.00 USD |
| `7D` | `0.1498` | 9,890,000.00 USD | 0.00 USD | 9,890,000.00 USD | 42,100.00 USD | 9,610.00 USD | 10,480.00 USD |
| `7D` | `0.1501` | 9,820,000.00 USD | 0.00 USD | 9,820,000.00 USD | 21,010.00 USD | 7,930.00 USD | 15,630.00 USD |
| `7D` | `0.1504` | 9,780,000.00 USD | 0.00 USD | 9,780,000.00 USD | 17,800.00 USD | 11,590.00 USD | 44,850.00 USD |
| `7D` | `0.1507` | 9,710,000.00 USD | 0.00 USD | 9,710,000.00 USD | 28,940.00 USD | 12,910.00 USD | 30,500.00 USD |
| `1D` | `0.1510` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 5,640.00 USD | 3,930.00 USD | 3,700.00 USD |
| `7D` | `0.1510` | 9,630,000.00 USD | 0.00 USD | 9,630,000.00 USD | 12,660.00 USD | 12,930.00 USD | 29,700.00 USD |
| `1D` | `0.1512` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 0.00 USD | 5,780.00 USD | 1,300.00 USD |
| `7D` | `0.1513` | 9,580,000.00 USD | 0.00 USD | 9,580,000.00 USD | 32,900.00 USD | 17,610.00 USD | 38,800.00 USD |
| `1D` | `0.1514` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 0.00 USD | 1,730.00 USD | 1,300.00 USD |
| `1D` | `0.1516` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 0.00 USD | 1,690.00 USD | 0.00 USD |
| `7D` | `0.1516` | 9,490,000.00 USD | 0.00 USD | 9,490,000.00 USD | 54,550.00 USD | 0.00 USD | 43,840.00 USD |
| `1D` | `0.1518` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 4,860.00 USD | 0.00 USD | 7,420.00 USD |
| `7D` | `0.1519` | 9,390,000.00 USD | 0.00 USD | 9,390,000.00 USD | 37,430.00 USD | 19,520.00 USD | 70,660.00 USD |
| `1D` | `0.1520` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 3,590.00 USD | 1,470.00 USD | 3,670.00 USD |
| `1D` | `0.1522` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 5,860.00 USD | 2,970.00 USD | 2,100.00 USD |
| `7D` | `0.1522` | 9,260,000.00 USD | 0.00 USD | 9,260,000.00 USD | 49,800.00 USD | 9,640.00 USD | 24,710.00 USD |
| `1D` | `0.1524` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 1,870.00 USD | 0.00 USD | 5,050.00 USD |
| `7D` | `0.1525` | 9,180,000.00 USD | 0.00 USD | 9,180,000.00 USD | 25,790.00 USD | 13,700.00 USD | 19,910.00 USD |
| `1D` | `0.1526` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 3,300.00 USD | 0.00 USD | 7,060.00 USD |
| `1D` | `0.1528` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 3,160.00 USD |
| `7D` | `0.1528` | 9,120,000.00 USD | 0.00 USD | 9,120,000.00 USD | 75,690.00 USD | 27,110.00 USD | 27,860.00 USD |
| `1D` | `0.1530` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 4,960.00 USD | 5,040.00 USD | 3,970.00 USD |
| `7D` | `0.1531` | 8,990,000.00 USD | 0.00 USD | 8,990,000.00 USD | 35,030.00 USD | 8,400.00 USD | 16,920.00 USD |
| `1D` | `0.1532` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 9,350.00 USD | 0.00 USD | 3,140.00 USD |
| `1D` | `0.1534` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 1,960.00 USD | 2,820.00 USD | 2,290.00 USD |
| `7D` | `0.1534` | 8,930,000.00 USD | 0.00 USD | 8,930,000.00 USD | 15,780.00 USD | 17,430.00 USD | 20,220.00 USD |
| `1D` | `0.1536` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 4,320.00 USD | 2,760.00 USD | 4,090.00 USD |
| `7D` | `0.1537` | 8,880,000.00 USD | 0.00 USD | 8,880,000.00 USD | 28,060.00 USD | 5,880.00 USD | 10,520.00 USD |
| `1D` | `0.1538` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 2,880.00 USD | 3,160.00 USD | 3,960.00 USD |
| `1D` | `0.1540` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 4,630.00 USD | 4,960.00 USD | 0.00 USD |
| `7D` | `0.1540` | 8,830,000.00 USD | 0.00 USD | 8,830,000.00 USD | 14,000.00 USD | 6,530.00 USD | 5,070.00 USD |
| `1D` | `0.1542` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 4,050.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1543` | 8,810,000.00 USD | 0.00 USD | 8,810,000.00 USD | 9,250.00 USD | 3,590.00 USD | 4,670.00 USD |
| `1D` | `0.1544` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 4,000.00 USD | 3,150.00 USD | 1,730.00 USD |
| `1D` | `0.1546` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 0.00 USD | 4,570.00 USD | 7,640.00 USD |
| `7D` | `0.1546` | 8,790,000.00 USD | 0.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 5,620.00 USD |
| `1D` | `0.1548` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 1,140.00 USD | 1,840.00 USD | 1,070.00 USD |
| `7D` | `0.1549` | 8,780,000.00 USD | 0.00 USD | 8,780,000.00 USD | 11,570.00 USD | 6,940.00 USD | 0.00 USD |
| `1D` | `0.1550` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 4,810.00 USD | 2,620.00 USD | 959.69 USD |
| `1D` | `0.1552` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 4,500.00 USD | 1,530.00 USD | 2,930.00 USD |
| `7D` | `0.1552` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 23,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1554` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 6,780.00 USD | 6,040.00 USD | 0.00 USD |
| `1D` | `0.1558` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 1,090.00 USD |
| `7D` | `0.1558` | 8,740,000.00 USD | 0.00 USD | 8,740,000.00 USD | 0.00 USD | 4,510.00 USD | 5,200.00 USD |
| `1D` | `0.1560` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 5,460.00 USD | 1,210.00 USD | 2,210.00 USD |
| `1D` | `0.1562` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 3,050.00 USD | 1,050.00 USD | 10,350.00 USD |
| `1D` | `0.1564` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 6,880.00 USD | 2,310.00 USD | 11,410.00 USD |
| `7D` | `0.1564` | 8,730,000.00 USD | 0.00 USD | 8,730,000.00 USD | 24,300.00 USD | 19,310.00 USD | 21,180.00 USD |
| `1D` | `0.1566` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 35,850.00 USD | 6,370.00 USD | 11,550.00 USD |
| `7D` | `0.1567` | 8,670,000.00 USD | 0.00 USD | 8,670,000.00 USD | 41,770.00 USD | 15,360.00 USD | 15,440.00 USD |
| `1D` | `0.1568` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 13,610.00 USD | 14,320.00 USD | 4,740.00 USD |
| `1D` | `0.1570` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 19,150.00 USD | 16,600.00 USD | 12,140.00 USD |
| `7D` | `0.1570` | 8,590,000.00 USD | 0.00 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 11,900.00 USD |
| `1D` | `0.1572` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 30,100.00 USD | 12,820.00 USD | 22,850.00 USD |
| `7D` | `0.1573` | 8,580,000.00 USD | 0.00 USD | 8,580,000.00 USD | 58,830.00 USD | 47,690.00 USD | 25,810.00 USD |
| `1D` | `0.1574` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 21,250.00 USD | 6,090.00 USD | 1,670.00 USD |
| `1D` | `0.1576` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 13,180.00 USD | 21,900.00 USD | 11,770.00 USD |
| `7D` | `0.1576` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 26,600.00 USD | 102,190.00 USD | 54,870.00 USD |
| `1D` | `0.1578` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 62,820.00 USD | 51,020.00 USD | 17,730.00 USD |
| `7D` | `0.1579` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 101,500.00 USD | 95,190.00 USD | 42,790.00 USD |
| `1D` | `0.1580` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 25,030.00 USD | 0.00 USD | 25,750.00 USD |
| `1D` | `0.1582` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 19,780.00 USD | 23,000.00 USD | 22,540.00 USD |
| `7D` | `0.1582` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 56,130.00 USD | 13,480.00 USD | 89,190.00 USD |
| `1D` | `0.1584` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 24,310.00 USD | 2,750.00 USD | 8,730.00 USD |
| `7D` | `0.1585` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 87,110.00 USD | 50,340.00 USD | 75,690.00 USD |
| `1D` | `0.1586` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 8,200.00 USD | 20,700.00 USD | 24,820.00 USD |
| `1D` | `0.1588` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 14,390.00 USD | 17,570.00 USD | 5,640.00 USD |
| `7D` | `0.1588` | 7,650,000.00 USD | 0.00 USD | 7,650,000.00 USD | 34,830.00 USD | 30,030.00 USD | 41,060.00 USD |
| `1D` | `0.1590` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 7,770.00 USD | 21,670.00 USD | 5,770.00 USD |
| `7D` | `0.1591` | 7,550,000.00 USD | 0.00 USD | 7,550,000.00 USD | 110,640.00 USD | 49,670.00 USD | 60,600.00 USD |
| `1D` | `0.1592` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 29,280.00 USD | 9,550.00 USD | 29,010.00 USD |
| `1D` | `0.1594` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 53,920.00 USD | 13,170.00 USD | 23,770.00 USD |
| `7D` | `0.1594` | 7,330,000.00 USD | 0.00 USD | 7,330,000.00 USD | 85,560.00 USD | 39,260.00 USD | 102,800.00 USD |
| `1D` | `0.1596` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 14,990.00 USD | 8,110.00 USD | 45,630.00 USD |
| `7D` | `0.1597` | 7,100,000.00 USD | 0.00 USD | 7,100,000.00 USD | 228,850.00 USD | 96,110.00 USD | 102,580.00 USD |
| `1D` | `0.1598` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 61,390.00 USD | 27,500.00 USD | 33,770.00 USD |
| `1D` | `0.1600` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 20,010.00 USD | 25,530.00 USD | 19,990.00 USD |
| `7D` | `0.1600` | 6,670,000.00 USD | 0.00 USD | 6,670,000.00 USD | 105,580.00 USD | 38,830.00 USD | 76,540.00 USD |
| `1D` | `0.1602` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 47,310.00 USD | 37,150.00 USD | 27,880.00 USD |
| `7D` | `0.1603` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 62,240.00 USD | 54,840.00 USD | 81,850.00 USD |
| `1D` | `0.1604` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 26,220.00 USD | 13,920.00 USD | 17,830.00 USD |
| `1D` | `0.1606` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 43,010.00 USD | 23,580.00 USD | 44,940.00 USD |
| `7D` | `0.1606` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 211,140.00 USD | 149,480.00 USD | 227,860.00 USD |
| `1D` | `0.1608` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 42,100.00 USD | 37,120.00 USD | 18,140.00 USD |
| `7D` | `0.1609` | 5,660,000.00 USD | 0.00 USD | 5,660,000.00 USD | 92,990.00 USD | 229,060.00 USD | 182,360.00 USD |
| `1D` | `0.1610` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 91,680.00 USD | 90,460.00 USD | 32,860.00 USD |
| `1D` | `0.1612` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 79,330.00 USD | 54,580.00 USD | 50,940.00 USD |
| `7D` | `0.1612` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 291,500.00 USD | 250,360.00 USD | 159,570.00 USD |
| `1D` | `0.1614` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 20,150.00 USD | 22,780.00 USD | 40,340.00 USD |
| `7D` | `0.1615` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 300,450.00 USD | 107,900.00 USD | 374,650.00 USD |
| `1D` | `0.1616` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 46,750.00 USD | 32,270.00 USD | 49,450.00 USD |
| `1D` | `0.1618` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 35,250.00 USD | 22,220.00 USD | 43,070.00 USD |
| `7D` | `0.1618` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 310,070.00 USD | 132,060.00 USD | 318,720.00 USD |
| `1D` | `0.1620` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 31,540.00 USD | 45,810.00 USD | 47,550.00 USD |
| `7D` | `0.1621` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 228,220.00 USD | 154,980.00 USD | 316,140.00 USD |
| `1D` | `0.1622` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 63,130.00 USD | 34,460.00 USD | 16,500.00 USD |
| `1D` | `0.1624` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 9,570.00 USD | 55,410.00 USD | 9,100.00 USD |
| `7D` | `0.1624` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 381,800.00 USD | 138,890.00 USD | 119,380.00 USD |
| `1D` | `0.1626` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 9,420.00 USD | 3,170.00 USD | 14,960.00 USD |
| `7D` | `0.1627` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 291,760.00 USD | 0.00 USD | 12,330.00 USD |
| `1D` | `0.1628` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 14,220.00 USD | 29,880.00 USD | 12,840.00 USD |
| `1D` | `0.1630` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 0.00 USD | 3,150.00 USD | 6,780.00 USD |
| `7D` | `0.1630` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 9,210.00 USD | 0.00 USD | 8,530.00 USD |
| `1D` | `0.1632` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 12,400.00 USD | 25,710.00 USD | 5,440.00 USD |
| `1D` | `0.1634` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 21,220.00 USD | 1,640.00 USD | 7,850.00 USD |
| `1D` | `0.1636` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 4,900.00 USD | 7,060.00 USD | 16,790.00 USD |
| `7D` | `0.1636` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 0.00 USD | 13,670.00 USD | 21,360.00 USD |
| `1D` | `0.1638` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 9,410.00 USD | 13,220.00 USD | 34,190.00 USD |
| `7D` | `0.1639` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 62,410.00 USD |
| `1D` | `0.1640` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 7,360.00 USD | 6,090.00 USD | 5,360.00 USD |
| `1D` | `0.1642` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 20,760.00 USD | 17,890.00 USD | 3,370.00 USD |
| `7D` | `0.1642` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 0.00 USD | 14,690.00 USD | 26,230.00 USD |
| `1D` | `0.1644` | 975,290.00 USD | 0.00 USD | 975,290.00 USD | 4,830.00 USD | 2,450.00 USD | 12,490.00 USD |
| `7D` | `0.1645` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 23,120.00 USD | 8,990.00 USD | 7,650.00 USD |
| `1D` | `0.1646` | 955,520.00 USD | 0.00 USD | 955,520.00 USD | 10,010.00 USD | 15,920.00 USD | 10,850.00 USD |
| `1D` | `0.1648` | 918,740.00 USD | 0.00 USD | 918,740.00 USD | 0.00 USD | 11,690.00 USD | 13,170.00 USD |
| `1D` | `0.1650` | 893,870.00 USD | 0.00 USD | 893,870.00 USD | 7,830.00 USD | 14,550.00 USD | 0.00 USD |
| `7D` | `0.1651` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 51,100.00 USD |
| `1D` | `0.1652` | 871,490.00 USD | 0.00 USD | 871,490.00 USD | 11,940.00 USD | 0.00 USD | 30,320.00 USD |
| `1D` | `0.1654` | 829,220.00 USD | 0.00 USD | 829,220.00 USD | 3,610.00 USD | 7,080.00 USD | 18,360.00 USD |
| `7D` | `0.1654` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 33,810.00 USD | 12,460.00 USD | 0.00 USD |
| `1D` | `0.1656` | 800,170.00 USD | 0.00 USD | 800,170.00 USD | 29,290.00 USD | 7,370.00 USD | 3,750.00 USD |
| `1D` | `0.1658` | 759,770.00 USD | 0.00 USD | 759,770.00 USD | 6,580.00 USD | 14,850.00 USD | 16,110.00 USD |
| `1D` | `0.1660` | 722,220.00 USD | 0.00 USD | 722,220.00 USD | 18,840.00 USD | 0.00 USD | 25,870.00 USD |
| `7D` | `0.1660` | 977,060.00 USD | 0.00 USD | 977,060.00 USD | 29,890.00 USD | 11,020.00 USD | 19,680.00 USD |
| `1D` | `0.1662` | 677,510.00 USD | 0.00 USD | 677,510.00 USD | 16,520.00 USD | 11,720.00 USD | 25,680.00 USD |
| `7D` | `0.1663` | 916,470.00 USD | 0.00 USD | 916,470.00 USD | 86,050.00 USD | 27,600.00 USD | 75,880.00 USD |
| `1D` | `0.1664` | 623,590.00 USD | 0.00 USD | 623,590.00 USD | 27,910.00 USD | 19,050.00 USD | 30,040.00 USD |
| `1D` | `0.1666` | 546,610.00 USD | 0.00 USD | 546,610.00 USD | 41,260.00 USD | 47,610.00 USD | 20,360.00 USD |
| `7D` | `0.1666` | 726,930.00 USD | 0.00 USD | 726,930.00 USD | 49,590.00 USD | 20,110.00 USD | 19,400.00 USD |
| `1D` | `0.1668` | 437,380.00 USD | 0.00 USD | 437,380.00 USD | 80,730.00 USD | 12,260.00 USD | 15,710.00 USD |
| `7D` | `0.1669` | 637,830.00 USD | 0.00 USD | 637,830.00 USD | 0.00 USD | 40,600.00 USD | 42,720.00 USD |
| `1D` | `0.1670` | 328,680.00 USD | 0.00 USD | 328,680.00 USD | 18,320.00 USD | 14,120.00 USD | 22,000.00 USD |
| `1D` | `0.1672` | 274,240.00 USD | 0.00 USD | 274,240.00 USD | 30,150.00 USD | 0.00 USD | 10,610.00 USD |
| `7D` | `0.1672` | 554,510.00 USD | 0.00 USD | 554,510.00 USD | 70,540.00 USD | 38,070.00 USD | 0.00 USD |
| `1D` | `0.1674` | 233,490.00 USD | 0.00 USD | 233,490.00 USD | 0.00 USD | 15,830.00 USD | 9,880.00 USD |
| `7D` | `0.1675` | 445,900.00 USD | 0.00 USD | 445,900.00 USD | 19,540.00 USD | 64,060.00 USD | 0.00 USD |
| `1D` | `0.1676` | 207,780.00 USD | 0.00 USD | 207,780.00 USD | 14,620.00 USD | 17,410.00 USD | 0.00 USD |
| `7D` | `0.1678` | 362,300.00 USD | 0.00 USD | 362,300.00 USD | 71,860.00 USD | 58,920.00 USD | 0.00 USD |
| `1D` | `0.1680` | 175,740.00 USD | 0.00 USD | 175,740.00 USD | 40,170.00 USD | 0.00 USD | 8,670.00 USD |
| `7D` | `0.1681` | 231,520.00 USD | 0.00 USD | 231,520.00 USD | 46,250.00 USD | 36,390.00 USD | 15,310.00 USD |
| `1D` | `0.1682` | 126,900.00 USD | 0.00 USD | 126,900.00 USD | 55,230.00 USD | 6,130.00 USD | 18,210.00 USD |
| `1D` | `0.1684` | 47,330.00 USD | 0.00 USD | 47,330.00 USD | 0.00 USD | 15,370.00 USD | 5,340.00 USD |
| `7D` | `0.1684` | 133,570.00 USD | 0.00 USD | 133,570.00 USD | 60,960.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1686` | 26,610.00 USD | 0.00 USD | 26,610.00 USD | 0.00 USD | 26,610.00 USD | 0.00 USD |
| `7D` | `0.1693` | 72,620.00 USD | 0.00 USD | 72,620.00 USD | 0.00 USD | 32,070.00 USD | 0.00 USD |
| `7D` | `0.1696` | 40,550.00 USD | 0.00 USD | 40,550.00 USD | 0.00 USD | 40,550.00 USD | 0.00 USD |
| `7D` | `0.1704` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1705` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1705` | 70,320.00 USD | 70,320.00 USD | 0.00 USD | 70,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1708` | 11,770.00 USD | 11,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,770.00 USD |
| `7D` | `0.1708` | 168,190.00 USD | 168,190.00 USD | 0.00 USD | 33,170.00 USD | 0.00 USD | 64,690.00 USD |
| `1D` | `0.1710` | 49,520.00 USD | 49,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 37,750.00 USD |
| `1D` | `0.1712` | 94,210.00 USD | 94,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44,680.00 USD |
| `1D` | `0.1714` | 144,330.00 USD | 144,330.00 USD | 0.00 USD | 0.00 USD | 50,120.00 USD | 0.00 USD |
| `1D` | `0.1720` | 192,090.00 USD | 192,090.00 USD | 0.00 USD | 36,870.00 USD | 0.00 USD | 10,890.00 USD |
| `7D` | `0.1720` | 322,550.00 USD | 322,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 154,360.00 USD |
| `1D` | `0.1722` | 244,370.00 USD | 244,370.00 USD | 0.00 USD | 6,910.00 USD | 21,240.00 USD | 24,130.00 USD |
| `7D` | `0.1723` | 608,420.00 USD | 608,420.00 USD | 0.00 USD | 74,150.00 USD | 32,300.00 USD | 179,420.00 USD |
| `1D` | `0.1724` | 348,990.00 USD | 348,990.00 USD | 0.00 USD | 73,970.00 USD | 13,690.00 USD | 16,960.00 USD |
| `1D` | `0.1726` | 442,100.00 USD | 442,100.00 USD | 0.00 USD | 35,300.00 USD | 28,020.00 USD | 29,780.00 USD |
| `7D` | `0.1726` | 668,280.00 USD | 668,280.00 USD | 0.00 USD | 48,420.00 USD | 11,440.00 USD | 0.00 USD |
| `1D` | `0.1728` | 501,530.00 USD | 501,530.00 USD | 0.00 USD | 18,840.00 USD | 1,400.00 USD | 39,190.00 USD |
| `7D` | `0.1729` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 290,020.00 USD | 61,150.00 USD | 48,520.00 USD |
| `1D` | `0.1730` | 556,340.00 USD | 556,340.00 USD | 0.00 USD | 16,520.00 USD | 7,090.00 USD | 31,200.00 USD |
| `1D` | `0.1732` | 588,170.00 USD | 588,170.00 USD | 0.00 USD | 0.00 USD | 9,440.00 USD | 22,400.00 USD |
| `7D` | `0.1732` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 550,580.00 USD | 49,950.00 USD | 17,060.00 USD |
| `1D` | `0.1734` | 671,560.00 USD | 671,560.00 USD | 0.00 USD | 28,370.00 USD | 33,350.00 USD | 21,670.00 USD |
| `7D` | `0.1735` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 222,370.00 USD | 32,580.00 USD | 19,920.00 USD |
| `1D` | `0.1736` | 751,250.00 USD | 751,250.00 USD | 0.00 USD | 59,140.00 USD | 4,840.00 USD | 15,710.00 USD |
| `1D` | `0.1738` | 851,790.00 USD | 851,790.00 USD | 0.00 USD | 14,580.00 USD | 20,730.00 USD | 65,230.00 USD |
| `7D` | `0.1738` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 27,340.00 USD | 126,530.00 USD |
| `1D` | `0.1740` | 943,640.00 USD | 943,640.00 USD | 0.00 USD | 36,460.00 USD | 20,960.00 USD | 34,430.00 USD |
| `1D` | `0.1742` | 982,990.00 USD | 982,990.00 USD | 0.00 USD | 15,160.00 USD | 19,280.00 USD | 4,930.00 USD |
| `1D` | `0.1744` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 28,550.00 USD | 26,830.00 USD | 1,690.00 USD |
| `7D` | `0.1744` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 9,550.00 USD | 64,970.00 USD | 13,120.00 USD |
| `1D` | `0.1746` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 8,530.00 USD | 15,640.00 USD | 9,500.00 USD |
| `7D` | `0.1747` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 56,850.00 USD | 0.00 USD |
| `1D` | `0.1748` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 20,020.00 USD | 2,100.00 USD | 13,930.00 USD |
| `1D` | `0.1750` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 14,420.00 USD | 0.00 USD |
| `7D` | `0.1750` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 46,250.00 USD | 0.00 USD | 196,550.00 USD |
| `1D` | `0.1752` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 11,260.00 USD | 32,510.00 USD | 20,810.00 USD |
| `7D` | `0.1753` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 191,160.00 USD |
| `1D` | `0.1754` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 24,650.00 USD | 9,220.00 USD | 11,720.00 USD |
| `1D` | `0.1756` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 27,900.00 USD | 19,210.00 USD | 16,240.00 USD |
| `7D` | `0.1756` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 75,620.00 USD | 56,810.00 USD | 89,390.00 USD |
| `1D` | `0.1758` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 54,910.00 USD | 13,960.00 USD | 16,540.00 USD |
| `7D` | `0.1759` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 238,650.00 USD | 105,180.00 USD | 0.00 USD |
| `1D` | `0.1760` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 20,820.00 USD | 10,240.00 USD | 13,300.00 USD |
| `1D` | `0.1762` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 43,230.00 USD | 11,990.00 USD | 12,930.00 USD |
| `7D` | `0.1762` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 288,350.00 USD | 196,430.00 USD | 0.00 USD |
| `1D` | `0.1764` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 21,470.00 USD | 3,540.00 USD | 12,840.00 USD |
| `7D` | `0.1765` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 154,540.00 USD | 218,770.00 USD | 20,860.00 USD |
| `1D` | `0.1766` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 3,150.00 USD | 13,330.00 USD |
| `1D` | `0.1768` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 24,840.00 USD | 26,520.00 USD | 9,930.00 USD |
| `7D` | `0.1768` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 161,560.00 USD | 106,860.00 USD | 4,210.00 USD |
| `1D` | `0.1770` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 25,060.00 USD | 3,850.00 USD | 13,540.00 USD |
| `7D` | `0.1771` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 46,210.00 USD | 113,470.00 USD | 21,360.00 USD |
| `1D` | `0.1772` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 7,290.00 USD | 12,310.00 USD | 12,610.00 USD |
| `1D` | `0.1774` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 35,970.00 USD | 6,900.00 USD | 7,600.00 USD |
| `7D` | `0.1774` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 148,780.00 USD | 79,410.00 USD | 0.00 USD |
| `1D` | `0.1776` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 51,050.00 USD | 6,090.00 USD | 4,280.00 USD |
| `7D` | `0.1777` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 44,880.00 USD | 26,150.00 USD | 59,520.00 USD |
| `1D` | `0.1778` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 7,310.00 USD | 19,140.00 USD | 0.00 USD |
| `1D` | `0.1780` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 4,270.00 USD | 1,060.00 USD | 6,340.00 USD |
| `7D` | `0.1780` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 52,730.00 USD | 13,420.00 USD | 97,990.00 USD |
| `1D` | `0.1782` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 56,420.00 USD | 3,060.00 USD | 35,820.00 USD |
| `7D` | `0.1783` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 105,900.00 USD | 13,990.00 USD | 21,910.00 USD |
| `1D` | `0.1784` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 52,550.00 USD | 16,240.00 USD | 8,300.00 USD |
| `1D` | `0.1786` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 14,350.00 USD | 7,200.00 USD | 34,660.00 USD |
| `7D` | `0.1786` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 129,440.00 USD | 48,090.00 USD | 14,040.00 USD |
| `1D` | `0.1788` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 21,600.00 USD | 26,660.00 USD | 22,150.00 USD |
| `7D` | `0.1789` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 48,810.00 USD | 7,150.00 USD | 0.00 USD |
| `1D` | `0.1790` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 41,020.00 USD | 8,720.00 USD | 5,800.00 USD |
| `1D` | `0.1792` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 4,130.00 USD | 15,740.00 USD | 20,480.00 USD |
| `7D` | `0.1792` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 134,000.00 USD | 20,480.00 USD | 3,940.00 USD |
| `1D` | `0.1794` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 32,080.00 USD | 18,670.00 USD | 8,290.00 USD |
| `7D` | `0.1795` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 6,230.00 USD | 19,870.00 USD | 28,270.00 USD |
| `1D` | `0.1796` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 16,900.00 USD | 15,920.00 USD | 11,900.00 USD |
| `1D` | `0.1798` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 11,000.00 USD | 3,920.00 USD | 8,330.00 USD |
| `7D` | `0.1798` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 0.00 USD | 6,240.00 USD | 13,000.00 USD |
| `1D` | `0.1800` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 2,030.00 USD | 1,930.00 USD | 2,710.00 USD |
| `7D` | `0.1801` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 6,490.00 USD | 16,690.00 USD | 46,450.00 USD |
| `1D` | `0.1802` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 11,410.00 USD | 9,390.00 USD | 11,430.00 USD |
| `1D` | `0.1804` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 4,260.00 USD | 1,110.00 USD | 22,650.00 USD |
| `7D` | `0.1804` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 28,790.00 USD | 14,780.00 USD | 5,320.00 USD |
| `1D` | `0.1806` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 18,420.00 USD | 11,530.00 USD | 3,930.00 USD |
| `7D` | `0.1807` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 0.00 USD | 39,730.00 USD | 67,160.00 USD |
| `1D` | `0.1808` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 24,170.00 USD | 14,570.00 USD | 28,810.00 USD |
| `1D` | `0.1810` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 14,660.00 USD | 5,590.00 USD | 8,830.00 USD |
| `7D` | `0.1810` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 79,380.00 USD | 30,940.00 USD | 12,950.00 USD |
| `1D` | `0.1812` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 25,610.00 USD | 10,820.00 USD | 28,400.00 USD |
| `7D` | `0.1813` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 32,530.00 USD | 3,040.00 USD | 56,130.00 USD |
| `1D` | `0.1814` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 8,290.00 USD | 5,770.00 USD | 13,060.00 USD |
| `1D` | `0.1816` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 28,660.00 USD | 1,120.00 USD | 20,390.00 USD |
| `7D` | `0.1816` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 46,430.00 USD | 21,200.00 USD | 25,980.00 USD |
| `1D` | `0.1818` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 13,970.00 USD | 7,560.00 USD | 14,690.00 USD |
| `7D` | `0.1819` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 65,350.00 USD | 3,710.00 USD | 43,100.00 USD |
| `1D` | `0.1820` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 22,900.00 USD | 7,280.00 USD | 3,000.00 USD |
| `1D` | `0.1822` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 8,490.00 USD | 6,830.00 USD | 11,390.00 USD |
| `7D` | `0.1822` | 6,560,000.00 USD | 6,560,000.00 USD | 0.00 USD | 46,760.00 USD | 36,230.00 USD | 92,280.00 USD |
| `1D` | `0.1824` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 6,880.00 USD | 8,890.00 USD | 13,500.00 USD |
| `7D` | `0.1825` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 61,720.00 USD | 17,120.00 USD | 12,140.00 USD |
| `1D` | `0.1826` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 24,440.00 USD | 6,860.00 USD | 5,430.00 USD |
| `1D` | `0.1828` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 3,490.00 USD | 0.00 USD | 3,740.00 USD |
| `7D` | `0.1828` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 51,470.00 USD | 24,320.00 USD | 69,840.00 USD |
| `1D` | `0.1830` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 5,730.00 USD | 8,420.00 USD |
| `7D` | `0.1831` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 85,970.00 USD | 21,930.00 USD | 63,170.00 USD |
| `1D` | `0.1832` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 2,990.00 USD | 4,630.00 USD |
| `1D` | `0.1834` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 1,420.00 USD | 655.16 USD | 3,390.00 USD |
| `7D` | `0.1834` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 165,640.00 USD | 47,980.00 USD | 51,750.00 USD |
| `1D` | `0.1836` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 3,610.00 USD | 0.00 USD | 1,620.00 USD |
| `7D` | `0.1837` | 7,460,000.00 USD | 7,460,000.00 USD | 0.00 USD | 72,930.00 USD | 76,140.00 USD | 83,480.00 USD |
| `1D` | `0.1838` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 2,640.00 USD | 5,780.00 USD |
| `1D` | `0.1840` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 5,430.00 USD | 0.00 USD | 10,500.00 USD |
| `7D` | `0.1840` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 98,270.00 USD | 47,250.00 USD | 80,190.00 USD |
| `1D` | `0.1842` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 7,720.00 USD | 3,670.00 USD | 0.00 USD |
| `7D` | `0.1843` | 7,900,000.00 USD | 7,900,000.00 USD | 0.00 USD | 86,180.00 USD | 18,570.00 USD | 105,350.00 USD |
| `1D` | `0.1844` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 2,690.00 USD | 3,930.00 USD | 15,280.00 USD |
| `1D` | `0.1846` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 2,950.00 USD | 2,790.00 USD | 7,930.00 USD |
| `7D` | `0.1846` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 8,330.00 USD | 56,460.00 USD | 199,630.00 USD |
| `1D` | `0.1848` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 4,680.00 USD | 5,780.00 USD | 3,310.00 USD |
| `7D` | `0.1849` | 8,390,000.00 USD | 8,390,000.00 USD | 0.00 USD | 104,530.00 USD | 79,580.00 USD | 38,800.00 USD |
| `1D` | `0.1850` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD | 1,300.00 USD |
| `1D` | `0.1852` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 1,690.00 USD | 4,440.00 USD |
| `7D` | `0.1852` | 8,780,000.00 USD | 8,780,000.00 USD | 0.00 USD | 153,970.00 USD | 9,590.00 USD | 234,380.00 USD |
| `1D` | `0.1854` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 1,510.00 USD | 0.00 USD | 7,420.00 USD |
| `7D` | `0.1855` | 8,950,000.00 USD | 8,950,000.00 USD | 0.00 USD | 58,210.00 USD | 10,160.00 USD | 94,330.00 USD |
| `1D` | `0.1856` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 3,340.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1858` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 3,590.00 USD | 1,470.00 USD | 3,670.00 USD |
| `7D` | `0.1858` | 9,230,000.00 USD | 9,230,000.00 USD | 0.00 USD | 96,280.00 USD | 51,010.00 USD | 133,250.00 USD |
| `1D` | `0.1860` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 5,860.00 USD | 2,970.00 USD | 2,100.00 USD |
| `7D` | `0.1861` | 9,400,000.00 USD | 9,400,000.00 USD | 0.00 USD | 99,880.00 USD | 55,030.00 USD | 21,120.00 USD |
| `1D` | `0.1862` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD | 5,050.00 USD |
| `1D` | `0.1864` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,930.00 USD |
| `7D` | `0.1864` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 87,420.00 USD | 65,980.00 USD | 61,380.00 USD |
| `1D` | `0.1866` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 3,300.00 USD | 0.00 USD | 5,140.00 USD |
| `7D` | `0.1867` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 130,970.00 USD | 47,840.00 USD | 73,600.00 USD |
| `1D` | `0.1868` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,160.00 USD |
| `1D` | `0.1870` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 4,960.00 USD | 5,040.00 USD | 3,970.00 USD |
| `7D` | `0.1870` | 10,240,000.00 USD | 10,240,000.00 USD | 0.00 USD | 175,600.00 USD | 83,890.00 USD | 113,170.00 USD |
| `1D` | `0.1872` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 9,350.00 USD | 0.00 USD | 3,140.00 USD |
| `7D` | `0.1873` | 10,550,000.00 USD | 10,550,000.00 USD | 0.00 USD | 72,410.00 USD | 122,400.00 USD | 116,760.00 USD |
| `1D` | `0.1874` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 1,960.00 USD | 2,820.00 USD | 2,290.00 USD |
| `7D` | `0.1876` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 76,050.00 USD | 41,870.00 USD | 10,330.00 USD |
| `1D` | `0.1878` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 4,320.00 USD | 2,760.00 USD | 4,090.00 USD |
| `7D` | `0.1879` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 48,260.00 USD | 46,860.00 USD | 48,730.00 USD |
| `1D` | `0.1880` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 2,880.00 USD | 3,160.00 USD | 3,960.00 USD |
| `1D` | `0.1882` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 4,630.00 USD | 4,960.00 USD | 0.00 USD |
| `7D` | `0.1882` | 10,960,000.00 USD | 10,960,000.00 USD | 0.00 USD | 14,000.00 USD | 29,330.00 USD | 91,340.00 USD |
| `1D` | `0.1884` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 4,050.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1885` | 11,040,000.00 USD | 11,040,000.00 USD | 0.00 USD | 41,060.00 USD | 31,900.00 USD | 4,670.00 USD |
| `1D` | `0.1886` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 4,000.00 USD | 0.00 USD | 1,730.00 USD |
| `1D` | `0.1888` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 3,150.00 USD | 0.00 USD |
| `7D` | `0.1888` | 11,150,000.00 USD | 11,150,000.00 USD | 0.00 USD | 13,720.00 USD | 17,330.00 USD | 83,540.00 USD |
| `1D` | `0.1890` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 4,570.00 USD | 7,640.00 USD |
| `7D` | `0.1891` | 11,210,000.00 USD | 11,210,000.00 USD | 0.00 USD | 36,740.00 USD | 0.00 USD | 17,340.00 USD |
| `1D` | `0.1892` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 1,140.00 USD | 1,840.00 USD | 1,070.00 USD |
| `1D` | `0.1894` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 4,810.00 USD | 2,620.00 USD | 959.69 USD |
| `7D` | `0.1894` | 11,310,000.00 USD | 11,310,000.00 USD | 0.00 USD | 69,540.00 USD | 12,420.00 USD | 16,820.00 USD |
| `1D` | `0.1896` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 4,500.00 USD | 1,530.00 USD | 2,930.00 USD |
| `7D` | `0.1897` | 11,390,000.00 USD | 11,390,000.00 USD | 0.00 USD | 25,640.00 USD | 31,390.00 USD | 25,080.00 USD |
| `1D` | `0.1898` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 2,530.00 USD | 3,640.00 USD | 0.00 USD |
| `7D` | `0.1900` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 11,530.00 USD | 21,370.00 USD | 7,550.00 USD |
| `7D` | `0.1903` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 14,330.00 USD | 11,220.00 USD | 5,200.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `213.35M` | Total OI Tokens: `1,255,126,388.4 ARB`
  * 1h OI Change: `-1.37%` | 4h OI Change: `-0.01%` | 24h OI Change: `-8.65%`
  * Exchange Breakdown: Binance=`49.45M` | Bybit=`29.77M` | OKX=`16.95M` | Hyperliquid=`14.72M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `9.57K` | Last 24h: `645.76` | Last 3d: `18.56K` | Last 7d: `31.80K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0099%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0099%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0027%` | **USDT Bitget** | `0.0072%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `44.96%` | `55.04%` | `0.82` | 3,650,000.00 USD |
| `15M` | `Binance` | `49.52%` | `50.48%` | `0.98` | 1,150,000.00 USD |
| `15M` | `OKX` | `47.69%` | `52.31%` | `0.91` | 174,680.00 USD |
| `15M` | `Bybit` | `43.35%` | `56.65%` | `0.77` | 93,100.00 USD |
| `15M` | `KuCoin` | `48.36%` | `51.64%` | `0.94` | 16,350.00 USD |
| `15M` | `Gate` | `50.5%` | `49.5%` | `1.02` | 33,920.00 USD |
| `15M` | `Bitget` | `20.61%` | `79.39%` | `0.26` | 76,240.00 USD |
| `15M` | `BingX` | `41.84%` | `58.16%` | `0.72` | 849,570.00 USD |
| `15M` | `MEXC` | `39.37%` | `60.63%` | `0.65` | 148,240.00 USD |
| `15M` | `Bitunix` | `53.69%` | `46.31%` | `1.16` | 53,320.00 USD |
| `15M` | `Hyperliquid` | `43.89%` | `56.11%` | `0.78` | 121,100.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `45.48%` | `54.52%` | `0.83` | 555,850.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.88 USD |
| `15M` | `WhiteBIT` | `68.92%` | `31.08%` | `2.22` | 371,170.00 USD |
| `15M` | `HTX` | `66.67%` | `33.33%` | `2.00` | 740.61 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `100%` | `0.00` | 1,380.00 USD |
| `15M` | `Aster` | `7.99%` | `92.01%` | `0.09` | 1,910.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `58.27%` | `41.73%` | `1.40` | 5,250.00 USD |
| `15M` | `Whale Positions` | `49.52%` | `50.48%` | `0.98` | 1,150,000.00 USD |
| `15M` | `Global Accounts` | `44.96%` | `55.04%` | `0.82` | 3,650,000.00 USD |
| `1H` | `ARB` | `48.74%` | `51.26%` | `0.95` | 105,400,000.00 USD |
| `1H` | `Binance` | `47.74%` | `52.26%` | `0.91` | 44,070,000.00 USD |
| `1H` | `OKX` | `49.09%` | `50.91%` | `0.96` | 15,990,000.00 USD |
| `1H` | `Bybit` | `50.11%` | `49.89%` | `1.00` | 14,790,000.00 USD |
| `1H` | `KuCoin` | `52.18%` | `47.82%` | `1.09` | 654,980.00 USD |
| `1H` | `Gate` | `45.8%` | `54.2%` | `0.85` | 1,490,000.00 USD |
| `1H` | `Bitget` | `52.93%` | `47.07%` | `1.12` | 5,690,000.00 USD |
| `1H` | `BingX` | `44.95%` | `55.05%` | `0.82` | 3,620,000.00 USD |
| `1H` | `MEXC` | `47.63%` | `52.37%` | `0.91` | 4,990,000.00 USD |
| `1H` | `Bitunix` | `49.16%` | `50.84%` | `0.97` | 3,050,000.00 USD |
| `1H` | `Hyperliquid` | `40.68%` | `59.32%` | `0.69` | 4,990,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.63%` | `52.37%` | `0.91` | 832,510.00 USD |
| `1H` | `Crypto.com` | `47.76%` | `52.24%` | `0.91` | 17,040.00 USD |
| `1H` | `WhiteBIT` | `68.96%` | `31.04%` | `2.22` | 2,630,000.00 USD |
| `1H` | `HTX` | `51.53%` | `48.47%` | `1.06` | 254,090.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `52.07%` | `47.93%` | `1.09` | 1,520,000.00 USD |
| `1H` | `Aster` | `49.96%` | `50.04%` | `1.00` | 31,510.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `44.44%` | `55.56%` | `0.80` | 783,090.00 USD |
| `1H` | `Whale Positions` | `47.74%` | `52.26%` | `0.91` | 44,070,000.00 USD |
| `1H` | `Global Accounts` | `48.74%` | `51.26%` | `0.95` | 105,400,000.00 USD |
| `4H` | `ARB` | `55.33%` | `44.67%` | `1.24` | 48,580,000.00 USD |
| `4H` | `Binance` | `52.79%` | `47.21%` | `1.12` | 12,630,000.00 USD |
| `4H` | `OKX` | `48.76%` | `51.24%` | `0.95` | 4,740,000.00 USD |
| `4H` | `Bybit` | `66.68%` | `33.32%` | `2.00` | 5,490,000.00 USD |
| `4H` | `KuCoin` | `49.81%` | `50.19%` | `0.99` | 430,860.00 USD |
| `4H` | `Gate` | `48.68%` | `51.32%` | `0.95` | 6,260,000.00 USD |
| `4H` | `Bitget` | `50.81%` | `49.19%` | `1.03` | 646,010.00 USD |
| `4H` | `BingX` | `46.13%` | `53.87%` | `0.86` | 10,800,000.00 USD |
| `4H` | `MEXC` | `51.9%` | `48.1%` | `1.08` | 753,340.00 USD |
| `4H` | `Bitunix` | `53.2%` | `46.8%` | `1.14` | 794,140.00 USD |
| `4H` | `Hyperliquid` | `54.82%` | `45.18%` | `1.21` | 175,070.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.51%` | `49.49%` | `1.02` | 1,540,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `95.32%` | `4.68%` | `20.37` | 3,870,000.00 USD |
| `4H` | `HTX` | `66.48%` | `33.52%` | `1.98` | 86,450.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `64.09%` | `35.91%` | `1.78` | 295,940.00 USD |
| `4H` | `Aster` | `62.18%` | `37.82%` | `1.64` | 37,100.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `61.34%` | `38.66%` | `1.59` | 26,830.00 USD |
| `4H` | `Whale Positions` | `52.79%` | `47.21%` | `1.12` | 12,630,000.00 USD |
| `4H` | `Global Accounts` | `55.33%` | `44.67%` | `1.24` | 48,580,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1684` | `0.1681` | `0.1684` | `0.1686` | `0.1674` | 446,205.68 USD | 230,756.41 USD | 215,449.27 USD | 15,307.14 USD | `+3.43%` | `34B / 21S` |
| `0:00 UTC` | `0.1682` | `0.1680` | `0.1682` | `0.1683` | `0.1674` | 484,114.34 USD | 229,312.56 USD | 254,801.78 USD | -25,489.21 USD | `-5.27%` | `8B / 14S` |
| `5:00 UTC` | `0.1682` | `0.1684` | `0.1682` | `0.1689` | `0.1680` | 510,391.75 USD | 241,704.72 USD | 268,687.03 USD | -26,982.30 USD | `-5.29%` | `10B / 14S` |
| `0:00 UTC` | `0.1699` | `0.1696` | `0.1699` | `0.1705` | `0.1682` | 1,318,321.77 USD | 721,056.29 USD | 597,265.48 USD | 123,790.81 USD | `+9.39%` | `26B / 9S` |
| `5:00 UTC` | `0.1701` | `0.1703` | `0.1701` | `0.1710` | `0.1699` | 1,100,970.36 USD | 446,093.76 USD | 654,876.60 USD | -208,782.83 USD | `-18.96%` | `11B / 28S` |
| `0:00 UTC` | `0.1718` | `0.1715` | `0.1718` | `0.1722` | `0.1705` | 2,029,934.04 USD | 850,328.25 USD | 1,179,605.79 USD | -329,277.54 USD | `-16.22%` | `17B / 39S` |
| `5:00 UTC` | `0.1710` | `0.1707` | `0.1710` | `0.1716` | `0.1700` | 959,671.94 USD | 464,352.66 USD | 495,319.27 USD | -30,966.61 USD | `-3.23%` | `30B / 30S` |
| `0:00 UTC` | `0.1693` | `0.1693` | `0.1693` | `0.1704` | `0.1685` | 1,438,333.93 USD | 705,582.08 USD | 732,751.85 USD | -27,169.77 USD | `-1.89%` | `16B / 44S` |
| `5:00 UTC` | `0.1701` | `0.1701` | `0.1701` | `0.1709` | `0.1692` | 883,684.54 USD | 412,493.60 USD | 471,190.94 USD | -58,697.35 USD | `-6.64%` | `23B / 30S` |
| `0:00 UTC` | `0.1704` | `0.1701` | `0.1704` | `0.1707` | `0.1695` | 611,622.67 USD | 277,546.25 USD | 334,076.43 USD | -56,530.18 USD | `-9.24%` | `12B / 31S` |

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
| `5m` | 1,970.00 USD | 38,180.00 USD | **`ACCUMULATION`** |
| `15m` | 17,650.00 USD | 95,980.00 USD | **`ACCUMULATION`** |
| `30m` | -9,280.00 USD | 140,800.00 USD | **`ACCUMULATION`** |
| `1h` | -87,470.00 USD | -438,740.00 USD | **`DISTRIBUTION`** |
| `2h` | 25,380.00 USD | -963,150.00 USD | **`DISTRIBUTION`** |
| `4h` | 370,810.00 USD | -1,650,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 479,270.00 USD | -1,340,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 80,990.00 USD | -2,360,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -210,560.00 USD | -610,470.00 USD | **`DISTRIBUTION`** |
| `24h` | -552,750.00 USD | -4,910,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,030,000.00 USD | -29,210,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -32,880,000.00 USD | -163,770,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+1.97K` | 15m=`+17.65K` | 1h=`-87.47K` | 24h=`-552.75K`
* Futures Capital Netflows: 5m=`+38.18K` | 15m=`+95.98K` | 1h=`-438.74K` | 24h=`-4.91M`
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
  * `2026-10-29 19:41:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:20:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:09:49 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-29 16:50:49 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [bankofengland.co.uk] - (Sentiment: `Neutral`)


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
