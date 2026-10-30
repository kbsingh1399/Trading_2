# 🏛️ SOVEREIGN CANDIDATE DOSSIER: CRVUSD
**Canonical Key**: `CRVUSD` | **Broker Instrument**: `CRVUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 07:39:19 IST` (`2026-10-30 02:09:19 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.2810` | **Live Ask Quote**: `0.3040` | **Mid Price**: `0.2925`
- **Spread Points**: `23.00` | **Spread BPS**: `786.32 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.2925` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.2945` | Lower -3.00σ Band: `0.2905`
  * Upper +2.51σ Band: `0.2941` | Lower -2.51σ Band: `0.2909`
  * Upper +2.01σ Band: `0.2937` | Lower -2.01σ Band: `0.2913`
  * Upper +2.00σ Band: `0.2937` | Lower -2.00σ Band: `0.2913`
  * Upper +1.28σ Band: `0.2933` | Lower -1.28σ Band: `0.2917`
  * Upper +1.00σ Band: `0.2931` | Lower -1.00σ Band: `0.2919`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.2925` | EMA-20=`0.2925` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.2925` (Slope: `+0.0000`) | EMA-100=`0.2925`
  * Institutional Anchors: EMA-144=`0.2925` | EMA-200=`0.2925` (Slope: `+0.0000`) | EMA-233=`0.2925`
- **Range Boundaries**: 24H High=`0.2954` | 24H Low=`0.2896` | Weekly High=`0.2984` | Weekly Low=`0.2866`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3010` (Distance: `-3.05%`)
  * Point of Control (POC) = `0.2970` (Distance: `-1.70%`)
  * Value Area Low (VAL) = `0.2860` (Distance: `+2.16%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3230` | POC=`0.3160` | VAL=`0.3100`
  * Prior Day Extremes: PDH=`0.3330` | PDL=`0.2890` | PDC=`0.2980`
  * Monday Range Blueprint: High=`0.3430` | Mid=`0.3340` | Low=`0.3250`
  * Developing Weekly Value Area: Weekly VAH=`0.3420` | Weekly POC=`0.3290` | Weekly VAL=`0.3180`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3040` | Low=`0.2800`
  * London Session (08:00-16:00 UTC): High=`0.2937` | Low=`0.2913`
  * New York Session (13:00-21:00 UTC): High=`0.2943` | Low=`0.2907`
  * Initial Balance (First Hour): IB High=`0.2934` | IB Low=`0.2916`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.2913` - `0.2937`
  * Optimal Trade Entry (OTE 0.705): `0.2931`
  * Structural Invalidation Anchor (0.786): `0.2948`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:28:02 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1860` | `0x12d2...f97f` | `LONG` | 1,055,651.74 USD | `3,602,046.40` | `0.3331` | `0.2936` | `0.000000` | -144,348.03 USD | `-13.67%` | `10X Cross` |

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
| `Live` | `Long` | `0.0735` | 5,210,000.00 USD | 0.00 USD | 3,100.00 USD | `-75.78%` | `42,146.00` |
| `Live` | `Long` | `0.0745` | 5,210,000.00 USD | 0.00 USD | 5,210.00 USD | `-75.45%` | `70,000.00` |
| `Live` | `Long` | `0.0785` | 5,200,000.00 USD | 0.00 USD | 2,330.00 USD | `-74.13%` | `29,622.60` |
| `Live` | `Long` | `0.0805` | 5,200,000.00 USD | 0.00 USD | 269.08 USD | `-73.47%` | `3,342.60` |
| `Live` | `Long` | `0.0845` | 5,200,000.00 USD | 0.00 USD | 441.29 USD | `-72.15%` | `5,222.40` |
| `Live` | `Long` | `0.0865` | 5,200,000.00 USD | 0.00 USD | 485.44 USD | `-71.49%` | `5,612.00` |
| `Live` | `Long` | `0.0925` | 5,200,000.00 USD | 0.00 USD | 4,700.00 USD | `-69.52%` | `50,846.60` |
| `Live` | `Long` | `0.1065` | 5,190,000.00 USD | 0.00 USD | 12,530.00 USD | `-64.90%` | `117,630.40` |
| `Live` | `Long` | `0.1125` | 5,180,000.00 USD | 0.00 USD | 2,110.00 USD | `-62.92%` | `18,735.40` |
| `Live` | `Long` | `0.1135` | 5,180,000.00 USD | 0.00 USD | 5,410.00 USD | `-62.59%` | `47,700.00` |
| `Live` | `Long` | `0.1225` | 5,170,000.00 USD | 0.00 USD | 116.35 USD | `-59.63%` | `949.80` |
| `Live` | `Long` | `0.1245` | 5,170,000.00 USD | 0.00 USD | 1,220.00 USD | `-58.97%` | `9,765.50` |
| `Live` | `Long` | `0.1255` | 5,170,000.00 USD | 0.00 USD | 4,300.00 USD | `-58.64%` | `34,264.40` |
| `Live` | `Long` | `0.1285` | 5,170,000.00 USD | 0.00 USD | 613.05 USD | `-57.65%` | `4,770.80` |
| `Live` | `Long` | `0.1295` | 5,170,000.00 USD | 0.00 USD | 689.70 USD | `-57.32%` | `5,325.90` |
| `Live` | `Long` | `0.1455` | 5,170,000.00 USD | 0.00 USD | 1,160.00 USD | `-52.05%` | `8,000.00` |
| `Live` | `Long` | `0.1465` | 5,160,000.00 USD | 0.00 USD | 1,720.00 USD | `-51.72%` | `11,739.70` |
| `Live` | `Long` | `0.1475` | 5,160,000.00 USD | 0.00 USD | 233.33 USD | `-51.39%` | `1,581.90` |
| `Live` | `Long` | `0.1505` | 5,160,000.00 USD | 0.00 USD | 1,210.00 USD | `-50.40%` | `8,042.60` |
| `Live` | `Long` | `0.1535` | 5,160,000.00 USD | 0.00 USD | 20,300.00 USD | `-49.41%` | `132,229.20` |
| `Live` | `Long` | `0.1565` | 5,140,000.00 USD | 0.00 USD | 1,180.00 USD | `-48.42%` | `7,514.20` |
| `Live` | `Long` | `0.1575` | 5,140,000.00 USD | 0.00 USD | 7,410.00 USD | `-48.09%` | `47,058.80` |
| `Live` | `Long` | `0.1645` | 5,130,000.00 USD | 0.00 USD | 397.60 USD | `-45.79%` | `2,417.00` |
| `Live` | `Long` | `0.1665` | 5,130,000.00 USD | 0.00 USD | 4,930.00 USD | `-45.13%` | `29,616.80` |
| `Live` | `Long` | `0.1695` | 5,130,000.00 USD | 0.00 USD | 6,310.00 USD | `-44.14%` | `37,201.60` |
| `Live` | `Long` | `0.1715` | 5,120,000.00 USD | 0.00 USD | 464.68 USD | `-43.48%` | `2,709.50` |
| `Live` | `Long` | `0.1725` | 5,120,000.00 USD | 0.00 USD | 4,670.00 USD | `-43.15%` | `27,059.00` |
| `Live` | `Long` | `0.1765` | 5,120,000.00 USD | 0.00 USD | 1,530.00 USD | `-41.83%` | `8,680.50` |
| `Live` | `Long` | `0.1775` | 5,110,000.00 USD | 0.00 USD | 14,130.00 USD | `-41.50%` | `79,610.90` |
| `Live` | `Long` | `0.1785` | 5,100,000.00 USD | 0.00 USD | 12,010.00 USD | `-41.17%` | `67,270.30` |
| `Live` | `Long` | `0.1795` | 5,090,000.00 USD | 0.00 USD | 13,180.00 USD | `-40.84%` | `73,444.60` |
| `Live` | `Long` | `0.1805` | 5,070,000.00 USD | 0.00 USD | 16,880.00 USD | `-40.51%` | `93,542.70` |
| `Live` | `Long` | `0.1835` | 5,060,000.00 USD | 0.00 USD | 179.10 USD | `-39.52%` | `976.00` |
| `Live` | `Long` | `0.1845` | 5,060,000.00 USD | 0.00 USD | 21,640.00 USD | `-39.20%` | `117,269.40` |
| `Live` | `Long` | `0.1865` | 5,040,000.00 USD | 0.00 USD | 38,040.00 USD | `-38.54%` | `203,946.00` |
| `Live` | `Long` | `0.1875` | 5,000,000.00 USD | 0.00 USD | 5,840.00 USD | `-38.21%` | `31,135.10` |
| `Live` | `Long` | `0.1885` | 4,990,000.00 USD | 0.00 USD | 1,660.00 USD | `-37.88%` | `8,802.20` |
| `Live` | `Long` | `0.1895` | 4,990,000.00 USD | 0.00 USD | 1,050.00 USD | `-37.55%` | `5,539.20` |
| `Live` | `Long` | `0.1905` | 4,990,000.00 USD | 0.00 USD | 952.50 USD | `-37.22%` | `5,000.00` |
| `Live` | `Long` | `0.1915` | 4,990,000.00 USD | 0.00 USD | 3,640.00 USD | `-36.89%` | `19,000.00` |
| `Live` | `Long` | `0.1925` | 4,980,000.00 USD | 0.00 USD | 928.81 USD | `-36.56%` | `4,825.00` |
| `Live` | `Long` | `0.1935` | 4,980,000.00 USD | 0.00 USD | 2,440.00 USD | `-36.23%` | `12,592.40` |
| `Live` | `Long` | `0.1955` | 4,980,000.00 USD | 0.00 USD | 13,190.00 USD | `-35.57%` | `67,459.20` |
| `Live` | `Long` | `0.1965` | 4,970,000.00 USD | 0.00 USD | 5,890.00 USD | `-35.24%` | `30,000.00` |
| `Live` | `Long` | `0.1985` | 4,960,000.00 USD | 0.00 USD | 1,100.00 USD | `-34.58%` | `5,563.00` |
| `Live` | `Long` | `0.1995` | 4,960,000.00 USD | 0.00 USD | 146,050.00 USD | `-34.25%` | `732,075.00` |
| `Live` | `Long` | `0.2025` | 4,820,000.00 USD | 0.00 USD | 8,880.00 USD | `-33.26%` | `43,861.60` |
| `Live` | `Long` | `0.2045` | 4,810,000.00 USD | 0.00 USD | 51,100.00 USD | `-32.60%` | `249,877.80` |
| `Live` | `Long` | `0.2085` | 4,760,000.00 USD | 0.00 USD | 2,520.00 USD | `-31.29%` | `12,063.00` |
| `Live` | `Long` | `0.2095` | 4,750,000.00 USD | 0.00 USD | 73,980.00 USD | `-30.96%` | `353,108.90` |
| `Live` | `Long` | `0.2105` | 4,680,000.00 USD | 0.00 USD | 9,500.00 USD | `-30.63%` | `45,147.80` |
| `Live` | `Long` | `0.2115` | 4,670,000.00 USD | 0.00 USD | 5,290.00 USD | `-30.30%` | `25,000.00` |
| `Live` | `Long` | `0.2125` | 4,660,000.00 USD | 0.00 USD | 893.41 USD | `-29.97%` | `4,204.30` |
| `Live` | `Long` | `0.2135` | 4,660,000.00 USD | 0.00 USD | 1,720.00 USD | `-29.64%` | `8,060.00` |
| `Live` | `Long` | `0.2155` | 4,660,000.00 USD | 0.00 USD | 30,170.00 USD | `-28.98%` | `140,000.00` |
| `Live` | `Long` | `0.2175` | 4,630,000.00 USD | 0.00 USD | 9,230.00 USD | `-28.32%` | `42,435.10` |
| `Live` | `Long` | `0.2195` | 4,620,000.00 USD | 0.00 USD | 436.01 USD | `-27.66%` | `1,986.40` |
| `Live` | `Long` | `0.2205` | 4,620,000.00 USD | 0.00 USD | 130,550.00 USD | `-27.33%` | `592,044.70` |
| `Live` | `Long` | `0.2215` | 4,490,000.00 USD | 0.00 USD | 974.95 USD | `-27.00%` | `4,401.60` |
| `Live` | `Long` | `0.2225` | 4,490,000.00 USD | 0.00 USD | 15,420.00 USD | `-26.67%` | `69,315.90` |
| `Live` | `Long` | `0.2255` | 4,470,000.00 USD | 0.00 USD | 676.50 USD | `-25.68%` | `3,000.00` |
| `Live` | `Long` | `0.2285` | 4,470,000.00 USD | 0.00 USD | 19,980.00 USD | `-24.69%` | `87,429.70` |
| `Live` | `Long` | `0.2295` | 4,450,000.00 USD | 0.00 USD | 1,520.00 USD | `-24.36%` | `6,610.20` |
| `Live` | `Long` | `0.2305` | 4,450,000.00 USD | 0.00 USD | 41,850.00 USD | `-24.04%` | `181,549.30` |
| `Live` | `Long` | `0.2315` | 4,410,000.00 USD | 0.00 USD | 131,630.00 USD | `-23.71%` | `568,586.80` |
| `Live` | `Long` | `0.2325` | 4,280,000.00 USD | 0.00 USD | 10,270.00 USD | `-23.38%` | `44,170.10` |
| `Live` | `Long` | `0.2335` | 4,270,000.00 USD | 0.00 USD | 132,820.00 USD | `-23.05%` | `568,834.10` |
| `Live` | `Long` | `0.2345` | 4,140,000.00 USD | 0.00 USD | 344.27 USD | `-22.72%` | `1,468.10` |
| `Live` | `Long` | `0.2385` | 4,140,000.00 USD | 0.00 USD | 100,890.00 USD | `-21.40%` | `422,998.70` |
| `Live` | `Long` | `0.2395` | 4,030,000.00 USD | 0.00 USD | 7,680.00 USD | `-21.07%` | `32,081.10` |
| `Live` | `Long` | `0.2405` | 4,030,000.00 USD | 0.00 USD | 13,650.00 USD | `-20.74%` | `56,745.50` |
| `Live` | `Long` | `0.2415` | 4,010,000.00 USD | 0.00 USD | 23,940.00 USD | `-20.41%` | `99,135.40` |
| `Live` | `Long` | `0.2425` | 3,990,000.00 USD | 0.00 USD | 123,330.00 USD | `-20.08%` | `508,580.10` |
| `Live` | `Long` | `0.2435` | 3,870,000.00 USD | 0.00 USD | 133,840.00 USD | `-19.75%` | `549,652.30` |
| `Live` | `Long` | `0.2445` | 3,730,000.00 USD | 0.00 USD | 1,040.00 USD | `-19.42%` | `4,237.20` |
| `Live` | `Long` | `0.2455` | 3,730,000.00 USD | 0.00 USD | 153,350.00 USD | `-19.09%` | `624,660.50` |
| `Live` | `Long` | `0.2475` | 3,580,000.00 USD | 0.00 USD | 9,480.00 USD | `-18.43%` | `38,294.10` |
| `Live` | `Long` | `0.2485` | 3,570,000.00 USD | 0.00 USD | 16,050.00 USD | `-18.10%` | `64,597.00` |
| `Live` | `Long` | `0.2495` | 3,550,000.00 USD | 0.00 USD | 28,290.00 USD | `-17.77%` | `113,393.90` |
| `Live` | `Long` | `0.2505` | 3,520,000.00 USD | 0.00 USD | 173,840.00 USD | `-17.44%` | `693,980.10` |
| `Live` | `Long` | `0.2525` | 3,350,000.00 USD | 0.00 USD | 5,390.00 USD | `-16.78%` | `21,359.60` |
| `Live` | `Long` | `0.2535` | 3,340,000.00 USD | 0.00 USD | 23,030.00 USD | `-16.46%` | `90,859.60` |
| `Live` | `Long` | `0.2545` | 3,320,000.00 USD | 0.00 USD | 22,030.00 USD | `-16.13%` | `86,545.50` |
| `Live` | `Long` | `0.2555` | 3,300,000.00 USD | 0.00 USD | 73,600.00 USD | `-15.80%` | `288,066.70` |
| `Live` | `Long` | `0.2565` | 3,230,000.00 USD | 0.00 USD | 823.90 USD | `-15.47%` | `3,212.10` |
| `Live` | `Long` | `0.2575` | 3,230,000.00 USD | 0.00 USD | 74,210.00 USD | `-15.14%` | `288,210.20` |
| `Live` | `Long` | `0.2585` | 3,150,000.00 USD | 0.00 USD | 31,370.00 USD | `-14.81%` | `121,365.50` |
| `Live` | `Long` | `0.2595` | 3,120,000.00 USD | 0.00 USD | 218,150.00 USD | `-14.48%` | `840,658.20` |
| `Live` | `Long` | `0.2605` | 2,900,000.00 USD | 0.00 USD | 6,800.00 USD | `-14.15%` | `26,111.50` |
| `Live` | `Long` | `0.2615` | 2,890,000.00 USD | 0.00 USD | 304,730.00 USD | `-13.82%` | `1,165,328.30` |
| `Live` | `Long` | `0.2625` | 2,590,000.00 USD | 0.00 USD | 4,870.00 USD | `-13.49%` | `18,540.50` |
| `Live` | `Long` | `0.2635` | 2,580,000.00 USD | 0.00 USD | 18,750.00 USD | `-13.16%` | `71,154.00` |
| `Live` | `Long` | `0.2655` | 2,570,000.00 USD | 0.00 USD | 80,780.00 USD | `-12.50%` | `304,259.40` |
| `Live` | `Long` | `0.2665` | 2,490,000.00 USD | 0.00 USD | 26,710.00 USD | `-12.17%` | `100,206.40` |
| `Live` | `Long` | `0.2675` | 2,460,000.00 USD | 0.00 USD | 14,640.00 USD | `-11.84%` | `54,730.60` |
| `Live` | `Long` | `0.2685` | 2,440,000.00 USD | 0.00 USD | 38,340.00 USD | `-11.51%` | `142,807.80` |
| `Live` | `Long` | `0.2695` | 2,410,000.00 USD | 0.00 USD | 171,800.00 USD | `-11.18%` | `637,492.80` |
| `Live` | `Long` | `0.2705` | 2,230,000.00 USD | 0.00 USD | 9,840.00 USD | `-10.85%` | `36,376.70` |
| `Live` | `Long` | `0.2715` | 2,220,000.00 USD | 0.00 USD | 42,540.00 USD | `-10.52%` | `156,679.70` |
| `Live` | `Long` | `0.2725` | 2,180,000.00 USD | 0.00 USD | 18,770.00 USD | `-10.19%` | `68,894.10` |
| `Live` | `Long` | `0.2735` | 2,160,000.00 USD | 0.00 USD | 64,290.00 USD | `-9.86%` | `235,050.70` |
| `Live` | `Long` | `0.2745` | 2,100,000.00 USD | 0.00 USD | 442,310.00 USD | `-9.53%` | `1,611,325.60` |
| `Live` | `Long` | `0.2755` | 1,660,000.00 USD | 0.00 USD | 30,710.00 USD | `-9.20%` | `111,456.20` |
| `Live` | `Long` | `0.2765` | 1,630,000.00 USD | 0.00 USD | 80,450.00 USD | `-8.88%` | `290,945.10` |
| `Live` | `Long` | `0.2775` | 1,540,000.00 USD | 0.00 USD | 420.33 USD | `-8.55%` | `1,514.70` |
| `Live` | `Long` | `0.2785` | 1,540,000.00 USD | 0.00 USD | 319.69 USD | `-8.22%` | `1,147.90` |
| `Live` | `Long` | `0.2795` | 1,540,000.00 USD | 0.00 USD | 152,320.00 USD | `-7.89%` | `544,979.90` |
| `Live` | `Long` | `0.2805` | 1,390,000.00 USD | 0.00 USD | 53,660.00 USD | `-7.56%` | `191,313.00` |
| `Live` | `Long` | `0.2815` | 1,340,000.00 USD | 0.00 USD | 35,240.00 USD | `-7.23%` | `125,183.90` |
| `Live` | `Long` | `0.2825` | 1,300,000.00 USD | 0.00 USD | 248,430.00 USD | `-6.90%` | `879,399.00` |
| `Live` | `Long` | `0.2835` | 1,050,000.00 USD | 0.00 USD | 115,260.00 USD | `-6.57%` | `406,551.50` |
| `Live` | `Long` | `0.2845` | 939,310.00 USD | 0.00 USD | 33,470.00 USD | `-6.24%` | `117,637.00` |
| `Live` | `Long` | `0.2855` | 905,840.00 USD | 0.00 USD | 50,000.00 USD | `-5.91%` | `175,131.50` |
| `Live` | `Long` | `0.2865` | 855,840.00 USD | 0.00 USD | 46,150.00 USD | `-5.58%` | `161,095.50` |
| `Live` | `Long` | `0.2875` | 809,680.00 USD | 0.00 USD | 12,890.00 USD | `-5.25%` | `44,842.10` |
| `Live` | `Long` | `0.2885` | 796,790.00 USD | 0.00 USD | 253,090.00 USD | `-4.92%` | `877,268.40` |
| `Live` | `Long` | `0.2895` | 543,700.00 USD | 0.00 USD | 261,190.00 USD | `-4.59%` | `902,214.20` |
| `Live` | `Long` | `0.2905` | 282,510.00 USD | 0.00 USD | 163,980.00 USD | `-4.26%` | `564,479.30` |
| `Live` | `Long` | `0.2915` | 118,530.00 USD | 0.00 USD | 89,150.00 USD | `-3.93%` | `305,830.40` |
| `Live` | `Long` | `0.2925` | 29,380.00 USD | 0.00 USD | 29,380.00 USD | `-3.60%` | `100,440.10` |
| `Live` | `Short` | `0.3065` | 15,320.00 USD | 15,320.00 USD | 0.00 USD | `+1.01%` | `50,000.00` |
| `Live` | `Short` | `0.3105` | 38,540.00 USD | 23,210.00 USD | 0.00 USD | `+2.33%` | `74,753.30` |
| `Live` | `Short` | `0.3175` | 45,940.00 USD | 7,400.00 USD | 0.00 USD | `+4.64%` | `23,312.20` |
| `Live` | `Short` | `0.3185` | 47,800.00 USD | 1,870.00 USD | 0.00 USD | `+4.97%` | `5,858.00` |
| `Live` | `Short` | `0.3215` | 53,190.00 USD | 5,380.00 USD | 0.00 USD | `+5.96%` | `16,745.80` |
| `Live` | `Short` | `0.3485` | 53,600.00 USD | 413.95 USD | 0.00 USD | `+14.85%` | `1,187.80` |
| `Live` | `Short` | `0.3545` | 54,050.00 USD | 446.07 USD | 0.00 USD | `+16.83%` | `1,258.30` |
| `Live` | `Short` | `0.3575` | 54,150.00 USD | 100.14 USD | 0.00 USD | `+17.82%` | `280.10` |
| `Live` | `Short` | `0.3625` | 56,240.00 USD | 2,100.00 USD | 0.00 USD | `+19.47%` | `5,784.00` |
| `Live` | `Short` | `0.3675` | 58,340.00 USD | 2,100.00 USD | 0.00 USD | `+21.12%` | `5,705.10` |
| `Live` | `Short` | `0.3855` | 58,460.00 USD | 119.04 USD | 0.00 USD | `+27.05%` | `308.80` |
| `Live` | `Short` | `0.3885` | 58,560.00 USD | 103.81 USD | 0.00 USD | `+28.04%` | `267.20` |
| `Live` | `Short` | `0.4025` | 59,040.00 USD | 477.49 USD | 0.00 USD | `+32.65%` | `1,186.30` |
| `Live` | `Short` | `0.4035` | 59,280.00 USD | 236.85 USD | 0.00 USD | `+32.98%` | `587.00` |
| `Live` | `Short` | `0.4205` | 60,970.00 USD | 1,700.00 USD | 0.00 USD | `+38.58%` | `4,032.60` |
| `Live` | `Short` | `0.4445` | 61,860.00 USD | 889.00 USD | 0.00 USD | `+46.49%` | `2,000.00` |
| `Live` | `Short` | `0.4465` | 62,240.00 USD | 379.44 USD | 0.00 USD | `+47.15%` | `849.80` |
| `Live` | `Short` | `0.4615` | 63,270.00 USD | 1,030.00 USD | 0.00 USD | `+52.09%` | `2,227.00` |
| `Live` | `Short` | `0.4785` | 63,450.00 USD | 179.29 USD | 0.00 USD | `+57.70%` | `374.70` |
| `Live` | `Short` | `0.4965` | 425,400.00 USD | 361,950.00 USD | 0.00 USD | `+63.63%` | `729,000.00` |
| `Live` | `Short` | `0.5025` | 427,010.00 USD | 1,610.00 USD | 0.00 USD | `+65.61%` | `3,205.50` |
| `Live` | `Short` | `0.5155` | 427,440.00 USD | 428.28 USD | 0.00 USD | `+69.89%` | `830.80` |
| `Live` | `Short` | `0.5235` | 490,260.00 USD | 62,820.00 USD | 0.00 USD | `+72.53%` | `120,000.00` |
| `Live` | `Short` | `0.5315` | 504,770.00 USD | 14,510.00 USD | 0.00 USD | `+75.16%` | `27,300.00` |
| `Live` | `Short` | `0.5565` | 507,620.00 USD | 2,860.00 USD | 0.00 USD | `+83.40%` | `5,135.90` |
| `Live` | `Short` | `0.5835` | 525,020.00 USD | 17,400.00 USD | 0.00 USD | `+92.30%` | `29,816.80` |
| `Live` | `Short` | `0.5845` | 525,250.00 USD | 232.16 USD | 0.00 USD | `+92.63%` | `397.20` |

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
  * Current Rate: `4.09K` | Last 24h: `9.20K` | Last 3d: `30.42K` | Last 7d: `57.33K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0073%` | **USDT OKX** | `0.0038%` |
| **USDT Bybit** | `0.0076%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0034%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0014%` | **USDT Bitget** | `0.0100%` |
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
| `5m` | 0.00 USD | -31,930.00 USD | **`DISTRIBUTION`** |
| `15m` | 0.00 USD | -289,280.00 USD | **`DISTRIBUTION`** |
| `30m` | 0.00 USD | -67,820.00 USD | **`DISTRIBUTION`** |
| `1h` | 0.00 USD | -1,020,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 0.00 USD | -1,880,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 0.00 USD | -1,970,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 0.00 USD | -5,200,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 0.00 USD | -6,750,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 0.00 USD | -7,510,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 0.00 USD | -8,290,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 0.00 USD | -20,020,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 0.00 USD | -63,980,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`-31.93K` | 15m=`-289.28K` | 1h=`-1.02M` | 24h=`-8.29M`
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
  * `2026-10-30 05:01:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:15:10 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:01:10 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:02:10 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.2860` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-0.9485` (Risk Distance: `1.23` pts)
  * +2.5R Take Profit: `3.37`
  * Mathematical Lot Sizing: **`8.10 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3010` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.54` (Risk Distance: `1.23` pts)
  * +2.5R Take Profit: `-2.79`
  * Mathematical Lot Sizing: **`8.10 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.2948`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
