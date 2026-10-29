# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 02:51:54 IST` (`2026-10-29 21:21:54 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9180` | **Live Ask Quote**: `0.9390` | **Mid Price**: `0.9285`
- **Spread Points**: `21.00` | **Spread BPS**: `226.17 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.9672` | VWAP Z-Score: `-1.85` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0138` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `28.96` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.05` | Lower -3.00σ Band: `0.8877`
  * Upper +2.51σ Band: `1.03` | Lower -2.51σ Band: `0.9006`
  * Upper +2.01σ Band: `1.02` | Lower -2.01σ Band: `0.9139`
  * Upper +2.00σ Band: `1.02` | Lower -2.00σ Band: `0.9142`
  * Upper +1.28σ Band: `1.00` | Lower -1.28σ Band: `0.9332`
  * Upper +1.00σ Band: `0.9937` | Lower -1.00σ Band: `0.9407`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9400` | EMA-20=`0.9587` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9714` (Slope: `+0.0000`) | EMA-100=`0.9771`
  * Institutional Anchors: EMA-144=`0.9796` | EMA-200=`0.9810` (Slope: `-0.3592`) | EMA-233=`0.9820`
- **Range Boundaries**: 24H High=`1.02` | 24H Low=`0.8800` | Weekly High=`1.03` | Weekly Low=`0.8800`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9190` (Distance: `+1.04%`)
  * Point of Control (POC) = `0.9180` (Distance: `+1.14%`)
  * Value Area Low (VAL) = `0.9092` (Distance: `+2.12%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.01` | Weekly POC=`0.9932` | Weekly VAL=`0.9761`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9190` | Low=`0.9050`
  * London Session (08:00-16:00 UTC): High=`0.9322` | Low=`0.9248`
  * New York Session (13:00-21:00 UTC): High=`0.9341` | Low=`0.9229`
  * Initial Balance (First Hour): IB High=`0.9313` | IB Low=`0.9257`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9248` - `0.9322`
  * Optimal Trade Entry (OTE 0.705): `0.9304`
  * Structural Invalidation Anchor (0.786): `0.9359`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9166` | `0.9272` | `0.9155` | `0.9269` | `973,146` | 898,249.43 USD | 14,133.67 USD | `+1.57%` | -4,034,478.17 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.9267` | `0.9302` | `0.9238` | `0.9289` | `992,394` | 920,085.93 USD | 168,061.68 USD | `+18.27%` | -3,866,416.50 USD | `+0.74` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.9288` | `0.9292` | `0.9283` | `0.9285` | `12,859` | 11,942.91 USD | -4,861.57 USD | `-40.71%` | -3,871,278.07 USD | `+0.36` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9192` | `0.9241` | `0.8892` | `0.9107` | `10,082,852` | 9,166,573.96 USD | -702,958.89 USD | `-7.67%` | -3,620,957.75 USD | `-1.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.9106` | `0.9302` | `0.9075` | `0.9289` | `3,681,802` | 3,388,598.53 USD | -157,295.54 USD | `-4.64%` | -3,778,253.29 USD | `+0.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.9288` | `0.9291` | `0.9285` | `0.9290` | `8,200` | 7,616.35 USD | -2,650.36 USD | `-34.80%` | -3,780,903.65 USD | `+0.37` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9839` | `0.9886` | `0.9780` | `0.9844` | `1,864,944` | 1,834,632.46 USD | 75,709.02 USD | `+4.13%` | -271,595.36 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9845` | `0.9849` | `0.8892` | `0.9107` | `25,741,782` | 23,981,753.25 USD | -3,181,821.86 USD | `-13.27%` | -3,453,417.22 USD | `-3.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.9106` | `0.9302` | `0.9075` | `0.9283` | `3,694,052` | 3,399,976.08 USD | -162,561.85 USD | `-4.78%` | -3,615,979.07 USD | `+0.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | 516,506.12 USD | `-1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -280,559.32 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9285` | `29,436,443` | 27,382,294.69 USD | -3,343,978.97 USD | `-12.21%` | -3,624,538.29 USD | `-2.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9699` | `0.9906` | `0.9674` | `0.9732` | `8,505,701` | 8,320,368.15 USD | 13,201.93 USD | `+0.16%` | 609,018.52 USD | `-1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | 694,082.93 USD | `-0.56` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | 516,506.12 USD | `-1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -280,559.32 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9285` | `29,436,443` | 27,382,294.69 USD | -3,343,978.97 USD | `-12.21%` | -3,624,538.29 USD | `-2.12` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:45:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9983` | 5,996.93 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale SELL: 6.00K USD at 0.9983 USD [API] | `2026-10-28 07:11:22` |
