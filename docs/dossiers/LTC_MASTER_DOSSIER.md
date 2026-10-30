# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 08:54:59 IST` (`2026-10-30 03:24:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `55.25` | **Live Ask Quote**: `55.55` | **Mid Price**: `55.40`
- **Spread Points**: `300.00` | **Spread BPS**: `54.15 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `0.01 USD` | Point Value (0.01 Lot): `0.0001 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `54.06` | VWAP Z-Score: `+1.83` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.5355` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `49.41` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `55.58` | Lower -3.00σ Band: `52.55`
  * Upper +2.51σ Band: `55.33` | Lower -2.51σ Band: `52.80`
  * Upper +2.01σ Band: `55.08` | Lower -2.01σ Band: `53.05`
  * Upper +2.00σ Band: `55.07` | Lower -2.00σ Band: `53.05`
  * Upper +1.28σ Band: `54.71` | Lower -1.28σ Band: `53.42`
  * Upper +1.00σ Band: `54.57` | Lower -1.00σ Band: `53.56`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`54.66` | EMA-20=`54.81` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`55.70` (Slope: `+0.0000`) | EMA-100=`56.46`
  * Institutional Anchors: EMA-144=`56.72` | EMA-200=`56.75` (Slope: `-0.5487`) | EMA-233=`56.81`
- **Range Boundaries**: 24H High=`58.72` | 24H Low=`52.64` | Weekly High=`59.62` | Weekly Low=`52.64`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `55.66` (Distance: `-0.51%`)
  * Point of Control (POC) = `55.27` (Distance: `+0.19%`)
  * Value Area Low (VAL) = `54.10` (Distance: `+2.36%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.40` | POC=`57.72` | VAL=`56.83`
  * Prior Day Extremes: PDH=`59.52` | PDL=`54.18` | PDC=`54.46`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`58.34` | Weekly POC=`56.43` | Weekly VAL=`55.97`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`55.89` | Low=`52.64`
  * London Session (08:00-16:00 UTC): High=`55.62` | Low=`55.18`
  * New York Session (13:00-21:00 UTC): High=`55.73` | Low=`55.07`
  * Initial Balance (First Hour): IB High=`55.57` | IB Low=`55.23`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `55.18` - `55.62`
  * Optimal Trade Entry (OTE 0.705): `55.51`
  * Structural Invalidation Anchor (0.786): `55.84`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `55.09` | `55.14` | `55.04` | `55.13` | `3,830` | 211,020.58 USD | -71,329.32 USD | `-33.80%` | -4,224,102.28 USD | `-0.58` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `55.13` | `55.38` | `55.11` | `55.25` | `6,270` | 346,629.86 USD | -69,858.44 USD | `-20.15%` | -4,293,960.72 USD | `-0.54` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `55.26` | `55.43` | `55.20` | `55.41` | `4,424` | 244,714.58 USD | 50,327.72 USD | `+20.57%` | -4,243,633.00 USD | `+0.55` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `55.04` | `55.34` | `55.00` | `55.26` | `30,044` | 1,657,433.83 USD | -2,904.65 USD | `-0.18%` | -3,812,677.83 USD | `+0.29` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `55.27` | `55.27` | `54.97` | `55.13` | `15,673` | 863,748.33 USD | -386,338.95 USD | `-44.73%` | -4,199,016.78 USD | `-0.99` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `55.13` | `55.43` | `55.11` | `55.41` | `10,694` | 591,344.44 USD | -19,530.72 USD | `-3.30%` | -4,218,547.50 USD | `+0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `54.36` | `54.62` | `53.64` | `54.29` | `95,012` | 5,151,310.38 USD | -124,905.13 USD | `-2.42%` | -4,162,296.53 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `54.30` | `55.34` | `53.91` | `55.13` | `78,887` | 4,333,440.29 USD | -426,625.42 USD | `-9.84%` | -4,588,921.95 USD | `-0.29` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `55.13` | `55.43` | `55.11` | `55.41` | `10,694` | 591,344.44 USD | -19,530.72 USD | `-3.30%` | -4,608,452.67 USD | `+0.23` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | 340,473.45 USD | `+0.15` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,923,567.46 USD | `-1.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `55.43` | `52.77` | `55.41` | `479,635` | 25,953,325.50 USD | -1,684,885.21 USD | `-6.49%` | -4,608,452.67 USD | `-0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `57.04` | `58.16` | `56.85` | `58.00` | `178,996` | 10,300,529.12 USD | 452,809.17 USD | `+4.40%` | -47,398.66 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | 201,186.90 USD | `+0.44` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | 340,473.45 USD | `+0.15` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,923,567.46 USD | `-1.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `55.43` | `52.77` | `55.41` | `479,635` | 25,953,325.50 USD | -1,684,885.21 USD | `-6.49%` | -4,608,452.67 USD | `-0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:53:31 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1071` | `0xeadc...9d55` | `LONG` | 2,015,680.74 USD | `36,463.77` | `52.78` | `55.38` | `0.000000` | 91,004.79 USD | `+4.51%` | `10X Cross` |
| `1078` | `0x9aa5...58af` | `SHORT` | 2,002,758.53 USD | `36,177.65` | `71.22` | `55.38` | `309.69` | 573,728.14 USD | `+28.65%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `59.36` | 7,245.48 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.25K USD at 59.3600 USD [API] | `2026-10-28 21:23:31` |
| `ANNOUNCEMENT` | `INFO` | `59.35` | 7,506.71 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 59.3510 USD [API] | `2026-10-28 21:23:31` |
| `ANNOUNCEMENT` | `INFO` | `59.23` | 5,285.54 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.29K USD at 59.2350 USD [API] | `2026-10-28 22:05:44` |
| `ANNOUNCEMENT` | `INFO` | `59.50` | 5,882.07 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 5.88K USD at 59.4990 USD [API] | `2026-10-28 22:34:27` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`59.03` (Vol: 286,000.00 USD, Dist: `+6.81%`) | Long MP=`54.13` (Vol: 113,000.00 USD, Dist: `--2.06%`)
  * 48H Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.75%`) | Long MP=`54.12` (Vol: 113,000.00 USD, Dist: `--2.09%`)
  * 3D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.75%`) | Long MP=`52.66` (Vol: 75,900.00 USD, Dist: `--4.72%`)
  * 7D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.75%`) | Long MP=`54.12` (Vol: 113,000.00 USD, Dist: `--2.09%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `11.35` | 363.20 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `11.45` | 366.40 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.25` | 122.50 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.75` | 2,560.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.15` | 2,220.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.65` | 150.15 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `15.65` | 182.48 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.05` | 113.72 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.35` | 307.18 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.85` | 2,260.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.05` | 3,470.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.45` | 2,010.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.45` | 3,080.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.95` | 19,480.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.35` | 179.92 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.45` | 323.28 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.05` | 4,870.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.85` | 195.57 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.65` | 485.36 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.75` | 1,490.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.05` | 561.62 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 277,980.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 173.39 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 50,740.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 374.20 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.05` | 5,510.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.35` | 124,900.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 272.75 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 1,260.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.65` | 8,600.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.95` | 8,530.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 755.28 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.55` | 657.19 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 297,500.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 218.46 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.35` | 569.06 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 538.53 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 5,880.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 1,060.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.65` | 4,920.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 2,870.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 125.24 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.05` | 22,370.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 450.10 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.35` | 1,070.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 653.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 953.68 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 35,660.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 257.76 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.75` | 4,190.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 182.85 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 6,080.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.45` | 65,890.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 3,240.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 104.85 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 166.49 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.75` | 4,670.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.85` | 179.25 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 3,020.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 423.18 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 101.80 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 438.74 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 9,520.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.45` | 1,060.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 3,530.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 377.50 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 6,210.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 446.67 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.25` | 1,150.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 847.54 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 2,400.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 993.82 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 4,280.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.85` | 1,940.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 2,730.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 664,760.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 570.02 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.25` | 638.99 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 1,290.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 716.41 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 312.44 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 5,900.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 1,180.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 133.10 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 2,160.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 1,010.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 133.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 274.39 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 6,340.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 509.01 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 396.54 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 55,740.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 644.96 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 982.29 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 69,270.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 44,700.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 7,190.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 5,800.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 2,000.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 9,080.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 122,400.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 417.80 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 5,390.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 980.67 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 426.02 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 21,880.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 801.14 USD | 989,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 3,980.00 USD | 989,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 2,380.00 USD | 985,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 84,440.00 USD | 982,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 842.44 USD | 898,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.65` | 531.34 USD | 897,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 32,450.00 USD | 896,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 134.55 USD | 864,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 2,620.00 USD | 864,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 4,830.00 USD | 861,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 8,710.00 USD | 856,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 3,180.00 USD | 848,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 4,740.00 USD | 844,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 23,940.00 USD | 840,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 13,200.00 USD | 816,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 42,180.00 USD | 803,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.85` | 326.91 USD | 760,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 4,320.00 USD | 760,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 706.41 USD | 756,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.15` | 5,940.00 USD | 755,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.25` | 842.21 USD | 749,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.35` | 383.78 USD | 748,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 24,670.00 USD | 748,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 4,330.00 USD | 723,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 358.40 USD | 719,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 158.22 USD | 719,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 1,980.00 USD | 718,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 2,320.00 USD | 716,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.35` | 43,340.00 USD | 714,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.45` | 2,180.00 USD | 671,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 4,450.00 USD | 669,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 47,750.00 USD | 664,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.85` | 3,800.00 USD | 616,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 1,340.00 USD | 613,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 1,690.00 USD | 611,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 525.44 USD | 610,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.45` | 279.07 USD | 609,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 2,560.00 USD | 609,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 273.90 USD | 606,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 333.94 USD | 606,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 252.58 USD | 606,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,580.00 USD | 605,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 15,740.00 USD | 604,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.30` | 2,870,000.00 USD | 2,870,000.00 USD | 13,300.00 USD | 4,090.00 USD | 367.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.30` | 8,100,000.00 USD | 8,100,000.00 USD | 15,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.35` | 5,230.00 USD | 588,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.40` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 626.48 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.40` | 8,080,000.00 USD | 8,080,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.45` | 419.34 USD | 583,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.50` | 2,850,000.00 USD | 2,850,000.00 USD | 1,180.00 USD | 4,200.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.50` | 8,070,000.00 USD | 8,070,000.00 USD | 1,130.00 USD | 6,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.55` | 37,080.00 USD | 582,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.60` | 2,830,000.00 USD | 2,830,000.00 USD | 980.75 USD | 4,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.60` | 8,070,000.00 USD | 8,070,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.65` | 73,260.00 USD | 545,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.70` | 2,820,000.00 USD | 2,820,000.00 USD | 3,550.00 USD | 1,980.00 USD | 416.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.70` | 8,050,000.00 USD | 8,050,000.00 USD | 788.92 USD | 0.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.75` | 1,770.00 USD | 472,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.80` | 2,820,000.00 USD | 2,820,000.00 USD | 2,920.00 USD | 388.95 USD | 14,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.80` | 8,040,000.00 USD | 8,040,000.00 USD | 8,590.00 USD | 8,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `49.90` | 2,800,000.00 USD | 2,800,000.00 USD | 17,280.00 USD | 8,370.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.90` | 8,030,000.00 USD | 8,030,000.00 USD | 45,030.00 USD | 7,170.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.95` | 19,920.00 USD | 470,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.00` | 2,750,000.00 USD | 2,750,000.00 USD | 7,520.00 USD | 6,290.00 USD | 40,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.00` | 7,970,000.00 USD | 7,970,000.00 USD | 22,100.00 USD | 7,630.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.05` | 1,820.00 USD | 450,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.10` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.10` | 7,920,000.00 USD | 7,920,000.00 USD | 363.50 USD | 682.90 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.20` | 7,920,000.00 USD | 7,920,000.00 USD | 6,960.00 USD | 500.40 USD | 34,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.25` | 102.51 USD | 448,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.30` | 7,870,000.00 USD | 7,870,000.00 USD | 16,270.00 USD | 3,640.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.35` | 1,140.00 USD | 448,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.40` | 2,690,000.00 USD | 2,690,000.00 USD | 349.63 USD | 2,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.40` | 7,850,000.00 USD | 7,850,000.00 USD | 23,520.00 USD | 19,110.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,720.00 USD | 447,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.50` | 7,780,000.00 USD | 7,780,000.00 USD | 24,840.00 USD | 6,790.00 USD | 43,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.55` | 84,100.00 USD | 443,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.60` | 7,700,000.00 USD | 7,700,000.00 USD | 52,670.00 USD | 17,830.00 USD | 22,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.70` | 7,610,000.00 USD | 7,610,000.00 USD | 53,670.00 USD | 24,710.00 USD | 32,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.75` | 9,050.00 USD | 358,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.80` | 2,690,000.00 USD | 2,690,000.00 USD | 5,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.80` | 7,500,000.00 USD | 7,500,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.90` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 497.60 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.90` | 7,400,000.00 USD | 7,400,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.95` | 431.55 USD | 349,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.00` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 129.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.00` | 7,150,000.00 USD | 7,150,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.10` | 2,680,000.00 USD | 2,680,000.00 USD | 263.90 USD | 1,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.10` | 7,020,000.00 USD | 7,020,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.15` | 219,370.00 USD | 349,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.20` | 2,680,000.00 USD | 2,680,000.00 USD | 1,100.00 USD | 1,130.00 USD | 327.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.20` | 6,940,000.00 USD | 6,940,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.25` | 202.44 USD | 130,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.30` | 2,670,000.00 USD | 2,670,000.00 USD | 20,430.00 USD | 5,180.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.30` | 6,870,000.00 USD | 6,870,000.00 USD | 19,510.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.35` | 453.93 USD | 129,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.40` | 2,630,000.00 USD | 2,630,000.00 USD | 17,800.00 USD | 7,000.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.40` | 6,800,000.00 USD | 6,800,000.00 USD | 73,130.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.45` | 27,210.00 USD | 129,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.50` | 2,590,000.00 USD | 2,590,000.00 USD | 11,810.00 USD | 9,610.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.50` | 6,650,000.00 USD | 6,650,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.55` | 551.07 USD | 102,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.60` | 2,570,000.00 USD | 2,570,000.00 USD | 9,850.00 USD | 8,110.00 USD | 4,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.60` | 6,560,000.00 USD | 6,560,000.00 USD | 35,880.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.65` | 9,100.00 USD | 101,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.70` | 2,550,000.00 USD | 2,550,000.00 USD | 5,340.00 USD | 3,950.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.70` | 6,490,000.00 USD | 6,490,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.75` | 6,480.00 USD | 92,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.80` | 2,530,000.00 USD | 2,530,000.00 USD | 13,220.00 USD | 2,980.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.80` | 6,450,000.00 USD | 6,450,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.85` | 13,890.00 USD | 86,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.90` | 2,500,000.00 USD | 2,500,000.00 USD | 12,520.00 USD | 19,700.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.90` | 6,400,000.00 USD | 6,400,000.00 USD | 5,870.00 USD | 15,810.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.95` | 13,950.00 USD | 72,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.00` | 2,460,000.00 USD | 2,460,000.00 USD | 25,510.00 USD | 8,240.00 USD | 23,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.00` | 6,370,000.00 USD | 6,370,000.00 USD | 64,300.00 USD | 20,800.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.10` | 2,400,000.00 USD | 2,400,000.00 USD | 27,630.00 USD | 6,280.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 6,270,000.00 USD | 6,270,000.00 USD | 24,220.00 USD | 18,810.00 USD | 35,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.15` | 3,350.00 USD | 58,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.20` | 2,340,000.00 USD | 2,340,000.00 USD | 20,520.00 USD | 11,250.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 6,190,000.00 USD | 6,190,000.00 USD | 38,380.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.25` | 4,930.00 USD | 54,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.30` | 2,290,000.00 USD | 2,290,000.00 USD | 39,260.00 USD | 7,260.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 6,130,000.00 USD | 6,130,000.00 USD | 21,450.00 USD | 12,840.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.35` | 3,010.00 USD | 49,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.40` | 2,230,000.00 USD | 2,230,000.00 USD | 11,920.00 USD | 7,830.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 6,080,000.00 USD | 6,080,000.00 USD | 20,580.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.45` | 2,220.00 USD | 46,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.50` | 2,200,000.00 USD | 2,200,000.00 USD | 49,720.00 USD | 13,570.00 USD | 998.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.50` | 6,030,000.00 USD | 6,030,000.00 USD | 36,050.00 USD | 667.05 USD | 11,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.55` | 8,700.00 USD | 44,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.60` | 2,140,000.00 USD | 2,140,000.00 USD | 5,230.00 USD | 9,230.00 USD | 506.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.60` | 5,980,000.00 USD | 5,980,000.00 USD | 74,610.00 USD | 14,530.00 USD | 584.77 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.70` | 2,120,000.00 USD | 2,120,000.00 USD | 13,770.00 USD | 8,280.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.70` | 5,890,000.00 USD | 5,890,000.00 USD | 20,250.00 USD | 43,820.00 USD | 62,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.75` | 4,240.00 USD | 36,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.80` | 2,080,000.00 USD | 2,080,000.00 USD | 14,400.00 USD | 16,180.00 USD | 74,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.80` | 5,770,000.00 USD | 5,770,000.00 USD | 46,600.00 USD | 29,900.00 USD | 108.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.85` | 5,950.00 USD | 31,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.90` | 1,980,000.00 USD | 1,980,000.00 USD | 40,590.00 USD | 10,870.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.90` | 5,690,000.00 USD | 5,690,000.00 USD | 51,920.00 USD | 26,170.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.95` | 25,840.00 USD | 25,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.00` | 1,920,000.00 USD | 1,920,000.00 USD | 9,470.00 USD | 10,940.00 USD | 4,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.00` | 5,580,000.00 USD | 5,580,000.00 USD | 18,990.00 USD | 10,540.00 USD | 55,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.10` | 1,900,000.00 USD | 1,900,000.00 USD | 27,870.00 USD | 10,120.00 USD | 60,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.10` | 5,490,000.00 USD | 5,490,000.00 USD | 52,760.00 USD | 37,960.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.20` | 1,800,000.00 USD | 1,800,000.00 USD | 68,380.00 USD | 25,970.00 USD | 63,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.20` | 5,390,000.00 USD | 5,390,000.00 USD | 162,460.00 USD | 42,920.00 USD | 27,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.30` | 1,640,000.00 USD | 1,640,000.00 USD | 32,910.00 USD | 26,340.00 USD | 41,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.30` | 5,160,000.00 USD | 5,160,000.00 USD | 63,050.00 USD | 18,150.00 USD | 37,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.40` | 1,540,000.00 USD | 1,540,000.00 USD | 14,390.00 USD | 16,470.00 USD | 75,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.40` | 5,040,000.00 USD | 5,040,000.00 USD | 48,160.00 USD | 18,090.00 USD | 95,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.50` | 1,430,000.00 USD | 1,430,000.00 USD | 14,780.00 USD | 11,880.00 USD | 7,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.50` | 4,880,000.00 USD | 4,880,000.00 USD | 49,490.00 USD | 8,960.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.60` | 1,400,000.00 USD | 1,400,000.00 USD | 74,660.00 USD | 19,660.00 USD | 1,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.60` | 4,800,000.00 USD | 4,800,000.00 USD | 53,580.00 USD | 5,690.00 USD | 98,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.70` | 1,300,000.00 USD | 1,300,000.00 USD | 5,710.00 USD | 7,700.00 USD | 465.28 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.70` | 4,640,000.00 USD | 4,640,000.00 USD | 131,400.00 USD | 14,420.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.80` | 1,290,000.00 USD | 1,290,000.00 USD | 16,800.00 USD | 5,280.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.80` | 4,490,000.00 USD | 4,490,000.00 USD | 99,150.00 USD | 80,510.00 USD | 126,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.90` | 1,260,000.00 USD | 1,260,000.00 USD | 7,480.00 USD | 26,500.00 USD | 125,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.90` | 4,180,000.00 USD | 4,180,000.00 USD | 111,970.00 USD | 56,750.00 USD | 123,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.00` | 1,100,000.00 USD | 1,100,000.00 USD | 28,730.00 USD | 21,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.00` | 3,890,000.00 USD | 3,890,000.00 USD | 344,710.00 USD | 148,420.00 USD | 271,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.10` | 1,050,000.00 USD | 1,050,000.00 USD | 34,220.00 USD | 18,680.00 USD | 6,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.10` | 3,130,000.00 USD | 3,130,000.00 USD | 234,120.00 USD | 48,800.00 USD | 184,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.20` | 993,930.00 USD | 993,930.00 USD | 64,160.00 USD | 16,200.00 USD | 120,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.20` | 2,660,000.00 USD | 2,660,000.00 USD | 234,980.00 USD | 158,770.00 USD | 128,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.30` | 793,560.00 USD | 793,560.00 USD | 127,400.00 USD | 44,430.00 USD | 148,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.30` | 2,140,000.00 USD | 2,140,000.00 USD | 381,380.00 USD | 140,500.00 USD | 185,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.40` | 473,060.00 USD | 473,060.00 USD | 52,750.00 USD | 45,620.00 USD | 78,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.40` | 1,430,000.00 USD | 1,430,000.00 USD | 304,270.00 USD | 13,830.00 USD | 92,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.50` | 296,420.00 USD | 296,420.00 USD | 9,670.00 USD | 26,440.00 USD | 144,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.50` | 1,020,000.00 USD | 1,020,000.00 USD | 159,720.00 USD | 36,920.00 USD | 237,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.60` | 116,240.00 USD | 116,240.00 USD | 18,470.00 USD | 16,730.00 USD | 14,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.60` | 584,340.00 USD | 584,340.00 USD | 0.00 USD | 1,930.00 USD | 72,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.70` | 66,720.00 USD | 66,720.00 USD | 0.00 USD | 0.00 USD | 57,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.70` | 510,010.00 USD | 510,010.00 USD | 0.00 USD | 0.00 USD | 173,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.80` | 9,610.00 USD | 9,610.00 USD | 0.00 USD | 9,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.10` | 189.61 USD | 189.61 USD | 0.00 USD | 0.00 USD | 189.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.20` | 336,630.00 USD | 336,630.00 USD | 336,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.60` | 426,340.00 USD | 426,340.00 USD | 426,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.70` | 407.86 USD | 407.86 USD | 0.00 USD | 0.00 USD | 407.86 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.70` | 632,770.00 USD | 632,770.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.80` | 64,490.00 USD | 64,490.00 USD | 0.00 USD | 17,410.00 USD | 46,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.80` | 723,740.00 USD | 723,740.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `55.85` | 741.13 USD | 741.13 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `55.90` | 344,790.00 USD | 344,790.00 USD | 137,200.00 USD | 2,990.00 USD | 140,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.90` | 930,900.00 USD | 930,900.00 USD | 141,330.00 USD | 65,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.00` | 544,060.00 USD | 544,060.00 USD | 139,840.00 USD | 0.00 USD | 59,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.00` | 1,360,000.00 USD | 1,360,000.00 USD | 181,230.00 USD | 98,600.00 USD | 147,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `56.05` | 2,410.00 USD | 3,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `56.10` | 851,070.00 USD | 851,070.00 USD | 105,950.00 USD | 26,500.00 USD | 174,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.10` | 1,690,000.00 USD | 1,690,000.00 USD | 121,920.00 USD | 144,120.00 USD | 61,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.20` | 1,110,000.00 USD | 1,110,000.00 USD | 96,820.00 USD | 86,290.00 USD | 71,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.20` | 2,100,000.00 USD | 2,100,000.00 USD | 104,510.00 USD | 72,410.00 USD | 240,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.30` | 1,220,000.00 USD | 1,220,000.00 USD | 10,860.00 USD | 55,630.00 USD | 43,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.30` | 2,460,000.00 USD | 2,460,000.00 USD | 91,850.00 USD | 132,300.00 USD | 131,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.40` | 1,550,000.00 USD | 1,550,000.00 USD | 49,190.00 USD | 51,430.00 USD | 237,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.40` | 2,930,000.00 USD | 2,930,000.00 USD | 215,940.00 USD | 119,990.00 USD | 137,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.50` | 1,960,000.00 USD | 1,960,000.00 USD | 117,430.00 USD | 164,400.00 USD | 120,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.50` | 3,240,000.00 USD | 3,240,000.00 USD | 170,750.00 USD | 134,140.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.60` | 2,190,000.00 USD | 2,190,000.00 USD | 49,560.00 USD | 105,330.00 USD | 77,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.60` | 3,730,000.00 USD | 3,730,000.00 USD | 363,190.00 USD | 126,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.70` | 2,760,000.00 USD | 2,760,000.00 USD | 201,670.00 USD | 26,440.00 USD | 338,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.70` | 4,060,000.00 USD | 4,060,000.00 USD | 110,940.00 USD | 121,500.00 USD | 96,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.80` | 3,080,000.00 USD | 3,080,000.00 USD | 191,190.00 USD | 18,260.00 USD | 115,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.80` | 4,570,000.00 USD | 4,570,000.00 USD | 153,580.00 USD | 92,780.00 USD | 261,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.90` | 3,120,000.00 USD | 3,120,000.00 USD | 33,240.00 USD | 8,700.00 USD | 1,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.90` | 4,990,000.00 USD | 4,990,000.00 USD | 108,440.00 USD | 48,600.00 USD | 266,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.00` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 10,920.00 USD | 659.87 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.00` | 5,170,000.00 USD | 5,170,000.00 USD | 88,680.00 USD | 2,620.00 USD | 93,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.10` | 3,160,000.00 USD | 3,160,000.00 USD | 7,480.00 USD | 10,560.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.10` | 5,250,000.00 USD | 5,250,000.00 USD | 36,580.00 USD | 16,110.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.20` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 13,250.00 USD | 63,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.20` | 5,290,000.00 USD | 5,290,000.00 USD | 21,160.00 USD | 15,720.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.30` | 3,260,000.00 USD | 3,260,000.00 USD | 12,360.00 USD | 10,870.00 USD | 386.57 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.30` | 5,350,000.00 USD | 5,350,000.00 USD | 22,360.00 USD | 3,150.00 USD | 34,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.40` | 3,320,000.00 USD | 3,320,000.00 USD | 24,850.00 USD | 35,100.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.40` | 5,570,000.00 USD | 5,570,000.00 USD | 38,520.00 USD | 31,660.00 USD | 153,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.50` | 3,570,000.00 USD | 3,570,000.00 USD | 133,260.00 USD | 20,440.00 USD | 96,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.50` | 5,680,000.00 USD | 5,680,000.00 USD | 76,670.00 USD | 31,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.60` | 3,710,000.00 USD | 3,710,000.00 USD | 58,710.00 USD | 22,220.00 USD | 60,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.60` | 5,890,000.00 USD | 5,890,000.00 USD | 144,800.00 USD | 40,430.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.70` | 3,870,000.00 USD | 3,870,000.00 USD | 35,650.00 USD | 26,090.00 USD | 96,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.70` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 5,400.00 USD | 57,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.80` | 3,960,000.00 USD | 3,960,000.00 USD | 5,680.00 USD | 13,220.00 USD | 72,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.80` | 6,020,000.00 USD | 6,020,000.00 USD | 2,260.00 USD | 14,360.00 USD | 48,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.90` | 3,990,000.00 USD | 3,990,000.00 USD | 9,940.00 USD | 14,110.00 USD | 7,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.90` | 6,030,000.00 USD | 6,030,000.00 USD | 5,120.00 USD | 963.90 USD | 1,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.95` | 125.75 USD | 3,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.00` | 4,000,000.00 USD | 4,000,000.00 USD | 4,040.00 USD | 5,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.00` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 3,670.00 USD | 86,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `58.05` | 201,590.00 USD | 204,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.10` | 4,070,000.00 USD | 4,070,000.00 USD | 30,850.00 USD | 29,810.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.10` | 6,120,000.00 USD | 6,120,000.00 USD | 2,810.00 USD | 1,310.00 USD | 848.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.20` | 4,080,000.00 USD | 4,080,000.00 USD | 2,470.00 USD | 6,140.00 USD | 350.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.30` | 4,140,000.00 USD | 4,140,000.00 USD | 10,290.00 USD | 11,540.00 USD | 36,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.30` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 9,580.00 USD | 26,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.40` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 4,720.00 USD | 33,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.40` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 54,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.50` | 4,250,000.00 USD | 4,250,000.00 USD | 49,290.00 USD | 20,280.00 USD | 379.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.50` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.60` | 6,240,000.00 USD | 6,240,000.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.70` | 4,270,000.00 USD | 4,270,000.00 USD | 15,850.00 USD | 7,050.00 USD | 355.85 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.70` | 6,280,000.00 USD | 6,280,000.00 USD | 1,700.00 USD | 5,910.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.80` | 4,350,000.00 USD | 4,350,000.00 USD | 35,430.00 USD | 20,110.00 USD | 23,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.80` | 6,300,000.00 USD | 6,300,000.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.90` | 4,580,000.00 USD | 4,580,000.00 USD | 19,650.00 USD | 116,560.00 USD | 91,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.90` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 48,700.00 USD | 83,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.00` | 4,920,000.00 USD | 4,920,000.00 USD | 152,520.00 USD | 57,050.00 USD | 134,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.00` | 6,870,000.00 USD | 6,870,000.00 USD | 257,280.00 USD | 65,270.00 USD | 118,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.10` | 5,350,000.00 USD | 5,350,000.00 USD | 191,500.00 USD | 51,650.00 USD | 186,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.10` | 7,170,000.00 USD | 7,170,000.00 USD | 91,060.00 USD | 45,400.00 USD | 158,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.20` | 5,690,000.00 USD | 5,690,000.00 USD | 159,440.00 USD | 79,360.00 USD | 96,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.20` | 7,510,000.00 USD | 7,510,000.00 USD | 153,580.00 USD | 12,460.00 USD | 174,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.30` | 6,210,000.00 USD | 6,210,000.00 USD | 306,360.00 USD | 69,590.00 USD | 143,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.30` | 7,780,000.00 USD | 7,780,000.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.35` | 9,440.00 USD | 214,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.40` | 6,420,000.00 USD | 6,420,000.00 USD | 78,860.00 USD | 57,570.00 USD | 76,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.40` | 8,100,000.00 USD | 8,100,000.00 USD | 103,370.00 USD | 73,620.00 USD | 137,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.50` | 6,630,000.00 USD | 6,630,000.00 USD | 119,350.00 USD | 57,840.00 USD | 28,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.50` | 8,250,000.00 USD | 8,250,000.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.60` | 6,770,000.00 USD | 6,770,000.00 USD | 62,780.00 USD | 66,500.00 USD | 18,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.60` | 8,750,000.00 USD | 8,750,000.00 USD | 268,680.00 USD | 145,550.00 USD | 86,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.70` | 6,920,000.00 USD | 6,920,000.00 USD | 20,820.00 USD | 33,740.00 USD | 94,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.70` | 9,150,000.00 USD | 9,150,000.00 USD | 55,510.00 USD | 180,620.00 USD | 161,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.80` | 7,010,000.00 USD | 7,010,000.00 USD | 40,970.00 USD | 36,850.00 USD | 10,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.80` | 9,520,000.00 USD | 9,520,000.00 USD | 118,240.00 USD | 97,600.00 USD | 155,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.90` | 7,230,000.00 USD | 7,230,000.00 USD | 112,870.00 USD | 25,260.00 USD | 80,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.90` | 9,890,000.00 USD | 9,890,000.00 USD | 246,770.00 USD | 84,430.00 USD | 40,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.00` | 7,540,000.00 USD | 7,540,000.00 USD | 182,880.00 USD | 58,590.00 USD | 69,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.00` | 10,400,000.00 USD | 10,400,000.00 USD | 231,370.00 USD | 183,130.00 USD | 94,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.05` | 160.93 USD | 214,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.10` | 7,750,000.00 USD | 7,750,000.00 USD | 95,780.00 USD | 38,060.00 USD | 71,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.10` | 10,970,000.00 USD | 10,970,000.00 USD | 263,890.00 USD | 129,860.00 USD | 174,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.20` | 8,000,000.00 USD | 8,000,000.00 USD | 119,070.00 USD | 39,460.00 USD | 96,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.20` | 11,460,000.00 USD | 11,460,000.00 USD | 207,990.00 USD | 131,530.00 USD | 157,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.30` | 8,220,000.00 USD | 8,220,000.00 USD | 93,620.00 USD | 59,030.00 USD | 68,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.30` | 11,850,000.00 USD | 11,850,000.00 USD | 133,350.00 USD | 95,890.00 USD | 155,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.40` | 8,480,000.00 USD | 8,480,000.00 USD | 158,310.00 USD | 43,400.00 USD | 57,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.40` | 12,300,000.00 USD | 12,300,000.00 USD | 93,890.00 USD | 133,310.00 USD | 226,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.50` | 8,650,000.00 USD | 8,650,000.00 USD | 69,310.00 USD | 44,120.00 USD | 57,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.50` | 12,730,000.00 USD | 12,730,000.00 USD | 131,870.00 USD | 86,290.00 USD | 206,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.60` | 8,760,000.00 USD | 8,760,000.00 USD | 69,650.00 USD | 29,260.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.60` | 13,170,000.00 USD | 13,170,000.00 USD | 251,100.00 USD | 52,650.00 USD | 134,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.70` | 8,840,000.00 USD | 8,840,000.00 USD | 47,740.00 USD | 33,330.00 USD | 1,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.70` | 13,390,000.00 USD | 13,390,000.00 USD | 129,660.00 USD | 67,510.00 USD | 28,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.80` | 8,940,000.00 USD | 8,940,000.00 USD | 24,780.00 USD | 14,010.00 USD | 57,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.80` | 13,620,000.00 USD | 13,620,000.00 USD | 55,810.00 USD | 76,460.00 USD | 94,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.90` | 9,040,000.00 USD | 9,040,000.00 USD | 57,330.00 USD | 26,930.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.90` | 13,860,000.00 USD | 13,860,000.00 USD | 116,730.00 USD | 50,120.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.95` | 397.39 USD | 214,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.00` | 9,120,000.00 USD | 9,120,000.00 USD | 46,000.00 USD | 7,600.00 USD | 28,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 14,000,000.00 USD | 14,000,000.00 USD | 96,160.00 USD | 36,500.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.10` | 9,160,000.00 USD | 9,160,000.00 USD | 13,630.00 USD | 5,800.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 14,040,000.00 USD | 14,040,000.00 USD | 31,540.00 USD | 1,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.15` | 3,870.00 USD | 218,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.20` | 9,280,000.00 USD | 9,280,000.00 USD | 75,930.00 USD | 948.62 USD | 47,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.20` | 14,280,000.00 USD | 14,280,000.00 USD | 116,610.00 USD | 75,410.00 USD | 52,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.30` | 9,300,000.00 USD | 9,300,000.00 USD | 9,540.00 USD | 8,190.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.30` | 14,420,000.00 USD | 14,420,000.00 USD | 51,130.00 USD | 35,650.00 USD | 55,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.40` | 9,310,000.00 USD | 9,310,000.00 USD | 6,350.00 USD | 5,880.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.40` | 14,610,000.00 USD | 14,610,000.00 USD | 89,350.00 USD | 41,800.00 USD | 59,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.50` | 9,340,000.00 USD | 9,340,000.00 USD | 7,070.00 USD | 10,230.00 USD | 10,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.50` | 14,700,000.00 USD | 14,700,000.00 USD | 19,810.00 USD | 35,300.00 USD | 36,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.60` | 9,380,000.00 USD | 9,380,000.00 USD | 18,990.00 USD | 10,510.00 USD | 6,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.60` | 14,950,000.00 USD | 14,950,000.00 USD | 54,240.00 USD | 63,390.00 USD | 132,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.70` | 9,430,000.00 USD | 9,430,000.00 USD | 31,820.00 USD | 10,080.00 USD | 9,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.70` | 15,160,000.00 USD | 15,160,000.00 USD | 84,300.00 USD | 11,330.00 USD | 114,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.80` | 9,450,000.00 USD | 9,450,000.00 USD | 18,210.00 USD | 4,670.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.80` | 15,430,000.00 USD | 15,430,000.00 USD | 160,110.00 USD | 38,970.00 USD | 69,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.90` | 15,570,000.00 USD | 15,570,000.00 USD | 72,380.00 USD | 29,730.00 USD | 35,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.00` | 15,690,000.00 USD | 15,690,000.00 USD | 56,450.00 USD | 12,140.00 USD | 49,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.10` | 15,720,000.00 USD | 15,720,000.00 USD | 14,790.00 USD | 7,860.00 USD | 7,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.20` | 15,830,000.00 USD | 15,830,000.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.30` | 15,990,000.00 USD | 15,990,000.00 USD | 31,770.00 USD | 23,450.00 USD | 97,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.40` | 16,130,000.00 USD | 16,130,000.00 USD | 79,620.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.50` | 16,210,000.00 USD | 16,210,000.00 USD | 44,300.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.60` | 16,280,000.00 USD | 16,280,000.00 USD | 34,910.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.70` | 16,360,000.00 USD | 16,360,000.00 USD | 22,020.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.80` | 16,510,000.00 USD | 16,510,000.00 USD | 72,250.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.90` | 16,600,000.00 USD | 16,600,000.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `62.95` | 138.49 USD | 218,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `63.00` | 16,670,000.00 USD | 16,670,000.00 USD | 34,730.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.10` | 16,700,000.00 USD | 16,700,000.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.30` | 16,740,000.00 USD | 16,740,000.00 USD | 17,050.00 USD | 11,500.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.40` | 16,770,000.00 USD | 16,770,000.00 USD | 13,220.00 USD | 1,320.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `63.45` | 3,350.00 USD | 222,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `63.50` | 16,790,000.00 USD | 16,790,000.00 USD | 6,620.00 USD | 15,810.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.60` | 16,890,000.00 USD | 16,890,000.00 USD | 63,480.00 USD | 20,800.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.70` | 16,970,000.00 USD | 16,970,000.00 USD | 21,940.00 USD | 18,810.00 USD | 35,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.80` | 17,030,000.00 USD | 17,030,000.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.90` | 17,060,000.00 USD | 17,060,000.00 USD | 7,650.00 USD | 12,840.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.00` | 17,100,000.00 USD | 17,100,000.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.10` | 17,130,000.00 USD | 17,130,000.00 USD | 20,350.00 USD | 667.05 USD | 10,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.20` | 17,180,000.00 USD | 17,180,000.00 USD | 28,840.00 USD | 14,530.00 USD | 584.77 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.40` | 17,230,000.00 USD | 17,230,000.00 USD | 2,540.00 USD | 20,590.00 USD | 29,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.50` | 17,260,000.00 USD | 17,260,000.00 USD | 7,700.00 USD | 7,120.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.60` | 17,300,000.00 USD | 17,300,000.00 USD | 32,220.00 USD | 14,180.00 USD | 108.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.70` | 17,370,000.00 USD | 17,370,000.00 USD | 39,430.00 USD | 23,030.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.80` | 17,410,000.00 USD | 17,410,000.00 USD | 7,540.00 USD | 8,210.00 USD | 20,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.90` | 17,450,000.00 USD | 17,450,000.00 USD | 25,320.00 USD | 8,010.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.00` | 17,470,000.00 USD | 17,470,000.00 USD | 1,790.00 USD | 9,480.00 USD | 13,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.10` | 17,530,000.00 USD | 17,530,000.00 USD | 5,810.00 USD | 14,250.00 USD | 37,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.20` | 17,570,000.00 USD | 17,570,000.00 USD | 9,780.00 USD | 1,630.00 USD | 28,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.30` | 17,620,000.00 USD | 17,620,000.00 USD | 22,330.00 USD | 5,510.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `66.15` | 6,750.00 USD | 228,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.95` | 121.18 USD | 229,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.85` | 709.03 USD | 229,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `69.15` | 39,980.00 USD | 269,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `76.35` | 8,380.00 USD | 278,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.75` | 578,460.00 USD | 856,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.85` | 602.56 USD | 857,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.95` | 136.41 USD | 857,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.75` | 646.00 USD | 858,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.05` | 19,000.00 USD | 877,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.15` | 3,250.00 USD | 880,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.55` | 123.96 USD | 880,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.75` | 214.32 USD | 880,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `83.05` | 2,740.00 USD | 883,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `83.15` | 754.17 USD | 884,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `85.25` | 22,750.00 USD | 906,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `90.95` | 966.80 USD | 907,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `93.85` | 105.11 USD | 907,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `94.75` | 125.07 USD | 908,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.25` | 2,480.00 USD | 910,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.25` | 213.71 USD | 910,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.25` | 355,110.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.75` | 1,620.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.85` | 1,860.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.15` | 199.30 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.05` | 6,470.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.55` | 32,570.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `11.35` | 3,050,000.00 USD | 0.00 USD | 363.20 USD | `-79.41%` | `32.00` |
| `Live` | `Long` | `11.45` | 3,050,000.00 USD | 0.00 USD | 366.40 USD | `-79.23%` | `32.00` |
| `Live` | `Long` | `12.25` | 3,050,000.00 USD | 0.00 USD | 122.50 USD | `-77.78%` | `10.00` |
| `Live` | `Long` | `12.75` | 3,050,000.00 USD | 0.00 USD | 2,560.00 USD | `-76.87%` | `200.43` |
| `Live` | `Long` | `13.15` | 3,040,000.00 USD | 0.00 USD | 2,220.00 USD | `-76.15%` | `168.79` |
| `Live` | `Long` | `13.65` | 3,040,000.00 USD | 0.00 USD | 150.15 USD | `-75.24%` | `11.00` |
| `Live` | `Long` | `15.65` | 3,040,000.00 USD | 0.00 USD | 182.48 USD | `-71.61%` | `11.66` |
| `Live` | `Long` | `18.05` | 3,040,000.00 USD | 0.00 USD | 113.72 USD | `-67.26%` | `6.30` |
| `Live` | `Long` | `18.35` | 3,040,000.00 USD | 0.00 USD | 307.18 USD | `-66.71%` | `16.74` |
| `Live` | `Long` | `18.85` | 3,040,000.00 USD | 0.00 USD | 2,260.00 USD | `-65.81%` | `120.00` |
| `Live` | `Long` | `19.05` | 3,040,000.00 USD | 0.00 USD | 3,470.00 USD | `-65.44%` | `182.00` |
| `Live` | `Long` | `19.45` | 3,030,000.00 USD | 0.00 USD | 2,010.00 USD | `-64.72%` | `103.47` |
| `Live` | `Long` | `20.45` | 3,030,000.00 USD | 0.00 USD | 3,080.00 USD | `-62.90%` | `150.57` |
| `Live` | `Long` | `20.95` | 3,030,000.00 USD | 0.00 USD | 19,480.00 USD | `-62.00%` | `930.00` |
| `Live` | `Long` | `22.35` | 3,010,000.00 USD | 0.00 USD | 179.92 USD | `-59.46%` | `8.05` |
| `Live` | `Long` | `22.45` | 3,010,000.00 USD | 0.00 USD | 323.28 USD | `-59.28%` | `14.40` |
| `Live` | `Long` | `23.05` | 3,010,000.00 USD | 0.00 USD | 4,870.00 USD | `-58.19%` | `211.16` |
| `Live` | `Long` | `23.85` | 3,000,000.00 USD | 0.00 USD | 195.57 USD | `-56.74%` | `8.20` |
| `Live` | `Long` | `24.65` | 3,000,000.00 USD | 0.00 USD | 485.36 USD | `-55.28%` | `19.69` |
| `Live` | `Long` | `24.75` | 3,000,000.00 USD | 0.00 USD | 1,490.00 USD | `-55.10%` | `60.00` |
| `Live` | `Long` | `25.05` | 3,000,000.00 USD | 0.00 USD | 561.62 USD | `-54.56%` | `22.42` |
| `Live` | `Long` | `25.25` | 3,000,000.00 USD | 0.00 USD | 277,980.00 USD | `-54.20%` | `11,009.19` |
| `Live` | `Long` | `25.35` | 2,720,000.00 USD | 0.00 USD | 173.39 USD | `-54.01%` | `6.84` |
| `Live` | `Long` | `25.55` | 2,720,000.00 USD | 0.00 USD | 50,740.00 USD | `-53.65%` | `1,985.99` |
| `Live` | `Long` | `25.95` | 2,670,000.00 USD | 0.00 USD | 374.20 USD | `-52.93%` | `14.42` |
| `Live` | `Long` | `27.05` | 2,670,000.00 USD | 0.00 USD | 5,510.00 USD | `-50.93%` | `203.85` |
| `Live` | `Long` | `27.35` | 2,670,000.00 USD | 0.00 USD | 124,900.00 USD | `-50.39%` | `4,566.66` |
| `Live` | `Long` | `27.55` | 2,540,000.00 USD | 0.00 USD | 272.75 USD | `-50.02%` | `9.90` |
| `Live` | `Long` | `27.95` | 2,540,000.00 USD | 0.00 USD | 1,260.00 USD | `-49.30%` | `45.14` |
| `Live` | `Long` | `28.65` | 2,540,000.00 USD | 0.00 USD | 8,600.00 USD | `-48.03%` | `300.00` |
| `Live` | `Long` | `28.95` | 2,530,000.00 USD | 0.00 USD | 8,530.00 USD | `-47.48%` | `294.67` |
| `Live` | `Long` | `29.15` | 2,520,000.00 USD | 0.00 USD | 755.28 USD | `-47.12%` | `25.91` |
| `Live` | `Long` | `29.55` | 2,520,000.00 USD | 0.00 USD | 657.19 USD | `-46.40%` | `22.24` |
| `Live` | `Long` | `29.75` | 2,520,000.00 USD | 0.00 USD | 297,500.00 USD | `-46.03%` | `10,000.00` |
| `Live` | `Long` | `30.05` | 2,220,000.00 USD | 0.00 USD | 218.46 USD | `-45.49%` | `7.27` |
| `Live` | `Long` | `30.35` | 2,220,000.00 USD | 0.00 USD | 569.06 USD | `-44.94%` | `18.75` |
| `Live` | `Long` | `30.95` | 2,220,000.00 USD | 0.00 USD | 538.53 USD | `-43.86%` | `17.40` |
| `Live` | `Long` | `31.15` | 2,220,000.00 USD | 0.00 USD | 5,880.00 USD | `-43.49%` | `188.85` |
| `Live` | `Long` | `31.55` | 2,220,000.00 USD | 0.00 USD | 1,060.00 USD | `-42.77%` | `33.49` |
| `Live` | `Long` | `31.65` | 2,220,000.00 USD | 0.00 USD | 4,920.00 USD | `-42.59%` | `155.55` |
| `Live` | `Long` | `31.85` | 2,210,000.00 USD | 0.00 USD | 2,870.00 USD | `-42.22%` | `90.00` |
| `Live` | `Long` | `31.95` | 2,210,000.00 USD | 0.00 USD | 125.24 USD | `-42.04%` | `3.92` |
| `Live` | `Long` | `32.05` | 2,210,000.00 USD | 0.00 USD | 22,370.00 USD | `-41.86%` | `697.95` |
| `Live` | `Long` | `32.15` | 2,190,000.00 USD | 0.00 USD | 450.10 USD | `-41.68%` | `14.00` |
| `Live` | `Long` | `32.35` | 2,190,000.00 USD | 0.00 USD | 1,070.00 USD | `-41.32%` | `33.03` |
| `Live` | `Long` | `32.65` | 2,180,000.00 USD | 0.00 USD | 653.00 USD | `-40.77%` | `20.00` |
| `Live` | `Long` | `32.75` | 2,180,000.00 USD | 0.00 USD | 953.68 USD | `-40.59%` | `29.12` |
| `Live` | `Long` | `32.85` | 2,180,000.00 USD | 0.00 USD | 35,660.00 USD | `-40.41%` | `1,085.44` |
| `Live` | `Long` | `33.65` | 2,150,000.00 USD | 0.00 USD | 257.76 USD | `-38.96%` | `7.66` |
| `Live` | `Long` | `33.75` | 2,150,000.00 USD | 0.00 USD | 4,190.00 USD | `-38.78%` | `124.01` |
| `Live` | `Long` | `34.05` | 2,140,000.00 USD | 0.00 USD | 182.85 USD | `-38.23%` | `5.37` |
| `Live` | `Long` | `34.15` | 2,140,000.00 USD | 0.00 USD | 6,080.00 USD | `-38.05%` | `177.93` |
| `Live` | `Long` | `34.45` | 2,140,000.00 USD | 0.00 USD | 65,890.00 USD | `-37.51%` | `1,912.61` |
| `Live` | `Long` | `34.65` | 2,070,000.00 USD | 0.00 USD | 3,240.00 USD | `-37.14%` | `93.56` |
| `Live` | `Long` | `34.95` | 2,070,000.00 USD | 0.00 USD | 104.85 USD | `-36.60%` | `3.00` |
| `Live` | `Long` | `35.05` | 2,070,000.00 USD | 0.00 USD | 166.49 USD | `-36.42%` | `4.75` |
| `Live` | `Long` | `35.75` | 2,070,000.00 USD | 0.00 USD | 4,670.00 USD | `-35.15%` | `130.63` |
| `Live` | `Long` | `35.85` | 2,060,000.00 USD | 0.00 USD | 179.25 USD | `-34.97%` | `5.00` |
| `Live` | `Long` | `36.35` | 2,060,000.00 USD | 0.00 USD | 3,020.00 USD | `-34.06%` | `83.03` |
| `Live` | `Long` | `36.45` | 2,060,000.00 USD | 0.00 USD | 423.18 USD | `-33.88%` | `11.61` |
| `Live` | `Long` | `36.75` | 2,060,000.00 USD | 0.00 USD | 101.80 USD | `-33.33%` | `2.77` |
| `Live` | `Long` | `37.15` | 2,060,000.00 USD | 0.00 USD | 438.74 USD | `-32.61%` | `11.81` |
| `Live` | `Long` | `37.35` | 2,060,000.00 USD | 0.00 USD | 9,520.00 USD | `-32.25%` | `254.91` |
| `Live` | `Long` | `37.45` | 2,050,000.00 USD | 0.00 USD | 1,060.00 USD | `-32.06%` | `28.27` |
| `Live` | `Long` | `37.55` | 2,050,000.00 USD | 0.00 USD | 3,530.00 USD | `-31.88%` | `94.04` |
| `Live` | `Long` | `37.75` | 2,040,000.00 USD | 0.00 USD | 377.50 USD | `-31.52%` | `10.00` |
| `Live` | `Long` | `37.85` | 2,040,000.00 USD | 0.00 USD | 6,210.00 USD | `-31.34%` | `164.03` |
| `Live` | `Long` | `37.95` | 2,040,000.00 USD | 0.00 USD | 446.67 USD | `-31.16%` | `11.77` |
| `Live` | `Long` | `38.25` | 2,040,000.00 USD | 0.00 USD | 1,150.00 USD | `-30.61%` | `30.10` |
| `Live` | `Long` | `38.35` | 2,040,000.00 USD | 0.00 USD | 847.54 USD | `-30.43%` | `22.10` |
| `Live` | `Long` | `38.45` | 2,040,000.00 USD | 0.00 USD | 2,400.00 USD | `-30.25%` | `62.34` |
| `Live` | `Long` | `38.55` | 2,030,000.00 USD | 0.00 USD | 993.82 USD | `-30.07%` | `25.78` |
| `Live` | `Long` | `38.65` | 2,030,000.00 USD | 0.00 USD | 4,280.00 USD | `-29.89%` | `110.74` |
| `Live` | `Long` | `38.85` | 2,030,000.00 USD | 0.00 USD | 1,940.00 USD | `-29.53%` | `50.00` |
| `Live` | `Long` | `38.95` | 2,030,000.00 USD | 0.00 USD | 2,730.00 USD | `-29.34%` | `70.00` |
| `Live` | `Long` | `39.05` | 2,020,000.00 USD | 0.00 USD | 664,760.00 USD | `-29.16%` | `17,023.28` |
| `Live` | `Long` | `39.15` | 1,360,000.00 USD | 0.00 USD | 570.02 USD | `-28.98%` | `14.56` |
| `Live` | `Long` | `39.25` | 1,360,000.00 USD | 0.00 USD | 638.99 USD | `-28.80%` | `16.28` |
| `Live` | `Long` | `39.35` | 1,360,000.00 USD | 0.00 USD | 1,290.00 USD | `-28.62%` | `32.73` |
| `Live` | `Long` | `39.45` | 1,360,000.00 USD | 0.00 USD | 716.41 USD | `-28.44%` | `18.16` |
| `Live` | `Long` | `39.55` | 1,360,000.00 USD | 0.00 USD | 312.44 USD | `-28.26%` | `7.90` |
| `Live` | `Long` | `39.65` | 1,350,000.00 USD | 0.00 USD | 5,900.00 USD | `-28.07%` | `148.78` |
| `Live` | `Long` | `39.75` | 1,350,000.00 USD | 0.00 USD | 1,180.00 USD | `-27.89%` | `29.57` |
| `Live` | `Long` | `39.85` | 1,350,000.00 USD | 0.00 USD | 133.10 USD | `-27.71%` | `3.34` |
| `Live` | `Long` | `40.05` | 1,350,000.00 USD | 0.00 USD | 2,160.00 USD | `-27.35%` | `53.97` |
| `Live` | `Long` | `40.45` | 1,350,000.00 USD | 0.00 USD | 1,010.00 USD | `-26.62%` | `24.92` |
| `Live` | `Long` | `40.55` | 1,340,000.00 USD | 0.00 USD | 133.00 USD | `-26.44%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,340,000.00 USD | 0.00 USD | 274.39 USD | `-26.26%` | `6.75` |
| `Live` | `Long` | `40.85` | 1,340,000.00 USD | 0.00 USD | 6,340.00 USD | `-25.90%` | `155.23` |
| `Live` | `Long` | `40.95` | 1,340,000.00 USD | 0.00 USD | 509.01 USD | `-25.72%` | `12.43` |
| `Live` | `Long` | `41.05` | 1,340,000.00 USD | 0.00 USD | 396.54 USD | `-25.53%` | `9.66` |
| `Live` | `Long` | `41.25` | 1,340,000.00 USD | 0.00 USD | 55,740.00 USD | `-25.17%` | `1,351.26` |
| `Live` | `Long` | `41.45` | 1,280,000.00 USD | 0.00 USD | 644.96 USD | `-24.81%` | `15.56` |
| `Live` | `Long` | `42.05` | 1,280,000.00 USD | 0.00 USD | 982.29 USD | `-23.72%` | `23.36` |
| `Live` | `Long` | `42.15` | 1,280,000.00 USD | 0.00 USD | 69,270.00 USD | `-23.54%` | `1,643.33` |
| `Live` | `Long` | `42.25` | 1,210,000.00 USD | 0.00 USD | 44,700.00 USD | `-23.36%` | `1,058.00` |
| `Live` | `Long` | `42.65` | 1,170,000.00 USD | 0.00 USD | 7,190.00 USD | `-22.63%` | `168.64` |
| `Live` | `Long` | `42.85` | 1,160,000.00 USD | 0.00 USD | 5,800.00 USD | `-22.27%` | `135.38` |
| `Live` | `Long` | `42.95` | 1,150,000.00 USD | 0.00 USD | 2,000.00 USD | `-22.09%` | `46.65` |
| `Live` | `Long` | `43.05` | 1,150,000.00 USD | 0.00 USD | 9,080.00 USD | `-21.91%` | `211.00` |
| `Live` | `Long` | `43.15` | 1,140,000.00 USD | 0.00 USD | 122,400.00 USD | `-21.72%` | `2,836.59` |
| `Live` | `Long` | `43.25` | 1,020,000.00 USD | 0.00 USD | 417.80 USD | `-21.54%` | `9.66` |
| `Live` | `Long` | `43.35` | 1,020,000.00 USD | 0.00 USD | 5,390.00 USD | `-21.36%` | `124.24` |
| `Live` | `Long` | `43.45` | 1,010,000.00 USD | 0.00 USD | 980.67 USD | `-21.18%` | `22.57` |
| `Live` | `Long` | `43.65` | 1,010,000.00 USD | 0.00 USD | 426.02 USD | `-20.82%` | `9.76` |
| `Live` | `Long` | `43.75` | 1,010,000.00 USD | 0.00 USD | 21,880.00 USD | `-20.64%` | `500.00` |
| `Live` | `Long` | `43.85` | 989,890.00 USD | 0.00 USD | 801.14 USD | `-20.45%` | `18.27` |
| `Live` | `Long` | `43.95` | 989,090.00 USD | 0.00 USD | 3,980.00 USD | `-20.27%` | `90.60` |
| `Live` | `Long` | `44.15` | 985,110.00 USD | 0.00 USD | 2,380.00 USD | `-19.91%` | `53.99` |
| `Live` | `Long` | `44.35` | 982,720.00 USD | 0.00 USD | 84,440.00 USD | `-19.55%` | `1,903.87` |
| `Live` | `Long` | `44.55` | 898,290.00 USD | 0.00 USD | 842.44 USD | `-19.19%` | `18.91` |
| `Live` | `Long` | `44.65` | 897,450.00 USD | 0.00 USD | 531.34 USD | `-19.00%` | `11.90` |
| `Live` | `Long` | `44.75` | 896,910.00 USD | 0.00 USD | 32,450.00 USD | `-18.82%` | `725.23` |
| `Live` | `Long` | `44.85` | 864,460.00 USD | 0.00 USD | 134.55 USD | `-18.64%` | `3.00` |
| `Live` | `Long` | `44.95` | 864,330.00 USD | 0.00 USD | 2,620.00 USD | `-18.46%` | `58.18` |
| `Live` | `Long` | `45.05` | 861,710.00 USD | 0.00 USD | 4,830.00 USD | `-18.28%` | `107.31` |
| `Live` | `Long` | `45.15` | 856,880.00 USD | 0.00 USD | 8,710.00 USD | `-18.10%` | `193.00` |
| `Live` | `Long` | `45.25` | 848,160.00 USD | 0.00 USD | 3,180.00 USD | `-17.92%` | `70.37` |
| `Live` | `Long` | `45.35` | 844,980.00 USD | 0.00 USD | 4,740.00 USD | `-17.73%` | `104.53` |
| `Live` | `Long` | `45.45` | 840,240.00 USD | 0.00 USD | 23,940.00 USD | `-17.55%` | `526.65` |
| `Live` | `Long` | `45.55` | 816,300.00 USD | 0.00 USD | 13,200.00 USD | `-17.37%` | `289.74` |
| `Live` | `Long` | `45.65` | 803,100.00 USD | 0.00 USD | 42,180.00 USD | `-17.19%` | `924.03` |
| `Live` | `Long` | `45.85` | 760,920.00 USD | 0.00 USD | 326.91 USD | `-16.83%` | `7.13` |
| `Live` | `Long` | `45.95` | 760,600.00 USD | 0.00 USD | 4,320.00 USD | `-16.65%` | `94.09` |
| `Live` | `Long` | `46.05` | 756,270.00 USD | 0.00 USD | 706.41 USD | `-16.46%` | `15.34` |
| `Live` | `Long` | `46.15` | 755,570.00 USD | 0.00 USD | 5,940.00 USD | `-16.28%` | `128.71` |
| `Live` | `Long` | `46.25` | 749,630.00 USD | 0.00 USD | 842.21 USD | `-16.10%` | `18.21` |
| `Live` | `Long` | `46.35` | 748,780.00 USD | 0.00 USD | 383.78 USD | `-15.92%` | `8.28` |
| `Live` | `Long` | `46.55` | 748,400.00 USD | 0.00 USD | 24,670.00 USD | `-15.56%` | `529.90` |
| `Live` | `Long` | `46.65` | 723,730.00 USD | 0.00 USD | 4,330.00 USD | `-15.38%` | `92.91` |
| `Live` | `Long` | `46.85` | 719,400.00 USD | 0.00 USD | 358.40 USD | `-15.01%` | `7.65` |
| `Live` | `Long` | `46.95` | 719,040.00 USD | 0.00 USD | 158.22 USD | `-14.83%` | `3.37` |
| `Live` | `Long` | `47.15` | 718,880.00 USD | 0.00 USD | 1,980.00 USD | `-14.47%` | `42.07` |
| `Live` | `Long` | `47.25` | 716,900.00 USD | 0.00 USD | 2,320.00 USD | `-14.29%` | `49.07` |
| `Live` | `Long` | `47.35` | 714,580.00 USD | 0.00 USD | 43,340.00 USD | `-14.11%` | `915.41` |
| `Live` | `Long` | `47.45` | 671,230.00 USD | 0.00 USD | 2,180.00 USD | `-13.92%` | `45.94` |
| `Live` | `Long` | `47.55` | 669,050.00 USD | 0.00 USD | 4,450.00 USD | `-13.74%` | `93.69` |
| `Live` | `Long` | `47.75` | 664,600.00 USD | 0.00 USD | 47,750.00 USD | `-13.38%` | `1,000.00` |
| `Live` | `Long` | `47.85` | 616,850.00 USD | 0.00 USD | 3,800.00 USD | `-13.20%` | `79.49` |
| `Live` | `Long` | `48.05` | 613,050.00 USD | 0.00 USD | 1,340.00 USD | `-12.84%` | `27.93` |
| `Live` | `Long` | `48.15` | 611,700.00 USD | 0.00 USD | 1,690.00 USD | `-12.65%` | `35.03` |
| `Live` | `Long` | `48.25` | 610,020.00 USD | 0.00 USD | 525.44 USD | `-12.47%` | `10.89` |
| `Live` | `Long` | `48.45` | 609,490.00 USD | 0.00 USD | 279.07 USD | `-12.11%` | `5.76` |
| `Live` | `Long` | `48.55` | 609,210.00 USD | 0.00 USD | 2,560.00 USD | `-11.93%` | `52.70` |
| `Live` | `Long` | `48.65` | 606,650.00 USD | 0.00 USD | 273.90 USD | `-11.75%` | `5.63` |
| `Live` | `Long` | `48.75` | 606,380.00 USD | 0.00 USD | 333.94 USD | `-11.57%` | `6.85` |
| `Live` | `Long` | `48.95` | 606,050.00 USD | 0.00 USD | 252.58 USD | `-11.20%` | `5.16` |
| `Live` | `Long` | `49.05` | 605,790.00 USD | 0.00 USD | 1,580.00 USD | `-11.02%` | `32.25` |
| `Live` | `Long` | `49.15` | 604,210.00 USD | 0.00 USD | 15,740.00 USD | `-10.84%` | `320.20` |
| `Live` | `Long` | `49.35` | 588,470.00 USD | 0.00 USD | 5,230.00 USD | `-10.48%` | `105.97` |
| `Live` | `Long` | `49.45` | 583,240.00 USD | 0.00 USD | 419.34 USD | `-10.30%` | `8.48` |
| `Live` | `Long` | `49.55` | 582,830.00 USD | 0.00 USD | 37,080.00 USD | `-10.12%` | `748.26` |
| `Live` | `Long` | `49.65` | 545,750.00 USD | 0.00 USD | 73,260.00 USD | `-9.93%` | `1,475.52` |
| `Live` | `Long` | `49.75` | 472,490.00 USD | 0.00 USD | 1,770.00 USD | `-9.75%` | `35.51` |
| `Live` | `Long` | `49.95` | 470,720.00 USD | 0.00 USD | 19,920.00 USD | `-9.39%` | `398.70` |
| `Live` | `Long` | `50.05` | 450,810.00 USD | 0.00 USD | 1,820.00 USD | `-9.21%` | `36.43` |
| `Live` | `Long` | `50.25` | 448,980.00 USD | 0.00 USD | 102.51 USD | `-8.85%` | `2.04` |
| `Live` | `Long` | `50.35` | 448,880.00 USD | 0.00 USD | 1,140.00 USD | `-8.66%` | `22.67` |
| `Live` | `Long` | `50.45` | 447,740.00 USD | 0.00 USD | 4,720.00 USD | `-8.48%` | `93.64` |
| `Live` | `Long` | `50.55` | 443,020.00 USD | 0.00 USD | 84,100.00 USD | `-8.30%` | `1,663.61` |
| `Live` | `Long` | `50.75` | 358,920.00 USD | 0.00 USD | 9,050.00 USD | `-7.94%` | `178.28` |
| `Live` | `Long` | `50.95` | 349,870.00 USD | 0.00 USD | 431.55 USD | `-7.58%` | `8.47` |
| `Live` | `Long` | `51.15` | 349,440.00 USD | 0.00 USD | 219,370.00 USD | `-7.21%` | `4,288.79` |
| `Live` | `Long` | `51.25` | 130,070.00 USD | 0.00 USD | 202.44 USD | `-7.03%` | `3.95` |
| `Live` | `Long` | `51.35` | 129,870.00 USD | 0.00 USD | 453.93 USD | `-6.85%` | `8.84` |
| `Live` | `Long` | `51.45` | 129,410.00 USD | 0.00 USD | 27,210.00 USD | `-6.67%` | `528.81` |
| `Live` | `Long` | `51.55` | 102,210.00 USD | 0.00 USD | 551.07 USD | `-6.49%` | `10.69` |
| `Live` | `Long` | `51.65` | 101,660.00 USD | 0.00 USD | 9,100.00 USD | `-6.31%` | `176.09` |
| `Live` | `Long` | `51.75` | 92,560.00 USD | 0.00 USD | 6,480.00 USD | `-6.12%` | `125.17` |
| `Live` | `Long` | `51.85` | 86,080.00 USD | 0.00 USD | 13,890.00 USD | `-5.94%` | `267.97` |
| `Live` | `Long` | `51.95` | 72,190.00 USD | 0.00 USD | 13,950.00 USD | `-5.76%` | `268.48` |
| `Live` | `Long` | `52.15` | 58,240.00 USD | 0.00 USD | 3,350.00 USD | `-5.40%` | `64.18` |
| `Live` | `Long` | `52.25` | 54,890.00 USD | 0.00 USD | 4,930.00 USD | `-5.22%` | `94.33` |
| `Live` | `Long` | `52.35` | 49,970.00 USD | 0.00 USD | 3,010.00 USD | `-5.04%` | `57.56` |
| `Live` | `Long` | `52.45` | 46,950.00 USD | 0.00 USD | 2,220.00 USD | `-4.85%` | `42.26` |
| `Live` | `Long` | `52.55` | 44,740.00 USD | 0.00 USD | 8,700.00 USD | `-4.67%` | `165.49` |
| `Live` | `Long` | `52.75` | 36,040.00 USD | 0.00 USD | 4,240.00 USD | `-4.31%` | `80.44` |
| `Live` | `Long` | `52.85` | 31,800.00 USD | 0.00 USD | 5,950.00 USD | `-4.13%` | `112.64` |
| `Live` | `Long` | `52.95` | 25,840.00 USD | 0.00 USD | 25,840.00 USD | `-3.95%` | `488.06` |
| `Live` | `Short` | `55.85` | 741.13 USD | 741.13 USD | 0.00 USD | `+1.31%` | `13.27` |
| `Live` | `Short` | `56.05` | 3,150.00 USD | 2,410.00 USD | 0.00 USD | `+1.68%` | `43.06` |
| `Live` | `Short` | `57.95` | 3,280.00 USD | 125.75 USD | 0.00 USD | `+5.12%` | `2.17` |
| `Live` | `Short` | `58.05` | 204,870.00 USD | 201,590.00 USD | 0.00 USD | `+5.30%` | `3,472.67` |
| `Live` | `Short` | `59.35` | 214,310.00 USD | 9,440.00 USD | 0.00 USD | `+7.66%` | `159.09` |
| `Live` | `Short` | `60.05` | 214,470.00 USD | 160.93 USD | 0.00 USD | `+8.93%` | `2.68` |
| `Live` | `Short` | `60.95` | 214,870.00 USD | 397.39 USD | 0.00 USD | `+10.56%` | `6.52` |
| `Live` | `Short` | `61.15` | 218,740.00 USD | 3,870.00 USD | 0.00 USD | `+10.93%` | `63.26` |
| `Live` | `Short` | `62.95` | 218,880.00 USD | 138.49 USD | 0.00 USD | `+14.19%` | `2.20` |
| `Live` | `Short` | `63.45` | 222,230.00 USD | 3,350.00 USD | 0.00 USD | `+15.10%` | `52.83` |
| `Live` | `Short` | `66.15` | 228,980.00 USD | 6,750.00 USD | 0.00 USD | `+20.00%` | `102.07` |
| `Live` | `Short` | `66.95` | 229,100.00 USD | 121.18 USD | 0.00 USD | `+21.45%` | `1.81` |
| `Live` | `Short` | `67.85` | 229,810.00 USD | 709.03 USD | 0.00 USD | `+23.08%` | `10.45` |
| `Live` | `Short` | `69.15` | 269,790.00 USD | 39,980.00 USD | 0.00 USD | `+25.44%` | `578.10` |
| `Live` | `Short` | `76.35` | 278,170.00 USD | 8,380.00 USD | 0.00 USD | `+38.50%` | `109.80` |
| `Live` | `Short` | `77.75` | 856,630.00 USD | 578,460.00 USD | 0.00 USD | `+41.04%` | `7,440.05` |
| `Live` | `Short` | `77.85` | 857,240.00 USD | 602.56 USD | 0.00 USD | `+41.22%` | `7.74` |
| `Live` | `Short` | `77.95` | 857,370.00 USD | 136.41 USD | 0.00 USD | `+41.40%` | `1.75` |
| `Live` | `Short` | `80.75` | 858,020.00 USD | 646.00 USD | 0.00 USD | `+46.48%` | `8.00` |
| `Live` | `Short` | `81.05` | 877,020.00 USD | 19,000.00 USD | 0.00 USD | `+47.03%` | `234.42` |
| `Live` | `Short` | `81.15` | 880,260.00 USD | 3,250.00 USD | 0.00 USD | `+47.21%` | `40.00` |
| `Live` | `Short` | `81.55` | 880,390.00 USD | 123.96 USD | 0.00 USD | `+47.93%` | `1.52` |
| `Live` | `Short` | `82.75` | 880,600.00 USD | 214.32 USD | 0.00 USD | `+50.11%` | `2.59` |
| `Live` | `Short` | `83.05` | 883,340.00 USD | 2,740.00 USD | 0.00 USD | `+50.65%` | `33.00` |
| `Live` | `Short` | `83.15` | 884,100.00 USD | 754.17 USD | 0.00 USD | `+50.84%` | `9.07` |
| `Live` | `Short` | `85.25` | 906,840.00 USD | 22,750.00 USD | 0.00 USD | `+54.65%` | `266.81` |
| `Live` | `Short` | `90.95` | 907,810.00 USD | 966.80 USD | 0.00 USD | `+64.99%` | `10.63` |
| `Live` | `Short` | `93.85` | 907,910.00 USD | 105.11 USD | 0.00 USD | `+70.25%` | `1.12` |
| `Live` | `Short` | `94.75` | 908,040.00 USD | 125.07 USD | 0.00 USD | `+71.88%` | `1.32` |
| `Live` | `Short` | `99.25` | 910,520.00 USD | 2,480.00 USD | 0.00 USD | `+80.04%` | `25.00` |
| `Live` | `Short` | `104.25` | 910,730.00 USD | 213.71 USD | 0.00 USD | `+89.11%` | `2.05` |
| `Live` | `Short` | `105.25` | 1,270,000.00 USD | 355,110.00 USD | 0.00 USD | `+90.93%` | `3,374.01` |
| `Live` | `Short` | `106.75` | 1,270,000.00 USD | 1,620.00 USD | 0.00 USD | `+93.65%` | `15.16` |
| `Live` | `Short` | `106.85` | 1,270,000.00 USD | 1,860.00 USD | 0.00 USD | `+93.83%` | `17.43` |
| `Live` | `Short` | `107.15` | 1,270,000.00 USD | 199.30 USD | 0.00 USD | `+94.37%` | `1.86` |
| `Live` | `Short` | `108.05` | 1,280,000.00 USD | 6,470.00 USD | 0.00 USD | `+96.01%` | `59.91` |
| `Live` | `Short` | `108.55` | 1,310,000.00 USD | 32,570.00 USD | 0.00 USD | `+96.91%` | `300.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 806,720.00 USD | 0.00 USD | 392.18 USD | `-63.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 806,330.00 USD | 0.00 USD | 2,310.00 USD | `-60.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 804,020.00 USD | 0.00 USD | 806.86 USD | `-54.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 803,220.00 USD | 0.00 USD | 1,560.00 USD | `-54.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 801,660.00 USD | 0.00 USD | 410.25 USD | `-50.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 801,250.00 USD | 0.00 USD | 281.57 USD | `-45.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 800,970.00 USD | 0.00 USD | 36,050.00 USD | `-34.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 764,920.00 USD | 0.00 USD | 37,550.00 USD | `-31.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 727,370.00 USD | 0.00 USD | 447.01 USD | `-31.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.35` | 726,920.00 USD | 0.00 USD | 73,350.00 USD | `-30.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 653,570.00 USD | 0.00 USD | 40,560.00 USD | `-29.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 613,010.00 USD | 0.00 USD | 489.57 USD | `-28.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 612,520.00 USD | 0.00 USD | 1,180.00 USD | `-27.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 611,340.00 USD | 0.00 USD | 9,840.00 USD | `-27.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 601,510.00 USD | 0.00 USD | 2,060.00 USD | `-25.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.05` | 599,450.00 USD | 0.00 USD | 2,060.00 USD | `-25.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 597,390.00 USD | 0.00 USD | 2,960.00 USD | `-24.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 594,430.00 USD | 0.00 USD | 4,010.00 USD | `-23.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.65` | 590,420.00 USD | 0.00 USD | 3,000.00 USD | `-22.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 587,420.00 USD | 0.00 USD | 5,680.00 USD | `-21.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 581,740.00 USD | 0.00 USD | 672.22 USD | `-20.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.35` | 581,060.00 USD | 0.00 USD | 329,970.00 USD | `-19.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 251,100.00 USD | 0.00 USD | 213.80 USD | `-19.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 250,880.00 USD | 0.00 USD | 223.20 USD | `-19.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 250,660.00 USD | 0.00 USD | 391.13 USD | `-19.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 250,270.00 USD | 0.00 USD | 7,080.00 USD | `-18.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 243,190.00 USD | 0.00 USD | 1,370.00 USD | `-17.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 241,830.00 USD | 0.00 USD | 553.80 USD | `-16.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.35` | 241,270.00 USD | 0.00 USD | 2,970.00 USD | `-15.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.45` | 238,300.00 USD | 0.00 USD | 3,080.00 USD | `-15.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 235,230.00 USD | 0.00 USD | 14,000.00 USD | `-15.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 221,230.00 USD | 0.00 USD | 158.56 USD | `-14.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 221,070.00 USD | 0.00 USD | 373.28 USD | `-14.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 220,700.00 USD | 0.00 USD | 849.46 USD | `-14.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 219,850.00 USD | 0.00 USD | 1,150.00 USD | `-13.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 218,700.00 USD | 0.00 USD | 129.25 USD | `-12.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.15` | 218,570.00 USD | 0.00 USD | 303.35 USD | `-12.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 218,270.00 USD | 0.00 USD | 1,740.00 USD | `-11.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 216,530.00 USD | 0.00 USD | 981.00 USD | `-11.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.35` | 215,540.00 USD | 0.00 USD | 817.24 USD | `-10.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 214,730.00 USD | 0.00 USD | 237.85 USD | `-10.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.55` | 214,490.00 USD | 0.00 USD | 1,420.00 USD | `-10.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.85` | 213,070.00 USD | 0.00 USD | 108.17 USD | `-9.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 212,960.00 USD | 0.00 USD | 298.20 USD | `-9.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 212,670.00 USD | 0.00 USD | 34,670.00 USD | `-9.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 177,990.00 USD | 0.00 USD | 6,410.00 USD | `-9.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 171,580.00 USD | 0.00 USD | 459.70 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 171,120.00 USD | 0.00 USD | 236.57 USD | `-8.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 170,880.00 USD | 0.00 USD | 1,020.00 USD | `-7.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 169,860.00 USD | 0.00 USD | 439.89 USD | `-7.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.45` | 169,420.00 USD | 0.00 USD | 204.26 USD | `-6.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 169,220.00 USD | 0.00 USD | 10,190.00 USD | `-6.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.85` | 159,030.00 USD | 0.00 USD | 106.29 USD | `-5.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.95` | 158,920.00 USD | 0.00 USD | 8,700.00 USD | `-5.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 150,220.00 USD | 0.00 USD | 26,490.00 USD | `-5.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.25` | 123,730.00 USD | 0.00 USD | 140.03 USD | `-5.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 123,590.00 USD | 0.00 USD | 70,190.00 USD | `-4.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 53,400.00 USD | 0.00 USD | 5,460.00 USD | `-4.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 47,940.00 USD | 0.00 USD | 271.13 USD | `-4.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.85` | 47,670.00 USD | 0.00 USD | 2,840.00 USD | `-4.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 44,830.00 USD | 0.00 USD | 115.43 USD | `-3.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 44,710.00 USD | 0.00 USD | 9,240.00 USD | `-3.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 35,470.00 USD | 0.00 USD | 2,660.00 USD | `-3.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.25` | 32,810.00 USD | 0.00 USD | 881.82 USD | `-3.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 31,930.00 USD | 0.00 USD | 566.57 USD | `-3.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 31,360.00 USD | 0.00 USD | 5,950.00 USD | `-2.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 25,420.00 USD | 0.00 USD | 1,370.00 USD | `-2.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.75` | 24,050.00 USD | 0.00 USD | 1,120.00 USD | `-2.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 22,920.00 USD | 0.00 USD | 462.03 USD | `-2.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 22,460.00 USD | 0.00 USD | 895.07 USD | `-1.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.15` | 21,570.00 USD | 0.00 USD | 398.54 USD | `-1.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 21,170.00 USD | 0.00 USD | 3,090.00 USD | `-1.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 18,080.00 USD | 0.00 USD | 156.53 USD | `-1.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.45` | 17,920.00 USD | 0.00 USD | 144.29 USD | `-1.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.55` | 17,780.00 USD | 0.00 USD | 1,690.00 USD | `-1.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.65` | 16,090.00 USD | 0.00 USD | 14,930.00 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.75` | 1,160.00 USD | 0.00 USD | 198.74 USD | `-0.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 956.80 USD | 0.00 USD | 398.21 USD | `-0.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.95` | 558.58 USD | 0.00 USD | 397.84 USD | `-0.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 160.75 USD | 0.00 USD | 160.75 USD | `-0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.15` | 398.18 USD | 398.18 USD | 0.00 USD | `+0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.25` | 797.09 USD | 398.90 USD | 0.00 USD | `+0.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.35` | 1,200.00 USD | 407.38 USD | 0.00 USD | `+0.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.45` | 1,610.00 USD | 408.11 USD | 0.00 USD | `+0.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.55` | 1,770.00 USD | 156.65 USD | 0.00 USD | `+0.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.65` | 5,380.00 USD | 3,610.00 USD | 0.00 USD | `+0.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.75` | 5,580.00 USD | 202.37 USD | 0.00 USD | `+1.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.85` | 5,730.00 USD | 149.68 USD | 0.00 USD | `+1.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.95` | 5,930.00 USD | 193.03 USD | 0.00 USD | `+1.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.05` | 6,560.00 USD | 632.24 USD | 0.00 USD | `+1.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.15` | 6,970.00 USD | 407.65 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.25` | 7,170.00 USD | 204.19 USD | 0.00 USD | `+2.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.35` | 7,560.00 USD | 387.12 USD | 0.00 USD | `+2.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.45` | 7,960.00 USD | 407.57 USD | 0.00 USD | `+2.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.55` | 10,600.00 USD | 2,640.00 USD | 0.00 USD | `+2.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.65` | 10,720.00 USD | 121.23 USD | 0.00 USD | `+2.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.75` | 10,950.00 USD | 228.70 USD | 0.00 USD | `+2.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.85` | 28,980.00 USD | 18,030.00 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.95` | 29,370.00 USD | 390.68 USD | 0.00 USD | `+3.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.15` | 29,760.00 USD | 392.05 USD | 0.00 USD | `+3.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.25` | 29,970.00 USD | 201.52 USD | 0.00 USD | `+3.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.35` | 30,170.00 USD | 207.03 USD | 0.00 USD | `+4.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.45` | 30,520.00 USD | 344.70 USD | 0.00 USD | `+4.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.55` | 50,880.00 USD | 20,360.00 USD | 0.00 USD | `+4.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.65` | 50,990.00 USD | 118.18 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.75` | 51,110.00 USD | 119.54 USD | 0.00 USD | `+4.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.95` | 51,240.00 USD | 128.65 USD | 0.00 USD | `+5.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 51,990.00 USD | 747.68 USD | 0.00 USD | `+5.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 52,190.00 USD | 200.04 USD | 0.00 USD | `+5.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 52,390.00 USD | 200.96 USD | 0.00 USD | `+5.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 52,510.00 USD | 123.70 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 53,120.00 USD | 601.45 USD | 0.00 USD | `+6.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 53,730.00 USD | 611.85 USD | 0.00 USD | `+6.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.65` | 54,000.00 USD | 274.48 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 54,490.00 USD | 491.15 USD | 0.00 USD | `+6.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 57,440.00 USD | 2,940.00 USD | 0.00 USD | `+6.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 57,570.00 USD | 129.69 USD | 0.00 USD | `+6.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 62,360.00 USD | 4,800.00 USD | 0.00 USD | `+7.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 63,640.00 USD | 1,280.00 USD | 0.00 USD | `+7.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.25` | 63,860.00 USD | 210.34 USD | 0.00 USD | `+7.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 64,320.00 USD | 461.74 USD | 0.00 USD | `+7.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 64,480.00 USD | 159.92 USD | 0.00 USD | `+7.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.55` | 64,970.00 USD | 496.65 USD | 0.00 USD | `+8.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 65,700.00 USD | 724.75 USD | 0.00 USD | `+8.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.75` | 65,810.00 USD | 113.53 USD | 0.00 USD | `+8.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 65,970.00 USD | 158.00 USD | 0.00 USD | `+8.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 66,140.00 USD | 171.14 USD | 0.00 USD | `+8.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 66,690.00 USD | 551.00 USD | 0.00 USD | `+9.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.45` | 66,850.00 USD | 155.36 USD | 0.00 USD | `+9.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 67,730.00 USD | 878.58 USD | 0.00 USD | `+9.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 69,110.00 USD | 1,390.00 USD | 0.00 USD | `+10.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 70,100.00 USD | 986.99 USD | 0.00 USD | `+10.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 70,770.00 USD | 674.72 USD | 0.00 USD | `+10.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 73,140.00 USD | 2,360.00 USD | 0.00 USD | `+10.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 73,260.00 USD | 125.56 USD | 0.00 USD | `+11.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 76,860.00 USD | 3,600.00 USD | 0.00 USD | `+11.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 77,500.00 USD | 643.20 USD | 0.00 USD | `+11.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.95` | 79,620.00 USD | 2,120.00 USD | 0.00 USD | `+12.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 79,750.00 USD | 130.31 USD | 0.00 USD | `+12.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 80,470.00 USD | 716.72 USD | 0.00 USD | `+13.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 80,700.00 USD | 231.39 USD | 0.00 USD | `+14.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 81,330.00 USD | 630.87 USD | 0.00 USD | `+14.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 82,030.00 USD | 703.97 USD | 0.00 USD | `+14.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.35` | 82,170.00 USD | 140.64 USD | 0.00 USD | `+14.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 82,840.00 USD | 668.13 USD | 0.00 USD | `+15.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 91,570.00 USD | 8,730.00 USD | 0.00 USD | `+15.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 92,130.00 USD | 555.03 USD | 0.00 USD | `+15.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 92,660.00 USD | 531.62 USD | 0.00 USD | `+16.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.35` | 93,320.00 USD | 664.09 USD | 0.00 USD | `+16.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.45` | 93,990.00 USD | 665.12 USD | 0.00 USD | `+16.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 94,190.00 USD | 202.69 USD | 0.00 USD | `+17.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 94,490.00 USD | 298.04 USD | 0.00 USD | `+17.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 94,590.00 USD | 102.13 USD | 0.00 USD | `+18.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 95,130.00 USD | 540.09 USD | 0.00 USD | `+18.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 95,230.00 USD | 100.79 USD | 0.00 USD | `+18.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 95,500.00 USD | 262.20 USD | 0.00 USD | `+18.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 95,870.00 USD | 371.49 USD | 0.00 USD | `+19.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 96,560.00 USD | 696.17 USD | 0.00 USD | `+19.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 97,100.00 USD | 534.00 USD | 0.00 USD | `+21.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 108,180.00 USD | 11,080.00 USD | 0.00 USD | `+21.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 114,880.00 USD | 6,710.00 USD | 0.00 USD | `+21.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.05` | 117,240.00 USD | 2,360.00 USD | 0.00 USD | `+23.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 122,110.00 USD | 4,860.00 USD | 0.00 USD | `+23.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 122,310.00 USD | 204.48 USD | 0.00 USD | `+26.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.65` | 640,510.00 USD | 518,200.00 USD | 0.00 USD | `+26.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 641,320.00 USD | 810.02 USD | 0.00 USD | `+26.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 964,780.00 USD | 323,460.00 USD | 0.00 USD | `+27.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 964,950.00 USD | 170.04 USD | 0.00 USD | `+28.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 970,710.00 USD | 5,770.00 USD | 0.00 USD | `+28.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 970,980.00 USD | 269.28 USD | 0.00 USD | `+28.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 971,270.00 USD | 291.40 USD | 0.00 USD | `+30.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 978,490.00 USD | 7,220.00 USD | 0.00 USD | `+30.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 978,650.00 USD | 156.78 USD | 0.00 USD | `+31.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 981,870.00 USD | 3,220.00 USD | 0.00 USD | `+31.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 982,280.00 USD | 411.14 USD | 0.00 USD | `+33.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 1,110,000.00 USD | 123,190.00 USD | 0.00 USD | `+34.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 1,110,000.00 USD | 1,020.00 USD | 0.00 USD | `+35.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.75` | 1,110,000.00 USD | 811.04 USD | 0.00 USD | `+35.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 1,110,000.00 USD | 104.93 USD | 0.00 USD | `+35.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 1,110,000.00 USD | 133.59 USD | 0.00 USD | `+36.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 1,110,000.00 USD | 402.59 USD | 0.00 USD | `+36.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.85` | 1,110,000.00 USD | 308.71 USD | 0.00 USD | `+37.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 1,110,000.00 USD | 315.18 USD | 0.00 USD | `+40.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 1,170,000.00 USD | 59,310.00 USD | 0.00 USD | `+42.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 1,170,000.00 USD | 3,160.00 USD | 0.00 USD | `+43.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.35` | 1,180,000.00 USD | 5,260.00 USD | 0.00 USD | `+43.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 1,180,000.00 USD | 5,690.00 USD | 0.00 USD | `+44.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 1,220,000.00 USD | 36,590.00 USD | 0.00 USD | `+45.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 1,220,000.00 USD | 433.89 USD | 0.00 USD | `+46.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 1,220,000.00 USD | 172.64 USD | 0.00 USD | `+47.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 1,220,000.00 USD | 164.10 USD | 0.00 USD | `+48.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 1,220,000.00 USD | 546.81 USD | 0.00 USD | `+50.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 1,220,000.00 USD | 2,300.00 USD | 0.00 USD | `+52.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 1,230,000.00 USD | 12,070.00 USD | 0.00 USD | `+54.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.05` | 1,250,000.00 USD | 20,230.00 USD | 0.00 USD | `+57.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 1,260,000.00 USD | 1,580.00 USD | 0.00 USD | `+59.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 1,290,000.00 USD | 37,000.00 USD | 0.00 USD | `+59.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 1,290,000.00 USD | 473.21 USD | 0.00 USD | `+61.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 1,290,000.00 USD | 422.99 USD | 0.00 USD | `+61.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 1,300,000.00 USD | 1,630.00 USD | 0.00 USD | `+62.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 1,300,000.00 USD | 4,870.00 USD | 0.00 USD | `+63.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 1,300,000.00 USD | 481.55 USD | 0.00 USD | `+66.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 1,300,000.00 USD | 1,330.00 USD | 0.00 USD | `+66.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 1,300,000.00 USD | 188.10 USD | 0.00 USD | `+70.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,570,000.00 USD | 266,140.00 USD | 0.00 USD | `+72.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,570,000.00 USD | 3,400.00 USD | 0.00 USD | `+72.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,590,000.00 USD | 21,930.00 USD | 0.00 USD | `+74.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,590,000.00 USD | 294.15 USD | 0.00 USD | `+77.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 1,610,000.00 USD | 15,380.00 USD | 0.00 USD | `+79.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,610,000.00 USD | 3,660.00 USD | 0.00 USD | `+81.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,610,000.00 USD | 306.15 USD | 0.00 USD | `+85.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,610,000.00 USD | 936.72 USD | 0.00 USD | `+86.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,620,000.00 USD | 2,920.00 USD | 0.00 USD | `+87.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,620,000.00 USD | 324.15 USD | 0.00 USD | `+96.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 1,620,000.00 USD | 123.23 USD | 0.00 USD | `+97.82%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `49.30` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 13,300.00 USD | 4,090.00 USD | 367.32 USD |
| `7D` | `49.30` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 15,190.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `49.40` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 626.48 USD |
| `7D` | `49.40` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD |
| `1D` | `49.50` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 1,180.00 USD | 4,200.00 USD | 13,790.00 USD |
| `7D` | `49.50` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 1,130.00 USD | 6,290.00 USD | 0.00 USD |
| `1D` | `49.60` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 980.75 USD | 4,350.00 USD | 0.00 USD |
| `7D` | `49.60` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD |
| `1D` | `49.70` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 3,550.00 USD | 1,980.00 USD | 416.86 USD |
| `7D` | `49.70` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 788.92 USD | 0.00 USD | 4,900.00 USD |
| `1D` | `49.80` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 2,920.00 USD | 388.95 USD | 14,210.00 USD |
| `7D` | `49.80` | 8,040,000.00 USD | 0.00 USD | 8,040,000.00 USD | 8,590.00 USD | 8,220.00 USD | 0.00 USD |
| `1D` | `49.90` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 17,280.00 USD | 8,370.00 USD | 22,850.00 USD |
| `7D` | `49.90` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 45,030.00 USD | 7,170.00 USD | 4,700.00 USD |
| `1D` | `50.00` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 7,520.00 USD | 6,290.00 USD | 40,300.00 USD |
| `7D` | `50.00` | 7,970,000.00 USD | 0.00 USD | 7,970,000.00 USD | 22,100.00 USD | 7,630.00 USD | 24,550.00 USD |
| `1D` | `50.10` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD |
| `7D` | `50.10` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 363.50 USD | 682.90 USD | 0.00 USD |
| `7D` | `50.20` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 6,960.00 USD | 500.40 USD | 34,680.00 USD |
| `7D` | `50.30` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 16,270.00 USD | 3,640.00 USD | 1,950.00 USD |
| `1D` | `50.40` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 349.63 USD | 2,000.00 USD | 0.00 USD |
| `7D` | `50.40` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 23,520.00 USD | 19,110.00 USD | 33,450.00 USD |
| `7D` | `50.50` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 24,840.00 USD | 6,790.00 USD | 43,710.00 USD |
| `7D` | `50.60` | 7,700,000.00 USD | 0.00 USD | 7,700,000.00 USD | 52,670.00 USD | 17,830.00 USD | 22,250.00 USD |
| `7D` | `50.70` | 7,610,000.00 USD | 0.00 USD | 7,610,000.00 USD | 53,670.00 USD | 24,710.00 USD | 32,520.00 USD |
| `1D` | `50.80` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 5,630.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `50.80` | 7,500,000.00 USD | 0.00 USD | 7,500,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD |
| `1D` | `50.90` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 0.00 USD | 497.60 USD | 8,390.00 USD |
| `7D` | `50.90` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD |
| `1D` | `51.00` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 129.78 USD |
| `7D` | `51.00` | 7,150,000.00 USD | 0.00 USD | 7,150,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `51.10` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 263.90 USD | 1,060.00 USD | 0.00 USD |
| `7D` | `51.10` | 7,020,000.00 USD | 0.00 USD | 7,020,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD |
| `1D` | `51.20` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 1,100.00 USD | 1,130.00 USD | 327.72 USD |
| `7D` | `51.20` | 6,940,000.00 USD | 0.00 USD | 6,940,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD |
| `1D` | `51.30` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 20,430.00 USD | 5,180.00 USD | 18,640.00 USD |
| `7D` | `51.30` | 6,870,000.00 USD | 0.00 USD | 6,870,000.00 USD | 19,510.00 USD | 12,490.00 USD | 47,090.00 USD |
| `1D` | `51.40` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 17,800.00 USD | 7,000.00 USD | 10,780.00 USD |
| `7D` | `51.40` | 6,800,000.00 USD | 0.00 USD | 6,800,000.00 USD | 73,130.00 USD | 28,960.00 USD | 45,150.00 USD |
| `1D` | `51.50` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 11,810.00 USD | 9,610.00 USD | 4,080.00 USD |
| `7D` | `51.50` | 6,650,000.00 USD | 0.00 USD | 6,650,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `51.60` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 9,850.00 USD | 8,110.00 USD | 4,820.00 USD |
| `7D` | `51.60` | 6,560,000.00 USD | 0.00 USD | 6,560,000.00 USD | 35,880.00 USD | 12,240.00 USD | 17,650.00 USD |
| `1D` | `51.70` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 5,340.00 USD | 3,950.00 USD | 6,480.00 USD |
| `7D` | `51.70` | 6,490,000.00 USD | 0.00 USD | 6,490,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `51.80` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 13,220.00 USD | 2,980.00 USD | 10,050.00 USD |
| `7D` | `51.80` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD |
| `1D` | `51.90` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 12,520.00 USD | 19,700.00 USD | 9,190.00 USD |
| `7D` | `51.90` | 6,400,000.00 USD | 0.00 USD | 6,400,000.00 USD | 5,870.00 USD | 15,810.00 USD | 4,760.00 USD |
| `1D` | `52.00` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 25,510.00 USD | 8,240.00 USD | 23,340.00 USD |
| `7D` | `52.00` | 6,370,000.00 USD | 0.00 USD | 6,370,000.00 USD | 64,300.00 USD | 20,800.00 USD | 11,880.00 USD |
| `1D` | `52.10` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 27,630.00 USD | 6,280.00 USD | 35,220.00 USD |
| `7D` | `52.10` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 24,220.00 USD | 18,810.00 USD | 35,480.00 USD |
| `1D` | `52.20` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 20,520.00 USD | 11,250.00 USD | 14,390.00 USD |
| `7D` | `52.20` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 38,380.00 USD | 4,340.00 USD | 25,270.00 USD |
| `1D` | `52.30` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 39,260.00 USD | 7,260.00 USD | 16,110.00 USD |
| `7D` | `52.30` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 21,450.00 USD | 12,840.00 USD | 8,940.00 USD |
| `1D` | `52.40` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 11,920.00 USD | 7,830.00 USD | 6,280.00 USD |
| `7D` | `52.40` | 6,080,000.00 USD | 0.00 USD | 6,080,000.00 USD | 20,580.00 USD | 11,230.00 USD | 20,050.00 USD |
| `1D` | `52.50` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 49,720.00 USD | 13,570.00 USD | 998.32 USD |
| `7D` | `52.50` | 6,030,000.00 USD | 0.00 USD | 6,030,000.00 USD | 36,050.00 USD | 667.05 USD | 11,240.00 USD |
| `1D` | `52.60` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 5,230.00 USD | 9,230.00 USD | 506.16 USD |
| `7D` | `52.60` | 5,980,000.00 USD | 0.00 USD | 5,980,000.00 USD | 74,610.00 USD | 14,530.00 USD | 584.77 USD |
| `1D` | `52.70` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 13,770.00 USD | 8,280.00 USD | 15,080.00 USD |
| `7D` | `52.70` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 20,250.00 USD | 43,820.00 USD | 62,360.00 USD |
| `1D` | `52.80` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 14,400.00 USD | 16,180.00 USD | 74,160.00 USD |
| `7D` | `52.80` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 46,600.00 USD | 29,900.00 USD | 108.50 USD |
| `1D` | `52.90` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 40,590.00 USD | 10,870.00 USD | 6,120.00 USD |
| `7D` | `52.90` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 51,920.00 USD | 26,170.00 USD | 34,400.00 USD |
| `1D` | `53.00` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 9,470.00 USD | 10,940.00 USD | 4,190.00 USD |
| `7D` | `53.00` | 5,580,000.00 USD | 0.00 USD | 5,580,000.00 USD | 18,990.00 USD | 10,540.00 USD | 55,850.00 USD |
| `1D` | `53.10` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 27,870.00 USD | 10,120.00 USD | 60,680.00 USD |
| `7D` | `53.10` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 52,760.00 USD | 37,960.00 USD | 9,860.00 USD |
| `1D` | `53.20` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 68,380.00 USD | 25,970.00 USD | 63,770.00 USD |
| `7D` | `53.20` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 162,460.00 USD | 42,920.00 USD | 27,410.00 USD |
| `1D` | `53.30` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 32,910.00 USD | 26,340.00 USD | 41,770.00 USD |
| `7D` | `53.30` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 63,050.00 USD | 18,150.00 USD | 37,140.00 USD |
| `1D` | `53.40` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 14,390.00 USD | 16,470.00 USD | 75,840.00 USD |
| `7D` | `53.40` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 48,160.00 USD | 18,090.00 USD | 95,920.00 USD |
| `1D` | `53.50` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 14,780.00 USD | 11,880.00 USD | 7,160.00 USD |
| `7D` | `53.50` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 49,490.00 USD | 8,960.00 USD | 17,890.00 USD |
| `1D` | `53.60` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 74,660.00 USD | 19,660.00 USD | 1,840.00 USD |
| `7D` | `53.60` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 53,580.00 USD | 5,690.00 USD | 98,500.00 USD |
| `1D` | `53.70` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 5,710.00 USD | 7,700.00 USD | 465.28 USD |
| `7D` | `53.70` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 131,400.00 USD | 14,420.00 USD | 10,200.00 USD |
| `1D` | `53.80` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 16,800.00 USD | 5,280.00 USD | 3,130.00 USD |
| `7D` | `53.80` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 99,150.00 USD | 80,510.00 USD | 126,140.00 USD |
| `1D` | `53.90` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 7,480.00 USD | 26,500.00 USD | 125,910.00 USD |
| `7D` | `53.90` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 111,970.00 USD | 56,750.00 USD | 123,850.00 USD |
| `1D` | `54.00` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 28,730.00 USD | 21,740.00 USD | 0.00 USD |
| `7D` | `54.00` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 344,710.00 USD | 148,420.00 USD | 271,500.00 USD |
| `1D` | `54.10` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 34,220.00 USD | 18,680.00 USD | 6,500.00 USD |
| `7D` | `54.10` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 234,120.00 USD | 48,800.00 USD | 184,480.00 USD |
| `1D` | `54.20` | 993,930.00 USD | 0.00 USD | 993,930.00 USD | 64,160.00 USD | 16,200.00 USD | 120,010.00 USD |
| `7D` | `54.20` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 234,980.00 USD | 158,770.00 USD | 128,910.00 USD |
| `1D` | `54.30` | 793,560.00 USD | 0.00 USD | 793,560.00 USD | 127,400.00 USD | 44,430.00 USD | 148,670.00 USD |
| `7D` | `54.30` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 381,380.00 USD | 140,500.00 USD | 185,160.00 USD |
| `1D` | `54.40` | 473,060.00 USD | 0.00 USD | 473,060.00 USD | 52,750.00 USD | 45,620.00 USD | 78,270.00 USD |
| `7D` | `54.40` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 304,270.00 USD | 13,830.00 USD | 92,140.00 USD |
| `1D` | `54.50` | 296,420.00 USD | 0.00 USD | 296,420.00 USD | 9,670.00 USD | 26,440.00 USD | 144,050.00 USD |
| `7D` | `54.50` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 159,720.00 USD | 36,920.00 USD | 237,000.00 USD |
| `1D` | `54.60` | 116,240.00 USD | 0.00 USD | 116,240.00 USD | 18,470.00 USD | 16,730.00 USD | 14,320.00 USD |
| `7D` | `54.60` | 584,340.00 USD | 0.00 USD | 584,340.00 USD | 0.00 USD | 1,930.00 USD | 72,400.00 USD |
| `1D` | `54.70` | 66,720.00 USD | 0.00 USD | 66,720.00 USD | 0.00 USD | 0.00 USD | 57,100.00 USD |
| `7D` | `54.70` | 510,010.00 USD | 0.00 USD | 510,010.00 USD | 0.00 USD | 0.00 USD | 173,390.00 USD |
| `1D` | `54.80` | 9,610.00 USD | 0.00 USD | 9,610.00 USD | 0.00 USD | 9,420.00 USD | 0.00 USD |
| `1D` | `55.10` | 189.61 USD | 0.00 USD | 189.61 USD | 0.00 USD | 0.00 USD | 189.61 USD |
| `7D` | `55.20` | 336,630.00 USD | 0.00 USD | 336,630.00 USD | 336,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `55.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.60` | 426,340.00 USD | 426,340.00 USD | 0.00 USD | 426,340.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `55.70` | 407.86 USD | 407.86 USD | 0.00 USD | 0.00 USD | 0.00 USD | 407.86 USD |
| `7D` | `55.70` | 632,770.00 USD | 632,770.00 USD | 0.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD |
| `1D` | `55.80` | 64,490.00 USD | 64,490.00 USD | 0.00 USD | 0.00 USD | 17,410.00 USD | 46,680.00 USD |
| `7D` | `55.80` | 723,740.00 USD | 723,740.00 USD | 0.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD |
| `1D` | `55.90` | 344,790.00 USD | 344,790.00 USD | 0.00 USD | 137,200.00 USD | 2,990.00 USD | 140,110.00 USD |
| `7D` | `55.90` | 930,900.00 USD | 930,900.00 USD | 0.00 USD | 141,330.00 USD | 65,840.00 USD | 0.00 USD |
| `1D` | `56.00` | 544,060.00 USD | 544,060.00 USD | 0.00 USD | 139,840.00 USD | 0.00 USD | 59,430.00 USD |
| `7D` | `56.00` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 181,230.00 USD | 98,600.00 USD | 147,270.00 USD |
| `1D` | `56.10` | 851,070.00 USD | 851,070.00 USD | 0.00 USD | 105,950.00 USD | 26,500.00 USD | 174,550.00 USD |
| `7D` | `56.10` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 121,920.00 USD | 144,120.00 USD | 61,210.00 USD |
| `1D` | `56.20` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 96,820.00 USD | 86,290.00 USD | 71,790.00 USD |
| `7D` | `56.20` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 104,510.00 USD | 72,410.00 USD | 240,740.00 USD |
| `1D` | `56.30` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 10,860.00 USD | 55,630.00 USD | 43,380.00 USD |
| `7D` | `56.30` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 91,850.00 USD | 132,300.00 USD | 131,790.00 USD |
| `1D` | `56.40` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 49,190.00 USD | 51,430.00 USD | 237,370.00 USD |
| `7D` | `56.40` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 215,940.00 USD | 119,990.00 USD | 137,070.00 USD |
| `1D` | `56.50` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 117,430.00 USD | 164,400.00 USD | 120,030.00 USD |
| `7D` | `56.50` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 170,750.00 USD | 134,140.00 USD | 3,750.00 USD |
| `1D` | `56.60` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 49,560.00 USD | 105,330.00 USD | 77,950.00 USD |
| `7D` | `56.60` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 363,190.00 USD | 126,950.00 USD | 0.00 USD |
| `1D` | `56.70` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 201,670.00 USD | 26,440.00 USD | 338,410.00 USD |
| `7D` | `56.70` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 110,940.00 USD | 121,500.00 USD | 96,070.00 USD |
| `1D` | `56.80` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 191,190.00 USD | 18,260.00 USD | 115,100.00 USD |
| `7D` | `56.80` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 153,580.00 USD | 92,780.00 USD | 261,330.00 USD |
| `1D` | `56.90` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 33,240.00 USD | 8,700.00 USD | 1,780.00 USD |
| `7D` | `56.90` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 108,440.00 USD | 48,600.00 USD | 266,610.00 USD |
| `1D` | `57.00` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 10,920.00 USD | 659.87 USD |
| `7D` | `57.00` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 88,680.00 USD | 2,620.00 USD | 93,100.00 USD |
| `1D` | `57.10` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 7,480.00 USD | 10,560.00 USD | 5,950.00 USD |
| `7D` | `57.10` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 36,580.00 USD | 16,110.00 USD | 20,440.00 USD |
| `1D` | `57.20` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 13,250.00 USD | 63,210.00 USD |
| `7D` | `57.20` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 21,160.00 USD | 15,720.00 USD | 3,700.00 USD |
| `1D` | `57.30` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 12,360.00 USD | 10,870.00 USD | 386.57 USD |
| `7D` | `57.30` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 22,360.00 USD | 3,150.00 USD | 34,250.00 USD |
| `1D` | `57.40` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 24,850.00 USD | 35,100.00 USD | 3,250.00 USD |
| `7D` | `57.40` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 38,520.00 USD | 31,660.00 USD | 153,130.00 USD |
| `1D` | `57.50` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 133,260.00 USD | 20,440.00 USD | 96,450.00 USD |
| `7D` | `57.50` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 76,670.00 USD | 31,830.00 USD | 0.00 USD |
| `1D` | `57.60` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 58,710.00 USD | 22,220.00 USD | 60,010.00 USD |
| `7D` | `57.60` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 144,800.00 USD | 40,430.00 USD | 28,320.00 USD |
| `1D` | `57.70` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 35,650.00 USD | 26,090.00 USD | 96,250.00 USD |
| `7D` | `57.70` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 0.00 USD | 5,400.00 USD | 57,330.00 USD |
| `1D` | `57.80` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 5,680.00 USD | 13,220.00 USD | 72,680.00 USD |
| `7D` | `57.80` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 2,260.00 USD | 14,360.00 USD | 48,030.00 USD |
| `1D` | `57.90` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 9,940.00 USD | 14,110.00 USD | 7,160.00 USD |
| `7D` | `57.90` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 5,120.00 USD | 963.90 USD | 1,510.00 USD |
| `1D` | `58.00` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 4,040.00 USD | 5,650.00 USD | 0.00 USD |
| `7D` | `58.00` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 3,670.00 USD | 86,690.00 USD |
| `1D` | `58.10` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 30,850.00 USD | 29,810.00 USD | 9,350.00 USD |
| `7D` | `58.10` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 2,810.00 USD | 1,310.00 USD | 848.40 USD |
| `1D` | `58.20` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 2,470.00 USD | 6,140.00 USD | 350.42 USD |
| `1D` | `58.30` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 10,290.00 USD | 11,540.00 USD | 36,830.00 USD |
| `7D` | `58.30` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 0.00 USD | 9,580.00 USD | 26,820.00 USD |
| `1D` | `58.40` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 4,720.00 USD | 33,950.00 USD |
| `7D` | `58.40` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 54,120.00 USD |
| `1D` | `58.50` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 49,290.00 USD | 20,280.00 USD | 379.22 USD |
| `7D` | `58.50` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD |
| `7D` | `58.60` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `58.70` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 15,850.00 USD | 7,050.00 USD | 355.85 USD |
| `7D` | `58.70` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 1,700.00 USD | 5,910.00 USD | 35,320.00 USD |
| `1D` | `58.80` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 35,430.00 USD | 20,110.00 USD | 23,630.00 USD |
| `7D` | `58.80` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD |
| `1D` | `58.90` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 19,650.00 USD | 116,560.00 USD | 91,310.00 USD |
| `7D` | `58.90` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 0.00 USD | 48,700.00 USD | 83,500.00 USD |
| `1D` | `59.00` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 152,520.00 USD | 57,050.00 USD | 134,010.00 USD |
| `7D` | `59.00` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 257,280.00 USD | 65,270.00 USD | 118,570.00 USD |
| `1D` | `59.10` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 191,500.00 USD | 51,650.00 USD | 186,370.00 USD |
| `7D` | `59.10` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 91,060.00 USD | 45,400.00 USD | 158,780.00 USD |
| `1D` | `59.20` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 159,440.00 USD | 79,360.00 USD | 96,020.00 USD |
| `7D` | `59.20` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 153,580.00 USD | 12,460.00 USD | 174,600.00 USD |
| `1D` | `59.30` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 306,360.00 USD | 69,590.00 USD | 143,250.00 USD |
| `7D` | `59.30` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD |
| `1D` | `59.40` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 78,860.00 USD | 57,570.00 USD | 76,960.00 USD |
| `7D` | `59.40` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 103,370.00 USD | 73,620.00 USD | 137,500.00 USD |
| `1D` | `59.50` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 119,350.00 USD | 57,840.00 USD | 28,370.00 USD |
| `7D` | `59.50` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD |
| `1D` | `59.60` | 6,770,000.00 USD | 6,770,000.00 USD | 0.00 USD | 62,780.00 USD | 66,500.00 USD | 18,340.00 USD |
| `7D` | `59.60` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 268,680.00 USD | 145,550.00 USD | 86,840.00 USD |
| `1D` | `59.70` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 20,820.00 USD | 33,740.00 USD | 94,130.00 USD |
| `7D` | `59.70` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 55,510.00 USD | 180,620.00 USD | 161,880.00 USD |
| `1D` | `59.80` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 40,970.00 USD | 36,850.00 USD | 10,870.00 USD |
| `7D` | `59.80` | 9,520,000.00 USD | 9,520,000.00 USD | 0.00 USD | 118,240.00 USD | 97,600.00 USD | 155,270.00 USD |
| `1D` | `59.90` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 112,870.00 USD | 25,260.00 USD | 80,370.00 USD |
| `7D` | `59.90` | 9,890,000.00 USD | 9,890,000.00 USD | 0.00 USD | 246,770.00 USD | 84,430.00 USD | 40,130.00 USD |
| `1D` | `60.00` | 7,540,000.00 USD | 7,540,000.00 USD | 0.00 USD | 182,880.00 USD | 58,590.00 USD | 69,570.00 USD |
| `7D` | `60.00` | 10,400,000.00 USD | 10,400,000.00 USD | 0.00 USD | 231,370.00 USD | 183,130.00 USD | 94,160.00 USD |
| `1D` | `60.10` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 95,780.00 USD | 38,060.00 USD | 71,530.00 USD |
| `7D` | `60.10` | 10,970,000.00 USD | 10,970,000.00 USD | 0.00 USD | 263,890.00 USD | 129,860.00 USD | 174,140.00 USD |
| `1D` | `60.20` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 119,070.00 USD | 39,460.00 USD | 96,900.00 USD |
| `7D` | `60.20` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 207,990.00 USD | 131,530.00 USD | 157,150.00 USD |
| `1D` | `60.30` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 93,620.00 USD | 59,030.00 USD | 68,160.00 USD |
| `7D` | `60.30` | 11,850,000.00 USD | 11,850,000.00 USD | 0.00 USD | 133,350.00 USD | 95,890.00 USD | 155,610.00 USD |
| `1D` | `60.40` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 158,310.00 USD | 43,400.00 USD | 57,550.00 USD |
| `7D` | `60.40` | 12,300,000.00 USD | 12,300,000.00 USD | 0.00 USD | 93,890.00 USD | 133,310.00 USD | 226,940.00 USD |
| `1D` | `60.50` | 8,650,000.00 USD | 8,650,000.00 USD | 0.00 USD | 69,310.00 USD | 44,120.00 USD | 57,940.00 USD |
| `7D` | `60.50` | 12,730,000.00 USD | 12,730,000.00 USD | 0.00 USD | 131,870.00 USD | 86,290.00 USD | 206,240.00 USD |
| `1D` | `60.60` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 69,650.00 USD | 29,260.00 USD | 5,340.00 USD |
| `7D` | `60.60` | 13,170,000.00 USD | 13,170,000.00 USD | 0.00 USD | 251,100.00 USD | 52,650.00 USD | 134,260.00 USD |
| `1D` | `60.70` | 8,840,000.00 USD | 8,840,000.00 USD | 0.00 USD | 47,740.00 USD | 33,330.00 USD | 1,100.00 USD |
| `7D` | `60.70` | 13,390,000.00 USD | 13,390,000.00 USD | 0.00 USD | 129,660.00 USD | 67,510.00 USD | 28,830.00 USD |
| `1D` | `60.80` | 8,940,000.00 USD | 8,940,000.00 USD | 0.00 USD | 24,780.00 USD | 14,010.00 USD | 57,540.00 USD |
| `7D` | `60.80` | 13,620,000.00 USD | 13,620,000.00 USD | 0.00 USD | 55,810.00 USD | 76,460.00 USD | 94,420.00 USD |
| `1D` | `60.90` | 9,040,000.00 USD | 9,040,000.00 USD | 0.00 USD | 57,330.00 USD | 26,930.00 USD | 22,850.00 USD |
| `7D` | `60.90` | 13,860,000.00 USD | 13,860,000.00 USD | 0.00 USD | 116,730.00 USD | 50,120.00 USD | 79,720.00 USD |
| `1D` | `61.00` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 46,000.00 USD | 7,600.00 USD | 28,080.00 USD |
| `7D` | `61.00` | 14,000,000.00 USD | 14,000,000.00 USD | 0.00 USD | 96,160.00 USD | 36,500.00 USD | 5,370.00 USD |
| `1D` | `61.10` | 9,160,000.00 USD | 9,160,000.00 USD | 0.00 USD | 13,630.00 USD | 5,800.00 USD | 11,490.00 USD |
| `7D` | `61.10` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 31,540.00 USD | 1,560.00 USD | 0.00 USD |
| `1D` | `61.20` | 9,280,000.00 USD | 9,280,000.00 USD | 0.00 USD | 75,930.00 USD | 948.62 USD | 47,920.00 USD |
| `7D` | `61.20` | 14,280,000.00 USD | 14,280,000.00 USD | 0.00 USD | 116,610.00 USD | 75,410.00 USD | 52,570.00 USD |
| `1D` | `61.30` | 9,300,000.00 USD | 9,300,000.00 USD | 0.00 USD | 9,540.00 USD | 8,190.00 USD | 2,340.00 USD |
| `7D` | `61.30` | 14,420,000.00 USD | 14,420,000.00 USD | 0.00 USD | 51,130.00 USD | 35,650.00 USD | 55,130.00 USD |
| `1D` | `61.40` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 6,350.00 USD | 5,880.00 USD | 1,670.00 USD |
| `7D` | `61.40` | 14,610,000.00 USD | 14,610,000.00 USD | 0.00 USD | 89,350.00 USD | 41,800.00 USD | 59,330.00 USD |
| `1D` | `61.50` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 7,070.00 USD | 10,230.00 USD | 10,310.00 USD |
| `7D` | `61.50` | 14,700,000.00 USD | 14,700,000.00 USD | 0.00 USD | 19,810.00 USD | 35,300.00 USD | 36,110.00 USD |
| `1D` | `61.60` | 9,380,000.00 USD | 9,380,000.00 USD | 0.00 USD | 18,990.00 USD | 10,510.00 USD | 6,980.00 USD |
| `7D` | `61.60` | 14,950,000.00 USD | 14,950,000.00 USD | 0.00 USD | 54,240.00 USD | 63,390.00 USD | 132,550.00 USD |
| `1D` | `61.70` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 31,820.00 USD | 10,080.00 USD | 9,600.00 USD |
| `7D` | `61.70` | 15,160,000.00 USD | 15,160,000.00 USD | 0.00 USD | 84,300.00 USD | 11,330.00 USD | 114,420.00 USD |
| `1D` | `61.80` | 9,450,000.00 USD | 9,450,000.00 USD | 0.00 USD | 18,210.00 USD | 4,670.00 USD | 1,570.00 USD |
| `7D` | `61.80` | 15,430,000.00 USD | 15,430,000.00 USD | 0.00 USD | 160,110.00 USD | 38,970.00 USD | 69,850.00 USD |
| `7D` | `61.90` | 15,570,000.00 USD | 15,570,000.00 USD | 0.00 USD | 72,380.00 USD | 29,730.00 USD | 35,780.00 USD |
| `7D` | `62.00` | 15,690,000.00 USD | 15,690,000.00 USD | 0.00 USD | 56,450.00 USD | 12,140.00 USD | 49,710.00 USD |
| `7D` | `62.10` | 15,720,000.00 USD | 15,720,000.00 USD | 0.00 USD | 14,790.00 USD | 7,860.00 USD | 7,220.00 USD |
| `7D` | `62.20` | 15,830,000.00 USD | 15,830,000.00 USD | 0.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD |
| `7D` | `62.30` | 15,990,000.00 USD | 15,990,000.00 USD | 0.00 USD | 31,770.00 USD | 23,450.00 USD | 97,450.00 USD |
| `7D` | `62.40` | 16,130,000.00 USD | 16,130,000.00 USD | 0.00 USD | 79,620.00 USD | 27,560.00 USD | 30,890.00 USD |
| `7D` | `62.50` | 16,210,000.00 USD | 16,210,000.00 USD | 0.00 USD | 44,300.00 USD | 14,320.00 USD | 26,610.00 USD |
| `7D` | `62.60` | 16,280,000.00 USD | 16,280,000.00 USD | 0.00 USD | 34,910.00 USD | 7,830.00 USD | 27,730.00 USD |
| `7D` | `62.70` | 16,360,000.00 USD | 16,360,000.00 USD | 0.00 USD | 22,020.00 USD | 12,490.00 USD | 47,090.00 USD |
| `7D` | `62.80` | 16,510,000.00 USD | 16,510,000.00 USD | 0.00 USD | 72,250.00 USD | 28,960.00 USD | 45,150.00 USD |
| `7D` | `62.90` | 16,600,000.00 USD | 16,600,000.00 USD | 0.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD |
| `7D` | `63.00` | 16,670,000.00 USD | 16,670,000.00 USD | 0.00 USD | 34,730.00 USD | 12,240.00 USD | 17,650.00 USD |
| `7D` | `63.10` | 16,700,000.00 USD | 16,700,000.00 USD | 0.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD |
| `7D` | `63.30` | 16,740,000.00 USD | 16,740,000.00 USD | 0.00 USD | 17,050.00 USD | 11,500.00 USD | 9,730.00 USD |
| `7D` | `63.40` | 16,770,000.00 USD | 16,770,000.00 USD | 0.00 USD | 13,220.00 USD | 1,320.00 USD | 9,960.00 USD |
| `7D` | `63.50` | 16,790,000.00 USD | 16,790,000.00 USD | 0.00 USD | 6,620.00 USD | 15,810.00 USD | 4,760.00 USD |
| `7D` | `63.60` | 16,890,000.00 USD | 16,890,000.00 USD | 0.00 USD | 63,480.00 USD | 20,800.00 USD | 11,880.00 USD |
| `7D` | `63.70` | 16,970,000.00 USD | 16,970,000.00 USD | 0.00 USD | 21,940.00 USD | 18,810.00 USD | 35,480.00 USD |
| `7D` | `63.80` | 17,030,000.00 USD | 17,030,000.00 USD | 0.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD |
| `7D` | `63.90` | 17,060,000.00 USD | 17,060,000.00 USD | 0.00 USD | 7,650.00 USD | 12,840.00 USD | 8,940.00 USD |
| `7D` | `64.00` | 17,100,000.00 USD | 17,100,000.00 USD | 0.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD |
| `7D` | `64.10` | 17,130,000.00 USD | 17,130,000.00 USD | 0.00 USD | 20,350.00 USD | 667.05 USD | 10,640.00 USD |
| `7D` | `64.20` | 17,180,000.00 USD | 17,180,000.00 USD | 0.00 USD | 28,840.00 USD | 14,530.00 USD | 584.77 USD |
| `7D` | `64.40` | 17,230,000.00 USD | 17,230,000.00 USD | 0.00 USD | 2,540.00 USD | 20,590.00 USD | 29,110.00 USD |
| `7D` | `64.50` | 17,260,000.00 USD | 17,260,000.00 USD | 0.00 USD | 7,700.00 USD | 7,120.00 USD | 13,310.00 USD |
| `7D` | `64.60` | 17,300,000.00 USD | 17,300,000.00 USD | 0.00 USD | 32,220.00 USD | 14,180.00 USD | 108.50 USD |
| `7D` | `64.70` | 17,370,000.00 USD | 17,370,000.00 USD | 0.00 USD | 39,430.00 USD | 23,030.00 USD | 3,870.00 USD |
| `7D` | `64.80` | 17,410,000.00 USD | 17,410,000.00 USD | 0.00 USD | 7,540.00 USD | 8,210.00 USD | 20,430.00 USD |
| `7D` | `64.90` | 17,450,000.00 USD | 17,450,000.00 USD | 0.00 USD | 25,320.00 USD | 8,010.00 USD | 9,860.00 USD |
| `7D` | `65.00` | 17,470,000.00 USD | 17,470,000.00 USD | 0.00 USD | 1,790.00 USD | 9,480.00 USD | 13,480.00 USD |
| `7D` | `65.10` | 17,530,000.00 USD | 17,530,000.00 USD | 0.00 USD | 5,810.00 USD | 14,250.00 USD | 37,140.00 USD |
| `7D` | `65.20` | 17,570,000.00 USD | 17,570,000.00 USD | 0.00 USD | 9,780.00 USD | 1,630.00 USD | 28,280.00 USD |
| `7D` | `65.30` | 17,620,000.00 USD | 17,620,000.00 USD | 0.00 USD | 22,330.00 USD | 5,510.00 USD | 17,890.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `416.16M` | Total OI Tokens: `7,519,070.8 LTC`
  * 1h OI Change: `+1.81%` | 4h OI Change: `-0.54%` | 24h OI Change: `-8.15%`
  * Exchange Breakdown: Binance=`73.17M` | Bybit=`65.95M` | OKX=`33.97M` | Hyperliquid=`22.16M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `11.38K` | Last 24h: `31.76K` | Last 3d: `59.78K` | Last 7d: `115.16K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0076%` | **USDT OKX** | `0.0014%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0017%` |
| **USDT MEXC** | `0.0075%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0068%` | **USDT Bitget** | `0.0047%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `44.12%` | `55.88%` | `0.79` | 2,380,000.00 USD |
| `15M` | `Binance` | `34.54%` | `65.46%` | `0.53` | 1,000,000.00 USD |
| `15M` | `OKX` | `57.33%` | `42.67%` | `1.34` | 195,550.00 USD |
| `15M` | `Bybit` | `49.96%` | `50.04%` | `1.00` | 111,000.00 USD |
| `15M` | `KuCoin` | `51.97%` | `48.03%` | `1.08` | 145,950.00 USD |
| `15M` | `Gate` | `44.5%` | `55.5%` | `0.80` | 145,900.00 USD |
| `15M` | `Bitget` | `44.79%` | `55.21%` | `0.81` | 161,390.00 USD |
| `15M` | `BingX` | `50.97%` | `49.03%` | `1.04` | 124,920.00 USD |
| `15M` | `MEXC` | `41.9%` | `58.1%` | `0.72` | 34,420.00 USD |
| `15M` | `Bitunix` | `42.33%` | `57.67%` | `0.73` | 52,880.00 USD |
| `15M` | `Hyperliquid` | `83.91%` | `16.09%` | `5.22` | 22,240.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.17%` | `49.83%` | `1.01` | 359,490.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `99.23%` | `0.77%` | `128.87` | 26,130.00 USD |
| `15M` | `HTX` | `32.95%` | `67.05%` | `0.49` | 802.60 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `3.23%` | `96.77%` | `0.03` | 2,870.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `34.54%` | `65.46%` | `0.53` | 1,000,000.00 USD |
| `15M` | `Global Accounts` | `44.12%` | `55.88%` | `0.79` | 2,380,000.00 USD |
| `1H` | `LTC` | `49.05%` | `50.95%` | `0.96` | 15,620,000.00 USD |
| `1H` | `Binance` | `45.41%` | `54.59%` | `0.83` | 5,020,000.00 USD |
| `1H` | `OKX` | `49.14%` | `50.86%` | `0.97` | 1,510,000.00 USD |
| `1H` | `Bybit` | `52.11%` | `47.89%` | `1.09` | 1,110,000.00 USD |
| `1H` | `KuCoin` | `55.23%` | `44.77%` | `1.23` | 71,560.00 USD |
| `1H` | `Gate` | `50.94%` | `49.06%` | `1.04` | 966,330.00 USD |
| `1H` | `Bitget` | `62.08%` | `37.92%` | `1.64` | 775,240.00 USD |
| `1H` | `BingX` | `37.05%` | `62.95%` | `0.59` | 3,150,000.00 USD |
| `1H` | `MEXC` | `60.45%` | `39.55%` | `1.53` | 1,420,000.00 USD |
| `1H` | `Bitunix` | `50.67%` | `49.33%` | `1.03` | 460,910.00 USD |
| `1H` | `Hyperliquid` | `72.47%` | `27.53%` | `2.63` | 234,860.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.05%` | `48.95%` | `1.04` | 501,820.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `99.65%` | `0.35%` | `284.71` | 313,810.00 USD |
| `1H` | `HTX` | `36.52%` | `63.48%` | `0.58` | 29,650.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `19.37%` | `80.63%` | `0.24` | 2,310.00 USD |
| `1H` | `Aster` | `76.22%` | `23.78%` | `3.21` | 41,090.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `72.06%` | `27.94%` | `2.58` | 6,690.00 USD |
| `1H` | `Whale Positions` | `45.41%` | `54.59%` | `0.83` | 5,020,000.00 USD |
| `1H` | `Global Accounts` | `49.05%` | `50.95%` | `0.96` | 15,620,000.00 USD |
| `4H` | `LTC` | `48.77%` | `51.23%` | `0.95` | 95,980,000.00 USD |
| `4H` | `Binance` | `46.24%` | `53.76%` | `0.86` | 33,430,000.00 USD |
| `4H` | `OKX` | `48.56%` | `51.44%` | `0.94` | 12,370,000.00 USD |
| `4H` | `Bybit` | `51.58%` | `48.42%` | `1.07` | 10,820,000.00 USD |
| `4H` | `KuCoin` | `39.79%` | `60.21%` | `0.66` | 1,130,000.00 USD |
| `4H` | `Gate` | `46.47%` | `53.53%` | `0.87` | 5,790,000.00 USD |
| `4H` | `Bitget` | `52.14%` | `47.86%` | `1.09` | 3,030,000.00 USD |
| `4H` | `BingX` | `45.16%` | `54.84%` | `0.82` | 10,160,000.00 USD |
| `4H` | `MEXC` | `42.61%` | `57.39%` | `0.74` | 4,760,000.00 USD |
| `4H` | `Bitunix` | `49.79%` | `50.21%` | `0.99` | 2,430,000.00 USD |
| `4H` | `Hyperliquid` | `43.74%` | `56.26%` | `0.78` | 2,860,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.28%` | `49.72%` | `1.01` | 2,770,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `79.24%` | `20.76%` | `3.82` | 5,010,000.00 USD |
| `4H` | `HTX` | `55.07%` | `44.93%` | `1.23` | 235,400.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `33.27%` | `66.73%` | `0.50` | 672,810.00 USD |
| `4H` | `Aster` | `60.63%` | `39.37%` | `1.54` | 368,510.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `21.08%` | `78.92%` | `0.27` | 152,090.00 USD |
| `4H` | `Whale Positions` | `46.24%` | `53.76%` | `0.86` | 33,430,000.00 USD |
| `4H` | `Global Accounts` | `48.77%` | `51.23%` | `0.95` | 95,980,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `54.30` | `54.36` | `54.30` | `54.62` | `54.16` | 1,483,061.64 USD | 620,330.38 USD | 862,731.26 USD | -242,400.88 USD | `-16.34%` | `4B / 6S` |
| `5:00 UTC` | `54.11` | `54.23` | `54.11` | `54.50` | `54.03` | 1,110,276.34 USD | 501,463.73 USD | 608,812.62 USD | -107,348.89 USD | `-9.67%` | `2B / 8S` |
| `0:00 UTC` | `53.86` | `54.08` | `53.86` | `54.55` | `53.64` | 1,780,531.79 USD | 1,005,907.66 USD | 774,624.13 USD | 231,283.53 USD | `+12.99%` | `11B / 6S` |
| `5:00 UTC` | `54.34` | `54.28` | `54.34` | `54.41` | `54.11` | 777,440.60 USD | 385,500.86 USD | 391,939.75 USD | -6,438.89 USD | `-0.83%` | `0B / 4S` |
| `0:00 UTC` | `54.52` | `54.26` | `54.52` | `54.55` | `53.91` | 698,950.15 USD | 352,602.70 USD | 346,347.45 USD | 6,255.26 USD | `+0.89%` | `7B / 7S` |
| `5:00 UTC` | `55.09` | `54.88` | `55.09` | `55.16` | `54.53` | 1,113,307.98 USD | 534,835.45 USD | 578,472.53 USD | -43,637.08 USD | `-3.92%` | `11B / 6S` |
| `0:00 UTC` | `55.17` | `55.17` | `55.17` | `55.34` | `55.00` | 1,657,433.83 USD | 827,264.59 USD | 830,169.24 USD | -2,904.65 USD | `-0.18%` | `3B / 4S` |
| `5:00 UTC` | `55.09` | `55.12` | `55.09` | `55.28` | `54.97` | 863,748.33 USD | 238,704.69 USD | 625,043.64 USD | -386,338.95 USD | `-44.73%` | `0B / 13S` |
| `0:00 UTC` | `55.41` | `55.33` | `55.41` | `55.44` | `55.11` | 1,037,180.75 USD | 435,075.60 USD | 602,105.15 USD | -167,029.55 USD | `-16.10%` | `6B / 3S` |
| `5:00 UTC` | `55.28` | `55.28` | `55.28` | `55.38` | `55.20` | 220,040.77 USD | 83,095.31 USD | 136,945.46 USD | -53,850.15 USD | `-24.47%` | `1B / 2S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 21:10` | `Volume 50K LTC` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `58.75` | 0.00 USD | 0.00 USD |
| `10-28 20:58` | `Volume 50K LTC` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `58.09` | 8,700.00 USD | 0.00 USD |
| `10-28 20:51` | `Range 0.2` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `58.55` | 0.00 USD | 0.00 USD |
| `10-28 20:34` | `Volume 50K LTC` | `Divergence` | **`BULLISH`** | Drop without taker selling | `57.96` | 0.00 USD | 0.00 USD |
| `10-28 20:31` | `Range 0.2` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `58.43` | 0.00 USD | 0.00 USD |
| `10-28 20:22` | `Range 0.2` | `Divergence` | **`BULLISH`** | Drop without taker selling | `57.80` | 0.00 USD | 0.00 USD |
| `10-28 19:58` | `Range 0.2` | `Trapped longs` | **`BEARISH`** | Failed breakout | `57.47` | 6,700.00 USD | 0.00 USD |
| `10-28 19:07` | `Range 0.2` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `57.43` | 3,500.00 USD | 0.00 USD |
| `10-28 17:09` | `Range 0.2` | `Divergence` | **`BULLISH`** | Drop without taker selling | `57.66` | 0.00 USD | 0.00 USD |
| `10-28 16:32` | `Range 0.2` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `57.49` | 0.00 USD | 0.00 USD |
| `10-28 14:20` | `Volume 50K LTC` | `Divergence` | **`BEARISH`** | Rally without taker buying | `57.96` | 0.00 USD | 0.00 USD |
| `10-28 11:09` | `Range 0.2` | `Divergence` | **`BEARISH`** | Rally without taker buying | `57.49` | 0.00 USD | 0.00 USD |
| `10-28 08:20` | `Range 0.2` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `57.39` | 4,900.00 USD | 0.00 USD |
| `10-28 07:52` | `Range 0.2` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `57.28` | 2,800.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 83,080.00 USD | -5,400.00 USD | **`ACCUMULATION`** |
| `15m` | 101,360.00 USD | -68,530.00 USD | **`ACCUMULATION`** |
| `30m` | 106,180.00 USD | -302,880.00 USD | **`DISTRIBUTION`** |
| `1h` | 179,880.00 USD | -714,060.00 USD | **`DISTRIBUTION`** |
| `2h` | 285,080.00 USD | -276,930.00 USD | **`ACCUMULATION`** |
| `4h` | -786,300.00 USD | -2,900,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 296,690.00 USD | -2,480,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,950,000.00 USD | -5,740,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,030,000.00 USD | -6,070,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 579,750.00 USD | -4,080,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 3,410,000.00 USD | -24,980,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -23,190,000.00 USD | -194,520,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+83.08K` | 15m=`+101.36K` | 1h=`+179.88K` | 24h=`+579.75K`
* Futures Capital Netflows: 5m=`-5.40K` | 15m=`-68.53K` | 1h=`-714.06K` | 24h=`-4.08M`
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
  * `2026-10-30 08:33:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:00:58 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:48:58 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:47:58 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:47:58 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:47:58 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:49:58 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:49:58 IST`: [investinglive.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `54.10` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `53.01` (Risk Distance: `1.09` pts)
  * +2.5R Take Profit: `56.83`
  * Mathematical Lot Sizing: **`9.15 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `55.66` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `56.76` (Risk Distance: `1.09` pts)
  * +2.5R Take Profit: `52.93`
  * Mathematical Lot Sizing: **`9.15 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`55.84`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
