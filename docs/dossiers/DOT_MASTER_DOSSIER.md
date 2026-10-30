# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 11:41:29 IST` (`2026-10-30 06:11:29 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9350` | **Live Ask Quote**: `0.9560` | **Mid Price**: `0.9455`
- **Spread Points**: `21.00` | **Spread BPS**: `222.10 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.9009` | VWAP Z-Score: `+1.84` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0092` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `64.40` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.9646` | Lower -3.00σ Band: `0.8371`
  * Upper +2.51σ Band: `0.9542` | Lower -2.51σ Band: `0.8475`
  * Upper +2.01σ Band: `0.9436` | Lower -2.01σ Band: `0.8582`
  * Upper +2.00σ Band: `0.9433` | Lower -2.00σ Band: `0.8584`
  * Upper +1.28σ Band: `0.9280` | Lower -1.28σ Band: `0.8737`
  * Upper +1.00σ Band: `0.9221` | Lower -1.00σ Band: `0.8796`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9318` | EMA-20=`0.9231` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9289` (Slope: `+0.0000`) | EMA-100=`0.9447`
  * Institutional Anchors: EMA-144=`0.9533` | EMA-200=`0.9605` (Slope: `-0.4459`) | EMA-233=`0.9644`
- **Range Boundaries**: 24H High=`1.01` | 24H Low=`0.8570` | Weekly High=`1.03` | Weekly Low=`0.8570`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9259` (Distance: `+2.07%`)
  * Point of Control (POC) = `0.9119` (Distance: `+3.63%`)
  * Value Area Low (VAL) = `0.8901` (Distance: `+6.17%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.02` | Weekly POC=`0.9945` | Weekly VAL=`0.9713`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9330` | Low=`0.8570`
  * London Session (08:00-16:00 UTC): High=`0.9480` | Low=`0.9290`
  * New York Session (13:00-21:00 UTC): High=`0.9512` | Low=`0.9398`
  * Initial Balance (First Hour): IB High=`0.9480` | IB Low=`0.9290`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9417` - `0.9493`
  * Optimal Trade Entry (OTE 0.705): `0.9474`
  * Structural Invalidation Anchor (0.786): `0.9531`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9520` | `0.9539` | `0.9510` | `0.9527` | `196,314` | 187,023.98 USD | -26,892.25 USD | `-14.38%` | -3,794,345.51 USD | `-0.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.9528` | `0.9570` | `0.9527` | `0.9545` | `200,600` | 191,638.99 USD | -63,314.41 USD | `-33.04%` | -3,857,659.92 USD | `-0.83` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.9546` | `0.9565` | `0.9532` | `0.9556` | `148,560` | 141,818.22 USD | 2,885.65 USD | `+2.03%` | -3,854,774.27 USD | `+0.40` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.9428` | `0.9570` | `0.9410` | `0.9497` | `1,216,863` | 1,155,581.71 USD | -251,680.92 USD | `-21.78%` | -3,622,267.34 USD | `-0.58` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.9496` | `0.9544` | `0.9487` | `0.9519` | `593,394` | 564,921.36 USD | -145,185.92 USD | `-25.70%` | -3,767,453.26 USD | `-0.50` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.9520` | `0.9570` | `0.9510` | `0.9558` | `547,316` | 522,242.59 USD | -87,472.37 USD | `-16.75%` | -3,854,925.63 USD | `-0.39` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9176` | `0.9341` | `0.9170` | `0.9318` | `3,070,214` | 2,839,814.60 USD | -92,909.79 USD | `-3.27%` | -3,396,468.88 USD | `+0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9318` | `0.9453` | `0.9263` | `0.9427` | `3,017,884` | 2,825,399.84 USD | 74,707.92 USD | `+2.64%` | -3,321,760.96 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9428` | `0.9570` | `0.9410` | `0.9556` | `2,355,730` | 2,240,984.27 USD | -484,187.85 USD | `-21.61%` | -3,805,948.81 USD | `-0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,414,306.57 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,007,919.25 USD | `+1.11` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9570` | `0.9263` | `0.9558` | `5,375,457` | 5,068,145.50 USD | -409,631.29 USD | `-8.08%` | -4,417,550.53 USD | `+0.18` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | -92,512.40 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -889,577.85 USD | `-1.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,414,306.57 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,007,919.25 USD | `+1.11` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9603` | `0.9263` | `0.9521` | `6,155,888` | 5,814,384.25 USD | -386,098.70 USD | `-6.64%` | -4,394,017.94 USD | `+0.19` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`0.9455`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:33:47 IST` |

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
| `Live` | `Long Liquidation` | `0.2235` | 111.75 USD | 469,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3575` | 789.72 USD | 468,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4055` | 2,310.00 USD | 468,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4195` | 2,800.00 USD | 465,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4495` | 1,180.00 USD | 463,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4675` | 146.70 USD | 461,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4705` | 2,590.00 USD | 461,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4875` | 195.34 USD | 459,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5065` | 3,290.00 USD | 458,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5385` | 538.50 USD | 455,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5405` | 141.67 USD | 455,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5515` | 218.67 USD | 454,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 14,600.00 USD | 454,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 577.36 USD | 440,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 683.51 USD | 439,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 137.53 USD | 438,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6055` | 1,480.00 USD | 438,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6075` | 1,810.00 USD | 437,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 105.96 USD | 435,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 147.48 USD | 435,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 757.80 USD | 435,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 106.00 USD | 434,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 507.86 USD | 434,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 2,090.00 USD | 433,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 20,270.00 USD | 431,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 4,230.00 USD | 411,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 202.47 USD | 407,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6555` | 521.19 USD | 407,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 149.44 USD | 406,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 63,890.00 USD | 406,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6755` | 84,440.00 USD | 342,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 423.10 USD | 258,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 512.97 USD | 257,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6905` | 19,770.00 USD | 257,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 478.22 USD | 237,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7005` | 1,140.00 USD | 236,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 988.87 USD | 235,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7215` | 1,580.00 USD | 234,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 397.93 USD | 233,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 291.18 USD | 232,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 2,300.00 USD | 232,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,140.00 USD | 230,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 283.30 USD | 229,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 2,220.00 USD | 228,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7545` | 1,400.00 USD | 226,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 9,980.00 USD | 225,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7635` | 308.00 USD | 215,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7655` | 54,350.00 USD | 214,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7720` | 3,910,000.00 USD | 3,910,000.00 USD | 10,530.00 USD | 1,600.00 USD | 7,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7725` | 3,840.00 USD | 160,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7740` | 3,890,000.00 USD | 3,890,000.00 USD | 5,450.00 USD | 0.00 USD | 3,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7760` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 147.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7775` | 2,490.00 USD | 156,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7780` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 3,100.00 USD | 53.43 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7795` | 272.83 USD | 154,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7800` | 3,880,000.00 USD | 3,880,000.00 USD | 436.65 USD | 25.30 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7820` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 1,920.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7840` | 3,870,000.00 USD | 3,870,000.00 USD | 227.10 USD | 1,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7860` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 2,250.00 USD | 365.01 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7865` | 292.03 USD | 153,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7880` | 3,870,000.00 USD | 3,870,000.00 USD | 5,690.00 USD | 2,050.00 USD | 723.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7900` | 3,860,000.00 USD | 3,860,000.00 USD | 6,940.00 USD | 2,650.00 USD | 4,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 277.39 USD | 153,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7920` | 3,850,000.00 USD | 3,850,000.00 USD | 12,590.00 USD | 2,180.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7940` | 3,820,000.00 USD | 3,820,000.00 USD | 15,680.00 USD | 2,500.00 USD | 13,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7960` | 3,790,000.00 USD | 3,790,000.00 USD | 4,520.00 USD | 7,120.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7980` | 3,780,000.00 USD | 3,780,000.00 USD | 16,210.00 USD | 3,000.00 USD | 14,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8000` | 3,740,000.00 USD | 3,740,000.00 USD | 10,100.00 USD | 5,540.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8020` | 3,720,000.00 USD | 3,720,000.00 USD | 8,990.00 USD | 4,460.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8040` | 3,700,000.00 USD | 3,700,000.00 USD | 5,500.00 USD | 2,170.00 USD | 940.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8060` | 3,690,000.00 USD | 3,690,000.00 USD | 16,390.00 USD | 10,990.00 USD | 10,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8080` | 3,650,000.00 USD | 3,650,000.00 USD | 1,570.00 USD | 1,230.00 USD | 10,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8100` | 3,640,000.00 USD | 3,640,000.00 USD | 2,890.00 USD | 2,010.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8120` | 3,630,000.00 USD | 3,630,000.00 USD | 15,720.00 USD | 3,030.00 USD | 9,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 153,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8140` | 3,600,000.00 USD | 3,600,000.00 USD | 32,880.00 USD | 6,050.00 USD | 15,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8160` | 3,550,000.00 USD | 3,550,000.00 USD | 38,200.00 USD | 10,180.00 USD | 6,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8180` | 3,490,000.00 USD | 3,490,000.00 USD | 12,550.00 USD | 2,560.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8200` | 3,470,000.00 USD | 3,470,000.00 USD | 1,740.00 USD | 1,570.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 152,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8220` | 3,460,000.00 USD | 3,460,000.00 USD | 20,390.00 USD | 6,820.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 749.96 USD | 150,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8240` | 3,430,000.00 USD | 3,430,000.00 USD | 23,160.00 USD | 93.73 USD | 11,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8260` | 3,390,000.00 USD | 3,390,000.00 USD | 5,220.00 USD | 3,490.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8280` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 3,910.00 USD | 1,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8300` | 3,380,000.00 USD | 3,380,000.00 USD | 9,280.00 USD | 4,780.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8320` | 2,750,000.00 USD | 2,750,000.00 USD | 2,670.00 USD | 1,950.00 USD | 3,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8320` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 401.80 USD | 77.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8340` | 2,740,000.00 USD | 2,740,000.00 USD | 25,550.00 USD | 5,650.00 USD | 8,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8340` | 3,360,000.00 USD | 3,360,000.00 USD | 35,710.00 USD | 10,960.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8360` | 2,700,000.00 USD | 2,700,000.00 USD | 1,870.00 USD | 636.81 USD | 14,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8360` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 844.23 USD | 311.26 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 149,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8380` | 2,690,000.00 USD | 2,690,000.00 USD | 16,380.00 USD | 1,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8380` | 3,310,000.00 USD | 3,310,000.00 USD | 15,240.00 USD | 633.60 USD | 539.92 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8400` | 2,670,000.00 USD | 2,670,000.00 USD | 458.00 USD | 1,050.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8400` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 798.38 USD | 8,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,570.00 USD | 149,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 2,660,000.00 USD | 2,660,000.00 USD | 1,340.00 USD | 4,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8420` | 3,280,000.00 USD | 3,280,000.00 USD | 6,400.00 USD | 4,650.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8440` | 2,660,000.00 USD | 2,660,000.00 USD | 2,210.00 USD | 5.65 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8440` | 3,270,000.00 USD | 3,270,000.00 USD | 7,170.00 USD | 24.80 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8460` | 2,660,000.00 USD | 2,660,000.00 USD | 15,140.00 USD | 6,600.00 USD | 25.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8460` | 3,260,000.00 USD | 3,260,000.00 USD | 2,560.00 USD | 427.62 USD | 2,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8480` | 2,630,000.00 USD | 2,630,000.00 USD | 6,670.00 USD | 230.58 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8480` | 3,260,000.00 USD | 3,260,000.00 USD | 26,310.00 USD | 10,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 148,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 2,630,000.00 USD | 2,630,000.00 USD | 8,440.00 USD | 371.56 USD | 744.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8500` | 3,220,000.00 USD | 3,220,000.00 USD | 2,050.00 USD | 477.96 USD | 4,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8515` | 2,700.00 USD | 146,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8520` | 2,620,000.00 USD | 2,620,000.00 USD | 1,230.00 USD | 1,940.00 USD | 12,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8520` | 3,210,000.00 USD | 3,210,000.00 USD | 5,900.00 USD | 669.43 USD | 226.67 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8540` | 2,600,000.00 USD | 2,600,000.00 USD | 2,300.00 USD | 4,910.00 USD | 4,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8540` | 3,200,000.00 USD | 3,200,000.00 USD | 254.55 USD | 2,660.00 USD | 5,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8560` | 2,590,000.00 USD | 2,590,000.00 USD | 16,210.00 USD | 306.64 USD | 880.90 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8560` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 842.92 USD | 2,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 144,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8580` | 2,570,000.00 USD | 2,570,000.00 USD | 2,870.00 USD | 209.22 USD | 8,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8580` | 3,190,000.00 USD | 3,190,000.00 USD | 3,540.00 USD | 101.30 USD | 7,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8595` | 180.75 USD | 143,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8600` | 2,560,000.00 USD | 2,560,000.00 USD | 7,990.00 USD | 10,610.00 USD | 18,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8600` | 3,180,000.00 USD | 3,180,000.00 USD | 6,780.00 USD | 211.77 USD | 10,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8620` | 2,520,000.00 USD | 2,520,000.00 USD | 12,920.00 USD | 12,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8620` | 3,160,000.00 USD | 3,160,000.00 USD | 7,670.00 USD | 6,050.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 143,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 2,500,000.00 USD | 2,500,000.00 USD | 48,740.00 USD | 2,370.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8640` | 3,120,000.00 USD | 3,120,000.00 USD | 4,820.00 USD | 321.30 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 143,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8660` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8660` | 3,120,000.00 USD | 3,120,000.00 USD | 45,020.00 USD | 19,050.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,390.00 USD | 142,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8680` | 2,440,000.00 USD | 2,440,000.00 USD | 43,000.00 USD | 9,030.00 USD | 11,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8680` | 3,050,000.00 USD | 3,050,000.00 USD | 92,530.00 USD | 14,760.00 USD | 50,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 12,590.00 USD | 141,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8700` | 2,380,000.00 USD | 2,380,000.00 USD | 49,290.00 USD | 3,880.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8700` | 2,890,000.00 USD | 2,890,000.00 USD | 81,840.00 USD | 9,460.00 USD | 7,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8705` | 92,480.00 USD | 128,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8720` | 2,290,000.00 USD | 2,290,000.00 USD | 30,840.00 USD | 34,140.00 USD | 24,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8720` | 2,800,000.00 USD | 2,800,000.00 USD | 5,420.00 USD | 18,020.00 USD | 11,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8725` | 26,640.00 USD | 36,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8740` | 2,200,000.00 USD | 2,200,000.00 USD | 59,860.00 USD | 12,180.00 USD | 33,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8740` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 12,360.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 2,100,000.00 USD | 2,100,000.00 USD | 16,700.00 USD | 5,410.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8760` | 2,740,000.00 USD | 2,740,000.00 USD | 766.43 USD | 0.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 9,560.00 USD | 9,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8780` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 214.09 USD | 54,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8780` | 2,740,000.00 USD | 2,740,000.00 USD | 1,500.00 USD | 0.00 USD | 33,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8800` | 2,020,000.00 USD | 2,020,000.00 USD | 10,360.00 USD | 16.72 USD | 7,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8800` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 5,580.00 USD | 51,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8820` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 10,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8820` | 2,650,000.00 USD | 2,650,000.00 USD | 454.20 USD | 9,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 1,990,000.00 USD | 1,990,000.00 USD | 1,770.00 USD | 17,420.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8840` | 2,640,000.00 USD | 2,640,000.00 USD | 2,090.00 USD | 6,440.00 USD | 15,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8860` | 1,960,000.00 USD | 1,960,000.00 USD | 66,480.00 USD | 27,710.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8860` | 2,610,000.00 USD | 2,610,000.00 USD | 141,730.00 USD | 22,320.00 USD | 78,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8880` | 1,860,000.00 USD | 1,860,000.00 USD | 73,700.00 USD | 14,120.00 USD | 36,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8880` | 2,370,000.00 USD | 2,370,000.00 USD | 130,140.00 USD | 31,410.00 USD | 9,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8900` | 1,740,000.00 USD | 1,740,000.00 USD | 2,730.00 USD | 51,750.00 USD | 910.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8900` | 2,200,000.00 USD | 2,200,000.00 USD | 108,250.00 USD | 45,590.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8920` | 1,680,000.00 USD | 1,680,000.00 USD | 45,630.00 USD | 32,720.00 USD | 56,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8920` | 2,010,000.00 USD | 2,010,000.00 USD | 46,210.00 USD | 38,810.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8940` | 1,550,000.00 USD | 1,550,000.00 USD | 13,790.00 USD | 18,130.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8940` | 1,910,000.00 USD | 1,910,000.00 USD | 45,210.00 USD | 12,120.00 USD | 26,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8960` | 1,520,000.00 USD | 1,520,000.00 USD | 2,010.00 USD | 26,370.00 USD | 5,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8960` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 32,500.00 USD | 93,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8980` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 26,620.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8980` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 17,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9000` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 10,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9000` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 22,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9020` | 1,430,000.00 USD | 1,430,000.00 USD | 538.90 USD | 9,990.00 USD | 1,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9020` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 44,210.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9040` | 1,420,000.00 USD | 1,420,000.00 USD | 7,870.00 USD | 21,080.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9040` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 12,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9060` | 1,370,000.00 USD | 1,370,000.00 USD | 19,570.00 USD | 35.10 USD | 7,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9060` | 1,590,000.00 USD | 1,590,000.00 USD | 1,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9080` | 1,340,000.00 USD | 1,340,000.00 USD | 7,220.00 USD | 6,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9100` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 404.79 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9120` | 1,330,000.00 USD | 1,330,000.00 USD | 27,150.00 USD | 3,440.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9140` | 1,290,000.00 USD | 1,290,000.00 USD | 7,740.00 USD | 3,740.00 USD | 23,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9140` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 515.41 USD | 36,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9160` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 5,930.00 USD | 10,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9160` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 9,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9180` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 8,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9180` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 23,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9200` | 1,230,000.00 USD | 1,230,000.00 USD | 5,710.00 USD | 2,090.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9200` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9220` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 48.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9220` | 1,510,000.00 USD | 1,510,000.00 USD | 152,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9240` | 1,220,000.00 USD | 1,220,000.00 USD | 77,940.00 USD | 8,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9240` | 1,360,000.00 USD | 1,360,000.00 USD | 145,560.00 USD | 12,790.00 USD | 29,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9260` | 1,140,000.00 USD | 1,140,000.00 USD | 898.50 USD | 39,060.00 USD | 31,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9260` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 32,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9280` | 1,060,000.00 USD | 1,060,000.00 USD | 78,050.00 USD | 4,120.00 USD | 66,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9280` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 24,550.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9300` | 916,190.00 USD | 916,190.00 USD | 0.00 USD | 12,290.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9320` | 902,700.00 USD | 902,700.00 USD | 7,440.00 USD | 68.90 USD | 11,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9320` | 1,110,000.00 USD | 1,110,000.00 USD | 37,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9340` | 884,030.00 USD | 884,030.00 USD | 93,080.00 USD | 15,060.00 USD | 38,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9340` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 11,160.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9360` | 737,070.00 USD | 737,070.00 USD | 90,760.00 USD | 45,310.00 USD | 29,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9360` | 1,030,000.00 USD | 1,030,000.00 USD | 8,250.00 USD | 0.00 USD | 68,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9380` | 571,340.00 USD | 571,340.00 USD | 54,410.00 USD | 17,230.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9380` | 953,250.00 USD | 953,250.00 USD | 42,660.00 USD | 19,540.00 USD | 27,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9400` | 484,880.00 USD | 484,880.00 USD | 88,450.00 USD | 36,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9400` | 863,360.00 USD | 863,360.00 USD | 75,540.00 USD | 32,570.00 USD | 47,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9420` | 359,510.00 USD | 359,510.00 USD | 101,680.00 USD | 20,480.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9420` | 707,950.00 USD | 707,950.00 USD | 106,320.00 USD | 7,050.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9440` | 201,180.00 USD | 201,180.00 USD | 135,580.00 USD | 34,100.00 USD | 31,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9440` | 589,810.00 USD | 589,810.00 USD | 102,440.00 USD | 49,100.00 USD | 57,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 206,430.00 USD | 206,430.00 USD | 89,630.00 USD | 54,970.00 USD | 61,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 412,860.00 USD | 412,860.00 USD | 89,630.00 USD | 54,970.00 USD | 61,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9460` | 380,950.00 USD | 380,950.00 USD | 286,390.00 USD | 27,270.00 USD | 67,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9480` | 595,030.00 USD | 595,030.00 USD | 103,240.00 USD | 4,720.00 USD | 74,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9480` | 298,700.00 USD | 298,700.00 USD | 193,280.00 USD | 10,340.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9480` | 597,400.00 USD | 597,400.00 USD | 193,280.00 USD | 10,340.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 675,210.00 USD | 675,210.00 USD | 80,090.00 USD | 85.68 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9500` | 821,820.00 USD | 821,820.00 USD | 196,070.00 USD | 18,830.00 USD | 9,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 693,350.00 USD | 693,350.00 USD | 0.00 USD | 18,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9520` | 1,010,000.00 USD | 1,010,000.00 USD | 175,720.00 USD | 9,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 751,300.00 USD | 751,300.00 USD | 48,110.00 USD | 9,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9540` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 9,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 777,060.00 USD | 777,060.00 USD | 10,720.00 USD | 15,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9560` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 28,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 781,940.00 USD | 781,940.00 USD | 4,400.00 USD | 0.00 USD | 471.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9580` | 1,060,000.00 USD | 1,060,000.00 USD | 3,880.00 USD | 6,110.00 USD | 957.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 791,820.00 USD | 791,820.00 USD | 3,440.00 USD | 4,720.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9600` | 1,080,000.00 USD | 1,080,000.00 USD | 17,690.00 USD | 4,660.00 USD | 866.69 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 887,330.00 USD | 887,330.00 USD | 71,510.00 USD | 7,410.00 USD | 16,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9620` | 1,110,000.00 USD | 1,110,000.00 USD | 17,990.00 USD | 16,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 965,250.00 USD | 965,250.00 USD | 19,400.00 USD | 30,520.00 USD | 28,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9640` | 1,230,000.00 USD | 1,230,000.00 USD | 95,370.00 USD | 7,500.00 USD | 12,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 1,010,000.00 USD | 1,010,000.00 USD | 2,700.00 USD | 4,970.00 USD | 37,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9660` | 1,240,000.00 USD | 1,240,000.00 USD | 5,050.00 USD | 5,170.00 USD | 778.15 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9680` | 1,070,000.00 USD | 1,070,000.00 USD | 39,090.00 USD | 15,070.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9680` | 1,280,000.00 USD | 1,280,000.00 USD | 38,090.00 USD | 5,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 1,120,000.00 USD | 1,120,000.00 USD | 16,500.00 USD | 4,190.00 USD | 33,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9700` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 30,140.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 1,210,000.00 USD | 1,210,000.00 USD | 24,360.00 USD | 395.16 USD | 64,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9720` | 1,380,000.00 USD | 1,380,000.00 USD | 1,430.00 USD | 3,960.00 USD | 31,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 1,270,000.00 USD | 1,270,000.00 USD | 25,800.00 USD | 5,170.00 USD | 27,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9740` | 1,480,000.00 USD | 1,480,000.00 USD | 1,480.00 USD | 25,640.00 USD | 76,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 1,370,000.00 USD | 1,370,000.00 USD | 53,500.00 USD | 24,670.00 USD | 20,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9760` | 1,560,000.00 USD | 1,560,000.00 USD | 51,990.00 USD | 16,870.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 1,430,000.00 USD | 1,430,000.00 USD | 40,740.00 USD | 3,080.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9780` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 24,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 1,490,000.00 USD | 1,490,000.00 USD | 34,990.00 USD | 9,680.00 USD | 20,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9800` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 152,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 1,530,000.00 USD | 1,530,000.00 USD | 22,110.00 USD | 11,710.00 USD | 7,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9820` | 1,910,000.00 USD | 1,910,000.00 USD | 53,310.00 USD | 15,990.00 USD | 104,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 1,590,000.00 USD | 1,590,000.00 USD | 665.59 USD | 13,380.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9840` | 1,990,000.00 USD | 1,990,000.00 USD | 49,930.00 USD | 211.77 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 1,670,000.00 USD | 1,670,000.00 USD | 50,550.00 USD | 3,630.00 USD | 24,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9860` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9880` | 1,700,000.00 USD | 1,700,000.00 USD | 17,200.00 USD | 1,570.00 USD | 16,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9880` | 2,090,000.00 USD | 2,090,000.00 USD | 40,020.00 USD | 0.00 USD | 67,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 1,790,000.00 USD | 1,790,000.00 USD | 61,110.00 USD | 1,320.00 USD | 28,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9900` | 2,130,000.00 USD | 2,130,000.00 USD | 20,530.00 USD | 0.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 1,840,000.00 USD | 1,840,000.00 USD | 9,580.00 USD | 4,160.00 USD | 32,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9920` | 2,160,000.00 USD | 2,160,000.00 USD | 1,570.00 USD | 479.24 USD | 31,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 1,880,000.00 USD | 1,880,000.00 USD | 25,660.00 USD | 10,700.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9940` | 2,230,000.00 USD | 2,230,000.00 USD | 29,270.00 USD | 0.00 USD | 39,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 1,910,000.00 USD | 1,910,000.00 USD | 19,070.00 USD | 3,600.00 USD | 7,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9960` | 2,360,000.00 USD | 2,360,000.00 USD | 75,810.00 USD | 5,380.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 1,990,000.00 USD | 1,990,000.00 USD | 53,920.00 USD | 10,730.00 USD | 15,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9980` | 2,420,000.00 USD | 2,420,000.00 USD | 53,110.00 USD | 6,740.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9985` | 852.22 USD | 852.22 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,080,000.00 USD | 2,080,000.00 USD | 60,660.00 USD | 18,230.00 USD | 6,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,480,000.00 USD | 2,480,000.00 USD | 52,850.00 USD | 0.00 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,110,000.00 USD | 2,110,000.00 USD | 16,570.00 USD | 1,970.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,570,000.00 USD | 2,570,000.00 USD | 56,560.00 USD | 21,850.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,140,000.00 USD | 2,140,000.00 USD | 10,790.00 USD | 9,550.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,650,000.00 USD | 2,650,000.00 USD | 70,950.00 USD | 3,970.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,270,000.00 USD | 2,270,000.00 USD | 101,040.00 USD | 10,160.00 USD | 25,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,700,000.00 USD | 2,700,000.00 USD | 46,710.00 USD | 0.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,340,000.00 USD | 2,340,000.00 USD | 22,410.00 USD | 9,170.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 44,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,370,000.00 USD | 2,370,000.00 USD | 12,560.00 USD | 17,230.00 USD | 971.85 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,770,000.00 USD | 2,770,000.00 USD | 10,260.00 USD | 14,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,410,000.00 USD | 2,410,000.00 USD | 16,880.00 USD | 22,370.00 USD | 265.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,840,000.00 USD | 2,840,000.00 USD | 33,230.00 USD | 30,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,440,000.00 USD | 2,440,000.00 USD | 6,560.00 USD | 5,790.00 USD | 21,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,870,000.00 USD | 2,870,000.00 USD | 2,870.00 USD | 28,450.00 USD | 735.11 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,490,000.00 USD | 2,490,000.00 USD | 15,150.00 USD | 25,460.00 USD | 11,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,910,000.00 USD | 2,910,000.00 USD | 526.60 USD | 28,470.00 USD | 11,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,540,000.00 USD | 2,540,000.00 USD | 26,110.00 USD | 4,240.00 USD | 22,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,960,000.00 USD | 2,960,000.00 USD | 1,430.00 USD | 25,010.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,620,000.00 USD | 2,620,000.00 USD | 47,410.00 USD | 9,980.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,120,000.00 USD | 3,120,000.00 USD | 33,820.00 USD | 84,220.00 USD | 44,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,700,000.00 USD | 2,700,000.00 USD | 35,050.00 USD | 20,320.00 USD | 27,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,340,000.00 USD | 3,340,000.00 USD | 56,930.00 USD | 52,610.00 USD | 112,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,790,000.00 USD | 2,790,000.00 USD | 44,050.00 USD | 9,760.00 USD | 34,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,560,000.00 USD | 3,560,000.00 USD | 78,220.00 USD | 56,700.00 USD | 86,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,860,000.00 USD | 2,860,000.00 USD | 36,400.00 USD | 18,290.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,740,000.00 USD | 3,740,000.00 USD | 22,650.00 USD | 124,880.00 USD | 33,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,900,000.00 USD | 2,900,000.00 USD | 15,280.00 USD | 8,920.00 USD | 15,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,070,000.00 USD | 4,070,000.00 USD | 250,310.00 USD | 50,530.00 USD | 24,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,000,000.00 USD | 3,000,000.00 USD | 64,370.00 USD | 12,650.00 USD | 18,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,260,000.00 USD | 4,260,000.00 USD | 134,200.00 USD | 33,660.00 USD | 19,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,070,000.00 USD | 3,070,000.00 USD | 30,350.00 USD | 7,050.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,360,000.00 USD | 4,360,000.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,100,000.00 USD | 3,100,000.00 USD | 12,070.00 USD | 8,650.00 USD | 12,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,590,000.00 USD | 4,590,000.00 USD | 217,210.00 USD | 8,290.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,120,000.00 USD | 3,120,000.00 USD | 4,320.00 USD | 10,280.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 4,900,000.00 USD | 4,900,000.00 USD | 262,550.00 USD | 3,170.00 USD | 42,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,170,000.00 USD | 3,170,000.00 USD | 42,730.00 USD | 767.34 USD | 2,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,280,000.00 USD | 5,280,000.00 USD | 178,400.00 USD | 1,290.00 USD | 199,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,190,000.00 USD | 3,190,000.00 USD | 6,280.00 USD | 6,670.00 USD | 8,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,660,000.00 USD | 5,660,000.00 USD | 279,840.00 USD | 9,430.00 USD | 93,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,210,000.00 USD | 3,210,000.00 USD | 10,930.00 USD | 5,820.00 USD | 3,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,990,000.00 USD | 5,990,000.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,220,000.00 USD | 3,220,000.00 USD | 2,950.00 USD | 1,330.00 USD | 10,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,250,000.00 USD | 6,250,000.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,230,000.00 USD | 3,230,000.00 USD | 5,280.00 USD | 4,540.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 6,670,000.00 USD | 6,670,000.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 367.04 USD | 1,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,250,000.00 USD | 3,250,000.00 USD | 4,070.00 USD | 73.95 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,060,000.00 USD | 7,060,000.00 USD | 199,320.00 USD | 28,070.00 USD | 167,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,290,000.00 USD | 3,290,000.00 USD | 29,490.00 USD | 4,070.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,220,000.00 USD | 7,220,000.00 USD | 92,710.00 USD | 29,070.00 USD | 41,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,310,000.00 USD | 3,310,000.00 USD | 4,960.00 USD | 1,200.00 USD | 16,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,560,000.00 USD | 7,560,000.00 USD | 140,530.00 USD | 49,780.00 USD | 143,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,330,000.00 USD | 3,330,000.00 USD | 10,950.00 USD | 345.49 USD | 2,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,730,000.00 USD | 7,730,000.00 USD | 88,940.00 USD | 44,290.00 USD | 36,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,340,000.00 USD | 3,340,000.00 USD | 6,010.00 USD | 4,840.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,090,000.00 USD | 8,090,000.00 USD | 187,610.00 USD | 48,000.00 USD | 121,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,360,000.00 USD | 3,360,000.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,450,000.00 USD | 8,450,000.00 USD | 205,290.00 USD | 63,350.00 USD | 94,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,860,000.00 USD | 8,860,000.00 USD | 217,790.00 USD | 73,000.00 USD | 125,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,150,000.00 USD | 9,150,000.00 USD | 131,720.00 USD | 83,000.00 USD | 66,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,390,000.00 USD | 9,390,000.00 USD | 102,750.00 USD | 49,310.00 USD | 92,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 9,570,000.00 USD | 9,570,000.00 USD | 77,920.00 USD | 32,860.00 USD | 73,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 9,920,000.00 USD | 9,920,000.00 USD | 221,410.00 USD | 30,180.00 USD | 93,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,120,000.00 USD | 10,120,000.00 USD | 121,300.00 USD | 33,170.00 USD | 42,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,340,000.00 USD | 10,340,000.00 USD | 103,500.00 USD | 37,730.00 USD | 83,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,540,000.00 USD | 10,540,000.00 USD | 92,440.00 USD | 21,500.00 USD | 83,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 10,690,000.00 USD | 10,690,000.00 USD | 103,110.00 USD | 18,720.00 USD | 27,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 10,960,000.00 USD | 10,960,000.00 USD | 158,650.00 USD | 40,740.00 USD | 69,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,190,000.00 USD | 11,190,000.00 USD | 176,790.00 USD | 25,790.00 USD | 31,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,220,000.00 USD | 11,220,000.00 USD | 34,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.08` | 2,230.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.11` | 170.02 USD | 3,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.15` | 15,610.00 USD | 19,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 11,730.00 USD | 30,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 239.77 USD | 31,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.38` | 3,920.00 USD | 35,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,190.00 USD | 38,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 118.18 USD | 38,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 176.31 USD | 38,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 1,810.00 USD | 40,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 799.79 USD | 41,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.63` | 2,440.00 USD | 43,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 8,240.00 USD | 51,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 242.64 USD | 52,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 300.15 USD | 52,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 323.26 USD | 52,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 190.42 USD | 52,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 13,140.00 USD | 66,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 380.81 USD | 66,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 88,950.00 USD | 155,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 23,530.00 USD | 178,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 208.37 USD | 179,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 181.88 USD | 179,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2235` | 469,050.00 USD | 0.00 USD | 111.75 USD | `-76.52%` | `500.00` |
| `Live` | `Long` | `0.3575` | 468,930.00 USD | 0.00 USD | 789.72 USD | `-62.44%` | `2,209.00` |
| `Live` | `Long` | `0.4055` | 468,140.00 USD | 0.00 USD | 2,310.00 USD | `-57.40%` | `5,698.80` |
| `Live` | `Long` | `0.4195` | 465,830.00 USD | 0.00 USD | 2,800.00 USD | `-55.93%` | `6,675.20` |
| `Live` | `Long` | `0.4495` | 463,030.00 USD | 0.00 USD | 1,180.00 USD | `-52.78%` | `2,618.10` |
| `Live` | `Long` | `0.4675` | 461,860.00 USD | 0.00 USD | 146.70 USD | `-50.88%` | `313.80` |
| `Live` | `Long` | `0.4705` | 461,710.00 USD | 0.00 USD | 2,590.00 USD | `-50.57%` | `5,500.00` |
| `Live` | `Long` | `0.4875` | 459,120.00 USD | 0.00 USD | 195.34 USD | `-48.78%` | `400.70` |
| `Live` | `Long` | `0.5065` | 458,930.00 USD | 0.00 USD | 3,290.00 USD | `-46.79%` | `6,504.70` |
| `Live` | `Long` | `0.5385` | 455,630.00 USD | 0.00 USD | 538.50 USD | `-43.43%` | `1,000.00` |
| `Live` | `Long` | `0.5405` | 455,090.00 USD | 0.00 USD | 141.67 USD | `-43.22%` | `262.10` |
| `Live` | `Long` | `0.5515` | 454,950.00 USD | 0.00 USD | 218.67 USD | `-42.06%` | `396.50` |
| `Live` | `Long` | `0.5655` | 454,730.00 USD | 0.00 USD | 14,600.00 USD | `-40.59%` | `25,816.60` |
| `Live` | `Long` | `0.5695` | 440,130.00 USD | 0.00 USD | 577.36 USD | `-40.17%` | `1,013.80` |
| `Live` | `Long` | `0.5845` | 439,560.00 USD | 0.00 USD | 683.51 USD | `-38.59%` | `1,169.40` |
| `Live` | `Long` | `0.5895` | 438,870.00 USD | 0.00 USD | 137.53 USD | `-38.07%` | `233.30` |
| `Live` | `Long` | `0.6055` | 438,740.00 USD | 0.00 USD | 1,480.00 USD | `-36.39%` | `2,448.50` |
| `Live` | `Long` | `0.6075` | 437,250.00 USD | 0.00 USD | 1,810.00 USD | `-36.18%` | `2,971.80` |
| `Live` | `Long` | `0.6125` | 435,450.00 USD | 0.00 USD | 105.96 USD | `-35.65%` | `173.00` |
| `Live` | `Long` | `0.6145` | 435,340.00 USD | 0.00 USD | 147.48 USD | `-35.44%` | `240.00` |
| `Live` | `Long` | `0.6315` | 435,190.00 USD | 0.00 USD | 757.80 USD | `-33.65%` | `1,200.00` |
| `Live` | `Long` | `0.6355` | 434,440.00 USD | 0.00 USD | 106.00 USD | `-33.23%` | `166.80` |
| `Live` | `Long` | `0.6365` | 434,330.00 USD | 0.00 USD | 507.86 USD | `-33.13%` | `797.90` |
| `Live` | `Long` | `0.6405` | 433,820.00 USD | 0.00 USD | 2,090.00 USD | `-32.71%` | `3,262.00` |
| `Live` | `Long` | `0.6415` | 431,730.00 USD | 0.00 USD | 20,270.00 USD | `-32.60%` | `31,595.60` |
| `Live` | `Long` | `0.6465` | 411,460.00 USD | 0.00 USD | 4,230.00 USD | `-32.08%` | `6,539.70` |
| `Live` | `Long` | `0.6475` | 407,240.00 USD | 0.00 USD | 202.47 USD | `-31.97%` | `312.70` |
| `Live` | `Long` | `0.6555` | 407,030.00 USD | 0.00 USD | 521.19 USD | `-31.13%` | `795.10` |
| `Live` | `Long` | `0.6595` | 406,510.00 USD | 0.00 USD | 149.44 USD | `-30.71%` | `226.60` |
| `Live` | `Long` | `0.6725` | 406,360.00 USD | 0.00 USD | 63,890.00 USD | `-29.35%` | `95,000.00` |
| `Live` | `Long` | `0.6755` | 342,480.00 USD | 0.00 USD | 84,440.00 USD | `-29.03%` | `125,000.00` |
| `Live` | `Long` | `0.6775` | 258,040.00 USD | 0.00 USD | 423.10 USD | `-28.82%` | `624.50` |
| `Live` | `Long` | `0.6835` | 257,620.00 USD | 0.00 USD | 512.97 USD | `-28.19%` | `750.50` |
| `Live` | `Long` | `0.6905` | 257,100.00 USD | 0.00 USD | 19,770.00 USD | `-27.46%` | `28,635.00` |
| `Live` | `Long` | `0.6965` | 237,330.00 USD | 0.00 USD | 478.22 USD | `-26.83%` | `686.60` |
| `Live` | `Long` | `0.7005` | 236,850.00 USD | 0.00 USD | 1,140.00 USD | `-26.41%` | `1,634.20` |
| `Live` | `Long` | `0.7145` | 235,710.00 USD | 0.00 USD | 988.87 USD | `-24.93%` | `1,384.00` |
| `Live` | `Long` | `0.7215` | 234,720.00 USD | 0.00 USD | 1,580.00 USD | `-24.20%` | `2,190.90` |
| `Live` | `Long` | `0.7235` | 233,140.00 USD | 0.00 USD | 397.93 USD | `-23.99%` | `550.00` |
| `Live` | `Long` | `0.7285` | 232,740.00 USD | 0.00 USD | 291.18 USD | `-23.46%` | `399.70` |
| `Live` | `Long` | `0.7305` | 232,450.00 USD | 0.00 USD | 2,300.00 USD | `-23.25%` | `3,143.00` |
| `Live` | `Long` | `0.7335` | 230,150.00 USD | 0.00 USD | 1,140.00 USD | `-22.94%` | `1,557.80` |
| `Live` | `Long` | `0.7395` | 229,010.00 USD | 0.00 USD | 283.30 USD | `-22.31%` | `383.10` |
| `Live` | `Long` | `0.7525` | 228,730.00 USD | 0.00 USD | 2,220.00 USD | `-20.94%` | `2,947.70` |
| `Live` | `Long` | `0.7545` | 226,510.00 USD | 0.00 USD | 1,400.00 USD | `-20.73%` | `1,859.90` |
| `Live` | `Long` | `0.7555` | 225,100.00 USD | 0.00 USD | 9,980.00 USD | `-20.63%` | `13,204.90` |
| `Live` | `Long` | `0.7635` | 215,130.00 USD | 0.00 USD | 308.00 USD | `-19.79%` | `403.40` |
| `Live` | `Long` | `0.7655` | 214,820.00 USD | 0.00 USD | 54,350.00 USD | `-19.58%` | `71,003.30` |
| `Live` | `Long` | `0.7725` | 160,470.00 USD | 0.00 USD | 3,840.00 USD | `-18.84%` | `4,968.90` |
| `Live` | `Long` | `0.7775` | 156,630.00 USD | 0.00 USD | 2,490.00 USD | `-18.32%` | `3,199.30` |
| `Live` | `Long` | `0.7795` | 154,140.00 USD | 0.00 USD | 272.83 USD | `-18.11%` | `350.00` |
| `Live` | `Long` | `0.7865` | 153,870.00 USD | 0.00 USD | 292.03 USD | `-17.37%` | `371.30` |
| `Live` | `Long` | `0.7905` | 153,580.00 USD | 0.00 USD | 277.39 USD | `-16.95%` | `350.90` |
| `Live` | `Long` | `0.8135` | 153,300.00 USD | 0.00 USD | 647.79 USD | `-14.53%` | `796.30` |
| `Live` | `Long` | `0.8215` | 152,650.00 USD | 0.00 USD | 1,950.00 USD | `-13.69%` | `2,370.70` |
| `Live` | `Long` | `0.8235` | 150,700.00 USD | 0.00 USD | 749.96 USD | `-13.48%` | `910.70` |
| `Live` | `Long` | `0.8365` | 149,950.00 USD | 0.00 USD | 316.70 USD | `-12.12%` | `378.60` |
| `Live` | `Long` | `0.8415` | 149,640.00 USD | 0.00 USD | 1,570.00 USD | `-11.59%` | `1,862.40` |
| `Live` | `Long` | `0.8495` | 148,070.00 USD | 0.00 USD | 1,260.00 USD | `-10.75%` | `1,486.90` |
| `Live` | `Long` | `0.8515` | 146,810.00 USD | 0.00 USD | 2,700.00 USD | `-10.54%` | `3,175.90` |
| `Live` | `Long` | `0.8575` | 144,100.00 USD | 0.00 USD | 620.32 USD | `-9.91%` | `723.40` |
| `Live` | `Long` | `0.8595` | 143,480.00 USD | 0.00 USD | 180.75 USD | `-9.70%` | `210.30` |
| `Live` | `Long` | `0.8635` | 143,300.00 USD | 0.00 USD | 208.02 USD | `-9.28%` | `240.90` |
| `Live` | `Long` | `0.8645` | 143,090.00 USD | 0.00 USD | 438.30 USD | `-9.18%` | `507.00` |
| `Live` | `Long` | `0.8665` | 142,660.00 USD | 0.00 USD | 1,390.00 USD | `-8.97%` | `1,606.10` |
| `Live` | `Long` | `0.8695` | 141,260.00 USD | 0.00 USD | 12,590.00 USD | `-8.65%` | `14,478.80` |
| `Live` | `Long` | `0.8705` | 128,670.00 USD | 0.00 USD | 92,480.00 USD | `-8.55%` | `106,233.40` |
| `Live` | `Long` | `0.8725` | 36,200.00 USD | 0.00 USD | 26,640.00 USD | `-8.34%` | `30,534.60` |
| `Live` | `Long` | `0.8765` | 9,560.00 USD | 0.00 USD | 9,560.00 USD | `-7.92%` | `10,903.10` |
| `Live` | `Short` | `0.9985` | 852.22 USD | 852.22 USD | 0.00 USD | `+4.90%` | `853.50` |
| `Live` | `Short` | `1.05` | 1,220.00 USD | 367.04 USD | 0.00 USD | `+10.05%` | `350.40` |
| `Live` | `Short` | `1.08` | 3,450.00 USD | 2,230.00 USD | 0.00 USD | `+13.62%` | `2,064.20` |
| `Live` | `Short` | `1.11` | 3,620.00 USD | 170.02 USD | 0.00 USD | `+16.67%` | `153.10` |
| `Live` | `Short` | `1.15` | 19,230.00 USD | 15,610.00 USD | 0.00 USD | `+20.66%` | `13,590.60` |
| `Live` | `Short` | `1.32` | 30,960.00 USD | 11,730.00 USD | 0.00 USD | `+39.05%` | `8,862.90` |
| `Live` | `Short` | `1.34` | 31,200.00 USD | 239.77 USD | 0.00 USD | `+40.73%` | `179.00` |
| `Live` | `Short` | `1.38` | 35,120.00 USD | 3,920.00 USD | 0.00 USD | `+45.14%` | `2,834.10` |
| `Live` | `Short` | `1.42` | 38,310.00 USD | 3,190.00 USD | 0.00 USD | `+49.13%` | `2,249.30` |
| `Live` | `Short` | `1.49` | 38,430.00 USD | 118.18 USD | 0.00 USD | `+56.17%` | `79.50` |
| `Live` | `Short` | `1.54` | 38,600.00 USD | 176.31 USD | 0.00 USD | `+62.05%` | `114.30` |
| `Live` | `Short` | `1.56` | 40,410.00 USD | 1,810.00 USD | 0.00 USD | `+63.53%` | `1,161.90` |
| `Live` | `Short` | `1.60` | 41,210.00 USD | 799.79 USD | 0.00 USD | `+68.25%` | `499.40` |
| `Live` | `Short` | `1.63` | 43,650.00 USD | 2,440.00 USD | 0.00 USD | `+70.77%` | `1,500.00` |
| `Live` | `Short` | `1.65` | 51,890.00 USD | 8,240.00 USD | 0.00 USD | `+73.09%` | `5,000.00` |
| `Live` | `Short` | `1.66` | 52,130.00 USD | 242.64 USD | 0.00 USD | `+74.24%` | `146.30` |
| `Live` | `Short` | `1.67` | 52,430.00 USD | 300.15 USD | 0.00 USD | `+75.19%` | `180.00` |
| `Live` | `Short` | `1.68` | 52,750.00 USD | 323.26 USD | 0.00 USD | `+76.97%` | `191.90` |
| `Live` | `Short` | `1.73` | 52,940.00 USD | 190.42 USD | 0.00 USD | `+81.70%` | `110.10` |
| `Live` | `Short` | `1.74` | 66,090.00 USD | 13,140.00 USD | 0.00 USD | `+82.44%` | `7,569.10` |
| `Live` | `Short` | `1.77` | 66,470.00 USD | 380.81 USD | 0.00 USD | `+86.43%` | `214.60` |
| `Live` | `Short` | `1.79` | 155,410.00 USD | 88,950.00 USD | 0.00 USD | `+87.79%` | `49,759.80` |
| `Live` | `Short` | `1.82` | 178,940.00 USD | 23,530.00 USD | 0.00 USD | `+91.37%` | `12,916.90` |
| `Live` | `Short` | `1.86` | 179,150.00 USD | 208.37 USD | 0.00 USD | `+94.94%` | `112.30` |
| `Live` | `Short` | `1.90` | 179,330.00 USD | 181.88 USD | 0.00 USD | `+99.67%` | `95.70` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.4015` | 363,820.00 USD | 0.00 USD | 120.45 USD | `-57.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 363,700.00 USD | 0.00 USD | 150.15 USD | `-47.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5435` | 363,550.00 USD | 0.00 USD | 186.15 USD | `-42.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 363,370.00 USD | 0.00 USD | 1,150.00 USD | `-31.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 362,220.00 USD | 0.00 USD | 781.90 USD | `-26.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 361,440.00 USD | 0.00 USD | 477.38 USD | `-25.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 360,960.00 USD | 0.00 USD | 341.33 USD | `-24.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 360,620.00 USD | 0.00 USD | 972.82 USD | `-24.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 359,650.00 USD | 0.00 USD | 160.20 USD | `-23.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7385` | 359,490.00 USD | 0.00 USD | 102.58 USD | `-22.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 359,380.00 USD | 0.00 USD | 289.49 USD | `-21.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7615` | 359,090.00 USD | 0.00 USD | 197.53 USD | `-20.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 358,900.00 USD | 0.00 USD | 14,570.00 USD | `-18.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 344,330.00 USD | 0.00 USD | 213.58 USD | `-17.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 344,120.00 USD | 0.00 USD | 274,830.00 USD | `-16.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 69,280.00 USD | 0.00 USD | 108.47 USD | `-15.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 69,170.00 USD | 0.00 USD | 326.96 USD | `-14.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 68,850.00 USD | 0.00 USD | 405.75 USD | `-14.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 68,440.00 USD | 0.00 USD | 772.84 USD | `-12.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8415` | 67,670.00 USD | 0.00 USD | 2,670.00 USD | `-11.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8495` | 65,000.00 USD | 0.00 USD | 3,470.00 USD | `-10.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 61,530.00 USD | 0.00 USD | 9,180.00 USD | `-10.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 52,350.00 USD | 0.00 USD | 341.94 USD | `-10.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 52,000.00 USD | 0.00 USD | 1,150.00 USD | `-10.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 50,860.00 USD | 0.00 USD | 429.25 USD | `-9.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 50,430.00 USD | 0.00 USD | 223.30 USD | `-9.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 50,200.00 USD | 0.00 USD | 518.51 USD | `-8.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 49,690.00 USD | 0.00 USD | 205.24 USD | `-8.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 49,480.00 USD | 0.00 USD | 649.66 USD | `-8.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 48,830.00 USD | 0.00 USD | 194.06 USD | `-7.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8845` | 48,640.00 USD | 0.00 USD | 193.35 USD | `-7.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 48,440.00 USD | 0.00 USD | 223.04 USD | `-6.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 48,220.00 USD | 0.00 USD | 10,840.00 USD | `-6.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 37,380.00 USD | 0.00 USD | 4,920.00 USD | `-6.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8915` | 32,460.00 USD | 0.00 USD | 317.02 USD | `-6.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 32,140.00 USD | 0.00 USD | 192.07 USD | `-6.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 31,950.00 USD | 0.00 USD | 195.32 USD | `-6.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8965` | 31,750.00 USD | 0.00 USD | 196.87 USD | `-5.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8985` | 31,560.00 USD | 0.00 USD | 2,870.00 USD | `-5.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9005` | 28,680.00 USD | 0.00 USD | 319.05 USD | `-5.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9025` | 28,360.00 USD | 0.00 USD | 398.91 USD | `-5.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9035` | 27,970.00 USD | 0.00 USD | 196.96 USD | `-5.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9045` | 27,770.00 USD | 0.00 USD | 300.38 USD | `-4.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9065` | 27,470.00 USD | 0.00 USD | 198.61 USD | `-4.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9075` | 27,270.00 USD | 0.00 USD | 994.35 USD | `-4.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 26,280.00 USD | 0.00 USD | 363.40 USD | `-4.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9095` | 25,910.00 USD | 0.00 USD | 198.18 USD | `-4.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9115` | 25,710.00 USD | 0.00 USD | 397.23 USD | `-4.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9135` | 25,320.00 USD | 0.00 USD | 398.65 USD | `-4.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9145` | 24,920.00 USD | 0.00 USD | 399.09 USD | `-3.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9155` | 24,520.00 USD | 0.00 USD | 403.92 USD | `-3.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9165` | 24,110.00 USD | 0.00 USD | 198.06 USD | `-3.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9175` | 23,920.00 USD | 0.00 USD | 223.78 USD | `-3.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9185` | 23,690.00 USD | 0.00 USD | 899.85 USD | `-3.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9195` | 22,790.00 USD | 0.00 USD | 900.19 USD | `-3.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 21,890.00 USD | 0.00 USD | 407.41 USD | `-3.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9215` | 21,490.00 USD | 0.00 USD | 407.30 USD | `-3.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9225` | 21,080.00 USD | 0.00 USD | 201.94 USD | `-3.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9245` | 20,880.00 USD | 0.00 USD | 201.45 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9255` | 20,670.00 USD | 0.00 USD | 817.40 USD | `-2.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9265` | 19,860.00 USD | 0.00 USD | 403.77 USD | `-2.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9275` | 19,450.00 USD | 0.00 USD | 2,120.00 USD | `-2.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9285` | 17,340.00 USD | 0.00 USD | 246.05 USD | `-2.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9295` | 17,090.00 USD | 0.00 USD | 407.49 USD | `-2.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9305` | 16,680.00 USD | 0.00 USD | 203.97 USD | `-2.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9315` | 16,480.00 USD | 0.00 USD | 263.80 USD | `-2.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9325` | 16,210.00 USD | 0.00 USD | 241.98 USD | `-2.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9335` | 15,970.00 USD | 0.00 USD | 814.76 USD | `-1.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9355` | 15,160.00 USD | 0.00 USD | 201.97 USD | `-1.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9365` | 14,960.00 USD | 0.00 USD | 9,680.00 USD | `-1.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9395` | 5,270.00 USD | 0.00 USD | 416.01 USD | `-1.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9405` | 4,860.00 USD | 0.00 USD | 555.18 USD | `-1.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9425` | 4,300.00 USD | 0.00 USD | 816.96 USD | `-0.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9435` | 3,480.00 USD | 0.00 USD | 334.28 USD | `-0.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9445` | 3,150.00 USD | 0.00 USD | 1,730.00 USD | `-0.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9455` | 1,420.00 USD | 0.00 USD | 383.87 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9465` | 1,040.00 USD | 0.00 USD | 623.93 USD | `-0.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9485` | 414.68 USD | 0.00 USD | 414.68 USD | `-0.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9525` | 381.00 USD | 381.00 USD | 0.00 USD | `+0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 2,400.00 USD | 2,020.00 USD | 0.00 USD | `+0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 2,610.00 USD | 206.77 USD | 0.00 USD | `+0.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 2,840.00 USD | 236.26 USD | 0.00 USD | `+0.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 2,980.00 USD | 136.83 USD | 0.00 USD | `+0.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 3,240.00 USD | 261.16 USD | 0.00 USD | `+0.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 5,150.00 USD | 1,910.00 USD | 0.00 USD | `+1.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 5,710.00 USD | 568.75 USD | 0.00 USD | `+1.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 5,880.00 USD | 163.29 USD | 0.00 USD | `+1.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 6,260.00 USD | 385.74 USD | 0.00 USD | `+1.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 8,300.00 USD | 2,030.00 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 8,560.00 USD | 262.52 USD | 0.00 USD | `+1.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 8,950.00 USD | 387.83 USD | 0.00 USD | `+2.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 16,580.00 USD | 7,630.00 USD | 0.00 USD | `+2.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9745` | 25,330.00 USD | 8,750.00 USD | 0.00 USD | `+2.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 47,290.00 USD | 21,960.00 USD | 0.00 USD | `+2.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 47,690.00 USD | 396.17 USD | 0.00 USD | `+2.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 48,360.00 USD | 676.53 USD | 0.00 USD | `+2.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 56,720.00 USD | 8,350.00 USD | 0.00 USD | `+3.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 58,740.00 USD | 2,030.00 USD | 0.00 USD | `+3.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 60,800.00 USD | 2,060.00 USD | 0.00 USD | `+3.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 61,060.00 USD | 255.38 USD | 0.00 USD | `+3.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 76,130.00 USD | 15,070.00 USD | 0.00 USD | `+3.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9865` | 76,240.00 USD | 109.99 USD | 0.00 USD | `+3.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 79,760.00 USD | 3,520.00 USD | 0.00 USD | `+4.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 111,510.00 USD | 31,750.00 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 111,910.00 USD | 403.06 USD | 0.00 USD | `+4.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 112,320.00 USD | 403.28 USD | 0.00 USD | `+4.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 117,460.00 USD | 5,140.00 USD | 0.00 USD | `+4.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 154,770.00 USD | 37,310.00 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 155,770.00 USD | 1,000.00 USD | 0.00 USD | `+5.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 196,360.00 USD | 40,590.00 USD | 0.00 USD | `+5.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 196,600.00 USD | 235.79 USD | 0.00 USD | `+5.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 197,940.00 USD | 1,340.00 USD | 0.00 USD | `+5.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 198,170.00 USD | 230.39 USD | 0.00 USD | `+5.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 198,390.00 USD | 218.64 USD | 0.00 USD | `+5.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 198,800.00 USD | 409.86 USD | 0.00 USD | `+6.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 198,910.00 USD | 110.95 USD | 0.00 USD | `+6.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 199,530.00 USD | 615.60 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 200,090.00 USD | 561.17 USD | 0.00 USD | `+6.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 200,300.00 USD | 214.40 USD | 0.00 USD | `+7.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 200,550.00 USD | 249.88 USD | 0.00 USD | `+7.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 200,760.00 USD | 207.97 USD | 0.00 USD | `+7.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 200,970.00 USD | 208.26 USD | 0.00 USD | `+8.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 201,490.00 USD | 516.75 USD | 0.00 USD | `+8.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 201,840.00 USD | 348.86 USD | 0.00 USD | `+8.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 202,230.00 USD | 391.80 USD | 0.00 USD | `+8.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 202,640.00 USD | 413.76 USD | 0.00 USD | `+9.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 203,000.00 USD | 354.91 USD | 0.00 USD | `+9.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 204,900.00 USD | 1,900.00 USD | 0.00 USD | `+9.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 205,110.00 USD | 207.87 USD | 0.00 USD | `+9.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 205,320.00 USD | 207.97 USD | 0.00 USD | `+9.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 205,420.00 USD | 107.99 USD | 0.00 USD | `+10.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 280,260.00 USD | 74,840.00 USD | 0.00 USD | `+11.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 282,430.00 USD | 2,170.00 USD | 0.00 USD | `+14.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 283,970.00 USD | 1,540.00 USD | 0.00 USD | `+14.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 293,890.00 USD | 9,930.00 USD | 0.00 USD | `+15.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 294,770.00 USD | 877.63 USD | 0.00 USD | `+16.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 294,940.00 USD | 171.09 USD | 0.00 USD | `+17.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 297,710.00 USD | 2,770.00 USD | 0.00 USD | `+18.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 299,750.00 USD | 2,040.00 USD | 0.00 USD | `+18.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 299,920.00 USD | 172.32 USD | 0.00 USD | `+18.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 300,110.00 USD | 187.72 USD | 0.00 USD | `+18.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 300,300.00 USD | 188.39 USD | 0.00 USD | `+19.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 302,970.00 USD | 2,670.00 USD | 0.00 USD | `+19.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 303,140.00 USD | 174.23 USD | 0.00 USD | `+19.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 303,310.00 USD | 174.38 USD | 0.00 USD | `+19.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 303,490.00 USD | 174.84 USD | 0.00 USD | `+19.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 303,640.00 USD | 150.90 USD | 0.00 USD | `+20.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 303,790.00 USD | 151.03 USD | 0.00 USD | `+20.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 303,940.00 USD | 151.16 USD | 0.00 USD | `+20.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 304,090.00 USD | 151.29 USD | 0.00 USD | `+20.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 306,140.00 USD | 2,050.00 USD | 0.00 USD | `+22.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 306,250.00 USD | 110.00 USD | 0.00 USD | `+23.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 306,730.00 USD | 475.80 USD | 0.00 USD | `+24.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 307,930.00 USD | 1,210.00 USD | 0.00 USD | `+26.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 350,860.00 USD | 42,930.00 USD | 0.00 USD | `+26.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 352,860.00 USD | 2,000.00 USD | 0.00 USD | `+29.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 354,250.00 USD | 1,380.00 USD | 0.00 USD | `+31.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 354,490.00 USD | 245.41 USD | 0.00 USD | `+34.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 362,890.00 USD | 8,390.00 USD | 0.00 USD | `+35.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 363,300.00 USD | 415.25 USD | 0.00 USD | `+36.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 369,820.00 USD | 6,520.00 USD | 0.00 USD | `+36.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 374,620.00 USD | 4,800.00 USD | 0.00 USD | `+37.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 375,270.00 USD | 655.75 USD | 0.00 USD | `+37.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 375,870.00 USD | 596.43 USD | 0.00 USD | `+39.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 377,680.00 USD | 1,810.00 USD | 0.00 USD | `+40.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 391,570.00 USD | 13,880.00 USD | 0.00 USD | `+41.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 392,820.00 USD | 1,250.00 USD | 0.00 USD | `+42.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 394,890.00 USD | 2,070.00 USD | 0.00 USD | `+46.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 395,030.00 USD | 140.05 USD | 0.00 USD | `+47.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 395,190.00 USD | 160.42 USD | 0.00 USD | `+47.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 396,140.00 USD | 954.32 USD | 0.00 USD | `+48.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 430,320.00 USD | 34,170.00 USD | 0.00 USD | `+50.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 431,200.00 USD | 879.84 USD | 0.00 USD | `+56.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 434,250.00 USD | 3,050.00 USD | 0.00 USD | `+59.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 434,550.00 USD | 297.27 USD | 0.00 USD | `+63.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 443,080.00 USD | 8,530.00 USD | 0.00 USD | `+73.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 443,220.00 USD | 143.99 USD | 0.00 USD | `+75.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 443,400.00 USD | 177.05 USD | 0.00 USD | `+86.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 443,830.00 USD | 431.40 USD | 0.00 USD | `+89.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 444,050.00 USD | 220.77 USD | 0.00 USD | `+91.05%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7720` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 10,530.00 USD | 1,600.00 USD | 7,310.00 USD |
| `7D` | `0.7740` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 5,450.00 USD | 0.00 USD | 3,310.00 USD |
| `7D` | `0.7760` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 147.66 USD |
| `7D` | `0.7780` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 0.00 USD | 3,100.00 USD | 53.43 USD |
| `7D` | `0.7800` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 436.65 USD | 25.30 USD | 0.00 USD |
| `7D` | `0.7820` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 0.00 USD | 1,920.00 USD | 1,410.00 USD |
| `7D` | `0.7840` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 227.10 USD | 1,190.00 USD | 0.00 USD |
| `7D` | `0.7860` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 0.00 USD | 2,250.00 USD | 365.01 USD |
| `7D` | `0.7880` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 5,690.00 USD | 2,050.00 USD | 723.49 USD |
| `7D` | `0.7900` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 6,940.00 USD | 2,650.00 USD | 4,030.00 USD |
| `7D` | `0.7920` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 12,590.00 USD | 2,180.00 USD | 10,760.00 USD |
| `7D` | `0.7940` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 15,680.00 USD | 2,500.00 USD | 13,480.00 USD |
| `7D` | `0.7960` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 4,520.00 USD | 7,120.00 USD | 3,290.00 USD |
| `7D` | `0.7980` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 16,210.00 USD | 3,000.00 USD | 14,230.00 USD |
| `7D` | `0.8000` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 10,100.00 USD | 5,540.00 USD | 2,430.00 USD |
| `7D` | `0.8020` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 8,990.00 USD | 4,460.00 USD | 9,540.00 USD |
| `7D` | `0.8040` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 5,500.00 USD | 2,170.00 USD | 940.33 USD |
| `7D` | `0.8060` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 16,390.00 USD | 10,990.00 USD | 10,100.00 USD |
| `7D` | `0.8080` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 1,570.00 USD | 1,230.00 USD | 10,210.00 USD |
| `7D` | `0.8100` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 2,890.00 USD | 2,010.00 USD | 4,690.00 USD |
| `7D` | `0.8120` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 15,720.00 USD | 3,030.00 USD | 9,400.00 USD |
| `7D` | `0.8140` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 32,880.00 USD | 6,050.00 USD | 15,910.00 USD |
| `7D` | `0.8160` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 38,200.00 USD | 10,180.00 USD | 6,010.00 USD |
| `7D` | `0.8180` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 12,550.00 USD | 2,560.00 USD | 11,440.00 USD |
| `7D` | `0.8200` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 1,740.00 USD | 1,570.00 USD | 7,460.00 USD |
| `7D` | `0.8220` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 20,390.00 USD | 6,820.00 USD | 4,490.00 USD |
| `7D` | `0.8240` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 23,160.00 USD | 93.73 USD | 11,990.00 USD |
| `7D` | `0.8260` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 5,220.00 USD | 3,490.00 USD | 1,560.00 USD |
| `7D` | `0.8280` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 0.00 USD | 3,910.00 USD | 1,040.00 USD |
| `7D` | `0.8300` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 9,280.00 USD | 4,780.00 USD | 2,450.00 USD |
| `1D` | `0.8320` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 2,670.00 USD | 1,950.00 USD | 3,580.00 USD |
| `7D` | `0.8320` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 0.00 USD | 401.80 USD | 77.95 USD |
| `1D` | `0.8340` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 25,550.00 USD | 5,650.00 USD | 8,980.00 USD |
| `7D` | `0.8340` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 35,710.00 USD | 10,960.00 USD | 1,980.00 USD |
| `1D` | `0.8360` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 1,870.00 USD | 636.81 USD | 14,840.00 USD |
| `7D` | `0.8360` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 0.00 USD | 844.23 USD | 311.26 USD |
| `1D` | `0.8380` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 16,380.00 USD | 1,900.00 USD | 0.00 USD |
| `7D` | `0.8380` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 15,240.00 USD | 633.60 USD | 539.92 USD |
| `1D` | `0.8400` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 458.00 USD | 1,050.00 USD | 2,340.00 USD |
| `7D` | `0.8400` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 0.00 USD | 798.38 USD | 8,060.00 USD |
| `1D` | `0.8420` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 1,340.00 USD | 4,840.00 USD | 0.00 USD |
| `7D` | `0.8420` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 6,400.00 USD | 4,650.00 USD | 4,060.00 USD |
| `1D` | `0.8440` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 2,210.00 USD | 5.65 USD | 0.00 USD |
| `7D` | `0.8440` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 7,170.00 USD | 24.80 USD | 0.00 USD |
| `1D` | `0.8460` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 15,140.00 USD | 6,600.00 USD | 25.04 USD |
| `7D` | `0.8460` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 2,560.00 USD | 427.62 USD | 2,660.00 USD |
| `1D` | `0.8480` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 6,670.00 USD | 230.58 USD | 0.00 USD |
| `7D` | `0.8480` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 26,310.00 USD | 10,990.00 USD | 0.00 USD |
| `1D` | `0.8500` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 8,440.00 USD | 371.56 USD | 744.62 USD |
| `7D` | `0.8500` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 2,050.00 USD | 477.96 USD | 4,430.00 USD |
| `1D` | `0.8520` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,230.00 USD | 1,940.00 USD | 12,140.00 USD |
| `7D` | `0.8520` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 5,900.00 USD | 669.43 USD | 226.67 USD |
| `1D` | `0.8540` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 2,300.00 USD | 4,910.00 USD | 4,270.00 USD |
| `7D` | `0.8540` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 254.55 USD | 2,660.00 USD | 5,540.00 USD |
| `1D` | `0.8560` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 16,210.00 USD | 306.64 USD | 880.90 USD |
| `7D` | `0.8560` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 0.00 USD | 842.92 USD | 2,180.00 USD |
| `1D` | `0.8580` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 2,870.00 USD | 209.22 USD | 8,640.00 USD |
| `7D` | `0.8580` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 3,540.00 USD | 101.30 USD | 7,540.00 USD |
| `1D` | `0.8600` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 7,990.00 USD | 10,610.00 USD | 18,580.00 USD |
| `7D` | `0.8600` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 6,780.00 USD | 211.77 USD | 10,030.00 USD |
| `1D` | `0.8620` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 12,920.00 USD | 12,720.00 USD | 0.00 USD |
| `7D` | `0.8620` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 7,670.00 USD | 6,050.00 USD | 26,880.00 USD |
| `1D` | `0.8640` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 48,740.00 USD | 2,370.00 USD | 3,790.00 USD |
| `7D` | `0.8640` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 4,820.00 USD | 321.30 USD | 0.00 USD |
| `1D` | `0.8660` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD |
| `7D` | `0.8660` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 45,020.00 USD | 19,050.00 USD | 2,170.00 USD |
| `1D` | `0.8680` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 43,000.00 USD | 9,030.00 USD | 11,890.00 USD |
| `7D` | `0.8680` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 92,530.00 USD | 14,760.00 USD | 50,800.00 USD |
| `1D` | `0.8700` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 49,290.00 USD | 3,880.00 USD | 33,390.00 USD |
| `7D` | `0.8700` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 81,840.00 USD | 9,460.00 USD | 7,550.00 USD |
| `1D` | `0.8720` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 30,840.00 USD | 34,140.00 USD | 24,590.00 USD |
| `7D` | `0.8720` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 5,420.00 USD | 18,020.00 USD | 11,450.00 USD |
| `1D` | `0.8740` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 59,860.00 USD | 12,180.00 USD | 33,580.00 USD |
| `7D` | `0.8740` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 0.00 USD | 12,360.00 USD | 3,200.00 USD |
| `1D` | `0.8760` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 16,700.00 USD | 5,410.00 USD | 1,470.00 USD |
| `7D` | `0.8760` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 766.43 USD | 0.00 USD | 5,750.00 USD |
| `1D` | `0.8780` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 0.00 USD | 214.09 USD | 54,890.00 USD |
| `7D` | `0.8780` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 1,500.00 USD | 0.00 USD | 33,650.00 USD |
| `1D` | `0.8800` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 10,360.00 USD | 16.72 USD | 7,750.00 USD |
| `7D` | `0.8800` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 0.00 USD | 5,580.00 USD | 51,030.00 USD |
| `1D` | `0.8820` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 0.00 USD | 10,010.00 USD | 0.00 USD |
| `7D` | `0.8820` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 454.20 USD | 9,500.00 USD | 0.00 USD |
| `1D` | `0.8840` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 1,770.00 USD | 17,420.00 USD | 8,890.00 USD |
| `7D` | `0.8840` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 2,090.00 USD | 6,440.00 USD | 15,690.00 USD |
| `1D` | `0.8860` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 66,480.00 USD | 27,710.00 USD | 2,350.00 USD |
| `7D` | `0.8860` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 141,730.00 USD | 22,320.00 USD | 78,280.00 USD |
| `1D` | `0.8880` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 73,700.00 USD | 14,120.00 USD | 36,640.00 USD |
| `7D` | `0.8880` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 130,140.00 USD | 31,410.00 USD | 9,920.00 USD |
| `1D` | `0.8900` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 2,730.00 USD | 51,750.00 USD | 910.96 USD |
| `7D` | `0.8900` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 108,250.00 USD | 45,590.00 USD | 30,420.00 USD |
| `1D` | `0.8920` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 45,630.00 USD | 32,720.00 USD | 56,100.00 USD |
| `7D` | `0.8920` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 46,210.00 USD | 38,810.00 USD | 14,520.00 USD |
| `1D` | `0.8940` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 13,790.00 USD | 18,130.00 USD | 1,980.00 USD |
| `7D` | `0.8940` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 45,210.00 USD | 12,120.00 USD | 26,470.00 USD |
| `1D` | `0.8960` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 2,010.00 USD | 26,370.00 USD | 5,550.00 USD |
| `7D` | `0.8960` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 0.00 USD | 32,500.00 USD | 93,060.00 USD |
| `1D` | `0.8980` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 0.00 USD | 26,620.00 USD | 16,170.00 USD |
| `7D` | `0.8980` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 0.00 USD | 17,870.00 USD | 0.00 USD |
| `1D` | `0.9000` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 10,050.00 USD | 0.00 USD |
| `7D` | `0.9000` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 0.00 USD | 22,600.00 USD | 0.00 USD |
| `1D` | `0.9020` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 538.90 USD | 9,990.00 USD | 1,590.00 USD |
| `7D` | `0.9020` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 0.00 USD | 44,210.00 USD | 23,430.00 USD |
| `1D` | `0.9040` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 7,870.00 USD | 21,080.00 USD | 17,930.00 USD |
| `7D` | `0.9040` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 0.00 USD | 12,290.00 USD | 0.00 USD |
| `1D` | `0.9060` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 19,570.00 USD | 35.10 USD | 7,720.00 USD |
| `7D` | `0.9060` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 1,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9080` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 7,220.00 USD | 6,560.00 USD | 0.00 USD |
| `1D` | `0.9100` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 404.79 USD |
| `1D` | `0.9120` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 27,150.00 USD | 3,440.00 USD | 2,870.00 USD |
| `1D` | `0.9140` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 7,740.00 USD | 3,740.00 USD | 23,680.00 USD |
| `7D` | `0.9140` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 0.00 USD | 515.41 USD | 36,400.00 USD |
| `1D` | `0.9160` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 0.00 USD | 5,930.00 USD | 10,930.00 USD |
| `7D` | `0.9160` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 9,800.00 USD |
| `1D` | `0.9180` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 8,160.00 USD |
| `7D` | `0.9180` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 23,380.00 USD |
| `1D` | `0.9200` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 5,710.00 USD | 2,090.00 USD | 3,710.00 USD |
| `7D` | `0.9200` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 3,970.00 USD |
| `1D` | `0.9220` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 48.22 USD |
| `7D` | `0.9220` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 152,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9240` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 77,940.00 USD | 8,630.00 USD | 0.00 USD |
| `7D` | `0.9240` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 145,560.00 USD | 12,790.00 USD | 29,500.00 USD |
| `1D` | `0.9260` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 898.50 USD | 39,060.00 USD | 31,770.00 USD |
| `7D` | `0.9260` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 32,300.00 USD | 0.00 USD |
| `1D` | `0.9280` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 78,050.00 USD | 4,120.00 USD | 66,550.00 USD |
| `7D` | `0.9280` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 0.00 USD | 24,550.00 USD | 1,600.00 USD |
| `1D` | `0.9300` | 916,190.00 USD | 0.00 USD | 916,190.00 USD | 0.00 USD | 12,290.00 USD | 1,200.00 USD |
| `1D` | `0.9320` | 902,700.00 USD | 0.00 USD | 902,700.00 USD | 7,440.00 USD | 68.90 USD | 11,160.00 USD |
| `7D` | `0.9320` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 37,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9340` | 884,030.00 USD | 0.00 USD | 884,030.00 USD | 93,080.00 USD | 15,060.00 USD | 38,820.00 USD |
| `7D` | `0.9340` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 0.00 USD | 11,160.00 USD | 32,130.00 USD |
| `1D` | `0.9360` | 737,070.00 USD | 0.00 USD | 737,070.00 USD | 90,760.00 USD | 45,310.00 USD | 29,660.00 USD |
| `7D` | `0.9360` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 8,250.00 USD | 0.00 USD | 68,130.00 USD |
| `1D` | `0.9380` | 571,340.00 USD | 0.00 USD | 571,340.00 USD | 54,410.00 USD | 17,230.00 USD | 14,830.00 USD |
| `7D` | `0.9380` | 953,250.00 USD | 0.00 USD | 953,250.00 USD | 42,660.00 USD | 19,540.00 USD | 27,700.00 USD |
| `1D` | `0.9400` | 484,880.00 USD | 0.00 USD | 484,880.00 USD | 88,450.00 USD | 36,910.00 USD | 0.00 USD |
| `7D` | `0.9400` | 863,360.00 USD | 0.00 USD | 863,360.00 USD | 75,540.00 USD | 32,570.00 USD | 47,300.00 USD |
| `1D` | `0.9420` | 359,510.00 USD | 0.00 USD | 359,510.00 USD | 101,680.00 USD | 20,480.00 USD | 36,170.00 USD |
| `7D` | `0.9420` | 707,950.00 USD | 0.00 USD | 707,950.00 USD | 106,320.00 USD | 7,050.00 USD | 4,780.00 USD |
| `1D` | `0.9440` | 201,180.00 USD | 0.00 USD | 201,180.00 USD | 135,580.00 USD | 34,100.00 USD | 31,500.00 USD |
| `7D` | `0.9440` | 589,810.00 USD | 0.00 USD | 589,810.00 USD | 102,440.00 USD | 49,100.00 USD | 57,320.00 USD |
| `1D` | `0.9460` | 206,430.00 USD | 206,430.00 USD | 0.00 USD | 89,630.00 USD | 54,970.00 USD | 61,820.00 USD |
| `1D` | `0.9460` | 412,860.00 USD | 412,860.00 USD | 0.00 USD | 89,630.00 USD | 54,970.00 USD | 61,820.00 USD |
| `7D` | `0.9460` | 380,950.00 USD | 0.00 USD | 380,950.00 USD | 286,390.00 USD | 27,270.00 USD | 67,290.00 USD |
| `1D` | `0.9480` | 595,030.00 USD | 595,030.00 USD | 0.00 USD | 103,240.00 USD | 4,720.00 USD | 74,210.00 USD |
| `7D` | `0.9480` | 298,700.00 USD | 298,700.00 USD | 0.00 USD | 193,280.00 USD | 10,340.00 USD | 95,080.00 USD |
| `7D` | `0.9480` | 597,400.00 USD | 597,400.00 USD | 0.00 USD | 193,280.00 USD | 10,340.00 USD | 95,080.00 USD |
| `1D` | `0.9500` | 675,210.00 USD | 675,210.00 USD | 0.00 USD | 80,090.00 USD | 85.68 USD | 0.00 USD |
| `7D` | `0.9500` | 821,820.00 USD | 821,820.00 USD | 0.00 USD | 196,070.00 USD | 18,830.00 USD | 9,530.00 USD |
| `1D` | `0.9520` | 693,350.00 USD | 693,350.00 USD | 0.00 USD | 0.00 USD | 18,130.00 USD | 0.00 USD |
| `7D` | `0.9520` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 175,720.00 USD | 9,750.00 USD | 0.00 USD |
| `1D` | `0.9540` | 751,300.00 USD | 751,300.00 USD | 0.00 USD | 48,110.00 USD | 9,840.00 USD | 0.00 USD |
| `7D` | `0.9540` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 9,460.00 USD | 0.00 USD |
| `1D` | `0.9560` | 777,060.00 USD | 777,060.00 USD | 0.00 USD | 10,720.00 USD | 15,050.00 USD | 0.00 USD |
| `7D` | `0.9560` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 28,100.00 USD | 0.00 USD |
| `1D` | `0.9580` | 781,940.00 USD | 781,940.00 USD | 0.00 USD | 4,400.00 USD | 0.00 USD | 471.48 USD |
| `7D` | `0.9580` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 3,880.00 USD | 6,110.00 USD | 957.94 USD |
| `1D` | `0.9600` | 791,820.00 USD | 791,820.00 USD | 0.00 USD | 3,440.00 USD | 4,720.00 USD | 1,720.00 USD |
| `7D` | `0.9600` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 17,690.00 USD | 4,660.00 USD | 866.69 USD |
| `1D` | `0.9620` | 887,330.00 USD | 887,330.00 USD | 0.00 USD | 71,510.00 USD | 7,410.00 USD | 16,600.00 USD |
| `7D` | `0.9620` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 17,990.00 USD | 16,630.00 USD | 0.00 USD |
| `1D` | `0.9640` | 965,250.00 USD | 965,250.00 USD | 0.00 USD | 19,400.00 USD | 30,520.00 USD | 28,000.00 USD |
| `7D` | `0.9640` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 95,370.00 USD | 7,500.00 USD | 12,040.00 USD |
| `1D` | `0.9660` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 2,700.00 USD | 4,970.00 USD | 37,190.00 USD |
| `7D` | `0.9660` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 5,050.00 USD | 5,170.00 USD | 778.15 USD |
| `1D` | `0.9680` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 39,090.00 USD | 15,070.00 USD | 1,320.00 USD |
| `7D` | `0.9680` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 38,090.00 USD | 5,870.00 USD | 0.00 USD |
| `1D` | `0.9700` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 16,500.00 USD | 4,190.00 USD | 33,870.00 USD |
| `7D` | `0.9700` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 30,140.00 USD | 30,500.00 USD |
| `1D` | `0.9720` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 24,360.00 USD | 395.16 USD | 64,940.00 USD |
| `7D` | `0.9720` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 1,430.00 USD | 3,960.00 USD | 31,370.00 USD |
| `1D` | `0.9740` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 25,800.00 USD | 5,170.00 USD | 27,930.00 USD |
| `7D` | `0.9740` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 1,480.00 USD | 25,640.00 USD | 76,600.00 USD |
| `1D` | `0.9760` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 53,500.00 USD | 24,670.00 USD | 20,220.00 USD |
| `7D` | `0.9760` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 51,990.00 USD | 16,870.00 USD | 9,280.00 USD |
| `1D` | `0.9780` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 40,740.00 USD | 3,080.00 USD | 16,650.00 USD |
| `7D` | `0.9780` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,280.00 USD |
| `1D` | `0.9800` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 34,990.00 USD | 9,680.00 USD | 20,300.00 USD |
| `7D` | `0.9800` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 152,470.00 USD |
| `1D` | `0.9820` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 22,110.00 USD | 11,710.00 USD | 7,280.00 USD |
| `7D` | `0.9820` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 53,310.00 USD | 15,990.00 USD | 104,160.00 USD |
| `1D` | `0.9840` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 665.59 USD | 13,380.00 USD | 38,710.00 USD |
| `7D` | `0.9840` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 49,930.00 USD | 211.77 USD | 22,300.00 USD |
| `1D` | `0.9860` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 50,550.00 USD | 3,630.00 USD | 24,820.00 USD |
| `7D` | `0.9860` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,390.00 USD |
| `1D` | `0.9880` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 17,200.00 USD | 1,570.00 USD | 16,960.00 USD |
| `7D` | `0.9880` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 67,460.00 USD |
| `1D` | `0.9900` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 61,110.00 USD | 1,320.00 USD | 28,530.00 USD |
| `7D` | `0.9900` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 16,590.00 USD |
| `1D` | `0.9920` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 9,580.00 USD | 4,160.00 USD | 32,100.00 USD |
| `7D` | `0.9920` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 1,570.00 USD | 479.24 USD | 31,040.00 USD |
| `1D` | `0.9940` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 25,660.00 USD | 10,700.00 USD | 10,030.00 USD |
| `7D` | `0.9940` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 29,270.00 USD | 0.00 USD | 39,460.00 USD |
| `1D` | `0.9960` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 19,070.00 USD | 3,600.00 USD | 7,450.00 USD |
| `7D` | `0.9960` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 75,810.00 USD | 5,380.00 USD | 43,230.00 USD |
| `1D` | `0.9980` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 53,920.00 USD | 10,730.00 USD | 15,870.00 USD |
| `7D` | `0.9980` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 53,110.00 USD | 6,740.00 USD | 4,210.00 USD |
| `1D` | `1.00` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 60,660.00 USD | 18,230.00 USD | 6,760.00 USD |
| `7D` | `1.00` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 462.12 USD |
| `1D` | `1.00` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 16,570.00 USD | 1,970.00 USD | 7,440.00 USD |
| `7D` | `1.00` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 56,560.00 USD | 21,850.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 10,790.00 USD | 9,550.00 USD | 9,410.00 USD |
| `7D` | `1.00` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 70,950.00 USD | 3,970.00 USD | 1,470.00 USD |
| `1D` | `1.01` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 101,040.00 USD | 10,160.00 USD | 25,320.00 USD |
| `7D` | `1.01` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 46,710.00 USD | 0.00 USD | 11,560.00 USD |
| `1D` | `1.01` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 22,410.00 USD | 9,170.00 USD | 30,960.00 USD |
| `7D` | `1.01` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44,430.00 USD |
| `1D` | `1.01` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 12,560.00 USD | 17,230.00 USD | 971.85 USD |
| `7D` | `1.01` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 10,260.00 USD | 14,180.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 16,880.00 USD | 22,370.00 USD | 265.91 USD |
| `7D` | `1.01` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 33,230.00 USD | 30,100.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 6,560.00 USD | 5,790.00 USD | 21,570.00 USD |
| `7D` | `1.01` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 2,870.00 USD | 28,450.00 USD | 735.11 USD |
| `1D` | `1.02` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 15,150.00 USD | 25,460.00 USD | 11,300.00 USD |
| `7D` | `1.02` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 526.60 USD | 28,470.00 USD | 11,910.00 USD |
| `1D` | `1.02` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 26,110.00 USD | 4,240.00 USD | 22,530.00 USD |
| `7D` | `1.02` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 1,430.00 USD | 25,010.00 USD | 21,560.00 USD |
| `1D` | `1.02` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 47,410.00 USD | 9,980.00 USD | 18,380.00 USD |
| `7D` | `1.02` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 33,820.00 USD | 84,220.00 USD | 44,250.00 USD |
| `1D` | `1.02` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 35,050.00 USD | 20,320.00 USD | 27,460.00 USD |
| `7D` | `1.02` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 56,930.00 USD | 52,610.00 USD | 112,030.00 USD |
| `1D` | `1.02` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 44,050.00 USD | 9,760.00 USD | 34,590.00 USD |
| `7D` | `1.02` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 78,220.00 USD | 56,700.00 USD | 86,740.00 USD |
| `1D` | `1.03` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 36,400.00 USD | 18,290.00 USD | 17,280.00 USD |
| `7D` | `1.03` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 22,650.00 USD | 124,880.00 USD | 33,130.00 USD |
| `1D` | `1.03` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 15,280.00 USD | 8,920.00 USD | 15,510.00 USD |
| `7D` | `1.03` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 250,310.00 USD | 50,530.00 USD | 24,480.00 USD |
| `1D` | `1.03` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 64,370.00 USD | 12,650.00 USD | 18,360.00 USD |
| `7D` | `1.03` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 134,200.00 USD | 33,660.00 USD | 19,120.00 USD |
| `1D` | `1.03` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 30,350.00 USD | 7,050.00 USD | 32,130.00 USD |
| `7D` | `1.03` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD |
| `1D` | `1.03` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 12,070.00 USD | 8,650.00 USD | 12,980.00 USD |
| `7D` | `1.03` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 217,210.00 USD | 8,290.00 USD | 4,310.00 USD |
| `1D` | `1.04` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 4,320.00 USD | 10,280.00 USD | 2,970.00 USD |
| `7D` | `1.04` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 262,550.00 USD | 3,170.00 USD | 42,930.00 USD |
| `1D` | `1.04` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 42,730.00 USD | 767.34 USD | 2,900.00 USD |
| `7D` | `1.04` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 178,400.00 USD | 1,290.00 USD | 199,090.00 USD |
| `1D` | `1.04` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 6,280.00 USD | 6,670.00 USD | 8,460.00 USD |
| `7D` | `1.04` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 279,840.00 USD | 9,430.00 USD | 93,080.00 USD |
| `1D` | `1.04` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 10,930.00 USD | 5,820.00 USD | 3,380.00 USD |
| `7D` | `1.04` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD |
| `1D` | `1.04` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 2,950.00 USD | 1,330.00 USD | 10,840.00 USD |
| `7D` | `1.04` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD |
| `1D` | `1.05` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 5,280.00 USD | 4,540.00 USD | 1,200.00 USD |
| `7D` | `1.05` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD |
| `1D` | `1.05` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 4,070.00 USD | 73.95 USD | 9,870.00 USD |
| `7D` | `1.05` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 199,320.00 USD | 28,070.00 USD | 167,700.00 USD |
| `1D` | `1.05` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 29,490.00 USD | 4,070.00 USD | 8,230.00 USD |
| `7D` | `1.05` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 92,710.00 USD | 29,070.00 USD | 41,030.00 USD |
| `1D` | `1.05` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 4,960.00 USD | 1,200.00 USD | 16,730.00 USD |
| `7D` | `1.05` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 140,530.00 USD | 49,780.00 USD | 143,430.00 USD |
| `1D` | `1.05` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 10,950.00 USD | 345.49 USD | 2,970.00 USD |
| `7D` | `1.05` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 88,940.00 USD | 44,290.00 USD | 36,750.00 USD |
| `1D` | `1.06` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 6,010.00 USD | 4,840.00 USD | 3,790.00 USD |
| `7D` | `1.06` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 187,610.00 USD | 48,000.00 USD | 121,890.00 USD |
| `1D` | `1.06` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.06` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 205,290.00 USD | 63,350.00 USD | 94,840.00 USD |
| `7D` | `1.06` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 217,790.00 USD | 73,000.00 USD | 125,100.00 USD |
| `7D` | `1.06` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 131,720.00 USD | 83,000.00 USD | 66,000.00 USD |
| `7D` | `1.06` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 102,750.00 USD | 49,310.00 USD | 92,130.00 USD |
| `7D` | `1.07` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 77,920.00 USD | 32,860.00 USD | 73,060.00 USD |
| `7D` | `1.07` | 9,920,000.00 USD | 9,920,000.00 USD | 0.00 USD | 221,410.00 USD | 30,180.00 USD | 93,450.00 USD |
| `7D` | `1.07` | 10,120,000.00 USD | 10,120,000.00 USD | 0.00 USD | 121,300.00 USD | 33,170.00 USD | 42,800.00 USD |
| `7D` | `1.07` | 10,340,000.00 USD | 10,340,000.00 USD | 0.00 USD | 103,500.00 USD | 37,730.00 USD | 83,520.00 USD |
| `7D` | `1.07` | 10,540,000.00 USD | 10,540,000.00 USD | 0.00 USD | 92,440.00 USD | 21,500.00 USD | 83,440.00 USD |
| `7D` | `1.08` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 103,110.00 USD | 18,720.00 USD | 27,400.00 USD |
| `7D` | `1.08` | 10,960,000.00 USD | 10,960,000.00 USD | 0.00 USD | 158,650.00 USD | 40,740.00 USD | 69,670.00 USD |
| `7D` | `1.08` | 11,190,000.00 USD | 11,190,000.00 USD | 0.00 USD | 176,790.00 USD | 25,790.00 USD | 31,240.00 USD |
| `7D` | `1.08` | 11,220,000.00 USD | 11,220,000.00 USD | 0.00 USD | 34,550.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `175.09M` | Total OI Tokens: `185,507,059.6 DOT`
  * 1h OI Change: `-0.31%` | 4h OI Change: `-8.95%` | 24h OI Change: `-15.58%`
  * Exchange Breakdown: Binance=`34.63M` | Bybit=`22.22M` | OKX=`10.04M` | Hyperliquid=`5.88M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.03K` | Last 24h: `2.25K` | Last 3d: `-11.45K` | Last 7d: `-19.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0090%` | **USDT OKX** | `-0.0161%` |
