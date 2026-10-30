# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 11:29:21 IST` (`2026-10-30 05:59:21 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9400` | **Live Ask Quote**: `0.9610` | **Mid Price**: `0.9505`
- **Spread Points**: `21.00` | **Spread BPS**: `220.94 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.8995` | VWAP Z-Score: `+2.20` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0092` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `68.56` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.9602` | Lower -3.00σ Band: `0.8388`
  * Upper +2.51σ Band: `0.9503` | Lower -2.51σ Band: `0.8487`
  * Upper +2.01σ Band: `0.9402` | Lower -2.01σ Band: `0.8589`
  * Upper +2.00σ Band: `0.9400` | Lower -2.00σ Band: `0.8591`
  * Upper +1.28σ Band: `0.9254` | Lower -1.28σ Band: `0.8736`
  * Upper +1.00σ Band: `0.9197` | Lower -1.00σ Band: `0.8793`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9297` | EMA-20=`0.9213` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9285` (Slope: `+0.0000`) | EMA-100=`0.9448`
  * Institutional Anchors: EMA-144=`0.9535` | EMA-200=`0.9607` (Slope: `-0.4849`) | EMA-233=`0.9646`
- **Range Boundaries**: 24H High=`1.01` | 24H Low=`0.8570` | Weekly High=`1.03` | Weekly Low=`0.8570`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9259` (Distance: `+2.66%`)
  * Point of Control (POC) = `0.9119` (Distance: `+4.23%`)
  * Value Area Low (VAL) = `0.8907` (Distance: `+6.72%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.02` | Weekly POC=`0.9945` | Weekly VAL=`0.9713`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9330` | Low=`0.8570`
  * London Session (08:00-16:00 UTC): High=`0.9480` | Low=`0.9290`
  * New York Session (13:00-21:00 UTC): High=`0.9562` | Low=`0.9448`
  * Initial Balance (First Hour): IB High=`0.9480` | IB Low=`0.9290`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9467` - `0.9543`
  * Optimal Trade Entry (OTE 0.705): `0.9524`
  * Structural Invalidation Anchor (0.786): `0.9581`

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
| `BID/ASK` | None | `0.0000` | 0.00 USD | `0.00%` | Unarmored | `0.0%` | Interbank L2 | NONE |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:24:14 IST` |

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
| `7D` | `Long Liquidation` | `0.7700` | 4,860,000.00 USD | 4,860,000.00 USD | 5,540.00 USD | 1,600.00 USD | 5,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7720` | 4,850,000.00 USD | 4,850,000.00 USD | 4,990.00 USD | 0.00 USD | 2,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7725` | 3,840.00 USD | 160,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7740` | 4,840,000.00 USD | 4,840,000.00 USD | 5,450.00 USD | 0.00 USD | 3,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7760` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 147.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7775` | 2,490.00 USD | 156,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7780` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 3,100.00 USD | 53.43 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7795` | 272.83 USD | 154,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7800` | 4,830,000.00 USD | 4,830,000.00 USD | 436.65 USD | 25.30 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7820` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 1,920.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7840` | 4,830,000.00 USD | 4,830,000.00 USD | 227.10 USD | 1,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7860` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 2,250.00 USD | 365.01 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7865` | 292.03 USD | 153,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7880` | 4,820,000.00 USD | 4,820,000.00 USD | 5,690.00 USD | 2,050.00 USD | 723.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7900` | 4,820,000.00 USD | 4,820,000.00 USD | 6,940.00 USD | 2,650.00 USD | 4,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 277.39 USD | 153,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7920` | 4,800,000.00 USD | 4,800,000.00 USD | 12,590.00 USD | 2,180.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7940` | 4,780,000.00 USD | 4,780,000.00 USD | 15,680.00 USD | 2,500.00 USD | 13,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7960` | 4,740,000.00 USD | 4,740,000.00 USD | 4,520.00 USD | 7,120.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7980` | 4,730,000.00 USD | 4,730,000.00 USD | 16,210.00 USD | 3,000.00 USD | 14,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8000` | 4,700,000.00 USD | 4,700,000.00 USD | 10,100.00 USD | 5,540.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8020` | 4,680,000.00 USD | 4,680,000.00 USD | 8,990.00 USD | 4,460.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8040` | 4,660,000.00 USD | 4,660,000.00 USD | 5,500.00 USD | 2,170.00 USD | 940.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8060` | 4,650,000.00 USD | 4,650,000.00 USD | 16,390.00 USD | 10,990.00 USD | 10,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8080` | 4,610,000.00 USD | 4,610,000.00 USD | 1,570.00 USD | 1,230.00 USD | 10,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8100` | 4,600,000.00 USD | 4,600,000.00 USD | 2,890.00 USD | 2,010.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8120` | 4,590,000.00 USD | 4,590,000.00 USD | 15,720.00 USD | 3,030.00 USD | 9,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 153,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8140` | 4,560,000.00 USD | 4,560,000.00 USD | 32,880.00 USD | 6,050.00 USD | 15,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8160` | 4,500,000.00 USD | 4,500,000.00 USD | 38,200.00 USD | 10,180.00 USD | 6,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8180` | 4,450,000.00 USD | 4,450,000.00 USD | 12,550.00 USD | 2,560.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8200` | 4,420,000.00 USD | 4,420,000.00 USD | 1,740.00 USD | 1,570.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 152,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8220` | 4,410,000.00 USD | 4,410,000.00 USD | 20,390.00 USD | 6,820.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 749.96 USD | 150,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8240` | 4,380,000.00 USD | 4,380,000.00 USD | 23,160.00 USD | 93.73 USD | 11,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8260` | 4,350,000.00 USD | 4,350,000.00 USD | 5,220.00 USD | 3,490.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8280` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 3,910.00 USD | 1,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8300` | 4,330,000.00 USD | 4,330,000.00 USD | 9,280.00 USD | 4,780.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8320` | 3,330,000.00 USD | 3,330,000.00 USD | 2,670.00 USD | 1,950.00 USD | 3,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8320` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 401.80 USD | 77.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8340` | 3,320,000.00 USD | 3,320,000.00 USD | 25,550.00 USD | 5,650.00 USD | 8,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8340` | 4,310,000.00 USD | 4,310,000.00 USD | 35,710.00 USD | 10,960.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8360` | 3,280,000.00 USD | 3,280,000.00 USD | 1,870.00 USD | 636.81 USD | 14,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8360` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 844.23 USD | 311.26 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 149,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8380` | 3,260,000.00 USD | 3,260,000.00 USD | 16,380.00 USD | 1,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8380` | 4,260,000.00 USD | 4,260,000.00 USD | 15,240.00 USD | 633.60 USD | 539.92 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8400` | 3,240,000.00 USD | 3,240,000.00 USD | 458.00 USD | 1,050.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8400` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 798.38 USD | 8,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,570.00 USD | 149,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 3,240,000.00 USD | 3,240,000.00 USD | 1,340.00 USD | 4,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8420` | 4,240,000.00 USD | 4,240,000.00 USD | 6,400.00 USD | 4,650.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8435` | 751.39 USD | 148,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8440` | 3,230,000.00 USD | 3,230,000.00 USD | 2,210.00 USD | 5.65 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8440` | 4,220,000.00 USD | 4,220,000.00 USD | 7,170.00 USD | 24.80 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8460` | 3,230,000.00 USD | 3,230,000.00 USD | 15,140.00 USD | 6,600.00 USD | 25.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8460` | 4,220,000.00 USD | 4,220,000.00 USD | 2,560.00 USD | 427.62 USD | 2,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8480` | 3,210,000.00 USD | 3,210,000.00 USD | 6,670.00 USD | 230.58 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8480` | 4,210,000.00 USD | 4,210,000.00 USD | 26,310.00 USD | 10,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 147,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 3,200,000.00 USD | 3,200,000.00 USD | 8,440.00 USD | 371.56 USD | 744.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8500` | 4,170,000.00 USD | 4,170,000.00 USD | 2,050.00 USD | 477.96 USD | 4,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8515` | 2,700.00 USD | 146,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8520` | 3,190,000.00 USD | 3,190,000.00 USD | 1,230.00 USD | 1,940.00 USD | 12,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8520` | 4,170,000.00 USD | 4,170,000.00 USD | 5,900.00 USD | 669.43 USD | 226.67 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8540` | 3,180,000.00 USD | 3,180,000.00 USD | 2,300.00 USD | 4,910.00 USD | 4,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8540` | 4,160,000.00 USD | 4,160,000.00 USD | 254.55 USD | 2,660.00 USD | 5,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8560` | 3,160,000.00 USD | 3,160,000.00 USD | 16,210.00 USD | 306.64 USD | 880.90 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8560` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 842.92 USD | 2,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 143,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8580` | 3,150,000.00 USD | 3,150,000.00 USD | 2,410.00 USD | 209.22 USD | 6,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8580` | 4,150,000.00 USD | 4,150,000.00 USD | 3,540.00 USD | 101.30 USD | 1,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8600` | 3,140,000.00 USD | 3,140,000.00 USD | 7,580.00 USD | 10,610.00 USD | 17,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8600` | 4,140,000.00 USD | 4,140,000.00 USD | 6,780.00 USD | 211.77 USD | 10,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8605` | 25,780.00 USD | 142,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8615` | 181.17 USD | 116,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8620` | 3,100,000.00 USD | 3,100,000.00 USD | 12,920.00 USD | 12,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8620` | 4,130,000.00 USD | 4,130,000.00 USD | 7,670.00 USD | 6,050.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 116,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 3,080,000.00 USD | 3,080,000.00 USD | 48,740.00 USD | 2,370.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8640` | 4,080,000.00 USD | 4,080,000.00 USD | 4,820.00 USD | 321.30 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 116,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8660` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8660` | 4,080,000.00 USD | 4,080,000.00 USD | 45,020.00 USD | 19,050.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,390.00 USD | 116,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8680` | 3,020,000.00 USD | 3,020,000.00 USD | 43,000.00 USD | 9,030.00 USD | 11,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8680` | 4,010,000.00 USD | 4,010,000.00 USD | 92,530.00 USD | 14,760.00 USD | 50,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 12,590.00 USD | 114,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8700` | 2,960,000.00 USD | 2,960,000.00 USD | 49,290.00 USD | 3,880.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8700` | 3,860,000.00 USD | 3,860,000.00 USD | 81,840.00 USD | 9,460.00 USD | 7,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8715` | 92,580.00 USD | 102,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8720` | 2,870,000.00 USD | 2,870,000.00 USD | 30,840.00 USD | 34,140.00 USD | 24,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8720` | 3,760,000.00 USD | 3,760,000.00 USD | 5,420.00 USD | 18,020.00 USD | 11,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 2,780,000.00 USD | 2,780,000.00 USD | 59,860.00 USD | 12,180.00 USD | 33,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8740` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 12,360.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 2,670,000.00 USD | 2,670,000.00 USD | 16,700.00 USD | 5,410.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8760` | 3,710,000.00 USD | 3,710,000.00 USD | 766.43 USD | 0.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 9,560.00 USD | 9,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8780` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 214.09 USD | 54,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8780` | 3,700,000.00 USD | 3,700,000.00 USD | 1,500.00 USD | 0.00 USD | 33,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8800` | 2,590,000.00 USD | 2,590,000.00 USD | 10,360.00 USD | 16.72 USD | 7,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8800` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 5,580.00 USD | 51,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8820` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 10,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8820` | 3,610,000.00 USD | 3,610,000.00 USD | 454.20 USD | 9,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 2,570,000.00 USD | 2,570,000.00 USD | 1,980.00 USD | 17,420.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8840` | 3,600,000.00 USD | 3,600,000.00 USD | 2,090.00 USD | 6,440.00 USD | 15,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8860` | 2,540,000.00 USD | 2,540,000.00 USD | 66,480.00 USD | 28,300.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8860` | 3,570,000.00 USD | 3,570,000.00 USD | 141,730.00 USD | 22,320.00 USD | 78,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8880` | 2,440,000.00 USD | 2,440,000.00 USD | 73,700.00 USD | 14,120.00 USD | 36,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8880` | 3,330,000.00 USD | 3,330,000.00 USD | 130,140.00 USD | 31,410.00 USD | 9,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8900` | 2,320,000.00 USD | 2,320,000.00 USD | 1,430.00 USD | 51,750.00 USD | 910.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8900` | 3,160,000.00 USD | 3,160,000.00 USD | 108,260.00 USD | 45,590.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8920` | 2,260,000.00 USD | 2,260,000.00 USD | 45,630.00 USD | 32,720.00 USD | 56,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8920` | 2,980,000.00 USD | 2,980,000.00 USD | 46,210.00 USD | 38,810.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8940` | 2,130,000.00 USD | 2,130,000.00 USD | 13,790.00 USD | 18,130.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8940` | 2,880,000.00 USD | 2,880,000.00 USD | 45,210.00 USD | 12,120.00 USD | 26,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8960` | 2,090,000.00 USD | 2,090,000.00 USD | 2,010.00 USD | 26,370.00 USD | 5,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8960` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 32,500.00 USD | 93,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8980` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 26,620.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8980` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 17,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9000` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 10,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9000` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 22,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9020` | 2,010,000.00 USD | 2,010,000.00 USD | 538.90 USD | 9,990.00 USD | 1,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9020` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 44,210.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9040` | 2,000,000.00 USD | 2,000,000.00 USD | 7,870.00 USD | 21,080.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9040` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 12,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9060` | 1,950,000.00 USD | 1,950,000.00 USD | 17,830.00 USD | 35.10 USD | 7,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9060` | 2,550,000.00 USD | 2,550,000.00 USD | 1,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9080` | 1,920,000.00 USD | 1,920,000.00 USD | 7,220.00 USD | 6,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9100` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 404.79 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9120` | 1,910,000.00 USD | 1,910,000.00 USD | 27,150.00 USD | 2,020.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9140` | 1,880,000.00 USD | 1,880,000.00 USD | 4,020.00 USD | 3,740.00 USD | 16,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9140` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 515.41 USD | 20,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9160` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 5,930.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9160` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 9,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9180` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 8,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9180` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 23,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9200` | 1,830,000.00 USD | 1,830,000.00 USD | 5,710.00 USD | 2,090.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9200` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9220` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 48.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9220` | 2,490,000.00 USD | 2,490,000.00 USD | 152,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9240` | 1,820,000.00 USD | 1,820,000.00 USD | 77,940.00 USD | 8,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9240` | 2,330,000.00 USD | 2,330,000.00 USD | 145,560.00 USD | 12,790.00 USD | 29,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9260` | 1,730,000.00 USD | 1,730,000.00 USD | 898.50 USD | 39,060.00 USD | 31,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9260` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 32,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9280` | 1,660,000.00 USD | 1,660,000.00 USD | 78,050.00 USD | 4,120.00 USD | 66,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9280` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 24,550.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9300` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 9,460.00 USD | 366.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9320` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 68.90 USD | 6,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9320` | 2,090,000.00 USD | 2,090,000.00 USD | 37,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9340` | 1,500,000.00 USD | 1,500,000.00 USD | 93,080.00 USD | 15,100.00 USD | 27,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9340` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 11,160.00 USD | 768.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9360` | 1,360,000.00 USD | 1,360,000.00 USD | 90,760.00 USD | 45,310.00 USD | 23,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9360` | 2,040,000.00 USD | 2,040,000.00 USD | 8,250.00 USD | 0.00 USD | 68,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9380` | 1,200,000.00 USD | 1,200,000.00 USD | 54,410.00 USD | 17,230.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9380` | 1,960,000.00 USD | 1,960,000.00 USD | 42,660.00 USD | 19,540.00 USD | 27,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9400` | 1,110,000.00 USD | 1,110,000.00 USD | 88,450.00 USD | 36,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9400` | 1,870,000.00 USD | 1,870,000.00 USD | 75,540.00 USD | 32,570.00 USD | 47,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9420` | 989,280.00 USD | 989,280.00 USD | 101,680.00 USD | 20,480.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9420` | 1,720,000.00 USD | 1,720,000.00 USD | 106,320.00 USD | 7,050.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9440` | 830,950.00 USD | 830,950.00 USD | 140,870.00 USD | 34,100.00 USD | 31,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9440` | 1,600,000.00 USD | 1,600,000.00 USD | 102,440.00 USD | 49,100.00 USD | 57,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9460` | 624,480.00 USD | 624,480.00 USD | 89,630.00 USD | 54,970.00 USD | 61,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9460` | 1,390,000.00 USD | 1,390,000.00 USD | 286,390.00 USD | 27,270.00 USD | 67,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9480` | 418,050.00 USD | 418,050.00 USD | 103,240.00 USD | 10,350.00 USD | 74,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9480` | 1,010,000.00 USD | 1,010,000.00 USD | 193,280.00 USD | 10,340.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9500` | 230,250.00 USD | 230,250.00 USD | 105,450.00 USD | 17,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9500` | 709,430.00 USD | 709,430.00 USD | 196,070.00 USD | 18,830.00 USD | 166,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9520` | 107,370.00 USD | 107,370.00 USD | 31,280.00 USD | 18,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9520` | 327,800.00 USD | 327,800.00 USD | 175,720.00 USD | 9,750.00 USD | 142,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9540` | 57,950.00 USD | 57,950.00 USD | 48,110.00 USD | 9,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9540` | 9,460.00 USD | 9,460.00 USD | 0.00 USD | 9,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9540` | 18,920.00 USD | 18,920.00 USD | 0.00 USD | 9,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 25,770.00 USD | 25,770.00 USD | 10,720.00 USD | 15,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9560` | 47,020.00 USD | 47,020.00 USD | 0.00 USD | 28,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 30,640.00 USD | 30,640.00 USD | 4,400.00 USD | 0.00 USD | 471.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9580` | 57,970.00 USD | 57,970.00 USD | 3,880.00 USD | 6,110.00 USD | 957.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 40,520.00 USD | 40,520.00 USD | 3,440.00 USD | 4,720.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9600` | 81,190.00 USD | 81,190.00 USD | 17,690.00 USD | 4,660.00 USD | 866.69 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 136,030.00 USD | 136,030.00 USD | 71,510.00 USD | 7,410.00 USD | 16,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9620` | 115,820.00 USD | 115,820.00 USD | 17,990.00 USD | 16,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 213,950.00 USD | 213,950.00 USD | 19,400.00 USD | 30,520.00 USD | 28,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9640` | 230,720.00 USD | 230,720.00 USD | 95,370.00 USD | 7,500.00 USD | 12,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 258,800.00 USD | 258,800.00 USD | 2,700.00 USD | 4,970.00 USD | 37,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9660` | 241,720.00 USD | 241,720.00 USD | 5,050.00 USD | 5,170.00 USD | 778.15 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9680` | 310,610.00 USD | 310,610.00 USD | 39,090.00 USD | 12,230.00 USD | 482.60 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9680` | 285,680.00 USD | 285,680.00 USD | 38,090.00 USD | 5,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9695` | 14,120.00 USD | 14,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9700` | 353,290.00 USD | 353,290.00 USD | 9,060.00 USD | 4,190.00 USD | 29,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9700` | 346,320.00 USD | 346,320.00 USD | 0.00 USD | 30,140.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 431,780.00 USD | 431,780.00 USD | 24,360.00 USD | 395.16 USD | 53,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9720` | 351,710.00 USD | 351,710.00 USD | 1,430.00 USD | 3,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 484,550.00 USD | 484,550.00 USD | 25,800.00 USD | 5,170.00 USD | 21,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9740` | 455,470.00 USD | 455,470.00 USD | 1,480.00 USD | 25,640.00 USD | 76,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9745` | 214.00 USD | 14,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9755` | 345.62 USD | 14,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9760` | 582,950.00 USD | 582,950.00 USD | 53,500.00 USD | 24,670.00 USD | 20,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9760` | 533,610.00 USD | 533,610.00 USD | 51,990.00 USD | 16,870.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 643,410.00 USD | 643,410.00 USD | 40,740.00 USD | 3,080.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9780` | 557,900.00 USD | 557,900.00 USD | 0.00 USD | 0.00 USD | 24,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 708,380.00 USD | 708,380.00 USD | 34,990.00 USD | 9,680.00 USD | 20,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9800` | 710,370.00 USD | 710,370.00 USD | 0.00 USD | 0.00 USD | 152,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 749,480.00 USD | 749,480.00 USD | 22,110.00 USD | 11,710.00 USD | 7,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9820` | 883,830.00 USD | 883,830.00 USD | 53,310.00 USD | 15,990.00 USD | 104,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 802,240.00 USD | 802,240.00 USD | 665.59 USD | 13,380.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9840` | 956,280.00 USD | 956,280.00 USD | 49,930.00 USD | 211.77 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 881,240.00 USD | 881,240.00 USD | 50,550.00 USD | 3,630.00 USD | 24,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9860` | 957,660.00 USD | 957,660.00 USD | 0.00 USD | 0.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9880` | 915,140.00 USD | 915,140.00 USD | 17,200.00 USD | 151.21 USD | 16,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9880` | 1,070,000.00 USD | 1,070,000.00 USD | 40,020.00 USD | 0.00 USD | 67,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 994,760.00 USD | 994,760.00 USD | 57,390.00 USD | 1,320.00 USD | 20,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9900` | 1,090,000.00 USD | 1,090,000.00 USD | 20,530.00 USD | 0.00 USD | 906.61 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 1,040,000.00 USD | 1,040,000.00 USD | 9,580.00 USD | 4,160.00 USD | 28,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9920` | 1,120,000.00 USD | 1,120,000.00 USD | 1,570.00 USD | 479.24 USD | 31,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 1,080,000.00 USD | 1,080,000.00 USD | 25,660.00 USD | 10,700.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9940` | 1,190,000.00 USD | 1,190,000.00 USD | 29,270.00 USD | 0.00 USD | 39,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 1,110,000.00 USD | 1,110,000.00 USD | 19,070.00 USD | 3,600.00 USD | 7,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9960` | 1,310,000.00 USD | 1,310,000.00 USD | 75,810.00 USD | 5,380.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 1,190,000.00 USD | 1,190,000.00 USD | 53,920.00 USD | 10,730.00 USD | 15,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9980` | 1,380,000.00 USD | 1,380,000.00 USD | 53,110.00 USD | 6,740.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,280,000.00 USD | 1,280,000.00 USD | 60,660.00 USD | 18,230.00 USD | 6,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 1,430,000.00 USD | 1,430,000.00 USD | 52,850.00 USD | 0.00 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,300,000.00 USD | 1,300,000.00 USD | 14,830.00 USD | 1,970.00 USD | 7,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 1,530,000.00 USD | 1,530,000.00 USD | 56,570.00 USD | 21,850.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,330,000.00 USD | 1,330,000.00 USD | 10,790.00 USD | 9,550.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 1,600,000.00 USD | 1,600,000.00 USD | 70,950.00 USD | 3,970.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 1,470,000.00 USD | 1,470,000.00 USD | 101,040.00 USD | 10,160.00 USD | 25,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 1,660,000.00 USD | 1,660,000.00 USD | 46,710.00 USD | 0.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 221.13 USD | 14,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.01` | 1,530,000.00 USD | 1,530,000.00 USD | 22,410.00 USD | 9,170.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 44,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 1,560,000.00 USD | 1,560,000.00 USD | 12,560.00 USD | 17,230.00 USD | 971.85 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 1,730,000.00 USD | 1,730,000.00 USD | 10,260.00 USD | 14,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 1,600,000.00 USD | 1,600,000.00 USD | 16,880.00 USD | 22,370.00 USD | 265.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 1,790,000.00 USD | 1,790,000.00 USD | 33,230.00 USD | 30,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 1,640,000.00 USD | 1,640,000.00 USD | 6,560.00 USD | 5,790.00 USD | 21,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 1,820,000.00 USD | 1,820,000.00 USD | 2,870.00 USD | 28,450.00 USD | 735.11 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,690,000.00 USD | 1,690,000.00 USD | 15,150.00 USD | 25,460.00 USD | 11,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 1,870,000.00 USD | 1,870,000.00 USD | 526.60 USD | 28,470.00 USD | 11,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,740,000.00 USD | 1,740,000.00 USD | 24,800.00 USD | 4,240.00 USD | 22,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 1,910,000.00 USD | 1,910,000.00 USD | 1,440.00 USD | 25,010.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,820,000.00 USD | 1,820,000.00 USD | 47,410.00 USD | 9,980.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,080,000.00 USD | 2,080,000.00 USD | 33,820.00 USD | 84,220.00 USD | 44,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,910,000.00 USD | 1,910,000.00 USD | 40,340.00 USD | 20,320.00 USD | 29,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,300,000.00 USD | 2,300,000.00 USD | 56,930.00 USD | 52,610.00 USD | 112,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,000,000.00 USD | 2,000,000.00 USD | 44,050.00 USD | 11,230.00 USD | 34,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,520,000.00 USD | 2,520,000.00 USD | 78,220.00 USD | 56,700.00 USD | 86,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,070,000.00 USD | 2,070,000.00 USD | 36,400.00 USD | 18,290.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,700,000.00 USD | 2,700,000.00 USD | 22,650.00 USD | 124,880.00 USD | 33,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,110,000.00 USD | 2,110,000.00 USD | 15,280.00 USD | 8,920.00 USD | 15,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,020,000.00 USD | 3,020,000.00 USD | 250,310.00 USD | 50,530.00 USD | 24,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,200,000.00 USD | 2,200,000.00 USD | 64,370.00 USD | 12,650.00 USD | 18,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,210,000.00 USD | 3,210,000.00 USD | 134,200.00 USD | 33,660.00 USD | 19,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,270,000.00 USD | 2,270,000.00 USD | 30,760.00 USD | 7,090.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,320,000.00 USD | 3,320,000.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,310,000.00 USD | 2,310,000.00 USD | 12,070.00 USD | 8,650.00 USD | 12,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,550,000.00 USD | 3,550,000.00 USD | 217,210.00 USD | 8,290.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,320,000.00 USD | 2,320,000.00 USD | 4,320.00 USD | 10,280.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,860,000.00 USD | 3,860,000.00 USD | 262,550.00 USD | 3,170.00 USD | 42,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,370,000.00 USD | 2,370,000.00 USD | 42,730.00 USD | 767.34 USD | 2,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 4,240,000.00 USD | 4,240,000.00 USD | 178,400.00 USD | 1,290.00 USD | 199,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 228.37 USD | 15,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,390,000.00 USD | 2,390,000.00 USD | 6,280.00 USD | 6,670.00 USD | 8,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 4,620,000.00 USD | 4,620,000.00 USD | 279,840.00 USD | 9,430.00 USD | 93,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,410,000.00 USD | 2,410,000.00 USD | 10,930.00 USD | 5,820.00 USD | 3,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 4,940,000.00 USD | 4,940,000.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,430,000.00 USD | 2,430,000.00 USD | 2,950.00 USD | 1,330.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,210,000.00 USD | 5,210,000.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,440,000.00 USD | 2,440,000.00 USD | 5,280.00 USD | 4,540.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 5,620,000.00 USD | 5,620,000.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 367.04 USD | 15,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,450,000.00 USD | 2,450,000.00 USD | 3,910.00 USD | 73.95 USD | 7,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 6,010,000.00 USD | 6,010,000.00 USD | 199,320.00 USD | 28,070.00 USD | 161,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,490,000.00 USD | 2,490,000.00 USD | 29,080.00 USD | 4,100.00 USD | 7,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 6,170,000.00 USD | 6,170,000.00 USD | 92,710.00 USD | 29,070.00 USD | 41,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,510,000.00 USD | 2,510,000.00 USD | 4,960.00 USD | 1,200.00 USD | 16,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 6,510,000.00 USD | 6,510,000.00 USD | 140,530.00 USD | 49,780.00 USD | 143,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,530,000.00 USD | 2,530,000.00 USD | 10,950.00 USD | 345.49 USD | 2,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 6,680,000.00 USD | 6,680,000.00 USD | 88,940.00 USD | 44,290.00 USD | 36,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 2,540,000.00 USD | 2,540,000.00 USD | 6,010.00 USD | 4,840.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 7,030,000.00 USD | 7,030,000.00 USD | 187,610.00 USD | 48,000.00 USD | 121,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 2,560,000.00 USD | 2,560,000.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 7,400,000.00 USD | 7,400,000.00 USD | 205,290.00 USD | 63,350.00 USD | 94,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 7,810,000.00 USD | 7,810,000.00 USD | 217,790.00 USD | 73,000.00 USD | 125,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,090,000.00 USD | 8,090,000.00 USD | 131,720.00 USD | 83,000.00 USD | 66,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,340,000.00 USD | 8,340,000.00 USD | 102,750.00 USD | 49,310.00 USD | 92,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 8,520,000.00 USD | 8,520,000.00 USD | 77,920.00 USD | 32,860.00 USD | 73,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 8,870,000.00 USD | 8,870,000.00 USD | 221,410.00 USD | 30,180.00 USD | 93,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 9,060,000.00 USD | 9,060,000.00 USD | 121,300.00 USD | 33,170.00 USD | 42,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 9,290,000.00 USD | 9,290,000.00 USD | 103,500.00 USD | 37,730.00 USD | 83,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 9,490,000.00 USD | 9,490,000.00 USD | 92,440.00 USD | 21,500.00 USD | 83,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 9,640,000.00 USD | 9,640,000.00 USD | 103,110.00 USD | 18,720.00 USD | 27,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 9,900,000.00 USD | 9,900,000.00 USD | 158,650.00 USD | 40,740.00 USD | 69,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 10,140,000.00 USD | 10,140,000.00 USD | 176,790.00 USD | 26,190.00 USD | 33,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.08` | 2,230.00 USD | 17,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.08` | 10,260,000.00 USD | 10,260,000.00 USD | 62,710.00 USD | 20,510.00 USD | 39,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 10,450,000.00 USD | 10,450,000.00 USD | 46,000.00 USD | 31,940.00 USD | 103,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 10,680,000.00 USD | 10,680,000.00 USD | 161,270.00 USD | 28,200.00 USD | 42,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 10,910,000.00 USD | 10,910,000.00 USD | 59,850.00 USD | 57,700.00 USD | 117,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 11,070,000.00 USD | 11,070,000.00 USD | 109,670.00 USD | 18,350.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 11,190,000.00 USD | 11,190,000.00 USD | 36,490.00 USD | 24,570.00 USD | 62,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 11,350,000.00 USD | 11,350,000.00 USD | 67,090.00 USD | 37,290.00 USD | 55,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 11,520,000.00 USD | 11,520,000.00 USD | 64,450.00 USD | 32,080.00 USD | 65,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 11,750,000.00 USD | 11,750,000.00 USD | 118,930.00 USD | 21,050.00 USD | 97,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 12,020,000.00 USD | 12,020,000.00 USD | 165,350.00 USD | 61,190.00 USD | 40,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 12,090,000.00 USD | 12,090,000.00 USD | 56,270.00 USD | 10,900.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.7710` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 10,530.00 USD | 1,600.00 USD | 5,080.00 USD |
| `7D` | `0.7730` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 4,750.00 USD | 0.00 USD | 2,230.00 USD |
| `7D` | `0.7750` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 698.40 USD | 0.00 USD | 3,460.00 USD |
| `7D` | `0.7790` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 0.00 USD | 3,100.00 USD | 53.43 USD |
| `7D` | `0.7810` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 436.65 USD | 25.30 USD | 1,410.00 USD |
| `7D` | `0.7830` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 114.15 USD | 1,980.00 USD | 0.00 USD |
| `7D` | `0.7850` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 112.95 USD | 2,340.00 USD | 180.30 USD |
| `7D` | `0.7870` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 5,690.00 USD | 3,090.00 USD | 450.49 USD |
| `7D` | `0.7890` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 88.75 USD | 0.00 USD | 2,110.00 USD |
| `7D` | `0.7910` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD |
| `7D` | `0.7930` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 20,360.00 USD | 1,560.00 USD | 6,130.00 USD |
| `7D` | `0.7950` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 3,290.00 USD | 8,430.00 USD | 14,710.00 USD |
| `7D` | `0.7970` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 10,100.00 USD | 1,130.00 USD | 522.30 USD |
| `7D` | `0.7990` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 20,360.00 USD | 6,180.00 USD | 13,950.00 USD |
| `7D` | `0.8010` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 5,420.00 USD | 5,300.00 USD | 2,300.00 USD |
| `7D` | `0.8030` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 4,550.00 USD | 2,440.00 USD | 10,410.00 USD |
| `7D` | `0.8050` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD |
| `7D` | `0.8070` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 12,160.00 USD | 4,660.00 USD | 16,650.00 USD |
| `7D` | `0.8090` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD |
| `7D` | `0.8110` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD |
| `7D` | `0.8130` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 14,060.00 USD | 2,970.00 USD | 9,350.00 USD |
| `7D` | `0.8150` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 61,120.00 USD | 7,590.00 USD | 19,500.00 USD |
| `7D` | `0.8170` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 10,780.00 USD | 8,770.00 USD | 9,670.00 USD |
| `7D` | `0.8190` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD |
| `7D` | `0.8210` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 7,510.00 USD | 3,290.00 USD | 10,030.00 USD |
| `7D` | `0.8230` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 29,430.00 USD | 5,100.00 USD | 13,220.00 USD |
| `7D` | `0.8250` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD |
| `7D` | `0.8270` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 4,320.00 USD | 5,770.00 USD | 616.76 USD |
| `7D` | `0.8290` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD |
| `7D` | `0.8310` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 9,280.00 USD | 1,660.00 USD | 2,450.00 USD |
| `1D` | `0.8320` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 2,670.00 USD | 1,950.00 USD | 3,580.00 USD |
| `7D` | `0.8330` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 16,220.00 USD | 11,360.00 USD | 77.95 USD |
| `1D` | `0.8340` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 25,550.00 USD | 5,650.00 USD | 8,980.00 USD |
| `7D` | `0.8350` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 19,490.00 USD | 0.00 USD | 2,290.00 USD |
| `1D` | `0.8360` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 1,870.00 USD | 636.81 USD | 14,840.00 USD |
| `7D` | `0.8370` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 15,240.00 USD | 1,480.00 USD | 0.00 USD |
| `1D` | `0.8380` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 16,380.00 USD | 1,900.00 USD | 0.00 USD |
| `7D` | `0.8390` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD |
| `1D` | `0.8400` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 458.00 USD | 1,050.00 USD | 2,340.00 USD |
| `7D` | `0.8410` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD |
| `1D` | `0.8420` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 1,340.00 USD | 4,840.00 USD | 0.00 USD |
| `7D` | `0.8430` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 11,320.00 USD | 3,840.00 USD | 4,060.00 USD |
| `1D` | `0.8440` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 2,210.00 USD | 5.65 USD | 0.00 USD |
| `7D` | `0.8450` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 1,980.00 USD | 404.64 USD | 474.61 USD |
| `1D` | `0.8460` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 15,140.00 USD | 6,600.00 USD | 25.04 USD |
| `7D` | `0.8470` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 7,900.00 USD | 1,730.00 USD | 2,180.00 USD |
| `1D` | `0.8480` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 6,670.00 USD | 230.58 USD | 0.00 USD |
| `7D` | `0.8490` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 21,300.00 USD | 9,450.00 USD | 0.00 USD |
| `1D` | `0.8500` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 8,440.00 USD | 371.56 USD | 744.62 USD |
| `7D` | `0.8510` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 5,480.00 USD | 991.53 USD | 4,660.00 USD |
| `1D` | `0.8520` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 1,230.00 USD | 1,940.00 USD | 12,140.00 USD |
| `7D` | `0.8530` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD |
| `1D` | `0.8540` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 2,300.00 USD | 4,910.00 USD | 4,110.00 USD |
| `7D` | `0.8550` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD |
| `1D` | `0.8560` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 16,210.00 USD | 306.64 USD | 880.90 USD |
| `7D` | `0.8570` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 3,540.00 USD | 944.22 USD | 8,450.00 USD |
| `1D` | `0.8580` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 2,870.00 USD | 209.22 USD | 8,640.00 USD |
| `7D` | `0.8590` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 3,730.00 USD | 0.00 USD | 1,560.00 USD |
| `1D` | `0.8600` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 7,990.00 USD | 10,610.00 USD | 18,580.00 USD |
| `7D` | `0.8610` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 9,960.00 USD | 3,660.00 USD | 35,340.00 USD |
| `1D` | `0.8620` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 12,920.00 USD | 12,720.00 USD | 0.00 USD |
| `7D` | `0.8630` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 758.91 USD | 2,910.00 USD | 1,280.00 USD |
| `1D` | `0.8640` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 48,740.00 USD | 2,370.00 USD | 3,790.00 USD |
| `7D` | `0.8650` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 47,860.00 USD | 18,930.00 USD | 184.85 USD |
| `1D` | `0.8660` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD |
| `7D` | `0.8670` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 13,660.00 USD | 3,720.00 USD | 12,140.00 USD |
| `1D` | `0.8680` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 43,000.00 USD | 9,030.00 USD | 11,890.00 USD |
| `7D` | `0.8690` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 160,750.00 USD | 13,110.00 USD | 46,230.00 USD |
| `1D` | `0.8700` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 49,290.00 USD | 3,880.00 USD | 33,390.00 USD |
| `7D` | `0.8710` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 7,370.00 USD | 23,340.00 USD | 13,110.00 USD |
| `1D` | `0.8720` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 30,840.00 USD | 34,140.00 USD | 24,590.00 USD |
| `7D` | `0.8730` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 0.00 USD | 8,170.00 USD | 295.31 USD |
| `1D` | `0.8740` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 59,860.00 USD | 12,180.00 USD | 33,580.00 USD |
| `7D` | `0.8750` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 0.00 USD | 6,380.00 USD | 8,950.00 USD |
| `1D` | `0.8760` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 16,700.00 USD | 5,410.00 USD | 1,470.00 USD |
| `7D` | `0.8770` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 1,390.00 USD | 0.00 USD | 30,820.00 USD |
| `1D` | `0.8780` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 0.00 USD | 214.09 USD | 54,890.00 USD |
| `7D` | `0.8790` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 873.30 USD | 5,580.00 USD | 53,860.00 USD |
| `1D` | `0.8800` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 10,360.00 USD | 16.72 USD | 7,750.00 USD |
| `7D` | `0.8810` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 228.30 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8820` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 0.00 USD | 10,010.00 USD | 0.00 USD |
| `7D` | `0.8830` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 2,320.00 USD | 10,140.00 USD | 11,710.00 USD |
| `1D` | `0.8840` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 1,980.00 USD | 17,420.00 USD | 8,890.00 USD |
| `7D` | `0.8850` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 0.00 USD | 5,800.00 USD | 3,970.00 USD |
| `1D` | `0.8860` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 66,480.00 USD | 27,710.00 USD | 2,350.00 USD |
| `7D` | `0.8870` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 271,870.00 USD | 22,320.00 USD | 81,590.00 USD |
| `1D` | `0.8880` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 73,700.00 USD | 14,120.00 USD | 36,640.00 USD |
| `7D` | `0.8890` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 54,380.00 USD | 73,890.00 USD | 13,880.00 USD |
| `1D` | `0.8900` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 2,730.00 USD | 51,750.00 USD | 910.96 USD |
| `7D` | `0.8910` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 75,300.00 USD | 22,240.00 USD | 34,270.00 USD |
| `1D` | `0.8920` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 45,630.00 USD | 32,720.00 USD | 56,100.00 USD |
| `7D` | `0.8930` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 62,870.00 USD | 23,560.00 USD | 9,170.00 USD |
| `1D` | `0.8940` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 13,790.00 USD | 18,130.00 USD | 1,980.00 USD |
| `7D` | `0.8950` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 7,120.00 USD | 37,670.00 USD | 57,420.00 USD |
| `1D` | `0.8960` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 2,010.00 USD | 26,370.00 USD | 5,550.00 USD |
| `7D` | `0.8970` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 0.00 USD | 4,500.00 USD | 56,330.00 USD |
| `1D` | `0.8980` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 0.00 USD | 26,620.00 USD | 16,170.00 USD |
| `7D` | `0.8990` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 0.00 USD | 34,220.00 USD | 0.00 USD |
| `1D` | `0.9000` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 0.00 USD | 10,050.00 USD | 0.00 USD |
| `7D` | `0.9010` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 0.00 USD | 48,840.00 USD | 0.00 USD |
| `1D` | `0.9020` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 538.90 USD | 9,990.00 USD | 1,590.00 USD |
| `7D` | `0.9030` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 0.00 USD | 12,490.00 USD | 23,430.00 USD |
| `1D` | `0.9040` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 7,870.00 USD | 21,080.00 USD | 17,930.00 USD |
| `1D` | `0.9060` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 19,570.00 USD | 35.10 USD | 7,720.00 USD |
| `7D` | `0.9070` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 1,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9080` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 7,220.00 USD | 6,560.00 USD | 0.00 USD |
| `1D` | `0.9100` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 404.79 USD |
| `1D` | `0.9120` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 27,150.00 USD | 2,020.00 USD | 2,460.00 USD |
| `7D` | `0.9130` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 20,720.00 USD |
| `1D` | `0.9140` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 7,740.00 USD | 3,740.00 USD | 23,680.00 USD |
| `7D` | `0.9150` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 0.00 USD | 515.41 USD | 15,680.00 USD |
| `1D` | `0.9160` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 0.00 USD | 5,930.00 USD | 10,930.00 USD |
| `7D` | `0.9170` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 33,180.00 USD |
| `1D` | `0.9180` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 8,160.00 USD |
| `1D` | `0.9200` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 5,710.00 USD | 2,090.00 USD | 3,710.00 USD |
| `7D` | `0.9210` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 3,970.00 USD |
| `1D` | `0.9220` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 48.22 USD |
| `7D` | `0.9230` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 298,040.00 USD | 0.00 USD | 29,500.00 USD |
| `1D` | `0.9240` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 77,940.00 USD | 8,630.00 USD | 0.00 USD |
| `7D` | `0.9250` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 0.00 USD | 45,090.00 USD | 0.00 USD |
| `1D` | `0.9260` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 898.50 USD | 39,060.00 USD | 31,770.00 USD |
| `7D` | `0.9270` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 0.00 USD | 11,800.00 USD | 0.00 USD |
| `1D` | `0.9280` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 78,050.00 USD | 4,120.00 USD | 66,550.00 USD |
| `7D` | `0.9290` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 0.00 USD | 12,750.00 USD | 1,600.00 USD |
| `1D` | `0.9300` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD | 9,460.00 USD | 366.80 USD |
| `1D` | `0.9320` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 7,440.00 USD | 68.90 USD | 11,160.00 USD |
| `7D` | `0.9330` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 37,450.00 USD | 0.00 USD | 31,370.00 USD |
| `1D` | `0.9340` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 93,080.00 USD | 15,090.00 USD | 38,820.00 USD |
| `7D` | `0.9350` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 11,160.00 USD | 20,370.00 USD |
| `1D` | `0.9360` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 90,760.00 USD | 45,310.00 USD | 29,660.00 USD |
| `7D` | `0.9370` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 16,340.00 USD | 19,540.00 USD | 48,530.00 USD |
| `1D` | `0.9380` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 54,410.00 USD | 17,230.00 USD | 14,830.00 USD |
| `7D` | `0.9390` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 39,250.00 USD | 11,610.00 USD | 35,060.00 USD |
| `1D` | `0.9400` | 981,920.00 USD | 0.00 USD | 981,920.00 USD | 88,450.00 USD | 36,910.00 USD | 0.00 USD |
| `7D` | `0.9410` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 165,130.00 USD | 21,610.00 USD | 41,800.00 USD |
| `1D` | `0.9420` | 856,550.00 USD | 0.00 USD | 856,550.00 USD | 101,680.00 USD | 20,480.00 USD | 36,170.00 USD |
| `7D` | `0.9430` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 45,490.00 USD | 22,230.00 USD | 8,720.00 USD |
| `1D` | `0.9440` | 698,220.00 USD | 0.00 USD | 698,220.00 USD | 140,870.00 USD | 34,100.00 USD | 31,500.00 USD |
| `7D` | `0.9450` | 951,520.00 USD | 0.00 USD | 951,520.00 USD | 261,930.00 USD | 54,160.00 USD | 71,090.00 USD |
| `1D` | `0.9460` | 491,750.00 USD | 0.00 USD | 491,750.00 USD | 89,630.00 USD | 54,970.00 USD | 61,820.00 USD |
| `7D` | `0.9470` | 564,330.00 USD | 0.00 USD | 564,330.00 USD | 204,050.00 USD | 6,380.00 USD | 76,590.00 USD |
| `1D` | `0.9480` | 285,320.00 USD | 0.00 USD | 285,320.00 USD | 103,240.00 USD | 10,350.00 USD | 74,210.00 USD |
| `7D` | `0.9490` | 277,310.00 USD | 0.00 USD | 277,310.00 USD | 195,810.00 USD | 10,340.00 USD | 71,150.00 USD |
| `1D` | `0.9500` | 97,520.00 USD | 0.00 USD | 97,520.00 USD | 80,090.00 USD | 17,420.00 USD | 0.00 USD |
| `1D` | `0.9510` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9510` | 291,390.00 USD | 291,390.00 USD | 0.00 USD | 258,650.00 USD | 28,180.00 USD | 4,570.00 USD |
| `7D` | `0.9510` | 582,790.00 USD | 582,790.00 USD | 0.00 USD | 258,650.00 USD | 28,180.00 USD | 4,570.00 USD |
| `1D` | `0.9520` | 18,130.00 USD | 18,130.00 USD | 0.00 USD | 0.00 USD | 18,130.00 USD | 0.00 USD |
| `7D` | `0.9530` | 591,020.00 USD | 591,020.00 USD | 0.00 USD | 0.00 USD | 8,240.00 USD | 0.00 USD |
| `1D` | `0.9540` | 76,090.00 USD | 76,090.00 USD | 0.00 USD | 48,110.00 USD | 9,840.00 USD | 0.00 USD |
| `7D` | `0.9550` | 610,760.00 USD | 610,760.00 USD | 0.00 USD | 0.00 USD | 19,730.00 USD | 0.00 USD |
| `1D` | `0.9560` | 101,850.00 USD | 101,850.00 USD | 0.00 USD | 10,720.00 USD | 15,050.00 USD | 0.00 USD |
| `7D` | `0.9570` | 623,920.00 USD | 623,920.00 USD | 0.00 USD | 1,910.00 USD | 10,300.00 USD | 957.94 USD |
| `1D` | `0.9580` | 106,730.00 USD | 106,730.00 USD | 0.00 USD | 4,400.00 USD | 0.00 USD | 471.48 USD |
| `7D` | `0.9590` | 637,230.00 USD | 637,230.00 USD | 0.00 USD | 1,980.00 USD | 10,470.00 USD | 866.69 USD |
| `1D` | `0.9600` | 116,610.00 USD | 116,610.00 USD | 0.00 USD | 3,440.00 USD | 4,720.00 USD | 1,720.00 USD |
| `7D` | `0.9610` | 661,600.00 USD | 661,600.00 USD | 0.00 USD | 24,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9620` | 212,120.00 USD | 212,120.00 USD | 0.00 USD | 71,510.00 USD | 7,410.00 USD | 16,600.00 USD |
| `7D` | `0.9630` | 742,380.00 USD | 742,380.00 USD | 0.00 USD | 56,160.00 USD | 24,130.00 USD | 481.70 USD |
| `1D` | `0.9640` | 290,040.00 USD | 290,040.00 USD | 0.00 USD | 19,400.00 USD | 30,520.00 USD | 28,000.00 USD |
| `7D` | `0.9650` | 808,300.00 USD | 808,300.00 USD | 0.00 USD | 53,580.00 USD | 0.00 USD | 12,330.00 USD |
| `1D` | `0.9660` | 334,890.00 USD | 334,890.00 USD | 0.00 USD | 2,700.00 USD | 4,970.00 USD | 37,190.00 USD |
| `7D` | `0.9670` | 853,920.00 USD | 853,920.00 USD | 0.00 USD | 40,070.00 USD | 5,550.00 USD | 0.00 USD |
| `1D` | `0.9680` | 386,690.00 USD | 386,690.00 USD | 0.00 USD | 39,090.00 USD | 12,230.00 USD | 482.60 USD |
| `7D` | `0.9690` | 905,530.00 USD | 905,530.00 USD | 0.00 USD | 0.00 USD | 21,100.00 USD | 30,500.00 USD |
| `1D` | `0.9700` | 441,250.00 USD | 441,250.00 USD | 0.00 USD | 16,500.00 USD | 4,190.00 USD | 33,870.00 USD |
| `7D` | `0.9710` | 955,140.00 USD | 955,140.00 USD | 0.00 USD | 0.00 USD | 18,250.00 USD | 31,370.00 USD |
| `1D` | `0.9720` | 530,940.00 USD | 530,940.00 USD | 0.00 USD | 24,360.00 USD | 395.16 USD | 64,940.00 USD |
| `7D` | `0.9730` | 994,450.00 USD | 994,450.00 USD | 0.00 USD | 2,910.00 USD | 9,290.00 USD | 27,110.00 USD |
| `1D` | `0.9740` | 589,840.00 USD | 589,840.00 USD | 0.00 USD | 25,800.00 USD | 5,170.00 USD | 27,930.00 USD |
| `7D` | `0.9750` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 2,090.00 USD | 17,230.00 USD | 51,650.00 USD |
| `1D` | `0.9760` | 688,240.00 USD | 688,240.00 USD | 0.00 USD | 53,500.00 USD | 24,670.00 USD | 20,220.00 USD |
| `7D` | `0.9770` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD |
| `1D` | `0.9780` | 748,700.00 USD | 748,700.00 USD | 0.00 USD | 40,740.00 USD | 3,080.00 USD | 16,650.00 USD |
| `7D` | `0.9790` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 84,920.00 USD |
| `1D` | `0.9800` | 813,670.00 USD | 813,670.00 USD | 0.00 USD | 34,990.00 USD | 9,680.00 USD | 20,300.00 USD |
| `7D` | `0.9810` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 540.00 USD | 178.67 USD | 119,460.00 USD |
| `1D` | `0.9820` | 854,770.00 USD | 854,770.00 USD | 0.00 USD | 22,110.00 USD | 11,710.00 USD | 7,280.00 USD |
| `7D` | `0.9830` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 102,710.00 USD | 15,810.00 USD | 52,260.00 USD |
| `1D` | `0.9840` | 907,530.00 USD | 907,530.00 USD | 0.00 USD | 665.59 USD | 13,380.00 USD | 38,710.00 USD |
| `7D` | `0.9850` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 211.77 USD | 22,300.00 USD |
| `1D` | `0.9860` | 986,530.00 USD | 986,530.00 USD | 0.00 USD | 50,550.00 USD | 3,630.00 USD | 24,820.00 USD |
| `7D` | `0.9870` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 67,950.00 USD |
| `1D` | `0.9880` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 17,200.00 USD | 151.21 USD | 16,550.00 USD |
| `7D` | `0.9890` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `0.9900` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 61,110.00 USD | 1,320.00 USD | 28,530.00 USD |
| `7D` | `0.9910` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 1,570.00 USD | 479.24 USD | 35,270.00 USD |
| `1D` | `0.9920` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 9,580.00 USD | 4,160.00 USD | 32,100.00 USD |
| `7D` | `0.9930` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 36,000.00 USD |
| `1D` | `0.9940` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 25,660.00 USD | 10,700.00 USD | 10,030.00 USD |
| `7D` | `0.9950` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 63,060.00 USD | 5,380.00 USD | 58,050.00 USD |
| `1D` | `0.9960` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 19,070.00 USD | 3,600.00 USD | 7,450.00 USD |
| `7D` | `0.9970` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 95,130.00 USD | 253.35 USD | 4,670.00 USD |
| `1D` | `0.9980` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 53,920.00 USD | 10,730.00 USD | 15,870.00 USD |
| `7D` | `0.9990` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 6,490.00 USD | 462.12 USD |
| `1D` | `1.00` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 60,660.00 USD | 18,230.00 USD | 6,760.00 USD |
| `7D` | `1.00` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.00` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 16,570.00 USD | 1,970.00 USD | 7,450.00 USD |
| `7D` | `1.00` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 107,670.00 USD | 21,850.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 10,790.00 USD | 9,550.00 USD | 9,410.00 USD |
| `7D` | `1.00` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 32,430.00 USD | 3,970.00 USD | 12,730.00 USD |
| `1D` | `1.01` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 101,040.00 USD | 10,160.00 USD | 25,320.00 USD |
| `7D` | `1.01` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 34,110.00 USD | 0.00 USD | 29,210.00 USD |
| `1D` | `1.01` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 22,410.00 USD | 9,170.00 USD | 30,960.00 USD |
| `7D` | `1.01` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD |
| `1D` | `1.01` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 12,560.00 USD | 17,230.00 USD | 971.85 USD |
| `7D` | `1.01` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 20,090.00 USD | 17,980.00 USD | 0.00 USD |
| `1D` | `1.01` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 16,880.00 USD | 22,370.00 USD | 265.91 USD |
| `7D` | `1.01` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD |
| `1D` | `1.01` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 6,560.00 USD | 5,790.00 USD | 21,570.00 USD |
| `7D` | `1.01` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 26,510.00 USD | 7,420.00 USD |
| `1D` | `1.02` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 15,150.00 USD | 25,460.00 USD | 11,300.00 USD |
| `7D` | `1.02` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD |
| `1D` | `1.02` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 26,110.00 USD | 4,240.00 USD | 22,530.00 USD |
| `7D` | `1.02` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 17,960.00 USD | 83,360.00 USD | 11,810.00 USD |
| `1D` | `1.02` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 47,410.00 USD | 9,980.00 USD | 18,380.00 USD |
| `7D` | `1.02` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 61,450.00 USD | 32,840.00 USD | 68,370.00 USD |
| `1D` | `1.02` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 40,340.00 USD | 20,320.00 USD | 29,140.00 USD |
| `7D` | `1.02` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 82,230.00 USD | 86,210.00 USD | 146,060.00 USD |
| `1D` | `1.02` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 44,050.00 USD | 9,760.00 USD | 34,590.00 USD |
| `7D` | `1.02` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 28,320.00 USD | 48,490.00 USD | 37,230.00 USD |
| `1D` | `1.03` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 36,400.00 USD | 18,290.00 USD | 17,280.00 USD |
| `7D` | `1.03` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 161,070.00 USD | 127,000.00 USD | 25,260.00 USD |
| `1D` | `1.03` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 15,280.00 USD | 8,920.00 USD | 15,510.00 USD |
| `7D` | `1.03` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD |
| `1D` | `1.03` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 64,370.00 USD | 12,650.00 USD | 18,360.00 USD |
| `7D` | `1.03` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD |
| `1D` | `1.03` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 30,760.00 USD | 7,080.00 USD | 32,130.00 USD |
| `7D` | `1.03` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD |
| `1D` | `1.03` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 12,070.00 USD | 8,650.00 USD | 12,980.00 USD |
| `7D` | `1.03` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 259,060.00 USD | 8,290.00 USD | 43,490.00 USD |
| `1D` | `1.04` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 4,320.00 USD | 10,280.00 USD | 2,970.00 USD |
| `7D` | `1.04` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 192,080.00 USD | 3,170.00 USD | 109,460.00 USD |
| `1D` | `1.04` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 42,730.00 USD | 767.34 USD | 2,900.00 USD |
| `7D` | `1.04` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 239,580.00 USD | 9,010.00 USD | 117,630.00 USD |
| `1D` | `1.04` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 6,280.00 USD | 6,670.00 USD | 8,460.00 USD |
| `7D` | `1.04` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 276,890.00 USD | 2,090.00 USD | 159,500.00 USD |
| `1D` | `1.04` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 10,930.00 USD | 5,820.00 USD | 3,380.00 USD |
| `7D` | `1.04` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD |
| `1D` | `1.04` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 2,950.00 USD | 1,330.00 USD | 10,670.00 USD |
| `7D` | `1.04` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD |
| `1D` | `1.05` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 5,280.00 USD | 4,540.00 USD | 1,200.00 USD |
| `7D` | `1.05` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 178,890.00 USD | 96,370.00 USD | 244,850.00 USD |
| `1D` | `1.05` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 4,380.00 USD | 73.95 USD | 9,870.00 USD |
| `7D` | `1.05` | 6,680,000.00 USD | 6,680,000.00 USD | 0.00 USD | 117,630.00 USD | 13,780.00 USD | 77,620.00 USD |
| `1D` | `1.05` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 29,490.00 USD | 4,100.00 USD | 8,230.00 USD |
| `7D` | `1.05` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 175,350.00 USD | 43,690.00 USD | 96,730.00 USD |
| `1D` | `1.05` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 4,960.00 USD | 1,200.00 USD | 16,730.00 USD |
| `7D` | `1.05` | 7,200,000.00 USD | 7,200,000.00 USD | 0.00 USD | 68,010.00 USD | 58,070.00 USD | 74,380.00 USD |
| `1D` | `1.05` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 10,950.00 USD | 345.49 USD | 2,970.00 USD |
| `7D` | `1.05` | 7,430,000.00 USD | 7,430,000.00 USD | 0.00 USD | 125,020.00 USD | 33,860.00 USD | 72,330.00 USD |
| `1D` | `1.06` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 6,010.00 USD | 4,840.00 USD | 3,790.00 USD |
| `7D` | `1.06` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 218,860.00 USD | 70,160.00 USD | 106,380.00 USD |
| `1D` | `1.06` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.06` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 239,650.00 USD | 74,380.00 USD | 145,170.00 USD |
| `7D` | `1.06` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 140,850.00 USD | 56,310.00 USD | 78,020.00 USD |
| `7D` | `1.06` | 8,840,000.00 USD | 8,840,000.00 USD | 0.00 USD | 141,700.00 USD | 73,690.00 USD | 71,340.00 USD |
| `7D` | `1.06` | 9,060,000.00 USD | 9,060,000.00 USD | 0.00 USD | 90,670.00 USD | 28,390.00 USD | 95,080.00 USD |
| `7D` | `1.07` | 9,270,000.00 USD | 9,270,000.00 USD | 0.00 USD | 86,760.00 USD | 43,390.00 USD | 82,980.00 USD |
| `7D` | `1.07` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 219,670.00 USD | 14,440.00 USD | 62,270.00 USD |
| `7D` | `1.07` | 9,800,000.00 USD | 9,800,000.00 USD | 0.00 USD | 141,570.00 USD | 36,670.00 USD | 52,600.00 USD |
| `7D` | `1.07` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 96,630.00 USD | 42,960.00 USD | 95,510.00 USD |
| `7D` | `1.07` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 87,490.00 USD | 27,560.00 USD | 60,670.00 USD |
| `7D` | `1.08` | 10,360,000.00 USD | 10,360,000.00 USD | 0.00 USD | 75,040.00 USD | 29,910.00 USD | 48,910.00 USD |
| `7D` | `1.08` | 10,600,000.00 USD | 10,600,000.00 USD | 0.00 USD | 166,380.00 USD | 21,060.00 USD | 52,480.00 USD |
| `7D` | `1.08` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 164,440.00 USD | 26,480.00 USD | 33,950.00 USD |
| `7D` | `1.08` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 61,330.00 USD | 41,110.00 USD | 101,150.00 USD |
| `7D` | `1.08` | 11,200,000.00 USD | 11,200,000.00 USD | 0.00 USD | 100,580.00 USD | 18,540.00 USD | 54,080.00 USD |
| `7D` | `1.09` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 115,430.00 USD | 58,300.00 USD | 69,640.00 USD |
| `7D` | `1.09` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 71,650.00 USD | 26,310.00 USD | 85,300.00 USD |
| `7D` | `1.09` | 11,760,000.00 USD | 11,760,000.00 USD | 0.00 USD | 69,790.00 USD | 25,660.00 USD | 32,870.00 USD |
| `7D` | `1.09` | 11,920,000.00 USD | 11,920,000.00 USD | 0.00 USD | 59,760.00 USD | 39,220.00 USD | 62,330.00 USD |
| `7D` | `1.09` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 51,610.00 USD | 22,240.00 USD | 92,520.00 USD |
| `7D` | `1.10` | 12,180,000.00 USD | 12,180,000.00 USD | 0.00 USD | 80,640.00 USD | 12,450.00 USD | 4,370.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `176.78M` | Total OI Tokens: `185,972,004.4 DOT`
  * 1h OI Change: `+0.84%` | 4h OI Change: `-7.81%` | 24h OI Change: `-14.88%`
  * Exchange Breakdown: Binance=`34.92M` | Bybit=`22.38M` | OKX=`10.11M` | Hyperliquid=`5.90M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.08K` | Last 24h: `2.25K` | Last 3d: `-11.45K` | Last 7d: `-19.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0161%` |
| **USDT Bybit** | `0.0011%` | **USDT KuCoin** | `-0.0195%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0051%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-0.0031%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `31.37%` | `68.63%` | `0.46` | 16,480,000.00 USD |
| `15M` | `Binance` | `37.29%` | `62.71%` | `0.59` | 5,810,000.00 USD |
| `15M` | `OKX` | `32.17%` | `67.83%` | `0.47` | 1,930,000.00 USD |
| `15M` | `Bybit` | `41.65%` | `58.35%` | `0.71` | 2,090,000.00 USD |
| `15M` | `KuCoin` | `38.54%` | `61.46%` | `0.63` | 86,570.00 USD |
| `15M` | `Gate` | `48.13%` | `51.87%` | `0.93` | 347,320.00 USD |
| `15M` | `Bitget` | `16.79%` | `83.21%` | `0.20` | 958,970.00 USD |
| `15M` | `BingX` | `7.12%` | `92.88%` | `0.08` | 2,690,000.00 USD |
| `15M` | `MEXC` | `36.33%` | `63.67%` | `0.57` | 576,300.00 USD |
| `15M` | `Bitunix` | `23.62%` | `76.38%` | `0.31` | 476,050.00 USD |
| `15M` | `Hyperliquid` | `25.73%` | `74.27%` | `0.35` | 1,010,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `37.48%` | `62.52%` | `0.60` | 100,200.00 USD |
| `15M` | `Crypto.com` | `50.02%` | `49.98%` | `1.00` | 270.31 USD |
| `15M` | `WhiteBIT` | `99.43%` | `0.57%` | `174.44` | 305,030.00 USD |
| `15M` | `HTX` | `18.54%` | `81.46%` | `0.23` | 17,400.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `52.22%` | `47.78%` | `1.09` | 45,130.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `20.34%` | `79.66%` | `0.26` | 22,360.00 USD |
| `15M` | `Whale Positions` | `37.29%` | `62.71%` | `0.59` | 5,810,000.00 USD |
| `15M` | `Global Accounts` | `31.37%` | `68.63%` | `0.46` | 16,480,000.00 USD |
| `1H` | `DOT` | `41.10%` | `58.90%` | `0.70` | 69,270,000.00 USD |
| `1H` | `Binance` | `41.99%` | `58.01%` | `0.72` | 25,390,000.00 USD |
| `1H` | `OKX` | `38.67%` | `61.33%` | `0.63` | 9,620,000.00 USD |
| `1H` | `Bybit` | `37.45%` | `62.55%` | `0.60` | 10,020,000.00 USD |
| `1H` | `KuCoin` | `29.73%` | `70.27%` | `0.42` | 548,150.00 USD |
| `1H` | `Gate` | `51.05%` | `48.95%` | `1.04` | 1,790,000.00 USD |
| `1H` | `Bitget` | `36.49%` | `63.51%` | `0.57` | 4,630,000.00 USD |
| `1H` | `BingX` | `38.66%` | `61.34%` | `0.63` | 3,390,000.00 USD |
| `1H` | `MEXC` | `42.82%` | `57.18%` | `0.75` | 2,980,000.00 USD |
| `1H` | `Bitunix` | `34.41%` | `65.59%` | `0.52` | 2,260,000.00 USD |
| `1H` | `Hyperliquid` | `40.84%` | `59.16%` | `0.69` | 6,220,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `41.88%` | `58.12%` | `0.72` | 368,120.00 USD |
| `1H` | `Crypto.com` | `37.82%` | `62.18%` | `0.61` | 2,270.00 USD |
| `1H` | `WhiteBIT` | `81.41%` | `18.59%` | `4.38` | 1,570,000.00 USD |
| `1H` | `HTX` | `29.62%` | `70.38%` | `0.42` | 29,480.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `43.46%` | `56.54%` | `0.77` | 152,330.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `53.19%` | `46.81%` | `1.14` | 289,270.00 USD |
| `1H` | `Whale Positions` | `41.99%` | `58.01%` | `0.72` | 25,390,000.00 USD |
| `1H` | `Global Accounts` | `41.10%` | `58.90%` | `0.70` | 69,270,000.00 USD |
| `4H` | `DOT` | `54.08%` | `45.92%` | `1.18` | 293,170,000.00 USD |
| `4H` | `Binance` | `52.83%` | `47.17%` | `1.12` | 116,820,000.00 USD |
| `4H` | `OKX` | `53.72%` | `46.28%` | `1.16` | 36,330,000.00 USD |
| `4H` | `Bybit` | `53.48%` | `46.52%` | `1.15` | 40,040,000.00 USD |
| `4H` | `KuCoin` | `48.24%` | `51.76%` | `0.93` | 2,050,000.00 USD |
| `4H` | `Gate` | `55.91%` | `44.09%` | `1.27` | 11,000,000.00 USD |
| `4H` | `Bitget` | `50.97%` | `49.03%` | `1.04` | 17,270,000.00 USD |
| `4H` | `BingX` | `55.75%` | `44.25%` | `1.26` | 16,790,000.00 USD |
| `4H` | `MEXC` | `51.62%` | `48.38%` | `1.07` | 10,040,000.00 USD |
| `4H` | `Bitunix` | `51.46%` | `48.54%` | `1.06` | 6,920,000.00 USD |
| `4H` | `Hyperliquid` | `55.83%` | `44.17%` | `1.26` | 26,630,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.4%` | `47.6%` | `1.10` | 1,770,000.00 USD |
| `4H` | `Crypto.com` | `49.38%` | `50.62%` | `0.98` | 19,860.00 USD |
| `4H` | `WhiteBIT` | `92.67%` | `7.33%` | `12.64` | 4,950,000.00 USD |
| `4H` | `HTX` | `48.75%` | `51.25%` | `0.95` | 184,590.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `78.04%` | `21.96%` | `3.55` | 397,260.00 USD |
| `4H` | `Aster` | `59.13%` | `40.87%` | `1.45` | 550,600.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.25%` | `47.75%` | `1.09` | 1,390,000.00 USD |
| `4H` | `Whale Positions` | `52.83%` | `47.17%` | `1.12` | 116,820,000.00 USD |
| `4H` | `Global Accounts` | `54.08%` | `45.92%` | `1.18` | 293,170,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.9301` | `0.9294` | `0.9301` | `0.9320` | `0.9246` | 722,739.41 USD | 436,845.68 USD | 285,893.73 USD | 150,951.95 USD | `+20.89%` | `15B / 5S` |
| `5:00 UTC` | `0.9322` | `0.9317` | `0.9322` | `0.9342` | `0.9301` | 515,769.04 USD | 235,727.30 USD | 280,041.74 USD | -44,314.44 USD | `-8.59%` | `11B / 7S` |
| `0:00 UTC` | `0.9301` | `0.9291` | `0.9301` | `0.9327` | `0.9264` | 525,506.21 USD | 261,479.52 USD | 264,026.69 USD | -2,547.17 USD | `-0.48%` | `9B / 12S` |
| `5:00 UTC` | `0.9325` | `0.9314` | `0.9325` | `0.9344` | `0.9288` | 497,143.85 USD | 263,231.22 USD | 233,912.62 USD | 29,318.60 USD | `+5.90%` | `7B / 6S` |
| `0:00 UTC` | `0.9354` | `0.9348` | `0.9354` | `0.9365` | `0.9333` | 404,247.05 USD | 223,080.64 USD | 181,166.41 USD | 41,914.22 USD | `+10.37%` | `5B / 3S` |
| `5:00 UTC` | `0.9425` | `0.9411` | `0.9425` | `0.9454` | `0.9362` | 1,398,502.73 USD | 702,262.50 USD | 696,240.23 USD | 6,022.27 USD | `+0.43%` | `30B / 12S` |
| `0:00 UTC` | `0.9563` | `0.9497` | `0.9563` | `0.9570` | `0.9410` | 1,155,581.71 USD | 451,950.39 USD | 703,631.31 USD | -251,680.92 USD | `-21.78%` | `29B / 39S` |
| `5:00 UTC` | `0.9533` | `0.9521` | `0.9533` | `0.9545` | `0.9487` | 564,921.36 USD | 209,867.72 USD | 355,053.64 USD | -145,185.92 USD | `-25.70%` | `9B / 14S` |
| `0:00 UTC` | `0.9564` | `0.9543` | `0.9564` | `0.9570` | `0.9510` | 548,666.48 USD | 227,756.91 USD | 320,909.57 USD | -93,152.67 USD | `-16.98%` | `3B / 13S` |
| `5:00 UTC` | `0.9556` | `0.9567` | `0.9556` | `0.9604` | `0.9534` | 622,350.69 USD | 333,856.61 USD | 288,494.08 USD | 45,362.53 USD | `+7.29%` | `8B / 11S` |

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
| `5m` | -56,270.00 USD | 17,390.00 USD | **`DISTRIBUTION`** |
| `15m` | 184,550.00 USD | 80,540.00 USD | **`ACCUMULATION`** |
| `30m` | 140,990.00 USD | -165,920.00 USD | **`DISTRIBUTION`** |
| `1h` | 147,860.00 USD | -742,640.00 USD | **`DISTRIBUTION`** |
| `2h` | 161,680.00 USD | -863,100.00 USD | **`DISTRIBUTION`** |
| `4h` | 268,160.00 USD | 36,220.00 USD | **`ACCUMULATION`** |
| `6h` | -72,920.00 USD | 981,880.00 USD | **`ACCUMULATION`** |
| `8h` | 39,700.00 USD | -4,900,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -862,870.00 USD | -5,360,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,010,000.00 USD | -6,580,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,890,000.00 USD | -23,290,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,440,000.00 USD | -77,780,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-56.27K` | 15m=`+184.55K` | 1h=`+147.86K` | 24h=`-1.01M`
* Futures Capital Netflows: 5m=`+17.39K` | 15m=`+80.54K` | 1h=`-742.64K` | 24h=`-6.58M`
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
  * `2026-10-30 11:19:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:20:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:20:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:20:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:20:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.8907` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.8482` (Risk Distance: `0.0425` pts)
  * +2.5R Take Profit: `0.9970`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9259` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9684` (Risk Distance: `0.0425` pts)
  * +2.5R Take Profit: `0.8196`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9581`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
