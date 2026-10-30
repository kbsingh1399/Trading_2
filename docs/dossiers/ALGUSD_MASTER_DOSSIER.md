# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ALGUSD
**Canonical Key**: `ALGUSD` | **Broker Instrument**: `ALGUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 16:33:46 IST` (`2026-10-30 11:03:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0946` | **Live Ask Quote**: `0.0968` | **Mid Price**: `0.0957`
- **Spread Points**: `22.00` | **Spread BPS**: `229.89 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0957` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0964` | Lower -3.00σ Band: `0.0950`
  * Upper +2.51σ Band: `0.0962` | Lower -2.51σ Band: `0.0952`
  * Upper +2.01σ Band: `0.0961` | Lower -2.01σ Band: `0.0953`
  * Upper +2.00σ Band: `0.0961` | Lower -2.00σ Band: `0.0953`
  * Upper +1.28σ Band: `0.0960` | Lower -1.28σ Band: `0.0954`
  * Upper +1.00σ Band: `0.0959` | Lower -1.00σ Band: `0.0955`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0957` | EMA-20=`0.0957` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0957` (Slope: `+0.0000`) | EMA-100=`0.0957`
  * Institutional Anchors: EMA-144=`0.0957` | EMA-200=`0.0957` (Slope: `+0.0000`) | EMA-233=`0.0957`
- **Range Boundaries**: 24H High=`0.0967` | 24H Low=`0.0947` | Weekly High=`0.0976` | Weekly Low=`0.0938`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0946` (Distance: `+1.15%`)
  * Point of Control (POC) = `0.0930` (Distance: `+2.88%`)
  * Value Area Low (VAL) = `0.0914` (Distance: `+4.66%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.1013` | POC=`0.0982` | VAL=`0.0969`
  * Prior Day Extremes: PDH=`0.1037` | PDL=`0.0911` | PDC=`0.0922`
  * Monday Range Blueprint: High=`0.1046` | Mid=`0.1031` | Low=`0.1015`
  * Developing Weekly Value Area: Weekly VAH=`0.1044` | Weekly POC=`0.1026` | Weekly VAL=`0.0979`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0950` | Low=`0.0881`
  * London Session (08:00-16:00 UTC): High=`0.0951` | Low=`0.0929`
  * New York Session (13:00-21:00 UTC): High=`0.0948` | Low=`0.0937`
  * Initial Balance (First Hour): IB High=`0.0945` | IB Low=`0.0933`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0953` - `0.0961`
  * Optimal Trade Entry (OTE 0.705): `0.0959`
  * Structural Invalidation Anchor (0.786): `0.0965`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:32:44 IST` |

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
| `Live` | `Long Liquidation` | `0.0209` | 3,710.00 USD | 184,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0225` | 314.97 USD | 180,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0307` | 17,680.00 USD | 180,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0357` | 292.26 USD | 162,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0421` | 3,680.00 USD | 162,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 1,900.00 USD | 158,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0456` | 143.12 USD | 156,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0474` | 2,340.00 USD | 156,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0478` | 5,920.00 USD | 154,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 17,460.00 USD | 148,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0496` | 267.76 USD | 130,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 506.59 USD | 130,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 2,870.00 USD | 130,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 319.81 USD | 127,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0551` | 5,830.00 USD | 126,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0588` | 111.76 USD | 121,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 441.33 USD | 121,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 589.62 USD | 120,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 8,270.00 USD | 119,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 223.26 USD | 111,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 292.73 USD | 111,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 1,630.00 USD | 111,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 260.91 USD | 109,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 180.46 USD | 109,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 167.24 USD | 109,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 525.94 USD | 108,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0654` | 13,390.00 USD | 108,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 3,960.00 USD | 95,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0663` | 5,600.00 USD | 91,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 208.52 USD | 85,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0693` | 919.79 USD | 85,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0694` | 155.50 USD | 84,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0697` | 165.07 USD | 84,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0701` | 663.93 USD | 84,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0707` | 176.62 USD | 83,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0717` | 224.98 USD | 83,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0720` | 7,110.00 USD | 82,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0721` | 347.79 USD | 75,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0727` | 918.15 USD | 75,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0728` | 1,320.00 USD | 74,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0732` | 1,020.00 USD | 73,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 1,120.00 USD | 72,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0736` | 444.48 USD | 71,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0741` | 741.50 USD | 70,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0742` | 174.34 USD | 69,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0751` | 474.99 USD | 69,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0752` | 299.65 USD | 69,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0754` | 557.29 USD | 69,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 1,250.00 USD | 68,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0756` | 4,630.00 USD | 67,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0757` | 2,900.00 USD | 62,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0759` | 142.90 USD | 59,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0761` | 189.82 USD | 59,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0764` | 1,620.00 USD | 59,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0766` | 180.43 USD | 57,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0770` | 5,050.00 USD | 57,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0774` | 7,740.00 USD | 52,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 930.06 USD | 44,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0780` | 438.48 USD | 43,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0784` | 3,150.00 USD | 43,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0791` | 308.69 USD | 40,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0799` | 289.02 USD | 39,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0801` | 6,210.00 USD | 39,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0806` | 393.57 USD | 33,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0808` | 487.00 USD | 33,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0809` | 729.68 USD | 32,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0814` | 2,480.00 USD | 31,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0819` | 181.85 USD | 29,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0828` | 1,660.00 USD | 29,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0830` | 1,110.00 USD | 27,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0833` | 335.73 USD | 26,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 8,540.00 USD | 26,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0838` | 5,470.00 USD | 17,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0842` | 445.07 USD | 12,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0848` | 811.31 USD | 11,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0859` | 2,150.00 USD | 10,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0862` | 1,450.00 USD | 8,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0867` | 1,310.00 USD | 7,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0872` | 223.88 USD | 5,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0877` | 4,750.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0882` | 221.24 USD | 916.74 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0893` | 695.50 USD | 695.50 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1003` | 178.95 USD | 178.95 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1006` | 545.08 USD | 724.03 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1021` | 402.08 USD | 1,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1109` | 217.13 USD | 1,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1376` | 2,460.00 USD | 3,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1477` | 162.97 USD | 3,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1689` | 294.81 USD | 4,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1812` | 1,910.00 USD | 6,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0209` | 182,890.00 USD | 0.00 USD | 3,710.00 USD | `-78.23%` | `177,866.00` |
| `Live` | `Long` | `0.0225` | 179,180.00 USD | 0.00 USD | 314.97 USD | `-76.56%` | `14,030.00` |
| `Live` | `Long` | `0.0306` | 178,870.00 USD | 0.00 USD | 17,630.00 USD | `-68.10%` | `576,930.00` |
| `Live` | `Long` | `0.0323` | 161,240.00 USD | 0.00 USD | 265.21 USD | `-66.22%` | `8,198.00` |
| `Live` | `Long` | `0.0413` | 160,980.00 USD | 0.00 USD | 1,730.00 USD | `-56.82%` | `41,853.00` |
| `Live` | `Long` | `0.0421` | 159,250.00 USD | 0.00 USD | 3,680.00 USD | `-55.99%` | `87,382.00` |
| `Live` | `Long` | `0.0440` | 155,560.00 USD | 0.00 USD | 138.41 USD | `-54.00%` | `3,142.00` |
| `Live` | `Long` | `0.0462` | 155,420.00 USD | 0.00 USD | 16,430.00 USD | `-51.71%` | `355,228.00` |
| `Live` | `Long` | `0.0464` | 138,990.00 USD | 0.00 USD | 2,290.00 USD | `-51.60%` | `49,368.00` |
| `Live` | `Long` | `0.0471` | 136,710.00 USD | 0.00 USD | 5,820.00 USD | `-50.87%` | `123,747.00` |
| `Live` | `Long` | `0.0496` | 130,880.00 USD | 0.00 USD | 267.76 USD | `-48.16%` | `5,393.00` |
| `Live` | `Long` | `0.0508` | 130,620.00 USD | 0.00 USD | 506.59 USD | `-47.01%` | `9,982.00` |
| `Live` | `Long` | `0.0530` | 130,110.00 USD | 0.00 USD | 2,850.00 USD | `-44.61%` | `53,784.00` |
| `Live` | `Long` | `0.0539` | 127,260.00 USD | 0.00 USD | 527.09 USD | `-43.67%` | `9,770.00` |
| `Live` | `Long` | `0.0546` | 126,730.00 USD | 0.00 USD | 319.81 USD | `-42.94%` | `5,852.00` |
| `Live` | `Long` | `0.0551` | 126,410.00 USD | 0.00 USD | 5,830.00 USD | `-42.41%` | `105,702.00` |
| `Live` | `Long` | `0.0588` | 120,580.00 USD | 0.00 USD | 111.76 USD | `-38.55%` | `1,899.00` |
| `Live` | `Long` | `0.0599` | 120,470.00 USD | 0.00 USD | 441.33 USD | `-37.51%` | `7,374.00` |
| `Live` | `Long` | `0.0605` | 120,030.00 USD | 0.00 USD | 8,270.00 USD | `-36.77%` | `136,663.00` |
| `Live` | `Long` | `0.0607` | 111,750.00 USD | 0.00 USD | 223.26 USD | `-36.57%` | `3,675.00` |
| `Live` | `Long` | `0.0614` | 111,530.00 USD | 0.00 USD | 1,630.00 USD | `-35.84%` | `26,498.00` |
| `Live` | `Long` | `0.0621` | 109,900.00 USD | 0.00 USD | 260.91 USD | `-35.10%` | `4,198.00` |
| `Live` | `Long` | `0.0625` | 109,640.00 USD | 0.00 USD | 180.46 USD | `-34.69%` | `2,885.00` |
| `Live` | `Long` | `0.0629` | 109,460.00 USD | 0.00 USD | 300.86 USD | `-34.37%` | `4,787.00` |
| `Live` | `Long` | `0.0634` | 109,160.00 USD | 0.00 USD | 167.24 USD | `-33.85%` | `2,640.00` |
| `Live` | `Long` | `0.0636` | 108,990.00 USD | 0.00 USD | 525.94 USD | `-33.54%` | `8,263.00` |
| `Live` | `Long` | `0.0654` | 108,470.00 USD | 0.00 USD | 13,390.00 USD | `-31.76%` | `204,927.00` |
| `Live` | `Long` | `0.0659` | 95,070.00 USD | 0.00 USD | 3,960.00 USD | `-31.14%` | `60,000.00` |
| `Live` | `Long` | `0.0663` | 91,120.00 USD | 0.00 USD | 5,600.00 USD | `-30.82%` | `84,534.00` |
| `Live` | `Long` | `0.0673` | 85,520.00 USD | 0.00 USD | 208.52 USD | `-29.67%` | `3,096.00` |
| `Live` | `Long` | `0.0693` | 85,310.00 USD | 0.00 USD | 919.79 USD | `-27.59%` | `13,263.00` |
| `Live` | `Long` | `0.0694` | 84,390.00 USD | 0.00 USD | 155.50 USD | `-27.48%` | `2,239.00` |
| `Live` | `Long` | `0.0697` | 84,230.00 USD | 0.00 USD | 165.07 USD | `-27.27%` | `2,370.00` |
| `Live` | `Long` | `0.0701` | 84,070.00 USD | 0.00 USD | 663.93 USD | `-26.86%` | `9,478.00` |
| `Live` | `Long` | `0.0707` | 83,400.00 USD | 0.00 USD | 176.62 USD | `-26.23%` | `2,500.00` |
| `Live` | `Long` | `0.0717` | 83,230.00 USD | 0.00 USD | 224.98 USD | `-25.18%` | `3,140.00` |
| `Live` | `Long` | `0.0720` | 83,000.00 USD | 0.00 USD | 7,110.00 USD | `-24.87%` | `98,791.00` |
| `Live` | `Long` | `0.0721` | 75,890.00 USD | 0.00 USD | 347.79 USD | `-24.77%` | `4,827.00` |
| `Live` | `Long` | `0.0727` | 75,550.00 USD | 0.00 USD | 918.15 USD | `-24.14%` | `12,638.00` |
| `Live` | `Long` | `0.0728` | 74,630.00 USD | 0.00 USD | 1,320.00 USD | `-23.93%` | `18,128.00` |
| `Live` | `Long` | `0.0732` | 73,310.00 USD | 0.00 USD | 1,020.00 USD | `-23.51%` | `13,863.00` |
| `Live` | `Long` | `0.0735` | 72,290.00 USD | 0.00 USD | 1,120.00 USD | `-23.31%` | `15,256.00` |
| `Live` | `Long` | `0.0736` | 71,170.00 USD | 0.00 USD | 444.48 USD | `-23.10%` | `6,035.00` |
| `Live` | `Long` | `0.0741` | 70,730.00 USD | 0.00 USD | 741.50 USD | `-22.57%` | `10,000.00` |
| `Live` | `Long` | `0.0742` | 69,980.00 USD | 0.00 USD | 174.34 USD | `-22.47%` | `2,348.00` |
| `Live` | `Long` | `0.0751` | 69,810.00 USD | 0.00 USD | 474.99 USD | `-21.63%` | `6,329.00` |
| `Live` | `Long` | `0.0752` | 69,340.00 USD | 0.00 USD | 299.65 USD | `-21.43%` | `3,982.00` |
| `Live` | `Long` | `0.0754` | 69,040.00 USD | 0.00 USD | 557.29 USD | `-21.32%` | `7,396.00` |
| `Live` | `Long` | `0.0755` | 68,480.00 USD | 0.00 USD | 1,250.00 USD | `-21.22%` | `16,502.00` |
| `Live` | `Long` | `0.0756` | 67,230.00 USD | 0.00 USD | 4,630.00 USD | `-21.01%` | `61,227.00` |
| `Live` | `Long` | `0.0757` | 62,600.00 USD | 0.00 USD | 3,050.00 USD | `-20.90%` | `40,199.00` |
| `Live` | `Long` | `0.0761` | 59,560.00 USD | 0.00 USD | 189.82 USD | `-20.59%` | `2,496.00` |
| `Live` | `Long` | `0.0764` | 59,370.00 USD | 0.00 USD | 1,620.00 USD | `-20.28%` | `21,173.00` |
| `Live` | `Long` | `0.0766` | 57,750.00 USD | 0.00 USD | 180.43 USD | `-19.96%` | `2,354.00` |
| `Live` | `Long` | `0.0769` | 57,570.00 USD | 0.00 USD | 5,040.00 USD | `-19.75%` | `65,640.00` |
| `Live` | `Long` | `0.0774` | 52,530.00 USD | 0.00 USD | 7,740.00 USD | `-19.23%` | `100,000.00` |
| `Live` | `Long` | `0.0775` | 44,790.00 USD | 0.00 USD | 930.06 USD | `-19.02%` | `11,993.00` |
| `Live` | `Long` | `0.0780` | 43,860.00 USD | 0.00 USD | 438.48 USD | `-18.50%` | `5,618.00` |
| `Live` | `Long` | `0.0784` | 43,420.00 USD | 0.00 USD | 3,150.00 USD | `-18.19%` | `40,227.00` |
| `Live` | `Long` | `0.0791` | 40,270.00 USD | 0.00 USD | 308.69 USD | `-17.35%` | `3,900.00` |
| `Live` | `Long` | `0.0799` | 39,960.00 USD | 0.00 USD | 289.02 USD | `-16.52%` | `3,615.00` |
| `Live` | `Long` | `0.0801` | 39,670.00 USD | 0.00 USD | 6,210.00 USD | `-16.31%` | `77,489.00` |
| `Live` | `Long` | `0.0806` | 33,460.00 USD | 0.00 USD | 393.57 USD | `-15.79%` | `4,880.00` |
| `Live` | `Long` | `0.0808` | 33,070.00 USD | 0.00 USD | 487.00 USD | `-15.68%` | `6,031.00` |
| `Live` | `Long` | `0.0809` | 32,580.00 USD | 0.00 USD | 729.68 USD | `-15.47%` | `9,014.00` |
| `Live` | `Long` | `0.0814` | 31,850.00 USD | 0.00 USD | 2,480.00 USD | `-14.95%` | `30,478.00` |
| `Live` | `Long` | `0.0819` | 29,370.00 USD | 0.00 USD | 181.85 USD | `-14.43%` | `2,219.00` |
| `Live` | `Long` | `0.0827` | 29,190.00 USD | 0.00 USD | 1,650.00 USD | `-13.70%` | `20,000.00` |
| `Live` | `Long` | `0.0830` | 27,530.00 USD | 0.00 USD | 1,110.00 USD | `-13.28%` | `13,414.00` |
| `Live` | `Long` | `0.0833` | 26,420.00 USD | 0.00 USD | 335.73 USD | `-12.97%` | `4,028.00` |
| `Live` | `Long` | `0.0835` | 26,080.00 USD | 0.00 USD | 8,540.00 USD | `-12.76%` | `102,183.00` |
| `Live` | `Long` | `0.0838` | 17,550.00 USD | 0.00 USD | 5,470.00 USD | `-12.55%` | `65,287.00` |
| `Live` | `Long` | `0.0842` | 12,080.00 USD | 0.00 USD | 445.07 USD | `-12.13%` | `5,289.00` |
| `Live` | `Long` | `0.0851` | 11,630.00 USD | 0.00 USD | 844.80 USD | `-11.19%` | `9,933.00` |
| `Live` | `Long` | `0.0859` | 10,790.00 USD | 0.00 USD | 2,150.00 USD | `-10.25%` | `25,000.00` |
| `Live` | `Long` | `0.0862` | 8,640.00 USD | 0.00 USD | 1,450.00 USD | `-10.04%` | `16,779.00` |
| `Live` | `Long` | `0.0867` | 7,190.00 USD | 0.00 USD | 1,310.00 USD | `-9.42%` | `15,068.00` |
| `Live` | `Long` | `0.0872` | 5,890.00 USD | 0.00 USD | 223.88 USD | `-8.90%` | `2,566.00` |
| `Live` | `Long` | `0.0877` | 5,660.00 USD | 0.00 USD | 4,750.00 USD | `-8.37%` | `54,098.00` |
| `Live` | `Long` | `0.0882` | 916.74 USD | 0.00 USD | 221.24 USD | `-7.85%` | `2,507.00` |
| `Live` | `Long` | `0.0893` | 695.50 USD | 0.00 USD | 695.50 USD | `-6.70%` | `7,784.00` |
| `Live` | `Short` | `0.1003` | 178.95 USD | 178.95 USD | 0.00 USD | `+4.68%` | `1,785.00` |
| `Live` | `Short` | `0.1006` | 724.03 USD | 545.08 USD | 0.00 USD | `+4.99%` | `5,421.00` |
| `Live` | `Short` | `0.1021` | 1,130.00 USD | 402.08 USD | 0.00 USD | `+6.56%` | `3,940.00` |
| `Live` | `Short` | `0.1109` | 1,340.00 USD | 217.13 USD | 0.00 USD | `+15.85%` | `1,957.00` |
| `Live` | `Short` | `0.1381` | 3,820.00 USD | 2,470.00 USD | 0.00 USD | `+44.25%` | `17,912.00` |
| `Live` | `Short` | `0.1477` | 3,980.00 USD | 162.97 USD | 0.00 USD | `+54.28%` | `1,103.00` |
| `Live` | `Short` | `0.1689` | 4,280.00 USD | 294.81 USD | 0.00 USD | `+76.31%` | `1,746.00` |
| `Live` | `Short` | `0.1781` | 6,150.00 USD | 1,870.00 USD | 0.00 USD | `+85.92%` | `10,520.00` |
| `Live` | `Short` | `0.1908` | 6,250.00 USD | 102.62 USD | 0.00 USD | `+99.18%` | `538.00` |

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
  * Current Rate: `128.22` | Last 24h: `-2.41K` | Last 3d: `-9.10K` | Last 7d: `-8.18K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0009%` | **USDT OKX** | `-0.0165%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0011%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0045%` | **USDT Bitget** | `0.0075%` |
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
| `5m` | 6,010.00 USD | 3,130.00 USD | **`ACCUMULATION`** |
| `15m` | 17,540.00 USD | 21,970.00 USD | **`ACCUMULATION`** |
| `30m` | -41,220.00 USD | -35,800.00 USD | **`DISTRIBUTION`** |
| `1h` | -48,510.00 USD | -22,290.00 USD | **`DISTRIBUTION`** |
| `2h` | 44,240.00 USD | 28,480.00 USD | **`ACCUMULATION`** |
| `4h` | -80,790.00 USD | 54,940.00 USD | **`DISTRIBUTION`** |
| `6h` | -62,290.00 USD | 86,600.00 USD | **`ACCUMULATION`** |
| `8h` | -23,470.00 USD | 54,960.00 USD | **`ACCUMULATION`** |
| `12h` | -433,890.00 USD | -524,150.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,190,000.00 USD | -2,020,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -2,540,000.00 USD | -3,820,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,260,000.00 USD | -20,810,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+6.01K` | 15m=`+17.54K` | 1h=`-48.51K` | 24h=`-1.19M`
* Futures Capital Netflows: 5m=`+3.13K` | 15m=`+21.97K` | 1h=`-22.29K` | 24h=`-2.02M`
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
  * `2026-10-30 16:26:21 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:29:21 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0914` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-1.11` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `3.10`
  * Mathematical Lot Sizing: **`8.31 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0946` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.30` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-2.91`
  * Mathematical Lot Sizing: **`8.31 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0965`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
