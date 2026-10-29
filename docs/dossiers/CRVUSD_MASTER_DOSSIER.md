# 🏛️ SOVEREIGN CANDIDATE DOSSIER: CRVUSD
**Canonical Key**: `CRVUSD` | **Broker Instrument**: `CRVUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 00:35:21 IST` (`2026-10-29 19:05:21 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3120` | **Live Ask Quote**: `0.3350` | **Mid Price**: `0.3235`
- **Spread Points**: `23.00` | **Spread BPS**: `710.97 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3170` | VWAP Z-Score: `-1.30` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0025` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `31.88` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3285` | Lower -3.00σ Band: `0.3055`
  * Upper +2.51σ Band: `0.3266` | Lower -2.51σ Band: `0.3074`
  * Upper +2.01σ Band: `0.3247` | Lower -2.01σ Band: `0.3093`
  * Upper +2.00σ Band: `0.3247` | Lower -2.00σ Band: `0.3093`
  * Upper +1.28σ Band: `0.3219` | Lower -1.28σ Band: `0.3121`
  * Upper +1.00σ Band: `0.3208` | Lower -1.00σ Band: `0.3132`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3159` | EMA-20=`0.3176` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3180` (Slope: `+0.0000`) | EMA-100=`0.3193`
  * Institutional Anchors: EMA-144=`0.3204` | EMA-200=`0.3216` (Slope: `-0.1336`) | EMA-233=`0.3221`
- **Range Boundaries**: 24H High=`0.3340` | 24H Low=`0.3090` | Weekly High=`0.3380` | Weekly Low=`0.3090`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3210` (Distance: `+0.70%`)
  * Point of Control (POC) = `0.3150` (Distance: `+2.70%`)
  * Value Area Low (VAL) = `0.3110` (Distance: `+4.02%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3300` | POC=`0.3270` | VAL=`0.3240`
  * Prior Day Extremes: PDH=`0.3340` | PDL=`0.3210` | PDC=`0.3300`
  * Monday Range Blueprint: High=`0.3430` | Mid=`0.3340` | Low=`0.3250`
  * Developing Weekly Value Area: Weekly VAH=`0.3340` | Weekly POC=`0.3280` | Weekly VAL=`0.3200`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3330` | Low=`0.3090`
  * London Session (08:00-16:00 UTC): High=`0.3210` | Low=`0.3120`
  * New York Session (13:00-21:00 UTC): High=`0.3270` | Low=`0.3120`
  * Initial Balance (First Hour): IB High=`0.3190` | IB Low=`0.3140`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3222` - `0.3248`
  * Optimal Trade Entry (OTE 0.705): `0.3241`
  * Structural Invalidation Anchor (0.786): `0.3261`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:34:35 IST` |

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
| `Live` | `Long Liquidation` | `0.0725` | 3,690.00 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 453.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 2,330.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 32,460.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 485.44 USD | 5,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 1,580.00 USD | 5,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 719.81 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 134.25 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 1,530.00 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 564.03 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 116.35 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 4,300.00 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 6,000.00 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 176.88 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1375` | 1,150.00 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 427.50 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 546.89 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 397.60 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 12,720.00 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 752.44 USD | 5,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 464.68 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 7,950.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 37,870.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 28,080.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 1,530.00 USD | 5,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 14,130.00 USD | 5,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1785` | 12,900.00 USD | 5,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 13,180.00 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1805` | 16,880.00 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1835` | 4,770.00 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1845` | 1,480.00 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1865` | 9,460.00 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 11,460.00 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1885` | 1,660.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1895` | 1,050.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1905` | 2,660.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1925` | 359.78 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1935` | 2,150.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1945` | 511.07 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1955` | 13,190.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1965` | 2,230.00 USD | 5,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1975` | 20,310.00 USD | 5,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1985` | 1,100.00 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 146,050.00 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 18,380.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2055` | 1,060.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2075` | 6,090.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2085` | 2,390.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2105` | 30,380.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2125` | 521.03 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2135` | 34,730.00 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2145` | 1,730.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 153.87 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 130,550.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2215` | 25,340.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 667.50 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2235` | 8,940.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2285` | 12,040.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 337.59 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 63,770.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 135,690.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 17,320.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 1,940.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 92,210.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 13,650.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2415` | 36,950.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 407,510.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 19,800.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 5,530.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 18,110.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 9,480.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 4,030.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2495` | 28,290.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 167,340.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2525` | 73,400.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2535` | 8,000.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2545` | 39,840.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 59,960.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 823.90 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 16,260.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 46,140.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 1,700.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 13,120.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 33,800.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 14,650.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 10,710.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 7,330.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 14,790.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 20,470.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2695` | 7,750.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2705` | 1,900.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2715` | 46,010.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 21,260.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 367,390.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 9,700.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2765` | 5,970.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2775` | 158,550.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 6,160.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 70,670.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 87,930.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 44,690.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 84,670.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2835` | 328,760.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2845` | 18,360.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 23,820.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2865` | 218,760.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2875` | 125,350.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 567,680.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2895` | 42,410.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 208,310.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 205,070.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2925` | 10,690.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2935` | 13,940.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 38,460.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2955` | 3,960.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2965` | 273,630.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2975` | 14,370.00 USD | 795,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2985` | 58,260.00 USD | 781,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2995` | 1,890.00 USD | 722,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3005` | 33,480.00 USD | 721,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3015` | 60,430.00 USD | 687,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3025` | 5,630.00 USD | 627,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3035` | 170,860.00 USD | 621,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3045` | 768.34 USD | 450,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3055` | 72,120.00 USD | 449,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3065` | 56,040.00 USD | 377,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3075` | 60,980.00 USD | 321,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3085` | 23,710.00 USD | 260,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3095` | 8,430.00 USD | 237,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3105` | 33,040.00 USD | 228,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3115` | 81,680.00 USD | 195,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3125` | 3,120.00 USD | 113,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3135` | 5,080.00 USD | 110,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3155` | 14,410.00 USD | 105,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3165` | 2,080.00 USD | 91,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3175` | 26,860.00 USD | 89,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3185` | 60,270.00 USD | 62,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3195` | 2,050.00 USD | 2,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3435` | 5,610.00 USD | 5,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3445` | 151.92 USD | 5,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3465` | 522.80 USD | 6,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3485` | 1,570.00 USD | 7,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3495` | 1,390.00 USD | 9,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3505` | 3,960.00 USD | 13,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3575` | 497.00 USD | 13,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 2,100.00 USD | 15,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3675` | 2,100.00 USD | 17,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3885` | 103.81 USD | 18,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3915` | 4,740.00 USD | 22,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4025` | 477.49 USD | 23,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4035` | 236.85 USD | 23,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4115` | 5,430.00 USD | 28,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4205` | 1,700.00 USD | 30,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4245` | 115.25 USD | 30,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4445` | 889.00 USD | 31,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4485` | 998.81 USD | 32,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4575` | 10,480.00 USD | 43,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4665` | 325.01 USD | 43,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4795` | 4,360.00 USD | 47,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5015` | 160.23 USD | 47,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5065` | 430,020.00 USD | 477,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5155` | 428.28 USD | 478,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5305` | 14,480.00 USD | 492,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5565` | 2,860.00 USD | 495,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5825` | 426,390.00 USD | 922,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5835` | 17,400.00 USD | 939,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6015` | 121,080.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6315` | 190.46 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6465` | 121.61 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6475` | 5,730.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6485` | 1,100.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6495` | 450.62 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0675` | 5,790,000.00 USD | 0.00 USD | 3,430.00 USD | `-79.14%` | `50,846.60` |
| `Live` | `Long` | `0.0765` | 5,780,000.00 USD | 0.00 USD | 459.00 USD | `-76.35%` | `6,000.00` |
| `Live` | `Long` | `0.0775` | 5,780,000.00 USD | 0.00 USD | 953.06 USD | `-76.04%` | `12,297.60` |
| `Live` | `Long` | `0.0785` | 5,780,000.00 USD | 0.00 USD | 2,330.00 USD | `-75.73%` | `29,622.60` |
| `Live` | `Long` | `0.0865` | 5,780,000.00 USD | 0.00 USD | 485.44 USD | `-73.26%` | `5,612.00` |
| `Live` | `Long` | `0.0915` | 5,780,000.00 USD | 0.00 USD | 1,650.00 USD | `-71.72%` | `18,050.00` |
| `Live` | `Long` | `0.0925` | 5,780,000.00 USD | 0.00 USD | 35,950.00 USD | `-71.41%` | `388,690.50` |
| `Live` | `Long` | `0.0945` | 5,740,000.00 USD | 0.00 USD | 760.03 USD | `-70.79%` | `8,042.60` |
| `Live` | `Long` | `0.1225` | 5,740,000.00 USD | 0.00 USD | 116.35 USD | `-62.13%` | `949.80` |
| `Live` | `Long` | `0.1255` | 5,740,000.00 USD | 0.00 USD | 4,300.00 USD | `-61.21%` | `34,264.40` |
| `Live` | `Long` | `0.1345` | 5,740,000.00 USD | 0.00 USD | 6,330.00 USD | `-58.42%` | `47,058.80` |
| `Live` | `Long` | `0.1365` | 5,730,000.00 USD | 0.00 USD | 677.87 USD | `-57.81%` | `4,966.10` |
| `Live` | `Long` | `0.1375` | 5,730,000.00 USD | 0.00 USD | 1,150.00 USD | `-57.50%` | `8,365.30` |
| `Live` | `Long` | `0.1425` | 5,730,000.00 USD | 0.00 USD | 427.50 USD | `-55.95%` | `3,000.00` |
| `Live` | `Long` | `0.1445` | 5,730,000.00 USD | 0.00 USD | 1,850.00 USD | `-55.33%` | `12,814.90` |
| `Live` | `Long` | `0.1535` | 5,720,000.00 USD | 0.00 USD | 208.05 USD | `-52.55%` | `1,355.40` |
| `Live` | `Long` | `0.1605` | 5,720,000.00 USD | 0.00 USD | 611.68 USD | `-50.39%` | `3,811.10` |
| `Live` | `Long` | `0.1645` | 5,720,000.00 USD | 0.00 USD | 397.60 USD | `-49.15%` | `2,417.00` |
| `Live` | `Long` | `0.1655` | 5,720,000.00 USD | 0.00 USD | 6,620.00 USD | `-48.84%` | `40,000.00` |
| `Live` | `Long` | `0.1665` | 5,720,000.00 USD | 0.00 USD | 4,930.00 USD | `-48.53%` | `29,616.80` |
| `Live` | `Long` | `0.1715` | 5,710,000.00 USD | 0.00 USD | 7,320.00 USD | `-46.99%` | `42,709.50` |
| `Live` | `Long` | `0.1725` | 5,700,000.00 USD | 0.00 USD | 4,670.00 USD | `-46.68%` | `27,059.00` |
| `Live` | `Long` | `0.1745` | 5,700,000.00 USD | 0.00 USD | 4,090.00 USD | `-46.06%` | `23,439.20` |
| `Live` | `Long` | `0.1755` | 5,700,000.00 USD | 0.00 USD | 272.45 USD | `-45.75%` | `1,552.40` |
| `Live` | `Long` | `0.1765` | 5,700,000.00 USD | 0.00 USD | 1,530.00 USD | `-45.44%` | `8,680.50` |
| `Live` | `Long` | `0.1775` | 5,690,000.00 USD | 0.00 USD | 42,530.00 USD | `-45.13%` | `239,610.90` |
| `Live` | `Long` | `0.1785` | 5,650,000.00 USD | 0.00 USD | 40,250.00 USD | `-44.82%` | `225,516.90` |
| `Live` | `Long` | `0.1795` | 5,610,000.00 USD | 0.00 USD | 14,400.00 USD | `-44.51%` | `80,241.60` |
| `Live` | `Long` | `0.1805` | 5,600,000.00 USD | 0.00 USD | 16,880.00 USD | `-44.21%` | `93,542.70` |
| `Live` | `Long` | `0.1835` | 5,580,000.00 USD | 0.00 USD | 179.10 USD | `-43.28%` | `976.00` |
| `Live` | `Long` | `0.1845` | 5,580,000.00 USD | 0.00 USD | 1,480.00 USD | `-42.97%` | `8,024.00` |
| `Live` | `Long` | `0.1855` | 5,580,000.00 USD | 0.00 USD | 4,640.00 USD | `-42.66%` | `25,000.00` |
| `Live` | `Long` | `0.1865` | 5,570,000.00 USD | 0.00 USD | 9,460.00 USD | `-42.35%` | `50,699.40` |
| `Live` | `Long` | `0.1875` | 5,560,000.00 USD | 0.00 USD | 10,530.00 USD | `-42.04%` | `56,135.10` |
| `Live` | `Long` | `0.1885` | 5,550,000.00 USD | 0.00 USD | 7,310.00 USD | `-41.73%` | `38,802.20` |
| `Live` | `Long` | `0.1895` | 5,550,000.00 USD | 0.00 USD | 1,050.00 USD | `-41.42%` | `5,539.20` |
| `Live` | `Long` | `0.1925` | 5,550,000.00 USD | 0.00 USD | 3,040.00 USD | `-40.50%` | `15,809.20` |
| `Live` | `Long` | `0.1935` | 5,540,000.00 USD | 0.00 USD | 2,150.00 USD | `-40.19%` | `11,110.40` |
| `Live` | `Long` | `0.1955` | 5,540,000.00 USD | 0.00 USD | 13,190.00 USD | `-39.57%` | `67,459.20` |
| `Live` | `Long` | `0.1985` | 5,530,000.00 USD | 0.00 USD | 1,630.00 USD | `-38.64%` | `8,190.60` |
| `Live` | `Long` | `0.1995` | 5,530,000.00 USD | 0.00 USD | 146,050.00 USD | `-38.33%` | `732,075.00` |
| `Live` | `Long` | `0.2035` | 5,380,000.00 USD | 0.00 USD | 2,310.00 USD | `-37.10%` | `11,332.30` |
| `Live` | `Long` | `0.2045` | 5,380,000.00 USD | 0.00 USD | 18,380.00 USD | `-36.79%` | `89,877.80` |
| `Live` | `Long` | `0.2055` | 5,360,000.00 USD | 0.00 USD | 1,060.00 USD | `-36.48%` | `5,147.80` |
| `Live` | `Long` | `0.2075` | 5,360,000.00 USD | 0.00 USD | 21,330.00 USD | `-35.86%` | `102,814.70` |
| `Live` | `Long` | `0.2085` | 5,340,000.00 USD | 0.00 USD | 2,390.00 USD | `-35.55%` | `11,465.50` |
| `Live` | `Long` | `0.2105` | 5,330,000.00 USD | 0.00 USD | 30,380.00 USD | `-34.93%` | `144,300.00` |
| `Live` | `Long` | `0.2115` | 5,300,000.00 USD | 0.00 USD | 6,200.00 USD | `-34.62%` | `29,332.10` |
| `Live` | `Long` | `0.2125` | 5,300,000.00 USD | 0.00 USD | 521.03 USD | `-34.31%` | `2,451.90` |
| `Live` | `Long` | `0.2135` | 5,300,000.00 USD | 0.00 USD | 29,960.00 USD | `-34.01%` | `140,310.00` |
| `Live` | `Long` | `0.2195` | 5,270,000.00 USD | 0.00 USD | 153.87 USD | `-32.15%` | `701.00` |
| `Live` | `Long` | `0.2205` | 5,270,000.00 USD | 0.00 USD | 130,550.00 USD | `-31.84%` | `592,044.70` |
| `Live` | `Long` | `0.2215` | 5,140,000.00 USD | 0.00 USD | 30,880.00 USD | `-31.53%` | `139,423.00` |
| `Live` | `Long` | `0.2225` | 5,110,000.00 USD | 0.00 USD | 667.50 USD | `-31.22%` | `3,000.00` |
| `Live` | `Long` | `0.2235` | 5,100,000.00 USD | 0.00 USD | 8,940.00 USD | `-30.91%` | `39,998.20` |
| `Live` | `Long` | `0.2245` | 5,100,000.00 USD | 0.00 USD | 6,830.00 USD | `-30.60%` | `30,430.10` |
| `Live` | `Long` | `0.2285` | 5,090,000.00 USD | 0.00 USD | 12,150.00 USD | `-29.37%` | `53,170.90` |
| `Live` | `Long` | `0.2295` | 5,080,000.00 USD | 0.00 USD | 438.80 USD | `-29.06%` | `1,912.00` |
| `Live` | `Long` | `0.2305` | 5,080,000.00 USD | 0.00 USD | 45,160.00 USD | `-28.75%` | `195,912.20` |
| `Live` | `Long` | `0.2315` | 5,030,000.00 USD | 0.00 USD | 154,390.00 USD | `-28.44%` | `666,908.60` |
| `Live` | `Long` | `0.2325` | 4,880,000.00 USD | 0.00 USD | 17,320.00 USD | `-28.13%` | `74,516.00` |
| `Live` | `Long` | `0.2335` | 4,860,000.00 USD | 0.00 USD | 1,940.00 USD | `-27.82%` | `8,326.10` |
| `Live` | `Long` | `0.2375` | 4,860,000.00 USD | 0.00 USD | 6,410.00 USD | `-26.59%` | `26,996.60` |
| `Live` | `Long` | `0.2385` | 4,850,000.00 USD | 0.00 USD | 92,210.00 USD | `-26.28%` | `386,645.00` |
| `Live` | `Long` | `0.2405` | 4,760,000.00 USD | 0.00 USD | 13,650.00 USD | `-25.66%` | `56,745.50` |
| `Live` | `Long` | `0.2415` | 4,750,000.00 USD | 0.00 USD | 36,950.00 USD | `-25.35%` | `153,010.30` |
| `Live` | `Long` | `0.2425` | 4,710,000.00 USD | 0.00 USD | 140,760.00 USD | `-25.04%` | `580,469.40` |
| `Live` | `Long` | `0.2435` | 4,570,000.00 USD | 0.00 USD | 19,800.00 USD | `-24.73%` | `81,305.00` |
| `Live` | `Long` | `0.2445` | 4,550,000.00 USD | 0.00 USD | 637.31 USD | `-24.42%` | `2,606.60` |
| `Live` | `Long` | `0.2455` | 4,550,000.00 USD | 0.00 USD | 23,020.00 USD | `-24.11%` | `93,774.40` |
| `Live` | `Long` | `0.2475` | 4,520,000.00 USD | 0.00 USD | 9,480.00 USD | `-23.50%` | `38,294.10` |
| `Live` | `Long` | `0.2485` | 4,510,000.00 USD | 0.00 USD | 282,350.00 USD | `-23.19%` | `1,136,203.80` |
| `Live` | `Long` | `0.2495` | 4,230,000.00 USD | 0.00 USD | 28,290.00 USD | `-22.88%` | `113,393.90` |
| `Live` | `Long` | `0.2505` | 4,200,000.00 USD | 0.00 USD | 151,180.00 USD | `-22.57%` | `603,515.90` |
| `Live` | `Long` | `0.2515` | 4,050,000.00 USD | 0.00 USD | 16,230.00 USD | `-22.26%` | `64,516.00` |
| `Live` | `Long` | `0.2525` | 4,040,000.00 USD | 0.00 USD | 5,390.00 USD | `-21.95%` | `21,359.60` |
| `Live` | `Long` | `0.2545` | 4,030,000.00 USD | 0.00 USD | 90,570.00 USD | `-21.33%` | `355,888.80` |
| `Live` | `Long` | `0.2555` | 3,940,000.00 USD | 0.00 USD | 59,960.00 USD | `-21.02%` | `234,689.20` |
| `Live` | `Long` | `0.2565` | 3,880,000.00 USD | 0.00 USD | 18,780.00 USD | `-20.71%` | `73,212.10` |
| `Live` | `Long` | `0.2585` | 3,860,000.00 USD | 0.00 USD | 18,900.00 USD | `-20.10%` | `73,130.00` |
| `Live` | `Long` | `0.2595` | 3,840,000.00 USD | 0.00 USD | 46,140.00 USD | `-19.79%` | `177,797.60` |
| `Live` | `Long` | `0.2615` | 3,800,000.00 USD | 0.00 USD | 1,700.00 USD | `-19.17%` | `6,486.80` |
| `Live` | `Long` | `0.2635` | 3,800,000.00 USD | 0.00 USD | 34,110.00 USD | `-18.55%` | `129,456.20` |
| `Live` | `Long` | `0.2645` | 3,760,000.00 USD | 0.00 USD | 18,310.00 USD | `-18.24%` | `69,209.40` |
| `Live` | `Long` | `0.2655` | 3,740,000.00 USD | 0.00 USD | 16,020.00 USD | `-17.93%` | `60,345.40` |
| `Live` | `Long` | `0.2665` | 3,730,000.00 USD | 0.00 USD | 25,020.00 USD | `-17.62%` | `93,885.20` |
| `Live` | `Long` | `0.2675` | 3,700,000.00 USD | 0.00 USD | 9,990.00 USD | `-17.31%` | `37,343.80` |
| `Live` | `Long` | `0.2685` | 3,690,000.00 USD | 0.00 USD | 20,470.00 USD | `-17.00%` | `76,236.40` |
| `Live` | `Long` | `0.2695` | 3,670,000.00 USD | 0.00 USD | 7,750.00 USD | `-16.70%` | `28,742.90` |
| `Live` | `Long` | `0.2705` | 3,660,000.00 USD | 0.00 USD | 7,870.00 USD | `-16.39%` | `29,086.50` |
| `Live` | `Long` | `0.2715` | 3,660,000.00 USD | 0.00 USD | 46,010.00 USD | `-16.08%` | `169,467.20` |
| `Live` | `Long` | `0.2735` | 3,610,000.00 USD | 0.00 USD | 21,660.00 USD | `-15.46%` | `79,210.00` |
| `Live` | `Long` | `0.2745` | 3,590,000.00 USD | 0.00 USD | 402,330.00 USD | `-15.15%` | `1,465,667.90` |
| `Live` | `Long` | `0.2755` | 3,190,000.00 USD | 0.00 USD | 9,700.00 USD | `-14.84%` | `35,194.00` |
| `Live` | `Long` | `0.2765` | 3,180,000.00 USD | 0.00 USD | 5,970.00 USD | `-14.53%` | `21,598.50` |
| `Live` | `Long` | `0.2775` | 3,170,000.00 USD | 0.00 USD | 126,550.00 USD | `-14.22%` | `456,028.20` |
| `Live` | `Long` | `0.2785` | 3,040,000.00 USD | 0.00 USD | 8,260.00 USD | `-13.91%` | `29,673.60` |
| `Live` | `Long` | `0.2795` | 3,040,000.00 USD | 0.00 USD | 76,330.00 USD | `-13.60%` | `273,091.00` |
| `Live` | `Long` | `0.2805` | 2,960,000.00 USD | 0.00 USD | 87,930.00 USD | `-13.29%` | `313,473.20` |
| `Live` | `Long` | `0.2815` | 2,870,000.00 USD | 0.00 USD | 2,990.00 USD | `-12.99%` | `10,607.70` |
| `Live` | `Long` | `0.2825` | 2,870,000.00 USD | 0.00 USD | 124,730.00 USD | `-12.68%` | `441,504.90` |
| `Live` | `Long` | `0.2835` | 2,740,000.00 USD | 0.00 USD | 332,980.00 USD | `-12.37%` | `1,174,526.90` |
| `Live` | `Long` | `0.2845` | 2,410,000.00 USD | 0.00 USD | 17,510.00 USD | `-12.06%` | `61,548.90` |
| `Live` | `Long` | `0.2855` | 2,390,000.00 USD | 0.00 USD | 25,530.00 USD | `-11.75%` | `89,420.90` |
| `Live` | `Long` | `0.2865` | 2,370,000.00 USD | 0.00 USD | 215,600.00 USD | `-11.44%` | `752,543.70` |
| `Live` | `Long` | `0.2875` | 2,150,000.00 USD | 0.00 USD | 127,620.00 USD | `-11.13%` | `443,912.20` |
| `Live` | `Long` | `0.2885` | 2,020,000.00 USD | 0.00 USD | 566,580.00 USD | `-10.82%` | `1,963,870.80` |
| `Live` | `Long` | `0.2895` | 1,460,000.00 USD | 0.00 USD | 14,440.00 USD | `-10.51%` | `49,895.00` |
| `Live` | `Long` | `0.2905` | 1,440,000.00 USD | 0.00 USD | 203,160.00 USD | `-10.20%` | `699,339.00` |
| `Live` | `Long` | `0.2915` | 1,240,000.00 USD | 0.00 USD | 213,910.00 USD | `-9.89%` | `733,819.90` |
| `Live` | `Long` | `0.2925` | 1,030,000.00 USD | 0.00 USD | 10,690.00 USD | `-9.59%` | `36,560.50` |
| `Live` | `Long` | `0.2935` | 1,020,000.00 USD | 0.00 USD | 7,460.00 USD | `-9.28%` | `25,431.30` |
| `Live` | `Long` | `0.2945` | 1,010,000.00 USD | 0.00 USD | 38,460.00 USD | `-8.97%` | `130,590.00` |
| `Live` | `Long` | `0.2955` | 969,100.00 USD | 0.00 USD | 10,960.00 USD | `-8.66%` | `37,078.70` |
| `Live` | `Long` | `0.2965` | 958,140.00 USD | 0.00 USD | 273,630.00 USD | `-8.35%` | `922,857.00` |
| `Live` | `Long` | `0.2975` | 684,510.00 USD | 0.00 USD | 2,540.00 USD | `-8.04%` | `8,536.40` |
| `Live` | `Long` | `0.2985` | 681,970.00 USD | 0.00 USD | 53,970.00 USD | `-7.73%` | `180,793.60` |
| `Live` | `Long` | `0.2995` | 628,010.00 USD | 0.00 USD | 12,760.00 USD | `-7.42%` | `42,600.30` |
| `Live` | `Long` | `0.3005` | 615,250.00 USD | 0.00 USD | 25,510.00 USD | `-7.11%` | `84,878.10` |
| `Live` | `Long` | `0.3015` | 589,740.00 USD | 0.00 USD | 4,260.00 USD | `-6.80%` | `14,122.10` |
| `Live` | `Long` | `0.3025` | 585,490.00 USD | 0.00 USD | 5,630.00 USD | `-6.49%` | `18,610.70` |
| `Live` | `Long` | `0.3035` | 579,860.00 USD | 0.00 USD | 11,520.00 USD | `-6.19%` | `37,948.50` |
| `Live` | `Long` | `0.3045` | 568,340.00 USD | 0.00 USD | 768.34 USD | `-5.88%` | `2,523.30` |
| `Live` | `Long` | `0.3055` | 567,570.00 USD | 0.00 USD | 65,840.00 USD | `-5.57%` | `215,504.90` |
| `Live` | `Long` | `0.3065` | 501,730.00 USD | 0.00 USD | 171,920.00 USD | `-5.26%` | `560,910.50` |
| `Live` | `Long` | `0.3075` | 329,810.00 USD | 0.00 USD | 60,980.00 USD | `-4.95%` | `198,299.10` |
| `Live` | `Long` | `0.3085` | 268,840.00 USD | 0.00 USD | 40,780.00 USD | `-4.64%` | `132,194.60` |
| `Live` | `Long` | `0.3095` | 228,060.00 USD | 0.00 USD | 13,430.00 USD | `-4.33%` | `43,403.90` |
| `Live` | `Long` | `0.3105` | 214,620.00 USD | 0.00 USD | 41,300.00 USD | `-4.02%` | `133,004.00` |
| `Live` | `Long` | `0.3115` | 173,320.00 USD | 0.00 USD | 81,680.00 USD | `-3.71%` | `262,212.50` |
| `Live` | `Long` | `0.3135` | 91,640.00 USD | 0.00 USD | 568.38 USD | `-3.09%` | `1,813.00` |
| `Live` | `Long` | `0.3145` | 91,080.00 USD | 0.00 USD | 3,570.00 USD | `-2.79%` | `11,347.80` |
| `Live` | `Long` | `0.3155` | 87,510.00 USD | 0.00 USD | 14,410.00 USD | `-2.48%` | `45,681.90` |
| `Live` | `Long` | `0.3165` | 73,090.00 USD | 0.00 USD | 2,080.00 USD | `-2.17%` | `6,582.50` |
| `Live` | `Long` | `0.3175` | 71,010.00 USD | 0.00 USD | 27,670.00 USD | `-1.86%` | `87,153.10` |
| `Live` | `Long` | `0.3185` | 43,340.00 USD | 0.00 USD | 41,290.00 USD | `-1.55%` | `129,650.90` |
| `Live` | `Long` | `0.3195` | 2,050.00 USD | 0.00 USD | 2,050.00 USD | `-1.24%` | `6,405.40` |
| `Live` | `Short` | `0.3395` | 4,780.00 USD | 4,780.00 USD | 0.00 USD | `+4.94%` | `14,087.10` |
| `Live` | `Short` | `0.3405` | 8,400.00 USD | 3,620.00 USD | 0.00 USD | `+5.25%` | `10,623.80` |
| `Live` | `Short` | `0.3425` | 14,440.00 USD | 6,040.00 USD | 0.00 USD | `+5.87%` | `17,633.80` |
| `Live` | `Short` | `0.3455` | 15,820.00 USD | 1,380.00 USD | 0.00 USD | `+6.80%` | `3,992.80` |
| `Live` | `Short` | `0.3465` | 16,340.00 USD | 522.80 USD | 0.00 USD | `+7.11%` | `1,508.80` |
| `Live` | `Short` | `0.3495` | 17,170.00 USD | 830.24 USD | 0.00 USD | `+8.03%` | `2,375.50` |
| `Live` | `Short` | `0.3575` | 21,180.00 USD | 4,010.00 USD | 0.00 USD | `+10.51%` | `11,216.00` |
| `Live` | `Short` | `0.3625` | 23,280.00 USD | 2,100.00 USD | 0.00 USD | `+12.05%` | `5,784.00` |
| `Live` | `Short` | `0.3675` | 25,380.00 USD | 2,100.00 USD | 0.00 USD | `+13.60%` | `5,705.10` |
| `Live` | `Short` | `0.3885` | 25,480.00 USD | 103.81 USD | 0.00 USD | `+20.09%` | `267.20` |
| `Live` | `Short` | `0.4025` | 25,960.00 USD | 477.49 USD | 0.00 USD | `+24.42%` | `1,186.30` |
| `Live` | `Short` | `0.4035` | 26,190.00 USD | 236.85 USD | 0.00 USD | `+24.73%` | `587.00` |
| `Live` | `Short` | `0.4205` | 27,890.00 USD | 1,700.00 USD | 0.00 USD | `+29.98%` | `4,032.60` |
| `Live` | `Short` | `0.4245` | 28,000.00 USD | 115.25 USD | 0.00 USD | `+31.22%` | `271.50` |
| `Live` | `Short` | `0.4255` | 29,370.00 USD | 1,360.00 USD | 0.00 USD | `+31.53%` | `3,205.50` |
| `Live` | `Short` | `0.4435` | 32,740.00 USD | 3,370.00 USD | 0.00 USD | `+37.09%` | `7,600.00` |
| `Live` | `Short` | `0.4445` | 33,630.00 USD | 889.00 USD | 0.00 USD | `+37.40%` | `2,000.00` |
| `Live` | `Short` | `0.4495` | 34,630.00 USD | 1,000.00 USD | 0.00 USD | `+38.94%` | `2,227.00` |
| `Live` | `Short` | `0.4575` | 45,110.00 USD | 10,480.00 USD | 0.00 USD | `+41.42%` | `22,906.80` |
| `Live` | `Short` | `0.4665` | 45,430.00 USD | 325.01 USD | 0.00 USD | `+44.20%` | `696.70` |
| `Live` | `Short` | `0.4795` | 49,800.00 USD | 4,360.00 USD | 0.00 USD | `+48.22%` | `9,100.00` |
| `Live` | `Short` | `0.5015` | 49,960.00 USD | 160.23 USD | 0.00 USD | `+55.02%` | `319.50` |
| `Live` | `Short` | `0.5075` | 480,820.00 USD | 430,870.00 USD | 0.00 USD | `+56.87%` | `849,000.00` |
| `Live` | `Short` | `0.5155` | 481,250.00 USD | 428.28 USD | 0.00 USD | `+59.35%` | `830.80` |
| `Live` | `Short` | `0.5315` | 495,760.00 USD | 14,510.00 USD | 0.00 USD | `+64.29%` | `27,300.00` |
| `Live` | `Short` | `0.5565` | 498,620.00 USD | 2,860.00 USD | 0.00 USD | `+72.02%` | `5,135.90` |
| `Live` | `Short` | `0.5835` | 516,020.00 USD | 17,400.00 USD | 0.00 USD | `+80.37%` | `29,816.80` |
| `Live` | `Short` | `0.5865` | 945,340.00 USD | 429,320.00 USD | 0.00 USD | `+81.29%` | `732,000.00` |
| `Live` | `Short` | `0.6335` | 1,070,000.00 USD | 127,520.00 USD | 0.00 USD | `+95.82%` | `201,296.00` |
| `Live` | `Short` | `0.6465` | 1,070,000.00 USD | 121.61 USD | 0.00 USD | `+99.84%` | `188.10` |
| `Live` | `Short` | `0.6475` | 1,080,000.00 USD | 5,730.00 USD | 0.00 USD | `+100.15%` | `8,843.60` |

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
  * Current Rate: `1.65K` | Last 24h: `14.14K` | Last 3d: `34.03K` | Last 7d: `51.20K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0037%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0002%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0063%` | **USDT Bitget** | `0.0100%` |
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
| `5m` | 403.74 USD | 13,930.00 USD | **`ACCUMULATION`** |
| `15m` | 4,470.00 USD | 21,510.00 USD | **`ACCUMULATION`** |
| `30m` | -62,620.00 USD | -8,330.00 USD | **`DISTRIBUTION`** |
| `1h` | -205,210.00 USD | -458,030.00 USD | **`DISTRIBUTION`** |
| `2h` | -246,420.00 USD | -1,160,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -255,810.00 USD | -2,290,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -72,670.00 USD | -2,400,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -122,020.00 USD | -2,930,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -331,940.00 USD | -2,920,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -302,690.00 USD | -4,690,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -1,690,000.00 USD | -15,810,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -15,310,000.00 USD | -57,960,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+403.74` | 15m=`+4.47K` | 1h=`-205.21K` | 24h=`-302.69K`
* Futures Capital Netflows: 5m=`+13.93K` | 15m=`+21.51K` | 1h=`-458.03K` | 24h=`-4.69M`
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
  * `2026-10-30 00:17:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:29:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3210` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3585` (Risk Distance: `0.0460` pts)
  * +2.5R Take Profit: `0.2060`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3261`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
