# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 00:50:30 IST` (`2026-10-29 19:20:30 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9700` | **Live Ask Quote**: `0.9900` | **Mid Price**: `0.9800`
- **Spread Points**: `20.00` | **Spread BPS**: `204.08 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.9776` | VWAP Z-Score: `-0.32` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0075` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `39.84` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.02` | Lower -3.00σ Band: `0.9350`
  * Upper +2.51σ Band: `1.01` | Lower -2.51σ Band: `0.9419`
  * Upper +2.01σ Band: `1.01` | Lower -2.01σ Band: `0.9490`
  * Upper +2.00σ Band: `1.01` | Lower -2.00σ Band: `0.9492`
  * Upper +1.28σ Band: `0.9958` | Lower -1.28σ Band: `0.9594`
  * Upper +1.00σ Band: `0.9918` | Lower -1.00σ Band: `0.9634`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9800` | EMA-20=`0.9840` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9827` (Slope: `+0.0000`) | EMA-100=`0.9831`
  * Institutional Anchors: EMA-144=`0.9841` | EMA-200=`0.9846` (Slope: `+0.0101`) | EMA-233=`0.9844`
- **Range Boundaries**: 24H High=`1.03` | 24H Low=`0.9510` | Weekly High=`1.03` | Weekly Low=`0.9510`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9938` (Distance: `-1.39%`)
  * Point of Control (POC) = `0.9630` (Distance: `+1.76%`)
  * Value Area Low (VAL) = `0.9530` (Distance: `+2.83%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `0.9761` - `0.9839`
  * Optimal Trade Entry (OTE 0.705): `0.9820`
  * Structural Invalidation Anchor (0.786): `0.9878`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9827` | `0.9861` | `0.9825` | `0.9853` | `251,036` | 247,208.52 USD | 66,399.71 USD | `+26.86%` | -1,487,455.10 USD | `+0.50` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.9853` | `0.9866` | `0.9836` | `0.9840` | `118,697` | 116,889.95 USD | 32,749.43 USD | `+28.02%` | -1,454,705.67 USD | `+0.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.9839` | `0.9848` | `0.9802` | `0.9819` | `177,967` | 174,893.05 USD | 4,459.75 USD | `+2.55%` | -1,450,245.92 USD | `+0.11` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.9858` | `0.9872` | `0.9766` | `0.9804` | `1,791,023` | 1,756,422.05 USD | -186,041.32 USD | `-10.59%` | -1,827,917.35 USD | `-0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.9804` | `0.9866` | `0.9789` | `0.9840` | `963,740` | 947,049.41 USD | 493,472.58 USD | `+52.11%` | -1,334,444.77 USD | `+2.41` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.9839` | `0.9848` | `0.9799` | `0.9805` | `465,362` | 456,870.22 USD | -18,418.97 USD | `-4.03%` | -1,352,863.74 USD | `+0.19` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `1.01` | `1.01` | `0.9847` | `0.9918` | `3,301,086` | 3,291,262.18 USD | -377,105.92 USD | `-11.46%` | -1,426,808.60 USD | `-1.10` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.9918` | `0.9929` | `0.9766` | `0.9840` | `3,542,573` | 3,482,685.13 USD | 238,678.91 USD | `+6.85%` | -1,188,129.69 USD | `+0.79` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.9839` | `0.9848` | `0.9799` | `0.9803` | `464,628` | 456,151.03 USD | -19,138.16 USD | `-4.20%` | -1,207,267.85 USD | `-0.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | -137,778.42 USD | `+0.23` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | -315,355.23 USD | `-0.25` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9803` | `10,175,984` | 10,132,979.85 USD | -891,912.62 USD | `-8.80%` | -1,207,267.85 USD | `-1.32` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.01` | `1.01` | `0.9612` | `0.9700` | `15,616,467` | 15,304,422.31 USD | 595,816.59 USD | `+3.89%` | -236,044.76 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.9699` | `0.9906` | `0.9674` | `0.9732` | `8,505,701` | 8,320,368.15 USD | 13,201.93 USD | `+0.16%` | -222,842.83 USD | `+0.15` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | -137,778.42 USD | `+0.23` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | -315,355.23 USD | `-0.25` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9803` | `10,175,984` | 10,132,979.85 USD | -891,912.62 USD | `-8.80%` | -1,207,267.85 USD | `-1.32` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.9800`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:43:50 IST` |

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
  * 24H Horizon: Short MP=`1.04` (Vol: 74,700.00 USD, Dist: `+5.40%`) | Long MP=`0.9471` (Vol: 122,200.00 USD, Dist: `--3.75%`)
  * 48H Horizon: Short MP=`1.04` (Vol: 74,700.00 USD, Dist: `+5.40%`) | Long MP=`0.9471` (Vol: 122,200.00 USD, Dist: `--3.75%`)
  * 3D Horizon: Short MP=`1.04` (Vol: 74,700.00 USD, Dist: `+5.40%`) | Long MP=`0.9510` (Vol: 130,500.00 USD, Dist: `--3.35%`)
  * 7D Horizon: Short MP=`1.07` (Vol: 211,000.00 USD, Dist: `+8.57%`) | Long MP=`0.9606` (Vol: 177,500.00 USD, Dist: `--2.38%`)
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
| `7D` | `Long Liquidation` | `0.8760` | 5,040,000.00 USD | 5,040,000.00 USD | 6,030.00 USD | 6,200.00 USD | 5,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 171.88 USD | 258,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8780` | 2,550,000.00 USD | 2,550,000.00 USD | 19,130.00 USD | 7,220.00 USD | 10,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8780` | 5,030,000.00 USD | 5,030,000.00 USD | 15,500.00 USD | 50.60 USD | 5,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8795` | 948.01 USD | 257,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8800` | 2,510,000.00 USD | 2,510,000.00 USD | 4,390.00 USD | 5,110.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8800` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 3,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8820` | 2,500,000.00 USD | 2,500,000.00 USD | 8,250.00 USD | 3,980.00 USD | 150.13 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8820` | 5,000,000.00 USD | 5,000,000.00 USD | 8,660.00 USD | 3,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 2,490,000.00 USD | 2,490,000.00 USD | 7,440.00 USD | 1,810.00 USD | 711.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8840` | 4,990,000.00 USD | 4,990,000.00 USD | 4,540.00 USD | 5,480.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8860` | 2,480,000.00 USD | 2,480,000.00 USD | 4,980.00 USD | 1,690.00 USD | 4,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8860` | 4,980,000.00 USD | 4,980,000.00 USD | 15,460.00 USD | 7,970.00 USD | 2,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8880` | 2,470,000.00 USD | 2,470,000.00 USD | 12,080.00 USD | 3,880.00 USD | 9,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8880` | 4,950,000.00 USD | 4,950,000.00 USD | 7,150.00 USD | 1,990.00 USD | 11,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8900` | 2,440,000.00 USD | 2,440,000.00 USD | 3,630.00 USD | 4,230.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8900` | 4,930,000.00 USD | 4,930,000.00 USD | 23,060.00 USD | 6,420.00 USD | 20,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8920` | 2,430,000.00 USD | 2,430,000.00 USD | 4,920.00 USD | 3,160.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8920` | 4,880,000.00 USD | 4,880,000.00 USD | 45,890.00 USD | 9,570.00 USD | 15,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8925` | 526.84 USD | 256,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8940` | 2,420,000.00 USD | 2,420,000.00 USD | 4,240.00 USD | 23.75 USD | 966.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8940` | 4,810,000.00 USD | 4,810,000.00 USD | 7,120.00 USD | 8,030.00 USD | 26,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8960` | 2,410,000.00 USD | 2,410,000.00 USD | 1,740.00 USD | 6,100.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8960` | 4,770,000.00 USD | 4,770,000.00 USD | 30,390.00 USD | 10,550.00 USD | 12,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8975` | 9,210.00 USD | 256,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8980` | 2,400,000.00 USD | 2,400,000.00 USD | 5,420.00 USD | 65.95 USD | 992.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8980` | 4,720,000.00 USD | 4,720,000.00 USD | 31,140.00 USD | 6,910.00 USD | 36,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8995` | 3,820.00 USD | 247,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9000` | 2,400,000.00 USD | 2,400,000.00 USD | 3,760.00 USD | 759.75 USD | 2,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9000` | 4,640,000.00 USD | 4,640,000.00 USD | 39,940.00 USD | 14,050.00 USD | 14,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9020` | 2,390,000.00 USD | 2,390,000.00 USD | 4,180.00 USD | 3,230.00 USD | 2,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9020` | 4,570,000.00 USD | 4,570,000.00 USD | 16,980.00 USD | 11,760.00 USD | 15,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9035` | 180.16 USD | 243,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9040` | 2,380,000.00 USD | 2,380,000.00 USD | 3,130.00 USD | 2,520.00 USD | 5,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9040` | 4,530,000.00 USD | 4,530,000.00 USD | 17,160.00 USD | 5,930.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9060` | 2,370,000.00 USD | 2,370,000.00 USD | 9,620.00 USD | 1,660.00 USD | 111.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9060` | 4,490,000.00 USD | 4,490,000.00 USD | 53,450.00 USD | 30,600.00 USD | 41,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9080` | 2,360,000.00 USD | 2,360,000.00 USD | 5,800.00 USD | 3,150.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9080` | 4,370,000.00 USD | 4,370,000.00 USD | 21,830.00 USD | 3,470.00 USD | 6,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9095` | 951.34 USD | 243,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9100` | 2,340,000.00 USD | 2,340,000.00 USD | 21,840.00 USD | 2,070.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9100` | 4,340,000.00 USD | 4,340,000.00 USD | 6,870.00 USD | 10,340.00 USD | 17,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9120` | 2,310,000.00 USD | 2,310,000.00 USD | 4,140.00 USD | 274.81 USD | 3,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9120` | 4,300,000.00 USD | 4,300,000.00 USD | 21,820.00 USD | 4,010.00 USD | 371.71 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9135` | 143.42 USD | 242,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9140` | 2,310,000.00 USD | 2,310,000.00 USD | 5,930.00 USD | 1,290.00 USD | 4,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9140` | 4,280,000.00 USD | 4,280,000.00 USD | 46,660.00 USD | 8,800.00 USD | 26,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9160` | 2,290,000.00 USD | 2,290,000.00 USD | 14,110.00 USD | 100.68 USD | 3,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9160` | 4,190,000.00 USD | 4,190,000.00 USD | 12,570.00 USD | 12,620.00 USD | 17,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9180` | 2,280,000.00 USD | 2,280,000.00 USD | 49.41 USD | 452.74 USD | 583.97 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9180` | 4,150,000.00 USD | 4,150,000.00 USD | 29,970.00 USD | 9,070.00 USD | 13,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9185` | 145.86 USD | 242,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9195` | 7,330.00 USD | 241,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9200` | 2,280,000.00 USD | 2,280,000.00 USD | 2,990.00 USD | 112.72 USD | 192.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9200` | 4,100,000.00 USD | 4,100,000.00 USD | 40,700.00 USD | 4,910.00 USD | 22,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9220` | 2,270,000.00 USD | 2,270,000.00 USD | 7,870.00 USD | 1,100.00 USD | 3,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9220` | 4,030,000.00 USD | 4,030,000.00 USD | 15,960.00 USD | 2,440.00 USD | 15,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9225` | 8,360.00 USD | 234,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9240` | 2,260,000.00 USD | 2,260,000.00 USD | 14,860.00 USD | 5,440.00 USD | 36.99 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9240` | 4,000,000.00 USD | 4,000,000.00 USD | 56,450.00 USD | 17,850.00 USD | 51,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9260` | 2,240,000.00 USD | 2,240,000.00 USD | 10,930.00 USD | 9,570.00 USD | 21,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9260` | 3,870,000.00 USD | 3,870,000.00 USD | 32,320.00 USD | 3,140.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9280` | 2,200,000.00 USD | 2,200,000.00 USD | 24,160.00 USD | 4,120.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9280` | 3,810,000.00 USD | 3,810,000.00 USD | 85,040.00 USD | 14,050.00 USD | 26,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9295` | 253.01 USD | 226,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9300` | 2,160,000.00 USD | 2,160,000.00 USD | 14,980.00 USD | 1,350.00 USD | 16,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9300` | 3,690,000.00 USD | 3,690,000.00 USD | 27,510.00 USD | 12,060.00 USD | 18,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9320` | 2,130,000.00 USD | 2,130,000.00 USD | 24,520.00 USD | 12,760.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9320` | 3,630,000.00 USD | 3,630,000.00 USD | 29,490.00 USD | 7,900.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9325` | 324.42 USD | 324.42 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9335` | 361.45 USD | 226,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9340` | 2,080,000.00 USD | 2,080,000.00 USD | 21,360.00 USD | 11,340.00 USD | 10,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9340` | 3,590,000.00 USD | 3,590,000.00 USD | 53,710.00 USD | 31,710.00 USD | 24,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9360` | 2,040,000.00 USD | 2,040,000.00 USD | 49,360.00 USD | 11,970.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9360` | 3,480,000.00 USD | 3,480,000.00 USD | 59,280.00 USD | 6,250.00 USD | 14,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9365` | 6,560.00 USD | 225,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9375` | 196.97 USD | 219,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9380` | 1,960,000.00 USD | 1,960,000.00 USD | 25,680.00 USD | 14,710.00 USD | 10,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9380` | 3,400,000.00 USD | 3,400,000.00 USD | 20,200.00 USD | 20,670.00 USD | 12,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9400` | 1,900,000.00 USD | 1,900,000.00 USD | 28,130.00 USD | 10,650.00 USD | 13,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9400` | 3,340,000.00 USD | 3,340,000.00 USD | 26,270.00 USD | 6,010.00 USD | 7,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9405` | 141.83 USD | 218,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9420` | 1,850,000.00 USD | 1,850,000.00 USD | 30,630.00 USD | 12,880.00 USD | 3,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9420` | 3,300,000.00 USD | 3,300,000.00 USD | 51,440.00 USD | 21,220.00 USD | 10,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9440` | 1,810,000.00 USD | 1,810,000.00 USD | 35,560.00 USD | 18,570.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9440` | 3,220,000.00 USD | 3,220,000.00 USD | 57,220.00 USD | 26,910.00 USD | 26,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9445` | 1,060.00 USD | 218,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9455` | 106,880.00 USD | 217,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9460` | 1,740,000.00 USD | 1,740,000.00 USD | 31,490.00 USD | 28,910.00 USD | 59,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9460` | 3,110,000.00 USD | 3,110,000.00 USD | 70,510.00 USD | 19,530.00 USD | 44,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9475` | 323.19 USD | 110,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9480` | 1,620,000.00 USD | 1,620,000.00 USD | 95,800.00 USD | 23,630.00 USD | 34,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9480` | 2,980,000.00 USD | 2,980,000.00 USD | 202,170.00 USD | 42,900.00 USD | 92,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9495` | 105,430.00 USD | 110,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9500` | 1,470,000.00 USD | 1,470,000.00 USD | 40,200.00 USD | 9,070.00 USD | 38,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9500` | 2,640,000.00 USD | 2,640,000.00 USD | 125,620.00 USD | 46,290.00 USD | 114,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9515` | 405.62 USD | 5,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9520` | 1,380,000.00 USD | 1,380,000.00 USD | 66,670.00 USD | 32,590.00 USD | 23,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9520` | 2,350,000.00 USD | 2,350,000.00 USD | 144,770.00 USD | 19,800.00 USD | 57,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9540` | 1,260,000.00 USD | 1,260,000.00 USD | 52,780.00 USD | 30,680.00 USD | 29,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9540` | 2,130,000.00 USD | 2,130,000.00 USD | 116,590.00 USD | 92,780.00 USD | 108,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9555` | 3,160.00 USD | 4,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9560` | 1,150,000.00 USD | 1,150,000.00 USD | 122,960.00 USD | 46,040.00 USD | 63,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9560` | 1,810,000.00 USD | 1,810,000.00 USD | 207,570.00 USD | 32,950.00 USD | 87,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9580` | 913,420.00 USD | 913,420.00 USD | 46,030.00 USD | 28,570.00 USD | 32,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9580` | 1,480,000.00 USD | 1,480,000.00 USD | 107,300.00 USD | 48,150.00 USD | 119,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9585` | 1,530.00 USD | 1,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9600` | 806,220.00 USD | 806,220.00 USD | 94,650.00 USD | 29,910.00 USD | 10,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9600` | 1,210,000.00 USD | 1,210,000.00 USD | 222,250.00 USD | 82,170.00 USD | 59,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9620` | 671,470.00 USD | 671,470.00 USD | 50,390.00 USD | 18,850.00 USD | 13,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9620` | 844,540.00 USD | 844,540.00 USD | 140,700.00 USD | 46,240.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9640` | 589,070.00 USD | 589,070.00 USD | 21,690.00 USD | 14,940.00 USD | 32,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9640` | 631,520.00 USD | 631,520.00 USD | 84,900.00 USD | 778.20 USD | 6,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9660` | 519,710.00 USD | 519,710.00 USD | 76,360.00 USD | 26,330.00 USD | 35,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9660` | 539,670.00 USD | 539,670.00 USD | 40,050.00 USD | 9,550.00 USD | 31,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9680` | 381,870.00 USD | 381,870.00 USD | 39,890.00 USD | 18,800.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9680` | 458,670.00 USD | 458,670.00 USD | 26,480.00 USD | 4,670.00 USD | 36,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9700` | 284,470.00 USD | 284,470.00 USD | 52,020.00 USD | 17,520.00 USD | 19,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9700` | 390,580.00 USD | 390,580.00 USD | 33,960.00 USD | 25,160.00 USD | 36,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9720` | 195,220.00 USD | 195,220.00 USD | 49,670.00 USD | 14,050.00 USD | 22,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9720` | 294,590.00 USD | 294,590.00 USD | 53,850.00 USD | 0.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9740` | 109,310.00 USD | 109,310.00 USD | 9,580.00 USD | 12,820.00 USD | 14,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9740` | 231,130.00 USD | 231,130.00 USD | 0.00 USD | 16,590.00 USD | 8,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9760` | 72,670.00 USD | 72,670.00 USD | 19,600.00 USD | 13,960.00 USD | 8,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9760` | 205,910.00 USD | 205,910.00 USD | 15,320.00 USD | 5,480.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9780` | 31,040.00 USD | 31,040.00 USD | 23,150.00 USD | 0.00 USD | 7,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9780` | 175,830.00 USD | 175,830.00 USD | 0.00 USD | 0.00 USD | 24,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 12,020.00 USD | 12,020.00 USD | 156.00 USD | 0.00 USD | 11,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 24,040.00 USD | 24,040.00 USD | 156.00 USD | 0.00 USD | 11,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9800` | 151,540.00 USD | 151,540.00 USD | 0.00 USD | 0.00 USD | 151,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 59,050.00 USD | 59,050.00 USD | 15,980.00 USD | 12,160.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9820` | 82,360.00 USD | 82,360.00 USD | 10,090.00 USD | 0.00 USD | 72,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 80,250.00 USD | 80,250.00 USD | 0.00 USD | 0.00 USD | 21,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9840` | 103,280.00 USD | 103,280.00 USD | 0.00 USD | 0.00 USD | 20,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 81,980.00 USD | 81,980.00 USD | 575.70 USD | 0.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9860` | 104,090.00 USD | 104,090.00 USD | 0.00 USD | 0.00 USD | 803.95 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9880` | 82,520.00 USD | 82,520.00 USD | 0.00 USD | 0.00 USD | 531.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9880` | 145,010.00 USD | 145,010.00 USD | 40,020.00 USD | 0.00 USD | 901.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 146,330.00 USD | 146,330.00 USD | 50,430.00 USD | 0.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9900` | 145,910.00 USD | 145,910.00 USD | 0.00 USD | 0.00 USD | 906.61 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 159,210.00 USD | 159,210.00 USD | 0.00 USD | 0.00 USD | 12,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9920` | 166,350.00 USD | 166,350.00 USD | 0.00 USD | 0.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 179,380.00 USD | 179,380.00 USD | 6,920.00 USD | 13,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 182,010.00 USD | 182,010.00 USD | 0.00 USD | 2,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9960` | 241,800.00 USD | 241,800.00 USD | 32,670.00 USD | 0.00 USD | 42,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 209,940.00 USD | 209,940.00 USD | 26,250.00 USD | 0.00 USD | 1,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9980` | 298,250.00 USD | 298,250.00 USD | 52,700.00 USD | 0.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 291,830.00 USD | 291,830.00 USD | 50,740.00 USD | 29,610.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 351,100.00 USD | 351,100.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 292,030.00 USD | 292,030.00 USD | 0.00 USD | 0.00 USD | 192.37 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 394,670.00 USD | 394,670.00 USD | 28,410.00 USD | 13,940.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 310,330.00 USD | 310,330.00 USD | 10,110.00 USD | 5,360.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 419,740.00 USD | 419,740.00 USD | 25,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 378,960.00 USD | 378,960.00 USD | 44,970.00 USD | 5,090.00 USD | 18,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 453,840.00 USD | 453,840.00 USD | 34,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 397,810.00 USD | 397,810.00 USD | 0.00 USD | 4,400.00 USD | 14,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 470,090.00 USD | 470,090.00 USD | 0.00 USD | 0.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 413,000.00 USD | 413,000.00 USD | 7,050.00 USD | 8,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 484,110.00 USD | 484,110.00 USD | 0.00 USD | 14,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 454,530.00 USD | 454,530.00 USD | 16,070.00 USD | 25,300.00 USD | 155.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 543,640.00 USD | 543,640.00 USD | 33,230.00 USD | 26,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 489,530.00 USD | 489,530.00 USD | 5,630.00 USD | 4,350.00 USD | 25,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 575,050.00 USD | 575,050.00 USD | 2,870.00 USD | 28,140.00 USD | 388.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 529,750.00 USD | 529,750.00 USD | 20,120.00 USD | 21.80 USD | 20,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 615,200.00 USD | 615,200.00 USD | 0.00 USD | 28,470.00 USD | 11,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 757.09 USD | 1,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.02` | 567,180.00 USD | 567,180.00 USD | 5,990.00 USD | 8,490.00 USD | 22,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 657,170.00 USD | 657,170.00 USD | 0.00 USD | 20,410.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 630,450.00 USD | 630,450.00 USD | 44,710.00 USD | 3,450.00 USD | 15,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 782,650.00 USD | 782,650.00 USD | 0.00 USD | 81,220.00 USD | 44,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 706,920.00 USD | 706,920.00 USD | 51,380.00 USD | 3,670.00 USD | 21,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 1,000,000.00 USD | 1,000,000.00 USD | 56,930.00 USD | 52,290.00 USD | 111,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 819,270.00 USD | 819,270.00 USD | 34,630.00 USD | 24,720.00 USD | 53,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 1,200,000.00 USD | 1,200,000.00 USD | 52,560.00 USD | 56,700.00 USD | 86,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 907,230.00 USD | 907,230.00 USD | 52,170.00 USD | 17,130.00 USD | 18,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,370,000.00 USD | 1,370,000.00 USD | 22,650.00 USD | 124,760.00 USD | 25,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 967,860.00 USD | 967,860.00 USD | 31,210.00 USD | 10,940.00 USD | 18,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,700,000.00 USD | 1,700,000.00 USD | 250,040.00 USD | 50,530.00 USD | 24,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,120,000.00 USD | 1,120,000.00 USD | 95,190.00 USD | 24,470.00 USD | 33,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,880,000.00 USD | 1,880,000.00 USD | 134,200.00 USD | 29,810.00 USD | 19,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,240,000.00 USD | 1,240,000.00 USD | 69,660.00 USD | 8,960.00 USD | 35,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,990,000.00 USD | 1,990,000.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,300,000.00 USD | 1,300,000.00 USD | 38,050.00 USD | 9,250.00 USD | 21,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,220,000.00 USD | 2,220,000.00 USD | 216,820.00 USD | 8,290.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,370,000.00 USD | 1,370,000.00 USD | 18,100.00 USD | 13,840.00 USD | 33,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 2,530,000.00 USD | 2,530,000.00 USD | 262,550.00 USD | 3,170.00 USD | 42,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,460,000.00 USD | 1,460,000.00 USD | 62,580.00 USD | 3,190.00 USD | 24,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 2,900,000.00 USD | 2,900,000.00 USD | 178,400.00 USD | 1,290.00 USD | 199,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,490,000.00 USD | 1,490,000.00 USD | 7,710.00 USD | 8,100.00 USD | 15,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,290,000.00 USD | 3,290,000.00 USD | 279,460.00 USD | 9,430.00 USD | 93,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,520,000.00 USD | 1,520,000.00 USD | 11,290.00 USD | 9,870.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,610,000.00 USD | 3,610,000.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,580,000.00 USD | 1,580,000.00 USD | 7,410.00 USD | 14,400.00 USD | 36,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,870,000.00 USD | 3,870,000.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,600,000.00 USD | 1,600,000.00 USD | 21,630.00 USD | 4,160.00 USD | 321.14 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,290,000.00 USD | 4,290,000.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 733.98 USD | 1,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,630,000.00 USD | 1,630,000.00 USD | 15,080.00 USD | 3,210.00 USD | 4,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,680,000.00 USD | 4,680,000.00 USD | 199,320.00 USD | 28,070.00 USD | 161,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,700,000.00 USD | 1,700,000.00 USD | 43,610.00 USD | 11,120.00 USD | 19,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,840,000.00 USD | 4,840,000.00 USD | 91,750.00 USD | 29,070.00 USD | 40,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,760,000.00 USD | 1,760,000.00 USD | 23,230.00 USD | 7,030.00 USD | 31,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 5,160,000.00 USD | 5,160,000.00 USD | 140,970.00 USD | 49,780.00 USD | 133,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,780,000.00 USD | 1,780,000.00 USD | 8,900.00 USD | 340.84 USD | 6,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 5,320,000.00 USD | 5,320,000.00 USD | 82,020.00 USD | 42,140.00 USD | 36,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.06` | 74,410.00 USD | 76,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,810,000.00 USD | 1,810,000.00 USD | 7,850.00 USD | 1,750.00 USD | 25,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 5,680,000.00 USD | 5,680,000.00 USD | 187,610.00 USD | 48,000.00 USD | 121,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,860,000.00 USD | 1,860,000.00 USD | 29,640.00 USD | 3,000.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,050,000.00 USD | 6,050,000.00 USD | 205,690.00 USD | 63,110.00 USD | 94,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,880,000.00 USD | 1,880,000.00 USD | 3,760.00 USD | 3,710.00 USD | 10,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,430,000.00 USD | 6,430,000.00 USD | 197,680.00 USD | 69,880.00 USD | 118,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,890,000.00 USD | 1,890,000.00 USD | 1,990.00 USD | 7,750.00 USD | 2,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,710,000.00 USD | 6,710,000.00 USD | 131,720.00 USD | 83,000.00 USD | 65,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,910,000.00 USD | 1,910,000.00 USD | 5,090.00 USD | 2,370.00 USD | 7,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,960,000.00 USD | 6,960,000.00 USD | 102,750.00 USD | 49,310.00 USD | 92,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,930,000.00 USD | 1,930,000.00 USD | 12,510.00 USD | 2,930.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,130,000.00 USD | 7,130,000.00 USD | 77,660.00 USD | 32,860.00 USD | 61,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,950,000.00 USD | 1,950,000.00 USD | 10,720.00 USD | 4,390.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,470,000.00 USD | 7,470,000.00 USD | 221,410.00 USD | 30,180.00 USD | 93,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,970,000.00 USD | 1,970,000.00 USD | 9,230.00 USD | 5,040.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,670,000.00 USD | 7,670,000.00 USD | 121,300.00 USD | 33,170.00 USD | 42,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,990,000.00 USD | 1,990,000.00 USD | 9,330.00 USD | 5,210.00 USD | 11,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,900,000.00 USD | 7,900,000.00 USD | 103,500.00 USD | 37,730.00 USD | 83,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 2,010,000.00 USD | 2,010,000.00 USD | 7,810.00 USD | 4,630.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 8,100,000.00 USD | 8,100,000.00 USD | 102,600.00 USD | 21,500.00 USD | 83,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,040,000.00 USD | 2,040,000.00 USD | 6,260.00 USD | 5,330.00 USD | 12,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,250,000.00 USD | 8,250,000.00 USD | 103,110.00 USD | 18,720.00 USD | 27,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,050,000.00 USD | 2,050,000.00 USD | 9,360.00 USD | 4,070.00 USD | 150.13 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,520,000.00 USD | 8,520,000.00 USD | 158,650.00 USD | 40,740.00 USD | 69,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,060,000.00 USD | 2,060,000.00 USD | 8,360.00 USD | 1,870.00 USD | 711.93 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,760,000.00 USD | 8,760,000.00 USD | 176,790.00 USD | 26,190.00 USD | 33,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,070,000.00 USD | 2,070,000.00 USD | 5,240.00 USD | 3,920.00 USD | 4,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,880,000.00 USD | 8,880,000.00 USD | 62,710.00 USD | 20,510.00 USD | 38,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,080,000.00 USD | 2,080,000.00 USD | 3,940.00 USD | 1,660.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 9,060,000.00 USD | 9,060,000.00 USD | 46,000.00 USD | 31,940.00 USD | 103,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,100,000.00 USD | 2,100,000.00 USD | 9,560.00 USD | 2,760.00 USD | 6,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,260,000.00 USD | 9,260,000.00 USD | 134,170.00 USD | 28,200.00 USD | 34,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,120,000.00 USD | 2,120,000.00 USD | 3,630.00 USD | 4,390.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,490,000.00 USD | 9,490,000.00 USD | 59,850.00 USD | 54,400.00 USD | 117,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,130,000.00 USD | 2,130,000.00 USD | 5,800.00 USD | 3,270.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,650,000.00 USD | 9,650,000.00 USD | 109,670.00 USD | 18,350.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,130,000.00 USD | 2,130,000.00 USD | 4,370.00 USD | 149.76 USD | 966.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,780,000.00 USD | 9,780,000.00 USD | 39,750.00 USD | 24,570.00 USD | 62,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,140,000.00 USD | 2,140,000.00 USD | 687.18 USD | 2,490.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,940,000.00 USD | 9,940,000.00 USD | 66,620.00 USD | 37,290.00 USD | 55,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 2,140,000.00 USD | 2,140,000.00 USD | 1,740.00 USD | 3,660.00 USD | 82.24 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,100,000.00 USD | 10,100,000.00 USD | 71,580.00 USD | 30,090.00 USD | 65,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 2,150,000.00 USD | 2,150,000.00 USD | 4,120.00 USD | 11.15 USD | 992.14 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,350,000.00 USD | 10,350,000.00 USD | 114,820.00 USD | 34,430.00 USD | 97,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 2,150,000.00 USD | 2,150,000.00 USD | 1,940.00 USD | 798.95 USD | 2,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,650,000.00 USD | 10,650,000.00 USD | 182,190.00 USD | 62,900.00 USD | 52,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 2,160,000.00 USD | 2,160,000.00 USD | 2,330.00 USD | 3,250.00 USD | 2,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,870,000.00 USD | 10,870,000.00 USD | 118,210.00 USD | 18,440.00 USD | 88,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 2,170,000.00 USD | 2,170,000.00 USD | 2,770.00 USD | 2,620.00 USD | 5,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 11,020,000.00 USD | 11,020,000.00 USD | 65,300.00 USD | 22,070.00 USD | 57,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.11` | 2,170,000.00 USD | 2,170,000.00 USD | 1,590.00 USD | 50.69 USD | 111.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 11,060,000.00 USD | 11,060,000.00 USD | 22,290.00 USD | 5,830.00 USD | 12,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.11` | 2,180,000.00 USD | 2,180,000.00 USD | 2,660.00 USD | 1,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 11,240,000.00 USD | 11,240,000.00 USD | 90,280.00 USD | 31,510.00 USD | 54,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.11` | 169.86 USD | 76,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.11` | 11,400,000.00 USD | 11,400,000.00 USD | 33,280.00 USD | 36,570.00 USD | 93,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 11,510,000.00 USD | 11,510,000.00 USD | 64,670.00 USD | 26,930.00 USD | 24,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 11,590,000.00 USD | 11,590,000.00 USD | 32,450.00 USD | 36,820.00 USD | 6,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 11,700,000.00 USD | 11,700,000.00 USD | 59,080.00 USD | 33,150.00 USD | 13,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 11,780,000.00 USD | 11,780,000.00 USD | 37,220.00 USD | 17,240.00 USD | 30,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 11,880,000.00 USD | 11,880,000.00 USD | 32,060.00 USD | 41,540.00 USD | 25,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 11,960,000.00 USD | 11,960,000.00 USD | 52,230.00 USD | 16,980.00 USD | 11,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 12,050,000.00 USD | 12,050,000.00 USD | 58,100.00 USD | 5,280.00 USD | 29,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 12,100,000.00 USD | 12,100,000.00 USD | 16,200.00 USD | 5,970.00 USD | 28,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 12,150,000.00 USD | 12,150,000.00 USD | 2,210.00 USD | 13,650.00 USD | 28,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 12,300,000.00 USD | 12,300,000.00 USD | 95,910.00 USD | 18,230.00 USD | 42,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 12,440,000.00 USD | 12,440,000.00 USD | 71,210.00 USD | 0.00 USD | 65,880.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.2385` | 539,580.00 USD | 0.00 USD | 119.25 USD | `-75.77%` | `500.00` |
| `Live` | `Long` | `0.3375` | 539,460.00 USD | 0.00 USD | 745.54 USD | `-65.72%` | `2,209.00` |
| `Live` | `Long` | `0.3605` | 538,720.00 USD | 0.00 USD | 650.95 USD | `-63.38%` | `1,805.70` |
| `Live` | `Long` | `0.3735` | 538,070.00 USD | 0.00 USD | 2,130.00 USD | `-62.06%` | `5,698.80` |
| `Live` | `Long` | `0.4185` | 535,940.00 USD | 0.00 USD | 2,790.00 USD | `-57.49%` | `6,675.20` |
| `Live` | `Long` | `0.4315` | 533,150.00 USD | 0.00 USD | 171.09 USD | `-56.17%` | `396.50` |
| `Live` | `Long` | `0.4335` | 532,980.00 USD | 0.00 USD | 138.42 USD | `-55.96%` | `319.30` |
| `Live` | `Long` | `0.4695` | 532,840.00 USD | 0.00 USD | 2,580.00 USD | `-52.31%` | `5,500.00` |
| `Live` | `Long` | `0.5115` | 530,250.00 USD | 0.00 USD | 811.34 USD | `-48.04%` | `1,586.20` |
| `Live` | `Long` | `0.5125` | 529,440.00 USD | 0.00 USD | 4,130.00 USD | `-47.94%` | `8,067.10` |
| `Live` | `Long` | `0.5165` | 525,310.00 USD | 0.00 USD | 1,020.00 USD | `-47.53%` | `1,979.90` |
| `Live` | `Long` | `0.5465` | 524,290.00 USD | 0.00 USD | 106.84 USD | `-44.49%` | `195.50` |
| `Live` | `Long` | `0.5575` | 524,180.00 USD | 0.00 USD | 13,600.00 USD | `-43.37%` | `24,390.20` |
| `Live` | `Long` | `0.5695` | 510,580.00 USD | 0.00 USD | 577.36 USD | `-42.15%` | `1,013.80` |
| `Live` | `Long` | `0.5895` | 510,000.00 USD | 0.00 USD | 137.53 USD | `-40.12%` | `233.30` |
| `Live` | `Long` | `0.5955` | 509,870.00 USD | 0.00 USD | 3,390.00 USD | `-39.51%` | `5,695.60` |
| `Live` | `Long` | `0.6055` | 506,480.00 USD | 0.00 USD | 1,480.00 USD | `-38.49%` | `2,448.50` |
| `Live` | `Long` | `0.6065` | 504,990.00 USD | 0.00 USD | 1,800.00 USD | `-38.39%` | `2,971.80` |
| `Live` | `Long` | `0.6125` | 503,190.00 USD | 0.00 USD | 105.96 USD | `-37.78%` | `173.00` |
| `Live` | `Long` | `0.6145` | 503,080.00 USD | 0.00 USD | 147.48 USD | `-37.58%` | `240.00` |
| `Live` | `Long` | `0.6245` | 502,940.00 USD | 0.00 USD | 525.77 USD | `-36.56%` | `841.90` |
| `Live` | `Long` | `0.6315` | 502,410.00 USD | 0.00 USD | 757.80 USD | `-35.85%` | `1,200.00` |
| `Live` | `Long` | `0.6355` | 501,650.00 USD | 0.00 USD | 106.00 USD | `-35.45%` | `166.80` |
| `Live` | `Long` | `0.6385` | 501,550.00 USD | 0.00 USD | 156.18 USD | `-35.14%` | `244.60` |
| `Live` | `Long` | `0.6415` | 501,390.00 USD | 0.00 USD | 20,270.00 USD | `-34.84%` | `31,595.60` |
| `Live` | `Long` | `0.6465` | 481,120.00 USD | 0.00 USD | 4,230.00 USD | `-34.33%` | `6,539.70` |
| `Live` | `Long` | `0.6475` | 476,890.00 USD | 0.00 USD | 202.47 USD | `-34.23%` | `312.70` |
| `Live` | `Long` | `0.6595` | 476,690.00 USD | 0.00 USD | 149.44 USD | `-33.01%` | `226.60` |
| `Live` | `Long` | `0.6725` | 476,540.00 USD | 0.00 USD | 63,890.00 USD | `-31.69%` | `95,000.00` |
| `Live` | `Long` | `0.6775` | 412,660.00 USD | 0.00 USD | 423.10 USD | `-31.18%` | `624.50` |
| `Live` | `Long` | `0.6835` | 412,230.00 USD | 0.00 USD | 512.97 USD | `-30.57%` | `750.50` |
| `Live` | `Long` | `0.6855` | 411,720.00 USD | 0.00 USD | 2,110.00 USD | `-30.37%` | `3,075.70` |
| `Live` | `Long` | `0.6955` | 409,610.00 USD | 0.00 USD | 322.16 USD | `-29.35%` | `463.20` |
| `Live` | `Long` | `0.7045` | 409,290.00 USD | 0.00 USD | 157.39 USD | `-28.44%` | `223.40` |
| `Live` | `Long` | `0.7055` | 409,130.00 USD | 0.00 USD | 881.88 USD | `-28.33%` | `1,250.00` |
| `Live` | `Long` | `0.7075` | 408,250.00 USD | 0.00 USD | 16,520.00 USD | `-28.13%` | `23,344.30` |
| `Live` | `Long` | `0.7145` | 391,730.00 USD | 0.00 USD | 988.87 USD | `-27.42%` | `1,384.00` |
| `Live` | `Long` | `0.7175` | 390,740.00 USD | 0.00 USD | 322.88 USD | `-27.12%` | `450.00` |
| `Live` | `Long` | `0.7205` | 390,420.00 USD | 0.00 USD | 866.26 USD | `-26.81%` | `1,202.30` |
| `Live` | `Long` | `0.7255` | 389,560.00 USD | 0.00 USD | 1,090.00 USD | `-26.30%` | `1,500.00` |
| `Live` | `Long` | `0.7275` | 388,470.00 USD | 0.00 USD | 126.44 USD | `-26.10%` | `173.80` |
| `Live` | `Long` | `0.7285` | 388,340.00 USD | 0.00 USD | 291.18 USD | `-26.00%` | `399.70` |
| `Live` | `Long` | `0.7305` | 388,050.00 USD | 0.00 USD | 2,300.00 USD | `-25.80%` | `3,143.00` |
| `Live` | `Long` | `0.7335` | 385,750.00 USD | 0.00 USD | 1,140.00 USD | `-25.49%` | `1,557.80` |
| `Live` | `Long` | `0.7365` | 384,610.00 USD | 0.00 USD | 2,050.00 USD | `-25.19%` | `2,785.30` |
| `Live` | `Long` | `0.7395` | 382,560.00 USD | 0.00 USD | 283.30 USD | `-24.88%` | `383.10` |
| `Live` | `Long` | `0.7495` | 382,280.00 USD | 0.00 USD | 1,390.00 USD | `-23.87%` | `1,859.90` |
| `Live` | `Long` | `0.7525` | 380,880.00 USD | 0.00 USD | 331.18 USD | `-23.56%` | `440.10` |
| `Live` | `Long` | `0.7555` | 380,550.00 USD | 0.00 USD | 2,390.00 USD | `-23.26%` | `3,161.00` |
| `Live` | `Long` | `0.7605` | 378,160.00 USD | 0.00 USD | 834.88 USD | `-22.75%` | `1,097.80` |
| `Live` | `Long` | `0.7655` | 377,330.00 USD | 0.00 USD | 2,300.00 USD | `-22.24%` | `3,003.90` |
| `Live` | `Long` | `0.7725` | 375,030.00 USD | 0.00 USD | 1,580.00 USD | `-21.53%` | `2,046.10` |
| `Live` | `Long` | `0.7865` | 373,450.00 USD | 0.00 USD | 292.03 USD | `-20.11%` | `371.30` |
| `Live` | `Long` | `0.7895` | 373,160.00 USD | 0.00 USD | 20,380.00 USD | `-19.80%` | `25,816.60` |
| `Live` | `Long` | `0.7965` | 352,770.00 USD | 0.00 USD | 106.49 USD | `-19.09%` | `133.70` |
| `Live` | `Long` | `0.8025` | 352,670.00 USD | 0.00 USD | 238.90 USD | `-18.48%` | `297.70` |
| `Live` | `Long` | `0.8045` | 352,430.00 USD | 0.00 USD | 566.61 USD | `-18.28%` | `704.30` |
| `Live` | `Long` | `0.8055` | 351,860.00 USD | 0.00 USD | 699.01 USD | `-18.18%` | `867.80` |
| `Live` | `Long` | `0.8135` | 351,160.00 USD | 0.00 USD | 647.79 USD | `-17.36%` | `796.30` |
| `Live` | `Long` | `0.8195` | 350,510.00 USD | 0.00 USD | 13,560.00 USD | `-16.75%` | `16,544.60` |
| `Live` | `Long` | `0.8215` | 336,960.00 USD | 0.00 USD | 1,950.00 USD | `-16.55%` | `2,370.70` |
| `Live` | `Long` | `0.8285` | 335,010.00 USD | 0.00 USD | 1,890.00 USD | `-15.84%` | `2,283.30` |
| `Live` | `Long` | `0.8325` | 333,120.00 USD | 0.00 USD | 8,990.00 USD | `-15.43%` | `10,795.60` |
| `Live` | `Long` | `0.8365` | 324,130.00 USD | 0.00 USD | 316.70 USD | `-15.03%` | `378.60` |
| `Live` | `Long` | `0.8375` | 323,810.00 USD | 0.00 USD | 167.00 USD | `-14.93%` | `199.40` |
| `Live` | `Long` | `0.8415` | 323,650.00 USD | 0.00 USD | 1,240.00 USD | `-14.52%` | `1,469.60` |
| `Live` | `Long` | `0.8445` | 322,410.00 USD | 0.00 USD | 168.31 USD | `-14.22%` | `199.30` |
| `Live` | `Long` | `0.8495` | 322,240.00 USD | 0.00 USD | 1,260.00 USD | `-13.71%` | `1,486.90` |
| `Live` | `Long` | `0.8575` | 320,980.00 USD | 0.00 USD | 620.32 USD | `-12.89%` | `723.40` |
| `Live` | `Long` | `0.8595` | 320,360.00 USD | 0.00 USD | 61,200.00 USD | `-12.69%` | `71,202.70` |
| `Live` | `Long` | `0.8625` | 259,160.00 USD | 0.00 USD | 309.55 USD | `-12.39%` | `358.90` |
| `Live` | `Long` | `0.8635` | 258,850.00 USD | 0.00 USD | 208.02 USD | `-12.29%` | `240.90` |
| `Live` | `Long` | `0.8645` | 258,640.00 USD | 0.00 USD | 438.30 USD | `-12.18%` | `507.00` |
| `Live` | `Long` | `0.8665` | 258,200.00 USD | 0.00 USD | 118.54 USD | `-11.98%` | `136.80` |
| `Live` | `Long` | `0.8765` | 258,080.00 USD | 0.00 USD | 171.88 USD | `-10.96%` | `196.10` |
| `Live` | `Long` | `0.8795` | 257,910.00 USD | 0.00 USD | 948.01 USD | `-10.66%` | `1,077.90` |
| `Live` | `Long` | `0.8925` | 256,960.00 USD | 0.00 USD | 526.84 USD | `-9.34%` | `590.30` |
| `Live` | `Long` | `0.8975` | 256,440.00 USD | 0.00 USD | 9,210.00 USD | `-8.83%` | `10,267.00` |
| `Live` | `Long` | `0.8995` | 247,220.00 USD | 0.00 USD | 3,820.00 USD | `-8.63%` | `4,250.30` |
| `Live` | `Long` | `0.9035` | 243,400.00 USD | 0.00 USD | 180.16 USD | `-8.22%` | `199.40` |
| `Live` | `Long` | `0.9095` | 243,220.00 USD | 0.00 USD | 951.34 USD | `-7.61%` | `1,046.00` |
| `Live` | `Long` | `0.9135` | 242,270.00 USD | 0.00 USD | 143.42 USD | `-7.21%` | `157.00` |
| `Live` | `Long` | `0.9185` | 242,130.00 USD | 0.00 USD | 145.86 USD | `-6.70%` | `158.80` |
| `Live` | `Long` | `0.9195` | 241,980.00 USD | 0.00 USD | 7,330.00 USD | `-6.60%` | `7,970.50` |
| `Live` | `Long` | `0.9225` | 234,650.00 USD | 0.00 USD | 8,360.00 USD | `-6.29%` | `9,060.10` |
| `Live` | `Long` | `0.9295` | 226,290.00 USD | 0.00 USD | 253.01 USD | `-5.58%` | `272.20` |
| `Live` | `Short` | `0.9325` | 324.42 USD | 324.42 USD | 0.00 USD | `-5.28%` | `347.90` |
| `Live` | `Long` | `0.9335` | 226,040.00 USD | 0.00 USD | 361.45 USD | `-5.17%` | `387.20` |
| `Live` | `Long` | `0.9365` | 225,680.00 USD | 0.00 USD | 6,560.00 USD | `-4.87%` | `7,000.00` |
| `Live` | `Long` | `0.9375` | 219,120.00 USD | 0.00 USD | 196.97 USD | `-4.77%` | `210.10` |
| `Live` | `Long` | `0.9405` | 218,930.00 USD | 0.00 USD | 141.83 USD | `-4.46%` | `150.80` |
| `Live` | `Long` | `0.9445` | 218,780.00 USD | 0.00 USD | 1,060.00 USD | `-4.06%` | `1,117.80` |
| `Live` | `Long` | `0.9455` | 217,730.00 USD | 0.00 USD | 106,880.00 USD | `-3.96%` | `113,040.20` |
| `Live` | `Long` | `0.9475` | 110,850.00 USD | 0.00 USD | 323.19 USD | `-3.75%` | `341.10` |
| `Live` | `Long` | `0.9495` | 110,530.00 USD | 0.00 USD | 105,430.00 USD | `-3.55%` | `111,034.60` |
| `Live` | `Long` | `0.9515` | 5,100.00 USD | 0.00 USD | 405.62 USD | `-3.35%` | `426.30` |
| `Live` | `Long` | `0.9555` | 4,690.00 USD | 0.00 USD | 3,160.00 USD | `-2.94%` | `3,305.70` |
| `Live` | `Long` | `0.9585` | 1,530.00 USD | 0.00 USD | 1,530.00 USD | `-2.64%` | `1,600.00` |
| `Live` | `Short` | `1.02` | 1,080.00 USD | 757.09 USD | 0.00 USD | `+3.26%` | `744.80` |
| `Live` | `Short` | `1.05` | 1,820.00 USD | 733.98 USD | 0.00 USD | `+6.41%` | `700.70` |
| `Live` | `Short` | `1.06` | 76,230.00 USD | 74,410.00 USD | 0.00 USD | `+7.22%` | `70,500.00` |
| `Live` | `Short` | `1.11` | 76,400.00 USD | 169.86 USD | 0.00 USD | `+12.70%` | `153.10` |
| `Live` | `Short` | `1.18` | 76,630.00 USD | 228.59 USD | 0.00 USD | `+19.51%` | `194.30` |
| `Live` | `Short` | `1.19` | 98,810.00 USD | 22,180.00 USD | 0.00 USD | `+20.73%` | `18,664.00` |
| `Live` | `Short` | `1.32` | 110,540.00 USD | 11,730.00 USD | 0.00 USD | `+34.44%` | `8,862.90` |
| `Live` | `Short` | `1.34` | 110,930.00 USD | 389.93 USD | 0.00 USD | `+36.07%` | `291.10` |
| `Live` | `Short` | `1.42` | 115,260.00 USD | 4,330.00 USD | 0.00 USD | `+44.19%` | `3,049.30` |
| `Live` | `Short` | `1.49` | 628,870.00 USD | 513,610.00 USD | 0.00 USD | `+51.20%` | `345,051.20` |
| `Live` | `Short` | `1.52` | 629,090.00 USD | 225.19 USD | 0.00 USD | `+54.35%` | `148.20` |
| `Live` | `Short` | `1.52` | 630,050.00 USD | 960.68 USD | 0.00 USD | `+54.55%` | `631.40` |
| `Live` | `Short` | `1.52` | 630,280.00 USD | 232.49 USD | 0.00 USD | `+54.86%` | `152.50` |
| `Live` | `Short` | `1.54` | 630,460.00 USD | 176.31 USD | 0.00 USD | `+56.69%` | `114.30` |
| `Live` | `Short` | `1.56` | 640,050.00 USD | 9,590.00 USD | 0.00 USD | `+58.11%` | `6,161.90` |
| `Live` | `Short` | `1.64` | 640,810.00 USD | 762.12 USD | 0.00 USD | `+66.85%` | `464.00` |
| `Live` | `Short` | `1.66` | 641,060.00 USD | 242.35 USD | 0.00 USD | `+68.27%` | `146.30` |
| `Live` | `Short` | `1.67` | 641,360.00 USD | 300.15 USD | 0.00 USD | `+69.39%` | `180.00` |
| `Live` | `Short` | `1.67` | 641,680.00 USD | 320.38 USD | 0.00 USD | `+69.59%` | `191.90` |
| `Live` | `Short` | `1.78` | 730,470.00 USD | 88,800.00 USD | 0.00 USD | `+81.27%` | `49,759.80` |
| `Live` | `Short` | `1.86` | 730,680.00 USD | 208.37 USD | 0.00 USD | `+88.48%` | `112.30` |
| `Live` | `Short` | `1.90` | 730,860.00 USD | 181.88 USD | 0.00 USD | `+93.05%` | `95.70` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.4015` | 454,290.00 USD | 0.00 USD | 120.45 USD | `-59.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 454,170.00 USD | 0.00 USD | 150.15 USD | `-49.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 454,020.00 USD | 0.00 USD | 781.90 USD | `-28.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 453,230.00 USD | 0.00 USD | 477.38 USD | `-27.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 452,760.00 USD | 0.00 USD | 341.33 USD | `-26.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 452,410.00 USD | 0.00 USD | 972.82 USD | `-26.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 451,440.00 USD | 0.00 USD | 160.20 USD | `-25.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 451,280.00 USD | 0.00 USD | 289.49 USD | `-24.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 450,990.00 USD | 0.00 USD | 14,570.00 USD | `-20.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 436,420.00 USD | 0.00 USD | 274,830.00 USD | `-19.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 161,590.00 USD | 0.00 USD | 405.75 USD | `-17.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 161,190.00 USD | 0.00 USD | 772.84 USD | `-15.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8495` | 160,410.00 USD | 0.00 USD | 3,470.00 USD | `-13.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 156,940.00 USD | 0.00 USD | 9,180.00 USD | `-13.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 147,760.00 USD | 0.00 USD | 341.94 USD | `-13.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 147,420.00 USD | 0.00 USD | 1,150.00 USD | `-13.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 146,270.00 USD | 0.00 USD | 2,020.00 USD | `-12.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 144,260.00 USD | 0.00 USD | 429.25 USD | `-12.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 143,830.00 USD | 0.00 USD | 1,290.00 USD | `-12.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 142,540.00 USD | 0.00 USD | 518.51 USD | `-11.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 142,020.00 USD | 0.00 USD | 223.04 USD | `-9.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 141,800.00 USD | 0.00 USD | 401.86 USD | `-9.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 141,390.00 USD | 0.00 USD | 158.51 USD | `-9.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 141,240.00 USD | 0.00 USD | 498.10 USD | `-9.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 140,740.00 USD | 0.00 USD | 363.40 USD | `-7.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 140,370.00 USD | 0.00 USD | 913.41 USD | `-6.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9255` | 139,460.00 USD | 0.00 USD | 1,010.00 USD | `-5.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9275` | 138,450.00 USD | 0.00 USD | 2,120.00 USD | `-5.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9285` | 136,330.00 USD | 0.00 USD | 246.05 USD | `-5.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9295` | 136,080.00 USD | 0.00 USD | 776.50 USD | `-5.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9365` | 135,310.00 USD | 0.00 USD | 9,680.00 USD | `-4.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9405` | 125,620.00 USD | 0.00 USD | 555.18 USD | `-4.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9425` | 125,070.00 USD | 0.00 USD | 145.43 USD | `-4.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9445` | 124,920.00 USD | 0.00 USD | 1,730.00 USD | `-4.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9485` | 123,200.00 USD | 0.00 USD | 634.74 USD | `-3.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9525` | 122,560.00 USD | 0.00 USD | 381.00 USD | `-3.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9555` | 122,180.00 USD | 0.00 USD | 3,900.00 USD | `-2.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9565` | 118,280.00 USD | 0.00 USD | 674.91 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9575` | 117,610.00 USD | 0.00 USD | 166.41 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9605` | 117,440.00 USD | 0.00 USD | 376.80 USD | `-2.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9615` | 117,070.00 USD | 0.00 USD | 152.11 USD | `-2.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9625` | 116,910.00 USD | 0.00 USD | 1,910.00 USD | `-2.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9635` | 115,010.00 USD | 0.00 USD | 568.75 USD | `-2.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9645` | 114,440.00 USD | 0.00 USD | 163.29 USD | `-2.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9665` | 114,280.00 USD | 0.00 USD | 554.58 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9675` | 113,720.00 USD | 0.00 USD | 385.74 USD | `-1.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9685` | 113,330.00 USD | 0.00 USD | 153.22 USD | `-1.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9695` | 113,180.00 USD | 0.00 USD | 22,800.00 USD | `-1.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9705` | 90,380.00 USD | 0.00 USD | 11,230.00 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9715` | 79,150.00 USD | 0.00 USD | 10,370.00 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9725` | 68,780.00 USD | 0.00 USD | 387.83 USD | `-1.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9735` | 68,400.00 USD | 0.00 USD | 7,630.00 USD | `-1.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9745` | 60,760.00 USD | 0.00 USD | 8,750.00 USD | `-1.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9755` | 52,020.00 USD | 0.00 USD | 21,960.00 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9765` | 30,050.00 USD | 0.00 USD | 9,500.00 USD | `-0.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9775` | 20,550.00 USD | 0.00 USD | 676.53 USD | `-0.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9785` | 19,880.00 USD | 0.00 USD | 11,400.00 USD | `-0.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9795` | 8,480.00 USD | 0.00 USD | 123.61 USD | `-0.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9805` | 8,350.00 USD | 0.00 USD | 8,350.00 USD | `-0.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 22,170.00 USD | 22,170.00 USD | 0.00 USD | `+0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 37,240.00 USD | 15,070.00 USD | 0.00 USD | `+0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9865` | 70,030.00 USD | 32,800.00 USD | 0.00 USD | `+0.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9895` | 105,010.00 USD | 34,970.00 USD | 0.00 USD | `+0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 108,520.00 USD | 3,520.00 USD | 0.00 USD | `+0.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 140,280.00 USD | 31,750.00 USD | 0.00 USD | `+0.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 141,600.00 USD | 1,320.00 USD | 0.00 USD | `+0.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 142,380.00 USD | 782.07 USD | 0.00 USD | `+1.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 142,790.00 USD | 403.28 USD | 0.00 USD | `+1.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 146,190.00 USD | 3,400.00 USD | 0.00 USD | `+1.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 151,330.00 USD | 5,140.00 USD | 0.00 USD | `+1.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 188,640.00 USD | 37,310.00 USD | 0.00 USD | `+1.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 189,640.00 USD | 1,000.00 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 230,240.00 USD | 40,590.00 USD | 0.00 USD | `+1.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 230,470.00 USD | 235.79 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 231,810.00 USD | 1,340.00 USD | 0.00 USD | `+1.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 232,040.00 USD | 230.39 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 233,050.00 USD | 1,000.00 USD | 0.00 USD | `+2.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 233,240.00 USD | 198.46 USD | 0.00 USD | `+2.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 233,860.00 USD | 615.60 USD | 0.00 USD | `+2.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 237,320.00 USD | 3,460.00 USD | 0.00 USD | `+2.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 239,430.00 USD | 2,110.00 USD | 0.00 USD | `+3.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 239,990.00 USD | 561.17 USD | 0.00 USD | `+3.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 240,100.00 USD | 103.07 USD | 0.00 USD | `+3.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 240,500.00 USD | 401.26 USD | 0.00 USD | `+3.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 240,780.00 USD | 286.22 USD | 0.00 USD | `+3.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 241,590.00 USD | 804.09 USD | 0.00 USD | `+3.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 241,790.00 USD | 201.52 USD | 0.00 USD | `+4.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 241,990.00 USD | 201.92 USD | 0.00 USD | `+4.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 242,190.00 USD | 201.60 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 242,290.00 USD | 101.51 USD | 0.00 USD | `+4.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 242,500.00 USD | 202.90 USD | 0.00 USD | `+4.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 243,010.00 USD | 516.75 USD | 0.00 USD | `+4.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 243,220.00 USD | 204.93 USD | 0.00 USD | `+5.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 243,570.00 USD | 348.86 USD | 0.00 USD | `+5.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 243,980.00 USD | 413.76 USD | 0.00 USD | `+5.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 244,340.00 USD | 354.91 USD | 0.00 USD | `+5.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 246,240.00 USD | 1,900.00 USD | 0.00 USD | `+5.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 246,450.00 USD | 207.87 USD | 0.00 USD | `+5.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 246,660.00 USD | 207.97 USD | 0.00 USD | `+6.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 257,960.00 USD | 11,310.00 USD | 0.00 USD | `+6.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 259,260.00 USD | 1,290.00 USD | 0.00 USD | `+6.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 259,460.00 USD | 206.97 USD | 0.00 USD | `+6.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 259,570.00 USD | 107.99 USD | 0.00 USD | `+6.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 259,820.00 USD | 247.60 USD | 0.00 USD | `+7.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 334,660.00 USD | 74,840.00 USD | 0.00 USD | `+7.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 335,200.00 USD | 544.88 USD | 0.00 USD | `+8.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 335,360.00 USD | 157.10 USD | 0.00 USD | `+9.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 337,530.00 USD | 2,170.00 USD | 0.00 USD | `+10.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 339,070.00 USD | 1,540.00 USD | 0.00 USD | `+10.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 348,990.00 USD | 9,930.00 USD | 0.00 USD | `+11.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 349,970.00 USD | 976.36 USD | 0.00 USD | `+11.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 351,180.00 USD | 1,210.00 USD | 0.00 USD | `+12.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 352,060.00 USD | 877.63 USD | 0.00 USD | `+12.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 352,230.00 USD | 171.50 USD | 0.00 USD | `+12.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 352,400.00 USD | 171.09 USD | 0.00 USD | `+13.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 355,170.00 USD | 2,770.00 USD | 0.00 USD | `+14.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 357,210.00 USD | 2,040.00 USD | 0.00 USD | `+14.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 357,460.00 USD | 249.83 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 360,130.00 USD | 2,670.00 USD | 0.00 USD | `+15.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 360,280.00 USD | 151.16 USD | 0.00 USD | `+16.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 360,430.00 USD | 151.29 USD | 0.00 USD | `+16.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 360,580.00 USD | 151.42 USD | 0.00 USD | `+16.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 360,730.00 USD | 151.55 USD | 0.00 USD | `+17.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 360,880.00 USD | 151.69 USD | 0.00 USD | `+17.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 361,870.00 USD | 986.35 USD | 0.00 USD | `+17.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 363,920.00 USD | 2,050.00 USD | 0.00 USD | `+18.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 364,030.00 USD | 110.00 USD | 0.00 USD | `+19.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 364,270.00 USD | 237.90 USD | 0.00 USD | `+20.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 365,470.00 USD | 1,210.00 USD | 0.00 USD | `+21.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 408,400.00 USD | 42,930.00 USD | 0.00 USD | `+22.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 410,400.00 USD | 2,000.00 USD | 0.00 USD | `+25.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 411,790.00 USD | 1,380.00 USD | 0.00 USD | `+27.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 412,030.00 USD | 245.41 USD | 0.00 USD | `+29.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 419,380.00 USD | 7,350.00 USD | 0.00 USD | `+31.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 419,800.00 USD | 415.25 USD | 0.00 USD | `+32.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 426,320.00 USD | 6,520.00 USD | 0.00 USD | `+32.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 883,300.00 USD | 456,990.00 USD | 0.00 USD | `+33.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 883,960.00 USD | 655.75 USD | 0.00 USD | `+33.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 885,770.00 USD | 1,810.00 USD | 0.00 USD | `+36.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 899,660.00 USD | 13,880.00 USD | 0.00 USD | `+36.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 900,910.00 USD | 1,250.00 USD | 0.00 USD | `+37.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 902,980.00 USD | 2,070.00 USD | 0.00 USD | `+41.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 903,120.00 USD | 140.05 USD | 0.00 USD | `+42.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 903,280.00 USD | 160.42 USD | 0.00 USD | `+42.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 903,880.00 USD | 598.33 USD | 0.00 USD | `+43.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 938,050.00 USD | 34,170.00 USD | 0.00 USD | `+45.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 938,930.00 USD | 879.84 USD | 0.00 USD | `+51.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 939,520.00 USD | 590.88 USD | 0.00 USD | `+52.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 942,570.00 USD | 3,050.00 USD | 0.00 USD | `+53.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 942,870.00 USD | 297.27 USD | 0.00 USD | `+57.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 951,400.00 USD | 8,530.00 USD | 0.00 USD | `+67.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 951,550.00 USD | 143.99 USD | 0.00 USD | `+69.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 951,720.00 USD | 177.05 USD | 0.00 USD | `+79.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 952,150.00 USD | 431.40 USD | 0.00 USD | `+82.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 957,260.00 USD | 5,100.00 USD | 0.00 USD | `+93.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 959,740.00 USD | 2,480.00 USD | 0.00 USD | `+94.07%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.8760` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 6,030.00 USD | 6,200.00 USD | 5,860.00 USD |
| `1D` | `0.8780` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 19,130.00 USD | 7,220.00 USD | 10,930.00 USD |
| `7D` | `0.8780` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 15,500.00 USD | 50.60 USD | 5,490.00 USD |
| `1D` | `0.8800` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 4,390.00 USD | 5,110.00 USD | 5,410.00 USD |
| `7D` | `0.8800` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 0.00 USD | 3,930.00 USD | 0.00 USD |
| `1D` | `0.8820` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 8,280.00 USD | 3,980.00 USD | 150.13 USD |
| `7D` | `0.8820` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 8,660.00 USD | 3,420.00 USD | 0.00 USD |
| `1D` | `0.8840` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 7,440.00 USD | 1,810.00 USD | 711.93 USD |
| `7D` | `0.8840` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 4,540.00 USD | 5,480.00 USD | 1,300.00 USD |
| `1D` | `0.8860` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 4,980.00 USD | 1,690.00 USD | 4,120.00 USD |
| `7D` | `0.8860` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 15,460.00 USD | 7,970.00 USD | 2,410.00 USD |
| `1D` | `0.8880` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 12,080.00 USD | 3,880.00 USD | 9,140.00 USD |
| `7D` | `0.8880` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 7,150.00 USD | 1,990.00 USD | 11,620.00 USD |
| `1D` | `0.8900` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 3,630.00 USD | 4,230.00 USD | 4,990.00 USD |
| `7D` | `0.8900` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 23,060.00 USD | 6,420.00 USD | 20,580.00 USD |
| `1D` | `0.8920` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 4,920.00 USD | 3,160.00 USD | 1,950.00 USD |
| `7D` | `0.8920` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 45,890.00 USD | 9,570.00 USD | 15,680.00 USD |
| `1D` | `0.8940` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 4,240.00 USD | 23.75 USD | 966.50 USD |
| `7D` | `0.8940` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 7,120.00 USD | 8,030.00 USD | 26,540.00 USD |
| `1D` | `0.8960` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 1,740.00 USD | 6,100.00 USD | 2,140.00 USD |
| `7D` | `0.8960` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 30,390.00 USD | 9,210.00 USD | 12,150.00 USD |
| `1D` | `0.8980` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 5,420.00 USD | 65.95 USD | 992.14 USD |
| `7D` | `0.8980` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 31,140.00 USD | 6,910.00 USD | 36,260.00 USD |
| `1D` | `0.9000` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 3,760.00 USD | 759.75 USD | 2,390.00 USD |
| `7D` | `0.9000` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 39,940.00 USD | 14,050.00 USD | 14,850.00 USD |
| `1D` | `0.9020` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 4,180.00 USD | 3,230.00 USD | 2,320.00 USD |
| `7D` | `0.9020` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 16,980.00 USD | 11,760.00 USD | 15,220.00 USD |
| `1D` | `0.9040` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 3,130.00 USD | 2,520.00 USD | 5,730.00 USD |
| `7D` | `0.9040` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 17,160.00 USD | 5,930.00 USD | 11,110.00 USD |
| `1D` | `0.9060` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 9,620.00 USD | 1,660.00 USD | 111.00 USD |
| `7D` | `0.9060` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 53,450.00 USD | 30,600.00 USD | 41,510.00 USD |
| `1D` | `0.9080` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 5,800.00 USD | 3,150.00 USD | 3,500.00 USD |
| `7D` | `0.9080` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 21,830.00 USD | 3,470.00 USD | 6,850.00 USD |
| `1D` | `0.9100` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 21,840.00 USD | 2,070.00 USD | 5,600.00 USD |
| `7D` | `0.9100` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 6,870.00 USD | 10,340.00 USD | 17,140.00 USD |
| `1D` | `0.9120` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 4,140.00 USD | 274.81 USD | 3,690.00 USD |
| `7D` | `0.9120` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 21,820.00 USD | 4,010.00 USD | 371.71 USD |
| `1D` | `0.9140` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 5,980.00 USD | 1,290.00 USD | 4,460.00 USD |
| `7D` | `0.9140` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 46,660.00 USD | 8,800.00 USD | 26,510.00 USD |
| `1D` | `0.9160` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 14,110.00 USD | 100.68 USD | 3,990.00 USD |
| `7D` | `0.9160` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 12,570.00 USD | 12,620.00 USD | 17,320.00 USD |
| `1D` | `0.9180` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 49.41 USD | 452.74 USD | 583.97 USD |
| `7D` | `0.9180` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 29,970.00 USD | 9,070.00 USD | 13,780.00 USD |
| `1D` | `0.9200` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 2,990.00 USD | 112.72 USD | 192.17 USD |
| `7D` | `0.9200` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 40,700.00 USD | 4,910.00 USD | 22,830.00 USD |
| `1D` | `0.9220` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 7,870.00 USD | 1,100.00 USD | 3,060.00 USD |
| `7D` | `0.9220` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 15,960.00 USD | 2,440.00 USD | 15,640.00 USD |
| `1D` | `0.9240` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 14,860.00 USD | 5,440.00 USD | 36.99 USD |
| `7D` | `0.9240` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 56,450.00 USD | 17,850.00 USD | 51,900.00 USD |
| `1D` | `0.9260` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 10,930.00 USD | 9,570.00 USD | 21,980.00 USD |
| `7D` | `0.9260` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 32,320.00 USD | 3,140.00 USD | 21,360.00 USD |
| `1D` | `0.9280` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 24,160.00 USD | 4,120.00 USD | 6,930.00 USD |
| `7D` | `0.9280` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 85,040.00 USD | 14,050.00 USD | 26,530.00 USD |
| `1D` | `0.9300` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 14,980.00 USD | 1,350.00 USD | 16,060.00 USD |
| `7D` | `0.9300` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 27,510.00 USD | 12,060.00 USD | 18,410.00 USD |
| `1D` | `0.9320` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 24,590.00 USD | 12,760.00 USD | 12,400.00 USD |
| `7D` | `0.9320` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 29,490.00 USD | 7,900.00 USD | 6,120.00 USD |
| `1D` | `0.9340` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 21,360.00 USD | 11,340.00 USD | 10,720.00 USD |
| `7D` | `0.9340` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 53,710.00 USD | 31,710.00 USD | 24,000.00 USD |
| `1D` | `0.9360` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 49,360.00 USD | 11,970.00 USD | 19,500.00 USD |
| `7D` | `0.9360` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 59,280.00 USD | 6,250.00 USD | 14,950.00 USD |
| `1D` | `0.9380` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 25,680.00 USD | 14,710.00 USD | 10,490.00 USD |
| `7D` | `0.9380` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 20,200.00 USD | 20,670.00 USD | 12,240.00 USD |
| `1D` | `0.9400` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 28,130.00 USD | 10,650.00 USD | 13,970.00 USD |
| `7D` | `0.9400` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 26,270.00 USD | 6,010.00 USD | 7,370.00 USD |
| `1D` | `0.9420` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 30,630.00 USD | 13,800.00 USD | 3,150.00 USD |
| `7D` | `0.9420` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 51,440.00 USD | 21,220.00 USD | 10,090.00 USD |
| `1D` | `0.9440` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 35,560.00 USD | 18,570.00 USD | 7,510.00 USD |
| `7D` | `0.9440` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 57,220.00 USD | 26,910.00 USD | 26,070.00 USD |
| `1D` | `0.9460` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 31,490.00 USD | 28,910.00 USD | 59,600.00 USD |
| `7D` | `0.9460` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 70,510.00 USD | 19,530.00 USD | 44,410.00 USD |
| `1D` | `0.9480` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 95,800.00 USD | 23,580.00 USD | 34,860.00 USD |
| `7D` | `0.9480` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 202,170.00 USD | 42,900.00 USD | 92,480.00 USD |
| `1D` | `0.9500` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 40,200.00 USD | 9,070.00 USD | 38,620.00 USD |
| `7D` | `0.9500` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 125,620.00 USD | 46,290.00 USD | 114,560.00 USD |
| `1D` | `0.9520` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 66,670.00 USD | 32,590.00 USD | 23,670.00 USD |
| `7D` | `0.9520` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 144,770.00 USD | 19,800.00 USD | 57,660.00 USD |
| `1D` | `0.9540` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 52,780.00 USD | 30,680.00 USD | 29,540.00 USD |
| `7D` | `0.9540` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 116,590.00 USD | 92,780.00 USD | 108,960.00 USD |
| `1D` | `0.9560` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 122,960.00 USD | 46,040.00 USD | 63,010.00 USD |
| `7D` | `0.9560` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 207,570.00 USD | 32,950.00 USD | 87,460.00 USD |
| `1D` | `0.9580` | 915,330.00 USD | 0.00 USD | 915,330.00 USD | 46,030.00 USD | 28,570.00 USD | 32,600.00 USD |
| `7D` | `0.9580` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 107,300.00 USD | 48,150.00 USD | 119,950.00 USD |
| `1D` | `0.9600` | 808,130.00 USD | 0.00 USD | 808,130.00 USD | 94,650.00 USD | 31,740.00 USD | 10,350.00 USD |
| `7D` | `0.9600` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 222,250.00 USD | 82,170.00 USD | 59,710.00 USD |
| `1D` | `0.9620` | 671,390.00 USD | 0.00 USD | 671,390.00 USD | 50,390.00 USD | 18,850.00 USD | 13,160.00 USD |
| `7D` | `0.9620` | 693,000.00 USD | 0.00 USD | 693,000.00 USD | 140,700.00 USD | 46,240.00 USD | 26,080.00 USD |
| `1D` | `0.9640` | 589,000.00 USD | 0.00 USD | 589,000.00 USD | 21,690.00 USD | 14,860.00 USD | 32,740.00 USD |
| `7D` | `0.9640` | 479,980.00 USD | 0.00 USD | 479,980.00 USD | 84,900.00 USD | 778.20 USD | 6,180.00 USD |
| `1D` | `0.9660` | 519,710.00 USD | 0.00 USD | 519,710.00 USD | 76,360.00 USD | 26,330.00 USD | 35,150.00 USD |
| `7D` | `0.9660` | 388,120.00 USD | 0.00 USD | 388,120.00 USD | 40,050.00 USD | 9,550.00 USD | 31,400.00 USD |
| `1D` | `0.9680` | 381,870.00 USD | 0.00 USD | 381,870.00 USD | 39,890.00 USD | 18,800.00 USD | 38,710.00 USD |
| `7D` | `0.9680` | 307,130.00 USD | 0.00 USD | 307,130.00 USD | 26,480.00 USD | 4,670.00 USD | 36,940.00 USD |
| `1D` | `0.9700` | 284,470.00 USD | 0.00 USD | 284,470.00 USD | 52,020.00 USD | 17,520.00 USD | 19,710.00 USD |
| `7D` | `0.9700` | 239,040.00 USD | 0.00 USD | 239,040.00 USD | 33,960.00 USD | 25,160.00 USD | 36,880.00 USD |
| `1D` | `0.9720` | 195,220.00 USD | 0.00 USD | 195,220.00 USD | 49,670.00 USD | 14,050.00 USD | 22,180.00 USD |
| `7D` | `0.9720` | 143,040.00 USD | 0.00 USD | 143,040.00 USD | 53,850.00 USD | 0.00 USD | 9,610.00 USD |
| `1D` | `0.9740` | 109,310.00 USD | 0.00 USD | 109,310.00 USD | 9,580.00 USD | 12,820.00 USD | 14,240.00 USD |
| `7D` | `0.9740` | 79,590.00 USD | 0.00 USD | 79,590.00 USD | 0.00 USD | 16,590.00 USD | 8,630.00 USD |
| `1D` | `0.9760` | 72,670.00 USD | 0.00 USD | 72,670.00 USD | 19,600.00 USD | 13,960.00 USD | 8,070.00 USD |
| `7D` | `0.9760` | 54,370.00 USD | 0.00 USD | 54,370.00 USD | 15,320.00 USD | 5,480.00 USD | 9,280.00 USD |
| `1D` | `0.9780` | 31,040.00 USD | 0.00 USD | 31,040.00 USD | 23,150.00 USD | 0.00 USD | 7,890.00 USD |
| `7D` | `0.9780` | 24,280.00 USD | 0.00 USD | 24,280.00 USD | 0.00 USD | 0.00 USD | 24,280.00 USD |
| `1D` | `0.9790` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9800` | 12,020.00 USD | 12,020.00 USD | 0.00 USD | 156.00 USD | 0.00 USD | 11,860.00 USD |
| `7D` | `0.9800` | 151,540.00 USD | 151,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 151,540.00 USD |
| `7D` | `0.9800` | 303,090.00 USD | 303,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 151,540.00 USD |
| `1D` | `0.9820` | 47,030.00 USD | 47,030.00 USD | 0.00 USD | 15,980.00 USD | 12,160.00 USD | 6,870.00 USD |
| `7D` | `0.9820` | 385,450.00 USD | 385,450.00 USD | 0.00 USD | 10,090.00 USD | 0.00 USD | 72,280.00 USD |
| `1D` | `0.9840` | 68,230.00 USD | 68,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21,190.00 USD |
| `7D` | `0.9840` | 406,370.00 USD | 406,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,920.00 USD |
| `1D` | `0.9860` | 69,960.00 USD | 69,960.00 USD | 0.00 USD | 575.70 USD | 0.00 USD | 1,160.00 USD |
| `7D` | `0.9860` | 407,180.00 USD | 407,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 803.95 USD |
| `1D` | `0.9880` | 70,490.00 USD | 70,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 531.00 USD |
| `7D` | `0.9880` | 448,100.00 USD | 448,100.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 901.60 USD |
| `1D` | `0.9900` | 134,310.00 USD | 134,310.00 USD | 0.00 USD | 50,430.00 USD | 0.00 USD | 13,390.00 USD |
| `7D` | `0.9900` | 449,000.00 USD | 449,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 906.61 USD |
| `1D` | `0.9920` | 147,190.00 USD | 147,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,880.00 USD |
| `7D` | `0.9920` | 469,440.00 USD | 469,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,440.00 USD |
| `1D` | `0.9940` | 167,360.00 USD | 167,360.00 USD | 0.00 USD | 6,920.00 USD | 13,250.00 USD | 0.00 USD |
| `1D` | `0.9960` | 169,990.00 USD | 169,990.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD | 0.00 USD |
| `7D` | `0.9960` | 544,890.00 USD | 544,890.00 USD | 0.00 USD | 32,670.00 USD | 0.00 USD | 42,770.00 USD |
| `1D` | `0.9980` | 197,910.00 USD | 197,910.00 USD | 0.00 USD | 26,250.00 USD | 0.00 USD | 1,680.00 USD |
| `7D` | `0.9980` | 601,800.00 USD | 601,800.00 USD | 0.00 USD | 52,700.00 USD | 0.00 USD | 4,210.00 USD |
| `1D` | `1.00` | 281,800.00 USD | 281,800.00 USD | 0.00 USD | 50,740.00 USD | 31,440.00 USD | 1,710.00 USD |
| `7D` | `1.00` | 654,650.00 USD | 654,650.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.00` | 282,000.00 USD | 282,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 192.37 USD |
| `7D` | `1.00` | 698,220.00 USD | 698,220.00 USD | 0.00 USD | 28,410.00 USD | 13,940.00 USD | 1,220.00 USD |
| `1D` | `1.00` | 300,310.00 USD | 300,310.00 USD | 0.00 USD | 10,110.00 USD | 5,360.00 USD | 2,830.00 USD |
| `7D` | `1.00` | 723,290.00 USD | 723,290.00 USD | 0.00 USD | 25,070.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.01` | 368,930.00 USD | 368,930.00 USD | 0.00 USD | 44,970.00 USD | 5,090.00 USD | 18,570.00 USD |
| `7D` | `1.01` | 757,400.00 USD | 757,400.00 USD | 0.00 USD | 34,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.01` | 387,780.00 USD | 387,780.00 USD | 0.00 USD | 0.00 USD | 4,400.00 USD | 14,450.00 USD |
| `7D` | `1.01` | 773,650.00 USD | 773,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,250.00 USD |
| `1D` | `1.01` | 402,970.00 USD | 402,970.00 USD | 0.00 USD | 7,050.00 USD | 8,140.00 USD | 0.00 USD |
| `7D` | `1.01` | 787,660.00 USD | 787,660.00 USD | 0.00 USD | 0.00 USD | 14,020.00 USD | 0.00 USD |
| `1D` | `1.01` | 444,500.00 USD | 444,500.00 USD | 0.00 USD | 16,070.00 USD | 25,300.00 USD | 155.80 USD |
| `7D` | `1.01` | 847,200.00 USD | 847,200.00 USD | 0.00 USD | 33,230.00 USD | 26,300.00 USD | 0.00 USD |
| `1D` | `1.01` | 479,500.00 USD | 479,500.00 USD | 0.00 USD | 5,630.00 USD | 4,350.00 USD | 25,020.00 USD |
| `7D` | `1.01` | 878,600.00 USD | 878,600.00 USD | 0.00 USD | 2,870.00 USD | 28,140.00 USD | 388.43 USD |
| `1D` | `1.02` | 519,720.00 USD | 519,720.00 USD | 0.00 USD | 20,120.00 USD | 21.80 USD | 20,080.00 USD |
| `7D` | `1.02` | 918,980.00 USD | 918,980.00 USD | 0.00 USD | 0.00 USD | 28,470.00 USD | 11,910.00 USD |
| `1D` | `1.02` | 557,230.00 USD | 557,230.00 USD | 0.00 USD | 5,990.00 USD | 8,490.00 USD | 23,040.00 USD |
| `7D` | `1.02` | 960,960.00 USD | 960,960.00 USD | 0.00 USD | 0.00 USD | 20,410.00 USD | 21,560.00 USD |
| `1D` | `1.02` | 621,420.00 USD | 621,420.00 USD | 0.00 USD | 44,710.00 USD | 4,370.00 USD | 15,110.00 USD |
| `7D` | `1.02` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 81,220.00 USD | 44,250.00 USD |
| `1D` | `1.02` | 697,880.00 USD | 697,880.00 USD | 0.00 USD | 51,380.00 USD | 3,670.00 USD | 21,410.00 USD |
| `7D` | `1.02` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 56,930.00 USD | 52,290.00 USD | 111,720.00 USD |
| `1D` | `1.02` | 810,230.00 USD | 810,230.00 USD | 0.00 USD | 34,630.00 USD | 24,720.00 USD | 53,000.00 USD |
| `7D` | `1.02` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 52,560.00 USD | 56,700.00 USD | 86,350.00 USD |
| `1D` | `1.03` | 898,200.00 USD | 898,200.00 USD | 0.00 USD | 52,170.00 USD | 17,130.00 USD | 18,660.00 USD |
| `7D` | `1.03` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 22,650.00 USD | 124,760.00 USD | 25,070.00 USD |
| `1D` | `1.03` | 958,830.00 USD | 958,830.00 USD | 0.00 USD | 31,210.00 USD | 10,940.00 USD | 18,480.00 USD |
| `7D` | `1.03` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 250,040.00 USD | 50,530.00 USD | 24,480.00 USD |
| `1D` | `1.03` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 95,260.00 USD | 24,470.00 USD | 33,610.00 USD |
| `7D` | `1.03` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 134,200.00 USD | 29,810.00 USD | 19,120.00 USD |
| `1D` | `1.03` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 69,660.00 USD | 8,960.00 USD | 35,950.00 USD |
| `7D` | `1.03` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD |
| `1D` | `1.03` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 38,050.00 USD | 9,250.00 USD | 21,490.00 USD |
| `7D` | `1.03` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 216,820.00 USD | 8,290.00 USD | 4,310.00 USD |
| `1D` | `1.04` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 18,100.00 USD | 13,840.00 USD | 33,350.00 USD |
| `7D` | `1.04` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 262,550.00 USD | 3,170.00 USD | 42,930.00 USD |
| `1D` | `1.04` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 62,580.00 USD | 3,190.00 USD | 24,080.00 USD |
| `7D` | `1.04` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 178,400.00 USD | 1,290.00 USD | 199,090.00 USD |
| `1D` | `1.04` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 7,710.00 USD | 8,100.00 USD | 10,490.00 USD |
| `7D` | `1.04` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 279,460.00 USD | 9,430.00 USD | 93,080.00 USD |
| `1D` | `1.04` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 11,290.00 USD | 9,870.00 USD | 8,370.00 USD |
| `7D` | `1.04` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD |
| `1D` | `1.04` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 7,410.00 USD | 14,400.00 USD | 36,760.00 USD |
| `7D` | `1.04` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD |
| `1D` | `1.05` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 21,670.00 USD | 4,160.00 USD | 321.14 USD |
| `7D` | `1.05` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD |
| `1D` | `1.05` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 15,080.00 USD | 3,210.00 USD | 4,880.00 USD |
| `7D` | `1.05` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 199,320.00 USD | 28,070.00 USD | 161,420.00 USD |
| `1D` | `1.05` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 43,610.00 USD | 11,120.00 USD | 19,950.00 USD |
| `7D` | `1.05` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 91,750.00 USD | 29,070.00 USD | 40,740.00 USD |
| `1D` | `1.05` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 23,230.00 USD | 7,030.00 USD | 31,690.00 USD |
| `7D` | `1.05` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 140,970.00 USD | 49,780.00 USD | 133,760.00 USD |
| `1D` | `1.05` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 8,900.00 USD | 340.84 USD | 6,470.00 USD |
| `7D` | `1.05` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 82,020.00 USD | 42,140.00 USD | 36,750.00 USD |
| `1D` | `1.06` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 7,850.00 USD | 1,750.00 USD | 25,090.00 USD |
| `7D` | `1.06` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 187,610.00 USD | 48,000.00 USD | 121,890.00 USD |
| `1D` | `1.06` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 29,640.00 USD | 3,000.00 USD | 14,040.00 USD |
| `7D` | `1.06` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 205,690.00 USD | 63,110.00 USD | 94,960.00 USD |
| `1D` | `1.06` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 3,760.00 USD | 3,710.00 USD | 8,130.00 USD |
| `7D` | `1.06` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 197,680.00 USD | 69,880.00 USD | 118,850.00 USD |
| `1D` | `1.06` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 1,990.00 USD | 7,750.00 USD | 2,400.00 USD |
| `7D` | `1.06` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 131,720.00 USD | 83,000.00 USD | 65,720.00 USD |
| `1D` | `1.06` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 5,090.00 USD | 2,370.00 USD | 7,970.00 USD |
| `7D` | `1.06` | 7,260,000.00 USD | 7,260,000.00 USD | 0.00 USD | 102,750.00 USD | 49,310.00 USD | 92,130.00 USD |
| `1D` | `1.07` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 12,510.00 USD | 2,860.00 USD | 5,690.00 USD |
| `7D` | `1.07` | 7,430,000.00 USD | 7,430,000.00 USD | 0.00 USD | 77,660.00 USD | 32,860.00 USD | 61,900.00 USD |
| `1D` | `1.07` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 10,720.00 USD | 4,390.00 USD | 3,180.00 USD |
| `7D` | `1.07` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 221,410.00 USD | 30,180.00 USD | 93,450.00 USD |
| `1D` | `1.07` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 9,230.00 USD | 5,040.00 USD | 6,410.00 USD |
| `7D` | `1.07` | 7,970,000.00 USD | 7,970,000.00 USD | 0.00 USD | 121,300.00 USD | 33,170.00 USD | 42,480.00 USD |
| `1D` | `1.07` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 9,330.00 USD | 5,210.00 USD | 11,220.00 USD |
| `7D` | `1.07` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 103,500.00 USD | 37,730.00 USD | 83,520.00 USD |
| `1D` | `1.07` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 7,810.00 USD | 4,630.00 USD | 6,930.00 USD |
| `7D` | `1.07` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 102,600.00 USD | 21,500.00 USD | 83,440.00 USD |
| `1D` | `1.08` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 6,260.00 USD | 5,330.00 USD | 12,740.00 USD |
| `7D` | `1.08` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 103,110.00 USD | 18,720.00 USD | 27,400.00 USD |
| `1D` | `1.08` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 9,390.00 USD | 4,070.00 USD | 150.13 USD |
| `7D` | `1.08` | 8,830,000.00 USD | 8,830,000.00 USD | 0.00 USD | 158,650.00 USD | 40,740.00 USD | 69,670.00 USD |
| `1D` | `1.08` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 8,360.00 USD | 1,870.00 USD | 711.93 USD |
| `7D` | `1.08` | 9,060,000.00 USD | 9,060,000.00 USD | 0.00 USD | 176,790.00 USD | 26,190.00 USD | 33,510.00 USD |
| `1D` | `1.08` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 5,240.00 USD | 3,920.00 USD | 4,530.00 USD |
| `7D` | `1.08` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 62,710.00 USD | 20,510.00 USD | 38,480.00 USD |
| `1D` | `1.08` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 3,940.00 USD | 1,600.00 USD | 2,780.00 USD |
| `7D` | `1.08` | 9,370,000.00 USD | 9,370,000.00 USD | 0.00 USD | 46,000.00 USD | 31,940.00 USD | 103,610.00 USD |
| `1D` | `1.09` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 9,560.00 USD | 2,760.00 USD | 6,350.00 USD |
| `7D` | `1.09` | 9,560,000.00 USD | 9,560,000.00 USD | 0.00 USD | 134,170.00 USD | 28,200.00 USD | 34,220.00 USD |
| `1D` | `1.09` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 3,630.00 USD | 4,390.00 USD | 4,990.00 USD |
| `7D` | `1.09` | 9,790,000.00 USD | 9,790,000.00 USD | 0.00 USD | 59,850.00 USD | 54,400.00 USD | 117,570.00 USD |
| `1D` | `1.09` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 5,800.00 USD | 3,270.00 USD | 1,950.00 USD |
| `7D` | `1.09` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 109,670.00 USD | 18,350.00 USD | 31,220.00 USD |
| `1D` | `1.09` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 4,370.00 USD | 149.76 USD | 966.50 USD |
| `7D` | `1.09` | 10,080,000.00 USD | 10,080,000.00 USD | 0.00 USD | 39,750.00 USD | 24,570.00 USD | 62,450.00 USD |
| `1D` | `1.09` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 687.18 USD | 2,490.00 USD | 2,060.00 USD |
| `7D` | `1.09` | 10,240,000.00 USD | 10,240,000.00 USD | 0.00 USD | 66,620.00 USD | 37,290.00 USD | 55,440.00 USD |
| `1D` | `1.10` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 1,740.00 USD | 3,660.00 USD | 82.24 USD |
| `7D` | `1.10` | 10,410,000.00 USD | 10,410,000.00 USD | 0.00 USD | 71,580.00 USD | 30,090.00 USD | 65,790.00 USD |
| `1D` | `1.10` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 4,120.00 USD | 11.15 USD | 992.14 USD |
| `7D` | `1.10` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 114,820.00 USD | 21,050.00 USD | 97,830.00 USD |
| `1D` | `1.10` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 1,940.00 USD | 798.95 USD | 2,390.00 USD |
| `7D` | `1.10` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 182,190.00 USD | 62,900.00 USD | 52,890.00 USD |
| `1D` | `1.10` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 2,330.00 USD | 3,250.00 USD | 2,320.00 USD |
| `7D` | `1.10` | 11,160,000.00 USD | 11,160,000.00 USD | 0.00 USD | 118,210.00 USD | 18,440.00 USD | 88,980.00 USD |
| `1D` | `1.10` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 2,770.00 USD | 2,620.00 USD | 5,730.00 USD |
| `7D` | `1.10` | 11,310,000.00 USD | 11,310,000.00 USD | 0.00 USD | 65,300.00 USD | 22,070.00 USD | 57,280.00 USD |
| `1D` | `1.11` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 1,590.00 USD | 50.69 USD | 111.00 USD |
| `7D` | `1.11` | 11,350,000.00 USD | 11,350,000.00 USD | 0.00 USD | 22,290.00 USD | 5,830.00 USD | 12,610.00 USD |
| `1D` | `1.11` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 2,660.00 USD | 1,620.00 USD | 0.00 USD |
| `7D` | `1.11` | 11,530,000.00 USD | 11,530,000.00 USD | 0.00 USD | 90,280.00 USD | 31,510.00 USD | 54,600.00 USD |
| `7D` | `1.11` | 11,690,000.00 USD | 11,690,000.00 USD | 0.00 USD | 33,280.00 USD | 36,570.00 USD | 93,640.00 USD |
| `7D` | `1.11` | 11,800,000.00 USD | 11,800,000.00 USD | 0.00 USD | 64,670.00 USD | 26,930.00 USD | 24,380.00 USD |
| `7D` | `1.11` | 11,880,000.00 USD | 11,880,000.00 USD | 0.00 USD | 32,450.00 USD | 36,820.00 USD | 6,220.00 USD |
| `7D` | `1.12` | 11,990,000.00 USD | 11,990,000.00 USD | 0.00 USD | 59,080.00 USD | 33,150.00 USD | 13,270.00 USD |
| `7D` | `1.12` | 12,070,000.00 USD | 12,070,000.00 USD | 0.00 USD | 37,220.00 USD | 17,240.00 USD | 30,330.00 USD |
| `7D` | `1.12` | 12,170,000.00 USD | 12,170,000.00 USD | 0.00 USD | 32,060.00 USD | 41,540.00 USD | 25,240.00 USD |
| `7D` | `1.12` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 52,230.00 USD | 16,980.00 USD | 11,540.00 USD |
| `7D` | `1.12` | 12,340,000.00 USD | 12,340,000.00 USD | 0.00 USD | 58,100.00 USD | 5,280.00 USD | 29,870.00 USD |
| `7D` | `1.13` | 12,390,000.00 USD | 12,390,000.00 USD | 0.00 USD | 16,200.00 USD | 5,970.00 USD | 28,450.00 USD |
| `7D` | `1.13` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 2,210.00 USD | 13,650.00 USD | 28,630.00 USD |
| `7D` | `1.13` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 95,910.00 USD | 18,230.00 USD | 42,350.00 USD |
| `7D` | `1.13` | 12,730,000.00 USD | 12,730,000.00 USD | 0.00 USD | 71,210.00 USD | 0.00 USD | 65,880.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `207.00M` | Total OI Tokens: `211,450,911.5 DOT`
  * 1h OI Change: `-1.20%` | 4h OI Change: `-3.39%` | 24h OI Change: `-7.06%`
  * Exchange Breakdown: Binance=`36.32M` | Bybit=`24.31M` | OKX=`10.19M` | Hyperliquid=`5.65M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.31K` | Last 24h: `7.91K` | Last 3d: `-10.37K` | Last 7d: `-19.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0093%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0097%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0040%` | **USDT Bitget** | `0.0042%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `52.31%` | `47.69%` | `1.10` | 3,340,000.00 USD |
