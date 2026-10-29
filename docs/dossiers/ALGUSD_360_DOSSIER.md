# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ALGUSD
**Canonical Key**: `ALGUSD` | **Broker Instrument**: `ALGUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-29 23:52:58 IST` (`2026-10-29 18:22:58 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0992` | **Live Ask Quote**: `0.1014` | **Mid Price**: `0.1003`
- **Spread Points**: `22.00` | **Spread BPS**: `219.34 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0994` | VWAP Z-Score: `-0.14` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000740` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `43.39` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1035` | Lower -3.00σ Band: `0.0953`
  * Upper +2.51σ Band: `0.1028` | Lower -2.51σ Band: `0.0959`
  * Upper +2.01σ Band: `0.1022` | Lower -2.01σ Band: `0.0966`
  * Upper +2.00σ Band: `0.1021` | Lower -2.00σ Band: `0.0966`
  * Upper +1.28σ Band: `0.1012` | Lower -1.28σ Band: `0.0976`
  * Upper +1.00σ Band: `0.1008` | Lower -1.00σ Band: `0.0980`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1000` | EMA-20=`0.1000` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0997` (Slope: `+0.0000`) | EMA-100=`0.1000`
  * Institutional Anchors: EMA-144=`0.1004` | EMA-200=`0.1008` (Slope: `-0.0361`) | EMA-233=`0.1009`
- **Range Boundaries**: 24H High=`0.1048` | 24H Low=`0.0972` | Weekly High=`0.1051` | Weekly Low=`0.0972`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1006` (Distance: `-0.21%`)
  * Point of Control (POC) = `0.0995` (Distance: `+0.84%`)
  * Value Area Low (VAL) = `0.0974` (Distance: `+3.03%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
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
  * Golden Pocket Zone (0.618 - 0.650): `0.0999` - `0.1007`
  * Optimal Trade Entry (OTE 0.705): `0.1005`
  * Structural Invalidation Anchor (0.786): `0.1011`

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
| `Live` | `Long Liquidation` | `0.0205` | 3,650.00 USD | 264,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0235` | 329.70 USD | 260,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0245` | 1,030.00 USD | 260,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0255` | 209.05 USD | 259,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0305` | 10,830.00 USD | 258,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0385` | 376.14 USD | 248,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0395` | 9,660.00 USD | 247,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0405` | 23,280.00 USD | 238,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 2,050.00 USD | 214,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 3,710.00 USD | 212,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0435` | 5,380.00 USD | 209,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0455` | 540.63 USD | 203,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 410.16 USD | 203,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 504.09 USD | 202,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 318.93 USD | 202,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0555` | 5,870.00 USD | 201,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 514.39 USD | 195,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 111.09 USD | 195,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 6,390.00 USD | 195,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 328.21 USD | 188,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 442.69 USD | 188,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 2,050.00 USD | 188,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 17,350.00 USD | 186,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 18,260.00 USD | 168,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 5,060.00 USD | 150,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 1,080.00 USD | 145,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 7,290.00 USD | 144,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 2,220.00 USD | 137,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,480.00 USD | 134,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 919.93 USD | 132,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 10,240.00 USD | 131,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 12,170.00 USD | 121,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 929.46 USD | 109,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 441.01 USD | 108,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 310.05 USD | 107,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 6,630.00 USD | 107,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 2,220.00 USD | 100,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 1,650.00 USD | 98,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 9,430.00 USD | 96,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 24,950.00 USD | 87,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 2,140.00 USD | 62,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 1,450.00 USD | 60,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 7,040.00 USD | 58,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 1,180.00 USD | 51,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 1,540.00 USD | 50,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 559.29 USD | 49,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 6,880.00 USD | 48,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 6,560.00 USD | 41,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 4,580.00 USD | 35,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 1,500.00 USD | 30,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 23,260.00 USD | 29,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 5,850.00 USD | 5,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1105` | 216.25 USD | 216.25 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1125` | 288.11 USD | 504.36 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1265` | 2,180.00 USD | 2,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1415` | 2,530.00 USD | 5,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1475` | 289.25 USD | 5,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1905` | 102.49 USD | 5,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0205` | 264,140.00 USD | 0.00 USD | 3,650.00 USD | `-79.62%` | `177,866.00` |
| `Live` | `Long` | `0.0235` | 260,490.00 USD | 0.00 USD | 329.70 USD | `-76.63%` | `14,030.00` |
| `Live` | `Long` | `0.0245` | 260,160.00 USD | 0.00 USD | 1,030.00 USD | `-75.64%` | `41,853.00` |
| `Live` | `Long` | `0.0255` | 259,130.00 USD | 0.00 USD | 209.05 USD | `-74.64%` | `8,198.00` |
| `Live` | `Long` | `0.0305` | 258,920.00 USD | 0.00 USD | 10,830.00 USD | `-69.67%` | `355,228.00` |
| `Live` | `Long` | `0.0385` | 248,090.00 USD | 0.00 USD | 376.14 USD | `-61.72%` | `9,770.00` |
| `Live` | `Long` | `0.0395` | 247,710.00 USD | 0.00 USD | 9,660.00 USD | `-60.72%` | `244,544.00` |
| `Live` | `Long` | `0.0405` | 238,050.00 USD | 0.00 USD | 23,280.00 USD | `-59.73%` | `574,860.00` |
| `Live` | `Long` | `0.0415` | 214,770.00 USD | 0.00 USD | 2,050.00 USD | `-58.74%` | `49,368.00` |
| `Live` | `Long` | `0.0425` | 212,720.00 USD | 0.00 USD | 3,710.00 USD | `-57.74%` | `87,382.00` |
| `Live` | `Long` | `0.0435` | 209,010.00 USD | 0.00 USD | 5,380.00 USD | `-56.75%` | `123,747.00` |
| `Live` | `Long` | `0.0455` | 203,630.00 USD | 0.00 USD | 540.63 USD | `-54.76%` | `11,882.00` |
| `Live` | `Long` | `0.0495` | 203,090.00 USD | 0.00 USD | 410.16 USD | `-50.78%` | `8,286.00` |
| `Live` | `Long` | `0.0505` | 202,680.00 USD | 0.00 USD | 504.09 USD | `-49.79%` | `9,982.00` |
| `Live` | `Long` | `0.0545` | 202,170.00 USD | 0.00 USD | 318.93 USD | `-45.81%` | `5,852.00` |
| `Live` | `Long` | `0.0555` | 201,850.00 USD | 0.00 USD | 5,870.00 USD | `-44.81%` | `105,702.00` |
| `Live` | `Long` | `0.0575` | 195,990.00 USD | 0.00 USD | 514.39 USD | `-42.83%` | `8,946.00` |
| `Live` | `Long` | `0.0585` | 195,470.00 USD | 0.00 USD | 111.09 USD | `-41.83%` | `1,899.00` |
| `Live` | `Long` | `0.0595` | 195,360.00 USD | 0.00 USD | 6,390.00 USD | `-40.84%` | `107,374.00` |
| `Live` | `Long` | `0.0605` | 188,970.00 USD | 0.00 USD | 328.21 USD | `-39.84%` | `5,425.00` |
| `Live` | `Long` | `0.0625` | 188,640.00 USD | 0.00 USD | 442.69 USD | `-37.85%` | `7,083.00` |
| `Live` | `Long` | `0.0635` | 188,200.00 USD | 0.00 USD | 2,050.00 USD | `-36.86%` | `32,225.00` |
| `Live` | `Long` | `0.0655` | 186,160.00 USD | 0.00 USD | 17,350.00 USD | `-34.87%` | `264,927.00` |
| `Live` | `Long` | `0.0675` | 168,800.00 USD | 0.00 USD | 18,260.00 USD | `-32.88%` | `270,519.00` |
| `Live` | `Long` | `0.0685` | 150,540.00 USD | 0.00 USD | 5,060.00 USD | `-31.89%` | `73,856.00` |
| `Live` | `Long` | `0.0695` | 145,480.00 USD | 0.00 USD | 1,080.00 USD | `-30.89%` | `15,502.00` |
| `Live` | `Long` | `0.0715` | 144,410.00 USD | 0.00 USD | 7,290.00 USD | `-28.91%` | `101,931.00` |
| `Live` | `Long` | `0.0725` | 137,120.00 USD | 0.00 USD | 2,220.00 USD | `-27.91%` | `30,574.00` |
| `Live` | `Long` | `0.0735` | 134,900.00 USD | 0.00 USD | 2,480.00 USD | `-26.92%` | `33,731.00` |
| `Live` | `Long` | `0.0745` | 132,420.00 USD | 0.00 USD | 919.93 USD | `-25.92%` | `12,348.00` |
| `Live` | `Long` | `0.0755` | 131,500.00 USD | 0.00 USD | 10,240.00 USD | `-24.93%` | `135,635.00` |
| `Live` | `Long` | `0.0765` | 121,260.00 USD | 0.00 USD | 12,170.00 USD | `-23.93%` | `159,033.00` |
| `Live` | `Long` | `0.0775` | 109,100.00 USD | 0.00 USD | 929.46 USD | `-22.94%` | `11,993.00` |
| `Live` | `Long` | `0.0785` | 108,170.00 USD | 0.00 USD | 441.01 USD | `-21.94%` | `5,618.00` |
| `Live` | `Long` | `0.0795` | 107,730.00 USD | 0.00 USD | 310.05 USD | `-20.95%` | `3,900.00` |
| `Live` | `Long` | `0.0805` | 107,420.00 USD | 0.00 USD | 6,630.00 USD | `-19.96%` | `82,369.00` |
| `Live` | `Long` | `0.0815` | 100,780.00 USD | 0.00 USD | 2,220.00 USD | `-18.96%` | `27,260.00` |
| `Live` | `Long` | `0.0825` | 98,560.00 USD | 0.00 USD | 1,650.00 USD | `-17.97%` | `20,000.00` |
| `Live` | `Long` | `0.0835` | 96,910.00 USD | 0.00 USD | 9,430.00 USD | `-16.97%` | `112,949.00` |
| `Live` | `Long` | `0.0845` | 87,480.00 USD | 0.00 USD | 24,950.00 USD | `-15.98%` | `295,245.00` |
| `Live` | `Long` | `0.0855` | 62,530.00 USD | 0.00 USD | 2,140.00 USD | `-14.98%` | `25,000.00` |
| `Live` | `Long` | `0.0865` | 60,400.00 USD | 0.00 USD | 1,450.00 USD | `-13.99%` | `16,779.00` |
| `Live` | `Long` | `0.0875` | 58,940.00 USD | 0.00 USD | 7,040.00 USD | `-13.00%` | `80,402.00` |
| `Live` | `Long` | `0.0885` | 51,910.00 USD | 0.00 USD | 1,180.00 USD | `-12.00%` | `13,304.00` |
| `Live` | `Long` | `0.0895` | 50,730.00 USD | 0.00 USD | 1,540.00 USD | `-11.01%` | `17,219.00` |
| `Live` | `Long` | `0.0905` | 49,190.00 USD | 0.00 USD | 559.29 USD | `-10.01%` | `6,180.00` |
| `Live` | `Long` | `0.0915` | 48,630.00 USD | 0.00 USD | 6,880.00 USD | `-9.02%` | `75,183.00` |
| `Live` | `Long` | `0.0925` | 41,750.00 USD | 0.00 USD | 6,560.00 USD | `-8.02%` | `70,947.00` |
| `Live` | `Long` | `0.0935` | 35,190.00 USD | 0.00 USD | 4,580.00 USD | `-7.03%` | `48,972.00` |
| `Live` | `Long` | `0.0945` | 30,610.00 USD | 0.00 USD | 1,500.00 USD | `-6.04%` | `15,879.00` |
| `Live` | `Long` | `0.0965` | 29,110.00 USD | 0.00 USD | 23,260.00 USD | `-4.05%` | `241,013.00` |
| `Live` | `Long` | `0.0975` | 5,850.00 USD | 0.00 USD | 5,850.00 USD | `-3.05%` | `60,028.00` |
| `Live` | `Short` | `0.1105` | 216.25 USD | 216.25 USD | 0.00 USD | `+9.87%` | `1,957.00` |
| `Live` | `Short` | `0.1125` | 504.36 USD | 288.11 USD | 0.00 USD | `+11.86%` | `2,561.00` |
| `Live` | `Short` | `0.1265` | 2,690.00 USD | 2,180.00 USD | 0.00 USD | `+25.78%` | `17,254.00` |
| `Live` | `Short` | `0.1415` | 5,220.00 USD | 2,530.00 USD | 0.00 USD | `+40.70%` | `17,912.00` |
| `Live` | `Short` | `0.1475` | 5,510.00 USD | 289.25 USD | 0.00 USD | `+46.66%` | `1,961.00` |
| `Live` | `Short` | `0.1905` | 5,610.00 USD | 102.49 USD | 0.00 USD | `+89.42%` | `538.00` |

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
  * Current Rate: `-138.78` | Last 24h: `-4.06K` | Last 3d: `-3.32K` | Last 7d: `-6.03K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0020%` | **USDT OKX** | `-0.0034%` |
| **USDT Bybit** | `0.0025%` | **USDT KuCoin** | `0.0062%` |
| **USDT MEXC** | `-0.0022%` | **USDT BingX** | `0.0089%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0093%` |
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
| `5m` | 276.42 USD | -25,380.00 USD | **`DISTRIBUTION`** |
| `15m` | -4,040.00 USD | -22,700.00 USD | **`DISTRIBUTION`** |
| `30m` | -14,230.00 USD | -79,400.00 USD | **`DISTRIBUTION`** |
| `1h` | -51,780.00 USD | -107,490.00 USD | **`DISTRIBUTION`** |
| `2h` | -63,710.00 USD | -256,540.00 USD | **`DISTRIBUTION`** |
| `4h` | -48,330.00 USD | -448,830.00 USD | **`DISTRIBUTION`** |
| `6h` | -78,980.00 USD | -503,960.00 USD | **`DISTRIBUTION`** |
| `8h` | -72,120.00 USD | -453,880.00 USD | **`DISTRIBUTION`** |
| `12h` | -9,340.00 USD | -303,110.00 USD | **`DISTRIBUTION`** |
| `24h` | -143,950.00 USD | -520,490.00 USD | **`DISTRIBUTION`** |
| `1w` | -1,390,000.00 USD | -2,400,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,600,000.00 USD | -19,960,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+276.42` | 15m=`-4.04K` | 1h=`-51.78K` | 24h=`-143.95K`
* Futures Capital Netflows: 5m=`-25.38K` | 15m=`-22.70K` | 1h=`-107.49K` | 24h=`-520.49K`
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
  * `2026-10-29 23:31:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:51:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:51:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:52:26 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:52:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `0.0932` (Risk Distance: `0.0044` pts)
  * +2.5R Take Profit: `0.1084`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1006` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.1048` (Risk Distance: `0.0044` pts)
  * +2.5R Take Profit: `0.0896`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1011`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
