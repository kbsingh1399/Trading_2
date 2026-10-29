# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 01:23:52 IST` (`2026-10-29 19:53:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `57.88` | **Live Ask Quote**: `58.17` | **Mid Price**: `58.02`
- **Spread Points**: `300.00` | **Spread BPS**: `51.70 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `57.82` | VWAP Z-Score: `-0.09` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.3171` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `49.85` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `59.61` | Lower -3.00σ Band: `56.02`
  * Upper +2.51σ Band: `59.32` | Lower -2.51σ Band: `56.32`
  * Upper +2.01σ Band: `59.02` | Lower -2.01σ Band: `56.62`
  * Upper +2.00σ Band: `59.01` | Lower -2.00σ Band: `56.62`
  * Upper +1.28σ Band: `58.58` | Lower -1.28σ Band: `57.05`
  * Upper +1.00σ Band: `58.41` | Lower -1.00σ Band: `57.22`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`57.67` | EMA-20=`57.76` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`57.77` (Slope: `+0.0000`) | EMA-100=`57.76`
  * Institutional Anchors: EMA-144=`57.67` | EMA-200=`57.47` (Slope: `+0.0504`) | EMA-233=`57.30`
- **Range Boundaries**: 24H High=`59.62` | 24H Low=`56.67` | Weekly High=`59.62` | Weekly Low=`55.48`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `58.48` (Distance: `-0.80%`)
  * Point of Control (POC) = `57.84` (Distance: `+0.31%`)
  * Value Area Low (VAL) = `57.04` (Distance: `+1.71%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.44` | POC=`57.22` | VAL=`56.70`
  * Prior Day Extremes: PDH=`59.62` | PDL=`56.37` | PDC=`58.69`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`57.76` | Weekly POC=`56.49` | Weekly VAL=`55.99`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`59.52` | Low=`56.73`
  * London Session (08:00-16:00 UTC): High=`58.12` | Low=`56.67`
  * New York Session (13:00-21:00 UTC): High=`58.72` | Low=`57.04`
  * Initial Balance (First Hour): IB High=`58.02` | IB Low=`57.29`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `57.79` - `58.26`
  * Optimal Trade Entry (OTE 0.705): `58.14`
  * Structural Invalidation Anchor (0.786): `58.49`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `57.83` | `58.05` | `57.83` | `57.99` | `2,654` | 153,898.40 USD | -4,392.60 USD | `-2.85%` | -997,194.59 USD | `-0.37` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `57.99` | `58.02` | `57.87` | `57.90` | `1,806` | 104,624.73 USD | 3,458.56 USD | `+3.31%` | -993,736.03 USD | `-0.19` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `57.91` | `58.01` | `57.91` | `57.95` | `1,270` | 73,607.75 USD | 21,791.08 USD | `+29.60%` | -971,944.95 USD | `+0.05` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `57.74` | `57.76` | `57.54` | `57.62` | `7,316` | 421,492.76 USD | 91,119.46 USD | `+21.62%` | -1,119,038.23 USD | `+0.55` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `57.63` | `57.93` | `57.61` | `57.83` | `7,014` | 405,316.11 USD | 126,236.24 USD | `+31.15%` | -992,801.98 USD | `+0.70` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `57.83` | `58.05` | `57.83` | `57.94` | `5,729` | 332,100.92 USD | 20,827.07 USD | `+6.27%` | -971,974.91 USD | `+0.17` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `58.44` | `58.44` | `57.50` | `57.71` | `54,276` | 3,147,173.69 USD | -410,603.26 USD | `-13.05%` | -1,227,884.54 USD | `-0.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `57.72` | `57.92` | `57.43` | `57.74` | `47,138` | 2,718,274.03 USD | 101,628.42 USD | `+3.74%` | -1,126,256.12 USD | `+0.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `57.74` | `58.05` | `57.54` | `57.93` | `20,053` | 1,158,590.95 USD | 237,863.93 USD | `+20.53%` | -888,392.19 USD | `+0.77` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `57.04` | `58.16` | `56.85` | `58.00` | `178,996` | 10,300,529.12 USD | 452,809.17 USD | `+4.40%` | -1,290,330.89 USD | `+1.24` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | -1,041,745.33 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.95` | `226,922` | 13,208,049.51 USD | 153,701.94 USD | `+1.16%` | -888,043.39 USD | `+0.53` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `59.19` | `59.70` | `56.95` | `57.21` | `387,394` | 22,568,170.72 USD | -1,232,294.71 USD | `-5.46%` | -1,242,932.23 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `57.20` | `58.23` | `56.92` | `57.04` | `229,127` | 13,178,164.26 USD | -500,207.83 USD | `-3.80%` | -1,743,140.06 USD | `+0.16` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `57.04` | `58.16` | `56.85` | `58.00` | `178,996` | 10,300,529.12 USD | 452,809.17 USD | `+4.40%` | -1,290,330.89 USD | `+1.24` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | -1,041,745.33 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.95` | `226,922` | 13,208,049.51 USD | 153,701.94 USD | `+1.16%` | -888,043.39 USD | `+0.53` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| --- | **`58.02`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:23:08 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1065` | `0xeadc...9d55` | `LONG` | 2,114,643.41 USD | `36,463.77` | `52.78` | `57.95` | `0.000000` | 189,967.46 USD | `+8.98%` | `10X Cross` |
| `1073` | `0x9aa5...58af` | `SHORT` | 2,097,146.02 USD | `36,177.65` | `71.22` | `57.95` | `264.42` | 479,340.65 USD | `+22.86%` | `10X Cross` |
| `2014` | `0xcac1...26b3` | `SHORT` | 1,009,730.61 USD | `17,411.55` | `49.01` | `57.95` | `504.52` | -156,325.29 USD | `-15.48%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `57.00` | 7,510.28 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 57.0040 USD [API] | `2026-10-27 21:51:50` |
| `ANNOUNCEMENT` | `INFO` | `57.03` | 6,666.57 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 6.67K USD at 57.0280 USD [API] | `2026-10-27 22:17:57` |
| `ANNOUNCEMENT` | `INFO` | `56.91` | 6,835.37 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 6.84K USD at 56.9140 USD [API] | `2026-10-27 22:43:37` |
| `ANNOUNCEMENT` | `INFO` | `95.72` | 1,503.76 USD | `-` | `NEWS_INTEL` | `-` | #LTC Liquidated Long: 1.50K USD at 95.7200 USD [API] | `2025-11-16 17:33:32` |
| `ANNOUNCEMENT` | `INFO` | `95.73` | 1,629.27 USD | `-` | `NEWS_INTEL` | `-` | #LTC Liquidated Long: 1.63K USD at 95.7270 USD [API] | `2025-11-16 17:33:32` |
| `ANNOUNCEMENT` | `INFO` | `95.73` | 1,612.16 USD | `-` | `NEWS_INTEL` | `-` | #LTC Liquidated Long: 1.61K USD at 95.7340 USD [API] | `2025-11-16 17:33:32` |
| `ANNOUNCEMENT` | `INFO` | `95.76` | 291.11 USD | `-` | `NEWS_INTEL` | `-` | #LTC Liquidated Long: 0.29K USD at 95.7610 USD [API] | `2025-11-16 17:33:32` |
| `ANNOUNCEMENT` | `INFO` | `57.06` | 5,006.36 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 5.01K USD at 57.0590 USD [API] | `2026-10-27 23:35:34` |
| `ANNOUNCEMENT` | `INFO` | `57.05` | 5,852.60 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 5.85K USD at 57.0540 USD [API] | `2026-10-27 23:35:34` |
| `ANNOUNCEMENT` | `INFO` | `57.05` | 6,837.32 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 6.84K USD at 57.0490 USD [API] | `2026-10-27 23:35:34` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`59.03` (Vol: 256,600.00 USD, Dist: `+1.95%`) | Long MP=`56.68` (Vol: 327,300.00 USD, Dist: `--2.10%`)
  * 48H Horizon: Short MP=`59.00` (Vol: 285,100.00 USD, Dist: `+1.91%`) | Long MP=`56.72` (Vol: 274,000.00 USD, Dist: `--2.04%`)
  * 3D Horizon: Short MP=`59.01` (Vol: 285,100.00 USD, Dist: `+1.91%`) | Long MP=`56.70` (Vol: 302,600.00 USD, Dist: `--2.08%`)
  * 7D Horizon: Short MP=`59.04` (Vol: 256,600.00 USD, Dist: `+1.96%`) | Long MP=`55.27` (Vol: 344,500.00 USD, Dist: `--4.55%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `12.25` | 122.50 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.45` | 100.22 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.75` | 2,560.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.85` | 411.20 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.05` | 2,200.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.15` | 251.43 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.65` | 150.15 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `15.35` | 4,520.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `16.15` | 1,940.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `16.95` | 479.18 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `17.25` | 3,360.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.55` | 371.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.05` | 3,470.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.45` | 2,010.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.55` | 1,170.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.65` | 764.78 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.85` | 100.64 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.45` | 19,950.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.65` | 349.21 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.65` | 5,230.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.75` | 655.74 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.05` | 421.36 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 277,980.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 173.39 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 50,740.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 374.20 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.35` | 263.50 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.65` | 738.47 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.95` | 5,490.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.45` | 546.53 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 272.75 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 173.85 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.15` | 445.33 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.45` | 4,100.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.05` | 227.46 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 583.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.25` | 3,630.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.45` | 999.53 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.55` | 108.74 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 297,600.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 218.46 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 9,470.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.75` | 708.48 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 538.53 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 27,730.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.45` | 4,110.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 5,680.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 2,870.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 125.24 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 1,450.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.45` | 166.47 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 3,250.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 953.68 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 32,850.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.05` | 393.96 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.15` | 826.43 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 257.76 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.85` | 4,470.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 182.85 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 126.70 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 3,240.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 17,580.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 166.49 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.25` | 264.38 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.75` | 929.50 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.85` | 6,250.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 3,020.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 423.18 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.65` | 687.19 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 101.80 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 359.76 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 438.74 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 9,580.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 11,790.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 4,860.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 6,210.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 446.67 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.05` | 7,570.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 341.70 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 287.61 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 4,880.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 384.57 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 4,840.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 664,760.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 570.02 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 865.53 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 444.94 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 5,900.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 1,550.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 133.10 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 2,160.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 1,010.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 133.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 1,290.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 6,340.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 666.26 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 396.54 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 14,490.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 644.96 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.55` | 41,550.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.65` | 685.98 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.95` | 3,580.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 3,090.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 64,190.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 35,410.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 1,570.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 5,800.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 2,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 8,950.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 120,820.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 312.26 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 5,640.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 2,010.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.55` | 1,520.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 426.02 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 801.14 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 1,580.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 2,380.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 12,190.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 89,810.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 842.44 USD | 937,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.65` | 277.28 USD | 936,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 4,230.00 USD | 936,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 134.55 USD | 932,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 2,620.00 USD | 932,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 329.32 USD | 929,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 135.00 USD | 929,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 41,150.00 USD | 928,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 2,180.00 USD | 887,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 23,940.00 USD | 885,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 7,820.00 USD | 861,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 704.87 USD | 853,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 9,710.00 USD | 853,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.25` | 39,320.00 USD | 843,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.35` | 383.78 USD | 804,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 936.73 USD | 803,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 1,300.00 USD | 802,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 11,860.00 USD | 801,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 1,980.00 USD | 789,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 1,050.00 USD | 787,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.35` | 2,600.00 USD | 786,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.45` | 2,180.00 USD | 783,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 1,770.00 USD | 781,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 4,780.00 USD | 780,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.95` | 2,420.00 USD | 775,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 1,860.00 USD | 772,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 2,680.00 USD | 770,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 4,390.00 USD | 768,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.35` | 263.02 USD | 763,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 2,030.00 USD | 763,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 273.90 USD | 761,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 231.56 USD | 761,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 1,390.00 USD | 761,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,580.00 USD | 759,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,740.00 USD | 758,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.35` | 5,230.00 USD | 752,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.45` | 2,500.00 USD | 747,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.55` | 18,010.00 USD | 744,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.65` | 12,030.00 USD | 726,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.75` | 1,250.00 USD | 714,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.95` | 28,540.00 USD | 713,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.05` | 1,820.00 USD | 684,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.15` | 19,460.00 USD | 683,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.25` | 102.51 USD | 663,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.35` | 1,030.00 USD | 663,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,720.00 USD | 662,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.55` | 84,100.00 USD | 657,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.65` | 15,930.00 USD | 573,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.75` | 9,050.00 USD | 557,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.95` | 245.07 USD | 548,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.15` | 219,370.00 USD | 548,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.35` | 3,340.00 USD | 329,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.40` | 18,890,000.00 USD | 18,890,000.00 USD | 87,100.00 USD | 41,450.00 USD | 92,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.45` | 22,270.00 USD | 325,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.50` | 18,670,000.00 USD | 18,670,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.55` | 551.07 USD | 303,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.60` | 18,580,000.00 USD | 18,580,000.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.65` | 155.47 USD | 302,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.70` | 5,840,000.00 USD | 5,840,000.00 USD | 11,140.00 USD | 11,120.00 USD | 11,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.70` | 18,510,000.00 USD | 18,510,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.75` | 6,450.00 USD | 302,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.80` | 5,810,000.00 USD | 5,810,000.00 USD | 12,120.00 USD | 2,040.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.80` | 18,480,000.00 USD | 18,480,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.85` | 3,580.00 USD | 296,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.90` | 5,780,000.00 USD | 5,780,000.00 USD | 12,520.00 USD | 21,470.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.90` | 18,420,000.00 USD | 18,420,000.00 USD | 5,870.00 USD | 15,810.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.95` | 12,070.00 USD | 292,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.00` | 5,740,000.00 USD | 5,740,000.00 USD | 23,390.00 USD | 8,230.00 USD | 23,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.00` | 18,390,000.00 USD | 18,390,000.00 USD | 64,300.00 USD | 20,800.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.10` | 5,690,000.00 USD | 5,690,000.00 USD | 27,580.00 USD | 5,780.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 18,300,000.00 USD | 18,300,000.00 USD | 24,220.00 USD | 18,810.00 USD | 35,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.20` | 5,620,000.00 USD | 5,620,000.00 USD | 18,580.00 USD | 10,410.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 18,220,000.00 USD | 18,220,000.00 USD | 35,740.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.25` | 179.22 USD | 280,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.30` | 5,570,000.00 USD | 5,570,000.00 USD | 33,360.00 USD | 8,170.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 18,150,000.00 USD | 18,150,000.00 USD | 14,070.00 USD | 12,840.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.35` | 27,650.00 USD | 280,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.40` | 5,520,000.00 USD | 5,520,000.00 USD | 7,880.00 USD | 6,900.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 18,120,000.00 USD | 18,120,000.00 USD | 20,580.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.45` | 3,830.00 USD | 252,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.50` | 5,490,000.00 USD | 5,490,000.00 USD | 13,740.00 USD | 5,360.00 USD | 80.02 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.50` | 18,070,000.00 USD | 18,070,000.00 USD | 33,240.00 USD | 667.05 USD | 10,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.55` | 8,700.00 USD | 248,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.60` | 5,480,000.00 USD | 5,480,000.00 USD | 2,760.00 USD | 8,200.00 USD | 273.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.60` | 18,020,000.00 USD | 18,020,000.00 USD | 36,640.00 USD | 14,530.00 USD | 584.77 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.70` | 5,460,000.00 USD | 5,460,000.00 USD | 4,310.00 USD | 7,610.00 USD | 13,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.70` | 17,970,000.00 USD | 17,970,000.00 USD | 20,250.00 USD | 27,720.00 USD | 42,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.75` | 7,450.00 USD | 240,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.80` | 5,440,000.00 USD | 5,440,000.00 USD | 14,400.00 USD | 2,680.00 USD | 11,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.80` | 17,880,000.00 USD | 17,880,000.00 USD | 46,600.00 USD | 14,180.00 USD | 108.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.85` | 5,950.00 USD | 232,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.90` | 5,410,000.00 USD | 5,410,000.00 USD | 28,000.00 USD | 465.85 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.90` | 17,820,000.00 USD | 17,820,000.00 USD | 51,920.00 USD | 23,030.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.95` | 11,680.00 USD | 226,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.00` | 5,380,000.00 USD | 5,380,000.00 USD | 3,880.00 USD | 2,200.00 USD | 936.80 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.00` | 17,740,000.00 USD | 17,740,000.00 USD | 18,990.00 USD | 8,880.00 USD | 32,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.05` | 900.26 USD | 215,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.10` | 5,370,000.00 USD | 5,370,000.00 USD | 9,600.00 USD | 2,540.00 USD | 780.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.10` | 17,680,000.00 USD | 17,680,000.00 USD | 51,920.00 USD | 29,200.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.15` | 22,150.00 USD | 214,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.20` | 5,360,000.00 USD | 5,360,000.00 USD | 8,730.00 USD | 7,180.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.20` | 17,590,000.00 USD | 17,590,000.00 USD | 90,340.00 USD | 17,580.00 USD | 25,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.25` | 1,500.00 USD | 192,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.30` | 5,330,000.00 USD | 5,330,000.00 USD | 10,170.00 USD | 4,410.00 USD | 7,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.30` | 17,450,000.00 USD | 17,450,000.00 USD | 63,050.00 USD | 14,250.00 USD | 37,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.35` | 1,910.00 USD | 190,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.40` | 5,310,000.00 USD | 5,310,000.00 USD | 18,620.00 USD | 3,050.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.40` | 17,340,000.00 USD | 17,340,000.00 USD | 49,250.00 USD | 4,350.00 USD | 48,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.45` | 4,880.00 USD | 188,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.50` | 5,280,000.00 USD | 5,280,000.00 USD | 9,130.00 USD | 2,350.00 USD | 83.29 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.50` | 17,240,000.00 USD | 17,240,000.00 USD | 50,210.00 USD | 13,810.00 USD | 22,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.60` | 5,270,000.00 USD | 5,270,000.00 USD | 20,020.00 USD | 5,030.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.60` | 17,150,000.00 USD | 17,150,000.00 USD | 53,580.00 USD | 8,450.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.65` | 533.82 USD | 183,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.70` | 5,230,000.00 USD | 5,230,000.00 USD | 5,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.70` | 17,080,000.00 USD | 17,080,000.00 USD | 64,150.00 USD | 15,090.00 USD | 12,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.75` | 332.71 USD | 183,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.80` | 5,230,000.00 USD | 5,230,000.00 USD | 1,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.80` | 16,990,000.00 USD | 16,990,000.00 USD | 99,150.00 USD | 48,300.00 USD | 86,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.85` | 2,130.00 USD | 182,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.90` | 5,220,000.00 USD | 5,220,000.00 USD | 7,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.90` | 16,750,000.00 USD | 16,750,000.00 USD | 111,970.00 USD | 25,310.00 USD | 123,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.95` | 50,550.00 USD | 180,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.00` | 5,220,000.00 USD | 5,220,000.00 USD | 3,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.00` | 16,490,000.00 USD | 16,490,000.00 USD | 344,710.00 USD | 142,130.00 USD | 210,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.05` | 219.44 USD | 130,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.10` | 5,210,000.00 USD | 5,210,000.00 USD | 9,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.10` | 15,800,000.00 USD | 15,800,000.00 USD | 232,410.00 USD | 45,470.00 USD | 138,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.15` | 13,210.00 USD | 130,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.20` | 5,200,000.00 USD | 5,200,000.00 USD | 14,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.20` | 15,380,000.00 USD | 15,380,000.00 USD | 234,980.00 USD | 141,240.00 USD | 133,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.25` | 2,400.00 USD | 116,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.30` | 5,190,000.00 USD | 5,190,000.00 USD | 4,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.30` | 14,870,000.00 USD | 14,870,000.00 USD | 245,850.00 USD | 89,080.00 USD | 257,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.40` | 5,180,000.00 USD | 5,180,000.00 USD | 2,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.40` | 14,280,000.00 USD | 14,280,000.00 USD | 319,640.00 USD | 106,460.00 USD | 105,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.45` | 12,640.00 USD | 114,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.50` | 5,180,000.00 USD | 5,180,000.00 USD | 3,040.00 USD | 126.10 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.50` | 13,750,000.00 USD | 13,750,000.00 USD | 169,910.00 USD | 53,460.00 USD | 142,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.55` | 2,470.00 USD | 101,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.60` | 5,180,000.00 USD | 5,180,000.00 USD | 2,510.00 USD | 601.45 USD | 944.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.60` | 13,380,000.00 USD | 13,380,000.00 USD | 111,350.00 USD | 43,430.00 USD | 73,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.65` | 2,380.00 USD | 99,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.70` | 5,170,000.00 USD | 5,170,000.00 USD | 48,030.00 USD | 15,810.00 USD | 52,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.70` | 13,150,000.00 USD | 13,150,000.00 USD | 122,080.00 USD | 50,560.00 USD | 172,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.75` | 470.85 USD | 96,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.80` | 5,060,000.00 USD | 5,060,000.00 USD | 46,570.00 USD | 18,410.00 USD | 26,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.80` | 12,810,000.00 USD | 12,810,000.00 USD | 307,590.00 USD | 104,820.00 USD | 156,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.85` | 167.29 USD | 96,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.90` | 4,970,000.00 USD | 4,970,000.00 USD | 52,330.00 USD | 21,230.00 USD | 5,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.90` | 12,240,000.00 USD | 12,240,000.00 USD | 256,370.00 USD | 162,220.00 USD | 276,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.95` | 7,220.00 USD | 96,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.00` | 4,890,000.00 USD | 4,890,000.00 USD | 39,320.00 USD | 24,110.00 USD | 12,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.00` | 11,540,000.00 USD | 11,540,000.00 USD | 269,610.00 USD | 81,220.00 USD | 310,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.05` | 394.71 USD | 89,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.10` | 4,810,000.00 USD | 4,810,000.00 USD | 24,090.00 USD | 10,460.00 USD | 18,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.10` | 10,880,000.00 USD | 10,880,000.00 USD | 362,320.00 USD | 145,730.00 USD | 171,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.15` | 3,710.00 USD | 88,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.20` | 4,760,000.00 USD | 4,760,000.00 USD | 17,880.00 USD | 4,030.00 USD | 10,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.20` | 10,200,000.00 USD | 10,200,000.00 USD | 338,950.00 USD | 177,110.00 USD | 279,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.25` | 1,660.00 USD | 85,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.30` | 4,730,000.00 USD | 4,730,000.00 USD | 28,540.00 USD | 7,260.00 USD | 24,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.30` | 9,410,000.00 USD | 9,410,000.00 USD | 367,680.00 USD | 68,970.00 USD | 256,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.35` | 1,610.00 USD | 83,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.40` | 4,670,000.00 USD | 4,670,000.00 USD | 35,570.00 USD | 61,990.00 USD | 31,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.40` | 8,710,000.00 USD | 8,710,000.00 USD | 302,780.00 USD | 188,590.00 USD | 249,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.45` | 424.19 USD | 81,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.50` | 4,540,000.00 USD | 4,540,000.00 USD | 70,830.00 USD | 28,530.00 USD | 66,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.50` | 7,970,000.00 USD | 7,970,000.00 USD | 329,130.00 USD | 186,800.00 USD | 529,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.55` | 3,100.00 USD | 81,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.60` | 4,370,000.00 USD | 4,370,000.00 USD | 95,580.00 USD | 23,020.00 USD | 93,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.60` | 6,930,000.00 USD | 6,930,000.00 USD | 426,340.00 USD | 261,500.00 USD | 277,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.70` | 4,160,000.00 USD | 4,160,000.00 USD | 77,300.00 USD | 36,250.00 USD | 47,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.70` | 5,960,000.00 USD | 5,960,000.00 USD | 174,240.00 USD | 32,180.00 USD | 273,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.80` | 4,000,000.00 USD | 4,000,000.00 USD | 118,840.00 USD | 29,840.00 USD | 42,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.80` | 5,480,000.00 USD | 5,480,000.00 USD | 60,840.00 USD | 54,060.00 USD | 144,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.90` | 3,810,000.00 USD | 3,810,000.00 USD | 110,070.00 USD | 50,820.00 USD | 130,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.90` | 5,220,000.00 USD | 5,220,000.00 USD | 65,400.00 USD | 94,580.00 USD | 280,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.00` | 3,520,000.00 USD | 3,520,000.00 USD | 125,000.00 USD | 52,160.00 USD | 56,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.00` | 4,780,000.00 USD | 4,780,000.00 USD | 181,230.00 USD | 88,840.00 USD | 107,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.10` | 3,280,000.00 USD | 3,280,000.00 USD | 98,040.00 USD | 63,650.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.10` | 4,400,000.00 USD | 4,400,000.00 USD | 121,920.00 USD | 133,900.00 USD | 46,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `56.15` | 78,230.00 USD | 78,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `56.20` | 3,110,000.00 USD | 3,110,000.00 USD | 72,300.00 USD | 58,350.00 USD | 62,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.20` | 4,100,000.00 USD | 4,100,000.00 USD | 104,510.00 USD | 80,130.00 USD | 205,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.30` | 2,920,000.00 USD | 2,920,000.00 USD | 47,900.00 USD | 38,230.00 USD | 37,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.30` | 3,710,000.00 USD | 3,710,000.00 USD | 91,850.00 USD | 140,830.00 USD | 85,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.40` | 2,790,000.00 USD | 2,790,000.00 USD | 185,180.00 USD | 31,390.00 USD | 126,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.40` | 3,390,000.00 USD | 3,390,000.00 USD | 215,940.00 USD | 124,050.00 USD | 140,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.50` | 2,450,000.00 USD | 2,450,000.00 USD | 76,980.00 USD | 130,940.00 USD | 65,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.50` | 2,910,000.00 USD | 2,910,000.00 USD | 26,520.00 USD | 101,420.00 USD | 71,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.60` | 2,180,000.00 USD | 2,180,000.00 USD | 161,590.00 USD | 64,600.00 USD | 135,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.60` | 2,710,000.00 USD | 2,710,000.00 USD | 363,190.00 USD | 130,070.00 USD | 128,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.70` | 1,820,000.00 USD | 1,820,000.00 USD | 198,110.00 USD | 66,620.00 USD | 208,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.70` | 2,090,000.00 USD | 2,090,000.00 USD | 110,940.00 USD | 105,810.00 USD | 206,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.80` | 1,340,000.00 USD | 1,340,000.00 USD | 175,040.00 USD | 85,530.00 USD | 115,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.80` | 1,670,000.00 USD | 1,670,000.00 USD | 153,580.00 USD | 97,670.00 USD | 262,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.90` | 965,230.00 USD | 965,230.00 USD | 280,920.00 USD | 56,960.00 USD | 109,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.90` | 1,150,000.00 USD | 1,150,000.00 USD | 108,440.00 USD | 65,260.00 USD | 94,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.00` | 518,300.00 USD | 518,300.00 USD | 34,380.00 USD | 24,060.00 USD | 44,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.00` | 885,980.00 USD | 885,980.00 USD | 50,710.00 USD | 111,780.00 USD | 91,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.10` | 415,140.00 USD | 415,140.00 USD | 73,260.00 USD | 25,570.00 USD | 4,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.10` | 632,090.00 USD | 632,090.00 USD | 36,580.00 USD | 14,880.00 USD | 500.18 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.20` | 311,930.00 USD | 311,930.00 USD | 27,530.00 USD | 40,100.00 USD | 256.90 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.20` | 580,130.00 USD | 580,130.00 USD | 21,160.00 USD | 50,300.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.30` | 244,040.00 USD | 244,040.00 USD | 0.00 USD | 15,520.00 USD | 51,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.30` | 504,980.00 USD | 504,980.00 USD | 22,360.00 USD | 27,320.00 USD | 45,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.40` | 176,620.00 USD | 176,620.00 USD | 19,650.00 USD | 26,470.00 USD | 673.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.40` | 409,770.00 USD | 409,770.00 USD | 38,520.00 USD | 30,000.00 USD | 129,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.50` | 129,820.00 USD | 129,820.00 USD | 80,510.00 USD | 12,870.00 USD | 36,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.50` | 211,310.00 USD | 211,310.00 USD | 76,670.00 USD | 23,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.60` | 111,570.00 USD | 111,570.00 USD | 70,040.00 USD | 15,090.00 USD | 26,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.20` | 638.03 USD | 638.03 USD | 0.00 USD | 0.00 USD | 638.03 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.40` | 24,790.00 USD | 24,790.00 USD | 0.00 USD | 0.00 USD | 24,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.40` | 54,120.00 USD | 54,120.00 USD | 0.00 USD | 0.00 USD | 54,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.50` | 94,910.00 USD | 94,910.00 USD | 48,820.00 USD | 20,920.00 USD | 379.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.50` | 78,650.00 USD | 78,650.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.70` | 103,330.00 USD | 103,330.00 USD | 0.00 USD | 8,070.00 USD | 355.85 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.70` | 118,400.00 USD | 118,400.00 USD | 0.00 USD | 4,430.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.80` | 174,400.00 USD | 174,400.00 USD | 32,920.00 USD | 14,520.00 USD | 23,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.80` | 128,130.00 USD | 128,130.00 USD | 0.00 USD | 3,320.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.90` | 372,240.00 USD | 372,240.00 USD | 11,180.00 USD | 123,990.00 USD | 62,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.90` | 230,920.00 USD | 230,920.00 USD | 0.00 USD | 47,950.00 USD | 54,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.00` | 704,650.00 USD | 704,650.00 USD | 141,660.00 USD | 57,070.00 USD | 133,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.00` | 669,930.00 USD | 669,930.00 USD | 255,180.00 USD | 65,270.00 USD | 118,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.10` | 1,130,000.00 USD | 1,130,000.00 USD | 189,650.00 USD | 46,160.00 USD | 186,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.10` | 964,420.00 USD | 964,420.00 USD | 91,060.00 USD | 45,400.00 USD | 158,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.20` | 1,450,000.00 USD | 1,450,000.00 USD | 153,040.00 USD | 72,590.00 USD | 96,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.20` | 1,300,000.00 USD | 1,300,000.00 USD | 153,580.00 USD | 10,620.00 USD | 174,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.30` | 1,940,000.00 USD | 1,940,000.00 USD | 283,630.00 USD | 73,090.00 USD | 133,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.30` | 1,580,000.00 USD | 1,580,000.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.40` | 2,150,000.00 USD | 2,150,000.00 USD | 78,510.00 USD | 56,810.00 USD | 76,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.40` | 1,890,000.00 USD | 1,890,000.00 USD | 103,370.00 USD | 73,620.00 USD | 137,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.50` | 2,330,000.00 USD | 2,330,000.00 USD | 114,880.00 USD | 51,920.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.50` | 2,030,000.00 USD | 2,030,000.00 USD | 67,060.00 USD | 59,920.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.60` | 2,470,000.00 USD | 2,470,000.00 USD | 62,260.00 USD | 66,510.00 USD | 13,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.60` | 2,530,000.00 USD | 2,530,000.00 USD | 268,680.00 USD | 145,550.00 USD | 86,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.70` | 2,620,000.00 USD | 2,620,000.00 USD | 20,820.00 USD | 30,710.00 USD | 94,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.70` | 2,930,000.00 USD | 2,930,000.00 USD | 53,810.00 USD | 180,620.00 USD | 161,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.80` | 2,710,000.00 USD | 2,710,000.00 USD | 40,180.00 USD | 38,670.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.80` | 3,300,000.00 USD | 3,300,000.00 USD | 118,240.00 USD | 96,860.00 USD | 155,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.90` | 2,930,000.00 USD | 2,930,000.00 USD | 112,870.00 USD | 21,840.00 USD | 90,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.90` | 3,670,000.00 USD | 3,670,000.00 USD | 246,770.00 USD | 84,430.00 USD | 40,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.00` | 3,260,000.00 USD | 3,260,000.00 USD | 182,690.00 USD | 65,010.00 USD | 78,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.00` | 4,180,000.00 USD | 4,180,000.00 USD | 231,370.00 USD | 183,130.00 USD | 94,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.10` | 3,460,000.00 USD | 3,460,000.00 USD | 91,380.00 USD | 42,440.00 USD | 71,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.10` | 4,740,000.00 USD | 4,740,000.00 USD | 263,890.00 USD | 130,900.00 USD | 174,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.20` | 3,730,000.00 USD | 3,730,000.00 USD | 136,940.00 USD | 38,090.00 USD | 97,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.20` | 5,240,000.00 USD | 5,240,000.00 USD | 207,990.00 USD | 131,530.00 USD | 157,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.30` | 4,000,000.00 USD | 4,000,000.00 USD | 94,410.00 USD | 77,160.00 USD | 92,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.30` | 5,610,000.00 USD | 5,610,000.00 USD | 118,160.00 USD | 95,890.00 USD | 155,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.40` | 4,300,000.00 USD | 4,300,000.00 USD | 164,780.00 USD | 55,740.00 USD | 81,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.40` | 6,060,000.00 USD | 6,060,000.00 USD | 92,570.00 USD | 126,870.00 USD | 226,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.50` | 4,530,000.00 USD | 4,530,000.00 USD | 105,740.00 USD | 38,540.00 USD | 82,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.50` | 6,510,000.00 USD | 6,510,000.00 USD | 160,180.00 USD | 89,250.00 USD | 207,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.60` | 4,640,000.00 USD | 4,640,000.00 USD | 79,140.00 USD | 32,180.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.60` | 7,090,000.00 USD | 7,090,000.00 USD | 294,830.00 USD | 109,510.00 USD | 167,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.70` | 4,810,000.00 USD | 4,810,000.00 USD | 85,730.00 USD | 45,070.00 USD | 33,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.70` | 7,340,000.00 USD | 7,340,000.00 USD | 142,880.00 USD | 79,060.00 USD | 28,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.75` | 1,040.00 USD | 1,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.80` | 4,930,000.00 USD | 4,930,000.00 USD | 46,230.00 USD | 13,240.00 USD | 65,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.80` | 7,560,000.00 USD | 7,560,000.00 USD | 54,870.00 USD | 78,710.00 USD | 94,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.90` | 5,000,000.00 USD | 5,000,000.00 USD | 39,620.00 USD | 19,210.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.90` | 7,850,000.00 USD | 7,850,000.00 USD | 139,720.00 USD | 52,860.00 USD | 92,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.95` | 794.18 USD | 1,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.00` | 5,080,000.00 USD | 5,080,000.00 USD | 46,000.00 USD | 7,290.00 USD | 32,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 7,990,000.00 USD | 7,990,000.00 USD | 96,160.00 USD | 36,500.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.05` | 482.91 USD | 2,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.10` | 5,090,000.00 USD | 5,090,000.00 USD | 5,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 8,020,000.00 USD | 8,020,000.00 USD | 31,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.15` | 3,870.00 USD | 6,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.20` | 5,190,000.00 USD | 5,190,000.00 USD | 75,930.00 USD | 1,510.00 USD | 23,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.20` | 8,240,000.00 USD | 8,240,000.00 USD | 116,610.00 USD | 70,180.00 USD | 33,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.30` | 5,210,000.00 USD | 5,210,000.00 USD | 9,540.00 USD | 6,960.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.30` | 8,380,000.00 USD | 8,380,000.00 USD | 51,130.00 USD | 36,170.00 USD | 55,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.40` | 5,240,000.00 USD | 5,240,000.00 USD | 22,150.00 USD | 7,530.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.40` | 8,540,000.00 USD | 8,540,000.00 USD | 89,350.00 USD | 41,800.00 USD | 24,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.50` | 5,290,000.00 USD | 5,290,000.00 USD | 8,990.00 USD | 20,580.00 USD | 22,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.50` | 8,630,000.00 USD | 8,630,000.00 USD | 19,810.00 USD | 34,770.00 USD | 35,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.60` | 5,350,000.00 USD | 5,350,000.00 USD | 23,830.00 USD | 13,550.00 USD | 20,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.60` | 8,880,000.00 USD | 8,880,000.00 USD | 54,240.00 USD | 63,390.00 USD | 132,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.65` | 211,210.00 USD | 217,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.70` | 5,440,000.00 USD | 5,440,000.00 USD | 51,690.00 USD | 9,670.00 USD | 28,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.70` | 9,110,000.00 USD | 9,110,000.00 USD | 99,020.00 USD | 15,950.00 USD | 114,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.80` | 5,480,000.00 USD | 5,480,000.00 USD | 23,530.00 USD | 8,420.00 USD | 1,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.80` | 9,450,000.00 USD | 9,450,000.00 USD | 183,860.00 USD | 68,030.00 USD | 92,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.90` | 5,540,000.00 USD | 5,540,000.00 USD | 34,520.00 USD | 11,940.00 USD | 16,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.90` | 9,600,000.00 USD | 9,600,000.00 USD | 79,630.00 USD | 35,500.00 USD | 35,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.00` | 5,580,000.00 USD | 5,580,000.00 USD | 21,250.00 USD | 1,560.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.00` | 9,720,000.00 USD | 9,720,000.00 USD | 57,760.00 USD | 13,260.00 USD | 49,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.10` | 5,590,000.00 USD | 5,590,000.00 USD | 12,050.00 USD | 945.47 USD | 2,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.10` | 9,790,000.00 USD | 9,790,000.00 USD | 36,500.00 USD | 12,820.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.20` | 5,590,000.00 USD | 5,590,000.00 USD | 3,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.20` | 9,900,000.00 USD | 9,900,000.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.30` | 5,590,000.00 USD | 5,590,000.00 USD | 464.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.30` | 10,050,000.00 USD | 10,050,000.00 USD | 38,120.00 USD | 23,450.00 USD | 85,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.40` | 5,600,000.00 USD | 5,600,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.40` | 10,190,000.00 USD | 10,190,000.00 USD | 81,060.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.50` | 10,270,000.00 USD | 10,270,000.00 USD | 44,300.00 USD | 14,320.00 USD | 26,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.60` | 5,600,000.00 USD | 5,600,000.00 USD | 1,100.00 USD | 0.00 USD | 327.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.60` | 10,340,000.00 USD | 10,340,000.00 USD | 34,340.00 USD | 7,100.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.70` | 5,640,000.00 USD | 5,640,000.00 USD | 16,430.00 USD | 4,920.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.70` | 10,430,000.00 USD | 10,430,000.00 USD | 22,020.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.80` | 5,670,000.00 USD | 5,670,000.00 USD | 16,330.00 USD | 7,010.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.80` | 10,570,000.00 USD | 10,570,000.00 USD | 73,200.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.90` | 5,690,000.00 USD | 5,690,000.00 USD | 8,780.00 USD | 6,670.00 USD | 63.10 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.90` | 10,660,000.00 USD | 10,660,000.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.00` | 5,710,000.00 USD | 5,710,000.00 USD | 7,650.00 USD | 7,040.00 USD | 4,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.00` | 10,730,000.00 USD | 10,730,000.00 USD | 35,710.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.10` | 5,720,000.00 USD | 5,720,000.00 USD | 4,260.00 USD | 4,070.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.10` | 10,770,000.00 USD | 10,770,000.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.20` | 5,720,000.00 USD | 5,720,000.00 USD | 2,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.30` | 5,730,000.00 USD | 5,730,000.00 USD | 4,590.00 USD | 594.25 USD | 2,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.30` | 10,810,000.00 USD | 10,810,000.00 USD | 21,810.00 USD | 11,500.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.40` | 5,750,000.00 USD | 5,750,000.00 USD | 9,050.00 USD | 1,440.00 USD | 7,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.40` | 10,840,000.00 USD | 10,840,000.00 USD | 14,300.00 USD | 1,320.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.50` | 5,790,000.00 USD | 5,790,000.00 USD | 12,520.00 USD | 21,470.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.50` | 10,870,000.00 USD | 10,870,000.00 USD | 6,620.00 USD | 15,810.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.60` | 5,850,000.00 USD | 5,850,000.00 USD | 23,390.00 USD | 8,230.00 USD | 23,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.60` | 10,960,000.00 USD | 10,960,000.00 USD | 63,480.00 USD | 20,800.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.70` | 5,920,000.00 USD | 5,920,000.00 USD | 28,350.00 USD | 5,780.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.70` | 11,040,000.00 USD | 11,040,000.00 USD | 21,940.00 USD | 18,810.00 USD | 35,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.80` | 5,960,000.00 USD | 5,960,000.00 USD | 18,580.00 USD | 10,410.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.80` | 11,100,000.00 USD | 11,100,000.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.90` | 6,020,000.00 USD | 6,020,000.00 USD | 31,330.00 USD | 8,170.00 USD | 15,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.90` | 11,130,000.00 USD | 11,130,000.00 USD | 7,650.00 USD | 12,840.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.00` | 11,170,000.00 USD | 11,170,000.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.10` | 11,200,000.00 USD | 11,200,000.00 USD | 20,350.00 USD | 667.05 USD | 10,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.20` | 11,250,000.00 USD | 11,250,000.00 USD | 28,840.00 USD | 14,530.00 USD | 584.77 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.40` | 11,300,000.00 USD | 11,300,000.00 USD | 2,540.00 USD | 20,590.00 USD | 29,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.50` | 11,330,000.00 USD | 11,330,000.00 USD | 7,700.00 USD | 7,120.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.60` | 11,380,000.00 USD | 11,380,000.00 USD | 32,220.00 USD | 14,180.00 USD | 108.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.70` | 11,440,000.00 USD | 11,440,000.00 USD | 39,430.00 USD | 23,030.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.80` | 11,480,000.00 USD | 11,480,000.00 USD | 7,540.00 USD | 8,210.00 USD | 20,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.90` | 11,520,000.00 USD | 11,520,000.00 USD | 25,750.00 USD | 8,010.00 USD | 9,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.00` | 11,530,000.00 USD | 11,530,000.00 USD | 0.00 USD | 0.00 USD | 13,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `65.95` | 1,160.00 USD | 218,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.05` | 2,200.00 USD | 220,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.85` | 33,950.00 USD | 254,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.95` | 121.18 USD | 254,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.85` | 709.03 USD | 255,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `69.45` | 414.62 USD | 255,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `70.45` | 5,270.00 USD | 261,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `73.15` | 667.86 USD | 261,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `76.35` | 8,380.00 USD | 270,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.85` | 602.56 USD | 270,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.95` | 136.41 USD | 271,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.75` | 646.00 USD | 271,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.05` | 19,000.00 USD | 290,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.55` | 123.96 USD | 290,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.65` | 3,850.00 USD | 294,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.75` | 214.32 USD | 294,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `84.65` | 862.58 USD | 295,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `85.25` | 2,810.00 USD | 298,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `85.55` | 22,830.00 USD | 321,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `86.65` | 3,470.00 USD | 324,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `96.55` | 2,410.00 USD | 327,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `97.75` | 1,040.00 USD | 328,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.75` | 674.46 USD | 328,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.85` | 353,760.00 USD | 682,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.05` | 21,210.00 USD | 703,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.45` | 131.44 USD | 704,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.55` | 1,120.00 USD | 705,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.65` | 4,830.00 USD | 709,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 664.59 USD | 710,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.65` | 22,330.00 USD | 732,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.65` | 420.77 USD | 733,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `12.25` | 2,920,000.00 USD | 0.00 USD | 122.50 USD | `-78.79%` | `10.00` |
| `Live` | `Long` | `12.45` | 2,920,000.00 USD | 0.00 USD | 100.22 USD | `-78.45%` | `8.05` |
| `Live` | `Long` | `12.75` | 2,920,000.00 USD | 0.00 USD | 2,560.00 USD | `-77.93%` | `200.43` |
| `Live` | `Long` | `12.85` | 2,920,000.00 USD | 0.00 USD | 411.20 USD | `-77.75%` | `32.00` |
| `Live` | `Long` | `13.05` | 2,920,000.00 USD | 0.00 USD | 2,200.00 USD | `-77.41%` | `168.79` |
| `Live` | `Long` | `13.15` | 2,910,000.00 USD | 0.00 USD | 251.43 USD | `-77.23%` | `19.12` |
| `Live` | `Long` | `13.65` | 2,910,000.00 USD | 0.00 USD | 150.15 USD | `-76.37%` | `11.00` |
| `Live` | `Long` | `15.35` | 2,910,000.00 USD | 0.00 USD | 4,520.00 USD | `-73.43%` | `294.67` |
| `Live` | `Long` | `16.15` | 2,910,000.00 USD | 0.00 USD | 1,940.00 USD | `-72.04%` | `120.00` |
| `Live` | `Long` | `16.95` | 2,910,000.00 USD | 0.00 USD | 479.18 USD | `-70.66%` | `28.27` |
| `Live` | `Long` | `17.25` | 2,910,000.00 USD | 0.00 USD | 3,360.00 USD | `-70.14%` | `195.03` |
| `Live` | `Long` | `18.55` | 2,900,000.00 USD | 0.00 USD | 371.00 USD | `-67.89%` | `20.00` |
| `Live` | `Long` | `19.05` | 2,900,000.00 USD | 0.00 USD | 3,470.00 USD | `-67.02%` | `182.00` |
| `Live` | `Long` | `19.45` | 2,900,000.00 USD | 0.00 USD | 2,010.00 USD | `-66.33%` | `103.47` |
| `Live` | `Long` | `19.55` | 2,900,000.00 USD | 0.00 USD | 1,170.00 USD | `-66.16%` | `60.00` |
| `Live` | `Long` | `19.65` | 2,900,000.00 USD | 0.00 USD | 764.78 USD | `-65.98%` | `38.92` |
| `Live` | `Long` | `19.85` | 2,900,000.00 USD | 0.00 USD | 100.64 USD | `-65.64%` | `5.07` |
| `Live` | `Long` | `21.45` | 2,900,000.00 USD | 0.00 USD | 19,950.00 USD | `-62.87%` | `930.00` |
| `Live` | `Long` | `21.65` | 2,880,000.00 USD | 0.00 USD | 349.21 USD | `-62.52%` | `16.13` |
| `Live` | `Long` | `22.65` | 2,870,000.00 USD | 0.00 USD | 5,230.00 USD | `-60.79%` | `230.91` |
| `Live` | `Long` | `23.75` | 2,870,000.00 USD | 0.00 USD | 655.74 USD | `-58.88%` | `27.61` |
| `Live` | `Long` | `24.05` | 2,870,000.00 USD | 0.00 USD | 421.36 USD | `-58.37%` | `17.52` |
| `Live` | `Long` | `25.25` | 2,870,000.00 USD | 0.00 USD | 277,980.00 USD | `-56.29%` | `11,009.19` |
| `Live` | `Long` | `25.35` | 2,590,000.00 USD | 0.00 USD | 173.39 USD | `-56.11%` | `6.84` |
| `Live` | `Long` | `25.55` | 2,590,000.00 USD | 0.00 USD | 50,740.00 USD | `-55.77%` | `1,985.99` |
| `Live` | `Long` | `25.95` | 2,540,000.00 USD | 0.00 USD | 374.20 USD | `-55.08%` | `14.42` |
| `Live` | `Long` | `26.35` | 2,540,000.00 USD | 0.00 USD | 263.50 USD | `-54.38%` | `10.00` |
| `Live` | `Long` | `26.65` | 2,540,000.00 USD | 0.00 USD | 738.47 USD | `-53.86%` | `27.71` |
| `Live` | `Long` | `26.95` | 2,540,000.00 USD | 0.00 USD | 5,490.00 USD | `-53.34%` | `203.85` |
| `Live` | `Long` | `27.45` | 2,530,000.00 USD | 0.00 USD | 546.53 USD | `-52.48%` | `19.91` |
| `Live` | `Long` | `27.55` | 2,530,000.00 USD | 0.00 USD | 272.75 USD | `-52.31%` | `9.90` |
| `Live` | `Long` | `27.95` | 2,530,000.00 USD | 0.00 USD | 173.85 USD | `-51.61%` | `6.22` |
| `Live` | `Long` | `28.15` | 2,530,000.00 USD | 0.00 USD | 445.33 USD | `-51.27%` | `15.82` |
| `Live` | `Long` | `28.45` | 2,530,000.00 USD | 0.00 USD | 4,100.00 USD | `-50.75%` | `144.17` |
| `Live` | `Long` | `29.05` | 2,530,000.00 USD | 0.00 USD | 227.46 USD | `-49.71%` | `7.83` |
| `Live` | `Long` | `29.15` | 2,530,000.00 USD | 0.00 USD | 583.00 USD | `-49.54%` | `20.00` |
| `Live` | `Long` | `29.25` | 2,530,000.00 USD | 0.00 USD | 3,630.00 USD | `-49.36%` | `124.01` |
| `Live` | `Long` | `29.45` | 2,520,000.00 USD | 0.00 USD | 999.53 USD | `-49.02%` | `33.94` |
| `Live` | `Long` | `29.55` | 2,520,000.00 USD | 0.00 USD | 108.74 USD | `-48.84%` | `3.68` |
| `Live` | `Long` | `29.75` | 2,520,000.00 USD | 0.00 USD | 297,600.00 USD | `-48.50%` | `10,003.44` |
| `Live` | `Long` | `30.05` | 2,220,000.00 USD | 0.00 USD | 218.46 USD | `-47.98%` | `7.27` |
| `Live` | `Long` | `30.55` | 2,220,000.00 USD | 0.00 USD | 9,470.00 USD | `-47.11%` | `310.00` |
| `Live` | `Long` | `30.75` | 2,210,000.00 USD | 0.00 USD | 708.48 USD | `-46.77%` | `23.04` |
| `Live` | `Long` | `30.95` | 2,210,000.00 USD | 0.00 USD | 538.53 USD | `-46.42%` | `17.40` |
| `Live` | `Long` | `31.15` | 2,210,000.00 USD | 0.00 USD | 27,730.00 USD | `-46.07%` | `890.26` |
| `Live` | `Long` | `31.45` | 2,190,000.00 USD | 0.00 USD | 4,110.00 USD | `-45.55%` | `130.63` |
| `Live` | `Long` | `31.55` | 2,180,000.00 USD | 0.00 USD | 5,680.00 USD | `-45.38%` | `180.02` |
| `Live` | `Long` | `31.85` | 2,180,000.00 USD | 0.00 USD | 2,870.00 USD | `-44.86%` | `90.00` |
| `Live` | `Long` | `31.95` | 2,170,000.00 USD | 0.00 USD | 125.24 USD | `-44.69%` | `3.92` |
| `Live` | `Long` | `32.15` | 2,170,000.00 USD | 0.00 USD | 1,450.00 USD | `-44.34%` | `45.01` |
| `Live` | `Long` | `32.45` | 2,170,000.00 USD | 0.00 USD | 166.47 USD | `-43.82%` | `5.13` |
| `Live` | `Long` | `32.65` | 2,170,000.00 USD | 0.00 USD | 3,250.00 USD | `-43.48%` | `99.49` |
| `Live` | `Long` | `32.75` | 2,170,000.00 USD | 0.00 USD | 953.68 USD | `-43.30%` | `29.12` |
| `Live` | `Long` | `32.85` | 2,170,000.00 USD | 0.00 USD | 32,850.00 USD | `-43.13%` | `1,000.01` |
| `Live` | `Long` | `33.05` | 2,130,000.00 USD | 0.00 USD | 393.96 USD | `-42.78%` | `11.92` |
| `Live` | `Long` | `33.15` | 2,130,000.00 USD | 0.00 USD | 826.43 USD | `-42.61%` | `24.93` |
| `Live` | `Long` | `33.65` | 2,130,000.00 USD | 0.00 USD | 257.76 USD | `-41.75%` | `7.66` |
| `Live` | `Long` | `33.85` | 2,130,000.00 USD | 0.00 USD | 4,470.00 USD | `-41.40%` | `131.94` |
| `Live` | `Long` | `34.05` | 2,130,000.00 USD | 0.00 USD | 182.85 USD | `-41.05%` | `5.37` |
| `Live` | `Long` | `34.15` | 2,130,000.00 USD | 0.00 USD | 126.70 USD | `-40.88%` | `3.71` |
| `Live` | `Long` | `34.65` | 2,130,000.00 USD | 0.00 USD | 3,240.00 USD | `-40.01%` | `93.56` |
| `Live` | `Long` | `34.95` | 2,120,000.00 USD | 0.00 USD | 17,580.00 USD | `-39.50%` | `503.00` |
| `Live` | `Long` | `35.05` | 2,110,000.00 USD | 0.00 USD | 166.49 USD | `-39.32%` | `4.75` |
| `Live` | `Long` | `35.25` | 2,110,000.00 USD | 0.00 USD | 264.38 USD | `-38.98%` | `7.50` |
| `Live` | `Long` | `35.75` | 2,110,000.00 USD | 0.00 USD | 929.50 USD | `-38.11%` | `26.00` |
| `Live` | `Long` | `35.85` | 2,110,000.00 USD | 0.00 USD | 6,250.00 USD | `-37.94%` | `174.22` |
| `Live` | `Long` | `36.35` | 2,100,000.00 USD | 0.00 USD | 3,020.00 USD | `-37.07%` | `83.03` |
| `Live` | `Long` | `36.45` | 2,100,000.00 USD | 0.00 USD | 423.18 USD | `-36.90%` | `11.61` |
| `Live` | `Long` | `36.65` | 2,100,000.00 USD | 0.00 USD | 687.19 USD | `-36.55%` | `18.75` |
| `Live` | `Long` | `36.75` | 2,100,000.00 USD | 0.00 USD | 101.80 USD | `-36.38%` | `2.77` |
| `Live` | `Long` | `37.05` | 2,100,000.00 USD | 0.00 USD | 359.76 USD | `-35.86%` | `9.71` |
| `Live` | `Long` | `37.15` | 2,090,000.00 USD | 0.00 USD | 438.74 USD | `-35.69%` | `11.81` |
| `Live` | `Long` | `37.35` | 2,090,000.00 USD | 0.00 USD | 9,580.00 USD | `-35.34%` | `256.36` |
| `Live` | `Long` | `37.55` | 2,080,000.00 USD | 0.00 USD | 11,790.00 USD | `-34.99%` | `314.04` |
| `Live` | `Long` | `37.75` | 2,070,000.00 USD | 0.00 USD | 4,860.00 USD | `-34.65%` | `128.71` |
| `Live` | `Long` | `37.85` | 2,070,000.00 USD | 0.00 USD | 6,210.00 USD | `-34.47%` | `164.03` |
| `Live` | `Long` | `37.95` | 2,060,000.00 USD | 0.00 USD | 446.67 USD | `-34.30%` | `11.77` |
| `Live` | `Long` | `38.05` | 2,060,000.00 USD | 0.00 USD | 7,570.00 USD | `-34.13%` | `198.87` |
| `Live` | `Long` | `38.35` | 2,050,000.00 USD | 0.00 USD | 341.70 USD | `-33.61%` | `8.91` |
| `Live` | `Long` | `38.45` | 2,050,000.00 USD | 0.00 USD | 287.61 USD | `-33.44%` | `7.48` |
| `Live` | `Long` | `38.55` | 2,050,000.00 USD | 0.00 USD | 4,880.00 USD | `-33.26%` | `126.57` |
| `Live` | `Long` | `38.65` | 2,050,000.00 USD | 0.00 USD | 384.57 USD | `-33.09%` | `9.95` |
| `Live` | `Long` | `38.95` | 2,050,000.00 USD | 0.00 USD | 4,840.00 USD | `-32.57%` | `124.26` |
| `Live` | `Long` | `39.05` | 2,040,000.00 USD | 0.00 USD | 664,760.00 USD | `-32.40%` | `17,023.28` |
| `Live` | `Long` | `39.15` | 1,380,000.00 USD | 0.00 USD | 570.02 USD | `-32.22%` | `14.56` |
| `Live` | `Long` | `39.45` | 1,380,000.00 USD | 0.00 USD | 865.53 USD | `-31.70%` | `21.94` |
| `Live` | `Long` | `39.55` | 1,380,000.00 USD | 0.00 USD | 444.94 USD | `-31.53%` | `11.25` |
| `Live` | `Long` | `39.65` | 1,380,000.00 USD | 0.00 USD | 5,900.00 USD | `-31.36%` | `148.78` |
| `Live` | `Long` | `39.75` | 1,370,000.00 USD | 0.00 USD | 1,550.00 USD | `-31.19%` | `38.90` |
| `Live` | `Long` | `39.85` | 1,370,000.00 USD | 0.00 USD | 133.10 USD | `-31.01%` | `3.34` |
| `Live` | `Long` | `40.05` | 1,370,000.00 USD | 0.00 USD | 2,160.00 USD | `-30.67%` | `53.97` |
| `Live` | `Long` | `40.45` | 1,370,000.00 USD | 0.00 USD | 1,010.00 USD | `-29.97%` | `24.92` |
| `Live` | `Long` | `40.55` | 1,370,000.00 USD | 0.00 USD | 133.00 USD | `-29.80%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,370,000.00 USD | 0.00 USD | 1,290.00 USD | `-29.63%` | `31.63` |
| `Live` | `Long` | `40.85` | 1,360,000.00 USD | 0.00 USD | 6,340.00 USD | `-29.28%` | `155.23` |
| `Live` | `Long` | `40.95` | 1,360,000.00 USD | 0.00 USD | 666.26 USD | `-29.11%` | `16.27` |
| `Live` | `Long` | `41.05` | 1,360,000.00 USD | 0.00 USD | 396.54 USD | `-28.93%` | `9.66` |
| `Live` | `Long` | `41.25` | 1,360,000.00 USD | 0.00 USD | 14,490.00 USD | `-28.59%` | `351.26` |
| `Live` | `Long` | `41.45` | 1,340,000.00 USD | 0.00 USD | 644.96 USD | `-28.24%` | `15.56` |
| `Live` | `Long` | `41.55` | 1,340,000.00 USD | 0.00 USD | 41,550.00 USD | `-28.07%` | `1,000.00` |
| `Live` | `Long` | `41.65` | 1,300,000.00 USD | 0.00 USD | 685.98 USD | `-27.90%` | `16.47` |
| `Live` | `Long` | `41.95` | 1,300,000.00 USD | 0.00 USD | 3,580.00 USD | `-27.38%` | `85.43` |
| `Live` | `Long` | `42.05` | 1,300,000.00 USD | 0.00 USD | 3,090.00 USD | `-27.20%` | `73.52` |
| `Live` | `Long` | `42.15` | 1,290,000.00 USD | 0.00 USD | 64,190.00 USD | `-27.03%` | `1,522.78` |
| `Live` | `Long` | `42.25` | 1,230,000.00 USD | 0.00 USD | 35,410.00 USD | `-26.86%` | `838.00` |
| `Live` | `Long` | `42.65` | 1,190,000.00 USD | 0.00 USD | 1,570.00 USD | `-26.17%` | `36.70` |
| `Live` | `Long` | `42.85` | 1,190,000.00 USD | 0.00 USD | 5,800.00 USD | `-25.82%` | `135.38` |
| `Live` | `Long` | `42.95` | 1,190,000.00 USD | 0.00 USD | 2,000.00 USD | `-25.65%` | `46.65` |
| `Live` | `Long` | `43.05` | 1,180,000.00 USD | 0.00 USD | 8,950.00 USD | `-25.47%` | `208.00` |
| `Live` | `Long` | `43.15` | 1,170,000.00 USD | 0.00 USD | 120,820.00 USD | `-25.30%` | `2,800.00` |
| `Live` | `Long` | `43.25` | 1,050,000.00 USD | 0.00 USD | 312.26 USD | `-25.13%` | `7.22` |
| `Live` | `Long` | `43.35` | 1,050,000.00 USD | 0.00 USD | 5,640.00 USD | `-24.95%` | `130.00` |
| `Live` | `Long` | `43.45` | 1,050,000.00 USD | 0.00 USD | 2,010.00 USD | `-24.78%` | `46.25` |
| `Live` | `Long` | `43.55` | 1,050,000.00 USD | 0.00 USD | 1,520.00 USD | `-24.61%` | `35.00` |
| `Live` | `Long` | `43.65` | 1,040,000.00 USD | 0.00 USD | 426.02 USD | `-24.43%` | `9.76` |
| `Live` | `Long` | `43.85` | 1,040,000.00 USD | 0.00 USD | 801.14 USD | `-24.09%` | `18.27` |
| `Live` | `Long` | `43.95` | 1,040,000.00 USD | 0.00 USD | 1,580.00 USD | `-23.91%` | `35.97` |
| `Live` | `Long` | `44.15` | 1,040,000.00 USD | 0.00 USD | 2,380.00 USD | `-23.57%` | `53.99` |
| `Live` | `Long` | `44.25` | 1,040,000.00 USD | 0.00 USD | 12,190.00 USD | `-23.40%` | `275.59` |
| `Live` | `Long` | `44.35` | 1,030,000.00 USD | 0.00 USD | 89,810.00 USD | `-23.22%` | `2,024.93` |
| `Live` | `Long` | `44.55` | 937,480.00 USD | 0.00 USD | 842.44 USD | `-22.88%` | `18.91` |
| `Live` | `Long` | `44.65` | 936,640.00 USD | 0.00 USD | 277.28 USD | `-22.70%` | `6.21` |
| `Live` | `Long` | `44.75` | 936,360.00 USD | 0.00 USD | 4,230.00 USD | `-22.53%` | `94.55` |
| `Live` | `Long` | `44.85` | 932,130.00 USD | 0.00 USD | 134.55 USD | `-22.36%` | `3.00` |
| `Live` | `Long` | `44.95` | 932,000.00 USD | 0.00 USD | 2,620.00 USD | `-22.18%` | `58.18` |
| `Live` | `Long` | `45.05` | 929,380.00 USD | 0.00 USD | 329.32 USD | `-22.01%` | `7.31` |
| `Live` | `Long` | `45.15` | 929,050.00 USD | 0.00 USD | 135.00 USD | `-21.84%` | `2.99` |
| `Live` | `Long` | `45.25` | 928,920.00 USD | 0.00 USD | 41,150.00 USD | `-21.66%` | `909.29` |
| `Live` | `Long` | `45.35` | 887,770.00 USD | 0.00 USD | 2,180.00 USD | `-21.49%` | `48.02` |
| `Live` | `Long` | `45.45` | 885,590.00 USD | 0.00 USD | 23,940.00 USD | `-21.32%` | `526.65` |
| `Live` | `Long` | `45.55` | 861,660.00 USD | 0.00 USD | 7,820.00 USD | `-21.14%` | `171.57` |
| `Live` | `Long` | `45.95` | 853,840.00 USD | 0.00 USD | 704.87 USD | `-20.45%` | `15.34` |
| `Live` | `Long` | `46.05` | 853,140.00 USD | 0.00 USD | 9,710.00 USD | `-20.28%` | `210.95` |
| `Live` | `Long` | `46.25` | 843,420.00 USD | 0.00 USD | 39,320.00 USD | `-19.93%` | `850.21` |
| `Live` | `Long` | `46.35` | 804,100.00 USD | 0.00 USD | 383.78 USD | `-19.76%` | `8.28` |
| `Live` | `Long` | `46.65` | 803,720.00 USD | 0.00 USD | 936.73 USD | `-19.24%` | `20.08` |
| `Live` | `Long` | `46.85` | 802,780.00 USD | 0.00 USD | 1,300.00 USD | `-18.89%` | `27.72` |
| `Live` | `Long` | `46.95` | 801,480.00 USD | 0.00 USD | 11,860.00 USD | `-18.72%` | `252.68` |
| `Live` | `Long` | `47.15` | 789,620.00 USD | 0.00 USD | 1,980.00 USD | `-18.37%` | `42.07` |
| `Live` | `Long` | `47.25` | 787,630.00 USD | 0.00 USD | 1,050.00 USD | `-18.20%` | `22.15` |
| `Live` | `Long` | `47.35` | 786,590.00 USD | 0.00 USD | 2,600.00 USD | `-18.03%` | `55.00` |
| `Live` | `Long` | `47.45` | 783,980.00 USD | 0.00 USD | 2,180.00 USD | `-17.86%` | `45.94` |
| `Live` | `Long` | `47.55` | 781,800.00 USD | 0.00 USD | 1,770.00 USD | `-17.68%` | `37.28` |
| `Live` | `Long` | `47.75` | 780,030.00 USD | 0.00 USD | 4,780.00 USD | `-17.34%` | `100.00` |
| `Live` | `Long` | `47.95` | 775,260.00 USD | 0.00 USD | 2,420.00 USD | `-16.99%` | `50.39` |
| `Live` | `Long` | `48.05` | 772,840.00 USD | 0.00 USD | 1,860.00 USD | `-16.82%` | `38.61` |
| `Live` | `Long` | `48.15` | 770,980.00 USD | 0.00 USD | 2,680.00 USD | `-16.64%` | `55.56` |
| `Live` | `Long` | `48.25` | 768,310.00 USD | 0.00 USD | 4,390.00 USD | `-16.47%` | `90.89` |
| `Live` | `Long` | `48.35` | 763,920.00 USD | 0.00 USD | 263.02 USD | `-16.30%` | `5.44` |
| `Live` | `Long` | `48.55` | 763,660.00 USD | 0.00 USD | 2,030.00 USD | `-15.95%` | `41.85` |
| `Live` | `Long` | `48.65` | 761,630.00 USD | 0.00 USD | 273.90 USD | `-15.78%` | `5.63` |
| `Live` | `Long` | `48.75` | 761,360.00 USD | 0.00 USD | 231.56 USD | `-15.60%` | `4.75` |
| `Live` | `Long` | `48.95` | 761,120.00 USD | 0.00 USD | 1,390.00 USD | `-15.26%` | `28.33` |
| `Live` | `Long` | `49.05` | 759,740.00 USD | 0.00 USD | 1,580.00 USD | `-15.09%` | `32.25` |
| `Live` | `Long` | `49.15` | 758,160.00 USD | 0.00 USD | 5,740.00 USD | `-14.91%` | `116.83` |
| `Live` | `Long` | `49.35` | 752,410.00 USD | 0.00 USD | 5,230.00 USD | `-14.57%` | `105.97` |
| `Live` | `Long` | `49.45` | 747,180.00 USD | 0.00 USD | 2,500.00 USD | `-14.39%` | `50.51` |
| `Live` | `Long` | `49.55` | 744,690.00 USD | 0.00 USD | 18,010.00 USD | `-14.22%` | `363.57` |
| `Live` | `Long` | `49.65` | 726,670.00 USD | 0.00 USD | 12,030.00 USD | `-14.05%` | `242.33` |
| `Live` | `Long` | `49.75` | 714,640.00 USD | 0.00 USD | 1,250.00 USD | `-13.87%` | `25.06` |
| `Live` | `Long` | `49.95` | 713,390.00 USD | 0.00 USD | 28,540.00 USD | `-13.53%` | `571.31` |
| `Live` | `Long` | `50.05` | 684,860.00 USD | 0.00 USD | 1,820.00 USD | `-13.35%` | `36.43` |
| `Live` | `Long` | `50.15` | 683,030.00 USD | 0.00 USD | 19,460.00 USD | `-13.18%` | `388.12` |
| `Live` | `Long` | `50.25` | 663,570.00 USD | 0.00 USD | 102.51 USD | `-13.01%` | `2.04` |
| `Live` | `Long` | `50.35` | 663,470.00 USD | 0.00 USD | 1,030.00 USD | `-12.83%` | `20.49` |
| `Live` | `Long` | `50.45` | 662,430.00 USD | 0.00 USD | 4,720.00 USD | `-12.66%` | `93.64` |
| `Live` | `Long` | `50.55` | 657,710.00 USD | 0.00 USD | 84,100.00 USD | `-12.49%` | `1,663.61` |
| `Live` | `Long` | `50.65` | 573,610.00 USD | 0.00 USD | 15,930.00 USD | `-12.32%` | `314.44` |
| `Live` | `Long` | `50.75` | 557,690.00 USD | 0.00 USD | 9,050.00 USD | `-12.14%` | `178.28` |
| `Live` | `Long` | `50.95` | 548,640.00 USD | 0.00 USD | 245.07 USD | `-11.80%` | `4.81` |
| `Live` | `Long` | `51.15` | 548,400.00 USD | 0.00 USD | 219,370.00 USD | `-11.45%` | `4,288.79` |
| `Live` | `Long` | `51.35` | 329,020.00 USD | 0.00 USD | 3,340.00 USD | `-11.10%` | `65.00` |
| `Live` | `Long` | `51.45` | 325,690.00 USD | 0.00 USD | 22,270.00 USD | `-10.93%` | `432.80` |
| `Live` | `Long` | `51.55` | 303,420.00 USD | 0.00 USD | 551.07 USD | `-10.76%` | `10.69` |
| `Live` | `Long` | `51.65` | 302,870.00 USD | 0.00 USD | 155.47 USD | `-10.58%` | `3.01` |
| `Live` | `Long` | `51.75` | 302,710.00 USD | 0.00 USD | 6,450.00 USD | `-10.41%` | `124.64` |
| `Live` | `Long` | `51.85` | 296,260.00 USD | 0.00 USD | 3,580.00 USD | `-10.24%` | `69.10` |
| `Live` | `Long` | `51.95` | 292,680.00 USD | 0.00 USD | 12,070.00 USD | `-10.07%` | `232.41` |
| `Live` | `Long` | `52.25` | 280,600.00 USD | 0.00 USD | 179.22 USD | `-9.55%` | `3.43` |
| `Live` | `Long` | `52.35` | 280,430.00 USD | 0.00 USD | 27,650.00 USD | `-9.37%` | `528.09` |
| `Live` | `Long` | `52.45` | 252,780.00 USD | 0.00 USD | 3,830.00 USD | `-9.20%` | `72.95` |
| `Live` | `Long` | `52.55` | 248,950.00 USD | 0.00 USD | 8,700.00 USD | `-9.03%` | `165.49` |
| `Live` | `Long` | `52.75` | 240,260.00 USD | 0.00 USD | 7,450.00 USD | `-8.68%` | `141.16` |
| `Live` | `Long` | `52.85` | 232,810.00 USD | 0.00 USD | 5,950.00 USD | `-8.51%` | `112.64` |
| `Live` | `Long` | `52.95` | 226,860.00 USD | 0.00 USD | 11,680.00 USD | `-8.33%` | `220.59` |
| `Live` | `Long` | `53.05` | 215,180.00 USD | 0.00 USD | 900.26 USD | `-8.16%` | `16.97` |
| `Live` | `Long` | `53.15` | 214,280.00 USD | 0.00 USD | 22,150.00 USD | `-7.99%` | `416.71` |
| `Live` | `Long` | `53.25` | 192,130.00 USD | 0.00 USD | 1,500.00 USD | `-7.81%` | `28.15` |
| `Live` | `Long` | `53.35` | 190,630.00 USD | 0.00 USD | 1,910.00 USD | `-7.64%` | `35.71` |
| `Live` | `Long` | `53.45` | 188,730.00 USD | 0.00 USD | 4,880.00 USD | `-7.47%` | `91.21` |
| `Live` | `Long` | `53.65` | 183,850.00 USD | 0.00 USD | 533.82 USD | `-7.12%` | `9.95` |
| `Live` | `Long` | `53.75` | 183,320.00 USD | 0.00 USD | 332.71 USD | `-6.95%` | `6.19` |
| `Live` | `Long` | `53.85` | 182,980.00 USD | 0.00 USD | 2,130.00 USD | `-6.78%` | `39.58` |
| `Live` | `Long` | `53.95` | 180,850.00 USD | 0.00 USD | 50,550.00 USD | `-6.60%` | `937.06` |
| `Live` | `Long` | `54.05` | 130,300.00 USD | 0.00 USD | 219.44 USD | `-6.43%` | `4.06` |
| `Live` | `Long` | `54.15` | 130,080.00 USD | 0.00 USD | 13,210.00 USD | `-6.26%` | `243.97` |
| `Live` | `Long` | `54.25` | 116,870.00 USD | 0.00 USD | 2,400.00 USD | `-6.08%` | `44.18` |
| `Live` | `Long` | `54.45` | 114,470.00 USD | 0.00 USD | 12,640.00 USD | `-5.74%` | `232.06` |
| `Live` | `Long` | `54.55` | 101,840.00 USD | 0.00 USD | 2,470.00 USD | `-5.56%` | `45.19` |
| `Live` | `Long` | `54.65` | 99,370.00 USD | 0.00 USD | 2,380.00 USD | `-5.39%` | `43.63` |
| `Live` | `Long` | `54.75` | 96,990.00 USD | 0.00 USD | 470.85 USD | `-5.22%` | `8.60` |
| `Live` | `Long` | `54.85` | 96,510.00 USD | 0.00 USD | 167.29 USD | `-5.04%` | `3.05` |
| `Live` | `Long` | `54.95` | 96,350.00 USD | 0.00 USD | 7,220.00 USD | `-4.87%` | `131.47` |
| `Live` | `Long` | `55.05` | 89,120.00 USD | 0.00 USD | 394.71 USD | `-4.70%` | `7.17` |
| `Live` | `Long` | `55.15` | 88,730.00 USD | 0.00 USD | 3,710.00 USD | `-4.53%` | `67.31` |
| `Live` | `Long` | `55.25` | 85,020.00 USD | 0.00 USD | 1,660.00 USD | `-4.35%` | `30.00` |
| `Live` | `Long` | `55.35` | 83,360.00 USD | 0.00 USD | 1,610.00 USD | `-4.18%` | `29.05` |
| `Live` | `Long` | `55.45` | 81,750.00 USD | 0.00 USD | 424.19 USD | `-4.01%` | `7.65` |
| `Live` | `Long` | `55.55` | 81,330.00 USD | 0.00 USD | 3,100.00 USD | `-3.83%` | `55.74` |
| `Live` | `Long` | `56.15` | 78,230.00 USD | 0.00 USD | 78,230.00 USD | `-2.79%` | `1,393.24` |
| `Live` | `Short` | `60.75` | 1,040.00 USD | 1,040.00 USD | 0.00 USD | `+5.17%` | `17.16` |
| `Live` | `Short` | `60.95` | 1,840.00 USD | 794.18 USD | 0.00 USD | `+5.52%` | `13.03` |
| `Live` | `Short` | `61.05` | 2,320.00 USD | 482.91 USD | 0.00 USD | `+5.69%` | `7.91` |
| `Live` | `Short` | `61.15` | 6,190.00 USD | 3,870.00 USD | 0.00 USD | `+5.86%` | `63.26` |
| `Live` | `Short` | `61.65` | 217,390.00 USD | 211,210.00 USD | 0.00 USD | `+6.73%` | `3,425.89` |
| `Live` | `Short` | `65.95` | 218,550.00 USD | 1,160.00 USD | 0.00 USD | `+14.17%` | `17.59` |
| `Live` | `Short` | `66.05` | 220,750.00 USD | 2,200.00 USD | 0.00 USD | `+14.34%` | `33.31` |
| `Live` | `Short` | `66.85` | 254,700.00 USD | 33,950.00 USD | 0.00 USD | `+15.73%` | `507.83` |
| `Live` | `Short` | `66.95` | 254,820.00 USD | 121.18 USD | 0.00 USD | `+15.90%` | `1.81` |
| `Live` | `Short` | `67.85` | 255,530.00 USD | 709.03 USD | 0.00 USD | `+17.46%` | `10.45` |
| `Live` | `Short` | `69.45` | 255,950.00 USD | 414.62 USD | 0.00 USD | `+20.23%` | `5.97` |
| `Live` | `Short` | `70.45` | 261,210.00 USD | 5,270.00 USD | 0.00 USD | `+21.96%` | `74.74` |
| `Live` | `Short` | `73.15` | 261,880.00 USD | 667.86 USD | 0.00 USD | `+26.64%` | `9.13` |
| `Live` | `Short` | `76.35` | 270,260.00 USD | 8,380.00 USD | 0.00 USD | `+32.18%` | `109.80` |
| `Live` | `Short` | `77.85` | 270,870.00 USD | 602.56 USD | 0.00 USD | `+34.77%` | `7.74` |
| `Live` | `Short` | `77.95` | 271,000.00 USD | 136.41 USD | 0.00 USD | `+34.95%` | `1.75` |
| `Live` | `Short` | `80.75` | 271,650.00 USD | 646.00 USD | 0.00 USD | `+39.79%` | `8.00` |
| `Live` | `Short` | `81.05` | 290,650.00 USD | 19,000.00 USD | 0.00 USD | `+40.31%` | `234.42` |
| `Live` | `Short` | `81.55` | 290,770.00 USD | 123.96 USD | 0.00 USD | `+41.18%` | `1.52` |
| `Live` | `Short` | `82.65` | 294,620.00 USD | 3,850.00 USD | 0.00 USD | `+43.08%` | `46.61` |
| `Live` | `Short` | `82.75` | 294,840.00 USD | 214.32 USD | 0.00 USD | `+43.26%` | `2.59` |
| `Live` | `Short` | `84.65` | 295,700.00 USD | 862.58 USD | 0.00 USD | `+46.54%` | `10.19` |
| `Live` | `Short` | `85.25` | 298,520.00 USD | 2,810.00 USD | 0.00 USD | `+47.58%` | `33.00` |
| `Live` | `Short` | `85.55` | 321,340.00 USD | 22,830.00 USD | 0.00 USD | `+48.10%` | `266.81` |
| `Live` | `Short` | `86.65` | 324,810.00 USD | 3,470.00 USD | 0.00 USD | `+50.01%` | `40.00` |
| `Live` | `Short` | `96.55` | 327,220.00 USD | 2,410.00 USD | 0.00 USD | `+67.15%` | `25.00` |
| `Live` | `Short` | `97.75` | 328,260.00 USD | 1,040.00 USD | 0.00 USD | `+69.22%` | `10.63` |
| `Live` | `Short` | `98.75` | 328,930.00 USD | 674.46 USD | 0.00 USD | `+70.95%` | `6.83` |
| `Live` | `Short` | `104.85` | 682,700.00 USD | 353,760.00 USD | 0.00 USD | `+81.51%` | `3,374.01` |
| `Live` | `Short` | `106.05` | 703,910.00 USD | 21,210.00 USD | 0.00 USD | `+83.59%` | `200.00` |
| `Live` | `Short` | `110.45` | 704,040.00 USD | 131.44 USD | 0.00 USD | `+91.21%` | `1.19` |
| `Live` | `Short` | `110.55` | 705,160.00 USD | 1,120.00 USD | 0.00 USD | `+91.38%` | `10.11` |
| `Live` | `Short` | `110.65` | 709,990.00 USD | 4,830.00 USD | 0.00 USD | `+91.56%` | `43.66` |
| `Live` | `Short` | `110.95` | 710,650.00 USD | 664.59 USD | 0.00 USD | `+92.07%` | `5.99` |
| `Live` | `Short` | `111.65` | 732,980.00 USD | 22,330.00 USD | 0.00 USD | `+93.29%` | `200.00` |
| `Live` | `Short` | `114.65` | 733,400.00 USD | 420.77 USD | 0.00 USD | `+98.48%` | `3.67` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 491,980.00 USD | 0.00 USD | 392.18 USD | `-65.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 491,590.00 USD | 0.00 USD | 2,310.00 USD | `-61.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 489,280.00 USD | 0.00 USD | 122.24 USD | `-56.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 489,160.00 USD | 0.00 USD | 1,560.00 USD | `-56.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 487,600.00 USD | 0.00 USD | 410.25 USD | `-52.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 487,190.00 USD | 0.00 USD | 281.57 USD | `-47.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 486,910.00 USD | 0.00 USD | 36,050.00 USD | `-37.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 450,860.00 USD | 0.00 USD | 37,550.00 USD | `-34.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 413,310.00 USD | 0.00 USD | 447.01 USD | `-34.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 412,860.00 USD | 0.00 USD | 40,560.00 USD | `-32.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 372,310.00 USD | 0.00 USD | 489.57 USD | `-31.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 371,820.00 USD | 0.00 USD | 1,550.00 USD | `-30.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 370,260.00 USD | 0.00 USD | 9,500.00 USD | `-30.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 360,760.00 USD | 0.00 USD | 2,060.00 USD | `-29.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 358,700.00 USD | 0.00 USD | 2,960.00 USD | `-28.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 355,750.00 USD | 0.00 USD | 6,050.00 USD | `-27.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 349,700.00 USD | 0.00 USD | 5,680.00 USD | `-25.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 344,020.00 USD | 0.00 USD | 672.22 USD | `-24.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 343,340.00 USD | 0.00 USD | 213.80 USD | `-23.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 343,130.00 USD | 0.00 USD | 223.20 USD | `-22.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 342,910.00 USD | 0.00 USD | 391.13 USD | `-22.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 342,520.00 USD | 0.00 USD | 7,080.00 USD | `-22.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 335,440.00 USD | 0.00 USD | 1,370.00 USD | `-21.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 334,070.00 USD | 0.00 USD | 553.80 USD | `-20.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 333,520.00 USD | 0.00 USD | 14,000.00 USD | `-19.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 319,520.00 USD | 0.00 USD | 158.56 USD | `-18.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 319,360.00 USD | 0.00 USD | 373.28 USD | `-18.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 318,990.00 USD | 0.00 USD | 849.46 USD | `-18.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 318,140.00 USD | 0.00 USD | 1,150.00 USD | `-16.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 316,990.00 USD | 0.00 USD | 1,740.00 USD | `-15.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 315,250.00 USD | 0.00 USD | 981.00 USD | `-15.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 314,270.00 USD | 0.00 USD | 1,150.00 USD | `-14.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 313,120.00 USD | 0.00 USD | 298.20 USD | `-13.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 312,820.00 USD | 0.00 USD | 14,650.00 USD | `-13.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 298,170.00 USD | 0.00 USD | 6,410.00 USD | `-13.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 291,760.00 USD | 0.00 USD | 459.70 USD | `-12.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 291,300.00 USD | 0.00 USD | 1,020.00 USD | `-11.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 290,280.00 USD | 0.00 USD | 439.89 USD | `-11.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 289,840.00 USD | 0.00 USD | 3,700.00 USD | `-10.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 286,140.00 USD | 0.00 USD | 27,730.00 USD | `-9.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 258,410.00 USD | 0.00 USD | 51,800.00 USD | `-9.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 206,610.00 USD | 0.00 USD | 10,530.00 USD | `-8.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 196,080.00 USD | 0.00 USD | 271.13 USD | `-8.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 195,800.00 USD | 0.00 USD | 5,050.00 USD | `-8.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 190,760.00 USD | 0.00 USD | 1,060.00 USD | `-8.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 189,700.00 USD | 0.00 USD | 460.81 USD | `-7.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 189,240.00 USD | 0.00 USD | 184.21 USD | `-7.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 189,050.00 USD | 0.00 USD | 1,370.00 USD | `-7.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 187,680.00 USD | 0.00 USD | 462.03 USD | `-6.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 187,220.00 USD | 0.00 USD | 601.58 USD | `-6.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 186,620.00 USD | 0.00 USD | 3,090.00 USD | `-6.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 183,530.00 USD | 0.00 USD | 156.53 USD | `-5.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.45` | 183,370.00 USD | 0.00 USD | 570.09 USD | `-5.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.55` | 182,800.00 USD | 0.00 USD | 1,690.00 USD | `-5.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.65` | 181,110.00 USD | 0.00 USD | 4,110.00 USD | `-5.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 177,010.00 USD | 0.00 USD | 33,280.00 USD | `-5.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.95` | 143,730.00 USD | 0.00 USD | 1,630.00 USD | `-4.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 142,100.00 USD | 0.00 USD | 1,580.00 USD | `-4.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.25` | 140,520.00 USD | 0.00 USD | 429.85 USD | `-4.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.35` | 140,090.00 USD | 0.00 USD | 2,140.00 USD | `-4.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.55` | 137,950.00 USD | 0.00 USD | 113.88 USD | `-3.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.65` | 137,840.00 USD | 0.00 USD | 4,930.00 USD | `-3.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.75` | 132,910.00 USD | 0.00 USD | 1,820.00 USD | `-3.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.85` | 131,090.00 USD | 0.00 USD | 196.59 USD | `-3.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.95` | 130,900.00 USD | 0.00 USD | 193.03 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 130,700.00 USD | 0.00 USD | 587.96 USD | `-2.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 130,120.00 USD | 0.00 USD | 1,070.00 USD | `-2.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.35` | 129,040.00 USD | 0.00 USD | 78,570.00 USD | `-2.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.45` | 50,470.00 USD | 0.00 USD | 694.90 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.55` | 49,780.00 USD | 0.00 USD | 2,640.00 USD | `-2.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.65` | 47,140.00 USD | 0.00 USD | 1,230.00 USD | `-1.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.75` | 45,910.00 USD | 0.00 USD | 228.70 USD | `-1.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.85` | 45,680.00 USD | 0.00 USD | 17,830.00 USD | `-1.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.95` | 27,840.00 USD | 0.00 USD | 390.68 USD | `-1.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.05` | 27,450.00 USD | 0.00 USD | 5,800.00 USD | `-1.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.15` | 21,650.00 USD | 0.00 USD | 392.05 USD | `-1.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.25` | 21,260.00 USD | 0.00 USD | 196.37 USD | `-0.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.45` | 21,060.00 USD | 0.00 USD | 344.70 USD | `-0.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.55` | 20,720.00 USD | 0.00 USD | 20,360.00 USD | `-0.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.65` | 359.50 USD | 0.00 USD | 160.27 USD | `-0.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.75` | 199.24 USD | 0.00 USD | 199.24 USD | `-0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.85` | 392.22 USD | 392.22 USD | 0.00 USD | `+0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.95` | 520.87 USD | 128.65 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 2,500.00 USD | 1,980.00 USD | 0.00 USD | `+0.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 3,210.00 USD | 706.52 USD | 0.00 USD | `+0.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 4,290.00 USD | 1,080.00 USD | 0.00 USD | `+0.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 4,410.00 USD | 123.70 USD | 0.00 USD | `+1.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 5,010.00 USD | 601.45 USD | 0.00 USD | `+1.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 5,410.00 USD | 401.65 USD | 0.00 USD | `+1.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.65` | 5,690.00 USD | 274.48 USD | 0.00 USD | `+1.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 5,810.00 USD | 124.55 USD | 0.00 USD | `+1.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 8,760.00 USD | 2,940.00 USD | 0.00 USD | `+1.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 13,850.00 USD | 5,100.00 USD | 0.00 USD | `+2.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 18,650.00 USD | 4,800.00 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 19,930.00 USD | 1,280.00 USD | 0.00 USD | `+2.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.25` | 20,240.00 USD | 307.51 USD | 0.00 USD | `+2.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 20,700.00 USD | 461.74 USD | 0.00 USD | `+2.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 20,900.00 USD | 200.35 USD | 0.00 USD | `+2.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.55` | 21,400.00 USD | 496.65 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 22,120.00 USD | 724.75 USD | 0.00 USD | `+3.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.75` | 22,240.00 USD | 113.53 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 22,400.00 USD | 158.00 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.95` | 37,760.00 USD | 15,360.00 USD | 0.00 USD | `+3.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 38,750.00 USD | 987.82 USD | 0.00 USD | `+3.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.15` | 40,550.00 USD | 1,800.00 USD | 0.00 USD | `+4.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 41,100.00 USD | 551.00 USD | 0.00 USD | `+4.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.45` | 325,210.00 USD | 284,100.00 USD | 0.00 USD | `+4.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 326,090.00 USD | 878.58 USD | 0.00 USD | `+4.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 327,470.00 USD | 1,390.00 USD | 0.00 USD | `+5.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.75` | 327,880.00 USD | 407.63 USD | 0.00 USD | `+5.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 329,070.00 USD | 1,190.00 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 329,960.00 USD | 882.56 USD | 0.00 USD | `+5.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 332,320.00 USD | 2,360.00 USD | 0.00 USD | `+5.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 332,440.00 USD | 125.56 USD | 0.00 USD | `+6.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.35` | 332,680.00 USD | 236.20 USD | 0.00 USD | `+6.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 336,280.00 USD | 3,600.00 USD | 0.00 USD | `+6.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 336,920.00 USD | 643.20 USD | 0.00 USD | `+6.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.95` | 339,040.00 USD | 2,120.00 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 339,150.00 USD | 106.11 USD | 0.00 USD | `+7.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.25` | 339,260.00 USD | 117.03 USD | 0.00 USD | `+7.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.45` | 339,480.00 USD | 217.95 USD | 0.00 USD | `+8.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.55` | 339,830.00 USD | 347.15 USD | 0.00 USD | `+8.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 340,550.00 USD | 716.72 USD | 0.00 USD | `+8.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.75` | 340,690.00 USD | 141.19 USD | 0.00 USD | `+8.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 342,030.00 USD | 1,340.00 USD | 0.00 USD | `+9.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 342,930.00 USD | 900.52 USD | 0.00 USD | `+9.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 343,630.00 USD | 703.97 USD | 0.00 USD | `+9.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.35` | 343,770.00 USD | 140.64 USD | 0.00 USD | `+9.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 344,440.00 USD | 668.13 USD | 0.00 USD | `+9.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 348,990.00 USD | 4,550.00 USD | 0.00 USD | `+10.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 349,550.00 USD | 555.03 USD | 0.00 USD | `+10.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 350,080.00 USD | 531.62 USD | 0.00 USD | `+10.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 350,280.00 USD | 202.69 USD | 0.00 USD | `+11.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 350,580.00 USD | 298.04 USD | 0.00 USD | `+11.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 350,680.00 USD | 102.13 USD | 0.00 USD | `+12.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 351,220.00 USD | 540.09 USD | 0.00 USD | `+12.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 351,320.00 USD | 100.79 USD | 0.00 USD | `+13.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 351,580.00 USD | 262.20 USD | 0.00 USD | `+13.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.65` | 351,900.00 USD | 315.12 USD | 0.00 USD | `+13.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 352,270.00 USD | 371.49 USD | 0.00 USD | `+13.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.85` | 353,150.00 USD | 881.07 USD | 0.00 USD | `+14.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 353,850.00 USD | 696.17 USD | 0.00 USD | `+14.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 354,380.00 USD | 534.00 USD | 0.00 USD | `+15.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 365,460.00 USD | 11,080.00 USD | 0.00 USD | `+15.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 378,870.00 USD | 13,410.00 USD | 0.00 USD | `+16.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.05` | 381,230.00 USD | 2,360.00 USD | 0.00 USD | `+17.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 386,100.00 USD | 4,860.00 USD | 0.00 USD | `+18.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 386,300.00 USD | 204.48 USD | 0.00 USD | `+20.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 387,230.00 USD | 929.64 USD | 0.00 USD | `+21.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 707,120.00 USD | 319,890.00 USD | 0.00 USD | `+21.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 707,290.00 USD | 170.04 USD | 0.00 USD | `+22.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 713,060.00 USD | 5,770.00 USD | 0.00 USD | `+22.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 713,620.00 USD | 555.61 USD | 0.00 USD | `+23.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 714,770.00 USD | 1,150.00 USD | 0.00 USD | `+24.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 717,470.00 USD | 2,700.00 USD | 0.00 USD | `+24.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 717,630.00 USD | 156.78 USD | 0.00 USD | `+25.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 720,850.00 USD | 3,220.00 USD | 0.00 USD | `+25.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 721,260.00 USD | 411.14 USD | 0.00 USD | `+27.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 844,450.00 USD | 123,190.00 USD | 0.00 USD | `+28.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 845,470.00 USD | 1,020.00 USD | 0.00 USD | `+29.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 845,570.00 USD | 104.93 USD | 0.00 USD | `+29.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 845,970.00 USD | 392.51 USD | 0.00 USD | `+29.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 846,370.00 USD | 402.59 USD | 0.00 USD | `+30.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 846,680.00 USD | 315.18 USD | 0.00 USD | `+33.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 905,990.00 USD | 59,310.00 USD | 0.00 USD | `+36.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 909,150.00 USD | 3,160.00 USD | 0.00 USD | `+36.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 914,840.00 USD | 5,690.00 USD | 0.00 USD | `+38.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 952,460.00 USD | 37,620.00 USD | 0.00 USD | `+38.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 952,900.00 USD | 433.89 USD | 0.00 USD | `+40.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 993,590.00 USD | 40,700.00 USD | 0.00 USD | `+40.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 993,760.00 USD | 164.10 USD | 0.00 USD | `+42.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 994,300.00 USD | 546.81 USD | 0.00 USD | `+43.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 996,610.00 USD | 2,300.00 USD | 0.00 USD | `+45.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 1,010,000.00 USD | 12,070.00 USD | 0.00 USD | `+47.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.75` | 1,020,000.00 USD | 12,330.00 USD | 0.00 USD | `+48.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.25` | 1,020,000.00 USD | 435.38 USD | 0.00 USD | `+51.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 1,020,000.00 USD | 1,580.00 USD | 0.00 USD | `+52.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 1,060,000.00 USD | 37,000.00 USD | 0.00 USD | `+52.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 1,060,000.00 USD | 473.21 USD | 0.00 USD | `+53.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 1,060,000.00 USD | 1,270.00 USD | 0.00 USD | `+54.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 1,060,000.00 USD | 1,630.00 USD | 0.00 USD | `+54.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 1,080,000.00 USD | 21,060.00 USD | 0.00 USD | `+55.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 1,080,000.00 USD | 481.55 USD | 0.00 USD | `+58.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 1,090,000.00 USD | 1,330.00 USD | 0.00 USD | `+59.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 1,090,000.00 USD | 188.10 USD | 0.00 USD | `+62.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,350,000.00 USD | 266,140.00 USD | 0.00 USD | `+64.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,360,000.00 USD | 3,400.00 USD | 0.00 USD | `+65.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,380,000.00 USD | 21,930.00 USD | 0.00 USD | `+66.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,380,000.00 USD | 294.15 USD | 0.00 USD | `+69.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,380,000.00 USD | 4,010.00 USD | 0.00 USD | `+73.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,380,000.00 USD | 306.15 USD | 0.00 USD | `+76.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,380,000.00 USD | 936.72 USD | 0.00 USD | `+78.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,390,000.00 USD | 2,920.00 USD | 0.00 USD | `+78.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,390,000.00 USD | 324.15 USD | 0.00 USD | `+87.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 1,390,000.00 USD | 123.23 USD | 0.00 USD | `+88.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 1,480,000.00 USD | 89,110.00 USD | 0.00 USD | `+92.25%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `51.40` | 18,890,000.00 USD | 0.00 USD | 18,890,000.00 USD | 87,100.00 USD | 41,450.00 USD | 92,230.00 USD |
| `7D` | `51.50` | 18,670,000.00 USD | 0.00 USD | 18,670,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD |
| `7D` | `51.60` | 18,580,000.00 USD | 0.00 USD | 18,580,000.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD |
| `1D` | `51.70` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 11,140.00 USD | 11,120.00 USD | 11,370.00 USD |
| `7D` | `51.70` | 18,510,000.00 USD | 0.00 USD | 18,510,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `51.80` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 12,120.00 USD | 2,040.00 USD | 10,050.00 USD |
| `7D` | `51.80` | 18,480,000.00 USD | 0.00 USD | 18,480,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD |
| `1D` | `51.90` | 5,780,000.00 USD | 0.00 USD | 5,780,000.00 USD | 12,520.00 USD | 21,470.00 USD | 9,190.00 USD |
| `7D` | `51.90` | 18,420,000.00 USD | 0.00 USD | 18,420,000.00 USD | 5,870.00 USD | 15,810.00 USD | 4,760.00 USD |
| `1D` | `52.00` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 23,390.00 USD | 8,230.00 USD | 23,340.00 USD |
| `7D` | `52.00` | 18,390,000.00 USD | 0.00 USD | 18,390,000.00 USD | 64,300.00 USD | 20,800.00 USD | 11,880.00 USD |
| `1D` | `52.10` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 27,580.00 USD | 5,780.00 USD | 35,220.00 USD |
| `7D` | `52.10` | 18,300,000.00 USD | 0.00 USD | 18,300,000.00 USD | 24,220.00 USD | 18,810.00 USD | 35,480.00 USD |
| `1D` | `52.20` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 18,580.00 USD | 10,410.00 USD | 14,390.00 USD |
| `7D` | `52.20` | 18,220,000.00 USD | 0.00 USD | 18,220,000.00 USD | 35,740.00 USD | 4,340.00 USD | 25,270.00 USD |
| `1D` | `52.30` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 33,360.00 USD | 8,170.00 USD | 16,110.00 USD |
| `7D` | `52.30` | 18,150,000.00 USD | 0.00 USD | 18,150,000.00 USD | 14,070.00 USD | 12,840.00 USD | 8,940.00 USD |
| `1D` | `52.40` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 7,880.00 USD | 6,900.00 USD | 6,280.00 USD |
| `7D` | `52.40` | 18,120,000.00 USD | 0.00 USD | 18,120,000.00 USD | 20,580.00 USD | 11,230.00 USD | 20,050.00 USD |
| `1D` | `52.50` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 13,740.00 USD | 5,360.00 USD | 80.02 USD |
| `7D` | `52.50` | 18,070,000.00 USD | 0.00 USD | 18,070,000.00 USD | 33,240.00 USD | 667.05 USD | 10,640.00 USD |
| `1D` | `52.60` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 2,760.00 USD | 8,200.00 USD | 273.52 USD |
| `7D` | `52.60` | 18,020,000.00 USD | 0.00 USD | 18,020,000.00 USD | 36,640.00 USD | 14,530.00 USD | 584.77 USD |
| `1D` | `52.70` | 5,460,000.00 USD | 0.00 USD | 5,460,000.00 USD | 4,310.00 USD | 7,610.00 USD | 13,520.00 USD |
| `7D` | `52.70` | 17,970,000.00 USD | 0.00 USD | 17,970,000.00 USD | 20,250.00 USD | 27,720.00 USD | 42,430.00 USD |
| `1D` | `52.80` | 5,440,000.00 USD | 0.00 USD | 5,440,000.00 USD | 14,400.00 USD | 2,680.00 USD | 11,200.00 USD |
| `7D` | `52.80` | 17,880,000.00 USD | 0.00 USD | 17,880,000.00 USD | 46,600.00 USD | 14,180.00 USD | 108.50 USD |
| `1D` | `52.90` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 28,000.00 USD | 465.85 USD | 6,120.00 USD |
| `7D` | `52.90` | 17,820,000.00 USD | 0.00 USD | 17,820,000.00 USD | 51,920.00 USD | 23,030.00 USD | 3,870.00 USD |
| `1D` | `53.00` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 3,880.00 USD | 2,200.00 USD | 936.80 USD |
| `7D` | `53.00` | 17,740,000.00 USD | 0.00 USD | 17,740,000.00 USD | 18,990.00 USD | 8,880.00 USD | 32,670.00 USD |
| `1D` | `53.10` | 5,370,000.00 USD | 0.00 USD | 5,370,000.00 USD | 9,600.00 USD | 2,540.00 USD | 780.78 USD |
| `7D` | `53.10` | 17,680,000.00 USD | 0.00 USD | 17,680,000.00 USD | 51,920.00 USD | 29,200.00 USD | 9,860.00 USD |
| `1D` | `53.20` | 5,360,000.00 USD | 0.00 USD | 5,360,000.00 USD | 8,730.00 USD | 7,180.00 USD | 6,370.00 USD |
| `7D` | `53.20` | 17,590,000.00 USD | 0.00 USD | 17,590,000.00 USD | 90,340.00 USD | 17,580.00 USD | 25,530.00 USD |
| `1D` | `53.30` | 5,330,000.00 USD | 0.00 USD | 5,330,000.00 USD | 10,170.00 USD | 4,410.00 USD | 7,610.00 USD |
| `7D` | `53.30` | 17,450,000.00 USD | 0.00 USD | 17,450,000.00 USD | 63,050.00 USD | 14,250.00 USD | 37,140.00 USD |
| `1D` | `53.40` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 18,620.00 USD | 3,050.00 USD | 11,520.00 USD |
| `7D` | `53.40` | 17,340,000.00 USD | 0.00 USD | 17,340,000.00 USD | 49,250.00 USD | 4,350.00 USD | 48,070.00 USD |
| `1D` | `53.50` | 5,280,000.00 USD | 0.00 USD | 5,280,000.00 USD | 9,130.00 USD | 2,350.00 USD | 83.29 USD |
| `7D` | `53.50` | 17,240,000.00 USD | 0.00 USD | 17,240,000.00 USD | 50,210.00 USD | 13,810.00 USD | 22,130.00 USD |
| `1D` | `53.60` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 20,020.00 USD | 5,030.00 USD | 10,180.00 USD |
| `7D` | `53.60` | 17,150,000.00 USD | 0.00 USD | 17,150,000.00 USD | 53,580.00 USD | 8,450.00 USD | 10,670.00 USD |
| `1D` | `53.70` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 5,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `53.70` | 17,080,000.00 USD | 0.00 USD | 17,080,000.00 USD | 64,150.00 USD | 15,090.00 USD | 12,040.00 USD |
| `1D` | `53.80` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 1,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `53.80` | 16,990,000.00 USD | 0.00 USD | 16,990,000.00 USD | 99,150.00 USD | 48,300.00 USD | 86,270.00 USD |
| `1D` | `53.90` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 7,480.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `53.90` | 16,750,000.00 USD | 0.00 USD | 16,750,000.00 USD | 111,970.00 USD | 25,310.00 USD | 123,850.00 USD |
| `1D` | `54.00` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 3,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.00` | 16,490,000.00 USD | 0.00 USD | 16,490,000.00 USD | 344,710.00 USD | 142,130.00 USD | 210,440.00 USD |
| `1D` | `54.10` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 9,530.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.10` | 15,800,000.00 USD | 0.00 USD | 15,800,000.00 USD | 232,410.00 USD | 45,470.00 USD | 138,110.00 USD |
| `1D` | `54.20` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 14,770.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.20` | 15,380,000.00 USD | 0.00 USD | 15,380,000.00 USD | 234,980.00 USD | 141,240.00 USD | 133,320.00 USD |
| `1D` | `54.30` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 4,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.30` | 14,870,000.00 USD | 0.00 USD | 14,870,000.00 USD | 245,850.00 USD | 89,080.00 USD | 257,030.00 USD |
| `1D` | `54.40` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 2,750.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.40` | 14,280,000.00 USD | 0.00 USD | 14,280,000.00 USD | 319,640.00 USD | 106,460.00 USD | 105,880.00 USD |
| `1D` | `54.50` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 3,040.00 USD | 126.10 USD | 0.00 USD |
| `7D` | `54.50` | 13,750,000.00 USD | 0.00 USD | 13,750,000.00 USD | 169,910.00 USD | 53,460.00 USD | 142,750.00 USD |
| `1D` | `54.60` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 2,510.00 USD | 601.45 USD | 944.92 USD |
| `7D` | `54.60` | 13,380,000.00 USD | 0.00 USD | 13,380,000.00 USD | 111,350.00 USD | 43,430.00 USD | 73,330.00 USD |
| `1D` | `54.70` | 5,170,000.00 USD | 0.00 USD | 5,170,000.00 USD | 48,030.00 USD | 15,810.00 USD | 52,670.00 USD |
| `7D` | `54.70` | 13,150,000.00 USD | 0.00 USD | 13,150,000.00 USD | 122,080.00 USD | 50,560.00 USD | 172,060.00 USD |
| `1D` | `54.80` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 46,570.00 USD | 18,410.00 USD | 26,940.00 USD |
| `7D` | `54.80` | 12,810,000.00 USD | 0.00 USD | 12,810,000.00 USD | 307,590.00 USD | 104,820.00 USD | 156,690.00 USD |
| `1D` | `54.90` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 52,330.00 USD | 21,230.00 USD | 5,570.00 USD |
| `7D` | `54.90` | 12,240,000.00 USD | 0.00 USD | 12,240,000.00 USD | 256,370.00 USD | 162,220.00 USD | 276,830.00 USD |
| `1D` | `55.00` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 39,320.00 USD | 24,110.00 USD | 12,080.00 USD |
| `7D` | `55.00` | 11,540,000.00 USD | 0.00 USD | 11,540,000.00 USD | 269,610.00 USD | 81,220.00 USD | 310,900.00 USD |
| `1D` | `55.10` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 24,090.00 USD | 10,460.00 USD | 18,440.00 USD |
| `7D` | `55.10` | 10,880,000.00 USD | 0.00 USD | 10,880,000.00 USD | 362,320.00 USD | 145,730.00 USD | 171,990.00 USD |
| `1D` | `55.20` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 17,880.00 USD | 4,030.00 USD | 10,870.00 USD |
| `7D` | `55.20` | 10,200,000.00 USD | 0.00 USD | 10,200,000.00 USD | 338,950.00 USD | 177,110.00 USD | 279,820.00 USD |
| `1D` | `55.30` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 28,540.00 USD | 7,260.00 USD | 24,210.00 USD |
| `7D` | `55.30` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 367,680.00 USD | 68,970.00 USD | 256,640.00 USD |
| `1D` | `55.40` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 35,570.00 USD | 61,990.00 USD | 31,340.00 USD |
| `7D` | `55.40` | 8,710,000.00 USD | 0.00 USD | 8,710,000.00 USD | 302,780.00 USD | 188,590.00 USD | 249,120.00 USD |
| `1D` | `55.50` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 70,830.00 USD | 28,530.00 USD | 66,840.00 USD |
| `7D` | `55.50` | 7,970,000.00 USD | 0.00 USD | 7,970,000.00 USD | 329,130.00 USD | 186,800.00 USD | 529,720.00 USD |
| `1D` | `55.60` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 95,580.00 USD | 23,020.00 USD | 93,140.00 USD |
| `7D` | `55.60` | 6,930,000.00 USD | 0.00 USD | 6,930,000.00 USD | 426,340.00 USD | 261,500.00 USD | 277,380.00 USD |
| `1D` | `55.70` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 77,300.00 USD | 36,250.00 USD | 47,540.00 USD |
| `7D` | `55.70` | 5,960,000.00 USD | 0.00 USD | 5,960,000.00 USD | 174,240.00 USD | 32,180.00 USD | 273,340.00 USD |
| `1D` | `55.80` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 118,840.00 USD | 29,840.00 USD | 42,220.00 USD |
| `7D` | `55.80` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 60,840.00 USD | 54,060.00 USD | 144,450.00 USD |
| `1D` | `55.90` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 110,070.00 USD | 50,820.00 USD | 130,300.00 USD |
| `7D` | `55.90` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 65,400.00 USD | 94,580.00 USD | 280,140.00 USD |
| `1D` | `56.00` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 125,000.00 USD | 52,160.00 USD | 56,070.00 USD |
| `7D` | `56.00` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 181,230.00 USD | 88,840.00 USD | 107,640.00 USD |
| `1D` | `56.10` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 98,040.00 USD | 63,650.00 USD | 11,820.00 USD |
| `7D` | `56.10` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 121,920.00 USD | 133,900.00 USD | 46,880.00 USD |
| `1D` | `56.20` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 72,300.00 USD | 58,350.00 USD | 62,000.00 USD |
| `7D` | `56.20` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 104,510.00 USD | 80,130.00 USD | 205,740.00 USD |
| `1D` | `56.30` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 47,900.00 USD | 38,230.00 USD | 37,220.00 USD |
| `7D` | `56.30` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 91,850.00 USD | 140,830.00 USD | 85,420.00 USD |
| `1D` | `56.40` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 185,180.00 USD | 31,390.00 USD | 126,560.00 USD |
| `7D` | `56.40` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 215,940.00 USD | 124,050.00 USD | 140,220.00 USD |
| `1D` | `56.50` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 76,980.00 USD | 130,940.00 USD | 65,020.00 USD |
| `7D` | `56.50` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 26,520.00 USD | 101,420.00 USD | 71,820.00 USD |
| `1D` | `56.60` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 161,590.00 USD | 64,600.00 USD | 135,640.00 USD |
| `7D` | `56.60` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 363,190.00 USD | 130,070.00 USD | 128,320.00 USD |
| `1D` | `56.70` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 198,110.00 USD | 66,620.00 USD | 208,930.00 USD |
| `7D` | `56.70` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 110,940.00 USD | 105,810.00 USD | 206,510.00 USD |
| `1D` | `56.80` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 175,040.00 USD | 85,530.00 USD | 115,680.00 USD |
| `7D` | `56.80` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 153,580.00 USD | 97,670.00 USD | 262,620.00 USD |
| `1D` | `56.90` | 965,230.00 USD | 0.00 USD | 965,230.00 USD | 280,920.00 USD | 56,960.00 USD | 109,060.00 USD |
| `7D` | `56.90` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 108,440.00 USD | 65,260.00 USD | 94,810.00 USD |
| `1D` | `57.00` | 518,300.00 USD | 0.00 USD | 518,300.00 USD | 34,380.00 USD | 24,060.00 USD | 44,710.00 USD |
| `7D` | `57.00` | 885,980.00 USD | 0.00 USD | 885,980.00 USD | 50,710.00 USD | 111,780.00 USD | 91,400.00 USD |
| `1D` | `57.10` | 415,140.00 USD | 0.00 USD | 415,140.00 USD | 73,260.00 USD | 25,570.00 USD | 4,390.00 USD |
| `7D` | `57.10` | 632,090.00 USD | 0.00 USD | 632,090.00 USD | 36,580.00 USD | 14,880.00 USD | 500.18 USD |
| `1D` | `57.20` | 311,930.00 USD | 0.00 USD | 311,930.00 USD | 27,530.00 USD | 40,100.00 USD | 256.90 USD |
| `7D` | `57.20` | 580,130.00 USD | 0.00 USD | 580,130.00 USD | 21,160.00 USD | 50,300.00 USD | 3,700.00 USD |
| `1D` | `57.30` | 244,040.00 USD | 0.00 USD | 244,040.00 USD | 0.00 USD | 15,520.00 USD | 51,900.00 USD |
| `7D` | `57.30` | 504,980.00 USD | 0.00 USD | 504,980.00 USD | 22,360.00 USD | 27,320.00 USD | 45,530.00 USD |
| `1D` | `57.40` | 176,620.00 USD | 0.00 USD | 176,620.00 USD | 19,650.00 USD | 26,470.00 USD | 673.96 USD |
| `7D` | `57.40` | 409,770.00 USD | 0.00 USD | 409,770.00 USD | 38,520.00 USD | 30,000.00 USD | 129,940.00 USD |
| `1D` | `57.50` | 129,820.00 USD | 0.00 USD | 129,820.00 USD | 80,510.00 USD | 12,870.00 USD | 36,450.00 USD |
| `7D` | `57.50` | 211,310.00 USD | 0.00 USD | 211,310.00 USD | 76,670.00 USD | 23,070.00 USD | 0.00 USD |
| `7D` | `57.60` | 111,570.00 USD | 0.00 USD | 111,570.00 USD | 70,040.00 USD | 15,090.00 USD | 26,440.00 USD |
| `1D` | `58.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `58.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `58.20` | 638.03 USD | 638.03 USD | 0.00 USD | 0.00 USD | 0.00 USD | 638.03 USD |
| `1D` | `58.40` | 24,790.00 USD | 24,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,150.00 USD |
| `7D` | `58.40` | 54,120.00 USD | 54,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 54,120.00 USD |
| `1D` | `58.50` | 94,910.00 USD | 94,910.00 USD | 0.00 USD | 48,820.00 USD | 20,920.00 USD | 379.22 USD |
| `7D` | `58.50` | 78,650.00 USD | 78,650.00 USD | 0.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD |
| `1D` | `58.70` | 103,330.00 USD | 103,330.00 USD | 0.00 USD | 0.00 USD | 8,070.00 USD | 355.85 USD |
| `7D` | `58.70` | 118,400.00 USD | 118,400.00 USD | 0.00 USD | 0.00 USD | 4,430.00 USD | 35,320.00 USD |
| `1D` | `58.80` | 174,400.00 USD | 174,400.00 USD | 0.00 USD | 32,920.00 USD | 14,520.00 USD | 23,630.00 USD |
| `7D` | `58.80` | 128,130.00 USD | 128,130.00 USD | 0.00 USD | 0.00 USD | 3,320.00 USD | 6,410.00 USD |
| `1D` | `58.90` | 372,240.00 USD | 372,240.00 USD | 0.00 USD | 11,180.00 USD | 123,990.00 USD | 62,670.00 USD |
| `7D` | `58.90` | 230,920.00 USD | 230,920.00 USD | 0.00 USD | 0.00 USD | 47,950.00 USD | 54,840.00 USD |
| `1D` | `59.00` | 704,650.00 USD | 704,650.00 USD | 0.00 USD | 141,660.00 USD | 57,070.00 USD | 133,690.00 USD |
| `7D` | `59.00` | 669,930.00 USD | 669,930.00 USD | 0.00 USD | 255,180.00 USD | 65,270.00 USD | 118,570.00 USD |
| `1D` | `59.10` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 189,650.00 USD | 46,160.00 USD | 186,290.00 USD |
| `7D` | `59.10` | 964,420.00 USD | 964,420.00 USD | 0.00 USD | 91,060.00 USD | 45,400.00 USD | 158,030.00 USD |
| `1D` | `59.20` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 153,040.00 USD | 72,590.00 USD | 96,020.00 USD |
| `7D` | `59.20` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 153,580.00 USD | 10,620.00 USD | 174,600.00 USD |
| `1D` | `59.30` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 283,630.00 USD | 73,090.00 USD | 133,320.00 USD |
| `7D` | `59.30` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD |
| `1D` | `59.40` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 78,510.00 USD | 56,810.00 USD | 76,850.00 USD |
| `7D` | `59.40` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 103,370.00 USD | 73,620.00 USD | 137,500.00 USD |
| `1D` | `59.50` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 114,880.00 USD | 51,920.00 USD | 9,950.00 USD |
| `7D` | `59.50` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 67,060.00 USD | 59,920.00 USD | 7,680.00 USD |
| `1D` | `59.60` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 62,260.00 USD | 66,510.00 USD | 13,440.00 USD |
| `7D` | `59.60` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 268,680.00 USD | 145,550.00 USD | 86,840.00 USD |
| `1D` | `59.70` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 20,820.00 USD | 30,710.00 USD | 94,130.00 USD |
| `7D` | `59.70` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 53,810.00 USD | 180,620.00 USD | 161,880.00 USD |
| `1D` | `59.80` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 40,180.00 USD | 38,670.00 USD | 11,550.00 USD |
| `7D` | `59.80` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 118,240.00 USD | 96,860.00 USD | 155,270.00 USD |
| `1D` | `59.90` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 112,870.00 USD | 21,840.00 USD | 90,050.00 USD |
| `7D` | `59.90` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 246,770.00 USD | 84,430.00 USD | 40,130.00 USD |
| `1D` | `60.00` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 182,690.00 USD | 65,010.00 USD | 78,300.00 USD |
| `7D` | `60.00` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 231,370.00 USD | 183,130.00 USD | 94,160.00 USD |
| `1D` | `60.10` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 91,380.00 USD | 42,440.00 USD | 71,530.00 USD |
| `7D` | `60.10` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 263,890.00 USD | 130,900.00 USD | 174,140.00 USD |
| `1D` | `60.20` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 136,940.00 USD | 38,090.00 USD | 97,050.00 USD |
| `7D` | `60.20` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 207,990.00 USD | 131,530.00 USD | 157,150.00 USD |
| `1D` | `60.30` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 94,410.00 USD | 77,160.00 USD | 92,820.00 USD |
| `7D` | `60.30` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 118,160.00 USD | 95,890.00 USD | 155,610.00 USD |
| `1D` | `60.40` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 164,780.00 USD | 55,740.00 USD | 81,520.00 USD |
| `7D` | `60.40` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 92,570.00 USD | 126,870.00 USD | 226,430.00 USD |
| `1D` | `60.50` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 105,740.00 USD | 38,540.00 USD | 82,680.00 USD |
| `7D` | `60.50` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 160,180.00 USD | 89,250.00 USD | 207,360.00 USD |
| `1D` | `60.60` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 79,140.00 USD | 32,180.00 USD | 5,850.00 USD |
| `7D` | `60.60` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 294,830.00 USD | 109,510.00 USD | 167,360.00 USD |
| `1D` | `60.70` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 85,730.00 USD | 45,070.00 USD | 33,670.00 USD |
| `7D` | `60.70` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 142,880.00 USD | 79,060.00 USD | 28,990.00 USD |
| `1D` | `60.80` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 46,230.00 USD | 13,240.00 USD | 65,780.00 USD |
| `7D` | `60.80` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 54,870.00 USD | 78,710.00 USD | 94,850.00 USD |
| `1D` | `60.90` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 39,620.00 USD | 19,210.00 USD | 4,800.00 USD |
| `7D` | `60.90` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 139,720.00 USD | 52,860.00 USD | 92,420.00 USD |
| `1D` | `61.00` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 46,000.00 USD | 7,290.00 USD | 32,920.00 USD |
| `7D` | `61.00` | 7,990,000.00 USD | 7,990,000.00 USD | 0.00 USD | 96,160.00 USD | 36,500.00 USD | 5,370.00 USD |
| `1D` | `61.10` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 5,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `61.10` | 8,020,000.00 USD | 8,020,000.00 USD | 0.00 USD | 31,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `61.20` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 75,930.00 USD | 1,510.00 USD | 23,480.00 USD |
| `7D` | `61.20` | 8,240,000.00 USD | 8,240,000.00 USD | 0.00 USD | 116,610.00 USD | 70,180.00 USD | 33,350.00 USD |
| `1D` | `61.30` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 9,540.00 USD | 6,960.00 USD | 2,340.00 USD |
| `7D` | `61.30` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 51,130.00 USD | 36,170.00 USD | 55,130.00 USD |
| `1D` | `61.40` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 22,150.00 USD | 7,530.00 USD | 1,950.00 USD |
| `7D` | `61.40` | 8,540,000.00 USD | 8,540,000.00 USD | 0.00 USD | 89,350.00 USD | 41,800.00 USD | 24,650.00 USD |
| `1D` | `61.50` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 8,990.00 USD | 20,580.00 USD | 22,640.00 USD |
| `7D` | `61.50` | 8,630,000.00 USD | 8,630,000.00 USD | 0.00 USD | 19,810.00 USD | 34,770.00 USD | 35,770.00 USD |
| `1D` | `61.60` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 23,830.00 USD | 13,550.00 USD | 20,600.00 USD |
| `7D` | `61.60` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 54,240.00 USD | 63,390.00 USD | 132,550.00 USD |
| `1D` | `61.70` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 51,690.00 USD | 9,670.00 USD | 28,860.00 USD |
| `7D` | `61.70` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 99,020.00 USD | 15,950.00 USD | 114,970.00 USD |
| `1D` | `61.80` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 23,530.00 USD | 8,420.00 USD | 1,830.00 USD |
| `7D` | `61.80` | 9,450,000.00 USD | 9,450,000.00 USD | 0.00 USD | 183,860.00 USD | 68,030.00 USD | 92,510.00 USD |
| `1D` | `61.90` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 34,520.00 USD | 11,940.00 USD | 16,490.00 USD |
| `7D` | `61.90` | 9,600,000.00 USD | 9,600,000.00 USD | 0.00 USD | 79,630.00 USD | 35,500.00 USD | 35,860.00 USD |
| `1D` | `62.00` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 21,250.00 USD | 1,560.00 USD | 13,970.00 USD |
| `7D` | `62.00` | 9,720,000.00 USD | 9,720,000.00 USD | 0.00 USD | 57,760.00 USD | 13,260.00 USD | 49,920.00 USD |
| `1D` | `62.10` | 5,590,000.00 USD | 5,590,000.00 USD | 0.00 USD | 12,050.00 USD | 945.47 USD | 2,230.00 USD |
| `7D` | `62.10` | 9,790,000.00 USD | 9,790,000.00 USD | 0.00 USD | 36,500.00 USD | 12,820.00 USD | 13,950.00 USD |
| `1D` | `62.20` | 5,590,000.00 USD | 5,590,000.00 USD | 0.00 USD | 3,350.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.20` | 9,900,000.00 USD | 9,900,000.00 USD | 0.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD |
| `1D` | `62.30` | 5,590,000.00 USD | 5,590,000.00 USD | 0.00 USD | 464.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.30` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 38,120.00 USD | 23,450.00 USD | 85,980.00 USD |
| `1D` | `62.40` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.40` | 10,190,000.00 USD | 10,190,000.00 USD | 0.00 USD | 81,060.00 USD | 27,560.00 USD | 30,890.00 USD |
| `7D` | `62.50` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 44,300.00 USD | 14,320.00 USD | 26,310.00 USD |
| `1D` | `62.60` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 1,100.00 USD | 0.00 USD | 327.72 USD |
| `7D` | `62.60` | 10,340,000.00 USD | 10,340,000.00 USD | 0.00 USD | 34,340.00 USD | 7,100.00 USD | 27,730.00 USD |
| `1D` | `62.70` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 16,430.00 USD | 4,920.00 USD | 18,640.00 USD |
| `7D` | `62.70` | 10,430,000.00 USD | 10,430,000.00 USD | 0.00 USD | 22,020.00 USD | 12,490.00 USD | 47,090.00 USD |
| `1D` | `62.80` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 16,330.00 USD | 7,010.00 USD | 10,780.00 USD |
| `7D` | `62.80` | 10,570,000.00 USD | 10,570,000.00 USD | 0.00 USD | 73,200.00 USD | 28,960.00 USD | 45,150.00 USD |
| `1D` | `62.90` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 8,780.00 USD | 6,670.00 USD | 63.10 USD |
| `7D` | `62.90` | 10,660,000.00 USD | 10,660,000.00 USD | 0.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `63.00` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 7,650.00 USD | 7,040.00 USD | 4,820.00 USD |
| `7D` | `63.00` | 10,730,000.00 USD | 10,730,000.00 USD | 0.00 USD | 35,710.00 USD | 12,240.00 USD | 17,650.00 USD |
| `1D` | `63.10` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 4,260.00 USD | 4,070.00 USD | 6,480.00 USD |
| `7D` | `63.10` | 10,770,000.00 USD | 10,770,000.00 USD | 0.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `63.20` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 2,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `63.30` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 4,590.00 USD | 594.25 USD | 2,790.00 USD |
| `7D` | `63.30` | 10,810,000.00 USD | 10,810,000.00 USD | 0.00 USD | 21,810.00 USD | 11,500.00 USD | 9,730.00 USD |
| `1D` | `63.40` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 9,050.00 USD | 1,440.00 USD | 7,260.00 USD |
| `7D` | `63.40` | 10,840,000.00 USD | 10,840,000.00 USD | 0.00 USD | 14,300.00 USD | 1,320.00 USD | 9,960.00 USD |
| `1D` | `63.50` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 12,520.00 USD | 21,470.00 USD | 9,190.00 USD |
| `7D` | `63.50` | 10,870,000.00 USD | 10,870,000.00 USD | 0.00 USD | 6,620.00 USD | 15,810.00 USD | 4,760.00 USD |
| `1D` | `63.60` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 23,390.00 USD | 8,230.00 USD | 23,340.00 USD |
| `7D` | `63.60` | 10,960,000.00 USD | 10,960,000.00 USD | 0.00 USD | 63,480.00 USD | 20,800.00 USD | 11,880.00 USD |
| `1D` | `63.70` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 28,350.00 USD | 5,780.00 USD | 35,220.00 USD |
| `7D` | `63.70` | 11,040,000.00 USD | 11,040,000.00 USD | 0.00 USD | 21,940.00 USD | 18,810.00 USD | 35,480.00 USD |
| `1D` | `63.80` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 18,580.00 USD | 10,410.00 USD | 14,390.00 USD |
| `7D` | `63.80` | 11,100,000.00 USD | 11,100,000.00 USD | 0.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD |
| `1D` | `63.90` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 31,330.00 USD | 8,170.00 USD | 15,960.00 USD |
| `7D` | `63.90` | 11,130,000.00 USD | 11,130,000.00 USD | 0.00 USD | 7,650.00 USD | 12,840.00 USD | 8,940.00 USD |
| `7D` | `64.00` | 11,170,000.00 USD | 11,170,000.00 USD | 0.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD |
| `7D` | `64.10` | 11,200,000.00 USD | 11,200,000.00 USD | 0.00 USD | 20,350.00 USD | 667.05 USD | 10,640.00 USD |
| `7D` | `64.20` | 11,250,000.00 USD | 11,250,000.00 USD | 0.00 USD | 28,840.00 USD | 14,530.00 USD | 584.77 USD |
| `7D` | `64.40` | 11,300,000.00 USD | 11,300,000.00 USD | 0.00 USD | 2,540.00 USD | 20,590.00 USD | 29,110.00 USD |
| `7D` | `64.50` | 11,330,000.00 USD | 11,330,000.00 USD | 0.00 USD | 7,700.00 USD | 7,120.00 USD | 13,310.00 USD |
| `7D` | `64.60` | 11,380,000.00 USD | 11,380,000.00 USD | 0.00 USD | 32,220.00 USD | 14,180.00 USD | 108.50 USD |
| `7D` | `64.70` | 11,440,000.00 USD | 11,440,000.00 USD | 0.00 USD | 39,430.00 USD | 23,030.00 USD | 3,870.00 USD |
| `7D` | `64.80` | 11,480,000.00 USD | 11,480,000.00 USD | 0.00 USD | 7,540.00 USD | 8,210.00 USD | 20,430.00 USD |
| `7D` | `64.90` | 11,520,000.00 USD | 11,520,000.00 USD | 0.00 USD | 25,750.00 USD | 8,010.00 USD | 9,630.00 USD |
| `7D` | `65.00` | 11,530,000.00 USD | 11,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,480.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `450.41M` | Total OI Tokens: `7,777,667.6 LTC`
  * 1h OI Change: `+0.21%` | 4h OI Change: `-1.70%` | 24h OI Change: `-4.61%`
  * Exchange Breakdown: Binance=`81.51M` | Bybit=`69.58M` | OKX=`34.82M` | Hyperliquid=`22.85M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `16.68K` | Last 24h: `36.85K` | Last 3d: `60.07K` | Last 7d: `106.71K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0092%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0073%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `51.99%` | `48.01%` | `1.08` | 1,200,000.00 USD |
| `15M` | `Binance` | `48.61%` | `51.39%` | `0.95` | 446,220.00 USD |
| `15M` | `OKX` | `77.47%` | `22.53%` | `3.44` | 128,680.00 USD |
| `15M` | `Bybit` | `79.17%` | `20.83%` | `3.80` | 64,730.00 USD |
| `15M` | `KuCoin` | `45.8%` | `54.2%` | `0.85` | 54,100.00 USD |
| `15M` | `Gate` | `52.29%` | `47.71%` | `1.10` | 13,280.00 USD |
| `15M` | `Bitget` | `80.12%` | `19.88%` | `4.03` | 55,220.00 USD |
| `15M` | `BingX` | `54.84%` | `45.16%` | `1.21` | 122,640.00 USD |
| `15M` | `MEXC` | `44.53%` | `55.47%` | `0.80` | 41,120.00 USD |
| `15M` | `Bitunix` | `44.25%` | `55.75%` | `0.79` | 31,940.00 USD |
| `15M` | `Hyperliquid` | `22.77%` | `77.23%` | `0.29` | 4,530.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.69%` | `51.31%` | `0.95` | 161,600.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 73,030.00 USD |
| `15M` | `HTX` | `42.33%` | `57.67%` | `0.73` | 398.27 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `9.18%` | `90.82%` | `0.10` | 1,960.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 56.04 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `48.61%` | `51.39%` | `0.95` | 446,220.00 USD |
| `15M` | `Global Accounts` | `51.99%` | `48.01%` | `1.08` | 1,200,000.00 USD |
| `1H` | `LTC` | `60.13%` | `39.87%` | `1.51` | 8,200,000.00 USD |
| `1H` | `Binance` | `59.88%` | `40.12%` | `1.49` | 1,890,000.00 USD |
| `1H` | `OKX` | `63.76%` | `36.24%` | `1.76` | 788,010.00 USD |
| `1H` | `Bybit` | `70.08%` | `29.92%` | `2.34` | 715,360.00 USD |
| `1H` | `KuCoin` | `36.93%` | `63.07%` | `0.59` | 20,430.00 USD |
| `1H` | `Gate` | `47.34%` | `52.66%` | `0.90` | 1,280,000.00 USD |
| `1H` | `Bitget` | `59.54%` | `40.46%` | `1.47` | 145,450.00 USD |
| `1H` | `BingX` | `50.42%` | `49.58%` | `1.02` | 1,970,000.00 USD |
| `1H` | `MEXC` | `56.31%` | `43.69%` | `1.29` | 195,490.00 USD |
| `1H` | `Bitunix` | `58.98%` | `41.02%` | `1.44` | 96,310.00 USD |
| `1H` | `Hyperliquid` | `70.13%` | `29.87%` | `2.35` | 53,710.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.53%` | `49.47%` | `1.02` | 203,540.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `97.11%` | `2.89%` | `33.60` | 761,250.00 USD |
| `1H` | `HTX` | `85.67%` | `14.33%` | `5.98` | 7,540.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `38.97%` | `61.03%` | `0.64` | 20,730.00 USD |
| `1H` | `Aster` | `77.4%` | `22.6%` | `3.42` | 52,290.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `34.43%` | `65.57%` | `0.53` | 367.47 USD |
| `1H` | `Whale Positions` | `59.88%` | `40.12%` | `1.49` | 1,890,000.00 USD |
| `1H` | `Global Accounts` | `60.13%` | `39.87%` | `1.51` | 8,200,000.00 USD |
| `4H` | `LTC` | `54.01%` | `45.99%` | `1.17` | 34,920,000.00 USD |
| `4H` | `Binance` | `50.15%` | `49.85%` | `1.01` | 12,910,000.00 USD |
| `4H` | `OKX` | `49.88%` | `50.12%` | `1.00` | 3,250,000.00 USD |
| `4H` | `Bybit` | `54.05%` | `45.95%` | `1.18` | 2,670,000.00 USD |
| `4H` | `KuCoin` | `47.2%` | `52.8%` | `0.89` | 1,730,000.00 USD |
| `4H` | `Gate` | `49.92%` | `50.08%` | `1.00` | 1,450,000.00 USD |
| `4H` | `Bitget` | `54.84%` | `45.16%` | `1.21` | 1,130,000.00 USD |
| `4H` | `BingX` | `45.82%` | `54.18%` | `0.85` | 2,630,000.00 USD |
| `4H` | `MEXC` | `47.15%` | `52.85%` | `0.89` | 2,320,000.00 USD |
| `4H` | `Bitunix` | `51.43%` | `48.57%` | `1.06` | 944,660.00 USD |
| `4H` | `Hyperliquid` | `46.15%` | `53.85%` | `0.86` | 553,950.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.72%` | `50.28%` | `0.99` | 3,900,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `96.76%` | `3.24%` | `29.86` | 1,150,000.00 USD |
| `4H` | `HTX` | `46.18%` | `53.82%` | `0.86` | 81,720.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `35.22%` | `64.78%` | `0.54` | 121,010.00 USD |
| `4H` | `Aster` | `79.65%` | `20.35%` | `3.91` | 78,060.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `31.27%` | `68.73%` | `0.45` | 0.00 USD |
| `4H` | `Whale Positions` | `50.15%` | `49.85%` | `1.01` | 12,910,000.00 USD |
| `4H` | `Global Accounts` | `54.01%` | `45.99%` | `1.17` | 34,920,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `57.89` | `58.07` | `57.89` | `58.36` | `57.84` | 621,283.45 USD | 280,339.51 USD | 340,943.94 USD | -60,604.43 USD | `-9.75%` | `5B / 14S` |
| `5:00 UTC` | `57.58` | `57.64` | `57.58` | `57.91` | `57.50` | 1,187,641.81 USD | 478,923.89 USD | 708,717.92 USD | -229,794.02 USD | `-19.35%` | `2B / 11S` |
| `0:00 UTC` | `57.69` | `57.76` | `57.69` | `57.89` | `57.67` | 706,696.44 USD | 375,137.92 USD | 331,558.52 USD | 43,579.41 USD | `+6.17%` | `4B / 3S` |
| `5:00 UTC` | `57.59` | `57.69` | `57.59` | `57.92` | `57.55` | 386,395.75 USD | 217,528.58 USD | 168,867.17 USD | 48,661.41 USD | `+12.59%` | `5B / 5S` |
| `0:00 UTC` | `57.73` | `57.60` | `57.73` | `57.75` | `57.44` | 1,217,516.75 USD | 556,410.68 USD | 661,106.07 USD | -104,695.39 USD | `-8.60%` | `4B / 9S` |
| `5:00 UTC` | `57.59` | `57.70` | `57.59` | `57.88` | `57.55` | 407,665.08 USD | 260,874.04 USD | 146,791.04 USD | 114,082.99 USD | `+27.98%` | `15B / 1S` |
| `0:00 UTC` | `57.56` | `57.61` | `57.56` | `57.77` | `57.55` | 421,492.76 USD | 256,306.11 USD | 165,186.65 USD | 91,119.46 USD | `+21.62%` | `3B / 4S` |
| `5:00 UTC` | `57.83` | `57.80` | `57.83` | `57.94` | `57.61` | 405,316.11 USD | 265,776.17 USD | 139,539.93 USD | 126,236.24 USD | `+31.15%` | `10B / 0S` |
| `0:00 UTC` | `57.98` | `57.97` | `57.98` | `58.05` | `57.84` | 364,891.83 USD | 190,130.13 USD | 174,761.70 USD | 15,368.44 USD | `+4.21%` | `2B / 2S` |
| `5:00 UTC` | `58.00` | `57.98` | `58.00` | `58.08` | `57.89` | 113,574.12 USD | 54,301.87 USD | 59,272.25 USD | -4,970.37 USD | `-4.38%` | `1B / 3S` |

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
| `5m` | -12,320.00 USD | 78,020.00 USD | **`ACCUMULATION`** |
| `15m` | 62,080.00 USD | 163,260.00 USD | **`ACCUMULATION`** |
| `30m` | 79,120.00 USD | 604,580.00 USD | **`ACCUMULATION`** |
| `1h` | 132,450.00 USD | 950,780.00 USD | **`ACCUMULATION`** |
| `2h` | 290,140.00 USD | 805,300.00 USD | **`ACCUMULATION`** |
| `4h` | 1,050,000.00 USD | 591,600.00 USD | **`ACCUMULATION`** |
| `6h` | 1,930,000.00 USD | 598,610.00 USD | **`ACCUMULATION`** |
| `8h` | 1,960,000.00 USD | 2,950,000.00 USD | **`ACCUMULATION`** |
| `12h` | 2,670,000.00 USD | 4,090,000.00 USD | **`ACCUMULATION`** |
| `24h` | 2,040,000.00 USD | -2,070,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 5,890,000.00 USD | -19,880,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -19,960,000.00 USD | -188,130,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-12.32K` | 15m=`+62.08K` | 1h=`+132.45K` | 24h=`+2.04M`
* Futures Capital Netflows: 5m=`+78.02K` | 15m=`+163.26K` | 1h=`+950.78K` | 24h=`-2.07M`
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
  * Execution Entry: `57.04` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `56.21` (Risk Distance: `0.8305` pts)
  * +2.5R Take Profit: `59.12`
  * Mathematical Lot Sizing: **`12.04 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `58.48` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `59.31` (Risk Distance: `0.8305` pts)
  * +2.5R Take Profit: `56.40`
  * Mathematical Lot Sizing: **`12.04 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`58.49`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
