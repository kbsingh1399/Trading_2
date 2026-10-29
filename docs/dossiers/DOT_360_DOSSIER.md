# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 02:36:43 IST` (`2026-10-29 21:06:43 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9050` | **Live Ask Quote**: `0.9260` | **Mid Price**: `0.9155`
- **Spread Points**: `21.00` | **Spread BPS**: `229.38 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.9683` | VWAP Z-Score: `-2.67` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0134` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `16.16` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.05` | Lower -3.00σ Band: `0.8917`
  * Upper +2.51σ Band: `1.03` | Lower -2.51σ Band: `0.9042`
  * Upper +2.01σ Band: `1.02` | Lower -2.01σ Band: `0.9170`
  * Upper +2.00σ Band: `1.02` | Lower -2.00σ Band: `0.9172`
  * Upper +1.28σ Band: `1.00` | Lower -1.28σ Band: `0.9356`
  * Upper +1.00σ Band: `0.9939` | Lower -1.00σ Band: `0.9428`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9455` | EMA-20=`0.9630` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9736` (Slope: `+0.0000`) | EMA-100=`0.9783`
  * Institutional Anchors: EMA-144=`0.9804` | EMA-200=`0.9817` (Slope: `-0.3005`) | EMA-233=`0.9826`
- **Range Boundaries**: 24H High=`1.02` | 24H Low=`0.8800` | Weekly High=`1.03` | Weekly Low=`0.8800`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9078` (Distance: `+1.29%`)
  * Point of Control (POC) = `0.9050` (Distance: `+1.60%`)
  * Value Area Low (VAL) = `0.9050` (Distance: `+1.60%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.01` | Weekly POC=`0.9932` | Weekly VAL=`0.9761`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9090` | Low=`0.9050`
  * London Session (08:00-16:00 UTC): High=`0.9192` | Low=`0.9118`
  * New York Session (13:00-21:00 UTC): High=`0.9210` | Low=`0.9100`
  * Initial Balance (First Hour): IB High=`0.9182` | IB Low=`0.9128`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9118` - `0.9192`
  * Optimal Trade Entry (OTE 0.705): `0.9173`
  * Structural Invalidation Anchor (0.786): `0.9228`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9151` | `0.9170` | `0.9087` | `0.9107` | `952,047` | 869,823.57 USD | -5,121.08 USD | `-0.59%` | -3,729,280.55 USD | `+0.33` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `0.9106` | `0.9216` | `0.9075` | `0.9166` | `1,716,262` | 1,570,263.17 USD | -339,490.88 USD | `-21.62%` | -4,068,771.43 USD | `-0.37` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.9166` | `0.9177` | `0.9155` | `0.9176` | `65,000` | 59,564.00 USD | -19,860.90 USD | `-33.34%` | -4,088,632.33 USD | `+0.35` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.9676` | `0.9706` | `0.9105` | `0.9193` | `10,984,354` | 10,294,158.77 USD | -2,039,909.11 USD | `-19.82%` | -3,033,378.23 USD | `-3.85` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9192` | `0.9241` | `0.8892` | `0.9107` | `10,082,852` | 9,166,573.96 USD | -702,958.89 USD | `-7.67%` | -3,736,337.12 USD | `-1.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.9106` | `0.9216` | `0.9075` | `0.9173` | `1,780,795` | 1,629,399.19 USD | -359,598.44 USD | `-22.07%` | -4,095,935.57 USD | `-0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9839` | `0.9886` | `0.9780` | `0.9844` | `1,864,944` | 1,834,632.46 USD | 75,709.02 USD | `+4.13%` | -271,595.36 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9845` | `0.9849` | `0.8892` | `0.9107` | `25,741,782` | 23,981,753.25 USD | -3,181,821.86 USD | `-13.27%` | -3,453,417.22 USD | `-3.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.9106` | `0.9216` | `0.9075` | `0.9186` | `1,812,106` | 1,658,145.74 USD | -353,950.00 USD | `-21.35%` | -3,807,367.22 USD | `-0.23` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | 516,506.12 USD | `-1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -280,559.32 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9176` | `27,523,043` | 25,611,580.42 USD | -3,541,173.64 USD | `-13.83%` | -3,821,732.96 USD | `-2.13` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9699` | `0.9906` | `0.9674` | `0.9732` | `8,505,701` | 8,320,368.15 USD | 13,201.93 USD | `+0.16%` | 609,018.52 USD | `-1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | 694,082.93 USD | `-0.56` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | 516,506.12 USD | `-1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -280,559.32 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9176` | `27,523,043` | 25,611,580.42 USD | -3,541,173.64 USD | `-13.83%` | -3,821,732.96 USD | `-2.13` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.9155`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:35:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.00` | 5,901.97 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale BUY: 5.90K USD at 1.0012 USD [API] | `2026-10-28 03:15:43` |
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
| `7D` | `Long Liquidation` | `0.7890` | 1,270,000.00 USD | 1,270,000.00 USD | 7,140.00 USD | 2,210.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7895` | 20,380.00 USD | 364,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7910` | 1,260,000.00 USD | 1,260,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.7920` | 674,280.00 USD | 674,280.00 USD | 6,470.00 USD | 1,650.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7930` | 1,230,000.00 USD | 1,230,000.00 USD | 20,360.00 USD | 1,250.00 USD | 6,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.7940` | 661,100.00 USD | 661,100.00 USD | 1,860.00 USD | 595.59 USD | 965.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7950` | 1,200,000.00 USD | 1,200,000.00 USD | 3,290.00 USD | 4,710.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.7960` | 657,680.00 USD | 657,680.00 USD | 222.45 USD | 2,470.00 USD | 1,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7965` | 106.49 USD | 344,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7970` | 1,180,000.00 USD | 1,180,000.00 USD | 10,100.00 USD | 1,130.00 USD | 522.30 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.7980` | 653,920.00 USD | 653,920.00 USD | 1,140.00 USD | 22.38 USD | 494.59 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7990` | 1,170,000.00 USD | 1,170,000.00 USD | 20,360.00 USD | 6,180.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8000` | 652,260.00 USD | 652,260.00 USD | 7.83 USD | 5.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8010` | 1,130,000.00 USD | 1,130,000.00 USD | 5,420.00 USD | 5,300.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8020` | 651,060.00 USD | 651,060.00 USD | 2,290.00 USD | 1,600.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8025` | 238.90 USD | 344,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8030` | 1,120,000.00 USD | 1,120,000.00 USD | 4,550.00 USD | 2,260.00 USD | 9,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8040` | 645,050.00 USD | 645,050.00 USD | 813.73 USD | 993.93 USD | 952.73 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8045` | 566.61 USD | 344,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8050` | 1,100,000.00 USD | 1,100,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8055` | 699.01 USD | 343,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8060` | 642,290.00 USD | 642,290.00 USD | 536.61 USD | 845.93 USD | 53.10 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8070` | 1,080,000.00 USD | 1,080,000.00 USD | 12,160.00 USD | 4,660.00 USD | 6,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8080` | 640,850.00 USD | 640,850.00 USD | 4,130.00 USD | 657.69 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8090` | 1,050,000.00 USD | 1,050,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8100` | 634,280.00 USD | 634,280.00 USD | 1,940.00 USD | 14.30 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8110` | 1,050,000.00 USD | 1,050,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8115` | 13,430.00 USD | 342,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8120` | 628,780.00 USD | 628,780.00 USD | 821.06 USD | 258.31 USD | 44.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8130` | 1,040,000.00 USD | 1,040,000.00 USD | 14,060.00 USD | 2,970.00 USD | 8,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 329,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8140` | 627,660.00 USD | 627,660.00 USD | 4,760.00 USD | 30.50 USD | 796.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8150` | 1,010,000.00 USD | 1,010,000.00 USD | 5,990.00 USD | 7,330.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8160` | 622,080.00 USD | 622,080.00 USD | 0.00 USD | 182.45 USD | 26.89 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8170` | 994,970.00 USD | 994,970.00 USD | 10,780.00 USD | 2,430.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8180` | 621,870.00 USD | 621,870.00 USD | 9,320.00 USD | 6.25 USD | 96.08 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8190` | 972,090.00 USD | 972,090.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8200` | 612,440.00 USD | 612,440.00 USD | 1,260.00 USD | 0.00 USD | 435.27 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8210` | 956,660.00 USD | 956,660.00 USD | 6,850.00 USD | 3,190.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 328,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8220` | 610,750.00 USD | 610,750.00 USD | 0.00 USD | 0.00 USD | 471.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8230` | 936,590.00 USD | 936,590.00 USD | 16,840.00 USD | 4,620.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8240` | 610,270.00 USD | 610,270.00 USD | 905.13 USD | 3,640.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8250` | 913,180.00 USD | 913,180.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8260` | 598,930.00 USD | 598,930.00 USD | 0.00 USD | 5,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 900,890.00 USD | 900,890.00 USD | 4,320.00 USD | 1,970.00 USD | 616.76 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8285` | 1,890.00 USD | 326,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8290` | 893,980.00 USD | 893,980.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8310` | 890,310.00 USD | 890,310.00 USD | 9,280.00 USD | 1,520.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8330` | 877,400.00 USD | 877,400.00 USD | 0.00 USD | 3,360.00 USD | 77.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8350` | 873,970.00 USD | 873,970.00 USD | 2,200.00 USD | 0.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 324,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8370` | 869,790.00 USD | 869,790.00 USD | 0.00 USD | 36.87 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8375` | 167.00 USD | 324,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8390` | 869,750.00 USD | 869,750.00 USD | 0.00 USD | 798.38 USD | 539.92 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8400` | 593,020.00 USD | 593,020.00 USD | 458.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8410` | 868,410.00 USD | 868,410.00 USD | 270.00 USD | 804.10 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,240.00 USD | 324,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 592,560.00 USD | 592,560.00 USD | 0.00 USD | 149.63 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8430` | 867,340.00 USD | 867,340.00 USD | 6,590.00 USD | 3,840.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8440` | 592,410.00 USD | 592,410.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8445` | 168.31 USD | 323,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8450` | 852,850.00 USD | 852,850.00 USD | 0.00 USD | 24.80 USD | 474.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8470` | 852,350.00 USD | 852,350.00 USD | 7,900.00 USD | 949.62 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8490` | 841,310.00 USD | 841,310.00 USD | 731.45 USD | 137.03 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 323,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 590,450.00 USD | 590,450.00 USD | 421.90 USD | 61.55 USD | 206.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 840,440.00 USD | 840,440.00 USD | 3,990.00 USD | 109.15 USD | 4,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8520` | 589,760.00 USD | 589,760.00 USD | 0.00 USD | 1,940.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 831,680.00 USD | 831,680.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 825,730.00 USD | 825,730.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8560` | 585,350.00 USD | 585,350.00 USD | 2,040.00 USD | 199.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8570` | 821,080.00 USD | 821,080.00 USD | 0.00 USD | 944.22 USD | 577.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 321,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8580` | 583,120.00 USD | 583,120.00 USD | 250.65 USD | 0.00 USD | 182.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8590` | 819,560.00 USD | 819,560.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8595` | 171.38 USD | 321,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8600` | 582,680.00 USD | 582,680.00 USD | 5,860.00 USD | 1,030.00 USD | 251.39 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8605` | 61,100.00 USD | 320,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8610` | 818,290.00 USD | 818,290.00 USD | 7,320.00 USD | 2,950.00 USD | 467.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8620` | 575,540.00 USD | 575,540.00 USD | 7,410.00 USD | 24.95 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8625` | 309.55 USD | 259,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8630` | 807,560.00 USD | 807,560.00 USD | 758.91 USD | 2,590.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 259,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 568,100.00 USD | 568,100.00 USD | 5,790.00 USD | 1,940.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 259,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8650` | 802,920.00 USD | 802,920.00 USD | 6,720.00 USD | 0.00 USD | 184.85 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8660` | 556,580.00 USD | 556,580.00 USD | 0.00 USD | 20.18 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 118.54 USD | 258,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8670` | 796,010.00 USD | 796,010.00 USD | 10,120.00 USD | 3,240.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8680` | 556,560.00 USD | 556,560.00 USD | 3,320.00 USD | 3,550.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8690` | 772,500.00 USD | 772,500.00 USD | 25,250.00 USD | 1,950.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8700` | 540,970.00 USD | 540,970.00 USD | 18,340.00 USD | 3,580.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8710` | 737,270.00 USD | 737,270.00 USD | 7,370.00 USD | 1,110.00 USD | 13,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8720` | 514,290.00 USD | 514,290.00 USD | 32,240.00 USD | 26.70 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 715,680.00 USD | 715,680.00 USD | 0.00 USD | 2,270.00 USD | 295.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 475,810.00 USD | 475,810.00 USD | 6,780.00 USD | 3,080.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 713,110.00 USD | 713,110.00 USD | 0.00 USD | 0.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 462,920.00 USD | 462,920.00 USD | 6,140.00 USD | 3,510.00 USD | 4,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 171.88 USD | 258,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8770` | 706,900.00 USD | 706,900.00 USD | 20,650.00 USD | 16,130.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8780` | 448,880.00 USD | 448,880.00 USD | 24,840.00 USD | 15,510.00 USD | 27,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 667,350.00 USD | 667,350.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8795` | 948.01 USD | 258,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8800` | 381,430.00 USD | 381,430.00 USD | 22,140.00 USD | 12,830.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 659,730.00 USD | 659,730.00 USD | 228.30 USD | 167.73 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8820` | 340,970.00 USD | 340,970.00 USD | 8,950.00 USD | 11,150.00 USD | 150.13 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8830` | 659,330.00 USD | 659,330.00 USD | 8,430.00 USD | 5,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 320,730.00 USD | 320,730.00 USD | 7,440.00 USD | 1,810.00 USD | 1,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8850` | 645,170.00 USD | 645,170.00 USD | 8,630.00 USD | 5,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8860` | 310,450.00 USD | 310,450.00 USD | 5,930.00 USD | 1,700.00 USD | 8,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8870` | 630,580.00 USD | 630,580.00 USD | 19,060.00 USD | 5,060.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8880` | 294,630.00 USD | 294,630.00 USD | 17,470.00 USD | 4,160.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8890` | 598,990.00 USD | 598,990.00 USD | 13,840.00 USD | 5,510.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8900` | 263,240.00 USD | 263,240.00 USD | 50,120.00 USD | 4,210.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8910` | 565,770.00 USD | 565,770.00 USD | 30,650.00 USD | 10,730.00 USD | 22,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8920` | 203,920.00 USD | 203,920.00 USD | 4,920.00 USD | 3,110.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8925` | 526.84 USD | 257,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8930` | 501,670.00 USD | 501,670.00 USD | 24,780.00 USD | 5,820.00 USD | 10,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8940` | 193,940.00 USD | 193,940.00 USD | 4,240.00 USD | 0.00 USD | 966.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8950` | 460,970.00 USD | 460,970.00 USD | 7,380.00 USD | 29,250.00 USD | 26,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8960` | 188,720.00 USD | 188,720.00 USD | 21,000.00 USD | 15,480.00 USD | 6,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8970` | 397,430.00 USD | 397,430.00 USD | 43,430.00 USD | 5,400.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8980` | 145,690.00 USD | 145,690.00 USD | 21,610.00 USD | 10,780.00 USD | 32,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8985` | 9,220.00 USD | 257,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8990` | 318,710.00 USD | 318,710.00 USD | 52,250.00 USD | 23,810.00 USD | 19,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8995` | 3,820.00 USD | 247,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9000` | 80,400.00 USD | 80,400.00 USD | 24,060.00 USD | 30,300.00 USD | 2,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9010` | 223,430.00 USD | 223,430.00 USD | 20,170.00 USD | 11,690.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9020` | 23,670.00 USD | 23,670.00 USD | 4,420.00 USD | 3,120.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9030` | 188,330.00 USD | 188,330.00 USD | 13,100.00 USD | 8,710.00 USD | 25,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9035` | 180.16 USD | 244,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9040` | 13,890.00 USD | 13,890.00 USD | 1,580.00 USD | 2,430.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9050` | 140,980.00 USD | 140,980.00 USD | 31,190.00 USD | 3,730.00 USD | 25,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9055` | 674.42 USD | 243,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9060` | 4,160.00 USD | 4,160.00 USD | 0.00 USD | 1,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9070` | 80,500.00 USD | 80,500.00 USD | 32,990.00 USD | 857.81 USD | 14,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9080` | 2,550.00 USD | 2,550.00 USD | 0.00 USD | 346.80 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9090` | 32,110.00 USD | 32,110.00 USD | 4,250.00 USD | 954.68 USD | 6,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9095` | 951.34 USD | 243,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9100` | 2,200.00 USD | 2,200.00 USD | 1,380.00 USD | 815.15 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9110` | 20,770.00 USD | 20,770.00 USD | 3,880.00 USD | 441.10 USD | 16,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9120` | 1,240.00 USD | 1,240.00 USD | 925.04 USD | 315.61 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9120` | 2,480.00 USD | 2,480.00 USD | 925.04 USD | 315.61 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9130` | 23,190.00 USD | 23,190.00 USD | 22,720.00 USD | 473.74 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9135` | 143.42 USD | 242,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9140` | 2,680.00 USD | 2,680.00 USD | 0.00 USD | 200.33 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9150` | 95,970.00 USD | 95,970.00 USD | 39,030.00 USD | 515.41 USD | 33,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9160` | 2,810.00 USD | 2,810.00 USD | 0.00 USD | 131.45 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9170` | 129,040.00 USD | 129,040.00 USD | 17,820.00 USD | 0.00 USD | 15,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9180` | 2,950.00 USD | 2,950.00 USD | 0.00 USD | 132.34 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9185` | 145.86 USD | 242,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9190` | 193,580.00 USD | 193,580.00 USD | 46,070.00 USD | 0.00 USD | 18,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9195` | 7,330.00 USD | 241,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9200` | 3,110.00 USD | 3,110.00 USD | 0.00 USD | 166.12 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9210` | 223,170.00 USD | 223,170.00 USD | 13,710.00 USD | 0.00 USD | 15,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9220` | 31,560.00 USD | 31,560.00 USD | 14,160.00 USD | 77.74 USD | 14,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9225` | 8,360.00 USD | 234,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9230` | 290,270.00 USD | 290,270.00 USD | 27,030.00 USD | 0.00 USD | 40,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9240` | 40,580.00 USD | 40,580.00 USD | 7,970.00 USD | 1,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9250` | 431,040.00 USD | 431,040.00 USD | 95,150.00 USD | 0.00 USD | 45,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9260` | 132,640.00 USD | 132,640.00 USD | 52,420.00 USD | 1,100.00 USD | 38,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9270` | 513,100.00 USD | 513,100.00 USD | 59,970.00 USD | 0.00 USD | 22,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9280` | 193,710.00 USD | 193,710.00 USD | 47,790.00 USD | 145.20 USD | 13,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9290` | 602,440.00 USD | 602,440.00 USD | 28,390.00 USD | 0.00 USD | 60,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9295` | 253.01 USD | 226,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9300` | 238,520.00 USD | 238,520.00 USD | 21,640.00 USD | 221.69 USD | 22,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9310` | 660,890.00 USD | 660,890.00 USD | 31,000.00 USD | 19,860.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9320` | 305,440.00 USD | 305,440.00 USD | 45,470.00 USD | 7,580.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9330` | 711,440.00 USD | 711,440.00 USD | 25,260.00 USD | 0.00 USD | 25,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9335` | 361.45 USD | 226,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9340` | 395,260.00 USD | 395,260.00 USD | 35,410.00 USD | 10,860.00 USD | 43,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9350` | 800,410.00 USD | 800,410.00 USD | 71,590.00 USD | 0.00 USD | 17,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9360` | 529,680.00 USD | 529,680.00 USD | 84,420.00 USD | 30,060.00 USD | 19,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9365` | 6,560.00 USD | 225,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9370` | 825,580.00 USD | 825,580.00 USD | 16,340.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9375` | 196.97 USD | 219,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9380` | 586,560.00 USD | 586,560.00 USD | 56,080.00 USD | 103.28 USD | 695.88 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9390` | 877,360.00 USD | 877,360.00 USD | 39,250.00 USD | 0.00 USD | 12,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9400` | 630,920.00 USD | 630,920.00 USD | 41,740.00 USD | 0.00 USD | 2,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9405` | 141.83 USD | 218,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9410` | 912,440.00 USD | 912,440.00 USD | 29,630.00 USD | 0.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9420` | 688,390.00 USD | 688,390.00 USD | 57,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9430` | 970,440.00 USD | 970,440.00 USD | 45,490.00 USD | 0.00 USD | 12,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9440` | 746,700.00 USD | 746,700.00 USD | 58,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9445` | 1,060.00 USD | 218,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9450` | 1,220,000.00 USD | 1,220,000.00 USD | 180,850.00 USD | 0.00 USD | 73,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9455` | 106,880.00 USD | 217,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9460` | 792,640.00 USD | 792,640.00 USD | 45,730.00 USD | 199.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 1,390,000.00 USD | 1,390,000.00 USD | 114,070.00 USD | 0.00 USD | 51,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9475` | 323.19 USD | 110,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9480` | 938,110.00 USD | 938,110.00 USD | 145,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 1,690,000.00 USD | 1,690,000.00 USD | 116,860.00 USD | 0.00 USD | 178,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9495` | 105,430.00 USD | 110,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9500` | 999,900.00 USD | 999,900.00 USD | 59,460.00 USD | 105.68 USD | 2,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 1,980,000.00 USD | 1,980,000.00 USD | 210,510.00 USD | 9,930.00 USD | 76,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9515` | 405.62 USD | 5,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9520` | 1,090,000.00 USD | 1,090,000.00 USD | 47,190.00 USD | 13,410.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 1,940.00 USD | 121,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 1,140,000.00 USD | 1,140,000.00 USD | 19,080.00 USD | 8,110.00 USD | 29,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 19,730.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9555` | 3,160.00 USD | 4,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9560` | 1,150,000.00 USD | 1,150,000.00 USD | 865.00 USD | 7,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 2,150,000.00 USD | 2,150,000.00 USD | 1,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 313.25 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9585` | 1,530.00 USD | 1,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9610` | 2,170,000.00 USD | 2,170,000.00 USD | 24,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 1,150,000.00 USD | 1,150,000.00 USD | 2,720.00 USD | 149.63 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 2,180,000.00 USD | 2,180,000.00 USD | 12,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 9,690.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 2,190,000.00 USD | 2,190,000.00 USD | 8,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 1,180,000.00 USD | 1,180,000.00 USD | 2,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 11,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 2,050.00 USD | 10,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 1,240,000.00 USD | 1,240,000.00 USD | 23,620.00 USD | 0.00 USD | 23,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 2,240,000.00 USD | 2,240,000.00 USD | 1,430.00 USD | 9,050.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 1,280,000.00 USD | 1,280,000.00 USD | 25,800.00 USD | 5,170.00 USD | 14,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 16,590.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 1,360,000.00 USD | 1,360,000.00 USD | 50,870.00 USD | 13,960.00 USD | 8,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 2,360,000.00 USD | 2,360,000.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 1,420,000.00 USD | 1,420,000.00 USD | 39,740.00 USD | 2,960.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 84,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 1,480,000.00 USD | 1,480,000.00 USD | 29,240.00 USD | 9,580.00 USD | 20,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9810` | 2,560,000.00 USD | 2,560,000.00 USD | 540.00 USD | 0.00 USD | 118,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 1,510,000.00 USD | 1,510,000.00 USD | 15,980.00 USD | 12,160.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 2,730,000.00 USD | 2,730,000.00 USD | 102,710.00 USD | 15,810.00 USD | 52,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 13,190.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 1,640,000.00 USD | 1,640,000.00 USD | 50,550.00 USD | 3,460.00 USD | 19,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 2,850,000.00 USD | 2,850,000.00 USD | 40,020.00 USD | 0.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9880` | 1,670,000.00 USD | 1,670,000.00 USD | 16,640.00 USD | 0.00 USD | 14,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9890` | 2,870,000.00 USD | 2,870,000.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 1,740,000.00 USD | 1,740,000.00 USD | 57,390.00 USD | 1,300.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9910` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 1,770,000.00 USD | 1,770,000.00 USD | 8,950.00 USD | 2,810.00 USD | 13,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9930` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 1,790,000.00 USD | 1,790,000.00 USD | 12,310.00 USD | 13,250.00 USD | 1,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9950` | 2,980,000.00 USD | 2,980,000.00 USD | 33,790.00 USD | 5,380.00 USD | 42,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 1,820,000.00 USD | 1,820,000.00 USD | 18,530.00 USD | 4,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 3,050,000.00 USD | 3,050,000.00 USD | 69,270.00 USD | 0.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 1,870,000.00 USD | 1,870,000.00 USD | 40,410.00 USD | 4,790.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 156.00 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,960,000.00 USD | 1,960,000.00 USD | 59,960.00 USD | 28,860.00 USD | 1,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,100,000.00 USD | 3,100,000.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,960,000.00 USD | 1,960,000.00 USD | 501.30 USD | 0.00 USD | 266.05 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,250,000.00 USD | 3,250,000.00 USD | 105,110.00 USD | 21,740.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,990,000.00 USD | 1,990,000.00 USD | 10,110.00 USD | 9,540.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,270,000.00 USD | 3,270,000.00 USD | 19,830.00 USD | 3,970.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,130,000.00 USD | 2,130,000.00 USD | 101,040.00 USD | 10,140.00 USD | 31,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,340,000.00 USD | 3,340,000.00 USD | 34,110.00 USD | 0.00 USD | 29,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,180,000.00 USD | 2,180,000.00 USD | 10,110.00 USD | 9,160.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,360,000.00 USD | 3,360,000.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,210,000.00 USD | 2,210,000.00 USD | 10,530.00 USD | 14,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,400,000.00 USD | 3,400,000.00 USD | 20,090.00 USD | 14,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,250,000.00 USD | 2,250,000.00 USD | 16,240.00 USD | 25,350.00 USD | 155.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,450,000.00 USD | 3,450,000.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,280,000.00 USD | 2,280,000.00 USD | 5,950.00 USD | 4,370.00 USD | 25,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 26,360.00 USD | 7,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,320,000.00 USD | 2,320,000.00 USD | 20,120.00 USD | 75.20 USD | 20,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,530,000.00 USD | 3,530,000.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,360,000.00 USD | 2,360,000.00 USD | 6,670.00 USD | 8,490.00 USD | 22,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,620,000.00 USD | 3,620,000.00 USD | 315.97 USD | 75,760.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,430,000.00 USD | 2,430,000.00 USD | 44,710.00 USD | 4,370.00 USD | 15,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,760,000.00 USD | 3,760,000.00 USD | 44,170.00 USD | 32,840.00 USD | 68,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,500,000.00 USD | 2,500,000.00 USD | 51,380.00 USD | 3,710.00 USD | 21,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 4,060,000.00 USD | 4,060,000.00 USD | 66,990.00 USD | 85,890.00 USD | 146,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,630,000.00 USD | 2,630,000.00 USD | 50,330.00 USD | 25,640.00 USD | 53,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 4,170,000.00 USD | 4,170,000.00 USD | 28,320.00 USD | 48,490.00 USD | 29,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,720,000.00 USD | 2,720,000.00 USD | 52,630.00 USD | 18,370.00 USD | 20,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,480,000.00 USD | 4,480,000.00 USD | 161,070.00 USD | 127,000.00 USD | 25,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,780,000.00 USD | 2,780,000.00 USD | 31,340.00 USD | 10,940.00 USD | 18,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,690,000.00 USD | 4,690,000.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,940,000.00 USD | 2,940,000.00 USD | 95,330.00 USD | 24,510.00 USD | 33,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,890,000.00 USD | 4,890,000.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,050,000.00 USD | 3,050,000.00 USD | 70,060.00 USD | 8,980.00 USD | 35,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 5,020,000.00 USD | 5,020,000.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,120,000.00 USD | 3,120,000.00 USD | 38,330.00 USD | 9,300.00 USD | 21,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 5,330,000.00 USD | 5,330,000.00 USD | 259,060.00 USD | 8,290.00 USD | 43,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,160,000.00 USD | 3,160,000.00 USD | 18,100.00 USD | 13,840.00 USD | 7,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,640,000.00 USD | 5,640,000.00 USD | 192,080.00 USD | 3,170.00 USD | 109,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 210.51 USD | 210.51 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,230,000.00 USD | 3,230,000.00 USD | 63,010.00 USD | 3,250.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,000,000.00 USD | 6,000,000.00 USD | 239,580.00 USD | 9,010.00 USD | 117,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,260,000.00 USD | 3,260,000.00 USD | 7,790.00 USD | 7,460.00 USD | 12,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,440,000.00 USD | 6,440,000.00 USD | 276,890.00 USD | 2,090.00 USD | 159,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,290,000.00 USD | 3,290,000.00 USD | 11,290.00 USD | 9,870.00 USD | 8,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,640,000.00 USD | 6,640,000.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,330,000.00 USD | 3,330,000.00 USD | 7,410.00 USD | 9,310.00 USD | 21,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 212.03 USD | 422.54 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,910,000.00 USD | 6,910,000.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,350,000.00 USD | 3,350,000.00 USD | 21,730.00 USD | 4,160.00 USD | 321.14 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 424.67 USD | 847.21 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,420,000.00 USD | 7,420,000.00 USD | 178,890.00 USD | 96,370.00 USD | 238,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 733.98 USD | 1,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,370,000.00 USD | 3,370,000.00 USD | 8,930.00 USD | 3,210.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,630,000.00 USD | 7,630,000.00 USD | 116,670.00 USD | 13,780.00 USD | 77,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,440,000.00 USD | 3,440,000.00 USD | 42,790.00 USD | 10,010.00 USD | 13,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,930,000.00 USD | 7,930,000.00 USD | 175,350.00 USD | 43,690.00 USD | 87,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,480,000.00 USD | 3,480,000.00 USD | 23,270.00 USD | 1,310.00 USD | 15,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 213.55 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 8,130,000.00 USD | 8,130,000.00 USD | 68,590.00 USD | 58,070.00 USD | 74,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 213.76 USD | 2,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,500,000.00 USD | 3,500,000.00 USD | 16,310.00 USD | 365.79 USD | 6,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 8,370,000.00 USD | 8,370,000.00 USD | 125,020.00 USD | 33,860.00 USD | 72,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.06` | 74,410.00 USD | 76,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,520,000.00 USD | 3,520,000.00 USD | 13,640.00 USD | 3,680.00 USD | 4,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,760,000.00 USD | 8,760,000.00 USD | 218,860.00 USD | 70,000.00 USD | 106,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,560,000.00 USD | 3,560,000.00 USD | 29,640.00 USD | 3,000.00 USD | 725.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,220,000.00 USD | 9,220,000.00 USD | 240,060.00 USD | 74,380.00 USD | 145,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.06` | 214.97 USD | 76,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,570,000.00 USD | 3,570,000.00 USD | 3,850.00 USD | 4,510.00 USD | 8,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,500,000.00 USD | 9,500,000.00 USD | 140,850.00 USD | 56,310.00 USD | 78,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,580,000.00 USD | 3,580,000.00 USD | 1,990.00 USD | 2,450.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,780,000.00 USD | 9,780,000.00 USD | 141,700.00 USD | 73,690.00 USD | 71,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.06` | 431.57 USD | 77,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.06` | 3,600,000.00 USD | 3,600,000.00 USD | 15,200.00 USD | 2,970.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 10,000,000.00 USD | 10,000,000.00 USD | 90,670.00 USD | 28,390.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 3,630,000.00 USD | 3,630,000.00 USD | 16,000.00 USD | 141.60 USD | 8,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,210,000.00 USD | 10,210,000.00 USD | 86,760.00 USD | 43,390.00 USD | 82,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 3,640,000.00 USD | 3,640,000.00 USD | 7,520.00 USD | 4,330.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,510,000.00 USD | 10,510,000.00 USD | 219,670.00 USD | 14,440.00 USD | 62,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.07` | 216.89 USD | 77,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.07` | 3,650,000.00 USD | 3,650,000.00 USD | 7,140.00 USD | 3,900.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.07` | 217.20 USD | 77,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,740,000.00 USD | 10,740,000.00 USD | 141,570.00 USD | 36,670.00 USD | 52,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 3,670,000.00 USD | 3,670,000.00 USD | 9,330.00 USD | 2,350.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,970,000.00 USD | 10,970,000.00 USD | 96,630.00 USD | 42,960.00 USD | 95,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 3,690,000.00 USD | 3,690,000.00 USD | 7,860.00 USD | 4,560.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.07` | 436.03 USD | 77,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.07` | 11,160,000.00 USD | 11,160,000.00 USD | 97,650.00 USD | 27,560.00 USD | 60,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 3,710,000.00 USD | 3,710,000.00 USD | 5,350.00 USD | 5,330.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,310,000.00 USD | 11,310,000.00 USD | 75,040.00 USD | 29,910.00 USD | 48,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 3,720,000.00 USD | 3,720,000.00 USD | 9,430.00 USD | 4,070.00 USD | 150.13 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,550,000.00 USD | 11,550,000.00 USD | 166,380.00 USD | 21,060.00 USD | 52,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 3,730,000.00 USD | 3,730,000.00 USD | 7,700.00 USD | 1,870.00 USD | 711.93 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,780,000.00 USD | 11,780,000.00 USD | 164,440.00 USD | 26,480.00 USD | 33,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 3,740,000.00 USD | 3,740,000.00 USD | 5,280.00 USD | 1,770.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,980,000.00 USD | 11,980,000.00 USD | 61,330.00 USD | 41,110.00 USD | 100,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 3,750,000.00 USD | 3,750,000.00 USD | 9,180.00 USD | 1,500.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 12,130,000.00 USD | 12,130,000.00 USD | 86,400.00 USD | 18,540.00 USD | 46,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 3,770,000.00 USD | 3,770,000.00 USD | 8,920.00 USD | 2,900.00 USD | 6,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,360,000.00 USD | 12,360,000.00 USD | 102,510.00 USD | 58,170.00 USD | 69,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 3,790,000.00 USD | 3,790,000.00 USD | 3,630.00 USD | 4,290.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,540,000.00 USD | 12,540,000.00 USD | 71,650.00 USD | 23,140.00 USD | 85,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 3,800,000.00 USD | 3,800,000.00 USD | 9,830.00 USD | 3,220.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.09` | 221.37 USD | 78,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,670,000.00 USD | 12,670,000.00 USD | 70,660.00 USD | 25,660.00 USD | 32,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 3,810,000.00 USD | 3,810,000.00 USD | 4,370.00 USD | 93.54 USD | 966.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,830,000.00 USD | 12,830,000.00 USD | 59,760.00 USD | 39,220.00 USD | 62,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 2,490.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 13,000,000.00 USD | 13,000,000.00 USD | 56,240.00 USD | 22,740.00 USD | 92,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 3,820,000.00 USD | 3,820,000.00 USD | 1,740.00 USD | 3,660.00 USD | 318.21 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,140,000.00 USD | 13,140,000.00 USD | 86,360.00 USD | 13,380.00 USD | 38,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 3,830,000.00 USD | 3,830,000.00 USD | 3,620.00 USD | 1,090.00 USD | 4,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 3,830,000.00 USD | 3,830,000.00 USD | 1,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,470,000.00 USD | 13,470,000.00 USD | 188,000.00 USD | 49,370.00 USD | 89,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,650,000.00 USD | 13,650,000.00 USD | 122,300.00 USD | 44,140.00 USD | 15,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,870,000.00 USD | 13,870,000.00 USD | 91,720.00 USD | 19,140.00 USD | 110,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,940,000.00 USD | 13,940,000.00 USD | 22,500.00 USD | 10,390.00 USD | 31,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,050,000.00 USD | 14,050,000.00 USD | 51,840.00 USD | 24,280.00 USD | 34,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,230,000.00 USD | 14,230,000.00 USD | 80,930.00 USD | 42,230.00 USD | 56,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.11` | 169.86 USD | 78,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,380,000.00 USD | 14,380,000.00 USD | 69,040.00 USD | 16,050.00 USD | 64,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,460,000.00 USD | 14,460,000.00 USD | 20,190.00 USD | 43,570.00 USD | 25,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,520,000.00 USD | 14,520,000.00 USD | 34,700.00 USD | 6,650.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,660,000.00 USD | 14,660,000.00 USD | 68,170.00 USD | 45,980.00 USD | 32,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,720,000.00 USD | 14,720,000.00 USD | 24,700.00 USD | 22,760.00 USD | 13,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.12` | 518.90 USD | 78,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,830,000.00 USD | 14,830,000.00 USD | 49,110.00 USD | 30,950.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,920,000.00 USD | 14,920,000.00 USD | 61,780.00 USD | 7,080.00 USD | 25,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,980,000.00 USD | 14,980,000.00 USD | 18,300.00 USD | 10,940.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,000,000.00 USD | 15,000,000.00 USD | 14,700.00 USD | 342.11 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,120,000.00 USD | 15,120,000.00 USD | 56,500.00 USD | 19,160.00 USD | 45,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,330,000.00 USD | 15,330,000.00 USD | 106,510.00 USD | 12,730.00 USD | 90,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,440,000.00 USD | 15,440,000.00 USD | 77,640.00 USD | 4,280.00 USD | 27,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,530,000.00 USD | 15,530,000.00 USD | 16,300.00 USD | 10,920.00 USD | 61,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,550,000.00 USD | 15,550,000.00 USD | 4,780.00 USD | 4,820.00 USD | 6,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,590,000.00 USD | 15,590,000.00 USD | 2,980.00 USD | 0.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,640,000.00 USD | 15,640,000.00 USD | 36,300.00 USD | 8,480.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,710,000.00 USD | 15,710,000.00 USD | 36,560.00 USD | 1,660.00 USD | 37,230.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.7890` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 7,140.00 USD | 2,210.00 USD | 2,800.00 USD |
| `7D` | `0.7910` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD |
| `1D` | `0.7920` | 674,280.00 USD | 0.00 USD | 674,280.00 USD | 6,470.00 USD | 1,650.00 USD | 5,060.00 USD |
| `7D` | `0.7930` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 20,360.00 USD | 1,250.00 USD | 6,130.00 USD |
| `1D` | `0.7940` | 661,100.00 USD | 0.00 USD | 661,100.00 USD | 1,860.00 USD | 595.59 USD | 965.49 USD |
| `7D` | `0.7950` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 3,290.00 USD | 4,710.00 USD | 14,710.00 USD |
| `1D` | `0.7960` | 657,680.00 USD | 0.00 USD | 657,680.00 USD | 222.45 USD | 2,470.00 USD | 1,060.00 USD |
| `7D` | `0.7970` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 10,100.00 USD | 1,130.00 USD | 522.30 USD |
| `1D` | `0.7980` | 653,920.00 USD | 0.00 USD | 653,920.00 USD | 1,140.00 USD | 22.38 USD | 494.59 USD |
| `7D` | `0.7990` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 20,360.00 USD | 6,180.00 USD | 13,950.00 USD |
| `1D` | `0.8000` | 652,260.00 USD | 0.00 USD | 652,260.00 USD | 7.83 USD | 5.00 USD | 1,200.00 USD |
| `7D` | `0.8010` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 5,420.00 USD | 5,300.00 USD | 2,300.00 USD |
| `1D` | `0.8020` | 651,060.00 USD | 0.00 USD | 651,060.00 USD | 2,290.00 USD | 1,600.00 USD | 2,110.00 USD |
| `7D` | `0.8030` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 4,550.00 USD | 2,260.00 USD | 9,770.00 USD |
| `1D` | `0.8040` | 645,050.00 USD | 0.00 USD | 645,050.00 USD | 813.73 USD | 993.93 USD | 952.73 USD |
| `7D` | `0.8050` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD |
| `1D` | `0.8060` | 642,290.00 USD | 0.00 USD | 642,290.00 USD | 536.61 USD | 845.93 USD | 53.10 USD |
| `7D` | `0.8070` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 12,160.00 USD | 4,660.00 USD | 6,450.00 USD |
| `1D` | `0.8080` | 640,850.00 USD | 0.00 USD | 640,850.00 USD | 4,130.00 USD | 657.69 USD | 1,790.00 USD |
| `7D` | `0.8090` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD |
| `1D` | `0.8100` | 634,280.00 USD | 0.00 USD | 634,280.00 USD | 1,940.00 USD | 14.30 USD | 3,540.00 USD |
| `7D` | `0.8110` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD |
| `1D` | `0.8120` | 628,780.00 USD | 0.00 USD | 628,780.00 USD | 821.06 USD | 258.31 USD | 44.49 USD |
| `7D` | `0.8130` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 14,060.00 USD | 2,970.00 USD | 8,560.00 USD |
| `1D` | `0.8140` | 627,660.00 USD | 0.00 USD | 627,660.00 USD | 4,760.00 USD | 30.50 USD | 796.05 USD |
| `7D` | `0.8150` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 5,990.00 USD | 7,330.00 USD | 4,220.00 USD |
| `1D` | `0.8160` | 622,080.00 USD | 0.00 USD | 622,080.00 USD | 0.00 USD | 182.45 USD | 26.89 USD |
| `7D` | `0.8170` | 994,970.00 USD | 0.00 USD | 994,970.00 USD | 10,780.00 USD | 2,430.00 USD | 9,670.00 USD |
| `1D` | `0.8180` | 621,870.00 USD | 0.00 USD | 621,870.00 USD | 9,320.00 USD | 6.25 USD | 96.08 USD |
| `7D` | `0.8190` | 972,090.00 USD | 0.00 USD | 972,090.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD |
| `1D` | `0.8200` | 612,440.00 USD | 0.00 USD | 612,440.00 USD | 1,260.00 USD | 0.00 USD | 435.27 USD |
| `7D` | `0.8210` | 956,660.00 USD | 0.00 USD | 956,660.00 USD | 6,850.00 USD | 3,190.00 USD | 10,030.00 USD |
| `1D` | `0.8220` | 610,750.00 USD | 0.00 USD | 610,750.00 USD | 0.00 USD | 0.00 USD | 471.94 USD |
| `7D` | `0.8230` | 936,590.00 USD | 0.00 USD | 936,590.00 USD | 16,840.00 USD | 4,620.00 USD | 1,960.00 USD |
| `1D` | `0.8240` | 610,270.00 USD | 0.00 USD | 610,270.00 USD | 905.13 USD | 3,640.00 USD | 6,790.00 USD |
| `7D` | `0.8250` | 913,180.00 USD | 0.00 USD | 913,180.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD |
| `1D` | `0.8260` | 598,930.00 USD | 0.00 USD | 598,930.00 USD | 0.00 USD | 5,920.00 USD | 0.00 USD |
| `7D` | `0.8270` | 900,890.00 USD | 0.00 USD | 900,890.00 USD | 4,320.00 USD | 1,970.00 USD | 616.76 USD |
| `7D` | `0.8290` | 893,980.00 USD | 0.00 USD | 893,980.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD |
| `7D` | `0.8310` | 890,310.00 USD | 0.00 USD | 890,310.00 USD | 9,280.00 USD | 1,520.00 USD | 2,110.00 USD |
| `7D` | `0.8330` | 877,400.00 USD | 0.00 USD | 877,400.00 USD | 0.00 USD | 3,360.00 USD | 77.95 USD |
| `7D` | `0.8350` | 873,970.00 USD | 0.00 USD | 873,970.00 USD | 2,200.00 USD | 0.00 USD | 1,980.00 USD |
| `7D` | `0.8370` | 869,790.00 USD | 0.00 USD | 869,790.00 USD | 0.00 USD | 36.87 USD | 0.00 USD |
| `7D` | `0.8390` | 869,750.00 USD | 0.00 USD | 869,750.00 USD | 0.00 USD | 798.38 USD | 539.92 USD |
| `1D` | `0.8400` | 593,020.00 USD | 0.00 USD | 593,020.00 USD | 458.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8410` | 868,410.00 USD | 0.00 USD | 868,410.00 USD | 270.00 USD | 804.10 USD | 0.00 USD |
| `1D` | `0.8420` | 592,560.00 USD | 0.00 USD | 592,560.00 USD | 0.00 USD | 149.63 USD | 0.00 USD |
| `7D` | `0.8430` | 867,340.00 USD | 0.00 USD | 867,340.00 USD | 6,590.00 USD | 3,840.00 USD | 4,060.00 USD |
| `1D` | `0.8440` | 592,410.00 USD | 0.00 USD | 592,410.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8450` | 852,850.00 USD | 0.00 USD | 852,850.00 USD | 0.00 USD | 24.80 USD | 474.61 USD |
| `7D` | `0.8470` | 852,350.00 USD | 0.00 USD | 852,350.00 USD | 7,900.00 USD | 949.62 USD | 2,180.00 USD |
| `7D` | `0.8490` | 841,310.00 USD | 0.00 USD | 841,310.00 USD | 731.45 USD | 137.03 USD | 0.00 USD |
| `1D` | `0.8500` | 590,450.00 USD | 0.00 USD | 590,450.00 USD | 421.90 USD | 61.55 USD | 206.79 USD |
| `7D` | `0.8510` | 840,440.00 USD | 0.00 USD | 840,440.00 USD | 3,990.00 USD | 109.15 USD | 4,660.00 USD |
| `1D` | `0.8520` | 589,760.00 USD | 0.00 USD | 589,760.00 USD | 0.00 USD | 1,940.00 USD | 2,470.00 USD |
| `7D` | `0.8530` | 831,680.00 USD | 0.00 USD | 831,680.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD |
| `7D` | `0.8550` | 825,730.00 USD | 0.00 USD | 825,730.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD |
| `1D` | `0.8560` | 585,350.00 USD | 0.00 USD | 585,350.00 USD | 2,040.00 USD | 199.60 USD | 0.00 USD |
| `7D` | `0.8570` | 821,080.00 USD | 0.00 USD | 821,080.00 USD | 0.00 USD | 944.22 USD | 577.61 USD |
| `1D` | `0.8580` | 583,120.00 USD | 0.00 USD | 583,120.00 USD | 250.65 USD | 0.00 USD | 182.69 USD |
| `7D` | `0.8590` | 819,560.00 USD | 0.00 USD | 819,560.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD |
| `1D` | `0.8600` | 582,680.00 USD | 0.00 USD | 582,680.00 USD | 5,860.00 USD | 1,030.00 USD | 251.39 USD |
| `7D` | `0.8610` | 818,290.00 USD | 0.00 USD | 818,290.00 USD | 7,320.00 USD | 2,950.00 USD | 467.14 USD |
| `1D` | `0.8620` | 575,540.00 USD | 0.00 USD | 575,540.00 USD | 7,410.00 USD | 24.95 USD | 0.00 USD |
| `7D` | `0.8630` | 807,560.00 USD | 0.00 USD | 807,560.00 USD | 758.91 USD | 2,590.00 USD | 1,280.00 USD |
| `1D` | `0.8640` | 568,100.00 USD | 0.00 USD | 568,100.00 USD | 5,790.00 USD | 1,940.00 USD | 3,790.00 USD |
| `7D` | `0.8650` | 802,920.00 USD | 0.00 USD | 802,920.00 USD | 6,720.00 USD | 0.00 USD | 184.85 USD |
| `1D` | `0.8660` | 556,580.00 USD | 0.00 USD | 556,580.00 USD | 0.00 USD | 20.18 USD | 0.00 USD |
| `7D` | `0.8670` | 796,010.00 USD | 0.00 USD | 796,010.00 USD | 10,120.00 USD | 3,240.00 USD | 10,160.00 USD |
| `1D` | `0.8680` | 556,560.00 USD | 0.00 USD | 556,560.00 USD | 3,320.00 USD | 3,550.00 USD | 8,720.00 USD |
| `7D` | `0.8690` | 772,500.00 USD | 0.00 USD | 772,500.00 USD | 25,250.00 USD | 1,950.00 USD | 8,040.00 USD |
| `1D` | `0.8700` | 540,970.00 USD | 0.00 USD | 540,970.00 USD | 18,340.00 USD | 3,580.00 USD | 4,760.00 USD |
| `7D` | `0.8710` | 737,270.00 USD | 0.00 USD | 737,270.00 USD | 7,370.00 USD | 1,110.00 USD | 13,110.00 USD |
| `1D` | `0.8720` | 514,290.00 USD | 0.00 USD | 514,290.00 USD | 32,240.00 USD | 26.70 USD | 6,210.00 USD |
| `7D` | `0.8730` | 715,680.00 USD | 0.00 USD | 715,680.00 USD | 0.00 USD | 2,270.00 USD | 295.31 USD |
| `1D` | `0.8740` | 475,810.00 USD | 0.00 USD | 475,810.00 USD | 6,780.00 USD | 3,080.00 USD | 3,030.00 USD |
| `7D` | `0.8750` | 713,110.00 USD | 0.00 USD | 713,110.00 USD | 0.00 USD | 0.00 USD | 6,210.00 USD |
| `1D` | `0.8760` | 462,920.00 USD | 0.00 USD | 462,920.00 USD | 6,140.00 USD | 3,510.00 USD | 4,390.00 USD |
| `7D` | `0.8770` | 706,900.00 USD | 0.00 USD | 706,900.00 USD | 20,650.00 USD | 16,130.00 USD | 2,760.00 USD |
| `1D` | `0.8780` | 448,880.00 USD | 0.00 USD | 448,880.00 USD | 24,840.00 USD | 15,510.00 USD | 27,090.00 USD |
| `7D` | `0.8790` | 667,350.00 USD | 0.00 USD | 667,350.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD |
| `1D` | `0.8800` | 381,430.00 USD | 0.00 USD | 381,430.00 USD | 22,140.00 USD | 12,830.00 USD | 5,490.00 USD |
| `7D` | `0.8810` | 659,730.00 USD | 0.00 USD | 659,730.00 USD | 228.30 USD | 167.73 USD | 0.00 USD |
| `1D` | `0.8820` | 340,970.00 USD | 0.00 USD | 340,970.00 USD | 8,950.00 USD | 11,150.00 USD | 150.13 USD |
| `7D` | `0.8830` | 659,330.00 USD | 0.00 USD | 659,330.00 USD | 8,430.00 USD | 5,730.00 USD | 0.00 USD |
| `1D` | `0.8840` | 320,730.00 USD | 0.00 USD | 320,730.00 USD | 7,440.00 USD | 1,810.00 USD | 1,030.00 USD |
| `7D` | `0.8850` | 645,170.00 USD | 0.00 USD | 645,170.00 USD | 8,630.00 USD | 5,960.00 USD | 0.00 USD |
| `1D` | `0.8860` | 310,450.00 USD | 0.00 USD | 310,450.00 USD | 5,930.00 USD | 1,700.00 USD | 8,190.00 USD |
| `7D` | `0.8870` | 630,580.00 USD | 0.00 USD | 630,580.00 USD | 19,060.00 USD | 5,060.00 USD | 7,460.00 USD |
| `1D` | `0.8880` | 294,630.00 USD | 0.00 USD | 294,630.00 USD | 17,470.00 USD | 4,160.00 USD | 9,760.00 USD |
| `7D` | `0.8890` | 598,990.00 USD | 0.00 USD | 598,990.00 USD | 13,840.00 USD | 5,510.00 USD | 13,880.00 USD |
| `1D` | `0.8900` | 263,240.00 USD | 0.00 USD | 263,240.00 USD | 50,120.00 USD | 4,210.00 USD | 4,990.00 USD |
| `7D` | `0.8910` | 565,770.00 USD | 0.00 USD | 565,770.00 USD | 30,650.00 USD | 10,730.00 USD | 22,720.00 USD |
| `1D` | `0.8920` | 203,920.00 USD | 0.00 USD | 203,920.00 USD | 4,920.00 USD | 3,110.00 USD | 1,950.00 USD |
| `7D` | `0.8930` | 501,670.00 USD | 0.00 USD | 501,670.00 USD | 24,780.00 USD | 5,820.00 USD | 10,100.00 USD |
| `1D` | `0.8940` | 193,940.00 USD | 0.00 USD | 193,940.00 USD | 4,240.00 USD | 0.00 USD | 966.50 USD |
| `7D` | `0.8950` | 460,970.00 USD | 0.00 USD | 460,970.00 USD | 7,380.00 USD | 29,250.00 USD | 26,920.00 USD |
| `1D` | `0.8960` | 188,720.00 USD | 0.00 USD | 188,720.00 USD | 21,000.00 USD | 15,480.00 USD | 6,550.00 USD |
| `7D` | `0.8970` | 397,430.00 USD | 0.00 USD | 397,430.00 USD | 43,430.00 USD | 5,400.00 USD | 29,890.00 USD |
| `1D` | `0.8980` | 145,690.00 USD | 0.00 USD | 145,690.00 USD | 21,610.00 USD | 10,780.00 USD | 32,910.00 USD |
| `7D` | `0.8990` | 318,710.00 USD | 0.00 USD | 318,710.00 USD | 52,250.00 USD | 23,810.00 USD | 19,220.00 USD |
| `1D` | `0.9000` | 80,400.00 USD | 0.00 USD | 80,400.00 USD | 24,060.00 USD | 30,300.00 USD | 2,370.00 USD |
| `7D` | `0.9010` | 223,430.00 USD | 0.00 USD | 223,430.00 USD | 20,170.00 USD | 11,690.00 USD | 3,230.00 USD |
| `1D` | `0.9020` | 23,670.00 USD | 0.00 USD | 23,670.00 USD | 4,420.00 USD | 3,120.00 USD | 2,240.00 USD |
| `7D` | `0.9030` | 188,330.00 USD | 0.00 USD | 188,330.00 USD | 13,100.00 USD | 8,710.00 USD | 25,540.00 USD |
| `1D` | `0.9040` | 13,890.00 USD | 0.00 USD | 13,890.00 USD | 1,580.00 USD | 2,430.00 USD | 5,710.00 USD |
| `7D` | `0.9050` | 140,980.00 USD | 0.00 USD | 140,980.00 USD | 31,190.00 USD | 3,730.00 USD | 25,570.00 USD |
| `1D` | `0.9060` | 4,160.00 USD | 0.00 USD | 4,160.00 USD | 0.00 USD | 1,620.00 USD | 0.00 USD |
| `7D` | `0.9070` | 80,500.00 USD | 0.00 USD | 80,500.00 USD | 32,990.00 USD | 857.81 USD | 14,540.00 USD |
| `1D` | `0.9080` | 2,550.00 USD | 0.00 USD | 2,550.00 USD | 0.00 USD | 346.80 USD | 0.00 USD |
| `7D` | `0.9090` | 32,110.00 USD | 0.00 USD | 32,110.00 USD | 4,250.00 USD | 954.68 USD | 6,140.00 USD |
| `1D` | `0.9100` | 2,200.00 USD | 0.00 USD | 2,200.00 USD | 1,380.00 USD | 815.15 USD | 0.00 USD |
| `7D` | `0.9110` | 20,770.00 USD | 0.00 USD | 20,770.00 USD | 3,880.00 USD | 441.10 USD | 16,450.00 USD |
| `1D` | `0.9120` | 1,240.00 USD | 1,240.00 USD | 0.00 USD | 925.04 USD | 315.61 USD | 0.00 USD |
| `1D` | `0.9120` | 2,480.00 USD | 2,480.00 USD | 0.00 USD | 925.04 USD | 315.61 USD | 0.00 USD |
| `7D` | `0.9120` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9130` | 23,190.00 USD | 23,190.00 USD | 0.00 USD | 22,720.00 USD | 473.74 USD | 0.00 USD |
| `1D` | `0.9140` | 2,680.00 USD | 2,680.00 USD | 0.00 USD | 0.00 USD | 200.33 USD | 0.00 USD |
| `7D` | `0.9150` | 95,970.00 USD | 95,970.00 USD | 0.00 USD | 39,030.00 USD | 515.41 USD | 33,220.00 USD |
| `1D` | `0.9160` | 2,810.00 USD | 2,810.00 USD | 0.00 USD | 0.00 USD | 131.45 USD | 0.00 USD |
| `7D` | `0.9170` | 129,040.00 USD | 129,040.00 USD | 0.00 USD | 17,820.00 USD | 0.00 USD | 15,250.00 USD |
| `1D` | `0.9180` | 2,950.00 USD | 2,950.00 USD | 0.00 USD | 0.00 USD | 132.34 USD | 0.00 USD |
| `7D` | `0.9190` | 193,580.00 USD | 193,580.00 USD | 0.00 USD | 46,070.00 USD | 0.00 USD | 18,470.00 USD |
| `1D` | `0.9200` | 3,110.00 USD | 3,110.00 USD | 0.00 USD | 0.00 USD | 166.12 USD | 0.00 USD |
| `7D` | `0.9210` | 223,170.00 USD | 223,170.00 USD | 0.00 USD | 13,710.00 USD | 0.00 USD | 15,880.00 USD |
| `1D` | `0.9220` | 31,560.00 USD | 31,560.00 USD | 0.00 USD | 14,160.00 USD | 77.74 USD | 14,210.00 USD |
| `7D` | `0.9230` | 290,270.00 USD | 290,270.00 USD | 0.00 USD | 27,030.00 USD | 0.00 USD | 40,070.00 USD |
| `1D` | `0.9240` | 40,580.00 USD | 40,580.00 USD | 0.00 USD | 7,970.00 USD | 1,040.00 USD | 0.00 USD |
| `7D` | `0.9250` | 431,040.00 USD | 431,040.00 USD | 0.00 USD | 95,150.00 USD | 0.00 USD | 45,620.00 USD |
| `1D` | `0.9260` | 132,640.00 USD | 132,640.00 USD | 0.00 USD | 52,420.00 USD | 1,100.00 USD | 38,550.00 USD |
| `7D` | `0.9270` | 513,100.00 USD | 513,100.00 USD | 0.00 USD | 59,970.00 USD | 0.00 USD | 22,080.00 USD |
| `1D` | `0.9280` | 193,710.00 USD | 193,710.00 USD | 0.00 USD | 47,790.00 USD | 145.20 USD | 13,130.00 USD |
| `7D` | `0.9290` | 602,440.00 USD | 602,440.00 USD | 0.00 USD | 28,390.00 USD | 0.00 USD | 60,950.00 USD |
| `1D` | `0.9300` | 238,520.00 USD | 238,520.00 USD | 0.00 USD | 21,640.00 USD | 221.69 USD | 22,950.00 USD |
| `7D` | `0.9310` | 660,890.00 USD | 660,890.00 USD | 0.00 USD | 31,000.00 USD | 19,860.00 USD | 7,590.00 USD |
| `1D` | `0.9320` | 305,440.00 USD | 305,440.00 USD | 0.00 USD | 45,470.00 USD | 7,580.00 USD | 13,880.00 USD |
| `7D` | `0.9330` | 711,440.00 USD | 711,440.00 USD | 0.00 USD | 25,260.00 USD | 0.00 USD | 25,290.00 USD |
| `1D` | `0.9340` | 395,260.00 USD | 395,260.00 USD | 0.00 USD | 35,410.00 USD | 10,860.00 USD | 43,550.00 USD |
| `7D` | `0.9350` | 800,410.00 USD | 800,410.00 USD | 0.00 USD | 71,590.00 USD | 0.00 USD | 17,380.00 USD |
| `1D` | `0.9360` | 529,680.00 USD | 529,680.00 USD | 0.00 USD | 84,420.00 USD | 30,060.00 USD | 19,940.00 USD |
| `7D` | `0.9370` | 825,580.00 USD | 825,580.00 USD | 0.00 USD | 16,340.00 USD | 0.00 USD | 8,830.00 USD |
| `1D` | `0.9380` | 586,560.00 USD | 586,560.00 USD | 0.00 USD | 56,080.00 USD | 103.28 USD | 695.88 USD |
| `7D` | `0.9390` | 877,360.00 USD | 877,360.00 USD | 0.00 USD | 39,250.00 USD | 0.00 USD | 12,530.00 USD |
| `1D` | `0.9400` | 630,920.00 USD | 630,920.00 USD | 0.00 USD | 41,740.00 USD | 0.00 USD | 2,620.00 USD |
| `7D` | `0.9410` | 912,440.00 USD | 912,440.00 USD | 0.00 USD | 29,630.00 USD | 0.00 USD | 5,450.00 USD |
| `1D` | `0.9420` | 688,390.00 USD | 688,390.00 USD | 0.00 USD | 57,470.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9430` | 970,440.00 USD | 970,440.00 USD | 0.00 USD | 45,490.00 USD | 0.00 USD | 12,520.00 USD |
| `1D` | `0.9440` | 746,700.00 USD | 746,700.00 USD | 0.00 USD | 58,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9450` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 180,850.00 USD | 0.00 USD | 73,090.00 USD |
| `1D` | `0.9460` | 792,640.00 USD | 792,640.00 USD | 0.00 USD | 45,730.00 USD | 199.60 USD | 0.00 USD |
| `7D` | `0.9470` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 114,070.00 USD | 0.00 USD | 51,930.00 USD |
| `1D` | `0.9480` | 938,110.00 USD | 938,110.00 USD | 0.00 USD | 145,470.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9490` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 116,860.00 USD | 0.00 USD | 178,870.00 USD |
| `1D` | `0.9500` | 999,900.00 USD | 999,900.00 USD | 0.00 USD | 59,460.00 USD | 105.68 USD | 2,230.00 USD |
| `7D` | `0.9510` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 210,510.00 USD | 9,930.00 USD | 76,900.00 USD |
| `1D` | `0.9520` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 47,190.00 USD | 13,410.00 USD | 25,300.00 USD |
| `7D` | `0.9530` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 1,940.00 USD | 121,100.00 USD |
| `1D` | `0.9540` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 19,080.00 USD | 8,110.00 USD | 29,110.00 USD |
| `7D` | `0.9550` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 19,730.00 USD | 18,890.00 USD |
| `1D` | `0.9560` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 865.00 USD | 7,070.00 USD | 0.00 USD |
| `7D` | `0.9570` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 1,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9580` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 313.25 USD |
| `7D` | `0.9610` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 24,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9620` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 2,720.00 USD | 149.63 USD | 0.00 USD |
| `7D` | `0.9630` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 12,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9640` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 9,690.00 USD | 13,390.00 USD |
| `7D` | `0.9650` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 8,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9660` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 2,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9690` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 11,390.00 USD | 0.00 USD |
| `1D` | `0.9700` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 2,050.00 USD | 10,450.00 USD |
| `7D` | `0.9710` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD |
| `1D` | `0.9720` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 23,620.00 USD | 0.00 USD | 23,100.00 USD |
| `7D` | `0.9730` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 1,430.00 USD | 9,050.00 USD | 7,510.00 USD |
| `1D` | `0.9740` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 25,800.00 USD | 5,170.00 USD | 14,840.00 USD |
| `7D` | `0.9750` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 4,890.00 USD |
| `1D` | `0.9760` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 50,870.00 USD | 13,960.00 USD | 8,400.00 USD |
| `7D` | `0.9770` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD |
| `1D` | `0.9780` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 39,740.00 USD | 2,960.00 USD | 17,920.00 USD |
| `7D` | `0.9790` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 84,920.00 USD |
| `1D` | `0.9800` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 29,240.00 USD | 9,580.00 USD | 20,800.00 USD |
| `7D` | `0.9810` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 540.00 USD | 0.00 USD | 118,820.00 USD |
| `1D` | `0.9820` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 15,980.00 USD | 12,160.00 USD | 7,210.00 USD |
| `7D` | `0.9830` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 102,710.00 USD | 15,810.00 USD | 52,260.00 USD |
| `1D` | `0.9840` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 13,190.00 USD | 38,710.00 USD |
| `7D` | `0.9850` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,300.00 USD |
| `1D` | `0.9860` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 50,550.00 USD | 3,460.00 USD | 19,890.00 USD |
| `7D` | `0.9870` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 57,740.00 USD |
| `1D` | `0.9880` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 16,640.00 USD | 0.00 USD | 14,320.00 USD |
| `7D` | `0.9890` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `0.9900` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 57,390.00 USD | 1,300.00 USD | 13,390.00 USD |
| `7D` | `0.9910` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD |
| `1D` | `0.9920` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 8,950.00 USD | 2,810.00 USD | 13,340.00 USD |
| `7D` | `0.9930` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `0.9940` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 12,310.00 USD | 13,250.00 USD | 1,420.00 USD |
| `7D` | `0.9950` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 33,790.00 USD | 5,380.00 USD | 42,770.00 USD |
| `1D` | `0.9960` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 18,530.00 USD | 4,110.00 USD | 0.00 USD |
| `7D` | `0.9970` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 69,270.00 USD | 0.00 USD | 4,670.00 USD |
| `1D` | `0.9980` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 40,410.00 USD | 4,790.00 USD | 10,500.00 USD |
| `7D` | `0.9990` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 156.00 USD | 462.12 USD |
| `1D` | `1.00` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 59,960.00 USD | 28,860.00 USD | 1,710.00 USD |
| `7D` | `1.00` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.00` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 501.30 USD | 0.00 USD | 266.05 USD |
| `7D` | `1.00` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 105,110.00 USD | 21,740.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 10,110.00 USD | 9,540.00 USD | 9,410.00 USD |
| `7D` | `1.00` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 19,830.00 USD | 3,970.00 USD | 1,470.00 USD |
| `1D` | `1.01` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 101,040.00 USD | 10,140.00 USD | 31,440.00 USD |
| `7D` | `1.01` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 34,110.00 USD | 0.00 USD | 29,210.00 USD |
| `1D` | `1.01` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 10,110.00 USD | 9,160.00 USD | 27,730.00 USD |
| `7D` | `1.01` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD |
| `1D` | `1.01` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 10,530.00 USD | 14,710.00 USD | 0.00 USD |
| `7D` | `1.01` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 20,090.00 USD | 14,180.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 16,240.00 USD | 25,350.00 USD | 155.80 USD |
| `7D` | `1.01` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD |
| `1D` | `1.01` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 5,950.00 USD | 4,370.00 USD | 25,020.00 USD |
| `7D` | `1.01` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 26,360.00 USD | 7,070.00 USD |
| `1D` | `1.02` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 20,120.00 USD | 75.20 USD | 20,270.00 USD |
| `7D` | `1.02` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD |
| `1D` | `1.02` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 6,670.00 USD | 8,490.00 USD | 22,230.00 USD |
| `7D` | `1.02` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 315.97 USD | 75,760.00 USD | 11,810.00 USD |
| `1D` | `1.02` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 44,710.00 USD | 4,370.00 USD | 15,110.00 USD |
| `7D` | `1.02` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 44,170.00 USD | 32,840.00 USD | 68,050.00 USD |
| `1D` | `1.02` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 51,380.00 USD | 3,710.00 USD | 21,450.00 USD |
| `7D` | `1.02` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 66,990.00 USD | 85,890.00 USD | 146,060.00 USD |
| `1D` | `1.02` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 50,330.00 USD | 25,640.00 USD | 53,210.00 USD |
| `7D` | `1.02` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 28,320.00 USD | 48,490.00 USD | 29,170.00 USD |
| `1D` | `1.03` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 52,630.00 USD | 18,370.00 USD | 20,210.00 USD |
| `7D` | `1.03` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 161,070.00 USD | 127,000.00 USD | 25,260.00 USD |
| `1D` | `1.03` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 31,340.00 USD | 10,940.00 USD | 18,480.00 USD |
| `7D` | `1.03` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD |
| `1D` | `1.03` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 95,330.00 USD | 24,510.00 USD | 33,610.00 USD |
| `7D` | `1.03` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD |
| `1D` | `1.03` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 70,060.00 USD | 8,980.00 USD | 35,950.00 USD |
| `7D` | `1.03` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD |
| `1D` | `1.03` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 38,330.00 USD | 9,300.00 USD | 21,490.00 USD |
| `7D` | `1.03` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 259,060.00 USD | 8,290.00 USD | 43,490.00 USD |
| `1D` | `1.04` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 18,100.00 USD | 13,840.00 USD | 7,800.00 USD |
| `7D` | `1.04` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 192,080.00 USD | 3,170.00 USD | 109,460.00 USD |
| `1D` | `1.04` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 63,010.00 USD | 3,250.00 USD | 4,330.00 USD |
| `7D` | `1.04` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 239,580.00 USD | 9,010.00 USD | 117,630.00 USD |
| `1D` | `1.04` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 7,790.00 USD | 7,460.00 USD | 12,300.00 USD |
| `7D` | `1.04` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 276,890.00 USD | 2,090.00 USD | 159,500.00 USD |
| `1D` | `1.04` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 11,290.00 USD | 9,870.00 USD | 8,020.00 USD |
| `7D` | `1.04` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD |
| `1D` | `1.04` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 7,410.00 USD | 9,310.00 USD | 21,860.00 USD |
| `7D` | `1.04` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD |
| `1D` | `1.05` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 21,730.00 USD | 4,160.00 USD | 321.14 USD |
| `7D` | `1.05` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 178,890.00 USD | 96,370.00 USD | 238,570.00 USD |
| `1D` | `1.05` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 8,930.00 USD | 3,210.00 USD | 5,060.00 USD |
| `7D` | `1.05` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 116,670.00 USD | 13,780.00 USD | 77,320.00 USD |
| `1D` | `1.05` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 42,790.00 USD | 10,010.00 USD | 13,550.00 USD |
| `7D` | `1.05` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 175,350.00 USD | 43,690.00 USD | 87,370.00 USD |
| `1D` | `1.05` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 23,270.00 USD | 1,310.00 USD | 15,860.00 USD |
| `7D` | `1.05` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 68,590.00 USD | 58,070.00 USD | 74,380.00 USD |
| `1D` | `1.05` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 16,310.00 USD | 365.79 USD | 6,470.00 USD |
| `7D` | `1.05` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 125,020.00 USD | 33,860.00 USD | 72,330.00 USD |
| `1D` | `1.06` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 13,640.00 USD | 3,680.00 USD | 4,790.00 USD |
| `7D` | `1.06` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 218,860.00 USD | 70,000.00 USD | 106,380.00 USD |
| `1D` | `1.06` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 29,640.00 USD | 3,000.00 USD | 725.34 USD |
| `7D` | `1.06` | 9,220,000.00 USD | 9,220,000.00 USD | 0.00 USD | 240,060.00 USD | 74,380.00 USD | 145,470.00 USD |
| `1D` | `1.06` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 3,850.00 USD | 4,510.00 USD | 8,650.00 USD |
| `7D` | `1.06` | 9,500,000.00 USD | 9,500,000.00 USD | 0.00 USD | 140,850.00 USD | 56,310.00 USD | 78,020.00 USD |
| `1D` | `1.06` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 1,990.00 USD | 2,450.00 USD | 2,070.00 USD |
| `7D` | `1.06` | 9,780,000.00 USD | 9,780,000.00 USD | 0.00 USD | 141,700.00 USD | 73,690.00 USD | 71,340.00 USD |
| `1D` | `1.06` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 15,200.00 USD | 2,970.00 USD | 3,220.00 USD |
| `7D` | `1.06` | 10,000,000.00 USD | 10,000,000.00 USD | 0.00 USD | 90,670.00 USD | 28,390.00 USD | 95,080.00 USD |
| `1D` | `1.07` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 16,000.00 USD | 141.60 USD | 8,440.00 USD |
| `7D` | `1.07` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 86,760.00 USD | 43,390.00 USD | 82,980.00 USD |
| `1D` | `1.07` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 7,520.00 USD | 4,330.00 USD | 3,180.00 USD |
| `7D` | `1.07` | 10,510,000.00 USD | 10,510,000.00 USD | 0.00 USD | 219,670.00 USD | 14,440.00 USD | 62,270.00 USD |
| `1D` | `1.07` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 7,140.00 USD | 3,900.00 USD | 3,210.00 USD |
| `7D` | `1.07` | 10,740,000.00 USD | 10,740,000.00 USD | 0.00 USD | 141,570.00 USD | 36,670.00 USD | 52,290.00 USD |
| `1D` | `1.07` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 9,330.00 USD | 2,350.00 USD | 3,180.00 USD |
| `7D` | `1.07` | 10,970,000.00 USD | 10,970,000.00 USD | 0.00 USD | 96,630.00 USD | 42,960.00 USD | 95,510.00 USD |
| `1D` | `1.07` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 7,860.00 USD | 4,560.00 USD | 6,930.00 USD |
| `7D` | `1.07` | 11,160,000.00 USD | 11,160,000.00 USD | 0.00 USD | 97,650.00 USD | 27,560.00 USD | 60,670.00 USD |
| `1D` | `1.08` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 5,350.00 USD | 5,330.00 USD | 5,490.00 USD |
| `7D` | `1.08` | 11,310,000.00 USD | 11,310,000.00 USD | 0.00 USD | 75,040.00 USD | 29,910.00 USD | 48,910.00 USD |
| `1D` | `1.08` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 9,430.00 USD | 4,070.00 USD | 150.13 USD |
| `7D` | `1.08` | 11,550,000.00 USD | 11,550,000.00 USD | 0.00 USD | 166,380.00 USD | 21,060.00 USD | 52,480.00 USD |
| `1D` | `1.08` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 7,700.00 USD | 1,870.00 USD | 711.93 USD |
| `7D` | `1.08` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 164,440.00 USD | 26,480.00 USD | 33,950.00 USD |
| `1D` | `1.08` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 5,280.00 USD | 1,770.00 USD | 4,210.00 USD |
| `7D` | `1.08` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 61,330.00 USD | 41,110.00 USD | 100,750.00 USD |
| `1D` | `1.08` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 9,180.00 USD | 1,500.00 USD | 3,180.00 USD |
| `7D` | `1.08` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 86,400.00 USD | 18,540.00 USD | 46,440.00 USD |
| `1D` | `1.09` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 8,920.00 USD | 2,900.00 USD | 6,970.00 USD |
| `7D` | `1.09` | 12,360,000.00 USD | 12,360,000.00 USD | 0.00 USD | 102,510.00 USD | 58,170.00 USD | 69,640.00 USD |
| `1D` | `1.09` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 3,630.00 USD | 4,290.00 USD | 4,990.00 USD |
| `7D` | `1.09` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 71,650.00 USD | 23,140.00 USD | 85,300.00 USD |
| `1D` | `1.09` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 9,830.00 USD | 3,220.00 USD | 1,950.00 USD |
| `7D` | `1.09` | 12,670,000.00 USD | 12,670,000.00 USD | 0.00 USD | 70,660.00 USD | 25,660.00 USD | 32,870.00 USD |
| `1D` | `1.09` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 4,370.00 USD | 93.54 USD | 966.50 USD |
| `7D` | `1.09` | 12,830,000.00 USD | 12,830,000.00 USD | 0.00 USD | 59,760.00 USD | 39,220.00 USD | 62,330.00 USD |
| `1D` | `1.09` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 2,490.00 USD | 2,060.00 USD |
| `7D` | `1.09` | 13,000,000.00 USD | 13,000,000.00 USD | 0.00 USD | 56,240.00 USD | 22,740.00 USD | 92,520.00 USD |
| `1D` | `1.10` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 1,740.00 USD | 3,660.00 USD | 318.21 USD |
| `7D` | `1.10` | 13,140,000.00 USD | 13,140,000.00 USD | 0.00 USD | 86,360.00 USD | 13,380.00 USD | 38,150.00 USD |
| `1D` | `1.10` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 3,620.00 USD | 1,090.00 USD | 4,380.00 USD |
| `1D` | `1.10` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 1,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.10` | 13,470,000.00 USD | 13,470,000.00 USD | 0.00 USD | 188,000.00 USD | 49,370.00 USD | 89,650.00 USD |
| `7D` | `1.10` | 13,650,000.00 USD | 13,650,000.00 USD | 0.00 USD | 122,300.00 USD | 44,140.00 USD | 15,590.00 USD |
| `7D` | `1.10` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 91,720.00 USD | 19,140.00 USD | 110,190.00 USD |
| `7D` | `1.10` | 13,940,000.00 USD | 13,940,000.00 USD | 0.00 USD | 22,500.00 USD | 10,390.00 USD | 31,450.00 USD |
| `7D` | `1.11` | 14,050,000.00 USD | 14,050,000.00 USD | 0.00 USD | 51,840.00 USD | 24,280.00 USD | 34,190.00 USD |
| `7D` | `1.11` | 14,230,000.00 USD | 14,230,000.00 USD | 0.00 USD | 80,930.00 USD | 42,230.00 USD | 56,110.00 USD |
| `7D` | `1.11` | 14,380,000.00 USD | 14,380,000.00 USD | 0.00 USD | 69,040.00 USD | 16,050.00 USD | 64,910.00 USD |
| `7D` | `1.11` | 14,460,000.00 USD | 14,460,000.00 USD | 0.00 USD | 20,190.00 USD | 43,570.00 USD | 25,640.00 USD |
| `7D` | `1.11` | 14,520,000.00 USD | 14,520,000.00 USD | 0.00 USD | 34,700.00 USD | 6,650.00 USD | 9,420.00 USD |
| `7D` | `1.12` | 14,660,000.00 USD | 14,660,000.00 USD | 0.00 USD | 68,170.00 USD | 45,980.00 USD | 32,030.00 USD |
| `7D` | `1.12` | 14,720,000.00 USD | 14,720,000.00 USD | 0.00 USD | 24,700.00 USD | 22,760.00 USD | 13,750.00 USD |
| `7D` | `1.12` | 14,830,000.00 USD | 14,830,000.00 USD | 0.00 USD | 49,110.00 USD | 30,950.00 USD | 23,330.00 USD |
| `7D` | `1.12` | 14,920,000.00 USD | 14,920,000.00 USD | 0.00 USD | 61,780.00 USD | 7,080.00 USD | 25,460.00 USD |
| `7D` | `1.12` | 14,980,000.00 USD | 14,980,000.00 USD | 0.00 USD | 18,300.00 USD | 10,940.00 USD | 29,890.00 USD |
| `7D` | `1.13` | 15,000,000.00 USD | 15,000,000.00 USD | 0.00 USD | 14,700.00 USD | 342.11 USD | 8,690.00 USD |
| `7D` | `1.13` | 15,120,000.00 USD | 15,120,000.00 USD | 0.00 USD | 56,500.00 USD | 19,160.00 USD | 45,770.00 USD |
| `7D` | `1.13` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 106,510.00 USD | 12,730.00 USD | 90,150.00 USD |
| `7D` | `1.13` | 15,440,000.00 USD | 15,440,000.00 USD | 0.00 USD | 77,640.00 USD | 4,280.00 USD | 27,360.00 USD |
| `7D` | `1.14` | 15,530,000.00 USD | 15,530,000.00 USD | 0.00 USD | 16,300.00 USD | 10,920.00 USD | 61,260.00 USD |
| `7D` | `1.14` | 15,550,000.00 USD | 15,550,000.00 USD | 0.00 USD | 4,780.00 USD | 4,820.00 USD | 6,530.00 USD |
| `7D` | `1.14` | 15,590,000.00 USD | 15,590,000.00 USD | 0.00 USD | 2,980.00 USD | 0.00 USD | 35,230.00 USD |
| `7D` | `1.14` | 15,640,000.00 USD | 15,640,000.00 USD | 0.00 USD | 36,300.00 USD | 8,480.00 USD | 6,790.00 USD |
| `7D` | `1.14` | 15,710,000.00 USD | 15,710,000.00 USD | 0.00 USD | 36,560.00 USD | 1,660.00 USD | 37,230.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `191.63M` | Total OI Tokens: `210,297,945.8 DOT`
  * 1h OI Change: `-8.15%` | 4h OI Change: `-9.85%` | 24h OI Change: `-13.51%`
  * Exchange Breakdown: Binance=`33.66M` | Bybit=`21.99M` | OKX=`9.72M` | Hyperliquid=`5.41M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.23K` | Last 24h: `7.91K` | Last 3d: `-10.37K` | Last 7d: `-19.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0004%` | **USDT OKX** | `0.0020%` |
