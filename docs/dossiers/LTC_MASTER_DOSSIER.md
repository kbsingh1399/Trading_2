# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 14:47:51 IST` (`2026-10-30 09:17:51 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Value Area High (VAH) = `56.19` (Distance: `-1.33%`)
  * Point of Control (POC) = `55.30` (Distance: `+0.24%`)
  * Value Area Low (VAL) = `54.61` (Distance: `+1.52%`)
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
| `5m` | `55.54` | `55.70` | `55.50` | `55.64` | `2,758` | 153,294.40 USD | -24,746.97 USD | `-16.14%` | -5,483,800.03 USD | `-0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `55.64` | `55.65` | `55.44` | `55.50` | `3,103` | 172,233.52 USD | -45,074.31 USD | `-26.17%` | -5,528,874.35 USD | `-0.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `55.50` | `55.51` | `55.43` | `55.50` | `1,750` | 97,087.52 USD | -3,571.03 USD | `-3.68%` | -5,532,445.37 USD | `+0.12` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `55.68` | `55.78` | `55.54` | `55.56` | `15,076` | 839,476.56 USD | 306,295.77 USD | `+36.49%` | -5,507,158.06 USD | `+2.47` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `55.57` | `55.70` | `55.51` | `55.54` | `7,845` | 436,166.22 USD | 48,104.99 USD | `+11.03%` | -5,459,053.07 USD | `+0.55` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `55.54` | `55.70` | `55.43` | `55.51` | `7,619` | 423,079.85 USD | -73,428.84 USD | `-17.36%` | -5,532,481.91 USD | `-0.38` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `56.22` | `56.34` | `55.72` | `55.97` | `54,792` | 3,072,188.69 USD | -261,201.20 USD | `-8.50%` | -5,429,107.24 USD | `+0.02` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `55.96` | `55.99` | `55.51` | `55.54` | `48,222` | 2,686,866.22 USD | -29,505.47 USD | `-1.10%` | -5,458,612.72 USD | `+0.34` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `55.54` | `55.70` | `55.43` | `55.50` | `7,611` | 422,615.44 USD | -73,392.30 USD | `-17.37%` | -5,532,005.02 USD | `+0.30` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -5,054,684.98 USD | `-0.61` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.47` | `55.72` | `55.97` | `202,255` | 11,356,305.33 USD | -519,640.59 USD | `-4.58%` | -5,574,325.57 USD | `+0.43` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `55.96` | `55.99` | `55.43` | `55.50` | `55,833` | 3,109,481.66 USD | -102,897.78 USD | `-3.31%` | -5,677,223.34 USD | `+0.64` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | 387,872.12 USD | `-1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,876,168.80 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -5,054,684.98 USD | `-0.61` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.47` | `55.72` | `55.97` | `202,255` | 11,356,305.33 USD | -519,640.59 USD | `-4.58%` | -5,574,325.57 USD | `+0.43` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `55.96` | `55.99` | `55.43` | `55.50` | `55,833` | 3,109,481.66 USD | -102,897.78 USD | `-3.31%` | -5,677,223.34 USD | `+0.64` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:43:12 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1084` | `0xeadc...9d55` | `LONG` | 2,023,155.81 USD | `36,463.77` | `52.78` | `55.50` | `0.000000` | 98,479.87 USD | `+4.87%` | `10X Cross` |
| `1098` | `0x9aa5...58af` | `SHORT` | 2,007,316.91 USD | `36,177.65` | `71.22` | `55.50` | `309.88` | 569,169.76 USD | `+28.35%` | `10X Cross` |

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
| `7D` | `47.20` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 9,650.00 USD | 2,470.00 USD | 114.09 USD |
| `7D` | `47.30` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 692.33 USD | 4,740.00 USD | 6,830.00 USD |
| `7D` | `47.40` | 8,250,000.00 USD | 0.00 USD | 8,250,000.00 USD | 0.00 USD | 1,520.00 USD | 28,550.00 USD |
| `7D` | `47.50` | 8,220,000.00 USD | 0.00 USD | 8,220,000.00 USD | 11,830.00 USD | 0.00 USD | 7,960.00 USD |
| `7D` | `48.10` | 8,200,000.00 USD | 0.00 USD | 8,200,000.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD |
| `7D` | `48.20` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 0.00 USD | 5,540.00 USD | 960.40 USD |
| `7D` | `48.40` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 0.00 USD | 6,080.00 USD | 0.00 USD |
| `7D` | `48.60` | 8,180,000.00 USD | 0.00 USD | 8,180,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `48.80` | 8,180,000.00 USD | 0.00 USD | 8,180,000.00 USD | 1,780.00 USD | 2,250.00 USD | 0.00 USD |
| `7D` | `49.30` | 8,180,000.00 USD | 0.00 USD | 8,180,000.00 USD | 15,190.00 USD | 4,490.00 USD | 14,870.00 USD |
| `7D` | `49.40` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 1,320.00 USD | 6,440.00 USD | 339.36 USD |
| `7D` | `49.50` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 2,830.00 USD | 7,770.00 USD | 0.00 USD |
| `7D` | `49.60` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 1,200.00 USD | 1,260.00 USD | 13,250.00 USD |
| `7D` | `49.70` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 12,090.00 USD | 0.00 USD | 4,900.00 USD |
| `7D` | `49.80` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 9,930.00 USD | 8,220.00 USD | 749.14 USD |
| `1D` | `49.90` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 26,820.00 USD | 15,440.00 USD | 45,510.00 USD |
| `7D` | `49.90` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 45,030.00 USD | 8,880.00 USD | 3,950.00 USD |
| `1D` | `50.00` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 13,200.00 USD | 16,830.00 USD | 40,730.00 USD |
| `7D` | `50.00` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 22,100.00 USD | 19,810.00 USD | 24,550.00 USD |
| `1D` | `50.10` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 3,780.00 USD | 4,040.00 USD | 7,600.00 USD |
| `7D` | `50.10` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 363.50 USD | 682.90 USD | 8,700.00 USD |
| `1D` | `50.20` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 177.10 USD | 709.61 USD | 5,230.00 USD |
| `7D` | `50.20` | 7,940,000.00 USD | 0.00 USD | 7,940,000.00 USD | 6,960.00 USD | 500.40 USD | 42,940.00 USD |
| `1D` | `50.30` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 171.03 USD | 3,880.00 USD | 2,500.00 USD |
| `7D` | `50.30` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 16,270.00 USD | 10,780.00 USD | 6,950.00 USD |
| `1D` | `50.40` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 8,260.00 USD | 11,890.00 USD | 1,150.00 USD |
| `7D` | `50.40` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 28,280.00 USD | 26,580.00 USD | 29,240.00 USD |
| `1D` | `50.50` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 8,910.00 USD | 8,790.00 USD | 10,530.00 USD |
| `7D` | `50.50` | 7,770,000.00 USD | 0.00 USD | 7,770,000.00 USD | 32,490.00 USD | 6,790.00 USD | 46,400.00 USD |
| `1D` | `50.60` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 7,330.00 USD | 3,440.00 USD | 10,850.00 USD |
| `7D` | `50.60` | 7,680,000.00 USD | 0.00 USD | 7,680,000.00 USD | 67,580.00 USD | 21,530.00 USD | 25,230.00 USD |
| `1D` | `50.70` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 8,170.00 USD | 2,300.00 USD | 11,770.00 USD |
| `7D` | `50.70` | 7,570,000.00 USD | 0.00 USD | 7,570,000.00 USD | 65,920.00 USD | 32,820.00 USD | 43,270.00 USD |
| `1D` | `50.80` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 12,550.00 USD | 3,100.00 USD | 8,280.00 USD |
| `7D` | `50.80` | 7,430,000.00 USD | 0.00 USD | 7,430,000.00 USD | 48,340.00 USD | 8,550.00 USD | 38,250.00 USD |
| `1D` | `50.90` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 826.24 USD | 260.05 USD | 8,390.00 USD |
| `7D` | `50.90` | 7,330,000.00 USD | 0.00 USD | 7,330,000.00 USD | 57,110.00 USD | 58,070.00 USD | 141,070.00 USD |
| `1D` | `51.00` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 5,040.00 USD | 0.00 USD | 430.77 USD |
| `7D` | `51.00` | 7,080,000.00 USD | 0.00 USD | 7,080,000.00 USD | 66,570.00 USD | 27,560.00 USD | 37,820.00 USD |
| `1D` | `51.10` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 9,210.00 USD | 6,650.00 USD | 0.00 USD |
| `7D` | `51.10` | 6,940,000.00 USD | 0.00 USD | 6,940,000.00 USD | 41,150.00 USD | 14,320.00 USD | 25,930.00 USD |
| `1D` | `51.20` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 1,770.00 USD | 1,130.00 USD | 19,220.00 USD |
| `7D` | `51.20` | 6,860,000.00 USD | 0.00 USD | 6,860,000.00 USD | 28,370.00 USD | 7,830.00 USD | 29,500.00 USD |
| `1D` | `51.30` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 8,650.00 USD | 9,710.00 USD | 0.00 USD |
| `7D` | `51.30` | 6,800,000.00 USD | 0.00 USD | 6,800,000.00 USD | 28,400.00 USD | 26,720.00 USD | 47,080.00 USD |
| `1D` | `51.40` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 3,250.00 USD | 5,610.00 USD | 416.23 USD |
| `7D` | `51.40` | 6,690,000.00 USD | 0.00 USD | 6,690,000.00 USD | 73,130.00 USD | 42,820.00 USD | 52,010.00 USD |
| `1D` | `51.50` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 5,650.00 USD | 10,010.00 USD | 41,580.00 USD |
| `7D` | `51.50` | 6,530,000.00 USD | 0.00 USD | 6,530,000.00 USD | 38,520.00 USD | 23,710.00 USD | 35,500.00 USD |
| `1D` | `51.60` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 9,060.00 USD | 18,580.00 USD | 757.87 USD |
| `7D` | `51.60` | 6,430,000.00 USD | 0.00 USD | 6,430,000.00 USD | 37,880.00 USD | 36,790.00 USD | 36,650.00 USD |
| `1D` | `51.70` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 2,510.00 USD | 12,840.00 USD | 44.86 USD |
| `7D` | `51.70` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,310.00 USD |
| `1D` | `51.80` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 13,770.00 USD | 19,520.00 USD | 14,360.00 USD |
| `7D` | `51.80` | 6,280,000.00 USD | 0.00 USD | 6,280,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,450.00 USD |
| `1D` | `51.90` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 10,140.00 USD | 19,910.00 USD | 23,480.00 USD |
| `7D` | `51.90` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 5,870.00 USD | 25,410.00 USD | 27,990.00 USD |
| `1D` | `52.00` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 20,980.00 USD | 25,620.00 USD | 24,820.00 USD |
| `7D` | `52.00` | 6,160,000.00 USD | 0.00 USD | 6,160,000.00 USD | 65,840.00 USD | 26,440.00 USD | 11,930.00 USD |
| `1D` | `52.10` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 34,970.00 USD | 17,300.00 USD | 50,500.00 USD |
| `7D` | `52.10` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 24,220.00 USD | 28,090.00 USD | 35,530.00 USD |
| `1D` | `52.20` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 15,890.00 USD | 7,630.00 USD | 49,960.00 USD |
| `7D` | `52.20` | 5,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 38,380.00 USD | 13,960.00 USD | 27,770.00 USD |
| `1D` | `52.30` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 26,510.00 USD | 22,090.00 USD | 11,210.00 USD |
| `7D` | `52.30` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 26,450.00 USD | 40,700.00 USD | 7,950.00 USD |
| `1D` | `52.40` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 13,070.00 USD | 15,400.00 USD | 7,040.00 USD |
| `7D` | `52.40` | 5,820,000.00 USD | 0.00 USD | 5,820,000.00 USD | 20,580.00 USD | 38,950.00 USD | 22,340.00 USD |
| `1D` | `52.50` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 53,990.00 USD | 30,000.00 USD | 79,400.00 USD |
| `7D` | `52.50` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 40,460.00 USD | 0.00 USD | 11,070.00 USD |
| `1D` | `52.60` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 8,330.00 USD | 43,700.00 USD | 5,450.00 USD |
| `7D` | `52.60` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 67,180.00 USD | 32,590.00 USD | 61,340.00 USD |
| `1D` | `52.70` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 18,270.00 USD | 19,780.00 USD | 40,000.00 USD |
| `7D` | `52.70` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 19,550.00 USD | 75,910.00 USD | 108,640.00 USD |
| `1D` | `52.80` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 28,000.00 USD | 50,850.00 USD | 72,920.00 USD |
| `7D` | `52.80` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 30,590.00 USD | 25,700.00 USD | 0.00 USD |
| `1D` | `52.90` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 43,760.00 USD | 50,880.00 USD | 30,100.00 USD |
| `7D` | `52.90` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 30,900.00 USD | 11,650.00 USD | 35,700.00 USD |
| `1D` | `53.00` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 26,800.00 USD | 30,500.00 USD | 39,600.00 USD |
| `7D` | `53.00` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 39,690.00 USD | 22,700.00 USD | 76,400.00 USD |
| `1D` | `53.10` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 12,590.00 USD | 46,290.00 USD | 85,170.00 USD |
| `7D` | `53.10` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 45,320.00 USD | 17,950.00 USD | 0.00 USD |
| `1D` | `53.20` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 20,660.00 USD | 9,840.00 USD | 42,170.00 USD |
| `7D` | `53.20` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 162,460.00 USD | 32,580.00 USD | 23,350.00 USD |
| `1D` | `53.30` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 8,610.00 USD | 27,570.00 USD | 5,690.00 USD |
| `7D` | `53.30` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 59,390.00 USD | 49,210.00 USD | 35,070.00 USD |
| `1D` | `53.40` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 12,600.00 USD | 10,640.00 USD | 4,540.00 USD |
| `7D` | `53.40` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 44,030.00 USD | 17,420.00 USD | 89,780.00 USD |
| `1D` | `53.50` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 9,960.00 USD | 5,700.00 USD | 22,000.00 USD |
| `7D` | `53.50` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 60,260.00 USD | 3,440.00 USD | 29,940.00 USD |
| `1D` | `53.60` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 75,950.00 USD | 3,830.00 USD | 20,970.00 USD |
| `7D` | `53.60` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 52,800.00 USD | 3,780.00 USD | 20,660.00 USD |
| `1D` | `53.70` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 6,210.00 USD | 11,100.00 USD | 11,960.00 USD |
| `7D` | `53.70` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 131,400.00 USD | 21,330.00 USD | 13,220.00 USD |
| `1D` | `53.80` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 53,640.00 USD | 28,920.00 USD | 4,830.00 USD |
| `7D` | `53.80` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 99,150.00 USD | 43,900.00 USD | 1,660.00 USD |
| `1D` | `53.90` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 51,060.00 USD | 39,560.00 USD | 27,830.00 USD |
| `7D` | `53.90` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 160,820.00 USD | 22,780.00 USD | 8,330.00 USD |
| `1D` | `54.00` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 76,010.00 USD | 21,440.00 USD | 86,580.00 USD |
| `7D` | `54.00` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 380,340.00 USD | 71,820.00 USD | 307,130.00 USD |
| `1D` | `54.10` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 94,870.00 USD | 19,160.00 USD | 49,170.00 USD |
| `7D` | `54.10` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 302,190.00 USD | 0.00 USD | 54,840.00 USD |
| `1D` | `54.20` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 72,600.00 USD | 22,000.00 USD | 40,120.00 USD |
| `7D` | `54.20` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 205,060.00 USD | 0.00 USD | 3,750.00 USD |
| `1D` | `54.30` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 15,600.00 USD | 6,650.00 USD | 5,590.00 USD |
| `7D` | `54.30` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 381,380.00 USD | 8,520.00 USD | 181,420.00 USD |
| `1D` | `54.40` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 63,410.00 USD | 90,630.00 USD | 3,290.00 USD |
| `7D` | `54.40` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 304,270.00 USD | 63,170.00 USD | 94,630.00 USD |
| `1D` | `54.50` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 25,050.00 USD | 64,250.00 USD | 9,090.00 USD |
| `7D` | `54.50` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 159,720.00 USD | 35,580.00 USD | 237,000.00 USD |
| `1D` | `54.60` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 913.17 USD | 25,490.00 USD | 43,580.00 USD |
| `7D` | `54.60` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 18,530.00 USD | 1,930.00 USD | 137,080.00 USD |
| `1D` | `54.70` | 952,760.00 USD | 0.00 USD | 952,760.00 USD | 6,600.00 USD | 23,060.00 USD | 105,800.00 USD |
| `7D` | `54.70` | 846,520.00 USD | 0.00 USD | 846,520.00 USD | 0.00 USD | 3,600.00 USD | 41,310.00 USD |
| `1D` | `54.80` | 817,300.00 USD | 0.00 USD | 817,300.00 USD | 0.00 USD | 48,420.00 USD | 23,920.00 USD |
| `7D` | `54.80` | 801,610.00 USD | 0.00 USD | 801,610.00 USD | 0.00 USD | 35,700.00 USD | 26,440.00 USD |
| `1D` | `54.90` | 744,960.00 USD | 0.00 USD | 744,960.00 USD | 66,900.00 USD | 65,440.00 USD | 10,850.00 USD |
| `7D` | `54.90` | 739,470.00 USD | 0.00 USD | 739,470.00 USD | 0.00 USD | 112,280.00 USD | 51,000.00 USD |
| `1D` | `55.00` | 601,770.00 USD | 0.00 USD | 601,770.00 USD | 40,710.00 USD | 54,150.00 USD | 55,190.00 USD |
| `7D` | `55.00` | 576,190.00 USD | 0.00 USD | 576,190.00 USD | 97,700.00 USD | 2,830.00 USD | 16,650.00 USD |
| `1D` | `55.10` | 451,720.00 USD | 0.00 USD | 451,720.00 USD | 50,530.00 USD | 62,170.00 USD | 80,200.00 USD |
| `7D` | `55.10` | 459,010.00 USD | 0.00 USD | 459,010.00 USD | 54,590.00 USD | 18,510.00 USD | 64,690.00 USD |
| `1D` | `55.20` | 258,820.00 USD | 0.00 USD | 258,820.00 USD | 39,390.00 USD | 11,830.00 USD | 66,410.00 USD |
| `7D` | `55.20` | 321,230.00 USD | 0.00 USD | 321,230.00 USD | 57,400.00 USD | 59,710.00 USD | 150,160.00 USD |
| `1D` | `55.30` | 141,200.00 USD | 0.00 USD | 141,200.00 USD | 52,860.00 USD | 22,650.00 USD | 59,180.00 USD |
| `7D` | `55.30` | 53,950.00 USD | 0.00 USD | 53,950.00 USD | 23,140.00 USD | 11,270.00 USD | 0.00 USD |
| `1D` | `55.40` | 6,510.00 USD | 0.00 USD | 6,510.00 USD | 0.00 USD | 6,510.00 USD | 0.00 USD |
| `7D` | `55.40` | 19,540.00 USD | 0.00 USD | 19,540.00 USD | 0.00 USD | 18,550.00 USD | 990.00 USD |
| `1D` | `55.50` | 5,500.00 USD | 5,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD |
| `1D` | `55.50` | 11,000.00 USD | 11,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD |
| `7D` | `55.50` | 114,340.00 USD | 114,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 114,340.00 USD |
| `7D` | `55.50` | 228,670.00 USD | 228,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 114,340.00 USD |
| `7D` | `55.60` | 294,570.00 USD | 294,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65,900.00 USD |
| `1D` | `55.70` | 19,310.00 USD | 19,310.00 USD | 0.00 USD | 0.00 USD | 7,700.00 USD | 613.46 USD |
| `7D` | `55.70` | 500,990.00 USD | 500,990.00 USD | 0.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD |
| `1D` | `55.80` | 22,490.00 USD | 22,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,170.00 USD |
| `7D` | `55.80` | 590,760.00 USD | 590,760.00 USD | 0.00 USD | 60,840.00 USD | 28,930.00 USD | 0.00 USD |
| `1D` | `55.90` | 75,550.00 USD | 75,550.00 USD | 0.00 USD | 51,520.00 USD | 0.00 USD | 1,550.00 USD |
| `7D` | `55.90` | 732,080.00 USD | 732,080.00 USD | 0.00 USD | 141,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `56.00` | 79,930.00 USD | 79,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,380.00 USD |
| `7D` | `56.00` | 903,200.00 USD | 903,200.00 USD | 0.00 USD | 2,590.00 USD | 0.00 USD | 168,520.00 USD |
| `7D` | `56.20` | 983,140.00 USD | 983,140.00 USD | 0.00 USD | 0.00 USD | 79,940.00 USD | 0.00 USD |
| `1D` | `56.30` | 83,880.00 USD | 83,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,950.00 USD |
| `7D` | `56.30` | 985,570.00 USD | 985,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,430.00 USD |
| `1D` | `56.40` | 114,700.00 USD | 114,700.00 USD | 0.00 USD | 5,040.00 USD | 23,310.00 USD | 2,470.00 USD |
| `7D` | `56.40` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 2,650.00 USD | 11,040.00 USD | 3,750.00 USD |
| `1D` | `56.50` | 506,910.00 USD | 506,910.00 USD | 0.00 USD | 138,540.00 USD | 108,630.00 USD | 145,040.00 USD |
| `7D` | `56.50` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 170,750.00 USD | 151,940.00 USD | 0.00 USD |
| `1D` | `56.60` | 808,760.00 USD | 808,760.00 USD | 0.00 USD | 61,400.00 USD | 159,370.00 USD | 81,070.00 USD |
| `7D` | `56.60` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 363,190.00 USD | 185,910.00 USD | 4,520.00 USD |
| `1D` | `56.70` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 114,230.00 USD | 45,300.00 USD | 315,590.00 USD |
| `7D` | `56.70` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 117,290.00 USD | 141,830.00 USD | 99,270.00 USD |
| `1D` | `56.80` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 117,760.00 USD | 20,790.00 USD | 106,140.00 USD |
| `7D` | `56.80` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 172,110.00 USD | 92,780.00 USD | 324,570.00 USD |
| `1D` | `56.90` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 45,140.00 USD | 17,930.00 USD | 35,720.00 USD |
| `7D` | `56.90` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 113,780.00 USD | 52,200.00 USD | 310,820.00 USD |
| `1D` | `57.00` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 6,480.00 USD | 43,030.00 USD | 29,740.00 USD |
| `7D` | `57.00` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 88,680.00 USD | 56,390.00 USD | 176,670.00 USD |
| `1D` | `57.10` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 77,000.00 USD | 77,400.00 USD | 46,610.00 USD |
| `7D` | `57.10` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 36,580.00 USD | 79,290.00 USD | 22,810.00 USD |
| `1D` | `57.20` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 53,080.00 USD | 78,490.00 USD | 120,900.00 USD |
| `7D` | `57.20` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 118,850.00 USD | 23,920.00 USD | 17,750.00 USD |
| `1D` | `57.30` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 70,930.00 USD | 44,630.00 USD | 87,180.00 USD |
| `7D` | `57.30` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 76,940.00 USD | 28,570.00 USD | 97,810.00 USD |
| `1D` | `57.40` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 84,960.00 USD | 49,470.00 USD | 78,400.00 USD |
| `7D` | `57.40` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 124,180.00 USD | 72,180.00 USD | 192,480.00 USD |
| `1D` | `57.50` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 197,830.00 USD | 51,590.00 USD | 174,740.00 USD |
| `7D` | `57.50` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 99,810.00 USD | 31,830.00 USD | 1,870.00 USD |
| `1D` | `57.60` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 69,720.00 USD | 27,370.00 USD | 62,630.00 USD |
| `7D` | `57.60` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 149,560.00 USD | 44,690.00 USD | 27,950.00 USD |
| `1D` | `57.70` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 42,540.00 USD | 53,630.00 USD | 96,430.00 USD |
| `7D` | `57.70` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 30,070.00 USD | 57,580.00 USD |
| `1D` | `57.80` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 18,150.00 USD | 22,650.00 USD | 77,220.00 USD |
| `7D` | `57.80` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 9,650.00 USD | 24,520.00 USD | 48,030.00 USD |
| `1D` | `57.90` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 13,000.00 USD | 15,870.00 USD | 28,950.00 USD |
| `7D` | `57.90` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 14,390.00 USD | 963.90 USD | 29,940.00 USD |
| `1D` | `58.00` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 7,880.00 USD | 9,480.00 USD | 15,330.00 USD |
| `7D` | `58.00` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD | 107,350.00 USD |
| `1D` | `58.10` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 31,400.00 USD | 17,830.00 USD | 21,300.00 USD |
| `7D` | `58.10` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 5,470.00 USD | 19,160.00 USD | 13,220.00 USD |
| `1D` | `58.20` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 35,920.00 USD | 34,800.00 USD | 4,940.00 USD |
| `7D` | `58.20` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 31,590.00 USD | 1,660.00 USD |
| `1D` | `58.30` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 33,360.00 USD | 38,620.00 USD | 64,380.00 USD |
| `7D` | `58.30` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 48,850.00 USD | 11,000.00 USD | 35,150.00 USD |
| `1D` | `58.40` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 26,490.00 USD | 18,940.00 USD | 50,160.00 USD |
| `7D` | `58.40` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 27,290.00 USD | 9,260.00 USD | 85,100.00 USD |
| `1D` | `58.50` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 16,410.00 USD | 1,750.00 USD | 124.02 USD |
| `7D` | `58.50` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 2,060.00 USD | 24,530.00 USD | 0.00 USD |
| `1D` | `58.60` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 21,940.00 USD | 5,920.00 USD | 40,890.00 USD |
| `7D` | `58.60` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 30,680.00 USD | 20,260.00 USD | 51,650.00 USD |
| `1D` | `58.70` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 44,920.00 USD | 10,120.00 USD | 29,940.00 USD |
| `7D` | `58.70` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 15,810.00 USD | 11,600.00 USD | 31,210.00 USD |
| `1D` | `58.80` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 36,630.00 USD | 9,890.00 USD | 23,340.00 USD |
| `7D` | `58.80` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 3,840.00 USD | 3,320.00 USD | 54,600.00 USD |
| `1D` | `58.90` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 22,130.00 USD | 60,970.00 USD | 90,490.00 USD |
| `7D` | `58.90` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 2,140.00 USD | 54,240.00 USD | 141,400.00 USD |
| `1D` | `59.00` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 129,990.00 USD | 58,870.00 USD | 129,440.00 USD |
| `7D` | `59.00` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 259,280.00 USD | 65,270.00 USD | 149,290.00 USD |
| `1D` | `59.10` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 92,240.00 USD | 39,740.00 USD | 163,590.00 USD |
| `7D` | `59.10` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 93,390.00 USD | 45,400.00 USD | 158,260.00 USD |
| `1D` | `59.20` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 102,940.00 USD | 59,320.00 USD | 49,210.00 USD |
| `7D` | `59.20` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 153,580.00 USD | 18,540.00 USD | 177,190.00 USD |
| `1D` | `59.30` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 146,220.00 USD | 30,070.00 USD | 66,050.00 USD |
| `7D` | `59.30` | 7,300,000.00 USD | 7,300,000.00 USD | 0.00 USD | 88,710.00 USD | 67,460.00 USD | 91,480.00 USD |
| `1D` | `59.40` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 35,110.00 USD | 30,780.00 USD | 49,030.00 USD |
| `7D` | `59.40` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 107,040.00 USD | 73,620.00 USD | 124,650.00 USD |
| `1D` | `59.50` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 81,240.00 USD | 34,430.00 USD | 32,400.00 USD |
| `7D` | `59.50` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 67,060.00 USD | 61,370.00 USD | 13,410.00 USD |
| `1D` | `59.60` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 43,950.00 USD | 51,200.00 USD | 5,300.00 USD |
| `7D` | `59.60` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 236,760.00 USD | 129,330.00 USD | 84,540.00 USD |
| `1D` | `59.70` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 7,970.00 USD | 15,970.00 USD | 62,040.00 USD |
| `7D` | `59.70` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 55,510.00 USD | 99,970.00 USD | 161,990.00 USD |
| `1D` | `59.80` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 32,130.00 USD | 26,470.00 USD | 2,350.00 USD |
| `7D` | `59.80` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 118,240.00 USD | 91,980.00 USD | 155,300.00 USD |
| `1D` | `59.90` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 102,020.00 USD | 17,810.00 USD | 50,060.00 USD |
| `7D` | `59.90` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 142,290.00 USD | 34,490.00 USD | 28,910.00 USD |
| `1D` | `60.00` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 162,970.00 USD | 29,090.00 USD | 50,570.00 USD |
| `7D` | `60.00` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 100,570.00 USD | 67,520.00 USD | 83,690.00 USD |
| `1D` | `60.10` | 6,490,000.00 USD | 6,490,000.00 USD | 0.00 USD | 64,550.00 USD | 28,140.00 USD | 57,080.00 USD |
| `7D` | `60.10` | 9,720,000.00 USD | 9,720,000.00 USD | 0.00 USD | 200,540.00 USD | 84,980.00 USD | 95,270.00 USD |
| `1D` | `60.20` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 59,560.00 USD | 19,740.00 USD | 82,270.00 USD |
| `7D` | `60.20` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 162,230.00 USD | 99,360.00 USD | 109,110.00 USD |
| `1D` | `60.30` | 6,770,000.00 USD | 6,770,000.00 USD | 0.00 USD | 52,350.00 USD | 31,630.00 USD | 26,470.00 USD |
| `7D` | `60.30` | 10,500,000.00 USD | 10,500,000.00 USD | 0.00 USD | 133,350.00 USD | 100,380.00 USD | 171,800.00 USD |
| `1D` | `60.40` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 66,740.00 USD | 13,730.00 USD | 42,520.00 USD |
| `7D` | `60.40` | 10,870,000.00 USD | 10,870,000.00 USD | 0.00 USD | 64,850.00 USD | 100,560.00 USD | 201,060.00 USD |
| `1D` | `60.50` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 22,700.00 USD | 19,320.00 USD | 36,200.00 USD |
| `7D` | `60.50` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 115,390.00 USD | 80,510.00 USD | 170,290.00 USD |
| `1D` | `60.60` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 40,710.00 USD | 19,140.00 USD | 3,930.00 USD |
| `7D` | `60.60` | 11,620,000.00 USD | 11,620,000.00 USD | 0.00 USD | 251,100.00 USD | 16,970.00 USD | 122,080.00 USD |
| `1D` | `60.70` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 31,880.00 USD | 22,330.00 USD | 3,120.00 USD |
| `7D` | `60.70` | 11,790,000.00 USD | 11,790,000.00 USD | 0.00 USD | 102,230.00 USD | 48,240.00 USD | 20,440.00 USD |
| `1D` | `60.80` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 11,060.00 USD | 12,980.00 USD | 47,810.00 USD |
| `7D` | `60.80` | 11,940,000.00 USD | 11,940,000.00 USD | 0.00 USD | 46,960.00 USD | 28,960.00 USD | 74,950.00 USD |
| `1D` | `60.90` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 34,200.00 USD | 23,250.00 USD | 22,900.00 USD |
| `7D` | `60.90` | 12,150,000.00 USD | 12,150,000.00 USD | 0.00 USD | 105,970.00 USD | 33,290.00 USD | 64,610.00 USD |
| `1D` | `61.00` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 43,930.00 USD | 6,430.00 USD | 18,420.00 USD |
| `7D` | `61.00` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 43,120.00 USD | 11,530.00 USD | 0.00 USD |
| `1D` | `61.10` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 13,810.00 USD | 14,950.00 USD | 11,520.00 USD |
| `7D` | `61.10` | 12,240,000.00 USD | 12,240,000.00 USD | 0.00 USD | 31,540.00 USD | 10,430.00 USD | 0.00 USD |
| `1D` | `61.20` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 75,070.00 USD | 1,880.00 USD | 39,080.00 USD |
| `7D` | `61.20` | 12,360,000.00 USD | 12,360,000.00 USD | 0.00 USD | 51,210.00 USD | 20,920.00 USD | 47,450.00 USD |
| `1D` | `61.30` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 4,040.00 USD | 7,600.00 USD |
| `7D` | `61.30` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 16,510.00 USD | 13,210.00 USD | 24,600.00 USD |
| `1D` | `61.40` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 1,190.00 USD | 709.61 USD | 5,230.00 USD |
| `7D` | `61.40` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 62,340.00 USD | 25,720.00 USD | 43,510.00 USD |
| `1D` | `61.50` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 1,060.00 USD | 3,880.00 USD | 2,500.00 USD |
| `7D` | `61.50` | 12,650,000.00 USD | 12,650,000.00 USD | 0.00 USD | 17,710.00 USD | 42,440.00 USD | 41,110.00 USD |
| `1D` | `61.60` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 9,250.00 USD | 11,890.00 USD | 1,150.00 USD |
| `7D` | `61.60` | 12,860,000.00 USD | 12,860,000.00 USD | 0.00 USD | 32,920.00 USD | 58,350.00 USD | 116,740.00 USD |
| `1D` | `61.70` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 13,890.00 USD | 8,790.00 USD | 10,530.00 USD |
| `7D` | `61.70` | 13,050,000.00 USD | 13,050,000.00 USD | 0.00 USD | 82,860.00 USD | 10,880.00 USD | 102,270.00 USD |
| `1D` | `61.80` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 9,150.00 USD | 3,440.00 USD | 10,850.00 USD |
| `7D` | `61.80` | 13,320,000.00 USD | 13,320,000.00 USD | 0.00 USD | 169,680.00 USD | 25,670.00 USD | 65,810.00 USD |
| `1D` | `61.90` | 7,590,000.00 USD | 7,590,000.00 USD | 0.00 USD | 5,210.00 USD | 1,580.00 USD | 11,700.00 USD |
| `7D` | `61.90` | 13,470,000.00 USD | 13,470,000.00 USD | 0.00 USD | 73,690.00 USD | 32,820.00 USD | 43,270.00 USD |
| `1D` | `62.00` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 12,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.00` | 13,560,000.00 USD | 13,560,000.00 USD | 0.00 USD | 50,080.00 USD | 8,550.00 USD | 38,250.00 USD |
| `7D` | `62.10` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.20` | 13,710,000.00 USD | 13,710,000.00 USD | 0.00 USD | 39,180.00 USD | 34,620.00 USD | 61,090.00 USD |
| `7D` | `62.30` | 13,840,000.00 USD | 13,840,000.00 USD | 0.00 USD | 27,500.00 USD | 23,450.00 USD | 79,980.00 USD |
| `7D` | `62.40` | 13,970,000.00 USD | 13,970,000.00 USD | 0.00 USD | 74,860.00 USD | 27,560.00 USD | 25,440.00 USD |
| `7D` | `62.50` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 36,690.00 USD | 12,720.00 USD | 25,700.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `409.38M` | Total OI Tokens: `7,380,764.1 LTC`
  * 1h OI Change: `-0.67%` | 4h OI Change: `-2.32%` | 24h OI Change: `-9.20%`
  * Exchange Breakdown: Binance=`72.60M` | Bybit=`66.50M` | OKX=`34.21M` | Hyperliquid=`22.17M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `12.14K` | Last 24h: `29.34K` | Last 3d: `56.60K` | Last 7d: `113.64K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0006%` |
| **USDT Bybit** | `0.0087%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0026%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `49.70%` | `50.30%` | `0.99` | 2,820,000.00 USD |
| `15M` | `Binance` | `50.04%` | `49.96%` | `1.00` | 640,970.00 USD |
| `15M` | `OKX` | `47.36%` | `52.64%` | `0.90` | 294,170.00 USD |
| `15M` | `Bybit` | `51.67%` | `48.33%` | `1.07` | 238,000.00 USD |
| `15M` | `KuCoin` | `53.52%` | `46.48%` | `1.15` | 12,520.00 USD |
| `15M` | `Gate` | `60.14%` | `39.86%` | `1.51` | 252,080.00 USD |
| `15M` | `Bitget` | `45.93%` | `54.07%` | `0.85` | 34,120.00 USD |
| `15M` | `BingX` | `28.38%` | `71.62%` | `0.40` | 708,770.00 USD |
| `15M` | `MEXC` | `3.59%` | `96.41%` | `0.04` | 136,280.00 USD |
| `15M` | `Bitunix` | `58.07%` | `41.93%` | `1.38` | 80,690.00 USD |
| `15M` | `Hyperliquid` | `58.72%` | `41.28%` | `1.42` | 6,170.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.02%` | `51.98%` | `0.92` | 31,050.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `98.77%` | `1.23%` | `80.30` | 372,520.00 USD |
| `15M` | `HTX` | `34.86%` | `65.14%` | `0.54` | 7,410.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `63.54%` | `36.46%` | `1.74` | 694.38 USD |
| `15M` | `Aster` | `94.45%` | `5.55%` | `17.02` | 1,650.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `11.38%` | `88.62%` | `0.13` | 2,530.00 USD |
| `15M` | `Whale Positions` | `50.04%` | `49.96%` | `1.00` | 640,970.00 USD |
| `15M` | `Global Accounts` | `49.70%` | `50.30%` | `0.99` | 2,820,000.00 USD |
| `1H` | `LTC` | `51.94%` | `48.06%` | `1.08` | 10,920,000.00 USD |
| `1H` | `Binance` | `53.15%` | `46.85%` | `1.13` | 3,010,000.00 USD |
| `1H` | `OKX` | `39.3%` | `60.7%` | `0.65` | 1,090,000.00 USD |
| `1H` | `Bybit` | `55.99%` | `44.01%` | `1.27` | 809,330.00 USD |
| `1H` | `KuCoin` | `48.98%` | `51.02%` | `0.96` | 41,160.00 USD |
| `1H` | `Gate` | `52.02%` | `47.98%` | `1.08` | 916,070.00 USD |
| `1H` | `Bitget` | `30.28%` | `69.72%` | `0.43` | 287,230.00 USD |
| `1H` | `BingX` | `35.16%` | `64.84%` | `0.54` | 2,420,000.00 USD |
| `1H` | `MEXC` | `27.59%` | `72.41%` | `0.38` | 272,990.00 USD |
| `1H` | `Bitunix` | `57.72%` | `42.28%` | `1.37` | 187,070.00 USD |
| `1H` | `Hyperliquid` | `52.44%` | `47.56%` | `1.10` | 52,350.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.75%` | `48.25%` | `1.07` | 288,820.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `91.36%` | `8.64%` | `10.57` | 1,510,000.00 USD |
| `1H` | `HTX` | `59.12%` | `40.88%` | `1.45` | 13,410.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `35.9%` | `64.1%` | `0.56` | 16,570.00 USD |
| `1H` | `Aster` | `62.84%` | `37.16%` | `1.69` | 7,290.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `7.96%` | `92.04%` | `0.09` | 4,070.00 USD |
| `1H` | `Whale Positions` | `53.15%` | `46.85%` | `1.13` | 3,010,000.00 USD |
| `1H` | `Global Accounts` | `51.94%` | `48.06%` | `1.08` | 10,920,000.00 USD |
| `4H` | `LTC` | `49.16%` | `50.84%` | `0.97` | 42,330,000.00 USD |
| `4H` | `Binance` | `49.97%` | `50.03%` | `1.00` | 12,470,000.00 USD |
| `4H` | `OKX` | `40.09%` | `59.91%` | `0.67` | 4,880,000.00 USD |
| `4H` | `Bybit` | `54.59%` | `45.41%` | `1.20` | 3,890,000.00 USD |
| `4H` | `KuCoin` | `50.22%` | `49.78%` | `1.01` | 348,910.00 USD |
| `4H` | `Gate` | `49.48%` | `50.52%` | `0.98` | 4,250,000.00 USD |
| `4H` | `Bitget` | `48.13%` | `51.87%` | `0.93` | 1,410,000.00 USD |
| `4H` | `BingX` | `39.44%` | `60.56%` | `0.65` | 8,930,000.00 USD |
| `4H` | `MEXC` | `46.55%` | `53.45%` | `0.87` | 1,070,000.00 USD |
| `4H` | `Bitunix` | `41.73%` | `58.27%` | `0.72` | 908,570.00 USD |
| `4H` | `Hyperliquid` | `51.21%` | `48.79%` | `1.05` | 376,670.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.78%` | `50.22%` | `0.99` | 1,130,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `91.26%` | `8.74%` | `10.44` | 2,550,000.00 USD |
| `4H` | `HTX` | `51.12%` | `48.88%` | `1.05` | 52,810.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `41.56%` | `58.44%` | `0.71` | 19,350.00 USD |
| `4H` | `Aster` | `43.83%` | `56.17%` | `0.78` | 18,340.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `60.44%` | `39.56%` | `1.53` | 17,340.00 USD |
| `4H` | `Whale Positions` | `49.97%` | `50.03%` | `1.00` | 12,470,000.00 USD |
| `4H` | `Global Accounts` | `49.16%` | `50.84%` | `0.97` | 42,330,000.00 USD |


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
| `5m` | -32,000.00 USD | -51,470.00 USD | **`DISTRIBUTION`** |
| `15m` | -87,770.00 USD | -89,530.00 USD | **`DISTRIBUTION`** |
| `30m` | -119,360.00 USD | 13,730.00 USD | **`DISTRIBUTION`** |
| `1h` | -170,360.00 USD | -12,520.00 USD | **`DISTRIBUTION`** |
| `2h` | -161,110.00 USD | -882,070.00 USD | **`DISTRIBUTION`** |
| `4h` | 183,440.00 USD | -627,760.00 USD | **`DISTRIBUTION`** |
| `6h` | 350,030.00 USD | -1,530,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 467,730.00 USD | -3,800,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 576,750.00 USD | -2,920,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 747,180.00 USD | -5,290,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 4,270,000.00 USD | -24,470,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -24,460,000.00 USD | -197,500,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-32.00K` | 15m=`-87.77K` | 1h=`-170.36K` | 24h=`+747.18K`
* Futures Capital Netflows: 5m=`-51.47K` | 15m=`-89.53K` | 1h=`-12.52K` | 24h=`-5.29M`
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
  * Execution Entry: `56.19` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `57.04` (Risk Distance: `0.8524` pts)
  * +2.5R Take Profit: `54.06`
  * Mathematical Lot Sizing: **`11.73 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`55.87`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
