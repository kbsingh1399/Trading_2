# 🏛️ SOVEREIGN CANDIDATE DOSSIER: CRVUSD
**Canonical Key**: `CRVUSD` | **Broker Instrument**: `CRVUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 11:47:32 IST` (`2026-10-30 06:17:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.2620` | **Live Ask Quote**: `0.2840` | **Mid Price**: `0.2730`
- **Spread Points**: `22.00` | **Spread BPS**: `805.86 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.2721` | VWAP Z-Score: `-1.13` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0048` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `30.66` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3070` | Lower -3.00σ Band: `0.2373`
  * Upper +2.51σ Band: `0.3013` | Lower -2.51σ Band: `0.2430`
  * Upper +2.01σ Band: `0.2955` | Lower -2.01σ Band: `0.2488`
  * Upper +2.00σ Band: `0.2954` | Lower -2.00σ Band: `0.2489`
  * Upper +1.28σ Band: `0.2870` | Lower -1.28σ Band: `0.2573`
  * Upper +1.00σ Band: `0.2837` | Lower -1.00σ Band: `0.2605`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.2619` | EMA-20=`0.2681` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.2835` (Slope: `+0.0000`) | EMA-100=`0.2965`
  * Institutional Anchors: EMA-144=`0.3026` | EMA-200=`0.3077` (Slope: `-1.8603`) | EMA-233=`0.3102`
- **Range Boundaries**: 24H High=`0.3270` | 24H Low=`0.2530` | Weekly High=`0.3340` | Weekly Low=`0.2530`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.2920` (Distance: `-6.20%`)
  * Point of Control (POC) = `0.2630` (Distance: `+3.98%`)
  * Value Area Low (VAL) = `0.2570` (Distance: `+6.46%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3230` | POC=`0.3160` | VAL=`0.3100`
  * Prior Day Extremes: PDH=`0.3330` | PDL=`0.2890` | PDC=`0.2980`
  * Monday Range Blueprint: High=`0.3430` | Mid=`0.3340` | Low=`0.3250`
  * Developing Weekly Value Area: Weekly VAH=`0.3420` | Weekly POC=`0.3280` | Weekly VAL=`0.3150`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3040` | Low=`0.2530`
  * London Session (08:00-16:00 UTC): High=`0.2640` | Low=`0.2570`
  * New York Session (13:00-21:00 UTC): High=`0.2746` | Low=`0.2714`
  * Initial Balance (First Hour): IB High=`0.2640` | IB Low=`0.2580`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.2719` - `0.2741`
  * Optimal Trade Entry (OTE 0.705): `0.2735`
  * Structural Invalidation Anchor (0.786): `0.2752`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:43:56 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1867` | `0x12d2...f97f` | `LONG` | 1,084,820.60 USD | `3,972,828.70` | `0.3272` | `0.2725` | `0.000000` | -215,018.13 USD | `-19.82%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


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
| `Live` | `Long Liquidation` | `0.0585` | 219.49 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 2,400.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 1,190.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 3,330.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 544.78 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 8,160.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 2,330.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 485.44 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 922.84 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 1,140.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 2,000.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 116.35 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 5,810.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 327.14 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 4,300.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 20,400.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 613.05 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 14,050.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 1,130.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 941.69 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 4,770.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 12,380.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 20,300.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 19,500.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 2,500.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 7,600.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 278.30 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 464.68 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 35,390.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 2,020.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 1,340.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 14,270.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1785` | 12,010.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 33,390.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1805` | 15,590.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1825` | 1,670.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1835` | 179.10 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1845` | 21,640.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1865` | 7,460.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 13,340.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1885` | 16,180.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1895` | 12,270.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1905` | 32,820.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1915` | 100.84 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1925` | 8,820.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1935` | 2,440.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1955` | 13,540.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1985` | 1,100.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 3,430.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2015` | 111,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2025` | 3,270.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 19,770.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2055` | 42,160.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2085` | 2,970.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2115` | 55,550.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2125` | 521.03 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2145` | 68,790.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2165` | 3,140.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 13,830.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 153.87 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 8,610.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2215` | 127,020.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 4,540.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 7,870.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2255` | 1,020.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2275` | 79,060.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2285` | 18,820.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 2,690.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 76,590.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 24,760.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 20,660.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 1,940.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 336.32 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 7,070.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 24,590.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 1,170.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 92,510.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2395` | 27,700.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 13,650.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2415` | 27,560.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 401,070.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 42,780.00 USD | 696,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 1,290.00 USD | 654,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 12,150.00 USD | 652,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 5,140.00 USD | 640,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 10,700.00 USD | 635,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 31,460.00 USD | 624,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2495` | 168,010.00 USD | 593,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 113.35 USD | 425,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2535` | 6,370.00 USD | 425,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2545` | 44,410.00 USD | 418,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 51,100.00 USD | 374,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 2,730.00 USD | 323,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2575` | 63,230.00 USD | 320,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 115,440.00 USD | 257,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 43,150.00 USD | 142,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 88,220.00 USD | 98,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 4,460.00 USD | 10,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 4,740.00 USD | 6,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 126.69 USD | 1,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 1,330.00 USD | 1,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2825` | 4,190.00 USD | 4,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2835` | 1,950.00 USD | 6,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2855` | 309.71 USD | 6,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2865` | 18,750.00 USD | 25,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2885` | 402.57 USD | 25,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 525.49 USD | 26,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3215` | 5,380.00 USD | 31,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3405` | 298.07 USD | 31,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3485` | 413.95 USD | 32,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3545` | 446.07 USD | 32,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3575` | 100.14 USD | 32,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 2,100.00 USD | 34,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3675` | 2,100.00 USD | 36,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3855` | 119.04 USD | 37,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3885` | 103.81 USD | 37,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3945` | 47,340.00 USD | 84,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4025` | 238.76 USD | 84,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4035` | 165.84 USD | 84,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4205` | 1,700.00 USD | 86,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4445` | 666.75 USD | 87,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4465` | 325,500.00 USD | 412,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4535` | 1,010.00 USD | 413,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4565` | 1,460.00 USD | 415,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4825` | 24,350.00 USD | 439,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5155` | 428.28 USD | 440,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5315` | 14,510.00 USD | 454,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0585` | 2,370,000.00 USD | 0.00 USD | 219.49 USD | `-78.52%` | `3,752.00` |
| `Live` | `Long` | `0.0595` | 2,370,000.00 USD | 0.00 USD | 2,400.00 USD | `-78.15%` | `40,384.50` |
| `Live` | `Long` | `0.0635` | 2,370,000.00 USD | 0.00 USD | 1,190.00 USD | `-76.68%` | `18,735.40` |
| `Live` | `Long` | `0.0655` | 2,370,000.00 USD | 0.00 USD | 3,330.00 USD | `-75.95%` | `50,846.60` |
| `Live` | `Long` | `0.0725` | 2,370,000.00 USD | 0.00 USD | 544.78 USD | `-73.38%` | `7,514.20` |
| `Live` | `Long` | `0.0765` | 2,370,000.00 USD | 0.00 USD | 8,160.00 USD | `-71.91%` | `106,697.00` |
| `Live` | `Long` | `0.0785` | 2,360,000.00 USD | 0.00 USD | 2,330.00 USD | `-71.17%` | `29,622.60` |
| `Live` | `Long` | `0.0865` | 2,360,000.00 USD | 0.00 USD | 485.44 USD | `-68.24%` | `5,612.00` |
| `Live` | `Long` | `0.0945` | 2,360,000.00 USD | 0.00 USD | 922.84 USD | `-65.30%` | `9,765.50` |
| `Live` | `Long` | `0.0975` | 2,350,000.00 USD | 0.00 USD | 1,140.00 USD | `-64.20%` | `11,739.70` |
| `Live` | `Long` | `0.1185` | 2,350,000.00 USD | 0.00 USD | 2,000.00 USD | `-56.49%` | `16,859.10` |
| `Live` | `Long` | `0.1225` | 2,350,000.00 USD | 0.00 USD | 116.35 USD | `-55.02%` | `949.80` |
| `Live` | `Long` | `0.1235` | 2,350,000.00 USD | 0.00 USD | 5,810.00 USD | `-54.65%` | `47,058.80` |
| `Live` | `Long` | `0.1245` | 2,350,000.00 USD | 0.00 USD | 327.14 USD | `-54.28%` | `2,627.60` |
| `Live` | `Long` | `0.1255` | 2,350,000.00 USD | 0.00 USD | 4,300.00 USD | `-53.91%` | `34,264.40` |
| `Live` | `Long` | `0.1275` | 2,340,000.00 USD | 0.00 USD | 20,400.00 USD | `-53.18%` | `160,000.00` |
| `Live` | `Long` | `0.1285` | 2,320,000.00 USD | 0.00 USD | 613.05 USD | `-52.81%` | `4,770.80` |
| `Live` | `Long` | `0.1405` | 2,320,000.00 USD | 0.00 USD | 14,050.00 USD | `-48.41%` | `100,000.00` |
| `Live` | `Long` | `0.1415` | 2,310,000.00 USD | 0.00 USD | 1,130.00 USD | `-48.04%` | `8,000.00` |
| `Live` | `Long` | `0.1435` | 2,310,000.00 USD | 0.00 USD | 941.69 USD | `-47.30%` | `6,562.30` |
| `Live` | `Long` | `0.1445` | 2,300,000.00 USD | 0.00 USD | 4,770.00 USD | `-46.94%` | `33,042.60` |
| `Live` | `Long` | `0.1465` | 2,300,000.00 USD | 0.00 USD | 12,380.00 USD | `-46.20%` | `84,498.00` |
| `Live` | `Long` | `0.1535` | 2,290,000.00 USD | 0.00 USD | 20,300.00 USD | `-43.63%` | `132,229.20` |
| `Live` | `Long` | `0.1625` | 2,270,000.00 USD | 0.00 USD | 19,500.00 USD | `-40.33%` | `120,000.00` |
| `Live` | `Long` | `0.1645` | 2,250,000.00 USD | 0.00 USD | 2,500.00 USD | `-39.59%` | `15,205.80` |
| `Live` | `Long` | `0.1665` | 2,240,000.00 USD | 0.00 USD | 7,600.00 USD | `-38.86%` | `45,616.80` |
| `Live` | `Long` | `0.1695` | 2,240,000.00 USD | 0.00 USD | 278.30 USD | `-37.76%` | `1,641.90` |
| `Live` | `Long` | `0.1715` | 2,240,000.00 USD | 0.00 USD | 464.68 USD | `-37.02%` | `2,709.50` |
| `Live` | `Long` | `0.1725` | 2,240,000.00 USD | 0.00 USD | 35,390.00 USD | `-36.66%` | `205,143.90` |
| `Live` | `Long` | `0.1735` | 2,200,000.00 USD | 0.00 USD | 2,020.00 USD | `-36.29%` | `11,641.60` |
| `Live` | `Long` | `0.1765` | 2,200,000.00 USD | 0.00 USD | 1,340.00 USD | `-35.19%` | `7,607.60` |
| `Live` | `Long` | `0.1775` | 2,200,000.00 USD | 0.00 USD | 14,270.00 USD | `-34.82%` | `80,391.40` |
| `Live` | `Long` | `0.1785` | 2,180,000.00 USD | 0.00 USD | 12,010.00 USD | `-34.45%` | `67,270.30` |
| `Live` | `Long` | `0.1795` | 2,170,000.00 USD | 0.00 USD | 33,390.00 USD | `-34.08%` | `186,041.70` |
| `Live` | `Long` | `0.1805` | 2,140,000.00 USD | 0.00 USD | 15,590.00 USD | `-33.72%` | `86,371.80` |
| `Live` | `Long` | `0.1825` | 2,120,000.00 USD | 0.00 USD | 1,670.00 USD | `-32.98%` | `9,160.60` |
| `Live` | `Long` | `0.1835` | 2,120,000.00 USD | 0.00 USD | 179.10 USD | `-32.62%` | `976.00` |
| `Live` | `Long` | `0.1845` | 2,120,000.00 USD | 0.00 USD | 21,640.00 USD | `-32.25%` | `117,269.40` |
| `Live` | `Long` | `0.1865` | 2,100,000.00 USD | 0.00 USD | 7,460.00 USD | `-31.51%` | `40,000.00` |
| `Live` | `Long` | `0.1875` | 2,090,000.00 USD | 0.00 USD | 13,340.00 USD | `-31.15%` | `71,135.10` |
| `Live` | `Long` | `0.1885` | 2,080,000.00 USD | 0.00 USD | 16,180.00 USD | `-30.78%` | `85,829.20` |
| `Live` | `Long` | `0.1895` | 2,060,000.00 USD | 0.00 USD | 12,270.00 USD | `-30.41%` | `64,758.40` |
| `Live` | `Long` | `0.1905` | 2,050,000.00 USD | 0.00 USD | 32,820.00 USD | `-30.05%` | `172,299.70` |
| `Live` | `Long` | `0.1915` | 2,020,000.00 USD | 0.00 USD | 100.84 USD | `-29.68%` | `526.60` |
| `Live` | `Long` | `0.1925` | 2,020,000.00 USD | 0.00 USD | 8,820.00 USD | `-29.31%` | `45,821.40` |
| `Live` | `Long` | `0.1935` | 2,010,000.00 USD | 0.00 USD | 2,440.00 USD | `-28.94%` | `12,592.40` |
| `Live` | `Long` | `0.1955` | 2,010,000.00 USD | 0.00 USD | 13,540.00 USD | `-28.21%` | `69,252.60` |
| `Live` | `Long` | `0.1985` | 1,990,000.00 USD | 0.00 USD | 1,100.00 USD | `-27.11%` | `5,563.00` |
| `Live` | `Long` | `0.1995` | 1,990,000.00 USD | 0.00 USD | 3,430.00 USD | `-26.74%` | `17,199.40` |
| `Live` | `Long` | `0.2015` | 1,990,000.00 USD | 0.00 USD | 111,000.00 USD | `-26.01%` | `550,886.10` |
| `Live` | `Long` | `0.2025` | 1,880,000.00 USD | 0.00 USD | 3,270.00 USD | `-25.64%` | `16,132.50` |
| `Live` | `Long` | `0.2045` | 1,870,000.00 USD | 0.00 USD | 19,770.00 USD | `-24.90%` | `96,680.20` |
| `Live` | `Long` | `0.2055` | 1,850,000.00 USD | 0.00 USD | 42,160.00 USD | `-24.54%` | `205,147.80` |
| `Live` | `Long` | `0.2085` | 1,810,000.00 USD | 0.00 USD | 2,970.00 USD | `-23.44%` | `14,230.20` |
| `Live` | `Long` | `0.2115` | 1,810,000.00 USD | 0.00 USD | 55,550.00 USD | `-22.33%` | `262,635.40` |
| `Live` | `Long` | `0.2125` | 1,750,000.00 USD | 0.00 USD | 521.03 USD | `-21.97%` | `2,451.90` |
| `Live` | `Long` | `0.2145` | 1,750,000.00 USD | 0.00 USD | 68,790.00 USD | `-21.23%` | `320,696.20` |
| `Live` | `Long` | `0.2165` | 1,680,000.00 USD | 0.00 USD | 3,140.00 USD | `-20.50%` | `14,516.00` |
| `Live` | `Long` | `0.2175` | 1,680,000.00 USD | 0.00 USD | 13,830.00 USD | `-20.13%` | `63,568.40` |
| `Live` | `Long` | `0.2195` | 1,670,000.00 USD | 0.00 USD | 153.87 USD | `-19.40%` | `701.00` |
| `Live` | `Long` | `0.2205` | 1,670,000.00 USD | 0.00 USD | 8,610.00 USD | `-19.03%` | `39,028.70` |
| `Live` | `Long` | `0.2215` | 1,660,000.00 USD | 0.00 USD | 127,020.00 USD | `-18.66%` | `573,439.00` |
| `Live` | `Long` | `0.2225` | 1,530,000.00 USD | 0.00 USD | 4,540.00 USD | `-18.29%` | `20,384.10` |
| `Live` | `Long` | `0.2245` | 1,530,000.00 USD | 0.00 USD | 7,870.00 USD | `-17.56%` | `35,072.00` |
| `Live` | `Long` | `0.2255` | 1,520,000.00 USD | 0.00 USD | 1,020.00 USD | `-17.19%` | `4,510.70` |
| `Live` | `Long` | `0.2275` | 1,520,000.00 USD | 0.00 USD | 79,060.00 USD | `-16.46%` | `347,527.40` |
| `Live` | `Long` | `0.2285` | 1,440,000.00 USD | 0.00 USD | 18,820.00 USD | `-16.09%` | `82,342.00` |
| `Live` | `Long` | `0.2295` | 1,420,000.00 USD | 0.00 USD | 2,690.00 USD | `-15.72%` | `11,727.30` |
| `Live` | `Long` | `0.2305` | 1,420,000.00 USD | 0.00 USD | 76,590.00 USD | `-15.36%` | `332,256.90` |
| `Live` | `Long` | `0.2315` | 1,340,000.00 USD | 0.00 USD | 24,760.00 USD | `-14.99%` | `106,949.50` |
| `Live` | `Long` | `0.2325` | 1,320,000.00 USD | 0.00 USD | 20,660.00 USD | `-14.62%` | `88,851.00` |
| `Live` | `Long` | `0.2335` | 1,290,000.00 USD | 0.00 USD | 1,940.00 USD | `-14.26%` | `8,326.10` |
| `Live` | `Long` | `0.2345` | 1,290,000.00 USD | 0.00 USD | 336.32 USD | `-13.89%` | `1,434.20` |
| `Live` | `Long` | `0.2355` | 1,290,000.00 USD | 0.00 USD | 7,070.00 USD | `-13.52%` | `30,000.00` |
| `Live` | `Long` | `0.2365` | 1,290,000.00 USD | 0.00 USD | 24,590.00 USD | `-13.15%` | `103,980.90` |
| `Live` | `Long` | `0.2375` | 1,260,000.00 USD | 0.00 USD | 1,170.00 USD | `-12.79%` | `4,929.00` |
| `Live` | `Long` | `0.2385` | 1,260,000.00 USD | 0.00 USD | 92,510.00 USD | `-12.42%` | `387,884.40` |
| `Live` | `Long` | `0.2395` | 1,170,000.00 USD | 0.00 USD | 27,700.00 USD | `-12.05%` | `115,638.00` |
| `Live` | `Long` | `0.2405` | 1,140,000.00 USD | 0.00 USD | 13,650.00 USD | `-11.68%` | `56,745.50` |
| `Live` | `Long` | `0.2415` | 1,130,000.00 USD | 0.00 USD | 27,560.00 USD | `-11.32%` | `114,135.40` |
| `Live` | `Long` | `0.2425` | 1,100,000.00 USD | 0.00 USD | 401,070.00 USD | `-10.95%` | `1,653,886.80` |
| `Live` | `Long` | `0.2435` | 696,940.00 USD | 0.00 USD | 42,780.00 USD | `-10.58%` | `175,685.10` |
| `Live` | `Long` | `0.2445` | 654,160.00 USD | 0.00 USD | 1,290.00 USD | `-10.22%` | `5,283.30` |
| `Live` | `Long` | `0.2455` | 652,860.00 USD | 0.00 USD | 12,150.00 USD | `-9.85%` | `49,500.00` |
| `Live` | `Long` | `0.2465` | 640,710.00 USD | 0.00 USD | 5,140.00 USD | `-9.48%` | `20,841.30` |
| `Live` | `Long` | `0.2475` | 635,570.00 USD | 0.00 USD | 10,700.00 USD | `-9.11%` | `43,223.20` |
| `Live` | `Long` | `0.2485` | 624,880.00 USD | 0.00 USD | 31,460.00 USD | `-8.75%` | `126,587.90` |
| `Live` | `Long` | `0.2495` | 593,420.00 USD | 0.00 USD | 168,010.00 USD | `-8.38%` | `673,393.90` |
| `Live` | `Long` | `0.2505` | 425,410.00 USD | 0.00 USD | 113.35 USD | `-8.01%` | `452.50` |
| `Live` | `Long` | `0.2535` | 425,290.00 USD | 0.00 USD | 6,370.00 USD | `-6.91%` | `25,132.30` |
| `Live` | `Long` | `0.2545` | 418,920.00 USD | 0.00 USD | 44,410.00 USD | `-6.54%` | `174,480.30` |
| `Live` | `Long` | `0.2555` | 374,520.00 USD | 0.00 USD | 51,100.00 USD | `-6.18%` | `199,996.80` |
| `Live` | `Long` | `0.2565` | 323,420.00 USD | 0.00 USD | 2,730.00 USD | `-5.81%` | `10,630.50` |
| `Live` | `Long` | `0.2575` | 320,690.00 USD | 0.00 USD | 63,230.00 USD | `-5.44%` | `245,562.80` |
| `Live` | `Long` | `0.2585` | 257,460.00 USD | 0.00 USD | 115,440.00 USD | `-5.07%` | `446,590.30` |
| `Live` | `Long` | `0.2595` | 142,020.00 USD | 0.00 USD | 43,150.00 USD | `-4.71%` | `166,271.70` |
| `Live` | `Long` | `0.2605` | 98,870.00 USD | 0.00 USD | 88,220.00 USD | `-4.34%` | `338,637.40` |
| `Live` | `Long` | `0.2615` | 10,650.00 USD | 0.00 USD | 4,460.00 USD | `-3.97%` | `17,053.00` |
| `Live` | `Long` | `0.2625` | 6,190.00 USD | 0.00 USD | 4,740.00 USD | `-3.61%` | `18,059.70` |
| `Live` | `Long` | `0.2635` | 1,450.00 USD | 0.00 USD | 126.69 USD | `-3.24%` | `480.80` |
| `Live` | `Long` | `0.2655` | 1,330.00 USD | 0.00 USD | 1,330.00 USD | `-2.50%` | `5,000.00` |
| `Live` | `Short` | `0.2825` | 4,190.00 USD | 4,190.00 USD | 0.00 USD | `+3.74%` | `14,827.70` |
| `Live` | `Short` | `0.2835` | 6,140.00 USD | 1,950.00 USD | 0.00 USD | `+4.11%` | `6,884.00` |
| `Live` | `Short` | `0.2855` | 6,450.00 USD | 309.71 USD | 0.00 USD | `+4.84%` | `1,084.80` |
| `Live` | `Short` | `0.2865` | 25,200.00 USD | 18,750.00 USD | 0.00 USD | `+5.21%` | `65,448.90` |
| `Live` | `Short` | `0.2885` | 25,600.00 USD | 402.57 USD | 0.00 USD | `+5.94%` | `1,395.40` |
| `Live` | `Short` | `0.2915` | 26,130.00 USD | 525.49 USD | 0.00 USD | `+7.04%` | `1,802.70` |
| `Live` | `Short` | `0.3215` | 31,510.00 USD | 5,380.00 USD | 0.00 USD | `+18.06%` | `16,745.80` |
| `Live` | `Short` | `0.3405` | 31,810.00 USD | 298.07 USD | 0.00 USD | `+25.04%` | `875.40` |
| `Live` | `Short` | `0.3485` | 32,230.00 USD | 413.95 USD | 0.00 USD | `+27.97%` | `1,187.80` |
| `Live` | `Short` | `0.3545` | 32,670.00 USD | 446.07 USD | 0.00 USD | `+30.18%` | `1,258.30` |
| `Live` | `Short` | `0.3575` | 32,770.00 USD | 100.14 USD | 0.00 USD | `+31.28%` | `280.10` |
| `Live` | `Short` | `0.3625` | 34,870.00 USD | 2,100.00 USD | 0.00 USD | `+33.12%` | `5,784.00` |
| `Live` | `Short` | `0.3675` | 36,960.00 USD | 2,100.00 USD | 0.00 USD | `+34.95%` | `5,705.10` |
| `Live` | `Short` | `0.3855` | 37,080.00 USD | 119.04 USD | 0.00 USD | `+41.56%` | `308.80` |
| `Live` | `Short` | `0.3885` | 37,190.00 USD | 103.81 USD | 0.00 USD | `+42.66%` | `267.20` |
| `Live` | `Short` | `0.3945` | 84,530.00 USD | 47,340.00 USD | 0.00 USD | `+44.87%` | `120,000.00` |
| `Live` | `Short` | `0.4025` | 84,770.00 USD | 238.76 USD | 0.00 USD | `+47.80%` | `593.20` |
| `Live` | `Short` | `0.4035` | 84,930.00 USD | 165.84 USD | 0.00 USD | `+48.17%` | `411.00` |
| `Live` | `Short` | `0.4205` | 86,630.00 USD | 1,700.00 USD | 0.00 USD | `+54.41%` | `4,032.60` |
| `Live` | `Short` | `0.4445` | 87,290.00 USD | 666.75 USD | 0.00 USD | `+63.23%` | `1,500.00` |
| `Live` | `Short` | `0.4465` | 412,790.00 USD | 325,500.00 USD | 0.00 USD | `+63.96%` | `729,000.00` |
| `Live` | `Short` | `0.4535` | 413,800.00 USD | 1,010.00 USD | 0.00 USD | `+66.53%` | `2,227.00` |
| `Live` | `Short` | `0.4565` | 415,270.00 USD | 1,460.00 USD | 0.00 USD | `+67.63%` | `3,205.50` |
| `Live` | `Short` | `0.4825` | 439,620.00 USD | 24,350.00 USD | 0.00 USD | `+77.18%` | `50,463.70` |
| `Live` | `Short` | `0.5155` | 440,040.00 USD | 428.28 USD | 0.00 USD | `+89.30%` | `830.80` |
| `Live` | `Short` | `0.5315` | 454,550.00 USD | 14,510.00 USD | 0.00 USD | `+95.17%` | `27,300.00` |

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
  * Current Rate: `-3.48K` | Last 24h: `9.20K` | Last 3d: `30.42K` | Last 7d: `57.33K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0019%` | **USDT OKX** | `-0.0101%` |
| **USDT Bybit** | `-0.0132%` | **USDT KuCoin** | `-0.0372%` |
| **USDT MEXC** | `-0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0005%` | **USDT Bitget** | `0.0100%` |
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
| `5m` | 10,130.00 USD | 27,940.00 USD | **`ACCUMULATION`** |
| `15m` | 56,540.00 USD | -224,200.00 USD | **`DISTRIBUTION`** |
| `30m` | 116,560.00 USD | -276,480.00 USD | **`DISTRIBUTION`** |
| `1h` | 66,180.00 USD | -100,140.00 USD | **`DISTRIBUTION`** |
| `2h` | 40,000.00 USD | -201,410.00 USD | **`DISTRIBUTION`** |
| `4h` | 303,410.00 USD | 207,020.00 USD | **`ACCUMULATION`** |
| `6h` | -325,930.00 USD | -5,350,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -221,290.00 USD | -6,460,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -565,270.00 USD | -9,380,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -698,670.00 USD | -11,910,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -2,090,000.00 USD | -23,780,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -15,040,000.00 USD | -67,050,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+10.13K` | 15m=`+56.54K` | 1h=`+66.18K` | 24h=`-698.67K`
* Futures Capital Netflows: 5m=`+27.94K` | 15m=`-224.20K` | 1h=`-100.14K` | 24h=`-11.91M`
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
  * `2026-10-30 11:03:46 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:38:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:37:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:39:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `0.2183` (Risk Distance: `0.0440` pts)
  * +2.5R Take Profit: `0.3670`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.2920` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3307` (Risk Distance: `0.0440` pts)
  * +2.5R Take Profit: `0.1820`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.2752`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
