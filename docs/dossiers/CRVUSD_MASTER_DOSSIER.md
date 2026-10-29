# 🏛️ SOVEREIGN CANDIDATE DOSSIER: CRVUSD
**Canonical Key**: `CRVUSD` | **Broker Instrument**: `CRVUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 03:28:19 IST` (`2026-10-29 21:58:19 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.2970` | **Live Ask Quote**: `0.3190` | **Mid Price**: `0.3080`
- **Spread Points**: `22.00` | **Spread BPS**: `714.29 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3139` | VWAP Z-Score: `-2.20` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0043` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `24.75` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3355` | Lower -3.00σ Band: `0.2922`
  * Upper +2.51σ Band: `0.3320` | Lower -2.51σ Band: `0.2957`
  * Upper +2.01σ Band: `0.3284` | Lower -2.01σ Band: `0.2994`
  * Upper +2.00σ Band: `0.3283` | Lower -2.00σ Band: `0.2994`
  * Upper +1.28σ Band: `0.3231` | Lower -1.28σ Band: `0.3046`
  * Upper +1.00σ Band: `0.3211` | Lower -1.00σ Band: `0.3066`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3038` | EMA-20=`0.3089` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3136` (Slope: `+0.0000`) | EMA-100=`0.3166`
  * Institutional Anchors: EMA-144=`0.3183` | EMA-200=`0.3198` (Slope: `-0.5250`) | EMA-233=`0.3208`
- **Range Boundaries**: 24H High=`0.3330` | 24H Low=`0.2890` | Weekly High=`0.3340` | Weekly Low=`0.2890`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3030` (Distance: `+1.63%`)
  * Point of Control (POC) = `0.3010` (Distance: `+2.34%`)
  * Value Area Low (VAL) = `0.2990` (Distance: `+3.12%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3230` | POC=`0.3160` | VAL=`0.3100`
  * Prior Day Extremes: PDH=`0.3330` | PDL=`0.2890` | PDC=`0.2980`
  * Monday Range Blueprint: High=`0.3430` | Mid=`0.3340` | Low=`0.3250`
  * Developing Weekly Value Area: Weekly VAH=`0.3380` | Weekly POC=`0.3290` | Weekly VAL=`0.3200`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3040` | Low=`0.2950`
  * London Session (08:00-16:00 UTC): High=`0.3092` | Low=`0.3068`
  * New York Session (13:00-21:00 UTC): High=`0.3098` | Low=`0.3062`
  * Initial Balance (First Hour): IB High=`0.3089` | IB Low=`0.3071`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3068` - `0.3092`
  * Optimal Trade Entry (OTE 0.705): `0.3086`
  * Structural Invalidation Anchor (0.786): `0.3105`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:25:41 IST` |

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
| `Live` | `Long Liquidation` | `0.0645` | 102.03 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 547.67 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 2,330.00 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 4,190.00 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 485.44 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 883.78 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 286.50 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 535.30 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 1,560.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 116.35 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 4,300.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 1,500.00 USD | 5,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 1,040.00 USD | 5,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1375` | 1,150.00 USD | 5,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 57,720.00 USD | 5,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 827.59 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 397.60 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 4,930.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 813.42 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 464.68 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 4,670.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 1,530.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 14,130.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1785` | 12,010.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 13,180.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1805` | 16,880.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1835` | 179.10 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1845` | 4,990.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1865` | 9,460.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 5,840.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1885` | 10,530.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1895` | 8,910.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1905` | 952.50 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1925` | 8,990.00 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1935` | 2,150.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1945` | 5,830.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1955` | 13,190.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1985` | 1,100.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 178,490.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2025` | 781.97 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2035` | 356.61 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 18,380.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2055` | 32,550.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2085` | 3,320.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2095` | 2,680.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2125` | 19,700.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2135` | 58,120.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 153.87 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 131,570.00 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2215` | 30,880.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 7,260.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2285` | 2,780.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 498.24 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 45,160.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 19,940.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 10,270.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 1,940.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 10,540.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 92,210.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 13,650.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2415` | 21,530.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 121,740.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 22,560.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 26,100.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 23,020.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 7,910.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 18,230.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 4,230.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2495` | 28,290.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 151,550.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2525` | 5,390.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2545` | 22,030.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 61,240.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 7,240.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 51,830.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 44,370.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 9,290.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 28,620.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 1,910.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 20,760.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 190,880.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 87,230.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 25,020.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 21,780.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 22,620.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2695` | 35,450.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2705` | 11,110.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2715` | 44,010.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2725` | 2,420.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 21,260.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 301,980.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 319,420.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2765` | 10,610.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2775` | 90,440.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 3,950.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 14,770.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 54,240.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 26,670.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 371,710.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2835` | 331,540.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2845` | 16,970.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 23,390.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2865` | 44,720.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2875` | 203,880.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 464,670.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2895` | 333,410.00 USD | 990,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 207,180.00 USD | 656,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 22,800.00 USD | 449,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2925` | 25,320.00 USD | 426,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2935` | 24,880.00 USD | 401,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 179,490.00 USD | 376,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2955` | 21,630.00 USD | 197,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2965` | 13,370.00 USD | 175,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2975` | 1,700.00 USD | 162,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2985` | 59,790.00 USD | 160,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2995` | 7,640.00 USD | 100,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3005` | 56,820.00 USD | 92,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3015` | 7,160.00 USD | 36,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3025` | 567.49 USD | 28,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3035` | 13,620.00 USD | 28,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3065` | 14,710.00 USD | 14,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3095` | 21,210.00 USD | 21,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 531.79 USD | 21,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3125` | 13,450.00 USD | 35,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3195` | 4,470.00 USD | 39,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3215` | 257.88 USD | 39,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3245` | 28,680.00 USD | 68,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3265` | 3,060.00 USD | 71,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3275` | 2,370.00 USD | 74,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3285` | 31,480.00 USD | 105,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 2,180.00 USD | 107,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3425` | 12,100.00 USD | 119,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3495` | 830.24 USD | 120,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3565` | 3,740.00 USD | 124,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3575` | 100.14 USD | 124,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 2,100.00 USD | 126,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3675` | 2,100.00 USD | 128,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3835` | 2,750.00 USD | 131,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3885` | 103.81 USD | 131,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4025` | 477.49 USD | 132,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4035` | 236.85 USD | 132,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4205` | 1,700.00 USD | 133,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4245` | 115.25 USD | 134,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4445` | 889.00 USD | 134,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4575` | 10,480.00 USD | 145,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4595` | 1,020.00 USD | 146,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4655` | 1,490.00 USD | 147,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5015` | 160.23 USD | 148,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5035` | 367,050.00 USD | 515,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5155` | 428.28 USD | 515,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5165` | 61,980.00 USD | 577,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5315` | 14,510.00 USD | 592,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5565` | 2,860.00 USD | 594,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5835` | 17,400.00 USD | 612,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0645` | 5,310,000.00 USD | 0.00 USD | 102.03 USD | `-79.13%` | `1,581.90` |
| `Live` | `Long` | `0.0745` | 5,310,000.00 USD | 0.00 USD | 547.67 USD | `-75.90%` | `7,351.30` |
| `Live` | `Long` | `0.0785` | 5,310,000.00 USD | 0.00 USD | 2,330.00 USD | `-74.60%` | `29,622.60` |
| `Live` | `Long` | `0.0825` | 5,310,000.00 USD | 0.00 USD | 4,190.00 USD | `-73.31%` | `50,846.60` |
| `Live` | `Long` | `0.0865` | 5,300,000.00 USD | 0.00 USD | 485.44 USD | `-72.02%` | `5,612.00` |
| `Live` | `Long` | `0.0905` | 5,300,000.00 USD | 0.00 USD | 883.78 USD | `-70.72%` | `9,765.50` |
| `Live` | `Long` | `0.0955` | 5,300,000.00 USD | 0.00 USD | 286.50 USD | `-69.10%` | `3,000.00` |
| `Live` | `Long` | `0.1025` | 5,300,000.00 USD | 0.00 USD | 535.30 USD | `-66.84%` | `5,222.40` |
| `Live` | `Long` | `0.1195` | 5,300,000.00 USD | 0.00 USD | 1,560.00 USD | `-61.34%` | `13,019.50` |
| `Live` | `Long` | `0.1225` | 5,300,000.00 USD | 0.00 USD | 116.35 USD | `-60.37%` | `949.80` |
| `Live` | `Long` | `0.1255` | 5,300,000.00 USD | 0.00 USD | 4,300.00 USD | `-59.40%` | `34,264.40` |
| `Live` | `Long` | `0.1275` | 5,290,000.00 USD | 0.00 USD | 1,500.00 USD | `-58.75%` | `11,739.70` |
| `Live` | `Long` | `0.1295` | 5,290,000.00 USD | 0.00 USD | 1,040.00 USD | `-58.10%` | `8,042.60` |
| `Live` | `Long` | `0.1375` | 5,290,000.00 USD | 0.00 USD | 1,150.00 USD | `-55.52%` | `8,365.30` |
| `Live` | `Long` | `0.1485` | 5,290,000.00 USD | 0.00 USD | 57,720.00 USD | `-51.96%` | `388,690.50` |
| `Live` | `Long` | `0.1525` | 5,230,000.00 USD | 0.00 USD | 827.59 USD | `-50.66%` | `5,426.80` |
| `Live` | `Long` | `0.1645` | 5,230,000.00 USD | 0.00 USD | 397.60 USD | `-46.78%` | `2,417.00` |
| `Live` | `Long` | `0.1665` | 5,230,000.00 USD | 0.00 USD | 4,930.00 USD | `-46.13%` | `29,616.80` |
| `Live` | `Long` | `0.1705` | 5,230,000.00 USD | 0.00 USD | 813.42 USD | `-44.84%` | `4,770.80` |
| `Live` | `Long` | `0.1715` | 5,220,000.00 USD | 0.00 USD | 464.68 USD | `-44.52%` | `2,709.50` |
| `Live` | `Long` | `0.1725` | 5,220,000.00 USD | 0.00 USD | 4,670.00 USD | `-44.19%` | `27,059.00` |
| `Live` | `Long` | `0.1765` | 5,220,000.00 USD | 0.00 USD | 1,530.00 USD | `-42.90%` | `8,680.50` |
| `Live` | `Long` | `0.1775` | 5,220,000.00 USD | 0.00 USD | 14,130.00 USD | `-42.58%` | `79,610.90` |
| `Live` | `Long` | `0.1785` | 5,200,000.00 USD | 0.00 USD | 12,010.00 USD | `-42.25%` | `67,270.30` |
| `Live` | `Long` | `0.1795` | 5,190,000.00 USD | 0.00 USD | 13,180.00 USD | `-41.93%` | `73,444.60` |
| `Live` | `Long` | `0.1805` | 5,180,000.00 USD | 0.00 USD | 16,880.00 USD | `-41.60%` | `93,542.70` |
| `Live` | `Long` | `0.1835` | 5,160,000.00 USD | 0.00 USD | 179.10 USD | `-40.63%` | `976.00` |
| `Live` | `Long` | `0.1845` | 5,160,000.00 USD | 0.00 USD | 4,990.00 USD | `-40.31%` | `27,024.00` |
| `Live` | `Long` | `0.1865` | 5,160,000.00 USD | 0.00 USD | 9,460.00 USD | `-39.66%` | `50,699.40` |
| `Live` | `Long` | `0.1875` | 5,150,000.00 USD | 0.00 USD | 5,840.00 USD | `-39.34%` | `31,135.10` |
| `Live` | `Long` | `0.1885` | 5,140,000.00 USD | 0.00 USD | 10,530.00 USD | `-39.02%` | `55,861.00` |
| `Live` | `Long` | `0.1895` | 5,130,000.00 USD | 0.00 USD | 8,910.00 USD | `-38.69%` | `47,021.20` |
| `Live` | `Long` | `0.1905` | 5,120,000.00 USD | 0.00 USD | 952.50 USD | `-38.37%` | `5,000.00` |
| `Live` | `Long` | `0.1925` | 5,120,000.00 USD | 0.00 USD | 8,990.00 USD | `-37.72%` | `46,694.00` |
| `Live` | `Long` | `0.1935` | 5,110,000.00 USD | 0.00 USD | 2,150.00 USD | `-37.40%` | `11,110.40` |
| `Live` | `Long` | `0.1945` | 5,110,000.00 USD | 0.00 USD | 5,830.00 USD | `-37.08%` | `30,000.00` |
| `Live` | `Long` | `0.1955` | 5,100,000.00 USD | 0.00 USD | 13,190.00 USD | `-36.75%` | `67,459.20` |
| `Live` | `Long` | `0.1985` | 5,090,000.00 USD | 0.00 USD | 1,100.00 USD | `-35.78%` | `5,563.00` |
| `Live` | `Long` | `0.1995` | 5,090,000.00 USD | 0.00 USD | 178,490.00 USD | `-35.46%` | `894,702.60` |
| `Live` | `Long` | `0.2025` | 4,910,000.00 USD | 0.00 USD | 781.97 USD | `-34.49%` | `3,861.60` |
| `Live` | `Long` | `0.2035` | 4,910,000.00 USD | 0.00 USD | 356.61 USD | `-34.16%` | `1,752.40` |
| `Live` | `Long` | `0.2045` | 4,910,000.00 USD | 0.00 USD | 18,380.00 USD | `-33.84%` | `89,877.80` |
| `Live` | `Long` | `0.2055` | 4,890,000.00 USD | 0.00 USD | 32,550.00 USD | `-33.52%` | `158,394.40` |
| `Live` | `Long` | `0.2085` | 4,860,000.00 USD | 0.00 USD | 3,320.00 USD | `-32.55%` | `15,904.70` |
| `Live` | `Long` | `0.2095` | 4,860,000.00 USD | 0.00 USD | 2,680.00 USD | `-32.22%` | `12,814.90` |
| `Live` | `Long` | `0.2125` | 4,850,000.00 USD | 0.00 USD | 19,700.00 USD | `-31.25%` | `92,714.90` |
| `Live` | `Long` | `0.2135` | 4,830,000.00 USD | 0.00 USD | 58,120.00 USD | `-30.93%` | `272,229.20` |
| `Live` | `Long` | `0.2195` | 4,780,000.00 USD | 0.00 USD | 153.87 USD | `-28.99%` | `701.00` |
| `Live` | `Long` | `0.2205` | 4,780,000.00 USD | 0.00 USD | 131,570.00 USD | `-28.66%` | `596,694.70` |
| `Live` | `Long` | `0.2215` | 4,640,000.00 USD | 0.00 USD | 30,880.00 USD | `-28.34%` | `139,423.00` |
| `Live` | `Long` | `0.2245` | 4,610,000.00 USD | 0.00 USD | 7,260.00 USD | `-27.37%` | `32,332.10` |
| `Live` | `Long` | `0.2285` | 4,610,000.00 USD | 0.00 USD | 2,780.00 USD | `-26.08%` | `12,174.10` |
| `Live` | `Long` | `0.2295` | 4,600,000.00 USD | 0.00 USD | 498.24 USD | `-25.75%` | `2,171.00` |
| `Live` | `Long` | `0.2305` | 4,600,000.00 USD | 0.00 USD | 45,160.00 USD | `-25.43%` | `195,912.20` |
| `Live` | `Long` | `0.2315` | 4,560,000.00 USD | 0.00 USD | 19,940.00 USD | `-25.11%` | `86,139.70` |
| `Live` | `Long` | `0.2325` | 4,540,000.00 USD | 0.00 USD | 10,270.00 USD | `-24.78%` | `44,170.10` |
| `Live` | `Long` | `0.2335` | 4,530,000.00 USD | 0.00 USD | 1,940.00 USD | `-24.46%` | `8,326.10` |
| `Live` | `Long` | `0.2355` | 4,530,000.00 USD | 0.00 USD | 10,540.00 USD | `-23.81%` | `44,770.40` |
| `Live` | `Long` | `0.2385` | 4,510,000.00 USD | 0.00 USD | 92,210.00 USD | `-22.84%` | `386,645.00` |
| `Live` | `Long` | `0.2405` | 4,420,000.00 USD | 0.00 USD | 13,650.00 USD | `-22.19%` | `56,745.50` |
| `Live` | `Long` | `0.2415` | 4,410,000.00 USD | 0.00 USD | 21,530.00 USD | `-21.87%` | `89,135.40` |
| `Live` | `Long` | `0.2425` | 4,390,000.00 USD | 0.00 USD | 121,740.00 USD | `-21.55%` | `502,037.20` |
| `Live` | `Long` | `0.2435` | 4,270,000.00 USD | 0.00 USD | 22,560.00 USD | `-21.22%` | `92,637.30` |
| `Live` | `Long` | `0.2445` | 4,240,000.00 USD | 0.00 USD | 26,100.00 USD | `-20.90%` | `106,766.80` |
| `Live` | `Long` | `0.2455` | 4,220,000.00 USD | 0.00 USD | 23,020.00 USD | `-20.58%` | `93,774.40` |
| `Live` | `Long` | `0.2465` | 4,190,000.00 USD | 0.00 USD | 7,910.00 USD | `-20.25%` | `32,081.10` |
| `Live` | `Long` | `0.2475` | 4,190,000.00 USD | 0.00 USD | 18,230.00 USD | `-19.93%` | `73,640.00` |
| `Live` | `Long` | `0.2485` | 4,170,000.00 USD | 0.00 USD | 4,230.00 USD | `-19.61%` | `17,005.20` |
| `Live` | `Long` | `0.2495` | 4,160,000.00 USD | 0.00 USD | 28,290.00 USD | `-19.28%` | `113,393.90` |
| `Live` | `Long` | `0.2505` | 4,140,000.00 USD | 0.00 USD | 151,550.00 USD | `-18.96%` | `604,984.00` |
| `Live` | `Long` | `0.2525` | 3,980,000.00 USD | 0.00 USD | 5,390.00 USD | `-18.31%` | `21,359.60` |
| `Live` | `Long` | `0.2545` | 3,980,000.00 USD | 0.00 USD | 22,030.00 USD | `-17.66%` | `86,545.50` |
| `Live` | `Long` | `0.2555` | 3,960,000.00 USD | 0.00 USD | 61,240.00 USD | `-17.34%` | `239,689.20` |
| `Live` | `Long` | `0.2565` | 3,890,000.00 USD | 0.00 USD | 7,240.00 USD | `-17.02%` | `28,212.10` |
| `Live` | `Long` | `0.2585` | 3,890,000.00 USD | 0.00 USD | 51,830.00 USD | `-16.37%` | `200,494.00` |
| `Live` | `Long` | `0.2595` | 3,840,000.00 USD | 0.00 USD | 44,370.00 USD | `-16.05%` | `170,996.10` |
| `Live` | `Long` | `0.2605` | 3,790,000.00 USD | 0.00 USD | 9,290.00 USD | `-15.72%` | `35,646.80` |
| `Live` | `Long` | `0.2615` | 3,780,000.00 USD | 0.00 USD | 28,620.00 USD | `-15.40%` | `109,459.40` |
| `Live` | `Long` | `0.2625` | 3,750,000.00 USD | 0.00 USD | 1,910.00 USD | `-15.08%` | `7,277.80` |
| `Live` | `Long` | `0.2635` | 3,750,000.00 USD | 0.00 USD | 20,760.00 USD | `-14.75%` | `78,768.90` |
| `Live` | `Long` | `0.2645` | 3,730,000.00 USD | 0.00 USD | 190,880.00 USD | `-14.43%` | `721,669.50` |
| `Live` | `Long` | `0.2655` | 3,540,000.00 USD | 0.00 USD | 87,230.00 USD | `-14.11%` | `328,555.60` |
| `Live` | `Long` | `0.2665` | 3,450,000.00 USD | 0.00 USD | 25,020.00 USD | `-13.78%` | `93,885.20` |
| `Live` | `Long` | `0.2675` | 3,430,000.00 USD | 0.00 USD | 21,780.00 USD | `-13.46%` | `81,418.40` |
| `Live` | `Long` | `0.2685` | 3,410,000.00 USD | 0.00 USD | 22,620.00 USD | `-13.13%` | `84,234.80` |
| `Live` | `Long` | `0.2695` | 3,380,000.00 USD | 0.00 USD | 35,450.00 USD | `-12.81%` | `131,557.60` |
| `Live` | `Long` | `0.2705` | 3,350,000.00 USD | 0.00 USD | 11,110.00 USD | `-12.49%` | `41,086.50` |
| `Live` | `Long` | `0.2715` | 3,340,000.00 USD | 0.00 USD | 44,010.00 USD | `-12.16%` | `162,081.90` |
| `Live` | `Long` | `0.2725` | 3,290,000.00 USD | 0.00 USD | 2,420.00 USD | `-11.84%` | `8,894.10` |
| `Live` | `Long` | `0.2735` | 3,290,000.00 USD | 0.00 USD | 21,260.00 USD | `-11.52%` | `77,741.90` |
| `Live` | `Long` | `0.2745` | 3,270,000.00 USD | 0.00 USD | 301,980.00 USD | `-11.19%` | `1,100,106.20` |
| `Live` | `Long` | `0.2755` | 2,970,000.00 USD | 0.00 USD | 319,420.00 USD | `-10.87%` | `1,159,434.10` |
| `Live` | `Long` | `0.2765` | 2,650,000.00 USD | 0.00 USD | 10,610.00 USD | `-10.55%` | `38,363.00` |
| `Live` | `Long` | `0.2775` | 2,640,000.00 USD | 0.00 USD | 90,440.00 USD | `-10.22%` | `325,926.10` |
| `Live` | `Long` | `0.2785` | 2,550,000.00 USD | 0.00 USD | 3,950.00 USD | `-9.90%` | `14,195.20` |
| `Live` | `Long` | `0.2795` | 2,540,000.00 USD | 0.00 USD | 14,770.00 USD | `-9.58%` | `52,856.00` |
| `Live` | `Long` | `0.2805` | 2,530,000.00 USD | 0.00 USD | 54,240.00 USD | `-9.25%` | `193,376.20` |
| `Live` | `Long` | `0.2815` | 2,470,000.00 USD | 0.00 USD | 26,670.00 USD | `-8.93%` | `94,725.70` |
| `Live` | `Long` | `0.2825` | 2,450,000.00 USD | 0.00 USD | 371,710.00 USD | `-8.61%` | `1,315,803.90` |
| `Live` | `Long` | `0.2835` | 2,080,000.00 USD | 0.00 USD | 331,540.00 USD | `-8.28%` | `1,169,455.50` |
| `Live` | `Long` | `0.2845` | 1,740,000.00 USD | 0.00 USD | 16,970.00 USD | `-7.96%` | `59,665.00` |
| `Live` | `Long` | `0.2855` | 1,730,000.00 USD | 0.00 USD | 23,390.00 USD | `-7.64%` | `81,912.50` |
| `Live` | `Long` | `0.2865` | 1,700,000.00 USD | 0.00 USD | 44,720.00 USD | `-7.31%` | `156,095.50` |
| `Live` | `Long` | `0.2875` | 1,660,000.00 USD | 0.00 USD | 203,880.00 USD | `-6.99%` | `709,136.30` |
| `Live` | `Long` | `0.2885` | 1,450,000.00 USD | 0.00 USD | 464,670.00 USD | `-6.66%` | `1,610,631.60` |
| `Live` | `Long` | `0.2895` | 990,100.00 USD | 0.00 USD | 333,410.00 USD | `-6.34%` | `1,151,676.90` |
| `Live` | `Long` | `0.2905` | 656,690.00 USD | 0.00 USD | 207,180.00 USD | `-6.02%` | `713,175.40` |
| `Live` | `Long` | `0.2915` | 449,510.00 USD | 0.00 USD | 22,800.00 USD | `-5.69%` | `78,218.10` |
| `Live` | `Long` | `0.2925` | 426,710.00 USD | 0.00 USD | 25,320.00 USD | `-5.37%` | `86,560.50` |
| `Live` | `Long` | `0.2935` | 401,390.00 USD | 0.00 USD | 24,880.00 USD | `-5.05%` | `84,783.00` |
| `Live` | `Long` | `0.2945` | 376,510.00 USD | 0.00 USD | 179,490.00 USD | `-4.72%` | `609,483.60` |
| `Live` | `Long` | `0.2955` | 197,010.00 USD | 0.00 USD | 21,630.00 USD | `-4.40%` | `73,210.80` |
| `Live` | `Long` | `0.2965` | 175,380.00 USD | 0.00 USD | 13,370.00 USD | `-4.08%` | `45,105.80` |
| `Live` | `Long` | `0.2975` | 162,010.00 USD | 0.00 USD | 1,700.00 USD | `-3.75%` | `5,703.10` |
| `Live` | `Long` | `0.2985` | 160,310.00 USD | 0.00 USD | 59,790.00 USD | `-3.43%` | `200,289.60` |
| `Live` | `Long` | `0.2995` | 100,520.00 USD | 0.00 USD | 7,640.00 USD | `-3.11%` | `25,524.00` |
| `Live` | `Long` | `0.3005` | 92,880.00 USD | 0.00 USD | 56,820.00 USD | `-2.78%` | `189,086.60` |
| `Live` | `Long` | `0.3015` | 36,060.00 USD | 0.00 USD | 7,160.00 USD | `-2.46%` | `23,741.60` |
| `Live` | `Long` | `0.3025` | 28,900.00 USD | 0.00 USD | 567.49 USD | `-2.14%` | `1,876.00` |
| `Live` | `Long` | `0.3035` | 28,330.00 USD | 0.00 USD | 13,620.00 USD | `-1.81%` | `44,876.90` |
| `Live` | `Long` | `0.3065` | 14,710.00 USD | 0.00 USD | 14,710.00 USD | `-0.84%` | `48,000.00` |
| `Live` | `Short` | `0.3095` | 21,210.00 USD | 21,210.00 USD | 0.00 USD | `+0.13%` | `68,532.30` |
| `Live` | `Short` | `0.3105` | 21,740.00 USD | 531.79 USD | 0.00 USD | `+0.45%` | `1,712.70` |
| `Live` | `Short` | `0.3125` | 35,190.00 USD | 13,450.00 USD | 0.00 USD | `+1.10%` | `43,035.30` |
| `Live` | `Short` | `0.3195` | 39,660.00 USD | 4,470.00 USD | 0.00 USD | `+3.36%` | `13,985.90` |
| `Live` | `Short` | `0.3215` | 39,920.00 USD | 257.88 USD | 0.00 USD | `+4.01%` | `802.10` |
| `Live` | `Short` | `0.3245` | 68,600.00 USD | 28,680.00 USD | 0.00 USD | `+4.98%` | `88,396.70` |
| `Live` | `Short` | `0.3265` | 71,660.00 USD | 3,060.00 USD | 0.00 USD | `+5.63%` | `9,364.30` |
| `Live` | `Short` | `0.3275` | 74,030.00 USD | 2,370.00 USD | 0.00 USD | `+5.95%` | `7,249.40` |
| `Live` | `Short` | `0.3285` | 105,520.00 USD | 31,480.00 USD | 0.00 USD | `+6.28%` | `95,841.10` |
| `Live` | `Short` | `0.3295` | 107,700.00 USD | 2,180.00 USD | 0.00 USD | `+6.60%` | `6,616.80` |
| `Live` | `Short` | `0.3425` | 119,800.00 USD | 12,100.00 USD | 0.00 USD | `+10.81%` | `35,339.80` |
| `Live` | `Short` | `0.3495` | 120,630.00 USD | 830.24 USD | 0.00 USD | `+13.07%` | `2,375.50` |
| `Live` | `Short` | `0.3565` | 124,370.00 USD | 3,740.00 USD | 0.00 USD | `+15.33%` | `10,499.10` |
| `Live` | `Short` | `0.3575` | 124,480.00 USD | 100.14 USD | 0.00 USD | `+15.66%` | `280.10` |
| `Live` | `Short` | `0.3625` | 126,570.00 USD | 2,100.00 USD | 0.00 USD | `+17.28%` | `5,784.00` |
| `Live` | `Short` | `0.3675` | 128,670.00 USD | 2,100.00 USD | 0.00 USD | `+18.89%` | `5,705.10` |
| `Live` | `Short` | `0.3835` | 131,420.00 USD | 2,750.00 USD | 0.00 USD | `+24.07%` | `7,164.40` |
| `Live` | `Short` | `0.3885` | 131,520.00 USD | 103.81 USD | 0.00 USD | `+25.69%` | `267.20` |
| `Live` | `Short` | `0.4025` | 132,000.00 USD | 477.49 USD | 0.00 USD | `+30.22%` | `1,186.30` |
| `Live` | `Short` | `0.4035` | 132,230.00 USD | 236.85 USD | 0.00 USD | `+30.54%` | `587.00` |
| `Live` | `Short` | `0.4205` | 133,930.00 USD | 1,700.00 USD | 0.00 USD | `+36.04%` | `4,032.60` |
| `Live` | `Short` | `0.4245` | 134,040.00 USD | 115.25 USD | 0.00 USD | `+37.33%` | `271.50` |
| `Live` | `Short` | `0.4445` | 134,930.00 USD | 889.00 USD | 0.00 USD | `+43.80%` | `2,000.00` |
| `Live` | `Short` | `0.4575` | 145,410.00 USD | 10,480.00 USD | 0.00 USD | `+48.01%` | `22,906.80` |
| `Live` | `Short` | `0.4595` | 146,440.00 USD | 1,020.00 USD | 0.00 USD | `+48.66%` | `2,227.00` |
| `Live` | `Short` | `0.4655` | 147,930.00 USD | 1,490.00 USD | 0.00 USD | `+50.60%` | `3,205.50` |
| `Live` | `Short` | `0.5015` | 148,090.00 USD | 160.23 USD | 0.00 USD | `+62.25%` | `319.50` |
| `Live` | `Short` | `0.5035` | 515,140.00 USD | 367,050.00 USD | 0.00 USD | `+62.89%` | `729,000.00` |
| `Live` | `Short` | `0.5155` | 515,570.00 USD | 428.28 USD | 0.00 USD | `+66.77%` | `830.80` |
| `Live` | `Short` | `0.5165` | 577,550.00 USD | 61,980.00 USD | 0.00 USD | `+67.10%` | `120,000.00` |
| `Live` | `Short` | `0.5315` | 592,060.00 USD | 14,510.00 USD | 0.00 USD | `+71.95%` | `27,300.00` |
| `Live` | `Short` | `0.5565` | 594,920.00 USD | 2,860.00 USD | 0.00 USD | `+80.04%` | `5,135.90` |
| `Live` | `Short` | `0.5835` | 612,320.00 USD | 17,400.00 USD | 0.00 USD | `+88.77%` | `29,816.80` |

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
  * Current Rate: `2.31K` | Last 24h: `14.14K` | Last 3d: `34.03K` | Last 7d: `51.20K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0025%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0045%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0067%` | **USDT Bitget** | `0.0100%` |
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
| `5m` | -3,020.00 USD | -151,940.00 USD | **`DISTRIBUTION`** |
| `15m` | -33,070.00 USD | -296,800.00 USD | **`DISTRIBUTION`** |
| `30m` | -106,570.00 USD | -937,430.00 USD | **`DISTRIBUTION`** |
| `1h` | 3,260.00 USD | -1,180,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -199,790.00 USD | -3,360,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -413,930.00 USD | -3,630,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -511,790.00 USD | -5,310,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -311,540.00 USD | -5,480,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -458,390.00 USD | -6,080,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -475,970.00 USD | -7,150,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -1,920,000.00 USD | -18,660,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -15,200,000.00 USD | -60,760,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-3.02K` | 15m=`-33.07K` | 1h=`+3.26K` | 24h=`-475.97K`
* Futures Capital Netflows: 5m=`-151.94K` | 15m=`-296.80K` | 1h=`-1.18M` | 24h=`-7.15M`
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
  * `2026-10-30 02:54:14 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:21:14 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:21:14 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:20:14 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:20:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:14 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:14 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:14 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:14 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:22:14 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:14 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.2990` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.2608` (Risk Distance: `0.0440` pts)
  * +2.5R Take Profit: `0.4090`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3030` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3412` (Risk Distance: `0.0440` pts)
  * +2.5R Take Profit: `0.1930`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3105`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
