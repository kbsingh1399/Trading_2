# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 10:59:03 IST` (`2026-10-30 05:29:03 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `0.8968` | VWAP Z-Score: `+2.26` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0098` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `65.00` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.9502` | Lower -3.00σ Band: `0.8435`
  * Upper +2.51σ Band: `0.9415` | Lower -2.51σ Band: `0.8522`
  * Upper +2.01σ Band: `0.9326` | Lower -2.01σ Band: `0.8611`
  * Upper +2.00σ Band: `0.9324` | Lower -2.00σ Band: `0.8613`
  * Upper +1.28σ Band: `0.9196` | Lower -1.28σ Band: `0.8741`
  * Upper +1.00σ Band: `0.9146` | Lower -1.00σ Band: `0.8790`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9227` | EMA-20=`0.9167` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9274` (Slope: `+0.0000`) | EMA-100=`0.9449`
  * Institutional Anchors: EMA-144=`0.9538` | EMA-200=`0.9610` (Slope: `-0.5608`) | EMA-233=`0.9650`
- **Range Boundaries**: 24H High=`1.01` | 24H Low=`0.8570` | Weekly High=`1.03` | Weekly Low=`0.8570`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9253` (Distance: `+2.72%`)
  * Point of Control (POC) = `0.9119` (Distance: `+4.24%`)
  * Value Area Low (VAL) = `0.8925` (Distance: `+6.50%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.02` | Weekly POC=`0.9945` | Weekly VAL=`0.9713`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9330` | Low=`0.8570`
  * London Session (08:00-16:00 UTC): High=`0.9450` | Low=`0.9290`
  * New York Session (13:00-21:00 UTC): High=`0.9562` | Low=`0.9448`
  * Initial Balance (First Hour): IB High=`0.9450` | IB Low=`0.9290`
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
| `5m` | `0.9510` | `0.9570` | `0.9493` | `0.9497` | `530,826` | 506,272.13 USD | -87,832.98 USD | `-17.35%` | -3,797,231.91 USD | `-1.42` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.9496` | `0.9536` | `0.9487` | `0.9528` | `218,190` | 207,483.11 USD | -46,013.16 USD | `-22.18%` | -3,843,245.07 USD | `-0.65` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.9529` | `0.9531` | `0.9503` | `0.9520` | `84,076` | 80,005.80 USD | -12,912.99 USD | `-16.14%` | -3,856,158.06 USD | `+0.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9361` | `0.9453` | `0.9361` | `0.9427` | `1,486,047` | 1,398,502.73 USD | 6,022.27 USD | `+0.43%` | -3,545,221.36 USD | `-0.13` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.9428` | `0.9570` | `0.9410` | `0.9497` | `1,216,863` | 1,155,581.71 USD | -251,680.92 USD | `-21.78%` | -3,796,902.28 USD | `-0.58` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.9496` | `0.9536` | `0.9487` | `0.9520` | `302,266` | 287,488.90 USD | -58,926.15 USD | `-20.50%` | -3,855,828.42 USD | `-0.34` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9176` | `0.9341` | `0.9170` | `0.9318` | `3,070,214` | 2,839,814.60 USD | -92,909.79 USD | `-3.27%` | -3,396,468.88 USD | `+0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9318` | `0.9453` | `0.9263` | `0.9427` | `3,017,884` | 2,825,399.84 USD | 74,707.92 USD | `+2.64%` | -3,321,760.96 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9428` | `0.9570` | `0.9410` | `0.9520` | `1,519,129` | 1,443,070.61 USD | -310,607.06 USD | `-21.52%` | -3,632,368.02 USD | `-0.09` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,414,306.57 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,007,919.25 USD | `+1.11` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9570` | `0.9263` | `0.9520` | `4,537,013` | 4,268,470.45 USD | -235,899.14 USD | `-5.53%` | -4,243,818.39 USD | `+0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | -92,512.40 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -889,577.85 USD | `-1.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,414,306.57 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,007,919.25 USD | `+1.11` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9570` | `0.9263` | `0.9520` | `4,537,013` | 4,268,470.45 USD | -235,899.14 USD | `-5.53%` | -4,243,818.39 USD | `+0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`0.9505`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:53:16 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9734` | 545.61 USD | `-` | `NEWS_INTEL` | `-` | #DOT Liquidated Short: 0.55K USD at 0.9734 USD [API] | `2026-10-29 01:59:46` |
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
| `7D` | `Long Liquidation` | `0.7700` | 4,430,000.00 USD | 4,430,000.00 USD | 5,060.00 USD | 1,600.00 USD | 5,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7720` | 4,420,000.00 USD | 4,420,000.00 USD | 4,990.00 USD | 0.00 USD | 2,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7725` | 3,840.00 USD | 160,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7740` | 4,410,000.00 USD | 4,410,000.00 USD | 5,450.00 USD | 0.00 USD | 3,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7760` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 147.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7775` | 2,490.00 USD | 156,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7780` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 3,100.00 USD | 53.43 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7795` | 272.83 USD | 154,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7800` | 4,400,000.00 USD | 4,400,000.00 USD | 436.65 USD | 25.30 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7820` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 1,920.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7840` | 4,390,000.00 USD | 4,390,000.00 USD | 227.10 USD | 1,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7860` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 2,250.00 USD | 365.01 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7865` | 292.03 USD | 153,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7880` | 4,390,000.00 USD | 4,390,000.00 USD | 5,690.00 USD | 2,050.00 USD | 723.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7900` | 4,380,000.00 USD | 4,380,000.00 USD | 6,940.00 USD | 2,650.00 USD | 4,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 277.39 USD | 153,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7920` | 4,370,000.00 USD | 4,370,000.00 USD | 12,590.00 USD | 2,180.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7940` | 4,340,000.00 USD | 4,340,000.00 USD | 15,680.00 USD | 2,500.00 USD | 13,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7960` | 4,310,000.00 USD | 4,310,000.00 USD | 4,520.00 USD | 7,120.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7980` | 4,300,000.00 USD | 4,300,000.00 USD | 16,210.00 USD | 3,000.00 USD | 14,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8000` | 4,260,000.00 USD | 4,260,000.00 USD | 10,100.00 USD | 5,540.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8020` | 4,240,000.00 USD | 4,240,000.00 USD | 8,990.00 USD | 4,460.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8040` | 4,220,000.00 USD | 4,220,000.00 USD | 5,500.00 USD | 2,170.00 USD | 940.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8060` | 4,210,000.00 USD | 4,210,000.00 USD | 16,390.00 USD | 10,990.00 USD | 10,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8080` | 4,180,000.00 USD | 4,180,000.00 USD | 1,570.00 USD | 1,230.00 USD | 10,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8100` | 4,160,000.00 USD | 4,160,000.00 USD | 2,890.00 USD | 2,010.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8120` | 4,150,000.00 USD | 4,150,000.00 USD | 15,720.00 USD | 3,030.00 USD | 9,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 153,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8140` | 4,120,000.00 USD | 4,120,000.00 USD | 32,880.00 USD | 6,050.00 USD | 15,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8160` | 4,070,000.00 USD | 4,070,000.00 USD | 38,200.00 USD | 10,180.00 USD | 6,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8180` | 4,020,000.00 USD | 4,020,000.00 USD | 12,550.00 USD | 2,560.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8200` | 3,990,000.00 USD | 3,990,000.00 USD | 1,740.00 USD | 1,570.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 152,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8220` | 3,980,000.00 USD | 3,980,000.00 USD | 20,390.00 USD | 6,820.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 749.96 USD | 150,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8240` | 3,200,000.00 USD | 3,200,000.00 USD | 15,220.00 USD | 3,960.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8240` | 3,950,000.00 USD | 3,950,000.00 USD | 23,160.00 USD | 93.73 USD | 11,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8260` | 3,170,000.00 USD | 3,170,000.00 USD | 3,220.00 USD | 8,710.00 USD | 971.85 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8260` | 3,910,000.00 USD | 3,910,000.00 USD | 5,220.00 USD | 3,490.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8280` | 3,160,000.00 USD | 3,160,000.00 USD | 244.70 USD | 1,600.00 USD | 110.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8280` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 3,910.00 USD | 1,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8300` | 3,160,000.00 USD | 3,160,000.00 USD | 295.97 USD | 1,440.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8300` | 3,900,000.00 USD | 3,900,000.00 USD | 9,280.00 USD | 4,780.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8320` | 3,150,000.00 USD | 3,150,000.00 USD | 2,130.00 USD | 1,910.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8320` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 401.80 USD | 77.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8340` | 3,140,000.00 USD | 3,140,000.00 USD | 25,550.00 USD | 5,650.00 USD | 8,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8340` | 3,880,000.00 USD | 3,880,000.00 USD | 35,710.00 USD | 10,960.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8360` | 3,100,000.00 USD | 3,100,000.00 USD | 1,870.00 USD | 636.81 USD | 14,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8360` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 844.23 USD | 311.26 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 149,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8380` | 3,090,000.00 USD | 3,090,000.00 USD | 16,380.00 USD | 1,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8380` | 3,830,000.00 USD | 3,830,000.00 USD | 15,240.00 USD | 633.60 USD | 539.92 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8400` | 3,070,000.00 USD | 3,070,000.00 USD | 458.00 USD | 1,050.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8400` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 798.38 USD | 8,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,570.00 USD | 149,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 3,060,000.00 USD | 3,060,000.00 USD | 1,340.00 USD | 4,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8420` | 3,800,000.00 USD | 3,800,000.00 USD | 6,400.00 USD | 4,650.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8435` | 751.39 USD | 148,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8440` | 3,060,000.00 USD | 3,060,000.00 USD | 2,210.00 USD | 5.65 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8440` | 3,790,000.00 USD | 3,790,000.00 USD | 7,170.00 USD | 24.80 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8460` | 3,050,000.00 USD | 3,050,000.00 USD | 15,140.00 USD | 6,600.00 USD | 25.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8460` | 3,780,000.00 USD | 3,780,000.00 USD | 2,560.00 USD | 427.62 USD | 2,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8480` | 3,030,000.00 USD | 3,030,000.00 USD | 6,670.00 USD | 230.58 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8480` | 3,780,000.00 USD | 3,780,000.00 USD | 26,310.00 USD | 10,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 147,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 3,030,000.00 USD | 3,030,000.00 USD | 8,440.00 USD | 371.56 USD | 744.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8500` | 3,740,000.00 USD | 3,740,000.00 USD | 2,050.00 USD | 477.96 USD | 4,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8515` | 2,700.00 USD | 146,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8520` | 3,020,000.00 USD | 3,020,000.00 USD | 1,230.00 USD | 1,940.00 USD | 12,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8520` | 3,730,000.00 USD | 3,730,000.00 USD | 5,900.00 USD | 669.43 USD | 226.67 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8540` | 3,000,000.00 USD | 3,000,000.00 USD | 2,300.00 USD | 4,890.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8540` | 3,720,000.00 USD | 3,720,000.00 USD | 254.55 USD | 2,660.00 USD | 5,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8560` | 2,990,000.00 USD | 2,990,000.00 USD | 16,210.00 USD | 306.64 USD | 880.90 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8560` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 842.92 USD | 2,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 143,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8580` | 2,970,000.00 USD | 2,970,000.00 USD | 2,410.00 USD | 209.22 USD | 4,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8580` | 3,710,000.00 USD | 3,710,000.00 USD | 3,540.00 USD | 101.30 USD | 1,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8600` | 2,970,000.00 USD | 2,970,000.00 USD | 6,860.00 USD | 10,590.00 USD | 13,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8600` | 3,710,000.00 USD | 3,710,000.00 USD | 5,820.00 USD | 211.77 USD | 383.26 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8605` | 25,780.00 USD | 142,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8615` | 181.17 USD | 116,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8620` | 2,930,000.00 USD | 2,930,000.00 USD | 12,920.00 USD | 12,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8620` | 3,700,000.00 USD | 3,700,000.00 USD | 7,670.00 USD | 6,050.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 116,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 2,910,000.00 USD | 2,910,000.00 USD | 48,740.00 USD | 2,370.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8640` | 3,660,000.00 USD | 3,660,000.00 USD | 4,820.00 USD | 321.30 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 116,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8660` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8660` | 3,660,000.00 USD | 3,660,000.00 USD | 45,020.00 USD | 19,050.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,390.00 USD | 116,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8680` | 2,850,000.00 USD | 2,850,000.00 USD | 43,000.00 USD | 9,030.00 USD | 11,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8680` | 3,590,000.00 USD | 3,590,000.00 USD | 92,530.00 USD | 14,760.00 USD | 50,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 12,590.00 USD | 114,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8700` | 2,790,000.00 USD | 2,790,000.00 USD | 49,290.00 USD | 3,880.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8700` | 3,430,000.00 USD | 3,430,000.00 USD | 81,840.00 USD | 9,460.00 USD | 7,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8715` | 92,580.00 USD | 102,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8720` | 2,700,000.00 USD | 2,700,000.00 USD | 30,840.00 USD | 34,140.00 USD | 24,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8720` | 3,330,000.00 USD | 3,330,000.00 USD | 5,420.00 USD | 18,020.00 USD | 11,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 2,610,000.00 USD | 2,610,000.00 USD | 59,860.00 USD | 12,180.00 USD | 33,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8740` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 12,360.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 2,510,000.00 USD | 2,510,000.00 USD | 16,700.00 USD | 5,410.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8760` | 3,280,000.00 USD | 3,280,000.00 USD | 766.43 USD | 0.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 9,560.00 USD | 9,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8780` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 214.09 USD | 54,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8780` | 3,280,000.00 USD | 3,280,000.00 USD | 1,500.00 USD | 0.00 USD | 33,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8800` | 2,430,000.00 USD | 2,430,000.00 USD | 10,360.00 USD | 16.72 USD | 7,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8800` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 5,580.00 USD | 51,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8820` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 10,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8820` | 3,180,000.00 USD | 3,180,000.00 USD | 454.20 USD | 9,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 2,400,000.00 USD | 2,400,000.00 USD | 1,980.00 USD | 17,400.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8840` | 3,170,000.00 USD | 3,170,000.00 USD | 2,090.00 USD | 6,440.00 USD | 15,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8860` | 2,370,000.00 USD | 2,370,000.00 USD | 66,480.00 USD | 28,300.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8860` | 3,150,000.00 USD | 3,150,000.00 USD | 141,730.00 USD | 22,320.00 USD | 78,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8880` | 2,270,000.00 USD | 2,270,000.00 USD | 73,520.00 USD | 14,120.00 USD | 36,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8880` | 2,910,000.00 USD | 2,910,000.00 USD | 130,140.00 USD | 31,410.00 USD | 9,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8900` | 2,150,000.00 USD | 2,150,000.00 USD | 375.79 USD | 51,720.00 USD | 910.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8900` | 2,740,000.00 USD | 2,740,000.00 USD | 106,830.00 USD | 45,590.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8920` | 2,100,000.00 USD | 2,100,000.00 USD | 45,120.00 USD | 32,720.00 USD | 56,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8920` | 2,550,000.00 USD | 2,550,000.00 USD | 46,210.00 USD | 38,810.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8940` | 1,960,000.00 USD | 1,960,000.00 USD | 13,790.00 USD | 18,130.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8940` | 2,450,000.00 USD | 2,450,000.00 USD | 45,210.00 USD | 12,120.00 USD | 26,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8960` | 1,930,000.00 USD | 1,930,000.00 USD | 2,010.00 USD | 26,370.00 USD | 5,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8960` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 32,500.00 USD | 93,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8980` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 26,620.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8980` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 17,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9000` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 10,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9000` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 22,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9020` | 1,840,000.00 USD | 1,840,000.00 USD | 538.90 USD | 9,960.00 USD | 1,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9020` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 44,210.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9040` | 1,830,000.00 USD | 1,830,000.00 USD | 7,300.00 USD | 21,080.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9040` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 12,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9060` | 1,780,000.00 USD | 1,780,000.00 USD | 16,420.00 USD | 0.00 USD | 7,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9080` | 1,760,000.00 USD | 1,760,000.00 USD | 6,530.00 USD | 6,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9100` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 404.79 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9120` | 1,750,000.00 USD | 1,750,000.00 USD | 27,150.00 USD | 2,020.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9140` | 1,710,000.00 USD | 1,710,000.00 USD | 4,020.00 USD | 3,740.00 USD | 10,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9140` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 515.41 USD | 20,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9160` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 5,930.00 USD | 2,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9200` | 1,690,000.00 USD | 1,690,000.00 USD | 5,710.00 USD | 0.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9200` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9220` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 48.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9220` | 2,100,000.00 USD | 2,100,000.00 USD | 152,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9240` | 1,680,000.00 USD | 1,680,000.00 USD | 77,940.00 USD | 8,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9240` | 1,950,000.00 USD | 1,950,000.00 USD | 145,560.00 USD | 12,790.00 USD | 29,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9260` | 1,590,000.00 USD | 1,590,000.00 USD | 898.50 USD | 39,060.00 USD | 31,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9260` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 32,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9280` | 1,520,000.00 USD | 1,520,000.00 USD | 78,050.00 USD | 4,120.00 USD | 66,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9280` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 24,550.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9300` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 9,460.00 USD | 142.30 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9320` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 68.90 USD | 4,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9320` | 1,700,000.00 USD | 1,700,000.00 USD | 37,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9340` | 1,360,000.00 USD | 1,360,000.00 USD | 93,080.00 USD | 15,100.00 USD | 12,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9340` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 11,160.00 USD | 768.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9360` | 1,240,000.00 USD | 1,240,000.00 USD | 90,760.00 USD | 45,310.00 USD | 16,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9360` | 1,650,000.00 USD | 1,650,000.00 USD | 8,250.00 USD | 0.00 USD | 1,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9380` | 1,080,000.00 USD | 1,080,000.00 USD | 54,410.00 USD | 13,050.00 USD | 1,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9380` | 1,640,000.00 USD | 1,640,000.00 USD | 42,660.00 USD | 19,540.00 USD | 27,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9400` | 1,010,000.00 USD | 1,010,000.00 USD | 88,450.00 USD | 36,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9400` | 1,550,000.00 USD | 1,550,000.00 USD | 75,540.00 USD | 32,570.00 USD | 47,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9420` | 889,540.00 USD | 889,540.00 USD | 101,680.00 USD | 20,480.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9420` | 1,400,000.00 USD | 1,400,000.00 USD | 106,320.00 USD | 7,050.00 USD | 12,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9440` | 731,210.00 USD | 731,210.00 USD | 140,870.00 USD | 34,100.00 USD | 31,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9440` | 1,270,000.00 USD | 1,270,000.00 USD | 102,440.00 USD | 49,100.00 USD | 57,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9460` | 524,730.00 USD | 524,730.00 USD | 89,630.00 USD | 54,970.00 USD | 61,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9460` | 1,060,000.00 USD | 1,060,000.00 USD | 286,390.00 USD | 27,270.00 USD | 67,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9480` | 318,310.00 USD | 318,310.00 USD | 110,860.00 USD | 10,350.00 USD | 74,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9480` | 680,330.00 USD | 680,330.00 USD | 193,280.00 USD | 10,340.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9500` | 122,880.00 USD | 122,880.00 USD | 105,450.00 USD | 17,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9500` | 381,620.00 USD | 381,620.00 USD | 196,070.00 USD | 18,830.00 USD | 166,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 49,410.00 USD | 49,410.00 USD | 31,280.00 USD | 18,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9520` | 327,800.00 USD | 327,800.00 USD | 175,720.00 USD | 9,750.00 USD | 142,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 109,450.00 USD | 109,450.00 USD | 49,650.00 USD | 10,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9540` | 442,760.00 USD | 442,760.00 USD | 0.00 USD | 9,460.00 USD | 105,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 140,470.00 USD | 140,470.00 USD | 10,720.00 USD | 20,030.00 USD | 275.27 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9560` | 470,860.00 USD | 470,860.00 USD | 0.00 USD | 28,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 166,820.00 USD | 166,820.00 USD | 4,400.00 USD | 9,570.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9580` | 493,530.00 USD | 493,530.00 USD | 3,880.00 USD | 6,110.00 USD | 12,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 180,880.00 USD | 180,880.00 USD | 3,440.00 USD | 8,890.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9600` | 516,750.00 USD | 516,750.00 USD | 17,690.00 USD | 4,660.00 USD | 866.69 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 276,400.00 USD | 276,400.00 USD | 71,510.00 USD | 7,410.00 USD | 16,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9620` | 551,370.00 USD | 551,370.00 USD | 17,990.00 USD | 16,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 354,310.00 USD | 354,310.00 USD | 19,400.00 USD | 30,520.00 USD | 28,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9640` | 666,280.00 USD | 666,280.00 USD | 95,370.00 USD | 7,500.00 USD | 12,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 399,170.00 USD | 399,170.00 USD | 2,700.00 USD | 4,970.00 USD | 37,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9660` | 677,280.00 USD | 677,280.00 USD | 5,050.00 USD | 5,170.00 USD | 778.15 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9680` | 450,740.00 USD | 450,740.00 USD | 39,090.00 USD | 12,230.00 USD | 258.10 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9680` | 721,240.00 USD | 721,240.00 USD | 38,090.00 USD | 5,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9695` | 14,120.00 USD | 14,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9700` | 491,100.00 USD | 491,100.00 USD | 9,060.00 USD | 4,190.00 USD | 27,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9700` | 781,880.00 USD | 781,880.00 USD | 0.00 USD | 30,140.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 554,410.00 USD | 554,410.00 USD | 24,360.00 USD | 395.16 USD | 38,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9720` | 787,270.00 USD | 787,270.00 USD | 1,430.00 USD | 3,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 600,010.00 USD | 600,010.00 USD | 25,800.00 USD | 5,170.00 USD | 14,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9740` | 824,630.00 USD | 824,630.00 USD | 1,480.00 USD | 25,640.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9745` | 214.00 USD | 14,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9755` | 345.62 USD | 14,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9760` | 680,600.00 USD | 680,600.00 USD | 53,500.00 USD | 20,490.00 USD | 6,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9760` | 902,770.00 USD | 902,770.00 USD | 51,990.00 USD | 16,870.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 741,070.00 USD | 741,070.00 USD | 40,740.00 USD | 3,080.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9780` | 927,050.00 USD | 927,050.00 USD | 0.00 USD | 0.00 USD | 24,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 806,040.00 USD | 806,040.00 USD | 34,990.00 USD | 9,680.00 USD | 20,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9800` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 152,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 847,130.00 USD | 847,130.00 USD | 22,110.00 USD | 11,710.00 USD | 7,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9820` | 1,250,000.00 USD | 1,250,000.00 USD | 53,310.00 USD | 15,990.00 USD | 104,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 899,900.00 USD | 899,900.00 USD | 665.59 USD | 13,380.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9840` | 1,330,000.00 USD | 1,330,000.00 USD | 49,930.00 USD | 211.77 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 978,890.00 USD | 978,890.00 USD | 50,550.00 USD | 3,630.00 USD | 24,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9860` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9880` | 1,010,000.00 USD | 1,010,000.00 USD | 17,200.00 USD | 151.21 USD | 16,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9880` | 1,430,000.00 USD | 1,430,000.00 USD | 40,020.00 USD | 0.00 USD | 67,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 1,090,000.00 USD | 1,090,000.00 USD | 57,390.00 USD | 1,320.00 USD | 15,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9900` | 1,460,000.00 USD | 1,460,000.00 USD | 20,530.00 USD | 0.00 USD | 906.61 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 1,120,000.00 USD | 1,120,000.00 USD | 9,580.00 USD | 4,160.00 USD | 23,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9920` | 1,480,000.00 USD | 1,480,000.00 USD | 1,570.00 USD | 479.24 USD | 21,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 1,160,000.00 USD | 1,160,000.00 USD | 25,660.00 USD | 10,700.00 USD | 1,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9940` | 1,520,000.00 USD | 1,520,000.00 USD | 29,270.00 USD | 0.00 USD | 16,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 1,190,000.00 USD | 1,190,000.00 USD | 19,070.00 USD | 1,480.00 USD | 7,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9960` | 1,650,000.00 USD | 1,650,000.00 USD | 75,810.00 USD | 5,380.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 1,270,000.00 USD | 1,270,000.00 USD | 53,920.00 USD | 10,730.00 USD | 15,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9980` | 1,710,000.00 USD | 1,710,000.00 USD | 53,110.00 USD | 6,740.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,360,000.00 USD | 1,360,000.00 USD | 60,090.00 USD | 18,230.00 USD | 6,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 1,770,000.00 USD | 1,770,000.00 USD | 52,850.00 USD | 0.00 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,380,000.00 USD | 1,380,000.00 USD | 13,430.00 USD | 1,930.00 USD | 7,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 1,860,000.00 USD | 1,860,000.00 USD | 54,650.00 USD | 21,850.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,410,000.00 USD | 1,410,000.00 USD | 10,110.00 USD | 9,550.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 1,940,000.00 USD | 1,940,000.00 USD | 70,950.00 USD | 3,970.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 1,550,000.00 USD | 1,550,000.00 USD | 101,040.00 USD | 10,160.00 USD | 31,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 1,990,000.00 USD | 1,990,000.00 USD | 46,710.00 USD | 0.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 221.13 USD | 14,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.01` | 1,610,000.00 USD | 1,610,000.00 USD | 22,410.00 USD | 9,170.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 44,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 1,640,000.00 USD | 1,640,000.00 USD | 12,560.00 USD | 17,230.00 USD | 971.85 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,060,000.00 USD | 2,060,000.00 USD | 10,260.00 USD | 14,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 1,680,000.00 USD | 1,680,000.00 USD | 16,880.00 USD | 22,350.00 USD | 265.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,130,000.00 USD | 2,130,000.00 USD | 33,230.00 USD | 30,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 1,720,000.00 USD | 1,720,000.00 USD | 6,560.00 USD | 5,790.00 USD | 21,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,160,000.00 USD | 2,160,000.00 USD | 2,870.00 USD | 28,450.00 USD | 735.11 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,770,000.00 USD | 1,770,000.00 USD | 14,730.00 USD | 25,460.00 USD | 11,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,200,000.00 USD | 2,200,000.00 USD | 526.60 USD | 28,470.00 USD | 11,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,820,000.00 USD | 1,820,000.00 USD | 23,750.00 USD | 4,210.00 USD | 22,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 25,010.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,890,000.00 USD | 1,890,000.00 USD | 46,900.00 USD | 9,980.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,410,000.00 USD | 2,410,000.00 USD | 33,820.00 USD | 84,220.00 USD | 44,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,980,000.00 USD | 1,980,000.00 USD | 40,340.00 USD | 20,320.00 USD | 29,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,630,000.00 USD | 2,630,000.00 USD | 56,930.00 USD | 52,610.00 USD | 112,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,070,000.00 USD | 2,070,000.00 USD | 44,050.00 USD | 11,230.00 USD | 34,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,850,000.00 USD | 2,850,000.00 USD | 78,220.00 USD | 56,700.00 USD | 86,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,150,000.00 USD | 2,150,000.00 USD | 40,090.00 USD | 18,290.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,030,000.00 USD | 3,030,000.00 USD | 22,650.00 USD | 124,880.00 USD | 33,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,200,000.00 USD | 2,200,000.00 USD | 19,210.00 USD | 8,920.00 USD | 15,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,360,000.00 USD | 3,360,000.00 USD | 250,310.00 USD | 50,530.00 USD | 24,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,290,000.00 USD | 2,290,000.00 USD | 64,370.00 USD | 12,650.00 USD | 18,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,540,000.00 USD | 3,540,000.00 USD | 134,200.00 USD | 33,660.00 USD | 19,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,360,000.00 USD | 2,360,000.00 USD | 30,760.00 USD | 7,090.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,650,000.00 USD | 3,650,000.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,400,000.00 USD | 2,400,000.00 USD | 12,440.00 USD | 8,650.00 USD | 12,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,880,000.00 USD | 3,880,000.00 USD | 217,210.00 USD | 8,290.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,410,000.00 USD | 2,410,000.00 USD | 4,520.00 USD | 10,280.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 4,190,000.00 USD | 4,190,000.00 USD | 262,550.00 USD | 3,170.00 USD | 42,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,460,000.00 USD | 2,460,000.00 USD | 42,730.00 USD | 767.34 USD | 2,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 4,570,000.00 USD | 4,570,000.00 USD | 178,400.00 USD | 1,290.00 USD | 199,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 228.37 USD | 15,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,480,000.00 USD | 2,480,000.00 USD | 6,280.00 USD | 6,670.00 USD | 8,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 4,950,000.00 USD | 4,950,000.00 USD | 279,840.00 USD | 9,430.00 USD | 93,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,500,000.00 USD | 2,500,000.00 USD | 10,930.00 USD | 5,820.00 USD | 3,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,280,000.00 USD | 5,280,000.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,520,000.00 USD | 2,520,000.00 USD | 2,950.00 USD | 1,310.00 USD | 10,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,540,000.00 USD | 5,540,000.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,530,000.00 USD | 2,530,000.00 USD | 5,280.00 USD | 4,540.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 5,950,000.00 USD | 5,950,000.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 367.04 USD | 15,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,540,000.00 USD | 2,540,000.00 USD | 3,910.00 USD | 73.95 USD | 5,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 6,340,000.00 USD | 6,340,000.00 USD | 199,320.00 USD | 28,070.00 USD | 161,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,580,000.00 USD | 2,580,000.00 USD | 28,700.00 USD | 4,090.00 USD | 6,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 6,500,000.00 USD | 6,500,000.00 USD | 91,750.00 USD | 29,070.00 USD | 40,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,600,000.00 USD | 2,600,000.00 USD | 4,900.00 USD | 1,200.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 6,830,000.00 USD | 6,830,000.00 USD | 140,530.00 USD | 49,780.00 USD | 134,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,610,000.00 USD | 2,610,000.00 USD | 11,090.00 USD | 345.49 USD | 2,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,000,000.00 USD | 7,000,000.00 USD | 88,940.00 USD | 44,290.00 USD | 36,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 2,630,000.00 USD | 2,630,000.00 USD | 5,790.00 USD | 4,530.00 USD | 3,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 7,360,000.00 USD | 7,360,000.00 USD | 187,610.00 USD | 48,000.00 USD | 121,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 2,630,000.00 USD | 2,630,000.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 7,720,000.00 USD | 7,720,000.00 USD | 205,690.00 USD | 63,350.00 USD | 94,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,140,000.00 USD | 8,140,000.00 USD | 217,790.00 USD | 73,000.00 USD | 125,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,420,000.00 USD | 8,420,000.00 USD | 131,720.00 USD | 83,000.00 USD | 66,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,660,000.00 USD | 8,660,000.00 USD | 102,750.00 USD | 49,310.00 USD | 92,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 8,840,000.00 USD | 8,840,000.00 USD | 77,920.00 USD | 32,860.00 USD | 73,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 9,190,000.00 USD | 9,190,000.00 USD | 221,410.00 USD | 30,180.00 USD | 93,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 9,390,000.00 USD | 9,390,000.00 USD | 121,300.00 USD | 33,170.00 USD | 42,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 9,610,000.00 USD | 9,610,000.00 USD | 103,500.00 USD | 37,730.00 USD | 83,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 9,810,000.00 USD | 9,810,000.00 USD | 92,440.00 USD | 21,500.00 USD | 83,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 9,960,000.00 USD | 9,960,000.00 USD | 103,110.00 USD | 18,720.00 USD | 27,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 10,230,000.00 USD | 10,230,000.00 USD | 158,650.00 USD | 40,740.00 USD | 69,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 10,460,000.00 USD | 10,460,000.00 USD | 176,790.00 USD | 26,190.00 USD | 33,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.08` | 2,230.00 USD | 17,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.08` | 10,590,000.00 USD | 10,590,000.00 USD | 62,710.00 USD | 20,510.00 USD | 39,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 10,770,000.00 USD | 10,770,000.00 USD | 46,000.00 USD | 31,940.00 USD | 103,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 11,000,000.00 USD | 11,000,000.00 USD | 161,270.00 USD | 28,200.00 USD | 42,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 11,230,000.00 USD | 11,230,000.00 USD | 59,850.00 USD | 57,700.00 USD | 117,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 11,390,000.00 USD | 11,390,000.00 USD | 109,670.00 USD | 18,350.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 11,520,000.00 USD | 11,520,000.00 USD | 36,490.00 USD | 24,570.00 USD | 62,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 11,680,000.00 USD | 11,680,000.00 USD | 67,090.00 USD | 37,290.00 USD | 55,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 11,840,000.00 USD | 11,840,000.00 USD | 65,410.00 USD | 32,080.00 USD | 65,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 12,080,000.00 USD | 12,080,000.00 USD | 119,850.00 USD | 21,050.00 USD | 97,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 12,360,000.00 USD | 12,360,000.00 USD | 182,190.00 USD | 62,380.00 USD | 40,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 12,440,000.00 USD | 12,440,000.00 USD | 59,740.00 USD | 10,900.00 USD | 2,270.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.7700` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 5,060.00 USD | 1,600.00 USD | 5,080.00 USD |
| `7D` | `0.7720` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 4,990.00 USD | 0.00 USD | 2,230.00 USD |
| `7D` | `0.7740` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 5,450.00 USD | 0.00 USD | 3,310.00 USD |
| `7D` | `0.7760` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 147.66 USD |
| `7D` | `0.7780` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 0.00 USD | 3,100.00 USD | 53.43 USD |
| `7D` | `0.7800` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 436.65 USD | 25.30 USD | 0.00 USD |
| `7D` | `0.7820` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 0.00 USD | 1,920.00 USD | 1,410.00 USD |
| `7D` | `0.7840` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 227.10 USD | 1,190.00 USD | 0.00 USD |
| `7D` | `0.7860` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 0.00 USD | 2,250.00 USD | 365.01 USD |
| `7D` | `0.7880` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 5,690.00 USD | 2,050.00 USD | 723.49 USD |
| `7D` | `0.7900` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 6,940.00 USD | 2,650.00 USD | 4,030.00 USD |
| `7D` | `0.7920` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 12,590.00 USD | 2,180.00 USD | 10,760.00 USD |
| `7D` | `0.7940` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 15,680.00 USD | 2,500.00 USD | 13,480.00 USD |
| `7D` | `0.7960` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 4,520.00 USD | 7,120.00 USD | 3,290.00 USD |
| `7D` | `0.7980` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 16,210.00 USD | 3,000.00 USD | 14,230.00 USD |
| `7D` | `0.8000` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 10,100.00 USD | 5,540.00 USD | 2,430.00 USD |
| `7D` | `0.8020` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 8,990.00 USD | 4,460.00 USD | 9,540.00 USD |
| `7D` | `0.8040` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 5,500.00 USD | 2,170.00 USD | 940.33 USD |
| `7D` | `0.8060` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 16,390.00 USD | 10,990.00 USD | 10,100.00 USD |
| `7D` | `0.8080` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 1,570.00 USD | 1,230.00 USD | 10,210.00 USD |
| `7D` | `0.8100` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 2,890.00 USD | 2,010.00 USD | 4,690.00 USD |
| `7D` | `0.8120` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 15,720.00 USD | 3,030.00 USD | 9,400.00 USD |
| `7D` | `0.8140` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 32,880.00 USD | 6,050.00 USD | 15,910.00 USD |
| `7D` | `0.8160` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 38,200.00 USD | 10,180.00 USD | 6,010.00 USD |
| `7D` | `0.8180` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 12,550.00 USD | 2,560.00 USD | 11,440.00 USD |
| `7D` | `0.8200` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 1,740.00 USD | 1,570.00 USD | 7,460.00 USD |
| `7D` | `0.8220` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 20,390.00 USD | 6,820.00 USD | 4,490.00 USD |
| `7D` | `0.8240` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 23,160.00 USD | 93.73 USD | 11,990.00 USD |
| `7D` | `0.8260` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 5,220.00 USD | 3,490.00 USD | 1,560.00 USD |
| `7D` | `0.8280` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 0.00 USD | 3,910.00 USD | 1,040.00 USD |
| `1D` | `0.8300` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 615.92 USD | 3,010.00 USD | 3,790.00 USD |
| `7D` | `0.8300` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 9,280.00 USD | 4,780.00 USD | 2,450.00 USD |
| `1D` | `0.8320` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 2,130.00 USD | 1,910.00 USD | 3,450.00 USD |
| `7D` | `0.8320` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 0.00 USD | 401.80 USD | 77.95 USD |
| `1D` | `0.8340` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 25,550.00 USD | 5,650.00 USD | 8,980.00 USD |
| `7D` | `0.8340` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 35,710.00 USD | 10,960.00 USD | 1,980.00 USD |
| `1D` | `0.8360` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 1,870.00 USD | 636.81 USD | 14,840.00 USD |
| `7D` | `0.8360` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 0.00 USD | 844.23 USD | 311.26 USD |
| `1D` | `0.8380` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 16,380.00 USD | 1,900.00 USD | 0.00 USD |
| `7D` | `0.8380` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 15,240.00 USD | 633.60 USD | 539.92 USD |
| `1D` | `0.8400` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 458.00 USD | 1,050.00 USD | 2,340.00 USD |
| `7D` | `0.8400` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 0.00 USD | 798.38 USD | 8,060.00 USD |
| `1D` | `0.8420` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 1,340.00 USD | 4,840.00 USD | 0.00 USD |
| `7D` | `0.8420` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 6,400.00 USD | 4,650.00 USD | 4,060.00 USD |
| `1D` | `0.8440` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 2,210.00 USD | 5.65 USD | 0.00 USD |
| `7D` | `0.8440` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 7,170.00 USD | 24.80 USD | 0.00 USD |
| `1D` | `0.8460` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 15,140.00 USD | 6,600.00 USD | 25.04 USD |
| `7D` | `0.8460` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 2,560.00 USD | 427.62 USD | 2,660.00 USD |
| `1D` | `0.8480` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 6,670.00 USD | 230.58 USD | 0.00 USD |
| `7D` | `0.8480` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 26,310.00 USD | 10,990.00 USD | 0.00 USD |
| `1D` | `0.8500` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 8,440.00 USD | 371.56 USD | 744.62 USD |
| `7D` | `0.8500` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 2,050.00 USD | 477.96 USD | 4,430.00 USD |
| `1D` | `0.8520` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 1,230.00 USD | 1,940.00 USD | 12,140.00 USD |
| `7D` | `0.8520` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 5,900.00 USD | 669.43 USD | 226.67 USD |
| `1D` | `0.8540` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 2,300.00 USD | 4,910.00 USD | 4,110.00 USD |
| `7D` | `0.8540` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 254.55 USD | 2,660.00 USD | 5,540.00 USD |
| `1D` | `0.8560` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 16,210.00 USD | 306.64 USD | 880.90 USD |
| `7D` | `0.8560` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 0.00 USD | 842.92 USD | 2,180.00 USD |
| `1D` | `0.8580` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 2,410.00 USD | 209.22 USD | 5,110.00 USD |
| `7D` | `0.8580` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 3,540.00 USD | 101.30 USD | 1,270.00 USD |
| `1D` | `0.8600` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 6,860.00 USD | 10,590.00 USD | 13,690.00 USD |
| `7D` | `0.8600` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 5,820.00 USD | 211.77 USD | 383.26 USD |
| `1D` | `0.8620` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 12,920.00 USD | 12,720.00 USD | 0.00 USD |
| `7D` | `0.8620` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 7,670.00 USD | 6,050.00 USD | 26,880.00 USD |
| `1D` | `0.8640` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 48,740.00 USD | 2,370.00 USD | 3,790.00 USD |
| `7D` | `0.8640` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 4,820.00 USD | 321.30 USD | 0.00 USD |
| `1D` | `0.8660` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD |
| `7D` | `0.8660` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 45,020.00 USD | 19,050.00 USD | 2,170.00 USD |
| `1D` | `0.8680` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 43,000.00 USD | 9,030.00 USD | 11,890.00 USD |
| `7D` | `0.8680` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 92,530.00 USD | 14,760.00 USD | 50,800.00 USD |
| `1D` | `0.8700` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 49,290.00 USD | 3,880.00 USD | 33,390.00 USD |
| `7D` | `0.8700` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 81,840.00 USD | 9,460.00 USD | 7,550.00 USD |
| `1D` | `0.8720` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 30,840.00 USD | 34,140.00 USD | 24,590.00 USD |
| `7D` | `0.8720` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 5,420.00 USD | 18,020.00 USD | 11,450.00 USD |
| `1D` | `0.8740` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 59,860.00 USD | 12,180.00 USD | 33,580.00 USD |
| `7D` | `0.8740` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 0.00 USD | 12,360.00 USD | 3,200.00 USD |
| `1D` | `0.8760` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 16,700.00 USD | 5,410.00 USD | 1,470.00 USD |
| `7D` | `0.8760` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 766.43 USD | 0.00 USD | 5,750.00 USD |
| `1D` | `0.8780` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 0.00 USD | 214.09 USD | 54,890.00 USD |
| `7D` | `0.8780` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 1,500.00 USD | 0.00 USD | 33,650.00 USD |
| `1D` | `0.8800` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 10,360.00 USD | 16.72 USD | 7,750.00 USD |
| `7D` | `0.8800` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 0.00 USD | 5,580.00 USD | 51,030.00 USD |
| `1D` | `0.8820` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 0.00 USD | 10,010.00 USD | 0.00 USD |
| `7D` | `0.8820` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 454.20 USD | 9,500.00 USD | 0.00 USD |
| `1D` | `0.8840` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 1,980.00 USD | 17,420.00 USD | 8,890.00 USD |
| `7D` | `0.8840` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 2,090.00 USD | 6,440.00 USD | 15,690.00 USD |
| `1D` | `0.8860` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 66,480.00 USD | 28,300.00 USD | 2,350.00 USD |
| `7D` | `0.8860` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 141,730.00 USD | 22,320.00 USD | 78,280.00 USD |
| `1D` | `0.8880` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 73,950.00 USD | 14,120.00 USD | 36,640.00 USD |
| `7D` | `0.8880` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 130,140.00 USD | 31,410.00 USD | 9,920.00 USD |
| `1D` | `0.8900` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 375.79 USD | 51,720.00 USD | 910.96 USD |
| `7D` | `0.8900` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 106,830.00 USD | 45,590.00 USD | 30,420.00 USD |
| `1D` | `0.8920` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 45,120.00 USD | 32,720.00 USD | 56,100.00 USD |
| `7D` | `0.8920` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 46,210.00 USD | 38,810.00 USD | 14,520.00 USD |
| `1D` | `0.8940` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 13,790.00 USD | 18,130.00 USD | 1,980.00 USD |
| `7D` | `0.8940` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 45,210.00 USD | 12,120.00 USD | 26,470.00 USD |
| `1D` | `0.8960` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 2,010.00 USD | 26,370.00 USD | 5,550.00 USD |
| `7D` | `0.8960` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 0.00 USD | 32,500.00 USD | 93,060.00 USD |
| `1D` | `0.8980` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 0.00 USD | 26,620.00 USD | 16,170.00 USD |
| `7D` | `0.8980` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 0.00 USD | 17,870.00 USD | 0.00 USD |
| `1D` | `0.9000` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 0.00 USD | 10,050.00 USD | 0.00 USD |
| `7D` | `0.9000` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 0.00 USD | 22,600.00 USD | 0.00 USD |
| `1D` | `0.9020` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 538.90 USD | 9,990.00 USD | 1,590.00 USD |
| `7D` | `0.9020` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 0.00 USD | 44,210.00 USD | 23,430.00 USD |
| `1D` | `0.9040` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 7,870.00 USD | 21,080.00 USD | 17,930.00 USD |
| `7D` | `0.9040` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 0.00 USD | 12,290.00 USD | 0.00 USD |
| `1D` | `0.9060` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 16,420.00 USD | 0.00 USD | 7,720.00 USD |
| `1D` | `0.9080` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 6,530.00 USD | 6,560.00 USD | 0.00 USD |
| `1D` | `0.9100` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 404.79 USD |
| `1D` | `0.9120` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 27,150.00 USD | 2,020.00 USD | 2,460.00 USD |
| `1D` | `0.9140` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 4,020.00 USD | 3,740.00 USD | 13,710.00 USD |
| `7D` | `0.9140` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 0.00 USD | 515.41 USD | 20,720.00 USD |
| `1D` | `0.9160` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 0.00 USD | 5,930.00 USD | 2,220.00 USD |
| `1D` | `0.9200` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 5,710.00 USD | 0.00 USD | 3,710.00 USD |
| `7D` | `0.9200` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 3,970.00 USD |
| `1D` | `0.9220` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 48.22 USD |
| `7D` | `0.9220` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 152,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9240` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 77,940.00 USD | 8,630.00 USD | 0.00 USD |
| `7D` | `0.9240` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 145,560.00 USD | 12,790.00 USD | 29,500.00 USD |
| `1D` | `0.9260` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 898.50 USD | 39,060.00 USD | 31,770.00 USD |
| `7D` | `0.9260` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 0.00 USD | 32,300.00 USD | 0.00 USD |
| `1D` | `0.9280` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 78,050.00 USD | 4,120.00 USD | 66,550.00 USD |
| `7D` | `0.9280` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 0.00 USD | 24,550.00 USD | 1,600.00 USD |
| `1D` | `0.9300` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 0.00 USD | 9,460.00 USD | 366.80 USD |
| `1D` | `0.9320` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 0.00 USD | 68.90 USD | 4,400.00 USD |
| `7D` | `0.9320` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 37,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9340` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 93,080.00 USD | 15,100.00 USD | 18,810.00 USD |
| `7D` | `0.9340` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 0.00 USD | 11,160.00 USD | 768.64 USD |
| `1D` | `0.9360` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 90,760.00 USD | 45,310.00 USD | 16,350.00 USD |
| `7D` | `0.9360` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 8,250.00 USD | 0.00 USD | 1,760.00 USD |
| `1D` | `0.9380` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 54,410.00 USD | 13,050.00 USD | 1,210.00 USD |
| `7D` | `0.9380` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 42,660.00 USD | 19,540.00 USD | 27,700.00 USD |
| `1D` | `0.9400` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 88,450.00 USD | 36,910.00 USD | 0.00 USD |
| `7D` | `0.9400` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 75,540.00 USD | 32,570.00 USD | 47,300.00 USD |
| `1D` | `0.9420` | 938,950.00 USD | 0.00 USD | 938,950.00 USD | 101,680.00 USD | 20,480.00 USD | 36,170.00 USD |
| `7D` | `0.9420` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 106,320.00 USD | 7,050.00 USD | 8,580.00 USD |
| `1D` | `0.9440` | 780,620.00 USD | 0.00 USD | 780,620.00 USD | 140,870.00 USD | 34,100.00 USD | 31,500.00 USD |
| `7D` | `0.9440` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 102,440.00 USD | 49,100.00 USD | 57,320.00 USD |
| `1D` | `0.9460` | 574,150.00 USD | 0.00 USD | 574,150.00 USD | 89,630.00 USD | 54,970.00 USD | 61,820.00 USD |
| `7D` | `0.9460` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 286,390.00 USD | 27,270.00 USD | 67,290.00 USD |
| `1D` | `0.9480` | 367,720.00 USD | 0.00 USD | 367,720.00 USD | 110,860.00 USD | 10,350.00 USD | 74,210.00 USD |
| `7D` | `0.9480` | 680,330.00 USD | 0.00 USD | 680,330.00 USD | 193,280.00 USD | 10,340.00 USD | 95,080.00 USD |
| `1D` | `0.9500` | 172,290.00 USD | 0.00 USD | 172,290.00 USD | 105,450.00 USD | 17,420.00 USD | 0.00 USD |
| `7D` | `0.9500` | 381,620.00 USD | 0.00 USD | 381,620.00 USD | 196,070.00 USD | 18,830.00 USD | 166,730.00 USD |
| `1D` | `0.9520` | 49,410.00 USD | 0.00 USD | 49,410.00 USD | 31,280.00 USD | 18,130.00 USD | 0.00 USD |
| `7D` | `0.9520` | 327,800.00 USD | 327,800.00 USD | 0.00 USD | 175,720.00 USD | 9,750.00 USD | 142,330.00 USD |
| `7D` | `0.9520` | 655,600.00 USD | 655,600.00 USD | 0.00 USD | 175,720.00 USD | 9,750.00 USD | 142,330.00 USD |
| `1D` | `0.9530` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9540` | 60,040.00 USD | 60,040.00 USD | 0.00 USD | 49,650.00 USD | 10,390.00 USD | 0.00 USD |
| `7D` | `0.9540` | 770,570.00 USD | 770,570.00 USD | 0.00 USD | 0.00 USD | 9,460.00 USD | 105,500.00 USD |
| `1D` | `0.9560` | 91,060.00 USD | 91,060.00 USD | 0.00 USD | 10,720.00 USD | 20,030.00 USD | 275.27 USD |
| `7D` | `0.9560` | 798,660.00 USD | 798,660.00 USD | 0.00 USD | 0.00 USD | 28,100.00 USD | 0.00 USD |
| `1D` | `0.9580` | 117,410.00 USD | 117,410.00 USD | 0.00 USD | 4,400.00 USD | 9,570.00 USD | 12,380.00 USD |
| `7D` | `0.9580` | 821,330.00 USD | 821,330.00 USD | 0.00 USD | 3,880.00 USD | 6,110.00 USD | 12,670.00 USD |
| `1D` | `0.9600` | 131,470.00 USD | 131,470.00 USD | 0.00 USD | 3,440.00 USD | 8,890.00 USD | 1,720.00 USD |
| `7D` | `0.9600` | 844,550.00 USD | 844,550.00 USD | 0.00 USD | 17,690.00 USD | 4,660.00 USD | 866.69 USD |
| `1D` | `0.9620` | 226,990.00 USD | 226,990.00 USD | 0.00 USD | 71,510.00 USD | 7,410.00 USD | 16,600.00 USD |
| `7D` | `0.9620` | 879,180.00 USD | 879,180.00 USD | 0.00 USD | 17,990.00 USD | 16,630.00 USD | 0.00 USD |
| `1D` | `0.9640` | 304,900.00 USD | 304,900.00 USD | 0.00 USD | 19,400.00 USD | 30,520.00 USD | 28,000.00 USD |
| `7D` | `0.9640` | 994,080.00 USD | 994,080.00 USD | 0.00 USD | 95,370.00 USD | 7,500.00 USD | 12,040.00 USD |
| `1D` | `0.9660` | 349,750.00 USD | 349,750.00 USD | 0.00 USD | 2,700.00 USD | 4,970.00 USD | 37,190.00 USD |
| `7D` | `0.9660` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 5,050.00 USD | 5,170.00 USD | 778.15 USD |
| `1D` | `0.9680` | 401,560.00 USD | 401,560.00 USD | 0.00 USD | 39,090.00 USD | 12,230.00 USD | 482.60 USD |
| `7D` | `0.9680` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 38,090.00 USD | 5,870.00 USD | 0.00 USD |
| `1D` | `0.9700` | 441,910.00 USD | 441,910.00 USD | 0.00 USD | 9,060.00 USD | 4,190.00 USD | 27,110.00 USD |
| `7D` | `0.9700` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 30,140.00 USD | 30,500.00 USD |
| `1D` | `0.9720` | 511,590.00 USD | 511,590.00 USD | 0.00 USD | 24,360.00 USD | 395.16 USD | 44,920.00 USD |
| `7D` | `0.9720` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 1,430.00 USD | 3,960.00 USD | 0.00 USD |
| `1D` | `0.9740` | 557,180.00 USD | 557,180.00 USD | 0.00 USD | 25,800.00 USD | 5,170.00 USD | 14,620.00 USD |
| `7D` | `0.9740` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 1,480.00 USD | 25,640.00 USD | 10,230.00 USD |
| `1D` | `0.9760` | 637,780.00 USD | 637,780.00 USD | 0.00 USD | 53,500.00 USD | 20,490.00 USD | 6,610.00 USD |
| `7D` | `0.9760` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 51,990.00 USD | 16,870.00 USD | 9,280.00 USD |
| `1D` | `0.9780` | 698,250.00 USD | 698,250.00 USD | 0.00 USD | 40,740.00 USD | 3,080.00 USD | 16,650.00 USD |
| `7D` | `0.9780` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,280.00 USD |
| `1D` | `0.9800` | 763,220.00 USD | 763,220.00 USD | 0.00 USD | 34,990.00 USD | 9,680.00 USD | 20,300.00 USD |
| `7D` | `0.9800` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 152,470.00 USD |
| `1D` | `0.9820` | 804,310.00 USD | 804,310.00 USD | 0.00 USD | 22,110.00 USD | 11,710.00 USD | 7,280.00 USD |
| `7D` | `0.9820` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 53,310.00 USD | 15,990.00 USD | 104,160.00 USD |
| `1D` | `0.9840` | 857,070.00 USD | 857,070.00 USD | 0.00 USD | 665.59 USD | 13,380.00 USD | 38,710.00 USD |
| `7D` | `0.9840` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 49,930.00 USD | 211.77 USD | 22,300.00 USD |
| `1D` | `0.9860` | 936,070.00 USD | 936,070.00 USD | 0.00 USD | 50,550.00 USD | 3,630.00 USD | 24,820.00 USD |
| `7D` | `0.9860` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,390.00 USD |
| `1D` | `0.9880` | 969,970.00 USD | 969,970.00 USD | 0.00 USD | 17,200.00 USD | 151.21 USD | 16,550.00 USD |
| `7D` | `0.9880` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 67,460.00 USD |
| `1D` | `0.9900` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 57,390.00 USD | 1,320.00 USD | 18,560.00 USD |
| `7D` | `0.9900` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 906.61 USD |
| `1D` | `0.9920` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 9,580.00 USD | 4,160.00 USD | 23,390.00 USD |
| `7D` | `0.9920` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 1,570.00 USD | 479.24 USD | 21,240.00 USD |
| `1D` | `0.9940` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 25,660.00 USD | 10,700.00 USD | 1,870.00 USD |
| `7D` | `0.9940` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 29,270.00 USD | 0.00 USD | 16,080.00 USD |
| `1D` | `0.9960` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 19,070.00 USD | 1,510.00 USD | 7,450.00 USD |
| `7D` | `0.9960` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 75,810.00 USD | 5,380.00 USD | 43,230.00 USD |
| `1D` | `0.9980` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 53,920.00 USD | 10,730.00 USD | 15,870.00 USD |
| `7D` | `0.9980` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 53,110.00 USD | 6,740.00 USD | 4,210.00 USD |
| `1D` | `1.00` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 60,660.00 USD | 18,230.00 USD | 6,760.00 USD |
| `7D` | `1.00` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 462.12 USD |
| `1D` | `1.00` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 13,430.00 USD | 1,930.00 USD | 7,450.00 USD |
| `7D` | `1.00` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 54,650.00 USD | 21,850.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 10,110.00 USD | 9,550.00 USD | 9,410.00 USD |
| `7D` | `1.00` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 70,950.00 USD | 3,970.00 USD | 1,470.00 USD |
| `1D` | `1.01` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 101,040.00 USD | 10,160.00 USD | 31,440.00 USD |
| `7D` | `1.01` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 46,710.00 USD | 0.00 USD | 11,560.00 USD |
| `1D` | `1.01` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 22,410.00 USD | 9,170.00 USD | 30,960.00 USD |
| `7D` | `1.01` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44,430.00 USD |
| `1D` | `1.01` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 12,560.00 USD | 17,230.00 USD | 971.85 USD |
| `7D` | `1.01` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 10,260.00 USD | 14,180.00 USD | 0.00 USD |
| `1D` | `1.01` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 16,880.00 USD | 22,370.00 USD | 265.91 USD |
| `7D` | `1.01` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 33,230.00 USD | 30,100.00 USD | 0.00 USD |
| `1D` | `1.01` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 6,560.00 USD | 5,790.00 USD | 21,570.00 USD |
| `7D` | `1.01` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 2,870.00 USD | 28,450.00 USD | 735.11 USD |
| `1D` | `1.02` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 15,150.00 USD | 25,460.00 USD | 11,300.00 USD |
| `7D` | `1.02` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 526.60 USD | 28,470.00 USD | 11,910.00 USD |
| `1D` | `1.02` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 23,750.00 USD | 4,210.00 USD | 22,530.00 USD |
| `7D` | `1.02` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 25,010.00 USD | 21,560.00 USD |
| `1D` | `1.02` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 46,900.00 USD | 9,980.00 USD | 18,380.00 USD |
| `7D` | `1.02` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 33,820.00 USD | 84,220.00 USD | 44,250.00 USD |
| `1D` | `1.02` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 40,340.00 USD | 20,320.00 USD | 29,140.00 USD |
| `7D` | `1.02` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 56,930.00 USD | 52,610.00 USD | 112,030.00 USD |
| `1D` | `1.02` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 44,050.00 USD | 11,230.00 USD | 34,590.00 USD |
| `7D` | `1.02` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 78,220.00 USD | 56,700.00 USD | 86,740.00 USD |
| `1D` | `1.03` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 40,090.00 USD | 18,290.00 USD | 21,370.00 USD |
| `7D` | `1.03` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 22,650.00 USD | 124,880.00 USD | 33,130.00 USD |
| `1D` | `1.03` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 19,210.00 USD | 8,920.00 USD | 15,510.00 USD |
| `7D` | `1.03` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 250,310.00 USD | 50,530.00 USD | 24,480.00 USD |
| `1D` | `1.03` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 64,370.00 USD | 12,650.00 USD | 18,360.00 USD |
| `7D` | `1.03` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 134,200.00 USD | 33,660.00 USD | 19,120.00 USD |
| `1D` | `1.03` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 30,760.00 USD | 7,090.00 USD | 32,130.00 USD |
| `7D` | `1.03` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD |
| `1D` | `1.03` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 12,440.00 USD | 8,650.00 USD | 12,980.00 USD |
| `7D` | `1.03` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 217,210.00 USD | 8,290.00 USD | 4,310.00 USD |
| `1D` | `1.04` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 4,520.00 USD | 10,280.00 USD | 2,970.00 USD |
| `7D` | `1.04` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 262,550.00 USD | 3,170.00 USD | 42,930.00 USD |
| `1D` | `1.04` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 42,730.00 USD | 767.34 USD | 2,900.00 USD |
| `7D` | `1.04` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 178,400.00 USD | 1,290.00 USD | 199,090.00 USD |
| `1D` | `1.04` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 6,280.00 USD | 6,670.00 USD | 8,460.00 USD |
| `7D` | `1.04` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 279,840.00 USD | 9,430.00 USD | 93,080.00 USD |
| `1D` | `1.04` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 10,930.00 USD | 5,820.00 USD | 3,380.00 USD |
| `7D` | `1.04` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD |
| `1D` | `1.04` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 2,950.00 USD | 1,330.00 USD | 10,670.00 USD |
| `7D` | `1.04` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD |
| `1D` | `1.05` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 5,280.00 USD | 4,540.00 USD | 1,200.00 USD |
| `7D` | `1.05` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD |
| `1D` | `1.05` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 3,910.00 USD | 73.95 USD | 6,340.00 USD |
| `7D` | `1.05` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 199,320.00 USD | 28,070.00 USD | 161,420.00 USD |
| `1D` | `1.05` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 28,700.00 USD | 4,090.00 USD | 6,110.00 USD |
| `7D` | `1.05` | 6,830,000.00 USD | 6,830,000.00 USD | 0.00 USD | 91,750.00 USD | 29,070.00 USD | 40,740.00 USD |
| `1D` | `1.05` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 4,900.00 USD | 1,200.00 USD | 13,950.00 USD |
| `7D` | `1.05` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 140,530.00 USD | 49,780.00 USD | 134,080.00 USD |
| `1D` | `1.05` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 11,090.00 USD | 202.75 USD | 2,970.00 USD |
| `7D` | `1.05` | 7,330,000.00 USD | 7,330,000.00 USD | 0.00 USD | 88,940.00 USD | 44,290.00 USD | 36,750.00 USD |
| `1D` | `1.06` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 5,670.00 USD | 4,530.00 USD | 1,960.00 USD |
| `7D` | `1.06` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 187,610.00 USD | 48,000.00 USD | 121,890.00 USD |
| `7D` | `1.06` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 205,690.00 USD | 63,350.00 USD | 94,840.00 USD |
| `7D` | `1.06` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 217,790.00 USD | 73,000.00 USD | 125,100.00 USD |
| `7D` | `1.06` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 131,720.00 USD | 83,000.00 USD | 66,000.00 USD |
| `7D` | `1.06` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 102,750.00 USD | 49,310.00 USD | 92,130.00 USD |
| `7D` | `1.07` | 9,170,000.00 USD | 9,170,000.00 USD | 0.00 USD | 77,920.00 USD | 32,860.00 USD | 73,060.00 USD |
| `7D` | `1.07` | 9,520,000.00 USD | 9,520,000.00 USD | 0.00 USD | 221,410.00 USD | 30,180.00 USD | 93,450.00 USD |
| `7D` | `1.07` | 9,710,000.00 USD | 9,710,000.00 USD | 0.00 USD | 121,300.00 USD | 33,170.00 USD | 42,800.00 USD |
| `7D` | `1.07` | 9,940,000.00 USD | 9,940,000.00 USD | 0.00 USD | 103,500.00 USD | 37,730.00 USD | 83,520.00 USD |
| `7D` | `1.07` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 92,440.00 USD | 21,500.00 USD | 83,440.00 USD |
| `7D` | `1.08` | 10,290,000.00 USD | 10,290,000.00 USD | 0.00 USD | 103,110.00 USD | 18,720.00 USD | 27,400.00 USD |
| `7D` | `1.08` | 10,560,000.00 USD | 10,560,000.00 USD | 0.00 USD | 158,650.00 USD | 40,740.00 USD | 69,670.00 USD |
| `7D` | `1.08` | 10,790,000.00 USD | 10,790,000.00 USD | 0.00 USD | 176,790.00 USD | 26,190.00 USD | 33,510.00 USD |
| `7D` | `1.08` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 62,710.00 USD | 20,510.00 USD | 39,030.00 USD |
| `7D` | `1.08` | 11,100,000.00 USD | 11,100,000.00 USD | 0.00 USD | 46,000.00 USD | 31,940.00 USD | 103,610.00 USD |
| `7D` | `1.09` | 11,330,000.00 USD | 11,330,000.00 USD | 0.00 USD | 161,270.00 USD | 28,200.00 USD | 42,090.00 USD |
| `7D` | `1.09` | 11,560,000.00 USD | 11,560,000.00 USD | 0.00 USD | 59,850.00 USD | 57,700.00 USD | 117,570.00 USD |
| `7D` | `1.09` | 11,720,000.00 USD | 11,720,000.00 USD | 0.00 USD | 109,670.00 USD | 18,350.00 USD | 31,220.00 USD |
| `7D` | `1.09` | 11,840,000.00 USD | 11,840,000.00 USD | 0.00 USD | 36,490.00 USD | 24,570.00 USD | 62,450.00 USD |
| `7D` | `1.09` | 12,000,000.00 USD | 12,000,000.00 USD | 0.00 USD | 67,090.00 USD | 37,290.00 USD | 55,440.00 USD |
| `7D` | `1.10` | 12,170,000.00 USD | 12,170,000.00 USD | 0.00 USD | 64,450.00 USD | 32,080.00 USD | 65,790.00 USD |
| `7D` | `1.10` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 119,850.00 USD | 21,050.00 USD | 97,790.00 USD |
| `7D` | `1.10` | 12,690,000.00 USD | 12,690,000.00 USD | 0.00 USD | 182,190.00 USD | 62,380.00 USD | 40,340.00 USD |
| `7D` | `1.10` | 12,760,000.00 USD | 12,760,000.00 USD | 0.00 USD | 59,740.00 USD | 10,900.00 USD | 2,270.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `176.90M` | Total OI Tokens: `185,920,429.8 DOT`
  * 1h OI Change: `+1.45%` | 4h OI Change: `-8.20%` | 24h OI Change: `-16.17%`
  * Exchange Breakdown: Binance=`35.23M` | Bybit=`22.17M` | OKX=`10.20M` | Hyperliquid=`5.91M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.75K` | Last 24h: `2.25K` | Last 3d: `-11.45K` | Last 7d: `-19.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0212%` |
| **USDT Bybit** | `0.0009%` | **USDT KuCoin** | `-0.0174%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0036%` | **USDT Bitget** | `0.0092%` |
| **CoinM Binance** | `0.0018%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `49.63%` | `50.37%` | `0.99` | 5,400,000.00 USD |
| `15M` | `Binance` | `63.59%` | `36.41%` | `1.75` | 2,260,000.00 USD |
| `15M` | `OKX` | `36.52%` | `63.48%` | `0.58` | 263,830.00 USD |
| `15M` | `Bybit` | `51.04%` | `48.96%` | `1.04` | 388,360.00 USD |
| `15M` | `KuCoin` | `36.9%` | `63.1%` | `0.58` | 15,100.00 USD |
| `15M` | `Gate` | `53.49%` | `46.51%` | `1.15` | 88,850.00 USD |
| `15M` | `Bitget` | `65.38%` | `34.62%` | `1.89` | 64,290.00 USD |
| `15M` | `BingX` | `47.22%` | `52.78%` | `0.89` | 857,200.00 USD |
| `15M` | `MEXC` | `42.42%` | `57.58%` | `0.74` | 154,170.00 USD |
| `15M` | `Bitunix` | `33.14%` | `66.86%` | `0.50` | 96,630.00 USD |
| `15M` | `Hyperliquid` | `67.67%` | `32.33%` | `2.09` | 9,830.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `27.65%` | `72.35%` | `0.38` | 1,160,000.00 USD |
| `15M` | `Crypto.com` | `88.96%` | `11.04%` | `8.06` | 7.69 USD |
| `15M` | `WhiteBIT` | `74.32%` | `25.68%` | `2.89` | 14,210.00 USD |
| `15M` | `HTX` | `36.68%` | `63.32%` | `0.58` | 2,220.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `33.32%` | `66.68%` | `0.50` | 309.14 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `50.75%` | `49.25%` | `1.03` | 11,190.00 USD |
| `15M` | `Whale Positions` | `63.59%` | `36.41%` | `1.75` | 2,260,000.00 USD |
| `15M` | `Global Accounts` | `49.63%` | `50.37%` | `0.99` | 5,400,000.00 USD |
| `1H` | `DOT` | `48.96%` | `51.04%` | `0.96` | 18,080,000.00 USD |
| `1H` | `Binance` | `55.2%` | `44.8%` | `1.23` | 6,760,000.00 USD |
| `1H` | `OKX` | `40.2%` | `59.8%` | `0.67` | 1,090,000.00 USD |
| `1H` | `Bybit` | `47.13%` | `52.87%` | `0.89` | 1,320,000.00 USD |
| `1H` | `KuCoin` | `50.84%` | `49.16%` | `1.03` | 61,330.00 USD |
| `1H` | `Gate` | `42.28%` | `57.72%` | `0.73` | 407,910.00 USD |
| `1H` | `Bitget` | `46.45%` | `53.55%` | `0.87` | 266,880.00 USD |
| `1H` | `BingX` | `45.45%` | `54.55%` | `0.83` | 3,540,000.00 USD |
| `1H` | `MEXC` | `53.64%` | `46.36%` | `1.16` | 639,050.00 USD |
| `1H` | `Bitunix` | `47.82%` | `52.18%` | `0.92` | 295,290.00 USD |
| `1H` | `Hyperliquid` | `43.9%` | `56.1%` | `0.78` | 211,170.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `42.81%` | `57.19%` | `0.75` | 3,340,000.00 USD |
| `1H` | `Crypto.com` | `48.23%` | `51.77%` | `0.93` | 47.65 USD |
| `1H` | `WhiteBIT` | `78.45%` | `21.55%` | `3.64` | 79,090.00 USD |
| `1H` | `HTX` | `44.65%` | `55.35%` | `0.81` | 6,590.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `92.99%` | `7.01%` | `13.27` | 42,580.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `56.16%` | `43.84%` | `1.28` | 37,800.00 USD |
| `1H` | `Whale Positions` | `55.2%` | `44.8%` | `1.23` | 6,760,000.00 USD |
| `1H` | `Global Accounts` | `48.96%` | `51.04%` | `0.96` | 18,080,000.00 USD |
| `4H` | `DOT` | `55.02%` | `44.98%` | `1.22` | 310,050,000.00 USD |
| `4H` | `Binance` | `52.91%` | `47.09%` | `1.12` | 125,620,000.00 USD |
| `4H` | `OKX` | `54.65%` | `45.35%` | `1.21` | 37,510,000.00 USD |
| `4H` | `Bybit` | `54.63%` | `45.37%` | `1.20` | 41,770,000.00 USD |
| `4H` | `KuCoin` | `53.24%` | `46.76%` | `1.14` | 1,990,000.00 USD |
| `4H` | `Gate` | `57.77%` | `42.23%` | `1.37` | 12,380,000.00 USD |
| `4H` | `Bitget` | `54.46%` | `45.54%` | `1.20` | 17,260,000.00 USD |
| `4H` | `BingX` | `58.06%` | `41.94%` | `1.38` | 16,760,000.00 USD |
| `4H` | `MEXC` | `52.64%` | `47.36%` | `1.11` | 10,830,000.00 USD |
| `4H` | `Bitunix` | `53.75%` | `46.25%` | `1.16` | 6,860,000.00 USD |
| `4H` | `Hyperliquid` | `58.68%` | `41.32%` | `1.42` | 28,220,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.76%` | `48.24%` | `1.07` | 1,640,000.00 USD |
| `4H` | `Crypto.com` | `49.65%` | `50.35%` | `0.99` | 20,180.00 USD |
| `4H` | `WhiteBIT` | `89.78%` | `10.22%` | `8.78` | 5,510,000.00 USD |
| `4H` | `HTX` | `47.93%` | `52.07%` | `0.92` | 228,670.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `68.03%` | `31.97%` | `2.13` | 582,660.00 USD |
| `4H` | `Aster` | `31.21%` | `68.79%` | `0.45` | 1,320,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.21%` | `48.79%` | `1.05` | 1,550,000.00 USD |
| `4H` | `Whale Positions` | `52.91%` | `47.09%` | `1.12` | 125,620,000.00 USD |
| `4H` | `Global Accounts` | `55.02%` | `44.98%` | `1.22` | 310,050,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.9193` | `0.9207` | `0.9193` | `0.9244` | `0.9172` | 1,009,160.47 USD | 369,502.50 USD | 639,657.97 USD | -270,155.47 USD | `-26.77%` | `7B / 22S` |
| `5:00 UTC` | `0.9247` | `0.9214` | `0.9247` | `0.9264` | `0.9171` | 592,145.67 USD | 331,376.92 USD | 260,768.76 USD | 70,608.16 USD | `+11.92%` | `20B / 3S` |
| `0:00 UTC` | `0.9301` | `0.9294` | `0.9301` | `0.9320` | `0.9246` | 722,739.41 USD | 436,845.68 USD | 285,893.73 USD | 150,951.95 USD | `+20.89%` | `15B / 5S` |
| `5:00 UTC` | `0.9322` | `0.9317` | `0.9322` | `0.9342` | `0.9301` | 515,769.04 USD | 235,727.30 USD | 280,041.74 USD | -44,314.44 USD | `-8.59%` | `11B / 7S` |
| `0:00 UTC` | `0.9301` | `0.9291` | `0.9301` | `0.9327` | `0.9264` | 525,506.21 USD | 261,479.52 USD | 264,026.69 USD | -2,547.17 USD | `-0.48%` | `9B / 12S` |
| `5:00 UTC` | `0.9325` | `0.9314` | `0.9325` | `0.9344` | `0.9288` | 497,143.85 USD | 263,231.22 USD | 233,912.62 USD | 29,318.60 USD | `+5.90%` | `7B / 6S` |
| `0:00 UTC` | `0.9354` | `0.9348` | `0.9354` | `0.9365` | `0.9333` | 404,247.05 USD | 223,080.64 USD | 181,166.41 USD | 41,914.22 USD | `+10.37%` | `5B / 3S` |
| `5:00 UTC` | `0.9425` | `0.9411` | `0.9425` | `0.9454` | `0.9362` | 1,398,502.73 USD | 702,262.50 USD | 696,240.23 USD | 6,022.27 USD | `+0.43%` | `30B / 12S` |
| `0:00 UTC` | `0.9563` | `0.9497` | `0.9563` | `0.9570` | `0.9410` | 1,155,581.71 USD | 451,950.39 USD | 703,631.31 USD | -251,680.92 USD | `-21.78%` | `29B / 39S` |
| `5:00 UTC` | `0.9507` | `0.9509` | `0.9507` | `0.9536` | `0.9487` | 196,927.22 USD | 80,434.77 USD | 116,492.45 USD | -36,057.68 USD | `-18.31%` | `11B / 8S` |

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
| `5m` | -26,510.00 USD | -36,860.00 USD | **`DISTRIBUTION`** |
| `15m` | -17,650.00 USD | -240,330.00 USD | **`DISTRIBUTION`** |
| `30m` | -33,540.00 USD | -536,160.00 USD | **`DISTRIBUTION`** |
| `1h` | 29,090.00 USD | -546,420.00 USD | **`DISTRIBUTION`** |
| `2h` | 39,770.00 USD | -204,250.00 USD | **`DISTRIBUTION`** |
| `4h` | -25,560.00 USD | 407,090.00 USD | **`ACCUMULATION`** |
| `6h` | -317,460.00 USD | 727,330.00 USD | **`ACCUMULATION`** |
| `8h` | -150,300.00 USD | -5,390,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,070,000.00 USD | -5,790,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,120,000.00 USD | -6,640,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,950,000.00 USD | -23,140,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,710,000.00 USD | -77,630,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-26.51K` | 15m=`-17.65K` | 1h=`+29.09K` | 24h=`-1.12M`
* Futures Capital Netflows: 5m=`-36.86K` | 15m=`-240.33K` | 1h=`-546.42K` | 24h=`-6.64M`
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
  * `2026-10-30 09:50:40 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:48:40 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:49:40 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.8925` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.8493` (Risk Distance: `0.0432` pts)
  * +2.5R Take Profit: `1.00`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9253` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9685` (Risk Distance: `0.0432` pts)
  * +2.5R Take Profit: `0.8173`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9581`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
