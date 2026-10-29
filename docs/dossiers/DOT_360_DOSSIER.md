# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 02:24:37 IST` (`2026-10-29 20:54:37 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9030` | **Live Ask Quote**: `0.9290` | **Mid Price**: `0.9160`
- **Spread Points**: `26.00` | **Spread BPS**: `283.84 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.9762` | VWAP Z-Score: `-1.35` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0083` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `32.10` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.02` | Lower -3.00σ Band: `0.9335`
  * Upper +2.51σ Band: `1.01` | Lower -2.51σ Band: `0.9405`
  * Upper +2.01σ Band: `1.00` | Lower -2.01σ Band: `0.9476`
  * Upper +2.00σ Band: `1.00` | Lower -2.00σ Band: `0.9478`
  * Upper +1.28σ Band: `0.9945` | Lower -1.28σ Band: `0.9580`
  * Upper +1.00σ Band: `0.9905` | Lower -1.00σ Band: `0.9620`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9694` | EMA-20=`0.9762` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9794` (Slope: `+0.0000`) | EMA-100=`0.9814`
  * Institutional Anchors: EMA-144=`0.9826` | EMA-200=`0.9834` (Slope: `-0.1474`) | EMA-233=`0.9839`
- **Range Boundaries**: 24H High=`1.02` | 24H Low=`0.9460` | Weekly High=`1.03` | Weekly Low=`0.9460`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9952` (Distance: `-7.31%`)
  * Point of Control (POC) = `0.9749` (Distance: `-5.38%`)
  * Value Area Low (VAL) = `0.9539` (Distance: `-3.29%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.00` | POC=`0.9890` | VAL=`0.9812`
  * Prior Day Extremes: PDH=`1.03` | PDL=`0.9690` | PDC=`1.01`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.01` | Weekly POC=`0.9927` | Weekly VAL=`0.9772`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.02` | Low=`0.9510`
  * London Session (08:00-16:00 UTC): High=`0.9850` | Low=`0.9600`
  * New York Session (13:00-21:00 UTC): High=`1.01` | Low=`0.9680`
  * Initial Balance (First Hour): IB High=`0.9800` | IB Low=`0.9670`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9123` - `0.9197`
  * Optimal Trade Entry (OTE 0.705): `0.9178`
  * Structural Invalidation Anchor (0.786): `0.9233`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9676` | `0.9706` | `0.9530` | `0.9596` | `1,655,701` | 1,587,708.15 USD | -75,534.85 USD | `-4.76%` | -1,040,741.65 USD | `-0.78` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `0.9596` | `0.9622` | `0.9512` | `0.9549` | `1,126,283` | 1,077,334.46 USD | 9,246.36 USD | `+0.86%` | -1,031,495.29 USD | `+0.44` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.9548` | `0.9555` | `0.9105` | `0.9210` | `7,083,669` | 6,596,293.46 USD | -1,826,195.88 USD | `-27.69%` | -2,857,691.17 USD | `-4.29` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9845` | `0.9849` | `0.9556` | `0.9696` | `3,856,197` | 3,728,299.49 USD | -392,746.09 USD | `-10.53%` | -918,999.04 USD | `-1.45` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.9695` | `0.9717` | `0.9650` | `0.9676` | `818,379` | 792,721.03 USD | -46,207.76 USD | `-5.83%` | -965,206.80 USD | `-0.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.9676` | `0.9706` | `0.9105` | `0.9230` | `9,842,673` | 9,240,151.50 USD | -1,882,726.05 USD | `-20.38%` | -2,847,932.85 USD | `-3.78` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.9918` | `0.9929` | `0.9766` | `0.9840` | `3,542,573` | 3,482,685.13 USD | 238,678.91 USD | `+6.85%` | -618,930.49 USD | `+0.79` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.9839` | `0.9886` | `0.9780` | `0.9844` | `1,864,944` | 1,834,632.46 USD | 75,709.02 USD | `+4.13%` | -543,221.47 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9845` | `0.9849` | `0.9105` | `0.9239` | `14,510,999` | 13,755,402.52 USD | -2,322,020.11 USD | `-16.88%` | -2,865,241.58 USD | `-3.67` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | 516,506.12 USD | `-1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -280,559.32 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.9105` | `0.9230` | `14,517,249` | 13,761,172.02 USD | -2,321,679.90 USD | `-16.87%` | -2,602,239.23 USD | `-2.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.9699` | `0.9906` | `0.9674` | `0.9732` | `8,505,701` | 8,320,368.15 USD | 13,201.93 USD | `+0.16%` | 609,018.52 USD | `-1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | 694,082.93 USD | `-0.56` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | 516,506.12 USD | `-1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -280,559.32 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.9105` | `0.9230` | `14,517,249` | 13,761,172.02 USD | -2,321,679.90 USD | `-16.87%` | -2,602,239.23 USD | `-2.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:14:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.01` | 5,229.69 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale BUY: 5.23K USD at 1.0066 USD [API] | `2026-10-28 01:55:55` |
