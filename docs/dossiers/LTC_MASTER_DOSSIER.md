# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 10:34:48 IST` (`2026-10-30 05:04:48 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `55.92` | **Live Ask Quote**: `56.22` | **Mid Price**: `56.07`
- **Spread Points**: `300.00` | **Spread BPS**: `53.50 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `54.40` | VWAP Z-Score: `+1.65` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.4497` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `56.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `56.85` | Lower -3.00σ Band: `51.95`
  * Upper +2.51σ Band: `56.45` | Lower -2.51σ Band: `52.35`
  * Upper +2.01σ Band: `56.04` | Lower -2.01σ Band: `52.75`
  * Upper +2.00σ Band: `56.03` | Lower -2.00σ Band: `52.76`
  * Upper +1.28σ Band: `55.44` | Lower -1.28σ Band: `53.35`
  * Upper +1.00σ Band: `55.22` | Lower -1.00σ Band: `53.58`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`55.58` | EMA-20=`55.32` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`55.73` (Slope: `+0.0000`) | EMA-100=`56.38`
  * Institutional Anchors: EMA-144=`56.64` | EMA-200=`56.69` (Slope: `-0.2895`) | EMA-233=`56.76`
- **Range Boundaries**: 24H High=`58.72` | 24H Low=`52.64` | Weekly High=`59.62` | Weekly Low=`52.64`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `56.02` (Distance: `+0.11%`)
  * Point of Control (POC) = `55.28` (Distance: `+1.46%`)
  * Value Area Low (VAL) = `54.26` (Distance: `+3.37%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.40` | POC=`57.72` | VAL=`56.83`
  * Prior Day Extremes: PDH=`59.52` | PDL=`54.18` | PDC=`54.46`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`58.39` | Weekly POC=`56.43` | Weekly VAL=`55.97`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`56.03` | Low=`52.64`
  * London Session (08:00-16:00 UTC): High=`55.98` | Low=`55.73`
  * New York Session (13:00-21:00 UTC): High=`56.41` | Low=`55.73`
  * Initial Balance (First Hour): IB High=`55.98` | IB Low=`55.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `55.85` - `56.29`
  * Optimal Trade Entry (OTE 0.705): `56.18`
  * Structural Invalidation Anchor (0.786): `56.52`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `56.11` | `56.15` | `56.05` | `56.10` | `3,251` | 182,363.27 USD | -13,332.70 USD | `-7.31%` | -5,724,506.30 USD | `+0.32` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `56.09` | `56.09` | `55.98` | `55.98` | `3,151` | 176,611.17 USD | -32,242.65 USD | `-18.26%` | -5,756,748.95 USD | `+0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `55.99` | `56.24` | `55.98` | `56.18` | `4,528` | 254,082.34 USD | 55,204.90 USD | `+21.73%` | -5,701,544.05 USD | `+1.21` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `56.13` | `56.27` | `56.12` | `56.22` | `11,491` | 645,876.21 USD | -58,194.71 USD | `-9.01%` | -5,807,884.88 USD | `+0.24` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `56.23` | `56.25` | `55.98` | `55.98` | `10,748` | 603,205.25 USD | -60,425.65 USD | `-10.02%` | -5,868,310.53 USD | `+0.24` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `55.99` | `56.24` | `55.98` | `56.18` | `4,528` | 254,082.34 USD | 55,204.90 USD | `+21.73%` | -5,813,105.63 USD | `+0.65` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `55.13` | `56.26` | `55.11` | `56.25` | `76,464` | 4,260,452.16 USD | -513,161.69 USD | `-12.04%` | -4,553,852.57 USD | `-0.35` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `56.25` | `56.29` | `55.73` | `55.98` | `57,057` | 3,198,717.26 USD | -379,690.29 USD | `-11.87%` | -4,933,542.86 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `55.99` | `56.24` | `55.98` | `56.17` | `4,526` | 253,992.29 USD | 55,162.48 USD | `+21.72%` | -4,878,380.38 USD | `+0.39` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,423,359.63 USD | `-1.73` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -4,601,875.81 USD | `-0.83` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.29` | `55.73` | `56.17` | `61,558` | 3,451,267.77 USD | -324,846.39 USD | `-9.41%` | -4,926,722.20 USD | `+0.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | 701,394.73 USD | `-1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | 840,681.28 USD | `-1.08` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,423,359.63 USD | `-1.73` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -4,601,875.81 USD | `-0.83` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.29` | `55.73` | `56.17` | `61,558` | 3,451,267.77 USD | -324,846.39 USD | `-9.41%` | -4,926,722.20 USD | `+0.35` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:34:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1070` | `0xeadc...9d55` | `LONG` | 2,043,794.31 USD | `36,463.77` | `52.78` | `56.08` | `0.000000` | 119,118.36 USD | `+5.83%` | `10X Cross` |
