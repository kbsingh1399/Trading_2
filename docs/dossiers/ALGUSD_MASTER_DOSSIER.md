# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ALGUSD
**Canonical Key**: `ALGUSD` | **Broker Instrument**: `ALGUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 03:13:10 IST` (`2026-10-29 21:43:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0942` | **Live Ask Quote**: `0.0965` | **Mid Price**: `0.0954`
- **Spread Points**: `23.00` | **Spread BPS**: `241.22 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0981` | VWAP Z-Score: `-1.60` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0012` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `30.71` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1057` | Lower -3.00σ Band: `0.0906`
  * Upper +2.51σ Band: `0.1044` | Lower -2.51σ Band: `0.0918`
  * Upper +2.01σ Band: `0.1032` | Lower -2.01σ Band: `0.0931`
  * Upper +2.00σ Band: `0.1032` | Lower -2.00σ Band: `0.0931`
  * Upper +1.28σ Band: `0.1014` | Lower -1.28σ Band: `0.0949`
  * Upper +1.00σ Band: `0.1006` | Lower -1.00σ Band: `0.0956`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0954` | EMA-20=`0.0970` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0983` (Slope: `+0.0000`) | EMA-100=`0.0992`
  * Institutional Anchors: EMA-144=`0.0997` | EMA-200=`0.1003` (Slope: `-0.4974`) | EMA-233=`0.1006`
- **Range Boundaries**: 24H High=`0.1034` | 24H Low=`0.0911` | Weekly High=`0.1051` | Weekly Low=`0.0911`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0945` (Distance: `+0.93%`)
  * Point of Control (POC) = `0.0941` (Distance: `+1.33%`)
  * Value Area Low (VAL) = `0.0937` (Distance: `+1.76%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.1013` | POC=`0.0982` | VAL=`0.0969`
  * Prior Day Extremes: PDH=`0.1037` | PDL=`0.0911` | PDC=`0.0922`
  * Monday Range Blueprint: High=`0.1046` | Mid=`0.1031` | Low=`0.1015`
  * Developing Weekly Value Area: Weekly VAH=`0.1042` | Weekly POC=`0.1025` | Weekly VAL=`0.1004`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0950` | Low=`0.0936`
  * London Session (08:00-16:00 UTC): High=`0.0957` | Low=`0.0950`
  * New York Session (13:00-21:00 UTC): High=`0.0959` | Low=`0.0948`
  * Initial Balance (First Hour): IB High=`0.0956` | IB Low=`0.0951`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0950` - `0.0957`
  * Optimal Trade Entry (OTE 0.705): `0.0955`
  * Structural Invalidation Anchor (0.786): `0.0961`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:04:58 IST` |

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
  * 24H Horizon: Short MP=`0.1068` (Vol: 34,981.57 USD, Dist: `+3.28%`) | Long MP=`0.1015` (Vol: 29,089.31 USD, Dist: `--1.77%`)
  * 48H Horizon: Short MP=`0.1067` (Vol: 34,068.88 USD, Dist: `+3.26%`) | Long MP=`0.1016` (Vol: 32,527.85 USD, Dist: `--1.74%`)
  * 3D Horizon: Short MP=`0.1065` (Vol: 32,466.82 USD, Dist: `+3.02%`) | Long MP=`0.1009` (Vol: 37,584.26 USD, Dist: `--2.44%`)
  * 7D Horizon: Short MP=`0.1067` (Vol: 62,663.70 USD, Dist: `+3.72%`) | Long MP=`0.1008` (Vol: 53,528.78 USD, Dist: `--2.01%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0193` | 221.15 USD | 223,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0209` | 3,710.00 USD | 223,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0228` | 777.59 USD | 219,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0360` | 113.27 USD | 218,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0396` | 1,660.00 USD | 218,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0401` | 112.62 USD | 217,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0420` | 344.73 USD | 216,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0421` | 3,680.00 USD | 216,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 193.70 USD | 212,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0457` | 26,180.00 USD | 212,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0462` | 16,430.00 USD | 186,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0483` | 2,390.00 USD | 170,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0493` | 142.77 USD | 167,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0496` | 267.76 USD | 167,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 506.59 USD | 167,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 6,430.00 USD | 166,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0548` | 13,710.00 USD | 160,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0549` | 442.47 USD | 146,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0553` | 5,840.00 USD | 146,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0588` | 111.76 USD | 140,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 441.33 USD | 140,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 106.14 USD | 139,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 223.62 USD | 139,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 260.91 USD | 139,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 180.46 USD | 139,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0628` | 613.07 USD | 139,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 167.24 USD | 138,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 1,570.00 USD | 138,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 525.94 USD | 136,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 309.00 USD | 136,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0654` | 13,390.00 USD | 135,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 3,960.00 USD | 122,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0674` | 208.83 USD | 118,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0683` | 5,040.00 USD | 118,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0693` | 919.79 USD | 113,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0694` | 155.50 USD | 112,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0717` | 224.98 USD | 112,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0720` | 7,110.00 USD | 112,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0721` | 347.79 USD | 104,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0727` | 918.15 USD | 104,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0728` | 388.00 USD | 103,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0730` | 933.91 USD | 103,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0732` | 1,020.00 USD | 102,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 1,120.00 USD | 101,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0736` | 444.48 USD | 100,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0741` | 741.50 USD | 99,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0742` | 174.34 USD | 98,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0751` | 475.62 USD | 98,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0752` | 299.65 USD | 98,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0754` | 557.29 USD | 98,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 1,250.00 USD | 97,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0756` | 4,630.00 USD | 96,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0759` | 3,050.00 USD | 91,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0761` | 189.82 USD | 88,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0762` | 954.42 USD | 88,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0764` | 1,620.00 USD | 87,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0766` | 180.43 USD | 85,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0770` | 5,050.00 USD | 85,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 930.06 USD | 80,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0780` | 438.48 USD | 79,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0793` | 309.08 USD | 79,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0796` | 7,960.00 USD | 78,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0800` | 139.21 USD | 70,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0801` | 6,210.00 USD | 70,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0808` | 394.06 USD | 64,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0809` | 487.61 USD | 64,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0814` | 2,040.00 USD | 63,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0819` | 181.85 USD | 61,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0828` | 1,660.00 USD | 61,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0830` | 1,110.00 USD | 59,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0833` | 3,420.00 USD | 58,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 7,980.00 USD | 55,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0843` | 25,250.00 USD | 47,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0844` | 808.44 USD | 22,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0859` | 2,150.00 USD | 21,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0862` | 1,450.00 USD | 19,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0871` | 994.37 USD | 17,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0872` | 133.43 USD | 16,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0872` | 223.88 USD | 16,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0880` | 4,640.00 USD | 16,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0882` | 1,080.00 USD | 11,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0886` | 142.57 USD | 10,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0887` | 442.72 USD | 10,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0893` | 695.50 USD | 9,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0901` | 2,310.00 USD | 9,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0912` | 909.76 USD | 6,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0917` | 5,420.00 USD | 6,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0922` | 659.13 USD | 659.13 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1027` | 4,130.00 USD | 4,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1109` | 217.13 USD | 4,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1268` | 2,190.00 USD | 6,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1384` | 2,480.00 USD | 9,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1474` | 126.43 USD | 9,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1477` | 162.97 USD | 9,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0193` | 223,570.00 USD | 0.00 USD | 221.15 USD | `-79.25%` | `11,429.00` |
| `Live` | `Long` | `0.0209` | 223,340.00 USD | 0.00 USD | 3,710.00 USD | `-77.64%` | `177,866.00` |
| `Live` | `Long` | `0.0228` | 219,640.00 USD | 0.00 USD | 777.59 USD | `-75.49%` | `34,030.00` |
| `Live` | `Long` | `0.0360` | 218,860.00 USD | 0.00 USD | 113.27 USD | `-61.34%` | `3,142.00` |
| `Live` | `Long` | `0.0396` | 218,750.00 USD | 0.00 USD | 1,660.00 USD | `-57.48%` | `41,853.00` |
| `Live` | `Long` | `0.0401` | 217,090.00 USD | 0.00 USD | 112.62 USD | `-56.94%` | `2,805.00` |
| `Live` | `Long` | `0.0420` | 216,970.00 USD | 0.00 USD | 344.73 USD | `-54.90%` | `8,198.00` |
| `Live` | `Long` | `0.0421` | 216,630.00 USD | 0.00 USD | 3,680.00 USD | `-54.80%` | `87,382.00` |
| `Live` | `Long` | `0.0425` | 212,950.00 USD | 0.00 USD | 193.70 USD | `-54.48%` | `4,563.00` |
| `Live` | `Long` | `0.0457` | 212,750.00 USD | 0.00 USD | 26,180.00 USD | `-51.04%` | `573,450.00` |
| `Live` | `Long` | `0.0462` | 186,570.00 USD | 0.00 USD | 16,430.00 USD | `-50.40%` | `355,228.00` |
| `Live` | `Long` | `0.0483` | 170,140.00 USD | 0.00 USD | 2,390.00 USD | `-48.15%` | `49,368.00` |
| `Live` | `Long` | `0.0493` | 167,760.00 USD | 0.00 USD | 142.77 USD | `-47.08%` | `2,893.00` |
| `Live` | `Long` | `0.0496` | 167,610.00 USD | 0.00 USD | 267.76 USD | `-46.75%` | `5,393.00` |
| `Live` | `Long` | `0.0508` | 167,350.00 USD | 0.00 USD | 506.59 USD | `-45.57%` | `9,982.00` |
| `Live` | `Long` | `0.0520` | 166,840.00 USD | 0.00 USD | 6,430.00 USD | `-44.29%` | `123,747.00` |
| `Live` | `Long` | `0.0548` | 160,410.00 USD | 0.00 USD | 13,710.00 USD | `-41.28%` | `250,396.00` |
| `Live` | `Long` | `0.0549` | 146,700.00 USD | 0.00 USD | 442.47 USD | `-41.18%` | `8,067.00` |
| `Live` | `Long` | `0.0553` | 146,260.00 USD | 0.00 USD | 5,840.00 USD | `-40.75%` | `105,702.00` |
| `Live` | `Long` | `0.0588` | 140,420.00 USD | 0.00 USD | 111.76 USD | `-36.89%` | `1,899.00` |
| `Live` | `Long` | `0.0599` | 140,310.00 USD | 0.00 USD | 441.33 USD | `-35.81%` | `7,374.00` |
| `Live` | `Long` | `0.0607` | 139,870.00 USD | 0.00 USD | 106.14 USD | `-34.96%` | `1,750.00` |
| `Live` | `Long` | `0.0609` | 139,760.00 USD | 0.00 USD | 223.62 USD | `-34.74%` | `3,675.00` |
| `Live` | `Long` | `0.0621` | 139,540.00 USD | 0.00 USD | 260.91 USD | `-33.35%` | `4,198.00` |
| `Live` | `Long` | `0.0625` | 139,280.00 USD | 0.00 USD | 180.46 USD | `-32.92%` | `2,885.00` |
| `Live` | `Long` | `0.0628` | 139,100.00 USD | 0.00 USD | 613.07 USD | `-32.70%` | `9,770.00` |
| `Live` | `Long` | `0.0634` | 138,480.00 USD | 0.00 USD | 167.24 USD | `-32.06%` | `2,640.00` |
| `Live` | `Long` | `0.0635` | 138,320.00 USD | 0.00 USD | 1,570.00 USD | `-31.95%` | `24,765.00` |
| `Live` | `Long` | `0.0636` | 136,740.00 USD | 0.00 USD | 525.94 USD | `-31.74%` | `8,263.00` |
| `Live` | `Long` | `0.0645` | 136,220.00 USD | 0.00 USD | 309.00 USD | `-30.77%` | `4,787.00` |
| `Live` | `Long` | `0.0654` | 135,910.00 USD | 0.00 USD | 13,390.00 USD | `-29.92%` | `204,927.00` |
| `Live` | `Long` | `0.0659` | 122,520.00 USD | 0.00 USD | 3,960.00 USD | `-29.27%` | `60,000.00` |
| `Live` | `Long` | `0.0674` | 118,560.00 USD | 0.00 USD | 208.83 USD | `-27.66%` | `3,096.00` |
| `Live` | `Long` | `0.0683` | 118,350.00 USD | 0.00 USD | 5,040.00 USD | `-26.81%` | `73,856.00` |
| `Live` | `Long` | `0.0693` | 113,310.00 USD | 0.00 USD | 919.79 USD | `-25.63%` | `13,263.00` |
| `Live` | `Long` | `0.0694` | 112,390.00 USD | 0.00 USD | 155.50 USD | `-25.52%` | `2,239.00` |
| `Live` | `Long` | `0.0717` | 112,240.00 USD | 0.00 USD | 224.98 USD | `-23.16%` | `3,140.00` |
| `Live` | `Long` | `0.0720` | 112,010.00 USD | 0.00 USD | 7,110.00 USD | `-22.84%` | `98,791.00` |
| `Live` | `Long` | `0.0721` | 104,900.00 USD | 0.00 USD | 347.79 USD | `-22.73%` | `4,827.00` |
| `Live` | `Long` | `0.0727` | 104,550.00 USD | 0.00 USD | 918.15 USD | `-22.09%` | `12,638.00` |
| `Live` | `Long` | `0.0728` | 103,640.00 USD | 0.00 USD | 388.00 USD | `-21.87%` | `5,326.00` |
| `Live` | `Long` | `0.0730` | 103,250.00 USD | 0.00 USD | 933.91 USD | `-21.77%` | `12,802.00` |
| `Live` | `Long` | `0.0732` | 102,310.00 USD | 0.00 USD | 1,020.00 USD | `-21.44%` | `13,863.00` |
| `Live` | `Long` | `0.0735` | 101,300.00 USD | 0.00 USD | 1,120.00 USD | `-21.23%` | `15,256.00` |
| `Live` | `Long` | `0.0736` | 100,180.00 USD | 0.00 USD | 444.48 USD | `-21.02%` | `6,035.00` |
| `Live` | `Long` | `0.0741` | 99,730.00 USD | 0.00 USD | 741.50 USD | `-20.48%` | `10,000.00` |
| `Live` | `Long` | `0.0742` | 98,990.00 USD | 0.00 USD | 174.34 USD | `-20.37%` | `2,348.00` |
| `Live` | `Long` | `0.0751` | 98,820.00 USD | 0.00 USD | 475.62 USD | `-19.41%` | `6,329.00` |
| `Live` | `Long` | `0.0752` | 98,340.00 USD | 0.00 USD | 299.65 USD | `-19.30%` | `3,982.00` |
| `Live` | `Long` | `0.0754` | 98,040.00 USD | 0.00 USD | 557.29 USD | `-19.19%` | `7,396.00` |
| `Live` | `Long` | `0.0755` | 97,490.00 USD | 0.00 USD | 1,250.00 USD | `-19.09%` | `16,502.00` |
| `Live` | `Long` | `0.0756` | 96,240.00 USD | 0.00 USD | 4,630.00 USD | `-18.87%` | `61,227.00` |
| `Live` | `Long` | `0.0759` | 91,610.00 USD | 0.00 USD | 3,050.00 USD | `-18.66%` | `40,199.00` |
| `Live` | `Long` | `0.0761` | 88,560.00 USD | 0.00 USD | 189.82 USD | `-18.44%` | `2,496.00` |
| `Live` | `Long` | `0.0762` | 88,370.00 USD | 0.00 USD | 954.42 USD | `-18.23%` | `12,517.00` |
| `Live` | `Long` | `0.0764` | 87,420.00 USD | 0.00 USD | 1,620.00 USD | `-18.12%` | `21,173.00` |
| `Live` | `Long` | `0.0766` | 85,800.00 USD | 0.00 USD | 180.43 USD | `-17.80%` | `2,354.00` |
| `Live` | `Long` | `0.0770` | 85,620.00 USD | 0.00 USD | 5,050.00 USD | `-17.48%` | `65,640.00` |
| `Live` | `Long` | `0.0775` | 80,570.00 USD | 0.00 USD | 930.06 USD | `-16.83%` | `11,993.00` |
| `Live` | `Long` | `0.0780` | 79,640.00 USD | 0.00 USD | 438.48 USD | `-16.30%` | `5,618.00` |
| `Live` | `Long` | `0.0793` | 79,200.00 USD | 0.00 USD | 309.08 USD | `-15.01%` | `3,900.00` |
| `Live` | `Long` | `0.0796` | 78,890.00 USD | 0.00 USD | 7,960.00 USD | `-14.58%` | `100,000.00` |
| `Live` | `Long` | `0.0800` | 70,930.00 USD | 0.00 USD | 139.21 USD | `-14.15%` | `1,739.00` |
| `Live` | `Long` | `0.0801` | 70,790.00 USD | 0.00 USD | 6,210.00 USD | `-14.04%` | `77,489.00` |
| `Live` | `Long` | `0.0808` | 64,580.00 USD | 0.00 USD | 394.06 USD | `-13.40%` | `4,880.00` |
| `Live` | `Long` | `0.0809` | 64,180.00 USD | 0.00 USD | 487.61 USD | `-13.29%` | `6,031.00` |
| `Live` | `Long` | `0.0814` | 63,690.00 USD | 0.00 USD | 2,040.00 USD | `-12.65%` | `25,041.00` |
| `Live` | `Long` | `0.0819` | 61,650.00 USD | 0.00 USD | 181.85 USD | `-12.11%` | `2,219.00` |
| `Live` | `Long` | `0.0828` | 61,470.00 USD | 0.00 USD | 1,660.00 USD | `-11.26%` | `20,000.00` |
| `Live` | `Long` | `0.0830` | 59,820.00 USD | 0.00 USD | 1,110.00 USD | `-10.93%` | `13,414.00` |
| `Live` | `Long` | `0.0833` | 58,700.00 USD | 0.00 USD | 3,420.00 USD | `-10.61%` | `41,029.00` |
| `Live` | `Long` | `0.0835` | 55,280.00 USD | 0.00 USD | 7,980.00 USD | `-10.40%` | `95,507.00` |
| `Live` | `Long` | `0.0843` | 47,300.00 USD | 0.00 USD | 25,250.00 USD | `-9.54%` | `299,301.00` |
| `Live` | `Long` | `0.0844` | 22,060.00 USD | 0.00 USD | 808.44 USD | `-9.43%` | `9,573.00` |
| `Live` | `Long` | `0.0859` | 21,250.00 USD | 0.00 USD | 2,150.00 USD | `-7.82%` | `25,000.00` |
| `Live` | `Long` | `0.0862` | 19,100.00 USD | 0.00 USD | 1,450.00 USD | `-7.61%` | `16,779.00` |
| `Live` | `Long` | `0.0871` | 17,650.00 USD | 0.00 USD | 994.37 USD | `-6.64%` | `11,423.00` |
| `Live` | `Long` | `0.0872` | 16,660.00 USD | 0.00 USD | 133.43 USD | `-6.54%` | `1,531.00` |
| `Live` | `Long` | `0.0872` | 16,530.00 USD | 0.00 USD | 223.88 USD | `-6.43%` | `2,566.00` |
| `Live` | `Long` | `0.0880` | 16,300.00 USD | 0.00 USD | 4,640.00 USD | `-5.68%` | `52,790.00` |
| `Live` | `Long` | `0.0882` | 11,660.00 USD | 0.00 USD | 1,080.00 USD | `-5.36%` | `12,280.00` |
| `Live` | `Long` | `0.0886` | 10,580.00 USD | 0.00 USD | 142.57 USD | `-5.04%` | `1,610.00` |
| `Live` | `Long` | `0.0887` | 10,430.00 USD | 0.00 USD | 442.72 USD | `-4.93%` | `4,994.00` |
| `Live` | `Long` | `0.0893` | 9,990.00 USD | 0.00 USD | 695.50 USD | `-4.18%` | `7,784.00` |
| `Live` | `Long` | `0.0901` | 9,300.00 USD | 0.00 USD | 2,310.00 USD | `-3.43%` | `25,643.00` |
| `Live` | `Long` | `0.0912` | 6,990.00 USD | 0.00 USD | 909.76 USD | `-2.14%` | `9,970.00` |
| `Live` | `Long` | `0.0917` | 6,080.00 USD | 0.00 USD | 5,420.00 USD | `-1.60%` | `59,049.00` |
| `Live` | `Long` | `0.0922` | 659.13 USD | 0.00 USD | 659.13 USD | `-1.07%` | `7,145.00` |
| `Live` | `Short` | `0.1027` | 4,130.00 USD | 4,130.00 USD | 0.00 USD | `+10.09%` | `40,227.00` |
| `Live` | `Short` | `0.1109` | 4,350.00 USD | 217.13 USD | 0.00 USD | `+18.99%` | `1,957.00` |
| `Live` | `Short` | `0.1268` | 6,530.00 USD | 2,190.00 USD | 0.00 USD | `+35.93%` | `17,254.00` |
| `Live` | `Short` | `0.1384` | 9,010.00 USD | 2,480.00 USD | 0.00 USD | `+48.37%` | `17,912.00` |
| `Live` | `Short` | `0.1474` | 9,140.00 USD | 126.43 USD | 0.00 USD | `+58.02%` | `858.00` |
| `Live` | `Short` | `0.1477` | 9,300.00 USD | 162.97 USD | 0.00 USD | `+58.45%` | `1,103.00` |

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
  * Current Rate: `-601.97` | Last 24h: `-4.06K` | Last 3d: `-3.32K` | Last 7d: `-6.03K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0095%` | **USDT OKX** | `-0.0153%` |
| **USDT Bybit** | `0.0081%` | **USDT KuCoin** | `-0.0011%` |
| **USDT MEXC** | `-0.0093%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0007%` | **USDT Bitget** | `0.0100%` |
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
| `5m` | -20,440.00 USD | 10,350.00 USD | **`DISTRIBUTION`** |
| `15m` | -7,080.00 USD | 9,580.00 USD | **`ACCUMULATION`** |
| `30m` | 99,420.00 USD | 50,830.00 USD | **`ACCUMULATION`** |
| `1h` | -475,280.00 USD | -774,670.00 USD | **`DISTRIBUTION`** |
| `2h` | -579,320.00 USD | -804,880.00 USD | **`DISTRIBUTION`** |
| `4h` | -647,500.00 USD | -906,320.00 USD | **`DISTRIBUTION`** |
| `6h` | -683,510.00 USD | -1,270,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -696,130.00 USD | -1,320,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -666,160.00 USD | -1,260,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -754,680.00 USD | -1,520,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -2,020,000.00 USD | -3,260,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -13,230,000.00 USD | -20,610,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-20.44K` | 15m=`-7.08K` | 1h=`-475.28K` | 24h=`-754.68K`
* Futures Capital Netflows: 5m=`+10.35K` | 15m=`+9.58K` | 1h=`-774.67K` | 24h=`-1.52M`
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
  * `2026-10-30 02:54:26 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:10:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:11:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:11:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:11:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0937` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0888` (Risk Distance: `0.0049` pts)
  * +2.5R Take Profit: `0.1060`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0945` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0994` (Risk Distance: `0.0049` pts)
  * +2.5R Take Profit: `0.0822`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0961`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
