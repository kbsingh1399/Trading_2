# 🏛️ SOVEREIGN CANDIDATE DOSSIER: CRVUSD
**Canonical Key**: `CRVUSD` | **Broker Instrument**: `CRVUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-29 23:13:21 IST` (`2026-10-29 17:43:21 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3190` | **Live Ask Quote**: `0.3410` | **Mid Price**: `0.3300`
- **Spread Points**: `22.00` | **Spread BPS**: `666.67 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3172` | VWAP Z-Score: `+0.46` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0023` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `47.57` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3289` | Lower -3.00σ Band: `0.3055`
  * Upper +2.51σ Band: `0.3269` | Lower -2.51σ Band: `0.3074`
  * Upper +2.01σ Band: `0.3250` | Lower -2.01σ Band: `0.3094`
  * Upper +2.00σ Band: `0.3250` | Lower -2.00σ Band: `0.3094`
  * Upper +1.28σ Band: `0.3222` | Lower -1.28σ Band: `0.3122`
  * Upper +1.00σ Band: `0.3211` | Lower -1.00σ Band: `0.3133`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3214` | EMA-20=`0.3203` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3190` (Slope: `+0.0000`) | EMA-100=`0.3199`
  * Institutional Anchors: EMA-144=`0.3209` | EMA-200=`0.3221` (Slope: `+0.0064`) | EMA-233=`0.3226`
- **Range Boundaries**: 24H High=`0.3340` | 24H Low=`0.3090` | Weekly High=`0.3420` | Weekly Low=`0.3090`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3220` (Distance: `+2.52%`)
  * Point of Control (POC) = `0.3150` (Distance: `+4.76%`)
  * Value Area Low (VAL) = `0.3110` (Distance: `+6.11%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `0.3287` - `0.3313`
  * Optimal Trade Entry (OTE 0.705): `0.3307`
  * Structural Invalidation Anchor (0.786): `0.3326`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:06:38 IST` |

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
| `Live` | `Long` | `0.0745` | 5,880,000.00 USD | 0.00 USD | 447.00 USD | `-77.75%` | `6,000.00` |
| `Live` | `Long` | `0.0765` | 5,880,000.00 USD | 0.00 USD | 1,380.00 USD | `-77.15%` | `18,050.00` |
| `Live` | `Long` | `0.0785` | 5,880,000.00 USD | 0.00 USD | 2,330.00 USD | `-76.56%` | `29,622.60` |
| `Live` | `Long` | `0.0865` | 5,880,000.00 USD | 0.00 USD | 485.44 USD | `-74.17%` | `5,612.00` |
| `Live` | `Long` | `0.0885` | 5,880,000.00 USD | 0.00 USD | 711.77 USD | `-73.57%` | `8,042.60` |
| `Live` | `Long` | `0.1095` | 5,880,000.00 USD | 0.00 USD | 417.32 USD | `-67.30%` | `3,811.10` |
| `Live` | `Long` | `0.1125` | 5,880,000.00 USD | 0.00 USD | 1,230.00 USD | `-66.40%` | `10,972.80` |
| `Live` | `Long` | `0.1195` | 5,880,000.00 USD | 0.00 USD | 5,620.00 USD | `-64.31%` | `47,058.80` |
| `Live` | `Long` | `0.1225` | 5,870,000.00 USD | 0.00 USD | 116.35 USD | `-63.41%` | `949.80` |
| `Live` | `Long` | `0.1255` | 5,870,000.00 USD | 0.00 USD | 4,300.00 USD | `-62.52%` | `34,264.40` |
| `Live` | `Long` | `0.1295` | 5,870,000.00 USD | 0.00 USD | 601.16 USD | `-61.32%` | `4,642.20` |
| `Live` | `Long` | `0.1375` | 5,870,000.00 USD | 0.00 USD | 1,150.00 USD | `-58.93%` | `8,365.30` |
| `Live` | `Long` | `0.1425` | 5,860,000.00 USD | 0.00 USD | 427.50 USD | `-57.44%` | `3,000.00` |
| `Live` | `Long` | `0.1505` | 5,860,000.00 USD | 0.00 USD | 1,020.00 USD | `-55.05%` | `6,797.00` |
| `Live` | `Long` | `0.1525` | 5,860,000.00 USD | 0.00 USD | 6,100.00 USD | `-54.45%` | `40,000.00` |
| `Live` | `Long` | `0.1545` | 5,860,000.00 USD | 0.00 USD | 3,860.00 USD | `-53.86%` | `25,000.00` |
| `Live` | `Long` | `0.1605` | 5,850,000.00 USD | 0.00 USD | 712.49 USD | `-52.07%` | `4,439.20` |
| `Live` | `Long` | `0.1625` | 5,850,000.00 USD | 0.00 USD | 6,500.00 USD | `-51.47%` | `40,000.00` |
| `Live` | `Long` | `0.1645` | 5,850,000.00 USD | 0.00 USD | 397.60 USD | `-50.87%` | `2,417.00` |
| `Live` | `Long` | `0.1665` | 5,850,000.00 USD | 0.00 USD | 4,930.00 USD | `-50.27%` | `29,616.80` |
| `Live` | `Long` | `0.1675` | 5,840,000.00 USD | 0.00 USD | 28,850.00 USD | `-49.97%` | `172,246.60` |
| `Live` | `Long` | `0.1695` | 5,810,000.00 USD | 0.00 USD | 27,120.00 USD | `-49.38%` | `160,000.00` |
| `Live` | `Long` | `0.1715` | 5,780,000.00 USD | 0.00 USD | 464.68 USD | `-48.78%` | `2,709.50` |
| `Live` | `Long` | `0.1725` | 5,780,000.00 USD | 0.00 USD | 8,980.00 USD | `-48.48%` | `52,059.00` |
| `Live` | `Long` | `0.1765` | 5,770,000.00 USD | 0.00 USD | 1,530.00 USD | `-47.29%` | `8,680.50` |
| `Live` | `Long` | `0.1775` | 5,770,000.00 USD | 0.00 USD | 14,130.00 USD | `-46.99%` | `79,610.90` |
| `Live` | `Long` | `0.1785` | 5,760,000.00 USD | 0.00 USD | 12,900.00 USD | `-46.69%` | `72,270.30` |
| `Live` | `Long` | `0.1795` | 5,750,000.00 USD | 0.00 USD | 15,690.00 USD | `-46.39%` | `87,384.80` |
| `Live` | `Long` | `0.1805` | 5,730,000.00 USD | 0.00 USD | 16,880.00 USD | `-46.09%` | `93,542.70` |
| `Live` | `Long` | `0.1815` | 5,710,000.00 USD | 0.00 USD | 18,660.00 USD | `-45.79%` | `102,814.70` |
| `Live` | `Long` | `0.1835` | 5,690,000.00 USD | 0.00 USD | 179.10 USD | `-45.20%` | `976.00` |
| `Live` | `Long` | `0.1845` | 5,690,000.00 USD | 0.00 USD | 1,480.00 USD | `-44.90%` | `8,024.00` |
| `Live` | `Long` | `0.1865` | 5,690,000.00 USD | 0.00 USD | 12,060.00 USD | `-44.30%` | `64,659.30` |
| `Live` | `Long` | `0.1875` | 5,680,000.00 USD | 0.00 USD | 11,460.00 USD | `-44.00%` | `61,135.10` |
| `Live` | `Long` | `0.1885` | 5,670,000.00 USD | 0.00 USD | 1,660.00 USD | `-43.70%` | `8,802.20` |
| `Live` | `Long` | `0.1895` | 5,670,000.00 USD | 0.00 USD | 1,050.00 USD | `-43.40%` | `5,539.20` |
| `Live` | `Long` | `0.1915` | 5,670,000.00 USD | 0.00 USD | 1,870.00 USD | `-42.81%` | `9,786.10` |
| `Live` | `Long` | `0.1925` | 5,670,000.00 USD | 0.00 USD | 359.78 USD | `-42.51%` | `1,869.00` |
| `Live` | `Long` | `0.1935` | 5,660,000.00 USD | 0.00 USD | 2,150.00 USD | `-42.21%` | `11,110.40` |
| `Live` | `Long` | `0.1955` | 5,660,000.00 USD | 0.00 USD | 13,190.00 USD | `-41.61%` | `67,459.20` |
| `Live` | `Long` | `0.1975` | 5,650,000.00 USD | 0.00 USD | 6,010.00 USD | `-41.01%` | `30,430.10` |
| `Live` | `Long` | `0.1985` | 5,640,000.00 USD | 0.00 USD | 1,100.00 USD | `-40.72%` | `5,563.00` |
| `Live` | `Long` | `0.1995` | 5,640,000.00 USD | 0.00 USD | 146,050.00 USD | `-40.42%` | `732,075.00` |
| `Live` | `Long` | `0.2005` | 5,500,000.00 USD | 0.00 USD | 5,880.00 USD | `-40.12%` | `29,332.10` |
| `Live` | `Long` | `0.2045` | 5,490,000.00 USD | 0.00 USD | 18,380.00 USD | `-38.92%` | `89,877.80` |
| `Live` | `Long` | `0.2055` | 5,470,000.00 USD | 0.00 USD | 1,060.00 USD | `-38.63%` | `5,147.80` |
| `Live` | `Long` | `0.2085` | 5,470,000.00 USD | 0.00 USD | 2,390.00 USD | `-37.73%` | `11,465.50` |
| `Live` | `Long` | `0.2095` | 5,470,000.00 USD | 0.00 USD | 126.08 USD | `-37.43%` | `601.80` |
| `Live` | `Long` | `0.2105` | 5,470,000.00 USD | 0.00 USD | 30,380.00 USD | `-37.13%` | `144,300.00` |
| `Live` | `Long` | `0.2125` | 5,440,000.00 USD | 0.00 USD | 2,240.00 USD | `-36.53%` | `10,532.70` |
| `Live` | `Long` | `0.2135` | 5,440,000.00 USD | 0.00 USD | 28,230.00 USD | `-36.24%` | `132,229.20` |
| `Live` | `Long` | `0.2195` | 5,410,000.00 USD | 0.00 USD | 153.87 USD | `-34.44%` | `701.00` |
| `Live` | `Long` | `0.2205` | 5,410,000.00 USD | 0.00 USD | 131,210.00 USD | `-34.15%` | `595,044.70` |
| `Live` | `Long` | `0.2215` | 5,280,000.00 USD | 0.00 USD | 25,340.00 USD | `-33.85%` | `114,401.60` |
| `Live` | `Long` | `0.2235` | 5,250,000.00 USD | 0.00 USD | 8,940.00 USD | `-33.25%` | `39,998.20` |
| `Live` | `Long` | `0.2265` | 5,240,000.00 USD | 0.00 USD | 18,290.00 USD | `-32.35%` | `80,768.90` |
| `Live` | `Long` | `0.2285` | 5,220,000.00 USD | 0.00 USD | 12,040.00 USD | `-31.76%` | `52,680.20` |
| `Live` | `Long` | `0.2295` | 5,210,000.00 USD | 0.00 USD | 967.55 USD | `-31.46%` | `4,215.90` |
| `Live` | `Long` | `0.2305` | 5,210,000.00 USD | 0.00 USD | 45,160.00 USD | `-31.16%` | `195,912.20` |
| `Live` | `Long` | `0.2315` | 5,170,000.00 USD | 0.00 USD | 19,940.00 USD | `-30.86%` | `86,139.70` |
| `Live` | `Long` | `0.2325` | 5,150,000.00 USD | 0.00 USD | 17,320.00 USD | `-30.56%` | `74,516.00` |
| `Live` | `Long` | `0.2335` | 5,130,000.00 USD | 0.00 USD | 31,680.00 USD | `-30.26%` | `135,690.10` |
| `Live` | `Long` | `0.2385` | 5,100,000.00 USD | 0.00 USD | 354,560.00 USD | `-28.77%` | `1,486,645.00` |
| `Live` | `Long` | `0.2405` | 4,740,000.00 USD | 0.00 USD | 13,650.00 USD | `-28.17%` | `56,745.50` |
| `Live` | `Long` | `0.2415` | 4,730,000.00 USD | 0.00 USD | 36,950.00 USD | `-27.87%` | `153,010.30` |
| `Live` | `Long` | `0.2425` | 4,690,000.00 USD | 0.00 USD | 109,880.00 USD | `-27.58%` | `453,105.40` |
| `Live` | `Long` | `0.2435` | 4,580,000.00 USD | 0.00 USD | 19,800.00 USD | `-27.28%` | `81,305.00` |
| `Live` | `Long` | `0.2445` | 4,560,000.00 USD | 0.00 USD | 5,530.00 USD | `-26.98%` | `22,606.60` |
| `Live` | `Long` | `0.2455` | 4,560,000.00 USD | 0.00 USD | 18,110.00 USD | `-26.68%` | `73,774.40` |
| `Live` | `Long` | `0.2465` | 4,540,000.00 USD | 0.00 USD | 17,250.00 USD | `-26.38%` | `70,000.00` |
| `Live` | `Long` | `0.2475` | 4,520,000.00 USD | 0.00 USD | 9,480.00 USD | `-26.08%` | `38,294.10` |
| `Live` | `Long` | `0.2485` | 4,510,000.00 USD | 0.00 USD | 20,060.00 USD | `-25.78%` | `80,719.80` |
| `Live` | `Long` | `0.2495` | 4,490,000.00 USD | 0.00 USD | 28,290.00 USD | `-25.48%` | `113,393.90` |
| `Live` | `Long` | `0.2505` | 4,460,000.00 USD | 0.00 USD | 218,650.00 USD | `-25.19%` | `872,859.20` |
| `Live` | `Long` | `0.2525` | 4,240,000.00 USD | 0.00 USD | 9,370.00 USD | `-24.59%` | `37,099.80` |
| `Live` | `Long` | `0.2535` | 4,230,000.00 USD | 0.00 USD | 8,200.00 USD | `-24.29%` | `32,332.40` |
| `Live` | `Long` | `0.2545` | 4,230,000.00 USD | 0.00 USD | 22,030.00 USD | `-23.99%` | `86,545.50` |
| `Live` | `Long` | `0.2555` | 4,200,000.00 USD | 0.00 USD | 68,910.00 USD | `-23.69%` | `269,689.20` |
| `Live` | `Long` | `0.2565` | 4,140,000.00 USD | 0.00 USD | 13,650.00 USD | `-23.39%` | `53,212.10` |
| `Live` | `Long` | `0.2585` | 4,120,000.00 USD | 0.00 USD | 23,480.00 USD | `-22.80%` | `90,837.40` |
| `Live` | `Long` | `0.2595` | 4,100,000.00 USD | 0.00 USD | 46,140.00 USD | `-22.50%` | `177,797.60` |
| `Live` | `Long` | `0.2615` | 4,050,000.00 USD | 0.00 USD | 1,700.00 USD | `-21.90%` | `6,486.80` |
| `Live` | `Long` | `0.2625` | 4,050,000.00 USD | 0.00 USD | 9,030.00 USD | `-21.60%` | `34,402.20` |
| `Live` | `Long` | `0.2635` | 4,040,000.00 USD | 0.00 USD | 20,760.00 USD | `-21.30%` | `78,768.90` |
| `Live` | `Long` | `0.2645` | 4,020,000.00 USD | 0.00 USD | 5,390.00 USD | `-21.00%` | `20,384.10` |
| `Live` | `Long` | `0.2655` | 4,020,000.00 USD | 0.00 USD | 196,560.00 USD | `-20.71%` | `740,345.40` |
| `Live` | `Long` | `0.2665` | 3,820,000.00 USD | 0.00 USD | 2,000.00 USD | `-20.41%` | `7,501.40` |
| `Live` | `Long` | `0.2675` | 3,820,000.00 USD | 0.00 USD | 14,790.00 USD | `-20.11%` | `55,307.60` |
| `Live` | `Long` | `0.2685` | 3,800,000.00 USD | 0.00 USD | 20,470.00 USD | `-19.81%` | `76,236.40` |
| `Live` | `Long` | `0.2695` | 3,780,000.00 USD | 0.00 USD | 61,670.00 USD | `-19.51%` | `228,845.00` |
| `Live` | `Long` | `0.2705` | 3,720,000.00 USD | 0.00 USD | 1,900.00 USD | `-19.21%` | `7,034.00` |
| `Live` | `Long` | `0.2715` | 3,720,000.00 USD | 0.00 USD | 46,010.00 USD | `-18.91%` | `169,467.20` |
| `Live` | `Long` | `0.2735` | 3,670,000.00 USD | 0.00 USD | 21,260.00 USD | `-18.32%` | `77,741.90` |
| `Live` | `Long` | `0.2745` | 3,650,000.00 USD | 0.00 USD | 312,470.00 USD | `-18.02%` | `1,138,306.10` |
| `Live` | `Long` | `0.2755` | 3,340,000.00 USD | 0.00 USD | 9,700.00 USD | `-17.72%` | `35,194.00` |
| `Live` | `Long` | `0.2765` | 3,330,000.00 USD | 0.00 USD | 5,970.00 USD | `-17.42%` | `21,598.50` |
| `Live` | `Long` | `0.2775` | 3,320,000.00 USD | 0.00 USD | 158,150.00 USD | `-17.12%` | `569,892.20` |
| `Live` | `Long` | `0.2785` | 3,160,000.00 USD | 0.00 USD | 43,440.00 USD | `-16.82%` | `155,977.10` |
| `Live` | `Long` | `0.2795` | 3,120,000.00 USD | 0.00 USD | 70,670.00 USD | `-16.52%` | `252,856.00` |
| `Live` | `Long` | `0.2805` | 3,050,000.00 USD | 0.00 USD | 87,930.00 USD | `-16.23%` | `313,473.20` |
| `Live` | `Long` | `0.2815` | 2,960,000.00 USD | 0.00 USD | 2,240.00 USD | `-15.93%` | `7,941.30` |
| `Live` | `Long` | `0.2825` | 2,960,000.00 USD | 0.00 USD | 84,670.00 USD | `-15.63%` | `299,723.00` |
| `Live` | `Long` | `0.2835` | 2,880,000.00 USD | 0.00 USD | 329,170.00 USD | `-15.33%` | `1,161,109.20` |
| `Live` | `Long` | `0.2845` | 2,550,000.00 USD | 0.00 USD | 25,100.00 USD | `-15.03%` | `88,212.60` |
| `Live` | `Long` | `0.2855` | 2,520,000.00 USD | 0.00 USD | 23,820.00 USD | `-14.73%` | `83,420.90` |
| `Live` | `Long` | `0.2865` | 2,500,000.00 USD | 0.00 USD | 218,760.00 USD | `-14.43%` | `763,577.60` |
| `Live` | `Long` | `0.2875` | 2,280,000.00 USD | 0.00 USD | 125,350.00 USD | `-14.14%` | `435,983.70` |
| `Live` | `Long` | `0.2885` | 2,150,000.00 USD | 0.00 USD | 567,680.00 USD | `-13.84%` | `1,967,678.70` |
| `Live` | `Long` | `0.2895` | 1,590,000.00 USD | 0.00 USD | 42,410.00 USD | `-13.54%` | `146,499.90` |
| `Live` | `Long` | `0.2905` | 1,540,000.00 USD | 0.00 USD | 201,430.00 USD | `-13.24%` | `693,397.20` |
| `Live` | `Long` | `0.2915` | 1,340,000.00 USD | 0.00 USD | 30,170.00 USD | `-12.94%` | `103,482.00` |
| `Live` | `Long` | `0.2925` | 1,310,000.00 USD | 0.00 USD | 186,190.00 USD | `-12.64%` | `636,560.50` |
| `Live` | `Long` | `0.2935` | 1,130,000.00 USD | 0.00 USD | 33,540.00 USD | `-12.34%` | `114,261.50` |
| `Live` | `Long` | `0.2945` | 1,090,000.00 USD | 0.00 USD | 30,500.00 USD | `-12.04%` | `103,571.70` |
| `Live` | `Long` | `0.2955` | 1,060,000.00 USD | 0.00 USD | 16,010.00 USD | `-11.75%` | `54,194.60` |
| `Live` | `Long` | `0.2965` | 1,050,000.00 USD | 0.00 USD | 273,630.00 USD | `-11.45%` | `922,857.00` |
| `Live` | `Long` | `0.2975` | 772,030.00 USD | 0.00 USD | 2,540.00 USD | `-11.15%` | `8,536.40` |
| `Live` | `Long` | `0.2985` | 769,490.00 USD | 0.00 USD | 53,970.00 USD | `-10.85%` | `180,793.60` |
| `Live` | `Long` | `0.2995` | 715,530.00 USD | 0.00 USD | 1,890.00 USD | `-10.55%` | `6,321.30` |
| `Live` | `Long` | `0.3005` | 713,630.00 USD | 0.00 USD | 24,630.00 USD | `-10.25%` | `81,968.30` |
| `Live` | `Long` | `0.3015` | 689,000.00 USD | 0.00 USD | 236,270.00 USD | `-9.95%` | `783,644.80` |
| `Live` | `Long` | `0.3025` | 452,730.00 USD | 0.00 USD | 13,250.00 USD | `-9.66%` | `43,814.90` |
| `Live` | `Long` | `0.3035` | 439,480.00 USD | 0.00 USD | 11,460.00 USD | `-9.36%` | `37,765.70` |
| `Live` | `Long` | `0.3045` | 428,020.00 USD | 0.00 USD | 768.34 USD | `-9.06%` | `2,523.30` |
| `Live` | `Long` | `0.3055` | 427,250.00 USD | 0.00 USD | 72,120.00 USD | `-8.76%` | `236,081.50` |
| `Live` | `Long` | `0.3065` | 355,130.00 USD | 0.00 USD | 18,670.00 USD | `-8.46%` | `60,910.50` |
| `Live` | `Long` | `0.3075` | 336,460.00 USD | 0.00 USD | 63,560.00 USD | `-8.16%` | `206,690.30` |
| `Live` | `Long` | `0.3085` | 272,900.00 USD | 0.00 USD | 33,070.00 USD | `-7.86%` | `107,205.50` |
| `Live` | `Long` | `0.3095` | 239,830.00 USD | 0.00 USD | 19,290.00 USD | `-7.57%` | `62,341.10` |
| `Live` | `Long` | `0.3105` | 220,530.00 USD | 0.00 USD | 28,020.00 USD | `-7.27%` | `90,229.10` |
| `Live` | `Long` | `0.3115` | 192,520.00 USD | 0.00 USD | 81,680.00 USD | `-6.97%` | `262,212.50` |
| `Live` | `Long` | `0.3125` | 110,840.00 USD | 0.00 USD | 3,430.00 USD | `-6.67%` | `10,977.90` |
| `Live` | `Long` | `0.3135` | 107,410.00 USD | 0.00 USD | 975.30 USD | `-6.37%` | `3,111.00` |
| `Live` | `Long` | `0.3155` | 106,430.00 USD | 0.00 USD | 14,410.00 USD | `-5.77%` | `45,681.90` |
| `Live` | `Long` | `0.3165` | 92,020.00 USD | 0.00 USD | 2,080.00 USD | `-5.47%` | `6,582.50` |
| `Live` | `Long` | `0.3175` | 89,940.00 USD | 0.00 USD | 1,070.00 USD | `-5.18%` | `3,380.50` |
| `Live` | `Long` | `0.3185` | 88,860.00 USD | 0.00 USD | 60,870.00 USD | `-4.88%` | `191,101.60` |
| `Live` | `Long` | `0.3195` | 28,000.00 USD | 0.00 USD | 28,000.00 USD | `-4.58%` | `87,624.60` |
| `Live` | `Short` | `0.3495` | 2,230.00 USD | 2,230.00 USD | 0.00 USD | `+4.38%` | `6,384.30` |
| `Live` | `Short` | `0.3505` | 6,190.00 USD | 3,960.00 USD | 0.00 USD | `+4.68%` | `11,304.90` |
| `Live` | `Short` | `0.3525` | 8,430.00 USD | 2,240.00 USD | 0.00 USD | `+5.28%` | `6,356.60` |
| `Live` | `Short` | `0.3575` | 8,930.00 USD | 497.00 USD | 0.00 USD | `+6.77%` | `1,390.20` |
| `Live` | `Short` | `0.3625` | 11,030.00 USD | 2,100.00 USD | 0.00 USD | `+8.26%` | `5,784.00` |
| `Live` | `Short` | `0.3675` | 13,120.00 USD | 2,100.00 USD | 0.00 USD | `+9.76%` | `5,705.10` |
| `Live` | `Short` | `0.3885` | 13,230.00 USD | 103.81 USD | 0.00 USD | `+16.03%` | `267.20` |
| `Live` | `Short` | `0.3915` | 17,970.00 USD | 4,740.00 USD | 0.00 USD | `+16.93%` | `12,118.00` |
| `Live` | `Short` | `0.4025` | 18,450.00 USD | 477.49 USD | 0.00 USD | `+20.21%` | `1,186.30` |
| `Live` | `Short` | `0.4035` | 18,690.00 USD | 236.85 USD | 0.00 USD | `+20.51%` | `587.00` |
| `Live` | `Short` | `0.4045` | 19,980.00 USD | 1,300.00 USD | 0.00 USD | `+20.81%` | `3,205.50` |
| `Live` | `Short` | `0.4205` | 21,680.00 USD | 1,700.00 USD | 0.00 USD | `+25.59%` | `4,032.60` |
| `Live` | `Short` | `0.4245` | 21,790.00 USD | 115.25 USD | 0.00 USD | `+26.78%` | `271.50` |
| `Live` | `Short` | `0.4445` | 22,680.00 USD | 889.00 USD | 0.00 USD | `+32.75%` | `2,000.00` |
| `Live` | `Short` | `0.4455` | 23,680.00 USD | 992.13 USD | 0.00 USD | `+33.05%` | `2,227.00` |
| `Live` | `Short` | `0.4575` | 34,160.00 USD | 10,480.00 USD | 0.00 USD | `+36.64%` | `22,906.80` |
| `Live` | `Short` | `0.4665` | 34,480.00 USD | 325.01 USD | 0.00 USD | `+39.32%` | `696.70` |
| `Live` | `Short` | `0.4795` | 38,840.00 USD | 4,360.00 USD | 0.00 USD | `+43.21%` | `9,100.00` |
| `Live` | `Short` | `0.4945` | 399,330.00 USD | 360,490.00 USD | 0.00 USD | `+47.69%` | `729,000.00` |
| `Live` | `Short` | `0.5015` | 399,490.00 USD | 160.23 USD | 0.00 USD | `+49.78%` | `319.50` |
| `Live` | `Short` | `0.5035` | 459,910.00 USD | 60,420.00 USD | 0.00 USD | `+50.37%` | `120,000.00` |
| `Live` | `Short` | `0.5155` | 460,340.00 USD | 428.28 USD | 0.00 USD | `+53.96%` | `830.80` |
| `Live` | `Short` | `0.5305` | 474,830.00 USD | 14,480.00 USD | 0.00 USD | `+58.44%` | `27,300.00` |
| `Live` | `Short` | `0.5485` | 876,330.00 USD | 401,500.00 USD | 0.00 USD | `+63.81%` | `732,000.00` |
| `Live` | `Short` | `0.5525` | 987,540.00 USD | 111,220.00 USD | 0.00 USD | `+65.01%` | `201,296.00` |
| `Live` | `Short` | `0.5565` | 990,400.00 USD | 2,860.00 USD | 0.00 USD | `+66.20%` | `5,135.90` |
| `Live` | `Short` | `0.5835` | 1,010,000.00 USD | 17,400.00 USD | 0.00 USD | `+74.27%` | `29,816.80` |
| `Live` | `Short` | `0.6315` | 1,010,000.00 USD | 190.46 USD | 0.00 USD | `+88.60%` | `301.60` |
| `Live` | `Short` | `0.6425` | 1,010,000.00 USD | 445.77 USD | 0.00 USD | `+91.89%` | `693.80` |
| `Live` | `Short` | `0.6465` | 1,010,000.00 USD | 121.61 USD | 0.00 USD | `+93.08%` | `188.10` |
| `Live` | `Short` | `0.6475` | 1,010,000.00 USD | 5,730.00 USD | 0.00 USD | `+93.38%` | `8,843.60` |
| `Live` | `Short` | `0.6485` | 1,020,000.00 USD | 1,100.00 USD | 0.00 USD | `+93.68%` | `1,692.90` |
| `Live` | `Short` | `0.6575` | 1,040,000.00 USD | 19,730.00 USD | 0.00 USD | `+96.37%` | `30,000.00` |

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
  * Current Rate: `5.65K` | Last 24h: `14.14K` | Last 3d: `34.03K` | Last 7d: `51.20K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0089%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0094%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0051%` | **USDT Bitget** | `0.0100%` |
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
| `5m` | 280.47 USD | 15,880.00 USD | **`ACCUMULATION`** |
| `15m` | 9,450.00 USD | 91,910.00 USD | **`ACCUMULATION`** |
| `30m` | -27,300.00 USD | -129,910.00 USD | **`DISTRIBUTION`** |
| `1h` | -83,890.00 USD | -692,430.00 USD | **`DISTRIBUTION`** |
| `2h` | -74,200.00 USD | -1,160,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 138,700.00 USD | -1,460,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 108,680.00 USD | -1,520,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 3,030.00 USD | -1,910,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -49,960.00 USD | -2,100,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 32,450.00 USD | -3,650,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -1,550,000.00 USD | -15,580,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,880,000.00 USD | -55,970,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+280.47` | 15m=`+9.45K` | 1h=`-83.89K` | 24h=`+32.45K`
* Futures Capital Netflows: 5m=`+15.88K` | 15m=`+91.91K` | 1h=`-692.43K` | 24h=`-3.65M`
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
  * `2026-10-29 23:01:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:02:06 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `0.2752` (Risk Distance: `0.0440` pts)
  * +2.5R Take Profit: `0.4210`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3220` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3578` (Risk Distance: `0.0440` pts)
  * +2.5R Take Profit: `0.2120`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3326`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