| `ANNOUNCEMENT` | `INFO` | `0.9959` | 5,157.12 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale SELL: 5.16K USD at 0.9959 USD [API] | `2026-10-28 07:15:20` |
| `ANNOUNCEMENT` | `INFO` | `1.00` | 6,571.94 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale BUY: 6.57K USD at 1.0043 USD [API] | `2026-10-28 08:00:01` |


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
| `Live` | `Long Liquidation` | `0.2215` | 110.75 USD | 342,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3525` | 142.30 USD | 341,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3595` | 794.14 USD | 341,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4145` | 31,090.00 USD | 341,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 2,790.00 USD | 309,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4385` | 2,500.00 USD | 307,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4695` | 2,580.00 USD | 304,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5115` | 606.38 USD | 302,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 4,130.00 USD | 301,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5355` | 212.33 USD | 297,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5605` | 35,030.00 USD | 297,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5665` | 2,240.00 USD | 262,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 577.36 USD | 259,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 137.53 USD | 259,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5955` | 3,390.00 USD | 259,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6055` | 2,260.00 USD | 255,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6065` | 1,800.00 USD | 253,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 105.96 USD | 251,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 147.48 USD | 251,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6245` | 525.77 USD | 251,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 757.80 USD | 250,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 106.00 USD | 250,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 2,090.00 USD | 250,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 20,270.00 USD | 247,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 104.60 USD | 227,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6435` | 253.09 USD | 227,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 4,230.00 USD | 227,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 461.93 USD | 223,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 149.44 USD | 222,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6605` | 210.90 USD | 222,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6635` | 1,200.00 USD | 222,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 63,890.00 USD | 221,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 423.10 USD | 157,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 512.97 USD | 156,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6955` | 322.16 USD | 156,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7055` | 176.38 USD | 155,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 16,520.00 USD | 155,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 988.87 USD | 139,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 397.93 USD | 138,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 1,090.00 USD | 137,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 291.18 USD | 136,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 2,300.00 USD | 136,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,140.00 USD | 134,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7365` | 736.50 USD | 133,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 283.30 USD | 132,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7455` | 8,590.00 USD | 131,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 331.18 USD | 123,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 1,400.00 USD | 123,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 2,390.00 USD | 121,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7605` | 834.88 USD | 119,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7735` | 172.80 USD | 118,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7785` | 1,710.00 USD | 118,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7835` | 55,630.00 USD | 116,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7855` | 1,280.00 USD | 60,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 292.03 USD | 59,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7890` | 1,660,000.00 USD | 1,660,000.00 USD | 7,140.00 USD | 2,210.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7895` | 20,380.00 USD | 59,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7910` | 1,650,000.00 USD | 1,650,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.7920` | 810,860.00 USD | 810,860.00 USD | 6,470.00 USD | 1,650.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7930` | 1,620,000.00 USD | 1,620,000.00 USD | 20,360.00 USD | 1,250.00 USD | 6,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.7940` | 797,680.00 USD | 797,680.00 USD | 1,860.00 USD | 595.59 USD | 965.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7950` | 1,600,000.00 USD | 1,600,000.00 USD | 3,290.00 USD | 4,710.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.7960` | 794,260.00 USD | 794,260.00 USD | 222.45 USD | 2,470.00 USD | 1,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7965` | 106.49 USD | 38,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7970` | 1,570,000.00 USD | 1,570,000.00 USD | 10,100.00 USD | 1,130.00 USD | 522.30 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.7980` | 790,500.00 USD | 790,500.00 USD | 1,140.00 USD | 22.38 USD | 494.59 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7990` | 1,560,000.00 USD | 1,560,000.00 USD | 20,360.00 USD | 6,180.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8000` | 788,850.00 USD | 788,850.00 USD | 7.83 USD | 5.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8010` | 1,520,000.00 USD | 1,520,000.00 USD | 5,420.00 USD | 5,300.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8020` | 787,640.00 USD | 787,640.00 USD | 2,290.00 USD | 1,600.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8025` | 238.90 USD | 38,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8030` | 1,510,000.00 USD | 1,510,000.00 USD | 4,550.00 USD | 2,260.00 USD | 9,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8040` | 781,630.00 USD | 781,630.00 USD | 813.73 USD | 993.93 USD | 952.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8050` | 1,490,000.00 USD | 1,490,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8060` | 778,870.00 USD | 778,870.00 USD | 536.61 USD | 845.93 USD | 53.10 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8065` | 13,340.00 USD | 38,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8070` | 1,470,000.00 USD | 1,470,000.00 USD | 12,160.00 USD | 4,660.00 USD | 6,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8080` | 777,430.00 USD | 777,430.00 USD | 4,130.00 USD | 657.69 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8090` | 1,450,000.00 USD | 1,450,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8100` | 770,860.00 USD | 770,860.00 USD | 1,940.00 USD | 14.30 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8110` | 1,440,000.00 USD | 1,440,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8120` | 765,360.00 USD | 765,360.00 USD | 821.06 USD | 258.31 USD | 44.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8130` | 1,430,000.00 USD | 1,430,000.00 USD | 14,060.00 USD | 2,970.00 USD | 8,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 25,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8140` | 764,240.00 USD | 764,240.00 USD | 4,760.00 USD | 30.50 USD | 796.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8150` | 1,410,000.00 USD | 1,410,000.00 USD | 5,990.00 USD | 7,330.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8160` | 758,660.00 USD | 758,660.00 USD | 0.00 USD | 182.45 USD | 26.89 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8170` | 1,390,000.00 USD | 1,390,000.00 USD | 10,780.00 USD | 2,430.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8180` | 758,450.00 USD | 758,450.00 USD | 9,320.00 USD | 6.25 USD | 96.08 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8190` | 1,370,000.00 USD | 1,370,000.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8200` | 749,020.00 USD | 749,020.00 USD | 1,260.00 USD | 0.00 USD | 435.27 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8205` | 200.69 USD | 24,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8210` | 1,350,000.00 USD | 1,350,000.00 USD | 7,510.00 USD | 3,190.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 24,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8220` | 747,330.00 USD | 747,330.00 USD | 0.00 USD | 0.00 USD | 471.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8230` | 1,330,000.00 USD | 1,330,000.00 USD | 29,430.00 USD | 4,620.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8240` | 746,850.00 USD | 746,850.00 USD | 8,060.00 USD | 3,640.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8250` | 1,290,000.00 USD | 1,290,000.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8255` | 4,100.00 USD | 22,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8260` | 728,350.00 USD | 728,350.00 USD | 0.00 USD | 5,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 1,280,000.00 USD | 1,280,000.00 USD | 4,320.00 USD | 1,970.00 USD | 616.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8290` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8310` | 1,270,000.00 USD | 1,270,000.00 USD | 9,280.00 USD | 1,520.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8330` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 3,360.00 USD | 77.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8350` | 1,250,000.00 USD | 1,250,000.00 USD | 2,200.00 USD | 0.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 18,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8370` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 36.87 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8390` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 798.38 USD | 539.92 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8400` | 722,440.00 USD | 722,440.00 USD | 458.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8410` | 1,250,000.00 USD | 1,250,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,240.00 USD | 18,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 721,980.00 USD | 721,980.00 USD | 0.00 USD | 149.63 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8430` | 1,250,000.00 USD | 1,250,000.00 USD | 6,590.00 USD | 3,840.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8440` | 721,830.00 USD | 721,830.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8450` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 24.80 USD | 474.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8470` | 1,230,000.00 USD | 1,230,000.00 USD | 7,900.00 USD | 949.62 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8490` | 1,220,000.00 USD | 1,220,000.00 USD | 731.45 USD | 137.03 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 16,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 719,870.00 USD | 719,870.00 USD | 421.90 USD | 61.55 USD | 206.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 1,220,000.00 USD | 1,220,000.00 USD | 5,480.00 USD | 109.15 USD | 4,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8520` | 719,180.00 USD | 719,180.00 USD | 0.00 USD | 1,940.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 1,210,000.00 USD | 1,210,000.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8540` | 714,770.00 USD | 714,770.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 1,200,000.00 USD | 1,200,000.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8560` | 712,650.00 USD | 712,650.00 USD | 2,040.00 USD | 199.60 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8565` | 1,110.00 USD | 15,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8570` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 944.22 USD | 577.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 1,530.00 USD | 14,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8580` | 710,420.00 USD | 710,420.00 USD | 250.65 USD | 0.00 USD | 182.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8590` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8600` | 709,980.00 USD | 709,980.00 USD | 5,860.00 USD | 1,030.00 USD | 251.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8610` | 1,200,000.00 USD | 1,200,000.00 USD | 7,320.00 USD | 2,950.00 USD | 467.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8620` | 702,840.00 USD | 702,840.00 USD | 7,410.00 USD | 24.95 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8625` | 309.55 USD | 12,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8630` | 1,190,000.00 USD | 1,190,000.00 USD | 758.91 USD | 2,590.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 12,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 695,400.00 USD | 695,400.00 USD | 5,790.00 USD | 1,940.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 12,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8650` | 1,180,000.00 USD | 1,180,000.00 USD | 6,720.00 USD | 0.00 USD | 184.85 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8660` | 683,880.00 USD | 683,880.00 USD | 0.00 USD | 20.18 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 118.54 USD | 11,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8670` | 1,170,000.00 USD | 1,170,000.00 USD | 12,100.00 USD | 3,240.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8680` | 683,860.00 USD | 683,860.00 USD | 3,320.00 USD | 3,550.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8690` | 1,150,000.00 USD | 1,150,000.00 USD | 25,250.00 USD | 1,950.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 10,740.00 USD | 11,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8700` | 668,270.00 USD | 668,270.00 USD | 21,170.00 USD | 3,580.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8710` | 1,110,000.00 USD | 1,110,000.00 USD | 7,370.00 USD | 1,110.00 USD | 13,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8720` | 638,760.00 USD | 638,760.00 USD | 32,240.00 USD | 26.70 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 2,270.00 USD | 295.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 600,280.00 USD | 600,280.00 USD | 6,780.00 USD | 3,080.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 587,390.00 USD | 587,390.00 USD | 16,620.00 USD | 3,510.00 USD | 4,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 171.88 USD | 1,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8770` | 1,080,000.00 USD | 1,080,000.00 USD | 52,140.00 USD | 16,130.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8780` | 562,870.00 USD | 562,870.00 USD | 24,840.00 USD | 15,510.00 USD | 27,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 1,010,000.00 USD | 1,010,000.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8795` | 948.01 USD | 948.01 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8800` | 495,420.00 USD | 495,420.00 USD | 40,040.00 USD | 12,830.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 1,000,000.00 USD | 1,000,000.00 USD | 228.30 USD | 167.73 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8820` | 437,060.00 USD | 437,060.00 USD | 8,950.00 USD | 11,150.00 USD | 150.13 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8830` | 1,000,000.00 USD | 1,000,000.00 USD | 8,430.00 USD | 5,730.00 USD | 468.81 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 416,820.00 USD | 416,820.00 USD | 7,440.00 USD | 1,810.00 USD | 1,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8850` | 989,460.00 USD | 989,460.00 USD | 8,630.00 USD | 5,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8860` | 406,540.00 USD | 406,540.00 USD | 5,930.00 USD | 1,700.00 USD | 8,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8870` | 974,870.00 USD | 974,870.00 USD | 19,060.00 USD | 5,060.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8880` | 390,720.00 USD | 390,720.00 USD | 17,470.00 USD | 4,160.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8890` | 943,280.00 USD | 943,280.00 USD | 13,840.00 USD | 5,510.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8900` | 359,330.00 USD | 359,330.00 USD | 50,120.00 USD | 4,210.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8910` | 910,060.00 USD | 910,060.00 USD | 30,650.00 USD | 10,730.00 USD | 22,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8920` | 300,010.00 USD | 300,010.00 USD | 4,920.00 USD | 3,110.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8930` | 845,960.00 USD | 845,960.00 USD | 24,780.00 USD | 5,820.00 USD | 10,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8940` | 290,030.00 USD | 290,030.00 USD | 25,200.00 USD | 0.00 USD | 966.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8950` | 805,260.00 USD | 805,260.00 USD | 7,380.00 USD | 29,250.00 USD | 26,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8960` | 263,860.00 USD | 263,860.00 USD | 21,000.00 USD | 15,480.00 USD | 6,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8970` | 741,710.00 USD | 741,710.00 USD | 106,410.00 USD | 5,400.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8980` | 220,830.00 USD | 220,830.00 USD | 57,410.00 USD | 10,780.00 USD | 32,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8990` | 600,010.00 USD | 600,010.00 USD | 52,250.00 USD | 23,810.00 USD | 19,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9000` | 119,740.00 USD | 119,740.00 USD | 24,060.00 USD | 30,300.00 USD | 2,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9010` | 504,730.00 USD | 504,730.00 USD | 20,170.00 USD | 11,690.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9020` | 63,000.00 USD | 63,000.00 USD | 4,420.00 USD | 3,120.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9030` | 469,630.00 USD | 469,630.00 USD | 13,100.00 USD | 8,710.00 USD | 26,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9040` | 53,230.00 USD | 53,230.00 USD | 1,580.00 USD | 2,430.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9050` | 421,340.00 USD | 421,340.00 USD | 31,190.00 USD | 3,730.00 USD | 25,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9060` | 43,500.00 USD | 43,500.00 USD | 0.00 USD | 1,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9070` | 360,860.00 USD | 360,860.00 USD | 32,990.00 USD | 857.81 USD | 14,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9080` | 41,880.00 USD | 41,880.00 USD | 0.00 USD | 346.80 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9090` | 312,470.00 USD | 312,470.00 USD | 0.00 USD | 954.68 USD | 6,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9100` | 41,540.00 USD | 41,540.00 USD | 1,380.00 USD | 815.15 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9110` | 305,380.00 USD | 305,380.00 USD | 0.00 USD | 441.10 USD | 16,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9120` | 39,340.00 USD | 39,340.00 USD | 925.04 USD | 315.61 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9130` | 288,490.00 USD | 288,490.00 USD | 0.00 USD | 473.74 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9140` | 38,100.00 USD | 38,100.00 USD | 0.00 USD | 200.33 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9150` | 288,010.00 USD | 288,010.00 USD | 0.00 USD | 515.41 USD | 33,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9160` | 37,900.00 USD | 37,900.00 USD | 0.00 USD | 131.45 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9170` | 254,280.00 USD | 254,280.00 USD | 0.00 USD | 0.00 USD | 15,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9180` | 37,760.00 USD | 37,760.00 USD | 0.00 USD | 132.34 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9190` | 239,020.00 USD | 239,020.00 USD | 0.00 USD | 0.00 USD | 18,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9200` | 37,630.00 USD | 37,630.00 USD | 0.00 USD | 166.12 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9210` | 220,550.00 USD | 220,550.00 USD | 0.00 USD | 0.00 USD | 15,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9220` | 37,470.00 USD | 37,470.00 USD | 14,160.00 USD | 77.74 USD | 14,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9230` | 204,760.00 USD | 204,760.00 USD | 27,030.00 USD | 0.00 USD | 37,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9240` | 9,010.00 USD | 9,010.00 USD | 7,970.00 USD | 1,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9250` | 140,620.00 USD | 140,620.00 USD | 95,150.00 USD | 0.00 USD | 45,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9260` | 92,060.00 USD | 92,060.00 USD | 52,420.00 USD | 1,100.00 USD | 38,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9260` | 184,130.00 USD | 184,130.00 USD | 52,420.00 USD | 1,100.00 USD | 38,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9270` | 82,060.00 USD | 82,060.00 USD | 59,970.00 USD | 0.00 USD | 22,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9280` | 245,190.00 USD | 245,190.00 USD | 47,790.00 USD | 145.20 USD | 13,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9290` | 171,400.00 USD | 171,400.00 USD | 28,390.00 USD | 0.00 USD | 60,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9300` | 310,970.00 USD | 310,970.00 USD | 42,600.00 USD | 221.69 USD | 22,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9310` | 229,850.00 USD | 229,850.00 USD | 31,000.00 USD | 19,860.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9320` | 377,890.00 USD | 377,890.00 USD | 45,470.00 USD | 7,580.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9330` | 343,380.00 USD | 343,380.00 USD | 88,250.00 USD | 0.00 USD | 25,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9340` | 503,500.00 USD | 503,500.00 USD | 71,210.00 USD | 10,860.00 USD | 43,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9350` | 432,350.00 USD | 432,350.00 USD | 71,590.00 USD | 0.00 USD | 17,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9360` | 637,920.00 USD | 637,920.00 USD | 84,420.00 USD | 30,060.00 USD | 19,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9370` | 457,520.00 USD | 457,520.00 USD | 16,340.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9380` | 694,800.00 USD | 694,800.00 USD | 56,080.00 USD | 103.28 USD | 695.88 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9390` | 510,240.00 USD | 510,240.00 USD | 39,250.00 USD | 0.00 USD | 13,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9400` | 739,160.00 USD | 739,160.00 USD | 41,740.00 USD | 0.00 USD | 2,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9410` | 545,320.00 USD | 545,320.00 USD | 29,630.00 USD | 0.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9420` | 796,630.00 USD | 796,630.00 USD | 57,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9430` | 603,330.00 USD | 603,330.00 USD | 45,490.00 USD | 0.00 USD | 12,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9440` | 854,950.00 USD | 854,950.00 USD | 58,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 857,270.00 USD | 857,270.00 USD | 180,850.00 USD | 0.00 USD | 73,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 900,880.00 USD | 900,880.00 USD | 45,730.00 USD | 199.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 1,020,000.00 USD | 1,020,000.00 USD | 114,070.00 USD | 0.00 USD | 51,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9480` | 1,060,000.00 USD | 1,060,000.00 USD | 155,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 1,320,000.00 USD | 1,320,000.00 USD | 116,860.00 USD | 0.00 USD | 178,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 1,120,000.00 USD | 1,120,000.00 USD | 59,460.00 USD | 105.68 USD | 2,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 1,650,000.00 USD | 1,650,000.00 USD | 242,000.00 USD | 9,930.00 USD | 76,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 1,200,000.00 USD | 1,200,000.00 USD | 47,190.00 USD | 13,410.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 1,940.00 USD | 121,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 1,280,000.00 USD | 1,280,000.00 USD | 36,980.00 USD | 8,110.00 USD | 29,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 19,730.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 1,290,000.00 USD | 1,290,000.00 USD | 865.00 USD | 7,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 1,810,000.00 USD | 1,810,000.00 USD | 1,910.00 USD | 0.00 USD | 468.81 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 313.25 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 1,810,000.00 USD | 1,810,000.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9605` | 210.64 USD | 210.64 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9610` | 1,840,000.00 USD | 1,840,000.00 USD | 24,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 1,290,000.00 USD | 1,290,000.00 USD | 5,550.00 USD | 149.63 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 1,850,000.00 USD | 1,850,000.00 USD | 12,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 9,690.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 1,860,000.00 USD | 1,860,000.00 USD | 8,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 1,320,000.00 USD | 1,320,000.00 USD | 2,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9675` | 2,060.00 USD | 2,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9685` | 211.13 USD | 2,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9690` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 11,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 2,050.00 USD | 10,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 1,380,000.00 USD | 1,380,000.00 USD | 23,620.00 USD | 0.00 USD | 23,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 1,900,000.00 USD | 1,900,000.00 USD | 2,910.00 USD | 9,050.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 1,420,000.00 USD | 1,420,000.00 USD | 25,800.00 USD | 5,170.00 USD | 14,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 16,590.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 1,500,000.00 USD | 1,500,000.00 USD | 53,000.00 USD | 13,960.00 USD | 8,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 2,020,000.00 USD | 2,020,000.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 1,560,000.00 USD | 1,560,000.00 USD | 39,740.00 USD | 2,960.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 84,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 1,620,000.00 USD | 1,620,000.00 USD | 29,240.00 USD | 9,580.00 USD | 20,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9810` | 2,230,000.00 USD | 2,230,000.00 USD | 540.00 USD | 0.00 USD | 118,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 1,650,000.00 USD | 1,650,000.00 USD | 15,980.00 USD | 12,160.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 2,400,000.00 USD | 2,400,000.00 USD | 102,710.00 USD | 15,810.00 USD | 52,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 13,190.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 1,780,000.00 USD | 1,780,000.00 USD | 50,550.00 USD | 3,460.00 USD | 19,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 2,520,000.00 USD | 2,520,000.00 USD | 40,020.00 USD | 0.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9875` | 432.33 USD | 2,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9880` | 1,810,000.00 USD | 1,810,000.00 USD | 16,640.00 USD | 0.00 USD | 14,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9890` | 2,540,000.00 USD | 2,540,000.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 1,880,000.00 USD | 1,880,000.00 USD | 57,390.00 USD | 1,300.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9910` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 1,910,000.00 USD | 1,910,000.00 USD | 8,950.00 USD | 2,810.00 USD | 13,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9930` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 1,940,000.00 USD | 1,940,000.00 USD | 12,310.00 USD | 13,250.00 USD | 1,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9950` | 2,640,000.00 USD | 2,640,000.00 USD | 33,790.00 USD | 5,380.00 USD | 42,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 1,960,000.00 USD | 1,960,000.00 USD | 18,530.00 USD | 4,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 2,720,000.00 USD | 2,720,000.00 USD | 69,270.00 USD | 0.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9975` | 218.35 USD | 3,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9980` | 2,010,000.00 USD | 2,010,000.00 USD | 40,410.00 USD | 4,790.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 156.00 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,100,000.00 USD | 2,100,000.00 USD | 59,960.00 USD | 28,860.00 USD | 1,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,770,000.00 USD | 2,770,000.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,100,000.00 USD | 2,100,000.00 USD | 501.30 USD | 0.00 USD | 266.05 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,920,000.00 USD | 2,920,000.00 USD | 105,770.00 USD | 21,740.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,130,000.00 USD | 2,130,000.00 USD | 10,110.00 USD | 9,540.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,950,000.00 USD | 2,950,000.00 USD | 32,430.00 USD | 3,970.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,280,000.00 USD | 2,280,000.00 USD | 101,040.00 USD | 10,140.00 USD | 31,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,020,000.00 USD | 3,020,000.00 USD | 34,110.00 USD | 0.00 USD | 29,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,330,000.00 USD | 2,330,000.00 USD | 17,270.00 USD | 9,160.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,040,000.00 USD | 3,040,000.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,360,000.00 USD | 2,360,000.00 USD | 10,530.00 USD | 14,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,080,000.00 USD | 3,080,000.00 USD | 20,090.00 USD | 14,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,400,000.00 USD | 2,400,000.00 USD | 16,240.00 USD | 25,350.00 USD | 155.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,130,000.00 USD | 3,130,000.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,430,000.00 USD | 2,430,000.00 USD | 5,950.00 USD | 4,370.00 USD | 25,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 26,360.00 USD | 7,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,470,000.00 USD | 2,470,000.00 USD | 20,120.00 USD | 75.20 USD | 20,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,210,000.00 USD | 3,210,000.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,510,000.00 USD | 2,510,000.00 USD | 6,670.00 USD | 8,490.00 USD | 22,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,300,000.00 USD | 3,300,000.00 USD | 315.97 USD | 75,760.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,580,000.00 USD | 2,580,000.00 USD | 44,710.00 USD | 4,370.00 USD | 15,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,440,000.00 USD | 3,440,000.00 USD | 44,170.00 USD | 32,840.00 USD | 68,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,650,000.00 USD | 2,650,000.00 USD | 51,380.00 USD | 3,710.00 USD | 21,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,740,000.00 USD | 3,740,000.00 USD | 66,990.00 USD | 85,890.00 USD | 146,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,780,000.00 USD | 2,780,000.00 USD | 50,330.00 USD | 25,640.00 USD | 53,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,850,000.00 USD | 3,850,000.00 USD | 28,320.00 USD | 48,490.00 USD | 29,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,870,000.00 USD | 2,870,000.00 USD | 52,630.00 USD | 18,370.00 USD | 20,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,160,000.00 USD | 4,160,000.00 USD | 161,070.00 USD | 127,000.00 USD | 25,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,930,000.00 USD | 2,930,000.00 USD | 31,340.00 USD | 10,940.00 USD | 18,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,370,000.00 USD | 4,370,000.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,090,000.00 USD | 3,090,000.00 USD | 95,330.00 USD | 24,510.00 USD | 33,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,580,000.00 USD | 4,580,000.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,200,000.00 USD | 3,200,000.00 USD | 70,060.00 USD | 8,980.00 USD | 35,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,700,000.00 USD | 4,700,000.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,270,000.00 USD | 3,270,000.00 USD | 38,330.00 USD | 9,300.00 USD | 21,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 5,010,000.00 USD | 5,010,000.00 USD | 259,060.00 USD | 8,290.00 USD | 43,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,310,000.00 USD | 3,310,000.00 USD | 18,100.00 USD | 13,840.00 USD | 7,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,320,000.00 USD | 5,320,000.00 USD | 192,080.00 USD | 3,170.00 USD | 109,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,380,000.00 USD | 3,380,000.00 USD | 63,010.00 USD | 3,250.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,680,000.00 USD | 5,680,000.00 USD | 239,580.00 USD | 9,010.00 USD | 117,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,410,000.00 USD | 3,410,000.00 USD | 7,790.00 USD | 7,460.00 USD | 12,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,120,000.00 USD | 6,120,000.00 USD | 276,890.00 USD | 2,090.00 USD | 159,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,440,000.00 USD | 3,440,000.00 USD | 11,290.00 USD | 9,870.00 USD | 8,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,320,000.00 USD | 6,320,000.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,480,000.00 USD | 3,480,000.00 USD | 7,410.00 USD | 9,310.00 USD | 21,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,590,000.00 USD | 6,590,000.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,500,000.00 USD | 3,500,000.00 USD | 21,730.00 USD | 4,160.00 USD | 321.14 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,100,000.00 USD | 7,100,000.00 USD | 178,890.00 USD | 96,370.00 USD | 238,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 733.98 USD | 3,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,520,000.00 USD | 3,520,000.00 USD | 8,930.00 USD | 3,210.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,310,000.00 USD | 7,310,000.00 USD | 116,670.00 USD | 13,780.00 USD | 77,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,590,000.00 USD | 3,590,000.00 USD | 42,790.00 USD | 10,010.00 USD | 13,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,610,000.00 USD | 7,610,000.00 USD | 175,350.00 USD | 43,690.00 USD | 87,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,630,000.00 USD | 3,630,000.00 USD | 23,270.00 USD | 1,310.00 USD | 15,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,820,000.00 USD | 7,820,000.00 USD | 68,590.00 USD | 58,070.00 USD | 74,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,650,000.00 USD | 3,650,000.00 USD | 16,310.00 USD | 365.79 USD | 6,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 8,050,000.00 USD | 8,050,000.00 USD | 125,020.00 USD | 33,860.00 USD | 72,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,670,000.00 USD | 3,670,000.00 USD | 13,640.00 USD | 3,680.00 USD | 4,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,440,000.00 USD | 8,440,000.00 USD | 218,860.00 USD | 70,000.00 USD | 106,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,700,000.00 USD | 3,700,000.00 USD | 29,640.00 USD | 3,000.00 USD | 725.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,900,000.00 USD | 8,900,000.00 USD | 240,060.00 USD | 74,380.00 USD | 145,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,720,000.00 USD | 3,720,000.00 USD | 3,850.00 USD | 4,510.00 USD | 8,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,180,000.00 USD | 9,180,000.00 USD | 140,850.00 USD | 56,310.00 USD | 78,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,730,000.00 USD | 3,730,000.00 USD | 1,990.00 USD | 2,450.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,460,000.00 USD | 9,460,000.00 USD | 141,700.00 USD | 73,690.00 USD | 71,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,750,000.00 USD | 3,750,000.00 USD | 15,200.00 USD | 2,970.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,680,000.00 USD | 9,680,000.00 USD | 90,670.00 USD | 28,390.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 3,770,000.00 USD | 3,770,000.00 USD | 16,000.00 USD | 141.60 USD | 8,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 9,890,000.00 USD | 9,890,000.00 USD | 86,760.00 USD | 43,390.00 USD | 82,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 3,790,000.00 USD | 3,790,000.00 USD | 7,520.00 USD | 4,330.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,190,000.00 USD | 10,190,000.00 USD | 219,670.00 USD | 14,440.00 USD | 62,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 3,800,000.00 USD | 3,800,000.00 USD | 7,140.00 USD | 3,900.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,420,000.00 USD | 10,420,000.00 USD | 141,570.00 USD | 36,670.00 USD | 52,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 3,820,000.00 USD | 3,820,000.00 USD | 9,330.00 USD | 2,350.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,650,000.00 USD | 10,650,000.00 USD | 96,630.00 USD | 42,960.00 USD | 95,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 3,840,000.00 USD | 3,840,000.00 USD | 7,860.00 USD | 4,560.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,840,000.00 USD | 10,840,000.00 USD | 97,650.00 USD | 27,560.00 USD | 60,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 3,850,000.00 USD | 3,850,000.00 USD | 5,350.00 USD | 5,330.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 10,990,000.00 USD | 10,990,000.00 USD | 75,040.00 USD | 29,910.00 USD | 48,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 3,870,000.00 USD | 3,870,000.00 USD | 9,430.00 USD | 4,070.00 USD | 150.13 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,230,000.00 USD | 11,230,000.00 USD | 166,380.00 USD | 21,060.00 USD | 52,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 3,880,000.00 USD | 3,880,000.00 USD | 7,700.00 USD | 1,870.00 USD | 711.93 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,460,000.00 USD | 11,460,000.00 USD | 164,440.00 USD | 26,480.00 USD | 33,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 3,890,000.00 USD | 3,890,000.00 USD | 5,280.00 USD | 1,770.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,660,000.00 USD | 11,660,000.00 USD | 61,330.00 USD | 41,110.00 USD | 100,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 3,900,000.00 USD | 3,900,000.00 USD | 9,180.00 USD | 1,500.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,810,000.00 USD | 11,810,000.00 USD | 86,400.00 USD | 18,540.00 USD | 46,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 3,920,000.00 USD | 3,920,000.00 USD | 8,920.00 USD | 2,900.00 USD | 6,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,040,000.00 USD | 12,040,000.00 USD | 102,510.00 USD | 58,170.00 USD | 69,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 3,930,000.00 USD | 3,930,000.00 USD | 3,630.00 USD | 4,290.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,220,000.00 USD | 12,220,000.00 USD | 71,650.00 USD | 23,140.00 USD | 85,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 3,950,000.00 USD | 3,950,000.00 USD | 9,830.00 USD | 3,220.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,350,000.00 USD | 12,350,000.00 USD | 70,660.00 USD | 25,660.00 USD | 32,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 3,960,000.00 USD | 3,960,000.00 USD | 4,370.00 USD | 93.54 USD | 966.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,510,000.00 USD | 12,510,000.00 USD | 59,760.00 USD | 39,220.00 USD | 62,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 2,490.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,680,000.00 USD | 12,680,000.00 USD | 56,240.00 USD | 22,740.00 USD | 92,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 3,970,000.00 USD | 3,970,000.00 USD | 1,740.00 USD | 3,660.00 USD | 318.21 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 12,830,000.00 USD | 12,830,000.00 USD | 92,660.00 USD | 13,380.00 USD | 38,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 3,970,000.00 USD | 3,970,000.00 USD | 3,620.00 USD | 1,090.00 USD | 4,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 3,980,000.00 USD | 3,980,000.00 USD | 1,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,160,000.00 USD | 13,160,000.00 USD | 188,000.00 USD | 49,370.00 USD | 89,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,340,000.00 USD | 13,340,000.00 USD | 122,300.00 USD | 44,140.00 USD | 15,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,560,000.00 USD | 13,560,000.00 USD | 91,720.00 USD | 19,140.00 USD | 110,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,620,000.00 USD | 13,620,000.00 USD | 22,500.00 USD | 10,390.00 USD | 31,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 13,730,000.00 USD | 13,730,000.00 USD | 51,840.00 USD | 24,280.00 USD | 34,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 13,910,000.00 USD | 13,910,000.00 USD | 80,930.00 USD | 42,230.00 USD | 56,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.11` | 169.86 USD | 4,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,060,000.00 USD | 14,060,000.00 USD | 69,040.00 USD | 16,050.00 USD | 64,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,150,000.00 USD | 14,150,000.00 USD | 20,190.00 USD | 43,570.00 USD | 25,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,200,000.00 USD | 14,200,000.00 USD | 34,700.00 USD | 6,650.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,350,000.00 USD | 14,350,000.00 USD | 68,170.00 USD | 45,980.00 USD | 32,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,410,000.00 USD | 14,410,000.00 USD | 24,700.00 USD | 22,760.00 USD | 13,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.12` | 78,920.00 USD | 82,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,510,000.00 USD | 14,510,000.00 USD | 49,110.00 USD | 30,950.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,610,000.00 USD | 14,610,000.00 USD | 61,780.00 USD | 7,080.00 USD | 25,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,670,000.00 USD | 14,670,000.00 USD | 18,300.00 USD | 10,940.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 14,690,000.00 USD | 14,690,000.00 USD | 14,700.00 USD | 342.11 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 14,810,000.00 USD | 14,810,000.00 USD | 56,500.00 USD | 19,160.00 USD | 45,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,020,000.00 USD | 15,020,000.00 USD | 106,510.00 USD | 12,730.00 USD | 90,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,130,000.00 USD | 15,130,000.00 USD | 77,640.00 USD | 4,280.00 USD | 27,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.13` | 1,480.00 USD | 84,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,220,000.00 USD | 15,220,000.00 USD | 16,300.00 USD | 10,920.00 USD | 61,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,240,000.00 USD | 15,240,000.00 USD | 4,780.00 USD | 4,820.00 USD | 6,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,270,000.00 USD | 15,270,000.00 USD | 2,980.00 USD | 0.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,330,000.00 USD | 15,330,000.00 USD | 36,300.00 USD | 8,480.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,400,000.00 USD | 15,400,000.00 USD | 36,560.00 USD | 1,660.00 USD | 37,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.17` | 2,450.00 USD | 86,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 22,180.00 USD | 109,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 11,730.00 USD | 120,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 513,610.00 USD | 634,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 3,420.00 USD | 637,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 176.31 USD | 638,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 1,810.00 USD | 639,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 779.81 USD | 640,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.63` | 292.58 USD | 640,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 8,240.00 USD | 649,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 300.15 USD | 649,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 247.76 USD | 649,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 333.04 USD | 650,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2215` | 342,050.00 USD | 0.00 USD | 110.75 USD | `-75.68%` | `500.00` |
| `Live` | `Long` | `0.3525` | 341,940.00 USD | 0.00 USD | 142.30 USD | `-61.30%` | `403.70` |
| `Live` | `Long` | `0.3595` | 341,800.00 USD | 0.00 USD | 794.14 USD | `-60.53%` | `2,209.00` |
| `Live` | `Long` | `0.4145` | 341,010.00 USD | 0.00 USD | 31,090.00 USD | `-54.49%` | `75,000.00` |
| `Live` | `Long` | `0.4185` | 309,920.00 USD | 0.00 USD | 2,790.00 USD | `-54.05%` | `6,675.20` |
| `Live` | `Long` | `0.4385` | 307,120.00 USD | 0.00 USD | 2,500.00 USD | `-51.85%` | `5,698.80` |
| `Live` | `Long` | `0.4695` | 304,630.00 USD | 0.00 USD | 2,580.00 USD | `-48.45%` | `5,500.00` |
| `Live` | `Long` | `0.5115` | 302,040.00 USD | 0.00 USD | 606.38 USD | `-43.84%` | `1,185.50` |
| `Live` | `Long` | `0.5125` | 301,440.00 USD | 0.00 USD | 4,130.00 USD | `-43.73%` | `8,067.10` |
| `Live` | `Long` | `0.5355` | 297,300.00 USD | 0.00 USD | 212.33 USD | `-41.20%` | `396.50` |
| `Live` | `Long` | `0.5605` | 297,090.00 USD | 0.00 USD | 35,030.00 USD | `-38.46%` | `62,500.00` |
| `Live` | `Long` | `0.5665` | 262,060.00 USD | 0.00 USD | 2,240.00 USD | `-37.80%` | `3,955.10` |
| `Live` | `Long` | `0.5695` | 259,820.00 USD | 0.00 USD | 577.36 USD | `-37.47%` | `1,013.80` |
| `Live` | `Long` | `0.5895` | 259,240.00 USD | 0.00 USD | 137.53 USD | `-35.27%` | `233.30` |
| `Live` | `Long` | `0.5955` | 259,100.00 USD | 0.00 USD | 3,390.00 USD | `-34.61%` | `5,695.60` |
| `Live` | `Long` | `0.6055` | 255,710.00 USD | 0.00 USD | 2,260.00 USD | `-33.52%` | `3,731.20` |
| `Live` | `Long` | `0.6065` | 253,450.00 USD | 0.00 USD | 1,800.00 USD | `-33.41%` | `2,971.80` |
| `Live` | `Long` | `0.6125` | 251,650.00 USD | 0.00 USD | 105.96 USD | `-32.75%` | `173.00` |
| `Live` | `Long` | `0.6145` | 251,540.00 USD | 0.00 USD | 147.48 USD | `-32.53%` | `240.00` |
| `Live` | `Long` | `0.6245` | 251,400.00 USD | 0.00 USD | 525.77 USD | `-31.43%` | `841.90` |
| `Live` | `Long` | `0.6315` | 250,870.00 USD | 0.00 USD | 757.80 USD | `-30.66%` | `1,200.00` |
| `Live` | `Long` | `0.6355` | 250,110.00 USD | 0.00 USD | 106.00 USD | `-30.22%` | `166.80` |
| `Live` | `Long` | `0.6405` | 250,010.00 USD | 0.00 USD | 2,090.00 USD | `-29.67%` | `3,262.00` |
| `Live` | `Long` | `0.6415` | 247,920.00 USD | 0.00 USD | 20,270.00 USD | `-29.56%` | `31,595.60` |
| `Live` | `Long` | `0.6425` | 227,650.00 USD | 0.00 USD | 104.60 USD | `-29.45%` | `162.80` |
| `Live` | `Long` | `0.6435` | 227,550.00 USD | 0.00 USD | 253.09 USD | `-29.34%` | `393.30` |
| `Live` | `Long` | `0.6465` | 227,290.00 USD | 0.00 USD | 4,230.00 USD | `-29.01%` | `6,539.70` |
| `Live` | `Long` | `0.6475` | 223,060.00 USD | 0.00 USD | 461.93 USD | `-28.90%` | `713.40` |
| `Live` | `Long` | `0.6595` | 222,600.00 USD | 0.00 USD | 149.44 USD | `-27.59%` | `226.60` |
| `Live` | `Long` | `0.6605` | 222,450.00 USD | 0.00 USD | 210.90 USD | `-27.48%` | `319.30` |
| `Live` | `Long` | `0.6635` | 222,240.00 USD | 0.00 USD | 1,200.00 USD | `-27.15%` | `1,805.70` |
| `Live` | `Long` | `0.6725` | 221,040.00 USD | 0.00 USD | 63,890.00 USD | `-26.16%` | `95,000.00` |
| `Live` | `Long` | `0.6775` | 157,160.00 USD | 0.00 USD | 423.10 USD | `-25.61%` | `624.50` |
| `Live` | `Long` | `0.6835` | 156,730.00 USD | 0.00 USD | 512.97 USD | `-24.95%` | `750.50` |
| `Live` | `Long` | `0.6955` | 156,220.00 USD | 0.00 USD | 322.16 USD | `-23.63%` | `463.20` |
| `Live` | `Long` | `0.7055` | 155,900.00 USD | 0.00 USD | 176.38 USD | `-22.54%` | `250.00` |
| `Live` | `Long` | `0.7075` | 155,720.00 USD | 0.00 USD | 16,520.00 USD | `-22.32%` | `23,344.30` |
| `Live` | `Long` | `0.7145` | 139,210.00 USD | 0.00 USD | 988.87 USD | `-21.55%` | `1,384.00` |
| `Live` | `Long` | `0.7235` | 138,220.00 USD | 0.00 USD | 397.93 USD | `-20.56%` | `550.00` |
| `Live` | `Long` | `0.7255` | 137,820.00 USD | 0.00 USD | 1,090.00 USD | `-20.34%` | `1,500.00` |
| `Live` | `Long` | `0.7285` | 136,730.00 USD | 0.00 USD | 291.18 USD | `-20.01%` | `399.70` |
| `Live` | `Long` | `0.7305` | 136,440.00 USD | 0.00 USD | 2,300.00 USD | `-19.79%` | `3,143.00` |
| `Live` | `Long` | `0.7335` | 134,140.00 USD | 0.00 USD | 1,140.00 USD | `-19.46%` | `1,557.80` |
| `Live` | `Long` | `0.7365` | 133,000.00 USD | 0.00 USD | 736.50 USD | `-19.13%` | `1,000.00` |
| `Live` | `Long` | `0.7395` | 132,260.00 USD | 0.00 USD | 283.30 USD | `-18.80%` | `383.10` |
| `Live` | `Long` | `0.7455` | 131,980.00 USD | 0.00 USD | 8,590.00 USD | `-18.14%` | `11,518.80` |
| `Live` | `Long` | `0.7525` | 123,390.00 USD | 0.00 USD | 331.18 USD | `-17.38%` | `440.10` |
| `Live` | `Long` | `0.7535` | 123,060.00 USD | 0.00 USD | 1,400.00 USD | `-17.27%` | `1,859.90` |
| `Live` | `Long` | `0.7555` | 121,660.00 USD | 0.00 USD | 2,390.00 USD | `-17.05%` | `3,161.00` |
| `Live` | `Long` | `0.7605` | 119,270.00 USD | 0.00 USD | 834.88 USD | `-16.50%` | `1,097.80` |
| `Live` | `Long` | `0.7735` | 118,440.00 USD | 0.00 USD | 172.80 USD | `-15.07%` | `223.40` |
| `Live` | `Long` | `0.7785` | 118,270.00 USD | 0.00 USD | 1,710.00 USD | `-14.52%` | `2,190.90` |
| `Live` | `Long` | `0.7835` | 116,560.00 USD | 0.00 USD | 55,630.00 USD | `-13.97%` | `71,003.30` |
| `Live` | `Long` | `0.7855` | 60,930.00 USD | 0.00 USD | 1,280.00 USD | `-13.75%` | `1,634.20` |
| `Live` | `Long` | `0.7865` | 59,640.00 USD | 0.00 USD | 292.03 USD | `-13.64%` | `371.30` |
| `Live` | `Long` | `0.7895` | 59,350.00 USD | 0.00 USD | 20,380.00 USD | `-13.31%` | `25,816.60` |
| `Live` | `Long` | `0.7965` | 38,970.00 USD | 0.00 USD | 106.49 USD | `-12.54%` | `133.70` |
| `Live` | `Long` | `0.8025` | 38,860.00 USD | 0.00 USD | 238.90 USD | `-11.89%` | `297.70` |
| `Live` | `Long` | `0.8065` | 38,630.00 USD | 0.00 USD | 13,340.00 USD | `-11.45%` | `16,544.60` |
| `Live` | `Long` | `0.8135` | 25,280.00 USD | 0.00 USD | 647.79 USD | `-10.68%` | `796.30` |
| `Live` | `Long` | `0.8205` | 24,630.00 USD | 0.00 USD | 200.69 USD | `-9.91%` | `244.60` |
| `Live` | `Long` | `0.8215` | 24,430.00 USD | 0.00 USD | 1,950.00 USD | `-9.80%` | `2,370.70` |
| `Live` | `Long` | `0.8255` | 22,490.00 USD | 0.00 USD | 4,100.00 USD | `-9.36%` | `4,968.90` |
| `Live` | `Long` | `0.8365` | 18,380.00 USD | 0.00 USD | 316.70 USD | `-8.15%` | `378.60` |
| `Live` | `Long` | `0.8415` | 18,070.00 USD | 0.00 USD | 1,240.00 USD | `-7.60%` | `1,469.60` |
| `Live` | `Long` | `0.8495` | 16,830.00 USD | 0.00 USD | 1,260.00 USD | `-6.73%` | `1,486.90` |
| `Live` | `Long` | `0.8565` | 15,570.00 USD | 0.00 USD | 1,110.00 USD | `-5.96%` | `1,295.40` |
| `Live` | `Long` | `0.8575` | 14,460.00 USD | 0.00 USD | 1,530.00 USD | `-5.85%` | `1,779.30` |
| `Live` | `Long` | `0.8625` | 12,930.00 USD | 0.00 USD | 309.55 USD | `-5.30%` | `358.90` |
| `Live` | `Long` | `0.8635` | 12,620.00 USD | 0.00 USD | 208.02 USD | `-5.19%` | `240.90` |
| `Live` | `Long` | `0.8645` | 12,410.00 USD | 0.00 USD | 438.30 USD | `-5.08%` | `507.00` |
| `Live` | `Long` | `0.8665` | 11,980.00 USD | 0.00 USD | 118.54 USD | `-4.86%` | `136.80` |
| `Live` | `Long` | `0.8695` | 11,860.00 USD | 0.00 USD | 10,740.00 USD | `-4.53%` | `12,349.70` |
| `Live` | `Long` | `0.8765` | 1,120.00 USD | 0.00 USD | 171.88 USD | `-3.76%` | `196.10` |
| `Live` | `Long` | `0.8795` | 948.01 USD | 0.00 USD | 948.01 USD | `-3.43%` | `1,077.90` |
| `Live` | `Short` | `0.9605` | 210.64 USD | 210.64 USD | 0.00 USD | `+5.46%` | `219.30` |
| `Live` | `Short` | `0.9675` | 2,270.00 USD | 2,060.00 USD | 0.00 USD | `+6.23%` | `2,129.10` |
| `Live` | `Short` | `0.9685` | 2,480.00 USD | 211.13 USD | 0.00 USD | `+6.34%` | `218.00` |
| `Live` | `Short` | `0.9875` | 2,910.00 USD | 432.33 USD | 0.00 USD | `+8.43%` | `437.80` |
| `Live` | `Short` | `0.9975` | 3,130.00 USD | 218.35 USD | 0.00 USD | `+9.53%` | `218.90` |
| `Live` | `Short` | `1.05` | 3,870.00 USD | 733.98 USD | 0.00 USD | `+15.02%` | `700.70` |
| `Live` | `Short` | `1.11` | 4,040.00 USD | 169.86 USD | 0.00 USD | `+21.82%` | `153.10` |
| `Live` | `Short` | `1.12` | 82,960.00 USD | 78,920.00 USD | 0.00 USD | `+22.92%` | `70,500.00` |
| `Live` | `Short` | `1.13` | 84,440.00 USD | 1,480.00 USD | 0.00 USD | `+24.46%` | `1,306.30` |
| `Live` | `Short` | `1.17` | 86,900.00 USD | 2,450.00 USD | 0.00 USD | `+28.52%` | `2,096.60` |
| `Live` | `Short` | `1.19` | 109,080.00 USD | 22,180.00 USD | 0.00 USD | `+30.50%` | `18,664.00` |
| `Live` | `Short` | `1.32` | 120,810.00 USD | 11,730.00 USD | 0.00 USD | `+45.32%` | `8,862.90` |
| `Live` | `Short` | `1.49` | 634,420.00 USD | 513,610.00 USD | 0.00 USD | `+63.44%` | `345,051.20` |
| `Live` | `Short` | `1.52` | 637,830.00 USD | 3,420.00 USD | 0.00 USD | `+66.73%` | `2,249.30` |
| `Live` | `Short` | `1.54` | 638,010.00 USD | 176.31 USD | 0.00 USD | `+69.37%` | `114.30` |
| `Live` | `Short` | `1.56` | 639,820.00 USD | 1,810.00 USD | 0.00 USD | `+70.90%` | `1,161.90` |
| `Live` | `Short` | `1.56` | 640,600.00 USD | 779.81 USD | 0.00 USD | `+71.45%` | `499.40` |
| `Live` | `Short` | `1.63` | 640,890.00 USD | 292.58 USD | 0.00 USD | `+79.47%` | `179.00` |
| `Live` | `Short` | `1.65` | 649,130.00 USD | 8,240.00 USD | 0.00 USD | `+80.89%` | `5,000.00` |
| `Live` | `Short` | `1.67` | 649,430.00 USD | 300.15 USD | 0.00 USD | `+83.09%` | `180.00` |
| `Live` | `Short` | `1.69` | 649,670.00 USD | 247.76 USD | 0.00 USD | `+85.95%` | `146.30` |
| `Live` | `Short` | `1.74` | 650,010.00 USD | 333.04 USD | 0.00 USD | `+90.56%` | `191.90` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.4015` | 317,240.00 USD | 0.00 USD | 120.45 USD | `-55.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 317,120.00 USD | 0.00 USD | 150.15 USD | `-45.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 316,970.00 USD | 0.00 USD | 1,150.00 USD | `-28.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 315,820.00 USD | 0.00 USD | 781.90 USD | `-23.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 315,040.00 USD | 0.00 USD | 477.38 USD | `-21.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 314,560.00 USD | 0.00 USD | 341.33 USD | `-21.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 314,220.00 USD | 0.00 USD | 972.82 USD | `-20.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 313,250.00 USD | 0.00 USD | 160.20 USD | `-19.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 313,090.00 USD | 0.00 USD | 289.49 USD | `-18.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 312,800.00 USD | 0.00 USD | 14,570.00 USD | `-14.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 298,230.00 USD | 0.00 USD | 274,830.00 USD | `-12.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 23,400.00 USD | 0.00 USD | 108.47 USD | `-12.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 23,290.00 USD | 0.00 USD | 405.75 USD | `-10.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 22,880.00 USD | 0.00 USD | 772.84 USD | `-8.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8495` | 22,110.00 USD | 0.00 USD | 3,470.00 USD | `-6.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 18,640.00 USD | 0.00 USD | 9,180.00 USD | `-6.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 9,460.00 USD | 0.00 USD | 341.94 USD | `-6.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 9,120.00 USD | 0.00 USD | 1,150.00 USD | `-5.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 7,970.00 USD | 0.00 USD | 2,020.00 USD | `-5.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 5,950.00 USD | 0.00 USD | 429.25 USD | `-5.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 5,520.00 USD | 0.00 USD | 1,290.00 USD | `-5.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 4,230.00 USD | 0.00 USD | 518.51 USD | `-4.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8845` | 3,710.00 USD | 0.00 USD | 193.35 USD | `-2.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 3,520.00 USD | 0.00 USD | 223.04 USD | `-2.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 3,300.00 USD | 0.00 USD | 401.86 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 2,900.00 USD | 0.00 USD | 158.51 USD | `-2.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 2,740.00 USD | 0.00 USD | 192.07 USD | `-2.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 2,550.00 USD | 0.00 USD | 195.32 USD | `-1.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9035` | 2,350.00 USD | 0.00 USD | 196.96 USD | `-0.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9045` | 2,150.00 USD | 0.00 USD | 198.18 USD | `-0.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9065` | 1,960.00 USD | 0.00 USD | 198.61 USD | `-0.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9075` | 1,760.00 USD | 0.00 USD | 994.35 USD | `-0.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 762.12 USD | 0.00 USD | 363.40 USD | `-0.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9095` | 398.72 USD | 0.00 USD | 398.72 USD | `-0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9115` | 199.80 USD | 199.80 USD | 0.00 USD | `+0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9155` | 399.29 USD | 199.49 USD | 0.00 USD | `+0.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9195` | 600.75 USD | 201.46 USD | 0.00 USD | `+0.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9205` | 1,510.00 USD | 913.41 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9215` | 1,720.00 USD | 201.90 USD | 0.00 USD | `+1.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9225` | 1,920.00 USD | 201.94 USD | 0.00 USD | `+1.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9275` | 4,040.00 USD | 2,120.00 USD | 0.00 USD | `+1.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9285` | 4,280.00 USD | 246.05 USD | 0.00 USD | `+1.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9295` | 4,690.00 USD | 407.49 USD | 0.00 USD | `+2.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 4,890.00 USD | 203.97 USD | 0.00 USD | `+2.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 5,710.00 USD | 817.62 USD | 0.00 USD | `+2.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 5,910.00 USD | 203.41 USD | 0.00 USD | `+2.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 15,600.00 USD | 9,680.00 USD | 0.00 USD | `+2.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 16,150.00 USD | 555.18 USD | 0.00 USD | `+3.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 16,300.00 USD | 145.43 USD | 0.00 USD | `+3.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 18,030.00 USD | 1,730.00 USD | 0.00 USD | `+3.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 18,410.00 USD | 383.87 USD | 0.00 USD | `+3.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 18,820.00 USD | 414.68 USD | 0.00 USD | `+4.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9525` | 19,210.00 USD | 381.00 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 19,410.00 USD | 207.86 USD | 0.00 USD | `+4.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 23,310.00 USD | 3,900.00 USD | 0.00 USD | `+4.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 23,780.00 USD | 473.56 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 23,950.00 USD | 166.41 USD | 0.00 USD | `+5.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 24,330.00 USD | 376.80 USD | 0.00 USD | `+5.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 26,230.00 USD | 1,910.00 USD | 0.00 USD | `+5.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 26,800.00 USD | 568.75 USD | 0.00 USD | `+5.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 26,960.00 USD | 163.29 USD | 0.00 USD | `+5.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 27,520.00 USD | 554.58 USD | 0.00 USD | `+6.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 27,910.00 USD | 385.74 USD | 0.00 USD | `+6.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9685` | 28,060.00 USD | 153.22 USD | 0.00 USD | `+6.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 50,860.00 USD | 22,800.00 USD | 0.00 USD | `+6.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 62,090.00 USD | 11,230.00 USD | 0.00 USD | `+6.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 72,460.00 USD | 10,370.00 USD | 0.00 USD | `+6.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 72,840.00 USD | 387.83 USD | 0.00 USD | `+6.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 80,480.00 USD | 7,630.00 USD | 0.00 USD | `+6.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9745` | 89,220.00 USD | 8,750.00 USD | 0.00 USD | `+7.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 111,190.00 USD | 21,960.00 USD | 0.00 USD | `+7.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 111,580.00 USD | 396.17 USD | 0.00 USD | `+7.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 112,260.00 USD | 676.53 USD | 0.00 USD | `+7.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9785` | 123,660.00 USD | 11,400.00 USD | 0.00 USD | `+7.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9795` | 123,780.00 USD | 123.61 USD | 0.00 USD | `+7.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 132,140.00 USD | 8,350.00 USD | 0.00 USD | `+7.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 134,200.00 USD | 2,060.00 USD | 0.00 USD | `+7.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 156,360.00 USD | 22,170.00 USD | 0.00 USD | `+8.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 171,430.00 USD | 15,070.00 USD | 0.00 USD | `+8.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9865` | 204,230.00 USD | 32,800.00 USD | 0.00 USD | `+8.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9895` | 239,200.00 USD | 34,970.00 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 242,720.00 USD | 3,520.00 USD | 0.00 USD | `+8.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 274,480.00 USD | 31,750.00 USD | 0.00 USD | `+8.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 274,880.00 USD | 403.06 USD | 0.00 USD | `+9.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 275,660.00 USD | 782.07 USD | 0.00 USD | `+9.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 276,060.00 USD | 403.28 USD | 0.00 USD | `+9.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 281,210.00 USD | 5,140.00 USD | 0.00 USD | `+9.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 318,520.00 USD | 37,310.00 USD | 0.00 USD | `+9.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 319,520.00 USD | 1,000.00 USD | 0.00 USD | `+9.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 360,110.00 USD | 40,590.00 USD | 0.00 USD | `+9.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 360,350.00 USD | 235.79 USD | 0.00 USD | `+10.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 361,690.00 USD | 1,340.00 USD | 0.00 USD | `+10.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 361,920.00 USD | 230.39 USD | 0.00 USD | `+10.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 362,920.00 USD | 1,000.00 USD | 0.00 USD | `+10.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 363,330.00 USD | 409.86 USD | 0.00 USD | `+10.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 363,440.00 USD | 110.95 USD | 0.00 USD | `+10.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 364,060.00 USD | 615.60 USD | 0.00 USD | `+11.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 367,520.00 USD | 3,460.00 USD | 0.00 USD | `+11.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 368,080.00 USD | 561.17 USD | 0.00 USD | `+11.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 368,180.00 USD | 103.07 USD | 0.00 USD | `+11.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 368,580.00 USD | 401.26 USD | 0.00 USD | `+12.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 369,380.00 USD | 804.09 USD | 0.00 USD | `+12.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 369,590.00 USD | 201.52 USD | 0.00 USD | `+12.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 369,790.00 USD | 207.97 USD | 0.00 USD | `+12.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 370,000.00 USD | 201.60 USD | 0.00 USD | `+12.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 370,100.00 USD | 101.51 USD | 0.00 USD | `+12.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 370,310.00 USD | 208.26 USD | 0.00 USD | `+13.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 370,820.00 USD | 516.75 USD | 0.00 USD | `+13.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 371,030.00 USD | 204.93 USD | 0.00 USD | `+13.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 371,380.00 USD | 348.86 USD | 0.00 USD | `+13.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 371,790.00 USD | 413.76 USD | 0.00 USD | `+13.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 372,150.00 USD | 354.91 USD | 0.00 USD | `+14.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 374,050.00 USD | 1,900.00 USD | 0.00 USD | `+14.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 374,260.00 USD | 207.87 USD | 0.00 USD | `+14.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 374,460.00 USD | 207.97 USD | 0.00 USD | `+14.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 375,760.00 USD | 1,290.00 USD | 0.00 USD | `+14.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 375,970.00 USD | 206.97 USD | 0.00 USD | `+15.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 376,070.00 USD | 107.99 USD | 0.00 USD | `+15.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 376,320.00 USD | 247.60 USD | 0.00 USD | `+15.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 451,160.00 USD | 74,840.00 USD | 0.00 USD | `+16.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 451,700.00 USD | 544.88 USD | 0.00 USD | `+17.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 451,860.00 USD | 157.10 USD | 0.00 USD | `+18.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 454,030.00 USD | 2,170.00 USD | 0.00 USD | `+19.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 455,570.00 USD | 1,540.00 USD | 0.00 USD | `+19.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 465,490.00 USD | 9,930.00 USD | 0.00 USD | `+20.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 466,470.00 USD | 976.36 USD | 0.00 USD | `+20.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 467,350.00 USD | 877.63 USD | 0.00 USD | `+21.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 467,520.00 USD | 171.50 USD | 0.00 USD | `+22.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 467,690.00 USD | 171.09 USD | 0.00 USD | `+22.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 470,460.00 USD | 2,770.00 USD | 0.00 USD | `+23.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 472,500.00 USD | 2,040.00 USD | 0.00 USD | `+23.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 475,170.00 USD | 2,670.00 USD | 0.00 USD | `+24.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 475,320.00 USD | 150.90 USD | 0.00 USD | `+26.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 475,470.00 USD | 151.03 USD | 0.00 USD | `+26.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 475,620.00 USD | 151.16 USD | 0.00 USD | `+26.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 475,770.00 USD | 151.29 USD | 0.00 USD | `+26.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 475,920.00 USD | 151.42 USD | 0.00 USD | `+26.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 476,070.00 USD | 151.55 USD | 0.00 USD | `+26.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 476,220.00 USD | 151.69 USD | 0.00 USD | `+26.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 478,270.00 USD | 2,050.00 USD | 0.00 USD | `+27.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 478,380.00 USD | 110.00 USD | 0.00 USD | `+28.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 478,740.00 USD | 356.85 USD | 0.00 USD | `+30.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 479,950.00 USD | 1,210.00 USD | 0.00 USD | `+31.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 522,870.00 USD | 42,930.00 USD | 0.00 USD | `+32.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 524,880.00 USD | 2,000.00 USD | 0.00 USD | `+35.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 526,260.00 USD | 1,380.00 USD | 0.00 USD | `+37.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 526,510.00 USD | 245.41 USD | 0.00 USD | `+40.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 533,860.00 USD | 7,350.00 USD | 0.00 USD | `+41.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 534,270.00 USD | 415.25 USD | 0.00 USD | `+42.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 540,790.00 USD | 6,520.00 USD | 0.00 USD | `+43.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 997,780.00 USD | 456,990.00 USD | 0.00 USD | `+43.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 998,430.00 USD | 655.75 USD | 0.00 USD | `+44.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 1,000,000.00 USD | 1,810.00 USD | 0.00 USD | `+47.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 1,010,000.00 USD | 13,880.00 USD | 0.00 USD | `+47.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 1,020,000.00 USD | 1,250.00 USD | 0.00 USD | `+48.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 1,020,000.00 USD | 2,070.00 USD | 0.00 USD | `+52.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 1,020,000.00 USD | 140.05 USD | 0.00 USD | `+53.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 1,020,000.00 USD | 160.42 USD | 0.00 USD | `+54.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 1,020,000.00 USD | 598.33 USD | 0.00 USD | `+54.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 1,050,000.00 USD | 34,170.00 USD | 0.00 USD | `+57.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 1,050,000.00 USD | 879.84 USD | 0.00 USD | `+63.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 1,050,000.00 USD | 590.88 USD | 0.00 USD | `+65.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 1,060,000.00 USD | 3,050.00 USD | 0.00 USD | `+66.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 1,060,000.00 USD | 297.27 USD | 0.00 USD | `+70.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 1,070,000.00 USD | 8,530.00 USD | 0.00 USD | `+81.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 1,070,000.00 USD | 143.99 USD | 0.00 USD | `+83.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 1,070,000.00 USD | 177.05 USD | 0.00 USD | `+94.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 1,070,000.00 USD | 431.40 USD | 0.00 USD | `+97.69%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7890` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 7,140.00 USD | 2,210.00 USD | 2,800.00 USD |
| `7D` | `0.7910` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD |
| `1D` | `0.7920` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 6,470.00 USD | 1,650.00 USD | 5,060.00 USD |
| `7D` | `0.7930` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 20,360.00 USD | 1,250.00 USD | 6,130.00 USD |
| `1D` | `0.7940` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 1,860.00 USD | 595.59 USD | 965.49 USD |
| `7D` | `0.7950` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 3,290.00 USD | 4,710.00 USD | 14,710.00 USD |
| `1D` | `0.7960` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 222.45 USD | 2,470.00 USD | 1,060.00 USD |
| `7D` | `0.7970` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 10,100.00 USD | 1,130.00 USD | 522.30 USD |
| `1D` | `0.7980` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 1,140.00 USD | 22.38 USD | 494.59 USD |
| `7D` | `0.7990` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 20,360.00 USD | 6,180.00 USD | 13,950.00 USD |
| `1D` | `0.8000` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 7.83 USD | 5.00 USD | 1,200.00 USD |
| `7D` | `0.8010` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 5,420.00 USD | 5,300.00 USD | 2,300.00 USD |
| `1D` | `0.8020` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 2,290.00 USD | 1,600.00 USD | 2,110.00 USD |
| `7D` | `0.8030` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 4,550.00 USD | 2,260.00 USD | 9,770.00 USD |
| `1D` | `0.8040` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 813.73 USD | 993.93 USD | 952.73 USD |
| `7D` | `0.8050` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD |
| `1D` | `0.8060` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 536.61 USD | 845.93 USD | 53.10 USD |
| `7D` | `0.8070` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 12,160.00 USD | 4,660.00 USD | 6,450.00 USD |
| `1D` | `0.8080` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 4,130.00 USD | 657.69 USD | 1,790.00 USD |
| `7D` | `0.8090` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD |
| `1D` | `0.8100` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 1,940.00 USD | 14.30 USD | 3,540.00 USD |
| `7D` | `0.8110` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD |
| `1D` | `0.8120` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 821.06 USD | 258.31 USD | 44.49 USD |
| `7D` | `0.8130` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 14,060.00 USD | 2,970.00 USD | 8,560.00 USD |
| `1D` | `0.8140` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 4,760.00 USD | 30.50 USD | 796.05 USD |
| `7D` | `0.8150` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 5,990.00 USD | 7,330.00 USD | 4,220.00 USD |
| `1D` | `0.8160` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 182.45 USD | 26.89 USD |
| `7D` | `0.8170` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 10,780.00 USD | 2,430.00 USD | 9,670.00 USD |
| `1D` | `0.8180` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 9,280.00 USD | 6.25 USD | 68.61 USD |
| `7D` | `0.8190` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD |
| `1D` | `0.8200` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 1,260.00 USD | 0.00 USD | 435.27 USD |
| `7D` | `0.8210` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 7,510.00 USD | 3,190.00 USD | 10,030.00 USD |
| `1D` | `0.8220` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 471.94 USD |
| `7D` | `0.8230` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 29,430.00 USD | 4,620.00 USD | 1,960.00 USD |
| `1D` | `0.8240` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 8,060.00 USD | 3,640.00 USD | 6,790.00 USD |
| `7D` | `0.8250` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD |
| `1D` | `0.8260` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 0.00 USD | 5,920.00 USD | 0.00 USD |
| `7D` | `0.8270` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 4,320.00 USD | 1,970.00 USD | 616.76 USD |
| `7D` | `0.8290` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD |
| `7D` | `0.8310` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 9,280.00 USD | 1,520.00 USD | 2,110.00 USD |
| `7D` | `0.8330` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 3,360.00 USD | 77.95 USD |
| `1D` | `0.8340` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 7,020.00 USD | 0.00 USD | 5,450.00 USD |
| `7D` | `0.8350` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 2,200.00 USD | 0.00 USD | 1,980.00 USD |
| `1D` | `0.8360` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 14,810.00 USD |
| `7D` | `0.8370` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 36.87 USD | 0.00 USD |
| `7D` | `0.8390` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 798.38 USD | 12,770.00 USD |
| `1D` | `0.8400` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 458.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8410` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD |
| `1D` | `0.8420` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD | 149.63 USD | 0.00 USD |
| `7D` | `0.8430` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 6,590.00 USD | 3,840.00 USD | 4,060.00 USD |
| `1D` | `0.8440` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8450` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD | 24.80 USD | 474.61 USD |
| `7D` | `0.8470` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 7,900.00 USD | 949.62 USD | 2,180.00 USD |
| `7D` | `0.8490` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 731.45 USD | 137.03 USD | 0.00 USD |
| `1D` | `0.8500` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 421.90 USD | 61.55 USD | 206.79 USD |
| `7D` | `0.8510` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 5,480.00 USD | 109.15 USD | 4,660.00 USD |
| `1D` | `0.8520` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD | 1,940.00 USD | 2,470.00 USD |
| `7D` | `0.8530` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD |
| `1D` | `0.8540` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8550` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD |
| `1D` | `0.8560` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 2,040.00 USD | 199.60 USD | 0.00 USD |
| `7D` | `0.8570` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 0.00 USD | 944.22 USD | 577.61 USD |
| `1D` | `0.8580` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 250.65 USD | 0.00 USD | 182.69 USD |
| `7D` | `0.8590` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD |
| `1D` | `0.8600` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 5,860.00 USD | 1,030.00 USD | 251.39 USD |
| `7D` | `0.8610` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 7,320.00 USD | 2,950.00 USD | 467.14 USD |
| `1D` | `0.8620` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 7,410.00 USD | 24.95 USD | 0.00 USD |
| `7D` | `0.8630` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 758.91 USD | 2,590.00 USD | 1,280.00 USD |
| `1D` | `0.8640` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 5,790.00 USD | 1,940.00 USD | 3,790.00 USD |
| `7D` | `0.8650` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 6,720.00 USD | 0.00 USD | 184.85 USD |
| `1D` | `0.8660` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 0.00 USD | 20.18 USD | 0.00 USD |
| `7D` | `0.8670` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 12,100.00 USD | 3,240.00 USD | 10,160.00 USD |
| `1D` | `0.8680` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 3,320.00 USD | 3,550.00 USD | 8,720.00 USD |
| `7D` | `0.8690` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 25,250.00 USD | 1,950.00 USD | 8,040.00 USD |
| `1D` | `0.8700` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 21,170.00 USD | 3,580.00 USD | 4,760.00 USD |
| `7D` | `0.8710` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 7,370.00 USD | 1,110.00 USD | 13,110.00 USD |
| `1D` | `0.8720` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 32,240.00 USD | 26.70 USD | 6,210.00 USD |
| `7D` | `0.8730` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 2,270.00 USD | 295.31 USD |
| `1D` | `0.8740` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 6,780.00 USD | 3,080.00 USD | 3,030.00 USD |
| `7D` | `0.8750` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 6,210.00 USD |
| `1D` | `0.8760` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 16,620.00 USD | 3,510.00 USD | 4,390.00 USD |
| `7D` | `0.8770` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 52,140.00 USD | 16,130.00 USD | 2,760.00 USD |
| `1D` | `0.8780` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 24,840.00 USD | 15,510.00 USD | 27,090.00 USD |
| `7D` | `0.8790` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD |
| `1D` | `0.8800` | 951,300.00 USD | 0.00 USD | 951,300.00 USD | 40,040.00 USD | 12,830.00 USD | 5,490.00 USD |
| `7D` | `0.8810` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 228.30 USD | 167.73 USD | 0.00 USD |
| `1D` | `0.8820` | 892,950.00 USD | 0.00 USD | 892,950.00 USD | 8,950.00 USD | 11,150.00 USD | 150.13 USD |
| `7D` | `0.8830` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 8,430.00 USD | 5,730.00 USD | 469.21 USD |
| `1D` | `0.8840` | 872,700.00 USD | 0.00 USD | 872,700.00 USD | 7,440.00 USD | 1,810.00 USD | 1,030.00 USD |
| `7D` | `0.8850` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 8,630.00 USD | 5,960.00 USD | 0.00 USD |
| `1D` | `0.8860` | 862,430.00 USD | 0.00 USD | 862,430.00 USD | 5,930.00 USD | 1,700.00 USD | 8,190.00 USD |
| `7D` | `0.8870` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 19,060.00 USD | 5,060.00 USD | 7,460.00 USD |
| `1D` | `0.8880` | 846,610.00 USD | 0.00 USD | 846,610.00 USD | 17,470.00 USD | 4,160.00 USD | 9,760.00 USD |
| `7D` | `0.8890` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 13,840.00 USD | 5,510.00 USD | 14,360.00 USD |
| `1D` | `0.8900` | 815,220.00 USD | 0.00 USD | 815,220.00 USD | 67,680.00 USD | 7,010.00 USD | 18,630.00 USD |
| `7D` | `0.8910` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 30,650.00 USD | 10,730.00 USD | 34,270.00 USD |
| `1D` | `0.8920` | 721,900.00 USD | 0.00 USD | 721,900.00 USD | 4,920.00 USD | 3,110.00 USD | 38,970.00 USD |
| `7D` | `0.8930` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 24,780.00 USD | 5,820.00 USD | 10,100.00 USD |
| `1D` | `0.8940` | 674,900.00 USD | 0.00 USD | 674,900.00 USD | 25,200.00 USD | 0.00 USD | 966.50 USD |
| `7D` | `0.8950` | 966,990.00 USD | 0.00 USD | 966,990.00 USD | 7,380.00 USD | 29,250.00 USD | 57,500.00 USD |
| `1D` | `0.8960` | 648,730.00 USD | 0.00 USD | 648,730.00 USD | 21,000.00 USD | 15,480.00 USD | 6,550.00 USD |
| `7D` | `0.8970` | 872,860.00 USD | 0.00 USD | 872,860.00 USD | 106,410.00 USD | 5,400.00 USD | 29,890.00 USD |
| `1D` | `0.8980` | 605,700.00 USD | 0.00 USD | 605,700.00 USD | 57,410.00 USD | 10,780.00 USD | 32,910.00 USD |
| `7D` | `0.8990` | 731,160.00 USD | 0.00 USD | 731,160.00 USD | 52,250.00 USD | 23,810.00 USD | 19,220.00 USD |
| `1D` | `0.9000` | 504,610.00 USD | 0.00 USD | 504,610.00 USD | 24,060.00 USD | 30,300.00 USD | 2,370.00 USD |
| `7D` | `0.9010` | 635,880.00 USD | 0.00 USD | 635,880.00 USD | 20,170.00 USD | 11,690.00 USD | 3,230.00 USD |
| `1D` | `0.9020` | 447,880.00 USD | 0.00 USD | 447,880.00 USD | 4,420.00 USD | 3,120.00 USD | 2,240.00 USD |
| `7D` | `0.9030` | 600,780.00 USD | 0.00 USD | 600,780.00 USD | 13,100.00 USD | 8,710.00 USD | 26,480.00 USD |
| `1D` | `0.9040` | 438,100.00 USD | 0.00 USD | 438,100.00 USD | 1,580.00 USD | 2,430.00 USD | 5,710.00 USD |
| `7D` | `0.9050` | 552,490.00 USD | 0.00 USD | 552,490.00 USD | 31,190.00 USD | 3,730.00 USD | 25,570.00 USD |
| `1D` | `0.9060` | 428,380.00 USD | 0.00 USD | 428,380.00 USD | 0.00 USD | 1,620.00 USD | 0.00 USD |
| `7D` | `0.9070` | 492,010.00 USD | 0.00 USD | 492,010.00 USD | 32,990.00 USD | 857.81 USD | 15,500.00 USD |
| `1D` | `0.9080` | 426,760.00 USD | 0.00 USD | 426,760.00 USD | 35,110.00 USD | 5,950.00 USD | 27,270.00 USD |
| `7D` | `0.9090` | 442,660.00 USD | 0.00 USD | 442,660.00 USD | 0.00 USD | 954.68 USD | 29,250.00 USD |
| `1D` | `0.9100` | 358,430.00 USD | 0.00 USD | 358,430.00 USD | 1,380.00 USD | 815.15 USD | 74,030.00 USD |
| `7D` | `0.9110` | 412,460.00 USD | 0.00 USD | 412,460.00 USD | 0.00 USD | 441.10 USD | 16,450.00 USD |
| `1D` | `0.9120` | 282,190.00 USD | 0.00 USD | 282,190.00 USD | 925.04 USD | 315.61 USD | 0.00 USD |
| `7D` | `0.9130` | 395,560.00 USD | 0.00 USD | 395,560.00 USD | 0.00 USD | 473.74 USD | 61,160.00 USD |
| `1D` | `0.9140` | 280,950.00 USD | 0.00 USD | 280,950.00 USD | 0.00 USD | 200.33 USD | 0.00 USD |
| `7D` | `0.9150` | 333,930.00 USD | 0.00 USD | 333,930.00 USD | 0.00 USD | 515.41 USD | 33,220.00 USD |
| `1D` | `0.9160` | 280,750.00 USD | 0.00 USD | 280,750.00 USD | 0.00 USD | 131.45 USD | 0.00 USD |
| `7D` | `0.9170` | 300,190.00 USD | 0.00 USD | 300,190.00 USD | 0.00 USD | 0.00 USD | 15,250.00 USD |
| `1D` | `0.9180` | 280,620.00 USD | 0.00 USD | 280,620.00 USD | 0.00 USD | 132.34 USD | 0.00 USD |
| `7D` | `0.9190` | 284,940.00 USD | 0.00 USD | 284,940.00 USD | 0.00 USD | 0.00 USD | 18,470.00 USD |
| `1D` | `0.9200` | 280,490.00 USD | 0.00 USD | 280,490.00 USD | 0.00 USD | 166.12 USD | 0.00 USD |
| `7D` | `0.9210` | 266,470.00 USD | 0.00 USD | 266,470.00 USD | 0.00 USD | 0.00 USD | 15,790.00 USD |
| `1D` | `0.9220` | 280,320.00 USD | 0.00 USD | 280,320.00 USD | 14,160.00 USD | 77.74 USD | 14,210.00 USD |
| `7D` | `0.9230` | 250,670.00 USD | 0.00 USD | 250,670.00 USD | 27,030.00 USD | 0.00 USD | 37,100.00 USD |
| `1D` | `0.9240` | 251,870.00 USD | 0.00 USD | 251,870.00 USD | 2,520.00 USD | 1,040.00 USD | 0.00 USD |
| `7D` | `0.9250` | 186,540.00 USD | 0.00 USD | 186,540.00 USD | 95,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9260` | 248,310.00 USD | 0.00 USD | 248,310.00 USD | 0.00 USD | 1,100.00 USD | 16,850.00 USD |
| `7D` | `0.9270` | 91,390.00 USD | 0.00 USD | 91,390.00 USD | 59,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9280` | 230,360.00 USD | 0.00 USD | 230,360.00 USD | 0.00 USD | 145.20 USD | 353.46 USD |
| `7D` | `0.9290` | 31,420.00 USD | 0.00 USD | 31,420.00 USD | 28,390.00 USD | 0.00 USD | 3,020.00 USD |
| `1D` | `0.9300` | 229,860.00 USD | 0.00 USD | 229,860.00 USD | 42,600.00 USD | 221.69 USD | 753.09 USD |
| `7D` | `0.9310` | 53,950.00 USD | 53,950.00 USD | 0.00 USD | 31,000.00 USD | 19,860.00 USD | 3,090.00 USD |
| `7D` | `0.9310` | 107,900.00 USD | 107,900.00 USD | 0.00 USD | 31,000.00 USD | 19,860.00 USD | 3,090.00 USD |
| `1D` | `0.9320` | 186,290.00 USD | 0.00 USD | 186,290.00 USD | 45,470.00 USD | 7,580.00 USD | 7,630.00 USD |
| `7D` | `0.9330` | 197,510.00 USD | 197,510.00 USD | 0.00 USD | 88,250.00 USD | 0.00 USD | 1,360.00 USD |
| `1D` | `0.9340` | 125,620.00 USD | 0.00 USD | 125,620.00 USD | 71,210.00 USD | 10,860.00 USD | 43,550.00 USD |
| `7D` | `0.9350` | 269,870.00 USD | 269,870.00 USD | 0.00 USD | 71,590.00 USD | 0.00 USD | 768.64 USD |
| `1D` | `0.9360` | 134,420.00 USD | 134,420.00 USD | 0.00 USD | 84,420.00 USD | 30,060.00 USD | 19,940.00 USD |
| `1D` | `0.9360` | 268,830.00 USD | 268,830.00 USD | 0.00 USD | 84,420.00 USD | 30,060.00 USD | 19,940.00 USD |
| `7D` | `0.9370` | 287,960.00 USD | 287,960.00 USD | 0.00 USD | 16,340.00 USD | 0.00 USD | 1,760.00 USD |
| `1D` | `0.9380` | 325,720.00 USD | 325,720.00 USD | 0.00 USD | 56,080.00 USD | 103.28 USD | 695.88 USD |
| `7D` | `0.9390` | 336,070.00 USD | 336,070.00 USD | 0.00 USD | 39,250.00 USD | 0.00 USD | 8,860.00 USD |
| `1D` | `0.9400` | 370,070.00 USD | 370,070.00 USD | 0.00 USD | 41,740.00 USD | 0.00 USD | 2,620.00 USD |
| `7D` | `0.9410` | 371,150.00 USD | 371,150.00 USD | 0.00 USD | 29,630.00 USD | 0.00 USD | 5,450.00 USD |
| `1D` | `0.9420` | 427,550.00 USD | 427,550.00 USD | 0.00 USD | 57,470.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9430` | 429,160.00 USD | 429,160.00 USD | 0.00 USD | 45,490.00 USD | 0.00 USD | 12,520.00 USD |
| `1D` | `0.9440` | 485,860.00 USD | 485,860.00 USD | 0.00 USD | 58,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9450` | 684,070.00 USD | 684,070.00 USD | 0.00 USD | 180,850.00 USD | 0.00 USD | 74,060.00 USD |
| `1D` | `0.9460` | 599,780.00 USD | 599,780.00 USD | 0.00 USD | 80,840.00 USD | 5,810.00 USD | 27,270.00 USD |
| `7D` | `0.9470` | 873,170.00 USD | 873,170.00 USD | 0.00 USD | 114,070.00 USD | 0.00 USD | 75,040.00 USD |
| `1D` | `0.9480` | 829,760.00 USD | 829,760.00 USD | 0.00 USD | 155,950.00 USD | 0.00 USD | 74,030.00 USD |
| `7D` | `0.9490` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 116,860.00 USD | 0.00 USD | 178,870.00 USD |
| `1D` | `0.9500` | 891,550.00 USD | 891,550.00 USD | 0.00 USD | 59,460.00 USD | 105.68 USD | 2,230.00 USD |
| `7D` | `0.9510` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 242,000.00 USD | 9,930.00 USD | 138,060.00 USD |
| `1D` | `0.9520` | 977,460.00 USD | 977,460.00 USD | 0.00 USD | 47,190.00 USD | 13,410.00 USD | 25,300.00 USD |
| `7D` | `0.9530` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 1,940.00 USD | 121,100.00 USD |
| `1D` | `0.9540` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 36,850.00 USD | 8,040.00 USD | 29,110.00 USD |
| `7D` | `0.9550` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 19,730.00 USD | 18,890.00 USD |
| `1D` | `0.9560` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 865.00 USD | 7,070.00 USD | 0.00 USD |
| `7D` | `0.9570` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 1,910.00 USD | 0.00 USD | 469.21 USD |
| `1D` | `0.9580` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 313.25 USD |
| `7D` | `0.9590` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9610` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 24,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9620` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 5,550.00 USD | 149.63 USD | 0.00 USD |
| `7D` | `0.9630` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 12,970.00 USD | 0.00 USD | 481.70 USD |
| `1D` | `0.9640` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 17,560.00 USD | 12,490.00 USD | 27,030.00 USD |
| `7D` | `0.9650` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 8,280.00 USD | 0.00 USD | 11,560.00 USD |
| `1D` | `0.9660` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 2,550.00 USD | 0.00 USD | 37,020.00 USD |
| `7D` | `0.9690` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 11,390.00 USD | 30,580.00 USD |
| `1D` | `0.9700` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 2,050.00 USD | 10,450.00 USD |
| `7D` | `0.9710` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD |
| `1D` | `0.9720` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 23,620.00 USD | 0.00 USD | 23,100.00 USD |
| `7D` | `0.9730` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 2,910.00 USD | 9,050.00 USD | 7,510.00 USD |
| `1D` | `0.9740` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 25,800.00 USD | 5,170.00 USD | 14,840.00 USD |
| `7D` | `0.9750` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 4,890.00 USD |
| `1D` | `0.9760` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 53,000.00 USD | 13,960.00 USD | 8,400.00 USD |
| `7D` | `0.9770` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD |
| `1D` | `0.9780` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 39,740.00 USD | 2,960.00 USD | 17,920.00 USD |
| `7D` | `0.9790` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 84,920.00 USD |
| `1D` | `0.9800` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 29,240.00 USD | 9,580.00 USD | 20,800.00 USD |
| `7D` | `0.9810` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 540.00 USD | 0.00 USD | 118,820.00 USD |
| `1D` | `0.9820` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 15,980.00 USD | 12,160.00 USD | 7,210.00 USD |
| `7D` | `0.9830` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 102,710.00 USD | 15,810.00 USD | 52,260.00 USD |
| `1D` | `0.9840` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 13,190.00 USD | 38,710.00 USD |
| `7D` | `0.9850` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,300.00 USD |
| `1D` | `0.9860` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 50,550.00 USD | 3,460.00 USD | 19,890.00 USD |
| `7D` | `0.9870` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 57,740.00 USD |
| `1D` | `0.9880` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 16,640.00 USD | 0.00 USD | 14,320.00 USD |
| `7D` | `0.9890` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `0.9900` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 57,390.00 USD | 1,300.00 USD | 13,390.00 USD |
| `7D` | `0.9910` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD |
| `1D` | `0.9920` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 8,950.00 USD | 2,810.00 USD | 13,340.00 USD |
| `7D` | `0.9930` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `0.9940` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 12,310.00 USD | 13,250.00 USD | 1,420.00 USD |
| `7D` | `0.9950` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 33,790.00 USD | 5,380.00 USD | 42,770.00 USD |
| `1D` | `0.9960` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 18,530.00 USD | 4,110.00 USD | 0.00 USD |
| `7D` | `0.9970` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 69,270.00 USD | 0.00 USD | 4,670.00 USD |
| `1D` | `0.9980` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 40,410.00 USD | 4,790.00 USD | 10,500.00 USD |
| `7D` | `0.9990` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 156.00 USD | 462.12 USD |
| `1D` | `1.00` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 59,960.00 USD | 28,860.00 USD | 1,710.00 USD |
| `7D` | `1.00` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.00` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 501.30 USD | 0.00 USD | 266.05 USD |
| `7D` | `1.00` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 105,770.00 USD | 21,740.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 10,110.00 USD | 9,540.00 USD | 9,410.00 USD |
| `7D` | `1.00` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 32,430.00 USD | 3,970.00 USD | 1,470.00 USD |
| `1D` | `1.01` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 101,040.00 USD | 10,140.00 USD | 31,440.00 USD |
| `7D` | `1.01` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 34,110.00 USD | 0.00 USD | 29,210.00 USD |
| `1D` | `1.01` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 17,270.00 USD | 9,160.00 USD | 27,730.00 USD |
| `7D` | `1.01` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD |
| `1D` | `1.01` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 10,530.00 USD | 14,710.00 USD | 0.00 USD |
| `7D` | `1.01` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 20,090.00 USD | 14,180.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 16,240.00 USD | 25,350.00 USD | 155.80 USD |
| `7D` | `1.01` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD |
| `1D` | `1.01` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 5,950.00 USD | 4,370.00 USD | 25,020.00 USD |
| `7D` | `1.01` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 26,360.00 USD | 7,070.00 USD |
| `1D` | `1.02` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 20,120.00 USD | 75.20 USD | 20,270.00 USD |
| `7D` | `1.02` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD |
| `1D` | `1.02` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 6,670.00 USD | 8,490.00 USD | 22,230.00 USD |
| `7D` | `1.02` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 315.97 USD | 75,760.00 USD | 11,810.00 USD |
| `1D` | `1.02` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 51,730.00 USD | 4,370.00 USD | 20,560.00 USD |
| `7D` | `1.02` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 44,170.00 USD | 32,840.00 USD | 68,050.00 USD |
| `1D` | `1.02` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 51,380.00 USD | 3,710.00 USD | 36,250.00 USD |
| `7D` | `1.02` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 66,990.00 USD | 85,890.00 USD | 146,060.00 USD |
| `1D` | `1.02` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 50,330.00 USD | 25,640.00 USD | 53,210.00 USD |
| `7D` | `1.02` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 28,320.00 USD | 48,490.00 USD | 41,400.00 USD |
| `1D` | `1.03` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 52,630.00 USD | 18,370.00 USD | 20,210.00 USD |
| `7D` | `1.03` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 161,070.00 USD | 127,000.00 USD | 25,260.00 USD |
| `1D` | `1.03` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 31,340.00 USD | 10,940.00 USD | 18,480.00 USD |
| `7D` | `1.03` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD |
| `1D` | `1.03` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 95,330.00 USD | 24,510.00 USD | 33,610.00 USD |
| `7D` | `1.03` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD |
| `1D` | `1.03` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 70,060.00 USD | 8,980.00 USD | 35,950.00 USD |
| `7D` | `1.03` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD |
| `1D` | `1.03` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 38,330.00 USD | 9,300.00 USD | 21,490.00 USD |
| `7D` | `1.03` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 259,060.00 USD | 8,290.00 USD | 43,490.00 USD |
| `1D` | `1.04` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 18,100.00 USD | 13,840.00 USD | 7,800.00 USD |
| `7D` | `1.04` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 192,080.00 USD | 3,170.00 USD | 109,460.00 USD |
| `1D` | `1.04` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 63,010.00 USD | 3,250.00 USD | 4,330.00 USD |
| `7D` | `1.04` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 239,580.00 USD | 9,010.00 USD | 117,630.00 USD |
| `1D` | `1.04` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 7,790.00 USD | 7,460.00 USD | 12,300.00 USD |
| `7D` | `1.04` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 276,890.00 USD | 2,090.00 USD | 159,500.00 USD |
| `1D` | `1.04` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 11,290.00 USD | 9,870.00 USD | 7,750.00 USD |
| `7D` | `1.04` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD |
| `1D` | `1.04` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 7,410.00 USD | 9,310.00 USD | 21,860.00 USD |
| `7D` | `1.04` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD |
| `1D` | `1.05` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 21,730.00 USD | 4,160.00 USD | 321.14 USD |
| `7D` | `1.05` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 178,890.00 USD | 96,370.00 USD | 238,570.00 USD |
| `1D` | `1.05` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 8,930.00 USD | 3,210.00 USD | 4,950.00 USD |
| `7D` | `1.05` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 116,670.00 USD | 13,780.00 USD | 77,320.00 USD |
| `1D` | `1.05` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 42,790.00 USD | 10,010.00 USD | 13,550.00 USD |
| `7D` | `1.05` | 7,580,000.00 USD | 7,580,000.00 USD | 0.00 USD | 175,350.00 USD | 43,690.00 USD | 87,370.00 USD |
| `1D` | `1.05` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 23,270.00 USD | 1,310.00 USD | 15,860.00 USD |
| `7D` | `1.05` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 68,590.00 USD | 58,070.00 USD | 74,380.00 USD |
| `1D` | `1.05` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 16,310.00 USD | 365.79 USD | 6,470.00 USD |
| `7D` | `1.05` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 125,020.00 USD | 33,860.00 USD | 72,330.00 USD |
| `1D` | `1.06` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 13,640.00 USD | 3,680.00 USD | 4,790.00 USD |
| `7D` | `1.06` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 218,860.00 USD | 70,000.00 USD | 106,380.00 USD |
| `1D` | `1.06` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 29,640.00 USD | 3,000.00 USD | 725.34 USD |
| `7D` | `1.06` | 8,870,000.00 USD | 8,870,000.00 USD | 0.00 USD | 240,060.00 USD | 74,380.00 USD | 145,470.00 USD |
| `1D` | `1.06` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 3,850.00 USD | 4,510.00 USD | 8,650.00 USD |
| `7D` | `1.06` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 140,850.00 USD | 56,310.00 USD | 78,020.00 USD |
| `1D` | `1.06` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 1,990.00 USD | 2,450.00 USD | 1,930.00 USD |
| `7D` | `1.06` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 141,700.00 USD | 73,690.00 USD | 71,340.00 USD |
| `1D` | `1.06` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 15,200.00 USD | 2,970.00 USD | 3,220.00 USD |
| `7D` | `1.06` | 9,640,000.00 USD | 9,640,000.00 USD | 0.00 USD | 90,670.00 USD | 28,390.00 USD | 95,080.00 USD |
| `1D` | `1.07` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 16,000.00 USD | 141.60 USD | 8,440.00 USD |
| `7D` | `1.07` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 86,760.00 USD | 43,390.00 USD | 82,980.00 USD |
| `1D` | `1.07` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 7,520.00 USD | 4,330.00 USD | 3,120.00 USD |
| `7D` | `1.07` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 219,670.00 USD | 14,440.00 USD | 62,270.00 USD |
| `1D` | `1.07` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 7,140.00 USD | 3,900.00 USD | 3,210.00 USD |
| `7D` | `1.07` | 10,380,000.00 USD | 10,380,000.00 USD | 0.00 USD | 141,570.00 USD | 36,670.00 USD | 52,290.00 USD |
| `1D` | `1.07` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 9,330.00 USD | 2,350.00 USD | 3,180.00 USD |
| `7D` | `1.07` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 96,630.00 USD | 42,960.00 USD | 95,510.00 USD |
| `1D` | `1.07` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 7,690.00 USD | 4,460.00 USD | 6,930.00 USD |
| `7D` | `1.07` | 10,810,000.00 USD | 10,810,000.00 USD | 0.00 USD | 97,650.00 USD | 27,560.00 USD | 60,670.00 USD |
| `1D` | `1.08` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 5,350.00 USD | 5,330.00 USD | 5,490.00 USD |
| `7D` | `1.08` | 10,960,000.00 USD | 10,960,000.00 USD | 0.00 USD | 75,040.00 USD | 29,910.00 USD | 48,910.00 USD |
| `1D` | `1.08` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 9,430.00 USD | 4,070.00 USD | 150.13 USD |
| `7D` | `1.08` | 11,200,000.00 USD | 11,200,000.00 USD | 0.00 USD | 166,380.00 USD | 21,060.00 USD | 52,480.00 USD |
| `1D` | `1.08` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 7,700.00 USD | 1,870.00 USD | 711.93 USD |
| `7D` | `1.08` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 164,440.00 USD | 26,480.00 USD | 33,950.00 USD |
| `1D` | `1.08` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 5,280.00 USD | 1,770.00 USD | 4,210.00 USD |
| `7D` | `1.08` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 61,330.00 USD | 41,110.00 USD | 100,750.00 USD |
| `1D` | `1.08` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 9,180.00 USD | 1,500.00 USD | 3,180.00 USD |
| `7D` | `1.08` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 86,400.00 USD | 18,540.00 USD | 46,440.00 USD |
| `1D` | `1.09` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 8,920.00 USD | 2,900.00 USD | 6,970.00 USD |
| `7D` | `1.09` | 12,010,000.00 USD | 12,010,000.00 USD | 0.00 USD | 102,510.00 USD | 58,170.00 USD | 69,640.00 USD |
| `1D` | `1.09` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 3,630.00 USD | 4,290.00 USD | 4,990.00 USD |
| `7D` | `1.09` | 12,190,000.00 USD | 12,190,000.00 USD | 0.00 USD | 71,650.00 USD | 23,140.00 USD | 85,300.00 USD |
| `1D` | `1.09` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 9,700.00 USD | 3,220.00 USD | 1,950.00 USD |
| `7D` | `1.09` | 12,320,000.00 USD | 12,320,000.00 USD | 0.00 USD | 70,660.00 USD | 25,660.00 USD | 32,870.00 USD |
| `1D` | `1.09` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 4,370.00 USD | 23.75 USD | 966.50 USD |
| `7D` | `1.09` | 12,480,000.00 USD | 12,480,000.00 USD | 0.00 USD | 59,760.00 USD | 39,220.00 USD | 62,330.00 USD |
| `1D` | `1.09` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 2,490.00 USD | 2,060.00 USD |
| `7D` | `1.09` | 12,650,000.00 USD | 12,650,000.00 USD | 0.00 USD | 56,240.00 USD | 22,740.00 USD | 92,520.00 USD |
| `1D` | `1.10` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 1,740.00 USD | 3,660.00 USD | 318.21 USD |
| `7D` | `1.10` | 12,800,000.00 USD | 12,800,000.00 USD | 0.00 USD | 92,660.00 USD | 13,380.00 USD | 38,150.00 USD |
| `1D` | `1.10` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 3,620.00 USD | 1,090.00 USD | 4,380.00 USD |
| `1D` | `1.10` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 1,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.10` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 188,000.00 USD | 49,370.00 USD | 89,650.00 USD |
| `7D` | `1.10` | 13,300,000.00 USD | 13,300,000.00 USD | 0.00 USD | 122,300.00 USD | 44,140.00 USD | 15,590.00 USD |
| `7D` | `1.10` | 13,530,000.00 USD | 13,530,000.00 USD | 0.00 USD | 91,720.00 USD | 19,140.00 USD | 110,190.00 USD |
| `7D` | `1.10` | 13,590,000.00 USD | 13,590,000.00 USD | 0.00 USD | 22,500.00 USD | 10,390.00 USD | 31,450.00 USD |
| `7D` | `1.11` | 13,700,000.00 USD | 13,700,000.00 USD | 0.00 USD | 51,840.00 USD | 24,280.00 USD | 34,190.00 USD |
| `7D` | `1.11` | 13,880,000.00 USD | 13,880,000.00 USD | 0.00 USD | 80,930.00 USD | 42,230.00 USD | 56,110.00 USD |
| `7D` | `1.11` | 14,030,000.00 USD | 14,030,000.00 USD | 0.00 USD | 69,040.00 USD | 16,050.00 USD | 64,910.00 USD |
| `7D` | `1.11` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 20,190.00 USD | 43,570.00 USD | 25,640.00 USD |
| `7D` | `1.11` | 14,170,000.00 USD | 14,170,000.00 USD | 0.00 USD | 34,700.00 USD | 6,650.00 USD | 9,420.00 USD |
| `7D` | `1.12` | 14,320,000.00 USD | 14,320,000.00 USD | 0.00 USD | 68,170.00 USD | 45,980.00 USD | 32,030.00 USD |
| `7D` | `1.12` | 14,380,000.00 USD | 14,380,000.00 USD | 0.00 USD | 24,700.00 USD | 22,760.00 USD | 19,870.00 USD |
| `7D` | `1.12` | 14,490,000.00 USD | 14,490,000.00 USD | 0.00 USD | 49,110.00 USD | 30,950.00 USD | 23,330.00 USD |
| `7D` | `1.12` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 61,780.00 USD | 7,080.00 USD | 25,460.00 USD |
| `7D` | `1.12` | 14,640,000.00 USD | 14,640,000.00 USD | 0.00 USD | 18,300.00 USD | 10,940.00 USD | 29,890.00 USD |
| `7D` | `1.13` | 14,660,000.00 USD | 14,660,000.00 USD | 0.00 USD | 14,700.00 USD | 342.11 USD | 8,690.00 USD |
| `7D` | `1.13` | 14,780,000.00 USD | 14,780,000.00 USD | 0.00 USD | 56,500.00 USD | 19,160.00 USD | 45,770.00 USD |
| `7D` | `1.13` | 14,990,000.00 USD | 14,990,000.00 USD | 0.00 USD | 106,510.00 USD | 12,730.00 USD | 90,150.00 USD |
| `7D` | `1.13` | 15,100,000.00 USD | 15,100,000.00 USD | 0.00 USD | 77,640.00 USD | 4,280.00 USD | 27,360.00 USD |
| `7D` | `1.14` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 16,300.00 USD | 10,920.00 USD | 61,260.00 USD |
| `7D` | `1.14` | 15,210,000.00 USD | 15,210,000.00 USD | 0.00 USD | 4,780.00 USD | 4,820.00 USD | 6,530.00 USD |
| `7D` | `1.14` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 2,980.00 USD | 0.00 USD | 35,230.00 USD |
| `7D` | `1.14` | 15,300,000.00 USD | 15,300,000.00 USD | 0.00 USD | 36,300.00 USD | 8,480.00 USD | 6,790.00 USD |
| `7D` | `1.14` | 15,370,000.00 USD | 15,370,000.00 USD | 0.00 USD | 36,560.00 USD | 1,660.00 USD | 37,230.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `195.85M` | Total OI Tokens: `209,429,002.4 DOT`
  * 1h OI Change: `-4.34%` | 4h OI Change: `-7.30%` | 24h OI Change: `-11.66%`
  * Exchange Breakdown: Binance=`34.44M` | Bybit=`22.55M` | OKX=`9.83M` | Hyperliquid=`5.47M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-310.13` | Last 24h: `7.91K` | Last 3d: `-10.37K` | Last 7d: `-19.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0015%` | **USDT OKX** | `-0.0004%` |
