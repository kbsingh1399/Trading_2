# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 11:11:09 IST` (`2026-10-30 05:41:09 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9410` | **Live Ask Quote**: `0.9610` | **Mid Price**: `0.9510`
- **Spread Points**: `20.00` | **Spread BPS**: `210.30 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.9510` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.9577` | Lower -3.00σ Band: `0.9443`
  * Upper +2.51σ Band: `0.9562` | Lower -2.51σ Band: `0.9458`
  * Upper +2.01σ Band: `0.9550` | Lower -2.01σ Band: `0.9470`
  * Upper +2.00σ Band: `0.9548` | Lower -2.00σ Band: `0.9472`
  * Upper +1.28σ Band: `0.9537` | Lower -1.28σ Band: `0.9483`
  * Upper +1.00σ Band: `0.9529` | Lower -1.00σ Band: `0.9491`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9510` | EMA-20=`0.9510` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9510` (Slope: `+0.0000`) | EMA-100=`0.9510`
  * Institutional Anchors: EMA-144=`0.9510` | EMA-200=`0.9510` (Slope: `+0.0000`) | EMA-233=`0.9510`
- **Range Boundaries**: 24H High=`0.9605` | 24H Low=`0.9415` | Weekly High=`0.9700` | Weekly Low=`0.9320`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9253` (Distance: `+2.72%`)
  * Point of Control (POC) = `0.9119` (Distance: `+4.24%`)
  * Value Area Low (VAL) = `0.8919` (Distance: `+6.57%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.02` | Weekly POC=`0.9945` | Weekly VAL=`0.9713`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9330` | Low=`0.8570`
  * London Session (08:00-16:00 UTC): High=`0.9450` | Low=`0.9290`
  * New York Session (13:00-21:00 UTC): High=`0.9567` | Low=`0.9453`
  * Initial Balance (First Hour): IB High=`0.9450` | IB Low=`0.9290`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9472` - `0.9548`
  * Optimal Trade Entry (OTE 0.705): `0.9529`
  * Structural Invalidation Anchor (0.786): `0.9586`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9529` | `0.9539` | `0.9503` | `0.9530` | `193,228` | 184,048.92 USD | -30,502.20 USD | `-16.57%` | -3,772,443.89 USD | `-0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.9529` | `0.9544` | `0.9510` | `0.9519` | `181,976` | 173,389.33 USD | -68,670.56 USD | `-39.60%` | -3,841,114.45 USD | `-0.96` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.9520` | `0.9539` | `0.9510` | `0.9519` | `114,425` | 109,008.84 USD | -16,517.22 USD | `-15.15%` | -3,857,631.67 USD | `-0.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9428` | `0.9570` | `0.9410` | `0.9497` | `1,216,863` | 1,155,581.71 USD | -251,680.92 USD | `-21.78%` | -3,622,267.34 USD | `-0.58` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.9496` | `0.9544` | `0.9487` | `0.9519` | `593,394` | 564,921.36 USD | -145,185.92 USD | `-25.70%` | -3,767,453.26 USD | `-0.50` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.9520` | `0.9539` | `0.9510` | `0.9519` | `114,425` | 109,008.84 USD | -16,517.22 USD | `-15.15%` | -3,783,970.48 USD | `-0.25` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.9176` | `0.9341` | `0.9170` | `0.9318` | `3,070,214` | 2,839,814.60 USD | -92,909.79 USD | `-3.27%` | -3,396,468.88 USD | `+0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9318` | `0.9453` | `0.9263` | `0.9427` | `3,017,884` | 2,825,399.84 USD | 74,707.92 USD | `+2.64%` | -3,321,760.96 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9428` | `0.9570` | `0.9410` | `0.9521` | `1,930,929` | 1,835,458.37 USD | -407,648.33 USD | `-22.21%` | -3,729,409.29 USD | `-0.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,414,306.57 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,007,919.25 USD | `+1.11` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9570` | `0.9263` | `0.9519` | `4,942,566` | 4,654,911.75 USD | -338,676.14 USD | `-7.28%` | -4,346,595.38 USD | `+0.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | -92,512.40 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -889,577.85 USD | `-1.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,414,306.57 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,007,919.25 USD | `+1.11` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9570` | `0.9263` | `0.9519` | `4,942,566` | 4,654,911.75 USD | -338,676.14 USD | `-7.28%` | -4,346,595.38 USD | `+0.21` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`0.9510`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:04:06 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9691` | 5,115.20 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale BUY: 5.12K USD at 0.9691 USD [API] | `2026-10-29 03:19:50` |


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
| `Live` | `Long Liquidation` | `0.2255` | 112.75 USD | 466,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3595` | 794.14 USD | 466,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4195` | 2,800.00 USD | 465,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4215` | 2,400.00 USD | 463,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4645` | 315.16 USD | 460,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4675` | 146.70 USD | 460,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4705` | 2,590.00 USD | 460,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4755` | 1,240.00 USD | 457,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5065` | 3,290.00 USD | 456,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5325` | 532.50 USD | 453,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5455` | 142.98 USD | 452,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 14,600.00 USD | 452,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 803.17 USD | 437,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5815` | 233.01 USD | 437,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 683.51 USD | 436,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 137.53 USD | 436,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6055` | 1,480.00 USD | 436,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6065` | 1,800.00 USD | 434,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 105.96 USD | 432,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 147.48 USD | 432,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 757.80 USD | 432,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 106.00 USD | 431,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 507.86 USD | 431,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 2,090.00 USD | 431,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 20,270.00 USD | 429,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 4,230.00 USD | 408,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 202.47 USD | 404,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6555` | 521.19 USD | 404,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 149.44 USD | 403,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 63,890.00 USD | 403,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 85,110.00 USD | 339,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 512.97 USD | 254,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6915` | 19,800.00 USD | 254,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6935` | 154.93 USD | 234,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 322.62 USD | 234,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7005` | 1,140.00 USD | 233,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 988.87 USD | 232,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7215` | 1,580.00 USD | 231,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 397.93 USD | 230,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 291.18 USD | 229,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 2,300.00 USD | 229,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,140.00 USD | 227,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 283.30 USD | 226,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 331.18 USD | 225,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7545` | 1,400.00 USD | 225,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 8,990.00 USD | 224,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7635` | 308.00 USD | 215,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7645` | 54,280.00 USD | 214,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7700` | 4,900,000.00 USD | 4,900,000.00 USD | 5,060.00 USD | 1,600.00 USD | 5,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7720` | 4,880,000.00 USD | 4,880,000.00 USD | 4,990.00 USD | 0.00 USD | 2,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7725` | 3,840.00 USD | 160,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7740` | 4,880,000.00 USD | 4,880,000.00 USD | 5,450.00 USD | 0.00 USD | 3,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7760` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 147.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7775` | 2,490.00 USD | 156,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7780` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 3,100.00 USD | 53.43 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7795` | 272.83 USD | 154,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7800` | 4,870,000.00 USD | 4,870,000.00 USD | 436.65 USD | 25.30 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7820` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 1,920.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7840` | 4,860,000.00 USD | 4,860,000.00 USD | 227.10 USD | 1,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7860` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 2,250.00 USD | 365.01 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7865` | 292.03 USD | 153,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7880` | 4,860,000.00 USD | 4,860,000.00 USD | 5,690.00 USD | 2,050.00 USD | 723.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7900` | 4,850,000.00 USD | 4,850,000.00 USD | 6,940.00 USD | 2,650.00 USD | 4,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 277.39 USD | 153,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7920` | 4,840,000.00 USD | 4,840,000.00 USD | 12,590.00 USD | 2,180.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7940` | 4,810,000.00 USD | 4,810,000.00 USD | 15,680.00 USD | 2,500.00 USD | 13,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7960` | 4,780,000.00 USD | 4,780,000.00 USD | 4,520.00 USD | 7,120.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7980` | 4,760,000.00 USD | 4,760,000.00 USD | 16,210.00 USD | 3,000.00 USD | 14,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8000` | 4,730,000.00 USD | 4,730,000.00 USD | 10,100.00 USD | 5,540.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8020` | 4,710,000.00 USD | 4,710,000.00 USD | 8,990.00 USD | 4,460.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8040` | 4,690,000.00 USD | 4,690,000.00 USD | 5,500.00 USD | 2,170.00 USD | 940.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8060` | 4,680,000.00 USD | 4,680,000.00 USD | 16,390.00 USD | 10,990.00 USD | 10,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8080` | 4,640,000.00 USD | 4,640,000.00 USD | 1,570.00 USD | 1,230.00 USD | 10,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8100` | 4,630,000.00 USD | 4,630,000.00 USD | 2,890.00 USD | 2,010.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8120` | 4,620,000.00 USD | 4,620,000.00 USD | 15,720.00 USD | 3,030.00 USD | 9,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 153,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8140` | 4,590,000.00 USD | 4,590,000.00 USD | 32,880.00 USD | 6,050.00 USD | 15,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8160` | 4,540,000.00 USD | 4,540,000.00 USD | 38,200.00 USD | 10,180.00 USD | 6,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8180` | 4,480,000.00 USD | 4,480,000.00 USD | 12,550.00 USD | 2,560.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8200` | 4,460,000.00 USD | 4,460,000.00 USD | 1,740.00 USD | 1,570.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 152,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8220` | 4,450,000.00 USD | 4,450,000.00 USD | 20,390.00 USD | 6,820.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 749.96 USD | 150,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8240` | 4,410,000.00 USD | 4,410,000.00 USD | 23,160.00 USD | 93.73 USD | 11,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8260` | 4,380,000.00 USD | 4,380,000.00 USD | 5,220.00 USD | 3,490.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8280` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 3,910.00 USD | 1,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8300` | 4,360,000.00 USD | 4,360,000.00 USD | 9,280.00 USD | 4,780.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8320` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 401.80 USD | 77.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8330` | 3,300,000.00 USD | 3,300,000.00 USD | 28,220.00 USD | 3,030.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8340` | 4,350,000.00 USD | 4,350,000.00 USD | 35,710.00 USD | 10,960.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8350` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 4,750.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8360` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 844.23 USD | 311.26 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 149,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8370` | 3,250,000.00 USD | 3,250,000.00 USD | 18,030.00 USD | 2,360.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8380` | 4,300,000.00 USD | 4,300,000.00 USD | 15,240.00 USD | 633.60 USD | 539.92 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8390` | 3,220,000.00 USD | 3,220,000.00 USD | 671.95 USD | 745.84 USD | 1,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8400` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 798.38 USD | 8,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8410` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 449.73 USD | 933.95 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,570.00 USD | 149,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8420` | 4,270,000.00 USD | 4,270,000.00 USD | 6,400.00 USD | 4,650.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8430` | 3,210,000.00 USD | 3,210,000.00 USD | 1,590.00 USD | 4,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8435` | 751.39 USD | 148,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8440` | 4,260,000.00 USD | 4,260,000.00 USD | 7,170.00 USD | 24.80 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8450` | 3,210,000.00 USD | 3,210,000.00 USD | 2,200.00 USD | 6,340.00 USD | 25.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8460` | 4,250,000.00 USD | 4,250,000.00 USD | 2,560.00 USD | 427.62 USD | 2,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8470` | 3,200,000.00 USD | 3,200,000.00 USD | 21,360.00 USD | 417.76 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8480` | 4,240,000.00 USD | 4,240,000.00 USD | 26,310.00 USD | 10,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8490` | 3,180,000.00 USD | 3,180,000.00 USD | 2,500.00 USD | 142.65 USD | 537.83 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 147,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8500` | 4,210,000.00 USD | 4,210,000.00 USD | 2,050.00 USD | 477.96 USD | 4,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8510` | 3,170,000.00 USD | 3,170,000.00 USD | 6,130.00 USD | 2,240.00 USD | 7,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8515` | 2,700.00 USD | 146,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8520` | 4,200,000.00 USD | 4,200,000.00 USD | 5,900.00 USD | 669.43 USD | 226.67 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8530` | 3,160,000.00 USD | 3,160,000.00 USD | 1,410.00 USD | 2,440.00 USD | 4,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8540` | 4,190,000.00 USD | 4,190,000.00 USD | 254.55 USD | 2,660.00 USD | 5,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8550` | 3,150,000.00 USD | 3,150,000.00 USD | 17,960.00 USD | 2,470.00 USD | 4,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8560` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 842.92 USD | 2,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8570` | 3,120,000.00 USD | 3,120,000.00 USD | 739.96 USD | 445.99 USD | 2,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 143,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8580` | 4,180,000.00 USD | 4,180,000.00 USD | 3,540.00 USD | 101.30 USD | 1,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8590` | 3,120,000.00 USD | 3,120,000.00 USD | 5,620.00 USD | 10,610.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8600` | 4,180,000.00 USD | 4,180,000.00 USD | 5,820.00 USD | 211.77 USD | 383.26 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8605` | 25,780.00 USD | 142,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8610` | 3,100,000.00 USD | 3,100,000.00 USD | 7,980.00 USD | 855.53 USD | 13,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8615` | 181.17 USD | 116,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8620` | 4,170,000.00 USD | 4,170,000.00 USD | 7,670.00 USD | 6,050.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8630` | 3,080,000.00 USD | 3,080,000.00 USD | 39,330.00 USD | 12,290.00 USD | 2,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 116,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8640` | 4,130,000.00 USD | 4,130,000.00 USD | 4,820.00 USD | 321.30 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 116,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8650` | 3,030,000.00 USD | 3,030,000.00 USD | 17,640.00 USD | 2,110.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8660` | 4,120,000.00 USD | 4,120,000.00 USD | 45,020.00 USD | 19,050.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,390.00 USD | 116,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8670` | 3,000,000.00 USD | 3,000,000.00 USD | 11,890.00 USD | 10,090.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8680` | 4,060,000.00 USD | 4,060,000.00 USD | 92,530.00 USD | 14,760.00 USD | 50,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8690` | 2,980,000.00 USD | 2,980,000.00 USD | 41,960.00 USD | 3,780.00 USD | 29,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 12,590.00 USD | 114,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8700` | 3,900,000.00 USD | 3,900,000.00 USD | 81,840.00 USD | 9,460.00 USD | 7,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8710` | 2,910,000.00 USD | 2,910,000.00 USD | 42,250.00 USD | 24,870.00 USD | 28,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8715` | 92,580.00 USD | 102,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8720` | 3,800,000.00 USD | 3,800,000.00 USD | 5,420.00 USD | 18,020.00 USD | 11,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8730` | 2,810,000.00 USD | 2,810,000.00 USD | 54,380.00 USD | 21,510.00 USD | 25,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8740` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 12,360.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8750` | 2,710,000.00 USD | 2,710,000.00 USD | 38,730.00 USD | 7,110.00 USD | 19,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8760` | 3,750,000.00 USD | 3,750,000.00 USD | 766.43 USD | 0.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 9,560.00 USD | 9,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8770` | 2,640,000.00 USD | 2,640,000.00 USD | 10,480.00 USD | 493.34 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8780` | 3,740,000.00 USD | 3,740,000.00 USD | 1,500.00 USD | 0.00 USD | 33,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8790` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 53,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8800` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 5,580.00 USD | 51,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8810` | 2,580,000.00 USD | 2,580,000.00 USD | 10,360.00 USD | 5,040.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8820` | 3,650,000.00 USD | 3,650,000.00 USD | 454.20 USD | 9,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8830` | 2,550,000.00 USD | 2,550,000.00 USD | 612.60 USD | 5,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8840` | 3,640,000.00 USD | 3,640,000.00 USD | 2,090.00 USD | 6,440.00 USD | 15,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8850` | 2,550,000.00 USD | 2,550,000.00 USD | 5,780.00 USD | 36,160.00 USD | 11,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8860` | 3,620,000.00 USD | 3,620,000.00 USD | 141,730.00 USD | 22,320.00 USD | 78,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8870` | 2,490,000.00 USD | 2,490,000.00 USD | 67,940.00 USD | 19,040.00 USD | 32,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8880` | 3,380,000.00 USD | 3,380,000.00 USD | 130,140.00 USD | 31,410.00 USD | 9,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8890` | 2,370,000.00 USD | 2,370,000.00 USD | 68,270.00 USD | 40,810.00 USD | 4,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8900` | 3,200,000.00 USD | 3,200,000.00 USD | 106,830.00 USD | 45,590.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8910` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 38,660.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8920` | 3,020,000.00 USD | 3,020,000.00 USD | 46,210.00 USD | 38,810.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8930` | 2,200,000.00 USD | 2,200,000.00 USD | 56,810.00 USD | 24,630.00 USD | 37,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8940` | 2,920,000.00 USD | 2,920,000.00 USD | 45,210.00 USD | 12,120.00 USD | 26,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8950` | 2,080,000.00 USD | 2,080,000.00 USD | 4,110.00 USD | 15,360.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8960` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 32,500.00 USD | 93,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8970` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 24,290.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8980` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 17,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8990` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 15,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9000` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 22,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9010` | 2,000,000.00 USD | 2,000,000.00 USD | 538.90 USD | 20,040.00 USD | 1,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9020` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 44,210.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9030` | 1,980,000.00 USD | 1,980,000.00 USD | 988.10 USD | 15,830.00 USD | 17,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9040` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 12,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9050` | 1,940,000.00 USD | 1,940,000.00 USD | 12,640.00 USD | 5,250.00 USD | 254.51 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9070` | 1,930,000.00 USD | 1,930,000.00 USD | 17,190.00 USD | 1,670.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9090` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 4,890.00 USD | 176.94 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9110` | 1,890,000.00 USD | 1,890,000.00 USD | 22,990.00 USD | 0.00 USD | 340.10 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9130` | 1,870,000.00 USD | 1,870,000.00 USD | 8,180.00 USD | 5,750.00 USD | 10,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9140` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 515.41 USD | 20,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9150` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 5,860.00 USD | 10,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9170` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 79.80 USD | 1,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9190` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 537.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9200` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9210` | 1,830,000.00 USD | 1,830,000.00 USD | 5,710.00 USD | 0.00 USD | 3,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9220` | 2,570,000.00 USD | 2,570,000.00 USD | 152,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9230` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 4,160.00 USD | 48.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9240` | 2,410,000.00 USD | 2,410,000.00 USD | 145,560.00 USD | 12,790.00 USD | 29,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9250` | 1,820,000.00 USD | 1,820,000.00 USD | 78,840.00 USD | 42,820.00 USD | 27,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9260` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 32,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9270` | 1,670,000.00 USD | 1,670,000.00 USD | 13,430.00 USD | 778.79 USD | 34,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9280` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 24,550.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9290` | 1,620,000.00 USD | 1,620,000.00 USD | 64,620.00 USD | 13,490.00 USD | 35,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9310` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 16.72 USD | 4,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9320` | 2,170,000.00 USD | 2,170,000.00 USD | 37,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9330` | 1,500,000.00 USD | 1,500,000.00 USD | 6,540.00 USD | 10,870.00 USD | 18,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9340` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 11,160.00 USD | 768.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9350` | 1,460,000.00 USD | 1,460,000.00 USD | 143,100.00 USD | 19,960.00 USD | 15,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9360` | 2,120,000.00 USD | 2,120,000.00 USD | 8,250.00 USD | 0.00 USD | 1,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9370` | 1,280,000.00 USD | 1,280,000.00 USD | 55,450.00 USD | 39,710.00 USD | 9,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9380` | 2,110,000.00 USD | 2,110,000.00 USD | 42,660.00 USD | 19,540.00 USD | 27,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9390` | 1,180,000.00 USD | 1,180,000.00 USD | 59,780.00 USD | 29,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9400` | 2,020,000.00 USD | 2,020,000.00 USD | 75,540.00 USD | 32,570.00 USD | 47,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9410` | 1,090,000.00 USD | 1,090,000.00 USD | 110,670.00 USD | 21,700.00 USD | 18,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9420` | 1,860,000.00 USD | 1,860,000.00 USD | 106,320.00 USD | 7,050.00 USD | 8,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9430` | 939,380.00 USD | 939,380.00 USD | 68,020.00 USD | 27,400.00 USD | 31,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9440` | 1,740,000.00 USD | 1,740,000.00 USD | 102,440.00 USD | 49,100.00 USD | 57,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9450` | 812,540.00 USD | 812,540.00 USD | 165,230.00 USD | 40,480.00 USD | 34,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9460` | 1,530,000.00 USD | 1,530,000.00 USD | 286,390.00 USD | 27,270.00 USD | 67,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9470` | 572,610.00 USD | 572,610.00 USD | 118,040.00 USD | 35,120.00 USD | 73,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9480` | 1,150,000.00 USD | 1,150,000.00 USD | 193,280.00 USD | 10,340.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9490` | 345,720.00 USD | 345,720.00 USD | 119,310.00 USD | 17,950.00 USD | 45,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9500` | 852,490.00 USD | 852,490.00 USD | 196,070.00 USD | 18,830.00 USD | 166,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9510` | 162,730.00 USD | 162,730.00 USD | 56,640.00 USD | 13,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9520` | 470,860.00 USD | 470,860.00 USD | 175,720.00 USD | 9,750.00 USD | 142,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9530` | 92,810.00 USD | 92,810.00 USD | 39,160.00 USD | 12,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9540` | 143,060.00 USD | 143,060.00 USD | 0.00 USD | 9,460.00 USD | 105,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9550` | 41,230.00 USD | 41,230.00 USD | 18,340.00 USD | 22,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9560` | 28,100.00 USD | 28,100.00 USD | 0.00 USD | 28,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9570` | 9,130.00 USD | 9,130.00 USD | 3,780.00 USD | 5,070.00 USD | 275.27 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9570` | 18,270.00 USD | 18,270.00 USD | 3,780.00 USD | 5,070.00 USD | 275.27 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9580` | 22,670.00 USD | 22,670.00 USD | 3,880.00 USD | 6,110.00 USD | 12,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9590` | 51,920.00 USD | 51,920.00 USD | 6,920.00 USD | 13,740.00 USD | 12,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9600` | 45,890.00 USD | 45,890.00 USD | 17,690.00 USD | 4,660.00 USD | 866.69 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9610` | 77,450.00 USD | 77,450.00 USD | 8,160.00 USD | 8,480.00 USD | 8,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9620` | 80,510.00 USD | 80,510.00 USD | 17,990.00 USD | 16,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9630` | 179,350.00 USD | 179,350.00 USD | 80,900.00 USD | 10,170.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9640` | 195,420.00 USD | 195,420.00 USD | 95,370.00 USD | 7,500.00 USD | 12,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9650` | 248,230.00 USD | 248,230.00 USD | 2,580.00 USD | 26,060.00 USD | 40,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9660` | 206,420.00 USD | 206,420.00 USD | 5,050.00 USD | 5,170.00 USD | 778.15 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9670` | 318,730.00 USD | 318,730.00 USD | 37,640.00 USD | 9,780.00 USD | 23,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9680` | 250,380.00 USD | 250,380.00 USD | 38,090.00 USD | 5,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9690` | 346,900.00 USD | 346,900.00 USD | 12,270.00 USD | 7,500.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9695` | 14,120.00 USD | 14,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9700` | 311,020.00 USD | 311,020.00 USD | 0.00 USD | 30,140.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9710` | 401,470.00 USD | 401,470.00 USD | 198.50 USD | 2,290.00 USD | 52,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9720` | 316,410.00 USD | 316,410.00 USD | 1,430.00 USD | 3,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9730` | 466,040.00 USD | 466,040.00 USD | 40,580.00 USD | 5,320.00 USD | 18,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9740` | 353,770.00 USD | 353,770.00 USD | 1,480.00 USD | 25,640.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9745` | 214.00 USD | 14,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9750` | 527,520.00 USD | 527,520.00 USD | 25,990.00 USD | 17,610.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9755` | 345.62 USD | 14,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9760` | 431,910.00 USD | 431,910.00 USD | 51,990.00 USD | 16,870.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9770` | 621,240.00 USD | 621,240.00 USD | 77,410.00 USD | 5,960.00 USD | 10,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9780` | 456,190.00 USD | 456,190.00 USD | 0.00 USD | 0.00 USD | 24,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9790` | 686,390.00 USD | 686,390.00 USD | 29,670.00 USD | 9,580.00 USD | 25,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9800` | 608,660.00 USD | 608,660.00 USD | 0.00 USD | 0.00 USD | 152,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9810` | 705,260.00 USD | 705,260.00 USD | 11,870.00 USD | 246.39 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9820` | 782,130.00 USD | 782,130.00 USD | 53,310.00 USD | 15,990.00 USD | 104,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9830` | 771,410.00 USD | 771,410.00 USD | 15,980.00 USD | 20,550.00 USD | 29,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9840` | 854,570.00 USD | 854,570.00 USD | 49,930.00 USD | 211.77 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9850` | 833,940.00 USD | 833,940.00 USD | 39,130.00 USD | 4,560.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9860` | 855,960.00 USD | 855,960.00 USD | 0.00 USD | 0.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9870` | 870,310.00 USD | 870,310.00 USD | 12,080.00 USD | 3,610.00 USD | 20,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9880` | 963,440.00 USD | 963,440.00 USD | 40,020.00 USD | 0.00 USD | 67,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9890` | 917,950.00 USD | 917,950.00 USD | 24,170.00 USD | 0.00 USD | 23,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9900` | 984,870.00 USD | 984,870.00 USD | 20,530.00 USD | 0.00 USD | 906.61 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9910` | 1,010,000.00 USD | 1,010,000.00 USD | 51,650.00 USD | 1,610.00 USD | 36,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9920` | 1,010,000.00 USD | 1,010,000.00 USD | 1,570.00 USD | 479.24 USD | 21,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9930` | 1,040,000.00 USD | 1,040,000.00 USD | 16,270.00 USD | 14,570.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9940` | 1,050,000.00 USD | 1,050,000.00 USD | 29,270.00 USD | 0.00 USD | 16,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9950` | 1,070,000.00 USD | 1,070,000.00 USD | 29,210.00 USD | 31.60 USD | 329.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9960` | 1,180,000.00 USD | 1,180,000.00 USD | 75,810.00 USD | 5,380.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9970` | 1,130,000.00 USD | 1,130,000.00 USD | 46,950.00 USD | 1,840.00 USD | 13,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9980` | 1,240,000.00 USD | 1,240,000.00 USD | 53,110.00 USD | 6,740.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9990` | 1,200,000.00 USD | 1,200,000.00 USD | 34,090.00 USD | 17,910.00 USD | 10,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 1,300,000.00 USD | 1,300,000.00 USD | 52,850.00 USD | 0.00 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,270,000.00 USD | 1,270,000.00 USD | 54,580.00 USD | 10,730.00 USD | 13,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 1,390,000.00 USD | 1,390,000.00 USD | 54,650.00 USD | 21,850.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,300,000.00 USD | 1,300,000.00 USD | 10,110.00 USD | 9,280.00 USD | 6,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 1,470,000.00 USD | 1,470,000.00 USD | 70,950.00 USD | 3,970.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,370,000.00 USD | 1,370,000.00 USD | 54,780.00 USD | 5,480.00 USD | 5,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 1,520,000.00 USD | 1,520,000.00 USD | 46,710.00 USD | 0.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 221.13 USD | 14,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.01` | 1,480,000.00 USD | 1,480,000.00 USD | 47,140.00 USD | 11,610.00 USD | 53,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 44,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 1,530,000.00 USD | 1,530,000.00 USD | 30,870.00 USD | 13,790.00 USD | 7,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 1,590,000.00 USD | 1,590,000.00 USD | 10,260.00 USD | 14,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 1,570,000.00 USD | 1,570,000.00 USD | 9,660.00 USD | 28,610.00 USD | 265.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 1,660,000.00 USD | 1,660,000.00 USD | 33,230.00 USD | 30,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 1,590,000.00 USD | 1,590,000.00 USD | 10,450.00 USD | 3,050.00 USD | 3,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 1,690,000.00 USD | 1,690,000.00 USD | 2,870.00 USD | 28,450.00 USD | 735.11 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 1,650,000.00 USD | 1,650,000.00 USD | 19,580.00 USD | 25,030.00 USD | 21,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 1,730,000.00 USD | 1,730,000.00 USD | 526.60 USD | 28,470.00 USD | 11,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,690,000.00 USD | 1,690,000.00 USD | 2,810.00 USD | 7,870.00 USD | 26,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 25,010.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,770,000.00 USD | 1,770,000.00 USD | 60,720.00 USD | 4,830.00 USD | 10,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 1,940,000.00 USD | 1,940,000.00 USD | 33,820.00 USD | 84,220.00 USD | 44,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,820,000.00 USD | 1,820,000.00 USD | 26,430.00 USD | 11,530.00 USD | 21,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,160,000.00 USD | 2,160,000.00 USD | 56,930.00 USD | 52,610.00 USD | 112,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,930,000.00 USD | 1,930,000.00 USD | 48,740.00 USD | 21,040.00 USD | 36,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,380,000.00 USD | 2,380,000.00 USD | 78,220.00 USD | 56,700.00 USD | 86,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,020,000.00 USD | 2,020,000.00 USD | 44,890.00 USD | 13,350.00 USD | 30,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,560,000.00 USD | 2,560,000.00 USD | 22,650.00 USD | 124,880.00 USD | 33,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,050,000.00 USD | 2,050,000.00 USD | 16,060.00 USD | 10,270.00 USD | 7,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,890,000.00 USD | 2,890,000.00 USD | 250,310.00 USD | 50,530.00 USD | 24,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,120,000.00 USD | 2,120,000.00 USD | 22,230.00 USD | 18,890.00 USD | 25,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,070,000.00 USD | 3,070,000.00 USD | 134,200.00 USD | 33,660.00 USD | 19,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,240,000.00 USD | 2,240,000.00 USD | 75,770.00 USD | 9,640.00 USD | 31,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,180,000.00 USD | 3,180,000.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,270,000.00 USD | 2,270,000.00 USD | 17,220.00 USD | 124.83 USD | 16,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,410,000.00 USD | 3,410,000.00 USD | 217,210.00 USD | 8,290.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,300,000.00 USD | 2,300,000.00 USD | 9,200.00 USD | 17,340.00 USD | 7,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,720,000.00 USD | 3,720,000.00 USD | 262,550.00 USD | 3,170.00 USD | 42,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,350,000.00 USD | 2,350,000.00 USD | 41,230.00 USD | 1,910.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 4,100,000.00 USD | 4,100,000.00 USD | 178,400.00 USD | 1,290.00 USD | 199,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 228.37 USD | 15,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,370,000.00 USD | 2,370,000.00 USD | 7,870.00 USD | 4,560.00 USD | 3,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 4,480,000.00 USD | 4,480,000.00 USD | 279,840.00 USD | 9,430.00 USD | 93,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,380,000.00 USD | 2,380,000.00 USD | 2,930.00 USD | 2,550.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 4,810,000.00 USD | 4,810,000.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,410,000.00 USD | 2,410,000.00 USD | 10,940.00 USD | 7,010.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,070,000.00 USD | 5,070,000.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,410,000.00 USD | 2,410,000.00 USD | 1,400.00 USD | 63.94 USD | 6,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 5,480,000.00 USD | 5,480,000.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,430,000.00 USD | 2,430,000.00 USD | 7,610.00 USD | 4,620.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 367.04 USD | 15,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 5,870,000.00 USD | 5,870,000.00 USD | 199,320.00 USD | 28,070.00 USD | 161,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,440,000.00 USD | 2,440,000.00 USD | 3,990.00 USD | 4,010.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 6,030,000.00 USD | 6,030,000.00 USD | 91,750.00 USD | 29,070.00 USD | 40,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,490,000.00 USD | 2,490,000.00 USD | 30,030.00 USD | 73.09 USD | 13,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 6,360,000.00 USD | 6,360,000.00 USD | 140,530.00 USD | 49,780.00 USD | 134,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,500,000.00 USD | 2,500,000.00 USD | 4,370.00 USD | 1,400.00 USD | 3,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 6,530,000.00 USD | 6,530,000.00 USD | 88,940.00 USD | 44,290.00 USD | 36,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,510,000.00 USD | 2,510,000.00 USD | 6,580.00 USD | 1,450.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 2,520,000.00 USD | 2,520,000.00 USD | 5,670.00 USD | 3,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,890,000.00 USD | 6,890,000.00 USD | 187,610.00 USD | 48,000.00 USD | 121,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 7,250,000.00 USD | 7,250,000.00 USD | 205,690.00 USD | 63,350.00 USD | 94,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 7,660,000.00 USD | 7,660,000.00 USD | 217,790.00 USD | 73,000.00 USD | 125,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 7,950,000.00 USD | 7,950,000.00 USD | 131,720.00 USD | 83,000.00 USD | 66,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,190,000.00 USD | 8,190,000.00 USD | 102,750.00 USD | 49,310.00 USD | 92,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 8,370,000.00 USD | 8,370,000.00 USD | 77,920.00 USD | 32,860.00 USD | 73,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 8,720,000.00 USD | 8,720,000.00 USD | 221,410.00 USD | 30,180.00 USD | 93,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 8,920,000.00 USD | 8,920,000.00 USD | 121,300.00 USD | 33,170.00 USD | 42,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 9,140,000.00 USD | 9,140,000.00 USD | 103,500.00 USD | 37,730.00 USD | 83,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 9,340,000.00 USD | 9,340,000.00 USD | 92,440.00 USD | 21,500.00 USD | 83,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 9,490,000.00 USD | 9,490,000.00 USD | 103,110.00 USD | 18,720.00 USD | 27,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 9,760,000.00 USD | 9,760,000.00 USD | 158,650.00 USD | 40,740.00 USD | 69,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 9,990,000.00 USD | 9,990,000.00 USD | 176,790.00 USD | 26,190.00 USD | 33,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.08` | 2,230.00 USD | 17,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.08` | 10,120,000.00 USD | 10,120,000.00 USD | 62,710.00 USD | 20,510.00 USD | 39,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 10,300,000.00 USD | 10,300,000.00 USD | 46,000.00 USD | 31,940.00 USD | 103,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 10,530,000.00 USD | 10,530,000.00 USD | 161,270.00 USD | 28,200.00 USD | 42,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 10,760,000.00 USD | 10,760,000.00 USD | 59,850.00 USD | 57,700.00 USD | 117,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 10,920,000.00 USD | 10,920,000.00 USD | 109,670.00 USD | 18,350.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 11,050,000.00 USD | 11,050,000.00 USD | 36,490.00 USD | 24,570.00 USD | 62,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 11,210,000.00 USD | 11,210,000.00 USD | 67,090.00 USD | 37,290.00 USD | 55,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 11,370,000.00 USD | 11,370,000.00 USD | 64,450.00 USD | 32,080.00 USD | 65,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 11,610,000.00 USD | 11,610,000.00 USD | 119,850.00 USD | 21,050.00 USD | 97,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 11,890,000.00 USD | 11,890,000.00 USD | 182,190.00 USD | 61,190.00 USD | 40,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 11,960,000.00 USD | 11,960,000.00 USD | 59,740.00 USD | 10,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.11` | 170.02 USD | 17,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.17` | 2,450.00 USD | 20,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 11,730.00 USD | 32,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 239.77 USD | 32,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,190.00 USD | 35,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 119.37 USD | 35,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 176.31 USD | 35,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 1,810.00 USD | 37,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 799.29 USD | 38,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 2,440.00 USD | 40,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 8,240.00 USD | 49,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 300.15 USD | 49,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 244.83 USD | 49,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 328.44 USD | 49,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 190.42 USD | 50,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 380.81 USD | 50,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 89,590.00 USD | 140,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 23,760.00 USD | 163,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 208.37 USD | 164,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2255` | 466,900.00 USD | 0.00 USD | 112.75 USD | `-76.07%` | `500.00` |
| `Live` | `Long` | `0.3595` | 466,790.00 USD | 0.00 USD | 794.14 USD | `-61.85%` | `2,209.00` |
| `Live` | `Long` | `0.4195` | 465,990.00 USD | 0.00 USD | 2,800.00 USD | `-55.48%` | `6,675.20` |
| `Live` | `Long` | `0.4215` | 463,190.00 USD | 0.00 USD | 2,400.00 USD | `-55.27%` | `5,698.80` |
| `Live` | `Long` | `0.4645` | 460,790.00 USD | 0.00 USD | 315.16 USD | `-50.71%` | `678.50` |
| `Live` | `Long` | `0.4675` | 460,480.00 USD | 0.00 USD | 146.70 USD | `-50.39%` | `313.80` |
| `Live` | `Long` | `0.4705` | 460,330.00 USD | 0.00 USD | 2,590.00 USD | `-50.07%` | `5,500.00` |
| `Live` | `Long` | `0.4755` | 457,740.00 USD | 0.00 USD | 1,240.00 USD | `-49.54%` | `2,618.10` |
| `Live` | `Long` | `0.5065` | 456,500.00 USD | 0.00 USD | 3,290.00 USD | `-46.25%` | `6,504.70` |
| `Live` | `Long` | `0.5325` | 453,200.00 USD | 0.00 USD | 532.50 USD | `-43.49%` | `1,000.00` |
| `Live` | `Long` | `0.5455` | 452,670.00 USD | 0.00 USD | 142.98 USD | `-42.11%` | `262.10` |
| `Live` | `Long` | `0.5655` | 452,530.00 USD | 0.00 USD | 14,600.00 USD | `-39.99%` | `25,816.60` |
| `Live` | `Long` | `0.5695` | 437,930.00 USD | 0.00 USD | 803.17 USD | `-39.57%` | `1,410.30` |
| `Live` | `Long` | `0.5815` | 437,120.00 USD | 0.00 USD | 233.01 USD | `-38.29%` | `400.70` |
| `Live` | `Long` | `0.5845` | 436,890.00 USD | 0.00 USD | 683.51 USD | `-37.97%` | `1,169.40` |
| `Live` | `Long` | `0.5895` | 436,210.00 USD | 0.00 USD | 137.53 USD | `-37.44%` | `233.30` |
| `Live` | `Long` | `0.6055` | 436,070.00 USD | 0.00 USD | 1,480.00 USD | `-35.75%` | `2,448.50` |
| `Live` | `Long` | `0.6065` | 434,590.00 USD | 0.00 USD | 1,800.00 USD | `-35.64%` | `2,971.80` |
| `Live` | `Long` | `0.6125` | 432,780.00 USD | 0.00 USD | 105.96 USD | `-35.00%` | `173.00` |
| `Live` | `Long` | `0.6145` | 432,680.00 USD | 0.00 USD | 147.48 USD | `-34.79%` | `240.00` |
| `Live` | `Long` | `0.6315` | 432,530.00 USD | 0.00 USD | 757.80 USD | `-32.99%` | `1,200.00` |
| `Live` | `Long` | `0.6355` | 431,770.00 USD | 0.00 USD | 106.00 USD | `-32.56%` | `166.80` |
| `Live` | `Long` | `0.6365` | 431,670.00 USD | 0.00 USD | 507.86 USD | `-32.46%` | `797.90` |
| `Live` | `Long` | `0.6405` | 431,160.00 USD | 0.00 USD | 2,090.00 USD | `-32.03%` | `3,262.00` |
| `Live` | `Long` | `0.6415` | 429,070.00 USD | 0.00 USD | 20,270.00 USD | `-31.93%` | `31,595.60` |
| `Live` | `Long` | `0.6465` | 408,800.00 USD | 0.00 USD | 4,230.00 USD | `-31.40%` | `6,539.70` |
| `Live` | `Long` | `0.6475` | 404,570.00 USD | 0.00 USD | 202.47 USD | `-31.29%` | `312.70` |
| `Live` | `Long` | `0.6555` | 404,370.00 USD | 0.00 USD | 521.19 USD | `-30.44%` | `795.10` |
| `Live` | `Long` | `0.6595` | 403,850.00 USD | 0.00 USD | 149.44 USD | `-30.02%` | `226.60` |
| `Live` | `Long` | `0.6725` | 403,700.00 USD | 0.00 USD | 63,890.00 USD | `-28.64%` | `95,000.00` |
| `Live` | `Long` | `0.6775` | 339,810.00 USD | 0.00 USD | 85,110.00 USD | `-28.11%` | `125,624.50` |
| `Live` | `Long` | `0.6835` | 254,700.00 USD | 0.00 USD | 512.97 USD | `-27.47%` | `750.50` |
| `Live` | `Long` | `0.6915` | 254,190.00 USD | 0.00 USD | 19,800.00 USD | `-26.62%` | `28,635.00` |
| `Live` | `Long` | `0.6935` | 234,390.00 USD | 0.00 USD | 154.93 USD | `-26.41%` | `223.40` |
| `Live` | `Long` | `0.6965` | 234,230.00 USD | 0.00 USD | 322.62 USD | `-26.09%` | `463.20` |
| `Live` | `Long` | `0.7005` | 233,910.00 USD | 0.00 USD | 1,140.00 USD | `-25.67%` | `1,634.20` |
| `Live` | `Long` | `0.7145` | 232,770.00 USD | 0.00 USD | 988.87 USD | `-24.18%` | `1,384.00` |
| `Live` | `Long` | `0.7215` | 231,780.00 USD | 0.00 USD | 1,580.00 USD | `-23.44%` | `2,190.90` |
| `Live` | `Long` | `0.7235` | 230,200.00 USD | 0.00 USD | 397.93 USD | `-23.22%` | `550.00` |
| `Live` | `Long` | `0.7285` | 229,800.00 USD | 0.00 USD | 291.18 USD | `-22.69%` | `399.70` |
| `Live` | `Long` | `0.7305` | 229,510.00 USD | 0.00 USD | 2,300.00 USD | `-22.48%` | `3,143.00` |
| `Live` | `Long` | `0.7335` | 227,210.00 USD | 0.00 USD | 1,140.00 USD | `-22.16%` | `1,557.80` |
| `Live` | `Long` | `0.7395` | 226,070.00 USD | 0.00 USD | 283.30 USD | `-21.53%` | `383.10` |
| `Live` | `Long` | `0.7525` | 225,790.00 USD | 0.00 USD | 331.18 USD | `-20.15%` | `440.10` |
| `Live` | `Long` | `0.7545` | 225,450.00 USD | 0.00 USD | 1,400.00 USD | `-19.94%` | `1,859.90` |
| `Live` | `Long` | `0.7555` | 224,050.00 USD | 0.00 USD | 8,990.00 USD | `-19.83%` | `11,902.80` |
| `Live` | `Long` | `0.7635` | 215,060.00 USD | 0.00 USD | 308.00 USD | `-18.98%` | `403.40` |
| `Live` | `Long` | `0.7645` | 214,750.00 USD | 0.00 USD | 54,280.00 USD | `-18.87%` | `71,003.30` |
| `Live` | `Long` | `0.7725` | 160,470.00 USD | 0.00 USD | 3,840.00 USD | `-18.02%` | `4,968.90` |
| `Live` | `Long` | `0.7775` | 156,630.00 USD | 0.00 USD | 2,490.00 USD | `-17.49%` | `3,199.30` |
| `Live` | `Long` | `0.7795` | 154,140.00 USD | 0.00 USD | 272.83 USD | `-17.28%` | `350.00` |
| `Live` | `Long` | `0.7865` | 153,870.00 USD | 0.00 USD | 292.03 USD | `-16.54%` | `371.30` |
| `Live` | `Long` | `0.7905` | 153,580.00 USD | 0.00 USD | 277.39 USD | `-16.11%` | `350.90` |
| `Live` | `Long` | `0.8135` | 153,300.00 USD | 0.00 USD | 647.79 USD | `-13.67%` | `796.30` |
| `Live` | `Long` | `0.8215` | 152,650.00 USD | 0.00 USD | 1,950.00 USD | `-12.83%` | `2,370.70` |
| `Live` | `Long` | `0.8235` | 150,700.00 USD | 0.00 USD | 749.96 USD | `-12.61%` | `910.70` |
| `Live` | `Long` | `0.8365` | 149,950.00 USD | 0.00 USD | 316.70 USD | `-11.23%` | `378.60` |
| `Live` | `Long` | `0.8415` | 149,640.00 USD | 0.00 USD | 1,570.00 USD | `-10.70%` | `1,862.40` |
| `Live` | `Long` | `0.8435` | 148,070.00 USD | 0.00 USD | 751.39 USD | `-10.49%` | `890.80` |
| `Live` | `Long` | `0.8495` | 147,320.00 USD | 0.00 USD | 1,260.00 USD | `-9.85%` | `1,486.90` |
| `Live` | `Long` | `0.8515` | 146,060.00 USD | 0.00 USD | 2,700.00 USD | `-9.64%` | `3,175.90` |
| `Live` | `Long` | `0.8575` | 143,350.00 USD | 0.00 USD | 620.32 USD | `-9.01%` | `723.40` |
| `Live` | `Long` | `0.8605` | 142,730.00 USD | 0.00 USD | 25,780.00 USD | `-8.69%` | `29,964.40` |
| `Live` | `Long` | `0.8615` | 116,950.00 USD | 0.00 USD | 181.17 USD | `-8.58%` | `210.30` |
| `Live` | `Long` | `0.8635` | 116,770.00 USD | 0.00 USD | 208.02 USD | `-8.37%` | `240.90` |
| `Live` | `Long` | `0.8645` | 116,560.00 USD | 0.00 USD | 438.30 USD | `-8.26%` | `507.00` |
| `Live` | `Long` | `0.8665` | 116,120.00 USD | 0.00 USD | 1,390.00 USD | `-8.05%` | `1,606.10` |
| `Live` | `Long` | `0.8695` | 114,730.00 USD | 0.00 USD | 12,590.00 USD | `-7.73%` | `14,478.80` |
| `Live` | `Long` | `0.8715` | 102,140.00 USD | 0.00 USD | 92,580.00 USD | `-7.52%` | `106,233.40` |
| `Live` | `Long` | `0.8765` | 9,560.00 USD | 0.00 USD | 9,560.00 USD | `-6.99%` | `10,903.10` |
| `Live` | `Short` | `0.9695` | 14,120.00 USD | 14,120.00 USD | 0.00 USD | `+2.88%` | `14,561.60` |
| `Live` | `Short` | `0.9745` | 14,330.00 USD | 214.00 USD | 0.00 USD | `+3.41%` | `219.60` |
| `Live` | `Short` | `0.9755` | 14,680.00 USD | 345.62 USD | 0.00 USD | `+3.52%` | `354.30` |
| `Live` | `Short` | `1.01` | 14,900.00 USD | 221.13 USD | 0.00 USD | `+6.81%` | `219.70` |
| `Live` | `Short` | `1.04` | 15,130.00 USD | 228.37 USD | 0.00 USD | `+10.20%` | `219.90` |
| `Live` | `Short` | `1.05` | 15,490.00 USD | 367.04 USD | 0.00 USD | `+11.16%` | `350.40` |
| `Live` | `Short` | `1.08` | 17,730.00 USD | 2,230.00 USD | 0.00 USD | `+14.77%` | `2,064.20` |
| `Live` | `Short` | `1.11` | 17,900.00 USD | 170.02 USD | 0.00 USD | `+17.84%` | `153.10` |
| `Live` | `Short` | `1.17` | 20,350.00 USD | 2,450.00 USD | 0.00 USD | `+24.21%` | `2,096.60` |
| `Live` | `Short` | `1.32` | 32,080.00 USD | 11,730.00 USD | 0.00 USD | `+40.45%` | `8,862.90` |
| `Live` | `Short` | `1.34` | 32,320.00 USD | 239.77 USD | 0.00 USD | `+42.14%` | `179.00` |
| `Live` | `Short` | `1.42` | 35,510.00 USD | 3,190.00 USD | 0.00 USD | `+50.63%` | `2,249.30` |
| `Live` | `Short` | `1.50` | 35,630.00 USD | 119.37 USD | 0.00 USD | `+59.33%` | `79.50` |
| `Live` | `Short` | `1.54` | 35,810.00 USD | 176.31 USD | 0.00 USD | `+63.68%` | `114.30` |
| `Live` | `Short` | `1.56` | 37,620.00 USD | 1,810.00 USD | 0.00 USD | `+65.17%` | `1,161.90` |
| `Live` | `Short` | `1.60` | 38,420.00 USD | 799.29 USD | 0.00 USD | `+69.84%` | `499.40` |
| `Live` | `Short` | `1.62` | 40,850.00 USD | 2,440.00 USD | 0.00 USD | `+72.39%` | `1,500.00` |
| `Live` | `Short` | `1.65` | 49,090.00 USD | 8,240.00 USD | 0.00 USD | `+74.83%` | `5,000.00` |
| `Live` | `Short` | `1.67` | 49,390.00 USD | 300.15 USD | 0.00 USD | `+76.95%` | `180.00` |
| `Live` | `Short` | `1.67` | 49,640.00 USD | 244.83 USD | 0.00 USD | `+77.59%` | `146.30` |
| `Live` | `Short` | `1.71` | 49,960.00 USD | 328.44 USD | 0.00 USD | `+81.62%` | `191.90` |
| `Live` | `Short` | `1.73` | 50,150.00 USD | 190.42 USD | 0.00 USD | `+83.53%` | `110.10` |
| `Live` | `Short` | `1.77` | 50,540.00 USD | 380.81 USD | 0.00 USD | `+88.30%` | `214.60` |
| `Live` | `Short` | `1.80` | 140,130.00 USD | 89,590.00 USD | 0.00 USD | `+91.06%` | `49,759.80` |
| `Live` | `Short` | `1.84` | 163,890.00 USD | 23,760.00 USD | 0.00 USD | `+95.20%` | `12,916.90` |
| `Live` | `Short` | `1.86` | 164,100.00 USD | 208.37 USD | 0.00 USD | `+96.90%` | `112.30` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.4015` | 359,520.00 USD | 0.00 USD | 120.45 USD | `-57.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 359,400.00 USD | 0.00 USD | 150.15 USD | `-46.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5435` | 359,250.00 USD | 0.00 USD | 186.15 USD | `-42.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 359,070.00 USD | 0.00 USD | 1,150.00 USD | `-30.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 357,920.00 USD | 0.00 USD | 781.90 USD | `-25.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 357,140.00 USD | 0.00 USD | 477.38 USD | `-24.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 356,660.00 USD | 0.00 USD | 341.33 USD | `-23.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 356,320.00 USD | 0.00 USD | 972.82 USD | `-23.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 355,350.00 USD | 0.00 USD | 160.20 USD | `-22.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7385` | 355,190.00 USD | 0.00 USD | 102.58 USD | `-21.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 355,080.00 USD | 0.00 USD | 289.49 USD | `-20.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7615` | 354,790.00 USD | 0.00 USD | 197.53 USD | `-19.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 354,600.00 USD | 0.00 USD | 14,570.00 USD | `-17.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 340,030.00 USD | 0.00 USD | 213.58 USD | `-16.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 339,820.00 USD | 0.00 USD | 274,830.00 USD | `-15.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 64,980.00 USD | 0.00 USD | 108.47 USD | `-15.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 64,870.00 USD | 0.00 USD | 326.96 USD | `-13.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 64,550.00 USD | 0.00 USD | 405.75 USD | `-13.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 64,140.00 USD | 0.00 USD | 772.84 USD | `-11.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8415` | 63,370.00 USD | 0.00 USD | 2,670.00 USD | `-10.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8495` | 60,700.00 USD | 0.00 USD | 3,470.00 USD | `-9.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 57,230.00 USD | 0.00 USD | 9,180.00 USD | `-9.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 48,050.00 USD | 0.00 USD | 341.94 USD | `-9.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 47,700.00 USD | 0.00 USD | 1,150.00 USD | `-9.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 46,560.00 USD | 0.00 USD | 429.25 USD | `-8.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 46,130.00 USD | 0.00 USD | 223.30 USD | `-8.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 45,900.00 USD | 0.00 USD | 518.51 USD | `-8.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 45,390.00 USD | 0.00 USD | 205.24 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 45,180.00 USD | 0.00 USD | 649.66 USD | `-7.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 44,530.00 USD | 0.00 USD | 194.06 USD | `-6.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8845` | 44,340.00 USD | 0.00 USD | 193.35 USD | `-6.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 44,140.00 USD | 0.00 USD | 223.04 USD | `-5.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 43,920.00 USD | 0.00 USD | 10,840.00 USD | `-5.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 33,080.00 USD | 0.00 USD | 4,920.00 USD | `-5.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8915` | 28,160.00 USD | 0.00 USD | 317.02 USD | `-5.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 27,840.00 USD | 0.00 USD | 192.07 USD | `-5.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 27,650.00 USD | 0.00 USD | 195.32 USD | `-5.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8965` | 27,450.00 USD | 0.00 USD | 196.87 USD | `-4.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8985` | 27,260.00 USD | 0.00 USD | 2,870.00 USD | `-4.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9005` | 24,380.00 USD | 0.00 USD | 319.05 USD | `-4.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9025` | 24,060.00 USD | 0.00 USD | 398.91 USD | `-4.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9035` | 23,670.00 USD | 0.00 USD | 196.96 USD | `-4.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9045` | 23,470.00 USD | 0.00 USD | 300.38 USD | `-4.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9065` | 23,170.00 USD | 0.00 USD | 198.61 USD | `-3.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9075` | 22,970.00 USD | 0.00 USD | 994.35 USD | `-3.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 21,980.00 USD | 0.00 USD | 363.40 USD | `-3.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9095` | 21,610.00 USD | 0.00 USD | 198.18 USD | `-3.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9115` | 21,410.00 USD | 0.00 USD | 397.23 USD | `-3.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9135` | 21,020.00 USD | 0.00 USD | 398.65 USD | `-3.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9145` | 20,620.00 USD | 0.00 USD | 399.09 USD | `-2.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9155` | 20,220.00 USD | 0.00 USD | 403.92 USD | `-2.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9165` | 19,810.00 USD | 0.00 USD | 198.06 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9175` | 19,620.00 USD | 0.00 USD | 223.78 USD | `-2.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9185` | 19,390.00 USD | 0.00 USD | 899.85 USD | `-2.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9195` | 18,490.00 USD | 0.00 USD | 900.19 USD | `-2.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 17,590.00 USD | 0.00 USD | 407.41 USD | `-2.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9215` | 17,190.00 USD | 0.00 USD | 407.30 USD | `-2.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9225` | 16,780.00 USD | 0.00 USD | 201.94 USD | `-2.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9245` | 16,580.00 USD | 0.00 USD | 201.45 USD | `-1.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9255` | 16,370.00 USD | 0.00 USD | 817.40 USD | `-1.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9265` | 15,560.00 USD | 0.00 USD | 403.77 USD | `-1.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9275` | 15,150.00 USD | 0.00 USD | 2,120.00 USD | `-1.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9285` | 13,040.00 USD | 0.00 USD | 246.05 USD | `-1.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9295` | 12,790.00 USD | 0.00 USD | 407.49 USD | `-1.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9305` | 12,380.00 USD | 0.00 USD | 203.97 USD | `-1.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9315` | 12,180.00 USD | 0.00 USD | 263.80 USD | `-1.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9325` | 11,910.00 USD | 0.00 USD | 241.98 USD | `-1.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9335` | 11,670.00 USD | 0.00 USD | 814.76 USD | `-0.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9355` | 10,860.00 USD | 0.00 USD | 201.97 USD | `-0.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9365` | 10,660.00 USD | 0.00 USD | 9,680.00 USD | `-0.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9395` | 971.19 USD | 0.00 USD | 416.01 USD | `-0.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9405` | 555.18 USD | 0.00 USD | 555.18 USD | `-0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 816.96 USD | 816.96 USD | 0.00 USD | `+0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 1,150.00 USD | 334.28 USD | 0.00 USD | `+0.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 2,880.00 USD | 1,730.00 USD | 0.00 USD | `+0.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 3,260.00 USD | 383.87 USD | 0.00 USD | `+0.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 3,890.00 USD | 623.93 USD | 0.00 USD | `+0.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 4,300.00 USD | 414.68 USD | 0.00 USD | `+0.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9525` | 4,680.00 USD | 381.00 USD | 0.00 USD | `+1.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 6,700.00 USD | 2,020.00 USD | 0.00 USD | `+1.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 6,910.00 USD | 206.77 USD | 0.00 USD | `+1.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 7,140.00 USD | 236.26 USD | 0.00 USD | `+1.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 7,280.00 USD | 136.83 USD | 0.00 USD | `+1.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 7,540.00 USD | 261.16 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 9,450.00 USD | 1,910.00 USD | 0.00 USD | `+2.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 10,010.00 USD | 568.75 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 10,180.00 USD | 163.29 USD | 0.00 USD | `+2.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 10,560.00 USD | 385.74 USD | 0.00 USD | `+2.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 12,600.00 USD | 2,030.00 USD | 0.00 USD | `+2.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 12,860.00 USD | 262.52 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 13,250.00 USD | 387.83 USD | 0.00 USD | `+3.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 20,880.00 USD | 7,630.00 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9745` | 29,630.00 USD | 8,750.00 USD | 0.00 USD | `+3.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 51,590.00 USD | 21,960.00 USD | 0.00 USD | `+3.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 51,990.00 USD | 396.17 USD | 0.00 USD | `+3.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 52,660.00 USD | 676.53 USD | 0.00 USD | `+3.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 61,020.00 USD | 8,350.00 USD | 0.00 USD | `+4.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 63,040.00 USD | 2,030.00 USD | 0.00 USD | `+4.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 65,100.00 USD | 2,060.00 USD | 0.00 USD | `+4.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 65,360.00 USD | 255.38 USD | 0.00 USD | `+4.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 80,430.00 USD | 15,070.00 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9865` | 80,540.00 USD | 109.99 USD | 0.00 USD | `+4.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 84,060.00 USD | 3,520.00 USD | 0.00 USD | `+5.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 115,810.00 USD | 31,750.00 USD | 0.00 USD | `+5.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 116,210.00 USD | 403.06 USD | 0.00 USD | `+5.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 116,620.00 USD | 403.28 USD | 0.00 USD | `+5.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 121,760.00 USD | 5,140.00 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 159,070.00 USD | 37,310.00 USD | 0.00 USD | `+5.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 160,070.00 USD | 1,000.00 USD | 0.00 USD | `+6.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 200,660.00 USD | 40,590.00 USD | 0.00 USD | `+6.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 200,900.00 USD | 235.79 USD | 0.00 USD | `+6.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 202,240.00 USD | 1,340.00 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 202,470.00 USD | 230.39 USD | 0.00 USD | `+6.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 202,690.00 USD | 218.64 USD | 0.00 USD | `+7.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 203,100.00 USD | 409.86 USD | 0.00 USD | `+7.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 203,210.00 USD | 110.95 USD | 0.00 USD | `+7.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 203,830.00 USD | 615.60 USD | 0.00 USD | `+7.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 204,390.00 USD | 561.17 USD | 0.00 USD | `+7.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 204,600.00 USD | 214.40 USD | 0.00 USD | `+8.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 204,850.00 USD | 249.88 USD | 0.00 USD | `+8.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 205,060.00 USD | 207.97 USD | 0.00 USD | `+8.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 205,270.00 USD | 208.26 USD | 0.00 USD | `+9.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 205,790.00 USD | 516.75 USD | 0.00 USD | `+9.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 206,140.00 USD | 348.86 USD | 0.00 USD | `+9.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 206,530.00 USD | 391.80 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 206,940.00 USD | 413.76 USD | 0.00 USD | `+10.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 207,300.00 USD | 354.91 USD | 0.00 USD | `+10.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 209,200.00 USD | 1,900.00 USD | 0.00 USD | `+10.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 209,410.00 USD | 207.87 USD | 0.00 USD | `+10.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 209,620.00 USD | 207.97 USD | 0.00 USD | `+10.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 209,720.00 USD | 107.99 USD | 0.00 USD | `+11.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 284,560.00 USD | 74,840.00 USD | 0.00 USD | `+12.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 285,100.00 USD | 544.88 USD | 0.00 USD | `+13.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 287,280.00 USD | 2,170.00 USD | 0.00 USD | `+15.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 288,810.00 USD | 1,540.00 USD | 0.00 USD | `+15.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 298,740.00 USD | 9,930.00 USD | 0.00 USD | `+16.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 299,620.00 USD | 877.63 USD | 0.00 USD | `+17.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 299,790.00 USD | 171.09 USD | 0.00 USD | `+18.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 302,560.00 USD | 2,770.00 USD | 0.00 USD | `+19.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 304,600.00 USD | 2,040.00 USD | 0.00 USD | `+19.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 304,770.00 USD | 172.32 USD | 0.00 USD | `+19.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 304,960.00 USD | 187.72 USD | 0.00 USD | `+19.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 305,140.00 USD | 188.39 USD | 0.00 USD | `+20.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 307,810.00 USD | 2,670.00 USD | 0.00 USD | `+20.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 307,980.00 USD | 174.23 USD | 0.00 USD | `+20.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 308,160.00 USD | 174.38 USD | 0.00 USD | `+20.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 308,330.00 USD | 174.84 USD | 0.00 USD | `+21.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 308,480.00 USD | 150.90 USD | 0.00 USD | `+21.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 308,640.00 USD | 151.03 USD | 0.00 USD | `+21.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 308,790.00 USD | 151.16 USD | 0.00 USD | `+21.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 308,940.00 USD | 151.29 USD | 0.00 USD | `+22.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 310,990.00 USD | 2,050.00 USD | 0.00 USD | `+23.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 311,100.00 USD | 110.00 USD | 0.00 USD | `+24.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 311,570.00 USD | 475.80 USD | 0.00 USD | `+26.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 312,780.00 USD | 1,210.00 USD | 0.00 USD | `+27.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 355,710.00 USD | 42,930.00 USD | 0.00 USD | `+27.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 357,710.00 USD | 2,000.00 USD | 0.00 USD | `+31.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 359,090.00 USD | 1,380.00 USD | 0.00 USD | `+32.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 359,340.00 USD | 245.41 USD | 0.00 USD | `+35.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 367,730.00 USD | 8,390.00 USD | 0.00 USD | `+36.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 368,150.00 USD | 415.25 USD | 0.00 USD | `+38.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 374,670.00 USD | 6,520.00 USD | 0.00 USD | `+38.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 379,460.00 USD | 4,800.00 USD | 0.00 USD | `+39.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 380,120.00 USD | 655.75 USD | 0.00 USD | `+39.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 380,710.00 USD | 596.43 USD | 0.00 USD | `+41.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 382,530.00 USD | 1,810.00 USD | 0.00 USD | `+42.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 396,410.00 USD | 13,880.00 USD | 0.00 USD | `+42.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 397,670.00 USD | 1,250.00 USD | 0.00 USD | `+43.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 399,730.00 USD | 2,070.00 USD | 0.00 USD | `+47.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 399,870.00 USD | 140.05 USD | 0.00 USD | `+48.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 400,030.00 USD | 160.42 USD | 0.00 USD | `+48.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 400,990.00 USD | 954.32 USD | 0.00 USD | `+49.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 435,160.00 USD | 34,170.00 USD | 0.00 USD | `+52.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 436,040.00 USD | 879.84 USD | 0.00 USD | `+58.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 439,090.00 USD | 3,050.00 USD | 0.00 USD | `+60.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 439,390.00 USD | 297.27 USD | 0.00 USD | `+64.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 447,920.00 USD | 8,530.00 USD | 0.00 USD | `+75.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 448,070.00 USD | 143.99 USD | 0.00 USD | `+77.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 448,240.00 USD | 177.05 USD | 0.00 USD | `+87.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 448,680.00 USD | 431.40 USD | 0.00 USD | `+91.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 448,900.00 USD | 220.77 USD | 0.00 USD | `+92.97%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7700` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 5,060.00 USD | 1,600.00 USD | 5,080.00 USD |
| `7D` | `0.7720` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 4,990.00 USD | 0.00 USD | 2,230.00 USD |
| `7D` | `0.7740` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 5,450.00 USD | 0.00 USD | 3,310.00 USD |
| `7D` | `0.7760` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 147.66 USD |
| `7D` | `0.7780` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 0.00 USD | 3,100.00 USD | 53.43 USD |
| `7D` | `0.7800` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 436.65 USD | 25.30 USD | 0.00 USD |
| `7D` | `0.7820` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 0.00 USD | 1,920.00 USD | 1,410.00 USD |
| `7D` | `0.7840` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 227.10 USD | 1,190.00 USD | 0.00 USD |
| `7D` | `0.7860` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 0.00 USD | 2,250.00 USD | 365.01 USD |
| `7D` | `0.7880` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 5,690.00 USD | 2,050.00 USD | 723.49 USD |
| `7D` | `0.7900` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 6,940.00 USD | 2,650.00 USD | 4,030.00 USD |
| `7D` | `0.7920` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 12,590.00 USD | 2,180.00 USD | 10,760.00 USD |
| `7D` | `0.7940` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 15,680.00 USD | 2,500.00 USD | 13,480.00 USD |
| `7D` | `0.7960` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 4,520.00 USD | 7,120.00 USD | 3,290.00 USD |
| `7D` | `0.7980` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 16,210.00 USD | 3,000.00 USD | 14,230.00 USD |
| `7D` | `0.8000` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 10,100.00 USD | 5,540.00 USD | 2,430.00 USD |
| `7D` | `0.8020` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 8,990.00 USD | 4,460.00 USD | 9,540.00 USD |
| `7D` | `0.8040` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 5,500.00 USD | 2,170.00 USD | 940.33 USD |
| `7D` | `0.8060` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 16,390.00 USD | 10,990.00 USD | 10,100.00 USD |
| `7D` | `0.8080` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 1,570.00 USD | 1,230.00 USD | 10,210.00 USD |
| `7D` | `0.8100` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 2,890.00 USD | 2,010.00 USD | 4,690.00 USD |
| `7D` | `0.8120` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 15,720.00 USD | 3,030.00 USD | 9,400.00 USD |
| `7D` | `0.8140` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 32,880.00 USD | 6,050.00 USD | 15,910.00 USD |
| `7D` | `0.8160` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 38,200.00 USD | 10,180.00 USD | 6,010.00 USD |
| `7D` | `0.8180` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 12,550.00 USD | 2,560.00 USD | 11,440.00 USD |
| `7D` | `0.8200` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 1,740.00 USD | 1,570.00 USD | 7,460.00 USD |
| `7D` | `0.8220` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 20,390.00 USD | 6,820.00 USD | 4,490.00 USD |
| `7D` | `0.8240` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 23,160.00 USD | 93.73 USD | 11,990.00 USD |
| `7D` | `0.8260` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 5,220.00 USD | 3,490.00 USD | 1,560.00 USD |
| `7D` | `0.8280` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 0.00 USD | 3,910.00 USD | 1,040.00 USD |
| `7D` | `0.8300` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 9,280.00 USD | 4,780.00 USD | 2,450.00 USD |
| `7D` | `0.8320` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 0.00 USD | 401.80 USD | 77.95 USD |
| `1D` | `0.8330` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 28,220.00 USD | 3,030.00 USD | 7,110.00 USD |
| `7D` | `0.8340` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 35,710.00 USD | 10,960.00 USD | 1,980.00 USD |
| `1D` | `0.8350` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 0.00 USD | 4,750.00 USD | 11,120.00 USD |
| `7D` | `0.8360` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 0.00 USD | 844.23 USD | 311.26 USD |
| `1D` | `0.8370` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 18,030.00 USD | 2,360.00 USD | 9,180.00 USD |
| `7D` | `0.8380` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 15,240.00 USD | 633.60 USD | 539.92 USD |
| `1D` | `0.8390` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 671.95 USD | 745.84 USD | 1,400.00 USD |
| `7D` | `0.8400` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 0.00 USD | 798.38 USD | 8,060.00 USD |
| `1D` | `0.8410` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 0.00 USD | 449.73 USD | 933.95 USD |
| `7D` | `0.8420` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 6,400.00 USD | 4,650.00 USD | 4,060.00 USD |
| `1D` | `0.8430` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 1,590.00 USD | 4,690.00 USD | 0.00 USD |
| `7D` | `0.8440` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 7,170.00 USD | 24.80 USD | 0.00 USD |
| `1D` | `0.8450` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 2,200.00 USD | 6,340.00 USD | 25.04 USD |
| `7D` | `0.8460` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 2,560.00 USD | 427.62 USD | 2,660.00 USD |
| `1D` | `0.8470` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 21,360.00 USD | 417.76 USD | 0.00 USD |
| `7D` | `0.8480` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 26,310.00 USD | 10,990.00 USD | 0.00 USD |
| `1D` | `0.8490` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 2,500.00 USD | 142.65 USD | 537.83 USD |
| `7D` | `0.8500` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 2,050.00 USD | 477.96 USD | 4,430.00 USD |
| `1D` | `0.8510` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 6,130.00 USD | 2,240.00 USD | 7,400.00 USD |
| `7D` | `0.8520` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 5,900.00 USD | 669.43 USD | 226.67 USD |
| `1D` | `0.8530` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 1,410.00 USD | 2,440.00 USD | 4,980.00 USD |
| `7D` | `0.8540` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 254.55 USD | 2,660.00 USD | 5,540.00 USD |
| `1D` | `0.8550` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 17,960.00 USD | 2,470.00 USD | 4,920.00 USD |
| `7D` | `0.8560` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 0.00 USD | 842.92 USD | 2,180.00 USD |
| `1D` | `0.8570` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 739.96 USD | 445.99 USD | 2,210.00 USD |
| `7D` | `0.8580` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 3,540.00 USD | 101.30 USD | 1,270.00 USD |
| `1D` | `0.8590` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 5,620.00 USD | 10,610.00 USD | 2,940.00 USD |
| `7D` | `0.8600` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 5,820.00 USD | 211.77 USD | 383.26 USD |
| `1D` | `0.8610` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 7,980.00 USD | 855.53 USD | 13,690.00 USD |
| `7D` | `0.8620` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 7,670.00 USD | 6,050.00 USD | 26,880.00 USD |
| `1D` | `0.8630` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 39,330.00 USD | 12,290.00 USD | 2,010.00 USD |
| `7D` | `0.8640` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 4,820.00 USD | 321.30 USD | 0.00 USD |
| `1D` | `0.8650` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 17,640.00 USD | 2,110.00 USD | 1,790.00 USD |
| `7D` | `0.8660` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 45,020.00 USD | 19,050.00 USD | 2,170.00 USD |
| `1D` | `0.8670` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 11,890.00 USD | 10,090.00 USD | 1,110.00 USD |
| `7D` | `0.8680` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 92,530.00 USD | 14,760.00 USD | 50,800.00 USD |
| `1D` | `0.8690` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 41,960.00 USD | 3,780.00 USD | 29,400.00 USD |
| `7D` | `0.8700` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 81,840.00 USD | 9,460.00 USD | 7,550.00 USD |
| `1D` | `0.8710` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 42,250.00 USD | 24,870.00 USD | 28,630.00 USD |
| `7D` | `0.8720` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 5,420.00 USD | 18,020.00 USD | 11,450.00 USD |
| `1D` | `0.8730` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 54,380.00 USD | 21,510.00 USD | 25,960.00 USD |
| `7D` | `0.8740` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 0.00 USD | 12,360.00 USD | 3,200.00 USD |
| `1D` | `0.8750` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 38,730.00 USD | 7,110.00 USD | 19,010.00 USD |
| `7D` | `0.8760` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 766.43 USD | 0.00 USD | 5,750.00 USD |
| `1D` | `0.8770` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 10,480.00 USD | 493.34 USD | 2,530.00 USD |
| `7D` | `0.8780` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 1,500.00 USD | 0.00 USD | 33,650.00 USD |
| `1D` | `0.8790` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 53,150.00 USD |
| `7D` | `0.8800` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 0.00 USD | 5,580.00 USD | 51,030.00 USD |
| `1D` | `0.8810` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 10,360.00 USD | 5,040.00 USD | 7,750.00 USD |
| `7D` | `0.8820` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 454.20 USD | 9,500.00 USD | 0.00 USD |
| `1D` | `0.8830` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 612.60 USD | 5,570.00 USD | 0.00 USD |
| `7D` | `0.8840` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 2,090.00 USD | 6,440.00 USD | 15,690.00 USD |
| `1D` | `0.8850` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 5,780.00 USD | 36,160.00 USD | 11,180.00 USD |
| `7D` | `0.8860` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 141,730.00 USD | 22,320.00 USD | 78,280.00 USD |
| `1D` | `0.8870` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 67,940.00 USD | 19,040.00 USD | 32,750.00 USD |
| `7D` | `0.8880` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 130,140.00 USD | 31,410.00 USD | 9,920.00 USD |
| `1D` | `0.8890` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 68,270.00 USD | 40,810.00 USD | 4,860.00 USD |
| `7D` | `0.8900` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 106,830.00 USD | 45,590.00 USD | 30,420.00 USD |
| `1D` | `0.8910` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 0.00 USD | 38,660.00 USD | 20,050.00 USD |
| `7D` | `0.8920` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 46,210.00 USD | 38,810.00 USD | 14,520.00 USD |
| `1D` | `0.8930` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 56,810.00 USD | 24,630.00 USD | 37,920.00 USD |
| `7D` | `0.8940` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 45,210.00 USD | 12,120.00 USD | 26,470.00 USD |
| `1D` | `0.8950` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 4,110.00 USD | 15,360.00 USD | 5,670.00 USD |
| `7D` | `0.8960` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 0.00 USD | 32,500.00 USD | 93,060.00 USD |
| `1D` | `0.8970` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 0.00 USD | 24,290.00 USD | 16,170.00 USD |
| `7D` | `0.8980` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 0.00 USD | 17,870.00 USD | 0.00 USD |
| `1D` | `0.8990` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 0.00 USD | 15,840.00 USD | 0.00 USD |
| `7D` | `0.9000` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 0.00 USD | 22,600.00 USD | 0.00 USD |
| `1D` | `0.9010` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 538.90 USD | 20,040.00 USD | 1,590.00 USD |
| `7D` | `0.9020` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 0.00 USD | 44,210.00 USD | 23,430.00 USD |
| `1D` | `0.9030` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 988.10 USD | 15,830.00 USD | 17,810.00 USD |
| `7D` | `0.9040` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 0.00 USD | 12,290.00 USD | 0.00 USD |
| `1D` | `0.9050` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 12,640.00 USD | 5,250.00 USD | 254.51 USD |
| `1D` | `0.9070` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 17,190.00 USD | 1,670.00 USD | 7,590.00 USD |
| `1D` | `0.9090` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 0.00 USD | 4,890.00 USD | 176.94 USD |
| `1D` | `0.9110` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 22,990.00 USD | 0.00 USD | 340.10 USD |
| `1D` | `0.9130` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 8,180.00 USD | 5,750.00 USD | 10,610.00 USD |
| `7D` | `0.9140` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 0.00 USD | 515.41 USD | 20,720.00 USD |
| `1D` | `0.9150` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 0.00 USD | 5,860.00 USD | 10,020.00 USD |
| `1D` | `0.9170` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 0.00 USD | 79.80 USD | 1,230.00 USD |
| `1D` | `0.9190` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 537.83 USD |
| `7D` | `0.9200` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 3,970.00 USD |
| `1D` | `0.9210` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 5,710.00 USD | 0.00 USD | 3,170.00 USD |
| `7D` | `0.9220` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 152,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9230` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 0.00 USD | 4,160.00 USD | 48.22 USD |
| `7D` | `0.9240` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 145,560.00 USD | 12,790.00 USD | 29,500.00 USD |
| `1D` | `0.9250` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 78,840.00 USD | 42,820.00 USD | 27,740.00 USD |
| `7D` | `0.9260` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 0.00 USD | 32,300.00 USD | 0.00 USD |
| `1D` | `0.9270` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 13,430.00 USD | 778.79 USD | 34,800.00 USD |
| `7D` | `0.9280` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 0.00 USD | 24,550.00 USD | 1,600.00 USD |
| `1D` | `0.9290` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 64,620.00 USD | 13,490.00 USD | 35,920.00 USD |
| `1D` | `0.9310` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 0.00 USD | 16.72 USD | 4,450.00 USD |
| `7D` | `0.9320` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 37,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9330` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 6,540.00 USD | 10,870.00 USD | 18,270.00 USD |
| `7D` | `0.9340` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 0.00 USD | 11,160.00 USD | 768.64 USD |
| `1D` | `0.9350` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 143,100.00 USD | 19,960.00 USD | 15,610.00 USD |
| `7D` | `0.9360` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 8,250.00 USD | 0.00 USD | 1,760.00 USD |
| `1D` | `0.9370` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 55,450.00 USD | 39,710.00 USD | 9,850.00 USD |
| `7D` | `0.9380` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 42,660.00 USD | 19,540.00 USD | 27,700.00 USD |
| `1D` | `0.9390` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 59,780.00 USD | 29,470.00 USD | 0.00 USD |
| `7D` | `0.9400` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 75,540.00 USD | 32,570.00 USD | 47,300.00 USD |
| `1D` | `0.9410` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 110,670.00 USD | 21,700.00 USD | 18,630.00 USD |
| `7D` | `0.9420` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 106,320.00 USD | 7,050.00 USD | 8,580.00 USD |
| `1D` | `0.9430` | 939,380.00 USD | 0.00 USD | 939,380.00 USD | 68,020.00 USD | 27,400.00 USD | 31,420.00 USD |
| `7D` | `0.9440` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 102,440.00 USD | 49,100.00 USD | 57,320.00 USD |
| `1D` | `0.9450` | 812,540.00 USD | 0.00 USD | 812,540.00 USD | 165,230.00 USD | 40,480.00 USD | 34,210.00 USD |
| `7D` | `0.9460` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 286,390.00 USD | 27,270.00 USD | 67,290.00 USD |
| `1D` | `0.9470` | 572,610.00 USD | 0.00 USD | 572,610.00 USD | 118,040.00 USD | 35,120.00 USD | 73,730.00 USD |
| `7D` | `0.9480` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 193,280.00 USD | 10,340.00 USD | 95,080.00 USD |
| `1D` | `0.9490` | 345,720.00 USD | 0.00 USD | 345,720.00 USD | 119,310.00 USD | 17,950.00 USD | 45,720.00 USD |
| `7D` | `0.9500` | 852,490.00 USD | 0.00 USD | 852,490.00 USD | 196,070.00 USD | 18,830.00 USD | 166,730.00 USD |
| `1D` | `0.9510` | 162,730.00 USD | 0.00 USD | 162,730.00 USD | 56,640.00 USD | 13,290.00 USD | 0.00 USD |
| `7D` | `0.9520` | 470,860.00 USD | 0.00 USD | 470,860.00 USD | 175,720.00 USD | 9,750.00 USD | 142,330.00 USD |
| `1D` | `0.9530` | 92,810.00 USD | 0.00 USD | 92,810.00 USD | 39,160.00 USD | 12,410.00 USD | 0.00 USD |
| `7D` | `0.9540` | 143,060.00 USD | 0.00 USD | 143,060.00 USD | 0.00 USD | 9,460.00 USD | 105,500.00 USD |
| `1D` | `0.9550` | 41,230.00 USD | 0.00 USD | 41,230.00 USD | 18,340.00 USD | 22,890.00 USD | 0.00 USD |
| `7D` | `0.9560` | 28,100.00 USD | 0.00 USD | 28,100.00 USD | 0.00 USD | 28,100.00 USD | 0.00 USD |
| `1D` | `0.9570` | 9,130.00 USD | 9,130.00 USD | 0.00 USD | 3,780.00 USD | 5,070.00 USD | 275.27 USD |
| `1D` | `0.9570` | 18,270.00 USD | 18,270.00 USD | 0.00 USD | 3,780.00 USD | 5,070.00 USD | 275.27 USD |
| `7D` | `0.9570` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9580` | 22,670.00 USD | 22,670.00 USD | 0.00 USD | 3,880.00 USD | 6,110.00 USD | 12,670.00 USD |
| `1D` | `0.9590` | 51,920.00 USD | 51,920.00 USD | 0.00 USD | 6,920.00 USD | 13,740.00 USD | 12,990.00 USD |
| `7D` | `0.9600` | 45,890.00 USD | 45,890.00 USD | 0.00 USD | 17,690.00 USD | 4,660.00 USD | 866.69 USD |
| `1D` | `0.9610` | 77,450.00 USD | 77,450.00 USD | 0.00 USD | 8,160.00 USD | 8,480.00 USD | 8,900.00 USD |
| `7D` | `0.9620` | 80,510.00 USD | 80,510.00 USD | 0.00 USD | 17,990.00 USD | 16,630.00 USD | 0.00 USD |
| `1D` | `0.9630` | 179,350.00 USD | 179,350.00 USD | 0.00 USD | 80,900.00 USD | 10,170.00 USD | 10,820.00 USD |
| `7D` | `0.9640` | 195,420.00 USD | 195,420.00 USD | 0.00 USD | 95,370.00 USD | 7,500.00 USD | 12,040.00 USD |
| `1D` | `0.9650` | 248,230.00 USD | 248,230.00 USD | 0.00 USD | 2,580.00 USD | 26,060.00 USD | 40,240.00 USD |
| `7D` | `0.9660` | 206,420.00 USD | 206,420.00 USD | 0.00 USD | 5,050.00 USD | 5,170.00 USD | 778.15 USD |
| `1D` | `0.9670` | 318,730.00 USD | 318,730.00 USD | 0.00 USD | 37,640.00 USD | 9,780.00 USD | 23,080.00 USD |
| `7D` | `0.9680` | 250,380.00 USD | 250,380.00 USD | 0.00 USD | 38,090.00 USD | 5,870.00 USD | 0.00 USD |
| `1D` | `0.9690` | 346,900.00 USD | 346,900.00 USD | 0.00 USD | 12,270.00 USD | 7,500.00 USD | 8,390.00 USD |
| `7D` | `0.9700` | 311,020.00 USD | 311,020.00 USD | 0.00 USD | 0.00 USD | 30,140.00 USD | 30,500.00 USD |
| `1D` | `0.9710` | 401,470.00 USD | 401,470.00 USD | 0.00 USD | 198.50 USD | 2,290.00 USD | 52,090.00 USD |
| `7D` | `0.9720` | 316,410.00 USD | 316,410.00 USD | 0.00 USD | 1,430.00 USD | 3,960.00 USD | 0.00 USD |
| `1D` | `0.9730` | 466,040.00 USD | 466,040.00 USD | 0.00 USD | 40,580.00 USD | 5,320.00 USD | 18,670.00 USD |
| `7D` | `0.9740` | 353,770.00 USD | 353,770.00 USD | 0.00 USD | 1,480.00 USD | 25,640.00 USD | 10,230.00 USD |
| `1D` | `0.9750` | 527,520.00 USD | 527,520.00 USD | 0.00 USD | 25,990.00 USD | 17,610.00 USD | 17,870.00 USD |
| `7D` | `0.9760` | 431,910.00 USD | 431,910.00 USD | 0.00 USD | 51,990.00 USD | 16,870.00 USD | 9,280.00 USD |
| `1D` | `0.9770` | 621,240.00 USD | 621,240.00 USD | 0.00 USD | 77,410.00 USD | 5,960.00 USD | 10,350.00 USD |
| `7D` | `0.9780` | 456,190.00 USD | 456,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,280.00 USD |
| `1D` | `0.9790` | 686,390.00 USD | 686,390.00 USD | 0.00 USD | 29,670.00 USD | 9,580.00 USD | 25,910.00 USD |
| `7D` | `0.9800` | 608,660.00 USD | 608,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 152,470.00 USD |
| `1D` | `0.9810` | 705,260.00 USD | 705,260.00 USD | 0.00 USD | 11,870.00 USD | 246.39 USD | 6,750.00 USD |
| `7D` | `0.9820` | 782,130.00 USD | 782,130.00 USD | 0.00 USD | 53,310.00 USD | 15,990.00 USD | 104,160.00 USD |
| `1D` | `0.9830` | 771,410.00 USD | 771,410.00 USD | 0.00 USD | 15,980.00 USD | 20,550.00 USD | 29,620.00 USD |
| `7D` | `0.9840` | 854,570.00 USD | 854,570.00 USD | 0.00 USD | 49,930.00 USD | 211.77 USD | 22,300.00 USD |
| `1D` | `0.9850` | 833,940.00 USD | 833,940.00 USD | 0.00 USD | 39,130.00 USD | 4,560.00 USD | 18,830.00 USD |
| `7D` | `0.9860` | 855,960.00 USD | 855,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,390.00 USD |
| `1D` | `0.9870` | 870,310.00 USD | 870,310.00 USD | 0.00 USD | 12,080.00 USD | 3,610.00 USD | 20,680.00 USD |
| `7D` | `0.9880` | 963,440.00 USD | 963,440.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 67,460.00 USD |
| `1D` | `0.9890` | 917,950.00 USD | 917,950.00 USD | 0.00 USD | 24,170.00 USD | 0.00 USD | 23,470.00 USD |
| `7D` | `0.9900` | 984,870.00 USD | 984,870.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 906.61 USD |
| `1D` | `0.9910` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 51,650.00 USD | 1,610.00 USD | 36,560.00 USD |
| `7D` | `0.9920` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 1,570.00 USD | 479.24 USD | 21,240.00 USD |
| `1D` | `0.9930` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 16,270.00 USD | 14,570.00 USD | 2,940.00 USD |
| `7D` | `0.9940` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 29,270.00 USD | 0.00 USD | 16,080.00 USD |
| `1D` | `0.9950` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 29,210.00 USD | 31.60 USD | 329.08 USD |
| `7D` | `0.9960` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 75,810.00 USD | 5,380.00 USD | 43,230.00 USD |
| `1D` | `0.9970` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 46,950.00 USD | 1,840.00 USD | 13,030.00 USD |
| `7D` | `0.9980` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 53,110.00 USD | 6,740.00 USD | 4,210.00 USD |
| `1D` | `0.9990` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 34,090.00 USD | 17,910.00 USD | 10,730.00 USD |
| `7D` | `1.00` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 462.12 USD |
| `1D` | `1.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 54,580.00 USD | 10,730.00 USD | 13,690.00 USD |
| `7D` | `1.00` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 54,650.00 USD | 21,850.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 10,110.00 USD | 9,280.00 USD | 6,140.00 USD |
| `7D` | `1.00` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 70,950.00 USD | 3,970.00 USD | 1,470.00 USD |
| `1D` | `1.00` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 54,780.00 USD | 5,480.00 USD | 5,820.00 USD |
| `7D` | `1.01` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 46,710.00 USD | 0.00 USD | 11,560.00 USD |
| `1D` | `1.01` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 47,140.00 USD | 11,610.00 USD | 53,290.00 USD |
| `7D` | `1.01` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44,430.00 USD |
| `1D` | `1.01` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 30,870.00 USD | 13,790.00 USD | 7,610.00 USD |
| `7D` | `1.01` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 10,260.00 USD | 14,180.00 USD | 0.00 USD |
| `1D` | `1.01` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 9,660.00 USD | 28,610.00 USD | 265.91 USD |
| `7D` | `1.01` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 33,230.00 USD | 30,100.00 USD | 0.00 USD |
| `1D` | `1.01` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 10,450.00 USD | 3,050.00 USD | 3,900.00 USD |
| `7D` | `1.01` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 2,870.00 USD | 28,450.00 USD | 735.11 USD |
| `1D` | `1.01` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 19,580.00 USD | 25,030.00 USD | 21,210.00 USD |
| `7D` | `1.02` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 526.60 USD | 28,470.00 USD | 11,910.00 USD |
| `1D` | `1.02` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 2,810.00 USD | 7,870.00 USD | 26,620.00 USD |
| `7D` | `1.02` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 25,010.00 USD | 21,560.00 USD |
| `1D` | `1.02` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 60,720.00 USD | 4,830.00 USD | 10,660.00 USD |
| `7D` | `1.02` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 33,820.00 USD | 84,220.00 USD | 44,250.00 USD |
| `1D` | `1.02` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 26,430.00 USD | 11,530.00 USD | 21,110.00 USD |
| `7D` | `1.02` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 56,930.00 USD | 52,610.00 USD | 112,030.00 USD |
| `1D` | `1.02` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 48,740.00 USD | 21,040.00 USD | 36,520.00 USD |
| `7D` | `1.02` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 78,220.00 USD | 56,700.00 USD | 86,740.00 USD |
| `1D` | `1.02` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 44,890.00 USD | 13,350.00 USD | 30,580.00 USD |
| `7D` | `1.03` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 22,650.00 USD | 124,880.00 USD | 33,130.00 USD |
| `1D` | `1.03` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 16,060.00 USD | 10,270.00 USD | 7,260.00 USD |
| `7D` | `1.03` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 250,310.00 USD | 50,530.00 USD | 24,480.00 USD |
| `1D` | `1.03` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 22,230.00 USD | 18,890.00 USD | 25,030.00 USD |
| `7D` | `1.03` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 134,200.00 USD | 33,660.00 USD | 19,120.00 USD |
| `1D` | `1.03` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 75,770.00 USD | 9,640.00 USD | 31,790.00 USD |
| `7D` | `1.03` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD |
| `1D` | `1.03` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 17,220.00 USD | 124.83 USD | 16,180.00 USD |
| `7D` | `1.03` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 217,210.00 USD | 8,290.00 USD | 4,310.00 USD |
| `1D` | `1.03` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 9,200.00 USD | 17,340.00 USD | 7,080.00 USD |
| `7D` | `1.04` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 262,550.00 USD | 3,170.00 USD | 42,930.00 USD |
| `1D` | `1.04` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 41,230.00 USD | 1,910.00 USD | 4,540.00 USD |
| `7D` | `1.04` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 178,400.00 USD | 1,290.00 USD | 199,090.00 USD |
| `1D` | `1.04` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 7,870.00 USD | 4,560.00 USD | 3,960.00 USD |
| `7D` | `1.04` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 279,840.00 USD | 9,430.00 USD | 93,080.00 USD |
| `1D` | `1.04` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 2,930.00 USD | 2,550.00 USD | 5,890.00 USD |
| `7D` | `1.04` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD |
| `1D` | `1.04` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 10,940.00 USD | 7,010.00 USD | 8,060.00 USD |
| `7D` | `1.04` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD |
| `1D` | `1.04` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 1,400.00 USD | 63.94 USD | 6,000.00 USD |
| `7D` | `1.05` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD |
| `1D` | `1.05` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 7,610.00 USD | 4,620.00 USD | 2,210.00 USD |
| `7D` | `1.05` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 199,320.00 USD | 28,070.00 USD | 161,420.00 USD |
| `1D` | `1.05` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 3,990.00 USD | 4,010.00 USD | 7,320.00 USD |
| `7D` | `1.05` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 91,750.00 USD | 29,070.00 USD | 40,740.00 USD |
| `1D` | `1.05` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 30,030.00 USD | 73.09 USD | 13,350.00 USD |
| `7D` | `1.05` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 140,530.00 USD | 49,780.00 USD | 134,080.00 USD |
| `1D` | `1.05` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 4,370.00 USD | 1,400.00 USD | 3,560.00 USD |
| `7D` | `1.05` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 88,940.00 USD | 44,290.00 USD | 36,750.00 USD |
| `1D` | `1.05` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 6,580.00 USD | 1,450.00 USD | 4,930.00 USD |
| `1D` | `1.06` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 5,670.00 USD | 3,070.00 USD | 0.00 USD |
| `7D` | `1.06` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 187,610.00 USD | 48,000.00 USD | 121,890.00 USD |
| `7D` | `1.06` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 205,690.00 USD | 63,350.00 USD | 94,840.00 USD |
| `7D` | `1.06` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 217,790.00 USD | 73,000.00 USD | 125,100.00 USD |
| `7D` | `1.06` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 131,720.00 USD | 83,000.00 USD | 66,000.00 USD |
| `7D` | `1.06` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 102,750.00 USD | 49,310.00 USD | 92,130.00 USD |
| `7D` | `1.07` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 77,920.00 USD | 32,860.00 USD | 73,060.00 USD |
| `7D` | `1.07` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 221,410.00 USD | 30,180.00 USD | 93,450.00 USD |
| `7D` | `1.07` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 121,300.00 USD | 33,170.00 USD | 42,800.00 USD |
| `7D` | `1.07` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 103,500.00 USD | 37,730.00 USD | 83,520.00 USD |
| `7D` | `1.07` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 92,440.00 USD | 21,500.00 USD | 83,440.00 USD |
| `7D` | `1.08` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 103,110.00 USD | 18,720.00 USD | 27,400.00 USD |
| `7D` | `1.08` | 9,760,000.00 USD | 9,760,000.00 USD | 0.00 USD | 158,650.00 USD | 40,740.00 USD | 69,670.00 USD |
| `7D` | `1.08` | 9,990,000.00 USD | 9,990,000.00 USD | 0.00 USD | 176,790.00 USD | 26,190.00 USD | 33,510.00 USD |
| `7D` | `1.08` | 10,120,000.00 USD | 10,120,000.00 USD | 0.00 USD | 62,710.00 USD | 20,510.00 USD | 39,030.00 USD |
| `7D` | `1.08` | 10,300,000.00 USD | 10,300,000.00 USD | 0.00 USD | 46,000.00 USD | 31,940.00 USD | 103,610.00 USD |
| `7D` | `1.09` | 10,530,000.00 USD | 10,530,000.00 USD | 0.00 USD | 161,270.00 USD | 28,200.00 USD | 42,090.00 USD |
| `7D` | `1.09` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 59,850.00 USD | 57,700.00 USD | 117,570.00 USD |
| `7D` | `1.09` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 109,670.00 USD | 18,350.00 USD | 31,220.00 USD |
| `7D` | `1.09` | 11,050,000.00 USD | 11,050,000.00 USD | 0.00 USD | 36,490.00 USD | 24,570.00 USD | 62,450.00 USD |
| `7D` | `1.09` | 11,210,000.00 USD | 11,210,000.00 USD | 0.00 USD | 67,090.00 USD | 37,290.00 USD | 55,440.00 USD |
| `7D` | `1.10` | 11,370,000.00 USD | 11,370,000.00 USD | 0.00 USD | 64,450.00 USD | 32,080.00 USD | 65,790.00 USD |
| `7D` | `1.10` | 11,610,000.00 USD | 11,610,000.00 USD | 0.00 USD | 119,850.00 USD | 21,050.00 USD | 97,790.00 USD |
| `7D` | `1.10` | 11,890,000.00 USD | 11,890,000.00 USD | 0.00 USD | 182,190.00 USD | 61,190.00 USD | 40,340.00 USD |
| `7D` | `1.10` | 11,960,000.00 USD | 11,960,000.00 USD | 0.00 USD | 59,740.00 USD | 10,900.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `177.02M` | Total OI Tokens: `185,664,054.7 DOT`
  * 1h OI Change: `+1.32%` | 4h OI Change: `-8.23%` | 24h OI Change: `-15.08%`
  * Exchange Breakdown: Binance=`35.19M` | Bybit=`22.23M` | OKX=`10.13M` | Hyperliquid=`5.92M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.86K` | Last 24h: `2.25K` | Last 3d: `-11.45K` | Last 7d: `-19.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0192%` |
| **USDT Bybit** | `0.0008%` | **USDT KuCoin** | `-0.0184%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0040%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-0.0003%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `39.58%` | `60.42%` | `0.66` | 15,010,000.00 USD |
| `15M` | `Binance` | `46.34%` | `53.66%` | `0.86` | 5,290,000.00 USD |
| `15M` | `OKX` | `43.79%` | `56.21%` | `0.78` | 2,440,000.00 USD |
| `15M` | `Bybit` | `32.65%` | `67.35%` | `0.48` | 2,300,000.00 USD |
| `15M` | `KuCoin` | `17.53%` | `82.47%` | `0.21` | 233,220.00 USD |
| `15M` | `Gate` | `41.08%` | `58.92%` | `0.70` | 282,060.00 USD |
| `15M` | `Bitget` | `27.77%` | `72.23%` | `0.38` | 1,060,000.00 USD |
| `15M` | `BingX` | `44.43%` | `55.57%` | `0.80` | 551,420.00 USD |
| `15M` | `MEXC` | `28.45%` | `71.55%` | `0.40` | 523,970.00 USD |
| `15M` | `Bitunix` | `23.83%` | `76.17%` | `0.31` | 620,130.00 USD |
| `15M` | `Hyperliquid` | `28.51%` | `71.49%` | `0.40` | 1,240,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.55%` | `53.45%` | `0.87` | 92,270.00 USD |
| `15M` | `Crypto.com` | `70.88%` | `29.12%` | `2.43` | 233.95 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 256,650.00 USD |
| `15M` | `HTX` | `33.3%` | `66.7%` | `0.50` | 7,420.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `10.62%` | `89.38%` | `0.12` | 56,560.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `27.93%` | `72.07%` | `0.39` | 68,430.00 USD |
| `15M` | `Whale Positions` | `46.34%` | `53.66%` | `0.86` | 5,290,000.00 USD |
| `15M` | `Global Accounts` | `39.58%` | `60.42%` | `0.66` | 15,010,000.00 USD |
| `1H` | `DOT` | `47.00%` | `53.00%` | `0.89` | 71,370,000.00 USD |
| `1H` | `Binance` | `45.1%` | `54.9%` | `0.82` | 26,590,000.00 USD |
| `1H` | `OKX` | `43.99%` | `56.01%` | `0.79` | 9,730,000.00 USD |
| `1H` | `Bybit` | `43.38%` | `56.62%` | `0.77` | 10,010,000.00 USD |
| `1H` | `KuCoin` | `31.48%` | `68.52%` | `0.46` | 543,060.00 USD |
| `1H` | `Gate` | `52.48%` | `47.52%` | `1.10` | 4,250,000.00 USD |
| `1H` | `Bitget` | `47.78%` | `52.22%` | `0.91` | 3,980,000.00 USD |
| `1H` | `BingX` | `54.87%` | `45.13%` | `1.22` | 3,020,000.00 USD |
| `1H` | `MEXC` | `52.74%` | `47.26%` | `1.12` | 2,750,000.00 USD |
| `1H` | `Bitunix` | `40.79%` | `59.21%` | `0.69` | 2,080,000.00 USD |
| `1H` | `Hyperliquid` | `50.6%` | `49.4%` | `1.02` | 6,070,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `46.23%` | `53.77%` | `0.86` | 373,410.00 USD |
| `1H` | `Crypto.com` | `47.54%` | `52.46%` | `0.91` | 3,830.00 USD |
| `1H` | `WhiteBIT` | `80.48%` | `19.52%` | `4.12` | 1,490,000.00 USD |
| `1H` | `HTX` | `45.09%` | `54.91%` | `0.82` | 19,900.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `46.66%` | `53.34%` | `0.87` | 118,460.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `47.13%` | `52.87%` | `0.89` | 344,480.00 USD |
| `1H` | `Whale Positions` | `45.1%` | `54.9%` | `0.82` | 26,590,000.00 USD |
| `1H` | `Global Accounts` | `47.00%` | `53.00%` | `0.89` | 71,370,000.00 USD |
| `4H` | `DOT` | `55.18%` | `44.82%` | `1.23` | 301,220,000.00 USD |
| `4H` | `Binance` | `53.2%` | `46.8%` | `1.14` | 122,260,000.00 USD |
| `4H` | `OKX` | `54.99%` | `45.01%` | `1.22` | 36,520,000.00 USD |
| `4H` | `Bybit` | `54.86%` | `45.14%` | `1.22` | 39,920,000.00 USD |
| `4H` | `KuCoin` | `48.92%` | `51.08%` | `0.96` | 2,080,000.00 USD |
| `4H` | `Gate` | `56.77%` | `43.23%` | `1.31` | 11,820,000.00 USD |
| `4H` | `Bitget` | `54.58%` | `45.42%` | `1.20` | 16,890,000.00 USD |
| `4H` | `BingX` | `58.41%` | `41.59%` | `1.40` | 16,320,000.00 USD |
| `4H` | `MEXC` | `54.65%` | `45.35%` | `1.21` | 9,810,000.00 USD |
| `4H` | `Bitunix` | `51.58%` | `48.42%` | `1.07` | 6,940,000.00 USD |
| `4H` | `Hyperliquid` | `58.73%` | `41.27%` | `1.42` | 27,580,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.52%` | `48.48%` | `1.06` | 1,660,000.00 USD |
| `4H` | `Crypto.com` | `50%` | `50%` | `1.00` | 19,920.00 USD |
| `4H` | `WhiteBIT` | `90.38%` | `9.62%` | `9.40` | 5,580,000.00 USD |
| `4H` | `HTX` | `52.11%` | `47.89%` | `1.09` | 210,340.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `68.01%` | `31.99%` | `2.13` | 541,620.00 USD |
| `4H` | `Aster` | `27.02%` | `72.98%` | `0.37` | 1,620,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.5%` | `48.5%` | `1.06` | 1,460,000.00 USD |
| `4H` | `Whale Positions` | `53.2%` | `46.8%` | `1.14` | 122,260,000.00 USD |
| `4H` | `Global Accounts` | `55.18%` | `44.82%` | `1.23` | 301,220,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.9247` | `0.9214` | `0.9247` | `0.9264` | `0.9171` | 592,145.67 USD | 331,376.92 USD | 260,768.76 USD | 70,608.16 USD | `+11.92%` | `20B / 3S` |
| `0:00 UTC` | `0.9301` | `0.9294` | `0.9301` | `0.9320` | `0.9246` | 722,739.41 USD | 436,845.68 USD | 285,893.73 USD | 150,951.95 USD | `+20.89%` | `15B / 5S` |
| `5:00 UTC` | `0.9322` | `0.9317` | `0.9322` | `0.9342` | `0.9301` | 515,769.04 USD | 235,727.30 USD | 280,041.74 USD | -44,314.44 USD | `-8.59%` | `11B / 7S` |
| `0:00 UTC` | `0.9301` | `0.9291` | `0.9301` | `0.9327` | `0.9264` | 525,506.21 USD | 261,479.52 USD | 264,026.69 USD | -2,547.17 USD | `-0.48%` | `9B / 12S` |
| `5:00 UTC` | `0.9325` | `0.9314` | `0.9325` | `0.9344` | `0.9288` | 497,143.85 USD | 263,231.22 USD | 233,912.62 USD | 29,318.60 USD | `+5.90%` | `7B / 6S` |
| `0:00 UTC` | `0.9354` | `0.9348` | `0.9354` | `0.9365` | `0.9333` | 404,247.05 USD | 223,080.64 USD | 181,166.41 USD | 41,914.22 USD | `+10.37%` | `5B / 3S` |
| `5:00 UTC` | `0.9425` | `0.9411` | `0.9425` | `0.9454` | `0.9362` | 1,398,502.73 USD | 702,262.50 USD | 696,240.23 USD | 6,022.27 USD | `+0.43%` | `30B / 12S` |
| `0:00 UTC` | `0.9563` | `0.9497` | `0.9563` | `0.9570` | `0.9410` | 1,155,581.71 USD | 451,950.39 USD | 703,631.31 USD | -251,680.92 USD | `-21.78%` | `29B / 39S` |
| `5:00 UTC` | `0.9533` | `0.9521` | `0.9533` | `0.9545` | `0.9487` | 564,921.36 USD | 209,867.72 USD | 355,053.64 USD | -145,185.92 USD | `-25.70%` | `9B / 14S` |
| `0:00 UTC` | `0.9519` | `0.9541` | `0.9519` | `0.9570` | `0.9510` | 387,852.31 USD | 148,454.01 USD | 239,398.31 USD | -90,944.30 USD | `-23.45%` | `10B / 16S` |

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
| `5m` | -25,790.00 USD | -66,630.00 USD | **`DISTRIBUTION`** |
| `15m` | -65,550.00 USD | -226,560.00 USD | **`DISTRIBUTION`** |
| `30m` | -47,570.00 USD | -501,250.00 USD | **`DISTRIBUTION`** |
| `1h` | -18,570.00 USD | -801,630.00 USD | **`DISTRIBUTION`** |
| `2h` | 12,670.00 USD | -545,800.00 USD | **`DISTRIBUTION`** |
| `4h` | 2,190.00 USD | -1,180.00 USD | **`ACCUMULATION`** |
| `6h` | -325,580.00 USD | 496,100.00 USD | **`ACCUMULATION`** |
| `8h` | -184,480.00 USD | -5,060,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,150,000.00 USD | -6,050,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,190,000.00 USD | -6,700,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,060,000.00 USD | -23,340,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,640,000.00 USD | -77,830,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-25.79K` | 15m=`-65.55K` | 1h=`-18.57K` | 24h=`-1.19M`
* Futures Capital Netflows: 5m=`-66.63K` | 15m=`-226.56K` | 1h=`-801.63K` | 24h=`-6.70M`
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
  * `2026-10-30 11:03:23 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:09:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:10:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.8919` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-0.3381` (Risk Distance: `1.23` pts)
  * +2.5R Take Profit: `3.97`
  * Mathematical Lot Sizing: **`8.13 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9253` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2.16` (Risk Distance: `1.23` pts)
  * +2.5R Take Profit: `-2.15`
  * Mathematical Lot Sizing: **`8.13 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9586`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
