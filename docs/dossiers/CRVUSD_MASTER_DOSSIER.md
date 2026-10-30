# 🏛️ SOVEREIGN CANDIDATE DOSSIER: CRVUSD
**Canonical Key**: `CRVUSD` | **Broker Instrument**: `CRVUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 16:45:52 IST` (`2026-10-30 11:15:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.2760` | **Live Ask Quote**: `0.2980` | **Mid Price**: `0.2870`
- **Spread Points**: `22.00` | **Spread BPS**: `766.55 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
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
  * Session VWAP: `0.2713` | VWAP Z-Score: `+0.47` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0036` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `60.04` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3012` | Lower -3.00σ Band: `0.2414`
  * Upper +2.51σ Band: `0.2963` | Lower -2.51σ Band: `0.2463`
  * Upper +2.01σ Band: `0.2913` | Lower -2.01σ Band: `0.2513`
  * Upper +2.00σ Band: `0.2912` | Lower -2.00σ Band: `0.2514`
  * Upper +1.28σ Band: `0.2841` | Lower -1.28σ Band: `0.2585`
  * Upper +1.00σ Band: `0.2813` | Lower -1.00σ Band: `0.2613`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.2725` | EMA-20=`0.2708` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.2762` (Slope: `+0.0000`) | EMA-100=`0.2877`
  * Institutional Anchors: EMA-144=`0.2947` | EMA-200=`0.3011` (Slope: `-1.2133`) | EMA-233=`0.3039`
- **Range Boundaries**: 24H High=`0.3270` | 24H Low=`0.2530` | Weekly High=`0.3340` | Weekly Low=`0.2530`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.2860` (Distance: `+0.42%`)
  * Point of Control (POC) = `0.2630` (Distance: `+9.11%`)
  * Value Area Low (VAL) = `0.2570` (Distance: `+11.71%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3230` | POC=`0.3160` | VAL=`0.3100`
  * Prior Day Extremes: PDH=`0.3330` | PDL=`0.2890` | PDC=`0.2980`
  * Monday Range Blueprint: High=`0.3430` | Mid=`0.3340` | Low=`0.3250`
  * Developing Weekly Value Area: Weekly VAH=`0.3420` | Weekly POC=`0.3280` | Weekly VAL=`0.3110`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3040` | Low=`0.2530`
  * London Session (08:00-16:00 UTC): High=`0.2760` | Low=`0.2570`
  * New York Session (13:00-21:00 UTC): High=`0.2760` | Low=`0.2700`
  * Initial Balance (First Hour): IB High=`0.2640` | IB Low=`0.2580`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.2859` - `0.2881`
  * Optimal Trade Entry (OTE 0.705): `0.2876`
  * Structural Invalidation Anchor (0.786): `0.2893`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `15m` | - | - | - | - | - | 0.00 USD | 0.00 USD | `+0.00%` | 0.00 USD | `0.00` | **`BALANCED`** | Interbank Volume |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:42:20 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1816` | `0x12d2...f97f` | `LONG` | 1,140,122.38 USD | `3,972,828.70` | `0.3272` | `0.2872` | `0.000000` | -159,716.36 USD | `-14.01%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3526` | 6,026.15 USD | `-` | `NEWS_INTEL` | `-` | #CRV Liquidated Short: 6.03K USD at 0.3526 USD [API] | `2026-10-23 22:42:24` |
| `ANNOUNCEMENT` | `INFO` | `0.3181` | 57.22 USD | `-` | `NEWS_INTEL` | `-` | #CRV Liquidated Short: 0.06K USD at 0.3181 USD [API] | `2026-10-29 20:06:55` |
| `ANNOUNCEMENT` | `INFO` | `0.3213` | 1,611.91 USD | `-` | `NEWS_INTEL` | `-` | #CRV Liquidated Short: 1.61K USD at 0.3213 USD [API] | `2026-10-29 20:04:17` |
| `ANNOUNCEMENT` | `INFO` | `0.3179` | 806.51 USD | `-` | `NEWS_INTEL` | `-` | #CRV Liquidated Short: 0.81K USD at 0.3179 USD [API] | `2026-10-29 20:35:42` |
| `ANNOUNCEMENT` | `INFO` | `0.3181` | 1,390.07 USD | `-` | `NEWS_INTEL` | `-` | #CRV Liquidated Short: 1.39K USD at 0.3181 USD [API] | `2026-10-29 20:35:42` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.3453` (Vol: 74,017.03 USD, Dist: `+2.95%`) | Long MP=`0.3285` (Vol: 54,223.53 USD, Dist: `--2.06%`)
  * 48H Horizon: Short MP=`0.3451` (Vol: 61,276.63 USD, Dist: `+2.89%`) | Long MP=`0.3266` (Vol: 86,480.44 USD, Dist: `--2.62%`)
  * 3D Horizon: Short MP=`0.3454` (Vol: 78,069.95 USD, Dist: `+2.98%`) | Long MP=`0.3267` (Vol: 81,272.05 USD, Dist: `--2.59%`)
  * 7D Horizon: Short MP=`0.3626` (Vol: 135,917.70 USD, Dist: `+8.67%`) | Long MP=`0.3267` (Vol: 96,300.06 USD, Dist: `--2.09%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0585` | 2,580.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 477.15 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 4,490.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 2,640.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 306.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 2,350.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 14,790.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 485.44 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 460.38 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 4,850.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 1,290.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 1,960.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 5,530.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 116.35 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 4,300.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 342.90 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1385` | 22,160.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 1,150.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 6,200.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 1,160.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 12,380.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1495` | 22,430.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 3,810.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 21,090.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 722.25 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 19,500.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 397.60 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1655` | 3,990.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 4,930.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 278.30 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 464.68 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 4,670.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 2,940.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 1,340.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 14,130.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1785` | 39,360.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 5,890.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1805` | 14,020.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1815` | 13,980.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1825` | 1,670.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1835` | 179.10 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1845` | 25,400.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1865` | 7,460.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 13,340.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1885` | 1,660.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1895` | 1,050.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1905` | 31,840.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1925` | 8,820.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1935` | 5,280.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1945` | 303.61 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1955` | 13,540.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1975` | 292.69 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1985` | 4,100.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 3,430.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2015` | 132,260.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 18,380.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2055` | 1,060.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2075` | 42,550.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2085` | 2,970.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2095` | 69,880.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2115` | 55,550.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2125` | 521.03 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2145` | 68,790.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2155` | 4,800.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2165` | 1,900.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 9,880.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2185` | 153,610.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 899.88 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 9,110.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2215` | 128,040.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 5,630.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2255` | 676.50 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2265` | 83,810.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2285` | 19,240.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 160.65 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 74,180.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 5,840.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 30,810.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 1,940.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 336.32 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 10,150.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 24,980.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 1,050.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 91,590.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2395` | 15,990.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 41,930.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2415` | 32,410.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 399,620.00 USD | 981,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 51,230.00 USD | 581,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 1,290.00 USD | 530,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 12,150.00 USD | 529,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 5,140.00 USD | 517,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 53,540.00 USD | 512,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 31,460.00 USD | 458,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2495` | 28,290.00 USD | 427,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 5,090.00 USD | 398,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2515` | 18,010.00 USD | 393,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2535` | 6,370.00 USD | 375,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2545` | 27,660.00 USD | 369,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 25,730.00 USD | 341,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 361.20 USD | 315,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2575` | 60,670.00 USD | 315,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 29,640.00 USD | 254,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 101,220.00 USD | 225,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 89,520.00 USD | 124,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 9,490.00 USD | 34,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 342.09 USD | 25,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 126.69 USD | 24,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 1,320.00 USD | 24,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 345.52 USD | 23,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 535.00 USD | 22,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 6,780.00 USD | 22,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2695` | 7,320.00 USD | 15,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2715` | 8,150.00 USD | 8,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 147.68 USD | 147.68 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2905` | 22,150.00 USD | 22,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 515.62 USD | 22,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2975` | 423.94 USD | 23,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3005` | 5,940.00 USD | 29,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3015` | 81,220.00 USD | 110,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3215` | 5,380.00 USD | 115,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3235` | 747.16 USD | 116,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3415` | 105.22 USD | 116,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3425` | 103.85 USD | 116,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3485` | 413.95 USD | 117,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3575` | 100.14 USD | 117,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 2,100.00 USD | 119,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3675` | 2,100.00 USD | 121,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3865` | 119.35 USD | 121,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3885` | 103.81 USD | 121,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3965` | 47,580.00 USD | 169,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4025` | 238.76 USD | 169,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4035` | 165.84 USD | 169,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4165` | 587.64 USD | 170,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4205` | 1,700.00 USD | 171,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4305` | 313,830.00 USD | 485,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4365` | 1,400.00 USD | 487,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4445` | 666.75 USD | 487,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4555` | 1,010.00 USD | 488,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4585` | 216.14 USD | 488,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4775` | 24,100.00 USD | 513,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5155` | 428.28 USD | 513,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5315` | 14,510.00 USD | 527,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5455` | 108.72 USD | 528,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5565` | 2,860.00 USD | 530,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5605` | 546.15 USD | 531,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0585` | 2,500,000.00 USD | 0.00 USD | 2,580.00 USD | `-79.62%` | `44,136.50` |
| `Live` | `Long` | `0.0635` | 2,500,000.00 USD | 0.00 USD | 477.15 USD | `-77.87%` | `7,514.20` |
| `Live` | `Long` | `0.0645` | 2,500,000.00 USD | 0.00 USD | 4,490.00 USD | `-77.53%` | `69,582.00` |
| `Live` | `Long` | `0.0685` | 2,500,000.00 USD | 0.00 USD | 2,640.00 USD | `-76.13%` | `38,602.60` |
| `Live` | `Long` | `0.0765` | 2,490,000.00 USD | 0.00 USD | 306.00 USD | `-73.34%` | `4,000.00` |
| `Live` | `Long` | `0.0795` | 2,490,000.00 USD | 0.00 USD | 2,350.00 USD | `-72.30%` | `29,622.60` |
| `Live` | `Long` | `0.0815` | 2,490,000.00 USD | 0.00 USD | 14,790.00 USD | `-71.60%` | `181,411.80` |
| `Live` | `Long` | `0.0865` | 2,480,000.00 USD | 0.00 USD | 485.44 USD | `-69.86%` | `5,612.00` |
| `Live` | `Long` | `0.0965` | 2,480,000.00 USD | 0.00 USD | 460.38 USD | `-66.38%` | `4,770.80` |
| `Live` | `Long` | `0.1005` | 2,480,000.00 USD | 0.00 USD | 4,850.00 USD | `-64.98%` | `48,255.50` |
| `Live` | `Long` | `0.1095` | 2,470,000.00 USD | 0.00 USD | 1,290.00 USD | `-61.85%` | `11,739.70` |
| `Live` | `Long` | `0.1165` | 2,470,000.00 USD | 0.00 USD | 1,960.00 USD | `-59.41%` | `16,859.10` |
| `Live` | `Long` | `0.1175` | 2,470,000.00 USD | 0.00 USD | 5,530.00 USD | `-59.06%` | `47,058.80` |
| `Live` | `Long` | `0.1225` | 2,460,000.00 USD | 0.00 USD | 116.35 USD | `-57.32%` | `949.80` |
| `Live` | `Long` | `0.1255` | 2,460,000.00 USD | 0.00 USD | 4,300.00 USD | `-56.27%` | `34,264.40` |
| `Live` | `Long` | `0.1305` | 2,460,000.00 USD | 0.00 USD | 342.90 USD | `-54.53%` | `2,627.60` |
| `Live` | `Long` | `0.1385` | 2,460,000.00 USD | 0.00 USD | 22,160.00 USD | `-51.74%` | `160,000.00` |
| `Live` | `Long` | `0.1425` | 2,440,000.00 USD | 0.00 USD | 1,150.00 USD | `-50.35%` | `8,042.60` |
| `Live` | `Long` | `0.1435` | 2,430,000.00 USD | 0.00 USD | 6,200.00 USD | `-50.00%` | `43,210.20` |
| `Live` | `Long` | `0.1445` | 2,430,000.00 USD | 0.00 USD | 1,160.00 USD | `-49.65%` | `8,000.00` |
| `Live` | `Long` | `0.1465` | 2,430,000.00 USD | 0.00 USD | 12,380.00 USD | `-48.95%` | `84,498.00` |
| `Live` | `Long` | `0.1495` | 2,410,000.00 USD | 0.00 USD | 22,430.00 USD | `-47.91%` | `150,000.00` |
| `Live` | `Long` | `0.1525` | 2,390,000.00 USD | 0.00 USD | 3,810.00 USD | `-46.86%` | `25,000.00` |
| `Live` | `Long` | `0.1595` | 2,390,000.00 USD | 0.00 USD | 21,090.00 USD | `-44.43%` | `132,229.20` |
| `Live` | `Long` | `0.1605` | 2,370,000.00 USD | 0.00 USD | 722.25 USD | `-44.08%` | `4,500.00` |
| `Live` | `Long` | `0.1625` | 2,370,000.00 USD | 0.00 USD | 19,500.00 USD | `-43.38%` | `120,000.00` |
| `Live` | `Long` | `0.1645` | 2,350,000.00 USD | 0.00 USD | 397.60 USD | `-42.68%` | `2,417.00` |
| `Live` | `Long` | `0.1655` | 2,350,000.00 USD | 0.00 USD | 3,990.00 USD | `-42.33%` | `24,121.10` |
| `Live` | `Long` | `0.1665` | 2,340,000.00 USD | 0.00 USD | 4,930.00 USD | `-41.99%` | `29,616.80` |
| `Live` | `Long` | `0.1695` | 2,340,000.00 USD | 0.00 USD | 278.30 USD | `-40.94%` | `1,641.90` |
| `Live` | `Long` | `0.1715` | 2,340,000.00 USD | 0.00 USD | 464.68 USD | `-40.24%` | `2,709.50` |
| `Live` | `Long` | `0.1725` | 2,340,000.00 USD | 0.00 USD | 4,670.00 USD | `-39.90%` | `27,059.00` |
| `Live` | `Long` | `0.1755` | 2,330,000.00 USD | 0.00 USD | 2,940.00 USD | `-38.85%` | `16,780.50` |
| `Live` | `Long` | `0.1765` | 2,330,000.00 USD | 0.00 USD | 1,340.00 USD | `-38.50%` | `7,607.60` |
| `Live` | `Long` | `0.1775` | 2,330,000.00 USD | 0.00 USD | 14,130.00 USD | `-38.15%` | `79,610.90` |
| `Live` | `Long` | `0.1785` | 2,310,000.00 USD | 0.00 USD | 39,360.00 USD | `-37.80%` | `220,516.90` |
| `Live` | `Long` | `0.1795` | 2,270,000.00 USD | 0.00 USD | 5,890.00 USD | `-37.46%` | `32,795.10` |
| `Live` | `Long` | `0.1805` | 2,270,000.00 USD | 0.00 USD | 14,020.00 USD | `-37.11%` | `77,683.60` |
| `Live` | `Long` | `0.1815` | 2,250,000.00 USD | 0.00 USD | 13,980.00 USD | `-36.76%` | `77,027.00` |
| `Live` | `Long` | `0.1825` | 2,240,000.00 USD | 0.00 USD | 1,670.00 USD | `-36.41%` | `9,160.60` |
| `Live` | `Long` | `0.1835` | 2,240,000.00 USD | 0.00 USD | 179.10 USD | `-36.06%` | `976.00` |
| `Live` | `Long` | `0.1845` | 2,240,000.00 USD | 0.00 USD | 25,400.00 USD | `-35.71%` | `137,653.50` |
| `Live` | `Long` | `0.1865` | 2,210,000.00 USD | 0.00 USD | 7,460.00 USD | `-35.02%` | `40,000.00` |
| `Live` | `Long` | `0.1875` | 2,210,000.00 USD | 0.00 USD | 13,340.00 USD | `-34.67%` | `71,135.10` |
| `Live` | `Long` | `0.1885` | 2,190,000.00 USD | 0.00 USD | 1,660.00 USD | `-34.32%` | `8,802.20` |
| `Live` | `Long` | `0.1895` | 2,190,000.00 USD | 0.00 USD | 1,050.00 USD | `-33.97%` | `5,539.20` |
| `Live` | `Long` | `0.1905` | 2,190,000.00 USD | 0.00 USD | 31,840.00 USD | `-33.62%` | `167,120.70` |
| `Live` | `Long` | `0.1925` | 2,160,000.00 USD | 0.00 USD | 8,820.00 USD | `-32.93%` | `45,821.40` |
| `Live` | `Long` | `0.1935` | 2,150,000.00 USD | 0.00 USD | 5,280.00 USD | `-32.58%` | `27,264.60` |
| `Live` | `Long` | `0.1945` | 2,140,000.00 USD | 0.00 USD | 303.61 USD | `-32.23%` | `1,561.00` |
| `Live` | `Long` | `0.1955` | 2,140,000.00 USD | 0.00 USD | 13,540.00 USD | `-31.88%` | `69,252.60` |
| `Live` | `Long` | `0.1975` | 2,130,000.00 USD | 0.00 USD | 292.69 USD | `-31.18%` | `1,482.00` |
| `Live` | `Long` | `0.1985` | 2,130,000.00 USD | 0.00 USD | 4,100.00 USD | `-30.84%` | `20,652.40` |
| `Live` | `Long` | `0.1995` | 2,130,000.00 USD | 0.00 USD | 3,430.00 USD | `-30.49%` | `17,199.40` |
| `Live` | `Long` | `0.2015` | 2,120,000.00 USD | 0.00 USD | 132,260.00 USD | `-29.79%` | `656,375.00` |
| `Live` | `Long` | `0.2045` | 1,990,000.00 USD | 0.00 USD | 18,380.00 USD | `-28.75%` | `89,877.80` |
| `Live` | `Long` | `0.2055` | 1,970,000.00 USD | 0.00 USD | 1,060.00 USD | `-28.40%` | `5,147.80` |
| `Live` | `Long` | `0.2075` | 1,970,000.00 USD | 0.00 USD | 42,550.00 USD | `-27.70%` | `205,050.00` |
| `Live` | `Long` | `0.2085` | 1,930,000.00 USD | 0.00 USD | 2,970.00 USD | `-27.35%` | `14,230.20` |
| `Live` | `Long` | `0.2095` | 1,930,000.00 USD | 0.00 USD | 69,880.00 USD | `-27.00%` | `333,552.00` |
| `Live` | `Long` | `0.2115` | 1,860,000.00 USD | 0.00 USD | 55,550.00 USD | `-26.31%` | `262,635.40` |
| `Live` | `Long` | `0.2125` | 1,800,000.00 USD | 0.00 USD | 521.03 USD | `-25.96%` | `2,451.90` |
| `Live` | `Long` | `0.2145` | 1,800,000.00 USD | 0.00 USD | 68,790.00 USD | `-25.26%` | `320,696.20` |
| `Live` | `Long` | `0.2155` | 1,730,000.00 USD | 0.00 USD | 4,800.00 USD | `-24.91%` | `22,278.60` |
| `Live` | `Long` | `0.2165` | 1,730,000.00 USD | 0.00 USD | 1,900.00 USD | `-24.56%` | `8,765.50` |
| `Live` | `Long` | `0.2175` | 1,720,000.00 USD | 0.00 USD | 9,880.00 USD | `-24.22%` | `45,406.80` |
| `Live` | `Long` | `0.2185` | 1,710,000.00 USD | 0.00 USD | 153,610.00 USD | `-23.87%` | `703,006.40` |
| `Live` | `Long` | `0.2195` | 1,560,000.00 USD | 0.00 USD | 899.88 USD | `-23.52%` | `4,099.70` |
| `Live` | `Long` | `0.2205` | 1,560,000.00 USD | 0.00 USD | 9,110.00 USD | `-23.17%` | `41,306.20` |
| `Live` | `Long` | `0.2215` | 1,550,000.00 USD | 0.00 USD | 128,040.00 USD | `-22.82%` | `578,059.90` |
| `Live` | `Long` | `0.2245` | 1,420,000.00 USD | 0.00 USD | 5,630.00 USD | `-21.78%` | `25,072.00` |
| `Live` | `Long` | `0.2255` | 1,420,000.00 USD | 0.00 USD | 676.50 USD | `-21.43%` | `3,000.00` |
| `Live` | `Long` | `0.2265` | 1,420,000.00 USD | 0.00 USD | 83,810.00 USD | `-21.08%` | `370,000.00` |
| `Live` | `Long` | `0.2285` | 1,330,000.00 USD | 0.00 USD | 19,240.00 USD | `-20.38%` | `84,190.60` |
| `Live` | `Long` | `0.2295` | 1,310,000.00 USD | 0.00 USD | 160.65 USD | `-20.03%` | `700.00` |
| `Live` | `Long` | `0.2305` | 1,310,000.00 USD | 0.00 USD | 74,180.00 USD | `-19.69%` | `321,829.10` |
| `Live` | `Long` | `0.2315` | 1,240,000.00 USD | 0.00 USD | 5,840.00 USD | `-19.34%` | `25,245.30` |
| `Live` | `Long` | `0.2325` | 1,230,000.00 USD | 0.00 USD | 30,810.00 USD | `-18.99%` | `132,530.50` |
| `Live` | `Long` | `0.2335` | 1,200,000.00 USD | 0.00 USD | 1,940.00 USD | `-18.64%` | `8,326.10` |
| `Live` | `Long` | `0.2345` | 1,200,000.00 USD | 0.00 USD | 336.32 USD | `-18.29%` | `1,434.20` |
| `Live` | `Long` | `0.2355` | 1,200,000.00 USD | 0.00 USD | 10,150.00 USD | `-17.94%` | `43,081.00` |
| `Live` | `Long` | `0.2365` | 1,190,000.00 USD | 0.00 USD | 24,980.00 USD | `-17.60%` | `105,619.90` |
| `Live` | `Long` | `0.2375` | 1,160,000.00 USD | 0.00 USD | 1,050.00 USD | `-17.25%` | `4,438.30` |
| `Live` | `Long` | `0.2385` | 1,160,000.00 USD | 0.00 USD | 91,590.00 USD | `-16.90%` | `384,037.20` |
| `Live` | `Long` | `0.2395` | 1,070,000.00 USD | 0.00 USD | 15,990.00 USD | `-16.55%` | `66,745.60` |
| `Live` | `Long` | `0.2405` | 1,060,000.00 USD | 0.00 USD | 41,930.00 USD | `-16.20%` | `174,328.00` |
| `Live` | `Long` | `0.2415` | 1,010,000.00 USD | 0.00 USD | 32,410.00 USD | `-15.85%` | `134,189.70` |
| `Live` | `Long` | `0.2425` | 981,550.00 USD | 0.00 USD | 399,620.00 USD | `-15.51%` | `1,647,937.20` |
| `Live` | `Long` | `0.2435` | 581,930.00 USD | 0.00 USD | 51,230.00 USD | `-15.16%` | `210,408.30` |
| `Live` | `Long` | `0.2445` | 530,690.00 USD | 0.00 USD | 1,290.00 USD | `-14.81%` | `5,283.30` |
| `Live` | `Long` | `0.2455` | 529,400.00 USD | 0.00 USD | 12,150.00 USD | `-14.46%` | `49,500.00` |
| `Live` | `Long` | `0.2465` | 517,250.00 USD | 0.00 USD | 5,140.00 USD | `-14.11%` | `20,841.30` |
| `Live` | `Long` | `0.2475` | 512,110.00 USD | 0.00 USD | 53,540.00 USD | `-13.76%` | `216,321.70` |
| `Live` | `Long` | `0.2485` | 458,570.00 USD | 0.00 USD | 31,460.00 USD | `-13.41%` | `126,587.90` |
| `Live` | `Long` | `0.2495` | 427,120.00 USD | 0.00 USD | 28,290.00 USD | `-13.07%` | `113,393.90` |
| `Live` | `Long` | `0.2505` | 398,820.00 USD | 0.00 USD | 5,090.00 USD | `-12.72%` | `20,333.10` |
| `Live` | `Long` | `0.2515` | 393,730.00 USD | 0.00 USD | 18,010.00 USD | `-12.37%` | `71,592.20` |
| `Live` | `Long` | `0.2535` | 375,730.00 USD | 0.00 USD | 6,370.00 USD | `-11.67%` | `25,132.30` |
| `Live` | `Long` | `0.2545` | 369,350.00 USD | 0.00 USD | 27,660.00 USD | `-11.32%` | `108,701.80` |
| `Live` | `Long` | `0.2555` | 341,690.00 USD | 0.00 USD | 25,730.00 USD | `-10.98%` | `100,701.70` |
| `Live` | `Long` | `0.2565` | 315,960.00 USD | 0.00 USD | 361.20 USD | `-10.63%` | `1,408.20` |
| `Live` | `Long` | `0.2575` | 315,600.00 USD | 0.00 USD | 60,670.00 USD | `-10.28%` | `235,621.00` |
| `Live` | `Long` | `0.2585` | 254,930.00 USD | 0.00 USD | 29,640.00 USD | `-9.93%` | `114,655.60` |
| `Live` | `Long` | `0.2595` | 225,290.00 USD | 0.00 USD | 101,220.00 USD | `-9.58%` | `390,064.10` |
| `Live` | `Long` | `0.2605` | 124,070.00 USD | 0.00 USD | 89,520.00 USD | `-9.23%` | `343,640.90` |
| `Live` | `Long` | `0.2615` | 34,550.00 USD | 0.00 USD | 9,490.00 USD | `-8.89%` | `36,274.50` |
| `Live` | `Long` | `0.2625` | 25,060.00 USD | 0.00 USD | 342.09 USD | `-8.54%` | `1,303.20` |
| `Live` | `Long` | `0.2635` | 24,720.00 USD | 0.00 USD | 126.69 USD | `-8.19%` | `480.80` |
| `Live` | `Long` | `0.2645` | 24,590.00 USD | 0.00 USD | 1,320.00 USD | `-7.84%` | `5,000.00` |
| `Live` | `Long` | `0.2665` | 23,270.00 USD | 0.00 USD | 345.52 USD | `-7.14%` | `1,296.50` |
| `Live` | `Long` | `0.2675` | 22,930.00 USD | 0.00 USD | 535.00 USD | `-6.79%` | `2,000.00` |
| `Live` | `Long` | `0.2685` | 22,390.00 USD | 0.00 USD | 6,780.00 USD | `-6.45%` | `25,246.20` |
| `Live` | `Long` | `0.2695` | 15,610.00 USD | 0.00 USD | 7,320.00 USD | `-6.10%` | `27,156.50` |
| `Live` | `Long` | `0.2715` | 8,290.00 USD | 0.00 USD | 8,150.00 USD | `-5.40%` | `30,003.20` |
| `Live` | `Long` | `0.2805` | 147.68 USD | 0.00 USD | 147.68 USD | `-2.26%` | `526.50` |
| `Live` | `Short` | `0.2905` | 22,150.00 USD | 22,150.00 USD | 0.00 USD | `+1.22%` | `76,259.70` |
| `Live` | `Short` | `0.2935` | 22,670.00 USD | 515.62 USD | 0.00 USD | `+2.26%` | `1,756.80` |
| `Live` | `Short` | `0.2975` | 23,090.00 USD | 423.94 USD | 0.00 USD | `+3.66%` | `1,425.00` |
| `Live` | `Short` | `0.3005` | 29,030.00 USD | 5,940.00 USD | 0.00 USD | `+4.70%` | `19,754.20` |
| `Live` | `Short` | `0.3015` | 110,250.00 USD | 81,220.00 USD | 0.00 USD | `+5.05%` | `269,397.90` |
| `Live` | `Short` | `0.3215` | 115,640.00 USD | 5,380.00 USD | 0.00 USD | `+12.02%` | `16,745.80` |
| `Live` | `Short` | `0.3235` | 116,380.00 USD | 747.16 USD | 0.00 USD | `+12.72%` | `2,309.60` |
| `Live` | `Short` | `0.3415` | 116,490.00 USD | 105.22 USD | 0.00 USD | `+18.99%` | `308.10` |
| `Live` | `Short` | `0.3425` | 116,590.00 USD | 103.85 USD | 0.00 USD | `+19.34%` | `303.20` |
| `Live` | `Short` | `0.3485` | 117,010.00 USD | 413.95 USD | 0.00 USD | `+21.43%` | `1,187.80` |
| `Live` | `Short` | `0.3575` | 117,110.00 USD | 100.14 USD | 0.00 USD | `+24.56%` | `280.10` |
| `Live` | `Short` | `0.3625` | 119,200.00 USD | 2,100.00 USD | 0.00 USD | `+26.31%` | `5,784.00` |
| `Live` | `Short` | `0.3675` | 121,300.00 USD | 2,100.00 USD | 0.00 USD | `+28.05%` | `5,705.10` |
| `Live` | `Short` | `0.3865` | 121,420.00 USD | 119.35 USD | 0.00 USD | `+34.67%` | `308.80` |
| `Live` | `Short` | `0.3885` | 121,520.00 USD | 103.81 USD | 0.00 USD | `+35.37%` | `267.20` |
| `Live` | `Short` | `0.3965` | 169,100.00 USD | 47,580.00 USD | 0.00 USD | `+38.15%` | `120,000.00` |
| `Live` | `Short` | `0.4025` | 169,340.00 USD | 238.76 USD | 0.00 USD | `+40.24%` | `593.20` |
| `Live` | `Short` | `0.4035` | 169,510.00 USD | 165.84 USD | 0.00 USD | `+40.59%` | `411.00` |
| `Live` | `Short` | `0.4165` | 170,100.00 USD | 587.64 USD | 0.00 USD | `+45.12%` | `1,410.90` |
| `Live` | `Short` | `0.4205` | 171,790.00 USD | 1,700.00 USD | 0.00 USD | `+46.52%` | `4,032.60` |
| `Live` | `Short` | `0.4305` | 485,630.00 USD | 313,830.00 USD | 0.00 USD | `+50.00%` | `729,000.00` |
| `Live` | `Short` | `0.4365` | 487,020.00 USD | 1,400.00 USD | 0.00 USD | `+52.09%` | `3,205.50` |
| `Live` | `Short` | `0.4445` | 487,690.00 USD | 666.75 USD | 0.00 USD | `+54.88%` | `1,500.00` |
| `Live` | `Short` | `0.4555` | 488,710.00 USD | 1,010.00 USD | 0.00 USD | `+58.71%` | `2,227.00` |
| `Live` | `Short` | `0.4585` | 488,920.00 USD | 216.14 USD | 0.00 USD | `+59.76%` | `471.40` |
| `Live` | `Short` | `0.4775` | 513,020.00 USD | 24,100.00 USD | 0.00 USD | `+66.38%` | `50,463.70` |
| `Live` | `Short` | `0.5155` | 513,450.00 USD | 428.28 USD | 0.00 USD | `+79.62%` | `830.80` |
| `Live` | `Short` | `0.5315` | 527,960.00 USD | 14,510.00 USD | 0.00 USD | `+85.19%` | `27,300.00` |
| `Live` | `Short` | `0.5455` | 528,070.00 USD | 108.72 USD | 0.00 USD | `+90.07%` | `199.30` |
| `Live` | `Short` | `0.5565` | 530,920.00 USD | 2,860.00 USD | 0.00 USD | `+93.90%` | `5,135.90` |
| `Live` | `Short` | `0.5605` | 531,470.00 USD | 546.15 USD | 0.00 USD | `+95.30%` | `974.40` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Exchange | Baseline | - | - | - | - | - | - |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-11.14K` | Last 24h: `968.79` | Last 3d: `19.73K` | Last 7d: `53.52K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0234%` | **USDT OKX** | `-0.0224%` |
| **USDT Bybit** | `-0.0204%` | **USDT KuCoin** | `-0.0242%` |
| **USDT MEXC** | `-0.0225%` | **USDT BingX** | `-0.0059%` |
| **USDT Gate** | `-0.0104%` | **USDT Bitget** | `-0.0075%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Multi-TF | Interbank Desk | 50.0% | 50.0% | 1.00 | Normal Balanced Liquidity |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 15m Bar | Interbank Tick Flow | - | - | - | - | - | - | - | - | 0.00% | Balanced Interbank Imbalance |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| Live | 15m | Tape Flow | NEUTRAL | Orderflow balanced at current level | - | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -8,170.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `15m` | -85,170.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30m` | 49,080.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `1h` | 96,600.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `2h` | -18,990.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `4h` | 364,560.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `6h` | 444,860.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `8h` | 447,600.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `12h` | 82,080.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `24h` | -167,830.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1w` | -1,800,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,490,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-8.17K` | 15m=`-85.17K` | 1h=`+96.60K` | 24h=`-167.83K`
* Futures Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
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
  * `2026-10-30 16:35:32 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:32 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:32 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:38:32 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.2570` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.2197` (Risk Distance: `0.0440` pts)
  * +2.5R Take Profit: `0.3670`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.2860` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3233` (Risk Distance: `0.0440` pts)
  * +2.5R Take Profit: `0.1760`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.2893`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
