# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 16:33:46 IST` (`2026-10-30 11:03:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `55.60` | **Live Ask Quote**: `55.91` | **Mid Price**: `55.75`
- **Spread Points**: `300.00` | **Spread BPS**: `53.81 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `55.75` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `56.15` | Lower -3.00σ Band: `55.36`
  * Upper +2.51σ Band: `56.06` | Lower -2.51σ Band: `55.45`
  * Upper +2.01σ Band: `55.99` | Lower -2.01σ Band: `55.52`
  * Upper +2.00σ Band: `55.98` | Lower -2.00σ Band: `55.53`
  * Upper +1.28σ Band: `55.91` | Lower -1.28σ Band: `55.60`
  * Upper +1.00σ Band: `55.87` | Lower -1.00σ Band: `55.64`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`55.75` | EMA-20=`55.75` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`55.75` (Slope: `+0.0000`) | EMA-100=`55.75`
  * Institutional Anchors: EMA-144=`55.75` | EMA-200=`55.75` (Slope: `+0.0000`) | EMA-233=`55.75`
- **Range Boundaries**: 24H High=`56.31` | 24H Low=`55.20` | Weekly High=`56.87` | Weekly Low=`54.64`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `56.07` (Distance: `-0.58%`)
  * Point of Control (POC) = `55.30` (Distance: `+0.80%`)
  * Value Area Low (VAL) = `54.61` (Distance: `+2.08%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.40` | POC=`57.72` | VAL=`56.83`
  * Prior Day Extremes: PDH=`59.52` | PDL=`54.18` | PDC=`54.46`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`58.39` | Weekly POC=`56.43` | Weekly VAL=`55.83`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`56.03` | Low=`52.64`
  * London Session (08:00-16:00 UTC): High=`56.23` | Low=`54.91`
  * New York Session (13:00-21:00 UTC): High=`55.68` | Low=`54.91`
  * Initial Balance (First Hour): IB High=`56.22` | IB Low=`55.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `55.53` - `55.98`
  * Optimal Trade Entry (OTE 0.705): `55.87`
  * Structural Invalidation Anchor (0.786): `56.20`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `55.63` | `55.76` | `55.62` | `55.69` | `4,293` | 239,048.98 USD | 102,745.15 USD | `+42.98%` | -6,252,780.24 USD | `+1.18` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `55.70` | `55.73` | `55.41` | `55.49` | `17,560` | 974,843.65 USD | -676,481.31 USD | `-69.39%` | -6,929,261.55 USD | `-3.39` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `55.48` | `55.55` | `55.45` | `55.55` | `1,223` | 67,849.02 USD | 14,441.56 USD | `+21.28%` | -6,914,819.99 USD | `+0.42` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `55.50` | `55.76` | `55.46` | `55.69` | `12,473` | 693,956.44 USD | 210,975.35 USD | `+30.40%` | -6,140,870.98 USD | `+1.42` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `55.70` | `55.79` | `55.41` | `55.79` | `22,951` | 1,274,778.93 USD | -604,952.03 USD | `-47.46%` | -6,745,823.00 USD | `-2.47` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `55.79` | `55.88` | `55.75` | `55.79` | `3,524` | 196,677.52 USD | 75,184.50 USD | `+38.23%` | -6,670,638.50 USD | `+0.67` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `55.54` | `55.70` | `55.26` | `55.41` | `38,786` | 2,150,474.73 USD | -475,444.38 USD | `-22.11%` | -6,079,275.42 USD | `-0.18` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `55.41` | `55.79` | `55.11` | `55.79` | `78,766` | 4,368,598.06 USD | -793,797.55 USD | `-18.17%` | -6,873,072.97 USD | `-0.53` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `55.79` | `55.88` | `55.75` | `55.82` | `3,404` | 189,987.88 USD | 81,746.65 USD | `+43.03%` | -6,791,326.32 USD | `+0.54` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -5,054,684.98 USD | `-0.61` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.47` | `55.72` | `55.97` | `202,255` | 11,356,305.33 USD | -519,640.59 USD | `-4.58%` | -5,574,325.57 USD | `+0.43` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `55.96` | `55.99` | `55.11` | `55.54` | `161,575` | 8,972,166.19 USD | -1,357,521.68 USD | `-15.13%` | -6,931,847.25 USD | `-0.16` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | 387,872.12 USD | `-1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,876,168.80 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -5,054,684.98 USD | `-0.61` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.47` | `55.72` | `55.97` | `202,255` | 11,356,305.33 USD | -519,640.59 USD | `-4.58%` | -5,574,325.57 USD | `+0.43` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `55.96` | `55.99` | `55.11` | `55.82` | `169,179` | 9,395,926.88 USD | -1,217,000.75 USD | `-12.95%` | -6,791,326.32 USD | `-0.07` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`55.75`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:32:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1066` | `0xeadc...9d55` | `LONG` | 2,030,922.60 USD | `36,463.77` | `52.78` | `55.70` | `0.000000` | 106,246.65 USD | `+5.23%` | `10X Cross` |
