# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ALGUSD
**Canonical Key**: `ALGUSD` | **Broker Instrument**: `ALGUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-29 22:55:04 IST` (`2026-10-29 17:25:04 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1001` | **Live Ask Quote**: `0.1024` | **Mid Price**: `0.1013`
- **Spread Points**: `23.00` | **Spread BPS**: `227.16 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0994` | VWAP Z-Score: `+0.51` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000734` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.77` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1036` | Lower -3.00σ Band: `0.0951`
  * Upper +2.51σ Band: `0.1029` | Lower -2.51σ Band: `0.0958`
  * Upper +2.01σ Band: `0.1022` | Lower -2.01σ Band: `0.0965`
  * Upper +2.00σ Band: `0.1022` | Lower -2.00σ Band: `0.0965`
  * Upper +1.28σ Band: `0.1012` | Lower -1.28σ Band: `0.0976`
  * Upper +1.00σ Band: `0.1008` | Lower -1.00σ Band: `0.0980`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1007` | EMA-20=`0.1002` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0997` (Slope: `+0.0000`) | EMA-100=`0.1001`
  * Institutional Anchors: EMA-144=`0.1004` | EMA-200=`0.1008` (Slope: `-0.0124`) | EMA-233=`0.1010`
- **Range Boundaries**: 24H High=`0.1048` | 24H Low=`0.0972` | Weekly High=`0.1051` | Weekly Low=`0.0972`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1006` (Distance: `+0.55%`)
  * Point of Control (POC) = `0.0981` (Distance: `+3.17%`)
  * Value Area Low (VAL) = `0.0974` (Distance: `+3.91%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.1038` | POC=`0.1023` | VAL=`0.1011`
  * Prior Day Extremes: PDH=`0.1048` | PDL=`0.0994` | PDC=`0.1031`
  * Monday Range Blueprint: High=`0.1046` | Mid=`0.1031` | Low=`0.1015`
  * Developing Weekly Value Area: Weekly VAH=`0.1042` | Weekly POC=`0.1023` | Weekly VAL=`0.1011`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1037` | Low=`0.0972`
  * London Session (08:00-16:00 UTC): High=`0.0999` | Low=`0.0972`
  * New York Session (13:00-21:00 UTC): High=`0.1024` | Low=`0.0978`
  * Initial Balance (First Hour): IB High=`0.0999` | IB Low=`0.0987`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1008` - `0.1017`
  * Optimal Trade Entry (OTE 0.705): `0.1015`
  * Structural Invalidation Anchor (0.786): `0.1021`

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
| Hyperdash | Resting Book | - | - | - | Normal Interbank Book | - | - |

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
| `Live` | `Long Liquidation` | `0.0205` | 3,810.00 USD | 252,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0215` | 899.84 USD | 249,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0225` | 130.23 USD | 248,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0235` | 329.70 USD | 248,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0245` | 291.11 USD | 247,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0265` | 9,410.00 USD | 247,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0305` | 297.99 USD | 238,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0355` | 8,680.00 USD | 237,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0385` | 22,130.00 USD | 229,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0395` | 1,950.00 USD | 206,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 5,140.00 USD | 204,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 3,710.00 USD | 199,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 410.16 USD | 196,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 504.09 USD | 195,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 5,770.00 USD | 195,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0555` | 5,870.00 USD | 189,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 111.09 USD | 183,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 438.75 USD | 183,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 328.21 USD | 183,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 442.69 USD | 182,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 2,050.00 USD | 182,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 17,350.00 USD | 180,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 12,940.00 USD | 162,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 5,060.00 USD | 149,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 1,080.00 USD | 144,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 7,290.00 USD | 143,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 2,220.00 USD | 136,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,480.00 USD | 134,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 919.93 USD | 131,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 14,050.00 USD | 130,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 8,100.00 USD | 116,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 929.46 USD | 108,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 441.01 USD | 107,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 310.05 USD | 107,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 6,630.00 USD | 107,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 2,220.00 USD | 100,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 1,650.00 USD | 98,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 9,430.00 USD | 96,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 24,950.00 USD | 87,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 2,140.00 USD | 62,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 1,450.00 USD | 60,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 7,040.00 USD | 58,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 1,180.00 USD | 51,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 1,540.00 USD | 50,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 530.69 USD | 48,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 6,880.00 USD | 48,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 6,220.00 USD | 41,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 4,580.00 USD | 35,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 1,500.00 USD | 30,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 23,260.00 USD | 29,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 5,850.00 USD | 5,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1105` | 216.25 USD | 216.25 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1125` | 288.11 USD | 504.36 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1245` | 2,180.00 USD | 2,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1265` | 2,180.00 USD | 4,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1425` | 2,550.00 USD | 7,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1475` | 289.25 USD | 7,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1905` | 102.49 USD | 7,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0205` | 252,910.00 USD | 0.00 USD | 3,810.00 USD | `-79.88%` | `186,064.00` |
| `Live` | `Long` | `0.0215` | 249,100.00 USD | 0.00 USD | 899.84 USD | `-78.90%` | `41,853.00` |
| `Live` | `Long` | `0.0225` | 248,200.00 USD | 0.00 USD | 130.23 USD | `-77.92%` | `5,788.00` |
| `Live` | `Long` | `0.0235` | 248,070.00 USD | 0.00 USD | 329.70 USD | `-76.94%` | `14,030.00` |
| `Live` | `Long` | `0.0245` | 247,740.00 USD | 0.00 USD | 291.11 USD | `-75.96%` | `11,882.00` |
| `Live` | `Long` | `0.0265` | 247,450.00 USD | 0.00 USD | 9,410.00 USD | `-74.00%` | `355,228.00` |
| `Live` | `Long` | `0.0305` | 238,030.00 USD | 0.00 USD | 297.99 USD | `-70.07%` | `9,770.00` |
| `Live` | `Long` | `0.0355` | 237,740.00 USD | 0.00 USD | 8,680.00 USD | `-65.17%` | `244,544.00` |
| `Live` | `Long` | `0.0385` | 229,060.00 USD | 0.00 USD | 22,130.00 USD | `-62.22%` | `574,860.00` |
| `Live` | `Long` | `0.0395` | 206,920.00 USD | 0.00 USD | 1,950.00 USD | `-61.24%` | `49,368.00` |
| `Live` | `Long` | `0.0415` | 204,970.00 USD | 0.00 USD | 5,140.00 USD | `-59.28%` | `123,747.00` |
| `Live` | `Long` | `0.0425` | 199,840.00 USD | 0.00 USD | 3,710.00 USD | `-58.30%` | `87,382.00` |
| `Live` | `Long` | `0.0495` | 196,120.00 USD | 0.00 USD | 410.16 USD | `-51.43%` | `8,286.00` |
| `Live` | `Long` | `0.0505` | 195,710.00 USD | 0.00 USD | 504.09 USD | `-50.45%` | `9,982.00` |
| `Live` | `Long` | `0.0545` | 195,210.00 USD | 0.00 USD | 5,770.00 USD | `-46.52%` | `105,852.00` |
| `Live` | `Long` | `0.0555` | 189,440.00 USD | 0.00 USD | 5,870.00 USD | `-45.54%` | `105,702.00` |
| `Live` | `Long` | `0.0585` | 183,570.00 USD | 0.00 USD | 111.09 USD | `-42.60%` | `1,899.00` |
| `Live` | `Long` | `0.0595` | 183,460.00 USD | 0.00 USD | 438.75 USD | `-41.62%` | `7,374.00` |
| `Live` | `Long` | `0.0605` | 183,020.00 USD | 0.00 USD | 328.21 USD | `-40.63%` | `5,425.00` |
| `Live` | `Long` | `0.0625` | 182,700.00 USD | 0.00 USD | 442.69 USD | `-38.67%` | `7,083.00` |
| `Live` | `Long` | `0.0635` | 182,250.00 USD | 0.00 USD | 2,050.00 USD | `-37.69%` | `32,225.00` |
| `Live` | `Long` | `0.0655` | 180,210.00 USD | 0.00 USD | 17,350.00 USD | `-35.73%` | `264,927.00` |
| `Live` | `Long` | `0.0675` | 162,850.00 USD | 0.00 USD | 12,940.00 USD | `-33.77%` | `191,757.00` |
| `Live` | `Long` | `0.0685` | 149,910.00 USD | 0.00 USD | 5,060.00 USD | `-32.78%` | `73,856.00` |
| `Live` | `Long` | `0.0695` | 144,850.00 USD | 0.00 USD | 1,080.00 USD | `-31.80%` | `15,502.00` |
| `Live` | `Long` | `0.0715` | 143,770.00 USD | 0.00 USD | 7,290.00 USD | `-29.84%` | `101,931.00` |
| `Live` | `Long` | `0.0725` | 136,490.00 USD | 0.00 USD | 2,220.00 USD | `-28.86%` | `30,574.00` |
| `Live` | `Long` | `0.0735` | 134,270.00 USD | 0.00 USD | 2,480.00 USD | `-27.88%` | `33,731.00` |
| `Live` | `Long` | `0.0745` | 131,790.00 USD | 0.00 USD | 919.93 USD | `-26.90%` | `12,348.00` |
| `Live` | `Long` | `0.0755` | 130,870.00 USD | 0.00 USD | 14,050.00 USD | `-25.92%` | `186,042.00` |
| `Live` | `Long` | `0.0765` | 116,820.00 USD | 0.00 USD | 8,100.00 USD | `-24.93%` | `105,922.00` |
| `Live` | `Long` | `0.0775` | 108,720.00 USD | 0.00 USD | 929.46 USD | `-23.95%` | `11,993.00` |
| `Live` | `Long` | `0.0785` | 107,790.00 USD | 0.00 USD | 441.01 USD | `-22.97%` | `5,618.00` |
| `Live` | `Long` | `0.0795` | 107,350.00 USD | 0.00 USD | 310.05 USD | `-21.99%` | `3,900.00` |
| `Live` | `Long` | `0.0805` | 107,040.00 USD | 0.00 USD | 6,630.00 USD | `-21.01%` | `82,369.00` |
| `Live` | `Long` | `0.0815` | 100,410.00 USD | 0.00 USD | 2,220.00 USD | `-20.03%` | `27,260.00` |
| `Live` | `Long` | `0.0825` | 98,190.00 USD | 0.00 USD | 1,650.00 USD | `-19.05%` | `20,000.00` |
| `Live` | `Long` | `0.0835` | 96,540.00 USD | 0.00 USD | 9,430.00 USD | `-18.06%` | `112,949.00` |
| `Live` | `Long` | `0.0845` | 87,110.00 USD | 0.00 USD | 24,950.00 USD | `-17.08%` | `295,245.00` |
| `Live` | `Long` | `0.0855` | 62,160.00 USD | 0.00 USD | 2,140.00 USD | `-16.10%` | `25,000.00` |
| `Live` | `Long` | `0.0865` | 60,020.00 USD | 0.00 USD | 1,450.00 USD | `-15.12%` | `16,779.00` |
| `Live` | `Long` | `0.0875` | 58,570.00 USD | 0.00 USD | 7,040.00 USD | `-14.14%` | `80,402.00` |
| `Live` | `Long` | `0.0885` | 51,540.00 USD | 0.00 USD | 1,180.00 USD | `-13.16%` | `13,304.00` |
| `Live` | `Long` | `0.0895` | 50,360.00 USD | 0.00 USD | 1,540.00 USD | `-12.18%` | `17,219.00` |
| `Live` | `Long` | `0.0905` | 48,820.00 USD | 0.00 USD | 530.69 USD | `-11.20%` | `5,864.00` |
| `Live` | `Long` | `0.0915` | 48,290.00 USD | 0.00 USD | 6,880.00 USD | `-10.21%` | `75,183.00` |
| `Live` | `Long` | `0.0925` | 41,410.00 USD | 0.00 USD | 6,220.00 USD | `-9.23%` | `67,209.00` |
| `Live` | `Long` | `0.0935` | 35,190.00 USD | 0.00 USD | 4,580.00 USD | `-8.25%` | `48,972.00` |
| `Live` | `Long` | `0.0945` | 30,610.00 USD | 0.00 USD | 1,500.00 USD | `-7.27%` | `15,879.00` |
| `Live` | `Long` | `0.0965` | 29,110.00 USD | 0.00 USD | 23,260.00 USD | `-5.31%` | `241,013.00` |
| `Live` | `Long` | `0.0975` | 5,850.00 USD | 0.00 USD | 5,850.00 USD | `-4.33%` | `60,028.00` |
| `Live` | `Short` | `0.1105` | 216.25 USD | 216.25 USD | 0.00 USD | `+8.43%` | `1,957.00` |
| `Live` | `Short` | `0.1125` | 504.36 USD | 288.11 USD | 0.00 USD | `+10.39%` | `2,561.00` |
| `Live` | `Short` | `0.1245` | 2,680.00 USD | 2,180.00 USD | 0.00 USD | `+22.17%` | `17,482.00` |
| `Live` | `Short` | `0.1265` | 4,860.00 USD | 2,180.00 USD | 0.00 USD | `+24.13%` | `17,254.00` |
| `Live` | `Short` | `0.1425` | 7,420.00 USD | 2,550.00 USD | 0.00 USD | `+39.83%` | `17,912.00` |
| `Live` | `Short` | `0.1475` | 7,710.00 USD | 289.25 USD | 0.00 USD | `+44.74%` | `1,961.00` |
| `Live` | `Short` | `0.1905` | 7,810.00 USD | 102.49 USD | 0.00 USD | `+86.93%` | `538.00` |

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
  * Current Rate: `-213.44` | Last 24h: `-4.06K` | Last 3d: `-3.32K` | Last 7d: `-6.03K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0006%` | **USDT OKX** | `-0.0016%` |
| **USDT Bybit** | `-0.0031%` | **USDT KuCoin** | `0.0096%` |
| **USDT MEXC** | `-0.0003%` | **USDT BingX** | `0.0069%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0073%` |
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
| `5m` | -8,820.00 USD | -4,980.00 USD | **`DISTRIBUTION`** |
| `15m` | -28,970.00 USD | -27,860.00 USD | **`DISTRIBUTION`** |
| `30m` | -17,250.00 USD | -26,330.00 USD | **`DISTRIBUTION`** |
| `1h` | -3,440.00 USD | -155,690.00 USD | **`DISTRIBUTION`** |
| `2h` | -31,410.00 USD | -341,270.00 USD | **`DISTRIBUTION`** |
| `4h` | -42,410.00 USD | -433,330.00 USD | **`DISTRIBUTION`** |
| `6h` | -24,300.00 USD | -419,570.00 USD | **`DISTRIBUTION`** |
| `8h` | -11,080.00 USD | -235,510.00 USD | **`DISTRIBUTION`** |
| `12h` | 32,600.00 USD | -152,900.00 USD | **`DISTRIBUTION`** |
| `24h` | -3,710.00 USD | -331,960.00 USD | **`DISTRIBUTION`** |
| `1w` | -1,270,000.00 USD | -2,200,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -11,830,000.00 USD | -18,970,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-8.82K` | 15m=`-28.97K` | 1h=`-3.44K` | 24h=`-3.71K`
* Futures Capital Netflows: 5m=`-4.98K` | 15m=`-27.86K` | 1h=`-155.69K` | 24h=`-331.96K`
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
  * `2026-10-29 22:45:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:14 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [dol.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0974` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0931` (Risk Distance: `0.0046` pts)
  * +2.5R Take Profit: `0.1089`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1006` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.1049` (Risk Distance: `0.0046` pts)
  * +2.5R Take Profit: `0.0891`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1021`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
