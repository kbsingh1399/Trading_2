# 🏛️ SOVEREIGN CANDIDATE DOSSIER: CRVUSD
**Canonical Key**: `CRVUSD` | **Broker Instrument**: `CRVUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 14:29:41 IST` (`2026-10-30 08:59:41 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.2690` | **Live Ask Quote**: `0.2910` | **Mid Price**: `0.2800`
- **Spread Points**: `22.00` | **Spread BPS**: `785.71 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.2712` | VWAP Z-Score: `-0.20` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0042` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `48.69` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3034` | Lower -3.00σ Band: `0.2389`
  * Upper +2.51σ Band: `0.2981` | Lower -2.51σ Band: `0.2442`
  * Upper +2.01σ Band: `0.2928` | Lower -2.01σ Band: `0.2496`
  * Upper +2.00σ Band: `0.2927` | Lower -2.00σ Band: `0.2497`
  * Upper +1.28σ Band: `0.2849` | Lower -1.28σ Band: `0.2574`
  * Upper +1.00σ Band: `0.2819` | Lower -1.00σ Band: `0.2604`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.2681` | EMA-20=`0.2679` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.2777` (Slope: `+0.0000`) | EMA-100=`0.2907`
  * Institutional Anchors: EMA-144=`0.2977` | EMA-200=`0.3037` (Slope: `-1.5396`) | EMA-233=`0.3064`
- **Range Boundaries**: 24H High=`0.3270` | 24H Low=`0.2530` | Weekly High=`0.3340` | Weekly Low=`0.2530`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.2890` (Distance: `-3.07%`)
  * Point of Control (POC) = `0.2630` (Distance: `+6.45%`)
  * Value Area Low (VAL) = `0.2570` (Distance: `+8.99%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3230` | POC=`0.3160` | VAL=`0.3100`
  * Prior Day Extremes: PDH=`0.3330` | PDL=`0.2890` | PDC=`0.2980`
  * Monday Range Blueprint: High=`0.3430` | Mid=`0.3340` | Low=`0.3250`
  * Developing Weekly Value Area: Weekly VAH=`0.3420` | Weekly POC=`0.3280` | Weekly VAL=`0.3130`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3040` | Low=`0.2530`
  * London Session (08:00-16:00 UTC): High=`0.2750` | Low=`0.2570`
  * New York Session (13:00-21:00 UTC): High=`0.2817` | Low=`0.2783`
  * Initial Balance (First Hour): IB High=`0.2640` | IB Low=`0.2580`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.2789` - `0.2811`
  * Optimal Trade Entry (OTE 0.705): `0.2806`
  * Structural Invalidation Anchor (0.786): `0.2822`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:22:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1859` | `0x12d2...f97f` | `LONG` | 1,111,081.00 USD | `3,972,828.70` | `0.3272` | `0.2814` | `0.000000` | -188,757.74 USD | `-16.99%` | `10X Cross` |

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
| `Live` | `Long Liquidation` | `0.0575` | 2,770.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 219.49 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 140.43 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 964.44 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 1,230.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 339.25 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 2,640.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 3,800.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 2,350.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 8,800.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 485.44 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 665.01 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 16,240.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,010.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 1,290.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 5,580.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 116.35 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 4,300.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 2,130.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 613.05 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 345.53 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 21,200.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 6,200.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 14,730.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1505` | 3,760.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 21,090.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 19,500.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 2,500.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 4,930.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 2,990.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 1,930.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 38,290.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 5,200.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 2,020.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 1,340.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 14,130.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1785` | 12,150.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 5,890.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1805` | 43,250.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1825` | 16,120.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1835` | 179.10 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1845` | 25,400.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 5,840.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1885` | 1,660.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1895` | 1,050.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1905` | 39,050.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1925` | 3,050.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1935` | 8,410.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1945` | 8,250.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1955` | 13,540.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1975` | 292.69 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1985` | 9,040.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 3,430.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2015` | 111,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 18,380.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2065` | 1,400.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2075` | 1,070.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2085` | 2,970.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2115` | 55,550.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2125` | 521.03 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2145` | 68,790.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2155` | 43,100.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2165` | 6,720.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 9,060.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2185` | 72,500.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 899.88 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 8,610.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2215` | 128,040.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 8,550.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2255` | 3,950.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2275` | 420.56 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2285` | 18,940.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 160.65 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 77,640.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 25,920.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 11,290.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 12,380.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 336.32 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 10,150.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 24,590.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 1,050.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 116,990.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2395` | 2,650.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 37,820.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2415` | 32,410.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 108,620.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 45,960.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 123,540.00 USD | 959,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 306,750.00 USD | 836,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 5,140.00 USD | 529,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 10,700.00 USD | 524,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 31,460.00 USD | 513,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2495` | 28,290.00 USD | 482,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 326.05 USD | 453,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2515` | 18,010.00 USD | 453,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2535` | 6,370.00 USD | 435,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2545` | 27,660.00 USD | 429,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 48,600.00 USD | 401,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 361.20 USD | 353,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2575` | 62,880.00 USD | 352,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 70,980.00 USD | 289,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 113,910.00 USD | 218,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 92,970.00 USD | 104,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 8,690.00 USD | 11,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 485.10 USD | 3,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 126.69 USD | 2,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 2,410.00 USD | 2,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 205.05 USD | 205.05 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2695` | 13,520.00 USD | 13,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 8,350.00 USD | 21,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 24,650.00 USD | 46,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2825` | 4,190.00 USD | 50,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2835` | 1,950.00 USD | 52,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2855` | 28,850.00 USD | 81,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 126.41 USD | 81,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3215` | 5,380.00 USD | 87,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3235` | 747.16 USD | 87,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3415` | 103.54 USD | 87,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3455` | 115.05 USD | 87,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3485` | 413.95 USD | 88,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3545` | 446.07 USD | 88,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3575` | 100.14 USD | 88,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 2,100.00 USD | 91,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3675` | 2,100.00 USD | 93,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3865` | 119.35 USD | 93,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3885` | 103.81 USD | 93,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3955` | 47,460.00 USD | 140,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4025` | 238.76 USD | 141,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4035` | 165.84 USD | 141,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4205` | 1,700.00 USD | 142,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4445` | 666.75 USD | 143,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4475` | 210.95 USD | 143,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4495` | 327,690.00 USD | 471,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4545` | 1,010.00 USD | 472,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4625` | 1,480.00 USD | 473,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4755` | 24,000.00 USD | 497,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5155` | 428.28 USD | 498,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5315` | 14,510.00 USD | 512,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5455` | 239.04 USD | 513,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5565` | 2,860.00 USD | 516,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0575` | 2,440,000.00 USD | 0.00 USD | 2,770.00 USD | `-79.54%` | `48,255.50` |
| `Live` | `Long` | `0.0585` | 2,440,000.00 USD | 0.00 USD | 219.49 USD | `-79.19%` | `3,752.00` |
| `Live` | `Long` | `0.0625` | 2,440,000.00 USD | 0.00 USD | 140.43 USD | `-77.77%` | `2,246.90` |
| `Live` | `Long` | `0.0645` | 2,440,000.00 USD | 0.00 USD | 964.44 USD | `-77.05%` | `14,952.50` |
| `Live` | `Long` | `0.0655` | 2,440,000.00 USD | 0.00 USD | 1,230.00 USD | `-76.70%` | `18,735.40` |
| `Live` | `Long` | `0.0675` | 2,440,000.00 USD | 0.00 USD | 339.25 USD | `-75.99%` | `5,026.00` |
| `Live` | `Long` | `0.0685` | 2,440,000.00 USD | 0.00 USD | 2,640.00 USD | `-75.63%` | `38,602.60` |
| `Live` | `Long` | `0.0725` | 2,430,000.00 USD | 0.00 USD | 3,800.00 USD | `-74.21%` | `52,428.50` |
| `Live` | `Long` | `0.0795` | 2,430,000.00 USD | 0.00 USD | 2,350.00 USD | `-71.72%` | `29,622.60` |
| `Live` | `Long` | `0.0825` | 2,430,000.00 USD | 0.00 USD | 8,800.00 USD | `-70.65%` | `106,697.00` |
| `Live` | `Long` | `0.0865` | 2,420,000.00 USD | 0.00 USD | 485.44 USD | `-69.23%` | `5,612.00` |
| `Live` | `Long` | `0.0885` | 2,420,000.00 USD | 0.00 USD | 665.01 USD | `-68.52%` | `7,514.20` |
| `Live` | `Long` | `0.0895` | 2,420,000.00 USD | 0.00 USD | 16,240.00 USD | `-68.16%` | `181,411.80` |
| `Live` | `Long` | `0.1035` | 2,400,000.00 USD | 0.00 USD | 1,010.00 USD | `-63.18%` | `9,765.50` |
| `Live` | `Long` | `0.1095` | 2,400,000.00 USD | 0.00 USD | 1,290.00 USD | `-61.04%` | `11,739.70` |
| `Live` | `Long` | `0.1185` | 2,400,000.00 USD | 0.00 USD | 5,580.00 USD | `-57.84%` | `47,058.80` |
| `Live` | `Long` | `0.1225` | 2,390,000.00 USD | 0.00 USD | 116.35 USD | `-56.42%` | `949.80` |
| `Live` | `Long` | `0.1255` | 2,390,000.00 USD | 0.00 USD | 4,300.00 USD | `-55.35%` | `34,264.40` |
| `Live` | `Long` | `0.1265` | 2,390,000.00 USD | 0.00 USD | 2,130.00 USD | `-55.00%` | `16,859.10` |
| `Live` | `Long` | `0.1285` | 2,390,000.00 USD | 0.00 USD | 613.05 USD | `-54.29%` | `4,770.80` |
| `Live` | `Long` | `0.1315` | 2,390,000.00 USD | 0.00 USD | 345.53 USD | `-53.22%` | `2,627.60` |
| `Live` | `Long` | `0.1325` | 2,380,000.00 USD | 0.00 USD | 21,200.00 USD | `-52.86%` | `160,000.00` |
| `Live` | `Long` | `0.1435` | 2,360,000.00 USD | 0.00 USD | 6,200.00 USD | `-48.95%` | `43,210.20` |
| `Live` | `Long` | `0.1465` | 2,360,000.00 USD | 0.00 USD | 14,730.00 USD | `-47.88%` | `100,540.60` |
| `Live` | `Long` | `0.1505` | 2,340,000.00 USD | 0.00 USD | 3,760.00 USD | `-46.46%` | `25,000.00` |
| `Live` | `Long` | `0.1595` | 2,340,000.00 USD | 0.00 USD | 21,090.00 USD | `-43.26%` | `132,229.20` |
| `Live` | `Long` | `0.1625` | 2,320,000.00 USD | 0.00 USD | 19,500.00 USD | `-42.19%` | `120,000.00` |
| `Live` | `Long` | `0.1645` | 2,300,000.00 USD | 0.00 USD | 2,500.00 USD | `-41.48%` | `15,205.80` |
| `Live` | `Long` | `0.1665` | 2,300,000.00 USD | 0.00 USD | 4,930.00 USD | `-40.77%` | `29,616.80` |
| `Live` | `Long` | `0.1695` | 2,290,000.00 USD | 0.00 USD | 2,990.00 USD | `-39.70%` | `17,641.90` |
| `Live` | `Long` | `0.1705` | 2,290,000.00 USD | 0.00 USD | 1,930.00 USD | `-39.34%` | `11,332.30` |
| `Live` | `Long` | `0.1715` | 2,290,000.00 USD | 0.00 USD | 38,290.00 USD | `-38.99%` | `223,280.90` |
| `Live` | `Long` | `0.1725` | 2,250,000.00 USD | 0.00 USD | 5,200.00 USD | `-38.63%` | `30,143.90` |
| `Live` | `Long` | `0.1735` | 2,240,000.00 USD | 0.00 USD | 2,020.00 USD | `-38.28%` | `11,641.60` |
| `Live` | `Long` | `0.1765` | 2,240,000.00 USD | 0.00 USD | 1,340.00 USD | `-37.21%` | `7,607.60` |
| `Live` | `Long` | `0.1775` | 2,240,000.00 USD | 0.00 USD | 14,130.00 USD | `-36.85%` | `79,610.90` |
| `Live` | `Long` | `0.1785` | 2,220,000.00 USD | 0.00 USD | 12,150.00 USD | `-36.50%` | `68,050.80` |
| `Live` | `Long` | `0.1795` | 2,210,000.00 USD | 0.00 USD | 5,890.00 USD | `-36.14%` | `32,795.10` |
| `Live` | `Long` | `0.1805` | 2,210,000.00 USD | 0.00 USD | 43,250.00 USD | `-35.79%` | `239,618.40` |
| `Live` | `Long` | `0.1825` | 2,160,000.00 USD | 0.00 USD | 16,120.00 USD | `-35.07%` | `88,308.30` |
| `Live` | `Long` | `0.1835` | 2,150,000.00 USD | 0.00 USD | 179.10 USD | `-34.72%` | `976.00` |
| `Live` | `Long` | `0.1845` | 2,150,000.00 USD | 0.00 USD | 25,400.00 USD | `-34.36%` | `137,653.50` |
| `Live` | `Long` | `0.1875` | 2,120,000.00 USD | 0.00 USD | 5,840.00 USD | `-33.30%` | `31,135.10` |
| `Live` | `Long` | `0.1885` | 2,120,000.00 USD | 0.00 USD | 1,660.00 USD | `-32.94%` | `8,802.20` |
| `Live` | `Long` | `0.1895` | 2,110,000.00 USD | 0.00 USD | 1,050.00 USD | `-32.58%` | `5,539.20` |
| `Live` | `Long` | `0.1905` | 2,110,000.00 USD | 0.00 USD | 39,050.00 USD | `-32.23%` | `205,000.00` |
| `Live` | `Long` | `0.1925` | 2,070,000.00 USD | 0.00 USD | 3,050.00 USD | `-31.52%` | `15,821.40` |
| `Live` | `Long` | `0.1935` | 2,070,000.00 USD | 0.00 USD | 8,410.00 USD | `-31.16%` | `43,453.50` |
| `Live` | `Long` | `0.1945` | 2,060,000.00 USD | 0.00 USD | 8,250.00 USD | `-30.81%` | `42,397.20` |
| `Live` | `Long` | `0.1955` | 2,050,000.00 USD | 0.00 USD | 13,540.00 USD | `-30.45%` | `69,252.60` |
| `Live` | `Long` | `0.1975` | 2,040,000.00 USD | 0.00 USD | 292.69 USD | `-29.74%` | `1,482.00` |
| `Live` | `Long` | `0.1985` | 2,040,000.00 USD | 0.00 USD | 9,040.00 USD | `-29.38%` | `45,563.00` |
| `Live` | `Long` | `0.1995` | 2,030,000.00 USD | 0.00 USD | 3,430.00 USD | `-29.03%` | `17,199.40` |
| `Live` | `Long` | `0.2015` | 2,030,000.00 USD | 0.00 USD | 111,000.00 USD | `-28.31%` | `550,886.10` |
| `Live` | `Long` | `0.2045` | 1,920,000.00 USD | 0.00 USD | 18,380.00 USD | `-27.25%` | `89,877.80` |
| `Live` | `Long` | `0.2065` | 1,900,000.00 USD | 0.00 USD | 1,400.00 USD | `-26.54%` | `6,802.40` |
| `Live` | `Long` | `0.2075` | 1,900,000.00 USD | 0.00 USD | 1,070.00 USD | `-26.18%` | `5,147.80` |
| `Live` | `Long` | `0.2085` | 1,900,000.00 USD | 0.00 USD | 2,970.00 USD | `-25.82%` | `14,230.20` |
| `Live` | `Long` | `0.2115` | 1,890,000.00 USD | 0.00 USD | 55,550.00 USD | `-24.76%` | `262,635.40` |
| `Live` | `Long` | `0.2125` | 1,840,000.00 USD | 0.00 USD | 521.03 USD | `-24.40%` | `2,451.90` |
| `Live` | `Long` | `0.2145` | 1,840,000.00 USD | 0.00 USD | 68,790.00 USD | `-23.69%` | `320,696.20` |
| `Live` | `Long` | `0.2155` | 1,770,000.00 USD | 0.00 USD | 43,100.00 USD | `-23.33%` | `200,000.00` |
| `Live` | `Long` | `0.2165` | 1,730,000.00 USD | 0.00 USD | 6,720.00 USD | `-22.98%` | `31,044.10` |
| `Live` | `Long` | `0.2175` | 1,720,000.00 USD | 0.00 USD | 9,060.00 USD | `-22.62%` | `41,666.50` |
| `Live` | `Long` | `0.2185` | 1,710,000.00 USD | 0.00 USD | 72,500.00 USD | `-22.27%` | `331,799.60` |
| `Live` | `Long` | `0.2195` | 1,640,000.00 USD | 0.00 USD | 899.88 USD | `-21.91%` | `4,099.70` |
| `Live` | `Long` | `0.2205` | 1,640,000.00 USD | 0.00 USD | 8,610.00 USD | `-21.56%` | `39,028.70` |
| `Live` | `Long` | `0.2215` | 1,630,000.00 USD | 0.00 USD | 128,040.00 USD | `-21.20%` | `578,059.90` |
| `Live` | `Long` | `0.2245` | 1,500,000.00 USD | 0.00 USD | 8,550.00 USD | `-20.13%` | `38,072.00` |
| `Live` | `Long` | `0.2255` | 1,490,000.00 USD | 0.00 USD | 3,950.00 USD | `-19.78%` | `17,532.10` |
| `Live` | `Long` | `0.2275` | 1,490,000.00 USD | 0.00 USD | 420.56 USD | `-19.07%` | `1,848.60` |
| `Live` | `Long` | `0.2285` | 1,490,000.00 USD | 0.00 USD | 18,940.00 USD | `-18.71%` | `82,884.40` |
| `Live` | `Long` | `0.2295` | 1,470,000.00 USD | 0.00 USD | 160.65 USD | `-18.35%` | `700.00` |
| `Live` | `Long` | `0.2305` | 1,470,000.00 USD | 0.00 USD | 77,640.00 USD | `-18.00%` | `336,829.50` |
| `Live` | `Long` | `0.2315` | 1,390,000.00 USD | 0.00 USD | 25,920.00 USD | `-17.64%` | `111,949.50` |
| `Live` | `Long` | `0.2325` | 1,360,000.00 USD | 0.00 USD | 11,290.00 USD | `-17.29%` | `48,549.10` |
| `Live` | `Long` | `0.2335` | 1,350,000.00 USD | 0.00 USD | 12,380.00 USD | `-16.93%` | `53,007.00` |
| `Live` | `Long` | `0.2345` | 1,340,000.00 USD | 0.00 USD | 336.32 USD | `-16.57%` | `1,434.20` |
| `Live` | `Long` | `0.2355` | 1,340,000.00 USD | 0.00 USD | 10,150.00 USD | `-16.22%` | `43,081.00` |
| `Live` | `Long` | `0.2365` | 1,330,000.00 USD | 0.00 USD | 24,590.00 USD | `-15.86%` | `103,980.90` |
| `Live` | `Long` | `0.2375` | 1,310,000.00 USD | 0.00 USD | 1,050.00 USD | `-15.51%` | `4,438.30` |
| `Live` | `Long` | `0.2385` | 1,300,000.00 USD | 0.00 USD | 116,990.00 USD | `-15.15%` | `490,531.10` |
| `Live` | `Long` | `0.2395` | 1,190,000.00 USD | 0.00 USD | 2,650.00 USD | `-14.80%` | `11,083.20` |
| `Live` | `Long` | `0.2405` | 1,180,000.00 USD | 0.00 USD | 37,820.00 USD | `-14.44%` | `157,236.20` |
| `Live` | `Long` | `0.2415` | 1,150,000.00 USD | 0.00 USD | 32,410.00 USD | `-14.08%` | `134,189.70` |
| `Live` | `Long` | `0.2425` | 1,110,000.00 USD | 0.00 USD | 108,620.00 USD | `-13.73%` | `447,937.20` |
| `Live` | `Long` | `0.2435` | 1,010,000.00 USD | 0.00 USD | 45,960.00 USD | `-13.37%` | `188,765.20` |
| `Live` | `Long` | `0.2445` | 959,860.00 USD | 0.00 USD | 123,540.00 USD | `-13.02%` | `505,283.30` |
| `Live` | `Long` | `0.2455` | 836,320.00 USD | 0.00 USD | 306,750.00 USD | `-12.66%` | `1,249,500.00` |
| `Live` | `Long` | `0.2465` | 529,570.00 USD | 0.00 USD | 5,140.00 USD | `-12.31%` | `20,841.30` |
| `Live` | `Long` | `0.2475` | 524,430.00 USD | 0.00 USD | 10,700.00 USD | `-11.95%` | `43,223.20` |
| `Live` | `Long` | `0.2485` | 513,730.00 USD | 0.00 USD | 31,460.00 USD | `-11.59%` | `126,587.90` |
| `Live` | `Long` | `0.2495` | 482,270.00 USD | 0.00 USD | 28,290.00 USD | `-11.24%` | `113,393.90` |
| `Live` | `Long` | `0.2505` | 453,980.00 USD | 0.00 USD | 326.05 USD | `-10.88%` | `1,301.60` |
| `Live` | `Long` | `0.2515` | 453,660.00 USD | 0.00 USD | 18,010.00 USD | `-10.53%` | `71,592.20` |
| `Live` | `Long` | `0.2535` | 435,650.00 USD | 0.00 USD | 6,370.00 USD | `-9.82%` | `25,132.30` |
| `Live` | `Long` | `0.2545` | 429,280.00 USD | 0.00 USD | 27,660.00 USD | `-9.46%` | `108,701.80` |
| `Live` | `Long` | `0.2555` | 401,620.00 USD | 0.00 USD | 48,600.00 USD | `-9.10%` | `190,199.50` |
| `Live` | `Long` | `0.2565` | 353,020.00 USD | 0.00 USD | 361.20 USD | `-8.75%` | `1,408.20` |
| `Live` | `Long` | `0.2575` | 352,660.00 USD | 0.00 USD | 62,880.00 USD | `-8.39%` | `244,210.00` |
| `Live` | `Long` | `0.2585` | 289,770.00 USD | 0.00 USD | 70,980.00 USD | `-8.04%` | `274,571.40` |
| `Live` | `Long` | `0.2595` | 218,800.00 USD | 0.00 USD | 113,910.00 USD | `-7.68%` | `438,964.90` |
| `Live` | `Long` | `0.2605` | 104,890.00 USD | 0.00 USD | 92,970.00 USD | `-7.33%` | `356,895.00` |
| `Live` | `Long` | `0.2615` | 11,910.00 USD | 0.00 USD | 8,690.00 USD | `-6.97%` | `33,217.30` |
| `Live` | `Long` | `0.2625` | 3,230.00 USD | 0.00 USD | 485.10 USD | `-6.61%` | `1,848.00` |
| `Live` | `Long` | `0.2635` | 2,740.00 USD | 0.00 USD | 126.69 USD | `-6.26%` | `480.80` |
| `Live` | `Long` | `0.2645` | 2,620.00 USD | 0.00 USD | 2,410.00 USD | `-5.90%` | `9,117.10` |
| `Live` | `Long` | `0.2665` | 205.05 USD | 0.00 USD | 205.05 USD | `-5.19%` | `769.40` |
| `Live` | `Short` | `0.2695` | 13,520.00 USD | 13,520.00 USD | 0.00 USD | `-4.12%` | `50,169.80` |
| `Live` | `Short` | `0.2725` | 21,870.00 USD | 8,350.00 USD | 0.00 USD | `-3.06%` | `30,652.90` |
| `Live` | `Short` | `0.2745` | 46,520.00 USD | 24,650.00 USD | 0.00 USD | `-2.34%` | `89,803.50` |
| `Live` | `Short` | `0.2825` | 50,710.00 USD | 4,190.00 USD | 0.00 USD | `+0.50%` | `14,827.70` |
| `Live` | `Short` | `0.2835` | 52,670.00 USD | 1,950.00 USD | 0.00 USD | `+0.86%` | `6,884.00` |
| `Live` | `Short` | `0.2855` | 81,510.00 USD | 28,850.00 USD | 0.00 USD | `+1.57%` | `101,046.90` |
| `Live` | `Short` | `0.2935` | 81,640.00 USD | 126.41 USD | 0.00 USD | `+4.41%` | `430.70` |
| `Live` | `Short` | `0.3215` | 87,020.00 USD | 5,380.00 USD | 0.00 USD | `+14.38%` | `16,745.80` |
| `Live` | `Short` | `0.3235` | 87,770.00 USD | 747.16 USD | 0.00 USD | `+15.09%` | `2,309.60` |
| `Live` | `Short` | `0.3415` | 87,870.00 USD | 103.54 USD | 0.00 USD | `+21.49%` | `303.20` |
| `Live` | `Short` | `0.3455` | 87,990.00 USD | 115.05 USD | 0.00 USD | `+22.91%` | `333.00` |
| `Live` | `Short` | `0.3485` | 88,400.00 USD | 413.95 USD | 0.00 USD | `+23.98%` | `1,187.80` |
| `Live` | `Short` | `0.3545` | 88,850.00 USD | 446.07 USD | 0.00 USD | `+26.12%` | `1,258.30` |
| `Live` | `Short` | `0.3575` | 88,950.00 USD | 100.14 USD | 0.00 USD | `+27.18%` | `280.10` |
| `Live` | `Short` | `0.3625` | 91,050.00 USD | 2,100.00 USD | 0.00 USD | `+28.96%` | `5,784.00` |
| `Live` | `Short` | `0.3675` | 93,140.00 USD | 2,100.00 USD | 0.00 USD | `+30.74%` | `5,705.10` |
| `Live` | `Short` | `0.3865` | 93,260.00 USD | 119.35 USD | 0.00 USD | `+37.50%` | `308.80` |
| `Live` | `Short` | `0.3885` | 93,370.00 USD | 103.81 USD | 0.00 USD | `+38.21%` | `267.20` |
| `Live` | `Short` | `0.3955` | 140,830.00 USD | 47,460.00 USD | 0.00 USD | `+40.70%` | `120,000.00` |
| `Live` | `Short` | `0.4025` | 141,070.00 USD | 238.76 USD | 0.00 USD | `+43.19%` | `593.20` |
| `Live` | `Short` | `0.4035` | 141,230.00 USD | 165.84 USD | 0.00 USD | `+43.55%` | `411.00` |
| `Live` | `Short` | `0.4205` | 142,930.00 USD | 1,700.00 USD | 0.00 USD | `+49.60%` | `4,032.60` |
| `Live` | `Short` | `0.4445` | 143,590.00 USD | 666.75 USD | 0.00 USD | `+58.13%` | `1,500.00` |
| `Live` | `Short` | `0.4475` | 143,800.00 USD | 210.95 USD | 0.00 USD | `+59.20%` | `471.40` |
| `Live` | `Short` | `0.4495` | 471,490.00 USD | 327,690.00 USD | 0.00 USD | `+59.91%` | `729,000.00` |
| `Live` | `Short` | `0.4545` | 472,500.00 USD | 1,010.00 USD | 0.00 USD | `+61.69%` | `2,227.00` |
| `Live` | `Short` | `0.4625` | 473,980.00 USD | 1,480.00 USD | 0.00 USD | `+64.54%` | `3,205.50` |
| `Live` | `Short` | `0.4755` | 497,980.00 USD | 24,000.00 USD | 0.00 USD | `+69.16%` | `50,463.70` |
| `Live` | `Short` | `0.5155` | 498,410.00 USD | 428.28 USD | 0.00 USD | `+83.39%` | `830.80` |
| `Live` | `Short` | `0.5315` | 512,920.00 USD | 14,510.00 USD | 0.00 USD | `+89.09%` | `27,300.00` |
| `Live` | `Short` | `0.5455` | 513,160.00 USD | 239.04 USD | 0.00 USD | `+94.07%` | `438.20` |
| `Live` | `Short` | `0.5565` | 516,020.00 USD | 2,860.00 USD | 0.00 USD | `+97.98%` | `5,135.90` |

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
  * Current Rate: `-4.72K` | Last 24h: `968.79` | Last 3d: `19.73K` | Last 7d: `53.52K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0152%` | **USDT OKX** | `-0.0287%` |
| **USDT Bybit** | `0.0004%` | **USDT KuCoin** | `-0.0461%` |
| **USDT MEXC** | `-0.0286%` | **USDT BingX** | `0.0093%` |
| **USDT Gate** | `-0.0054%` | **USDT Bitget** | `0.0086%` |
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
| `5m` | 0.00 USD | -178,330.00 USD | **`DISTRIBUTION`** |
| `15m` | 0.00 USD | -349,710.00 USD | **`DISTRIBUTION`** |
| `30m` | 0.00 USD | -349,260.00 USD | **`DISTRIBUTION`** |
| `1h` | 0.00 USD | 533,100.00 USD | **`ACCUMULATION`** |
| `2h` | 0.00 USD | 1,590,000.00 USD | **`ACCUMULATION`** |
| `4h` | 0.00 USD | 2,200,000.00 USD | **`ACCUMULATION`** |
| `6h` | 0.00 USD | 1,530,000.00 USD | **`ACCUMULATION`** |
| `8h` | 0.00 USD | -4,070,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 0.00 USD | -5,050,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 0.00 USD | -10,070,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 0.00 USD | -21,670,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 0.00 USD | -66,450,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`-178.33K` | 15m=`-349.71K` | 1h=`+533.10K` | 24h=`-10.07M`
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
  * `2026-10-30 14:09:50 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:50:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:31:50 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `0.2190` (Risk Distance: `0.0440` pts)
  * +2.5R Take Profit: `0.3670`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.2890` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3270` (Risk Distance: `0.0440` pts)
  * +2.5R Take Profit: `0.1790`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.2822`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