| `ANNOUNCEMENT` | `INFO` | `1.00` | 5,901.97 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale BUY: 5.90K USD at 1.0012 USD [API] | `2026-10-28 03:15:43` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.03` (Vol: 80,100.00 USD, Dist: `+6.18%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`1.04` (Vol: 74,700.00 USD, Dist: `+7.15%`) | Long MP=`0.9471` (Vol: 122,200.00 USD, Dist: `--2.16%`)
  * 3D Horizon: Short MP=`1.04` (Vol: 74,700.00 USD, Dist: `+7.15%`) | Long MP=`0.9510` (Vol: 130,500.00 USD, Dist: `--1.75%`)
  * 7D Horizon: Short MP=`1.06` (Vol: 233,300.00 USD, Dist: `+9.35%`) | Long MP=`0.9512` (Vol: 153,700.00 USD, Dist: `--1.73%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2345` | 117.25 USD | 530,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3265` | 589.56 USD | 530,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3355` | 741.12 USD | 529,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3775` | 2,150.00 USD | 528,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4025` | 128.52 USD | 526,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 2,790.00 USD | 526,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4505` | 178.62 USD | 523,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4695` | 2,580.00 USD | 523,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5005` | 146.30 USD | 521,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5025` | 201.35 USD | 520,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5035` | 996.88 USD | 520,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5115` | 606.38 USD | 519,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 4,130.00 USD | 519,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5215` | 12,720.00 USD | 515,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5465` | 106.84 USD | 502,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 577.36 USD | 502,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 137.53 USD | 501,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5955` | 3,390.00 USD | 501,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6055` | 1,480.00 USD | 498,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6065` | 1,800.00 USD | 496,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 105.96 USD | 494,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 147.48 USD | 494,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6245` | 525.77 USD | 494,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6305` | 154.22 USD | 494,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 757.80 USD | 493,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 106.00 USD | 493,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 20,270.00 USD | 493,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 4,230.00 USD | 472,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 202.47 USD | 468,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 149.44 USD | 468,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 63,890.00 USD | 468,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 423.10 USD | 404,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 512.97 USD | 403,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6855` | 2,110.00 USD | 403,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6955` | 322.16 USD | 401,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 155.60 USD | 400,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7025` | 702.50 USD | 400,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7055` | 176.38 USD | 400,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 16,520.00 USD | 399,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 988.87 USD | 383,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7175` | 322.88 USD | 382,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7205` | 866.26 USD | 382,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 1,090.00 USD | 381,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7275` | 126.44 USD | 380,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 291.18 USD | 379,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 2,300.00 USD | 379,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,140.00 USD | 377,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7375` | 2,050.00 USD | 376,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 283.30 USD | 374,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7455` | 1,390.00 USD | 373,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 331.18 USD | 372,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 2,390.00 USD | 372,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7605` | 3,120.00 USD | 369,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 1,580.00 USD | 366,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 292.03 USD | 365,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7895` | 20,380.00 USD | 364,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7920` | 491,830.00 USD | 491,830.00 USD | 6,470.00 USD | 1,650.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7920` | 559,290.00 USD | 559,290.00 USD | 6,470.00 USD | 1,650.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.7940` | 478,650.00 USD | 478,650.00 USD | 1,860.00 USD | 595.59 USD | 965.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7940` | 546,110.00 USD | 546,110.00 USD | 1,860.00 USD | 595.59 USD | 965.49 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.7960` | 475,230.00 USD | 475,230.00 USD | 222.45 USD | 2,470.00 USD | 1,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7960` | 542,690.00 USD | 542,690.00 USD | 222.45 USD | 2,470.00 USD | 1,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7965` | 106.49 USD | 344,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7980` | 471,480.00 USD | 471,480.00 USD | 1,140.00 USD | 22.38 USD | 494.59 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7980` | 538,940.00 USD | 538,940.00 USD | 1,140.00 USD | 22.38 USD | 494.59 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8000` | 469,820.00 USD | 469,820.00 USD | 7.83 USD | 5.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8000` | 537,280.00 USD | 537,280.00 USD | 7.83 USD | 5.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8020` | 468,610.00 USD | 468,610.00 USD | 2,290.00 USD | 1,600.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8020` | 536,070.00 USD | 536,070.00 USD | 2,290.00 USD | 1,600.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8025` | 238.90 USD | 344,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8040` | 462,600.00 USD | 462,600.00 USD | 813.73 USD | 993.93 USD | 952.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8040` | 530,060.00 USD | 530,060.00 USD | 813.73 USD | 993.93 USD | 952.73 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8045` | 566.61 USD | 344,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8055` | 699.01 USD | 343,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8060` | 459,840.00 USD | 459,840.00 USD | 536.61 USD | 845.93 USD | 53.10 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8060` | 527,300.00 USD | 527,300.00 USD | 536.61 USD | 845.93 USD | 53.10 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8080` | 458,410.00 USD | 458,410.00 USD | 4,130.00 USD | 657.69 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8080` | 525,870.00 USD | 525,870.00 USD | 4,130.00 USD | 657.69 USD | 1,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8100` | 451,830.00 USD | 451,830.00 USD | 1,940.00 USD | 14.30 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8100` | 519,290.00 USD | 519,290.00 USD | 1,940.00 USD | 14.30 USD | 3,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8115` | 13,430.00 USD | 342,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8120` | 446,330.00 USD | 446,330.00 USD | 821.06 USD | 258.31 USD | 44.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8120` | 513,800.00 USD | 513,800.00 USD | 821.06 USD | 258.31 USD | 44.49 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 329,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8140` | 445,210.00 USD | 445,210.00 USD | 4,760.00 USD | 30.50 USD | 796.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8140` | 512,670.00 USD | 512,670.00 USD | 4,760.00 USD | 30.50 USD | 796.05 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8160` | 439,630.00 USD | 439,630.00 USD | 0.00 USD | 182.45 USD | 26.89 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8160` | 507,090.00 USD | 507,090.00 USD | 0.00 USD | 182.45 USD | 26.89 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8180` | 439,420.00 USD | 439,420.00 USD | 99.55 USD | 6.25 USD | 96.08 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8180` | 506,880.00 USD | 506,880.00 USD | 9,320.00 USD | 6.25 USD | 96.08 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8200` | 439,220.00 USD | 439,220.00 USD | 1,260.00 USD | 0.00 USD | 435.27 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8200` | 497,460.00 USD | 497,460.00 USD | 1,260.00 USD | 0.00 USD | 435.27 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 328,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8220` | 437,520.00 USD | 437,520.00 USD | 0.00 USD | 0.00 USD | 471.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8220` | 495,760.00 USD | 495,760.00 USD | 0.00 USD | 0.00 USD | 471.94 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8240` | 437,050.00 USD | 437,050.00 USD | 0.00 USD | 3,640.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8240` | 495,290.00 USD | 495,290.00 USD | 0.00 USD | 3,640.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8285` | 1,890.00 USD | 326,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 324,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8375` | 167.00 USD | 324,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8400` | 426,610.00 USD | 426,610.00 USD | 458.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8400` | 484,850.00 USD | 484,850.00 USD | 458.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,240.00 USD | 324,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 426,150.00 USD | 426,150.00 USD | 0.00 USD | 149.63 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8420` | 484,390.00 USD | 484,390.00 USD | 0.00 USD | 149.63 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8440` | 484,240.00 USD | 484,240.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8445` | 168.31 USD | 323,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 323,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 426,000.00 USD | 426,000.00 USD | 421.90 USD | 61.55 USD | 206.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8500` | 482,290.00 USD | 482,290.00 USD | 421.90 USD | 61.55 USD | 206.79 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8520` | 425,310.00 USD | 425,310.00 USD | 0.00 USD | 1,940.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8520` | 481,600.00 USD | 481,600.00 USD | 0.00 USD | 1,940.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8560` | 420,910.00 USD | 420,910.00 USD | 0.00 USD | 199.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8560` | 477,190.00 USD | 477,190.00 USD | 0.00 USD | 199.60 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 321,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8580` | 420,710.00 USD | 420,710.00 USD | 250.65 USD | 0.00 USD | 182.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8580` | 476,990.00 USD | 476,990.00 USD | 250.65 USD | 0.00 USD | 182.69 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8595` | 171.38 USD | 321,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8600` | 420,270.00 USD | 420,270.00 USD | 3,240.00 USD | 1,030.00 USD | 251.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8600` | 476,550.00 USD | 476,550.00 USD | 5,860.00 USD | 1,030.00 USD | 251.39 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8605` | 61,100.00 USD | 320,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8620` | 415,740.00 USD | 415,740.00 USD | 7,410.00 USD | 24.95 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8620` | 469,410.00 USD | 469,410.00 USD | 7,410.00 USD | 24.95 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8625` | 309.55 USD | 259,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 259,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 408,300.00 USD | 408,300.00 USD | 5,790.00 USD | 1,940.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8640` | 461,970.00 USD | 461,970.00 USD | 5,790.00 USD | 1,940.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 259,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8660` | 396,780.00 USD | 396,780.00 USD | 0.00 USD | 20.18 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8660` | 450,450.00 USD | 450,450.00 USD | 0.00 USD | 20.18 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 118.54 USD | 258,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8680` | 396,760.00 USD | 396,760.00 USD | 3,320.00 USD | 3,550.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8680` | 450,430.00 USD | 450,430.00 USD | 3,320.00 USD | 3,550.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8700` | 381,170.00 USD | 381,170.00 USD | 15,620.00 USD | 3,580.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8700` | 434,840.00 USD | 434,840.00 USD | 15,620.00 USD | 3,580.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8720` | 357,210.00 USD | 357,210.00 USD | 9,180.00 USD | 26.70 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8720` | 410,880.00 USD | 410,880.00 USD | 32,240.00 USD | 26.70 USD | 6,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 341,790.00 USD | 341,790.00 USD | 6,780.00 USD | 3,080.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8740` | 372,400.00 USD | 372,400.00 USD | 6,780.00 USD | 3,080.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 328,890.00 USD | 328,890.00 USD | 6,140.00 USD | 3,510.00 USD | 4,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8760` | 359,510.00 USD | 359,510.00 USD | 6,140.00 USD | 3,510.00 USD | 4,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 171.88 USD | 258,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8780` | 314,850.00 USD | 314,850.00 USD | 15,310.00 USD | 15,510.00 USD | 27,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8780` | 345,460.00 USD | 345,460.00 USD | 15,310.00 USD | 15,510.00 USD | 27,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8795` | 948.01 USD | 258,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8800` | 256,930.00 USD | 256,930.00 USD | 12,000.00 USD | 5,110.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8800` | 287,550.00 USD | 287,550.00 USD | 12,000.00 USD | 5,110.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8820` | 234,340.00 USD | 234,340.00 USD | 8,950.00 USD | 4,070.00 USD | 150.13 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8820` | 264,960.00 USD | 264,960.00 USD | 8,950.00 USD | 4,070.00 USD | 150.13 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 221,170.00 USD | 221,170.00 USD | 7,440.00 USD | 1,810.00 USD | 1,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8840` | 251,780.00 USD | 251,780.00 USD | 7,440.00 USD | 1,810.00 USD | 1,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8860` | 210,890.00 USD | 210,890.00 USD | 5,930.00 USD | 1,700.00 USD | 8,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8860` | 241,510.00 USD | 241,510.00 USD | 5,930.00 USD | 1,700.00 USD | 8,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8880` | 195,080.00 USD | 195,080.00 USD | 17,470.00 USD | 4,160.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8880` | 225,690.00 USD | 225,690.00 USD | 17,470.00 USD | 4,160.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8900` | 163,690.00 USD | 163,690.00 USD | 4,010.00 USD | 4,210.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8900` | 194,300.00 USD | 194,300.00 USD | 50,120.00 USD | 4,210.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8920` | 150,470.00 USD | 150,470.00 USD | 4,920.00 USD | 3,110.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8920` | 134,970.00 USD | 134,970.00 USD | 4,920.00 USD | 3,110.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8925` | 526.84 USD | 257,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8940` | 140,490.00 USD | 140,490.00 USD | 4,240.00 USD | 0.00 USD | 966.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8940` | 124,990.00 USD | 124,990.00 USD | 4,240.00 USD | 0.00 USD | 966.50 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8960` | 135,280.00 USD | 135,280.00 USD | 1,930.00 USD | 15,480.00 USD | 6,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8960` | 119,780.00 USD | 119,780.00 USD | 1,930.00 USD | 15,480.00 USD | 6,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8980` | 111,320.00 USD | 111,320.00 USD | 21,610.00 USD | 10,780.00 USD | 32,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8980` | 95,820.00 USD | 95,820.00 USD | 21,610.00 USD | 10,780.00 USD | 32,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8985` | 9,220.00 USD | 257,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8995` | 3,820.00 USD | 247,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9000` | 46,020.00 USD | 46,020.00 USD | 3,760.00 USD | 720.16 USD | 2,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9000` | 30,520.00 USD | 30,520.00 USD | 3,760.00 USD | 720.16 USD | 2,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9020` | 39,160.00 USD | 39,160.00 USD | 4,420.00 USD | 3,120.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9020` | 23,670.00 USD | 23,670.00 USD | 4,420.00 USD | 3,120.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9035` | 180.16 USD | 244,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9040` | 29,380.00 USD | 29,380.00 USD | 3,360.00 USD | 2,430.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9040` | 13,890.00 USD | 13,890.00 USD | 1,580.00 USD | 2,430.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9055` | 674.42 USD | 243,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9060` | 17,880.00 USD | 17,880.00 USD | 10,120.00 USD | 1,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9060` | 4,160.00 USD | 4,160.00 USD | 0.00 USD | 1,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9080` | 6,140.00 USD | 6,140.00 USD | 5,800.00 USD | 346.80 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9080` | 2,550.00 USD | 2,550.00 USD | 0.00 USD | 346.80 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9095` | 951.34 USD | 243,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9100` | 4,690.00 USD | 4,690.00 USD | 3,880.00 USD | 815.15 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9100` | 2,200.00 USD | 2,200.00 USD | 1,380.00 USD | 815.15 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9120` | 6,990.00 USD | 6,990.00 USD | 1,980.00 USD | 315.61 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9120` | 2,290.00 USD | 2,290.00 USD | 1,980.00 USD | 315.61 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9120` | 4,590.00 USD | 4,590.00 USD | 1,980.00 USD | 315.61 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9135` | 143.42 USD | 242,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9140` | 9,030.00 USD | 9,030.00 USD | 1,840.00 USD | 200.33 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9140` | 6,630.00 USD | 6,630.00 USD | 1,840.00 USD | 200.33 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9160` | 14,860.00 USD | 14,860.00 USD | 5,700.00 USD | 131.45 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9160` | 12,460.00 USD | 12,460.00 USD | 5,700.00 USD | 131.45 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9180` | 15,480.00 USD | 15,480.00 USD | 485.63 USD | 132.34 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9180` | 13,080.00 USD | 13,080.00 USD | 485.63 USD | 132.34 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9185` | 145.86 USD | 242,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9195` | 7,330.00 USD | 241,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9200` | 15,640.00 USD | 15,640.00 USD | 0.00 USD | 166.12 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9200` | 13,240.00 USD | 13,240.00 USD | 0.00 USD | 166.12 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9220` | 44,100.00 USD | 44,100.00 USD | 14,160.00 USD | 77.74 USD | 14,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9220` | 41,700.00 USD | 41,700.00 USD | 14,160.00 USD | 77.74 USD | 14,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9225` | 8,360.00 USD | 234,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9240` | 53,110.00 USD | 53,110.00 USD | 7,970.00 USD | 1,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9240` | 50,710.00 USD | 50,710.00 USD | 7,970.00 USD | 1,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9260` | 99,060.00 USD | 99,060.00 USD | 6,310.00 USD | 1,100.00 USD | 38,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9260` | 142,770.00 USD | 142,770.00 USD | 52,420.00 USD | 1,100.00 USD | 38,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9280` | 160,130.00 USD | 160,130.00 USD | 47,790.00 USD | 145.20 USD | 13,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9280` | 203,840.00 USD | 203,840.00 USD | 47,790.00 USD | 145.20 USD | 13,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9295` | 253.01 USD | 226,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9300` | 204,940.00 USD | 204,940.00 USD | 21,640.00 USD | 221.69 USD | 22,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9300` | 248,650.00 USD | 248,650.00 USD | 21,640.00 USD | 221.69 USD | 22,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9320` | 252,790.00 USD | 252,790.00 USD | 26,400.00 USD | 7,580.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9320` | 296,500.00 USD | 296,500.00 USD | 26,400.00 USD | 7,580.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9335` | 361.45 USD | 226,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9340` | 342,620.00 USD | 342,620.00 USD | 35,410.00 USD | 10,860.00 USD | 43,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9340` | 386,330.00 USD | 386,330.00 USD | 35,410.00 USD | 10,860.00 USD | 43,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9360` | 427,160.00 USD | 427,160.00 USD | 64,130.00 USD | 475.50 USD | 19,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9360` | 470,870.00 USD | 470,870.00 USD | 64,130.00 USD | 475.50 USD | 19,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9365` | 6,560.00 USD | 225,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9375` | 196.97 USD | 219,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9380` | 484,040.00 USD | 484,040.00 USD | 56,080.00 USD | 103.28 USD | 695.88 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9380` | 527,750.00 USD | 527,750.00 USD | 56,080.00 USD | 103.28 USD | 695.88 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9400` | 528,400.00 USD | 528,400.00 USD | 41,740.00 USD | 0.00 USD | 2,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9400` | 572,110.00 USD | 572,110.00 USD | 41,740.00 USD | 0.00 USD | 2,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9405` | 141.83 USD | 218,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9420` | 585,870.00 USD | 585,870.00 USD | 57,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9420` | 629,580.00 USD | 629,580.00 USD | 57,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9440` | 621,130.00 USD | 621,130.00 USD | 35,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9440` | 687,890.00 USD | 687,890.00 USD | 58,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9445` | 1,060.00 USD | 218,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9455` | 106,880.00 USD | 217,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9460` | 667,060.00 USD | 667,060.00 USD | 45,730.00 USD | 199.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9460` | 733,820.00 USD | 733,820.00 USD | 45,730.00 USD | 199.60 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9475` | 323.19 USD | 110,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9480` | 812,540.00 USD | 812,540.00 USD | 145,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9480` | 879,300.00 USD | 879,300.00 USD | 145,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9495` | 105,430.00 USD | 110,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9500` | 871,710.00 USD | 871,710.00 USD | 56,840.00 USD | 105.68 USD | 2,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9500` | 941,090.00 USD | 941,090.00 USD | 59,460.00 USD | 105.68 USD | 2,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9515` | 405.62 USD | 5,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9520` | 948,080.00 USD | 948,080.00 USD | 37,660.00 USD | 13,410.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9520` | 1,020,000.00 USD | 1,020,000.00 USD | 37,660.00 USD | 13,410.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 986,530.00 USD | 986,530.00 USD | 8,940.00 USD | 394.58 USD | 29,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9540` | 1,060,000.00 USD | 1,060,000.00 USD | 8,940.00 USD | 394.58 USD | 29,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9555` | 3,160.00 USD | 4,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9560` | 987,390.00 USD | 987,390.00 USD | 865.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9560` | 1,060,000.00 USD | 1,060,000.00 USD | 865.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 987,700.00 USD | 987,700.00 USD | 0.00 USD | 0.00 USD | 313.25 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9580` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 313.25 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9585` | 1,530.00 USD | 1,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9620` | 987,850.00 USD | 987,850.00 USD | 0.00 USD | 149.63 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9620` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 149.63 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 9,690.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9640` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 9,690.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 1,010,000.00 USD | 1,010,000.00 USD | 595.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9660` | 1,080,000.00 USD | 1,080,000.00 USD | 2,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 2,050.00 USD | 10,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9700` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 2,050.00 USD | 10,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 1,070,000.00 USD | 1,070,000.00 USD | 23,620.00 USD | 0.00 USD | 23,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9720` | 1,140,000.00 USD | 1,140,000.00 USD | 23,620.00 USD | 0.00 USD | 23,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 1,120,000.00 USD | 1,120,000.00 USD | 25,800.00 USD | 5,170.00 USD | 14,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9740` | 1,190,000.00 USD | 1,190,000.00 USD | 25,800.00 USD | 5,170.00 USD | 14,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 1,190,000.00 USD | 1,190,000.00 USD | 50,870.00 USD | 13,960.00 USD | 8,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9760` | 1,260,000.00 USD | 1,260,000.00 USD | 50,870.00 USD | 13,960.00 USD | 8,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 1,250,000.00 USD | 1,250,000.00 USD | 37,710.00 USD | 2,960.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9780` | 1,320,000.00 USD | 1,320,000.00 USD | 37,710.00 USD | 2,960.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 1,310,000.00 USD | 1,310,000.00 USD | 29,240.00 USD | 9,580.00 USD | 20,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9800` | 1,380,000.00 USD | 1,380,000.00 USD | 29,240.00 USD | 9,580.00 USD | 20,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 1,340,000.00 USD | 1,340,000.00 USD | 15,980.00 USD | 12,160.00 USD | 7,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9820` | 1,410,000.00 USD | 1,410,000.00 USD | 15,980.00 USD | 12,160.00 USD | 7,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 13,190.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9840` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 13,190.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 1,470,000.00 USD | 1,470,000.00 USD | 50,550.00 USD | 3,460.00 USD | 19,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9860` | 1,540,000.00 USD | 1,540,000.00 USD | 50,550.00 USD | 3,460.00 USD | 19,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9880` | 1,500,000.00 USD | 1,500,000.00 USD | 16,640.00 USD | 0.00 USD | 14,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9880` | 1,570,000.00 USD | 1,570,000.00 USD | 16,640.00 USD | 0.00 USD | 14,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 1,570,000.00 USD | 1,570,000.00 USD | 57,390.00 USD | 1,300.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9900` | 1,640,000.00 USD | 1,640,000.00 USD | 57,390.00 USD | 1,300.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 1,600,000.00 USD | 1,600,000.00 USD | 8,950.00 USD | 2,810.00 USD | 13,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9920` | 1,670,000.00 USD | 1,670,000.00 USD | 8,950.00 USD | 2,810.00 USD | 13,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 1,620,000.00 USD | 1,620,000.00 USD | 12,310.00 USD | 13,250.00 USD | 1,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9940` | 1,700,000.00 USD | 1,700,000.00 USD | 12,310.00 USD | 13,250.00 USD | 1,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 1,650,000.00 USD | 1,650,000.00 USD | 18,530.00 USD | 4,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9960` | 1,720,000.00 USD | 1,720,000.00 USD | 18,530.00 USD | 4,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 1,700,000.00 USD | 1,700,000.00 USD | 40,410.00 USD | 4,790.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9980` | 1,770,000.00 USD | 1,770,000.00 USD | 40,410.00 USD | 4,790.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,790,000.00 USD | 1,790,000.00 USD | 50,740.00 USD | 31,440.00 USD | 1,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 1,870,000.00 USD | 1,870,000.00 USD | 59,960.00 USD | 31,440.00 USD | 1,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,790,000.00 USD | 1,790,000.00 USD | 501.30 USD | 0.00 USD | 266.05 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 1,870,000.00 USD | 1,870,000.00 USD | 501.30 USD | 0.00 USD | 266.05 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,820,000.00 USD | 1,820,000.00 USD | 10,110.00 USD | 9,540.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 1,900,000.00 USD | 1,900,000.00 USD | 10,110.00 USD | 9,540.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 1,960,000.00 USD | 1,960,000.00 USD | 101,040.00 USD | 10,140.00 USD | 31,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,040,000.00 USD | 2,040,000.00 USD | 101,040.00 USD | 10,140.00 USD | 31,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,010,000.00 USD | 2,010,000.00 USD | 9,210.00 USD | 9,160.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,090,000.00 USD | 2,090,000.00 USD | 9,210.00 USD | 9,160.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,020,000.00 USD | 2,020,000.00 USD | 10,530.00 USD | 8,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,110,000.00 USD | 2,110,000.00 USD | 10,530.00 USD | 8,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,070,000.00 USD | 2,070,000.00 USD | 16,240.00 USD | 25,350.00 USD | 155.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,150,000.00 USD | 2,150,000.00 USD | 16,240.00 USD | 25,350.00 USD | 155.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,100,000.00 USD | 2,100,000.00 USD | 5,950.00 USD | 4,370.00 USD | 25,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,180,000.00 USD | 2,180,000.00 USD | 5,950.00 USD | 4,370.00 USD | 25,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,140,000.00 USD | 2,140,000.00 USD | 20,120.00 USD | 75.20 USD | 20,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,220,000.00 USD | 2,220,000.00 USD | 20,120.00 USD | 75.20 USD | 20,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,180,000.00 USD | 2,180,000.00 USD | 6,670.00 USD | 8,490.00 USD | 22,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,260,000.00 USD | 2,260,000.00 USD | 6,670.00 USD | 8,490.00 USD | 22,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,240,000.00 USD | 2,240,000.00 USD | 44,710.00 USD | 4,370.00 USD | 15,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,320,000.00 USD | 2,320,000.00 USD | 44,710.00 USD | 4,370.00 USD | 15,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,320,000.00 USD | 2,320,000.00 USD | 51,380.00 USD | 3,710.00 USD | 21,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,400,000.00 USD | 2,400,000.00 USD | 51,380.00 USD | 3,710.00 USD | 21,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,450,000.00 USD | 2,450,000.00 USD | 50,330.00 USD | 25,640.00 USD | 53,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,530,000.00 USD | 2,530,000.00 USD | 50,330.00 USD | 25,640.00 USD | 53,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,540,000.00 USD | 2,540,000.00 USD | 52,630.00 USD | 18,370.00 USD | 20,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,620,000.00 USD | 2,620,000.00 USD | 52,630.00 USD | 18,370.00 USD | 20,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,600,000.00 USD | 2,600,000.00 USD | 31,340.00 USD | 10,940.00 USD | 18,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,680,000.00 USD | 2,680,000.00 USD | 31,340.00 USD | 10,940.00 USD | 18,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,750,000.00 USD | 2,750,000.00 USD | 95,330.00 USD | 24,510.00 USD | 33,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,840,000.00 USD | 2,840,000.00 USD | 95,330.00 USD | 24,510.00 USD | 33,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,870,000.00 USD | 2,870,000.00 USD | 70,060.00 USD | 8,980.00 USD | 35,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,950,000.00 USD | 2,950,000.00 USD | 70,060.00 USD | 8,980.00 USD | 35,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,940,000.00 USD | 2,940,000.00 USD | 38,330.00 USD | 9,300.00 USD | 21,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,020,000.00 USD | 3,020,000.00 USD | 38,330.00 USD | 9,300.00 USD | 21,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,980,000.00 USD | 2,980,000.00 USD | 18,100.00 USD | 13,840.00 USD | 7,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,060,000.00 USD | 3,060,000.00 USD | 18,100.00 USD | 13,840.00 USD | 7,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 210.51 USD | 210.51 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,050,000.00 USD | 3,050,000.00 USD | 63,010.00 USD | 3,250.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,130,000.00 USD | 3,130,000.00 USD | 63,010.00 USD | 3,250.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,080,000.00 USD | 3,080,000.00 USD | 7,790.00 USD | 10,040.00 USD | 12,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,160,000.00 USD | 3,160,000.00 USD | 7,790.00 USD | 10,040.00 USD | 12,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,110,000.00 USD | 3,110,000.00 USD | 11,290.00 USD | 9,870.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,190,000.00 USD | 3,190,000.00 USD | 11,290.00 USD | 9,870.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,150,000.00 USD | 3,150,000.00 USD | 7,410.00 USD | 9,310.00 USD | 21,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,230,000.00 USD | 3,230,000.00 USD | 7,410.00 USD | 9,310.00 USD | 21,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 212.03 USD | 422.54 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,170,000.00 USD | 3,170,000.00 USD | 21,730.00 USD | 4,160.00 USD | 321.14 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 3,250,000.00 USD | 3,250,000.00 USD | 21,730.00 USD | 4,160.00 USD | 321.14 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 424.67 USD | 847.21 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 733.98 USD | 1,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,190,000.00 USD | 3,190,000.00 USD | 8,930.00 USD | 3,210.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 3,270,000.00 USD | 3,270,000.00 USD | 8,930.00 USD | 3,210.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,260,000.00 USD | 3,260,000.00 USD | 42,790.00 USD | 10,010.00 USD | 13,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 3,340,000.00 USD | 3,340,000.00 USD | 42,790.00 USD | 10,010.00 USD | 13,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,300,000.00 USD | 3,300,000.00 USD | 23,270.00 USD | 1,310.00 USD | 15,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 3,380,000.00 USD | 3,380,000.00 USD | 23,270.00 USD | 1,310.00 USD | 15,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 213.55 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 213.76 USD | 2,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,320,000.00 USD | 3,320,000.00 USD | 16,310.00 USD | 365.79 USD | 6,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 3,400,000.00 USD | 3,400,000.00 USD | 16,310.00 USD | 365.79 USD | 6,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.06` | 74,410.00 USD | 76,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,340,000.00 USD | 3,340,000.00 USD | 13,640.00 USD | 3,680.00 USD | 4,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 3,420,000.00 USD | 3,420,000.00 USD | 13,640.00 USD | 3,680.00 USD | 4,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,380,000.00 USD | 3,380,000.00 USD | 29,640.00 USD | 3,000.00 USD | 725.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 3,460,000.00 USD | 3,460,000.00 USD | 29,640.00 USD | 3,000.00 USD | 725.34 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.06` | 214.97 USD | 76,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,390,000.00 USD | 3,390,000.00 USD | 3,850.00 USD | 4,510.00 USD | 8,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 3,470,000.00 USD | 3,470,000.00 USD | 3,850.00 USD | 4,510.00 USD | 8,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,400,000.00 USD | 3,400,000.00 USD | 1,990.00 USD | 3,730.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 3,480,000.00 USD | 3,480,000.00 USD | 1,990.00 USD | 3,730.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.06` | 431.57 USD | 77,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,420,000.00 USD | 3,420,000.00 USD | 15,200.00 USD | 2,970.00 USD | 3,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 3,500,000.00 USD | 3,500,000.00 USD | 15,200.00 USD | 2,970.00 USD | 3,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 3,450,000.00 USD | 3,450,000.00 USD | 16,000.00 USD | 141.60 USD | 8,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 3,530,000.00 USD | 3,530,000.00 USD | 16,000.00 USD | 141.60 USD | 8,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 3,460,000.00 USD | 3,460,000.00 USD | 7,520.00 USD | 4,330.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 3,540,000.00 USD | 3,540,000.00 USD | 7,520.00 USD | 4,330.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.07` | 216.89 USD | 77,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.07` | 3,480,000.00 USD | 3,480,000.00 USD | 7,140.00 USD | 3,900.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 3,560,000.00 USD | 3,560,000.00 USD | 7,140.00 USD | 3,900.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.07` | 217.20 USD | 77,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.07` | 3,490,000.00 USD | 3,490,000.00 USD | 9,330.00 USD | 2,350.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 3,570,000.00 USD | 3,570,000.00 USD | 9,330.00 USD | 2,350.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 3,510,000.00 USD | 3,510,000.00 USD | 7,860.00 USD | 4,560.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 3,590,000.00 USD | 3,590,000.00 USD | 7,860.00 USD | 4,560.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.07` | 436.03 USD | 77,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.08` | 3,530,000.00 USD | 3,530,000.00 USD | 5,350.00 USD | 5,330.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 3,610,000.00 USD | 3,610,000.00 USD | 5,350.00 USD | 5,330.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 3,540,000.00 USD | 3,540,000.00 USD | 9,430.00 USD | 4,070.00 USD | 150.13 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 3,620,000.00 USD | 3,620,000.00 USD | 9,430.00 USD | 4,070.00 USD | 150.13 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 3,550,000.00 USD | 3,550,000.00 USD | 7,700.00 USD | 1,870.00 USD | 711.93 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 3,630,000.00 USD | 3,630,000.00 USD | 7,700.00 USD | 1,870.00 USD | 711.93 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 3,560,000.00 USD | 3,560,000.00 USD | 5,280.00 USD | 1,770.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 3,640,000.00 USD | 3,640,000.00 USD | 5,280.00 USD | 1,770.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 3,580,000.00 USD | 3,580,000.00 USD | 9,180.00 USD | 1,500.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 3,660,000.00 USD | 3,660,000.00 USD | 9,180.00 USD | 1,500.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 3,590,000.00 USD | 3,590,000.00 USD | 8,920.00 USD | 2,900.00 USD | 6,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 3,680,000.00 USD | 3,680,000.00 USD | 8,920.00 USD | 2,900.00 USD | 6,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 3,610,000.00 USD | 3,610,000.00 USD | 3,630.00 USD | 4,290.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 3,690,000.00 USD | 3,690,000.00 USD | 3,630.00 USD | 4,290.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 3,620,000.00 USD | 3,620,000.00 USD | 5,220.00 USD | 3,220.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 3,700,000.00 USD | 3,700,000.00 USD | 9,830.00 USD | 3,220.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.09` | 221.37 USD | 78,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.09` | 3,620,000.00 USD | 3,620,000.00 USD | 4,370.00 USD | 93.54 USD | 966.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 3,710,000.00 USD | 3,710,000.00 USD | 4,370.00 USD | 93.54 USD | 966.50 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 2,490.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 2,490.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 3,630,000.00 USD | 3,630,000.00 USD | 1,740.00 USD | 3,660.00 USD | 318.21 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 3,720,000.00 USD | 3,720,000.00 USD | 1,740.00 USD | 3,660.00 USD | 318.21 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 3,640,000.00 USD | 3,640,000.00 USD | 3,620.00 USD | 1,090.00 USD | 4,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 3,730,000.00 USD | 3,730,000.00 USD | 3,620.00 USD | 1,090.00 USD | 4,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 3,640,000.00 USD | 3,640,000.00 USD | 1,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 3,730,000.00 USD | 3,730,000.00 USD | 1,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.11` | 169.86 USD | 78,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.12` | 518.90 USD | 78,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.15` | 232.94 USD | 79,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.17` | 2,890.00 USD | 81,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.18` | 228.59 USD | 82,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 22,180.00 USD | 104,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 11,730.00 USD | 116,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 389.93 USD | 116,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.42` | 4,330.00 USD | 120,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 513,610.00 USD | 634,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 232.49 USD | 634,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 176.31 USD | 634,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 9,590.00 USD | 644,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 759.80 USD | 645,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 240.30 USD | 645,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 318.46 USD | 645,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 300.15 USD | 646,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 88,600.00 USD | 734,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 208.37 USD | 734,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 181.88 USD | 735,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

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
| `Sell Stop` | `0.4015` | 444,330.00 USD | 0.00 USD | 120.45 USD | `-59.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 444,210.00 USD | 0.00 USD | 150.15 USD | `-49.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 444,060.00 USD | 0.00 USD | 781.90 USD | `-28.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 443,280.00 USD | 0.00 USD | 477.38 USD | `-27.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 442,800.00 USD | 0.00 USD | 341.33 USD | `-26.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 442,460.00 USD | 0.00 USD | 972.82 USD | `-26.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 441,490.00 USD | 0.00 USD | 160.20 USD | `-25.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 441,330.00 USD | 0.00 USD | 289.49 USD | `-24.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 441,040.00 USD | 0.00 USD | 14,570.00 USD | `-20.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 426,470.00 USD | 0.00 USD | 274,830.00 USD | `-19.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 151,640.00 USD | 0.00 USD | 405.75 USD | `-17.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 151,230.00 USD | 0.00 USD | 772.84 USD | `-15.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8495` | 150,460.00 USD | 0.00 USD | 3,470.00 USD | `-13.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 146,990.00 USD | 0.00 USD | 9,180.00 USD | `-13.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 137,810.00 USD | 0.00 USD | 341.94 USD | `-13.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 137,470.00 USD | 0.00 USD | 1,150.00 USD | `-13.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 136,320.00 USD | 0.00 USD | 2,020.00 USD | `-12.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 134,300.00 USD | 0.00 USD | 429.25 USD | `-12.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 133,870.00 USD | 0.00 USD | 1,290.00 USD | `-12.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 132,580.00 USD | 0.00 USD | 518.51 USD | `-11.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 132,060.00 USD | 0.00 USD | 223.04 USD | `-9.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 131,840.00 USD | 0.00 USD | 401.86 USD | `-9.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 131,440.00 USD | 0.00 USD | 158.51 USD | `-9.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 131,280.00 USD | 0.00 USD | 498.10 USD | `-9.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 130,780.00 USD | 0.00 USD | 363.40 USD | `-7.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 130,420.00 USD | 0.00 USD | 913.41 USD | `-6.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9275` | 129,510.00 USD | 0.00 USD | 2,120.00 USD | `-5.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9285` | 127,390.00 USD | 0.00 USD | 246.05 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9295` | 127,140.00 USD | 0.00 USD | 776.50 USD | `-5.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9335` | 126,370.00 USD | 0.00 USD | 131.90 USD | `-5.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9365` | 126,230.00 USD | 0.00 USD | 9,680.00 USD | `-4.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9405` | 116,550.00 USD | 0.00 USD | 555.18 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9425` | 115,990.00 USD | 0.00 USD | 145.43 USD | `-4.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9445` | 115,850.00 USD | 0.00 USD | 1,730.00 USD | `-4.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9455` | 114,120.00 USD | 0.00 USD | 383.87 USD | `-3.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9485` | 113,740.00 USD | 0.00 USD | 634.74 USD | `-3.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9525` | 113,100.00 USD | 0.00 USD | 381.00 USD | `-3.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9555` | 112,720.00 USD | 0.00 USD | 3,900.00 USD | `-2.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9565` | 108,830.00 USD | 0.00 USD | 473.56 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9575` | 108,350.00 USD | 0.00 USD | 166.41 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9605` | 108,190.00 USD | 0.00 USD | 376.80 USD | `-2.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9625` | 107,810.00 USD | 0.00 USD | 1,910.00 USD | `-2.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9635` | 105,900.00 USD | 0.00 USD | 568.75 USD | `-2.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9645` | 105,330.00 USD | 0.00 USD | 163.29 USD | `-2.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9665` | 105,170.00 USD | 0.00 USD | 554.58 USD | `-1.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9675` | 104,620.00 USD | 0.00 USD | 385.74 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9685` | 104,230.00 USD | 0.00 USD | 153.22 USD | `-1.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9695` | 104,080.00 USD | 0.00 USD | 22,800.00 USD | `-1.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9705` | 81,280.00 USD | 0.00 USD | 11,230.00 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9715` | 70,050.00 USD | 0.00 USD | 10,370.00 USD | `-1.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9725` | 59,680.00 USD | 0.00 USD | 387.83 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9735` | 59,290.00 USD | 0.00 USD | 7,630.00 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9745` | 51,660.00 USD | 0.00 USD | 8,750.00 USD | `-1.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9755` | 42,910.00 USD | 0.00 USD | 21,960.00 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9765` | 20,950.00 USD | 0.00 USD | 396.17 USD | `-0.81%` | `TACTICAL (Retail Cluster)` |
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
| `Buy Stop` | `0.9935` | 140,680.00 USD | 403.06 USD | 0.00 USD | `+0.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 141,460.00 USD | 782.07 USD | 0.00 USD | `+1.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 141,870.00 USD | 403.28 USD | 0.00 USD | `+1.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 145,270.00 USD | 3,400.00 USD | 0.00 USD | `+1.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 150,410.00 USD | 5,140.00 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 187,720.00 USD | 37,310.00 USD | 0.00 USD | `+1.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 188,720.00 USD | 1,000.00 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 229,320.00 USD | 40,590.00 USD | 0.00 USD | `+1.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 229,550.00 USD | 235.79 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 230,900.00 USD | 1,340.00 USD | 0.00 USD | `+1.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 231,130.00 USD | 230.39 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 232,130.00 USD | 1,000.00 USD | 0.00 USD | `+2.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 232,540.00 USD | 409.86 USD | 0.00 USD | `+2.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 232,740.00 USD | 198.46 USD | 0.00 USD | `+2.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 233,350.00 USD | 615.60 USD | 0.00 USD | `+2.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 236,810.00 USD | 3,460.00 USD | 0.00 USD | `+2.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 237,370.00 USD | 561.17 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 237,470.00 USD | 103.07 USD | 0.00 USD | `+3.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 237,880.00 USD | 401.26 USD | 0.00 USD | `+3.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 238,680.00 USD | 804.09 USD | 0.00 USD | `+3.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 238,880.00 USD | 201.52 USD | 0.00 USD | `+4.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 239,090.00 USD | 207.97 USD | 0.00 USD | `+4.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 239,290.00 USD | 201.60 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 239,390.00 USD | 101.51 USD | 0.00 USD | `+4.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 239,600.00 USD | 208.26 USD | 0.00 USD | `+4.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 240,120.00 USD | 516.75 USD | 0.00 USD | `+4.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 240,320.00 USD | 204.93 USD | 0.00 USD | `+5.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 240,670.00 USD | 348.86 USD | 0.00 USD | `+5.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 241,080.00 USD | 413.76 USD | 0.00 USD | `+5.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 241,440.00 USD | 354.91 USD | 0.00 USD | `+5.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 243,340.00 USD | 1,900.00 USD | 0.00 USD | `+5.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 243,550.00 USD | 207.87 USD | 0.00 USD | `+5.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 243,760.00 USD | 207.97 USD | 0.00 USD | `+5.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 245,050.00 USD | 1,290.00 USD | 0.00 USD | `+6.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 245,260.00 USD | 206.97 USD | 0.00 USD | `+6.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 245,370.00 USD | 107.99 USD | 0.00 USD | `+6.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 245,620.00 USD | 247.60 USD | 0.00 USD | `+7.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 320,450.00 USD | 74,840.00 USD | 0.00 USD | `+7.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 321,000.00 USD | 544.88 USD | 0.00 USD | `+8.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 321,150.00 USD | 157.10 USD | 0.00 USD | `+9.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 323,330.00 USD | 2,170.00 USD | 0.00 USD | `+10.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 324,860.00 USD | 1,540.00 USD | 0.00 USD | `+10.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 334,790.00 USD | 9,930.00 USD | 0.00 USD | `+11.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 335,760.00 USD | 976.36 USD | 0.00 USD | `+11.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 336,640.00 USD | 877.63 USD | 0.00 USD | `+12.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 336,810.00 USD | 171.50 USD | 0.00 USD | `+12.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 336,990.00 USD | 171.09 USD | 0.00 USD | `+13.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 339,760.00 USD | 2,770.00 USD | 0.00 USD | `+14.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 341,790.00 USD | 2,040.00 USD | 0.00 USD | `+14.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 344,460.00 USD | 2,670.00 USD | 0.00 USD | `+15.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 344,610.00 USD | 151.03 USD | 0.00 USD | `+16.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 344,760.00 USD | 151.16 USD | 0.00 USD | `+16.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 344,910.00 USD | 151.29 USD | 0.00 USD | `+16.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 345,060.00 USD | 151.42 USD | 0.00 USD | `+16.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 345,220.00 USD | 151.55 USD | 0.00 USD | `+17.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 345,370.00 USD | 151.69 USD | 0.00 USD | `+17.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 347,420.00 USD | 2,050.00 USD | 0.00 USD | `+18.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 347,530.00 USD | 110.00 USD | 0.00 USD | `+19.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 347,760.00 USD | 237.90 USD | 0.00 USD | `+20.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 348,970.00 USD | 1,210.00 USD | 0.00 USD | `+21.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 391,900.00 USD | 42,930.00 USD | 0.00 USD | `+22.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 393,900.00 USD | 2,000.00 USD | 0.00 USD | `+25.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 395,290.00 USD | 1,380.00 USD | 0.00 USD | `+27.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 395,530.00 USD | 245.41 USD | 0.00 USD | `+29.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 402,880.00 USD | 7,350.00 USD | 0.00 USD | `+31.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 403,300.00 USD | 415.25 USD | 0.00 USD | `+32.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 409,810.00 USD | 6,520.00 USD | 0.00 USD | `+32.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 866,800.00 USD | 456,990.00 USD | 0.00 USD | `+33.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 867,460.00 USD | 655.75 USD | 0.00 USD | `+33.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 869,270.00 USD | 1,810.00 USD | 0.00 USD | `+36.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 883,150.00 USD | 13,880.00 USD | 0.00 USD | `+36.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 884,410.00 USD | 1,250.00 USD | 0.00 USD | `+37.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 886,470.00 USD | 2,070.00 USD | 0.00 USD | `+41.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 886,610.00 USD | 140.05 USD | 0.00 USD | `+42.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 886,770.00 USD | 160.42 USD | 0.00 USD | `+42.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 887,370.00 USD | 598.33 USD | 0.00 USD | `+43.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 921,550.00 USD | 34,170.00 USD | 0.00 USD | `+45.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 922,430.00 USD | 879.84 USD | 0.00 USD | `+51.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 923,020.00 USD | 590.88 USD | 0.00 USD | `+52.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 926,070.00 USD | 3,050.00 USD | 0.00 USD | `+53.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 926,370.00 USD | 297.27 USD | 0.00 USD | `+57.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 934,900.00 USD | 8,530.00 USD | 0.00 USD | `+67.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 935,040.00 USD | 143.99 USD | 0.00 USD | `+69.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 935,220.00 USD | 177.05 USD | 0.00 USD | `+79.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 935,650.00 USD | 431.40 USD | 0.00 USD | `+82.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 940,760.00 USD | 5,100.00 USD | 0.00 USD | `+93.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 943,240.00 USD | 2,480.00 USD | 0.00 USD | `+94.06%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.7920` | 491,830.00 USD | 0.00 USD | 491,830.00 USD | 6,470.00 USD | 1,650.00 USD | 5,060.00 USD |
| `7D` | `0.7920` | 559,290.00 USD | 0.00 USD | 559,290.00 USD | 6,470.00 USD | 1,650.00 USD | 5,060.00 USD |
| `1D` | `0.7940` | 478,650.00 USD | 0.00 USD | 478,650.00 USD | 1,860.00 USD | 595.59 USD | 965.49 USD |
| `7D` | `0.7940` | 546,110.00 USD | 0.00 USD | 546,110.00 USD | 1,860.00 USD | 595.59 USD | 965.49 USD |
| `1D` | `0.7960` | 475,230.00 USD | 0.00 USD | 475,230.00 USD | 222.45 USD | 2,470.00 USD | 1,060.00 USD |
| `7D` | `0.7960` | 542,690.00 USD | 0.00 USD | 542,690.00 USD | 222.45 USD | 2,470.00 USD | 1,060.00 USD |
| `1D` | `0.7980` | 471,480.00 USD | 0.00 USD | 471,480.00 USD | 1,140.00 USD | 22.38 USD | 494.59 USD |
| `7D` | `0.7980` | 538,940.00 USD | 0.00 USD | 538,940.00 USD | 1,140.00 USD | 22.38 USD | 494.59 USD |
| `1D` | `0.8000` | 469,820.00 USD | 0.00 USD | 469,820.00 USD | 7.83 USD | 5.00 USD | 1,200.00 USD |
| `7D` | `0.8000` | 537,280.00 USD | 0.00 USD | 537,280.00 USD | 7.83 USD | 5.00 USD | 1,200.00 USD |
| `1D` | `0.8020` | 468,610.00 USD | 0.00 USD | 468,610.00 USD | 2,290.00 USD | 1,600.00 USD | 2,110.00 USD |
| `7D` | `0.8020` | 536,070.00 USD | 0.00 USD | 536,070.00 USD | 2,290.00 USD | 1,600.00 USD | 2,110.00 USD |
| `1D` | `0.8040` | 462,600.00 USD | 0.00 USD | 462,600.00 USD | 813.73 USD | 993.93 USD | 952.73 USD |
| `7D` | `0.8040` | 530,060.00 USD | 0.00 USD | 530,060.00 USD | 813.73 USD | 993.93 USD | 952.73 USD |
| `1D` | `0.8060` | 459,840.00 USD | 0.00 USD | 459,840.00 USD | 536.61 USD | 845.93 USD | 53.10 USD |
| `7D` | `0.8060` | 527,300.00 USD | 0.00 USD | 527,300.00 USD | 536.61 USD | 845.93 USD | 53.10 USD |
| `1D` | `0.8080` | 458,410.00 USD | 0.00 USD | 458,410.00 USD | 4,130.00 USD | 657.69 USD | 1,790.00 USD |
| `7D` | `0.8080` | 525,870.00 USD | 0.00 USD | 525,870.00 USD | 4,130.00 USD | 657.69 USD | 1,790.00 USD |
| `1D` | `0.8100` | 451,830.00 USD | 0.00 USD | 451,830.00 USD | 1,940.00 USD | 14.30 USD | 3,540.00 USD |
| `7D` | `0.8100` | 519,290.00 USD | 0.00 USD | 519,290.00 USD | 1,940.00 USD | 14.30 USD | 3,540.00 USD |
| `1D` | `0.8120` | 446,330.00 USD | 0.00 USD | 446,330.00 USD | 821.06 USD | 258.31 USD | 44.49 USD |
| `7D` | `0.8120` | 513,800.00 USD | 0.00 USD | 513,800.00 USD | 821.06 USD | 258.31 USD | 44.49 USD |
| `1D` | `0.8140` | 445,210.00 USD | 0.00 USD | 445,210.00 USD | 4,760.00 USD | 30.50 USD | 796.05 USD |
| `7D` | `0.8140` | 512,670.00 USD | 0.00 USD | 512,670.00 USD | 4,760.00 USD | 30.50 USD | 796.05 USD |
| `1D` | `0.8160` | 439,630.00 USD | 0.00 USD | 439,630.00 USD | 0.00 USD | 182.45 USD | 26.89 USD |
| `7D` | `0.8160` | 507,090.00 USD | 0.00 USD | 507,090.00 USD | 0.00 USD | 182.45 USD | 26.89 USD |
| `1D` | `0.8180` | 439,420.00 USD | 0.00 USD | 439,420.00 USD | 99.55 USD | 6.25 USD | 96.08 USD |
| `7D` | `0.8180` | 506,880.00 USD | 0.00 USD | 506,880.00 USD | 9,320.00 USD | 6.25 USD | 96.08 USD |
| `1D` | `0.8200` | 439,220.00 USD | 0.00 USD | 439,220.00 USD | 1,260.00 USD | 0.00 USD | 435.27 USD |
| `7D` | `0.8200` | 497,460.00 USD | 0.00 USD | 497,460.00 USD | 1,260.00 USD | 0.00 USD | 435.27 USD |
| `1D` | `0.8220` | 437,520.00 USD | 0.00 USD | 437,520.00 USD | 0.00 USD | 0.00 USD | 471.94 USD |
| `7D` | `0.8220` | 495,760.00 USD | 0.00 USD | 495,760.00 USD | 0.00 USD | 0.00 USD | 471.94 USD |
| `1D` | `0.8240` | 437,050.00 USD | 0.00 USD | 437,050.00 USD | 0.00 USD | 3,640.00 USD | 6,790.00 USD |
| `7D` | `0.8240` | 495,290.00 USD | 0.00 USD | 495,290.00 USD | 0.00 USD | 3,640.00 USD | 6,790.00 USD |
| `1D` | `0.8400` | 426,610.00 USD | 0.00 USD | 426,610.00 USD | 458.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8400` | 484,850.00 USD | 0.00 USD | 484,850.00 USD | 458.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8420` | 426,150.00 USD | 0.00 USD | 426,150.00 USD | 0.00 USD | 149.63 USD | 0.00 USD |
| `7D` | `0.8420` | 484,390.00 USD | 0.00 USD | 484,390.00 USD | 0.00 USD | 149.63 USD | 0.00 USD |
| `7D` | `0.8440` | 484,240.00 USD | 0.00 USD | 484,240.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8500` | 426,000.00 USD | 0.00 USD | 426,000.00 USD | 421.90 USD | 61.55 USD | 206.79 USD |
| `7D` | `0.8500` | 482,290.00 USD | 0.00 USD | 482,290.00 USD | 421.90 USD | 61.55 USD | 206.79 USD |
| `1D` | `0.8520` | 425,310.00 USD | 0.00 USD | 425,310.00 USD | 0.00 USD | 1,940.00 USD | 2,470.00 USD |
| `7D` | `0.8520` | 481,600.00 USD | 0.00 USD | 481,600.00 USD | 0.00 USD | 1,940.00 USD | 2,470.00 USD |
| `1D` | `0.8560` | 420,910.00 USD | 0.00 USD | 420,910.00 USD | 0.00 USD | 199.60 USD | 0.00 USD |
| `7D` | `0.8560` | 477,190.00 USD | 0.00 USD | 477,190.00 USD | 0.00 USD | 199.60 USD | 0.00 USD |
| `1D` | `0.8580` | 420,710.00 USD | 0.00 USD | 420,710.00 USD | 250.65 USD | 0.00 USD | 182.69 USD |
| `7D` | `0.8580` | 476,990.00 USD | 0.00 USD | 476,990.00 USD | 250.65 USD | 0.00 USD | 182.69 USD |
| `1D` | `0.8600` | 420,270.00 USD | 0.00 USD | 420,270.00 USD | 3,240.00 USD | 1,030.00 USD | 251.39 USD |
| `7D` | `0.8600` | 476,550.00 USD | 0.00 USD | 476,550.00 USD | 5,860.00 USD | 1,030.00 USD | 251.39 USD |
| `1D` | `0.8620` | 415,740.00 USD | 0.00 USD | 415,740.00 USD | 7,410.00 USD | 24.95 USD | 0.00 USD |
| `7D` | `0.8620` | 469,410.00 USD | 0.00 USD | 469,410.00 USD | 7,410.00 USD | 24.95 USD | 0.00 USD |
| `1D` | `0.8640` | 408,300.00 USD | 0.00 USD | 408,300.00 USD | 5,790.00 USD | 1,940.00 USD | 3,790.00 USD |
| `7D` | `0.8640` | 461,970.00 USD | 0.00 USD | 461,970.00 USD | 5,790.00 USD | 1,940.00 USD | 3,790.00 USD |
| `1D` | `0.8660` | 396,780.00 USD | 0.00 USD | 396,780.00 USD | 0.00 USD | 20.18 USD | 0.00 USD |
| `7D` | `0.8660` | 450,450.00 USD | 0.00 USD | 450,450.00 USD | 0.00 USD | 20.18 USD | 0.00 USD |
| `1D` | `0.8680` | 396,760.00 USD | 0.00 USD | 396,760.00 USD | 3,320.00 USD | 3,550.00 USD | 8,720.00 USD |
| `7D` | `0.8680` | 450,430.00 USD | 0.00 USD | 450,430.00 USD | 3,320.00 USD | 3,550.00 USD | 8,720.00 USD |
| `1D` | `0.8700` | 381,170.00 USD | 0.00 USD | 381,170.00 USD | 15,620.00 USD | 3,580.00 USD | 4,760.00 USD |
| `7D` | `0.8700` | 434,840.00 USD | 0.00 USD | 434,840.00 USD | 15,620.00 USD | 3,580.00 USD | 4,760.00 USD |
| `1D` | `0.8720` | 357,210.00 USD | 0.00 USD | 357,210.00 USD | 9,180.00 USD | 26.70 USD | 6,210.00 USD |
| `7D` | `0.8720` | 410,880.00 USD | 0.00 USD | 410,880.00 USD | 32,240.00 USD | 26.70 USD | 6,210.00 USD |
| `1D` | `0.8740` | 341,790.00 USD | 0.00 USD | 341,790.00 USD | 6,780.00 USD | 3,080.00 USD | 3,030.00 USD |
| `7D` | `0.8740` | 372,400.00 USD | 0.00 USD | 372,400.00 USD | 6,780.00 USD | 3,080.00 USD | 3,030.00 USD |
| `1D` | `0.8760` | 328,890.00 USD | 0.00 USD | 328,890.00 USD | 6,140.00 USD | 3,510.00 USD | 4,390.00 USD |
| `7D` | `0.8760` | 359,510.00 USD | 0.00 USD | 359,510.00 USD | 6,140.00 USD | 3,510.00 USD | 4,390.00 USD |
| `1D` | `0.8780` | 314,850.00 USD | 0.00 USD | 314,850.00 USD | 15,310.00 USD | 15,510.00 USD | 27,090.00 USD |
| `7D` | `0.8780` | 345,460.00 USD | 0.00 USD | 345,460.00 USD | 15,310.00 USD | 15,510.00 USD | 27,090.00 USD |
| `1D` | `0.8800` | 256,930.00 USD | 0.00 USD | 256,930.00 USD | 12,000.00 USD | 5,110.00 USD | 5,490.00 USD |
| `7D` | `0.8800` | 287,550.00 USD | 0.00 USD | 287,550.00 USD | 12,000.00 USD | 5,110.00 USD | 5,490.00 USD |
| `1D` | `0.8820` | 234,340.00 USD | 0.00 USD | 234,340.00 USD | 8,950.00 USD | 4,070.00 USD | 150.13 USD |
| `7D` | `0.8820` | 264,960.00 USD | 0.00 USD | 264,960.00 USD | 8,950.00 USD | 4,070.00 USD | 150.13 USD |
| `1D` | `0.8840` | 221,170.00 USD | 0.00 USD | 221,170.00 USD | 7,440.00 USD | 1,810.00 USD | 1,030.00 USD |
| `7D` | `0.8840` | 251,780.00 USD | 0.00 USD | 251,780.00 USD | 7,440.00 USD | 1,810.00 USD | 1,030.00 USD |
| `1D` | `0.8860` | 210,890.00 USD | 0.00 USD | 210,890.00 USD | 5,930.00 USD | 1,700.00 USD | 8,190.00 USD |
| `7D` | `0.8860` | 241,510.00 USD | 0.00 USD | 241,510.00 USD | 5,930.00 USD | 1,700.00 USD | 8,190.00 USD |
| `1D` | `0.8880` | 195,080.00 USD | 0.00 USD | 195,080.00 USD | 17,470.00 USD | 4,160.00 USD | 9,760.00 USD |
| `7D` | `0.8880` | 225,690.00 USD | 0.00 USD | 225,690.00 USD | 17,470.00 USD | 4,160.00 USD | 9,760.00 USD |
| `1D` | `0.8900` | 163,690.00 USD | 0.00 USD | 163,690.00 USD | 4,010.00 USD | 4,210.00 USD | 4,990.00 USD |
| `7D` | `0.8900` | 194,300.00 USD | 0.00 USD | 194,300.00 USD | 50,120.00 USD | 4,210.00 USD | 4,990.00 USD |
| `1D` | `0.8920` | 150,470.00 USD | 0.00 USD | 150,470.00 USD | 4,920.00 USD | 3,110.00 USD | 1,950.00 USD |
| `7D` | `0.8920` | 134,970.00 USD | 0.00 USD | 134,970.00 USD | 4,920.00 USD | 3,110.00 USD | 1,950.00 USD |
| `1D` | `0.8940` | 140,490.00 USD | 0.00 USD | 140,490.00 USD | 4,240.00 USD | 0.00 USD | 966.50 USD |
| `7D` | `0.8940` | 124,990.00 USD | 0.00 USD | 124,990.00 USD | 4,240.00 USD | 0.00 USD | 966.50 USD |
| `1D` | `0.8960` | 135,280.00 USD | 0.00 USD | 135,280.00 USD | 1,930.00 USD | 15,480.00 USD | 6,550.00 USD |
| `7D` | `0.8960` | 119,780.00 USD | 0.00 USD | 119,780.00 USD | 1,930.00 USD | 15,480.00 USD | 6,550.00 USD |
| `1D` | `0.8980` | 111,320.00 USD | 0.00 USD | 111,320.00 USD | 21,610.00 USD | 10,780.00 USD | 32,910.00 USD |
| `7D` | `0.8980` | 95,820.00 USD | 0.00 USD | 95,820.00 USD | 21,610.00 USD | 10,780.00 USD | 32,910.00 USD |
| `1D` | `0.9000` | 46,020.00 USD | 0.00 USD | 46,020.00 USD | 3,760.00 USD | 720.16 USD | 2,370.00 USD |
| `7D` | `0.9000` | 30,520.00 USD | 0.00 USD | 30,520.00 USD | 3,760.00 USD | 720.16 USD | 2,370.00 USD |
| `1D` | `0.9020` | 39,160.00 USD | 0.00 USD | 39,160.00 USD | 4,420.00 USD | 3,120.00 USD | 2,240.00 USD |
| `7D` | `0.9020` | 23,670.00 USD | 0.00 USD | 23,670.00 USD | 4,420.00 USD | 3,120.00 USD | 2,240.00 USD |
| `1D` | `0.9040` | 29,380.00 USD | 0.00 USD | 29,380.00 USD | 3,360.00 USD | 2,430.00 USD | 5,710.00 USD |
| `7D` | `0.9040` | 13,890.00 USD | 0.00 USD | 13,890.00 USD | 1,580.00 USD | 2,430.00 USD | 5,710.00 USD |
| `1D` | `0.9060` | 17,880.00 USD | 0.00 USD | 17,880.00 USD | 10,120.00 USD | 1,620.00 USD | 0.00 USD |
| `7D` | `0.9060` | 4,160.00 USD | 0.00 USD | 4,160.00 USD | 0.00 USD | 1,620.00 USD | 0.00 USD |
| `1D` | `0.9080` | 6,140.00 USD | 0.00 USD | 6,140.00 USD | 5,800.00 USD | 346.80 USD | 0.00 USD |
| `7D` | `0.9080` | 2,550.00 USD | 0.00 USD | 2,550.00 USD | 0.00 USD | 346.80 USD | 0.00 USD |
| `1D` | `0.9090` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9100` | 4,690.00 USD | 4,690.00 USD | 0.00 USD | 3,880.00 USD | 815.15 USD | 0.00 USD |
| `7D` | `0.9100` | 2,200.00 USD | 0.00 USD | 2,200.00 USD | 1,380.00 USD | 815.15 USD | 0.00 USD |
| `1D` | `0.9120` | 6,990.00 USD | 6,990.00 USD | 0.00 USD | 1,980.00 USD | 315.61 USD | 0.00 USD |
| `7D` | `0.9120` | 2,290.00 USD | 2,290.00 USD | 0.00 USD | 1,980.00 USD | 315.61 USD | 0.00 USD |
| `7D` | `0.9120` | 4,590.00 USD | 4,590.00 USD | 0.00 USD | 1,980.00 USD | 315.61 USD | 0.00 USD |
| `1D` | `0.9140` | 9,030.00 USD | 9,030.00 USD | 0.00 USD | 1,840.00 USD | 200.33 USD | 0.00 USD |
| `7D` | `0.9140` | 6,630.00 USD | 6,630.00 USD | 0.00 USD | 1,840.00 USD | 200.33 USD | 0.00 USD |
| `1D` | `0.9160` | 14,860.00 USD | 14,860.00 USD | 0.00 USD | 5,700.00 USD | 131.45 USD | 0.00 USD |
| `7D` | `0.9160` | 12,460.00 USD | 12,460.00 USD | 0.00 USD | 5,700.00 USD | 131.45 USD | 0.00 USD |
| `1D` | `0.9180` | 15,480.00 USD | 15,480.00 USD | 0.00 USD | 485.63 USD | 132.34 USD | 0.00 USD |
| `7D` | `0.9180` | 13,080.00 USD | 13,080.00 USD | 0.00 USD | 485.63 USD | 132.34 USD | 0.00 USD |
| `1D` | `0.9200` | 15,640.00 USD | 15,640.00 USD | 0.00 USD | 0.00 USD | 166.12 USD | 0.00 USD |
| `7D` | `0.9200` | 13,240.00 USD | 13,240.00 USD | 0.00 USD | 0.00 USD | 166.12 USD | 0.00 USD |
| `1D` | `0.9220` | 44,100.00 USD | 44,100.00 USD | 0.00 USD | 14,160.00 USD | 77.74 USD | 14,210.00 USD |
| `7D` | `0.9220` | 41,700.00 USD | 41,700.00 USD | 0.00 USD | 14,160.00 USD | 77.74 USD | 14,210.00 USD |
| `1D` | `0.9240` | 53,110.00 USD | 53,110.00 USD | 0.00 USD | 7,970.00 USD | 1,040.00 USD | 0.00 USD |
| `7D` | `0.9240` | 50,710.00 USD | 50,710.00 USD | 0.00 USD | 7,970.00 USD | 1,040.00 USD | 0.00 USD |
| `1D` | `0.9260` | 99,060.00 USD | 99,060.00 USD | 0.00 USD | 6,310.00 USD | 1,100.00 USD | 38,550.00 USD |
| `7D` | `0.9260` | 142,770.00 USD | 142,770.00 USD | 0.00 USD | 52,420.00 USD | 1,100.00 USD | 38,550.00 USD |
| `1D` | `0.9280` | 160,130.00 USD | 160,130.00 USD | 0.00 USD | 47,790.00 USD | 145.20 USD | 13,130.00 USD |
| `7D` | `0.9280` | 203,840.00 USD | 203,840.00 USD | 0.00 USD | 47,790.00 USD | 145.20 USD | 13,130.00 USD |
| `1D` | `0.9300` | 204,940.00 USD | 204,940.00 USD | 0.00 USD | 21,640.00 USD | 221.69 USD | 22,950.00 USD |
| `7D` | `0.9300` | 248,650.00 USD | 248,650.00 USD | 0.00 USD | 21,640.00 USD | 221.69 USD | 22,950.00 USD |
| `1D` | `0.9320` | 252,790.00 USD | 252,790.00 USD | 0.00 USD | 26,400.00 USD | 7,580.00 USD | 13,880.00 USD |
| `7D` | `0.9320` | 296,500.00 USD | 296,500.00 USD | 0.00 USD | 26,400.00 USD | 7,580.00 USD | 13,880.00 USD |
| `1D` | `0.9340` | 342,620.00 USD | 342,620.00 USD | 0.00 USD | 35,410.00 USD | 10,860.00 USD | 43,550.00 USD |
| `7D` | `0.9340` | 386,330.00 USD | 386,330.00 USD | 0.00 USD | 35,410.00 USD | 10,860.00 USD | 43,550.00 USD |
| `1D` | `0.9360` | 427,160.00 USD | 427,160.00 USD | 0.00 USD | 64,130.00 USD | 475.50 USD | 19,940.00 USD |
| `7D` | `0.9360` | 470,870.00 USD | 470,870.00 USD | 0.00 USD | 64,130.00 USD | 475.50 USD | 19,940.00 USD |
| `1D` | `0.9380` | 484,040.00 USD | 484,040.00 USD | 0.00 USD | 56,080.00 USD | 103.28 USD | 695.88 USD |
| `7D` | `0.9380` | 527,750.00 USD | 527,750.00 USD | 0.00 USD | 56,080.00 USD | 103.28 USD | 695.88 USD |
| `1D` | `0.9400` | 528,400.00 USD | 528,400.00 USD | 0.00 USD | 41,740.00 USD | 0.00 USD | 2,620.00 USD |
| `7D` | `0.9400` | 572,110.00 USD | 572,110.00 USD | 0.00 USD | 41,740.00 USD | 0.00 USD | 2,620.00 USD |
| `1D` | `0.9420` | 585,870.00 USD | 585,870.00 USD | 0.00 USD | 57,470.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9420` | 629,580.00 USD | 629,580.00 USD | 0.00 USD | 57,470.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9440` | 621,130.00 USD | 621,130.00 USD | 0.00 USD | 35,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9440` | 687,890.00 USD | 687,890.00 USD | 0.00 USD | 58,310.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9460` | 667,060.00 USD | 667,060.00 USD | 0.00 USD | 45,730.00 USD | 199.60 USD | 0.00 USD |
| `7D` | `0.9460` | 733,820.00 USD | 733,820.00 USD | 0.00 USD | 45,730.00 USD | 199.60 USD | 0.00 USD |
| `1D` | `0.9480` | 812,540.00 USD | 812,540.00 USD | 0.00 USD | 145,470.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9480` | 879,300.00 USD | 879,300.00 USD | 0.00 USD | 145,470.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9500` | 871,710.00 USD | 871,710.00 USD | 0.00 USD | 56,840.00 USD | 105.68 USD | 2,230.00 USD |
| `7D` | `0.9500` | 941,090.00 USD | 941,090.00 USD | 0.00 USD | 59,460.00 USD | 105.68 USD | 2,230.00 USD |
| `1D` | `0.9520` | 948,080.00 USD | 948,080.00 USD | 0.00 USD | 37,660.00 USD | 13,410.00 USD | 25,300.00 USD |
| `7D` | `0.9520` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 37,660.00 USD | 13,410.00 USD | 25,300.00 USD |
| `1D` | `0.9540` | 986,530.00 USD | 986,530.00 USD | 0.00 USD | 8,940.00 USD | 394.58 USD | 29,110.00 USD |
| `7D` | `0.9540` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 8,940.00 USD | 394.58 USD | 29,110.00 USD |
| `1D` | `0.9560` | 987,390.00 USD | 987,390.00 USD | 0.00 USD | 865.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9560` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 865.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9580` | 987,700.00 USD | 987,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 313.25 USD |
| `7D` | `0.9580` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 313.25 USD |
| `1D` | `0.9620` | 987,850.00 USD | 987,850.00 USD | 0.00 USD | 0.00 USD | 149.63 USD | 0.00 USD |
| `7D` | `0.9620` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 149.63 USD | 0.00 USD |
| `1D` | `0.9640` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 9,690.00 USD | 13,390.00 USD |
| `7D` | `0.9640` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 9,690.00 USD | 13,390.00 USD |
| `1D` | `0.9660` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 595.80 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9660` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 2,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9700` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 2,050.00 USD | 10,450.00 USD |
| `7D` | `0.9700` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 2,050.00 USD | 10,450.00 USD |
| `1D` | `0.9720` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 23,620.00 USD | 0.00 USD | 23,100.00 USD |
| `7D` | `0.9720` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 23,620.00 USD | 0.00 USD | 23,100.00 USD |
| `1D` | `0.9740` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 25,800.00 USD | 5,170.00 USD | 14,840.00 USD |
| `7D` | `0.9740` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 25,800.00 USD | 5,170.00 USD | 14,840.00 USD |
| `1D` | `0.9760` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 50,870.00 USD | 13,960.00 USD | 8,400.00 USD |
| `7D` | `0.9760` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 50,870.00 USD | 13,960.00 USD | 8,400.00 USD |
| `1D` | `0.9780` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 37,710.00 USD | 2,960.00 USD | 17,920.00 USD |
| `7D` | `0.9780` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 37,710.00 USD | 2,960.00 USD | 17,920.00 USD |
| `1D` | `0.9800` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 29,240.00 USD | 9,580.00 USD | 20,800.00 USD |
| `7D` | `0.9800` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 29,240.00 USD | 9,580.00 USD | 20,800.00 USD |
| `1D` | `0.9820` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 15,980.00 USD | 12,160.00 USD | 7,390.00 USD |
| `7D` | `0.9820` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 15,980.00 USD | 12,160.00 USD | 7,390.00 USD |
| `1D` | `0.9840` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 13,190.00 USD | 38,710.00 USD |
| `7D` | `0.9840` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 13,190.00 USD | 38,710.00 USD |
| `1D` | `0.9860` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 50,550.00 USD | 3,460.00 USD | 19,890.00 USD |
| `7D` | `0.9860` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 50,550.00 USD | 3,460.00 USD | 19,890.00 USD |
| `1D` | `0.9880` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 16,640.00 USD | 0.00 USD | 14,320.00 USD |
| `7D` | `0.9880` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 16,640.00 USD | 0.00 USD | 14,320.00 USD |
| `1D` | `0.9900` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 57,390.00 USD | 1,300.00 USD | 13,390.00 USD |
| `7D` | `0.9900` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 57,390.00 USD | 1,300.00 USD | 13,390.00 USD |
| `1D` | `0.9920` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 8,950.00 USD | 2,810.00 USD | 13,340.00 USD |
| `7D` | `0.9920` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 8,950.00 USD | 2,810.00 USD | 13,340.00 USD |
| `1D` | `0.9940` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 12,310.00 USD | 13,250.00 USD | 1,420.00 USD |
| `7D` | `0.9940` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 12,310.00 USD | 13,250.00 USD | 1,420.00 USD |
| `1D` | `0.9960` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 18,530.00 USD | 4,110.00 USD | 0.00 USD |
| `7D` | `0.9960` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 18,530.00 USD | 4,110.00 USD | 0.00 USD |
| `1D` | `0.9980` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 40,410.00 USD | 4,790.00 USD | 10,500.00 USD |
| `7D` | `0.9980` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 40,410.00 USD | 4,790.00 USD | 10,500.00 USD |
| `1D` | `1.00` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 50,740.00 USD | 31,440.00 USD | 1,710.00 USD |
| `7D` | `1.00` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 59,960.00 USD | 31,440.00 USD | 1,710.00 USD |
| `1D` | `1.00` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 501.30 USD | 0.00 USD | 266.05 USD |
| `7D` | `1.00` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 501.30 USD | 0.00 USD | 266.05 USD |
| `1D` | `1.00` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 10,110.00 USD | 9,540.00 USD | 9,410.00 USD |
| `7D` | `1.00` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 10,110.00 USD | 9,540.00 USD | 9,410.00 USD |
| `1D` | `1.01` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 101,040.00 USD | 10,140.00 USD | 31,440.00 USD |
| `7D` | `1.01` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 101,040.00 USD | 10,140.00 USD | 31,440.00 USD |
| `1D` | `1.01` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 9,210.00 USD | 9,160.00 USD | 27,730.00 USD |
| `7D` | `1.01` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 9,210.00 USD | 9,160.00 USD | 27,730.00 USD |
| `1D` | `1.01` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 10,530.00 USD | 8,790.00 USD | 0.00 USD |
| `7D` | `1.01` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 10,530.00 USD | 8,790.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 16,240.00 USD | 25,350.00 USD | 155.80 USD |
| `7D` | `1.01` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 16,240.00 USD | 25,350.00 USD | 155.80 USD |
| `1D` | `1.01` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 5,950.00 USD | 4,370.00 USD | 25,020.00 USD |
| `7D` | `1.01` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 5,950.00 USD | 4,370.00 USD | 25,020.00 USD |
| `1D` | `1.02` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 20,120.00 USD | 75.20 USD | 20,270.00 USD |
| `7D` | `1.02` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 20,120.00 USD | 75.20 USD | 20,270.00 USD |
| `1D` | `1.02` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 6,670.00 USD | 8,490.00 USD | 22,230.00 USD |
| `7D` | `1.02` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 6,670.00 USD | 8,490.00 USD | 22,230.00 USD |
| `1D` | `1.02` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 44,710.00 USD | 4,370.00 USD | 15,110.00 USD |
| `7D` | `1.02` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 44,710.00 USD | 4,370.00 USD | 15,110.00 USD |
| `1D` | `1.02` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 51,380.00 USD | 3,710.00 USD | 21,450.00 USD |
| `7D` | `1.02` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 51,380.00 USD | 3,710.00 USD | 21,450.00 USD |
| `1D` | `1.02` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 50,330.00 USD | 25,640.00 USD | 53,210.00 USD |
| `7D` | `1.02` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 50,330.00 USD | 25,640.00 USD | 53,210.00 USD |
| `1D` | `1.03` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 52,630.00 USD | 18,370.00 USD | 20,210.00 USD |
| `7D` | `1.03` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 52,630.00 USD | 18,370.00 USD | 20,210.00 USD |
| `1D` | `1.03` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 31,340.00 USD | 10,940.00 USD | 18,480.00 USD |
| `7D` | `1.03` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 31,340.00 USD | 10,940.00 USD | 18,480.00 USD |
| `1D` | `1.03` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 95,330.00 USD | 24,510.00 USD | 33,610.00 USD |
| `7D` | `1.03` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 95,330.00 USD | 24,510.00 USD | 33,610.00 USD |
| `1D` | `1.03` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 70,060.00 USD | 8,980.00 USD | 35,950.00 USD |
| `7D` | `1.03` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 70,060.00 USD | 8,980.00 USD | 35,950.00 USD |
| `1D` | `1.03` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 38,330.00 USD | 9,300.00 USD | 21,490.00 USD |
| `7D` | `1.03` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 38,330.00 USD | 9,300.00 USD | 21,490.00 USD |
| `1D` | `1.04` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 18,100.00 USD | 13,840.00 USD | 7,800.00 USD |
| `7D` | `1.04` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 18,100.00 USD | 13,840.00 USD | 7,800.00 USD |
| `1D` | `1.04` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 63,010.00 USD | 3,250.00 USD | 4,330.00 USD |
| `7D` | `1.04` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 63,010.00 USD | 3,250.00 USD | 4,330.00 USD |
| `1D` | `1.04` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 7,790.00 USD | 10,040.00 USD | 12,300.00 USD |
| `7D` | `1.04` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 7,790.00 USD | 10,040.00 USD | 12,300.00 USD |
| `1D` | `1.04` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 11,290.00 USD | 9,870.00 USD | 8,370.00 USD |
| `7D` | `1.04` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 11,290.00 USD | 9,870.00 USD | 8,370.00 USD |
| `1D` | `1.04` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 7,410.00 USD | 9,310.00 USD | 21,860.00 USD |
| `7D` | `1.04` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 7,410.00 USD | 9,310.00 USD | 21,860.00 USD |
| `1D` | `1.05` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 21,730.00 USD | 4,160.00 USD | 321.14 USD |
| `7D` | `1.05` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 21,730.00 USD | 4,160.00 USD | 321.14 USD |
| `1D` | `1.05` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 8,930.00 USD | 3,210.00 USD | 5,060.00 USD |
| `7D` | `1.05` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 8,930.00 USD | 3,210.00 USD | 5,060.00 USD |
| `1D` | `1.05` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 42,790.00 USD | 10,010.00 USD | 13,550.00 USD |
| `7D` | `1.05` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 42,790.00 USD | 10,010.00 USD | 13,550.00 USD |
| `1D` | `1.05` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 23,270.00 USD | 1,310.00 USD | 15,860.00 USD |
| `7D` | `1.05` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 23,270.00 USD | 1,310.00 USD | 15,860.00 USD |
| `1D` | `1.05` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 16,310.00 USD | 365.79 USD | 6,470.00 USD |
| `7D` | `1.05` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 16,310.00 USD | 365.79 USD | 6,470.00 USD |
| `1D` | `1.06` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 13,640.00 USD | 3,680.00 USD | 4,790.00 USD |
| `7D` | `1.06` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 13,640.00 USD | 3,680.00 USD | 4,790.00 USD |
| `1D` | `1.06` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 29,640.00 USD | 3,000.00 USD | 725.34 USD |
| `7D` | `1.06` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 29,640.00 USD | 3,000.00 USD | 725.34 USD |
| `1D` | `1.06` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 3,850.00 USD | 4,510.00 USD | 8,650.00 USD |
| `7D` | `1.06` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 3,850.00 USD | 4,510.00 USD | 8,650.00 USD |
| `1D` | `1.06` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 1,990.00 USD | 3,730.00 USD | 2,070.00 USD |
| `7D` | `1.06` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 1,990.00 USD | 3,730.00 USD | 2,070.00 USD |
| `1D` | `1.06` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 15,200.00 USD | 2,970.00 USD | 3,400.00 USD |
| `7D` | `1.06` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 15,200.00 USD | 2,970.00 USD | 3,400.00 USD |
| `1D` | `1.07` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 16,000.00 USD | 141.60 USD | 8,440.00 USD |
| `7D` | `1.07` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 16,000.00 USD | 141.60 USD | 8,440.00 USD |
| `1D` | `1.07` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 7,520.00 USD | 4,330.00 USD | 3,180.00 USD |
| `7D` | `1.07` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 7,520.00 USD | 4,330.00 USD | 3,180.00 USD |
| `1D` | `1.07` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 7,140.00 USD | 3,900.00 USD | 3,210.00 USD |
| `7D` | `1.07` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 7,140.00 USD | 3,900.00 USD | 3,210.00 USD |
| `1D` | `1.07` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 9,330.00 USD | 2,350.00 USD | 3,180.00 USD |
| `7D` | `1.07` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 9,330.00 USD | 2,350.00 USD | 3,180.00 USD |
| `1D` | `1.07` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 7,860.00 USD | 4,560.00 USD | 6,930.00 USD |
| `7D` | `1.07` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 7,860.00 USD | 4,560.00 USD | 6,930.00 USD |
| `1D` | `1.08` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 5,350.00 USD | 5,330.00 USD | 5,490.00 USD |
| `7D` | `1.08` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 5,350.00 USD | 5,330.00 USD | 5,490.00 USD |
| `1D` | `1.08` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 9,430.00 USD | 4,070.00 USD | 150.13 USD |
| `7D` | `1.08` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 9,430.00 USD | 4,070.00 USD | 150.13 USD |
| `1D` | `1.08` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 7,700.00 USD | 1,870.00 USD | 711.93 USD |
| `7D` | `1.08` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 7,700.00 USD | 1,870.00 USD | 711.93 USD |
| `1D` | `1.08` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 5,280.00 USD | 1,770.00 USD | 4,210.00 USD |
| `7D` | `1.08` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 5,280.00 USD | 1,770.00 USD | 4,210.00 USD |
| `1D` | `1.08` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 9,180.00 USD | 1,500.00 USD | 3,180.00 USD |
| `7D` | `1.08` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 9,180.00 USD | 1,500.00 USD | 3,180.00 USD |
| `1D` | `1.09` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 8,920.00 USD | 2,900.00 USD | 6,970.00 USD |
| `7D` | `1.09` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 8,920.00 USD | 2,900.00 USD | 6,970.00 USD |
| `1D` | `1.09` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 3,630.00 USD | 4,290.00 USD | 4,990.00 USD |
| `7D` | `1.09` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 3,630.00 USD | 4,290.00 USD | 4,990.00 USD |
| `1D` | `1.09` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 5,220.00 USD | 3,220.00 USD | 1,950.00 USD |
| `7D` | `1.09` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 9,830.00 USD | 3,220.00 USD | 1,950.00 USD |
| `1D` | `1.09` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 4,370.00 USD | 93.54 USD | 966.50 USD |
| `7D` | `1.09` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 4,370.00 USD | 93.54 USD | 966.50 USD |
| `1D` | `1.09` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 2,490.00 USD | 2,060.00 USD |
| `7D` | `1.09` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 2,490.00 USD | 2,060.00 USD |
| `1D` | `1.10` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 1,740.00 USD | 3,660.00 USD | 318.21 USD |
| `7D` | `1.10` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 1,740.00 USD | 3,660.00 USD | 318.21 USD |
| `1D` | `1.10` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 3,620.00 USD | 1,090.00 USD | 4,380.00 USD |
| `7D` | `1.10` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 3,620.00 USD | 1,090.00 USD | 4,380.00 USD |
| `1D` | `1.10` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 1,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.10` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 1,810.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `190.79M` | Total OI Tokens: `212,594,140.5 DOT`
  * 1h OI Change: `-8.63%` | 4h OI Change: `-10.39%` | 24h OI Change: `-13.74%`
  * Exchange Breakdown: Binance=`33.17M` | Bybit=`21.91M` | OKX=`9.52M` | Hyperliquid=`5.43M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.17K` | Last 24h: `7.91K` | Last 3d: `-10.37K` | Last 7d: `-19.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0004%` | **USDT OKX** | `0.0025%` |
| **USDT Bybit** | `0.0082%` | **USDT KuCoin** | `0.0042%` |
| **USDT MEXC** | `0.0004%` | **USDT BingX** | `0.0098%` |
| **USDT Gate** | `-0.0051%` | **USDT Bitget** | `-0.0001%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `41.52%` | `58.48%` | `0.71` | 33,860,000.00 USD |
| `15M` | `Binance` | `40.64%` | `59.36%` | `0.68` | 12,940,000.00 USD |
| `15M` | `OKX` | `44.65%` | `55.35%` | `0.81` | 4,150,000.00 USD |
| `15M` | `Bybit` | `39.01%` | `60.99%` | `0.64` | 5,100,000.00 USD |
| `15M` | `KuCoin` | `42.57%` | `57.43%` | `0.74` | 706,250.00 USD |
| `15M` | `Gate` | `53.92%` | `46.08%` | `1.17` | 2,630,000.00 USD |
| `15M` | `Bitget` | `46.15%` | `53.85%` | `0.86` | 1,300,000.00 USD |
| `15M` | `BingX` | `24.17%` | `75.83%` | `0.32` | 554,970.00 USD |
| `15M` | `MEXC` | `34.76%` | `65.24%` | `0.53` | 2,450,000.00 USD |
| `15M` | `Bitunix` | `45.4%` | `54.6%` | `0.83` | 908,200.00 USD |
| `15M` | `Hyperliquid` | `30.4%` | `69.6%` | `0.44` | 769,480.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `44.58%` | `55.42%` | `0.80` | 1,990,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `5.8%` | `94.2%` | `0.06` | 122,180.00 USD |
| `15M` | `HTX` | `40.74%` | `59.26%` | `0.69` | 58,570.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `54.54%` | `45.46%` | `1.20` | 112,590.00 USD |
| `15M` | `Aster` | `41.53%` | `58.47%` | `0.71` | 55,290.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `40.64%` | `59.36%` | `0.68` | 12,940,000.00 USD |
| `15M` | `Global Accounts` | `41.52%` | `58.48%` | `0.71` | 33,860,000.00 USD |
| `1H` | `DOT` | `42.17%` | `57.83%` | `0.73` | 46,000,000.00 USD |
| `1H` | `Binance` | `42.02%` | `57.98%` | `0.72` | 17,470,000.00 USD |
| `1H` | `OKX` | `44.79%` | `55.21%` | `0.81` | 5,540,000.00 USD |
| `1H` | `Bybit` | `38.54%` | `61.46%` | `0.63` | 6,120,000.00 USD |
| `1H` | `KuCoin` | `42.51%` | `57.49%` | `0.74` | 1,120,000.00 USD |
| `1H` | `Gate` | `51.79%` | `48.21%` | `1.07` | 4,060,000.00 USD |
| `1H` | `Bitget` | `43.99%` | `56.01%` | `0.79` | 1,880,000.00 USD |
| `1H` | `BingX` | `35.71%` | `64.29%` | `0.56` | 929,520.00 USD |
| `1H` | `MEXC` | `34.02%` | `65.98%` | `0.52` | 3,230,000.00 USD |
| `1H` | `Bitunix` | `45.48%` | `54.52%` | `0.83` | 1,320,000.00 USD |
| `1H` | `Hyperliquid` | `38.35%` | `61.65%` | `0.62` | 988,940.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `45.43%` | `54.57%` | `0.83` | 2,710,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `15.89%` | `84.11%` | `0.19` | 386,970.00 USD |
| `1H` | `HTX` | `37.85%` | `62.15%` | `0.61` | 58,910.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `51.56%` | `48.44%` | `1.06` | 135,010.00 USD |
| `1H` | `Aster` | `34.97%` | `65.03%` | `0.54` | 67,660.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `42.02%` | `57.98%` | `0.72` | 17,470,000.00 USD |
| `1H` | `Global Accounts` | `42.17%` | `57.83%` | `0.73` | 46,000,000.00 USD |
| `4H` | `DOT` | `43.64%` | `56.36%` | `0.77` | 76,210,000.00 USD |
| `4H` | `Binance` | `43.66%` | `56.34%` | `0.77` | 28,420,000.00 USD |
| `4H` | `OKX` | `44.99%` | `55.01%` | `0.82` | 8,450,000.00 USD |
| `4H` | `Bybit` | `40.68%` | `59.32%` | `0.69` | 9,540,000.00 USD |
| `4H` | `KuCoin` | `47.23%` | `52.77%` | `0.90` | 2,460,000.00 USD |
| `4H` | `Gate` | `50.89%` | `49.11%` | `1.04` | 5,380,000.00 USD |
| `4H` | `Bitget` | `47.22%` | `52.78%` | `0.89` | 3,290,000.00 USD |
| `4H` | `BingX` | `38.22%` | `61.78%` | `0.62` | 2,960,000.00 USD |
| `4H` | `MEXC` | `38.73%` | `61.27%` | `0.63` | 4,860,000.00 USD |
| `4H` | `Bitunix` | `46.85%` | `53.15%` | `0.88` | 2,010,000.00 USD |
| `4H` | `Hyperliquid` | `37.97%` | `62.03%` | `0.61` | 1,340,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.11%` | `50.89%` | `0.97` | 5,860,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `13.72%` | `86.28%` | `0.16` | 1,200,000.00 USD |
| `4H` | `HTX` | `51.13%` | `48.87%` | `1.05` | 109,120.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `51.81%` | `48.19%` | `1.08` | 227,210.00 USD |
| `4H` | `Aster` | `33.87%` | `66.13%` | `0.51` | 81,230.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `43.66%` | `56.34%` | `0.77` | 28,420,000.00 USD |
| `4H` | `Global Accounts` | `43.64%` | `56.36%` | `0.77` | 76,210,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.9787` | `0.9807` | `0.9787` | `0.9872` | `0.9767` | 1,756,422.05 USD | 785,190.37 USD | 971,231.69 USD | -186,041.32 USD | `-10.59%` | `9B / 23S` |
| `5:00 UTC` | `0.9813` | `0.9827` | `0.9813` | `0.9867` | `0.9789` | 947,049.41 USD | 720,261.00 USD | 226,788.42 USD | 493,472.58 USD | `+52.11%` | `28B / 1S` |
| `0:00 UTC` | `0.9805` | `0.9815` | `0.9805` | `0.9849` | `0.9787` | 512,523.44 USD | 243,023.57 USD | 269,499.87 USD | -26,476.30 USD | `-5.17%` | `12B / 6S` |
| `5:00 UTC` | `0.9856` | `0.9822` | `0.9856` | `0.9858` | `0.9780` | 526,140.64 USD | 318,567.26 USD | 207,573.38 USD | 110,993.88 USD | `+21.10%` | `16B / 9S` |
| `0:00 UTC` | `0.9873` | `0.9868` | `0.9873` | `0.9887` | `0.9839` | 407,897.05 USD | 216,028.73 USD | 191,868.32 USD | 24,160.41 USD | `+5.92%` | `8B / 4S` |
| `5:00 UTC` | `0.9858` | `0.9859` | `0.9858` | `0.9880` | `0.9839` | 388,071.33 USD | 177,551.18 USD | 210,520.15 USD | -32,968.97 USD | `-8.50%` | `3B / 8S` |
| `0:00 UTC` | `0.9681` | `0.9669` | `0.9681` | `0.9851` | `0.9557` | 3,728,299.49 USD | 1,667,776.70 USD | 2,060,522.79 USD | -392,746.09 USD | `-10.53%` | `7B / 26S` |
| `5:00 UTC` | `0.9681` | `0.9687` | `0.9681` | `0.9718` | `0.9650` | 792,721.03 USD | 373,256.63 USD | 419,464.39 USD | -46,207.76 USD | `-5.83%` | `5B / 11S` |
| `0:00 UTC` | `0.9271` | `0.9372` | `0.9271` | `0.9707` | `0.9107` | 10,294,158.77 USD | 4,127,124.83 USD | 6,167,033.94 USD | -2,039,909.11 USD | `-19.82%` | `5B / 37S` |
| `5:00 UTC` | `0.9095` | `0.9081` | `0.9095` | `0.9241` | `0.8893` | 7,538,652.19 USD | 3,452,360.38 USD | 4,086,291.81 USD | -633,931.44 USD | `-8.41%` | `7B / 14S` |

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
| `5m` | -648,710.00 USD | -2,980,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -561,160.00 USD | -3,200,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -585,270.00 USD | -3,210,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -809,090.00 USD | -4,090,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -284,180.00 USD | -3,160,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -469,370.00 USD | -4,390,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -525,370.00 USD | -5,630,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -887,090.00 USD | -5,330,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,080,000.00 USD | -5,740,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,190,000.00 USD | -5,580,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,200,000.00 USD | -22,110,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,420,000.00 USD | -76,560,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-648.71K` | 15m=`-561.16K` | 1h=`-809.09K` | 24h=`-1.19M`
* Futures Capital Netflows: 5m=`-2.98M` | 15m=`-3.20M` | 1h=`-4.09M` | 24h=`-5.58M`
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
  * `2026-10-30 02:14:39 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:39 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:21:39 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:21:39 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:22:39 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.9539` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.9049` (Risk Distance: `0.0520` pts)
  * +2.5R Take Profit: `1.08`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9952` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.04` (Risk Distance: `0.0520` pts)
  * +2.5R Take Profit: `0.8652`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9233`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
