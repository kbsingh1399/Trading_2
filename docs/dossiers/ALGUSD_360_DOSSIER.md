# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ALGUSD
**Canonical Key**: `ALGUSD` | **Broker Instrument**: `ALGUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 04:50:10 IST` (`2026-10-29 23:20:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0929` | **Live Ask Quote**: `0.0952` | **Mid Price**: `0.0940`
- **Spread Points**: `23.00` | **Spread BPS**: `244.55 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0974` | VWAP Z-Score: `-1.52` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0012` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `31.14` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1063` | Lower -3.00σ Band: `0.0885`
  * Upper +2.51σ Band: `0.1049` | Lower -2.51σ Band: `0.0900`
  * Upper +2.01σ Band: `0.1034` | Lower -2.01σ Band: `0.0914`
  * Upper +2.00σ Band: `0.1033` | Lower -2.00σ Band: `0.0915`
  * Upper +1.28σ Band: `0.1012` | Lower -1.28σ Band: `0.0936`
  * Upper +1.00σ Band: `0.1004` | Lower -1.00σ Band: `0.0944`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0934` | EMA-20=`0.0949` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0970` (Slope: `+0.0000`) | EMA-100=`0.0984`
  * Institutional Anchors: EMA-144=`0.0991` | EMA-200=`0.0997` (Slope: `-0.8077`) | EMA-233=`0.1001`
- **Range Boundaries**: 24H High=`0.1032` | 24H Low=`0.0911` | Weekly High=`0.1051` | Weekly Low=`0.0911`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0937` (Distance: `+0.49%`)
  * Point of Control (POC) = `0.0930` (Distance: `+1.23%`)
  * Value Area Low (VAL) = `0.0921` (Distance: `+2.22%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.1013` | POC=`0.0982` | VAL=`0.0969`
  * Prior Day Extremes: PDH=`0.1037` | PDL=`0.0911` | PDC=`0.0922`
  * Monday Range Blueprint: High=`0.1046` | Mid=`0.1031` | Low=`0.1015`
  * Developing Weekly Value Area: Weekly VAH=`0.1043` | Weekly POC=`0.1025` | Weekly VAL=`0.0999`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0950` | Low=`0.0917`
  * London Session (08:00-16:00 UTC): High=`0.0944` | Low=`0.0937`
  * New York Session (13:00-21:00 UTC): High=`0.0946` | Low=`0.0935`
  * Initial Balance (First Hour): IB High=`0.0943` | IB Low=`0.0938`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0937` - `0.0944`
  * Optimal Trade Entry (OTE 0.705): `0.0942`
  * Structural Invalidation Anchor (0.786): `0.0948`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:46:31 IST` |

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
| `Live` | `Long Liquidation` | `0.0209` | 3,710.00 USD | 237,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0244` | 341.63 USD | 233,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0365` | 114.53 USD | 233,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0374` | 1,570.00 USD | 233,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0377` | 171.80 USD | 231,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0396` | 324.23 USD | 231,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0418` | 24,190.00 USD | 231,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0421` | 3,680.00 USD | 206,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0478` | 16,960.00 USD | 203,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 2,380.00 USD | 186,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0496` | 267.76 USD | 183,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 2,420.00 USD | 183,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 506.59 USD | 181,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 6,480.00 USD | 180,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0548` | 320.40 USD | 174,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0551` | 5,830.00 USD | 173,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 13,580.00 USD | 168,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 495.68 USD | 154,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0588` | 111.76 USD | 153,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 441.33 USD | 153,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 223.62 USD | 153,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 260.91 USD | 153,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0622` | 1,540.00 USD | 152,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 180.46 USD | 151,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 167.24 USD | 151,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 620.88 USD | 151,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 525.94 USD | 150,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0654` | 13,390.00 USD | 149,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 3,960.00 USD | 136,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0663` | 5,600.00 USD | 132,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0674` | 208.83 USD | 126,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0693` | 919.79 USD | 126,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0694` | 155.50 USD | 125,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0708` | 339.16 USD | 125,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0717` | 224.98 USD | 125,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0720` | 7,110.00 USD | 125,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0721` | 347.79 USD | 117,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0727` | 918.15 USD | 117,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0728` | 388.00 USD | 116,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0730` | 933.91 USD | 116,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0732` | 1,020.00 USD | 115,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 1,120.00 USD | 114,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0736` | 444.48 USD | 113,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0741` | 741.50 USD | 112,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0742` | 174.34 USD | 112,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0751` | 475.62 USD | 111,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0752` | 299.65 USD | 111,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0754` | 557.29 USD | 111,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 1,250.00 USD | 110,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0756` | 4,630.00 USD | 109,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0759` | 3,050.00 USD | 104,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0761` | 189.82 USD | 101,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0762` | 954.42 USD | 101,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0764` | 1,620.00 USD | 100,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0766` | 180.43 USD | 98,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0770` | 5,050.00 USD | 98,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 930.06 USD | 93,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0780` | 438.48 USD | 92,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0784` | 3,290.00 USD | 92,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0793` | 309.08 USD | 88,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 7,960.00 USD | 88,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0799` | 289.02 USD | 80,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0801` | 6,210.00 USD | 80,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0808` | 394.06 USD | 74,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0809` | 487.61 USD | 73,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0814` | 2,040.00 USD | 73,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0819` | 181.85 USD | 71,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0828` | 1,660.00 USD | 71,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0830` | 1,110.00 USD | 69,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0833` | 335.73 USD | 68,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 7,980.00 USD | 68,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0838` | 4,570.00 USD | 60,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0843` | 25,090.00 USD | 55,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0844` | 685.06 USD | 30,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0848` | 11,500.00 USD | 29,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0856` | 256.82 USD | 18,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0859` | 2,150.00 USD | 17,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0862` | 1,450.00 USD | 15,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0872` | 223.88 USD | 14,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0877` | 4,750.00 USD | 14,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0882` | 1,080.00 USD | 9,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0886` | 142.57 USD | 8,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0887` | 442.72 USD | 8,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0893` | 695.50 USD | 7,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0911` | 498.50 USD | 6,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0912` | 410.72 USD | 6,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0917` | 5,420.00 USD | 6,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0921` | 473.19 USD | 658.61 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0922` | 185.42 USD | 185.42 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1109` | 217.13 USD | 217.13 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1366` | 2,450.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1474` | 126.43 USD | 2,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1477` | 162.97 USD | 2,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0209` | 237,290.00 USD | 0.00 USD | 3,710.00 USD | `-77.79%` | `177,866.00` |
| `Live` | `Long` | `0.0244` | 233,580.00 USD | 0.00 USD | 341.63 USD | `-74.06%` | `14,030.00` |
| `Live` | `Long` | `0.0365` | 233,240.00 USD | 0.00 USD | 114.53 USD | `-61.17%` | `3,142.00` |
| `Live` | `Long` | `0.0374` | 233,120.00 USD | 0.00 USD | 1,570.00 USD | `-60.10%` | `41,853.00` |
| `Live` | `Long` | `0.0377` | 231,560.00 USD | 0.00 USD | 171.80 USD | `-59.89%` | `4,563.00` |
| `Live` | `Long` | `0.0396` | 231,380.00 USD | 0.00 USD | 324.23 USD | `-57.87%` | `8,198.00` |
| `Live` | `Long` | `0.0418` | 231,060.00 USD | 0.00 USD | 24,190.00 USD | `-55.42%` | `578,040.00` |
| `Live` | `Long` | `0.0421` | 206,870.00 USD | 0.00 USD | 3,680.00 USD | `-55.10%` | `87,382.00` |
| `Live` | `Long` | `0.0478` | 203,190.00 USD | 0.00 USD | 16,960.00 USD | `-49.13%` | `355,228.00` |
| `Live` | `Long` | `0.0481` | 186,220.00 USD | 0.00 USD | 2,380.00 USD | `-48.70%` | `49,368.00` |
| `Live` | `Long` | `0.0496` | 183,850.00 USD | 0.00 USD | 267.76 USD | `-47.11%` | `5,393.00` |
| `Live` | `Long` | `0.0503` | 183,580.00 USD | 0.00 USD | 2,420.00 USD | `-46.47%` | `48,218.00` |
| `Live` | `Long` | `0.0508` | 181,160.00 USD | 0.00 USD | 506.59 USD | `-45.93%` | `9,982.00` |
| `Live` | `Long` | `0.0524` | 180,650.00 USD | 0.00 USD | 6,480.00 USD | `-44.23%` | `123,747.00` |
| `Live` | `Long` | `0.0548` | 174,170.00 USD | 0.00 USD | 320.40 USD | `-41.67%` | `5,852.00` |
| `Live` | `Long` | `0.0551` | 173,850.00 USD | 0.00 USD | 5,830.00 USD | `-41.25%` | `105,702.00` |
| `Live` | `Long` | `0.0556` | 168,020.00 USD | 0.00 USD | 13,580.00 USD | `-40.82%` | `244,544.00` |
| `Live` | `Long` | `0.0563` | 154,440.00 USD | 0.00 USD | 495.68 USD | `-40.08%` | `8,812.00` |
| `Live` | `Long` | `0.0588` | 153,940.00 USD | 0.00 USD | 111.76 USD | `-37.31%` | `1,899.00` |
| `Live` | `Long` | `0.0599` | 153,830.00 USD | 0.00 USD | 441.33 USD | `-36.24%` | `7,374.00` |
| `Live` | `Long` | `0.0609` | 153,390.00 USD | 0.00 USD | 223.62 USD | `-35.17%` | `3,675.00` |
| `Live` | `Long` | `0.0621` | 153,170.00 USD | 0.00 USD | 260.91 USD | `-33.79%` | `4,198.00` |
| `Live` | `Long` | `0.0622` | 152,900.00 USD | 0.00 USD | 1,540.00 USD | `-33.68%` | `24,765.00` |
| `Live` | `Long` | `0.0625` | 151,360.00 USD | 0.00 USD | 180.46 USD | `-33.36%` | `2,885.00` |
| `Live` | `Long` | `0.0634` | 151,180.00 USD | 0.00 USD | 167.24 USD | `-32.51%` | `2,640.00` |
| `Live` | `Long` | `0.0635` | 151,010.00 USD | 0.00 USD | 620.88 USD | `-32.30%` | `9,770.00` |
| `Live` | `Long` | `0.0636` | 150,390.00 USD | 0.00 USD | 525.94 USD | `-32.19%` | `8,263.00` |
| `Live` | `Long` | `0.0654` | 149,870.00 USD | 0.00 USD | 13,390.00 USD | `-30.38%` | `204,927.00` |
| `Live` | `Long` | `0.0659` | 136,480.00 USD | 0.00 USD | 3,960.00 USD | `-29.74%` | `60,000.00` |
| `Live` | `Long` | `0.0663` | 132,520.00 USD | 0.00 USD | 5,600.00 USD | `-29.42%` | `84,534.00` |
| `Live` | `Long` | `0.0674` | 126,920.00 USD | 0.00 USD | 208.83 USD | `-28.14%` | `3,096.00` |
| `Live` | `Long` | `0.0693` | 126,710.00 USD | 0.00 USD | 919.79 USD | `-26.12%` | `13,263.00` |
| `Live` | `Long` | `0.0694` | 125,790.00 USD | 0.00 USD | 155.50 USD | `-26.01%` | `2,239.00` |
| `Live` | `Long` | `0.0708` | 125,630.00 USD | 0.00 USD | 339.16 USD | `-24.52%` | `4,787.00` |
| `Live` | `Long` | `0.0717` | 125,300.00 USD | 0.00 USD | 224.98 USD | `-23.67%` | `3,140.00` |
| `Live` | `Long` | `0.0720` | 125,070.00 USD | 0.00 USD | 7,110.00 USD | `-23.35%` | `98,791.00` |
| `Live` | `Long` | `0.0721` | 117,960.00 USD | 0.00 USD | 347.79 USD | `-23.24%` | `4,827.00` |
| `Live` | `Long` | `0.0727` | 117,610.00 USD | 0.00 USD | 918.15 USD | `-22.60%` | `12,638.00` |
| `Live` | `Long` | `0.0728` | 116,700.00 USD | 0.00 USD | 388.00 USD | `-22.39%` | `5,326.00` |
| `Live` | `Long` | `0.0730` | 116,310.00 USD | 0.00 USD | 933.91 USD | `-22.28%` | `12,802.00` |
| `Live` | `Long` | `0.0732` | 115,370.00 USD | 0.00 USD | 1,020.00 USD | `-21.96%` | `13,863.00` |
| `Live` | `Long` | `0.0735` | 114,360.00 USD | 0.00 USD | 1,120.00 USD | `-21.75%` | `15,256.00` |
| `Live` | `Long` | `0.0736` | 113,240.00 USD | 0.00 USD | 444.48 USD | `-21.54%` | `6,035.00` |
| `Live` | `Long` | `0.0741` | 112,790.00 USD | 0.00 USD | 741.50 USD | `-21.01%` | `10,000.00` |
| `Live` | `Long` | `0.0742` | 112,050.00 USD | 0.00 USD | 174.34 USD | `-20.90%` | `2,348.00` |
| `Live` | `Long` | `0.0751` | 111,880.00 USD | 0.00 USD | 475.62 USD | `-19.94%` | `6,329.00` |
| `Live` | `Long` | `0.0752` | 111,400.00 USD | 0.00 USD | 299.65 USD | `-19.83%` | `3,982.00` |
| `Live` | `Long` | `0.0754` | 111,100.00 USD | 0.00 USD | 557.29 USD | `-19.73%` | `7,396.00` |
| `Live` | `Long` | `0.0755` | 110,550.00 USD | 0.00 USD | 1,250.00 USD | `-19.62%` | `16,502.00` |
| `Live` | `Long` | `0.0756` | 109,300.00 USD | 0.00 USD | 4,630.00 USD | `-19.41%` | `61,227.00` |
| `Live` | `Long` | `0.0759` | 104,670.00 USD | 0.00 USD | 3,050.00 USD | `-19.20%` | `40,199.00` |
| `Live` | `Long` | `0.0761` | 101,620.00 USD | 0.00 USD | 189.82 USD | `-18.98%` | `2,496.00` |
| `Live` | `Long` | `0.0762` | 101,430.00 USD | 0.00 USD | 954.42 USD | `-18.77%` | `12,517.00` |
| `Live` | `Long` | `0.0764` | 100,480.00 USD | 0.00 USD | 1,620.00 USD | `-18.66%` | `21,173.00` |
| `Live` | `Long` | `0.0766` | 98,860.00 USD | 0.00 USD | 180.43 USD | `-18.34%` | `2,354.00` |
| `Live` | `Long` | `0.0770` | 98,680.00 USD | 0.00 USD | 5,050.00 USD | `-18.02%` | `65,640.00` |
| `Live` | `Long` | `0.0775` | 93,630.00 USD | 0.00 USD | 930.06 USD | `-17.38%` | `11,993.00` |
| `Live` | `Long` | `0.0780` | 92,700.00 USD | 0.00 USD | 438.48 USD | `-16.85%` | `5,618.00` |
| `Live` | `Long` | `0.0784` | 92,260.00 USD | 0.00 USD | 3,290.00 USD | `-16.53%` | `41,966.00` |
| `Live` | `Long` | `0.0793` | 88,970.00 USD | 0.00 USD | 309.08 USD | `-15.57%` | `3,900.00` |
| `Live` | `Long` | `0.0795` | 88,660.00 USD | 0.00 USD | 7,960.00 USD | `-15.25%` | `100,000.00` |
| `Live` | `Long` | `0.0799` | 80,710.00 USD | 0.00 USD | 289.02 USD | `-14.83%` | `3,615.00` |
| `Live` | `Long` | `0.0801` | 80,420.00 USD | 0.00 USD | 6,210.00 USD | `-14.61%` | `77,489.00` |
| `Live` | `Long` | `0.0808` | 74,210.00 USD | 0.00 USD | 394.06 USD | `-13.97%` | `4,880.00` |
| `Live` | `Long` | `0.0809` | 73,810.00 USD | 0.00 USD | 487.61 USD | `-13.87%` | `6,031.00` |
| `Live` | `Long` | `0.0814` | 73,330.00 USD | 0.00 USD | 2,040.00 USD | `-13.23%` | `25,041.00` |
| `Live` | `Long` | `0.0819` | 71,290.00 USD | 0.00 USD | 181.85 USD | `-12.70%` | `2,219.00` |
| `Live` | `Long` | `0.0828` | 71,100.00 USD | 0.00 USD | 1,660.00 USD | `-11.84%` | `20,000.00` |
| `Live` | `Long` | `0.0830` | 69,450.00 USD | 0.00 USD | 1,110.00 USD | `-11.52%` | `13,414.00` |
| `Live` | `Long` | `0.0833` | 68,340.00 USD | 0.00 USD | 335.73 USD | `-11.21%` | `4,028.00` |
| `Live` | `Long` | `0.0835` | 68,000.00 USD | 0.00 USD | 7,980.00 USD | `-10.99%` | `95,507.00` |
| `Live` | `Long` | `0.0838` | 60,020.00 USD | 0.00 USD | 4,570.00 USD | `-10.78%` | `54,577.00` |
| `Live` | `Long` | `0.0843` | 55,450.00 USD | 0.00 USD | 25,090.00 USD | `-10.14%` | `297,495.00` |
| `Live` | `Long` | `0.0844` | 30,360.00 USD | 0.00 USD | 685.06 USD | `-10.03%` | `8,112.00` |
| `Live` | `Long` | `0.0848` | 29,670.00 USD | 0.00 USD | 11,500.00 USD | `-9.71%` | `135,669.00` |
| `Live` | `Long` | `0.0856` | 18,170.00 USD | 0.00 USD | 256.82 USD | `-8.86%` | `3,002.00` |
| `Live` | `Long` | `0.0859` | 17,920.00 USD | 0.00 USD | 2,150.00 USD | `-8.44%` | `25,000.00` |
| `Live` | `Long` | `0.0862` | 15,770.00 USD | 0.00 USD | 1,450.00 USD | `-8.22%` | `16,779.00` |
| `Live` | `Long` | `0.0872` | 14,320.00 USD | 0.00 USD | 223.88 USD | `-7.05%` | `2,566.00` |
| `Live` | `Long` | `0.0877` | 14,100.00 USD | 0.00 USD | 4,750.00 USD | `-6.52%` | `54,098.00` |
| `Live` | `Long` | `0.0882` | 9,350.00 USD | 0.00 USD | 1,080.00 USD | `-5.99%` | `12,280.00` |
| `Live` | `Long` | `0.0886` | 8,270.00 USD | 0.00 USD | 142.57 USD | `-5.67%` | `1,610.00` |
| `Live` | `Long` | `0.0887` | 8,120.00 USD | 0.00 USD | 442.72 USD | `-5.56%` | `4,994.00` |
| `Live` | `Long` | `0.0893` | 7,680.00 USD | 0.00 USD | 695.50 USD | `-4.81%` | `7,784.00` |
| `Live` | `Long` | `0.0911` | 6,990.00 USD | 0.00 USD | 498.50 USD | `-2.90%` | `5,469.00` |
| `Live` | `Long` | `0.0912` | 6,490.00 USD | 0.00 USD | 410.72 USD | `-2.79%` | `4,501.00` |
| `Live` | `Long` | `0.0917` | 6,080.00 USD | 0.00 USD | 5,420.00 USD | `-2.26%` | `59,049.00` |
| `Live` | `Long` | `0.0921` | 658.61 USD | 0.00 USD | 473.19 USD | `-1.83%` | `5,135.00` |
| `Live` | `Long` | `0.0922` | 185.42 USD | 0.00 USD | 185.42 USD | `-1.72%` | `2,010.00` |
| `Live` | `Short` | `0.1109` | 217.13 USD | 217.13 USD | 0.00 USD | `+18.20%` | `1,957.00` |
| `Live` | `Short` | `0.1366` | 2,660.00 USD | 2,450.00 USD | 0.00 USD | `+45.58%` | `17,912.00` |
| `Live` | `Short` | `0.1474` | 2,790.00 USD | 126.43 USD | 0.00 USD | `+56.98%` | `858.00` |
| `Live` | `Short` | `0.1477` | 2,950.00 USD | 162.97 USD | 0.00 USD | `+57.40%` | `1,103.00` |

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
  * Current Rate: `-428.08` | Last 24h: `-4.06K` | Last 3d: `-3.32K` | Last 7d: `-6.03K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0087%` | **USDT OKX** | `-0.0148%` |
| **USDT Bybit** | `0.0086%` | **USDT KuCoin** | `0.0052%` |
| **USDT MEXC** | `-0.0085%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0002%` | **USDT Bitget** | `0.0100%` |
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
| `5m` | 6,670.00 USD | 10,770.00 USD | **`ACCUMULATION`** |
| `15m` | -12,080.00 USD | 39,650.00 USD | **`ACCUMULATION`** |
| `30m` | 20,000.00 USD | 12,190.00 USD | **`ACCUMULATION`** |
| `1h` | 32,900.00 USD | -3,480.00 USD | **`ACCUMULATION`** |
| `2h` | -62,710.00 USD | -81,740.00 USD | **`DISTRIBUTION`** |
| `4h` | -643,480.00 USD | -891,660.00 USD | **`DISTRIBUTION`** |
| `6h` | -724,730.00 USD | -1,020,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -767,330.00 USD | -1,300,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -763,560.00 USD | -1,450,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -882,710.00 USD | -1,630,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -2,120,000.00 USD | -3,370,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -13,170,000.00 USD | -20,460,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+6.67K` | 15m=`-12.08K` | 1h=`+32.90K` | 24h=`-882.71K`
* Futures Capital Netflows: 5m=`+10.77K` | 15m=`+39.65K` | 1h=`-3.48K` | 24h=`-1.63M`
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
  * `2026-10-30 04:15:34 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:40:34 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:34 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0921` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0873` (Risk Distance: `0.0048` pts)
  * +2.5R Take Profit: `0.1042`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0937` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0985` (Risk Distance: `0.0048` pts)
  * +2.5R Take Profit: `0.0816`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0948`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
