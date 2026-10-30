# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 16:24:41 IST` (`2026-10-30 10:54:41 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9270` | **Live Ask Quote**: `0.9480` | **Mid Price**: `0.9375`
- **Spread Points**: `21.00` | **Spread BPS**: `224.00 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.9106` | VWAP Z-Score: `+0.76` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0066` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `51.36` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.9795` | Lower -3.00σ Band: `0.8417`
  * Upper +2.51σ Band: `0.9683` | Lower -2.51σ Band: `0.8530`
  * Upper +2.01σ Band: `0.9568` | Lower -2.01σ Band: `0.8645`
  * Upper +2.00σ Band: `0.9566` | Lower -2.00σ Band: `0.8647`
  * Upper +1.28σ Band: `0.9400` | Lower -1.28σ Band: `0.8812`
  * Upper +1.00σ Band: `0.9336` | Lower -1.00σ Band: `0.8877`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9255` | EMA-20=`0.9269` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9291` (Slope: `+0.0000`) | EMA-100=`0.9400`
  * Institutional Anchors: EMA-144=`0.9480` | EMA-200=`0.9561` (Slope: `-0.3950`) | EMA-233=`0.9592`
- **Range Boundaries**: 24H High=`1.01` | 24H Low=`0.8570` | Weekly High=`1.03` | Weekly Low=`0.8570`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9447` (Distance: `-0.71%`)
  * Point of Control (POC) = `0.9119` (Distance: `+2.86%`)
  * Value Area Low (VAL) = `0.9004` (Distance: `+4.18%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.02` | Weekly POC=`0.9945` | Weekly VAL=`0.9689`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9330` | Low=`0.8570`
  * London Session (08:00-16:00 UTC): High=`0.9480` | Low=`0.9190`
  * New York Session (13:00-21:00 UTC): High=`0.9290` | Low=`0.9190`
  * Initial Balance (First Hour): IB High=`0.9480` | IB Low=`0.9290`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9337` - `0.9413`
  * Optimal Trade Entry (OTE 0.705): `0.9394`
  * Structural Invalidation Anchor (0.786): `0.9450`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9372` | `0.9399` | `0.9370` | `0.9383` | `150,261` | 140,987.53 USD | 49,839.93 USD | `+35.35%` | -6,036,571.63 USD | `+2.12` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.9384` | `0.9395` | `0.9368` | `0.9375` | `144,089` | 135,115.87 USD | 18,401.27 USD | `+13.62%` | -6,018,170.37 USD | `+1.30` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.9374` | `0.9390` | `0.9366` | `0.9390` | `43,694` | 40,958.16 USD | 15,277.09 USD | `+37.30%` | -6,002,893.28 USD | `+1.07` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.9323` | `0.9366` | `0.9302` | `0.9326` | `268,379` | 250,363.19 USD | -49,781.52 USD | `-19.88%` | -6,036,394.00 USD | `+0.29` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.9327` | `0.9399` | `0.9325` | `0.9383` | `644,715` | 603,897.34 USD | 5,468.79 USD | `+0.91%` | -6,030,925.20 USD | `+0.91` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.9384` | `0.9395` | `0.9366` | `0.9389` | `187,270` | 175,591.72 USD | 33,364.84 USD | `+19.00%` | -5,997,560.36 USD | `+1.16` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.9454` | `0.9488` | `0.9359` | `0.9375` | `1,853,058` | 1,744,265.88 USD | -394,329.00 USD | `-22.61%` | -5,481,321.37 USD | `-0.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.9375` | `0.9390` | `0.9292` | `0.9340` | `1,605,127` | 1,499,731.69 USD | -461,107.04 USD | `-30.75%` | -5,942,428.41 USD | `-0.17` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.9340` | `0.9399` | `0.9302` | `0.9388` | `1,511,531` | 1,413,320.86 USD | -55,099.66 USD | `-3.90%` | -5,997,528.07 USD | `+0.23` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,092,983.65 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9603` | `0.9263` | `0.9454` | `10,832,060` | 10,247,507.62 USD | -822,915.31 USD | `-8.03%` | -4,915,898.96 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9454` | `0.9488` | `0.9292` | `0.9390` | `4,970,016` | 4,657,599.64 USD | -910,254.48 USD | `-19.54%` | -5,826,153.44 USD | `+0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -974,642.25 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,499,370.98 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,092,983.65 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9603` | `0.9263` | `0.9454` | `10,832,060` | 10,247,507.62 USD | -822,915.31 USD | `-8.03%` | -4,915,898.96 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9454` | `0.9488` | `0.9292` | `0.9390` | `4,970,016` | 4,657,599.64 USD | -910,254.48 USD | `-19.54%` | -5,826,153.44 USD | `+0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`0.9375`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:23:13 IST` |

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
| `Live` | `Long Liquidation` | `0.7905` | 277.39 USD | 116,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7935` | 1,760.00 USD | 116,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7980` | 3,090,000.00 USD | 3,090,000.00 USD | 20,730.00 USD | 3,720.00 USD | 17,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7985` | 210.40 USD | 114,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8000` | 3,050,000.00 USD | 3,050,000.00 USD | 10,100.00 USD | 5,540.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8020` | 3,030,000.00 USD | 3,030,000.00 USD | 8,990.00 USD | 4,460.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8040` | 3,010,000.00 USD | 3,010,000.00 USD | 5,500.00 USD | 2,170.00 USD | 940.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8060` | 3,000,000.00 USD | 3,000,000.00 USD | 16,390.00 USD | 10,990.00 USD | 10,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8080` | 2,960,000.00 USD | 2,960,000.00 USD | 1,570.00 USD | 1,230.00 USD | 10,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8100` | 2,950,000.00 USD | 2,950,000.00 USD | 2,890.00 USD | 2,010.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8120` | 2,940,000.00 USD | 2,940,000.00 USD | 15,720.00 USD | 3,030.00 USD | 9,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 114,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8140` | 2,910,000.00 USD | 2,910,000.00 USD | 32,880.00 USD | 6,050.00 USD | 15,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8160` | 2,850,000.00 USD | 2,850,000.00 USD | 38,200.00 USD | 10,180.00 USD | 6,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8180` | 2,800,000.00 USD | 2,800,000.00 USD | 12,550.00 USD | 2,560.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8200` | 2,770,000.00 USD | 2,770,000.00 USD | 1,740.00 USD | 1,570.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 113,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8220` | 2,760,000.00 USD | 2,760,000.00 USD | 20,390.00 USD | 6,820.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 749.96 USD | 111,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8240` | 2,730,000.00 USD | 2,730,000.00 USD | 23,160.00 USD | 93.73 USD | 11,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8260` | 2,690,000.00 USD | 2,690,000.00 USD | 5,220.00 USD | 3,490.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8280` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 3,910.00 USD | 1,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8300` | 2,680,000.00 USD | 2,680,000.00 USD | 9,280.00 USD | 4,780.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8320` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 401.80 USD | 77.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8340` | 2,660,000.00 USD | 2,660,000.00 USD | 35,710.00 USD | 10,960.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8360` | 2,430,000.00 USD | 2,430,000.00 USD | 1,940.00 USD | 636.81 USD | 20,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8360` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 844.23 USD | 311.26 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 110,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8370` | 2,410,000.00 USD | 2,410,000.00 USD | 16,200.00 USD | 1,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8380` | 2,390,000.00 USD | 2,390,000.00 USD | 1,250.00 USD | 0.00 USD | 30.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8380` | 2,610,000.00 USD | 2,610,000.00 USD | 15,240.00 USD | 633.60 USD | 539.92 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8390` | 2,390,000.00 USD | 2,390,000.00 USD | 483.40 USD | 745.84 USD | 1,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8400` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 1,870.00 USD | 933.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8400` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 798.38 USD | 8,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8410` | 2,380,000.00 USD | 2,380,000.00 USD | 1,470.00 USD | 171.18 USD | 844.45 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,570.00 USD | 110,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 2,380,000.00 USD | 2,380,000.00 USD | 2,880.00 USD | 6,220.00 USD | 1,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8420` | 2,590,000.00 USD | 2,590,000.00 USD | 6,400.00 USD | 7,120.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8430` | 2,370,000.00 USD | 2,370,000.00 USD | 1,660.00 USD | 651.98 USD | 31.90 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8440` | 2,370,000.00 USD | 2,370,000.00 USD | 2,110.00 USD | 1,350.00 USD | 693.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8440` | 2,570,000.00 USD | 2,570,000.00 USD | 7,170.00 USD | 24.80 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8450` | 2,360,000.00 USD | 2,360,000.00 USD | 246.63 USD | 7,080.00 USD | 429.42 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8460` | 2,350,000.00 USD | 2,350,000.00 USD | 16,320.00 USD | 259.22 USD | 165.77 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8460` | 2,560,000.00 USD | 2,560,000.00 USD | 2,560.00 USD | 427.62 USD | 2,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8470` | 2,340,000.00 USD | 2,340,000.00 USD | 7,790.00 USD | 852.58 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8480` | 2,330,000.00 USD | 2,330,000.00 USD | 198.50 USD | 99.34 USD | 3,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8480` | 2,560,000.00 USD | 2,560,000.00 USD | 26,310.00 USD | 10,990.00 USD | 202.79 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8490` | 2,330,000.00 USD | 2,330,000.00 USD | 4,920.00 USD | 2,300.00 USD | 4,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 108,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 2,310,000.00 USD | 2,310,000.00 USD | 8,870.00 USD | 1,680.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8500` | 2,520,000.00 USD | 2,520,000.00 USD | 3,110.00 USD | 638.56 USD | 21,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8510` | 2,300,000.00 USD | 2,300,000.00 USD | 4,700.00 USD | 2,450.00 USD | 14,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8520` | 2,280,000.00 USD | 2,280,000.00 USD | 3,470.00 USD | 1,390.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8520` | 2,490,000.00 USD | 2,490,000.00 USD | 14,700.00 USD | 669.43 USD | 226.67 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8530` | 2,270,000.00 USD | 2,270,000.00 USD | 1,210.00 USD | 2,440.00 USD | 556.74 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8540` | 2,270,000.00 USD | 2,270,000.00 USD | 2,120.00 USD | 3,040.00 USD | 4,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8540` | 2,480,000.00 USD | 2,480,000.00 USD | 254.55 USD | 2,660.00 USD | 5,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8550` | 2,260,000.00 USD | 2,260,000.00 USD | 16,150.00 USD | 0.00 USD | 844.60 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8560` | 2,240,000.00 USD | 2,240,000.00 USD | 622.24 USD | 760.40 USD | 1,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8560` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 842.92 USD | 2,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8570` | 2,240,000.00 USD | 2,240,000.00 USD | 366.87 USD | 954.65 USD | 4,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 107,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8580` | 2,230,000.00 USD | 2,230,000.00 USD | 2,510.00 USD | 81.07 USD | 4,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8580` | 2,470,000.00 USD | 2,470,000.00 USD | 3,540.00 USD | 101.30 USD | 7,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8590` | 2,220,000.00 USD | 2,220,000.00 USD | 4,370.00 USD | 10,560.00 USD | 2,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8600` | 2,210,000.00 USD | 2,210,000.00 USD | 3,620.00 USD | 57.05 USD | 16,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8600` | 2,460,000.00 USD | 2,460,000.00 USD | 6,780.00 USD | 211.77 USD | 10,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8610` | 2,190,000.00 USD | 2,190,000.00 USD | 4,700.00 USD | 798.48 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8620` | 2,180,000.00 USD | 2,180,000.00 USD | 8,220.00 USD | 11,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8620` | 2,440,000.00 USD | 2,440,000.00 USD | 7,670.00 USD | 6,050.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8630` | 2,160,000.00 USD | 2,160,000.00 USD | 31,110.00 USD | 362.71 USD | 2,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 107,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 2,130,000.00 USD | 2,130,000.00 USD | 17,640.00 USD | 2,010.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8640` | 2,400,000.00 USD | 2,400,000.00 USD | 4,820.00 USD | 321.30 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 106,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8650` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 94.20 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8660` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 2,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8660` | 2,390,000.00 USD | 2,390,000.00 USD | 45,020.00 USD | 19,050.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,390.00 USD | 106,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8670` | 2,100,000.00 USD | 2,100,000.00 USD | 12,000.00 USD | 7,110.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8680` | 2,080,000.00 USD | 2,080,000.00 USD | 31,170.00 USD | 1,930.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8680` | 2,330,000.00 USD | 2,330,000.00 USD | 92,530.00 USD | 14,760.00 USD | 50,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8690` | 2,040,000.00 USD | 2,040,000.00 USD | 10,850.00 USD | 1,850.00 USD | 18,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 12,590.00 USD | 105,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8700` | 2,010,000.00 USD | 2,010,000.00 USD | 38,480.00 USD | 2,030.00 USD | 14,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8700` | 2,170,000.00 USD | 2,170,000.00 USD | 81,840.00 USD | 9,460.00 USD | 7,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8705` | 92,480.00 USD | 92,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8710` | 1,950,000.00 USD | 1,950,000.00 USD | 3,800.00 USD | 22,880.00 USD | 13,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8720` | 1,910,000.00 USD | 1,910,000.00 USD | 27,150.00 USD | 11,300.00 USD | 10,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8720` | 2,070,000.00 USD | 2,070,000.00 USD | 5,420.00 USD | 18,020.00 USD | 11,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8730` | 1,860,000.00 USD | 1,860,000.00 USD | 27,340.00 USD | 10,210.00 USD | 15,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 1,810,000.00 USD | 1,810,000.00 USD | 32,310.00 USD | 1,980.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8740` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 12,360.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8750` | 1,760,000.00 USD | 1,760,000.00 USD | 4,290.00 USD | 4,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 1,750,000.00 USD | 1,750,000.00 USD | 10,480.00 USD | 76.10 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8760` | 2,020,000.00 USD | 2,020,000.00 USD | 766.43 USD | 0.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8770` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 76.69 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8780` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 50,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8780` | 2,010,000.00 USD | 2,010,000.00 USD | 1,500.00 USD | 0.00 USD | 33,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8790` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 40.93 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8800` | 1,690,000.00 USD | 1,690,000.00 USD | 12,990.00 USD | 16.72 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8800` | 1,980,000.00 USD | 1,980,000.00 USD | 1,600.00 USD | 5,820.00 USD | 51,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8810` | 1,670,000.00 USD | 1,670,000.00 USD | 825.04 USD | 5,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8820` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8820` | 1,920,000.00 USD | 1,920,000.00 USD | 454.20 USD | 9,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8830` | 1,660,000.00 USD | 1,660,000.00 USD | 656.20 USD | 591.34 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 1,660,000.00 USD | 1,660,000.00 USD | 1,230.00 USD | 15,560.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8840` | 1,910,000.00 USD | 1,910,000.00 USD | 2,090.00 USD | 6,440.00 USD | 15,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8850` | 1,630,000.00 USD | 1,630,000.00 USD | 4,440.00 USD | 19,330.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8860` | 1,610,000.00 USD | 1,610,000.00 USD | 62,530.00 USD | 8,380.00 USD | 67.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8860` | 1,890,000.00 USD | 1,890,000.00 USD | 141,730.00 USD | 22,320.00 USD | 78,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8870` | 1,540,000.00 USD | 1,540,000.00 USD | 6,180.00 USD | 8,320.00 USD | 32,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8880` | 1,490,000.00 USD | 1,490,000.00 USD | 68,050.00 USD | 4,050.00 USD | 3,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8880` | 1,640,000.00 USD | 1,640,000.00 USD | 130,140.00 USD | 31,410.00 USD | 9,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8890` | 1,410,000.00 USD | 1,410,000.00 USD | 1,550.00 USD | 36,780.00 USD | 910.96 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8900` | 1,370,000.00 USD | 1,370,000.00 USD | 1,180.00 USD | 14,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8900` | 1,470,000.00 USD | 1,470,000.00 USD | 108,250.00 USD | 45,590.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8910` | 1,360,000.00 USD | 1,360,000.00 USD | 965.62 USD | 23,750.00 USD | 20,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8920` | 1,310,000.00 USD | 1,310,000.00 USD | 45,120.00 USD | 9,020.00 USD | 36,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8920` | 1,290,000.00 USD | 1,290,000.00 USD | 46,210.00 USD | 38,810.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8930` | 1,220,000.00 USD | 1,220,000.00 USD | 11,680.00 USD | 15,620.00 USD | 1,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8940` | 1,190,000.00 USD | 1,190,000.00 USD | 4,700.00 USD | 2,510.00 USD | 191.55 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8940` | 1,190,000.00 USD | 1,190,000.00 USD | 45,210.00 USD | 12,120.00 USD | 26,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8950` | 1,190,000.00 USD | 1,190,000.00 USD | 2,010.00 USD | 12,910.00 USD | 7,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8960` | 1,160,000.00 USD | 1,160,000.00 USD | 3,520.00 USD | 17,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8960` | 1,100,000.00 USD | 1,100,000.00 USD | 2,140.00 USD | 32,820.00 USD | 93,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8970` | 1,140,000.00 USD | 1,140,000.00 USD | 4,780.00 USD | 10,990.00 USD | 19,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8980` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 18,250.00 USD | 871.02 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8980` | 975,980.00 USD | 975,980.00 USD | 0.00 USD | 24,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8990` | 1,090,000.00 USD | 1,090,000.00 USD | 3,650.00 USD | 5,880.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9000` | 1,070,000.00 USD | 1,070,000.00 USD | 4,950.00 USD | 15,830.00 USD | 4,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9000` | 951,920.00 USD | 951,920.00 USD | 0.00 USD | 25,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9010` | 1,050,000.00 USD | 1,050,000.00 USD | 538.90 USD | 11,830.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9020` | 1,040,000.00 USD | 1,040,000.00 USD | 3,570.00 USD | 0.00 USD | 414.44 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9020` | 926,880.00 USD | 926,880.00 USD | 0.00 USD | 48,090.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9030` | 1,030,000.00 USD | 1,030,000.00 USD | 5,410.00 USD | 17,560.00 USD | 17,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9040` | 990,280.00 USD | 990,280.00 USD | 6,880.00 USD | 5,250.00 USD | 10,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9040` | 855,370.00 USD | 855,370.00 USD | 0.00 USD | 12,290.00 USD | 506.97 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9050` | 967,210.00 USD | 967,210.00 USD | 12,450.00 USD | 6,350.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9060` | 937,300.00 USD | 937,300.00 USD | 17,690.00 USD | 3,930.00 USD | 14,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9060` | 842,570.00 USD | 842,570.00 USD | 1,910.00 USD | 3,840.00 USD | 42,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9070` | 901,670.00 USD | 901,670.00 USD | 18,960.00 USD | 4,440.00 USD | 19,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9080` | 858,760.00 USD | 858,760.00 USD | 1,500.00 USD | 5,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9080` | 794,790.00 USD | 794,790.00 USD | 22,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9090` | 851,660.00 USD | 851,660.00 USD | 5,600.00 USD | 3,480.00 USD | 239.84 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9100` | 842,350.00 USD | 842,350.00 USD | 2,570.00 USD | 0.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9110` | 838,230.00 USD | 838,230.00 USD | 22,990.00 USD | 2,850.00 USD | 528.48 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9120` | 811,860.00 USD | 811,860.00 USD | 9,340.00 USD | 2,720.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9130` | 797,230.00 USD | 797,230.00 USD | 7,740.00 USD | 6,760.00 USD | 19,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9140` | 762,980.00 USD | 762,980.00 USD | 1,860.00 USD | 11,300.00 USD | 13,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9140` | 772,780.00 USD | 772,780.00 USD | 0.00 USD | 515.41 USD | 36,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9150` | 736,570.00 USD | 736,570.00 USD | 9,260.00 USD | 6,480.00 USD | 11,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9160` | 709,420.00 USD | 709,420.00 USD | 0.00 USD | 4,900.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9160` | 735,420.00 USD | 735,420.00 USD | 0.00 USD | 12,370.00 USD | 9,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9170` | 697,480.00 USD | 697,480.00 USD | 7,300.00 USD | 11,760.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9180` | 670,370.00 USD | 670,370.00 USD | 7,040.00 USD | 3,230.00 USD | 11,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9180` | 713,240.00 USD | 713,240.00 USD | 0.00 USD | 0.00 USD | 23,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9190` | 648,520.00 USD | 648,520.00 USD | 2,860.00 USD | 10,410.00 USD | 4,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9200` | 631,250.00 USD | 631,250.00 USD | 5,710.00 USD | 3,680.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9200` | 689,860.00 USD | 689,860.00 USD | 0.00 USD | 4,870.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9210` | 616,660.00 USD | 616,660.00 USD | 7,140.00 USD | 0.00 USD | 828.87 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9220` | 608,690.00 USD | 608,690.00 USD | 6,600.00 USD | 3,470.00 USD | 48.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9220` | 681,020.00 USD | 681,020.00 USD | 152,480.00 USD | 7,760.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9230` | 598,570.00 USD | 598,570.00 USD | 0.00 USD | 3,670.00 USD | 21,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9240` | 573,260.00 USD | 573,260.00 USD | 88,170.00 USD | 17,120.00 USD | 21,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9240` | 519,770.00 USD | 519,770.00 USD | 141,890.00 USD | 20,480.00 USD | 25,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9250` | 446,030.00 USD | 446,030.00 USD | 11,810.00 USD | 46,150.00 USD | 40,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9260` | 347,490.00 USD | 347,490.00 USD | 23,500.00 USD | 5,610.00 USD | 43,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9260` | 331,740.00 USD | 331,740.00 USD | 44,020.00 USD | 32,300.00 USD | 84,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9270` | 275,330.00 USD | 275,330.00 USD | 16,430.00 USD | 1,430.00 USD | 30,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9280` | 226,710.00 USD | 226,710.00 USD | 75,820.00 USD | 11,000.00 USD | 35,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9280` | 171,340.00 USD | 171,340.00 USD | 0.00 USD | 24,550.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9290` | 104,120.00 USD | 104,120.00 USD | 5,140.00 USD | 9,440.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9300` | 86,760.00 USD | 86,760.00 USD | 0.00 USD | 5,730.00 USD | 1,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9310` | 79,980.00 USD | 79,980.00 USD | 0.00 USD | 1,400.00 USD | 4,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9320` | 74,230.00 USD | 74,230.00 USD | 0.00 USD | 6,110.00 USD | 181.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9320` | 145,190.00 USD | 145,190.00 USD | 37,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9330` | 67,930.00 USD | 67,930.00 USD | 3,720.00 USD | 30.28 USD | 26,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9340` | 107,750.00 USD | 107,750.00 USD | 0.00 USD | 0.00 USD | 31,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9350` | 37,770.00 USD | 37,770.00 USD | 36,510.00 USD | 221.86 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9360` | 1,030.00 USD | 1,030.00 USD | 0.00 USD | 91.53 USD | 852.35 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9360` | 76,380.00 USD | 76,380.00 USD | 8,250.00 USD | 0.00 USD | 68,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9370` | 90.48 USD | 90.48 USD | 0.00 USD | 90.48 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9380` | 89,890.00 USD | 89,890.00 USD | 42,660.00 USD | 19,540.00 USD | 27,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9390` | 1,650.00 USD | 1,650.00 USD | 1,340.00 USD | 309.30 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9400` | 2,560.00 USD | 2,560.00 USD | 673.54 USD | 239.40 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9400` | 173,120.00 USD | 173,120.00 USD | 75,540.00 USD | 474.96 USD | 7,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9420` | 3,800.00 USD | 3,800.00 USD | 1,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9420` | 264,830.00 USD | 264,830.00 USD | 91,060.00 USD | 650.60 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9430` | 4,020.00 USD | 4,020.00 USD | 0.00 USD | 224.96 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9440` | 265,550.00 USD | 265,550.00 USD | 0.00 USD | 0.00 USD | 713.33 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 4,300.00 USD | 4,300.00 USD | 0.00 USD | 199.60 USD | 79.38 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9460` | 343,200.00 USD | 343,200.00 USD | 0.00 USD | 27,270.00 USD | 50,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9470` | 4,540.00 USD | 4,540.00 USD | 0.00 USD | 0.00 USD | 239.84 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9480` | 6,330.00 USD | 6,330.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9480` | 451,830.00 USD | 451,830.00 USD | 3,540.00 USD | 10,340.00 USD | 94,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9490` | 85,070.00 USD | 85,070.00 USD | 78,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 90,490.00 USD | 90,490.00 USD | 5,190.00 USD | 85.68 USD | 151.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9500` | 565,890.00 USD | 565,890.00 USD | 85,700.00 USD | 18,830.00 USD | 9,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9510` | 96,060.00 USD | 96,060.00 USD | 0.00 USD | 727.50 USD | 4,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 104,550.00 USD | 104,550.00 USD | 0.00 USD | 8,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9520` | 751,810.00 USD | 751,810.00 USD | 175,720.00 USD | 9,750.00 USD | 447.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9530` | 117,680.00 USD | 117,680.00 USD | 7,370.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 142,110.00 USD | 142,110.00 USD | 10,150.00 USD | 12,540.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9540` | 773,640.00 USD | 773,640.00 USD | 0.00 USD | 21,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9550` | 190,670.00 USD | 190,670.00 USD | 15,150.00 USD | 26,720.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 208,670.00 USD | 208,670.00 USD | 9,900.00 USD | 3,330.00 USD | 4,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9560` | 801,740.00 USD | 801,740.00 USD | 0.00 USD | 28,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9570` | 224,240.00 USD | 224,240.00 USD | 3,780.00 USD | 8,320.00 USD | 3,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 233,890.00 USD | 233,890.00 USD | 3,480.00 USD | 3,680.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9580` | 817,560.00 USD | 817,560.00 USD | 3,880.00 USD | 10,980.00 USD | 957.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9590` | 245,910.00 USD | 245,910.00 USD | 10,580.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 261,810.00 USD | 261,810.00 USD | 6,600.00 USD | 8,190.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9600` | 849,550.00 USD | 849,550.00 USD | 17,690.00 USD | 12,420.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9610` | 303,160.00 USD | 303,160.00 USD | 8,160.00 USD | 3,760.00 USD | 29,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 423,810.00 USD | 423,810.00 USD | 73,570.00 USD | 16,310.00 USD | 30,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9620` | 891,860.00 USD | 891,860.00 USD | 17,990.00 USD | 24,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9630` | 481,440.00 USD | 481,440.00 USD | 28,460.00 USD | 14,320.00 USD | 14,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 601,310.00 USD | 601,310.00 USD | 25,340.00 USD | 29,540.00 USD | 65,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9640` | 1,130,000.00 USD | 1,130,000.00 USD | 139,390.00 USD | 7,500.00 USD | 96,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9650` | 622,820.00 USD | 622,820.00 USD | 3,740.00 USD | 3,490.00 USD | 14,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 668,770.00 USD | 668,770.00 USD | 13,160.00 USD | 9,860.00 USD | 22,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9660` | 1,150,000.00 USD | 1,150,000.00 USD | 5,050.00 USD | 5,170.00 USD | 778.15 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9670` | 719,250.00 USD | 719,250.00 USD | 40,820.00 USD | 6,870.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9680` | 737,570.00 USD | 737,570.00 USD | 6,000.00 USD | 11,070.00 USD | 1,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9680` | 1,190,000.00 USD | 1,190,000.00 USD | 38,090.00 USD | 5,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9690` | 760,580.00 USD | 760,580.00 USD | 8,860.00 USD | 3,540.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 814,930.00 USD | 814,930.00 USD | 7,640.00 USD | 12,030.00 USD | 34,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9700` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 30,140.00 USD | 30,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9710` | 873,900.00 USD | 873,900.00 USD | 7,400.00 USD | 7,090.00 USD | 44,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 930,200.00 USD | 930,200.00 USD | 28,150.00 USD | 3,850.00 USD | 24,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9720` | 1,290,000.00 USD | 1,290,000.00 USD | 1,430.00 USD | 10,140.00 USD | 31,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9730` | 977,140.00 USD | 977,140.00 USD | 19,870.00 USD | 11,060.00 USD | 16,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 1,010,000.00 USD | 1,010,000.00 USD | 13,100.00 USD | 1,620.00 USD | 17,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9740` | 1,400,000.00 USD | 1,400,000.00 USD | 1,480.00 USD | 25,640.00 USD | 76,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9750` | 1,060,000.00 USD | 1,060,000.00 USD | 16,550.00 USD | 17,610.00 USD | 16,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 1,120,000.00 USD | 1,120,000.00 USD | 38,530.00 USD | 11,220.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9760` | 1,480,000.00 USD | 1,480,000.00 USD | 51,990.00 USD | 19,300.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9770` | 1,170,000.00 USD | 1,170,000.00 USD | 40,380.00 USD | 4,920.00 USD | 7,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 1,180,000.00 USD | 1,180,000.00 USD | 4,000.00 USD | 0.00 USD | 10,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9780` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 3,880.00 USD | 24,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9790` | 1,240,000.00 USD | 1,240,000.00 USD | 32,590.00 USD | 11,310.00 USD | 15,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 1,260,000.00 USD | 1,260,000.00 USD | 5,740.00 USD | 107.04 USD | 15,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9800` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 152,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 102.95 USD | 102.95 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9810` | 1,290,000.00 USD | 1,290,000.00 USD | 11,240.00 USD | 6,510.00 USD | 13,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 1,340,000.00 USD | 1,340,000.00 USD | 21,600.00 USD | 15,460.00 USD | 11,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9820` | 1,880,000.00 USD | 1,880,000.00 USD | 53,310.00 USD | 19,830.00 USD | 146,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9830` | 1,410,000.00 USD | 1,410,000.00 USD | 11,750.00 USD | 11,760.00 USD | 44,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 1,430,000.00 USD | 1,430,000.00 USD | 2,170.00 USD | 5,110.00 USD | 14,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9840` | 1,970,000.00 USD | 1,970,000.00 USD | 71,940.00 USD | 211.77 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9850` | 1,490,000.00 USD | 1,490,000.00 USD | 44,520.00 USD | 3,690.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 1,520,000.00 USD | 1,520,000.00 USD | 14,650.00 USD | 3,460.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9860` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9870` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 3,010.00 USD | 1,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9880` | 1,560,000.00 USD | 1,560,000.00 USD | 17,200.00 USD | 700.08 USD | 15,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9880` | 2,080,000.00 USD | 2,080,000.00 USD | 40,020.00 USD | 0.00 USD | 67,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9890` | 1,590,000.00 USD | 1,590,000.00 USD | 10,690.00 USD | 3,080.00 USD | 14,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 1,670,000.00 USD | 1,670,000.00 USD | 55,800.00 USD | 4,740.00 USD | 18,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9900` | 2,120,000.00 USD | 2,120,000.00 USD | 22,660.00 USD | 321.20 USD | 16,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9910` | 1,700,000.00 USD | 1,700,000.00 USD | 4,330.00 USD | 1,150.00 USD | 26,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 1,720,000.00 USD | 1,720,000.00 USD | 8,410.00 USD | 3,870.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9920` | 2,150,000.00 USD | 2,150,000.00 USD | 1,570.00 USD | 479.24 USD | 31,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9925` | 3,940.00 USD | 4,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9930` | 1,730,000.00 USD | 1,730,000.00 USD | 7,910.00 USD | 1,250.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 1,760,000.00 USD | 1,760,000.00 USD | 17,780.00 USD | 0.00 USD | 7,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9940` | 2,220,000.00 USD | 2,220,000.00 USD | 29,270.00 USD | 0.00 USD | 39,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9950` | 1,770,000.00 USD | 1,770,000.00 USD | 11,460.00 USD | 2,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 1,790,000.00 USD | 1,790,000.00 USD | 7,610.00 USD | 1,480.00 USD | 7,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9960` | 2,350,000.00 USD | 2,350,000.00 USD | 75,810.00 USD | 5,380.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9970` | 1,830,000.00 USD | 1,830,000.00 USD | 39,340.00 USD | 396.06 USD | 5,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 1,870,000.00 USD | 1,870,000.00 USD | 15,330.00 USD | 10,370.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9980` | 2,410,000.00 USD | 2,410,000.00 USD | 53,110.00 USD | 6,740.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9985` | 852.22 USD | 4,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9990` | 1,900,000.00 USD | 1,900,000.00 USD | 20,010.00 USD | 7,540.00 USD | 428.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,940,000.00 USD | 1,940,000.00 USD | 29,250.00 USD | 10,690.00 USD | 6,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,460,000.00 USD | 2,460,000.00 USD | 52,850.00 USD | 0.00 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,960,000.00 USD | 1,960,000.00 USD | 15,340.00 USD | 105.11 USD | 7,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,970,000.00 USD | 1,970,000.00 USD | 1,570.00 USD | 1,920.00 USD | 73.68 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,560,000.00 USD | 2,560,000.00 USD | 56,560.00 USD | 21,850.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,990,000.00 USD | 1,990,000.00 USD | 10,790.00 USD | 7,390.00 USD | 6,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 2,160.00 USD | 3,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,640,000.00 USD | 2,640,000.00 USD | 70,950.00 USD | 3,970.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,060,000.00 USD | 2,060,000.00 USD | 54,780.00 USD | 3,360.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,130,000.00 USD | 2,130,000.00 USD | 48,890.00 USD | 6,840.00 USD | 13,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,700,000.00 USD | 2,700,000.00 USD | 48,310.00 USD | 240.78 USD | 11,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,160,000.00 USD | 2,160,000.00 USD | 1,710.00 USD | 4,930.00 USD | 24,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,190,000.00 USD | 2,190,000.00 USD | 21,530.00 USD | 4,400.00 USD | 6,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 44,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,210,000.00 USD | 2,210,000.00 USD | 9,350.00 USD | 9,390.00 USD | 971.85 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,220,000.00 USD | 2,220,000.00 USD | 3,220.00 USD | 7,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,770,000.00 USD | 2,770,000.00 USD | 10,260.00 USD | 14,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,250,000.00 USD | 2,250,000.00 USD | 6,440.00 USD | 15,620.00 USD | 265.91 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,260,000.00 USD | 2,260,000.00 USD | 10,450.00 USD | 104.36 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,830,000.00 USD | 2,830,000.00 USD | 33,230.00 USD | 30,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 1,440.00 USD | 3,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,280,000.00 USD | 2,280,000.00 USD | 7,030.00 USD | 4,350.00 USD | 12,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,860,000.00 USD | 2,860,000.00 USD | 2,870.00 USD | 28,450.00 USD | 735.11 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,310,000.00 USD | 2,310,000.00 USD | 7,280.00 USD | 19,430.00 USD | 2,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,330,000.00 USD | 2,330,000.00 USD | 2,130.00 USD | 2,920.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,900,000.00 USD | 2,900,000.00 USD | 526.60 USD | 28,470.00 USD | 11,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,330,000.00 USD | 2,330,000.00 USD | 1,860.00 USD | 16.79 USD | 5,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,360,000.00 USD | 2,360,000.00 USD | 24,250.00 USD | 1,140.00 USD | 3,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,950,000.00 USD | 2,950,000.00 USD | 1,430.00 USD | 25,010.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,400,000.00 USD | 2,400,000.00 USD | 31,380.00 USD | 3,720.00 USD | 6,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 760.04 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,420,000.00 USD | 2,420,000.00 USD | 2,180.00 USD | 5,820.00 USD | 11,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,110,000.00 USD | 3,110,000.00 USD | 33,820.00 USD | 84,220.00 USD | 44,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,440,000.00 USD | 2,440,000.00 USD | 4,500.00 USD | 1,590.00 USD | 9,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,490,000.00 USD | 2,490,000.00 USD | 21,190.00 USD | 14,220.00 USD | 15,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,330,000.00 USD | 3,330,000.00 USD | 56,930.00 USD | 52,610.00 USD | 112,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,530,000.00 USD | 2,530,000.00 USD | 23,700.00 USD | 4,240.00 USD | 14,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,570,000.00 USD | 2,570,000.00 USD | 19,140.00 USD | 2,930.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,560,000.00 USD | 3,560,000.00 USD | 78,220.00 USD | 56,700.00 USD | 86,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,600,000.00 USD | 2,600,000.00 USD | 20,590.00 USD | 4,010.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,620,000.00 USD | 2,620,000.00 USD | 8,150.00 USD | 11,760.00 USD | 7,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,740,000.00 USD | 3,740,000.00 USD | 22,650.00 USD | 124,880.00 USD | 33,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,630,000.00 USD | 2,630,000.00 USD | 7,050.00 USD | 106.85 USD | 844.45 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,650,000.00 USD | 2,650,000.00 USD | 6,270.00 USD | 3,780.00 USD | 6,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,060,000.00 USD | 4,060,000.00 USD | 250,310.00 USD | 53,000.00 USD | 24,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.03` | 152.32 USD | 5,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,680,000.00 USD | 2,680,000.00 USD | 7,800.00 USD | 10,060.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,750,000.00 USD | 2,750,000.00 USD | 56,450.00 USD | 4,120.00 USD | 9,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,250,000.00 USD | 4,250,000.00 USD | 134,200.00 USD | 33,660.00 USD | 19,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,790,000.00 USD | 2,790,000.00 USD | 17,790.00 USD | 7,690.00 USD | 22,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,820,000.00 USD | 2,820,000.00 USD | 10,390.00 USD | 1,350.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,360,000.00 USD | 4,360,000.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,830,000.00 USD | 2,830,000.00 USD | 6,940.00 USD | 812.59 USD | 7,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,850,000.00 USD | 2,850,000.00 USD | 6,560.00 USD | 8,560.00 USD | 5,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,590,000.00 USD | 4,590,000.00 USD | 217,210.00 USD | 8,290.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.03` | 221.28 USD | 6,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,870,000.00 USD | 2,870,000.00 USD | 4,560.00 USD | 9,450.00 USD | 910.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 4,900,000.00 USD | 4,900,000.00 USD | 262,550.00 USD | 3,170.00 USD | 43,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,290,000.00 USD | 5,290,000.00 USD | 179,470.00 USD | 1,450.00 USD | 215,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,690,000.00 USD | 5,690,000.00 USD | 288,650.00 USD | 9,430.00 USD | 93,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 182.19 USD | 6,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,010,000.00 USD | 6,010,000.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,270,000.00 USD | 6,270,000.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 6,690,000.00 USD | 6,690,000.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 367.04 USD | 6,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,080,000.00 USD | 7,080,000.00 USD | 197,310.00 USD | 28,070.00 USD | 167,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,240,000.00 USD | 7,240,000.00 USD | 87,270.00 USD | 29,070.00 USD | 41,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,570,000.00 USD | 7,570,000.00 USD | 140,530.00 USD | 49,780.00 USD | 143,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,740,000.00 USD | 7,740,000.00 USD | 87,130.00 USD | 44,290.00 USD | 36,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,100,000.00 USD | 8,100,000.00 USD | 185,840.00 USD | 48,000.00 USD | 121,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,460,000.00 USD | 8,460,000.00 USD | 205,290.00 USD | 63,350.00 USD | 94,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,870,000.00 USD | 8,870,000.00 USD | 217,790.00 USD | 73,000.00 USD | 125,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,130,000.00 USD | 9,130,000.00 USD | 115,520.00 USD | 81,560.00 USD | 61,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,250,000.00 USD | 9,250,000.00 USD | 91,360.00 USD | 25,320.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.7980` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 20,730.00 USD | 3,720.00 USD | 17,520.00 USD |
| `7D` | `0.8000` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 10,100.00 USD | 5,540.00 USD | 2,430.00 USD |
| `7D` | `0.8020` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 8,990.00 USD | 4,460.00 USD | 9,540.00 USD |
| `7D` | `0.8040` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 5,500.00 USD | 2,170.00 USD | 940.33 USD |
| `7D` | `0.8060` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 16,390.00 USD | 10,990.00 USD | 10,100.00 USD |
| `7D` | `0.8080` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 1,570.00 USD | 1,230.00 USD | 10,210.00 USD |
| `7D` | `0.8100` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 2,890.00 USD | 2,010.00 USD | 4,690.00 USD |
| `7D` | `0.8120` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 15,720.00 USD | 3,030.00 USD | 9,400.00 USD |
| `7D` | `0.8140` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 32,880.00 USD | 6,050.00 USD | 15,910.00 USD |
| `7D` | `0.8160` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 38,200.00 USD | 10,180.00 USD | 6,010.00 USD |
| `7D` | `0.8180` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 12,550.00 USD | 2,560.00 USD | 11,440.00 USD |
| `7D` | `0.8200` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 1,740.00 USD | 1,570.00 USD | 7,460.00 USD |
| `7D` | `0.8220` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 20,390.00 USD | 6,820.00 USD | 4,490.00 USD |
| `7D` | `0.8240` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 23,160.00 USD | 93.73 USD | 11,990.00 USD |
| `7D` | `0.8260` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 5,220.00 USD | 3,490.00 USD | 1,560.00 USD |
| `7D` | `0.8280` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 0.00 USD | 3,910.00 USD | 1,040.00 USD |
| `7D` | `0.8300` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 9,280.00 USD | 4,780.00 USD | 2,450.00 USD |
| `7D` | `0.8320` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 0.00 USD | 401.80 USD | 77.95 USD |
| `7D` | `0.8340` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 35,710.00 USD | 10,960.00 USD | 1,980.00 USD |
| `1D` | `0.8360` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 1,940.00 USD | 636.81 USD | 20,310.00 USD |
| `7D` | `0.8360` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 0.00 USD | 844.23 USD | 311.26 USD |
| `1D` | `0.8370` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 16,200.00 USD | 1,900.00 USD | 0.00 USD |
| `1D` | `0.8380` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 1,250.00 USD | 0.00 USD | 30.30 USD |
| `7D` | `0.8380` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 15,240.00 USD | 633.60 USD | 539.92 USD |
| `1D` | `0.8390` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 483.40 USD | 745.84 USD | 1,980.00 USD |
| `1D` | `0.8400` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 0.00 USD | 1,870.00 USD | 933.95 USD |
| `7D` | `0.8400` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 0.00 USD | 798.38 USD | 8,060.00 USD |
| `1D` | `0.8410` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 1,470.00 USD | 171.18 USD | 844.45 USD |
| `1D` | `0.8420` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,880.00 USD | 6,220.00 USD | 1,120.00 USD |
| `7D` | `0.8420` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 6,400.00 USD | 7,120.00 USD | 4,060.00 USD |
| `1D` | `0.8430` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 1,660.00 USD | 651.98 USD | 31.90 USD |
| `1D` | `0.8440` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 2,110.00 USD | 1,350.00 USD | 693.86 USD |
| `7D` | `0.8440` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 7,170.00 USD | 24.80 USD | 0.00 USD |
| `1D` | `0.8450` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 246.63 USD | 7,080.00 USD | 429.42 USD |
| `1D` | `0.8460` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 16,320.00 USD | 259.22 USD | 165.77 USD |
| `7D` | `0.8460` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 2,560.00 USD | 427.62 USD | 2,660.00 USD |
| `1D` | `0.8470` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 7,790.00 USD | 852.58 USD | 0.00 USD |
| `1D` | `0.8480` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 198.50 USD | 99.34 USD | 3,080.00 USD |
| `7D` | `0.8480` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 26,310.00 USD | 10,990.00 USD | 202.79 USD |
| `1D` | `0.8490` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 4,920.00 USD | 2,300.00 USD | 4,860.00 USD |
| `1D` | `0.8500` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 8,870.00 USD | 1,680.00 USD | 1,720.00 USD |
| `7D` | `0.8500` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 3,110.00 USD | 638.56 USD | 21,250.00 USD |
| `1D` | `0.8510` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 4,700.00 USD | 2,450.00 USD | 14,990.00 USD |
| `1D` | `0.8520` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 3,470.00 USD | 1,390.00 USD | 4,950.00 USD |
| `7D` | `0.8520` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 14,700.00 USD | 669.43 USD | 226.67 USD |
| `1D` | `0.8530` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 1,210.00 USD | 2,440.00 USD | 556.74 USD |
| `1D` | `0.8540` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 2,120.00 USD | 3,040.00 USD | 4,240.00 USD |
| `7D` | `0.8540` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 254.55 USD | 2,660.00 USD | 5,540.00 USD |
| `1D` | `0.8550` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 16,150.00 USD | 0.00 USD | 844.60 USD |
| `1D` | `0.8560` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 622.24 USD | 760.40 USD | 1,810.00 USD |
| `7D` | `0.8560` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 0.00 USD | 842.92 USD | 2,180.00 USD |
| `1D` | `0.8570` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 366.87 USD | 954.65 USD | 4,340.00 USD |
| `1D` | `0.8580` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 2,510.00 USD | 81.07 USD | 4,300.00 USD |
| `7D` | `0.8580` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 3,540.00 USD | 101.30 USD | 7,540.00 USD |
| `1D` | `0.8590` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 4,370.00 USD | 10,560.00 USD | 2,120.00 USD |
| `1D` | `0.8600` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 3,620.00 USD | 57.05 USD | 16,460.00 USD |
| `7D` | `0.8600` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 6,780.00 USD | 211.77 USD | 10,030.00 USD |
| `1D` | `0.8610` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 4,700.00 USD | 798.48 USD | 0.00 USD |
| `1D` | `0.8620` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 8,220.00 USD | 11,930.00 USD | 0.00 USD |
| `7D` | `0.8620` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 7,670.00 USD | 6,050.00 USD | 26,880.00 USD |
| `1D` | `0.8630` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 31,110.00 USD | 362.71 USD | 2,010.00 USD |
| `1D` | `0.8640` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 17,640.00 USD | 2,010.00 USD | 1,790.00 USD |
| `7D` | `0.8640` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 4,820.00 USD | 321.30 USD | 0.00 USD |
| `1D` | `0.8650` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 0.00 USD | 94.20 USD | 0.00 USD |
| `1D` | `0.8660` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 0.00 USD | 2,980.00 USD | 0.00 USD |
| `7D` | `0.8660` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 45,020.00 USD | 19,050.00 USD | 2,170.00 USD |
| `1D` | `0.8670` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 12,000.00 USD | 7,110.00 USD | 1,110.00 USD |
| `1D` | `0.8680` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 31,170.00 USD | 1,930.00 USD | 10,780.00 USD |
| `7D` | `0.8680` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 92,530.00 USD | 14,760.00 USD | 50,800.00 USD |
| `1D` | `0.8690` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 10,850.00 USD | 1,850.00 USD | 18,630.00 USD |
| `1D` | `0.8700` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 38,480.00 USD | 2,030.00 USD | 14,760.00 USD |
| `7D` | `0.8700` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 81,840.00 USD | 9,460.00 USD | 7,550.00 USD |
| `1D` | `0.8710` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 3,800.00 USD | 22,880.00 USD | 13,870.00 USD |
| `1D` | `0.8720` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 27,150.00 USD | 11,300.00 USD | 10,720.00 USD |
| `7D` | `0.8720` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 5,420.00 USD | 18,020.00 USD | 11,450.00 USD |
| `1D` | `0.8730` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 27,340.00 USD | 10,210.00 USD | 15,240.00 USD |
| `1D` | `0.8740` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 32,310.00 USD | 1,980.00 USD | 17,890.00 USD |
| `7D` | `0.8740` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 0.00 USD | 12,360.00 USD | 3,200.00 USD |
| `1D` | `0.8750` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 4,290.00 USD | 4,920.00 USD | 0.00 USD |
| `1D` | `0.8760` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 10,480.00 USD | 76.10 USD | 0.00 USD |
| `7D` | `0.8760` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 766.43 USD | 0.00 USD | 5,750.00 USD |
| `1D` | `0.8770` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 0.00 USD | 76.69 USD | 0.00 USD |
| `1D` | `0.8780` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 50,910.00 USD |
| `7D` | `0.8780` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 1,500.00 USD | 0.00 USD | 33,650.00 USD |
| `1D` | `0.8790` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 0.00 USD | 40.93 USD | 0.00 USD |
| `1D` | `0.8800` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 12,990.00 USD | 16.72 USD | 2,430.00 USD |
| `7D` | `0.8800` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 1,600.00 USD | 5,820.00 USD | 51,030.00 USD |
| `1D` | `0.8810` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 825.04 USD | 5,190.00 USD | 0.00 USD |
| `1D` | `0.8820` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD |
| `7D` | `0.8820` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 454.20 USD | 9,500.00 USD | 0.00 USD |
| `1D` | `0.8830` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 656.20 USD | 591.34 USD | 0.00 USD |
| `1D` | `0.8840` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 1,230.00 USD | 15,560.00 USD | 8,890.00 USD |
| `7D` | `0.8840` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 2,090.00 USD | 6,440.00 USD | 15,690.00 USD |
| `1D` | `0.8850` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 4,440.00 USD | 19,330.00 USD | 2,290.00 USD |
| `1D` | `0.8860` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 62,530.00 USD | 8,380.00 USD | 67.73 USD |
| `7D` | `0.8860` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 141,730.00 USD | 22,320.00 USD | 78,280.00 USD |
| `1D` | `0.8870` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 6,180.00 USD | 8,320.00 USD | 32,690.00 USD |
| `1D` | `0.8880` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 68,050.00 USD | 4,050.00 USD | 3,950.00 USD |
| `7D` | `0.8880` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 130,140.00 USD | 31,410.00 USD | 9,920.00 USD |
| `1D` | `0.8890` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 1,550.00 USD | 36,780.00 USD | 910.96 USD |
| `1D` | `0.8900` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,180.00 USD | 14,980.00 USD | 0.00 USD |
| `7D` | `0.8900` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 108,250.00 USD | 45,590.00 USD | 30,420.00 USD |
| `1D` | `0.8910` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 965.62 USD | 23,750.00 USD | 20,080.00 USD |
| `1D` | `0.8920` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 45,120.00 USD | 9,020.00 USD | 36,050.00 USD |
| `7D` | `0.8920` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 46,210.00 USD | 38,810.00 USD | 14,520.00 USD |
| `1D` | `0.8930` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 11,680.00 USD | 15,620.00 USD | 1,870.00 USD |
| `1D` | `0.8940` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 4,700.00 USD | 2,510.00 USD | 191.55 USD |
| `7D` | `0.8940` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 45,210.00 USD | 12,120.00 USD | 26,470.00 USD |
| `1D` | `0.8950` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 2,010.00 USD | 12,910.00 USD | 7,970.00 USD |
| `1D` | `0.8960` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 3,520.00 USD | 17,450.00 USD | 0.00 USD |
| `7D` | `0.8960` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 2,140.00 USD | 32,820.00 USD | 93,280.00 USD |
| `1D` | `0.8970` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 4,780.00 USD | 10,990.00 USD | 19,060.00 USD |
| `1D` | `0.8980` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 0.00 USD | 18,250.00 USD | 871.02 USD |
| `7D` | `0.8980` | 975,980.00 USD | 0.00 USD | 975,980.00 USD | 0.00 USD | 24,060.00 USD | 0.00 USD |
| `1D` | `0.8990` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 3,650.00 USD | 5,880.00 USD | 3,350.00 USD |
| `1D` | `0.9000` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 4,950.00 USD | 15,830.00 USD | 4,120.00 USD |
| `7D` | `0.9000` | 951,920.00 USD | 0.00 USD | 951,920.00 USD | 0.00 USD | 25,040.00 USD | 0.00 USD |
| `1D` | `0.9010` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 538.90 USD | 11,830.00 USD | 2,600.00 USD |
| `1D` | `0.9020` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 3,570.00 USD | 0.00 USD | 414.44 USD |
| `7D` | `0.9020` | 926,880.00 USD | 0.00 USD | 926,880.00 USD | 0.00 USD | 48,090.00 USD | 23,430.00 USD |
| `1D` | `0.9030` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 5,410.00 USD | 17,560.00 USD | 17,810.00 USD |
| `1D` | `0.9040` | 990,280.00 USD | 0.00 USD | 990,280.00 USD | 6,880.00 USD | 5,250.00 USD | 10,940.00 USD |
| `7D` | `0.9040` | 855,370.00 USD | 0.00 USD | 855,370.00 USD | 0.00 USD | 12,290.00 USD | 506.97 USD |
| `1D` | `0.9050` | 967,210.00 USD | 0.00 USD | 967,210.00 USD | 12,450.00 USD | 6,350.00 USD | 11,110.00 USD |
| `1D` | `0.9060` | 937,300.00 USD | 0.00 USD | 937,300.00 USD | 17,690.00 USD | 3,930.00 USD | 14,010.00 USD |
| `7D` | `0.9060` | 842,570.00 USD | 0.00 USD | 842,570.00 USD | 1,910.00 USD | 3,840.00 USD | 42,040.00 USD |
| `1D` | `0.9070` | 901,670.00 USD | 0.00 USD | 901,670.00 USD | 18,960.00 USD | 4,440.00 USD | 19,510.00 USD |
| `1D` | `0.9080` | 858,760.00 USD | 0.00 USD | 858,760.00 USD | 1,500.00 USD | 5,600.00 USD | 0.00 USD |
| `7D` | `0.9080` | 794,790.00 USD | 0.00 USD | 794,790.00 USD | 22,010.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9090` | 851,660.00 USD | 0.00 USD | 851,660.00 USD | 5,600.00 USD | 3,480.00 USD | 239.84 USD |
| `1D` | `0.9100` | 842,350.00 USD | 0.00 USD | 842,350.00 USD | 2,570.00 USD | 0.00 USD | 1,550.00 USD |
| `1D` | `0.9110` | 838,230.00 USD | 0.00 USD | 838,230.00 USD | 22,990.00 USD | 2,850.00 USD | 528.48 USD |
| `1D` | `0.9120` | 811,860.00 USD | 0.00 USD | 811,860.00 USD | 9,340.00 USD | 2,720.00 USD | 2,560.00 USD |
| `1D` | `0.9130` | 797,230.00 USD | 0.00 USD | 797,230.00 USD | 7,740.00 USD | 6,760.00 USD | 19,750.00 USD |
| `1D` | `0.9140` | 762,980.00 USD | 0.00 USD | 762,980.00 USD | 1,860.00 USD | 11,300.00 USD | 13,250.00 USD |
| `7D` | `0.9140` | 772,780.00 USD | 0.00 USD | 772,780.00 USD | 0.00 USD | 515.41 USD | 36,850.00 USD |
| `1D` | `0.9150` | 736,570.00 USD | 0.00 USD | 736,570.00 USD | 9,260.00 USD | 6,480.00 USD | 11,400.00 USD |
| `1D` | `0.9160` | 709,420.00 USD | 0.00 USD | 709,420.00 USD | 0.00 USD | 4,900.00 USD | 7,040.00 USD |
| `7D` | `0.9160` | 735,420.00 USD | 0.00 USD | 735,420.00 USD | 0.00 USD | 12,370.00 USD | 9,800.00 USD |
| `1D` | `0.9170` | 697,480.00 USD | 0.00 USD | 697,480.00 USD | 7,300.00 USD | 11,760.00 USD | 8,050.00 USD |
| `1D` | `0.9180` | 670,370.00 USD | 0.00 USD | 670,370.00 USD | 7,040.00 USD | 3,230.00 USD | 11,570.00 USD |
| `7D` | `0.9180` | 713,240.00 USD | 0.00 USD | 713,240.00 USD | 0.00 USD | 0.00 USD | 23,380.00 USD |
| `1D` | `0.9190` | 648,520.00 USD | 0.00 USD | 648,520.00 USD | 2,860.00 USD | 10,410.00 USD | 4,010.00 USD |
| `1D` | `0.9200` | 631,250.00 USD | 0.00 USD | 631,250.00 USD | 5,710.00 USD | 3,680.00 USD | 5,190.00 USD |
| `7D` | `0.9200` | 689,860.00 USD | 0.00 USD | 689,860.00 USD | 0.00 USD | 4,870.00 USD | 3,970.00 USD |
| `1D` | `0.9210` | 616,660.00 USD | 0.00 USD | 616,660.00 USD | 7,140.00 USD | 0.00 USD | 828.87 USD |
| `1D` | `0.9220` | 608,690.00 USD | 0.00 USD | 608,690.00 USD | 6,600.00 USD | 3,470.00 USD | 48.22 USD |
| `7D` | `0.9220` | 681,020.00 USD | 0.00 USD | 681,020.00 USD | 152,480.00 USD | 7,760.00 USD | 1,010.00 USD |
| `1D` | `0.9230` | 598,570.00 USD | 0.00 USD | 598,570.00 USD | 0.00 USD | 3,670.00 USD | 21,650.00 USD |
| `1D` | `0.9240` | 573,260.00 USD | 0.00 USD | 573,260.00 USD | 88,170.00 USD | 17,120.00 USD | 21,950.00 USD |
| `7D` | `0.9240` | 519,770.00 USD | 0.00 USD | 519,770.00 USD | 141,890.00 USD | 20,480.00 USD | 25,670.00 USD |
| `1D` | `0.9250` | 446,030.00 USD | 0.00 USD | 446,030.00 USD | 11,810.00 USD | 46,150.00 USD | 40,580.00 USD |
| `1D` | `0.9260` | 347,490.00 USD | 0.00 USD | 347,490.00 USD | 23,500.00 USD | 5,610.00 USD | 43,040.00 USD |
| `7D` | `0.9260` | 331,740.00 USD | 0.00 USD | 331,740.00 USD | 44,020.00 USD | 32,300.00 USD | 84,070.00 USD |
| `1D` | `0.9270` | 275,330.00 USD | 0.00 USD | 275,330.00 USD | 16,430.00 USD | 1,430.00 USD | 30,770.00 USD |
| `1D` | `0.9280` | 226,710.00 USD | 0.00 USD | 226,710.00 USD | 75,820.00 USD | 11,000.00 USD | 35,780.00 USD |
| `7D` | `0.9280` | 171,340.00 USD | 0.00 USD | 171,340.00 USD | 0.00 USD | 24,550.00 USD | 1,600.00 USD |
| `1D` | `0.9290` | 104,120.00 USD | 0.00 USD | 104,120.00 USD | 5,140.00 USD | 9,440.00 USD | 2,780.00 USD |
| `1D` | `0.9300` | 86,760.00 USD | 0.00 USD | 86,760.00 USD | 0.00 USD | 5,730.00 USD | 1,060.00 USD |
| `1D` | `0.9310` | 79,980.00 USD | 0.00 USD | 79,980.00 USD | 0.00 USD | 1,400.00 USD | 4,350.00 USD |
| `1D` | `0.9320` | 74,230.00 USD | 0.00 USD | 74,230.00 USD | 0.00 USD | 6,110.00 USD | 181.50 USD |
| `7D` | `0.9320` | 145,190.00 USD | 0.00 USD | 145,190.00 USD | 37,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9330` | 67,930.00 USD | 0.00 USD | 67,930.00 USD | 3,720.00 USD | 30.28 USD | 26,410.00 USD |
| `7D` | `0.9340` | 107,750.00 USD | 0.00 USD | 107,750.00 USD | 0.00 USD | 0.00 USD | 31,370.00 USD |
| `1D` | `0.9350` | 37,770.00 USD | 0.00 USD | 37,770.00 USD | 36,510.00 USD | 221.86 USD | 0.00 USD |
| `1D` | `0.9360` | 1,030.00 USD | 0.00 USD | 1,030.00 USD | 0.00 USD | 91.53 USD | 852.35 USD |
| `7D` | `0.9360` | 76,380.00 USD | 0.00 USD | 76,380.00 USD | 8,250.00 USD | 0.00 USD | 68,130.00 USD |
| `1D` | `0.9370` | 90.48 USD | 0.00 USD | 90.48 USD | 0.00 USD | 90.48 USD | 0.00 USD |
| `7D` | `0.9370` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9380` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9380` | 89,890.00 USD | 89,890.00 USD | 0.00 USD | 42,660.00 USD | 19,540.00 USD | 27,700.00 USD |
| `1D` | `0.9390` | 1,650.00 USD | 1,650.00 USD | 0.00 USD | 1,340.00 USD | 309.30 USD | 0.00 USD |
| `1D` | `0.9400` | 2,560.00 USD | 2,560.00 USD | 0.00 USD | 673.54 USD | 239.40 USD | 0.00 USD |
| `7D` | `0.9400` | 173,120.00 USD | 173,120.00 USD | 0.00 USD | 75,540.00 USD | 474.96 USD | 7,220.00 USD |
| `1D` | `0.9420` | 3,800.00 USD | 3,800.00 USD | 0.00 USD | 1,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9420` | 264,830.00 USD | 264,830.00 USD | 0.00 USD | 91,060.00 USD | 650.60 USD | 0.00 USD |
| `1D` | `0.9430` | 4,020.00 USD | 4,020.00 USD | 0.00 USD | 0.00 USD | 224.96 USD | 0.00 USD |
| `7D` | `0.9440` | 265,550.00 USD | 265,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 713.33 USD |
| `1D` | `0.9460` | 4,300.00 USD | 4,300.00 USD | 0.00 USD | 0.00 USD | 199.60 USD | 79.38 USD |
| `7D` | `0.9460` | 343,200.00 USD | 343,200.00 USD | 0.00 USD | 0.00 USD | 27,270.00 USD | 50,380.00 USD |
| `1D` | `0.9470` | 4,540.00 USD | 4,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 239.84 USD |
| `1D` | `0.9480` | 6,330.00 USD | 6,330.00 USD | 0.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9480` | 451,830.00 USD | 451,830.00 USD | 0.00 USD | 3,540.00 USD | 10,340.00 USD | 94,750.00 USD |
| `1D` | `0.9490` | 85,070.00 USD | 85,070.00 USD | 0.00 USD | 78,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9500` | 90,490.00 USD | 90,490.00 USD | 0.00 USD | 5,190.00 USD | 85.68 USD | 151.50 USD |
| `7D` | `0.9500` | 565,890.00 USD | 565,890.00 USD | 0.00 USD | 85,700.00 USD | 18,830.00 USD | 9,530.00 USD |
| `1D` | `0.9510` | 96,060.00 USD | 96,060.00 USD | 0.00 USD | 0.00 USD | 727.50 USD | 4,840.00 USD |
| `1D` | `0.9520` | 104,550.00 USD | 104,550.00 USD | 0.00 USD | 0.00 USD | 8,490.00 USD | 0.00 USD |
| `7D` | `0.9520` | 751,810.00 USD | 751,810.00 USD | 0.00 USD | 175,720.00 USD | 9,750.00 USD | 447.96 USD |
| `1D` | `0.9530` | 117,680.00 USD | 117,680.00 USD | 0.00 USD | 7,370.00 USD | 0.00 USD | 5,770.00 USD |
| `1D` | `0.9540` | 142,110.00 USD | 142,110.00 USD | 0.00 USD | 10,150.00 USD | 12,540.00 USD | 1,740.00 USD |
| `7D` | `0.9540` | 773,640.00 USD | 773,640.00 USD | 0.00 USD | 0.00 USD | 21,830.00 USD | 0.00 USD |
| `1D` | `0.9550` | 190,670.00 USD | 190,670.00 USD | 0.00 USD | 15,150.00 USD | 26,720.00 USD | 6,690.00 USD |
| `1D` | `0.9560` | 208,670.00 USD | 208,670.00 USD | 0.00 USD | 9,900.00 USD | 3,330.00 USD | 4,770.00 USD |
| `7D` | `0.9560` | 801,740.00 USD | 801,740.00 USD | 0.00 USD | 0.00 USD | 28,100.00 USD | 0.00 USD |
| `1D` | `0.9570` | 224,240.00 USD | 224,240.00 USD | 0.00 USD | 3,780.00 USD | 8,320.00 USD | 3,470.00 USD |
| `1D` | `0.9580` | 233,890.00 USD | 233,890.00 USD | 0.00 USD | 3,480.00 USD | 3,680.00 USD | 2,490.00 USD |
| `7D` | `0.9580` | 817,560.00 USD | 817,560.00 USD | 0.00 USD | 3,880.00 USD | 10,980.00 USD | 957.94 USD |
| `1D` | `0.9590` | 245,910.00 USD | 245,910.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `0.9600` | 261,810.00 USD | 261,810.00 USD | 0.00 USD | 6,600.00 USD | 8,190.00 USD | 1,110.00 USD |
| `7D` | `0.9600` | 849,550.00 USD | 849,550.00 USD | 0.00 USD | 17,690.00 USD | 12,420.00 USD | 1,880.00 USD |
| `1D` | `0.9610` | 303,160.00 USD | 303,160.00 USD | 0.00 USD | 8,160.00 USD | 3,760.00 USD | 29,430.00 USD |
| `1D` | `0.9620` | 423,810.00 USD | 423,810.00 USD | 0.00 USD | 73,570.00 USD | 16,310.00 USD | 30,760.00 USD |
| `7D` | `0.9620` | 891,860.00 USD | 891,860.00 USD | 0.00 USD | 17,990.00 USD | 24,320.00 USD | 0.00 USD |
| `1D` | `0.9630` | 481,440.00 USD | 481,440.00 USD | 0.00 USD | 28,460.00 USD | 14,320.00 USD | 14,850.00 USD |
| `1D` | `0.9640` | 601,310.00 USD | 601,310.00 USD | 0.00 USD | 25,340.00 USD | 29,540.00 USD | 65,000.00 USD |
| `7D` | `0.9640` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 139,390.00 USD | 7,500.00 USD | 96,110.00 USD |
| `1D` | `0.9650` | 622,820.00 USD | 622,820.00 USD | 0.00 USD | 3,740.00 USD | 3,490.00 USD | 14,280.00 USD |
| `1D` | `0.9660` | 668,770.00 USD | 668,770.00 USD | 0.00 USD | 13,160.00 USD | 9,860.00 USD | 22,940.00 USD |
| `7D` | `0.9660` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 5,050.00 USD | 5,170.00 USD | 778.15 USD |
| `1D` | `0.9670` | 719,250.00 USD | 719,250.00 USD | 0.00 USD | 40,820.00 USD | 6,870.00 USD | 2,780.00 USD |
| `1D` | `0.9680` | 737,570.00 USD | 737,570.00 USD | 0.00 USD | 6,000.00 USD | 11,070.00 USD | 1,250.00 USD |
| `7D` | `0.9680` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 38,090.00 USD | 5,870.00 USD | 0.00 USD |
| `1D` | `0.9690` | 760,580.00 USD | 760,580.00 USD | 0.00 USD | 8,860.00 USD | 3,540.00 USD | 10,600.00 USD |
| `1D` | `0.9700` | 814,930.00 USD | 814,930.00 USD | 0.00 USD | 7,640.00 USD | 12,030.00 USD | 34,680.00 USD |
| `7D` | `0.9700` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 30,140.00 USD | 30,730.00 USD |
| `1D` | `0.9710` | 873,900.00 USD | 873,900.00 USD | 0.00 USD | 7,400.00 USD | 7,090.00 USD | 44,480.00 USD |
| `1D` | `0.9720` | 930,200.00 USD | 930,200.00 USD | 0.00 USD | 28,150.00 USD | 3,850.00 USD | 24,300.00 USD |
| `7D` | `0.9720` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 1,430.00 USD | 10,140.00 USD | 31,370.00 USD |
| `1D` | `0.9730` | 977,140.00 USD | 977,140.00 USD | 0.00 USD | 19,870.00 USD | 11,060.00 USD | 16,020.00 USD |
| `1D` | `0.9740` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 13,100.00 USD | 1,620.00 USD | 17,640.00 USD |
| `7D` | `0.9740` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 1,480.00 USD | 25,640.00 USD | 76,600.00 USD |
| `1D` | `0.9750` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 16,550.00 USD | 17,610.00 USD | 16,480.00 USD |
| `1D` | `0.9760` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 38,530.00 USD | 11,220.00 USD | 5,470.00 USD |
| `7D` | `0.9760` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 51,990.00 USD | 19,300.00 USD | 9,280.00 USD |
| `1D` | `0.9770` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 40,380.00 USD | 4,920.00 USD | 7,620.00 USD |
| `1D` | `0.9780` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 4,000.00 USD | 0.00 USD | 10,450.00 USD |
| `7D` | `0.9780` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD | 24,280.00 USD |
| `1D` | `0.9790` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 32,590.00 USD | 11,310.00 USD | 15,870.00 USD |
| `1D` | `0.9800` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 5,740.00 USD | 107.04 USD | 15,250.00 USD |
| `7D` | `0.9800` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 152,980.00 USD |
| `1D` | `0.9810` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 11,240.00 USD | 6,510.00 USD | 13,300.00 USD |
| `1D` | `0.9820` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 21,600.00 USD | 15,460.00 USD | 11,380.00 USD |
| `7D` | `0.9820` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 53,310.00 USD | 19,830.00 USD | 146,200.00 USD |
| `1D` | `0.9830` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 11,750.00 USD | 11,760.00 USD | 44,170.00 USD |
| `1D` | `0.9840` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 2,170.00 USD | 5,110.00 USD | 14,050.00 USD |
| `7D` | `0.9840` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 71,940.00 USD | 211.77 USD | 22,300.00 USD |
| `1D` | `0.9850` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 44,520.00 USD | 3,690.00 USD | 4,780.00 USD |
| `1D` | `0.9860` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 14,650.00 USD | 3,460.00 USD | 21,360.00 USD |
| `7D` | `0.9860` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,390.00 USD |
| `1D` | `0.9870` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 3,010.00 USD | 1,050.00 USD |
| `1D` | `0.9880` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 17,200.00 USD | 700.08 USD | 15,980.00 USD |
| `7D` | `0.9880` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 67,460.00 USD |
| `1D` | `0.9890` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 10,690.00 USD | 3,080.00 USD | 14,210.00 USD |
| `1D` | `0.9900` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 55,800.00 USD | 4,740.00 USD | 18,800.00 USD |
| `7D` | `0.9900` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 22,660.00 USD | 321.20 USD | 16,590.00 USD |
| `1D` | `0.9910` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 4,330.00 USD | 1,150.00 USD | 26,630.00 USD |
| `1D` | `0.9920` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 8,410.00 USD | 3,870.00 USD | 5,300.00 USD |
| `7D` | `0.9920` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 1,570.00 USD | 479.24 USD | 31,040.00 USD |
| `1D` | `0.9930` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 7,910.00 USD | 1,250.00 USD | 2,900.00 USD |
| `1D` | `0.9940` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 17,780.00 USD | 0.00 USD | 7,140.00 USD |
| `7D` | `0.9940` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 29,270.00 USD | 0.00 USD | 39,460.00 USD |
| `1D` | `0.9950` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 11,460.00 USD | 2,120.00 USD | 0.00 USD |
| `1D` | `0.9960` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 7,610.00 USD | 1,480.00 USD | 7,450.00 USD |
| `7D` | `0.9960` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 75,810.00 USD | 5,380.00 USD | 43,230.00 USD |
| `1D` | `0.9970` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 39,340.00 USD | 396.06 USD | 5,580.00 USD |
| `1D` | `0.9980` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 15,330.00 USD | 10,370.00 USD | 10,290.00 USD |
| `7D` | `0.9980` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 53,110.00 USD | 6,740.00 USD | 4,210.00 USD |
| `1D` | `0.9990` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 20,010.00 USD | 7,540.00 USD | 428.72 USD |
| `1D` | `1.00` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 29,250.00 USD | 10,690.00 USD | 6,310.00 USD |
| `7D` | `1.00` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 462.12 USD |
| `1D` | `1.00` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 15,340.00 USD | 105.11 USD | 7,190.00 USD |
| `1D` | `1.00` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 1,570.00 USD | 1,920.00 USD | 73.68 USD |
| `7D` | `1.00` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 56,560.00 USD | 21,850.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 10,790.00 USD | 7,390.00 USD | 6,060.00 USD |
| `1D` | `1.00` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 2,160.00 USD | 3,340.00 USD |
| `7D` | `1.00` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 70,950.00 USD | 3,970.00 USD | 1,470.00 USD |
| `1D` | `1.00` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 54,780.00 USD | 3,360.00 USD | 2,480.00 USD |
| `1D` | `1.01` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 48,890.00 USD | 6,840.00 USD | 13,960.00 USD |
| `7D` | `1.01` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 48,310.00 USD | 240.78 USD | 11,560.00 USD |
| `1D` | `1.01` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 1,710.00 USD | 4,930.00 USD | 24,330.00 USD |
| `1D` | `1.01` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 21,530.00 USD | 4,400.00 USD | 6,630.00 USD |
| `7D` | `1.01` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44,430.00 USD |
| `1D` | `1.01` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 9,350.00 USD | 9,390.00 USD | 971.85 USD |
| `1D` | `1.01` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 3,220.00 USD | 7,840.00 USD | 0.00 USD |
| `7D` | `1.01` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 10,260.00 USD | 14,180.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 6,440.00 USD | 15,620.00 USD | 265.91 USD |
| `1D` | `1.01` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 10,450.00 USD | 104.36 USD | 0.00 USD |
| `7D` | `1.01` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 33,230.00 USD | 30,100.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 1,440.00 USD | 3,780.00 USD |
| `1D` | `1.01` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 7,030.00 USD | 4,350.00 USD | 12,090.00 USD |
| `7D` | `1.01` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 2,870.00 USD | 28,450.00 USD | 735.11 USD |
| `1D` | `1.01` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 7,280.00 USD | 19,430.00 USD | 2,540.00 USD |
| `1D` | `1.02` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 2,130.00 USD | 2,920.00 USD | 7,130.00 USD |
| `7D` | `1.02` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 526.60 USD | 28,470.00 USD | 11,910.00 USD |
| `1D` | `1.02` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 1,860.00 USD | 16.79 USD | 5,560.00 USD |
| `1D` | `1.02` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 24,250.00 USD | 1,140.00 USD | 3,660.00 USD |
| `7D` | `1.02` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 1,430.00 USD | 25,010.00 USD | 21,560.00 USD |
| `1D` | `1.02` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 31,380.00 USD | 3,720.00 USD | 6,990.00 USD |
| `1D` | `1.02` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 2,180.00 USD | 5,820.00 USD | 11,300.00 USD |
| `7D` | `1.02` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 33,820.00 USD | 84,220.00 USD | 44,250.00 USD |
| `1D` | `1.02` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 4,500.00 USD | 1,590.00 USD | 9,720.00 USD |
| `1D` | `1.02` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 21,190.00 USD | 14,220.00 USD | 15,680.00 USD |
| `7D` | `1.02` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 56,930.00 USD | 52,610.00 USD | 112,030.00 USD |
| `1D` | `1.02` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 23,700.00 USD | 4,240.00 USD | 14,260.00 USD |
| `1D` | `1.02` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 19,140.00 USD | 2,930.00 USD | 11,130.00 USD |
| `7D` | `1.02` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 78,220.00 USD | 56,700.00 USD | 86,740.00 USD |
| `1D` | `1.02` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 20,590.00 USD | 4,010.00 USD | 5,950.00 USD |
| `1D` | `1.03` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 8,150.00 USD | 11,760.00 USD | 7,260.00 USD |
| `7D` | `1.03` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 22,650.00 USD | 124,880.00 USD | 33,130.00 USD |
| `1D` | `1.03` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 7,050.00 USD | 106.85 USD | 844.45 USD |
| `1D` | `1.03` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 6,270.00 USD | 3,780.00 USD | 6,310.00 USD |
| `7D` | `1.03` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 250,310.00 USD | 53,000.00 USD | 24,480.00 USD |
| `1D` | `1.03` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 7,800.00 USD | 10,060.00 USD | 9,540.00 USD |
| `1D` | `1.03` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 56,450.00 USD | 4,120.00 USD | 9,930.00 USD |
| `7D` | `1.03` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 134,200.00 USD | 33,660.00 USD | 19,120.00 USD |
| `1D` | `1.03` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 17,790.00 USD | 7,690.00 USD | 22,980.00 USD |
| `1D` | `1.03` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 10,390.00 USD | 1,350.00 USD | 9,870.00 USD |
| `7D` | `1.03` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD |
| `1D` | `1.03` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 6,940.00 USD | 812.59 USD | 7,260.00 USD |
| `1D` | `1.03` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 6,560.00 USD | 8,560.00 USD | 5,940.00 USD |
| `7D` | `1.03` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 217,210.00 USD | 8,290.00 USD | 4,310.00 USD |
| `1D` | `1.03` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 4,560.00 USD | 9,450.00 USD | 910.18 USD |
| `7D` | `1.04` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 262,550.00 USD | 3,170.00 USD | 43,130.00 USD |
| `7D` | `1.04` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 179,470.00 USD | 1,450.00 USD | 215,900.00 USD |
| `7D` | `1.04` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 288,650.00 USD | 9,430.00 USD | 93,080.00 USD |
| `7D` | `1.04` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD |
| `7D` | `1.04` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD |
| `7D` | `1.05` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD |
| `7D` | `1.05` | 7,080,000.00 USD | 7,080,000.00 USD | 0.00 USD | 197,310.00 USD | 28,070.00 USD | 167,700.00 USD |
| `7D` | `1.05` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 87,270.00 USD | 29,070.00 USD | 41,030.00 USD |
| `7D` | `1.05` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 140,530.00 USD | 49,780.00 USD | 143,430.00 USD |
| `7D` | `1.05` | 7,740,000.00 USD | 7,740,000.00 USD | 0.00 USD | 87,130.00 USD | 44,290.00 USD | 36,750.00 USD |
| `7D` | `1.06` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 185,840.00 USD | 48,000.00 USD | 121,890.00 USD |
| `7D` | `1.06` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 205,290.00 USD | 63,350.00 USD | 94,840.00 USD |
| `7D` | `1.06` | 8,870,000.00 USD | 8,870,000.00 USD | 0.00 USD | 217,790.00 USD | 73,000.00 USD | 125,100.00 USD |
| `7D` | `1.06` | 9,130,000.00 USD | 9,130,000.00 USD | 0.00 USD | 115,520.00 USD | 81,560.00 USD | 61,320.00 USD |
| `7D` | `1.06` | 9,250,000.00 USD | 9,250,000.00 USD | 0.00 USD | 91,360.00 USD | 25,320.00 USD | 0.00 USD |

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
  * Current Rate: `3.73K` | Last 24h: `6.26K` | Last 3d: `-7.35K` | Last 7d: `-25.50K`
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
| `15M` | `DOT` | `47.94%` | `52.06%` | `0.92` | 2,340,000.00 USD |
| `15M` | `Binance` | `66.18%` | `33.82%` | `1.96` | 437,960.00 USD |
| `15M` | `OKX` | `44.39%` | `55.61%` | `0.80` | 77,120.00 USD |
| `15M` | `Bybit` | `62.89%` | `37.11%` | `1.69` | 90,330.00 USD |
| `15M` | `KuCoin` | `75.09%` | `24.91%` | `3.01` | 97,500.00 USD |
| `15M` | `Gate` | `50.1%` | `49.9%` | `1.00` | 35,460.00 USD |
| `15M` | `Bitget` | `61.09%` | `38.91%` | `1.57` | 11,960.00 USD |
| `15M` | `BingX` | `6.78%` | `93.22%` | `0.07` | 510,030.00 USD |
| `15M` | `MEXC` | `75.64%` | `24.36%` | `3.11` | 59,230.00 USD |
| `15M` | `Bitunix` | `66.58%` | `33.42%` | `1.99` | 47,030.00 USD |
| `15M` | `Hyperliquid` | `94.41%` | `5.59%` | `16.89` | 43,250.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.28%` | `49.72%` | `1.01` | 755,350.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `99.14%` | `0.86%` | `115.28` | 92,340.00 USD |
| `15M` | `HTX` | `37.02%` | `62.98%` | `0.59` | 509.20 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `17%` | `83%` | `0.20` | 71,300.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 533.16 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `100%` | `0%` | `1.00` | 4,140.00 USD |
| `15M` | `Whale Positions` | `66.18%` | `33.82%` | `1.96` | 437,960.00 USD |
| `15M` | `Global Accounts` | `47.94%` | `52.06%` | `0.92` | 2,340,000.00 USD |
| `1H` | `DOT` | `51.13%` | `48.87%` | `1.05` | 7,160,000.00 USD |
| `1H` | `Binance` | `49.27%` | `50.73%` | `0.97` | 1,610,000.00 USD |
| `1H` | `OKX` | `45.69%` | `54.31%` | `0.84` | 557,970.00 USD |
| `1H` | `Bybit` | `54.27%` | `45.73%` | `1.19` | 295,380.00 USD |
| `1H` | `KuCoin` | `59.1%` | `40.9%` | `1.44` | 585,700.00 USD |
| `1H` | `Gate` | `45.66%` | `54.34%` | `0.84` | 113,520.00 USD |
| `1H` | `Bitget` | `44.57%` | `55.43%` | `0.80` | 90,590.00 USD |
| `1H` | `BingX` | `23.12%` | `76.88%` | `0.30` | 818,280.00 USD |
| `1H` | `MEXC` | `60.19%` | `39.81%` | `1.51` | 169,500.00 USD |
| `1H` | `Bitunix` | `54.37%` | `45.63%` | `1.19` | 172,540.00 USD |
| `1H` | `Hyperliquid` | `77.28%` | `22.72%` | `3.40` | 135,070.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.14%` | `49.86%` | `1.01` | 2,040,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `98.61%` | `1.39%` | `70.94` | 461,720.00 USD |
| `1H` | `HTX` | `17.45%` | `82.55%` | `0.21` | 5,540.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `23.13%` | `76.87%` | `0.30` | 83,880.00 USD |
| `1H` | `Aster` | `67.83%` | `32.17%` | `2.11` | 2,040.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `96.37%` | `3.63%` | `26.55` | 34,030.00 USD |
| `1H` | `Whale Positions` | `49.27%` | `50.73%` | `0.97` | 1,610,000.00 USD |
| `1H` | `Global Accounts` | `51.13%` | `48.87%` | `1.05` | 7,160,000.00 USD |
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
| `0:00 UTC` | `0.9378` | `0.9391` | `0.9378` | `0.9427` | `0.9366` | 674,681.66 USD | 251,815.20 USD | 422,866.46 USD | -171,051.26 USD | `-25.35%` | `2B / 15S` |
| `5:00 UTC` | `0.9365` | `0.9373` | `0.9365` | `0.9404` | `0.9360` | 347,308.90 USD | 133,864.50 USD | 213,444.40 USD | -79,579.90 USD | `-22.91%` | `8B / 13S` |
| `0:00 UTC` | `0.9349` | `0.9360` | `0.9349` | `0.9390` | `0.9338` | 565,103.94 USD | 170,366.16 USD | 394,737.78 USD | -224,371.62 USD | `-39.70%` | `1B / 22S` |
| `5:00 UTC` | `0.9357` | `0.9351` | `0.9357` | `0.9366` | `0.9332` | 272,828.10 USD | 122,126.72 USD | 150,701.37 USD | -28,574.65 USD | `-10.47%` | `1B / 6S` |
| `0:00 UTC` | `0.9343` | `0.9337` | `0.9343` | `0.9365` | `0.9315` | 323,640.65 USD | 113,112.66 USD | 210,527.99 USD | -97,415.33 USD | `-30.10%` | `2B / 14S` |
| `5:00 UTC` | `0.9312` | `0.9319` | `0.9312` | `0.9351` | `0.9293` | 338,159.00 USD | 113,706.78 USD | 224,452.22 USD | -110,745.44 USD | `-32.75%` | `4B / 15S` |
| `0:00 UTC` | `0.9326` | `0.9327` | `0.9326` | `0.9345` | `0.9304` | 383,267.52 USD | 169,541.73 USD | 213,725.79 USD | -44,184.07 USD | `-11.53%` | `4B / 8S` |
| `5:00 UTC` | `0.9325` | `0.9329` | `0.9325` | `0.9366` | `0.9303` | 250,363.19 USD | 100,290.83 USD | 150,072.35 USD | -49,781.52 USD | `-19.88%` | `3B / 19S` |
| `0:00 UTC` | `0.9365` | `0.9367` | `0.9365` | `0.9399` | `0.9325` | 603,897.34 USD | 304,683.07 USD | 299,214.28 USD | 5,468.79 USD | `+0.91%` | `10B / 15S` |
| `5:00 UTC` | `0.9374` | `0.9378` | `0.9374` | `0.9395` | `0.9368` | 132,574.03 USD | 76,042.79 USD | 56,531.23 USD | 19,511.56 USD | `+14.72%` | `3B / 4S` |

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
| `5m` | 6,490.00 USD | 16,260.00 USD | **`ACCUMULATION`** |
| `15m` | -53,700.00 USD | 78,570.00 USD | **`ACCUMULATION`** |
| `30m` | -18,310.00 USD | -47,800.00 USD | **`DISTRIBUTION`** |
| `1h` | -69,640.00 USD | -161,340.00 USD | **`DISTRIBUTION`** |
| `2h` | -112,290.00 USD | -757,190.00 USD | **`DISTRIBUTION`** |
| `4h` | -128,220.00 USD | -1,420,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -246,290.00 USD | -2,680,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -197,000.00 USD | -1,840,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -490,230.00 USD | -1,430,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,360,000.00 USD | -9,400,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,930,000.00 USD | -23,560,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,860,000.00 USD | -78,880,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+6.49K` | 15m=`-53.70K` | 1h=`-69.64K` | 24h=`-1.36M`
* Futures Capital Netflows: 5m=`+16.26K` | 15m=`+78.57K` | 1h=`-161.34K` | 24h=`-9.40M`
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
  * `2026-10-30 15:50:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.9004` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.8609` (Risk Distance: `0.0420` pts)
  * +2.5R Take Profit: `1.01`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9447` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9842` (Risk Distance: `0.0420` pts)
  * +2.5R Take Profit: `0.8397`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9450`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
