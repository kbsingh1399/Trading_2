# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ALGUSD
**Canonical Key**: `ALGUSD` | **Broker Instrument**: `ALGUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 14:47:51 IST` (`2026-10-30 09:17:51 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0933` | **Live Ask Quote**: `0.0956` | **Mid Price**: `0.0945`
- **Spread Points**: `23.00` | **Spread BPS**: `243.52 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0919` | VWAP Z-Score: `+0.82` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000681` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `46.13` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0966` | Lower -3.00σ Band: `0.0873`
  * Upper +2.51σ Band: `0.0958` | Lower -2.51σ Band: `0.0880`
  * Upper +2.01σ Band: `0.0950` | Lower -2.01σ Band: `0.0888`
  * Upper +2.00σ Band: `0.0950` | Lower -2.00σ Band: `0.0888`
  * Upper +1.28σ Band: `0.0939` | Lower -1.28σ Band: `0.0899`
  * Upper +1.00σ Band: `0.0935` | Lower -1.00σ Band: `0.0904`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0937` | EMA-20=`0.0936` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0940` (Slope: `+0.0000`) | EMA-100=`0.0955`
  * Institutional Anchors: EMA-144=`0.0965` | EMA-200=`0.0976` (Slope: `-0.4698`) | EMA-233=`0.0982`
- **Range Boundaries**: 24H High=`0.1024` | 24H Low=`0.0881` | Weekly High=`0.1048` | Weekly Low=`0.0881`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0941` (Distance: `+0.43%`)
  * Point of Control (POC) = `0.0926` (Distance: `+1.99%`)
  * Value Area Low (VAL) = `0.0908` (Distance: `+4.04%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.1013` | POC=`0.0982` | VAL=`0.0969`
  * Prior Day Extremes: PDH=`0.1037` | PDL=`0.0911` | PDC=`0.0922`
  * Monday Range Blueprint: High=`0.1046` | Mid=`0.1031` | Low=`0.1015`
  * Developing Weekly Value Area: Weekly VAH=`0.1044` | Weekly POC=`0.1026` | Weekly VAL=`0.0980`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0950` | Low=`0.0881`
  * London Session (08:00-16:00 UTC): High=`0.0951` | Low=`0.0930`
  * New York Session (13:00-21:00 UTC): High=`0.0950` | Low=`0.0939`
  * Initial Balance (First Hour): IB High=`0.0945` | IB Low=`0.0933`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0941` - `0.0948`
  * Optimal Trade Entry (OTE 0.705): `0.0946`
  * Structural Invalidation Anchor (0.786): `0.0952`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:43:12 IST` |

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
| `Live` | `Long Liquidation` | `0.0209` | 3,710.00 USD | 176,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0225` | 314.97 USD | 173,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0309` | 17,860.00 USD | 172,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0353` | 289.80 USD | 155,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0355` | 1,720.00 USD | 154,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0421` | 3,680.00 USD | 153,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 1,780.00 USD | 149,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0435` | 136.83 USD | 147,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0471` | 2,320.00 USD | 147,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0473` | 5,850.00 USD | 145,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 17,570.00 USD | 139,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0496` | 267.76 USD | 121,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 506.59 USD | 121,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0537` | 2,890.00 USD | 120,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 319.81 USD | 118,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0551` | 5,830.00 USD | 117,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0588` | 111.76 USD | 111,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 580.83 USD | 111,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 441.33 USD | 111,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 8,270.00 USD | 110,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 223.26 USD | 102,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 293.68 USD | 102,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 1,630.00 USD | 102,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 260.91 USD | 100,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 180.46 USD | 100,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 167.24 USD | 99,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 525.94 USD | 99,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0654` | 13,390.00 USD | 99,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 3,960.00 USD | 85,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0663` | 5,600.00 USD | 81,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 208.52 USD | 76,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0693` | 919.79 USD | 76,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0694` | 155.50 USD | 75,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0697` | 165.07 USD | 75,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0707` | 176.62 USD | 74,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0717` | 224.98 USD | 74,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0720` | 7,110.00 USD | 74,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0721` | 347.79 USD | 67,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0727` | 918.15 USD | 67,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0728` | 1,320.00 USD | 66,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0732` | 1,020.00 USD | 64,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 1,120.00 USD | 63,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0736` | 444.48 USD | 62,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0741` | 741.50 USD | 62,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0742` | 174.34 USD | 61,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0751` | 474.99 USD | 61,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0752` | 299.65 USD | 60,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0754` | 557.29 USD | 60,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 1,250.00 USD | 59,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0756` | 4,630.00 USD | 58,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0757` | 2,900.00 USD | 54,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0759` | 142.90 USD | 51,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0761` | 189.82 USD | 51,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0764` | 1,620.00 USD | 50,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0766` | 180.43 USD | 49,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0770` | 5,050.00 USD | 49,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 930.06 USD | 43,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0780` | 438.48 USD | 43,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0784` | 3,150.00 USD | 42,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0793` | 309.08 USD | 39,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0799` | 289.02 USD | 39,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0801` | 6,210.00 USD | 38,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0806` | 393.57 USD | 32,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0809` | 487.61 USD | 32,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0809` | 729.68 USD | 31,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0814` | 2,480.00 USD | 31,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0819` | 181.85 USD | 28,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0828` | 1,660.00 USD | 28,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0830` | 1,110.00 USD | 26,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0833` | 335.73 USD | 25,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 8,540.00 USD | 25,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0838` | 4,570.00 USD | 16,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0842` | 445.07 USD | 12,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0848` | 811.31 USD | 11,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0859` | 2,150.00 USD | 10,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0862` | 1,450.00 USD | 8,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0872` | 223.88 USD | 7,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0877` | 4,750.00 USD | 7,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0882` | 221.24 USD | 2,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0893` | 695.50 USD | 2,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0941` | 1,420.00 USD | 1,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1003` | 178.95 USD | 178.95 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1006` | 545.08 USD | 724.03 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1021` | 402.08 USD | 1,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1051` | 995.66 USD | 2,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1109` | 217.13 USD | 2,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1378` | 2,470.00 USD | 4,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1477` | 162.97 USD | 4,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1689` | 294.81 USD | 5,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1830` | 1,930.00 USD | 7,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0209` | 176,980.00 USD | 0.00 USD | 3,710.00 USD | `-77.88%` | `177,866.00` |
| `Live` | `Long` | `0.0225` | 173,270.00 USD | 0.00 USD | 314.97 USD | `-76.18%` | `14,030.00` |
| `Live` | `Long` | `0.0309` | 172,950.00 USD | 0.00 USD | 17,860.00 USD | `-67.16%` | `576,930.00` |
| `Live` | `Long` | `0.0353` | 155,100.00 USD | 0.00 USD | 289.80 USD | `-62.49%` | `8,198.00` |
| `Live` | `Long` | `0.0355` | 154,810.00 USD | 0.00 USD | 1,720.00 USD | `-62.28%` | `48,295.00` |
| `Live` | `Long` | `0.0421` | 153,090.00 USD | 0.00 USD | 3,680.00 USD | `-55.28%` | `87,382.00` |
| `Live` | `Long` | `0.0425` | 149,410.00 USD | 0.00 USD | 1,780.00 USD | `-54.85%` | `41,853.00` |
| `Live` | `Long` | `0.0435` | 147,630.00 USD | 0.00 USD | 136.83 USD | `-53.79%` | `3,142.00` |
| `Live` | `Long` | `0.0471` | 147,490.00 USD | 0.00 USD | 2,320.00 USD | `-50.08%` | `49,368.00` |
| `Live` | `Long` | `0.0473` | 145,170.00 USD | 0.00 USD | 5,850.00 USD | `-49.87%` | `123,747.00` |
| `Live` | `Long` | `0.0495` | 139,320.00 USD | 0.00 USD | 17,570.00 USD | `-47.53%` | `355,228.00` |
| `Live` | `Long` | `0.0496` | 121,750.00 USD | 0.00 USD | 267.76 USD | `-47.32%` | `5,393.00` |
| `Live` | `Long` | `0.0508` | 121,490.00 USD | 0.00 USD | 506.59 USD | `-46.15%` | `9,982.00` |
| `Live` | `Long` | `0.0537` | 120,980.00 USD | 0.00 USD | 2,890.00 USD | `-43.08%` | `53,784.00` |
| `Live` | `Long` | `0.0546` | 118,090.00 USD | 0.00 USD | 319.81 USD | `-42.02%` | `5,852.00` |
| `Live` | `Long` | `0.0551` | 117,780.00 USD | 0.00 USD | 5,830.00 USD | `-41.49%` | `105,702.00` |
| `Live` | `Long` | `0.0588` | 111,950.00 USD | 0.00 USD | 111.76 USD | `-37.56%` | `1,899.00` |
| `Live` | `Long` | `0.0595` | 111,830.00 USD | 0.00 USD | 580.83 USD | `-36.92%` | `9,770.00` |
| `Live` | `Long` | `0.0599` | 111,250.00 USD | 0.00 USD | 441.33 USD | `-36.50%` | `7,374.00` |
| `Live` | `Long` | `0.0605` | 110,810.00 USD | 0.00 USD | 8,270.00 USD | `-35.76%` | `136,663.00` |
| `Live` | `Long` | `0.0607` | 102,540.00 USD | 0.00 USD | 223.26 USD | `-35.54%` | `3,675.00` |
| `Live` | `Long` | `0.0614` | 102,310.00 USD | 0.00 USD | 293.68 USD | `-34.91%` | `4,787.00` |
| `Live` | `Long` | `0.0614` | 102,020.00 USD | 0.00 USD | 1,630.00 USD | `-34.80%` | `26,498.00` |
| `Live` | `Long` | `0.0621` | 100,390.00 USD | 0.00 USD | 260.91 USD | `-34.06%` | `4,198.00` |
| `Live` | `Long` | `0.0625` | 100,130.00 USD | 0.00 USD | 180.46 USD | `-33.63%` | `2,885.00` |
| `Live` | `Long` | `0.0634` | 99,950.00 USD | 0.00 USD | 167.24 USD | `-32.79%` | `2,640.00` |
| `Live` | `Long` | `0.0636` | 99,780.00 USD | 0.00 USD | 525.94 USD | `-32.47%` | `8,263.00` |
| `Live` | `Long` | `0.0654` | 99,260.00 USD | 0.00 USD | 13,390.00 USD | `-30.66%` | `204,927.00` |
| `Live` | `Long` | `0.0659` | 85,860.00 USD | 0.00 USD | 3,960.00 USD | `-30.03%` | `60,000.00` |
| `Live` | `Long` | `0.0663` | 81,910.00 USD | 0.00 USD | 5,600.00 USD | `-29.71%` | `84,534.00` |
| `Live` | `Long` | `0.0673` | 76,310.00 USD | 0.00 USD | 208.52 USD | `-28.54%` | `3,096.00` |
| `Live` | `Long` | `0.0693` | 76,100.00 USD | 0.00 USD | 919.79 USD | `-26.42%` | `13,263.00` |
| `Live` | `Long` | `0.0694` | 75,180.00 USD | 0.00 USD | 155.50 USD | `-26.31%` | `2,239.00` |
| `Live` | `Long` | `0.0697` | 75,020.00 USD | 0.00 USD | 165.07 USD | `-26.10%` | `2,370.00` |
| `Live` | `Long` | `0.0707` | 74,860.00 USD | 0.00 USD | 176.62 USD | `-25.04%` | `2,500.00` |
| `Live` | `Long` | `0.0717` | 74,680.00 USD | 0.00 USD | 224.98 USD | `-23.98%` | `3,140.00` |
| `Live` | `Long` | `0.0720` | 74,460.00 USD | 0.00 USD | 7,110.00 USD | `-23.66%` | `98,791.00` |
| `Live` | `Long` | `0.0721` | 67,350.00 USD | 0.00 USD | 347.79 USD | `-23.56%` | `4,827.00` |
| `Live` | `Long` | `0.0727` | 67,000.00 USD | 0.00 USD | 918.15 USD | `-22.92%` | `12,638.00` |
| `Live` | `Long` | `0.0728` | 66,080.00 USD | 0.00 USD | 1,320.00 USD | `-22.71%` | `18,128.00` |
| `Live` | `Long` | `0.0732` | 64,760.00 USD | 0.00 USD | 1,020.00 USD | `-22.28%` | `13,863.00` |
| `Live` | `Long` | `0.0735` | 63,750.00 USD | 0.00 USD | 1,120.00 USD | `-22.07%` | `15,256.00` |
| `Live` | `Long` | `0.0736` | 62,630.00 USD | 0.00 USD | 444.48 USD | `-21.86%` | `6,035.00` |
| `Live` | `Long` | `0.0741` | 62,180.00 USD | 0.00 USD | 741.50 USD | `-21.33%` | `10,000.00` |
| `Live` | `Long` | `0.0742` | 61,440.00 USD | 0.00 USD | 174.34 USD | `-21.22%` | `2,348.00` |
| `Live` | `Long` | `0.0751` | 61,270.00 USD | 0.00 USD | 474.99 USD | `-20.37%` | `6,329.00` |
| `Live` | `Long` | `0.0752` | 60,790.00 USD | 0.00 USD | 299.65 USD | `-20.16%` | `3,982.00` |
| `Live` | `Long` | `0.0754` | 60,490.00 USD | 0.00 USD | 557.29 USD | `-20.05%` | `7,396.00` |
| `Live` | `Long` | `0.0755` | 59,930.00 USD | 0.00 USD | 1,250.00 USD | `-19.95%` | `16,502.00` |
| `Live` | `Long` | `0.0756` | 58,690.00 USD | 0.00 USD | 4,630.00 USD | `-19.74%` | `61,227.00` |
| `Live` | `Long` | `0.0757` | 54,060.00 USD | 0.00 USD | 2,900.00 USD | `-19.63%` | `38,315.00` |
| `Live` | `Long` | `0.0759` | 51,160.00 USD | 0.00 USD | 142.90 USD | `-19.52%` | `1,884.00` |
| `Live` | `Long` | `0.0761` | 51,010.00 USD | 0.00 USD | 189.82 USD | `-19.31%` | `2,496.00` |
| `Live` | `Long` | `0.0764` | 50,820.00 USD | 0.00 USD | 1,620.00 USD | `-18.99%` | `21,173.00` |
| `Live` | `Long` | `0.0766` | 49,210.00 USD | 0.00 USD | 180.43 USD | `-18.67%` | `2,354.00` |
| `Live` | `Long` | `0.0770` | 49,030.00 USD | 0.00 USD | 5,050.00 USD | `-18.36%` | `65,640.00` |
| `Live` | `Long` | `0.0775` | 43,970.00 USD | 0.00 USD | 930.06 USD | `-17.72%` | `11,993.00` |
| `Live` | `Long` | `0.0780` | 43,040.00 USD | 0.00 USD | 438.48 USD | `-17.19%` | `5,618.00` |
| `Live` | `Long` | `0.0784` | 42,610.00 USD | 0.00 USD | 3,150.00 USD | `-16.87%` | `40,227.00` |
| `Live` | `Long` | `0.0793` | 39,450.00 USD | 0.00 USD | 309.08 USD | `-15.92%` | `3,900.00` |
| `Live` | `Long` | `0.0799` | 39,140.00 USD | 0.00 USD | 289.02 USD | `-15.17%` | `3,615.00` |
| `Live` | `Long` | `0.0801` | 38,860.00 USD | 0.00 USD | 6,210.00 USD | `-14.96%` | `77,489.00` |
| `Live` | `Long` | `0.0806` | 32,650.00 USD | 0.00 USD | 393.57 USD | `-14.43%` | `4,880.00` |
| `Live` | `Long` | `0.0809` | 32,250.00 USD | 0.00 USD | 487.61 USD | `-14.22%` | `6,031.00` |
| `Live` | `Long` | `0.0809` | 31,760.00 USD | 0.00 USD | 729.68 USD | `-14.11%` | `9,014.00` |
| `Live` | `Long` | `0.0814` | 31,030.00 USD | 0.00 USD | 2,480.00 USD | `-13.58%` | `30,478.00` |
| `Live` | `Long` | `0.0819` | 28,550.00 USD | 0.00 USD | 181.85 USD | `-13.05%` | `2,219.00` |
| `Live` | `Long` | `0.0828` | 28,370.00 USD | 0.00 USD | 1,660.00 USD | `-12.20%` | `20,000.00` |
| `Live` | `Long` | `0.0830` | 26,720.00 USD | 0.00 USD | 1,110.00 USD | `-11.88%` | `13,414.00` |
| `Live` | `Long` | `0.0833` | 25,600.00 USD | 0.00 USD | 335.73 USD | `-11.57%` | `4,028.00` |
| `Live` | `Long` | `0.0835` | 25,270.00 USD | 0.00 USD | 8,540.00 USD | `-11.35%` | `102,183.00` |
| `Live` | `Long` | `0.0838` | 16,730.00 USD | 0.00 USD | 4,570.00 USD | `-11.14%` | `54,577.00` |
| `Live` | `Long` | `0.0842` | 12,160.00 USD | 0.00 USD | 445.07 USD | `-10.72%` | `5,289.00` |
| `Live` | `Long` | `0.0848` | 11,710.00 USD | 0.00 USD | 811.31 USD | `-10.08%` | `9,573.00` |
| `Live` | `Long` | `0.0859` | 10,900.00 USD | 0.00 USD | 2,150.00 USD | `-8.81%` | `25,000.00` |
| `Live` | `Long` | `0.0862` | 8,750.00 USD | 0.00 USD | 1,450.00 USD | `-8.60%` | `16,779.00` |
| `Live` | `Long` | `0.0872` | 7,310.00 USD | 0.00 USD | 223.88 USD | `-7.43%` | `2,566.00` |
| `Live` | `Long` | `0.0877` | 7,080.00 USD | 0.00 USD | 4,750.00 USD | `-6.90%` | `54,098.00` |
| `Live` | `Long` | `0.0882` | 2,340.00 USD | 0.00 USD | 221.24 USD | `-6.37%` | `2,507.00` |
| `Live` | `Long` | `0.0893` | 2,110.00 USD | 0.00 USD | 695.50 USD | `-5.20%` | `7,784.00` |
| `Live` | `Long` | `0.0941` | 1,420.00 USD | 0.00 USD | 1,420.00 USD | `-0.11%` | `15,068.00` |
| `Live` | `Short` | `0.1003` | 178.95 USD | 178.95 USD | 0.00 USD | `+6.36%` | `1,785.00` |
| `Live` | `Short` | `0.1006` | 724.03 USD | 545.08 USD | 0.00 USD | `+6.68%` | `5,421.00` |
| `Live` | `Short` | `0.1021` | 1,130.00 USD | 402.08 USD | 0.00 USD | `+8.27%` | `3,940.00` |
| `Live` | `Short` | `0.1051` | 2,120.00 USD | 995.66 USD | 0.00 USD | `+11.46%` | `9,478.00` |
| `Live` | `Short` | `0.1109` | 2,340.00 USD | 217.13 USD | 0.00 USD | `+17.72%` | `1,957.00` |
| `Live` | `Short` | `0.1378` | 4,810.00 USD | 2,470.00 USD | 0.00 USD | `+46.15%` | `17,912.00` |
| `Live` | `Short` | `0.1477` | 4,970.00 USD | 162.97 USD | 0.00 USD | `+56.76%` | `1,103.00` |
| `Live` | `Short` | `0.1689` | 5,260.00 USD | 294.81 USD | 0.00 USD | `+79.15%` | `1,746.00` |
| `Live` | `Short` | `0.1830` | 7,190.00 USD | 1,930.00 USD | 0.00 USD | `+94.22%` | `10,520.00` |

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
  * Current Rate: `-884.68` | Last 24h: `-2.41K` | Last 3d: `-9.10K` | Last 7d: `-8.18K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0092%` | **USDT OKX** | `-0.0332%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0090%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0052%` |
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
| `5m` | -2,660.00 USD | -3,900.00 USD | **`DISTRIBUTION`** |
| `15m` | 18,920.00 USD | -28,190.00 USD | **`DISTRIBUTION`** |
| `30m` | -21,620.00 USD | 35,220.00 USD | **`ACCUMULATION`** |
| `1h` | -6,090.00 USD | 60,100.00 USD | **`ACCUMULATION`** |
| `2h` | -84,830.00 USD | 36,140.00 USD | **`DISTRIBUTION`** |
| `4h` | -110,080.00 USD | 18,760.00 USD | **`DISTRIBUTION`** |
| `6h` | -50,720.00 USD | 43,450.00 USD | **`DISTRIBUTION`** |
| `8h` | -105,950.00 USD | -559,810.00 USD | **`DISTRIBUTION`** |
| `12h` | -480,640.00 USD | -726,710.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,190,000.00 USD | -2,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -2,560,000.00 USD | -3,790,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,040,000.00 USD | -20,640,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-2.66K` | 15m=`+18.92K` | 1h=`-6.09K` | 24h=`-1.19M`
* Futures Capital Netflows: 5m=`-3.90K` | 15m=`-28.19K` | 1h=`+60.10K` | 24h=`-2.00M`
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
  * `2026-10-30 14:37:38 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:38 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:32:38 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 14:09:38 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:52:38 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:38 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:37:38 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:37:38 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0908` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0865` (Risk Distance: `0.0046` pts)
  * +2.5R Take Profit: `0.1023`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0941` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0984` (Risk Distance: `0.0046` pts)
  * +2.5R Take Profit: `0.0826`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0952`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
