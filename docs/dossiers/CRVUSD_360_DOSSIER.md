# 🏛️ SOVEREIGN CANDIDATE DOSSIER: CRVUSD
**Canonical Key**: `CRVUSD` | **Broker Instrument**: `CRVUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 04:50:10 IST` (`2026-10-29 23:20:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.2970` | **Live Ask Quote**: `0.3200` | **Mid Price**: `0.3085`
- **Spread Points**: `23.00` | **Spread BPS**: `745.54 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3120` | VWAP Z-Score: `-1.64` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0042` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `32.09` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3378` | Lower -3.00σ Band: `0.2863`
  * Upper +2.51σ Band: `0.3336` | Lower -2.51σ Band: `0.2905`
  * Upper +2.01σ Band: `0.3293` | Lower -2.01σ Band: `0.2948`
  * Upper +2.00σ Band: `0.3292` | Lower -2.00σ Band: `0.2949`
  * Upper +1.28σ Band: `0.3230` | Lower -1.28σ Band: `0.3011`
  * Upper +1.00σ Band: `0.3206` | Lower -1.00σ Band: `0.3035`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.2993` | EMA-20=`0.3038` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3102` (Slope: `+0.0000`) | EMA-100=`0.3145`
  * Institutional Anchors: EMA-144=`0.3166` | EMA-200=`0.3184` (Slope: `-0.7605`) | EMA-233=`0.3197`
- **Range Boundaries**: 24H High=`0.3270` | 24H Low=`0.2890` | Weekly High=`0.3340` | Weekly Low=`0.2890`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3010` (Distance: `+2.62%`)
  * Point of Control (POC) = `0.2990` (Distance: `+3.35%`)
  * Value Area Low (VAL) = `0.2960` (Distance: `+4.51%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3230` | POC=`0.3160` | VAL=`0.3100`
  * Prior Day Extremes: PDH=`0.3330` | PDL=`0.2890` | PDC=`0.2980`
  * Monday Range Blueprint: High=`0.3430` | Mid=`0.3340` | Low=`0.3250`
  * Developing Weekly Value Area: Weekly VAH=`0.3390` | Weekly POC=`0.3290` | Weekly VAL=`0.3200`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3040` | Low=`0.2930`
  * London Session (08:00-16:00 UTC): High=`0.3097` | Low=`0.3073`
  * New York Session (13:00-21:00 UTC): High=`0.3104` | Low=`0.3066`
  * Initial Balance (First Hour): IB High=`0.3094` | IB Low=`0.3076`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3073` - `0.3097`
  * Optimal Trade Entry (OTE 0.705): `0.3091`
  * Structural Invalidation Anchor (0.786): `0.3110`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:46:31 IST` |

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
| `Live` | `Long Liquidation` | `0.0625` | 4,380.00 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 116.27 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 374.44 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 567.32 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 2,330.00 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 111.48 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 1,560.00 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 485.44 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 854.48 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 4,650.00 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 5,180.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1125` | 252.78 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 1,360.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 116.35 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 4,300.00 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 613.05 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 689.70 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 1,090.00 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 1,160.00 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 20,300.00 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 827.75 USD | 5,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 1,340.00 USD | 5,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 4,930.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 464.68 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 4,670.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 68,220.00 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 1,530.00 USD | 5,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 14,130.00 USD | 5,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1785` | 12,010.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 13,180.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1805` | 16,880.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1835` | 3,670.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1845` | 1,480.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1865` | 9,460.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 5,840.00 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1885` | 1,660.00 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1895` | 1,050.00 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1905` | 952.50 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1915` | 283.80 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1925` | 928.81 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1935` | 2,150.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1945` | 5,830.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1955` | 15,480.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1975` | 7,900.00 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1985` | 1,100.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 177,970.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2005` | 8,020.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2025` | 1,670.00 USD | 5,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 18,380.00 USD | 5,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2055` | 1,060.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2065` | 31,650.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2075` | 622.50 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2085` | 2,390.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2105` | 934.45 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2125` | 521.03 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2135` | 31,610.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2145` | 10,090.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 10,700.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 436.01 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 131,350.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2215` | 25,450.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 15,420.00 USD | 4,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 2,540.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2255` | 676.50 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2285` | 2,780.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 498.24 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 45,160.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 19,620.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 10,270.00 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 8,790.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 10,540.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 112,340.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 24,830.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 98,180.00 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2395` | 13,670.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 13,650.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2415` | 21,530.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 109,880.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 31,580.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 1,040.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 158,620.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 19,910.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 18,230.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 4,030.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2495` | 28,290.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 151,180.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2515` | 201.55 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2525` | 6,660.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2535` | 6,340.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2545` | 22,030.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 73,600.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 823.90 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 26,200.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 44,370.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 16,140.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 81,860.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 468.30 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 25,940.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 104,970.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 39,280.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 26,710.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 15,220.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 42,530.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2695` | 212,800.00 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2705` | 28,770.00 USD | 3,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2715` | 43,600.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2725` | 8,770.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 29,940.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 442,080.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 30,910.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2765` | 6,580.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2775` | 56,210.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 3,950.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 40,110.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 53,850.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 410,250.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 260,250.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2835` | 167,190.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2845` | 21,530.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 215,740.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2865` | 50,450.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2875` | 126,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 239,420.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2895` | 299,110.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 356,530.00 USD | 782,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 46,990.00 USD | 426,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2925` | 55,810.00 USD | 379,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2935` | 68,200.00 USD | 323,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 10,990.00 USD | 255,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2955` | 37,340.00 USD | 244,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2965` | 25,390.00 USD | 207,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2975` | 25,610.00 USD | 181,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2985` | 102,350.00 USD | 156,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2995` | 850.85 USD | 53,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3005` | 2,100.00 USD | 2,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3015` | 4,260.00 USD | 52,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3075` | 48,650.00 USD | 48,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3195` | 2,270.00 USD | 4,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3255` | 352.26 USD | 4,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3265` | 5,140.00 USD | 9,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 14,350.00 USD | 24,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3485` | 413.95 USD | 24,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3545` | 446.07 USD | 25,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3575` | 100.14 USD | 25,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 2,100.00 USD | 27,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3675` | 2,100.00 USD | 29,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3885` | 103.81 USD | 29,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4025` | 477.49 USD | 29,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4035` | 236.85 USD | 30,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4205` | 1,700.00 USD | 31,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4245` | 115.25 USD | 32,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4445` | 889.00 USD | 32,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4465` | 379.44 USD | 33,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4575` | 11,500.00 USD | 44,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4945` | 360,490.00 USD | 405,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4995` | 1,600.00 USD | 406,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5015` | 160.23 USD | 407,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5155` | 428.28 USD | 407,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5185` | 62,220.00 USD | 469,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5315` | 14,510.00 USD | 484,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5565` | 2,860.00 USD | 487,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5835` | 17,400.00 USD | 504,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0625` | 5,690,000.00 USD | 0.00 USD | 4,380.00 USD | `-79.72%` | `70,000.00` |
| `Live` | `Long` | `0.0735` | 5,680,000.00 USD | 0.00 USD | 116.27 USD | `-76.15%` | `1,581.90` |
| `Live` | `Long` | `0.0745` | 5,680,000.00 USD | 0.00 USD | 374.44 USD | `-75.83%` | `5,026.00` |
| `Live` | `Long` | `0.0755` | 5,680,000.00 USD | 0.00 USD | 567.32 USD | `-75.50%` | `7,514.20` |
| `Live` | `Long` | `0.0785` | 5,680,000.00 USD | 0.00 USD | 2,330.00 USD | `-74.53%` | `29,622.60` |
| `Live` | `Long` | `0.0825` | 5,680,000.00 USD | 0.00 USD | 111.48 USD | `-73.23%` | `1,351.30` |
| `Live` | `Long` | `0.0835` | 5,680,000.00 USD | 0.00 USD | 1,560.00 USD | `-72.91%` | `18,735.40` |
| `Live` | `Long` | `0.0865` | 5,680,000.00 USD | 0.00 USD | 485.44 USD | `-71.93%` | `5,612.00` |
| `Live` | `Long` | `0.0875` | 5,680,000.00 USD | 0.00 USD | 854.48 USD | `-71.61%` | `9,765.50` |
| `Live` | `Long` | `0.0915` | 5,680,000.00 USD | 0.00 USD | 4,650.00 USD | `-70.31%` | `50,846.60` |
| `Live` | `Long` | `0.1085` | 5,670,000.00 USD | 0.00 USD | 5,180.00 USD | `-64.80%` | `47,700.00` |
| `Live` | `Long` | `0.1125` | 5,670,000.00 USD | 0.00 USD | 252.78 USD | `-63.50%` | `2,246.90` |
| `Live` | `Long` | `0.1155` | 5,670,000.00 USD | 0.00 USD | 1,360.00 USD | `-62.52%` | `11,739.70` |
| `Live` | `Long` | `0.1225` | 5,660,000.00 USD | 0.00 USD | 116.35 USD | `-60.25%` | `949.80` |
| `Live` | `Long` | `0.1255` | 5,660,000.00 USD | 0.00 USD | 4,300.00 USD | `-59.28%` | `34,264.40` |
| `Live` | `Long` | `0.1285` | 5,660,000.00 USD | 0.00 USD | 613.05 USD | `-58.31%` | `4,770.80` |
| `Live` | `Long` | `0.1295` | 5,660,000.00 USD | 0.00 USD | 689.70 USD | `-57.98%` | `5,325.90` |
| `Live` | `Long` | `0.1355` | 5,660,000.00 USD | 0.00 USD | 1,090.00 USD | `-56.04%` | `8,042.60` |
| `Live` | `Long` | `0.1455` | 5,660,000.00 USD | 0.00 USD | 1,160.00 USD | `-52.79%` | `8,000.00` |
| `Live` | `Long` | `0.1535` | 5,660,000.00 USD | 0.00 USD | 20,300.00 USD | `-50.19%` | `132,229.20` |
| `Live` | `Long` | `0.1585` | 5,640,000.00 USD | 0.00 USD | 827.75 USD | `-48.57%` | `5,222.40` |
| `Live` | `Long` | `0.1645` | 5,640,000.00 USD | 0.00 USD | 1,340.00 USD | `-46.63%` | `8,141.90` |
| `Live` | `Long` | `0.1665` | 5,630,000.00 USD | 0.00 USD | 4,930.00 USD | `-45.98%` | `29,616.80` |
| `Live` | `Long` | `0.1715` | 5,630,000.00 USD | 0.00 USD | 464.68 USD | `-44.35%` | `2,709.50` |
| `Live` | `Long` | `0.1725` | 5,630,000.00 USD | 0.00 USD | 4,670.00 USD | `-44.03%` | `27,059.00` |
| `Live` | `Long` | `0.1755` | 5,620,000.00 USD | 0.00 USD | 68,220.00 USD | `-43.06%` | `388,690.50` |
| `Live` | `Long` | `0.1765` | 5,560,000.00 USD | 0.00 USD | 1,530.00 USD | `-42.73%` | `8,680.50` |
| `Live` | `Long` | `0.1775` | 5,550,000.00 USD | 0.00 USD | 14,130.00 USD | `-42.41%` | `79,610.90` |
| `Live` | `Long` | `0.1785` | 5,540,000.00 USD | 0.00 USD | 12,010.00 USD | `-42.08%` | `67,270.30` |
| `Live` | `Long` | `0.1795` | 5,530,000.00 USD | 0.00 USD | 13,180.00 USD | `-41.76%` | `73,444.60` |
| `Live` | `Long` | `0.1805` | 5,510,000.00 USD | 0.00 USD | 16,880.00 USD | `-41.43%` | `93,542.70` |
| `Live` | `Long` | `0.1835` | 5,500,000.00 USD | 0.00 USD | 3,670.00 USD | `-40.46%` | `19,976.00` |
| `Live` | `Long` | `0.1845` | 5,490,000.00 USD | 0.00 USD | 1,480.00 USD | `-40.14%` | `8,024.00` |
| `Live` | `Long` | `0.1865` | 5,490,000.00 USD | 0.00 USD | 9,460.00 USD | `-39.49%` | `50,699.40` |
| `Live` | `Long` | `0.1875` | 5,480,000.00 USD | 0.00 USD | 5,840.00 USD | `-39.16%` | `31,135.10` |
| `Live` | `Long` | `0.1885` | 5,480,000.00 USD | 0.00 USD | 1,660.00 USD | `-38.84%` | `8,802.20` |
| `Live` | `Long` | `0.1895` | 5,480,000.00 USD | 0.00 USD | 1,050.00 USD | `-38.51%` | `5,539.20` |
| `Live` | `Long` | `0.1905` | 5,470,000.00 USD | 0.00 USD | 952.50 USD | `-38.19%` | `5,000.00` |
| `Live` | `Long` | `0.1915` | 5,470,000.00 USD | 0.00 USD | 283.80 USD | `-37.87%` | `1,482.00` |
| `Live` | `Long` | `0.1925` | 5,470,000.00 USD | 0.00 USD | 928.81 USD | `-37.54%` | `4,825.00` |
| `Live` | `Long` | `0.1935` | 5,470,000.00 USD | 0.00 USD | 2,150.00 USD | `-37.22%` | `11,110.40` |
| `Live` | `Long` | `0.1945` | 5,470,000.00 USD | 0.00 USD | 5,830.00 USD | `-36.89%` | `30,000.00` |
| `Live` | `Long` | `0.1955` | 5,460,000.00 USD | 0.00 USD | 15,480.00 USD | `-36.57%` | `79,182.40` |
| `Live` | `Long` | `0.1975` | 5,450,000.00 USD | 0.00 USD | 7,900.00 USD | `-35.92%` | `40,000.00` |
| `Live` | `Long` | `0.1985` | 5,440,000.00 USD | 0.00 USD | 1,100.00 USD | `-35.59%` | `5,563.00` |
| `Live` | `Long` | `0.1995` | 5,440,000.00 USD | 0.00 USD | 177,970.00 USD | `-35.27%` | `892,075.00` |
| `Live` | `Long` | `0.2005` | 5,260,000.00 USD | 0.00 USD | 8,020.00 USD | `-34.94%` | `40,000.00` |
| `Live` | `Long` | `0.2025` | 5,250,000.00 USD | 0.00 USD | 1,670.00 USD | `-34.30%` | `8,241.60` |
| `Live` | `Long` | `0.2045` | 5,250,000.00 USD | 0.00 USD | 18,380.00 USD | `-33.65%` | `89,877.80` |
| `Live` | `Long` | `0.2055` | 5,230,000.00 USD | 0.00 USD | 1,060.00 USD | `-33.32%` | `5,147.80` |
| `Live` | `Long` | `0.2065` | 5,230,000.00 USD | 0.00 USD | 31,650.00 USD | `-33.00%` | `153,246.60` |
| `Live` | `Long` | `0.2075` | 5,200,000.00 USD | 0.00 USD | 622.50 USD | `-32.67%` | `3,000.00` |
| `Live` | `Long` | `0.2085` | 5,200,000.00 USD | 0.00 USD | 2,390.00 USD | `-32.35%` | `11,465.50` |
| `Live` | `Long` | `0.2105` | 5,200,000.00 USD | 0.00 USD | 934.45 USD | `-31.70%` | `4,439.20` |
| `Live` | `Long` | `0.2125` | 5,200,000.00 USD | 0.00 USD | 521.03 USD | `-31.05%` | `2,451.90` |
| `Live` | `Long` | `0.2135` | 5,200,000.00 USD | 0.00 USD | 31,610.00 USD | `-30.73%` | `148,060.00` |
| `Live` | `Long` | `0.2145` | 5,170,000.00 USD | 0.00 USD | 10,090.00 USD | `-30.40%` | `47,058.80` |
| `Live` | `Long` | `0.2175` | 5,160,000.00 USD | 0.00 USD | 10,700.00 USD | `-29.43%` | `49,193.80` |
| `Live` | `Long` | `0.2195` | 5,140,000.00 USD | 0.00 USD | 436.01 USD | `-28.78%` | `1,986.40` |
| `Live` | `Long` | `0.2205` | 5,140,000.00 USD | 0.00 USD | 131,350.00 USD | `-28.46%` | `595,704.50` |
| `Live` | `Long` | `0.2215` | 5,010,000.00 USD | 0.00 USD | 25,450.00 USD | `-28.13%` | `114,892.30` |
| `Live` | `Long` | `0.2225` | 4,990,000.00 USD | 0.00 USD | 15,420.00 USD | `-27.81%` | `69,315.90` |
| `Live` | `Long` | `0.2245` | 4,970,000.00 USD | 0.00 USD | 2,540.00 USD | `-27.16%` | `11,332.30` |
| `Live` | `Long` | `0.2255` | 4,970,000.00 USD | 0.00 USD | 676.50 USD | `-26.83%` | `3,000.00` |
| `Live` | `Long` | `0.2285` | 4,970,000.00 USD | 0.00 USD | 2,780.00 USD | `-25.86%` | `12,174.10` |
| `Live` | `Long` | `0.2295` | 4,970,000.00 USD | 0.00 USD | 498.24 USD | `-25.54%` | `2,171.00` |
| `Live` | `Long` | `0.2305` | 4,970,000.00 USD | 0.00 USD | 45,160.00 USD | `-25.21%` | `195,912.20` |
| `Live` | `Long` | `0.2315` | 4,920,000.00 USD | 0.00 USD | 19,620.00 USD | `-24.89%` | `84,743.40` |
| `Live` | `Long` | `0.2325` | 4,900,000.00 USD | 0.00 USD | 10,270.00 USD | `-24.56%` | `44,170.10` |
| `Live` | `Long` | `0.2335` | 4,890,000.00 USD | 0.00 USD | 8,790.00 USD | `-24.24%` | `37,658.20` |
| `Live` | `Long` | `0.2355` | 4,880,000.00 USD | 0.00 USD | 10,540.00 USD | `-23.59%` | `44,770.40` |
| `Live` | `Long` | `0.2365` | 4,870,000.00 USD | 0.00 USD | 112,340.00 USD | `-23.26%` | `475,000.00` |
| `Live` | `Long` | `0.2375` | 4,760,000.00 USD | 0.00 USD | 24,830.00 USD | `-22.94%` | `104,554.80` |
| `Live` | `Long` | `0.2385` | 4,730,000.00 USD | 0.00 USD | 98,180.00 USD | `-22.62%` | `411,666.40` |
| `Live` | `Long` | `0.2395` | 4,640,000.00 USD | 0.00 USD | 13,670.00 USD | `-22.29%` | `57,081.10` |
| `Live` | `Long` | `0.2405` | 4,620,000.00 USD | 0.00 USD | 13,650.00 USD | `-21.97%` | `56,745.50` |
| `Live` | `Long` | `0.2415` | 4,610,000.00 USD | 0.00 USD | 21,530.00 USD | `-21.64%` | `89,135.40` |
| `Live` | `Long` | `0.2425` | 4,590,000.00 USD | 0.00 USD | 109,880.00 USD | `-21.32%` | `453,105.40` |
| `Live` | `Long` | `0.2435` | 4,480,000.00 USD | 0.00 USD | 31,580.00 USD | `-20.99%` | `129,692.00` |
| `Live` | `Long` | `0.2445` | 4,450,000.00 USD | 0.00 USD | 1,040.00 USD | `-20.67%` | `4,237.20` |
| `Live` | `Long` | `0.2455` | 4,440,000.00 USD | 0.00 USD | 158,620.00 USD | `-20.34%` | `646,128.60` |
| `Live` | `Long` | `0.2465` | 4,290,000.00 USD | 0.00 USD | 19,910.00 USD | `-20.02%` | `80,768.90` |
| `Live` | `Long` | `0.2475` | 4,270,000.00 USD | 0.00 USD | 18,230.00 USD | `-19.70%` | `73,640.00` |
| `Live` | `Long` | `0.2485` | 4,250,000.00 USD | 0.00 USD | 4,030.00 USD | `-19.37%` | `16,203.80` |
| `Live` | `Long` | `0.2495` | 4,240,000.00 USD | 0.00 USD | 28,290.00 USD | `-19.05%` | `113,393.90` |
| `Live` | `Long` | `0.2505` | 4,220,000.00 USD | 0.00 USD | 151,180.00 USD | `-18.72%` | `603,515.90` |
| `Live` | `Long` | `0.2515` | 4,060,000.00 USD | 0.00 USD | 201.55 USD | `-18.40%` | `801.40` |
| `Live` | `Long` | `0.2525` | 4,060,000.00 USD | 0.00 USD | 6,660.00 USD | `-18.07%` | `26,359.60` |
| `Live` | `Long` | `0.2535` | 4,060,000.00 USD | 0.00 USD | 6,340.00 USD | `-17.75%` | `25,000.00` |
| `Live` | `Long` | `0.2545` | 4,050,000.00 USD | 0.00 USD | 22,030.00 USD | `-17.42%` | `86,545.50` |
| `Live` | `Long` | `0.2555` | 4,030,000.00 USD | 0.00 USD | 73,600.00 USD | `-17.10%` | `288,066.70` |
| `Live` | `Long` | `0.2565` | 3,960,000.00 USD | 0.00 USD | 823.90 USD | `-16.77%` | `3,212.10` |
| `Live` | `Long` | `0.2585` | 3,950,000.00 USD | 0.00 USD | 26,200.00 USD | `-16.13%` | `101,365.50` |
| `Live` | `Long` | `0.2595` | 3,930,000.00 USD | 0.00 USD | 44,370.00 USD | `-15.80%` | `170,996.10` |
| `Live` | `Long` | `0.2605` | 3,880,000.00 USD | 0.00 USD | 16,140.00 USD | `-15.48%` | `61,951.90` |
| `Live` | `Long` | `0.2615` | 3,870,000.00 USD | 0.00 USD | 81,860.00 USD | `-15.15%` | `313,049.60` |
| `Live` | `Long` | `0.2625` | 3,790,000.00 USD | 0.00 USD | 468.30 USD | `-14.83%` | `1,784.00` |
| `Live` | `Long` | `0.2635` | 3,790,000.00 USD | 0.00 USD | 25,940.00 USD | `-14.50%` | `98,443.80` |
| `Live` | `Long` | `0.2645` | 3,760,000.00 USD | 0.00 USD | 104,970.00 USD | `-14.18%` | `396,854.30` |
| `Live` | `Long` | `0.2655` | 3,650,000.00 USD | 0.00 USD | 39,280.00 USD | `-13.85%` | `147,941.60` |
| `Live` | `Long` | `0.2665` | 3,610,000.00 USD | 0.00 USD | 26,710.00 USD | `-13.53%` | `100,206.40` |
| `Live` | `Long` | `0.2675` | 3,590,000.00 USD | 0.00 USD | 15,220.00 USD | `-13.21%` | `56,912.40` |
| `Live` | `Long` | `0.2685` | 3,570,000.00 USD | 0.00 USD | 42,530.00 USD | `-12.88%` | `158,390.10` |
| `Live` | `Long` | `0.2695` | 3,530,000.00 USD | 0.00 USD | 212,800.00 USD | `-12.56%` | `789,617.00` |
| `Live` | `Long` | `0.2705` | 3,320,000.00 USD | 0.00 USD | 28,770.00 USD | `-12.23%` | `106,376.70` |
| `Live` | `Long` | `0.2715` | 3,290,000.00 USD | 0.00 USD | 43,600.00 USD | `-11.91%` | `160,573.10` |
| `Live` | `Long` | `0.2725` | 3,250,000.00 USD | 0.00 USD | 8,770.00 USD | `-11.58%` | `32,190.70` |
| `Live` | `Long` | `0.2735` | 3,240,000.00 USD | 0.00 USD | 29,940.00 USD | `-11.26%` | `109,487.20` |
| `Live` | `Long` | `0.2745` | 3,210,000.00 USD | 0.00 USD | 442,080.00 USD | `-10.93%` | `1,610,485.00` |
| `Live` | `Long` | `0.2755` | 2,760,000.00 USD | 0.00 USD | 30,910.00 USD | `-10.61%` | `112,213.90` |
| `Live` | `Long` | `0.2765` | 2,730,000.00 USD | 0.00 USD | 6,580.00 USD | `-10.29%` | `23,799.30` |
| `Live` | `Long` | `0.2775` | 2,730,000.00 USD | 0.00 USD | 56,210.00 USD | `-9.96%` | `202,548.60` |
| `Live` | `Long` | `0.2785` | 2,670,000.00 USD | 0.00 USD | 3,950.00 USD | `-9.64%` | `14,195.20` |
| `Live` | `Long` | `0.2795` | 2,670,000.00 USD | 0.00 USD | 40,110.00 USD | `-9.31%` | `143,490.40` |
| `Live` | `Long` | `0.2805` | 2,630,000.00 USD | 0.00 USD | 53,850.00 USD | `-8.99%` | `191,973.80` |
| `Live` | `Long` | `0.2815` | 2,570,000.00 USD | 0.00 USD | 410,250.00 USD | `-8.66%` | `1,457,373.60` |
| `Live` | `Long` | `0.2825` | 2,160,000.00 USD | 0.00 USD | 260,250.00 USD | `-8.34%` | `921,226.50` |
| `Live` | `Long` | `0.2835` | 1,900,000.00 USD | 0.00 USD | 167,190.00 USD | `-8.01%` | `589,751.20` |
| `Live` | `Long` | `0.2845` | 1,740,000.00 USD | 0.00 USD | 21,530.00 USD | `-7.69%` | `75,669.80` |
| `Live` | `Long` | `0.2855` | 1,710,000.00 USD | 0.00 USD | 215,740.00 USD | `-7.37%` | `755,640.90` |
| `Live` | `Long` | `0.2865` | 1,500,000.00 USD | 0.00 USD | 50,450.00 USD | `-7.04%` | `176,098.30` |
| `Live` | `Long` | `0.2875` | 1,450,000.00 USD | 0.00 USD | 126,000.00 USD | `-6.72%` | `438,267.20` |
| `Live` | `Long` | `0.2885` | 1,320,000.00 USD | 0.00 USD | 239,420.00 USD | `-6.39%` | `829,885.90` |
| `Live` | `Long` | `0.2895` | 1,080,000.00 USD | 0.00 USD | 299,110.00 USD | `-6.07%` | `1,033,182.40` |
| `Live` | `Long` | `0.2905` | 782,970.00 USD | 0.00 USD | 356,530.00 USD | `-5.74%` | `1,227,287.30` |
| `Live` | `Long` | `0.2915` | 426,450.00 USD | 0.00 USD | 46,990.00 USD | `-5.42%` | `161,186.60` |
| `Live` | `Long` | `0.2925` | 379,460.00 USD | 0.00 USD | 55,810.00 USD | `-5.09%` | `190,818.30` |
| `Live` | `Long` | `0.2935` | 323,650.00 USD | 0.00 USD | 68,200.00 USD | `-4.77%` | `232,376.00` |
| `Live` | `Long` | `0.2945` | 255,440.00 USD | 0.00 USD | 10,990.00 USD | `-4.45%` | `37,302.60` |
| `Live` | `Long` | `0.2955` | 244,460.00 USD | 0.00 USD | 37,340.00 USD | `-4.12%` | `126,367.90` |
| `Live` | `Long` | `0.2965` | 207,120.00 USD | 0.00 USD | 25,390.00 USD | `-3.80%` | `85,644.70` |
| `Live` | `Long` | `0.2975` | 181,720.00 USD | 0.00 USD | 25,610.00 USD | `-3.47%` | `86,094.10` |
| `Live` | `Long` | `0.2985` | 156,110.00 USD | 0.00 USD | 102,350.00 USD | `-3.15%` | `342,890.40` |
| `Live` | `Long` | `0.2995` | 53,760.00 USD | 0.00 USD | 850.85 USD | `-2.82%` | `2,840.90` |
| `Live` | `Short` | `0.3005` | 2,100.00 USD | 2,100.00 USD | 0.00 USD | `-2.50%` | `7,001.10` |
| `Live` | `Long` | `0.3015` | 52,910.00 USD | 0.00 USD | 4,260.00 USD | `-2.17%` | `14,122.10` |
| `Live` | `Long` | `0.3075` | 48,650.00 USD | 0.00 USD | 48,650.00 USD | `-0.23%` | `158,209.00` |
| `Live` | `Short` | `0.3195` | 4,380.00 USD | 2,270.00 USD | 0.00 USD | `+3.67%` | `7,113.30` |
| `Live` | `Short` | `0.3255` | 4,730.00 USD | 352.26 USD | 0.00 USD | `+5.61%` | `1,082.20` |
| `Live` | `Short` | `0.3265` | 9,870.00 USD | 5,140.00 USD | 0.00 USD | `+5.94%` | `15,746.40` |
| `Live` | `Short` | `0.3295` | 24,220.00 USD | 14,350.00 USD | 0.00 USD | `+6.91%` | `43,543.60` |
| `Live` | `Short` | `0.3485` | 24,630.00 USD | 413.95 USD | 0.00 USD | `+13.08%` | `1,187.80` |
| `Live` | `Short` | `0.3545` | 25,080.00 USD | 446.07 USD | 0.00 USD | `+15.02%` | `1,258.30` |
| `Live` | `Short` | `0.3575` | 25,180.00 USD | 100.14 USD | 0.00 USD | `+16.00%` | `280.10` |
| `Live` | `Short` | `0.3625` | 27,270.00 USD | 2,100.00 USD | 0.00 USD | `+17.62%` | `5,784.00` |
| `Live` | `Short` | `0.3675` | 29,370.00 USD | 2,100.00 USD | 0.00 USD | `+19.24%` | `5,705.10` |
| `Live` | `Short` | `0.3885` | 29,470.00 USD | 103.81 USD | 0.00 USD | `+26.05%` | `267.20` |
| `Live` | `Short` | `0.4025` | 29,950.00 USD | 477.49 USD | 0.00 USD | `+30.60%` | `1,186.30` |
| `Live` | `Short` | `0.4035` | 30,190.00 USD | 236.85 USD | 0.00 USD | `+30.92%` | `587.00` |
| `Live` | `Short` | `0.4205` | 31,880.00 USD | 1,700.00 USD | 0.00 USD | `+36.44%` | `4,032.60` |
| `Live` | `Short` | `0.4245` | 32,000.00 USD | 115.25 USD | 0.00 USD | `+37.74%` | `271.50` |
| `Live` | `Short` | `0.4445` | 32,890.00 USD | 889.00 USD | 0.00 USD | `+44.22%` | `2,000.00` |
| `Live` | `Short` | `0.4465` | 33,270.00 USD | 379.44 USD | 0.00 USD | `+44.87%` | `849.80` |
| `Live` | `Short` | `0.4575` | 44,770.00 USD | 11,500.00 USD | 0.00 USD | `+48.44%` | `25,133.80` |
| `Live` | `Short` | `0.4945` | 405,260.00 USD | 360,490.00 USD | 0.00 USD | `+60.45%` | `729,000.00` |
| `Live` | `Short` | `0.4995` | 406,860.00 USD | 1,600.00 USD | 0.00 USD | `+62.07%` | `3,205.50` |
| `Live` | `Short` | `0.5015` | 407,020.00 USD | 160.23 USD | 0.00 USD | `+62.72%` | `319.50` |
| `Live` | `Short` | `0.5155` | 407,450.00 USD | 428.28 USD | 0.00 USD | `+67.26%` | `830.80` |
| `Live` | `Short` | `0.5185` | 469,670.00 USD | 62,220.00 USD | 0.00 USD | `+68.23%` | `120,000.00` |
| `Live` | `Short` | `0.5315` | 484,180.00 USD | 14,510.00 USD | 0.00 USD | `+72.45%` | `27,300.00` |
| `Live` | `Short` | `0.5565` | 487,040.00 USD | 2,860.00 USD | 0.00 USD | `+80.56%` | `5,135.90` |
| `Live` | `Short` | `0.5835` | 504,430.00 USD | 17,400.00 USD | 0.00 USD | `+89.33%` | `29,816.80` |

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
  * Current Rate: `2.18K` | Last 24h: `14.14K` | Last 3d: `34.03K` | Last 7d: `51.20K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0033%` | **USDT OKX** | `0.0056%` |
| **USDT Bybit** | `0.0032%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0057%` | **USDT BingX** | `0.0100%` |
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
| `5m` | 670.35 USD | 0.00 USD | **`ACCUMULATION`** |
| `15m` | 26,190.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `30m` | 36,340.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `1h` | 81,420.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `2h` | 156,820.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `4h` | -121,950.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `6h` | -372,850.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `8h` | -373,340.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `12h` | -223,250.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `24h` | -358,690.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1w` | -1,870,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,890,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+670.35` | 15m=`+26.19K` | 1h=`+81.42K` | 24h=`-358.69K`
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
  * `2026-10-30 04:15:34 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:40:34 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:34 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.2960` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.2565` (Risk Distance: `0.0460` pts)
  * +2.5R Take Profit: `0.4110`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3010` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3405` (Risk Distance: `0.0460` pts)
  * +2.5R Take Profit: `0.1860`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3110`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
