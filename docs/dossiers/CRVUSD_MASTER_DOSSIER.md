# 🏛️ SOVEREIGN CANDIDATE DOSSIER: CRVUSD
**Canonical Key**: `CRVUSD` | **Broker Instrument**: `CRVUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-29 23:40:51 IST` (`2026-10-29 18:10:51 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3170` | **Live Ask Quote**: `0.3400` | **Mid Price**: `0.3285`
- **Spread Points**: `23.00` | **Spread BPS**: `700.15 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3172` | VWAP Z-Score: `-0.31` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0025` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `39.14` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3287` | Lower -3.00σ Band: `0.3057`
  * Upper +2.51σ Band: `0.3268` | Lower -2.51σ Band: `0.3076`
  * Upper +2.01σ Band: `0.3249` | Lower -2.01σ Band: `0.3095`
  * Upper +2.00σ Band: `0.3249` | Lower -2.00σ Band: `0.3095`
  * Upper +1.28σ Band: `0.3221` | Lower -1.28σ Band: `0.3123`
  * Upper +1.00σ Band: `0.3210` | Lower -1.00σ Band: `0.3134`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3196` | EMA-20=`0.3196` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3188` (Slope: `+0.0000`) | EMA-100=`0.3198`
  * Institutional Anchors: EMA-144=`0.3208` | EMA-200=`0.3219` (Slope: `-0.0170`) | EMA-233=`0.3224`
- **Range Boundaries**: 24H High=`0.3340` | 24H Low=`0.3090` | Weekly High=`0.3420` | Weekly Low=`0.3090`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3220` (Distance: `+2.31%`)
  * Point of Control (POC) = `0.3150` (Distance: `+4.44%`)
  * Value Area Low (VAL) = `0.3110` (Distance: `+5.79%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3300` | POC=`0.3270` | VAL=`0.3240`
  * Prior Day Extremes: PDH=`0.3340` | PDL=`0.3210` | PDC=`0.3300`
  * Monday Range Blueprint: High=`0.3430` | Mid=`0.3340` | Low=`0.3250`
  * Developing Weekly Value Area: Weekly VAH=`0.3340` | Weekly POC=`0.3280` | Weekly VAL=`0.3210`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3330` | Low=`0.3090`
  * London Session (08:00-16:00 UTC): High=`0.3210` | Low=`0.3120`
  * New York Session (13:00-21:00 UTC): High=`0.3270` | Low=`0.3120`
  * Initial Balance (First Hour): IB High=`0.3190` | IB Low=`0.3140`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3272` - `0.3298`
  * Optimal Trade Entry (OTE 0.705): `0.3292`
  * Structural Invalidation Anchor (0.786): `0.3311`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:36:01 IST` |

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
| `Live` | `Long Liquidation` | `0.0745` | 447.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 1,380.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 2,330.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 485.44 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 711.77 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 417.32 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1125` | 1,230.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 5,620.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 116.35 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 4,300.00 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 601.16 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1375` | 1,150.00 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 427.50 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1505` | 1,020.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 6,100.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1545` | 3,860.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 712.49 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 6,500.00 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 397.60 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 4,930.00 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 28,850.00 USD | 5,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 27,120.00 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 464.68 USD | 5,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 8,980.00 USD | 5,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 1,530.00 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 14,130.00 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1785` | 12,900.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 15,690.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1805` | 16,880.00 USD | 5,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1815` | 18,660.00 USD | 5,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1835` | 179.10 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1845` | 1,480.00 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1865` | 12,060.00 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 11,460.00 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1885` | 1,660.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1895` | 1,050.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1915` | 1,870.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1925` | 359.78 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1935` | 2,150.00 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1955` | 13,190.00 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1975` | 6,010.00 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1985` | 1,100.00 USD | 5,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 146,050.00 USD | 5,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2005` | 5,880.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 18,380.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2055` | 1,060.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2085` | 2,390.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2095` | 126.08 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2105` | 30,380.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2125` | 2,240.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2135` | 28,230.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 153.87 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 131,210.00 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2215` | 25,340.00 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2235` | 8,940.00 USD | 5,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2265` | 18,290.00 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2285` | 12,040.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 967.55 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 45,160.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 19,940.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 17,320.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 31,680.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 354,560.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 13,650.00 USD | 4,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2415` | 36,950.00 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 109,880.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 19,800.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 5,530.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 18,110.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 17,250.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 9,480.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 20,060.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2495` | 28,290.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 218,650.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2525` | 9,370.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2535` | 8,200.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2545` | 22,030.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 68,910.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 13,650.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 23,480.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 46,140.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 1,700.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 9,030.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 20,760.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 5,390.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 196,560.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 2,000.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 14,790.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 20,470.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2695` | 61,670.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2705` | 1,900.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2715` | 46,010.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 21,260.00 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 312,470.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 9,700.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2765` | 5,970.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2775` | 158,150.00 USD | 3,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 43,440.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 70,670.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 87,930.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 2,240.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 84,670.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2835` | 329,170.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2845` | 25,100.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 23,820.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2865` | 218,760.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2875` | 125,350.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 567,680.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2895` | 42,410.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 201,430.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 30,170.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2925` | 186,190.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2935` | 33,540.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 30,500.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2955` | 16,010.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2965` | 273,630.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2975` | 2,540.00 USD | 772,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2985` | 53,970.00 USD | 769,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2995` | 1,890.00 USD | 715,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3005` | 24,630.00 USD | 713,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3015` | 236,270.00 USD | 689,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3025` | 13,250.00 USD | 452,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3035` | 11,460.00 USD | 439,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3045` | 768.34 USD | 428,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3055` | 72,120.00 USD | 427,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3065` | 18,670.00 USD | 355,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3075` | 63,560.00 USD | 336,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3085` | 33,070.00 USD | 272,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3095` | 19,290.00 USD | 239,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3105` | 28,020.00 USD | 220,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3115` | 81,680.00 USD | 192,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3125` | 3,430.00 USD | 110,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3135` | 975.30 USD | 107,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3155` | 14,410.00 USD | 106,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3165` | 2,080.00 USD | 92,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3175` | 1,070.00 USD | 89,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3185` | 60,870.00 USD | 88,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3195` | 28,000.00 USD | 28,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3495` | 2,230.00 USD | 2,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3505` | 3,960.00 USD | 6,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3525` | 2,240.00 USD | 8,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3575` | 497.00 USD | 8,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 2,100.00 USD | 11,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3675` | 2,100.00 USD | 13,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3885` | 103.81 USD | 13,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3915` | 4,740.00 USD | 17,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4025` | 477.49 USD | 18,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4035` | 236.85 USD | 18,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4045` | 1,300.00 USD | 19,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4205` | 1,700.00 USD | 21,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4245` | 115.25 USD | 21,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4445` | 889.00 USD | 22,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4455` | 992.13 USD | 23,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4575` | 10,480.00 USD | 34,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4665` | 325.01 USD | 34,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4795` | 4,360.00 USD | 38,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4945` | 360,490.00 USD | 399,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5015` | 160.23 USD | 399,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5035` | 60,420.00 USD | 459,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5155` | 428.28 USD | 460,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5305` | 14,480.00 USD | 474,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5485` | 401,500.00 USD | 876,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5525` | 111,220.00 USD | 987,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5565` | 2,860.00 USD | 990,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5835` | 17,400.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6315` | 190.46 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6425` | 445.77 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6465` | 121.61 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6475` | 5,730.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6485` | 1,100.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6575` | 19,730.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0725` | 5,870,000.00 USD | 0.00 USD | 3,690.00 USD | `-77.88%` | `50,846.60` |
| `Live` | `Long` | `0.0755` | 5,860,000.00 USD | 0.00 USD | 453.00 USD | `-76.97%` | `6,000.00` |
| `Live` | `Long` | `0.0785` | 5,860,000.00 USD | 0.00 USD | 2,330.00 USD | `-76.05%` | `29,622.60` |
| `Live` | `Long` | `0.0835` | 5,860,000.00 USD | 0.00 USD | 32,460.00 USD | `-74.53%` | `388,690.50` |
| `Live` | `Long` | `0.0865` | 5,830,000.00 USD | 0.00 USD | 485.44 USD | `-73.61%` | `5,612.00` |
| `Live` | `Long` | `0.0875` | 5,830,000.00 USD | 0.00 USD | 1,580.00 USD | `-73.31%` | `18,050.00` |
| `Live` | `Long` | `0.0895` | 5,820,000.00 USD | 0.00 USD | 719.81 USD | `-72.70%` | `8,042.60` |
| `Live` | `Long` | `0.1165` | 5,820,000.00 USD | 0.00 USD | 134.25 USD | `-64.46%` | `1,152.40` |
| `Live` | `Long` | `0.1195` | 5,820,000.00 USD | 0.00 USD | 1,530.00 USD | `-63.54%` | `12,814.90` |
| `Live` | `Long` | `0.1215` | 5,820,000.00 USD | 0.00 USD | 564.03 USD | `-62.93%` | `4,642.20` |
| `Live` | `Long` | `0.1225` | 5,820,000.00 USD | 0.00 USD | 116.35 USD | `-62.63%` | `949.80` |
| `Live` | `Long` | `0.1255` | 5,820,000.00 USD | 0.00 USD | 4,300.00 USD | `-61.71%` | `34,264.40` |
| `Live` | `Long` | `0.1275` | 5,820,000.00 USD | 0.00 USD | 6,000.00 USD | `-61.10%` | `47,058.80` |
| `Live` | `Long` | `0.1305` | 5,810,000.00 USD | 0.00 USD | 176.88 USD | `-60.19%` | `1,355.40` |
| `Live` | `Long` | `0.1375` | 5,810,000.00 USD | 0.00 USD | 1,150.00 USD | `-58.05%` | `8,365.30` |
| `Live` | `Long` | `0.1425` | 5,810,000.00 USD | 0.00 USD | 427.50 USD | `-56.53%` | `3,000.00` |
| `Live` | `Long` | `0.1435` | 5,810,000.00 USD | 0.00 USD | 546.89 USD | `-56.22%` | `3,811.10` |
| `Live` | `Long` | `0.1645` | 5,810,000.00 USD | 0.00 USD | 397.60 USD | `-49.82%` | `2,417.00` |
| `Live` | `Long` | `0.1665` | 5,810,000.00 USD | 0.00 USD | 12,720.00 USD | `-49.21%` | `76,413.80` |
| `Live` | `Long` | `0.1695` | 5,800,000.00 USD | 0.00 USD | 752.44 USD | `-48.29%` | `4,439.20` |
| `Live` | `Long` | `0.1715` | 5,790,000.00 USD | 0.00 USD | 464.68 USD | `-47.68%` | `2,709.50` |
| `Live` | `Long` | `0.1725` | 5,790,000.00 USD | 0.00 USD | 7,950.00 USD | `-47.37%` | `46,059.00` |
| `Live` | `Long` | `0.1735` | 5,790,000.00 USD | 0.00 USD | 37,870.00 USD | `-47.07%` | `218,246.60` |
| `Live` | `Long` | `0.1755` | 5,750,000.00 USD | 0.00 USD | 28,080.00 USD | `-46.46%` | `160,000.00` |
| `Live` | `Long` | `0.1765` | 5,720,000.00 USD | 0.00 USD | 1,530.00 USD | `-46.15%` | `8,680.50` |
| `Live` | `Long` | `0.1775` | 5,720,000.00 USD | 0.00 USD | 14,130.00 USD | `-45.85%` | `79,610.90` |
| `Live` | `Long` | `0.1785` | 5,700,000.00 USD | 0.00 USD | 12,900.00 USD | `-45.54%` | `72,270.30` |
| `Live` | `Long` | `0.1795` | 5,690,000.00 USD | 0.00 USD | 13,180.00 USD | `-45.24%` | `73,444.60` |
| `Live` | `Long` | `0.1805` | 5,680,000.00 USD | 0.00 USD | 16,880.00 USD | `-44.93%` | `93,542.70` |
| `Live` | `Long` | `0.1835` | 5,660,000.00 USD | 0.00 USD | 4,770.00 USD | `-44.02%` | `25,976.00` |
| `Live` | `Long` | `0.1845` | 5,660,000.00 USD | 0.00 USD | 1,480.00 USD | `-43.71%` | `8,024.00` |
| `Live` | `Long` | `0.1865` | 5,660,000.00 USD | 0.00 USD | 9,460.00 USD | `-43.10%` | `50,699.40` |
| `Live` | `Long` | `0.1875` | 5,650,000.00 USD | 0.00 USD | 11,460.00 USD | `-42.80%` | `61,135.10` |
| `Live` | `Long` | `0.1885` | 5,630,000.00 USD | 0.00 USD | 1,660.00 USD | `-42.49%` | `8,802.20` |
| `Live` | `Long` | `0.1895` | 5,630,000.00 USD | 0.00 USD | 1,050.00 USD | `-42.19%` | `5,539.20` |
| `Live` | `Long` | `0.1905` | 5,630,000.00 USD | 0.00 USD | 2,660.00 USD | `-41.88%` | `13,940.20` |
| `Live` | `Long` | `0.1925` | 5,630,000.00 USD | 0.00 USD | 359.78 USD | `-41.27%` | `1,869.00` |
| `Live` | `Long` | `0.1935` | 5,630,000.00 USD | 0.00 USD | 2,150.00 USD | `-40.97%` | `11,110.40` |
| `Live` | `Long` | `0.1945` | 5,630,000.00 USD | 0.00 USD | 511.07 USD | `-40.66%` | `2,627.60` |
| `Live` | `Long` | `0.1955` | 5,630,000.00 USD | 0.00 USD | 13,190.00 USD | `-40.36%` | `67,459.20` |
| `Live` | `Long` | `0.1965` | 5,610,000.00 USD | 0.00 USD | 2,230.00 USD | `-40.05%` | `11,332.30` |
| `Live` | `Long` | `0.1975` | 5,610,000.00 USD | 0.00 USD | 20,310.00 USD | `-39.75%` | `102,814.70` |
| `Live` | `Long` | `0.1985` | 5,590,000.00 USD | 0.00 USD | 1,100.00 USD | `-39.44%` | `5,563.00` |
| `Live` | `Long` | `0.1995` | 5,590,000.00 USD | 0.00 USD | 146,050.00 USD | `-39.14%` | `732,075.00` |
| `Live` | `Long` | `0.2045` | 5,440,000.00 USD | 0.00 USD | 18,380.00 USD | `-37.61%` | `89,877.80` |
| `Live` | `Long` | `0.2055` | 5,420,000.00 USD | 0.00 USD | 1,060.00 USD | `-37.31%` | `5,147.80` |
| `Live` | `Long` | `0.2075` | 5,420,000.00 USD | 0.00 USD | 6,090.00 USD | `-36.70%` | `29,332.10` |
| `Live` | `Long` | `0.2085` | 5,420,000.00 USD | 0.00 USD | 2,390.00 USD | `-36.39%` | `11,465.50` |
| `Live` | `Long` | `0.2105` | 5,420,000.00 USD | 0.00 USD | 30,380.00 USD | `-35.78%` | `144,300.00` |
| `Live` | `Long` | `0.2125` | 5,390,000.00 USD | 0.00 USD | 521.03 USD | `-35.17%` | `2,451.90` |
| `Live` | `Long` | `0.2135` | 5,380,000.00 USD | 0.00 USD | 34,730.00 USD | `-34.87%` | `162,659.30` |
| `Live` | `Long` | `0.2145` | 5,350,000.00 USD | 0.00 USD | 1,730.00 USD | `-34.56%` | `8,080.80` |
| `Live` | `Long` | `0.2195` | 5,350,000.00 USD | 0.00 USD | 153.87 USD | `-33.04%` | `701.00` |
| `Live` | `Long` | `0.2205` | 5,350,000.00 USD | 0.00 USD | 130,550.00 USD | `-32.73%` | `592,044.70` |
| `Live` | `Long` | `0.2215` | 5,220,000.00 USD | 0.00 USD | 25,340.00 USD | `-32.43%` | `114,401.60` |
| `Live` | `Long` | `0.2225` | 5,190,000.00 USD | 0.00 USD | 667.50 USD | `-32.12%` | `3,000.00` |
| `Live` | `Long` | `0.2235` | 5,190,000.00 USD | 0.00 USD | 8,940.00 USD | `-31.82%` | `39,998.20` |
| `Live` | `Long` | `0.2285` | 5,180,000.00 USD | 0.00 USD | 12,040.00 USD | `-30.29%` | `52,680.20` |
| `Live` | `Long` | `0.2295` | 5,170,000.00 USD | 0.00 USD | 337.59 USD | `-29.99%` | `1,471.00` |
| `Live` | `Long` | `0.2305` | 5,170,000.00 USD | 0.00 USD | 63,770.00 USD | `-29.68%` | `276,681.10` |
| `Live` | `Long` | `0.2315` | 5,110,000.00 USD | 0.00 USD | 135,690.00 USD | `-29.38%` | `586,139.70` |
| `Live` | `Long` | `0.2325` | 4,970,000.00 USD | 0.00 USD | 17,320.00 USD | `-29.07%` | `74,516.00` |
| `Live` | `Long` | `0.2335` | 4,950,000.00 USD | 0.00 USD | 1,940.00 USD | `-28.77%` | `8,326.10` |
| `Live` | `Long` | `0.2385` | 4,950,000.00 USD | 0.00 USD | 92,210.00 USD | `-27.24%` | `386,645.00` |
| `Live` | `Long` | `0.2405` | 4,860,000.00 USD | 0.00 USD | 13,650.00 USD | `-26.63%` | `56,745.50` |
| `Live` | `Long` | `0.2415` | 4,850,000.00 USD | 0.00 USD | 36,950.00 USD | `-26.32%` | `153,010.30` |
| `Live` | `Long` | `0.2425` | 4,810,000.00 USD | 0.00 USD | 407,510.00 USD | `-26.02%` | `1,680,469.40` |
| `Live` | `Long` | `0.2435` | 4,400,000.00 USD | 0.00 USD | 19,800.00 USD | `-25.71%` | `81,305.00` |
| `Live` | `Long` | `0.2445` | 4,380,000.00 USD | 0.00 USD | 5,530.00 USD | `-25.41%` | `22,606.60` |
| `Live` | `Long` | `0.2455` | 4,380,000.00 USD | 0.00 USD | 18,110.00 USD | `-25.10%` | `73,774.40` |
| `Live` | `Long` | `0.2475` | 4,360,000.00 USD | 0.00 USD | 9,480.00 USD | `-24.49%` | `38,294.10` |
| `Live` | `Long` | `0.2485` | 4,350,000.00 USD | 0.00 USD | 4,030.00 USD | `-24.19%` | `16,203.80` |
| `Live` | `Long` | `0.2495` | 4,340,000.00 USD | 0.00 USD | 28,290.00 USD | `-23.88%` | `113,393.90` |
| `Live` | `Long` | `0.2505` | 4,320,000.00 USD | 0.00 USD | 167,340.00 USD | `-23.58%` | `668,031.90` |
| `Live` | `Long` | `0.2525` | 4,150,000.00 USD | 0.00 USD | 73,400.00 USD | `-22.97%` | `290,702.90` |
| `Live` | `Long` | `0.2535` | 4,080,000.00 USD | 0.00 USD | 8,000.00 USD | `-22.66%` | `31,552.80` |
| `Live` | `Long` | `0.2545` | 4,070,000.00 USD | 0.00 USD | 39,840.00 USD | `-22.36%` | `156,545.50` |
| `Live` | `Long` | `0.2555` | 4,030,000.00 USD | 0.00 USD | 59,960.00 USD | `-22.05%` | `234,689.20` |
| `Live` | `Long` | `0.2565` | 3,970,000.00 USD | 0.00 USD | 823.90 USD | `-21.75%` | `3,212.10` |
| `Live` | `Long` | `0.2585` | 3,970,000.00 USD | 0.00 USD | 16,260.00 USD | `-21.14%` | `62,908.90` |
| `Live` | `Long` | `0.2595` | 3,950,000.00 USD | 0.00 USD | 46,140.00 USD | `-20.83%` | `177,797.60` |
| `Live` | `Long` | `0.2615` | 3,900,000.00 USD | 0.00 USD | 1,700.00 USD | `-20.22%` | `6,486.80` |
| `Live` | `Long` | `0.2625` | 3,900,000.00 USD | 0.00 USD | 13,120.00 USD | `-19.92%` | `50,000.00` |
| `Live` | `Long` | `0.2635` | 3,890,000.00 USD | 0.00 USD | 33,800.00 USD | `-19.61%` | `128,281.50` |
| `Live` | `Long` | `0.2645` | 3,860,000.00 USD | 0.00 USD | 14,650.00 USD | `-19.31%` | `55,384.10` |
| `Live` | `Long` | `0.2655` | 3,840,000.00 USD | 0.00 USD | 10,710.00 USD | `-19.00%` | `40,345.40` |
| `Live` | `Long` | `0.2665` | 3,830,000.00 USD | 0.00 USD | 7,330.00 USD | `-18.70%` | `27,501.40` |
| `Live` | `Long` | `0.2675` | 3,820,000.00 USD | 0.00 USD | 14,790.00 USD | `-18.39%` | `55,307.60` |
| `Live` | `Long` | `0.2685` | 3,810,000.00 USD | 0.00 USD | 20,470.00 USD | `-18.09%` | `76,236.40` |
| `Live` | `Long` | `0.2695` | 3,790,000.00 USD | 0.00 USD | 7,750.00 USD | `-17.78%` | `28,742.90` |
| `Live` | `Long` | `0.2705` | 3,780,000.00 USD | 0.00 USD | 1,900.00 USD | `-17.48%` | `7,034.00` |
| `Live` | `Long` | `0.2715` | 3,780,000.00 USD | 0.00 USD | 46,010.00 USD | `-17.17%` | `169,467.20` |
| `Live` | `Long` | `0.2735` | 3,730,000.00 USD | 0.00 USD | 21,260.00 USD | `-16.56%` | `77,741.90` |
| `Live` | `Long` | `0.2745` | 3,710,000.00 USD | 0.00 USD | 367,390.00 USD | `-16.26%` | `1,338,408.20` |
| `Live` | `Long` | `0.2755` | 3,340,000.00 USD | 0.00 USD | 9,700.00 USD | `-15.95%` | `35,194.00` |
| `Live` | `Long` | `0.2765` | 3,330,000.00 USD | 0.00 USD | 5,970.00 USD | `-15.65%` | `21,598.50` |
| `Live` | `Long` | `0.2775` | 3,330,000.00 USD | 0.00 USD | 158,550.00 USD | `-15.34%` | `571,360.30` |
| `Live` | `Long` | `0.2785` | 3,170,000.00 USD | 0.00 USD | 6,160.00 USD | `-15.04%` | `22,123.70` |
| `Live` | `Long` | `0.2795` | 3,160,000.00 USD | 0.00 USD | 70,670.00 USD | `-14.73%` | `252,856.00` |
| `Live` | `Long` | `0.2805` | 3,090,000.00 USD | 0.00 USD | 87,930.00 USD | `-14.43%` | `313,473.20` |
| `Live` | `Long` | `0.2815` | 3,000,000.00 USD | 0.00 USD | 44,690.00 USD | `-14.12%` | `158,746.20` |
| `Live` | `Long` | `0.2825` | 2,960,000.00 USD | 0.00 USD | 84,670.00 USD | `-13.82%` | `299,723.00` |
| `Live` | `Long` | `0.2835` | 2,870,000.00 USD | 0.00 USD | 328,760.00 USD | `-13.51%` | `1,159,641.10` |
| `Live` | `Long` | `0.2845` | 2,550,000.00 USD | 0.00 USD | 18,360.00 USD | `-13.21%` | `64,536.70` |
| `Live` | `Long` | `0.2855` | 2,530,000.00 USD | 0.00 USD | 23,820.00 USD | `-12.90%` | `83,420.90` |
| `Live` | `Long` | `0.2865` | 2,500,000.00 USD | 0.00 USD | 218,760.00 USD | `-12.60%` | `763,577.60` |
| `Live` | `Long` | `0.2875` | 2,290,000.00 USD | 0.00 USD | 125,350.00 USD | `-12.29%` | `435,983.70` |
| `Live` | `Long` | `0.2885` | 2,160,000.00 USD | 0.00 USD | 567,680.00 USD | `-11.99%` | `1,967,678.70` |
| `Live` | `Long` | `0.2895` | 1,590,000.00 USD | 0.00 USD | 42,410.00 USD | `-11.68%` | `146,499.90` |
| `Live` | `Long` | `0.2905` | 1,550,000.00 USD | 0.00 USD | 208,310.00 USD | `-11.38%` | `717,073.10` |
| `Live` | `Long` | `0.2915` | 1,340,000.00 USD | 0.00 USD | 205,070.00 USD | `-11.07%` | `703,482.00` |
| `Live` | `Long` | `0.2925` | 1,140,000.00 USD | 0.00 USD | 10,690.00 USD | `-10.77%` | `36,560.50` |
| `Live` | `Long` | `0.2935` | 1,130,000.00 USD | 0.00 USD | 13,940.00 USD | `-10.46%` | `47,483.80` |
| `Live` | `Long` | `0.2945` | 1,110,000.00 USD | 0.00 USD | 38,460.00 USD | `-10.16%` | `130,590.00` |
| `Live` | `Long` | `0.2955` | 1,070,000.00 USD | 0.00 USD | 3,960.00 USD | `-9.85%` | `13,402.80` |
| `Live` | `Long` | `0.2965` | 1,070,000.00 USD | 0.00 USD | 273,630.00 USD | `-9.55%` | `922,857.00` |
| `Live` | `Long` | `0.2975` | 795,570.00 USD | 0.00 USD | 14,370.00 USD | `-9.24%` | `48,295.80` |
| `Live` | `Long` | `0.2985` | 781,200.00 USD | 0.00 USD | 58,260.00 USD | `-8.94%` | `195,166.90` |
| `Live` | `Long` | `0.2995` | 722,950.00 USD | 0.00 USD | 1,890.00 USD | `-8.63%` | `6,321.30` |
| `Live` | `Long` | `0.3005` | 721,050.00 USD | 0.00 USD | 33,480.00 USD | `-8.33%` | `111,426.10` |
| `Live` | `Long` | `0.3015` | 687,570.00 USD | 0.00 USD | 60,430.00 USD | `-8.02%` | `200,416.40` |
| `Live` | `Long` | `0.3025` | 627,140.00 USD | 0.00 USD | 5,630.00 USD | `-7.72%` | `18,610.70` |
| `Live` | `Long` | `0.3035` | 621,510.00 USD | 0.00 USD | 170,860.00 USD | `-7.41%` | `562,969.90` |
| `Live` | `Long` | `0.3045` | 450,650.00 USD | 0.00 USD | 768.34 USD | `-7.11%` | `2,523.30` |
| `Live` | `Long` | `0.3055` | 449,880.00 USD | 0.00 USD | 72,120.00 USD | `-6.80%` | `236,081.50` |
| `Live` | `Long` | `0.3065` | 377,760.00 USD | 0.00 USD | 56,040.00 USD | `-6.50%` | `182,851.70` |
| `Live` | `Long` | `0.3075` | 321,720.00 USD | 0.00 USD | 60,980.00 USD | `-6.19%` | `198,299.10` |
| `Live` | `Long` | `0.3085` | 260,740.00 USD | 0.00 USD | 23,710.00 USD | `-5.88%` | `76,867.60` |
| `Live` | `Long` | `0.3095` | 237,030.00 USD | 0.00 USD | 8,430.00 USD | `-5.58%` | `27,235.10` |
| `Live` | `Long` | `0.3105` | 228,600.00 USD | 0.00 USD | 33,040.00 USD | `-5.27%` | `106,397.90` |
| `Live` | `Long` | `0.3115` | 195,560.00 USD | 0.00 USD | 81,680.00 USD | `-4.97%` | `262,212.50` |
| `Live` | `Long` | `0.3125` | 113,880.00 USD | 0.00 USD | 3,120.00 USD | `-4.66%` | `10,000.00` |
| `Live` | `Long` | `0.3135` | 110,760.00 USD | 0.00 USD | 5,080.00 USD | `-4.36%` | `16,219.10` |
| `Live` | `Long` | `0.3155` | 105,670.00 USD | 0.00 USD | 14,410.00 USD | `-3.75%` | `45,681.90` |
| `Live` | `Long` | `0.3165` | 91,260.00 USD | 0.00 USD | 2,080.00 USD | `-3.44%` | `6,582.50` |
| `Live` | `Long` | `0.3175` | 89,180.00 USD | 0.00 USD | 26,860.00 USD | `-3.14%` | `84,599.70` |
| `Live` | `Long` | `0.3185` | 62,320.00 USD | 0.00 USD | 60,270.00 USD | `-2.83%` | `189,229.10` |
| `Live` | `Long` | `0.3195` | 2,050.00 USD | 0.00 USD | 2,050.00 USD | `-2.53%` | `6,405.40` |
| `Live` | `Short` | `0.3435` | 5,610.00 USD | 5,610.00 USD | 0.00 USD | `+4.79%` | `16,341.80` |
| `Live` | `Short` | `0.3445` | 5,770.00 USD | 151.92 USD | 0.00 USD | `+5.10%` | `441.00` |
| `Live` | `Short` | `0.3465` | 6,290.00 USD | 522.80 USD | 0.00 USD | `+5.71%` | `1,508.80` |
| `Live` | `Short` | `0.3485` | 7,860.00 USD | 1,570.00 USD | 0.00 USD | `+6.32%` | `4,505.10` |
| `Live` | `Short` | `0.3495` | 9,250.00 USD | 1,390.00 USD | 0.00 USD | `+6.62%` | `3,989.10` |
| `Live` | `Short` | `0.3505` | 13,210.00 USD | 3,960.00 USD | 0.00 USD | `+6.93%` | `11,304.90` |
| `Live` | `Short` | `0.3575` | 13,710.00 USD | 497.00 USD | 0.00 USD | `+9.06%` | `1,390.20` |
| `Live` | `Short` | `0.3625` | 15,810.00 USD | 2,100.00 USD | 0.00 USD | `+10.59%` | `5,784.00` |
| `Live` | `Short` | `0.3675` | 17,910.00 USD | 2,100.00 USD | 0.00 USD | `+12.11%` | `5,705.10` |
| `Live` | `Short` | `0.3885` | 18,010.00 USD | 103.81 USD | 0.00 USD | `+18.52%` | `267.20` |
| `Live` | `Short` | `0.3915` | 22,750.00 USD | 4,740.00 USD | 0.00 USD | `+19.44%` | `12,118.00` |
| `Live` | `Short` | `0.4025` | 23,230.00 USD | 477.49 USD | 0.00 USD | `+22.79%` | `1,186.30` |
| `Live` | `Short` | `0.4035` | 23,470.00 USD | 236.85 USD | 0.00 USD | `+23.10%` | `587.00` |
| `Live` | `Short` | `0.4115` | 28,900.00 USD | 5,430.00 USD | 0.00 USD | `+25.54%` | `13,205.50` |
| `Live` | `Short` | `0.4205` | 30,600.00 USD | 1,700.00 USD | 0.00 USD | `+28.28%` | `4,032.60` |
| `Live` | `Short` | `0.4245` | 30,710.00 USD | 115.25 USD | 0.00 USD | `+29.50%` | `271.50` |
| `Live` | `Short` | `0.4445` | 31,600.00 USD | 889.00 USD | 0.00 USD | `+35.61%` | `2,000.00` |
| `Live` | `Short` | `0.4485` | 32,600.00 USD | 998.81 USD | 0.00 USD | `+36.83%` | `2,227.00` |
| `Live` | `Short` | `0.4575` | 43,080.00 USD | 10,480.00 USD | 0.00 USD | `+39.57%` | `22,906.80` |
| `Live` | `Short` | `0.4665` | 43,410.00 USD | 325.01 USD | 0.00 USD | `+42.32%` | `696.70` |
| `Live` | `Short` | `0.4795` | 47,770.00 USD | 4,360.00 USD | 0.00 USD | `+46.28%` | `9,100.00` |
| `Live` | `Short` | `0.5015` | 47,930.00 USD | 160.23 USD | 0.00 USD | `+52.99%` | `319.50` |
| `Live` | `Short` | `0.5065` | 477,950.00 USD | 430,020.00 USD | 0.00 USD | `+54.52%` | `849,000.00` |
| `Live` | `Short` | `0.5155` | 478,380.00 USD | 428.28 USD | 0.00 USD | `+57.27%` | `830.80` |
| `Live` | `Short` | `0.5305` | 492,860.00 USD | 14,480.00 USD | 0.00 USD | `+61.84%` | `27,300.00` |
| `Live` | `Short` | `0.5565` | 495,720.00 USD | 2,860.00 USD | 0.00 USD | `+69.77%` | `5,135.90` |
| `Live` | `Short` | `0.5825` | 922,110.00 USD | 426,390.00 USD | 0.00 USD | `+77.71%` | `732,000.00` |
| `Live` | `Short` | `0.5835` | 939,500.00 USD | 17,400.00 USD | 0.00 USD | `+78.01%` | `29,816.80` |
| `Live` | `Short` | `0.6015` | 1,060,000.00 USD | 121,080.00 USD | 0.00 USD | `+83.50%` | `201,296.00` |
| `Live` | `Short` | `0.6315` | 1,060,000.00 USD | 190.46 USD | 0.00 USD | `+92.65%` | `301.60` |
| `Live` | `Short` | `0.6465` | 1,060,000.00 USD | 121.61 USD | 0.00 USD | `+97.23%` | `188.10` |
| `Live` | `Short` | `0.6475` | 1,070,000.00 USD | 5,730.00 USD | 0.00 USD | `+97.54%` | `8,843.60` |
| `Live` | `Short` | `0.6485` | 1,070,000.00 USD | 1,100.00 USD | 0.00 USD | `+97.84%` | `1,692.90` |
| `Live` | `Short` | `0.6495` | 1,070,000.00 USD | 450.62 USD | 0.00 USD | `+98.15%` | `693.80` |

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
  * Current Rate: `2.53K` | Last 24h: `14.14K` | Last 3d: `34.03K` | Last 7d: `51.20K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0067%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0002%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0049%` | **USDT Bitget** | `0.0100%` |
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
| `5m` | 2,880.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `15m` | 2,510.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `30m` | -27,820.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1h` | -42,440.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `2h` | -81,010.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `4h` | 109,160.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `6h` | 119,350.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `8h` | -1,480.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `12h` | -67,120.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `24h` | -40,840.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1w` | -1,520,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,740,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+2.88K` | 15m=`+2.51K` | 1h=`-42.44K` | 24h=`-40.84K`
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
  * `2026-10-29 23:31:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:35 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:35 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:35 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:35 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:35 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:35 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3110` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.2735` (Risk Distance: `0.0460` pts)
  * +2.5R Take Profit: `0.4260`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3220` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3595` (Risk Distance: `0.0460` pts)
  * +2.5R Take Profit: `0.2070`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3311`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