| **USDT Bybit** | `0.0065%` | **USDT KuCoin** | `0.0036%` |
| **USDT MEXC** | `-0.0005%` | **USDT BingX** | `0.0078%` |
| **USDT Gate** | `-0.0072%` | **USDT Bitget** | `-0.0028%` |
| **CoinM Binance** | `0.0082%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `45.54%` | `54.46%` | `0.84` | 42,950,000.00 USD |
| `15M` | `Binance` | `41.76%` | `58.24%` | `0.72` | 15,900,000.00 USD |
| `15M` | `OKX` | `47.6%` | `52.4%` | `0.91` | 5,650,000.00 USD |
| `15M` | `Bybit` | `44.93%` | `55.07%` | `0.82` | 5,900,000.00 USD |
| `15M` | `KuCoin` | `43.19%` | `56.81%` | `0.76` | 855,440.00 USD |
| `15M` | `Gate` | `56.23%` | `43.77%` | `1.28` | 4,060,000.00 USD |
| `15M` | `Bitget` | `50.96%` | `49.04%` | `1.04` | 2,470,000.00 USD |
| `15M` | `BingX` | `39.23%` | `60.77%` | `0.65` | 823,250.00 USD |
| `15M` | `MEXC` | `39.3%` | `60.7%` | `0.65` | 2,290,000.00 USD |
| `15M` | `Bitunix` | `45.93%` | `54.07%` | `0.85` | 1,210,000.00 USD |
| `15M` | `Hyperliquid` | `53.32%` | `46.68%` | `1.14` | 948,080.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.61%` | `49.39%` | `1.02` | 2,450,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `17.51%` | `82.49%` | `0.21` | 138,460.00 USD |
| `15M` | `HTX` | `57.55%` | `42.45%` | `1.36` | 77,480.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `37.35%` | `62.65%` | `0.60` | 117,030.00 USD |
| `15M` | `Aster` | `52.04%` | `47.96%` | `1.09` | 67,810.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `41.76%` | `58.24%` | `0.72` | 15,900,000.00 USD |
| `15M` | `Global Accounts` | `45.54%` | `54.46%` | `0.84` | 42,950,000.00 USD |
| `1H` | `DOT` | `44.22%` | `55.78%` | `0.79` | 69,130,000.00 USD |
| `1H` | `Binance` | `42.44%` | `57.56%` | `0.74` | 25,480,000.00 USD |
| `1H` | `OKX` | `46.18%` | `53.82%` | `0.86` | 8,590,000.00 USD |
| `1H` | `Bybit` | `41.18%` | `58.82%` | `0.70` | 9,050,000.00 USD |
| `1H` | `KuCoin` | `44.56%` | `55.44%` | `0.80` | 1,390,000.00 USD |
| `1H` | `Gate` | `53.16%` | `46.84%` | `1.13` | 6,900,000.00 USD |
| `1H` | `Bitget` | `46.99%` | `53.01%` | `0.89` | 3,810,000.00 USD |
| `1H` | `BingX` | `39.08%` | `60.92%` | `0.64` | 1,360,000.00 USD |
| `1H` | `MEXC` | `38.5%` | `61.5%` | `0.63` | 4,100,000.00 USD |
| `1H` | `Bitunix` | `45.95%` | `54.05%` | `0.85` | 1,980,000.00 USD |
| `1H` | `Hyperliquid` | `49.06%` | `50.94%` | `0.96` | 1,460,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.19%` | `52.81%` | `0.89` | 4,170,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `18.67%` | `81.33%` | `0.23` | 421,180.00 USD |
| `1H` | `HTX` | `52.2%` | `47.8%` | `1.09` | 106,080.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `47.84%` | `52.16%` | `0.92` | 222,030.00 USD |
| `1H` | `Aster` | `45.63%` | `54.37%` | `0.84` | 88,620.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `42.44%` | `57.56%` | `0.74` | 25,480,000.00 USD |
| `1H` | `Global Accounts` | `44.22%` | `55.78%` | `0.79` | 69,130,000.00 USD |
| `4H` | `DOT` | `45.19%` | `54.81%` | `0.82` | 93,360,000.00 USD |
| `4H` | `Binance` | `44.37%` | `55.63%` | `0.80` | 34,370,000.00 USD |
| `4H` | `OKX` | `46.93%` | `53.07%` | `0.88` | 10,730,000.00 USD |
| `4H` | `Bybit` | `42.78%` | `57.22%` | `0.75` | 11,110,000.00 USD |
| `4H` | `KuCoin` | `47.15%` | `52.85%` | `0.89` | 2,610,000.00 USD |
| `4H` | `Gate` | `52.08%` | `47.92%` | `1.09` | 7,990,000.00 USD |
| `4H` | `Bitget` | `47.88%` | `52.12%` | `0.92` | 4,590,000.00 USD |
| `4H` | `BingX` | `40.65%` | `59.35%` | `0.68` | 3,190,000.00 USD |
| `4H` | `MEXC` | `41.36%` | `58.64%` | `0.71` | 5,440,000.00 USD |
| `4H` | `Bitunix` | `47.09%` | `52.91%` | `0.89` | 2,480,000.00 USD |
| `4H` | `Hyperliquid` | `45.15%` | `54.85%` | `0.82` | 1,740,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.35%` | `50.65%` | `0.97` | 7,340,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `14.46%` | `85.54%` | `0.17` | 1,240,000.00 USD |
| `4H` | `HTX` | `52.99%` | `47.01%` | `1.13` | 126,200.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `48.8%` | `51.2%` | `0.95` | 307,060.00 USD |
| `4H` | `Aster` | `43.91%` | `56.09%` | `0.78` | 98,940.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `44.37%` | `55.63%` | `0.80` | 34,370,000.00 USD |
| `4H` | `Global Accounts` | `45.19%` | `54.81%` | `0.82` | 93,360,000.00 USD |


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
| `0:00 UTC` | `0.9139` | `0.9141` | `0.9139` | `0.9211` | `0.9075` | 1,209,776.01 USD | 429,114.92 USD | 780,661.09 USD | -351,546.17 USD | `-29.06%` | `27B / 20S` |

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
| `5m` | 62,640.00 USD | -251,550.00 USD | **`DISTRIBUTION`** |
| `15m` | 285,770.00 USD | -73,420.00 USD | **`ACCUMULATION`** |
| `30m` | -676,410.00 USD | -5,290,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -860,470.00 USD | -5,950,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -908,340.00 USD | -6,020,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,050,000.00 USD | -6,280,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,080,000.00 USD | -7,330,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,000,000.00 USD | -7,390,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,160,000.00 USD | -7,860,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,310,000.00 USD | -7,860,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,250,000.00 USD | -24,640,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,610,000.00 USD | -78,740,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+62.64K` | 15m=`+285.77K` | 1h=`-860.47K` | 24h=`-1.31M`
* Futures Capital Netflows: 5m=`-251.55K` | 15m=`-73.42K` | 1h=`-5.95M` | 24h=`-7.86M`
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
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:30:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.9050` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.8574` (Risk Distance: `0.0476` pts)
  * +2.5R Take Profit: `1.02`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9078` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9554` (Risk Distance: `0.0476` pts)
  * +2.5R Take Profit: `0.7889`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9228`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
