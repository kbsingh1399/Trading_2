# 🏛️ SOVEREIGN CANDIDATE DOSSIER: CRVUSD
**Canonical Key**: `CRVUSD` | **Broker Instrument**: `CRVUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 10:13:37 IST` (`2026-10-30 04:43:37 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.2610` | **Live Ask Quote**: `0.2840` | **Mid Price**: `0.2725`
- **Spread Points**: `23.00` | **Spread BPS**: `844.04 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.2740` | VWAP Z-Score: `-1.14` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0055` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `29.58` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3083` | Lower -3.00σ Band: `0.2398`
  * Upper +2.51σ Band: `0.3027` | Lower -2.51σ Band: `0.2454`
  * Upper +2.01σ Band: `0.2970` | Lower -2.01σ Band: `0.2511`
  * Upper +2.00σ Band: `0.2969` | Lower -2.00σ Band: `0.2512`
  * Upper +1.28σ Band: `0.2887` | Lower -1.28σ Band: `0.2594`
  * Upper +1.00σ Band: `0.2855` | Lower -1.00σ Band: `0.2626`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.2659` | EMA-20=`0.2744` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.2897` (Slope: `+0.0000`) | EMA-100=`0.3011`
  * Institutional Anchors: EMA-144=`0.3063` | EMA-200=`0.3105` (Slope: `-1.7800`) | EMA-233=`0.3127`
- **Range Boundaries**: 24H High=`0.3270` | 24H Low=`0.2530` | Weekly High=`0.3340` | Weekly Low=`0.2530`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.2940` (Distance: `-7.30%`)
  * Point of Control (POC) = `0.2640` (Distance: `+3.20%`)
  * Value Area Low (VAL) = `0.2590` (Distance: `+5.23%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3230` | POC=`0.3160` | VAL=`0.3100`
  * Prior Day Extremes: PDH=`0.3330` | PDL=`0.2890` | PDC=`0.2980`
  * Monday Range Blueprint: High=`0.3430` | Mid=`0.3340` | Low=`0.3250`
  * Developing Weekly Value Area: Weekly VAH=`0.3420` | Weekly POC=`0.3280` | Weekly VAL=`0.3160`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3040` | Low=`0.2530`
  * London Session (08:00-16:00 UTC): High=`0.2736` | Low=`0.2714`
  * New York Session (13:00-21:00 UTC): High=`0.2741` | Low=`0.2709`
  * Initial Balance (First Hour): IB High=`0.2733` | IB Low=`0.2717`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.2714` - `0.2736`
  * Optimal Trade Entry (OTE 0.705): `0.2730`
  * Structural Invalidation Anchor (0.786): `0.2747`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:01:04 IST` |

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
| `Live` | `Long Liquidation` | `0.0555` | 2,360.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 283.97 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 304.95 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 3,430.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 1,360.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 2,330.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 185.37 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 10,150.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 141.58 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 777.72 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 1,030.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 1,260.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 116.35 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 10,210.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 335.02 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 613.05 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 21,520.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 14,050.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 2,090.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 5,190.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 12,380.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1505` | 1,210.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 20,300.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 15,310.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 2,500.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 4,930.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 2,680.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 278.30 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 464.68 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 5,730.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 4,390.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 1,340.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 14,130.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1785` | 12,010.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 13,180.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1805` | 17,400.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1825` | 29,640.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1835` | 179.10 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1845` | 21,640.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 5,980.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1885` | 1,660.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1895` | 1,050.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1905` | 40,440.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1925` | 1,740.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1935` | 8,240.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1945` | 8,070.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1955` | 13,640.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1985` | 1,100.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 3,430.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2015` | 111,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 18,380.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2055` | 41,100.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2075` | 1,430.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2085` | 2,510.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2115` | 55,550.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2125` | 521.03 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2145` | 170,030.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2165` | 3,110.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 9,490.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 153.87 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 130,550.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2215` | 974.95 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 4,540.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 22,580.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2255` | 110.65 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2265` | 1,470.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2275` | 420.56 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2285` | 19,980.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 3,550.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 73,970.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 22,940.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 10,270.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 79,420.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 336.32 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 7,070.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 114,460.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 94,760.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2395` | 2,650.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 13,650.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2415` | 28,290.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 134,220.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 170,620.00 USD | 982,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 8,460.00 USD | 811,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 315,360.00 USD | 803,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 14,230.00 USD | 487,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 10,700.00 USD | 473,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 31,460.00 USD | 462,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2495` | 28,290.00 USD | 431,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 113.35 USD | 402,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2525` | 2,390.00 USD | 402,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2535` | 14,320.00 USD | 400,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2545` | 42,440.00 USD | 386,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 51,100.00 USD | 343,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 4,240.00 USD | 292,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2575` | 90,720.00 USD | 288,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 51,510.00 USD | 197,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 42,390.00 USD | 146,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 90,680.00 USD | 103,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 449.94 USD | 13,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 4,740.00 USD | 12,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 245.27 USD | 7,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 7,630.00 USD | 7,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2775` | 2,030.00 USD | 2,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2825` | 2,200.00 USD | 4,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2895` | 1,120.00 USD | 5,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2905` | 6,080.00 USD | 11,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2925` | 543.93 USD | 11,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3215` | 5,380.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3485` | 413.95 USD | 17,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3545` | 446.07 USD | 18,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3575` | 100.14 USD | 18,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 2,100.00 USD | 20,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3675` | 2,100.00 USD | 22,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3855` | 119.04 USD | 22,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3885` | 103.81 USD | 22,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4025` | 238.76 USD | 22,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4035` | 165.84 USD | 23,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4205` | 1,700.00 USD | 24,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4385` | 202.54 USD | 25,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4445` | 889.00 USD | 25,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4545` | 1,010.00 USD | 26,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4605` | 335,700.00 USD | 362,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4695` | 1,500.00 USD | 364,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4765` | 24,050.00 USD | 388,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5155` | 428.28 USD | 388,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5235` | 62,820.00 USD | 451,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5315` | 14,510.00 USD | 465,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5455` | 108.72 USD | 466,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0555` | 2,500,000.00 USD | 0.00 USD | 2,360.00 USD | `-79.92%` | `42,584.50` |
| `Live` | `Long` | `0.0565` | 2,500,000.00 USD | 0.00 USD | 283.97 USD | `-79.55%` | `5,026.00` |
| `Live` | `Long` | `0.0575` | 2,500,000.00 USD | 0.00 USD | 304.95 USD | `-79.19%` | `5,303.40` |
| `Live` | `Long` | `0.0675` | 2,500,000.00 USD | 0.00 USD | 3,430.00 USD | `-75.57%` | `50,846.60` |
| `Live` | `Long` | `0.0725` | 2,500,000.00 USD | 0.00 USD | 1,360.00 USD | `-73.76%` | `18,735.40` |
| `Live` | `Long` | `0.0785` | 2,500,000.00 USD | 0.00 USD | 2,330.00 USD | `-71.59%` | `29,622.60` |
| `Live` | `Long` | `0.0825` | 2,490,000.00 USD | 0.00 USD | 185.37 USD | `-70.14%` | `2,246.90` |
| `Live` | `Long` | `0.0865` | 2,490,000.00 USD | 0.00 USD | 10,150.00 USD | `-68.70%` | `117,328.60` |
| `Live` | `Long` | `0.0895` | 2,480,000.00 USD | 0.00 USD | 141.58 USD | `-67.61%` | `1,581.90` |
| `Live` | `Long` | `0.1035` | 2,480,000.00 USD | 0.00 USD | 777.72 USD | `-62.54%` | `7,514.20` |
| `Live` | `Long` | `0.1055` | 2,480,000.00 USD | 0.00 USD | 1,030.00 USD | `-61.82%` | `9,765.50` |
| `Live` | `Long` | `0.1075` | 2,480,000.00 USD | 0.00 USD | 1,260.00 USD | `-61.10%` | `11,739.70` |
| `Live` | `Long` | `0.1225` | 2,480,000.00 USD | 0.00 USD | 116.35 USD | `-55.67%` | `949.80` |
| `Live` | `Long` | `0.1255` | 2,480,000.00 USD | 0.00 USD | 10,210.00 USD | `-54.58%` | `81,323.20` |
| `Live` | `Long` | `0.1275` | 2,470,000.00 USD | 0.00 USD | 335.02 USD | `-53.86%` | `2,627.60` |
| `Live` | `Long` | `0.1285` | 2,470,000.00 USD | 0.00 USD | 613.05 USD | `-53.50%` | `4,770.80` |
| `Live` | `Long` | `0.1345` | 2,470,000.00 USD | 0.00 USD | 21,520.00 USD | `-51.33%` | `160,000.00` |
| `Live` | `Long` | `0.1405` | 2,450,000.00 USD | 0.00 USD | 14,050.00 USD | `-49.15%` | `100,000.00` |
| `Live` | `Long` | `0.1435` | 2,430,000.00 USD | 0.00 USD | 2,090.00 USD | `-48.07%` | `14,562.30` |
| `Live` | `Long` | `0.1455` | 2,430,000.00 USD | 0.00 USD | 5,190.00 USD | `-47.35%` | `35,697.50` |
| `Live` | `Long` | `0.1465` | 2,430,000.00 USD | 0.00 USD | 12,380.00 USD | `-46.98%` | `84,498.00` |
| `Live` | `Long` | `0.1505` | 2,410,000.00 USD | 0.00 USD | 1,210.00 USD | `-45.54%` | `8,042.60` |
| `Live` | `Long` | `0.1535` | 2,410,000.00 USD | 0.00 USD | 20,300.00 USD | `-44.45%` | `132,229.20` |
| `Live` | `Long` | `0.1595` | 2,390,000.00 USD | 0.00 USD | 15,310.00 USD | `-42.28%` | `96,000.00` |
| `Live` | `Long` | `0.1645` | 2,380,000.00 USD | 0.00 USD | 2,500.00 USD | `-40.47%` | `15,205.80` |
| `Live` | `Long` | `0.1665` | 2,370,000.00 USD | 0.00 USD | 4,930.00 USD | `-39.75%` | `29,616.80` |
| `Live` | `Long` | `0.1675` | 2,370,000.00 USD | 0.00 USD | 2,680.00 USD | `-39.38%` | `16,000.00` |
| `Live` | `Long` | `0.1695` | 2,370,000.00 USD | 0.00 USD | 278.30 USD | `-38.66%` | `1,641.90` |
| `Live` | `Long` | `0.1715` | 2,370,000.00 USD | 0.00 USD | 464.68 USD | `-37.94%` | `2,709.50` |
| `Live` | `Long` | `0.1725` | 2,370,000.00 USD | 0.00 USD | 5,730.00 USD | `-37.57%` | `33,202.70` |
| `Live` | `Long` | `0.1755` | 2,360,000.00 USD | 0.00 USD | 4,390.00 USD | `-36.49%` | `25,000.00` |
| `Live` | `Long` | `0.1765` | 2,360,000.00 USD | 0.00 USD | 1,340.00 USD | `-36.13%` | `7,607.60` |
| `Live` | `Long` | `0.1775` | 2,360,000.00 USD | 0.00 USD | 14,130.00 USD | `-35.77%` | `79,610.90` |
| `Live` | `Long` | `0.1785` | 2,340,000.00 USD | 0.00 USD | 12,010.00 USD | `-35.40%` | `67,270.30` |
| `Live` | `Long` | `0.1795` | 2,330,000.00 USD | 0.00 USD | 13,180.00 USD | `-35.04%` | `73,444.60` |
| `Live` | `Long` | `0.1805` | 2,320,000.00 USD | 0.00 USD | 17,400.00 USD | `-34.68%` | `96,371.80` |
| `Live` | `Long` | `0.1825` | 2,300,000.00 USD | 0.00 USD | 29,640.00 USD | `-33.96%` | `162,407.20` |
| `Live` | `Long` | `0.1835` | 2,270,000.00 USD | 0.00 USD | 179.10 USD | `-33.59%` | `976.00` |
| `Live` | `Long` | `0.1845` | 2,270,000.00 USD | 0.00 USD | 21,640.00 USD | `-33.23%` | `117,269.40` |
| `Live` | `Long` | `0.1875` | 2,250,000.00 USD | 0.00 USD | 5,980.00 USD | `-32.15%` | `31,915.60` |
| `Live` | `Long` | `0.1885` | 2,240,000.00 USD | 0.00 USD | 1,660.00 USD | `-31.78%` | `8,802.20` |
| `Live` | `Long` | `0.1895` | 2,240,000.00 USD | 0.00 USD | 1,050.00 USD | `-31.42%` | `5,539.20` |
| `Live` | `Long` | `0.1905` | 2,240,000.00 USD | 0.00 USD | 40,440.00 USD | `-31.06%` | `212,299.70` |
| `Live` | `Long` | `0.1925` | 2,200,000.00 USD | 0.00 USD | 1,740.00 USD | `-30.34%` | `9,044.50` |
| `Live` | `Long` | `0.1935` | 2,200,000.00 USD | 0.00 USD | 8,240.00 USD | `-29.98%` | `42,581.40` |
| `Live` | `Long` | `0.1945` | 2,190,000.00 USD | 0.00 USD | 8,070.00 USD | `-29.61%` | `41,482.00` |
| `Live` | `Long` | `0.1955` | 2,180,000.00 USD | 0.00 USD | 13,640.00 USD | `-29.25%` | `69,769.50` |
| `Live` | `Long` | `0.1985` | 2,170,000.00 USD | 0.00 USD | 1,100.00 USD | `-28.17%` | `5,563.00` |
| `Live` | `Long` | `0.1995` | 2,170,000.00 USD | 0.00 USD | 3,430.00 USD | `-27.80%` | `17,199.40` |
| `Live` | `Long` | `0.2015` | 2,160,000.00 USD | 0.00 USD | 111,000.00 USD | `-27.08%` | `550,886.10` |
| `Live` | `Long` | `0.2045` | 2,050,000.00 USD | 0.00 USD | 18,380.00 USD | `-25.99%` | `89,877.80` |
| `Live` | `Long` | `0.2055` | 2,030,000.00 USD | 0.00 USD | 41,100.00 USD | `-25.63%` | `200,000.00` |
| `Live` | `Long` | `0.2075` | 1,990,000.00 USD | 0.00 USD | 1,430.00 USD | `-24.91%` | `6,900.20` |
| `Live` | `Long` | `0.2085` | 1,990,000.00 USD | 0.00 USD | 2,510.00 USD | `-24.55%` | `12,025.50` |
| `Live` | `Long` | `0.2115` | 1,990,000.00 USD | 0.00 USD | 55,550.00 USD | `-23.46%` | `262,635.40` |
| `Live` | `Long` | `0.2125` | 1,930,000.00 USD | 0.00 USD | 521.03 USD | `-23.10%` | `2,451.90` |
| `Live` | `Long` | `0.2145` | 1,930,000.00 USD | 0.00 USD | 170,030.00 USD | `-22.38%` | `792,665.80` |
| `Live` | `Long` | `0.2165` | 1,760,000.00 USD | 0.00 USD | 3,110.00 USD | `-21.65%` | `14,386.50` |
| `Live` | `Long` | `0.2175` | 1,760,000.00 USD | 0.00 USD | 9,490.00 USD | `-21.29%` | `43,612.50` |
| `Live` | `Long` | `0.2195` | 1,750,000.00 USD | 0.00 USD | 153.87 USD | `-20.57%` | `701.00` |
| `Live` | `Long` | `0.2205` | 1,750,000.00 USD | 0.00 USD | 130,550.00 USD | `-20.20%` | `592,044.70` |
| `Live` | `Long` | `0.2215` | 1,620,000.00 USD | 0.00 USD | 974.95 USD | `-19.84%` | `4,401.60` |
| `Live` | `Long` | `0.2225` | 1,620,000.00 USD | 0.00 USD | 4,540.00 USD | `-19.48%` | `20,384.10` |
| `Live` | `Long` | `0.2245` | 1,610,000.00 USD | 0.00 USD | 22,580.00 USD | `-18.76%` | `100,599.50` |
| `Live` | `Long` | `0.2255` | 1,590,000.00 USD | 0.00 USD | 110.65 USD | `-18.39%` | `490.70` |
| `Live` | `Long` | `0.2265` | 1,590,000.00 USD | 0.00 USD | 1,470.00 USD | `-18.03%` | `6,491.70` |
| `Live` | `Long` | `0.2275` | 1,590,000.00 USD | 0.00 USD | 420.56 USD | `-17.67%` | `1,848.60` |
| `Live` | `Long` | `0.2285` | 1,590,000.00 USD | 0.00 USD | 19,980.00 USD | `-17.31%` | `87,429.70` |
| `Live` | `Long` | `0.2295` | 1,570,000.00 USD | 0.00 USD | 3,550.00 USD | `-16.95%` | `15,472.80` |
| `Live` | `Long` | `0.2305` | 1,560,000.00 USD | 0.00 USD | 73,970.00 USD | `-16.59%` | `320,924.60` |
| `Live` | `Long` | `0.2315` | 1,490,000.00 USD | 0.00 USD | 22,940.00 USD | `-16.22%` | `99,106.30` |
| `Live` | `Long` | `0.2325` | 1,470,000.00 USD | 0.00 USD | 10,270.00 USD | `-15.86%` | `44,170.10` |
| `Live` | `Long` | `0.2335` | 1,460,000.00 USD | 0.00 USD | 79,420.00 USD | `-15.50%` | `340,125.70` |
| `Live` | `Long` | `0.2345` | 1,380,000.00 USD | 0.00 USD | 336.32 USD | `-15.14%` | `1,434.20` |
| `Live` | `Long` | `0.2355` | 1,380,000.00 USD | 0.00 USD | 7,070.00 USD | `-14.78%` | `30,000.00` |
| `Live` | `Long` | `0.2365` | 1,370,000.00 USD | 0.00 USD | 114,460.00 USD | `-14.41%` | `483,980.90` |
| `Live` | `Long` | `0.2385` | 1,260,000.00 USD | 0.00 USD | 94,760.00 USD | `-13.69%` | `397,308.60` |
| `Live` | `Long` | `0.2395` | 1,160,000.00 USD | 0.00 USD | 2,650.00 USD | `-13.33%` | `11,083.20` |
| `Live` | `Long` | `0.2405` | 1,160,000.00 USD | 0.00 USD | 13,650.00 USD | `-12.97%` | `56,745.50` |
| `Live` | `Long` | `0.2415` | 1,140,000.00 USD | 0.00 USD | 28,290.00 USD | `-12.60%` | `117,135.40` |
| `Live` | `Long` | `0.2425` | 1,120,000.00 USD | 0.00 USD | 134,220.00 USD | `-12.24%` | `553,464.90` |
| `Live` | `Long` | `0.2435` | 982,100.00 USD | 0.00 USD | 170,620.00 USD | `-11.88%` | `700,685.10` |
| `Live` | `Long` | `0.2445` | 811,480.00 USD | 0.00 USD | 8,460.00 USD | `-11.52%` | `34,615.40` |
| `Live` | `Long` | `0.2455` | 803,020.00 USD | 0.00 USD | 315,360.00 USD | `-11.16%` | `1,284,577.50` |
| `Live` | `Long` | `0.2465` | 487,650.00 USD | 0.00 USD | 14,230.00 USD | `-10.80%` | `57,730.00` |
| `Live` | `Long` | `0.2475` | 473,420.00 USD | 0.00 USD | 10,700.00 USD | `-10.43%` | `43,223.20` |
| `Live` | `Long` | `0.2485` | 462,730.00 USD | 0.00 USD | 31,460.00 USD | `-10.07%` | `126,587.90` |
| `Live` | `Long` | `0.2495` | 431,270.00 USD | 0.00 USD | 28,290.00 USD | `-9.71%` | `113,393.90` |
| `Live` | `Long` | `0.2505` | 402,980.00 USD | 0.00 USD | 113.35 USD | `-9.35%` | `452.50` |
| `Live` | `Long` | `0.2525` | 402,860.00 USD | 0.00 USD | 2,390.00 USD | `-8.62%` | `9,453.60` |
| `Live` | `Long` | `0.2535` | 400,480.00 USD | 0.00 USD | 14,320.00 USD | `-8.26%` | `56,501.50` |
| `Live` | `Long` | `0.2545` | 386,150.00 USD | 0.00 USD | 42,440.00 USD | `-7.90%` | `166,752.50` |
| `Live` | `Long` | `0.2555` | 343,710.00 USD | 0.00 USD | 51,100.00 USD | `-7.54%` | `199,996.80` |
| `Live` | `Long` | `0.2565` | 292,620.00 USD | 0.00 USD | 4,240.00 USD | `-7.18%` | `16,535.80` |
| `Live` | `Long` | `0.2575` | 288,370.00 USD | 0.00 USD | 90,720.00 USD | `-6.81%` | `352,311.70` |
| `Live` | `Long` | `0.2585` | 197,650.00 USD | 0.00 USD | 51,510.00 USD | `-6.45%` | `199,280.50` |
| `Live` | `Long` | `0.2595` | 146,140.00 USD | 0.00 USD | 42,390.00 USD | `-6.09%` | `163,345.70` |
| `Live` | `Long` | `0.2605` | 103,750.00 USD | 0.00 USD | 90,680.00 USD | `-5.73%` | `348,118.10` |
| `Live` | `Long` | `0.2615` | 13,070.00 USD | 0.00 USD | 449.94 USD | `-5.37%` | `1,720.60` |
| `Live` | `Long` | `0.2625` | 12,620.00 USD | 0.00 USD | 4,740.00 USD | `-5.00%` | `18,059.70` |
| `Live` | `Long` | `0.2635` | 7,880.00 USD | 0.00 USD | 245.27 USD | `-4.64%` | `930.80` |
| `Live` | `Long` | `0.2645` | 7,630.00 USD | 0.00 USD | 7,630.00 USD | `-4.28%` | `28,848.80` |
| `Live` | `Short` | `0.2775` | 2,030.00 USD | 2,030.00 USD | 0.00 USD | `+0.42%` | `7,328.20` |
| `Live` | `Short` | `0.2825` | 4,230.00 USD | 2,200.00 USD | 0.00 USD | `+2.23%` | `7,781.20` |
| `Live` | `Short` | `0.2895` | 5,350.00 USD | 1,120.00 USD | 0.00 USD | `+4.77%` | `3,870.00` |
| `Live` | `Short` | `0.2905` | 11,430.00 USD | 6,080.00 USD | 0.00 USD | `+5.13%` | `20,913.40` |
| `Live` | `Short` | `0.2925` | 11,970.00 USD | 543.93 USD | 0.00 USD | `+5.85%` | `1,859.60` |
| `Live` | `Short` | `0.3215` | 17,360.00 USD | 5,380.00 USD | 0.00 USD | `+16.35%` | `16,745.80` |
| `Live` | `Short` | `0.3485` | 17,770.00 USD | 413.95 USD | 0.00 USD | `+26.12%` | `1,187.80` |
| `Live` | `Short` | `0.3545` | 18,220.00 USD | 446.07 USD | 0.00 USD | `+28.29%` | `1,258.30` |
| `Live` | `Short` | `0.3575` | 18,320.00 USD | 100.14 USD | 0.00 USD | `+29.37%` | `280.10` |
| `Live` | `Short` | `0.3625` | 20,410.00 USD | 2,100.00 USD | 0.00 USD | `+31.18%` | `5,784.00` |
| `Live` | `Short` | `0.3675` | 22,510.00 USD | 2,100.00 USD | 0.00 USD | `+32.99%` | `5,705.10` |
| `Live` | `Short` | `0.3855` | 22,630.00 USD | 119.04 USD | 0.00 USD | `+39.51%` | `308.80` |
| `Live` | `Short` | `0.3885` | 22,730.00 USD | 103.81 USD | 0.00 USD | `+40.59%` | `267.20` |
| `Live` | `Short` | `0.4025` | 22,970.00 USD | 238.76 USD | 0.00 USD | `+45.66%` | `593.20` |
| `Live` | `Short` | `0.4035` | 23,140.00 USD | 165.84 USD | 0.00 USD | `+46.02%` | `411.00` |
| `Live` | `Short` | `0.4205` | 24,830.00 USD | 1,700.00 USD | 0.00 USD | `+52.17%` | `4,032.60` |
| `Live` | `Short` | `0.4385` | 25,030.00 USD | 202.54 USD | 0.00 USD | `+58.69%` | `461.90` |
| `Live` | `Short` | `0.4445` | 25,920.00 USD | 889.00 USD | 0.00 USD | `+60.86%` | `2,000.00` |
| `Live` | `Short` | `0.4545` | 26,940.00 USD | 1,010.00 USD | 0.00 USD | `+64.48%` | `2,227.00` |
| `Live` | `Short` | `0.4605` | 362,640.00 USD | 335,700.00 USD | 0.00 USD | `+66.65%` | `729,000.00` |
| `Live` | `Short` | `0.4695` | 364,150.00 USD | 1,500.00 USD | 0.00 USD | `+69.91%` | `3,205.50` |
| `Live` | `Short` | `0.4765` | 388,190.00 USD | 24,050.00 USD | 0.00 USD | `+72.44%` | `50,463.70` |
| `Live` | `Short` | `0.5155` | 388,620.00 USD | 428.28 USD | 0.00 USD | `+86.55%` | `830.80` |
| `Live` | `Short` | `0.5235` | 451,440.00 USD | 62,820.00 USD | 0.00 USD | `+89.45%` | `120,000.00` |
| `Live` | `Short` | `0.5315` | 465,950.00 USD | 14,510.00 USD | 0.00 USD | `+92.34%` | `27,300.00` |
| `Live` | `Short` | `0.5455` | 466,060.00 USD | 108.72 USD | 0.00 USD | `+97.41%` | `199.30` |

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
  * Current Rate: `-1.18K` | Last 24h: `9.20K` | Last 3d: `30.42K` | Last 7d: `57.33K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0027%` | **USDT OKX** | `0.0096%` |
| **USDT Bybit** | `-0.0123%` | **USDT KuCoin** | `-0.0032%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
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
| `5m` | -18,840.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `15m` | -64,980.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30m` | -87,410.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1h` | -48,700.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `2h` | 45,470.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `4h` | 27,150.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `6h` | -288,740.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `8h` | -426,530.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `12h` | -863,890.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `24h` | -675,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1w` | -2,160,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30d` | -15,240,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-18.84K` | 15m=`-64.98K` | 1h=`-48.70K` | 24h=`-675.00K`
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
  * `2026-10-30 09:50:55 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:09:55 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:09:55 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:09:55 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:08:55 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:08:55 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:55 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:10:55 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.2590` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.2179` (Risk Distance: `0.0460` pts)
  * +2.5R Take Profit: `0.3740`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.2940` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3351` (Risk Distance: `0.0460` pts)
  * +2.5R Take Profit: `0.1790`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.2747`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
