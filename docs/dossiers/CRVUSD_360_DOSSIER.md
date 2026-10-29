# 🏛️ SOVEREIGN CANDIDATE DOSSIER: CRVUSD
**Canonical Key**: `CRVUSD` | **Broker Instrument**: `CRVUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 04:04:42 IST` (`2026-10-29 22:34:42 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3000` | **Live Ask Quote**: `0.3230` | **Mid Price**: `0.3115`
- **Spread Points**: `23.00` | **Spread BPS**: `738.36 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3131` | VWAP Z-Score: `-2.15` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0044` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `22.92` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3369` | Lower -3.00σ Band: `0.2892`
  * Upper +2.51σ Band: `0.3330` | Lower -2.51σ Band: `0.2931`
  * Upper +2.01σ Band: `0.3291` | Lower -2.01σ Band: `0.2971`
  * Upper +2.00σ Band: `0.3290` | Lower -2.00σ Band: `0.2972`
  * Upper +1.28σ Band: `0.3233` | Lower -1.28σ Band: `0.3029`
  * Upper +1.00σ Band: `0.3210` | Lower -1.00σ Band: `0.3051`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3010` | EMA-20=`0.3066` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3122` (Slope: `+0.0000`) | EMA-100=`0.3158`
  * Institutional Anchors: EMA-144=`0.3176` | EMA-200=`0.3193` (Slope: `-0.6093`) | EMA-233=`0.3204`
- **Range Boundaries**: 24H High=`0.3290` | 24H Low=`0.2890` | Weekly High=`0.3340` | Weekly Low=`0.2890`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3020` (Distance: `+3.29%`)
  * Point of Control (POC) = `0.3010` (Distance: `+3.64%`)
  * Value Area Low (VAL) = `0.2960` (Distance: `+5.44%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3230` | POC=`0.3160` | VAL=`0.3100`
  * Prior Day Extremes: PDH=`0.3330` | PDL=`0.2890` | PDC=`0.2980`
  * Monday Range Blueprint: High=`0.3430` | Mid=`0.3340` | Low=`0.3250`
  * Developing Weekly Value Area: Weekly VAH=`0.3390` | Weekly POC=`0.3290` | Weekly VAL=`0.3200`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3040` | Low=`0.2930`
  * London Session (08:00-16:00 UTC): High=`0.3127` | Low=`0.3103`
  * New York Session (13:00-21:00 UTC): High=`0.3134` | Low=`0.3096`
  * Initial Balance (First Hour): IB High=`0.3124` | IB Low=`0.3106`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3103` - `0.3127`
  * Optimal Trade Entry (OTE 0.705): `0.3121`
  * Structural Invalidation Anchor (0.786): `0.3140`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:55:39 IST` |

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
| `Live` | `Long Liquidation` | `0.0655` | 492.18 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 447.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 2,330.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 4,090.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 834.95 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 485.44 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 4,510.00 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 2,510.00 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 592.74 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 1,360.00 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 116.35 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 4,300.00 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 613.05 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 689.70 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 1,060.00 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 60,830.00 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 1,340.00 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 4,930.00 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 22,280.00 USD | 5,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 464.68 USD | 5,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 4,670.00 USD | 5,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 1,530.00 USD | 5,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 14,130.00 USD | 5,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1785` | 12,010.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 13,180.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1805` | 16,880.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1835` | 3,670.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1845` | 1,480.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1865` | 9,460.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 13,340.00 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1885` | 1,660.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1895` | 8,630.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1905` | 1,230.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1925` | 10,350.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1935` | 7,950.00 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1955` | 15,480.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1965` | 589.50 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1985` | 32,860.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 146,570.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2025` | 1,140.00 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 18,380.00 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2055` | 33,460.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2085` | 2,390.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2125` | 30,270.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 2,590.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 436.01 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 131,350.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2215` | 25,340.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 10,890.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 2,650.00 USD | 4,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2255` | 676.50 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2275` | 6,670.00 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2285` | 2,780.00 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 498.24 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 45,160.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 19,620.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 10,270.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 7,780.00 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 10,540.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 24,830.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 98,180.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2395` | 7,680.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 13,650.00 USD | 4,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2415` | 21,530.00 USD | 4,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 129,460.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 19,800.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 243.99 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 23,020.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 18,230.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 4,030.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2495` | 28,490.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 151,180.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2515` | 6,290.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2525` | 150,950.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2545` | 22,030.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 73,600.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 823.90 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 26,200.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 40,390.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 91,220.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 36,620.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 126.21 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 42,940.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 120,180.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 39,280.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 35,520.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 15,220.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 29,620.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2695` | 9,630.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2705` | 8,490.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2715` | 43,600.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2725` | 2,420.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 28,290.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 440,470.00 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 50,200.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2765` | 317,370.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2775` | 56,210.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 3,950.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 40,110.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 53,580.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 95,980.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 256,870.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2835` | 326,470.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2845` | 12,500.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 168,090.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2865` | 286,740.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2875` | 132,510.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 304,540.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2895` | 231,410.00 USD | 971,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 388,500.00 USD | 739,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 48,960.00 USD | 351,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2925` | 36,680.00 USD | 302,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2935` | 19,500.00 USD | 265,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 37,890.00 USD | 245,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2955` | 34,870.00 USD | 208,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2965` | 25,390.00 USD | 173,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2975` | 26,620.00 USD | 147,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2985` | 105,090.00 USD | 121,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2995` | 2,450.00 USD | 16,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3005` | 6,870.00 USD | 13,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3015` | 4,260.00 USD | 6,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3025` | 2,530.00 USD | 2,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3125` | 10,740.00 USD | 10,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3155` | 2,110.00 USD | 12,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3245` | 13,580.00 USD | 26,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3255` | 10,670.00 USD | 37,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3265` | 2,690.00 USD | 39,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3325` | 16,340.00 USD | 56,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3335` | 2,990.00 USD | 59,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3425` | 12,100.00 USD | 71,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3575` | 100.14 USD | 71,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 2,100.00 USD | 73,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3675` | 2,100.00 USD | 75,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3885` | 103.81 USD | 75,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4025` | 477.49 USD | 76,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4035` | 716.13 USD | 76,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4205` | 1,700.00 USD | 78,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4245` | 115.25 USD | 78,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4445` | 889.00 USD | 79,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4465` | 379.44 USD | 79,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4575` | 11,500.00 USD | 91,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4825` | 1,550.00 USD | 92,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4995` | 364,140.00 USD | 457,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5015` | 160.23 USD | 457,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5155` | 428.28 USD | 457,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5175` | 62,100.00 USD | 519,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5315` | 14,510.00 USD | 534,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5565` | 2,860.00 USD | 537,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5835` | 17,400.00 USD | 554,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0655` | 5,670,000.00 USD | 0.00 USD | 492.18 USD | `-78.66%` | `7,514.20` |
| `Live` | `Long` | `0.0745` | 5,670,000.00 USD | 0.00 USD | 447.00 USD | `-75.73%` | `6,000.00` |
| `Live` | `Long` | `0.0785` | 5,670,000.00 USD | 0.00 USD | 2,330.00 USD | `-74.43%` | `29,622.60` |
| `Live` | `Long` | `0.0805` | 5,670,000.00 USD | 0.00 USD | 4,090.00 USD | `-73.78%` | `50,846.60` |
| `Live` | `Long` | `0.0855` | 5,670,000.00 USD | 0.00 USD | 834.95 USD | `-72.15%` | `9,765.50` |
| `Live` | `Long` | `0.0865` | 5,670,000.00 USD | 0.00 USD | 485.44 USD | `-71.82%` | `5,612.00` |
| `Live` | `Long` | `0.0945` | 5,660,000.00 USD | 0.00 USD | 4,510.00 USD | `-69.22%` | `47,700.00` |
| `Live` | `Long` | `0.1005` | 5,660,000.00 USD | 0.00 USD | 2,510.00 USD | `-67.26%` | `25,000.00` |
| `Live` | `Long` | `0.1135` | 5,660,000.00 USD | 0.00 USD | 592.74 USD | `-63.03%` | `5,222.40` |
| `Live` | `Long` | `0.1155` | 5,660,000.00 USD | 0.00 USD | 1,360.00 USD | `-62.38%` | `11,739.70` |
| `Live` | `Long` | `0.1225` | 5,660,000.00 USD | 0.00 USD | 116.35 USD | `-60.10%` | `949.80` |
| `Live` | `Long` | `0.1255` | 5,660,000.00 USD | 0.00 USD | 4,300.00 USD | `-59.12%` | `34,264.40` |
| `Live` | `Long` | `0.1285` | 5,650,000.00 USD | 0.00 USD | 613.05 USD | `-58.14%` | `4,770.80` |
| `Live` | `Long` | `0.1295` | 5,650,000.00 USD | 0.00 USD | 689.70 USD | `-57.82%` | `5,325.90` |
| `Live` | `Long` | `0.1315` | 5,650,000.00 USD | 0.00 USD | 1,060.00 USD | `-57.16%` | `8,042.60` |
| `Live` | `Long` | `0.1565` | 5,650,000.00 USD | 0.00 USD | 60,830.00 USD | `-49.02%` | `388,690.50` |
| `Live` | `Long` | `0.1645` | 5,590,000.00 USD | 0.00 USD | 1,340.00 USD | `-46.42%` | `8,141.90` |
| `Live` | `Long` | `0.1665` | 5,590,000.00 USD | 0.00 USD | 4,930.00 USD | `-45.76%` | `29,616.80` |
| `Live` | `Long` | `0.1685` | 5,580,000.00 USD | 0.00 USD | 22,280.00 USD | `-45.11%` | `132,229.20` |
| `Live` | `Long` | `0.1715` | 5,560,000.00 USD | 0.00 USD | 464.68 USD | `-44.13%` | `2,709.50` |
| `Live` | `Long` | `0.1725` | 5,560,000.00 USD | 0.00 USD | 4,670.00 USD | `-43.81%` | `27,059.00` |
| `Live` | `Long` | `0.1765` | 5,550,000.00 USD | 0.00 USD | 1,530.00 USD | `-42.51%` | `8,680.50` |
| `Live` | `Long` | `0.1775` | 5,550,000.00 USD | 0.00 USD | 14,130.00 USD | `-42.18%` | `79,610.90` |
| `Live` | `Long` | `0.1785` | 5,540,000.00 USD | 0.00 USD | 12,010.00 USD | `-41.85%` | `67,270.30` |
| `Live` | `Long` | `0.1795` | 5,530,000.00 USD | 0.00 USD | 13,180.00 USD | `-41.53%` | `73,444.60` |
| `Live` | `Long` | `0.1805` | 5,510,000.00 USD | 0.00 USD | 16,880.00 USD | `-41.20%` | `93,542.70` |
| `Live` | `Long` | `0.1835` | 5,500,000.00 USD | 0.00 USD | 3,670.00 USD | `-40.23%` | `19,976.00` |
| `Live` | `Long` | `0.1845` | 5,490,000.00 USD | 0.00 USD | 1,480.00 USD | `-39.90%` | `8,024.00` |
| `Live` | `Long` | `0.1865` | 5,490,000.00 USD | 0.00 USD | 9,460.00 USD | `-39.25%` | `50,699.40` |
| `Live` | `Long` | `0.1875` | 5,480,000.00 USD | 0.00 USD | 13,340.00 USD | `-38.92%` | `71,135.10` |
| `Live` | `Long` | `0.1885` | 5,470,000.00 USD | 0.00 USD | 1,660.00 USD | `-38.60%` | `8,802.20` |
| `Live` | `Long` | `0.1895` | 5,470,000.00 USD | 0.00 USD | 8,630.00 USD | `-38.27%` | `45,539.20` |
| `Live` | `Long` | `0.1905` | 5,460,000.00 USD | 0.00 USD | 1,230.00 USD | `-37.95%` | `6,482.00` |
| `Live` | `Long` | `0.1925` | 5,460,000.00 USD | 0.00 USD | 10,350.00 USD | `-37.29%` | `53,752.80` |
| `Live` | `Long` | `0.1935` | 5,450,000.00 USD | 0.00 USD | 7,950.00 USD | `-36.97%` | `41,110.40` |
| `Live` | `Long` | `0.1955` | 5,440,000.00 USD | 0.00 USD | 15,480.00 USD | `-36.32%` | `79,182.40` |
| `Live` | `Long` | `0.1965` | 5,420,000.00 USD | 0.00 USD | 589.50 USD | `-35.99%` | `3,000.00` |
| `Live` | `Long` | `0.1985` | 5,420,000.00 USD | 0.00 USD | 32,860.00 USD | `-35.34%` | `165,563.00` |
| `Live` | `Long` | `0.1995` | 5,390,000.00 USD | 0.00 USD | 146,570.00 USD | `-35.01%` | `734,702.60` |
| `Live` | `Long` | `0.2025` | 5,240,000.00 USD | 0.00 USD | 1,140.00 USD | `-34.04%` | `5,614.00` |
| `Live` | `Long` | `0.2045` | 5,240,000.00 USD | 0.00 USD | 18,380.00 USD | `-33.39%` | `89,877.80` |
| `Live` | `Long` | `0.2055` | 5,220,000.00 USD | 0.00 USD | 33,460.00 USD | `-33.06%` | `162,833.60` |
| `Live` | `Long` | `0.2085` | 5,190,000.00 USD | 0.00 USD | 2,390.00 USD | `-32.08%` | `11,465.50` |
| `Live` | `Long` | `0.2125` | 5,190,000.00 USD | 0.00 USD | 30,270.00 USD | `-30.78%` | `142,451.90` |
| `Live` | `Long` | `0.2175` | 5,160,000.00 USD | 0.00 USD | 2,590.00 USD | `-29.15%` | `11,899.40` |
| `Live` | `Long` | `0.2195` | 5,160,000.00 USD | 0.00 USD | 436.01 USD | `-28.50%` | `1,986.40` |
| `Live` | `Long` | `0.2205` | 5,150,000.00 USD | 0.00 USD | 131,350.00 USD | `-28.17%` | `595,704.50` |
| `Live` | `Long` | `0.2215` | 5,020,000.00 USD | 0.00 USD | 25,340.00 USD | `-27.85%` | `114,401.60` |
| `Live` | `Long` | `0.2225` | 5,000,000.00 USD | 0.00 USD | 10,890.00 USD | `-27.52%` | `48,931.80` |
| `Live` | `Long` | `0.2245` | 4,990,000.00 USD | 0.00 USD | 2,650.00 USD | `-26.87%` | `11,823.00` |
| `Live` | `Long` | `0.2255` | 4,980,000.00 USD | 0.00 USD | 676.50 USD | `-26.54%` | `3,000.00` |
| `Live` | `Long` | `0.2275` | 4,980,000.00 USD | 0.00 USD | 6,670.00 USD | `-25.89%` | `29,332.10` |
| `Live` | `Long` | `0.2285` | 4,980,000.00 USD | 0.00 USD | 2,780.00 USD | `-25.57%` | `12,174.10` |
| `Live` | `Long` | `0.2295` | 4,970,000.00 USD | 0.00 USD | 498.24 USD | `-25.24%` | `2,171.00` |
| `Live` | `Long` | `0.2305` | 4,970,000.00 USD | 0.00 USD | 45,160.00 USD | `-24.92%` | `195,912.20` |
| `Live` | `Long` | `0.2315` | 4,930,000.00 USD | 0.00 USD | 19,620.00 USD | `-24.59%` | `84,743.40` |
| `Live` | `Long` | `0.2325` | 4,910,000.00 USD | 0.00 USD | 10,270.00 USD | `-24.26%` | `44,170.10` |
| `Live` | `Long` | `0.2335` | 4,900,000.00 USD | 0.00 USD | 7,780.00 USD | `-23.94%` | `33,326.10` |
| `Live` | `Long` | `0.2355` | 4,890,000.00 USD | 0.00 USD | 10,540.00 USD | `-23.29%` | `44,770.40` |
| `Live` | `Long` | `0.2375` | 4,880,000.00 USD | 0.00 USD | 24,830.00 USD | `-22.64%` | `104,554.80` |
| `Live` | `Long` | `0.2385` | 4,860,000.00 USD | 0.00 USD | 98,180.00 USD | `-22.31%` | `411,666.40` |
| `Live` | `Long` | `0.2395` | 4,760,000.00 USD | 0.00 USD | 7,680.00 USD | `-21.98%` | `32,081.10` |
| `Live` | `Long` | `0.2405` | 4,750,000.00 USD | 0.00 USD | 13,650.00 USD | `-21.66%` | `56,745.50` |
| `Live` | `Long` | `0.2415` | 4,740,000.00 USD | 0.00 USD | 21,530.00 USD | `-21.33%` | `89,135.40` |
| `Live` | `Long` | `0.2425` | 4,710,000.00 USD | 0.00 USD | 129,460.00 USD | `-21.01%` | `533,874.30` |
| `Live` | `Long` | `0.2435` | 4,590,000.00 USD | 0.00 USD | 19,800.00 USD | `-20.68%` | `81,305.00` |
| `Live` | `Long` | `0.2445` | 4,570,000.00 USD | 0.00 USD | 243.99 USD | `-20.36%` | `997.90` |
| `Live` | `Long` | `0.2455` | 4,560,000.00 USD | 0.00 USD | 23,020.00 USD | `-20.03%` | `93,774.40` |
| `Live` | `Long` | `0.2475` | 4,540,000.00 USD | 0.00 USD | 18,230.00 USD | `-19.38%` | `73,640.00` |
| `Live` | `Long` | `0.2485` | 4,520,000.00 USD | 0.00 USD | 4,030.00 USD | `-19.05%` | `16,203.80` |
| `Live` | `Long` | `0.2495` | 4,520,000.00 USD | 0.00 USD | 28,490.00 USD | `-18.73%` | `114,195.30` |
| `Live` | `Long` | `0.2505` | 4,490,000.00 USD | 0.00 USD | 151,180.00 USD | `-18.40%` | `603,515.90` |
| `Live` | `Long` | `0.2515` | 4,340,000.00 USD | 0.00 USD | 6,290.00 USD | `-18.08%` | `25,000.00` |
| `Live` | `Long` | `0.2525` | 4,330,000.00 USD | 0.00 USD | 150,950.00 USD | `-17.75%` | `597,827.70` |
| `Live` | `Long` | `0.2545` | 4,180,000.00 USD | 0.00 USD | 22,030.00 USD | `-17.10%` | `86,545.50` |
| `Live` | `Long` | `0.2555` | 4,160,000.00 USD | 0.00 USD | 73,600.00 USD | `-16.77%` | `288,066.70` |
| `Live` | `Long` | `0.2565` | 4,090,000.00 USD | 0.00 USD | 823.90 USD | `-16.45%` | `3,212.10` |
| `Live` | `Long` | `0.2585` | 4,090,000.00 USD | 0.00 USD | 26,200.00 USD | `-15.80%` | `101,365.50` |
| `Live` | `Long` | `0.2595` | 4,060,000.00 USD | 0.00 USD | 40,390.00 USD | `-15.47%` | `155,658.20` |
| `Live` | `Long` | `0.2605` | 4,020,000.00 USD | 0.00 USD | 91,220.00 USD | `-15.14%` | `350,162.10` |
| `Live` | `Long` | `0.2615` | 3,930,000.00 USD | 0.00 USD | 36,620.00 USD | `-14.82%` | `140,043.00` |
| `Live` | `Long` | `0.2625` | 3,890,000.00 USD | 0.00 USD | 126.21 USD | `-14.49%` | `480.80` |
| `Live` | `Long` | `0.2635` | 3,890,000.00 USD | 0.00 USD | 42,940.00 USD | `-14.17%` | `162,959.80` |
| `Live` | `Long` | `0.2645` | 3,850,000.00 USD | 0.00 USD | 120,180.00 USD | `-13.84%` | `454,373.30` |
| `Live` | `Long` | `0.2655` | 3,730,000.00 USD | 0.00 USD | 39,280.00 USD | `-13.52%` | `147,941.60` |
| `Live` | `Long` | `0.2665` | 3,690,000.00 USD | 0.00 USD | 35,520.00 USD | `-13.19%` | `133,291.50` |
| `Live` | `Long` | `0.2675` | 3,650,000.00 USD | 0.00 USD | 15,220.00 USD | `-12.86%` | `56,912.40` |
| `Live` | `Long` | `0.2685` | 3,640,000.00 USD | 0.00 USD | 29,620.00 USD | `-12.54%` | `110,305.00` |
| `Live` | `Long` | `0.2695` | 3,610,000.00 USD | 0.00 USD | 9,630.00 USD | `-12.21%` | `35,746.50` |
| `Live` | `Long` | `0.2705` | 3,600,000.00 USD | 0.00 USD | 8,490.00 USD | `-11.89%` | `31,376.70` |
| `Live` | `Long` | `0.2715` | 3,590,000.00 USD | 0.00 USD | 43,600.00 USD | `-11.56%` | `160,573.10` |
| `Live` | `Long` | `0.2725` | 3,550,000.00 USD | 0.00 USD | 2,420.00 USD | `-11.23%` | `8,894.10` |
| `Live` | `Long` | `0.2735` | 3,540,000.00 USD | 0.00 USD | 28,290.00 USD | `-10.91%` | `103,421.10` |
| `Live` | `Long` | `0.2745` | 3,520,000.00 USD | 0.00 USD | 440,470.00 USD | `-10.58%` | `1,604,642.10` |
| `Live` | `Long` | `0.2755` | 3,080,000.00 USD | 0.00 USD | 50,200.00 USD | `-10.26%` | `182,213.90` |
| `Live` | `Long` | `0.2765` | 3,030,000.00 USD | 0.00 USD | 317,370.00 USD | `-9.93%` | `1,147,799.30` |
| `Live` | `Long` | `0.2775` | 2,710,000.00 USD | 0.00 USD | 56,210.00 USD | `-9.61%` | `202,548.60` |
| `Live` | `Long` | `0.2785` | 2,650,000.00 USD | 0.00 USD | 3,950.00 USD | `-9.28%` | `14,195.20` |
| `Live` | `Long` | `0.2795` | 2,650,000.00 USD | 0.00 USD | 40,110.00 USD | `-8.95%` | `143,490.40` |
| `Live` | `Long` | `0.2805` | 2,610,000.00 USD | 0.00 USD | 53,580.00 USD | `-8.63%` | `191,019.70` |
| `Live` | `Long` | `0.2815` | 2,550,000.00 USD | 0.00 USD | 95,980.00 USD | `-8.30%` | `340,947.20` |
| `Live` | `Long` | `0.2825` | 2,460,000.00 USD | 0.00 USD | 256,870.00 USD | `-7.98%` | `909,286.50` |
| `Live` | `Long` | `0.2835` | 2,200,000.00 USD | 0.00 USD | 326,470.00 USD | `-7.65%` | `1,151,572.00` |
| `Live` | `Long` | `0.2845` | 1,880,000.00 USD | 0.00 USD | 12,500.00 USD | `-7.33%` | `43,919.50` |
| `Live` | `Long` | `0.2855` | 1,860,000.00 USD | 0.00 USD | 168,090.00 USD | `-7.00%` | `588,746.90` |
| `Live` | `Long` | `0.2865` | 1,690,000.00 USD | 0.00 USD | 286,740.00 USD | `-6.67%` | `1,000,822.20` |
| `Live` | `Long` | `0.2875` | 1,410,000.00 USD | 0.00 USD | 132,510.00 USD | `-6.35%` | `460,907.30` |
| `Live` | `Long` | `0.2885` | 1,280,000.00 USD | 0.00 USD | 304,540.00 USD | `-6.02%` | `1,055,594.00` |
| `Live` | `Long` | `0.2895` | 971,020.00 USD | 0.00 USD | 231,410.00 USD | `-5.70%` | `799,354.50` |
| `Live` | `Long` | `0.2905` | 739,610.00 USD | 0.00 USD | 388,500.00 USD | `-5.37%` | `1,337,342.70` |
| `Live` | `Long` | `0.2915` | 351,110.00 USD | 0.00 USD | 48,960.00 USD | `-5.05%` | `167,946.30` |
| `Live` | `Long` | `0.2925` | 302,150.00 USD | 0.00 USD | 36,680.00 USD | `-4.72%` | `125,410.00` |
| `Live` | `Long` | `0.2935` | 265,470.00 USD | 0.00 USD | 19,500.00 USD | `-4.39%` | `66,438.40` |
| `Live` | `Long` | `0.2945` | 245,970.00 USD | 0.00 USD | 37,890.00 USD | `-4.07%` | `128,657.50` |
| `Live` | `Long` | `0.2955` | 208,080.00 USD | 0.00 USD | 34,870.00 USD | `-3.74%` | `117,988.20` |
| `Live` | `Long` | `0.2965` | 173,220.00 USD | 0.00 USD | 25,390.00 USD | `-3.42%` | `85,644.70` |
| `Live` | `Long` | `0.2975` | 147,820.00 USD | 0.00 USD | 26,620.00 USD | `-3.09%` | `89,479.50` |
| `Live` | `Long` | `0.2985` | 121,200.00 USD | 0.00 USD | 105,090.00 USD | `-2.77%` | `352,057.70` |
| `Live` | `Long` | `0.2995` | 16,110.00 USD | 0.00 USD | 2,450.00 USD | `-2.44%` | `8,196.60` |
| `Live` | `Long` | `0.3005` | 13,660.00 USD | 0.00 USD | 6,870.00 USD | `-2.11%` | `22,848.60` |
| `Live` | `Long` | `0.3015` | 6,790.00 USD | 0.00 USD | 4,260.00 USD | `-1.79%` | `14,122.10` |
| `Live` | `Long` | `0.3025` | 2,530.00 USD | 0.00 USD | 2,530.00 USD | `-1.46%` | `8,379.70` |
| `Live` | `Short` | `0.3125` | 10,740.00 USD | 10,740.00 USD | 0.00 USD | `+1.79%` | `34,377.70` |
| `Live` | `Short` | `0.3155` | 12,850.00 USD | 2,110.00 USD | 0.00 USD | `+2.77%` | `6,680.20` |
| `Live` | `Short` | `0.3245` | 26,430.00 USD | 13,580.00 USD | 0.00 USD | `+5.70%` | `41,855.30` |
| `Live` | `Short` | `0.3255` | 37,100.00 USD | 10,670.00 USD | 0.00 USD | `+6.03%` | `32,768.10` |
| `Live` | `Short` | `0.3265` | 39,790.00 USD | 2,690.00 USD | 0.00 USD | `+6.36%` | `8,239.30` |
| `Live` | `Short` | `0.3325` | 56,130.00 USD | 16,340.00 USD | 0.00 USD | `+8.31%` | `49,154.60` |
| `Live` | `Short` | `0.3335` | 59,120.00 USD | 2,990.00 USD | 0.00 USD | `+8.64%` | `8,954.10` |
| `Live` | `Short` | `0.3425` | 71,220.00 USD | 12,100.00 USD | 0.00 USD | `+11.57%` | `35,339.80` |
| `Live` | `Short` | `0.3575` | 71,320.00 USD | 100.14 USD | 0.00 USD | `+16.45%` | `280.10` |
| `Live` | `Short` | `0.3625` | 73,420.00 USD | 2,100.00 USD | 0.00 USD | `+18.08%` | `5,784.00` |
| `Live` | `Short` | `0.3675` | 75,520.00 USD | 2,100.00 USD | 0.00 USD | `+19.71%` | `5,705.10` |
| `Live` | `Short` | `0.3885` | 75,620.00 USD | 103.81 USD | 0.00 USD | `+26.55%` | `267.20` |
| `Live` | `Short` | `0.4025` | 76,100.00 USD | 477.49 USD | 0.00 USD | `+31.11%` | `1,186.30` |
| `Live` | `Short` | `0.4035` | 76,810.00 USD | 716.13 USD | 0.00 USD | `+31.44%` | `1,774.80` |
| `Live` | `Short` | `0.4205` | 78,510.00 USD | 1,700.00 USD | 0.00 USD | `+36.98%` | `4,032.60` |
| `Live` | `Short` | `0.4245` | 78,620.00 USD | 115.25 USD | 0.00 USD | `+38.28%` | `271.50` |
| `Live` | `Short` | `0.4445` | 79,510.00 USD | 889.00 USD | 0.00 USD | `+44.79%` | `2,000.00` |
| `Live` | `Short` | `0.4465` | 79,890.00 USD | 379.44 USD | 0.00 USD | `+45.44%` | `849.80` |
| `Live` | `Short` | `0.4575` | 91,390.00 USD | 11,500.00 USD | 0.00 USD | `+49.03%` | `25,133.80` |
| `Live` | `Short` | `0.4825` | 92,940.00 USD | 1,550.00 USD | 0.00 USD | `+57.17%` | `3,205.50` |
| `Live` | `Short` | `0.4995` | 457,070.00 USD | 364,140.00 USD | 0.00 USD | `+62.71%` | `729,000.00` |
| `Live` | `Short` | `0.5015` | 457,230.00 USD | 160.23 USD | 0.00 USD | `+63.36%` | `319.50` |
| `Live` | `Short` | `0.5155` | 457,660.00 USD | 428.28 USD | 0.00 USD | `+67.92%` | `830.80` |
| `Live` | `Short` | `0.5175` | 519,760.00 USD | 62,100.00 USD | 0.00 USD | `+68.57%` | `120,000.00` |
| `Live` | `Short` | `0.5315` | 534,270.00 USD | 14,510.00 USD | 0.00 USD | `+73.13%` | `27,300.00` |
| `Live` | `Short` | `0.5565` | 537,130.00 USD | 2,860.00 USD | 0.00 USD | `+81.28%` | `5,135.90` |
| `Live` | `Short` | `0.5835` | 554,530.00 USD | 17,400.00 USD | 0.00 USD | `+90.07%` | `29,816.80` |

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
  * Current Rate: `2.70K` | Last 24h: `14.14K` | Last 3d: `34.03K` | Last 7d: `51.20K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0027%` | **USDT OKX** | `0.0084%` |
| **USDT Bybit** | `0.0061%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0083%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0083%` | **USDT Bitget** | `0.0100%` |
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
| `5m` | 0.00 USD | -4,780.00 USD | **`DISTRIBUTION`** |
| `15m` | 0.00 USD | 25,240.00 USD | **`ACCUMULATION`** |
| `30m` | 0.00 USD | 336,800.00 USD | **`ACCUMULATION`** |
| `1h` | 0.00 USD | -576,690.00 USD | **`DISTRIBUTION`** |
| `2h` | 0.00 USD | -2,150,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 0.00 USD | -3,220,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 0.00 USD | -4,660,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 0.00 USD | -5,280,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 0.00 USD | -5,570,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 0.00 USD | -6,460,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 0.00 USD | -18,220,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 0.00 USD | -60,300,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`-4.78K` | 15m=`+25.24K` | 1h=`-576.69K` | 24h=`-6.46M`
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
  * `2026-10-30 03:29:36 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:00:36 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:00:36 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:59:36 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:01:36 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:01:36 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:01:36 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:36 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:36 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:36 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:01:36 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `0.2563` (Risk Distance: `0.0460` pts)
  * +2.5R Take Profit: `0.4110`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3020` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3417` (Risk Distance: `0.0460` pts)
  * +2.5R Take Profit: `0.1870`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3140`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
