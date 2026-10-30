# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 16:15:35 IST` (`2026-10-30 10:45:35 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9270` | **Live Ask Quote**: `0.9470` | **Mid Price**: `0.9370`
- **Spread Points**: `20.00` | **Spread BPS**: `213.45 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.9105` | VWAP Z-Score: `+0.50` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0066` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `44.40` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.9796` | Lower -3.00σ Band: `0.8414`
  * Upper +2.51σ Band: `0.9683` | Lower -2.51σ Band: `0.8527`
  * Upper +2.01σ Band: `0.9568` | Lower -2.01σ Band: `0.8642`
  * Upper +2.00σ Band: `0.9565` | Lower -2.00σ Band: `0.8645`
  * Upper +1.28σ Band: `0.9400` | Lower -1.28σ Band: `0.8810`
  * Upper +1.00σ Band: `0.9335` | Lower -1.00σ Band: `0.8875`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9248` | EMA-20=`0.9268` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9291` (Slope: `+0.0000`) | EMA-100=`0.9402`
  * Institutional Anchors: EMA-144=`0.9482` | EMA-200=`0.9564` (Slope: `-0.3943`) | EMA-233=`0.9595`
- **Range Boundaries**: 24H High=`1.01` | 24H Low=`0.8570` | Weekly High=`1.03` | Weekly Low=`0.8570`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9447` (Distance: `-0.76%`)
  * Point of Control (POC) = `0.9119` (Distance: `+2.81%`)
  * Value Area Low (VAL) = `0.8998` (Distance: `+4.19%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.02` | Weekly POC=`0.9945` | Weekly VAL=`0.9689`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9330` | Low=`0.8570`
  * London Session (08:00-16:00 UTC): High=`0.9480` | Low=`0.9190`
  * New York Session (13:00-21:00 UTC): High=`0.9270` | Low=`0.9190`
  * Initial Balance (First Hour): IB High=`0.9480` | IB Low=`0.9290`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9333` - `0.9407`
  * Optimal Trade Entry (OTE 0.705): `0.9389`
  * Structural Invalidation Anchor (0.786): `0.9445`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9327` | `0.9373` | `0.9325` | `0.9355` | `358,742` | 335,809.62 USD | -54,081.31 USD | `-16.10%` | -6,037,246.12 USD | `-0.75` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.9355` | `0.9374` | `0.9353` | `0.9372` | `135,713` | 127,100.20 USD | 9,710.17 USD | `+7.64%` | -6,027,535.95 USD | `+1.28` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.9372` | `0.9384` | `0.9370` | `0.9380` | `67,274` | 63,090.59 USD | 28,380.76 USD | `+44.98%` | -5,999,155.19 USD | `+1.64` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.9340` | `0.9345` | `0.9304` | `0.9324` | `410,952` | 383,267.52 USD | -44,184.07 USD | `-11.53%` | -5,933,383.29 USD | `+0.42` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.9323` | `0.9366` | `0.9302` | `0.9326` | `268,379` | 250,363.19 USD | -49,781.52 USD | `-19.88%` | -5,983,164.81 USD | `+0.29` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.9327` | `0.9384` | `0.9325` | `0.9381` | `562,442` | 526,669.56 USD | -16,298.15 USD | `-3.09%` | -5,999,462.96 USD | `+0.66` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9454` | `0.9488` | `0.9359` | `0.9375` | `1,853,058` | 1,744,265.88 USD | -394,329.00 USD | `-22.61%` | -5,481,321.37 USD | `-0.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.9375` | `0.9390` | `0.9292` | `0.9340` | `1,605,127` | 1,499,731.69 USD | -461,107.04 USD | `-30.75%` | -5,942,428.41 USD | `-0.17` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.9340` | `0.9384` | `0.9302` | `0.9382` | `1,241,271` | 1,159,829.16 USD | -109,948.36 USD | `-9.48%` | -6,052,376.76 USD | `+0.17` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,092,983.65 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9603` | `0.9263` | `0.9454` | `10,832,060` | 10,247,507.62 USD | -822,915.31 USD | `-8.03%` | -4,915,898.96 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9454` | `0.9488` | `0.9292` | `0.9380` | `4,699,085` | 4,403,478.97 USD | -965,541.71 USD | `-21.93%` | -5,881,440.67 USD | `+0.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -974,642.25 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,499,370.98 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,092,983.65 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9603` | `0.9263` | `0.9454` | `10,832,060` | 10,247,507.62 USD | -822,915.31 USD | `-8.03%` | -4,915,898.96 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9454` | `0.9488` | `0.9292` | `0.9380` | `4,699,085` | 4,403,478.97 USD | -965,541.71 USD | `-21.93%` | -5,881,440.67 USD | `+0.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`0.9370`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:12:11 IST` |

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
  * 24H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.8866` (Vol: 283,500.00 USD, Dist: `--3.43%`)
  * 48H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.8871` (Vol: 412,800.00 USD, Dist: `--3.38%`)
  * 3D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.8871` (Vol: 412,800.00 USD, Dist: `--3.38%`)
  * 7D Horizon: Short MP=`1.06` (Vol: 252,200.00 USD, Dist: `+15.33%`) | Long MP=`0.8862` (Vol: 283,500.00 USD, Dist: `--3.48%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.1945` | 333.66 USD | 462,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2105` | 105.25 USD | 461,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3045` | 192.63 USD | 461,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3625` | 800.76 USD | 461,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4195` | 2,800.00 USD | 460,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4265` | 2,430.00 USD | 457,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4685` | 147.02 USD | 455,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4705` | 2,590.00 USD | 455,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5035` | 201.75 USD | 452,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5065` | 3,290.00 USD | 452,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5425` | 542.50 USD | 449,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 14,600.00 USD | 448,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 577.36 USD | 434,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 683.51 USD | 433,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 137.53 USD | 432,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5995` | 237.70 USD | 432,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6055` | 1,480.00 USD | 432,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6075` | 1,810.00 USD | 430,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 105.96 USD | 429,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 147.48 USD | 429,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6295` | 220.32 USD | 428,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 757.80 USD | 428,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 106.00 USD | 427,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 507.86 USD | 427,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 2,090.00 USD | 427,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 20,300.00 USD | 425,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 4,230.00 USD | 404,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 202.47 USD | 400,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 149.44 USD | 400,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 63,890.00 USD | 400,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6745` | 84,310.00 USD | 336,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 423.10 USD | 252,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 512.97 USD | 251,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6915` | 19,800.00 USD | 251,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 322.62 USD | 231,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7005` | 1,140.00 USD | 231,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7115` | 158.95 USD | 229,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 988.87 USD | 229,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7215` | 1,580.00 USD | 228,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 397.93 USD | 227,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7295` | 291.58 USD | 226,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 2,300.00 USD | 226,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,140.00 USD | 224,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 283.30 USD | 223,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7515` | 32,890.00 USD | 222,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 2,800.00 USD | 189,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 629.25 USD | 187,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 144.07 USD | 186,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7565` | 8,860.00 USD | 186,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7615` | 54,070.00 USD | 177,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7635` | 308.00 USD | 123,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7705` | 152.94 USD | 123,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 3,840.00 USD | 122,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7775` | 2,490.00 USD | 119,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 156.51 USD | 116,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7870` | 3,110,000.00 USD | 3,110,000.00 USD | 5,920.00 USD | 4,300.00 USD | 630.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7890` | 3,100,000.00 USD | 3,100,000.00 USD | 88.75 USD | 0.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 277.39 USD | 116,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7910` | 3,100,000.00 USD | 3,100,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7930` | 3,080,000.00 USD | 3,080,000.00 USD | 20,360.00 USD | 1,560.00 USD | 6,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7935` | 1,760.00 USD | 116,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7950` | 3,050,000.00 USD | 3,050,000.00 USD | 3,290.00 USD | 8,430.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7970` | 3,020,000.00 USD | 3,020,000.00 USD | 10,100.00 USD | 1,130.00 USD | 522.30 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7985` | 210.40 USD | 114,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7990` | 3,010,000.00 USD | 3,010,000.00 USD | 20,360.00 USD | 6,180.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8010` | 2,970,000.00 USD | 2,970,000.00 USD | 5,420.00 USD | 5,300.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8030` | 2,960,000.00 USD | 2,960,000.00 USD | 4,550.00 USD | 2,440.00 USD | 10,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8050` | 2,940,000.00 USD | 2,940,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8070` | 2,920,000.00 USD | 2,920,000.00 USD | 12,160.00 USD | 4,660.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8090` | 2,880,000.00 USD | 2,880,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8110` | 2,880,000.00 USD | 2,880,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8130` | 2,870,000.00 USD | 2,870,000.00 USD | 14,060.00 USD | 2,970.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 114,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8150` | 2,840,000.00 USD | 2,840,000.00 USD | 61,120.00 USD | 7,590.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8170` | 2,750,000.00 USD | 2,750,000.00 USD | 10,780.00 USD | 8,770.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8190` | 2,720,000.00 USD | 2,720,000.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8210` | 2,710,000.00 USD | 2,710,000.00 USD | 7,510.00 USD | 3,290.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 113,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8230` | 2,690,000.00 USD | 2,690,000.00 USD | 29,430.00 USD | 5,100.00 USD | 13,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 749.96 USD | 111,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8250` | 2,640,000.00 USD | 2,640,000.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 2,630,000.00 USD | 2,630,000.00 USD | 4,320.00 USD | 5,770.00 USD | 616.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8290` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8310` | 2,610,000.00 USD | 2,610,000.00 USD | 9,280.00 USD | 1,660.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8330` | 2,600,000.00 USD | 2,600,000.00 USD | 16,220.00 USD | 11,360.00 USD | 77.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8350` | 2,570,000.00 USD | 2,570,000.00 USD | 19,490.00 USD | 0.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 110,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8370` | 2,380,000.00 USD | 2,380,000.00 USD | 18,140.00 USD | 2,530.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8370` | 2,550,000.00 USD | 2,550,000.00 USD | 15,240.00 USD | 1,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8390` | 2,340,000.00 USD | 2,340,000.00 USD | 1,740.00 USD | 745.84 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8390` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8410` | 2,340,000.00 USD | 2,340,000.00 USD | 1,470.00 USD | 2,040.00 USD | 1,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8410` | 2,520,000.00 USD | 2,520,000.00 USD | 270.00 USD | 3,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,570.00 USD | 110,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8430` | 2,330,000.00 USD | 2,330,000.00 USD | 4,540.00 USD | 6,880.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8430` | 2,520,000.00 USD | 2,520,000.00 USD | 11,320.00 USD | 3,840.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8450` | 2,320,000.00 USD | 2,320,000.00 USD | 2,360.00 USD | 7,850.00 USD | 429.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8450` | 2,500,000.00 USD | 2,500,000.00 USD | 1,980.00 USD | 404.64 USD | 474.61 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8470` | 2,310,000.00 USD | 2,310,000.00 USD | 24,110.00 USD | 1,110.00 USD | 165.77 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8470` | 2,500,000.00 USD | 2,500,000.00 USD | 7,900.00 USD | 1,730.00 USD | 2,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8490` | 2,280,000.00 USD | 2,280,000.00 USD | 5,120.00 USD | 2,400.00 USD | 7,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8490` | 2,490,000.00 USD | 2,490,000.00 USD | 22,370.00 USD | 9,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 108,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8510` | 2,270,000.00 USD | 2,270,000.00 USD | 13,560.00 USD | 4,140.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 2,450,000.00 USD | 2,450,000.00 USD | 14,280.00 USD | 991.53 USD | 21,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8530` | 2,230,000.00 USD | 2,230,000.00 USD | 4,680.00 USD | 3,830.00 USD | 5,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 2,420,000.00 USD | 2,420,000.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8550` | 2,220,000.00 USD | 2,220,000.00 USD | 18,270.00 USD | 3,040.00 USD | 5,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 2,410,000.00 USD | 2,410,000.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8570` | 2,190,000.00 USD | 2,190,000.00 USD | 989.11 USD | 1,720.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8570` | 2,410,000.00 USD | 2,410,000.00 USD | 3,540.00 USD | 944.22 USD | 8,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 107,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8590` | 2,180,000.00 USD | 2,180,000.00 USD | 6,870.00 USD | 10,640.00 USD | 6,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8590` | 2,390,000.00 USD | 2,390,000.00 USD | 3,730.00 USD | 0.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8610` | 2,160,000.00 USD | 2,160,000.00 USD | 8,320.00 USD | 855.53 USD | 16,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8610` | 2,390,000.00 USD | 2,390,000.00 USD | 9,960.00 USD | 3,660.00 USD | 35,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8630` | 2,130,000.00 USD | 2,130,000.00 USD | 39,330.00 USD | 12,290.00 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8630` | 2,340,000.00 USD | 2,340,000.00 USD | 758.91 USD | 2,910.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 107,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 106,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8650` | 2,080,000.00 USD | 2,080,000.00 USD | 17,640.00 USD | 2,110.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8650` | 2,330,000.00 USD | 2,330,000.00 USD | 47,860.00 USD | 18,930.00 USD | 184.85 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,390.00 USD | 106,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8670` | 2,060,000.00 USD | 2,060,000.00 USD | 12,000.00 USD | 10,090.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8670` | 2,270,000.00 USD | 2,270,000.00 USD | 13,660.00 USD | 3,720.00 USD | 12,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8690` | 2,040,000.00 USD | 2,040,000.00 USD | 42,010.00 USD | 3,780.00 USD | 29,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8690` | 2,240,000.00 USD | 2,240,000.00 USD | 160,750.00 USD | 13,110.00 USD | 46,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 12,590.00 USD | 105,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8705` | 92,480.00 USD | 92,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8710` | 1,960,000.00 USD | 1,960,000.00 USD | 42,290.00 USD | 24,900.00 USD | 28,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8710` | 2,020,000.00 USD | 2,020,000.00 USD | 7,370.00 USD | 23,340.00 USD | 13,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8730` | 1,860,000.00 USD | 1,860,000.00 USD | 54,500.00 USD | 21,510.00 USD | 25,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 8,170.00 USD | 295.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8750` | 1,760,000.00 USD | 1,760,000.00 USD | 36,600.00 USD | 6,900.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 6,380.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8770` | 1,700,000.00 USD | 1,700,000.00 USD | 10,480.00 USD | 152.79 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8770` | 1,950,000.00 USD | 1,950,000.00 USD | 1,390.00 USD | 0.00 USD | 30,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8790` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 40.93 USD | 50,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 1,920,000.00 USD | 1,920,000.00 USD | 873.30 USD | 5,580.00 USD | 53,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8810` | 1,640,000.00 USD | 1,640,000.00 USD | 13,820.00 USD | 5,210.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 1,860,000.00 USD | 1,860,000.00 USD | 1,830.00 USD | 240.78 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8830` | 1,620,000.00 USD | 1,620,000.00 USD | 656.20 USD | 5,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8830` | 1,860,000.00 USD | 1,860,000.00 USD | 2,320.00 USD | 10,140.00 USD | 11,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8850` | 1,610,000.00 USD | 1,610,000.00 USD | 5,680.00 USD | 34,880.00 USD | 11,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8850` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 5,800.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8870` | 1,560,000.00 USD | 1,560,000.00 USD | 68,710.00 USD | 17,740.00 USD | 32,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8870` | 1,820,000.00 USD | 1,820,000.00 USD | 271,870.00 USD | 22,320.00 USD | 81,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8890` | 1,440,000.00 USD | 1,440,000.00 USD | 69,610.00 USD | 40,830.00 USD | 4,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8890` | 1,450,000.00 USD | 1,450,000.00 USD | 54,380.00 USD | 73,890.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8910` | 1,330,000.00 USD | 1,330,000.00 USD | 2,150.00 USD | 38,730.00 USD | 20,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8910` | 1,300,000.00 USD | 1,300,000.00 USD | 75,300.00 USD | 22,240.00 USD | 34,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8930` | 1,260,000.00 USD | 1,260,000.00 USD | 56,810.00 USD | 24,630.00 USD | 37,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8930` | 1,170,000.00 USD | 1,170,000.00 USD | 62,870.00 USD | 23,560.00 USD | 9,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8950` | 1,150,000.00 USD | 1,150,000.00 USD | 6,700.00 USD | 15,420.00 USD | 8,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8950` | 1,080,000.00 USD | 1,080,000.00 USD | 7,120.00 USD | 37,670.00 USD | 57,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8970` | 1,120,000.00 USD | 1,120,000.00 USD | 8,300.00 USD | 28,440.00 USD | 19,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8970` | 973,990.00 USD | 973,990.00 USD | 2,140.00 USD | 11,010.00 USD | 56,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8990` | 1,060,000.00 USD | 1,060,000.00 USD | 3,650.00 USD | 24,130.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8990` | 904,290.00 USD | 904,290.00 USD | 0.00 USD | 34,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9010` | 1,030,000.00 USD | 1,030,000.00 USD | 5,490.00 USD | 26,220.00 USD | 4,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9010` | 870,070.00 USD | 870,070.00 USD | 0.00 USD | 48,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9030` | 990,890.00 USD | 990,890.00 USD | 8,980.00 USD | 17,560.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9030` | 821,230.00 USD | 821,230.00 USD | 0.00 USD | 16,370.00 USD | 23,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9050` | 946,120.00 USD | 946,120.00 USD | 19,330.00 USD | 11,600.00 USD | 22,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9050` | 780,930.00 USD | 780,930.00 USD | 0.00 USD | 3,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9070` | 893,130.00 USD | 893,130.00 USD | 36,650.00 USD | 8,370.00 USD | 33,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9070` | 777,090.00 USD | 777,090.00 USD | 23,910.00 USD | 0.00 USD | 42,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9090` | 814,600.00 USD | 814,600.00 USD | 7,100.00 USD | 9,080.00 USD | 239.84 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9110` | 798,180.00 USD | 798,180.00 USD | 25,560.00 USD | 2,850.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9130` | 767,690.00 USD | 767,690.00 USD | 17,080.00 USD | 9,480.00 USD | 22,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9130` | 711,140.00 USD | 711,140.00 USD | 0.00 USD | 0.00 USD | 20,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9150` | 718,810.00 USD | 718,810.00 USD | 11,120.00 USD | 17,780.00 USD | 24,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9150` | 690,420.00 USD | 690,420.00 USD | 0.00 USD | 12,890.00 USD | 16,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9170` | 665,260.00 USD | 665,260.00 USD | 7,300.00 USD | 16,660.00 USD | 15,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9170` | 661,400.00 USD | 661,400.00 USD | 0.00 USD | 0.00 USD | 33,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9190` | 626,250.00 USD | 626,250.00 USD | 9,900.00 USD | 10,760.00 USD | 12,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9210` | 593,480.00 USD | 593,480.00 USD | 12,850.00 USD | 3,680.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9210` | 628,210.00 USD | 628,210.00 USD | 0.00 USD | 7,760.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9230` | 570,920.00 USD | 570,920.00 USD | 6,600.00 USD | 7,140.00 USD | 21,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9230` | 616,490.00 USD | 616,490.00 USD | 294,370.00 USD | 0.00 USD | 26,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9250` | 535,490.00 USD | 535,490.00 USD | 99,970.00 USD | 63,270.00 USD | 62,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9250` | 295,440.00 USD | 295,440.00 USD | 0.00 USD | 52,780.00 USD | 84,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9270` | 309,720.00 USD | 309,720.00 USD | 39,920.00 USD | 7,040.00 USD | 73,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9270` | 158,580.00 USD | 158,580.00 USD | 44,020.00 USD | 11,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9290` | 188,950.00 USD | 188,950.00 USD | 80,950.00 USD | 20,440.00 USD | 38,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9290` | 102,770.00 USD | 102,770.00 USD | 0.00 USD | 12,750.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9310` | 48,990.00 USD | 48,990.00 USD | 0.00 USD | 7,130.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9330` | 36,460.00 USD | 36,460.00 USD | 3,720.00 USD | 6,140.00 USD | 26,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9330` | 88,410.00 USD | 88,410.00 USD | 37,450.00 USD | 0.00 USD | 31,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9350` | 36,730.00 USD | 36,730.00 USD | 36,510.00 USD | 221.86 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9350` | 73,460.00 USD | 73,460.00 USD | 36,510.00 USD | 221.86 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9350` | 19,600.00 USD | 19,600.00 USD | 0.00 USD | 0.00 USD | 19,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9370` | 74,500.00 USD | 74,500.00 USD | 0.00 USD | 182.01 USD | 852.35 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9370` | 84,400.00 USD | 84,400.00 USD | 16,340.00 USD | 19,540.00 USD | 48,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9390` | 76,150.00 USD | 76,150.00 USD | 1,340.00 USD | 309.30 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9390` | 158,560.00 USD | 158,560.00 USD | 39,250.00 USD | 0.00 USD | 34,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9410` | 77,060.00 USD | 77,060.00 USD | 673.54 USD | 239.40 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9410` | 321,610.00 USD | 321,610.00 USD | 161,930.00 USD | 1,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9430` | 78,520.00 USD | 78,520.00 USD | 1,230.00 USD | 224.96 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 345,900.00 USD | 345,900.00 USD | 0.00 USD | 20,890.00 USD | 3,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9470` | 79,040.00 USD | 79,040.00 USD | 0.00 USD | 199.60 USD | 319.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 432,410.00 USD | 432,410.00 USD | 3,540.00 USD | 6,380.00 USD | 76,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9490` | 159,570.00 USD | 159,570.00 USD | 80,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 516,340.00 USD | 516,340.00 USD | 2,770.00 USD | 10,340.00 USD | 70,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9510` | 170,560.00 USD | 170,560.00 USD | 5,190.00 USD | 813.18 USD | 4,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 807,740.00 USD | 807,740.00 USD | 258,650.00 USD | 28,180.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9530` | 192,180.00 USD | 192,180.00 USD | 7,370.00 USD | 8,490.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 828,800.00 USD | 828,800.00 USD | 0.00 USD | 20,610.00 USD | 447.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9550` | 265,130.00 USD | 265,130.00 USD | 25,300.00 USD | 39,260.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 848,530.00 USD | 848,530.00 USD | 0.00 USD | 19,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9570` | 292,340.00 USD | 292,340.00 USD | 13,680.00 USD | 8,760.00 USD | 4,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 861,690.00 USD | 861,690.00 USD | 1,910.00 USD | 10,300.00 USD | 957.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9590` | 314,010.00 USD | 314,010.00 USD | 14,060.00 USD | 3,680.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 882,760.00 USD | 882,760.00 USD | 1,980.00 USD | 18,220.00 USD | 866.69 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9610` | 371,260.00 USD | 371,260.00 USD | 14,760.00 USD | 11,950.00 USD | 30,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9610` | 908,150.00 USD | 908,150.00 USD | 24,370.00 USD | 0.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9630` | 549,540.00 USD | 549,540.00 USD | 102,030.00 USD | 30,630.00 USD | 45,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 1,080,000.00 USD | 1,080,000.00 USD | 56,160.00 USD | 31,820.00 USD | 84,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9650` | 690,920.00 USD | 690,920.00 USD | 29,080.00 USD | 33,020.00 USD | 79,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 1,190,000.00 USD | 1,190,000.00 USD | 97,600.00 USD | 0.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9670` | 787,350.00 USD | 787,350.00 USD | 53,970.00 USD | 16,730.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9670` | 1,240,000.00 USD | 1,240,000.00 USD | 40,070.00 USD | 5,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9690` | 828,680.00 USD | 828,680.00 USD | 14,860.00 USD | 14,610.00 USD | 11,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 21,100.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9710` | 942,000.00 USD | 942,000.00 USD | 15,040.00 USD | 19,120.00 USD | 79,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 24,440.00 USD | 31,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9730` | 1,050,000.00 USD | 1,050,000.00 USD | 48,020.00 USD | 14,900.00 USD | 40,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 1,380,000.00 USD | 1,380,000.00 USD | 2,910.00 USD | 9,290.00 USD | 27,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9750` | 1,130,000.00 USD | 1,130,000.00 USD | 29,660.00 USD | 19,230.00 USD | 34,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 1,450,000.00 USD | 1,450,000.00 USD | 2,090.00 USD | 17,230.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9770` | 1,230,000.00 USD | 1,230,000.00 USD | 78,910.00 USD | 14,700.00 USD | 11,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 1,550,000.00 USD | 1,550,000.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9790` | 1,310,000.00 USD | 1,310,000.00 USD | 36,590.00 USD | 11,310.00 USD | 26,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 3,880.00 USD | 85,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 102.95 USD | 102.95 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9810` | 1,360,000.00 USD | 1,360,000.00 USD | 16,990.00 USD | 6,620.00 USD | 28,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9810` | 1,770,000.00 USD | 1,770,000.00 USD | 540.00 USD | 4,020.00 USD | 119,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9830` | 1,480,000.00 USD | 1,480,000.00 USD | 33,340.00 USD | 27,220.00 USD | 55,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 2,000,000.00 USD | 2,000,000.00 USD | 124,720.00 USD | 15,810.00 USD | 94,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9850` | 1,550,000.00 USD | 1,550,000.00 USD | 46,690.00 USD | 8,800.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 211.77 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9870` | 1,590,000.00 USD | 1,590,000.00 USD | 14,650.00 USD | 6,470.00 USD | 22,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 2,130,000.00 USD | 2,130,000.00 USD | 40,020.00 USD | 0.00 USD | 67,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9890` | 1,660,000.00 USD | 1,660,000.00 USD | 27,890.00 USD | 3,780.00 USD | 30,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9890` | 2,150,000.00 USD | 2,150,000.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9910` | 1,770,000.00 USD | 1,770,000.00 USD | 60,130.00 USD | 5,890.00 USD | 45,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9910` | 2,190,000.00 USD | 2,190,000.00 USD | 3,700.00 USD | 800.44 USD | 35,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9925` | 3,940.00 USD | 4,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9930` | 1,800,000.00 USD | 1,800,000.00 USD | 16,320.00 USD | 5,130.00 USD | 8,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9930` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 36,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9950` | 1,830,000.00 USD | 1,830,000.00 USD | 29,250.00 USD | 2,120.00 USD | 7,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9950` | 2,350,000.00 USD | 2,350,000.00 USD | 63,060.00 USD | 5,380.00 USD | 58,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9970` | 1,900,000.00 USD | 1,900,000.00 USD | 46,950.00 USD | 1,870.00 USD | 13,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 2,450,000.00 USD | 2,450,000.00 USD | 95,130.00 USD | 253.35 USD | 4,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9985` | 852.22 USD | 4,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9990` | 1,960,000.00 USD | 1,960,000.00 USD | 35,340.00 USD | 17,910.00 USD | 10,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 6,490.00 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,030,000.00 USD | 2,030,000.00 USD | 44,580.00 USD | 10,790.00 USD | 13,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,510,000.00 USD | 2,510,000.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,060,000.00 USD | 2,060,000.00 USD | 12,370.00 USD | 9,310.00 USD | 6,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,660,000.00 USD | 2,660,000.00 USD | 107,670.00 USD | 21,850.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,120,000.00 USD | 2,120,000.00 USD | 54,780.00 USD | 5,520.00 USD | 5,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,710,000.00 USD | 2,710,000.00 USD | 32,430.00 USD | 3,970.00 USD | 12,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,230,000.00 USD | 2,230,000.00 USD | 50,600.00 USD | 11,770.00 USD | 45,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,780,000.00 USD | 2,780,000.00 USD | 35,710.00 USD | 240.78 USD | 29,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,280,000.00 USD | 2,280,000.00 USD | 30,870.00 USD | 13,790.00 USD | 7,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,800,000.00 USD | 2,800,000.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,320,000.00 USD | 2,320,000.00 USD | 9,660.00 USD | 23,460.00 USD | 265.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,840,000.00 USD | 2,840,000.00 USD | 20,090.00 USD | 17,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,330,000.00 USD | 2,330,000.00 USD | 10,450.00 USD | 1,540.00 USD | 3,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,890,000.00 USD | 2,890,000.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,390,000.00 USD | 2,390,000.00 USD | 14,310.00 USD | 23,780.00 USD | 14,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 26,510.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,400,000.00 USD | 2,400,000.00 USD | 3,990.00 USD | 2,940.00 USD | 12,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,970,000.00 USD | 2,970,000.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,480,000.00 USD | 2,480,000.00 USD | 55,630.00 USD | 4,860.00 USD | 10,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,090,000.00 USD | 3,090,000.00 USD | 17,960.00 USD | 83,360.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 760.04 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,510,000.00 USD | 2,510,000.00 USD | 6,670.00 USD | 7,410.00 USD | 21,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,250,000.00 USD | 3,250,000.00 USD | 61,450.00 USD | 32,840.00 USD | 68,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,600,000.00 USD | 2,600,000.00 USD | 44,890.00 USD | 18,460.00 USD | 29,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,560,000.00 USD | 3,560,000.00 USD | 82,230.00 USD | 86,210.00 USD | 146,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,680,000.00 USD | 2,680,000.00 USD | 43,590.00 USD | 9,520.00 USD | 20,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,680,000.00 USD | 3,680,000.00 USD | 28,320.00 USD | 48,490.00 USD | 37,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,710,000.00 USD | 2,710,000.00 USD | 15,190.00 USD | 11,870.00 USD | 8,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,990,000.00 USD | 3,990,000.00 USD | 161,070.00 USD | 129,470.00 USD | 25,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.03` | 152.32 USD | 5,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,760,000.00 USD | 2,760,000.00 USD | 14,070.00 USD | 16,110.00 USD | 20,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,200,000.00 USD | 4,200,000.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,890,000.00 USD | 2,890,000.00 USD | 77,920.00 USD | 11,810.00 USD | 32,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,410,000.00 USD | 4,410,000.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,920,000.00 USD | 2,920,000.00 USD | 17,330.00 USD | 1,510.00 USD | 16,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,530,000.00 USD | 4,530,000.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.03` | 221.28 USD | 6,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,960,000.00 USD | 2,960,000.00 USD | 11,120.00 USD | 18,010.00 USD | 6,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,840,000.00 USD | 4,840,000.00 USD | 259,060.00 USD | 8,290.00 USD | 43,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,150,000.00 USD | 5,150,000.00 USD | 193,150.00 USD | 3,330.00 USD | 109,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,530,000.00 USD | 5,530,000.00 USD | 239,580.00 USD | 9,010.00 USD | 134,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 182.19 USD | 6,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,980,000.00 USD | 5,980,000.00 USD | 285,690.00 USD | 2,090.00 USD | 159,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,180,000.00 USD | 6,180,000.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,440,000.00 USD | 6,440,000.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 6,960,000.00 USD | 6,960,000.00 USD | 178,890.00 USD | 96,370.00 USD | 244,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 367.04 USD | 6,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,170,000.00 USD | 7,170,000.00 USD | 110,190.00 USD | 13,780.00 USD | 77,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,480,000.00 USD | 7,480,000.00 USD | 175,350.00 USD | 43,690.00 USD | 96,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,680,000.00 USD | 7,680,000.00 USD | 68,010.00 USD | 58,070.00 USD | 74,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,910,000.00 USD | 7,910,000.00 USD | 121,450.00 USD | 33,860.00 USD | 72,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,310,000.00 USD | 8,310,000.00 USD | 218,860.00 USD | 70,160.00 USD | 106,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,760,000.00 USD | 8,760,000.00 USD | 239,650.00 USD | 74,380.00 USD | 145,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,040,000.00 USD | 9,040,000.00 USD | 138,520.00 USD | 56,310.00 USD | 78,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,310,000.00 USD | 9,310,000.00 USD | 132,250.00 USD | 71,450.00 USD | 66,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,470,000.00 USD | 9,470,000.00 USD | 74,870.00 USD | 22,420.00 USD | 61,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.08` | 2,230.00 USD | 8,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.11` | 170.02 USD | 8,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.15` | 13,470.00 USD | 22,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 126.85 USD | 22,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 11,730.00 USD | 34,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 239.77 USD | 34,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.37` | 3,880.00 USD | 38,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,200.00 USD | 41,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 176.42 USD | 41,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 123.26 USD | 41,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 1,810.00 USD | 43,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 791.80 USD | 44,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 79,040.00 USD | 123,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.63` | 2,440.00 USD | 126,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.63` | 237.96 USD | 126,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 8,240.00 USD | 134,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 318.07 USD | 134,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 300.15 USD | 135,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 190.42 USD | 135,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 13,140.00 USD | 148,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 647.64 USD | 149,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 380.81 USD | 149,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 208.37 USD | 149,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1945` | 462,110.00 USD | 0.00 USD | 333.66 USD | `-79.14%` | `1,715.50` |