| **USDT Bybit** | `0.0010%` | **USDT KuCoin** | `-0.0201%` |
| **USDT MEXC** | `0.0095%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0044%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-0.0058%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `30.41%` | `69.59%` | `0.44` | 28,280,000.00 USD |
| `15M` | `Binance` | `34.41%` | `65.59%` | `0.52` | 10,300,000.00 USD |
| `15M` | `OKX` | `32.14%` | `67.86%` | `0.47` | 3,560,000.00 USD |
| `15M` | `Bybit` | `35.19%` | `64.81%` | `0.54` | 3,640,000.00 USD |
| `15M` | `KuCoin` | `40.02%` | `59.98%` | `0.67` | 122,630.00 USD |
| `15M` | `Gate` | `24.97%` | `75.03%` | `0.33` | 722,690.00 USD |
| `15M` | `Bitget` | `26.34%` | `73.66%` | `0.36` | 1,570,000.00 USD |
| `15M` | `BingX` | `16.74%` | `83.26%` | `0.20` | 2,800,000.00 USD |
| `15M` | `MEXC` | `28.97%` | `71.03%` | `0.41` | 1,480,000.00 USD |
| `15M` | `Bitunix` | `22.52%` | `77.48%` | `0.29` | 585,500.00 USD |
| `15M` | `Hyperliquid` | `20.47%` | `79.53%` | `0.26` | 2,490,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `35.88%` | `64.12%` | `0.56` | 131,740.00 USD |
| `15M` | `Crypto.com` | `75%` | `25%` | `3.00` | 1,560.00 USD |
| `15M` | `WhiteBIT` | `97.93%` | `2.07%` | `47.31` | 336,230.00 USD |
| `15M` | `HTX` | `29.21%` | `70.79%` | `0.41` | 59,980.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `16.45%` | `83.55%` | `0.20` | 138,760.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `8.52%` | `91.48%` | `0.09` | 331,120.00 USD |
| `15M` | `Whale Positions` | `34.41%` | `65.59%` | `0.52` | 10,300,000.00 USD |
| `15M` | `Global Accounts` | `30.41%` | `69.59%` | `0.44` | 28,280,000.00 USD |
| `1H` | `DOT` | `38.56%` | `61.44%` | `0.63` | 17,030,000.00 USD |
| `1H` | `Binance` | `41.8%` | `58.2%` | `0.72` | 6,200,000.00 USD |
| `1H` | `OKX` | `37.96%` | `62.04%` | `0.61` | 1,120,000.00 USD |
| `1H` | `Bybit` | `38.39%` | `61.61%` | `0.62` | 1,620,000.00 USD |
| `1H` | `KuCoin` | `29.67%` | `70.33%` | `0.42` | 71,170.00 USD |
| `1H` | `Gate` | `41.81%` | `58.19%` | `0.72` | 536,570.00 USD |
| `1H` | `Bitget` | `35.95%` | `64.05%` | `0.56` | 260,520.00 USD |
| `1H` | `BingX` | `28.38%` | `71.62%` | `0.40` | 2,930,000.00 USD |
| `1H` | `MEXC` | `37.94%` | `62.06%` | `0.61` | 720,420.00 USD |
| `1H` | `Bitunix` | `34.29%` | `65.71%` | `0.52` | 292,880.00 USD |
| `1H` | `Hyperliquid` | `30.62%` | `69.38%` | `0.44` | 65,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `38.28%` | `61.72%` | `0.62` | 3,100,000.00 USD |
| `1H` | `Crypto.com` | `46.97%` | `53.03%` | `0.89` | 688.16 USD |
| `1H` | `WhiteBIT` | `99.55%` | `0.45%` | `221.22` | 78,880.00 USD |
| `1H` | `HTX` | `25.2%` | `74.8%` | `0.34` | 5,310.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `28.87%` | `71.13%` | `0.41` | 9,830.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `14.66%` | `85.34%` | `0.17` | 26,930.00 USD |
| `1H` | `Whale Positions` | `41.8%` | `58.2%` | `0.72` | 6,200,000.00 USD |
| `1H` | `Global Accounts` | `38.56%` | `61.44%` | `0.63` | 17,030,000.00 USD |
| `4H` | `DOT` | `52.89%` | `47.11%` | `1.12` | 302,310,000.00 USD |
| `4H` | `Binance` | `52.05%` | `47.95%` | `1.09` | 120,030,000.00 USD |
| `4H` | `OKX` | `52.67%` | `47.33%` | `1.11` | 37,580,000.00 USD |
| `4H` | `Bybit` | `52.5%` | `47.5%` | `1.11` | 41,350,000.00 USD |
| `4H` | `KuCoin` | `48.93%` | `51.07%` | `0.96` | 2,030,000.00 USD |
| `4H` | `Gate` | `54.21%` | `45.79%` | `1.18` | 11,420,000.00 USD |
| `4H` | `Bitget` | `51.05%` | `48.95%` | `1.04` | 17,710,000.00 USD |
| `4H` | `BingX` | `51.7%` | `48.3%` | `1.07` | 18,240,000.00 USD |
| `4H` | `MEXC` | `49.89%` | `50.11%` | `1.00` | 10,690,000.00 USD |
| `4H` | `Bitunix` | `49.53%` | `50.47%` | `0.98` | 7,190,000.00 USD |
| `4H` | `Hyperliquid` | `54.71%` | `45.29%` | `1.21` | 26,670,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.58%` | `51.42%` | `0.94` | 1,670,000.00 USD |
| `4H` | `Crypto.com` | `51.64%` | `48.36%` | `1.07` | 20,680.00 USD |
| `4H` | `WhiteBIT` | `92.58%` | `7.42%` | `12.48` | 4,930,000.00 USD |
| `4H` | `HTX` | `44.26%` | `55.74%` | `0.79` | 213,770.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `81.08%` | `18.92%` | `4.29` | 280,460.00 USD |
| `4H` | `Aster` | `52.52%` | `47.48%` | `1.11` | 627,950.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `43.83%` | `56.17%` | `0.78` | 1,660,000.00 USD |
| `4H` | `Whale Positions` | `52.05%` | `47.95%` | `1.09` | 120,030,000.00 USD |
| `4H` | `Global Accounts` | `52.89%` | `47.11%` | `1.12` | 302,310,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.9322` | `0.9317` | `0.9322` | `0.9342` | `0.9301` | 515,769.04 USD | 235,727.30 USD | 280,041.74 USD | -44,314.44 USD | `-8.59%` | `11B / 7S` |
| `0:00 UTC` | `0.9301` | `0.9291` | `0.9301` | `0.9327` | `0.9264` | 525,506.21 USD | 261,479.52 USD | 264,026.69 USD | -2,547.17 USD | `-0.48%` | `9B / 12S` |
| `5:00 UTC` | `0.9325` | `0.9314` | `0.9325` | `0.9344` | `0.9288` | 497,143.85 USD | 263,231.22 USD | 233,912.62 USD | 29,318.60 USD | `+5.90%` | `7B / 6S` |
| `0:00 UTC` | `0.9354` | `0.9348` | `0.9354` | `0.9365` | `0.9333` | 404,247.05 USD | 223,080.64 USD | 181,166.41 USD | 41,914.22 USD | `+10.37%` | `5B / 3S` |
| `5:00 UTC` | `0.9425` | `0.9411` | `0.9425` | `0.9454` | `0.9362` | 1,398,502.73 USD | 702,262.50 USD | 696,240.23 USD | 6,022.27 USD | `+0.43%` | `30B / 12S` |
| `0:00 UTC` | `0.9563` | `0.9497` | `0.9563` | `0.9570` | `0.9410` | 1,155,581.71 USD | 451,950.39 USD | 703,631.31 USD | -251,680.92 USD | `-21.78%` | `29B / 39S` |
| `5:00 UTC` | `0.9533` | `0.9521` | `0.9533` | `0.9545` | `0.9487` | 564,921.36 USD | 209,867.72 USD | 355,053.64 USD | -145,185.92 USD | `-25.70%` | `9B / 14S` |
| `0:00 UTC` | `0.9564` | `0.9543` | `0.9564` | `0.9570` | `0.9510` | 548,666.48 USD | 227,756.91 USD | 320,909.57 USD | -93,152.67 USD | `-16.98%` | `3B / 13S` |
| `5:00 UTC` | `0.9556` | `0.9547` | `0.9556` | `0.9604` | `0.9495` | 1,020,015.01 USD | 480,734.84 USD | 539,280.17 USD | -58,545.33 USD | `-5.74%` | `10B / 24S` |
| `0:00 UTC` | `0.9464` | `0.9464` | `0.9464` | `0.9523` | `0.9417` | 755,270.08 USD | 253,765.93 USD | 501,504.14 USD | -247,738.21 USD | `-32.80%` | `4B / 39S` |

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
| `5m` | -13,640.00 USD | -77,870.00 USD | **`DISTRIBUTION`** |
| `15m` | -128,260.00 USD | -262,180.00 USD | **`DISTRIBUTION`** |
| `30m` | 118,920.00 USD | -207,860.00 USD | **`DISTRIBUTION`** |
| `1h` | 82,210.00 USD | -717,300.00 USD | **`DISTRIBUTION`** |
| `2h` | 62,680.00 USD | -1,010,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 185,660.00 USD | -246,470.00 USD | **`DISTRIBUTION`** |
| `6h` | -160,570.00 USD | 948,510.00 USD | **`ACCUMULATION`** |
| `8h` | -51,920.00 USD | -1,740,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -948,880.00 USD | -5,610,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,080,000.00 USD | -6,740,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,800,000.00 USD | -23,140,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,530,000.00 USD | -77,550,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-13.64K` | 15m=`-128.26K` | 1h=`+82.21K` | 24h=`-1.08M`
* Futures Capital Netflows: 5m=`-77.87K` | 15m=`-262.18K` | 1h=`-717.30K` | 24h=`-6.74M`
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
  * `2026-10-30 11:03:46 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:38:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:37:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:39:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.8901` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.8475` (Risk Distance: `0.0426` pts)
  * +2.5R Take Profit: `0.9965`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9259` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9685` (Risk Distance: `0.0426` pts)
  * +2.5R Take Profit: `0.8195`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9531`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
