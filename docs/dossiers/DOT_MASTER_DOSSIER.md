# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 17:10:08 IST` (`2026-10-30 11:40:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `0.9112` | VWAP Z-Score: `+0.82` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0065` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `53.02` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.9798` | Lower -3.00σ Band: `0.8427`
  * Upper +2.51σ Band: `0.9686` | Lower -2.51σ Band: `0.8539`
  * Upper +2.01σ Band: `0.9572` | Lower -2.01σ Band: `0.8653`
  * Upper +2.00σ Band: `0.9570` | Lower -2.00σ Band: `0.8655`
  * Upper +1.28σ Band: `0.9405` | Lower -1.28σ Band: `0.8820`
  * Upper +1.00σ Band: `0.9341` | Lower -1.00σ Band: `0.8884`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9274` | EMA-20=`0.9276` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9292` (Slope: `+0.0000`) | EMA-100=`0.9396`
  * Institutional Anchors: EMA-144=`0.9474` | EMA-200=`0.9557` (Slope: `-0.3973`) | EMA-233=`0.9588`
- **Range Boundaries**: 24H High=`1.01` | 24H Low=`0.8570` | Weekly High=`1.03` | Weekly Low=`0.8570`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9447` (Distance: `-0.86%`)
  * Point of Control (POC) = `0.9119` (Distance: `+2.70%`)
  * Value Area Low (VAL) = `0.9010` (Distance: `+3.94%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `0.9333` - `0.9407`
  * Optimal Trade Entry (OTE 0.705): `0.9389`
  * Structural Invalidation Anchor (0.786): `0.9445`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9427` | `0.9442` | `0.9394` | `0.9398` | `183,419` | 172,915.80 USD | 34,978.55 USD | `+20.23%` | -5,857,830.01 USD | `+1.59` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.9399` | `0.9412` | `0.9392` | `0.9400` | `114,663` | 107,792.01 USD | 3,922.51 USD | `+3.64%` | -5,853,907.50 USD | `+0.56` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.9400` | `0.9408` | `0.9384` | `0.9390` | `51,342` | 48,222.10 USD | -16,773.15 USD | `-34.78%` | -5,870,680.66 USD | `-0.20` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9327` | `0.9399` | `0.9325` | `0.9383` | `644,715` | 603,897.34 USD | 5,468.79 USD | `+0.91%` | -5,905,463.42 USD | `+0.91` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.9384` | `0.9430` | `0.9366` | `0.9428` | `386,274` | 362,865.52 USD | 12,654.86 USD | `+3.49%` | -5,892,808.56 USD | `+0.94` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.9427` | `0.9442` | `0.9384` | `0.9390` | `349,410` | 328,917.34 USD | 22,115.32 USD | `+6.72%` | -5,870,693.24 USD | `+0.98` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.9375` | `0.9390` | `0.9292` | `0.9340` | `1,605,127` | 1,499,731.69 USD | -461,107.04 USD | `-30.75%` | -5,771,335.00 USD | `-0.17` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.9340` | `0.9430` | `0.9302` | `0.9428` | `1,710,321` | 1,600,393.57 USD | -75,841.93 USD | `-4.74%` | -5,847,176.93 USD | `+0.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9427` | `0.9442` | `0.9384` | `0.9390` | `349,410` | 328,917.34 USD | 22,115.32 USD | `+6.72%` | -5,825,061.61 USD | `+0.32` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,092,983.65 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9603` | `0.9263` | `0.9454` | `10,832,060` | 10,247,507.62 USD | -822,915.31 USD | `-8.03%` | -4,915,898.96 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9454` | `0.9488` | `0.9292` | `0.9390` | `5,517,917` | 5,173,308.47 USD | -909,162.65 USD | `-17.57%` | -5,825,061.61 USD | `+0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -974,642.25 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,499,370.98 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,092,983.65 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9603` | `0.9263` | `0.9454` | `10,832,060` | 10,247,507.62 USD | -822,915.31 USD | `-8.03%` | -4,915,898.96 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9454` | `0.9488` | `0.9292` | `0.9390` | `5,517,917` | 5,173,308.47 USD | -909,162.65 USD | `-17.57%` | -5,825,061.61 USD | `+0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:52:59 IST` |

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
| `Live` | `Long Liquidation` | `0.2015` | 127.47 USD | 486,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2135` | 106.75 USD | 486,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3565` | 787.51 USD | 486,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4195` | 5,190.00 USD | 485,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4685` | 147.02 USD | 480,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4705` | 2,590.00 USD | 480,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 193.74 USD | 477,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5065` | 3,290.00 USD | 477,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5375` | 213.12 USD | 474,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5505` | 550.50 USD | 473,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 14,600.00 USD | 473,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 577.36 USD | 458,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 683.51 USD | 458,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 137.53 USD | 457,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6055` | 1,480.00 USD | 457,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6075` | 1,810.00 USD | 455,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 105.96 USD | 454,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 147.48 USD | 453,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6295` | 220.32 USD | 453,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 757.80 USD | 453,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 106.00 USD | 452,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 507.86 USD | 452,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 2,090.00 USD | 452,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 20,300.00 USD | 450,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 4,230.00 USD | 429,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 202.47 USD | 425,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 149.44 USD | 425,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 63,890.00 USD | 425,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 423.10 USD | 361,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 512.97 USD | 360,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6855` | 19,630.00 USD | 360,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 322.62 USD | 340,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7005` | 1,140.00 USD | 340,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7065` | 157.83 USD | 339,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 988.87 USD | 339,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7225` | 1,580.00 USD | 338,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 397.93 USD | 336,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7245` | 108,670.00 USD | 336,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7295` | 291.58 USD | 227,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 2,300.00 USD | 227,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,140.00 USD | 224,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 283.30 USD | 223,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7515` | 32,890.00 USD | 223,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 910.22 USD | 190,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 629.25 USD | 189,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 144.07 USD | 189,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7565` | 8,860.00 USD | 188,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7635` | 308.00 USD | 180,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7705` | 152.94 USD | 179,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 3,840.00 USD | 179,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7775` | 2,490.00 USD | 175,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7855` | 55,770.00 USD | 173,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 156.51 USD | 117,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7905` | 277.39 USD | 117,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7935` | 1,760.00 USD | 117,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7985` | 210.40 USD | 115,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8030` | 3,090,000.00 USD | 3,090,000.00 USD | 9,970.00 USD | 5,760.00 USD | 10,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8050` | 3,070,000.00 USD | 3,070,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8070` | 3,050,000.00 USD | 3,050,000.00 USD | 12,160.00 USD | 4,660.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8090` | 3,010,000.00 USD | 3,010,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8110` | 3,000,000.00 USD | 3,000,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8130` | 3,000,000.00 USD | 3,000,000.00 USD | 14,060.00 USD | 2,970.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 115,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8150` | 2,970,000.00 USD | 2,970,000.00 USD | 61,120.00 USD | 7,590.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8170` | 2,880,000.00 USD | 2,880,000.00 USD | 10,780.00 USD | 8,770.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8190` | 2,850,000.00 USD | 2,850,000.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8210` | 2,840,000.00 USD | 2,840,000.00 USD | 7,510.00 USD | 3,290.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 114,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8230` | 2,820,000.00 USD | 2,820,000.00 USD | 29,430.00 USD | 5,100.00 USD | 13,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 749.96 USD | 112,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8250` | 2,770,000.00 USD | 2,770,000.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 2,760,000.00 USD | 2,760,000.00 USD | 4,320.00 USD | 5,770.00 USD | 616.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8290` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8310` | 2,740,000.00 USD | 2,740,000.00 USD | 9,280.00 USD | 1,660.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8330` | 2,730,000.00 USD | 2,730,000.00 USD | 16,220.00 USD | 11,360.00 USD | 77.95 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8345` | 626.21 USD | 111,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8350` | 2,700,000.00 USD | 2,700,000.00 USD | 19,490.00 USD | 0.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 111,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8370` | 2,490,000.00 USD | 2,490,000.00 USD | 18,140.00 USD | 2,530.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8370` | 2,680,000.00 USD | 2,680,000.00 USD | 15,240.00 USD | 1,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8390` | 2,450,000.00 USD | 2,450,000.00 USD | 1,740.00 USD | 745.84 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8390` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8410` | 2,450,000.00 USD | 2,450,000.00 USD | 1,470.00 USD | 2,040.00 USD | 1,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8410` | 2,650,000.00 USD | 2,650,000.00 USD | 270.00 USD | 3,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,570.00 USD | 110,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8430` | 2,440,000.00 USD | 2,440,000.00 USD | 4,670.00 USD | 6,880.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8430` | 2,650,000.00 USD | 2,650,000.00 USD | 11,320.00 USD | 3,840.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8450` | 2,430,000.00 USD | 2,430,000.00 USD | 2,530.00 USD | 8,430.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8450` | 2,630,000.00 USD | 2,630,000.00 USD | 1,980.00 USD | 404.64 USD | 474.61 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8470` | 2,420,000.00 USD | 2,420,000.00 USD | 24,200.00 USD | 1,110.00 USD | 1,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8470` | 2,630,000.00 USD | 2,630,000.00 USD | 7,900.00 USD | 5,280.00 USD | 2,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8490` | 2,390,000.00 USD | 2,390,000.00 USD | 6,900.00 USD | 5,020.00 USD | 7,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8490` | 2,610,000.00 USD | 2,610,000.00 USD | 22,370.00 USD | 9,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 109,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8510` | 2,370,000.00 USD | 2,370,000.00 USD | 13,560.00 USD | 4,140.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 2,580,000.00 USD | 2,580,000.00 USD | 14,280.00 USD | 991.53 USD | 21,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8530` | 2,340,000.00 USD | 2,340,000.00 USD | 4,680.00 USD | 3,830.00 USD | 5,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 2,540,000.00 USD | 2,540,000.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8550` | 2,320,000.00 USD | 2,320,000.00 USD | 18,270.00 USD | 3,040.00 USD | 5,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 2,540,000.00 USD | 2,540,000.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8570` | 2,300,000.00 USD | 2,300,000.00 USD | 989.11 USD | 1,720.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8570` | 2,530,000.00 USD | 2,530,000.00 USD | 3,540.00 USD | 944.22 USD | 8,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 107,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8590` | 2,290,000.00 USD | 2,290,000.00 USD | 6,870.00 USD | 10,640.00 USD | 6,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8590` | 2,520,000.00 USD | 2,520,000.00 USD | 3,730.00 USD | 0.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8610` | 2,260,000.00 USD | 2,260,000.00 USD | 8,320.00 USD | 855.53 USD | 16,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8610` | 2,510,000.00 USD | 2,510,000.00 USD | 9,960.00 USD | 3,660.00 USD | 35,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8630` | 2,240,000.00 USD | 2,240,000.00 USD | 39,330.00 USD | 12,290.00 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8630` | 2,470,000.00 USD | 2,470,000.00 USD | 758.91 USD | 2,910.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 107,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 107,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8650` | 2,180,000.00 USD | 2,180,000.00 USD | 17,640.00 USD | 2,110.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8650` | 2,460,000.00 USD | 2,460,000.00 USD | 47,860.00 USD | 18,930.00 USD | 184.85 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,390.00 USD | 106,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8670` | 2,160,000.00 USD | 2,160,000.00 USD | 12,000.00 USD | 10,090.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8670` | 2,390,000.00 USD | 2,390,000.00 USD | 13,660.00 USD | 3,720.00 USD | 12,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8690` | 2,140,000.00 USD | 2,140,000.00 USD | 42,010.00 USD | 3,780.00 USD | 29,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8690` | 2,360,000.00 USD | 2,360,000.00 USD | 160,750.00 USD | 13,110.00 USD | 46,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 12,590.00 USD | 105,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8705` | 92,480.00 USD | 92,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8710` | 2,060,000.00 USD | 2,060,000.00 USD | 42,290.00 USD | 24,900.00 USD | 28,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8710` | 2,140,000.00 USD | 2,140,000.00 USD | 7,370.00 USD | 23,340.00 USD | 13,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8730` | 1,970,000.00 USD | 1,970,000.00 USD | 54,500.00 USD | 21,510.00 USD | 25,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 8,170.00 USD | 295.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8750` | 1,870,000.00 USD | 1,870,000.00 USD | 37,070.00 USD | 6,900.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 6,380.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8770` | 1,800,000.00 USD | 1,800,000.00 USD | 10,690.00 USD | 152.79 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8770` | 2,080,000.00 USD | 2,080,000.00 USD | 1,390.00 USD | 0.00 USD | 30,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8790` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 40.93 USD | 50,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 2,040,000.00 USD | 2,040,000.00 USD | 873.30 USD | 5,580.00 USD | 53,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8810` | 1,740,000.00 USD | 1,740,000.00 USD | 13,820.00 USD | 5,210.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 1,980,000.00 USD | 1,980,000.00 USD | 1,830.00 USD | 240.78 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8830` | 1,720,000.00 USD | 1,720,000.00 USD | 656.20 USD | 5,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8830` | 1,980,000.00 USD | 1,980,000.00 USD | 2,320.00 USD | 10,140.00 USD | 11,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8850` | 1,710,000.00 USD | 1,710,000.00 USD | 5,680.00 USD | 34,880.00 USD | 11,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8850` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 5,800.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8865` | 212.67 USD | 212.67 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8870` | 1,660,000.00 USD | 1,660,000.00 USD | 68,700.00 USD | 16,710.00 USD | 32,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8870` | 1,950,000.00 USD | 1,950,000.00 USD | 271,870.00 USD | 22,320.00 USD | 81,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8890` | 1,540,000.00 USD | 1,540,000.00 USD | 69,610.00 USD | 40,830.00 USD | 4,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8890` | 1,570,000.00 USD | 1,570,000.00 USD | 54,380.00 USD | 73,890.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8910` | 1,430,000.00 USD | 1,430,000.00 USD | 2,770.00 USD | 38,730.00 USD | 20,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8910` | 1,430,000.00 USD | 1,430,000.00 USD | 75,300.00 USD | 22,240.00 USD | 34,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8930` | 1,370,000.00 USD | 1,370,000.00 USD | 57,080.00 USD | 23,480.00 USD | 37,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8930` | 1,300,000.00 USD | 1,300,000.00 USD | 62,870.00 USD | 23,560.00 USD | 9,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8950` | 1,250,000.00 USD | 1,250,000.00 USD | 6,700.00 USD | 15,420.00 USD | 8,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8950` | 1,200,000.00 USD | 1,200,000.00 USD | 7,120.00 USD | 37,670.00 USD | 57,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8970` | 1,220,000.00 USD | 1,220,000.00 USD | 8,300.00 USD | 27,310.00 USD | 19,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8970` | 1,100,000.00 USD | 1,100,000.00 USD | 2,140.00 USD | 11,010.00 USD | 56,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8990` | 1,160,000.00 USD | 1,160,000.00 USD | 3,650.00 USD | 24,130.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8990` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 34,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9010` | 1,130,000.00 USD | 1,130,000.00 USD | 5,490.00 USD | 28,480.00 USD | 7,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9010` | 995,960.00 USD | 995,960.00 USD | 0.00 USD | 51,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9030` | 1,090,000.00 USD | 1,090,000.00 USD | 10,610.00 USD | 19,460.00 USD | 20,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9030` | 944,690.00 USD | 944,690.00 USD | 0.00 USD | 27,770.00 USD | 23,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9050` | 1,040,000.00 USD | 1,040,000.00 USD | 23,790.00 USD | 18,920.00 USD | 22,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9050` | 892,990.00 USD | 892,990.00 USD | 0.00 USD | 3,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9070` | 975,680.00 USD | 975,680.00 USD | 36,650.00 USD | 8,370.00 USD | 33,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9070` | 889,150.00 USD | 889,150.00 USD | 23,910.00 USD | 0.00 USD | 42,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9090` | 897,140.00 USD | 897,140.00 USD | 7,100.00 USD | 9,080.00 USD | 239.84 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9110` | 880,730.00 USD | 880,730.00 USD | 25,560.00 USD | 2,850.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9130` | 850,240.00 USD | 850,240.00 USD | 17,080.00 USD | 9,480.00 USD | 22,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9130` | 823,200.00 USD | 823,200.00 USD | 0.00 USD | 0.00 USD | 20,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9150` | 801,360.00 USD | 801,360.00 USD | 11,120.00 USD | 17,780.00 USD | 24,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9150` | 802,480.00 USD | 802,480.00 USD | 0.00 USD | 12,890.00 USD | 16,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9170` | 747,800.00 USD | 747,800.00 USD | 7,300.00 USD | 16,660.00 USD | 15,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9170` | 773,460.00 USD | 773,460.00 USD | 0.00 USD | 0.00 USD | 33,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9190` | 708,750.00 USD | 708,750.00 USD | 9,900.00 USD | 15,280.00 USD | 16,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9190` | 740,280.00 USD | 740,280.00 USD | 0.00 USD | 4,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9210` | 666,600.00 USD | 666,600.00 USD | 12,850.00 USD | 7,480.00 USD | 10,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9210` | 735,410.00 USD | 735,410.00 USD | 0.00 USD | 7,760.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9230` | 635,490.00 USD | 635,490.00 USD | 9,860.00 USD | 10,950.00 USD | 21,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9230` | 723,680.00 USD | 723,680.00 USD | 294,370.00 USD | 22,800.00 USD | 26,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9250` | 592,980.00 USD | 592,980.00 USD | 108,890.00 USD | 74,100.00 USD | 62,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9250` | 379,830.00 USD | 379,830.00 USD | 0.00 USD | 52,780.00 USD | 84,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9270` | 347,460.00 USD | 347,460.00 USD | 39,920.00 USD | 7,040.00 USD | 73,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9270` | 242,980.00 USD | 242,980.00 USD | 44,020.00 USD | 11,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9290` | 226,690.00 USD | 226,690.00 USD | 80,950.00 USD | 20,440.00 USD | 38,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9290` | 187,160.00 USD | 187,160.00 USD | 0.00 USD | 12,750.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9310` | 86,740.00 USD | 86,740.00 USD | 0.00 USD | 7,130.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9330` | 74,200.00 USD | 74,200.00 USD | 3,720.00 USD | 6,140.00 USD | 26,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9330` | 172,810.00 USD | 172,810.00 USD | 37,450.00 USD | 0.00 USD | 31,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9350` | 37,740.00 USD | 37,740.00 USD | 36,510.00 USD | 197.86 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9350` | 104,000.00 USD | 104,000.00 USD | 0.00 USD | 0.00 USD | 19,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9370` | 1,030.00 USD | 1,030.00 USD | 0.00 USD | 182.01 USD | 852.35 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9370` | 84,400.00 USD | 84,400.00 USD | 16,340.00 USD | 19,540.00 USD | 48,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9390` | 1,650.00 USD | 1,650.00 USD | 1,340.00 USD | 309.30 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9390` | 3,300.00 USD | 3,300.00 USD | 1,340.00 USD | 309.30 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9390` | 74,160.00 USD | 74,160.00 USD | 39,250.00 USD | 0.00 USD | 34,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9410` | 4,210.00 USD | 4,210.00 USD | 673.54 USD | 239.40 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9410` | 237,210.00 USD | 237,210.00 USD | 161,930.00 USD | 1,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9430` | 5,670.00 USD | 5,670.00 USD | 1,230.00 USD | 224.96 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 261,500.00 USD | 261,500.00 USD | 0.00 USD | 20,890.00 USD | 3,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9470` | 6,190.00 USD | 6,190.00 USD | 0.00 USD | 199.60 USD | 319.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 348,010.00 USD | 348,010.00 USD | 3,540.00 USD | 6,380.00 USD | 76,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9490` | 84,260.00 USD | 84,260.00 USD | 78,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 431,950.00 USD | 431,950.00 USD | 2,770.00 USD | 10,340.00 USD | 70,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9510` | 95,250.00 USD | 95,250.00 USD | 5,190.00 USD | 813.18 USD | 4,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 723,340.00 USD | 723,340.00 USD | 258,650.00 USD | 28,180.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9530` | 116,880.00 USD | 116,880.00 USD | 7,370.00 USD | 8,490.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 744,400.00 USD | 744,400.00 USD | 0.00 USD | 20,610.00 USD | 447.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9550` | 189,870.00 USD | 189,870.00 USD | 25,300.00 USD | 39,260.00 USD | 8,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 764,130.00 USD | 764,130.00 USD | 0.00 USD | 19,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9570` | 226,470.00 USD | 226,470.00 USD | 13,680.00 USD | 13,280.00 USD | 9,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 782,160.00 USD | 782,160.00 USD | 1,910.00 USD | 15,160.00 USD | 957.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9590` | 256,690.00 USD | 256,690.00 USD | 14,060.00 USD | 7,480.00 USD | 8,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 803,230.00 USD | 803,230.00 USD | 1,980.00 USD | 18,220.00 USD | 866.69 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9610` | 321,020.00 USD | 321,020.00 USD | 18,020.00 USD | 15,760.00 USD | 30,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9610` | 851,410.00 USD | 851,410.00 USD | 24,370.00 USD | 22,800.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9630` | 519,040.00 USD | 519,040.00 USD | 110,950.00 USD | 41,450.00 USD | 45,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 1,020,000.00 USD | 1,020,000.00 USD | 56,160.00 USD | 31,820.00 USD | 84,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9650` | 660,420.00 USD | 660,420.00 USD | 29,080.00 USD | 33,020.00 USD | 79,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 1,130,000.00 USD | 1,130,000.00 USD | 97,600.00 USD | 0.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9670` | 756,850.00 USD | 756,850.00 USD | 53,970.00 USD | 16,730.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9670` | 1,180,000.00 USD | 1,180,000.00 USD | 40,070.00 USD | 5,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9690` | 798,180.00 USD | 798,180.00 USD | 14,860.00 USD | 14,610.00 USD | 11,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 21,100.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9710` | 911,370.00 USD | 911,370.00 USD | 15,040.00 USD | 19,120.00 USD | 79,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 24,440.00 USD | 31,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9730` | 1,000,000.00 USD | 1,000,000.00 USD | 37,900.00 USD | 14,900.00 USD | 40,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 1,330,000.00 USD | 1,330,000.00 USD | 2,910.00 USD | 9,290.00 USD | 27,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9750` | 1,080,000.00 USD | 1,080,000.00 USD | 29,660.00 USD | 13,550.00 USD | 34,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 1,400,000.00 USD | 1,400,000.00 USD | 2,090.00 USD | 17,230.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9770` | 1,190,000.00 USD | 1,190,000.00 USD | 78,910.00 USD | 16,960.00 USD | 13,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 1,500,000.00 USD | 1,500,000.00 USD | 49,900.00 USD | 18,660.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9790` | 1,270,000.00 USD | 1,270,000.00 USD | 38,220.00 USD | 13,210.00 USD | 28,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 15,280.00 USD | 85,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 102.95 USD | 102.95 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9810` | 1,340,000.00 USD | 1,340,000.00 USD | 21,440.00 USD | 13,940.00 USD | 28,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9810` | 1,720,000.00 USD | 1,720,000.00 USD | 540.00 USD | 4,020.00 USD | 119,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9830` | 1,450,000.00 USD | 1,450,000.00 USD | 33,340.00 USD | 27,220.00 USD | 55,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 1,960,000.00 USD | 1,960,000.00 USD | 124,720.00 USD | 15,810.00 USD | 94,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9850` | 1,530,000.00 USD | 1,530,000.00 USD | 47,310.00 USD | 8,800.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 211.77 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9870` | 1,570,000.00 USD | 1,570,000.00 USD | 14,930.00 USD | 6,470.00 USD | 22,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 2,090,000.00 USD | 2,090,000.00 USD | 40,020.00 USD | 0.00 USD | 67,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9875` | 211.62 USD | 314.57 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9890` | 1,630,000.00 USD | 1,630,000.00 USD | 27,890.00 USD | 3,780.00 USD | 30,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9890` | 2,110,000.00 USD | 2,110,000.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9910` | 1,740,000.00 USD | 1,740,000.00 USD | 60,130.00 USD | 5,890.00 USD | 45,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9910` | 2,150,000.00 USD | 2,150,000.00 USD | 3,700.00 USD | 800.44 USD | 35,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9925` | 3,940.00 USD | 4,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9930` | 1,770,000.00 USD | 1,770,000.00 USD | 16,320.00 USD | 5,130.00 USD | 8,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9930` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 36,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9935` | 212.91 USD | 4,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9945` | 426.24 USD | 4,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9950` | 1,810,000.00 USD | 1,810,000.00 USD | 29,250.00 USD | 2,120.00 USD | 7,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9950` | 2,310,000.00 USD | 2,310,000.00 USD | 63,060.00 USD | 5,380.00 USD | 58,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9970` | 1,870,000.00 USD | 1,870,000.00 USD | 46,950.00 USD | 1,870.00 USD | 13,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 2,410,000.00 USD | 2,410,000.00 USD | 95,130.00 USD | 253.35 USD | 4,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9985` | 852.22 USD | 5,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9990` | 1,940,000.00 USD | 1,940,000.00 USD | 35,340.00 USD | 17,910.00 USD | 10,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 6,490.00 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,010,000.00 USD | 2,010,000.00 USD | 45,050.00 USD | 10,790.00 USD | 13,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,470,000.00 USD | 2,470,000.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,040,000.00 USD | 2,040,000.00 USD | 12,580.00 USD | 9,310.00 USD | 6,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,620,000.00 USD | 2,620,000.00 USD | 107,670.00 USD | 21,850.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,100,000.00 USD | 2,100,000.00 USD | 54,780.00 USD | 5,520.00 USD | 5,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,670,000.00 USD | 2,670,000.00 USD | 32,430.00 USD | 3,970.00 USD | 12,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,200,000.00 USD | 2,200,000.00 USD | 50,600.00 USD | 11,770.00 USD | 38,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,730,000.00 USD | 2,730,000.00 USD | 35,710.00 USD | 240.78 USD | 29,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,250,000.00 USD | 2,250,000.00 USD | 30,870.00 USD | 13,790.00 USD | 7,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,760,000.00 USD | 2,760,000.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,280,000.00 USD | 2,280,000.00 USD | 9,660.00 USD | 17,670.00 USD | 265.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,800,000.00 USD | 2,800,000.00 USD | 20,090.00 USD | 17,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,300,000.00 USD | 2,300,000.00 USD | 10,450.00 USD | 1,540.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,850,000.00 USD | 2,850,000.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,340,000.00 USD | 2,340,000.00 USD | 14,310.00 USD | 18,100.00 USD | 14,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 26,510.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,360,000.00 USD | 2,360,000.00 USD | 3,990.00 USD | 2,940.00 USD | 12,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,930,000.00 USD | 2,930,000.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,440,000.00 USD | 2,440,000.00 USD | 55,630.00 USD | 4,860.00 USD | 10,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,040,000.00 USD | 3,040,000.00 USD | 17,960.00 USD | 83,360.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 760.04 USD | 6,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,470,000.00 USD | 2,470,000.00 USD | 6,670.00 USD | 7,410.00 USD | 21,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,210,000.00 USD | 3,210,000.00 USD | 61,450.00 USD | 32,840.00 USD | 68,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 218.91 USD | 6,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,560,000.00 USD | 2,560,000.00 USD | 40,460.00 USD | 18,460.00 USD | 29,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,520,000.00 USD | 3,520,000.00 USD | 82,230.00 USD | 86,210.00 USD | 146,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,620,000.00 USD | 2,620,000.00 USD | 39,730.00 USD | 5,800.00 USD | 17,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,630,000.00 USD | 3,630,000.00 USD | 28,320.00 USD | 48,490.00 USD | 37,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,660,000.00 USD | 2,660,000.00 USD | 15,190.00 USD | 11,870.00 USD | 8,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,950,000.00 USD | 3,950,000.00 USD | 161,070.00 USD | 129,470.00 USD | 25,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.03` | 220.19 USD | 6,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.03` | 152.32 USD | 7,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,700,000.00 USD | 2,700,000.00 USD | 11,620.00 USD | 13,840.00 USD | 15,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,160,000.00 USD | 4,160,000.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,810,000.00 USD | 2,810,000.00 USD | 65,750.00 USD | 8,920.00 USD | 32,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,360,000.00 USD | 4,360,000.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,840,000.00 USD | 2,840,000.00 USD | 12,420.00 USD | 2,140.00 USD | 17,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,490,000.00 USD | 4,490,000.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.03` | 221.28 USD | 7,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,870,000.00 USD | 2,870,000.00 USD | 11,210.00 USD | 15,190.00 USD | 8,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,800,000.00 USD | 4,800,000.00 USD | 259,060.00 USD | 11,850.00 USD | 43,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,930,000.00 USD | 2,930,000.00 USD | 44,200.00 USD | 6,370.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,110,000.00 USD | 5,110,000.00 USD | 193,150.00 USD | 3,330.00 USD | 109,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 333.46 USD | 7,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,950,000.00 USD | 2,950,000.00 USD | 7,640.00 USD | 5,430.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,490,000.00 USD | 5,490,000.00 USD | 239,580.00 USD | 9,010.00 USD | 134,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,970,000.00 USD | 2,970,000.00 USD | 4,700.00 USD | 2,450.00 USD | 12,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,940,000.00 USD | 5,940,000.00 USD | 285,690.00 USD | 2,090.00 USD | 159,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 223.41 USD | 7,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,140,000.00 USD | 6,140,000.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,410,000.00 USD | 6,410,000.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 6,930,000.00 USD | 6,930,000.00 USD | 178,890.00 USD | 96,370.00 USD | 244,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 367.04 USD | 8,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,120,000.00 USD | 7,120,000.00 USD | 108,060.00 USD | 13,780.00 USD | 77,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,440,000.00 USD | 7,440,000.00 USD | 173,140.00 USD | 43,690.00 USD | 96,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,640,000.00 USD | 7,640,000.00 USD | 68,010.00 USD | 58,070.00 USD | 74,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,870,000.00 USD | 7,870,000.00 USD | 121,450.00 USD | 33,860.00 USD | 72,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,260,000.00 USD | 8,260,000.00 USD | 218,860.00 USD | 70,160.00 USD | 106,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,720,000.00 USD | 8,720,000.00 USD | 239,650.00 USD | 74,380.00 USD | 145,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,980,000.00 USD | 8,980,000.00 USD | 129,140.00 USD | 55,290.00 USD | 76,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,200,000.00 USD | 9,200,000.00 USD | 132,250.00 USD | 46,140.00 USD | 38,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.07` | 229.41 USD | 8,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 2,230.00 USD | 10,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.11` | 170.02 USD | 10,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.11` | 2,440.00 USD | 13,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.12` | 240.98 USD | 13,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.14` | 14,370.00 USD | 27,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 126.85 USD | 28,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 11,730.00 USD | 39,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 239.77 USD | 40,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.37` | 3,870.00 USD | 43,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,200.00 USD | 47,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.43` | 530.97 USD | 47,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 121.12 USD | 47,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 176.42 USD | 47,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 1,810.00 USD | 49,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 782.81 USD | 50,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 78,700.00 USD | 129,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.63` | 2,440.00 USD | 131,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 8,240.00 USD | 139,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 243.81 USD | 140,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 300.33 USD | 140,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 324.22 USD | 140,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 190.42 USD | 140,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 13,140.00 USD | 154,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 380.81 USD | 154,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 208.37 USD | 154,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

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
| `Sell Stop` | `0.4015` | 370,880.00 USD | 0.00 USD | 120.45 USD | `-57.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 370,760.00 USD | 0.00 USD | 150.15 USD | `-46.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5435` | 370,610.00 USD | 0.00 USD | 186.15 USD | `-42.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 370,420.00 USD | 0.00 USD | 1,150.00 USD | `-30.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 369,270.00 USD | 0.00 USD | 781.90 USD | `-25.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 368,490.00 USD | 0.00 USD | 477.38 USD | `-24.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 368,020.00 USD | 0.00 USD | 341.33 USD | `-23.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 367,670.00 USD | 0.00 USD | 972.82 USD | `-23.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 366,700.00 USD | 0.00 USD | 160.20 USD | `-22.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7385` | 366,540.00 USD | 0.00 USD | 102.58 USD | `-21.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 366,440.00 USD | 0.00 USD | 289.49 USD | `-20.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7615` | 366,150.00 USD | 0.00 USD | 197.53 USD | `-19.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 365,950.00 USD | 0.00 USD | 14,570.00 USD | `-17.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 351,380.00 USD | 0.00 USD | 213.58 USD | `-16.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 351,170.00 USD | 0.00 USD | 274,830.00 USD | `-15.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 76,340.00 USD | 0.00 USD | 108.47 USD | `-15.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8025` | 76,230.00 USD | 0.00 USD | 2,010.00 USD | `-14.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 74,220.00 USD | 0.00 USD | 326.96 USD | `-14.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 73,890.00 USD | 0.00 USD | 405.75 USD | `-13.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 73,480.00 USD | 0.00 USD | 772.84 USD | `-11.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8415` | 72,710.00 USD | 0.00 USD | 2,670.00 USD | `-10.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8495` | 70,040.00 USD | 0.00 USD | 3,470.00 USD | `-9.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 66,570.00 USD | 0.00 USD | 9,180.00 USD | `-9.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 57,390.00 USD | 0.00 USD | 341.94 USD | `-9.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 57,050.00 USD | 0.00 USD | 1,150.00 USD | `-9.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 55,900.00 USD | 0.00 USD | 429.25 USD | `-8.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 55,470.00 USD | 0.00 USD | 223.30 USD | `-8.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 55,250.00 USD | 0.00 USD | 518.51 USD | `-8.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 54,730.00 USD | 0.00 USD | 128.39 USD | `-7.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 54,600.00 USD | 0.00 USD | 1,280.00 USD | `-7.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 53,320.00 USD | 0.00 USD | 205.24 USD | `-7.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 53,120.00 USD | 0.00 USD | 649.66 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 52,470.00 USD | 0.00 USD | 194.06 USD | `-6.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8845` | 52,270.00 USD | 0.00 USD | 193.35 USD | `-6.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 52,080.00 USD | 0.00 USD | 223.04 USD | `-5.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 51,860.00 USD | 0.00 USD | 10,840.00 USD | `-5.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 41,010.00 USD | 0.00 USD | 4,920.00 USD | `-5.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8915` | 36,100.00 USD | 0.00 USD | 121.15 USD | `-5.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 35,970.00 USD | 0.00 USD | 192.07 USD | `-5.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 35,780.00 USD | 0.00 USD | 195.32 USD | `-5.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8955` | 35,590.00 USD | 0.00 USD | 575.72 USD | `-5.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8965` | 35,010.00 USD | 0.00 USD | 196.87 USD | `-4.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8975` | 34,810.00 USD | 0.00 USD | 191.98 USD | `-4.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8985` | 34,620.00 USD | 0.00 USD | 2,870.00 USD | `-4.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9005` | 31,750.00 USD | 0.00 USD | 385.95 USD | `-4.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9025` | 31,360.00 USD | 0.00 USD | 398.91 USD | `-4.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9035` | 30,960.00 USD | 0.00 USD | 196.96 USD | `-4.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9045` | 30,770.00 USD | 0.00 USD | 300.38 USD | `-4.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9055` | 30,470.00 USD | 0.00 USD | 194.05 USD | `-3.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9065` | 30,270.00 USD | 0.00 USD | 198.61 USD | `-3.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9075` | 30,070.00 USD | 0.00 USD | 994.35 USD | `-3.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 29,080.00 USD | 0.00 USD | 363.40 USD | `-3.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9095` | 28,720.00 USD | 0.00 USD | 1,810.00 USD | `-3.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9115` | 26,910.00 USD | 0.00 USD | 134.99 USD | `-3.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9135` | 26,770.00 USD | 0.00 USD | 398.65 USD | `-3.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9145` | 26,380.00 USD | 0.00 USD | 195.98 USD | `-3.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9155` | 26,180.00 USD | 0.00 USD | 403.92 USD | `-2.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9165` | 25,780.00 USD | 0.00 USD | 198.06 USD | `-2.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9175` | 25,580.00 USD | 0.00 USD | 223.78 USD | `-2.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9185` | 25,350.00 USD | 0.00 USD | 899.85 USD | `-2.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9195` | 24,450.00 USD | 0.00 USD | 900.19 USD | `-2.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 23,550.00 USD | 0.00 USD | 2,920.00 USD | `-2.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9215` | 20,630.00 USD | 0.00 USD | 104.68 USD | `-2.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9225` | 20,530.00 USD | 0.00 USD | 201.94 USD | `-2.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9235` | 20,320.00 USD | 0.00 USD | 1,080.00 USD | `-2.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9245` | 19,240.00 USD | 0.00 USD | 201.45 USD | `-1.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9255` | 19,040.00 USD | 0.00 USD | 817.40 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9265` | 18,220.00 USD | 0.00 USD | 403.77 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9275` | 17,820.00 USD | 0.00 USD | 2,120.00 USD | `-1.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9285` | 15,700.00 USD | 0.00 USD | 1,090.00 USD | `-1.52%` | `TACTICAL (Retail Cluster)` |
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
| `Buy Stop` | `0.9585` | 67,290.00 USD | 719.26 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 67,550.00 USD | 261.16 USD | 0.00 USD | `+1.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9615` | 67,960.00 USD | 412.10 USD | 0.00 USD | `+1.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 69,870.00 USD | 1,910.00 USD | 0.00 USD | `+2.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 70,440.00 USD | 568.75 USD | 0.00 USD | `+2.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 70,800.00 USD | 364.58 USD | 0.00 USD | `+2.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 71,010.00 USD | 206.91 USD | 0.00 USD | `+2.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 71,830.00 USD | 824.91 USD | 0.00 USD | `+2.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 72,040.00 USD | 206.95 USD | 0.00 USD | `+2.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 74,070.00 USD | 2,030.00 USD | 0.00 USD | `+2.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 76,150.00 USD | 2,080.00 USD | 0.00 USD | `+2.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 76,540.00 USD | 387.83 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 77,370.00 USD | 830.10 USD | 0.00 USD | `+3.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 77,760.00 USD | 396.17 USD | 0.00 USD | `+3.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 78,440.00 USD | 676.53 USD | 0.00 USD | `+3.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 78,540.00 USD | 102.95 USD | 0.00 USD | `+3.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 80,570.00 USD | 2,030.00 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 80,920.00 USD | 346.13 USD | 0.00 USD | `+4.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 81,170.00 USD | 255.38 USD | 0.00 USD | `+4.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 81,400.00 USD | 223.91 USD | 0.00 USD | `+4.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9865` | 81,510.00 USD | 109.99 USD | 0.00 USD | `+4.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9885` | 81,610.00 USD | 104.78 USD | 0.00 USD | `+4.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 85,130.00 USD | 3,520.00 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 116,880.00 USD | 31,750.00 USD | 0.00 USD | `+5.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 117,290.00 USD | 403.06 USD | 0.00 USD | `+5.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 122,430.00 USD | 5,140.00 USD | 0.00 USD | `+5.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 159,740.00 USD | 37,310.00 USD | 0.00 USD | `+5.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 160,240.00 USD | 500.25 USD | 0.00 USD | `+6.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 200,830.00 USD | 40,590.00 USD | 0.00 USD | `+6.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 201,070.00 USD | 235.79 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 202,410.00 USD | 1,340.00 USD | 0.00 USD | `+6.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 202,560.00 USD | 146.66 USD | 0.00 USD | `+6.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 202,790.00 USD | 230.39 USD | 0.00 USD | `+6.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 202,920.00 USD | 127.65 USD | 0.00 USD | `+6.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 203,090.00 USD | 176.59 USD | 0.00 USD | `+6.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 203,500.00 USD | 409.86 USD | 0.00 USD | `+7.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 203,610.00 USD | 110.95 USD | 0.00 USD | `+7.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 204,230.00 USD | 615.60 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 204,790.00 USD | 561.17 USD | 0.00 USD | `+7.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 205,010.00 USD | 214.40 USD | 0.00 USD | `+8.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 205,260.00 USD | 249.88 USD | 0.00 USD | `+8.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 205,460.00 USD | 207.97 USD | 0.00 USD | `+8.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 205,670.00 USD | 208.26 USD | 0.00 USD | `+9.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 206,190.00 USD | 516.75 USD | 0.00 USD | `+9.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 206,540.00 USD | 348.86 USD | 0.00 USD | `+9.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 206,930.00 USD | 391.80 USD | 0.00 USD | `+9.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 207,340.00 USD | 413.76 USD | 0.00 USD | `+10.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 207,700.00 USD | 354.91 USD | 0.00 USD | `+10.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 209,600.00 USD | 1,900.00 USD | 0.00 USD | `+10.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 209,810.00 USD | 207.87 USD | 0.00 USD | `+10.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 210,020.00 USD | 207.97 USD | 0.00 USD | `+10.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 210,130.00 USD | 107.99 USD | 0.00 USD | `+11.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 284,960.00 USD | 74,840.00 USD | 0.00 USD | `+12.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 287,310.00 USD | 2,340.00 USD | 0.00 USD | `+13.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 289,480.00 USD | 2,170.00 USD | 0.00 USD | `+15.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 291,020.00 USD | 1,540.00 USD | 0.00 USD | `+15.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 300,940.00 USD | 9,930.00 USD | 0.00 USD | `+16.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 301,820.00 USD | 877.63 USD | 0.00 USD | `+17.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 301,990.00 USD | 171.09 USD | 0.00 USD | `+18.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 304,760.00 USD | 2,770.00 USD | 0.00 USD | `+19.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 306,800.00 USD | 2,040.00 USD | 0.00 USD | `+19.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 306,970.00 USD | 172.17 USD | 0.00 USD | `+19.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 307,140.00 USD | 172.32 USD | 0.00 USD | `+19.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 307,330.00 USD | 187.72 USD | 0.00 USD | `+19.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 307,520.00 USD | 188.39 USD | 0.00 USD | `+20.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 310,180.00 USD | 2,670.00 USD | 0.00 USD | `+20.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 310,360.00 USD | 174.23 USD | 0.00 USD | `+20.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 310,530.00 USD | 174.38 USD | 0.00 USD | `+20.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 310,710.00 USD | 174.84 USD | 0.00 USD | `+20.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 310,850.00 USD | 144.70 USD | 0.00 USD | `+21.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 311,000.00 USD | 151.03 USD | 0.00 USD | `+21.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 311,150.00 USD | 151.16 USD | 0.00 USD | `+21.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 313,200.00 USD | 2,050.00 USD | 0.00 USD | `+23.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 313,310.00 USD | 110.00 USD | 0.00 USD | `+24.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 313,790.00 USD | 475.80 USD | 0.00 USD | `+26.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 315,000.00 USD | 1,210.00 USD | 0.00 USD | `+27.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 357,920.00 USD | 42,930.00 USD | 0.00 USD | `+27.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 359,930.00 USD | 2,000.00 USD | 0.00 USD | `+30.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 361,310.00 USD | 1,380.00 USD | 0.00 USD | `+32.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 361,560.00 USD | 245.41 USD | 0.00 USD | `+35.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 369,950.00 USD | 8,390.00 USD | 0.00 USD | `+36.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 370,370.00 USD | 415.25 USD | 0.00 USD | `+37.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 376,880.00 USD | 6,520.00 USD | 0.00 USD | `+38.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 381,680.00 USD | 4,800.00 USD | 0.00 USD | `+38.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 382,340.00 USD | 655.75 USD | 0.00 USD | `+39.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 382,930.00 USD | 596.43 USD | 0.00 USD | `+41.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 384,750.00 USD | 1,810.00 USD | 0.00 USD | `+42.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 398,630.00 USD | 13,880.00 USD | 0.00 USD | `+42.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 399,880.00 USD | 1,250.00 USD | 0.00 USD | `+43.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 401,950.00 USD | 2,070.00 USD | 0.00 USD | `+47.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 402,090.00 USD | 140.05 USD | 0.00 USD | `+48.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 402,250.00 USD | 160.42 USD | 0.00 USD | `+48.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 403,200.00 USD | 954.32 USD | 0.00 USD | `+49.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 437,380.00 USD | 34,170.00 USD | 0.00 USD | `+52.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 438,260.00 USD | 879.84 USD | 0.00 USD | `+58.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 441,310.00 USD | 3,050.00 USD | 0.00 USD | `+60.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 441,610.00 USD | 297.27 USD | 0.00 USD | `+64.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 450,140.00 USD | 8,530.00 USD | 0.00 USD | `+75.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 450,280.00 USD | 143.99 USD | 0.00 USD | `+76.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 450,460.00 USD | 177.05 USD | 0.00 USD | `+87.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 450,890.00 USD | 431.40 USD | 0.00 USD | `+90.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 451,110.00 USD | 220.77 USD | 0.00 USD | `+92.87%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.8030` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 9,970.00 USD | 5,760.00 USD | 10,410.00 USD |
| `7D` | `0.8050` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD |
| `7D` | `0.8070` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 12,160.00 USD | 4,660.00 USD | 16,650.00 USD |
| `7D` | `0.8090` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD |
| `7D` | `0.8110` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD |
| `7D` | `0.8130` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 14,060.00 USD | 2,970.00 USD | 9,350.00 USD |
| `7D` | `0.8150` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 61,120.00 USD | 7,590.00 USD | 19,500.00 USD |
| `7D` | `0.8170` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 10,780.00 USD | 8,770.00 USD | 9,670.00 USD |
| `7D` | `0.8190` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD |
| `7D` | `0.8210` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 7,510.00 USD | 3,290.00 USD | 10,030.00 USD |
| `7D` | `0.8230` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 29,430.00 USD | 5,100.00 USD | 13,220.00 USD |
| `7D` | `0.8250` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD |
| `7D` | `0.8270` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 4,320.00 USD | 5,770.00 USD | 616.76 USD |
| `7D` | `0.8290` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD |
| `7D` | `0.8310` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 9,280.00 USD | 1,660.00 USD | 2,450.00 USD |
| `7D` | `0.8330` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 16,220.00 USD | 11,360.00 USD | 77.95 USD |
| `7D` | `0.8350` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 19,490.00 USD | 0.00 USD | 2,290.00 USD |
| `1D` | `0.8370` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 18,140.00 USD | 2,530.00 USD | 20,310.00 USD |
| `7D` | `0.8370` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 15,240.00 USD | 1,480.00 USD | 0.00 USD |
| `1D` | `0.8390` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 1,740.00 USD | 745.84 USD | 2,010.00 USD |
| `7D` | `0.8390` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD |
| `1D` | `0.8410` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 1,470.00 USD | 2,040.00 USD | 1,780.00 USD |
| `7D` | `0.8410` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 270.00 USD | 3,280.00 USD | 0.00 USD |
| `1D` | `0.8430` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 4,670.00 USD | 6,880.00 USD | 1,150.00 USD |
| `7D` | `0.8430` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 11,320.00 USD | 3,840.00 USD | 4,060.00 USD |
| `1D` | `0.8450` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 2,530.00 USD | 8,430.00 USD | 1,150.00 USD |
| `7D` | `0.8450` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 1,980.00 USD | 404.64 USD | 474.61 USD |
| `1D` | `0.8470` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 24,200.00 USD | 1,110.00 USD | 1,120.00 USD |
| `7D` | `0.8470` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 7,900.00 USD | 5,280.00 USD | 2,390.00 USD |
| `1D` | `0.8490` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 6,900.00 USD | 5,020.00 USD | 7,940.00 USD |
| `7D` | `0.8490` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 22,370.00 USD | 9,610.00 USD | 0.00 USD |
| `1D` | `0.8510` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 13,560.00 USD | 4,140.00 USD | 16,720.00 USD |
| `7D` | `0.8510` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 14,280.00 USD | 991.53 USD | 21,470.00 USD |
| `1D` | `0.8530` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 4,680.00 USD | 3,830.00 USD | 5,510.00 USD |
| `7D` | `0.8530` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD |
| `1D` | `0.8550` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 18,270.00 USD | 3,040.00 USD | 5,090.00 USD |
| `7D` | `0.8550` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD |
| `1D` | `0.8570` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 989.11 USD | 1,720.00 USD | 6,150.00 USD |
| `7D` | `0.8570` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 3,540.00 USD | 944.22 USD | 8,450.00 USD |
| `1D` | `0.8590` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 6,870.00 USD | 10,640.00 USD | 6,420.00 USD |
| `7D` | `0.8590` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 3,730.00 USD | 0.00 USD | 1,560.00 USD |
| `1D` | `0.8610` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 8,320.00 USD | 855.53 USD | 16,460.00 USD |
| `7D` | `0.8610` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 9,960.00 USD | 3,660.00 USD | 35,340.00 USD |
| `1D` | `0.8630` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 39,330.00 USD | 12,290.00 USD | 2,010.00 USD |
| `7D` | `0.8630` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 758.91 USD | 2,910.00 USD | 1,280.00 USD |
| `1D` | `0.8650` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 17,640.00 USD | 2,110.00 USD | 1,790.00 USD |
| `7D` | `0.8650` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 47,860.00 USD | 18,930.00 USD | 184.85 USD |
| `1D` | `0.8670` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 12,000.00 USD | 10,090.00 USD | 1,110.00 USD |
| `7D` | `0.8670` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 13,660.00 USD | 3,720.00 USD | 12,140.00 USD |
| `1D` | `0.8690` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 42,010.00 USD | 3,780.00 USD | 29,400.00 USD |
| `7D` | `0.8690` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 160,750.00 USD | 13,110.00 USD | 46,230.00 USD |
| `1D` | `0.8710` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 42,290.00 USD | 24,900.00 USD | 28,630.00 USD |
| `7D` | `0.8710` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 7,370.00 USD | 23,340.00 USD | 13,110.00 USD |
| `1D` | `0.8730` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 54,500.00 USD | 21,510.00 USD | 25,960.00 USD |
| `7D` | `0.8730` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 0.00 USD | 8,170.00 USD | 295.31 USD |
| `1D` | `0.8750` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 37,070.00 USD | 6,900.00 USD | 17,890.00 USD |
| `7D` | `0.8750` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 0.00 USD | 6,380.00 USD | 8,950.00 USD |
| `1D` | `0.8770` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 10,690.00 USD | 152.79 USD | 0.00 USD |
| `7D` | `0.8770` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 1,390.00 USD | 0.00 USD | 30,820.00 USD |
| `1D` | `0.8790` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 0.00 USD | 40.93 USD | 50,910.00 USD |
| `7D` | `0.8790` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 873.30 USD | 5,580.00 USD | 53,860.00 USD |
| `1D` | `0.8810` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 13,820.00 USD | 5,210.00 USD | 2,430.00 USD |
| `7D` | `0.8810` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 1,830.00 USD | 240.78 USD | 0.00 USD |
| `1D` | `0.8830` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 656.20 USD | 5,570.00 USD | 0.00 USD |
| `7D` | `0.8830` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 2,320.00 USD | 10,140.00 USD | 11,710.00 USD |
| `1D` | `0.8850` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 5,680.00 USD | 34,880.00 USD | 11,180.00 USD |
| `7D` | `0.8850` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 0.00 USD | 5,800.00 USD | 3,970.00 USD |
| `1D` | `0.8870` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 68,700.00 USD | 16,710.00 USD | 32,750.00 USD |
| `7D` | `0.8870` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 271,870.00 USD | 22,320.00 USD | 81,590.00 USD |
| `1D` | `0.8890` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 69,610.00 USD | 40,830.00 USD | 4,860.00 USD |
| `7D` | `0.8890` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 54,380.00 USD | 73,890.00 USD | 13,880.00 USD |
| `1D` | `0.8910` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 2,770.00 USD | 38,730.00 USD | 20,080.00 USD |
| `7D` | `0.8910` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 75,300.00 USD | 22,240.00 USD | 34,270.00 USD |
| `1D` | `0.8930` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 57,080.00 USD | 23,480.00 USD | 37,920.00 USD |
| `7D` | `0.8930` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 62,870.00 USD | 23,560.00 USD | 9,170.00 USD |
| `1D` | `0.8950` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 6,700.00 USD | 15,420.00 USD | 8,160.00 USD |
| `7D` | `0.8950` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 7,120.00 USD | 37,670.00 USD | 57,420.00 USD |
| `1D` | `0.8970` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 8,300.00 USD | 27,310.00 USD | 19,060.00 USD |
| `7D` | `0.8970` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 2,140.00 USD | 11,010.00 USD | 56,560.00 USD |
| `1D` | `0.8990` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 3,650.00 USD | 24,130.00 USD | 4,220.00 USD |
| `7D` | `0.8990` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 0.00 USD | 34,220.00 USD | 0.00 USD |
| `1D` | `0.9010` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 5,490.00 USD | 28,480.00 USD | 7,410.00 USD |
| `7D` | `0.9010` | 995,960.00 USD | 0.00 USD | 995,960.00 USD | 0.00 USD | 51,270.00 USD | 0.00 USD |
| `1D` | `0.9030` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 10,610.00 USD | 19,460.00 USD | 20,600.00 USD |
| `7D` | `0.9030` | 944,690.00 USD | 0.00 USD | 944,690.00 USD | 0.00 USD | 27,770.00 USD | 23,930.00 USD |
| `1D` | `0.9050` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 23,790.00 USD | 18,920.00 USD | 22,050.00 USD |
| `7D` | `0.9050` | 892,990.00 USD | 0.00 USD | 892,990.00 USD | 0.00 USD | 3,840.00 USD | 0.00 USD |
| `1D` | `0.9070` | 975,680.00 USD | 0.00 USD | 975,680.00 USD | 36,650.00 USD | 8,370.00 USD | 33,510.00 USD |
| `7D` | `0.9070` | 889,150.00 USD | 0.00 USD | 889,150.00 USD | 23,910.00 USD | 0.00 USD | 42,040.00 USD |
| `1D` | `0.9090` | 897,140.00 USD | 0.00 USD | 897,140.00 USD | 7,100.00 USD | 9,080.00 USD | 239.84 USD |
| `1D` | `0.9110` | 880,730.00 USD | 0.00 USD | 880,730.00 USD | 25,560.00 USD | 2,850.00 USD | 2,080.00 USD |
| `1D` | `0.9130` | 850,240.00 USD | 0.00 USD | 850,240.00 USD | 17,080.00 USD | 9,480.00 USD | 22,310.00 USD |
| `7D` | `0.9130` | 823,200.00 USD | 0.00 USD | 823,200.00 USD | 0.00 USD | 0.00 USD | 20,720.00 USD |
| `1D` | `0.9150` | 801,360.00 USD | 0.00 USD | 801,360.00 USD | 11,120.00 USD | 17,780.00 USD | 24,660.00 USD |
| `7D` | `0.9150` | 802,480.00 USD | 0.00 USD | 802,480.00 USD | 0.00 USD | 12,890.00 USD | 16,130.00 USD |
| `1D` | `0.9170` | 747,800.00 USD | 0.00 USD | 747,800.00 USD | 7,300.00 USD | 16,660.00 USD | 15,090.00 USD |
| `7D` | `0.9170` | 773,460.00 USD | 0.00 USD | 773,460.00 USD | 0.00 USD | 0.00 USD | 33,180.00 USD |
| `1D` | `0.9190` | 708,750.00 USD | 0.00 USD | 708,750.00 USD | 9,900.00 USD | 15,280.00 USD | 16,980.00 USD |
| `7D` | `0.9190` | 740,280.00 USD | 0.00 USD | 740,280.00 USD | 0.00 USD | 4,870.00 USD | 0.00 USD |
| `1D` | `0.9210` | 666,600.00 USD | 0.00 USD | 666,600.00 USD | 12,850.00 USD | 7,480.00 USD | 10,770.00 USD |
| `7D` | `0.9210` | 735,410.00 USD | 0.00 USD | 735,410.00 USD | 0.00 USD | 7,760.00 USD | 3,970.00 USD |
| `1D` | `0.9230` | 635,490.00 USD | 0.00 USD | 635,490.00 USD | 9,860.00 USD | 10,950.00 USD | 21,700.00 USD |
| `7D` | `0.9230` | 723,680.00 USD | 0.00 USD | 723,680.00 USD | 294,370.00 USD | 22,800.00 USD | 26,680.00 USD |
| `1D` | `0.9250` | 592,980.00 USD | 0.00 USD | 592,980.00 USD | 108,890.00 USD | 74,100.00 USD | 62,530.00 USD |
| `7D` | `0.9250` | 379,830.00 USD | 0.00 USD | 379,830.00 USD | 0.00 USD | 52,780.00 USD | 84,070.00 USD |
| `1D` | `0.9270` | 347,460.00 USD | 0.00 USD | 347,460.00 USD | 39,920.00 USD | 7,040.00 USD | 73,810.00 USD |
| `7D` | `0.9270` | 242,980.00 USD | 0.00 USD | 242,980.00 USD | 44,020.00 USD | 11,800.00 USD | 0.00 USD |
| `1D` | `0.9290` | 226,690.00 USD | 0.00 USD | 226,690.00 USD | 80,950.00 USD | 20,440.00 USD | 38,560.00 USD |
| `7D` | `0.9290` | 187,160.00 USD | 0.00 USD | 187,160.00 USD | 0.00 USD | 12,750.00 USD | 1,600.00 USD |
| `1D` | `0.9310` | 86,740.00 USD | 0.00 USD | 86,740.00 USD | 0.00 USD | 7,130.00 USD | 5,410.00 USD |
| `1D` | `0.9330` | 74,200.00 USD | 0.00 USD | 74,200.00 USD | 3,720.00 USD | 6,140.00 USD | 26,590.00 USD |
| `7D` | `0.9330` | 172,810.00 USD | 0.00 USD | 172,810.00 USD | 37,450.00 USD | 0.00 USD | 31,370.00 USD |
| `1D` | `0.9350` | 37,740.00 USD | 0.00 USD | 37,740.00 USD | 36,510.00 USD | 197.86 USD | 0.00 USD |
| `7D` | `0.9350` | 104,000.00 USD | 0.00 USD | 104,000.00 USD | 0.00 USD | 0.00 USD | 19,600.00 USD |
| `1D` | `0.9370` | 1,030.00 USD | 0.00 USD | 1,030.00 USD | 0.00 USD | 182.01 USD | 852.35 USD |
| `7D` | `0.9370` | 84,400.00 USD | 0.00 USD | 84,400.00 USD | 16,340.00 USD | 19,540.00 USD | 48,530.00 USD |
| `7D` | `0.9380` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9390` | 1,650.00 USD | 1,650.00 USD | 0.00 USD | 1,340.00 USD | 309.30 USD | 0.00 USD |
| `1D` | `0.9390` | 3,300.00 USD | 3,300.00 USD | 0.00 USD | 1,340.00 USD | 309.30 USD | 0.00 USD |
| `7D` | `0.9390` | 74,160.00 USD | 74,160.00 USD | 0.00 USD | 39,250.00 USD | 0.00 USD | 34,910.00 USD |
| `1D` | `0.9410` | 4,210.00 USD | 4,210.00 USD | 0.00 USD | 673.54 USD | 239.40 USD | 0.00 USD |
| `7D` | `0.9410` | 237,210.00 USD | 237,210.00 USD | 0.00 USD | 161,930.00 USD | 1,130.00 USD | 0.00 USD |
| `1D` | `0.9430` | 5,670.00 USD | 5,670.00 USD | 0.00 USD | 1,230.00 USD | 224.96 USD | 0.00 USD |
| `7D` | `0.9450` | 261,500.00 USD | 261,500.00 USD | 0.00 USD | 0.00 USD | 20,890.00 USD | 3,390.00 USD |
| `1D` | `0.9470` | 6,190.00 USD | 6,190.00 USD | 0.00 USD | 0.00 USD | 199.60 USD | 319.22 USD |
| `7D` | `0.9470` | 348,010.00 USD | 348,010.00 USD | 0.00 USD | 3,540.00 USD | 6,380.00 USD | 76,590.00 USD |
| `1D` | `0.9490` | 84,260.00 USD | 84,260.00 USD | 0.00 USD | 78,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9490` | 431,950.00 USD | 431,950.00 USD | 0.00 USD | 2,770.00 USD | 10,340.00 USD | 70,820.00 USD |
| `1D` | `0.9510` | 95,250.00 USD | 95,250.00 USD | 0.00 USD | 5,190.00 USD | 813.18 USD | 4,990.00 USD |
| `7D` | `0.9510` | 723,340.00 USD | 723,340.00 USD | 0.00 USD | 258,650.00 USD | 28,180.00 USD | 4,570.00 USD |
| `1D` | `0.9530` | 116,880.00 USD | 116,880.00 USD | 0.00 USD | 7,370.00 USD | 8,490.00 USD | 5,770.00 USD |
| `7D` | `0.9530` | 744,400.00 USD | 744,400.00 USD | 0.00 USD | 0.00 USD | 20,610.00 USD | 447.96 USD |
| `1D` | `0.9550` | 189,870.00 USD | 189,870.00 USD | 0.00 USD | 25,300.00 USD | 39,260.00 USD | 8,440.00 USD |
| `7D` | `0.9550` | 764,130.00 USD | 764,130.00 USD | 0.00 USD | 0.00 USD | 19,730.00 USD | 0.00 USD |
| `1D` | `0.9570` | 226,470.00 USD | 226,470.00 USD | 0.00 USD | 13,680.00 USD | 13,280.00 USD | 9,630.00 USD |
| `7D` | `0.9570` | 782,160.00 USD | 782,160.00 USD | 0.00 USD | 1,910.00 USD | 15,160.00 USD | 957.94 USD |
| `1D` | `0.9590` | 256,690.00 USD | 256,690.00 USD | 0.00 USD | 14,060.00 USD | 7,480.00 USD | 8,680.00 USD |
| `7D` | `0.9590` | 803,230.00 USD | 803,230.00 USD | 0.00 USD | 1,980.00 USD | 18,220.00 USD | 866.69 USD |
| `1D` | `0.9610` | 321,020.00 USD | 321,020.00 USD | 0.00 USD | 18,020.00 USD | 15,760.00 USD | 30,550.00 USD |
| `7D` | `0.9610` | 851,410.00 USD | 851,410.00 USD | 0.00 USD | 24,370.00 USD | 22,800.00 USD | 1,010.00 USD |
| `1D` | `0.9630` | 519,040.00 USD | 519,040.00 USD | 0.00 USD | 110,950.00 USD | 41,450.00 USD | 45,610.00 USD |
| `7D` | `0.9630` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 56,160.00 USD | 31,820.00 USD | 84,550.00 USD |
| `1D` | `0.9650` | 660,420.00 USD | 660,420.00 USD | 0.00 USD | 29,080.00 USD | 33,020.00 USD | 79,280.00 USD |
| `7D` | `0.9650` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 97,600.00 USD | 0.00 USD | 12,330.00 USD |
| `1D` | `0.9670` | 756,850.00 USD | 756,850.00 USD | 0.00 USD | 53,970.00 USD | 16,730.00 USD | 25,720.00 USD |
| `7D` | `0.9670` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 40,070.00 USD | 5,550.00 USD | 0.00 USD |
| `1D` | `0.9690` | 798,180.00 USD | 798,180.00 USD | 0.00 USD | 14,860.00 USD | 14,610.00 USD | 11,850.00 USD |
| `7D` | `0.9690` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 21,100.00 USD | 30,500.00 USD |
| `1D` | `0.9710` | 911,370.00 USD | 911,370.00 USD | 0.00 USD | 15,040.00 USD | 19,120.00 USD | 79,040.00 USD |
| `7D` | `0.9710` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 24,440.00 USD | 31,590.00 USD |
| `1D` | `0.9730` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 37,900.00 USD | 14,900.00 USD | 40,280.00 USD |
| `7D` | `0.9730` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 2,910.00 USD | 9,290.00 USD | 27,110.00 USD |
| `1D` | `0.9750` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 29,660.00 USD | 13,550.00 USD | 34,760.00 USD |
| `7D` | `0.9750` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 2,090.00 USD | 17,230.00 USD | 51,650.00 USD |
| `1D` | `0.9770` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 78,910.00 USD | 16,960.00 USD | 13,160.00 USD |
| `7D` | `0.9770` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 49,900.00 USD | 18,660.00 USD | 31,410.00 USD |
| `1D` | `0.9790` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 38,220.00 USD | 13,210.00 USD | 28,690.00 USD |
| `7D` | `0.9790` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 15,280.00 USD | 85,420.00 USD |
| `1D` | `0.9810` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 21,440.00 USD | 13,940.00 USD | 28,550.00 USD |
| `7D` | `0.9810` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 540.00 USD | 4,020.00 USD | 119,460.00 USD |
| `1D` | `0.9830` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 33,340.00 USD | 27,220.00 USD | 55,550.00 USD |
| `7D` | `0.9830` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 124,720.00 USD | 15,810.00 USD | 94,290.00 USD |
| `1D` | `0.9850` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 47,310.00 USD | 8,800.00 USD | 18,830.00 USD |
| `7D` | `0.9850` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 211.77 USD | 22,300.00 USD |
| `1D` | `0.9870` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 14,930.00 USD | 6,470.00 USD | 22,410.00 USD |
| `7D` | `0.9870` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 67,950.00 USD |
| `1D` | `0.9890` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 27,890.00 USD | 3,780.00 USD | 30,190.00 USD |
| `7D` | `0.9890` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `0.9910` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 60,130.00 USD | 5,890.00 USD | 45,430.00 USD |
| `7D` | `0.9910` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 3,700.00 USD | 800.44 USD | 35,270.00 USD |
| `1D` | `0.9930` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 16,320.00 USD | 5,130.00 USD | 8,200.00 USD |
| `7D` | `0.9930` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 36,000.00 USD |
| `1D` | `0.9950` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 29,250.00 USD | 2,120.00 USD | 7,140.00 USD |
| `7D` | `0.9950` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 63,060.00 USD | 5,380.00 USD | 58,050.00 USD |
| `1D` | `0.9970` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 46,950.00 USD | 1,870.00 USD | 13,030.00 USD |
| `7D` | `0.9970` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 95,130.00 USD | 253.35 USD | 4,670.00 USD |
| `1D` | `0.9990` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 35,340.00 USD | 17,910.00 USD | 10,720.00 USD |
| `7D` | `0.9990` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 6,490.00 USD | 462.12 USD |
| `1D` | `1.00` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 45,050.00 USD | 10,790.00 USD | 13,500.00 USD |
| `7D` | `1.00` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.00` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 12,580.00 USD | 9,310.00 USD | 6,140.00 USD |
| `7D` | `1.00` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 107,670.00 USD | 21,850.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 54,780.00 USD | 5,520.00 USD | 5,820.00 USD |
| `7D` | `1.00` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 32,430.00 USD | 3,970.00 USD | 12,730.00 USD |
| `1D` | `1.01` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 50,600.00 USD | 11,770.00 USD | 38,280.00 USD |
| `7D` | `1.01` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 35,710.00 USD | 240.78 USD | 29,210.00 USD |
| `1D` | `1.01` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 30,870.00 USD | 13,790.00 USD | 7,610.00 USD |
| `7D` | `1.01` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD |
| `1D` | `1.01` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 9,660.00 USD | 17,670.00 USD | 265.91 USD |
| `7D` | `1.01` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 20,090.00 USD | 17,980.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 10,450.00 USD | 1,540.00 USD | 3,750.00 USD |
| `7D` | `1.01` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD |
| `1D` | `1.01` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 14,310.00 USD | 18,100.00 USD | 14,630.00 USD |
| `7D` | `1.01` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 26,510.00 USD | 7,420.00 USD |
| `1D` | `1.02` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 3,990.00 USD | 2,940.00 USD | 12,700.00 USD |
| `7D` | `1.02` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD |
| `1D` | `1.02` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 55,630.00 USD | 4,860.00 USD | 10,650.00 USD |
| `7D` | `1.02` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 17,960.00 USD | 83,360.00 USD | 11,810.00 USD |
| `1D` | `1.02` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 6,670.00 USD | 7,410.00 USD | 21,020.00 USD |
| `7D` | `1.02` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 61,450.00 USD | 32,840.00 USD | 68,370.00 USD |
| `1D` | `1.02` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 40,460.00 USD | 18,460.00 USD | 29,940.00 USD |
| `7D` | `1.02` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 82,230.00 USD | 86,210.00 USD | 146,060.00 USD |
| `1D` | `1.02` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 39,730.00 USD | 5,800.00 USD | 17,080.00 USD |
| `7D` | `1.02` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 28,320.00 USD | 48,490.00 USD | 37,230.00 USD |
| `1D` | `1.03` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 15,190.00 USD | 11,870.00 USD | 8,070.00 USD |
| `7D` | `1.03` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 161,070.00 USD | 129,470.00 USD | 25,260.00 USD |
| `1D` | `1.03` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 11,620.00 USD | 13,840.00 USD | 15,740.00 USD |
| `7D` | `1.03` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD |
| `1D` | `1.03` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 65,750.00 USD | 8,920.00 USD | 32,850.00 USD |
| `7D` | `1.03` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD |
| `1D` | `1.03` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 12,420.00 USD | 2,140.00 USD | 17,290.00 USD |
| `7D` | `1.03` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD |
| `1D` | `1.03` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 11,210.00 USD | 15,190.00 USD | 8,200.00 USD |
| `7D` | `1.03` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 259,060.00 USD | 11,850.00 USD | 43,700.00 USD |
| `1D` | `1.04` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 44,200.00 USD | 6,370.00 USD | 11,940.00 USD |
| `7D` | `1.04` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 193,150.00 USD | 3,330.00 USD | 109,460.00 USD |
| `1D` | `1.04` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 7,640.00 USD | 5,430.00 USD | 5,210.00 USD |
| `7D` | `1.04` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 239,580.00 USD | 9,010.00 USD | 134,440.00 USD |
| `1D` | `1.04` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 4,700.00 USD | 2,450.00 USD | 12,490.00 USD |
| `7D` | `1.04` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 285,690.00 USD | 2,090.00 USD | 159,500.00 USD |
| `7D` | `1.04` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD |
| `7D` | `1.04` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD |
| `7D` | `1.05` | 6,930,000.00 USD | 6,930,000.00 USD | 0.00 USD | 178,890.00 USD | 96,370.00 USD | 244,850.00 USD |
| `7D` | `1.05` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 108,060.00 USD | 13,780.00 USD | 77,620.00 USD |
| `7D` | `1.05` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 173,140.00 USD | 43,690.00 USD | 96,730.00 USD |
| `7D` | `1.05` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 68,010.00 USD | 58,070.00 USD | 74,380.00 USD |
| `7D` | `1.05` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 121,450.00 USD | 33,860.00 USD | 72,330.00 USD |
| `7D` | `1.06` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 218,860.00 USD | 70,160.00 USD | 106,380.00 USD |
| `7D` | `1.06` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 239,650.00 USD | 74,380.00 USD | 145,170.00 USD |
| `7D` | `1.06` | 8,980,000.00 USD | 8,980,000.00 USD | 0.00 USD | 129,140.00 USD | 55,290.00 USD | 76,020.00 USD |
| `7D` | `1.06` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 132,250.00 USD | 46,140.00 USD | 38,790.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `172.99M` | Total OI Tokens: `184,461,652.9 DOT`
  * 1h OI Change: `+0.37%` | 4h OI Change: `-2.15%` | 24h OI Change: `-16.84%`
  * Exchange Breakdown: Binance=`33.57M` | Bybit=`22.07M` | OKX=`10.21M` | Hyperliquid=`5.84M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `4.22K` | Last 24h: `6.26K` | Last 3d: `-7.35K` | Last 7d: `-25.50K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0050%` |
