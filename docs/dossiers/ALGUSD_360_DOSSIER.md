# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ALGUSD
**Canonical Key**: `ALGUSD` | **Broker Instrument**: `ALGUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 09:43:23 IST` (`2026-10-30 04:13:23 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0926` | **Live Ask Quote**: `0.0949` | **Mid Price**: `0.0938`
- **Spread Points**: `23.00` | **Spread BPS**: `245.33 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0910` | VWAP Z-Score: `+2.23` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.000983` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `51.12` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0936` | Lower -3.00σ Band: `0.0884`
  * Upper +2.51σ Band: `0.0931` | Lower -2.51σ Band: `0.0888`
  * Upper +2.01σ Band: `0.0927` | Lower -2.01σ Band: `0.0892`
  * Upper +2.00σ Band: `0.0927` | Lower -2.00σ Band: `0.0892`
  * Upper +1.28σ Band: `0.0921` | Lower -1.28σ Band: `0.0899`
  * Upper +1.00σ Band: `0.0918` | Lower -1.00σ Band: `0.0901`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0922` | EMA-20=`0.0923` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0942` (Slope: `+0.0000`) | EMA-100=`0.0963`
  * Institutional Anchors: EMA-144=`0.0974` | EMA-200=`0.0983` (Slope: `-0.8367`) | EMA-233=`0.0989`
- **Range Boundaries**: 24H High=`0.1024` | 24H Low=`0.0881` | Weekly High=`0.1048` | Weekly Low=`0.0881`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0932` (Distance: `+0.56%`)
  * Point of Control (POC) = `0.0926` (Distance: `+1.26%`)
  * Value Area Low (VAL) = `0.0906` (Distance: `+3.47%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.1013` | POC=`0.0982` | VAL=`0.0969`
  * Prior Day Extremes: PDH=`0.1037` | PDL=`0.0911` | PDC=`0.0922`
  * Monday Range Blueprint: High=`0.1046` | Mid=`0.1031` | Low=`0.1015`
  * Developing Weekly Value Area: Weekly VAH=`0.1044` | Weekly POC=`0.1026` | Weekly VAL=`0.0986`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0950` | Low=`0.0881`
  * London Session (08:00-16:00 UTC): High=`0.0941` | Low=`0.0934`
  * New York Session (13:00-21:00 UTC): High=`0.0943` | Low=`0.0932`
  * Initial Balance (First Hour): IB High=`0.0940` | IB Low=`0.0935`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0934` - `0.0941`
  * Optimal Trade Entry (OTE 0.705): `0.0939`
  * Structural Invalidation Anchor (0.786): `0.0945`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:33:32 IST` |

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
| `Live` | `Long Liquidation` | `0.0209` | 3,710.00 USD | 192,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0223` | 206.00 USD | 188,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0249` | 350.05 USD | 188,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0314` | 17,120.00 USD | 188,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0421` | 3,680.00 USD | 171,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0428` | 2,140.00 USD | 167,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0437` | 1,860.00 USD | 165,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 146.57 USD | 163,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0473` | 5,850.00 USD | 163,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 2,440.00 USD | 157,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0496` | 267.76 USD | 155,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 506.59 USD | 154,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 19,160.00 USD | 154,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 319.81 USD | 135,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0551` | 5,830.00 USD | 134,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0588` | 111.76 USD | 128,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 441.33 USD | 128,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 223.26 USD | 128,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 1,630.00 USD | 128,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 260.91 USD | 126,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 180.46 USD | 126,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 167.24 USD | 126,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 525.94 USD | 125,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0654` | 13,390.00 USD | 125,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 3,960.00 USD | 112,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0663` | 5,600.00 USD | 108,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0674` | 208.83 USD | 102,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0687` | 1,140.00 USD | 102,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0693` | 919.79 USD | 101,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0694` | 266.20 USD | 100,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0698` | 165.31 USD | 99,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0713` | 341.55 USD | 99,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0717` | 224.98 USD | 99,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0720` | 7,110.00 USD | 99,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0721` | 347.79 USD | 92,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0727` | 918.15 USD | 91,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0728` | 388.00 USD | 90,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0730` | 933.91 USD | 90,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0732` | 1,020.00 USD | 89,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 1,120.00 USD | 88,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0736` | 444.48 USD | 87,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0737` | 720.54 USD | 86,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0741` | 741.50 USD | 86,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0742` | 174.34 USD | 85,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0751` | 475.62 USD | 85,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0752` | 299.65 USD | 84,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0754` | 557.29 USD | 84,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 1,250.00 USD | 83,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0756` | 4,630.00 USD | 82,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0757` | 2,900.00 USD | 78,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0759` | 142.90 USD | 75,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0761` | 189.82 USD | 75,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0764` | 1,620.00 USD | 74,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0766` | 180.43 USD | 73,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0769` | 333.76 USD | 73,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0770` | 5,050.00 USD | 72,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 930.06 USD | 67,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0780` | 438.48 USD | 66,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0784` | 3,150.00 USD | 66,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0793` | 309.08 USD | 63,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0799` | 289.02 USD | 62,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0801` | 6,210.00 USD | 62,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0806` | 393.57 USD | 56,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0809` | 487.61 USD | 55,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0809` | 729.68 USD | 55,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0814` | 2,480.00 USD | 54,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0819` | 181.85 USD | 52,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0828` | 1,660.00 USD | 52,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0830` | 1,110.00 USD | 50,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0833` | 335.73 USD | 49,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 7,980.00 USD | 48,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0838` | 4,570.00 USD | 40,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0839` | 209.88 USD | 36,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0843` | 24,900.00 USD | 36,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0848` | 811.31 USD | 11,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0859` | 2,150.00 USD | 10,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0862` | 1,450.00 USD | 8,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0872` | 223.88 USD | 6,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0877` | 4,750.00 USD | 6,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0882` | 1,080.00 USD | 1,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0886` | 142.57 USD | 838.07 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0893` | 695.50 USD | 695.50 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1003` | 282.20 USD | 282.20 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1003` | 1,360.00 USD | 1,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1007` | 545.62 USD | 2,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1022` | 402.47 USD | 2,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1109` | 217.13 USD | 2,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1361` | 2,440.00 USD | 5,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1477` | 162.97 USD | 5,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1689` | 294.81 USD | 5,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0209` | 190,320.00 USD | 0.00 USD | 3,710.00 USD | `-77.82%` | `177,866.00` |
| `Live` | `Long` | `0.0225` | 186,610.00 USD | 0.00 USD | 314.97 USD | `-76.12%` | `14,030.00` |
| `Live` | `Long` | `0.0301` | 186,290.00 USD | 0.00 USD | 16,460.00 USD | `-68.04%` | `547,660.00` |
| `Live` | `Long` | `0.0384` | 169,840.00 USD | 0.00 USD | 315.21 USD | `-59.10%` | `8,198.00` |
| `Live` | `Long` | `0.0396` | 169,520.00 USD | 0.00 USD | 1,660.00 USD | `-57.83%` | `41,853.00` |
| `Live` | `Long` | `0.0413` | 167,860.00 USD | 0.00 USD | 129.92 USD | `-56.02%` | `3,142.00` |
| `Live` | `Long` | `0.0421` | 167,730.00 USD | 0.00 USD | 3,680.00 USD | `-55.17%` | `87,382.00` |
| `Live` | `Long` | `0.0423` | 164,050.00 USD | 0.00 USD | 1,800.00 USD | `-54.95%` | `42,432.00` |
| `Live` | `Long` | `0.0466` | 162,250.00 USD | 0.00 USD | 5,770.00 USD | `-50.38%` | `123,747.00` |
| `Live` | `Long` | `0.0476` | 156,480.00 USD | 0.00 USD | 2,350.00 USD | `-49.42%` | `49,368.00` |
| `Live` | `Long` | `0.0496` | 154,130.00 USD | 0.00 USD | 267.76 USD | `-47.19%` | `5,393.00` |
| `Live` | `Long` | `0.0508` | 153,860.00 USD | 0.00 USD | 506.59 USD | `-46.02%` | `9,982.00` |
| `Live` | `Long` | `0.0517` | 153,360.00 USD | 0.00 USD | 18,350.00 USD | `-45.06%` | `355,228.00` |
| `Live` | `Long` | `0.0548` | 135,010.00 USD | 0.00 USD | 320.40 USD | `-41.77%` | `5,852.00` |
| `Live` | `Long` | `0.0551` | 134,690.00 USD | 0.00 USD | 5,830.00 USD | `-41.34%` | `105,702.00` |
| `Live` | `Long` | `0.0588` | 128,860.00 USD | 0.00 USD | 111.76 USD | `-37.40%` | `1,899.00` |
| `Live` | `Long` | `0.0599` | 128,750.00 USD | 0.00 USD | 441.33 USD | `-36.34%` | `7,374.00` |
| `Live` | `Long` | `0.0607` | 128,310.00 USD | 0.00 USD | 223.26 USD | `-35.38%` | `3,675.00` |
| `Live` | `Long` | `0.0614` | 128,080.00 USD | 0.00 USD | 1,630.00 USD | `-34.64%` | `26,498.00` |
| `Live` | `Long` | `0.0621` | 126,450.00 USD | 0.00 USD | 260.91 USD | `-33.89%` | `4,198.00` |
| `Live` | `Long` | `0.0625` | 126,190.00 USD | 0.00 USD | 180.46 USD | `-33.47%` | `2,885.00` |
| `Live` | `Long` | `0.0634` | 126,010.00 USD | 0.00 USD | 167.24 USD | `-32.62%` | `2,640.00` |
| `Live` | `Long` | `0.0636` | 125,850.00 USD | 0.00 USD | 525.94 USD | `-32.30%` | `8,263.00` |
| `Live` | `Long` | `0.0641` | 125,320.00 USD | 0.00 USD | 626.75 USD | `-31.77%` | `9,770.00` |
| `Live` | `Long` | `0.0654` | 124,690.00 USD | 0.00 USD | 13,390.00 USD | `-30.49%` | `204,927.00` |
| `Live` | `Long` | `0.0659` | 111,300.00 USD | 0.00 USD | 3,960.00 USD | `-29.85%` | `60,000.00` |
| `Live` | `Long` | `0.0663` | 107,340.00 USD | 0.00 USD | 5,600.00 USD | `-29.53%` | `84,534.00` |
| `Live` | `Long` | `0.0674` | 101,740.00 USD | 0.00 USD | 208.83 USD | `-28.26%` | `3,096.00` |
| `Live` | `Long` | `0.0687` | 101,540.00 USD | 0.00 USD | 1,140.00 USD | `-26.98%` | `16,582.00` |
| `Live` | `Long` | `0.0691` | 100,400.00 USD | 0.00 USD | 330.54 USD | `-26.56%` | `4,787.00` |
| `Live` | `Long` | `0.0693` | 100,070.00 USD | 0.00 USD | 919.79 USD | `-26.24%` | `13,263.00` |
| `Live` | `Long` | `0.0694` | 99,150.00 USD | 0.00 USD | 266.20 USD | `-26.13%` | `3,833.00` |
| `Live` | `Long` | `0.0698` | 98,880.00 USD | 0.00 USD | 165.31 USD | `-25.81%` | `2,370.00` |
| `Live` | `Long` | `0.0717` | 98,720.00 USD | 0.00 USD | 224.98 USD | `-23.79%` | `3,140.00` |
| `Live` | `Long` | `0.0720` | 98,490.00 USD | 0.00 USD | 7,110.00 USD | `-23.47%` | `98,791.00` |
| `Live` | `Long` | `0.0721` | 91,380.00 USD | 0.00 USD | 347.79 USD | `-23.36%` | `4,827.00` |
| `Live` | `Long` | `0.0727` | 91,030.00 USD | 0.00 USD | 918.15 USD | `-22.73%` | `12,638.00` |
| `Live` | `Long` | `0.0728` | 90,120.00 USD | 0.00 USD | 388.00 USD | `-22.51%` | `5,326.00` |
| `Live` | `Long` | `0.0730` | 89,730.00 USD | 0.00 USD | 933.91 USD | `-22.41%` | `12,802.00` |
| `Live` | `Long` | `0.0732` | 88,790.00 USD | 0.00 USD | 1,020.00 USD | `-22.09%` | `13,863.00` |
| `Live` | `Long` | `0.0735` | 87,780.00 USD | 0.00 USD | 1,120.00 USD | `-21.88%` | `15,256.00` |
| `Live` | `Long` | `0.0736` | 86,660.00 USD | 0.00 USD | 444.48 USD | `-21.66%` | `6,035.00` |
| `Live` | `Long` | `0.0741` | 86,210.00 USD | 0.00 USD | 741.50 USD | `-21.13%` | `10,000.00` |
| `Live` | `Long` | `0.0742` | 85,470.00 USD | 0.00 USD | 174.34 USD | `-21.02%` | `2,348.00` |
| `Live` | `Long` | `0.0751` | 85,300.00 USD | 0.00 USD | 475.62 USD | `-20.07%` | `6,329.00` |
| `Live` | `Long` | `0.0752` | 84,820.00 USD | 0.00 USD | 299.65 USD | `-19.96%` | `3,982.00` |
| `Live` | `Long` | `0.0754` | 84,520.00 USD | 0.00 USD | 557.29 USD | `-19.85%` | `7,396.00` |
| `Live` | `Long` | `0.0755` | 83,970.00 USD | 0.00 USD | 1,250.00 USD | `-19.75%` | `16,502.00` |
| `Live` | `Long` | `0.0756` | 82,720.00 USD | 0.00 USD | 4,630.00 USD | `-19.54%` | `61,227.00` |
| `Live` | `Long` | `0.0757` | 78,090.00 USD | 0.00 USD | 2,900.00 USD | `-19.43%` | `38,315.00` |
| `Live` | `Long` | `0.0759` | 75,190.00 USD | 0.00 USD | 142.90 USD | `-19.32%` | `1,884.00` |
| `Live` | `Long` | `0.0761` | 75,040.00 USD | 0.00 USD | 189.82 USD | `-19.11%` | `2,496.00` |
| `Live` | `Long` | `0.0764` | 74,850.00 USD | 0.00 USD | 1,620.00 USD | `-18.79%` | `21,173.00` |
| `Live` | `Long` | `0.0766` | 73,240.00 USD | 0.00 USD | 180.43 USD | `-18.47%` | `2,354.00` |
| `Live` | `Long` | `0.0769` | 73,060.00 USD | 0.00 USD | 333.76 USD | `-18.26%` | `4,343.00` |
| `Live` | `Long` | `0.0770` | 72,720.00 USD | 0.00 USD | 5,050.00 USD | `-18.15%` | `65,640.00` |
| `Live` | `Long` | `0.0775` | 67,670.00 USD | 0.00 USD | 930.06 USD | `-17.51%` | `11,993.00` |
| `Live` | `Long` | `0.0780` | 66,740.00 USD | 0.00 USD | 438.48 USD | `-16.98%` | `5,618.00` |
| `Live` | `Long` | `0.0784` | 66,300.00 USD | 0.00 USD | 3,150.00 USD | `-16.66%` | `40,227.00` |
| `Live` | `Long` | `0.0793` | 63,150.00 USD | 0.00 USD | 309.08 USD | `-15.71%` | `3,900.00` |
| `Live` | `Long` | `0.0799` | 62,840.00 USD | 0.00 USD | 289.02 USD | `-14.96%` | `3,615.00` |
| `Live` | `Long` | `0.0801` | 62,550.00 USD | 0.00 USD | 6,210.00 USD | `-14.75%` | `77,489.00` |
| `Live` | `Long` | `0.0806` | 56,340.00 USD | 0.00 USD | 393.57 USD | `-14.22%` | `4,880.00` |
| `Live` | `Long` | `0.0809` | 55,950.00 USD | 0.00 USD | 487.61 USD | `-14.00%` | `6,031.00` |
| `Live` | `Long` | `0.0809` | 55,460.00 USD | 0.00 USD | 729.68 USD | `-13.90%` | `9,014.00` |
| `Live` | `Long` | `0.0814` | 54,730.00 USD | 0.00 USD | 2,480.00 USD | `-13.37%` | `30,478.00` |
| `Live` | `Long` | `0.0819` | 52,250.00 USD | 0.00 USD | 181.85 USD | `-12.83%` | `2,219.00` |
| `Live` | `Long` | `0.0828` | 52,070.00 USD | 0.00 USD | 1,660.00 USD | `-11.98%` | `20,000.00` |
| `Live` | `Long` | `0.0830` | 50,410.00 USD | 0.00 USD | 1,110.00 USD | `-11.66%` | `13,414.00` |
| `Live` | `Long` | `0.0833` | 49,300.00 USD | 0.00 USD | 335.73 USD | `-11.35%` | `4,028.00` |
| `Live` | `Long` | `0.0835` | 48,960.00 USD | 0.00 USD | 7,980.00 USD | `-11.13%` | `95,507.00` |
| `Live` | `Long` | `0.0838` | 40,980.00 USD | 0.00 USD | 4,570.00 USD | `-10.92%` | `54,577.00` |
| `Live` | `Long` | `0.0839` | 36,410.00 USD | 0.00 USD | 209.88 USD | `-10.71%` | `2,500.00` |
| `Live` | `Long` | `0.0843` | 36,200.00 USD | 0.00 USD | 24,900.00 USD | `-10.28%` | `295,245.00` |
| `Live` | `Long` | `0.0848` | 11,300.00 USD | 0.00 USD | 811.31 USD | `-9.86%` | `9,573.00` |
| `Live` | `Long` | `0.0859` | 10,490.00 USD | 0.00 USD | 2,150.00 USD | `-8.58%` | `25,000.00` |
| `Live` | `Long` | `0.0862` | 8,340.00 USD | 0.00 USD | 1,450.00 USD | `-8.37%` | `16,779.00` |
| `Live` | `Long` | `0.0872` | 6,890.00 USD | 0.00 USD | 223.88 USD | `-7.20%` | `2,566.00` |
| `Live` | `Long` | `0.0877` | 6,670.00 USD | 0.00 USD | 4,750.00 USD | `-6.67%` | `54,098.00` |
| `Live` | `Long` | `0.0882` | 1,920.00 USD | 0.00 USD | 1,080.00 USD | `-6.13%` | `12,280.00` |
| `Live` | `Long` | `0.0886` | 838.07 USD | 0.00 USD | 142.57 USD | `-5.81%` | `1,610.00` |
| `Live` | `Long` | `0.0893` | 695.50 USD | 0.00 USD | 695.50 USD | `-4.96%` | `7,784.00` |
| `Live` | `Short` | `0.1003` | 282.20 USD | 282.20 USD | 0.00 USD | `+6.63%` | `2,815.00` |
| `Live` | `Short` | `0.1003` | 1,640.00 USD | 1,360.00 USD | 0.00 USD | `+6.74%` | `13,577.00` |
| `Live` | `Short` | `0.1007` | 2,190.00 USD | 545.62 USD | 0.00 USD | `+7.06%` | `5,421.00` |
| `Live` | `Short` | `0.1022` | 2,590.00 USD | 402.47 USD | 0.00 USD | `+8.65%` | `3,940.00` |
| `Live` | `Short` | `0.1042` | 2,700.00 USD | 104.88 USD | 0.00 USD | `+10.88%` | `1,006.00` |
| `Live` | `Short` | `0.1045` | 3,390.00 USD | 697.31 USD | 0.00 USD | `+11.10%` | `6,676.00` |
| `Live` | `Short` | `0.1109` | 3,610.00 USD | 217.13 USD | 0.00 USD | `+18.01%` | `1,957.00` |
| `Live` | `Short` | `0.1376` | 6,080.00 USD | 2,460.00 USD | 0.00 USD | `+46.30%` | `17,912.00` |
| `Live` | `Short` | `0.1477` | 6,240.00 USD | 162.97 USD | 0.00 USD | `+57.15%` | `1,103.00` |
| `Live` | `Short` | `0.1689` | 6,530.00 USD | 294.81 USD | 0.00 USD | `+79.60%` | `1,746.00` |

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
  * Current Rate: `-940.54` | Last 24h: `-4.75K` | Last 3d: `-6.09K` | Last 7d: `-6.64K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0035%` | **USDT OKX** | `-0.0212%` |
| **USDT Bybit** | `-0.0029%` | **USDT KuCoin** | `-0.0005%` |
| **USDT MEXC** | `-0.0030%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0151%` | **USDT Bitget** | `0.0100%` |
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
| `5m` | 0.00 USD | -12,410.00 USD | **`DISTRIBUTION`** |
| `15m` | 0.00 USD | 5,130.00 USD | **`ACCUMULATION`** |
| `30m` | 0.00 USD | 62,420.00 USD | **`ACCUMULATION`** |
| `1h` | 0.00 USD | 52,950.00 USD | **`ACCUMULATION`** |
| `2h` | 0.00 USD | 106,160.00 USD | **`ACCUMULATION`** |
| `4h` | 0.00 USD | -489,610.00 USD | **`DISTRIBUTION`** |
| `6h` | 0.00 USD | -578,080.00 USD | **`DISTRIBUTION`** |
| `8h` | 0.00 USD | -1,460,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 0.00 USD | -1,850,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 0.00 USD | -1,610,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 0.00 USD | -3,920,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 0.00 USD | -20,530,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`-12.41K` | 15m=`+5.13K` | 1h=`+52.95K` | 24h=`-1.61M`
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
  * `2026-10-30 09:09:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:28:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:29:56 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0906` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0860` (Risk Distance: `0.0046` pts)
  * +2.5R Take Profit: `0.1022`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0932` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0978` (Risk Distance: `0.0046` pts)
  * +2.5R Take Profit: `0.0816`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0945`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