| `1081` | `0x9aa5...58af` | `SHORT` | 2,028,878.79 USD | `36,177.65` | `71.22` | `56.08` | `302.86` | 547,607.88 USD | `+26.99%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `58.57` | 7,509.64 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 58.5730 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `58.16` | 6,599.76 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 6.60K USD at 58.1630 USD [API] | `2026-10-29 02:05:49` |
| `ANNOUNCEMENT` | `INFO` | `58.12` | 7,509.75 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 7.51K USD at 58.1160 USD [API] | `2026-10-29 02:11:22` |
| `ANNOUNCEMENT` | `INFO` | `58.05` | 7,509.74 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 7.51K USD at 58.0530 USD [API] | `2026-10-29 02:29:31` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`59.03` (Vol: 286,000.00 USD, Dist: `+5.38%`) | Long MP=`54.13` (Vol: 113,000.00 USD, Dist: `--3.37%`)
  * 48H Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+5.32%`) | Long MP=`54.12` (Vol: 113,000.00 USD, Dist: `--3.40%`)
  * 3D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+5.32%`) | Long MP=`54.12` (Vol: 113,000.00 USD, Dist: `--3.40%`)
  * 7D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+5.32%`) | Long MP=`54.12` (Vol: 113,000.00 USD, Dist: `--3.40%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `11.35` | 136.20 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.25` | 265.33 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.75` | 2,560.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.15` | 2,220.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.65` | 150.15 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `16.95` | 2,550.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.25` | 2,190.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.05` | 3,470.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.35` | 155.77 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.45` | 2,010.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.45` | 19,020.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.95` | 465.93 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.65` | 4,220.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.35` | 147.51 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.75` | 366.96 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.55` | 1,410.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.65` | 1,220.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.85` | 195.57 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.05` | 380.47 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.65` | 466.13 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 277,980.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 173.39 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.45` | 7,500.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 50,740.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.75` | 117,590.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 374.20 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.05` | 1,010.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.05` | 5,510.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 272.75 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 173.85 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.15` | 166.37 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.25` | 8,470.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.95` | 802.20 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 583.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 297,500.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 218.46 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.65` | 1,540.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 538.53 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 5,880.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 1,060.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.65` | 4,640.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 3,460.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 125.24 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.05` | 2,740.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 450.10 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.35` | 22,750.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 653.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 5,020.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 32,850.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.15` | 232.05 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 257.76 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.95` | 5,910.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 182.85 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 126.70 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.45` | 65,890.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 7,770.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 104.85 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 166.49 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.45` | 422.56 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.65` | 178.25 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 3,020.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 708.59 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 101.80 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.85` | 319.49 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 438.74 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.25` | 1,050.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 9,260.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 3,530.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 377.50 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 6,210.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 446.67 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.25` | 695.38 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 2,770.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 2,400.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 993.82 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 5,290.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 2,730.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 664,760.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 570.02 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 264.83 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 716.41 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 312.44 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 5,900.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 1,180.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 133.10 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 2,160.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 1,010.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 133.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 274.39 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 6,340.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 509.01 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 9,430.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.15` | 5,430.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 14,490.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 1,680.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 982.29 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 66,300.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 35,410.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 1,570.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 5,800.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 2,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 56,340.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 122,400.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 417.80 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 5,390.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 6,900.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 426.02 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 21,880.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 801.14 USD | 980,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 3,490.00 USD | 979,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 2,910.00 USD | 976,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 84,440.00 USD | 973,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.45` | 1,330.00 USD | 889,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 842.44 USD | 887,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 4,230.00 USD | 886,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 134.55 USD | 882,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 2,620.00 USD | 882,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 6,190.00 USD | 879,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 8,710.00 USD | 873,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 30,370.00 USD | 865,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 2,180.00 USD | 834,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 23,940.00 USD | 832,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 12,060.00 USD | 808,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 42,180.00 USD | 796,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 2,940.00 USD | 754,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 706.41 USD | 751,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.15` | 1,070.00 USD | 750,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.25` | 842.21 USD | 749,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.35` | 22,820.00 USD | 748,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 2,140.00 USD | 725,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 3,980.00 USD | 723,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 358.40 USD | 719,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 158.22 USD | 719,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.10` | 8,330,000.00 USD | 8,330,000.00 USD | 28,250.00 USD | 12,890.00 USD | 9,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.15` | 1,980.00 USD | 719,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.20` | 8,280,000.00 USD | 8,280,000.00 USD | 12,340.00 USD | 3,420.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.25` | 1,220.00 USD | 717,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.30` | 8,260,000.00 USD | 8,260,000.00 USD | 692.33 USD | 4,740.00 USD | 6,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.35` | 43,340.00 USD | 716,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.40` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 1,520.00 USD | 28,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.45` | 2,860.00 USD | 672,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.50` | 8,220,000.00 USD | 8,220,000.00 USD | 11,830.00 USD | 0.00 USD | 7,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.55` | 4,450.00 USD | 669,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 47,930.00 USD | 665,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 1,340.00 USD | 617,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.10` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.15` | 1,690.00 USD | 616,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.20` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.25` | 110.49 USD | 614,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.35` | 7,960.00 USD | 614,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.40` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 6,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.55` | 2,560.00 USD | 606,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.60` | 8,180,000.00 USD | 8,180,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.65` | 2,160.00 USD | 603,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 333.94 USD | 601,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.80` | 8,180,000.00 USD | 8,180,000.00 USD | 1,780.00 USD | 2,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `48.90` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 0.00 USD | 960.40 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.95` | 252.58 USD | 601,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,580.00 USD | 601,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,740.00 USD | 599,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.30` | 8,170,000.00 USD | 8,170,000.00 USD | 15,190.00 USD | 4,490.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.35` | 5,230.00 USD | 593,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.40` | 8,140,000.00 USD | 8,140,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.45` | 419.34 USD | 588,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.50` | 8,130,000.00 USD | 8,130,000.00 USD | 2,830.00 USD | 7,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.55` | 18,010.00 USD | 588,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.60` | 3,180,000.00 USD | 3,180,000.00 USD | 6,740.00 USD | 13,640.00 USD | 16,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.60` | 8,120,000.00 USD | 8,120,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.65` | 73,260.00 USD | 570,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.70` | 3,150,000.00 USD | 3,150,000.00 USD | 10,180.00 USD | 2,280.00 USD | 2,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.70` | 8,100,000.00 USD | 8,100,000.00 USD | 12,090.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.75` | 20,710.00 USD | 496,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.80` | 3,130,000.00 USD | 3,130,000.00 USD | 6,420.00 USD | 4,300.00 USD | 21,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.80` | 8,090,000.00 USD | 8,090,000.00 USD | 9,930.00 USD | 8,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `49.90` | 3,100,000.00 USD | 3,100,000.00 USD | 20,400.00 USD | 8,690.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.90` | 8,070,000.00 USD | 8,070,000.00 USD | 45,030.00 USD | 7,170.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.95` | 19,920.00 USD | 476,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.00` | 3,050,000.00 USD | 3,050,000.00 USD | 7,670.00 USD | 6,270.00 USD | 40,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.00` | 8,010,000.00 USD | 8,010,000.00 USD | 22,100.00 USD | 7,630.00 USD | 24,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.05` | 1,820.00 USD | 456,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.10` | 2,990,000.00 USD | 2,990,000.00 USD | 3,780.00 USD | 3,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.10` | 7,960,000.00 USD | 7,960,000.00 USD | 363.50 USD | 682.90 USD | 8,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.20` | 2,990,000.00 USD | 2,990,000.00 USD | 177.10 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.20` | 7,950,000.00 USD | 7,950,000.00 USD | 6,960.00 USD | 500.40 USD | 34,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.25` | 102.51 USD | 454,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.30` | 2,980,000.00 USD | 2,980,000.00 USD | 171.03 USD | 333.03 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.30` | 7,900,000.00 USD | 7,900,000.00 USD | 16,270.00 USD | 3,640.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.35` | 1,140.00 USD | 454,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.40` | 2,980,000.00 USD | 2,980,000.00 USD | 4,370.00 USD | 2,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.40` | 7,880,000.00 USD | 7,880,000.00 USD | 28,280.00 USD | 19,110.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,720.00 USD | 453,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.50` | 2,970,000.00 USD | 2,970,000.00 USD | 5,790.00 USD | 1,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.50` | 7,800,000.00 USD | 7,800,000.00 USD | 24,840.00 USD | 6,790.00 USD | 43,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.55` | 84,100.00 USD | 448,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.60` | 2,970,000.00 USD | 2,970,000.00 USD | 1,660.00 USD | 1,750.00 USD | 5,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.60` | 7,730,000.00 USD | 7,730,000.00 USD | 56,670.00 USD | 17,830.00 USD | 22,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.70` | 2,960,000.00 USD | 2,960,000.00 USD | 2,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.70` | 7,630,000.00 USD | 7,630,000.00 USD | 53,670.00 USD | 24,710.00 USD | 32,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.75` | 9,050.00 USD | 364,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.80` | 2,950,000.00 USD | 2,950,000.00 USD | 5,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.80` | 7,520,000.00 USD | 7,520,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.90` | 2,950,000.00 USD | 2,950,000.00 USD | 826.24 USD | 260.05 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.90` | 7,420,000.00 USD | 7,420,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.95` | 431.55 USD | 355,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.00` | 2,940,000.00 USD | 2,940,000.00 USD | 5,040.00 USD | 0.00 USD | 430.77 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.00` | 7,170,000.00 USD | 7,170,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.10` | 2,930,000.00 USD | 2,930,000.00 USD | 9,210.00 USD | 6,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.10` | 7,040,000.00 USD | 7,040,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.15` | 219,370.00 USD | 354,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.20` | 2,920,000.00 USD | 2,920,000.00 USD | 2,360.00 USD | 1,130.00 USD | 17,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.20` | 6,960,000.00 USD | 6,960,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.25` | 202.44 USD | 135,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.30` | 2,900,000.00 USD | 2,900,000.00 USD | 16,790.00 USD | 14,100.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.30` | 6,900,000.00 USD | 6,900,000.00 USD | 28,400.00 USD | 26,720.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.35` | 453.93 USD | 135,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.40` | 2,860,000.00 USD | 2,860,000.00 USD | 13,750.00 USD | 11,490.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.40` | 6,790,000.00 USD | 6,790,000.00 USD | 73,130.00 USD | 42,820.00 USD | 46,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.45` | 27,210.00 USD | 134,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.50` | 2,820,000.00 USD | 2,820,000.00 USD | 7,880.00 USD | 10,980.00 USD | 37,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.50` | 6,630,000.00 USD | 6,630,000.00 USD | 38,520.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.55` | 551.07 USD | 107,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.60` | 2,770,000.00 USD | 2,770,000.00 USD | 9,060.00 USD | 18,490.00 USD | 757.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.60` | 6,530,000.00 USD | 6,530,000.00 USD | 37,880.00 USD | 36,790.00 USD | 41,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.65` | 9,100.00 USD | 107,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.70` | 2,740,000.00 USD | 2,740,000.00 USD | 2,890.00 USD | 13,810.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.70` | 6,420,000.00 USD | 6,420,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.75` | 6,480.00 USD | 97,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.80` | 2,700,000.00 USD | 2,700,000.00 USD | 12,590.00 USD | 19,270.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.80` | 6,380,000.00 USD | 6,380,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.85` | 13,680.00 USD | 91,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.90` | 2,660,000.00 USD | 2,660,000.00 USD | 9,460.00 USD | 27,280.00 USD | 23,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.90` | 6,320,000.00 USD | 6,320,000.00 USD | 5,870.00 USD | 25,410.00 USD | 28,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.95` | 16,800.00 USD | 77,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.00` | 2,600,000.00 USD | 2,600,000.00 USD | 25,510.00 USD | 25,740.00 USD | 28,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.00` | 6,260,000.00 USD | 6,260,000.00 USD | 64,300.00 USD | 26,440.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.10` | 2,520,000.00 USD | 2,520,000.00 USD | 51,300.00 USD | 19,850.00 USD | 52,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 6,160,000.00 USD | 6,160,000.00 USD | 24,220.00 USD | 28,090.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.15` | 1,900.00 USD | 60,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.20` | 2,390,000.00 USD | 2,390,000.00 USD | 15,450.00 USD | 8,060.00 USD | 46,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 6,070,000.00 USD | 6,070,000.00 USD | 38,380.00 USD | 13,960.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.25` | 4,930.00 USD | 59,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.30` | 2,320,000.00 USD | 2,320,000.00 USD | 31,960.00 USD | 21,640.00 USD | 12,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 5,990,000.00 USD | 5,990,000.00 USD | 24,840.00 USD | 41,300.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.35` | 134.02 USD | 54,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.40` | 2,260,000.00 USD | 2,260,000.00 USD | 12,460.00 USD | 17,080.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 5,920,000.00 USD | 5,920,000.00 USD | 20,580.00 USD | 38,950.00 USD | 22,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.45` | 7,570.00 USD | 54,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.50` | 2,220,000.00 USD | 2,220,000.00 USD | 53,350.00 USD | 29,580.00 USD | 74,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.50` | 5,840,000.00 USD | 5,840,000.00 USD | 38,720.00 USD | 667.05 USD | 11,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.55` | 8,700.00 USD | 46,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.60` | 2,060,000.00 USD | 2,060,000.00 USD | 8,330.00 USD | 40,700.00 USD | 717.10 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.60` | 5,790,000.00 USD | 5,790,000.00 USD | 74,610.00 USD | 32,590.00 USD | 59,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.70` | 2,010,000.00 USD | 2,010,000.00 USD | 16,690.00 USD | 19,440.00 USD | 28,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.70` | 5,620,000.00 USD | 5,620,000.00 USD | 20,250.00 USD | 92,920.00 USD | 108,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.75` | 4,240.00 USD | 37,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.80` | 1,950,000.00 USD | 1,950,000.00 USD | 27,090.00 USD | 50,290.00 USD | 102,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.80` | 5,400,000.00 USD | 5,400,000.00 USD | 46,600.00 USD | 35,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.85` | 5,950.00 USD | 33,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.90` | 1,770,000.00 USD | 1,770,000.00 USD | 43,760.00 USD | 50,040.00 USD | 26,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.90` | 5,320,000.00 USD | 5,320,000.00 USD | 51,920.00 USD | 28,710.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.95` | 25,840.00 USD | 27,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.00` | 1,650,000.00 USD | 1,650,000.00 USD | 26,670.00 USD | 30,500.00 USD | 39,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.00` | 5,200,000.00 USD | 5,200,000.00 USD | 47,240.00 USD | 25,810.00 USD | 89,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.10` | 1,550,000.00 USD | 1,550,000.00 USD | 14,570.00 USD | 42,760.00 USD | 87,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.10` | 5,040,000.00 USD | 5,040,000.00 USD | 52,120.00 USD | 17,950.00 USD | 9,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.15` | 1,720.00 USD | 1,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.20` | 1,410,000.00 USD | 1,410,000.00 USD | 24,240.00 USD | 6,510.00 USD | 41,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.20` | 4,960,000.00 USD | 4,960,000.00 USD | 162,460.00 USD | 28,320.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.30` | 1,340,000.00 USD | 1,340,000.00 USD | 3,650.00 USD | 0.00 USD | 5,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.30` | 4,750,000.00 USD | 4,750,000.00 USD | 57,250.00 USD | 24,540.00 USD | 34,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.40` | 1,330,000.00 USD | 1,330,000.00 USD | 3,460.00 USD | 1,850.00 USD | 657.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.40` | 4,630,000.00 USD | 4,630,000.00 USD | 44,030.00 USD | 7,250.00 USD | 91,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.50` | 1,320,000.00 USD | 1,320,000.00 USD | 9,110.00 USD | 3,940.00 USD | 2,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.50` | 4,490,000.00 USD | 4,490,000.00 USD | 48,660.00 USD | 3,440.00 USD | 20,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.60` | 1,300,000.00 USD | 1,300,000.00 USD | 72,650.00 USD | 220.65 USD | 13,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.60` | 4,410,000.00 USD | 4,410,000.00 USD | 52,800.00 USD | 1,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.70` | 1,220,000.00 USD | 1,220,000.00 USD | 6,210.00 USD | 0.00 USD | 5,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.70` | 4,360,000.00 USD | 4,360,000.00 USD | 131,400.00 USD | 3,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.80` | 1,210,000.00 USD | 1,210,000.00 USD | 44,920.00 USD | 1,750.00 USD | 168.97 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.80` | 4,220,000.00 USD | 4,220,000.00 USD | 99,150.00 USD | 13,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.90` | 1,160,000.00 USD | 1,160,000.00 USD | 42,200.00 USD | 15,000.00 USD | 281.90 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.90` | 4,110,000.00 USD | 4,110,000.00 USD | 129,920.00 USD | 21,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.00` | 1,100,000.00 USD | 1,100,000.00 USD | 31,050.00 USD | 7,680.00 USD | 27,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.00` | 3,960,000.00 USD | 3,960,000.00 USD | 324,350.00 USD | 42,300.00 USD | 220,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.10` | 1,040,000.00 USD | 1,040,000.00 USD | 72,230.00 USD | 11,410.00 USD | 19,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.10` | 3,370,000.00 USD | 3,370,000.00 USD | 290,620.00 USD | 0.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.20` | 932,270.00 USD | 932,270.00 USD | 72,600.00 USD | 15,510.00 USD | 40,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.20` | 3,080,000.00 USD | 3,080,000.00 USD | 205,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.30` | 804,040.00 USD | 804,040.00 USD | 15,600.00 USD | 0.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.30` | 2,870,000.00 USD | 2,870,000.00 USD | 381,380.00 USD | 0.00 USD | 181,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.40` | 783,090.00 USD | 783,090.00 USD | 51,570.00 USD | 35,500.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.40` | 2,310,000.00 USD | 2,310,000.00 USD | 304,270.00 USD | 13,830.00 USD | 92,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.50` | 692,900.00 USD | 692,900.00 USD | 9,670.00 USD | 46,240.00 USD | 1,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.50` | 1,900,000.00 USD | 1,900,000.00 USD | 159,720.00 USD | 15,240.00 USD | 239,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.60` | 635,670.00 USD | 635,670.00 USD | 1,520.00 USD | 21,680.00 USD | 5,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.60` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 1,930.00 USD | 116,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.70` | 606,900.00 USD | 606,900.00 USD | 0.00 USD | 15,420.00 USD | 82,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.80` | 509,020.00 USD | 509,020.00 USD | 0.00 USD | 25,800.00 USD | 11,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.90` | 471,550.00 USD | 471,550.00 USD | 49,450.00 USD | 10,930.00 USD | 1,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.90` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 52,180.00 USD | 47,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.00` | 409,630.00 USD | 409,630.00 USD | 19,950.00 USD | 5,030.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.00` | 1,270,000.00 USD | 1,270,000.00 USD | 35,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.10` | 354,890.00 USD | 354,890.00 USD | 0.00 USD | 45,630.00 USD | 28,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.20` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 19,190.00 USD | 46,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.30` | 281,130.00 USD | 281,130.00 USD | 0.00 USD | 7,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.30` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 11,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.40` | 273,990.00 USD | 273,990.00 USD | 0.00 USD | 6,510.00 USD | 742.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.40` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 18,550.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.50` | 266,740.00 USD | 266,740.00 USD | 0.00 USD | 9,250.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.50` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 33,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.60` | 1,100,000.00 USD | 1,100,000.00 USD | 426,340.00 USD | 13,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.70` | 251,990.00 USD | 251,990.00 USD | 0.00 USD | 7,490.00 USD | 613.46 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.70` | 658,340.00 USD | 658,340.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.80` | 243,880.00 USD | 243,880.00 USD | 6,170.00 USD | 26,160.00 USD | 3,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.80` | 451,910.00 USD | 451,910.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.90` | 208,210.00 USD | 208,210.00 USD | 103,700.00 USD | 13,230.00 USD | 91,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.90` | 360,950.00 USD | 360,950.00 USD | 141,330.00 USD | 101,960.00 USD | 117,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.00` | 25,100.00 USD | 25,100.00 USD | 0.00 USD | 20,600.00 USD | 4,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.00` | 50,200.00 USD | 50,200.00 USD | 0.00 USD | 20,600.00 USD | 4,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.00` | 470,900.00 USD | 470,900.00 USD | 181,230.00 USD | 118,560.00 USD | 171,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.00` | 941,800.00 USD | 941,800.00 USD | 181,230.00 USD | 118,560.00 USD | 171,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.10` | 317,870.00 USD | 317,870.00 USD | 68,240.00 USD | 5,890.00 USD | 193,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.10` | 1,280,000.00 USD | 1,280,000.00 USD | 121,920.00 USD | 154,860.00 USD | 61,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.20` | 441,140.00 USD | 441,140.00 USD | 59,290.00 USD | 6,070.00 USD | 57,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.20` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 86,240.00 USD | 240,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.30` | 619,220.00 USD | 619,220.00 USD | 51,850.00 USD | 51,230.00 USD | 75,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.30` | 2,050,000.00 USD | 2,050,000.00 USD | 148,350.00 USD | 141,900.00 USD | 157,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.40` | 1,010,000.00 USD | 1,010,000.00 USD | 77,640.00 USD | 78,590.00 USD | 238,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.40` | 2,530,000.00 USD | 2,530,000.00 USD | 215,940.00 USD | 125,620.00 USD | 137,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.50` | 1,440,000.00 USD | 1,440,000.00 USD | 138,540.00 USD | 143,390.00 USD | 144,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.50` | 2,850,000.00 USD | 2,850,000.00 USD | 170,750.00 USD | 143,420.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.60` | 1,680,000.00 USD | 1,680,000.00 USD | 49,560.00 USD | 104,240.00 USD | 80,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.60` | 3,350,000.00 USD | 3,350,000.00 USD | 363,190.00 USD | 136,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.70` | 2,210,000.00 USD | 2,210,000.00 USD | 188,500.00 USD | 27,730.00 USD | 317,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.70` | 3,690,000.00 USD | 3,690,000.00 USD | 117,290.00 USD | 121,500.00 USD | 98,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.80` | 2,430,000.00 USD | 2,430,000.00 USD | 129,190.00 USD | 17,250.00 USD | 75,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.80` | 4,240,000.00 USD | 4,240,000.00 USD | 153,580.00 USD | 92,780.00 USD | 303,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.90` | 2,500,000.00 USD | 2,500,000.00 USD | 38,540.00 USD | 10,710.00 USD | 22,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.90` | 4,670,000.00 USD | 4,670,000.00 USD | 113,780.00 USD | 48,600.00 USD | 266,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.00` | 2,540,000.00 USD | 2,540,000.00 USD | 6,480.00 USD | 18,250.00 USD | 12,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.00` | 4,930,000.00 USD | 4,930,000.00 USD | 88,680.00 USD | 20,690.00 USD | 151,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.10` | 2,650,000.00 USD | 2,650,000.00 USD | 59,550.00 USD | 22,890.00 USD | 25,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.10` | 5,010,000.00 USD | 5,010,000.00 USD | 36,580.00 USD | 19,180.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.20` | 2,780,000.00 USD | 2,780,000.00 USD | 32,320.00 USD | 29,370.00 USD | 65,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.20` | 5,090,000.00 USD | 5,090,000.00 USD | 57,060.00 USD | 21,090.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.30` | 2,860,000.00 USD | 2,860,000.00 USD | 20,410.00 USD | 28,940.00 USD | 35,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.30` | 5,160,000.00 USD | 5,160,000.00 USD | 22,360.00 USD | 10,060.00 USD | 34,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.40` | 2,960,000.00 USD | 2,960,000.00 USD | 45,570.00 USD | 37,640.00 USD | 12,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.40` | 5,410,000.00 USD | 5,410,000.00 USD | 66,770.00 USD | 31,660.00 USD | 154,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.50` | 3,250,000.00 USD | 3,250,000.00 USD | 144,970.00 USD | 32,830.00 USD | 115,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.50` | 5,520,000.00 USD | 5,520,000.00 USD | 76,670.00 USD | 31,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.60` | 3,410,000.00 USD | 3,410,000.00 USD | 69,720.00 USD | 24,050.00 USD | 62,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.60` | 5,740,000.00 USD | 5,740,000.00 USD | 149,560.00 USD | 40,430.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.70` | 3,560,000.00 USD | 3,560,000.00 USD | 36,620.00 USD | 26,070.00 USD | 96,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.70` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 5,400.00 USD | 57,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.75` | 155.35 USD | 155.35 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `57.80` | 3,660,000.00 USD | 3,660,000.00 USD | 9,690.00 USD | 13,860.00 USD | 73,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.80` | 5,870,000.00 USD | 5,870,000.00 USD | 9,650.00 USD | 14,360.00 USD | 49,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.90` | 3,700,000.00 USD | 3,700,000.00 USD | 13,000.00 USD | 14,100.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.90` | 5,900,000.00 USD | 5,900,000.00 USD | 5,120.00 USD | 963.90 USD | 22,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.95` | 125.75 USD | 281.10 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.00` | 3,720,000.00 USD | 3,720,000.00 USD | 4,580.00 USD | 5,870.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.00` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 3,670.00 USD | 86,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `58.05` | 201,590.00 USD | 201,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.10` | 3,770,000.00 USD | 3,770,000.00 USD | 31,400.00 USD | 6,730.00 USD | 15,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.10` | 6,000,000.00 USD | 6,000,000.00 USD | 5,470.00 USD | 1,310.00 USD | 848.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.20` | 3,810,000.00 USD | 3,810,000.00 USD | 27,190.00 USD | 7,630.00 USD | 406.15 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.20` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 1,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.30` | 3,880,000.00 USD | 3,880,000.00 USD | 21,400.00 USD | 14,060.00 USD | 36,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.30` | 6,050,000.00 USD | 6,050,000.00 USD | 17,950.00 USD | 9,580.00 USD | 26,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.40` | 3,910,000.00 USD | 3,910,000.00 USD | 310.90 USD | 11,100.00 USD | 24,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.40` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 54,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.50` | 3,940,000.00 USD | 3,940,000.00 USD | 21,130.00 USD | 8,030.00 USD | 124.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.50` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.60` | 3,950,000.00 USD | 3,950,000.00 USD | 2,120.00 USD | 0.00 USD | 6,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.60` | 6,130,000.00 USD | 6,130,000.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.70` | 3,970,000.00 USD | 3,970,000.00 USD | 18,120.00 USD | 2,300.00 USD | 355.85 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.70` | 6,190,000.00 USD | 6,190,000.00 USD | 4,240.00 USD | 11,600.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.80` | 4,050,000.00 USD | 4,050,000.00 USD | 35,830.00 USD | 14,730.00 USD | 23,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.80` | 6,200,000.00 USD | 6,200,000.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.90` | 4,260,000.00 USD | 4,260,000.00 USD | 21,710.00 USD | 103,170.00 USD | 90,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.90` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 54,240.00 USD | 83,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.00` | 4,620,000.00 USD | 4,620,000.00 USD | 152,930.00 USD | 60,120.00 USD | 146,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.00` | 6,780,000.00 USD | 6,780,000.00 USD | 259,280.00 USD | 65,270.00 USD | 118,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.10` | 5,030,000.00 USD | 5,030,000.00 USD | 182,580.00 USD | 54,230.00 USD | 173,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.10` | 7,080,000.00 USD | 7,080,000.00 USD | 91,060.00 USD | 45,400.00 USD | 158,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.20` | 5,270,000.00 USD | 5,270,000.00 USD | 113,190.00 USD | 63,290.00 USD | 56,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.20` | 7,420,000.00 USD | 7,420,000.00 USD | 153,580.00 USD | 18,540.00 USD | 174,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.30` | 5,630,000.00 USD | 5,630,000.00 USD | 218,400.00 USD | 45,010.00 USD | 101,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.30` | 7,700,000.00 USD | 7,700,000.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.35` | 9,440.00 USD | 211,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.40` | 5,810,000.00 USD | 5,810,000.00 USD | 64,900.00 USD | 55,620.00 USD | 63,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.40` | 8,010,000.00 USD | 8,010,000.00 USD | 105,490.00 USD | 73,620.00 USD | 137,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.50` | 5,980,000.00 USD | 5,980,000.00 USD | 89,030.00 USD | 38,560.00 USD | 33,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.50` | 8,170,000.00 USD | 8,170,000.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.60` | 6,080,000.00 USD | 6,080,000.00 USD | 43,670.00 USD | 53,100.00 USD | 7,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.60` | 8,670,000.00 USD | 8,670,000.00 USD | 270,460.00 USD | 147,800.00 USD | 86,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.70` | 6,190,000.00 USD | 6,190,000.00 USD | 13,470.00 USD | 19,120.00 USD | 78,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.70` | 9,070,000.00 USD | 9,070,000.00 USD | 55,510.00 USD | 180,620.00 USD | 162,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.80` | 6,260,000.00 USD | 6,260,000.00 USD | 31,530.00 USD | 26,470.00 USD | 10,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.80` | 9,440,000.00 USD | 9,440,000.00 USD | 118,240.00 USD | 97,600.00 USD | 155,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.90` | 6,440,000.00 USD | 6,440,000.00 USD | 111,690.00 USD | 20,240.00 USD | 50,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.90` | 9,810,000.00 USD | 9,810,000.00 USD | 246,770.00 USD | 84,430.00 USD | 40,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.00` | 6,710,000.00 USD | 6,710,000.00 USD | 164,190.00 USD | 50,210.00 USD | 50,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.00` | 10,300,000.00 USD | 10,300,000.00 USD | 231,370.00 USD | 161,260.00 USD | 94,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.10` | 6,880,000.00 USD | 6,880,000.00 USD | 75,970.00 USD | 28,800.00 USD | 66,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.10` | 10,820,000.00 USD | 10,820,000.00 USD | 251,520.00 USD | 110,270.00 USD | 160,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.20` | 7,100,000.00 USD | 7,100,000.00 USD | 105,160.00 USD | 26,960.00 USD | 87,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.20` | 11,320,000.00 USD | 11,320,000.00 USD | 207,990.00 USD | 131,530.00 USD | 157,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.30` | 7,220,000.00 USD | 7,220,000.00 USD | 59,630.00 USD | 32,520.00 USD | 28,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.30` | 11,720,000.00 USD | 11,720,000.00 USD | 133,350.00 USD | 100,380.00 USD | 170,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.40` | 7,360,000.00 USD | 7,360,000.00 USD | 90,730.00 USD | 13,730.00 USD | 42,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.40` | 12,100,000.00 USD | 12,100,000.00 USD | 64,850.00 USD | 108,300.00 USD | 204,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.50` | 7,450,000.00 USD | 7,450,000.00 USD | 22,700.00 USD | 24,220.00 USD | 38,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.50` | 12,480,000.00 USD | 12,480,000.00 USD | 115,390.00 USD | 86,870.00 USD | 175,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.60` | 7,510,000.00 USD | 7,510,000.00 USD | 40,710.00 USD | 19,140.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.60` | 12,870,000.00 USD | 12,870,000.00 USD | 251,100.00 USD | 18,640.00 USD | 118,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.70` | 7,580,000.00 USD | 7,580,000.00 USD | 36,270.00 USD | 22,330.00 USD | 3,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.70` | 13,070,000.00 USD | 13,070,000.00 USD | 119,080.00 USD | 57,480.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.80` | 7,650,000.00 USD | 7,650,000.00 USD | 15,430.00 USD | 12,060.00 USD | 47,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.80` | 13,260,000.00 USD | 13,260,000.00 USD | 46,960.00 USD | 69,290.00 USD | 76,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.90` | 7,730,000.00 USD | 7,730,000.00 USD | 36,430.00 USD | 21,920.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.90` | 13,470,000.00 USD | 13,470,000.00 USD | 105,970.00 USD | 34,400.00 USD | 65,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.95` | 397.39 USD | 211,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.00` | 7,800,000.00 USD | 7,800,000.00 USD | 45,040.00 USD | 6,430.00 USD | 18,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 13,600,000.00 USD | 13,600,000.00 USD | 96,160.00 USD | 36,500.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.10` | 7,830,000.00 USD | 7,830,000.00 USD | 12,010.00 USD | 6,270.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 13,640,000.00 USD | 13,640,000.00 USD | 31,540.00 USD | 1,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.15` | 3,870.00 USD | 215,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.20` | 7,940,000.00 USD | 7,940,000.00 USD | 72,520.00 USD | 0.00 USD | 38,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.20` | 13,870,000.00 USD | 13,870,000.00 USD | 116,610.00 USD | 64,470.00 USD | 52,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.30` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 3,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.30` | 14,000,000.00 USD | 14,000,000.00 USD | 44,950.00 USD | 25,850.00 USD | 56,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.40` | 7,950,000.00 USD | 7,950,000.00 USD | 1,650.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.40` | 14,190,000.00 USD | 14,190,000.00 USD | 89,350.00 USD | 41,800.00 USD | 59,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.50` | 7,950,000.00 USD | 7,950,000.00 USD | 1,060.00 USD | 333.03 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.50` | 14,280,000.00 USD | 14,280,000.00 USD | 19,810.00 USD | 35,300.00 USD | 36,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.60` | 7,960,000.00 USD | 7,960,000.00 USD | 5,360.00 USD | 2,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.60` | 14,490,000.00 USD | 14,490,000.00 USD | 39,720.00 USD | 50,880.00 USD | 121,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.70` | 7,980,000.00 USD | 7,980,000.00 USD | 12,300.00 USD | 1,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.70` | 14,680,000.00 USD | 14,680,000.00 USD | 75,210.00 USD | 10,880.00 USD | 99,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.80` | 7,990,000.00 USD | 7,990,000.00 USD | 3,480.00 USD | 1,750.00 USD | 5,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.80` | 14,920,000.00 USD | 14,920,000.00 USD | 160,110.00 USD | 21,960.00 USD | 62,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.90` | 7,990,000.00 USD | 7,990,000.00 USD | 3,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.90` | 15,040,000.00 USD | 15,040,000.00 USD | 61,440.00 USD | 24,710.00 USD | 32,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.00` | 8,000,000.00 USD | 8,000,000.00 USD | 5,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.00` | 15,140,000.00 USD | 15,140,000.00 USD | 50,080.00 USD | 8,550.00 USD | 40,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.10` | 15,150,000.00 USD | 15,150,000.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.20` | 15,260,000.00 USD | 15,260,000.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.30` | 15,410,000.00 USD | 15,410,000.00 USD | 29,050.00 USD | 23,450.00 USD | 97,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.40` | 15,550,000.00 USD | 15,550,000.00 USD | 77,960.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.50` | 15,630,000.00 USD | 15,630,000.00 USD | 42,730.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.60` | 15,700,000.00 USD | 15,700,000.00 USD | 34,910.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.70` | 15,790,000.00 USD | 15,790,000.00 USD | 22,020.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.80` | 15,930,000.00 USD | 15,930,000.00 USD | 72,250.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.90` | 16,020,000.00 USD | 16,020,000.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `62.95` | 138.49 USD | 215,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `63.00` | 16,090,000.00 USD | 16,090,000.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.10` | 16,130,000.00 USD | 16,130,000.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.30` | 16,160,000.00 USD | 16,160,000.00 USD | 15,010.00 USD | 11,500.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.40` | 16,190,000.00 USD | 16,190,000.00 USD | 11,980.00 USD | 1,320.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `63.45` | 3,350.00 USD | 219,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `63.50` | 16,210,000.00 USD | 16,210,000.00 USD | 5,430.00 USD | 15,810.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.60` | 16,310,000.00 USD | 16,310,000.00 USD | 63,480.00 USD | 20,800.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.70` | 16,380,000.00 USD | 16,380,000.00 USD | 21,940.00 USD | 18,810.00 USD | 35,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.80` | 16,450,000.00 USD | 16,450,000.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.90` | 16,480,000.00 USD | 16,480,000.00 USD | 7,650.00 USD | 12,840.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.00` | 16,520,000.00 USD | 16,520,000.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.10` | 16,550,000.00 USD | 16,550,000.00 USD | 20,350.00 USD | 667.05 USD | 10,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.20` | 16,600,000.00 USD | 16,600,000.00 USD | 28,840.00 USD | 14,530.00 USD | 584.77 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.40` | 16,650,000.00 USD | 16,650,000.00 USD | 2,540.00 USD | 20,590.00 USD | 29,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.50` | 16,680,000.00 USD | 16,680,000.00 USD | 7,700.00 USD | 7,120.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.60` | 16,700,000.00 USD | 16,700,000.00 USD | 28,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `65.95` | 246.65 USD | 219,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.15` | 6,750.00 USD | 226,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.95` | 121.18 USD | 226,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.85` | 709.03 USD | 226,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `69.85` | 40,380.00 USD | 267,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `76.35` | 8,380.00 USD | 275,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.75` | 578,460.00 USD | 854,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.85` | 602.56 USD | 854,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.95` | 136.41 USD | 854,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.45` | 729.68 USD | 855,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.75` | 646.00 USD | 856,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.95` | 2,670.00 USD | 858,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.05` | 19,000.00 USD | 877,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.55` | 123.96 USD | 878,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.75` | 3,520.00 USD | 881,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `87.45` | 23,330.00 USD | 904,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `90.95` | 120.05 USD | 905,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `91.65` | 974.24 USD | 905,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.65` | 2,470.00 USD | 908,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.25` | 213.71 USD | 908,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.85` | 2,320.00 USD | 910,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.25` | 355,110.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.35` | 31,610.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.75` | 1,620.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.85` | 1,860.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.15` | 199.30 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.05` | 6,470.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 664.59 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `11.35` | 3,030,000.00 USD | 0.00 USD | 268.54 USD | `-79.75%` | `23.66` |
| `Live` | `Long` | `12.25` | 3,030,000.00 USD | 0.00 USD | 122.50 USD | `-78.14%` | `10.00` |
| `Live` | `Long` | `12.75` | 3,030,000.00 USD | 0.00 USD | 2,560.00 USD | `-77.25%` | `200.43` |
| `Live` | `Long` | `13.15` | 3,020,000.00 USD | 0.00 USD | 2,220.00 USD | `-76.54%` | `168.79` |
| `Live` | `Long` | `13.65` | 3,020,000.00 USD | 0.00 USD | 150.15 USD | `-75.64%` | `11.00` |
| `Live` | `Long` | `16.75` | 3,020,000.00 USD | 0.00 USD | 2,520.00 USD | `-70.11%` | `150.57` |
| `Live` | `Long` | `18.05` | 3,020,000.00 USD | 0.00 USD | 2,170.00 USD | `-67.79%` | `120.00` |
| `Live` | `Long` | `18.45` | 3,020,000.00 USD | 0.00 USD | 148.52 USD | `-67.08%` | `8.05` |
| `Live` | `Long` | `19.05` | 3,020,000.00 USD | 0.00 USD | 3,470.00 USD | `-66.01%` | `182.00` |
| `Live` | `Long` | `19.45` | 3,010,000.00 USD | 0.00 USD | 2,010.00 USD | `-65.29%` | `103.47` |
| `Live` | `Long` | `19.85` | 3,010,000.00 USD | 0.00 USD | 18,900.00 USD | `-64.58%` | `952.24` |
| `Live` | `Long` | `20.65` | 2,990,000.00 USD | 0.00 USD | 136.29 USD | `-63.15%` | `6.60` |
| `Live` | `Long` | `21.15` | 2,990,000.00 USD | 0.00 USD | 4,120.00 USD | `-62.26%` | `195.03` |
| `Live` | `Long` | `21.85` | 2,990,000.00 USD | 0.00 USD | 197.09 USD | `-61.01%` | `9.02` |
| `Live` | `Long` | `22.65` | 2,990,000.00 USD | 0.00 USD | 365.34 USD | `-59.58%` | `16.13` |
| `Live` | `Long` | `23.05` | 2,990,000.00 USD | 0.00 USD | 1,380.00 USD | `-58.87%` | `60.00` |
| `Live` | `Long` | `23.55` | 2,990,000.00 USD | 0.00 USD | 999.23 USD | `-57.98%` | `42.43` |
| `Live` | `Long` | `23.75` | 2,990,000.00 USD | 0.00 USD | 375.73 USD | `-57.62%` | `15.82` |
| `Live` | `Long` | `23.85` | 2,990,000.00 USD | 0.00 USD | 195.57 USD | `-57.44%` | `8.20` |
| `Live` | `Long` | `24.65` | 2,980,000.00 USD | 0.00 USD | 453.56 USD | `-56.02%` | `18.40` |
| `Live` | `Long` | `24.75` | 2,980,000.00 USD | 0.00 USD | 963.27 USD | `-55.84%` | `38.92` |
| `Live` | `Long` | `24.95` | 2,980,000.00 USD | 0.00 USD | 516.22 USD | `-55.48%` | `20.69` |
| `Live` | `Long` | `25.05` | 2,980,000.00 USD | 0.00 USD | 114,390.00 USD | `-55.30%` | `4,566.66` |
| `Live` | `Long` | `25.25` | 2,870,000.00 USD | 0.00 USD | 277,980.00 USD | `-54.94%` | `11,009.19` |
| `Live` | `Long` | `25.35` | 2,590,000.00 USD | 0.00 USD | 173.39 USD | `-54.77%` | `6.84` |
| `Live` | `Long` | `25.55` | 2,590,000.00 USD | 0.00 USD | 50,740.00 USD | `-54.41%` | `1,985.99` |
| `Live` | `Long` | `25.85` | 2,540,000.00 USD | 0.00 USD | 7,620.00 USD | `-53.87%` | `294.67` |
| `Live` | `Long` | `25.95` | 2,530,000.00 USD | 0.00 USD | 374.20 USD | `-53.70%` | `14.42` |
| `Live` | `Long` | `26.65` | 2,530,000.00 USD | 0.00 USD | 738.47 USD | `-52.45%` | `27.71` |
| `Live` | `Long` | `27.05` | 2,530,000.00 USD | 0.00 USD | 5,510.00 USD | `-51.73%` | `203.85` |
| `Live` | `Long` | `27.55` | 2,530,000.00 USD | 0.00 USD | 8,540.00 USD | `-50.84%` | `309.90` |
| `Live` | `Long` | `27.85` | 2,520,000.00 USD | 0.00 USD | 164.59 USD | `-50.31%` | `5.91` |
| `Live` | `Long` | `27.95` | 2,520,000.00 USD | 0.00 USD | 173.85 USD | `-50.13%` | `6.22` |
| `Live` | `Long` | `29.15` | 2,520,000.00 USD | 0.00 USD | 583.00 USD | `-47.99%` | `20.00` |
| `Live` | `Long` | `29.75` | 2,520,000.00 USD | 0.00 USD | 297,500.00 USD | `-46.91%` | `10,000.00` |
| `Live` | `Long` | `30.05` | 2,220,000.00 USD | 0.00 USD | 218.46 USD | `-46.38%` | `7.27` |
| `Live` | `Long` | `30.65` | 2,220,000.00 USD | 0.00 USD | 1,540.00 USD | `-45.31%` | `50.19` |
| `Live` | `Long` | `30.85` | 2,220,000.00 USD | 0.00 USD | 578.44 USD | `-44.95%` | `18.75` |
| `Live` | `Long` | `30.95` | 2,220,000.00 USD | 0.00 USD | 538.53 USD | `-44.77%` | `17.40` |
| `Live` | `Long` | `31.15` | 2,220,000.00 USD | 0.00 USD | 5,880.00 USD | `-44.42%` | `188.85` |
| `Live` | `Long` | `31.55` | 2,210,000.00 USD | 0.00 USD | 1,060.00 USD | `-43.70%` | `33.49` |
| `Live` | `Long` | `31.65` | 2,210,000.00 USD | 0.00 USD | 4,640.00 USD | `-43.52%` | `146.53` |
| `Live` | `Long` | `31.85` | 2,200,000.00 USD | 0.00 USD | 2,870.00 USD | `-43.17%` | `90.00` |
| `Live` | `Long` | `31.95` | 2,200,000.00 USD | 0.00 USD | 3,080.00 USD | `-42.99%` | `96.35` |
| `Live` | `Long` | `32.15` | 2,200,000.00 USD | 0.00 USD | 450.10 USD | `-42.63%` | `14.00` |
| `Live` | `Long` | `32.35` | 2,200,000.00 USD | 0.00 USD | 26,760.00 USD | `-42.28%` | `827.28` |
| `Live` | `Long` | `32.65` | 2,170,000.00 USD | 0.00 USD | 653.00 USD | `-41.74%` | `20.00` |
| `Live` | `Long` | `32.75` | 2,170,000.00 USD | 0.00 USD | 953.68 USD | `-41.56%` | `29.12` |
| `Live` | `Long` | `32.85` | 2,170,000.00 USD | 0.00 USD | 32,850.00 USD | `-41.38%` | `1,000.01` |
| `Live` | `Long` | `33.35` | 2,140,000.00 USD | 0.00 USD | 5,810.00 USD | `-40.49%` | `174.22` |
| `Live` | `Long` | `33.65` | 2,130,000.00 USD | 0.00 USD | 257.76 USD | `-39.96%` | `7.66` |
| `Live` | `Long` | `34.05` | 2,130,000.00 USD | 0.00 USD | 182.85 USD | `-39.24%` | `5.37` |
| `Live` | `Long` | `34.15` | 2,130,000.00 USD | 0.00 USD | 126.70 USD | `-39.06%` | `3.71` |
| `Live` | `Long` | `34.25` | 2,130,000.00 USD | 0.00 USD | 4,470.00 USD | `-38.89%` | `130.63` |
| `Live` | `Long` | `34.45` | 2,130,000.00 USD | 0.00 USD | 65,890.00 USD | `-38.53%` | `1,912.61` |
| `Live` | `Long` | `34.65` | 2,060,000.00 USD | 0.00 USD | 3,240.00 USD | `-38.17%` | `93.56` |
| `Live` | `Long` | `34.85` | 2,060,000.00 USD | 0.00 USD | 415.41 USD | `-37.81%` | `11.92` |
| `Live` | `Long` | `34.95` | 2,060,000.00 USD | 0.00 USD | 104.85 USD | `-37.64%` | `3.00` |
| `Live` | `Long` | `35.05` | 2,060,000.00 USD | 0.00 USD | 166.49 USD | `-37.46%` | `4.75` |
| `Live` | `Long` | `35.75` | 2,060,000.00 USD | 0.00 USD | 279.92 USD | `-36.21%` | `7.83` |
| `Live` | `Long` | `36.25` | 2,060,000.00 USD | 0.00 USD | 181.25 USD | `-35.32%` | `5.00` |
| `Live` | `Long` | `36.35` | 2,060,000.00 USD | 0.00 USD | 3,020.00 USD | `-35.14%` | `83.03` |
| `Live` | `Long` | `36.45` | 2,050,000.00 USD | 0.00 USD | 423.18 USD | `-34.96%` | `11.61` |
| `Live` | `Long` | `36.65` | 2,050,000.00 USD | 0.00 USD | 317.76 USD | `-34.60%` | `8.67` |
| `Live` | `Long` | `36.75` | 2,050,000.00 USD | 0.00 USD | 101.80 USD | `-34.42%` | `2.77` |
| `Live` | `Long` | `37.15` | 2,050,000.00 USD | 0.00 USD | 1,490.00 USD | `-33.71%` | `40.08` |
| `Live` | `Long` | `37.25` | 2,050,000.00 USD | 0.00 USD | 2,830.00 USD | `-33.53%` | `76.00` |
| `Live` | `Long` | `37.35` | 2,050,000.00 USD | 0.00 USD | 9,260.00 USD | `-33.35%` | `247.91` |
| `Live` | `Long` | `37.55` | 2,040,000.00 USD | 0.00 USD | 3,530.00 USD | `-33.00%` | `94.04` |
| `Live` | `Long` | `37.75` | 2,030,000.00 USD | 0.00 USD | 377.50 USD | `-32.64%` | `10.00` |
| `Live` | `Long` | `37.85` | 2,030,000.00 USD | 0.00 USD | 6,210.00 USD | `-32.46%` | `164.03` |
| `Live` | `Long` | `37.95` | 2,030,000.00 USD | 0.00 USD | 446.67 USD | `-32.28%` | `11.77` |
| `Live` | `Long` | `38.25` | 2,030,000.00 USD | 0.00 USD | 695.38 USD | `-31.75%` | `18.18` |
| `Live` | `Long` | `38.35` | 2,030,000.00 USD | 0.00 USD | 847.54 USD | `-31.57%` | `22.10` |
| `Live` | `Long` | `38.45` | 2,030,000.00 USD | 0.00 USD | 2,400.00 USD | `-31.39%` | `62.34` |
| `Live` | `Long` | `38.55` | 2,020,000.00 USD | 0.00 USD | 993.82 USD | `-31.21%` | `25.78` |
| `Live` | `Long` | `38.65` | 2,020,000.00 USD | 0.00 USD | 4,280.00 USD | `-31.03%` | `110.74` |
| `Live` | `Long` | `38.95` | 2,020,000.00 USD | 0.00 USD | 2,730.00 USD | `-30.50%` | `70.00` |
| `Live` | `Long` | `39.05` | 2,020,000.00 USD | 0.00 USD | 665,110.00 USD | `-30.32%` | `17,032.14` |
| `Live` | `Long` | `39.15` | 1,350,000.00 USD | 0.00 USD | 570.02 USD | `-30.14%` | `14.56` |
| `Live` | `Long` | `39.35` | 1,350,000.00 USD | 0.00 USD | 264.83 USD | `-29.78%` | `6.73` |
| `Live` | `Long` | `39.45` | 1,350,000.00 USD | 0.00 USD | 716.41 USD | `-29.61%` | `18.16` |
| `Live` | `Long` | `39.55` | 1,350,000.00 USD | 0.00 USD | 312.44 USD | `-29.43%` | `7.90` |
| `Live` | `Long` | `39.65` | 1,350,000.00 USD | 0.00 USD | 5,900.00 USD | `-29.25%` | `148.78` |
| `Live` | `Long` | `39.75` | 1,340,000.00 USD | 0.00 USD | 1,180.00 USD | `-29.07%` | `29.57` |
| `Live` | `Long` | `39.85` | 1,340,000.00 USD | 0.00 USD | 133.10 USD | `-28.89%` | `3.34` |
| `Live` | `Long` | `40.05` | 1,340,000.00 USD | 0.00 USD | 3,160.00 USD | `-28.54%` | `78.90` |
| `Live` | `Long` | `40.45` | 1,340,000.00 USD | 0.00 USD | 1,010.00 USD | `-27.82%` | `24.92` |
| `Live` | `Long` | `40.55` | 1,340,000.00 USD | 0.00 USD | 133.00 USD | `-27.64%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,340,000.00 USD | 0.00 USD | 274.39 USD | `-27.47%` | `6.75` |
| `Live` | `Long` | `40.75` | 1,340,000.00 USD | 0.00 USD | 8,960.00 USD | `-27.29%` | `220.00` |
| `Live` | `Long` | `40.85` | 1,330,000.00 USD | 0.00 USD | 6,340.00 USD | `-27.11%` | `155.23` |
| `Live` | `Long` | `40.95` | 1,320,000.00 USD | 0.00 USD | 509.01 USD | `-26.93%` | `12.43` |
| `Live` | `Long` | `41.05` | 1,320,000.00 USD | 0.00 USD | 396.54 USD | `-26.75%` | `9.66` |
| `Live` | `Long` | `41.25` | 1,320,000.00 USD | 0.00 USD | 19,930.00 USD | `-26.39%` | `483.20` |
| `Live` | `Long` | `41.45` | 1,300,000.00 USD | 0.00 USD | 644.96 USD | `-26.04%` | `15.56` |
| `Live` | `Long` | `42.05` | 1,300,000.00 USD | 0.00 USD | 982.29 USD | `-24.97%` | `23.36` |
| `Live` | `Long` | `42.15` | 1,300,000.00 USD | 0.00 USD | 66,300.00 USD | `-24.79%` | `1,572.94` |
| `Live` | `Long` | `42.25` | 1,230,000.00 USD | 0.00 USD | 35,410.00 USD | `-24.61%` | `838.00` |
| `Live` | `Long` | `42.35` | 1,200,000.00 USD | 0.00 USD | 301.96 USD | `-24.43%` | `7.13` |
| `Live` | `Long` | `42.55` | 1,200,000.00 USD | 0.00 USD | 3,380.00 USD | `-24.07%` | `79.49` |
| `Live` | `Long` | `42.65` | 1,190,000.00 USD | 0.00 USD | 1,890.00 USD | `-23.90%` | `44.20` |
| `Live` | `Long` | `42.75` | 1,190,000.00 USD | 0.00 USD | 46,620.00 USD | `-23.72%` | `1,090.60` |
| `Live` | `Long` | `42.85` | 1,140,000.00 USD | 0.00 USD | 11,320.00 USD | `-23.54%` | `264.09` |
| `Live` | `Long` | `42.95` | 1,130,000.00 USD | 0.00 USD | 2,000.00 USD | `-23.36%` | `46.65` |
| `Live` | `Long` | `43.05` | 1,130,000.00 USD | 0.00 USD | 9,080.00 USD | `-23.18%` | `211.00` |
| `Live` | `Long` | `43.15` | 1,120,000.00 USD | 0.00 USD | 122,400.00 USD | `-23.00%` | `2,836.59` |
| `Live` | `Long` | `43.25` | 1,000,000.00 USD | 0.00 USD | 417.80 USD | `-22.83%` | `9.66` |
| `Live` | `Long` | `43.35` | 999,760.00 USD | 0.00 USD | 5,390.00 USD | `-22.65%` | `124.24` |
| `Live` | `Long` | `43.45` | 994,370.00 USD | 0.00 USD | 980.67 USD | `-22.47%` | `22.57` |
| `Live` | `Long` | `43.65` | 993,390.00 USD | 0.00 USD | 426.02 USD | `-22.11%` | `9.76` |
| `Live` | `Long` | `43.75` | 992,970.00 USD | 0.00 USD | 21,880.00 USD | `-21.93%` | `500.00` |
| `Live` | `Long` | `43.85` | 971,090.00 USD | 0.00 USD | 801.14 USD | `-21.76%` | `18.27` |
| `Live` | `Long` | `44.15` | 970,290.00 USD | 0.00 USD | 2,380.00 USD | `-21.22%` | `53.99` |
| `Live` | `Long` | `44.35` | 967,910.00 USD | 0.00 USD | 84,440.00 USD | `-20.86%` | `1,903.87` |
| `Live` | `Long` | `44.45` | 883,470.00 USD | 0.00 USD | 1,330.00 USD | `-20.68%` | `30.00` |
| `Live` | `Long` | `44.55` | 882,140.00 USD | 0.00 USD | 842.44 USD | `-20.51%` | `18.91` |
| `Live` | `Long` | `44.75` | 881,300.00 USD | 0.00 USD | 4,230.00 USD | `-20.15%` | `94.55` |
| `Live` | `Long` | `44.85` | 877,060.00 USD | 0.00 USD | 1,480.00 USD | `-19.97%` | `33.00` |
| `Live` | `Long` | `44.95` | 875,580.00 USD | 0.00 USD | 2,620.00 USD | `-19.79%` | `58.18` |
| `Live` | `Long` | `45.05` | 872,970.00 USD | 0.00 USD | 4,830.00 USD | `-19.61%` | `107.31` |
| `Live` | `Long` | `45.15` | 868,140.00 USD | 0.00 USD | 8,710.00 USD | `-19.44%` | `193.00` |
| `Live` | `Long` | `45.25` | 859,420.00 USD | 0.00 USD | 3,180.00 USD | `-19.26%` | `70.37` |
| `Live` | `Long` | `45.35` | 856,240.00 USD | 0.00 USD | 2,180.00 USD | `-19.08%` | `48.02` |
| `Live` | `Long` | `45.45` | 854,060.00 USD | 0.00 USD | 23,940.00 USD | `-18.90%` | `526.65` |
| `Live` | `Long` | `45.55` | 830,120.00 USD | 0.00 USD | 12,060.00 USD | `-18.72%` | `264.81` |
| `Live` | `Long` | `45.65` | 818,060.00 USD | 0.00 USD | 42,180.00 USD | `-18.54%` | `924.03` |
| `Live` | `Long` | `45.75` | 775,880.00 USD | 0.00 USD | 27,480.00 USD | `-18.36%` | `600.68` |
| `Live` | `Long` | `45.95` | 748,400.00 USD | 0.00 USD | 2,940.00 USD | `-18.01%` | `64.09` |
| `Live` | `Long` | `46.05` | 745,450.00 USD | 0.00 USD | 706.41 USD | `-17.83%` | `15.34` |
| `Live` | `Long` | `46.15` | 744,750.00 USD | 0.00 USD | 177.22 USD | `-17.65%` | `3.84` |
| `Live` | `Long` | `46.25` | 744,570.00 USD | 0.00 USD | 842.21 USD | `-17.47%` | `18.21` |
| `Live` | `Long` | `46.35` | 743,730.00 USD | 0.00 USD | 22,820.00 USD | `-17.29%` | `492.25` |
| `Live` | `Long` | `46.55` | 720,910.00 USD | 0.00 USD | 2,140.00 USD | `-16.94%` | `45.93` |
| `Live` | `Long` | `46.65` | 718,770.00 USD | 0.00 USD | 3,980.00 USD | `-16.76%` | `85.41` |
| `Live` | `Long` | `46.85` | 714,790.00 USD | 0.00 USD | 358.40 USD | `-16.40%` | `7.65` |
| `Live` | `Long` | `46.95` | 714,430.00 USD | 0.00 USD | 158.22 USD | `-16.22%` | `3.37` |
| `Live` | `Long` | `47.05` | 714,270.00 USD | 0.00 USD | 271.01 USD | `-16.05%` | `5.76` |
| `Live` | `Long` | `47.15` | 714,000.00 USD | 0.00 USD | 1,980.00 USD | `-15.87%` | `42.07` |
| `Live` | `Long` | `47.25` | 712,020.00 USD | 0.00 USD | 1,220.00 USD | `-15.69%` | `25.84` |
| `Live` | `Long` | `47.35` | 710,800.00 USD | 0.00 USD | 43,340.00 USD | `-15.51%` | `915.41` |
| `Live` | `Long` | `47.45` | 667,450.00 USD | 0.00 USD | 2,590.00 USD | `-15.33%` | `54.54` |
| `Live` | `Long` | `47.55` | 664,860.00 USD | 0.00 USD | 4,450.00 USD | `-15.15%` | `93.69` |
| `Live` | `Long` | `47.75` | 660,410.00 USD | 0.00 USD | 47,750.00 USD | `-14.80%` | `1,000.00` |
| `Live` | `Long` | `48.05` | 612,660.00 USD | 0.00 USD | 9,250.00 USD | `-14.26%` | `192.51` |
| `Live` | `Long` | `48.15` | 603,410.00 USD | 0.00 USD | 1,690.00 USD | `-14.08%` | `35.03` |
| `Live` | `Long` | `48.25` | 601,720.00 USD | 0.00 USD | 110.49 USD | `-13.90%` | `2.29` |
| `Live` | `Long` | `48.55` | 601,610.00 USD | 0.00 USD | 4,440.00 USD | `-13.37%` | `91.49` |
| `Live` | `Long` | `48.65` | 597,170.00 USD | 0.00 USD | 273.90 USD | `-13.19%` | `5.63` |
| `Live` | `Long` | `48.75` | 596,900.00 USD | 0.00 USD | 333.94 USD | `-13.01%` | `6.85` |
| `Live` | `Long` | `48.95` | 596,560.00 USD | 0.00 USD | 252.58 USD | `-12.65%` | `5.16` |
| `Live` | `Long` | `49.05` | 596,310.00 USD | 0.00 USD | 1,580.00 USD | `-12.48%` | `32.25` |
| `Live` | `Long` | `49.15` | 594,730.00 USD | 0.00 USD | 5,740.00 USD | `-12.30%` | `116.83` |
| `Live` | `Long` | `49.35` | 588,990.00 USD | 0.00 USD | 5,230.00 USD | `-11.94%` | `105.97` |
| `Live` | `Long` | `49.45` | 583,760.00 USD | 0.00 USD | 419.34 USD | `-11.76%` | `8.48` |
| `Live` | `Long` | `49.55` | 583,340.00 USD | 0.00 USD | 18,010.00 USD | `-11.58%` | `363.57` |
| `Live` | `Long` | `49.65` | 565,320.00 USD | 0.00 USD | 73,260.00 USD | `-11.41%` | `1,475.52` |
| `Live` | `Long` | `49.75` | 492,060.00 USD | 0.00 USD | 1,580.00 USD | `-11.23%` | `31.67` |
| `Live` | `Long` | `49.85` | 490,490.00 USD | 0.00 USD | 19,180.00 USD | `-11.05%` | `384.69` |
| `Live` | `Long` | `49.95` | 471,310.00 USD | 0.00 USD | 19,920.00 USD | `-10.87%` | `398.70` |
| `Live` | `Long` | `50.05` | 451,390.00 USD | 0.00 USD | 1,820.00 USD | `-10.69%` | `36.43` |
| `Live` | `Long` | `50.25` | 449,570.00 USD | 0.00 USD | 102.51 USD | `-10.34%` | `2.04` |
| `Live` | `Long` | `50.35` | 449,470.00 USD | 0.00 USD | 1,140.00 USD | `-10.16%` | `22.67` |
| `Live` | `Long` | `50.45` | 448,330.00 USD | 0.00 USD | 4,720.00 USD | `-9.98%` | `93.64` |
| `Live` | `Long` | `50.55` | 443,600.00 USD | 0.00 USD | 84,100.00 USD | `-9.80%` | `1,663.61` |
| `Live` | `Long` | `50.75` | 359,510.00 USD | 0.00 USD | 9,050.00 USD | `-9.44%` | `178.28` |
| `Live` | `Long` | `50.95` | 350,460.00 USD | 0.00 USD | 431.55 USD | `-9.09%` | `8.47` |
| `Live` | `Long` | `51.15` | 350,030.00 USD | 0.00 USD | 219,370.00 USD | `-8.73%` | `4,288.79` |
| `Live` | `Long` | `51.25` | 130,660.00 USD | 0.00 USD | 202.44 USD | `-8.55%` | `3.95` |
| `Live` | `Long` | `51.35` | 130,450.00 USD | 0.00 USD | 453.93 USD | `-8.37%` | `8.84` |
| `Live` | `Long` | `51.45` | 130,000.00 USD | 0.00 USD | 27,210.00 USD | `-8.19%` | `528.81` |
| `Live` | `Long` | `51.55` | 102,790.00 USD | 0.00 USD | 551.07 USD | `-8.02%` | `10.69` |
| `Live` | `Long` | `51.65` | 102,240.00 USD | 0.00 USD | 9,100.00 USD | `-7.84%` | `176.09` |
| `Live` | `Long` | `51.75` | 93,150.00 USD | 0.00 USD | 6,480.00 USD | `-7.66%` | `125.17` |
| `Live` | `Long` | `51.85` | 86,670.00 USD | 0.00 USD | 13,680.00 USD | `-7.48%` | `263.89` |
| `Live` | `Long` | `51.95` | 72,990.00 USD | 0.00 USD | 16,800.00 USD | `-7.30%` | `323.48` |
| `Live` | `Long` | `52.15` | 56,180.00 USD | 0.00 USD | 1,900.00 USD | `-6.94%` | `36.36` |
| `Live` | `Long` | `52.25` | 54,290.00 USD | 0.00 USD | 4,930.00 USD | `-6.77%` | `94.33` |
| `Live` | `Long` | `52.35` | 49,360.00 USD | 0.00 USD | 134.02 USD | `-6.59%` | `2.56` |
| `Live` | `Long` | `52.45` | 49,220.00 USD | 0.00 USD | 2,360.00 USD | `-6.41%` | `44.95` |
| `Live` | `Long` | `52.55` | 46,870.00 USD | 0.00 USD | 8,700.00 USD | `-6.23%` | `165.49` |
| `Live` | `Long` | `52.75` | 38,170.00 USD | 0.00 USD | 4,240.00 USD | `-5.87%` | `80.44` |
| `Live` | `Long` | `52.85` | 33,930.00 USD | 0.00 USD | 5,950.00 USD | `-5.70%` | `112.64` |
| `Live` | `Long` | `52.95` | 27,970.00 USD | 0.00 USD | 25,840.00 USD | `-5.52%` | `488.06` |
| `Live` | `Long` | `53.15` | 2,130.00 USD | 0.00 USD | 1,720.00 USD | `-5.16%` | `32.44` |
| `Live` | `Long` | `53.25` | 405.76 USD | 0.00 USD | 405.76 USD | `-4.98%` | `7.62` |
| `Live` | `Short` | `57.75` | 155.35 USD | 155.35 USD | 0.00 USD | `+3.05%` | `2.69` |
| `Live` | `Short` | `57.95` | 281.10 USD | 125.75 USD | 0.00 USD | `+3.40%` | `2.17` |
| `Live` | `Short` | `59.35` | 9,720.00 USD | 9,440.00 USD | 0.00 USD | `+5.90%` | `159.09` |
| `Live` | `Short` | `60.15` | 218,600.00 USD | 208,880.00 USD | 0.00 USD | `+7.33%` | `3,472.67` |
| `Live` | `Short` | `60.95` | 219,000.00 USD | 397.39 USD | 0.00 USD | `+8.76%` | `6.52` |
| `Live` | `Short` | `61.15` | 222,870.00 USD | 3,870.00 USD | 0.00 USD | `+9.11%` | `63.26` |
| `Live` | `Short` | `62.95` | 223,010.00 USD | 138.49 USD | 0.00 USD | `+12.33%` | `2.20` |
| `Live` | `Short` | `63.45` | 226,360.00 USD | 3,350.00 USD | 0.00 USD | `+13.22%` | `52.83` |
| `Live` | `Short` | `66.15` | 233,110.00 USD | 6,750.00 USD | 0.00 USD | `+18.04%` | `102.07` |
| `Live` | `Short` | `66.95` | 233,230.00 USD | 121.18 USD | 0.00 USD | `+19.46%` | `1.81` |
| `Live` | `Short` | `67.85` | 233,940.00 USD | 709.03 USD | 0.00 USD | `+21.07%` | `10.45` |
| `Live` | `Short` | `69.95` | 274,380.00 USD | 40,440.00 USD | 0.00 USD | `+24.82%` | `578.10` |
| `Live` | `Short` | `76.35` | 282,760.00 USD | 8,380.00 USD | 0.00 USD | `+36.24%` | `109.80` |
| `Live` | `Short` | `77.75` | 861,230.00 USD | 578,460.00 USD | 0.00 USD | `+38.74%` | `7,440.05` |
| `Live` | `Short` | `77.85` | 861,830.00 USD | 602.56 USD | 0.00 USD | `+38.91%` | `7.74` |
| `Live` | `Short` | `77.95` | 861,970.00 USD | 136.41 USD | 0.00 USD | `+39.09%` | `1.75` |
| `Live` | `Short` | `80.75` | 862,610.00 USD | 646.00 USD | 0.00 USD | `+44.09%` | `8.00` |
| `Live` | `Short` | `81.05` | 881,610.00 USD | 19,000.00 USD | 0.00 USD | `+44.62%` | `234.42` |
| `Live` | `Short` | `81.55` | 881,740.00 USD | 123.96 USD | 0.00 USD | `+45.52%` | `1.52` |
| `Live` | `Short` | `81.75` | 884,430.00 USD | 2,700.00 USD | 0.00 USD | `+45.87%` | `33.00` |
| `Live` | `Short` | `82.75` | 887,960.00 USD | 3,520.00 USD | 0.00 USD | `+47.66%` | `42.59` |
| `Live` | `Short` | `83.95` | 888,720.00 USD | 761.43 USD | 0.00 USD | `+49.80%` | `9.07` |
| `Live` | `Short` | `87.95` | 912,190.00 USD | 23,470.00 USD | 0.00 USD | `+56.94%` | `266.81` |
| `Live` | `Short` | `89.85` | 913,140.00 USD | 955.11 USD | 0.00 USD | `+60.33%` | `10.63` |
| `Live` | `Short` | `89.95` | 913,260.00 USD | 118.73 USD | 0.00 USD | `+60.50%` | `1.32` |
| `Live` | `Short` | `92.05` | 913,420.00 USD | 155.56 USD | 0.00 USD | `+64.25%` | `1.69` |
| `Live` | `Short` | `98.65` | 915,880.00 USD | 2,470.00 USD | 0.00 USD | `+76.03%` | `25.00` |
| `Live` | `Short` | `103.95` | 947,070.00 USD | 31,180.00 USD | 0.00 USD | `+85.49%` | `300.00` |
| `Live` | `Short` | `104.25` | 947,280.00 USD | 213.71 USD | 0.00 USD | `+86.02%` | `2.05` |
| `Live` | `Short` | `104.85` | 949,600.00 USD | 2,320.00 USD | 0.00 USD | `+87.09%` | `22.13` |
| `Live` | `Short` | `105.25` | 1,300,000.00 USD | 355,110.00 USD | 0.00 USD | `+87.81%` | `3,374.01` |
| `Live` | `Short` | `106.75` | 1,310,000.00 USD | 1,620.00 USD | 0.00 USD | `+90.48%` | `15.16` |
| `Live` | `Short` | `106.85` | 1,310,000.00 USD | 1,860.00 USD | 0.00 USD | `+90.66%` | `17.43` |
| `Live` | `Short` | `107.15` | 1,310,000.00 USD | 199.30 USD | 0.00 USD | `+91.20%` | `1.86` |
| `Live` | `Short` | `108.05` | 1,310,000.00 USD | 6,470.00 USD | 0.00 USD | `+92.80%` | `59.91` |
| `Live` | `Short` | `110.95` | 1,320,000.00 USD | 664.59 USD | 0.00 USD | `+97.98%` | `5.99` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 811,990.00 USD | 0.00 USD | 392.18 USD | `-64.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 811,590.00 USD | 0.00 USD | 2,310.00 USD | `-60.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 809,290.00 USD | 0.00 USD | 806.86 USD | `-55.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 808,480.00 USD | 0.00 USD | 1,560.00 USD | `-54.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 806,920.00 USD | 0.00 USD | 410.25 USD | `-51.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 806,510.00 USD | 0.00 USD | 281.57 USD | `-46.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 806,230.00 USD | 0.00 USD | 36,050.00 USD | `-35.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 770,180.00 USD | 0.00 USD | 37,550.00 USD | `-33.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 732,630.00 USD | 0.00 USD | 447.01 USD | `-32.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.35` | 732,180.00 USD | 0.00 USD | 73,350.00 USD | `-31.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 658,840.00 USD | 0.00 USD | 40,560.00 USD | `-30.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 618,280.00 USD | 0.00 USD | 489.57 USD | `-29.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 617,790.00 USD | 0.00 USD | 1,180.00 USD | `-28.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 616,610.00 USD | 0.00 USD | 9,840.00 USD | `-28.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 606,770.00 USD | 0.00 USD | 2,060.00 USD | `-26.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.05` | 604,720.00 USD | 0.00 USD | 2,060.00 USD | `-26.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 602,650.00 USD | 0.00 USD | 2,960.00 USD | `-25.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 599,700.00 USD | 0.00 USD | 4,010.00 USD | `-24.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.65` | 595,680.00 USD | 0.00 USD | 3,000.00 USD | `-23.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 592,680.00 USD | 0.00 USD | 5,680.00 USD | `-23.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 587,000.00 USD | 0.00 USD | 672.22 USD | `-21.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.35` | 586,330.00 USD | 0.00 USD | 329,970.00 USD | `-20.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 256,360.00 USD | 0.00 USD | 213.80 USD | `-20.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 256,150.00 USD | 0.00 USD | 223.20 USD | `-20.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 255,930.00 USD | 0.00 USD | 391.13 USD | `-20.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 255,540.00 USD | 0.00 USD | 7,080.00 USD | `-19.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 248,460.00 USD | 0.00 USD | 1,370.00 USD | `-18.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 247,090.00 USD | 0.00 USD | 553.80 USD | `-17.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.35` | 246,540.00 USD | 0.00 USD | 2,970.00 USD | `-17.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.45` | 243,570.00 USD | 0.00 USD | 3,080.00 USD | `-17.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 240,490.00 USD | 0.00 USD | 14,000.00 USD | `-16.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 226,490.00 USD | 0.00 USD | 158.56 USD | `-16.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 226,340.00 USD | 0.00 USD | 373.28 USD | `-15.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 225,960.00 USD | 0.00 USD | 849.46 USD | `-15.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 225,110.00 USD | 0.00 USD | 1,150.00 USD | `-14.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 223,960.00 USD | 0.00 USD | 129.25 USD | `-14.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.15` | 223,830.00 USD | 0.00 USD | 303.35 USD | `-14.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 223,530.00 USD | 0.00 USD | 1,740.00 USD | `-12.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 221,790.00 USD | 0.00 USD | 981.00 USD | `-12.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.35` | 220,810.00 USD | 0.00 USD | 817.24 USD | `-11.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 219,990.00 USD | 0.00 USD | 237.85 USD | `-11.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.55` | 219,750.00 USD | 0.00 USD | 1,420.00 USD | `-11.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.85` | 218,340.00 USD | 0.00 USD | 108.17 USD | `-11.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 218,230.00 USD | 0.00 USD | 298.20 USD | `-10.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 217,930.00 USD | 0.00 USD | 34,670.00 USD | `-10.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 183,260.00 USD | 0.00 USD | 6,410.00 USD | `-10.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 176,840.00 USD | 0.00 USD | 459.70 USD | `-10.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 176,380.00 USD | 0.00 USD | 236.57 USD | `-9.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 176,150.00 USD | 0.00 USD | 1,020.00 USD | `-8.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 175,130.00 USD | 0.00 USD | 439.89 USD | `-8.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.45` | 174,690.00 USD | 0.00 USD | 204.26 USD | `-8.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 174,480.00 USD | 0.00 USD | 10,190.00 USD | `-7.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.85` | 164,290.00 USD | 0.00 USD | 106.29 USD | `-7.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.95` | 164,190.00 USD | 0.00 USD | 8,700.00 USD | `-7.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 155,490.00 USD | 0.00 USD | 26,490.00 USD | `-7.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.25` | 129,000.00 USD | 0.00 USD | 140.03 USD | `-6.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 128,860.00 USD | 0.00 USD | 70,190.00 USD | `-6.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 58,670.00 USD | 0.00 USD | 5,460.00 USD | `-6.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 53,210.00 USD | 0.00 USD | 271.13 USD | `-5.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.85` | 52,940.00 USD | 0.00 USD | 2,840.00 USD | `-5.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 50,090.00 USD | 0.00 USD | 115.43 USD | `-5.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 49,980.00 USD | 0.00 USD | 9,240.00 USD | `-5.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 40,740.00 USD | 0.00 USD | 2,660.00 USD | `-5.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.25` | 38,080.00 USD | 0.00 USD | 881.82 USD | `-4.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 37,200.00 USD | 0.00 USD | 566.57 USD | `-4.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 36,630.00 USD | 0.00 USD | 5,950.00 USD | `-4.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 30,680.00 USD | 0.00 USD | 1,370.00 USD | `-4.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.75` | 29,310.00 USD | 0.00 USD | 1,120.00 USD | `-4.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 28,190.00 USD | 0.00 USD | 462.03 USD | `-3.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 27,730.00 USD | 0.00 USD | 895.07 USD | `-3.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.15` | 26,830.00 USD | 0.00 USD | 398.54 USD | `-3.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 26,430.00 USD | 0.00 USD | 3,090.00 USD | `-3.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 23,340.00 USD | 0.00 USD | 156.53 USD | `-3.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.45` | 23,190.00 USD | 0.00 USD | 144.29 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.55` | 23,040.00 USD | 0.00 USD | 1,690.00 USD | `-2.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.65` | 21,350.00 USD | 0.00 USD | 14,570.00 USD | `-2.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.75` | 6,780.00 USD | 0.00 USD | 198.74 USD | `-2.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 6,590.00 USD | 0.00 USD | 398.21 USD | `-2.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.95` | 6,190.00 USD | 0.00 USD | 397.84 USD | `-1.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 5,790.00 USD | 0.00 USD | 160.75 USD | `-1.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.15` | 5,630.00 USD | 0.00 USD | 101.48 USD | `-1.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.25` | 5,530.00 USD | 0.00 USD | 398.90 USD | `-1.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.35` | 5,130.00 USD | 0.00 USD | 407.38 USD | `-1.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.45` | 4,720.00 USD | 0.00 USD | 408.11 USD | `-1.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.55` | 4,310.00 USD | 0.00 USD | 156.65 USD | `-0.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.65` | 4,160.00 USD | 0.00 USD | 3,610.00 USD | `-0.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.75` | 545.08 USD | 0.00 USD | 202.37 USD | `-0.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.85` | 342.71 USD | 0.00 USD | 149.68 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.95` | 193.03 USD | 0.00 USD | 193.03 USD | `-0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.05` | 632.24 USD | 632.24 USD | 0.00 USD | `+0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.15` | 829.89 USD | 197.65 USD | 0.00 USD | `+0.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.25` | 1,030.00 USD | 204.19 USD | 0.00 USD | `+0.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.35` | 1,420.00 USD | 387.12 USD | 0.00 USD | `+0.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.45` | 1,830.00 USD | 407.57 USD | 0.00 USD | `+0.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.55` | 4,470.00 USD | 2,640.00 USD | 0.00 USD | `+0.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.65` | 4,590.00 USD | 121.23 USD | 0.00 USD | `+1.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.75` | 4,690.00 USD | 104.42 USD | 0.00 USD | `+1.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.85` | 22,720.00 USD | 18,030.00 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.95` | 23,110.00 USD | 390.68 USD | 0.00 USD | `+1.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.15` | 23,500.00 USD | 392.05 USD | 0.00 USD | `+1.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.25` | 23,700.00 USD | 201.52 USD | 0.00 USD | `+2.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.35` | 23,910.00 USD | 207.03 USD | 0.00 USD | `+2.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.45` | 24,260.00 USD | 344.70 USD | 0.00 USD | `+2.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.55` | 44,620.00 USD | 20,360.00 USD | 0.00 USD | `+2.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.65` | 44,730.00 USD | 118.18 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.75` | 44,850.00 USD | 119.54 USD | 0.00 USD | `+3.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 45,600.00 USD | 747.68 USD | 0.00 USD | `+3.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 45,800.00 USD | 200.04 USD | 0.00 USD | `+3.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 46,000.00 USD | 200.96 USD | 0.00 USD | `+3.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 46,130.00 USD | 123.70 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 46,730.00 USD | 601.45 USD | 0.00 USD | `+4.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 47,340.00 USD | 611.85 USD | 0.00 USD | `+4.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.65` | 47,610.00 USD | 274.48 USD | 0.00 USD | `+4.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 48,100.00 USD | 491.15 USD | 0.00 USD | `+4.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 51,050.00 USD | 2,940.00 USD | 0.00 USD | `+5.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 51,180.00 USD | 129.69 USD | 0.00 USD | `+5.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 55,980.00 USD | 4,800.00 USD | 0.00 USD | `+5.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 57,260.00 USD | 1,280.00 USD | 0.00 USD | `+5.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.25` | 57,470.00 USD | 210.34 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 57,930.00 USD | 461.74 USD | 0.00 USD | `+5.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 58,090.00 USD | 159.92 USD | 0.00 USD | `+6.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.55` | 58,580.00 USD | 496.65 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 59,310.00 USD | 724.75 USD | 0.00 USD | `+6.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 59,470.00 USD | 158.00 USD | 0.00 USD | `+6.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 59,640.00 USD | 171.14 USD | 0.00 USD | `+7.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 60,190.00 USD | 551.00 USD | 0.00 USD | `+7.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.45` | 60,340.00 USD | 155.36 USD | 0.00 USD | `+7.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 61,220.00 USD | 878.58 USD | 0.00 USD | `+8.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 62,610.00 USD | 1,390.00 USD | 0.00 USD | `+8.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 63,600.00 USD | 986.99 USD | 0.00 USD | `+8.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 64,270.00 USD | 674.72 USD | 0.00 USD | `+8.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 66,630.00 USD | 2,360.00 USD | 0.00 USD | `+9.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 66,760.00 USD | 125.56 USD | 0.00 USD | `+9.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 70,360.00 USD | 3,600.00 USD | 0.00 USD | `+9.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 71,000.00 USD | 643.20 USD | 0.00 USD | `+9.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 71,130.00 USD | 130.31 USD | 0.00 USD | `+10.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 71,850.00 USD | 716.72 USD | 0.00 USD | `+11.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 72,080.00 USD | 231.39 USD | 0.00 USD | `+12.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 72,710.00 USD | 630.87 USD | 0.00 USD | `+12.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 73,410.00 USD | 703.97 USD | 0.00 USD | `+12.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 74,080.00 USD | 668.13 USD | 0.00 USD | `+13.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 82,810.00 USD | 8,730.00 USD | 0.00 USD | `+13.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 83,370.00 USD | 555.03 USD | 0.00 USD | `+13.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 83,900.00 USD | 531.62 USD | 0.00 USD | `+14.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.35` | 84,560.00 USD | 664.09 USD | 0.00 USD | `+14.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.45` | 85,230.00 USD | 665.12 USD | 0.00 USD | `+15.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 85,430.00 USD | 202.69 USD | 0.00 USD | `+15.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 85,730.00 USD | 298.04 USD | 0.00 USD | `+15.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 85,830.00 USD | 102.13 USD | 0.00 USD | `+16.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 86,370.00 USD | 540.09 USD | 0.00 USD | `+16.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 86,470.00 USD | 100.79 USD | 0.00 USD | `+16.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 86,730.00 USD | 262.20 USD | 0.00 USD | `+16.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 87,100.00 USD | 371.49 USD | 0.00 USD | `+17.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 87,800.00 USD | 696.17 USD | 0.00 USD | `+17.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 88,330.00 USD | 534.00 USD | 0.00 USD | `+19.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 99,410.00 USD | 11,080.00 USD | 0.00 USD | `+19.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 106,120.00 USD | 6,710.00 USD | 0.00 USD | `+19.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.05` | 108,480.00 USD | 2,360.00 USD | 0.00 USD | `+21.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 113,340.00 USD | 4,860.00 USD | 0.00 USD | `+21.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 113,550.00 USD | 204.48 USD | 0.00 USD | `+24.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.65` | 631,750.00 USD | 518,200.00 USD | 0.00 USD | `+24.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 632,560.00 USD | 810.02 USD | 0.00 USD | `+24.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 952,450.00 USD | 319,890.00 USD | 0.00 USD | `+25.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 952,620.00 USD | 170.04 USD | 0.00 USD | `+26.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 958,390.00 USD | 5,770.00 USD | 0.00 USD | `+26.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 958,660.00 USD | 269.28 USD | 0.00 USD | `+26.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 958,950.00 USD | 291.40 USD | 0.00 USD | `+28.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 966,160.00 USD | 7,220.00 USD | 0.00 USD | `+28.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 966,320.00 USD | 156.78 USD | 0.00 USD | `+28.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 969,540.00 USD | 3,220.00 USD | 0.00 USD | `+29.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 969,950.00 USD | 411.14 USD | 0.00 USD | `+31.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 1,090,000.00 USD | 123,190.00 USD | 0.00 USD | `+32.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 1,090,000.00 USD | 1,020.00 USD | 0.00 USD | `+33.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.75` | 1,090,000.00 USD | 811.04 USD | 0.00 USD | `+33.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 1,100,000.00 USD | 104.93 USD | 0.00 USD | `+33.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 1,100,000.00 USD | 133.59 USD | 0.00 USD | `+33.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 1,100,000.00 USD | 402.59 USD | 0.00 USD | `+34.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.85` | 1,100,000.00 USD | 308.71 USD | 0.00 USD | `+35.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 1,100,000.00 USD | 315.18 USD | 0.00 USD | `+37.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 1,160,000.00 USD | 59,310.00 USD | 0.00 USD | `+40.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 1,160,000.00 USD | 3,160.00 USD | 0.00 USD | `+41.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.35` | 1,160,000.00 USD | 5,260.00 USD | 0.00 USD | `+41.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 1,170,000.00 USD | 5,690.00 USD | 0.00 USD | `+42.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 1,210,000.00 USD | 36,590.00 USD | 0.00 USD | `+42.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 1,210,000.00 USD | 433.89 USD | 0.00 USD | `+44.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 1,210,000.00 USD | 172.64 USD | 0.00 USD | `+44.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 1,210,000.00 USD | 164.10 USD | 0.00 USD | `+46.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 1,210,000.00 USD | 546.81 USD | 0.00 USD | `+47.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 1,210,000.00 USD | 2,300.00 USD | 0.00 USD | `+49.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 1,220,000.00 USD | 12,070.00 USD | 0.00 USD | `+51.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.05` | 1,240,000.00 USD | 20,230.00 USD | 0.00 USD | `+55.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 1,240,000.00 USD | 1,580.00 USD | 0.00 USD | `+56.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 1,280,000.00 USD | 37,000.00 USD | 0.00 USD | `+57.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 1,280,000.00 USD | 473.21 USD | 0.00 USD | `+58.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 1,280,000.00 USD | 422.99 USD | 0.00 USD | `+58.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 1,280,000.00 USD | 1,630.00 USD | 0.00 USD | `+59.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 1,290,000.00 USD | 4,870.00 USD | 0.00 USD | `+60.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 1,290,000.00 USD | 481.55 USD | 0.00 USD | `+63.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 1,290,000.00 USD | 1,330.00 USD | 0.00 USD | `+64.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 1,290,000.00 USD | 188.10 USD | 0.00 USD | `+67.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,560,000.00 USD | 266,140.00 USD | 0.00 USD | `+69.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,560,000.00 USD | 3,400.00 USD | 0.00 USD | `+70.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,580,000.00 USD | 21,930.00 USD | 0.00 USD | `+71.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,580,000.00 USD | 294.15 USD | 0.00 USD | `+74.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 1,600,000.00 USD | 15,380.00 USD | 0.00 USD | `+76.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,600,000.00 USD | 3,660.00 USD | 0.00 USD | `+78.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,600,000.00 USD | 306.15 USD | 0.00 USD | `+82.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,600,000.00 USD | 936.72 USD | 0.00 USD | `+83.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,610,000.00 USD | 2,920.00 USD | 0.00 USD | `+84.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,610,000.00 USD | 324.15 USD | 0.00 USD | `+92.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 1,610,000.00 USD | 123.23 USD | 0.00 USD | `+94.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 1,690,000.00 USD | 89,110.00 USD | 0.00 USD | `+98.15%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `47.10` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 28,250.00 USD | 12,890.00 USD | 9,220.00 USD |
| `7D` | `47.20` | 8,280,000.00 USD | 0.00 USD | 8,280,000.00 USD | 12,340.00 USD | 3,420.00 USD | 4,930.00 USD |
| `7D` | `47.30` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 692.33 USD | 4,740.00 USD | 6,740.00 USD |
| `7D` | `47.40` | 8,250,000.00 USD | 0.00 USD | 8,250,000.00 USD | 0.00 USD | 1,520.00 USD | 28,650.00 USD |
| `7D` | `47.50` | 8,220,000.00 USD | 0.00 USD | 8,220,000.00 USD | 11,830.00 USD | 0.00 USD | 7,960.00 USD |
| `7D` | `48.10` | 8,200,000.00 USD | 0.00 USD | 8,200,000.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD |
| `7D` | `48.20` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD |
| `7D` | `48.40` | 8,180,000.00 USD | 0.00 USD | 8,180,000.00 USD | 0.00 USD | 6,080.00 USD | 0.00 USD |
| `7D` | `48.60` | 8,180,000.00 USD | 0.00 USD | 8,180,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `48.80` | 8,180,000.00 USD | 0.00 USD | 8,180,000.00 USD | 1,780.00 USD | 2,250.00 USD | 0.00 USD |
| `7D` | `48.90` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 0.00 USD | 0.00 USD | 960.40 USD |
| `7D` | `49.30` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 15,190.00 USD | 4,490.00 USD | 14,870.00 USD |
| `7D` | `49.40` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD |
| `7D` | `49.50` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 2,830.00 USD | 7,770.00 USD | 0.00 USD |
| `1D` | `49.60` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 6,740.00 USD | 13,640.00 USD | 16,210.00 USD |
| `7D` | `49.60` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD |
| `1D` | `49.70` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 10,180.00 USD | 2,280.00 USD | 2,990.00 USD |
| `7D` | `49.70` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 12,090.00 USD | 0.00 USD | 5,410.00 USD |
| `1D` | `49.80` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 6,420.00 USD | 4,300.00 USD | 21,850.00 USD |
| `7D` | `49.80` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 9,930.00 USD | 8,220.00 USD | 0.00 USD |
| `1D` | `49.90` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 20,400.00 USD | 8,690.00 USD | 22,850.00 USD |
| `7D` | `49.90` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 45,030.00 USD | 7,170.00 USD | 4,700.00 USD |
| `1D` | `50.00` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 7,670.00 USD | 6,270.00 USD | 40,560.00 USD |
| `7D` | `50.00` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 22,100.00 USD | 7,630.00 USD | 24,920.00 USD |
| `1D` | `50.10` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 3,780.00 USD | 3,330.00 USD | 0.00 USD |
| `7D` | `50.10` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 363.50 USD | 682.90 USD | 8,340.00 USD |
| `1D` | `50.20` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 177.10 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `50.20` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 6,960.00 USD | 500.40 USD | 34,680.00 USD |
| `1D` | `50.30` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 171.03 USD | 333.03 USD | 2,340.00 USD |
| `7D` | `50.30` | 7,900,000.00 USD | 0.00 USD | 7,900,000.00 USD | 16,270.00 USD | 3,640.00 USD | 1,950.00 USD |
| `1D` | `50.40` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 4,370.00 USD | 2,740.00 USD | 0.00 USD |
| `7D` | `50.40` | 7,880,000.00 USD | 0.00 USD | 7,880,000.00 USD | 28,280.00 USD | 19,110.00 USD | 33,450.00 USD |
| `1D` | `50.50` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 5,790.00 USD | 1,010.00 USD | 0.00 USD |
| `7D` | `50.50` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 24,840.00 USD | 6,790.00 USD | 43,710.00 USD |
| `1D` | `50.60` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 1,660.00 USD | 1,750.00 USD | 5,610.00 USD |
| `7D` | `50.60` | 7,730,000.00 USD | 0.00 USD | 7,730,000.00 USD | 56,670.00 USD | 17,830.00 USD | 22,250.00 USD |
| `1D` | `50.70` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 2,530.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `50.70` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 53,670.00 USD | 24,710.00 USD | 32,520.00 USD |
| `1D` | `50.80` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 5,630.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `50.80` | 7,520,000.00 USD | 0.00 USD | 7,520,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD |
| `1D` | `50.90` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 826.24 USD | 260.05 USD | 8,390.00 USD |
| `7D` | `50.90` | 7,420,000.00 USD | 0.00 USD | 7,420,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD |
| `1D` | `51.00` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 5,040.00 USD | 0.00 USD | 430.77 USD |
| `7D` | `51.00` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `51.10` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 9,210.00 USD | 6,560.00 USD | 0.00 USD |
| `7D` | `51.10` | 7,040,000.00 USD | 0.00 USD | 7,040,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD |
| `1D` | `51.20` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 2,360.00 USD | 1,130.00 USD | 17,310.00 USD |
| `7D` | `51.20` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD |
| `1D` | `51.30` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 16,790.00 USD | 14,100.00 USD | 10,670.00 USD |
| `7D` | `51.30` | 6,900,000.00 USD | 0.00 USD | 6,900,000.00 USD | 28,400.00 USD | 26,720.00 USD | 47,090.00 USD |
| `1D` | `51.40` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 13,750.00 USD | 11,490.00 USD | 4,890.00 USD |
| `7D` | `51.40` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 73,130.00 USD | 42,820.00 USD | 46,140.00 USD |
| `1D` | `51.50` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 7,880.00 USD | 10,980.00 USD | 37,710.00 USD |
| `7D` | `51.50` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 38,520.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `51.60` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 9,060.00 USD | 18,490.00 USD | 757.87 USD |
| `7D` | `51.60` | 6,530,000.00 USD | 0.00 USD | 6,530,000.00 USD | 37,880.00 USD | 36,790.00 USD | 41,490.00 USD |
| `1D` | `51.70` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 2,890.00 USD | 13,810.00 USD | 21,320.00 USD |
| `7D` | `51.70` | 6,420,000.00 USD | 0.00 USD | 6,420,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `51.80` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 12,590.00 USD | 19,270.00 USD | 14,170.00 USD |
| `7D` | `51.80` | 6,380,000.00 USD | 0.00 USD | 6,380,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD |
| `1D` | `51.90` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 9,460.00 USD | 27,280.00 USD | 23,480.00 USD |
| `7D` | `51.90` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 5,870.00 USD | 25,410.00 USD | 28,190.00 USD |
| `1D` | `52.00` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 25,510.00 USD | 25,740.00 USD | 28,120.00 USD |
| `7D` | `52.00` | 6,260,000.00 USD | 0.00 USD | 6,260,000.00 USD | 64,300.00 USD | 26,440.00 USD | 11,880.00 USD |
| `1D` | `52.10` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 51,300.00 USD | 19,850.00 USD | 52,320.00 USD |
| `7D` | `52.10` | 6,160,000.00 USD | 0.00 USD | 6,160,000.00 USD | 24,220.00 USD | 28,090.00 USD | 37,880.00 USD |
| `1D` | `52.20` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 15,450.00 USD | 8,060.00 USD | 46,100.00 USD |
| `7D` | `52.20` | 6,070,000.00 USD | 0.00 USD | 6,070,000.00 USD | 38,380.00 USD | 13,960.00 USD | 25,270.00 USD |
| `1D` | `52.30` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 31,960.00 USD | 21,640.00 USD | 12,670.00 USD |
| `7D` | `52.30` | 5,990,000.00 USD | 0.00 USD | 5,990,000.00 USD | 24,840.00 USD | 41,300.00 USD | 8,940.00 USD |
| `1D` | `52.40` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 12,460.00 USD | 17,080.00 USD | 7,040.00 USD |
| `7D` | `52.40` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 20,580.00 USD | 38,950.00 USD | 22,030.00 USD |
| `1D` | `52.50` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 53,350.00 USD | 29,580.00 USD | 74,280.00 USD |
| `7D` | `52.50` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 38,720.00 USD | 667.05 USD | 11,240.00 USD |
| `1D` | `52.60` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 8,330.00 USD | 40,700.00 USD | 717.10 USD |
| `7D` | `52.60` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 74,610.00 USD | 32,590.00 USD | 59,410.00 USD |
| `1D` | `52.70` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 16,690.00 USD | 19,440.00 USD | 28,640.00 USD |
| `7D` | `52.70` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 20,250.00 USD | 92,920.00 USD | 108,640.00 USD |
| `1D` | `52.80` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 27,090.00 USD | 50,290.00 USD | 102,590.00 USD |
| `7D` | `52.80` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 46,600.00 USD | 35,280.00 USD | 0.00 USD |
| `1D` | `52.90` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 43,760.00 USD | 50,040.00 USD | 26,190.00 USD |
| `7D` | `52.90` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 51,920.00 USD | 28,710.00 USD | 34,400.00 USD |
| `1D` | `53.00` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 26,670.00 USD | 30,500.00 USD | 39,600.00 USD |
| `7D` | `53.00` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 47,240.00 USD | 25,810.00 USD | 89,050.00 USD |
| `1D` | `53.10` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 14,570.00 USD | 42,760.00 USD | 87,010.00 USD |
| `7D` | `53.10` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 52,120.00 USD | 17,950.00 USD | 9,630.00 USD |
| `1D` | `53.20` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 24,240.00 USD | 6,510.00 USD | 41,660.00 USD |
| `7D` | `53.20` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 162,460.00 USD | 28,320.00 USD | 23,350.00 USD |
| `1D` | `53.30` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 3,650.00 USD | 0.00 USD | 5,610.00 USD |
| `7D` | `53.30` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 57,250.00 USD | 24,540.00 USD | 34,820.00 USD |
| `1D` | `53.40` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 3,460.00 USD | 1,850.00 USD | 657.14 USD |
| `7D` | `53.40` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 44,030.00 USD | 7,250.00 USD | 91,220.00 USD |
| `1D` | `53.50` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 9,110.00 USD | 3,940.00 USD | 2,990.00 USD |
| `7D` | `53.50` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 48,660.00 USD | 3,440.00 USD | 20,840.00 USD |
| `1D` | `53.60` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 72,650.00 USD | 220.65 USD | 13,180.00 USD |
| `7D` | `53.60` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 52,800.00 USD | 1,980.00 USD | 0.00 USD |
| `1D` | `53.70` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 6,210.00 USD | 0.00 USD | 5,840.00 USD |
| `7D` | `53.70` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 131,400.00 USD | 3,480.00 USD | 0.00 USD |
| `1D` | `53.80` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 44,920.00 USD | 1,750.00 USD | 168.97 USD |
| `7D` | `53.80` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 99,150.00 USD | 13,850.00 USD | 0.00 USD |
| `1D` | `53.90` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 42,200.00 USD | 15,000.00 USD | 281.90 USD |
| `7D` | `53.90` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 129,920.00 USD | 21,360.00 USD | 0.00 USD |
| `1D` | `54.00` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 31,050.00 USD | 7,680.00 USD | 27,340.00 USD |
| `7D` | `54.00` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 324,350.00 USD | 42,300.00 USD | 220,540.00 USD |
| `1D` | `54.10` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 72,230.00 USD | 11,410.00 USD | 19,580.00 USD |
| `7D` | `54.10` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 290,620.00 USD | 0.00 USD | 2,590.00 USD |
| `1D` | `54.20` | 932,270.00 USD | 0.00 USD | 932,270.00 USD | 72,600.00 USD | 15,510.00 USD | 40,120.00 USD |
| `7D` | `54.20` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 205,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `54.30` | 804,040.00 USD | 0.00 USD | 804,040.00 USD | 15,600.00 USD | 0.00 USD | 5,350.00 USD |
| `7D` | `54.30` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 381,380.00 USD | 0.00 USD | 181,420.00 USD |
| `1D` | `54.40` | 783,090.00 USD | 0.00 USD | 783,090.00 USD | 51,570.00 USD | 35,500.00 USD | 3,130.00 USD |
| `7D` | `54.40` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 304,270.00 USD | 13,830.00 USD | 92,140.00 USD |
| `1D` | `54.50` | 692,900.00 USD | 0.00 USD | 692,900.00 USD | 9,670.00 USD | 46,240.00 USD | 1,310.00 USD |
| `7D` | `54.50` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 159,720.00 USD | 15,240.00 USD | 239,890.00 USD |
| `1D` | `54.60` | 635,670.00 USD | 0.00 USD | 635,670.00 USD | 1,520.00 USD | 21,680.00 USD | 5,570.00 USD |
| `7D` | `54.60` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 0.00 USD | 1,930.00 USD | 116,060.00 USD |
| `1D` | `54.70` | 606,900.00 USD | 0.00 USD | 606,900.00 USD | 0.00 USD | 15,420.00 USD | 82,460.00 USD |
| `1D` | `54.80` | 509,020.00 USD | 0.00 USD | 509,020.00 USD | 0.00 USD | 25,800.00 USD | 11,680.00 USD |
| `1D` | `54.90` | 471,550.00 USD | 0.00 USD | 471,550.00 USD | 49,450.00 USD | 10,930.00 USD | 1,530.00 USD |
| `7D` | `54.90` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 0.00 USD | 52,180.00 USD | 47,680.00 USD |
| `1D` | `55.00` | 409,630.00 USD | 0.00 USD | 409,630.00 USD | 19,950.00 USD | 5,030.00 USD | 29,770.00 USD |
| `7D` | `55.00` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 35,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `55.10` | 354,890.00 USD | 0.00 USD | 354,890.00 USD | 0.00 USD | 45,630.00 USD | 28,130.00 USD |
| `7D` | `55.20` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 19,190.00 USD | 46,850.00 USD |
| `1D` | `55.30` | 281,130.00 USD | 0.00 USD | 281,130.00 USD | 0.00 USD | 7,130.00 USD | 0.00 USD |
| `7D` | `55.30` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 11,270.00 USD | 0.00 USD |
| `1D` | `55.40` | 273,990.00 USD | 0.00 USD | 273,990.00 USD | 0.00 USD | 6,510.00 USD | 742.75 USD |
| `7D` | `55.40` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 0.00 USD | 18,550.00 USD | 4,800.00 USD |
| `1D` | `55.50` | 266,740.00 USD | 0.00 USD | 266,740.00 USD | 0.00 USD | 9,250.00 USD | 5,500.00 USD |
| `7D` | `55.50` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 0.00 USD | 33,460.00 USD | 0.00 USD |
| `7D` | `55.60` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 426,340.00 USD | 13,860.00 USD | 0.00 USD |
| `1D` | `55.70` | 251,990.00 USD | 0.00 USD | 251,990.00 USD | 0.00 USD | 7,490.00 USD | 613.46 USD |
| `7D` | `55.70` | 658,340.00 USD | 0.00 USD | 658,340.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD |
| `1D` | `55.80` | 243,880.00 USD | 0.00 USD | 243,880.00 USD | 6,170.00 USD | 26,160.00 USD | 3,340.00 USD |
| `7D` | `55.80` | 451,910.00 USD | 0.00 USD | 451,910.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD |
| `1D` | `55.90` | 208,210.00 USD | 0.00 USD | 208,210.00 USD | 103,700.00 USD | 13,230.00 USD | 91,290.00 USD |
| `7D` | `55.90` | 360,950.00 USD | 0.00 USD | 360,950.00 USD | 141,330.00 USD | 101,960.00 USD | 117,660.00 USD |
| `1D` | `56.00` | 25,100.00 USD | 25,100.00 USD | 0.00 USD | 0.00 USD | 20,600.00 USD | 4,510.00 USD |
| `1D` | `56.00` | 50,200.00 USD | 50,200.00 USD | 0.00 USD | 0.00 USD | 20,600.00 USD | 4,510.00 USD |
| `7D` | `56.00` | 470,900.00 USD | 470,900.00 USD | 0.00 USD | 181,230.00 USD | 118,560.00 USD | 171,110.00 USD |
| `7D` | `56.00` | 941,800.00 USD | 941,800.00 USD | 0.00 USD | 181,230.00 USD | 118,560.00 USD | 171,110.00 USD |
| `1D` | `56.10` | 317,870.00 USD | 317,870.00 USD | 0.00 USD | 68,240.00 USD | 5,890.00 USD | 193,530.00 USD |
| `7D` | `56.10` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 121,920.00 USD | 154,860.00 USD | 61,210.00 USD |
| `1D` | `56.20` | 441,140.00 USD | 441,140.00 USD | 0.00 USD | 59,290.00 USD | 6,070.00 USD | 57,910.00 USD |
| `7D` | `56.20` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 86,240.00 USD | 240,740.00 USD |
| `1D` | `56.30` | 619,220.00 USD | 619,220.00 USD | 0.00 USD | 51,850.00 USD | 51,230.00 USD | 75,010.00 USD |
| `7D` | `56.30` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 148,350.00 USD | 141,900.00 USD | 157,810.00 USD |
| `1D` | `56.40` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 77,640.00 USD | 78,590.00 USD | 238,780.00 USD |
| `7D` | `56.40` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 215,940.00 USD | 125,620.00 USD | 137,070.00 USD |
| `1D` | `56.50` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 138,540.00 USD | 143,390.00 USD | 144,610.00 USD |
| `7D` | `56.50` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 170,750.00 USD | 143,420.00 USD | 6,150.00 USD |
| `1D` | `56.60` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 49,560.00 USD | 104,240.00 USD | 80,910.00 USD |
| `7D` | `56.60` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 363,190.00 USD | 136,570.00 USD | 0.00 USD |
| `1D` | `56.70` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 188,500.00 USD | 27,730.00 USD | 317,930.00 USD |
| `7D` | `56.70` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 117,290.00 USD | 121,500.00 USD | 98,950.00 USD |
| `1D` | `56.80` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 129,190.00 USD | 17,250.00 USD | 75,090.00 USD |
| `7D` | `56.80` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 153,580.00 USD | 92,780.00 USD | 303,010.00 USD |
| `1D` | `56.90` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 38,540.00 USD | 10,710.00 USD | 22,790.00 USD |
| `7D` | `56.90` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 113,780.00 USD | 48,600.00 USD | 266,610.00 USD |
| `1D` | `57.00` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 6,480.00 USD | 18,250.00 USD | 12,770.00 USD |
| `7D` | `57.00` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 88,680.00 USD | 20,690.00 USD | 151,930.00 USD |
| `1D` | `57.10` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 59,550.00 USD | 22,890.00 USD | 25,930.00 USD |
| `7D` | `57.10` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 36,580.00 USD | 19,180.00 USD | 20,440.00 USD |
| `1D` | `57.20` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 32,320.00 USD | 29,370.00 USD | 65,790.00 USD |
| `7D` | `57.20` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 57,060.00 USD | 21,090.00 USD | 3,700.00 USD |
| `1D` | `57.30` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 20,410.00 USD | 28,940.00 USD | 35,110.00 USD |
| `7D` | `57.30` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 22,360.00 USD | 10,060.00 USD | 34,250.00 USD |
| `1D` | `57.40` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 45,570.00 USD | 37,640.00 USD | 12,000.00 USD |
| `7D` | `57.40` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 66,770.00 USD | 31,660.00 USD | 154,430.00 USD |
| `1D` | `57.50` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 144,970.00 USD | 32,830.00 USD | 115,570.00 USD |
| `7D` | `57.50` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 76,670.00 USD | 31,830.00 USD | 0.00 USD |
| `1D` | `57.60` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 69,720.00 USD | 24,050.00 USD | 62,510.00 USD |
| `7D` | `57.60` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 149,560.00 USD | 40,430.00 USD | 28,320.00 USD |
| `1D` | `57.70` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 36,620.00 USD | 26,070.00 USD | 96,350.00 USD |
| `7D` | `57.70` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 0.00 USD | 5,400.00 USD | 57,330.00 USD |
| `1D` | `57.80` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 9,690.00 USD | 13,860.00 USD | 73,330.00 USD |
| `7D` | `57.80` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 9,650.00 USD | 14,360.00 USD | 49,480.00 USD |
| `1D` | `57.90` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 13,000.00 USD | 14,100.00 USD | 9,940.00 USD |
| `7D` | `57.90` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 5,120.00 USD | 963.90 USD | 22,350.00 USD |
| `1D` | `58.00` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 4,580.00 USD | 5,870.00 USD | 7,540.00 USD |
| `7D` | `58.00` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 0.00 USD | 3,670.00 USD | 86,690.00 USD |
| `1D` | `58.10` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 31,400.00 USD | 6,730.00 USD | 15,180.00 USD |
| `7D` | `58.10` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 5,470.00 USD | 1,310.00 USD | 848.40 USD |
| `1D` | `58.20` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 27,190.00 USD | 7,630.00 USD | 406.15 USD |
| `7D` | `58.20` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 0.00 USD | 1,540.00 USD | 0.00 USD |
| `1D` | `58.30` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 21,400.00 USD | 14,060.00 USD | 36,830.00 USD |
| `7D` | `58.30` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 17,950.00 USD | 9,580.00 USD | 26,820.00 USD |
| `1D` | `58.40` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 310.90 USD | 11,100.00 USD | 24,130.00 USD |
| `7D` | `58.40` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 54,120.00 USD |
| `1D` | `58.50` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 21,130.00 USD | 8,030.00 USD | 124.02 USD |
| `7D` | `58.50` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD |
| `1D` | `58.60` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 2,120.00 USD | 0.00 USD | 6,920.00 USD |
| `7D` | `58.60` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `58.70` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 18,120.00 USD | 2,300.00 USD | 355.85 USD |
| `7D` | `58.70` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 4,240.00 USD | 11,600.00 USD | 35,320.00 USD |
| `1D` | `58.80` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 35,830.00 USD | 14,730.00 USD | 23,630.00 USD |
| `7D` | `58.80` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD |
| `1D` | `58.90` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 21,710.00 USD | 103,170.00 USD | 90,770.00 USD |
| `7D` | `58.90` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 0.00 USD | 54,240.00 USD | 83,500.00 USD |
| `1D` | `59.00` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 152,930.00 USD | 60,120.00 USD | 146,730.00 USD |
| `7D` | `59.00` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 259,280.00 USD | 65,270.00 USD | 118,570.00 USD |
| `1D` | `59.10` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 182,580.00 USD | 54,230.00 USD | 173,970.00 USD |
| `7D` | `59.10` | 7,080,000.00 USD | 7,080,000.00 USD | 0.00 USD | 91,060.00 USD | 45,400.00 USD | 158,780.00 USD |
| `1D` | `59.20` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 113,190.00 USD | 63,290.00 USD | 56,270.00 USD |
| `7D` | `59.20` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 153,580.00 USD | 18,540.00 USD | 174,600.00 USD |
| `1D` | `59.30` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 218,400.00 USD | 45,010.00 USD | 101,400.00 USD |
| `7D` | `59.30` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD |
| `1D` | `59.40` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 64,900.00 USD | 55,620.00 USD | 63,750.00 USD |
| `7D` | `59.40` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 105,490.00 USD | 73,620.00 USD | 137,500.00 USD |
| `1D` | `59.50` | 5,980,000.00 USD | 5,980,000.00 USD | 0.00 USD | 89,030.00 USD | 38,560.00 USD | 33,840.00 USD |
| `7D` | `59.50` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD |
| `1D` | `59.60` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 43,670.00 USD | 53,100.00 USD | 7,010.00 USD |
| `7D` | `59.60` | 8,670,000.00 USD | 8,670,000.00 USD | 0.00 USD | 270,460.00 USD | 147,800.00 USD | 86,840.00 USD |
| `1D` | `59.70` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 13,470.00 USD | 19,120.00 USD | 78,050.00 USD |
| `7D` | `59.70` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 55,510.00 USD | 180,620.00 USD | 162,850.00 USD |
| `1D` | `59.80` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 31,530.00 USD | 26,470.00 USD | 10,630.00 USD |
| `7D` | `59.80` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 118,240.00 USD | 97,600.00 USD | 155,270.00 USD |
| `1D` | `59.90` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 111,690.00 USD | 20,240.00 USD | 50,210.00 USD |
| `7D` | `59.90` | 9,810,000.00 USD | 9,810,000.00 USD | 0.00 USD | 246,770.00 USD | 84,430.00 USD | 40,130.00 USD |
| `1D` | `60.00` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 164,190.00 USD | 50,210.00 USD | 50,710.00 USD |
| `7D` | `60.00` | 10,300,000.00 USD | 10,300,000.00 USD | 0.00 USD | 231,370.00 USD | 161,260.00 USD | 94,160.00 USD |
| `1D` | `60.10` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 75,970.00 USD | 28,800.00 USD | 66,510.00 USD |
| `7D` | `60.10` | 10,820,000.00 USD | 10,820,000.00 USD | 0.00 USD | 251,520.00 USD | 110,270.00 USD | 160,960.00 USD |
| `1D` | `60.20` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 105,160.00 USD | 26,960.00 USD | 87,460.00 USD |
| `7D` | `60.20` | 11,320,000.00 USD | 11,320,000.00 USD | 0.00 USD | 207,990.00 USD | 131,530.00 USD | 157,150.00 USD |
| `1D` | `60.30` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 59,630.00 USD | 32,520.00 USD | 28,060.00 USD |
| `7D` | `60.30` | 11,720,000.00 USD | 11,720,000.00 USD | 0.00 USD | 133,350.00 USD | 100,380.00 USD | 170,480.00 USD |
| `1D` | `60.40` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 90,730.00 USD | 13,730.00 USD | 42,890.00 USD |
| `7D` | `60.40` | 12,100,000.00 USD | 12,100,000.00 USD | 0.00 USD | 64,850.00 USD | 108,300.00 USD | 204,780.00 USD |
| `1D` | `60.50` | 7,450,000.00 USD | 7,450,000.00 USD | 0.00 USD | 22,700.00 USD | 24,220.00 USD | 38,360.00 USD |
| `7D` | `60.50` | 12,480,000.00 USD | 12,480,000.00 USD | 0.00 USD | 115,390.00 USD | 86,870.00 USD | 175,550.00 USD |
| `1D` | `60.60` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 40,710.00 USD | 19,140.00 USD | 3,930.00 USD |
| `7D` | `60.60` | 12,870,000.00 USD | 12,870,000.00 USD | 0.00 USD | 251,100.00 USD | 18,640.00 USD | 118,680.00 USD |
| `1D` | `60.70` | 7,580,000.00 USD | 7,580,000.00 USD | 0.00 USD | 36,270.00 USD | 22,330.00 USD | 3,120.00 USD |
| `7D` | `60.70` | 13,070,000.00 USD | 13,070,000.00 USD | 0.00 USD | 119,080.00 USD | 57,480.00 USD | 22,840.00 USD |
| `1D` | `60.80` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 15,430.00 USD | 12,060.00 USD | 47,810.00 USD |
| `7D` | `60.80` | 13,260,000.00 USD | 13,260,000.00 USD | 0.00 USD | 46,960.00 USD | 69,290.00 USD | 76,200.00 USD |
| `1D` | `60.90` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 36,430.00 USD | 21,920.00 USD | 22,850.00 USD |
| `7D` | `60.90` | 13,470,000.00 USD | 13,470,000.00 USD | 0.00 USD | 105,970.00 USD | 34,400.00 USD | 65,270.00 USD |
| `1D` | `61.00` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 45,040.00 USD | 6,430.00 USD | 18,420.00 USD |
| `7D` | `61.00` | 13,600,000.00 USD | 13,600,000.00 USD | 0.00 USD | 96,160.00 USD | 36,500.00 USD | 5,370.00 USD |
| `1D` | `61.10` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 12,010.00 USD | 6,270.00 USD | 11,490.00 USD |
| `7D` | `61.10` | 13,640,000.00 USD | 13,640,000.00 USD | 0.00 USD | 31,540.00 USD | 1,560.00 USD | 0.00 USD |
| `1D` | `61.20` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 72,520.00 USD | 0.00 USD | 38,940.00 USD |
| `7D` | `61.20` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 116,610.00 USD | 64,470.00 USD | 52,930.00 USD |
| `1D` | `61.30` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 0.00 USD | 3,330.00 USD | 0.00 USD |
| `7D` | `61.30` | 14,000,000.00 USD | 14,000,000.00 USD | 0.00 USD | 44,950.00 USD | 25,850.00 USD | 56,880.00 USD |
| `1D` | `61.40` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 1,650.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `61.40` | 14,190,000.00 USD | 14,190,000.00 USD | 0.00 USD | 89,350.00 USD | 41,800.00 USD | 59,330.00 USD |
| `1D` | `61.50` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 1,060.00 USD | 333.03 USD | 2,340.00 USD |
| `7D` | `61.50` | 14,280,000.00 USD | 14,280,000.00 USD | 0.00 USD | 19,810.00 USD | 35,300.00 USD | 36,110.00 USD |
| `1D` | `61.60` | 7,960,000.00 USD | 7,960,000.00 USD | 0.00 USD | 5,360.00 USD | 2,740.00 USD | 0.00 USD |
| `7D` | `61.60` | 14,490,000.00 USD | 14,490,000.00 USD | 0.00 USD | 39,720.00 USD | 50,880.00 USD | 121,470.00 USD |
| `1D` | `61.70` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 12,300.00 USD | 1,010.00 USD | 0.00 USD |
| `7D` | `61.70` | 14,680,000.00 USD | 14,680,000.00 USD | 0.00 USD | 75,210.00 USD | 10,880.00 USD | 99,070.00 USD |
| `1D` | `61.80` | 7,990,000.00 USD | 7,990,000.00 USD | 0.00 USD | 3,480.00 USD | 1,750.00 USD | 5,610.00 USD |
| `7D` | `61.80` | 14,920,000.00 USD | 14,920,000.00 USD | 0.00 USD | 160,110.00 USD | 21,960.00 USD | 62,060.00 USD |
| `1D` | `61.90` | 7,990,000.00 USD | 7,990,000.00 USD | 0.00 USD | 3,160.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `61.90` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 61,440.00 USD | 24,710.00 USD | 32,520.00 USD |
| `1D` | `62.00` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 5,630.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.00` | 15,140,000.00 USD | 15,140,000.00 USD | 0.00 USD | 50,080.00 USD | 8,550.00 USD | 40,590.00 USD |
| `7D` | `62.10` | 15,150,000.00 USD | 15,150,000.00 USD | 0.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.20` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD |
| `7D` | `62.30` | 15,410,000.00 USD | 15,410,000.00 USD | 0.00 USD | 29,050.00 USD | 23,450.00 USD | 97,450.00 USD |
| `7D` | `62.40` | 15,550,000.00 USD | 15,550,000.00 USD | 0.00 USD | 77,960.00 USD | 27,560.00 USD | 30,890.00 USD |
| `7D` | `62.50` | 15,630,000.00 USD | 15,630,000.00 USD | 0.00 USD | 42,730.00 USD | 14,320.00 USD | 26,610.00 USD |
| `7D` | `62.60` | 15,700,000.00 USD | 15,700,000.00 USD | 0.00 USD | 34,910.00 USD | 7,830.00 USD | 27,730.00 USD |
| `7D` | `62.70` | 15,790,000.00 USD | 15,790,000.00 USD | 0.00 USD | 22,020.00 USD | 12,490.00 USD | 47,090.00 USD |
| `7D` | `62.80` | 15,930,000.00 USD | 15,930,000.00 USD | 0.00 USD | 72,250.00 USD | 28,960.00 USD | 45,150.00 USD |
| `7D` | `62.90` | 16,020,000.00 USD | 16,020,000.00 USD | 0.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD |
| `7D` | `63.00` | 16,090,000.00 USD | 16,090,000.00 USD | 0.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD |
| `7D` | `63.10` | 16,130,000.00 USD | 16,130,000.00 USD | 0.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD |
| `7D` | `63.30` | 16,160,000.00 USD | 16,160,000.00 USD | 0.00 USD | 15,010.00 USD | 11,500.00 USD | 9,730.00 USD |
| `7D` | `63.40` | 16,190,000.00 USD | 16,190,000.00 USD | 0.00 USD | 11,980.00 USD | 1,320.00 USD | 9,960.00 USD |
| `7D` | `63.50` | 16,210,000.00 USD | 16,210,000.00 USD | 0.00 USD | 5,430.00 USD | 15,810.00 USD | 4,760.00 USD |
| `7D` | `63.60` | 16,310,000.00 USD | 16,310,000.00 USD | 0.00 USD | 63,480.00 USD | 20,800.00 USD | 11,880.00 USD |
| `7D` | `63.70` | 16,380,000.00 USD | 16,380,000.00 USD | 0.00 USD | 21,940.00 USD | 18,810.00 USD | 35,480.00 USD |
| `7D` | `63.80` | 16,450,000.00 USD | 16,450,000.00 USD | 0.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD |
| `7D` | `63.90` | 16,480,000.00 USD | 16,480,000.00 USD | 0.00 USD | 7,650.00 USD | 12,840.00 USD | 8,940.00 USD |
| `7D` | `64.00` | 16,520,000.00 USD | 16,520,000.00 USD | 0.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD |
| `7D` | `64.10` | 16,550,000.00 USD | 16,550,000.00 USD | 0.00 USD | 20,350.00 USD | 667.05 USD | 10,640.00 USD |
| `7D` | `64.20` | 16,600,000.00 USD | 16,600,000.00 USD | 0.00 USD | 28,840.00 USD | 14,530.00 USD | 584.77 USD |
| `7D` | `64.40` | 16,650,000.00 USD | 16,650,000.00 USD | 0.00 USD | 2,540.00 USD | 20,590.00 USD | 29,110.00 USD |
| `7D` | `64.50` | 16,680,000.00 USD | 16,680,000.00 USD | 0.00 USD | 7,700.00 USD | 7,120.00 USD | 13,310.00 USD |
| `7D` | `64.60` | 16,700,000.00 USD | 16,700,000.00 USD | 0.00 USD | 28,620.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `417.96M` | Total OI Tokens: `7,456,971.6 LTC`
  * 1h OI Change: `-0.85%` | 4h OI Change: `+2.82%` | 24h OI Change: `-7.34%`
  * Exchange Breakdown: Binance=`73.73M` | Bybit=`66.65M` | OKX=`33.87M` | Hyperliquid=`22.45M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `12.81K` | Last 24h: `31.76K` | Last 3d: `59.78K` | Last 7d: `115.16K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0019%` |
| **USDT Bybit** | `0.0090%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0048%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `48.04%` | `51.96%` | `0.92` | 2,980,000.00 USD |
| `15M` | `Binance` | `48.05%` | `51.95%` | `0.92` | 1,170,000.00 USD |
| `15M` | `OKX` | `31.55%` | `68.45%` | `0.46` | 482,420.00 USD |
| `15M` | `Bybit` | `55.24%` | `44.76%` | `1.23` | 158,640.00 USD |
| `15M` | `KuCoin` | `47.63%` | `52.37%` | `0.91` | 164,430.00 USD |
| `15M` | `Gate` | `69.02%` | `30.98%` | `2.23` | 184,120.00 USD |
| `15M` | `Bitget` | `43.6%` | `56.4%` | `0.77` | 51,460.00 USD |
| `15M` | `BingX` | `33.94%` | `66.06%` | `0.51` | 127,410.00 USD |
| `15M` | `MEXC` | `76.53%` | `23.47%` | `3.26` | 98,090.00 USD |
| `15M` | `Bitunix` | `49.95%` | `50.05%` | `1.00` | 62,300.00 USD |
| `15M` | `Hyperliquid` | `41.81%` | `58.19%` | `0.72` | 80,650.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.15%` | `48.85%` | `1.05` | 369,810.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 27,320.00 USD |
| `15M` | `HTX` | `42.45%` | `57.55%` | `0.74` | 1,720.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `74.43%` | `25.57%` | `2.91` | 2,110.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `48.05%` | `51.95%` | `0.92` | 1,170,000.00 USD |
| `15M` | `Global Accounts` | `48.04%` | `51.96%` | `0.92` | 2,980,000.00 USD |
| `1H` | `LTC` | `49.54%` | `50.46%` | `0.98` | 6,730,000.00 USD |
| `1H` | `Binance` | `50.38%` | `49.62%` | `1.02` | 2,550,000.00 USD |
| `1H` | `OKX` | `42.66%` | `57.34%` | `0.74` | 877,580.00 USD |
| `1H` | `Bybit` | `37.93%` | `62.07%` | `0.61` | 551,680.00 USD |
| `1H` | `KuCoin` | `48.26%` | `51.74%` | `0.93` | 557,470.00 USD |
| `1H` | `Gate` | `56.45%` | `43.55%` | `1.30` | 247,310.00 USD |
| `1H` | `Bitget` | `46.98%` | `53.02%` | `0.89` | 119,400.00 USD |
| `1H` | `BingX` | `45.98%` | `54.02%` | `0.85` | 375,960.00 USD |
| `1H` | `MEXC` | `66.58%` | `33.42%` | `1.99` | 276,260.00 USD |
| `1H` | `Bitunix` | `45.84%` | `54.16%` | `0.85` | 141,560.00 USD |
| `1H` | `Hyperliquid` | `40.35%` | `59.65%` | `0.68` | 165,080.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.68%` | `49.32%` | `1.03` | 717,040.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `100%` | `0%` | `1.00` | 147,310.00 USD |
| `1H` | `HTX` | `41.93%` | `58.07%` | `0.72` | 3,070.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `67.5%` | `32.5%` | `2.08` | 1,690.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `50.38%` | `49.62%` | `1.02` | 2,550,000.00 USD |
| `1H` | `Global Accounts` | `49.54%` | `50.46%` | `0.98` | 6,730,000.00 USD |
| `4H` | `LTC` | `48.51%` | `51.49%` | `0.94` | 74,950,000.00 USD |
| `4H` | `Binance` | `53.99%` | `46.01%` | `1.17` | 26,710,000.00 USD |
| `4H` | `OKX` | `50.08%` | `49.92%` | `1.00` | 4,010,000.00 USD |
| `4H` | `Bybit` | `51.67%` | `48.33%` | `1.07` | 5,710,000.00 USD |
| `4H` | `KuCoin` | `41.77%` | `58.23%` | `0.72` | 1,040,000.00 USD |
| `4H` | `Gate` | `41.34%` | `58.66%` | `0.70` | 2,080,000.00 USD |
| `4H` | `Bitget` | `52.5%` | `47.5%` | `1.11` | 1,510,000.00 USD |
| `4H` | `BingX` | `38.03%` | `61.97%` | `0.61` | 13,940,000.00 USD |
| `4H` | `MEXC` | `53.29%` | `46.71%` | `1.14` | 3,000,000.00 USD |
| `4H` | `Bitunix` | `47.99%` | `52.01%` | `0.92` | 1,650,000.00 USD |
| `4H` | `Hyperliquid` | `42.97%` | `57.03%` | `0.75` | 1,680,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.69%` | `51.31%` | `0.95` | 12,420,000.00 USD |
| `4H` | `Crypto.com` | `17.5%` | `82.5%` | `0.21` | 5,050.00 USD |
| `4H` | `WhiteBIT` | `26.31%` | `73.69%` | `0.36` | 571,180.00 USD |
| `4H` | `HTX` | `59.34%` | `40.66%` | `1.46` | 38,870.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.18%` | `54.82%` | `0.82` | 217,490.00 USD |
| `4H` | `Aster` | `67.81%` | `32.19%` | `2.11` | 100,470.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `34.75%` | `65.25%` | `0.53` | 265,400.00 USD |
| `4H` | `Whale Positions` | `53.99%` | `46.01%` | `1.17` | 26,710,000.00 USD |
| `4H` | `Global Accounts` | `48.51%` | `51.49%` | `0.94` | 74,950,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `55.09` | `55.12` | `55.09` | `55.28` | `54.97` | 863,748.33 USD | 238,704.69 USD | 625,043.64 USD | -386,338.95 USD | `-44.73%` | `0B / 13S` |
| `0:00 UTC` | `55.41` | `55.33` | `55.41` | `55.44` | `55.11` | 1,037,180.75 USD | 435,075.60 USD | 602,105.15 USD | -167,029.55 USD | `-16.10%` | `6B / 3S` |
| `5:00 UTC` | `55.56` | `55.49` | `55.56` | `55.70` | `55.20` | 870,084.16 USD | 411,175.51 USD | 458,908.65 USD | -47,733.14 USD | `-5.49%` | `12B / 6S` |
| `0:00 UTC` | `55.98` | `55.89` | `55.98` | `56.08` | `55.64` | 1,411,324.18 USD | 622,108.47 USD | 789,215.71 USD | -167,107.24 USD | `-11.84%` | `7B / 3S` |
| `5:00 UTC` | `56.20` | `56.14` | `56.20` | `56.27` | `55.95` | 941,863.07 USD | 405,285.65 USD | 536,577.42 USD | -131,291.77 USD | `-13.94%` | `0B / 5S` |
| `0:00 UTC` | `56.03` | `55.95` | `56.03` | `56.28` | `55.73` | 1,432,521.27 USD | 626,753.60 USD | 805,767.67 USD | -179,014.08 USD | `-12.50%` | `6B / 18S` |
| `5:00 UTC` | `56.11` | `56.13` | `56.11` | `56.30` | `56.02` | 517,114.54 USD | 217,529.34 USD | 299,585.20 USD | -82,055.86 USD | `-15.87%` | `3B / 3S` |
| `0:00 UTC` | `56.22` | `56.21` | `56.22` | `56.28` | `56.12` | 645,876.21 USD | 293,840.75 USD | 352,035.46 USD | -58,194.71 USD | `-9.01%` | `0B / 1S` |
| `5:00 UTC` | `56.22` | `56.13` | `56.22` | `56.25` | `55.98` | 603,205.25 USD | 271,389.80 USD | 331,815.45 USD | -60,425.65 USD | `-10.02%` | `2B / 7S` |
| `0:00 UTC` | `56.00` | `56.01` | `56.00` | `56.03` | `55.98` | 45,771.82 USD | 23,499.62 USD | 22,272.20 USD | 1,227.43 USD | `+2.68%` | `2B / 1S` |

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
| `5m` | 3,570.00 USD | -96,880.00 USD | **`DISTRIBUTION`** |
| `15m` | 89,790.00 USD | 5,700.00 USD | **`ACCUMULATION`** |
| `30m` | 155,160.00 USD | -66,010.00 USD | **`ACCUMULATION`** |
| `1h` | -3,480.00 USD | -955,400.00 USD | **`DISTRIBUTION`** |
| `2h` | 200,700.00 USD | -1,240,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 316,460.00 USD | -1,620,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -396,830.00 USD | -4,050,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 120,380.00 USD | -7,510,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,530,000.00 USD | -7,500,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 623,180.00 USD | -5,160,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 3,460,000.00 USD | -25,740,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -23,450,000.00 USD | -195,500,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+3.57K` | 15m=`+89.79K` | 1h=`-3.48K` | 24h=`+623.18K`
* Futures Capital Netflows: 5m=`-96.88K` | 15m=`+5.70K` | 1h=`-955.40K` | 24h=`-5.16M`
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
  * `2026-10-30 09:51:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:29:10 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `54.26` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `53.27` (Risk Distance: `0.9896` pts)
  * +2.5R Take Profit: `56.73`
  * Mathematical Lot Sizing: **`10.10 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `56.02` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `57.01` (Risk Distance: `0.9896` pts)
  * +2.5R Take Profit: `53.55`
  * Mathematical Lot Sizing: **`10.10 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`56.52`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
