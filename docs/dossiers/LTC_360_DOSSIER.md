# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 14:59:56 IST` (`2026-10-30 09:29:56 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `55.28` | **Live Ask Quote**: `55.58` | **Mid Price**: `55.43`
- **Spread Points**: `300.00` | **Spread BPS**: `54.12 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `54.84` | VWAP Z-Score: `+0.43` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.3296` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `42.08` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `57.68` | Lower -3.00σ Band: `52.01`
  * Upper +2.51σ Band: `57.22` | Lower -2.51σ Band: `52.47`
  * Upper +2.01σ Band: `56.75` | Lower -2.01σ Band: `52.94`
  * Upper +2.00σ Band: `56.74` | Lower -2.00σ Band: `52.95`
  * Upper +1.28σ Band: `56.05` | Lower -1.28σ Band: `53.63`
  * Upper +1.00σ Band: `55.79` | Lower -1.00σ Band: `53.90`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`55.52` | EMA-20=`55.59` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`55.73` (Slope: `+0.0000`) | EMA-100=`56.20`
  * Institutional Anchors: EMA-144=`56.44` | EMA-200=`56.58` (Slope: `-0.2030`) | EMA-233=`56.63`
- **Range Boundaries**: 24H High=`58.72` | 24H Low=`52.64` | Weekly High=`59.62` | Weekly Low=`52.64`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `56.16` (Distance: `-1.34%`)
  * Point of Control (POC) = `55.30` (Distance: `+0.19%`)
  * Value Area Low (VAL) = `54.61` (Distance: `+1.46%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.40` | POC=`57.72` | VAL=`56.83`
  * Prior Day Extremes: PDH=`59.52` | PDL=`54.18` | PDC=`54.46`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`58.29` | Weekly POC=`56.43` | Weekly VAL=`55.83`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`56.03` | Low=`52.64`
  * London Session (08:00-16:00 UTC): High=`56.23` | Low=`55.22`
  * New York Session (13:00-21:00 UTC): High=`55.76` | Low=`55.10`
  * Initial Balance (First Hour): IB High=`56.22` | IB Low=`55.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `55.21` - `55.65`
  * Optimal Trade Entry (OTE 0.705): `55.54`
  * Structural Invalidation Anchor (0.786): `55.87`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `55.50` | `55.54` | `55.43` | `55.47` | `2,504` | 138,909.71 USD | -9,505.46 USD | `-6.84%` | -5,511,289.61 USD | `+0.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `55.47` | `55.59` | `55.45` | `55.48` | `2,239` | 124,280.76 USD | -22,525.90 USD | `-18.13%` | -5,533,815.51 USD | `-0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `55.49` | `55.54` | `55.48` | `55.49` | `487` | 27,054.96 USD | -697.88 USD | `-2.58%` | -5,534,513.39 USD | `+0.03` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `55.57` | `55.70` | `55.51` | `55.54` | `7,845` | 436,166.22 USD | 48,104.99 USD | `+11.03%` | -5,388,709.62 USD | `+0.55` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `55.54` | `55.70` | `55.43` | `55.47` | `8,364` | 464,437.63 USD | -79,326.74 USD | `-17.08%` | -5,468,036.36 USD | `-0.42` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `55.47` | `55.59` | `55.45` | `55.49` | `2,728` | 151,430.44 USD | -23,318.50 USD | `-15.40%` | -5,491,354.86 USD | `-0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `56.22` | `56.34` | `55.72` | `55.97` | `54,792` | 3,072,188.69 USD | -261,201.20 USD | `-8.50%` | -5,429,107.24 USD | `+0.02` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `55.96` | `55.99` | `55.51` | `55.54` | `48,222` | 2,686,866.22 USD | -29,505.47 USD | `-1.10%` | -5,458,612.72 USD | `+0.34` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `55.54` | `55.70` | `55.43` | `55.49` | `11,091` | 615,773.34 USD | -102,550.52 USD | `-16.65%` | -5,561,163.24 USD | `+0.27` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -5,054,684.98 USD | `-0.61` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.47` | `55.72` | `55.97` | `202,255` | 11,356,305.33 USD | -519,640.59 USD | `-4.58%` | -5,574,325.57 USD | `+0.43` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `55.96` | `55.99` | `55.43` | `55.49` | `59,315` | 3,302,734.28 USD | -132,150.71 USD | `-4.00%` | -5,706,476.28 USD | `+0.62` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | 387,872.12 USD | `-1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,876,168.80 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -5,054,684.98 USD | `-0.61` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.47` | `55.72` | `55.97` | `202,255` | 11,356,305.33 USD | -519,640.59 USD | `-4.58%` | -5,574,325.57 USD | `+0.43` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `55.96` | `55.99` | `55.43` | `55.49` | `59,315` | 3,302,734.28 USD | -132,150.71 USD | `-4.00%` | -5,706,476.28 USD | `+0.62` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`55.43`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:52:21 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1081` | `0xeadc...9d55` | `LONG` | 2,024,030.95 USD | `36,463.77` | `52.78` | `55.40` | `0.000000` | 99,355.00 USD | `+4.91%` | `10X Cross` |
| `1094` | `0x9aa5...58af` | `SHORT` | 2,005,001.54 USD | `36,177.65` | `71.22` | `55.40` | `309.85` | 571,485.13 USD | `+28.50%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `57.41` | 5,214.91 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 5.21K USD at 57.4140 USD [API] | `2026-10-29 10:32:18` |
| `ANNOUNCEMENT` | `INFO` | `58.00` | 7,509.00 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 57.9980 USD [API] | `2026-10-29 11:54:42` |
| `ANNOUNCEMENT` | `INFO` | `57.87` | 7,508.89 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 57.8720 USD [API] | `2026-10-29 12:02:05` |
| `ANNOUNCEMENT` | `INFO` | `57.87` | 5,812.29 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.81K USD at 57.8740 USD [API] | `2026-10-29 13:57:22` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`56.49` (Vol: 204,200.00 USD, Dist: `+1.89%`) | Long MP=`54.13` (Vol: 153,300.00 USD, Dist: `--2.36%`)
  * 48H Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.42%`) | Long MP=`54.12` (Vol: 153,300.00 USD, Dist: `--2.39%`)
  * 3D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.42%`) | Long MP=`54.12` (Vol: 153,300.00 USD, Dist: `--2.39%`)
  * 7D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.42%`) | Long MP=`54.12` (Vol: 153,300.00 USD, Dist: `--2.39%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `11.35` | 136.20 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `11.45` | 133.51 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.25` | 122.50 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.75` | 2,560.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.15` | 2,220.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.65` | 150.15 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.25` | 16,970.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.45` | 4,990.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.05` | 3,470.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.25` | 173.63 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.45` | 2,010.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.25` | 133.65 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.85` | 4,260.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.55` | 2,220.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.25` | 986.50 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.85` | 195.57 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.95` | 378.89 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.65` | 447.40 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 277,980.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 173.39 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 167,420.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.65` | 1,240.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.85` | 7,620.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 374.20 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.85` | 1,050.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.05` | 5,510.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 272.75 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 173.85 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 755.28 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 297,500.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.95` | 220.43 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 218.46 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 152.75 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.65` | 1,540.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 538.53 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 27,620.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 1,060.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.65` | 4,640.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 2,870.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 125.24 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 450.10 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.25` | 225.75 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.35` | 172.10 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 3,440.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 953.68 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.95` | 32,950.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.05` | 4,100.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.35` | 5,810.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 257.76 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.85` | 259.63 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 10,400.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 126.70 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.45` | 67,610.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 8,200.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 104.85 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 166.49 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.35` | 421.37 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 3,020.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 423.18 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.65` | 3,000.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 101.80 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 110.78 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 2,750.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 9,260.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 3,530.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 377.50 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 6,210.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 446.67 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.25` | 695.38 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 847.54 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 2,400.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 993.82 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 4,280.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 2,730.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 664,760.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 570.02 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.25` | 340.30 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 264.83 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 716.41 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 312.44 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 5,900.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 1,180.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 133.10 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 2,160.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 1,010.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 133.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 40,920.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 6,340.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 509.01 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 396.54 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.15` | 5,430.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 14,850.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.35` | 9,100.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 644.96 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.65` | 1,040.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 201.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 66,300.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 35,410.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.35` | 301.96 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.55` | 682.50 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 1,570.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.75` | 3,800.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 5,800.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 2,000.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 9,410.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 1,580.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 121,520.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 5,390.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 710.84 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 3,900.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 21,880.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 801.14 USD | 991,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 5,660.00 USD | 990,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 2,380.00 USD | 985,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 84,440.00 USD | 982,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 842.44 USD | 898,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 5,570.00 USD | 897,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 134.55 USD | 891,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 2,620.00 USD | 891,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 6,190.00 USD | 889,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 8,710.00 USD | 882,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 3,180.00 USD | 874,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 2,180.00 USD | 870,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 23,940.00 USD | 868,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 12,060.00 USD | 844,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 42,180.00 USD | 832,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 30,970.00 USD | 790,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 706.41 USD | 759,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.35` | 383.78 USD | 758,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.45` | 22,480.00 USD | 758,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 2,140.00 USD | 736,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 4,430.00 USD | 733,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 358.40 USD | 729,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 158.22 USD | 729,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.05` | 2,140.00 USD | 728,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 1,980.00 USD | 726,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.20` | 8,190,000.00 USD | 8,190,000.00 USD | 9,650.00 USD | 2,470.00 USD | 114.09 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.25` | 9,030.00 USD | 724,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.30` | 8,180,000.00 USD | 8,180,000.00 USD | 692.33 USD | 4,740.00 USD | 6,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.35` | 43,920.00 USD | 715,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.40` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 1,520.00 USD | 28,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.45` | 2,590.00 USD | 671,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.50` | 8,130,000.00 USD | 8,130,000.00 USD | 11,830.00 USD | 0.00 USD | 7,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.55` | 4,450.00 USD | 669,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 47,750.00 USD | 664,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 381.04 USD | 617,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.10` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.15` | 1,690.00 USD | 616,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.20` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.25` | 110.49 USD | 615,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.40` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 6,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.55` | 2,030.00 USD | 614,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.60` | 8,100,000.00 USD | 8,100,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.65` | 8,280.00 USD | 612,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 333.94 USD | 604,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.80` | 8,090,000.00 USD | 8,090,000.00 USD | 1,780.00 USD | 2,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `48.90` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 0.00 USD | 960.40 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.95` | 252.58 USD | 604,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,580.00 USD | 604,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,740.00 USD | 602,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.30` | 8,090,000.00 USD | 8,090,000.00 USD | 15,190.00 USD | 4,490.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.35` | 5,230.00 USD | 596,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.40` | 8,050,000.00 USD | 8,050,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.45` | 19,440.00 USD | 591,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.50` | 8,050,000.00 USD | 8,050,000.00 USD | 2,830.00 USD | 7,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.55` | 18,010.00 USD | 572,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.60` | 8,040,000.00 USD | 8,040,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.65` | 75,190.00 USD | 554,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.70` | 8,020,000.00 USD | 8,020,000.00 USD | 12,090.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.75` | 1,250.00 USD | 478,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.80` | 8,000,000.00 USD | 8,000,000.00 USD | 9,930.00 USD | 8,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `49.90` | 4,070,000.00 USD | 4,070,000.00 USD | 29,140.00 USD | 17,520.00 USD | 47,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.90` | 7,990,000.00 USD | 7,990,000.00 USD | 45,030.00 USD | 8,880.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.95` | 19,920.00 USD | 477,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.00` | 3,980,000.00 USD | 3,980,000.00 USD | 13,200.00 USD | 16,830.00 USD | 40,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.00` | 7,930,000.00 USD | 7,930,000.00 USD | 22,100.00 USD | 19,810.00 USD | 24,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.05` | 1,820.00 USD | 457,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.10` | 3,910,000.00 USD | 3,910,000.00 USD | 3,780.00 USD | 4,040.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.10` | 7,860,000.00 USD | 7,860,000.00 USD | 363.50 USD | 682.90 USD | 8,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.20` | 3,890,000.00 USD | 3,890,000.00 USD | 177.10 USD | 709.61 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.20` | 7,850,000.00 USD | 7,850,000.00 USD | 6,960.00 USD | 500.40 USD | 42,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.25` | 102.51 USD | 455,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.30` | 3,890,000.00 USD | 3,890,000.00 USD | 171.03 USD | 3,880.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.30` | 7,800,000.00 USD | 7,800,000.00 USD | 16,270.00 USD | 10,780.00 USD | 7,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.35` | 1,140.00 USD | 455,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.40` | 3,880,000.00 USD | 3,880,000.00 USD | 8,260.00 USD | 11,890.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.40` | 7,770,000.00 USD | 7,770,000.00 USD | 28,280.00 USD | 26,580.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,720.00 USD | 454,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.50` | 3,860,000.00 USD | 3,860,000.00 USD | 8,910.00 USD | 8,790.00 USD | 10,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.50` | 7,680,000.00 USD | 7,680,000.00 USD | 32,490.00 USD | 6,790.00 USD | 44,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.55` | 84,100.00 USD | 449,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.60` | 3,830,000.00 USD | 3,830,000.00 USD | 7,330.00 USD | 3,440.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.60` | 7,590,000.00 USD | 7,590,000.00 USD | 67,580.00 USD | 21,530.00 USD | 31,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.70` | 3,810,000.00 USD | 3,810,000.00 USD | 8,170.00 USD | 2,300.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.70` | 7,470,000.00 USD | 7,470,000.00 USD | 65,920.00 USD | 32,820.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.75` | 9,050.00 USD | 365,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.80` | 3,790,000.00 USD | 3,790,000.00 USD | 12,550.00 USD | 3,100.00 USD | 8,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.80` | 7,330,000.00 USD | 7,330,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.90` | 3,760,000.00 USD | 3,760,000.00 USD | 826.24 USD | 260.05 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.90` | 7,240,000.00 USD | 7,240,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.95` | 431.55 USD | 356,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.00` | 3,750,000.00 USD | 3,750,000.00 USD | 5,040.00 USD | 0.00 USD | 430.77 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.00` | 6,980,000.00 USD | 6,980,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.10` | 3,750,000.00 USD | 3,750,000.00 USD | 9,210.00 USD | 6,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.10` | 6,860,000.00 USD | 6,860,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.15` | 219,370.00 USD | 356,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.20` | 3,730,000.00 USD | 3,730,000.00 USD | 1,770.00 USD | 1,130.00 USD | 19,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.20` | 6,770,000.00 USD | 6,770,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.25` | 202.44 USD | 136,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.30` | 3,710,000.00 USD | 3,710,000.00 USD | 8,650.00 USD | 9,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.30` | 6,710,000.00 USD | 6,710,000.00 USD | 28,400.00 USD | 26,720.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.35` | 453.93 USD | 136,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.40` | 3,690,000.00 USD | 3,690,000.00 USD | 3,250.00 USD | 5,610.00 USD | 416.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.40` | 6,610,000.00 USD | 6,610,000.00 USD | 73,130.00 USD | 42,820.00 USD | 46,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.45` | 27,210.00 USD | 136,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.50` | 3,680,000.00 USD | 3,680,000.00 USD | 5,650.00 USD | 10,010.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.50` | 6,450,000.00 USD | 6,450,000.00 USD | 38,520.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.55` | 551.07 USD | 109,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.60` | 3,630,000.00 USD | 3,630,000.00 USD | 9,060.00 USD | 18,580.00 USD | 731.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.60` | 6,350,000.00 USD | 6,350,000.00 USD | 37,880.00 USD | 36,790.00 USD | 41,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.65` | 9,100.00 USD | 108,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.70` | 3,600,000.00 USD | 3,600,000.00 USD | 2,510.00 USD | 12,840.00 USD | 44.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.70` | 6,230,000.00 USD | 6,230,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.75` | 6,480.00 USD | 99,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.80` | 3,580,000.00 USD | 3,580,000.00 USD | 13,770.00 USD | 19,520.00 USD | 14,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.80` | 6,190,000.00 USD | 6,190,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.85` | 13,680.00 USD | 92,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.90` | 3,530,000.00 USD | 3,530,000.00 USD | 10,140.00 USD | 19,910.00 USD | 23,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.90` | 6,140,000.00 USD | 6,140,000.00 USD | 5,870.00 USD | 25,410.00 USD | 28,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.95` | 13,950.00 USD | 79,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.00` | 3,480,000.00 USD | 3,480,000.00 USD | 20,980.00 USD | 25,620.00 USD | 24,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.00` | 6,080,000.00 USD | 6,080,000.00 USD | 65,840.00 USD | 26,440.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.05` | 2,860.00 USD | 65,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.10` | 3,410,000.00 USD | 3,410,000.00 USD | 34,970.00 USD | 17,300.00 USD | 50,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 5,970,000.00 USD | 5,970,000.00 USD | 24,220.00 USD | 28,090.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.15` | 1,900.00 USD | 62,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.20` | 3,310,000.00 USD | 3,310,000.00 USD | 15,890.00 USD | 7,630.00 USD | 49,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 5,880,000.00 USD | 5,880,000.00 USD | 38,380.00 USD | 13,960.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.25` | 4,930.00 USD | 60,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.30` | 3,230,000.00 USD | 3,230,000.00 USD | 26,510.00 USD | 22,090.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 5,810,000.00 USD | 5,810,000.00 USD | 26,450.00 USD | 40,700.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.35` | 134.02 USD | 55,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.40` | 3,170,000.00 USD | 3,170,000.00 USD | 13,070.00 USD | 15,400.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 5,730,000.00 USD | 5,730,000.00 USD | 20,580.00 USD | 38,950.00 USD | 22,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.45` | 5,820.00 USD | 55,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.50` | 3,140,000.00 USD | 3,140,000.00 USD | 53,990.00 USD | 30,000.00 USD | 79,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.50` | 5,650,000.00 USD | 5,650,000.00 USD | 40,460.00 USD | 0.00 USD | 11,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.55` | 8,700.00 USD | 49,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.60` | 2,980,000.00 USD | 2,980,000.00 USD | 8,330.00 USD | 43,700.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.60` | 5,600,000.00 USD | 5,600,000.00 USD | 67,180.00 USD | 32,590.00 USD | 59,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.70` | 2,920,000.00 USD | 2,920,000.00 USD | 18,270.00 USD | 19,780.00 USD | 40,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.70` | 5,440,000.00 USD | 5,440,000.00 USD | 19,550.00 USD | 75,910.00 USD | 108,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.75` | 30,280.00 USD | 40,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.80` | 2,840,000.00 USD | 2,840,000.00 USD | 28,000.00 USD | 50,850.00 USD | 72,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.80` | 5,240,000.00 USD | 5,240,000.00 USD | 30,590.00 USD | 25,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.85` | 5,950.00 USD | 10,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.90` | 2,690,000.00 USD | 2,690,000.00 USD | 43,760.00 USD | 50,880.00 USD | 30,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.90` | 5,180,000.00 USD | 5,180,000.00 USD | 30,900.00 USD | 11,650.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.95` | 531.09 USD | 4,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.00` | 2,560,000.00 USD | 2,560,000.00 USD | 26,800.00 USD | 30,500.00 USD | 39,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.00` | 5,100,000.00 USD | 5,100,000.00 USD | 39,690.00 USD | 22,700.00 USD | 77,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.05` | 202.12 USD | 4,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.10` | 2,470,000.00 USD | 2,470,000.00 USD | 12,590.00 USD | 47,310.00 USD | 85,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.10` | 4,960,000.00 USD | 4,960,000.00 USD | 45,320.00 USD | 17,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.15` | 2,030.00 USD | 3,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.20` | 2,320,000.00 USD | 2,320,000.00 USD | 26,460.00 USD | 10,830.00 USD | 42,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.20` | 4,900,000.00 USD | 4,900,000.00 USD | 162,460.00 USD | 32,580.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.25` | 1,030.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.30` | 2,240,000.00 USD | 2,240,000.00 USD | 8,610.00 USD | 28,530.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.30` | 4,680,000.00 USD | 4,680,000.00 USD | 59,390.00 USD | 49,210.00 USD | 35,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.35` | 941.09 USD | 941.09 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.40` | 2,200,000.00 USD | 2,200,000.00 USD | 12,600.00 USD | 10,640.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.40` | 4,540,000.00 USD | 4,540,000.00 USD | 44,030.00 USD | 17,420.00 USD | 91,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.50` | 2,170,000.00 USD | 2,170,000.00 USD | 9,410.00 USD | 5,700.00 USD | 22,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.50` | 4,380,000.00 USD | 4,380,000.00 USD | 60,260.00 USD | 3,440.00 USD | 28,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.60` | 2,130,000.00 USD | 2,130,000.00 USD | 75,950.00 USD | 3,830.00 USD | 20,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.60` | 4,290,000.00 USD | 4,290,000.00 USD | 52,800.00 USD | 3,780.00 USD | 20,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.70` | 2,030,000.00 USD | 2,030,000.00 USD | 6,210.00 USD | 11,100.00 USD | 11,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.70` | 4,210,000.00 USD | 4,210,000.00 USD | 131,400.00 USD | 21,330.00 USD | 13,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.80` | 2,000,000.00 USD | 2,000,000.00 USD | 53,640.00 USD | 28,920.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.80` | 4,050,000.00 USD | 4,050,000.00 USD | 99,150.00 USD | 43,900.00 USD | 302.55 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.90` | 1,920,000.00 USD | 1,920,000.00 USD | 51,060.00 USD | 39,560.00 USD | 27,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.90` | 3,910,000.00 USD | 3,910,000.00 USD | 160,820.00 USD | 22,780.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.00` | 1,800,000.00 USD | 1,800,000.00 USD | 76,010.00 USD | 21,440.00 USD | 86,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.00` | 3,710,000.00 USD | 3,710,000.00 USD | 380,340.00 USD | 71,820.00 USD | 304,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.10` | 1,610,000.00 USD | 1,610,000.00 USD | 94,870.00 USD | 19,160.00 USD | 49,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.10` | 2,960,000.00 USD | 2,960,000.00 USD | 302,190.00 USD | 0.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.20` | 1,450,000.00 USD | 1,450,000.00 USD | 72,600.00 USD | 24,050.00 USD | 40,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.20` | 2,650,000.00 USD | 2,650,000.00 USD | 205,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.30` | 1,310,000.00 USD | 1,310,000.00 USD | 27,200.00 USD | 8,640.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.30` | 2,450,000.00 USD | 2,450,000.00 USD | 381,380.00 USD | 8,520.00 USD | 181,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.40` | 1,270,000.00 USD | 1,270,000.00 USD | 62,680.00 USD | 92,560.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.40` | 1,870,000.00 USD | 1,870,000.00 USD | 304,270.00 USD | 63,170.00 USD | 92,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.50` | 1,110,000.00 USD | 1,110,000.00 USD | 25,050.00 USD | 64,250.00 USD | 9,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.50` | 1,410,000.00 USD | 1,410,000.00 USD | 159,720.00 USD | 35,580.00 USD | 239,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.60` | 1,020,000.00 USD | 1,020,000.00 USD | 913.17 USD | 25,490.00 USD | 43,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.60` | 978,810.00 USD | 978,810.00 USD | 18,530.00 USD | 1,930.00 USD | 131,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.70` | 945,620.00 USD | 945,620.00 USD | 6,600.00 USD | 23,060.00 USD | 105,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.70` | 826,970.00 USD | 826,970.00 USD | 0.00 USD | 3,600.00 USD | 41,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.80` | 810,160.00 USD | 810,160.00 USD | 0.00 USD | 48,420.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.80` | 782,060.00 USD | 782,060.00 USD | 0.00 USD | 35,700.00 USD | 26,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.90` | 737,820.00 USD | 737,820.00 USD | 66,900.00 USD | 65,440.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.90` | 719,920.00 USD | 719,920.00 USD | 0.00 USD | 112,280.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.00` | 594,640.00 USD | 594,640.00 USD | 40,710.00 USD | 54,150.00 USD | 55,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.00` | 559,350.00 USD | 559,350.00 USD | 97,700.00 USD | 2,830.00 USD | 19,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.10` | 444,580.00 USD | 444,580.00 USD | 50,530.00 USD | 62,170.00 USD | 80,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.10` | 439,470.00 USD | 439,470.00 USD | 54,590.00 USD | 18,510.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.20` | 251,690.00 USD | 251,690.00 USD | 39,390.00 USD | 11,830.00 USD | 66,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.20` | 301,680.00 USD | 301,680.00 USD | 57,400.00 USD | 59,710.00 USD | 150,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.30` | 134,060.00 USD | 134,060.00 USD | 52,860.00 USD | 15,520.00 USD | 59,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.30` | 34,410.00 USD | 34,410.00 USD | 23,140.00 USD | 11,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.40` | 6,510.00 USD | 6,510.00 USD | 0.00 USD | 6,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.40` | 23,360.00 USD | 23,360.00 USD | 0.00 USD | 18,550.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.40` | 46,710.00 USD | 46,710.00 USD | 0.00 USD | 18,550.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.50` | 5,500.00 USD | 5,500.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.50` | 11,000.00 USD | 11,000.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.70` | 19,310.00 USD | 19,310.00 USD | 0.00 USD | 7,700.00 USD | 613.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.70` | 253,130.00 USD | 253,130.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.80` | 22,490.00 USD | 22,490.00 USD | 0.00 USD | 0.00 USD | 3,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.80` | 344,100.00 USD | 344,100.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.90` | 75,550.00 USD | 75,550.00 USD | 51,520.00 USD | 0.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.90` | 485,430.00 USD | 485,430.00 USD | 141,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.00` | 79,930.00 USD | 79,930.00 USD | 0.00 USD | 0.00 USD | 4,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.00` | 656,540.00 USD | 656,540.00 USD | 2,590.00 USD | 0.00 USD | 168,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.20` | 736,490.00 USD | 736,490.00 USD | 0.00 USD | 79,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `56.25` | 700.88 USD | 700.88 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `56.30` | 83,880.00 USD | 83,880.00 USD | 0.00 USD | 0.00 USD | 3,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.30` | 739,080.00 USD | 739,080.00 USD | 0.00 USD | 0.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.40` | 116,760.00 USD | 116,760.00 USD | 5,040.00 USD | 25,370.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.40` | 752,770.00 USD | 752,770.00 USD | 2,650.00 USD | 11,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.50` | 522,560.00 USD | 522,560.00 USD | 150,140.00 USD | 110,620.00 USD | 145,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.50` | 1,080,000.00 USD | 1,080,000.00 USD | 170,750.00 USD | 151,940.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.60` | 826,330.00 USD | 826,330.00 USD | 61,400.00 USD | 161,300.00 USD | 81,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.60` | 1,630,000.00 USD | 1,630,000.00 USD | 363,190.00 USD | 185,910.00 USD | 507.54 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.70` | 1,300,000.00 USD | 1,300,000.00 USD | 114,230.00 USD | 45,300.00 USD | 315,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.70` | 1,990,000.00 USD | 1,990,000.00 USD | 117,290.00 USD | 141,830.00 USD | 98,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.80` | 1,550,000.00 USD | 1,550,000.00 USD | 117,760.00 USD | 20,790.00 USD | 106,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.80` | 2,570,000.00 USD | 2,570,000.00 USD | 172,110.00 USD | 92,780.00 USD | 318,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.90` | 1,640,000.00 USD | 1,640,000.00 USD | 45,140.00 USD | 17,930.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.90` | 3,050,000.00 USD | 3,050,000.00 USD | 113,780.00 USD | 52,200.00 USD | 307,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.00` | 1,720,000.00 USD | 1,720,000.00 USD | 6,480.00 USD | 43,030.00 USD | 29,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.00` | 3,370,000.00 USD | 3,370,000.00 USD | 88,680.00 USD | 56,390.00 USD | 178,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.10` | 1,930,000.00 USD | 1,930,000.00 USD | 77,000.00 USD | 77,400.00 USD | 46,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.10` | 3,510,000.00 USD | 3,510,000.00 USD | 36,580.00 USD | 79,290.00 USD | 21,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.20` | 2,180,000.00 USD | 2,180,000.00 USD | 53,080.00 USD | 78,490.00 USD | 120,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.20` | 3,670,000.00 USD | 3,670,000.00 USD | 118,850.00 USD | 23,920.00 USD | 23,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.30` | 2,380,000.00 USD | 2,380,000.00 USD | 70,930.00 USD | 44,630.00 USD | 87,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.30` | 3,880,000.00 USD | 3,880,000.00 USD | 76,940.00 USD | 28,570.00 USD | 98,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.40` | 2,590,000.00 USD | 2,590,000.00 USD | 84,960.00 USD | 49,470.00 USD | 78,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.40` | 4,330,000.00 USD | 4,330,000.00 USD | 124,180.00 USD | 72,180.00 USD | 257,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.50` | 3,020,000.00 USD | 3,020,000.00 USD | 197,830.00 USD | 52,620.00 USD | 174,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.50` | 4,460,000.00 USD | 4,460,000.00 USD | 99,810.00 USD | 31,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.60` | 3,180,000.00 USD | 3,180,000.00 USD | 75,520.00 USD | 28,370.00 USD | 62,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.60` | 4,680,000.00 USD | 4,680,000.00 USD | 149,560.00 USD | 44,690.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.70` | 3,380,000.00 USD | 3,380,000.00 USD | 42,540.00 USD | 54,600.00 USD | 96,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.70` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 30,070.00 USD | 57,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.75` | 155.35 USD | 856.22 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `57.80` | 3,500,000.00 USD | 3,500,000.00 USD | 18,150.00 USD | 22,650.00 USD | 77,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.80` | 4,860,000.00 USD | 4,860,000.00 USD | 9,650.00 USD | 24,520.00 USD | 49,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.90` | 3,550,000.00 USD | 3,550,000.00 USD | 13,000.00 USD | 15,870.00 USD | 28,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.90` | 4,900,000.00 USD | 4,900,000.00 USD | 14,390.00 USD | 963.90 USD | 30,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.95` | 125.75 USD | 981.97 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.00` | 3,590,000.00 USD | 3,590,000.00 USD | 7,880.00 USD | 9,480.00 USD | 15,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.00` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 5,470.00 USD | 107,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.10` | 3,660,000.00 USD | 3,660,000.00 USD | 31,400.00 USD | 17,830.00 USD | 21,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.10` | 5,050,000.00 USD | 5,050,000.00 USD | 5,470.00 USD | 19,160.00 USD | 14,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.20` | 3,730,000.00 USD | 3,730,000.00 USD | 35,920.00 USD | 34,800.00 USD | 4,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.20` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 31,590.00 USD | 302.55 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.30` | 3,870,000.00 USD | 3,870,000.00 USD | 33,360.00 USD | 38,620.00 USD | 64,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.30` | 5,180,000.00 USD | 5,180,000.00 USD | 48,850.00 USD | 11,000.00 USD | 36,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.40` | 3,970,000.00 USD | 3,970,000.00 USD | 26,490.00 USD | 18,940.00 USD | 49,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.40` | 5,300,000.00 USD | 5,300,000.00 USD | 27,290.00 USD | 9,260.00 USD | 86,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.50` | 3,980,000.00 USD | 3,980,000.00 USD | 16,410.00 USD | 1,200.00 USD | 124.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.50` | 5,330,000.00 USD | 5,330,000.00 USD | 2,060.00 USD | 24,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.60` | 4,050,000.00 USD | 4,050,000.00 USD | 21,940.00 USD | 5,920.00 USD | 40,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.60` | 5,430,000.00 USD | 5,430,000.00 USD | 30,680.00 USD | 20,260.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.70` | 4,140,000.00 USD | 4,140,000.00 USD | 44,920.00 USD | 10,120.00 USD | 29,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.70` | 5,500,000.00 USD | 5,500,000.00 USD | 15,810.00 USD | 11,600.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.80` | 4,210,000.00 USD | 4,210,000.00 USD | 36,630.00 USD | 9,890.00 USD | 23,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.80` | 5,510,000.00 USD | 5,510,000.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `58.85` | 1,480.00 USD | 2,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.90` | 4,380,000.00 USD | 4,380,000.00 USD | 22,130.00 USD | 60,970.00 USD | 90,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.90` | 5,650,000.00 USD | 5,650,000.00 USD | 2,140.00 USD | 54,240.00 USD | 83,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.00` | 4,700,000.00 USD | 4,700,000.00 USD | 129,990.00 USD | 58,870.00 USD | 129,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.00` | 6,090,000.00 USD | 6,090,000.00 USD | 259,280.00 USD | 65,270.00 USD | 118,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.10` | 4,990,000.00 USD | 4,990,000.00 USD | 92,240.00 USD | 39,740.00 USD | 163,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.10` | 6,390,000.00 USD | 6,390,000.00 USD | 93,390.00 USD | 45,400.00 USD | 158,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.20` | 5,210,000.00 USD | 5,210,000.00 USD | 102,940.00 USD | 59,320.00 USD | 49,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.20` | 6,740,000.00 USD | 6,740,000.00 USD | 153,580.00 USD | 18,540.00 USD | 174,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.30` | 5,450,000.00 USD | 5,450,000.00 USD | 146,220.00 USD | 30,070.00 USD | 66,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.30` | 7,010,000.00 USD | 7,010,000.00 USD | 88,710.00 USD | 67,460.00 USD | 114,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.35` | 9,440.00 USD | 11,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.40` | 5,560,000.00 USD | 5,560,000.00 USD | 35,110.00 USD | 30,780.00 USD | 49,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.40` | 7,330,000.00 USD | 7,330,000.00 USD | 107,040.00 USD | 73,620.00 USD | 137,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.45` | 213.43 USD | 12,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.50` | 5,710,000.00 USD | 5,710,000.00 USD | 81,240.00 USD | 34,430.00 USD | 32,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.50` | 7,470,000.00 USD | 7,470,000.00 USD | 67,060.00 USD | 61,370.00 USD | 21,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.55` | 213.78 USD | 12,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.60` | 5,810,000.00 USD | 5,810,000.00 USD | 43,950.00 USD | 51,200.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.60` | 7,910,000.00 USD | 7,910,000.00 USD | 236,760.00 USD | 129,330.00 USD | 72,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.70` | 5,900,000.00 USD | 5,900,000.00 USD | 7,970.00 USD | 15,700.00 USD | 62,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.70` | 8,230,000.00 USD | 8,230,000.00 USD | 55,510.00 USD | 99,970.00 USD | 162,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.80` | 5,960,000.00 USD | 5,960,000.00 USD | 32,130.00 USD | 26,470.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.80` | 8,600,000.00 USD | 8,600,000.00 USD | 118,240.00 USD | 91,980.00 USD | 154,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.90` | 6,130,000.00 USD | 6,130,000.00 USD | 102,020.00 USD | 17,810.00 USD | 50,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.90` | 8,800,000.00 USD | 8,800,000.00 USD | 142,290.00 USD | 34,490.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.95` | 215.22 USD | 12,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.00` | 6,370,000.00 USD | 6,370,000.00 USD | 162,970.00 USD | 29,090.00 USD | 50,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.00` | 9,060,000.00 USD | 9,060,000.00 USD | 100,570.00 USD | 67,520.00 USD | 83,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.10` | 6,520,000.00 USD | 6,520,000.00 USD | 64,550.00 USD | 28,140.00 USD | 57,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.10` | 9,440,000.00 USD | 9,440,000.00 USD | 200,540.00 USD | 84,980.00 USD | 95,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.15` | 208,880.00 USD | 221,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.20` | 6,680,000.00 USD | 6,680,000.00 USD | 58,830.00 USD | 19,740.00 USD | 82,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.20` | 9,810,000.00 USD | 9,810,000.00 USD | 162,230.00 USD | 99,360.00 USD | 108,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.30` | 6,790,000.00 USD | 6,790,000.00 USD | 52,350.00 USD | 31,630.00 USD | 26,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.30` | 10,210,000.00 USD | 10,210,000.00 USD | 133,350.00 USD | 100,380.00 USD | 170,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.40` | 6,910,000.00 USD | 6,910,000.00 USD | 66,740.00 USD | 13,730.00 USD | 42,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.40` | 10,580,000.00 USD | 10,580,000.00 USD | 64,850.00 USD | 100,560.00 USD | 202,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.50` | 6,990,000.00 USD | 6,990,000.00 USD | 22,700.00 USD | 19,320.00 USD | 36,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.50` | 10,950,000.00 USD | 10,950,000.00 USD | 115,390.00 USD | 80,510.00 USD | 175,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.55` | 217.37 USD | 221,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.60` | 7,060,000.00 USD | 7,060,000.00 USD | 40,710.00 USD | 19,140.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.60` | 11,340,000.00 USD | 11,340,000.00 USD | 251,100.00 USD | 16,970.00 USD | 118,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.65` | 217.73 USD | 221,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.70` | 7,110,000.00 USD | 7,110,000.00 USD | 31,880.00 USD | 22,330.00 USD | 3,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.70` | 11,500,000.00 USD | 11,500,000.00 USD | 102,230.00 USD | 48,240.00 USD | 15,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.80` | 7,190,000.00 USD | 7,190,000.00 USD | 11,060.00 USD | 12,980.00 USD | 47,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.80` | 11,660,000.00 USD | 11,660,000.00 USD | 46,960.00 USD | 28,960.00 USD | 76,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.85` | 218.45 USD | 222,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.90` | 7,270,000.00 USD | 7,270,000.00 USD | 36,520.00 USD | 23,250.00 USD | 22,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.90` | 11,860,000.00 USD | 11,860,000.00 USD | 105,970.00 USD | 33,290.00 USD | 64,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.95` | 397.39 USD | 222,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.00` | 7,340,000.00 USD | 7,340,000.00 USD | 43,930.00 USD | 6,430.00 USD | 18,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 11,910,000.00 USD | 11,910,000.00 USD | 43,120.00 USD | 11,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.10` | 7,380,000.00 USD | 7,380,000.00 USD | 13,270.00 USD | 14,950.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 11,960,000.00 USD | 11,960,000.00 USD | 31,540.00 USD | 10,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.20` | 7,490,000.00 USD | 7,490,000.00 USD | 75,070.00 USD | 1,880.00 USD | 39,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.20` | 12,080,000.00 USD | 12,080,000.00 USD | 51,210.00 USD | 20,920.00 USD | 47,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.30` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 4,040.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.30` | 12,130,000.00 USD | 12,130,000.00 USD | 16,510.00 USD | 13,210.00 USD | 24,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.40` | 7,510,000.00 USD | 7,510,000.00 USD | 1,190.00 USD | 709.61 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.40` | 12,260,000.00 USD | 12,260,000.00 USD | 62,340.00 USD | 25,720.00 USD | 43,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.50` | 7,520,000.00 USD | 7,520,000.00 USD | 1,060.00 USD | 3,880.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.50` | 12,360,000.00 USD | 12,360,000.00 USD | 17,710.00 USD | 42,440.00 USD | 41,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.55` | 220.96 USD | 222,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.60` | 7,540,000.00 USD | 7,540,000.00 USD | 9,250.00 USD | 11,890.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.60` | 12,580,000.00 USD | 12,580,000.00 USD | 32,920.00 USD | 58,350.00 USD | 121,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.70` | 7,570,000.00 USD | 7,570,000.00 USD | 13,890.00 USD | 8,790.00 USD | 10,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.70` | 12,770,000.00 USD | 12,770,000.00 USD | 82,860.00 USD | 10,880.00 USD | 99,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.80` | 7,600,000.00 USD | 7,600,000.00 USD | 9,150.00 USD | 3,440.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.80` | 13,040,000.00 USD | 13,040,000.00 USD | 169,680.00 USD | 25,670.00 USD | 71,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.90` | 7,620,000.00 USD | 7,620,000.00 USD | 5,210.00 USD | 1,580.00 USD | 11,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.90` | 13,180,000.00 USD | 13,180,000.00 USD | 73,690.00 USD | 32,820.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.00` | 7,640,000.00 USD | 7,640,000.00 USD | 12,550.00 USD | 3,100.00 USD | 8,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.00` | 13,280,000.00 USD | 13,280,000.00 USD | 50,080.00 USD | 8,550.00 USD | 40,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `62.05` | 222.76 USD | 222,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `62.10` | 13,290,000.00 USD | 13,290,000.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.20` | 13,410,000.00 USD | 13,410,000.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.30` | 13,560,000.00 USD | 13,560,000.00 USD | 27,500.00 USD | 23,450.00 USD | 97,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.40` | 13,680,000.00 USD | 13,680,000.00 USD | 74,860.00 USD | 27,560.00 USD | 25,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.50` | 13,760,000.00 USD | 13,760,000.00 USD | 36,690.00 USD | 12,720.00 USD | 25,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `62.95` | 138.49 USD | 223,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `63.45` | 3,350.00 USD | 226,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `63.55` | 8,180.00 USD | 234,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.05` | 121.36 USD | 234,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.85` | 709.03 USD | 235,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `70.25` | 40,610.00 USD | 276,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `76.35` | 8,380.00 USD | 284,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.75` | 578,460.00 USD | 862,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.85` | 713.88 USD | 863,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.25` | 3,210.00 USD | 866,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.75` | 646.00 USD | 867,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.05` | 19,000.00 USD | 886,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.55` | 123.96 USD | 886,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.75` | 214.32 USD | 886,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `83.15` | 883.88 USD | 887,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `83.75` | 2,760.00 USD | 890,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `83.85` | 22,370.00 USD | 912,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `84.45` | 765.96 USD | 913,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `89.45` | 100.18 USD | 913,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `91.95` | 121.37 USD | 913,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.05` | 2,450.00 USD | 916,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.35` | 166.21 USD | 916,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.55` | 31,070.00 USD | 947,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.25` | 213.71 USD | 947,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.85` | 2,320.00 USD | 950,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.45` | 355,790.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.75` | 1,620.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.85` | 1,860.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.15` | 199.30 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.05` | 6,470.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 664.59 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `11.35` | 3,050,000.00 USD | 0.00 USD | 136.20 USD | `-79.53%` | `12.00` |
| `Live` | `Long` | `11.45` | 3,050,000.00 USD | 0.00 USD | 133.51 USD | `-79.35%` | `11.66` |
| `Live` | `Long` | `12.25` | 3,050,000.00 USD | 0.00 USD | 122.50 USD | `-77.91%` | `10.00` |
| `Live` | `Long` | `12.75` | 3,050,000.00 USD | 0.00 USD | 2,560.00 USD | `-77.01%` | `200.43` |
| `Live` | `Long` | `13.15` | 3,040,000.00 USD | 0.00 USD | 2,220.00 USD | `-76.29%` | `168.79` |
| `Live` | `Long` | `13.65` | 3,040,000.00 USD | 0.00 USD | 150.15 USD | `-75.39%` | `11.00` |
| `Live` | `Long` | `18.25` | 3,040,000.00 USD | 0.00 USD | 16,970.00 USD | `-67.09%` | `930.00` |
| `Live` | `Long` | `18.45` | 3,020,000.00 USD | 0.00 USD | 4,990.00 USD | `-66.73%` | `270.57` |
| `Live` | `Long` | `19.05` | 3,020,000.00 USD | 0.00 USD | 3,470.00 USD | `-65.65%` | `182.00` |
| `Live` | `Long` | `19.25` | 3,020,000.00 USD | 0.00 USD | 173.63 USD | `-65.29%` | `9.02` |
| `Live` | `Long` | `19.45` | 3,020,000.00 USD | 0.00 USD | 2,010.00 USD | `-64.93%` | `103.47` |
| `Live` | `Long` | `20.25` | 3,010,000.00 USD | 0.00 USD | 133.65 USD | `-63.49%` | `6.60` |
| `Live` | `Long` | `21.85` | 3,010,000.00 USD | 0.00 USD | 4,260.00 USD | `-60.60%` | `195.03` |
| `Live` | `Long` | `22.55` | 3,010,000.00 USD | 0.00 USD | 2,220.00 USD | `-59.34%` | `98.37` |
| `Live` | `Long` | `23.25` | 3,010,000.00 USD | 0.00 USD | 986.50 USD | `-58.08%` | `42.43` |
| `Live` | `Long` | `23.85` | 3,010,000.00 USD | 0.00 USD | 195.57 USD | `-56.99%` | `8.20` |
| `Live` | `Long` | `23.95` | 3,010,000.00 USD | 0.00 USD | 378.89 USD | `-56.81%` | `15.82` |
| `Live` | `Long` | `24.65` | 3,000,000.00 USD | 0.00 USD | 447.40 USD | `-55.55%` | `18.15` |
| `Live` | `Long` | `25.25` | 3,000,000.00 USD | 0.00 USD | 277,980.00 USD | `-54.47%` | `11,009.19` |
| `Live` | `Long` | `25.35` | 2,730,000.00 USD | 0.00 USD | 173.39 USD | `-54.29%` | `6.84` |
| `Live` | `Long` | `25.55` | 2,730,000.00 USD | 0.00 USD | 167,420.00 USD | `-53.93%` | `6,552.65` |
| `Live` | `Long` | `25.65` | 2,560,000.00 USD | 0.00 USD | 1,240.00 USD | `-53.75%` | `48.40` |
| `Live` | `Long` | `25.85` | 2,560,000.00 USD | 0.00 USD | 7,620.00 USD | `-53.39%` | `294.67` |
| `Live` | `Long` | `25.95` | 2,550,000.00 USD | 0.00 USD | 374.20 USD | `-53.21%` | `14.42` |
| `Live` | `Long` | `26.85` | 2,550,000.00 USD | 0.00 USD | 1,050.00 USD | `-51.58%` | `38.92` |
| `Live` | `Long` | `27.05` | 2,550,000.00 USD | 0.00 USD | 5,510.00 USD | `-51.22%` | `203.85` |
| `Live` | `Long` | `27.55` | 2,540,000.00 USD | 0.00 USD | 272.75 USD | `-50.32%` | `9.90` |
| `Live` | `Long` | `27.95` | 2,540,000.00 USD | 0.00 USD | 173.85 USD | `-49.60%` | `6.22` |
| `Live` | `Long` | `29.15` | 2,540,000.00 USD | 0.00 USD | 755.28 USD | `-47.44%` | `25.91` |
| `Live` | `Long` | `29.75` | 2,540,000.00 USD | 0.00 USD | 297,500.00 USD | `-46.36%` | `10,000.00` |
| `Live` | `Long` | `29.95` | 2,240,000.00 USD | 0.00 USD | 220.43 USD | `-46.00%` | `7.36` |
| `Live` | `Long` | `30.05` | 2,240,000.00 USD | 0.00 USD | 218.46 USD | `-45.81%` | `7.27` |
| `Live` | `Long` | `30.55` | 2,240,000.00 USD | 0.00 USD | 152.75 USD | `-44.91%` | `5.00` |
| `Live` | `Long` | `30.65` | 2,240,000.00 USD | 0.00 USD | 1,540.00 USD | `-44.73%` | `50.19` |
| `Live` | `Long` | `30.95` | 2,240,000.00 USD | 0.00 USD | 538.53 USD | `-44.19%` | `17.40` |
| `Live` | `Long` | `31.15` | 2,240,000.00 USD | 0.00 USD | 27,620.00 USD | `-43.83%` | `886.80` |
| `Live` | `Long` | `31.55` | 2,210,000.00 USD | 0.00 USD | 1,060.00 USD | `-43.11%` | `33.49` |
| `Live` | `Long` | `31.65` | 2,210,000.00 USD | 0.00 USD | 4,640.00 USD | `-42.93%` | `146.53` |
| `Live` | `Long` | `31.85` | 2,210,000.00 USD | 0.00 USD | 2,870.00 USD | `-42.57%` | `90.00` |
| `Live` | `Long` | `31.95` | 2,210,000.00 USD | 0.00 USD | 125.24 USD | `-42.39%` | `3.92` |
| `Live` | `Long` | `32.15` | 2,210,000.00 USD | 0.00 USD | 450.10 USD | `-42.03%` | `14.00` |
| `Live` | `Long` | `32.25` | 2,200,000.00 USD | 0.00 USD | 225.75 USD | `-41.85%` | `7.00` |
| `Live` | `Long` | `32.35` | 2,200,000.00 USD | 0.00 USD | 172.10 USD | `-41.67%` | `5.32` |
| `Live` | `Long` | `32.65` | 2,200,000.00 USD | 0.00 USD | 3,440.00 USD | `-41.13%` | `105.43` |
| `Live` | `Long` | `32.75` | 2,200,000.00 USD | 0.00 USD | 953.68 USD | `-40.95%` | `29.12` |
| `Live` | `Long` | `32.95` | 2,200,000.00 USD | 0.00 USD | 32,950.00 USD | `-40.59%` | `1,000.01` |
| `Live` | `Long` | `33.05` | 2,170,000.00 USD | 0.00 USD | 4,100.00 USD | `-40.41%` | `124.01` |
| `Live` | `Long` | `33.35` | 2,160,000.00 USD | 0.00 USD | 5,810.00 USD | `-39.86%` | `174.22` |
| `Live` | `Long` | `33.65` | 2,160,000.00 USD | 0.00 USD | 257.76 USD | `-39.32%` | `7.66` |
| `Live` | `Long` | `33.85` | 2,160,000.00 USD | 0.00 USD | 259.63 USD | `-38.96%` | `7.67` |
| `Live` | `Long` | `34.05` | 2,160,000.00 USD | 0.00 USD | 10,400.00 USD | `-38.60%` | `305.37` |
| `Live` | `Long` | `34.15` | 2,150,000.00 USD | 0.00 USD | 126.70 USD | `-38.42%` | `3.71` |
| `Live` | `Long` | `34.45` | 2,150,000.00 USD | 0.00 USD | 67,610.00 USD | `-37.88%` | `1,962.61` |
| `Live` | `Long` | `34.65` | 2,080,000.00 USD | 0.00 USD | 8,200.00 USD | `-37.52%` | `236.68` |
| `Live` | `Long` | `34.95` | 2,070,000.00 USD | 0.00 USD | 104.85 USD | `-36.98%` | `3.00` |
| `Live` | `Long` | `35.05` | 2,070,000.00 USD | 0.00 USD | 166.49 USD | `-36.80%` | `4.75` |
| `Live` | `Long` | `35.35` | 2,070,000.00 USD | 0.00 USD | 421.37 USD | `-36.26%` | `11.92` |
| `Live` | `Long` | `36.35` | 2,070,000.00 USD | 0.00 USD | 3,020.00 USD | `-34.45%` | `83.03` |
| `Live` | `Long` | `36.45` | 2,070,000.00 USD | 0.00 USD | 423.18 USD | `-34.27%` | `11.61` |
| `Live` | `Long` | `36.65` | 2,070,000.00 USD | 0.00 USD | 3,000.00 USD | `-33.91%` | `81.91` |
| `Live` | `Long` | `36.75` | 2,060,000.00 USD | 0.00 USD | 101.80 USD | `-33.73%` | `2.77` |
| `Live` | `Long` | `37.05` | 2,060,000.00 USD | 0.00 USD | 110.78 USD | `-33.19%` | `2.99` |
| `Live` | `Long` | `37.15` | 2,060,000.00 USD | 0.00 USD | 2,750.00 USD | `-33.01%` | `73.91` |
| `Live` | `Long` | `37.35` | 2,060,000.00 USD | 0.00 USD | 9,260.00 USD | `-32.65%` | `247.91` |
| `Live` | `Long` | `37.55` | 2,050,000.00 USD | 0.00 USD | 3,530.00 USD | `-32.29%` | `94.04` |
| `Live` | `Long` | `37.75` | 2,050,000.00 USD | 0.00 USD | 377.50 USD | `-31.93%` | `10.00` |
| `Live` | `Long` | `37.85` | 2,050,000.00 USD | 0.00 USD | 6,210.00 USD | `-31.75%` | `164.03` |
| `Live` | `Long` | `37.95` | 2,040,000.00 USD | 0.00 USD | 446.67 USD | `-31.57%` | `11.77` |
| `Live` | `Long` | `38.25` | 2,040,000.00 USD | 0.00 USD | 695.38 USD | `-31.03%` | `18.18` |
| `Live` | `Long` | `38.35` | 2,040,000.00 USD | 0.00 USD | 847.54 USD | `-30.85%` | `22.10` |
| `Live` | `Long` | `38.45` | 2,040,000.00 USD | 0.00 USD | 2,400.00 USD | `-30.67%` | `62.34` |
| `Live` | `Long` | `38.55` | 2,040,000.00 USD | 0.00 USD | 993.82 USD | `-30.49%` | `25.78` |
| `Live` | `Long` | `38.65` | 2,040,000.00 USD | 0.00 USD | 4,280.00 USD | `-30.31%` | `110.74` |
| `Live` | `Long` | `38.95` | 2,030,000.00 USD | 0.00 USD | 2,730.00 USD | `-29.77%` | `70.00` |
| `Live` | `Long` | `39.05` | 2,030,000.00 USD | 0.00 USD | 664,760.00 USD | `-29.59%` | `17,023.28` |
| `Live` | `Long` | `39.15` | 1,360,000.00 USD | 0.00 USD | 570.02 USD | `-29.41%` | `14.56` |
| `Live` | `Long` | `39.25` | 1,360,000.00 USD | 0.00 USD | 340.30 USD | `-29.23%` | `8.67` |
| `Live` | `Long` | `39.35` | 1,360,000.00 USD | 0.00 USD | 264.83 USD | `-29.05%` | `6.73` |
| `Live` | `Long` | `39.45` | 1,360,000.00 USD | 0.00 USD | 716.41 USD | `-28.87%` | `18.16` |
| `Live` | `Long` | `39.55` | 1,360,000.00 USD | 0.00 USD | 312.44 USD | `-28.68%` | `7.90` |
| `Live` | `Long` | `39.65` | 1,360,000.00 USD | 0.00 USD | 5,900.00 USD | `-28.50%` | `148.78` |
| `Live` | `Long` | `39.75` | 1,360,000.00 USD | 0.00 USD | 1,180.00 USD | `-28.32%` | `29.57` |
| `Live` | `Long` | `39.85` | 1,350,000.00 USD | 0.00 USD | 133.10 USD | `-28.14%` | `3.34` |
| `Live` | `Long` | `40.05` | 1,350,000.00 USD | 0.00 USD | 2,160.00 USD | `-27.78%` | `53.97` |
| `Live` | `Long` | `40.45` | 1,350,000.00 USD | 0.00 USD | 1,010.00 USD | `-27.06%` | `24.92` |
| `Live` | `Long` | `40.55` | 1,350,000.00 USD | 0.00 USD | 133.00 USD | `-26.88%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,350,000.00 USD | 0.00 USD | 40,920.00 USD | `-26.70%` | `1,006.75` |
| `Live` | `Long` | `40.85` | 1,310,000.00 USD | 0.00 USD | 6,340.00 USD | `-26.34%` | `155.23` |
| `Live` | `Long` | `40.95` | 1,300,000.00 USD | 0.00 USD | 509.01 USD | `-26.16%` | `12.43` |
| `Live` | `Long` | `41.05` | 1,300,000.00 USD | 0.00 USD | 396.54 USD | `-25.98%` | `9.66` |
| `Live` | `Long` | `41.15` | 1,300,000.00 USD | 0.00 USD | 5,430.00 USD | `-25.80%` | `131.94` |
| `Live` | `Long` | `41.25` | 1,300,000.00 USD | 0.00 USD | 14,850.00 USD | `-25.62%` | `359.91` |
| `Live` | `Long` | `41.35` | 1,280,000.00 USD | 0.00 USD | 9,100.00 USD | `-25.44%` | `220.00` |
| `Live` | `Long` | `41.45` | 1,270,000.00 USD | 0.00 USD | 644.96 USD | `-25.26%` | `15.56` |
| `Live` | `Long` | `41.65` | 1,270,000.00 USD | 0.00 USD | 1,040.00 USD | `-24.90%` | `24.93` |
| `Live` | `Long` | `42.05` | 1,270,000.00 USD | 0.00 USD | 201.00 USD | `-24.18%` | `4.78` |
| `Live` | `Long` | `42.15` | 1,270,000.00 USD | 0.00 USD | 66,300.00 USD | `-24.00%` | `1,572.94` |
| `Live` | `Long` | `42.25` | 1,210,000.00 USD | 0.00 USD | 35,410.00 USD | `-23.82%` | `838.00` |
| `Live` | `Long` | `42.35` | 1,170,000.00 USD | 0.00 USD | 301.96 USD | `-23.64%` | `7.13` |
| `Live` | `Long` | `42.55` | 1,170,000.00 USD | 0.00 USD | 682.50 USD | `-23.28%` | `16.04` |
| `Live` | `Long` | `42.65` | 1,170,000.00 USD | 0.00 USD | 1,570.00 USD | `-23.09%` | `36.70` |
| `Live` | `Long` | `42.75` | 1,170,000.00 USD | 0.00 USD | 3,800.00 USD | `-22.91%` | `88.83` |
| `Live` | `Long` | `42.85` | 1,160,000.00 USD | 0.00 USD | 5,800.00 USD | `-22.73%` | `135.38` |
| `Live` | `Long` | `42.95` | 1,160,000.00 USD | 0.00 USD | 2,000.00 USD | `-22.55%` | `46.65` |
| `Live` | `Long` | `43.05` | 1,160,000.00 USD | 0.00 USD | 9,410.00 USD | `-22.37%` | `218.50` |
| `Live` | `Long` | `43.15` | 1,150,000.00 USD | 0.00 USD | 1,580.00 USD | `-22.19%` | `36.59` |
| `Live` | `Long` | `43.25` | 1,140,000.00 USD | 0.00 USD | 121,520.00 USD | `-22.01%` | `2,809.66` |
| `Live` | `Long` | `43.35` | 1,020,000.00 USD | 0.00 USD | 5,390.00 USD | `-21.83%` | `124.24` |
| `Live` | `Long` | `43.45` | 1,020,000.00 USD | 0.00 USD | 710.84 USD | `-21.65%` | `16.36` |
| `Live` | `Long` | `43.65` | 1,020,000.00 USD | 0.00 USD | 3,900.00 USD | `-21.29%` | `89.25` |
| `Live` | `Long` | `43.75` | 1,010,000.00 USD | 0.00 USD | 21,880.00 USD | `-21.11%` | `500.00` |
| `Live` | `Long` | `43.85` | 991,470.00 USD | 0.00 USD | 801.14 USD | `-20.93%` | `18.27` |
| `Live` | `Long` | `43.95` | 990,670.00 USD | 0.00 USD | 5,660.00 USD | `-20.75%` | `128.71` |
| `Live` | `Long` | `44.15` | 985,010.00 USD | 0.00 USD | 2,380.00 USD | `-20.39%` | `53.99` |
| `Live` | `Long` | `44.35` | 982,630.00 USD | 0.00 USD | 84,440.00 USD | `-20.03%` | `1,903.87` |
| `Live` | `Long` | `44.55` | 898,190.00 USD | 0.00 USD | 842.44 USD | `-19.67%` | `18.91` |
| `Live` | `Long` | `44.75` | 897,350.00 USD | 0.00 USD | 5,570.00 USD | `-19.31%` | `124.55` |
| `Live` | `Long` | `44.85` | 891,780.00 USD | 0.00 USD | 134.55 USD | `-19.13%` | `3.00` |
| `Live` | `Long` | `44.95` | 891,640.00 USD | 0.00 USD | 2,620.00 USD | `-18.95%` | `58.18` |
| `Live` | `Long` | `45.05` | 889,030.00 USD | 0.00 USD | 6,190.00 USD | `-18.77%` | `137.31` |
| `Live` | `Long` | `45.15` | 882,840.00 USD | 0.00 USD | 8,710.00 USD | `-18.59%` | `193.00` |
| `Live` | `Long` | `45.25` | 874,130.00 USD | 0.00 USD | 3,180.00 USD | `-18.41%` | `70.37` |
| `Live` | `Long` | `45.35` | 870,940.00 USD | 0.00 USD | 2,180.00 USD | `-18.23%` | `48.02` |
| `Live` | `Long` | `45.45` | 868,760.00 USD | 0.00 USD | 23,940.00 USD | `-18.05%` | `526.65` |
| `Live` | `Long` | `45.55` | 844,830.00 USD | 0.00 USD | 12,060.00 USD | `-17.87%` | `264.81` |
| `Live` | `Long` | `45.65` | 832,770.00 USD | 0.00 USD | 42,180.00 USD | `-17.69%` | `924.03` |
| `Live` | `Long` | `45.95` | 790,580.00 USD | 0.00 USD | 30,970.00 USD | `-17.14%` | `673.93` |
| `Live` | `Long` | `46.05` | 759,620.00 USD | 0.00 USD | 706.41 USD | `-16.96%` | `15.34` |
| `Live` | `Long` | `46.35` | 758,910.00 USD | 0.00 USD | 383.78 USD | `-16.42%` | `8.28` |
| `Live` | `Long` | `46.45` | 758,530.00 USD | 0.00 USD | 22,480.00 USD | `-16.24%` | `483.97` |
| `Live` | `Long` | `46.55` | 736,050.00 USD | 0.00 USD | 2,140.00 USD | `-16.06%` | `45.93` |
| `Live` | `Long` | `46.65` | 733,910.00 USD | 0.00 USD | 4,430.00 USD | `-15.88%` | `95.01` |
| `Live` | `Long` | `46.85` | 729,480.00 USD | 0.00 USD | 358.40 USD | `-15.52%` | `7.65` |
| `Live` | `Long` | `46.95` | 729,120.00 USD | 0.00 USD | 158.22 USD | `-15.34%` | `3.37` |
| `Live` | `Long` | `47.05` | 728,960.00 USD | 0.00 USD | 2,140.00 USD | `-15.16%` | `45.57` |
| `Live` | `Long` | `47.15` | 726,820.00 USD | 0.00 USD | 1,980.00 USD | `-14.98%` | `42.07` |
| `Live` | `Long` | `47.25` | 724,830.00 USD | 0.00 USD | 9,030.00 USD | `-14.80%` | `191.21` |
| `Live` | `Long` | `47.35` | 715,800.00 USD | 0.00 USD | 43,920.00 USD | `-14.62%` | `927.56` |
| `Live` | `Long` | `47.45` | 671,880.00 USD | 0.00 USD | 2,590.00 USD | `-14.44%` | `54.54` |
| `Live` | `Long` | `47.55` | 669,290.00 USD | 0.00 USD | 4,450.00 USD | `-14.26%` | `93.69` |
| `Live` | `Long` | `47.75` | 664,830.00 USD | 0.00 USD | 47,750.00 USD | `-13.90%` | `1,000.00` |
| `Live` | `Long` | `48.05` | 617,080.00 USD | 0.00 USD | 381.04 USD | `-13.36%` | `7.93` |
| `Live` | `Long` | `48.15` | 616,700.00 USD | 0.00 USD | 1,690.00 USD | `-13.18%` | `35.03` |
| `Live` | `Long` | `48.25` | 615,020.00 USD | 0.00 USD | 110.49 USD | `-13.00%` | `2.29` |
| `Live` | `Long` | `48.55` | 614,910.00 USD | 0.00 USD | 2,030.00 USD | `-12.46%` | `41.85` |
| `Live` | `Long` | `48.65` | 612,870.00 USD | 0.00 USD | 8,280.00 USD | `-12.28%` | `170.21` |
| `Live` | `Long` | `48.75` | 604,590.00 USD | 0.00 USD | 333.94 USD | `-12.10%` | `6.85` |
| `Live` | `Long` | `48.95` | 604,260.00 USD | 0.00 USD | 252.58 USD | `-11.74%` | `5.16` |
| `Live` | `Long` | `49.05` | 604,010.00 USD | 0.00 USD | 1,580.00 USD | `-11.55%` | `32.25` |
| `Live` | `Long` | `49.15` | 602,430.00 USD | 0.00 USD | 5,740.00 USD | `-11.37%` | `116.83` |
| `Live` | `Long` | `49.35` | 596,680.00 USD | 0.00 USD | 5,230.00 USD | `-11.01%` | `105.97` |
| `Live` | `Long` | `49.45` | 591,450.00 USD | 0.00 USD | 19,440.00 USD | `-10.83%` | `393.17` |
| `Live` | `Long` | `49.55` | 572,010.00 USD | 0.00 USD | 18,010.00 USD | `-10.65%` | `363.57` |
| `Live` | `Long` | `49.65` | 554,000.00 USD | 0.00 USD | 75,190.00 USD | `-10.47%` | `1,514.31` |
| `Live` | `Long` | `49.75` | 478,810.00 USD | 0.00 USD | 1,250.00 USD | `-10.29%` | `25.06` |
| `Live` | `Long` | `49.95` | 477,560.00 USD | 0.00 USD | 19,920.00 USD | `-9.93%` | `398.70` |
| `Live` | `Long` | `50.05` | 457,650.00 USD | 0.00 USD | 1,820.00 USD | `-9.75%` | `36.43` |
| `Live` | `Long` | `50.25` | 455,830.00 USD | 0.00 USD | 102.51 USD | `-9.39%` | `2.04` |
| `Live` | `Long` | `50.35` | 455,720.00 USD | 0.00 USD | 1,140.00 USD | `-9.21%` | `22.67` |
| `Live` | `Long` | `50.45` | 454,580.00 USD | 0.00 USD | 4,720.00 USD | `-9.03%` | `93.64` |
| `Live` | `Long` | `50.55` | 449,860.00 USD | 0.00 USD | 84,100.00 USD | `-8.85%` | `1,663.61` |
| `Live` | `Long` | `50.75` | 365,760.00 USD | 0.00 USD | 9,050.00 USD | `-8.49%` | `178.28` |
| `Live` | `Long` | `50.95` | 356,710.00 USD | 0.00 USD | 431.55 USD | `-8.13%` | `8.47` |
| `Live` | `Long` | `51.15` | 356,280.00 USD | 0.00 USD | 219,370.00 USD | `-7.77%` | `4,288.79` |
| `Live` | `Long` | `51.25` | 136,910.00 USD | 0.00 USD | 202.44 USD | `-7.59%` | `3.95` |
| `Live` | `Long` | `51.35` | 136,710.00 USD | 0.00 USD | 453.93 USD | `-7.41%` | `8.84` |
| `Live` | `Long` | `51.45` | 136,260.00 USD | 0.00 USD | 27,210.00 USD | `-7.23%` | `528.81` |
| `Live` | `Long` | `51.55` | 109,050.00 USD | 0.00 USD | 551.07 USD | `-7.05%` | `10.69` |
| `Live` | `Long` | `51.65` | 108,500.00 USD | 0.00 USD | 9,100.00 USD | `-6.87%` | `176.09` |
| `Live` | `Long` | `51.75` | 99,400.00 USD | 0.00 USD | 6,480.00 USD | `-6.69%` | `125.17` |
| `Live` | `Long` | `51.85` | 92,920.00 USD | 0.00 USD | 13,680.00 USD | `-6.51%` | `263.89` |
| `Live` | `Long` | `51.95` | 79,240.00 USD | 0.00 USD | 13,950.00 USD | `-6.33%` | `268.48` |
| `Live` | `Long` | `52.05` | 65,290.00 USD | 0.00 USD | 2,860.00 USD | `-6.15%` | `55.00` |
| `Live` | `Long` | `52.15` | 62,430.00 USD | 0.00 USD | 1,900.00 USD | `-5.96%` | `36.36` |
| `Live` | `Long` | `52.25` | 60,540.00 USD | 0.00 USD | 4,930.00 USD | `-5.78%` | `94.33` |
| `Live` | `Long` | `52.35` | 55,610.00 USD | 0.00 USD | 134.02 USD | `-5.60%` | `2.56` |
| `Live` | `Long` | `52.45` | 55,470.00 USD | 0.00 USD | 5,820.00 USD | `-5.42%` | `110.91` |
| `Live` | `Long` | `52.55` | 49,660.00 USD | 0.00 USD | 8,700.00 USD | `-5.24%` | `165.49` |
| `Live` | `Long` | `52.75` | 40,960.00 USD | 0.00 USD | 30,280.00 USD | `-4.88%` | `574.00` |
| `Live` | `Long` | `52.85` | 10,680.00 USD | 0.00 USD | 5,950.00 USD | `-4.70%` | `112.64` |
| `Live` | `Long` | `52.95` | 4,730.00 USD | 0.00 USD | 531.09 USD | `-4.52%` | `10.03` |
| `Live` | `Long` | `53.05` | 4,200.00 USD | 0.00 USD | 202.12 USD | `-4.34%` | `3.81` |
| `Live` | `Long` | `53.15` | 3,990.00 USD | 0.00 USD | 2,030.00 USD | `-4.16%` | `38.15` |
| `Live` | `Long` | `53.25` | 1,970.00 USD | 0.00 USD | 1,030.00 USD | `-3.98%` | `19.25` |
| `Live` | `Long` | `53.35` | 941.09 USD | 0.00 USD | 941.09 USD | `-3.80%` | `17.64` |
| `Live` | `Short` | `56.25` | 700.88 USD | 700.88 USD | 0.00 USD | `+1.43%` | `12.46` |
| `Live` | `Short` | `57.75` | 856.22 USD | 155.35 USD | 0.00 USD | `+4.13%` | `2.69` |
| `Live` | `Short` | `57.95` | 981.97 USD | 125.75 USD | 0.00 USD | `+4.49%` | `2.17` |
| `Live` | `Short` | `58.85` | 2,460.00 USD | 1,480.00 USD | 0.00 USD | `+6.12%` | `25.13` |
| `Live` | `Short` | `59.35` | 11,900.00 USD | 9,440.00 USD | 0.00 USD | `+7.02%` | `159.09` |
| `Live` | `Short` | `59.45` | 12,120.00 USD | 213.43 USD | 0.00 USD | `+7.20%` | `3.59` |
| `Live` | `Short` | `59.55` | 12,330.00 USD | 213.78 USD | 0.00 USD | `+7.38%` | `3.59` |
| `Live` | `Short` | `59.95` | 12,550.00 USD | 215.22 USD | 0.00 USD | `+8.10%` | `3.59` |
| `Live` | `Short` | `60.15` | 221,430.00 USD | 208,880.00 USD | 0.00 USD | `+8.46%` | `3,472.67` |
| `Live` | `Short` | `60.55` | 221,640.00 USD | 217.37 USD | 0.00 USD | `+9.18%` | `3.59` |
| `Live` | `Short` | `60.65` | 221,860.00 USD | 217.73 USD | 0.00 USD | `+9.36%` | `3.59` |
| `Live` | `Short` | `60.85` | 222,080.00 USD | 218.45 USD | 0.00 USD | `+9.72%` | `3.59` |
| `Live` | `Short` | `60.95` | 222,480.00 USD | 397.39 USD | 0.00 USD | `+9.90%` | `6.52` |
| `Live` | `Short` | `61.55` | 222,700.00 USD | 220.96 USD | 0.00 USD | `+10.98%` | `3.59` |
| `Live` | `Short` | `62.05` | 222,920.00 USD | 222.76 USD | 0.00 USD | `+11.89%` | `3.59` |
| `Live` | `Short` | `62.95` | 223,060.00 USD | 138.49 USD | 0.00 USD | `+13.51%` | `2.20` |
| `Live` | `Short` | `63.45` | 226,410.00 USD | 3,350.00 USD | 0.00 USD | `+14.41%` | `52.83` |
| `Live` | `Short` | `63.55` | 234,590.00 USD | 8,180.00 USD | 0.00 USD | `+14.59%` | `128.67` |
| `Live` | `Short` | `67.05` | 234,710.00 USD | 121.36 USD | 0.00 USD | `+20.90%` | `1.81` |
| `Live` | `Short` | `67.85` | 235,420.00 USD | 709.03 USD | 0.00 USD | `+22.34%` | `10.45` |
| `Live` | `Short` | `70.25` | 276,030.00 USD | 40,610.00 USD | 0.00 USD | `+26.67%` | `578.10` |
| `Live` | `Short` | `76.35` | 284,410.00 USD | 8,380.00 USD | 0.00 USD | `+37.67%` | `109.80` |
| `Live` | `Short` | `77.75` | 862,880.00 USD | 578,460.00 USD | 0.00 USD | `+40.20%` | `7,440.05` |
| `Live` | `Short` | `77.85` | 863,590.00 USD | 713.88 USD | 0.00 USD | `+40.38%` | `9.17` |
| `Live` | `Short` | `80.25` | 866,800.00 USD | 3,210.00 USD | 0.00 USD | `+44.70%` | `40.00` |
| `Live` | `Short` | `80.75` | 867,450.00 USD | 646.00 USD | 0.00 USD | `+45.61%` | `8.00` |
| `Live` | `Short` | `81.05` | 886,450.00 USD | 19,000.00 USD | 0.00 USD | `+46.15%` | `234.42` |
| `Live` | `Short` | `81.55` | 886,570.00 USD | 123.96 USD | 0.00 USD | `+47.05%` | `1.52` |
| `Live` | `Short` | `82.75` | 886,790.00 USD | 214.32 USD | 0.00 USD | `+49.21%` | `2.59` |
| `Live` | `Short` | `83.15` | 887,670.00 USD | 883.88 USD | 0.00 USD | `+49.93%` | `10.63` |
| `Live` | `Short` | `83.75` | 890,430.00 USD | 2,760.00 USD | 0.00 USD | `+51.02%` | `33.00` |
| `Live` | `Short` | `83.85` | 912,810.00 USD | 22,370.00 USD | 0.00 USD | `+51.20%` | `266.81` |
| `Live` | `Short` | `84.45` | 913,570.00 USD | 765.96 USD | 0.00 USD | `+52.28%` | `9.07` |
| `Live` | `Short` | `89.45` | 913,670.00 USD | 100.18 USD | 0.00 USD | `+61.29%` | `1.12` |
| `Live` | `Short` | `91.95` | 913,790.00 USD | 121.37 USD | 0.00 USD | `+65.80%` | `1.32` |
| `Live` | `Short` | `98.05` | 916,240.00 USD | 2,450.00 USD | 0.00 USD | `+76.80%` | `25.00` |
| `Live` | `Short` | `98.35` | 916,410.00 USD | 166.21 USD | 0.00 USD | `+77.34%` | `1.69` |
| `Live` | `Short` | `103.55` | 947,480.00 USD | 31,070.00 USD | 0.00 USD | `+86.72%` | `300.00` |
| `Live` | `Short` | `104.25` | 947,690.00 USD | 213.71 USD | 0.00 USD | `+87.98%` | `2.05` |
| `Live` | `Short` | `104.85` | 950,010.00 USD | 2,320.00 USD | 0.00 USD | `+89.06%` | `22.13` |
| `Live` | `Short` | `105.45` | 1,310,000.00 USD | 355,790.00 USD | 0.00 USD | `+90.14%` | `3,374.01` |
| `Live` | `Short` | `106.75` | 1,310,000.00 USD | 1,620.00 USD | 0.00 USD | `+92.49%` | `15.16` |
| `Live` | `Short` | `106.85` | 1,310,000.00 USD | 1,860.00 USD | 0.00 USD | `+92.67%` | `17.43` |
| `Live` | `Short` | `107.15` | 1,310,000.00 USD | 199.30 USD | 0.00 USD | `+93.21%` | `1.86` |
| `Live` | `Short` | `108.05` | 1,320,000.00 USD | 6,470.00 USD | 0.00 USD | `+94.83%` | `59.91` |
| `Live` | `Short` | `110.95` | 1,320,000.00 USD | 664.59 USD | 0.00 USD | `+100.06%` | `5.99` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 840,520.00 USD | 0.00 USD | 392.18 USD | `-63.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 840,120.00 USD | 0.00 USD | 2,310.00 USD | `-60.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 837,820.00 USD | 0.00 USD | 806.86 USD | `-54.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 837,010.00 USD | 0.00 USD | 1,560.00 USD | `-54.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 835,450.00 USD | 0.00 USD | 410.25 USD | `-50.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 835,040.00 USD | 0.00 USD | 281.57 USD | `-45.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 834,760.00 USD | 0.00 USD | 36,050.00 USD | `-35.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 798,710.00 USD | 0.00 USD | 37,550.00 USD | `-32.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 761,160.00 USD | 0.00 USD | 447.01 USD | `-31.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.35` | 760,710.00 USD | 0.00 USD | 73,350.00 USD | `-30.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 687,370.00 USD | 0.00 USD | 40,560.00 USD | `-29.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 646,810.00 USD | 0.00 USD | 489.57 USD | `-28.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 646,320.00 USD | 0.00 USD | 1,180.00 USD | `-27.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 645,140.00 USD | 0.00 USD | 9,840.00 USD | `-27.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 635,300.00 USD | 0.00 USD | 2,060.00 USD | `-26.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.05` | 633,250.00 USD | 0.00 USD | 2,060.00 USD | `-25.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 631,190.00 USD | 0.00 USD | 2,960.00 USD | `-25.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 628,230.00 USD | 0.00 USD | 4,010.00 USD | `-24.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.65` | 624,210.00 USD | 0.00 USD | 3,000.00 USD | `-23.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 621,210.00 USD | 0.00 USD | 5,680.00 USD | `-22.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 615,530.00 USD | 0.00 USD | 672.22 USD | `-20.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.35` | 614,860.00 USD | 0.00 USD | 329,970.00 USD | `-20.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 284,890.00 USD | 0.00 USD | 569.85 USD | `-19.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 284,320.00 USD | 0.00 USD | 223.20 USD | `-19.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 284,100.00 USD | 0.00 USD | 391.13 USD | `-19.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 283,710.00 USD | 0.00 USD | 7,080.00 USD | `-18.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 276,630.00 USD | 0.00 USD | 1,370.00 USD | `-17.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 275,270.00 USD | 0.00 USD | 553.80 USD | `-16.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.35` | 274,710.00 USD | 0.00 USD | 2,970.00 USD | `-16.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.45` | 271,740.00 USD | 0.00 USD | 3,080.00 USD | `-16.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 268,660.00 USD | 0.00 USD | 14,000.00 USD | `-15.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 254,670.00 USD | 0.00 USD | 158.56 USD | `-15.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 254,510.00 USD | 0.00 USD | 373.28 USD | `-14.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 254,140.00 USD | 0.00 USD | 849.46 USD | `-14.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 253,290.00 USD | 0.00 USD | 1,150.00 USD | `-13.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 252,140.00 USD | 0.00 USD | 129.25 USD | `-13.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.15` | 252,010.00 USD | 0.00 USD | 303.35 USD | `-13.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 251,710.00 USD | 0.00 USD | 1,740.00 USD | `-11.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 249,960.00 USD | 0.00 USD | 981.00 USD | `-11.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.35` | 248,980.00 USD | 0.00 USD | 817.24 USD | `-11.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 248,170.00 USD | 0.00 USD | 237.85 USD | `-10.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.55` | 247,930.00 USD | 0.00 USD | 879.51 USD | `-10.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.85` | 247,050.00 USD | 0.00 USD | 108.17 USD | `-10.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 246,940.00 USD | 0.00 USD | 298.20 USD | `-9.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 246,640.00 USD | 0.00 USD | 34,670.00 USD | `-9.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 211,970.00 USD | 0.00 USD | 6,410.00 USD | `-9.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 205,550.00 USD | 0.00 USD | 459.70 USD | `-9.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 205,100.00 USD | 0.00 USD | 236.57 USD | `-8.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 204,860.00 USD | 0.00 USD | 1,020.00 USD | `-7.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 203,840.00 USD | 0.00 USD | 439.89 USD | `-7.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.45` | 203,400.00 USD | 0.00 USD | 204.26 USD | `-7.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 203,190.00 USD | 0.00 USD | 11,560.00 USD | `-6.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.85` | 191,630.00 USD | 0.00 USD | 106.29 USD | `-6.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.95` | 191,530.00 USD | 0.00 USD | 8,700.00 USD | `-6.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 182,830.00 USD | 0.00 USD | 27,140.00 USD | `-6.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.25` | 155,690.00 USD | 0.00 USD | 140.03 USD | `-5.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 155,550.00 USD | 0.00 USD | 18,390.00 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 137,150.00 USD | 0.00 USD | 5,460.00 USD | `-5.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 131,700.00 USD | 0.00 USD | 271.13 USD | `-4.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.85` | 131,430.00 USD | 0.00 USD | 2,840.00 USD | `-4.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 128,580.00 USD | 0.00 USD | 115.43 USD | `-4.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 128,470.00 USD | 0.00 USD | 9,340.00 USD | `-4.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 119,120.00 USD | 0.00 USD | 2,660.00 USD | `-4.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.25` | 116,470.00 USD | 0.00 USD | 881.82 USD | `-3.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.35` | 115,580.00 USD | 0.00 USD | 25,130.00 USD | `-3.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 90,460.00 USD | 0.00 USD | 566.57 USD | `-3.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 89,890.00 USD | 0.00 USD | 5,950.00 USD | `-3.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 83,940.00 USD | 0.00 USD | 1,370.00 USD | `-3.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.75` | 82,570.00 USD | 0.00 USD | 52,980.00 USD | `-3.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 29,590.00 USD | 0.00 USD | 462.03 USD | `-2.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 29,130.00 USD | 0.00 USD | 6,010.00 USD | `-2.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.15` | 23,120.00 USD | 0.00 USD | 398.54 USD | `-2.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 22,720.00 USD | 0.00 USD | 3,090.00 USD | `-2.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 19,630.00 USD | 0.00 USD | 958.73 USD | `-2.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.45` | 18,670.00 USD | 0.00 USD | 144.29 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.55` | 18,530.00 USD | 0.00 USD | 788.25 USD | `-1.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.65` | 17,740.00 USD | 0.00 USD | 13,660.00 USD | `-1.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.75` | 4,080.00 USD | 0.00 USD | 198.74 USD | `-1.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 3,880.00 USD | 0.00 USD | 398.21 USD | `-1.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.95` | 3,480.00 USD | 0.00 USD | 909.97 USD | `-0.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 2,570.00 USD | 0.00 USD | 160.75 USD | `-0.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.15` | 2,410.00 USD | 0.00 USD | 101.48 USD | `-0.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.25` | 2,310.00 USD | 0.00 USD | 914.94 USD | `-0.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.35` | 1,390.00 USD | 0.00 USD | 198.71 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.45` | 1,190.00 USD | 0.00 USD | 1,190.00 USD | `-0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.55` | 156.65 USD | 156.65 USD | 0.00 USD | `+0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.65` | 355.32 USD | 198.67 USD | 0.00 USD | `+0.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.75` | 753.38 USD | 398.06 USD | 0.00 USD | `+0.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.85` | 1,550.00 USD | 797.54 USD | 0.00 USD | `+0.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.95` | 1,740.00 USD | 193.03 USD | 0.00 USD | `+0.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.05` | 2,380.00 USD | 632.24 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.15` | 2,570.00 USD | 197.65 USD | 0.00 USD | `+1.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.25` | 2,780.00 USD | 204.19 USD | 0.00 USD | `+1.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.35` | 3,170.00 USD | 387.12 USD | 0.00 USD | `+1.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.45` | 3,570.00 USD | 407.57 USD | 0.00 USD | `+1.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.55` | 3,780.00 USD | 203.01 USD | 0.00 USD | `+1.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.65` | 4,300.00 USD | 527.98 USD | 0.00 USD | `+2.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.75` | 4,510.00 USD | 203.73 USD | 0.00 USD | `+2.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.85` | 4,710.00 USD | 204.09 USD | 0.00 USD | `+2.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.95` | 5,890.00 USD | 1,170.00 USD | 0.00 USD | `+2.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.05` | 6,480.00 USD | 596.17 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.15` | 6,690.00 USD | 204.03 USD | 0.00 USD | `+3.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.25` | 8,120.00 USD | 1,440.00 USD | 0.00 USD | `+3.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.35` | 8,330.00 USD | 207.03 USD | 0.00 USD | `+3.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.45` | 8,680.00 USD | 344.70 USD | 0.00 USD | `+3.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.55` | 8,900.00 USD | 218.69 USD | 0.00 USD | `+3.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.65` | 9,010.00 USD | 118.18 USD | 0.00 USD | `+3.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.75` | 9,130.00 USD | 119.54 USD | 0.00 USD | `+4.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 9,880.00 USD | 747.68 USD | 0.00 USD | `+4.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 10,080.00 USD | 200.04 USD | 0.00 USD | `+4.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 10,280.00 USD | 200.96 USD | 0.00 USD | `+5.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 10,410.00 USD | 123.70 USD | 0.00 USD | `+5.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 11,010.00 USD | 601.45 USD | 0.00 USD | `+5.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 11,620.00 USD | 611.85 USD | 0.00 USD | `+5.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.65` | 11,890.00 USD | 274.48 USD | 0.00 USD | `+5.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 12,380.00 USD | 491.15 USD | 0.00 USD | `+5.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 15,330.00 USD | 2,940.00 USD | 0.00 USD | `+6.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 15,460.00 USD | 129.69 USD | 0.00 USD | `+6.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 20,260.00 USD | 4,800.00 USD | 0.00 USD | `+6.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 21,540.00 USD | 1,280.00 USD | 0.00 USD | `+6.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.25` | 21,750.00 USD | 210.34 USD | 0.00 USD | `+6.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 22,210.00 USD | 461.74 USD | 0.00 USD | `+7.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 22,370.00 USD | 159.92 USD | 0.00 USD | `+7.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 23,090.00 USD | 724.75 USD | 0.00 USD | `+7.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 23,250.00 USD | 158.00 USD | 0.00 USD | `+7.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 23,420.00 USD | 171.14 USD | 0.00 USD | `+8.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 23,970.00 USD | 551.00 USD | 0.00 USD | `+8.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.45` | 24,130.00 USD | 155.36 USD | 0.00 USD | `+9.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 25,010.00 USD | 878.58 USD | 0.00 USD | `+9.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 26,390.00 USD | 1,390.00 USD | 0.00 USD | `+9.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 27,380.00 USD | 986.99 USD | 0.00 USD | `+9.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 28,050.00 USD | 674.72 USD | 0.00 USD | `+9.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 30,420.00 USD | 2,360.00 USD | 0.00 USD | `+10.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 30,540.00 USD | 125.56 USD | 0.00 USD | `+10.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 34,140.00 USD | 3,600.00 USD | 0.00 USD | `+10.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 34,780.00 USD | 643.20 USD | 0.00 USD | `+10.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 34,910.00 USD | 130.31 USD | 0.00 USD | `+11.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.35` | 36,010.00 USD | 1,100.00 USD | 0.00 USD | `+12.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 36,730.00 USD | 716.72 USD | 0.00 USD | `+12.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 36,960.00 USD | 231.39 USD | 0.00 USD | `+13.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 37,590.00 USD | 630.87 USD | 0.00 USD | `+13.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 38,290.00 USD | 703.97 USD | 0.00 USD | `+14.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 38,960.00 USD | 668.13 USD | 0.00 USD | `+14.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 49,380.00 USD | 10,420.00 USD | 0.00 USD | `+14.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 49,940.00 USD | 555.03 USD | 0.00 USD | `+14.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 50,470.00 USD | 531.62 USD | 0.00 USD | `+15.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.35` | 51,130.00 USD | 664.09 USD | 0.00 USD | `+16.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.45` | 51,800.00 USD | 665.12 USD | 0.00 USD | `+16.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 52,000.00 USD | 202.69 USD | 0.00 USD | `+16.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 52,300.00 USD | 298.04 USD | 0.00 USD | `+16.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 52,400.00 USD | 102.13 USD | 0.00 USD | `+17.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 52,940.00 USD | 540.09 USD | 0.00 USD | `+17.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 53,040.00 USD | 100.79 USD | 0.00 USD | `+18.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 53,310.00 USD | 262.20 USD | 0.00 USD | `+18.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 53,680.00 USD | 371.49 USD | 0.00 USD | `+18.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 54,370.00 USD | 696.17 USD | 0.00 USD | `+19.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 54,910.00 USD | 534.00 USD | 0.00 USD | `+20.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 65,990.00 USD | 11,080.00 USD | 0.00 USD | `+20.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 72,690.00 USD | 6,710.00 USD | 0.00 USD | `+20.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.05` | 75,050.00 USD | 2,360.00 USD | 0.00 USD | `+22.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 79,920.00 USD | 4,860.00 USD | 0.00 USD | `+23.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 80,120.00 USD | 204.48 USD | 0.00 USD | `+25.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.65` | 598,320.00 USD | 518,200.00 USD | 0.00 USD | `+25.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 599,130.00 USD | 810.02 USD | 0.00 USD | `+26.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 919,020.00 USD | 319,890.00 USD | 0.00 USD | `+26.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 919,190.00 USD | 170.04 USD | 0.00 USD | `+27.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 924,960.00 USD | 5,770.00 USD | 0.00 USD | `+27.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 925,230.00 USD | 269.28 USD | 0.00 USD | `+28.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 925,520.00 USD | 291.40 USD | 0.00 USD | `+29.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 932,740.00 USD | 7,220.00 USD | 0.00 USD | `+29.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 932,890.00 USD | 156.78 USD | 0.00 USD | `+30.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 936,120.00 USD | 3,220.00 USD | 0.00 USD | `+31.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 936,530.00 USD | 411.14 USD | 0.00 USD | `+32.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 1,060,000.00 USD | 123,190.00 USD | 0.00 USD | `+33.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 1,060,000.00 USD | 1,020.00 USD | 0.00 USD | `+34.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.75` | 1,060,000.00 USD | 811.04 USD | 0.00 USD | `+34.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 1,060,000.00 USD | 104.93 USD | 0.00 USD | `+35.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 1,060,000.00 USD | 133.59 USD | 0.00 USD | `+35.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 1,060,000.00 USD | 402.59 USD | 0.00 USD | `+35.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.85` | 1,060,000.00 USD | 308.71 USD | 0.00 USD | `+36.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 1,060,000.00 USD | 315.18 USD | 0.00 USD | `+39.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 1,120,000.00 USD | 59,310.00 USD | 0.00 USD | `+41.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 1,130,000.00 USD | 3,160.00 USD | 0.00 USD | `+42.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.35` | 1,130,000.00 USD | 5,260.00 USD | 0.00 USD | `+43.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 1,140,000.00 USD | 5,690.00 USD | 0.00 USD | `+43.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 1,170,000.00 USD | 36,590.00 USD | 0.00 USD | `+44.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 1,170,000.00 USD | 433.89 USD | 0.00 USD | `+45.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 1,170,000.00 USD | 172.64 USD | 0.00 USD | `+46.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 1,170,000.00 USD | 164.10 USD | 0.00 USD | `+47.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 1,170,000.00 USD | 546.81 USD | 0.00 USD | `+49.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 1,180,000.00 USD | 2,300.00 USD | 0.00 USD | `+51.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 1,190,000.00 USD | 12,070.00 USD | 0.00 USD | `+53.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.05` | 1,210,000.00 USD | 20,230.00 USD | 0.00 USD | `+56.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 1,210,000.00 USD | 1,580.00 USD | 0.00 USD | `+58.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 1,250,000.00 USD | 37,000.00 USD | 0.00 USD | `+58.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 1,250,000.00 USD | 473.21 USD | 0.00 USD | `+60.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 1,250,000.00 USD | 422.99 USD | 0.00 USD | `+60.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 1,250,000.00 USD | 1,630.00 USD | 0.00 USD | `+61.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 1,250,000.00 USD | 4,870.00 USD | 0.00 USD | `+62.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 1,260,000.00 USD | 481.55 USD | 0.00 USD | `+65.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 1,260,000.00 USD | 1,330.00 USD | 0.00 USD | `+65.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 1,260,000.00 USD | 281.21 USD | 0.00 USD | `+69.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,520,000.00 USD | 266,140.00 USD | 0.00 USD | `+71.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,530,000.00 USD | 3,400.00 USD | 0.00 USD | `+71.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,550,000.00 USD | 21,930.00 USD | 0.00 USD | `+73.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,550,000.00 USD | 294.15 USD | 0.00 USD | `+76.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 1,560,000.00 USD | 15,380.00 USD | 0.00 USD | `+78.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,570,000.00 USD | 3,660.00 USD | 0.00 USD | `+80.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,570,000.00 USD | 306.15 USD | 0.00 USD | `+84.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,570,000.00 USD | 936.72 USD | 0.00 USD | `+85.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,570,000.00 USD | 2,920.00 USD | 0.00 USD | `+86.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,570,000.00 USD | 324.15 USD | 0.00 USD | `+94.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 1,570,000.00 USD | 123.23 USD | 0.00 USD | `+96.64%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `47.20` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 9,650.00 USD | 2,470.00 USD | 114.09 USD |
| `7D` | `47.30` | 8,180,000.00 USD | 0.00 USD | 8,180,000.00 USD | 692.33 USD | 4,740.00 USD | 6,740.00 USD |
| `7D` | `47.40` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 0.00 USD | 1,520.00 USD | 28,650.00 USD |
| `7D` | `47.50` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 11,830.00 USD | 0.00 USD | 7,960.00 USD |
| `7D` | `48.10` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD |
| `7D` | `48.20` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD |
| `7D` | `48.40` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 0.00 USD | 6,080.00 USD | 0.00 USD |
| `7D` | `48.60` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `48.80` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 1,780.00 USD | 2,250.00 USD | 0.00 USD |
| `7D` | `48.90` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 0.00 USD | 0.00 USD | 960.40 USD |
| `7D` | `49.30` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 15,190.00 USD | 4,490.00 USD | 14,870.00 USD |
| `7D` | `49.40` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD |
| `7D` | `49.50` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 2,830.00 USD | 7,770.00 USD | 0.00 USD |
| `7D` | `49.60` | 8,040,000.00 USD | 0.00 USD | 8,040,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD |
| `7D` | `49.70` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 12,090.00 USD | 0.00 USD | 5,410.00 USD |
| `7D` | `49.80` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 9,930.00 USD | 8,220.00 USD | 0.00 USD |
| `1D` | `49.90` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 29,140.00 USD | 17,520.00 USD | 47,750.00 USD |
| `7D` | `49.90` | 7,990,000.00 USD | 0.00 USD | 7,990,000.00 USD | 45,030.00 USD | 8,880.00 USD | 4,700.00 USD |
| `1D` | `50.00` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 13,200.00 USD | 16,830.00 USD | 40,730.00 USD |
| `7D` | `50.00` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 22,100.00 USD | 19,810.00 USD | 24,920.00 USD |
| `1D` | `50.10` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 3,780.00 USD | 4,040.00 USD | 7,600.00 USD |
| `7D` | `50.10` | 7,860,000.00 USD | 0.00 USD | 7,860,000.00 USD | 363.50 USD | 682.90 USD | 8,340.00 USD |
| `1D` | `50.20` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 177.10 USD | 709.61 USD | 5,230.00 USD |
| `7D` | `50.20` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 6,960.00 USD | 500.40 USD | 42,940.00 USD |
| `1D` | `50.30` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 171.03 USD | 3,880.00 USD | 2,500.00 USD |
| `7D` | `50.30` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 16,270.00 USD | 10,780.00 USD | 7,240.00 USD |
| `1D` | `50.40` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 8,260.00 USD | 11,890.00 USD | 1,150.00 USD |
| `7D` | `50.40` | 7,770,000.00 USD | 0.00 USD | 7,770,000.00 USD | 28,280.00 USD | 26,580.00 USD | 33,450.00 USD |
| `1D` | `50.50` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 8,910.00 USD | 8,790.00 USD | 10,530.00 USD |
| `7D` | `50.50` | 7,680,000.00 USD | 0.00 USD | 7,680,000.00 USD | 32,490.00 USD | 6,790.00 USD | 44,380.00 USD |
| `1D` | `50.60` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 7,330.00 USD | 3,440.00 USD | 10,850.00 USD |
| `7D` | `50.60` | 7,590,000.00 USD | 0.00 USD | 7,590,000.00 USD | 67,580.00 USD | 21,530.00 USD | 31,730.00 USD |
| `1D` | `50.70` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 8,170.00 USD | 2,300.00 USD | 11,770.00 USD |
| `7D` | `50.70` | 7,470,000.00 USD | 0.00 USD | 7,470,000.00 USD | 65,920.00 USD | 32,820.00 USD | 41,580.00 USD |
| `1D` | `50.80` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 12,550.00 USD | 3,100.00 USD | 8,280.00 USD |
| `7D` | `50.80` | 7,330,000.00 USD | 0.00 USD | 7,330,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD |
| `1D` | `50.90` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 826.24 USD | 260.05 USD | 8,390.00 USD |
| `7D` | `50.90` | 7,240,000.00 USD | 0.00 USD | 7,240,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD |
| `1D` | `51.00` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 5,040.00 USD | 0.00 USD | 430.77 USD |
| `7D` | `51.00` | 6,980,000.00 USD | 0.00 USD | 6,980,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `51.10` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 9,210.00 USD | 6,650.00 USD | 0.00 USD |
| `7D` | `51.10` | 6,860,000.00 USD | 0.00 USD | 6,860,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD |
| `1D` | `51.20` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 1,770.00 USD | 1,130.00 USD | 19,220.00 USD |
| `7D` | `51.20` | 6,770,000.00 USD | 0.00 USD | 6,770,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD |
| `1D` | `51.30` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 8,650.00 USD | 9,710.00 USD | 0.00 USD |
| `7D` | `51.30` | 6,710,000.00 USD | 0.00 USD | 6,710,000.00 USD | 28,400.00 USD | 26,720.00 USD | 47,090.00 USD |
| `1D` | `51.40` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 3,250.00 USD | 5,610.00 USD | 416.23 USD |
| `7D` | `51.40` | 6,610,000.00 USD | 0.00 USD | 6,610,000.00 USD | 73,130.00 USD | 42,820.00 USD | 46,140.00 USD |
| `1D` | `51.50` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 5,650.00 USD | 10,010.00 USD | 41,580.00 USD |
| `7D` | `51.50` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 38,520.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `51.60` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 9,060.00 USD | 18,580.00 USD | 731.68 USD |
| `7D` | `51.60` | 6,350,000.00 USD | 0.00 USD | 6,350,000.00 USD | 37,880.00 USD | 36,790.00 USD | 41,490.00 USD |
| `1D` | `51.70` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 2,510.00 USD | 12,840.00 USD | 44.86 USD |
| `7D` | `51.70` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `51.80` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 13,770.00 USD | 19,520.00 USD | 14,360.00 USD |
| `7D` | `51.80` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD |
| `1D` | `51.90` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 10,140.00 USD | 19,910.00 USD | 23,480.00 USD |
| `7D` | `51.90` | 6,140,000.00 USD | 0.00 USD | 6,140,000.00 USD | 5,870.00 USD | 25,410.00 USD | 28,190.00 USD |
| `1D` | `52.00` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 20,980.00 USD | 25,620.00 USD | 24,820.00 USD |
| `7D` | `52.00` | 6,080,000.00 USD | 0.00 USD | 6,080,000.00 USD | 65,840.00 USD | 26,440.00 USD | 11,880.00 USD |
| `1D` | `52.10` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 34,970.00 USD | 17,300.00 USD | 50,500.00 USD |
| `7D` | `52.10` | 5,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 24,220.00 USD | 28,090.00 USD | 37,880.00 USD |
| `1D` | `52.20` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 15,890.00 USD | 7,630.00 USD | 49,960.00 USD |
| `7D` | `52.20` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 38,380.00 USD | 13,960.00 USD | 25,270.00 USD |
| `1D` | `52.30` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 26,510.00 USD | 22,090.00 USD | 11,210.00 USD |
| `7D` | `52.30` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 26,450.00 USD | 40,700.00 USD | 7,980.00 USD |
| `1D` | `52.40` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 13,070.00 USD | 15,400.00 USD | 7,040.00 USD |
| `7D` | `52.40` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 20,580.00 USD | 38,950.00 USD | 22,030.00 USD |
| `1D` | `52.50` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 53,990.00 USD | 30,000.00 USD | 79,400.00 USD |
| `7D` | `52.50` | 5,650,000.00 USD | 0.00 USD | 5,650,000.00 USD | 40,460.00 USD | 0.00 USD | 11,240.00 USD |
| `1D` | `52.60` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 8,330.00 USD | 43,700.00 USD | 5,450.00 USD |
| `7D` | `52.60` | 5,600,000.00 USD | 0.00 USD | 5,600,000.00 USD | 67,180.00 USD | 32,590.00 USD | 59,410.00 USD |
| `1D` | `52.70` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 18,270.00 USD | 19,780.00 USD | 40,000.00 USD |
| `7D` | `52.70` | 5,440,000.00 USD | 0.00 USD | 5,440,000.00 USD | 19,550.00 USD | 75,910.00 USD | 108,640.00 USD |
| `1D` | `52.80` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 28,000.00 USD | 50,850.00 USD | 72,920.00 USD |
| `7D` | `52.80` | 5,240,000.00 USD | 0.00 USD | 5,240,000.00 USD | 30,590.00 USD | 25,700.00 USD | 0.00 USD |
| `1D` | `52.90` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 43,760.00 USD | 50,880.00 USD | 30,100.00 USD |
| `7D` | `52.90` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 30,900.00 USD | 11,650.00 USD | 34,400.00 USD |
| `1D` | `53.00` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 26,800.00 USD | 30,500.00 USD | 39,600.00 USD |
| `7D` | `53.00` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 39,690.00 USD | 22,700.00 USD | 77,700.00 USD |
| `1D` | `53.10` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 12,590.00 USD | 47,310.00 USD | 85,170.00 USD |
| `7D` | `53.10` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 45,320.00 USD | 17,950.00 USD | 0.00 USD |
| `1D` | `53.20` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 26,460.00 USD | 10,830.00 USD | 42,170.00 USD |
| `7D` | `53.20` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 162,460.00 USD | 32,580.00 USD | 23,350.00 USD |
| `1D` | `53.30` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 8,610.00 USD | 28,530.00 USD | 5,690.00 USD |
| `7D` | `53.30` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 59,390.00 USD | 49,210.00 USD | 35,070.00 USD |
| `1D` | `53.40` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 12,600.00 USD | 10,640.00 USD | 4,540.00 USD |
| `7D` | `53.40` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 44,030.00 USD | 17,420.00 USD | 91,220.00 USD |
| `1D` | `53.50` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 9,410.00 USD | 5,700.00 USD | 22,000.00 USD |
| `7D` | `53.50` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 60,260.00 USD | 3,440.00 USD | 28,500.00 USD |
| `1D` | `53.60` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 75,950.00 USD | 3,830.00 USD | 20,970.00 USD |
| `7D` | `53.60` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 52,800.00 USD | 3,780.00 USD | 20,660.00 USD |
| `1D` | `53.70` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 6,210.00 USD | 11,100.00 USD | 11,960.00 USD |
| `7D` | `53.70` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 131,400.00 USD | 21,330.00 USD | 13,220.00 USD |
| `1D` | `53.80` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 53,640.00 USD | 28,920.00 USD | 4,830.00 USD |
| `7D` | `53.80` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 99,150.00 USD | 43,900.00 USD | 302.55 USD |
| `1D` | `53.90` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 51,060.00 USD | 39,560.00 USD | 27,830.00 USD |
| `7D` | `53.90` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 160,820.00 USD | 22,780.00 USD | 9,680.00 USD |
| `1D` | `54.00` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 76,010.00 USD | 21,440.00 USD | 86,580.00 USD |
| `7D` | `54.00` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 380,340.00 USD | 71,820.00 USD | 304,530.00 USD |
| `1D` | `54.10` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 94,870.00 USD | 19,160.00 USD | 49,170.00 USD |
| `7D` | `54.10` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 302,190.00 USD | 0.00 USD | 2,590.00 USD |
| `1D` | `54.20` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 72,600.00 USD | 24,050.00 USD | 40,120.00 USD |
| `7D` | `54.20` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 205,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `54.30` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 27,200.00 USD | 8,640.00 USD | 5,590.00 USD |
| `7D` | `54.30` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 381,380.00 USD | 8,520.00 USD | 181,420.00 USD |
| `1D` | `54.40` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 62,680.00 USD | 92,560.00 USD | 3,290.00 USD |
| `7D` | `54.40` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 304,270.00 USD | 63,170.00 USD | 92,650.00 USD |
| `1D` | `54.50` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 25,050.00 USD | 64,250.00 USD | 9,090.00 USD |
| `7D` | `54.50` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 159,720.00 USD | 35,580.00 USD | 239,890.00 USD |
| `1D` | `54.60` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 913.17 USD | 25,490.00 USD | 43,580.00 USD |
| `7D` | `54.60` | 978,810.00 USD | 0.00 USD | 978,810.00 USD | 18,530.00 USD | 1,930.00 USD | 131,380.00 USD |
| `1D` | `54.70` | 945,620.00 USD | 0.00 USD | 945,620.00 USD | 6,600.00 USD | 23,060.00 USD | 105,800.00 USD |
| `7D` | `54.70` | 826,970.00 USD | 0.00 USD | 826,970.00 USD | 0.00 USD | 3,600.00 USD | 41,310.00 USD |
| `1D` | `54.80` | 810,160.00 USD | 0.00 USD | 810,160.00 USD | 0.00 USD | 48,420.00 USD | 23,920.00 USD |
| `7D` | `54.80` | 782,060.00 USD | 0.00 USD | 782,060.00 USD | 0.00 USD | 35,700.00 USD | 26,440.00 USD |
| `1D` | `54.90` | 737,820.00 USD | 0.00 USD | 737,820.00 USD | 66,900.00 USD | 65,440.00 USD | 10,850.00 USD |
| `7D` | `54.90` | 719,920.00 USD | 0.00 USD | 719,920.00 USD | 0.00 USD | 112,280.00 USD | 48,290.00 USD |
| `1D` | `55.00` | 594,640.00 USD | 0.00 USD | 594,640.00 USD | 40,710.00 USD | 54,150.00 USD | 55,190.00 USD |
| `7D` | `55.00` | 559,350.00 USD | 0.00 USD | 559,350.00 USD | 97,700.00 USD | 2,830.00 USD | 19,360.00 USD |
| `1D` | `55.10` | 444,580.00 USD | 0.00 USD | 444,580.00 USD | 50,530.00 USD | 62,170.00 USD | 80,200.00 USD |
| `7D` | `55.10` | 439,470.00 USD | 0.00 USD | 439,470.00 USD | 54,590.00 USD | 18,510.00 USD | 64,690.00 USD |
| `1D` | `55.20` | 251,690.00 USD | 0.00 USD | 251,690.00 USD | 39,390.00 USD | 11,830.00 USD | 66,410.00 USD |
| `7D` | `55.20` | 301,680.00 USD | 0.00 USD | 301,680.00 USD | 57,400.00 USD | 59,710.00 USD | 150,160.00 USD |
| `1D` | `55.30` | 134,060.00 USD | 0.00 USD | 134,060.00 USD | 52,860.00 USD | 15,520.00 USD | 59,180.00 USD |
| `7D` | `55.30` | 34,410.00 USD | 0.00 USD | 34,410.00 USD | 23,140.00 USD | 11,270.00 USD | 0.00 USD |
| `1D` | `55.40` | 6,510.00 USD | 0.00 USD | 6,510.00 USD | 0.00 USD | 6,510.00 USD | 0.00 USD |
| `7D` | `55.40` | 23,360.00 USD | 23,360.00 USD | 0.00 USD | 0.00 USD | 18,550.00 USD | 4,800.00 USD |
| `7D` | `55.40` | 46,710.00 USD | 46,710.00 USD | 0.00 USD | 0.00 USD | 18,550.00 USD | 4,800.00 USD |
| `1D` | `55.50` | 5,500.00 USD | 5,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD |
| `1D` | `55.50` | 11,000.00 USD | 11,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD |
| `1D` | `55.70` | 19,310.00 USD | 19,310.00 USD | 0.00 USD | 0.00 USD | 7,700.00 USD | 613.46 USD |
| `7D` | `55.70` | 253,130.00 USD | 253,130.00 USD | 0.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD |
| `1D` | `55.80` | 22,490.00 USD | 22,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,170.00 USD |
| `7D` | `55.80` | 344,100.00 USD | 344,100.00 USD | 0.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD |
| `1D` | `55.90` | 75,550.00 USD | 75,550.00 USD | 0.00 USD | 51,520.00 USD | 0.00 USD | 1,550.00 USD |
| `7D` | `55.90` | 485,430.00 USD | 485,430.00 USD | 0.00 USD | 141,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `56.00` | 79,930.00 USD | 79,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,380.00 USD |
| `7D` | `56.00` | 656,540.00 USD | 656,540.00 USD | 0.00 USD | 2,590.00 USD | 0.00 USD | 168,520.00 USD |
| `7D` | `56.20` | 736,490.00 USD | 736,490.00 USD | 0.00 USD | 0.00 USD | 79,940.00 USD | 0.00 USD |
| `1D` | `56.30` | 83,880.00 USD | 83,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,950.00 USD |
| `7D` | `56.30` | 739,080.00 USD | 739,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,590.00 USD |
| `1D` | `56.40` | 116,760.00 USD | 116,760.00 USD | 0.00 USD | 5,040.00 USD | 25,370.00 USD | 2,470.00 USD |
| `7D` | `56.40` | 752,770.00 USD | 752,770.00 USD | 0.00 USD | 2,650.00 USD | 11,040.00 USD | 0.00 USD |
| `1D` | `56.50` | 522,560.00 USD | 522,560.00 USD | 0.00 USD | 150,140.00 USD | 110,620.00 USD | 145,040.00 USD |
| `7D` | `56.50` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 170,750.00 USD | 151,940.00 USD | 6,150.00 USD |
| `1D` | `56.60` | 826,330.00 USD | 826,330.00 USD | 0.00 USD | 61,400.00 USD | 161,300.00 USD | 81,070.00 USD |
| `7D` | `56.60` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 363,190.00 USD | 185,910.00 USD | 507.54 USD |
| `1D` | `56.70` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 114,230.00 USD | 45,300.00 USD | 315,590.00 USD |
| `7D` | `56.70` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 117,290.00 USD | 141,830.00 USD | 98,950.00 USD |
| `1D` | `56.80` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 117,760.00 USD | 20,790.00 USD | 106,140.00 USD |
| `7D` | `56.80` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 172,110.00 USD | 92,780.00 USD | 318,330.00 USD |
| `1D` | `56.90` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 45,140.00 USD | 17,930.00 USD | 35,720.00 USD |
| `7D` | `56.90` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 113,780.00 USD | 52,200.00 USD | 307,930.00 USD |
| `1D` | `57.00` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 6,480.00 USD | 43,030.00 USD | 29,740.00 USD |
| `7D` | `57.00` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 88,680.00 USD | 56,390.00 USD | 178,370.00 USD |
| `1D` | `57.10` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 77,000.00 USD | 77,400.00 USD | 46,610.00 USD |
| `7D` | `57.10` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 36,580.00 USD | 79,290.00 USD | 21,040.00 USD |
| `1D` | `57.20` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 53,080.00 USD | 78,490.00 USD | 120,900.00 USD |
| `7D` | `57.20` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 118,850.00 USD | 23,920.00 USD | 23,060.00 USD |
| `1D` | `57.30` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 70,930.00 USD | 44,630.00 USD | 87,180.00 USD |
| `7D` | `57.30` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 76,940.00 USD | 28,570.00 USD | 98,930.00 USD |
| `1D` | `57.40` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 84,960.00 USD | 49,470.00 USD | 78,400.00 USD |
| `7D` | `57.40` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 124,180.00 USD | 72,180.00 USD | 257,020.00 USD |
| `1D` | `57.50` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 197,830.00 USD | 52,620.00 USD | 174,740.00 USD |
| `7D` | `57.50` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 99,810.00 USD | 31,830.00 USD | 0.00 USD |
| `1D` | `57.60` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 75,520.00 USD | 28,370.00 USD | 62,630.00 USD |
| `7D` | `57.60` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 149,560.00 USD | 44,690.00 USD | 28,320.00 USD |
| `1D` | `57.70` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 42,540.00 USD | 54,600.00 USD | 96,430.00 USD |
| `7D` | `57.70` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 30,070.00 USD | 57,580.00 USD |
| `1D` | `57.80` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 18,150.00 USD | 22,650.00 USD | 77,220.00 USD |
| `7D` | `57.80` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 9,650.00 USD | 24,520.00 USD | 49,480.00 USD |
| `1D` | `57.90` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 13,000.00 USD | 15,870.00 USD | 28,950.00 USD |
| `7D` | `57.90` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 14,390.00 USD | 963.90 USD | 30,010.00 USD |
| `1D` | `58.00` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 7,880.00 USD | 9,480.00 USD | 15,330.00 USD |
| `7D` | `58.00` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD | 107,350.00 USD |
| `1D` | `58.10` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 31,400.00 USD | 17,830.00 USD | 21,300.00 USD |
| `7D` | `58.10` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 5,470.00 USD | 19,160.00 USD | 14,070.00 USD |
| `1D` | `58.20` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 35,920.00 USD | 34,800.00 USD | 4,940.00 USD |
| `7D` | `58.20` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 31,590.00 USD | 302.55 USD |
| `1D` | `58.30` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 33,360.00 USD | 38,620.00 USD | 64,380.00 USD |
| `7D` | `58.30` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 48,850.00 USD | 11,000.00 USD | 36,500.00 USD |
| `1D` | `58.40` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 26,490.00 USD | 18,940.00 USD | 49,980.00 USD |
| `7D` | `58.40` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 27,290.00 USD | 9,260.00 USD | 86,460.00 USD |
| `1D` | `58.50` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 16,410.00 USD | 1,200.00 USD | 124.02 USD |
| `7D` | `58.50` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 2,060.00 USD | 24,530.00 USD | 0.00 USD |
| `1D` | `58.60` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 21,940.00 USD | 5,920.00 USD | 40,890.00 USD |
| `7D` | `58.60` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 30,680.00 USD | 20,260.00 USD | 51,650.00 USD |
| `1D` | `58.70` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 44,920.00 USD | 10,120.00 USD | 29,940.00 USD |
| `7D` | `58.70` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 15,810.00 USD | 11,600.00 USD | 35,320.00 USD |
| `1D` | `58.80` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 36,630.00 USD | 9,890.00 USD | 23,340.00 USD |
| `7D` | `58.80` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD |
| `1D` | `58.90` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 22,130.00 USD | 60,970.00 USD | 90,490.00 USD |
| `7D` | `58.90` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 2,140.00 USD | 54,240.00 USD | 83,500.00 USD |
| `1D` | `59.00` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 129,990.00 USD | 58,870.00 USD | 129,440.00 USD |
| `7D` | `59.00` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 259,280.00 USD | 65,270.00 USD | 118,570.00 USD |
| `1D` | `59.10` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 92,240.00 USD | 39,740.00 USD | 163,590.00 USD |
| `7D` | `59.10` | 6,390,000.00 USD | 6,390,000.00 USD | 0.00 USD | 93,390.00 USD | 45,400.00 USD | 158,780.00 USD |
| `1D` | `59.20` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 102,940.00 USD | 59,320.00 USD | 49,210.00 USD |
| `7D` | `59.20` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 153,580.00 USD | 18,540.00 USD | 174,600.00 USD |
| `1D` | `59.30` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 146,220.00 USD | 30,070.00 USD | 66,050.00 USD |
| `7D` | `59.30` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 88,710.00 USD | 67,460.00 USD | 114,310.00 USD |
| `1D` | `59.40` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 35,110.00 USD | 30,780.00 USD | 49,030.00 USD |
| `7D` | `59.40` | 7,330,000.00 USD | 7,330,000.00 USD | 0.00 USD | 107,040.00 USD | 73,620.00 USD | 137,500.00 USD |
| `1D` | `59.50` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 81,240.00 USD | 34,430.00 USD | 32,400.00 USD |
| `7D` | `59.50` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 67,060.00 USD | 61,370.00 USD | 21,090.00 USD |
| `1D` | `59.60` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 43,950.00 USD | 51,200.00 USD | 5,210.00 USD |
| `7D` | `59.60` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 236,760.00 USD | 129,330.00 USD | 72,920.00 USD |
| `1D` | `59.70` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 7,970.00 USD | 15,700.00 USD | 62,040.00 USD |
| `7D` | `59.70` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 55,510.00 USD | 99,970.00 USD | 162,850.00 USD |
| `1D` | `59.80` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 32,130.00 USD | 26,470.00 USD | 2,350.00 USD |
| `7D` | `59.80` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 118,240.00 USD | 91,980.00 USD | 154,560.00 USD |
| `1D` | `59.90` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 102,020.00 USD | 17,810.00 USD | 50,060.00 USD |
| `7D` | `59.90` | 8,800,000.00 USD | 8,800,000.00 USD | 0.00 USD | 142,290.00 USD | 34,490.00 USD | 29,380.00 USD |
| `1D` | `60.00` | 6,370,000.00 USD | 6,370,000.00 USD | 0.00 USD | 162,970.00 USD | 29,090.00 USD | 50,570.00 USD |
| `7D` | `60.00` | 9,060,000.00 USD | 9,060,000.00 USD | 0.00 USD | 100,570.00 USD | 67,520.00 USD | 83,920.00 USD |
| `1D` | `60.10` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 64,550.00 USD | 28,140.00 USD | 57,080.00 USD |
| `7D` | `60.10` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 200,540.00 USD | 84,980.00 USD | 95,670.00 USD |
| `1D` | `60.20` | 6,680,000.00 USD | 6,680,000.00 USD | 0.00 USD | 58,830.00 USD | 19,740.00 USD | 82,270.00 USD |
| `7D` | `60.20` | 9,810,000.00 USD | 9,810,000.00 USD | 0.00 USD | 162,230.00 USD | 99,360.00 USD | 108,990.00 USD |
| `1D` | `60.30` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 52,350.00 USD | 31,630.00 USD | 26,470.00 USD |
| `7D` | `60.30` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 133,350.00 USD | 100,380.00 USD | 170,480.00 USD |
| `1D` | `60.40` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 66,740.00 USD | 13,730.00 USD | 42,520.00 USD |
| `7D` | `60.40` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 64,850.00 USD | 100,560.00 USD | 202,370.00 USD |
| `1D` | `60.50` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 22,700.00 USD | 19,320.00 USD | 36,200.00 USD |
| `7D` | `60.50` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 115,390.00 USD | 80,510.00 USD | 175,550.00 USD |
| `1D` | `60.60` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 40,710.00 USD | 19,140.00 USD | 3,930.00 USD |
| `7D` | `60.60` | 11,340,000.00 USD | 11,340,000.00 USD | 0.00 USD | 251,100.00 USD | 16,970.00 USD | 118,680.00 USD |
| `1D` | `60.70` | 7,110,000.00 USD | 7,110,000.00 USD | 0.00 USD | 31,880.00 USD | 22,330.00 USD | 3,120.00 USD |
| `7D` | `60.70` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 102,230.00 USD | 48,240.00 USD | 15,880.00 USD |
| `1D` | `60.80` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 11,060.00 USD | 12,980.00 USD | 47,810.00 USD |
| `7D` | `60.80` | 11,660,000.00 USD | 11,660,000.00 USD | 0.00 USD | 46,960.00 USD | 28,960.00 USD | 76,200.00 USD |
| `1D` | `60.90` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 36,520.00 USD | 23,250.00 USD | 22,900.00 USD |
| `7D` | `60.90` | 11,860,000.00 USD | 11,860,000.00 USD | 0.00 USD | 105,970.00 USD | 33,290.00 USD | 64,920.00 USD |
| `1D` | `61.00` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 43,930.00 USD | 6,430.00 USD | 18,420.00 USD |
| `7D` | `61.00` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 43,120.00 USD | 11,530.00 USD | 0.00 USD |
| `1D` | `61.10` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 13,270.00 USD | 14,950.00 USD | 11,520.00 USD |
| `7D` | `61.10` | 11,960,000.00 USD | 11,960,000.00 USD | 0.00 USD | 31,540.00 USD | 10,430.00 USD | 0.00 USD |
| `1D` | `61.20` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 75,070.00 USD | 1,880.00 USD | 39,080.00 USD |
| `7D` | `61.20` | 12,080,000.00 USD | 12,080,000.00 USD | 0.00 USD | 51,210.00 USD | 20,920.00 USD | 47,810.00 USD |
| `1D` | `61.30` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 4,040.00 USD | 7,600.00 USD |
| `7D` | `61.30` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 16,510.00 USD | 13,210.00 USD | 24,230.00 USD |
| `1D` | `61.40` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 1,190.00 USD | 709.61 USD | 5,230.00 USD |
| `7D` | `61.40` | 12,260,000.00 USD | 12,260,000.00 USD | 0.00 USD | 62,340.00 USD | 25,720.00 USD | 43,510.00 USD |
| `1D` | `61.50` | 7,520,000.00 USD | 7,520,000.00 USD | 0.00 USD | 1,060.00 USD | 3,880.00 USD | 2,500.00 USD |
| `7D` | `61.50` | 12,360,000.00 USD | 12,360,000.00 USD | 0.00 USD | 17,710.00 USD | 42,440.00 USD | 41,390.00 USD |
| `1D` | `61.60` | 7,540,000.00 USD | 7,540,000.00 USD | 0.00 USD | 9,250.00 USD | 11,890.00 USD | 1,150.00 USD |
| `7D` | `61.60` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 32,920.00 USD | 58,350.00 USD | 121,470.00 USD |
| `1D` | `61.70` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 13,890.00 USD | 8,790.00 USD | 10,530.00 USD |
| `7D` | `61.70` | 12,770,000.00 USD | 12,770,000.00 USD | 0.00 USD | 82,860.00 USD | 10,880.00 USD | 99,740.00 USD |
| `1D` | `61.80` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 9,150.00 USD | 3,440.00 USD | 10,850.00 USD |
| `7D` | `61.80` | 13,040,000.00 USD | 13,040,000.00 USD | 0.00 USD | 169,680.00 USD | 25,670.00 USD | 71,530.00 USD |
| `1D` | `61.90` | 7,620,000.00 USD | 7,620,000.00 USD | 0.00 USD | 5,210.00 USD | 1,580.00 USD | 11,700.00 USD |
| `7D` | `61.90` | 13,180,000.00 USD | 13,180,000.00 USD | 0.00 USD | 73,690.00 USD | 32,820.00 USD | 41,580.00 USD |
| `1D` | `62.00` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 12,550.00 USD | 3,100.00 USD | 8,280.00 USD |
| `7D` | `62.00` | 13,280,000.00 USD | 13,280,000.00 USD | 0.00 USD | 50,080.00 USD | 8,550.00 USD | 40,590.00 USD |
| `7D` | `62.10` | 13,290,000.00 USD | 13,290,000.00 USD | 0.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.20` | 13,410,000.00 USD | 13,410,000.00 USD | 0.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD |
| `7D` | `62.30` | 13,560,000.00 USD | 13,560,000.00 USD | 0.00 USD | 27,500.00 USD | 23,450.00 USD | 97,450.00 USD |
| `7D` | `62.40` | 13,680,000.00 USD | 13,680,000.00 USD | 0.00 USD | 74,860.00 USD | 27,560.00 USD | 25,440.00 USD |
| `7D` | `62.50` | 13,760,000.00 USD | 13,760,000.00 USD | 0.00 USD | 36,690.00 USD | 12,720.00 USD | 25,700.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `408.64M` | Total OI Tokens: `7,376,665.6 LTC`
  * 1h OI Change: `-0.61%` | 4h OI Change: `-2.50%` | 24h OI Change: `-9.36%`
  * Exchange Breakdown: Binance=`72.50M` | Bybit=`66.38M` | OKX=`34.20M` | Hyperliquid=`22.14M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `11.45K` | Last 24h: `29.34K` | Last 3d: `56.60K` | Last 7d: `113.64K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0010%` |
| **USDT Bybit** | `0.0075%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0023%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `43.78%` | `56.22%` | `0.78` | 2,310,000.00 USD |
| `15M` | `Binance` | `46.66%` | `53.34%` | `0.87` | 492,530.00 USD |
| `15M` | `OKX` | `35.26%` | `64.74%` | `0.54` | 127,540.00 USD |
| `15M` | `Bybit` | `49.47%` | `50.53%` | `0.98` | 66,550.00 USD |
| `15M` | `KuCoin` | `56.2%` | `43.8%` | `1.28` | 119,730.00 USD |
| `15M` | `Gate` | `47.98%` | `52.02%` | `0.92` | 33,040.00 USD |
| `15M` | `Bitget` | `34.93%` | `65.07%` | `0.54` | 90,590.00 USD |
| `15M` | `BingX` | `30.37%` | `69.63%` | `0.44` | 109,140.00 USD |
| `15M` | `MEXC` | `10.05%` | `89.95%` | `0.11` | 73,700.00 USD |
| `15M` | `Bitunix` | `20.39%` | `79.61%` | `0.26` | 41,370.00 USD |
| `15M` | `Hyperliquid` | `57.2%` | `42.8%` | `1.34` | 7,500.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.27%` | `48.73%` | `1.05` | 939,370.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `97.43%` | `2.57%` | `37.91` | 193,670.00 USD |
| `15M` | `HTX` | `67.71%` | `32.29%` | `2.10` | 865.44 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `46.12%` | `53.88%` | `0.86` | 13,480.00 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 5.51 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `58.35%` | `41.65%` | `1.40` | 306.39 USD |
| `15M` | `Whale Positions` | `46.66%` | `53.34%` | `0.87` | 492,530.00 USD |
| `15M` | `Global Accounts` | `43.78%` | `56.22%` | `0.78` | 2,310,000.00 USD |
| `1H` | `LTC` | `52.65%` | `47.35%` | `1.11` | 10,920,000.00 USD |
| `1H` | `Binance` | `55.43%` | `44.57%` | `1.24` | 2,960,000.00 USD |
| `1H` | `OKX` | `34.77%` | `65.23%` | `0.53` | 1,270,000.00 USD |
| `1H` | `Bybit` | `55.79%` | `44.21%` | `1.26` | 780,370.00 USD |
| `1H` | `KuCoin` | `47.04%` | `52.96%` | `0.89` | 41,990.00 USD |
| `1H` | `Gate` | `50.55%` | `49.45%` | `1.02` | 953,690.00 USD |
| `1H` | `Bitget` | `28.49%` | `71.51%` | `0.40` | 280,130.00 USD |
| `1H` | `BingX` | `37.75%` | `62.25%` | `0.61` | 2,240,000.00 USD |
| `1H` | `MEXC` | `27.61%` | `72.39%` | `0.38` | 283,730.00 USD |
| `1H` | `Bitunix` | `55.23%` | `44.77%` | `1.23` | 202,810.00 USD |
| `1H` | `Hyperliquid` | `54.72%` | `45.28%` | `1.21` | 49,890.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.09%` | `47.91%` | `1.09` | 270,470.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `92.12%` | `7.88%` | `11.69` | 1,550,000.00 USD |
| `1H` | `HTX` | `57.35%` | `42.65%` | `1.34` | 14,910.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `43.88%` | `56.12%` | `0.78` | 13,630.00 USD |
| `1H` | `Aster` | `60.9%` | `39.1%` | `1.56` | 7,500.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `8.14%` | `91.86%` | `0.09` | 4,140.00 USD |
| `1H` | `Whale Positions` | `55.43%` | `44.57%` | `1.24` | 2,960,000.00 USD |
| `1H` | `Global Accounts` | `52.65%` | `47.35%` | `1.11` | 10,920,000.00 USD |
| `4H` | `LTC` | `49.01%` | `50.99%` | `0.96` | 42,360,000.00 USD |
| `4H` | `Binance` | `50.24%` | `49.76%` | `1.01` | 12,420,000.00 USD |
| `4H` | `OKX` | `39.01%` | `60.99%` | `0.64` | 4,930,000.00 USD |
| `4H` | `Bybit` | `54.49%` | `45.51%` | `1.20` | 3,820,000.00 USD |
| `4H` | `KuCoin` | `49.82%` | `50.18%` | `0.99` | 333,750.00 USD |
| `4H` | `Gate` | `49%` | `51%` | `0.96` | 4,280,000.00 USD |
| `4H` | `Bitget` | `48.62%` | `51.38%` | `0.95` | 1,410,000.00 USD |
| `4H` | `BingX` | `39.62%` | `60.38%` | `0.66` | 8,960,000.00 USD |
| `4H` | `MEXC` | `46.68%` | `53.32%` | `0.88` | 1,090,000.00 USD |
| `4H` | `Bitunix` | `39.83%` | `60.17%` | `0.66` | 969,120.00 USD |
| `4H` | `Hyperliquid` | `51.72%` | `48.28%` | `1.07` | 364,700.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.85%` | `50.15%` | `0.99` | 1,140,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `91.07%` | `8.93%` | `10.20` | 2,550,000.00 USD |
| `4H` | `HTX` | `48.65%` | `51.35%` | `0.95` | 50,990.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `41.57%` | `58.43%` | `0.71` | 19,440.00 USD |
| `4H` | `Aster` | `42.83%` | `57.17%` | `0.75` | 18,770.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.62%` | `48.38%` | `1.07` | 14,210.00 USD |
| `4H` | `Whale Positions` | `50.24%` | `49.76%` | `1.01` | 12,420,000.00 USD |
| `4H` | `Global Accounts` | `49.01%` | `50.99%` | `0.96` | 42,360,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `56.22` | `56.21` | `56.22` | `56.34` | `56.09` | 877,726.36 USD | 435,989.57 USD | 441,736.79 USD | -5,747.23 USD | `-0.65%` | `1B / 1S` |
| `5:00 UTC` | `56.12` | `56.15` | `56.12` | `56.22` | `56.09` | 467,194.95 USD | 242,503.27 USD | 224,691.68 USD | 17,811.60 USD | `+3.81%` | `1B / 1S` |
| `0:00 UTC` | `56.00` | `56.00` | `56.00` | `56.27` | `55.72` | 908,665.96 USD | 294,841.59 USD | 613,824.36 USD | -318,982.77 USD | `-35.10%` | `2B / 17S` |
| `5:00 UTC` | `55.91` | `55.98` | `55.91` | `56.12` | `55.78` | 818,601.42 USD | 432,159.31 USD | 386,442.11 USD | 45,717.20 USD | `+5.58%` | `3B / 5S` |
| `0:00 UTC` | `55.77` | `55.81` | `55.77` | `56.00` | `55.66` | 705,526.23 USD | 343,392.26 USD | 362,133.97 USD | -18,741.70 USD | `-2.66%` | `2B / 3S` |
| `5:00 UTC` | `55.64` | `55.76` | `55.64` | `55.98` | `55.62` | 705,697.21 USD | 170,266.34 USD | 535,430.87 USD | -365,164.53 USD | `-51.75%` | `2B / 13S` |
| `0:00 UTC` | `55.70` | `55.69` | `55.70` | `55.78` | `55.55` | 839,476.56 USD | 572,886.16 USD | 266,590.39 USD | 306,295.77 USD | `+36.49%` | `1B / 5S` |
| `5:00 UTC` | `55.59` | `55.60` | `55.59` | `55.70` | `55.52` | 436,166.22 USD | 242,135.61 USD | 194,030.61 USD | 48,104.99 USD | `+11.03%` | `3B / 4S` |
| `0:00 UTC` | `55.50` | `55.53` | `55.50` | `55.70` | `55.44` | 464,437.63 USD | 192,555.45 USD | 271,882.18 USD | -79,326.74 USD | `-17.08%` | `3B / 5S` |
| `5:00 UTC` | `55.42` | `55.46` | `55.42` | `55.59` | `55.39` | 357,748.74 USD | 176,874.34 USD | 180,874.40 USD | -4,000.06 USD | `-1.12%` | `2B / 5S` |

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
| `5m` | 6,010.00 USD | -121,930.00 USD | **`DISTRIBUTION`** |
| `15m` | -20,110.00 USD | -148,660.00 USD | **`DISTRIBUTION`** |
| `30m` | -81,620.00 USD | -94,300.00 USD | **`DISTRIBUTION`** |
| `1h` | -187,000.00 USD | -56,480.00 USD | **`DISTRIBUTION`** |
| `2h` | -82,270.00 USD | -886,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 216,490.00 USD | -712,750.00 USD | **`DISTRIBUTION`** |
| `6h` | 411,680.00 USD | -1,560,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 530,890.00 USD | -4,010,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 634,380.00 USD | -4,260,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 815,400.00 USD | -5,280,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 4,340,000.00 USD | -24,570,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -24,390,000.00 USD | -197,600,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+6.01K` | 15m=`-20.11K` | 1h=`-187.00K` | 24h=`+815.40K`
* Futures Capital Netflows: 5m=`-121.93K` | 15m=`-148.66K` | 1h=`-56.48K` | 24h=`-5.28M`
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
  * `2026-10-30 14:41:20 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:20 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:20 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:20 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 14:09:20 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:56:20 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:56:20 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:56:20 IST`: [destatis.de] - (Sentiment: `Neutral`)


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
  * Execution Entry: `54.61` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `53.77` (Risk Distance: `0.8455` pts)
  * +2.5R Take Profit: `56.73`
  * Mathematical Lot Sizing: **`11.82 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `56.16` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `57.01` (Risk Distance: `0.8455` pts)
  * +2.5R Take Profit: `54.05`
  * Mathematical Lot Sizing: **`11.82 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`55.87`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