| `15M` | `Binance` | `46.64%` | `53.36%` | `0.87` | 1,280,000.00 USD |
| `15M` | `OKX` | `54.89%` | `45.11%` | `1.22` | 347,070.00 USD |
| `15M` | `Bybit` | `67.09%` | `32.91%` | `2.04` | 419,780.00 USD |
| `15M` | `KuCoin` | `44.52%` | `55.48%` | `0.80` | 46,700.00 USD |
| `15M` | `Gate` | `55.66%` | `44.34%` | `1.26` | 67,090.00 USD |
| `15M` | `Bitget` | `54.61%` | `45.39%` | `1.20` | 120,740.00 USD |
| `15M` | `BingX` | `47.73%` | `52.27%` | `0.91` | 145,580.00 USD |
| `15M` | `MEXC` | `40.76%` | `59.24%` | `0.69` | 321,430.00 USD |
| `15M` | `Bitunix` | `48.85%` | `51.15%` | `0.96` | 181,600.00 USD |
| `15M` | `Hyperliquid` | `62.43%` | `37.57%` | `1.66` | 29,320.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.1%` | `50.9%` | `0.96` | 40,630.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `64.72%` | `35.28%` | `1.83` | 279,580.00 USD |
| `15M` | `HTX` | `1.22%` | `98.78%` | `0.01` | 11,320.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `92.52%` | `7.48%` | `12.37` | 49,840.00 USD |
| `15M` | `Aster` | `5.25%` | `94.75%` | `0.06` | 874.63 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `71.16%` | `28.84%` | `2.47` | 753.89 USD |
| `15M` | `Whale Positions` | `46.64%` | `53.36%` | `0.87` | 1,280,000.00 USD |
| `15M` | `Global Accounts` | `52.31%` | `47.69%` | `1.10` | 3,340,000.00 USD |
| `1H` | `DOT` | `47.99%` | `52.01%` | `0.92` | 26,260,000.00 USD |
| `1H` | `Binance` | `48.32%` | `51.68%` | `0.93` | 10,490,000.00 USD |
| `1H` | `OKX` | `49.69%` | `50.31%` | `0.99` | 3,320,000.00 USD |
| `1H` | `Bybit` | `49.49%` | `50.51%` | `0.98` | 3,890,000.00 USD |
| `1H` | `KuCoin` | `44.33%` | `55.67%` | `0.80` | 532,220.00 USD |
| `1H` | `Gate` | `41.06%` | `58.94%` | `0.70` | 717,460.00 USD |
| `1H` | `Bitget` | `43.42%` | `56.58%` | `0.77` | 819,870.00 USD |
| `1H` | `BingX` | `46.97%` | `53.03%` | `0.89` | 1,600,000.00 USD |
| `1H` | `MEXC` | `58.85%` | `41.15%` | `1.43` | 1,960,000.00 USD |
| `1H` | `Bitunix` | `40.79%` | `59.21%` | `0.69` | 934,880.00 USD |
| `1H` | `Hyperliquid` | `34.74%` | `65.26%` | `0.53` | 406,540.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `44.92%` | `55.08%` | `0.82` | 165,700.00 USD |
| `1H` | `Crypto.com` | `80.88%` | `19.12%` | `4.23` | 0.00 USD |
| `1H` | `WhiteBIT` | `77.24%` | `22.76%` | `3.39` | 1,090,000.00 USD |
| `1H` | `HTX` | `49.29%` | `50.71%` | `0.97` | 35,220.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `27.95%` | `72.05%` | `0.39` | 185,380.00 USD |
| `1H` | `Aster` | `73.93%` | `26.07%` | `2.84` | 107,250.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `54.91%` | `45.09%` | `1.22` | 9,890.00 USD |
| `1H` | `Whale Positions` | `48.32%` | `51.68%` | `0.93` | 10,490,000.00 USD |
| `1H` | `Global Accounts` | `47.99%` | `52.01%` | `0.92` | 26,260,000.00 USD |
| `4H` | `DOT` | `48.25%` | `51.75%` | `0.93` | 415,740,000.00 USD |
| `4H` | `Binance` | `49.31%` | `50.69%` | `0.97` | 171,200,000.00 USD |
| `4H` | `OKX` | `46.49%` | `53.51%` | `0.87` | 66,030,000.00 USD |
| `4H` | `Bybit` | `44.15%` | `55.85%` | `0.79` | 49,240,000.00 USD |
| `4H` | `KuCoin` | `43.93%` | `56.07%` | `0.78` | 4,140,000.00 USD |
| `4H` | `Gate` | `49.12%` | `50.88%` | `0.97` | 7,690,000.00 USD |
| `4H` | `Bitget` | `44.89%` | `55.11%` | `0.81` | 14,280,000.00 USD |
| `4H` | `BingX` | `46.52%` | `53.48%` | `0.87` | 16,050,000.00 USD |
| `4H` | `MEXC` | `50.34%` | `49.66%` | `1.01` | 24,530,000.00 USD |
| `4H` | `Bitunix` | `43.32%` | `56.68%` | `0.76` | 10,740,000.00 USD |
| `4H` | `Hyperliquid` | `46.06%` | `53.94%` | `0.85` | 28,160,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `42.04%` | `57.96%` | `0.73` | 2,000,000.00 USD |
| `4H` | `Crypto.com` | `42.91%` | `57.09%` | `0.75` | 11,300.00 USD |
| `4H` | `WhiteBIT` | `79.64%` | `20.36%` | `3.91` | 10,800,000.00 USD |
| `4H` | `HTX` | `52.95%` | `47.05%` | `1.13` | 289,290.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `37.59%` | `62.41%` | `0.60` | 6,550,000.00 USD |
| `4H` | `Aster` | `47.54%` | `52.46%` | `0.91` | 600,260.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `56.52%` | `43.48%` | `1.30` | 3,410,000.00 USD |
| `4H` | `Whale Positions` | `49.31%` | `50.69%` | `0.97` | 171,200,000.00 USD |
| `4H` | `Global Accounts` | `48.25%` | `51.75%` | `0.93` | 415,740,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.01` | `1.01` | `1.01` | `1.01` | `1.00` | 367,151.31 USD | 115,663.71 USD | 251,487.60 USD | -135,823.89 USD | `-36.99%` | `2B / 13S` |
| `0:00 UTC` | `1.00` | `1.00` | `1.00` | `1.01` | `0.9990` | 615,154.97 USD | 223,058.23 USD | 392,096.73 USD | -169,038.50 USD | `-27.48%` | `6B / 35S` |
| `5:00 UTC` | `1.00` | `1.00` | `1.00` | `1.00` | `0.9973` | 953,336.44 USD | 578,861.35 USD | 374,475.09 USD | 204,386.27 USD | `+21.44%` | `11B / 7S` |
| `0:00 UTC` | `0.9950` | `0.9984` | `0.9950` | `1.00` | `0.9922` | 743,609.00 USD | 261,947.82 USD | 481,661.18 USD | -219,713.36 USD | `-29.55%` | `13B / 51S` |
| `5:00 UTC` | `0.9889` | `0.9893` | `0.9889` | `0.9946` | `0.9848` | 979,161.78 USD | 393,210.73 USD | 585,951.05 USD | -192,740.33 USD | `-19.68%` | `5B / 24S` |
| `0:00 UTC` | `0.9900` | `0.9907` | `0.9900` | `0.9929` | `0.9876` | 406,034.57 USD | 195,166.38 USD | 210,868.18 USD | -15,701.80 USD | `-3.87%` | `3B / 8S` |
| `5:00 UTC` | `0.9850` | `0.9875` | `0.9850` | `0.9919` | `0.9848` | 373,179.10 USD | 160,064.27 USD | 213,114.83 USD | -53,050.55 USD | `-14.22%` | `10B / 18S` |
| `0:00 UTC` | `0.9787` | `0.9807` | `0.9787` | `0.9872` | `0.9767` | 1,756,422.05 USD | 785,190.37 USD | 971,231.69 USD | -186,041.32 USD | `-10.59%` | `9B / 23S` |
| `5:00 UTC` | `0.9813` | `0.9827` | `0.9813` | `0.9867` | `0.9789` | 947,049.41 USD | 720,261.00 USD | 226,788.42 USD | 493,472.58 USD | `+52.11%` | `28B / 1S` |
| `0:00 UTC` | `0.9805` | `0.9820` | `0.9805` | `0.9849` | `0.9799` | 378,562.61 USD | 187,566.73 USD | 190,995.87 USD | -3,429.14 USD | `-0.91%` | `11B / 5S` |

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
| `5m` | -3,310.00 USD | -7,670.00 USD | **`DISTRIBUTION`** |
| `15m` | -5,630.00 USD | -30,180.00 USD | **`DISTRIBUTION`** |
| `30m` | 6,520.00 USD | 647,430.00 USD | **`ACCUMULATION`** |
| `1h` | -91,020.00 USD | 285,300.00 USD | **`ACCUMULATION`** |
| `2h` | -107,900.00 USD | -68,110.00 USD | **`DISTRIBUTION`** |
| `4h` | -148,300.00 USD | -1,240,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -132,680.00 USD | -1,610,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -179,710.00 USD | -2,120,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -349,650.00 USD | -1,330,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -405,560.00 USD | -3,080,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,570,000.00 USD | -18,540,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,590,000.00 USD | -73,190,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-3.31K` | 15m=`-5.63K` | 1h=`-91.02K` | 24h=`-405.56K`
* Futures Capital Netflows: 5m=`-7.67K` | 15m=`-30.18K` | 1h=`+285.30K` | 24h=`-3.08M`
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
  * `2026-10-30 00:48:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:17:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.9938` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.03` (Risk Distance: `0.0400` pts)
  * +2.5R Take Profit: `0.8938`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9878`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