| `Live` | `Long` | `0.2105` | 461,780.00 USD | 0.00 USD | 105.25 USD | `-77.43%` | `500.00` |
| `Live` | `Long` | `0.3045` | 461,680.00 USD | 0.00 USD | 192.63 USD | `-67.35%` | `632.60` |
| `Live` | `Long` | `0.3625` | 461,480.00 USD | 0.00 USD | 800.76 USD | `-61.13%` | `2,209.00` |
| `Live` | `Long` | `0.4195` | 460,680.00 USD | 0.00 USD | 2,800.00 USD | `-55.02%` | `6,675.20` |
| `Live` | `Long` | `0.4265` | 457,880.00 USD | 0.00 USD | 2,430.00 USD | `-54.26%` | `5,698.80` |
| `Live` | `Long` | `0.4685` | 455,450.00 USD | 0.00 USD | 147.02 USD | `-49.76%` | `313.80` |
| `Live` | `Long` | `0.4705` | 455,300.00 USD | 0.00 USD | 2,590.00 USD | `-49.55%` | `5,500.00` |
| `Live` | `Long` | `0.5035` | 452,720.00 USD | 0.00 USD | 201.75 USD | `-46.01%` | `400.70` |
| `Live` | `Long` | `0.5065` | 452,510.00 USD | 0.00 USD | 3,290.00 USD | `-45.69%` | `6,504.70` |
| `Live` | `Long` | `0.5425` | 449,220.00 USD | 0.00 USD | 542.50 USD | `-41.83%` | `1,000.00` |
| `Live` | `Long` | `0.5655` | 448,680.00 USD | 0.00 USD | 14,600.00 USD | `-39.36%` | `25,816.60` |
| `Live` | `Long` | `0.5695` | 434,080.00 USD | 0.00 USD | 577.36 USD | `-38.93%` | `1,013.80` |
| `Live` | `Long` | `0.5845` | 433,500.00 USD | 0.00 USD | 683.51 USD | `-37.32%` | `1,169.40` |
| `Live` | `Long` | `0.5895` | 432,820.00 USD | 0.00 USD | 137.53 USD | `-36.79%` | `233.30` |
| `Live` | `Long` | `0.5995` | 432,680.00 USD | 0.00 USD | 237.70 USD | `-35.71%` | `396.50` |
| `Live` | `Long` | `0.6055` | 432,440.00 USD | 0.00 USD | 1,480.00 USD | `-35.07%` | `2,448.50` |
| `Live` | `Long` | `0.6075` | 430,960.00 USD | 0.00 USD | 1,810.00 USD | `-34.86%` | `2,971.80` |
| `Live` | `Long` | `0.6125` | 429,150.00 USD | 0.00 USD | 105.96 USD | `-34.32%` | `173.00` |
| `Live` | `Long` | `0.6145` | 429,050.00 USD | 0.00 USD | 147.48 USD | `-34.10%` | `240.00` |
| `Live` | `Long` | `0.6295` | 428,900.00 USD | 0.00 USD | 220.32 USD | `-32.50%` | `350.00` |
| `Live` | `Long` | `0.6315` | 428,680.00 USD | 0.00 USD | 757.80 USD | `-32.28%` | `1,200.00` |
| `Live` | `Long` | `0.6355` | 427,920.00 USD | 0.00 USD | 106.00 USD | `-31.85%` | `166.80` |
| `Live` | `Long` | `0.6365` | 427,820.00 USD | 0.00 USD | 507.86 USD | `-31.75%` | `797.90` |
| `Live` | `Long` | `0.6405` | 427,310.00 USD | 0.00 USD | 2,090.00 USD | `-31.32%` | `3,262.00` |
| `Live` | `Long` | `0.6425` | 425,220.00 USD | 0.00 USD | 20,300.00 USD | `-31.10%` | `31,595.60` |
| `Live` | `Long` | `0.6465` | 404,920.00 USD | 0.00 USD | 4,230.00 USD | `-30.67%` | `6,539.70` |
| `Live` | `Long` | `0.6475` | 400,690.00 USD | 0.00 USD | 202.47 USD | `-30.57%` | `312.70` |
| `Live` | `Long` | `0.6595` | 400,490.00 USD | 0.00 USD | 149.44 USD | `-29.28%` | `226.60` |
| `Live` | `Long` | `0.6725` | 400,340.00 USD | 0.00 USD | 63,890.00 USD | `-27.89%` | `95,000.00` |
| `Live` | `Long` | `0.6745` | 336,450.00 USD | 0.00 USD | 84,310.00 USD | `-27.67%` | `125,000.00` |
| `Live` | `Long` | `0.6775` | 252,140.00 USD | 0.00 USD | 423.10 USD | `-27.35%` | `624.50` |
| `Live` | `Long` | `0.6835` | 251,720.00 USD | 0.00 USD | 512.97 USD | `-26.71%` | `750.50` |
| `Live` | `Long` | `0.6915` | 251,200.00 USD | 0.00 USD | 19,800.00 USD | `-25.85%` | `28,635.00` |
| `Live` | `Long` | `0.6965` | 231,400.00 USD | 0.00 USD | 322.62 USD | `-25.31%` | `463.20` |
| `Live` | `Long` | `0.7005` | 231,080.00 USD | 0.00 USD | 1,140.00 USD | `-24.88%` | `1,634.20` |
| `Live` | `Long` | `0.7115` | 229,930.00 USD | 0.00 USD | 158.95 USD | `-23.70%` | `223.40` |
| `Live` | `Long` | `0.7145` | 229,780.00 USD | 0.00 USD | 988.87 USD | `-23.38%` | `1,384.00` |
| `Live` | `Long` | `0.7215` | 228,790.00 USD | 0.00 USD | 1,580.00 USD | `-22.63%` | `2,190.90` |
| `Live` | `Long` | `0.7235` | 227,210.00 USD | 0.00 USD | 397.93 USD | `-22.42%` | `550.00` |
| `Live` | `Long` | `0.7295` | 226,810.00 USD | 0.00 USD | 291.58 USD | `-21.77%` | `399.70` |
| `Live` | `Long` | `0.7305` | 226,520.00 USD | 0.00 USD | 2,300.00 USD | `-21.67%` | `3,143.00` |
| `Live` | `Long` | `0.7335` | 224,220.00 USD | 0.00 USD | 1,140.00 USD | `-21.34%` | `1,557.80` |
| `Live` | `Long` | `0.7395` | 223,080.00 USD | 0.00 USD | 283.30 USD | `-20.70%` | `383.10` |
| `Live` | `Long` | `0.7515` | 222,790.00 USD | 0.00 USD | 32,890.00 USD | `-19.41%` | `43,766.90` |
| `Live` | `Long` | `0.7525` | 189,900.00 USD | 0.00 USD | 2,800.00 USD | `-19.31%` | `3,717.20` |
| `Live` | `Long` | `0.7535` | 187,110.00 USD | 0.00 USD | 629.25 USD | `-19.20%` | `835.10` |
| `Live` | `Long` | `0.7555` | 186,480.00 USD | 0.00 USD | 144.07 USD | `-18.98%` | `190.70` |
| `Live` | `Long` | `0.7565` | 186,330.00 USD | 0.00 USD | 8,860.00 USD | `-18.88%` | `11,712.10` |
| `Live` | `Long` | `0.7615` | 177,470.00 USD | 0.00 USD | 54,070.00 USD | `-18.34%` | `71,003.30` |
| `Live` | `Long` | `0.7635` | 123,400.00 USD | 0.00 USD | 308.00 USD | `-18.13%` | `403.40` |
| `Live` | `Long` | `0.7705` | 123,100.00 USD | 0.00 USD | 152.94 USD | `-17.38%` | `198.50` |
| `Live` | `Long` | `0.7725` | 122,940.00 USD | 0.00 USD | 3,840.00 USD | `-17.16%` | `4,968.90` |
| `Live` | `Long` | `0.7775` | 119,100.00 USD | 0.00 USD | 2,490.00 USD | `-16.63%` | `3,199.30` |
| `Live` | `Long` | `0.7865` | 116,620.00 USD | 0.00 USD | 156.51 USD | `-15.66%` | `199.00` |
| `Live` | `Long` | `0.7905` | 116,460.00 USD | 0.00 USD | 277.39 USD | `-15.23%` | `350.90` |
| `Live` | `Long` | `0.7935` | 116,180.00 USD | 0.00 USD | 1,760.00 USD | `-14.91%` | `2,214.10` |
| `Live` | `Long` | `0.7985` | 114,430.00 USD | 0.00 USD | 210.40 USD | `-14.37%` | `263.50` |
| `Live` | `Long` | `0.8135` | 114,220.00 USD | 0.00 USD | 647.79 USD | `-12.77%` | `796.30` |
| `Live` | `Long` | `0.8215` | 113,570.00 USD | 0.00 USD | 1,950.00 USD | `-11.91%` | `2,370.70` |
| `Live` | `Long` | `0.8235` | 111,620.00 USD | 0.00 USD | 749.96 USD | `-11.69%` | `910.70` |
| `Live` | `Long` | `0.8365` | 110,870.00 USD | 0.00 USD | 316.70 USD | `-10.30%` | `378.60` |
| `Live` | `Long` | `0.8415` | 110,550.00 USD | 0.00 USD | 1,570.00 USD | `-9.76%` | `1,862.40` |
| `Live` | `Long` | `0.8495` | 108,990.00 USD | 0.00 USD | 1,260.00 USD | `-8.90%` | `1,486.90` |
| `Live` | `Long` | `0.8575` | 107,720.00 USD | 0.00 USD | 620.32 USD | `-8.05%` | `723.40` |
| `Live` | `Long` | `0.8635` | 107,100.00 USD | 0.00 USD | 208.02 USD | `-7.40%` | `240.90` |
| `Live` | `Long` | `0.8645` | 106,900.00 USD | 0.00 USD | 438.30 USD | `-7.30%` | `507.00` |
| `Live` | `Long` | `0.8665` | 106,460.00 USD | 0.00 USD | 1,390.00 USD | `-7.08%` | `1,606.10` |
| `Live` | `Long` | `0.8695` | 105,070.00 USD | 0.00 USD | 12,590.00 USD | `-6.76%` | `14,478.80` |
| `Live` | `Long` | `0.8705` | 92,480.00 USD | 0.00 USD | 92,480.00 USD | `-6.65%` | `106,233.40` |
| `Live` | `Short` | `0.9805` | 102.95 USD | 102.95 USD | 0.00 USD | `+5.14%` | `105.00` |
| `Live` | `Short` | `0.9925` | 4,040.00 USD | 3,940.00 USD | 0.00 USD | `+6.43%` | `3,970.40` |
| `Live` | `Short` | `0.9985` | 4,900.00 USD | 852.22 USD | 0.00 USD | `+7.07%` | `853.50` |
| `Live` | `Short` | `1.02` | 5,660.00 USD | 760.04 USD | 0.00 USD | `+9.33%` | `745.50` |
| `Live` | `Short` | `1.03` | 5,810.00 USD | 152.32 USD | 0.00 USD | `+10.29%` | `148.10` |
| `Live` | `Short` | `1.03` | 6,030.00 USD | 221.28 USD | 0.00 USD | `+10.93%` | `213.90` |
| `Live` | `Short` | `1.04` | 6,210.00 USD | 182.19 USD | 0.00 USD | `+11.58%` | `175.10` |
| `Live` | `Short` | `1.05` | 6,580.00 USD | 367.04 USD | 0.00 USD | `+12.33%` | `350.40` |
| `Live` | `Short` | `1.08` | 8,810.00 USD | 2,230.00 USD | 0.00 USD | `+15.97%` | `2,064.20` |
| `Live` | `Short` | `1.11` | 8,980.00 USD | 170.02 USD | 0.00 USD | `+19.08%` | `153.10` |
| `Live` | `Short` | `1.15` | 22,450.00 USD | 13,470.00 USD | 0.00 USD | `+23.16%` | `11,730.60` |
| `Live` | `Short` | `1.31` | 22,580.00 USD | 126.85 USD | 0.00 USD | `+40.96%` | `96.50` |
| `Live` | `Short` | `1.32` | 34,310.00 USD | 11,730.00 USD | 0.00 USD | `+41.92%` | `8,862.90` |
| `Live` | `Short` | `1.34` | 34,550.00 USD | 239.77 USD | 0.00 USD | `+43.64%` | `179.00` |
| `Live` | `Short` | `1.37` | 38,430.00 USD | 3,880.00 USD | 0.00 USD | `+46.64%` | `2,834.10` |
| `Live` | `Short` | `1.42` | 41,620.00 USD | 3,200.00 USD | 0.00 USD | `+52.33%` | `2,249.30` |
| `Live` | `Short` | `1.54` | 41,800.00 USD | 176.42 USD | 0.00 USD | `+65.52%` | `114.30` |
| `Live` | `Short` | `1.55` | 41,920.00 USD | 123.26 USD | 0.00 USD | `+66.27%` | `79.50` |
| `Live` | `Short` | `1.56` | 43,730.00 USD | 1,810.00 USD | 0.00 USD | `+66.91%` | `1,161.90` |
| `Live` | `Short` | `1.59` | 44,520.00 USD | 791.80 USD | 0.00 USD | `+70.02%` | `499.40` |
| `Live` | `Short` | `1.59` | 123,560.00 USD | 79,040.00 USD | 0.00 USD | `+70.34%` | `49,759.80` |
| `Live` | `Short` | `1.63` | 126,000.00 USD | 2,440.00 USD | 0.00 USD | `+74.31%` | `1,500.00` |
| `Live` | `Short` | `1.63` | 126,240.00 USD | 237.96 USD | 0.00 USD | `+74.42%` | `146.30` |
| `Live` | `Short` | `1.65` | 134,480.00 USD | 8,240.00 USD | 0.00 USD | `+76.67%` | `5,000.00` |
| `Live` | `Short` | `1.66` | 134,800.00 USD | 318.07 USD | 0.00 USD | `+77.74%` | `191.90` |
| `Live` | `Short` | `1.67` | 135,100.00 USD | 300.15 USD | 0.00 USD | `+78.81%` | `180.00` |
| `Live` | `Short` | `1.73` | 135,290.00 USD | 190.42 USD | 0.00 USD | `+85.46%` | `110.10` |
| `Live` | `Short` | `1.74` | 148,430.00 USD | 13,140.00 USD | 0.00 USD | `+86.21%` | `7,569.10` |
| `Live` | `Short` | `1.75` | 149,080.00 USD | 647.64 USD | 0.00 USD | `+87.50%` | `370.40` |
| `Live` | `Short` | `1.77` | 149,460.00 USD | 380.81 USD | 0.00 USD | `+90.29%` | `214.60` |
| `Live` | `Short` | `1.86` | 149,670.00 USD | 208.37 USD | 0.00 USD | `+98.97%` | `112.30` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.4015` | 356,970.00 USD | 0.00 USD | 120.45 USD | `-56.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 356,850.00 USD | 0.00 USD | 150.15 USD | `-46.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5435` | 356,700.00 USD | 0.00 USD | 186.15 USD | `-41.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 356,510.00 USD | 0.00 USD | 1,150.00 USD | `-29.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 355,360.00 USD | 0.00 USD | 781.90 USD | `-24.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 354,580.00 USD | 0.00 USD | 477.38 USD | `-23.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 354,100.00 USD | 0.00 USD | 341.33 USD | `-22.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 353,760.00 USD | 0.00 USD | 972.82 USD | `-22.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 352,790.00 USD | 0.00 USD | 160.20 USD | `-21.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7385` | 352,630.00 USD | 0.00 USD | 102.58 USD | `-20.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 352,530.00 USD | 0.00 USD | 289.49 USD | `-19.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7615` | 352,240.00 USD | 0.00 USD | 197.53 USD | `-18.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 352,040.00 USD | 0.00 USD | 14,570.00 USD | `-16.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 337,470.00 USD | 0.00 USD | 213.58 USD | `-15.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 337,260.00 USD | 0.00 USD | 274,830.00 USD | `-14.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 62,420.00 USD | 0.00 USD | 108.47 USD | `-14.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8025` | 62,320.00 USD | 0.00 USD | 2,010.00 USD | `-13.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 60,300.00 USD | 0.00 USD | 326.96 USD | `-13.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 59,980.00 USD | 0.00 USD | 405.75 USD | `-12.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 59,570.00 USD | 0.00 USD | 772.84 USD | `-10.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8415` | 58,800.00 USD | 0.00 USD | 2,670.00 USD | `-9.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8495` | 56,130.00 USD | 0.00 USD | 3,470.00 USD | `-8.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 52,660.00 USD | 0.00 USD | 9,180.00 USD | `-8.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 43,480.00 USD | 0.00 USD | 341.94 USD | `-8.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 43,130.00 USD | 0.00 USD | 1,150.00 USD | `-8.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 41,990.00 USD | 0.00 USD | 429.25 USD | `-7.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 41,560.00 USD | 0.00 USD | 223.30 USD | `-7.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 41,330.00 USD | 0.00 USD | 518.51 USD | `-7.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 40,820.00 USD | 0.00 USD | 128.39 USD | `-6.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 40,690.00 USD | 0.00 USD | 1,280.00 USD | `-6.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 39,410.00 USD | 0.00 USD | 205.24 USD | `-6.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 39,200.00 USD | 0.00 USD | 649.66 USD | `-6.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 38,550.00 USD | 0.00 USD | 194.06 USD | `-5.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8845` | 38,360.00 USD | 0.00 USD | 193.35 USD | `-5.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 38,170.00 USD | 0.00 USD | 223.04 USD | `-4.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 37,940.00 USD | 0.00 USD | 10,840.00 USD | `-4.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 27,100.00 USD | 0.00 USD | 4,920.00 USD | `-4.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8915` | 22,180.00 USD | 0.00 USD | 121.15 USD | `-4.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 22,060.00 USD | 0.00 USD | 192.07 USD | `-4.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 21,870.00 USD | 0.00 USD | 195.32 USD | `-4.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8955` | 21,670.00 USD | 0.00 USD | 575.72 USD | `-3.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8965` | 21,100.00 USD | 0.00 USD | 196.87 USD | `-3.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8975` | 20,900.00 USD | 0.00 USD | 191.98 USD | `-3.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8985` | 20,710.00 USD | 0.00 USD | 2,870.00 USD | `-3.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9005` | 17,840.00 USD | 0.00 USD | 385.95 USD | `-3.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9025` | 17,450.00 USD | 0.00 USD | 398.91 USD | `-3.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9035` | 17,050.00 USD | 0.00 USD | 196.96 USD | `-3.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9045` | 16,850.00 USD | 0.00 USD | 300.38 USD | `-3.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9065` | 16,550.00 USD | 0.00 USD | 198.61 USD | `-2.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9075` | 16,350.00 USD | 0.00 USD | 994.35 USD | `-2.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 15,360.00 USD | 0.00 USD | 363.40 USD | `-2.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9095` | 15,000.00 USD | 0.00 USD | 1,810.00 USD | `-2.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9115` | 13,190.00 USD | 0.00 USD | 397.23 USD | `-2.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9135` | 12,790.00 USD | 0.00 USD | 398.65 USD | `-2.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9145` | 12,390.00 USD | 0.00 USD | 399.09 USD | `-1.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9155` | 12,000.00 USD | 0.00 USD | 403.92 USD | `-1.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9165` | 11,590.00 USD | 0.00 USD | 198.06 USD | `-1.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9175` | 11,390.00 USD | 0.00 USD | 223.78 USD | `-1.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9185` | 11,170.00 USD | 0.00 USD | 899.85 USD | `-1.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9195` | 10,270.00 USD | 0.00 USD | 900.19 USD | `-1.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 9,370.00 USD | 0.00 USD | 2,920.00 USD | `-1.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9215` | 6,450.00 USD | 0.00 USD | 104.68 USD | `-1.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9225` | 6,340.00 USD | 0.00 USD | 201.94 USD | `-1.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9235` | 6,140.00 USD | 0.00 USD | 1,080.00 USD | `-0.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9245` | 5,060.00 USD | 0.00 USD | 201.45 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9255` | 4,850.00 USD | 0.00 USD | 817.40 USD | `-0.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9265` | 4,040.00 USD | 0.00 USD | 403.77 USD | `-0.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9275` | 3,630.00 USD | 0.00 USD | 2,120.00 USD | `-0.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9285` | 1,520.00 USD | 0.00 USD | 397.96 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9295` | 1,120.00 USD | 0.00 USD | 407.49 USD | `-0.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9305` | 709.75 USD | 0.00 USD | 203.97 USD | `-0.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9315` | 505.78 USD | 0.00 USD | 263.80 USD | `-0.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9325` | 241.98 USD | 0.00 USD | 241.98 USD | `-0.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 814.76 USD | 814.76 USD | 0.00 USD | `+0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 1,020.00 USD | 201.97 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 10,700.00 USD | 9,680.00 USD | 0.00 USD | `+0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 11,120.00 USD | 416.01 USD | 0.00 USD | `+0.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 11,670.00 USD | 555.18 USD | 0.00 USD | `+0.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9415` | 12,670.00 USD | 997.80 USD | 0.00 USD | `+0.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 13,490.00 USD | 816.96 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 17,230.00 USD | 3,750.00 USD | 0.00 USD | `+1.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 44,650.00 USD | 27,420.00 USD | 0.00 USD | `+1.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 45,030.00 USD | 383.87 USD | 0.00 USD | `+1.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 45,170.00 USD | 140.18 USD | 0.00 USD | `+1.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 74,100.00 USD | 28,930.00 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 74,520.00 USD | 414.68 USD | 0.00 USD | `+1.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9525` | 74,900.00 USD | 381.00 USD | 0.00 USD | `+2.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 75,310.00 USD | 408.67 USD | 0.00 USD | `+2.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9545` | 75,720.00 USD | 408.72 USD | 0.00 USD | `+2.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 79,510.00 USD | 3,790.00 USD | 0.00 USD | `+2.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 79,920.00 USD | 409.96 USD | 0.00 USD | `+2.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 80,060.00 USD | 136.83 USD | 0.00 USD | `+2.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 80,320.00 USD | 261.16 USD | 0.00 USD | `+3.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9615` | 80,730.00 USD | 412.10 USD | 0.00 USD | `+3.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 82,640.00 USD | 1,910.00 USD | 0.00 USD | `+3.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 83,210.00 USD | 568.75 USD | 0.00 USD | `+3.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 83,570.00 USD | 364.58 USD | 0.00 USD | `+3.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 83,780.00 USD | 206.91 USD | 0.00 USD | `+3.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 84,600.00 USD | 824.91 USD | 0.00 USD | `+3.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 84,810.00 USD | 206.95 USD | 0.00 USD | `+3.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 86,840.00 USD | 2,030.00 USD | 0.00 USD | `+3.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 88,400.00 USD | 1,560.00 USD | 0.00 USD | `+4.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 88,790.00 USD | 387.83 USD | 0.00 USD | `+4.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 89,620.00 USD | 830.10 USD | 0.00 USD | `+4.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 90,010.00 USD | 396.17 USD | 0.00 USD | `+4.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 90,690.00 USD | 676.53 USD | 0.00 USD | `+4.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 90,790.00 USD | 102.95 USD | 0.00 USD | `+5.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 92,820.00 USD | 2,030.00 USD | 0.00 USD | `+5.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 93,160.00 USD | 346.13 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 93,420.00 USD | 255.38 USD | 0.00 USD | `+5.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 93,640.00 USD | 223.91 USD | 0.00 USD | `+5.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9865` | 93,750.00 USD | 109.99 USD | 0.00 USD | `+5.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 97,270.00 USD | 3,520.00 USD | 0.00 USD | `+6.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 129,030.00 USD | 31,750.00 USD | 0.00 USD | `+6.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 129,430.00 USD | 403.06 USD | 0.00 USD | `+6.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 134,570.00 USD | 5,140.00 USD | 0.00 USD | `+6.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 171,880.00 USD | 37,310.00 USD | 0.00 USD | `+7.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 172,380.00 USD | 500.25 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 212,980.00 USD | 40,590.00 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 213,210.00 USD | 235.79 USD | 0.00 USD | `+7.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 214,560.00 USD | 1,340.00 USD | 0.00 USD | `+7.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 214,790.00 USD | 230.39 USD | 0.00 USD | `+7.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 214,910.00 USD | 127.65 USD | 0.00 USD | `+8.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 215,090.00 USD | 176.59 USD | 0.00 USD | `+8.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 215,500.00 USD | 409.86 USD | 0.00 USD | `+8.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 215,610.00 USD | 110.95 USD | 0.00 USD | `+8.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 216,230.00 USD | 615.60 USD | 0.00 USD | `+8.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 216,790.00 USD | 561.17 USD | 0.00 USD | `+8.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 217,000.00 USD | 214.40 USD | 0.00 USD | `+9.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 217,250.00 USD | 249.88 USD | 0.00 USD | `+9.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 217,460.00 USD | 207.97 USD | 0.00 USD | `+9.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 217,670.00 USD | 208.26 USD | 0.00 USD | `+10.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 218,180.00 USD | 516.75 USD | 0.00 USD | `+10.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 218,530.00 USD | 348.86 USD | 0.00 USD | `+11.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 218,930.00 USD | 391.80 USD | 0.00 USD | `+11.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 219,340.00 USD | 413.76 USD | 0.00 USD | `+11.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 219,690.00 USD | 354.91 USD | 0.00 USD | `+11.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 221,600.00 USD | 1,900.00 USD | 0.00 USD | `+11.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 221,810.00 USD | 207.87 USD | 0.00 USD | `+11.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 222,010.00 USD | 207.97 USD | 0.00 USD | `+11.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 222,120.00 USD | 107.99 USD | 0.00 USD | `+12.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 296,960.00 USD | 74,840.00 USD | 0.00 USD | `+13.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 299,130.00 USD | 2,170.00 USD | 0.00 USD | `+17.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 300,670.00 USD | 1,540.00 USD | 0.00 USD | `+17.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 310,590.00 USD | 9,930.00 USD | 0.00 USD | `+17.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 311,470.00 USD | 877.63 USD | 0.00 USD | `+19.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 311,640.00 USD | 171.09 USD | 0.00 USD | `+19.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 314,410.00 USD | 2,770.00 USD | 0.00 USD | `+20.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 316,450.00 USD | 2,040.00 USD | 0.00 USD | `+20.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 316,620.00 USD | 172.17 USD | 0.00 USD | `+20.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 316,790.00 USD | 172.32 USD | 0.00 USD | `+21.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 316,980.00 USD | 187.72 USD | 0.00 USD | `+21.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 317,170.00 USD | 188.39 USD | 0.00 USD | `+21.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 319,840.00 USD | 2,670.00 USD | 0.00 USD | `+21.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 320,010.00 USD | 174.23 USD | 0.00 USD | `+21.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 320,180.00 USD | 174.38 USD | 0.00 USD | `+21.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 320,360.00 USD | 174.84 USD | 0.00 USD | `+22.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 320,510.00 USD | 150.90 USD | 0.00 USD | `+23.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 320,660.00 USD | 151.03 USD | 0.00 USD | `+23.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 320,810.00 USD | 151.16 USD | 0.00 USD | `+23.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 322,860.00 USD | 2,050.00 USD | 0.00 USD | `+24.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 322,970.00 USD | 110.00 USD | 0.00 USD | `+25.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 323,450.00 USD | 475.80 USD | 0.00 USD | `+27.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 324,650.00 USD | 1,210.00 USD | 0.00 USD | `+28.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 367,580.00 USD | 42,930.00 USD | 0.00 USD | `+29.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 369,580.00 USD | 2,000.00 USD | 0.00 USD | `+32.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 370,970.00 USD | 1,380.00 USD | 0.00 USD | `+34.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 371,210.00 USD | 245.41 USD | 0.00 USD | `+36.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 379,610.00 USD | 8,390.00 USD | 0.00 USD | `+38.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 380,020.00 USD | 415.25 USD | 0.00 USD | `+39.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 386,540.00 USD | 6,520.00 USD | 0.00 USD | `+39.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 391,340.00 USD | 4,800.00 USD | 0.00 USD | `+40.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 391,990.00 USD | 655.75 USD | 0.00 USD | `+40.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 392,590.00 USD | 596.43 USD | 0.00 USD | `+42.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 394,400.00 USD | 1,810.00 USD | 0.00 USD | `+43.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 408,290.00 USD | 13,880.00 USD | 0.00 USD | `+43.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 409,540.00 USD | 1,250.00 USD | 0.00 USD | `+45.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 411,610.00 USD | 2,070.00 USD | 0.00 USD | `+49.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 411,750.00 USD | 140.05 USD | 0.00 USD | `+50.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 411,910.00 USD | 160.42 USD | 0.00 USD | `+50.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 412,860.00 USD | 954.32 USD | 0.00 USD | `+51.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 447,040.00 USD | 34,170.00 USD | 0.00 USD | `+53.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 447,920.00 USD | 879.84 USD | 0.00 USD | `+59.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 450,970.00 USD | 3,050.00 USD | 0.00 USD | `+62.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 451,270.00 USD | 297.27 USD | 0.00 USD | `+66.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 459,800.00 USD | 8,530.00 USD | 0.00 USD | `+77.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 459,940.00 USD | 143.99 USD | 0.00 USD | `+78.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 460,120.00 USD | 177.05 USD | 0.00 USD | `+89.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 460,550.00 USD | 431.40 USD | 0.00 USD | `+93.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 460,770.00 USD | 220.77 USD | 0.00 USD | `+95.01%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7870` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 5,920.00 USD | 4,300.00 USD | 630.79 USD |
| `7D` | `0.7890` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 88.75 USD | 0.00 USD | 2,110.00 USD |
| `7D` | `0.7910` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD |
| `7D` | `0.7930` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 20,360.00 USD | 1,560.00 USD | 6,130.00 USD |
| `7D` | `0.7950` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 3,290.00 USD | 8,430.00 USD | 14,710.00 USD |
| `7D` | `0.7970` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 10,100.00 USD | 1,130.00 USD | 522.30 USD |
| `7D` | `0.7990` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 20,360.00 USD | 6,180.00 USD | 13,950.00 USD |
| `7D` | `0.8010` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 5,420.00 USD | 5,300.00 USD | 2,300.00 USD |
| `7D` | `0.8030` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 4,550.00 USD | 2,440.00 USD | 10,410.00 USD |
| `7D` | `0.8050` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD |
| `7D` | `0.8070` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 12,160.00 USD | 4,660.00 USD | 16,650.00 USD |
| `7D` | `0.8090` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD |
| `7D` | `0.8110` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD |
| `7D` | `0.8130` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 14,060.00 USD | 2,970.00 USD | 9,350.00 USD |
| `7D` | `0.8150` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 61,120.00 USD | 7,590.00 USD | 19,500.00 USD |
| `7D` | `0.8170` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 10,780.00 USD | 8,770.00 USD | 9,670.00 USD |
| `7D` | `0.8190` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD |
| `7D` | `0.8210` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 7,510.00 USD | 3,290.00 USD | 10,030.00 USD |
| `7D` | `0.8230` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 29,430.00 USD | 5,100.00 USD | 13,220.00 USD |
| `7D` | `0.8250` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD |
| `7D` | `0.8270` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 4,320.00 USD | 5,770.00 USD | 616.76 USD |
| `7D` | `0.8290` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD |
| `7D` | `0.8310` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 9,280.00 USD | 1,660.00 USD | 2,450.00 USD |
| `7D` | `0.8330` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 16,220.00 USD | 11,360.00 USD | 77.95 USD |
| `7D` | `0.8350` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 19,490.00 USD | 0.00 USD | 2,290.00 USD |
| `1D` | `0.8370` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 18,140.00 USD | 2,530.00 USD | 20,310.00 USD |
| `7D` | `0.8370` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 15,240.00 USD | 1,480.00 USD | 0.00 USD |
| `1D` | `0.8390` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 1,740.00 USD | 745.84 USD | 2,010.00 USD |
| `7D` | `0.8390` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD |
| `1D` | `0.8410` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 1,470.00 USD | 2,040.00 USD | 1,780.00 USD |
| `7D` | `0.8410` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 270.00 USD | 3,280.00 USD | 0.00 USD |
| `1D` | `0.8430` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 4,540.00 USD | 6,880.00 USD | 1,150.00 USD |
| `7D` | `0.8430` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 11,320.00 USD | 3,840.00 USD | 4,060.00 USD |
| `1D` | `0.8450` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 2,360.00 USD | 7,850.00 USD | 429.42 USD |
| `7D` | `0.8450` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 1,980.00 USD | 404.64 USD | 474.61 USD |
| `1D` | `0.8470` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 24,110.00 USD | 1,110.00 USD | 165.77 USD |
| `7D` | `0.8470` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 7,900.00 USD | 1,730.00 USD | 2,390.00 USD |
| `1D` | `0.8490` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 5,120.00 USD | 2,400.00 USD | 7,940.00 USD |
| `7D` | `0.8490` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 22,370.00 USD | 9,610.00 USD | 0.00 USD |
| `1D` | `0.8510` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 13,560.00 USD | 4,140.00 USD | 16,720.00 USD |
| `7D` | `0.8510` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 14,280.00 USD | 991.53 USD | 21,470.00 USD |
| `1D` | `0.8530` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 4,680.00 USD | 3,830.00 USD | 5,510.00 USD |
| `7D` | `0.8530` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD |
| `1D` | `0.8550` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 18,270.00 USD | 3,040.00 USD | 5,090.00 USD |
| `7D` | `0.8550` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD |
| `1D` | `0.8570` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 989.11 USD | 1,720.00 USD | 6,150.00 USD |
| `7D` | `0.8570` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 3,540.00 USD | 944.22 USD | 8,450.00 USD |
| `1D` | `0.8590` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 6,870.00 USD | 10,640.00 USD | 6,420.00 USD |
| `7D` | `0.8590` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 3,730.00 USD | 0.00 USD | 1,560.00 USD |
| `1D` | `0.8610` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 8,320.00 USD | 855.53 USD | 16,460.00 USD |
| `7D` | `0.8610` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 9,960.00 USD | 3,660.00 USD | 35,340.00 USD |
| `1D` | `0.8630` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 39,330.00 USD | 12,290.00 USD | 2,010.00 USD |
| `7D` | `0.8630` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 758.91 USD | 2,910.00 USD | 1,280.00 USD |
| `1D` | `0.8650` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 17,640.00 USD | 2,110.00 USD | 1,790.00 USD |
| `7D` | `0.8650` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 47,860.00 USD | 18,930.00 USD | 184.85 USD |
| `1D` | `0.8670` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 12,000.00 USD | 10,090.00 USD | 1,110.00 USD |
| `7D` | `0.8670` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 13,660.00 USD | 3,720.00 USD | 12,140.00 USD |
| `1D` | `0.8690` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 42,010.00 USD | 3,780.00 USD | 29,400.00 USD |
| `7D` | `0.8690` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 160,750.00 USD | 13,110.00 USD | 46,230.00 USD |
| `1D` | `0.8710` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 42,290.00 USD | 24,900.00 USD | 28,630.00 USD |
| `7D` | `0.8710` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 7,370.00 USD | 23,340.00 USD | 13,110.00 USD |
| `1D` | `0.8730` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 54,500.00 USD | 21,510.00 USD | 25,960.00 USD |
| `7D` | `0.8730` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 0.00 USD | 8,170.00 USD | 295.31 USD |
| `1D` | `0.8750` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 36,600.00 USD | 6,900.00 USD | 17,890.00 USD |
| `7D` | `0.8750` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 0.00 USD | 6,380.00 USD | 8,950.00 USD |
| `1D` | `0.8770` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 10,480.00 USD | 152.79 USD | 0.00 USD |
| `7D` | `0.8770` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 1,390.00 USD | 0.00 USD | 30,820.00 USD |
| `1D` | `0.8790` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 0.00 USD | 40.93 USD | 50,910.00 USD |
| `7D` | `0.8790` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 873.30 USD | 5,580.00 USD | 53,860.00 USD |
| `1D` | `0.8810` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 13,820.00 USD | 5,210.00 USD | 2,430.00 USD |
| `7D` | `0.8810` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 1,830.00 USD | 240.78 USD | 0.00 USD |
| `1D` | `0.8830` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 656.20 USD | 5,570.00 USD | 0.00 USD |
| `7D` | `0.8830` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 2,320.00 USD | 10,140.00 USD | 11,710.00 USD |
| `1D` | `0.8850` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 5,680.00 USD | 34,880.00 USD | 11,180.00 USD |
| `7D` | `0.8850` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 0.00 USD | 5,800.00 USD | 3,970.00 USD |
| `1D` | `0.8870` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 68,710.00 USD | 17,740.00 USD | 32,750.00 USD |
| `7D` | `0.8870` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 271,870.00 USD | 22,320.00 USD | 81,590.00 USD |
| `1D` | `0.8890` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 69,610.00 USD | 40,830.00 USD | 4,860.00 USD |
| `7D` | `0.8890` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 54,380.00 USD | 73,890.00 USD | 13,880.00 USD |
| `1D` | `0.8910` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 2,150.00 USD | 38,730.00 USD | 20,080.00 USD |
| `7D` | `0.8910` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 75,300.00 USD | 22,240.00 USD | 34,270.00 USD |
| `1D` | `0.8930` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 56,810.00 USD | 24,630.00 USD | 37,920.00 USD |
| `7D` | `0.8930` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 62,870.00 USD | 23,560.00 USD | 9,170.00 USD |
| `1D` | `0.8950` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 6,700.00 USD | 15,420.00 USD | 8,160.00 USD |
| `7D` | `0.8950` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 7,120.00 USD | 37,670.00 USD | 57,420.00 USD |
| `1D` | `0.8970` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 8,300.00 USD | 28,440.00 USD | 19,060.00 USD |
| `7D` | `0.8970` | 973,990.00 USD | 0.00 USD | 973,990.00 USD | 2,140.00 USD | 11,010.00 USD | 56,560.00 USD |
| `1D` | `0.8990` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 3,650.00 USD | 24,130.00 USD | 4,200.00 USD |
| `7D` | `0.8990` | 904,290.00 USD | 0.00 USD | 904,290.00 USD | 0.00 USD | 34,220.00 USD | 0.00 USD |
| `1D` | `0.9010` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 5,490.00 USD | 26,220.00 USD | 4,980.00 USD |
| `7D` | `0.9010` | 870,070.00 USD | 0.00 USD | 870,070.00 USD | 0.00 USD | 48,840.00 USD | 0.00 USD |
| `1D` | `0.9030` | 990,890.00 USD | 0.00 USD | 990,890.00 USD | 8,980.00 USD | 17,560.00 USD | 18,230.00 USD |
| `7D` | `0.9030` | 821,230.00 USD | 0.00 USD | 821,230.00 USD | 0.00 USD | 16,370.00 USD | 23,930.00 USD |
| `1D` | `0.9050` | 946,120.00 USD | 0.00 USD | 946,120.00 USD | 19,330.00 USD | 11,600.00 USD | 22,050.00 USD |
| `7D` | `0.9050` | 780,930.00 USD | 0.00 USD | 780,930.00 USD | 0.00 USD | 3,840.00 USD | 0.00 USD |
| `1D` | `0.9070` | 893,130.00 USD | 0.00 USD | 893,130.00 USD | 36,650.00 USD | 8,370.00 USD | 33,510.00 USD |
| `7D` | `0.9070` | 777,090.00 USD | 0.00 USD | 777,090.00 USD | 23,910.00 USD | 0.00 USD | 42,040.00 USD |
| `1D` | `0.9090` | 814,600.00 USD | 0.00 USD | 814,600.00 USD | 7,100.00 USD | 9,080.00 USD | 239.84 USD |
| `1D` | `0.9110` | 798,180.00 USD | 0.00 USD | 798,180.00 USD | 25,560.00 USD | 2,850.00 USD | 2,080.00 USD |
| `1D` | `0.9130` | 767,690.00 USD | 0.00 USD | 767,690.00 USD | 17,080.00 USD | 9,480.00 USD | 22,310.00 USD |
| `7D` | `0.9130` | 711,140.00 USD | 0.00 USD | 711,140.00 USD | 0.00 USD | 0.00 USD | 20,720.00 USD |
| `1D` | `0.9150` | 718,810.00 USD | 0.00 USD | 718,810.00 USD | 11,120.00 USD | 17,780.00 USD | 24,660.00 USD |
| `7D` | `0.9150` | 690,420.00 USD | 0.00 USD | 690,420.00 USD | 0.00 USD | 12,890.00 USD | 16,130.00 USD |
| `1D` | `0.9170` | 665,260.00 USD | 0.00 USD | 665,260.00 USD | 7,300.00 USD | 16,660.00 USD | 15,050.00 USD |
| `7D` | `0.9170` | 661,400.00 USD | 0.00 USD | 661,400.00 USD | 0.00 USD | 0.00 USD | 33,180.00 USD |
| `1D` | `0.9190` | 626,250.00 USD | 0.00 USD | 626,250.00 USD | 9,900.00 USD | 10,760.00 USD | 12,110.00 USD |
| `1D` | `0.9210` | 593,480.00 USD | 0.00 USD | 593,480.00 USD | 12,850.00 USD | 3,680.00 USD | 6,020.00 USD |
| `7D` | `0.9210` | 628,210.00 USD | 0.00 USD | 628,210.00 USD | 0.00 USD | 7,760.00 USD | 3,970.00 USD |
| `1D` | `0.9230` | 570,920.00 USD | 0.00 USD | 570,920.00 USD | 6,600.00 USD | 7,140.00 USD | 21,700.00 USD |
| `7D` | `0.9230` | 616,490.00 USD | 0.00 USD | 616,490.00 USD | 294,370.00 USD | 0.00 USD | 26,680.00 USD |
| `1D` | `0.9250` | 535,490.00 USD | 0.00 USD | 535,490.00 USD | 99,970.00 USD | 63,270.00 USD | 62,530.00 USD |
| `7D` | `0.9250` | 295,440.00 USD | 0.00 USD | 295,440.00 USD | 0.00 USD | 52,780.00 USD | 84,070.00 USD |
| `1D` | `0.9270` | 309,720.00 USD | 0.00 USD | 309,720.00 USD | 39,920.00 USD | 7,040.00 USD | 73,810.00 USD |
| `7D` | `0.9270` | 158,580.00 USD | 0.00 USD | 158,580.00 USD | 44,020.00 USD | 11,800.00 USD | 0.00 USD |
| `1D` | `0.9290` | 188,950.00 USD | 0.00 USD | 188,950.00 USD | 80,950.00 USD | 20,440.00 USD | 38,560.00 USD |
| `7D` | `0.9290` | 102,770.00 USD | 0.00 USD | 102,770.00 USD | 0.00 USD | 12,750.00 USD | 1,600.00 USD |
| `1D` | `0.9310` | 48,990.00 USD | 0.00 USD | 48,990.00 USD | 0.00 USD | 7,130.00 USD | 5,410.00 USD |
| `1D` | `0.9330` | 36,460.00 USD | 0.00 USD | 36,460.00 USD | 3,720.00 USD | 6,140.00 USD | 26,590.00 USD |
| `7D` | `0.9330` | 88,410.00 USD | 0.00 USD | 88,410.00 USD | 37,450.00 USD | 0.00 USD | 31,370.00 USD |
| `1D` | `0.9350` | 36,730.00 USD | 36,730.00 USD | 0.00 USD | 36,510.00 USD | 221.86 USD | 0.00 USD |
| `1D` | `0.9350` | 73,460.00 USD | 73,460.00 USD | 0.00 USD | 36,510.00 USD | 221.86 USD | 0.00 USD |
| `7D` | `0.9350` | 19,600.00 USD | 0.00 USD | 19,600.00 USD | 0.00 USD | 0.00 USD | 19,600.00 USD |
| `7D` | `0.9360` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9370` | 74,500.00 USD | 74,500.00 USD | 0.00 USD | 0.00 USD | 182.01 USD | 852.35 USD |
| `7D` | `0.9370` | 84,400.00 USD | 84,400.00 USD | 0.00 USD | 16,340.00 USD | 19,540.00 USD | 48,530.00 USD |
| `1D` | `0.9390` | 76,150.00 USD | 76,150.00 USD | 0.00 USD | 1,340.00 USD | 309.30 USD | 0.00 USD |
| `7D` | `0.9390` | 158,560.00 USD | 158,560.00 USD | 0.00 USD | 39,250.00 USD | 0.00 USD | 34,910.00 USD |
| `1D` | `0.9410` | 77,060.00 USD | 77,060.00 USD | 0.00 USD | 673.54 USD | 239.40 USD | 0.00 USD |
| `7D` | `0.9410` | 321,610.00 USD | 321,610.00 USD | 0.00 USD | 161,930.00 USD | 1,130.00 USD | 0.00 USD |
| `1D` | `0.9430` | 78,520.00 USD | 78,520.00 USD | 0.00 USD | 1,230.00 USD | 224.96 USD | 0.00 USD |
| `7D` | `0.9450` | 345,900.00 USD | 345,900.00 USD | 0.00 USD | 0.00 USD | 20,890.00 USD | 3,390.00 USD |
| `1D` | `0.9470` | 79,040.00 USD | 79,040.00 USD | 0.00 USD | 0.00 USD | 199.60 USD | 319.22 USD |
| `7D` | `0.9470` | 432,410.00 USD | 432,410.00 USD | 0.00 USD | 3,540.00 USD | 6,380.00 USD | 76,590.00 USD |
| `1D` | `0.9490` | 159,570.00 USD | 159,570.00 USD | 0.00 USD | 80,530.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9490` | 516,340.00 USD | 516,340.00 USD | 0.00 USD | 2,770.00 USD | 10,340.00 USD | 70,820.00 USD |
| `1D` | `0.9510` | 170,560.00 USD | 170,560.00 USD | 0.00 USD | 5,190.00 USD | 813.18 USD | 4,990.00 USD |
| `7D` | `0.9510` | 807,740.00 USD | 807,740.00 USD | 0.00 USD | 258,650.00 USD | 28,180.00 USD | 4,570.00 USD |
| `1D` | `0.9530` | 192,180.00 USD | 192,180.00 USD | 0.00 USD | 7,370.00 USD | 8,490.00 USD | 5,770.00 USD |
| `7D` | `0.9530` | 828,800.00 USD | 828,800.00 USD | 0.00 USD | 0.00 USD | 20,610.00 USD | 447.96 USD |
| `1D` | `0.9550` | 265,130.00 USD | 265,130.00 USD | 0.00 USD | 25,300.00 USD | 39,260.00 USD | 8,390.00 USD |
| `7D` | `0.9550` | 848,530.00 USD | 848,530.00 USD | 0.00 USD | 0.00 USD | 19,730.00 USD | 0.00 USD |
| `1D` | `0.9570` | 292,340.00 USD | 292,340.00 USD | 0.00 USD | 13,680.00 USD | 8,760.00 USD | 4,770.00 USD |
| `7D` | `0.9570` | 861,690.00 USD | 861,690.00 USD | 0.00 USD | 1,910.00 USD | 10,300.00 USD | 957.94 USD |
| `1D` | `0.9590` | 314,010.00 USD | 314,010.00 USD | 0.00 USD | 14,060.00 USD | 3,680.00 USD | 3,930.00 USD |
| `7D` | `0.9590` | 882,760.00 USD | 882,760.00 USD | 0.00 USD | 1,980.00 USD | 18,220.00 USD | 866.69 USD |
| `1D` | `0.9610` | 371,260.00 USD | 371,260.00 USD | 0.00 USD | 14,760.00 USD | 11,950.00 USD | 30,550.00 USD |
| `7D` | `0.9610` | 908,150.00 USD | 908,150.00 USD | 0.00 USD | 24,370.00 USD | 0.00 USD | 1,010.00 USD |
| `1D` | `0.9630` | 549,540.00 USD | 549,540.00 USD | 0.00 USD | 102,030.00 USD | 30,630.00 USD | 45,610.00 USD |
| `7D` | `0.9630` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 56,160.00 USD | 31,820.00 USD | 84,550.00 USD |
| `1D` | `0.9650` | 690,920.00 USD | 690,920.00 USD | 0.00 USD | 29,080.00 USD | 33,020.00 USD | 79,280.00 USD |
| `7D` | `0.9650` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 97,600.00 USD | 0.00 USD | 12,330.00 USD |
| `1D` | `0.9670` | 787,350.00 USD | 787,350.00 USD | 0.00 USD | 53,970.00 USD | 16,730.00 USD | 25,720.00 USD |
| `7D` | `0.9670` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 40,070.00 USD | 5,550.00 USD | 0.00 USD |
| `1D` | `0.9690` | 828,680.00 USD | 828,680.00 USD | 0.00 USD | 14,860.00 USD | 14,610.00 USD | 11,850.00 USD |
| `7D` | `0.9690` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 21,100.00 USD | 30,500.00 USD |
| `1D` | `0.9710` | 942,000.00 USD | 942,000.00 USD | 0.00 USD | 15,040.00 USD | 19,120.00 USD | 79,160.00 USD |
| `7D` | `0.9710` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 24,440.00 USD | 31,590.00 USD |
| `1D` | `0.9730` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 48,020.00 USD | 14,900.00 USD | 40,300.00 USD |
| `7D` | `0.9730` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 2,910.00 USD | 9,290.00 USD | 27,110.00 USD |
| `1D` | `0.9750` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 29,660.00 USD | 19,230.00 USD | 34,130.00 USD |
| `7D` | `0.9750` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 2,090.00 USD | 17,230.00 USD | 51,650.00 USD |
| `1D` | `0.9770` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 78,910.00 USD | 14,700.00 USD | 11,360.00 USD |
| `7D` | `0.9770` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD |
| `1D` | `0.9790` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 36,590.00 USD | 11,310.00 USD | 26,320.00 USD |
| `7D` | `0.9790` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD | 85,420.00 USD |
| `1D` | `0.9810` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 16,990.00 USD | 6,620.00 USD | 28,550.00 USD |
| `7D` | `0.9810` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 540.00 USD | 4,020.00 USD | 119,460.00 USD |
| `1D` | `0.9830` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 33,340.00 USD | 27,220.00 USD | 55,550.00 USD |
| `7D` | `0.9830` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 124,720.00 USD | 15,810.00 USD | 94,290.00 USD |
| `1D` | `0.9850` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 46,690.00 USD | 8,800.00 USD | 18,830.00 USD |
| `7D` | `0.9850` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 211.77 USD | 22,300.00 USD |
| `1D` | `0.9870` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 14,650.00 USD | 6,470.00 USD | 22,410.00 USD |
| `7D` | `0.9870` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 67,950.00 USD |
| `1D` | `0.9890` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 27,890.00 USD | 3,780.00 USD | 30,190.00 USD |
| `7D` | `0.9890` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `0.9910` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 60,130.00 USD | 5,890.00 USD | 45,430.00 USD |
| `7D` | `0.9910` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 3,700.00 USD | 800.44 USD | 35,270.00 USD |
| `1D` | `0.9930` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 16,320.00 USD | 5,130.00 USD | 8,200.00 USD |
| `7D` | `0.9930` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 36,000.00 USD |
| `1D` | `0.9950` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 29,250.00 USD | 2,120.00 USD | 7,140.00 USD |
| `7D` | `0.9950` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 63,060.00 USD | 5,380.00 USD | 58,050.00 USD |
| `1D` | `0.9970` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 46,950.00 USD | 1,870.00 USD | 13,030.00 USD |
| `7D` | `0.9970` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 95,130.00 USD | 253.35 USD | 4,670.00 USD |
| `1D` | `0.9990` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 35,340.00 USD | 17,910.00 USD | 10,720.00 USD |
| `7D` | `0.9990` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 6,490.00 USD | 462.12 USD |
| `1D` | `1.00` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 44,580.00 USD | 10,790.00 USD | 13,500.00 USD |
| `7D` | `1.00` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.00` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 12,370.00 USD | 9,310.00 USD | 6,140.00 USD |
| `7D` | `1.00` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 107,670.00 USD | 21,850.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 54,780.00 USD | 5,520.00 USD | 5,820.00 USD |
| `7D` | `1.00` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 32,430.00 USD | 3,970.00 USD | 12,730.00 USD |
| `1D` | `1.01` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 50,600.00 USD | 11,770.00 USD | 45,110.00 USD |
| `7D` | `1.01` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 35,710.00 USD | 240.78 USD | 29,210.00 USD |
| `1D` | `1.01` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 30,870.00 USD | 13,790.00 USD | 7,610.00 USD |
| `7D` | `1.01` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD |
| `1D` | `1.01` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 9,660.00 USD | 23,460.00 USD | 265.91 USD |
| `7D` | `1.01` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 20,090.00 USD | 17,980.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 10,450.00 USD | 1,540.00 USD | 3,780.00 USD |
| `7D` | `1.01` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD |
| `1D` | `1.01` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 14,310.00 USD | 23,780.00 USD | 14,630.00 USD |
| `7D` | `1.01` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 26,510.00 USD | 7,420.00 USD |
| `1D` | `1.02` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 3,990.00 USD | 2,940.00 USD | 12,700.00 USD |
| `7D` | `1.02` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD |
| `1D` | `1.02` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 55,630.00 USD | 4,860.00 USD | 10,650.00 USD |
| `7D` | `1.02` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 17,960.00 USD | 83,360.00 USD | 11,810.00 USD |
| `1D` | `1.02` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 6,670.00 USD | 7,410.00 USD | 21,020.00 USD |
| `7D` | `1.02` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 61,450.00 USD | 32,840.00 USD | 68,370.00 USD |
| `1D` | `1.02` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 44,890.00 USD | 18,460.00 USD | 29,940.00 USD |
| `7D` | `1.02` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 82,230.00 USD | 86,210.00 USD | 146,060.00 USD |
| `1D` | `1.02` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 43,590.00 USD | 9,520.00 USD | 20,510.00 USD |
| `7D` | `1.02` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 28,320.00 USD | 48,490.00 USD | 37,230.00 USD |
| `1D` | `1.03` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 15,190.00 USD | 11,870.00 USD | 8,110.00 USD |
| `7D` | `1.03` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 161,070.00 USD | 129,470.00 USD | 25,260.00 USD |
| `1D` | `1.03` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 14,070.00 USD | 16,110.00 USD | 20,760.00 USD |
| `7D` | `1.03` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD |
| `1D` | `1.03` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 77,920.00 USD | 11,810.00 USD | 32,920.00 USD |
| `7D` | `1.03` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD |
| `1D` | `1.03` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 17,330.00 USD | 1,510.00 USD | 16,440.00 USD |
| `7D` | `1.03` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD |
| `1D` | `1.03` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 11,120.00 USD | 18,010.00 USD | 6,850.00 USD |
| `7D` | `1.03` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 259,060.00 USD | 8,290.00 USD | 43,700.00 USD |
| `7D` | `1.04` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 193,150.00 USD | 3,330.00 USD | 109,460.00 USD |
| `7D` | `1.04` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 239,580.00 USD | 9,010.00 USD | 134,440.00 USD |
| `7D` | `1.04` | 5,980,000.00 USD | 5,980,000.00 USD | 0.00 USD | 285,690.00 USD | 2,090.00 USD | 159,500.00 USD |
| `7D` | `1.04` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD |
| `7D` | `1.04` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD |
| `7D` | `1.05` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 178,890.00 USD | 96,370.00 USD | 244,850.00 USD |
| `7D` | `1.05` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 110,190.00 USD | 13,780.00 USD | 77,620.00 USD |
| `7D` | `1.05` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 175,350.00 USD | 43,690.00 USD | 96,730.00 USD |
| `7D` | `1.05` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 68,010.00 USD | 58,070.00 USD | 74,380.00 USD |
| `7D` | `1.05` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 121,450.00 USD | 33,860.00 USD | 72,330.00 USD |
| `7D` | `1.06` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 218,860.00 USD | 70,160.00 USD | 106,380.00 USD |
| `7D` | `1.06` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 239,650.00 USD | 74,380.00 USD | 145,170.00 USD |
| `7D` | `1.06` | 9,040,000.00 USD | 9,040,000.00 USD | 0.00 USD | 138,520.00 USD | 56,310.00 USD | 78,020.00 USD |
| `7D` | `1.06` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 132,250.00 USD | 71,450.00 USD | 66,230.00 USD |
| `7D` | `1.06` | 9,470,000.00 USD | 9,470,000.00 USD | 0.00 USD | 74,870.00 USD | 22,420.00 USD | 61,060.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `173.05M` | Total OI Tokens: `184,426,628.9 DOT`
  * 1h OI Change: `+0.28%` | 4h OI Change: `-2.06%` | 24h OI Change: `-17.14%`
  * Exchange Breakdown: Binance=`33.70M` | Bybit=`22.13M` | OKX=`10.02M` | Hyperliquid=`5.84M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.53K` | Last 24h: `6.26K` | Last 3d: `-7.35K` | Last 7d: `-25.50K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0071%` |
| **USDT Bybit** | `0.0050%` | **USDT KuCoin** | `-0.0140%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0065%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `63.85%` | `36.15%` | `1.77` | 9,820,000.00 USD |
| `15M` | `Binance` | `53.58%` | `46.42%` | `1.15` | 3,810,000.00 USD |
| `15M` | `OKX` | `70.83%` | `29.17%` | `2.43` | 1,770,000.00 USD |
| `15M` | `Bybit` | `57.12%` | `42.88%` | `1.33` | 701,350.00 USD |
| `15M` | `KuCoin` | `80.1%` | `19.9%` | `4.03` | 535,560.00 USD |
| `15M` | `Gate` | `44.43%` | `55.57%` | `0.80` | 158,170.00 USD |
| `15M` | `Bitget` | `69.92%` | `30.08%` | `2.32` | 248,280.00 USD |
| `15M` | `BingX` | `73.19%` | `26.81%` | `2.73` | 465,840.00 USD |
| `15M` | `MEXC` | `63.35%` | `36.65%` | `1.73` | 979,150.00 USD |
| `15M` | `Bitunix` | `65.98%` | `34.02%` | `1.94` | 257,570.00 USD |
| `15M` | `Hyperliquid` | `66.74%` | `33.26%` | `2.01` | 215,240.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `63.58%` | `36.42%` | `1.75` | 37,270.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `97.66%` | `2.34%` | `41.74` | 349,650.00 USD |
| `15M` | `HTX` | `98.78%` | `1.22%` | `80.97` | 1,080.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `90.62%` | `9.38%` | `9.66` | 273,260.00 USD |
| `15M` | `Aster` | `81.02%` | `18.98%` | `4.27` | 9,390.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `64.4%` | `35.6%` | `1.81` | 3,030.00 USD |
| `15M` | `Whale Positions` | `53.58%` | `46.42%` | `1.15` | 3,810,000.00 USD |
| `15M` | `Global Accounts` | `63.85%` | `36.15%` | `1.77` | 9,820,000.00 USD |
| `1H` | `DOT` | `57.18%` | `42.82%` | `1.34` | 21,880,000.00 USD |
| `1H` | `Binance` | `51.89%` | `48.11%` | `1.08` | 8,310,000.00 USD |
| `1H` | `OKX` | `55.54%` | `44.46%` | `1.25` | 3,560,000.00 USD |
| `1H` | `Bybit` | `51.78%` | `48.22%` | `1.07` | 1,800,000.00 USD |
| `1H` | `KuCoin` | `73.76%` | `26.24%` | `2.81` | 766,450.00 USD |
| `1H` | `Gate` | `53.67%` | `46.33%` | `1.16` | 313,590.00 USD |
| `1H` | `Bitget` | `62.11%` | `37.89%` | `1.64` | 702,720.00 USD |
| `1H` | `BingX` | `41.78%` | `58.22%` | `0.72` | 1,370,000.00 USD |
| `1H` | `MEXC` | `64.52%` | `35.48%` | `1.82` | 2,140,000.00 USD |
| `1H` | `Bitunix` | `55.23%` | `44.77%` | `1.23` | 623,180.00 USD |
| `1H` | `Hyperliquid` | `70.6%` | `29.4%` | `2.40` | 393,760.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.52%` | `47.48%` | `1.11` | 164,760.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `86.13%` | `13.87%` | `6.21` | 1,320,000.00 USD |
| `1H` | `HTX` | `64.48%` | `35.52%` | `1.82` | 16,250.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `84.64%` | `15.36%` | `5.51` | 326,730.00 USD |
| `1H` | `Aster` | `53.57%` | `46.43%` | `1.15` | 25,540.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `28.76%` | `71.24%` | `0.40` | 27,820.00 USD |
| `1H` | `Whale Positions` | `51.89%` | `48.11%` | `1.08` | 8,310,000.00 USD |
| `1H` | `Global Accounts` | `57.18%` | `42.82%` | `1.34` | 21,880,000.00 USD |
| `4H` | `DOT` | `49.11%` | `50.89%` | `0.97` | 99,710,000.00 USD |
| `4H` | `Binance` | `47.15%` | `52.85%` | `0.89` | 37,520,000.00 USD |
| `4H` | `OKX` | `45.52%` | `54.48%` | `0.84` | 14,280,000.00 USD |
| `4H` | `Bybit` | `46.45%` | `53.55%` | `0.87` | 7,220,000.00 USD |
| `4H` | `KuCoin` | `59.98%` | `40.02%` | `1.50` | 1,810,000.00 USD |
| `4H` | `Gate` | `59.52%` | `40.48%` | `1.47` | 2,700,000.00 USD |
| `4H` | `Bitget` | `46.78%` | `53.22%` | `0.88` | 4,660,000.00 USD |
| `4H` | `BingX` | `26.89%` | `73.11%` | `0.37` | 6,100,000.00 USD |
| `4H` | `MEXC` | `51.37%` | `48.63%` | `1.06` | 14,370,000.00 USD |
| `4H` | `Bitunix` | `51.94%` | `48.06%` | `1.08` | 3,120,000.00 USD |
| `4H` | `Hyperliquid` | `46.48%` | `53.52%` | `0.87` | 1,460,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.29%` | `48.71%` | `1.05` | 1,160,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `93.48%` | `6.52%` | `14.34` | 4,330,000.00 USD |
| `4H` | `HTX` | `49.16%` | `50.84%` | `0.97` | 227,940.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `67.33%` | `32.67%` | `2.06` | 553,550.00 USD |
| `4H` | `Aster` | `55.59%` | `44.41%` | `1.25` | 123,380.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `38.67%` | `61.33%` | `0.63` | 80,610.00 USD |
| `4H` | `Whale Positions` | `47.15%` | `52.85%` | `0.89` | 37,520,000.00 USD |
| `4H` | `Global Accounts` | `49.11%` | `50.89%` | `0.97` | 99,710,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.9438` | `0.9447` | `0.9438` | `0.9488` | `0.9423` | 353,543.62 USD | 111,318.38 USD | 242,225.25 USD | -130,906.87 USD | `-37.03%` | `2B / 19S` |
| `0:00 UTC` | `0.9378` | `0.9391` | `0.9378` | `0.9427` | `0.9366` | 674,681.66 USD | 251,815.20 USD | 422,866.46 USD | -171,051.26 USD | `-25.35%` | `2B / 15S` |
| `5:00 UTC` | `0.9365` | `0.9373` | `0.9365` | `0.9404` | `0.9360` | 347,308.90 USD | 133,864.50 USD | 213,444.40 USD | -79,579.90 USD | `-22.91%` | `8B / 13S` |
| `0:00 UTC` | `0.9349` | `0.9360` | `0.9349` | `0.9390` | `0.9338` | 565,103.94 USD | 170,366.16 USD | 394,737.78 USD | -224,371.62 USD | `-39.70%` | `1B / 22S` |
| `5:00 UTC` | `0.9357` | `0.9351` | `0.9357` | `0.9366` | `0.9332` | 272,828.10 USD | 122,126.72 USD | 150,701.37 USD | -28,574.65 USD | `-10.47%` | `1B / 6S` |
| `0:00 UTC` | `0.9343` | `0.9337` | `0.9343` | `0.9365` | `0.9315` | 323,640.65 USD | 113,112.66 USD | 210,527.99 USD | -97,415.33 USD | `-30.10%` | `2B / 14S` |
| `5:00 UTC` | `0.9312` | `0.9319` | `0.9312` | `0.9351` | `0.9293` | 338,159.00 USD | 113,706.78 USD | 224,452.22 USD | -110,745.44 USD | `-32.75%` | `4B / 15S` |
| `0:00 UTC` | `0.9326` | `0.9327` | `0.9326` | `0.9345` | `0.9304` | 383,267.52 USD | 169,541.73 USD | 213,725.79 USD | -44,184.07 USD | `-11.53%` | `4B / 8S` |
| `5:00 UTC` | `0.9325` | `0.9329` | `0.9325` | `0.9366` | `0.9303` | 250,363.19 USD | 100,290.83 USD | 150,072.35 USD | -49,781.52 USD | `-19.88%` | `3B / 19S` |
| `0:00 UTC` | `0.9365` | `0.9362` | `0.9365` | `0.9374` | `0.9325` | 414,508.65 USD | 180,671.36 USD | 233,837.29 USD | -53,165.93 USD | `-12.83%` | `4B / 12S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:39` | `Volume 1.0M DOT` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 19:19` | `Range 0.005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.9951` | 122,000.00 USD | 0.00 USD |
| `10-28 19:07` | `Volume 1.0M DOT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.01` | 333,000.00 USD | 0.00 USD |
| `10-28 19:01` | `Range 0.005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 18:58` | `Volume 1.0M DOT` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 18:40` | `Volume 1.0M DOT` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.9970` | 0.00 USD | 0.00 USD |
| `10-28 18:31` | `Range 0.005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.9987` | 0.00 USD | 0.00 USD |
| `10-28 18:31` | `Range 0.005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.00` | 219,000.00 USD | 0.00 USD |
| `10-28 18:30` | `Volume 1.0M DOT` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.9987` | 0.00 USD | 0.00 USD |
| `10-28 18:30` | `Volume 1.0M DOT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.00` | 221,000.00 USD | 0.00 USD |
| `10-28 18:19` | `Range 0.005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9972` | 0.00 USD | 0.00 USD |
| `10-28 18:16` | `Volume 1.0M DOT` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9972` | 0.00 USD | 0.00 USD |
| `10-28 17:55` | `Volume 1.0M DOT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.01` | 229,000.00 USD | 0.00 USD |
| `10-28 17:46` | `Range 0.005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.01` | 260,000.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 1.0M DOT` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 1.0M DOT` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `1.00` | 0.00 USD | 0.00 USD |
| `10-28 11:08` | `Range 0.005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.00` | 0.00 USD | 0.00 USD |
| `10-28 09:02` | `Range 0.005` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `1.01` | 363,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -44,830.00 USD | -48,220.00 USD | **`DISTRIBUTION`** |
| `15m` | -37,490.00 USD | -89,820.00 USD | **`DISTRIBUTION`** |
| `30m` | -39,630.00 USD | -142,200.00 USD | **`DISTRIBUTION`** |
| `1h` | -8,110.00 USD | -408,660.00 USD | **`DISTRIBUTION`** |
| `2h` | -93,930.00 USD | -958,490.00 USD | **`DISTRIBUTION`** |
| `4h` | -122,670.00 USD | -1,440,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -211,640.00 USD | -2,770,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -226,600.00 USD | -1,720,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -511,650.00 USD | -1,570,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,320,000.00 USD | -9,610,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,930,000.00 USD | -23,630,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,980,000.00 USD | -78,950,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-44.83K` | 15m=`-37.49K` | 1h=`-8.11K` | 24h=`-1.32M`
* Futures Capital Netflows: 5m=`-48.22K` | 15m=`-89.82K` | 1h=`-408.66K` | 24h=`-9.61M`
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
  * `2026-10-30 15:49:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:45 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:45 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.8998` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.8619` (Risk Distance: `0.0400` pts)
  * +2.5R Take Profit: `0.9998`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9447` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9826` (Risk Distance: `0.0400` pts)
  * +2.5R Take Profit: `0.8447`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9445`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
