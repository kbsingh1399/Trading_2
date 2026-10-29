# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 02:36:43 IST` (`2026-10-29 21:06:43 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `54.63` | **Live Ask Quote**: `54.93` | **Mid Price**: `54.78`
- **Spread Points**: `300.00` | **Spread BPS**: `54.76 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `57.55` | VWAP Z-Score: `-3.29` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.5328` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `18.00` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `60.37` | Lower -3.00σ Band: `54.73`
  * Upper +2.51σ Band: `59.91` | Lower -2.51σ Band: `55.19`
  * Upper +2.01σ Band: `59.44` | Lower -2.01σ Band: `55.66`
  * Upper +2.00σ Band: `59.43` | Lower -2.00σ Band: `55.67`
  * Upper +1.28σ Band: `58.75` | Lower -1.28σ Band: `56.35`
  * Upper +1.00σ Band: `58.49` | Lower -1.00σ Band: `56.61`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`56.51` | EMA-20=`57.13` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`57.50` (Slope: `+0.0000`) | EMA-100=`57.62`
  * Institutional Anchors: EMA-144=`57.57` | EMA-200=`57.40` (Slope: `-0.0831`) | EMA-233=`57.26`
- **Range Boundaries**: 24H High=`59.52` | 24H Low=`54.18` | Weekly High=`59.62` | Weekly Low=`54.18`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `54.78` (Distance: `+0.40%`)
  * Point of Control (POC) = `54.62` (Distance: `+0.71%`)
  * Value Area Low (VAL) = `54.62` (Distance: `+0.71%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.40` | POC=`57.72` | VAL=`56.83`
  * Prior Day Extremes: PDH=`59.52` | PDL=`54.18` | PDC=`54.46`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`57.79` | Weekly POC=`56.45` | Weekly VAL=`56.01`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`54.85` | Low=`54.62`
  * London Session (08:00-16:00 UTC): High=`55.00` | Low=`54.56`
  * New York Session (13:00-21:00 UTC): High=`55.11` | Low=`54.45`
  * Initial Balance (First Hour): IB High=`54.94` | IB Low=`54.62`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `54.56` - `55.00`
  * Optimal Trade Entry (OTE 0.705): `54.89`
  * Structural Invalidation Anchor (0.786): `55.22`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `55.18` | `55.27` | `54.58` | `54.65` | `28,009` | 1,538,737.92 USD | -164,851.33 USD | `-10.71%` | -4,263,045.60 USD | `+0.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `54.64` | `55.19` | `54.52` | `54.89` | `34,549` | 1,896,627.95 USD | 396,115.49 USD | `+20.89%` | -3,866,930.11 USD | `+1.04` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `54.89` | `54.94` | `54.78` | `54.94` | `5,052` | 277,069.46 USD | 223,186.51 USD | `+80.55%` | -3,643,743.60 USD | `+0.69` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `57.16` | `57.31` | `55.29` | `55.41` | `127,847` | 7,177,688.25 USD | -1,165,151.48 USD | `-16.23%` | -2,521,986.16 USD | `-3.22` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `55.42` | `55.58` | `54.17` | `54.65` | `202,189` | 11,110,862.71 USD | -1,793,452.21 USD | `-16.14%` | -4,315,438.37 USD | `-3.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `54.64` | `55.19` | `54.52` | `54.94` | `39,601` | 2,173,697.41 USD | 619,302.00 USD | `+28.49%` | -3,696,136.37 USD | `+1.56` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `57.74` | `58.16` | `57.54` | `57.98` | `28,429` | 1,644,456.85 USD | 223,797.34 USD | `+13.61%` | -941,351.78 USD | `+0.74` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `57.98` | `58.01` | `54.17` | `54.65` | `399,021` | 22,240,643.23 USD | -3,425,260.07 USD | `-15.40%` | -4,366,611.84 USD | `-3.93` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `54.64` | `55.19` | `54.52` | `54.96` | `40,332` | 2,213,916.56 USD | 639,893.56 USD | `+28.90%` | -3,726,718.29 USD | `+0.94` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | -1,031,107.81 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | -891,821.26 USD | `+0.52` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.96` | `439,354` | 24,454,559.79 USD | -2,785,366.51 USD | `-11.39%` | -3,677,187.77 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `57.20` | `58.23` | `56.92` | `57.04` | `229,127` | 13,178,164.26 USD | -500,207.83 USD | `-3.80%` | -1,732,502.54 USD | `+1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `57.04` | `58.16` | `56.85` | `58.00` | `178,996` | 10,300,529.12 USD | 452,809.17 USD | `+4.40%` | -1,279,693.37 USD | `+1.27` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | -1,031,107.81 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | -891,821.26 USD | `+0.52` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.96` | `439,354` | 24,454,559.79 USD | -2,785,366.51 USD | `-11.39%` | -3,677,187.77 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`54.78`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

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
| `1065` | `0xeadc...9d55` | `LONG` | 2,080,659.18 USD | `36,463.77` | `52.78` | `54.87` | `0.000000` | 155,983.23 USD | `+7.50%` | `10X Cross` |
| `1069` | `0x9aa5...58af` | `SHORT` | 2,069,361.58 USD | `36,177.65` | `71.22` | `54.87` | `272.55` | 507,125.09 USD | `+24.51%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `57.71` | 6,835.28 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 6.84K USD at 57.7060 USD [API] | `2026-10-28 03:32:40` |
| `ANNOUNCEMENT` | `INFO` | `57.68` | 6,981.37 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 6.98K USD at 57.6830 USD [API] | `2026-10-28 03:40:52` |
| `ANNOUNCEMENT` | `INFO` | `57.62` | 5,689.97 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.69K USD at 57.6200 USD [API] | `2026-10-28 08:22:51` |
| `ANNOUNCEMENT` | `INFO` | `57.66` | 6,834.46 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 6.83K USD at 57.6650 USD [API] | `2026-10-28 09:03:25` |
| `ANNOUNCEMENT` | `INFO` | `57.79` | 5,189.94 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.19K USD at 57.7880 USD [API] | `2026-10-28 10:16:37` |
| `ANNOUNCEMENT` | `INFO` | `57.79` | 5,114.41 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.11K USD at 57.7900 USD [API] | `2026-10-28 10:16:37` |
| `ANNOUNCEMENT` | `INFO` | `57.85` | 7,509.64 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 57.8510 USD [API] | `2026-10-28 10:22:44` |
| `ANNOUNCEMENT` | `INFO` | `57.85` | 5,530.08 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 5.53K USD at 57.8460 USD [API] | `2026-10-28 10:22:44` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`59.03` (Vol: 256,600.00 USD, Dist: `+3.00%`) | Long MP=`56.68` (Vol: 327,300.00 USD, Dist: `--1.09%`)
  * 48H Horizon: Short MP=`59.00` (Vol: 285,100.00 USD, Dist: `+2.96%`) | Long MP=`56.72` (Vol: 274,000.00 USD, Dist: `--1.04%`)
  * 3D Horizon: Short MP=`59.01` (Vol: 285,100.00 USD, Dist: `+2.96%`) | Long MP=`56.70` (Vol: 302,600.00 USD, Dist: `--1.07%`)
  * 7D Horizon: Short MP=`59.04` (Vol: 256,600.00 USD, Dist: `+3.01%`) | Long MP=`55.27` (Vol: 344,500.00 USD, Dist: `--3.57%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `11.35` | 136.20 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `11.55` | 231.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.25` | 514.50 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.35` | 236.13 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.75` | 2,560.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.05` | 2,200.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.65` | 150.15 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `15.25` | 4,490.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `15.95` | 1,910.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `16.75` | 473.52 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `17.05` | 3,330.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `17.75` | 690.83 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.05` | 3,470.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.45` | 3,180.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.95` | 406.64 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.45` | 19,950.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.55` | 347.60 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.45` | 132.68 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.65` | 5,100.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.75` | 237.50 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.85` | 195.57 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.05` | 421.36 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 277,980.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 173.39 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 50,740.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 374.20 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.45` | 732.93 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.95` | 5,490.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.45` | 546.53 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 272.75 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 173.85 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.15` | 8,890.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.45` | 4,100.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.55` | 223.55 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.85` | 3,580.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 583.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.35` | 996.14 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.55` | 108.74 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 297,600.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 910.82 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 538.53 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 31,690.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 5,680.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 2,870.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 125.24 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.05` | 2,550.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 1,450.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.45` | 166.47 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.55` | 811.47 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 653.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 953.68 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 32,850.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.15` | 395.15 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.55` | 4,430.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 257.76 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 182.85 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 126.70 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 3,240.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 17,580.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 166.49 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.45` | 6,180.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.65` | 926.90 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 3,020.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 423.18 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 101.80 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 1,050.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 438.74 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.25` | 8,510.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 9,260.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 3,530.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 4,860.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 6,210.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 446.67 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.05` | 7,570.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 341.70 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 575.98 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 4,880.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 384.57 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 4,840.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 664,760.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 570.02 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 1,150.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 162.95 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 5,900.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 1,550.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 133.10 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 2,160.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.25` | 1,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 1,160.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 133.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 274.39 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 6,340.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 509.01 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 396.54 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.15` | 213.16 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 15,170.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 644.96 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.55` | 41,550.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.85` | 3,580.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 3,090.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 64,190.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 35,410.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 1,570.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 5,800.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 2,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 8,950.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 120,820.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 1,860.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 5,390.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 2,230.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 426.02 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 21,880.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 801.14 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 1,580.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 2,380.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 17,550.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 84,440.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 38,220.00 USD | 929,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.65` | 277.28 USD | 891,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 4,230.00 USD | 891,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 134.55 USD | 887,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 2,620.00 USD | 886,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 329.32 USD | 884,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 135.00 USD | 884,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 10,630.00 USD | 883,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 2,180.00 USD | 873,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 23,940.00 USD | 871,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 318.39 USD | 847,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 704.87 USD | 846,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 10,640.00 USD | 846,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.25` | 39,320.00 USD | 835,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.35` | 383.78 USD | 796,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.45` | 11,580.00 USD | 795,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 465.50 USD | 784,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 936.73 USD | 783,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 358.40 USD | 782,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 158.22 USD | 782,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 1,980.00 USD | 782,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 574.09 USD | 780,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.35` | 2,600.00 USD | 779,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.45` | 2,180.00 USD | 777,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 1,770.00 USD | 774,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 5,030.00 USD | 773,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.95` | 2,420.00 USD | 768,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 1,860.00 USD | 765,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 2,680.00 USD | 763,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 4,390.00 USD | 761,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 2,030.00 USD | 756,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 273.90 USD | 754,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 231.56 USD | 754,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 1,910.00 USD | 754,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 8,640.00 USD | 752,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.10` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 242.30 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,740.00 USD | 743,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.20` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 3,260.00 USD | 367.32 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.35` | 5,230.00 USD | 737,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.40` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 626.48 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.40` | 6,670,000.00 USD | 6,670,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.45` | 1,960.00 USD | 732,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.50` | 1,240,000.00 USD | 1,240,000.00 USD | 1,180.00 USD | 4,790.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.50` | 6,660,000.00 USD | 6,660,000.00 USD | 1,130.00 USD | 5,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.55` | 18,010.00 USD | 730,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.60` | 1,220,000.00 USD | 1,220,000.00 USD | 785.85 USD | 2,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.60` | 6,650,000.00 USD | 6,650,000.00 USD | 1,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.65` | 4,890.00 USD | 712,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.70` | 1,210,000.00 USD | 1,210,000.00 USD | 1,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.70` | 6,650,000.00 USD | 6,650,000.00 USD | 788.92 USD | 0.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.75` | 1,250.00 USD | 707,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.80` | 1,210,000.00 USD | 1,210,000.00 USD | 667.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.80` | 6,650,000.00 USD | 6,650,000.00 USD | 7,660.00 USD | 8,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `49.90` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 2,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.90` | 6,630,000.00 USD | 6,630,000.00 USD | 24,600.00 USD | 0.00 USD | 3,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.95` | 28,540.00 USD | 706,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.00` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.00` | 6,600,000.00 USD | 6,600,000.00 USD | 22,100.00 USD | 838.65 USD | 5,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.05` | 1,820.00 USD | 678,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.10` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 315.50 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.10` | 6,570,000.00 USD | 6,570,000.00 USD | 363.50 USD | 682.90 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.15` | 172.01 USD | 676,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.20` | 6,570,000.00 USD | 6,570,000.00 USD | 6,960.00 USD | 500.40 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.25` | 102.51 USD | 676,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.30` | 6,570,000.00 USD | 6,570,000.00 USD | 16,270.00 USD | 3,640.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.35` | 36,230.00 USD | 675,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.40` | 1,200,000.00 USD | 1,200,000.00 USD | 349.63 USD | 2,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.40` | 6,540,000.00 USD | 6,540,000.00 USD | 23,520.00 USD | 19,110.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,720.00 USD | 639,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.50` | 6,470,000.00 USD | 6,470,000.00 USD | 24,840.00 USD | 6,790.00 USD | 43,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.55` | 84,100.00 USD | 635,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.60` | 6,390,000.00 USD | 6,390,000.00 USD | 52,670.00 USD | 17,830.00 USD | 22,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.70` | 6,300,000.00 USD | 6,300,000.00 USD | 53,670.00 USD | 24,710.00 USD | 32,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.75` | 9,050.00 USD | 550,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.80` | 1,190,000.00 USD | 1,190,000.00 USD | 5,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.80` | 6,190,000.00 USD | 6,190,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.90` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 260.05 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.90` | 6,090,000.00 USD | 6,090,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.95` | 245.07 USD | 541,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.00` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 129.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.00` | 5,840,000.00 USD | 5,840,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.05` | 3,320.00 USD | 541,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.10` | 1,180,000.00 USD | 1,180,000.00 USD | 263.90 USD | 1,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.10` | 5,710,000.00 USD | 5,710,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.15` | 219,370.00 USD | 538,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.20` | 1,180,000.00 USD | 1,180,000.00 USD | 1,100.00 USD | 1,130.00 USD | 327.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.20` | 5,630,000.00 USD | 5,630,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.30` | 1,180,000.00 USD | 1,180,000.00 USD | 20,430.00 USD | 5,150.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.30` | 5,570,000.00 USD | 5,570,000.00 USD | 19,510.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.40` | 1,130,000.00 USD | 1,130,000.00 USD | 17,510.00 USD | 7,090.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.40` | 5,490,000.00 USD | 5,490,000.00 USD | 71,090.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.45` | 22,270.00 USD | 318,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.50` | 1,100,000.00 USD | 1,100,000.00 USD | 10,410.00 USD | 8,980.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.50` | 5,340,000.00 USD | 5,340,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.55` | 551.07 USD | 296,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.60` | 1,070,000.00 USD | 1,070,000.00 USD | 8,800.00 USD | 7,990.00 USD | 4,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.60` | 5,250,000.00 USD | 5,250,000.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.65` | 155.47 USD | 296,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.70` | 1,050,000.00 USD | 1,050,000.00 USD | 3,490.00 USD | 4,150.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.70` | 5,190,000.00 USD | 5,190,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.75` | 6,450.00 USD | 295,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.80` | 1,040,000.00 USD | 1,040,000.00 USD | 12,210.00 USD | 2,080.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.80` | 5,150,000.00 USD | 5,150,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.85` | 29,510.00 USD | 289,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.90` | 1,010,000.00 USD | 1,010,000.00 USD | 12,520.00 USD | 21,470.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.90` | 5,090,000.00 USD | 5,090,000.00 USD | 5,870.00 USD | 15,810.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.95` | 12,070.00 USD | 260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.00` | 968,990.00 USD | 968,990.00 USD | 25,150.00 USD | 8,230.00 USD | 23,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.00` | 5,070,000.00 USD | 5,070,000.00 USD | 64,300.00 USD | 20,800.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.05` | 179.57 USD | 247,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.10` | 912,270.00 USD | 912,270.00 USD | 27,630.00 USD | 5,780.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 4,970,000.00 USD | 4,970,000.00 USD | 24,220.00 USD | 18,810.00 USD | 35,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.20` | 843,640.00 USD | 843,640.00 USD | 20,520.00 USD | 10,450.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 4,890,000.00 USD | 4,890,000.00 USD | 38,380.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.25` | 358.96 USD | 247,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.30` | 798,280.00 USD | 798,280.00 USD | 38,870.00 USD | 8,170.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 4,820,000.00 USD | 4,820,000.00 USD | 18,740.00 USD | 12,840.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.35` | 1,470.00 USD | 247,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.40` | 735,130.00 USD | 735,130.00 USD | 10,040.00 USD | 7,510.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 4,780,000.00 USD | 4,780,000.00 USD | 20,580.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.45` | 3,830.00 USD | 245,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.50` | 711,290.00 USD | 711,290.00 USD | 15,070.00 USD | 13,510.00 USD | 998.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.50` | 4,730,000.00 USD | 4,730,000.00 USD | 33,240.00 USD | 667.05 USD | 10,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.55` | 8,700.00 USD | 242,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.60` | 681,710.00 USD | 681,710.00 USD | 2,760.00 USD | 8,750.00 USD | 273.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.60` | 4,680,000.00 USD | 4,680,000.00 USD | 36,640.00 USD | 14,530.00 USD | 584.77 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.70` | 669,920.00 USD | 669,920.00 USD | 4,930.00 USD | 7,610.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.70` | 4,630,000.00 USD | 4,630,000.00 USD | 20,250.00 USD | 43,820.00 USD | 62,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.75` | 7,450.00 USD | 233,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.80` | 642,300.00 USD | 642,300.00 USD | 14,400.00 USD | 14,660.00 USD | 60,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.80` | 4,510,000.00 USD | 4,510,000.00 USD | 46,600.00 USD | 27,850.00 USD | 108.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.85` | 5,950.00 USD | 225,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.90` | 552,910.00 USD | 552,910.00 USD | 28,000.00 USD | 7,150.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.90` | 4,430,000.00 USD | 4,430,000.00 USD | 51,920.00 USD | 23,030.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.95` | 4,320.00 USD | 220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.00` | 511,640.00 USD | 511,640.00 USD | 4,280.00 USD | 1,860.00 USD | 936.80 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.00` | 4,350,000.00 USD | 4,350,000.00 USD | 18,990.00 USD | 8,880.00 USD | 32,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.05` | 900.26 USD | 215,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.10` | 504,580.00 USD | 504,580.00 USD | 3,280.00 USD | 2,540.00 USD | 669.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.10` | 4,290,000.00 USD | 4,290,000.00 USD | 52,760.00 USD | 29,200.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.15` | 22,150.00 USD | 214,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.20` | 498,090.00 USD | 498,090.00 USD | 9,780.00 USD | 13,340.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.20` | 4,200,000.00 USD | 4,200,000.00 USD | 90,340.00 USD | 17,580.00 USD | 25,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.25` | 1,030.00 USD | 192,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.30` | 468,610.00 USD | 468,610.00 USD | 17,240.00 USD | 4,110.00 USD | 36,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.30` | 4,070,000.00 USD | 4,070,000.00 USD | 63,050.00 USD | 14,250.00 USD | 37,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.35` | 1,910.00 USD | 191,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.40` | 411,010.00 USD | 411,010.00 USD | 13,040.00 USD | 3,050.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.40` | 3,950,000.00 USD | 3,950,000.00 USD | 48,760.00 USD | 4,350.00 USD | 48,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.45` | 4,880.00 USD | 189,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.50` | 389,990.00 USD | 389,990.00 USD | 8,970.00 USD | 4,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.50` | 3,850,000.00 USD | 3,850,000.00 USD | 49,490.00 USD | 11,660.00 USD | 22,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.60` | 376,670.00 USD | 376,670.00 USD | 12,620.00 USD | 21,080.00 USD | 8,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.60` | 3,770,000.00 USD | 3,770,000.00 USD | 53,580.00 USD | 6,140.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.65` | 533.82 USD | 184,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.70` | 334,660.00 USD | 334,660.00 USD | 5,710.00 USD | 1,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.70` | 3,700,000.00 USD | 3,700,000.00 USD | 64,150.00 USD | 16,400.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.75` | 332.71 USD | 184,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.80` | 327,840.00 USD | 327,840.00 USD | 1,830.00 USD | 5,480.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.80` | 3,600,000.00 USD | 3,600,000.00 USD | 99,150.00 USD | 80,510.00 USD | 126,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.85` | 25,590.00 USD | 183,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.90` | 317,400.00 USD | 317,400.00 USD | 7,480.00 USD | 23,960.00 USD | 98,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.90` | 3,300,000.00 USD | 3,300,000.00 USD | 111,970.00 USD | 52,650.00 USD | 123,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.95` | 27,050.00 USD | 158,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.00` | 187,710.00 USD | 187,710.00 USD | 4,010.00 USD | 13,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.00` | 3,010,000.00 USD | 3,010,000.00 USD | 344,710.00 USD | 142,130.00 USD | 210,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.05` | 219.44 USD | 131,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.10` | 170,070.00 USD | 170,070.00 USD | 23,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.10` | 2,310,000.00 USD | 2,310,000.00 USD | 234,120.00 USD | 45,470.00 USD | 138,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.15` | 13,210.00 USD | 131,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.20` | 146,240.00 USD | 146,240.00 USD | 14,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.20` | 1,900,000.00 USD | 1,900,000.00 USD | 234,980.00 USD | 141,240.00 USD | 128,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.25` | 2,400.00 USD | 117,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.30` | 131,280.00 USD | 131,280.00 USD | 9,970.00 USD | 12,300.00 USD | 28,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.30` | 1,390,000.00 USD | 1,390,000.00 USD | 237,140.00 USD | 89,820.00 USD | 181,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.40` | 80,370.00 USD | 80,370.00 USD | 17,060.00 USD | 0.00 USD | 57,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.40` | 882,110.00 USD | 882,110.00 USD | 304,270.00 USD | 6,020.00 USD | 92,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.45` | 186.76 USD | 115,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.50` | 5,550.00 USD | 5,550.00 USD | 3,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.50` | 479,680.00 USD | 479,680.00 USD | 159,720.00 USD | 8,200.00 USD | 140,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.55` | 2,470.00 USD | 115,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.60` | 2,510.00 USD | 2,510.00 USD | 2,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.60` | 170,830.00 USD | 170,830.00 USD | 98,430.00 USD | 0.00 USD | 72,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.65` | 2,380.00 USD | 112,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `54.70` | 117,110.00 USD | 117,110.00 USD | 60,000.00 USD | 0.00 USD | 57,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `54.70` | 234,210.00 USD | 234,210.00 USD | 60,000.00 USD | 0.00 USD | 57,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `54.70` | 118,580.00 USD | 118,580.00 USD | 118,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `54.70` | 237,150.00 USD | 237,150.00 USD | 118,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.75` | 470.85 USD | 110,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `54.80` | 278,340.00 USD | 278,340.00 USD | 44,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `54.80` | 529,770.00 USD | 529,770.00 USD | 292,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.85` | 12,540.00 USD | 109,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `54.90` | 324,430.00 USD | 324,430.00 USD | 46,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `54.90` | 771,510.00 USD | 771,510.00 USD | 241,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.95` | 7,220.00 USD | 97,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `55.00` | 359,160.00 USD | 359,160.00 USD | 34,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.00` | 1,030,000.00 USD | 1,030,000.00 USD | 255,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.05` | 1,500.00 USD | 90,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `55.10` | 375,790.00 USD | 375,790.00 USD | 16,450.00 USD | 0.00 USD | 189.61 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.10` | 1,380,000.00 USD | 1,380,000.00 USD | 348,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.15` | 5,400.00 USD | 88,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `55.20` | 387,310.00 USD | 387,310.00 USD | 11,100.00 USD | 0.00 USD | 420.67 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.20` | 1,710,000.00 USD | 1,710,000.00 USD | 336,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.25` | 1,660.00 USD | 83,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `55.30` | 463,770.00 USD | 463,770.00 USD | 52,250.00 USD | 0.00 USD | 24,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.30` | 2,280,000.00 USD | 2,280,000.00 USD | 359,480.00 USD | 17,490.00 USD | 187,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.35` | 1,610.00 USD | 81,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `55.40` | 2,820,000.00 USD | 2,820,000.00 USD | 300,790.00 USD | 0.00 USD | 238,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.45` | 424.19 USD | 80,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `55.50` | 491,100.00 USD | 491,100.00 USD | 0.00 USD | 27,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.50` | 3,700,000.00 USD | 3,700,000.00 USD | 326,800.00 USD | 167,870.00 USD | 385,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.55` | 1,390.00 USD | 79,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `55.60` | 512,340.00 USD | 512,340.00 USD | 755.00 USD | 20,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.60` | 4,620,000.00 USD | 4,620,000.00 USD | 426,340.00 USD | 245,070.00 USD | 248,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.70` | 548,540.00 USD | 548,540.00 USD | 0.00 USD | 35,800.00 USD | 407.86 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.70` | 5,090,000.00 USD | 5,090,000.00 USD | 174,240.00 USD | 32,180.00 USD | 269,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.80` | 734,290.00 USD | 734,290.00 USD | 122,760.00 USD | 16,300.00 USD | 46,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.80` | 5,320,000.00 USD | 5,320,000.00 USD | 60,840.00 USD | 28,930.00 USD | 142,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.90` | 1,010,000.00 USD | 1,010,000.00 USD | 137,200.00 USD | 1,100.00 USD | 139,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.90` | 5,690,000.00 USD | 5,690,000.00 USD | 65,400.00 USD | 65,840.00 USD | 234,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.00` | 1,200,000.00 USD | 1,200,000.00 USD | 124,870.00 USD | 0.00 USD | 59,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.00` | 6,120,000.00 USD | 6,120,000.00 USD | 181,230.00 USD | 98,600.00 USD | 147,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.10` | 1,470,000.00 USD | 1,470,000.00 USD | 105,950.00 USD | 23,960.00 USD | 146,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.10` | 6,440,000.00 USD | 6,440,000.00 USD | 121,920.00 USD | 140,020.00 USD | 61,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `56.15` | 78,230.00 USD | 78,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `56.20` | 1,690,000.00 USD | 1,690,000.00 USD | 72,300.00 USD | 73,200.00 USD | 71,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.20` | 6,790,000.00 USD | 6,790,000.00 USD | 104,510.00 USD | 66,120.00 USD | 179,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.30` | 1,760,000.00 USD | 1,760,000.00 USD | 464.20 USD | 31,280.00 USD | 36,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.30` | 7,100,000.00 USD | 7,100,000.00 USD | 91,850.00 USD | 128,970.00 USD | 85,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.40` | 1,910,000.00 USD | 1,910,000.00 USD | 579.50 USD | 30,930.00 USD | 117,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.40` | 7,550,000.00 USD | 7,550,000.00 USD | 215,940.00 USD | 102,460.00 USD | 137,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.50` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 118,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.50` | 7,660,000.00 USD | 7,660,000.00 USD | 26,520.00 USD | 83,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.60` | 2,160,000.00 USD | 2,160,000.00 USD | 13,870.00 USD | 58,070.00 USD | 57,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.60` | 8,140,000.00 USD | 8,140,000.00 USD | 363,190.00 USD | 119,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.70` | 2,550,000.00 USD | 2,550,000.00 USD | 197,080.00 USD | 0.00 USD | 201,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.70` | 8,350,000.00 USD | 8,350,000.00 USD | 110,940.00 USD | 92,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.80` | 2,850,000.00 USD | 2,850,000.00 USD | 180,420.00 USD | 2,180.00 USD | 113,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.80` | 8,850,000.00 USD | 8,850,000.00 USD | 153,580.00 USD | 90,850.00 USD | 261,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.90` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 8,150.00 USD | 1,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.90` | 9,100,000.00 USD | 9,100,000.00 USD | 108,440.00 USD | 48,600.00 USD | 92,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.00` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 552.05 USD | 427.23 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.00` | 9,250,000.00 USD | 9,250,000.00 USD | 50,710.00 USD | 2,620.00 USD | 93,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.10` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 10,960.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.10` | 9,320,000.00 USD | 9,320,000.00 USD | 36,580.00 USD | 16,110.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.20` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 11,980.00 USD | 49,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.20` | 9,360,000.00 USD | 9,360,000.00 USD | 21,160.00 USD | 13,670.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.30` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 7,220.00 USD | 386.57 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.30` | 9,390,000.00 USD | 9,390,000.00 USD | 22,360.00 USD | 0.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.40` | 2,990,000.00 USD | 2,990,000.00 USD | 19,650.00 USD | 25,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.40` | 9,590,000.00 USD | 9,590,000.00 USD | 38,520.00 USD | 30,000.00 USD | 129,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.50` | 3,150,000.00 USD | 3,150,000.00 USD | 108,670.00 USD | 12,870.00 USD | 36,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.50` | 9,690,000.00 USD | 9,690,000.00 USD | 76,670.00 USD | 23,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.60` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 6,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.60` | 9,800,000.00 USD | 9,800,000.00 USD | 72,680.00 USD | 15,090.00 USD | 26,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.70` | 3,260,000.00 USD | 3,260,000.00 USD | 17,800.00 USD | 1,300.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.70` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 1,500.00 USD | 57,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.80` | 3,270,000.00 USD | 3,270,000.00 USD | 2,360.00 USD | 0.00 USD | 648.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.80` | 9,860,000.00 USD | 9,860,000.00 USD | 2,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.90` | 3,270,000.00 USD | 3,270,000.00 USD | 1,570.00 USD | 6,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.90` | 9,870,000.00 USD | 9,870,000.00 USD | 2,410.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.00` | 3,280,000.00 USD | 3,280,000.00 USD | 2,170.00 USD | 5,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.00` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 3,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.10` | 3,320,000.00 USD | 3,320,000.00 USD | 29,450.00 USD | 1,180.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.10` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 1,310.00 USD | 848.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.20` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 5,880.00 USD | 350.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.30` | 3,390,000.00 USD | 3,390,000.00 USD | 8,940.00 USD | 11,540.00 USD | 36,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.30` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 9,580.00 USD | 26,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.40` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 4,990.00 USD | 33,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.40` | 9,960,000.00 USD | 9,960,000.00 USD | 0.00 USD | 0.00 USD | 54,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.50` | 3,490,000.00 USD | 3,490,000.00 USD | 48,820.00 USD | 21,280.00 USD | 379.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.50` | 9,990,000.00 USD | 9,990,000.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.60` | 9,990,000.00 USD | 9,990,000.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.70` | 3,520,000.00 USD | 3,520,000.00 USD | 15,850.00 USD | 8,070.00 USD | 355.85 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.70` | 10,030,000.00 USD | 10,030,000.00 USD | 1,700.00 USD | 5,910.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.80` | 3,590,000.00 USD | 3,590,000.00 USD | 35,140.00 USD | 14,730.00 USD | 23,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.80` | 10,040,000.00 USD | 10,040,000.00 USD | 1,810.00 USD | 3,320.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.90` | 3,830,000.00 USD | 3,830,000.00 USD | 18,240.00 USD | 124,640.00 USD | 91,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.90` | 10,170,000.00 USD | 10,170,000.00 USD | 0.00 USD | 48,700.00 USD | 83,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.00` | 4,170,000.00 USD | 4,170,000.00 USD | 151,460.00 USD | 57,070.00 USD | 134,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.00` | 10,610,000.00 USD | 10,610,000.00 USD | 255,180.00 USD | 65,270.00 USD | 118,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.10` | 4,590,000.00 USD | 4,590,000.00 USD | 189,650.00 USD | 49,050.00 USD | 186,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.10` | 10,910,000.00 USD | 10,910,000.00 USD | 91,060.00 USD | 45,400.00 USD | 158,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.20` | 4,920,000.00 USD | 4,920,000.00 USD | 158,420.00 USD | 75,700.00 USD | 96,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.20` | 11,250,000.00 USD | 11,250,000.00 USD | 153,580.00 USD | 12,460.00 USD | 174,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.30` | 5,450,000.00 USD | 5,450,000.00 USD | 306,360.00 USD | 73,680.00 USD | 143,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.30` | 11,530,000.00 USD | 11,530,000.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.40` | 5,660,000.00 USD | 5,660,000.00 USD | 78,510.00 USD | 57,010.00 USD | 76,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.40` | 11,840,000.00 USD | 11,840,000.00 USD | 103,370.00 USD | 73,620.00 USD | 137,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.50` | 5,870,000.00 USD | 5,870,000.00 USD | 119,350.00 USD | 57,690.00 USD | 28,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.50` | 11,990,000.00 USD | 11,990,000.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.60` | 6,020,000.00 USD | 6,020,000.00 USD | 62,780.00 USD | 68,870.00 USD | 18,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.60` | 12,490,000.00 USD | 12,490,000.00 USD | 268,680.00 USD | 145,550.00 USD | 86,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.70` | 6,160,000.00 USD | 6,160,000.00 USD | 20,820.00 USD | 30,890.00 USD | 94,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.70` | 12,890,000.00 USD | 12,890,000.00 USD | 55,510.00 USD | 180,620.00 USD | 161,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.80` | 6,250,000.00 USD | 6,250,000.00 USD | 40,970.00 USD | 37,360.00 USD | 10,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.80` | 13,260,000.00 USD | 13,260,000.00 USD | 118,240.00 USD | 97,600.00 USD | 155,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.90` | 6,470,000.00 USD | 6,470,000.00 USD | 112,870.00 USD | 21,300.00 USD | 80,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.90` | 13,630,000.00 USD | 13,630,000.00 USD | 246,770.00 USD | 84,430.00 USD | 40,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.00` | 6,780,000.00 USD | 6,780,000.00 USD | 182,880.00 USD | 64,320.00 USD | 69,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.00` | 14,140,000.00 USD | 14,140,000.00 USD | 231,370.00 USD | 183,130.00 USD | 94,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.10` | 6,990,000.00 USD | 6,990,000.00 USD | 95,780.00 USD | 40,300.00 USD | 71,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.10` | 14,710,000.00 USD | 14,710,000.00 USD | 263,890.00 USD | 129,860.00 USD | 174,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.20` | 7,230,000.00 USD | 7,230,000.00 USD | 105,780.00 USD | 41,350.00 USD | 96,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.20` | 15,210,000.00 USD | 15,210,000.00 USD | 207,990.00 USD | 131,530.00 USD | 157,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.30` | 7,490,000.00 USD | 7,490,000.00 USD | 97,720.00 USD | 76,060.00 USD | 83,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.30` | 15,580,000.00 USD | 15,580,000.00 USD | 118,160.00 USD | 95,890.00 USD | 155,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.40` | 7,800,000.00 USD | 7,800,000.00 USD | 168,700.00 USD | 54,240.00 USD | 84,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.40` | 16,030,000.00 USD | 16,030,000.00 USD | 93,890.00 USD | 133,310.00 USD | 226,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.45` | 589.39 USD | 589.39 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.50` | 7,980,000.00 USD | 7,980,000.00 USD | 79,160.00 USD | 43,330.00 USD | 63,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.50` | 16,470,000.00 USD | 16,470,000.00 USD | 147,230.00 USD | 88,570.00 USD | 207,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.60` | 8,100,000.00 USD | 8,100,000.00 USD | 80,330.00 USD | 34,850.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.60` | 16,990,000.00 USD | 16,990,000.00 USD | 266,850.00 USD | 98,770.00 USD | 155,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.70` | 8,260,000.00 USD | 8,260,000.00 USD | 74,340.00 USD | 45,070.00 USD | 33,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.70` | 17,220,000.00 USD | 17,220,000.00 USD | 129,660.00 USD | 67,510.00 USD | 28,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.75` | 1,040.00 USD | 1,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.80` | 8,330,000.00 USD | 8,330,000.00 USD | 22,530.00 USD | 11,950.00 USD | 43,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.80` | 17,450,000.00 USD | 17,450,000.00 USD | 54,870.00 USD | 78,710.00 USD | 94,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.90` | 8,400,000.00 USD | 8,400,000.00 USD | 40,050.00 USD | 21,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.90` | 17,730,000.00 USD | 17,730,000.00 USD | 139,720.00 USD | 52,860.00 USD | 92,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.95` | 794.18 USD | 2,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.00` | 8,480,000.00 USD | 8,480,000.00 USD | 46,000.00 USD | 6,970.00 USD | 28,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 17,870,000.00 USD | 17,870,000.00 USD | 96,160.00 USD | 36,500.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.05` | 482.91 USD | 2,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.10` | 8,490,000.00 USD | 8,490,000.00 USD | 6,110.00 USD | 0.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 17,900,000.00 USD | 17,900,000.00 USD | 31,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.15` | 3,870.00 USD | 6,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.20` | 8,590,000.00 USD | 8,590,000.00 USD | 75,930.00 USD | 1,160.00 USD | 19,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.20` | 18,120,000.00 USD | 18,120,000.00 USD | 116,610.00 USD | 70,180.00 USD | 33,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.30` | 8,610,000.00 USD | 8,610,000.00 USD | 9,540.00 USD | 6,080.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.30` | 18,270,000.00 USD | 18,270,000.00 USD | 51,130.00 USD | 35,650.00 USD | 55,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.40` | 8,620,000.00 USD | 8,620,000.00 USD | 6,350.00 USD | 7,530.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.40` | 18,420,000.00 USD | 18,420,000.00 USD | 89,350.00 USD | 41,800.00 USD | 24,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.50` | 8,670,000.00 USD | 8,670,000.00 USD | 9,120.00 USD | 19,960.00 USD | 17,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.50` | 18,510,000.00 USD | 18,510,000.00 USD | 19,810.00 USD | 35,300.00 USD | 36,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.60` | 8,730,000.00 USD | 8,730,000.00 USD | 24,180.00 USD | 14,990.00 USD | 20,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.60` | 18,760,000.00 USD | 18,760,000.00 USD | 54,240.00 USD | 63,390.00 USD | 132,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.65` | 211,210.00 USD | 217,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.70` | 8,790,000.00 USD | 8,790,000.00 USD | 37,720.00 USD | 9,670.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.70` | 18,980,000.00 USD | 18,980,000.00 USD | 91,980.00 USD | 12,880.00 USD | 114,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.80` | 8,820,000.00 USD | 8,820,000.00 USD | 23,640.00 USD | 8,420.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.80` | 19,300,000.00 USD | 19,300,000.00 USD | 167,990.00 USD | 62,660.00 USD | 86,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.90` | 8,880,000.00 USD | 8,880,000.00 USD | 28,490.00 USD | 11,940.00 USD | 16,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.90` | 19,440,000.00 USD | 19,440,000.00 USD | 72,380.00 USD | 29,730.00 USD | 35,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.00` | 8,900,000.00 USD | 8,900,000.00 USD | 14,630.00 USD | 911.46 USD | 2,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.00` | 19,560,000.00 USD | 19,560,000.00 USD | 56,450.00 USD | 13,260.00 USD | 49,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.10` | 8,910,000.00 USD | 8,910,000.00 USD | 12,050.00 USD | 945.47 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.10` | 19,620,000.00 USD | 19,620,000.00 USD | 36,500.00 USD | 12,820.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.20` | 8,920,000.00 USD | 8,920,000.00 USD | 3,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.20` | 19,740,000.00 USD | 19,740,000.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.30` | 8,920,000.00 USD | 8,920,000.00 USD | 464.20 USD | 260.05 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.30` | 19,890,000.00 USD | 19,890,000.00 USD | 35,280.00 USD | 23,450.00 USD | 97,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.40` | 8,930,000.00 USD | 8,930,000.00 USD | 1,150.00 USD | 0.00 USD | 129.78 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.40` | 20,030,000.00 USD | 20,030,000.00 USD | 79,620.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.50` | 8,930,000.00 USD | 8,930,000.00 USD | 263.90 USD | 1,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.50` | 20,120,000.00 USD | 20,120,000.00 USD | 44,300.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.60` | 8,930,000.00 USD | 8,930,000.00 USD | 1,100.00 USD | 1,130.00 USD | 327.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.60` | 20,190,000.00 USD | 20,190,000.00 USD | 34,910.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.70` | 8,970,000.00 USD | 8,970,000.00 USD | 19,390.00 USD | 5,150.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.70` | 20,270,000.00 USD | 20,270,000.00 USD | 22,020.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.80` | 9,010,000.00 USD | 9,010,000.00 USD | 16,430.00 USD | 7,090.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.80` | 20,410,000.00 USD | 20,410,000.00 USD | 72,250.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.90` | 9,030,000.00 USD | 9,030,000.00 USD | 8,780.00 USD | 8,980.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.90` | 20,510,000.00 USD | 20,510,000.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.00` | 9,050,000.00 USD | 9,050,000.00 USD | 7,800.00 USD | 7,990.00 USD | 4,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.00` | 20,570,000.00 USD | 20,570,000.00 USD | 34,730.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.10` | 9,060,000.00 USD | 9,060,000.00 USD | 4,260.00 USD | 4,150.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.10` | 20,610,000.00 USD | 20,610,000.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.20` | 9,070,000.00 USD | 9,070,000.00 USD | 2,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.30` | 9,070,000.00 USD | 9,070,000.00 USD | 4,590.00 USD | 594.25 USD | 2,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.30` | 20,650,000.00 USD | 20,650,000.00 USD | 19,680.00 USD | 11,500.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.40` | 9,090,000.00 USD | 9,090,000.00 USD | 8,400.00 USD | 1,480.00 USD | 7,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.40` | 20,680,000.00 USD | 20,680,000.00 USD | 13,220.00 USD | 1,320.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.50` | 9,130,000.00 USD | 9,130,000.00 USD | 12,520.00 USD | 21,470.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.50` | 20,700,000.00 USD | 20,700,000.00 USD | 6,620.00 USD | 15,810.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.60` | 9,190,000.00 USD | 9,190,000.00 USD | 25,150.00 USD | 8,230.00 USD | 23,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.60` | 20,800,000.00 USD | 20,800,000.00 USD | 63,480.00 USD | 20,800.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.70` | 9,260,000.00 USD | 9,260,000.00 USD | 27,630.00 USD | 5,780.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.70` | 20,870,000.00 USD | 20,870,000.00 USD | 21,940.00 USD | 18,810.00 USD | 35,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.80` | 9,300,000.00 USD | 9,300,000.00 USD | 19,730.00 USD | 10,450.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.80` | 20,940,000.00 USD | 20,940,000.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.90` | 9,360,000.00 USD | 9,360,000.00 USD | 34,930.00 USD | 8,170.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.90` | 20,970,000.00 USD | 20,970,000.00 USD | 7,650.00 USD | 12,840.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.00` | 9,380,000.00 USD | 9,380,000.00 USD | 7,880.00 USD | 6,900.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.00` | 21,010,000.00 USD | 21,010,000.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.10` | 9,400,000.00 USD | 9,400,000.00 USD | 13,740.00 USD | 5,360.00 USD | 80.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.10` | 21,040,000.00 USD | 21,040,000.00 USD | 20,350.00 USD | 667.05 USD | 10,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.20` | 9,420,000.00 USD | 9,420,000.00 USD | 2,760.00 USD | 8,200.00 USD | 273.52 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.20` | 21,090,000.00 USD | 21,090,000.00 USD | 28,840.00 USD | 14,530.00 USD | 584.77 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.40` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 946.37 USD | 13,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.40` | 21,140,000.00 USD | 21,140,000.00 USD | 2,540.00 USD | 20,590.00 USD | 29,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.50` | 21,170,000.00 USD | 21,170,000.00 USD | 7,700.00 USD | 7,120.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.60` | 21,210,000.00 USD | 21,210,000.00 USD | 32,220.00 USD | 14,180.00 USD | 108.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.70` | 21,280,000.00 USD | 21,280,000.00 USD | 39,430.00 USD | 23,030.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.80` | 21,320,000.00 USD | 21,320,000.00 USD | 7,540.00 USD | 8,210.00 USD | 20,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.90` | 21,360,000.00 USD | 21,360,000.00 USD | 25,320.00 USD | 8,010.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.00` | 21,380,000.00 USD | 21,380,000.00 USD | 1,790.00 USD | 9,480.00 USD | 13,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.10` | 21,440,000.00 USD | 21,440,000.00 USD | 5,810.00 USD | 14,250.00 USD | 37,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.20` | 21,480,000.00 USD | 21,480,000.00 USD | 10,380.00 USD | 2,250.00 USD | 28,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.30` | 21,530,000.00 USD | 21,530,000.00 USD | 22,330.00 USD | 9,180.00 USD | 22,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `65.95` | 1,160.00 USD | 219,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.85` | 33,950.00 USD | 253,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.95` | 121.18 USD | 253,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.85` | 709.03 USD | 253,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `69.45` | 414.62 USD | 254,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `70.45` | 5,270.00 USD | 259,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `72.95` | 666.03 USD | 260,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `76.35` | 8,380.00 USD | 268,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.85` | 602.56 USD | 269,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.95` | 136.41 USD | 269,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.75` | 646.00 USD | 270,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.05` | 19,000.00 USD | 289,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.55` | 123.96 USD | 289,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.65` | 3,850.00 USD | 293,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.75` | 214.32 USD | 293,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `84.65` | 862.58 USD | 294,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `85.45` | 2,820.00 USD | 296,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `86.35` | 3,450.00 USD | 300,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `87.45` | 23,330.00 USD | 323,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `96.35` | 2,410.00 USD | 326,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.05` | 669.68 USD | 326,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.45` | 1,050.00 USD | 327,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.85` | 353,760.00 USD | 681,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.45` | 21,090.00 USD | 702,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.25` | 21,850.00 USD | 724,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.45` | 131.44 USD | 724,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.55` | 1,120.00 USD | 725,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.65` | 973.72 USD | 726,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.75` | 3,860.00 USD | 730,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 664.59 USD | 731,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.65` | 420.77 USD | 731,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `11.35` | 2,700,000.00 USD | 0.00 USD | 136.20 USD | `-79.22%` | `12.00` |
| `Live` | `Long` | `11.75` | 2,700,000.00 USD | 0.00 USD | 105.98 USD | `-78.49%` | `9.02` |
| `Live` | `Long` | `12.25` | 2,700,000.00 USD | 0.00 USD | 122.50 USD | `-77.57%` | `10.00` |
| `Live` | `Long` | `12.35` | 2,700,000.00 USD | 0.00 USD | 395.20 USD | `-77.39%` | `32.00` |
| `Live` | `Long` | `12.75` | 2,700,000.00 USD | 0.00 USD | 2,560.00 USD | `-76.66%` | `200.43` |
| `Live` | `Long` | `12.85` | 2,700,000.00 USD | 0.00 USD | 334.74 USD | `-76.48%` | `26.05` |
| `Live` | `Long` | `13.05` | 2,700,000.00 USD | 0.00 USD | 2,200.00 USD | `-76.11%` | `168.79` |
| `Live` | `Long` | `13.65` | 2,700,000.00 USD | 0.00 USD | 150.15 USD | `-75.01%` | `11.00` |
| `Live` | `Long` | `17.65` | 2,690,000.00 USD | 0.00 USD | 2,120.00 USD | `-67.69%` | `120.00` |
| `Live` | `Long` | `18.75` | 2,690,000.00 USD | 0.00 USD | 18,030.00 USD | `-65.68%` | `961.58` |
| `Live` | `Long` | `19.05` | 2,670,000.00 USD | 0.00 USD | 3,470.00 USD | `-65.13%` | `182.00` |
| `Live` | `Long` | `19.45` | 2,670,000.00 USD | 0.00 USD | 2,010.00 USD | `-64.39%` | `103.47` |
| `Live` | `Long` | `19.65` | 2,670,000.00 USD | 0.00 USD | 158.18 USD | `-64.03%` | `8.05` |
| `Live` | `Long` | `20.05` | 2,670,000.00 USD | 0.00 USD | 445.91 USD | `-63.30%` | `22.24` |
| `Live` | `Long` | `21.05` | 2,670,000.00 USD | 0.00 USD | 3,170.00 USD | `-61.47%` | `150.57` |
| `Live` | `Long` | `21.15` | 2,670,000.00 USD | 0.00 USD | 423.00 USD | `-61.28%` | `20.00` |
| `Live` | `Long` | `21.75` | 2,670,000.00 USD | 0.00 USD | 6,410.00 USD | `-60.18%` | `294.67` |
| `Live` | `Long` | `22.05` | 2,660,000.00 USD | 0.00 USD | 4,300.00 USD | `-59.63%` | `195.03` |
| `Live` | `Long` | `22.15` | 2,650,000.00 USD | 0.00 USD | 146.19 USD | `-59.45%` | `6.60` |
| `Live` | `Long` | `22.85` | 2,650,000.00 USD | 0.00 USD | 368.57 USD | `-58.17%` | `16.13` |
| `Live` | `Long` | `23.25` | 2,650,000.00 USD | 0.00 USD | 1,400.00 USD | `-57.44%` | `60.00` |
| `Live` | `Long` | `23.55` | 2,650,000.00 USD | 0.00 USD | 5,300.00 USD | `-56.89%` | `225.00` |
| `Live` | `Long` | `23.85` | 2,650,000.00 USD | 0.00 USD | 195.57 USD | `-56.34%` | `8.20` |
| `Live` | `Long` | `24.15` | 2,650,000.00 USD | 0.00 USD | 432.77 USD | `-55.79%` | `17.92` |
| `Live` | `Long` | `24.85` | 2,650,000.00 USD | 0.00 USD | 967.16 USD | `-54.51%` | `38.92` |
| `Live` | `Long` | `25.25` | 2,650,000.00 USD | 0.00 USD | 277,980.00 USD | `-53.78%` | `11,009.19` |
| `Live` | `Long` | `25.35` | 2,370,000.00 USD | 0.00 USD | 173.39 USD | `-53.59%` | `6.84` |
| `Live` | `Long` | `25.55` | 2,370,000.00 USD | 0.00 USD | 50,740.00 USD | `-53.23%` | `1,985.99` |
| `Live` | `Long` | `25.85` | 2,320,000.00 USD | 0.00 USD | 152.77 USD | `-52.68%` | `5.91` |
| `Live` | `Long` | `25.95` | 2,320,000.00 USD | 0.00 USD | 374.20 USD | `-52.50%` | `14.42` |
| `Live` | `Long` | `26.45` | 2,320,000.00 USD | 0.00 USD | 955.64 USD | `-51.58%` | `36.13` |
| `Live` | `Long` | `26.75` | 2,320,000.00 USD | 0.00 USD | 24,880.00 USD | `-51.03%` | `930.00` |
| `Live` | `Long` | `26.95` | 2,290,000.00 USD | 0.00 USD | 5,490.00 USD | `-50.66%` | `203.85` |
| `Live` | `Long` | `27.55` | 2,280,000.00 USD | 0.00 USD | 272.75 USD | `-49.57%` | `9.90` |
| `Live` | `Long` | `27.85` | 2,280,000.00 USD | 0.00 USD | 139.25 USD | `-49.02%` | `5.00` |
| `Live` | `Long` | `27.95` | 2,280,000.00 USD | 0.00 USD | 173.85 USD | `-48.83%` | `6.22` |
| `Live` | `Long` | `28.45` | 2,280,000.00 USD | 0.00 USD | 4,670.00 USD | `-47.92%` | `164.08` |
| `Live` | `Long` | `29.15` | 2,280,000.00 USD | 0.00 USD | 583.00 USD | `-46.64%` | `20.00` |
| `Live` | `Long` | `29.55` | 2,280,000.00 USD | 0.00 USD | 835.38 USD | `-45.90%` | `28.27` |
| `Live` | `Long` | `29.75` | 2,280,000.00 USD | 0.00 USD | 297,600.00 USD | `-45.54%` | `10,003.44` |
| `Live` | `Long` | `29.85` | 1,980,000.00 USD | 0.00 USD | 472.23 USD | `-45.36%` | `15.82` |
| `Live` | `Long` | `30.05` | 1,980,000.00 USD | 0.00 USD | 218.46 USD | `-44.99%` | `7.27` |
| `Live` | `Long` | `30.95` | 1,980,000.00 USD | 0.00 USD | 538.53 USD | `-43.34%` | `17.40` |
| `Live` | `Long` | `31.15` | 1,980,000.00 USD | 0.00 USD | 27,620.00 USD | `-42.98%` | `886.80` |
| `Live` | `Long` | `31.55` | 1,950,000.00 USD | 0.00 USD | 5,680.00 USD | `-42.24%` | `180.02` |
| `Live` | `Long` | `31.85` | 1,950,000.00 USD | 0.00 USD | 6,820.00 USD | `-41.69%` | `214.01` |
| `Live` | `Long` | `31.95` | 1,940,000.00 USD | 0.00 USD | 125.24 USD | `-41.51%` | `3.92` |
| `Live` | `Long` | `32.15` | 1,940,000.00 USD | 0.00 USD | 450.10 USD | `-41.15%` | `14.00` |
| `Live` | `Long` | `32.25` | 1,940,000.00 USD | 0.00 USD | 270.90 USD | `-40.96%` | `8.40` |
| `Live` | `Long` | `32.45` | 1,940,000.00 USD | 0.00 USD | 166.47 USD | `-40.60%` | `5.13` |
| `Live` | `Long` | `32.65` | 1,940,000.00 USD | 0.00 USD | 653.00 USD | `-40.23%` | `20.00` |
| `Live` | `Long` | `32.75` | 1,940,000.00 USD | 0.00 USD | 953.68 USD | `-40.05%` | `29.12` |
| `Live` | `Long` | `32.85` | 1,940,000.00 USD | 0.00 USD | 32,850.00 USD | `-39.86%` | `1,000.01` |
| `Live` | `Long` | `33.35` | 1,900,000.00 USD | 0.00 USD | 625.31 USD | `-38.95%` | `18.75` |
| `Live` | `Long` | `33.65` | 1,900,000.00 USD | 0.00 USD | 257.76 USD | `-38.40%` | `7.66` |
| `Live` | `Long` | `34.05` | 1,900,000.00 USD | 0.00 USD | 421.20 USD | `-37.67%` | `12.37` |
| `Live` | `Long` | `34.15` | 1,900,000.00 USD | 0.00 USD | 126.70 USD | `-37.48%` | `3.71` |
| `Live` | `Long` | `34.35` | 1,900,000.00 USD | 0.00 USD | 14,790.00 USD | `-37.12%` | `430.63` |
| `Live` | `Long` | `34.65` | 1,890,000.00 USD | 0.00 USD | 3,240.00 USD | `-36.57%` | `93.56` |
| `Live` | `Long` | `34.95` | 1,880,000.00 USD | 0.00 USD | 104.85 USD | `-36.02%` | `3.00` |
| `Live` | `Long` | `35.05` | 1,880,000.00 USD | 0.00 USD | 166.49 USD | `-35.84%` | `4.75` |
| `Live` | `Long` | `36.35` | 1,880,000.00 USD | 0.00 USD | 3,020.00 USD | `-33.46%` | `83.03` |
| `Live` | `Long` | `36.45` | 1,880,000.00 USD | 0.00 USD | 423.18 USD | `-33.27%` | `11.61` |
| `Live` | `Long` | `36.55` | 1,880,000.00 USD | 0.00 USD | 1,010.00 USD | `-33.09%` | `27.71` |
| `Live` | `Long` | `36.75` | 1,880,000.00 USD | 0.00 USD | 5,610.00 USD | `-32.72%` | `152.77` |
| `Live` | `Long` | `37.05` | 1,870,000.00 USD | 0.00 USD | 359.76 USD | `-32.18%` | `9.71` |
| `Live` | `Long` | `37.15` | 1,870,000.00 USD | 0.00 USD | 438.74 USD | `-31.99%` | `11.81` |
| `Live` | `Long` | `37.25` | 1,870,000.00 USD | 0.00 USD | 1,860.00 USD | `-31.81%` | `50.00` |
| `Live` | `Long` | `37.35` | 1,870,000.00 USD | 0.00 USD | 9,260.00 USD | `-31.63%` | `247.91` |
| `Live` | `Long` | `37.55` | 1,860,000.00 USD | 0.00 USD | 3,530.00 USD | `-31.26%` | `94.04` |
| `Live` | `Long` | `37.75` | 1,860,000.00 USD | 0.00 USD | 295.58 USD | `-30.89%` | `7.83` |
| `Live` | `Long` | `37.85` | 1,860,000.00 USD | 0.00 USD | 6,210.00 USD | `-30.71%` | `164.03` |
| `Live` | `Long` | `37.95` | 1,850,000.00 USD | 0.00 USD | 446.67 USD | `-30.53%` | `11.77` |
| `Live` | `Long` | `38.05` | 1,850,000.00 USD | 0.00 USD | 7,570.00 USD | `-30.34%` | `198.87` |
| `Live` | `Long` | `38.15` | 1,840,000.00 USD | 0.00 USD | 361.28 USD | `-30.16%` | `9.47` |
| `Live` | `Long` | `38.25` | 1,840,000.00 USD | 0.00 USD | 455.94 USD | `-29.98%` | `11.92` |
| `Live` | `Long` | `38.35` | 1,840,000.00 USD | 0.00 USD | 341.70 USD | `-29.80%` | `8.91` |
| `Live` | `Long` | `38.45` | 1,840,000.00 USD | 0.00 USD | 287.61 USD | `-29.61%` | `7.48` |
| `Live` | `Long` | `38.55` | 1,840,000.00 USD | 0.00 USD | 4,880.00 USD | `-29.43%` | `126.57` |
| `Live` | `Long` | `38.65` | 1,840,000.00 USD | 0.00 USD | 5,480.00 USD | `-29.25%` | `141.89` |
| `Live` | `Long` | `38.95` | 1,830,000.00 USD | 0.00 USD | 4,840.00 USD | `-28.70%` | `124.26` |
| `Live` | `Long` | `39.05` | 1,830,000.00 USD | 0.00 USD | 664,760.00 USD | `-28.51%` | `17,023.28` |
| `Live` | `Long` | `39.15` | 1,160,000.00 USD | 0.00 USD | 570.02 USD | `-28.33%` | `14.56` |
| `Live` | `Long` | `39.45` | 1,160,000.00 USD | 0.00 USD | 865.53 USD | `-27.78%` | `21.94` |
| `Live` | `Long` | `39.55` | 1,160,000.00 USD | 0.00 USD | 162.95 USD | `-27.60%` | `4.12` |
| `Live` | `Long` | `39.65` | 1,160,000.00 USD | 0.00 USD | 5,900.00 USD | `-27.42%` | `148.78` |
| `Live` | `Long` | `39.75` | 1,160,000.00 USD | 0.00 USD | 1,550.00 USD | `-27.23%` | `38.90` |
| `Live` | `Long` | `39.85` | 1,150,000.00 USD | 0.00 USD | 1,170.00 USD | `-27.05%` | `29.34` |
| `Live` | `Long` | `39.95` | 1,150,000.00 USD | 0.00 USD | 8,790.00 USD | `-26.87%` | `220.00` |
| `Live` | `Long` | `40.05` | 1,140,000.00 USD | 0.00 USD | 2,160.00 USD | `-26.68%` | `53.97` |
| `Live` | `Long` | `40.45` | 1,140,000.00 USD | 0.00 USD | 1,010.00 USD | `-25.95%` | `24.92` |
| `Live` | `Long` | `40.55` | 1,140,000.00 USD | 0.00 USD | 133.00 USD | `-25.77%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,140,000.00 USD | 0.00 USD | 1,650.00 USD | `-25.58%` | `40.69` |
| `Live` | `Long` | `40.85` | 1,140,000.00 USD | 0.00 USD | 6,340.00 USD | `-25.22%` | `155.23` |
| `Live` | `Long` | `40.95` | 1,130,000.00 USD | 0.00 USD | 509.01 USD | `-25.04%` | `12.43` |
| `Live` | `Long` | `41.05` | 1,130,000.00 USD | 0.00 USD | 396.54 USD | `-24.85%` | `9.66` |
| `Live` | `Long` | `41.25` | 1,130,000.00 USD | 0.00 USD | 14,490.00 USD | `-24.49%` | `351.26` |
| `Live` | `Long` | `41.35` | 1,120,000.00 USD | 0.00 USD | 25,190.00 USD | `-24.30%` | `609.13` |
| `Live` | `Long` | `41.45` | 1,090,000.00 USD | 0.00 USD | 644.96 USD | `-24.12%` | `15.56` |
| `Live` | `Long` | `41.55` | 1,090,000.00 USD | 0.00 USD | 41,550.00 USD | `-23.94%` | `1,000.00` |
| `Live` | `Long` | `41.75` | 1,050,000.00 USD | 0.00 USD | 662.99 USD | `-23.57%` | `15.88` |
| `Live` | `Long` | `42.05` | 1,050,000.00 USD | 0.00 USD | 4,140.00 USD | `-23.02%` | `98.45` |
| `Live` | `Long` | `42.15` | 1,040,000.00 USD | 0.00 USD | 64,190.00 USD | `-22.84%` | `1,522.78` |
| `Live` | `Long` | `42.25` | 980,460.00 USD | 0.00 USD | 35,410.00 USD | `-22.66%` | `838.00` |
| `Live` | `Long` | `42.45` | 945,060.00 USD | 0.00 USD | 5,460.00 USD | `-22.29%` | `128.71` |
| `Live` | `Long` | `42.65` | 939,590.00 USD | 0.00 USD | 4,960.00 USD | `-21.92%` | `116.19` |
| `Live` | `Long` | `42.85` | 934,640.00 USD | 0.00 USD | 5,800.00 USD | `-21.56%` | `135.38` |
| `Live` | `Long` | `42.95` | 928,840.00 USD | 0.00 USD | 2,000.00 USD | `-21.37%` | `46.65` |
| `Live` | `Long` | `43.05` | 926,830.00 USD | 0.00 USD | 8,950.00 USD | `-21.19%` | `208.00` |
| `Live` | `Long` | `43.15` | 917,880.00 USD | 0.00 USD | 121,600.00 USD | `-21.01%` | `2,818.00` |
| `Live` | `Long` | `43.25` | 796,280.00 USD | 0.00 USD | 312.26 USD | `-20.83%` | `7.22` |
| `Live` | `Long` | `43.35` | 795,970.00 USD | 0.00 USD | 5,390.00 USD | `-20.64%` | `124.24` |
| `Live` | `Long` | `43.45` | 790,580.00 USD | 0.00 USD | 12,210.00 USD | `-20.46%` | `281.07` |
| `Live` | `Long` | `43.65` | 778,370.00 USD | 0.00 USD | 737.25 USD | `-20.09%` | `16.89` |
| `Live` | `Long` | `43.75` | 777,630.00 USD | 0.00 USD | 21,880.00 USD | `-19.91%` | `500.00` |
| `Live` | `Long` | `43.85` | 755,760.00 USD | 0.00 USD | 801.14 USD | `-19.73%` | `18.27` |
| `Live` | `Long` | `43.95` | 754,960.00 USD | 0.00 USD | 1,580.00 USD | `-19.54%` | `35.97` |
| `Live` | `Long` | `44.15` | 753,380.00 USD | 0.00 USD | 2,380.00 USD | `-19.18%` | `53.99` |
| `Live` | `Long` | `44.35` | 750,990.00 USD | 0.00 USD | 84,440.00 USD | `-18.81%` | `1,903.87` |
| `Live` | `Long` | `44.45` | 666,560.00 USD | 0.00 USD | 1,670.00 USD | `-18.63%` | `37.50` |
| `Live` | `Long` | `44.55` | 664,890.00 USD | 0.00 USD | 4,650.00 USD | `-18.45%` | `104.34` |
| `Live` | `Long` | `44.75` | 660,240.00 USD | 0.00 USD | 4,230.00 USD | `-18.08%` | `94.55` |
| `Live` | `Long` | `44.85` | 656,010.00 USD | 0.00 USD | 134.55 USD | `-17.90%` | `3.00` |
| `Live` | `Long` | `44.95` | 655,880.00 USD | 0.00 USD | 2,620.00 USD | `-17.71%` | `58.18` |
| `Live` | `Long` | `45.05` | 653,260.00 USD | 0.00 USD | 329.32 USD | `-17.53%` | `7.31` |
| `Live` | `Long` | `45.15` | 652,930.00 USD | 0.00 USD | 135.00 USD | `-17.35%` | `2.99` |
| `Live` | `Long` | `45.25` | 652,800.00 USD | 0.00 USD | 3,180.00 USD | `-17.16%` | `70.37` |
| `Live` | `Long` | `45.35` | 649,610.00 USD | 0.00 USD | 2,180.00 USD | `-16.98%` | `48.02` |
| `Live` | `Long` | `45.45` | 647,430.00 USD | 0.00 USD | 23,940.00 USD | `-16.80%` | `526.65` |
| `Live` | `Long` | `45.55` | 623,500.00 USD | 0.00 USD | 493.31 USD | `-16.61%` | `10.83` |
| `Live` | `Long` | `45.95` | 623,000.00 USD | 0.00 USD | 704.87 USD | `-15.88%` | `15.34` |
| `Live` | `Long` | `46.05` | 622,300.00 USD | 0.00 USD | 9,710.00 USD | `-15.70%` | `210.95` |
| `Live` | `Long` | `46.15` | 612,590.00 USD | 0.00 USD | 265.82 USD | `-15.52%` | `5.76` |
| `Live` | `Long` | `46.35` | 612,320.00 USD | 0.00 USD | 383.78 USD | `-15.15%` | `8.28` |
| `Live` | `Long` | `46.65` | 611,940.00 USD | 0.00 USD | 936.73 USD | `-14.60%` | `20.08` |
| `Live` | `Long` | `46.75` | 611,000.00 USD | 0.00 USD | 1,640.00 USD | `-14.42%` | `35.00` |
| `Live` | `Long` | `46.85` | 609,360.00 USD | 0.00 USD | 358.40 USD | `-14.23%` | `7.65` |
| `Live` | `Long` | `46.95` | 609,000.00 USD | 0.00 USD | 158.22 USD | `-14.05%` | `3.37` |
| `Live` | `Long` | `47.15` | 608,850.00 USD | 0.00 USD | 1,980.00 USD | `-13.69%` | `42.07` |
| `Live` | `Long` | `47.25` | 606,860.00 USD | 0.00 USD | 574.09 USD | `-13.50%` | `12.15` |
| `Live` | `Long` | `47.45` | 606,290.00 USD | 0.00 USD | 4,820.00 USD | `-13.14%` | `101.62` |
| `Live` | `Long` | `47.55` | 601,470.00 USD | 0.00 USD | 1,770.00 USD | `-12.95%` | `37.28` |
| `Live` | `Long` | `47.65` | 599,690.00 USD | 0.00 USD | 7,840.00 USD | `-12.77%` | `164.58` |
| `Live` | `Long` | `47.75` | 591,850.00 USD | 0.00 USD | 4,780.00 USD | `-12.59%` | `100.00` |
| `Live` | `Long` | `47.95` | 587,080.00 USD | 0.00 USD | 977.70 USD | `-12.22%` | `20.39` |
| `Live` | `Long` | `48.05` | 586,100.00 USD | 0.00 USD | 1,340.00 USD | `-12.04%` | `27.93` |
| `Live` | `Long` | `48.15` | 584,760.00 USD | 0.00 USD | 2,680.00 USD | `-11.86%` | `55.56` |
| `Live` | `Long` | `48.25` | 582,080.00 USD | 0.00 USD | 525.44 USD | `-11.67%` | `10.89` |
| `Live` | `Long` | `48.55` | 581,560.00 USD | 0.00 USD | 2,030.00 USD | `-11.12%` | `41.85` |
| `Live` | `Long` | `48.65` | 579,520.00 USD | 0.00 USD | 273.90 USD | `-10.94%` | `5.63` |
| `Live` | `Long` | `48.75` | 579,250.00 USD | 0.00 USD | 231.56 USD | `-10.76%` | `4.75` |
| `Live` | `Long` | `48.95` | 579,020.00 USD | 0.00 USD | 797.40 USD | `-10.39%` | `16.29` |
| `Live` | `Long` | `49.05` | 578,220.00 USD | 0.00 USD | 1,580.00 USD | `-10.21%` | `32.25` |
| `Live` | `Long` | `49.15` | 576,640.00 USD | 0.00 USD | 5,740.00 USD | `-10.02%` | `116.83` |
| `Live` | `Long` | `49.35` | 570,900.00 USD | 0.00 USD | 5,230.00 USD | `-9.66%` | `105.97` |
| `Live` | `Long` | `49.45` | 565,670.00 USD | 0.00 USD | 22,670.00 USD | `-9.48%` | `458.50` |
| `Live` | `Long` | `49.55` | 543,000.00 USD | 0.00 USD | 19,940.00 USD | `-9.29%` | `402.36` |
| `Live` | `Long` | `49.65` | 523,060.00 USD | 0.00 USD | 4,890.00 USD | `-9.11%` | `98.52` |
| `Live` | `Long` | `49.75` | 518,170.00 USD | 0.00 USD | 1,250.00 USD | `-8.93%` | `25.06` |
| `Live` | `Long` | `49.95` | 516,920.00 USD | 0.00 USD | 28,540.00 USD | `-8.56%` | `571.31` |
| `Live` | `Long` | `50.05` | 488,380.00 USD | 0.00 USD | 1,820.00 USD | `-8.38%` | `36.43` |
| `Live` | `Long` | `50.25` | 486,560.00 USD | 0.00 USD | 102.51 USD | `-8.01%` | `2.04` |
| `Live` | `Long` | `50.35` | 486,460.00 USD | 0.00 USD | 1,290.00 USD | `-7.83%` | `25.67` |
| `Live` | `Long` | `50.45` | 485,160.00 USD | 0.00 USD | 4,720.00 USD | `-7.64%` | `93.64` |
| `Live` | `Long` | `50.55` | 480,440.00 USD | 0.00 USD | 84,100.00 USD | `-7.46%` | `1,663.61` |
| `Live` | `Long` | `50.75` | 396,350.00 USD | 0.00 USD | 9,320.00 USD | `-7.10%` | `183.72` |
| `Live` | `Long` | `50.85` | 387,020.00 USD | 0.00 USD | 106.79 USD | `-6.91%` | `2.10` |
| `Live` | `Long` | `50.95` | 386,910.00 USD | 0.00 USD | 245.07 USD | `-6.73%` | `4.81` |
| `Live` | `Long` | `51.15` | 386,670.00 USD | 0.00 USD | 219,370.00 USD | `-6.36%` | `4,288.79` |
| `Live` | `Long` | `51.45` | 167,300.00 USD | 0.00 USD | 20,410.00 USD | `-5.81%` | `396.78` |
| `Live` | `Long` | `51.55` | 146,880.00 USD | 0.00 USD | 551.07 USD | `-5.63%` | `10.69` |
| `Live` | `Long` | `51.65` | 146,330.00 USD | 0.00 USD | 155.47 USD | `-5.45%` | `3.01` |
| `Live` | `Long` | `51.75` | 146,180.00 USD | 0.00 USD | 12,660.00 USD | `-5.26%` | `244.64` |
| `Live` | `Long` | `51.85` | 133,520.00 USD | 0.00 USD | 3,580.00 USD | `-5.08%` | `69.10` |
| `Live` | `Long` | `51.95` | 129,930.00 USD | 0.00 USD | 10,300.00 USD | `-4.90%` | `198.33` |
| `Live` | `Long` | `52.15` | 119,630.00 USD | 0.00 USD | 3,390.00 USD | `-4.53%` | `65.00` |
| `Live` | `Long` | `52.35` | 116,240.00 USD | 0.00 USD | 2,700.00 USD | `-4.17%` | `51.51` |
| `Live` | `Long` | `52.45` | 113,540.00 USD | 0.00 USD | 3,830.00 USD | `-3.98%` | `72.95` |
| `Live` | `Long` | `52.55` | 109,720.00 USD | 0.00 USD | 8,700.00 USD | `-3.80%` | `165.49` |
| `Live` | `Long` | `52.75` | 101,020.00 USD | 0.00 USD | 7,290.00 USD | `-3.43%` | `138.28` |
| `Live` | `Long` | `52.85` | 93,730.00 USD | 0.00 USD | 5,950.00 USD | `-3.25%` | `112.64` |
| `Live` | `Long` | `52.95` | 87,770.00 USD | 0.00 USD | 20,790.00 USD | `-3.07%` | `392.63` |
| `Live` | `Long` | `53.05` | 66,980.00 USD | 0.00 USD | 900.26 USD | `-2.89%` | `16.97` |
| `Live` | `Long` | `53.15` | 66,080.00 USD | 0.00 USD | 21,970.00 USD | `-2.70%` | `413.30` |
| `Live` | `Long` | `53.25` | 44,120.00 USD | 0.00 USD | 1,860.00 USD | `-2.52%` | `34.87` |
| `Live` | `Long` | `53.35` | 42,260.00 USD | 0.00 USD | 1,910.00 USD | `-2.34%` | `35.71` |
| `Live` | `Long` | `53.45` | 40,360.00 USD | 0.00 USD | 4,880.00 USD | `-2.15%` | `91.21` |
| `Live` | `Long` | `53.65` | 35,480.00 USD | 0.00 USD | 454.95 USD | `-1.79%` | `8.48` |
| `Live` | `Long` | `53.75` | 35,030.00 USD | 0.00 USD | 148.35 USD | `-1.60%` | `2.76` |
| `Live` | `Long` | `53.85` | 34,880.00 USD | 0.00 USD | 2,130.00 USD | `-1.42%` | `39.58` |
| `Live` | `Long` | `53.95` | 32,750.00 USD | 0.00 USD | 27,050.00 USD | `-1.24%` | `501.35` |
| `Live` | `Long` | `54.05` | 5,700.00 USD | 0.00 USD | 219.44 USD | `-1.05%` | `4.06` |
| `Live` | `Long` | `54.15` | 5,480.00 USD | 0.00 USD | 3,080.00 USD | `-0.87%` | `56.91` |
| `Live` | `Long` | `54.25` | 2,400.00 USD | 0.00 USD | 2,400.00 USD | `-0.69%` | `44.18` |
| `Live` | `Short` | `54.35` | 2,620.00 USD | 2,620.00 USD | 0.00 USD | `-0.51%` | `48.28` |
| `Live` | `Short` | `54.95` | 6,480.00 USD | 3,850.00 USD | 0.00 USD | `+0.59%` | `70.15` |
| `Live` | `Short` | `55.75` | 7,320.00 USD | 839.60 USD | 0.00 USD | `+2.06%` | `15.06` |
| `Live` | `Short` | `57.15` | 11,030.00 USD | 3,710.00 USD | 0.00 USD | `+4.62%` | `64.90` |
| `Live` | `Short` | `57.45` | 12,070.00 USD | 1,040.00 USD | 0.00 USD | `+5.17%` | `18.17` |
| `Live` | `Short` | `57.95` | 101,790.00 USD | 89,720.00 USD | 0.00 USD | `+6.09%` | `1,548.25` |
| `Live` | `Short` | `58.25` | 103,390.00 USD | 1,600.00 USD | 0.00 USD | `+6.63%` | `27.49` |
| `Live` | `Short` | `59.35` | 112,840.00 USD | 9,440.00 USD | 0.00 USD | `+8.65%` | `159.09` |
| `Live` | `Short` | `60.95` | 113,630.00 USD | 794.18 USD | 0.00 USD | `+11.58%` | `13.03` |
| `Live` | `Short` | `61.15` | 117,500.00 USD | 3,870.00 USD | 0.00 USD | `+11.94%` | `63.26` |
| `Live` | `Short` | `61.65` | 328,700.00 USD | 211,210.00 USD | 0.00 USD | `+12.86%` | `3,425.89` |
| `Live` | `Short` | `65.95` | 329,860.00 USD | 1,160.00 USD | 0.00 USD | `+20.73%` | `17.59` |
| `Live` | `Short` | `66.85` | 363,810.00 USD | 33,950.00 USD | 0.00 USD | `+22.38%` | `507.83` |
| `Live` | `Short` | `66.95` | 363,930.00 USD | 121.18 USD | 0.00 USD | `+22.56%` | `1.81` |
| `Live` | `Short` | `67.55` | 364,960.00 USD | 1,020.00 USD | 0.00 USD | `+23.66%` | `15.12` |
| `Live` | `Short` | `67.85` | 365,660.00 USD | 709.03 USD | 0.00 USD | `+24.21%` | `10.45` |
| `Live` | `Short` | `70.45` | 370,190.00 USD | 4,530.00 USD | 0.00 USD | `+28.97%` | `64.29` |
| `Live` | `Short` | `70.95` | 389,120.00 USD | 18,930.00 USD | 0.00 USD | `+29.88%` | `266.81` |
| `Live` | `Short` | `71.85` | 389,330.00 USD | 205.49 USD | 0.00 USD | `+31.53%` | `2.86` |
| `Live` | `Short` | `72.35` | 389,500.00 USD | 167.13 USD | 0.00 USD | `+32.45%` | `2.31` |
| `Live` | `Short` | `76.35` | 397,880.00 USD | 8,380.00 USD | 0.00 USD | `+39.77%` | `109.80` |
| `Live` | `Short` | `77.85` | 398,480.00 USD | 602.56 USD | 0.00 USD | `+42.51%` | `7.74` |
| `Live` | `Short` | `77.95` | 398,620.00 USD | 136.41 USD | 0.00 USD | `+42.70%` | `1.75` |
| `Live` | `Short` | `79.75` | 399,350.00 USD | 728.12 USD | 0.00 USD | `+45.99%` | `9.13` |
| `Live` | `Short` | `80.75` | 399,990.00 USD | 646.00 USD | 0.00 USD | `+47.82%` | `8.00` |
| `Live` | `Short` | `81.05` | 418,990.00 USD | 19,000.00 USD | 0.00 USD | `+48.37%` | `234.42` |
| `Live` | `Short` | `81.55` | 419,120.00 USD | 123.96 USD | 0.00 USD | `+49.29%` | `1.52` |
| `Live` | `Short` | `82.15` | 422,400.00 USD | 3,290.00 USD | 0.00 USD | `+50.39%` | `40.00` |
| `Live` | `Short` | `82.65` | 426,250.00 USD | 3,850.00 USD | 0.00 USD | `+51.30%` | `46.61` |
| `Live` | `Short` | `82.75` | 426,470.00 USD | 214.32 USD | 0.00 USD | `+51.48%` | `2.59` |
| `Live` | `Short` | `84.65` | 427,330.00 USD | 862.58 USD | 0.00 USD | `+54.96%` | `10.19` |
| `Live` | `Short` | `87.75` | 428,260.00 USD | 932.78 USD | 0.00 USD | `+60.64%` | `10.63` |
| `Live` | `Short` | `91.05` | 431,270.00 USD | 3,000.00 USD | 0.00 USD | `+66.68%` | `33.00` |
| `Live` | `Short` | `95.65` | 431,440.00 USD | 172.17 USD | 0.00 USD | `+75.10%` | `1.80` |
| `Live` | `Short` | `98.15` | 433,890.00 USD | 2,450.00 USD | 0.00 USD | `+79.68%` | `25.00` |
| `Live` | `Short` | `103.65` | 434,600.00 USD | 707.93 USD | 0.00 USD | `+89.74%` | `6.83` |
| `Live` | `Short` | `105.75` | 791,400.00 USD | 356,800.00 USD | 0.00 USD | `+93.59%` | `3,374.01` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 335,070.00 USD | 0.00 USD | 392.18 USD | `-63.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 334,680.00 USD | 0.00 USD | 2,310.00 USD | `-59.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 332,380.00 USD | 0.00 USD | 806.86 USD | `-54.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 331,570.00 USD | 0.00 USD | 1,560.00 USD | `-53.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 330,010.00 USD | 0.00 USD | 410.25 USD | `-49.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 329,600.00 USD | 0.00 USD | 281.57 USD | `-44.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 329,320.00 USD | 0.00 USD | 36,050.00 USD | `-34.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 293,270.00 USD | 0.00 USD | 37,550.00 USD | `-31.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 255,720.00 USD | 0.00 USD | 447.01 USD | `-30.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 255,270.00 USD | 0.00 USD | 40,560.00 USD | `-28.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 214,720.00 USD | 0.00 USD | 489.57 USD | `-27.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 214,230.00 USD | 0.00 USD | 1,550.00 USD | `-26.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 212,670.00 USD | 0.00 USD | 9,500.00 USD | `-26.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 203,170.00 USD | 0.00 USD | 2,060.00 USD | `-25.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 201,110.00 USD | 0.00 USD | 2,960.00 USD | `-23.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 198,160.00 USD | 0.00 USD | 6,050.00 USD | `-23.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 192,110.00 USD | 0.00 USD | 5,680.00 USD | `-21.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 186,430.00 USD | 0.00 USD | 672.22 USD | `-19.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 185,750.00 USD | 0.00 USD | 213.80 USD | `-18.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 185,540.00 USD | 0.00 USD | 223.20 USD | `-18.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 185,320.00 USD | 0.00 USD | 391.13 USD | `-18.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 184,930.00 USD | 0.00 USD | 7,080.00 USD | `-17.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 177,850.00 USD | 0.00 USD | 1,370.00 USD | `-16.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 176,480.00 USD | 0.00 USD | 553.80 USD | `-15.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 175,930.00 USD | 0.00 USD | 14,000.00 USD | `-14.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 161,930.00 USD | 0.00 USD | 158.56 USD | `-13.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 161,770.00 USD | 0.00 USD | 373.28 USD | `-13.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 161,400.00 USD | 0.00 USD | 849.46 USD | `-13.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 160,550.00 USD | 0.00 USD | 1,150.00 USD | `-12.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 159,400.00 USD | 0.00 USD | 1,740.00 USD | `-10.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 157,660.00 USD | 0.00 USD | 981.00 USD | `-10.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.35` | 156,680.00 USD | 0.00 USD | 817.24 USD | `-9.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 155,860.00 USD | 0.00 USD | 1,150.00 USD | `-9.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.55` | 154,710.00 USD | 0.00 USD | 879.51 USD | `-9.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 153,840.00 USD | 0.00 USD | 298.20 USD | `-8.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 153,540.00 USD | 0.00 USD | 14,650.00 USD | `-8.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 138,880.00 USD | 0.00 USD | 6,410.00 USD | `-8.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 132,470.00 USD | 0.00 USD | 459.70 USD | `-7.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 132,010.00 USD | 0.00 USD | 144.57 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 131,870.00 USD | 0.00 USD | 1,020.00 USD | `-6.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 130,840.00 USD | 0.00 USD | 439.89 USD | `-6.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.45` | 130,400.00 USD | 0.00 USD | 204.26 USD | `-5.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 130,200.00 USD | 0.00 USD | 7,320.00 USD | `-5.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.95` | 122,880.00 USD | 0.00 USD | 107.54 USD | `-4.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 122,770.00 USD | 0.00 USD | 27,730.00 USD | `-4.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 95,040.00 USD | 0.00 USD | 51,800.00 USD | `-3.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 43,240.00 USD | 0.00 USD | 10,530.00 USD | `-3.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 32,710.00 USD | 0.00 USD | 271.13 USD | `-3.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 32,440.00 USD | 0.00 USD | 5,050.00 USD | `-3.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 27,390.00 USD | 0.00 USD | 12,330.00 USD | `-2.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 15,060.00 USD | 0.00 USD | 460.81 USD | `-2.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 14,600.00 USD | 0.00 USD | 566.57 USD | `-2.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 14,030.00 USD | 0.00 USD | 5,950.00 USD | `-1.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 8,080.00 USD | 0.00 USD | 1,370.00 USD | `-1.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 6,710.00 USD | 0.00 USD | 462.03 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 6,250.00 USD | 0.00 USD | 746.97 USD | `-1.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 5,510.00 USD | 0.00 USD | 3,090.00 USD | `-0.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 2,420.00 USD | 0.00 USD | 156.53 USD | `-0.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.45` | 2,260.00 USD | 0.00 USD | 570.09 USD | `-0.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.55` | 1,690.00 USD | 0.00 USD | 1,690.00 USD | `-0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `54.65` | 4,110.00 USD | 4,110.00 USD | 0.00 USD | `+0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `54.85` | 37,380.00 USD | 33,280.00 USD | 0.00 USD | `+0.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `54.95` | 38,800.00 USD | 1,410.00 USD | 0.00 USD | `+0.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.05` | 40,370.00 USD | 1,580.00 USD | 0.00 USD | `+0.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.25` | 40,800.00 USD | 429.85 USD | 0.00 USD | `+1.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.35` | 42,940.00 USD | 2,140.00 USD | 0.00 USD | `+1.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.55` | 43,060.00 USD | 113.88 USD | 0.00 USD | `+1.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.65` | 46,670.00 USD | 3,610.00 USD | 0.00 USD | `+1.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.75` | 46,870.00 USD | 202.37 USD | 0.00 USD | `+2.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.85` | 47,070.00 USD | 196.59 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.95` | 47,260.00 USD | 193.03 USD | 0.00 USD | `+2.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.05` | 47,850.00 USD | 587.96 USD | 0.00 USD | `+2.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.15` | 48,040.00 USD | 193.72 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.35` | 48,170.00 USD | 128.48 USD | 0.00 USD | `+3.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.55` | 50,810.00 USD | 2,640.00 USD | 0.00 USD | `+3.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.65` | 50,930.00 USD | 121.23 USD | 0.00 USD | `+3.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.75` | 51,160.00 USD | 228.70 USD | 0.00 USD | `+3.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.85` | 69,190.00 USD | 18,030.00 USD | 0.00 USD | `+4.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.95` | 69,580.00 USD | 390.68 USD | 0.00 USD | `+4.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.05` | 75,380.00 USD | 5,800.00 USD | 0.00 USD | `+4.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.15` | 75,770.00 USD | 392.05 USD | 0.00 USD | `+4.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.25` | 75,970.00 USD | 201.52 USD | 0.00 USD | `+4.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.45` | 76,320.00 USD | 344.70 USD | 0.00 USD | `+5.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.55` | 96,680.00 USD | 20,360.00 USD | 0.00 USD | `+5.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.65` | 96,880.00 USD | 198.89 USD | 0.00 USD | `+5.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.75` | 97,000.00 USD | 119.54 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.95` | 97,120.00 USD | 128.65 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 97,350.00 USD | 230.46 USD | 0.00 USD | `+6.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 97,550.00 USD | 200.04 USD | 0.00 USD | `+6.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 97,760.00 USD | 200.96 USD | 0.00 USD | `+6.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 97,880.00 USD | 123.70 USD | 0.00 USD | `+6.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 98,480.00 USD | 601.45 USD | 0.00 USD | `+7.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 98,880.00 USD | 401.65 USD | 0.00 USD | `+7.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.65` | 99,160.00 USD | 274.48 USD | 0.00 USD | `+7.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 99,280.00 USD | 124.55 USD | 0.00 USD | `+7.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 102,220.00 USD | 2,940.00 USD | 0.00 USD | `+7.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 102,430.00 USD | 203.38 USD | 0.00 USD | `+7.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 107,230.00 USD | 4,800.00 USD | 0.00 USD | `+8.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 108,510.00 USD | 1,280.00 USD | 0.00 USD | `+8.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.25` | 108,810.00 USD | 307.51 USD | 0.00 USD | `+8.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 109,280.00 USD | 461.74 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 109,440.00 USD | 159.92 USD | 0.00 USD | `+8.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.55` | 109,930.00 USD | 496.65 USD | 0.00 USD | `+9.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 110,660.00 USD | 724.75 USD | 0.00 USD | `+9.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.75` | 110,770.00 USD | 113.53 USD | 0.00 USD | `+9.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 110,930.00 USD | 158.00 USD | 0.00 USD | `+9.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.95` | 126,290.00 USD | 15,360.00 USD | 0.00 USD | `+9.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 126,460.00 USD | 171.14 USD | 0.00 USD | `+9.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 127,010.00 USD | 551.00 USD | 0.00 USD | `+10.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.45` | 411,120.00 USD | 284,100.00 USD | 0.00 USD | `+10.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 412,000.00 USD | 878.58 USD | 0.00 USD | `+10.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 413,380.00 USD | 1,390.00 USD | 0.00 USD | `+11.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.75` | 413,790.00 USD | 407.63 USD | 0.00 USD | `+11.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 414,780.00 USD | 986.99 USD | 0.00 USD | `+11.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 415,450.00 USD | 674.72 USD | 0.00 USD | `+11.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 417,810.00 USD | 2,360.00 USD | 0.00 USD | `+11.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 417,940.00 USD | 125.56 USD | 0.00 USD | `+12.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.35` | 418,180.00 USD | 236.20 USD | 0.00 USD | `+12.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 421,770.00 USD | 3,600.00 USD | 0.00 USD | `+12.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 422,420.00 USD | 643.20 USD | 0.00 USD | `+12.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.95` | 424,540.00 USD | 2,120.00 USD | 0.00 USD | `+13.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 424,670.00 USD | 130.31 USD | 0.00 USD | `+13.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.25` | 424,780.00 USD | 117.03 USD | 0.00 USD | `+13.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.45` | 425,000.00 USD | 217.95 USD | 0.00 USD | `+14.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.55` | 425,350.00 USD | 347.15 USD | 0.00 USD | `+14.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 426,070.00 USD | 716.72 USD | 0.00 USD | `+14.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.75` | 426,210.00 USD | 141.19 USD | 0.00 USD | `+14.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 426,440.00 USD | 231.39 USD | 0.00 USD | `+15.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 426,950.00 USD | 508.36 USD | 0.00 USD | `+15.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 427,650.00 USD | 703.97 USD | 0.00 USD | `+15.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.35` | 427,790.00 USD | 140.64 USD | 0.00 USD | `+15.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 428,460.00 USD | 668.13 USD | 0.00 USD | `+16.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 433,010.00 USD | 4,550.00 USD | 0.00 USD | `+16.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 433,560.00 USD | 555.03 USD | 0.00 USD | `+16.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 434,100.00 USD | 531.62 USD | 0.00 USD | `+17.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.45` | 434,940.00 USD | 840.43 USD | 0.00 USD | `+17.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 435,140.00 USD | 202.69 USD | 0.00 USD | `+18.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 435,440.00 USD | 298.04 USD | 0.00 USD | `+18.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 435,540.00 USD | 102.13 USD | 0.00 USD | `+19.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 436,080.00 USD | 540.09 USD | 0.00 USD | `+19.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 436,180.00 USD | 100.79 USD | 0.00 USD | `+19.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 436,440.00 USD | 262.20 USD | 0.00 USD | `+20.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.65` | 436,760.00 USD | 315.12 USD | 0.00 USD | `+20.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 437,130.00 USD | 371.49 USD | 0.00 USD | `+20.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.85` | 438,010.00 USD | 881.07 USD | 0.00 USD | `+20.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 438,710.00 USD | 696.17 USD | 0.00 USD | `+20.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 439,240.00 USD | 534.00 USD | 0.00 USD | `+22.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 450,320.00 USD | 11,080.00 USD | 0.00 USD | `+22.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 463,730.00 USD | 13,410.00 USD | 0.00 USD | `+22.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.05` | 466,090.00 USD | 2,360.00 USD | 0.00 USD | `+24.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 470,950.00 USD | 4,860.00 USD | 0.00 USD | `+25.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 471,160.00 USD | 204.48 USD | 0.00 USD | `+27.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 471,970.00 USD | 810.02 USD | 0.00 USD | `+28.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 791,860.00 USD | 319,890.00 USD | 0.00 USD | `+28.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 792,030.00 USD | 170.04 USD | 0.00 USD | `+29.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 797,800.00 USD | 5,770.00 USD | 0.00 USD | `+29.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 798,070.00 USD | 269.28 USD | 0.00 USD | `+30.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 798,360.00 USD | 291.40 USD | 0.00 USD | `+31.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 805,940.00 USD | 7,580.00 USD | 0.00 USD | `+31.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 806,090.00 USD | 156.78 USD | 0.00 USD | `+32.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 809,310.00 USD | 3,220.00 USD | 0.00 USD | `+33.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 809,730.00 USD | 411.14 USD | 0.00 USD | `+34.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 932,920.00 USD | 123,190.00 USD | 0.00 USD | `+35.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 933,930.00 USD | 1,020.00 USD | 0.00 USD | `+36.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 934,040.00 USD | 104.93 USD | 0.00 USD | `+37.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 934,170.00 USD | 133.59 USD | 0.00 USD | `+37.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 934,570.00 USD | 402.59 USD | 0.00 USD | `+37.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.85` | 934,720.00 USD | 147.15 USD | 0.00 USD | `+38.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 935,040.00 USD | 315.18 USD | 0.00 USD | `+41.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 994,340.00 USD | 59,310.00 USD | 0.00 USD | `+43.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 997,510.00 USD | 3,160.00 USD | 0.00 USD | `+44.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 1,000,000.00 USD | 5,690.00 USD | 0.00 USD | `+45.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 1,040,000.00 USD | 36,590.00 USD | 0.00 USD | `+46.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 1,040,000.00 USD | 433.89 USD | 0.00 USD | `+48.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 1,040,000.00 USD | 172.64 USD | 0.00 USD | `+48.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 1,040,000.00 USD | 164.10 USD | 0.00 USD | `+50.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 1,040,000.00 USD | 546.81 USD | 0.00 USD | `+51.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 1,040,000.00 USD | 2,300.00 USD | 0.00 USD | `+53.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 1,060,000.00 USD | 12,070.00 USD | 0.00 USD | `+55.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.75` | 1,070,000.00 USD | 12,330.00 USD | 0.00 USD | `+56.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.05` | 1,090,000.00 USD | 20,230.00 USD | 0.00 USD | `+59.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.25` | 1,090,000.00 USD | 435.38 USD | 0.00 USD | `+59.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 1,090,000.00 USD | 1,580.00 USD | 0.00 USD | `+61.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 1,130,000.00 USD | 37,000.00 USD | 0.00 USD | `+61.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 1,130,000.00 USD | 473.21 USD | 0.00 USD | `+62.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 1,130,000.00 USD | 1,270.00 USD | 0.00 USD | `+63.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 1,130,000.00 USD | 1,630.00 USD | 0.00 USD | `+63.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 1,150,000.00 USD | 18,740.00 USD | 0.00 USD | `+64.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 1,150,000.00 USD | 481.55 USD | 0.00 USD | `+67.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 1,150,000.00 USD | 1,330.00 USD | 0.00 USD | `+68.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 1,150,000.00 USD | 188.10 USD | 0.00 USD | `+72.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,420,000.00 USD | 266,140.00 USD | 0.00 USD | `+74.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,420,000.00 USD | 3,400.00 USD | 0.00 USD | `+74.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,440,000.00 USD | 21,930.00 USD | 0.00 USD | `+75.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,440,000.00 USD | 294.15 USD | 0.00 USD | `+79.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,450,000.00 USD | 4,010.00 USD | 0.00 USD | `+83.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,450,000.00 USD | 306.15 USD | 0.00 USD | `+86.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,450,000.00 USD | 936.72 USD | 0.00 USD | `+88.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,450,000.00 USD | 2,920.00 USD | 0.00 USD | `+88.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,450,000.00 USD | 324.15 USD | 0.00 USD | `+97.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 1,450,000.00 USD | 123.23 USD | 0.00 USD | `+99.63%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `49.10` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 242.30 USD | 0.00 USD |
| `1D` | `49.20` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 3,260.00 USD | 367.32 USD |
| `1D` | `49.40` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 626.48 USD |
| `7D` | `49.40` | 6,670,000.00 USD | 0.00 USD | 6,670,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD |
| `1D` | `49.50` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 1,180.00 USD | 4,790.00 USD | 13,790.00 USD |
| `7D` | `49.50` | 6,660,000.00 USD | 0.00 USD | 6,660,000.00 USD | 1,130.00 USD | 5,470.00 USD | 0.00 USD |
| `1D` | `49.60` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 785.85 USD | 2,670.00 USD | 0.00 USD |
| `7D` | `49.60` | 6,650,000.00 USD | 0.00 USD | 6,650,000.00 USD | 1,200.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `49.70` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 1,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `49.70` | 6,650,000.00 USD | 0.00 USD | 6,650,000.00 USD | 788.92 USD | 0.00 USD | 4,900.00 USD |
| `1D` | `49.80` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 667.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `49.80` | 6,650,000.00 USD | 0.00 USD | 6,650,000.00 USD | 7,660.00 USD | 8,220.00 USD | 0.00 USD |
| `1D` | `49.90` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 0.00 USD | 2,460.00 USD | 0.00 USD |
| `7D` | `49.90` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 24,600.00 USD | 0.00 USD | 3,950.00 USD |
| `1D` | `50.00` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 11,490.00 USD |
| `7D` | `50.00` | 6,600,000.00 USD | 0.00 USD | 6,600,000.00 USD | 22,100.00 USD | 838.65 USD | 5,340.00 USD |
| `1D` | `50.10` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 0.00 USD | 315.50 USD | 0.00 USD |
| `7D` | `50.10` | 6,570,000.00 USD | 0.00 USD | 6,570,000.00 USD | 363.50 USD | 682.90 USD | 0.00 USD |
| `7D` | `50.20` | 6,570,000.00 USD | 0.00 USD | 6,570,000.00 USD | 6,960.00 USD | 500.40 USD | 0.00 USD |
| `7D` | `50.30` | 6,570,000.00 USD | 0.00 USD | 6,570,000.00 USD | 16,270.00 USD | 3,640.00 USD | 1,950.00 USD |
| `1D` | `50.40` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 349.63 USD | 2,190.00 USD | 0.00 USD |
| `7D` | `50.40` | 6,540,000.00 USD | 0.00 USD | 6,540,000.00 USD | 23,520.00 USD | 19,110.00 USD | 33,450.00 USD |
| `7D` | `50.50` | 6,470,000.00 USD | 0.00 USD | 6,470,000.00 USD | 24,840.00 USD | 6,790.00 USD | 43,710.00 USD |
| `7D` | `50.60` | 6,390,000.00 USD | 0.00 USD | 6,390,000.00 USD | 52,670.00 USD | 17,830.00 USD | 22,250.00 USD |
| `7D` | `50.70` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 53,670.00 USD | 24,710.00 USD | 32,520.00 USD |
| `1D` | `50.80` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 5,630.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `50.80` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD |
| `1D` | `50.90` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 260.05 USD | 8,390.00 USD |
| `7D` | `50.90` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD |
| `1D` | `51.00` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 129.78 USD |
| `7D` | `51.00` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `51.10` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 263.90 USD | 1,160.00 USD | 0.00 USD |
| `7D` | `51.10` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD |
| `1D` | `51.20` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 1,100.00 USD | 1,130.00 USD | 327.72 USD |
| `7D` | `51.20` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD |
| `1D` | `51.30` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 20,430.00 USD | 5,150.00 USD | 18,640.00 USD |
| `7D` | `51.30` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 19,510.00 USD | 12,490.00 USD | 47,090.00 USD |
| `1D` | `51.40` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 17,510.00 USD | 7,090.00 USD | 10,780.00 USD |
| `7D` | `51.40` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 71,090.00 USD | 28,960.00 USD | 45,150.00 USD |
| `1D` | `51.50` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 10,410.00 USD | 8,980.00 USD | 4,080.00 USD |
| `7D` | `51.50` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `51.60` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 8,800.00 USD | 7,990.00 USD | 4,820.00 USD |
| `7D` | `51.60` | 5,250,000.00 USD | 0.00 USD | 5,250,000.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD |
| `1D` | `51.70` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 3,490.00 USD | 4,150.00 USD | 6,480.00 USD |
| `7D` | `51.70` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `51.80` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 12,210.00 USD | 2,080.00 USD | 10,050.00 USD |
| `7D` | `51.80` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD |
| `1D` | `51.90` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 12,520.00 USD | 21,470.00 USD | 9,190.00 USD |
| `7D` | `51.90` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 5,870.00 USD | 15,810.00 USD | 4,760.00 USD |
| `1D` | `52.00` | 968,990.00 USD | 0.00 USD | 968,990.00 USD | 25,150.00 USD | 8,230.00 USD | 23,340.00 USD |
| `7D` | `52.00` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 64,300.00 USD | 20,800.00 USD | 11,880.00 USD |
| `1D` | `52.10` | 912,270.00 USD | 0.00 USD | 912,270.00 USD | 27,630.00 USD | 5,780.00 USD | 35,220.00 USD |
| `7D` | `52.10` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 24,220.00 USD | 18,810.00 USD | 35,480.00 USD |
| `1D` | `52.20` | 843,640.00 USD | 0.00 USD | 843,640.00 USD | 20,520.00 USD | 10,450.00 USD | 14,390.00 USD |
| `7D` | `52.20` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 38,380.00 USD | 4,340.00 USD | 25,270.00 USD |
| `1D` | `52.30` | 798,280.00 USD | 0.00 USD | 798,280.00 USD | 38,870.00 USD | 8,170.00 USD | 16,110.00 USD |
| `7D` | `52.30` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 18,740.00 USD | 12,840.00 USD | 8,940.00 USD |
| `1D` | `52.40` | 735,130.00 USD | 0.00 USD | 735,130.00 USD | 10,040.00 USD | 7,510.00 USD | 6,280.00 USD |
| `7D` | `52.40` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 20,580.00 USD | 11,230.00 USD | 20,050.00 USD |
| `1D` | `52.50` | 711,290.00 USD | 0.00 USD | 711,290.00 USD | 15,070.00 USD | 13,510.00 USD | 998.32 USD |
| `7D` | `52.50` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 33,240.00 USD | 667.05 USD | 10,640.00 USD |
| `1D` | `52.60` | 681,710.00 USD | 0.00 USD | 681,710.00 USD | 2,760.00 USD | 8,750.00 USD | 273.52 USD |
| `7D` | `52.60` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 36,640.00 USD | 14,530.00 USD | 584.77 USD |
| `1D` | `52.70` | 669,920.00 USD | 0.00 USD | 669,920.00 USD | 4,930.00 USD | 7,610.00 USD | 15,080.00 USD |
| `7D` | `52.70` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 20,250.00 USD | 43,820.00 USD | 62,360.00 USD |
| `1D` | `52.80` | 642,300.00 USD | 0.00 USD | 642,300.00 USD | 14,400.00 USD | 14,660.00 USD | 60,330.00 USD |
| `7D` | `52.80` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 46,600.00 USD | 27,850.00 USD | 108.50 USD |
| `1D` | `52.90` | 552,910.00 USD | 0.00 USD | 552,910.00 USD | 28,000.00 USD | 7,150.00 USD | 6,120.00 USD |
| `7D` | `52.90` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 51,920.00 USD | 23,030.00 USD | 3,870.00 USD |
| `1D` | `53.00` | 511,640.00 USD | 0.00 USD | 511,640.00 USD | 4,280.00 USD | 1,860.00 USD | 936.80 USD |
| `7D` | `53.00` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 18,990.00 USD | 8,880.00 USD | 32,670.00 USD |
| `1D` | `53.10` | 504,580.00 USD | 0.00 USD | 504,580.00 USD | 3,280.00 USD | 2,540.00 USD | 669.73 USD |
| `7D` | `53.10` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 52,760.00 USD | 29,200.00 USD | 9,860.00 USD |
| `1D` | `53.20` | 498,090.00 USD | 0.00 USD | 498,090.00 USD | 9,780.00 USD | 13,340.00 USD | 6,370.00 USD |
| `7D` | `53.20` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 90,340.00 USD | 17,580.00 USD | 25,530.00 USD |
| `1D` | `53.30` | 468,610.00 USD | 0.00 USD | 468,610.00 USD | 17,240.00 USD | 4,110.00 USD | 36,250.00 USD |
| `7D` | `53.30` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 63,050.00 USD | 14,250.00 USD | 37,140.00 USD |
| `1D` | `53.40` | 411,010.00 USD | 0.00 USD | 411,010.00 USD | 13,040.00 USD | 3,050.00 USD | 4,930.00 USD |
| `7D` | `53.40` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 48,760.00 USD | 4,350.00 USD | 48,020.00 USD |
| `1D` | `53.50` | 389,990.00 USD | 0.00 USD | 389,990.00 USD | 8,970.00 USD | 4,350.00 USD | 0.00 USD |
| `7D` | `53.50` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 49,490.00 USD | 11,660.00 USD | 22,130.00 USD |
| `1D` | `53.60` | 376,670.00 USD | 0.00 USD | 376,670.00 USD | 12,620.00 USD | 21,080.00 USD | 8,310.00 USD |
| `7D` | `53.60` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 53,580.00 USD | 6,140.00 USD | 10,670.00 USD |
| `1D` | `53.70` | 334,660.00 USD | 0.00 USD | 334,660.00 USD | 5,710.00 USD | 1,100.00 USD | 0.00 USD |
| `7D` | `53.70` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 64,150.00 USD | 16,400.00 USD | 12,890.00 USD |
| `1D` | `53.80` | 327,840.00 USD | 0.00 USD | 327,840.00 USD | 1,830.00 USD | 5,480.00 USD | 3,130.00 USD |
| `7D` | `53.80` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 99,150.00 USD | 80,510.00 USD | 126,140.00 USD |
| `1D` | `53.90` | 317,400.00 USD | 0.00 USD | 317,400.00 USD | 7,480.00 USD | 23,960.00 USD | 98,250.00 USD |
| `7D` | `53.90` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 111,970.00 USD | 52,650.00 USD | 123,850.00 USD |
| `1D` | `54.00` | 187,710.00 USD | 0.00 USD | 187,710.00 USD | 4,010.00 USD | 13,640.00 USD | 0.00 USD |
| `7D` | `54.00` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 344,710.00 USD | 142,130.00 USD | 210,440.00 USD |
| `1D` | `54.10` | 170,070.00 USD | 0.00 USD | 170,070.00 USD | 23,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.10` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 234,120.00 USD | 45,470.00 USD | 138,110.00 USD |
| `1D` | `54.20` | 146,240.00 USD | 0.00 USD | 146,240.00 USD | 14,960.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.20` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 234,980.00 USD | 141,240.00 USD | 128,910.00 USD |
| `1D` | `54.30` | 131,280.00 USD | 0.00 USD | 131,280.00 USD | 9,970.00 USD | 12,300.00 USD | 28,640.00 USD |
| `7D` | `54.30` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 237,140.00 USD | 89,820.00 USD | 181,420.00 USD |
| `1D` | `54.40` | 80,370.00 USD | 0.00 USD | 80,370.00 USD | 17,060.00 USD | 0.00 USD | 57,760.00 USD |
| `7D` | `54.40` | 882,110.00 USD | 0.00 USD | 882,110.00 USD | 304,270.00 USD | 6,020.00 USD | 92,140.00 USD |
| `1D` | `54.50` | 5,550.00 USD | 0.00 USD | 5,550.00 USD | 3,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.50` | 479,680.00 USD | 0.00 USD | 479,680.00 USD | 159,720.00 USD | 8,200.00 USD | 140,930.00 USD |
| `1D` | `54.60` | 2,510.00 USD | 0.00 USD | 2,510.00 USD | 2,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.60` | 170,830.00 USD | 0.00 USD | 170,830.00 USD | 98,430.00 USD | 0.00 USD | 72,400.00 USD |
| `1D` | `54.70` | 117,110.00 USD | 117,110.00 USD | 0.00 USD | 60,000.00 USD | 0.00 USD | 57,100.00 USD |
| `1D` | `54.70` | 234,210.00 USD | 234,210.00 USD | 0.00 USD | 60,000.00 USD | 0.00 USD | 57,100.00 USD |
| `7D` | `54.70` | 118,580.00 USD | 118,580.00 USD | 0.00 USD | 118,580.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.70` | 237,150.00 USD | 237,150.00 USD | 0.00 USD | 118,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `54.80` | 278,340.00 USD | 278,340.00 USD | 0.00 USD | 44,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.80` | 529,770.00 USD | 529,770.00 USD | 0.00 USD | 292,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `54.90` | 324,430.00 USD | 324,430.00 USD | 0.00 USD | 46,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.90` | 771,510.00 USD | 771,510.00 USD | 0.00 USD | 241,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `55.00` | 359,160.00 USD | 359,160.00 USD | 0.00 USD | 34,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.00` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 255,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `55.10` | 375,790.00 USD | 375,790.00 USD | 0.00 USD | 16,450.00 USD | 0.00 USD | 189.61 USD |
| `7D` | `55.10` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 348,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `55.20` | 387,310.00 USD | 387,310.00 USD | 0.00 USD | 11,100.00 USD | 0.00 USD | 420.67 USD |
| `7D` | `55.20` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 336,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `55.30` | 463,770.00 USD | 463,770.00 USD | 0.00 USD | 52,250.00 USD | 0.00 USD | 24,210.00 USD |
| `7D` | `55.30` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 359,480.00 USD | 17,490.00 USD | 187,300.00 USD |
| `7D` | `55.40` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 300,790.00 USD | 0.00 USD | 238,510.00 USD |
| `1D` | `55.50` | 491,100.00 USD | 491,100.00 USD | 0.00 USD | 0.00 USD | 27,320.00 USD | 0.00 USD |
| `7D` | `55.50` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 326,800.00 USD | 167,870.00 USD | 385,110.00 USD |
| `1D` | `55.60` | 512,340.00 USD | 512,340.00 USD | 0.00 USD | 755.00 USD | 20,490.00 USD | 0.00 USD |
| `7D` | `55.60` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 426,340.00 USD | 245,070.00 USD | 248,650.00 USD |
| `1D` | `55.70` | 548,540.00 USD | 548,540.00 USD | 0.00 USD | 0.00 USD | 35,800.00 USD | 407.86 USD |
| `7D` | `55.70` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 174,240.00 USD | 32,180.00 USD | 269,560.00 USD |
| `1D` | `55.80` | 734,290.00 USD | 734,290.00 USD | 0.00 USD | 122,760.00 USD | 16,300.00 USD | 46,680.00 USD |
| `7D` | `55.80` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 60,840.00 USD | 28,930.00 USD | 142,890.00 USD |
| `1D` | `55.90` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 137,200.00 USD | 1,100.00 USD | 139,640.00 USD |
| `7D` | `55.90` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 65,400.00 USD | 65,840.00 USD | 234,280.00 USD |
| `1D` | `56.00` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 124,870.00 USD | 0.00 USD | 59,430.00 USD |
| `7D` | `56.00` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 181,230.00 USD | 98,600.00 USD | 147,270.00 USD |
| `1D` | `56.10` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 105,950.00 USD | 23,960.00 USD | 146,900.00 USD |
| `7D` | `56.10` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 121,920.00 USD | 140,020.00 USD | 61,210.00 USD |
| `1D` | `56.20` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 72,300.00 USD | 73,200.00 USD | 71,790.00 USD |
| `7D` | `56.20` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 104,510.00 USD | 66,120.00 USD | 179,680.00 USD |
| `1D` | `56.30` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 464.20 USD | 31,280.00 USD | 36,880.00 USD |
| `7D` | `56.30` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 91,850.00 USD | 128,970.00 USD | 85,420.00 USD |
| `1D` | `56.40` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 579.50 USD | 30,930.00 USD | 117,360.00 USD |
| `7D` | `56.40` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 215,940.00 USD | 102,460.00 USD | 137,070.00 USD |
| `1D` | `56.50` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 118,430.00 USD | 0.00 USD |
| `7D` | `56.50` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 26,520.00 USD | 83,470.00 USD | 0.00 USD |
| `1D` | `56.60` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 13,870.00 USD | 58,070.00 USD | 57,440.00 USD |
| `7D` | `56.60` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 363,190.00 USD | 119,150.00 USD | 0.00 USD |
| `1D` | `56.70` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 197,080.00 USD | 0.00 USD | 201,730.00 USD |
| `7D` | `56.70` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 110,940.00 USD | 92,780.00 USD | 0.00 USD |
| `1D` | `56.80` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 180,420.00 USD | 2,180.00 USD | 113,990.00 USD |
| `7D` | `56.80` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 153,580.00 USD | 90,850.00 USD | 261,330.00 USD |
| `1D` | `56.90` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 8,150.00 USD | 1,780.00 USD |
| `7D` | `56.90` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 108,440.00 USD | 48,600.00 USD | 92,630.00 USD |
| `1D` | `57.00` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 552.05 USD | 427.23 USD |
| `7D` | `57.00` | 9,250,000.00 USD | 9,250,000.00 USD | 0.00 USD | 50,710.00 USD | 2,620.00 USD | 93,100.00 USD |
| `1D` | `57.10` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 10,960.00 USD | 5,950.00 USD |
| `7D` | `57.10` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 36,580.00 USD | 16,110.00 USD | 20,440.00 USD |
| `1D` | `57.20` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 11,980.00 USD | 49,380.00 USD |
| `7D` | `57.20` | 9,360,000.00 USD | 9,360,000.00 USD | 0.00 USD | 21,160.00 USD | 13,670.00 USD | 3,700.00 USD |
| `1D` | `57.30` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 7,220.00 USD | 386.57 USD |
| `7D` | `57.30` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 22,360.00 USD | 0.00 USD | 3,710.00 USD |
| `1D` | `57.40` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 19,650.00 USD | 25,750.00 USD | 0.00 USD |
| `7D` | `57.40` | 9,590,000.00 USD | 9,590,000.00 USD | 0.00 USD | 38,520.00 USD | 30,000.00 USD | 129,940.00 USD |
| `1D` | `57.50` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 108,670.00 USD | 12,870.00 USD | 36,450.00 USD |
| `7D` | `57.50` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 76,670.00 USD | 23,070.00 USD | 0.00 USD |
| `1D` | `57.60` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 6,150.00 USD | 0.00 USD |
| `7D` | `57.60` | 9,800,000.00 USD | 9,800,000.00 USD | 0.00 USD | 72,680.00 USD | 15,090.00 USD | 26,440.00 USD |
| `1D` | `57.70` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 17,800.00 USD | 1,300.00 USD | 85,990.00 USD |
| `7D` | `57.70` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 0.00 USD | 1,500.00 USD | 57,330.00 USD |
| `1D` | `57.80` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 2,360.00 USD | 0.00 USD | 648.90 USD |
| `7D` | `57.80` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 2,260.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `57.90` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 1,570.00 USD | 6,570.00 USD | 0.00 USD |
| `7D` | `57.90` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `58.00` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 2,170.00 USD | 5,650.00 USD | 0.00 USD |
| `7D` | `58.00` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD | 3,670.00 USD | 0.00 USD |
| `1D` | `58.10` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 29,450.00 USD | 1,180.00 USD | 9,350.00 USD |
| `7D` | `58.10` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD | 848.40 USD |
| `1D` | `58.20` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 5,880.00 USD | 350.42 USD |
| `1D` | `58.30` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 8,940.00 USD | 11,540.00 USD | 36,830.00 USD |
| `7D` | `58.30` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 0.00 USD | 9,580.00 USD | 26,820.00 USD |
| `1D` | `58.40` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 4,990.00 USD | 33,950.00 USD |
| `7D` | `58.40` | 9,960,000.00 USD | 9,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 54,120.00 USD |
| `1D` | `58.50` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 48,820.00 USD | 21,280.00 USD | 379.22 USD |
| `7D` | `58.50` | 9,990,000.00 USD | 9,990,000.00 USD | 0.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD |
| `7D` | `58.60` | 9,990,000.00 USD | 9,990,000.00 USD | 0.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `58.70` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 15,850.00 USD | 8,070.00 USD | 355.85 USD |
| `7D` | `58.70` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 1,700.00 USD | 5,910.00 USD | 35,320.00 USD |
| `1D` | `58.80` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 35,140.00 USD | 14,730.00 USD | 23,630.00 USD |
| `7D` | `58.80` | 10,040,000.00 USD | 10,040,000.00 USD | 0.00 USD | 1,810.00 USD | 3,320.00 USD | 6,410.00 USD |
| `1D` | `58.90` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 18,240.00 USD | 124,640.00 USD | 91,310.00 USD |
| `7D` | `58.90` | 10,170,000.00 USD | 10,170,000.00 USD | 0.00 USD | 0.00 USD | 48,700.00 USD | 83,500.00 USD |
| `1D` | `59.00` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 151,460.00 USD | 57,070.00 USD | 134,010.00 USD |
| `7D` | `59.00` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 255,180.00 USD | 65,270.00 USD | 118,570.00 USD |
| `1D` | `59.10` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 189,650.00 USD | 49,050.00 USD | 186,370.00 USD |
| `7D` | `59.10` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 91,060.00 USD | 45,400.00 USD | 158,780.00 USD |
| `1D` | `59.20` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 158,420.00 USD | 75,700.00 USD | 96,020.00 USD |
| `7D` | `59.20` | 11,250,000.00 USD | 11,250,000.00 USD | 0.00 USD | 153,580.00 USD | 12,460.00 USD | 174,600.00 USD |
| `1D` | `59.30` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 306,360.00 USD | 73,680.00 USD | 143,250.00 USD |
| `7D` | `59.30` | 11,530,000.00 USD | 11,530,000.00 USD | 0.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD |
| `1D` | `59.40` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 78,510.00 USD | 57,010.00 USD | 76,960.00 USD |
| `7D` | `59.40` | 11,840,000.00 USD | 11,840,000.00 USD | 0.00 USD | 103,370.00 USD | 73,620.00 USD | 137,500.00 USD |
| `1D` | `59.50` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 119,350.00 USD | 57,690.00 USD | 28,370.00 USD |
| `7D` | `59.50` | 11,990,000.00 USD | 11,990,000.00 USD | 0.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD |
| `1D` | `59.60` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 62,780.00 USD | 68,870.00 USD | 18,340.00 USD |
| `7D` | `59.60` | 12,490,000.00 USD | 12,490,000.00 USD | 0.00 USD | 268,680.00 USD | 145,550.00 USD | 86,840.00 USD |
| `1D` | `59.70` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 20,820.00 USD | 30,890.00 USD | 94,130.00 USD |
| `7D` | `59.70` | 12,890,000.00 USD | 12,890,000.00 USD | 0.00 USD | 55,510.00 USD | 180,620.00 USD | 161,880.00 USD |
| `1D` | `59.80` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 40,970.00 USD | 37,360.00 USD | 10,870.00 USD |
| `7D` | `59.80` | 13,260,000.00 USD | 13,260,000.00 USD | 0.00 USD | 118,240.00 USD | 97,600.00 USD | 155,270.00 USD |
| `1D` | `59.90` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 112,870.00 USD | 21,300.00 USD | 80,370.00 USD |
| `7D` | `59.90` | 13,630,000.00 USD | 13,630,000.00 USD | 0.00 USD | 246,770.00 USD | 84,430.00 USD | 40,130.00 USD |
| `1D` | `60.00` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 182,880.00 USD | 64,320.00 USD | 69,570.00 USD |
| `7D` | `60.00` | 14,140,000.00 USD | 14,140,000.00 USD | 0.00 USD | 231,370.00 USD | 183,130.00 USD | 94,160.00 USD |
| `1D` | `60.10` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 95,780.00 USD | 40,300.00 USD | 71,530.00 USD |
| `7D` | `60.10` | 14,710,000.00 USD | 14,710,000.00 USD | 0.00 USD | 263,890.00 USD | 129,860.00 USD | 174,140.00 USD |
| `1D` | `60.20` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 105,780.00 USD | 41,350.00 USD | 96,900.00 USD |
| `7D` | `60.20` | 15,210,000.00 USD | 15,210,000.00 USD | 0.00 USD | 207,990.00 USD | 131,530.00 USD | 157,150.00 USD |
| `1D` | `60.30` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 97,720.00 USD | 76,060.00 USD | 83,130.00 USD |
| `7D` | `60.30` | 15,580,000.00 USD | 15,580,000.00 USD | 0.00 USD | 118,160.00 USD | 95,890.00 USD | 155,610.00 USD |
| `1D` | `60.40` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 168,700.00 USD | 54,240.00 USD | 84,380.00 USD |
| `7D` | `60.40` | 16,030,000.00 USD | 16,030,000.00 USD | 0.00 USD | 93,890.00 USD | 133,310.00 USD | 226,940.00 USD |
| `1D` | `60.50` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 79,160.00 USD | 43,330.00 USD | 63,520.00 USD |
| `7D` | `60.50` | 16,470,000.00 USD | 16,470,000.00 USD | 0.00 USD | 147,230.00 USD | 88,570.00 USD | 207,100.00 USD |
| `1D` | `60.60` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 80,330.00 USD | 34,850.00 USD | 5,340.00 USD |
| `7D` | `60.60` | 16,990,000.00 USD | 16,990,000.00 USD | 0.00 USD | 266,850.00 USD | 98,770.00 USD | 155,390.00 USD |
| `1D` | `60.70` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 74,340.00 USD | 45,070.00 USD | 33,070.00 USD |
| `7D` | `60.70` | 17,220,000.00 USD | 17,220,000.00 USD | 0.00 USD | 129,660.00 USD | 67,510.00 USD | 28,990.00 USD |
| `1D` | `60.80` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 22,530.00 USD | 11,950.00 USD | 43,340.00 USD |
| `7D` | `60.80` | 17,450,000.00 USD | 17,450,000.00 USD | 0.00 USD | 54,870.00 USD | 78,710.00 USD | 94,850.00 USD |
| `1D` | `60.90` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 40,050.00 USD | 21,020.00 USD | 0.00 USD |
| `7D` | `60.90` | 17,730,000.00 USD | 17,730,000.00 USD | 0.00 USD | 139,720.00 USD | 52,860.00 USD | 92,420.00 USD |
| `1D` | `61.00` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 46,000.00 USD | 6,970.00 USD | 28,080.00 USD |
| `7D` | `61.00` | 17,870,000.00 USD | 17,870,000.00 USD | 0.00 USD | 96,160.00 USD | 36,500.00 USD | 5,370.00 USD |
| `1D` | `61.10` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 6,110.00 USD | 0.00 USD | 11,490.00 USD |
| `7D` | `61.10` | 17,900,000.00 USD | 17,900,000.00 USD | 0.00 USD | 31,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `61.20` | 8,590,000.00 USD | 8,590,000.00 USD | 0.00 USD | 75,930.00 USD | 1,160.00 USD | 19,110.00 USD |
| `7D` | `61.20` | 18,120,000.00 USD | 18,120,000.00 USD | 0.00 USD | 116,610.00 USD | 70,180.00 USD | 33,350.00 USD |
| `1D` | `61.30` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 9,540.00 USD | 6,080.00 USD | 2,340.00 USD |
| `7D` | `61.30` | 18,270,000.00 USD | 18,270,000.00 USD | 0.00 USD | 51,130.00 USD | 35,650.00 USD | 55,130.00 USD |
| `1D` | `61.40` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 6,350.00 USD | 7,530.00 USD | 1,670.00 USD |
| `7D` | `61.40` | 18,420,000.00 USD | 18,420,000.00 USD | 0.00 USD | 89,350.00 USD | 41,800.00 USD | 24,650.00 USD |
| `1D` | `61.50` | 8,670,000.00 USD | 8,670,000.00 USD | 0.00 USD | 9,120.00 USD | 19,960.00 USD | 17,790.00 USD |
| `7D` | `61.50` | 18,510,000.00 USD | 18,510,000.00 USD | 0.00 USD | 19,810.00 USD | 35,300.00 USD | 36,110.00 USD |
| `1D` | `61.60` | 8,730,000.00 USD | 8,730,000.00 USD | 0.00 USD | 24,180.00 USD | 14,990.00 USD | 20,400.00 USD |
| `7D` | `61.60` | 18,760,000.00 USD | 18,760,000.00 USD | 0.00 USD | 54,240.00 USD | 63,390.00 USD | 132,550.00 USD |
| `1D` | `61.70` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 37,720.00 USD | 9,670.00 USD | 12,390.00 USD |
| `7D` | `61.70` | 18,980,000.00 USD | 18,980,000.00 USD | 0.00 USD | 91,980.00 USD | 12,880.00 USD | 114,850.00 USD |
| `1D` | `61.80` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 23,640.00 USD | 8,420.00 USD | 1,570.00 USD |
| `7D` | `61.80` | 19,300,000.00 USD | 19,300,000.00 USD | 0.00 USD | 167,990.00 USD | 62,660.00 USD | 86,520.00 USD |
| `1D` | `61.90` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 28,490.00 USD | 11,940.00 USD | 16,200.00 USD |
| `7D` | `61.90` | 19,440,000.00 USD | 19,440,000.00 USD | 0.00 USD | 72,380.00 USD | 29,730.00 USD | 35,860.00 USD |
| `1D` | `62.00` | 8,900,000.00 USD | 8,900,000.00 USD | 0.00 USD | 14,630.00 USD | 911.46 USD | 2,750.00 USD |
| `7D` | `62.00` | 19,560,000.00 USD | 19,560,000.00 USD | 0.00 USD | 56,450.00 USD | 13,260.00 USD | 49,920.00 USD |
| `1D` | `62.10` | 8,910,000.00 USD | 8,910,000.00 USD | 0.00 USD | 12,050.00 USD | 945.47 USD | 0.00 USD |
| `7D` | `62.10` | 19,620,000.00 USD | 19,620,000.00 USD | 0.00 USD | 36,500.00 USD | 12,820.00 USD | 13,950.00 USD |
| `1D` | `62.20` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 3,350.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.20` | 19,740,000.00 USD | 19,740,000.00 USD | 0.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD |
| `1D` | `62.30` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 464.20 USD | 260.05 USD | 8,390.00 USD |
| `7D` | `62.30` | 19,890,000.00 USD | 19,890,000.00 USD | 0.00 USD | 35,280.00 USD | 23,450.00 USD | 97,450.00 USD |
| `1D` | `62.40` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 1,150.00 USD | 0.00 USD | 129.78 USD |
| `7D` | `62.40` | 20,030,000.00 USD | 20,030,000.00 USD | 0.00 USD | 79,620.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `62.50` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 263.90 USD | 1,160.00 USD | 0.00 USD |
| `7D` | `62.50` | 20,120,000.00 USD | 20,120,000.00 USD | 0.00 USD | 44,300.00 USD | 14,320.00 USD | 26,610.00 USD |
| `1D` | `62.60` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 1,100.00 USD | 1,130.00 USD | 327.72 USD |
| `7D` | `62.60` | 20,190,000.00 USD | 20,190,000.00 USD | 0.00 USD | 34,910.00 USD | 7,830.00 USD | 27,730.00 USD |
| `1D` | `62.70` | 8,970,000.00 USD | 8,970,000.00 USD | 0.00 USD | 19,390.00 USD | 5,150.00 USD | 18,640.00 USD |
| `7D` | `62.70` | 20,270,000.00 USD | 20,270,000.00 USD | 0.00 USD | 22,020.00 USD | 12,490.00 USD | 47,090.00 USD |
| `1D` | `62.80` | 9,010,000.00 USD | 9,010,000.00 USD | 0.00 USD | 16,430.00 USD | 7,090.00 USD | 10,780.00 USD |
| `7D` | `62.80` | 20,410,000.00 USD | 20,410,000.00 USD | 0.00 USD | 72,250.00 USD | 28,960.00 USD | 45,150.00 USD |
| `1D` | `62.90` | 9,030,000.00 USD | 9,030,000.00 USD | 0.00 USD | 8,780.00 USD | 8,980.00 USD | 4,080.00 USD |
| `7D` | `62.90` | 20,510,000.00 USD | 20,510,000.00 USD | 0.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `63.00` | 9,050,000.00 USD | 9,050,000.00 USD | 0.00 USD | 7,800.00 USD | 7,990.00 USD | 4,820.00 USD |
| `7D` | `63.00` | 20,570,000.00 USD | 20,570,000.00 USD | 0.00 USD | 34,730.00 USD | 12,240.00 USD | 17,650.00 USD |
| `1D` | `63.10` | 9,060,000.00 USD | 9,060,000.00 USD | 0.00 USD | 4,260.00 USD | 4,150.00 USD | 6,480.00 USD |
| `7D` | `63.10` | 20,610,000.00 USD | 20,610,000.00 USD | 0.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `63.20` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 2,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `63.30` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 4,590.00 USD | 594.25 USD | 2,790.00 USD |
| `7D` | `63.30` | 20,650,000.00 USD | 20,650,000.00 USD | 0.00 USD | 19,680.00 USD | 11,500.00 USD | 9,730.00 USD |
| `1D` | `63.40` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 8,400.00 USD | 1,480.00 USD | 7,260.00 USD |
| `7D` | `63.40` | 20,680,000.00 USD | 20,680,000.00 USD | 0.00 USD | 13,220.00 USD | 1,320.00 USD | 9,960.00 USD |
| `1D` | `63.50` | 9,130,000.00 USD | 9,130,000.00 USD | 0.00 USD | 12,520.00 USD | 21,470.00 USD | 9,190.00 USD |
| `7D` | `63.50` | 20,700,000.00 USD | 20,700,000.00 USD | 0.00 USD | 6,620.00 USD | 15,810.00 USD | 4,760.00 USD |
| `1D` | `63.60` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 25,150.00 USD | 8,230.00 USD | 23,340.00 USD |
| `7D` | `63.60` | 20,800,000.00 USD | 20,800,000.00 USD | 0.00 USD | 63,480.00 USD | 20,800.00 USD | 11,880.00 USD |
| `1D` | `63.70` | 9,260,000.00 USD | 9,260,000.00 USD | 0.00 USD | 27,630.00 USD | 5,780.00 USD | 35,220.00 USD |
| `7D` | `63.70` | 20,870,000.00 USD | 20,870,000.00 USD | 0.00 USD | 21,940.00 USD | 18,810.00 USD | 35,480.00 USD |
| `1D` | `63.80` | 9,300,000.00 USD | 9,300,000.00 USD | 0.00 USD | 19,730.00 USD | 10,450.00 USD | 14,390.00 USD |
| `7D` | `63.80` | 20,940,000.00 USD | 20,940,000.00 USD | 0.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD |
| `1D` | `63.90` | 9,360,000.00 USD | 9,360,000.00 USD | 0.00 USD | 34,930.00 USD | 8,170.00 USD | 16,110.00 USD |
| `7D` | `63.90` | 20,970,000.00 USD | 20,970,000.00 USD | 0.00 USD | 7,650.00 USD | 12,840.00 USD | 8,940.00 USD |
| `1D` | `64.00` | 9,380,000.00 USD | 9,380,000.00 USD | 0.00 USD | 7,880.00 USD | 6,900.00 USD | 6,280.00 USD |
| `7D` | `64.00` | 21,010,000.00 USD | 21,010,000.00 USD | 0.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD |
| `1D` | `64.10` | 9,400,000.00 USD | 9,400,000.00 USD | 0.00 USD | 13,740.00 USD | 5,360.00 USD | 80.02 USD |
| `7D` | `64.10` | 21,040,000.00 USD | 21,040,000.00 USD | 0.00 USD | 20,350.00 USD | 667.05 USD | 10,640.00 USD |
| `1D` | `64.20` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 2,760.00 USD | 8,200.00 USD | 273.52 USD |
| `7D` | `64.20` | 21,090,000.00 USD | 21,090,000.00 USD | 0.00 USD | 28,840.00 USD | 14,530.00 USD | 584.77 USD |
| `1D` | `64.40` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 0.00 USD | 946.37 USD | 13,440.00 USD |
| `7D` | `64.40` | 21,140,000.00 USD | 21,140,000.00 USD | 0.00 USD | 2,540.00 USD | 20,590.00 USD | 29,110.00 USD |
| `7D` | `64.50` | 21,170,000.00 USD | 21,170,000.00 USD | 0.00 USD | 7,700.00 USD | 7,120.00 USD | 13,310.00 USD |
| `7D` | `64.60` | 21,210,000.00 USD | 21,210,000.00 USD | 0.00 USD | 32,220.00 USD | 14,180.00 USD | 108.50 USD |
| `7D` | `64.70` | 21,280,000.00 USD | 21,280,000.00 USD | 0.00 USD | 39,430.00 USD | 23,030.00 USD | 3,870.00 USD |
| `7D` | `64.80` | 21,320,000.00 USD | 21,320,000.00 USD | 0.00 USD | 7,540.00 USD | 8,210.00 USD | 20,430.00 USD |
| `7D` | `64.90` | 21,360,000.00 USD | 21,360,000.00 USD | 0.00 USD | 25,320.00 USD | 8,010.00 USD | 9,860.00 USD |
| `7D` | `65.00` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 1,790.00 USD | 9,480.00 USD | 13,480.00 USD |
| `7D` | `65.10` | 21,440,000.00 USD | 21,440,000.00 USD | 0.00 USD | 5,810.00 USD | 14,250.00 USD | 37,140.00 USD |
| `7D` | `65.20` | 21,480,000.00 USD | 21,480,000.00 USD | 0.00 USD | 10,380.00 USD | 2,250.00 USD | 28,420.00 USD |
| `7D` | `65.30` | 21,530,000.00 USD | 21,530,000.00 USD | 0.00 USD | 22,330.00 USD | 9,180.00 USD | 22,130.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `414.45M` | Total OI Tokens: `7,569,977.2 LTC`
  * 1h OI Change: `-8.04%` | 4h OI Change: `-9.33%` | 24h OI Change: `-11.03%`
  * Exchange Breakdown: Binance=`75.82M` | Bybit=`64.77M` | OKX=`33.29M` | Hyperliquid=`21.37M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `13.43K` | Last 24h: `36.85K` | Last 3d: `60.07K` | Last 7d: `106.71K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0098%` | **USDT OKX** | `0.0022%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0073%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0060%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `45.54%` | `54.46%` | `0.84` | 42,950,000.00 USD |
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
| `1H` | `LTC` | `44.22%` | `55.78%` | `0.79` | 69,130,000.00 USD |
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
| `4H` | `LTC` | `45.19%` | `54.81%` | `0.82` | 93,360,000.00 USD |
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
| `5:00 UTC` | `57.59` | `57.70` | `57.59` | `57.88` | `57.55` | 407,665.08 USD | 260,874.04 USD | 146,791.04 USD | 114,082.99 USD | `+27.98%` | `15B / 1S` |
| `0:00 UTC` | `57.56` | `57.61` | `57.56` | `57.77` | `57.55` | 421,492.76 USD | 256,306.11 USD | 165,186.65 USD | 91,119.46 USD | `+21.62%` | `3B / 4S` |
| `5:00 UTC` | `57.83` | `57.80` | `57.83` | `57.94` | `57.61` | 405,316.11 USD | 265,776.17 USD | 139,539.93 USD | 126,236.24 USD | `+31.15%` | `10B / 0S` |
| `0:00 UTC` | `57.98` | `57.97` | `57.98` | `58.05` | `57.84` | 364,891.83 USD | 190,130.13 USD | 174,761.70 USD | 15,368.44 USD | `+4.21%` | `2B / 2S` |
| `5:00 UTC` | `58.02` | `58.02` | `58.02` | `58.16` | `57.89` | 452,756.15 USD | 221,914.68 USD | 230,841.47 USD | -8,926.79 USD | `-1.97%` | `3B / 4S` |
| `0:00 UTC` | `57.00` | `57.30` | `57.00` | `58.02` | `56.86` | 3,333,793.29 USD | 1,387,460.39 USD | 1,946,332.90 USD | -558,872.51 USD | `-16.76%` | `8B / 29S` |
| `5:00 UTC` | `57.25` | `57.29` | `57.25` | `57.45` | `57.14` | 618,298.97 USD | 355,257.55 USD | 263,041.42 USD | 92,216.13 USD | `+14.91%` | `5B / 2S` |
| `0:00 UTC` | `56.60` | `56.15` | `56.60` | `57.32` | `55.30` | 7,177,688.25 USD | 3,006,268.39 USD | 4,171,419.87 USD | -1,165,151.48 USD | `-16.23%` | `6B / 23S` |
| `5:00 UTC` | `55.00` | `54.96` | `55.00` | `55.59` | `54.17` | 11,110,862.71 USD | 4,658,705.25 USD | 6,452,157.46 USD | -1,793,452.21 USD | `-16.14%` | `3B / 23S` |
| `0:00 UTC` | `54.81` | `54.83` | `54.81` | `55.19` | `54.53` | 1,118,511.65 USD | 730,071.44 USD | 388,440.22 USD | 341,631.22 USD | `+30.54%` | `17B / 5S` |

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
| `5m` | 100,990.00 USD | 738,750.00 USD | **`ACCUMULATION`** |
| `15m` | -305,060.00 USD | 5,430.00 USD | **`DISTRIBUTION`** |
| `30m` | -2,200,000.00 USD | -5,370,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,310,000.00 USD | -5,630,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -2,400,000.00 USD | -5,310,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -2,160,000.00 USD | -5,860,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,020,000.00 USD | -5,420,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -826,390.00 USD | -3,590,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 55,040.00 USD | -3,120,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -341,730.00 USD | -7,090,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 3,480,000.00 USD | -25,990,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -22,420,000.00 USD | -194,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+100.99K` | 15m=`-305.06K` | 1h=`-2.31M` | 24h=`-341.73K`
* Futures Capital Netflows: 5m=`+738.75K` | 15m=`+5.43K` | 1h=`-5.63M` | 24h=`-7.09M`
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
  * Execution Entry: `54.62` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `53.53` (Risk Distance: `1.09` pts)
  * +2.5R Take Profit: `57.34`
  * Mathematical Lot Sizing: **`9.17 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `54.78` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `55.87` (Risk Distance: `1.09` pts)
  * +2.5R Take Profit: `52.06`
  * Mathematical Lot Sizing: **`9.17 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`55.22`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
