# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 14:14:31 IST` (`2026-10-30 08:44:31 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `55.40` | **Live Ask Quote**: `55.70` | **Mid Price**: `55.55`
- **Spread Points**: `300.00` | **Spread BPS**: `54.01 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `54.81` | VWAP Z-Score: `+0.66` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.3572` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `45.78` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `57.71` | Lower -3.00σ Band: `51.92`
  * Upper +2.51σ Band: `57.23` | Lower -2.51σ Band: `52.40`
  * Upper +2.01σ Band: `56.75` | Lower -2.01σ Band: `52.88`
  * Upper +2.00σ Band: `56.74` | Lower -2.00σ Band: `52.89`
  * Upper +1.28σ Band: `56.05` | Lower -1.28σ Band: `53.58`
  * Upper +1.00σ Band: `55.78` | Lower -1.00σ Band: `53.85`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`55.73` | EMA-20=`55.69` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`55.78` (Slope: `+0.0000`) | EMA-100=`56.25`
  * Institutional Anchors: EMA-144=`56.49` | EMA-200=`56.61` (Slope: `-0.1724`) | EMA-233=`56.67`
- **Range Boundaries**: 24H High=`58.72` | 24H Low=`52.64` | Weekly High=`59.62` | Weekly Low=`52.64`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `56.21` (Distance: `-1.17%`)
  * Point of Control (POC) = `55.85` (Distance: `-0.54%`)
  * Value Area Low (VAL) = `54.59` (Distance: `+1.77%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.40` | POC=`57.72` | VAL=`56.83`
  * Prior Day Extremes: PDH=`59.52` | PDL=`54.18` | PDC=`54.46`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`58.25` | Weekly POC=`56.43` | Weekly VAL=`55.83`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`56.03` | Low=`52.64`
  * London Session (08:00-16:00 UTC): High=`56.23` | Low=`55.38`
  * New York Session (13:00-21:00 UTC): High=`55.88` | Low=`55.22`
  * Initial Balance (First Hour): IB High=`56.22` | IB Low=`55.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `55.33` - `55.77`
  * Optimal Trade Entry (OTE 0.705): `55.66`
  * Structural Invalidation Anchor (0.786): `55.99`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `55.68` | `55.78` | `55.63` | `55.70` | `10,133` | 564,421.76 USD | 370,841.26 USD | `+65.70%` | -5,479,767.75 USD | `+3.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `55.70` | `55.75` | `55.64` | `55.70` | `1,972` | 109,862.37 USD | -14,869.24 USD | `-13.53%` | -5,494,636.98 USD | `-0.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `55.69` | `55.69` | `55.61` | `55.61` | `245` | 13,651.24 USD | -11,367.75 USD | `-83.27%` | -5,506,004.73 USD | `+0.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `55.96` | `55.99` | `55.65` | `55.90` | `12,643` | 705,526.23 USD | -18,741.70 USD | `-2.66%` | -5,485,444.48 USD | `+0.27` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `55.91` | `55.98` | `55.62` | `55.67` | `12,657` | 705,697.21 USD | -365,164.53 USD | `-51.75%` | -5,850,609.01 USD | `-2.61` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `55.68` | `55.78` | `55.61` | `55.63` | `12,634` | 703,702.65 USD | 344,481.32 USD | `+48.95%` | -5,506,127.68 USD | `+2.64` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `56.13` | `56.47` | `55.97` | `56.23` | `39,454` | 2,217,025.84 USD | 138,107.25 USD | `+6.23%` | -5,162,460.43 USD | `+0.49` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `56.22` | `56.34` | `55.72` | `55.97` | `54,792` | 3,072,188.69 USD | -261,201.20 USD | `-8.50%` | -5,423,661.63 USD | `+0.02` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `55.96` | `55.99` | `55.61` | `55.61` | `37,651` | 2,099,158.81 USD | -39,301.96 USD | `-1.87%` | -5,462,963.59 USD | `+0.33` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -5,054,684.98 USD | `-0.61` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.47` | `55.72` | `55.97` | `202,255` | 11,356,305.33 USD | -519,640.59 USD | `-4.58%` | -5,574,325.57 USD | `+0.43` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `55.96` | `55.99` | `55.61` | `55.63` | `37,934` | 2,114,926.09 USD | -39,424.91 USD | `-1.86%` | -5,613,750.48 USD | `+0.68` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | 387,872.12 USD | `-1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,876,168.80 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -5,054,684.98 USD | `-0.61` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.47` | `55.72` | `55.97` | `202,255` | 11,356,305.33 USD | -519,640.59 USD | `-4.58%` | -5,574,325.57 USD | `+0.43` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `55.96` | `55.99` | `55.61` | `55.63` | `37,934` | 2,114,926.09 USD | -39,424.91 USD | `-1.86%` | -5,613,750.48 USD | `+0.68` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`55.55`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:11:10 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1089` | `0xeadc...9d55` | `LONG` | 2,027,349.15 USD | `36,463.77` | `52.78` | `55.62` | `0.000000` | 102,673.20 USD | `+5.06%` | `10X Cross` |
| `1100` | `0x9aa5...58af` | `SHORT` | 2,011,477.34 USD | `36,177.65` | `71.22` | `55.62` | `307.89` | 565,009.33 USD | `+28.09%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `57.15` | 7,508.68 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 57.1480 USD [API] | `2026-10-29 08:12:16` |
| `ANNOUNCEMENT` | `INFO` | `57.41` | 5,214.91 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 5.21K USD at 57.4140 USD [API] | `2026-10-29 10:32:18` |
| `ANNOUNCEMENT` | `INFO` | `58.00` | 7,509.00 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 57.9980 USD [API] | `2026-10-29 11:54:42` |
| `ANNOUNCEMENT` | `INFO` | `57.87` | 7,508.89 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 57.8720 USD [API] | `2026-10-29 12:02:05` |
| `ANNOUNCEMENT` | `INFO` | `57.87` | 5,812.29 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.81K USD at 57.8740 USD [API] | `2026-10-29 13:57:22` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`56.49` (Vol: 204,200.00 USD, Dist: `+1.25%`) | Long MP=`54.13` (Vol: 153,300.00 USD, Dist: `--2.97%`)
  * 48H Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+5.75%`) | Long MP=`54.12` (Vol: 153,300.00 USD, Dist: `--3.00%`)
  * 3D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+5.75%`) | Long MP=`54.12` (Vol: 153,300.00 USD, Dist: `--3.00%`)
  * 7D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+5.75%`) | Long MP=`54.12` (Vol: 153,300.00 USD, Dist: `--3.00%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `11.35` | 136.20 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.25` | 122.50 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.75` | 2,560.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.15` | 2,220.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.65` | 150.15 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `17.15` | 2,580.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.15` | 2,180.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.05` | 3,470.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.45` | 2,190.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.45` | 454.81 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.55` | 19,110.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.65` | 290.55 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.55` | 4,200.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.45` | 362.12 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.95` | 1,380.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.15` | 982.25 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.65` | 489.32 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.85` | 572.88 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.65` | 447.40 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.75` | 113,020.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.15` | 7,410.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 277,980.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 173.39 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 50,740.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 374.20 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.85` | 744.01 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.05` | 5,510.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 1,340.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 339.03 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 583.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 297,500.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 218.46 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 152.75 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.65` | 1,540.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 538.53 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 27,620.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 1,060.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.65` | 4,640.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 2,870.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 125.24 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 450.10 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.25` | 225.75 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.35` | 2,940.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 4,700.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 953.68 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.95` | 32,950.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.15` | 5,780.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 257.76 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 1,890.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 126.70 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.45` | 70,390.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 3,240.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.75` | 266.53 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 521.45 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 166.49 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 6,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 11,640.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.55` | 109.28 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 101.80 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.85` | 958.10 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 1,490.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 9,260.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 3,530.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 377.50 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 6,210.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 446.67 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.15` | 330.76 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.25` | 695.38 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 847.54 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 2,400.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 993.82 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 4,280.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 2,730.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 664,760.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 570.02 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 264.83 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 716.41 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 806.42 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 5,900.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 1,180.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 133.10 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 2,160.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 1,010.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 133.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 274.39 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.75` | 5,380.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 6,340.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 10,540.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 396.54 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 15,590.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 644.96 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.85` | 336.89 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.95` | 41,950.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 201.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 66,300.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 35,410.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.35` | 301.96 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.55` | 4,120.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 1,570.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.75` | 3,400.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 5,800.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 2,000.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 14,620.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 122,720.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 417.80 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 5,390.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 710.84 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 426.02 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 21,880.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 801.14 USD | 982,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 2,380.00 USD | 981,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 84,440.00 USD | 979,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 2,180.00 USD | 894,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 4,230.00 USD | 892,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 1,480.00 USD | 888,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 2,620.00 USD | 886,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 4,830.00 USD | 884,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 8,710.00 USD | 879,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 3,180.00 USD | 870,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 2,180.00 USD | 867,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 23,940.00 USD | 865,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 12,060.00 USD | 841,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 42,180.00 USD | 829,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.75` | 27,480.00 USD | 787,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 2,940.00 USD | 759,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 706.41 USD | 756,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.35` | 828.74 USD | 755,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.45` | 22,480.00 USD | 755,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 2,140.00 USD | 732,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 3,980.00 USD | 730,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 358.40 USD | 726,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 158.22 USD | 726,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 1,980.00 USD | 725,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.20` | 8,540,000.00 USD | 8,540,000.00 USD | 9,650.00 USD | 2,470.00 USD | 114.09 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.25` | 9,030.00 USD | 723,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.30` | 8,530,000.00 USD | 8,530,000.00 USD | 692.33 USD | 4,740.00 USD | 6,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.35` | 43,920.00 USD | 714,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.40` | 8,510,000.00 USD | 8,510,000.00 USD | 0.00 USD | 1,520.00 USD | 28,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.45` | 2,590.00 USD | 671,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.50` | 8,480,000.00 USD | 8,480,000.00 USD | 11,830.00 USD | 0.00 USD | 7,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.55` | 4,450.00 USD | 668,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 47,750.00 USD | 663,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 381.04 USD | 616,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.10` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.15` | 1,690.00 USD | 615,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.20` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.25` | 8,050.00 USD | 614,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.40` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 6,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.55` | 2,560.00 USD | 606,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.60` | 8,450,000.00 USD | 8,450,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.65` | 273.90 USD | 603,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 333.94 USD | 603,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.80` | 8,440,000.00 USD | 8,440,000.00 USD | 1,780.00 USD | 2,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `48.90` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 0.00 USD | 960.40 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.95` | 252.58 USD | 602,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,580.00 USD | 602,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,740.00 USD | 601,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.30` | 8,440,000.00 USD | 8,440,000.00 USD | 15,190.00 USD | 4,490.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.35` | 5,230.00 USD | 595,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.40` | 8,400,000.00 USD | 8,400,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.45` | 19,440.00 USD | 590,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.50` | 8,400,000.00 USD | 8,400,000.00 USD | 2,830.00 USD | 7,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.55` | 19,940.00 USD | 570,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.60` | 8,390,000.00 USD | 8,390,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.65` | 73,260.00 USD | 550,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.70` | 8,370,000.00 USD | 8,370,000.00 USD | 12,090.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.75` | 1,250.00 USD | 477,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.80` | 8,350,000.00 USD | 8,350,000.00 USD | 9,930.00 USD | 8,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.90` | 8,330,000.00 USD | 8,330,000.00 USD | 45,030.00 USD | 7,170.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.95` | 19,920.00 USD | 476,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.00` | 8,280,000.00 USD | 8,280,000.00 USD | 22,100.00 USD | 7,630.00 USD | 24,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.05` | 1,820.00 USD | 456,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.10` | 3,820,000.00 USD | 3,820,000.00 USD | 11,930.00 USD | 13,980.00 USD | 48,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.10` | 8,220,000.00 USD | 8,220,000.00 USD | 363.50 USD | 682.90 USD | 8,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.20` | 3,750,000.00 USD | 3,750,000.00 USD | 177.10 USD | 709.61 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.20` | 8,210,000.00 USD | 8,210,000.00 USD | 6,960.00 USD | 500.40 USD | 42,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.25` | 102.51 USD | 454,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.30` | 3,740,000.00 USD | 3,740,000.00 USD | 171.03 USD | 3,880.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.30` | 8,160,000.00 USD | 8,160,000.00 USD | 16,270.00 USD | 10,780.00 USD | 7,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.35` | 1,140.00 USD | 454,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.40` | 3,740,000.00 USD | 3,740,000.00 USD | 8,260.00 USD | 11,890.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.40` | 8,130,000.00 USD | 8,130,000.00 USD | 28,280.00 USD | 26,580.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,720.00 USD | 453,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.50` | 3,710,000.00 USD | 3,710,000.00 USD | 8,910.00 USD | 8,790.00 USD | 10,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.50` | 8,040,000.00 USD | 8,040,000.00 USD | 32,490.00 USD | 6,790.00 USD | 44,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.55` | 84,100.00 USD | 448,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.60` | 3,690,000.00 USD | 3,690,000.00 USD | 7,330.00 USD | 3,440.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.60` | 7,960,000.00 USD | 7,960,000.00 USD | 67,580.00 USD | 21,530.00 USD | 31,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.70` | 3,670,000.00 USD | 3,670,000.00 USD | 8,170.00 USD | 2,300.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.70` | 7,840,000.00 USD | 7,840,000.00 USD | 65,920.00 USD | 32,820.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.75` | 9,050.00 USD | 364,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.80` | 3,640,000.00 USD | 3,640,000.00 USD | 12,550.00 USD | 3,100.00 USD | 8,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.80` | 7,700,000.00 USD | 7,700,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.90` | 3,620,000.00 USD | 3,620,000.00 USD | 826.24 USD | 260.05 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.90` | 7,600,000.00 USD | 7,600,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.95` | 431.55 USD | 355,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.00` | 3,610,000.00 USD | 3,610,000.00 USD | 5,040.00 USD | 0.00 USD | 430.77 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.00` | 7,350,000.00 USD | 7,350,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.10` | 3,600,000.00 USD | 3,600,000.00 USD | 9,210.00 USD | 6,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.10` | 7,220,000.00 USD | 7,220,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.15` | 219,370.00 USD | 354,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.20` | 3,590,000.00 USD | 3,590,000.00 USD | 1,770.00 USD | 1,130.00 USD | 19,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.20` | 7,140,000.00 USD | 7,140,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.25` | 202.44 USD | 135,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.30` | 3,570,000.00 USD | 3,570,000.00 USD | 13,550.00 USD | 10,730.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.30` | 7,070,000.00 USD | 7,070,000.00 USD | 28,400.00 USD | 26,720.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.35` | 453.93 USD | 135,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.40` | 3,540,000.00 USD | 3,540,000.00 USD | 7,350.00 USD | 6,840.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.40` | 6,970,000.00 USD | 6,970,000.00 USD | 73,130.00 USD | 42,820.00 USD | 46,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.45` | 27,210.00 USD | 134,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.50` | 3,520,000.00 USD | 3,520,000.00 USD | 5,650.00 USD | 11,190.00 USD | 41,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.50` | 6,810,000.00 USD | 6,810,000.00 USD | 38,520.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.55` | 551.07 USD | 107,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.60` | 3,460,000.00 USD | 3,460,000.00 USD | 9,060.00 USD | 18,580.00 USD | 757.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.60` | 6,710,000.00 USD | 6,710,000.00 USD | 37,880.00 USD | 36,790.00 USD | 41,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.65` | 9,100.00 USD | 107,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.70` | 3,430,000.00 USD | 3,430,000.00 USD | 2,890.00 USD | 13,780.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.70` | 6,600,000.00 USD | 6,600,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.75` | 6,480.00 USD | 98,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.80` | 3,410,000.00 USD | 3,410,000.00 USD | 12,590.00 USD | 19,520.00 USD | 14,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.80` | 6,560,000.00 USD | 6,560,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.85` | 13,680.00 USD | 91,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.90` | 3,360,000.00 USD | 3,360,000.00 USD | 9,590.00 USD | 19,910.00 USD | 23,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.90` | 6,500,000.00 USD | 6,500,000.00 USD | 5,870.00 USD | 25,410.00 USD | 28,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.95` | 16,800.00 USD | 77,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.00` | 3,310,000.00 USD | 3,310,000.00 USD | 20,980.00 USD | 25,620.00 USD | 24,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.00` | 6,440,000.00 USD | 6,440,000.00 USD | 65,840.00 USD | 26,440.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.10` | 3,240,000.00 USD | 3,240,000.00 USD | 34,970.00 USD | 17,300.00 USD | 50,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 6,340,000.00 USD | 6,340,000.00 USD | 24,220.00 USD | 28,090.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.15` | 1,900.00 USD | 61,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.20` | 3,140,000.00 USD | 3,140,000.00 USD | 15,890.00 USD | 7,630.00 USD | 49,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 6,250,000.00 USD | 6,250,000.00 USD | 38,380.00 USD | 13,960.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.25` | 4,930.00 USD | 59,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.30` | 3,060,000.00 USD | 3,060,000.00 USD | 26,510.00 USD | 22,090.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 6,170,000.00 USD | 6,170,000.00 USD | 26,450.00 USD | 40,700.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.35` | 134.02 USD | 54,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.40` | 3,000,000.00 USD | 3,000,000.00 USD | 13,070.00 USD | 15,400.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 6,100,000.00 USD | 6,100,000.00 USD | 20,580.00 USD | 38,950.00 USD | 22,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.45` | 5,930.00 USD | 54,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.50` | 2,970,000.00 USD | 2,970,000.00 USD | 53,990.00 USD | 30,000.00 USD | 79,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.50` | 6,010,000.00 USD | 6,010,000.00 USD | 40,460.00 USD | 667.05 USD | 11,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.55` | 8,700.00 USD | 48,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.60` | 2,800,000.00 USD | 2,800,000.00 USD | 8,330.00 USD | 43,700.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.60` | 5,960,000.00 USD | 5,960,000.00 USD | 73,920.00 USD | 32,590.00 USD | 59,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.70` | 2,750,000.00 USD | 2,750,000.00 USD | 16,690.00 USD | 19,780.00 USD | 40,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.70` | 5,800,000.00 USD | 5,800,000.00 USD | 20,250.00 USD | 84,940.00 USD | 108,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.75` | 30,160.00 USD | 39,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.80` | 2,670,000.00 USD | 2,670,000.00 USD | 27,260.00 USD | 50,850.00 USD | 72,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.80` | 5,580,000.00 USD | 5,580,000.00 USD | 30,590.00 USD | 25,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.85` | 5,950.00 USD | 9,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.90` | 2,520,000.00 USD | 2,520,000.00 USD | 43,760.00 USD | 50,880.00 USD | 30,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.90` | 5,530,000.00 USD | 5,530,000.00 USD | 30,900.00 USD | 11,650.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.95` | 191.15 USD | 3,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.00` | 2,390,000.00 USD | 2,390,000.00 USD | 26,800.00 USD | 30,500.00 USD | 39,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.00` | 5,450,000.00 USD | 5,450,000.00 USD | 39,690.00 USD | 22,700.00 USD | 77,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.10` | 2,300,000.00 USD | 2,300,000.00 USD | 13,270.00 USD | 43,040.00 USD | 85,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.10` | 5,310,000.00 USD | 5,310,000.00 USD | 45,320.00 USD | 17,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.15` | 1,260.00 USD | 3,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.20` | 2,160,000.00 USD | 2,160,000.00 USD | 21,040.00 USD | 6,510.00 USD | 42,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.20` | 5,240,000.00 USD | 5,240,000.00 USD | 162,460.00 USD | 28,320.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.25` | 1,030.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.30` | 2,090,000.00 USD | 2,090,000.00 USD | 2,690.00 USD | 0.00 USD | 5,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.30` | 5,030,000.00 USD | 5,030,000.00 USD | 59,390.00 USD | 24,540.00 USD | 35,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.35` | 941.09 USD | 941.09 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.40` | 2,080,000.00 USD | 2,080,000.00 USD | 4,130.00 USD | 2,880.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.40` | 4,910,000.00 USD | 4,910,000.00 USD | 44,030.00 USD | 7,250.00 USD | 91,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.50` | 2,070,000.00 USD | 2,070,000.00 USD | 9,960.00 USD | 5,700.00 USD | 22,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.50` | 4,770,000.00 USD | 4,770,000.00 USD | 50,990.00 USD | 3,440.00 USD | 28,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.60` | 2,030,000.00 USD | 2,030,000.00 USD | 75,950.00 USD | 3,830.00 USD | 20,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.60` | 4,690,000.00 USD | 4,690,000.00 USD | 52,800.00 USD | 3,780.00 USD | 20,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.70` | 1,930,000.00 USD | 1,930,000.00 USD | 6,210.00 USD | 11,100.00 USD | 11,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.70` | 4,610,000.00 USD | 4,610,000.00 USD | 131,400.00 USD | 21,330.00 USD | 13,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.80` | 1,900,000.00 USD | 1,900,000.00 USD | 53,640.00 USD | 28,920.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.80` | 4,440,000.00 USD | 4,440,000.00 USD | 99,150.00 USD | 43,900.00 USD | 302.55 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.90` | 1,810,000.00 USD | 1,810,000.00 USD | 51,060.00 USD | 39,560.00 USD | 27,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.90` | 4,300,000.00 USD | 4,300,000.00 USD | 160,820.00 USD | 22,780.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.00` | 1,690,000.00 USD | 1,690,000.00 USD | 76,010.00 USD | 21,440.00 USD | 86,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.00` | 4,110,000.00 USD | 4,110,000.00 USD | 380,340.00 USD | 71,820.00 USD | 304,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.10` | 1,510,000.00 USD | 1,510,000.00 USD | 95,780.00 USD | 19,160.00 USD | 49,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.10` | 3,350,000.00 USD | 3,350,000.00 USD | 302,190.00 USD | 0.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.20` | 1,350,000.00 USD | 1,350,000.00 USD | 72,600.00 USD | 15,510.00 USD | 40,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.20` | 3,050,000.00 USD | 3,050,000.00 USD | 205,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.30` | 1,220,000.00 USD | 1,220,000.00 USD | 15,600.00 USD | 0.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.30` | 2,840,000.00 USD | 2,840,000.00 USD | 381,380.00 USD | 0.00 USD | 181,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.40` | 1,200,000.00 USD | 1,200,000.00 USD | 51,570.00 USD | 35,500.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.40` | 2,280,000.00 USD | 2,280,000.00 USD | 304,270.00 USD | 13,830.00 USD | 92,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.50` | 1,110,000.00 USD | 1,110,000.00 USD | 9,670.00 USD | 48,740.00 USD | 8,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.50` | 1,870,000.00 USD | 1,870,000.00 USD | 159,720.00 USD | 15,240.00 USD | 239,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.60` | 1,040,000.00 USD | 1,040,000.00 USD | 913.17 USD | 25,490.00 USD | 43,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.60` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 1,930.00 USD | 131,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.70` | 968,480.00 USD | 968,480.00 USD | 6,600.00 USD | 23,060.00 USD | 105,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.70` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 3,600.00 USD | 41,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.80` | 833,020.00 USD | 833,020.00 USD | 0.00 USD | 48,420.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.80` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 35,700.00 USD | 26,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.90` | 760,680.00 USD | 760,680.00 USD | 66,900.00 USD | 65,440.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.90` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 112,280.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.00` | 617,490.00 USD | 617,490.00 USD | 40,710.00 USD | 54,150.00 USD | 55,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.00` | 1,050,000.00 USD | 1,050,000.00 USD | 97,700.00 USD | 2,830.00 USD | 19,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.10` | 467,440.00 USD | 467,440.00 USD | 50,530.00 USD | 62,170.00 USD | 80,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.10` | 930,880.00 USD | 930,880.00 USD | 54,590.00 USD | 18,510.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.20` | 274,540.00 USD | 274,540.00 USD | 39,390.00 USD | 11,830.00 USD | 66,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.20` | 793,100.00 USD | 793,100.00 USD | 57,400.00 USD | 59,710.00 USD | 150,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.30` | 156,920.00 USD | 156,920.00 USD | 52,860.00 USD | 22,650.00 USD | 59,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.30` | 525,820.00 USD | 525,820.00 USD | 23,140.00 USD | 11,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.40` | 22,230.00 USD | 22,230.00 USD | 0.00 USD | 6,510.00 USD | 742.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.40` | 491,410.00 USD | 491,410.00 USD | 0.00 USD | 18,550.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.50` | 14,980.00 USD | 14,980.00 USD | 0.00 USD | 9,480.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.50` | 468,060.00 USD | 468,060.00 USD | 0.00 USD | 33,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.60` | 434,600.00 USD | 434,600.00 USD | 420,740.00 USD | 13,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.70` | 8,310.00 USD | 8,310.00 USD | 0.00 USD | 7,700.00 USD | 613.46 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.70` | 16,630.00 USD | 16,630.00 USD | 0.00 USD | 7,700.00 USD | 613.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.70` | 206,420.00 USD | 206,420.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.70` | 412,850.00 USD | 412,850.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.80` | 19,800.00 USD | 19,800.00 USD | 0.00 USD | 0.00 USD | 3,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.80` | 503,810.00 USD | 503,810.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.90` | 100,330.00 USD | 100,330.00 USD | 78,980.00 USD | 0.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.90` | 645,140.00 USD | 645,140.00 USD | 141,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.00` | 104,710.00 USD | 104,710.00 USD | 0.00 USD | 0.00 USD | 4,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.00` | 816,260.00 USD | 816,260.00 USD | 2,590.00 USD | 0.00 USD | 168,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.20` | 896,200.00 USD | 896,200.00 USD | 0.00 USD | 79,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.30` | 108,660.00 USD | 108,660.00 USD | 0.00 USD | 0.00 USD | 3,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.30` | 898,790.00 USD | 898,790.00 USD | 0.00 USD | 0.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.40` | 132,990.00 USD | 132,990.00 USD | 5,040.00 USD | 16,820.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.40` | 912,480.00 USD | 912,480.00 USD | 2,650.00 USD | 11,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.50` | 518,310.00 USD | 518,310.00 USD | 138,540.00 USD | 101,980.00 USD | 144,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.50` | 1,230,000.00 USD | 1,230,000.00 USD | 170,750.00 USD | 143,420.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.60` | 753,020.00 USD | 753,020.00 USD | 49,560.00 USD | 104,240.00 USD | 80,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.60` | 1,730,000.00 USD | 1,730,000.00 USD | 363,190.00 USD | 136,570.00 USD | 507.54 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.70` | 1,200,000.00 USD | 1,200,000.00 USD | 97,300.00 USD | 29,790.00 USD | 315,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.70` | 2,070,000.00 USD | 2,070,000.00 USD | 117,290.00 USD | 121,500.00 USD | 98,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.80` | 1,440,000.00 USD | 1,440,000.00 USD | 117,760.00 USD | 20,790.00 USD | 106,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.80` | 2,640,000.00 USD | 2,640,000.00 USD | 153,580.00 USD | 92,780.00 USD | 318,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.90` | 1,540,000.00 USD | 1,540,000.00 USD | 45,140.00 USD | 17,930.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.90` | 3,110,000.00 USD | 3,110,000.00 USD | 113,780.00 USD | 52,200.00 USD | 307,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.00` | 1,620,000.00 USD | 1,620,000.00 USD | 6,480.00 USD | 43,030.00 USD | 29,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.00` | 3,430,000.00 USD | 3,430,000.00 USD | 88,680.00 USD | 56,390.00 USD | 178,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.10` | 1,820,000.00 USD | 1,820,000.00 USD | 77,000.00 USD | 77,400.00 USD | 46,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.10` | 3,570,000.00 USD | 3,570,000.00 USD | 36,580.00 USD | 79,290.00 USD | 21,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.20` | 2,070,000.00 USD | 2,070,000.00 USD | 53,080.00 USD | 78,490.00 USD | 120,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.20` | 3,740,000.00 USD | 3,740,000.00 USD | 118,850.00 USD | 23,920.00 USD | 23,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.30` | 2,270,000.00 USD | 2,270,000.00 USD | 70,930.00 USD | 44,630.00 USD | 87,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.30` | 3,940,000.00 USD | 3,940,000.00 USD | 76,940.00 USD | 28,570.00 USD | 98,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.40` | 2,490,000.00 USD | 2,490,000.00 USD | 84,960.00 USD | 49,470.00 USD | 78,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.40` | 4,390,000.00 USD | 4,390,000.00 USD | 124,180.00 USD | 72,180.00 USD | 257,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.50` | 2,910,000.00 USD | 2,910,000.00 USD | 197,830.00 USD | 48,350.00 USD | 174,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.50` | 4,530,000.00 USD | 4,530,000.00 USD | 99,810.00 USD | 31,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.60` | 3,060,000.00 USD | 3,060,000.00 USD | 69,720.00 USD | 24,050.00 USD | 62,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.60` | 4,740,000.00 USD | 4,740,000.00 USD | 149,560.00 USD | 40,430.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.70` | 3,220,000.00 USD | 3,220,000.00 USD | 36,620.00 USD | 26,070.00 USD | 96,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.70` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 5,400.00 USD | 57,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.75` | 155.35 USD | 155.35 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `57.80` | 3,330,000.00 USD | 3,330,000.00 USD | 9,690.00 USD | 14,890.00 USD | 77,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.80` | 4,880,000.00 USD | 4,880,000.00 USD | 9,650.00 USD | 14,360.00 USD | 49,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.90` | 3,380,000.00 USD | 3,380,000.00 USD | 13,000.00 USD | 15,870.00 USD | 28,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.90` | 4,920,000.00 USD | 4,920,000.00 USD | 5,120.00 USD | 963.90 USD | 30,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.95` | 125.75 USD | 281.10 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.00` | 3,420,000.00 USD | 3,420,000.00 USD | 7,880.00 USD | 9,480.00 USD | 15,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.00` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 5,470.00 USD | 107,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.10` | 3,490,000.00 USD | 3,490,000.00 USD | 31,400.00 USD | 17,830.00 USD | 21,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.10` | 5,070,000.00 USD | 5,070,000.00 USD | 5,470.00 USD | 19,160.00 USD | 14,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.20` | 3,560,000.00 USD | 3,560,000.00 USD | 35,920.00 USD | 34,800.00 USD | 4,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.20` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 31,590.00 USD | 302.55 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.30` | 3,700,000.00 USD | 3,700,000.00 USD | 31,780.00 USD | 38,620.00 USD | 64,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.30` | 5,200,000.00 USD | 5,200,000.00 USD | 48,850.00 USD | 11,000.00 USD | 36,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.40` | 3,790,000.00 USD | 3,790,000.00 USD | 25,750.00 USD | 18,940.00 USD | 50,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.40` | 5,320,000.00 USD | 5,320,000.00 USD | 27,290.00 USD | 9,260.00 USD | 86,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.50` | 3,820,000.00 USD | 3,820,000.00 USD | 21,130.00 USD | 6,460.00 USD | 124.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.50` | 5,350,000.00 USD | 5,350,000.00 USD | 2,060.00 USD | 24,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.60` | 3,890,000.00 USD | 3,890,000.00 USD | 21,940.00 USD | 5,920.00 USD | 40,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.60` | 5,450,000.00 USD | 5,450,000.00 USD | 30,680.00 USD | 20,260.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.70` | 3,970,000.00 USD | 3,970,000.00 USD | 44,920.00 USD | 10,120.00 USD | 29,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.70` | 5,510,000.00 USD | 5,510,000.00 USD | 15,810.00 USD | 11,600.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `58.75` | 789.60 USD | 1,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.80` | 4,040,000.00 USD | 4,040,000.00 USD | 36,630.00 USD | 9,890.00 USD | 23,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.80` | 5,520,000.00 USD | 5,520,000.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `58.85` | 1,480.00 USD | 2,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.90` | 4,220,000.00 USD | 4,220,000.00 USD | 22,130.00 USD | 60,970.00 USD | 90,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.90` | 5,660,000.00 USD | 5,660,000.00 USD | 2,140.00 USD | 54,240.00 USD | 83,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `58.95` | 392.02 USD | 2,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.00` | 4,530,000.00 USD | 4,530,000.00 USD | 129,990.00 USD | 58,870.00 USD | 129,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.00` | 6,110,000.00 USD | 6,110,000.00 USD | 259,280.00 USD | 65,270.00 USD | 118,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.05` | 853.27 USD | 3,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.10` | 4,830,000.00 USD | 4,830,000.00 USD | 92,240.00 USD | 39,860.00 USD | 163,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.10` | 6,400,000.00 USD | 6,400,000.00 USD | 93,390.00 USD | 45,400.00 USD | 158,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.15` | 239.56 USD | 4,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.20` | 5,040,000.00 USD | 5,040,000.00 USD | 101,760.00 USD | 59,450.00 USD | 49,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.20` | 6,750,000.00 USD | 6,750,000.00 USD | 153,580.00 USD | 18,540.00 USD | 174,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.30` | 5,310,000.00 USD | 5,310,000.00 USD | 159,400.00 USD | 34,020.00 USD | 79,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.30` | 7,020,000.00 USD | 7,020,000.00 USD | 88,710.00 USD | 67,460.00 USD | 114,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.35` | 9,440.00 USD | 13,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.40` | 5,450,000.00 USD | 5,450,000.00 USD | 47,830.00 USD | 33,860.00 USD | 58,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.40` | 7,340,000.00 USD | 7,340,000.00 USD | 107,040.00 USD | 73,620.00 USD | 137,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.50` | 5,610,000.00 USD | 5,610,000.00 USD | 83,790.00 USD | 37,380.00 USD | 32,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.50` | 7,490,000.00 USD | 7,490,000.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.60` | 5,710,000.00 USD | 5,710,000.00 USD | 43,950.00 USD | 51,200.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.60` | 8,000,000.00 USD | 8,000,000.00 USD | 270,460.00 USD | 147,800.00 USD | 86,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.70` | 5,810,000.00 USD | 5,810,000.00 USD | 11,230.00 USD | 18,330.00 USD | 72,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.70` | 8,360,000.00 USD | 8,360,000.00 USD | 55,510.00 USD | 145,160.00 USD | 162,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.80` | 5,870,000.00 USD | 5,870,000.00 USD | 32,130.00 USD | 26,470.00 USD | 6,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.80` | 8,730,000.00 USD | 8,730,000.00 USD | 118,240.00 USD | 91,980.00 USD | 154,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.90` | 6,050,000.00 USD | 6,050,000.00 USD | 102,520.00 USD | 17,810.00 USD | 50,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.90` | 8,930,000.00 USD | 8,930,000.00 USD | 142,290.00 USD | 34,490.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.00` | 6,290,000.00 USD | 6,290,000.00 USD | 162,970.00 USD | 29,090.00 USD | 50,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.00` | 9,180,000.00 USD | 9,180,000.00 USD | 100,570.00 USD | 67,520.00 USD | 83,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.05` | 214.38 USD | 13,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.10` | 6,440,000.00 USD | 6,440,000.00 USD | 64,550.00 USD | 28,140.00 USD | 57,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.10` | 9,570,000.00 USD | 9,570,000.00 USD | 200,540.00 USD | 84,980.00 USD | 95,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.15` | 208,880.00 USD | 222,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.20` | 6,600,000.00 USD | 6,600,000.00 USD | 59,560.00 USD | 19,740.00 USD | 82,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.20` | 9,940,000.00 USD | 9,940,000.00 USD | 162,230.00 USD | 99,360.00 USD | 108,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.30` | 6,710,000.00 USD | 6,710,000.00 USD | 53,910.00 USD | 31,630.00 USD | 26,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.30` | 10,340,000.00 USD | 10,340,000.00 USD | 133,350.00 USD | 100,380.00 USD | 170,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.40` | 6,830,000.00 USD | 6,830,000.00 USD | 66,740.00 USD | 13,730.00 USD | 42,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.40` | 10,710,000.00 USD | 10,710,000.00 USD | 64,850.00 USD | 100,560.00 USD | 202,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.50` | 6,910,000.00 USD | 6,910,000.00 USD | 22,700.00 USD | 19,320.00 USD | 36,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.50` | 11,080,000.00 USD | 11,080,000.00 USD | 115,390.00 USD | 80,510.00 USD | 175,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.60` | 6,980,000.00 USD | 6,980,000.00 USD | 40,710.00 USD | 19,140.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.60` | 11,470,000.00 USD | 11,470,000.00 USD | 251,100.00 USD | 18,640.00 USD | 118,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.70` | 7,030,000.00 USD | 7,030,000.00 USD | 32,560.00 USD | 22,330.00 USD | 3,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.70` | 11,670,000.00 USD | 11,670,000.00 USD | 119,080.00 USD | 57,480.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.80` | 7,110,000.00 USD | 7,110,000.00 USD | 11,430.00 USD | 12,060.00 USD | 47,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.80` | 11,840,000.00 USD | 11,840,000.00 USD | 46,960.00 USD | 51,550.00 USD | 76,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.90` | 7,180,000.00 USD | 7,180,000.00 USD | 34,200.00 USD | 21,920.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.90` | 12,040,000.00 USD | 12,040,000.00 USD | 105,970.00 USD | 31,590.00 USD | 64,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.95` | 397.39 USD | 222,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.00` | 7,250,000.00 USD | 7,250,000.00 USD | 43,930.00 USD | 6,430.00 USD | 18,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 12,100,000.00 USD | 12,100,000.00 USD | 43,120.00 USD | 11,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.10` | 7,280,000.00 USD | 7,280,000.00 USD | 12,010.00 USD | 6,270.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 12,130,000.00 USD | 12,130,000.00 USD | 31,540.00 USD | 1,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.20` | 7,390,000.00 USD | 7,390,000.00 USD | 72,600.00 USD | 0.00 USD | 39,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.20` | 12,250,000.00 USD | 12,250,000.00 USD | 51,210.00 USD | 17,600.00 USD | 47,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.30` | 7,410,000.00 USD | 7,410,000.00 USD | 0.00 USD | 4,040.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.30` | 12,300,000.00 USD | 12,300,000.00 USD | 16,510.00 USD | 13,210.00 USD | 24,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.40` | 7,410,000.00 USD | 7,410,000.00 USD | 1,190.00 USD | 709.61 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.40` | 12,440,000.00 USD | 12,440,000.00 USD | 64,440.00 USD | 25,720.00 USD | 43,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.50` | 7,420,000.00 USD | 7,420,000.00 USD | 1,060.00 USD | 3,880.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.50` | 12,540,000.00 USD | 12,540,000.00 USD | 17,710.00 USD | 42,440.00 USD | 41,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.60` | 7,440,000.00 USD | 7,440,000.00 USD | 9,250.00 USD | 11,890.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.60` | 12,750,000.00 USD | 12,750,000.00 USD | 32,920.00 USD | 58,350.00 USD | 121,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.65` | 220.09 USD | 223,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.70` | 7,480,000.00 USD | 7,480,000.00 USD | 13,890.00 USD | 8,790.00 USD | 10,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.70` | 12,940,000.00 USD | 12,940,000.00 USD | 82,860.00 USD | 10,880.00 USD | 99,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.80` | 7,500,000.00 USD | 7,500,000.00 USD | 9,150.00 USD | 3,440.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.80` | 13,210,000.00 USD | 13,210,000.00 USD | 169,680.00 USD | 25,670.00 USD | 71,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.90` | 7,520,000.00 USD | 7,520,000.00 USD | 8,160.00 USD | 2,300.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.90` | 13,360,000.00 USD | 13,360,000.00 USD | 73,690.00 USD | 32,820.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.00` | 7,550,000.00 USD | 7,550,000.00 USD | 15,300.00 USD | 3,100.00 USD | 8,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.00` | 13,460,000.00 USD | 13,460,000.00 USD | 50,080.00 USD | 8,550.00 USD | 40,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.10` | 13,470,000.00 USD | 13,470,000.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.20` | 13,580,000.00 USD | 13,580,000.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.30` | 13,730,000.00 USD | 13,730,000.00 USD | 27,500.00 USD | 23,450.00 USD | 97,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.40` | 13,860,000.00 USD | 13,860,000.00 USD | 76,440.00 USD | 27,560.00 USD | 25,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.50` | 13,940,000.00 USD | 13,940,000.00 USD | 36,690.00 USD | 12,720.00 USD | 25,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `62.95` | 138.49 USD | 223,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `63.45` | 3,350.00 USD | 226,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `63.55` | 8,180.00 USD | 234,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.05` | 121.36 USD | 234,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.85` | 709.03 USD | 235,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `70.75` | 40,900.00 USD | 276,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `71.35` | 112.02 USD | 276,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `76.35` | 8,380.00 USD | 285,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.75` | 578,460.00 USD | 863,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.85` | 602.56 USD | 864,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.95` | 102.89 USD | 864,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.75` | 3,880.00 USD | 868,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.05` | 19,000.00 USD | 887,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.55` | 123.96 USD | 887,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.75` | 214.32 USD | 887,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `84.65` | 2,790.00 USD | 890,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `86.05` | 22,960.00 USD | 913,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `86.85` | 923.22 USD | 914,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `88.85` | 805.87 USD | 914,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `90.65` | 119.66 USD | 915,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `97.65` | 165.03 USD | 915,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.05` | 2,450.00 USD | 917,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.25` | 213.71 USD | 917,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.65` | 31,390.00 USD | 949,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.85` | 2,320.00 USD | 951,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.45` | 355,790.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.75` | 1,620.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.85` | 1,860.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.15` | 199.30 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.05` | 6,470.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 664.59 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `11.35` | 3,040,000.00 USD | 0.00 USD | 136.20 USD | `-79.71%` | `12.00` |
| `Live` | `Long` | `12.25` | 3,040,000.00 USD | 0.00 USD | 122.50 USD | `-78.10%` | `10.00` |
| `Live` | `Long` | `12.75` | 3,040,000.00 USD | 0.00 USD | 2,560.00 USD | `-77.21%` | `200.43` |
| `Live` | `Long` | `13.15` | 3,040,000.00 USD | 0.00 USD | 2,220.00 USD | `-76.49%` | `168.79` |
| `Live` | `Long` | `13.65` | 3,040,000.00 USD | 0.00 USD | 150.15 USD | `-75.60%` | `11.00` |
| `Live` | `Long` | `17.15` | 3,040,000.00 USD | 0.00 USD | 2,580.00 USD | `-69.34%` | `150.57` |
| `Live` | `Long` | `18.15` | 3,030,000.00 USD | 0.00 USD | 2,180.00 USD | `-67.56%` | `120.00` |
| `Live` | `Long` | `19.05` | 3,030,000.00 USD | 0.00 USD | 3,470.00 USD | `-65.95%` | `182.00` |
| `Live` | `Long` | `19.45` | 3,030,000.00 USD | 0.00 USD | 2,190.00 USD | `-65.23%` | `112.49` |
| `Live` | `Long` | `20.45` | 3,030,000.00 USD | 0.00 USD | 454.81 USD | `-63.44%` | `22.24` |
| `Live` | `Long` | `20.55` | 3,030,000.00 USD | 0.00 USD | 19,110.00 USD | `-63.27%` | `930.00` |
| `Live` | `Long` | `20.65` | 3,010,000.00 USD | 0.00 USD | 290.55 USD | `-63.09%` | `14.07` |
| `Live` | `Long` | `21.55` | 3,010,000.00 USD | 0.00 USD | 4,200.00 USD | `-61.48%` | `195.03` |
| `Live` | `Long` | `22.45` | 3,000,000.00 USD | 0.00 USD | 362.12 USD | `-59.87%` | `16.13` |
| `Live` | `Long` | `22.95` | 3,000,000.00 USD | 0.00 USD | 1,380.00 USD | `-58.98%` | `60.00` |
| `Live` | `Long` | `23.15` | 3,000,000.00 USD | 0.00 USD | 982.25 USD | `-58.62%` | `42.43` |
| `Live` | `Long` | `23.65` | 3,000,000.00 USD | 0.00 USD | 489.32 USD | `-57.72%` | `20.69` |
| `Live` | `Long` | `23.85` | 3,000,000.00 USD | 0.00 USD | 572.88 USD | `-57.37%` | `24.02` |
| `Live` | `Long` | `24.65` | 3,000,000.00 USD | 0.00 USD | 447.40 USD | `-55.94%` | `18.15` |
| `Live` | `Long` | `24.75` | 3,000,000.00 USD | 0.00 USD | 113,020.00 USD | `-55.76%` | `4,566.66` |
| `Live` | `Long` | `25.15` | 2,890,000.00 USD | 0.00 USD | 7,410.00 USD | `-55.04%` | `294.67` |
| `Live` | `Long` | `25.25` | 2,880,000.00 USD | 0.00 USD | 277,980.00 USD | `-54.86%` | `11,009.19` |
| `Live` | `Long` | `25.35` | 2,600,000.00 USD | 0.00 USD | 173.39 USD | `-54.69%` | `6.84` |
| `Live` | `Long` | `25.55` | 2,600,000.00 USD | 0.00 USD | 50,740.00 USD | `-54.33%` | `1,985.99` |
| `Live` | `Long` | `25.95` | 2,550,000.00 USD | 0.00 USD | 374.20 USD | `-53.61%` | `14.42` |
| `Live` | `Long` | `26.85` | 2,550,000.00 USD | 0.00 USD | 744.01 USD | `-52.00%` | `27.71` |
| `Live` | `Long` | `27.05` | 2,550,000.00 USD | 0.00 USD | 5,510.00 USD | `-51.65%` | `203.85` |
| `Live` | `Long` | `27.55` | 2,540,000.00 USD | 0.00 USD | 1,340.00 USD | `-50.75%` | `48.82` |
| `Live` | `Long` | `27.95` | 2,540,000.00 USD | 0.00 USD | 339.03 USD | `-50.04%` | `12.13` |
| `Live` | `Long` | `29.15` | 2,540,000.00 USD | 0.00 USD | 583.00 USD | `-47.89%` | `20.00` |
| `Live` | `Long` | `29.75` | 2,540,000.00 USD | 0.00 USD | 297,500.00 USD | `-46.82%` | `10,000.00` |
| `Live` | `Long` | `30.05` | 2,240,000.00 USD | 0.00 USD | 218.46 USD | `-46.28%` | `7.27` |
| `Live` | `Long` | `30.55` | 2,240,000.00 USD | 0.00 USD | 152.75 USD | `-45.39%` | `5.00` |
| `Live` | `Long` | `30.65` | 2,240,000.00 USD | 0.00 USD | 1,540.00 USD | `-45.21%` | `50.19` |
| `Live` | `Long` | `30.95` | 2,240,000.00 USD | 0.00 USD | 538.53 USD | `-44.68%` | `17.40` |
| `Live` | `Long` | `31.15` | 2,240,000.00 USD | 0.00 USD | 27,620.00 USD | `-44.32%` | `886.80` |
| `Live` | `Long` | `31.55` | 2,210,000.00 USD | 0.00 USD | 1,060.00 USD | `-43.60%` | `33.49` |
| `Live` | `Long` | `31.65` | 2,210,000.00 USD | 0.00 USD | 4,640.00 USD | `-43.42%` | `146.53` |
| `Live` | `Long` | `31.85` | 2,210,000.00 USD | 0.00 USD | 2,870.00 USD | `-43.07%` | `90.00` |
| `Live` | `Long` | `31.95` | 2,200,000.00 USD | 0.00 USD | 125.24 USD | `-42.89%` | `3.92` |
| `Live` | `Long` | `32.15` | 2,200,000.00 USD | 0.00 USD | 450.10 USD | `-42.53%` | `14.00` |
| `Live` | `Long` | `32.25` | 2,200,000.00 USD | 0.00 USD | 225.75 USD | `-42.35%` | `7.00` |
| `Live` | `Long` | `32.35` | 2,200,000.00 USD | 0.00 USD | 2,940.00 USD | `-42.17%` | `90.75` |
| `Live` | `Long` | `32.65` | 2,200,000.00 USD | 0.00 USD | 4,700.00 USD | `-41.64%` | `144.01` |
| `Live` | `Long` | `32.75` | 2,200,000.00 USD | 0.00 USD | 953.68 USD | `-41.46%` | `29.12` |
| `Live` | `Long` | `32.95` | 2,190,000.00 USD | 0.00 USD | 32,950.00 USD | `-41.10%` | `1,000.01` |
| `Live` | `Long` | `33.15` | 2,160,000.00 USD | 0.00 USD | 5,780.00 USD | `-40.74%` | `174.22` |
| `Live` | `Long` | `33.65` | 2,160,000.00 USD | 0.00 USD | 257.76 USD | `-39.85%` | `7.66` |
| `Live` | `Long` | `34.05` | 2,160,000.00 USD | 0.00 USD | 1,890.00 USD | `-39.13%` | `55.37` |
| `Live` | `Long` | `34.15` | 2,150,000.00 USD | 0.00 USD | 126.70 USD | `-38.96%` | `3.71` |
| `Live` | `Long` | `34.45` | 2,150,000.00 USD | 0.00 USD | 70,390.00 USD | `-38.42%` | `2,043.24` |
| `Live` | `Long` | `34.65` | 2,080,000.00 USD | 0.00 USD | 3,240.00 USD | `-38.06%` | `93.56` |
| `Live` | `Long` | `34.75` | 2,080,000.00 USD | 0.00 USD | 266.53 USD | `-37.88%` | `7.67` |
| `Live` | `Long` | `34.95` | 2,080,000.00 USD | 0.00 USD | 521.45 USD | `-37.53%` | `14.92` |
| `Live` | `Long` | `35.05` | 2,080,000.00 USD | 0.00 USD | 166.49 USD | `-37.35%` | `4.75` |
| `Live` | `Long` | `36.35` | 2,080,000.00 USD | 0.00 USD | 6,000.00 USD | `-35.02%` | `164.94` |
| `Live` | `Long` | `36.45` | 2,070,000.00 USD | 0.00 USD | 11,640.00 USD | `-34.84%` | `319.44` |
| `Live` | `Long` | `36.55` | 2,060,000.00 USD | 0.00 USD | 109.28 USD | `-34.67%` | `2.99` |
| `Live` | `Long` | `36.75` | 2,060,000.00 USD | 0.00 USD | 101.80 USD | `-34.31%` | `2.77` |
| `Live` | `Long` | `36.85` | 2,060,000.00 USD | 0.00 USD | 958.10 USD | `-34.13%` | `26.00` |
| `Live` | `Long` | `37.15` | 2,060,000.00 USD | 0.00 USD | 1,490.00 USD | `-33.59%` | `40.08` |
| `Live` | `Long` | `37.35` | 2,060,000.00 USD | 0.00 USD | 9,260.00 USD | `-33.24%` | `247.91` |
| `Live` | `Long` | `37.55` | 2,050,000.00 USD | 0.00 USD | 3,530.00 USD | `-32.88%` | `94.04` |
| `Live` | `Long` | `37.75` | 2,050,000.00 USD | 0.00 USD | 377.50 USD | `-32.52%` | `10.00` |
| `Live` | `Long` | `37.85` | 2,050,000.00 USD | 0.00 USD | 6,210.00 USD | `-32.34%` | `164.03` |
| `Live` | `Long` | `37.95` | 2,040,000.00 USD | 0.00 USD | 446.67 USD | `-32.16%` | `11.77` |
| `Live` | `Long` | `38.15` | 2,040,000.00 USD | 0.00 USD | 330.76 USD | `-31.81%` | `8.67` |
| `Live` | `Long` | `38.25` | 2,040,000.00 USD | 0.00 USD | 695.38 USD | `-31.63%` | `18.18` |
| `Live` | `Long` | `38.35` | 2,040,000.00 USD | 0.00 USD | 847.54 USD | `-31.45%` | `22.10` |
| `Live` | `Long` | `38.45` | 2,040,000.00 USD | 0.00 USD | 2,400.00 USD | `-31.27%` | `62.34` |
| `Live` | `Long` | `38.55` | 2,030,000.00 USD | 0.00 USD | 993.82 USD | `-31.09%` | `25.78` |
| `Live` | `Long` | `38.65` | 2,030,000.00 USD | 0.00 USD | 4,280.00 USD | `-30.91%` | `110.74` |
| `Live` | `Long` | `38.95` | 2,030,000.00 USD | 0.00 USD | 2,730.00 USD | `-30.38%` | `70.00` |
| `Live` | `Long` | `39.05` | 2,030,000.00 USD | 0.00 USD | 664,760.00 USD | `-30.20%` | `17,023.28` |
| `Live` | `Long` | `39.15` | 1,360,000.00 USD | 0.00 USD | 570.02 USD | `-30.02%` | `14.56` |
| `Live` | `Long` | `39.35` | 1,360,000.00 USD | 0.00 USD | 264.83 USD | `-29.66%` | `6.73` |
| `Live` | `Long` | `39.45` | 1,360,000.00 USD | 0.00 USD | 716.41 USD | `-29.48%` | `18.16` |
| `Live` | `Long` | `39.55` | 1,360,000.00 USD | 0.00 USD | 806.42 USD | `-29.30%` | `20.39` |
| `Live` | `Long` | `39.65` | 1,360,000.00 USD | 0.00 USD | 5,900.00 USD | `-29.12%` | `148.78` |
| `Live` | `Long` | `39.75` | 1,350,000.00 USD | 0.00 USD | 1,180.00 USD | `-28.95%` | `29.57` |
| `Live` | `Long` | `39.85` | 1,350,000.00 USD | 0.00 USD | 133.10 USD | `-28.77%` | `3.34` |
| `Live` | `Long` | `40.05` | 1,350,000.00 USD | 0.00 USD | 2,160.00 USD | `-28.41%` | `53.97` |
| `Live` | `Long` | `40.45` | 1,350,000.00 USD | 0.00 USD | 1,010.00 USD | `-27.69%` | `24.92` |
| `Live` | `Long` | `40.55` | 1,350,000.00 USD | 0.00 USD | 133.00 USD | `-27.52%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,350,000.00 USD | 0.00 USD | 274.39 USD | `-27.34%` | `6.75` |
| `Live` | `Long` | `40.75` | 1,350,000.00 USD | 0.00 USD | 5,380.00 USD | `-27.16%` | `131.94` |
| `Live` | `Long` | `40.85` | 1,340,000.00 USD | 0.00 USD | 6,340.00 USD | `-26.98%` | `155.23` |
| `Live` | `Long` | `40.95` | 1,340,000.00 USD | 0.00 USD | 10,540.00 USD | `-26.80%` | `257.36` |
| `Live` | `Long` | `41.05` | 1,330,000.00 USD | 0.00 USD | 396.54 USD | `-26.62%` | `9.66` |
| `Live` | `Long` | `41.25` | 1,330,000.00 USD | 0.00 USD | 15,590.00 USD | `-26.26%` | `377.85` |
| `Live` | `Long` | `41.45` | 1,310,000.00 USD | 0.00 USD | 644.96 USD | `-25.91%` | `15.56` |
| `Live` | `Long` | `41.85` | 1,310,000.00 USD | 0.00 USD | 336.89 USD | `-25.19%` | `8.05` |
| `Live` | `Long` | `41.95` | 1,310,000.00 USD | 0.00 USD | 41,950.00 USD | `-25.01%` | `1,000.00` |
| `Live` | `Long` | `42.05` | 1,270,000.00 USD | 0.00 USD | 201.00 USD | `-24.83%` | `4.78` |
| `Live` | `Long` | `42.15` | 1,270,000.00 USD | 0.00 USD | 66,300.00 USD | `-24.66%` | `1,572.94` |
| `Live` | `Long` | `42.25` | 1,200,000.00 USD | 0.00 USD | 35,410.00 USD | `-24.48%` | `838.00` |
| `Live` | `Long` | `42.35` | 1,170,000.00 USD | 0.00 USD | 301.96 USD | `-24.30%` | `7.13` |
| `Live` | `Long` | `42.55` | 1,170,000.00 USD | 0.00 USD | 4,120.00 USD | `-23.94%` | `96.82` |
| `Live` | `Long` | `42.65` | 1,160,000.00 USD | 0.00 USD | 1,570.00 USD | `-23.76%` | `36.70` |
| `Live` | `Long` | `42.75` | 1,160,000.00 USD | 0.00 USD | 3,400.00 USD | `-23.58%` | `79.49` |
| `Live` | `Long` | `42.85` | 1,160,000.00 USD | 0.00 USD | 5,800.00 USD | `-23.40%` | `135.38` |
| `Live` | `Long` | `42.95` | 1,150,000.00 USD | 0.00 USD | 2,000.00 USD | `-23.23%` | `46.65` |
| `Live` | `Long` | `43.05` | 1,150,000.00 USD | 0.00 USD | 14,620.00 USD | `-23.05%` | `339.71` |
| `Live` | `Long` | `43.15` | 1,130,000.00 USD | 0.00 USD | 122,720.00 USD | `-22.87%` | `2,844.09` |
| `Live` | `Long` | `43.25` | 1,010,000.00 USD | 0.00 USD | 417.80 USD | `-22.69%` | `9.66` |
| `Live` | `Long` | `43.35` | 1,010,000.00 USD | 0.00 USD | 5,390.00 USD | `-22.51%` | `124.24` |
| `Live` | `Long` | `43.45` | 1,010,000.00 USD | 0.00 USD | 710.84 USD | `-22.33%` | `16.36` |
| `Live` | `Long` | `43.65` | 1,000,000.00 USD | 0.00 USD | 426.02 USD | `-21.97%` | `9.76` |
| `Live` | `Long` | `43.75` | 1,000,000.00 USD | 0.00 USD | 21,880.00 USD | `-21.80%` | `500.00` |
| `Live` | `Long` | `43.85` | 982,250.00 USD | 0.00 USD | 801.14 USD | `-21.62%` | `18.27` |
| `Live` | `Long` | `44.15` | 981,450.00 USD | 0.00 USD | 2,380.00 USD | `-21.08%` | `53.99` |
| `Live` | `Long` | `44.35` | 979,060.00 USD | 0.00 USD | 84,440.00 USD | `-20.72%` | `1,903.87` |
| `Live` | `Long` | `44.55` | 894,630.00 USD | 0.00 USD | 2,180.00 USD | `-20.37%` | `48.91` |
| `Live` | `Long` | `44.75` | 892,450.00 USD | 0.00 USD | 4,230.00 USD | `-20.01%` | `94.55` |
| `Live` | `Long` | `44.85` | 888,220.00 USD | 0.00 USD | 1,480.00 USD | `-19.83%` | `33.00` |
| `Live` | `Long` | `44.95` | 886,740.00 USD | 0.00 USD | 2,620.00 USD | `-19.65%` | `58.18` |
| `Live` | `Long` | `45.05` | 884,120.00 USD | 0.00 USD | 4,830.00 USD | `-19.47%` | `107.31` |
| `Live` | `Long` | `45.15` | 879,290.00 USD | 0.00 USD | 8,710.00 USD | `-19.29%` | `193.00` |
| `Live` | `Long` | `45.25` | 870,570.00 USD | 0.00 USD | 3,180.00 USD | `-19.11%` | `70.37` |
| `Live` | `Long` | `45.35` | 867,390.00 USD | 0.00 USD | 2,180.00 USD | `-18.94%` | `48.02` |
| `Live` | `Long` | `45.45` | 865,210.00 USD | 0.00 USD | 23,940.00 USD | `-18.76%` | `526.65` |
| `Live` | `Long` | `45.55` | 841,270.00 USD | 0.00 USD | 12,060.00 USD | `-18.58%` | `264.81` |
| `Live` | `Long` | `45.65` | 829,210.00 USD | 0.00 USD | 42,180.00 USD | `-18.40%` | `924.03` |
| `Live` | `Long` | `45.75` | 787,030.00 USD | 0.00 USD | 27,480.00 USD | `-18.22%` | `600.68` |
| `Live` | `Long` | `45.95` | 759,550.00 USD | 0.00 USD | 2,940.00 USD | `-17.86%` | `64.09` |
| `Live` | `Long` | `46.05` | 756,600.00 USD | 0.00 USD | 706.41 USD | `-17.68%` | `15.34` |
| `Live` | `Long` | `46.35` | 755,900.00 USD | 0.00 USD | 828.74 USD | `-17.15%` | `17.88` |
| `Live` | `Long` | `46.45` | 755,070.00 USD | 0.00 USD | 22,480.00 USD | `-16.97%` | `483.97` |
| `Live` | `Long` | `46.55` | 732,590.00 USD | 0.00 USD | 2,140.00 USD | `-16.79%` | `45.93` |
| `Live` | `Long` | `46.65` | 730,450.00 USD | 0.00 USD | 3,980.00 USD | `-16.61%` | `85.41` |
| `Live` | `Long` | `46.85` | 726,470.00 USD | 0.00 USD | 358.40 USD | `-16.25%` | `7.65` |
| `Live` | `Long` | `46.95` | 726,110.00 USD | 0.00 USD | 158.22 USD | `-16.08%` | `3.37` |
| `Live` | `Long` | `47.15` | 725,950.00 USD | 0.00 USD | 1,980.00 USD | `-15.72%` | `42.07` |
| `Live` | `Long` | `47.25` | 723,970.00 USD | 0.00 USD | 9,030.00 USD | `-15.54%` | `191.21` |
| `Live` | `Long` | `47.35` | 714,930.00 USD | 0.00 USD | 43,920.00 USD | `-15.36%` | `927.56` |
| `Live` | `Long` | `47.45` | 671,010.00 USD | 0.00 USD | 2,590.00 USD | `-15.18%` | `54.54` |
| `Live` | `Long` | `47.55` | 668,420.00 USD | 0.00 USD | 4,450.00 USD | `-15.00%` | `93.69` |
| `Live` | `Long` | `47.75` | 663,970.00 USD | 0.00 USD | 47,750.00 USD | `-14.65%` | `1,000.00` |
| `Live` | `Long` | `48.05` | 616,220.00 USD | 0.00 USD | 381.04 USD | `-14.11%` | `7.93` |
| `Live` | `Long` | `48.15` | 615,840.00 USD | 0.00 USD | 1,690.00 USD | `-13.93%` | `35.03` |
| `Live` | `Long` | `48.25` | 614,150.00 USD | 0.00 USD | 8,050.00 USD | `-13.75%` | `166.87` |
| `Live` | `Long` | `48.55` | 606,100.00 USD | 0.00 USD | 2,560.00 USD | `-13.22%` | `52.70` |
| `Live` | `Long` | `48.65` | 603,540.00 USD | 0.00 USD | 273.90 USD | `-13.04%` | `5.63` |
| `Live` | `Long` | `48.75` | 603,270.00 USD | 0.00 USD | 333.94 USD | `-12.86%` | `6.85` |
| `Live` | `Long` | `48.95` | 602,930.00 USD | 0.00 USD | 252.58 USD | `-12.50%` | `5.16` |
| `Live` | `Long` | `49.05` | 602,680.00 USD | 0.00 USD | 1,580.00 USD | `-12.32%` | `32.25` |
| `Live` | `Long` | `49.15` | 601,100.00 USD | 0.00 USD | 5,740.00 USD | `-12.14%` | `116.83` |
| `Live` | `Long` | `49.35` | 595,360.00 USD | 0.00 USD | 5,230.00 USD | `-11.79%` | `105.97` |
| `Live` | `Long` | `49.45` | 590,130.00 USD | 0.00 USD | 19,440.00 USD | `-11.61%` | `393.17` |
| `Live` | `Long` | `49.55` | 570,690.00 USD | 0.00 USD | 19,940.00 USD | `-11.43%` | `402.36` |
| `Live` | `Long` | `49.65` | 550,750.00 USD | 0.00 USD | 73,260.00 USD | `-11.25%` | `1,475.52` |
| `Live` | `Long` | `49.75` | 477,490.00 USD | 0.00 USD | 1,250.00 USD | `-11.07%` | `25.06` |
| `Live` | `Long` | `49.95` | 476,240.00 USD | 0.00 USD | 19,920.00 USD | `-10.71%` | `398.70` |
| `Live` | `Long` | `50.05` | 456,330.00 USD | 0.00 USD | 1,820.00 USD | `-10.53%` | `36.43` |
| `Live` | `Long` | `50.25` | 454,500.00 USD | 0.00 USD | 102.51 USD | `-10.18%` | `2.04` |
| `Live` | `Long` | `50.35` | 454,400.00 USD | 0.00 USD | 1,140.00 USD | `-10.00%` | `22.67` |
| `Live` | `Long` | `50.45` | 453,260.00 USD | 0.00 USD | 4,720.00 USD | `-9.82%` | `93.64` |
| `Live` | `Long` | `50.55` | 448,540.00 USD | 0.00 USD | 84,100.00 USD | `-9.64%` | `1,663.61` |
| `Live` | `Long` | `50.75` | 364,440.00 USD | 0.00 USD | 9,050.00 USD | `-9.28%` | `178.28` |
| `Live` | `Long` | `50.95` | 355,390.00 USD | 0.00 USD | 431.55 USD | `-8.93%` | `8.47` |
| `Live` | `Long` | `51.15` | 354,960.00 USD | 0.00 USD | 219,370.00 USD | `-8.57%` | `4,288.79` |
| `Live` | `Long` | `51.25` | 135,590.00 USD | 0.00 USD | 202.44 USD | `-8.39%` | `3.95` |
| `Live` | `Long` | `51.35` | 135,390.00 USD | 0.00 USD | 453.93 USD | `-8.21%` | `8.84` |
| `Live` | `Long` | `51.45` | 134,930.00 USD | 0.00 USD | 27,210.00 USD | `-8.03%` | `528.81` |
| `Live` | `Long` | `51.55` | 107,730.00 USD | 0.00 USD | 551.07 USD | `-7.85%` | `10.69` |
| `Live` | `Long` | `51.65` | 107,170.00 USD | 0.00 USD | 9,100.00 USD | `-7.67%` | `176.09` |
| `Live` | `Long` | `51.75` | 98,080.00 USD | 0.00 USD | 6,480.00 USD | `-7.50%` | `125.17` |
| `Live` | `Long` | `51.85` | 91,600.00 USD | 0.00 USD | 13,680.00 USD | `-7.32%` | `263.89` |
| `Live` | `Long` | `51.95` | 77,920.00 USD | 0.00 USD | 16,800.00 USD | `-7.14%` | `323.48` |
| `Live` | `Long` | `52.15` | 61,110.00 USD | 0.00 USD | 1,900.00 USD | `-6.78%` | `36.36` |
| `Live` | `Long` | `52.25` | 59,220.00 USD | 0.00 USD | 4,930.00 USD | `-6.60%` | `94.33` |
| `Live` | `Long` | `52.35` | 54,290.00 USD | 0.00 USD | 134.02 USD | `-6.42%` | `2.56` |
| `Live` | `Long` | `52.45` | 54,160.00 USD | 0.00 USD | 5,930.00 USD | `-6.24%` | `113.12` |
| `Live` | `Long` | `52.55` | 48,220.00 USD | 0.00 USD | 8,700.00 USD | `-6.07%` | `165.49` |
| `Live` | `Long` | `52.75` | 39,530.00 USD | 0.00 USD | 30,160.00 USD | `-5.71%` | `571.67` |
| `Live` | `Long` | `52.85` | 9,370.00 USD | 0.00 USD | 5,950.00 USD | `-5.53%` | `112.64` |
| `Live` | `Long` | `52.95` | 3,420.00 USD | 0.00 USD | 191.15 USD | `-5.35%` | `3.61` |
| `Live` | `Long` | `53.15` | 3,230.00 USD | 0.00 USD | 1,260.00 USD | `-4.99%` | `23.70` |
| `Live` | `Long` | `53.25` | 1,970.00 USD | 0.00 USD | 1,030.00 USD | `-4.81%` | `19.25` |
| `Live` | `Long` | `53.35` | 941.09 USD | 0.00 USD | 941.09 USD | `-4.64%` | `17.64` |
| `Live` | `Short` | `57.75` | 155.35 USD | 155.35 USD | 0.00 USD | `+3.23%` | `2.69` |
| `Live` | `Short` | `57.95` | 281.10 USD | 125.75 USD | 0.00 USD | `+3.59%` | `2.17` |
| `Live` | `Short` | `58.75` | 1,070.00 USD | 789.60 USD | 0.00 USD | `+5.02%` | `13.44` |
| `Live` | `Short` | `58.85` | 2,550.00 USD | 1,480.00 USD | 0.00 USD | `+5.20%` | `25.13` |
| `Live` | `Short` | `58.95` | 2,940.00 USD | 392.02 USD | 0.00 USD | `+5.38%` | `6.65` |
| `Live` | `Short` | `59.05` | 3,790.00 USD | 853.27 USD | 0.00 USD | `+5.55%` | `14.45` |
| `Live` | `Short` | `59.15` | 4,030.00 USD | 239.56 USD | 0.00 USD | `+5.73%` | `4.05` |
| `Live` | `Short` | `59.35` | 13,480.00 USD | 9,440.00 USD | 0.00 USD | `+6.09%` | `159.09` |
| `Live` | `Short` | `60.05` | 13,690.00 USD | 214.38 USD | 0.00 USD | `+7.34%` | `3.57` |
| `Live` | `Short` | `60.15` | 222,570.00 USD | 208,880.00 USD | 0.00 USD | `+7.52%` | `3,472.67` |
| `Live` | `Short` | `60.95` | 222,970.00 USD | 397.39 USD | 0.00 USD | `+8.95%` | `6.52` |
| `Live` | `Short` | `61.65` | 223,190.00 USD | 220.09 USD | 0.00 USD | `+10.20%` | `3.57` |
| `Live` | `Short` | `62.95` | 223,330.00 USD | 138.49 USD | 0.00 USD | `+12.53%` | `2.20` |
| `Live` | `Short` | `63.45` | 226,680.00 USD | 3,350.00 USD | 0.00 USD | `+13.42%` | `52.83` |
| `Live` | `Short` | `63.55` | 234,860.00 USD | 8,180.00 USD | 0.00 USD | `+13.60%` | `128.67` |
| `Live` | `Short` | `67.05` | 234,980.00 USD | 121.36 USD | 0.00 USD | `+19.85%` | `1.81` |
| `Live` | `Short` | `67.85` | 235,690.00 USD | 709.03 USD | 0.00 USD | `+21.28%` | `10.45` |
| `Live` | `Short` | `70.75` | 276,590.00 USD | 40,900.00 USD | 0.00 USD | `+26.47%` | `578.10` |
| `Live` | `Short` | `71.35` | 276,700.00 USD | 112.02 USD | 0.00 USD | `+27.54%` | `1.57` |
| `Live` | `Short` | `76.35` | 285,080.00 USD | 8,380.00 USD | 0.00 USD | `+36.48%` | `109.80` |
| `Live` | `Short` | `77.75` | 863,550.00 USD | 578,460.00 USD | 0.00 USD | `+38.98%` | `7,440.05` |
| `Live` | `Short` | `77.85` | 864,150.00 USD | 602.56 USD | 0.00 USD | `+39.16%` | `7.74` |
| `Live` | `Short` | `77.95` | 864,250.00 USD | 102.89 USD | 0.00 USD | `+39.34%` | `1.32` |
| `Live` | `Short` | `80.75` | 868,130.00 USD | 3,880.00 USD | 0.00 USD | `+44.34%` | `48.00` |
| `Live` | `Short` | `81.05` | 887,130.00 USD | 19,000.00 USD | 0.00 USD | `+44.88%` | `234.42` |
| `Live` | `Short` | `81.55` | 887,250.00 USD | 123.96 USD | 0.00 USD | `+45.77%` | `1.52` |
| `Live` | `Short` | `82.75` | 887,470.00 USD | 214.32 USD | 0.00 USD | `+47.92%` | `2.59` |
| `Live` | `Short` | `84.65` | 890,260.00 USD | 2,790.00 USD | 0.00 USD | `+51.31%` | `33.00` |
| `Live` | `Short` | `86.05` | 913,220.00 USD | 22,960.00 USD | 0.00 USD | `+53.82%` | `266.81` |
| `Live` | `Short` | `86.85` | 914,140.00 USD | 923.22 USD | 0.00 USD | `+55.25%` | `10.63` |
| `Live` | `Short` | `88.85` | 914,950.00 USD | 805.87 USD | 0.00 USD | `+58.82%` | `9.07` |
| `Live` | `Short` | `90.65` | 915,070.00 USD | 119.66 USD | 0.00 USD | `+62.04%` | `1.32` |
| `Live` | `Short` | `97.65` | 915,230.00 USD | 165.03 USD | 0.00 USD | `+74.55%` | `1.69` |
| `Live` | `Short` | `98.05` | 917,680.00 USD | 2,450.00 USD | 0.00 USD | `+75.27%` | `25.00` |
| `Live` | `Short` | `104.25` | 917,900.00 USD | 213.71 USD | 0.00 USD | `+86.35%` | `2.05` |
| `Live` | `Short` | `104.65` | 949,290.00 USD | 31,390.00 USD | 0.00 USD | `+87.07%` | `300.00` |
| `Live` | `Short` | `104.85` | 951,610.00 USD | 2,320.00 USD | 0.00 USD | `+87.42%` | `22.13` |
| `Live` | `Short` | `105.45` | 1,310,000.00 USD | 355,790.00 USD | 0.00 USD | `+88.50%` | `3,374.01` |
| `Live` | `Short` | `106.75` | 1,310,000.00 USD | 1,620.00 USD | 0.00 USD | `+90.82%` | `15.16` |
| `Live` | `Short` | `106.85` | 1,310,000.00 USD | 1,860.00 USD | 0.00 USD | `+91.00%` | `17.43` |
| `Live` | `Short` | `107.15` | 1,310,000.00 USD | 199.30 USD | 0.00 USD | `+91.53%` | `1.86` |
| `Live` | `Short` | `108.05` | 1,320,000.00 USD | 6,470.00 USD | 0.00 USD | `+93.14%` | `59.91` |
| `Live` | `Short` | `110.95` | 1,320,000.00 USD | 664.59 USD | 0.00 USD | `+98.33%` | `5.99` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 870,170.00 USD | 0.00 USD | 392.18 USD | `-64.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 869,780.00 USD | 0.00 USD | 2,310.00 USD | `-60.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 867,470.00 USD | 0.00 USD | 806.86 USD | `-55.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 866,660.00 USD | 0.00 USD | 1,560.00 USD | `-54.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 865,110.00 USD | 0.00 USD | 410.25 USD | `-51.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 864,700.00 USD | 0.00 USD | 281.57 USD | `-46.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 864,410.00 USD | 0.00 USD | 36,050.00 USD | `-35.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 828,360.00 USD | 0.00 USD | 37,550.00 USD | `-32.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 790,810.00 USD | 0.00 USD | 447.01 USD | `-32.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.35` | 790,370.00 USD | 0.00 USD | 73,350.00 USD | `-31.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 717,020.00 USD | 0.00 USD | 40,560.00 USD | `-30.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 676,460.00 USD | 0.00 USD | 489.57 USD | `-29.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 675,970.00 USD | 0.00 USD | 1,180.00 USD | `-28.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 674,790.00 USD | 0.00 USD | 9,840.00 USD | `-28.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 664,950.00 USD | 0.00 USD | 2,060.00 USD | `-26.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.05` | 662,900.00 USD | 0.00 USD | 2,060.00 USD | `-26.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 660,840.00 USD | 0.00 USD | 2,960.00 USD | `-25.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 657,880.00 USD | 0.00 USD | 4,010.00 USD | `-24.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.65` | 653,870.00 USD | 0.00 USD | 3,000.00 USD | `-23.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 650,860.00 USD | 0.00 USD | 5,680.00 USD | `-23.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 645,180.00 USD | 0.00 USD | 672.22 USD | `-21.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.35` | 644,510.00 USD | 0.00 USD | 329,970.00 USD | `-20.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 314,550.00 USD | 0.00 USD | 569.85 USD | `-20.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 313,980.00 USD | 0.00 USD | 223.20 USD | `-20.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 313,750.00 USD | 0.00 USD | 391.13 USD | `-20.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 313,360.00 USD | 0.00 USD | 7,080.00 USD | `-19.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 306,280.00 USD | 0.00 USD | 1,370.00 USD | `-18.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 304,920.00 USD | 0.00 USD | 553.80 USD | `-17.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.35` | 304,360.00 USD | 0.00 USD | 2,970.00 USD | `-17.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.45` | 301,390.00 USD | 0.00 USD | 3,080.00 USD | `-16.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 298,320.00 USD | 0.00 USD | 14,000.00 USD | `-16.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 284,320.00 USD | 0.00 USD | 158.56 USD | `-15.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 284,160.00 USD | 0.00 USD | 373.28 USD | `-15.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 283,790.00 USD | 0.00 USD | 849.46 USD | `-15.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 282,940.00 USD | 0.00 USD | 1,150.00 USD | `-14.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 281,790.00 USD | 0.00 USD | 129.25 USD | `-14.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.15` | 281,660.00 USD | 0.00 USD | 303.35 USD | `-13.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 281,360.00 USD | 0.00 USD | 1,740.00 USD | `-12.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 279,620.00 USD | 0.00 USD | 981.00 USD | `-12.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.35` | 278,640.00 USD | 0.00 USD | 817.24 USD | `-11.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 277,820.00 USD | 0.00 USD | 237.85 USD | `-11.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.55` | 277,580.00 USD | 0.00 USD | 879.51 USD | `-11.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.85` | 276,700.00 USD | 0.00 USD | 108.17 USD | `-10.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 276,590.00 USD | 0.00 USD | 298.20 USD | `-10.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 276,290.00 USD | 0.00 USD | 35,050.00 USD | `-10.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 241,250.00 USD | 0.00 USD | 6,410.00 USD | `-10.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 234,830.00 USD | 0.00 USD | 459.70 USD | `-10.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 234,370.00 USD | 0.00 USD | 236.57 USD | `-9.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 234,140.00 USD | 0.00 USD | 1,020.00 USD | `-8.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 233,120.00 USD | 0.00 USD | 439.89 USD | `-8.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.45` | 232,680.00 USD | 0.00 USD | 204.26 USD | `-8.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 232,470.00 USD | 0.00 USD | 11,560.00 USD | `-7.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.85` | 220,910.00 USD | 0.00 USD | 106.29 USD | `-7.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.95` | 220,810.00 USD | 0.00 USD | 8,700.00 USD | `-7.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 212,100.00 USD | 0.00 USD | 27,140.00 USD | `-6.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.25` | 184,970.00 USD | 0.00 USD | 140.03 USD | `-6.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 184,830.00 USD | 0.00 USD | 18,390.00 USD | `-6.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 166,430.00 USD | 0.00 USD | 5,460.00 USD | `-5.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 160,980.00 USD | 0.00 USD | 53,020.00 USD | `-5.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.85` | 107,950.00 USD | 0.00 USD | 2,840.00 USD | `-5.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 105,110.00 USD | 0.00 USD | 115.43 USD | `-5.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 105,000.00 USD | 0.00 USD | 15,140.00 USD | `-5.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 89,850.00 USD | 0.00 USD | 2,660.00 USD | `-4.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.25` | 87,200.00 USD | 0.00 USD | 881.82 USD | `-4.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 86,320.00 USD | 0.00 USD | 566.57 USD | `-4.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 85,750.00 USD | 0.00 USD | 5,950.00 USD | `-4.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 79,800.00 USD | 0.00 USD | 1,370.00 USD | `-4.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.75` | 78,430.00 USD | 0.00 USD | 52,980.00 USD | `-3.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 25,450.00 USD | 0.00 USD | 462.03 USD | `-3.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 24,990.00 USD | 0.00 USD | 895.07 USD | `-3.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.15` | 24,090.00 USD | 0.00 USD | 398.54 USD | `-3.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 23,690.00 USD | 0.00 USD | 3,090.00 USD | `-3.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 20,600.00 USD | 0.00 USD | 958.73 USD | `-2.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.45` | 19,650.00 USD | 0.00 USD | 144.29 USD | `-2.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.55` | 19,500.00 USD | 0.00 USD | 788.25 USD | `-2.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.65` | 18,710.00 USD | 0.00 USD | 13,660.00 USD | `-2.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.75` | 5,050.00 USD | 0.00 USD | 198.74 USD | `-2.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 4,850.00 USD | 0.00 USD | 398.21 USD | `-1.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.95` | 4,450.00 USD | 0.00 USD | 909.97 USD | `-1.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 3,540.00 USD | 0.00 USD | 160.75 USD | `-1.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.15` | 3,380.00 USD | 0.00 USD | 101.48 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.25` | 3,280.00 USD | 0.00 USD | 914.94 USD | `-1.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.35` | 2,370.00 USD | 0.00 USD | 407.38 USD | `-1.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.45` | 1,960.00 USD | 0.00 USD | 408.11 USD | `-0.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.55` | 1,550.00 USD | 0.00 USD | 156.65 USD | `-0.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.65` | 1,390.00 USD | 0.00 USD | 198.67 USD | `-0.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.75` | 1,200.00 USD | 0.00 USD | 398.06 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.85` | 797.54 USD | 0.00 USD | 797.54 USD | `-0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.95` | 193.03 USD | 193.03 USD | 0.00 USD | `+0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.05` | 825.27 USD | 632.24 USD | 0.00 USD | `+0.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.15` | 1,020.00 USD | 197.65 USD | 0.00 USD | `+0.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.25` | 1,230.00 USD | 204.19 USD | 0.00 USD | `+0.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.35` | 1,610.00 USD | 387.12 USD | 0.00 USD | `+0.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.45` | 2,020.00 USD | 407.57 USD | 0.00 USD | `+0.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.55` | 4,660.00 USD | 2,640.00 USD | 0.00 USD | `+1.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.65` | 4,780.00 USD | 121.23 USD | 0.00 USD | `+1.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.75` | 4,890.00 USD | 104.42 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.85` | 22,910.00 USD | 18,030.00 USD | 0.00 USD | `+1.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.95` | 23,730.00 USD | 813.25 USD | 0.00 USD | `+1.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.05` | 24,730.00 USD | 1,000.00 USD | 0.00 USD | `+1.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.15` | 24,930.00 USD | 204.03 USD | 0.00 USD | `+2.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.25` | 26,370.00 USD | 1,440.00 USD | 0.00 USD | `+2.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.35` | 26,580.00 USD | 207.03 USD | 0.00 USD | `+2.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.45` | 26,920.00 USD | 344.70 USD | 0.00 USD | `+2.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.55` | 47,280.00 USD | 20,360.00 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.65` | 47,400.00 USD | 118.18 USD | 0.00 USD | `+3.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.75` | 47,520.00 USD | 119.54 USD | 0.00 USD | `+3.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 48,270.00 USD | 747.68 USD | 0.00 USD | `+3.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 48,470.00 USD | 200.04 USD | 0.00 USD | `+3.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 48,670.00 USD | 200.96 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 48,790.00 USD | 123.70 USD | 0.00 USD | `+4.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 49,400.00 USD | 601.45 USD | 0.00 USD | `+4.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 50,010.00 USD | 611.85 USD | 0.00 USD | `+4.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.65` | 50,280.00 USD | 274.48 USD | 0.00 USD | `+4.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 50,770.00 USD | 491.15 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 53,720.00 USD | 2,940.00 USD | 0.00 USD | `+5.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 53,850.00 USD | 129.69 USD | 0.00 USD | `+5.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 58,640.00 USD | 4,800.00 USD | 0.00 USD | `+5.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 59,920.00 USD | 1,280.00 USD | 0.00 USD | `+5.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.25` | 60,130.00 USD | 210.34 USD | 0.00 USD | `+5.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 60,600.00 USD | 461.74 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 60,760.00 USD | 159.92 USD | 0.00 USD | `+6.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 61,480.00 USD | 724.75 USD | 0.00 USD | `+6.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 61,640.00 USD | 158.00 USD | 0.00 USD | `+6.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 61,810.00 USD | 171.14 USD | 0.00 USD | `+7.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 62,360.00 USD | 551.00 USD | 0.00 USD | `+7.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.45` | 62,520.00 USD | 155.36 USD | 0.00 USD | `+8.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 63,390.00 USD | 878.58 USD | 0.00 USD | `+8.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 64,780.00 USD | 1,390.00 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 65,770.00 USD | 986.99 USD | 0.00 USD | `+8.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 66,440.00 USD | 674.72 USD | 0.00 USD | `+8.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 68,810.00 USD | 2,360.00 USD | 0.00 USD | `+9.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 68,930.00 USD | 125.56 USD | 0.00 USD | `+9.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 72,530.00 USD | 3,600.00 USD | 0.00 USD | `+9.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 73,170.00 USD | 643.20 USD | 0.00 USD | `+10.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 73,300.00 USD | 130.31 USD | 0.00 USD | `+10.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.35` | 74,400.00 USD | 1,100.00 USD | 0.00 USD | `+11.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 75,120.00 USD | 716.72 USD | 0.00 USD | `+11.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 75,350.00 USD | 231.39 USD | 0.00 USD | `+12.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 75,980.00 USD | 630.87 USD | 0.00 USD | `+12.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 76,680.00 USD | 703.97 USD | 0.00 USD | `+13.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 77,350.00 USD | 668.13 USD | 0.00 USD | `+13.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 87,770.00 USD | 10,420.00 USD | 0.00 USD | `+13.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 88,330.00 USD | 555.03 USD | 0.00 USD | `+13.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 88,860.00 USD | 531.62 USD | 0.00 USD | `+14.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.35` | 89,520.00 USD | 664.09 USD | 0.00 USD | `+15.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.45` | 90,190.00 USD | 665.12 USD | 0.00 USD | `+15.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 90,390.00 USD | 202.69 USD | 0.00 USD | `+15.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 90,690.00 USD | 298.04 USD | 0.00 USD | `+15.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 90,790.00 USD | 102.13 USD | 0.00 USD | `+16.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 91,330.00 USD | 540.09 USD | 0.00 USD | `+16.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 91,430.00 USD | 100.79 USD | 0.00 USD | `+16.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 91,690.00 USD | 262.20 USD | 0.00 USD | `+17.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 92,070.00 USD | 371.49 USD | 0.00 USD | `+17.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 92,760.00 USD | 696.17 USD | 0.00 USD | `+18.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 93,300.00 USD | 534.00 USD | 0.00 USD | `+19.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 104,380.00 USD | 11,080.00 USD | 0.00 USD | `+19.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 111,080.00 USD | 6,710.00 USD | 0.00 USD | `+19.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.05` | 113,440.00 USD | 2,360.00 USD | 0.00 USD | `+21.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 118,300.00 USD | 4,860.00 USD | 0.00 USD | `+22.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 118,510.00 USD | 204.48 USD | 0.00 USD | `+24.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.65` | 636,710.00 USD | 518,200.00 USD | 0.00 USD | `+24.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 637,520.00 USD | 810.02 USD | 0.00 USD | `+25.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 957,410.00 USD | 319,890.00 USD | 0.00 USD | `+25.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 957,580.00 USD | 170.04 USD | 0.00 USD | `+26.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 963,350.00 USD | 5,770.00 USD | 0.00 USD | `+26.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 963,620.00 USD | 269.28 USD | 0.00 USD | `+27.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 963,910.00 USD | 291.40 USD | 0.00 USD | `+28.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 971,130.00 USD | 7,220.00 USD | 0.00 USD | `+28.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 971,280.00 USD | 156.78 USD | 0.00 USD | `+29.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 974,500.00 USD | 3,220.00 USD | 0.00 USD | `+29.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 974,920.00 USD | 411.14 USD | 0.00 USD | `+31.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 1,100,000.00 USD | 123,190.00 USD | 0.00 USD | `+32.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 1,100,000.00 USD | 1,020.00 USD | 0.00 USD | `+33.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.75` | 1,100,000.00 USD | 811.04 USD | 0.00 USD | `+33.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 1,100,000.00 USD | 104.93 USD | 0.00 USD | `+33.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 1,100,000.00 USD | 133.59 USD | 0.00 USD | `+34.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 1,100,000.00 USD | 402.59 USD | 0.00 USD | `+34.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.85` | 1,100,000.00 USD | 308.71 USD | 0.00 USD | `+35.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 1,100,000.00 USD | 315.18 USD | 0.00 USD | `+38.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 1,160,000.00 USD | 59,310.00 USD | 0.00 USD | `+40.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 1,160,000.00 USD | 3,160.00 USD | 0.00 USD | `+41.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.35` | 1,170,000.00 USD | 5,260.00 USD | 0.00 USD | `+41.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 1,170,000.00 USD | 5,690.00 USD | 0.00 USD | `+42.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 1,210,000.00 USD | 36,590.00 USD | 0.00 USD | `+43.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 1,210,000.00 USD | 433.89 USD | 0.00 USD | `+44.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 1,210,000.00 USD | 172.64 USD | 0.00 USD | `+44.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 1,210,000.00 USD | 164.10 USD | 0.00 USD | `+46.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 1,210,000.00 USD | 546.81 USD | 0.00 USD | `+48.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 1,210,000.00 USD | 2,300.00 USD | 0.00 USD | `+50.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 1,230,000.00 USD | 12,070.00 USD | 0.00 USD | `+52.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.05` | 1,250,000.00 USD | 20,230.00 USD | 0.00 USD | `+55.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 1,250,000.00 USD | 1,580.00 USD | 0.00 USD | `+57.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 1,290,000.00 USD | 37,000.00 USD | 0.00 USD | `+57.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 1,290,000.00 USD | 473.21 USD | 0.00 USD | `+59.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 1,290,000.00 USD | 422.99 USD | 0.00 USD | `+59.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 1,290,000.00 USD | 1,630.00 USD | 0.00 USD | `+59.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 1,290,000.00 USD | 4,870.00 USD | 0.00 USD | `+60.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 1,290,000.00 USD | 481.55 USD | 0.00 USD | `+63.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 1,290,000.00 USD | 1,330.00 USD | 0.00 USD | `+64.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 1,300,000.00 USD | 281.21 USD | 0.00 USD | `+68.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,560,000.00 USD | 266,140.00 USD | 0.00 USD | `+69.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,560,000.00 USD | 3,400.00 USD | 0.00 USD | `+70.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,590,000.00 USD | 21,930.00 USD | 0.00 USD | `+71.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,590,000.00 USD | 294.15 USD | 0.00 USD | `+75.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 1,600,000.00 USD | 15,380.00 USD | 0.00 USD | `+77.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,610,000.00 USD | 3,660.00 USD | 0.00 USD | `+78.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,610,000.00 USD | 306.15 USD | 0.00 USD | `+82.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,610,000.00 USD | 936.72 USD | 0.00 USD | `+84.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,610,000.00 USD | 2,920.00 USD | 0.00 USD | `+84.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,610,000.00 USD | 324.15 USD | 0.00 USD | `+93.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 1,610,000.00 USD | 123.23 USD | 0.00 USD | `+94.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 1,700,000.00 USD | 89,110.00 USD | 0.00 USD | `+98.51%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `47.20` | 8,540,000.00 USD | 0.00 USD | 8,540,000.00 USD | 9,650.00 USD | 2,470.00 USD | 114.09 USD |
| `7D` | `47.30` | 8,530,000.00 USD | 0.00 USD | 8,530,000.00 USD | 692.33 USD | 4,740.00 USD | 6,740.00 USD |
| `7D` | `47.40` | 8,510,000.00 USD | 0.00 USD | 8,510,000.00 USD | 0.00 USD | 1,520.00 USD | 28,650.00 USD |
| `7D` | `47.50` | 8,480,000.00 USD | 0.00 USD | 8,480,000.00 USD | 11,830.00 USD | 0.00 USD | 7,960.00 USD |
| `7D` | `48.10` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD |
| `7D` | `48.20` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD |
| `7D` | `48.40` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 0.00 USD | 6,080.00 USD | 0.00 USD |
| `7D` | `48.60` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `48.80` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 1,780.00 USD | 2,250.00 USD | 0.00 USD |
| `7D` | `48.90` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 0.00 USD | 0.00 USD | 960.40 USD |
| `7D` | `49.30` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 15,190.00 USD | 4,490.00 USD | 14,870.00 USD |
| `7D` | `49.40` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD |
| `7D` | `49.50` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 2,830.00 USD | 7,770.00 USD | 0.00 USD |
| `7D` | `49.60` | 8,390,000.00 USD | 0.00 USD | 8,390,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD |
| `7D` | `49.70` | 8,370,000.00 USD | 0.00 USD | 8,370,000.00 USD | 12,090.00 USD | 0.00 USD | 5,410.00 USD |
| `7D` | `49.80` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 9,930.00 USD | 8,220.00 USD | 0.00 USD |
| `7D` | `49.90` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 45,030.00 USD | 7,170.00 USD | 4,700.00 USD |
| `7D` | `50.00` | 8,280,000.00 USD | 0.00 USD | 8,280,000.00 USD | 22,100.00 USD | 7,630.00 USD | 24,920.00 USD |
| `1D` | `50.10` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 11,930.00 USD | 13,980.00 USD | 48,560.00 USD |
| `7D` | `50.10` | 8,220,000.00 USD | 0.00 USD | 8,220,000.00 USD | 363.50 USD | 682.90 USD | 8,340.00 USD |
| `1D` | `50.20` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 177.10 USD | 709.61 USD | 5,230.00 USD |
| `7D` | `50.20` | 8,210,000.00 USD | 0.00 USD | 8,210,000.00 USD | 6,960.00 USD | 500.40 USD | 42,940.00 USD |
| `1D` | `50.30` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 171.03 USD | 3,880.00 USD | 2,500.00 USD |
| `7D` | `50.30` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 16,270.00 USD | 10,780.00 USD | 7,240.00 USD |
| `1D` | `50.40` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 8,260.00 USD | 11,890.00 USD | 1,150.00 USD |
| `7D` | `50.40` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 28,280.00 USD | 26,580.00 USD | 33,450.00 USD |
| `1D` | `50.50` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 8,910.00 USD | 8,790.00 USD | 10,530.00 USD |
| `7D` | `50.50` | 8,040,000.00 USD | 0.00 USD | 8,040,000.00 USD | 32,490.00 USD | 6,790.00 USD | 44,380.00 USD |
| `1D` | `50.60` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 7,330.00 USD | 3,440.00 USD | 10,850.00 USD |
| `7D` | `50.60` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 67,580.00 USD | 21,530.00 USD | 31,730.00 USD |
| `1D` | `50.70` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 8,170.00 USD | 2,300.00 USD | 11,770.00 USD |
| `7D` | `50.70` | 7,840,000.00 USD | 0.00 USD | 7,840,000.00 USD | 65,920.00 USD | 32,820.00 USD | 41,580.00 USD |
| `1D` | `50.80` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 12,550.00 USD | 3,100.00 USD | 8,280.00 USD |
| `7D` | `50.80` | 7,700,000.00 USD | 0.00 USD | 7,700,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD |
| `1D` | `50.90` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 826.24 USD | 260.05 USD | 8,390.00 USD |
| `7D` | `50.90` | 7,600,000.00 USD | 0.00 USD | 7,600,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD |
| `1D` | `51.00` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 5,040.00 USD | 0.00 USD | 430.77 USD |
| `7D` | `51.00` | 7,350,000.00 USD | 0.00 USD | 7,350,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `51.10` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 9,210.00 USD | 6,650.00 USD | 0.00 USD |
| `7D` | `51.10` | 7,220,000.00 USD | 0.00 USD | 7,220,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD |
| `1D` | `51.20` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 1,770.00 USD | 1,130.00 USD | 19,220.00 USD |
| `7D` | `51.20` | 7,140,000.00 USD | 0.00 USD | 7,140,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD |
| `1D` | `51.30` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 13,550.00 USD | 10,730.00 USD | 5,560.00 USD |
| `7D` | `51.30` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 28,400.00 USD | 26,720.00 USD | 47,090.00 USD |
| `1D` | `51.40` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 7,350.00 USD | 6,840.00 USD | 4,080.00 USD |
| `7D` | `51.40` | 6,970,000.00 USD | 0.00 USD | 6,970,000.00 USD | 73,130.00 USD | 42,820.00 USD | 46,140.00 USD |
| `1D` | `51.50` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 5,650.00 USD | 11,190.00 USD | 41,600.00 USD |
| `7D` | `51.50` | 6,810,000.00 USD | 0.00 USD | 6,810,000.00 USD | 38,520.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `51.60` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 9,060.00 USD | 18,580.00 USD | 757.87 USD |
| `7D` | `51.60` | 6,710,000.00 USD | 0.00 USD | 6,710,000.00 USD | 37,880.00 USD | 36,790.00 USD | 41,490.00 USD |
| `1D` | `51.70` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 2,890.00 USD | 13,780.00 USD | 4,100.00 USD |
| `7D` | `51.70` | 6,600,000.00 USD | 0.00 USD | 6,600,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `51.80` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 12,590.00 USD | 19,520.00 USD | 14,360.00 USD |
| `7D` | `51.80` | 6,560,000.00 USD | 0.00 USD | 6,560,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD |
| `1D` | `51.90` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 9,590.00 USD | 19,910.00 USD | 23,480.00 USD |
| `7D` | `51.90` | 6,500,000.00 USD | 0.00 USD | 6,500,000.00 USD | 5,870.00 USD | 25,410.00 USD | 28,190.00 USD |
| `1D` | `52.00` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 20,980.00 USD | 25,620.00 USD | 24,820.00 USD |
| `7D` | `52.00` | 6,440,000.00 USD | 0.00 USD | 6,440,000.00 USD | 65,840.00 USD | 26,440.00 USD | 11,880.00 USD |
| `1D` | `52.10` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 34,970.00 USD | 17,300.00 USD | 50,500.00 USD |
| `7D` | `52.10` | 6,340,000.00 USD | 0.00 USD | 6,340,000.00 USD | 24,220.00 USD | 28,090.00 USD | 37,880.00 USD |
| `1D` | `52.20` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 15,890.00 USD | 7,630.00 USD | 49,960.00 USD |
| `7D` | `52.20` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 38,380.00 USD | 13,960.00 USD | 25,270.00 USD |
| `1D` | `52.30` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 26,510.00 USD | 22,090.00 USD | 11,210.00 USD |
| `7D` | `52.30` | 6,170,000.00 USD | 0.00 USD | 6,170,000.00 USD | 26,450.00 USD | 40,700.00 USD | 7,980.00 USD |
| `1D` | `52.40` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 13,070.00 USD | 15,400.00 USD | 7,040.00 USD |
| `7D` | `52.40` | 6,100,000.00 USD | 0.00 USD | 6,100,000.00 USD | 20,580.00 USD | 38,950.00 USD | 22,030.00 USD |
| `1D` | `52.50` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 53,990.00 USD | 30,000.00 USD | 79,400.00 USD |
| `7D` | `52.50` | 6,010,000.00 USD | 0.00 USD | 6,010,000.00 USD | 40,460.00 USD | 667.05 USD | 11,240.00 USD |
| `1D` | `52.60` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 8,330.00 USD | 43,700.00 USD | 5,450.00 USD |
| `7D` | `52.60` | 5,960,000.00 USD | 0.00 USD | 5,960,000.00 USD | 73,920.00 USD | 32,590.00 USD | 59,410.00 USD |
| `1D` | `52.70` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 16,690.00 USD | 19,780.00 USD | 40,000.00 USD |
| `7D` | `52.70` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 20,250.00 USD | 84,940.00 USD | 108,640.00 USD |
| `1D` | `52.80` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 27,260.00 USD | 50,850.00 USD | 72,920.00 USD |
| `7D` | `52.80` | 5,580,000.00 USD | 0.00 USD | 5,580,000.00 USD | 30,590.00 USD | 25,700.00 USD | 0.00 USD |
| `1D` | `52.90` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 43,760.00 USD | 50,880.00 USD | 30,100.00 USD |
| `7D` | `52.90` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 30,900.00 USD | 11,650.00 USD | 34,400.00 USD |
| `1D` | `53.00` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 26,800.00 USD | 30,500.00 USD | 39,600.00 USD |
| `7D` | `53.00` | 5,450,000.00 USD | 0.00 USD | 5,450,000.00 USD | 39,690.00 USD | 22,700.00 USD | 77,700.00 USD |
| `1D` | `53.10` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 13,270.00 USD | 43,040.00 USD | 85,170.00 USD |
| `7D` | `53.10` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 45,320.00 USD | 17,950.00 USD | 0.00 USD |
| `1D` | `53.20` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 21,040.00 USD | 6,510.00 USD | 42,060.00 USD |
| `7D` | `53.20` | 5,240,000.00 USD | 0.00 USD | 5,240,000.00 USD | 162,460.00 USD | 28,320.00 USD | 23,350.00 USD |
| `1D` | `53.30` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 2,690.00 USD | 0.00 USD | 5,610.00 USD |
| `7D` | `53.30` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 59,390.00 USD | 24,540.00 USD | 35,070.00 USD |
| `1D` | `53.40` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 4,130.00 USD | 2,880.00 USD | 4,500.00 USD |
| `7D` | `53.40` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 44,030.00 USD | 7,250.00 USD | 91,220.00 USD |
| `1D` | `53.50` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 9,960.00 USD | 5,700.00 USD | 22,000.00 USD |
| `7D` | `53.50` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 50,990.00 USD | 3,440.00 USD | 28,500.00 USD |
| `1D` | `53.60` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 75,950.00 USD | 3,830.00 USD | 20,970.00 USD |
| `7D` | `53.60` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 52,800.00 USD | 3,780.00 USD | 20,660.00 USD |
| `1D` | `53.70` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 6,210.00 USD | 11,100.00 USD | 11,960.00 USD |
| `7D` | `53.70` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 131,400.00 USD | 21,330.00 USD | 13,220.00 USD |
| `1D` | `53.80` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 53,640.00 USD | 28,920.00 USD | 4,830.00 USD |
| `7D` | `53.80` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 99,150.00 USD | 43,900.00 USD | 302.55 USD |
| `1D` | `53.90` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 51,060.00 USD | 39,560.00 USD | 27,830.00 USD |
| `7D` | `53.90` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 160,820.00 USD | 22,780.00 USD | 9,680.00 USD |
| `1D` | `54.00` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 76,010.00 USD | 21,440.00 USD | 86,580.00 USD |
| `7D` | `54.00` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 380,340.00 USD | 71,820.00 USD | 304,530.00 USD |
| `1D` | `54.10` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 95,780.00 USD | 19,160.00 USD | 49,170.00 USD |
| `7D` | `54.10` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 302,190.00 USD | 0.00 USD | 2,590.00 USD |
| `1D` | `54.20` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 72,600.00 USD | 15,510.00 USD | 40,120.00 USD |
| `7D` | `54.20` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 205,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `54.30` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 15,600.00 USD | 0.00 USD | 5,350.00 USD |
| `7D` | `54.30` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 381,380.00 USD | 0.00 USD | 181,420.00 USD |
| `1D` | `54.40` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 51,570.00 USD | 35,500.00 USD | 3,130.00 USD |
| `7D` | `54.40` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 304,270.00 USD | 13,830.00 USD | 92,650.00 USD |
| `1D` | `54.50` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 9,670.00 USD | 48,740.00 USD | 8,990.00 USD |
| `7D` | `54.50` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 159,720.00 USD | 15,240.00 USD | 239,890.00 USD |
| `1D` | `54.60` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 913.17 USD | 25,490.00 USD | 43,580.00 USD |
| `7D` | `54.60` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | 1,930.00 USD | 131,380.00 USD |
| `1D` | `54.70` | 968,480.00 USD | 0.00 USD | 968,480.00 USD | 6,600.00 USD | 23,060.00 USD | 105,800.00 USD |
| `7D` | `54.70` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 0.00 USD | 3,600.00 USD | 41,310.00 USD |
| `1D` | `54.80` | 833,020.00 USD | 0.00 USD | 833,020.00 USD | 0.00 USD | 48,420.00 USD | 23,920.00 USD |
| `7D` | `54.80` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 35,700.00 USD | 26,440.00 USD |
| `1D` | `54.90` | 760,680.00 USD | 0.00 USD | 760,680.00 USD | 66,900.00 USD | 65,440.00 USD | 10,850.00 USD |
| `7D` | `54.90` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 0.00 USD | 112,280.00 USD | 48,290.00 USD |
| `1D` | `55.00` | 617,490.00 USD | 0.00 USD | 617,490.00 USD | 40,710.00 USD | 54,150.00 USD | 55,190.00 USD |
| `7D` | `55.00` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 97,700.00 USD | 2,830.00 USD | 19,360.00 USD |
| `1D` | `55.10` | 467,440.00 USD | 0.00 USD | 467,440.00 USD | 50,530.00 USD | 62,170.00 USD | 80,200.00 USD |
| `7D` | `55.10` | 930,880.00 USD | 0.00 USD | 930,880.00 USD | 54,590.00 USD | 18,510.00 USD | 64,690.00 USD |
| `1D` | `55.20` | 274,540.00 USD | 0.00 USD | 274,540.00 USD | 39,390.00 USD | 11,830.00 USD | 66,410.00 USD |
| `7D` | `55.20` | 793,100.00 USD | 0.00 USD | 793,100.00 USD | 57,400.00 USD | 59,710.00 USD | 150,160.00 USD |
| `1D` | `55.30` | 156,920.00 USD | 0.00 USD | 156,920.00 USD | 52,860.00 USD | 22,650.00 USD | 59,180.00 USD |
| `7D` | `55.30` | 525,820.00 USD | 0.00 USD | 525,820.00 USD | 23,140.00 USD | 11,270.00 USD | 0.00 USD |
| `1D` | `55.40` | 22,230.00 USD | 0.00 USD | 22,230.00 USD | 0.00 USD | 6,510.00 USD | 742.75 USD |
| `7D` | `55.40` | 491,410.00 USD | 0.00 USD | 491,410.00 USD | 0.00 USD | 18,550.00 USD | 4,800.00 USD |
| `1D` | `55.50` | 14,980.00 USD | 0.00 USD | 14,980.00 USD | 0.00 USD | 9,480.00 USD | 5,500.00 USD |
| `7D` | `55.50` | 468,060.00 USD | 0.00 USD | 468,060.00 USD | 0.00 USD | 33,460.00 USD | 0.00 USD |
| `7D` | `55.60` | 434,600.00 USD | 0.00 USD | 434,600.00 USD | 420,740.00 USD | 13,860.00 USD | 0.00 USD |
| `1D` | `55.70` | 8,310.00 USD | 8,310.00 USD | 0.00 USD | 0.00 USD | 7,700.00 USD | 613.46 USD |
| `1D` | `55.70` | 16,630.00 USD | 16,630.00 USD | 0.00 USD | 0.00 USD | 7,700.00 USD | 613.46 USD |
| `7D` | `55.70` | 206,420.00 USD | 206,420.00 USD | 0.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD |
| `7D` | `55.70` | 412,850.00 USD | 412,850.00 USD | 0.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD |
| `1D` | `55.80` | 19,800.00 USD | 19,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,170.00 USD |
| `7D` | `55.80` | 503,810.00 USD | 503,810.00 USD | 0.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD |
| `1D` | `55.90` | 100,330.00 USD | 100,330.00 USD | 0.00 USD | 78,980.00 USD | 0.00 USD | 1,550.00 USD |
| `7D` | `55.90` | 645,140.00 USD | 645,140.00 USD | 0.00 USD | 141,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `56.00` | 104,710.00 USD | 104,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,380.00 USD |
| `7D` | `56.00` | 816,260.00 USD | 816,260.00 USD | 0.00 USD | 2,590.00 USD | 0.00 USD | 168,520.00 USD |
| `7D` | `56.20` | 896,200.00 USD | 896,200.00 USD | 0.00 USD | 0.00 USD | 79,940.00 USD | 0.00 USD |
| `1D` | `56.30` | 108,660.00 USD | 108,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,950.00 USD |
| `7D` | `56.30` | 898,790.00 USD | 898,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,590.00 USD |
| `1D` | `56.40` | 132,990.00 USD | 132,990.00 USD | 0.00 USD | 5,040.00 USD | 16,820.00 USD | 2,470.00 USD |
| `7D` | `56.40` | 912,480.00 USD | 912,480.00 USD | 0.00 USD | 2,650.00 USD | 11,040.00 USD | 0.00 USD |
| `1D` | `56.50` | 518,310.00 USD | 518,310.00 USD | 0.00 USD | 138,540.00 USD | 101,980.00 USD | 144,810.00 USD |
| `7D` | `56.50` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 170,750.00 USD | 143,420.00 USD | 6,150.00 USD |
| `1D` | `56.60` | 753,020.00 USD | 753,020.00 USD | 0.00 USD | 49,560.00 USD | 104,240.00 USD | 80,910.00 USD |
| `7D` | `56.60` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 363,190.00 USD | 136,570.00 USD | 507.54 USD |
| `1D` | `56.70` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 97,300.00 USD | 29,790.00 USD | 315,490.00 USD |
| `7D` | `56.70` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 117,290.00 USD | 121,500.00 USD | 98,950.00 USD |
| `1D` | `56.80` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 117,760.00 USD | 20,790.00 USD | 106,140.00 USD |
| `7D` | `56.80` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 153,580.00 USD | 92,780.00 USD | 318,330.00 USD |
| `1D` | `56.90` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 45,140.00 USD | 17,930.00 USD | 35,720.00 USD |
| `7D` | `56.90` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 113,780.00 USD | 52,200.00 USD | 307,930.00 USD |
| `1D` | `57.00` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 6,480.00 USD | 43,030.00 USD | 29,740.00 USD |
| `7D` | `57.00` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 88,680.00 USD | 56,390.00 USD | 178,370.00 USD |
| `1D` | `57.10` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 77,000.00 USD | 77,400.00 USD | 46,610.00 USD |
| `7D` | `57.10` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 36,580.00 USD | 79,290.00 USD | 21,040.00 USD |
| `1D` | `57.20` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 53,080.00 USD | 78,490.00 USD | 120,900.00 USD |
| `7D` | `57.20` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 118,850.00 USD | 23,920.00 USD | 23,060.00 USD |
| `1D` | `57.30` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 70,930.00 USD | 44,630.00 USD | 87,180.00 USD |
| `7D` | `57.30` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 76,940.00 USD | 28,570.00 USD | 98,930.00 USD |
| `1D` | `57.40` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 84,960.00 USD | 49,470.00 USD | 78,400.00 USD |
| `7D` | `57.40` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 124,180.00 USD | 72,180.00 USD | 257,020.00 USD |
| `1D` | `57.50` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 197,830.00 USD | 48,350.00 USD | 174,740.00 USD |
| `7D` | `57.50` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 99,810.00 USD | 31,830.00 USD | 0.00 USD |
| `1D` | `57.60` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 69,720.00 USD | 24,050.00 USD | 62,510.00 USD |
| `7D` | `57.60` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 149,560.00 USD | 40,430.00 USD | 28,320.00 USD |
| `1D` | `57.70` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 36,620.00 USD | 26,070.00 USD | 96,350.00 USD |
| `7D` | `57.70` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 5,400.00 USD | 57,580.00 USD |
| `1D` | `57.80` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 9,690.00 USD | 14,890.00 USD | 77,170.00 USD |
| `7D` | `57.80` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 9,650.00 USD | 14,360.00 USD | 49,480.00 USD |
| `1D` | `57.90` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 13,000.00 USD | 15,870.00 USD | 28,950.00 USD |
| `7D` | `57.90` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 5,120.00 USD | 963.90 USD | 30,010.00 USD |
| `1D` | `58.00` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 7,880.00 USD | 9,480.00 USD | 15,330.00 USD |
| `7D` | `58.00` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD | 107,350.00 USD |
| `1D` | `58.10` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 31,400.00 USD | 17,830.00 USD | 21,300.00 USD |
| `7D` | `58.10` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 5,470.00 USD | 19,160.00 USD | 14,070.00 USD |
| `1D` | `58.20` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 35,920.00 USD | 34,800.00 USD | 4,940.00 USD |
| `7D` | `58.20` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 31,590.00 USD | 302.55 USD |
| `1D` | `58.30` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 31,780.00 USD | 38,620.00 USD | 64,380.00 USD |
| `7D` | `58.30` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 48,850.00 USD | 11,000.00 USD | 36,500.00 USD |
| `1D` | `58.40` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 25,750.00 USD | 18,940.00 USD | 50,160.00 USD |
| `7D` | `58.40` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 27,290.00 USD | 9,260.00 USD | 86,460.00 USD |
| `1D` | `58.50` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 21,130.00 USD | 6,460.00 USD | 124.02 USD |
| `7D` | `58.50` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 2,060.00 USD | 24,530.00 USD | 0.00 USD |
| `1D` | `58.60` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 21,940.00 USD | 5,920.00 USD | 40,890.00 USD |
| `7D` | `58.60` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 30,680.00 USD | 20,260.00 USD | 51,650.00 USD |
| `1D` | `58.70` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 44,920.00 USD | 10,120.00 USD | 29,940.00 USD |
| `7D` | `58.70` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 15,810.00 USD | 11,600.00 USD | 35,320.00 USD |
| `1D` | `58.80` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 36,630.00 USD | 9,890.00 USD | 23,340.00 USD |
| `7D` | `58.80` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD |
| `1D` | `58.90` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 22,130.00 USD | 60,970.00 USD | 90,490.00 USD |
| `7D` | `58.90` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 2,140.00 USD | 54,240.00 USD | 83,500.00 USD |
| `1D` | `59.00` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 129,990.00 USD | 58,870.00 USD | 129,440.00 USD |
| `7D` | `59.00` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 259,280.00 USD | 65,270.00 USD | 118,570.00 USD |
| `1D` | `59.10` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 92,240.00 USD | 39,860.00 USD | 163,590.00 USD |
| `7D` | `59.10` | 6,400,000.00 USD | 6,400,000.00 USD | 0.00 USD | 93,390.00 USD | 45,400.00 USD | 158,780.00 USD |
| `1D` | `59.20` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 101,760.00 USD | 59,450.00 USD | 49,210.00 USD |
| `7D` | `59.20` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 153,580.00 USD | 18,540.00 USD | 174,600.00 USD |
| `1D` | `59.30` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 159,400.00 USD | 34,020.00 USD | 79,950.00 USD |
| `7D` | `59.30` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 88,710.00 USD | 67,460.00 USD | 114,310.00 USD |
| `1D` | `59.40` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 47,830.00 USD | 33,860.00 USD | 58,190.00 USD |
| `7D` | `59.40` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 107,040.00 USD | 73,620.00 USD | 137,500.00 USD |
| `1D` | `59.50` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 83,790.00 USD | 37,380.00 USD | 32,440.00 USD |
| `7D` | `59.50` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD |
| `1D` | `59.60` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 43,950.00 USD | 51,200.00 USD | 5,300.00 USD |
| `7D` | `59.60` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 270,460.00 USD | 147,800.00 USD | 86,840.00 USD |
| `1D` | `59.70` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 11,230.00 USD | 18,330.00 USD | 72,170.00 USD |
| `7D` | `59.70` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 55,510.00 USD | 145,160.00 USD | 162,850.00 USD |
| `1D` | `59.80` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 32,130.00 USD | 26,470.00 USD | 6,220.00 USD |
| `7D` | `59.80` | 8,730,000.00 USD | 8,730,000.00 USD | 0.00 USD | 118,240.00 USD | 91,980.00 USD | 154,560.00 USD |
| `1D` | `59.90` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 102,520.00 USD | 17,810.00 USD | 50,060.00 USD |
| `7D` | `59.90` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 142,290.00 USD | 34,490.00 USD | 29,380.00 USD |
| `1D` | `60.00` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 162,970.00 USD | 29,090.00 USD | 50,570.00 USD |
| `7D` | `60.00` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 100,570.00 USD | 67,520.00 USD | 83,920.00 USD |
| `1D` | `60.10` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 64,550.00 USD | 28,140.00 USD | 57,080.00 USD |
| `7D` | `60.10` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 200,540.00 USD | 84,980.00 USD | 95,670.00 USD |
| `1D` | `60.20` | 6,600,000.00 USD | 6,600,000.00 USD | 0.00 USD | 59,560.00 USD | 19,740.00 USD | 82,270.00 USD |
| `7D` | `60.20` | 9,940,000.00 USD | 9,940,000.00 USD | 0.00 USD | 162,230.00 USD | 99,360.00 USD | 108,990.00 USD |
| `1D` | `60.30` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 53,910.00 USD | 31,630.00 USD | 26,470.00 USD |
| `7D` | `60.30` | 10,340,000.00 USD | 10,340,000.00 USD | 0.00 USD | 133,350.00 USD | 100,380.00 USD | 170,480.00 USD |
| `1D` | `60.40` | 6,830,000.00 USD | 6,830,000.00 USD | 0.00 USD | 66,740.00 USD | 13,730.00 USD | 42,520.00 USD |
| `7D` | `60.40` | 10,710,000.00 USD | 10,710,000.00 USD | 0.00 USD | 64,850.00 USD | 100,560.00 USD | 202,370.00 USD |
| `1D` | `60.50` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 22,700.00 USD | 19,320.00 USD | 36,200.00 USD |
| `7D` | `60.50` | 11,080,000.00 USD | 11,080,000.00 USD | 0.00 USD | 115,390.00 USD | 80,510.00 USD | 175,550.00 USD |
| `1D` | `60.60` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 40,710.00 USD | 19,140.00 USD | 3,930.00 USD |
| `7D` | `60.60` | 11,470,000.00 USD | 11,470,000.00 USD | 0.00 USD | 251,100.00 USD | 18,640.00 USD | 118,680.00 USD |
| `1D` | `60.70` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 32,560.00 USD | 22,330.00 USD | 3,120.00 USD |
| `7D` | `60.70` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 119,080.00 USD | 57,480.00 USD | 22,840.00 USD |
| `1D` | `60.80` | 7,110,000.00 USD | 7,110,000.00 USD | 0.00 USD | 11,430.00 USD | 12,060.00 USD | 47,810.00 USD |
| `7D` | `60.80` | 11,840,000.00 USD | 11,840,000.00 USD | 0.00 USD | 46,960.00 USD | 51,550.00 USD | 76,200.00 USD |
| `1D` | `60.90` | 7,180,000.00 USD | 7,180,000.00 USD | 0.00 USD | 34,200.00 USD | 21,920.00 USD | 22,850.00 USD |
| `7D` | `60.90` | 12,040,000.00 USD | 12,040,000.00 USD | 0.00 USD | 105,970.00 USD | 31,590.00 USD | 64,920.00 USD |
| `1D` | `61.00` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 43,930.00 USD | 6,430.00 USD | 18,420.00 USD |
| `7D` | `61.00` | 12,100,000.00 USD | 12,100,000.00 USD | 0.00 USD | 43,120.00 USD | 11,530.00 USD | 0.00 USD |
| `1D` | `61.10` | 7,280,000.00 USD | 7,280,000.00 USD | 0.00 USD | 12,010.00 USD | 6,270.00 USD | 11,490.00 USD |
| `7D` | `61.10` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 31,540.00 USD | 1,560.00 USD | 0.00 USD |
| `1D` | `61.20` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 72,600.00 USD | 0.00 USD | 39,080.00 USD |
| `7D` | `61.20` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 51,210.00 USD | 17,600.00 USD | 47,810.00 USD |
| `1D` | `61.30` | 7,410,000.00 USD | 7,410,000.00 USD | 0.00 USD | 0.00 USD | 4,040.00 USD | 7,600.00 USD |
| `7D` | `61.30` | 12,300,000.00 USD | 12,300,000.00 USD | 0.00 USD | 16,510.00 USD | 13,210.00 USD | 24,230.00 USD |
| `1D` | `61.40` | 7,410,000.00 USD | 7,410,000.00 USD | 0.00 USD | 1,190.00 USD | 709.61 USD | 5,230.00 USD |
| `7D` | `61.40` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 64,440.00 USD | 25,720.00 USD | 43,510.00 USD |
| `1D` | `61.50` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 1,060.00 USD | 3,880.00 USD | 2,500.00 USD |
| `7D` | `61.50` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 17,710.00 USD | 42,440.00 USD | 41,390.00 USD |
| `1D` | `61.60` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 9,250.00 USD | 11,890.00 USD | 1,150.00 USD |
| `7D` | `61.60` | 12,750,000.00 USD | 12,750,000.00 USD | 0.00 USD | 32,920.00 USD | 58,350.00 USD | 121,470.00 USD |
| `1D` | `61.70` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 13,890.00 USD | 8,790.00 USD | 10,530.00 USD |
| `7D` | `61.70` | 12,940,000.00 USD | 12,940,000.00 USD | 0.00 USD | 82,860.00 USD | 10,880.00 USD | 99,740.00 USD |
| `1D` | `61.80` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 9,150.00 USD | 3,440.00 USD | 10,850.00 USD |
| `7D` | `61.80` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 169,680.00 USD | 25,670.00 USD | 71,530.00 USD |
| `1D` | `61.90` | 7,520,000.00 USD | 7,520,000.00 USD | 0.00 USD | 8,160.00 USD | 2,300.00 USD | 11,770.00 USD |
| `7D` | `61.90` | 13,360,000.00 USD | 13,360,000.00 USD | 0.00 USD | 73,690.00 USD | 32,820.00 USD | 41,580.00 USD |
| `1D` | `62.00` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 15,300.00 USD | 3,100.00 USD | 8,280.00 USD |
| `7D` | `62.00` | 13,460,000.00 USD | 13,460,000.00 USD | 0.00 USD | 50,080.00 USD | 8,550.00 USD | 40,590.00 USD |
| `7D` | `62.10` | 13,470,000.00 USD | 13,470,000.00 USD | 0.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.20` | 13,580,000.00 USD | 13,580,000.00 USD | 0.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD |
| `7D` | `62.30` | 13,730,000.00 USD | 13,730,000.00 USD | 0.00 USD | 27,500.00 USD | 23,450.00 USD | 97,450.00 USD |
| `7D` | `62.40` | 13,860,000.00 USD | 13,860,000.00 USD | 0.00 USD | 76,440.00 USD | 27,560.00 USD | 25,440.00 USD |
| `7D` | `62.50` | 13,940,000.00 USD | 13,940,000.00 USD | 0.00 USD | 36,690.00 USD | 12,720.00 USD | 25,700.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `409.54M` | Total OI Tokens: `7,369,687.9 LTC`
  * 1h OI Change: `-0.82%` | 4h OI Change: `-2.30%` | 24h OI Change: `-8.76%`
  * Exchange Breakdown: Binance=`72.73M` | Bybit=`66.70M` | OKX=`34.07M` | Hyperliquid=`22.20M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `5.05K` | Last 24h: `29.34K` | Last 3d: `56.60K` | Last 7d: `113.64K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0001%` |
| **USDT Bybit** | `-0.0025%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0041%` | **USDT Bitget** | `0.0040%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `39.69%` | `60.31%` | `0.66` | 13,660,000.00 USD |
| `15M` | `Binance` | `40.98%` | `59.02%` | `0.69` | 7,190,000.00 USD |
| `15M` | `OKX` | `36.16%` | `63.84%` | `0.57` | 1,220,000.00 USD |
| `15M` | `Bybit` | `41.95%` | `58.05%` | `0.72` | 1,380,000.00 USD |
| `15M` | `KuCoin` | `47.01%` | `52.99%` | `0.89` | 120,040.00 USD |
| `15M` | `Gate` | `41.85%` | `58.15%` | `0.72` | 335,350.00 USD |
| `15M` | `Bitget` | `34.12%` | `65.88%` | `0.52` | 698,130.00 USD |
| `15M` | `BingX` | `6.86%` | `93.14%` | `0.07` | 355,540.00 USD |
| `15M` | `MEXC` | `32.14%` | `67.86%` | `0.47` | 340,590.00 USD |
| `15M` | `Bitunix` | `43.03%` | `56.97%` | `0.76` | 379,090.00 USD |
| `15M` | `Hyperliquid` | `5.69%` | `94.31%` | `0.06` | 507,240.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.95%` | `51.05%` | `0.96` | 94,030.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 18,130.00 USD |
| `15M` | `WhiteBIT` | `98.69%` | `1.31%` | `75.34` | 761,530.00 USD |
| `15M` | `HTX` | `40.64%` | `59.36%` | `0.68` | 41,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `1%` | `99%` | `0.01` | 144,830.00 USD |
| `15M` | `Aster` | `13.9%` | `86.1%` | `0.16` | 2,890.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `100%` | `0%` | `1.00` | 69,560.00 USD |
| `15M` | `Whale Positions` | `40.98%` | `59.02%` | `0.69` | 7,190,000.00 USD |
| `15M` | `Global Accounts` | `39.69%` | `60.31%` | `0.66` | 13,660,000.00 USD |
| `1H` | `LTC` | `40.89%` | `59.11%` | `0.69` | 16,730,000.00 USD |
| `1H` | `Binance` | `42.79%` | `57.21%` | `0.75` | 5,400,000.00 USD |
| `1H` | `OKX` | `42.37%` | `57.63%` | `0.74` | 1,190,000.00 USD |
| `1H` | `Bybit` | `35.7%` | `64.3%` | `0.56` | 902,510.00 USD |
| `1H` | `KuCoin` | `59.39%` | `40.61%` | `1.46` | 126,080.00 USD |
| `1H` | `Gate` | `44.3%` | `55.7%` | `0.80` | 303,930.00 USD |
| `1H` | `Bitget` | `38.83%` | `61.17%` | `0.63` | 237,270.00 USD |
| `1H` | `BingX` | `40.49%` | `59.51%` | `0.68` | 4,000,000.00 USD |
| `1H` | `MEXC` | `42.84%` | `57.16%` | `0.75` | 613,360.00 USD |
| `1H` | `Bitunix` | `55.81%` | `44.19%` | `1.26` | 348,590.00 USD |
| `1H` | `Hyperliquid` | `18.61%` | `81.39%` | `0.23` | 251,490.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `45.41%` | `54.59%` | `0.83` | 2,620,000.00 USD |
| `1H` | `Crypto.com` | `44.56%` | `55.44%` | `0.80` | 4,020.00 USD |
| `1H` | `WhiteBIT` | `9.72%` | `90.28%` | `0.11` | 627,720.00 USD |
| `1H` | `HTX` | `27.89%` | `72.11%` | `0.39` | 34,010.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `9.56%` | `90.44%` | `0.11` | 16,040.00 USD |
| `1H` | `Aster` | `2.01%` | `97.99%` | `0.02` | 10,130.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `30.85%` | `69.15%` | `0.45` | 43,510.00 USD |
| `1H` | `Whale Positions` | `42.79%` | `57.21%` | `0.75` | 5,400,000.00 USD |
| `1H` | `Global Accounts` | `40.89%` | `59.11%` | `0.69` | 16,730,000.00 USD |
| `4H` | `LTC` | `45.25%` | `54.75%` | `0.83` | 33,370,000.00 USD |
| `4H` | `Binance` | `45.36%` | `54.64%` | `0.83` | 11,000,000.00 USD |
| `4H` | `OKX` | `40.59%` | `59.41%` | `0.68` | 3,570,000.00 USD |
| `4H` | `Bybit` | `49.23%` | `50.77%` | `0.97` | 2,750,000.00 USD |
| `4H` | `KuCoin` | `49.33%` | `50.67%` | `0.97` | 2,270,000.00 USD |
| `4H` | `Gate` | `44.21%` | `55.79%` | `0.79` | 1,750,000.00 USD |
| `4H` | `Bitget` | `48.49%` | `51.51%` | `0.94` | 928,680.00 USD |
| `4H` | `BingX` | `19.55%` | `80.45%` | `0.24` | 3,380,000.00 USD |
| `4H` | `MEXC` | `50.81%` | `49.19%` | `1.03` | 1,300,000.00 USD |
| `4H` | `Bitunix` | `45.87%` | `54.13%` | `0.85` | 727,410.00 USD |
| `4H` | `Hyperliquid` | `42.44%` | `57.56%` | `0.74` | 663,250.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.35%` | `50.65%` | `0.97` | 3,610,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `94.9%` | `5.1%` | `18.61` | 1,320,000.00 USD |
| `4H` | `HTX` | `31.15%` | `68.85%` | `0.45` | 15,270.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `2.11%` | `97.89%` | `0.02` | 111,190.00 USD |
| `4H` | `Aster` | `49.32%` | `50.68%` | `0.97` | 11,050.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `82.13%` | `17.87%` | `4.60` | 2,140.00 USD |
| `4H` | `Whale Positions` | `45.36%` | `54.64%` | `0.83` | 11,000,000.00 USD |
| `4H` | `Global Accounts` | `45.25%` | `54.75%` | `0.83` | 33,370,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `56.27` | `56.27` | `56.27` | `56.45` | `56.08` | 535,233.91 USD | 289,498.00 USD | 245,735.91 USD | 43,762.09 USD | `+8.18%` | `5B / 5S` |
| `0:00 UTC` | `56.34` | `56.33` | `56.34` | `56.47` | `56.22` | 338,253.49 USD | 177,461.44 USD | 160,792.05 USD | 16,669.39 USD | `+4.93%` | `3B / 7S` |
| `5:00 UTC` | `56.14` | `56.16` | `56.14` | `56.30` | `55.98` | 412,908.70 USD | 221,871.73 USD | 191,036.96 USD | 30,834.77 USD | `+7.47%` | `7B / 4S` |
| `0:00 UTC` | `56.22` | `56.21` | `56.22` | `56.34` | `56.09` | 877,726.36 USD | 435,989.57 USD | 441,736.79 USD | -5,747.23 USD | `-0.65%` | `1B / 1S` |
| `5:00 UTC` | `56.12` | `56.15` | `56.12` | `56.22` | `56.09` | 467,194.95 USD | 242,503.27 USD | 224,691.68 USD | 17,811.60 USD | `+3.81%` | `1B / 1S` |
| `0:00 UTC` | `56.00` | `56.00` | `56.00` | `56.27` | `55.72` | 908,665.96 USD | 294,841.59 USD | 613,824.36 USD | -318,982.77 USD | `-35.10%` | `2B / 17S` |
| `5:00 UTC` | `55.91` | `55.98` | `55.91` | `56.12` | `55.78` | 818,601.42 USD | 432,159.31 USD | 386,442.11 USD | 45,717.20 USD | `+5.58%` | `3B / 5S` |
| `0:00 UTC` | `55.77` | `55.81` | `55.77` | `56.00` | `55.66` | 705,526.23 USD | 343,392.26 USD | 362,133.97 USD | -18,741.70 USD | `-2.66%` | `2B / 3S` |
| `5:00 UTC` | `55.64` | `55.76` | `55.64` | `55.98` | `55.62` | 705,697.21 USD | 170,266.34 USD | 535,430.87 USD | -365,164.53 USD | `-51.75%` | `2B / 13S` |
| `0:00 UTC` | `55.70` | `55.71` | `55.70` | `55.78` | `55.64` | 611,182.25 USD | 491,059.61 USD | 120,122.64 USD | 370,936.96 USD | `+60.69%` | `2B / 2S` |

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
| `5m` | -56,120.00 USD | -14,840.00 USD | **`DISTRIBUTION`** |
| `15m` | -53,890.00 USD | 103,340.00 USD | **`ACCUMULATION`** |
| `30m` | -46,100.00 USD | -24,110.00 USD | **`DISTRIBUTION`** |
| `1h` | -38,090.00 USD | -478,100.00 USD | **`DISTRIBUTION`** |
| `2h` | -81,780.00 USD | -832,980.00 USD | **`DISTRIBUTION`** |
| `4h` | 432,450.00 USD | -508,210.00 USD | **`DISTRIBUTION`** |
| `6h` | 508,830.00 USD | -1,960,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 655,170.00 USD | -4,360,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,180,000.00 USD | -6,210,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 1,030,000.00 USD | -4,980,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 4,410,000.00 USD | -25,120,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -24,200,000.00 USD | -196,830,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-56.12K` | 15m=`-53.89K` | 1h=`-38.09K` | 24h=`+1.03M`
* Futures Capital Netflows: 5m=`-14.84K` | 15m=`+103.34K` | 1h=`-478.10K` | 24h=`-4.98M`
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
  * `2026-10-30 13:52:16 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:16 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:32:16 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:16 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:16 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 13:22:16 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 13:21:16 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:05:16 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:05:16 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:05:16 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `54.59` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `53.71` (Risk Distance: `0.8786` pts)
  * +2.5R Take Profit: `56.78`
  * Mathematical Lot Sizing: **`11.38 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `56.21` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `57.09` (Risk Distance: `0.8786` pts)
  * +2.5R Take Profit: `54.02`
  * Mathematical Lot Sizing: **`11.38 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`55.99`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
