# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 01:36:03 IST` (`2026-10-29 20:06:03 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9650` | **Live Ask Quote**: `0.9860` | **Mid Price**: `0.9755`
- **Spread Points**: `21.00` | **Spread BPS**: `215.27 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.9774` | VWAP Z-Score: `-0.24` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0070` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `43.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.02` | Lower -3.00σ Band: `0.9355`
  * Upper +2.51σ Band: `1.01` | Lower -2.51σ Band: `0.9424`
  * Upper +2.01σ Band: `1.01` | Lower -2.01σ Band: `0.9493`
  * Upper +2.00σ Band: `1.01` | Lower -2.00σ Band: `0.9495`
  * Upper +1.28σ Band: `0.9953` | Lower -1.28σ Band: `0.9595`
  * Upper +1.00σ Band: `0.9914` | Lower -1.00σ Band: `0.9634`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9759` | EMA-20=`0.9803` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9812` (Slope: `+0.0000`) | EMA-100=`0.9823`
  * Institutional Anchors: EMA-144=`0.9834` | EMA-200=`0.9840` (Slope: `-0.0883`) | EMA-233=`0.9842`
- **Range Boundaries**: 24H High=`1.03` | 24H Low=`0.9510` | Weekly High=`1.03` | Weekly Low=`0.9510`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9929` (Distance: `-1.60%`)
  * Point of Control (POC) = `0.9739` (Distance: `+0.32%`)
  * Value Area Low (VAL) = `0.9530` (Distance: `+2.51%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.00` | POC=`0.9890` | VAL=`0.9812`
  * Prior Day Extremes: PDH=`1.03` | PDL=`0.9690` | PDC=`1.01`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.01` | Weekly POC=`0.9929` | Weekly VAL=`0.9774`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.02` | Low=`0.9510`
  * London Session (08:00-16:00 UTC): High=`0.9850` | Low=`0.9600`
  * New York Session (13:00-21:00 UTC): High=`1.01` | Low=`0.9680`
  * Initial Balance (First Hour): IB High=`0.9800` | IB Low=`0.9670`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9716` - `0.9794`
  * Optimal Trade Entry (OTE 0.705): `0.9775`
  * Structural Invalidation Anchor (0.786): `0.9833`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9858` | `0.9880` | `0.9852` | `0.9856` | `139,190` | 137,348.77 USD | -2,903.89 USD | `-2.11%` | -1,035,048.54 USD | `-0.19` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `0.9856` | `0.9858` | `0.9839` | `0.9844` | `117,993` | 116,205.36 USD | -9,448.14 USD | `-8.13%` | -1,044,496.68 USD | `-0.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.9845` | `0.9849` | `0.9744` | `0.9766` | `570,334` | 558,634.59 USD | -118,458.96 USD | `-21.21%` | -1,162,955.64 USD | `-1.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9839` | `0.9886` | `0.9839` | `0.9861` | `413,382` | 407,897.05 USD | 24,160.41 USD | `+5.92%` | -639,794.95 USD | `+0.30` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.9861` | `0.9880` | `0.9839` | `0.9844` | `393,652` | 388,071.33 USD | -32,968.97 USD | `-8.50%` | -672,763.92 USD | `-0.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.9845` | `0.9849` | `0.9744` | `0.9763` | `568,715` | 557,054.11 USD | -119,985.15 USD | `-21.54%` | -792,749.07 USD | `-0.38` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.9918` | `0.9929` | `0.9766` | `0.9840` | `3,542,573` | 3,482,685.13 USD | 238,678.91 USD | `+6.85%` | -618,930.49 USD | `+0.79` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.9839` | `0.9886` | `0.9780` | `0.9844` | `1,864,944` | 1,834,632.46 USD | 75,709.02 USD | `+4.13%` | -543,221.47 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9845` | `0.9849` | `0.9744` | `0.9763` | `568,715` | 557,054.11 USD | -119,985.15 USD | `-21.54%` | -663,206.62 USD | `-0.31` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | 516,506.12 USD | `-1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -280,559.32 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.9744` | `0.9766` | `570,334` | 558,634.59 USD | -118,458.96 USD | `-21.21%` | -399,018.28 USD | `-0.13` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.9699` | `0.9906` | `0.9674` | `0.9732` | `8,505,701` | 8,320,368.15 USD | 13,201.93 USD | `+0.16%` | 609,018.52 USD | `-1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | 694,082.93 USD | `-0.56` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | 516,506.12 USD | `-1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -280,559.32 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.9744` | `0.9766` | `570,334` | 558,634.59 USD | -118,458.96 USD | `-21.21%` | -399,018.28 USD | `-0.13` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`0.9755`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:33:46 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9992` | 5,498.96 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale SELL: 5.50K USD at 0.9992 USD [API] | `2026-10-27 22:26:23` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.04` (Vol: 74,700.00 USD, Dist: `+5.25%`) | Long MP=`0.9649` (Vol: 133,600.00 USD, Dist: `--2.08%`)
  * 48H Horizon: Short MP=`1.04` (Vol: 74,700.00 USD, Dist: `+5.25%`) | Long MP=`0.9649` (Vol: 133,600.00 USD, Dist: `--2.08%`)
  * 3D Horizon: Short MP=`1.04` (Vol: 74,700.00 USD, Dist: `+5.25%`) | Long MP=`0.9510` (Vol: 130,500.00 USD, Dist: `--3.49%`)
  * 7D Horizon: Short MP=`1.07` (Vol: 211,000.00 USD, Dist: `+8.42%`) | Long MP=`0.9606` (Vol: 177,500.00 USD, Dist: `--2.52%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2385` | 119.25 USD | 539,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3375` | 745.54 USD | 539,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3605` | 650.95 USD | 538,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3735` | 2,130.00 USD | 538,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 2,790.00 USD | 535,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4315` | 171.09 USD | 533,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4335` | 138.42 USD | 532,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4695` | 2,580.00 USD | 532,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5115` | 811.34 USD | 530,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 4,130.00 USD | 529,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5165` | 1,020.00 USD | 525,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5465` | 106.84 USD | 524,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5575` | 13,600.00 USD | 524,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 577.36 USD | 510,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 137.53 USD | 510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5955` | 3,390.00 USD | 509,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6055` | 1,480.00 USD | 506,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6065` | 1,800.00 USD | 504,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 105.96 USD | 503,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 147.48 USD | 503,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6245` | 525.77 USD | 502,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 757.80 USD | 502,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 106.00 USD | 501,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6385` | 156.18 USD | 501,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 20,270.00 USD | 501,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 4,230.00 USD | 481,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 202.47 USD | 476,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 149.44 USD | 476,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 63,890.00 USD | 476,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 423.10 USD | 412,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 512.97 USD | 412,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6855` | 2,110.00 USD | 411,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6955` | 322.16 USD | 409,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7045` | 157.39 USD | 409,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7055` | 881.88 USD | 409,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 16,520.00 USD | 408,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 988.87 USD | 391,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7175` | 322.88 USD | 390,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7205` | 866.26 USD | 390,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 1,090.00 USD | 389,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7275` | 126.44 USD | 388,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 291.18 USD | 388,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 2,300.00 USD | 388,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,140.00 USD | 385,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7365` | 2,050.00 USD | 384,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 283.30 USD | 382,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7495` | 1,390.00 USD | 382,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 331.18 USD | 380,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 2,390.00 USD | 380,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7605` | 834.88 USD | 378,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7655` | 2,300.00 USD | 377,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 1,580.00 USD | 375,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 292.03 USD | 373,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7895` | 20,380.00 USD | 373,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7965` | 106.49 USD | 352,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8025` | 238.90 USD | 352,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8045` | 566.61 USD | 352,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8055` | 699.01 USD | 351,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 351,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8195` | 13,560.00 USD | 350,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 336,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8285` | 1,890.00 USD | 335,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8325` | 8,990.00 USD | 333,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 324,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8375` | 167.00 USD | 323,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,240.00 USD | 323,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8445` | 168.31 USD | 322,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 322,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 320,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8595` | 61,200.00 USD | 320,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8625` | 309.55 USD | 259,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 258,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 258,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8665` | 118.54 USD | 258,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8760` | 5,180,000.00 USD | 5,180,000.00 USD | 6,030.00 USD | 6,200.00 USD | 5,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 171.88 USD | 258,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8780` | 5,160,000.00 USD | 5,160,000.00 USD | 15,500.00 USD | 50.60 USD | 5,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8790` | 2,670,000.00 USD | 2,670,000.00 USD | 17,770.00 USD | 8,500.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8795` | 948.01 USD | 257,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8800` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 3,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8810` | 2,630,000.00 USD | 2,630,000.00 USD | 6,240.00 USD | 3,320.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8820` | 5,130,000.00 USD | 5,130,000.00 USD | 8,660.00 USD | 3,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8830` | 2,620,000.00 USD | 2,620,000.00 USD | 6,600.00 USD | 4,200.00 USD | 36.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8840` | 5,120,000.00 USD | 5,120,000.00 USD | 4,540.00 USD | 5,480.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8850` | 2,610,000.00 USD | 2,610,000.00 USD | 7,980.00 USD | 2,370.00 USD | 2,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8860` | 5,110,000.00 USD | 5,110,000.00 USD | 15,460.00 USD | 7,970.00 USD | 2,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8870` | 2,590,000.00 USD | 2,590,000.00 USD | 19,160.00 USD | 4,450.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8880` | 5,080,000.00 USD | 5,080,000.00 USD | 7,150.00 USD | 1,990.00 USD | 11,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8890` | 2,560,000.00 USD | 2,560,000.00 USD | 3,730.00 USD | 3,680.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8900` | 5,060,000.00 USD | 5,060,000.00 USD | 23,060.00 USD | 6,420.00 USD | 20,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8910` | 2,550,000.00 USD | 2,550,000.00 USD | 1,820.00 USD | 1,560.00 USD | 2,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8920` | 5,010,000.00 USD | 5,010,000.00 USD | 45,890.00 USD | 9,570.00 USD | 15,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8925` | 526.84 USD | 256,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8930` | 2,540,000.00 USD | 2,540,000.00 USD | 7,320.00 USD | 2,470.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8940` | 4,940,000.00 USD | 4,940,000.00 USD | 7,120.00 USD | 8,030.00 USD | 26,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8950` | 2,530,000.00 USD | 2,530,000.00 USD | 22.75 USD | 2,460.00 USD | 2,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8960` | 4,900,000.00 USD | 4,900,000.00 USD | 30,390.00 USD | 9,210.00 USD | 12,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8970` | 2,530,000.00 USD | 2,530,000.00 USD | 5,360.00 USD | 3,690.00 USD | 1,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8975` | 9,210.00 USD | 256,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8980` | 4,850,000.00 USD | 4,850,000.00 USD | 31,140.00 USD | 6,910.00 USD | 36,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8990` | 2,520,000.00 USD | 2,520,000.00 USD | 5,550.00 USD | 757.19 USD | 1,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8995` | 3,820.00 USD | 247,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9000` | 4,770,000.00 USD | 4,770,000.00 USD | 39,940.00 USD | 14,050.00 USD | 14,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9010` | 2,510,000.00 USD | 2,510,000.00 USD | 15.65 USD | 39.59 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9020` | 4,700,000.00 USD | 4,700,000.00 USD | 16,980.00 USD | 11,760.00 USD | 15,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9030` | 2,510,000.00 USD | 2,510,000.00 USD | 6,430.00 USD | 3,760.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9035` | 180.16 USD | 243,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9040` | 4,660,000.00 USD | 4,660,000.00 USD | 17,160.00 USD | 5,930.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9050` | 2,490,000.00 USD | 2,490,000.00 USD | 8,300.00 USD | 3,640.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9060` | 4,630,000.00 USD | 4,630,000.00 USD | 53,450.00 USD | 30,600.00 USD | 41,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9070` | 2,480,000.00 USD | 2,480,000.00 USD | 3,810.00 USD | 488.01 USD | 803.91 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9080` | 4,500,000.00 USD | 4,500,000.00 USD | 21,830.00 USD | 3,470.00 USD | 6,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9090` | 2,470,000.00 USD | 2,470,000.00 USD | 18,830.00 USD | 4,030.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9095` | 951.34 USD | 243,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9100` | 4,470,000.00 USD | 4,470,000.00 USD | 6,870.00 USD | 10,340.00 USD | 17,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9110` | 2,440,000.00 USD | 2,440,000.00 USD | 9,060.00 USD | 791.28 USD | 5,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9120` | 4,430,000.00 USD | 4,430,000.00 USD | 21,820.00 USD | 4,010.00 USD | 371.71 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9130` | 2,430,000.00 USD | 2,430,000.00 USD | 4,710.00 USD | 487.57 USD | 2,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9135` | 143.42 USD | 242,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9140` | 4,410,000.00 USD | 4,410,000.00 USD | 46,660.00 USD | 8,800.00 USD | 26,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9150` | 2,420,000.00 USD | 2,420,000.00 USD | 14,250.00 USD | 1,040.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9160` | 4,330,000.00 USD | 4,330,000.00 USD | 12,570.00 USD | 12,620.00 USD | 17,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9170` | 2,400,000.00 USD | 2,400,000.00 USD | 3,560.00 USD | 435.13 USD | 452.67 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9180` | 4,280,000.00 USD | 4,280,000.00 USD | 29,970.00 USD | 9,010.00 USD | 11,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9185` | 145.86 USD | 242,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9190` | 2,390,000.00 USD | 2,390,000.00 USD | 2,850.00 USD | 147.28 USD | 54.94 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9195` | 7,330.00 USD | 241,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9200` | 4,230,000.00 USD | 4,230,000.00 USD | 40,100.00 USD | 4,910.00 USD | 22,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9210` | 2,390,000.00 USD | 2,390,000.00 USD | 1,470.00 USD | 77.80 USD | 2,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9220` | 4,160,000.00 USD | 4,160,000.00 USD | 15,960.00 USD | 2,370.00 USD | 15,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9225` | 8,360.00 USD | 234,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9230` | 2,390,000.00 USD | 2,390,000.00 USD | 10,650.00 USD | 989.17 USD | 907.53 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9240` | 4,130,000.00 USD | 4,130,000.00 USD | 56,450.00 USD | 17,850.00 USD | 51,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9250` | 2,370,000.00 USD | 2,370,000.00 USD | 19,800.00 USD | 8,960.00 USD | 14,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9260` | 4,000,000.00 USD | 4,000,000.00 USD | 32,320.00 USD | 3,140.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9270` | 2,330,000.00 USD | 2,330,000.00 USD | 15,140.00 USD | 5,150.00 USD | 10,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9280` | 3,950,000.00 USD | 3,950,000.00 USD | 85,040.00 USD | 14,050.00 USD | 26,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9290` | 2,300,000.00 USD | 2,300,000.00 USD | 25,560.00 USD | 4,250.00 USD | 6,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9295` | 253.01 USD | 226,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9300` | 3,820,000.00 USD | 3,820,000.00 USD | 27,510.00 USD | 12,060.00 USD | 18,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9310` | 2,260,000.00 USD | 2,260,000.00 USD | 10,710.00 USD | 12,130.00 USD | 21,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9320` | 3,760,000.00 USD | 3,760,000.00 USD | 29,490.00 USD | 7,900.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9325` | 324.42 USD | 324.42 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9330` | 2,220,000.00 USD | 2,220,000.00 USD | 21,800.00 USD | 9,080.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9335` | 361.45 USD | 226,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9340` | 3,720,000.00 USD | 3,720,000.00 USD | 53,710.00 USD | 31,710.00 USD | 24,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9350` | 2,180,000.00 USD | 2,180,000.00 USD | 36,430.00 USD | 10,940.00 USD | 13,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9360` | 3,610,000.00 USD | 3,610,000.00 USD | 59,280.00 USD | 6,250.00 USD | 14,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9365` | 6,560.00 USD | 225,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9370` | 2,120,000.00 USD | 2,120,000.00 USD | 38,680.00 USD | 12,840.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9375` | 196.97 USD | 219,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9380` | 3,530,000.00 USD | 3,530,000.00 USD | 20,200.00 USD | 20,670.00 USD | 12,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9390` | 2,040,000.00 USD | 2,040,000.00 USD | 17,600.00 USD | 14,430.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9400` | 3,480,000.00 USD | 3,480,000.00 USD | 26,270.00 USD | 6,010.00 USD | 7,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9405` | 141.83 USD | 218,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9410` | 2,000,000.00 USD | 2,000,000.00 USD | 45,250.00 USD | 15,190.00 USD | 2,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9420` | 3,440,000.00 USD | 3,440,000.00 USD | 51,440.00 USD | 21,220.00 USD | 10,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9430` | 1,940,000.00 USD | 1,940,000.00 USD | 21,430.00 USD | 8,230.00 USD | 3,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9440` | 3,360,000.00 USD | 3,360,000.00 USD | 57,220.00 USD | 26,910.00 USD | 26,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9445` | 1,060.00 USD | 218,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9450` | 1,900,000.00 USD | 1,900,000.00 USD | 41,820.00 USD | 22,990.00 USD | 41,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9455` | 106,880.00 USD | 217,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9460` | 3,250,000.00 USD | 3,250,000.00 USD | 80,430.00 USD | 19,530.00 USD | 44,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9470` | 1,800,000.00 USD | 1,800,000.00 USD | 82,980.00 USD | 27,830.00 USD | 42,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9475` | 323.19 USD | 110,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9480` | 3,100,000.00 USD | 3,100,000.00 USD | 202,170.00 USD | 42,900.00 USD | 92,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9490` | 1,640,000.00 USD | 1,640,000.00 USD | 77,380.00 USD | 19,930.00 USD | 28,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9495` | 105,430.00 USD | 110,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9500` | 2,760,000.00 USD | 2,760,000.00 USD | 125,620.00 USD | 46,290.00 USD | 114,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9510` | 1,520,000.00 USD | 1,520,000.00 USD | 35,280.00 USD | 33,660.00 USD | 43,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9515` | 405.62 USD | 5,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9520` | 2,480,000.00 USD | 2,480,000.00 USD | 144,770.00 USD | 19,800.00 USD | 57,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9530` | 1,410,000.00 USD | 1,410,000.00 USD | 55,340.00 USD | 18,390.00 USD | 21,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9540` | 2,250,000.00 USD | 2,250,000.00 USD | 116,590.00 USD | 92,780.00 USD | 108,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9550` | 1,310,000.00 USD | 1,310,000.00 USD | 81,780.00 USD | 37,060.00 USD | 36,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9555` | 3,160.00 USD | 4,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9560` | 1,940,000.00 USD | 1,940,000.00 USD | 207,570.00 USD | 32,950.00 USD | 87,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9570` | 1,150,000.00 USD | 1,150,000.00 USD | 112,970.00 USD | 38,550.00 USD | 47,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9580` | 1,610,000.00 USD | 1,610,000.00 USD | 107,300.00 USD | 48,150.00 USD | 119,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9585` | 1,530.00 USD | 1,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9590` | 955,140.00 USD | 955,140.00 USD | 59,310.00 USD | 22,860.00 USD | 31,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9600` | 1,330,000.00 USD | 1,330,000.00 USD | 222,250.00 USD | 82,170.00 USD | 59,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9610` | 841,100.00 USD | 841,100.00 USD | 62,360.00 USD | 27,360.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9620` | 968,430.00 USD | 968,430.00 USD | 140,700.00 USD | 46,240.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9630` | 739,180.00 USD | 739,180.00 USD | 43,690.00 USD | 24,730.00 USD | 24,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9640` | 755,410.00 USD | 755,410.00 USD | 104,730.00 USD | 778.20 USD | 6,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9650` | 645,980.00 USD | 645,980.00 USD | 60,870.00 USD | 14,680.00 USD | 31,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9660` | 642,950.00 USD | 642,950.00 USD | 40,050.00 USD | 9,550.00 USD | 31,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9670` | 538,530.00 USD | 538,530.00 USD | 69,000.00 USD | 22,210.00 USD | 39,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9680` | 561,960.00 USD | 561,960.00 USD | 26,480.00 USD | 4,670.00 USD | 36,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9690` | 408,190.00 USD | 408,190.00 USD | 43,730.00 USD | 30,170.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9700` | 493,870.00 USD | 493,870.00 USD | 33,960.00 USD | 25,160.00 USD | 36,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9710` | 303,060.00 USD | 303,060.00 USD | 60,380.00 USD | 19,100.00 USD | 21,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9720` | 397,870.00 USD | 397,870.00 USD | 53,850.00 USD | 0.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9730` | 202,280.00 USD | 202,280.00 USD | 23,620.00 USD | 691.66 USD | 13,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9740` | 334,420.00 USD | 334,420.00 USD | 0.00 USD | 16,590.00 USD | 8,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9750` | 164,660.00 USD | 164,660.00 USD | 16,060.00 USD | 23,220.00 USD | 15,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9760` | 309,200.00 USD | 309,200.00 USD | 15,320.00 USD | 5,480.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9770` | 109,420.00 USD | 109,420.00 USD | 35,620.00 USD | 2,870.00 USD | 9,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9780` | 279,110.00 USD | 279,110.00 USD | 0.00 USD | 0.00 USD | 24,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9790` | 60,960.00 USD | 60,960.00 USD | 819.00 USD | 0.00 USD | 7,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9800` | 254,830.00 USD | 254,830.00 USD | 0.00 USD | 0.00 USD | 151,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9810` | 52,340.00 USD | 52,340.00 USD | 0.00 USD | 376.40 USD | 8,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9820` | 103,280.00 USD | 103,280.00 USD | 10,090.00 USD | 0.00 USD | 72,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9830` | 43,030.00 USD | 43,030.00 USD | 15,980.00 USD | 11,780.00 USD | 15,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9840` | 20,920.00 USD | 20,920.00 USD | 0.00 USD | 0.00 USD | 20,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9850` | 11,310.00 USD | 11,310.00 USD | 575.70 USD | 0.00 USD | 10,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9850` | 22,620.00 USD | 22,620.00 USD | 575.70 USD | 0.00 USD | 10,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9860` | 803.95 USD | 803.95 USD | 0.00 USD | 0.00 USD | 803.95 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9880` | 41,720.00 USD | 41,720.00 USD | 40,020.00 USD | 0.00 USD | 901.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9890` | 29,460.00 USD | 29,460.00 USD | 0.00 USD | 0.00 USD | 6,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9900` | 42,630.00 USD | 42,630.00 USD | 0.00 USD | 0.00 USD | 906.61 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9910` | 99,660.00 USD | 99,660.00 USD | 50,430.00 USD | 0.00 USD | 19,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9920` | 63,070.00 USD | 63,070.00 USD | 0.00 USD | 0.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9930` | 120,020.00 USD | 120,020.00 USD | 6,920.00 USD | 13,250.00 USD | 191.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9950` | 121,650.00 USD | 121,650.00 USD | 0.00 USD | 1,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9960` | 138,520.00 USD | 138,520.00 USD | 32,670.00 USD | 0.00 USD | 42,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9970` | 149,870.00 USD | 149,870.00 USD | 26,250.00 USD | 1,000.00 USD | 970.29 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9980` | 195,430.00 USD | 195,430.00 USD | 52,700.00 USD | 0.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9990` | 165,500.00 USD | 165,500.00 USD | 9,720.00 USD | 3,910.00 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 248,280.00 USD | 248,280.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 234,400.00 USD | 234,400.00 USD | 41,020.00 USD | 27,530.00 USD | 348.39 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 291,850.00 USD | 291,850.00 USD | 28,410.00 USD | 13,940.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 252,510.00 USD | 252,510.00 USD | 10,110.00 USD | 5,360.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 337,520.00 USD | 337,520.00 USD | 44,900.00 USD | 0.00 USD | 775.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 290,470.00 USD | 290,470.00 USD | 35,550.00 USD | 1,780.00 USD | 633.92 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 371,630.00 USD | 371,630.00 USD | 34,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 374,360.00 USD | 374,360.00 USD | 40,210.00 USD | 7,570.00 USD | 36,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 387,880.00 USD | 387,880.00 USD | 0.00 USD | 0.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 390,920.00 USD | 390,920.00 USD | 5,860.00 USD | 10,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 401,900.00 USD | 401,900.00 USD | 0.00 USD | 14,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 421,440.00 USD | 421,440.00 USD | 7,210.00 USD | 23,150.00 USD | 155.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 461,430.00 USD | 461,430.00 USD | 33,230.00 USD | 26,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 435,850.00 USD | 435,850.00 USD | 10,040.00 USD | 4,020.00 USD | 352.75 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 492,840.00 USD | 492,840.00 USD | 2,870.00 USD | 28,140.00 USD | 388.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 506,240.00 USD | 506,240.00 USD | 25,750.00 USD | 4,350.00 USD | 40,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 533,220.00 USD | 533,220.00 USD | 0.00 USD | 28,470.00 USD | 11,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 757.09 USD | 1,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.02` | 539,510.00 USD | 539,510.00 USD | 1,130.00 USD | 7,410.00 USD | 24,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 575,190.00 USD | 575,190.00 USD | 0.00 USD | 20,410.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 593,480.00 USD | 593,480.00 USD | 39,370.00 USD | 3,750.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 700,660.00 USD | 700,660.00 USD | 0.00 USD | 81,220.00 USD | 44,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 637,980.00 USD | 637,980.00 USD | 27,370.00 USD | 2,230.00 USD | 14,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 921,600.00 USD | 921,600.00 USD | 56,930.00 USD | 52,290.00 USD | 111,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 738,450.00 USD | 738,450.00 USD | 54,050.00 USD | 5,670.00 USD | 40,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 1,130,000.00 USD | 1,130,000.00 USD | 62,470.00 USD | 56,700.00 USD | 86,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 876,120.00 USD | 876,120.00 USD | 67,790.00 USD | 32,010.00 USD | 37,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,300,000.00 USD | 1,300,000.00 USD | 22,650.00 USD | 124,760.00 USD | 25,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 926,010.00 USD | 926,010.00 USD | 26,670.00 USD | 11,540.00 USD | 11,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,630,000.00 USD | 1,630,000.00 USD | 250,040.00 USD | 50,530.00 USD | 24,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,020,000.00 USD | 1,020,000.00 USD | 30,050.00 USD | 24,640.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,810,000.00 USD | 1,810,000.00 USD | 134,200.00 USD | 29,810.00 USD | 19,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,210,000.00 USD | 1,210,000.00 USD | 133,530.00 USD | 17,570.00 USD | 40,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,920,000.00 USD | 1,920,000.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,270,000.00 USD | 1,270,000.00 USD | 38,620.00 USD | 116.64 USD | 23,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,150,000.00 USD | 2,150,000.00 USD | 216,820.00 USD | 8,290.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,340,000.00 USD | 1,340,000.00 USD | 27,090.00 USD | 18,490.00 USD | 29,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 2,450,000.00 USD | 2,450,000.00 USD | 262,550.00 USD | 3,170.00 USD | 42,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,450,000.00 USD | 1,450,000.00 USD | 69,740.00 USD | 7,400.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 2,830,000.00 USD | 2,830,000.00 USD | 178,400.00 USD | 1,290.00 USD | 199,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,480,000.00 USD | 1,480,000.00 USD | 10,510.00 USD | 4,170.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,210,000.00 USD | 3,210,000.00 USD | 279,460.00 USD | 9,430.00 USD | 93,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,490,000.00 USD | 1,490,000.00 USD | 4,050.00 USD | 4,370.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,540,000.00 USD | 3,540,000.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,540,000.00 USD | 1,540,000.00 USD | 14,730.00 USD | 12,770.00 USD | 24,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,800,000.00 USD | 3,800,000.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,570,000.00 USD | 1,570,000.00 USD | 5,920.00 USD | 6,310.00 USD | 13,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,220,000.00 USD | 4,220,000.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,610,000.00 USD | 1,610,000.00 USD | 29,770.00 USD | 7,370.00 USD | 1,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 733.98 USD | 1,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,610,000.00 USD | 4,610,000.00 USD | 199,320.00 USD | 28,070.00 USD | 161,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,640,000.00 USD | 1,640,000.00 USD | 2,310.00 USD | 8,000.00 USD | 17,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,770,000.00 USD | 4,770,000.00 USD | 91,750.00 USD | 29,070.00 USD | 40,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,720,000.00 USD | 1,720,000.00 USD | 62,570.00 USD | 4,140.00 USD | 17,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 5,090,000.00 USD | 5,090,000.00 USD | 140,970.00 USD | 49,780.00 USD | 133,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,750,000.00 USD | 1,750,000.00 USD | 5,710.00 USD | 6,220.00 USD | 19,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 5,250,000.00 USD | 5,250,000.00 USD | 82,020.00 USD | 42,140.00 USD | 36,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,790,000.00 USD | 1,790,000.00 USD | 14,400.00 USD | 979.80 USD | 21,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.06` | 74,410.00 USD | 76,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.06` | 5,610,000.00 USD | 5,610,000.00 USD | 187,610.00 USD | 48,000.00 USD | 121,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,810,000.00 USD | 1,810,000.00 USD | 5,730.00 USD | 2,500.00 USD | 13,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 5,970,000.00 USD | 5,970,000.00 USD | 205,690.00 USD | 63,110.00 USD | 94,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,850,000.00 USD | 1,850,000.00 USD | 27,860.00 USD | 3,010.00 USD | 9,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,360,000.00 USD | 6,360,000.00 USD | 197,680.00 USD | 69,880.00 USD | 118,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,870,000.00 USD | 1,870,000.00 USD | 1,670.00 USD | 8,100.00 USD | 8,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,640,000.00 USD | 6,640,000.00 USD | 131,720.00 USD | 83,000.00 USD | 65,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,880,000.00 USD | 1,880,000.00 USD | 4,600.00 USD | 2,860.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,880,000.00 USD | 6,880,000.00 USD | 102,750.00 USD | 49,310.00 USD | 92,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,900,000.00 USD | 1,900,000.00 USD | 7,180.00 USD | 1,270.00 USD | 7,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,060,000.00 USD | 7,060,000.00 USD | 77,660.00 USD | 32,860.00 USD | 61,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,920,000.00 USD | 1,920,000.00 USD | 13,480.00 USD | 4,390.00 USD | 6,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,400,000.00 USD | 7,400,000.00 USD | 221,410.00 USD | 30,180.00 USD | 93,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,940,000.00 USD | 1,940,000.00 USD | 6,330.00 USD | 4,110.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,600,000.00 USD | 7,600,000.00 USD | 121,300.00 USD | 33,170.00 USD | 42,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,960,000.00 USD | 1,960,000.00 USD | 16,300.00 USD | 3,170.00 USD | 4,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,820,000.00 USD | 7,820,000.00 USD | 103,500.00 USD | 37,730.00 USD | 83,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,980,000.00 USD | 1,980,000.00 USD | 5,820.00 USD | 4,330.00 USD | 12,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 8,030,000.00 USD | 8,030,000.00 USD | 102,600.00 USD | 21,500.00 USD | 83,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 2,000,000.00 USD | 2,000,000.00 USD | 4,510.00 USD | 5,370.00 USD | 10,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,180,000.00 USD | 8,180,000.00 USD | 103,110.00 USD | 18,720.00 USD | 27,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,020,000.00 USD | 2,020,000.00 USD | 8,270.00 USD | 3,550.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,450,000.00 USD | 8,450,000.00 USD | 158,650.00 USD | 40,740.00 USD | 69,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,030,000.00 USD | 2,030,000.00 USD | 7,590.00 USD | 4,280.00 USD | 36.19 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,690,000.00 USD | 8,690,000.00 USD | 176,790.00 USD | 26,190.00 USD | 33,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,050,000.00 USD | 2,050,000.00 USD | 8,650.00 USD | 2,530.00 USD | 2,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,810,000.00 USD | 8,810,000.00 USD | 62,710.00 USD | 20,510.00 USD | 38,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,050,000.00 USD | 2,050,000.00 USD | 2,300.00 USD | 2,770.00 USD | 2,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,990,000.00 USD | 8,990,000.00 USD | 46,000.00 USD | 31,940.00 USD | 103,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,080,000.00 USD | 2,080,000.00 USD | 17,910.00 USD | 3,990.00 USD | 6,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,190,000.00 USD | 9,190,000.00 USD | 134,170.00 USD | 28,200.00 USD | 34,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,100,000.00 USD | 2,100,000.00 USD | 4,380.00 USD | 3,850.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,420,000.00 USD | 9,420,000.00 USD | 59,850.00 USD | 54,400.00 USD | 117,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,100,000.00 USD | 2,100,000.00 USD | 2,400.00 USD | 1,680.00 USD | 2,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,580,000.00 USD | 9,580,000.00 USD | 109,670.00 USD | 18,350.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,110,000.00 USD | 2,110,000.00 USD | 7,430.00 USD | 2,540.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,700,000.00 USD | 9,700,000.00 USD | 37,360.00 USD | 24,570.00 USD | 62,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 2,440.00 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,860,000.00 USD | 9,860,000.00 USD | 66,620.00 USD | 37,290.00 USD | 55,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,030,000.00 USD | 10,030,000.00 USD | 71,580.00 USD | 30,090.00 USD | 65,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,260,000.00 USD | 10,260,000.00 USD | 114,820.00 USD | 21,050.00 USD | 92,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,540,000.00 USD | 10,540,000.00 USD | 182,190.00 USD | 62,900.00 USD | 41,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,770,000.00 USD | 10,770,000.00 USD | 118,210.00 USD | 18,440.00 USD | 88,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,900,000.00 USD | 10,900,000.00 USD | 51,230.00 USD | 22,070.00 USD | 56,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 10,940,000.00 USD | 10,940,000.00 USD | 22,290.00 USD | 5,830.00 USD | 12,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 11,120,000.00 USD | 11,120,000.00 USD | 90,280.00 USD | 31,510.00 USD | 54,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.11` | 169.86 USD | 76,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.11` | 11,280,000.00 USD | 11,280,000.00 USD | 33,280.00 USD | 36,570.00 USD | 93,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 11,400,000.00 USD | 11,400,000.00 USD | 64,670.00 USD | 26,930.00 USD | 24,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 11,470,000.00 USD | 11,470,000.00 USD | 32,450.00 USD | 36,820.00 USD | 6,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 11,580,000.00 USD | 11,580,000.00 USD | 59,080.00 USD | 33,150.00 USD | 13,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 11,660,000.00 USD | 11,660,000.00 USD | 37,220.00 USD | 17,240.00 USD | 30,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 11,760,000.00 USD | 11,760,000.00 USD | 32,060.00 USD | 41,540.00 USD | 25,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 11,840,000.00 USD | 11,840,000.00 USD | 52,230.00 USD | 16,980.00 USD | 11,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 11,930,000.00 USD | 11,930,000.00 USD | 58,100.00 USD | 5,280.00 USD | 29,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 11,990,000.00 USD | 11,990,000.00 USD | 16,200.00 USD | 5,970.00 USD | 28,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 12,030,000.00 USD | 12,030,000.00 USD | 2,210.00 USD | 13,650.00 USD | 28,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 12,190,000.00 USD | 12,190,000.00 USD | 95,910.00 USD | 18,230.00 USD | 42,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 12,320,000.00 USD | 12,320,000.00 USD | 71,210.00 USD | 0.00 USD | 65,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.18` | 228.59 USD | 76,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 22,180.00 USD | 98,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 11,730.00 USD | 110,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 389.93 USD | 110,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.42` | 4,330.00 USD | 115,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 513,610.00 USD | 628,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 225.19 USD | 629,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 960.68 USD | 630,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 232.49 USD | 630,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 176.31 USD | 630,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 9,590.00 USD | 640,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 762.12 USD | 640,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 242.35 USD | 641,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 300.15 USD | 641,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 320.38 USD | 641,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 88,800.00 USD | 730,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 208.37 USD | 730,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 181.88 USD | 730,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2345` | 530,390.00 USD | 0.00 USD | 117.25 USD | `-76.18%` | `500.00` |
| `Live` | `Long` | `0.3265` | 530,270.00 USD | 0.00 USD | 589.56 USD | `-66.84%` | `1,805.70` |
| `Live` | `Long` | `0.3355` | 529,680.00 USD | 0.00 USD | 741.12 USD | `-65.92%` | `2,209.00` |
| `Live` | `Long` | `0.3775` | 528,940.00 USD | 0.00 USD | 2,150.00 USD | `-61.66%` | `5,698.80` |
| `Live` | `Long` | `0.4025` | 526,790.00 USD | 0.00 USD | 128.52 USD | `-59.12%` | `319.30` |
| `Live` | `Long` | `0.4185` | 526,660.00 USD | 0.00 USD | 2,790.00 USD | `-57.49%` | `6,675.20` |
| `Live` | `Long` | `0.4505` | 523,860.00 USD | 0.00 USD | 178.62 USD | `-54.24%` | `396.50` |
| `Live` | `Long` | `0.4695` | 523,690.00 USD | 0.00 USD | 2,580.00 USD | `-52.31%` | `5,500.00` |
| `Live` | `Long` | `0.5005` | 521,100.00 USD | 0.00 USD | 146.30 USD | `-49.16%` | `292.30` |
| `Live` | `Long` | `0.5025` | 520,960.00 USD | 0.00 USD | 201.35 USD | `-48.96%` | `400.70` |
| `Live` | `Long` | `0.5035` | 520,760.00 USD | 0.00 USD | 996.88 USD | `-48.86%` | `1,979.90` |
| `Live` | `Long` | `0.5115` | 519,760.00 USD | 0.00 USD | 606.38 USD | `-48.04%` | `1,185.50` |
| `Live` | `Long` | `0.5125` | 519,150.00 USD | 0.00 USD | 4,130.00 USD | `-47.94%` | `8,067.10` |
| `Live` | `Long` | `0.5215` | 515,020.00 USD | 0.00 USD | 12,720.00 USD | `-47.03%` | `24,390.20` |
| `Live` | `Long` | `0.5465` | 502,300.00 USD | 0.00 USD | 106.84 USD | `-44.49%` | `195.50` |
| `Live` | `Long` | `0.5695` | 502,190.00 USD | 0.00 USD | 577.36 USD | `-42.15%` | `1,013.80` |
| `Live` | `Long` | `0.5895` | 501,610.00 USD | 0.00 USD | 137.53 USD | `-40.12%` | `233.30` |
| `Live` | `Long` | `0.5955` | 501,480.00 USD | 0.00 USD | 3,390.00 USD | `-39.51%` | `5,695.60` |
| `Live` | `Long` | `0.6055` | 498,080.00 USD | 0.00 USD | 1,480.00 USD | `-38.50%` | `2,448.50` |
| `Live` | `Long` | `0.6065` | 496,600.00 USD | 0.00 USD | 1,800.00 USD | `-38.39%` | `2,971.80` |
| `Live` | `Long` | `0.6125` | 494,800.00 USD | 0.00 USD | 105.96 USD | `-37.79%` | `173.00` |
| `Live` | `Long` | `0.6145` | 494,690.00 USD | 0.00 USD | 147.48 USD | `-37.58%` | `240.00` |
| `Live` | `Long` | `0.6245` | 494,550.00 USD | 0.00 USD | 525.77 USD | `-36.57%` | `841.90` |
| `Live` | `Long` | `0.6305` | 494,020.00 USD | 0.00 USD | 154.22 USD | `-35.96%` | `244.60` |
| `Live` | `Long` | `0.6315` | 493,870.00 USD | 0.00 USD | 757.80 USD | `-35.86%` | `1,200.00` |
| `Live` | `Long` | `0.6355` | 493,110.00 USD | 0.00 USD | 106.00 USD | `-35.45%` | `166.80` |
| `Live` | `Long` | `0.6415` | 493,000.00 USD | 0.00 USD | 20,270.00 USD | `-34.84%` | `31,595.60` |
| `Live` | `Long` | `0.6465` | 472,730.00 USD | 0.00 USD | 4,230.00 USD | `-34.33%` | `6,539.70` |
| `Live` | `Long` | `0.6475` | 468,510.00 USD | 0.00 USD | 202.47 USD | `-34.23%` | `312.70` |
| `Live` | `Long` | `0.6595` | 468,300.00 USD | 0.00 USD | 149.44 USD | `-33.01%` | `226.60` |
| `Live` | `Long` | `0.6725` | 468,150.00 USD | 0.00 USD | 63,890.00 USD | `-31.69%` | `95,000.00` |
| `Live` | `Long` | `0.6775` | 404,270.00 USD | 0.00 USD | 423.10 USD | `-31.18%` | `624.50` |
| `Live` | `Long` | `0.6835` | 403,840.00 USD | 0.00 USD | 512.97 USD | `-30.57%` | `750.50` |
| `Live` | `Long` | `0.6855` | 403,330.00 USD | 0.00 USD | 2,110.00 USD | `-30.37%` | `3,075.70` |
| `Live` | `Long` | `0.6955` | 401,220.00 USD | 0.00 USD | 322.16 USD | `-29.35%` | `463.20` |
| `Live` | `Long` | `0.6965` | 400,900.00 USD | 0.00 USD | 155.60 USD | `-29.25%` | `223.40` |
| `Live` | `Long` | `0.7025` | 400,740.00 USD | 0.00 USD | 702.50 USD | `-28.64%` | `1,000.00` |
| `Live` | `Long` | `0.7055` | 400,040.00 USD | 0.00 USD | 176.38 USD | `-28.34%` | `250.00` |
| `Live` | `Long` | `0.7075` | 399,870.00 USD | 0.00 USD | 16,520.00 USD | `-28.14%` | `23,344.30` |
| `Live` | `Long` | `0.7145` | 383,350.00 USD | 0.00 USD | 988.87 USD | `-27.42%` | `1,384.00` |
| `Live` | `Long` | `0.7175` | 382,360.00 USD | 0.00 USD | 322.88 USD | `-27.12%` | `450.00` |
| `Live` | `Long` | `0.7205` | 382,040.00 USD | 0.00 USD | 866.26 USD | `-26.81%` | `1,202.30` |
| `Live` | `Long` | `0.7255` | 381,170.00 USD | 0.00 USD | 1,090.00 USD | `-26.31%` | `1,500.00` |
| `Live` | `Long` | `0.7275` | 380,080.00 USD | 0.00 USD | 126.44 USD | `-26.10%` | `173.80` |
| `Live` | `Long` | `0.7285` | 379,960.00 USD | 0.00 USD | 291.18 USD | `-26.00%` | `399.70` |
| `Live` | `Long` | `0.7305` | 379,670.00 USD | 0.00 USD | 2,300.00 USD | `-25.80%` | `3,143.00` |
| `Live` | `Long` | `0.7335` | 377,370.00 USD | 0.00 USD | 1,140.00 USD | `-25.49%` | `1,557.80` |
| `Live` | `Long` | `0.7375` | 376,230.00 USD | 0.00 USD | 2,050.00 USD | `-25.09%` | `2,785.30` |
| `Live` | `Long` | `0.7395` | 374,170.00 USD | 0.00 USD | 283.30 USD | `-24.88%` | `383.10` |
| `Live` | `Long` | `0.7455` | 373,890.00 USD | 0.00 USD | 1,390.00 USD | `-24.28%` | `1,859.90` |
| `Live` | `Long` | `0.7525` | 372,500.00 USD | 0.00 USD | 331.18 USD | `-23.56%` | `440.10` |
| `Live` | `Long` | `0.7555` | 372,170.00 USD | 0.00 USD | 2,390.00 USD | `-23.26%` | `3,161.00` |
| `Live` | `Long` | `0.7605` | 369,780.00 USD | 0.00 USD | 3,120.00 USD | `-22.75%` | `4,101.70` |
| `Live` | `Long` | `0.7725` | 366,660.00 USD | 0.00 USD | 1,580.00 USD | `-21.53%` | `2,046.10` |
| `Live` | `Long` | `0.7865` | 365,080.00 USD | 0.00 USD | 292.03 USD | `-20.11%` | `371.30` |
| `Live` | `Long` | `0.7895` | 364,790.00 USD | 0.00 USD | 20,380.00 USD | `-19.81%` | `25,816.60` |
| `Live` | `Long` | `0.7965` | 344,410.00 USD | 0.00 USD | 106.49 USD | `-19.10%` | `133.70` |
| `Live` | `Long` | `0.8025` | 344,300.00 USD | 0.00 USD | 238.90 USD | `-18.49%` | `297.70` |
| `Live` | `Long` | `0.8045` | 344,060.00 USD | 0.00 USD | 566.61 USD | `-18.28%` | `704.30` |
| `Live` | `Long` | `0.8055` | 343,500.00 USD | 0.00 USD | 699.01 USD | `-18.18%` | `867.80` |
| `Live` | `Long` | `0.8115` | 342,800.00 USD | 0.00 USD | 13,430.00 USD | `-17.57%` | `16,544.60` |
| `Live` | `Long` | `0.8135` | 329,370.00 USD | 0.00 USD | 647.79 USD | `-17.37%` | `796.30` |
| `Live` | `Long` | `0.8215` | 328,720.00 USD | 0.00 USD | 1,950.00 USD | `-16.56%` | `2,370.70` |
| `Live` | `Long` | `0.8285` | 326,780.00 USD | 0.00 USD | 1,890.00 USD | `-15.84%` | `2,283.30` |
| `Live` | `Long` | `0.8365` | 324,890.00 USD | 0.00 USD | 316.70 USD | `-15.03%` | `378.60` |
| `Live` | `Long` | `0.8375` | 324,570.00 USD | 0.00 USD | 167.00 USD | `-14.93%` | `199.40` |
| `Live` | `Long` | `0.8415` | 324,400.00 USD | 0.00 USD | 1,240.00 USD | `-14.52%` | `1,469.60` |
| `Live` | `Long` | `0.8445` | 323,170.00 USD | 0.00 USD | 168.31 USD | `-14.22%` | `199.30` |
| `Live` | `Long` | `0.8495` | 323,000.00 USD | 0.00 USD | 1,260.00 USD | `-13.71%` | `1,486.90` |
| `Live` | `Long` | `0.8575` | 321,730.00 USD | 0.00 USD | 620.32 USD | `-12.90%` | `723.40` |
| `Live` | `Long` | `0.8595` | 321,110.00 USD | 0.00 USD | 171.38 USD | `-12.70%` | `199.40` |
| `Live` | `Long` | `0.8605` | 320,940.00 USD | 0.00 USD | 61,100.00 USD | `-12.59%` | `71,003.30` |
| `Live` | `Long` | `0.8625` | 259,840.00 USD | 0.00 USD | 309.55 USD | `-12.39%` | `358.90` |
| `Live` | `Long` | `0.8635` | 259,530.00 USD | 0.00 USD | 208.02 USD | `-12.29%` | `240.90` |
| `Live` | `Long` | `0.8645` | 259,330.00 USD | 0.00 USD | 438.30 USD | `-12.19%` | `507.00` |
| `Live` | `Long` | `0.8665` | 258,890.00 USD | 0.00 USD | 118.54 USD | `-11.98%` | `136.80` |
| `Live` | `Long` | `0.8765` | 258,770.00 USD | 0.00 USD | 171.88 USD | `-10.97%` | `196.10` |
| `Live` | `Long` | `0.8795` | 258,600.00 USD | 0.00 USD | 948.01 USD | `-10.66%` | `1,077.90` |
| `Live` | `Long` | `0.8925` | 257,650.00 USD | 0.00 USD | 526.84 USD | `-9.34%` | `590.30` |
| `Live` | `Long` | `0.8985` | 257,120.00 USD | 0.00 USD | 9,220.00 USD | `-8.73%` | `10,267.00` |
| `Live` | `Long` | `0.8995` | 247,900.00 USD | 0.00 USD | 3,820.00 USD | `-8.63%` | `4,250.30` |
| `Live` | `Long` | `0.9035` | 244,070.00 USD | 0.00 USD | 180.16 USD | `-8.23%` | `199.40` |
| `Live` | `Long` | `0.9055` | 243,890.00 USD | 0.00 USD | 674.42 USD | `-8.02%` | `744.80` |
| `Live` | `Long` | `0.9095` | 243,220.00 USD | 0.00 USD | 951.34 USD | `-7.62%` | `1,046.00` |
| `Live` | `Long` | `0.9135` | 242,270.00 USD | 0.00 USD | 143.42 USD | `-7.21%` | `157.00` |
| `Live` | `Long` | `0.9185` | 242,130.00 USD | 0.00 USD | 145.86 USD | `-6.70%` | `158.80` |
| `Live` | `Long` | `0.9195` | 241,980.00 USD | 0.00 USD | 7,330.00 USD | `-6.60%` | `7,970.50` |
| `Live` | `Long` | `0.9225` | 234,650.00 USD | 0.00 USD | 8,360.00 USD | `-6.30%` | `9,060.10` |
| `Live` | `Long` | `0.9295` | 226,290.00 USD | 0.00 USD | 253.01 USD | `-5.59%` | `272.20` |
| `Live` | `Long` | `0.9335` | 226,040.00 USD | 0.00 USD | 361.45 USD | `-5.18%` | `387.20` |
| `Live` | `Long` | `0.9365` | 225,680.00 USD | 0.00 USD | 6,560.00 USD | `-4.87%` | `7,000.00` |
| `Live` | `Long` | `0.9375` | 219,120.00 USD | 0.00 USD | 196.97 USD | `-4.77%` | `210.10` |
| `Live` | `Long` | `0.9405` | 218,930.00 USD | 0.00 USD | 141.83 USD | `-4.47%` | `150.80` |
| `Live` | `Long` | `0.9445` | 218,780.00 USD | 0.00 USD | 1,060.00 USD | `-4.06%` | `1,117.80` |
| `Live` | `Long` | `0.9455` | 217,730.00 USD | 0.00 USD | 106,880.00 USD | `-3.96%` | `113,040.20` |
| `Live` | `Long` | `0.9475` | 110,850.00 USD | 0.00 USD | 323.19 USD | `-3.76%` | `341.10` |
| `Live` | `Long` | `0.9495` | 110,530.00 USD | 0.00 USD | 105,430.00 USD | `-3.55%` | `111,034.60` |
| `Live` | `Long` | `0.9515` | 5,100.00 USD | 0.00 USD | 405.62 USD | `-3.35%` | `426.30` |
| `Live` | `Long` | `0.9555` | 4,690.00 USD | 0.00 USD | 3,160.00 USD | `-2.94%` | `3,305.70` |
| `Live` | `Long` | `0.9585` | 1,530.00 USD | 0.00 USD | 1,530.00 USD | `-2.64%` | `1,600.00` |
| `Live` | `Short` | `1.04` | 210.51 USD | 210.51 USD | 0.00 USD | `+5.38%` | `202.90` |
| `Live` | `Short` | `1.04` | 422.54 USD | 212.03 USD | 0.00 USD | `+6.10%` | `203.00` |
| `Live` | `Short` | `1.05` | 847.21 USD | 424.67 USD | 0.00 USD | `+6.30%` | `405.80` |
| `Live` | `Short` | `1.05` | 1,580.00 USD | 733.98 USD | 0.00 USD | `+6.40%` | `700.70` |
| `Live` | `Short` | `1.05` | 1,790.00 USD | 213.55 USD | 0.00 USD | `+6.91%` | `202.90` |
| `Live` | `Short` | `1.05` | 2,010.00 USD | 213.76 USD | 0.00 USD | `+7.01%` | `202.90` |
| `Live` | `Short` | `1.06` | 76,420.00 USD | 74,410.00 USD | 0.00 USD | `+7.21%` | `70,500.00` |
| `Live` | `Short` | `1.06` | 76,640.00 USD | 214.97 USD | 0.00 USD | `+7.62%` | `202.90` |
| `Live` | `Short` | `1.06` | 77,070.00 USD | 431.57 USD | 0.00 USD | `+8.03%` | `405.80` |
| `Live` | `Short` | `1.07` | 77,280.00 USD | 216.89 USD | 0.00 USD | `+8.63%` | `202.80` |
| `Live` | `Short` | `1.07` | 77,500.00 USD | 217.20 USD | 0.00 USD | `+8.74%` | `202.90` |
| `Live` | `Short` | `1.07` | 77,940.00 USD | 436.03 USD | 0.00 USD | `+9.14%` | `405.80` |
| `Live` | `Short` | `1.09` | 78,160.00 USD | 221.37 USD | 0.00 USD | `+10.77%` | `203.00` |
| `Live` | `Short` | `1.11` | 78,330.00 USD | 169.86 USD | 0.00 USD | `+12.70%` | `153.10` |
| `Live` | `Short` | `1.12` | 78,850.00 USD | 518.90 USD | 0.00 USD | `+13.82%` | `463.10` |
| `Live` | `Short` | `1.15` | 79,080.00 USD | 232.94 USD | 0.00 USD | `+16.56%` | `203.00` |
| `Live` | `Short` | `1.17` | 81,970.00 USD | 2,890.00 USD | 0.00 USD | `+18.89%` | `2,466.50` |
| `Live` | `Short` | `1.18` | 82,200.00 USD | 228.59 USD | 0.00 USD | `+19.50%` | `194.30` |
| `Live` | `Short` | `1.19` | 104,380.00 USD | 22,180.00 USD | 0.00 USD | `+20.72%` | `18,664.00` |
| `Live` | `Short` | `1.32` | 116,110.00 USD | 11,730.00 USD | 0.00 USD | `+34.44%` | `8,862.90` |
| `Live` | `Short` | `1.34` | 116,500.00 USD | 389.93 USD | 0.00 USD | `+36.06%` | `291.10` |
| `Live` | `Short` | `1.42` | 120,830.00 USD | 4,330.00 USD | 0.00 USD | `+44.29%` | `3,049.30` |
| `Live` | `Short` | `1.49` | 634,440.00 USD | 513,610.00 USD | 0.00 USD | `+51.20%` | `345,051.20` |
| `Live` | `Short` | `1.52` | 634,670.00 USD | 232.49 USD | 0.00 USD | `+54.85%` | `152.50` |
| `Live` | `Short` | `1.54` | 634,850.00 USD | 176.31 USD | 0.00 USD | `+56.68%` | `114.30` |
| `Live` | `Short` | `1.56` | 644,440.00 USD | 9,590.00 USD | 0.00 USD | `+58.10%` | `6,161.90` |
| `Live` | `Short` | `1.64` | 645,200.00 USD | 759.80 USD | 0.00 USD | `+66.33%` | `464.00` |
| `Live` | `Short` | `1.64` | 645,440.00 USD | 240.30 USD | 0.00 USD | `+66.84%` | `146.30` |
| `Live` | `Short` | `1.66` | 645,760.00 USD | 318.46 USD | 0.00 USD | `+68.56%` | `191.90` |
| `Live` | `Short` | `1.67` | 646,060.00 USD | 300.15 USD | 0.00 USD | `+69.38%` | `180.00` |
| `Live` | `Short` | `1.78` | 734,650.00 USD | 88,600.00 USD | 0.00 USD | `+80.86%` | `49,759.80` |
| `Live` | `Short` | `1.86` | 734,860.00 USD | 208.37 USD | 0.00 USD | `+88.47%` | `112.30` |
| `Live` | `Short` | `1.90` | 735,050.00 USD | 181.88 USD | 0.00 USD | `+93.04%` | `95.70` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.4015` | 453,120.00 USD | 0.00 USD | 120.45 USD | `-59.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 453,000.00 USD | 0.00 USD | 150.15 USD | `-49.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 452,850.00 USD | 0.00 USD | 781.90 USD | `-28.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 452,070.00 USD | 0.00 USD | 477.38 USD | `-27.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 451,590.00 USD | 0.00 USD | 341.33 USD | `-26.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 451,250.00 USD | 0.00 USD | 972.82 USD | `-26.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 450,280.00 USD | 0.00 USD | 160.20 USD | `-25.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 450,120.00 USD | 0.00 USD | 289.49 USD | `-24.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 449,830.00 USD | 0.00 USD | 14,570.00 USD | `-20.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 435,260.00 USD | 0.00 USD | 274,830.00 USD | `-19.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 160,430.00 USD | 0.00 USD | 405.75 USD | `-17.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 160,020.00 USD | 0.00 USD | 772.84 USD | `-15.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8495` | 159,250.00 USD | 0.00 USD | 3,470.00 USD | `-13.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 155,780.00 USD | 0.00 USD | 9,180.00 USD | `-13.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 146,600.00 USD | 0.00 USD | 341.94 USD | `-13.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 146,260.00 USD | 0.00 USD | 1,150.00 USD | `-13.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 145,110.00 USD | 0.00 USD | 2,020.00 USD | `-12.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 143,090.00 USD | 0.00 USD | 429.25 USD | `-12.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 142,660.00 USD | 0.00 USD | 1,290.00 USD | `-12.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 141,370.00 USD | 0.00 USD | 518.51 USD | `-11.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 140,850.00 USD | 0.00 USD | 223.04 USD | `-9.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 140,630.00 USD | 0.00 USD | 401.86 USD | `-9.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 140,230.00 USD | 0.00 USD | 158.51 USD | `-9.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 140,070.00 USD | 0.00 USD | 498.10 USD | `-9.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 139,570.00 USD | 0.00 USD | 363.40 USD | `-7.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 139,210.00 USD | 0.00 USD | 913.41 USD | `-6.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9275` | 138,300.00 USD | 0.00 USD | 2,120.00 USD | `-5.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9285` | 136,180.00 USD | 0.00 USD | 246.05 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9295` | 135,930.00 USD | 0.00 USD | 776.50 USD | `-5.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9365` | 135,160.00 USD | 0.00 USD | 9,680.00 USD | `-4.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9405` | 125,470.00 USD | 0.00 USD | 555.18 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9425` | 124,920.00 USD | 0.00 USD | 145.43 USD | `-4.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9445` | 124,770.00 USD | 0.00 USD | 1,730.00 USD | `-4.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9485` | 123,040.00 USD | 0.00 USD | 634.74 USD | `-3.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9525` | 122,410.00 USD | 0.00 USD | 381.00 USD | `-3.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9555` | 122,030.00 USD | 0.00 USD | 3,900.00 USD | `-2.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9565` | 118,130.00 USD | 0.00 USD | 674.91 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9575` | 117,460.00 USD | 0.00 USD | 166.41 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9605` | 117,290.00 USD | 0.00 USD | 376.80 USD | `-2.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9625` | 116,910.00 USD | 0.00 USD | 1,910.00 USD | `-2.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9635` | 115,010.00 USD | 0.00 USD | 568.75 USD | `-2.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9645` | 114,440.00 USD | 0.00 USD | 163.29 USD | `-2.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9665` | 114,280.00 USD | 0.00 USD | 554.58 USD | `-1.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9675` | 113,720.00 USD | 0.00 USD | 385.74 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9685` | 113,330.00 USD | 0.00 USD | 153.22 USD | `-1.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9695` | 113,180.00 USD | 0.00 USD | 22,800.00 USD | `-1.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9705` | 90,380.00 USD | 0.00 USD | 11,230.00 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9715` | 79,150.00 USD | 0.00 USD | 10,370.00 USD | `-1.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9725` | 68,780.00 USD | 0.00 USD | 387.83 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9735` | 68,400.00 USD | 0.00 USD | 7,630.00 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9745` | 60,760.00 USD | 0.00 USD | 8,750.00 USD | `-1.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9755` | 52,020.00 USD | 0.00 USD | 21,960.00 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9765` | 30,050.00 USD | 0.00 USD | 9,500.00 USD | `-0.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9775` | 20,550.00 USD | 0.00 USD | 676.53 USD | `-0.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9785` | 19,880.00 USD | 0.00 USD | 11,400.00 USD | `-0.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9795` | 8,480.00 USD | 0.00 USD | 123.61 USD | `-0.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9805` | 8,350.00 USD | 0.00 USD | 8,350.00 USD | `-0.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 22,170.00 USD | 22,170.00 USD | 0.00 USD | `+0.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 37,240.00 USD | 15,070.00 USD | 0.00 USD | `+0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9865` | 70,030.00 USD | 32,800.00 USD | 0.00 USD | `+0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9895` | 105,010.00 USD | 34,970.00 USD | 0.00 USD | `+0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 108,520.00 USD | 3,520.00 USD | 0.00 USD | `+0.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 140,280.00 USD | 31,750.00 USD | 0.00 USD | `+0.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 141,600.00 USD | 1,320.00 USD | 0.00 USD | `+0.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 142,380.00 USD | 782.07 USD | 0.00 USD | `+1.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 142,790.00 USD | 403.28 USD | 0.00 USD | `+1.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 146,190.00 USD | 3,400.00 USD | 0.00 USD | `+1.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 151,330.00 USD | 5,140.00 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 188,640.00 USD | 37,310.00 USD | 0.00 USD | `+1.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 189,640.00 USD | 1,000.00 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 230,240.00 USD | 40,590.00 USD | 0.00 USD | `+1.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 230,470.00 USD | 235.79 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 231,810.00 USD | 1,340.00 USD | 0.00 USD | `+1.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 232,040.00 USD | 230.39 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 233,050.00 USD | 1,000.00 USD | 0.00 USD | `+2.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 233,240.00 USD | 198.46 USD | 0.00 USD | `+2.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 233,860.00 USD | 615.60 USD | 0.00 USD | `+2.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 237,320.00 USD | 3,460.00 USD | 0.00 USD | `+2.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 237,880.00 USD | 561.17 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 237,980.00 USD | 103.07 USD | 0.00 USD | `+3.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 238,380.00 USD | 401.26 USD | 0.00 USD | `+3.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 239,190.00 USD | 804.09 USD | 0.00 USD | `+3.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 239,390.00 USD | 201.52 USD | 0.00 USD | `+4.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 239,590.00 USD | 201.92 USD | 0.00 USD | `+4.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 239,790.00 USD | 201.60 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 239,890.00 USD | 101.51 USD | 0.00 USD | `+4.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 240,100.00 USD | 202.90 USD | 0.00 USD | `+4.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 240,610.00 USD | 516.75 USD | 0.00 USD | `+4.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 240,820.00 USD | 204.93 USD | 0.00 USD | `+5.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 241,170.00 USD | 348.86 USD | 0.00 USD | `+5.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 241,580.00 USD | 413.76 USD | 0.00 USD | `+5.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 241,940.00 USD | 354.91 USD | 0.00 USD | `+5.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 243,840.00 USD | 1,900.00 USD | 0.00 USD | `+5.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 244,050.00 USD | 207.87 USD | 0.00 USD | `+5.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 244,260.00 USD | 207.97 USD | 0.00 USD | `+5.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 245,550.00 USD | 1,290.00 USD | 0.00 USD | `+6.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 245,760.00 USD | 206.97 USD | 0.00 USD | `+6.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 245,860.00 USD | 107.99 USD | 0.00 USD | `+6.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 246,110.00 USD | 247.60 USD | 0.00 USD | `+7.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 320,950.00 USD | 74,840.00 USD | 0.00 USD | `+7.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 321,490.00 USD | 544.88 USD | 0.00 USD | `+8.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 321,650.00 USD | 157.10 USD | 0.00 USD | `+9.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 323,820.00 USD | 2,170.00 USD | 0.00 USD | `+10.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 325,360.00 USD | 1,540.00 USD | 0.00 USD | `+10.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 335,280.00 USD | 9,930.00 USD | 0.00 USD | `+11.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 336,260.00 USD | 976.36 USD | 0.00 USD | `+11.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 337,140.00 USD | 877.63 USD | 0.00 USD | `+12.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 337,310.00 USD | 171.50 USD | 0.00 USD | `+12.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 337,480.00 USD | 171.09 USD | 0.00 USD | `+13.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 340,250.00 USD | 2,770.00 USD | 0.00 USD | `+14.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 342,290.00 USD | 2,040.00 USD | 0.00 USD | `+14.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 344,960.00 USD | 2,670.00 USD | 0.00 USD | `+15.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 345,110.00 USD | 151.16 USD | 0.00 USD | `+16.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 345,260.00 USD | 151.29 USD | 0.00 USD | `+16.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 345,410.00 USD | 151.42 USD | 0.00 USD | `+16.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 345,560.00 USD | 151.55 USD | 0.00 USD | `+17.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 345,710.00 USD | 151.69 USD | 0.00 USD | `+17.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 347,760.00 USD | 2,050.00 USD | 0.00 USD | `+18.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 347,870.00 USD | 110.00 USD | 0.00 USD | `+19.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 348,110.00 USD | 237.90 USD | 0.00 USD | `+20.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 349,320.00 USD | 1,210.00 USD | 0.00 USD | `+21.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 392,240.00 USD | 42,930.00 USD | 0.00 USD | `+22.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 394,250.00 USD | 2,000.00 USD | 0.00 USD | `+25.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 395,630.00 USD | 1,380.00 USD | 0.00 USD | `+27.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 395,880.00 USD | 245.41 USD | 0.00 USD | `+29.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 403,230.00 USD | 7,350.00 USD | 0.00 USD | `+31.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 403,640.00 USD | 415.25 USD | 0.00 USD | `+32.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 410,160.00 USD | 6,520.00 USD | 0.00 USD | `+32.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 867,150.00 USD | 456,990.00 USD | 0.00 USD | `+33.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 867,800.00 USD | 655.75 USD | 0.00 USD | `+33.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 869,620.00 USD | 1,810.00 USD | 0.00 USD | `+36.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 883,500.00 USD | 13,880.00 USD | 0.00 USD | `+36.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 884,750.00 USD | 1,250.00 USD | 0.00 USD | `+37.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 886,820.00 USD | 2,070.00 USD | 0.00 USD | `+41.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 886,960.00 USD | 140.05 USD | 0.00 USD | `+42.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 887,120.00 USD | 160.42 USD | 0.00 USD | `+42.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 887,720.00 USD | 598.33 USD | 0.00 USD | `+43.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 921,890.00 USD | 34,170.00 USD | 0.00 USD | `+45.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 922,770.00 USD | 879.84 USD | 0.00 USD | `+51.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 923,360.00 USD | 590.88 USD | 0.00 USD | `+52.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 926,420.00 USD | 3,050.00 USD | 0.00 USD | `+53.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 926,710.00 USD | 297.27 USD | 0.00 USD | `+57.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 935,240.00 USD | 8,530.00 USD | 0.00 USD | `+67.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 935,390.00 USD | 143.99 USD | 0.00 USD | `+69.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 935,560.00 USD | 177.05 USD | 0.00 USD | `+79.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 936,000.00 USD | 431.40 USD | 0.00 USD | `+82.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 941,100.00 USD | 5,100.00 USD | 0.00 USD | `+93.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 943,580.00 USD | 2,480.00 USD | 0.00 USD | `+94.06%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.8760` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 6,030.00 USD | 6,200.00 USD | 5,860.00 USD |
| `7D` | `0.8780` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 15,500.00 USD | 50.60 USD | 5,490.00 USD |
| `1D` | `0.8790` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 17,770.00 USD | 8,500.00 USD | 7,060.00 USD |
| `7D` | `0.8800` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 0.00 USD | 3,930.00 USD | 0.00 USD |
| `1D` | `0.8810` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 6,240.00 USD | 3,320.00 USD | 5,560.00 USD |
| `7D` | `0.8820` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 8,660.00 USD | 3,420.00 USD | 0.00 USD |
| `1D` | `0.8830` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 6,600.00 USD | 4,200.00 USD | 36.19 USD |
| `7D` | `0.8840` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 4,540.00 USD | 5,480.00 USD | 1,300.00 USD |
| `1D` | `0.8850` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 7,980.00 USD | 2,370.00 USD | 2,160.00 USD |
| `7D` | `0.8860` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 15,460.00 USD | 7,970.00 USD | 2,570.00 USD |
| `1D` | `0.8870` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 19,160.00 USD | 4,450.00 USD | 9,500.00 USD |
| `7D` | `0.8880` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 7,150.00 USD | 1,990.00 USD | 11,620.00 USD |
| `1D` | `0.8890` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 3,730.00 USD | 3,680.00 USD | 6,690.00 USD |
| `7D` | `0.8900` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 23,060.00 USD | 6,420.00 USD | 20,580.00 USD |
| `1D` | `0.8910` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 1,820.00 USD | 1,560.00 USD | 2,270.00 USD |
| `7D` | `0.8920` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 45,890.00 USD | 9,570.00 USD | 15,680.00 USD |
| `1D` | `0.8930` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 7,320.00 USD | 2,470.00 USD | 1,890.00 USD |
| `7D` | `0.8940` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 7,120.00 USD | 8,030.00 USD | 26,540.00 USD |
| `1D` | `0.8950` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 22.75 USD | 2,460.00 USD | 2,100.00 USD |
| `7D` | `0.8960` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 30,390.00 USD | 9,210.00 USD | 12,150.00 USD |
| `1D` | `0.8970` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 5,360.00 USD | 3,690.00 USD | 1,060.00 USD |
| `7D` | `0.8980` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 31,140.00 USD | 6,910.00 USD | 36,260.00 USD |
| `1D` | `0.8990` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 5,550.00 USD | 757.19 USD | 1,240.00 USD |
| `7D` | `0.9000` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 39,940.00 USD | 14,050.00 USD | 14,850.00 USD |
| `1D` | `0.9010` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 15.65 USD | 39.59 USD | 1,890.00 USD |
| `7D` | `0.9020` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 16,980.00 USD | 11,760.00 USD | 15,220.00 USD |
| `1D` | `0.9030` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 6,430.00 USD | 3,760.00 USD | 4,220.00 USD |
| `7D` | `0.9040` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 17,160.00 USD | 5,930.00 USD | 11,110.00 USD |
| `1D` | `0.9050` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 8,300.00 USD | 3,640.00 USD | 3,200.00 USD |
| `7D` | `0.9060` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 53,450.00 USD | 30,600.00 USD | 41,510.00 USD |
| `1D` | `0.9070` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 3,810.00 USD | 488.01 USD | 803.91 USD |
| `7D` | `0.9080` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 21,830.00 USD | 3,470.00 USD | 6,850.00 USD |
| `1D` | `0.9090` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 18,830.00 USD | 4,030.00 USD | 4,140.00 USD |
| `7D` | `0.9100` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 6,870.00 USD | 10,340.00 USD | 17,140.00 USD |
| `1D` | `0.9110` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 9,060.00 USD | 791.28 USD | 5,530.00 USD |
| `7D` | `0.9120` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 21,820.00 USD | 4,010.00 USD | 371.71 USD |
| `1D` | `0.9130` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 4,710.00 USD | 487.57 USD | 2,400.00 USD |
| `7D` | `0.9140` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 46,660.00 USD | 8,800.00 USD | 26,510.00 USD |
| `1D` | `0.9150` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 14,250.00 USD | 1,040.00 USD | 8,050.00 USD |
| `7D` | `0.9160` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 12,570.00 USD | 12,620.00 USD | 17,320.00 USD |
| `1D` | `0.9170` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 3,560.00 USD | 435.13 USD | 452.67 USD |
| `7D` | `0.9180` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 29,970.00 USD | 9,010.00 USD | 11,540.00 USD |
| `1D` | `0.9190` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 2,850.00 USD | 147.28 USD | 54.94 USD |
| `7D` | `0.9200` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 40,100.00 USD | 4,910.00 USD | 22,830.00 USD |
| `1D` | `0.9210` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 1,470.00 USD | 77.80 USD | 2,330.00 USD |
| `7D` | `0.9220` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 15,960.00 USD | 2,370.00 USD | 15,640.00 USD |
| `1D` | `0.9230` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 10,650.00 USD | 989.17 USD | 907.53 USD |
| `7D` | `0.9240` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 56,450.00 USD | 17,850.00 USD | 51,900.00 USD |
| `1D` | `0.9250` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 19,800.00 USD | 8,960.00 USD | 14,770.00 USD |
| `7D` | `0.9260` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 32,320.00 USD | 3,140.00 USD | 21,360.00 USD |
| `1D` | `0.9270` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 15,140.00 USD | 5,150.00 USD | 10,980.00 USD |
| `7D` | `0.9280` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 85,040.00 USD | 14,050.00 USD | 26,530.00 USD |
| `1D` | `0.9290` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 25,560.00 USD | 4,250.00 USD | 6,800.00 USD |
| `7D` | `0.9300` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 27,510.00 USD | 12,060.00 USD | 18,410.00 USD |
| `1D` | `0.9310` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 10,710.00 USD | 12,130.00 USD | 21,600.00 USD |
| `7D` | `0.9320` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 29,490.00 USD | 7,900.00 USD | 6,120.00 USD |
| `1D` | `0.9330` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 21,800.00 USD | 9,080.00 USD | 9,250.00 USD |
| `7D` | `0.9340` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 53,710.00 USD | 31,710.00 USD | 24,000.00 USD |
| `1D` | `0.9350` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 36,430.00 USD | 10,940.00 USD | 13,660.00 USD |
| `7D` | `0.9360` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 59,280.00 USD | 6,250.00 USD | 14,950.00 USD |
| `1D` | `0.9370` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 38,680.00 USD | 12,840.00 USD | 20,310.00 USD |
| `7D` | `0.9380` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 20,200.00 USD | 20,670.00 USD | 12,240.00 USD |
| `1D` | `0.9390` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 17,600.00 USD | 14,430.00 USD | 14,430.00 USD |
| `7D` | `0.9400` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 26,270.00 USD | 6,010.00 USD | 7,370.00 USD |
| `1D` | `0.9410` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 45,250.00 USD | 15,190.00 USD | 2,190.00 USD |
| `7D` | `0.9420` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 51,440.00 USD | 21,220.00 USD | 10,090.00 USD |
| `1D` | `0.9430` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 21,430.00 USD | 8,230.00 USD | 3,110.00 USD |
| `7D` | `0.9440` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 57,220.00 USD | 26,910.00 USD | 26,070.00 USD |
| `1D` | `0.9450` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 41,820.00 USD | 22,990.00 USD | 41,780.00 USD |
| `7D` | `0.9460` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 80,430.00 USD | 19,530.00 USD | 44,800.00 USD |
| `1D` | `0.9470` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 82,980.00 USD | 27,830.00 USD | 42,410.00 USD |
| `7D` | `0.9480` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 202,170.00 USD | 42,900.00 USD | 92,480.00 USD |
| `1D` | `0.9490` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 77,380.00 USD | 19,930.00 USD | 28,330.00 USD |
| `7D` | `0.9500` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 125,620.00 USD | 46,290.00 USD | 114,560.00 USD |
| `1D` | `0.9510` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 35,280.00 USD | 33,660.00 USD | 43,040.00 USD |
| `7D` | `0.9520` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 144,770.00 USD | 19,800.00 USD | 57,660.00 USD |
| `1D` | `0.9530` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 55,340.00 USD | 18,390.00 USD | 21,850.00 USD |
| `7D` | `0.9540` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 116,590.00 USD | 92,780.00 USD | 108,960.00 USD |
| `1D` | `0.9550` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 81,780.00 USD | 37,060.00 USD | 36,990.00 USD |
| `7D` | `0.9560` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 207,570.00 USD | 32,950.00 USD | 87,460.00 USD |
| `1D` | `0.9570` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 112,970.00 USD | 38,550.00 USD | 47,580.00 USD |
| `7D` | `0.9580` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 107,300.00 USD | 48,150.00 USD | 119,950.00 USD |
| `1D` | `0.9590` | 955,140.00 USD | 0.00 USD | 955,140.00 USD | 59,310.00 USD | 22,860.00 USD | 31,870.00 USD |
| `7D` | `0.9600` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 222,250.00 USD | 82,170.00 USD | 59,710.00 USD |
| `1D` | `0.9610` | 841,100.00 USD | 0.00 USD | 841,100.00 USD | 62,360.00 USD | 27,360.00 USD | 12,190.00 USD |
| `7D` | `0.9620` | 968,430.00 USD | 0.00 USD | 968,430.00 USD | 140,700.00 USD | 46,240.00 USD | 26,080.00 USD |
| `1D` | `0.9630` | 739,180.00 USD | 0.00 USD | 739,180.00 USD | 43,690.00 USD | 24,730.00 USD | 24,780.00 USD |
| `7D` | `0.9640` | 755,410.00 USD | 0.00 USD | 755,410.00 USD | 104,730.00 USD | 778.20 USD | 6,950.00 USD |
| `1D` | `0.9650` | 645,980.00 USD | 0.00 USD | 645,980.00 USD | 60,870.00 USD | 14,680.00 USD | 31,900.00 USD |
| `7D` | `0.9660` | 642,950.00 USD | 0.00 USD | 642,950.00 USD | 40,050.00 USD | 9,550.00 USD | 31,400.00 USD |
| `1D` | `0.9670` | 538,530.00 USD | 0.00 USD | 538,530.00 USD | 69,000.00 USD | 22,210.00 USD | 39,140.00 USD |
| `7D` | `0.9680` | 561,960.00 USD | 0.00 USD | 561,960.00 USD | 26,480.00 USD | 4,670.00 USD | 36,940.00 USD |
| `1D` | `0.9690` | 408,190.00 USD | 0.00 USD | 408,190.00 USD | 43,730.00 USD | 30,170.00 USD | 31,220.00 USD |
| `7D` | `0.9700` | 493,870.00 USD | 0.00 USD | 493,870.00 USD | 33,960.00 USD | 25,160.00 USD | 36,880.00 USD |
| `1D` | `0.9710` | 303,060.00 USD | 0.00 USD | 303,060.00 USD | 60,380.00 USD | 19,100.00 USD | 21,290.00 USD |
| `7D` | `0.9720` | 397,870.00 USD | 0.00 USD | 397,870.00 USD | 53,850.00 USD | 0.00 USD | 9,610.00 USD |
| `1D` | `0.9730` | 202,280.00 USD | 0.00 USD | 202,280.00 USD | 23,620.00 USD | 691.66 USD | 13,310.00 USD |
| `7D` | `0.9740` | 334,420.00 USD | 0.00 USD | 334,420.00 USD | 0.00 USD | 16,590.00 USD | 8,630.00 USD |
| `1D` | `0.9750` | 164,660.00 USD | 0.00 USD | 164,660.00 USD | 16,060.00 USD | 23,220.00 USD | 15,960.00 USD |
| `7D` | `0.9760` | 309,200.00 USD | 0.00 USD | 309,200.00 USD | 15,320.00 USD | 5,480.00 USD | 9,280.00 USD |
| `1D` | `0.9770` | 109,420.00 USD | 0.00 USD | 109,420.00 USD | 35,620.00 USD | 2,870.00 USD | 9,980.00 USD |
| `7D` | `0.9780` | 279,110.00 USD | 0.00 USD | 279,110.00 USD | 0.00 USD | 0.00 USD | 24,280.00 USD |
| `1D` | `0.9790` | 60,960.00 USD | 0.00 USD | 60,960.00 USD | 819.00 USD | 0.00 USD | 7,800.00 USD |
| `7D` | `0.9800` | 254,830.00 USD | 0.00 USD | 254,830.00 USD | 0.00 USD | 0.00 USD | 151,540.00 USD |
| `1D` | `0.9810` | 52,340.00 USD | 0.00 USD | 52,340.00 USD | 0.00 USD | 376.40 USD | 8,930.00 USD |
| `7D` | `0.9820` | 103,280.00 USD | 0.00 USD | 103,280.00 USD | 10,090.00 USD | 0.00 USD | 72,280.00 USD |
| `1D` | `0.9830` | 43,030.00 USD | 0.00 USD | 43,030.00 USD | 15,980.00 USD | 11,780.00 USD | 15,270.00 USD |
| `7D` | `0.9840` | 20,920.00 USD | 0.00 USD | 20,920.00 USD | 0.00 USD | 0.00 USD | 20,920.00 USD |
| `1D` | `0.9850` | 11,310.00 USD | 11,310.00 USD | 0.00 USD | 575.70 USD | 0.00 USD | 10,740.00 USD |
| `1D` | `0.9850` | 22,620.00 USD | 22,620.00 USD | 0.00 USD | 575.70 USD | 0.00 USD | 10,740.00 USD |
| `7D` | `0.9850` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9860` | 803.95 USD | 803.95 USD | 0.00 USD | 0.00 USD | 0.00 USD | 803.95 USD |
| `7D` | `0.9880` | 41,720.00 USD | 41,720.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 901.60 USD |
| `1D` | `0.9890` | 29,460.00 USD | 29,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,840.00 USD |
| `7D` | `0.9900` | 42,630.00 USD | 42,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 906.61 USD |
| `1D` | `0.9910` | 99,660.00 USD | 99,660.00 USD | 0.00 USD | 50,430.00 USD | 0.00 USD | 19,770.00 USD |
| `7D` | `0.9920` | 63,070.00 USD | 63,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,440.00 USD |
| `1D` | `0.9930` | 120,020.00 USD | 120,020.00 USD | 0.00 USD | 6,920.00 USD | 13,250.00 USD | 191.64 USD |
| `1D` | `0.9950` | 121,650.00 USD | 121,650.00 USD | 0.00 USD | 0.00 USD | 1,630.00 USD | 0.00 USD |
| `7D` | `0.9960` | 138,520.00 USD | 138,520.00 USD | 0.00 USD | 32,670.00 USD | 0.00 USD | 42,770.00 USD |
| `1D` | `0.9970` | 149,870.00 USD | 149,870.00 USD | 0.00 USD | 26,250.00 USD | 1,000.00 USD | 970.29 USD |
| `7D` | `0.9980` | 195,430.00 USD | 195,430.00 USD | 0.00 USD | 52,700.00 USD | 0.00 USD | 4,210.00 USD |
| `1D` | `0.9990` | 165,500.00 USD | 165,500.00 USD | 0.00 USD | 9,720.00 USD | 3,910.00 USD | 2,010.00 USD |
| `7D` | `1.00` | 248,280.00 USD | 248,280.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.00` | 234,400.00 USD | 234,400.00 USD | 0.00 USD | 41,020.00 USD | 27,530.00 USD | 348.39 USD |
| `7D` | `1.00` | 291,850.00 USD | 291,850.00 USD | 0.00 USD | 28,410.00 USD | 13,940.00 USD | 1,220.00 USD |
| `1D` | `1.00` | 252,510.00 USD | 252,510.00 USD | 0.00 USD | 10,110.00 USD | 5,360.00 USD | 2,630.00 USD |
| `7D` | `1.00` | 337,520.00 USD | 337,520.00 USD | 0.00 USD | 44,900.00 USD | 0.00 USD | 775.10 USD |
| `1D` | `1.00` | 290,470.00 USD | 290,470.00 USD | 0.00 USD | 35,550.00 USD | 1,780.00 USD | 633.92 USD |
| `7D` | `1.01` | 371,630.00 USD | 371,630.00 USD | 0.00 USD | 34,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.01` | 374,360.00 USD | 374,360.00 USD | 0.00 USD | 40,210.00 USD | 7,570.00 USD | 36,110.00 USD |
| `7D` | `1.01` | 387,880.00 USD | 387,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,250.00 USD |
| `1D` | `1.01` | 390,920.00 USD | 390,920.00 USD | 0.00 USD | 5,860.00 USD | 10,700.00 USD | 0.00 USD |
| `7D` | `1.01` | 401,900.00 USD | 401,900.00 USD | 0.00 USD | 0.00 USD | 14,020.00 USD | 0.00 USD |
| `1D` | `1.01` | 421,440.00 USD | 421,440.00 USD | 0.00 USD | 7,210.00 USD | 23,150.00 USD | 155.80 USD |
| `7D` | `1.01` | 461,430.00 USD | 461,430.00 USD | 0.00 USD | 33,230.00 USD | 26,300.00 USD | 0.00 USD |
| `1D` | `1.01` | 435,850.00 USD | 435,850.00 USD | 0.00 USD | 10,040.00 USD | 4,020.00 USD | 352.75 USD |
| `7D` | `1.01` | 492,840.00 USD | 492,840.00 USD | 0.00 USD | 2,870.00 USD | 28,140.00 USD | 388.43 USD |
| `1D` | `1.01` | 506,240.00 USD | 506,240.00 USD | 0.00 USD | 25,750.00 USD | 4,350.00 USD | 40,290.00 USD |
| `7D` | `1.02` | 533,220.00 USD | 533,220.00 USD | 0.00 USD | 0.00 USD | 28,470.00 USD | 11,910.00 USD |
| `1D` | `1.02` | 539,510.00 USD | 539,510.00 USD | 0.00 USD | 1,130.00 USD | 7,410.00 USD | 24,720.00 USD |
| `7D` | `1.02` | 575,190.00 USD | 575,190.00 USD | 0.00 USD | 0.00 USD | 20,410.00 USD | 21,560.00 USD |
| `1D` | `1.02` | 593,480.00 USD | 593,480.00 USD | 0.00 USD | 39,370.00 USD | 3,750.00 USD | 10,850.00 USD |
| `7D` | `1.02` | 700,660.00 USD | 700,660.00 USD | 0.00 USD | 0.00 USD | 81,220.00 USD | 44,250.00 USD |
| `1D` | `1.02` | 637,980.00 USD | 637,980.00 USD | 0.00 USD | 27,370.00 USD | 2,230.00 USD | 14,900.00 USD |
| `7D` | `1.02` | 921,600.00 USD | 921,600.00 USD | 0.00 USD | 56,930.00 USD | 52,290.00 USD | 111,720.00 USD |
| `1D` | `1.02` | 738,450.00 USD | 738,450.00 USD | 0.00 USD | 54,050.00 USD | 5,670.00 USD | 40,750.00 USD |
| `7D` | `1.02` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 62,470.00 USD | 56,700.00 USD | 86,740.00 USD |
| `1D` | `1.02` | 876,120.00 USD | 876,120.00 USD | 0.00 USD | 67,790.00 USD | 32,010.00 USD | 37,870.00 USD |
| `7D` | `1.03` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 22,650.00 USD | 124,760.00 USD | 25,070.00 USD |
| `1D` | `1.03` | 926,010.00 USD | 926,010.00 USD | 0.00 USD | 26,670.00 USD | 11,540.00 USD | 11,680.00 USD |
| `7D` | `1.03` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 250,040.00 USD | 50,530.00 USD | 24,480.00 USD |
| `1D` | `1.03` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 30,050.00 USD | 24,640.00 USD | 35,230.00 USD |
| `7D` | `1.03` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 134,200.00 USD | 29,810.00 USD | 19,120.00 USD |
| `1D` | `1.03` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 133,530.00 USD | 17,570.00 USD | 40,480.00 USD |
| `7D` | `1.03` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD |
| `1D` | `1.03` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 38,620.00 USD | 116.64 USD | 23,160.00 USD |
| `7D` | `1.03` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 216,820.00 USD | 8,290.00 USD | 4,310.00 USD |
| `1D` | `1.03` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 27,090.00 USD | 18,490.00 USD | 29,910.00 USD |
| `7D` | `1.04` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 262,550.00 USD | 3,170.00 USD | 42,930.00 USD |
| `1D` | `1.04` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 69,740.00 USD | 7,400.00 USD | 32,590.00 USD |
| `7D` | `1.04` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 178,400.00 USD | 1,290.00 USD | 199,090.00 USD |
| `1D` | `1.04` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 10,510.00 USD | 4,170.00 USD | 7,780.00 USD |
| `7D` | `1.04` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 279,460.00 USD | 9,430.00 USD | 93,080.00 USD |
| `1D` | `1.04` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 4,050.00 USD | 4,370.00 USD | 6,280.00 USD |
| `7D` | `1.04` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD |
| `1D` | `1.04` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 14,730.00 USD | 12,770.00 USD | 24,950.00 USD |
| `7D` | `1.04` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD |
| `1D` | `1.04` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 5,920.00 USD | 6,310.00 USD | 13,170.00 USD |
| `7D` | `1.05` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD |
| `1D` | `1.05` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 29,770.00 USD | 7,370.00 USD | 1,860.00 USD |
| `7D` | `1.05` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 199,320.00 USD | 28,070.00 USD | 161,420.00 USD |
| `1D` | `1.05` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 2,310.00 USD | 8,000.00 USD | 17,750.00 USD |
| `7D` | `1.05` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 91,750.00 USD | 29,070.00 USD | 40,740.00 USD |
| `1D` | `1.05` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 62,570.00 USD | 4,140.00 USD | 17,630.00 USD |
| `7D` | `1.05` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 140,970.00 USD | 49,780.00 USD | 133,760.00 USD |
| `1D` | `1.05` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 5,710.00 USD | 6,220.00 USD | 19,270.00 USD |
| `7D` | `1.05` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 82,020.00 USD | 42,140.00 USD | 36,750.00 USD |
| `1D` | `1.05` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 14,400.00 USD | 979.80 USD | 21,350.00 USD |
| `7D` | `1.06` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 187,610.00 USD | 48,000.00 USD | 121,890.00 USD |
| `1D` | `1.06` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 5,730.00 USD | 2,500.00 USD | 13,800.00 USD |
| `7D` | `1.06` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 205,690.00 USD | 63,110.00 USD | 94,960.00 USD |
| `1D` | `1.06` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 27,860.00 USD | 3,010.00 USD | 9,650.00 USD |
| `7D` | `1.06` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 197,680.00 USD | 69,880.00 USD | 118,850.00 USD |
| `1D` | `1.06` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 1,670.00 USD | 8,100.00 USD | 8,130.00 USD |
| `7D` | `1.06` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 131,720.00 USD | 83,000.00 USD | 65,720.00 USD |
| `1D` | `1.06` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 4,600.00 USD | 2,860.00 USD | 2,590.00 USD |
| `7D` | `1.06` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 102,750.00 USD | 49,310.00 USD | 92,130.00 USD |
| `1D` | `1.06` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 7,180.00 USD | 1,270.00 USD | 7,700.00 USD |
| `7D` | `1.07` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 77,660.00 USD | 32,860.00 USD | 61,900.00 USD |
| `1D` | `1.07` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 13,480.00 USD | 4,390.00 USD | 6,100.00 USD |
| `7D` | `1.07` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 221,410.00 USD | 30,180.00 USD | 93,450.00 USD |
| `1D` | `1.07` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 6,330.00 USD | 4,110.00 USD | 6,120.00 USD |
| `7D` | `1.07` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 121,300.00 USD | 33,170.00 USD | 42,480.00 USD |
| `1D` | `1.07` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 16,300.00 USD | 3,170.00 USD | 4,120.00 USD |
| `7D` | `1.07` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 103,500.00 USD | 37,730.00 USD | 83,520.00 USD |
| `1D` | `1.07` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 5,820.00 USD | 4,330.00 USD | 12,130.00 USD |
| `7D` | `1.07` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 102,600.00 USD | 21,500.00 USD | 83,440.00 USD |
| `1D` | `1.07` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 4,510.00 USD | 5,370.00 USD | 10,130.00 USD |
| `7D` | `1.08` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 103,110.00 USD | 18,720.00 USD | 27,400.00 USD |
| `1D` | `1.08` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 8,270.00 USD | 3,550.00 USD | 5,560.00 USD |
| `7D` | `1.08` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 158,650.00 USD | 40,740.00 USD | 69,670.00 USD |
| `1D` | `1.08` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 7,590.00 USD | 4,280.00 USD | 36.19 USD |
| `7D` | `1.08` | 8,690,000.00 USD | 8,690,000.00 USD | 0.00 USD | 176,790.00 USD | 26,190.00 USD | 33,510.00 USD |
| `1D` | `1.08` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 8,650.00 USD | 2,530.00 USD | 2,570.00 USD |
| `7D` | `1.08` | 8,810,000.00 USD | 8,810,000.00 USD | 0.00 USD | 62,710.00 USD | 20,510.00 USD | 38,630.00 USD |
| `1D` | `1.08` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 2,300.00 USD | 2,770.00 USD | 2,730.00 USD |
| `7D` | `1.08` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 46,000.00 USD | 31,940.00 USD | 103,610.00 USD |
| `1D` | `1.08` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 17,910.00 USD | 3,990.00 USD | 6,770.00 USD |
| `7D` | `1.09` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 134,170.00 USD | 28,200.00 USD | 34,220.00 USD |
| `1D` | `1.09` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 4,380.00 USD | 3,850.00 USD | 6,690.00 USD |
| `7D` | `1.09` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 59,850.00 USD | 54,400.00 USD | 117,570.00 USD |
| `1D` | `1.09` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 2,400.00 USD | 1,680.00 USD | 2,270.00 USD |
| `7D` | `1.09` | 9,580,000.00 USD | 9,580,000.00 USD | 0.00 USD | 109,670.00 USD | 18,350.00 USD | 31,220.00 USD |
| `1D` | `1.09` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 7,430.00 USD | 2,540.00 USD | 1,890.00 USD |
| `7D` | `1.09` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 37,360.00 USD | 24,570.00 USD | 62,450.00 USD |
| `1D` | `1.09` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 2,440.00 USD | 2,090.00 USD |
| `7D` | `1.09` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 66,620.00 USD | 37,290.00 USD | 55,440.00 USD |
| `7D` | `1.10` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 71,580.00 USD | 30,090.00 USD | 65,790.00 USD |
| `7D` | `1.10` | 10,260,000.00 USD | 10,260,000.00 USD | 0.00 USD | 114,820.00 USD | 21,050.00 USD | 92,150.00 USD |
| `7D` | `1.10` | 10,540,000.00 USD | 10,540,000.00 USD | 0.00 USD | 182,190.00 USD | 62,900.00 USD | 41,720.00 USD |
| `7D` | `1.10` | 10,770,000.00 USD | 10,770,000.00 USD | 0.00 USD | 118,210.00 USD | 18,440.00 USD | 88,980.00 USD |
| `7D` | `1.10` | 10,900,000.00 USD | 10,900,000.00 USD | 0.00 USD | 51,230.00 USD | 22,070.00 USD | 56,980.00 USD |
| `7D` | `1.11` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 22,290.00 USD | 5,830.00 USD | 12,610.00 USD |
| `7D` | `1.11` | 11,120,000.00 USD | 11,120,000.00 USD | 0.00 USD | 90,280.00 USD | 31,510.00 USD | 54,600.00 USD |
| `7D` | `1.11` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 33,280.00 USD | 36,570.00 USD | 93,640.00 USD |
| `7D` | `1.11` | 11,400,000.00 USD | 11,400,000.00 USD | 0.00 USD | 64,670.00 USD | 26,930.00 USD | 24,380.00 USD |
| `7D` | `1.11` | 11,470,000.00 USD | 11,470,000.00 USD | 0.00 USD | 32,450.00 USD | 36,820.00 USD | 6,220.00 USD |
| `7D` | `1.12` | 11,580,000.00 USD | 11,580,000.00 USD | 0.00 USD | 59,080.00 USD | 33,150.00 USD | 13,270.00 USD |
| `7D` | `1.12` | 11,660,000.00 USD | 11,660,000.00 USD | 0.00 USD | 37,220.00 USD | 17,240.00 USD | 30,330.00 USD |
| `7D` | `1.12` | 11,760,000.00 USD | 11,760,000.00 USD | 0.00 USD | 32,060.00 USD | 41,540.00 USD | 25,240.00 USD |
| `7D` | `1.12` | 11,840,000.00 USD | 11,840,000.00 USD | 0.00 USD | 52,230.00 USD | 16,980.00 USD | 11,540.00 USD |
| `7D` | `1.12` | 11,930,000.00 USD | 11,930,000.00 USD | 0.00 USD | 58,100.00 USD | 5,280.00 USD | 29,870.00 USD |
| `7D` | `1.13` | 11,990,000.00 USD | 11,990,000.00 USD | 0.00 USD | 16,200.00 USD | 5,970.00 USD | 28,450.00 USD |
| `7D` | `1.13` | 12,030,000.00 USD | 12,030,000.00 USD | 0.00 USD | 2,210.00 USD | 13,650.00 USD | 28,630.00 USD |
| `7D` | `1.13` | 12,190,000.00 USD | 12,190,000.00 USD | 0.00 USD | 95,910.00 USD | 18,230.00 USD | 42,350.00 USD |
| `7D` | `1.13` | 12,320,000.00 USD | 12,320,000.00 USD | 0.00 USD | 71,210.00 USD | 0.00 USD | 65,880.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `208.72M` | Total OI Tokens: `211,852,021.0 DOT`
  * 1h OI Change: `+0.13%` | 4h OI Change: `-2.87%` | 24h OI Change: `-6.62%`
  * Exchange Breakdown: Binance=`36.50M` | Bybit=`24.40M` | OKX=`10.23M` | Hyperliquid=`5.68M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `5.02K` | Last 24h: `7.91K` | Last 3d: `-10.37K` | Last 7d: `-19.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0064%` | **USDT OKX** | `0.0079%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0070%` |
| **USDT MEXC** | `0.0065%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0037%` | **USDT Bitget** | `0.0038%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `48.02%` | `51.98%` | `0.92` | 3,480,000.00 USD |
| `15M` | `Binance` | `58.04%` | `41.96%` | `1.38` | 683,940.00 USD |
| `15M` | `OKX` | `49.78%` | `50.22%` | `0.99` | 336,270.00 USD |
| `15M` | `Bybit` | `55.84%` | `44.16%` | `1.26` | 116,880.00 USD |
| `15M` | `KuCoin` | `45.02%` | `54.98%` | `0.82` | 31,760.00 USD |
| `15M` | `Gate` | `56.59%` | `43.41%` | `1.30` | 29,620.00 USD |
| `15M` | `Bitget` | `42.38%` | `57.62%` | `0.74` | 95,580.00 USD |
| `15M` | `BingX` | `52.72%` | `47.28%` | `1.12` | 102,550.00 USD |
| `15M` | `MEXC` | `46.79%` | `53.21%` | `0.88` | 1,690,000.00 USD |
| `15M` | `Bitunix` | `60.85%` | `39.15%` | `1.55` | 60,520.00 USD |
| `15M` | `Hyperliquid` | `2.66%` | `97.34%` | `0.03` | 46,670.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `56.83%` | `43.17%` | `1.32` | 83,930.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 150,960.00 USD |
| `15M` | `HTX` | `6.98%` | `93.02%` | `0.08` | 2,330.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `90.13%` | `9.87%` | `9.13` | 19,370.00 USD |
| `15M` | `Aster` | `51.33%` | `48.67%` | `1.05` | 4,190.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `97.99%` | `2.01%` | `48.75` | 14,940.00 USD |
| `15M` | `Whale Positions` | `58.04%` | `41.96%` | `1.38` | 683,940.00 USD |
| `15M` | `Global Accounts` | `48.02%` | `51.98%` | `0.92` | 3,480,000.00 USD |
| `1H` | `DOT` | `53.23%` | `46.77%` | `1.14` | 4,900,000.00 USD |
| `1H` | `Binance` | `53.36%` | `46.64%` | `1.14` | 1,830,000.00 USD |
| `1H` | `OKX` | `69.54%` | `30.46%` | `2.28` | 385,660.00 USD |
| `1H` | `Bybit` | `60.09%` | `39.91%` | `1.51` | 277,020.00 USD |
| `1H` | `KuCoin` | `50.35%` | `49.65%` | `1.01` | 145,890.00 USD |
| `1H` | `Gate` | `45.85%` | `54.15%` | `0.85` | 93,130.00 USD |
| `1H` | `Bitget` | `72.07%` | `27.93%` | `2.58` | 186,160.00 USD |
| `1H` | `BingX` | `51.52%` | `48.48%` | `1.06` | 485,120.00 USD |
| `1H` | `MEXC` | `66.15%` | `33.85%` | `1.95` | 299,770.00 USD |
| `1H` | `Bitunix` | `54.76%` | `45.24%` | `1.21` | 118,660.00 USD |
| `1H` | `Hyperliquid` | `14.86%` | `85.14%` | `0.17` | 13,470.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.47%` | `49.53%` | `1.02` | 771,960.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `11.25%` | `88.75%` | `0.13` | 269,540.00 USD |
| `1H` | `HTX` | `22.9%` | `77.1%` | `0.30` | 2,620.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `46.19%` | `53.81%` | `0.86` | 17,800.00 USD |
| `1H` | `Aster` | `95.08%` | `4.92%` | `19.33` | 2,550.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `53.36%` | `46.64%` | `1.14` | 1,830,000.00 USD |
| `1H` | `Global Accounts` | `53.23%` | `46.77%` | `1.14` | 4,900,000.00 USD |
| `4H` | `DOT` | `46.77%` | `53.23%` | `0.88` | 350,080,000.00 USD |
| `4H` | `Binance` | `48.2%` | `51.8%` | `0.93` | 141,470,000.00 USD |
| `4H` | `OKX` | `47.05%` | `52.95%` | `0.89` | 48,160,000.00 USD |
| `4H` | `Bybit` | `48.28%` | `51.72%` | `0.93` | 42,480,000.00 USD |
| `4H` | `KuCoin` | `50.17%` | `49.83%` | `1.01` | 3,230,000.00 USD |
| `4H` | `Gate` | `44.4%` | `55.6%` | `0.80` | 6,580,000.00 USD |
| `4H` | `Bitget` | `51.98%` | `48.02%` | `1.08` | 11,660,000.00 USD |
| `4H` | `BingX` | `36.8%` | `63.2%` | `0.58` | 17,090,000.00 USD |
| `4H` | `MEXC` | `53.13%` | `46.87%` | `1.13` | 20,820,000.00 USD |
| `4H` | `Bitunix` | `46.07%` | `53.93%` | `0.85` | 10,250,000.00 USD |
| `4H` | `Hyperliquid` | `32.4%` | `67.6%` | `0.48` | 25,140,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.01%` | `47.99%` | `1.08` | 2,120,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 8,510.00 USD |
| `4H` | `WhiteBIT` | `19.13%` | `80.87%` | `0.24` | 10,400,000.00 USD |
| `4H` | `HTX` | `67.45%` | `32.55%` | `2.07` | 241,420.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `57.23%` | `42.77%` | `1.34` | 6,670,000.00 USD |
| `4H` | `Aster` | `31.53%` | `68.47%` | `0.46` | 398,640.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 3,330,000.00 USD |
| `4H` | `Whale Positions` | `48.2%` | `51.8%` | `0.93` | 141,470,000.00 USD |
| `4H` | `Global Accounts` | `46.77%` | `53.23%` | `0.88` | 350,080,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.9950` | `0.9984` | `0.9950` | `1.00` | `0.9922` | 743,609.00 USD | 261,947.82 USD | 481,661.18 USD | -219,713.36 USD | `-29.55%` | `13B / 51S` |
| `5:00 UTC` | `0.9889` | `0.9893` | `0.9889` | `0.9946` | `0.9848` | 979,161.78 USD | 393,210.73 USD | 585,951.05 USD | -192,740.33 USD | `-19.68%` | `5B / 24S` |
| `0:00 UTC` | `0.9900` | `0.9907` | `0.9900` | `0.9929` | `0.9876` | 406,034.57 USD | 195,166.38 USD | 210,868.18 USD | -15,701.80 USD | `-3.87%` | `3B / 8S` |
| `5:00 UTC` | `0.9850` | `0.9875` | `0.9850` | `0.9919` | `0.9848` | 373,179.10 USD | 160,064.27 USD | 213,114.83 USD | -53,050.55 USD | `-14.22%` | `10B / 18S` |
| `0:00 UTC` | `0.9787` | `0.9807` | `0.9787` | `0.9872` | `0.9767` | 1,756,422.05 USD | 785,190.37 USD | 971,231.69 USD | -186,041.32 USD | `-10.59%` | `9B / 23S` |
| `5:00 UTC` | `0.9813` | `0.9827` | `0.9813` | `0.9867` | `0.9789` | 947,049.41 USD | 720,261.00 USD | 226,788.42 USD | 493,472.58 USD | `+52.11%` | `28B / 1S` |
| `0:00 UTC` | `0.9805` | `0.9815` | `0.9805` | `0.9849` | `0.9787` | 512,523.44 USD | 243,023.57 USD | 269,499.87 USD | -26,476.30 USD | `-5.17%` | `12B / 6S` |
| `5:00 UTC` | `0.9856` | `0.9822` | `0.9856` | `0.9858` | `0.9780` | 526,140.64 USD | 318,567.26 USD | 207,573.38 USD | 110,993.88 USD | `+21.10%` | `16B / 9S` |
| `0:00 UTC` | `0.9873` | `0.9868` | `0.9873` | `0.9887` | `0.9839` | 407,897.05 USD | 216,028.73 USD | 191,868.32 USD | 24,160.41 USD | `+5.92%` | `8B / 4S` |
| `5:00 UTC` | `0.9858` | `0.9859` | `0.9858` | `0.9880` | `0.9839` | 384,841.22 USD | 175,564.29 USD | 209,276.93 USD | -33,712.64 USD | `-8.76%` | `3B / 7S` |

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
| `5m` | -52,780.00 USD | -381,400.00 USD | **`DISTRIBUTION`** |
| `15m` | -31,520.00 USD | -351,240.00 USD | **`DISTRIBUTION`** |
| `30m` | -36,840.00 USD | -317,920.00 USD | **`DISTRIBUTION`** |
| `1h` | 39,440.00 USD | -69,160.00 USD | **`DISTRIBUTION`** |
| `2h` | -86,640.00 USD | 198,890.00 USD | **`ACCUMULATION`** |
| `4h` | -158,130.00 USD | -1,420,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -135,240.00 USD | -1,780,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -167,190.00 USD | -1,800,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -245,490.00 USD | -1,830,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -477,550.00 USD | -3,030,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,450,000.00 USD | -18,550,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,570,000.00 USD | -73,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-52.78K` | 15m=`-31.52K` | 1h=`+39.44K` | 24h=`-477.55K`
* Futures Capital Netflows: 5m=`-381.40K` | 15m=`-351.24K` | 1h=`-69.16K` | 24h=`-3.03M`
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
  * `2026-10-30 00:58:24 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:29:24 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:29:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.9530` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.9131` (Risk Distance: `0.0420` pts)
  * +2.5R Take Profit: `1.06`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9929` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.03` (Risk Distance: `0.0420` pts)
  * +2.5R Take Profit: `0.8879`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9833`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
