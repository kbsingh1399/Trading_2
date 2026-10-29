# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 01:57:19 IST` (`2026-10-29 20:27:19 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9590` | **Live Ask Quote**: `0.9790` | **Mid Price**: `0.9690`
- **Spread Points**: `20.00` | **Spread BPS**: `206.40 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.9766` | VWAP Z-Score: `-1.25` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0085` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `33.16` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.02` | Lower -3.00σ Band: `0.9342`
  * Upper +2.51σ Band: `1.01` | Lower -2.51σ Band: `0.9412`
  * Upper +2.01σ Band: `1.01` | Lower -2.01σ Band: `0.9482`
  * Upper +2.00σ Band: `1.00` | Lower -2.00σ Band: `0.9484`
  * Upper +1.28σ Band: `0.9947` | Lower -1.28σ Band: `0.9585`
  * Upper +1.00σ Band: `0.9907` | Lower -1.00σ Band: `0.9625`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9725` | EMA-20=`0.9783` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9803` (Slope: `+0.0000`) | EMA-100=`0.9819`
  * Institutional Anchors: EMA-144=`0.9830` | EMA-200=`0.9837` (Slope: `-0.1159`) | EMA-233=`0.9840`
- **Range Boundaries**: 24H High=`1.02` | 24H Low=`0.9460` | Weekly High=`1.03` | Weekly Low=`0.9460`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9934` (Distance: `-2.56%`)
  * Point of Control (POC) = `0.9740` (Distance: `-0.61%`)
  * Value Area Low (VAL) = `0.9540` (Distance: `+1.46%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.00` | POC=`0.9890` | VAL=`0.9812`
  * Prior Day Extremes: PDH=`1.03` | PDL=`0.9690` | PDC=`1.01`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.01` | Weekly POC=`0.9927` | Weekly VAL=`0.9769`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.02` | Low=`0.9510`
  * London Session (08:00-16:00 UTC): High=`0.9850` | Low=`0.9600`
  * New York Session (13:00-21:00 UTC): High=`1.01` | Low=`0.9680`
  * Initial Balance (First Hour): IB High=`0.9800` | IB Low=`0.9670`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9651` - `0.9729`
  * Optimal Trade Entry (OTE 0.705): `0.9709`
  * Structural Invalidation Anchor (0.786): `0.9768`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9647` | `0.9704` | `0.9601` | `0.9696` | `529,477` | 511,475.64 USD | -9,117.27 USD | `-1.78%` | -916,011.83 USD | `-0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.9695` | `0.9717` | `0.9673` | `0.9702` | `309,510` | 300,097.83 USD | -6,578.06 USD | `-2.19%` | -922,589.90 USD | `-0.12` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.9703` | `0.9715` | `0.9650` | `0.9685` | `246,973` | 239,073.84 USD | -7,803.54 USD | `-3.26%` | -930,393.44 USD | `-0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.9861` | `0.9880` | `0.9839` | `0.9844` | `393,652` | 388,071.33 USD | -32,968.97 USD | `-8.50%` | -446,818.45 USD | `-0.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.9845` | `0.9849` | `0.9556` | `0.9696` | `3,856,197` | 3,728,299.49 USD | -392,746.09 USD | `-10.53%` | -839,564.54 USD | `-1.45` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.9695` | `0.9717` | `0.9650` | `0.9685` | `556,483` | 539,171.67 USD | -14,381.60 USD | `-2.67%` | -853,946.14 USD | `+0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9918` | `0.9929` | `0.9766` | `0.9840` | `3,542,573` | 3,482,685.13 USD | 238,678.91 USD | `+6.85%` | -618,930.49 USD | `+0.79` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.9839` | `0.9886` | `0.9780` | `0.9844` | `1,864,944` | 1,834,632.46 USD | 75,709.02 USD | `+4.13%` | -543,221.47 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9845` | `0.9849` | `0.9556` | `0.9685` | `4,412,680` | 4,267,471.16 USD | -407,127.69 USD | `-9.54%` | -950,349.17 USD | `-1.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | 516,506.12 USD | `-1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -280,559.32 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.9556` | `0.9685` | `4,412,680` | 4,267,471.16 USD | -407,127.69 USD | `-9.54%` | -687,687.02 USD | `-0.68` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9699` | `0.9906` | `0.9674` | `0.9732` | `8,505,701` | 8,320,368.15 USD | 13,201.93 USD | `+0.16%` | 609,018.52 USD | `-1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | 694,082.93 USD | `-0.56` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | 516,506.12 USD | `-1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -280,559.32 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.9556` | `0.9685` | `4,412,680` | 4,267,471.16 USD | -407,127.69 USD | `-9.54%` | -687,687.02 USD | `-0.68` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.9690`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:54:30 IST` |

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
| `Live` | `Long Liquidation` | `0.7965` | 106.49 USD | 344,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8025` | 238.90 USD | 344,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8045` | 566.61 USD | 344,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8055` | 699.01 USD | 343,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8115` | 13,430.00 USD | 342,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 329,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 328,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8285` | 1,890.00 USD | 326,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 324,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8375` | 167.00 USD | 324,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,240.00 USD | 324,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8445` | 168.31 USD | 323,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 323,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8550` | 3,720,000.00 USD | 3,720,000.00 USD | 254.55 USD | 2,670.00 USD | 5,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8570` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 944.22 USD | 577.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 321,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8590` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8595` | 171.38 USD | 321,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8605` | 61,100.00 USD | 320,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8610` | 3,710,000.00 USD | 3,710,000.00 USD | 264.68 USD | 794.46 USD | 146.13 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8625` | 309.55 USD | 259,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8630` | 3,710,000.00 USD | 3,710,000.00 USD | 758.91 USD | 2,590.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 259,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 1,760,000.00 USD | 1,760,000.00 USD | 5,790.00 USD | 1,940.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 259,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8650` | 3,700,000.00 USD | 3,700,000.00 USD | 4,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8660` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 20.18 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 118.54 USD | 258,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8670` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 3,240.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8680` | 1,750,000.00 USD | 1,750,000.00 USD | 3,320.00 USD | 3,550.00 USD | 6,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8690` | 3,680,000.00 USD | 3,680,000.00 USD | 25,250.00 USD | 1,950.00 USD | 6,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8700` | 1,740,000.00 USD | 1,740,000.00 USD | 12,660.00 USD | 3,580.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8710` | 3,650,000.00 USD | 3,650,000.00 USD | 6,960.00 USD | 1,110.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8720` | 1,720,000.00 USD | 1,720,000.00 USD | 5,850.00 USD | 26.70 USD | 3,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 2,120.00 USD | 295.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 1,710,000.00 USD | 1,710,000.00 USD | 6,780.00 USD | 3,080.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 1,700,000.00 USD | 1,700,000.00 USD | 6,140.00 USD | 3,510.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 171.88 USD | 258,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8770` | 3,630,000.00 USD | 3,630,000.00 USD | 20,650.00 USD | 6,200.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8780` | 1,690,000.00 USD | 1,690,000.00 USD | 15,310.00 USD | 6,400.00 USD | 10,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 3,600,000.00 USD | 3,600,000.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8795` | 948.01 USD | 258,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8800` | 1,650,000.00 USD | 1,650,000.00 USD | 4,390.00 USD | 5,110.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 3,600,000.00 USD | 3,600,000.00 USD | 228.30 USD | 167.73 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8820` | 1,640,000.00 USD | 1,640,000.00 USD | 8,320.00 USD | 3,980.00 USD | 150.13 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8830` | 3,600,000.00 USD | 3,600,000.00 USD | 8,430.00 USD | 5,730.00 USD | 360.61 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 1,630,000.00 USD | 1,630,000.00 USD | 7,440.00 USD | 1,810.00 USD | 711.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8850` | 3,580,000.00 USD | 3,580,000.00 USD | 8,630.00 USD | 5,960.00 USD | 942.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8860` | 1,620,000.00 USD | 1,620,000.00 USD | 5,010.00 USD | 1,700.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8870` | 3,560,000.00 USD | 3,560,000.00 USD | 18,520.00 USD | 5,060.00 USD | 6,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8880` | 1,610,000.00 USD | 1,610,000.00 USD | 17,470.00 USD | 4,180.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8890` | 3,530,000.00 USD | 3,530,000.00 USD | 13,840.00 USD | 5,300.00 USD | 14,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8900` | 1,570,000.00 USD | 1,570,000.00 USD | 3,630.00 USD | 4,230.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8910` | 3,500,000.00 USD | 3,500,000.00 USD | 30,330.00 USD | 10,730.00 USD | 24,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8920` | 1,560,000.00 USD | 1,560,000.00 USD | 4,920.00 USD | 3,160.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8925` | 526.84 USD | 257,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8930` | 3,430,000.00 USD | 3,430,000.00 USD | 24,780.00 USD | 5,820.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8940` | 1,550,000.00 USD | 1,550,000.00 USD | 4,240.00 USD | 23.75 USD | 966.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8950` | 3,390,000.00 USD | 3,390,000.00 USD | 7,380.00 USD | 9,390.00 USD | 27,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8960` | 1,550,000.00 USD | 1,550,000.00 USD | 1,930.00 USD | 6,130.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8970` | 3,350,000.00 USD | 3,350,000.00 USD | 43,430.00 USD | 5,400.00 USD | 31,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8980` | 1,540,000.00 USD | 1,540,000.00 USD | 5,550.00 USD | 65.95 USD | 992.14 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8985` | 9,220.00 USD | 257,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8990` | 3,270,000.00 USD | 3,270,000.00 USD | 52,250.00 USD | 14,760.00 USD | 20,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8995` | 3,820.00 USD | 247,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9000` | 1,530,000.00 USD | 1,530,000.00 USD | 3,760.00 USD | 796.93 USD | 2,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9010` | 3,180,000.00 USD | 3,180,000.00 USD | 20,170.00 USD | 11,690.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9020` | 1,520,000.00 USD | 1,520,000.00 USD | 4,180.00 USD | 3,250.00 USD | 2,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9030` | 3,150,000.00 USD | 3,150,000.00 USD | 13,100.00 USD | 8,710.00 USD | 25,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9035` | 180.16 USD | 244,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9040` | 1,510,000.00 USD | 1,510,000.00 USD | 3,360.00 USD | 2,560.00 USD | 5,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9050` | 3,100,000.00 USD | 3,100,000.00 USD | 35,230.00 USD | 25,240.00 USD | 27,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9055` | 674.42 USD | 243,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9060` | 1,500,000.00 USD | 1,500,000.00 USD | 9,620.00 USD | 1,660.00 USD | 111.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9070` | 3,010,000.00 USD | 3,010,000.00 USD | 37,740.00 USD | 7,720.00 USD | 15,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9080` | 1,490,000.00 USD | 1,490,000.00 USD | 5,800.00 USD | 3,150.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9090` | 2,950,000.00 USD | 2,950,000.00 USD | 14,170.00 USD | 8,050.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9095` | 951.34 USD | 243,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9100` | 1,480,000.00 USD | 1,480,000.00 USD | 21,930.00 USD | 2,070.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9110` | 2,920,000.00 USD | 2,920,000.00 USD | 8,490.00 USD | 7,760.00 USD | 17,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9120` | 1,450,000.00 USD | 1,450,000.00 USD | 4,400.00 USD | 315.61 USD | 3,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9130` | 2,890,000.00 USD | 2,890,000.00 USD | 26,980.00 USD | 2,230.00 USD | 680.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9135` | 143.42 USD | 242,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9140` | 1,440,000.00 USD | 1,440,000.00 USD | 6,040.00 USD | 1,290.00 USD | 4,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9150` | 2,860,000.00 USD | 2,860,000.00 USD | 41,520.00 USD | 10,930.00 USD | 34,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9160` | 1,430,000.00 USD | 1,430,000.00 USD | 14,280.00 USD | 131.45 USD | 3,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9170` | 2,770,000.00 USD | 2,770,000.00 USD | 22,610.00 USD | 14,910.00 USD | 15,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9180` | 1,410,000.00 USD | 1,410,000.00 USD | 167.33 USD | 484.89 USD | 452.67 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9185` | 145.86 USD | 242,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9190` | 2,720,000.00 USD | 2,720,000.00 USD | 33,380.00 USD | 4,860.00 USD | 19,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9195` | 7,330.00 USD | 241,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9200` | 1,410,000.00 USD | 1,410,000.00 USD | 3,030.00 USD | 166.12 USD | 192.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9210` | 2,660,000.00 USD | 2,660,000.00 USD | 22,590.00 USD | 7,000.00 USD | 15,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9220` | 1,410,000.00 USD | 1,410,000.00 USD | 22,330.00 USD | 4,870.00 USD | 12,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9225` | 8,360.00 USD | 234,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9230` | 2,610,000.00 USD | 2,610,000.00 USD | 35,230.00 USD | 11,030.00 USD | 37,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9240` | 1,370,000.00 USD | 1,370,000.00 USD | 14,520.00 USD | 5,440.00 USD | 36.99 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9250` | 2,530,000.00 USD | 2,530,000.00 USD | 82,280.00 USD | 17,010.00 USD | 45,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9260` | 1,350,000.00 USD | 1,350,000.00 USD | 11,040.00 USD | 13,740.00 USD | 26,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9270` | 2,390,000.00 USD | 2,390,000.00 USD | 70,300.00 USD | 9,380.00 USD | 22,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9280` | 1,290,000.00 USD | 1,290,000.00 USD | 43,650.00 USD | 4,700.00 USD | 5,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9290` | 2,280,000.00 USD | 2,280,000.00 USD | 39,160.00 USD | 6,760.00 USD | 31,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9295` | 253.01 USD | 226,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9300` | 1,240,000.00 USD | 1,240,000.00 USD | 14,980.00 USD | 1,340.00 USD | 16,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9310` | 2,210,000.00 USD | 2,210,000.00 USD | 37,460.00 USD | 10,070.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9320` | 1,210,000.00 USD | 1,210,000.00 USD | 27,830.00 USD | 13,360.00 USD | 9,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9330` | 2,150,000.00 USD | 2,150,000.00 USD | 33,550.00 USD | 9,670.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9335` | 361.45 USD | 226,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9340` | 1,160,000.00 USD | 1,160,000.00 USD | 21,510.00 USD | 11,340.00 USD | 10,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9350` | 2,080,000.00 USD | 2,080,000.00 USD | 82,010.00 USD | 29,330.00 USD | 17,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9360` | 1,110,000.00 USD | 1,110,000.00 USD | 49,420.00 USD | 11,180.00 USD | 19,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9365` | 6,560.00 USD | 225,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9370` | 1,950,000.00 USD | 1,950,000.00 USD | 29,580.00 USD | 14,910.00 USD | 7,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9375` | 196.97 USD | 219,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9380` | 1,030,000.00 USD | 1,030,000.00 USD | 25,680.00 USD | 14,710.00 USD | 10,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9390` | 1,900,000.00 USD | 1,900,000.00 USD | 18,750.00 USD | 14,310.00 USD | 12,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9400` | 982,310.00 USD | 982,310.00 USD | 28,130.00 USD | 10,650.00 USD | 24,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9405` | 141.83 USD | 218,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9410` | 1,860,000.00 USD | 1,860,000.00 USD | 45,790.00 USD | 14,660.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9420` | 919,520.00 USD | 919,520.00 USD | 58,960.00 USD | 23,370.00 USD | 12,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9430` | 1,790,000.00 USD | 1,790,000.00 USD | 54,680.00 USD | 18,070.00 USD | 11,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9440` | 825,100.00 USD | 825,100.00 USD | 35,560.00 USD | 18,570.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9445` | 1,060.00 USD | 218,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9450` | 1,710,000.00 USD | 1,710,000.00 USD | 137,080.00 USD | 49,320.00 USD | 73,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9455` | 106,880.00 USD | 217,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9460` | 763,420.00 USD | 763,420.00 USD | 46,890.00 USD | 38,090.00 USD | 70,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9470` | 1,450,000.00 USD | 1,450,000.00 USD | 125,790.00 USD | 24,210.00 USD | 51,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9475` | 323.19 USD | 110,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9480` | 607,510.00 USD | 607,510.00 USD | 134,950.00 USD | 28,180.00 USD | 40,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9490` | 1,250,000.00 USD | 1,250,000.00 USD | 129,370.00 USD | 34,600.00 USD | 122,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9495` | 105,430.00 USD | 110,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9500` | 403,650.00 USD | 403,650.00 USD | 40,200.00 USD | 9,030.00 USD | 39,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9510` | 959,780.00 USD | 959,780.00 USD | 229,420.00 USD | 44,120.00 USD | 81,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9515` | 405.62 USD | 5,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9520` | 315,270.00 USD | 315,270.00 USD | 73,640.00 USD | 33,830.00 USD | 23,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9530` | 604,840.00 USD | 604,840.00 USD | 79,700.00 USD | 27,910.00 USD | 123,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9540` | 184,120.00 USD | 184,120.00 USD | 52,780.00 USD | 30,680.00 USD | 29,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9550` | 374,100.00 USD | 374,100.00 USD | 172,820.00 USD | 89,220.00 USD | 21,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9555` | 3,160.00 USD | 4,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9560` | 71,130.00 USD | 71,130.00 USD | 49,230.00 USD | 20,890.00 USD | 419.82 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9570` | 91,020.00 USD | 91,020.00 USD | 20,700.00 USD | 0.00 USD | 6,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9585` | 1,530.00 USD | 1,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9590` | 63,410.00 USD | 63,410.00 USD | 16,080.00 USD | 0.00 USD | 1,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9610` | 45,620.00 USD | 45,620.00 USD | 24,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9630` | 21,250.00 USD | 21,250.00 USD | 12,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9650` | 8,280.00 USD | 8,280.00 USD | 8,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9660` | 595.80 USD | 595.80 USD | 595.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 47,560.00 USD | 47,560.00 USD | 0.00 USD | 11,390.00 USD | 36,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 19,790.00 USD | 19,790.00 USD | 0.00 USD | 82.70 USD | 19,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 71,690.00 USD | 71,690.00 USD | 0.00 USD | 14,530.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 65,590.00 USD | 65,590.00 USD | 23,620.00 USD | 0.00 USD | 22,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 79,200.00 USD | 79,200.00 USD | 0.00 USD | 0.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 89,420.00 USD | 89,420.00 USD | 9,580.00 USD | 0.00 USD | 14,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 99,070.00 USD | 99,070.00 USD | 0.00 USD | 16,590.00 USD | 3,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 130,730.00 USD | 130,730.00 USD | 19,600.00 USD | 13,960.00 USD | 7,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 151,280.00 USD | 151,280.00 USD | 15,320.00 USD | 5,480.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 171,140.00 USD | 171,140.00 USD | 22,490.00 USD | 0.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 236,200.00 USD | 236,200.00 USD | 0.00 USD | 0.00 USD | 84,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 229,840.00 USD | 229,840.00 USD | 28,330.00 USD | 9,580.00 USD | 20,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9810` | 354,090.00 USD | 354,090.00 USD | 0.00 USD | 0.00 USD | 117,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 264,860.00 USD | 264,860.00 USD | 15,980.00 USD | 12,160.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 474,070.00 USD | 474,070.00 USD | 52,130.00 USD | 15,600.00 USD | 52,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 305,510.00 USD | 305,510.00 USD | 0.00 USD | 8,340.00 USD | 32,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 496,380.00 USD | 496,380.00 USD | 0.00 USD | 0.00 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 353,610.00 USD | 353,610.00 USD | 39,150.00 USD | 3,460.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 537,760.00 USD | 537,760.00 USD | 40,020.00 USD | 0.00 USD | 1,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9880` | 354,670.00 USD | 354,670.00 USD | 0.00 USD | 0.00 USD | 1,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9890` | 559,670.00 USD | 559,670.00 USD | 20,470.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 426,750.00 USD | 426,750.00 USD | 57,390.00 USD | 1,300.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9910` | 579,260.00 USD | 579,260.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 439,630.00 USD | 439,630.00 USD | 0.00 USD | 0.00 USD | 12,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9930` | 580,480.00 USD | 580,480.00 USD | 0.00 USD | 0.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 459,790.00 USD | 459,790.00 USD | 6,920.00 USD | 13,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9950` | 639,760.00 USD | 639,760.00 USD | 16,510.00 USD | 0.00 USD | 42,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 462,420.00 USD | 462,420.00 USD | 0.00 USD | 2,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 712,840.00 USD | 712,840.00 USD | 68,870.00 USD | 0.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 518,130.00 USD | 518,130.00 USD | 40,410.00 USD | 4,790.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 602,020.00 USD | 602,020.00 USD | 50,740.00 USD | 31,440.00 USD | 1,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 765,690.00 USD | 765,690.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 602,280.00 USD | 602,280.00 USD | 0.00 USD | 0.00 USD | 266.05 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 882,720.00 USD | 882,720.00 USD | 78,440.00 USD | 21,740.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 630,750.00 USD | 630,750.00 USD | 10,110.00 USD | 9,540.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 904,010.00 USD | 904,010.00 USD | 19,830.00 USD | 0.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 758,520.00 USD | 758,520.00 USD | 95,330.00 USD | 8,600.00 USD | 23,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 939,150.00 USD | 939,150.00 USD | 34,110.00 USD | 0.00 USD | 1,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 780,400.00 USD | 780,400.00 USD | 255.10 USD | 6,910.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 964,890.00 USD | 964,890.00 USD | 10,230.00 USD | 0.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 799,720.00 USD | 799,720.00 USD | 10,530.00 USD | 8,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 999,150.00 USD | 999,150.00 USD | 20,090.00 USD | 14,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 841,460.00 USD | 841,460.00 USD | 16,240.00 USD | 25,350.00 USD | 155.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 1,050,000.00 USD | 1,050,000.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 876,480.00 USD | 876,480.00 USD | 5,630.00 USD | 4,370.00 USD | 25,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 26,360.00 USD | 7,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 916,950.00 USD | 916,950.00 USD | 20,120.00 USD | 75.20 USD | 20,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 1,130,000.00 USD | 1,130,000.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 953,960.00 USD | 953,960.00 USD | 6,290.00 USD | 8,490.00 USD | 22,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 75,760.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,020,000.00 USD | 1,020,000.00 USD | 44,710.00 USD | 4,370.00 USD | 15,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 1,370,000.00 USD | 1,370,000.00 USD | 44,170.00 USD | 32,840.00 USD | 68,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,090,000.00 USD | 1,090,000.00 USD | 51,380.00 USD | 3,670.00 USD | 21,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 1,660,000.00 USD | 1,660,000.00 USD | 66,990.00 USD | 85,890.00 USD | 146,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 1,220,000.00 USD | 1,220,000.00 USD | 50,330.00 USD | 25,640.00 USD | 53,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 1,770,000.00 USD | 1,770,000.00 USD | 28,320.00 USD | 48,490.00 USD | 29,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,310,000.00 USD | 1,310,000.00 USD | 52,170.00 USD | 18,370.00 USD | 20,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,080,000.00 USD | 2,080,000.00 USD | 160,800.00 USD | 127,000.00 USD | 25,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,380,000.00 USD | 1,380,000.00 USD | 31,340.00 USD | 10,940.00 USD | 18,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,290,000.00 USD | 2,290,000.00 USD | 142,240.00 USD | 38,750.00 USD | 30,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,530,000.00 USD | 1,530,000.00 USD | 95,330.00 USD | 24,510.00 USD | 33,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,490,000.00 USD | 2,490,000.00 USD | 170,960.00 USD | 7,350.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,640,000.00 USD | 1,640,000.00 USD | 69,820.00 USD | 8,980.00 USD | 35,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,620,000.00 USD | 2,620,000.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,710,000.00 USD | 1,710,000.00 USD | 38,330.00 USD | 9,300.00 USD | 21,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,930,000.00 USD | 2,930,000.00 USD | 259,060.00 USD | 8,290.00 USD | 43,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,780,000.00 USD | 1,780,000.00 USD | 18,100.00 USD | 13,840.00 USD | 32,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,240,000.00 USD | 3,240,000.00 USD | 192,080.00 USD | 3,170.00 USD | 109,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 210.51 USD | 210.51 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,870,000.00 USD | 1,870,000.00 USD | 62,580.00 USD | 3,190.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,600,000.00 USD | 3,600,000.00 USD | 239,580.00 USD | 9,010.00 USD | 117,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,890,000.00 USD | 1,890,000.00 USD | 7,790.00 USD | 8,100.00 USD | 9,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 4,040,000.00 USD | 4,040,000.00 USD | 276,890.00 USD | 2,090.00 USD | 159,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,920,000.00 USD | 1,920,000.00 USD | 11,290.00 USD | 9,870.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 4,240,000.00 USD | 4,240,000.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,970,000.00 USD | 1,970,000.00 USD | 7,410.00 USD | 9,310.00 USD | 32,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 212.03 USD | 422.54 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 4,500,000.00 USD | 4,500,000.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,000,000.00 USD | 2,000,000.00 USD | 21,730.00 USD | 4,160.00 USD | 321.14 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 424.67 USD | 847.21 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 5,020,000.00 USD | 5,020,000.00 USD | 178,890.00 USD | 96,370.00 USD | 238,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 733.98 USD | 1,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,010,000.00 USD | 2,010,000.00 USD | 8,680.00 USD | 3,210.00 USD | 4,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 5,230,000.00 USD | 5,230,000.00 USD | 116,670.00 USD | 13,780.00 USD | 77,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,080,000.00 USD | 2,080,000.00 USD | 39,540.00 USD | 8,970.00 USD | 13,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 5,530,000.00 USD | 5,530,000.00 USD | 175,210.00 USD | 43,690.00 USD | 87,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,120,000.00 USD | 2,120,000.00 USD | 23,270.00 USD | 1,310.00 USD | 15,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 213.55 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 5,720,000.00 USD | 5,720,000.00 USD | 61,670.00 USD | 55,920.00 USD | 74,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 213.76 USD | 2,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,130,000.00 USD | 2,130,000.00 USD | 8,900.00 USD | 340.84 USD | 6,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 5,950,000.00 USD | 5,950,000.00 USD | 125,020.00 USD | 33,860.00 USD | 72,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.06` | 74,410.00 USD | 76,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.06` | 2,160,000.00 USD | 2,160,000.00 USD | 13,640.00 USD | 3,680.00 USD | 13,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,350,000.00 USD | 6,350,000.00 USD | 218,860.00 USD | 70,000.00 USD | 106,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 2,210,000.00 USD | 2,210,000.00 USD | 29,640.00 USD | 3,000.00 USD | 13,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,800,000.00 USD | 6,800,000.00 USD | 229,940.00 USD | 74,380.00 USD | 145,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.06` | 214.97 USD | 76,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.06` | 2,230,000.00 USD | 2,230,000.00 USD | 3,850.00 USD | 4,510.00 USD | 8,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 7,070,000.00 USD | 7,070,000.00 USD | 140,850.00 USD | 56,310.00 USD | 78,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 2,230,000.00 USD | 2,230,000.00 USD | 1,990.00 USD | 3,730.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 7,360,000.00 USD | 7,360,000.00 USD | 141,700.00 USD | 73,690.00 USD | 71,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.06` | 431.57 USD | 77,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.06` | 2,260,000.00 USD | 2,260,000.00 USD | 12,920.00 USD | 3,060.00 USD | 5,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 7,560,000.00 USD | 7,560,000.00 USD | 90,670.00 USD | 28,390.00 USD | 83,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 2,270,000.00 USD | 2,270,000.00 USD | 12,670.00 USD | 141.60 USD | 5,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,780,000.00 USD | 7,780,000.00 USD | 86,760.00 USD | 43,390.00 USD | 82,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 2,290,000.00 USD | 2,290,000.00 USD | 7,520.00 USD | 4,330.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 8,070,000.00 USD | 8,070,000.00 USD | 219,670.00 USD | 14,440.00 USD | 62,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.07` | 216.89 USD | 77,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.07` | 2,300,000.00 USD | 2,300,000.00 USD | 7,140.00 USD | 3,900.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.07` | 217.20 USD | 77,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.07` | 8,300,000.00 USD | 8,300,000.00 USD | 141,570.00 USD | 36,670.00 USD | 52,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 2,320,000.00 USD | 2,320,000.00 USD | 9,330.00 USD | 2,350.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 8,540,000.00 USD | 8,540,000.00 USD | 96,630.00 USD | 42,960.00 USD | 95,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 2,340,000.00 USD | 2,340,000.00 USD | 7,860.00 USD | 4,630.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.07` | 436.03 USD | 77,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.07` | 8,730,000.00 USD | 8,730,000.00 USD | 97,650.00 USD | 27,560.00 USD | 60,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,350,000.00 USD | 2,350,000.00 USD | 5,350.00 USD | 5,330.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,880,000.00 USD | 8,880,000.00 USD | 75,040.00 USD | 29,910.00 USD | 48,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,370,000.00 USD | 2,370,000.00 USD | 9,430.00 USD | 4,070.00 USD | 150.13 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 9,120,000.00 USD | 9,120,000.00 USD | 166,380.00 USD | 21,060.00 USD | 52,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,380,000.00 USD | 2,380,000.00 USD | 7,700.00 USD | 1,870.00 USD | 711.93 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 9,340,000.00 USD | 9,340,000.00 USD | 164,440.00 USD | 26,480.00 USD | 33,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,390,000.00 USD | 2,390,000.00 USD | 5,280.00 USD | 1,790.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 9,550,000.00 USD | 9,550,000.00 USD | 61,330.00 USD | 41,110.00 USD | 100,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,400,000.00 USD | 2,400,000.00 USD | 9,180.00 USD | 1,500.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 9,700,000.00 USD | 9,700,000.00 USD | 86,400.00 USD | 18,540.00 USD | 46,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,420,000.00 USD | 2,420,000.00 USD | 8,920.00 USD | 2,900.00 USD | 6,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,930,000.00 USD | 9,930,000.00 USD | 102,510.00 USD | 58,170.00 USD | 69,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,430,000.00 USD | 2,430,000.00 USD | 3,630.00 USD | 4,290.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 10,110,000.00 USD | 10,110,000.00 USD | 71,650.00 USD | 23,140.00 USD | 85,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,450,000.00 USD | 2,450,000.00 USD | 5,220.00 USD | 3,140.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.09` | 221.37 USD | 78,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.09` | 10,240,000.00 USD | 10,240,000.00 USD | 70,660.00 USD | 25,660.00 USD | 32,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,450,000.00 USD | 2,450,000.00 USD | 4,370.00 USD | 0.00 USD | 966.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 10,400,000.00 USD | 10,400,000.00 USD | 59,280.00 USD | 39,220.00 USD | 62,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 2,440.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 10,570,000.00 USD | 10,570,000.00 USD | 56,240.00 USD | 22,740.00 USD | 92,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,710,000.00 USD | 10,710,000.00 USD | 88,860.00 USD | 11,400.00 USD | 38,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 11,040,000.00 USD | 11,040,000.00 USD | 188,000.00 USD | 49,370.00 USD | 89,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 11,220,000.00 USD | 11,220,000.00 USD | 122,300.00 USD | 44,140.00 USD | 15,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 11,440,000.00 USD | 11,440,000.00 USD | 91,720.00 USD | 19,430.00 USD | 110,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 11,500,000.00 USD | 11,500,000.00 USD | 22,500.00 USD | 10,390.00 USD | 31,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 11,610,000.00 USD | 11,610,000.00 USD | 51,840.00 USD | 24,280.00 USD | 34,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 11,800,000.00 USD | 11,800,000.00 USD | 80,930.00 USD | 42,230.00 USD | 63,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.11` | 169.86 USD | 78,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.11` | 11,950,000.00 USD | 11,950,000.00 USD | 69,040.00 USD | 16,050.00 USD | 64,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 12,040,000.00 USD | 12,040,000.00 USD | 20,190.00 USD | 43,570.00 USD | 25,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 12,090,000.00 USD | 12,090,000.00 USD | 34,700.00 USD | 6,650.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 12,240,000.00 USD | 12,240,000.00 USD | 68,170.00 USD | 45,980.00 USD | 32,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 12,300,000.00 USD | 12,300,000.00 USD | 24,700.00 USD | 22,760.00 USD | 13,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.12` | 518.90 USD | 78,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.12` | 12,400,000.00 USD | 12,400,000.00 USD | 48,980.00 USD | 30,950.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 12,490,000.00 USD | 12,490,000.00 USD | 61,780.00 USD | 5,220.00 USD | 25,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 12,550,000.00 USD | 12,550,000.00 USD | 18,300.00 USD | 10,940.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 12,580,000.00 USD | 12,580,000.00 USD | 14,700.00 USD | 342.11 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 12,700,000.00 USD | 12,700,000.00 USD | 56,500.00 USD | 19,160.00 USD | 45,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 12,910,000.00 USD | 12,910,000.00 USD | 106,510.00 USD | 12,730.00 USD | 90,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 13,010,000.00 USD | 13,010,000.00 USD | 77,640.00 USD | 3,650.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 13,040,000.00 USD | 13,040,000.00 USD | 0.00 USD | 8,380.00 USD | 20,850.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.8550` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 254.55 USD | 2,670.00 USD | 5,540.00 USD |
| `7D` | `0.8570` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 0.00 USD | 944.22 USD | 577.61 USD |
| `7D` | `0.8590` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD |
| `7D` | `0.8610` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 264.68 USD | 794.46 USD | 146.13 USD |
| `7D` | `0.8630` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 758.91 USD | 2,590.00 USD | 1,280.00 USD |
| `1D` | `0.8640` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 5,790.00 USD | 1,940.00 USD | 3,790.00 USD |
| `7D` | `0.8650` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 4,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8660` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 0.00 USD | 20.18 USD | 0.00 USD |
| `7D` | `0.8670` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 0.00 USD | 3,240.00 USD | 10,160.00 USD |
| `1D` | `0.8680` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 3,320.00 USD | 3,550.00 USD | 6,730.00 USD |
| `7D` | `0.8690` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 25,250.00 USD | 1,950.00 USD | 6,900.00 USD |
| `1D` | `0.8700` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 12,660.00 USD | 3,580.00 USD | 1,880.00 USD |
| `7D` | `0.8710` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 6,960.00 USD | 1,110.00 USD | 1,950.00 USD |
| `1D` | `0.8720` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 5,850.00 USD | 26.70 USD | 3,560.00 USD |
| `7D` | `0.8730` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 0.00 USD | 2,120.00 USD | 295.31 USD |
| `1D` | `0.8740` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 6,780.00 USD | 3,080.00 USD | 3,030.00 USD |
| `7D` | `0.8750` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 5,750.00 USD |
| `1D` | `0.8760` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 6,140.00 USD | 3,510.00 USD | 3,210.00 USD |
| `7D` | `0.8770` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 20,650.00 USD | 6,200.00 USD | 2,760.00 USD |
| `1D` | `0.8780` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 15,310.00 USD | 6,400.00 USD | 10,110.00 USD |
| `7D` | `0.8790` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD |
| `1D` | `0.8800` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 4,390.00 USD | 5,110.00 USD | 5,490.00 USD |
| `7D` | `0.8810` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 228.30 USD | 167.73 USD | 0.00 USD |
| `1D` | `0.8820` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 8,320.00 USD | 3,980.00 USD | 150.13 USD |
| `7D` | `0.8830` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 8,430.00 USD | 5,730.00 USD | 360.61 USD |
| `1D` | `0.8840` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 7,440.00 USD | 1,810.00 USD | 711.93 USD |
| `7D` | `0.8850` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 8,630.00 USD | 5,960.00 USD | 942.02 USD |
| `1D` | `0.8860` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 5,010.00 USD | 1,700.00 USD | 4,210.00 USD |
| `7D` | `0.8870` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 18,520.00 USD | 5,060.00 USD | 6,800.00 USD |
| `1D` | `0.8880` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 17,470.00 USD | 4,180.00 USD | 9,760.00 USD |
| `7D` | `0.8890` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 13,840.00 USD | 5,300.00 USD | 14,810.00 USD |
| `1D` | `0.8900` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 3,630.00 USD | 4,230.00 USD | 4,990.00 USD |
| `7D` | `0.8910` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 30,330.00 USD | 10,730.00 USD | 24,650.00 USD |
| `1D` | `0.8920` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 4,920.00 USD | 3,160.00 USD | 1,950.00 USD |
| `7D` | `0.8930` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 24,780.00 USD | 5,820.00 USD | 9,960.00 USD |
| `1D` | `0.8940` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 4,240.00 USD | 23.75 USD | 966.50 USD |
| `7D` | `0.8950` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 7,380.00 USD | 9,390.00 USD | 27,510.00 USD |
| `1D` | `0.8960` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 1,930.00 USD | 6,130.00 USD | 2,140.00 USD |
| `7D` | `0.8970` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 43,430.00 USD | 5,400.00 USD | 31,920.00 USD |
| `1D` | `0.8980` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 5,550.00 USD | 65.95 USD | 992.14 USD |
| `7D` | `0.8990` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 52,250.00 USD | 14,760.00 USD | 20,000.00 USD |
| `1D` | `0.9000` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 3,760.00 USD | 796.93 USD | 2,390.00 USD |
| `7D` | `0.9010` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 20,170.00 USD | 11,690.00 USD | 4,600.00 USD |
| `1D` | `0.9020` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 4,180.00 USD | 3,250.00 USD | 2,320.00 USD |
| `7D` | `0.9030` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 13,100.00 USD | 8,710.00 USD | 25,870.00 USD |
| `1D` | `0.9040` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 3,360.00 USD | 2,560.00 USD | 5,730.00 USD |
| `7D` | `0.9050` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 35,230.00 USD | 25,240.00 USD | 27,300.00 USD |
| `1D` | `0.9060` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 9,620.00 USD | 1,660.00 USD | 111.00 USD |
| `7D` | `0.9070` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 37,740.00 USD | 7,720.00 USD | 15,280.00 USD |
| `1D` | `0.9080` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 5,800.00 USD | 3,150.00 USD | 3,500.00 USD |
| `7D` | `0.9090` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 14,170.00 USD | 8,050.00 USD | 6,240.00 USD |
| `1D` | `0.9100` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 21,930.00 USD | 2,070.00 USD | 5,600.00 USD |
| `7D` | `0.9110` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 8,490.00 USD | 7,760.00 USD | 17,140.00 USD |
| `1D` | `0.9120` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 4,400.00 USD | 315.61 USD | 3,690.00 USD |
| `7D` | `0.9130` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 26,980.00 USD | 2,230.00 USD | 680.66 USD |
| `1D` | `0.9140` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 6,040.00 USD | 1,290.00 USD | 4,270.00 USD |
| `7D` | `0.9150` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 41,520.00 USD | 10,930.00 USD | 34,610.00 USD |
| `1D` | `0.9160` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 14,280.00 USD | 131.45 USD | 3,860.00 USD |
| `7D` | `0.9170` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 22,610.00 USD | 14,910.00 USD | 15,830.00 USD |
| `1D` | `0.9180` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 167.33 USD | 484.89 USD | 452.67 USD |
| `7D` | `0.9190` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 33,380.00 USD | 4,860.00 USD | 19,620.00 USD |
| `1D` | `0.9200` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 3,030.00 USD | 166.12 USD | 192.17 USD |
| `7D` | `0.9210` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 22,590.00 USD | 7,000.00 USD | 15,880.00 USD |
| `1D` | `0.9220` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 22,330.00 USD | 4,870.00 USD | 12,540.00 USD |
| `7D` | `0.9230` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 35,230.00 USD | 11,030.00 USD | 37,340.00 USD |
| `1D` | `0.9240` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 14,520.00 USD | 5,440.00 USD | 36.99 USD |
| `7D` | `0.9250` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 82,280.00 USD | 17,010.00 USD | 45,620.00 USD |
| `1D` | `0.9260` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 11,040.00 USD | 13,740.00 USD | 26,260.00 USD |
| `7D` | `0.9270` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 70,300.00 USD | 9,380.00 USD | 22,080.00 USD |
| `1D` | `0.9280` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 43,650.00 USD | 4,700.00 USD | 5,930.00 USD |
| `7D` | `0.9290` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 39,160.00 USD | 6,760.00 USD | 31,840.00 USD |
| `1D` | `0.9300` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 14,980.00 USD | 1,340.00 USD | 16,320.00 USD |
| `7D` | `0.9310` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 37,460.00 USD | 10,070.00 USD | 7,590.00 USD |
| `1D` | `0.9320` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 27,830.00 USD | 13,360.00 USD | 9,470.00 USD |
| `7D` | `0.9330` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 33,550.00 USD | 9,670.00 USD | 25,450.00 USD |
| `1D` | `0.9340` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 21,510.00 USD | 11,340.00 USD | 10,720.00 USD |
| `7D` | `0.9350` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 82,010.00 USD | 29,330.00 USD | 17,380.00 USD |
| `1D` | `0.9360` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 49,420.00 USD | 11,180.00 USD | 19,340.00 USD |
| `7D` | `0.9370` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 29,580.00 USD | 14,910.00 USD | 7,230.00 USD |
| `1D` | `0.9380` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 25,680.00 USD | 14,710.00 USD | 10,680.00 USD |
| `7D` | `0.9390` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 18,750.00 USD | 14,310.00 USD | 12,530.00 USD |
| `1D` | `0.9400` | 982,310.00 USD | 0.00 USD | 982,310.00 USD | 28,130.00 USD | 10,650.00 USD | 24,010.00 USD |
| `7D` | `0.9410` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 45,790.00 USD | 14,660.00 USD | 4,310.00 USD |
| `1D` | `0.9420` | 919,520.00 USD | 0.00 USD | 919,520.00 USD | 58,960.00 USD | 23,370.00 USD | 12,090.00 USD |
| `7D` | `0.9430` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 54,680.00 USD | 18,070.00 USD | 11,600.00 USD |
| `1D` | `0.9440` | 825,100.00 USD | 0.00 USD | 825,100.00 USD | 35,560.00 USD | 18,570.00 USD | 7,540.00 USD |
| `7D` | `0.9450` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 137,080.00 USD | 49,320.00 USD | 73,090.00 USD |
| `1D` | `0.9460` | 763,420.00 USD | 0.00 USD | 763,420.00 USD | 46,890.00 USD | 38,090.00 USD | 70,930.00 USD |
| `7D` | `0.9470` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 125,790.00 USD | 24,210.00 USD | 51,460.00 USD |
| `1D` | `0.9480` | 607,510.00 USD | 0.00 USD | 607,510.00 USD | 134,950.00 USD | 28,180.00 USD | 40,740.00 USD |
| `7D` | `0.9490` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 129,370.00 USD | 34,600.00 USD | 122,500.00 USD |
| `1D` | `0.9500` | 403,650.00 USD | 0.00 USD | 403,650.00 USD | 40,200.00 USD | 9,030.00 USD | 39,140.00 USD |
| `7D` | `0.9510` | 959,780.00 USD | 0.00 USD | 959,780.00 USD | 229,420.00 USD | 44,120.00 USD | 81,400.00 USD |
| `1D` | `0.9520` | 315,270.00 USD | 0.00 USD | 315,270.00 USD | 73,640.00 USD | 33,830.00 USD | 23,670.00 USD |
| `7D` | `0.9530` | 604,840.00 USD | 0.00 USD | 604,840.00 USD | 79,700.00 USD | 27,910.00 USD | 123,120.00 USD |
| `1D` | `0.9540` | 184,120.00 USD | 0.00 USD | 184,120.00 USD | 52,780.00 USD | 30,680.00 USD | 29,540.00 USD |
| `7D` | `0.9550` | 374,100.00 USD | 0.00 USD | 374,100.00 USD | 172,820.00 USD | 89,220.00 USD | 21,050.00 USD |
| `1D` | `0.9560` | 71,130.00 USD | 0.00 USD | 71,130.00 USD | 49,230.00 USD | 20,890.00 USD | 419.82 USD |
| `7D` | `0.9570` | 91,020.00 USD | 0.00 USD | 91,020.00 USD | 20,700.00 USD | 0.00 USD | 6,910.00 USD |
| `7D` | `0.9590` | 63,410.00 USD | 0.00 USD | 63,410.00 USD | 16,080.00 USD | 0.00 USD | 1,700.00 USD |
| `7D` | `0.9610` | 45,620.00 USD | 0.00 USD | 45,620.00 USD | 24,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9630` | 21,250.00 USD | 0.00 USD | 21,250.00 USD | 12,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9650` | 8,280.00 USD | 0.00 USD | 8,280.00 USD | 8,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9660` | 595.80 USD | 0.00 USD | 595.80 USD | 595.80 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9680` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9690` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9690` | 47,560.00 USD | 47,560.00 USD | 0.00 USD | 0.00 USD | 11,390.00 USD | 36,160.00 USD |
| `1D` | `0.9700` | 19,790.00 USD | 19,790.00 USD | 0.00 USD | 0.00 USD | 82.70 USD | 19,710.00 USD |
| `7D` | `0.9710` | 71,690.00 USD | 71,690.00 USD | 0.00 USD | 0.00 USD | 14,530.00 USD | 9,610.00 USD |
| `1D` | `0.9720` | 65,590.00 USD | 65,590.00 USD | 0.00 USD | 23,620.00 USD | 0.00 USD | 22,180.00 USD |
| `7D` | `0.9730` | 79,200.00 USD | 79,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,510.00 USD |
| `1D` | `0.9740` | 89,420.00 USD | 89,420.00 USD | 0.00 USD | 9,580.00 USD | 0.00 USD | 14,240.00 USD |
| `7D` | `0.9750` | 99,070.00 USD | 99,070.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 3,280.00 USD |
| `1D` | `0.9760` | 130,730.00 USD | 130,730.00 USD | 0.00 USD | 19,600.00 USD | 13,960.00 USD | 7,740.00 USD |
| `7D` | `0.9770` | 151,280.00 USD | 151,280.00 USD | 0.00 USD | 15,320.00 USD | 5,480.00 USD | 31,410.00 USD |
| `1D` | `0.9780` | 171,140.00 USD | 171,140.00 USD | 0.00 USD | 22,490.00 USD | 0.00 USD | 17,920.00 USD |
| `7D` | `0.9790` | 236,200.00 USD | 236,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 84,920.00 USD |
| `1D` | `0.9800` | 229,840.00 USD | 229,840.00 USD | 0.00 USD | 28,330.00 USD | 9,580.00 USD | 20,800.00 USD |
| `7D` | `0.9810` | 354,090.00 USD | 354,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 117,890.00 USD |
| `1D` | `0.9820` | 264,860.00 USD | 264,860.00 USD | 0.00 USD | 15,980.00 USD | 12,160.00 USD | 6,870.00 USD |
| `7D` | `0.9830` | 474,070.00 USD | 474,070.00 USD | 0.00 USD | 52,130.00 USD | 15,600.00 USD | 52,260.00 USD |
| `1D` | `0.9840` | 305,510.00 USD | 305,510.00 USD | 0.00 USD | 0.00 USD | 8,340.00 USD | 32,310.00 USD |
| `7D` | `0.9850` | 496,380.00 USD | 496,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,300.00 USD |
| `1D` | `0.9860` | 353,610.00 USD | 353,610.00 USD | 0.00 USD | 39,150.00 USD | 3,460.00 USD | 5,490.00 USD |
| `7D` | `0.9870` | 537,760.00 USD | 537,760.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 1,370.00 USD |
| `1D` | `0.9880` | 354,670.00 USD | 354,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,060.00 USD |
| `7D` | `0.9890` | 559,670.00 USD | 559,670.00 USD | 0.00 USD | 20,470.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `0.9900` | 426,750.00 USD | 426,750.00 USD | 0.00 USD | 57,390.00 USD | 1,300.00 USD | 13,390.00 USD |
| `7D` | `0.9910` | 579,260.00 USD | 579,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD |
| `1D` | `0.9920` | 439,630.00 USD | 439,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,880.00 USD |
| `7D` | `0.9930` | 580,480.00 USD | 580,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,220.00 USD |
| `1D` | `0.9940` | 459,790.00 USD | 459,790.00 USD | 0.00 USD | 6,920.00 USD | 13,250.00 USD | 0.00 USD |
| `7D` | `0.9950` | 639,760.00 USD | 639,760.00 USD | 0.00 USD | 16,510.00 USD | 0.00 USD | 42,770.00 USD |
| `1D` | `0.9960` | 462,420.00 USD | 462,420.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD | 0.00 USD |
| `7D` | `0.9970` | 712,840.00 USD | 712,840.00 USD | 0.00 USD | 68,870.00 USD | 0.00 USD | 4,210.00 USD |
| `1D` | `0.9980` | 518,130.00 USD | 518,130.00 USD | 0.00 USD | 40,410.00 USD | 4,790.00 USD | 10,500.00 USD |
| `1D` | `1.00` | 602,020.00 USD | 602,020.00 USD | 0.00 USD | 50,740.00 USD | 31,440.00 USD | 1,710.00 USD |
| `7D` | `1.00` | 765,690.00 USD | 765,690.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.00` | 602,280.00 USD | 602,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 266.05 USD |
| `7D` | `1.00` | 882,720.00 USD | 882,720.00 USD | 0.00 USD | 78,440.00 USD | 21,740.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 630,750.00 USD | 630,750.00 USD | 0.00 USD | 10,110.00 USD | 9,540.00 USD | 8,820.00 USD |
| `7D` | `1.00` | 904,010.00 USD | 904,010.00 USD | 0.00 USD | 19,830.00 USD | 0.00 USD | 1,470.00 USD |
| `1D` | `1.01` | 758,520.00 USD | 758,520.00 USD | 0.00 USD | 95,330.00 USD | 8,600.00 USD | 23,830.00 USD |
| `7D` | `1.01` | 939,150.00 USD | 939,150.00 USD | 0.00 USD | 34,110.00 USD | 0.00 USD | 1,030.00 USD |
| `1D` | `1.01` | 780,400.00 USD | 780,400.00 USD | 0.00 USD | 255.10 USD | 6,910.00 USD | 14,710.00 USD |
| `7D` | `1.01` | 964,890.00 USD | 964,890.00 USD | 0.00 USD | 10,230.00 USD | 0.00 USD | 15,500.00 USD |
| `1D` | `1.01` | 799,720.00 USD | 799,720.00 USD | 0.00 USD | 10,530.00 USD | 8,790.00 USD | 0.00 USD |
| `7D` | `1.01` | 999,150.00 USD | 999,150.00 USD | 0.00 USD | 20,090.00 USD | 14,180.00 USD | 0.00 USD |
| `1D` | `1.01` | 841,460.00 USD | 841,460.00 USD | 0.00 USD | 16,240.00 USD | 25,350.00 USD | 155.80 USD |
| `7D` | `1.01` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD |
| `1D` | `1.01` | 876,480.00 USD | 876,480.00 USD | 0.00 USD | 5,630.00 USD | 4,370.00 USD | 25,020.00 USD |
| `7D` | `1.01` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 26,360.00 USD | 7,070.00 USD |
| `1D` | `1.02` | 916,950.00 USD | 916,950.00 USD | 0.00 USD | 20,120.00 USD | 75.20 USD | 20,270.00 USD |
| `7D` | `1.02` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD |
| `1D` | `1.02` | 953,960.00 USD | 953,960.00 USD | 0.00 USD | 6,290.00 USD | 8,490.00 USD | 22,230.00 USD |
| `7D` | `1.02` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 75,760.00 USD | 11,810.00 USD |
| `1D` | `1.02` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 44,710.00 USD | 4,370.00 USD | 15,110.00 USD |
| `7D` | `1.02` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 44,170.00 USD | 32,840.00 USD | 68,050.00 USD |
| `1D` | `1.02` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 51,380.00 USD | 3,670.00 USD | 21,450.00 USD |
| `7D` | `1.02` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 66,990.00 USD | 85,890.00 USD | 146,060.00 USD |
| `1D` | `1.02` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 50,330.00 USD | 25,640.00 USD | 53,210.00 USD |
| `7D` | `1.02` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 28,320.00 USD | 48,490.00 USD | 29,170.00 USD |
| `1D` | `1.03` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 52,170.00 USD | 18,370.00 USD | 20,210.00 USD |
| `7D` | `1.03` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 160,800.00 USD | 127,000.00 USD | 25,260.00 USD |
| `1D` | `1.03` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 31,340.00 USD | 10,940.00 USD | 18,480.00 USD |
| `7D` | `1.03` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 142,240.00 USD | 38,750.00 USD | 30,660.00 USD |
| `1D` | `1.03` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 95,330.00 USD | 24,510.00 USD | 33,610.00 USD |
| `7D` | `1.03` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 170,960.00 USD | 7,350.00 USD | 19,590.00 USD |
| `1D` | `1.03` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 69,820.00 USD | 8,980.00 USD | 35,950.00 USD |
| `7D` | `1.03` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD |
| `1D` | `1.03` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 38,330.00 USD | 9,300.00 USD | 21,490.00 USD |
| `7D` | `1.03` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 259,060.00 USD | 8,290.00 USD | 43,490.00 USD |
| `1D` | `1.04` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 18,100.00 USD | 13,840.00 USD | 32,400.00 USD |
| `7D` | `1.04` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 192,080.00 USD | 3,170.00 USD | 109,460.00 USD |
| `1D` | `1.04` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 62,580.00 USD | 3,190.00 USD | 23,430.00 USD |
| `7D` | `1.04` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 239,580.00 USD | 9,010.00 USD | 117,630.00 USD |
| `1D` | `1.04` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 7,790.00 USD | 8,100.00 USD | 9,830.00 USD |
| `7D` | `1.04` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 276,890.00 USD | 2,090.00 USD | 159,500.00 USD |
| `1D` | `1.04` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 11,290.00 USD | 9,870.00 USD | 8,370.00 USD |
| `7D` | `1.04` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD |
| `1D` | `1.04` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 7,410.00 USD | 9,310.00 USD | 32,800.00 USD |
| `7D` | `1.04` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD |
| `1D` | `1.05` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 21,730.00 USD | 4,160.00 USD | 321.14 USD |
| `7D` | `1.05` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 178,890.00 USD | 96,370.00 USD | 238,570.00 USD |
| `1D` | `1.05` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 8,680.00 USD | 3,210.00 USD | 4,880.00 USD |
| `7D` | `1.05` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 116,670.00 USD | 13,780.00 USD | 77,320.00 USD |
| `1D` | `1.05` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 39,540.00 USD | 8,970.00 USD | 13,550.00 USD |
| `7D` | `1.05` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 175,210.00 USD | 43,690.00 USD | 87,050.00 USD |
| `1D` | `1.05` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 23,270.00 USD | 1,310.00 USD | 15,610.00 USD |
| `7D` | `1.05` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 61,670.00 USD | 55,920.00 USD | 74,380.00 USD |
| `1D` | `1.05` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 8,900.00 USD | 340.84 USD | 6,470.00 USD |
| `7D` | `1.05` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 125,020.00 USD | 33,860.00 USD | 72,330.00 USD |
| `1D` | `1.06` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 13,640.00 USD | 3,680.00 USD | 13,750.00 USD |
| `7D` | `1.06` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 218,860.00 USD | 70,000.00 USD | 106,190.00 USD |
| `1D` | `1.06` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 29,640.00 USD | 3,000.00 USD | 13,720.00 USD |
| `7D` | `1.06` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 229,940.00 USD | 74,380.00 USD | 145,470.00 USD |
| `1D` | `1.06` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 3,850.00 USD | 4,510.00 USD | 8,650.00 USD |
| `7D` | `1.06` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 140,850.00 USD | 56,310.00 USD | 78,020.00 USD |
| `1D` | `1.06` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 1,990.00 USD | 3,730.00 USD | 2,070.00 USD |
| `7D` | `1.06` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 141,700.00 USD | 73,690.00 USD | 71,340.00 USD |
| `1D` | `1.06` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 12,920.00 USD | 3,060.00 USD | 5,990.00 USD |
| `7D` | `1.06` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 90,670.00 USD | 28,390.00 USD | 83,920.00 USD |
| `1D` | `1.07` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 12,670.00 USD | 141.60 USD | 5,790.00 USD |
| `7D` | `1.07` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 86,760.00 USD | 43,390.00 USD | 82,980.00 USD |
| `1D` | `1.07` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 7,520.00 USD | 4,330.00 USD | 3,180.00 USD |
| `7D` | `1.07` | 8,070,000.00 USD | 8,070,000.00 USD | 0.00 USD | 219,670.00 USD | 14,440.00 USD | 62,270.00 USD |
| `1D` | `1.07` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 7,140.00 USD | 3,900.00 USD | 3,210.00 USD |
| `7D` | `1.07` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 141,570.00 USD | 36,670.00 USD | 52,290.00 USD |
| `1D` | `1.07` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 9,330.00 USD | 2,350.00 USD | 3,180.00 USD |
| `7D` | `1.07` | 8,540,000.00 USD | 8,540,000.00 USD | 0.00 USD | 96,630.00 USD | 42,960.00 USD | 95,510.00 USD |
| `1D` | `1.07` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 7,860.00 USD | 4,630.00 USD | 6,930.00 USD |
| `7D` | `1.07` | 8,730,000.00 USD | 8,730,000.00 USD | 0.00 USD | 97,650.00 USD | 27,560.00 USD | 60,670.00 USD |
| `1D` | `1.08` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 5,350.00 USD | 5,330.00 USD | 5,490.00 USD |
| `7D` | `1.08` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 75,040.00 USD | 29,910.00 USD | 48,910.00 USD |
| `1D` | `1.08` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 9,430.00 USD | 4,070.00 USD | 150.13 USD |
| `7D` | `1.08` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 166,380.00 USD | 21,060.00 USD | 52,480.00 USD |
| `1D` | `1.08` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 7,700.00 USD | 1,870.00 USD | 711.93 USD |
| `7D` | `1.08` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 164,440.00 USD | 26,480.00 USD | 33,950.00 USD |
| `1D` | `1.08` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 5,280.00 USD | 1,790.00 USD | 4,210.00 USD |
| `7D` | `1.08` | 9,550,000.00 USD | 9,550,000.00 USD | 0.00 USD | 61,330.00 USD | 41,110.00 USD | 100,750.00 USD |
| `1D` | `1.08` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 9,180.00 USD | 1,500.00 USD | 2,780.00 USD |
| `7D` | `1.08` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 86,400.00 USD | 18,540.00 USD | 46,440.00 USD |
| `1D` | `1.09` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 8,920.00 USD | 2,900.00 USD | 6,970.00 USD |
| `7D` | `1.09` | 9,930,000.00 USD | 9,930,000.00 USD | 0.00 USD | 102,510.00 USD | 58,170.00 USD | 69,410.00 USD |
| `1D` | `1.09` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 3,630.00 USD | 4,290.00 USD | 4,990.00 USD |
| `7D` | `1.09` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 71,650.00 USD | 23,140.00 USD | 85,300.00 USD |
| `1D` | `1.09` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 5,220.00 USD | 3,140.00 USD | 1,950.00 USD |
| `7D` | `1.09` | 10,240,000.00 USD | 10,240,000.00 USD | 0.00 USD | 70,660.00 USD | 25,660.00 USD | 32,870.00 USD |
| `1D` | `1.09` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 4,370.00 USD | 0.00 USD | 966.50 USD |
| `7D` | `1.09` | 10,400,000.00 USD | 10,400,000.00 USD | 0.00 USD | 59,280.00 USD | 39,220.00 USD | 62,330.00 USD |
| `1D` | `1.09` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 2,440.00 USD | 2,050.00 USD |
| `7D` | `1.09` | 10,570,000.00 USD | 10,570,000.00 USD | 0.00 USD | 56,240.00 USD | 22,740.00 USD | 92,520.00 USD |
| `7D` | `1.10` | 10,710,000.00 USD | 10,710,000.00 USD | 0.00 USD | 88,860.00 USD | 11,400.00 USD | 38,150.00 USD |
| `7D` | `1.10` | 11,040,000.00 USD | 11,040,000.00 USD | 0.00 USD | 188,000.00 USD | 49,370.00 USD | 89,650.00 USD |
| `7D` | `1.10` | 11,220,000.00 USD | 11,220,000.00 USD | 0.00 USD | 122,300.00 USD | 44,140.00 USD | 15,590.00 USD |
| `7D` | `1.10` | 11,440,000.00 USD | 11,440,000.00 USD | 0.00 USD | 91,720.00 USD | 19,430.00 USD | 110,190.00 USD |
| `7D` | `1.10` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 22,500.00 USD | 10,390.00 USD | 31,450.00 USD |
| `7D` | `1.11` | 11,610,000.00 USD | 11,610,000.00 USD | 0.00 USD | 51,840.00 USD | 24,280.00 USD | 34,190.00 USD |
| `7D` | `1.11` | 11,800,000.00 USD | 11,800,000.00 USD | 0.00 USD | 80,930.00 USD | 42,230.00 USD | 63,380.00 USD |
| `7D` | `1.11` | 11,950,000.00 USD | 11,950,000.00 USD | 0.00 USD | 69,040.00 USD | 16,050.00 USD | 64,910.00 USD |
| `7D` | `1.11` | 12,040,000.00 USD | 12,040,000.00 USD | 0.00 USD | 20,190.00 USD | 43,570.00 USD | 25,640.00 USD |
| `7D` | `1.11` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 34,700.00 USD | 6,650.00 USD | 9,990.00 USD |
| `7D` | `1.12` | 12,240,000.00 USD | 12,240,000.00 USD | 0.00 USD | 68,170.00 USD | 45,980.00 USD | 32,030.00 USD |
| `7D` | `1.12` | 12,300,000.00 USD | 12,300,000.00 USD | 0.00 USD | 24,700.00 USD | 22,760.00 USD | 13,750.00 USD |
| `7D` | `1.12` | 12,400,000.00 USD | 12,400,000.00 USD | 0.00 USD | 48,980.00 USD | 30,950.00 USD | 23,330.00 USD |
| `7D` | `1.12` | 12,490,000.00 USD | 12,490,000.00 USD | 0.00 USD | 61,780.00 USD | 5,220.00 USD | 25,460.00 USD |
| `7D` | `1.12` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 18,300.00 USD | 10,940.00 USD | 29,890.00 USD |
| `7D` | `1.13` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 14,700.00 USD | 342.11 USD | 8,690.00 USD |
| `7D` | `1.13` | 12,700,000.00 USD | 12,700,000.00 USD | 0.00 USD | 56,500.00 USD | 19,160.00 USD | 45,770.00 USD |
| `7D` | `1.13` | 12,910,000.00 USD | 12,910,000.00 USD | 0.00 USD | 106,510.00 USD | 12,730.00 USD | 90,150.00 USD |
| `7D` | `1.13` | 13,010,000.00 USD | 13,010,000.00 USD | 0.00 USD | 77,640.00 USD | 3,650.00 USD | 24,710.00 USD |
| `7D` | `1.13` | 13,040,000.00 USD | 13,040,000.00 USD | 0.00 USD | 0.00 USD | 8,380.00 USD | 20,850.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `204.63M` | Total OI Tokens: `211,073,582.5 DOT`
  * 1h OI Change: `-1.13%` | 4h OI Change: `-4.44%` | 24h OI Change: `-8.04%`
  * Exchange Breakdown: Binance=`36.12M` | Bybit=`24.06M` | OKX=`10.11M` | Hyperliquid=`5.60M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.76K` | Last 24h: `7.91K` | Last 3d: `-10.37K` | Last 7d: `-19.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0033%` | **USDT OKX** | `0.0059%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0055%` |