| `1078` | `0x9aa5...58af` | `SHORT` | 2,015,022.75 USD | `36,177.65` | `71.22` | `55.70` | `299.63` | 561,463.92 USD | `+27.86%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `57.87` | 5,812.29 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.81K USD at 57.8740 USD [API] | `2026-10-29 13:57:22` |
| `ANNOUNCEMENT` | `INFO` | `57.58` | 5,362.91 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.36K USD at 57.5790 USD [API] | `2026-10-29 18:28:11` |
| `ANNOUNCEMENT` | `INFO` | `57.58` | 7,508.12 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 7.51K USD at 57.5820 USD [API] | `2026-10-29 18:28:11` |
| `ANNOUNCEMENT` | `INFO` | `57.48` | 7,508.30 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 7.51K USD at 57.4820 USD [API] | `2026-10-29 18:31:51` |
| `ANNOUNCEMENT` | `INFO` | `58.07` | 7,508.58 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 58.0710 USD [API] | `2026-10-29 19:33:24` |
| `ANNOUNCEMENT` | `INFO` | `56.72` | 6,072.76 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 6.07K USD at 56.7230 USD [API] | `2026-10-29 20:33:49` |
| `ANNOUNCEMENT` | `INFO` | `56.72` | 7,508.42 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 7.51K USD at 56.7230 USD [API] | `2026-10-29 20:33:49` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`56.49` (Vol: 204,200.00 USD, Dist: `+1.88%`) | Long MP=`54.13` (Vol: 153,300.00 USD, Dist: `--2.37%`)
  * 48H Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.40%`) | Long MP=`54.12` (Vol: 153,300.00 USD, Dist: `--2.41%`)
  * 3D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.40%`) | Long MP=`54.12` (Vol: 153,300.00 USD, Dist: `--2.41%`)
  * 7D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.40%`) | Long MP=`54.12` (Vol: 153,300.00 USD, Dist: `--2.41%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `11.35` | 136.20 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.25` | 122.50 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.75` | 2,560.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.15` | 2,220.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.65` | 150.15 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `17.85` | 16,600.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.15` | 2,730.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.35` | 165.52 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.55` | 2,230.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.05` | 3,470.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.45` | 2,010.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.65` | 136.29 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.85` | 4,260.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.05` | 1,320.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.45` | 362.12 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.05` | 978.01 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.35` | 519.30 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.85` | 195.57 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.05` | 380.47 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.65` | 447.40 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.15` | 696.91 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 277,980.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 115,940.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 50,740.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.65` | 530.70 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 8,020.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.05` | 5,510.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 272.75 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.75` | 1,080.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 173.85 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.05` | 171.69 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 583.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 297,500.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 218.46 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 152.75 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.65` | 1,540.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 538.53 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 27,620.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 1,290.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.65` | 4,640.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 2,870.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 125.24 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 450.10 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.25` | 225.75 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.35` | 172.10 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.45` | 9,730.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 653.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 953.68 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.95` | 35,770.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.05` | 4,100.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.25` | 255.03 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.55` | 5,850.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 257.76 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.75` | 1,690.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 182.85 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 126.70 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.45` | 65,890.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 3,240.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 4,670.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 166.49 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.15` | 439.02 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.05` | 429.72 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 3,020.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 423.18 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.65` | 109.58 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 3,110.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 290.10 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 438.74 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.25` | 1,050.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 9,260.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 3,530.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.65` | 978.90 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 377.50 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 6,210.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 446.67 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.25` | 695.38 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 847.54 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 2,400.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 993.82 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 4,280.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 3,700.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 664,760.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 570.02 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 264.83 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 716.41 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 655.34 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 5,900.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 1,180.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 133.10 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 2,160.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 1,010.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 133.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 274.39 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 6,340.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 509.01 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 396.54 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.15` | 5,430.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 14,850.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 644.96 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.85` | 9,210.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.95` | 1,050.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 201.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 66,300.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 35,410.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.45` | 302.67 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.55` | 339.97 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 1,910.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.75` | 3,800.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 5,800.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 2,000.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 9,080.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 1,580.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 121,210.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 5,700.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 1,040.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 426.02 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 21,880.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 801.14 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.05` | 3,500.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 2,380.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 84,440.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.45` | 5,720.00 USD | 951,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 842.44 USD | 945,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 4,230.00 USD | 944,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 134.55 USD | 940,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 3,960.00 USD | 940,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 4,830.00 USD | 936,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 8,710.00 USD | 931,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 3,180.00 USD | 923,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 3,540.00 USD | 919,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 23,940.00 USD | 916,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 12,060.00 USD | 892,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 42,180.00 USD | 880,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 76,920.00 USD | 838,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 706.41 USD | 761,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.35` | 561.76 USD | 760,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 24,930.00 USD | 760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 3,980.00 USD | 735,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 358.40 USD | 731,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 158.22 USD | 730,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.05` | 2,140.00 USD | 730,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 1,980.00 USD | 728,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 9,030.00 USD | 726,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.35` | 43,920.00 USD | 717,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.45` | 2,590.00 USD | 673,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 4,450.00 USD | 670,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 47,750.00 USD | 666,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 381.04 USD | 618,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.10` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.15` | 1,690.00 USD | 618,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.20` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.25` | 110.49 USD | 616,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.40` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 6,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.55` | 10,020.00 USD | 616,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.60` | 8,290,000.00 USD | 8,290,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.65` | 273.90 USD | 606,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 333.94 USD | 606,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.80` | 8,290,000.00 USD | 8,290,000.00 USD | 1,780.00 USD | 2,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `48.90` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 0.00 USD | 960.40 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.95` | 252.58 USD | 605,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,580.00 USD | 605,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,740.00 USD | 604,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.30` | 8,280,000.00 USD | 8,280,000.00 USD | 15,190.00 USD | 4,490.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.35` | 24,210.00 USD | 598,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.40` | 8,250,000.00 USD | 8,250,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.45` | 419.34 USD | 574,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.50` | 8,240,000.00 USD | 8,240,000.00 USD | 2,830.00 USD | 7,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.55` | 18,010.00 USD | 573,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.60` | 4,410,000.00 USD | 4,410,000.00 USD | 5,570.00 USD | 14,890.00 USD | 16,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.60` | 8,230,000.00 USD | 8,230,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.65` | 73,260.00 USD | 555,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.70` | 4,380,000.00 USD | 4,380,000.00 USD | 12,650.00 USD | 3,970.00 USD | 8,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.70` | 8,220,000.00 USD | 8,220,000.00 USD | 12,090.00 USD | 0.00 USD | 13,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.75` | 3,180.00 USD | 482,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.80` | 4,350,000.00 USD | 4,350,000.00 USD | 6,420.00 USD | 11,200.00 USD | 23,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.80` | 8,190,000.00 USD | 8,190,000.00 USD | 9,930.00 USD | 8,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `49.90` | 4,310,000.00 USD | 4,310,000.00 USD | 24,520.00 USD | 18,280.00 USD | 24,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.90` | 8,170,000.00 USD | 8,170,000.00 USD | 45,030.00 USD | 19,460.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.95` | 19,920.00 USD | 479,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.00` | 4,240,000.00 USD | 4,240,000.00 USD | 21,740.00 USD | 24,020.00 USD | 44,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.00` | 8,100,000.00 USD | 8,100,000.00 USD | 29,070.00 USD | 26,820.00 USD | 25,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.05` | 1,820.00 USD | 459,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.10` | 4,150,000.00 USD | 4,150,000.00 USD | 7,310.00 USD | 6,650.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.10` | 8,020,000.00 USD | 8,020,000.00 USD | 363.50 USD | 682.90 USD | 8,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.20` | 4,130,000.00 USD | 4,130,000.00 USD | 177.10 USD | 709.61 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.20` | 8,010,000.00 USD | 8,010,000.00 USD | 6,960.00 USD | 500.40 USD | 42,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.25` | 102.51 USD | 457,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.30` | 4,120,000.00 USD | 4,120,000.00 USD | 171.03 USD | 3,880.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.30` | 7,960,000.00 USD | 7,960,000.00 USD | 16,270.00 USD | 10,780.00 USD | 7,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.35` | 1,140.00 USD | 457,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.40` | 4,120,000.00 USD | 4,120,000.00 USD | 8,260.00 USD | 11,890.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.40` | 7,930,000.00 USD | 7,930,000.00 USD | 28,280.00 USD | 26,580.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,720.00 USD | 456,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.50` | 4,100,000.00 USD | 4,100,000.00 USD | 8,910.00 USD | 8,790.00 USD | 10,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.50` | 7,840,000.00 USD | 7,840,000.00 USD | 32,490.00 USD | 6,790.00 USD | 44,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.55` | 84,100.00 USD | 451,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.60` | 4,070,000.00 USD | 4,070,000.00 USD | 7,330.00 USD | 3,440.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.60` | 7,760,000.00 USD | 7,760,000.00 USD | 67,580.00 USD | 21,530.00 USD | 31,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.70` | 4,050,000.00 USD | 4,050,000.00 USD | 8,170.00 USD | 2,300.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.70` | 7,630,000.00 USD | 7,630,000.00 USD | 65,920.00 USD | 32,820.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.75` | 9,650.00 USD | 367,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.80` | 4,020,000.00 USD | 4,020,000.00 USD | 12,550.00 USD | 3,100.00 USD | 8,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.80` | 7,490,000.00 USD | 7,490,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.90` | 4,000,000.00 USD | 4,000,000.00 USD | 826.24 USD | 260.05 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.90` | 7,400,000.00 USD | 7,400,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.95` | 431.55 USD | 357,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.00` | 3,990,000.00 USD | 3,990,000.00 USD | 5,040.00 USD | 0.00 USD | 430.77 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.00` | 7,140,000.00 USD | 7,140,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.10` | 3,990,000.00 USD | 3,990,000.00 USD | 9,210.00 USD | 6,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.10` | 7,020,000.00 USD | 7,020,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.15` | 219,370.00 USD | 357,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.20` | 3,970,000.00 USD | 3,970,000.00 USD | 1,770.00 USD | 1,130.00 USD | 19,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.20` | 6,940,000.00 USD | 6,940,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.25` | 202.44 USD | 137,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.30` | 3,950,000.00 USD | 3,950,000.00 USD | 8,650.00 USD | 9,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.30` | 6,870,000.00 USD | 6,870,000.00 USD | 28,400.00 USD | 26,720.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.35` | 453.93 USD | 137,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.40` | 3,930,000.00 USD | 3,930,000.00 USD | 3,250.00 USD | 5,460.00 USD | 416.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.40` | 6,770,000.00 USD | 6,770,000.00 USD | 73,130.00 USD | 42,820.00 USD | 46,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.45` | 27,210.00 USD | 137,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.50` | 3,920,000.00 USD | 3,920,000.00 USD | 7,580.00 USD | 10,010.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.50` | 6,610,000.00 USD | 6,610,000.00 USD | 38,520.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.55` | 551.07 USD | 110,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.60` | 3,860,000.00 USD | 3,860,000.00 USD | 5,990.00 USD | 17,860.00 USD | 709.44 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.60` | 6,510,000.00 USD | 6,510,000.00 USD | 37,880.00 USD | 36,790.00 USD | 41,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.65` | 9,100.00 USD | 109,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.70` | 3,840,000.00 USD | 3,840,000.00 USD | 2,660.00 USD | 12,840.00 USD | 44.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.70` | 6,390,000.00 USD | 6,390,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.75` | 6,480.00 USD | 100,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.80` | 3,820,000.00 USD | 3,820,000.00 USD | 10,010.00 USD | 18,760.00 USD | 12,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.80` | 6,360,000.00 USD | 6,360,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.85` | 13,680.00 USD | 93,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.90` | 3,780,000.00 USD | 3,780,000.00 USD | 10,800.00 USD | 19,770.00 USD | 21,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.90` | 6,300,000.00 USD | 6,300,000.00 USD | 5,870.00 USD | 25,410.00 USD | 28,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.95` | 13,950.00 USD | 80,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.00` | 3,730,000.00 USD | 3,730,000.00 USD | 20,190.00 USD | 25,620.00 USD | 16,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.00` | 6,240,000.00 USD | 6,240,000.00 USD | 65,840.00 USD | 26,440.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.05` | 2,860.00 USD | 66,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.10` | 3,660,000.00 USD | 3,660,000.00 USD | 34,790.00 USD | 17,300.00 USD | 44,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 6,140,000.00 USD | 6,140,000.00 USD | 24,220.00 USD | 28,090.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.15` | 1,900.00 USD | 63,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.20` | 3,570,000.00 USD | 3,570,000.00 USD | 13,190.00 USD | 5,050.00 USD | 49,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 6,050,000.00 USD | 6,050,000.00 USD | 38,380.00 USD | 13,960.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.25` | 4,930.00 USD | 61,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.30` | 3,500,000.00 USD | 3,500,000.00 USD | 26,510.00 USD | 22,090.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 5,970,000.00 USD | 5,970,000.00 USD | 26,450.00 USD | 40,700.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.35` | 134.02 USD | 56,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.40` | 3,440,000.00 USD | 3,440,000.00 USD | 15,630.00 USD | 15,400.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 5,890,000.00 USD | 5,890,000.00 USD | 20,580.00 USD | 38,950.00 USD | 19,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.45` | 5,820.00 USD | 56,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.50` | 3,400,000.00 USD | 3,400,000.00 USD | 53,990.00 USD | 30,000.00 USD | 79,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.50` | 5,810,000.00 USD | 5,810,000.00 USD | 38,650.00 USD | 0.00 USD | 11,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.55` | 8,700.00 USD | 50,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.60` | 3,240,000.00 USD | 3,240,000.00 USD | 9,060.00 USD | 43,700.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.60` | 5,760,000.00 USD | 5,760,000.00 USD | 60,960.00 USD | 31,860.00 USD | 59,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.65` | 1,050.00 USD | 42,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.70` | 3,180,000.00 USD | 3,180,000.00 USD | 18,270.00 USD | 19,780.00 USD | 40,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.70` | 5,610,000.00 USD | 5,610,000.00 USD | 19,550.00 USD | 75,910.00 USD | 108,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.75` | 30,280.00 USD | 40,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.80` | 3,100,000.00 USD | 3,100,000.00 USD | 28,880.00 USD | 50,850.00 USD | 72,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.80` | 5,410,000.00 USD | 5,410,000.00 USD | 30,590.00 USD | 25,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.85` | 5,950.00 USD | 10,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.90` | 2,950,000.00 USD | 2,950,000.00 USD | 44,710.00 USD | 55,550.00 USD | 30,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.90` | 5,350,000.00 USD | 5,350,000.00 USD | 30,900.00 USD | 11,650.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.95` | 531.09 USD | 4,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.00` | 2,820,000.00 USD | 2,820,000.00 USD | 31,870.00 USD | 34,720.00 USD | 52,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.00` | 5,270,000.00 USD | 5,270,000.00 USD | 39,690.00 USD | 25,380.00 USD | 97,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.05` | 202.12 USD | 4,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.10` | 2,700,000.00 USD | 2,700,000.00 USD | 12,590.00 USD | 63,920.00 USD | 88,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.10` | 5,110,000.00 USD | 5,110,000.00 USD | 45,320.00 USD | 20,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.15` | 2,030.00 USD | 3,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.20` | 2,530,000.00 USD | 2,530,000.00 USD | 36,030.00 USD | 34,380.00 USD | 46,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.20` | 5,050,000.00 USD | 5,050,000.00 USD | 162,460.00 USD | 64,060.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.25` | 1,030.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.30` | 2,420,000.00 USD | 2,420,000.00 USD | 28,400.00 USD | 37,270.00 USD | 16,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.30` | 4,800,000.00 USD | 4,800,000.00 USD | 59,390.00 USD | 57,120.00 USD | 35,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.35` | 941.09 USD | 941.09 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.40` | 2,340,000.00 USD | 2,340,000.00 USD | 12,600.00 USD | 19,860.00 USD | 8,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.40` | 4,640,000.00 USD | 4,640,000.00 USD | 61,460.00 USD | 31,500.00 USD | 99,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.50` | 2,290,000.00 USD | 2,290,000.00 USD | 21,250.00 USD | 15,340.00 USD | 22,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.50` | 4,450,000.00 USD | 4,450,000.00 USD | 60,260.00 USD | 7,980.00 USD | 28,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.60` | 2,240,000.00 USD | 2,240,000.00 USD | 75,950.00 USD | 3,830.00 USD | 20,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.60` | 4,350,000.00 USD | 4,350,000.00 USD | 52,800.00 USD | 3,780.00 USD | 20,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.70` | 2,140,000.00 USD | 2,140,000.00 USD | 6,210.00 USD | 11,100.00 USD | 11,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.70` | 4,280,000.00 USD | 4,280,000.00 USD | 131,400.00 USD | 21,330.00 USD | 13,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.80` | 2,110,000.00 USD | 2,110,000.00 USD | 53,640.00 USD | 28,920.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.80` | 4,110,000.00 USD | 4,110,000.00 USD | 99,150.00 USD | 43,900.00 USD | 302.55 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.90` | 2,020,000.00 USD | 2,020,000.00 USD | 50,300.00 USD | 39,560.00 USD | 27,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.90` | 3,970,000.00 USD | 3,970,000.00 USD | 160,820.00 USD | 22,780.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.00` | 1,900,000.00 USD | 1,900,000.00 USD | 76,010.00 USD | 30,780.00 USD | 86,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.00` | 3,770,000.00 USD | 3,770,000.00 USD | 380,340.00 USD | 71,820.00 USD | 304,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.10` | 1,710,000.00 USD | 1,710,000.00 USD | 105,010.00 USD | 27,610.00 USD | 74,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.10` | 3,020,000.00 USD | 3,020,000.00 USD | 302,190.00 USD | 5,360.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.20` | 1,500,000.00 USD | 1,500,000.00 USD | 72,600.00 USD | 57,270.00 USD | 47,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.20` | 2,670,000.00 USD | 2,670,000.00 USD | 205,060.00 USD | 5,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.30` | 1,320,000.00 USD | 1,320,000.00 USD | 46,340.00 USD | 55,750.00 USD | 15,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.30` | 2,460,000.00 USD | 2,460,000.00 USD | 381,380.00 USD | 71,490.00 USD | 181,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.40` | 1,210,000.00 USD | 1,210,000.00 USD | 102,880.00 USD | 110,050.00 USD | 24,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.40` | 1,820,000.00 USD | 1,820,000.00 USD | 304,270.00 USD | 78,990.00 USD | 93,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.50` | 968,710.00 USD | 968,710.00 USD | 24,100.00 USD | 82,700.00 USD | 16,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.50` | 1,350,000.00 USD | 1,350,000.00 USD | 194,580.00 USD | 63,740.00 USD | 257,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.60` | 845,330.00 USD | 845,330.00 USD | 25,070.00 USD | 44,770.00 USD | 43,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.60` | 831,250.00 USD | 831,250.00 USD | 18,530.00 USD | 11,000.00 USD | 131,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.70` | 731,900.00 USD | 731,900.00 USD | 6,600.00 USD | 23,060.00 USD | 105,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.70` | 670,350.00 USD | 670,350.00 USD | 0.00 USD | 3,600.00 USD | 41,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.80` | 596,440.00 USD | 596,440.00 USD | 0.00 USD | 48,420.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.80` | 625,440.00 USD | 625,440.00 USD | 0.00 USD | 35,700.00 USD | 26,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.90` | 524,100.00 USD | 524,100.00 USD | 66,900.00 USD | 65,440.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.90` | 563,300.00 USD | 563,300.00 USD | 0.00 USD | 112,280.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.00` | 380,920.00 USD | 380,920.00 USD | 40,710.00 USD | 54,150.00 USD | 55,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.00` | 402,720.00 USD | 402,720.00 USD | 97,700.00 USD | 2,830.00 USD | 19,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.10` | 230,860.00 USD | 230,860.00 USD | 50,530.00 USD | 0.00 USD | 80,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.10` | 282,840.00 USD | 282,840.00 USD | 54,590.00 USD | 18,510.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.20` | 100,140.00 USD | 100,140.00 USD | 39,390.00 USD | 7,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.20` | 145,060.00 USD | 145,060.00 USD | 57,400.00 USD | 59,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.30` | 52,860.00 USD | 52,860.00 USD | 52,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.30` | 27,940.00 USD | 27,940.00 USD | 23,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.40` | 4,800.00 USD | 4,800.00 USD | 0.00 USD | 0.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.70` | 613.46 USD | 613.46 USD | 0.00 USD | 0.00 USD | 613.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.70` | 174,240.00 USD | 174,240.00 USD | 174,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.70` | 348,480.00 USD | 348,480.00 USD | 174,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.80` | 3,790.00 USD | 3,790.00 USD | 0.00 USD | 0.00 USD | 3,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.80` | 439,450.00 USD | 439,450.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.90` | 56,850.00 USD | 56,850.00 USD | 51,520.00 USD | 0.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.90` | 580,780.00 USD | 580,780.00 USD | 141,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.00` | 61,230.00 USD | 61,230.00 USD | 0.00 USD | 0.00 USD | 4,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.00` | 751,900.00 USD | 751,900.00 USD | 2,590.00 USD | 0.00 USD | 168,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.20` | 70,570.00 USD | 70,570.00 USD | 0.00 USD | 9,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.20` | 831,840.00 USD | 831,840.00 USD | 0.00 USD | 79,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.30` | 118,460.00 USD | 118,460.00 USD | 10,140.00 USD | 8,440.00 USD | 29,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.30` | 879,910.00 USD | 879,910.00 USD | 0.00 USD | 5,360.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.40` | 191,530.00 USD | 191,530.00 USD | 5,040.00 USD | 58,450.00 USD | 9,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.40` | 898,800.00 USD | 898,800.00 USD | 2,650.00 USD | 16,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.50` | 671,750.00 USD | 671,750.00 USD | 169,280.00 USD | 156,300.00 USD | 154,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.50` | 1,290,000.00 USD | 1,290,000.00 USD | 170,750.00 USD | 214,910.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.60` | 1,050,000.00 USD | 1,050,000.00 USD | 101,920.00 USD | 173,560.00 USD | 102,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.60` | 1,860,000.00 USD | 1,860,000.00 USD | 363,190.00 USD | 201,730.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.70` | 1,520,000.00 USD | 1,520,000.00 USD | 110,240.00 USD | 63,740.00 USD | 295,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.70` | 2,300,000.00 USD | 2,300,000.00 USD | 152,150.00 USD | 169,990.00 USD | 116,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.80` | 1,790,000.00 USD | 1,790,000.00 USD | 128,400.00 USD | 40,070.00 USD | 106,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.80` | 2,890,000.00 USD | 2,890,000.00 USD | 172,110.00 USD | 101,840.00 USD | 318,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.90` | 1,890,000.00 USD | 1,890,000.00 USD | 45,140.00 USD | 17,930.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.90` | 3,360,000.00 USD | 3,360,000.00 USD | 113,780.00 USD | 52,200.00 USD | 307,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.00` | 1,970,000.00 USD | 1,970,000.00 USD | 6,480.00 USD | 43,030.00 USD | 29,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.00` | 3,680,000.00 USD | 3,680,000.00 USD | 88,680.00 USD | 56,390.00 USD | 178,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.10` | 2,170,000.00 USD | 2,170,000.00 USD | 77,000.00 USD | 77,400.00 USD | 46,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.10` | 3,820,000.00 USD | 3,820,000.00 USD | 36,580.00 USD | 79,290.00 USD | 21,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.20` | 2,430,000.00 USD | 2,430,000.00 USD | 53,080.00 USD | 78,490.00 USD | 120,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.20` | 3,990,000.00 USD | 3,990,000.00 USD | 118,850.00 USD | 23,920.00 USD | 23,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.30` | 2,630,000.00 USD | 2,630,000.00 USD | 70,930.00 USD | 49,300.00 USD | 87,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.30` | 4,190,000.00 USD | 4,190,000.00 USD | 76,940.00 USD | 28,570.00 USD | 98,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.40` | 2,870,000.00 USD | 2,870,000.00 USD | 90,030.00 USD | 53,690.00 USD | 91,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.40` | 4,670,000.00 USD | 4,670,000.00 USD | 124,180.00 USD | 74,860.00 USD | 277,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.50` | 3,310,000.00 USD | 3,310,000.00 USD | 197,830.00 USD | 69,230.00 USD | 178,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.50` | 4,800,000.00 USD | 4,800,000.00 USD | 99,810.00 USD | 34,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.60` | 3,520,000.00 USD | 3,520,000.00 USD | 85,090.00 USD | 51,920.00 USD | 67,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.60` | 5,060,000.00 USD | 5,060,000.00 USD | 149,560.00 USD | 76,180.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.70` | 3,750,000.00 USD | 3,750,000.00 USD | 62,800.00 USD | 63,340.00 USD | 106,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.70` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 37,980.00 USD | 58,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.75` | 155.35 USD | 155.35 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `57.80` | 3,880,000.00 USD | 3,880,000.00 USD | 18,150.00 USD | 31,870.00 USD | 80,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.80` | 5,280,000.00 USD | 5,280,000.00 USD | 27,080.00 USD | 38,610.00 USD | 58,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.90` | 3,960,000.00 USD | 3,960,000.00 USD | 25,080.00 USD | 25,510.00 USD | 28,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.90` | 5,330,000.00 USD | 5,330,000.00 USD | 14,390.00 USD | 5,500.00 USD | 30,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.95` | 125.75 USD | 281.10 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.00` | 4,000,000.00 USD | 4,000,000.00 USD | 10,450.00 USD | 9,480.00 USD | 15,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.00` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 5,470.00 USD | 107,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.10` | 4,070,000.00 USD | 4,070,000.00 USD | 31,400.00 USD | 17,830.00 USD | 21,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.10` | 5,480,000.00 USD | 5,480,000.00 USD | 5,470.00 USD | 19,160.00 USD | 14,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.20` | 4,140,000.00 USD | 4,140,000.00 USD | 36,640.00 USD | 34,800.00 USD | 4,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.20` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 31,590.00 USD | 302.55 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.30` | 4,280,000.00 USD | 4,280,000.00 USD | 33,360.00 USD | 38,620.00 USD | 64,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.30` | 5,610,000.00 USD | 5,610,000.00 USD | 48,850.00 USD | 11,000.00 USD | 36,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.40` | 4,380,000.00 USD | 4,380,000.00 USD | 27,360.00 USD | 18,940.00 USD | 49,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.40` | 5,730,000.00 USD | 5,730,000.00 USD | 27,290.00 USD | 9,260.00 USD | 86,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.50` | 4,380,000.00 USD | 4,380,000.00 USD | 1,420.00 USD | 1,200.00 USD | 124.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.50` | 5,760,000.00 USD | 5,760,000.00 USD | 2,060.00 USD | 24,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.60` | 4,450,000.00 USD | 4,450,000.00 USD | 21,940.00 USD | 5,920.00 USD | 40,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.60` | 5,860,000.00 USD | 5,860,000.00 USD | 30,680.00 USD | 20,260.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.70` | 4,530,000.00 USD | 4,530,000.00 USD | 44,920.00 USD | 10,120.00 USD | 29,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.70` | 5,920,000.00 USD | 5,920,000.00 USD | 15,810.00 USD | 11,600.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.80` | 4,600,000.00 USD | 4,600,000.00 USD | 36,630.00 USD | 5,970.00 USD | 23,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.80` | 5,930,000.00 USD | 5,930,000.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `58.85` | 1,480.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.90` | 4,760,000.00 USD | 4,760,000.00 USD | 24,050.00 USD | 58,880.00 USD | 80,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.90` | 6,070,000.00 USD | 6,070,000.00 USD | 2,140.00 USD | 54,240.00 USD | 83,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.00` | 5,020,000.00 USD | 5,020,000.00 USD | 123,770.00 USD | 53,650.00 USD | 80,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.00` | 6,520,000.00 USD | 6,520,000.00 USD | 259,280.00 USD | 65,270.00 USD | 118,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.10` | 5,280,000.00 USD | 5,280,000.00 USD | 88,790.00 USD | 37,020.00 USD | 135,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.10` | 6,810,000.00 USD | 6,810,000.00 USD | 93,390.00 USD | 45,400.00 USD | 158,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.20` | 5,470,000.00 USD | 5,470,000.00 USD | 89,410.00 USD | 46,380.00 USD | 49,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.20` | 7,160,000.00 USD | 7,160,000.00 USD | 153,580.00 USD | 18,540.00 USD | 174,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.25` | 213.89 USD | 1,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.30` | 5,710,000.00 USD | 5,710,000.00 USD | 146,880.00 USD | 30,070.00 USD | 66,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.30` | 7,430,000.00 USD | 7,430,000.00 USD | 88,710.00 USD | 67,460.00 USD | 114,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.35` | 9,440.00 USD | 11,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.40` | 5,820,000.00 USD | 5,820,000.00 USD | 35,830.00 USD | 30,410.00 USD | 49,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.40` | 7,740,000.00 USD | 7,740,000.00 USD | 107,040.00 USD | 73,620.00 USD | 124,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.45` | 214.02 USD | 11,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.50` | 5,960,000.00 USD | 5,960,000.00 USD | 78,730.00 USD | 34,150.00 USD | 28,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.50` | 7,890,000.00 USD | 7,890,000.00 USD | 67,060.00 USD | 61,370.00 USD | 21,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.60` | 6,050,000.00 USD | 6,050,000.00 USD | 29,830.00 USD | 49,290.00 USD | 5,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.60` | 8,250,000.00 USD | 8,250,000.00 USD | 184,700.00 USD | 106,840.00 USD | 72,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.65` | 215.34 USD | 11,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.70` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 15,700.00 USD | 59,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.70` | 8,570,000.00 USD | 8,570,000.00 USD | 55,510.00 USD | 99,970.00 USD | 162,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.80` | 6,170,000.00 USD | 6,170,000.00 USD | 21,030.00 USD | 26,470.00 USD | 177.92 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.80` | 8,930,000.00 USD | 8,930,000.00 USD | 118,240.00 USD | 91,980.00 USD | 154,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.90` | 6,340,000.00 USD | 6,340,000.00 USD | 102,020.00 USD | 15,860.00 USD | 48,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.90` | 9,140,000.00 USD | 9,140,000.00 USD | 142,290.00 USD | 34,490.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.00` | 6,570,000.00 USD | 6,570,000.00 USD | 162,340.00 USD | 28,040.00 USD | 45,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.00` | 9,390,000.00 USD | 9,390,000.00 USD | 100,570.00 USD | 67,520.00 USD | 83,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.10` | 6,690,000.00 USD | 6,690,000.00 USD | 61,440.00 USD | 25,530.00 USD | 32,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.10` | 9,770,000.00 USD | 9,770,000.00 USD | 200,540.00 USD | 84,980.00 USD | 95,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.15` | 208,880.00 USD | 220,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.20` | 6,840,000.00 USD | 6,840,000.00 USD | 56,510.00 USD | 18,380.00 USD | 68,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.20` | 10,140,000.00 USD | 10,140,000.00 USD | 162,230.00 USD | 99,360.00 USD | 108,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.30` | 6,930,000.00 USD | 6,930,000.00 USD | 44,650.00 USD | 25,170.00 USD | 26,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.30` | 10,550,000.00 USD | 10,550,000.00 USD | 133,350.00 USD | 100,380.00 USD | 170,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.40` | 7,060,000.00 USD | 7,060,000.00 USD | 66,740.00 USD | 13,730.00 USD | 42,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.40` | 10,910,000.00 USD | 10,910,000.00 USD | 55,050.00 USD | 100,560.00 USD | 202,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.45` | 230.92 USD | 220,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.50` | 7,130,000.00 USD | 7,130,000.00 USD | 22,700.00 USD | 19,320.00 USD | 36,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.50` | 11,270,000.00 USD | 11,270,000.00 USD | 115,390.00 USD | 80,510.00 USD | 169,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.55` | 435.96 USD | 221,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.60` | 7,200,000.00 USD | 7,200,000.00 USD | 40,710.00 USD | 20,390.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.60` | 11,660,000.00 USD | 11,660,000.00 USD | 251,100.00 USD | 16,970.00 USD | 118,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.70` | 7,270,000.00 USD | 7,270,000.00 USD | 33,350.00 USD | 24,020.00 USD | 8,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.70` | 11,800,000.00 USD | 11,800,000.00 USD | 76,200.00 USD | 37,000.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.75` | 218.70 USD | 221,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.80` | 7,340,000.00 USD | 7,340,000.00 USD | 10,510.00 USD | 18,960.00 USD | 49,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.80` | 11,950,000.00 USD | 11,950,000.00 USD | 46,960.00 USD | 28,960.00 USD | 76,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.90` | 7,440,000.00 USD | 7,440,000.00 USD | 37,840.00 USD | 31,510.00 USD | 24,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.90` | 12,160,000.00 USD | 12,160,000.00 USD | 105,970.00 USD | 43,870.00 USD | 64,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.95` | 397.39 USD | 222,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.00` | 7,510,000.00 USD | 7,510,000.00 USD | 43,930.00 USD | 6,430.00 USD | 18,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 12,220,000.00 USD | 12,220,000.00 USD | 43,120.00 USD | 11,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.10` | 7,560,000.00 USD | 7,560,000.00 USD | 21,130.00 USD | 18,440.00 USD | 15,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 12,260,000.00 USD | 12,260,000.00 USD | 31,540.00 USD | 13,590.00 USD | 189.67 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.20` | 7,680,000.00 USD | 7,680,000.00 USD | 74,800.00 USD | 5,570.00 USD | 39,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.20` | 12,390,000.00 USD | 12,390,000.00 USD | 51,570.00 USD | 24,770.00 USD | 47,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.30` | 7,700,000.00 USD | 7,700,000.00 USD | 3,530.00 USD | 6,650.00 USD | 7,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.30` | 12,440,000.00 USD | 12,440,000.00 USD | 14,390.00 USD | 13,210.00 USD | 24,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.40` | 7,710,000.00 USD | 7,710,000.00 USD | 1,190.00 USD | 709.61 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.40` | 12,570,000.00 USD | 12,570,000.00 USD | 62,340.00 USD | 25,720.00 USD | 43,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.50` | 12,670,000.00 USD | 12,670,000.00 USD | 17,710.00 USD | 42,440.00 USD | 41,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.55` | 222.20 USD | 222,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `61.60` | 12,880,000.00 USD | 12,880,000.00 USD | 32,920.00 USD | 58,350.00 USD | 121,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.70` | 13,080,000.00 USD | 13,080,000.00 USD | 82,860.00 USD | 10,880.00 USD | 99,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.80` | 13,340,000.00 USD | 13,340,000.00 USD | 169,680.00 USD | 25,670.00 USD | 71,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.90` | 13,490,000.00 USD | 13,490,000.00 USD | 73,690.00 USD | 32,820.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.00` | 13,590,000.00 USD | 13,590,000.00 USD | 50,080.00 USD | 8,550.00 USD | 40,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `62.05` | 223.38 USD | 222,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `62.10` | 13,600,000.00 USD | 13,600,000.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.20` | 13,710,000.00 USD | 13,710,000.00 USD | 34,230.00 USD | 34,620.00 USD | 41,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.30` | 13,820,000.00 USD | 13,820,000.00 USD | 25,910.00 USD | 23,450.00 USD | 57,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.40` | 13,930,000.00 USD | 13,930,000.00 USD | 62,940.00 USD | 25,250.00 USD | 25,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `62.95` | 138.49 USD | 222,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `63.45` | 3,350.00 USD | 225,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `63.55` | 8,180.00 USD | 234,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.05` | 121.36 USD | 234,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.85` | 709.03 USD | 234,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `70.25` | 40,610.00 USD | 275,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `76.35` | 8,380.00 USD | 283,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.65` | 111.04 USD | 284,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.75` | 578,460.00 USD | 862,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.85` | 602.56 USD | 863,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `79.95` | 3,200.00 USD | 866,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.75` | 646.00 USD | 866,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.05` | 19,000.00 USD | 885,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.55` | 123.96 USD | 886,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.75` | 741.47 USD | 886,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.25` | 874.32 USD | 887,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.75` | 214.32 USD | 887,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `83.05` | 2,740.00 USD | 890,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `84.25` | 22,480.00 USD | 913,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `89.55` | 100.30 USD | 913,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `92.55` | 122.17 USD | 913,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.15` | 2,450.00 USD | 915,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.35` | 166.21 USD | 915,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.55` | 31,070.00 USD | 947,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.25` | 213.71 USD | 947,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.85` | 2,320.00 USD | 949,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.95` | 354,100.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.75` | 1,620.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.85` | 1,860.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.25` | 199.48 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.05` | 6,470.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `11.35` | 3,050,000.00 USD | 0.00 USD | 136.20 USD | `-79.65%` | `12.00` |
| `Live` | `Long` | `12.25` | 3,050,000.00 USD | 0.00 USD | 122.50 USD | `-78.04%` | `10.00` |
| `Live` | `Long` | `12.75` | 3,050,000.00 USD | 0.00 USD | 2,560.00 USD | `-77.14%` | `200.43` |
| `Live` | `Long` | `13.15` | 3,050,000.00 USD | 0.00 USD | 2,220.00 USD | `-76.43%` | `168.79` |
| `Live` | `Long` | `13.65` | 3,040,000.00 USD | 0.00 USD | 150.15 USD | `-75.53%` | `11.00` |
| `Live` | `Long` | `14.95` | 3,040,000.00 USD | 0.00 USD | 2,250.00 USD | `-73.20%` | `150.57` |
| `Live` | `Long` | `17.45` | 3,040,000.00 USD | 0.00 USD | 16,230.00 USD | `-68.72%` | `930.00` |
| `Live` | `Long` | `18.15` | 3,030,000.00 USD | 0.00 USD | 403.66 USD | `-67.46%` | `22.24` |
| `Live` | `Long` | `18.25` | 3,030,000.00 USD | 0.00 USD | 2,190.00 USD | `-67.29%` | `120.00` |
| `Live` | `Long` | `19.05` | 3,020,000.00 USD | 0.00 USD | 3,590.00 USD | `-65.85%` | `188.60` |
| `Live` | `Long` | `19.45` | 3,020,000.00 USD | 0.00 USD | 2,010.00 USD | `-65.13%` | `103.47` |
| `Live` | `Long` | `20.75` | 3,020,000.00 USD | 0.00 USD | 4,480.00 USD | `-62.80%` | `215.72` |
| `Live` | `Long` | `21.05` | 3,010,000.00 USD | 0.00 USD | 1,260.00 USD | `-62.27%` | `60.00` |
| `Live` | `Long` | `22.25` | 3,010,000.00 USD | 0.00 USD | 358.89 USD | `-60.11%` | `16.13` |
| `Live` | `Long` | `22.65` | 3,010,000.00 USD | 0.00 USD | 961.04 USD | `-59.40%` | `42.43` |
| `Live` | `Long` | `23.35` | 3,010,000.00 USD | 0.00 USD | 647.03 USD | `-58.14%` | `27.71` |
| `Live` | `Long` | `23.75` | 3,010,000.00 USD | 0.00 USD | 375.73 USD | `-57.43%` | `15.82` |
| `Live` | `Long` | `23.85` | 3,010,000.00 USD | 0.00 USD | 7,220.00 USD | `-57.25%` | `302.87` |
| `Live` | `Long` | `24.65` | 3,000,000.00 USD | 0.00 USD | 113,020.00 USD | `-55.81%` | `4,584.81` |
| `Live` | `Long` | `25.25` | 2,890,000.00 USD | 0.00 USD | 277,980.00 USD | `-54.74%` | `11,009.19` |
| `Live` | `Long` | `25.35` | 2,610,000.00 USD | 0.00 USD | 173.39 USD | `-54.56%` | `6.84` |
| `Live` | `Long` | `25.55` | 2,610,000.00 USD | 0.00 USD | 50,740.00 USD | `-54.20%` | `1,985.99` |
| `Live` | `Long` | `25.75` | 2,560,000.00 USD | 0.00 USD | 189.52 USD | `-53.84%` | `7.36` |
| `Live` | `Long` | `25.95` | 2,560,000.00 USD | 0.00 USD | 374.20 USD | `-53.48%` | `14.42` |
| `Live` | `Long` | `27.05` | 2,560,000.00 USD | 0.00 USD | 5,510.00 USD | `-51.51%` | `203.85` |
| `Live` | `Long` | `27.15` | 2,550,000.00 USD | 0.00 USD | 3,210.00 USD | `-51.33%` | `118.41` |
| `Live` | `Long` | `27.55` | 2,550,000.00 USD | 0.00 USD | 272.75 USD | `-50.61%` | `9.90` |
| `Live` | `Long` | `27.95` | 2,550,000.00 USD | 0.00 USD | 173.85 USD | `-49.90%` | `6.22` |
| `Live` | `Long` | `28.55` | 2,550,000.00 USD | 0.00 USD | 8,560.00 USD | `-48.82%` | `300.00` |
| `Live` | `Long` | `29.15` | 2,540,000.00 USD | 0.00 USD | 755.28 USD | `-47.75%` | `25.91` |
| `Live` | `Long` | `29.75` | 2,540,000.00 USD | 0.00 USD | 297,500.00 USD | `-46.67%` | `10,000.00` |
| `Live` | `Long` | `30.05` | 2,240,000.00 USD | 0.00 USD | 218.46 USD | `-46.13%` | `7.27` |
| `Live` | `Long` | `30.55` | 2,240,000.00 USD | 0.00 USD | 152.75 USD | `-45.24%` | `5.00` |
| `Live` | `Long` | `30.65` | 2,240,000.00 USD | 0.00 USD | 1,540.00 USD | `-45.06%` | `50.19` |
| `Live` | `Long` | `30.95` | 2,240,000.00 USD | 0.00 USD | 538.53 USD | `-44.52%` | `17.40` |
| `Live` | `Long` | `31.15` | 2,240,000.00 USD | 0.00 USD | 27,840.00 USD | `-44.16%` | `893.80` |
| `Live` | `Long` | `31.55` | 2,210,000.00 USD | 0.00 USD | 1,060.00 USD | `-43.44%` | `33.49` |
| `Live` | `Long` | `31.65` | 2,210,000.00 USD | 0.00 USD | 4,640.00 USD | `-43.26%` | `146.53` |
| `Live` | `Long` | `31.85` | 2,210,000.00 USD | 0.00 USD | 2,870.00 USD | `-42.91%` | `90.00` |
| `Live` | `Long` | `31.95` | 2,200,000.00 USD | 0.00 USD | 125.24 USD | `-42.73%` | `3.92` |
| `Live` | `Long` | `32.15` | 2,200,000.00 USD | 0.00 USD | 450.10 USD | `-42.37%` | `14.00` |
| `Live` | `Long` | `32.25` | 2,200,000.00 USD | 0.00 USD | 5,610.00 USD | `-42.19%` | `174.01` |
| `Live` | `Long` | `32.35` | 2,200,000.00 USD | 0.00 USD | 172.10 USD | `-42.01%` | `5.32` |
| `Live` | `Long` | `32.65` | 2,200,000.00 USD | 0.00 USD | 653.00 USD | `-41.47%` | `20.00` |
| `Live` | `Long` | `32.75` | 2,200,000.00 USD | 0.00 USD | 3,750.00 USD | `-41.29%` | `114.55` |
| `Live` | `Long` | `32.95` | 2,190,000.00 USD | 0.00 USD | 32,950.00 USD | `-40.93%` | `1,000.01` |
| `Live` | `Long` | `33.25` | 2,160,000.00 USD | 0.00 USD | 6,210.00 USD | `-40.40%` | `186.71` |
| `Live` | `Long` | `33.65` | 2,150,000.00 USD | 0.00 USD | 257.76 USD | `-39.68%` | `7.66` |
| `Live` | `Long` | `34.05` | 2,150,000.00 USD | 0.00 USD | 182.85 USD | `-38.96%` | `5.37` |
| `Live` | `Long` | `34.15` | 2,150,000.00 USD | 0.00 USD | 126.70 USD | `-38.78%` | `3.71` |
| `Live` | `Long` | `34.45` | 2,150,000.00 USD | 0.00 USD | 65,890.00 USD | `-38.25%` | `1,912.61` |
| `Live` | `Long` | `34.65` | 2,090,000.00 USD | 0.00 USD | 3,240.00 USD | `-37.89%` | `93.56` |
| `Live` | `Long` | `34.95` | 2,090,000.00 USD | 0.00 USD | 4,670.00 USD | `-37.35%` | `133.63` |
| `Live` | `Long` | `35.05` | 2,080,000.00 USD | 0.00 USD | 166.49 USD | `-37.17%` | `4.75` |
| `Live` | `Long` | `35.55` | 2,080,000.00 USD | 0.00 USD | 423.76 USD | `-36.27%` | `11.92` |
| `Live` | `Long` | `36.05` | 2,080,000.00 USD | 0.00 USD | 314.72 USD | `-35.38%` | `8.73` |
| `Live` | `Long` | `36.35` | 2,080,000.00 USD | 0.00 USD | 3,020.00 USD | `-34.84%` | `83.03` |
| `Live` | `Long` | `36.45` | 2,080,000.00 USD | 0.00 USD | 708.59 USD | `-34.66%` | `19.44` |
| `Live` | `Long` | `36.55` | 2,080,000.00 USD | 0.00 USD | 2,990.00 USD | `-34.48%` | `81.91` |
| `Live` | `Long` | `36.75` | 2,070,000.00 USD | 0.00 USD | 101.80 USD | `-34.12%` | `2.77` |
| `Live` | `Long` | `36.85` | 2,070,000.00 USD | 0.00 USD | 147.03 USD | `-33.94%` | `3.99` |
| `Live` | `Long` | `36.95` | 2,070,000.00 USD | 0.00 USD | 960.70 USD | `-33.76%` | `26.00` |
| `Live` | `Long` | `37.05` | 2,070,000.00 USD | 0.00 USD | 1,050.00 USD | `-33.58%` | `28.27` |
| `Live` | `Long` | `37.15` | 2,070,000.00 USD | 0.00 USD | 438.74 USD | `-33.41%` | `11.81` |
| `Live` | `Long` | `37.35` | 2,070,000.00 USD | 0.00 USD | 9,260.00 USD | `-33.05%` | `247.91` |
| `Live` | `Long` | `37.55` | 2,060,000.00 USD | 0.00 USD | 3,530.00 USD | `-32.69%` | `94.04` |
| `Live` | `Long` | `37.75` | 2,060,000.00 USD | 0.00 USD | 377.50 USD | `-32.33%` | `10.00` |
| `Live` | `Long` | `37.85` | 2,060,000.00 USD | 0.00 USD | 6,540.00 USD | `-32.15%` | `172.70` |
| `Live` | `Long` | `37.95` | 2,050,000.00 USD | 0.00 USD | 446.67 USD | `-31.97%` | `11.77` |
| `Live` | `Long` | `38.25` | 2,050,000.00 USD | 0.00 USD | 695.38 USD | `-31.43%` | `18.18` |
| `Live` | `Long` | `38.35` | 2,050,000.00 USD | 0.00 USD | 847.54 USD | `-31.25%` | `22.10` |
| `Live` | `Long` | `38.45` | 2,050,000.00 USD | 0.00 USD | 2,400.00 USD | `-31.07%` | `62.34` |
| `Live` | `Long` | `38.55` | 2,050,000.00 USD | 0.00 USD | 993.82 USD | `-30.90%` | `25.78` |
| `Live` | `Long` | `38.65` | 2,050,000.00 USD | 0.00 USD | 4,280.00 USD | `-30.72%` | `110.74` |
| `Live` | `Long` | `38.75` | 2,040,000.00 USD | 0.00 USD | 1,040.00 USD | `-30.54%` | `26.84` |
| `Live` | `Long` | `38.95` | 2,040,000.00 USD | 0.00 USD | 3,700.00 USD | `-30.18%` | `95.00` |
| `Live` | `Long` | `39.05` | 2,040,000.00 USD | 0.00 USD | 664,760.00 USD | `-30.00%` | `17,023.28` |
| `Live` | `Long` | `39.15` | 1,370,000.00 USD | 0.00 USD | 570.02 USD | `-29.82%` | `14.56` |
| `Live` | `Long` | `39.35` | 1,370,000.00 USD | 0.00 USD | 264.83 USD | `-29.46%` | `6.73` |
| `Live` | `Long` | `39.55` | 1,370,000.00 USD | 0.00 USD | 1,030.00 USD | `-29.10%` | `26.06` |
| `Live` | `Long` | `39.65` | 1,370,000.00 USD | 0.00 USD | 5,900.00 USD | `-28.92%` | `148.78` |
| `Live` | `Long` | `39.75` | 1,360,000.00 USD | 0.00 USD | 1,180.00 USD | `-28.74%` | `29.57` |
| `Live` | `Long` | `39.85` | 1,360,000.00 USD | 0.00 USD | 5,390.00 USD | `-28.57%` | `135.28` |
| `Live` | `Long` | `40.05` | 1,360,000.00 USD | 0.00 USD | 2,160.00 USD | `-28.21%` | `53.97` |
| `Live` | `Long` | `40.25` | 1,350,000.00 USD | 0.00 USD | 1,000.00 USD | `-27.85%` | `24.93` |
| `Live` | `Long` | `40.45` | 1,350,000.00 USD | 0.00 USD | 1,010.00 USD | `-27.49%` | `24.92` |
| `Live` | `Long` | `40.55` | 1,350,000.00 USD | 0.00 USD | 133.00 USD | `-27.31%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,350,000.00 USD | 0.00 USD | 274.39 USD | `-27.13%` | `6.75` |
| `Live` | `Long` | `40.85` | 1,350,000.00 USD | 0.00 USD | 6,340.00 USD | `-26.77%` | `155.23` |
| `Live` | `Long` | `40.95` | 1,350,000.00 USD | 0.00 USD | 816.13 USD | `-26.59%` | `19.93` |
| `Live` | `Long` | `41.05` | 1,350,000.00 USD | 0.00 USD | 727.00 USD | `-26.41%` | `17.71` |
| `Live` | `Long` | `41.25` | 1,340,000.00 USD | 0.00 USD | 14,850.00 USD | `-26.06%` | `359.91` |
| `Live` | `Long` | `41.45` | 1,330,000.00 USD | 0.00 USD | 644.96 USD | `-25.70%` | `15.56` |
| `Live` | `Long` | `41.65` | 1,330,000.00 USD | 0.00 USD | 9,160.00 USD | `-25.34%` | `220.00` |
| `Live` | `Long` | `41.85` | 1,320,000.00 USD | 0.00 USD | 3,720.00 USD | `-24.98%` | `88.83` |
| `Live` | `Long` | `41.95` | 1,320,000.00 USD | 0.00 USD | 299.10 USD | `-24.80%` | `7.13` |
| `Live` | `Long` | `42.05` | 1,320,000.00 USD | 0.00 USD | 201.00 USD | `-24.62%` | `4.78` |
| `Live` | `Long` | `42.15` | 1,320,000.00 USD | 0.00 USD | 64,190.00 USD | `-24.44%` | `1,522.78` |
| `Live` | `Long` | `42.25` | 1,250,000.00 USD | 0.00 USD | 35,410.00 USD | `-24.26%` | `838.00` |
| `Live` | `Long` | `42.55` | 1,220,000.00 USD | 0.00 USD | 339.97 USD | `-23.73%` | `7.99` |
| `Live` | `Long` | `42.65` | 1,220,000.00 USD | 0.00 USD | 1,570.00 USD | `-23.55%` | `36.70` |
| `Live` | `Long` | `42.85` | 1,210,000.00 USD | 0.00 USD | 5,800.00 USD | `-23.19%` | `135.38` |
| `Live` | `Long` | `42.95` | 1,210,000.00 USD | 0.00 USD | 2,000.00 USD | `-23.01%` | `46.65` |
| `Live` | `Long` | `43.05` | 1,210,000.00 USD | 0.00 USD | 9,080.00 USD | `-22.83%` | `211.00` |
| `Live` | `Long` | `43.15` | 1,200,000.00 USD | 0.00 USD | 1,580.00 USD | `-22.65%` | `36.59` |
| `Live` | `Long` | `43.25` | 1,200,000.00 USD | 0.00 USD | 121,210.00 USD | `-22.47%` | `2,802.44` |
| `Live` | `Long` | `43.35` | 1,070,000.00 USD | 0.00 USD | 5,700.00 USD | `-22.29%` | `131.46` |
| `Live` | `Long` | `43.45` | 1,070,000.00 USD | 0.00 USD | 710.84 USD | `-22.11%` | `16.36` |
| `Live` | `Long` | `43.55` | 1,070,000.00 USD | 0.00 USD | 5,610.00 USD | `-21.93%` | `128.71` |
| `Live` | `Long` | `43.65` | 1,060,000.00 USD | 0.00 USD | 426.02 USD | `-21.75%` | `9.76` |
| `Live` | `Long` | `43.75` | 1,060,000.00 USD | 0.00 USD | 24,460.00 USD | `-21.57%` | `559.15` |
| `Live` | `Long` | `43.85` | 1,040,000.00 USD | 0.00 USD | 801.14 USD | `-21.39%` | `18.27` |
| `Live` | `Long` | `44.15` | 1,040,000.00 USD | 0.00 USD | 2,380.00 USD | `-20.86%` | `53.99` |
| `Live` | `Long` | `44.25` | 1,030,000.00 USD | 0.00 USD | 1,330.00 USD | `-20.68%` | `30.00` |
| `Live` | `Long` | `44.35` | 1,030,000.00 USD | 0.00 USD | 84,440.00 USD | `-20.50%` | `1,903.87` |
| `Live` | `Long` | `44.55` | 948,680.00 USD | 0.00 USD | 842.44 USD | `-20.14%` | `18.91` |
| `Live` | `Long` | `44.65` | 947,830.00 USD | 0.00 USD | 1,340.00 USD | `-19.96%` | `30.00` |
| `Live` | `Long` | `44.75` | 946,490.00 USD | 0.00 USD | 4,230.00 USD | `-19.78%` | `94.55` |
| `Live` | `Long` | `44.85` | 942,260.00 USD | 0.00 USD | 134.55 USD | `-19.60%` | `3.00` |
| `Live` | `Long` | `44.95` | 942,130.00 USD | 0.00 USD | 2,790.00 USD | `-19.42%` | `62.02` |
| `Live` | `Long` | `45.05` | 939,340.00 USD | 0.00 USD | 4,830.00 USD | `-19.24%` | `107.31` |
| `Live` | `Long` | `45.15` | 934,510.00 USD | 0.00 USD | 8,710.00 USD | `-19.06%` | `193.00` |
| `Live` | `Long` | `45.25` | 925,790.00 USD | 0.00 USD | 3,180.00 USD | `-18.89%` | `70.37` |
| `Live` | `Long` | `45.35` | 922,610.00 USD | 0.00 USD | 2,180.00 USD | `-18.71%` | `48.02` |
| `Live` | `Long` | `45.45` | 920,430.00 USD | 0.00 USD | 23,940.00 USD | `-18.53%` | `526.65` |
| `Live` | `Long` | `45.55` | 896,490.00 USD | 0.00 USD | 12,060.00 USD | `-18.35%` | `264.81` |
| `Live` | `Long` | `45.65` | 884,430.00 USD | 0.00 USD | 42,180.00 USD | `-18.17%` | `924.03` |
| `Live` | `Long` | `45.95` | 842,250.00 USD | 0.00 USD | 30,970.00 USD | `-17.63%` | `673.93` |
| `Live` | `Long` | `46.05` | 811,280.00 USD | 0.00 USD | 706.41 USD | `-17.45%` | `15.34` |
| `Live` | `Long` | `46.15` | 810,580.00 USD | 0.00 USD | 265.82 USD | `-17.27%` | `5.76` |
| `Live` | `Long` | `46.35` | 810,310.00 USD | 0.00 USD | 22,820.00 USD | `-16.91%` | `492.25` |
| `Live` | `Long` | `46.55` | 787,500.00 USD | 0.00 USD | 52,170.00 USD | `-16.55%` | `1,120.69` |
| `Live` | `Long` | `46.65` | 735,330.00 USD | 0.00 USD | 2,390.00 USD | `-16.38%` | `51.33` |
| `Live` | `Long` | `46.75` | 732,930.00 USD | 0.00 USD | 1,590.00 USD | `-16.20%` | `34.08` |
| `Live` | `Long` | `46.85` | 731,340.00 USD | 0.00 USD | 358.40 USD | `-16.02%` | `7.65` |
| `Live` | `Long` | `46.95` | 730,980.00 USD | 0.00 USD | 158.22 USD | `-15.84%` | `3.37` |
| `Live` | `Long` | `47.05` | 730,820.00 USD | 0.00 USD | 2,140.00 USD | `-15.66%` | `45.57` |
| `Live` | `Long` | `47.15` | 728,680.00 USD | 0.00 USD | 1,980.00 USD | `-15.48%` | `42.07` |
| `Live` | `Long` | `47.25` | 726,690.00 USD | 0.00 USD | 9,030.00 USD | `-15.30%` | `191.21` |
| `Live` | `Long` | `47.35` | 717,660.00 USD | 0.00 USD | 43,920.00 USD | `-15.12%` | `927.56` |
| `Live` | `Long` | `47.45` | 673,740.00 USD | 0.00 USD | 2,590.00 USD | `-14.94%` | `54.54` |
| `Live` | `Long` | `47.55` | 671,150.00 USD | 0.00 USD | 4,450.00 USD | `-14.76%` | `93.69` |
| `Live` | `Long` | `47.75` | 666,700.00 USD | 0.00 USD | 47,750.00 USD | `-14.40%` | `1,000.00` |
| `Live` | `Long` | `47.95` | 618,950.00 USD | 0.00 USD | 7,890.00 USD | `-14.04%` | `164.58` |
| `Live` | `Long` | `48.05` | 611,060.00 USD | 0.00 USD | 381.04 USD | `-13.87%` | `7.93` |
| `Live` | `Long` | `48.15` | 610,670.00 USD | 0.00 USD | 1,690.00 USD | `-13.69%` | `35.03` |
| `Live` | `Long` | `48.25` | 608,990.00 USD | 0.00 USD | 110.49 USD | `-13.51%` | `2.29` |
| `Live` | `Long` | `48.55` | 608,880.00 USD | 0.00 USD | 2,030.00 USD | `-12.97%` | `41.85` |
| `Live` | `Long` | `48.65` | 606,850.00 USD | 0.00 USD | 273.90 USD | `-12.79%` | `5.63` |
| `Live` | `Long` | `48.75` | 606,570.00 USD | 0.00 USD | 333.94 USD | `-12.61%` | `6.85` |
| `Live` | `Long` | `48.85` | 606,240.00 USD | 0.00 USD | 1,890.00 USD | `-12.43%` | `38.79` |
| `Live` | `Long` | `48.95` | 604,340.00 USD | 0.00 USD | 252.58 USD | `-12.25%` | `5.16` |
| `Live` | `Long` | `49.05` | 604,090.00 USD | 0.00 USD | 1,580.00 USD | `-12.07%` | `32.25` |
| `Live` | `Long` | `49.15` | 602,510.00 USD | 0.00 USD | 5,740.00 USD | `-11.89%` | `116.83` |
| `Live` | `Long` | `49.35` | 596,770.00 USD | 0.00 USD | 5,230.00 USD | `-11.54%` | `105.97` |
| `Live` | `Long` | `49.45` | 591,540.00 USD | 0.00 USD | 419.34 USD | `-11.36%` | `8.48` |
| `Live` | `Long` | `49.55` | 591,120.00 USD | 0.00 USD | 18,010.00 USD | `-11.18%` | `363.57` |
| `Live` | `Long` | `49.65` | 573,100.00 USD | 0.00 USD | 73,260.00 USD | `-11.00%` | `1,475.52` |
| `Live` | `Long` | `49.75` | 499,840.00 USD | 0.00 USD | 20,390.00 USD | `-10.82%` | `409.75` |
| `Live` | `Long` | `49.95` | 479,460.00 USD | 0.00 USD | 19,920.00 USD | `-10.46%` | `398.70` |
| `Live` | `Long` | `50.05` | 459,540.00 USD | 0.00 USD | 1,820.00 USD | `-10.28%` | `36.43` |
| `Live` | `Long` | `50.25` | 457,720.00 USD | 0.00 USD | 102.51 USD | `-9.92%` | `2.04` |
| `Live` | `Long` | `50.35` | 457,620.00 USD | 0.00 USD | 1,140.00 USD | `-9.74%` | `22.67` |
| `Live` | `Long` | `50.45` | 456,480.00 USD | 0.00 USD | 4,720.00 USD | `-9.56%` | `93.64` |
| `Live` | `Long` | `50.55` | 451,750.00 USD | 0.00 USD | 84,100.00 USD | `-9.38%` | `1,663.61` |
| `Live` | `Long` | `50.75` | 367,660.00 USD | 0.00 USD | 9,050.00 USD | `-9.03%` | `178.28` |
| `Live` | `Long` | `50.95` | 358,610.00 USD | 0.00 USD | 431.55 USD | `-8.67%` | `8.47` |
| `Live` | `Long` | `51.15` | 358,180.00 USD | 0.00 USD | 219,370.00 USD | `-8.31%` | `4,288.79` |
| `Live` | `Long` | `51.25` | 138,810.00 USD | 0.00 USD | 202.44 USD | `-8.13%` | `3.95` |
| `Live` | `Long` | `51.35` | 138,600.00 USD | 0.00 USD | 453.93 USD | `-7.95%` | `8.84` |
| `Live` | `Long` | `51.45` | 138,150.00 USD | 0.00 USD | 27,210.00 USD | `-7.77%` | `528.81` |
| `Live` | `Long` | `51.55` | 110,940.00 USD | 0.00 USD | 551.07 USD | `-7.59%` | `10.69` |
| `Live` | `Long` | `51.65` | 110,390.00 USD | 0.00 USD | 9,100.00 USD | `-7.41%` | `176.09` |
| `Live` | `Long` | `51.75` | 101,300.00 USD | 0.00 USD | 6,480.00 USD | `-7.23%` | `125.17` |
| `Live` | `Long` | `51.85` | 94,820.00 USD | 0.00 USD | 14,770.00 USD | `-7.05%` | `284.87` |
| `Live` | `Long` | `51.95` | 80,050.00 USD | 0.00 USD | 13,950.00 USD | `-6.87%` | `268.48` |
| `Live` | `Long` | `52.05` | 66,100.00 USD | 0.00 USD | 305.01 USD | `-6.70%` | `5.86` |
| `Live` | `Long` | `52.15` | 65,790.00 USD | 0.00 USD | 1,900.00 USD | `-6.52%` | `36.36` |
| `Live` | `Long` | `52.25` | 63,900.00 USD | 0.00 USD | 4,820.00 USD | `-6.34%` | `92.20` |
| `Live` | `Long` | `52.35` | 59,080.00 USD | 0.00 USD | 245.52 USD | `-6.16%` | `4.69` |
| `Live` | `Long` | `52.45` | 58,840.00 USD | 0.00 USD | 5,820.00 USD | `-5.98%` | `110.91` |
| `Live` | `Long` | `52.55` | 53,020.00 USD | 0.00 USD | 8,700.00 USD | `-5.80%` | `165.49` |
| `Live` | `Long` | `52.65` | 44,320.00 USD | 0.00 USD | 1,050.00 USD | `-5.62%` | `20.00` |
| `Live` | `Long` | `52.75` | 43,270.00 USD | 0.00 USD | 30,280.00 USD | `-5.44%` | `574.00` |
| `Live` | `Long` | `52.85` | 12,990.00 USD | 0.00 USD | 5,950.00 USD | `-5.26%` | `112.64` |
| `Live` | `Long` | `52.95` | 7,040.00 USD | 0.00 USD | 2,680.00 USD | `-5.08%` | `50.57` |
| `Live` | `Long` | `53.05` | 4,360.00 USD | 0.00 USD | 769.76 USD | `-4.90%` | `14.51` |
| `Live` | `Long` | `53.15` | 3,590.00 USD | 0.00 USD | 2,030.00 USD | `-4.72%` | `38.15` |
| `Live` | `Long` | `53.25` | 1,560.00 USD | 0.00 USD | 619.30 USD | `-4.54%` | `11.63` |
| `Live` | `Long` | `53.45` | 942.86 USD | 0.00 USD | 942.86 USD | `-4.19%` | `17.64` |
| `Live` | `Short` | `57.75` | 155.35 USD | 155.35 USD | 0.00 USD | `+3.52%` | `2.69` |
| `Live` | `Short` | `57.95` | 281.10 USD | 125.75 USD | 0.00 USD | `+3.88%` | `2.17` |
| `Live` | `Short` | `58.85` | 1,760.00 USD | 1,480.00 USD | 0.00 USD | `+5.49%` | `25.13` |
| `Live` | `Short` | `59.35` | 11,200.00 USD | 9,440.00 USD | 0.00 USD | `+6.39%` | `159.09` |
| `Live` | `Short` | `60.15` | 220,080.00 USD | 208,880.00 USD | 0.00 USD | `+7.82%` | `3,472.67` |
| `Live` | `Short` | `60.35` | 220,510.00 USD | 431.50 USD | 0.00 USD | `+8.18%` | `7.15` |
| `Live` | `Short` | `60.95` | 220,910.00 USD | 397.39 USD | 0.00 USD | `+9.26%` | `6.52` |
| `Live` | `Short` | `61.55` | 221,130.00 USD | 222.20 USD | 0.00 USD | `+10.33%` | `3.61` |
| `Live` | `Short` | `62.95` | 221,270.00 USD | 138.49 USD | 0.00 USD | `+12.84%` | `2.20` |
| `Live` | `Short` | `63.45` | 224,620.00 USD | 3,350.00 USD | 0.00 USD | `+13.74%` | `52.83` |
| `Live` | `Short` | `63.55` | 232,800.00 USD | 8,180.00 USD | 0.00 USD | `+13.92%` | `128.67` |
| `Live` | `Short` | `67.05` | 232,920.00 USD | 121.36 USD | 0.00 USD | `+20.19%` | `1.81` |
| `Live` | `Short` | `67.85` | 233,630.00 USD | 709.03 USD | 0.00 USD | `+21.63%` | `10.45` |
| `Live` | `Short` | `68.35` | 234,250.00 USD | 619.93 USD | 0.00 USD | `+22.52%` | `9.07` |
| `Live` | `Short` | `68.95` | 274,110.00 USD | 39,860.00 USD | 0.00 USD | `+23.60%` | `578.10` |
| `Live` | `Short` | `76.35` | 282,500.00 USD | 8,380.00 USD | 0.00 USD | `+36.86%` | `109.80` |
| `Live` | `Short` | `77.75` | 860,960.00 USD | 578,460.00 USD | 0.00 USD | `+39.37%` | `7,440.05` |
| `Live` | `Short` | `77.85` | 861,560.00 USD | 602.56 USD | 0.00 USD | `+39.55%` | `7.74` |
| `Live` | `Short` | `80.75` | 862,210.00 USD | 646.00 USD | 0.00 USD | `+44.75%` | `8.00` |
| `Live` | `Short` | `81.05` | 881,210.00 USD | 19,000.00 USD | 0.00 USD | `+45.29%` | `234.42` |
| `Live` | `Short` | `81.45` | 884,470.00 USD | 3,260.00 USD | 0.00 USD | `+46.01%` | `40.00` |
| `Live` | `Short` | `81.55` | 884,590.00 USD | 123.96 USD | 0.00 USD | `+46.19%` | `1.52` |
| `Live` | `Short` | `82.05` | 887,300.00 USD | 2,710.00 USD | 0.00 USD | `+47.08%` | `33.00` |
| `Live` | `Short` | `82.75` | 887,510.00 USD | 214.32 USD | 0.00 USD | `+48.34%` | `2.59` |
| `Live` | `Short` | `85.35` | 911,190.00 USD | 23,680.00 USD | 0.00 USD | `+53.00%` | `277.44` |
| `Live` | `Short` | `90.65` | 911,310.00 USD | 119.66 USD | 0.00 USD | `+62.50%` | `1.32` |
| `Live` | `Short` | `97.25` | 911,470.00 USD | 164.35 USD | 0.00 USD | `+74.33%` | `1.69` |
| `Live` | `Short` | `97.85` | 913,920.00 USD | 2,450.00 USD | 0.00 USD | `+75.41%` | `25.00` |
| `Live` | `Short` | `98.05` | 933,530.00 USD | 19,610.00 USD | 0.00 USD | `+75.76%` | `200.00` |
| `Live` | `Short` | `102.75` | 964,360.00 USD | 30,820.00 USD | 0.00 USD | `+84.19%` | `300.00` |
| `Live` | `Short` | `104.25` | 964,570.00 USD | 213.71 USD | 0.00 USD | `+86.88%` | `2.05` |
| `Live` | `Short` | `104.65` | 1,320,000.00 USD | 353,090.00 USD | 0.00 USD | `+87.60%` | `3,374.01` |
| `Live` | `Short` | `104.85` | 1,320,000.00 USD | 2,320.00 USD | 0.00 USD | `+87.95%` | `22.13` |
| `Live` | `Short` | `106.75` | 1,320,000.00 USD | 1,620.00 USD | 0.00 USD | `+91.36%` | `15.16` |
| `Live` | `Short` | `106.85` | 1,320,000.00 USD | 1,860.00 USD | 0.00 USD | `+91.54%` | `17.43` |
| `Live` | `Short` | `107.25` | 1,320,000.00 USD | 199.48 USD | 0.00 USD | `+92.26%` | `1.86` |
| `Live` | `Short` | `108.05` | 1,330,000.00 USD | 6,470.00 USD | 0.00 USD | `+93.69%` | `59.91` |
| `Live` | `Short` | `110.35` | 1,330,000.00 USD | 753.69 USD | 0.00 USD | `+97.81%` | `6.83` |
| `Live` | `Short` | `110.95` | 1,330,000.00 USD | 664.59 USD | 0.00 USD | `+98.89%` | `5.99` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 842,810.00 USD | 0.00 USD | 392.18 USD | `-64.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 842,420.00 USD | 0.00 USD | 2,310.00 USD | `-60.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 840,110.00 USD | 0.00 USD | 806.86 USD | `-55.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 839,300.00 USD | 0.00 USD | 1,560.00 USD | `-54.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 837,750.00 USD | 0.00 USD | 410.25 USD | `-50.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 837,340.00 USD | 0.00 USD | 281.57 USD | `-46.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 837,050.00 USD | 0.00 USD | 36,050.00 USD | `-35.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 801,000.00 USD | 0.00 USD | 37,550.00 USD | `-32.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 763,450.00 USD | 0.00 USD | 447.01 USD | `-32.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.35` | 763,010.00 USD | 0.00 USD | 73,350.00 USD | `-31.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 689,660.00 USD | 0.00 USD | 40,560.00 USD | `-30.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 649,100.00 USD | 0.00 USD | 489.57 USD | `-29.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 648,610.00 USD | 0.00 USD | 1,180.00 USD | `-28.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 647,430.00 USD | 0.00 USD | 9,840.00 USD | `-28.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 637,590.00 USD | 0.00 USD | 2,060.00 USD | `-26.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.05` | 635,540.00 USD | 0.00 USD | 2,060.00 USD | `-26.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 633,480.00 USD | 0.00 USD | 2,960.00 USD | `-25.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 630,520.00 USD | 0.00 USD | 4,010.00 USD | `-24.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.65` | 626,510.00 USD | 0.00 USD | 3,000.00 USD | `-23.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 623,510.00 USD | 0.00 USD | 5,680.00 USD | `-22.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 617,830.00 USD | 0.00 USD | 672.22 USD | `-21.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.35` | 617,150.00 USD | 0.00 USD | 329,970.00 USD | `-20.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 287,190.00 USD | 0.00 USD | 569.85 USD | `-20.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 286,620.00 USD | 0.00 USD | 223.20 USD | `-20.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 286,390.00 USD | 0.00 USD | 391.13 USD | `-19.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 286,000.00 USD | 0.00 USD | 7,080.00 USD | `-19.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 278,930.00 USD | 0.00 USD | 1,370.00 USD | `-18.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 277,560.00 USD | 0.00 USD | 553.80 USD | `-17.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.35` | 277,010.00 USD | 0.00 USD | 2,970.00 USD | `-16.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.45` | 274,040.00 USD | 0.00 USD | 3,080.00 USD | `-16.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 270,960.00 USD | 0.00 USD | 14,000.00 USD | `-16.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 256,960.00 USD | 0.00 USD | 158.56 USD | `-15.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 256,800.00 USD | 0.00 USD | 373.28 USD | `-15.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 256,430.00 USD | 0.00 USD | 849.46 USD | `-15.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 255,580.00 USD | 0.00 USD | 1,150.00 USD | `-14.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 254,430.00 USD | 0.00 USD | 129.25 USD | `-13.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.15` | 254,300.00 USD | 0.00 USD | 303.35 USD | `-13.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 254,000.00 USD | 0.00 USD | 1,740.00 USD | `-12.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 252,260.00 USD | 0.00 USD | 981.00 USD | `-12.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.35` | 251,280.00 USD | 0.00 USD | 817.24 USD | `-11.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 250,460.00 USD | 0.00 USD | 237.85 USD | `-11.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.55` | 250,220.00 USD | 0.00 USD | 879.51 USD | `-11.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.85` | 249,340.00 USD | 0.00 USD | 108.17 USD | `-10.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 249,230.00 USD | 0.00 USD | 298.20 USD | `-10.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 248,940.00 USD | 0.00 USD | 34,670.00 USD | `-10.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 214,260.00 USD | 0.00 USD | 6,410.00 USD | `-10.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 207,850.00 USD | 0.00 USD | 459.70 USD | `-9.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 207,390.00 USD | 0.00 USD | 236.57 USD | `-9.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 207,150.00 USD | 0.00 USD | 1,020.00 USD | `-8.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 206,130.00 USD | 0.00 USD | 439.89 USD | `-8.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.45` | 205,690.00 USD | 0.00 USD | 204.26 USD | `-7.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 205,490.00 USD | 0.00 USD | 11,560.00 USD | `-7.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.85` | 193,930.00 USD | 0.00 USD | 106.29 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.95` | 193,820.00 USD | 0.00 USD | 8,700.00 USD | `-6.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 185,120.00 USD | 0.00 USD | 27,140.00 USD | `-6.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.25` | 157,980.00 USD | 0.00 USD | 140.03 USD | `-6.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 157,840.00 USD | 0.00 USD | 18,390.00 USD | `-5.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 139,450.00 USD | 0.00 USD | 5,460.00 USD | `-5.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 133,990.00 USD | 0.00 USD | 271.13 USD | `-5.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.85` | 133,720.00 USD | 0.00 USD | 2,840.00 USD | `-5.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 130,880.00 USD | 0.00 USD | 115.43 USD | `-5.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 130,760.00 USD | 0.00 USD | 9,240.00 USD | `-4.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 121,520.00 USD | 0.00 USD | 2,660.00 USD | `-4.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.25` | 118,860.00 USD | 0.00 USD | 881.82 USD | `-4.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.35` | 117,980.00 USD | 0.00 USD | 25,130.00 USD | `-4.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 92,850.00 USD | 0.00 USD | 566.57 USD | `-4.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 92,280.00 USD | 0.00 USD | 5,950.00 USD | `-4.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 86,340.00 USD | 0.00 USD | 1,370.00 USD | `-3.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.75` | 84,970.00 USD | 0.00 USD | 52,980.00 USD | `-3.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 31,980.00 USD | 0.00 USD | 462.03 USD | `-3.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 31,520.00 USD | 0.00 USD | 6,010.00 USD | `-3.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.15` | 25,510.00 USD | 0.00 USD | 398.54 USD | `-2.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 25,110.00 USD | 0.00 USD | 3,090.00 USD | `-2.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 22,030.00 USD | 0.00 USD | 958.73 USD | `-2.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.45` | 21,070.00 USD | 0.00 USD | 144.29 USD | `-2.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.55` | 20,920.00 USD | 0.00 USD | 788.25 USD | `-2.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.65` | 20,130.00 USD | 0.00 USD | 13,660.00 USD | `-2.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.75` | 6,470.00 USD | 0.00 USD | 198.74 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 6,270.00 USD | 0.00 USD | 398.21 USD | `-1.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.95` | 5,870.00 USD | 0.00 USD | 909.97 USD | `-1.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 4,960.00 USD | 0.00 USD | 550.50 USD | `-1.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.15` | 4,410.00 USD | 0.00 USD | 596.17 USD | `-1.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.25` | 3,820.00 USD | 0.00 USD | 1,310.00 USD | `-0.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.35` | 2,500.00 USD | 0.00 USD | 198.71 USD | `-0.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.45` | 2,310.00 USD | 0.00 USD | 1,190.00 USD | `-0.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.55` | 1,110.00 USD | 0.00 USD | 156.65 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.65` | 954.56 USD | 0.00 USD | 556.50 USD | `-0.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.75` | 398.06 USD | 0.00 USD | 398.06 USD | `-0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.85` | 797.54 USD | 797.54 USD | 0.00 USD | `+0.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.95` | 990.57 USD | 193.03 USD | 0.00 USD | `+0.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.05` | 1,620.00 USD | 632.24 USD | 0.00 USD | `+0.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.15` | 1,820.00 USD | 197.65 USD | 0.00 USD | `+0.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.25` | 2,020.00 USD | 204.19 USD | 0.00 USD | `+0.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.35` | 2,430.00 USD | 406.85 USD | 0.00 USD | `+1.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.45` | 2,840.00 USD | 407.57 USD | 0.00 USD | `+1.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.55` | 3,040.00 USD | 204.15 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.65` | 3,570.00 USD | 529.11 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.75` | 3,780.00 USD | 203.73 USD | 0.00 USD | `+1.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.85` | 3,980.00 USD | 204.09 USD | 0.00 USD | `+1.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.95` | 4,750.00 USD | 765.41 USD | 0.00 USD | `+2.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.05` | 5,340.00 USD | 596.17 USD | 0.00 USD | `+2.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.15` | 5,550.00 USD | 204.03 USD | 0.00 USD | `+2.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.25` | 6,980.00 USD | 1,440.00 USD | 0.00 USD | `+2.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.35` | 7,190.00 USD | 207.03 USD | 0.00 USD | `+2.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.45` | 7,540.00 USD | 344.70 USD | 0.00 USD | `+2.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.55` | 7,750.00 USD | 218.69 USD | 0.00 USD | `+3.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.65` | 7,870.00 USD | 118.18 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.75` | 7,990.00 USD | 119.54 USD | 0.00 USD | `+3.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 8,740.00 USD | 747.68 USD | 0.00 USD | `+4.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 8,940.00 USD | 200.04 USD | 0.00 USD | `+4.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 9,140.00 USD | 200.96 USD | 0.00 USD | `+4.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 9,260.00 USD | 123.70 USD | 0.00 USD | `+4.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 9,870.00 USD | 601.45 USD | 0.00 USD | `+4.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 10,090.00 USD | 223.66 USD | 0.00 USD | `+4.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 10,580.00 USD | 491.15 USD | 0.00 USD | `+5.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 13,520.00 USD | 2,940.00 USD | 0.00 USD | `+5.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 13,650.00 USD | 129.69 USD | 0.00 USD | `+5.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 18,450.00 USD | 4,800.00 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 19,730.00 USD | 1,280.00 USD | 0.00 USD | `+6.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.25` | 19,940.00 USD | 210.34 USD | 0.00 USD | `+6.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 20,400.00 USD | 461.74 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 20,560.00 USD | 159.92 USD | 0.00 USD | `+6.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 21,290.00 USD | 724.75 USD | 0.00 USD | `+6.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 21,450.00 USD | 158.00 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 21,620.00 USD | 171.14 USD | 0.00 USD | `+7.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 22,170.00 USD | 551.00 USD | 0.00 USD | `+8.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.45` | 22,320.00 USD | 155.36 USD | 0.00 USD | `+8.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 23,200.00 USD | 878.58 USD | 0.00 USD | `+8.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 24,590.00 USD | 1,390.00 USD | 0.00 USD | `+8.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 25,580.00 USD | 986.99 USD | 0.00 USD | `+9.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 26,250.00 USD | 674.72 USD | 0.00 USD | `+9.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 28,610.00 USD | 2,360.00 USD | 0.00 USD | `+9.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 28,740.00 USD | 125.56 USD | 0.00 USD | `+9.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 32,340.00 USD | 3,600.00 USD | 0.00 USD | `+10.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 32,980.00 USD | 643.20 USD | 0.00 USD | `+10.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 33,110.00 USD | 130.31 USD | 0.00 USD | `+11.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.35` | 34,210.00 USD | 1,100.00 USD | 0.00 USD | `+11.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.55` | 35,460.00 USD | 1,250.00 USD | 0.00 USD | `+12.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 36,180.00 USD | 716.72 USD | 0.00 USD | `+12.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 36,410.00 USD | 231.39 USD | 0.00 USD | `+13.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 37,040.00 USD | 630.87 USD | 0.00 USD | `+13.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 37,740.00 USD | 703.97 USD | 0.00 USD | `+13.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 38,410.00 USD | 668.13 USD | 0.00 USD | `+13.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 48,830.00 USD | 10,420.00 USD | 0.00 USD | `+13.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 49,390.00 USD | 555.03 USD | 0.00 USD | `+14.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 49,920.00 USD | 531.62 USD | 0.00 USD | `+14.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.35` | 50,580.00 USD | 664.09 USD | 0.00 USD | `+15.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.45` | 51,250.00 USD | 665.12 USD | 0.00 USD | `+15.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 51,450.00 USD | 202.69 USD | 0.00 USD | `+15.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 51,750.00 USD | 298.04 USD | 0.00 USD | `+15.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 51,850.00 USD | 102.13 USD | 0.00 USD | `+16.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 52,390.00 USD | 540.09 USD | 0.00 USD | `+16.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 52,490.00 USD | 100.79 USD | 0.00 USD | `+17.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 52,750.00 USD | 262.20 USD | 0.00 USD | `+17.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 53,130.00 USD | 371.49 USD | 0.00 USD | `+17.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 53,820.00 USD | 696.17 USD | 0.00 USD | `+18.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 54,360.00 USD | 534.00 USD | 0.00 USD | `+19.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 65,440.00 USD | 11,080.00 USD | 0.00 USD | `+20.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 72,140.00 USD | 6,710.00 USD | 0.00 USD | `+20.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.05` | 74,500.00 USD | 2,360.00 USD | 0.00 USD | `+21.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 79,360.00 USD | 4,860.00 USD | 0.00 USD | `+22.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 79,570.00 USD | 204.48 USD | 0.00 USD | `+24.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.65` | 597,770.00 USD | 518,200.00 USD | 0.00 USD | `+24.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 598,580.00 USD | 810.02 USD | 0.00 USD | `+25.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 918,470.00 USD | 319,890.00 USD | 0.00 USD | `+25.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 918,640.00 USD | 170.04 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 924,410.00 USD | 5,770.00 USD | 0.00 USD | `+27.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 924,680.00 USD | 269.28 USD | 0.00 USD | `+27.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 924,970.00 USD | 291.40 USD | 0.00 USD | `+28.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 932,190.00 USD | 7,220.00 USD | 0.00 USD | `+29.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 932,340.00 USD | 156.78 USD | 0.00 USD | `+29.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 935,560.00 USD | 3,220.00 USD | 0.00 USD | `+30.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 935,980.00 USD | 411.14 USD | 0.00 USD | `+31.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 1,060,000.00 USD | 123,190.00 USD | 0.00 USD | `+32.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 1,060,000.00 USD | 1,020.00 USD | 0.00 USD | `+33.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.75` | 1,060,000.00 USD | 811.04 USD | 0.00 USD | `+34.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 1,060,000.00 USD | 104.93 USD | 0.00 USD | `+34.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 1,060,000.00 USD | 133.59 USD | 0.00 USD | `+34.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 1,060,000.00 USD | 402.59 USD | 0.00 USD | `+34.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.85` | 1,060,000.00 USD | 308.71 USD | 0.00 USD | `+35.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 1,060,000.00 USD | 315.18 USD | 0.00 USD | `+38.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 1,120,000.00 USD | 59,310.00 USD | 0.00 USD | `+40.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 1,120,000.00 USD | 3,160.00 USD | 0.00 USD | `+41.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.35` | 1,130,000.00 USD | 5,260.00 USD | 0.00 USD | `+42.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 1,140,000.00 USD | 5,690.00 USD | 0.00 USD | `+42.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 1,170,000.00 USD | 36,590.00 USD | 0.00 USD | `+43.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 1,170,000.00 USD | 433.89 USD | 0.00 USD | `+45.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 1,170,000.00 USD | 172.64 USD | 0.00 USD | `+45.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 1,170,000.00 USD | 164.10 USD | 0.00 USD | `+47.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 1,170,000.00 USD | 546.81 USD | 0.00 USD | `+48.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 1,180,000.00 USD | 2,300.00 USD | 0.00 USD | `+50.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 1,190,000.00 USD | 12,070.00 USD | 0.00 USD | `+52.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.05` | 1,210,000.00 USD | 20,230.00 USD | 0.00 USD | `+56.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 1,210,000.00 USD | 1,580.00 USD | 0.00 USD | `+57.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 1,250,000.00 USD | 37,000.00 USD | 0.00 USD | `+57.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 1,250,000.00 USD | 473.21 USD | 0.00 USD | `+59.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 1,250,000.00 USD | 422.99 USD | 0.00 USD | `+59.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 1,250,000.00 USD | 1,630.00 USD | 0.00 USD | `+60.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 1,250,000.00 USD | 4,870.00 USD | 0.00 USD | `+61.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 1,250,000.00 USD | 481.55 USD | 0.00 USD | `+64.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 1,260,000.00 USD | 1,330.00 USD | 0.00 USD | `+65.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 1,260,000.00 USD | 281.21 USD | 0.00 USD | `+68.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,520,000.00 USD | 266,140.00 USD | 0.00 USD | `+70.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,530,000.00 USD | 3,400.00 USD | 0.00 USD | `+70.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,550,000.00 USD | 21,930.00 USD | 0.00 USD | `+72.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,550,000.00 USD | 294.15 USD | 0.00 USD | `+75.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 1,560,000.00 USD | 15,380.00 USD | 0.00 USD | `+77.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,570,000.00 USD | 3,660.00 USD | 0.00 USD | `+79.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,570,000.00 USD | 306.15 USD | 0.00 USD | `+82.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,570,000.00 USD | 936.72 USD | 0.00 USD | `+84.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,570,000.00 USD | 2,920.00 USD | 0.00 USD | `+84.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,570,000.00 USD | 324.15 USD | 0.00 USD | `+93.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 1,570,000.00 USD | 123.23 USD | 0.00 USD | `+95.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 1,660,000.00 USD | 89,110.00 USD | 0.00 USD | `+99.07%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `48.10` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD |
| `7D` | `48.20` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD |
| `7D` | `48.40` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 0.00 USD | 6,080.00 USD | 0.00 USD |
| `7D` | `48.60` | 8,290,000.00 USD | 0.00 USD | 8,290,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `48.80` | 8,290,000.00 USD | 0.00 USD | 8,290,000.00 USD | 1,780.00 USD | 2,250.00 USD | 0.00 USD |
| `7D` | `48.90` | 8,280,000.00 USD | 0.00 USD | 8,280,000.00 USD | 0.00 USD | 0.00 USD | 960.40 USD |
| `7D` | `49.30` | 8,280,000.00 USD | 0.00 USD | 8,280,000.00 USD | 15,190.00 USD | 4,490.00 USD | 14,870.00 USD |
| `7D` | `49.40` | 8,250,000.00 USD | 0.00 USD | 8,250,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD |
| `7D` | `49.50` | 8,240,000.00 USD | 0.00 USD | 8,240,000.00 USD | 2,830.00 USD | 7,770.00 USD | 0.00 USD |
| `1D` | `49.60` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 5,570.00 USD | 14,890.00 USD | 16,210.00 USD |
| `7D` | `49.60` | 8,230,000.00 USD | 0.00 USD | 8,230,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD |
| `1D` | `49.70` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 12,650.00 USD | 3,970.00 USD | 8,070.00 USD |
| `7D` | `49.70` | 8,220,000.00 USD | 0.00 USD | 8,220,000.00 USD | 12,090.00 USD | 0.00 USD | 13,440.00 USD |
| `1D` | `49.80` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 6,420.00 USD | 11,200.00 USD | 23,300.00 USD |
| `7D` | `49.80` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 9,930.00 USD | 8,220.00 USD | 0.00 USD |
| `1D` | `49.90` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 24,520.00 USD | 18,280.00 USD | 24,800.00 USD |
| `7D` | `49.90` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 45,030.00 USD | 19,460.00 USD | 4,700.00 USD |
| `1D` | `50.00` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 21,740.00 USD | 24,020.00 USD | 44,940.00 USD |
| `7D` | `50.00` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 29,070.00 USD | 26,820.00 USD | 25,110.00 USD |
| `1D` | `50.10` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 7,310.00 USD | 6,650.00 USD | 7,600.00 USD |
| `7D` | `50.10` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 363.50 USD | 682.90 USD | 8,340.00 USD |
| `1D` | `50.20` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 177.10 USD | 709.61 USD | 5,230.00 USD |
| `7D` | `50.20` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 6,960.00 USD | 500.40 USD | 42,940.00 USD |
| `1D` | `50.30` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 171.03 USD | 3,880.00 USD | 2,500.00 USD |
| `7D` | `50.30` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 16,270.00 USD | 10,780.00 USD | 7,240.00 USD |
| `1D` | `50.40` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 8,260.00 USD | 11,890.00 USD | 1,150.00 USD |
| `7D` | `50.40` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 28,280.00 USD | 26,580.00 USD | 33,450.00 USD |
| `1D` | `50.50` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 8,910.00 USD | 8,790.00 USD | 10,530.00 USD |
| `7D` | `50.50` | 7,840,000.00 USD | 0.00 USD | 7,840,000.00 USD | 32,490.00 USD | 6,790.00 USD | 44,380.00 USD |
| `1D` | `50.60` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 7,330.00 USD | 3,440.00 USD | 10,850.00 USD |
| `7D` | `50.60` | 7,760,000.00 USD | 0.00 USD | 7,760,000.00 USD | 67,580.00 USD | 21,530.00 USD | 31,730.00 USD |
| `1D` | `50.70` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 8,170.00 USD | 2,300.00 USD | 11,770.00 USD |
| `7D` | `50.70` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 65,920.00 USD | 32,820.00 USD | 41,580.00 USD |
| `1D` | `50.80` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 12,550.00 USD | 3,100.00 USD | 8,280.00 USD |
| `7D` | `50.80` | 7,490,000.00 USD | 0.00 USD | 7,490,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD |
| `1D` | `50.90` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 826.24 USD | 260.05 USD | 8,390.00 USD |
| `7D` | `50.90` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD |
| `1D` | `51.00` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 5,040.00 USD | 0.00 USD | 430.77 USD |
| `7D` | `51.00` | 7,140,000.00 USD | 0.00 USD | 7,140,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `51.10` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 9,210.00 USD | 6,650.00 USD | 0.00 USD |
| `7D` | `51.10` | 7,020,000.00 USD | 0.00 USD | 7,020,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD |
| `1D` | `51.20` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 1,770.00 USD | 1,130.00 USD | 19,220.00 USD |
| `7D` | `51.20` | 6,940,000.00 USD | 0.00 USD | 6,940,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD |
| `1D` | `51.30` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 8,650.00 USD | 9,710.00 USD | 0.00 USD |
| `7D` | `51.30` | 6,870,000.00 USD | 0.00 USD | 6,870,000.00 USD | 28,400.00 USD | 26,720.00 USD | 47,090.00 USD |
| `1D` | `51.40` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 3,250.00 USD | 5,460.00 USD | 416.23 USD |
| `7D` | `51.40` | 6,770,000.00 USD | 0.00 USD | 6,770,000.00 USD | 73,130.00 USD | 42,820.00 USD | 46,140.00 USD |
| `1D` | `51.50` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 7,580.00 USD | 10,010.00 USD | 41,580.00 USD |
| `7D` | `51.50` | 6,610,000.00 USD | 0.00 USD | 6,610,000.00 USD | 38,520.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `51.60` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 5,990.00 USD | 17,860.00 USD | 709.44 USD |
| `7D` | `51.60` | 6,510,000.00 USD | 0.00 USD | 6,510,000.00 USD | 37,880.00 USD | 36,790.00 USD | 41,490.00 USD |
| `1D` | `51.70` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 2,660.00 USD | 12,840.00 USD | 44.86 USD |
| `7D` | `51.70` | 6,390,000.00 USD | 0.00 USD | 6,390,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `51.80` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 10,010.00 USD | 18,760.00 USD | 12,840.00 USD |
| `7D` | `51.80` | 6,360,000.00 USD | 0.00 USD | 6,360,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD |
| `1D` | `51.90` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 10,800.00 USD | 19,770.00 USD | 21,410.00 USD |
| `7D` | `51.90` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 5,870.00 USD | 25,410.00 USD | 28,190.00 USD |
| `1D` | `52.00` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 20,190.00 USD | 25,620.00 USD | 16,900.00 USD |
| `7D` | `52.00` | 6,240,000.00 USD | 0.00 USD | 6,240,000.00 USD | 65,840.00 USD | 26,440.00 USD | 11,880.00 USD |
| `1D` | `52.10` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 34,790.00 USD | 17,300.00 USD | 44,970.00 USD |
| `7D` | `52.10` | 6,140,000.00 USD | 0.00 USD | 6,140,000.00 USD | 24,220.00 USD | 28,090.00 USD | 37,880.00 USD |
| `1D` | `52.20` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 13,190.00 USD | 5,050.00 USD | 49,960.00 USD |
| `7D` | `52.20` | 6,050,000.00 USD | 0.00 USD | 6,050,000.00 USD | 38,380.00 USD | 13,960.00 USD | 25,270.00 USD |
| `1D` | `52.30` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 26,510.00 USD | 22,090.00 USD | 11,210.00 USD |
| `7D` | `52.30` | 5,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 26,450.00 USD | 40,700.00 USD | 7,980.00 USD |
| `1D` | `52.40` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 15,630.00 USD | 15,400.00 USD | 7,040.00 USD |
| `7D` | `52.40` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 20,580.00 USD | 38,950.00 USD | 19,520.00 USD |
| `1D` | `52.50` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 53,990.00 USD | 30,000.00 USD | 79,400.00 USD |
| `7D` | `52.50` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 38,650.00 USD | 0.00 USD | 11,240.00 USD |
| `1D` | `52.60` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 9,060.00 USD | 43,700.00 USD | 5,450.00 USD |
| `7D` | `52.60` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 60,960.00 USD | 31,860.00 USD | 59,410.00 USD |
| `1D` | `52.70` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 18,270.00 USD | 19,780.00 USD | 40,000.00 USD |
| `7D` | `52.70` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 19,550.00 USD | 75,910.00 USD | 108,640.00 USD |
| `1D` | `52.80` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 28,880.00 USD | 50,850.00 USD | 72,920.00 USD |
| `7D` | `52.80` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 30,590.00 USD | 25,700.00 USD | 0.00 USD |
| `1D` | `52.90` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 44,710.00 USD | 55,550.00 USD | 30,100.00 USD |
| `7D` | `52.90` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 30,900.00 USD | 11,650.00 USD | 34,400.00 USD |
| `1D` | `53.00` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 31,870.00 USD | 34,720.00 USD | 52,280.00 USD |
| `7D` | `53.00` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 39,690.00 USD | 25,380.00 USD | 97,750.00 USD |
| `1D` | `53.10` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 12,590.00 USD | 63,920.00 USD | 88,790.00 USD |
| `7D` | `53.10` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 45,320.00 USD | 20,560.00 USD | 0.00 USD |
| `1D` | `53.20` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 36,030.00 USD | 34,380.00 USD | 46,970.00 USD |
| `7D` | `53.20` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 162,460.00 USD | 64,060.00 USD | 23,350.00 USD |
| `1D` | `53.30` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 28,400.00 USD | 37,270.00 USD | 16,210.00 USD |
| `7D` | `53.30` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 59,390.00 USD | 57,120.00 USD | 35,550.00 USD |
| `1D` | `53.40` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 12,600.00 USD | 19,860.00 USD | 8,290.00 USD |
| `7D` | `53.40` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 61,460.00 USD | 31,500.00 USD | 99,790.00 USD |
| `1D` | `53.50` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 21,250.00 USD | 15,340.00 USD | 22,000.00 USD |
| `7D` | `53.50` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 60,260.00 USD | 7,980.00 USD | 28,500.00 USD |
| `1D` | `53.60` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 75,950.00 USD | 3,830.00 USD | 20,970.00 USD |
| `7D` | `53.60` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 52,800.00 USD | 3,780.00 USD | 20,660.00 USD |
| `1D` | `53.70` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 6,210.00 USD | 11,100.00 USD | 11,960.00 USD |
| `7D` | `53.70` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 131,400.00 USD | 21,330.00 USD | 13,220.00 USD |
| `1D` | `53.80` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 53,640.00 USD | 28,920.00 USD | 4,830.00 USD |
| `7D` | `53.80` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 99,150.00 USD | 43,900.00 USD | 302.55 USD |
| `1D` | `53.90` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 50,300.00 USD | 39,560.00 USD | 27,830.00 USD |
| `7D` | `53.90` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 160,820.00 USD | 22,780.00 USD | 9,680.00 USD |
| `1D` | `54.00` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 76,010.00 USD | 30,780.00 USD | 86,580.00 USD |
| `7D` | `54.00` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 380,340.00 USD | 71,820.00 USD | 304,530.00 USD |
| `1D` | `54.10` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 105,010.00 USD | 27,610.00 USD | 74,530.00 USD |
| `7D` | `54.10` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 302,190.00 USD | 5,360.00 USD | 42,710.00 USD |
| `1D` | `54.20` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 72,600.00 USD | 57,270.00 USD | 47,360.00 USD |
| `7D` | `54.20` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 205,060.00 USD | 5,200.00 USD | 0.00 USD |
| `1D` | `54.30` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 46,340.00 USD | 55,750.00 USD | 15,190.00 USD |
| `7D` | `54.30` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 381,380.00 USD | 71,490.00 USD | 181,420.00 USD |
| `1D` | `54.40` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 102,880.00 USD | 110,050.00 USD | 24,330.00 USD |
| `7D` | `54.40` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 304,270.00 USD | 78,990.00 USD | 93,590.00 USD |
| `1D` | `54.50` | 968,710.00 USD | 0.00 USD | 968,710.00 USD | 24,100.00 USD | 82,700.00 USD | 16,580.00 USD |
| `7D` | `54.50` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 194,580.00 USD | 63,740.00 USD | 257,020.00 USD |
| `1D` | `54.60` | 845,330.00 USD | 0.00 USD | 845,330.00 USD | 25,070.00 USD | 44,770.00 USD | 43,580.00 USD |
| `7D` | `54.60` | 831,250.00 USD | 0.00 USD | 831,250.00 USD | 18,530.00 USD | 11,000.00 USD | 131,380.00 USD |
| `1D` | `54.70` | 731,900.00 USD | 0.00 USD | 731,900.00 USD | 6,600.00 USD | 23,060.00 USD | 105,800.00 USD |
| `7D` | `54.70` | 670,350.00 USD | 0.00 USD | 670,350.00 USD | 0.00 USD | 3,600.00 USD | 41,310.00 USD |
| `1D` | `54.80` | 596,440.00 USD | 0.00 USD | 596,440.00 USD | 0.00 USD | 48,420.00 USD | 23,920.00 USD |
| `7D` | `54.80` | 625,440.00 USD | 0.00 USD | 625,440.00 USD | 0.00 USD | 35,700.00 USD | 26,440.00 USD |
| `1D` | `54.90` | 524,100.00 USD | 0.00 USD | 524,100.00 USD | 66,900.00 USD | 65,440.00 USD | 10,850.00 USD |
| `7D` | `54.90` | 563,300.00 USD | 0.00 USD | 563,300.00 USD | 0.00 USD | 112,280.00 USD | 48,290.00 USD |
| `1D` | `55.00` | 380,920.00 USD | 0.00 USD | 380,920.00 USD | 40,710.00 USD | 54,150.00 USD | 55,190.00 USD |
| `7D` | `55.00` | 402,720.00 USD | 0.00 USD | 402,720.00 USD | 97,700.00 USD | 2,830.00 USD | 19,360.00 USD |
| `1D` | `55.10` | 230,860.00 USD | 0.00 USD | 230,860.00 USD | 50,530.00 USD | 0.00 USD | 80,200.00 USD |
| `7D` | `55.10` | 282,840.00 USD | 0.00 USD | 282,840.00 USD | 54,590.00 USD | 18,510.00 USD | 64,690.00 USD |
| `1D` | `55.20` | 100,140.00 USD | 0.00 USD | 100,140.00 USD | 39,390.00 USD | 7,890.00 USD | 0.00 USD |
| `7D` | `55.20` | 145,060.00 USD | 0.00 USD | 145,060.00 USD | 57,400.00 USD | 59,710.00 USD | 0.00 USD |
| `1D` | `55.30` | 52,860.00 USD | 0.00 USD | 52,860.00 USD | 52,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.30` | 27,940.00 USD | 0.00 USD | 27,940.00 USD | 23,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.40` | 4,800.00 USD | 0.00 USD | 4,800.00 USD | 0.00 USD | 0.00 USD | 4,800.00 USD |
| `1D` | `55.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `55.70` | 613.46 USD | 613.46 USD | 0.00 USD | 0.00 USD | 0.00 USD | 613.46 USD |
| `7D` | `55.70` | 174,240.00 USD | 174,240.00 USD | 0.00 USD | 174,240.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.70` | 348,480.00 USD | 348,480.00 USD | 0.00 USD | 174,240.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `55.80` | 3,790.00 USD | 3,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,170.00 USD |
| `7D` | `55.80` | 439,450.00 USD | 439,450.00 USD | 0.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD |
| `1D` | `55.90` | 56,850.00 USD | 56,850.00 USD | 0.00 USD | 51,520.00 USD | 0.00 USD | 1,550.00 USD |
| `7D` | `55.90` | 580,780.00 USD | 580,780.00 USD | 0.00 USD | 141,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `56.00` | 61,230.00 USD | 61,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,380.00 USD |
| `7D` | `56.00` | 751,900.00 USD | 751,900.00 USD | 0.00 USD | 2,590.00 USD | 0.00 USD | 168,520.00 USD |
| `1D` | `56.20` | 70,570.00 USD | 70,570.00 USD | 0.00 USD | 0.00 USD | 9,340.00 USD | 0.00 USD |
| `7D` | `56.20` | 831,840.00 USD | 831,840.00 USD | 0.00 USD | 0.00 USD | 79,940.00 USD | 0.00 USD |
| `1D` | `56.30` | 118,460.00 USD | 118,460.00 USD | 0.00 USD | 10,140.00 USD | 8,440.00 USD | 29,310.00 USD |
| `7D` | `56.30` | 879,910.00 USD | 879,910.00 USD | 0.00 USD | 0.00 USD | 5,360.00 USD | 42,710.00 USD |
| `1D` | `56.40` | 191,530.00 USD | 191,530.00 USD | 0.00 USD | 5,040.00 USD | 58,450.00 USD | 9,570.00 USD |
| `7D` | `56.40` | 898,800.00 USD | 898,800.00 USD | 0.00 USD | 2,650.00 USD | 16,240.00 USD | 0.00 USD |
| `1D` | `56.50` | 671,750.00 USD | 671,750.00 USD | 0.00 USD | 169,280.00 USD | 156,300.00 USD | 154,640.00 USD |
| `7D` | `56.50` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 170,750.00 USD | 214,910.00 USD | 6,150.00 USD |
| `1D` | `56.60` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 101,920.00 USD | 173,560.00 USD | 102,110.00 USD |
| `7D` | `56.60` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 363,190.00 USD | 201,730.00 USD | 1,460.00 USD |
| `1D` | `56.70` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 110,240.00 USD | 63,740.00 USD | 295,600.00 USD |
| `7D` | `56.70` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 152,150.00 USD | 169,990.00 USD | 116,090.00 USD |
| `1D` | `56.80` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 128,400.00 USD | 40,070.00 USD | 106,140.00 USD |
| `7D` | `56.80` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 172,110.00 USD | 101,840.00 USD | 318,330.00 USD |
| `1D` | `56.90` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 45,140.00 USD | 17,930.00 USD | 35,720.00 USD |
| `7D` | `56.90` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 113,780.00 USD | 52,200.00 USD | 307,930.00 USD |
| `1D` | `57.00` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 6,480.00 USD | 43,030.00 USD | 29,740.00 USD |
| `7D` | `57.00` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 88,680.00 USD | 56,390.00 USD | 178,370.00 USD |
| `1D` | `57.10` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 77,000.00 USD | 77,400.00 USD | 46,610.00 USD |
| `7D` | `57.10` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 36,580.00 USD | 79,290.00 USD | 21,040.00 USD |
| `1D` | `57.20` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 53,080.00 USD | 78,490.00 USD | 120,900.00 USD |
| `7D` | `57.20` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 118,850.00 USD | 23,920.00 USD | 23,060.00 USD |
| `1D` | `57.30` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 70,930.00 USD | 49,300.00 USD | 87,180.00 USD |
| `7D` | `57.30` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 76,940.00 USD | 28,570.00 USD | 98,930.00 USD |
| `1D` | `57.40` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 90,030.00 USD | 53,690.00 USD | 91,080.00 USD |
| `7D` | `57.40` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 124,180.00 USD | 74,860.00 USD | 277,080.00 USD |
| `1D` | `57.50` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 197,830.00 USD | 69,230.00 USD | 178,360.00 USD |
| `7D` | `57.50` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 99,810.00 USD | 34,430.00 USD | 0.00 USD |
| `1D` | `57.60` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 85,090.00 USD | 51,920.00 USD | 67,430.00 USD |
| `7D` | `57.60` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 149,560.00 USD | 76,180.00 USD | 28,320.00 USD |
| `1D` | `57.70` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 62,800.00 USD | 63,340.00 USD | 106,960.00 USD |
| `7D` | `57.70` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 37,980.00 USD | 58,050.00 USD |
| `1D` | `57.80` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 18,150.00 USD | 31,870.00 USD | 80,960.00 USD |
| `7D` | `57.80` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 27,080.00 USD | 38,610.00 USD | 58,040.00 USD |
| `1D` | `57.90` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 25,080.00 USD | 25,510.00 USD | 28,950.00 USD |
| `7D` | `57.90` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 14,390.00 USD | 5,500.00 USD | 30,010.00 USD |
| `1D` | `58.00` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 10,450.00 USD | 9,480.00 USD | 15,330.00 USD |
| `7D` | `58.00` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD | 107,350.00 USD |
| `1D` | `58.10` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 31,400.00 USD | 17,830.00 USD | 21,300.00 USD |
| `7D` | `58.10` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 5,470.00 USD | 19,160.00 USD | 14,070.00 USD |
| `1D` | `58.20` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 36,640.00 USD | 34,800.00 USD | 4,940.00 USD |
| `7D` | `58.20` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 31,590.00 USD | 302.55 USD |
| `1D` | `58.30` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 33,360.00 USD | 38,620.00 USD | 64,380.00 USD |
| `7D` | `58.30` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 48,850.00 USD | 11,000.00 USD | 36,500.00 USD |
| `1D` | `58.40` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 27,360.00 USD | 18,940.00 USD | 49,870.00 USD |
| `7D` | `58.40` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 27,290.00 USD | 9,260.00 USD | 86,460.00 USD |
| `1D` | `58.50` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 1,420.00 USD | 1,200.00 USD | 124.02 USD |
| `7D` | `58.50` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 2,060.00 USD | 24,530.00 USD | 0.00 USD |
| `1D` | `58.60` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 21,940.00 USD | 5,920.00 USD | 40,890.00 USD |
| `7D` | `58.60` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 30,680.00 USD | 20,260.00 USD | 51,650.00 USD |
| `1D` | `58.70` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 44,920.00 USD | 10,120.00 USD | 29,940.00 USD |
| `7D` | `58.70` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 15,810.00 USD | 11,600.00 USD | 35,320.00 USD |
| `1D` | `58.80` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 36,630.00 USD | 5,970.00 USD | 23,200.00 USD |
| `7D` | `58.80` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD |
| `1D` | `58.90` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 24,050.00 USD | 58,880.00 USD | 80,110.00 USD |
| `7D` | `58.90` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 2,140.00 USD | 54,240.00 USD | 83,500.00 USD |
| `1D` | `59.00` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 123,770.00 USD | 53,650.00 USD | 80,100.00 USD |
| `7D` | `59.00` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 259,280.00 USD | 65,270.00 USD | 118,570.00 USD |
| `1D` | `59.10` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 88,790.00 USD | 37,020.00 USD | 135,930.00 USD |
| `7D` | `59.10` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 93,390.00 USD | 45,400.00 USD | 158,780.00 USD |
| `1D` | `59.20` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 89,410.00 USD | 46,380.00 USD | 49,210.00 USD |
| `7D` | `59.20` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 153,580.00 USD | 18,540.00 USD | 174,600.00 USD |
| `1D` | `59.30` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 146,880.00 USD | 30,070.00 USD | 66,050.00 USD |
| `7D` | `59.30` | 7,430,000.00 USD | 7,430,000.00 USD | 0.00 USD | 88,710.00 USD | 67,460.00 USD | 114,310.00 USD |
| `1D` | `59.40` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 35,830.00 USD | 30,410.00 USD | 49,030.00 USD |
| `7D` | `59.40` | 7,740,000.00 USD | 7,740,000.00 USD | 0.00 USD | 107,040.00 USD | 73,620.00 USD | 124,910.00 USD |
| `1D` | `59.50` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 78,730.00 USD | 34,150.00 USD | 28,530.00 USD |
| `7D` | `59.50` | 7,890,000.00 USD | 7,890,000.00 USD | 0.00 USD | 67,060.00 USD | 61,370.00 USD | 21,090.00 USD |
| `1D` | `59.60` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 29,830.00 USD | 49,290.00 USD | 5,160.00 USD |
| `7D` | `59.60` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 184,700.00 USD | 106,840.00 USD | 72,920.00 USD |
| `1D` | `59.70` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 15,700.00 USD | 59,880.00 USD |
| `7D` | `59.70` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 55,510.00 USD | 99,970.00 USD | 162,850.00 USD |
| `1D` | `59.80` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 21,030.00 USD | 26,470.00 USD | 177.92 USD |
| `7D` | `59.80` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 118,240.00 USD | 91,980.00 USD | 154,560.00 USD |
| `1D` | `59.90` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 102,020.00 USD | 15,860.00 USD | 48,450.00 USD |
| `7D` | `59.90` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 142,290.00 USD | 34,490.00 USD | 29,380.00 USD |
| `1D` | `60.00` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 162,340.00 USD | 28,040.00 USD | 45,390.00 USD |
| `7D` | `60.00` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 100,570.00 USD | 67,520.00 USD | 83,920.00 USD |
| `1D` | `60.10` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 61,440.00 USD | 25,530.00 USD | 32,410.00 USD |
| `7D` | `60.10` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 200,540.00 USD | 84,980.00 USD | 95,670.00 USD |
| `1D` | `60.20` | 6,840,000.00 USD | 6,840,000.00 USD | 0.00 USD | 56,510.00 USD | 18,380.00 USD | 68,440.00 USD |
| `7D` | `60.20` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 162,230.00 USD | 99,360.00 USD | 108,990.00 USD |
| `1D` | `60.30` | 6,930,000.00 USD | 6,930,000.00 USD | 0.00 USD | 44,650.00 USD | 25,170.00 USD | 26,470.00 USD |
| `7D` | `60.30` | 10,550,000.00 USD | 10,550,000.00 USD | 0.00 USD | 133,350.00 USD | 100,380.00 USD | 170,480.00 USD |
| `1D` | `60.40` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 66,740.00 USD | 13,730.00 USD | 42,520.00 USD |
| `7D` | `60.40` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 55,050.00 USD | 100,560.00 USD | 202,370.00 USD |
| `1D` | `60.50` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 22,700.00 USD | 19,320.00 USD | 36,200.00 USD |
| `7D` | `60.50` | 11,270,000.00 USD | 11,270,000.00 USD | 0.00 USD | 115,390.00 USD | 80,510.00 USD | 169,260.00 USD |
| `1D` | `60.60` | 7,200,000.00 USD | 7,200,000.00 USD | 0.00 USD | 40,710.00 USD | 20,390.00 USD | 3,930.00 USD |
| `7D` | `60.60` | 11,660,000.00 USD | 11,660,000.00 USD | 0.00 USD | 251,100.00 USD | 16,970.00 USD | 118,680.00 USD |
| `1D` | `60.70` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 33,350.00 USD | 24,020.00 USD | 8,190.00 USD |
| `7D` | `60.70` | 11,800,000.00 USD | 11,800,000.00 USD | 0.00 USD | 76,200.00 USD | 37,000.00 USD | 23,900.00 USD |
| `1D` | `60.80` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 10,510.00 USD | 18,960.00 USD | 49,250.00 USD |
| `7D` | `60.80` | 11,950,000.00 USD | 11,950,000.00 USD | 0.00 USD | 46,960.00 USD | 28,960.00 USD | 76,200.00 USD |
| `1D` | `60.90` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 37,840.00 USD | 31,510.00 USD | 24,800.00 USD |
| `7D` | `60.90` | 12,160,000.00 USD | 12,160,000.00 USD | 0.00 USD | 105,970.00 USD | 43,870.00 USD | 64,920.00 USD |
| `1D` | `61.00` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 43,930.00 USD | 6,430.00 USD | 18,420.00 USD |
| `7D` | `61.00` | 12,220,000.00 USD | 12,220,000.00 USD | 0.00 USD | 43,120.00 USD | 11,530.00 USD | 0.00 USD |
| `1D` | `61.10` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 21,130.00 USD | 18,440.00 USD | 15,730.00 USD |
| `7D` | `61.10` | 12,260,000.00 USD | 12,260,000.00 USD | 0.00 USD | 31,540.00 USD | 13,590.00 USD | 189.67 USD |
| `1D` | `61.20` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 74,800.00 USD | 5,570.00 USD | 39,080.00 USD |
| `7D` | `61.20` | 12,390,000.00 USD | 12,390,000.00 USD | 0.00 USD | 51,570.00 USD | 24,770.00 USD | 47,810.00 USD |
| `1D` | `61.30` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 3,530.00 USD | 6,650.00 USD | 7,570.00 USD |
| `7D` | `61.30` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 14,390.00 USD | 13,210.00 USD | 24,230.00 USD |
| `1D` | `61.40` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 1,190.00 USD | 709.61 USD | 5,230.00 USD |
| `7D` | `61.40` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 62,340.00 USD | 25,720.00 USD | 43,510.00 USD |
| `7D` | `61.50` | 12,670,000.00 USD | 12,670,000.00 USD | 0.00 USD | 17,710.00 USD | 42,440.00 USD | 41,390.00 USD |
| `7D` | `61.60` | 12,880,000.00 USD | 12,880,000.00 USD | 0.00 USD | 32,920.00 USD | 58,350.00 USD | 121,470.00 USD |
| `7D` | `61.70` | 13,080,000.00 USD | 13,080,000.00 USD | 0.00 USD | 82,860.00 USD | 10,880.00 USD | 99,740.00 USD |
| `7D` | `61.80` | 13,340,000.00 USD | 13,340,000.00 USD | 0.00 USD | 169,680.00 USD | 25,670.00 USD | 71,530.00 USD |
| `7D` | `61.90` | 13,490,000.00 USD | 13,490,000.00 USD | 0.00 USD | 73,690.00 USD | 32,820.00 USD | 41,580.00 USD |
| `7D` | `62.00` | 13,590,000.00 USD | 13,590,000.00 USD | 0.00 USD | 50,080.00 USD | 8,550.00 USD | 40,590.00 USD |
| `7D` | `62.10` | 13,600,000.00 USD | 13,600,000.00 USD | 0.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.20` | 13,710,000.00 USD | 13,710,000.00 USD | 0.00 USD | 34,230.00 USD | 34,620.00 USD | 41,360.00 USD |
| `7D` | `62.30` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 25,910.00 USD | 23,450.00 USD | 57,530.00 USD |
| `7D` | `62.40` | 13,930,000.00 USD | 13,930,000.00 USD | 0.00 USD | 62,940.00 USD | 25,250.00 USD | 25,440.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `409.90M` | Total OI Tokens: `7,357,800.3 LTC`
  * 1h OI Change: `+0.25%` | 4h OI Change: `-1.42%` | 24h OI Change: `-10.02%`
  * Exchange Breakdown: Binance=`72.11M` | Bybit=`66.61M` | OKX=`34.80M` | Hyperliquid=`22.26M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `9.38K` | Last 24h: `29.34K` | Last 3d: `56.60K` | Last 7d: `113.64K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0025%` |
| **USDT Bybit** | `0.0044%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0009%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `47.94%` | `52.06%` | `0.92` | 2,340,000.00 USD |
| `15M` | `Binance` | `66.18%` | `33.82%` | `1.96` | 437,960.00 USD |
| `15M` | `OKX` | `44.39%` | `55.61%` | `0.80` | 77,120.00 USD |
| `15M` | `Bybit` | `62.89%` | `37.11%` | `1.69` | 90,330.00 USD |
| `15M` | `KuCoin` | `75.09%` | `24.91%` | `3.01` | 97,500.00 USD |
| `15M` | `Gate` | `50.1%` | `49.9%` | `1.00` | 35,460.00 USD |
| `15M` | `Bitget` | `61.09%` | `38.91%` | `1.57` | 11,960.00 USD |
| `15M` | `BingX` | `6.78%` | `93.22%` | `0.07` | 510,030.00 USD |
| `15M` | `MEXC` | `75.64%` | `24.36%` | `3.11` | 59,230.00 USD |
| `15M` | `Bitunix` | `66.58%` | `33.42%` | `1.99` | 47,030.00 USD |
| `15M` | `Hyperliquid` | `94.41%` | `5.59%` | `16.89` | 43,250.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.28%` | `49.72%` | `1.01` | 755,350.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `99.14%` | `0.86%` | `115.28` | 92,340.00 USD |
| `15M` | `HTX` | `37.02%` | `62.98%` | `0.59` | 509.20 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `17%` | `83%` | `0.20` | 71,300.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 533.16 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `100%` | `0%` | `1.00` | 4,140.00 USD |
| `15M` | `Whale Positions` | `66.18%` | `33.82%` | `1.96` | 437,960.00 USD |
| `15M` | `Global Accounts` | `47.94%` | `52.06%` | `0.92` | 2,340,000.00 USD |
| `1H` | `LTC` | `51.13%` | `48.87%` | `1.05` | 7,160,000.00 USD |
| `1H` | `Binance` | `49.27%` | `50.73%` | `0.97` | 1,610,000.00 USD |
| `1H` | `OKX` | `45.69%` | `54.31%` | `0.84` | 557,970.00 USD |
| `1H` | `Bybit` | `54.27%` | `45.73%` | `1.19` | 295,380.00 USD |
| `1H` | `KuCoin` | `59.1%` | `40.9%` | `1.44` | 585,700.00 USD |
| `1H` | `Gate` | `45.66%` | `54.34%` | `0.84` | 113,520.00 USD |
| `1H` | `Bitget` | `44.57%` | `55.43%` | `0.80` | 90,590.00 USD |
| `1H` | `BingX` | `23.12%` | `76.88%` | `0.30` | 818,280.00 USD |
| `1H` | `MEXC` | `60.19%` | `39.81%` | `1.51` | 169,500.00 USD |
| `1H` | `Bitunix` | `54.37%` | `45.63%` | `1.19` | 172,540.00 USD |
| `1H` | `Hyperliquid` | `77.28%` | `22.72%` | `3.40` | 135,070.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.14%` | `49.86%` | `1.01` | 2,040,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `98.61%` | `1.39%` | `70.94` | 461,720.00 USD |
| `1H` | `HTX` | `17.45%` | `82.55%` | `0.21` | 5,540.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `23.13%` | `76.87%` | `0.30` | 83,880.00 USD |
| `1H` | `Aster` | `67.83%` | `32.17%` | `2.11` | 2,040.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `96.37%` | `3.63%` | `26.55` | 34,030.00 USD |
| `1H` | `Whale Positions` | `49.27%` | `50.73%` | `0.97` | 1,610,000.00 USD |
| `1H` | `Global Accounts` | `51.13%` | `48.87%` | `1.05` | 7,160,000.00 USD |
| `4H` | `LTC` | `48.17%` | `51.83%` | `0.93` | 49,260,000.00 USD |
| `4H` | `Binance` | `47.12%` | `52.88%` | `0.89` | 14,500,000.00 USD |
| `4H` | `OKX` | `37.64%` | `62.36%` | `0.60` | 4,910,000.00 USD |
| `4H` | `Bybit` | `45.49%` | `54.51%` | `0.83` | 3,670,000.00 USD |
| `4H` | `KuCoin` | `45.79%` | `54.21%` | `0.84` | 286,510.00 USD |
| `4H` | `Gate` | `52.1%` | `47.9%` | `1.09` | 4,210,000.00 USD |
| `4H` | `Bitget` | `50.23%` | `49.77%` | `1.01` | 1,760,000.00 USD |
| `4H` | `BingX` | `34.99%` | `65.01%` | `0.54` | 10,520,000.00 USD |
| `4H` | `MEXC` | `49.81%` | `50.19%` | `0.99` | 1,300,000.00 USD |
| `4H` | `Bitunix` | `48.04%` | `51.96%` | `0.92` | 1,030,000.00 USD |
| `4H` | `Hyperliquid` | `44.36%` | `55.64%` | `0.80` | 371,520.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.68%` | `49.32%` | `1.03` | 1,240,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `94.3%` | `5.7%` | `16.54` | 4,400,000.00 USD |
| `4H` | `HTX` | `50.76%` | `49.24%` | `1.03` | 99,680.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `59.65%` | `40.35%` | `1.48` | 258,650.00 USD |
| `4H` | `Aster` | `38.13%` | `61.87%` | `0.62` | 33,930.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `27.4%` | `72.6%` | `0.38` | 653,650.00 USD |
| `4H` | `Whale Positions` | `47.12%` | `52.88%` | `0.89` | 14,500,000.00 USD |
| `4H` | `Global Accounts` | `48.17%` | `51.83%` | `0.93` | 49,260,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `55.70` | `55.69` | `55.70` | `55.78` | `55.55` | 839,476.56 USD | 572,886.16 USD | 266,590.39 USD | 306,295.77 USD | `+36.49%` | `1B / 5S` |
| `5:00 UTC` | `55.59` | `55.60` | `55.59` | `55.70` | `55.52` | 436,166.22 USD | 242,135.61 USD | 194,030.61 USD | 48,104.99 USD | `+11.03%` | `3B / 4S` |
| `0:00 UTC` | `55.50` | `55.53` | `55.50` | `55.70` | `55.44` | 464,437.63 USD | 192,555.45 USD | 271,882.18 USD | -79,326.74 USD | `-17.08%` | `3B / 5S` |
| `5:00 UTC` | `55.42` | `55.46` | `55.42` | `55.59` | `55.39` | 371,902.17 USD | 185,679.40 USD | 186,222.77 USD | -543.37 USD | `-0.15%` | `2B / 4S` |
| `0:00 UTC` | `55.39` | `55.44` | `55.39` | `55.55` | `55.34` | 379,922.90 USD | 203,005.18 USD | 176,917.72 USD | 26,087.46 USD | `+6.87%` | `4B / 0S` |
| `5:00 UTC` | `55.42` | `55.40` | `55.42` | `55.52` | `55.27` | 934,212.03 USD | 256,275.15 USD | 677,936.88 USD | -421,661.72 USD | `-45.14%` | `0B / 6S` |
| `0:00 UTC` | `55.25` | `55.25` | `55.25` | `55.41` | `55.16` | 429,058.08 USD | 168,966.41 USD | 260,091.67 USD | -91,125.26 USD | `-21.24%` | `0B / 7S` |
| `5:00 UTC` | `55.55` | `55.41` | `55.55` | `55.62` | `55.11` | 1,970,804.61 USD | 831,054.50 USD | 1,139,750.11 USD | -308,695.61 USD | `-15.66%` | `11B / 5S` |
| `0:00 UTC` | `55.59` | `55.64` | `55.59` | `55.77` | `55.47` | 693,956.44 USD | 452,465.90 USD | 241,490.54 USD | 210,975.35 USD | `+30.40%` | `12B / 0S` |
| `5:00 UTC` | `55.45` | `55.54` | `55.45` | `55.75` | `55.41` | 1,258,146.87 USD | 321,813.56 USD | 936,333.31 USD | -614,519.74 USD | `-48.84%` | `2B / 16S` |

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
| `5m` | 26,140.00 USD | 39,550.00 USD | **`ACCUMULATION`** |
| `15m` | 101,670.00 USD | -718,540.00 USD | **`DISTRIBUTION`** |
| `30m` | 154,280.00 USD | -426,990.00 USD | **`DISTRIBUTION`** |
| `1h` | 221,150.00 USD | -910,610.00 USD | **`DISTRIBUTION`** |
| `2h` | 19,140.00 USD | -1,540,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -108,890.00 USD | -2,440,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 381,510.00 USD | -1,960,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 509,720.00 USD | -3,440,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -120,600.00 USD | -6,060,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 548,800.00 USD | -7,050,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 4,780,000.00 USD | -25,800,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -23,850,000.00 USD | -199,640,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+26.14K` | 15m=`+101.67K` | 1h=`+221.15K` | 24h=`+548.80K`
* Futures Capital Netflows: 5m=`+39.55K` | 15m=`-718.54K` | 1h=`-910.61K` | 24h=`-7.05M`
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
  * `2026-10-30 16:26:21 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:29:21 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `52.96` (Risk Distance: `1.65` pts)
  * +2.5R Take Profit: `58.74`
  * Mathematical Lot Sizing: **`6.06 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `56.07` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `57.72` (Risk Distance: `1.65` pts)
  * +2.5R Take Profit: `51.94`
  * Mathematical Lot Sizing: **`6.06 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`56.20`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
