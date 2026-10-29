# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 23:43:52 IST` (`2026-10-29 18:13:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9810` | **Live Ask Quote**: `1.00` | **Mid Price**: `0.9910`
- **Spread Points**: `20.00` | **Spread BPS**: `201.82 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.9778` | VWAP Z-Score: `+0.22` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0076` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `44.10` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.02` | Lower -3.00σ Band: `0.9341`
  * Upper +2.51σ Band: `1.01` | Lower -2.51σ Band: `0.9412`
  * Upper +2.01σ Band: `1.01` | Lower -2.01σ Band: `0.9485`
  * Upper +2.00σ Band: `1.01` | Lower -2.00σ Band: `0.9487`
  * Upper +1.28σ Band: `0.9965` | Lower -1.28σ Band: `0.9592`
  * Upper +1.00σ Band: `0.9924` | Lower -1.00σ Band: `0.9632`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9894` | EMA-20=`0.9890` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9842` (Slope: `+0.0000`) | EMA-100=`0.9839`
  * Institutional Anchors: EMA-144=`0.9847` | EMA-200=`0.9852` (Slope: `+0.1169`) | EMA-233=`0.9849`
- **Range Boundaries**: 24H High=`1.03` | 24H Low=`0.9510` | Weekly High=`1.03` | Weekly Low=`0.9510`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9947` (Distance: `-0.28%`)
  * Point of Control (POC) = `0.9630` (Distance: `+3.01%`)
  * Value Area Low (VAL) = `0.9530` (Distance: `+4.09%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.00` | POC=`0.9890` | VAL=`0.9812`
  * Prior Day Extremes: PDH=`1.03` | PDL=`0.9690` | PDC=`1.01`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.01` | Weekly POC=`0.9929` | Weekly VAL=`0.9779`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.02` | Low=`0.9510`
  * London Session (08:00-16:00 UTC): High=`0.9850` | Low=`0.9600`
  * New York Session (13:00-21:00 UTC): High=`1.01` | Low=`0.9680`
  * Initial Balance (First Hour): IB High=`0.9800` | IB Low=`0.9670`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9870` - `0.9950`
  * Optimal Trade Entry (OTE 0.705): `0.9930`
  * Structural Invalidation Anchor (0.786): `0.9989`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9889` | `0.9918` | `0.9886` | `0.9918` | `141,428` | 140,062.63 USD | 7,643.37 USD | `+5.46%` | -1,965,705.49 USD | `+0.47` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.9918` | `0.9927` | `0.9896` | `0.9912` | `197,906` | 196,179.49 USD | 30,885.30 USD | `+15.74%` | -1,934,820.19 USD | `+0.70` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.9912` | `0.9921` | `0.9910` | `0.9921` | `15,454` | 15,322.26 USD | 4,069.08 USD | `+26.56%` | -1,930,751.11 USD | `+0.37` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.00` | `1.00` | `0.9922` | `0.9937` | `744,852` | 743,609.00 USD | -219,713.36 USD | `-29.55%` | -1,731,250.68 USD | `-0.83` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9936` | `0.9945` | `0.9847` | `0.9918` | `989,782` | 979,161.78 USD | -192,740.33 USD | `-19.68%` | -1,923,991.00 USD | `-0.65` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9918` | `0.9927` | `0.9896` | `0.9921` | `213,361` | 211,501.75 USD | 34,954.38 USD | `+16.53%` | -1,889,036.62 USD | `+0.48` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.02` | `1.02` | `1.00` | `1.01` | `2,867,696` | 2,902,881.51 USD | -734,347.44 USD | `-25.30%` | -1,262,302.27 USD | `-2.29` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.01` | `1.01` | `0.9847` | `0.9918` | `3,301,086` | 3,291,262.18 USD | -377,105.92 USD | `-11.46%` | -1,639,408.20 USD | `-1.10` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.9918` | `0.9927` | `0.9896` | `0.9922` | `215,204` | 213,329.89 USD | 36,688.47 USD | `+17.20%` | -1,602,719.72 USD | `+0.20` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | -137,778.42 USD | `+0.23` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | -315,355.23 USD | `-0.25` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9847` | `0.9922` | `6,383,986` | 6,407,473.59 USD | -1,074,764.89 USD | `-16.77%` | -1,390,120.13 USD | `-1.49` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.01` | `1.01` | `0.9612` | `0.9700` | `15,616,467` | 15,304,422.31 USD | 595,816.59 USD | `+3.89%` | -236,044.76 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.9699` | `0.9906` | `0.9674` | `0.9732` | `8,505,701` | 8,320,368.15 USD | 13,201.93 USD | `+0.16%` | -222,842.83 USD | `+0.15` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | -137,778.42 USD | `+0.23` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | -315,355.23 USD | `-0.25` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9847` | `0.9922` | `6,383,986` | 6,407,473.59 USD | -1,074,764.89 USD | `-16.77%` | -1,390,120.13 USD | `-1.49` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`0.9910`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:36:01 IST` |

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
  * 24H Horizon: Short MP=`1.04` (Vol: 74,700.00 USD, Dist: `+4.87%`) | Long MP=`0.9649` (Vol: 113,700.00 USD, Dist: `--2.44%`)
  * 48H Horizon: Short MP=`1.04` (Vol: 74,700.00 USD, Dist: `+4.87%`) | Long MP=`0.9649` (Vol: 113,700.00 USD, Dist: `--2.44%`)
  * 3D Horizon: Short MP=`1.04` (Vol: 74,700.00 USD, Dist: `+4.87%`) | Long MP=`0.9510` (Vol: 130,500.00 USD, Dist: `--3.84%`)
  * 7D Horizon: Short MP=`1.07` (Vol: 211,000.00 USD, Dist: `+8.02%`) | Long MP=`0.9606` (Vol: 177,500.00 USD, Dist: `--2.87%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2465` | 123.25 USD | 565,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3085` | 557.06 USD | 565,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3345` | 738.91 USD | 565,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3605` | 2,050.00 USD | 564,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3825` | 122.13 USD | 562,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 2,790.00 USD | 562,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4425` | 175.45 USD | 559,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4695` | 2,580.00 USD | 559,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4785` | 947.38 USD | 556,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4885` | 11,910.00 USD | 555,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4965` | 198.95 USD | 543,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5115` | 606.38 USD | 543,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 4,130.00 USD | 542,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5465` | 106.84 USD | 538,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 577.36 USD | 538,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 137.53 USD | 538,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5955` | 3,390.00 USD | 538,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6055` | 1,480.00 USD | 534,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6065` | 1,800.00 USD | 533,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6115` | 149.57 USD | 531,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 105.96 USD | 531,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 147.48 USD | 531,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6245` | 525.77 USD | 530,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 757.80 USD | 530,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 106.00 USD | 529,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 20,270.00 USD | 529,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 4,230.00 USD | 509,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 202.47 USD | 505,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 149.44 USD | 504,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 63,890.00 USD | 504,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 423.10 USD | 440,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6825` | 264.67 USD | 440,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 247.91 USD | 440,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6855` | 2,110.00 USD | 439,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6955` | 322.16 USD | 437,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6975` | 697.50 USD | 437,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6995` | 156.27 USD | 436,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7055` | 176.38 USD | 436,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 16,520.00 USD | 436,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 988.87 USD | 419,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7175` | 322.88 USD | 418,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7205` | 866.26 USD | 418,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 1,090.00 USD | 417,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7275` | 126.44 USD | 416,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 291.18 USD | 416,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 2,300.00 USD | 416,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,140.00 USD | 413,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 283.30 USD | 412,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7415` | 1,380.00 USD | 412,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 331.18 USD | 411,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 2,390.00 USD | 410,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7605` | 834.88 USD | 408,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 1,580.00 USD | 407,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 292.03 USD | 405,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7895` | 20,380.00 USD | 405,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7925` | 157.95 USD | 385,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7965` | 3,360.00 USD | 385,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8025` | 238.90 USD | 381,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8045` | 566.61 USD | 381,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8055` | 699.01 USD | 380,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8125` | 13,440.00 USD | 380,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 366,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 366,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8285` | 1,890.00 USD | 364,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8325` | 8,990.00 USD | 362,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 353,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8375` | 167.00 USD | 353,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,240.00 USD | 352,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8445` | 168.31 USD | 351,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 351,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8565` | 170.70 USD | 350,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 350,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8595` | 171.38 USD | 349,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8625` | 309.55 USD | 349,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 348,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 348,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8665` | 118.54 USD | 348,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8730` | 5,160,000.00 USD | 5,160,000.00 USD | 4,750.00 USD | 2,080.00 USD | 295.31 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 301.30 USD | 5,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 171.88 USD | 348,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8770` | 5,150,000.00 USD | 5,150,000.00 USD | 20,650.00 USD | 5,900.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 5,120,000.00 USD | 5,120,000.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8795` | 948.01 USD | 348,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8810` | 5,110,000.00 USD | 5,110,000.00 USD | 228.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8830` | 5,110,000.00 USD | 5,110,000.00 USD | 8,430.00 USD | 6,110.00 USD | 360.61 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8850` | 2,510,000.00 USD | 2,510,000.00 USD | 10,630.00 USD | 1,790.00 USD | 2,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8850` | 5,100,000.00 USD | 5,100,000.00 USD | 8,630.00 USD | 2,860.00 USD | 698.60 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8870` | 2,500,000.00 USD | 2,500,000.00 USD | 6,560.00 USD | 3,430.00 USD | 8,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8870` | 5,080,000.00 USD | 5,080,000.00 USD | 11,700.00 USD | 5,060.00 USD | 6,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8890` | 2,480,000.00 USD | 2,480,000.00 USD | 3,730.00 USD | 3,370.00 USD | 6,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8890` | 5,060,000.00 USD | 5,060,000.00 USD | 13,840.00 USD | 5,300.00 USD | 14,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8910` | 2,470,000.00 USD | 2,470,000.00 USD | 1,820.00 USD | 1,560.00 USD | 2,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8910` | 5,030,000.00 USD | 5,030,000.00 USD | 30,330.00 USD | 10,770.00 USD | 24,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8915` | 41,900.00 USD | 347,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8925` | 526.84 USD | 305,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8930` | 2,460,000.00 USD | 2,460,000.00 USD | 7,320.00 USD | 2,470.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8930` | 4,960,000.00 USD | 4,960,000.00 USD | 24,780.00 USD | 5,700.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8935` | 9,170.00 USD | 304,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8950` | 2,450,000.00 USD | 2,450,000.00 USD | 22.75 USD | 2,530.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8950` | 4,920,000.00 USD | 4,920,000.00 USD | 7,380.00 USD | 10,990.00 USD | 27,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8970` | 2,450,000.00 USD | 2,450,000.00 USD | 5,360.00 USD | 4,910.00 USD | 9,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8970` | 4,880,000.00 USD | 4,880,000.00 USD | 43,430.00 USD | 5,260.00 USD | 31,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8990` | 2,430,000.00 USD | 2,430,000.00 USD | 5,550.00 USD | 757.19 USD | 1,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8990` | 4,800,000.00 USD | 4,800,000.00 USD | 52,250.00 USD | 14,420.00 USD | 20,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8995` | 3,820.00 USD | 295,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9010` | 2,420,000.00 USD | 2,420,000.00 USD | 15.65 USD | 39.59 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9010` | 4,710,000.00 USD | 4,710,000.00 USD | 20,170.00 USD | 11,360.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9030` | 2,420,000.00 USD | 2,420,000.00 USD | 6,430.00 USD | 3,760.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9030` | 4,670,000.00 USD | 4,670,000.00 USD | 12,700.00 USD | 9,020.00 USD | 25,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9035` | 180.16 USD | 291,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9050` | 2,400,000.00 USD | 2,400,000.00 USD | 8,300.00 USD | 3,640.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9050` | 4,620,000.00 USD | 4,620,000.00 USD | 35,230.00 USD | 25,340.00 USD | 27,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9070` | 2,390,000.00 USD | 2,390,000.00 USD | 3,810.00 USD | 488.01 USD | 803.91 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9070` | 4,540,000.00 USD | 4,540,000.00 USD | 37,740.00 USD | 8,280.00 USD | 15,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9090` | 2,380,000.00 USD | 2,380,000.00 USD | 18,830.00 USD | 4,070.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9090` | 4,480,000.00 USD | 4,480,000.00 USD | 13,790.00 USD | 7,650.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9095` | 951.34 USD | 291,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9110` | 2,350,000.00 USD | 2,350,000.00 USD | 13,080.00 USD | 791.28 USD | 10,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9110` | 4,450,000.00 USD | 4,450,000.00 USD | 8,490.00 USD | 7,660.00 USD | 17,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9130` | 2,330,000.00 USD | 2,330,000.00 USD | 4,770.00 USD | 441.47 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9130` | 4,410,000.00 USD | 4,410,000.00 USD | 26,980.00 USD | 2,030.00 USD | 680.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9135` | 143.42 USD | 290,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9150` | 2,320,000.00 USD | 2,320,000.00 USD | 14,130.00 USD | 2,620.00 USD | 8,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9150` | 4,380,000.00 USD | 4,380,000.00 USD | 41,000.00 USD | 11,200.00 USD | 34,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9170` | 2,290,000.00 USD | 2,290,000.00 USD | 3,440.00 USD | 435.13 USD | 452.67 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9170` | 4,300,000.00 USD | 4,300,000.00 USD | 22,610.00 USD | 14,690.00 USD | 18,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9185` | 145.86 USD | 290,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9190` | 2,290,000.00 USD | 2,290,000.00 USD | 2,770.00 USD | 138.43 USD | 186.24 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9190` | 4,240,000.00 USD | 4,240,000.00 USD | 33,980.00 USD | 4,720.00 USD | 19,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9195` | 7,330.00 USD | 290,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9210` | 2,290,000.00 USD | 2,290,000.00 USD | 1,470.00 USD | 77.80 USD | 2,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9210` | 4,180,000.00 USD | 4,180,000.00 USD | 22,070.00 USD | 7,060.00 USD | 15,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9225` | 17,900.00 USD | 282,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9230` | 2,280,000.00 USD | 2,280,000.00 USD | 10,750.00 USD | 2,010.00 USD | 907.53 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9230` | 4,140,000.00 USD | 4,140,000.00 USD | 35,230.00 USD | 11,600.00 USD | 37,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9235` | 282.78 USD | 264,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9250` | 2,270,000.00 USD | 2,270,000.00 USD | 19,800.00 USD | 8,960.00 USD | 14,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9250` | 4,060,000.00 USD | 4,060,000.00 USD | 56,800.00 USD | 8,470.00 USD | 30,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9270` | 2,230,000.00 USD | 2,230,000.00 USD | 15,140.00 USD | 5,250.00 USD | 10,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9270` | 3,960,000.00 USD | 3,960,000.00 USD | 70,300.00 USD | 9,450.00 USD | 21,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9275` | 34,800.00 USD | 264,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9290` | 2,190,000.00 USD | 2,190,000.00 USD | 25,560.00 USD | 4,290.00 USD | 6,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9290` | 3,860,000.00 USD | 3,860,000.00 USD | 39,160.00 USD | 7,600.00 USD | 31,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9295` | 253.01 USD | 229,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9310` | 2,160,000.00 USD | 2,160,000.00 USD | 10,550.00 USD | 12,130.00 USD | 21,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9310` | 3,780,000.00 USD | 3,780,000.00 USD | 26,530.00 USD | 10,380.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9330` | 2,110,000.00 USD | 2,110,000.00 USD | 21,800.00 USD | 9,020.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9330` | 3,740,000.00 USD | 3,740,000.00 USD | 33,550.00 USD | 9,810.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9335` | 361.45 USD | 229,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9350` | 2,070,000.00 USD | 2,070,000.00 USD | 36,280.00 USD | 10,930.00 USD | 13,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9350` | 3,670,000.00 USD | 3,670,000.00 USD | 82,010.00 USD | 29,520.00 USD | 17,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9355` | 186.45 USD | 229,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9365` | 6,740.00 USD | 229,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9370` | 2,010,000.00 USD | 2,010,000.00 USD | 38,570.00 USD | 12,840.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9370` | 3,540,000.00 USD | 3,540,000.00 USD | 29,580.00 USD | 13,940.00 USD | 7,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9375` | 196.97 USD | 222,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9390` | 1,940,000.00 USD | 1,940,000.00 USD | 17,600.00 USD | 14,430.00 USD | 13,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9390` | 3,490,000.00 USD | 3,490,000.00 USD | 18,750.00 USD | 15,630.00 USD | 12,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9405` | 756.82 USD | 222,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9410` | 1,890,000.00 USD | 1,890,000.00 USD | 35,770.00 USD | 11,440.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9410` | 3,440,000.00 USD | 3,440,000.00 USD | 45,790.00 USD | 14,190.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9430` | 1,850,000.00 USD | 1,850,000.00 USD | 21,520.00 USD | 8,450.00 USD | 3,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9430` | 3,380,000.00 USD | 3,380,000.00 USD | 54,680.00 USD | 11,000.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9435` | 2,630.00 USD | 221,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9445` | 1,060.00 USD | 218,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9450` | 1,810,000.00 USD | 1,810,000.00 USD | 36,850.00 USD | 20,360.00 USD | 40,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9450` | 3,300,000.00 USD | 3,300,000.00 USD | 77,230.00 USD | 33,680.00 USD | 41,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9455` | 106,880.00 USD | 217,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9470` | 1,720,000.00 USD | 1,720,000.00 USD | 45,200.00 USD | 24,790.00 USD | 40,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9470` | 3,150,000.00 USD | 3,150,000.00 USD | 108,740.00 USD | 23,910.00 USD | 50,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9475` | 323.19 USD | 110,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9490` | 1,600,000.00 USD | 1,600,000.00 USD | 77,380.00 USD | 17,790.00 USD | 28,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9490` | 2,960,000.00 USD | 2,960,000.00 USD | 129,370.00 USD | 34,510.00 USD | 121,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9495` | 105,430.00 USD | 110,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9510` | 1,480,000.00 USD | 1,480,000.00 USD | 35,280.00 USD | 32,810.00 USD | 43,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9510` | 2,680,000.00 USD | 2,680,000.00 USD | 208,950.00 USD | 43,880.00 USD | 81,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9515` | 405.62 USD | 5,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9530` | 1,370,000.00 USD | 1,370,000.00 USD | 55,340.00 USD | 18,390.00 USD | 21,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9530` | 2,350,000.00 USD | 2,350,000.00 USD | 79,700.00 USD | 28,300.00 USD | 123,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9550` | 1,270,000.00 USD | 1,270,000.00 USD | 81,780.00 USD | 37,060.00 USD | 37,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9550` | 2,110,000.00 USD | 2,110,000.00 USD | 172,820.00 USD | 90,270.00 USD | 56,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9555` | 3,160.00 USD | 4,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9570` | 1,120,000.00 USD | 1,120,000.00 USD | 122,040.00 USD | 43,130.00 USD | 68,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9570` | 1,790,000.00 USD | 1,790,000.00 USD | 129,820.00 USD | 46,750.00 USD | 128,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9585` | 1,530.00 USD | 1,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9590` | 884,370.00 USD | 884,370.00 USD | 49,590.00 USD | 20,710.00 USD | 31,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9590` | 1,490,000.00 USD | 1,490,000.00 USD | 176,280.00 USD | 57,050.00 USD | 72,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9610` | 782,810.00 USD | 782,810.00 USD | 53,350.00 USD | 22,130.00 USD | 12,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9610` | 1,180,000.00 USD | 1,180,000.00 USD | 183,020.00 USD | 77,730.00 USD | 32,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9630` | 695,300.00 USD | 695,300.00 USD | 33,580.00 USD | 19,430.00 USD | 22,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9630` | 889,220.00 USD | 889,220.00 USD | 95,260.00 USD | 0.00 USD | 22,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9650` | 620,140.00 USD | 620,140.00 USD | 25,320.00 USD | 13,180.00 USD | 31,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9650` | 771,050.00 USD | 771,050.00 USD | 65,160.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9670` | 550,370.00 USD | 550,370.00 USD | 28,790.00 USD | 14,700.00 USD | 35,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9670` | 696,760.00 USD | 696,760.00 USD | 31,440.00 USD | 12,340.00 USD | 45,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9690` | 471,090.00 USD | 471,090.00 USD | 43,730.00 USD | 28,330.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9690` | 607,060.00 USD | 607,060.00 USD | 3,040.00 USD | 10,300.00 USD | 53,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9710` | 367,800.00 USD | 367,800.00 USD | 60,380.00 USD | 17,310.00 USD | 21,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9710` | 540,300.00 USD | 540,300.00 USD | 84,760.00 USD | 13,910.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9730` | 268,810.00 USD | 268,810.00 USD | 23,620.00 USD | 691.66 USD | 13,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9730` | 431,830.00 USD | 431,830.00 USD | 0.00 USD | 0.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9750` | 230,830.00 USD | 230,830.00 USD | 16,060.00 USD | 23,220.00 USD | 15,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9750` | 424,320.00 USD | 424,320.00 USD | 0.00 USD | 16,590.00 USD | 3,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9770` | 175,590.00 USD | 175,590.00 USD | 35,620.00 USD | 2,870.00 USD | 10,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9770` | 404,450.00 USD | 404,450.00 USD | 15,320.00 USD | 5,480.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9790` | 126,210.00 USD | 126,210.00 USD | 9,790.00 USD | 4,480.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9790` | 352,240.00 USD | 352,240.00 USD | 0.00 USD | 15,440.00 USD | 89,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9810` | 103,770.00 USD | 103,770.00 USD | 4,500.00 USD | 376.40 USD | 9,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9810` | 247,280.00 USD | 247,280.00 USD | 7,900.00 USD | 0.00 USD | 133,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9830` | 89,860.00 USD | 89,860.00 USD | 20,680.00 USD | 13,960.00 USD | 15,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9830` | 106,000.00 USD | 106,000.00 USD | 2,190.00 USD | 0.00 USD | 21,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9850` | 39,960.00 USD | 39,960.00 USD | 575.70 USD | 0.00 USD | 10,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9850` | 82,800.00 USD | 82,800.00 USD | 0.00 USD | 17,440.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9870` | 28,650.00 USD | 28,650.00 USD | 13,720.00 USD | 8,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9870` | 42,540.00 USD | 42,540.00 USD | 40,020.00 USD | 0.00 USD | 803.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9890` | 6,840.00 USD | 6,840.00 USD | 0.00 USD | 0.00 USD | 6,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9890` | 1,720.00 USD | 1,720.00 USD | 0.00 USD | 284.26 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9910` | 70,200.00 USD | 70,200.00 USD | 50,430.00 USD | 0.00 USD | 19,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9910` | 19,590.00 USD | 19,590.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9930` | 90,960.00 USD | 90,960.00 USD | 6,920.00 USD | 13,250.00 USD | 601.92 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9930` | 20,810.00 USD | 20,810.00 USD | 0.00 USD | 0.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9950` | 92,600.00 USD | 92,600.00 USD | 0.00 USD | 1,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9950` | 80,090.00 USD | 80,090.00 USD | 16,510.00 USD | 0.00 USD | 42,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9970` | 121,460.00 USD | 121,460.00 USD | 26,250.00 USD | 1,000.00 USD | 1,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 152,710.00 USD | 152,710.00 USD | 68,870.00 USD | 0.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9990` | 124,620.00 USD | 124,620.00 USD | 0.00 USD | 1,760.00 USD | 1,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 178,770.00 USD | 178,770.00 USD | 31,780.00 USD | 22,180.00 USD | 192.37 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 205,560.00 USD | 205,560.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 259,040.00 USD | 259,040.00 USD | 53,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 211,530.00 USD | 211,530.00 USD | 0.00 USD | 0.00 USD | 32,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 226,200.00 USD | 226,200.00 USD | 5,860.00 USD | 8,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 274,540.00 USD | 274,540.00 USD | 0.00 USD | 0.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 254,920.00 USD | 254,920.00 USD | 7,210.00 USD | 21,350.00 USD | 155.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 308,640.00 USD | 308,640.00 USD | 20,090.00 USD | 14,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 269,330.00 USD | 269,330.00 USD | 10,040.00 USD | 4,020.00 USD | 352.75 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 359,820.00 USD | 359,820.00 USD | 16,020.00 USD | 34,770.00 USD | 388.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 339,720.00 USD | 339,720.00 USD | 25,750.00 USD | 4,350.00 USD | 40,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 393,260.00 USD | 393,260.00 USD | 0.00 USD | 26,360.00 USD | 7,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 372,480.00 USD | 372,480.00 USD | 1,130.00 USD | 7,410.00 USD | 24,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 441,210.00 USD | 441,210.00 USD | 0.00 USD | 21,770.00 USD | 26,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 413,060.00 USD | 413,060.00 USD | 29,890.00 USD | 0.00 USD | 10,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 528,880.00 USD | 528,880.00 USD | 0.00 USD | 75,860.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 457,560.00 USD | 457,560.00 USD | 27,370.00 USD | 2,230.00 USD | 14,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 666,970.00 USD | 666,970.00 USD | 44,170.00 USD | 26,480.00 USD | 67,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 548,670.00 USD | 548,670.00 USD | 49,000.00 USD | 2,990.00 USD | 39,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 954,500.00 USD | 954,500.00 USD | 56,570.00 USD | 85,290.00 USD | 145,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 643,470.00 USD | 643,470.00 USD | 29,910.00 USD | 28,580.00 USD | 36,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 1,040,000.00 USD | 1,040,000.00 USD | 11,270.00 USD | 48,490.00 USD | 29,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 691,940.00 USD | 691,940.00 USD | 26,670.00 USD | 10,240.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,360,000.00 USD | 1,360,000.00 USD | 160,800.00 USD | 126,720.00 USD | 24,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 780,750.00 USD | 780,750.00 USD | 29,890.00 USD | 23,690.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,570,000.00 USD | 1,570,000.00 USD | 141,540.00 USD | 39,160.00 USD | 30,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 971,370.00 USD | 971,370.00 USD | 133,530.00 USD | 16,610.00 USD | 40,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,770,000.00 USD | 1,770,000.00 USD | 170,960.00 USD | 7,320.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,050,000.00 USD | 1,050,000.00 USD | 58,000.00 USD | 104.84 USD | 24,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,890,000.00 USD | 1,890,000.00 USD | 122,520.00 USD | 0.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,150,000.00 USD | 1,150,000.00 USD | 26,980.00 USD | 26,510.00 USD | 37,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,200,000.00 USD | 2,200,000.00 USD | 259,060.00 USD | 8,500.00 USD | 43,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,300,000.00 USD | 1,300,000.00 USD | 78,650.00 USD | 11,980.00 USD | 67,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 2,510,000.00 USD | 2,510,000.00 USD | 192,080.00 USD | 4,140.00 USD | 109,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,330,000.00 USD | 1,330,000.00 USD | 10,510.00 USD | 4,170.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 2,870,000.00 USD | 2,870,000.00 USD | 239,200.00 USD | 8,210.00 USD | 117,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,350,000.00 USD | 1,350,000.00 USD | 4,050.00 USD | 4,370.00 USD | 6,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,310,000.00 USD | 3,310,000.00 USD | 276,890.00 USD | 1,800.00 USD | 159,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,400,000.00 USD | 1,400,000.00 USD | 14,730.00 USD | 12,900.00 USD | 28,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,510,000.00 USD | 3,510,000.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,430,000.00 USD | 1,430,000.00 USD | 5,920.00 USD | 11,350.00 USD | 13,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,780,000.00 USD | 3,780,000.00 USD | 184,670.00 USD | 23,440.00 USD | 59,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,470,000.00 USD | 1,470,000.00 USD | 29,640.00 USD | 7,470.00 USD | 1,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,290,000.00 USD | 4,290,000.00 USD | 178,360.00 USD | 96,750.00 USD | 238,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 733.98 USD | 733.98 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,500,000.00 USD | 1,500,000.00 USD | 2,200.00 USD | 8,000.00 USD | 17,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,500,000.00 USD | 4,500,000.00 USD | 116,670.00 USD | 13,190.00 USD | 77,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,590,000.00 USD | 1,590,000.00 USD | 62,490.00 USD | 4,130.00 USD | 22,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,800,000.00 USD | 4,800,000.00 USD | 175,210.00 USD | 43,000.00 USD | 87,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,640,000.00 USD | 1,640,000.00 USD | 15,480.00 USD | 6,220.00 USD | 27,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,990,000.00 USD | 4,990,000.00 USD | 61,670.00 USD | 56,570.00 USD | 74,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,680,000.00 USD | 1,680,000.00 USD | 14,400.00 USD | 979.80 USD | 27,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 5,220,000.00 USD | 5,220,000.00 USD | 125,020.00 USD | 33,480.00 USD | 72,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.06` | 74,410.00 USD | 75,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,710,000.00 USD | 1,710,000.00 USD | 5,730.00 USD | 6,510.00 USD | 20,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 5,620,000.00 USD | 5,620,000.00 USD | 218,860.00 USD | 71,040.00 USD | 106,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,760,000.00 USD | 1,760,000.00 USD | 27,860.00 USD | 3,010.00 USD | 13,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,060,000.00 USD | 6,060,000.00 USD | 232,260.00 USD | 71,280.00 USD | 139,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,780,000.00 USD | 1,780,000.00 USD | 1,670.00 USD | 8,320.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,330,000.00 USD | 6,330,000.00 USD | 130,860.00 USD | 57,130.00 USD | 78,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,790,000.00 USD | 1,790,000.00 USD | 4,830.00 USD | 3,040.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,620,000.00 USD | 6,620,000.00 USD | 141,700.00 USD | 72,770.00 USD | 71,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,810,000.00 USD | 1,810,000.00 USD | 7,310.00 USD | 3,890.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,820,000.00 USD | 6,820,000.00 USD | 90,400.00 USD | 28,820.00 USD | 83,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,830,000.00 USD | 1,830,000.00 USD | 13,480.00 USD | 4,670.00 USD | 6,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,030,000.00 USD | 7,030,000.00 USD | 86,760.00 USD | 43,510.00 USD | 82,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,850,000.00 USD | 1,850,000.00 USD | 6,330.00 USD | 4,160.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,330,000.00 USD | 7,330,000.00 USD | 219,670.00 USD | 15,540.00 USD | 62,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,870,000.00 USD | 1,870,000.00 USD | 16,300.00 USD | 3,230.00 USD | 4,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,560,000.00 USD | 7,560,000.00 USD | 141,570.00 USD | 35,440.00 USD | 52,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,900,000.00 USD | 1,900,000.00 USD | 5,820.00 USD | 4,330.00 USD | 12,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,790,000.00 USD | 7,790,000.00 USD | 96,630.00 USD | 43,620.00 USD | 95,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,920,000.00 USD | 1,920,000.00 USD | 4,510.00 USD | 5,370.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,980,000.00 USD | 7,980,000.00 USD | 97,650.00 USD | 27,650.00 USD | 60,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 1,930,000.00 USD | 1,930,000.00 USD | 8,480.00 USD | 3,520.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,130,000.00 USD | 8,130,000.00 USD | 75,040.00 USD | 29,680.00 USD | 48,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 1,950,000.00 USD | 1,950,000.00 USD | 7,600.00 USD | 3,640.00 USD | 36.19 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,370,000.00 USD | 8,370,000.00 USD | 166,380.00 USD | 21,770.00 USD | 52,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 1,960,000.00 USD | 1,960,000.00 USD | 8,690.00 USD | 1,510.00 USD | 2,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,600,000.00 USD | 8,600,000.00 USD | 164,440.00 USD | 23,420.00 USD | 33,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 1,970,000.00 USD | 1,970,000.00 USD | 2,390.00 USD | 3,030.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,800,000.00 USD | 8,800,000.00 USD | 61,330.00 USD | 40,620.00 USD | 100,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 1,980,000.00 USD | 1,980,000.00 USD | 5,310.00 USD | 3,010.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,940,000.00 USD | 8,940,000.00 USD | 79,580.00 USD | 18,560.00 USD | 46,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,000,000.00 USD | 2,000,000.00 USD | 4,380.00 USD | 3,600.00 USD | 6,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,170,000.00 USD | 9,170,000.00 USD | 102,510.00 USD | 58,250.00 USD | 69,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,000,000.00 USD | 2,000,000.00 USD | 2,400.00 USD | 1,680.00 USD | 2,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,350,000.00 USD | 9,350,000.00 USD | 71,650.00 USD | 23,730.00 USD | 85,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,010,000.00 USD | 2,010,000.00 USD | 7,620.00 USD | 2,540.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,480,000.00 USD | 9,480,000.00 USD | 70,660.00 USD | 25,600.00 USD | 32,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,020,000.00 USD | 2,020,000.00 USD | 149.14 USD | 2,650.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,670,000.00 USD | 9,670,000.00 USD | 81,350.00 USD | 40,310.00 USD | 68,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,020,000.00 USD | 2,020,000.00 USD | 2,430.00 USD | 3,110.00 USD | 73.78 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,840,000.00 USD | 9,840,000.00 USD | 56,240.00 USD | 23,050.00 USD | 92,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 2,040,000.00 USD | 2,040,000.00 USD | 3,620.00 USD | 1,840.00 USD | 9,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,000,000.00 USD | 10,000,000.00 USD | 88,860.00 USD | 25,120.00 USD | 43,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 2,040,000.00 USD | 2,040,000.00 USD | 2,310.00 USD | 775.48 USD | 1,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,330,000.00 USD | 10,330,000.00 USD | 188,000.00 USD | 49,270.00 USD | 89,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 2,050,000.00 USD | 2,050,000.00 USD | 132.59 USD | 23.47 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,520,000.00 USD | 10,520,000.00 USD | 122,300.00 USD | 43,950.00 USD | 26,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 2,060,000.00 USD | 2,060,000.00 USD | 5,060.00 USD | 3,840.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,740,000.00 USD | 10,740,000.00 USD | 91,720.00 USD | 19,120.00 USD | 110,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 2,060,000.00 USD | 2,060,000.00 USD | 37.25 USD | 2,030.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,820,000.00 USD | 10,820,000.00 USD | 36,570.00 USD | 10,260.00 USD | 31,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.11` | 2,070,000.00 USD | 2,070,000.00 USD | 4,080.00 USD | 1,690.00 USD | 111.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 10,930,000.00 USD | 10,930,000.00 USD | 51,840.00 USD | 24,560.00 USD | 34,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.11` | 2,070,000.00 USD | 2,070,000.00 USD | 1,670.00 USD | 87.40 USD | 803.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 11,120,000.00 USD | 11,120,000.00 USD | 80,930.00 USD | 42,090.00 USD | 63,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.11` | 169.86 USD | 75,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.11` | 2,090,000.00 USD | 2,090,000.00 USD | 12,800.00 USD | 3,460.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 11,270,000.00 USD | 11,270,000.00 USD | 69,040.00 USD | 16,250.00 USD | 64,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.11` | 2,120,000.00 USD | 2,120,000.00 USD | 11,280.00 USD | 260.69 USD | 10,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 11,360,000.00 USD | 11,360,000.00 USD | 20,190.00 USD | 43,670.00 USD | 25,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.11` | 2,120,000.00 USD | 2,120,000.00 USD | 3,720.00 USD | 294.76 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 11,420,000.00 USD | 11,420,000.00 USD | 34,700.00 USD | 14,480.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.12` | 2,130,000.00 USD | 2,130,000.00 USD | 56.85 USD | 1,860.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 11,560,000.00 USD | 11,560,000.00 USD | 68,170.00 USD | 45,850.00 USD | 32,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.12` | 2,150,000.00 USD | 2,150,000.00 USD | 10,810.00 USD | 658.54 USD | 4,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 11,630,000.00 USD | 11,630,000.00 USD | 24,700.00 USD | 23,340.00 USD | 13,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.12` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 382.75 USD | 452.67 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 11,730,000.00 USD | 11,730,000.00 USD | 48,980.00 USD | 31,670.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.12` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 12.35 USD | 186.24 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 11,820,000.00 USD | 11,820,000.00 USD | 61,780.00 USD | 4,660.00 USD | 25,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.12` | 2,150,000.00 USD | 2,150,000.00 USD | 199.10 USD | 0.00 USD | 2,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 11,880,000.00 USD | 11,880,000.00 USD | 18,300.00 USD | 10,300.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.13` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 1,020.00 USD | 870.54 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 11,900,000.00 USD | 11,900,000.00 USD | 14,700.00 USD | 1,030.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 12,030,000.00 USD | 12,030,000.00 USD | 56,500.00 USD | 19,040.00 USD | 45,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 12,220,000.00 USD | 12,220,000.00 USD | 96,260.00 USD | 12,540.00 USD | 90,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 12,260,000.00 USD | 12,260,000.00 USD | 16,560.00 USD | 0.00 USD | 22,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.14` | 114.25 USD | 75,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.18` | 228.59 USD | 75,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 22,180.00 USD | 97,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 11,730.00 USD | 109,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 389.93 USD | 109,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.42` | 4,330.00 USD | 114,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 513,610.00 USD | 627,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 232.49 USD | 628,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 176.31 USD | 628,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 9,590.00 USD | 637,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 761.19 USD | 638,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 243.37 USD | 638,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 300.15 USD | 639,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 320.76 USD | 639,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 88,000.00 USD | 727,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 208.37 USD | 727,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 181.88 USD | 727,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 2,950.00 USD | 730,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2465` | 565,790.00 USD | 0.00 USD | 123.25 USD | `-75.15%` | `500.00` |
| `Live` | `Long` | `0.3085` | 565,670.00 USD | 0.00 USD | 557.06 USD | `-68.90%` | `1,805.70` |
| `Live` | `Long` | `0.3345` | 565,110.00 USD | 0.00 USD | 738.91 USD | `-66.28%` | `2,209.00` |
| `Live` | `Long` | `0.3605` | 564,370.00 USD | 0.00 USD | 2,050.00 USD | `-63.66%` | `5,698.80` |
| `Live` | `Long` | `0.3825` | 562,320.00 USD | 0.00 USD | 122.13 USD | `-61.44%` | `319.30` |
| `Live` | `Long` | `0.4185` | 562,200.00 USD | 0.00 USD | 2,790.00 USD | `-57.81%` | `6,675.20` |
| `Live` | `Long` | `0.4425` | 559,400.00 USD | 0.00 USD | 175.45 USD | `-55.40%` | `396.50` |
| `Live` | `Long` | `0.4695` | 559,230.00 USD | 0.00 USD | 2,580.00 USD | `-52.67%` | `5,500.00` |
| `Live` | `Long` | `0.4785` | 556,650.00 USD | 0.00 USD | 947.38 USD | `-51.77%` | `1,979.90` |
| `Live` | `Long` | `0.4885` | 555,700.00 USD | 0.00 USD | 11,910.00 USD | `-50.76%` | `24,390.20` |
| `Live` | `Long` | `0.4965` | 543,780.00 USD | 0.00 USD | 198.95 USD | `-49.95%` | `400.70` |
| `Live` | `Long` | `0.5115` | 543,580.00 USD | 0.00 USD | 606.38 USD | `-48.44%` | `1,185.50` |
| `Live` | `Long` | `0.5125` | 542,980.00 USD | 0.00 USD | 4,130.00 USD | `-48.34%` | `8,067.10` |
| `Live` | `Long` | `0.5465` | 538,840.00 USD | 0.00 USD | 106.84 USD | `-44.91%` | `195.50` |
| `Live` | `Long` | `0.5695` | 538,740.00 USD | 0.00 USD | 577.36 USD | `-42.59%` | `1,013.80` |
| `Live` | `Long` | `0.5895` | 538,160.00 USD | 0.00 USD | 137.53 USD | `-40.58%` | `233.30` |
| `Live` | `Long` | `0.5955` | 538,020.00 USD | 0.00 USD | 3,390.00 USD | `-39.97%` | `5,695.60` |
| `Live` | `Long` | `0.6055` | 534,630.00 USD | 0.00 USD | 1,480.00 USD | `-38.96%` | `2,448.50` |
| `Live` | `Long` | `0.6065` | 533,150.00 USD | 0.00 USD | 1,800.00 USD | `-38.86%` | `2,971.80` |
| `Live` | `Long` | `0.6115` | 531,350.00 USD | 0.00 USD | 149.57 USD | `-38.36%` | `244.60` |
| `Live` | `Long` | `0.6125` | 531,200.00 USD | 0.00 USD | 105.96 USD | `-38.26%` | `173.00` |
| `Live` | `Long` | `0.6145` | 531,090.00 USD | 0.00 USD | 147.48 USD | `-38.06%` | `240.00` |
| `Live` | `Long` | `0.6245` | 530,940.00 USD | 0.00 USD | 525.77 USD | `-37.05%` | `841.90` |
| `Live` | `Long` | `0.6315` | 530,420.00 USD | 0.00 USD | 757.80 USD | `-36.34%` | `1,200.00` |
| `Live` | `Long` | `0.6355` | 529,660.00 USD | 0.00 USD | 106.00 USD | `-35.94%` | `166.80` |
| `Live` | `Long` | `0.6415` | 529,550.00 USD | 0.00 USD | 20,270.00 USD | `-35.34%` | `31,595.60` |
| `Live` | `Long` | `0.6465` | 509,280.00 USD | 0.00 USD | 4,230.00 USD | `-34.83%` | `6,539.70` |
| `Live` | `Long` | `0.6475` | 505,060.00 USD | 0.00 USD | 202.47 USD | `-34.73%` | `312.70` |
| `Live` | `Long` | `0.6595` | 504,850.00 USD | 0.00 USD | 149.44 USD | `-33.52%` | `226.60` |
| `Live` | `Long` | `0.6725` | 504,700.00 USD | 0.00 USD | 63,890.00 USD | `-32.21%` | `95,000.00` |
| `Live` | `Long` | `0.6775` | 440,820.00 USD | 0.00 USD | 423.10 USD | `-31.71%` | `624.50` |
| `Live` | `Long` | `0.6825` | 440,390.00 USD | 0.00 USD | 264.67 USD | `-31.20%` | `387.80` |
| `Live` | `Long` | `0.6835` | 440,130.00 USD | 0.00 USD | 247.91 USD | `-31.10%` | `362.70` |
| `Live` | `Long` | `0.6855` | 439,880.00 USD | 0.00 USD | 2,110.00 USD | `-30.90%` | `3,075.70` |
| `Live` | `Long` | `0.6955` | 437,770.00 USD | 0.00 USD | 322.16 USD | `-29.89%` | `463.20` |
| `Live` | `Long` | `0.6975` | 437,450.00 USD | 0.00 USD | 697.50 USD | `-29.69%` | `1,000.00` |
| `Live` | `Long` | `0.6995` | 436,750.00 USD | 0.00 USD | 156.27 USD | `-29.49%` | `223.40` |
| `Live` | `Long` | `0.7055` | 436,600.00 USD | 0.00 USD | 176.38 USD | `-28.88%` | `250.00` |
| `Live` | `Long` | `0.7075` | 436,420.00 USD | 0.00 USD | 16,520.00 USD | `-28.68%` | `23,344.30` |
| `Live` | `Long` | `0.7145` | 419,900.00 USD | 0.00 USD | 988.87 USD | `-27.98%` | `1,384.00` |
| `Live` | `Long` | `0.7175` | 418,920.00 USD | 0.00 USD | 322.88 USD | `-27.68%` | `450.00` |
| `Live` | `Long` | `0.7205` | 418,590.00 USD | 0.00 USD | 866.26 USD | `-27.37%` | `1,202.30` |
| `Live` | `Long` | `0.7255` | 417,730.00 USD | 0.00 USD | 1,090.00 USD | `-26.87%` | `1,500.00` |
| `Live` | `Long` | `0.7275` | 416,640.00 USD | 0.00 USD | 126.44 USD | `-26.67%` | `173.80` |
| `Live` | `Long` | `0.7285` | 416,510.00 USD | 0.00 USD | 291.18 USD | `-26.57%` | `399.70` |
| `Live` | `Long` | `0.7305` | 416,220.00 USD | 0.00 USD | 2,300.00 USD | `-26.36%` | `3,143.00` |
| `Live` | `Long` | `0.7335` | 413,920.00 USD | 0.00 USD | 1,140.00 USD | `-26.06%` | `1,557.80` |
| `Live` | `Long` | `0.7395` | 412,780.00 USD | 0.00 USD | 283.30 USD | `-25.46%` | `383.10` |
| `Live` | `Long` | `0.7415` | 412,500.00 USD | 0.00 USD | 1,380.00 USD | `-25.26%` | `1,859.90` |
| `Live` | `Long` | `0.7525` | 411,120.00 USD | 0.00 USD | 331.18 USD | `-24.15%` | `440.10` |
| `Live` | `Long` | `0.7555` | 410,790.00 USD | 0.00 USD | 2,390.00 USD | `-23.84%` | `3,161.00` |
| `Live` | `Long` | `0.7605` | 408,400.00 USD | 0.00 USD | 834.88 USD | `-23.34%` | `1,097.80` |
| `Live` | `Long` | `0.7725` | 407,570.00 USD | 0.00 USD | 1,580.00 USD | `-22.13%` | `2,046.10` |
| `Live` | `Long` | `0.7865` | 405,980.00 USD | 0.00 USD | 292.03 USD | `-20.72%` | `371.30` |
| `Live` | `Long` | `0.7895` | 405,690.00 USD | 0.00 USD | 20,380.00 USD | `-20.42%` | `25,816.60` |
| `Live` | `Long` | `0.7925` | 385,310.00 USD | 0.00 USD | 157.95 USD | `-20.11%` | `199.30` |
| `Live` | `Long` | `0.7965` | 385,150.00 USD | 0.00 USD | 3,360.00 USD | `-19.71%` | `4,216.70` |
| `Live` | `Long` | `0.8025` | 381,790.00 USD | 0.00 USD | 238.90 USD | `-19.11%` | `297.70` |
| `Live` | `Long` | `0.8045` | 381,560.00 USD | 0.00 USD | 566.61 USD | `-18.91%` | `704.30` |
| `Live` | `Long` | `0.8055` | 380,990.00 USD | 0.00 USD | 699.01 USD | `-18.80%` | `867.80` |
| `Live` | `Long` | `0.8125` | 380,290.00 USD | 0.00 USD | 13,440.00 USD | `-18.10%` | `16,544.60` |
| `Live` | `Long` | `0.8135` | 366,850.00 USD | 0.00 USD | 647.79 USD | `-18.00%` | `796.30` |
| `Live` | `Long` | `0.8215` | 366,200.00 USD | 0.00 USD | 1,950.00 USD | `-17.19%` | `2,370.70` |
| `Live` | `Long` | `0.8285` | 364,250.00 USD | 0.00 USD | 1,890.00 USD | `-16.49%` | `2,283.30` |
| `Live` | `Long` | `0.8325` | 362,360.00 USD | 0.00 USD | 8,990.00 USD | `-16.08%` | `10,795.60` |
| `Live` | `Long` | `0.8365` | 353,370.00 USD | 0.00 USD | 316.70 USD | `-15.68%` | `378.60` |
| `Live` | `Long` | `0.8375` | 353,060.00 USD | 0.00 USD | 167.00 USD | `-15.58%` | `199.40` |
| `Live` | `Long` | `0.8415` | 352,890.00 USD | 0.00 USD | 1,240.00 USD | `-15.18%` | `1,469.60` |
| `Live` | `Long` | `0.8445` | 351,650.00 USD | 0.00 USD | 168.31 USD | `-14.87%` | `199.30` |
| `Live` | `Long` | `0.8495` | 351,480.00 USD | 0.00 USD | 1,260.00 USD | `-14.37%` | `1,486.90` |
| `Live` | `Long` | `0.8565` | 350,220.00 USD | 0.00 USD | 170.70 USD | `-13.66%` | `199.30` |
| `Live` | `Long` | `0.8575` | 350,050.00 USD | 0.00 USD | 620.32 USD | `-13.56%` | `723.40` |
| `Live` | `Long` | `0.8595` | 349,430.00 USD | 0.00 USD | 171.38 USD | `-13.36%` | `199.40` |
| `Live` | `Long` | `0.8625` | 349,260.00 USD | 0.00 USD | 309.55 USD | `-13.06%` | `358.90` |
| `Live` | `Long` | `0.8635` | 348,950.00 USD | 0.00 USD | 208.02 USD | `-12.96%` | `240.90` |
| `Live` | `Long` | `0.8645` | 348,740.00 USD | 0.00 USD | 438.30 USD | `-12.86%` | `507.00` |
| `Live` | `Long` | `0.8665` | 348,300.00 USD | 0.00 USD | 118.54 USD | `-12.66%` | `136.80` |
| `Live` | `Long` | `0.8765` | 348,180.00 USD | 0.00 USD | 171.88 USD | `-11.65%` | `196.10` |
| `Live` | `Long` | `0.8795` | 348,010.00 USD | 0.00 USD | 948.01 USD | `-11.35%` | `1,077.90` |
| `Live` | `Long` | `0.8915` | 347,060.00 USD | 0.00 USD | 41,900.00 USD | `-10.14%` | `47,002.60` |
| `Live` | `Long` | `0.8925` | 305,160.00 USD | 0.00 USD | 526.84 USD | `-10.03%` | `590.30` |
| `Live` | `Long` | `0.8935` | 304,630.00 USD | 0.00 USD | 9,170.00 USD | `-9.93%` | `10,267.00` |
| `Live` | `Long` | `0.8995` | 295,460.00 USD | 0.00 USD | 3,820.00 USD | `-9.33%` | `4,250.30` |
| `Live` | `Long` | `0.9035` | 291,640.00 USD | 0.00 USD | 180.16 USD | `-8.93%` | `199.40` |
| `Live` | `Long` | `0.9095` | 291,460.00 USD | 0.00 USD | 951.34 USD | `-8.32%` | `1,046.00` |
| `Live` | `Long` | `0.9135` | 290,510.00 USD | 0.00 USD | 143.42 USD | `-7.92%` | `157.00` |
| `Live` | `Long` | `0.9185` | 290,360.00 USD | 0.00 USD | 145.86 USD | `-7.41%` | `158.80` |
| `Live` | `Long` | `0.9195` | 290,220.00 USD | 0.00 USD | 7,330.00 USD | `-7.31%` | `7,970.50` |
| `Live` | `Long` | `0.9225` | 282,890.00 USD | 0.00 USD | 17,900.00 USD | `-7.01%` | `19,401.30` |
| `Live` | `Long` | `0.9235` | 264,990.00 USD | 0.00 USD | 282.78 USD | `-6.91%` | `306.20` |
| `Live` | `Long` | `0.9275` | 264,710.00 USD | 0.00 USD | 34,800.00 USD | `-6.51%` | `37,519.20` |
| `Live` | `Long` | `0.9295` | 229,910.00 USD | 0.00 USD | 253.01 USD | `-6.31%` | `272.20` |
| `Live` | `Long` | `0.9335` | 229,660.00 USD | 0.00 USD | 361.45 USD | `-5.90%` | `387.20` |
| `Live` | `Long` | `0.9355` | 229,290.00 USD | 0.00 USD | 186.45 USD | `-5.70%` | `199.30` |
| `Live` | `Long` | `0.9365` | 229,110.00 USD | 0.00 USD | 6,740.00 USD | `-5.60%` | `7,199.60` |
| `Live` | `Long` | `0.9375` | 222,370.00 USD | 0.00 USD | 196.97 USD | `-5.50%` | `210.10` |
| `Live` | `Long` | `0.9405` | 222,170.00 USD | 0.00 USD | 756.82 USD | `-5.20%` | `804.70` |
| `Live` | `Long` | `0.9435` | 221,410.00 USD | 0.00 USD | 2,630.00 USD | `-4.89%` | `2,785.30` |
| `Live` | `Long` | `0.9445` | 218,780.00 USD | 0.00 USD | 1,060.00 USD | `-4.79%` | `1,117.80` |
| `Live` | `Long` | `0.9455` | 217,730.00 USD | 0.00 USD | 106,880.00 USD | `-4.69%` | `113,040.20` |
| `Live` | `Long` | `0.9475` | 110,850.00 USD | 0.00 USD | 323.19 USD | `-4.49%` | `341.10` |
| `Live` | `Long` | `0.9495` | 110,530.00 USD | 0.00 USD | 105,430.00 USD | `-4.29%` | `111,034.60` |
| `Live` | `Long` | `0.9515` | 5,100.00 USD | 0.00 USD | 405.62 USD | `-4.09%` | `426.30` |
| `Live` | `Long` | `0.9555` | 4,690.00 USD | 0.00 USD | 3,160.00 USD | `-3.68%` | `3,305.70` |
| `Live` | `Long` | `0.9585` | 1,530.00 USD | 0.00 USD | 1,530.00 USD | `-3.38%` | `1,600.00` |
| `Live` | `Short` | `1.05` | 733.98 USD | 733.98 USD | 0.00 USD | `+5.59%` | `700.70` |
| `Live` | `Short` | `1.06` | 75,150.00 USD | 74,410.00 USD | 0.00 USD | `+6.40%` | `70,500.00` |
| `Live` | `Short` | `1.11` | 75,320.00 USD | 169.86 USD | 0.00 USD | `+11.84%` | `153.10` |
| `Live` | `Short` | `1.14` | 75,430.00 USD | 114.25 USD | 0.00 USD | `+15.17%` | `100.00` |
| `Live` | `Short` | `1.18` | 75,660.00 USD | 228.59 USD | 0.00 USD | `+18.59%` | `194.30` |
| `Live` | `Short` | `1.19` | 97,840.00 USD | 22,180.00 USD | 0.00 USD | `+19.80%` | `18,664.00` |
| `Live` | `Short` | `1.32` | 109,570.00 USD | 11,730.00 USD | 0.00 USD | `+33.41%` | `8,862.90` |
| `Live` | `Short` | `1.34` | 109,960.00 USD | 389.93 USD | 0.00 USD | `+35.02%` | `291.10` |
| `Live` | `Short` | `1.42` | 114,290.00 USD | 4,330.00 USD | 0.00 USD | `+43.09%` | `3,049.30` |
| `Live` | `Short` | `1.49` | 627,900.00 USD | 513,610.00 USD | 0.00 USD | `+50.04%` | `345,051.20` |
| `Live` | `Short` | `1.52` | 628,130.00 USD | 232.49 USD | 0.00 USD | `+53.67%` | `152.50` |
| `Live` | `Short` | `1.54` | 628,310.00 USD | 176.31 USD | 0.00 USD | `+55.49%` | `114.30` |
| `Live` | `Short` | `1.56` | 637,900.00 USD | 9,590.00 USD | 0.00 USD | `+56.90%` | `6,161.90` |
| `Live` | `Short` | `1.64` | 638,660.00 USD | 761.19 USD | 0.00 USD | `+65.36%` | `464.00` |
| `Live` | `Short` | `1.66` | 638,900.00 USD | 243.37 USD | 0.00 USD | `+67.68%` | `146.30` |
| `Live` | `Short` | `1.67` | 639,200.00 USD | 300.15 USD | 0.00 USD | `+68.09%` | `180.00` |
| `Live` | `Short` | `1.67` | 639,520.00 USD | 320.76 USD | 0.00 USD | `+68.49%` | `191.90` |
| `Live` | `Short` | `1.77` | 727,520.00 USD | 88,000.00 USD | 0.00 USD | `+78.27%` | `49,759.80` |
| `Live` | `Short` | `1.86` | 727,730.00 USD | 208.37 USD | 0.00 USD | `+87.04%` | `112.30` |
| `Live` | `Short` | `1.90` | 727,910.00 USD | 181.88 USD | 0.00 USD | `+91.57%` | `95.70` |
| `Live` | `Short` | `1.97` | 730,870.00 USD | 2,950.00 USD | 0.00 USD | `+98.53%` | `1,500.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.4015` | 573,270.00 USD | 0.00 USD | 120.45 USD | `-59.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 573,150.00 USD | 0.00 USD | 150.15 USD | `-49.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 573,000.00 USD | 0.00 USD | 781.90 USD | `-29.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 572,220.00 USD | 0.00 USD | 477.38 USD | `-28.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 571,740.00 USD | 0.00 USD | 341.33 USD | `-27.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 571,400.00 USD | 0.00 USD | 972.82 USD | `-27.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 570,430.00 USD | 0.00 USD | 160.20 USD | `-26.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 570,270.00 USD | 0.00 USD | 289.49 USD | `-24.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 569,980.00 USD | 0.00 USD | 14,570.00 USD | `-21.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 555,410.00 USD | 0.00 USD | 274,830.00 USD | `-19.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 280,580.00 USD | 0.00 USD | 405.75 USD | `-18.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 280,170.00 USD | 0.00 USD | 772.84 USD | `-15.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8495` | 279,400.00 USD | 0.00 USD | 3,470.00 USD | `-14.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 275,930.00 USD | 0.00 USD | 9,180.00 USD | `-14.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 266,750.00 USD | 0.00 USD | 341.94 USD | `-13.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 266,410.00 USD | 0.00 USD | 1,150.00 USD | `-13.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 265,260.00 USD | 0.00 USD | 2,020.00 USD | `-13.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 263,250.00 USD | 0.00 USD | 429.25 USD | `-13.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 262,820.00 USD | 0.00 USD | 1,290.00 USD | `-13.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 261,530.00 USD | 0.00 USD | 518.51 USD | `-12.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 261,010.00 USD | 0.00 USD | 223.04 USD | `-10.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 260,780.00 USD | 0.00 USD | 401.86 USD | `-10.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 260,380.00 USD | 0.00 USD | 158.51 USD | `-10.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 260,220.00 USD | 0.00 USD | 293.81 USD | `-10.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 259,930.00 USD | 0.00 USD | 363.40 USD | `-8.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9155` | 259,570.00 USD | 0.00 USD | 869.27 USD | `-7.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9165` | 258,700.00 USD | 0.00 USD | 274.77 USD | `-7.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 258,420.00 USD | 0.00 USD | 913.41 USD | `-7.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9255` | 257,510.00 USD | 0.00 USD | 1,010.00 USD | `-6.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9275` | 256,500.00 USD | 0.00 USD | 2,120.00 USD | `-6.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9285` | 254,380.00 USD | 0.00 USD | 246.05 USD | `-6.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9295` | 254,130.00 USD | 0.00 USD | 776.50 USD | `-6.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9365` | 253,360.00 USD | 0.00 USD | 9,680.00 USD | `-5.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9405` | 243,670.00 USD | 0.00 USD | 555.18 USD | `-5.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9425` | 243,120.00 USD | 0.00 USD | 409.14 USD | `-4.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9445` | 242,710.00 USD | 0.00 USD | 1,730.00 USD | `-4.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9485` | 240,980.00 USD | 0.00 USD | 634.74 USD | `-4.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9525` | 240,350.00 USD | 0.00 USD | 381.00 USD | `-3.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9555` | 239,970.00 USD | 0.00 USD | 3,900.00 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9565` | 236,070.00 USD | 0.00 USD | 674.91 USD | `-3.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9575` | 235,390.00 USD | 0.00 USD | 166.41 USD | `-3.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9585` | 235,230.00 USD | 0.00 USD | 192.95 USD | `-3.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9595` | 235,030.00 USD | 0.00 USD | 383.90 USD | `-3.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9605` | 234,650.00 USD | 0.00 USD | 376.80 USD | `-3.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9615` | 234,270.00 USD | 0.00 USD | 152.11 USD | `-3.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9625` | 234,120.00 USD | 0.00 USD | 1,910.00 USD | `-2.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9635` | 232,220.00 USD | 0.00 USD | 568.75 USD | `-2.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9645` | 231,650.00 USD | 0.00 USD | 163.29 USD | `-2.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9665` | 231,480.00 USD | 0.00 USD | 554.58 USD | `-2.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9675` | 230,930.00 USD | 0.00 USD | 1,800.00 USD | `-2.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9685` | 229,130.00 USD | 0.00 USD | 153.22 USD | `-2.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9695` | 228,970.00 USD | 0.00 USD | 22,800.00 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9705` | 206,170.00 USD | 0.00 USD | 11,230.00 USD | `-2.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9715` | 194,940.00 USD | 0.00 USD | 10,370.00 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9725` | 184,570.00 USD | 0.00 USD | 6,930.00 USD | `-1.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9735` | 177,640.00 USD | 0.00 USD | 7,630.00 USD | `-1.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9745` | 170,010.00 USD | 0.00 USD | 8,750.00 USD | `-1.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9755` | 161,260.00 USD | 0.00 USD | 21,960.00 USD | `-1.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9765` | 139,300.00 USD | 0.00 USD | 9,500.00 USD | `-1.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9775` | 129,800.00 USD | 0.00 USD | 1,280.00 USD | `-1.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9785` | 128,520.00 USD | 0.00 USD | 11,400.00 USD | `-1.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9795` | 117,120.00 USD | 0.00 USD | 123.61 USD | `-1.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9805` | 117,000.00 USD | 0.00 USD | 8,350.00 USD | `-1.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9835` | 108,650.00 USD | 0.00 USD | 120.48 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9845` | 108,520.00 USD | 0.00 USD | 22,170.00 USD | `-0.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9855` | 86,360.00 USD | 0.00 USD | 15,070.00 USD | `-0.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9865` | 71,290.00 USD | 0.00 USD | 32,800.00 USD | `-0.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9895` | 38,490.00 USD | 0.00 USD | 34,970.00 USD | `-0.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9915` | 3,520.00 USD | 0.00 USD | 3,520.00 USD | `-0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 31,750.00 USD | 31,750.00 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 33,070.00 USD | 1,320.00 USD | 0.00 USD | `+0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 33,860.00 USD | 782.07 USD | 0.00 USD | `+0.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 34,260.00 USD | 403.28 USD | 0.00 USD | `+0.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 37,660.00 USD | 3,400.00 USD | 0.00 USD | `+0.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 42,800.00 USD | 5,140.00 USD | 0.00 USD | `+0.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 80,110.00 USD | 37,310.00 USD | 0.00 USD | `+0.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 81,120.00 USD | 1,000.00 USD | 0.00 USD | `+0.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 121,710.00 USD | 40,590.00 USD | 0.00 USD | `+0.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 121,950.00 USD | 235.79 USD | 0.00 USD | `+1.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 123,290.00 USD | 1,340.00 USD | 0.00 USD | `+1.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 124,290.00 USD | 1,000.00 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 124,490.00 USD | 198.46 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 125,100.00 USD | 615.60 USD | 0.00 USD | `+2.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 128,560.00 USD | 3,460.00 USD | 0.00 USD | `+2.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 130,680.00 USD | 2,110.00 USD | 0.00 USD | `+2.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 131,240.00 USD | 561.17 USD | 0.00 USD | `+2.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 133,680.00 USD | 2,450.00 USD | 0.00 USD | `+2.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 134,090.00 USD | 401.26 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 134,370.00 USD | 286.22 USD | 0.00 USD | `+2.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 135,180.00 USD | 804.09 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 137,830.00 USD | 2,660.00 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 138,030.00 USD | 201.52 USD | 0.00 USD | `+3.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 138,240.00 USD | 201.92 USD | 0.00 USD | `+3.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 138,440.00 USD | 201.60 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 141,640.00 USD | 3,210.00 USD | 0.00 USD | `+3.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 141,750.00 USD | 101.51 USD | 0.00 USD | `+3.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 143,450.00 USD | 1,700.00 USD | 0.00 USD | `+3.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 143,650.00 USD | 206.92 USD | 0.00 USD | `+3.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 143,860.00 USD | 202.90 USD | 0.00 USD | `+3.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 144,090.00 USD | 234.48 USD | 0.00 USD | `+4.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 144,610.00 USD | 516.75 USD | 0.00 USD | `+4.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 144,810.00 USD | 204.93 USD | 0.00 USD | `+4.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 145,160.00 USD | 348.86 USD | 0.00 USD | `+4.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 145,360.00 USD | 203.87 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 147,030.00 USD | 1,670.00 USD | 0.00 USD | `+4.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 147,390.00 USD | 354.91 USD | 0.00 USD | `+4.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 149,290.00 USD | 1,900.00 USD | 0.00 USD | `+4.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 150,250.00 USD | 962.12 USD | 0.00 USD | `+5.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 150,460.00 USD | 205.99 USD | 0.00 USD | `+5.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 161,760.00 USD | 11,310.00 USD | 0.00 USD | `+5.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 163,060.00 USD | 1,290.00 USD | 0.00 USD | `+5.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 163,270.00 USD | 206.97 USD | 0.00 USD | `+5.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 163,370.00 USD | 107.99 USD | 0.00 USD | `+5.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 163,620.00 USD | 247.60 USD | 0.00 USD | `+6.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 163,750.00 USD | 129.79 USD | 0.00 USD | `+6.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 229,560.00 USD | 65,810.00 USD | 0.00 USD | `+7.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 230,110.00 USD | 544.88 USD | 0.00 USD | `+7.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 230,270.00 USD | 157.10 USD | 0.00 USD | `+8.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 232,440.00 USD | 2,170.00 USD | 0.00 USD | `+10.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 233,980.00 USD | 1,540.00 USD | 0.00 USD | `+10.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 243,900.00 USD | 9,930.00 USD | 0.00 USD | `+10.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 244,880.00 USD | 976.36 USD | 0.00 USD | `+10.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 246,090.00 USD | 1,210.00 USD | 0.00 USD | `+11.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 246,970.00 USD | 877.63 USD | 0.00 USD | `+11.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 247,140.00 USD | 171.50 USD | 0.00 USD | `+12.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 247,310.00 USD | 171.09 USD | 0.00 USD | `+12.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 249,350.00 USD | 2,040.00 USD | 0.00 USD | `+13.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 249,600.00 USD | 249.83 USD | 0.00 USD | `+14.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 252,270.00 USD | 2,670.00 USD | 0.00 USD | `+14.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 254,640.00 USD | 2,380.00 USD | 0.00 USD | `+15.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 254,790.00 USD | 151.16 USD | 0.00 USD | `+15.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 254,940.00 USD | 151.29 USD | 0.00 USD | `+15.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 255,100.00 USD | 151.42 USD | 0.00 USD | `+16.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 255,250.00 USD | 151.55 USD | 0.00 USD | `+16.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 255,400.00 USD | 151.69 USD | 0.00 USD | `+16.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 256,390.00 USD | 986.35 USD | 0.00 USD | `+17.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 258,430.00 USD | 2,050.00 USD | 0.00 USD | `+17.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 258,540.00 USD | 110.00 USD | 0.00 USD | `+18.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 258,780.00 USD | 237.90 USD | 0.00 USD | `+19.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 259,990.00 USD | 1,210.00 USD | 0.00 USD | `+21.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 302,920.00 USD | 42,930.00 USD | 0.00 USD | `+21.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 304,920.00 USD | 2,000.00 USD | 0.00 USD | `+24.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 305,160.00 USD | 245.41 USD | 0.00 USD | `+28.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 312,510.00 USD | 7,350.00 USD | 0.00 USD | `+30.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 312,930.00 USD | 415.25 USD | 0.00 USD | `+31.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 319,450.00 USD | 6,520.00 USD | 0.00 USD | `+31.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 776,430.00 USD | 456,990.00 USD | 0.00 USD | `+32.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 777,090.00 USD | 655.75 USD | 0.00 USD | `+32.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 778,900.00 USD | 1,810.00 USD | 0.00 USD | `+35.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 792,790.00 USD | 13,880.00 USD | 0.00 USD | `+35.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 794,040.00 USD | 1,250.00 USD | 0.00 USD | `+36.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 796,110.00 USD | 2,070.00 USD | 0.00 USD | `+40.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 796,250.00 USD | 140.05 USD | 0.00 USD | `+41.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 796,410.00 USD | 160.42 USD | 0.00 USD | `+41.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 797,010.00 USD | 598.33 USD | 0.00 USD | `+42.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 831,180.00 USD | 34,170.00 USD | 0.00 USD | `+44.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 832,060.00 USD | 879.84 USD | 0.00 USD | `+50.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 832,650.00 USD | 590.88 USD | 0.00 USD | `+51.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 835,700.00 USD | 3,050.00 USD | 0.00 USD | `+52.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 836,000.00 USD | 297.27 USD | 0.00 USD | `+56.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 844,530.00 USD | 8,530.00 USD | 0.00 USD | `+66.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 844,680.00 USD | 143.99 USD | 0.00 USD | `+68.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 844,850.00 USD | 177.05 USD | 0.00 USD | `+78.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 845,280.00 USD | 431.40 USD | 0.00 USD | `+81.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 850,390.00 USD | 5,100.00 USD | 0.00 USD | `+92.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 852,870.00 USD | 2,480.00 USD | 0.00 USD | `+92.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 858,700.00 USD | 5,830.00 USD | 0.00 USD | `+99.64%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.8730` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 4,750.00 USD | 2,080.00 USD | 295.31 USD |
| `7D` | `0.8750` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 0.00 USD | 301.30 USD | 5,750.00 USD |
| `7D` | `0.8770` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 20,650.00 USD | 5,900.00 USD | 2,760.00 USD |
| `7D` | `0.8790` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD |
| `7D` | `0.8810` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 228.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8830` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 8,430.00 USD | 6,110.00 USD | 360.61 USD |
| `1D` | `0.8850` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 10,630.00 USD | 1,790.00 USD | 2,200.00 USD |
| `7D` | `0.8850` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 8,630.00 USD | 2,860.00 USD | 698.60 USD |
| `1D` | `0.8870` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 6,560.00 USD | 3,430.00 USD | 8,790.00 USD |
| `7D` | `0.8870` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 11,700.00 USD | 5,060.00 USD | 6,640.00 USD |
| `1D` | `0.8890` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 3,730.00 USD | 3,370.00 USD | 6,640.00 USD |
| `7D` | `0.8890` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 13,840.00 USD | 5,300.00 USD | 14,660.00 USD |
| `1D` | `0.8910` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 1,820.00 USD | 1,560.00 USD | 2,270.00 USD |
| `7D` | `0.8910` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 30,330.00 USD | 10,770.00 USD | 24,650.00 USD |
| `1D` | `0.8930` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 7,320.00 USD | 2,470.00 USD | 1,890.00 USD |
| `7D` | `0.8930` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 24,780.00 USD | 5,700.00 USD | 9,960.00 USD |
| `1D` | `0.8950` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 22.75 USD | 2,530.00 USD | 2,140.00 USD |
| `7D` | `0.8950` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 7,380.00 USD | 10,990.00 USD | 27,510.00 USD |
| `1D` | `0.8970` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 5,360.00 USD | 4,910.00 USD | 9,810.00 USD |
| `7D` | `0.8970` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 43,430.00 USD | 5,260.00 USD | 31,920.00 USD |
| `1D` | `0.8990` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 5,550.00 USD | 757.19 USD | 1,240.00 USD |
| `7D` | `0.8990` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 52,250.00 USD | 14,420.00 USD | 20,000.00 USD |
| `1D` | `0.9010` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 15.65 USD | 39.59 USD | 1,890.00 USD |
| `7D` | `0.9010` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 20,170.00 USD | 11,360.00 USD | 4,600.00 USD |
| `1D` | `0.9030` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 6,430.00 USD | 3,760.00 USD | 4,220.00 USD |
| `7D` | `0.9030` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 12,700.00 USD | 9,020.00 USD | 25,870.00 USD |
| `1D` | `0.9050` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 8,300.00 USD | 3,640.00 USD | 3,200.00 USD |
| `7D` | `0.9050` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 35,230.00 USD | 25,340.00 USD | 27,300.00 USD |
| `1D` | `0.9070` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 3,810.00 USD | 488.01 USD | 803.91 USD |
| `7D` | `0.9070` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 37,740.00 USD | 8,280.00 USD | 15,280.00 USD |
| `1D` | `0.9090` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 18,830.00 USD | 4,070.00 USD | 4,140.00 USD |
| `7D` | `0.9090` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 13,790.00 USD | 7,650.00 USD | 6,240.00 USD |
| `1D` | `0.9110` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 13,080.00 USD | 791.28 USD | 10,580.00 USD |
| `7D` | `0.9110` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 8,490.00 USD | 7,660.00 USD | 17,140.00 USD |
| `1D` | `0.9130` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 4,770.00 USD | 441.47 USD | 4,830.00 USD |
| `7D` | `0.9130` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 26,980.00 USD | 2,030.00 USD | 680.66 USD |
| `1D` | `0.9150` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 14,130.00 USD | 2,620.00 USD | 8,480.00 USD |
| `7D` | `0.9150` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 41,000.00 USD | 11,200.00 USD | 34,610.00 USD |
| `1D` | `0.9170` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 3,440.00 USD | 435.13 USD | 452.67 USD |
| `7D` | `0.9170` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 22,610.00 USD | 14,690.00 USD | 18,060.00 USD |
| `1D` | `0.9190` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 2,770.00 USD | 138.43 USD | 186.24 USD |
| `7D` | `0.9190` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 33,980.00 USD | 4,720.00 USD | 19,620.00 USD |
| `1D` | `0.9210` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 1,470.00 USD | 77.80 USD | 2,330.00 USD |
| `7D` | `0.9210` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 22,070.00 USD | 7,060.00 USD | 15,880.00 USD |
| `1D` | `0.9230` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 10,750.00 USD | 2,010.00 USD | 907.53 USD |
| `7D` | `0.9230` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 35,230.00 USD | 11,600.00 USD | 37,340.00 USD |
| `1D` | `0.9250` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 19,800.00 USD | 8,960.00 USD | 14,770.00 USD |
| `7D` | `0.9250` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 56,800.00 USD | 8,470.00 USD | 30,000.00 USD |
| `1D` | `0.9270` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 15,140.00 USD | 5,250.00 USD | 10,980.00 USD |
| `7D` | `0.9270` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 70,300.00 USD | 9,450.00 USD | 21,390.00 USD |
| `1D` | `0.9290` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 25,560.00 USD | 4,290.00 USD | 6,800.00 USD |
| `7D` | `0.9290` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 39,160.00 USD | 7,600.00 USD | 31,560.00 USD |
| `1D` | `0.9310` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 10,550.00 USD | 12,130.00 USD | 21,600.00 USD |
| `7D` | `0.9310` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 26,530.00 USD | 10,380.00 USD | 7,590.00 USD |
| `1D` | `0.9330` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 21,800.00 USD | 9,020.00 USD | 9,250.00 USD |
| `7D` | `0.9330` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 33,550.00 USD | 9,810.00 USD | 25,450.00 USD |
| `1D` | `0.9350` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 36,280.00 USD | 10,930.00 USD | 13,660.00 USD |
| `7D` | `0.9350` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 82,010.00 USD | 29,520.00 USD | 17,380.00 USD |
| `1D` | `0.9370` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 38,570.00 USD | 12,840.00 USD | 20,310.00 USD |
| `7D` | `0.9370` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 29,580.00 USD | 13,940.00 USD | 7,230.00 USD |
| `1D` | `0.9390` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 17,600.00 USD | 14,430.00 USD | 13,920.00 USD |
| `7D` | `0.9390` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 18,750.00 USD | 15,630.00 USD | 12,300.00 USD |
| `1D` | `0.9410` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 35,770.00 USD | 11,440.00 USD | 2,030.00 USD |
| `7D` | `0.9410` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 45,790.00 USD | 14,190.00 USD | 4,310.00 USD |
| `1D` | `0.9430` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 21,520.00 USD | 8,450.00 USD | 3,110.00 USD |
| `7D` | `0.9430` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 54,680.00 USD | 11,000.00 USD | 10,990.00 USD |
| `1D` | `0.9450` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 36,850.00 USD | 20,360.00 USD | 40,150.00 USD |
| `7D` | `0.9450` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 77,230.00 USD | 33,680.00 USD | 41,460.00 USD |
| `1D` | `0.9470` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 45,200.00 USD | 24,790.00 USD | 40,860.00 USD |
| `7D` | `0.9470` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 108,740.00 USD | 23,910.00 USD | 50,080.00 USD |
| `1D` | `0.9490` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 77,380.00 USD | 17,790.00 USD | 28,210.00 USD |
| `7D` | `0.9490` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 129,370.00 USD | 34,510.00 USD | 121,560.00 USD |
| `1D` | `0.9510` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 35,280.00 USD | 32,810.00 USD | 43,040.00 USD |
| `7D` | `0.9510` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 208,950.00 USD | 43,880.00 USD | 81,400.00 USD |
| `1D` | `0.9530` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 55,340.00 USD | 18,390.00 USD | 21,850.00 USD |
| `7D` | `0.9530` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 79,700.00 USD | 28,300.00 USD | 123,120.00 USD |
| `1D` | `0.9550` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 81,780.00 USD | 37,060.00 USD | 37,090.00 USD |
| `7D` | `0.9550` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 172,820.00 USD | 90,270.00 USD | 56,600.00 USD |
| `1D` | `0.9570` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 122,040.00 USD | 43,130.00 USD | 68,880.00 USD |
| `7D` | `0.9570` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 129,820.00 USD | 46,750.00 USD | 128,830.00 USD |
| `1D` | `0.9590` | 884,370.00 USD | 0.00 USD | 884,370.00 USD | 49,590.00 USD | 20,710.00 USD | 31,260.00 USD |
| `7D` | `0.9590` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 176,280.00 USD | 57,050.00 USD | 72,780.00 USD |
| `1D` | `0.9610` | 782,810.00 USD | 0.00 USD | 782,810.00 USD | 53,350.00 USD | 22,130.00 USD | 12,040.00 USD |
| `7D` | `0.9610` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 183,020.00 USD | 77,730.00 USD | 32,710.00 USD |
| `1D` | `0.9630` | 695,300.00 USD | 0.00 USD | 695,300.00 USD | 33,580.00 USD | 19,430.00 USD | 22,150.00 USD |
| `7D` | `0.9630` | 889,220.00 USD | 0.00 USD | 889,220.00 USD | 95,260.00 USD | 0.00 USD | 22,910.00 USD |
| `1D` | `0.9650` | 620,140.00 USD | 0.00 USD | 620,140.00 USD | 25,320.00 USD | 13,180.00 USD | 31,270.00 USD |
| `7D` | `0.9650` | 771,050.00 USD | 0.00 USD | 771,050.00 USD | 65,160.00 USD | 0.00 USD | 9,130.00 USD |
| `1D` | `0.9670` | 550,370.00 USD | 0.00 USD | 550,370.00 USD | 28,790.00 USD | 14,700.00 USD | 35,790.00 USD |
| `7D` | `0.9670` | 696,760.00 USD | 0.00 USD | 696,760.00 USD | 31,440.00 USD | 12,340.00 USD | 45,920.00 USD |
| `1D` | `0.9690` | 471,090.00 USD | 0.00 USD | 471,090.00 USD | 43,730.00 USD | 28,330.00 USD | 31,220.00 USD |
| `7D` | `0.9690` | 607,060.00 USD | 0.00 USD | 607,060.00 USD | 3,040.00 USD | 10,300.00 USD | 53,420.00 USD |
| `1D` | `0.9710` | 367,800.00 USD | 0.00 USD | 367,800.00 USD | 60,380.00 USD | 17,310.00 USD | 21,290.00 USD |
| `7D` | `0.9710` | 540,300.00 USD | 0.00 USD | 540,300.00 USD | 84,760.00 USD | 13,910.00 USD | 9,790.00 USD |
| `1D` | `0.9730` | 268,810.00 USD | 0.00 USD | 268,810.00 USD | 23,620.00 USD | 691.66 USD | 13,670.00 USD |
| `7D` | `0.9730` | 431,830.00 USD | 0.00 USD | 431,830.00 USD | 0.00 USD | 0.00 USD | 7,510.00 USD |
| `1D` | `0.9750` | 230,830.00 USD | 0.00 USD | 230,830.00 USD | 16,060.00 USD | 23,220.00 USD | 15,960.00 USD |
| `7D` | `0.9750` | 424,320.00 USD | 0.00 USD | 424,320.00 USD | 0.00 USD | 16,590.00 USD | 3,280.00 USD |
| `1D` | `0.9770` | 175,590.00 USD | 0.00 USD | 175,590.00 USD | 35,620.00 USD | 2,870.00 USD | 10,900.00 USD |
| `7D` | `0.9770` | 404,450.00 USD | 0.00 USD | 404,450.00 USD | 15,320.00 USD | 5,480.00 USD | 31,410.00 USD |
| `1D` | `0.9790` | 126,210.00 USD | 0.00 USD | 126,210.00 USD | 9,790.00 USD | 4,480.00 USD | 8,180.00 USD |
| `7D` | `0.9790` | 352,240.00 USD | 0.00 USD | 352,240.00 USD | 0.00 USD | 15,440.00 USD | 89,530.00 USD |
| `1D` | `0.9810` | 103,770.00 USD | 0.00 USD | 103,770.00 USD | 4,500.00 USD | 376.40 USD | 9,030.00 USD |
| `7D` | `0.9810` | 247,280.00 USD | 0.00 USD | 247,280.00 USD | 7,900.00 USD | 0.00 USD | 133,380.00 USD |
| `1D` | `0.9830` | 89,860.00 USD | 0.00 USD | 89,860.00 USD | 20,680.00 USD | 13,960.00 USD | 15,270.00 USD |
| `7D` | `0.9830` | 106,000.00 USD | 0.00 USD | 106,000.00 USD | 2,190.00 USD | 0.00 USD | 21,010.00 USD |
| `1D` | `0.9850` | 39,960.00 USD | 0.00 USD | 39,960.00 USD | 575.70 USD | 0.00 USD | 10,740.00 USD |
| `7D` | `0.9850` | 82,800.00 USD | 0.00 USD | 82,800.00 USD | 0.00 USD | 17,440.00 USD | 22,820.00 USD |
| `1D` | `0.9870` | 28,650.00 USD | 0.00 USD | 28,650.00 USD | 13,720.00 USD | 8,090.00 USD | 0.00 USD |
| `7D` | `0.9870` | 42,540.00 USD | 0.00 USD | 42,540.00 USD | 40,020.00 USD | 0.00 USD | 803.95 USD |
| `1D` | `0.9890` | 6,840.00 USD | 0.00 USD | 6,840.00 USD | 0.00 USD | 0.00 USD | 6,840.00 USD |
| `7D` | `0.9890` | 1,720.00 USD | 0.00 USD | 1,720.00 USD | 0.00 USD | 284.26 USD | 1,440.00 USD |
| `1D` | `0.9900` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9900` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9910` | 70,200.00 USD | 70,200.00 USD | 0.00 USD | 50,430.00 USD | 0.00 USD | 19,770.00 USD |
| `7D` | `0.9910` | 19,590.00 USD | 19,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD |
| `1D` | `0.9930` | 90,960.00 USD | 90,960.00 USD | 0.00 USD | 6,920.00 USD | 13,250.00 USD | 601.92 USD |
| `7D` | `0.9930` | 20,810.00 USD | 20,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,220.00 USD |
| `1D` | `0.9950` | 92,600.00 USD | 92,600.00 USD | 0.00 USD | 0.00 USD | 1,630.00 USD | 0.00 USD |
| `7D` | `0.9950` | 80,090.00 USD | 80,090.00 USD | 0.00 USD | 16,510.00 USD | 0.00 USD | 42,770.00 USD |
| `1D` | `0.9970` | 121,460.00 USD | 121,460.00 USD | 0.00 USD | 26,250.00 USD | 1,000.00 USD | 1,610.00 USD |
| `7D` | `0.9970` | 152,710.00 USD | 152,710.00 USD | 0.00 USD | 68,870.00 USD | 0.00 USD | 3,750.00 USD |
| `1D` | `0.9990` | 124,620.00 USD | 124,620.00 USD | 0.00 USD | 0.00 USD | 1,760.00 USD | 1,400.00 USD |
| `1D` | `1.00` | 178,770.00 USD | 178,770.00 USD | 0.00 USD | 31,780.00 USD | 22,180.00 USD | 192.37 USD |
| `7D` | `1.00` | 205,560.00 USD | 205,560.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.00` | 259,040.00 USD | 259,040.00 USD | 0.00 USD | 53,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.01` | 211,530.00 USD | 211,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 32,760.00 USD |
| `1D` | `1.01` | 226,200.00 USD | 226,200.00 USD | 0.00 USD | 5,860.00 USD | 8,800.00 USD | 0.00 USD |
| `7D` | `1.01` | 274,540.00 USD | 274,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,500.00 USD |
| `1D` | `1.01` | 254,920.00 USD | 254,920.00 USD | 0.00 USD | 7,210.00 USD | 21,350.00 USD | 155.80 USD |
| `7D` | `1.01` | 308,640.00 USD | 308,640.00 USD | 0.00 USD | 20,090.00 USD | 14,020.00 USD | 0.00 USD |
| `1D` | `1.01` | 269,330.00 USD | 269,330.00 USD | 0.00 USD | 10,040.00 USD | 4,020.00 USD | 352.75 USD |
| `7D` | `1.01` | 359,820.00 USD | 359,820.00 USD | 0.00 USD | 16,020.00 USD | 34,770.00 USD | 388.43 USD |
| `1D` | `1.01` | 339,720.00 USD | 339,720.00 USD | 0.00 USD | 25,750.00 USD | 4,350.00 USD | 40,290.00 USD |
| `7D` | `1.01` | 393,260.00 USD | 393,260.00 USD | 0.00 USD | 0.00 USD | 26,360.00 USD | 7,070.00 USD |
| `1D` | `1.02` | 372,480.00 USD | 372,480.00 USD | 0.00 USD | 1,130.00 USD | 7,410.00 USD | 24,210.00 USD |
| `7D` | `1.02` | 441,210.00 USD | 441,210.00 USD | 0.00 USD | 0.00 USD | 21,770.00 USD | 26,170.00 USD |
| `1D` | `1.02` | 413,060.00 USD | 413,060.00 USD | 0.00 USD | 29,890.00 USD | 0.00 USD | 10,690.00 USD |
| `7D` | `1.02` | 528,880.00 USD | 528,880.00 USD | 0.00 USD | 0.00 USD | 75,860.00 USD | 11,810.00 USD |
| `1D` | `1.02` | 457,560.00 USD | 457,560.00 USD | 0.00 USD | 27,370.00 USD | 2,230.00 USD | 14,900.00 USD |
| `7D` | `1.02` | 666,970.00 USD | 666,970.00 USD | 0.00 USD | 44,170.00 USD | 26,480.00 USD | 67,450.00 USD |
| `1D` | `1.02` | 548,670.00 USD | 548,670.00 USD | 0.00 USD | 49,000.00 USD | 2,990.00 USD | 39,120.00 USD |
| `7D` | `1.02` | 954,500.00 USD | 954,500.00 USD | 0.00 USD | 56,570.00 USD | 85,290.00 USD | 145,680.00 USD |
| `1D` | `1.02` | 643,470.00 USD | 643,470.00 USD | 0.00 USD | 29,910.00 USD | 28,580.00 USD | 36,320.00 USD |
| `7D` | `1.02` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 11,270.00 USD | 48,490.00 USD | 29,170.00 USD |
| `1D` | `1.03` | 691,940.00 USD | 691,940.00 USD | 0.00 USD | 26,670.00 USD | 10,240.00 USD | 11,550.00 USD |
| `7D` | `1.03` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 160,800.00 USD | 126,720.00 USD | 24,880.00 USD |
| `1D` | `1.03` | 780,750.00 USD | 780,750.00 USD | 0.00 USD | 29,890.00 USD | 23,690.00 USD | 35,230.00 USD |
| `7D` | `1.03` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 141,540.00 USD | 39,160.00 USD | 30,660.00 USD |
| `1D` | `1.03` | 971,370.00 USD | 971,370.00 USD | 0.00 USD | 133,530.00 USD | 16,610.00 USD | 40,480.00 USD |
| `7D` | `1.03` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 170,960.00 USD | 7,320.00 USD | 19,590.00 USD |
| `1D` | `1.03` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 58,000.00 USD | 104.84 USD | 24,580.00 USD |
| `7D` | `1.03` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 122,520.00 USD | 0.00 USD | 3,750.00 USD |
| `1D` | `1.03` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 26,980.00 USD | 26,510.00 USD | 37,510.00 USD |
| `7D` | `1.03` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 259,060.00 USD | 8,500.00 USD | 43,490.00 USD |
| `1D` | `1.04` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 78,650.00 USD | 11,980.00 USD | 67,970.00 USD |
| `7D` | `1.04` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 192,080.00 USD | 4,140.00 USD | 109,460.00 USD |
| `1D` | `1.04` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 10,510.00 USD | 4,170.00 USD | 12,470.00 USD |
| `7D` | `1.04` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 239,200.00 USD | 8,210.00 USD | 117,630.00 USD |
| `1D` | `1.04` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 4,050.00 USD | 4,370.00 USD | 6,940.00 USD |
| `7D` | `1.04` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 276,890.00 USD | 1,800.00 USD | 159,500.00 USD |
| `1D` | `1.04` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 14,730.00 USD | 12,900.00 USD | 28,900.00 USD |
| `7D` | `1.04` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD |
| `1D` | `1.04` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 5,920.00 USD | 11,350.00 USD | 13,170.00 USD |
| `7D` | `1.04` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 184,670.00 USD | 23,440.00 USD | 59,810.00 USD |
| `1D` | `1.05` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 29,640.00 USD | 7,470.00 USD | 1,860.00 USD |
| `7D` | `1.05` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 178,360.00 USD | 96,750.00 USD | 238,570.00 USD |
| `1D` | `1.05` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 2,200.00 USD | 8,000.00 USD | 17,750.00 USD |
| `7D` | `1.05` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 116,670.00 USD | 13,190.00 USD | 77,320.00 USD |
| `1D` | `1.05` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 62,490.00 USD | 4,130.00 USD | 22,780.00 USD |
| `7D` | `1.05` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 175,210.00 USD | 43,000.00 USD | 87,050.00 USD |
| `1D` | `1.05` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 15,480.00 USD | 6,220.00 USD | 27,030.00 USD |
| `7D` | `1.05` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 61,670.00 USD | 56,570.00 USD | 74,380.00 USD |
| `1D` | `1.05` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 14,400.00 USD | 979.80 USD | 27,520.00 USD |
| `7D` | `1.05` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 125,020.00 USD | 33,480.00 USD | 72,330.00 USD |
| `1D` | `1.06` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 5,730.00 USD | 6,510.00 USD | 20,020.00 USD |
| `7D` | `1.06` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 218,860.00 USD | 71,040.00 USD | 106,190.00 USD |
| `1D` | `1.06` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 27,860.00 USD | 3,010.00 USD | 13,590.00 USD |
| `7D` | `1.06` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 232,260.00 USD | 71,280.00 USD | 139,220.00 USD |
| `1D` | `1.06` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 1,670.00 USD | 8,320.00 USD | 10,800.00 USD |
| `7D` | `1.06` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 130,860.00 USD | 57,130.00 USD | 78,020.00 USD |
| `1D` | `1.06` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 4,830.00 USD | 3,040.00 USD | 2,590.00 USD |
| `7D` | `1.06` | 6,620,000.00 USD | 6,620,000.00 USD | 0.00 USD | 141,700.00 USD | 72,770.00 USD | 71,060.00 USD |
| `1D` | `1.06` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 7,310.00 USD | 3,890.00 USD | 9,680.00 USD |
| `7D` | `1.06` | 6,820,000.00 USD | 6,820,000.00 USD | 0.00 USD | 90,400.00 USD | 28,820.00 USD | 83,920.00 USD |
| `1D` | `1.07` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 13,480.00 USD | 4,670.00 USD | 6,100.00 USD |
| `7D` | `1.07` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 86,760.00 USD | 43,510.00 USD | 82,980.00 USD |
| `1D` | `1.07` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 6,330.00 USD | 4,160.00 USD | 6,120.00 USD |
| `7D` | `1.07` | 7,330,000.00 USD | 7,330,000.00 USD | 0.00 USD | 219,670.00 USD | 15,540.00 USD | 62,270.00 USD |
| `1D` | `1.07` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 16,300.00 USD | 3,230.00 USD | 4,120.00 USD |
| `7D` | `1.07` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 141,570.00 USD | 35,440.00 USD | 52,290.00 USD |
| `1D` | `1.07` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 5,820.00 USD | 4,330.00 USD | 12,130.00 USD |
| `7D` | `1.07` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 96,630.00 USD | 43,620.00 USD | 95,510.00 USD |
| `1D` | `1.07` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 4,510.00 USD | 5,370.00 USD | 10,050.00 USD |
| `7D` | `1.07` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 97,650.00 USD | 27,650.00 USD | 60,670.00 USD |
| `1D` | `1.08` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 8,480.00 USD | 3,520.00 USD | 5,470.00 USD |
| `7D` | `1.08` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 75,040.00 USD | 29,680.00 USD | 48,910.00 USD |
| `1D` | `1.08` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 7,600.00 USD | 3,640.00 USD | 36.19 USD |
| `7D` | `1.08` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 166,380.00 USD | 21,770.00 USD | 52,480.00 USD |
| `1D` | `1.08` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 8,690.00 USD | 1,510.00 USD | 2,570.00 USD |
| `7D` | `1.08` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 164,440.00 USD | 23,420.00 USD | 33,710.00 USD |
| `1D` | `1.08` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 2,390.00 USD | 3,030.00 USD | 2,640.00 USD |
| `7D` | `1.08` | 8,800,000.00 USD | 8,800,000.00 USD | 0.00 USD | 61,330.00 USD | 40,620.00 USD | 100,590.00 USD |
| `1D` | `1.08` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 5,310.00 USD | 3,010.00 USD | 6,150.00 USD |
| `7D` | `1.08` | 8,940,000.00 USD | 8,940,000.00 USD | 0.00 USD | 79,580.00 USD | 18,560.00 USD | 46,440.00 USD |
| `1D` | `1.09` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 4,380.00 USD | 3,600.00 USD | 6,640.00 USD |
| `7D` | `1.09` | 9,170,000.00 USD | 9,170,000.00 USD | 0.00 USD | 102,510.00 USD | 58,250.00 USD | 69,260.00 USD |
| `1D` | `1.09` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 2,400.00 USD | 1,680.00 USD | 2,270.00 USD |
| `7D` | `1.09` | 9,350,000.00 USD | 9,350,000.00 USD | 0.00 USD | 71,650.00 USD | 23,730.00 USD | 85,300.00 USD |
| `1D` | `1.09` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 7,620.00 USD | 2,540.00 USD | 1,890.00 USD |
| `7D` | `1.09` | 9,480,000.00 USD | 9,480,000.00 USD | 0.00 USD | 70,660.00 USD | 25,600.00 USD | 32,870.00 USD |
| `1D` | `1.09` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 149.14 USD | 2,650.00 USD | 2,140.00 USD |
| `7D` | `1.09` | 9,670,000.00 USD | 9,670,000.00 USD | 0.00 USD | 81,350.00 USD | 40,310.00 USD | 68,280.00 USD |
| `1D` | `1.09` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 2,430.00 USD | 3,110.00 USD | 73.78 USD |
| `7D` | `1.09` | 9,840,000.00 USD | 9,840,000.00 USD | 0.00 USD | 56,240.00 USD | 23,050.00 USD | 92,520.00 USD |
| `1D` | `1.10` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 3,620.00 USD | 1,840.00 USD | 9,740.00 USD |
| `7D` | `1.10` | 10,000,000.00 USD | 10,000,000.00 USD | 0.00 USD | 88,860.00 USD | 25,120.00 USD | 43,830.00 USD |
| `1D` | `1.10` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 2,310.00 USD | 775.48 USD | 1,240.00 USD |
| `7D` | `1.10` | 10,330,000.00 USD | 10,330,000.00 USD | 0.00 USD | 188,000.00 USD | 49,270.00 USD | 89,650.00 USD |
| `1D` | `1.10` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 132.59 USD | 23.47 USD | 1,890.00 USD |
| `7D` | `1.10` | 10,520,000.00 USD | 10,520,000.00 USD | 0.00 USD | 122,300.00 USD | 43,950.00 USD | 26,760.00 USD |
| `1D` | `1.10` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 5,060.00 USD | 3,840.00 USD | 4,220.00 USD |
| `7D` | `1.10` | 10,740,000.00 USD | 10,740,000.00 USD | 0.00 USD | 91,720.00 USD | 19,120.00 USD | 110,490.00 USD |
| `1D` | `1.10` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 37.25 USD | 2,030.00 USD | 3,090.00 USD |
| `7D` | `1.10` | 10,820,000.00 USD | 10,820,000.00 USD | 0.00 USD | 36,570.00 USD | 10,260.00 USD | 31,450.00 USD |
| `1D` | `1.11` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 4,080.00 USD | 1,690.00 USD | 111.00 USD |
| `7D` | `1.11` | 10,930,000.00 USD | 10,930,000.00 USD | 0.00 USD | 51,840.00 USD | 24,560.00 USD | 34,190.00 USD |
| `1D` | `1.11` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 1,670.00 USD | 87.40 USD | 803.91 USD |
| `7D` | `1.11` | 11,120,000.00 USD | 11,120,000.00 USD | 0.00 USD | 80,930.00 USD | 42,090.00 USD | 63,380.00 USD |
| `1D` | `1.11` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 12,800.00 USD | 3,460.00 USD | 4,140.00 USD |
| `7D` | `1.11` | 11,270,000.00 USD | 11,270,000.00 USD | 0.00 USD | 69,040.00 USD | 16,250.00 USD | 64,910.00 USD |
| `1D` | `1.11` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 11,280.00 USD | 260.69 USD | 10,580.00 USD |
| `7D` | `1.11` | 11,360,000.00 USD | 11,360,000.00 USD | 0.00 USD | 20,190.00 USD | 43,670.00 USD | 25,640.00 USD |
| `1D` | `1.11` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 3,720.00 USD | 294.76 USD | 4,830.00 USD |
| `7D` | `1.11` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 34,700.00 USD | 14,480.00 USD | 9,990.00 USD |
| `1D` | `1.12` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 56.85 USD | 1,860.00 USD | 4,080.00 USD |
| `7D` | `1.12` | 11,560,000.00 USD | 11,560,000.00 USD | 0.00 USD | 68,170.00 USD | 45,850.00 USD | 32,030.00 USD |
| `1D` | `1.12` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 10,810.00 USD | 658.54 USD | 4,390.00 USD |
| `7D` | `1.12` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 24,700.00 USD | 23,340.00 USD | 13,750.00 USD |
| `1D` | `1.12` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 382.75 USD | 452.67 USD |
| `7D` | `1.12` | 11,730,000.00 USD | 11,730,000.00 USD | 0.00 USD | 48,980.00 USD | 31,670.00 USD | 23,330.00 USD |
| `1D` | `1.12` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 12.35 USD | 186.24 USD |
| `7D` | `1.12` | 11,820,000.00 USD | 11,820,000.00 USD | 0.00 USD | 61,780.00 USD | 4,660.00 USD | 25,460.00 USD |
| `1D` | `1.12` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 199.10 USD | 0.00 USD | 2,330.00 USD |
| `7D` | `1.12` | 11,880,000.00 USD | 11,880,000.00 USD | 0.00 USD | 18,300.00 USD | 10,300.00 USD | 29,890.00 USD |
| `1D` | `1.13` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 1,020.00 USD | 870.54 USD |
| `7D` | `1.13` | 11,900,000.00 USD | 11,900,000.00 USD | 0.00 USD | 14,700.00 USD | 1,030.00 USD | 8,690.00 USD |
| `7D` | `1.13` | 12,030,000.00 USD | 12,030,000.00 USD | 0.00 USD | 56,500.00 USD | 19,040.00 USD | 45,770.00 USD |
| `7D` | `1.13` | 12,220,000.00 USD | 12,220,000.00 USD | 0.00 USD | 96,260.00 USD | 12,540.00 USD | 90,000.00 USD |
| `7D` | `1.13` | 12,260,000.00 USD | 12,260,000.00 USD | 0.00 USD | 16,560.00 USD | 0.00 USD | 22,800.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `209.62M` | Total OI Tokens: `211,637,237.7 DOT`
  * 1h OI Change: `-1.12%` | 4h OI Change: `-1.22%` | 24h OI Change: `-3.69%`
  * Exchange Breakdown: Binance=`36.57M` | Bybit=`24.70M` | OKX=`10.27M` | Hyperliquid=`5.75M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `5.92K` | Last 24h: `7.91K` | Last 3d: `-10.37K` | Last 7d: `-19.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0090%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0088%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0077%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `50.24%` | `49.76%` | `1.01` | 1,720,000.00 USD |
| `15M` | `Binance` | `56.41%` | `43.59%` | `1.29` | 589,360.00 USD |
| `15M` | `OKX` | `39.68%` | `60.32%` | `0.66` | 233,040.00 USD |
| `15M` | `Bybit` | `40.91%` | `59.09%` | `0.69` | 138,350.00 USD |
| `15M` | `KuCoin` | `54.67%` | `45.33%` | `1.21` | 138,350.00 USD |
| `15M` | `Gate` | `51.1%` | `48.9%` | `1.04` | 46,380.00 USD |
| `15M` | `Bitget` | `65.81%` | `34.19%` | `1.92` | 52,970.00 USD |
| `15M` | `BingX` | `51.13%` | `48.87%` | `1.05` | 138,160.00 USD |
| `15M` | `MEXC` | `64.25%` | `35.75%` | `1.80` | 80,260.00 USD |
| `15M` | `Bitunix` | `56.52%` | `43.48%` | `1.30` | 34,690.00 USD |
| `15M` | `Hyperliquid` | `32.6%` | `67.4%` | `0.48` | 15,740.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.46%` | `49.54%` | `1.02` | 181,980.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `2.25%` | `97.75%` | `0.02` | 62,760.00 USD |
| `15M` | `HTX` | `96.5%` | `3.5%` | `27.57` | 8,490.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `63.82%` | `36.18%` | `1.76` | 1,520.00 USD |
| `15M` | `Aster` | `41.25%` | `58.75%` | `0.70` | 132.26 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `56.41%` | `43.59%` | `1.29` | 589,360.00 USD |
| `15M` | `Global Accounts` | `50.24%` | `49.76%` | `1.01` | 1,720,000.00 USD |
| `1H` | `DOT` | `43.78%` | `56.22%` | `0.78` | 8,980,000.00 USD |
| `1H` | `Binance` | `45.53%` | `54.47%` | `0.84` | 3,200,000.00 USD |
| `1H` | `OKX` | `40.1%` | `59.9%` | `0.67` | 770,100.00 USD |
| `1H` | `Bybit` | `49.02%` | `50.98%` | `0.96` | 1,060,000.00 USD |
| `1H` | `KuCoin` | `49.73%` | `50.27%` | `0.99` | 530,730.00 USD |
| `1H` | `Gate` | `42.67%` | `57.33%` | `0.74` | 494,540.00 USD |
| `1H` | `Bitget` | `44.84%` | `55.16%` | `0.81` | 335,210.00 USD |
| `1H` | `BingX` | `40.64%` | `59.36%` | `0.68` | 628,630.00 USD |
| `1H` | `MEXC` | `37.28%` | `62.72%` | `0.59` | 431,020.00 USD |
| `1H` | `Bitunix` | `45.74%` | `54.26%` | `0.84` | 177,910.00 USD |
| `1H` | `Hyperliquid` | `20.29%` | `79.71%` | `0.25` | 116,460.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.07%` | `49.93%` | `1.00` | 928,710.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `4.95%` | `95.05%` | `0.05` | 275,830.00 USD |
| `1H` | `HTX` | `80.87%` | `19.13%` | `4.23` | 11,280.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `67.7%` | `32.3%` | `2.10` | 21,520.00 USD |
| `1H` | `Aster` | `5.79%` | `94.21%` | `0.06` | 4,130.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `45.53%` | `54.47%` | `0.84` | 3,200,000.00 USD |
| `1H` | `Global Accounts` | `43.78%` | `56.22%` | `0.78` | 8,980,000.00 USD |
| `4H` | `DOT` | `45.61%` | `54.39%` | `0.84` | 36,680,000.00 USD |
| `4H` | `Binance` | `44.49%` | `55.51%` | `0.80` | 13,210,000.00 USD |
| `4H` | `OKX` | `44.3%` | `55.7%` | `0.80` | 3,860,000.00 USD |
| `4H` | `Bybit` | `48.68%` | `51.32%` | `0.95` | 2,730,000.00 USD |
| `4H` | `KuCoin` | `50.06%` | `49.94%` | `1.00` | 2,130,000.00 USD |
| `4H` | `Gate` | `51.62%` | `48.38%` | `1.07` | 1,600,000.00 USD |
| `4H` | `Bitget` | `48.72%` | `51.28%` | `0.95` | 1,230,000.00 USD |
| `4H` | `BingX` | `38.49%` | `61.51%` | `0.63` | 2,650,000.00 USD |
| `4H` | `MEXC` | `50.13%` | `49.87%` | `1.01` | 2,170,000.00 USD |
| `4H` | `Bitunix` | `50.46%` | `49.54%` | `1.02` | 1,180,000.00 USD |
| `4H` | `Hyperliquid` | `47.64%` | `52.36%` | `0.91` | 954,810.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.15%` | `49.85%` | `1.01` | 3,620,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `18.46%` | `81.54%` | `0.23` | 993,880.00 USD |
| `4H` | `HTX` | `53.13%` | `46.87%` | `1.13` | 65,070.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `56.28%` | `43.72%` | `1.29` | 154,980.00 USD |
| `4H` | `Aster` | `31.85%` | `68.15%` | `0.47` | 133,670.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `44.49%` | `55.51%` | `0.80` | 13,210,000.00 USD |
| `4H` | `Global Accounts` | `45.61%` | `54.39%` | `0.84` | 36,680,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.02` | `1.02` | `1.02` | `1.02` | `1.01` | 1,420,574.95 USD | 1,000,262.40 USD | 420,312.55 USD | 579,949.86 USD | `+40.83%` | `13B / 20S` |
| `0:00 UTC` | `1.02` | `1.02` | `1.02` | `1.02` | `1.01` | 1,273,423.64 USD | 481,734.41 USD | 791,689.23 USD | -309,954.82 USD | `-24.34%` | `9B / 29S` |
| `5:00 UTC` | `1.01` | `1.01` | `1.01` | `1.01` | `1.01` | 657,161.08 USD | 244,063.77 USD | 413,097.31 USD | -169,033.55 USD | `-25.72%` | `3B / 15S` |
| `0:00 UTC` | `1.01` | `1.01` | `1.01` | `1.01` | `1.00` | 605,145.48 USD | 242,805.14 USD | 362,340.33 USD | -119,535.19 USD | `-19.75%` | `3B / 20S` |
| `5:00 UTC` | `1.01` | `1.01` | `1.01` | `1.01` | `1.00` | 367,151.31 USD | 115,663.71 USD | 251,487.60 USD | -135,823.89 USD | `-36.99%` | `2B / 13S` |
| `0:00 UTC` | `1.00` | `1.00` | `1.00` | `1.01` | `0.9990` | 615,154.97 USD | 223,058.23 USD | 392,096.73 USD | -169,038.50 USD | `-27.48%` | `6B / 35S` |
| `5:00 UTC` | `1.00` | `1.00` | `1.00` | `1.00` | `0.9973` | 953,336.44 USD | 578,861.35 USD | 374,475.09 USD | 204,386.27 USD | `+21.44%` | `11B / 7S` |
| `0:00 UTC` | `0.9950` | `0.9984` | `0.9950` | `1.00` | `0.9922` | 743,609.00 USD | 261,947.82 USD | 481,661.18 USD | -219,713.36 USD | `-29.55%` | `13B / 51S` |
| `5:00 UTC` | `0.9889` | `0.9893` | `0.9889` | `0.9946` | `0.9848` | 979,161.78 USD | 393,210.73 USD | 585,951.05 USD | -192,740.33 USD | `-19.68%` | `5B / 24S` |
| `0:00 UTC` | `0.9922` | `0.9909` | `0.9922` | `0.9929` | `0.9883` | 348,194.15 USD | 175,287.20 USD | 172,906.94 USD | 2,380.26 USD | `+0.68%` | `3B / 6S` |

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
| `5m` | 4,510.00 USD | 13,920.00 USD | **`ACCUMULATION`** |
| `15m` | 28,930.00 USD | 13,620.00 USD | **`ACCUMULATION`** |
| `30m` | -71,690.00 USD | -607,260.00 USD | **`DISTRIBUTION`** |
| `1h` | -22,600.00 USD | -432,820.00 USD | **`DISTRIBUTION`** |
| `2h` | -45,270.00 USD | -1,550,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -47,990.00 USD | -1,920,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -122,120.00 USD | -1,560,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -206,810.00 USD | -2,150,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -138,270.00 USD | -1,140,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -236,190.00 USD | -3,840,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,380,000.00 USD | -18,220,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,420,000.00 USD | -73,290,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+4.51K` | 15m=`+28.93K` | 1h=`-22.60K` | 24h=`-236.19K`
* Futures Capital Netflows: 5m=`+13.92K` | 15m=`+13.62K` | 1h=`-432.82K` | 24h=`-3.84M`
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
  * `2026-10-29 23:30:59 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:59 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:59 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:59 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:54:59 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:44:59 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:40:59 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:41:59 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:41:59 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:41:59 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:41:59 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `0.9139` (Risk Distance: `0.0400` pts)
  * +2.5R Take Profit: `1.05`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9947` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.03` (Risk Distance: `0.0400` pts)
  * +2.5R Take Profit: `0.8947`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9989`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