| **USDT MEXC** | `0.0029%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0017%` | **USDT Bitget** | `0.0028%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `61.20%` | `38.80%` | `1.58` | 20,310,000.00 USD |
| `15M` | `Binance` | `60.47%` | `39.53%` | `1.53` | 7,410,000.00 USD |
| `15M` | `OKX` | `59.02%` | `40.98%` | `1.44` | 2,540,000.00 USD |
| `15M` | `Bybit` | `66.59%` | `33.41%` | `1.99` | 2,450,000.00 USD |
| `15M` | `KuCoin` | `47.84%` | `52.16%` | `0.92` | 104,190.00 USD |
| `15M` | `Gate` | `60.52%` | `39.48%` | `1.53` | 327,290.00 USD |
| `15M` | `Bitget` | `66.37%` | `33.63%` | `1.97` | 1,250,000.00 USD |
| `15M` | `BingX` | `53.79%` | `46.21%` | `1.16` | 1,150,000.00 USD |
| `15M` | `MEXC` | `50.36%` | `49.64%` | `1.01` | 1,250,000.00 USD |
| `15M` | `Bitunix` | `70.15%` | `29.85%` | `2.35` | 549,580.00 USD |
| `15M` | `Hyperliquid` | `47.33%` | `52.67%` | `0.90` | 936,930.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `75.5%` | `24.5%` | `3.08` | 479,580.00 USD |
| `15M` | `Crypto.com` | `83.43%` | `16.57%` | `5.04` | 1,520.00 USD |
| `15M` | `WhiteBIT` | `53.02%` | `46.98%` | `1.13` | 738,400.00 USD |
| `15M` | `HTX` | `82.1%` | `17.9%` | `4.59` | 3,030.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `69.54%` | `30.46%` | `2.28` | 295,990.00 USD |
| `15M` | `Aster` | `99.55%` | `0.45%` | `221.22` | 630,600.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `38.32%` | `61.68%` | `0.62` | 198,170.00 USD |
| `15M` | `Whale Positions` | `60.47%` | `39.53%` | `1.53` | 7,410,000.00 USD |
| `15M` | `Global Accounts` | `61.20%` | `38.80%` | `1.58` | 20,310,000.00 USD |
| `1H` | `DOT` | `45.80%` | `54.20%` | `0.85` | 14,700,000.00 USD |
| `1H` | `Binance` | `46.5%` | `53.5%` | `0.87` | 5,420,000.00 USD |
| `1H` | `OKX` | `47.02%` | `52.98%` | `0.89` | 1,610,000.00 USD |
| `1H` | `Bybit` | `41.93%` | `58.07%` | `0.72` | 1,220,000.00 USD |
| `1H` | `KuCoin` | `47.95%` | `52.05%` | `0.92` | 504,120.00 USD |
| `1H` | `Gate` | `50.1%` | `49.9%` | `1.00` | 1,650,000.00 USD |
| `1H` | `Bitget` | `46.05%` | `53.95%` | `0.85` | 720,760.00 USD |
| `1H` | `BingX` | `49.76%` | `50.24%` | `0.99` | 537,870.00 USD |
| `1H` | `MEXC` | `35.8%` | `64.2%` | `0.56` | 910,620.00 USD |
| `1H` | `Bitunix` | `51.2%` | `48.8%` | `1.05` | 443,920.00 USD |
| `1H` | `Hyperliquid` | `58.72%` | `41.28%` | `1.42` | 224,220.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.78%` | `51.22%` | `0.95` | 1,070,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `15.99%` | `84.01%` | `0.19` | 340,100.00 USD |
| `1H` | `HTX` | `35.23%` | `64.77%` | `0.54` | 4,170.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `40.44%` | `59.56%` | `0.68` | 34,650.00 USD |
| `1H` | `Aster` | `8.93%` | `91.07%` | `0.10` | 13,370.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `46.5%` | `53.5%` | `0.87` | 5,420,000.00 USD |
| `1H` | `Global Accounts` | `45.80%` | `54.20%` | `0.85` | 14,700,000.00 USD |
| `4H` | `DOT` | `46.18%` | `53.82%` | `0.86` | 38,720,000.00 USD |
| `4H` | `Binance` | `47.13%` | `52.87%` | `0.89` | 14,260,000.00 USD |
| `4H` | `OKX` | `46.08%` | `53.92%` | `0.85` | 3,800,000.00 USD |
| `4H` | `Bybit` | `45.19%` | `54.81%` | `0.82` | 3,290,000.00 USD |
| `4H` | `KuCoin` | `49.37%` | `50.63%` | `0.98` | 1,810,000.00 USD |
| `4H` | `Gate` | `47.12%` | `52.88%` | `0.89` | 2,650,000.00 USD |
| `4H` | `Bitget` | `48.76%` | `51.24%` | `0.95` | 1,480,000.00 USD |
| `4H` | `BingX` | `42.75%` | `57.25%` | `0.75` | 2,320,000.00 USD |
| `4H` | `MEXC` | `46.25%` | `53.75%` | `0.86` | 2,320,000.00 USD |
| `4H` | `Bitunix` | `48.46%` | `51.54%` | `0.94` | 968,030.00 USD |
| `4H` | `Hyperliquid` | `40.77%` | `59.23%` | `0.69` | 526,080.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.49%` | `48.51%` | `1.06` | 4,000,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `14.1%` | `85.9%` | `0.16` | 1,100,000.00 USD |
| `4H` | `HTX` | `64.21%` | `35.79%` | `1.79` | 43,090.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `48.98%` | `51.02%` | `0.96` | 116,090.00 USD |
| `4H` | `Aster` | `15.87%` | `84.13%` | `0.19` | 23,330.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `47.13%` | `52.87%` | `0.89` | 14,260,000.00 USD |
| `4H` | `Global Accounts` | `46.18%` | `53.82%` | `0.86` | 38,720,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.9900` | `0.9907` | `0.9900` | `0.9929` | `0.9876` | 406,034.57 USD | 195,166.38 USD | 210,868.18 USD | -15,701.80 USD | `-3.87%` | `3B / 8S` |
| `5:00 UTC` | `0.9850` | `0.9875` | `0.9850` | `0.9919` | `0.9848` | 373,179.10 USD | 160,064.27 USD | 213,114.83 USD | -53,050.55 USD | `-14.22%` | `10B / 18S` |
| `0:00 UTC` | `0.9787` | `0.9807` | `0.9787` | `0.9872` | `0.9767` | 1,756,422.05 USD | 785,190.37 USD | 971,231.69 USD | -186,041.32 USD | `-10.59%` | `9B / 23S` |
| `5:00 UTC` | `0.9813` | `0.9827` | `0.9813` | `0.9867` | `0.9789` | 947,049.41 USD | 720,261.00 USD | 226,788.42 USD | 493,472.58 USD | `+52.11%` | `28B / 1S` |
| `0:00 UTC` | `0.9805` | `0.9815` | `0.9805` | `0.9849` | `0.9787` | 512,523.44 USD | 243,023.57 USD | 269,499.87 USD | -26,476.30 USD | `-5.17%` | `12B / 6S` |
| `5:00 UTC` | `0.9856` | `0.9822` | `0.9856` | `0.9858` | `0.9780` | 526,140.64 USD | 318,567.26 USD | 207,573.38 USD | 110,993.88 USD | `+21.10%` | `16B / 9S` |
| `0:00 UTC` | `0.9873` | `0.9868` | `0.9873` | `0.9887` | `0.9839` | 407,897.05 USD | 216,028.73 USD | 191,868.32 USD | 24,160.41 USD | `+5.92%` | `8B / 4S` |
| `5:00 UTC` | `0.9858` | `0.9859` | `0.9858` | `0.9880` | `0.9839` | 388,071.33 USD | 177,551.18 USD | 210,520.15 USD | -32,968.97 USD | `-8.50%` | `3B / 8S` |
| `0:00 UTC` | `0.9681` | `0.9669` | `0.9681` | `0.9851` | `0.9557` | 3,728,299.49 USD | 1,667,776.70 USD | 2,060,522.79 USD | -392,746.09 USD | `-10.53%` | `7B / 26S` |
| `5:00 UTC` | `0.9697` | `0.9698` | `0.9697` | `0.9718` | `0.9674` | 350,445.31 USD | 171,345.50 USD | 179,099.81 USD | -7,754.31 USD | `-2.21%` | `4B / 6S` |

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
| `5m` | -4,150.00 USD | 27,800.00 USD | **`ACCUMULATION`** |
| `15m` | -55,190.00 USD | 106,660.00 USD | **`ACCUMULATION`** |
| `30m` | -283,690.00 USD | -906,580.00 USD | **`DISTRIBUTION`** |
| `1h` | -241,130.00 USD | -624,510.00 USD | **`DISTRIBUTION`** |
| `2h` | -283,240.00 USD | -291,630.00 USD | **`DISTRIBUTION`** |
| `4h` | -345,700.00 USD | -1,430,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -424,510.00 USD | -2,170,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -311,190.00 USD | -2,350,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -490,400.00 USD | -2,630,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -647,590.00 USD | -2,540,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,660,000.00 USD | -18,870,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,850,000.00 USD | -73,320,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-4.15K` | 15m=`-55.19K` | 1h=`-241.13K` | 24h=`-647.59K`
* Futures Capital Netflows: 5m=`+27.80K` | 15m=`+106.66K` | 1h=`-624.51K` | 24h=`-2.54M`
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
  * `2026-10-30 01:36:09 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:09 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:51:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.9540` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.9138` (Risk Distance: `0.0402` pts)
  * +2.5R Take Profit: `1.05`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9934` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.03` (Risk Distance: `0.0402` pts)
  * +2.5R Take Profit: `0.8929`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9768`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
