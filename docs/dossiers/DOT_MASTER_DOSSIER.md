# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 01:20:51 IST` (`2026-10-29 19:50:51 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9760` | **Live Ask Quote**: `0.9960` | **Mid Price**: `0.9860`
- **Spread Points**: `20.00` | **Spread BPS**: `202.84 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.9775` | VWAP Z-Score: `-0.32` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0074` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `41.78` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.02` | Lower -3.00σ Band: `0.9352`
  * Upper +2.51σ Band: `1.01` | Lower -2.51σ Band: `0.9421`
  * Upper +2.01σ Band: `1.01` | Lower -2.01σ Band: `0.9491`
  * Upper +2.00σ Band: `1.01` | Lower -2.00σ Band: `0.9493`
  * Upper +1.28σ Band: `0.9955` | Lower -1.28σ Band: `0.9594`
  * Upper +1.00σ Band: `0.9915` | Lower -1.00σ Band: `0.9634`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9767` | EMA-20=`0.9816` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9818` (Slope: `+0.0000`) | EMA-100=`0.9827`
  * Institutional Anchors: EMA-144=`0.9836` | EMA-200=`0.9843` (Slope: `-0.0513`) | EMA-233=`0.9843`
- **Range Boundaries**: 24H High=`1.03` | 24H Low=`0.9510` | Weekly High=`1.03` | Weekly Low=`0.9510`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9934` (Distance: `-0.74%`)
  * Point of Control (POC) = `0.9739` (Distance: `+1.24%`)
  * Value Area Low (VAL) = `0.9530` (Distance: `+3.46%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `0.9821` - `0.9899`
  * Optimal Trade Entry (OTE 0.705): `0.9880`
  * Structural Invalidation Anchor (0.786): `0.9939`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9839` | `0.9886` | `0.9839` | `0.9874` | `203,844` | 201,213.34 USD | 22,986.52 USD | `+11.42%` | -1,133,865.06 USD | `+0.05` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.9873` | `0.9875` | `0.9851` | `0.9865` | `141,629` | 139,677.18 USD | 653.24 USD | `+0.47%` | -1,133,211.82 USD | `-0.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.9865` | `0.9873` | `0.9862` | `0.9862` | `47,958` | 47,326.51 USD | -5,539.83 USD | `-11.71%` | -1,138,751.65 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.9839` | `0.9848` | `0.9786` | `0.9788` | `522,197` | 512,523.44 USD | -26,476.30 USD | `-5.17%` | -1,267,845.45 USD | `+0.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.9788` | `0.9857` | `0.9780` | `0.9839` | `535,712` | 526,140.64 USD | 110,993.88 USD | `+21.10%` | -1,156,851.58 USD | `+0.70` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.9839` | `0.9886` | `0.9839` | `0.9864` | `393,648` | 388,431.28 USD | 18,314.18 USD | `+4.71%` | -1,138,537.40 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `1.01` | `1.01` | `0.9847` | `0.9918` | `3,301,086` | 3,291,262.18 USD | -377,105.92 USD | `-11.46%` | -1,426,808.60 USD | `-1.10` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.9918` | `0.9929` | `0.9766` | `0.9840` | `3,542,573` | 3,482,685.13 USD | 238,678.91 USD | `+6.85%` | -1,188,129.69 USD | `+0.79` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.9839` | `0.9886` | `0.9780` | `0.9864` | `1,451,558` | 1,427,095.36 USD | 102,831.75 USD | `+7.21%` | -1,085,297.93 USD | `+0.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | -137,778.42 USD | `+0.23` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | -315,355.23 USD | `-0.25` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9862` | `11,162,696` | 11,103,709.94 USD | -770,156.95 USD | `-6.94%` | -1,085,512.18 USD | `-1.19` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.01` | `1.01` | `0.9612` | `0.9700` | `15,616,467` | 15,304,422.31 USD | 595,816.59 USD | `+3.89%` | -236,044.76 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.9699` | `0.9906` | `0.9674` | `0.9732` | `8,505,701` | 8,320,368.15 USD | 13,201.93 USD | `+0.16%` | -222,842.83 USD | `+0.15` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | -137,778.42 USD | `+0.23` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | -315,355.23 USD | `-0.25` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9862` | `11,162,696` | 11,103,709.94 USD | -770,156.95 USD | `-6.94%` | -1,085,512.18 USD | `-1.19` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:14:07 IST` |

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
| `1D` | `Long Liquidation` | `0.8790` | 2,660,000.00 USD | 2,660,000.00 USD | 17,770.00 USD | 8,500.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8795` | 948.01 USD | 257,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8800` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 3,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8810` | 2,630,000.00 USD | 2,630,000.00 USD | 6,240.00 USD | 3,320.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8820` | 5,130,000.00 USD | 5,130,000.00 USD | 8,660.00 USD | 3,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8830` | 2,610,000.00 USD | 2,610,000.00 USD | 6,600.00 USD | 4,200.00 USD | 36.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8840` | 5,120,000.00 USD | 5,120,000.00 USD | 4,540.00 USD | 5,480.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8850` | 2,600,000.00 USD | 2,600,000.00 USD | 7,980.00 USD | 2,370.00 USD | 2,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8860` | 5,110,000.00 USD | 5,110,000.00 USD | 15,460.00 USD | 7,970.00 USD | 2,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8870` | 2,590,000.00 USD | 2,590,000.00 USD | 19,130.00 USD | 4,450.00 USD | 8,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8880` | 5,080,000.00 USD | 5,080,000.00 USD | 7,150.00 USD | 1,990.00 USD | 11,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8890` | 2,560,000.00 USD | 2,560,000.00 USD | 3,730.00 USD | 3,370.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8900` | 5,060,000.00 USD | 5,060,000.00 USD | 23,060.00 USD | 6,420.00 USD | 20,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8910` | 2,550,000.00 USD | 2,550,000.00 USD | 1,820.00 USD | 1,560.00 USD | 2,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8920` | 5,010,000.00 USD | 5,010,000.00 USD | 45,890.00 USD | 9,570.00 USD | 15,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8925` | 526.84 USD | 256,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8930` | 2,540,000.00 USD | 2,540,000.00 USD | 7,320.00 USD | 2,470.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8940` | 4,940,000.00 USD | 4,940,000.00 USD | 7,120.00 USD | 8,030.00 USD | 26,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8950` | 2,530,000.00 USD | 2,530,000.00 USD | 22.75 USD | 2,460.00 USD | 2,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8960` | 4,900,000.00 USD | 4,900,000.00 USD | 30,390.00 USD | 9,210.00 USD | 12,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8970` | 2,520,000.00 USD | 2,520,000.00 USD | 5,360.00 USD | 3,690.00 USD | 1,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8975` | 9,210.00 USD | 256,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8980` | 4,850,000.00 USD | 4,850,000.00 USD | 31,140.00 USD | 6,910.00 USD | 36,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8990` | 2,510,000.00 USD | 2,510,000.00 USD | 5,550.00 USD | 757.19 USD | 1,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8995` | 3,820.00 USD | 247,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9000` | 4,770,000.00 USD | 4,770,000.00 USD | 39,940.00 USD | 14,050.00 USD | 14,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9010` | 2,510,000.00 USD | 2,510,000.00 USD | 15.65 USD | 39.59 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9020` | 4,700,000.00 USD | 4,700,000.00 USD | 16,980.00 USD | 11,760.00 USD | 15,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9030` | 2,500,000.00 USD | 2,500,000.00 USD | 6,430.00 USD | 3,760.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9035` | 180.16 USD | 243,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9040` | 4,660,000.00 USD | 4,660,000.00 USD | 17,160.00 USD | 5,930.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9050` | 2,490,000.00 USD | 2,490,000.00 USD | 8,300.00 USD | 3,640.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9060` | 4,630,000.00 USD | 4,630,000.00 USD | 53,450.00 USD | 30,600.00 USD | 41,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9070` | 2,470,000.00 USD | 2,470,000.00 USD | 3,810.00 USD | 488.01 USD | 803.91 USD | `Tier 1 CEX` |
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
| `1D` | `Long Liquidation` | `0.9190` | 2,390,000.00 USD | 2,390,000.00 USD | 2,810.00 USD | 138.43 USD | 54.94 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9195` | 7,330.00 USD | 241,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9200` | 4,230,000.00 USD | 4,230,000.00 USD | 40,100.00 USD | 4,910.00 USD | 22,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9210` | 2,390,000.00 USD | 2,390,000.00 USD | 1,470.00 USD | 77.80 USD | 2,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9220` | 4,160,000.00 USD | 4,160,000.00 USD | 15,960.00 USD | 2,370.00 USD | 15,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9225` | 8,360.00 USD | 234,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9230` | 2,380,000.00 USD | 2,380,000.00 USD | 10,750.00 USD | 2,010.00 USD | 907.53 USD | `Tier 1 CEX` |
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
| `1D` | `Long Liquidation` | `0.9350` | 2,170,000.00 USD | 2,170,000.00 USD | 36,430.00 USD | 10,930.00 USD | 13,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9360` | 3,610,000.00 USD | 3,610,000.00 USD | 59,280.00 USD | 6,250.00 USD | 14,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9365` | 6,560.00 USD | 225,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9370` | 2,110,000.00 USD | 2,110,000.00 USD | 38,620.00 USD | 12,840.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9375` | 196.97 USD | 219,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9380` | 3,530,000.00 USD | 3,530,000.00 USD | 20,200.00 USD | 20,670.00 USD | 12,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9390` | 2,040,000.00 USD | 2,040,000.00 USD | 17,600.00 USD | 14,430.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9400` | 3,480,000.00 USD | 3,480,000.00 USD | 26,270.00 USD | 6,010.00 USD | 7,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9405` | 141.83 USD | 218,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9410` | 2,000,000.00 USD | 2,000,000.00 USD | 45,250.00 USD | 15,190.00 USD | 2,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9420` | 3,440,000.00 USD | 3,440,000.00 USD | 51,440.00 USD | 21,220.00 USD | 10,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9430` | 1,930,000.00 USD | 1,930,000.00 USD | 21,430.00 USD | 8,230.00 USD | 3,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9440` | 3,360,000.00 USD | 3,360,000.00 USD | 57,220.00 USD | 26,910.00 USD | 26,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9445` | 1,060.00 USD | 218,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9450` | 1,900,000.00 USD | 1,900,000.00 USD | 41,820.00 USD | 22,990.00 USD | 41,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9455` | 106,880.00 USD | 217,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9460` | 3,250,000.00 USD | 3,250,000.00 USD | 80,430.00 USD | 19,530.00 USD | 44,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9470` | 1,790,000.00 USD | 1,790,000.00 USD | 80,990.00 USD | 27,830.00 USD | 40,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9475` | 323.19 USD | 110,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9480` | 3,100,000.00 USD | 3,100,000.00 USD | 202,170.00 USD | 42,900.00 USD | 92,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9490` | 1,640,000.00 USD | 1,640,000.00 USD | 77,380.00 USD | 18,700.00 USD | 28,330.00 USD | `Tier 1 CEX` |
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
| `1D` | `Long Liquidation` | `0.9570` | 1,160,000.00 USD | 1,160,000.00 USD | 113,120.00 USD | 38,550.00 USD | 47,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9580` | 1,610,000.00 USD | 1,610,000.00 USD | 107,300.00 USD | 48,150.00 USD | 119,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9585` | 1,530.00 USD | 1,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9590` | 956,900.00 USD | 956,900.00 USD | 59,310.00 USD | 22,860.00 USD | 31,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9600` | 1,330,000.00 USD | 1,330,000.00 USD | 222,250.00 USD | 82,170.00 USD | 59,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9610` | 842,860.00 USD | 842,860.00 USD | 62,360.00 USD | 27,360.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9620` | 968,430.00 USD | 968,430.00 USD | 140,700.00 USD | 46,240.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9630` | 740,950.00 USD | 740,950.00 USD | 43,690.00 USD | 24,730.00 USD | 24,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9640` | 755,410.00 USD | 755,410.00 USD | 104,730.00 USD | 778.20 USD | 6,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9650` | 647,750.00 USD | 647,750.00 USD | 56,900.00 USD | 14,680.00 USD | 31,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9660` | 642,950.00 USD | 642,950.00 USD | 40,050.00 USD | 9,550.00 USD | 31,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9670` | 544,270.00 USD | 544,270.00 USD | 69,000.00 USD | 19,740.00 USD | 36,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9680` | 561,960.00 USD | 561,960.00 USD | 26,480.00 USD | 4,670.00 USD | 36,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9690` | 419,500.00 USD | 419,500.00 USD | 43,730.00 USD | 30,170.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9700` | 493,870.00 USD | 493,870.00 USD | 33,960.00 USD | 25,160.00 USD | 36,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9710` | 314,380.00 USD | 314,380.00 USD | 60,380.00 USD | 19,100.00 USD | 21,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9720` | 397,870.00 USD | 397,870.00 USD | 53,850.00 USD | 0.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9730` | 213,590.00 USD | 213,590.00 USD | 23,620.00 USD | 691.66 USD | 13,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9740` | 334,420.00 USD | 334,420.00 USD | 0.00 USD | 16,590.00 USD | 8,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9750` | 175,970.00 USD | 175,970.00 USD | 16,060.00 USD | 23,220.00 USD | 15,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9760` | 309,200.00 USD | 309,200.00 USD | 15,320.00 USD | 5,480.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9770` | 120,730.00 USD | 120,730.00 USD | 35,620.00 USD | 2,870.00 USD | 9,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9780` | 279,110.00 USD | 279,110.00 USD | 0.00 USD | 0.00 USD | 24,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9790` | 72,270.00 USD | 72,270.00 USD | 819.00 USD | 0.00 USD | 7,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9800` | 254,830.00 USD | 254,830.00 USD | 0.00 USD | 0.00 USD | 151,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9810` | 63,650.00 USD | 63,650.00 USD | 0.00 USD | 376.40 USD | 8,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9820` | 103,280.00 USD | 103,280.00 USD | 10,090.00 USD | 0.00 USD | 72,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9830` | 54,340.00 USD | 54,340.00 USD | 15,980.00 USD | 11,780.00 USD | 15,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9840` | 20,920.00 USD | 20,920.00 USD | 0.00 USD | 0.00 USD | 20,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9850` | 11,310.00 USD | 11,310.00 USD | 575.70 USD | 0.00 USD | 10,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9860` | 803.95 USD | 803.95 USD | 0.00 USD | 0.00 USD | 803.95 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9860` | 1,610.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | 803.95 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9880` | 42,530.00 USD | 42,530.00 USD | 40,020.00 USD | 0.00 USD | 901.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9890` | 6,840.00 USD | 6,840.00 USD | 0.00 USD | 0.00 USD | 6,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9900` | 43,430.00 USD | 43,430.00 USD | 0.00 USD | 0.00 USD | 906.61 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9910` | 77,040.00 USD | 77,040.00 USD | 50,430.00 USD | 0.00 USD | 19,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9920` | 63,870.00 USD | 63,870.00 USD | 0.00 USD | 0.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9930` | 97,390.00 USD | 97,390.00 USD | 6,920.00 USD | 13,250.00 USD | 191.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9950` | 99,020.00 USD | 99,020.00 USD | 0.00 USD | 1,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9960` | 139,320.00 USD | 139,320.00 USD | 32,670.00 USD | 0.00 USD | 42,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9970` | 127,240.00 USD | 127,240.00 USD | 26,250.00 USD | 1,000.00 USD | 970.29 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9980` | 196,230.00 USD | 196,230.00 USD | 52,700.00 USD | 0.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9990` | 142,880.00 USD | 142,880.00 USD | 9,720.00 USD | 3,910.00 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 249,080.00 USD | 249,080.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 211,780.00 USD | 211,780.00 USD | 41,020.00 USD | 27,530.00 USD | 348.39 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 292,650.00 USD | 292,650.00 USD | 28,410.00 USD | 13,940.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 229,880.00 USD | 229,880.00 USD | 10,110.00 USD | 5,360.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 338,320.00 USD | 338,320.00 USD | 44,900.00 USD | 0.00 USD | 775.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 263,870.00 USD | 263,870.00 USD | 31,570.00 USD | 1,780.00 USD | 633.92 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 372,430.00 USD | 372,430.00 USD | 34,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 342,190.00 USD | 342,190.00 USD | 40,210.00 USD | 5,090.00 USD | 33,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 388,680.00 USD | 388,680.00 USD | 0.00 USD | 0.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 358,750.00 USD | 358,750.00 USD | 5,860.00 USD | 10,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 402,700.00 USD | 402,700.00 USD | 0.00 USD | 14,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 389,270.00 USD | 389,270.00 USD | 7,210.00 USD | 23,150.00 USD | 155.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 462,230.00 USD | 462,230.00 USD | 33,230.00 USD | 26,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 403,680.00 USD | 403,680.00 USD | 10,040.00 USD | 4,020.00 USD | 352.75 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 493,640.00 USD | 493,640.00 USD | 2,870.00 USD | 28,140.00 USD | 388.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 474,070.00 USD | 474,070.00 USD | 25,750.00 USD | 4,350.00 USD | 40,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 534,020.00 USD | 534,020.00 USD | 0.00 USD | 28,470.00 USD | 11,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 757.09 USD | 1,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.02` | 507,340.00 USD | 507,340.00 USD | 1,130.00 USD | 7,410.00 USD | 24,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 575,990.00 USD | 575,990.00 USD | 0.00 USD | 20,410.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 561,310.00 USD | 561,310.00 USD | 39,370.00 USD | 3,750.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 701,470.00 USD | 701,470.00 USD | 0.00 USD | 81,220.00 USD | 44,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 605,810.00 USD | 605,810.00 USD | 27,370.00 USD | 2,230.00 USD | 14,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 922,410.00 USD | 922,410.00 USD | 56,930.00 USD | 52,290.00 USD | 111,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 706,280.00 USD | 706,280.00 USD | 54,050.00 USD | 5,670.00 USD | 40,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 1,130,000.00 USD | 1,130,000.00 USD | 62,470.00 USD | 56,700.00 USD | 86,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 840,410.00 USD | 840,410.00 USD | 65,800.00 USD | 32,010.00 USD | 36,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,300,000.00 USD | 1,300,000.00 USD | 22,650.00 USD | 124,760.00 USD | 25,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 889,070.00 USD | 889,070.00 USD | 26,670.00 USD | 10,300.00 USD | 11,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,630,000.00 USD | 1,630,000.00 USD | 250,040.00 USD | 50,530.00 USD | 24,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 978,980.00 USD | 978,980.00 USD | 30,050.00 USD | 24,640.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,810,000.00 USD | 1,810,000.00 USD | 134,200.00 USD | 29,810.00 USD | 19,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,170,000.00 USD | 1,170,000.00 USD | 133,530.00 USD | 17,570.00 USD | 40,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,920,000.00 USD | 1,920,000.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,230,000.00 USD | 1,230,000.00 USD | 38,620.00 USD | 104.84 USD | 23,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 2,150,000.00 USD | 2,150,000.00 USD | 216,820.00 USD | 8,290.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 1,310,000.00 USD | 1,310,000.00 USD | 27,040.00 USD | 18,490.00 USD | 29,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 2,450,000.00 USD | 2,450,000.00 USD | 262,550.00 USD | 3,170.00 USD | 42,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,420,000.00 USD | 1,420,000.00 USD | 69,740.00 USD | 7,400.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 2,830,000.00 USD | 2,830,000.00 USD | 178,400.00 USD | 1,290.00 USD | 199,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,440,000.00 USD | 1,440,000.00 USD | 10,510.00 USD | 4,170.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,220,000.00 USD | 3,220,000.00 USD | 279,460.00 USD | 9,430.00 USD | 93,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,450,000.00 USD | 1,450,000.00 USD | 4,050.00 USD | 4,370.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,540,000.00 USD | 3,540,000.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,510,000.00 USD | 1,510,000.00 USD | 14,730.00 USD | 12,770.00 USD | 28,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,800,000.00 USD | 3,800,000.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,540,000.00 USD | 1,540,000.00 USD | 5,920.00 USD | 11,400.00 USD | 13,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,220,000.00 USD | 4,220,000.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,580,000.00 USD | 1,580,000.00 USD | 29,770.00 USD | 7,370.00 USD | 1,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 733.98 USD | 1,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,610,000.00 USD | 4,610,000.00 USD | 199,320.00 USD | 28,070.00 USD | 161,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,610,000.00 USD | 1,610,000.00 USD | 2,310.00 USD | 8,000.00 USD | 17,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,770,000.00 USD | 4,770,000.00 USD | 91,750.00 USD | 29,070.00 USD | 40,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,690,000.00 USD | 1,690,000.00 USD | 62,530.00 USD | 4,130.00 USD | 17,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 5,090,000.00 USD | 5,090,000.00 USD | 140,970.00 USD | 49,780.00 USD | 133,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,720,000.00 USD | 1,720,000.00 USD | 5,710.00 USD | 6,220.00 USD | 19,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 5,250,000.00 USD | 5,250,000.00 USD | 82,020.00 USD | 42,140.00 USD | 36,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,760,000.00 USD | 1,760,000.00 USD | 14,400.00 USD | 979.80 USD | 21,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.06` | 74,410.00 USD | 76,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.06` | 5,610,000.00 USD | 5,610,000.00 USD | 187,610.00 USD | 48,000.00 USD | 121,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,780,000.00 USD | 1,780,000.00 USD | 5,730.00 USD | 2,500.00 USD | 13,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 5,970,000.00 USD | 5,970,000.00 USD | 205,690.00 USD | 63,110.00 USD | 94,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,820,000.00 USD | 1,820,000.00 USD | 27,860.00 USD | 3,010.00 USD | 9,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,360,000.00 USD | 6,360,000.00 USD | 197,680.00 USD | 69,880.00 USD | 118,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,840,000.00 USD | 1,840,000.00 USD | 1,670.00 USD | 8,100.00 USD | 8,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,640,000.00 USD | 6,640,000.00 USD | 131,720.00 USD | 83,000.00 USD | 65,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,850,000.00 USD | 1,850,000.00 USD | 4,600.00 USD | 2,860.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,890,000.00 USD | 6,890,000.00 USD | 102,750.00 USD | 49,310.00 USD | 92,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,870,000.00 USD | 1,870,000.00 USD | 7,180.00 USD | 3,820.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,060,000.00 USD | 7,060,000.00 USD | 77,660.00 USD | 32,860.00 USD | 61,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,900,000.00 USD | 1,900,000.00 USD | 13,480.00 USD | 4,390.00 USD | 6,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,400,000.00 USD | 7,400,000.00 USD | 221,410.00 USD | 30,180.00 USD | 93,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,910,000.00 USD | 1,910,000.00 USD | 6,330.00 USD | 4,110.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,600,000.00 USD | 7,600,000.00 USD | 121,300.00 USD | 33,170.00 USD | 42,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,940,000.00 USD | 1,940,000.00 USD | 16,300.00 USD | 3,170.00 USD | 4,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,820,000.00 USD | 7,820,000.00 USD | 103,500.00 USD | 37,730.00 USD | 83,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,960,000.00 USD | 1,960,000.00 USD | 5,820.00 USD | 4,330.00 USD | 12,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 8,030,000.00 USD | 8,030,000.00 USD | 102,600.00 USD | 21,500.00 USD | 83,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,980,000.00 USD | 1,980,000.00 USD | 4,510.00 USD | 5,370.00 USD | 10,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,180,000.00 USD | 8,180,000.00 USD | 103,110.00 USD | 18,720.00 USD | 27,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,000,000.00 USD | 2,000,000.00 USD | 8,480.00 USD | 3,550.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,450,000.00 USD | 8,450,000.00 USD | 158,650.00 USD | 40,740.00 USD | 69,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,010,000.00 USD | 2,010,000.00 USD | 7,590.00 USD | 4,280.00 USD | 36.19 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,690,000.00 USD | 8,690,000.00 USD | 176,790.00 USD | 26,190.00 USD | 33,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,020,000.00 USD | 2,020,000.00 USD | 8,650.00 USD | 2,530.00 USD | 2,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,810,000.00 USD | 8,810,000.00 USD | 62,710.00 USD | 20,510.00 USD | 38,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,030,000.00 USD | 2,030,000.00 USD | 2,300.00 USD | 2,770.00 USD | 2,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,990,000.00 USD | 8,990,000.00 USD | 46,000.00 USD | 31,940.00 USD | 103,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 2,060,000.00 USD | 2,060,000.00 USD | 17,880.00 USD | 3,990.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,190,000.00 USD | 9,190,000.00 USD | 134,170.00 USD | 28,200.00 USD | 34,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,070,000.00 USD | 2,070,000.00 USD | 4,380.00 USD | 3,550.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,420,000.00 USD | 9,420,000.00 USD | 59,850.00 USD | 54,400.00 USD | 117,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,080,000.00 USD | 2,080,000.00 USD | 2,400.00 USD | 1,680.00 USD | 2,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,580,000.00 USD | 9,580,000.00 USD | 109,670.00 USD | 18,350.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,090,000.00 USD | 2,090,000.00 USD | 7,430.00 USD | 2,540.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,700,000.00 USD | 9,700,000.00 USD | 37,360.00 USD | 24,570.00 USD | 62,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 2,440.00 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,860,000.00 USD | 9,860,000.00 USD | 66,620.00 USD | 37,290.00 USD | 55,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,030,000.00 USD | 10,030,000.00 USD | 71,580.00 USD | 30,090.00 USD | 65,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,260,000.00 USD | 10,260,000.00 USD | 114,820.00 USD | 21,050.00 USD | 92,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,540,000.00 USD | 10,540,000.00 USD | 182,190.00 USD | 62,900.00 USD | 41,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,770,000.00 USD | 10,770,000.00 USD | 118,210.00 USD | 18,440.00 USD | 88,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,900,000.00 USD | 10,900,000.00 USD | 51,230.00 USD | 22,070.00 USD | 57,280.00 USD | `Tier 1 CEX` |
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
| `7D` | `Short Liquidation` | `1.12` | 11,940,000.00 USD | 11,940,000.00 USD | 58,100.00 USD | 5,280.00 USD | 29,870.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.8760` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 6,030.00 USD | 6,200.00 USD | 5,860.00 USD |
| `7D` | `0.8780` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 15,500.00 USD | 50.60 USD | 5,490.00 USD |
| `1D` | `0.8790` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 17,770.00 USD | 8,500.00 USD | 7,060.00 USD |
| `7D` | `0.8800` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 0.00 USD | 3,930.00 USD | 0.00 USD |
| `1D` | `0.8810` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 6,240.00 USD | 3,320.00 USD | 5,560.00 USD |
| `7D` | `0.8820` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 8,660.00 USD | 3,420.00 USD | 0.00 USD |
| `1D` | `0.8830` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 6,600.00 USD | 4,200.00 USD | 36.19 USD |
| `7D` | `0.8840` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 4,540.00 USD | 5,480.00 USD | 1,300.00 USD |
| `1D` | `0.8850` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 7,980.00 USD | 2,370.00 USD | 2,160.00 USD |
| `7D` | `0.8860` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 15,460.00 USD | 7,970.00 USD | 2,570.00 USD |
| `1D` | `0.8870` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 19,130.00 USD | 4,450.00 USD | 8,880.00 USD |
| `7D` | `0.8880` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 7,150.00 USD | 1,990.00 USD | 11,620.00 USD |
| `1D` | `0.8890` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 3,730.00 USD | 3,370.00 USD | 6,690.00 USD |
| `7D` | `0.8900` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 23,060.00 USD | 6,420.00 USD | 20,580.00 USD |
| `1D` | `0.8910` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 1,820.00 USD | 1,560.00 USD | 2,270.00 USD |
| `7D` | `0.8920` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 45,890.00 USD | 9,570.00 USD | 15,680.00 USD |
| `1D` | `0.8930` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 7,320.00 USD | 2,470.00 USD | 1,890.00 USD |
| `7D` | `0.8940` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 7,120.00 USD | 8,030.00 USD | 26,540.00 USD |
| `1D` | `0.8950` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 22.75 USD | 2,460.00 USD | 2,100.00 USD |
| `7D` | `0.8960` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 30,390.00 USD | 9,210.00 USD | 12,150.00 USD |
| `1D` | `0.8970` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 5,360.00 USD | 3,690.00 USD | 1,060.00 USD |
| `7D` | `0.8980` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 31,140.00 USD | 6,910.00 USD | 36,260.00 USD |
| `1D` | `0.8990` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 5,550.00 USD | 757.19 USD | 1,240.00 USD |
| `7D` | `0.9000` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 39,940.00 USD | 14,050.00 USD | 14,850.00 USD |
| `1D` | `0.9010` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 15.65 USD | 39.59 USD | 1,890.00 USD |
| `7D` | `0.9020` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 16,980.00 USD | 11,760.00 USD | 15,220.00 USD |
| `1D` | `0.9030` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 6,430.00 USD | 3,760.00 USD | 4,220.00 USD |
| `7D` | `0.9040` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 17,160.00 USD | 5,930.00 USD | 11,110.00 USD |
| `1D` | `0.9050` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 8,300.00 USD | 3,640.00 USD | 3,200.00 USD |
| `7D` | `0.9060` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 53,450.00 USD | 30,600.00 USD | 41,510.00 USD |
| `1D` | `0.9070` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 3,810.00 USD | 488.01 USD | 803.91 USD |
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
| `1D` | `0.9190` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 2,810.00 USD | 138.43 USD | 54.94 USD |
| `7D` | `0.9200` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 40,100.00 USD | 4,910.00 USD | 22,830.00 USD |
| `1D` | `0.9210` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 1,470.00 USD | 77.80 USD | 2,330.00 USD |
| `7D` | `0.9220` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 15,960.00 USD | 2,370.00 USD | 15,640.00 USD |
| `1D` | `0.9230` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 10,750.00 USD | 2,010.00 USD | 907.53 USD |
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
| `1D` | `0.9350` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 36,430.00 USD | 10,930.00 USD | 13,660.00 USD |
| `7D` | `0.9360` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 59,280.00 USD | 6,250.00 USD | 14,950.00 USD |
| `1D` | `0.9370` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 38,620.00 USD | 12,840.00 USD | 20,310.00 USD |
| `7D` | `0.9380` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 20,200.00 USD | 20,670.00 USD | 12,240.00 USD |
| `1D` | `0.9390` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 17,600.00 USD | 14,430.00 USD | 14,430.00 USD |
| `7D` | `0.9400` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 26,270.00 USD | 6,010.00 USD | 7,370.00 USD |
| `1D` | `0.9410` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 45,250.00 USD | 15,190.00 USD | 2,190.00 USD |
| `7D` | `0.9420` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 51,440.00 USD | 21,220.00 USD | 10,090.00 USD |
| `1D` | `0.9430` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 21,430.00 USD | 8,230.00 USD | 3,110.00 USD |
| `7D` | `0.9440` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 57,220.00 USD | 26,910.00 USD | 26,070.00 USD |
| `1D` | `0.9450` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 41,820.00 USD | 22,990.00 USD | 41,780.00 USD |
| `7D` | `0.9460` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 80,430.00 USD | 19,530.00 USD | 44,800.00 USD |
| `1D` | `0.9470` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 80,990.00 USD | 27,830.00 USD | 40,860.00 USD |
| `7D` | `0.9480` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 202,170.00 USD | 42,900.00 USD | 92,480.00 USD |
| `1D` | `0.9490` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 77,380.00 USD | 18,700.00 USD | 28,330.00 USD |
| `7D` | `0.9500` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 125,620.00 USD | 46,290.00 USD | 114,560.00 USD |
| `1D` | `0.9510` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 35,280.00 USD | 33,660.00 USD | 43,040.00 USD |
| `7D` | `0.9520` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 144,770.00 USD | 19,800.00 USD | 57,660.00 USD |
| `1D` | `0.9530` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 55,340.00 USD | 18,390.00 USD | 21,850.00 USD |
| `7D` | `0.9540` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 116,590.00 USD | 92,780.00 USD | 108,960.00 USD |
| `1D` | `0.9550` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 81,780.00 USD | 37,060.00 USD | 36,990.00 USD |
| `7D` | `0.9560` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 207,570.00 USD | 32,950.00 USD | 87,460.00 USD |
| `1D` | `0.9570` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 113,120.00 USD | 38,550.00 USD | 47,580.00 USD |
| `7D` | `0.9580` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 107,300.00 USD | 48,150.00 USD | 119,950.00 USD |
| `1D` | `0.9590` | 956,900.00 USD | 0.00 USD | 956,900.00 USD | 59,310.00 USD | 22,860.00 USD | 31,870.00 USD |
| `7D` | `0.9600` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 222,250.00 USD | 82,170.00 USD | 59,710.00 USD |
| `1D` | `0.9610` | 842,860.00 USD | 0.00 USD | 842,860.00 USD | 62,360.00 USD | 27,360.00 USD | 12,190.00 USD |
| `7D` | `0.9620` | 968,430.00 USD | 0.00 USD | 968,430.00 USD | 140,700.00 USD | 46,240.00 USD | 26,080.00 USD |
| `1D` | `0.9630` | 740,950.00 USD | 0.00 USD | 740,950.00 USD | 43,690.00 USD | 24,730.00 USD | 24,780.00 USD |
| `7D` | `0.9640` | 755,410.00 USD | 0.00 USD | 755,410.00 USD | 104,730.00 USD | 778.20 USD | 6,950.00 USD |
| `1D` | `0.9650` | 647,750.00 USD | 0.00 USD | 647,750.00 USD | 56,900.00 USD | 14,680.00 USD | 31,900.00 USD |
| `7D` | `0.9660` | 642,950.00 USD | 0.00 USD | 642,950.00 USD | 40,050.00 USD | 9,550.00 USD | 31,400.00 USD |
| `1D` | `0.9670` | 544,270.00 USD | 0.00 USD | 544,270.00 USD | 69,000.00 USD | 19,740.00 USD | 36,040.00 USD |
| `7D` | `0.9680` | 561,960.00 USD | 0.00 USD | 561,960.00 USD | 26,480.00 USD | 4,670.00 USD | 36,940.00 USD |
| `1D` | `0.9690` | 419,500.00 USD | 0.00 USD | 419,500.00 USD | 43,730.00 USD | 30,170.00 USD | 31,220.00 USD |
| `7D` | `0.9700` | 493,870.00 USD | 0.00 USD | 493,870.00 USD | 33,960.00 USD | 25,160.00 USD | 36,880.00 USD |
| `1D` | `0.9710` | 314,380.00 USD | 0.00 USD | 314,380.00 USD | 60,380.00 USD | 19,100.00 USD | 21,290.00 USD |
| `7D` | `0.9720` | 397,870.00 USD | 0.00 USD | 397,870.00 USD | 53,850.00 USD | 0.00 USD | 9,610.00 USD |
| `1D` | `0.9730` | 213,590.00 USD | 0.00 USD | 213,590.00 USD | 23,620.00 USD | 691.66 USD | 13,310.00 USD |
| `7D` | `0.9740` | 334,420.00 USD | 0.00 USD | 334,420.00 USD | 0.00 USD | 16,590.00 USD | 8,630.00 USD |
| `1D` | `0.9750` | 175,970.00 USD | 0.00 USD | 175,970.00 USD | 16,060.00 USD | 23,220.00 USD | 15,960.00 USD |
| `7D` | `0.9760` | 309,200.00 USD | 0.00 USD | 309,200.00 USD | 15,320.00 USD | 5,480.00 USD | 9,280.00 USD |
| `1D` | `0.9770` | 120,730.00 USD | 0.00 USD | 120,730.00 USD | 35,620.00 USD | 2,870.00 USD | 9,980.00 USD |
| `7D` | `0.9780` | 279,110.00 USD | 0.00 USD | 279,110.00 USD | 0.00 USD | 0.00 USD | 24,280.00 USD |
| `1D` | `0.9790` | 72,270.00 USD | 0.00 USD | 72,270.00 USD | 819.00 USD | 0.00 USD | 7,800.00 USD |
| `7D` | `0.9800` | 254,830.00 USD | 0.00 USD | 254,830.00 USD | 0.00 USD | 0.00 USD | 151,540.00 USD |
| `1D` | `0.9810` | 63,650.00 USD | 0.00 USD | 63,650.00 USD | 0.00 USD | 376.40 USD | 8,930.00 USD |
| `7D` | `0.9820` | 103,280.00 USD | 0.00 USD | 103,280.00 USD | 10,090.00 USD | 0.00 USD | 72,280.00 USD |
| `1D` | `0.9830` | 54,340.00 USD | 0.00 USD | 54,340.00 USD | 15,980.00 USD | 11,780.00 USD | 15,270.00 USD |
| `7D` | `0.9840` | 20,920.00 USD | 0.00 USD | 20,920.00 USD | 0.00 USD | 0.00 USD | 20,920.00 USD |
| `1D` | `0.9850` | 11,310.00 USD | 0.00 USD | 11,310.00 USD | 575.70 USD | 0.00 USD | 10,740.00 USD |
| `1D` | `0.9860` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9860` | 803.95 USD | 803.95 USD | 0.00 USD | 0.00 USD | 0.00 USD | 803.95 USD |
| `7D` | `0.9860` | 1,610.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 803.95 USD |
| `7D` | `0.9880` | 42,530.00 USD | 42,530.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 901.60 USD |
| `1D` | `0.9890` | 6,840.00 USD | 6,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,840.00 USD |
| `7D` | `0.9900` | 43,430.00 USD | 43,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 906.61 USD |
| `1D` | `0.9910` | 77,040.00 USD | 77,040.00 USD | 0.00 USD | 50,430.00 USD | 0.00 USD | 19,770.00 USD |
| `7D` | `0.9920` | 63,870.00 USD | 63,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,440.00 USD |
| `1D` | `0.9930` | 97,390.00 USD | 97,390.00 USD | 0.00 USD | 6,920.00 USD | 13,250.00 USD | 191.64 USD |
| `1D` | `0.9950` | 99,020.00 USD | 99,020.00 USD | 0.00 USD | 0.00 USD | 1,630.00 USD | 0.00 USD |
| `7D` | `0.9960` | 139,320.00 USD | 139,320.00 USD | 0.00 USD | 32,670.00 USD | 0.00 USD | 42,770.00 USD |
| `1D` | `0.9970` | 127,240.00 USD | 127,240.00 USD | 0.00 USD | 26,250.00 USD | 1,000.00 USD | 970.29 USD |
| `7D` | `0.9980` | 196,230.00 USD | 196,230.00 USD | 0.00 USD | 52,700.00 USD | 0.00 USD | 4,210.00 USD |
| `1D` | `0.9990` | 142,880.00 USD | 142,880.00 USD | 0.00 USD | 9,720.00 USD | 3,910.00 USD | 2,010.00 USD |
| `7D` | `1.00` | 249,080.00 USD | 249,080.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.00` | 211,780.00 USD | 211,780.00 USD | 0.00 USD | 41,020.00 USD | 27,530.00 USD | 348.39 USD |
| `7D` | `1.00` | 292,650.00 USD | 292,650.00 USD | 0.00 USD | 28,410.00 USD | 13,940.00 USD | 1,220.00 USD |
| `1D` | `1.00` | 229,880.00 USD | 229,880.00 USD | 0.00 USD | 10,110.00 USD | 5,360.00 USD | 2,630.00 USD |
| `7D` | `1.00` | 338,320.00 USD | 338,320.00 USD | 0.00 USD | 44,900.00 USD | 0.00 USD | 775.10 USD |
| `1D` | `1.00` | 263,870.00 USD | 263,870.00 USD | 0.00 USD | 31,570.00 USD | 1,780.00 USD | 633.92 USD |
| `7D` | `1.01` | 372,430.00 USD | 372,430.00 USD | 0.00 USD | 34,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.01` | 342,190.00 USD | 342,190.00 USD | 0.00 USD | 40,210.00 USD | 5,090.00 USD | 33,010.00 USD |
| `7D` | `1.01` | 388,680.00 USD | 388,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,250.00 USD |
| `1D` | `1.01` | 358,750.00 USD | 358,750.00 USD | 0.00 USD | 5,860.00 USD | 10,700.00 USD | 0.00 USD |
| `7D` | `1.01` | 402,700.00 USD | 402,700.00 USD | 0.00 USD | 0.00 USD | 14,020.00 USD | 0.00 USD |
| `1D` | `1.01` | 389,270.00 USD | 389,270.00 USD | 0.00 USD | 7,210.00 USD | 23,150.00 USD | 155.80 USD |
| `7D` | `1.01` | 462,230.00 USD | 462,230.00 USD | 0.00 USD | 33,230.00 USD | 26,300.00 USD | 0.00 USD |
| `1D` | `1.01` | 403,680.00 USD | 403,680.00 USD | 0.00 USD | 10,040.00 USD | 4,020.00 USD | 352.75 USD |
| `7D` | `1.01` | 493,640.00 USD | 493,640.00 USD | 0.00 USD | 2,870.00 USD | 28,140.00 USD | 388.43 USD |
| `1D` | `1.01` | 474,070.00 USD | 474,070.00 USD | 0.00 USD | 25,750.00 USD | 4,350.00 USD | 40,290.00 USD |
| `7D` | `1.02` | 534,020.00 USD | 534,020.00 USD | 0.00 USD | 0.00 USD | 28,470.00 USD | 11,910.00 USD |
| `1D` | `1.02` | 507,340.00 USD | 507,340.00 USD | 0.00 USD | 1,130.00 USD | 7,410.00 USD | 24,720.00 USD |
| `7D` | `1.02` | 575,990.00 USD | 575,990.00 USD | 0.00 USD | 0.00 USD | 20,410.00 USD | 21,560.00 USD |
| `1D` | `1.02` | 561,310.00 USD | 561,310.00 USD | 0.00 USD | 39,370.00 USD | 3,750.00 USD | 10,850.00 USD |
| `7D` | `1.02` | 701,470.00 USD | 701,470.00 USD | 0.00 USD | 0.00 USD | 81,220.00 USD | 44,250.00 USD |
| `1D` | `1.02` | 605,810.00 USD | 605,810.00 USD | 0.00 USD | 27,370.00 USD | 2,230.00 USD | 14,900.00 USD |
| `7D` | `1.02` | 922,410.00 USD | 922,410.00 USD | 0.00 USD | 56,930.00 USD | 52,290.00 USD | 111,720.00 USD |
| `1D` | `1.02` | 706,280.00 USD | 706,280.00 USD | 0.00 USD | 54,050.00 USD | 5,670.00 USD | 40,750.00 USD |
| `7D` | `1.02` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 62,470.00 USD | 56,700.00 USD | 86,740.00 USD |
| `1D` | `1.02` | 840,410.00 USD | 840,410.00 USD | 0.00 USD | 65,800.00 USD | 32,010.00 USD | 36,320.00 USD |
| `7D` | `1.03` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 22,650.00 USD | 124,760.00 USD | 25,070.00 USD |
| `1D` | `1.03` | 889,070.00 USD | 889,070.00 USD | 0.00 USD | 26,670.00 USD | 10,300.00 USD | 11,680.00 USD |
| `7D` | `1.03` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 250,040.00 USD | 50,530.00 USD | 24,480.00 USD |
| `1D` | `1.03` | 978,980.00 USD | 978,980.00 USD | 0.00 USD | 30,050.00 USD | 24,640.00 USD | 35,230.00 USD |
| `7D` | `1.03` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 134,200.00 USD | 29,810.00 USD | 19,120.00 USD |
| `1D` | `1.03` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 133,530.00 USD | 17,570.00 USD | 40,480.00 USD |
| `7D` | `1.03` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD |
| `1D` | `1.03` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 38,620.00 USD | 104.84 USD | 23,160.00 USD |
| `7D` | `1.03` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 216,820.00 USD | 8,290.00 USD | 4,310.00 USD |
| `1D` | `1.03` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 27,040.00 USD | 18,490.00 USD | 29,910.00 USD |
| `7D` | `1.04` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 262,550.00 USD | 3,170.00 USD | 42,930.00 USD |
| `1D` | `1.04` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 69,740.00 USD | 7,400.00 USD | 32,590.00 USD |
| `7D` | `1.04` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 178,400.00 USD | 1,290.00 USD | 199,090.00 USD |
| `1D` | `1.04` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 10,510.00 USD | 4,170.00 USD | 7,780.00 USD |
| `7D` | `1.04` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 279,460.00 USD | 9,430.00 USD | 93,080.00 USD |
| `1D` | `1.04` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 4,050.00 USD | 4,370.00 USD | 6,280.00 USD |
| `7D` | `1.04` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD |
| `1D` | `1.04` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 14,730.00 USD | 12,770.00 USD | 28,900.00 USD |
| `7D` | `1.04` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD |
| `1D` | `1.04` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 5,920.00 USD | 11,400.00 USD | 13,170.00 USD |
| `7D` | `1.05` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD |
| `1D` | `1.05` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 29,770.00 USD | 7,370.00 USD | 1,860.00 USD |
| `7D` | `1.05` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 199,320.00 USD | 28,070.00 USD | 161,420.00 USD |
| `1D` | `1.05` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 2,310.00 USD | 8,000.00 USD | 17,750.00 USD |
| `7D` | `1.05` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 91,750.00 USD | 29,070.00 USD | 40,740.00 USD |
| `1D` | `1.05` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 62,530.00 USD | 4,130.00 USD | 17,630.00 USD |
| `7D` | `1.05` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 140,970.00 USD | 49,780.00 USD | 133,760.00 USD |
| `1D` | `1.05` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 5,710.00 USD | 6,220.00 USD | 19,270.00 USD |
| `7D` | `1.05` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 82,020.00 USD | 42,140.00 USD | 36,750.00 USD |
| `1D` | `1.05` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 14,400.00 USD | 979.80 USD | 21,350.00 USD |
| `7D` | `1.06` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 187,610.00 USD | 48,000.00 USD | 121,890.00 USD |
| `1D` | `1.06` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 5,730.00 USD | 2,500.00 USD | 13,800.00 USD |
| `7D` | `1.06` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 205,690.00 USD | 63,110.00 USD | 94,960.00 USD |
| `1D` | `1.06` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 27,860.00 USD | 3,010.00 USD | 9,650.00 USD |
| `7D` | `1.06` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 197,680.00 USD | 69,880.00 USD | 118,850.00 USD |
| `1D` | `1.06` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 1,670.00 USD | 8,100.00 USD | 8,130.00 USD |
| `7D` | `1.06` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 131,720.00 USD | 83,000.00 USD | 65,720.00 USD |
| `1D` | `1.06` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 4,600.00 USD | 2,860.00 USD | 2,590.00 USD |
| `7D` | `1.06` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 102,750.00 USD | 49,310.00 USD | 92,130.00 USD |
| `1D` | `1.06` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 7,180.00 USD | 3,820.00 USD | 9,680.00 USD |
| `7D` | `1.07` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 77,660.00 USD | 32,860.00 USD | 61,900.00 USD |
| `1D` | `1.07` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 13,480.00 USD | 4,390.00 USD | 6,100.00 USD |
| `7D` | `1.07` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 221,410.00 USD | 30,180.00 USD | 93,450.00 USD |
| `1D` | `1.07` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 6,330.00 USD | 4,110.00 USD | 6,120.00 USD |
| `7D` | `1.07` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 121,300.00 USD | 33,170.00 USD | 42,480.00 USD |
| `1D` | `1.07` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 16,300.00 USD | 3,170.00 USD | 4,120.00 USD |
| `7D` | `1.07` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 103,500.00 USD | 37,730.00 USD | 83,520.00 USD |
| `1D` | `1.07` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 5,820.00 USD | 4,330.00 USD | 12,130.00 USD |
| `7D` | `1.07` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 102,600.00 USD | 21,500.00 USD | 83,440.00 USD |
| `1D` | `1.07` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 4,510.00 USD | 5,370.00 USD | 10,130.00 USD |
| `7D` | `1.08` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 103,110.00 USD | 18,720.00 USD | 27,400.00 USD |
| `1D` | `1.08` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 8,480.00 USD | 3,550.00 USD | 5,560.00 USD |
| `7D` | `1.08` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 158,650.00 USD | 40,740.00 USD | 69,670.00 USD |
| `1D` | `1.08` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 7,590.00 USD | 4,280.00 USD | 36.19 USD |
| `7D` | `1.08` | 8,690,000.00 USD | 8,690,000.00 USD | 0.00 USD | 176,790.00 USD | 26,190.00 USD | 33,510.00 USD |
| `1D` | `1.08` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 8,650.00 USD | 2,530.00 USD | 2,570.00 USD |
| `7D` | `1.08` | 8,810,000.00 USD | 8,810,000.00 USD | 0.00 USD | 62,710.00 USD | 20,510.00 USD | 38,630.00 USD |
| `1D` | `1.08` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 2,300.00 USD | 2,770.00 USD | 2,730.00 USD |
| `7D` | `1.08` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 46,000.00 USD | 31,940.00 USD | 103,610.00 USD |
| `1D` | `1.08` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 17,880.00 USD | 3,990.00 USD | 6,150.00 USD |
| `7D` | `1.09` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 134,170.00 USD | 28,200.00 USD | 34,220.00 USD |
| `1D` | `1.09` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 4,380.00 USD | 3,550.00 USD | 6,690.00 USD |
| `7D` | `1.09` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 59,850.00 USD | 54,400.00 USD | 117,570.00 USD |
| `1D` | `1.09` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 2,400.00 USD | 1,680.00 USD | 2,270.00 USD |
| `7D` | `1.09` | 9,580,000.00 USD | 9,580,000.00 USD | 0.00 USD | 109,670.00 USD | 18,350.00 USD | 31,220.00 USD |
| `1D` | `1.09` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 7,430.00 USD | 2,540.00 USD | 1,890.00 USD |
| `7D` | `1.09` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 37,360.00 USD | 24,570.00 USD | 62,450.00 USD |
| `1D` | `1.09` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 2,440.00 USD | 2,090.00 USD |
| `7D` | `1.09` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 66,620.00 USD | 37,290.00 USD | 55,440.00 USD |
| `7D` | `1.10` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 71,580.00 USD | 30,090.00 USD | 65,790.00 USD |
| `7D` | `1.10` | 10,260,000.00 USD | 10,260,000.00 USD | 0.00 USD | 114,820.00 USD | 21,050.00 USD | 92,150.00 USD |
| `7D` | `1.10` | 10,540,000.00 USD | 10,540,000.00 USD | 0.00 USD | 182,190.00 USD | 62,900.00 USD | 41,720.00 USD |
| `7D` | `1.10` | 10,770,000.00 USD | 10,770,000.00 USD | 0.00 USD | 118,210.00 USD | 18,440.00 USD | 88,980.00 USD |
| `7D` | `1.10` | 10,900,000.00 USD | 10,900,000.00 USD | 0.00 USD | 51,230.00 USD | 22,070.00 USD | 57,280.00 USD |
| `7D` | `1.11` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 22,290.00 USD | 5,830.00 USD | 12,610.00 USD |
| `7D` | `1.11` | 11,120,000.00 USD | 11,120,000.00 USD | 0.00 USD | 90,280.00 USD | 31,510.00 USD | 54,600.00 USD |
| `7D` | `1.11` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 33,280.00 USD | 36,570.00 USD | 93,640.00 USD |
| `7D` | `1.11` | 11,400,000.00 USD | 11,400,000.00 USD | 0.00 USD | 64,670.00 USD | 26,930.00 USD | 24,380.00 USD |
| `7D` | `1.11` | 11,470,000.00 USD | 11,470,000.00 USD | 0.00 USD | 32,450.00 USD | 36,820.00 USD | 6,220.00 USD |
| `7D` | `1.12` | 11,580,000.00 USD | 11,580,000.00 USD | 0.00 USD | 59,080.00 USD | 33,150.00 USD | 13,270.00 USD |
| `7D` | `1.12` | 11,660,000.00 USD | 11,660,000.00 USD | 0.00 USD | 37,220.00 USD | 17,240.00 USD | 30,330.00 USD |
| `7D` | `1.12` | 11,760,000.00 USD | 11,760,000.00 USD | 0.00 USD | 32,060.00 USD | 41,540.00 USD | 25,240.00 USD |
| `7D` | `1.12` | 11,840,000.00 USD | 11,840,000.00 USD | 0.00 USD | 52,230.00 USD | 16,980.00 USD | 11,540.00 USD |
| `7D` | `1.12` | 11,940,000.00 USD | 11,940,000.00 USD | 0.00 USD | 58,100.00 USD | 5,280.00 USD | 29,870.00 USD |
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
  * Total Open Interest: `208.80M` | Total OI Tokens: `211,854,020.1 DOT`
  * 1h OI Change: `+0.69%` | 4h OI Change: `-2.60%` | 24h OI Change: `-6.29%`
  * Exchange Breakdown: Binance=`36.53M` | Bybit=`24.41M` | OKX=`10.23M` | Hyperliquid=`5.69M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `5.37K` | Last 24h: `7.91K` | Last 3d: `-10.37K` | Last 7d: `-19.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0072%` | **USDT OKX** | `0.0087%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0081%` |
| **USDT MEXC** | `0.0073%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0046%` | **USDT Bitget** | `0.0042%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `51.02%` | `48.98%` | `1.04` | 12,080,000.00 USD |
| `15M` | `Binance` | `53.04%` | `46.96%` | `1.13` | 4,490,000.00 USD |
| `15M` | `OKX` | `57.36%` | `42.64%` | `1.35` | 1,250,000.00 USD |
| `15M` | `Bybit` | `63.03%` | `36.97%` | `1.70` | 1,040,000.00 USD |
| `15M` | `KuCoin` | `44.41%` | `55.59%` | `0.80` | 34,360.00 USD |
| `15M` | `Gate` | `42.86%` | `57.14%` | `0.75` | 198,650.00 USD |
| `15M` | `Bitget` | `61.8%` | `38.2%` | `1.62` | 406,170.00 USD |
| `15M` | `BingX` | `61.06%` | `38.94%` | `1.57` | 720,890.00 USD |
| `15M` | `MEXC` | `48.49%` | `51.51%` | `0.94` | 973,620.00 USD |
| `15M` | `Bitunix` | `36.38%` | `63.62%` | `0.57` | 442,400.00 USD |
| `15M` | `Hyperliquid` | `23%` | `77%` | `0.30` | 1,690,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.29%` | `50.71%` | `0.97` | 116,410.00 USD |
| `15M` | `Crypto.com` | `71.43%` | `28.57%` | `2.50` | 61.63 USD |
| `15M` | `WhiteBIT` | `77.77%` | `22.23%` | `3.50` | 562,240.00 USD |
| `15M` | `HTX` | `59.96%` | `40.04%` | `1.50` | 3,040.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `89.33%` | `10.67%` | `8.37` | 67,160.00 USD |
| `15M` | `Aster` | `15.11%` | `84.89%` | `0.18` | 2,330.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `45.92%` | `54.08%` | `0.85` | 73,320.00 USD |
| `15M` | `Whale Positions` | `53.04%` | `46.96%` | `1.13` | 4,490,000.00 USD |
| `15M` | `Global Accounts` | `51.02%` | `48.98%` | `1.04` | 12,080,000.00 USD |
| `1H` | `DOT` | `59.85%` | `40.15%` | `1.49` | 5,900,000.00 USD |
| `1H` | `Binance` | `61.86%` | `38.14%` | `1.62` | 2,440,000.00 USD |
| `1H` | `OKX` | `71.3%` | `28.7%` | `2.48` | 495,490.00 USD |
| `1H` | `Bybit` | `63.71%` | `36.29%` | `1.76` | 336,850.00 USD |
| `1H` | `KuCoin` | `49.13%` | `50.87%` | `0.97` | 98,300.00 USD |
| `1H` | `Gate` | `42.93%` | `57.07%` | `0.75` | 147,120.00 USD |
| `1H` | `Bitget` | `70.33%` | `29.67%` | `2.37` | 211,360.00 USD |
| `1H` | `BingX` | `51.25%` | `48.75%` | `1.05` | 472,790.00 USD |
| `1H` | `MEXC` | `70.93%` | `29.07%` | `2.44` | 375,120.00 USD |
| `1H` | `Bitunix` | `56.96%` | `43.04%` | `1.32` | 132,350.00 USD |
| `1H` | `Hyperliquid` | `60.31%` | `39.69%` | `1.52` | 25,750.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `59.63%` | `40.37%` | `1.48` | 817,010.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `27.45%` | `72.55%` | `0.38` | 307,690.00 USD |
| `1H` | `HTX` | `34.03%` | `65.97%` | `0.52` | 3,740.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `57.64%` | `42.36%` | `1.36` | 22,660.00 USD |
| `1H` | `Aster` | `62.19%` | `37.81%` | `1.64` | 4,050.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `61.86%` | `38.14%` | `1.62` | 2,440,000.00 USD |
| `1H` | `Global Accounts` | `59.85%` | `40.15%` | `1.49` | 5,900,000.00 USD |
| `4H` | `DOT` | `48.06%` | `51.94%` | `0.93` | 363,600,000.00 USD |
| `4H` | `Binance` | `48.63%` | `51.37%` | `0.95` | 147,610,000.00 USD |
| `4H` | `OKX` | `44.56%` | `55.44%` | `0.80` | 51,950,000.00 USD |
| `4H` | `Bybit` | `46.46%` | `53.54%` | `0.87` | 43,720,000.00 USD |
| `4H` | `KuCoin` | `42.68%` | `57.32%` | `0.74` | 3,360,000.00 USD |
| `4H` | `Gate` | `48.01%` | `51.99%` | `0.92` | 6,770,000.00 USD |
| `4H` | `Bitget` | `44.93%` | `55.07%` | `0.82` | 12,220,000.00 USD |
| `4H` | `BingX` | `47.81%` | `52.19%` | `0.92` | 16,380,000.00 USD |
| `4H` | `MEXC` | `54.59%` | `45.41%` | `1.20` | 21,660,000.00 USD |
| `4H` | `Bitunix` | `45.15%` | `54.85%` | `0.82` | 10,120,000.00 USD |
| `4H` | `Hyperliquid` | `38.97%` | `61.03%` | `0.64` | 25,900,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `47.42%` | `52.58%` | `0.90` | 2,110,000.00 USD |
| `4H` | `Crypto.com` | `40.19%` | `59.81%` | `0.67` | 8,630.00 USD |
| `4H` | `WhiteBIT` | `81.83%` | `18.17%` | `4.50` | 10,620,000.00 USD |
| `4H` | `HTX` | `50.03%` | `49.97%` | `1.00` | 256,480.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `42.88%` | `57.12%` | `0.75` | 6,770,000.00 USD |
| `4H` | `Aster` | `42.31%` | `57.69%` | `0.73` | 655,860.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `57.46%` | `42.54%` | `1.35` | 3,480,000.00 USD |
| `4H` | `Whale Positions` | `48.63%` | `51.37%` | `0.95` | 147,610,000.00 USD |
| `4H` | `Global Accounts` | `48.06%` | `51.94%` | `0.93` | 363,600,000.00 USD |


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
| `5:00 UTC` | `0.9858` | `0.9858` | `0.9858` | `0.9873` | `0.9852` | 150,320.02 USD | 70,332.96 USD | 79,987.06 USD | -9,654.10 USD | `-6.42%` | `2B / 2S` |

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
| `5m` | -6,020.00 USD | 11,910.00 USD | **`ACCUMULATION`** |
| `15m` | -3,410.00 USD | 130,130.00 USD | **`ACCUMULATION`** |
| `30m` | 49,580.00 USD | 291,560.00 USD | **`ACCUMULATION`** |
| `1h` | 60,570.00 USD | 924,790.00 USD | **`ACCUMULATION`** |
| `2h` | -55,840.00 USD | 262,000.00 USD | **`ACCUMULATION`** |
| `4h` | -25,390.00 USD | -444,680.00 USD | **`DISTRIBUTION`** |
| `6h` | -67,390.00 USD | -1,290,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -121,490.00 USD | -1,740,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -248,910.00 USD | -1,420,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -400,470.00 USD | -2,640,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,400,000.00 USD | -18,260,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,520,000.00 USD | -72,900,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-6.02K` | 15m=`-3.41K` | 1h=`+60.57K` | 24h=`-400.47K`
* Futures Capital Netflows: 5m=`+11.91K` | 15m=`+130.13K` | 1h=`+924.79K` | 24h=`-2.64M`
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
  * `2026-10-30 00:57:53 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:47:53 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:19:53 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:19:53 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:19:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `0.9141` (Risk Distance: `0.0400` pts)
  * +2.5R Take Profit: `1.05`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9934` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.03` (Risk Distance: `0.0400` pts)
  * +2.5R Take Profit: `0.8934`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9939`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
