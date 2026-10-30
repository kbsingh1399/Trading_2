# 🏛️ SOVEREIGN CANDIDATE DOSSIER: CRVUSD
**Canonical Key**: `CRVUSD` | **Broker Instrument**: `CRVUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 14:41:48 IST` (`2026-10-30 09:11:48 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.2720` | **Live Ask Quote**: `0.2940` | **Mid Price**: `0.2830`
- **Spread Points**: `22.00` | **Spread BPS**: `777.39 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.2830` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.2850` | Lower -3.00σ Band: `0.2810`
  * Upper +2.51σ Band: `0.2846` | Lower -2.51σ Band: `0.2814`
  * Upper +2.01σ Band: `0.2842` | Lower -2.01σ Band: `0.2818`
  * Upper +2.00σ Band: `0.2841` | Lower -2.00σ Band: `0.2819`
  * Upper +1.28σ Band: `0.2838` | Lower -1.28σ Band: `0.2822`
  * Upper +1.00σ Band: `0.2836` | Lower -1.00σ Band: `0.2824`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.2830` | EMA-20=`0.2830` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.2830` (Slope: `+0.0000`) | EMA-100=`0.2830`
  * Institutional Anchors: EMA-144=`0.2830` | EMA-200=`0.2830` (Slope: `+0.0000`) | EMA-233=`0.2830`
- **Range Boundaries**: 24H High=`0.2858` | 24H Low=`0.2802` | Weekly High=`0.2887` | Weekly Low=`0.2773`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.2880` (Distance: `-1.63%`)
  * Point of Control (POC) = `0.2630` (Distance: `+7.78%`)
  * Value Area Low (VAL) = `0.2570` (Distance: `+10.35%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3230` | POC=`0.3160` | VAL=`0.3100`
  * Prior Day Extremes: PDH=`0.3330` | PDL=`0.2890` | PDC=`0.2980`
  * Monday Range Blueprint: High=`0.3430` | Mid=`0.3340` | Low=`0.3250`
  * Developing Weekly Value Area: Weekly VAH=`0.3420` | Weekly POC=`0.3280` | Weekly VAL=`0.3130`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3040` | Low=`0.2530`
  * London Session (08:00-16:00 UTC): High=`0.2750` | Low=`0.2570`
  * New York Session (13:00-21:00 UTC): High=`0.2847` | Low=`0.2813`
  * Initial Balance (First Hour): IB High=`0.2640` | IB Low=`0.2580`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.2819` - `0.2841`
  * Optimal Trade Entry (OTE 0.705): `0.2836`
  * Structural Invalidation Anchor (0.786): `0.2853`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:32:27 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1834` | `0x12d2...f97f` | `LONG` | 1,128,919.00 USD | `3,972,828.70` | `0.3272` | `0.2843` | `0.000000` | -170,919.74 USD | `-15.14%` | `10X Cross` |

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
| `Live` | `Long Liquidation` | `0.0575` | 129.20 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 219.49 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 2,240.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 2,640.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 116.27 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 374.44 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 3,840.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 13,880.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 2,350.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 9,710.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 687.55 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 460.38 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 1,080.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 1,380.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 7,770.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 116.35 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 4,300.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 335.02 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1365` | 21,840.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 6,200.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 1,160.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 12,380.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1495` | 1,200.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1545` | 3,860.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 21,090.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 19,500.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 2,500.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 4,930.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 278.30 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 33,220.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 5,200.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 3,990.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 136.98 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 1,340.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 14,130.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1785` | 12,010.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 5,890.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1805` | 14,020.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1815` | 27,810.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1825` | 16,120.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1835` | 179.10 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1845` | 25,400.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 5,840.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1885` | 1,660.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1895` | 1,050.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1905` | 39,050.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1925` | 3,050.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1935` | 2,600.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1945` | 6,140.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1955` | 13,830.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1975` | 7,900.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1985` | 1,100.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 3,430.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2015` | 119,060.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 18,550.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2065` | 1,040.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2075` | 41,500.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2085` | 3,330.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2095` | 70,590.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2115` | 55,550.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2125` | 1,240.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2145` | 68,790.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2165` | 6,720.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 9,060.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 899.88 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 8,750.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2215` | 128,040.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 7,870.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2255` | 676.50 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2285` | 19,240.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 160.65 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 74,180.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 25,460.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 11,400.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 1,940.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 336.32 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 20,670.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 25,230.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 5,610.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 92,430.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2395` | 3,620.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 37,700.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2415` | 32,410.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 108,620.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 45,960.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 123,540.00 USD | 986,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 306,750.00 USD | 862,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 5,140.00 USD | 555,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 10,700.00 USD | 550,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 74,760.00 USD | 540,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2495` | 28,290.00 USD | 465,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 113.35 USD | 436,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2515` | 18,010.00 USD | 436,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2535` | 6,370.00 USD | 418,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2545` | 56,730.00 USD | 412,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 48,600.00 USD | 355,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 1,640.00 USD | 307,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2575` | 60,880.00 USD | 305,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 29,970.00 USD | 244,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 101,500.00 USD | 214,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 92,800.00 USD | 113,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 6,160.00 USD | 20,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 342.09 USD | 14,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 126.69 USD | 13,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 3,030.00 USD | 13,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2695` | 9,840.00 USD | 10,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 863.38 USD | 863.38 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2965` | 384.41 USD | 384.41 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2975` | 5,500.00 USD | 5,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3035` | 16,220.00 USD | 22,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3065` | 1,120.00 USD | 23,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3215` | 5,380.00 USD | 28,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3235` | 747.16 USD | 29,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3415` | 103.54 USD | 29,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3485` | 413.95 USD | 29,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3575` | 100.14 USD | 29,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 2,100.00 USD | 32,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3675` | 2,100.00 USD | 34,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3865` | 119.35 USD | 34,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3885` | 103.81 USD | 34,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3965` | 47,580.00 USD | 81,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4025` | 238.76 USD | 82,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4035` | 165.84 USD | 82,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4205` | 1,700.00 USD | 84,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4385` | 319,670.00 USD | 403,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4445` | 666.75 USD | 404,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4515` | 212.84 USD | 404,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4525` | 1,450.00 USD | 406,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4565` | 1,020.00 USD | 407,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4725` | 23,840.00 USD | 430,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5085` | 120.62 USD | 431,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5155` | 428.28 USD | 431,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5315` | 14,510.00 USD | 445,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5455` | 108.72 USD | 446,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5565` | 2,860.00 USD | 448,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0575` | 2,420,000.00 USD | 0.00 USD | 129.20 USD | `-79.65%` | `2,246.90` |
| `Live` | `Long` | `0.0585` | 2,420,000.00 USD | 0.00 USD | 219.49 USD | `-79.30%` | `3,752.00` |
| `Live` | `Long` | `0.0665` | 2,420,000.00 USD | 0.00 USD | 2,240.00 USD | `-76.47%` | `33,687.90` |
| `Live` | `Long` | `0.0685` | 2,420,000.00 USD | 0.00 USD | 2,640.00 USD | `-75.76%` | `38,602.60` |
| `Live` | `Long` | `0.0735` | 2,420,000.00 USD | 0.00 USD | 116.27 USD | `-73.99%` | `1,581.90` |
| `Live` | `Long` | `0.0745` | 2,420,000.00 USD | 0.00 USD | 374.44 USD | `-73.64%` | `5,026.00` |
| `Live` | `Long` | `0.0755` | 2,420,000.00 USD | 0.00 USD | 3,840.00 USD | `-73.28%` | `50,846.60` |
| `Live` | `Long` | `0.0765` | 2,410,000.00 USD | 0.00 USD | 13,880.00 USD | `-72.93%` | `181,411.80` |
| `Live` | `Long` | `0.0795` | 2,400,000.00 USD | 0.00 USD | 2,350.00 USD | `-71.87%` | `29,622.60` |
| `Live` | `Long` | `0.0865` | 2,400,000.00 USD | 0.00 USD | 9,710.00 USD | `-69.39%` | `112,309.00` |
| `Live` | `Long` | `0.0915` | 2,390,000.00 USD | 0.00 USD | 687.55 USD | `-67.62%` | `7,514.20` |
| `Live` | `Long` | `0.0965` | 2,390,000.00 USD | 0.00 USD | 460.38 USD | `-65.85%` | `4,770.80` |
| `Live` | `Long` | `0.1105` | 2,390,000.00 USD | 0.00 USD | 1,080.00 USD | `-60.90%` | `9,765.50` |
| `Live` | `Long` | `0.1175` | 2,390,000.00 USD | 0.00 USD | 1,380.00 USD | `-58.42%` | `11,739.70` |
| `Live` | `Long` | `0.1215` | 2,390,000.00 USD | 0.00 USD | 7,770.00 USD | `-57.00%` | `63,917.90` |
| `Live` | `Long` | `0.1225` | 2,380,000.00 USD | 0.00 USD | 116.35 USD | `-56.65%` | `949.80` |
| `Live` | `Long` | `0.1255` | 2,380,000.00 USD | 0.00 USD | 4,300.00 USD | `-55.59%` | `34,264.40` |
| `Live` | `Long` | `0.1275` | 2,370,000.00 USD | 0.00 USD | 335.02 USD | `-54.88%` | `2,627.60` |
| `Live` | `Long` | `0.1365` | 2,370,000.00 USD | 0.00 USD | 21,840.00 USD | `-51.70%` | `160,000.00` |
| `Live` | `Long` | `0.1435` | 2,350,000.00 USD | 0.00 USD | 6,200.00 USD | `-49.22%` | `43,210.20` |
| `Live` | `Long` | `0.1455` | 2,340,000.00 USD | 0.00 USD | 1,160.00 USD | `-48.51%` | `8,000.00` |
| `Live` | `Long` | `0.1465` | 2,340,000.00 USD | 0.00 USD | 12,380.00 USD | `-48.16%` | `84,498.00` |
| `Live` | `Long` | `0.1495` | 2,330,000.00 USD | 0.00 USD | 1,200.00 USD | `-47.09%` | `8,042.60` |
| `Live` | `Long` | `0.1545` | 2,330,000.00 USD | 0.00 USD | 3,860.00 USD | `-45.33%` | `25,000.00` |
| `Live` | `Long` | `0.1595` | 2,330,000.00 USD | 0.00 USD | 21,090.00 USD | `-43.56%` | `132,229.20` |
| `Live` | `Long` | `0.1625` | 2,310,000.00 USD | 0.00 USD | 19,500.00 USD | `-42.49%` | `120,000.00` |
| `Live` | `Long` | `0.1645` | 2,290,000.00 USD | 0.00 USD | 2,500.00 USD | `-41.79%` | `15,205.80` |
| `Live` | `Long` | `0.1665` | 2,280,000.00 USD | 0.00 USD | 4,930.00 USD | `-41.08%` | `29,616.80` |
| `Live` | `Long` | `0.1695` | 2,280,000.00 USD | 0.00 USD | 278.30 USD | `-40.02%` | `1,641.90` |
| `Live` | `Long` | `0.1715` | 2,280,000.00 USD | 0.00 USD | 33,220.00 USD | `-39.31%` | `193,709.50` |
| `Live` | `Long` | `0.1725` | 2,240,000.00 USD | 0.00 USD | 5,200.00 USD | `-38.96%` | `30,143.90` |
| `Live` | `Long` | `0.1735` | 2,240,000.00 USD | 0.00 USD | 3,990.00 USD | `-38.60%` | `22,973.90` |
| `Live` | `Long` | `0.1755` | 2,240,000.00 USD | 0.00 USD | 136.98 USD | `-37.89%` | `780.50` |
| `Live` | `Long` | `0.1765` | 2,240,000.00 USD | 0.00 USD | 1,340.00 USD | `-37.54%` | `7,607.60` |
| `Live` | `Long` | `0.1775` | 2,230,000.00 USD | 0.00 USD | 14,130.00 USD | `-37.19%` | `79,610.90` |
| `Live` | `Long` | `0.1785` | 2,220,000.00 USD | 0.00 USD | 12,010.00 USD | `-36.83%` | `67,270.30` |
| `Live` | `Long` | `0.1795` | 2,210,000.00 USD | 0.00 USD | 5,890.00 USD | `-36.48%` | `32,795.10` |
| `Live` | `Long` | `0.1805` | 2,200,000.00 USD | 0.00 USD | 14,020.00 USD | `-36.12%` | `77,683.60` |
| `Live` | `Long` | `0.1815` | 2,190,000.00 USD | 0.00 USD | 27,810.00 USD | `-35.77%` | `153,246.60` |
| `Live` | `Long` | `0.1825` | 2,160,000.00 USD | 0.00 USD | 16,120.00 USD | `-35.42%` | `88,308.30` |
| `Live` | `Long` | `0.1835` | 2,140,000.00 USD | 0.00 USD | 179.10 USD | `-35.06%` | `976.00` |
| `Live` | `Long` | `0.1845` | 2,140,000.00 USD | 0.00 USD | 25,400.00 USD | `-34.71%` | `137,653.50` |
| `Live` | `Long` | `0.1875` | 2,120,000.00 USD | 0.00 USD | 5,840.00 USD | `-33.65%` | `31,135.10` |
| `Live` | `Long` | `0.1885` | 2,110,000.00 USD | 0.00 USD | 1,660.00 USD | `-33.29%` | `8,802.20` |
| `Live` | `Long` | `0.1895` | 2,110,000.00 USD | 0.00 USD | 1,050.00 USD | `-32.94%` | `5,539.20` |
| `Live` | `Long` | `0.1905` | 2,110,000.00 USD | 0.00 USD | 39,050.00 USD | `-32.59%` | `205,000.00` |
| `Live` | `Long` | `0.1925` | 2,070,000.00 USD | 0.00 USD | 3,050.00 USD | `-31.88%` | `15,821.40` |
| `Live` | `Long` | `0.1935` | 2,070,000.00 USD | 0.00 USD | 2,600.00 USD | `-31.52%` | `13,453.50` |
| `Live` | `Long` | `0.1945` | 2,070,000.00 USD | 0.00 USD | 6,140.00 USD | `-31.17%` | `31,561.00` |
| `Live` | `Long` | `0.1955` | 2,060,000.00 USD | 0.00 USD | 13,830.00 USD | `-30.82%` | `70,734.60` |
| `Live` | `Long` | `0.1975` | 2,050,000.00 USD | 0.00 USD | 7,900.00 USD | `-30.11%` | `40,000.00` |
| `Live` | `Long` | `0.1985` | 2,040,000.00 USD | 0.00 USD | 1,100.00 USD | `-29.75%` | `5,563.00` |
| `Live` | `Long` | `0.1995` | 2,040,000.00 USD | 0.00 USD | 3,430.00 USD | `-29.40%` | `17,199.40` |
| `Live` | `Long` | `0.2015` | 2,030,000.00 USD | 0.00 USD | 119,060.00 USD | `-28.69%` | `590,886.10` |
| `Live` | `Long` | `0.2045` | 1,910,000.00 USD | 0.00 USD | 18,550.00 USD | `-27.63%` | `90,714.00` |
| `Live` | `Long` | `0.2065` | 1,900,000.00 USD | 0.00 USD | 1,040.00 USD | `-26.92%` | `5,050.00` |
| `Live` | `Long` | `0.2075` | 1,890,000.00 USD | 0.00 USD | 41,500.00 USD | `-26.57%` | `200,000.00` |
| `Live` | `Long` | `0.2085` | 1,850,000.00 USD | 0.00 USD | 3,330.00 USD | `-26.22%` | `15,982.60` |
| `Live` | `Long` | `0.2095` | 1,850,000.00 USD | 0.00 USD | 70,590.00 USD | `-25.86%` | `336,947.40` |
| `Live` | `Long` | `0.2115` | 1,780,000.00 USD | 0.00 USD | 55,550.00 USD | `-25.15%` | `262,635.40` |
| `Live` | `Long` | `0.2125` | 1,720,000.00 USD | 0.00 USD | 1,240.00 USD | `-24.80%` | `5,840.90` |
| `Live` | `Long` | `0.2145` | 1,720,000.00 USD | 0.00 USD | 68,790.00 USD | `-24.09%` | `320,696.20` |
| `Live` | `Long` | `0.2165` | 1,650,000.00 USD | 0.00 USD | 6,720.00 USD | `-23.38%` | `31,044.10` |
| `Live` | `Long` | `0.2175` | 1,650,000.00 USD | 0.00 USD | 9,060.00 USD | `-23.03%` | `41,666.50` |
| `Live` | `Long` | `0.2195` | 1,640,000.00 USD | 0.00 USD | 899.88 USD | `-22.32%` | `4,099.70` |
| `Live` | `Long` | `0.2205` | 1,640,000.00 USD | 0.00 USD | 8,750.00 USD | `-21.97%` | `39,694.10` |
| `Live` | `Long` | `0.2215` | 1,630,000.00 USD | 0.00 USD | 128,040.00 USD | `-21.62%` | `578,059.90` |
| `Live` | `Long` | `0.2245` | 1,500,000.00 USD | 0.00 USD | 7,870.00 USD | `-20.55%` | `35,072.00` |
| `Live` | `Long` | `0.2255` | 1,490,000.00 USD | 0.00 USD | 676.50 USD | `-20.20%` | `3,000.00` |
| `Live` | `Long` | `0.2285` | 1,490,000.00 USD | 0.00 USD | 19,240.00 USD | `-19.14%` | `84,190.60` |
| `Live` | `Long` | `0.2295` | 1,470,000.00 USD | 0.00 USD | 160.65 USD | `-18.78%` | `700.00` |
| `Live` | `Long` | `0.2305` | 1,470,000.00 USD | 0.00 USD | 74,180.00 USD | `-18.43%` | `321,829.10` |
| `Live` | `Long` | `0.2315` | 1,400,000.00 USD | 0.00 USD | 25,460.00 USD | `-18.08%` | `109,988.70` |
| `Live` | `Long` | `0.2325` | 1,370,000.00 USD | 0.00 USD | 11,400.00 USD | `-17.72%` | `49,039.80` |
| `Live` | `Long` | `0.2335` | 1,360,000.00 USD | 0.00 USD | 1,940.00 USD | `-17.37%` | `8,326.10` |
| `Live` | `Long` | `0.2345` | 1,360,000.00 USD | 0.00 USD | 336.32 USD | `-17.01%` | `1,434.20` |
| `Live` | `Long` | `0.2355` | 1,360,000.00 USD | 0.00 USD | 20,670.00 USD | `-16.66%` | `87,761.90` |
| `Live` | `Long` | `0.2365` | 1,340,000.00 USD | 0.00 USD | 25,230.00 USD | `-16.31%` | `106,660.90` |
| `Live` | `Long` | `0.2375` | 1,310,000.00 USD | 0.00 USD | 5,610.00 USD | `-15.95%` | `23,636.90` |
| `Live` | `Long` | `0.2385` | 1,310,000.00 USD | 0.00 USD | 92,430.00 USD | `-15.60%` | `387,531.30` |
| `Live` | `Long` | `0.2395` | 1,210,000.00 USD | 0.00 USD | 3,620.00 USD | `-15.25%` | `15,104.80` |
| `Live` | `Long` | `0.2405` | 1,210,000.00 USD | 0.00 USD | 37,700.00 USD | `-14.89%` | `156,745.50` |
| `Live` | `Long` | `0.2415` | 1,170,000.00 USD | 0.00 USD | 32,410.00 USD | `-14.54%` | `134,189.70` |
| `Live` | `Long` | `0.2425` | 1,140,000.00 USD | 0.00 USD | 108,620.00 USD | `-14.18%` | `447,937.20` |
| `Live` | `Long` | `0.2435` | 1,030,000.00 USD | 0.00 USD | 45,960.00 USD | `-13.83%` | `188,765.20` |
| `Live` | `Long` | `0.2445` | 986,150.00 USD | 0.00 USD | 123,540.00 USD | `-13.48%` | `505,283.30` |
| `Live` | `Long` | `0.2455` | 862,610.00 USD | 0.00 USD | 306,750.00 USD | `-13.12%` | `1,249,500.00` |
| `Live` | `Long` | `0.2465` | 555,860.00 USD | 0.00 USD | 5,140.00 USD | `-12.77%` | `20,841.30` |
| `Live` | `Long` | `0.2475` | 550,720.00 USD | 0.00 USD | 10,700.00 USD | `-12.41%` | `43,223.20` |
| `Live` | `Long` | `0.2485` | 540,020.00 USD | 0.00 USD | 74,760.00 USD | `-12.06%` | `300,834.70` |
| `Live` | `Long` | `0.2495` | 465,270.00 USD | 0.00 USD | 28,290.00 USD | `-11.71%` | `113,393.90` |
| `Live` | `Long` | `0.2505` | 436,970.00 USD | 0.00 USD | 113.35 USD | `-11.35%` | `452.50` |
| `Live` | `Long` | `0.2515` | 436,860.00 USD | 0.00 USD | 18,010.00 USD | `-11.00%` | `71,592.20` |
| `Live` | `Long` | `0.2535` | 418,850.00 USD | 0.00 USD | 6,370.00 USD | `-10.29%` | `25,132.30` |
| `Live` | `Long` | `0.2545` | 412,480.00 USD | 0.00 USD | 56,730.00 USD | `-9.94%` | `222,905.40` |
| `Live` | `Long` | `0.2555` | 355,750.00 USD | 0.00 USD | 48,600.00 USD | `-9.58%` | `190,199.50` |
| `Live` | `Long` | `0.2565` | 307,160.00 USD | 0.00 USD | 1,640.00 USD | `-9.23%` | `6,408.20` |
| `Live` | `Long` | `0.2575` | 305,510.00 USD | 0.00 USD | 60,880.00 USD | `-8.88%` | `236,436.40` |
| `Live` | `Long` | `0.2585` | 244,630.00 USD | 0.00 USD | 29,970.00 USD | `-8.52%` | `115,931.80` |
| `Live` | `Long` | `0.2595` | 214,660.00 USD | 0.00 USD | 101,500.00 USD | `-8.17%` | `391,140.80` |
| `Live` | `Long` | `0.2605` | 113,160.00 USD | 0.00 USD | 92,800.00 USD | `-7.81%` | `356,229.60` |
| `Live` | `Long` | `0.2615` | 20,360.00 USD | 0.00 USD | 6,160.00 USD | `-7.46%` | `23,568.20` |
| `Live` | `Long` | `0.2625` | 14,200.00 USD | 0.00 USD | 342.09 USD | `-7.11%` | `1,303.20` |
| `Live` | `Long` | `0.2635` | 13,860.00 USD | 0.00 USD | 126.69 USD | `-6.75%` | `480.80` |
| `Live` | `Long` | `0.2645` | 13,730.00 USD | 0.00 USD | 3,030.00 USD | `-6.40%` | `11,437.60` |
| `Live` | `Long` | `0.2695` | 10,710.00 USD | 0.00 USD | 9,840.00 USD | `-4.63%` | `36,528.30` |
| `Live` | `Long` | `0.2805` | 863.38 USD | 0.00 USD | 863.38 USD | `-0.74%` | `3,078.00` |
| `Live` | `Short` | `0.2965` | 384.41 USD | 384.41 USD | 0.00 USD | `+4.93%` | `1,296.50` |
| `Live` | `Short` | `0.2975` | 5,880.00 USD | 5,500.00 USD | 0.00 USD | `+5.28%` | `18,482.00` |
| `Live` | `Short` | `0.3035` | 22,100.00 USD | 16,220.00 USD | 0.00 USD | `+7.40%` | `53,428.40` |
| `Live` | `Short` | `0.3065` | 23,220.00 USD | 1,120.00 USD | 0.00 USD | `+8.46%` | `3,643.80` |
| `Live` | `Short` | `0.3215` | 28,600.00 USD | 5,380.00 USD | 0.00 USD | `+13.77%` | `16,745.80` |
| `Live` | `Short` | `0.3235` | 29,350.00 USD | 747.16 USD | 0.00 USD | `+14.48%` | `2,309.60` |
| `Live` | `Short` | `0.3415` | 29,450.00 USD | 103.54 USD | 0.00 USD | `+20.85%` | `303.20` |
| `Live` | `Short` | `0.3485` | 29,860.00 USD | 413.95 USD | 0.00 USD | `+23.33%` | `1,187.80` |
| `Live` | `Short` | `0.3575` | 29,960.00 USD | 100.14 USD | 0.00 USD | `+26.51%` | `280.10` |
| `Live` | `Short` | `0.3625` | 32,060.00 USD | 2,100.00 USD | 0.00 USD | `+28.28%` | `5,784.00` |
| `Live` | `Short` | `0.3675` | 34,160.00 USD | 2,100.00 USD | 0.00 USD | `+30.05%` | `5,705.10` |
| `Live` | `Short` | `0.3865` | 34,280.00 USD | 119.35 USD | 0.00 USD | `+36.78%` | `308.80` |
| `Live` | `Short` | `0.3885` | 34,380.00 USD | 103.81 USD | 0.00 USD | `+37.48%` | `267.20` |
| `Live` | `Short` | `0.3965` | 81,960.00 USD | 47,580.00 USD | 0.00 USD | `+40.31%` | `120,000.00` |
| `Live` | `Short` | `0.4025` | 82,200.00 USD | 238.76 USD | 0.00 USD | `+42.44%` | `593.20` |
| `Live` | `Short` | `0.4035` | 82,360.00 USD | 165.84 USD | 0.00 USD | `+42.79%` | `411.00` |
| `Live` | `Short` | `0.4205` | 84,060.00 USD | 1,700.00 USD | 0.00 USD | `+48.81%` | `4,032.60` |
| `Live` | `Short` | `0.4385` | 403,730.00 USD | 319,670.00 USD | 0.00 USD | `+55.18%` | `729,000.00` |
| `Live` | `Short` | `0.4445` | 404,390.00 USD | 666.75 USD | 0.00 USD | `+57.30%` | `1,500.00` |
| `Live` | `Short` | `0.4515` | 404,610.00 USD | 212.84 USD | 0.00 USD | `+59.78%` | `471.40` |
| `Live` | `Short` | `0.4525` | 406,060.00 USD | 1,450.00 USD | 0.00 USD | `+60.13%` | `3,205.50` |
| `Live` | `Short` | `0.4565` | 407,070.00 USD | 1,020.00 USD | 0.00 USD | `+61.55%` | `2,227.00` |
| `Live` | `Short` | `0.4725` | 430,920.00 USD | 23,840.00 USD | 0.00 USD | `+67.21%` | `50,463.70` |
| `Live` | `Short` | `0.5085` | 431,040.00 USD | 120.62 USD | 0.00 USD | `+79.95%` | `237.20` |
| `Live` | `Short` | `0.5155` | 431,470.00 USD | 428.28 USD | 0.00 USD | `+82.43%` | `830.80` |
| `Live` | `Short` | `0.5315` | 445,980.00 USD | 14,510.00 USD | 0.00 USD | `+88.09%` | `27,300.00` |
| `Live` | `Short` | `0.5455` | 446,090.00 USD | 108.72 USD | 0.00 USD | `+93.04%` | `199.30` |
| `Live` | `Short` | `0.5565` | 448,940.00 USD | 2,860.00 USD | 0.00 USD | `+96.94%` | `5,135.90` |

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
  * Current Rate: `-4.60K` | Last 24h: `968.79` | Last 3d: `19.73K` | Last 7d: `53.52K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0152%` | **USDT OKX** | `-0.0288%` |
| **USDT Bybit** | `0.0073%` | **USDT KuCoin** | `-0.0456%` |
| **USDT MEXC** | `-0.0287%` | **USDT BingX** | `0.0084%` |
| **USDT Gate** | `0.0037%` | **USDT Bitget** | `0.0085%` |
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
| `5m` | 0.00 USD | 341,750.00 USD | **`ACCUMULATION`** |
| `15m` | 0.00 USD | 250,200.00 USD | **`ACCUMULATION`** |
| `30m` | 0.00 USD | 67,450.00 USD | **`ACCUMULATION`** |
| `1h` | 0.00 USD | 789,000.00 USD | **`ACCUMULATION`** |
| `2h` | 0.00 USD | 2,060,000.00 USD | **`ACCUMULATION`** |
| `4h` | 0.00 USD | 2,480,000.00 USD | **`ACCUMULATION`** |
| `6h` | 0.00 USD | 1,850,000.00 USD | **`ACCUMULATION`** |
| `8h` | 0.00 USD | -3,600,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 0.00 USD | -4,330,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 0.00 USD | -9,670,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 0.00 USD | -20,580,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 0.00 USD | -65,640,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`+341.75K` | 15m=`+250.20K` | 1h=`+789.00K` | 24h=`-9.67M`
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
  * `2026-10-30 14:37:38 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:38 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:32:38 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 14:09:38 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:52:38 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:38 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:37:38 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:37:38 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `-0.9760` (Risk Distance: `1.23` pts)
  * +2.5R Take Profit: `3.34`
  * Mathematical Lot Sizing: **`8.11 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.2880` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.52` (Risk Distance: `1.23` pts)
  * +2.5R Take Profit: `-2.79`
  * Mathematical Lot Sizing: **`8.11 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.2853`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