| **USDT Bybit** | `0.0020%` | **USDT KuCoin** | `0.0017%` |
| **USDT MEXC** | `-0.0015%` | **USDT BingX** | `0.0024%` |
| **USDT Gate** | `-0.0082%` | **USDT Bitget** | `-0.0068%` |
| **CoinM Binance** | `0.0041%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `58.42%` | `41.58%` | `1.41` | 17,900,000.00 USD |
| `15M` | `Binance` | `54.34%` | `45.66%` | `1.19` | 7,080,000.00 USD |
| `15M` | `OKX` | `69.45%` | `30.55%` | `2.27` | 1,450,000.00 USD |
| `15M` | `Bybit` | `58.65%` | `41.35%` | `1.42` | 1,110,000.00 USD |
| `15M` | `KuCoin` | `55.07%` | `44.93%` | `1.23` | 76,400.00 USD |
| `15M` | `Gate` | `62.94%` | `37.06%` | `1.70` | 520,210.00 USD |
| `15M` | `Bitget` | `50.58%` | `49.42%` | `1.02` | 584,540.00 USD |
| `15M` | `BingX` | `83.89%` | `16.11%` | `5.21` | 1,810,000.00 USD |
| `15M` | `MEXC` | `67.18%` | `32.82%` | `2.05` | 1,290,000.00 USD |
| `15M` | `Bitunix` | `50.42%` | `49.58%` | `1.02` | 436,600.00 USD |
| `15M` | `Hyperliquid` | `63.83%` | `36.17%` | `1.76` | 193,770.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.73%` | `53.27%` | `0.88` | 3,040,000.00 USD |
| `15M` | `Crypto.com` | `33.67%` | `66.33%` | `0.51` | 3,680.00 USD |
| `15M` | `WhiteBIT` | `64.45%` | `35.55%` | `1.81` | 160,320.00 USD |
| `15M` | `HTX` | `50.11%` | `49.89%` | `1.00` | 2,360.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `14.27%` | `85.73%` | `0.17` | 76,370.00 USD |
| `15M` | `Aster` | `23.94%` | `76.06%` | `0.31` | 56,350.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `71.22%` | `28.78%` | `2.47` | 11,990.00 USD |
| `15M` | `Whale Positions` | `54.34%` | `45.66%` | `1.19` | 7,080,000.00 USD |
| `15M` | `Global Accounts` | `58.42%` | `41.58%` | `1.41` | 17,900,000.00 USD |
| `1H` | `DOT` | `46.29%` | `53.71%` | `0.86` | 359,180,000.00 USD |
| `1H` | `Binance` | `45.71%` | `54.29%` | `0.84` | 150,840,000.00 USD |
| `1H` | `OKX` | `48.54%` | `51.46%` | `0.94` | 43,600,000.00 USD |
| `1H` | `Bybit` | `48.44%` | `51.56%` | `0.94` | 44,920,000.00 USD |
| `1H` | `KuCoin` | `52.24%` | `47.76%` | `1.09` | 3,140,000.00 USD |
| `1H` | `Gate` | `48.79%` | `51.21%` | `0.95` | 4,590,000.00 USD |
| `1H` | `Bitget` | `46.7%` | `53.3%` | `0.88` | 14,240,000.00 USD |
| `1H` | `BingX` | `40.2%` | `59.8%` | `0.67` | 17,210,000.00 USD |
| `1H` | `MEXC` | `45.25%` | `54.75%` | `0.83` | 16,350,000.00 USD |
| `1H` | `Bitunix` | `52.47%` | `47.53%` | `1.10` | 7,540,000.00 USD |
| `1H` | `Hyperliquid` | `45.11%` | `54.89%` | `0.82` | 38,770,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `44.29%` | `55.71%` | `0.80` | 2,370,000.00 USD |
| `1H` | `Crypto.com` | `37.84%` | `62.16%` | `0.61` | 23,730.00 USD |
| `1H` | `WhiteBIT` | `44.23%` | `55.77%` | `0.79` | 3,960,000.00 USD |
| `1H` | `HTX` | `48.28%` | `51.72%` | `0.93` | 736,200.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `44.69%` | `55.31%` | `0.81` | 7,870,000.00 USD |
| `1H` | `Aster` | `53.6%` | `46.4%` | `1.16` | 1,230,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `42.91%` | `57.09%` | `0.75` | 1,770,000.00 USD |
| `1H` | `Whale Positions` | `45.71%` | `54.29%` | `0.84` | 150,840,000.00 USD |
| `1H` | `Global Accounts` | `46.29%` | `53.71%` | `0.86` | 359,180,000.00 USD |
| `4H` | `DOT` | `47.68%` | `52.32%` | `0.91` | 619,930,000.00 USD |
| `4H` | `Binance` | `47.81%` | `52.19%` | `0.92` | 250,240,000.00 USD |
| `4H` | `OKX` | `48.88%` | `51.12%` | `0.96` | 76,280,000.00 USD |
| `4H` | `Bybit` | `49.78%` | `50.22%` | `0.99` | 78,190,000.00 USD |
| `4H` | `KuCoin` | `48.46%` | `51.54%` | `0.94` | 5,390,000.00 USD |
| `4H` | `Gate` | `48.4%` | `51.6%` | `0.94` | 9,030,000.00 USD |
| `4H` | `Bitget` | `45.38%` | `54.62%` | `0.83` | 24,220,000.00 USD |
| `4H` | `BingX` | `42.98%` | `57.02%` | `0.75` | 30,730,000.00 USD |
| `4H` | `MEXC` | `48.54%` | `51.46%` | `0.94` | 33,350,000.00 USD |
| `4H` | `Bitunix` | `49.54%` | `50.46%` | `0.98` | 16,650,000.00 USD |
| `4H` | `Hyperliquid` | `42.27%` | `57.73%` | `0.73` | 58,840,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.15%` | `50.85%` | `0.97` | 4,270,000.00 USD |
| `4H` | `Crypto.com` | `51.13%` | `48.87%` | `1.05` | 41,930.00 USD |
| `4H` | `WhiteBIT` | `62.81%` | `37.19%` | `1.69` | 12,070,000.00 USD |
| `4H` | `HTX` | `49.38%` | `50.62%` | `0.98` | 925,730.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `43.45%` | `56.55%` | `0.77` | 13,260,000.00 USD |
| `4H` | `Aster` | `58.59%` | `41.41%` | `1.41` | 1,950,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `49.14%` | `50.86%` | `0.97` | 4,480,000.00 USD |
| `4H` | `Whale Positions` | `47.81%` | `52.19%` | `0.92` | 250,240,000.00 USD |
| `4H` | `Global Accounts` | `47.68%` | `52.32%` | `0.91` | 619,930,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.9813` | `0.9827` | `0.9813` | `0.9867` | `0.9789` | 947,049.41 USD | 720,261.00 USD | 226,788.42 USD | 493,472.58 USD | `+52.11%` | `28B / 1S` |
| `0:00 UTC` | `0.9805` | `0.9815` | `0.9805` | `0.9849` | `0.9787` | 512,523.44 USD | 243,023.57 USD | 269,499.87 USD | -26,476.30 USD | `-5.17%` | `12B / 6S` |
| `5:00 UTC` | `0.9856` | `0.9822` | `0.9856` | `0.9858` | `0.9780` | 526,140.64 USD | 318,567.26 USD | 207,573.38 USD | 110,993.88 USD | `+21.10%` | `16B / 9S` |
| `0:00 UTC` | `0.9873` | `0.9868` | `0.9873` | `0.9887` | `0.9839` | 407,897.05 USD | 216,028.73 USD | 191,868.32 USD | 24,160.41 USD | `+5.92%` | `8B / 4S` |
| `5:00 UTC` | `0.9858` | `0.9859` | `0.9858` | `0.9880` | `0.9839` | 388,071.33 USD | 177,551.18 USD | 210,520.15 USD | -32,968.97 USD | `-8.50%` | `3B / 8S` |
| `0:00 UTC` | `0.9681` | `0.9669` | `0.9681` | `0.9851` | `0.9557` | 3,728,299.49 USD | 1,667,776.70 USD | 2,060,522.79 USD | -392,746.09 USD | `-10.53%` | `7B / 26S` |
| `5:00 UTC` | `0.9681` | `0.9687` | `0.9681` | `0.9718` | `0.9650` | 792,721.03 USD | 373,256.63 USD | 419,464.39 USD | -46,207.76 USD | `-5.83%` | `5B / 11S` |
| `0:00 UTC` | `0.9271` | `0.9372` | `0.9271` | `0.9707` | `0.9107` | 10,294,158.77 USD | 4,127,124.83 USD | 6,167,033.94 USD | -2,039,909.11 USD | `-19.82%` | `5B / 37S` |
| `5:00 UTC` | `0.9157` | `0.9093` | `0.9157` | `0.9241` | `0.8893` | 9,166,573.96 USD | 4,231,807.53 USD | 4,934,766.43 USD | -702,958.89 USD | `-7.67%` | `6B / 13S` |
| `0:00 UTC` | `0.9138` | `0.9196` | `0.9138` | `0.9286` | `0.9076` | 3,016,339.92 USD | 1,422,841.79 USD | 1,593,498.13 USD | -170,656.34 USD | `-5.66%` | `10B / 8S` |

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
| `5m` | 25,620.00 USD | 323,630.00 USD | **`ACCUMULATION`** |
| `15m` | 64,290.00 USD | 297,420.00 USD | **`ACCUMULATION`** |
| `30m` | -315,500.00 USD | -746,370.00 USD | **`DISTRIBUTION`** |
| `1h` | -701,780.00 USD | -4,860,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -840,330.00 USD | -5,480,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -939,390.00 USD | -5,840,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,020,000.00 USD | -6,770,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,010,000.00 USD | -7,150,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,200,000.00 USD | -7,430,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,310,000.00 USD | -7,300,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,280,000.00 USD | -24,240,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,610,000.00 USD | -78,330,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+25.62K` | 15m=`+64.29K` | 1h=`-701.78K` | 24h=`-1.31M`
* Futures Capital Netflows: 5m=`+323.63K` | 15m=`+297.42K` | 1h=`-4.86M` | 24h=`-7.30M`
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
  * `2026-10-30 02:15:06 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:40:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.9092` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.8612` (Risk Distance: `0.0480` pts)
  * +2.5R Take Profit: `1.03`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9190` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9670` (Risk Distance: `0.0480` pts)
  * +2.5R Take Profit: `0.7989`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9359`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
