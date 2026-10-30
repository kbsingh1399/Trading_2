# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 16:36:47 IST` (`2026-10-30 11:06:47 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9330` | **Live Ask Quote**: `0.9530` | **Mid Price**: `0.9430`
- **Spread Points**: `20.00` | **Spread BPS**: `212.09 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.9108` | VWAP Z-Score: `+0.92` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0066` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `55.37` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.9796` | Lower -3.00σ Band: `0.8421`
  * Upper +2.51σ Band: `0.9684` | Lower -2.51σ Band: `0.8533`
  * Upper +2.01σ Band: `0.9569` | Lower -2.01σ Band: `0.8648`
  * Upper +2.00σ Band: `0.9567` | Lower -2.00σ Band: `0.8650`
  * Upper +1.28σ Band: `0.9402` | Lower -1.28σ Band: `0.8815`
  * Upper +1.00σ Band: `0.9338` | Lower -1.00σ Band: `0.8879`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9268` | EMA-20=`0.9274` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9292` (Slope: `+0.0000`) | EMA-100=`0.9398`
  * Institutional Anchors: EMA-144=`0.9477` | EMA-200=`0.9559` (Slope: `-0.3935`) | EMA-233=`0.9590`
- **Range Boundaries**: 24H High=`1.01` | 24H Low=`0.8570` | Weekly High=`1.03` | Weekly Low=`0.8570`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9447` (Distance: `-0.18%`)
  * Point of Control (POC) = `0.9119` (Distance: `+3.41%`)
  * Value Area Low (VAL) = `0.9004` (Distance: `+4.73%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.02` | Weekly POC=`0.9945` | Weekly VAL=`0.9689`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9330` | Low=`0.8570`
  * London Session (08:00-16:00 UTC): High=`0.9480` | Low=`0.9190`
  * New York Session (13:00-21:00 UTC): High=`0.9330` | Low=`0.9190`
  * Initial Balance (First Hour): IB High=`0.9480` | IB Low=`0.9290`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9392` - `0.9468`
  * Optimal Trade Entry (OTE 0.705): `0.9449`
  * Structural Invalidation Anchor (0.786): `0.9505`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9372` | `0.9399` | `0.9370` | `0.9383` | `150,261` | 140,987.53 USD | 49,839.93 USD | `+35.35%` | -6,036,571.63 USD | `+2.12` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.9384` | `0.9395` | `0.9368` | `0.9375` | `144,089` | 135,115.87 USD | 18,401.27 USD | `+13.62%` | -6,018,170.37 USD | `+1.30` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.9374` | `0.9390` | `0.9366` | `0.9390` | `43,694` | 40,958.16 USD | 15,277.09 USD | `+37.30%` | -6,002,893.28 USD | `+1.07` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.9327` | `0.9399` | `0.9325` | `0.9383` | `644,715` | 603,897.34 USD | 5,468.79 USD | `+0.91%` | -5,905,463.42 USD | `+0.91` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.9384` | `0.9430` | `0.9366` | `0.9428` | `386,274` | 362,865.52 USD | 12,654.86 USD | `+3.49%` | -5,892,808.56 USD | `+0.94` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.9427` | `0.9442` | `0.9422` | `0.9435` | `118,788` | 112,059.58 USD | 32,508.90 USD | `+29.01%` | -5,860,299.66 USD | `+1.10` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.9375` | `0.9390` | `0.9292` | `0.9340` | `1,605,127` | 1,499,731.69 USD | -461,107.04 USD | `-30.75%` | -5,771,335.00 USD | `-0.17` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.9340` | `0.9430` | `0.9302` | `0.9428` | `1,710,321` | 1,600,393.57 USD | -75,841.93 USD | `-4.74%` | -5,847,176.93 USD | `+0.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9427` | `0.9442` | `0.9422` | `0.9435` | `118,788` | 112,059.58 USD | 32,508.90 USD | `+29.01%` | -5,814,668.03 USD | `+0.33` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,092,983.65 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9603` | `0.9263` | `0.9454` | `10,832,060` | 10,247,507.62 USD | -822,915.31 USD | `-8.03%` | -4,915,898.96 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9454` | `0.9488` | `0.9292` | `0.9390` | `4,970,016` | 4,657,599.64 USD | -910,254.48 USD | `-19.54%` | -5,826,153.44 USD | `+0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -974,642.25 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,499,370.98 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,092,983.65 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9603` | `0.9263` | `0.9454` | `10,832,060` | 10,247,507.62 USD | -822,915.31 USD | `-8.03%` | -4,915,898.96 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9454` | `0.9488` | `0.9292` | `0.9434` | `5,287,338` | 4,956,492.51 USD | -898,810.87 USD | `-18.13%` | -5,814,709.83 USD | `+0.04` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`0.9430`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

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
| `ANNOUNCEMENT` | `INFO` | `0.9575` | 1,531.95 USD | `-` | `NEWS_INTEL` | `-` | #DOT Liquidated Short: 1.53K USD at 0.9575 USD [API] | `2026-10-29 20:06:52` |
| `ANNOUNCEMENT` | `INFO` | `0.9679` | 6,377.95 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale BUY: 6.38K USD at 0.9679 USD [API] | `2026-10-29 20:21:54` |


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
| `Live` | `Long Liquidation` | `0.7985` | 210.40 USD | 114,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8000` | 3,250,000.00 USD | 3,250,000.00 USD | 21,120.00 USD | 8,540.00 USD | 16,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8020` | 3,200,000.00 USD | 3,200,000.00 USD | 8,990.00 USD | 4,460.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8040` | 3,180,000.00 USD | 3,180,000.00 USD | 5,500.00 USD | 2,170.00 USD | 940.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8060` | 3,170,000.00 USD | 3,170,000.00 USD | 16,390.00 USD | 10,990.00 USD | 10,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8080` | 3,130,000.00 USD | 3,130,000.00 USD | 1,570.00 USD | 1,230.00 USD | 10,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8100` | 3,120,000.00 USD | 3,120,000.00 USD | 2,890.00 USD | 2,010.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8120` | 3,110,000.00 USD | 3,110,000.00 USD | 15,720.00 USD | 3,030.00 USD | 9,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 114,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8140` | 3,080,000.00 USD | 3,080,000.00 USD | 32,880.00 USD | 6,050.00 USD | 15,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8160` | 3,030,000.00 USD | 3,030,000.00 USD | 38,200.00 USD | 10,180.00 USD | 6,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8180` | 2,970,000.00 USD | 2,970,000.00 USD | 12,550.00 USD | 2,560.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8200` | 2,950,000.00 USD | 2,950,000.00 USD | 1,740.00 USD | 1,570.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 113,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8220` | 2,930,000.00 USD | 2,930,000.00 USD | 20,390.00 USD | 6,820.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 749.96 USD | 111,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8240` | 2,900,000.00 USD | 2,900,000.00 USD | 23,160.00 USD | 93.73 USD | 11,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8260` | 2,870,000.00 USD | 2,870,000.00 USD | 5,220.00 USD | 3,490.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8280` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 3,910.00 USD | 1,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8300` | 2,850,000.00 USD | 2,850,000.00 USD | 9,280.00 USD | 4,780.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8320` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 401.80 USD | 77.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8340` | 2,840,000.00 USD | 2,840,000.00 USD | 35,710.00 USD | 10,960.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8360` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 844.23 USD | 311.26 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 110,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8370` | 2,440,000.00 USD | 2,440,000.00 USD | 18,140.00 USD | 2,530.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8380` | 2,790,000.00 USD | 2,790,000.00 USD | 15,240.00 USD | 633.60 USD | 539.92 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8390` | 2,400,000.00 USD | 2,400,000.00 USD | 1,740.00 USD | 745.84 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8400` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 798.38 USD | 8,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8410` | 2,390,000.00 USD | 2,390,000.00 USD | 1,470.00 USD | 2,040.00 USD | 1,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,570.00 USD | 110,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8420` | 2,760,000.00 USD | 2,760,000.00 USD | 6,400.00 USD | 7,120.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8430` | 2,390,000.00 USD | 2,390,000.00 USD | 4,670.00 USD | 6,880.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8440` | 2,740,000.00 USD | 2,740,000.00 USD | 7,170.00 USD | 24.80 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8450` | 2,380,000.00 USD | 2,380,000.00 USD | 2,360.00 USD | 8,430.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8460` | 2,740,000.00 USD | 2,740,000.00 USD | 2,560.00 USD | 427.62 USD | 2,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8470` | 2,370,000.00 USD | 2,370,000.00 USD | 24,110.00 USD | 1,110.00 USD | 165.77 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8480` | 2,730,000.00 USD | 2,730,000.00 USD | 26,310.00 USD | 10,990.00 USD | 202.79 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8490` | 2,340,000.00 USD | 2,340,000.00 USD | 5,120.00 USD | 2,400.00 USD | 7,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 108,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8500` | 2,690,000.00 USD | 2,690,000.00 USD | 3,110.00 USD | 638.56 USD | 21,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8510` | 2,320,000.00 USD | 2,320,000.00 USD | 13,560.00 USD | 4,140.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8520` | 2,670,000.00 USD | 2,670,000.00 USD | 14,700.00 USD | 669.43 USD | 226.67 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8530` | 2,290,000.00 USD | 2,290,000.00 USD | 4,680.00 USD | 3,830.00 USD | 5,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8540` | 2,650,000.00 USD | 2,650,000.00 USD | 254.55 USD | 2,660.00 USD | 5,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8550` | 2,280,000.00 USD | 2,280,000.00 USD | 18,270.00 USD | 3,040.00 USD | 5,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8560` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 842.92 USD | 2,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8570` | 2,250,000.00 USD | 2,250,000.00 USD | 989.11 USD | 1,720.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 107,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8580` | 2,640,000.00 USD | 2,640,000.00 USD | 3,540.00 USD | 101.30 USD | 7,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8590` | 2,240,000.00 USD | 2,240,000.00 USD | 6,870.00 USD | 10,640.00 USD | 6,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8600` | 2,630,000.00 USD | 2,630,000.00 USD | 6,780.00 USD | 211.77 USD | 10,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8610` | 2,220,000.00 USD | 2,220,000.00 USD | 8,320.00 USD | 855.53 USD | 16,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8620` | 2,610,000.00 USD | 2,610,000.00 USD | 7,670.00 USD | 6,050.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8630` | 2,190,000.00 USD | 2,190,000.00 USD | 39,330.00 USD | 12,290.00 USD | 2,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 107,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8640` | 2,570,000.00 USD | 2,570,000.00 USD | 4,820.00 USD | 321.30 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 106,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8650` | 2,140,000.00 USD | 2,140,000.00 USD | 17,640.00 USD | 2,110.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8660` | 2,570,000.00 USD | 2,570,000.00 USD | 45,020.00 USD | 19,050.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,390.00 USD | 106,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8670` | 2,120,000.00 USD | 2,120,000.00 USD | 12,000.00 USD | 10,090.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8680` | 2,500,000.00 USD | 2,500,000.00 USD | 92,530.00 USD | 14,760.00 USD | 50,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8690` | 2,090,000.00 USD | 2,090,000.00 USD | 42,010.00 USD | 3,780.00 USD | 29,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 12,590.00 USD | 105,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8700` | 2,340,000.00 USD | 2,340,000.00 USD | 81,840.00 USD | 9,460.00 USD | 7,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8705` | 92,480.00 USD | 92,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8710` | 2,020,000.00 USD | 2,020,000.00 USD | 42,290.00 USD | 24,900.00 USD | 28,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8720` | 2,240,000.00 USD | 2,240,000.00 USD | 5,420.00 USD | 18,020.00 USD | 11,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8730` | 1,920,000.00 USD | 1,920,000.00 USD | 54,500.00 USD | 21,510.00 USD | 25,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8740` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 12,360.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8750` | 1,820,000.00 USD | 1,820,000.00 USD | 36,800.00 USD | 6,900.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8760` | 2,190,000.00 USD | 2,190,000.00 USD | 766.43 USD | 0.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8770` | 1,760,000.00 USD | 1,760,000.00 USD | 10,480.00 USD | 152.79 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8780` | 2,190,000.00 USD | 2,190,000.00 USD | 1,500.00 USD | 0.00 USD | 33,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8790` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 40.93 USD | 50,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8800` | 2,150,000.00 USD | 2,150,000.00 USD | 1,600.00 USD | 5,820.00 USD | 51,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8810` | 1,700,000.00 USD | 1,700,000.00 USD | 13,820.00 USD | 5,210.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8820` | 2,090,000.00 USD | 2,090,000.00 USD | 454.20 USD | 9,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8830` | 1,670,000.00 USD | 1,670,000.00 USD | 656.20 USD | 5,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8840` | 2,080,000.00 USD | 2,080,000.00 USD | 2,090.00 USD | 6,440.00 USD | 15,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8850` | 1,670,000.00 USD | 1,670,000.00 USD | 5,680.00 USD | 34,880.00 USD | 11,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8860` | 2,060,000.00 USD | 2,060,000.00 USD | 141,730.00 USD | 22,320.00 USD | 78,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8870` | 1,620,000.00 USD | 1,620,000.00 USD | 68,710.00 USD | 16,710.00 USD | 32,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8880` | 1,820,000.00 USD | 1,820,000.00 USD | 130,140.00 USD | 31,410.00 USD | 9,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8890` | 1,500,000.00 USD | 1,500,000.00 USD | 69,610.00 USD | 40,830.00 USD | 4,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8900` | 1,640,000.00 USD | 1,640,000.00 USD | 108,250.00 USD | 45,590.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8910` | 1,380,000.00 USD | 1,380,000.00 USD | 2,410.00 USD | 38,730.00 USD | 20,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8920` | 1,460,000.00 USD | 1,460,000.00 USD | 46,210.00 USD | 38,810.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8930` | 1,320,000.00 USD | 1,320,000.00 USD | 56,810.00 USD | 24,630.00 USD | 37,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8940` | 1,360,000.00 USD | 1,360,000.00 USD | 45,210.00 USD | 12,120.00 USD | 26,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8950` | 1,200,000.00 USD | 1,200,000.00 USD | 6,700.00 USD | 15,420.00 USD | 8,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8960` | 1,280,000.00 USD | 1,280,000.00 USD | 2,140.00 USD | 32,820.00 USD | 93,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8970` | 1,170,000.00 USD | 1,170,000.00 USD | 8,300.00 USD | 27,310.00 USD | 19,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8980` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 24,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8990` | 1,120,000.00 USD | 1,120,000.00 USD | 3,650.00 USD | 24,130.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9000` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 25,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9010` | 1,090,000.00 USD | 1,090,000.00 USD | 5,490.00 USD | 28,480.00 USD | 7,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9020` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 48,090.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9030` | 1,040,000.00 USD | 1,040,000.00 USD | 10,610.00 USD | 17,560.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9040` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 12,290.00 USD | 506.97 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9050` | 998,230.00 USD | 998,230.00 USD | 19,330.00 USD | 11,600.00 USD | 22,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9060` | 1,020,000.00 USD | 1,020,000.00 USD | 1,910.00 USD | 3,840.00 USD | 42,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9070` | 945,250.00 USD | 945,250.00 USD | 36,650.00 USD | 8,370.00 USD | 33,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9080` | 967,910.00 USD | 967,910.00 USD | 22,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9090` | 866,710.00 USD | 866,710.00 USD | 7,100.00 USD | 9,080.00 USD | 239.84 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9110` | 850,290.00 USD | 850,290.00 USD | 25,560.00 USD | 2,850.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9130` | 819,800.00 USD | 819,800.00 USD | 17,080.00 USD | 9,480.00 USD | 22,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9140` | 945,900.00 USD | 945,900.00 USD | 0.00 USD | 515.41 USD | 36,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9150` | 770,920.00 USD | 770,920.00 USD | 11,120.00 USD | 17,780.00 USD | 24,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9160` | 908,540.00 USD | 908,540.00 USD | 0.00 USD | 12,370.00 USD | 9,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9170` | 717,370.00 USD | 717,370.00 USD | 7,300.00 USD | 16,660.00 USD | 15,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9180` | 886,360.00 USD | 886,360.00 USD | 0.00 USD | 0.00 USD | 23,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9190` | 678,320.00 USD | 678,320.00 USD | 9,900.00 USD | 15,280.00 USD | 16,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9200` | 862,980.00 USD | 862,980.00 USD | 0.00 USD | 4,870.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9210` | 636,160.00 USD | 636,160.00 USD | 12,850.00 USD | 3,680.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9220` | 854,140.00 USD | 854,140.00 USD | 152,480.00 USD | 7,760.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9230` | 613,600.00 USD | 613,600.00 USD | 9,860.00 USD | 7,140.00 USD | 21,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9240` | 692,890.00 USD | 692,890.00 USD | 141,890.00 USD | 20,480.00 USD | 25,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9250` | 574,910.00 USD | 574,910.00 USD | 99,970.00 USD | 63,270.00 USD | 62,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9260` | 504,860.00 USD | 504,860.00 USD | 44,020.00 USD | 32,300.00 USD | 84,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9270` | 349,140.00 USD | 349,140.00 USD | 39,920.00 USD | 7,040.00 USD | 73,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9280` | 344,470.00 USD | 344,470.00 USD | 0.00 USD | 24,550.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9290` | 228,370.00 USD | 228,370.00 USD | 80,950.00 USD | 20,440.00 USD | 38,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9310` | 88,410.00 USD | 88,410.00 USD | 0.00 USD | 7,130.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9320` | 318,320.00 USD | 318,320.00 USD | 37,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9330` | 75,880.00 USD | 75,880.00 USD | 3,720.00 USD | 6,140.00 USD | 26,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9340` | 280,870.00 USD | 280,870.00 USD | 0.00 USD | 0.00 USD | 31,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9350` | 39,420.00 USD | 39,420.00 USD | 36,510.00 USD | 221.86 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9360` | 249,500.00 USD | 249,500.00 USD | 8,250.00 USD | 0.00 USD | 68,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9370` | 2,690.00 USD | 2,690.00 USD | 0.00 USD | 182.01 USD | 852.35 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9380` | 173,120.00 USD | 173,120.00 USD | 42,660.00 USD | 19,540.00 USD | 27,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9390` | 1,650.00 USD | 1,650.00 USD | 1,340.00 USD | 309.30 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9400` | 83,230.00 USD | 83,230.00 USD | 75,540.00 USD | 474.96 USD | 7,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9410` | 912.94 USD | 912.94 USD | 673.54 USD | 239.40 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9410` | 1,830.00 USD | 1,830.00 USD | 673.54 USD | 239.40 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9420` | 91,710.00 USD | 91,710.00 USD | 91,060.00 USD | 650.60 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9430` | 3,280.00 USD | 3,280.00 USD | 1,230.00 USD | 224.96 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9440` | 92,420.00 USD | 92,420.00 USD | 0.00 USD | 0.00 USD | 713.33 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9460` | 170,070.00 USD | 170,070.00 USD | 0.00 USD | 27,270.00 USD | 50,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9470` | 3,800.00 USD | 3,800.00 USD | 0.00 USD | 199.60 USD | 319.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9480` | 278,710.00 USD | 278,710.00 USD | 3,540.00 USD | 10,340.00 USD | 94,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9490` | 84,330.00 USD | 84,330.00 USD | 80,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9500` | 392,770.00 USD | 392,770.00 USD | 85,700.00 USD | 18,830.00 USD | 9,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9510` | 95,320.00 USD | 95,320.00 USD | 5,190.00 USD | 813.18 USD | 4,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9520` | 578,690.00 USD | 578,690.00 USD | 175,720.00 USD | 9,750.00 USD | 447.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9530` | 116,950.00 USD | 116,950.00 USD | 7,370.00 USD | 8,490.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9540` | 600,520.00 USD | 600,520.00 USD | 0.00 USD | 21,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9550` | 189,940.00 USD | 189,940.00 USD | 25,300.00 USD | 39,260.00 USD | 8,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9560` | 628,620.00 USD | 628,620.00 USD | 0.00 USD | 28,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9570` | 226,530.00 USD | 226,530.00 USD | 13,680.00 USD | 13,280.00 USD | 9,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9580` | 644,440.00 USD | 644,440.00 USD | 3,880.00 USD | 10,980.00 USD | 957.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9590` | 248,210.00 USD | 248,210.00 USD | 14,060.00 USD | 3,680.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9600` | 676,430.00 USD | 676,430.00 USD | 17,690.00 USD | 12,420.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9610` | 308,720.00 USD | 308,720.00 USD | 18,020.00 USD | 11,950.00 USD | 30,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9620` | 718,740.00 USD | 718,740.00 USD | 17,990.00 USD | 24,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9630` | 487,000.00 USD | 487,000.00 USD | 102,030.00 USD | 30,630.00 USD | 45,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9640` | 961,740.00 USD | 961,740.00 USD | 139,390.00 USD | 7,500.00 USD | 96,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9650` | 628,380.00 USD | 628,380.00 USD | 29,080.00 USD | 33,020.00 USD | 79,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9660` | 972,730.00 USD | 972,730.00 USD | 5,050.00 USD | 5,170.00 USD | 778.15 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9670` | 724,810.00 USD | 724,810.00 USD | 53,970.00 USD | 16,730.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9680` | 1,020,000.00 USD | 1,020,000.00 USD | 38,090.00 USD | 5,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9690` | 766,140.00 USD | 766,140.00 USD | 14,860.00 USD | 14,610.00 USD | 11,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9700` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 30,140.00 USD | 30,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9710` | 879,460.00 USD | 879,460.00 USD | 15,040.00 USD | 19,120.00 USD | 79,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9720` | 1,120,000.00 USD | 1,120,000.00 USD | 1,430.00 USD | 10,140.00 USD | 31,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9730` | 972,540.00 USD | 972,540.00 USD | 37,900.00 USD | 14,900.00 USD | 40,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9740` | 1,220,000.00 USD | 1,220,000.00 USD | 1,480.00 USD | 25,640.00 USD | 76,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9750` | 1,050,000.00 USD | 1,050,000.00 USD | 29,660.00 USD | 13,550.00 USD | 34,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9760` | 1,300,000.00 USD | 1,300,000.00 USD | 51,990.00 USD | 19,300.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9770` | 1,160,000.00 USD | 1,160,000.00 USD | 78,910.00 USD | 16,960.00 USD | 13,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9780` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 3,880.00 USD | 24,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9790` | 1,240,000.00 USD | 1,240,000.00 USD | 38,220.00 USD | 11,310.00 USD | 26,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9800` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 152,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 102.95 USD | 102.95 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9810` | 1,290,000.00 USD | 1,290,000.00 USD | 16,990.00 USD | 6,620.00 USD | 28,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9820` | 1,710,000.00 USD | 1,710,000.00 USD | 53,310.00 USD | 19,830.00 USD | 146,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9830` | 1,400,000.00 USD | 1,400,000.00 USD | 33,340.00 USD | 27,220.00 USD | 55,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9840` | 1,800,000.00 USD | 1,800,000.00 USD | 71,940.00 USD | 211.77 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9850` | 1,480,000.00 USD | 1,480,000.00 USD | 46,950.00 USD | 8,800.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9860` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9870` | 1,520,000.00 USD | 1,520,000.00 USD | 14,650.00 USD | 6,470.00 USD | 22,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9880` | 1,910,000.00 USD | 1,910,000.00 USD | 40,020.00 USD | 0.00 USD | 67,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9890` | 1,580,000.00 USD | 1,580,000.00 USD | 27,890.00 USD | 3,780.00 USD | 30,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9900` | 1,950,000.00 USD | 1,950,000.00 USD | 22,660.00 USD | 321.20 USD | 16,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9910` | 1,700,000.00 USD | 1,700,000.00 USD | 60,130.00 USD | 5,890.00 USD | 45,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9920` | 1,980,000.00 USD | 1,980,000.00 USD | 1,570.00 USD | 479.24 USD | 31,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9925` | 3,940.00 USD | 4,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9930` | 1,720,000.00 USD | 1,720,000.00 USD | 16,320.00 USD | 5,130.00 USD | 8,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9940` | 2,050,000.00 USD | 2,050,000.00 USD | 29,270.00 USD | 0.00 USD | 39,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9950` | 1,760,000.00 USD | 1,760,000.00 USD | 29,250.00 USD | 2,120.00 USD | 7,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9960` | 2,170,000.00 USD | 2,170,000.00 USD | 75,810.00 USD | 5,380.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9970` | 1,830,000.00 USD | 1,830,000.00 USD | 46,950.00 USD | 1,870.00 USD | 13,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9980` | 2,240,000.00 USD | 2,240,000.00 USD | 53,110.00 USD | 6,740.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9985` | 852.22 USD | 4,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9990` | 1,890,000.00 USD | 1,890,000.00 USD | 35,340.00 USD | 17,910.00 USD | 10,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,290,000.00 USD | 2,290,000.00 USD | 52,850.00 USD | 0.00 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,960,000.00 USD | 1,960,000.00 USD | 44,780.00 USD | 10,790.00 USD | 13,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,390,000.00 USD | 2,390,000.00 USD | 56,560.00 USD | 21,850.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,990,000.00 USD | 1,990,000.00 USD | 12,370.00 USD | 9,310.00 USD | 6,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,460,000.00 USD | 2,460,000.00 USD | 70,950.00 USD | 3,970.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,050,000.00 USD | 2,050,000.00 USD | 54,780.00 USD | 5,520.00 USD | 5,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,520,000.00 USD | 2,520,000.00 USD | 48,310.00 USD | 240.78 USD | 11,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,150,000.00 USD | 2,150,000.00 USD | 50,600.00 USD | 11,770.00 USD | 38,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 44,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,200,000.00 USD | 2,200,000.00 USD | 30,870.00 USD | 13,790.00 USD | 7,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,590,000.00 USD | 2,590,000.00 USD | 10,260.00 USD | 14,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,240,000.00 USD | 2,240,000.00 USD | 9,660.00 USD | 23,460.00 USD | 265.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,660,000.00 USD | 2,660,000.00 USD | 33,230.00 USD | 30,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,250,000.00 USD | 2,250,000.00 USD | 10,450.00 USD | 1,540.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,690,000.00 USD | 2,690,000.00 USD | 2,870.00 USD | 28,450.00 USD | 735.11 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,300,000.00 USD | 2,300,000.00 USD | 14,310.00 USD | 18,100.00 USD | 14,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,730,000.00 USD | 2,730,000.00 USD | 526.60 USD | 28,470.00 USD | 11,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,320,000.00 USD | 2,320,000.00 USD | 3,990.00 USD | 2,940.00 USD | 12,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,780,000.00 USD | 2,780,000.00 USD | 1,430.00 USD | 25,010.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,390,000.00 USD | 2,390,000.00 USD | 55,630.00 USD | 4,860.00 USD | 10,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 760.04 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,940,000.00 USD | 2,940,000.00 USD | 33,820.00 USD | 84,220.00 USD | 44,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,430,000.00 USD | 2,430,000.00 USD | 6,670.00 USD | 7,410.00 USD | 21,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,160,000.00 USD | 3,160,000.00 USD | 56,930.00 USD | 52,610.00 USD | 112,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,520,000.00 USD | 2,520,000.00 USD | 44,890.00 USD | 18,460.00 USD | 29,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,380,000.00 USD | 3,380,000.00 USD | 78,220.00 USD | 56,700.00 USD | 86,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,580,000.00 USD | 2,580,000.00 USD | 39,730.00 USD | 6,940.00 USD | 17,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,560,000.00 USD | 3,560,000.00 USD | 22,650.00 USD | 124,880.00 USD | 33,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,620,000.00 USD | 2,620,000.00 USD | 15,190.00 USD | 11,870.00 USD | 8,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,890,000.00 USD | 3,890,000.00 USD | 250,310.00 USD | 53,000.00 USD | 24,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.03` | 152.32 USD | 5,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,660,000.00 USD | 2,660,000.00 USD | 14,070.00 USD | 13,840.00 USD | 15,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,080,000.00 USD | 4,080,000.00 USD | 134,200.00 USD | 33,660.00 USD | 19,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,780,000.00 USD | 2,780,000.00 USD | 69,800.00 USD | 11,810.00 USD | 32,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,190,000.00 USD | 4,190,000.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,810,000.00 USD | 2,810,000.00 USD | 12,270.00 USD | 2,160.00 USD | 17,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,420,000.00 USD | 4,420,000.00 USD | 217,210.00 USD | 8,290.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.03` | 221.28 USD | 6,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,840,000.00 USD | 2,840,000.00 USD | 11,120.00 USD | 15,190.00 USD | 7,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 1,430.00 USD | 4,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 4,720,000.00 USD | 4,720,000.00 USD | 262,550.00 USD | 3,170.00 USD | 43,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,120,000.00 USD | 5,120,000.00 USD | 179,470.00 USD | 1,450.00 USD | 215,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,510,000.00 USD | 5,510,000.00 USD | 288,650.00 USD | 9,430.00 USD | 93,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 182.19 USD | 6,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,840,000.00 USD | 5,840,000.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,100,000.00 USD | 6,100,000.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 6,510,000.00 USD | 6,510,000.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 367.04 USD | 6,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 6,910,000.00 USD | 6,910,000.00 USD | 195,180.00 USD | 28,070.00 USD | 167,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,060,000.00 USD | 7,060,000.00 USD | 87,270.00 USD | 29,070.00 USD | 41,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,400,000.00 USD | 7,400,000.00 USD | 140,530.00 USD | 49,780.00 USD | 143,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,560,000.00 USD | 7,560,000.00 USD | 87,130.00 USD | 44,290.00 USD | 36,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 7,920,000.00 USD | 7,920,000.00 USD | 185,840.00 USD | 48,000.00 USD | 121,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,280,000.00 USD | 8,280,000.00 USD | 205,290.00 USD | 63,350.00 USD | 94,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,700,000.00 USD | 8,700,000.00 USD | 217,790.00 USD | 73,000.00 USD | 125,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,960,000.00 USD | 8,960,000.00 USD | 115,520.00 USD | 81,560.00 USD | 61,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,050,000.00 USD | 9,050,000.00 USD | 63,260.00 USD | 25,320.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.2015` | 486,490.00 USD | 0.00 USD | 127.47 USD | `-78.63%` | `632.60` |
| `Live` | `Long` | `0.2135` | 486,360.00 USD | 0.00 USD | 106.75 USD | `-77.36%` | `500.00` |
| `Live` | `Long` | `0.3565` | 486,250.00 USD | 0.00 USD | 787.51 USD | `-62.19%` | `2,209.00` |
| `Live` | `Long` | `0.4195` | 485,470.00 USD | 0.00 USD | 5,190.00 USD | `-55.51%` | `12,374.00` |
| `Live` | `Long` | `0.4685` | 480,270.00 USD | 0.00 USD | 147.02 USD | `-50.31%` | `313.80` |
| `Live` | `Long` | `0.4705` | 480,130.00 USD | 0.00 USD | 2,590.00 USD | `-50.10%` | `5,500.00` |
| `Live` | `Long` | `0.4835` | 477,540.00 USD | 0.00 USD | 193.74 USD | `-48.72%` | `400.70` |
| `Live` | `Long` | `0.5065` | 477,350.00 USD | 0.00 USD | 3,290.00 USD | `-46.28%` | `6,504.70` |
| `Live` | `Long` | `0.5375` | 474,050.00 USD | 0.00 USD | 213.12 USD | `-42.99%` | `396.50` |
| `Live` | `Long` | `0.5505` | 473,840.00 USD | 0.00 USD | 550.50 USD | `-41.61%` | `1,000.00` |
| `Live` | `Long` | `0.5655` | 473,290.00 USD | 0.00 USD | 14,600.00 USD | `-40.02%` | `25,816.60` |
| `Live` | `Long` | `0.5695` | 458,690.00 USD | 0.00 USD | 577.36 USD | `-39.60%` | `1,013.80` |
| `Live` | `Long` | `0.5845` | 458,110.00 USD | 0.00 USD | 683.51 USD | `-38.01%` | `1,169.40` |
| `Live` | `Long` | `0.5895` | 457,430.00 USD | 0.00 USD | 137.53 USD | `-37.48%` | `233.30` |
| `Live` | `Long` | `0.6055` | 457,290.00 USD | 0.00 USD | 1,480.00 USD | `-35.78%` | `2,448.50` |
| `Live` | `Long` | `0.6075` | 455,810.00 USD | 0.00 USD | 1,810.00 USD | `-35.57%` | `2,971.80` |
| `Live` | `Long` | `0.6125` | 454,000.00 USD | 0.00 USD | 105.96 USD | `-35.04%` | `173.00` |
| `Live` | `Long` | `0.6145` | 453,900.00 USD | 0.00 USD | 147.48 USD | `-34.82%` | `240.00` |
| `Live` | `Long` | `0.6295` | 453,750.00 USD | 0.00 USD | 220.32 USD | `-33.23%` | `350.00` |
| `Live` | `Long` | `0.6315` | 453,530.00 USD | 0.00 USD | 757.80 USD | `-33.02%` | `1,200.00` |
| `Live` | `Long` | `0.6355` | 452,770.00 USD | 0.00 USD | 106.00 USD | `-32.60%` | `166.80` |
| `Live` | `Long` | `0.6365` | 452,660.00 USD | 0.00 USD | 507.86 USD | `-32.49%` | `797.90` |
| `Live` | `Long` | `0.6405` | 452,160.00 USD | 0.00 USD | 2,090.00 USD | `-32.07%` | `3,262.00` |
| `Live` | `Long` | `0.6425` | 450,070.00 USD | 0.00 USD | 20,300.00 USD | `-31.85%` | `31,595.60` |
| `Live` | `Long` | `0.6465` | 429,770.00 USD | 0.00 USD | 4,230.00 USD | `-31.43%` | `6,539.70` |
| `Live` | `Long` | `0.6475` | 425,540.00 USD | 0.00 USD | 202.47 USD | `-31.32%` | `312.70` |
| `Live` | `Long` | `0.6595` | 425,340.00 USD | 0.00 USD | 149.44 USD | `-30.05%` | `226.60` |
| `Live` | `Long` | `0.6725` | 425,190.00 USD | 0.00 USD | 63,890.00 USD | `-28.67%` | `95,000.00` |
| `Live` | `Long` | `0.6775` | 361,300.00 USD | 0.00 USD | 423.10 USD | `-28.14%` | `624.50` |
| `Live` | `Long` | `0.6835` | 360,880.00 USD | 0.00 USD | 512.97 USD | `-27.51%` | `750.50` |
| `Live` | `Long` | `0.6855` | 360,360.00 USD | 0.00 USD | 19,630.00 USD | `-27.29%` | `28,635.00` |
| `Live` | `Long` | `0.6965` | 340,730.00 USD | 0.00 USD | 322.62 USD | `-26.13%` | `463.20` |
| `Live` | `Long` | `0.7005` | 340,410.00 USD | 0.00 USD | 1,140.00 USD | `-25.70%` | `1,634.20` |
| `Live` | `Long` | `0.7065` | 339,270.00 USD | 0.00 USD | 157.83 USD | `-25.07%` | `223.40` |
| `Live` | `Long` | `0.7145` | 339,110.00 USD | 0.00 USD | 988.87 USD | `-24.22%` | `1,384.00` |
| `Live` | `Long` | `0.7225` | 338,120.00 USD | 0.00 USD | 1,580.00 USD | `-23.37%` | `2,190.90` |
| `Live` | `Long` | `0.7235` | 336,540.00 USD | 0.00 USD | 397.93 USD | `-23.26%` | `550.00` |
| `Live` | `Long` | `0.7245` | 336,140.00 USD | 0.00 USD | 108,670.00 USD | `-23.16%` | `150,000.00` |
| `Live` | `Long` | `0.7295` | 227,460.00 USD | 0.00 USD | 291.58 USD | `-22.63%` | `399.70` |
| `Live` | `Long` | `0.7305` | 227,170.00 USD | 0.00 USD | 2,300.00 USD | `-22.52%` | `3,143.00` |
| `Live` | `Long` | `0.7335` | 224,880.00 USD | 0.00 USD | 1,140.00 USD | `-22.20%` | `1,557.80` |
| `Live` | `Long` | `0.7395` | 223,730.00 USD | 0.00 USD | 283.30 USD | `-21.57%` | `383.10` |
| `Live` | `Long` | `0.7515` | 223,450.00 USD | 0.00 USD | 32,890.00 USD | `-20.29%` | `43,766.90` |
| `Live` | `Long` | `0.7525` | 190,560.00 USD | 0.00 USD | 910.22 USD | `-20.19%` | `1,209.60` |
| `Live` | `Long` | `0.7535` | 189,650.00 USD | 0.00 USD | 629.25 USD | `-20.08%` | `835.10` |
| `Live` | `Long` | `0.7555` | 189,020.00 USD | 0.00 USD | 144.07 USD | `-19.87%` | `190.70` |
| `Live` | `Long` | `0.7565` | 188,880.00 USD | 0.00 USD | 8,860.00 USD | `-19.76%` | `11,712.10` |
| `Live` | `Long` | `0.7635` | 180,020.00 USD | 0.00 USD | 308.00 USD | `-19.02%` | `403.40` |
| `Live` | `Long` | `0.7705` | 179,710.00 USD | 0.00 USD | 152.94 USD | `-18.28%` | `198.50` |
| `Live` | `Long` | `0.7725` | 179,560.00 USD | 0.00 USD | 3,840.00 USD | `-18.07%` | `4,968.90` |
| `Live` | `Long` | `0.7775` | 175,720.00 USD | 0.00 USD | 2,490.00 USD | `-17.54%` | `3,199.30` |
| `Live` | `Long` | `0.7855` | 173,230.00 USD | 0.00 USD | 55,770.00 USD | `-16.69%` | `71,003.30` |
| `Live` | `Long` | `0.7865` | 117,460.00 USD | 0.00 USD | 156.51 USD | `-16.58%` | `199.00` |
| `Live` | `Long` | `0.7905` | 117,300.00 USD | 0.00 USD | 277.39 USD | `-16.16%` | `350.90` |
| `Live` | `Long` | `0.7935` | 117,020.00 USD | 0.00 USD | 1,760.00 USD | `-15.84%` | `2,214.10` |
| `Live` | `Long` | `0.7985` | 115,270.00 USD | 0.00 USD | 210.40 USD | `-15.31%` | `263.50` |
| `Live` | `Long` | `0.8135` | 115,060.00 USD | 0.00 USD | 647.79 USD | `-13.72%` | `796.30` |
| `Live` | `Long` | `0.8215` | 114,410.00 USD | 0.00 USD | 1,950.00 USD | `-12.87%` | `2,370.70` |
| `Live` | `Long` | `0.8235` | 112,460.00 USD | 0.00 USD | 749.96 USD | `-12.66%` | `910.70` |
| `Live` | `Long` | `0.8345` | 111,710.00 USD | 0.00 USD | 626.21 USD | `-11.49%` | `750.40` |
| `Live` | `Long` | `0.8365` | 111,080.00 USD | 0.00 USD | 316.70 USD | `-11.28%` | `378.60` |
| `Live` | `Long` | `0.8415` | 110,770.00 USD | 0.00 USD | 1,570.00 USD | `-10.75%` | `1,862.40` |
| `Live` | `Long` | `0.8495` | 109,200.00 USD | 0.00 USD | 1,260.00 USD | `-9.90%` | `1,486.90` |
| `Live` | `Long` | `0.8575` | 107,940.00 USD | 0.00 USD | 620.32 USD | `-9.05%` | `723.40` |
| `Live` | `Long` | `0.8635` | 107,320.00 USD | 0.00 USD | 208.02 USD | `-8.42%` | `240.90` |
| `Live` | `Long` | `0.8645` | 107,110.00 USD | 0.00 USD | 438.30 USD | `-8.31%` | `507.00` |
| `Live` | `Long` | `0.8665` | 106,670.00 USD | 0.00 USD | 1,390.00 USD | `-8.10%` | `1,606.10` |
| `Live` | `Long` | `0.8695` | 105,280.00 USD | 0.00 USD | 12,590.00 USD | `-7.78%` | `14,478.80` |
| `Live` | `Long` | `0.8705` | 92,690.00 USD | 0.00 USD | 92,480.00 USD | `-7.67%` | `106,233.40` |
| `Live` | `Long` | `0.8865` | 212.67 USD | 0.00 USD | 212.67 USD | `-5.98%` | `239.90` |
| `Live` | `Short` | `0.9805` | 102.95 USD | 102.95 USD | 0.00 USD | `+3.99%` | `105.00` |
| `Live` | `Short` | `0.9875` | 314.57 USD | 211.62 USD | 0.00 USD | `+4.74%` | `214.30` |
| `Live` | `Short` | `0.9925` | 4,260.00 USD | 3,940.00 USD | 0.00 USD | `+5.27%` | `3,970.40` |
| `Live` | `Short` | `0.9935` | 4,470.00 USD | 212.91 USD | 0.00 USD | `+5.37%` | `214.30` |
| `Live` | `Short` | `0.9945` | 4,890.00 USD | 426.24 USD | 0.00 USD | `+5.48%` | `428.60` |
| `Live` | `Short` | `0.9985` | 5,750.00 USD | 852.22 USD | 0.00 USD | `+5.90%` | `853.50` |
| `Live` | `Short` | `1.02` | 6,510.00 USD | 760.04 USD | 0.00 USD | `+8.13%` | `745.50` |
| `Live` | `Short` | `1.02` | 6,730.00 USD | 218.91 USD | 0.00 USD | `+8.34%` | `214.30` |
| `Live` | `Short` | `1.03` | 6,950.00 USD | 220.19 USD | 0.00 USD | `+8.98%` | `214.30` |
| `Live` | `Short` | `1.03` | 7,100.00 USD | 152.32 USD | 0.00 USD | `+9.09%` | `148.10` |
| `Live` | `Short` | `1.03` | 7,320.00 USD | 221.28 USD | 0.00 USD | `+9.72%` | `213.90` |
| `Live` | `Short` | `1.04` | 7,650.00 USD | 333.46 USD | 0.00 USD | `+10.15%` | `321.10` |
| `Live` | `Short` | `1.04` | 7,880.00 USD | 223.41 USD | 0.00 USD | `+10.57%` | `214.30` |
| `Live` | `Short` | `1.05` | 8,240.00 USD | 367.04 USD | 0.00 USD | `+11.10%` | `350.40` |
| `Live` | `Short` | `1.07` | 8,470.00 USD | 229.41 USD | 0.00 USD | `+13.54%` | `214.30` |
| `Live` | `Short` | `1.08` | 10,710.00 USD | 2,230.00 USD | 0.00 USD | `+14.71%` | `2,064.20` |
| `Live` | `Short` | `1.11` | 10,880.00 USD | 170.02 USD | 0.00 USD | `+17.78%` | `153.10` |
| `Live` | `Short` | `1.11` | 13,320.00 USD | 2,440.00 USD | 0.00 USD | `+17.99%` | `2,194.20` |
| `Live` | `Short` | `1.12` | 13,560.00 USD | 240.98 USD | 0.00 USD | `+19.27%` | `214.30` |
| `Live` | `Short` | `1.14` | 27,920.00 USD | 14,370.00 USD | 0.00 USD | `+20.54%` | `12,639.80` |
| `Live` | `Short` | `1.31` | 28,050.00 USD | 126.85 USD | 0.00 USD | `+39.42%` | `96.50` |
| `Live` | `Short` | `1.32` | 39,780.00 USD | 11,730.00 USD | 0.00 USD | `+40.37%` | `8,862.90` |
| `Live` | `Short` | `1.34` | 40,020.00 USD | 239.77 USD | 0.00 USD | `+42.07%` | `179.00` |
| `Live` | `Short` | `1.37` | 43,890.00 USD | 3,870.00 USD | 0.00 USD | `+44.83%` | `2,834.10` |
| `Live` | `Short` | `1.42` | 47,080.00 USD | 3,200.00 USD | 0.00 USD | `+50.66%` | `2,249.30` |
| `Live` | `Short` | `1.43` | 47,610.00 USD | 530.97 USD | 0.00 USD | `+52.04%` | `370.40` |
| `Live` | `Short` | `1.52` | 47,740.00 USD | 121.12 USD | 0.00 USD | `+61.59%` | `79.50` |
| `Live` | `Short` | `1.54` | 47,910.00 USD | 176.42 USD | 0.00 USD | `+63.71%` | `114.30` |
| `Live` | `Short` | `1.56` | 49,720.00 USD | 1,810.00 USD | 0.00 USD | `+65.09%` | `1,161.90` |
| `Live` | `Short` | `1.57` | 50,500.00 USD | 782.81 USD | 0.00 USD | `+66.25%` | `499.40` |
| `Live` | `Short` | `1.58` | 129,200.00 USD | 78,700.00 USD | 0.00 USD | `+67.74%` | `49,759.80` |
| `Live` | `Short` | `1.63` | 131,640.00 USD | 2,440.00 USD | 0.00 USD | `+72.40%` | `1,500.00` |
| `Live` | `Short` | `1.65` | 139,870.00 USD | 8,240.00 USD | 0.00 USD | `+74.74%` | `5,000.00` |
| `Live` | `Short` | `1.67` | 140,120.00 USD | 243.81 USD | 0.00 USD | `+76.75%` | `146.30` |
| `Live` | `Short` | `1.67` | 140,420.00 USD | 300.33 USD | 0.00 USD | `+76.97%` | `180.00` |
| `Live` | `Short` | `1.69` | 140,740.00 USD | 324.22 USD | 0.00 USD | `+79.19%` | `191.90` |
| `Live` | `Short` | `1.73` | 140,930.00 USD | 190.42 USD | 0.00 USD | `+83.44%` | `110.10` |
| `Live` | `Short` | `1.74` | 154,080.00 USD | 13,140.00 USD | 0.00 USD | `+84.18%` | `7,569.10` |
| `Live` | `Short` | `1.77` | 154,460.00 USD | 380.81 USD | 0.00 USD | `+88.21%` | `214.60` |
| `Live` | `Short` | `1.86` | 154,670.00 USD | 208.37 USD | 0.00 USD | `+96.80%` | `112.30` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.4015` | 370,450.00 USD | 0.00 USD | 120.45 USD | `-57.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 370,330.00 USD | 0.00 USD | 150.15 USD | `-46.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5435` | 370,180.00 USD | 0.00 USD | 186.15 USD | `-42.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 370,000.00 USD | 0.00 USD | 1,150.00 USD | `-30.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 368,850.00 USD | 0.00 USD | 781.90 USD | `-25.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 368,070.00 USD | 0.00 USD | 477.38 USD | `-24.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 367,590.00 USD | 0.00 USD | 341.33 USD | `-23.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 367,250.00 USD | 0.00 USD | 972.82 USD | `-23.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 366,280.00 USD | 0.00 USD | 160.20 USD | `-22.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7385` | 366,120.00 USD | 0.00 USD | 102.58 USD | `-21.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 366,010.00 USD | 0.00 USD | 289.49 USD | `-20.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7615` | 365,720.00 USD | 0.00 USD | 197.53 USD | `-19.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 365,530.00 USD | 0.00 USD | 14,570.00 USD | `-17.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 350,960.00 USD | 0.00 USD | 213.58 USD | `-16.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 350,750.00 USD | 0.00 USD | 274,830.00 USD | `-15.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 75,910.00 USD | 0.00 USD | 108.47 USD | `-15.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8025` | 75,800.00 USD | 0.00 USD | 2,010.00 USD | `-14.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 73,790.00 USD | 0.00 USD | 326.96 USD | `-14.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 73,460.00 USD | 0.00 USD | 405.75 USD | `-13.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 73,060.00 USD | 0.00 USD | 772.84 USD | `-11.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8415` | 72,290.00 USD | 0.00 USD | 2,670.00 USD | `-10.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8495` | 69,610.00 USD | 0.00 USD | 3,470.00 USD | `-9.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 66,140.00 USD | 0.00 USD | 9,180.00 USD | `-9.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 56,960.00 USD | 0.00 USD | 341.94 USD | `-9.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 56,620.00 USD | 0.00 USD | 1,150.00 USD | `-9.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 55,470.00 USD | 0.00 USD | 429.25 USD | `-8.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 55,050.00 USD | 0.00 USD | 223.30 USD | `-8.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 54,820.00 USD | 0.00 USD | 518.51 USD | `-8.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 54,300.00 USD | 0.00 USD | 128.39 USD | `-7.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 54,180.00 USD | 0.00 USD | 1,280.00 USD | `-7.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 52,900.00 USD | 0.00 USD | 205.24 USD | `-7.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 52,690.00 USD | 0.00 USD | 649.66 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 52,040.00 USD | 0.00 USD | 194.06 USD | `-6.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8845` | 51,850.00 USD | 0.00 USD | 193.35 USD | `-6.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 51,650.00 USD | 0.00 USD | 223.04 USD | `-5.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 51,430.00 USD | 0.00 USD | 10,840.00 USD | `-5.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 40,590.00 USD | 0.00 USD | 4,920.00 USD | `-5.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8915` | 35,670.00 USD | 0.00 USD | 121.15 USD | `-5.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 35,550.00 USD | 0.00 USD | 192.07 USD | `-5.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 35,360.00 USD | 0.00 USD | 195.32 USD | `-5.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8955` | 35,160.00 USD | 0.00 USD | 575.72 USD | `-5.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8965` | 34,590.00 USD | 0.00 USD | 196.87 USD | `-4.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8975` | 34,390.00 USD | 0.00 USD | 191.98 USD | `-4.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8985` | 34,200.00 USD | 0.00 USD | 2,870.00 USD | `-4.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9005` | 31,320.00 USD | 0.00 USD | 385.95 USD | `-4.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9025` | 30,940.00 USD | 0.00 USD | 398.91 USD | `-4.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9035` | 30,540.00 USD | 0.00 USD | 196.96 USD | `-4.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9045` | 30,340.00 USD | 0.00 USD | 300.38 USD | `-4.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9065` | 30,040.00 USD | 0.00 USD | 198.61 USD | `-3.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9075` | 29,840.00 USD | 0.00 USD | 994.35 USD | `-3.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 28,850.00 USD | 0.00 USD | 363.40 USD | `-3.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9095` | 28,480.00 USD | 0.00 USD | 1,810.00 USD | `-3.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9115` | 26,680.00 USD | 0.00 USD | 397.23 USD | `-3.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9135` | 26,280.00 USD | 0.00 USD | 398.65 USD | `-3.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9145` | 25,880.00 USD | 0.00 USD | 399.09 USD | `-3.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9155` | 25,480.00 USD | 0.00 USD | 403.92 USD | `-2.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9165` | 25,080.00 USD | 0.00 USD | 198.06 USD | `-2.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9175` | 24,880.00 USD | 0.00 USD | 223.78 USD | `-2.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9185` | 24,660.00 USD | 0.00 USD | 899.85 USD | `-2.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9195` | 23,760.00 USD | 0.00 USD | 900.19 USD | `-2.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 22,860.00 USD | 0.00 USD | 2,920.00 USD | `-2.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9215` | 19,930.00 USD | 0.00 USD | 104.68 USD | `-2.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9225` | 19,830.00 USD | 0.00 USD | 201.94 USD | `-2.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9235` | 19,630.00 USD | 0.00 USD | 1,080.00 USD | `-2.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9245` | 18,540.00 USD | 0.00 USD | 201.45 USD | `-1.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9255` | 18,340.00 USD | 0.00 USD | 817.40 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9265` | 17,520.00 USD | 0.00 USD | 403.77 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9275` | 17,120.00 USD | 0.00 USD | 2,120.00 USD | `-1.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9285` | 15,000.00 USD | 0.00 USD | 397.96 USD | `-1.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9295` | 14,600.00 USD | 0.00 USD | 407.49 USD | `-1.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9305` | 14,200.00 USD | 0.00 USD | 203.97 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9315` | 13,990.00 USD | 0.00 USD | 263.80 USD | `-1.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9325` | 13,730.00 USD | 0.00 USD | 241.98 USD | `-1.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9335` | 13,490.00 USD | 0.00 USD | 814.76 USD | `-0.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9355` | 12,670.00 USD | 0.00 USD | 201.97 USD | `-0.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9365` | 12,470.00 USD | 0.00 USD | 9,680.00 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9395` | 2,790.00 USD | 0.00 USD | 416.01 USD | `-0.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9405` | 2,370.00 USD | 0.00 USD | 555.18 USD | `-0.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9415` | 1,810.00 USD | 0.00 USD | 997.80 USD | `-0.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9425` | 816.96 USD | 0.00 USD | 816.96 USD | `-0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 3,750.00 USD | 3,750.00 USD | 0.00 USD | `+0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 31,160.00 USD | 27,420.00 USD | 0.00 USD | `+0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 31,550.00 USD | 383.87 USD | 0.00 USD | `+0.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 31,690.00 USD | 140.18 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 60,620.00 USD | 28,930.00 USD | 0.00 USD | `+0.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 61,030.00 USD | 414.68 USD | 0.00 USD | `+0.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9525` | 61,410.00 USD | 381.00 USD | 0.00 USD | `+1.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 61,820.00 USD | 408.67 USD | 0.00 USD | `+1.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9545` | 62,230.00 USD | 408.72 USD | 0.00 USD | `+1.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 66,020.00 USD | 3,790.00 USD | 0.00 USD | `+1.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 66,430.00 USD | 409.96 USD | 0.00 USD | `+1.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 66,570.00 USD | 136.83 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 66,830.00 USD | 261.16 USD | 0.00 USD | `+1.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9615` | 67,240.00 USD | 412.10 USD | 0.00 USD | `+1.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 69,150.00 USD | 1,910.00 USD | 0.00 USD | `+2.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 69,720.00 USD | 568.75 USD | 0.00 USD | `+2.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 70,080.00 USD | 364.58 USD | 0.00 USD | `+2.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 70,290.00 USD | 206.91 USD | 0.00 USD | `+2.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 71,110.00 USD | 824.91 USD | 0.00 USD | `+2.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 71,320.00 USD | 206.95 USD | 0.00 USD | `+2.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 73,350.00 USD | 2,030.00 USD | 0.00 USD | `+2.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 74,910.00 USD | 1,560.00 USD | 0.00 USD | `+2.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 75,300.00 USD | 387.83 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 76,130.00 USD | 830.10 USD | 0.00 USD | `+3.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 76,520.00 USD | 396.17 USD | 0.00 USD | `+3.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 77,200.00 USD | 676.53 USD | 0.00 USD | `+3.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 77,300.00 USD | 102.95 USD | 0.00 USD | `+3.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 79,330.00 USD | 2,030.00 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 79,680.00 USD | 346.13 USD | 0.00 USD | `+4.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 79,930.00 USD | 255.38 USD | 0.00 USD | `+4.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 80,160.00 USD | 223.91 USD | 0.00 USD | `+4.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9865` | 80,270.00 USD | 109.99 USD | 0.00 USD | `+4.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 83,790.00 USD | 3,520.00 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 115,540.00 USD | 31,750.00 USD | 0.00 USD | `+5.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 115,940.00 USD | 403.06 USD | 0.00 USD | `+5.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 121,090.00 USD | 5,140.00 USD | 0.00 USD | `+5.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 158,390.00 USD | 37,310.00 USD | 0.00 USD | `+5.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 158,890.00 USD | 500.25 USD | 0.00 USD | `+6.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 199,490.00 USD | 40,590.00 USD | 0.00 USD | `+6.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 199,720.00 USD | 235.79 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 201,070.00 USD | 1,340.00 USD | 0.00 USD | `+6.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 201,300.00 USD | 230.39 USD | 0.00 USD | `+6.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 201,430.00 USD | 127.65 USD | 0.00 USD | `+6.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 201,600.00 USD | 176.59 USD | 0.00 USD | `+6.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 202,010.00 USD | 409.86 USD | 0.00 USD | `+7.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 202,120.00 USD | 110.95 USD | 0.00 USD | `+7.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 202,740.00 USD | 615.60 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 203,300.00 USD | 561.17 USD | 0.00 USD | `+7.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 203,510.00 USD | 214.40 USD | 0.00 USD | `+8.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 203,760.00 USD | 249.88 USD | 0.00 USD | `+8.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 203,970.00 USD | 207.97 USD | 0.00 USD | `+8.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 204,180.00 USD | 208.26 USD | 0.00 USD | `+9.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 204,700.00 USD | 516.75 USD | 0.00 USD | `+9.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 205,050.00 USD | 348.86 USD | 0.00 USD | `+9.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 205,440.00 USD | 391.80 USD | 0.00 USD | `+9.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 205,850.00 USD | 413.76 USD | 0.00 USD | `+10.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 206,210.00 USD | 354.91 USD | 0.00 USD | `+10.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 208,110.00 USD | 1,900.00 USD | 0.00 USD | `+10.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 208,320.00 USD | 207.87 USD | 0.00 USD | `+10.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 208,530.00 USD | 207.97 USD | 0.00 USD | `+10.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 208,630.00 USD | 107.99 USD | 0.00 USD | `+11.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 283,470.00 USD | 74,840.00 USD | 0.00 USD | `+12.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 285,640.00 USD | 2,170.00 USD | 0.00 USD | `+15.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 287,180.00 USD | 1,540.00 USD | 0.00 USD | `+15.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 297,100.00 USD | 9,930.00 USD | 0.00 USD | `+16.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 297,980.00 USD | 877.63 USD | 0.00 USD | `+17.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 298,150.00 USD | 171.09 USD | 0.00 USD | `+18.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 300,920.00 USD | 2,770.00 USD | 0.00 USD | `+19.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 302,960.00 USD | 2,040.00 USD | 0.00 USD | `+19.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 303,130.00 USD | 172.17 USD | 0.00 USD | `+19.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 303,310.00 USD | 172.32 USD | 0.00 USD | `+19.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 303,490.00 USD | 187.72 USD | 0.00 USD | `+19.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 303,680.00 USD | 188.39 USD | 0.00 USD | `+20.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 306,350.00 USD | 2,670.00 USD | 0.00 USD | `+20.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 306,520.00 USD | 174.23 USD | 0.00 USD | `+20.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 306,700.00 USD | 174.38 USD | 0.00 USD | `+20.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 306,870.00 USD | 174.84 USD | 0.00 USD | `+20.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 307,020.00 USD | 150.90 USD | 0.00 USD | `+21.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 307,170.00 USD | 151.03 USD | 0.00 USD | `+21.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 307,330.00 USD | 151.16 USD | 0.00 USD | `+21.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 309,370.00 USD | 2,050.00 USD | 0.00 USD | `+23.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 309,480.00 USD | 110.00 USD | 0.00 USD | `+24.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 309,960.00 USD | 475.80 USD | 0.00 USD | `+26.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 311,170.00 USD | 1,210.00 USD | 0.00 USD | `+27.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 354,090.00 USD | 42,930.00 USD | 0.00 USD | `+27.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 356,100.00 USD | 2,000.00 USD | 0.00 USD | `+30.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 357,480.00 USD | 1,380.00 USD | 0.00 USD | `+32.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 357,730.00 USD | 245.41 USD | 0.00 USD | `+35.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 366,120.00 USD | 8,390.00 USD | 0.00 USD | `+36.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 366,540.00 USD | 415.25 USD | 0.00 USD | `+37.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 373,050.00 USD | 6,520.00 USD | 0.00 USD | `+38.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 377,850.00 USD | 4,800.00 USD | 0.00 USD | `+38.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 378,510.00 USD | 655.75 USD | 0.00 USD | `+39.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 379,100.00 USD | 596.43 USD | 0.00 USD | `+41.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 380,920.00 USD | 1,810.00 USD | 0.00 USD | `+42.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 394,800.00 USD | 13,880.00 USD | 0.00 USD | `+42.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 396,050.00 USD | 1,250.00 USD | 0.00 USD | `+43.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 398,120.00 USD | 2,070.00 USD | 0.00 USD | `+47.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 398,260.00 USD | 140.05 USD | 0.00 USD | `+48.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 398,420.00 USD | 160.42 USD | 0.00 USD | `+48.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 399,380.00 USD | 954.32 USD | 0.00 USD | `+49.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 433,550.00 USD | 34,170.00 USD | 0.00 USD | `+52.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 434,430.00 USD | 879.84 USD | 0.00 USD | `+58.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 437,480.00 USD | 3,050.00 USD | 0.00 USD | `+60.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 437,780.00 USD | 297.27 USD | 0.00 USD | `+64.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 446,310.00 USD | 8,530.00 USD | 0.00 USD | `+75.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 446,450.00 USD | 143.99 USD | 0.00 USD | `+76.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 446,630.00 USD | 177.05 USD | 0.00 USD | `+87.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 447,060.00 USD | 431.40 USD | 0.00 USD | `+90.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 447,280.00 USD | 220.77 USD | 0.00 USD | `+92.87%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.8000` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 21,120.00 USD | 8,540.00 USD | 16,770.00 USD |
| `7D` | `0.8020` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 8,990.00 USD | 4,460.00 USD | 9,540.00 USD |
| `7D` | `0.8040` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 5,500.00 USD | 2,170.00 USD | 940.33 USD |
| `7D` | `0.8060` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 16,390.00 USD | 10,990.00 USD | 10,100.00 USD |
| `7D` | `0.8080` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 1,570.00 USD | 1,230.00 USD | 10,210.00 USD |
| `7D` | `0.8100` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 2,890.00 USD | 2,010.00 USD | 4,690.00 USD |
| `7D` | `0.8120` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 15,720.00 USD | 3,030.00 USD | 9,400.00 USD |
| `7D` | `0.8140` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 32,880.00 USD | 6,050.00 USD | 15,910.00 USD |
| `7D` | `0.8160` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 38,200.00 USD | 10,180.00 USD | 6,010.00 USD |
| `7D` | `0.8180` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 12,550.00 USD | 2,560.00 USD | 11,440.00 USD |
| `7D` | `0.8200` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 1,740.00 USD | 1,570.00 USD | 7,460.00 USD |
| `7D` | `0.8220` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 20,390.00 USD | 6,820.00 USD | 4,490.00 USD |
| `7D` | `0.8240` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 23,160.00 USD | 93.73 USD | 11,990.00 USD |
| `7D` | `0.8260` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 5,220.00 USD | 3,490.00 USD | 1,560.00 USD |
| `7D` | `0.8280` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 0.00 USD | 3,910.00 USD | 1,040.00 USD |
| `7D` | `0.8300` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 9,280.00 USD | 4,780.00 USD | 2,450.00 USD |
| `7D` | `0.8320` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 0.00 USD | 401.80 USD | 77.95 USD |
| `7D` | `0.8340` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 35,710.00 USD | 10,960.00 USD | 1,980.00 USD |
| `7D` | `0.8360` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 0.00 USD | 844.23 USD | 311.26 USD |
| `1D` | `0.8370` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 18,140.00 USD | 2,530.00 USD | 20,310.00 USD |
| `7D` | `0.8380` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 15,240.00 USD | 633.60 USD | 539.92 USD |
| `1D` | `0.8390` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 1,740.00 USD | 745.84 USD | 2,010.00 USD |
| `7D` | `0.8400` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 0.00 USD | 798.38 USD | 8,060.00 USD |
| `1D` | `0.8410` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 1,470.00 USD | 2,040.00 USD | 1,780.00 USD |
| `7D` | `0.8420` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 6,400.00 USD | 7,120.00 USD | 4,060.00 USD |
| `1D` | `0.8430` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 4,670.00 USD | 6,880.00 USD | 1,150.00 USD |
| `7D` | `0.8440` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 7,170.00 USD | 24.80 USD | 0.00 USD |
| `1D` | `0.8450` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 2,360.00 USD | 8,430.00 USD | 1,150.00 USD |
| `7D` | `0.8460` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 2,560.00 USD | 427.62 USD | 2,660.00 USD |
| `1D` | `0.8470` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 24,200.00 USD | 1,110.00 USD | 165.77 USD |
| `7D` | `0.8480` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 26,310.00 USD | 10,990.00 USD | 202.79 USD |
| `1D` | `0.8490` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 6,900.00 USD | 5,020.00 USD | 7,940.00 USD |
| `7D` | `0.8500` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 3,110.00 USD | 638.56 USD | 21,250.00 USD |
| `1D` | `0.8510` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 13,560.00 USD | 4,140.00 USD | 16,720.00 USD |
| `7D` | `0.8520` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 14,700.00 USD | 669.43 USD | 226.67 USD |
| `1D` | `0.8530` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 4,680.00 USD | 3,830.00 USD | 5,510.00 USD |
| `7D` | `0.8540` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 254.55 USD | 2,660.00 USD | 5,540.00 USD |
| `1D` | `0.8550` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 18,270.00 USD | 3,040.00 USD | 5,090.00 USD |
| `7D` | `0.8560` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 0.00 USD | 842.92 USD | 2,180.00 USD |
| `1D` | `0.8570` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 989.11 USD | 1,720.00 USD | 6,150.00 USD |
| `7D` | `0.8580` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 3,540.00 USD | 101.30 USD | 7,540.00 USD |
| `1D` | `0.8590` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 6,870.00 USD | 10,640.00 USD | 6,420.00 USD |
| `7D` | `0.8600` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 6,780.00 USD | 211.77 USD | 10,030.00 USD |
| `1D` | `0.8610` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 8,320.00 USD | 855.53 USD | 16,460.00 USD |
| `7D` | `0.8620` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 7,670.00 USD | 6,050.00 USD | 26,880.00 USD |
| `1D` | `0.8630` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 39,330.00 USD | 12,290.00 USD | 2,010.00 USD |
| `7D` | `0.8640` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 4,820.00 USD | 321.30 USD | 0.00 USD |
| `1D` | `0.8650` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 17,640.00 USD | 2,110.00 USD | 1,790.00 USD |
| `7D` | `0.8660` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 45,020.00 USD | 19,050.00 USD | 2,170.00 USD |
| `1D` | `0.8670` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 12,000.00 USD | 10,090.00 USD | 1,110.00 USD |
| `7D` | `0.8680` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 92,530.00 USD | 14,760.00 USD | 50,800.00 USD |
| `1D` | `0.8690` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 42,010.00 USD | 3,780.00 USD | 29,400.00 USD |
| `7D` | `0.8700` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 81,840.00 USD | 9,460.00 USD | 7,550.00 USD |
| `1D` | `0.8710` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 42,290.00 USD | 24,900.00 USD | 28,630.00 USD |
| `7D` | `0.8720` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 5,420.00 USD | 18,020.00 USD | 11,450.00 USD |
| `1D` | `0.8730` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 54,500.00 USD | 21,510.00 USD | 25,960.00 USD |
| `7D` | `0.8740` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 0.00 USD | 12,360.00 USD | 3,200.00 USD |
| `1D` | `0.8750` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 36,800.00 USD | 6,900.00 USD | 17,890.00 USD |
| `7D` | `0.8760` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 766.43 USD | 0.00 USD | 5,750.00 USD |
| `1D` | `0.8770` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 10,690.00 USD | 152.79 USD | 0.00 USD |
| `7D` | `0.8780` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 1,500.00 USD | 0.00 USD | 33,650.00 USD |
| `1D` | `0.8790` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 0.00 USD | 40.93 USD | 50,910.00 USD |
| `7D` | `0.8800` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 1,600.00 USD | 5,820.00 USD | 51,030.00 USD |
| `1D` | `0.8810` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 13,820.00 USD | 5,210.00 USD | 2,430.00 USD |
| `7D` | `0.8820` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 454.20 USD | 9,500.00 USD | 0.00 USD |
| `1D` | `0.8830` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 656.20 USD | 5,570.00 USD | 0.00 USD |
| `7D` | `0.8840` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 2,090.00 USD | 6,440.00 USD | 15,690.00 USD |
| `1D` | `0.8850` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 5,680.00 USD | 34,880.00 USD | 11,180.00 USD |
| `7D` | `0.8860` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 141,730.00 USD | 22,320.00 USD | 78,280.00 USD |
| `1D` | `0.8870` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 68,710.00 USD | 16,710.00 USD | 32,750.00 USD |
| `7D` | `0.8880` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 130,140.00 USD | 31,410.00 USD | 9,920.00 USD |
| `1D` | `0.8890` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 69,610.00 USD | 40,830.00 USD | 4,860.00 USD |
| `7D` | `0.8900` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 108,250.00 USD | 45,590.00 USD | 30,420.00 USD |
| `1D` | `0.8910` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 2,410.00 USD | 38,730.00 USD | 20,080.00 USD |
| `7D` | `0.8920` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 46,210.00 USD | 38,810.00 USD | 14,520.00 USD |
| `1D` | `0.8930` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 57,080.00 USD | 23,480.00 USD | 37,920.00 USD |
| `7D` | `0.8940` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 45,210.00 USD | 12,120.00 USD | 26,470.00 USD |
| `1D` | `0.8950` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 6,700.00 USD | 15,420.00 USD | 8,160.00 USD |
| `7D` | `0.8960` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 2,140.00 USD | 32,820.00 USD | 93,280.00 USD |
| `1D` | `0.8970` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 8,300.00 USD | 27,310.00 USD | 19,060.00 USD |
| `7D` | `0.8980` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 0.00 USD | 24,060.00 USD | 0.00 USD |
| `1D` | `0.8990` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 3,650.00 USD | 24,130.00 USD | 4,220.00 USD |
| `7D` | `0.9000` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 0.00 USD | 25,040.00 USD | 0.00 USD |
| `1D` | `0.9010` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 5,490.00 USD | 28,480.00 USD | 7,410.00 USD |
| `7D` | `0.9020` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 0.00 USD | 48,090.00 USD | 23,430.00 USD |
| `1D` | `0.9030` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 10,610.00 USD | 17,560.00 USD | 18,230.00 USD |
| `7D` | `0.9040` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 0.00 USD | 12,290.00 USD | 506.97 USD |
| `1D` | `0.9050` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 23,790.00 USD | 18,920.00 USD | 22,050.00 USD |
| `7D` | `0.9060` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 1,910.00 USD | 3,840.00 USD | 42,040.00 USD |
| `1D` | `0.9070` | 968,800.00 USD | 0.00 USD | 968,800.00 USD | 36,650.00 USD | 8,370.00 USD | 33,510.00 USD |
| `7D` | `0.9080` | 967,910.00 USD | 0.00 USD | 967,910.00 USD | 22,010.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9090` | 890,270.00 USD | 0.00 USD | 890,270.00 USD | 7,100.00 USD | 9,080.00 USD | 239.84 USD |
| `1D` | `0.9110` | 873,850.00 USD | 0.00 USD | 873,850.00 USD | 25,560.00 USD | 2,850.00 USD | 2,080.00 USD |
| `1D` | `0.9130` | 843,360.00 USD | 0.00 USD | 843,360.00 USD | 17,080.00 USD | 9,480.00 USD | 22,310.00 USD |
| `7D` | `0.9140` | 945,900.00 USD | 0.00 USD | 945,900.00 USD | 0.00 USD | 515.41 USD | 36,850.00 USD |
| `1D` | `0.9150` | 794,480.00 USD | 0.00 USD | 794,480.00 USD | 11,120.00 USD | 17,780.00 USD | 24,660.00 USD |
| `7D` | `0.9160` | 908,540.00 USD | 0.00 USD | 908,540.00 USD | 0.00 USD | 12,370.00 USD | 9,800.00 USD |
| `1D` | `0.9170` | 740,930.00 USD | 0.00 USD | 740,930.00 USD | 7,300.00 USD | 16,660.00 USD | 15,090.00 USD |
| `7D` | `0.9180` | 886,360.00 USD | 0.00 USD | 886,360.00 USD | 0.00 USD | 0.00 USD | 23,380.00 USD |
| `1D` | `0.9190` | 701,880.00 USD | 0.00 USD | 701,880.00 USD | 9,900.00 USD | 15,280.00 USD | 16,980.00 USD |
| `7D` | `0.9200` | 862,980.00 USD | 0.00 USD | 862,980.00 USD | 0.00 USD | 4,870.00 USD | 3,970.00 USD |
| `1D` | `0.9210` | 659,720.00 USD | 0.00 USD | 659,720.00 USD | 12,850.00 USD | 3,680.00 USD | 6,020.00 USD |
| `7D` | `0.9220` | 854,140.00 USD | 0.00 USD | 854,140.00 USD | 152,480.00 USD | 7,760.00 USD | 1,010.00 USD |
| `1D` | `0.9230` | 637,160.00 USD | 0.00 USD | 637,160.00 USD | 9,860.00 USD | 10,950.00 USD | 21,700.00 USD |
| `7D` | `0.9240` | 692,890.00 USD | 0.00 USD | 692,890.00 USD | 141,890.00 USD | 20,480.00 USD | 25,670.00 USD |
| `1D` | `0.9250` | 594,650.00 USD | 0.00 USD | 594,650.00 USD | 108,890.00 USD | 74,100.00 USD | 62,530.00 USD |
| `7D` | `0.9260` | 504,860.00 USD | 0.00 USD | 504,860.00 USD | 44,020.00 USD | 32,300.00 USD | 84,070.00 USD |
| `1D` | `0.9270` | 349,140.00 USD | 0.00 USD | 349,140.00 USD | 39,920.00 USD | 7,040.00 USD | 73,810.00 USD |
| `7D` | `0.9280` | 344,470.00 USD | 0.00 USD | 344,470.00 USD | 0.00 USD | 24,550.00 USD | 1,600.00 USD |
| `1D` | `0.9290` | 228,370.00 USD | 0.00 USD | 228,370.00 USD | 80,950.00 USD | 20,440.00 USD | 38,560.00 USD |
| `1D` | `0.9310` | 88,410.00 USD | 0.00 USD | 88,410.00 USD | 0.00 USD | 7,130.00 USD | 5,410.00 USD |
| `7D` | `0.9320` | 318,320.00 USD | 0.00 USD | 318,320.00 USD | 37,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9330` | 75,880.00 USD | 0.00 USD | 75,880.00 USD | 3,720.00 USD | 6,140.00 USD | 26,590.00 USD |
| `7D` | `0.9340` | 280,870.00 USD | 0.00 USD | 280,870.00 USD | 0.00 USD | 0.00 USD | 31,370.00 USD |
| `1D` | `0.9350` | 39,420.00 USD | 0.00 USD | 39,420.00 USD | 36,510.00 USD | 221.86 USD | 0.00 USD |
| `7D` | `0.9360` | 249,500.00 USD | 0.00 USD | 249,500.00 USD | 8,250.00 USD | 0.00 USD | 68,130.00 USD |
| `1D` | `0.9370` | 2,690.00 USD | 0.00 USD | 2,690.00 USD | 0.00 USD | 182.01 USD | 852.35 USD |
| `7D` | `0.9380` | 173,120.00 USD | 0.00 USD | 173,120.00 USD | 42,660.00 USD | 19,540.00 USD | 27,700.00 USD |
| `1D` | `0.9390` | 1,650.00 USD | 0.00 USD | 1,650.00 USD | 1,340.00 USD | 309.30 USD | 0.00 USD |
| `7D` | `0.9400` | 83,230.00 USD | 0.00 USD | 83,230.00 USD | 75,540.00 USD | 474.96 USD | 7,220.00 USD |
| `1D` | `0.9410` | 912.94 USD | 912.94 USD | 0.00 USD | 673.54 USD | 239.40 USD | 0.00 USD |
| `1D` | `0.9410` | 1,830.00 USD | 1,830.00 USD | 0.00 USD | 673.54 USD | 239.40 USD | 0.00 USD |
| `7D` | `0.9410` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9420` | 91,710.00 USD | 91,710.00 USD | 0.00 USD | 91,060.00 USD | 650.60 USD | 0.00 USD |
| `1D` | `0.9430` | 3,280.00 USD | 3,280.00 USD | 0.00 USD | 1,230.00 USD | 224.96 USD | 0.00 USD |
| `7D` | `0.9440` | 92,420.00 USD | 92,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 713.33 USD |
| `7D` | `0.9460` | 170,070.00 USD | 170,070.00 USD | 0.00 USD | 0.00 USD | 27,270.00 USD | 50,380.00 USD |
| `1D` | `0.9470` | 3,800.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD | 199.60 USD | 319.22 USD |
| `7D` | `0.9480` | 278,710.00 USD | 278,710.00 USD | 0.00 USD | 3,540.00 USD | 10,340.00 USD | 94,750.00 USD |
| `1D` | `0.9490` | 84,330.00 USD | 84,330.00 USD | 0.00 USD | 80,530.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9500` | 392,770.00 USD | 392,770.00 USD | 0.00 USD | 85,700.00 USD | 18,830.00 USD | 9,530.00 USD |
| `1D` | `0.9510` | 95,320.00 USD | 95,320.00 USD | 0.00 USD | 5,190.00 USD | 813.18 USD | 4,990.00 USD |
| `7D` | `0.9520` | 578,690.00 USD | 578,690.00 USD | 0.00 USD | 175,720.00 USD | 9,750.00 USD | 447.96 USD |
| `1D` | `0.9530` | 116,950.00 USD | 116,950.00 USD | 0.00 USD | 7,370.00 USD | 8,490.00 USD | 5,770.00 USD |
| `7D` | `0.9540` | 600,520.00 USD | 600,520.00 USD | 0.00 USD | 0.00 USD | 21,830.00 USD | 0.00 USD |
| `1D` | `0.9550` | 189,940.00 USD | 189,940.00 USD | 0.00 USD | 25,300.00 USD | 39,260.00 USD | 8,440.00 USD |
| `7D` | `0.9560` | 628,620.00 USD | 628,620.00 USD | 0.00 USD | 0.00 USD | 28,100.00 USD | 0.00 USD |
| `1D` | `0.9570` | 226,530.00 USD | 226,530.00 USD | 0.00 USD | 13,680.00 USD | 13,280.00 USD | 9,630.00 USD |
| `7D` | `0.9580` | 644,440.00 USD | 644,440.00 USD | 0.00 USD | 3,880.00 USD | 10,980.00 USD | 957.94 USD |
| `1D` | `0.9590` | 248,210.00 USD | 248,210.00 USD | 0.00 USD | 14,060.00 USD | 3,680.00 USD | 3,930.00 USD |
| `7D` | `0.9600` | 676,430.00 USD | 676,430.00 USD | 0.00 USD | 17,690.00 USD | 12,420.00 USD | 1,880.00 USD |
| `1D` | `0.9610` | 312,540.00 USD | 312,540.00 USD | 0.00 USD | 18,020.00 USD | 15,760.00 USD | 30,550.00 USD |
| `7D` | `0.9620` | 718,740.00 USD | 718,740.00 USD | 0.00 USD | 17,990.00 USD | 24,320.00 USD | 0.00 USD |
| `1D` | `0.9630` | 510,550.00 USD | 510,550.00 USD | 0.00 USD | 110,950.00 USD | 41,450.00 USD | 45,610.00 USD |
| `7D` | `0.9640` | 961,740.00 USD | 961,740.00 USD | 0.00 USD | 139,390.00 USD | 7,500.00 USD | 96,110.00 USD |
| `1D` | `0.9650` | 651,940.00 USD | 651,940.00 USD | 0.00 USD | 29,080.00 USD | 33,020.00 USD | 79,280.00 USD |
| `7D` | `0.9660` | 972,730.00 USD | 972,730.00 USD | 0.00 USD | 5,050.00 USD | 5,170.00 USD | 778.15 USD |
| `1D` | `0.9670` | 748,360.00 USD | 748,360.00 USD | 0.00 USD | 53,970.00 USD | 16,730.00 USD | 25,720.00 USD |
| `7D` | `0.9680` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 38,090.00 USD | 5,870.00 USD | 0.00 USD |
| `1D` | `0.9690` | 789,690.00 USD | 789,690.00 USD | 0.00 USD | 14,860.00 USD | 14,610.00 USD | 11,850.00 USD |
| `7D` | `0.9700` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 30,140.00 USD | 30,730.00 USD |
| `1D` | `0.9710` | 902,890.00 USD | 902,890.00 USD | 0.00 USD | 15,040.00 USD | 19,120.00 USD | 79,040.00 USD |
| `7D` | `0.9720` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 1,430.00 USD | 10,140.00 USD | 31,370.00 USD |
| `1D` | `0.9730` | 995,970.00 USD | 995,970.00 USD | 0.00 USD | 37,900.00 USD | 14,900.00 USD | 40,280.00 USD |
| `7D` | `0.9740` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 1,480.00 USD | 25,640.00 USD | 76,600.00 USD |
| `1D` | `0.9750` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 29,660.00 USD | 13,550.00 USD | 34,760.00 USD |
| `7D` | `0.9760` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 51,990.00 USD | 19,300.00 USD | 9,280.00 USD |
| `1D` | `0.9770` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 78,910.00 USD | 16,960.00 USD | 13,160.00 USD |
| `7D` | `0.9780` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD | 24,280.00 USD |
| `1D` | `0.9790` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 38,220.00 USD | 11,310.00 USD | 26,320.00 USD |
| `7D` | `0.9800` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 152,980.00 USD |
| `1D` | `0.9810` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 21,440.00 USD | 13,940.00 USD | 28,550.00 USD |
| `7D` | `0.9820` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 53,310.00 USD | 19,830.00 USD | 146,200.00 USD |
| `1D` | `0.9830` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 33,340.00 USD | 27,220.00 USD | 55,550.00 USD |
| `7D` | `0.9840` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 71,940.00 USD | 211.77 USD | 22,300.00 USD |
| `1D` | `0.9850` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 46,950.00 USD | 8,800.00 USD | 18,830.00 USD |
| `7D` | `0.9860` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,390.00 USD |
| `1D` | `0.9870` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 14,930.00 USD | 6,470.00 USD | 22,410.00 USD |
| `7D` | `0.9880` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 67,460.00 USD |
| `1D` | `0.9890` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 27,890.00 USD | 3,780.00 USD | 30,190.00 USD |
| `7D` | `0.9900` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 22,660.00 USD | 321.20 USD | 16,590.00 USD |
| `1D` | `0.9910` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 60,130.00 USD | 5,890.00 USD | 45,430.00 USD |
| `7D` | `0.9920` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 1,570.00 USD | 479.24 USD | 31,040.00 USD |
| `1D` | `0.9930` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 16,320.00 USD | 5,130.00 USD | 8,200.00 USD |
| `7D` | `0.9940` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 29,270.00 USD | 0.00 USD | 39,460.00 USD |
| `1D` | `0.9950` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 29,250.00 USD | 2,120.00 USD | 7,140.00 USD |
| `7D` | `0.9960` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 75,810.00 USD | 5,380.00 USD | 43,230.00 USD |
| `1D` | `0.9970` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 46,950.00 USD | 1,870.00 USD | 13,030.00 USD |
| `7D` | `0.9980` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 53,110.00 USD | 6,740.00 USD | 4,210.00 USD |
| `1D` | `0.9990` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 35,340.00 USD | 17,910.00 USD | 10,720.00 USD |
| `7D` | `1.00` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 462.12 USD |
| `1D` | `1.00` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 44,780.00 USD | 10,790.00 USD | 13,500.00 USD |
| `7D` | `1.00` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 56,560.00 USD | 21,850.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 12,580.00 USD | 9,310.00 USD | 6,140.00 USD |
| `7D` | `1.00` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 70,950.00 USD | 3,970.00 USD | 1,470.00 USD |
| `1D` | `1.00` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 54,780.00 USD | 5,520.00 USD | 5,820.00 USD |
| `7D` | `1.01` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 48,310.00 USD | 240.78 USD | 11,560.00 USD |
| `1D` | `1.01` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 50,600.00 USD | 11,770.00 USD | 38,280.00 USD |
| `7D` | `1.01` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44,430.00 USD |
| `1D` | `1.01` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 30,870.00 USD | 13,790.00 USD | 7,610.00 USD |
| `7D` | `1.01` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 10,260.00 USD | 14,180.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 9,660.00 USD | 17,670.00 USD | 265.91 USD |
| `7D` | `1.01` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 33,230.00 USD | 30,100.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 10,450.00 USD | 1,540.00 USD | 3,750.00 USD |
| `7D` | `1.01` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 2,870.00 USD | 28,450.00 USD | 735.11 USD |
| `1D` | `1.01` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 14,310.00 USD | 18,100.00 USD | 14,630.00 USD |
| `7D` | `1.02` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 526.60 USD | 28,470.00 USD | 11,910.00 USD |
| `1D` | `1.02` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 3,990.00 USD | 2,940.00 USD | 12,700.00 USD |
| `7D` | `1.02` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 1,430.00 USD | 25,010.00 USD | 21,560.00 USD |
| `1D` | `1.02` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 55,630.00 USD | 4,860.00 USD | 10,650.00 USD |
| `7D` | `1.02` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 33,820.00 USD | 84,220.00 USD | 44,250.00 USD |
| `1D` | `1.02` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 6,670.00 USD | 7,410.00 USD | 21,020.00 USD |
| `7D` | `1.02` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 56,930.00 USD | 52,610.00 USD | 112,030.00 USD |
| `1D` | `1.02` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 44,890.00 USD | 18,460.00 USD | 29,940.00 USD |
| `7D` | `1.02` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 78,220.00 USD | 56,700.00 USD | 86,740.00 USD |
| `1D` | `1.02` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 39,730.00 USD | 6,940.00 USD | 17,080.00 USD |
| `7D` | `1.03` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 22,650.00 USD | 124,880.00 USD | 33,130.00 USD |
| `1D` | `1.03` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 15,190.00 USD | 11,870.00 USD | 8,090.00 USD |
| `7D` | `1.03` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 250,310.00 USD | 53,000.00 USD | 24,480.00 USD |
| `1D` | `1.03` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 14,070.00 USD | 13,840.00 USD | 15,760.00 USD |
| `7D` | `1.03` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 134,200.00 USD | 33,660.00 USD | 19,120.00 USD |
| `1D` | `1.03` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 69,800.00 USD | 8,920.00 USD | 32,850.00 USD |
| `7D` | `1.03` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD |
| `1D` | `1.03` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 12,270.00 USD | 2,160.00 USD | 17,290.00 USD |
| `7D` | `1.03` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 217,210.00 USD | 8,290.00 USD | 4,310.00 USD |
| `1D` | `1.03` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 11,210.00 USD | 15,190.00 USD | 7,250.00 USD |
| `7D` | `1.04` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 262,550.00 USD | 3,170.00 USD | 43,130.00 USD |
| `1D` | `1.04` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 44,200.00 USD | 6,390.00 USD | 11,940.00 USD |
| `7D` | `1.04` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 179,470.00 USD | 1,450.00 USD | 215,900.00 USD |
| `1D` | `1.04` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 7,640.00 USD | 5,430.00 USD | 5,210.00 USD |
| `1D` | `1.04` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 4,700.00 USD | 2,450.00 USD | 12,490.00 USD |
| `7D` | `1.04` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 288,650.00 USD | 9,430.00 USD | 93,080.00 USD |
| `7D` | `1.04` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD |
| `7D` | `1.04` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD |
| `7D` | `1.05` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD |
| `7D` | `1.05` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 195,180.00 USD | 28,070.00 USD | 167,700.00 USD |
| `7D` | `1.05` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 87,270.00 USD | 29,070.00 USD | 41,030.00 USD |
| `7D` | `1.05` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 140,530.00 USD | 49,780.00 USD | 143,430.00 USD |
| `7D` | `1.05` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 87,130.00 USD | 44,290.00 USD | 36,750.00 USD |
| `7D` | `1.06` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 185,840.00 USD | 48,000.00 USD | 121,890.00 USD |
| `7D` | `1.06` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 205,290.00 USD | 63,350.00 USD | 94,840.00 USD |
| `7D` | `1.06` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 217,790.00 USD | 73,000.00 USD | 125,100.00 USD |
| `7D` | `1.06` | 8,960,000.00 USD | 8,960,000.00 USD | 0.00 USD | 115,520.00 USD | 81,560.00 USD | 61,320.00 USD |
| `7D` | `1.06` | 9,050,000.00 USD | 9,050,000.00 USD | 0.00 USD | 63,260.00 USD | 25,320.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `173.35M` | Total OI Tokens: `184,589,125.9 DOT`
  * 1h OI Change: `+0.75%` | 4h OI Change: `-1.90%` | 24h OI Change: `-17.10%`
  * Exchange Breakdown: Binance=`33.67M` | Bybit=`22.10M` | OKX=`10.24M` | Hyperliquid=`5.84M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.66K` | Last 24h: `6.26K` | Last 3d: `-7.35K` | Last 7d: `-25.50K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0069%` |
| **USDT Bybit** | `0.0055%` | **USDT KuCoin** | `-0.0149%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0054%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `50.61%` | `49.39%` | `1.02` | 2,630,000.00 USD |
| `15M` | `Binance` | `53.34%` | `46.66%` | `1.14` | 418,840.00 USD |
| `15M` | `OKX` | `80.17%` | `19.83%` | `4.04` | 440,560.00 USD |
| `15M` | `Bybit` | `70.15%` | `29.85%` | `2.35` | 93,800.00 USD |
| `15M` | `KuCoin` | `72.37%` | `27.63%` | `2.62` | 80,470.00 USD |
| `15M` | `Gate` | `47.72%` | `52.28%` | `0.91` | 40,400.00 USD |
| `15M` | `Bitget` | `57.01%` | `42.99%` | `1.33` | 24,920.00 USD |
| `15M` | `BingX` | `7.34%` | `92.66%` | `0.08` | 516,860.00 USD |
| `15M` | `MEXC` | `71.26%` | `28.74%` | `2.48` | 30,060.00 USD |
| `15M` | `Bitunix` | `45.89%` | `54.11%` | `0.85` | 31,330.00 USD |
| `15M` | `Hyperliquid` | `69.07%` | `30.93%` | `2.23` | 8,770.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.21%` | `49.79%` | `1.01` | 835,980.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 82,850.00 USD |
| `15M` | `HTX` | `75.66%` | `24.34%` | `3.11` | 1,520.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `60.76%` | `39.24%` | `1.55` | 17,640.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 58.90 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `18.53%` | `81.47%` | `0.23` | 1,130.00 USD |
| `15M` | `Whale Positions` | `53.34%` | `46.66%` | `1.14` | 418,840.00 USD |
| `15M` | `Global Accounts` | `50.61%` | `49.39%` | `1.02` | 2,630,000.00 USD |
| `1H` | `DOT` | `52.88%` | `47.12%` | `1.12` | 7,980,000.00 USD |
| `1H` | `Binance` | `51.65%` | `48.35%` | `1.07` | 1,720,000.00 USD |
| `1H` | `OKX` | `62.44%` | `37.56%` | `1.66` | 923,980.00 USD |
| `1H` | `Bybit` | `55.29%` | `44.71%` | `1.24` | 315,480.00 USD |
| `1H` | `KuCoin` | `60.41%` | `39.59%` | `1.53` | 558,310.00 USD |
| `1H` | `Gate` | `43.61%` | `56.39%` | `0.77` | 128,940.00 USD |
| `1H` | `Bitget` | `50.8%` | `49.2%` | `1.03` | 97,380.00 USD |
| `1H` | `BingX` | `20.84%` | `79.16%` | `0.26` | 844,660.00 USD |
| `1H` | `MEXC` | `66.45%` | `33.55%` | `1.98` | 176,910.00 USD |
| `1H` | `Bitunix` | `53.5%` | `46.5%` | `1.15` | 163,820.00 USD |
| `1H` | `Hyperliquid` | `77.53%` | `22.47%` | `3.45` | 140,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.08%` | `49.92%` | `1.00` | 2,360,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `98.45%` | `1.55%` | `63.52` | 413,350.00 USD |
| `1H` | `HTX` | `15.07%` | `84.93%` | `0.18` | 5,320.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `28.02%` | `71.98%` | `0.39` | 96,070.00 USD |
| `1H` | `Aster` | `100%` | `0%` | `1.00` | 1,430.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `92.62%` | `7.38%` | `12.55` | 28,950.00 USD |
| `1H` | `Whale Positions` | `51.65%` | `48.35%` | `1.07` | 1,720,000.00 USD |
| `1H` | `Global Accounts` | `52.88%` | `47.12%` | `1.12` | 7,980,000.00 USD |
| `4H` | `DOT` | `47.49%` | `52.51%` | `0.90` | 31,120,000.00 USD |
| `4H` | `Binance` | `44.58%` | `55.42%` | `0.80` | 7,140,000.00 USD |
| `4H` | `OKX` | `49.98%` | `50.02%` | `1.00` | 2,700,000.00 USD |
| `4H` | `Bybit` | `47.19%` | `52.81%` | `0.89` | 1,410,000.00 USD |
| `4H` | `KuCoin` | `52.97%` | `47.03%` | `1.13` | 1,850,000.00 USD |
| `4H` | `Gate` | `40.97%` | `59.03%` | `0.69` | 567,820.00 USD |
| `4H` | `Bitget` | `61.33%` | `38.67%` | `1.59` | 490,020.00 USD |
| `4H` | `BingX` | `18.45%` | `81.55%` | `0.23` | 3,840,000.00 USD |
| `4H` | `MEXC` | `50.05%` | `49.95%` | `1.00` | 1,010,000.00 USD |
| `4H` | `Bitunix` | `50.25%` | `49.75%` | `1.01` | 595,240.00 USD |
| `4H` | `Hyperliquid` | `44.77%` | `55.23%` | `0.81` | 426,650.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.97%` | `50.03%` | `1.00` | 8,530,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `94.06%` | `5.94%` | `15.84` | 2,120,000.00 USD |
| `4H` | `HTX` | `38.05%` | `61.95%` | `0.61` | 21,660.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `15.7%` | `84.3%` | `0.19` | 373,660.00 USD |
| `4H` | `Aster` | `46.91%` | `53.09%` | `0.88` | 4,460.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `85.09%` | `14.91%` | `5.71` | 57,320.00 USD |
| `4H` | `Whale Positions` | `44.58%` | `55.42%` | `0.80` | 7,140,000.00 USD |
| `4H` | `Global Accounts` | `47.49%` | `52.51%` | `0.90` | 31,120,000.00 USD |


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
| `5:00 UTC` | `0.9374` | `0.9390` | `0.9374` | `0.9427` | `0.9366` | 318,282.61 USD | 174,701.26 USD | 143,581.36 USD | 31,119.90 USD | `+9.78%` | `10B / 9S` |

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
| `5m` | 10,510.00 USD | -20,260.00 USD | **`DISTRIBUTION`** |
| `15m` | 16,130.00 USD | 69,440.00 USD | **`ACCUMULATION`** |
| `30m` | -40,760.00 USD | 80,450.00 USD | **`ACCUMULATION`** |
| `1h` | -48,870.00 USD | -51,910.00 USD | **`DISTRIBUTION`** |
| `2h` | -92,250.00 USD | -677,960.00 USD | **`DISTRIBUTION`** |
| `4h` | -73,230.00 USD | -1,380,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -235,520.00 USD | -2,450,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -200,620.00 USD | -1,840,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -525,950.00 USD | -1,470,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,350,000.00 USD | -9,320,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,860,000.00 USD | -23,510,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,730,000.00 USD | -78,830,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+10.51K` | 15m=`+16.13K` | 1h=`-48.87K` | 24h=`-1.35M`
* Futures Capital Netflows: 5m=`-20.26K` | 15m=`+69.44K` | 1h=`-51.91K` | 24h=`-9.32M`
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
  * Execution Entry: `0.9004` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.8625` (Risk Distance: `0.0400` pts)
  * +2.5R Take Profit: `1.00`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9447` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9826` (Risk Distance: `0.0400` pts)
  * +2.5R Take Profit: `0.8447`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9505`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