| **USDT Bybit** | `0.0092%` | **USDT KuCoin** | `-0.0115%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0057%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `47.50%` | `52.50%` | `0.90` | 4,310,000.00 USD |
| `15M` | `Binance` | `50.71%` | `49.29%` | `1.03` | 1,570,000.00 USD |
| `15M` | `OKX` | `31.78%` | `68.22%` | `0.47` | 578,620.00 USD |
| `15M` | `Bybit` | `38.27%` | `61.73%` | `0.62` | 351,470.00 USD |
| `15M` | `KuCoin` | `49.19%` | `50.81%` | `0.97` | 59,930.00 USD |
| `15M` | `Gate` | `54.11%` | `45.89%` | `1.18` | 41,050.00 USD |
| `15M` | `Bitget` | `26.09%` | `73.91%` | `0.35` | 133,880.00 USD |
| `15M` | `BingX` | `29.24%` | `70.76%` | `0.41` | 162,090.00 USD |
| `15M` | `MEXC` | `46.84%` | `53.16%` | `0.88` | 795,530.00 USD |
| `15M` | `Bitunix` | `46.57%` | `53.43%` | `0.87` | 192,180.00 USD |
| `15M` | `Hyperliquid` | `27.93%` | `72.07%` | `0.39` | 45,640.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.81%` | `53.19%` | `0.88` | 28,320.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `94.18%` | `5.82%` | `16.18` | 304,870.00 USD |
| `15M` | `HTX` | `84.53%` | `15.47%` | `5.46` | 241.74 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `49.45%` | `50.55%` | `0.98` | 35,290.00 USD |
| `15M` | `Aster` | `38.3%` | `61.7%` | `0.62` | 5,970.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `62.73%` | `37.27%` | `1.68` | 6,190.00 USD |
| `15M` | `Whale Positions` | `50.71%` | `49.29%` | `1.03` | 1,570,000.00 USD |
| `15M` | `Global Accounts` | `47.50%` | `52.50%` | `0.90` | 4,310,000.00 USD |
| `1H` | `DOT` | `54.08%` | `45.92%` | `1.18` | 27,030,000.00 USD |
| `1H` | `Binance` | `52.63%` | `47.37%` | `1.11` | 9,310,000.00 USD |
| `1H` | `OKX` | `48.72%` | `51.28%` | `0.95` | 4,850,000.00 USD |
| `1H` | `Bybit` | `49.86%` | `50.14%` | `0.99` | 2,250,000.00 USD |
| `1H` | `KuCoin` | `62.04%` | `37.96%` | `1.63` | 902,560.00 USD |
| `1H` | `Gate` | `51.72%` | `48.28%` | `1.07` | 446,720.00 USD |
| `1H` | `Bitget` | `56.3%` | `43.7%` | `1.29` | 809,540.00 USD |
| `1H` | `BingX` | `51.87%` | `48.13%` | `1.08` | 1,160,000.00 USD |
| `1H` | `MEXC` | `57.99%` | `42.01%` | `1.38` | 3,410,000.00 USD |
| `1H` | `Bitunix` | `50.37%` | `49.63%` | `1.01` | 899,020.00 USD |
| `1H` | `Hyperliquid` | `31.55%` | `68.45%` | `0.46` | 1,170,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.95%` | `46.05%` | `1.17` | 155,640.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `96.89%` | `3.11%` | `31.15` | 1,170,000.00 USD |
| `1H` | `HTX` | `52.33%` | `47.67%` | `1.10` | 13,700.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `74.22%` | `25.78%` | `2.88` | 444,000.00 USD |
| `1H` | `Aster` | `70.61%` | `29.39%` | `2.40` | 21,140.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `78.25%` | `21.75%` | `3.60` | 27,770.00 USD |
| `1H` | `Whale Positions` | `52.63%` | `47.37%` | `1.11` | 9,310,000.00 USD |
| `1H` | `Global Accounts` | `54.08%` | `45.92%` | `1.18` | 27,030,000.00 USD |
| `4H` | `DOT` | `49.39%` | `50.61%` | `0.98` | 99,150,000.00 USD |
| `4H` | `Binance` | `48.08%` | `51.92%` | `0.93` | 36,630,000.00 USD |
| `4H` | `OKX` | `45.95%` | `54.05%` | `0.85` | 14,800,000.00 USD |
| `4H` | `Bybit` | `46.96%` | `53.04%` | `0.89` | 7,790,000.00 USD |
| `4H` | `KuCoin` | `57.1%` | `42.9%` | `1.33` | 1,890,000.00 USD |
| `4H` | `Gate` | `57.99%` | `42.01%` | `1.38` | 2,520,000.00 USD |
| `4H` | `Bitget` | `49.16%` | `50.84%` | `0.97` | 3,920,000.00 USD |
| `4H` | `BingX` | `27.49%` | `72.51%` | `0.38` | 5,720,000.00 USD |
| `4H` | `MEXC` | `51.15%` | `48.85%` | `1.05` | 13,780,000.00 USD |
| `4H` | `Bitunix` | `49.84%` | `50.16%` | `0.99` | 3,270,000.00 USD |
| `4H` | `Hyperliquid` | `33.28%` | `66.72%` | `0.50` | 2,130,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `54.87%` | `45.13%` | `1.22` | 1,050,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `93.27%` | `6.73%` | `13.86` | 4,590,000.00 USD |
| `4H` | `HTX` | `56.54%` | `43.46%` | `1.30` | 174,930.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `63.14%` | `36.86%` | `1.71` | 716,560.00 USD |
| `4H` | `Aster` | `40.86%` | `59.14%` | `0.69` | 87,120.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `38.1%` | `61.9%` | `0.62` | 86,660.00 USD |
| `4H` | `Whale Positions` | `48.08%` | `51.92%` | `0.93` | 36,630,000.00 USD |
| `4H` | `Global Accounts` | `49.39%` | `50.61%` | `0.98` | 99,150,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.9349` | `0.9360` | `0.9349` | `0.9390` | `0.9338` | 565,103.94 USD | 170,366.16 USD | 394,737.78 USD | -224,371.62 USD | `-39.70%` | `1B / 22S` |
| `5:00 UTC` | `0.9357` | `0.9351` | `0.9357` | `0.9366` | `0.9332` | 272,828.10 USD | 122,126.72 USD | 150,701.37 USD | -28,574.65 USD | `-10.47%` | `1B / 6S` |
| `0:00 UTC` | `0.9343` | `0.9337` | `0.9343` | `0.9365` | `0.9315` | 323,640.65 USD | 113,112.66 USD | 210,527.99 USD | -97,415.33 USD | `-30.10%` | `2B / 14S` |
| `5:00 UTC` | `0.9312` | `0.9319` | `0.9312` | `0.9351` | `0.9293` | 338,159.00 USD | 113,706.78 USD | 224,452.22 USD | -110,745.44 USD | `-32.75%` | `4B / 15S` |
| `0:00 UTC` | `0.9326` | `0.9327` | `0.9326` | `0.9345` | `0.9304` | 383,267.52 USD | 169,541.73 USD | 213,725.79 USD | -44,184.07 USD | `-11.53%` | `4B / 8S` |
| `5:00 UTC` | `0.9325` | `0.9329` | `0.9325` | `0.9366` | `0.9303` | 250,363.19 USD | 100,290.83 USD | 150,072.35 USD | -49,781.52 USD | `-19.88%` | `3B / 19S` |
| `0:00 UTC` | `0.9365` | `0.9367` | `0.9365` | `0.9399` | `0.9325` | 603,897.34 USD | 304,683.07 USD | 299,214.28 USD | 5,468.79 USD | `+0.91%` | `10B / 15S` |
| `5:00 UTC` | `0.9425` | `0.9395` | `0.9425` | `0.9430` | `0.9366` | 362,865.52 USD | 187,760.19 USD | 175,105.33 USD | 12,654.86 USD | `+3.49%` | `12B / 9S` |
| `0:00 UTC` | `0.9434` | `0.9412` | `0.9434` | `0.9443` | `0.9385` | 364,164.72 USD | 198,094.67 USD | 166,070.05 USD | 32,024.63 USD | `+8.79%` | `12B / 5S` |
| `5:00 UTC` | `0.9401` | `0.9381` | `0.9401` | `0.9409` | `0.9361` | 110,075.50 USD | 44,521.04 USD | 65,554.46 USD | -21,033.42 USD | `-19.11%` | `4B / 17S` |

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
| `5m` | 20,430.00 USD | -23,180.00 USD | **`DISTRIBUTION`** |
| `15m` | -17,790.00 USD | -46,740.00 USD | **`DISTRIBUTION`** |
| `30m` | -13,670.00 USD | 287,070.00 USD | **`ACCUMULATION`** |
| `1h` | -32,860.00 USD | 265,890.00 USD | **`ACCUMULATION`** |
| `2h` | -29,490.00 USD | -145,190.00 USD | **`DISTRIBUTION`** |
| `4h` | -235,800.00 USD | -1,340,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -278,660.00 USD | -1,830,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -214,570.00 USD | -1,630,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -572,110.00 USD | -1,030,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,360,000.00 USD | -8,830,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,990,000.00 USD | -23,490,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,770,000.00 USD | -78,340,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+20.43K` | 15m=`-17.79K` | 1h=`-32.86K` | 24h=`-1.36M`
* Futures Capital Netflows: 5m=`-23.18K` | 15m=`-46.74K` | 1h=`+265.89K` | 24h=`-8.83M`
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
  * `2026-10-30 16:36:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:03 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:49:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.9010` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.8632` (Risk Distance: `0.0400` pts)
  * +2.5R Take Profit: `1.00`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9447` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9825` (Risk Distance: `0.0400` pts)
  * +2.5R Take Profit: `0.8447`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9445`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
