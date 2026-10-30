# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ALGUSD
**Canonical Key**: `ALGUSD` | **Broker Instrument**: `ALGUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 07:39:19 IST` (`2026-10-30 02:09:19 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0910` | **Live Ask Quote**: `0.0933` | **Mid Price**: `0.0921`
- **Spread Points**: `23.00` | **Spread BPS**: `249.59 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0973` | VWAP Z-Score: `-1.55` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0011` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `30.30` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1063` | Lower -3.00σ Band: `0.0884`
  * Upper +2.51σ Band: `0.1049` | Lower -2.51σ Band: `0.0898`
  * Upper +2.01σ Band: `0.1034` | Lower -2.01σ Band: `0.0913`
  * Upper +2.00σ Band: `0.1033` | Lower -2.00σ Band: `0.0914`
  * Upper +1.28σ Band: `0.1012` | Lower -1.28σ Band: `0.0935`
  * Upper +1.00σ Band: `0.1003` | Lower -1.00σ Band: `0.0944`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0933` | EMA-20=`0.0947` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0968` (Slope: `+0.0000`) | EMA-100=`0.0983`
  * Institutional Anchors: EMA-144=`0.0990` | EMA-200=`0.0997` (Slope: `-0.8413`) | EMA-233=`0.1001`
- **Range Boundaries**: 24H High=`0.1032` | 24H Low=`0.0911` | Weekly High=`0.1051` | Weekly Low=`0.0911`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0932` (Distance: `-1.21%`)
  * Point of Control (POC) = `0.0926` (Distance: `-0.52%`)
  * Value Area Low (VAL) = `0.0903` (Distance: `+1.96%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.1013` | POC=`0.0982` | VAL=`0.0969`
  * Prior Day Extremes: PDH=`0.1037` | PDL=`0.0911` | PDC=`0.0922`
  * Monday Range Blueprint: High=`0.1046` | Mid=`0.1031` | Low=`0.1015`
  * Developing Weekly Value Area: Weekly VAH=`0.1044` | Weekly POC=`0.1026` | Weekly VAL=`0.0989`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0950` | Low=`0.0881`
  * London Session (08:00-16:00 UTC): High=`0.0925` | Low=`0.0918`
  * New York Session (13:00-21:00 UTC): High=`0.0927` | Low=`0.0916`
  * Initial Balance (First Hour): IB High=`0.0924` | IB Low=`0.0919`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0918` - `0.0925`
  * Optimal Trade Entry (OTE 0.705): `0.0923`
  * Structural Invalidation Anchor (0.786): `0.0929`

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
| `Live` | `Long` | `0.0209` | 194,870.00 USD | 0.00 USD | 3,710.00 USD | `-77.45%` | `177,866.00` |
| `Live` | `Long` | `0.0248` | 191,160.00 USD | 0.00 USD | 347.24 USD | `-73.23%` | `14,030.00` |
| `Live` | `Long` | `0.0293` | 190,810.00 USD | 0.00 USD | 269.60 USD | `-68.36%` | `9,217.00` |
| `Live` | `Long` | `0.0372` | 190,550.00 USD | 0.00 USD | 20,300.00 USD | `-59.81%` | `546,520.00` |
| `Live` | `Long` | `0.0398` | 170,240.00 USD | 0.00 USD | 14,120.00 USD | `-57.00%` | `355,228.00` |
| `Live` | `Long` | `0.0421` | 156,120.00 USD | 0.00 USD | 3,680.00 USD | `-54.40%` | `87,382.00` |
| `Live` | `Long` | `0.0450` | 152,440.00 USD | 0.00 USD | 369.32 USD | `-51.27%` | `8,198.00` |
| `Live` | `Long` | `0.0454` | 152,070.00 USD | 0.00 USD | 1,900.00 USD | `-50.94%` | `41,853.00` |
| `Live` | `Long` | `0.0461` | 150,170.00 USD | 0.00 USD | 145.00 USD | `-50.08%` | `3,142.00` |
| `Live` | `Long` | `0.0478` | 150,030.00 USD | 0.00 USD | 5,910.00 USD | `-48.35%` | `123,747.00` |
| `Live` | `Long` | `0.0496` | 144,120.00 USD | 0.00 USD | 267.76 USD | `-46.29%` | `5,393.00` |
| `Live` | `Long` | `0.0505` | 143,850.00 USD | 0.00 USD | 2,490.00 USD | `-45.43%` | `49,368.00` |
| `Live` | `Long` | `0.0508` | 141,360.00 USD | 0.00 USD | 506.59 USD | `-45.10%` | `9,982.00` |
| `Live` | `Long` | `0.0515` | 140,850.00 USD | 0.00 USD | 2,480.00 USD | `-44.34%` | `48,218.00` |
| `Live` | `Long` | `0.0546` | 138,370.00 USD | 0.00 USD | 319.81 USD | `-40.88%` | `5,852.00` |
| `Live` | `Long` | `0.0551` | 138,050.00 USD | 0.00 USD | 5,830.00 USD | `-40.34%` | `105,702.00` |
| `Live` | `Long` | `0.0588` | 132,220.00 USD | 0.00 USD | 111.76 USD | `-36.34%` | `1,899.00` |
| `Live` | `Long` | `0.0599` | 132,110.00 USD | 0.00 USD | 441.33 USD | `-35.26%` | `7,374.00` |
| `Live` | `Long` | `0.0607` | 131,670.00 USD | 0.00 USD | 223.26 USD | `-34.28%` | `3,675.00` |
| `Live` | `Long` | `0.0614` | 131,450.00 USD | 0.00 USD | 1,630.00 USD | `-33.53%` | `26,498.00` |
| `Live` | `Long` | `0.0621` | 129,820.00 USD | 0.00 USD | 260.91 USD | `-32.77%` | `4,198.00` |
| `Live` | `Long` | `0.0625` | 129,560.00 USD | 0.00 USD | 180.46 USD | `-32.34%` | `2,885.00` |
| `Live` | `Long` | `0.0634` | 129,380.00 USD | 0.00 USD | 167.24 USD | `-31.47%` | `2,640.00` |
| `Live` | `Long` | `0.0636` | 129,210.00 USD | 0.00 USD | 525.94 USD | `-31.15%` | `8,263.00` |
| `Live` | `Long` | `0.0654` | 128,680.00 USD | 0.00 USD | 13,390.00 USD | `-29.31%` | `204,927.00` |
| `Live` | `Long` | `0.0655` | 115,290.00 USD | 0.00 USD | 3,500.00 USD | `-29.09%` | `53,418.00` |
| `Live` | `Long` | `0.0659` | 111,790.00 USD | 0.00 USD | 3,960.00 USD | `-28.66%` | `60,000.00` |
| `Live` | `Long` | `0.0663` | 107,830.00 USD | 0.00 USD | 5,600.00 USD | `-28.33%` | `84,534.00` |
| `Live` | `Long` | `0.0674` | 102,230.00 USD | 0.00 USD | 208.83 USD | `-27.04%` | `3,096.00` |
| `Live` | `Long` | `0.0693` | 102,020.00 USD | 0.00 USD | 919.79 USD | `-24.98%` | `13,263.00` |
| `Live` | `Long` | `0.0694` | 101,100.00 USD | 0.00 USD | 266.20 USD | `-24.87%` | `3,833.00` |
| `Live` | `Long` | `0.0698` | 100,840.00 USD | 0.00 USD | 165.31 USD | `-24.55%` | `2,370.00` |
| `Live` | `Long` | `0.0717` | 100,670.00 USD | 0.00 USD | 224.98 USD | `-22.49%` | `3,140.00` |
| `Live` | `Long` | `0.0720` | 100,450.00 USD | 0.00 USD | 7,110.00 USD | `-22.17%` | `98,791.00` |
| `Live` | `Long` | `0.0721` | 93,340.00 USD | 0.00 USD | 347.79 USD | `-22.06%` | `4,827.00` |
| `Live` | `Long` | `0.0727` | 92,990.00 USD | 0.00 USD | 918.15 USD | `-21.41%` | `12,638.00` |
| `Live` | `Long` | `0.0728` | 92,070.00 USD | 0.00 USD | 388.00 USD | `-21.20%` | `5,326.00` |
| `Live` | `Long` | `0.0730` | 91,680.00 USD | 0.00 USD | 933.91 USD | `-21.09%` | `12,802.00` |
| `Live` | `Long` | `0.0731` | 90,750.00 USD | 0.00 USD | 1,210.00 USD | `-20.98%` | `16,582.00` |
| `Live` | `Long` | `0.0732` | 89,540.00 USD | 0.00 USD | 1,020.00 USD | `-20.76%` | `13,863.00` |
| `Live` | `Long` | `0.0735` | 88,520.00 USD | 0.00 USD | 1,840.00 USD | `-20.55%` | `25,026.00` |
| `Live` | `Long` | `0.0736` | 86,690.00 USD | 0.00 USD | 444.48 USD | `-20.33%` | `6,035.00` |
| `Live` | `Long` | `0.0741` | 86,240.00 USD | 0.00 USD | 741.50 USD | `-19.79%` | `10,000.00` |
| `Live` | `Long` | `0.0742` | 85,500.00 USD | 0.00 USD | 174.34 USD | `-19.68%` | `2,348.00` |
| `Live` | `Long` | `0.0751` | 85,330.00 USD | 0.00 USD | 475.62 USD | `-18.71%` | `6,329.00` |
| `Live` | `Long` | `0.0752` | 84,850.00 USD | 0.00 USD | 299.65 USD | `-18.60%` | `3,982.00` |
| `Live` | `Long` | `0.0754` | 84,550.00 USD | 0.00 USD | 557.29 USD | `-18.49%` | `7,396.00` |
| `Live` | `Long` | `0.0755` | 83,990.00 USD | 0.00 USD | 1,250.00 USD | `-18.38%` | `16,502.00` |
| `Live` | `Long` | `0.0756` | 82,750.00 USD | 0.00 USD | 361.66 USD | `-18.27%` | `4,787.00` |
| `Live` | `Long` | `0.0756` | 82,390.00 USD | 0.00 USD | 4,630.00 USD | `-18.17%` | `61,227.00` |
| `Live` | `Long` | `0.0757` | 77,750.00 USD | 0.00 USD | 2,900.00 USD | `-18.06%` | `38,315.00` |
| `Live` | `Long` | `0.0759` | 74,850.00 USD | 0.00 USD | 142.90 USD | `-17.95%` | `1,884.00` |
| `Live` | `Long` | `0.0761` | 74,710.00 USD | 0.00 USD | 189.82 USD | `-17.73%` | `2,496.00` |
| `Live` | `Long` | `0.0764` | 74,520.00 USD | 0.00 USD | 1,620.00 USD | `-17.41%` | `21,173.00` |
| `Live` | `Long` | `0.0766` | 72,900.00 USD | 0.00 USD | 180.43 USD | `-17.08%` | `2,354.00` |
| `Live` | `Long` | `0.0770` | 72,720.00 USD | 0.00 USD | 5,050.00 USD | `-16.76%` | `65,640.00` |
| `Live` | `Long` | `0.0775` | 67,670.00 USD | 0.00 USD | 930.06 USD | `-16.11%` | `11,993.00` |
| `Live` | `Long` | `0.0780` | 66,740.00 USD | 0.00 USD | 438.48 USD | `-15.57%` | `5,618.00` |
| `Live` | `Long` | `0.0784` | 66,300.00 USD | 0.00 USD | 3,150.00 USD | `-15.25%` | `40,227.00` |
| `Live` | `Long` | `0.0793` | 63,150.00 USD | 0.00 USD | 309.08 USD | `-14.27%` | `3,900.00` |
| `Live` | `Long` | `0.0799` | 62,840.00 USD | 0.00 USD | 289.02 USD | `-13.52%` | `3,615.00` |
| `Live` | `Long` | `0.0801` | 62,550.00 USD | 0.00 USD | 6,210.00 USD | `-13.30%` | `77,489.00` |
| `Live` | `Long` | `0.0806` | 56,340.00 USD | 0.00 USD | 393.57 USD | `-12.76%` | `4,880.00` |
| `Live` | `Long` | `0.0809` | 55,950.00 USD | 0.00 USD | 487.61 USD | `-12.54%` | `6,031.00` |
| `Live` | `Long` | `0.0809` | 55,460.00 USD | 0.00 USD | 729.68 USD | `-12.43%` | `9,014.00` |
| `Live` | `Long` | `0.0814` | 54,730.00 USD | 0.00 USD | 2,480.00 USD | `-11.89%` | `30,478.00` |
| `Live` | `Long` | `0.0819` | 52,250.00 USD | 0.00 USD | 181.85 USD | `-11.35%` | `2,219.00` |
| `Live` | `Long` | `0.0828` | 52,070.00 USD | 0.00 USD | 1,660.00 USD | `-10.49%` | `20,000.00` |
| `Live` | `Long` | `0.0830` | 50,410.00 USD | 0.00 USD | 1,110.00 USD | `-10.16%` | `13,414.00` |
| `Live` | `Long` | `0.0833` | 49,300.00 USD | 0.00 USD | 335.73 USD | `-9.84%` | `4,028.00` |
| `Live` | `Long` | `0.0835` | 48,960.00 USD | 0.00 USD | 7,980.00 USD | `-9.62%` | `95,507.00` |
| `Live` | `Long` | `0.0838` | 40,980.00 USD | 0.00 USD | 4,570.00 USD | `-9.40%` | `54,577.00` |
| `Live` | `Long` | `0.0839` | 36,410.00 USD | 0.00 USD | 209.88 USD | `-9.19%` | `2,500.00` |
| `Live` | `Long` | `0.0843` | 36,200.00 USD | 0.00 USD | 24,900.00 USD | `-8.76%` | `295,245.00` |
| `Live` | `Long` | `0.0848` | 11,300.00 USD | 0.00 USD | 811.31 USD | `-8.32%` | `9,573.00` |
| `Live` | `Long` | `0.0859` | 10,490.00 USD | 0.00 USD | 2,150.00 USD | `-7.02%` | `25,000.00` |
| `Live` | `Long` | `0.0862` | 8,340.00 USD | 0.00 USD | 1,450.00 USD | `-6.81%` | `16,779.00` |
| `Live` | `Long` | `0.0872` | 6,890.00 USD | 0.00 USD | 223.88 USD | `-5.62%` | `2,566.00` |
| `Live` | `Long` | `0.0877` | 6,670.00 USD | 0.00 USD | 4,750.00 USD | `-5.08%` | `54,098.00` |
| `Live` | `Long` | `0.0882` | 1,920.00 USD | 0.00 USD | 1,080.00 USD | `-4.54%` | `12,280.00` |
| `Live` | `Long` | `0.0886` | 838.07 USD | 0.00 USD | 142.57 USD | `-4.21%` | `1,610.00` |
| `Live` | `Long` | `0.0893` | 695.50 USD | 0.00 USD | 695.50 USD | `-3.35%` | `7,784.00` |
| `Live` | `Short` | `0.1022` | 402.47 USD | 402.47 USD | 0.00 USD | `+10.50%` | `3,940.00` |
| `Live` | `Short` | `0.1109` | 619.60 USD | 217.13 USD | 0.00 USD | `+20.02%` | `1,957.00` |
| `Live` | `Short` | `0.1351` | 3,040.00 USD | 2,420.00 USD | 0.00 USD | `+46.09%` | `17,912.00` |
| `Live` | `Short` | `0.1477` | 3,200.00 USD | 162.97 USD | 0.00 USD | `+59.83%` | `1,103.00` |
| `Live` | `Short` | `0.1689` | 3,500.00 USD | 294.81 USD | 0.00 USD | `+82.65%` | `1,746.00` |

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
  * Current Rate: `-1.14K` | Last 24h: `-4.75K` | Last 3d: `-6.09K` | Last 7d: `-6.64K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0077%` | **USDT OKX** | `-0.0055%` |
| **USDT Bybit** | `-0.0041%` | **USDT KuCoin** | `0.0008%` |
| **USDT MEXC** | `-0.0080%` | **USDT BingX** | `0.0100%` |
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
| `5m` | 4,850.00 USD | -7,840.00 USD | **`DISTRIBUTION`** |
| `15m` | -3,340.00 USD | -34,530.00 USD | **`DISTRIBUTION`** |
| `30m` | -21,460.00 USD | -61,870.00 USD | **`DISTRIBUTION`** |
| `1h` | -52,940.00 USD | -96,890.00 USD | **`DISTRIBUTION`** |
| `2h` | -369,340.00 USD | -554,800.00 USD | **`DISTRIBUTION`** |
| `4h` | -406,980.00 USD | -673,610.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,090,000.00 USD | -1,590,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,090,000.00 USD | -1,740,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,140,000.00 USD | -1,980,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,150,000.00 USD | -2,120,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -2,560,000.00 USD | -4,020,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -13,900,000.00 USD | -21,080,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+4.85K` | 15m=`-3.34K` | 1h=`-52.94K` | 24h=`-1.15M`
* Futures Capital Netflows: 5m=`-7.84K` | 15m=`-34.53K` | 1h=`-96.89K` | 24h=`-2.12M`
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
  * Execution Entry: `0.0903` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0855` (Risk Distance: `0.0048` pts)
  * +2.5R Take Profit: `0.1023`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0932` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0980` (Risk Distance: `0.0048` pts)
  * +2.5R Take Profit: `0.0812`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0929`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
