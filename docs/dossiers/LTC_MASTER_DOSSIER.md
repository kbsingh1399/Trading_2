# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 14:41:48 IST` (`2026-10-30 09:11:48 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `55.33` | **Live Ask Quote**: `55.62` | **Mid Price**: `55.48`
- **Spread Points**: `300.00` | **Spread BPS**: `54.08 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `54.83` | VWAP Z-Score: `+0.50` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.3354` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `43.23` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `57.69` | Lower -3.00σ Band: `51.97`
  * Upper +2.51σ Band: `57.23` | Lower -2.51σ Band: `52.44`
  * Upper +2.01σ Band: `56.75` | Lower -2.01σ Band: `52.92`
  * Upper +2.00σ Band: `56.74` | Lower -2.00σ Band: `52.93`
  * Upper +1.28σ Band: `56.05` | Lower -1.28σ Band: `53.61`
  * Upper +1.00σ Band: `55.79` | Lower -1.00σ Band: `53.88`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`55.58` | EMA-20=`55.62` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`55.75` (Slope: `+0.0000`) | EMA-100=`56.22`
  * Institutional Anchors: EMA-144=`56.46` | EMA-200=`56.59` (Slope: `-0.1929`) | EMA-233=`56.65`
- **Range Boundaries**: 24H High=`58.72` | 24H Low=`52.64` | Weekly High=`59.62` | Weekly Low=`52.64`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `56.21` (Distance: `-1.20%`)
  * Point of Control (POC) = `55.85` (Distance: `-0.56%`)
  * Value Area Low (VAL) = `54.61` (Distance: `+1.70%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.40` | POC=`57.72` | VAL=`56.83`
  * Prior Day Extremes: PDH=`59.52` | PDL=`54.18` | PDC=`54.46`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`58.29` | Weekly POC=`56.43` | Weekly VAL=`55.83`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`56.03` | Low=`52.64`
  * London Session (08:00-16:00 UTC): High=`56.23` | Low=`55.27`
  * New York Session (13:00-21:00 UTC): High=`55.81` | Low=`55.14`
  * Initial Balance (First Hour): IB High=`56.22` | IB Low=`55.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `55.25` - `55.70`
  * Optimal Trade Entry (OTE 0.705): `55.59`
  * Structural Invalidation Anchor (0.786): `55.92`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `55.66` | `55.70` | `55.56` | `55.68` | `3,385` | 188,199.95 USD | 65,658.66 USD | `+34.89%` | -5,352,006.79 USD | `+0.69` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `55.69` | `55.69` | `55.51` | `55.54` | `2,369` | 131,650.02 USD | -26,661.66 USD | `-20.25%` | -5,378,668.45 USD | `-0.11` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `55.54` | `55.58` | `55.50` | `55.56` | `1,098` | 60,955.14 USD | -31,441.20 USD | `-51.58%` | -5,410,109.65 USD | `-0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `55.68` | `55.78` | `55.54` | `55.56` | `15,076` | 839,476.56 USD | 306,295.77 USD | `+36.49%` | -5,507,158.06 USD | `+2.47` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `55.57` | `55.70` | `55.51` | `55.54` | `7,845` | 436,166.22 USD | 48,104.99 USD | `+11.03%` | -5,459,053.07 USD | `+0.55` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `55.54` | `55.58` | `55.50` | `55.57` | `1,102` | 61,216.75 USD | -31,179.60 USD | `-50.93%` | -5,490,232.67 USD | `-0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `56.22` | `56.34` | `55.72` | `55.97` | `54,792` | 3,072,188.69 USD | -261,201.20 USD | `-8.50%` | -5,429,107.24 USD | `+0.02` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `55.96` | `55.99` | `55.51` | `55.54` | `48,222` | 2,686,866.22 USD | -29,505.47 USD | `-1.10%` | -5,458,612.72 USD | `+0.34` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `55.54` | `55.58` | `55.50` | `55.57` | `1,105` | 61,341.61 USD | -31,304.47 USD | `-51.03%` | -5,489,917.18 USD | `+0.35` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -5,054,684.98 USD | `-0.61` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.47` | `55.72` | `55.97` | `202,255` | 11,356,305.33 USD | -519,640.59 USD | `-4.58%` | -5,574,325.57 USD | `+0.43` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `55.96` | `55.99` | `55.50` | `55.57` | `49,327` | 2,748,207.83 USD | -60,809.94 USD | `-2.21%` | -5,635,135.50 USD | `+0.67` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | 387,872.12 USD | `-1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,876,168.80 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -5,054,684.98 USD | `-0.61` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.47` | `55.72` | `55.97` | `202,255` | 11,356,305.33 USD | -519,640.59 USD | `-4.58%` | -5,574,325.57 USD | `+0.43` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `55.96` | `55.99` | `55.50` | `55.57` | `49,327` | 2,748,207.83 USD | -60,809.94 USD | `-2.21%` | -5,635,135.50 USD | `+0.67` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`55.48`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:32:27 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1083` | `0xeadc...9d55` | `LONG` | 2,029,318.19 USD | `36,463.77` | `52.78` | `55.61` | `0.000000` | 104,642.24 USD | `+5.16%` | `10X Cross` |
| `1095` | `0x9aa5...58af` | `SHORT` | 2,013,286.22 USD | `36,177.65` | `71.22` | `55.61` | `309.34` | 563,200.44 USD | `+27.97%` | `10X Cross` |

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
  * 24H Horizon: Short MP=`56.49` (Vol: 204,200.00 USD, Dist: `+1.64%`) | Long MP=`54.13` (Vol: 153,300.00 USD, Dist: `--2.60%`)
  * 48H Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.15%`) | Long MP=`54.12` (Vol: 153,300.00 USD, Dist: `--2.63%`)
  * 3D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.15%`) | Long MP=`54.12` (Vol: 153,300.00 USD, Dist: `--2.63%`)
  * 7D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.15%`) | Long MP=`54.12` (Vol: 153,300.00 USD, Dist: `--2.63%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `47.20` | 8,220,000.00 USD | 8,220,000.00 USD | 9,650.00 USD | 2,470.00 USD | 114.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `47.30` | 8,210,000.00 USD | 8,210,000.00 USD | 692.33 USD | 4,740.00 USD | 6,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `47.40` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 1,520.00 USD | 28,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `47.50` | 8,160,000.00 USD | 8,160,000.00 USD | 11,830.00 USD | 0.00 USD | 7,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `48.10` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `48.20` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `48.40` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 6,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `48.60` | 8,130,000.00 USD | 8,130,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `48.80` | 8,120,000.00 USD | 8,120,000.00 USD | 1,780.00 USD | 2,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `48.90` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 960.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.30` | 8,120,000.00 USD | 8,120,000.00 USD | 15,190.00 USD | 4,490.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.40` | 8,090,000.00 USD | 8,090,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.50` | 8,080,000.00 USD | 8,080,000.00 USD | 2,830.00 USD | 7,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.60` | 8,070,000.00 USD | 8,070,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.70` | 8,050,000.00 USD | 8,050,000.00 USD | 12,090.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.80` | 8,030,000.00 USD | 8,030,000.00 USD | 9,930.00 USD | 8,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `49.90` | 4,030,000.00 USD | 4,030,000.00 USD | 26,820.00 USD | 14,520.00 USD | 44,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.90` | 8,020,000.00 USD | 8,020,000.00 USD | 45,030.00 USD | 8,880.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.00` | 3,940,000.00 USD | 3,940,000.00 USD | 11,780.00 USD | 15,870.00 USD | 40,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.00` | 7,960,000.00 USD | 7,960,000.00 USD | 22,100.00 USD | 19,810.00 USD | 24,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.10` | 3,870,000.00 USD | 3,870,000.00 USD | 3,780.00 USD | 4,040.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.10` | 7,890,000.00 USD | 7,890,000.00 USD | 363.50 USD | 682.90 USD | 8,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.20` | 3,860,000.00 USD | 3,860,000.00 USD | 177.10 USD | 709.61 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.20` | 7,880,000.00 USD | 7,880,000.00 USD | 6,960.00 USD | 500.40 USD | 42,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.30` | 3,850,000.00 USD | 3,850,000.00 USD | 171.03 USD | 3,880.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.30` | 7,830,000.00 USD | 7,830,000.00 USD | 16,270.00 USD | 10,780.00 USD | 7,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.40` | 3,840,000.00 USD | 3,840,000.00 USD | 8,260.00 USD | 11,890.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.40` | 7,800,000.00 USD | 7,800,000.00 USD | 28,280.00 USD | 26,580.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.50` | 3,820,000.00 USD | 3,820,000.00 USD | 8,910.00 USD | 8,790.00 USD | 10,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.50` | 7,710,000.00 USD | 7,710,000.00 USD | 32,490.00 USD | 6,790.00 USD | 44,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.60` | 3,790,000.00 USD | 3,790,000.00 USD | 7,330.00 USD | 3,440.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.60` | 7,620,000.00 USD | 7,620,000.00 USD | 67,580.00 USD | 21,530.00 USD | 31,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.70` | 3,770,000.00 USD | 3,770,000.00 USD | 8,170.00 USD | 2,300.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.70` | 7,500,000.00 USD | 7,500,000.00 USD | 65,920.00 USD | 32,820.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.80` | 3,750,000.00 USD | 3,750,000.00 USD | 12,550.00 USD | 3,100.00 USD | 8,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.80` | 7,360,000.00 USD | 7,360,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.90` | 3,730,000.00 USD | 3,730,000.00 USD | 826.24 USD | 260.05 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.90` | 7,270,000.00 USD | 7,270,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.00` | 3,720,000.00 USD | 3,720,000.00 USD | 5,040.00 USD | 0.00 USD | 430.77 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.00` | 7,010,000.00 USD | 7,010,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.10` | 3,710,000.00 USD | 3,710,000.00 USD | 9,210.00 USD | 6,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.10` | 6,890,000.00 USD | 6,890,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.20` | 3,700,000.00 USD | 3,700,000.00 USD | 1,770.00 USD | 1,130.00 USD | 19,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.20` | 6,810,000.00 USD | 6,810,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.30` | 3,670,000.00 USD | 3,670,000.00 USD | 8,650.00 USD | 9,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.30` | 6,740,000.00 USD | 6,740,000.00 USD | 28,400.00 USD | 26,720.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.40` | 3,650,000.00 USD | 3,650,000.00 USD | 3,250.00 USD | 5,610.00 USD | 416.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.40` | 6,640,000.00 USD | 6,640,000.00 USD | 73,130.00 USD | 42,820.00 USD | 46,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.50` | 3,650,000.00 USD | 3,650,000.00 USD | 5,650.00 USD | 10,010.00 USD | 41,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.50` | 6,480,000.00 USD | 6,480,000.00 USD | 38,520.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.60` | 3,590,000.00 USD | 3,590,000.00 USD | 9,060.00 USD | 18,580.00 USD | 757.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.60` | 6,380,000.00 USD | 6,380,000.00 USD | 37,880.00 USD | 36,790.00 USD | 41,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.70` | 3,560,000.00 USD | 3,560,000.00 USD | 2,890.00 USD | 13,780.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.70` | 6,260,000.00 USD | 6,260,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.80` | 3,540,000.00 USD | 3,540,000.00 USD | 13,770.00 USD | 19,520.00 USD | 14,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.80` | 6,230,000.00 USD | 6,230,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.90` | 3,490,000.00 USD | 3,490,000.00 USD | 10,140.00 USD | 19,910.00 USD | 23,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.90` | 6,170,000.00 USD | 6,170,000.00 USD | 5,870.00 USD | 25,410.00 USD | 28,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.00` | 3,440,000.00 USD | 3,440,000.00 USD | 20,980.00 USD | 25,620.00 USD | 24,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.00` | 6,110,000.00 USD | 6,110,000.00 USD | 65,840.00 USD | 26,440.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.10` | 3,370,000.00 USD | 3,370,000.00 USD | 34,970.00 USD | 17,300.00 USD | 50,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 6,010,000.00 USD | 6,010,000.00 USD | 24,220.00 USD | 28,090.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.20` | 3,260,000.00 USD | 3,260,000.00 USD | 15,890.00 USD | 7,630.00 USD | 49,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 5,920,000.00 USD | 5,920,000.00 USD | 38,380.00 USD | 13,960.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.30` | 3,190,000.00 USD | 3,190,000.00 USD | 26,510.00 USD | 22,090.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 5,840,000.00 USD | 5,840,000.00 USD | 26,450.00 USD | 40,700.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.40` | 3,130,000.00 USD | 3,130,000.00 USD | 13,070.00 USD | 15,400.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 5,760,000.00 USD | 5,760,000.00 USD | 20,580.00 USD | 38,950.00 USD | 22,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.50` | 3,100,000.00 USD | 3,100,000.00 USD | 53,990.00 USD | 30,000.00 USD | 79,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.50` | 5,680,000.00 USD | 5,680,000.00 USD | 40,460.00 USD | 667.05 USD | 11,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.60` | 2,930,000.00 USD | 2,930,000.00 USD | 8,330.00 USD | 43,700.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.60` | 5,630,000.00 USD | 5,630,000.00 USD | 73,920.00 USD | 32,590.00 USD | 59,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.70` | 2,870,000.00 USD | 2,870,000.00 USD | 18,270.00 USD | 19,780.00 USD | 40,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.70` | 5,460,000.00 USD | 5,460,000.00 USD | 19,550.00 USD | 75,910.00 USD | 108,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.80` | 2,800,000.00 USD | 2,800,000.00 USD | 28,000.00 USD | 50,850.00 USD | 72,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.80` | 5,260,000.00 USD | 5,260,000.00 USD | 30,590.00 USD | 25,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.90` | 2,640,000.00 USD | 2,640,000.00 USD | 43,760.00 USD | 50,880.00 USD | 30,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.90` | 5,200,000.00 USD | 5,200,000.00 USD | 30,900.00 USD | 11,650.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.00` | 2,520,000.00 USD | 2,520,000.00 USD | 26,800.00 USD | 30,500.00 USD | 39,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.00` | 5,130,000.00 USD | 5,130,000.00 USD | 39,690.00 USD | 22,700.00 USD | 77,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.10` | 2,420,000.00 USD | 2,420,000.00 USD | 12,590.00 USD | 43,040.00 USD | 85,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.10` | 4,990,000.00 USD | 4,990,000.00 USD | 45,320.00 USD | 17,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.20` | 2,280,000.00 USD | 2,280,000.00 USD | 20,660.00 USD | 9,840.00 USD | 42,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.20` | 4,920,000.00 USD | 4,920,000.00 USD | 162,460.00 USD | 32,580.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.30` | 2,210,000.00 USD | 2,210,000.00 USD | 5,080.00 USD | 25,160.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.30` | 4,700,000.00 USD | 4,700,000.00 USD | 59,390.00 USD | 49,210.00 USD | 35,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.40` | 2,170,000.00 USD | 2,170,000.00 USD | 12,600.00 USD | 10,640.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.40` | 4,560,000.00 USD | 4,560,000.00 USD | 44,030.00 USD | 17,420.00 USD | 91,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.50` | 2,150,000.00 USD | 2,150,000.00 USD | 9,960.00 USD | 5,700.00 USD | 22,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.50` | 4,410,000.00 USD | 4,410,000.00 USD | 60,260.00 USD | 3,440.00 USD | 28,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.60` | 2,110,000.00 USD | 2,110,000.00 USD | 75,950.00 USD | 3,830.00 USD | 20,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.60` | 4,320,000.00 USD | 4,320,000.00 USD | 52,800.00 USD | 3,780.00 USD | 20,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.70` | 2,010,000.00 USD | 2,010,000.00 USD | 6,210.00 USD | 11,100.00 USD | 11,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.70` | 4,240,000.00 USD | 4,240,000.00 USD | 131,400.00 USD | 21,330.00 USD | 13,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.80` | 1,980,000.00 USD | 1,980,000.00 USD | 53,640.00 USD | 28,920.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.80` | 4,070,000.00 USD | 4,070,000.00 USD | 99,150.00 USD | 43,900.00 USD | 302.55 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.90` | 1,890,000.00 USD | 1,890,000.00 USD | 51,060.00 USD | 39,560.00 USD | 27,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.90` | 3,930,000.00 USD | 3,930,000.00 USD | 160,820.00 USD | 22,780.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.00` | 1,770,000.00 USD | 1,770,000.00 USD | 76,010.00 USD | 21,440.00 USD | 86,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.00` | 3,740,000.00 USD | 3,740,000.00 USD | 380,340.00 USD | 71,820.00 USD | 304,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.10` | 1,590,000.00 USD | 1,590,000.00 USD | 94,870.00 USD | 19,160.00 USD | 49,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.10` | 2,980,000.00 USD | 2,980,000.00 USD | 302,190.00 USD | 0.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.20` | 1,420,000.00 USD | 1,420,000.00 USD | 72,600.00 USD | 15,510.00 USD | 40,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.20` | 2,670,000.00 USD | 2,670,000.00 USD | 205,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.30` | 1,300,000.00 USD | 1,300,000.00 USD | 15,600.00 USD | 6,650.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.30` | 2,470,000.00 USD | 2,470,000.00 USD | 381,380.00 USD | 8,520.00 USD | 181,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.40` | 1,270,000.00 USD | 1,270,000.00 USD | 56,350.00 USD | 85,810.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.40` | 1,900,000.00 USD | 1,900,000.00 USD | 304,270.00 USD | 63,170.00 USD | 92,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.50` | 1,120,000.00 USD | 1,120,000.00 USD | 26,610.00 USD | 64,250.00 USD | 9,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.50` | 1,440,000.00 USD | 1,440,000.00 USD | 159,720.00 USD | 35,580.00 USD | 239,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.60` | 1,020,000.00 USD | 1,020,000.00 USD | 913.17 USD | 25,490.00 USD | 43,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.60` | 1,000,000.00 USD | 1,000,000.00 USD | 18,530.00 USD | 1,930.00 USD | 131,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.70` | 953,500.00 USD | 953,500.00 USD | 6,600.00 USD | 23,060.00 USD | 105,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.70` | 850,330.00 USD | 850,330.00 USD | 0.00 USD | 3,600.00 USD | 41,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.80` | 818,040.00 USD | 818,040.00 USD | 0.00 USD | 48,420.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.80` | 805,420.00 USD | 805,420.00 USD | 0.00 USD | 35,700.00 USD | 26,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.90` | 745,700.00 USD | 745,700.00 USD | 66,900.00 USD | 65,440.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.90` | 743,280.00 USD | 743,280.00 USD | 0.00 USD | 112,280.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.00` | 602,520.00 USD | 602,520.00 USD | 40,710.00 USD | 54,150.00 USD | 55,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.00` | 582,710.00 USD | 582,710.00 USD | 97,700.00 USD | 2,830.00 USD | 19,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.10` | 452,460.00 USD | 452,460.00 USD | 50,530.00 USD | 62,170.00 USD | 80,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.10` | 462,820.00 USD | 462,820.00 USD | 54,590.00 USD | 18,510.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.20` | 259,560.00 USD | 259,560.00 USD | 39,390.00 USD | 11,830.00 USD | 66,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.20` | 325,040.00 USD | 325,040.00 USD | 57,400.00 USD | 59,710.00 USD | 150,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.30` | 141,940.00 USD | 141,940.00 USD | 52,860.00 USD | 22,650.00 USD | 59,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.30` | 57,770.00 USD | 57,770.00 USD | 23,140.00 USD | 11,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.40` | 7,250.00 USD | 7,250.00 USD | 0.00 USD | 6,510.00 USD | 742.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.40` | 23,360.00 USD | 23,360.00 USD | 0.00 USD | 18,550.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.50` | 5,500.00 USD | 5,500.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.50` | 11,000.00 USD | 11,000.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.70` | 19,310.00 USD | 19,310.00 USD | 0.00 USD | 7,700.00 USD | 613.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.70` | 206,420.00 USD | 206,420.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.80` | 22,490.00 USD | 22,490.00 USD | 0.00 USD | 0.00 USD | 3,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.80` | 297,390.00 USD | 297,390.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.90` | 75,550.00 USD | 75,550.00 USD | 51,520.00 USD | 0.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.90` | 438,720.00 USD | 438,720.00 USD | 141,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.00` | 79,930.00 USD | 79,930.00 USD | 0.00 USD | 0.00 USD | 4,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.00` | 609,830.00 USD | 609,830.00 USD | 2,590.00 USD | 0.00 USD | 168,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.20` | 689,780.00 USD | 689,780.00 USD | 0.00 USD | 79,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.30` | 83,880.00 USD | 83,880.00 USD | 0.00 USD | 0.00 USD | 3,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.30` | 692,370.00 USD | 692,370.00 USD | 0.00 USD | 0.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.40` | 108,220.00 USD | 108,220.00 USD | 5,040.00 USD | 16,820.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.40` | 706,060.00 USD | 706,060.00 USD | 2,650.00 USD | 11,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.50` | 500,310.00 USD | 500,310.00 USD | 138,540.00 USD | 108,630.00 USD | 144,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.50` | 1,030,000.00 USD | 1,030,000.00 USD | 170,750.00 USD | 151,940.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.60` | 790,260.00 USD | 790,260.00 USD | 54,340.00 USD | 154,550.00 USD | 81,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.60` | 1,580,000.00 USD | 1,580,000.00 USD | 363,190.00 USD | 185,910.00 USD | 507.54 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.70` | 1,270,000.00 USD | 1,270,000.00 USD | 114,230.00 USD | 45,300.00 USD | 315,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.70` | 1,940,000.00 USD | 1,940,000.00 USD | 117,290.00 USD | 141,830.00 USD | 98,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.80` | 1,510,000.00 USD | 1,510,000.00 USD | 117,760.00 USD | 20,790.00 USD | 106,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.80` | 2,530,000.00 USD | 2,530,000.00 USD | 172,110.00 USD | 92,780.00 USD | 318,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.90` | 1,610,000.00 USD | 1,610,000.00 USD | 45,140.00 USD | 17,930.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.90` | 3,000,000.00 USD | 3,000,000.00 USD | 113,780.00 USD | 52,200.00 USD | 307,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.00` | 1,690,000.00 USD | 1,690,000.00 USD | 6,480.00 USD | 43,030.00 USD | 29,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.00` | 3,320,000.00 USD | 3,320,000.00 USD | 88,680.00 USD | 56,390.00 USD | 178,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.10` | 1,890,000.00 USD | 1,890,000.00 USD | 77,000.00 USD | 77,400.00 USD | 46,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.10` | 3,460,000.00 USD | 3,460,000.00 USD | 36,580.00 USD | 79,290.00 USD | 21,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.20` | 2,140,000.00 USD | 2,140,000.00 USD | 53,080.00 USD | 78,490.00 USD | 120,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.20` | 3,630,000.00 USD | 3,630,000.00 USD | 118,850.00 USD | 23,920.00 USD | 23,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.30` | 2,340,000.00 USD | 2,340,000.00 USD | 70,930.00 USD | 44,630.00 USD | 87,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.30` | 3,830,000.00 USD | 3,830,000.00 USD | 76,940.00 USD | 28,570.00 USD | 98,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.40` | 2,560,000.00 USD | 2,560,000.00 USD | 84,960.00 USD | 49,470.00 USD | 78,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.40` | 4,280,000.00 USD | 4,280,000.00 USD | 124,180.00 USD | 72,180.00 USD | 257,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.50` | 2,980,000.00 USD | 2,980,000.00 USD | 197,830.00 USD | 48,350.00 USD | 174,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.50` | 4,420,000.00 USD | 4,420,000.00 USD | 99,810.00 USD | 31,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.60` | 3,140,000.00 USD | 3,140,000.00 USD | 69,720.00 USD | 27,370.00 USD | 62,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.60` | 4,640,000.00 USD | 4,640,000.00 USD | 149,560.00 USD | 44,690.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.70` | 3,320,000.00 USD | 3,320,000.00 USD | 39,010.00 USD | 51,220.00 USD | 96,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.70` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 30,070.00 USD | 57,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.80` | 3,440,000.00 USD | 3,440,000.00 USD | 18,150.00 USD | 22,650.00 USD | 77,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.80` | 4,810,000.00 USD | 4,810,000.00 USD | 9,650.00 USD | 24,520.00 USD | 49,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.90` | 3,500,000.00 USD | 3,500,000.00 USD | 13,000.00 USD | 15,870.00 USD | 28,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.90` | 4,850,000.00 USD | 4,850,000.00 USD | 14,390.00 USD | 963.90 USD | 30,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.00` | 3,530,000.00 USD | 3,530,000.00 USD | 7,880.00 USD | 9,480.00 USD | 15,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.00` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 5,470.00 USD | 107,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.10` | 3,600,000.00 USD | 3,600,000.00 USD | 31,400.00 USD | 17,830.00 USD | 21,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.10` | 5,010,000.00 USD | 5,010,000.00 USD | 5,470.00 USD | 19,160.00 USD | 14,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.20` | 3,680,000.00 USD | 3,680,000.00 USD | 35,920.00 USD | 34,800.00 USD | 4,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.20` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 31,590.00 USD | 302.55 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.30` | 3,820,000.00 USD | 3,820,000.00 USD | 33,360.00 USD | 38,620.00 USD | 64,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.30` | 5,130,000.00 USD | 5,130,000.00 USD | 48,850.00 USD | 11,000.00 USD | 36,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.40` | 3,910,000.00 USD | 3,910,000.00 USD | 26,490.00 USD | 18,940.00 USD | 50,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.40` | 5,260,000.00 USD | 5,260,000.00 USD | 27,290.00 USD | 9,260.00 USD | 86,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.50` | 3,940,000.00 USD | 3,940,000.00 USD | 21,130.00 USD | 6,460.00 USD | 124.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.50` | 5,280,000.00 USD | 5,280,000.00 USD | 2,060.00 USD | 24,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.60` | 4,010,000.00 USD | 4,010,000.00 USD | 21,940.00 USD | 5,920.00 USD | 40,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.60` | 5,390,000.00 USD | 5,390,000.00 USD | 30,680.00 USD | 20,260.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.70` | 4,090,000.00 USD | 4,090,000.00 USD | 44,920.00 USD | 10,120.00 USD | 29,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.70` | 5,450,000.00 USD | 5,450,000.00 USD | 15,810.00 USD | 11,600.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.80` | 4,160,000.00 USD | 4,160,000.00 USD | 36,630.00 USD | 9,890.00 USD | 23,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.80` | 5,460,000.00 USD | 5,460,000.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.90` | 4,340,000.00 USD | 4,340,000.00 USD | 22,130.00 USD | 60,970.00 USD | 90,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.90` | 5,600,000.00 USD | 5,600,000.00 USD | 2,140.00 USD | 54,240.00 USD | 83,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.00` | 4,650,000.00 USD | 4,650,000.00 USD | 129,990.00 USD | 58,870.00 USD | 129,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.00` | 6,050,000.00 USD | 6,050,000.00 USD | 259,280.00 USD | 65,270.00 USD | 118,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.10` | 4,950,000.00 USD | 4,950,000.00 USD | 92,240.00 USD | 39,740.00 USD | 163,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.10` | 6,340,000.00 USD | 6,340,000.00 USD | 93,390.00 USD | 45,400.00 USD | 158,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.20` | 5,160,000.00 USD | 5,160,000.00 USD | 102,940.00 USD | 59,320.00 USD | 49,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.20` | 6,690,000.00 USD | 6,690,000.00 USD | 153,580.00 USD | 18,540.00 USD | 174,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.30` | 5,400,000.00 USD | 5,400,000.00 USD | 146,220.00 USD | 30,070.00 USD | 66,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.30` | 6,960,000.00 USD | 6,960,000.00 USD | 88,710.00 USD | 67,460.00 USD | 114,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.40` | 5,520,000.00 USD | 5,520,000.00 USD | 35,110.00 USD | 30,780.00 USD | 49,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.40` | 7,280,000.00 USD | 7,280,000.00 USD | 107,040.00 USD | 73,620.00 USD | 137,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.50` | 5,670,000.00 USD | 5,670,000.00 USD | 81,240.00 USD | 34,430.00 USD | 32,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.50` | 7,430,000.00 USD | 7,430,000.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.60` | 5,770,000.00 USD | 5,770,000.00 USD | 43,950.00 USD | 51,200.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.60` | 7,940,000.00 USD | 7,940,000.00 USD | 270,460.00 USD | 147,800.00 USD | 86,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.70` | 5,870,000.00 USD | 5,870,000.00 USD | 10,330.00 USD | 18,330.00 USD | 72,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.70` | 8,260,000.00 USD | 8,260,000.00 USD | 55,510.00 USD | 99,970.00 USD | 162,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.80` | 5,930,000.00 USD | 5,930,000.00 USD | 32,130.00 USD | 26,470.00 USD | 6,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.80` | 8,620,000.00 USD | 8,620,000.00 USD | 118,240.00 USD | 91,980.00 USD | 154,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.90` | 6,100,000.00 USD | 6,100,000.00 USD | 102,020.00 USD | 17,810.00 USD | 50,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.90` | 8,830,000.00 USD | 8,830,000.00 USD | 142,290.00 USD | 34,490.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.00` | 6,350,000.00 USD | 6,350,000.00 USD | 162,970.00 USD | 29,090.00 USD | 50,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.00` | 9,080,000.00 USD | 9,080,000.00 USD | 100,570.00 USD | 67,520.00 USD | 83,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.10` | 6,500,000.00 USD | 6,500,000.00 USD | 64,550.00 USD | 28,140.00 USD | 57,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.10` | 9,460,000.00 USD | 9,460,000.00 USD | 200,540.00 USD | 84,980.00 USD | 95,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.20` | 6,660,000.00 USD | 6,660,000.00 USD | 59,560.00 USD | 19,740.00 USD | 82,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.20` | 9,830,000.00 USD | 9,830,000.00 USD | 162,230.00 USD | 99,360.00 USD | 108,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.30` | 6,770,000.00 USD | 6,770,000.00 USD | 53,910.00 USD | 31,630.00 USD | 26,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.30` | 10,230,000.00 USD | 10,230,000.00 USD | 133,350.00 USD | 100,380.00 USD | 170,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.40` | 6,890,000.00 USD | 6,890,000.00 USD | 66,740.00 USD | 13,730.00 USD | 42,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.40` | 10,600,000.00 USD | 10,600,000.00 USD | 64,850.00 USD | 100,560.00 USD | 202,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.50` | 6,970,000.00 USD | 6,970,000.00 USD | 22,700.00 USD | 19,320.00 USD | 36,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.50` | 10,970,000.00 USD | 10,970,000.00 USD | 115,390.00 USD | 80,510.00 USD | 175,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.60` | 7,030,000.00 USD | 7,030,000.00 USD | 40,710.00 USD | 19,140.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.60` | 11,360,000.00 USD | 11,360,000.00 USD | 251,100.00 USD | 18,640.00 USD | 118,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.70` | 7,090,000.00 USD | 7,090,000.00 USD | 31,880.00 USD | 22,330.00 USD | 3,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.70` | 11,560,000.00 USD | 11,560,000.00 USD | 119,080.00 USD | 57,480.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.80` | 7,160,000.00 USD | 7,160,000.00 USD | 11,060.00 USD | 12,060.00 USD | 47,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.80` | 11,710,000.00 USD | 11,710,000.00 USD | 46,960.00 USD | 28,960.00 USD | 76,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.90` | 7,240,000.00 USD | 7,240,000.00 USD | 34,200.00 USD | 23,250.00 USD | 22,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.90` | 11,920,000.00 USD | 11,920,000.00 USD | 105,970.00 USD | 33,290.00 USD | 64,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.00` | 7,310,000.00 USD | 7,310,000.00 USD | 43,930.00 USD | 6,430.00 USD | 18,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 11,970,000.00 USD | 11,970,000.00 USD | 43,120.00 USD | 11,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.10` | 7,350,000.00 USD | 7,350,000.00 USD | 12,400.00 USD | 13,980.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 12,010,000.00 USD | 12,010,000.00 USD | 31,540.00 USD | 10,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.20` | 7,470,000.00 USD | 7,470,000.00 USD | 76,240.00 USD | 1,880.00 USD | 39,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.20` | 12,130,000.00 USD | 12,130,000.00 USD | 51,210.00 USD | 20,920.00 USD | 47,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.30` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 4,040.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.30` | 12,190,000.00 USD | 12,190,000.00 USD | 16,510.00 USD | 13,210.00 USD | 24,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.40` | 7,480,000.00 USD | 7,480,000.00 USD | 1,190.00 USD | 709.61 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.40` | 12,320,000.00 USD | 12,320,000.00 USD | 62,340.00 USD | 25,720.00 USD | 43,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.50` | 7,490,000.00 USD | 7,490,000.00 USD | 1,060.00 USD | 3,880.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.50` | 12,420,000.00 USD | 12,420,000.00 USD | 17,710.00 USD | 42,440.00 USD | 41,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.60` | 7,510,000.00 USD | 7,510,000.00 USD | 9,250.00 USD | 11,890.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.60` | 12,630,000.00 USD | 12,630,000.00 USD | 32,920.00 USD | 58,350.00 USD | 121,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.70` | 7,550,000.00 USD | 7,550,000.00 USD | 13,890.00 USD | 8,790.00 USD | 10,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.70` | 12,830,000.00 USD | 12,830,000.00 USD | 82,860.00 USD | 10,880.00 USD | 99,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.80` | 7,570,000.00 USD | 7,570,000.00 USD | 9,150.00 USD | 3,440.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.80` | 13,090,000.00 USD | 13,090,000.00 USD | 169,680.00 USD | 25,670.00 USD | 71,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.90` | 7,590,000.00 USD | 7,590,000.00 USD | 8,160.00 USD | 1,580.00 USD | 11,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.90` | 13,240,000.00 USD | 13,240,000.00 USD | 73,690.00 USD | 32,820.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.00` | 7,610,000.00 USD | 7,610,000.00 USD | 12,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.00` | 13,340,000.00 USD | 13,340,000.00 USD | 50,080.00 USD | 8,550.00 USD | 40,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.10` | 13,350,000.00 USD | 13,350,000.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.20` | 13,470,000.00 USD | 13,470,000.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.30` | 13,610,000.00 USD | 13,610,000.00 USD | 27,500.00 USD | 23,450.00 USD | 97,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.40` | 13,740,000.00 USD | 13,740,000.00 USD | 74,860.00 USD | 27,560.00 USD | 25,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.50` | 13,820,000.00 USD | 13,820,000.00 USD | 36,690.00 USD | 12,720.00 USD | 25,700.00 USD | `Tier 1 CEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Map | Near Money | - | - | - | - | 0.00% | - |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 868,620.00 USD | 0.00 USD | 392.18 USD | `-63.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 868,230.00 USD | 0.00 USD | 2,310.00 USD | `-60.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 865,920.00 USD | 0.00 USD | 806.86 USD | `-54.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 865,110.00 USD | 0.00 USD | 1,560.00 USD | `-54.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 863,550.00 USD | 0.00 USD | 410.25 USD | `-50.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 863,140.00 USD | 0.00 USD | 281.57 USD | `-45.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 862,860.00 USD | 0.00 USD | 36,050.00 USD | `-35.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 826,810.00 USD | 0.00 USD | 37,550.00 USD | `-32.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 789,260.00 USD | 0.00 USD | 447.01 USD | `-31.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.35` | 788,820.00 USD | 0.00 USD | 73,350.00 USD | `-30.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 715,470.00 USD | 0.00 USD | 40,560.00 USD | `-29.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 674,910.00 USD | 0.00 USD | 489.57 USD | `-28.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 674,420.00 USD | 0.00 USD | 1,180.00 USD | `-28.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 673,240.00 USD | 0.00 USD | 9,840.00 USD | `-27.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 663,400.00 USD | 0.00 USD | 2,060.00 USD | `-26.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.05` | 661,350.00 USD | 0.00 USD | 2,060.00 USD | `-26.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 659,290.00 USD | 0.00 USD | 2,960.00 USD | `-25.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 656,330.00 USD | 0.00 USD | 4,010.00 USD | `-24.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.65` | 652,320.00 USD | 0.00 USD | 3,000.00 USD | `-23.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 649,310.00 USD | 0.00 USD | 5,680.00 USD | `-22.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 643,630.00 USD | 0.00 USD | 672.22 USD | `-21.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.35` | 642,960.00 USD | 0.00 USD | 329,970.00 USD | `-20.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 313,000.00 USD | 0.00 USD | 569.85 USD | `-19.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 312,430.00 USD | 0.00 USD | 223.20 USD | `-19.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 312,200.00 USD | 0.00 USD | 391.13 USD | `-19.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 311,810.00 USD | 0.00 USD | 7,080.00 USD | `-18.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 304,730.00 USD | 0.00 USD | 1,370.00 USD | `-17.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 303,370.00 USD | 0.00 USD | 553.80 USD | `-16.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.35` | 302,810.00 USD | 0.00 USD | 2,970.00 USD | `-16.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.45` | 299,840.00 USD | 0.00 USD | 3,080.00 USD | `-16.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 296,770.00 USD | 0.00 USD | 14,000.00 USD | `-15.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 282,770.00 USD | 0.00 USD | 158.56 USD | `-15.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 282,610.00 USD | 0.00 USD | 373.28 USD | `-14.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 282,240.00 USD | 0.00 USD | 849.46 USD | `-14.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 281,390.00 USD | 0.00 USD | 1,150.00 USD | `-13.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 280,240.00 USD | 0.00 USD | 129.25 USD | `-13.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.15` | 280,110.00 USD | 0.00 USD | 303.35 USD | `-13.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 279,810.00 USD | 0.00 USD | 1,740.00 USD | `-12.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 278,070.00 USD | 0.00 USD | 981.00 USD | `-11.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.35` | 277,090.00 USD | 0.00 USD | 817.24 USD | `-11.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 276,270.00 USD | 0.00 USD | 237.85 USD | `-10.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.55` | 276,030.00 USD | 0.00 USD | 879.51 USD | `-10.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.85` | 275,150.00 USD | 0.00 USD | 108.17 USD | `-10.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 275,040.00 USD | 0.00 USD | 298.20 USD | `-10.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 274,740.00 USD | 0.00 USD | 35,050.00 USD | `-9.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 239,700.00 USD | 0.00 USD | 6,410.00 USD | `-9.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 233,280.00 USD | 0.00 USD | 459.70 USD | `-9.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 232,820.00 USD | 0.00 USD | 236.57 USD | `-8.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 232,590.00 USD | 0.00 USD | 1,020.00 USD | `-8.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 231,570.00 USD | 0.00 USD | 439.89 USD | `-7.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.45` | 231,130.00 USD | 0.00 USD | 204.26 USD | `-7.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 230,920.00 USD | 0.00 USD | 11,560.00 USD | `-6.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.85` | 219,360.00 USD | 0.00 USD | 106.29 USD | `-6.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.95` | 219,250.00 USD | 0.00 USD | 8,700.00 USD | `-6.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 210,550.00 USD | 0.00 USD | 27,140.00 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.25` | 183,410.00 USD | 0.00 USD | 140.03 USD | `-5.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 183,270.00 USD | 0.00 USD | 18,390.00 USD | `-5.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 164,880.00 USD | 0.00 USD | 5,460.00 USD | `-5.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 159,420.00 USD | 0.00 USD | 53,020.00 USD | `-4.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.85` | 106,400.00 USD | 0.00 USD | 2,840.00 USD | `-4.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 103,560.00 USD | 0.00 USD | 115.43 USD | `-4.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 103,440.00 USD | 0.00 USD | 15,140.00 USD | `-4.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 88,300.00 USD | 0.00 USD | 2,660.00 USD | `-4.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.25` | 85,650.00 USD | 0.00 USD | 881.82 USD | `-4.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 84,760.00 USD | 0.00 USD | 566.57 USD | `-3.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 84,200.00 USD | 0.00 USD | 5,950.00 USD | `-3.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 78,250.00 USD | 0.00 USD | 1,370.00 USD | `-3.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.75` | 76,880.00 USD | 0.00 USD | 52,980.00 USD | `-3.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 23,900.00 USD | 0.00 USD | 462.03 USD | `-3.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 23,430.00 USD | 0.00 USD | 895.07 USD | `-2.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.15` | 22,540.00 USD | 0.00 USD | 398.54 USD | `-2.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 22,140.00 USD | 0.00 USD | 3,090.00 USD | `-2.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 19,050.00 USD | 0.00 USD | 958.73 USD | `-2.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.45` | 18,090.00 USD | 0.00 USD | 144.29 USD | `-1.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.55` | 17,950.00 USD | 0.00 USD | 788.25 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.65` | 17,160.00 USD | 0.00 USD | 13,660.00 USD | `-1.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.75` | 3,500.00 USD | 0.00 USD | 198.74 USD | `-1.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 3,300.00 USD | 0.00 USD | 398.21 USD | `-1.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.95` | 2,900.00 USD | 0.00 USD | 909.97 USD | `-1.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 1,990.00 USD | 0.00 USD | 160.75 USD | `-0.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.15` | 1,830.00 USD | 0.00 USD | 101.48 USD | `-0.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.25` | 1,730.00 USD | 0.00 USD | 914.94 USD | `-0.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.35` | 815.49 USD | 0.00 USD | 407.38 USD | `-0.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.45` | 408.11 USD | 0.00 USD | 408.11 USD | `-0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.55` | 156.65 USD | 156.65 USD | 0.00 USD | `+0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.65` | 355.32 USD | 198.67 USD | 0.00 USD | `+0.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.75` | 753.38 USD | 398.06 USD | 0.00 USD | `+0.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.85` | 1,550.00 USD | 797.54 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.95` | 1,740.00 USD | 193.03 USD | 0.00 USD | `+0.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.05` | 2,380.00 USD | 632.24 USD | 0.00 USD | `+0.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.15` | 2,570.00 USD | 197.65 USD | 0.00 USD | `+1.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.25` | 2,780.00 USD | 204.19 USD | 0.00 USD | `+1.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.35` | 3,170.00 USD | 387.12 USD | 0.00 USD | `+1.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.45` | 3,570.00 USD | 407.57 USD | 0.00 USD | `+1.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.55` | 6,210.00 USD | 2,640.00 USD | 0.00 USD | `+1.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.65` | 6,330.00 USD | 121.23 USD | 0.00 USD | `+2.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.75` | 6,440.00 USD | 104.42 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.85` | 24,460.00 USD | 18,030.00 USD | 0.00 USD | `+2.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.95` | 25,280.00 USD | 813.25 USD | 0.00 USD | `+2.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.05` | 26,280.00 USD | 1,000.00 USD | 0.00 USD | `+2.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.15` | 26,490.00 USD | 204.03 USD | 0.00 USD | `+2.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.25` | 27,920.00 USD | 1,440.00 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.35` | 28,130.00 USD | 207.03 USD | 0.00 USD | `+3.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.45` | 28,480.00 USD | 344.70 USD | 0.00 USD | `+3.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.55` | 48,830.00 USD | 20,360.00 USD | 0.00 USD | `+3.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.65` | 48,950.00 USD | 118.18 USD | 0.00 USD | `+3.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.75` | 49,070.00 USD | 119.54 USD | 0.00 USD | `+4.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 49,820.00 USD | 747.68 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 50,020.00 USD | 200.04 USD | 0.00 USD | `+4.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 50,220.00 USD | 200.96 USD | 0.00 USD | `+4.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 50,340.00 USD | 123.70 USD | 0.00 USD | `+5.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 50,950.00 USD | 601.45 USD | 0.00 USD | `+5.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 51,560.00 USD | 611.85 USD | 0.00 USD | `+5.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.65` | 51,830.00 USD | 274.48 USD | 0.00 USD | `+5.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 52,320.00 USD | 491.15 USD | 0.00 USD | `+5.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 55,270.00 USD | 2,940.00 USD | 0.00 USD | `+6.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 55,400.00 USD | 129.69 USD | 0.00 USD | `+6.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 60,200.00 USD | 4,800.00 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 61,480.00 USD | 1,280.00 USD | 0.00 USD | `+6.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.25` | 61,690.00 USD | 210.34 USD | 0.00 USD | `+6.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 62,150.00 USD | 461.74 USD | 0.00 USD | `+6.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 62,310.00 USD | 159.92 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 63,030.00 USD | 724.75 USD | 0.00 USD | `+7.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 63,190.00 USD | 158.00 USD | 0.00 USD | `+7.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 63,360.00 USD | 171.14 USD | 0.00 USD | `+8.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 63,910.00 USD | 551.00 USD | 0.00 USD | `+8.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.45` | 64,070.00 USD | 155.36 USD | 0.00 USD | `+8.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 64,950.00 USD | 878.58 USD | 0.00 USD | `+9.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 66,330.00 USD | 1,390.00 USD | 0.00 USD | `+9.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 67,320.00 USD | 986.99 USD | 0.00 USD | `+9.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 67,990.00 USD | 674.72 USD | 0.00 USD | `+9.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 70,360.00 USD | 2,360.00 USD | 0.00 USD | `+10.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 70,480.00 USD | 125.56 USD | 0.00 USD | `+10.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 74,080.00 USD | 3,600.00 USD | 0.00 USD | `+10.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 74,720.00 USD | 643.20 USD | 0.00 USD | `+10.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 74,850.00 USD | 130.31 USD | 0.00 USD | `+11.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.35` | 75,950.00 USD | 1,100.00 USD | 0.00 USD | `+12.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 76,670.00 USD | 716.72 USD | 0.00 USD | `+12.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 76,900.00 USD | 231.39 USD | 0.00 USD | `+13.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 77,530.00 USD | 630.87 USD | 0.00 USD | `+13.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 78,230.00 USD | 703.97 USD | 0.00 USD | `+13.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 78,900.00 USD | 668.13 USD | 0.00 USD | `+14.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 89,320.00 USD | 10,420.00 USD | 0.00 USD | `+14.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 89,880.00 USD | 555.03 USD | 0.00 USD | `+14.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 90,410.00 USD | 531.62 USD | 0.00 USD | `+15.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.35` | 91,070.00 USD | 664.09 USD | 0.00 USD | `+15.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.45` | 91,740.00 USD | 665.12 USD | 0.00 USD | `+16.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 91,940.00 USD | 202.69 USD | 0.00 USD | `+16.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 92,240.00 USD | 298.04 USD | 0.00 USD | `+16.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 92,340.00 USD | 102.13 USD | 0.00 USD | `+17.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 92,880.00 USD | 540.09 USD | 0.00 USD | `+17.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 92,980.00 USD | 100.79 USD | 0.00 USD | `+17.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 93,250.00 USD | 262.20 USD | 0.00 USD | `+18.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 93,620.00 USD | 371.49 USD | 0.00 USD | `+18.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 94,310.00 USD | 696.17 USD | 0.00 USD | `+18.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 94,850.00 USD | 534.00 USD | 0.00 USD | `+20.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 105,930.00 USD | 11,080.00 USD | 0.00 USD | `+20.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 112,630.00 USD | 6,710.00 USD | 0.00 USD | `+20.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.05` | 114,990.00 USD | 2,360.00 USD | 0.00 USD | `+22.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 119,860.00 USD | 4,860.00 USD | 0.00 USD | `+23.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 120,060.00 USD | 204.48 USD | 0.00 USD | `+25.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.65` | 638,260.00 USD | 518,200.00 USD | 0.00 USD | `+25.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 639,070.00 USD | 810.02 USD | 0.00 USD | `+26.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 958,960.00 USD | 319,890.00 USD | 0.00 USD | `+26.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 959,130.00 USD | 170.04 USD | 0.00 USD | `+27.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 964,900.00 USD | 5,770.00 USD | 0.00 USD | `+27.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 965,170.00 USD | 269.28 USD | 0.00 USD | `+27.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 965,460.00 USD | 291.40 USD | 0.00 USD | `+29.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 972,680.00 USD | 7,220.00 USD | 0.00 USD | `+29.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 972,830.00 USD | 156.78 USD | 0.00 USD | `+30.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 976,060.00 USD | 3,220.00 USD | 0.00 USD | `+30.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 976,470.00 USD | 411.14 USD | 0.00 USD | `+32.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 1,100,000.00 USD | 123,190.00 USD | 0.00 USD | `+33.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 1,100,000.00 USD | 1,020.00 USD | 0.00 USD | `+34.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.75` | 1,100,000.00 USD | 811.04 USD | 0.00 USD | `+34.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 1,100,000.00 USD | 104.93 USD | 0.00 USD | `+35.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 1,100,000.00 USD | 133.59 USD | 0.00 USD | `+35.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 1,100,000.00 USD | 402.59 USD | 0.00 USD | `+35.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.85` | 1,100,000.00 USD | 308.71 USD | 0.00 USD | `+36.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 1,100,000.00 USD | 315.18 USD | 0.00 USD | `+39.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 1,160,000.00 USD | 59,310.00 USD | 0.00 USD | `+41.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 1,170,000.00 USD | 3,160.00 USD | 0.00 USD | `+42.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.35` | 1,170,000.00 USD | 5,260.00 USD | 0.00 USD | `+42.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 1,180,000.00 USD | 5,690.00 USD | 0.00 USD | `+43.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 1,210,000.00 USD | 36,590.00 USD | 0.00 USD | `+44.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 1,210,000.00 USD | 433.89 USD | 0.00 USD | `+45.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 1,210,000.00 USD | 172.64 USD | 0.00 USD | `+46.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 1,210,000.00 USD | 164.10 USD | 0.00 USD | `+47.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 1,210,000.00 USD | 546.81 USD | 0.00 USD | `+49.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 1,220,000.00 USD | 2,300.00 USD | 0.00 USD | `+51.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 1,230,000.00 USD | 12,070.00 USD | 0.00 USD | `+53.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.05` | 1,250,000.00 USD | 20,230.00 USD | 0.00 USD | `+56.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 1,250,000.00 USD | 1,580.00 USD | 0.00 USD | `+58.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 1,290,000.00 USD | 37,000.00 USD | 0.00 USD | `+58.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 1,290,000.00 USD | 473.21 USD | 0.00 USD | `+60.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 1,290,000.00 USD | 422.99 USD | 0.00 USD | `+60.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 1,290,000.00 USD | 1,630.00 USD | 0.00 USD | `+61.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 1,290,000.00 USD | 4,870.00 USD | 0.00 USD | `+62.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 1,300,000.00 USD | 481.55 USD | 0.00 USD | `+64.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 1,300,000.00 USD | 1,330.00 USD | 0.00 USD | `+65.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 1,300,000.00 USD | 281.21 USD | 0.00 USD | `+69.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,560,000.00 USD | 266,140.00 USD | 0.00 USD | `+71.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,570,000.00 USD | 3,400.00 USD | 0.00 USD | `+71.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,590,000.00 USD | 21,930.00 USD | 0.00 USD | `+73.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,590,000.00 USD | 294.15 USD | 0.00 USD | `+76.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 1,600,000.00 USD | 15,380.00 USD | 0.00 USD | `+78.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,610,000.00 USD | 3,660.00 USD | 0.00 USD | `+80.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,610,000.00 USD | 306.15 USD | 0.00 USD | `+83.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,610,000.00 USD | 936.72 USD | 0.00 USD | `+85.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,610,000.00 USD | 2,920.00 USD | 0.00 USD | `+85.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,610,000.00 USD | 324.15 USD | 0.00 USD | `+94.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 1,610,000.00 USD | 123.23 USD | 0.00 USD | `+96.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 1,700,000.00 USD | 89,110.00 USD | 0.00 USD | `+100.04%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `47.20` | 8,220,000.00 USD | 0.00 USD | 8,220,000.00 USD | 9,650.00 USD | 2,470.00 USD | 114.09 USD |
| `7D` | `47.30` | 8,210,000.00 USD | 0.00 USD | 8,210,000.00 USD | 692.33 USD | 4,740.00 USD | 6,740.00 USD |
| `7D` | `47.40` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 0.00 USD | 1,520.00 USD | 28,650.00 USD |
| `7D` | `47.50` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 11,830.00 USD | 0.00 USD | 7,960.00 USD |
| `7D` | `48.10` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD |
| `7D` | `48.20` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD |
| `7D` | `48.40` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 0.00 USD | 6,080.00 USD | 0.00 USD |
| `7D` | `48.60` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `48.80` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 1,780.00 USD | 2,250.00 USD | 0.00 USD |
| `7D` | `48.90` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 960.40 USD |
| `7D` | `49.30` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 15,190.00 USD | 4,490.00 USD | 14,870.00 USD |
| `7D` | `49.40` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD |
| `7D` | `49.50` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 2,830.00 USD | 7,770.00 USD | 0.00 USD |
| `7D` | `49.60` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD |
| `7D` | `49.70` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 12,090.00 USD | 0.00 USD | 5,410.00 USD |
| `7D` | `49.80` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 9,930.00 USD | 8,220.00 USD | 0.00 USD |
| `1D` | `49.90` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 26,820.00 USD | 14,520.00 USD | 44,730.00 USD |
| `7D` | `49.90` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 45,030.00 USD | 8,880.00 USD | 4,700.00 USD |
| `1D` | `50.00` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 11,780.00 USD | 15,870.00 USD | 40,730.00 USD |
| `7D` | `50.00` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 22,100.00 USD | 19,810.00 USD | 24,920.00 USD |
| `1D` | `50.10` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 3,780.00 USD | 4,040.00 USD | 7,600.00 USD |
| `7D` | `50.10` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 363.50 USD | 682.90 USD | 8,340.00 USD |
| `1D` | `50.20` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 177.10 USD | 709.61 USD | 5,230.00 USD |
| `7D` | `50.20` | 7,880,000.00 USD | 0.00 USD | 7,880,000.00 USD | 6,960.00 USD | 500.40 USD | 42,940.00 USD |
| `1D` | `50.30` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 171.03 USD | 3,880.00 USD | 2,500.00 USD |
| `7D` | `50.30` | 7,830,000.00 USD | 0.00 USD | 7,830,000.00 USD | 16,270.00 USD | 10,780.00 USD | 7,240.00 USD |
| `1D` | `50.40` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 8,260.00 USD | 11,890.00 USD | 1,150.00 USD |
| `7D` | `50.40` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 28,280.00 USD | 26,580.00 USD | 33,450.00 USD |
| `1D` | `50.50` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 8,910.00 USD | 8,790.00 USD | 10,530.00 USD |
| `7D` | `50.50` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 32,490.00 USD | 6,790.00 USD | 44,380.00 USD |
| `1D` | `50.60` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 7,330.00 USD | 3,440.00 USD | 10,850.00 USD |
| `7D` | `50.60` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 67,580.00 USD | 21,530.00 USD | 31,730.00 USD |
| `1D` | `50.70` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 8,170.00 USD | 2,300.00 USD | 11,770.00 USD |
| `7D` | `50.70` | 7,500,000.00 USD | 0.00 USD | 7,500,000.00 USD | 65,920.00 USD | 32,820.00 USD | 41,580.00 USD |
| `1D` | `50.80` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 12,550.00 USD | 3,100.00 USD | 8,280.00 USD |
| `7D` | `50.80` | 7,360,000.00 USD | 0.00 USD | 7,360,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD |
| `1D` | `50.90` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 826.24 USD | 260.05 USD | 8,390.00 USD |
| `7D` | `50.90` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD |
| `1D` | `51.00` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 5,040.00 USD | 0.00 USD | 430.77 USD |
| `7D` | `51.00` | 7,010,000.00 USD | 0.00 USD | 7,010,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `51.10` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 9,210.00 USD | 6,650.00 USD | 0.00 USD |
| `7D` | `51.10` | 6,890,000.00 USD | 0.00 USD | 6,890,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD |
| `1D` | `51.20` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 1,770.00 USD | 1,130.00 USD | 19,220.00 USD |
| `7D` | `51.20` | 6,810,000.00 USD | 0.00 USD | 6,810,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD |
| `1D` | `51.30` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 8,650.00 USD | 9,710.00 USD | 0.00 USD |
| `7D` | `51.30` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 28,400.00 USD | 26,720.00 USD | 47,090.00 USD |
| `1D` | `51.40` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 3,250.00 USD | 5,610.00 USD | 416.23 USD |
| `7D` | `51.40` | 6,640,000.00 USD | 0.00 USD | 6,640,000.00 USD | 73,130.00 USD | 42,820.00 USD | 46,140.00 USD |
| `1D` | `51.50` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 5,650.00 USD | 10,010.00 USD | 41,600.00 USD |
| `7D` | `51.50` | 6,480,000.00 USD | 0.00 USD | 6,480,000.00 USD | 38,520.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `51.60` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 9,060.00 USD | 18,580.00 USD | 757.87 USD |
| `7D` | `51.60` | 6,380,000.00 USD | 0.00 USD | 6,380,000.00 USD | 37,880.00 USD | 36,790.00 USD | 41,490.00 USD |
| `1D` | `51.70` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 2,890.00 USD | 13,780.00 USD | 4,100.00 USD |
| `7D` | `51.70` | 6,260,000.00 USD | 0.00 USD | 6,260,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `51.80` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 13,770.00 USD | 19,520.00 USD | 14,360.00 USD |
| `7D` | `51.80` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD |
| `1D` | `51.90` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 10,140.00 USD | 19,910.00 USD | 23,480.00 USD |
| `7D` | `51.90` | 6,170,000.00 USD | 0.00 USD | 6,170,000.00 USD | 5,870.00 USD | 25,410.00 USD | 28,190.00 USD |
| `1D` | `52.00` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 20,980.00 USD | 25,620.00 USD | 24,820.00 USD |
| `7D` | `52.00` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 65,840.00 USD | 26,440.00 USD | 11,880.00 USD |
| `1D` | `52.10` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 34,970.00 USD | 17,300.00 USD | 50,500.00 USD |
| `7D` | `52.10` | 6,010,000.00 USD | 0.00 USD | 6,010,000.00 USD | 24,220.00 USD | 28,090.00 USD | 37,880.00 USD |
| `1D` | `52.20` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 15,890.00 USD | 7,630.00 USD | 49,960.00 USD |
| `7D` | `52.20` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 38,380.00 USD | 13,960.00 USD | 25,270.00 USD |
| `1D` | `52.30` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 26,510.00 USD | 22,090.00 USD | 11,210.00 USD |
| `7D` | `52.30` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 26,450.00 USD | 40,700.00 USD | 7,980.00 USD |
| `1D` | `52.40` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 13,070.00 USD | 15,400.00 USD | 7,040.00 USD |
| `7D` | `52.40` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 20,580.00 USD | 38,950.00 USD | 22,030.00 USD |
| `1D` | `52.50` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 53,990.00 USD | 30,000.00 USD | 79,400.00 USD |
| `7D` | `52.50` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 40,460.00 USD | 667.05 USD | 11,240.00 USD |
| `1D` | `52.60` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 8,330.00 USD | 43,700.00 USD | 5,450.00 USD |
| `7D` | `52.60` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 73,920.00 USD | 32,590.00 USD | 59,410.00 USD |
| `1D` | `52.70` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 18,270.00 USD | 19,780.00 USD | 40,000.00 USD |
| `7D` | `52.70` | 5,460,000.00 USD | 0.00 USD | 5,460,000.00 USD | 19,550.00 USD | 75,910.00 USD | 108,640.00 USD |
| `1D` | `52.80` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 28,000.00 USD | 50,850.00 USD | 72,920.00 USD |
| `7D` | `52.80` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 30,590.00 USD | 25,700.00 USD | 0.00 USD |
| `1D` | `52.90` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 43,760.00 USD | 50,880.00 USD | 30,100.00 USD |
| `7D` | `52.90` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 30,900.00 USD | 11,650.00 USD | 34,400.00 USD |
| `1D` | `53.00` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 26,800.00 USD | 30,500.00 USD | 39,600.00 USD |
| `7D` | `53.00` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 39,690.00 USD | 22,700.00 USD | 77,700.00 USD |
| `1D` | `53.10` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 12,590.00 USD | 43,040.00 USD | 85,170.00 USD |
| `7D` | `53.10` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 45,320.00 USD | 17,950.00 USD | 0.00 USD |
| `1D` | `53.20` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 20,660.00 USD | 9,840.00 USD | 42,110.00 USD |
| `7D` | `53.20` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 162,460.00 USD | 32,580.00 USD | 23,350.00 USD |
| `1D` | `53.30` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 5,080.00 USD | 25,160.00 USD | 5,690.00 USD |
| `7D` | `53.30` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 59,390.00 USD | 49,210.00 USD | 35,070.00 USD |
| `1D` | `53.40` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 12,600.00 USD | 10,640.00 USD | 4,540.00 USD |
| `7D` | `53.40` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 44,030.00 USD | 17,420.00 USD | 91,220.00 USD |
| `1D` | `53.50` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 9,960.00 USD | 5,700.00 USD | 22,000.00 USD |
| `7D` | `53.50` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 60,260.00 USD | 3,440.00 USD | 28,500.00 USD |
| `1D` | `53.60` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 75,950.00 USD | 3,830.00 USD | 20,970.00 USD |
| `7D` | `53.60` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 52,800.00 USD | 3,780.00 USD | 20,660.00 USD |
| `1D` | `53.70` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 6,210.00 USD | 11,100.00 USD | 11,960.00 USD |
| `7D` | `53.70` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 131,400.00 USD | 21,330.00 USD | 13,220.00 USD |
| `1D` | `53.80` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 53,640.00 USD | 28,920.00 USD | 4,830.00 USD |
| `7D` | `53.80` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 99,150.00 USD | 43,900.00 USD | 302.55 USD |
| `1D` | `53.90` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 51,060.00 USD | 39,560.00 USD | 27,830.00 USD |
| `7D` | `53.90` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 160,820.00 USD | 22,780.00 USD | 9,680.00 USD |
| `1D` | `54.00` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 76,010.00 USD | 21,440.00 USD | 86,580.00 USD |
| `7D` | `54.00` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 380,340.00 USD | 71,820.00 USD | 304,530.00 USD |
| `1D` | `54.10` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 94,870.00 USD | 19,160.00 USD | 49,170.00 USD |
| `7D` | `54.10` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 302,190.00 USD | 0.00 USD | 2,590.00 USD |
| `1D` | `54.20` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 72,600.00 USD | 15,510.00 USD | 40,120.00 USD |
| `7D` | `54.20` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 205,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `54.30` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 15,600.00 USD | 6,650.00 USD | 5,470.00 USD |
| `7D` | `54.30` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 381,380.00 USD | 8,520.00 USD | 181,420.00 USD |
| `1D` | `54.40` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 56,350.00 USD | 85,810.00 USD | 3,290.00 USD |
| `7D` | `54.40` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 304,270.00 USD | 63,170.00 USD | 92,650.00 USD |
| `1D` | `54.50` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 26,610.00 USD | 64,250.00 USD | 9,090.00 USD |
| `7D` | `54.50` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 159,720.00 USD | 35,580.00 USD | 239,890.00 USD |
| `1D` | `54.60` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 913.17 USD | 25,490.00 USD | 43,580.00 USD |
| `7D` | `54.60` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 18,530.00 USD | 1,930.00 USD | 131,380.00 USD |
| `1D` | `54.70` | 953,500.00 USD | 0.00 USD | 953,500.00 USD | 6,600.00 USD | 23,060.00 USD | 105,800.00 USD |
| `7D` | `54.70` | 850,330.00 USD | 0.00 USD | 850,330.00 USD | 0.00 USD | 3,600.00 USD | 41,310.00 USD |
| `1D` | `54.80` | 818,040.00 USD | 0.00 USD | 818,040.00 USD | 0.00 USD | 48,420.00 USD | 23,920.00 USD |
| `7D` | `54.80` | 805,420.00 USD | 0.00 USD | 805,420.00 USD | 0.00 USD | 35,700.00 USD | 26,440.00 USD |
| `1D` | `54.90` | 745,700.00 USD | 0.00 USD | 745,700.00 USD | 66,900.00 USD | 65,440.00 USD | 10,850.00 USD |
| `7D` | `54.90` | 743,280.00 USD | 0.00 USD | 743,280.00 USD | 0.00 USD | 112,280.00 USD | 48,290.00 USD |
| `1D` | `55.00` | 602,520.00 USD | 0.00 USD | 602,520.00 USD | 40,710.00 USD | 54,150.00 USD | 55,190.00 USD |
| `7D` | `55.00` | 582,710.00 USD | 0.00 USD | 582,710.00 USD | 97,700.00 USD | 2,830.00 USD | 19,360.00 USD |
| `1D` | `55.10` | 452,460.00 USD | 0.00 USD | 452,460.00 USD | 50,530.00 USD | 62,170.00 USD | 80,200.00 USD |
| `7D` | `55.10` | 462,820.00 USD | 0.00 USD | 462,820.00 USD | 54,590.00 USD | 18,510.00 USD | 64,690.00 USD |
| `1D` | `55.20` | 259,560.00 USD | 0.00 USD | 259,560.00 USD | 39,390.00 USD | 11,830.00 USD | 66,410.00 USD |
| `7D` | `55.20` | 325,040.00 USD | 0.00 USD | 325,040.00 USD | 57,400.00 USD | 59,710.00 USD | 150,160.00 USD |
| `1D` | `55.30` | 141,940.00 USD | 0.00 USD | 141,940.00 USD | 52,860.00 USD | 22,650.00 USD | 59,180.00 USD |
| `7D` | `55.30` | 57,770.00 USD | 0.00 USD | 57,770.00 USD | 23,140.00 USD | 11,270.00 USD | 0.00 USD |
| `1D` | `55.40` | 7,250.00 USD | 0.00 USD | 7,250.00 USD | 0.00 USD | 6,510.00 USD | 742.75 USD |
| `7D` | `55.40` | 23,360.00 USD | 0.00 USD | 23,360.00 USD | 0.00 USD | 18,550.00 USD | 4,800.00 USD |
| `1D` | `55.50` | 5,500.00 USD | 5,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD |
| `1D` | `55.50` | 11,000.00 USD | 11,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD |
| `7D` | `55.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `55.70` | 19,310.00 USD | 19,310.00 USD | 0.00 USD | 0.00 USD | 7,700.00 USD | 613.46 USD |
| `7D` | `55.70` | 206,420.00 USD | 206,420.00 USD | 0.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD |
| `1D` | `55.80` | 22,490.00 USD | 22,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,170.00 USD |
| `7D` | `55.80` | 297,390.00 USD | 297,390.00 USD | 0.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD |
| `1D` | `55.90` | 75,550.00 USD | 75,550.00 USD | 0.00 USD | 51,520.00 USD | 0.00 USD | 1,550.00 USD |
| `7D` | `55.90` | 438,720.00 USD | 438,720.00 USD | 0.00 USD | 141,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `56.00` | 79,930.00 USD | 79,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,380.00 USD |
| `7D` | `56.00` | 609,830.00 USD | 609,830.00 USD | 0.00 USD | 2,590.00 USD | 0.00 USD | 168,520.00 USD |
| `7D` | `56.20` | 689,780.00 USD | 689,780.00 USD | 0.00 USD | 0.00 USD | 79,940.00 USD | 0.00 USD |
| `1D` | `56.30` | 83,880.00 USD | 83,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,950.00 USD |
| `7D` | `56.30` | 692,370.00 USD | 692,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,590.00 USD |
| `1D` | `56.40` | 108,220.00 USD | 108,220.00 USD | 0.00 USD | 5,040.00 USD | 16,820.00 USD | 2,470.00 USD |
| `7D` | `56.40` | 706,060.00 USD | 706,060.00 USD | 0.00 USD | 2,650.00 USD | 11,040.00 USD | 0.00 USD |
| `1D` | `56.50` | 500,310.00 USD | 500,310.00 USD | 0.00 USD | 138,540.00 USD | 108,630.00 USD | 144,920.00 USD |
| `7D` | `56.50` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 170,750.00 USD | 151,940.00 USD | 6,150.00 USD |
| `1D` | `56.60` | 790,260.00 USD | 790,260.00 USD | 0.00 USD | 54,340.00 USD | 154,550.00 USD | 81,070.00 USD |
| `7D` | `56.60` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 363,190.00 USD | 185,910.00 USD | 507.54 USD |
| `1D` | `56.70` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 114,230.00 USD | 45,300.00 USD | 315,590.00 USD |
| `7D` | `56.70` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 117,290.00 USD | 141,830.00 USD | 98,950.00 USD |
| `1D` | `56.80` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 117,760.00 USD | 20,790.00 USD | 106,140.00 USD |
| `7D` | `56.80` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 172,110.00 USD | 92,780.00 USD | 318,330.00 USD |
| `1D` | `56.90` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 45,140.00 USD | 17,930.00 USD | 35,720.00 USD |
| `7D` | `56.90` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 113,780.00 USD | 52,200.00 USD | 307,930.00 USD |
| `1D` | `57.00` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 6,480.00 USD | 43,030.00 USD | 29,740.00 USD |
| `7D` | `57.00` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 88,680.00 USD | 56,390.00 USD | 178,370.00 USD |
| `1D` | `57.10` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 77,000.00 USD | 77,400.00 USD | 46,610.00 USD |
| `7D` | `57.10` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 36,580.00 USD | 79,290.00 USD | 21,040.00 USD |
| `1D` | `57.20` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 53,080.00 USD | 78,490.00 USD | 120,900.00 USD |
| `7D` | `57.20` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 118,850.00 USD | 23,920.00 USD | 23,060.00 USD |
| `1D` | `57.30` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 70,930.00 USD | 44,630.00 USD | 87,180.00 USD |
| `7D` | `57.30` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 76,940.00 USD | 28,570.00 USD | 98,930.00 USD |
| `1D` | `57.40` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 84,960.00 USD | 49,470.00 USD | 78,400.00 USD |
| `7D` | `57.40` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 124,180.00 USD | 72,180.00 USD | 257,020.00 USD |
| `1D` | `57.50` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 197,830.00 USD | 48,350.00 USD | 174,740.00 USD |
| `7D` | `57.50` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 99,810.00 USD | 31,830.00 USD | 0.00 USD |
| `1D` | `57.60` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 69,720.00 USD | 27,370.00 USD | 62,570.00 USD |
| `7D` | `57.60` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 149,560.00 USD | 44,690.00 USD | 28,320.00 USD |
| `1D` | `57.70` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 39,010.00 USD | 51,220.00 USD | 96,430.00 USD |
| `7D` | `57.70` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 30,070.00 USD | 57,580.00 USD |
| `1D` | `57.80` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 18,150.00 USD | 22,650.00 USD | 77,220.00 USD |
| `7D` | `57.80` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 9,650.00 USD | 24,520.00 USD | 49,480.00 USD |
| `1D` | `57.90` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 13,000.00 USD | 15,870.00 USD | 28,950.00 USD |
| `7D` | `57.90` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 14,390.00 USD | 963.90 USD | 30,010.00 USD |
| `1D` | `58.00` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 7,880.00 USD | 9,480.00 USD | 15,330.00 USD |
| `7D` | `58.00` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD | 107,350.00 USD |
| `1D` | `58.10` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 31,400.00 USD | 17,830.00 USD | 21,300.00 USD |
| `7D` | `58.10` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 5,470.00 USD | 19,160.00 USD | 14,070.00 USD |
| `1D` | `58.20` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 35,920.00 USD | 34,800.00 USD | 4,940.00 USD |
| `7D` | `58.20` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 31,590.00 USD | 302.55 USD |
| `1D` | `58.30` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 33,360.00 USD | 38,620.00 USD | 64,380.00 USD |
| `7D` | `58.30` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 48,850.00 USD | 11,000.00 USD | 36,500.00 USD |
| `1D` | `58.40` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 26,490.00 USD | 18,940.00 USD | 50,160.00 USD |
| `7D` | `58.40` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 27,290.00 USD | 9,260.00 USD | 86,460.00 USD |
| `1D` | `58.50` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 21,130.00 USD | 6,460.00 USD | 124.02 USD |
| `7D` | `58.50` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 2,060.00 USD | 24,530.00 USD | 0.00 USD |
| `1D` | `58.60` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 21,940.00 USD | 5,920.00 USD | 40,890.00 USD |
| `7D` | `58.60` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 30,680.00 USD | 20,260.00 USD | 51,650.00 USD |
| `1D` | `58.70` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 44,920.00 USD | 10,120.00 USD | 29,940.00 USD |
| `7D` | `58.70` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 15,810.00 USD | 11,600.00 USD | 35,320.00 USD |
| `1D` | `58.80` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 36,630.00 USD | 9,890.00 USD | 23,340.00 USD |
| `7D` | `58.80` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD |
| `1D` | `58.90` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 22,130.00 USD | 60,970.00 USD | 90,490.00 USD |
| `7D` | `58.90` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 2,140.00 USD | 54,240.00 USD | 83,500.00 USD |
| `1D` | `59.00` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 129,990.00 USD | 58,870.00 USD | 129,440.00 USD |
| `7D` | `59.00` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 259,280.00 USD | 65,270.00 USD | 118,570.00 USD |
| `1D` | `59.10` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 92,240.00 USD | 39,740.00 USD | 163,590.00 USD |
| `7D` | `59.10` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 93,390.00 USD | 45,400.00 USD | 158,780.00 USD |
| `1D` | `59.20` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 102,940.00 USD | 59,320.00 USD | 49,210.00 USD |
| `7D` | `59.20` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 153,580.00 USD | 18,540.00 USD | 174,600.00 USD |
| `1D` | `59.30` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 146,220.00 USD | 30,070.00 USD | 66,050.00 USD |
| `7D` | `59.30` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 88,710.00 USD | 67,460.00 USD | 114,310.00 USD |
| `1D` | `59.40` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 35,110.00 USD | 30,780.00 USD | 49,030.00 USD |
| `7D` | `59.40` | 7,280,000.00 USD | 7,280,000.00 USD | 0.00 USD | 107,040.00 USD | 73,620.00 USD | 137,500.00 USD |
| `1D` | `59.50` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 81,240.00 USD | 34,430.00 USD | 32,440.00 USD |
| `7D` | `59.50` | 7,430,000.00 USD | 7,430,000.00 USD | 0.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD |
| `1D` | `59.60` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 43,950.00 USD | 51,200.00 USD | 5,300.00 USD |
| `7D` | `59.60` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 270,460.00 USD | 147,800.00 USD | 86,840.00 USD |
| `1D` | `59.70` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 10,330.00 USD | 18,330.00 USD | 72,170.00 USD |
| `7D` | `59.70` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 55,510.00 USD | 99,970.00 USD | 162,850.00 USD |
| `1D` | `59.80` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 32,130.00 USD | 26,470.00 USD | 6,220.00 USD |
| `7D` | `59.80` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 118,240.00 USD | 91,980.00 USD | 154,560.00 USD |
| `1D` | `59.90` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 102,020.00 USD | 17,810.00 USD | 50,060.00 USD |
| `7D` | `59.90` | 8,830,000.00 USD | 8,830,000.00 USD | 0.00 USD | 142,290.00 USD | 34,490.00 USD | 29,380.00 USD |
| `1D` | `60.00` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 162,970.00 USD | 29,090.00 USD | 50,570.00 USD |
| `7D` | `60.00` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 100,570.00 USD | 67,520.00 USD | 83,920.00 USD |
| `1D` | `60.10` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 64,550.00 USD | 28,140.00 USD | 57,080.00 USD |
| `7D` | `60.10` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 200,540.00 USD | 84,980.00 USD | 95,670.00 USD |
| `1D` | `60.20` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 59,560.00 USD | 19,740.00 USD | 82,270.00 USD |
| `7D` | `60.20` | 9,830,000.00 USD | 9,830,000.00 USD | 0.00 USD | 162,230.00 USD | 99,360.00 USD | 108,990.00 USD |
| `1D` | `60.30` | 6,770,000.00 USD | 6,770,000.00 USD | 0.00 USD | 53,910.00 USD | 31,630.00 USD | 26,470.00 USD |
| `7D` | `60.30` | 10,230,000.00 USD | 10,230,000.00 USD | 0.00 USD | 133,350.00 USD | 100,380.00 USD | 170,480.00 USD |
| `1D` | `60.40` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 66,740.00 USD | 13,730.00 USD | 42,520.00 USD |
| `7D` | `60.40` | 10,600,000.00 USD | 10,600,000.00 USD | 0.00 USD | 64,850.00 USD | 100,560.00 USD | 202,370.00 USD |
| `1D` | `60.50` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 22,700.00 USD | 19,320.00 USD | 36,200.00 USD |
| `7D` | `60.50` | 10,970,000.00 USD | 10,970,000.00 USD | 0.00 USD | 115,390.00 USD | 80,510.00 USD | 175,550.00 USD |
| `1D` | `60.60` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 40,710.00 USD | 19,140.00 USD | 3,930.00 USD |
| `7D` | `60.60` | 11,360,000.00 USD | 11,360,000.00 USD | 0.00 USD | 251,100.00 USD | 18,640.00 USD | 118,680.00 USD |
| `1D` | `60.70` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 31,880.00 USD | 22,330.00 USD | 3,120.00 USD |
| `7D` | `60.70` | 11,560,000.00 USD | 11,560,000.00 USD | 0.00 USD | 119,080.00 USD | 57,480.00 USD | 22,840.00 USD |
| `1D` | `60.80` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 11,060.00 USD | 12,060.00 USD | 47,810.00 USD |
| `7D` | `60.80` | 11,710,000.00 USD | 11,710,000.00 USD | 0.00 USD | 46,960.00 USD | 28,960.00 USD | 76,200.00 USD |
| `1D` | `60.90` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 34,200.00 USD | 23,250.00 USD | 22,870.00 USD |
| `7D` | `60.90` | 11,920,000.00 USD | 11,920,000.00 USD | 0.00 USD | 105,970.00 USD | 33,290.00 USD | 64,920.00 USD |
| `1D` | `61.00` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 43,930.00 USD | 6,430.00 USD | 18,420.00 USD |
| `7D` | `61.00` | 11,970,000.00 USD | 11,970,000.00 USD | 0.00 USD | 43,120.00 USD | 11,530.00 USD | 0.00 USD |
| `1D` | `61.10` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 12,400.00 USD | 13,980.00 USD | 11,520.00 USD |
| `7D` | `61.10` | 12,010,000.00 USD | 12,010,000.00 USD | 0.00 USD | 31,540.00 USD | 10,430.00 USD | 0.00 USD |
| `1D` | `61.20` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 76,240.00 USD | 1,880.00 USD | 39,080.00 USD |
| `7D` | `61.20` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 51,210.00 USD | 20,920.00 USD | 47,810.00 USD |
| `1D` | `61.30` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 4,040.00 USD | 7,600.00 USD |
| `7D` | `61.30` | 12,190,000.00 USD | 12,190,000.00 USD | 0.00 USD | 16,510.00 USD | 13,210.00 USD | 24,230.00 USD |
| `1D` | `61.40` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 1,190.00 USD | 709.61 USD | 5,230.00 USD |
| `7D` | `61.40` | 12,320,000.00 USD | 12,320,000.00 USD | 0.00 USD | 62,340.00 USD | 25,720.00 USD | 43,510.00 USD |
| `1D` | `61.50` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 1,060.00 USD | 3,880.00 USD | 2,500.00 USD |
| `7D` | `61.50` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 17,710.00 USD | 42,440.00 USD | 41,390.00 USD |
| `1D` | `61.60` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 9,250.00 USD | 11,890.00 USD | 1,150.00 USD |
| `7D` | `61.60` | 12,630,000.00 USD | 12,630,000.00 USD | 0.00 USD | 32,920.00 USD | 58,350.00 USD | 121,470.00 USD |
| `1D` | `61.70` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 13,890.00 USD | 8,790.00 USD | 10,530.00 USD |
| `7D` | `61.70` | 12,830,000.00 USD | 12,830,000.00 USD | 0.00 USD | 82,860.00 USD | 10,880.00 USD | 99,740.00 USD |
| `1D` | `61.80` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 9,150.00 USD | 3,440.00 USD | 10,850.00 USD |
| `7D` | `61.80` | 13,090,000.00 USD | 13,090,000.00 USD | 0.00 USD | 169,680.00 USD | 25,670.00 USD | 71,530.00 USD |
| `1D` | `61.90` | 7,590,000.00 USD | 7,590,000.00 USD | 0.00 USD | 8,160.00 USD | 1,580.00 USD | 11,700.00 USD |
| `7D` | `61.90` | 13,240,000.00 USD | 13,240,000.00 USD | 0.00 USD | 73,690.00 USD | 32,820.00 USD | 41,580.00 USD |
| `1D` | `62.00` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 12,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.00` | 13,340,000.00 USD | 13,340,000.00 USD | 0.00 USD | 50,080.00 USD | 8,550.00 USD | 40,590.00 USD |
| `7D` | `62.10` | 13,350,000.00 USD | 13,350,000.00 USD | 0.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.20` | 13,470,000.00 USD | 13,470,000.00 USD | 0.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD |
| `7D` | `62.30` | 13,610,000.00 USD | 13,610,000.00 USD | 0.00 USD | 27,500.00 USD | 23,450.00 USD | 97,450.00 USD |
| `7D` | `62.40` | 13,740,000.00 USD | 13,740,000.00 USD | 0.00 USD | 74,860.00 USD | 27,560.00 USD | 25,440.00 USD |
| `7D` | `62.50` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 36,690.00 USD | 12,720.00 USD | 25,700.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `410.45M` | Total OI Tokens: `7,379,507.6 LTC`
  * 1h OI Change: `-0.28%` | 4h OI Change: `-1.96%` | 24h OI Change: `-8.81%`
  * Exchange Breakdown: Binance=`72.81M` | Bybit=`66.69M` | OKX=`34.26M` | Hyperliquid=`22.23M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `10.90K` | Last 24h: `29.34K` | Last 3d: `56.60K` | Last 7d: `113.64K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0003%` |
| **USDT Bybit** | `0.0084%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0030%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `55.54%` | `44.46%` | `1.25` | 7,100,000.00 USD |
| `15M` | `Binance` | `56.37%` | `43.63%` | `1.29` | 3,160,000.00 USD |
| `15M` | `OKX` | `54.19%` | `45.81%` | `1.18` | 388,390.00 USD |
| `15M` | `Bybit` | `53.91%` | `46.09%` | `1.17` | 613,730.00 USD |
| `15M` | `KuCoin` | `55.64%` | `44.36%` | `1.25` | 100,870.00 USD |
| `15M` | `Gate` | `53.7%` | `46.3%` | `1.16` | 91,470.00 USD |
| `15M` | `Bitget` | `39.83%` | `60.17%` | `0.66` | 336,190.00 USD |
| `15M` | `BingX` | `45.61%` | `54.39%` | `0.84` | 830,830.00 USD |
| `15M` | `MEXC` | `54.88%` | `45.12%` | `1.22` | 637,950.00 USD |
| `15M` | `Bitunix` | `48.41%` | `51.59%` | `0.94` | 514,340.00 USD |
| `15M` | `Hyperliquid` | `66.43%` | `33.57%` | `1.98` | 22,860.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.41%` | `51.59%` | `0.94` | 55,610.00 USD |
| `15M` | `Crypto.com` | `13.37%` | `86.63%` | `0.15` | 0.00 USD |
| `15M` | `WhiteBIT` | `42.53%` | `57.47%` | `0.74` | 275,500.00 USD |
| `15M` | `HTX` | `42.55%` | `57.45%` | `0.74` | 22,280.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `57.24%` | `42.76%` | `1.34` | 44,120.00 USD |
| `15M` | `Aster` | `42.61%` | `57.39%` | `0.74` | 1,250.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `56.54%` | `43.46%` | `1.30` | 941.79 USD |
| `15M` | `Whale Positions` | `56.37%` | `43.63%` | `1.29` | 3,160,000.00 USD |
| `15M` | `Global Accounts` | `55.54%` | `44.46%` | `1.25` | 7,100,000.00 USD |
| `1H` | `LTC` | `47.41%` | `52.59%` | `0.90` | 23,390,000.00 USD |
| `1H` | `Binance` | `49.17%` | `50.83%` | `0.97` | 8,540,000.00 USD |
| `1H` | `OKX` | `47.35%` | `52.65%` | `0.90` | 1,990,000.00 USD |
| `1H` | `Bybit` | `47.29%` | `52.71%` | `0.90` | 2,030,000.00 USD |
| `1H` | `KuCoin` | `58.73%` | `41.27%` | `1.42` | 378,190.00 USD |
| `1H` | `Gate` | `54.35%` | `45.65%` | `1.19` | 857,910.00 USD |
| `1H` | `Bitget` | `47.88%` | `52.12%` | `0.92` | 1,020,000.00 USD |
| `1H` | `BingX` | `11.93%` | `88.07%` | `0.14` | 2,440,000.00 USD |
| `1H` | `MEXC` | `49.56%` | `50.44%` | `0.98` | 3,490,000.00 USD |
| `1H` | `Bitunix` | `53.16%` | `46.84%` | `1.13` | 921,890.00 USD |
| `1H` | `Hyperliquid` | `43.53%` | `56.47%` | `0.77` | 271,920.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.08%` | `51.92%` | `0.93` | 269,040.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `99.54%` | `0.46%` | `216.39` | 958,490.00 USD |
| `1H` | `HTX` | `45.27%` | `54.73%` | `0.83` | 47,660.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `43.67%` | `56.33%` | `0.78` | 161,680.00 USD |
| `1H` | `Aster` | `45.82%` | `54.18%` | `0.85` | 24,550.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `36.17%` | `63.83%` | `0.57` | 6,640.00 USD |
| `1H` | `Whale Positions` | `49.17%` | `50.83%` | `0.97` | 8,540,000.00 USD |
| `1H` | `Global Accounts` | `47.41%` | `52.59%` | `0.90` | 23,390,000.00 USD |
| `4H` | `LTC` | `46.37%` | `53.63%` | `0.86` | 112,400,000.00 USD |
| `4H` | `Binance` | `45.05%` | `54.95%` | `0.82` | 45,840,000.00 USD |
| `4H` | `OKX` | `41.35%` | `58.65%` | `0.71` | 13,590,000.00 USD |
| `4H` | `Bybit` | `47.7%` | `52.3%` | `0.91` | 10,860,000.00 USD |
| `4H` | `KuCoin` | `47.17%` | `52.83%` | `0.89` | 1,490,000.00 USD |
| `4H` | `Gate` | `58.5%` | `41.5%` | `1.41` | 3,060,000.00 USD |
| `4H` | `Bitget` | `48.18%` | `51.82%` | `0.93` | 5,310,000.00 USD |
| `4H` | `BingX` | `23.88%` | `76.12%` | `0.31` | 5,140,000.00 USD |
| `4H` | `MEXC` | `45.57%` | `54.43%` | `0.84` | 15,350,000.00 USD |
| `4H` | `Bitunix` | `50.77%` | `49.23%` | `1.03` | 3,900,000.00 USD |
| `4H` | `Hyperliquid` | `42.67%` | `57.33%` | `0.74` | 1,600,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `57.52%` | `42.48%` | `1.35` | 2,210,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `96.68%` | `3.32%` | `29.12` | 3,170,000.00 USD |
| `4H` | `HTX` | `40.69%` | `59.31%` | `0.69` | 299,360.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `42.27%` | `57.73%` | `0.73` | 170,610.00 USD |
| `4H` | `Aster` | `46.7%` | `53.3%` | `0.88` | 266,940.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `56.83%` | `43.17%` | `1.32` | 135,340.00 USD |
| `4H` | `Whale Positions` | `45.05%` | `54.95%` | `0.82` | 45,840,000.00 USD |
| `4H` | `Global Accounts` | `46.37%` | `53.63%` | `0.86` | 112,400,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `56.14` | `56.16` | `56.14` | `56.30` | `55.98` | 412,908.70 USD | 221,871.73 USD | 191,036.96 USD | 30,834.77 USD | `+7.47%` | `7B / 4S` |
| `0:00 UTC` | `56.22` | `56.21` | `56.22` | `56.34` | `56.09` | 877,726.36 USD | 435,989.57 USD | 441,736.79 USD | -5,747.23 USD | `-0.65%` | `1B / 1S` |
| `5:00 UTC` | `56.12` | `56.15` | `56.12` | `56.22` | `56.09` | 467,194.95 USD | 242,503.27 USD | 224,691.68 USD | 17,811.60 USD | `+3.81%` | `1B / 1S` |
| `0:00 UTC` | `56.00` | `56.00` | `56.00` | `56.27` | `55.72` | 908,665.96 USD | 294,841.59 USD | 613,824.36 USD | -318,982.77 USD | `-35.10%` | `2B / 17S` |
| `5:00 UTC` | `55.91` | `55.98` | `55.91` | `56.12` | `55.78` | 818,601.42 USD | 432,159.31 USD | 386,442.11 USD | 45,717.20 USD | `+5.58%` | `3B / 5S` |
| `0:00 UTC` | `55.77` | `55.81` | `55.77` | `56.00` | `55.66` | 705,526.23 USD | 343,392.26 USD | 362,133.97 USD | -18,741.70 USD | `-2.66%` | `2B / 3S` |
| `5:00 UTC` | `55.64` | `55.76` | `55.64` | `55.98` | `55.62` | 705,697.21 USD | 170,266.34 USD | 535,430.87 USD | -365,164.53 USD | `-51.75%` | `2B / 13S` |
| `0:00 UTC` | `55.70` | `55.69` | `55.70` | `55.78` | `55.55` | 839,476.56 USD | 572,886.16 USD | 266,590.39 USD | 306,295.77 USD | `+36.49%` | `1B / 5S` |
| `5:00 UTC` | `55.59` | `55.60` | `55.59` | `55.70` | `55.52` | 436,166.22 USD | 242,135.61 USD | 194,030.61 USD | 48,104.99 USD | `+11.03%` | `3B / 4S` |
| `0:00 UTC` | `55.50` | `55.55` | `55.50` | `55.70` | `55.45` | 325,527.92 USD | 127,853.32 USD | 197,674.60 USD | -69,821.28 USD | `-21.45%` | `3B / 6S` |

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
| `5m` | -6,580.00 USD | -57,690.00 USD | **`DISTRIBUTION`** |
| `15m` | -38,170.00 USD | 77,310.00 USD | **`ACCUMULATION`** |
| `30m` | -69,900.00 USD | 458,420.00 USD | **`ACCUMULATION`** |
| `1h` | -147,850.00 USD | -162,160.00 USD | **`DISTRIBUTION`** |
| `2h` | -130,400.00 USD | -1,050,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 360,130.00 USD | -440,240.00 USD | **`DISTRIBUTION`** |
| `6h` | 488,560.00 USD | -1,640,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 558,500.00 USD | -4,150,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 819,970.00 USD | -1,800,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 831,380.00 USD | -5,130,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 4,380,000.00 USD | -24,470,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -24,290,000.00 USD | -197,500,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-6.58K` | 15m=`-38.17K` | 1h=`-147.85K` | 24h=`+831.38K`
* Futures Capital Netflows: 5m=`-57.69K` | 15m=`+77.31K` | 1h=`-162.16K` | 24h=`-5.13M`
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
  * `2026-10-30 14:37:38 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:38 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:32:38 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 14:09:38 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:52:38 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:38 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:37:38 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:37:38 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `53.76` (Risk Distance: `0.8524` pts)
  * +2.5R Take Profit: `56.74`
  * Mathematical Lot Sizing: **`11.73 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `56.21` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `57.07` (Risk Distance: `0.8524` pts)
  * +2.5R Take Profit: `54.08`
  * Mathematical Lot Sizing: **`11.73 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`55.92`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
