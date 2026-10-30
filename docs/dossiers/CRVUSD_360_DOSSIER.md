# 🏛️ SOVEREIGN CANDIDATE DOSSIER: CRVUSD
**Canonical Key**: `CRVUSD` | **Broker Instrument**: `CRVUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 11:11:09 IST` (`2026-10-30 05:41:09 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.2630` | **Live Ask Quote**: `0.2860` | **Mid Price**: `0.2745`
- **Spread Points**: `23.00` | **Spread BPS**: `837.89 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.2745` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.2764` | Lower -3.00σ Band: `0.2726`
  * Upper +2.51σ Band: `0.2760` | Lower -2.51σ Band: `0.2730`
  * Upper +2.01σ Band: `0.2757` | Lower -2.01σ Band: `0.2733`
  * Upper +2.00σ Band: `0.2756` | Lower -2.00σ Band: `0.2734`
  * Upper +1.28σ Band: `0.2753` | Lower -1.28σ Band: `0.2737`
  * Upper +1.00σ Band: `0.2750` | Lower -1.00σ Band: `0.2740`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.2745` | EMA-20=`0.2745` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.2745` (Slope: `+0.0000`) | EMA-100=`0.2745`
  * Institutional Anchors: EMA-144=`0.2745` | EMA-200=`0.2745` (Slope: `+0.0000`) | EMA-233=`0.2745`
- **Range Boundaries**: 24H High=`0.2772` | 24H Low=`0.2718` | Weekly High=`0.2800` | Weekly Low=`0.2690`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.2920` (Distance: `-6.08%`)
  * Point of Control (POC) = `0.2630` (Distance: `+4.36%`)
  * Value Area Low (VAL) = `0.2570` (Distance: `+6.85%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3230` | POC=`0.3160` | VAL=`0.3100`
  * Prior Day Extremes: PDH=`0.3330` | PDL=`0.2890` | PDC=`0.2980`
  * Monday Range Blueprint: High=`0.3430` | Mid=`0.3340` | Low=`0.3250`
  * Developing Weekly Value Area: Weekly VAH=`0.3420` | Weekly POC=`0.3280` | Weekly VAL=`0.3150`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3040` | Low=`0.2530`
  * London Session (08:00-16:00 UTC): High=`0.2630` | Low=`0.2580`
  * New York Session (13:00-21:00 UTC): High=`0.2761` | Low=`0.2729`
  * Initial Balance (First Hour): IB High=`0.2630` | IB Low=`0.2580`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.2734` - `0.2756`
  * Optimal Trade Entry (OTE 0.705): `0.2750`
  * Structural Invalidation Anchor (0.786): `0.2767`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:04:06 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1878` | `0x12d2...f97f` | `LONG` | 1,089,190.72 USD | `3,972,828.70` | `0.3272` | `0.2735` | `0.000000` | -210,648.02 USD | `-19.34%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3239` | 1,102.66 USD | `-` | `NEWS_INTEL` | `-` | #CRV Liquidated Short: 1.10K USD at 0.3239 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `0.3238` | 41.83 USD | `-` | `NEWS_INTEL` | `-` | #CRV Liquidated Short: 0.04K USD at 0.3238 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `0.3239` | 106.01 USD | `-` | `NEWS_INTEL` | `-` | #CRV Liquidated Short: 0.11K USD at 0.3239 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `0.3221` | 86.88 USD | `-` | `NEWS_INTEL` | `-` | #CRV Liquidated Short: 0.09K USD at 0.3221 USD [API] | `2026-10-29 02:34:23` |


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
| `Live` | `Long Liquidation` | `0.0555` | 124.70 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 2,580.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 319.15 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 1,250.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 3,580.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 119.43 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 2,330.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 8,590.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 485.44 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 695.06 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 971.67 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,220.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 5,620.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 116.35 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 4,630.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 613.05 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 21,040.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 14,050.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 1,140.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 941.69 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 12,380.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 1,190.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 20,300.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 3,910.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 2,500.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 7,600.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 278.30 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 464.68 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 35,390.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 2,020.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 1,340.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 14,130.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1785` | 12,150.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 13,180.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1805` | 15,590.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1815` | 27,810.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1825` | 1,670.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1835` | 179.10 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1845` | 21,640.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 5,840.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1885` | 1,660.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1895` | 1,050.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1905` | 57,210.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1925` | 9,660.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1935` | 8,240.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1945` | 7,780.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1955` | 13,540.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1985` | 1,100.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 3,430.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2015` | 111,000.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 18,380.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2055` | 41,460.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2065` | 1,060.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2085` | 2,970.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2095` | 4,050.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2115` | 55,550.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2125` | 521.03 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2145` | 69,200.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2165` | 1,020.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 9,060.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2185` | 21,980.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 153.87 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 131,660.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2215` | 974.95 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 4,540.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2255` | 676.50 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2265` | 133.11 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2275` | 420.56 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2285` | 19,980.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 273.27 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 78,230.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 22,940.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 33,690.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 89,850.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 2,990.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 7,070.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 24,590.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 92,060.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2395` | 2,650.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 13,650.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2415` | 53,530.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 108,860.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 312,000.00 USD | 936,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 123,540.00 USD | 624,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 12,150.00 USD | 500,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 5,140.00 USD | 488,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 10,700.00 USD | 483,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 31,460.00 USD | 472,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2495` | 35,610.00 USD | 441,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 113.35 USD | 405,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2515` | 503.00 USD | 405,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2535` | 14,320.00 USD | 405,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2545` | 44,410.00 USD | 390,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 51,100.00 USD | 346,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 171.29 USD | 295,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2575` | 65,330.00 USD | 295,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 83,870.00 USD | 229,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 36,780.00 USD | 145,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 91,980.00 USD | 109,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 4,460.00 USD | 17,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 4,740.00 USD | 12,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 245.27 USD | 7,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 6,310.00 USD | 7,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 1,340.00 USD | 1,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2865` | 410.53 USD | 410.53 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3045` | 838.11 USD | 1,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3215` | 5,380.00 USD | 6,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3405` | 298.07 USD | 6,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3485` | 413.95 USD | 7,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3545` | 446.07 USD | 7,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3575` | 100.14 USD | 7,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 2,100.00 USD | 9,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3675` | 2,100.00 USD | 12,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3855` | 119.04 USD | 12,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3885` | 103.81 USD | 12,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4025` | 238.76 USD | 12,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4035` | 165.84 USD | 12,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4205` | 1,700.00 USD | 14,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4445` | 666.75 USD | 15,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4545` | 1,010.00 USD | 16,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4595` | 1,470.00 USD | 17,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4655` | 339,350.00 USD | 356,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4755` | 24,000.00 USD | 380,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5155` | 428.28 USD | 381,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5225` | 62,700.00 USD | 444,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5315` | 14,510.00 USD | 458,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0555` | 2,340,000.00 USD | 0.00 USD | 124.70 USD | `-79.44%` | `2,246.90` |
| `Live` | `Long` | `0.0585` | 2,330,000.00 USD | 0.00 USD | 2,580.00 USD | `-78.33%` | `44,136.50` |
| `Live` | `Long` | `0.0635` | 2,330,000.00 USD | 0.00 USD | 319.15 USD | `-76.48%` | `5,026.00` |
| `Live` | `Long` | `0.0665` | 2,330,000.00 USD | 0.00 USD | 1,250.00 USD | `-75.37%` | `18,735.40` |
| `Live` | `Long` | `0.0705` | 2,330,000.00 USD | 0.00 USD | 3,580.00 USD | `-73.89%` | `50,846.60` |
| `Live` | `Long` | `0.0755` | 2,330,000.00 USD | 0.00 USD | 119.43 USD | `-72.03%` | `1,581.90` |
| `Live` | `Long` | `0.0785` | 2,330,000.00 USD | 0.00 USD | 2,330.00 USD | `-70.92%` | `29,622.60` |
| `Live` | `Long` | `0.0805` | 2,320,000.00 USD | 0.00 USD | 8,590.00 USD | `-70.18%` | `106,697.00` |
| `Live` | `Long` | `0.0865` | 2,320,000.00 USD | 0.00 USD | 485.44 USD | `-67.96%` | `5,612.00` |
| `Live` | `Long` | `0.0925` | 2,320,000.00 USD | 0.00 USD | 695.06 USD | `-65.74%` | `7,514.20` |
| `Live` | `Long` | `0.0995` | 2,310,000.00 USD | 0.00 USD | 971.67 USD | `-63.14%` | `9,765.50` |
| `Live` | `Long` | `0.1035` | 2,310,000.00 USD | 0.00 USD | 1,220.00 USD | `-61.66%` | `11,739.70` |
| `Live` | `Long` | `0.1195` | 2,310,000.00 USD | 0.00 USD | 5,620.00 USD | `-55.74%` | `47,058.80` |
| `Live` | `Long` | `0.1225` | 2,310,000.00 USD | 0.00 USD | 116.35 USD | `-54.62%` | `949.80` |
| `Live` | `Long` | `0.1255` | 2,310,000.00 USD | 0.00 USD | 4,630.00 USD | `-53.51%` | `36,892.00` |
| `Live` | `Long` | `0.1285` | 2,300,000.00 USD | 0.00 USD | 613.05 USD | `-52.40%` | `4,770.80` |
| `Live` | `Long` | `0.1315` | 2,300,000.00 USD | 0.00 USD | 21,040.00 USD | `-51.29%` | `160,000.00` |
| `Live` | `Long` | `0.1405` | 2,280,000.00 USD | 0.00 USD | 14,050.00 USD | `-47.96%` | `100,000.00` |
| `Live` | `Long` | `0.1425` | 2,270,000.00 USD | 0.00 USD | 1,140.00 USD | `-47.22%` | `8,000.00` |
| `Live` | `Long` | `0.1435` | 2,270,000.00 USD | 0.00 USD | 941.69 USD | `-46.85%` | `6,562.30` |
| `Live` | `Long` | `0.1465` | 2,260,000.00 USD | 0.00 USD | 12,380.00 USD | `-45.73%` | `84,498.00` |
| `Live` | `Long` | `0.1475` | 2,250,000.00 USD | 0.00 USD | 1,190.00 USD | `-45.36%` | `8,042.60` |
| `Live` | `Long` | `0.1535` | 2,250,000.00 USD | 0.00 USD | 20,300.00 USD | `-43.14%` | `132,229.20` |
| `Live` | `Long` | `0.1565` | 2,230,000.00 USD | 0.00 USD | 3,910.00 USD | `-42.03%` | `25,000.00` |
| `Live` | `Long` | `0.1645` | 2,230,000.00 USD | 0.00 USD | 2,500.00 USD | `-39.07%` | `15,205.80` |
| `Live` | `Long` | `0.1665` | 2,220,000.00 USD | 0.00 USD | 7,600.00 USD | `-38.33%` | `45,616.80` |
| `Live` | `Long` | `0.1695` | 2,220,000.00 USD | 0.00 USD | 278.30 USD | `-37.22%` | `1,641.90` |
| `Live` | `Long` | `0.1715` | 2,220,000.00 USD | 0.00 USD | 464.68 USD | `-36.47%` | `2,709.50` |
| `Live` | `Long` | `0.1725` | 2,220,000.00 USD | 0.00 USD | 35,390.00 USD | `-36.10%` | `205,143.90` |
| `Live` | `Long` | `0.1735` | 2,180,000.00 USD | 0.00 USD | 2,020.00 USD | `-35.73%` | `11,641.60` |
| `Live` | `Long` | `0.1765` | 2,180,000.00 USD | 0.00 USD | 1,340.00 USD | `-34.62%` | `7,607.60` |
| `Live` | `Long` | `0.1775` | 2,180,000.00 USD | 0.00 USD | 14,130.00 USD | `-34.25%` | `79,610.90` |
| `Live` | `Long` | `0.1785` | 2,160,000.00 USD | 0.00 USD | 12,150.00 USD | `-33.88%` | `68,050.80` |
| `Live` | `Long` | `0.1795` | 2,150,000.00 USD | 0.00 USD | 13,180.00 USD | `-33.51%` | `73,444.60` |
| `Live` | `Long` | `0.1805` | 2,140,000.00 USD | 0.00 USD | 15,590.00 USD | `-33.14%` | `86,371.80` |
| `Live` | `Long` | `0.1815` | 2,120,000.00 USD | 0.00 USD | 27,810.00 USD | `-32.77%` | `153,246.60` |
| `Live` | `Long` | `0.1825` | 2,090,000.00 USD | 0.00 USD | 1,670.00 USD | `-32.40%` | `9,160.60` |
| `Live` | `Long` | `0.1835` | 2,090,000.00 USD | 0.00 USD | 179.10 USD | `-32.03%` | `976.00` |
| `Live` | `Long` | `0.1845` | 2,090,000.00 USD | 0.00 USD | 21,640.00 USD | `-31.66%` | `117,269.40` |
| `Live` | `Long` | `0.1875` | 2,070,000.00 USD | 0.00 USD | 5,840.00 USD | `-30.55%` | `31,135.10` |
| `Live` | `Long` | `0.1885` | 2,070,000.00 USD | 0.00 USD | 1,660.00 USD | `-30.18%` | `8,802.20` |
| `Live` | `Long` | `0.1895` | 2,060,000.00 USD | 0.00 USD | 1,050.00 USD | `-29.81%` | `5,539.20` |
| `Live` | `Long` | `0.1905` | 2,060,000.00 USD | 0.00 USD | 57,210.00 USD | `-29.44%` | `300,299.70` |
| `Live` | `Long` | `0.1925` | 2,010,000.00 USD | 0.00 USD | 9,660.00 USD | `-28.70%` | `50,169.20` |
| `Live` | `Long` | `0.1935` | 2,000,000.00 USD | 0.00 USD | 8,240.00 USD | `-28.33%` | `42,592.40` |
| `Live` | `Long` | `0.1945` | 1,990,000.00 USD | 0.00 USD | 7,780.00 USD | `-27.95%` | `40,000.00` |
| `Live` | `Long` | `0.1955` | 1,980,000.00 USD | 0.00 USD | 13,540.00 USD | `-27.58%` | `69,252.60` |
| `Live` | `Long` | `0.1985` | 1,970,000.00 USD | 0.00 USD | 1,100.00 USD | `-26.47%` | `5,563.00` |
| `Live` | `Long` | `0.1995` | 1,960,000.00 USD | 0.00 USD | 3,430.00 USD | `-26.10%` | `17,199.40` |
| `Live` | `Long` | `0.2015` | 1,960,000.00 USD | 0.00 USD | 111,000.00 USD | `-25.36%` | `550,886.10` |
| `Live` | `Long` | `0.2045` | 1,850,000.00 USD | 0.00 USD | 18,380.00 USD | `-24.25%` | `89,877.80` |
| `Live` | `Long` | `0.2055` | 1,830,000.00 USD | 0.00 USD | 41,460.00 USD | `-23.88%` | `201,752.40` |
| `Live` | `Long` | `0.2065` | 1,790,000.00 USD | 0.00 USD | 1,060.00 USD | `-23.51%` | `5,147.80` |
| `Live` | `Long` | `0.2085` | 1,790,000.00 USD | 0.00 USD | 2,970.00 USD | `-22.77%` | `14,230.20` |
| `Live` | `Long` | `0.2095` | 1,790,000.00 USD | 0.00 USD | 4,050.00 USD | `-22.40%` | `19,328.60` |
| `Live` | `Long` | `0.2115` | 1,780,000.00 USD | 0.00 USD | 55,550.00 USD | `-21.66%` | `262,635.40` |
| `Live` | `Long` | `0.2125` | 1,730,000.00 USD | 0.00 USD | 521.03 USD | `-21.29%` | `2,451.90` |
| `Live` | `Long` | `0.2145` | 1,730,000.00 USD | 0.00 USD | 69,200.00 USD | `-20.55%` | `322,593.50` |
| `Live` | `Long` | `0.2165` | 1,660,000.00 USD | 0.00 USD | 1,020.00 USD | `-19.81%` | `4,695.30` |
| `Live` | `Long` | `0.2175` | 1,660,000.00 USD | 0.00 USD | 9,060.00 USD | `-19.44%` | `41,666.50` |
| `Live` | `Long` | `0.2185` | 1,650,000.00 USD | 0.00 USD | 21,980.00 USD | `-19.07%` | `100,599.50` |
| `Live` | `Long` | `0.2195` | 1,630,000.00 USD | 0.00 USD | 153.87 USD | `-18.69%` | `701.00` |
| `Live` | `Long` | `0.2205` | 1,630,000.00 USD | 0.00 USD | 131,660.00 USD | `-18.32%` | `597,094.70` |
| `Live` | `Long` | `0.2215` | 1,490,000.00 USD | 0.00 USD | 974.95 USD | `-17.95%` | `4,401.60` |
| `Live` | `Long` | `0.2225` | 1,490,000.00 USD | 0.00 USD | 4,540.00 USD | `-17.58%` | `20,384.10` |
| `Live` | `Long` | `0.2255` | 1,490,000.00 USD | 0.00 USD | 676.50 USD | `-16.47%` | `3,000.00` |
| `Live` | `Long` | `0.2265` | 1,490,000.00 USD | 0.00 USD | 133.11 USD | `-16.10%` | `587.70` |
| `Live` | `Long` | `0.2275` | 1,490,000.00 USD | 0.00 USD | 420.56 USD | `-15.73%` | `1,848.60` |
| `Live` | `Long` | `0.2285` | 1,490,000.00 USD | 0.00 USD | 19,980.00 USD | `-15.36%` | `87,429.70` |
| `Live` | `Long` | `0.2295` | 1,470,000.00 USD | 0.00 USD | 273.27 USD | `-14.99%` | `1,190.70` |
| `Live` | `Long` | `0.2305` | 1,470,000.00 USD | 0.00 USD | 78,230.00 USD | `-14.62%` | `339,408.60` |
| `Live` | `Long` | `0.2315` | 1,390,000.00 USD | 0.00 USD | 22,940.00 USD | `-14.25%` | `99,106.30` |
| `Live` | `Long` | `0.2325` | 1,370,000.00 USD | 0.00 USD | 33,690.00 USD | `-13.88%` | `144,900.90` |
| `Live` | `Long` | `0.2335` | 1,330,000.00 USD | 0.00 USD | 89,850.00 USD | `-13.51%` | `384,806.60` |
| `Live` | `Long` | `0.2345` | 1,240,000.00 USD | 0.00 USD | 2,990.00 USD | `-13.14%` | `12,766.50` |
| `Live` | `Long` | `0.2355` | 1,240,000.00 USD | 0.00 USD | 7,070.00 USD | `-12.77%` | `30,000.00` |
| `Live` | `Long` | `0.2365` | 1,230,000.00 USD | 0.00 USD | 24,590.00 USD | `-12.40%` | `103,980.90` |
| `Live` | `Long` | `0.2385` | 1,210,000.00 USD | 0.00 USD | 92,060.00 USD | `-11.66%` | `385,976.30` |
| `Live` | `Long` | `0.2395` | 1,110,000.00 USD | 0.00 USD | 2,650.00 USD | `-11.29%` | `11,083.20` |
| `Live` | `Long` | `0.2405` | 1,110,000.00 USD | 0.00 USD | 13,650.00 USD | `-10.92%` | `56,745.50` |
| `Live` | `Long` | `0.2415` | 1,100,000.00 USD | 0.00 USD | 53,530.00 USD | `-10.55%` | `221,648.50` |
| `Live` | `Long` | `0.2425` | 1,050,000.00 USD | 0.00 USD | 108,860.00 USD | `-10.18%` | `448,910.10` |
| `Live` | `Long` | `0.2435` | 936,250.00 USD | 0.00 USD | 312,000.00 USD | `-9.80%` | `1,281,305.00` |
| `Live` | `Long` | `0.2445` | 624,260.00 USD | 0.00 USD | 123,540.00 USD | `-9.43%` | `505,283.30` |
| `Live` | `Long` | `0.2455` | 500,710.00 USD | 0.00 USD | 12,150.00 USD | `-9.06%` | `49,500.00` |
| `Live` | `Long` | `0.2465` | 488,560.00 USD | 0.00 USD | 5,140.00 USD | `-8.69%` | `20,841.30` |
| `Live` | `Long` | `0.2475` | 483,430.00 USD | 0.00 USD | 10,700.00 USD | `-8.32%` | `43,223.20` |
| `Live` | `Long` | `0.2485` | 472,730.00 USD | 0.00 USD | 31,460.00 USD | `-7.95%` | `126,587.90` |
| `Live` | `Long` | `0.2495` | 441,270.00 USD | 0.00 USD | 35,610.00 USD | `-7.58%` | `142,726.00` |
| `Live` | `Long` | `0.2505` | 405,660.00 USD | 0.00 USD | 113.35 USD | `-7.21%` | `452.50` |
| `Live` | `Long` | `0.2515` | 405,550.00 USD | 0.00 USD | 503.00 USD | `-6.84%` | `2,000.00` |
| `Live` | `Long` | `0.2535` | 405,040.00 USD | 0.00 USD | 14,320.00 USD | `-6.10%` | `56,501.50` |
| `Live` | `Long` | `0.2545` | 390,720.00 USD | 0.00 USD | 44,410.00 USD | `-5.73%` | `174,480.30` |
| `Live` | `Long` | `0.2555` | 346,320.00 USD | 0.00 USD | 51,100.00 USD | `-5.36%` | `199,996.80` |
| `Live` | `Long` | `0.2565` | 295,220.00 USD | 0.00 USD | 171.29 USD | `-4.99%` | `667.80` |
| `Live` | `Long` | `0.2575` | 295,050.00 USD | 0.00 USD | 65,330.00 USD | `-4.62%` | `253,702.40` |
| `Live` | `Long` | `0.2585` | 229,720.00 USD | 0.00 USD | 83,870.00 USD | `-4.25%` | `324,443.70` |
| `Live` | `Long` | `0.2595` | 145,850.00 USD | 0.00 USD | 36,780.00 USD | `-3.88%` | `141,734.90` |
| `Live` | `Long` | `0.2605` | 109,070.00 USD | 0.00 USD | 91,980.00 USD | `-3.51%` | `353,079.00` |
| `Live` | `Long` | `0.2615` | 17,090.00 USD | 0.00 USD | 4,460.00 USD | `-3.14%` | `17,053.00` |
| `Live` | `Long` | `0.2625` | 12,630.00 USD | 0.00 USD | 4,740.00 USD | `-2.77%` | `18,059.70` |
| `Live` | `Long` | `0.2635` | 7,890.00 USD | 0.00 USD | 245.27 USD | `-2.40%` | `930.80` |
| `Live` | `Long` | `0.2645` | 7,650.00 USD | 0.00 USD | 6,310.00 USD | `-2.03%` | `23,848.80` |
| `Live` | `Long` | `0.2675` | 1,340.00 USD | 0.00 USD | 1,340.00 USD | `-0.91%` | `5,000.00` |
| `Live` | `Short` | `0.2865` | 410.53 USD | 410.53 USD | 0.00 USD | `+6.12%` | `1,432.90` |
| `Live` | `Short` | `0.3045` | 1,250.00 USD | 838.11 USD | 0.00 USD | `+12.79%` | `2,752.40` |
| `Live` | `Short` | `0.3215` | 6,630.00 USD | 5,380.00 USD | 0.00 USD | `+19.09%` | `16,745.80` |
| `Live` | `Short` | `0.3405` | 6,930.00 USD | 298.07 USD | 0.00 USD | `+26.13%` | `875.40` |
| `Live` | `Short` | `0.3485` | 7,340.00 USD | 413.95 USD | 0.00 USD | `+29.09%` | `1,187.80` |
| `Live` | `Short` | `0.3545` | 7,790.00 USD | 446.07 USD | 0.00 USD | `+31.31%` | `1,258.30` |
| `Live` | `Short` | `0.3575` | 7,890.00 USD | 100.14 USD | 0.00 USD | `+32.42%` | `280.10` |
| `Live` | `Short` | `0.3625` | 9,990.00 USD | 2,100.00 USD | 0.00 USD | `+34.27%` | `5,784.00` |
| `Live` | `Short` | `0.3675` | 12,080.00 USD | 2,100.00 USD | 0.00 USD | `+36.13%` | `5,705.10` |
| `Live` | `Short` | `0.3855` | 12,200.00 USD | 119.04 USD | 0.00 USD | `+42.79%` | `308.80` |
| `Live` | `Short` | `0.3885` | 12,310.00 USD | 103.81 USD | 0.00 USD | `+43.90%` | `267.20` |
| `Live` | `Short` | `0.4025` | 12,550.00 USD | 238.76 USD | 0.00 USD | `+49.09%` | `593.20` |
| `Live` | `Short` | `0.4035` | 12,710.00 USD | 165.84 USD | 0.00 USD | `+49.46%` | `411.00` |
| `Live` | `Short` | `0.4205` | 14,410.00 USD | 1,700.00 USD | 0.00 USD | `+55.76%` | `4,032.60` |
| `Live` | `Short` | `0.4445` | 15,070.00 USD | 666.75 USD | 0.00 USD | `+64.65%` | `1,500.00` |
| `Live` | `Short` | `0.4545` | 16,090.00 USD | 1,010.00 USD | 0.00 USD | `+68.35%` | `2,227.00` |
| `Live` | `Short` | `0.4595` | 17,560.00 USD | 1,470.00 USD | 0.00 USD | `+70.20%` | `3,205.50` |
| `Live` | `Short` | `0.4655` | 356,910.00 USD | 339,350.00 USD | 0.00 USD | `+72.43%` | `729,000.00` |
| `Live` | `Short` | `0.4755` | 380,900.00 USD | 24,000.00 USD | 0.00 USD | `+76.13%` | `50,463.70` |
| `Live` | `Short` | `0.5155` | 381,330.00 USD | 428.28 USD | 0.00 USD | `+90.95%` | `830.80` |
| `Live` | `Short` | `0.5225` | 444,030.00 USD | 62,700.00 USD | 0.00 USD | `+93.54%` | `120,000.00` |
| `Live` | `Short` | `0.5315` | 458,540.00 USD | 14,510.00 USD | 0.00 USD | `+96.87%` | `27,300.00` |

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
  * Current Rate: `-1.57K` | Last 24h: `9.20K` | Last 3d: `30.42K` | Last 7d: `57.33K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0020%` | **USDT OKX** | `-0.0037%` |
| **USDT Bybit** | `-0.0092%` | **USDT KuCoin** | `-0.0240%` |
| **USDT MEXC** | `-0.0032%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0079%` | **USDT Bitget** | `0.0100%` |
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
| `5m` | 13,450.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `15m` | -52,910.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30m` | 3,300.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `1h` | -12,530.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `2h` | -49,040.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `4h` | -171,430.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `6h` | -407,170.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `8h` | -332,910.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `12h` | -757,040.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `24h` | -801,920.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1w` | -2,170,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30d` | -15,110,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+13.45K` | 15m=`-52.91K` | 1h=`-12.53K` | 24h=`-801.92K`
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
  * `2026-10-30 11:03:23 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:09:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:10:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `-0.9775` (Risk Distance: `1.23` pts)
  * +2.5R Take Profit: `3.34`
  * Mathematical Lot Sizing: **`8.10 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.2920` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.53` (Risk Distance: `1.23` pts)
  * +2.5R Take Profit: `-2.79`
  * Mathematical Lot Sizing: **`8.10 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.2767`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
