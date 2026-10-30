# 🏛️ SOVEREIGN CANDIDATE DOSSIER: CRVUSD
**Canonical Key**: `CRVUSD` | **Broker Instrument**: `CRVUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 09:19:10 IST` (`2026-10-30 03:49:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.2650` | **Live Ask Quote**: `0.2870` | **Mid Price**: `0.2760`
- **Spread Points**: `22.00` | **Spread BPS**: `797.10 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.2755` | VWAP Z-Score: `-1.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0062` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `30.12` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3100` | Lower -3.00σ Band: `0.2410`
  * Upper +2.51σ Band: `0.3044` | Lower -2.51σ Band: `0.2466`
  * Upper +2.01σ Band: `0.2986` | Lower -2.01σ Band: `0.2524`
  * Upper +2.00σ Band: `0.2985` | Lower -2.00σ Band: `0.2525`
  * Upper +1.28σ Band: `0.2902` | Lower -1.28σ Band: `0.2608`
  * Upper +1.00σ Band: `0.2870` | Lower -1.00σ Band: `0.2640`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.2696` | EMA-20=`0.2797` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.2942` (Slope: `+0.0000`) | EMA-100=`0.3042`
  * Institutional Anchors: EMA-144=`0.3087` | EMA-200=`0.3123` (Slope: `-1.5220`) | EMA-233=`0.3144`
- **Range Boundaries**: 24H High=`0.3270` | 24H Low=`0.2530` | Weekly High=`0.3340` | Weekly Low=`0.2530`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3030` (Distance: `-9.06%`)
  * Point of Control (POC) = `0.2950` (Distance: `-6.44%`)
  * Value Area Low (VAL) = `0.2720` (Distance: `+1.65%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3230` | POC=`0.3160` | VAL=`0.3100`
  * Prior Day Extremes: PDH=`0.3330` | PDL=`0.2890` | PDC=`0.2980`
  * Monday Range Blueprint: High=`0.3430` | Mid=`0.3340` | Low=`0.3250`
  * Developing Weekly Value Area: Weekly VAH=`0.3420` | Weekly POC=`0.3280` | Weekly VAL=`0.3160`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3040` | Low=`0.2530`
  * London Session (08:00-16:00 UTC): High=`0.2771` | Low=`0.2749`
  * New York Session (13:00-21:00 UTC): High=`0.2777` | Low=`0.2743`
  * Initial Balance (First Hour): IB High=`0.2768` | IB Low=`0.2752`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.2749` - `0.2771`
  * Optimal Trade Entry (OTE 0.705): `0.2766`
  * Structural Invalidation Anchor (0.786): `0.2782`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:07:15 IST` |

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
  * 24H Horizon: Short MP=`0.3453` (Vol: 74,017.03 USD, Dist: `+2.95%`) | Long MP=`0.3285` (Vol: 54,223.53 USD, Dist: `--2.06%`)
  * 48H Horizon: Short MP=`0.3451` (Vol: 61,276.63 USD, Dist: `+2.89%`) | Long MP=`0.3266` (Vol: 86,480.44 USD, Dist: `--2.62%`)
  * 3D Horizon: Short MP=`0.3454` (Vol: 78,069.95 USD, Dist: `+2.98%`) | Long MP=`0.3267` (Vol: 81,272.05 USD, Dist: `--2.59%`)
  * 7D Horizon: Short MP=`0.3626` (Vol: 135,917.70 USD, Dist: `+8.67%`) | Long MP=`0.3267` (Vol: 96,300.06 USD, Dist: `--2.09%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0575` | 304.95 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 135.30 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 2,360.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 5,420.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 2,330.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 1,580.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 404.59 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 4,140.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 485.44 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 140.72 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 1,770.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 11,000.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 116.35 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 1,210.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 4,300.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 613.05 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 1,540.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 350.78 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1365` | 215.93 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1375` | 6,470.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 14,050.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 23,120.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 1,160.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 12,380.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 8,910.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 20,300.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1575` | 1,180.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 1,270.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 2,500.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 4,930.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 278.30 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 989.26 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 7,430.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 1,340.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 14,130.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1785` | 12,010.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 13,180.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1805` | 17,400.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1825` | 410.06 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1835` | 179.10 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1845` | 26,250.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1855` | 28,430.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1865` | 9,460.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 5,840.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1885` | 1,810.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1895` | 1,050.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1905` | 32,820.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1925` | 9,520.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1935` | 27,200.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1955` | 19,500.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1965` | 291.21 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1985` | 1,100.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 3,430.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 26,560.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2055` | 41,100.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2085` | 2,510.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2115` | 64,010.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2125` | 1,990.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2145` | 170,030.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2165` | 3,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 9,490.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 1,100.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 130,770.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2215` | 1,600.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 4,540.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 123,670.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2255` | 1,130.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2265` | 12,250.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2285` | 19,980.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 4,450.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 12,300.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 22,940.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 10,270.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 79,420.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 336.32 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 7,070.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 2,120.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 97,350.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 91,800.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2395` | 2,650.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 37,840.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2415` | 149,040.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 108,860.00 USD | 968,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 48,870.00 USD | 859,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 1,290.00 USD | 810,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 12,150.00 USD | 809,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 27,110.00 USD | 797,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 15,880.00 USD | 770,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 43,060.00 USD | 754,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2495` | 337,350.00 USD | 711,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 3,300.00 USD | 373,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2515` | 761.11 USD | 370,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2535` | 14,320.00 USD | 369,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2545` | 45,270.00 USD | 355,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 51,100.00 USD | 310,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 171.29 USD | 259,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2575` | 15,420.00 USD | 258,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 51,510.00 USD | 243,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 37,800.00 USD | 191,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 86,800.00 USD | 154,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 4,020.00 USD | 67,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 5,040.00 USD | 63,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 245.27 USD | 58,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 7,760.00 USD | 58,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2725` | 50,250.00 USD | 50,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2845` | 1,490.00 USD | 1,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2865` | 30,760.00 USD | 32,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2895` | 1,140.00 USD | 33,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2925` | 543.93 USD | 33,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3215` | 5,380.00 USD | 39,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3485` | 413.95 USD | 39,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3545` | 446.07 USD | 40,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3575` | 100.14 USD | 40,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 2,100.00 USD | 42,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3675` | 2,100.00 USD | 44,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3855` | 119.04 USD | 44,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3885` | 103.81 USD | 44,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4025` | 238.76 USD | 44,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4035` | 236.85 USD | 45,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4205` | 1,700.00 USD | 46,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4385` | 202.54 USD | 47,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4445` | 889.00 USD | 47,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4585` | 1,020.00 USD | 48,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4685` | 341,540.00 USD | 390,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4895` | 1,570.00 USD | 392,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5155` | 428.28 USD | 392,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5255` | 63,060.00 USD | 455,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5315` | 14,510.00 USD | 470,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0575` | 2,470,000.00 USD | 0.00 USD | 304.95 USD | `-78.99%` | `5,303.40` |
| `Live` | `Long` | `0.0615` | 2,470,000.00 USD | 0.00 USD | 135.30 USD | `-77.53%` | `2,200.00` |
| `Live` | `Long` | `0.0635` | 2,470,000.00 USD | 0.00 USD | 2,360.00 USD | `-76.80%` | `37,120.00` |
| `Live` | `Long` | `0.0775` | 2,470,000.00 USD | 0.00 USD | 5,420.00 USD | `-71.68%` | `70,000.00` |
| `Live` | `Long` | `0.0785` | 2,460,000.00 USD | 0.00 USD | 2,330.00 USD | `-71.31%` | `29,622.60` |
| `Live` | `Long` | `0.0795` | 2,460,000.00 USD | 0.00 USD | 1,580.00 USD | `-70.95%` | `19,907.20` |
| `Live` | `Long` | `0.0805` | 2,460,000.00 USD | 0.00 USD | 404.59 USD | `-70.58%` | `5,026.00` |
| `Live` | `Long` | `0.0815` | 2,460,000.00 USD | 0.00 USD | 4,140.00 USD | `-70.22%` | `50,846.60` |
| `Live` | `Long` | `0.0865` | 2,450,000.00 USD | 0.00 USD | 485.44 USD | `-68.39%` | `5,612.00` |
| `Live` | `Long` | `0.0915` | 2,450,000.00 USD | 0.00 USD | 140.72 USD | `-66.56%` | `1,537.90` |
| `Live` | `Long` | `0.0945` | 2,450,000.00 USD | 0.00 USD | 1,770.00 USD | `-65.47%` | `18,735.40` |
| `Live` | `Long` | `0.0985` | 2,450,000.00 USD | 0.00 USD | 11,000.00 USD | `-64.01%` | `111,716.60` |
| `Live` | `Long` | `0.1225` | 2,440,000.00 USD | 0.00 USD | 116.35 USD | `-55.24%` | `949.80` |
| `Live` | `Long` | `0.1235` | 2,440,000.00 USD | 0.00 USD | 1,210.00 USD | `-54.87%` | `9,765.50` |
| `Live` | `Long` | `0.1255` | 2,440,000.00 USD | 0.00 USD | 4,300.00 USD | `-54.14%` | `34,264.40` |
| `Live` | `Long` | `0.1285` | 2,430,000.00 USD | 0.00 USD | 613.05 USD | `-53.04%` | `4,770.80` |
| `Live` | `Long` | `0.1315` | 2,430,000.00 USD | 0.00 USD | 1,540.00 USD | `-51.95%` | `11,739.70` |
| `Live` | `Long` | `0.1335` | 2,430,000.00 USD | 0.00 USD | 350.78 USD | `-51.22%` | `2,627.60` |
| `Live` | `Long` | `0.1365` | 2,430,000.00 USD | 0.00 USD | 215.93 USD | `-50.12%` | `1,581.90` |
| `Live` | `Long` | `0.1375` | 2,430,000.00 USD | 0.00 USD | 6,470.00 USD | `-49.76%` | `47,058.80` |
| `Live` | `Long` | `0.1405` | 2,420,000.00 USD | 0.00 USD | 14,050.00 USD | `-48.66%` | `100,000.00` |
| `Live` | `Long` | `0.1445` | 2,410,000.00 USD | 0.00 USD | 23,120.00 USD | `-47.20%` | `160,000.00` |
| `Live` | `Long` | `0.1455` | 2,390,000.00 USD | 0.00 USD | 1,160.00 USD | `-46.83%` | `8,000.00` |
| `Live` | `Long` | `0.1465` | 2,390,000.00 USD | 0.00 USD | 12,380.00 USD | `-46.47%` | `84,498.00` |
| `Live` | `Long` | `0.1485` | 2,370,000.00 USD | 0.00 USD | 8,910.00 USD | `-45.74%` | `60,000.00` |
| `Live` | `Long` | `0.1535` | 2,360,000.00 USD | 0.00 USD | 20,300.00 USD | `-43.91%` | `132,229.20` |
| `Live` | `Long` | `0.1575` | 2,340,000.00 USD | 0.00 USD | 1,180.00 USD | `-42.45%` | `7,514.20` |
| `Live` | `Long` | `0.1585` | 2,340,000.00 USD | 0.00 USD | 1,270.00 USD | `-42.08%` | `8,042.60` |
| `Live` | `Long` | `0.1645` | 2,340,000.00 USD | 0.00 USD | 2,500.00 USD | `-39.89%` | `15,205.80` |
| `Live` | `Long` | `0.1665` | 2,340,000.00 USD | 0.00 USD | 4,930.00 USD | `-39.16%` | `29,616.80` |
| `Live` | `Long` | `0.1695` | 2,330,000.00 USD | 0.00 USD | 278.30 USD | `-38.06%` | `1,641.90` |
| `Live` | `Long` | `0.1715` | 2,330,000.00 USD | 0.00 USD | 989.26 USD | `-37.33%` | `5,768.30` |
| `Live` | `Long` | `0.1725` | 2,330,000.00 USD | 0.00 USD | 7,430.00 USD | `-36.97%` | `43,059.00` |
| `Live` | `Long` | `0.1765` | 2,320,000.00 USD | 0.00 USD | 1,340.00 USD | `-35.50%` | `7,607.60` |
| `Live` | `Long` | `0.1775` | 2,320,000.00 USD | 0.00 USD | 14,130.00 USD | `-35.14%` | `79,610.90` |
| `Live` | `Long` | `0.1785` | 2,310,000.00 USD | 0.00 USD | 12,010.00 USD | `-34.77%` | `67,270.30` |
| `Live` | `Long` | `0.1795` | 2,300,000.00 USD | 0.00 USD | 13,180.00 USD | `-34.41%` | `73,444.60` |
| `Live` | `Long` | `0.1805` | 2,280,000.00 USD | 0.00 USD | 17,400.00 USD | `-34.04%` | `96,371.80` |
| `Live` | `Long` | `0.1825` | 2,270,000.00 USD | 0.00 USD | 410.06 USD | `-33.31%` | `2,246.90` |
| `Live` | `Long` | `0.1835` | 2,270,000.00 USD | 0.00 USD | 179.10 USD | `-32.95%` | `976.00` |
| `Live` | `Long` | `0.1845` | 2,270,000.00 USD | 0.00 USD | 26,250.00 USD | `-32.58%` | `142,269.40` |
| `Live` | `Long` | `0.1855` | 2,240,000.00 USD | 0.00 USD | 28,430.00 USD | `-32.22%` | `153,246.60` |
| `Live` | `Long` | `0.1865` | 2,210,000.00 USD | 0.00 USD | 9,460.00 USD | `-31.85%` | `50,699.40` |
| `Live` | `Long` | `0.1875` | 2,200,000.00 USD | 0.00 USD | 5,840.00 USD | `-31.48%` | `31,135.10` |
| `Live` | `Long` | `0.1885` | 2,200,000.00 USD | 0.00 USD | 1,810.00 USD | `-31.12%` | `9,582.70` |
| `Live` | `Long` | `0.1895` | 2,190,000.00 USD | 0.00 USD | 1,050.00 USD | `-30.75%` | `5,539.20` |
| `Live` | `Long` | `0.1905` | 2,190,000.00 USD | 0.00 USD | 32,820.00 USD | `-30.39%` | `172,299.70` |
| `Live` | `Long` | `0.1925` | 2,160,000.00 USD | 0.00 USD | 9,520.00 USD | `-29.66%` | `49,429.00` |
| `Live` | `Long` | `0.1935` | 2,150,000.00 USD | 0.00 USD | 27,200.00 USD | `-29.29%` | `140,581.40` |
| `Live` | `Long` | `0.1955` | 2,120,000.00 USD | 0.00 USD | 19,500.00 USD | `-28.56%` | `99,769.50` |
| `Live` | `Long` | `0.1965` | 2,100,000.00 USD | 0.00 USD | 291.21 USD | `-28.20%` | `1,482.00` |
| `Live` | `Long` | `0.1985` | 2,100,000.00 USD | 0.00 USD | 1,100.00 USD | `-27.46%` | `5,563.00` |
| `Live` | `Long` | `0.1995` | 2,100,000.00 USD | 0.00 USD | 3,430.00 USD | `-27.10%` | `17,199.40` |
| `Live` | `Long` | `0.2045` | 2,100,000.00 USD | 0.00 USD | 26,560.00 USD | `-25.27%` | `129,877.80` |
| `Live` | `Long` | `0.2055` | 2,070,000.00 USD | 0.00 USD | 41,100.00 USD | `-24.91%` | `200,000.00` |
| `Live` | `Long` | `0.2085` | 2,030,000.00 USD | 0.00 USD | 2,510.00 USD | `-23.81%` | `12,025.50` |
| `Live` | `Long` | `0.2115` | 2,030,000.00 USD | 0.00 USD | 64,010.00 USD | `-22.71%` | `302,635.40` |
| `Live` | `Long` | `0.2125` | 1,970,000.00 USD | 0.00 USD | 1,990.00 USD | `-22.35%` | `9,352.10` |
| `Live` | `Long` | `0.2145` | 1,960,000.00 USD | 0.00 USD | 170,030.00 USD | `-21.62%` | `792,665.80` |
| `Live` | `Long` | `0.2165` | 1,790,000.00 USD | 0.00 USD | 3,000.00 USD | `-20.89%` | `13,855.90` |
| `Live` | `Long` | `0.2175` | 1,790,000.00 USD | 0.00 USD | 9,490.00 USD | `-20.52%` | `43,612.50` |
| `Live` | `Long` | `0.2195` | 1,780,000.00 USD | 0.00 USD | 1,100.00 USD | `-19.79%` | `5,028.50` |
| `Live` | `Long` | `0.2205` | 1,780,000.00 USD | 0.00 USD | 130,770.00 USD | `-19.43%` | `593,044.70` |
| `Live` | `Long` | `0.2215` | 1,650,000.00 USD | 0.00 USD | 1,600.00 USD | `-19.06%` | `7,240.00` |
| `Live` | `Long` | `0.2225` | 1,650,000.00 USD | 0.00 USD | 4,540.00 USD | `-18.69%` | `20,384.10` |
| `Live` | `Long` | `0.2245` | 1,640,000.00 USD | 0.00 USD | 123,670.00 USD | `-17.96%` | `550,886.10` |
| `Live` | `Long` | `0.2255` | 1,520,000.00 USD | 0.00 USD | 1,130.00 USD | `-17.60%` | `5,000.30` |
| `Live` | `Long` | `0.2265` | 1,520,000.00 USD | 0.00 USD | 12,250.00 USD | `-17.23%` | `54,078.40` |
| `Live` | `Long` | `0.2285` | 1,510,000.00 USD | 0.00 USD | 19,980.00 USD | `-16.50%` | `87,429.70` |
| `Live` | `Long` | `0.2295` | 1,490,000.00 USD | 0.00 USD | 4,450.00 USD | `-16.14%` | `19,392.20` |
| `Live` | `Long` | `0.2305` | 1,480,000.00 USD | 0.00 USD | 12,300.00 USD | `-15.77%` | `53,377.50` |
| `Live` | `Long` | `0.2315` | 1,470,000.00 USD | 0.00 USD | 22,940.00 USD | `-15.41%` | `99,106.30` |
| `Live` | `Long` | `0.2325` | 1,450,000.00 USD | 0.00 USD | 10,270.00 USD | `-15.04%` | `44,170.10` |
| `Live` | `Long` | `0.2335` | 1,440,000.00 USD | 0.00 USD | 79,420.00 USD | `-14.68%` | `340,125.70` |
| `Live` | `Long` | `0.2345` | 1,360,000.00 USD | 0.00 USD | 336.32 USD | `-14.31%` | `1,434.20` |
| `Live` | `Long` | `0.2355` | 1,360,000.00 USD | 0.00 USD | 7,070.00 USD | `-13.94%` | `30,000.00` |
| `Live` | `Long` | `0.2365` | 1,350,000.00 USD | 0.00 USD | 2,120.00 USD | `-13.58%` | `8,980.90` |
| `Live` | `Long` | `0.2375` | 1,350,000.00 USD | 0.00 USD | 97,350.00 USD | `-13.21%` | `409,900.00` |
| `Live` | `Long` | `0.2385` | 1,250,000.00 USD | 0.00 USD | 91,800.00 USD | `-12.85%` | `384,902.20` |
| `Live` | `Long` | `0.2395` | 1,160,000.00 USD | 0.00 USD | 2,650.00 USD | `-12.48%` | `11,083.20` |
| `Live` | `Long` | `0.2405` | 1,160,000.00 USD | 0.00 USD | 37,840.00 USD | `-12.12%` | `157,345.00` |
| `Live` | `Long` | `0.2415` | 1,120,000.00 USD | 0.00 USD | 149,040.00 USD | `-11.75%` | `617,135.40` |
| `Live` | `Long` | `0.2425` | 968,340.00 USD | 0.00 USD | 108,860.00 USD | `-11.39%` | `448,910.10` |
| `Live` | `Long` | `0.2435` | 859,470.00 USD | 0.00 USD | 48,870.00 USD | `-11.02%` | `200,685.10` |
| `Live` | `Long` | `0.2445` | 810,610.00 USD | 0.00 USD | 1,290.00 USD | `-10.66%` | `5,283.30` |
| `Live` | `Long` | `0.2455` | 809,320.00 USD | 0.00 USD | 12,150.00 USD | `-10.29%` | `49,500.00` |
| `Live` | `Long` | `0.2465` | 797,160.00 USD | 0.00 USD | 27,110.00 USD | `-9.92%` | `109,971.80` |
| `Live` | `Long` | `0.2475` | 770,060.00 USD | 0.00 USD | 15,880.00 USD | `-9.56%` | `64,170.50` |
| `Live` | `Long` | `0.2485` | 754,170.00 USD | 0.00 USD | 43,060.00 USD | `-9.19%` | `173,266.10` |
| `Live` | `Long` | `0.2495` | 711,120.00 USD | 0.00 USD | 337,350.00 USD | `-8.83%` | `1,352,096.60` |
| `Live` | `Long` | `0.2505` | 373,770.00 USD | 0.00 USD | 3,300.00 USD | `-8.46%` | `13,183.80` |
| `Live` | `Long` | `0.2515` | 370,470.00 USD | 0.00 USD | 761.11 USD | `-8.10%` | `3,026.30` |
| `Live` | `Long` | `0.2535` | 369,710.00 USD | 0.00 USD | 14,320.00 USD | `-7.37%` | `56,501.50` |
| `Live` | `Long` | `0.2545` | 355,380.00 USD | 0.00 USD | 45,270.00 USD | `-7.00%` | `177,858.60` |
| `Live` | `Long` | `0.2555` | 310,120.00 USD | 0.00 USD | 51,100.00 USD | `-6.64%` | `199,996.80` |
| `Live` | `Long` | `0.2565` | 259,020.00 USD | 0.00 USD | 171.29 USD | `-6.27%` | `667.80` |
| `Live` | `Long` | `0.2575` | 258,850.00 USD | 0.00 USD | 15,420.00 USD | `-5.91%` | `59,879.00` |
| `Live` | `Long` | `0.2585` | 243,430.00 USD | 0.00 USD | 51,510.00 USD | `-5.54%` | `199,280.50` |
| `Live` | `Long` | `0.2595` | 191,910.00 USD | 0.00 USD | 37,800.00 USD | `-5.17%` | `145,658.20` |
| `Live` | `Long` | `0.2605` | 154,120.00 USD | 0.00 USD | 86,800.00 USD | `-4.81%` | `333,223.40` |
| `Live` | `Long` | `0.2615` | 67,310.00 USD | 0.00 USD | 4,020.00 USD | `-4.44%` | `15,356.60` |
| `Live` | `Long` | `0.2625` | 63,300.00 USD | 0.00 USD | 5,040.00 USD | `-4.08%` | `19,208.00` |
| `Live` | `Long` | `0.2635` | 58,250.00 USD | 0.00 USD | 245.27 USD | `-3.71%` | `930.80` |
| `Live` | `Long` | `0.2645` | 58,010.00 USD | 0.00 USD | 7,760.00 USD | `-3.35%` | `29,324.90` |
| `Live` | `Long` | `0.2725` | 50,250.00 USD | 0.00 USD | 50,250.00 USD | `-0.42%` | `184,408.40` |
| `Live` | `Short` | `0.2845` | 1,490.00 USD | 1,490.00 USD | 0.00 USD | `+3.96%` | `5,239.80` |
| `Live` | `Short` | `0.2865` | 32,250.00 USD | 30,760.00 USD | 0.00 USD | `+4.69%` | `107,374.00` |
| `Live` | `Short` | `0.2895` | 33,390.00 USD | 1,140.00 USD | 0.00 USD | `+5.79%` | `3,939.00` |
| `Live` | `Short` | `0.2925` | 33,940.00 USD | 543.93 USD | 0.00 USD | `+6.88%` | `1,859.60` |
| `Live` | `Short` | `0.3215` | 39,320.00 USD | 5,380.00 USD | 0.00 USD | `+17.48%` | `16,745.80` |
| `Live` | `Short` | `0.3485` | 39,740.00 USD | 413.95 USD | 0.00 USD | `+27.35%` | `1,187.80` |
| `Live` | `Short` | `0.3545` | 40,180.00 USD | 446.07 USD | 0.00 USD | `+29.54%` | `1,258.30` |
| `Live` | `Short` | `0.3575` | 40,280.00 USD | 100.14 USD | 0.00 USD | `+30.64%` | `280.10` |
| `Live` | `Short` | `0.3625` | 42,380.00 USD | 2,100.00 USD | 0.00 USD | `+32.46%` | `5,784.00` |
| `Live` | `Short` | `0.3675` | 44,470.00 USD | 2,100.00 USD | 0.00 USD | `+34.29%` | `5,705.10` |
| `Live` | `Short` | `0.3855` | 44,590.00 USD | 119.04 USD | 0.00 USD | `+40.87%` | `308.80` |
| `Live` | `Short` | `0.3885` | 44,700.00 USD | 103.81 USD | 0.00 USD | `+41.96%` | `267.20` |
| `Live` | `Short` | `0.4025` | 44,940.00 USD | 238.76 USD | 0.00 USD | `+47.08%` | `593.20` |
| `Live` | `Short` | `0.4035` | 45,170.00 USD | 236.85 USD | 0.00 USD | `+47.45%` | `587.00` |
| `Live` | `Short` | `0.4205` | 46,870.00 USD | 1,700.00 USD | 0.00 USD | `+53.66%` | `4,032.60` |
| `Live` | `Short` | `0.4385` | 47,070.00 USD | 202.54 USD | 0.00 USD | `+60.24%` | `461.90` |
| `Live` | `Short` | `0.4445` | 47,960.00 USD | 889.00 USD | 0.00 USD | `+62.43%` | `2,000.00` |
| `Live` | `Short` | `0.4585` | 48,980.00 USD | 1,020.00 USD | 0.00 USD | `+67.54%` | `2,227.00` |
| `Live` | `Short` | `0.4685` | 390,520.00 USD | 341,540.00 USD | 0.00 USD | `+71.20%` | `729,000.00` |
| `Live` | `Short` | `0.4895` | 392,090.00 USD | 1,570.00 USD | 0.00 USD | `+78.87%` | `3,205.50` |
| `Live` | `Short` | `0.5155` | 392,520.00 USD | 428.28 USD | 0.00 USD | `+88.37%` | `830.80` |
| `Live` | `Short` | `0.5255` | 455,580.00 USD | 63,060.00 USD | 0.00 USD | `+92.03%` | `120,000.00` |
| `Live` | `Short` | `0.5315` | 470,090.00 USD | 14,510.00 USD | 0.00 USD | `+94.22%` | `27,300.00` |

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
  * Current Rate: `1.11K` | Last 24h: `9.20K` | Last 3d: `30.42K` | Last 7d: `57.33K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0072%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0072%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0099%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
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
| `5m` | 12,900.00 USD | -16,540.00 USD | **`DISTRIBUTION`** |
| `15m` | 56,690.00 USD | 22,720.00 USD | **`ACCUMULATION`** |
| `30m` | 20,520.00 USD | -143,200.00 USD | **`DISTRIBUTION`** |
| `1h` | 87,040.00 USD | -831,930.00 USD | **`DISTRIBUTION`** |
| `2h` | -373,260.00 USD | -3,850,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -341,310.00 USD | -5,750,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -285,520.00 USD | -6,510,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -453,050.00 USD | -9,190,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -760,560.00 USD | -10,930,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -582,720.00 USD | -11,650,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -2,230,000.00 USD | -24,320,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -15,220,000.00 USD | -66,680,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+12.90K` | 15m=`+56.69K` | 1h=`+87.04K` | 24h=`-582.72K`
* Futures Capital Netflows: 5m=`-16.54K` | 15m=`+22.72K` | 1h=`-831.93K` | 24h=`-11.65M`
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
  * `2026-10-30 09:09:58 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:15:58 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:14:58 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:14:58 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:16:58 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:16:58 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:16:58 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.2720` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.2315` (Risk Distance: `0.0440` pts)
  * +2.5R Take Profit: `0.3820`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3030` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3435` (Risk Distance: `0.0440` pts)
  * +2.5R Take Profit: `0.1930`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.2782`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
