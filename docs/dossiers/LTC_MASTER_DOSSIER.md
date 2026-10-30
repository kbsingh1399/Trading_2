# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 15:45:20 IST` (`2026-10-30 10:15:20 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `55.05` | **Live Ask Quote**: `55.34` | **Mid Price**: `55.20`
- **Spread Points**: `300.00` | **Spread BPS**: `54.35 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `54.86` | VWAP Z-Score: `+0.37` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.3067` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `41.40` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `57.64` | Lower -3.00σ Band: `52.08`
  * Upper +2.51σ Band: `57.19` | Lower -2.51σ Band: `52.54`
  * Upper +2.01σ Band: `56.73` | Lower -2.01σ Band: `53.00`
  * Upper +2.00σ Band: `56.72` | Lower -2.00σ Band: `53.01`
  * Upper +1.28σ Band: `56.05` | Lower -1.28σ Band: `53.68`
  * Upper +1.00σ Band: `55.79` | Lower -1.00σ Band: `53.94`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`55.39` | EMA-20=`55.50` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`55.67` (Slope: `+0.0000`) | EMA-100=`56.14`
  * Institutional Anchors: EMA-144=`56.39` | EMA-200=`56.55` (Slope: `-0.2406`) | EMA-233=`56.60`
- **Range Boundaries**: 24H High=`58.72` | 24H Low=`52.64` | Weekly High=`59.62` | Weekly Low=`52.64`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `56.12` (Distance: `-1.64%`)
  * Point of Control (POC) = `55.30` (Distance: `-0.20%`)
  * Value Area Low (VAL) = `54.61` (Distance: `+1.07%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.40` | POC=`57.72` | VAL=`56.83`
  * Prior Day Extremes: PDH=`59.52` | PDL=`54.18` | PDC=`54.46`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`58.34` | Weekly POC=`56.43` | Weekly VAL=`55.83`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`56.03` | Low=`52.64`
  * London Session (08:00-16:00 UTC): High=`56.23` | Low=`54.97`
  * New York Session (13:00-21:00 UTC): High=`55.24` | Low=`54.97`
  * Initial Balance (First Hour): IB High=`56.22` | IB Low=`55.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `54.97` - `55.42`
  * Optimal Trade Entry (OTE 0.705): `55.31`
  * Structural Invalidation Anchor (0.786): `55.64`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `55.51` | `55.51` | `55.26` | `55.38` | `6,052` | 335,237.70 USD | -114,613.85 USD | `-34.19%` | -5,627,009.22 USD | `-0.99` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `55.38` | `55.45` | `55.30` | `55.43` | `3,720` | 206,019.66 USD | -15,751.23 USD | `-7.65%` | -5,642,760.45 USD | `-0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `55.44` | `55.46` | `55.36` | `55.41` | `7,070` | 391,815.68 USD | -291,097.81 USD | `-74.29%` | -5,933,858.26 USD | `-2.16` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `55.47` | `55.55` | `55.33` | `55.51` | `6,853` | 379,922.90 USD | 26,087.46 USD | `+6.87%` | -5,470,201.09 USD | `+0.30` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `55.51` | `55.51` | `55.26` | `55.41` | `16,863` | 934,212.03 USD | -421,661.72 USD | `-45.14%` | -5,891,862.81 USD | `-2.43` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `55.41` | `55.41` | `55.16` | `55.25` | `6,269` | 346,340.42 USD | -88,963.34 USD | `-25.69%` | -5,980,826.15 USD | `-0.30` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `55.96` | `55.99` | `55.51` | `55.54` | `48,222` | 2,686,866.22 USD | -29,505.47 USD | `-1.10%` | -5,487,267.89 USD | `+0.34` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `55.54` | `55.70` | `55.26` | `55.41` | `38,786` | 2,150,474.73 USD | -475,444.38 USD | `-22.11%` | -5,962,712.28 USD | `-0.18` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `55.41` | `55.41` | `55.16` | `55.25` | `6,275` | 346,654.36 USD | -89,177.15 USD | `-25.73%` | -6,051,889.42 USD | `+0.31` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -5,054,684.98 USD | `-0.61` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.47` | `55.72` | `55.97` | `202,255` | 11,356,305.33 USD | -519,640.59 USD | `-4.58%` | -5,574,325.57 USD | `+0.43` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `55.96` | `55.99` | `55.26` | `55.41` | `86,981` | 4,835,820.08 USD | -504,369.13 USD | `-10.43%` | -6,078,694.70 USD | `+0.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | 387,872.12 USD | `-1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,876,168.80 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -5,054,684.98 USD | `-0.61` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.47` | `55.72` | `55.97` | `202,255` | 11,356,305.33 USD | -519,640.59 USD | `-4.58%` | -5,574,325.57 USD | `+0.43` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `55.96` | `55.99` | `55.16` | `55.25` | `93,278` | 5,183,681.37 USD | -593,913.19 USD | `-11.46%` | -6,168,238.76 USD | `+0.34` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`55.20`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:40:55 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1073` | `0xeadc...9d55` | `LONG` | 2,013,201.21 USD | `36,463.77` | `52.78` | `55.19` | `0.000000` | 88,525.26 USD | `+4.40%` | `10X Cross` |
| `1083` | `0x9aa5...58af` | `SHORT` | 1,996,789.21 USD | `36,177.65` | `71.22` | `55.19` | `306.31` | 579,697.45 USD | `+29.03%` | `10X Cross` |

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
  * 24H Horizon: Short MP=`56.49` (Vol: 204,200.00 USD, Dist: `+1.88%`) | Long MP=`54.13` (Vol: 153,300.00 USD, Dist: `--2.37%`)
  * 48H Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.40%`) | Long MP=`54.12` (Vol: 153,300.00 USD, Dist: `--2.41%`)
  * 3D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.40%`) | Long MP=`54.12` (Vol: 153,300.00 USD, Dist: `--2.41%`)
  * 7D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.40%`) | Long MP=`54.12` (Vol: 153,300.00 USD, Dist: `--2.41%`)
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
| `7D` | `Long Liquidation` | `47.20` | 8,220,000.00 USD | 8,220,000.00 USD | 9,650.00 USD | 2,470.00 USD | 114.09 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.25` | 9,030.00 USD | 724,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.30` | 8,210,000.00 USD | 8,210,000.00 USD | 692.33 USD | 4,740.00 USD | 6,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.35` | 43,920.00 USD | 715,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.40` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 1,520.00 USD | 28,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.45` | 2,590.00 USD | 671,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.50` | 8,160,000.00 USD | 8,160,000.00 USD | 11,830.00 USD | 0.00 USD | 7,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.55` | 4,450.00 USD | 669,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 47,750.00 USD | 664,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 381.04 USD | 617,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.10` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.15` | 1,690.00 USD | 616,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.20` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.25` | 110.49 USD | 615,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.40` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 6,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.55` | 2,030.00 USD | 614,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.60` | 8,130,000.00 USD | 8,130,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.65` | 8,280.00 USD | 612,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 333.94 USD | 604,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.80` | 8,120,000.00 USD | 8,120,000.00 USD | 1,780.00 USD | 2,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `48.90` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 960.40 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.95` | 252.58 USD | 604,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,580.00 USD | 604,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,740.00 USD | 602,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.30` | 8,120,000.00 USD | 8,120,000.00 USD | 15,190.00 USD | 4,490.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.35` | 5,230.00 USD | 596,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.40` | 8,080,000.00 USD | 8,080,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.45` | 19,440.00 USD | 591,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.50` | 8,080,000.00 USD | 8,080,000.00 USD | 2,830.00 USD | 7,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.55` | 18,010.00 USD | 572,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.60` | 8,070,000.00 USD | 8,070,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.65` | 75,190.00 USD | 554,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.70` | 3,950,000.00 USD | 3,950,000.00 USD | 11,420.00 USD | 10,990.00 USD | 4,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.70` | 8,050,000.00 USD | 8,050,000.00 USD | 12,090.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.75` | 1,250.00 USD | 478,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.80` | 3,920,000.00 USD | 3,920,000.00 USD | 6,420.00 USD | 6,910.00 USD | 21,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.80` | 8,030,000.00 USD | 8,030,000.00 USD | 9,930.00 USD | 8,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `49.90` | 3,890,000.00 USD | 3,890,000.00 USD | 24,520.00 USD | 13,560.00 USD | 24,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.90` | 8,020,000.00 USD | 8,020,000.00 USD | 45,030.00 USD | 13,920.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.95` | 19,920.00 USD | 477,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.00` | 3,830,000.00 USD | 3,830,000.00 USD | 13,200.00 USD | 16,830.00 USD | 40,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.00` | 7,950,000.00 USD | 7,950,000.00 USD | 22,100.00 USD | 19,810.00 USD | 24,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.05` | 1,820.00 USD | 457,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.10` | 3,750,000.00 USD | 3,750,000.00 USD | 3,780.00 USD | 4,040.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.10` | 7,890,000.00 USD | 7,890,000.00 USD | 363.50 USD | 682.90 USD | 8,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.20` | 3,740,000.00 USD | 3,740,000.00 USD | 177.10 USD | 709.61 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.20` | 7,880,000.00 USD | 7,880,000.00 USD | 6,960.00 USD | 500.40 USD | 42,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.25` | 102.51 USD | 455,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.30` | 3,730,000.00 USD | 3,730,000.00 USD | 171.03 USD | 3,880.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.30` | 7,830,000.00 USD | 7,830,000.00 USD | 16,270.00 USD | 10,780.00 USD | 7,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.35` | 1,140.00 USD | 455,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.40` | 3,730,000.00 USD | 3,730,000.00 USD | 8,260.00 USD | 11,890.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.40` | 7,790,000.00 USD | 7,790,000.00 USD | 28,280.00 USD | 26,580.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,720.00 USD | 454,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.50` | 3,700,000.00 USD | 3,700,000.00 USD | 8,910.00 USD | 8,790.00 USD | 10,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.50` | 7,700,000.00 USD | 7,700,000.00 USD | 32,490.00 USD | 6,790.00 USD | 44,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.55` | 84,100.00 USD | 449,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.60` | 3,680,000.00 USD | 3,680,000.00 USD | 7,330.00 USD | 3,440.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.60` | 7,620,000.00 USD | 7,620,000.00 USD | 67,580.00 USD | 21,530.00 USD | 31,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.70` | 3,660,000.00 USD | 3,660,000.00 USD | 8,170.00 USD | 2,300.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.70` | 7,500,000.00 USD | 7,500,000.00 USD | 65,920.00 USD | 32,820.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.75` | 9,050.00 USD | 365,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.80` | 3,630,000.00 USD | 3,630,000.00 USD | 12,550.00 USD | 3,100.00 USD | 8,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.80` | 7,360,000.00 USD | 7,360,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.90` | 3,610,000.00 USD | 3,610,000.00 USD | 826.24 USD | 260.05 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.90` | 7,260,000.00 USD | 7,260,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.95` | 431.55 USD | 356,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.00` | 3,600,000.00 USD | 3,600,000.00 USD | 5,040.00 USD | 0.00 USD | 430.77 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.00` | 7,010,000.00 USD | 7,010,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.10` | 3,590,000.00 USD | 3,590,000.00 USD | 9,210.00 USD | 6,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.10` | 6,880,000.00 USD | 6,880,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.15` | 219,370.00 USD | 356,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.20` | 3,580,000.00 USD | 3,580,000.00 USD | 1,770.00 USD | 1,130.00 USD | 19,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.20` | 6,800,000.00 USD | 6,800,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.25` | 202.44 USD | 136,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.30` | 3,560,000.00 USD | 3,560,000.00 USD | 8,650.00 USD | 9,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.30` | 6,740,000.00 USD | 6,740,000.00 USD | 28,400.00 USD | 26,720.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.35` | 453.93 USD | 136,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.40` | 3,540,000.00 USD | 3,540,000.00 USD | 3,250.00 USD | 5,460.00 USD | 416.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.40` | 6,630,000.00 USD | 6,630,000.00 USD | 73,130.00 USD | 42,820.00 USD | 46,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.45` | 27,210.00 USD | 136,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.50` | 3,530,000.00 USD | 3,530,000.00 USD | 5,650.00 USD | 10,010.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.50` | 6,470,000.00 USD | 6,470,000.00 USD | 38,520.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.55` | 551.07 USD | 109,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.60` | 3,470,000.00 USD | 3,470,000.00 USD | 7,150.00 USD | 18,440.00 USD | 731.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.60` | 6,370,000.00 USD | 6,370,000.00 USD | 37,880.00 USD | 36,790.00 USD | 41,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.65` | 9,100.00 USD | 108,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.70` | 3,440,000.00 USD | 3,440,000.00 USD | 2,660.00 USD | 12,840.00 USD | 44.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.70` | 6,260,000.00 USD | 6,260,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.75` | 6,480.00 USD | 99,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.80` | 3,430,000.00 USD | 3,430,000.00 USD | 11,460.00 USD | 19,520.00 USD | 13,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.80` | 6,220,000.00 USD | 6,220,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.85` | 13,680.00 USD | 92,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.90` | 3,380,000.00 USD | 3,380,000.00 USD | 10,140.00 USD | 19,910.00 USD | 23,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.90` | 6,160,000.00 USD | 6,160,000.00 USD | 5,870.00 USD | 25,410.00 USD | 28,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.95` | 13,950.00 USD | 79,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.00` | 3,330,000.00 USD | 3,330,000.00 USD | 20,980.00 USD | 25,620.00 USD | 24,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.00` | 6,100,000.00 USD | 6,100,000.00 USD | 65,840.00 USD | 26,440.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.05` | 2,860.00 USD | 65,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.10` | 3,260,000.00 USD | 3,260,000.00 USD | 34,970.00 USD | 17,300.00 USD | 50,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 6,000,000.00 USD | 6,000,000.00 USD | 24,220.00 USD | 28,090.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.15` | 1,900.00 USD | 62,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.20` | 3,160,000.00 USD | 3,160,000.00 USD | 15,890.00 USD | 7,630.00 USD | 49,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 5,910,000.00 USD | 5,910,000.00 USD | 38,380.00 USD | 13,960.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.25` | 4,930.00 USD | 60,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.30` | 3,080,000.00 USD | 3,080,000.00 USD | 26,510.00 USD | 22,090.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 5,830,000.00 USD | 5,830,000.00 USD | 26,450.00 USD | 40,700.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.35` | 134.02 USD | 55,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.40` | 3,020,000.00 USD | 3,020,000.00 USD | 13,070.00 USD | 15,400.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 5,760,000.00 USD | 5,760,000.00 USD | 20,580.00 USD | 38,950.00 USD | 22,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.45` | 5,820.00 USD | 55,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.50` | 2,990,000.00 USD | 2,990,000.00 USD | 53,990.00 USD | 30,000.00 USD | 79,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.50` | 5,680,000.00 USD | 5,680,000.00 USD | 39,410.00 USD | 0.00 USD | 11,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.55` | 8,700.00 USD | 49,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.60` | 2,830,000.00 USD | 2,830,000.00 USD | 9,060.00 USD | 43,700.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.60` | 5,620,000.00 USD | 5,620,000.00 USD | 67,180.00 USD | 32,590.00 USD | 59,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.70` | 2,770,000.00 USD | 2,770,000.00 USD | 18,270.00 USD | 19,780.00 USD | 40,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.70` | 5,470,000.00 USD | 5,470,000.00 USD | 19,550.00 USD | 75,910.00 USD | 108,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.75` | 30,280.00 USD | 40,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.80` | 2,690,000.00 USD | 2,690,000.00 USD | 28,000.00 USD | 50,850.00 USD | 72,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.80` | 5,260,000.00 USD | 5,260,000.00 USD | 30,590.00 USD | 25,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.85` | 5,950.00 USD | 10,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.90` | 2,540,000.00 USD | 2,540,000.00 USD | 43,760.00 USD | 50,880.00 USD | 30,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.90` | 5,210,000.00 USD | 5,210,000.00 USD | 30,900.00 USD | 11,650.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.95` | 531.09 USD | 4,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.00` | 2,410,000.00 USD | 2,410,000.00 USD | 26,800.00 USD | 33,430.00 USD | 39,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.00` | 5,130,000.00 USD | 5,130,000.00 USD | 39,690.00 USD | 22,700.00 USD | 77,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.05` | 202.12 USD | 4,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.10` | 2,310,000.00 USD | 2,310,000.00 USD | 12,590.00 USD | 53,180.00 USD | 85,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.10` | 4,990,000.00 USD | 4,990,000.00 USD | 45,320.00 USD | 20,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.15` | 2,030.00 USD | 3,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.20` | 2,160,000.00 USD | 2,160,000.00 USD | 36,030.00 USD | 22,000.00 USD | 46,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.20` | 4,920,000.00 USD | 4,920,000.00 USD | 162,460.00 USD | 50,210.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.25` | 1,030.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.30` | 2,060,000.00 USD | 2,060,000.00 USD | 8,140.00 USD | 28,530.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.30` | 4,690,000.00 USD | 4,690,000.00 USD | 59,390.00 USD | 49,210.00 USD | 35,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.35` | 941.09 USD | 941.09 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.40` | 2,010,000.00 USD | 2,010,000.00 USD | 12,600.00 USD | 10,640.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.40` | 4,540,000.00 USD | 4,540,000.00 USD | 44,030.00 USD | 17,420.00 USD | 91,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.50` | 1,990,000.00 USD | 1,990,000.00 USD | 9,170.00 USD | 5,700.00 USD | 22,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.50` | 4,390,000.00 USD | 4,390,000.00 USD | 60,260.00 USD | 3,440.00 USD | 28,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.60` | 1,950,000.00 USD | 1,950,000.00 USD | 75,950.00 USD | 3,830.00 USD | 20,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.60` | 4,300,000.00 USD | 4,300,000.00 USD | 52,800.00 USD | 3,780.00 USD | 20,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.70` | 1,850,000.00 USD | 1,850,000.00 USD | 6,210.00 USD | 11,100.00 USD | 11,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.70` | 4,220,000.00 USD | 4,220,000.00 USD | 131,400.00 USD | 21,330.00 USD | 13,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.80` | 1,820,000.00 USD | 1,820,000.00 USD | 53,640.00 USD | 28,920.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.80` | 4,050,000.00 USD | 4,050,000.00 USD | 99,150.00 USD | 43,900.00 USD | 302.55 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.90` | 1,730,000.00 USD | 1,730,000.00 USD | 51,060.00 USD | 39,560.00 USD | 27,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.90` | 3,910,000.00 USD | 3,910,000.00 USD | 160,820.00 USD | 22,780.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.00` | 1,610,000.00 USD | 1,610,000.00 USD | 76,010.00 USD | 21,440.00 USD | 86,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.00` | 3,720,000.00 USD | 3,720,000.00 USD | 380,340.00 USD | 71,820.00 USD | 304,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.10` | 1,430,000.00 USD | 1,430,000.00 USD | 94,870.00 USD | 25,040.00 USD | 49,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.10` | 2,960,000.00 USD | 2,960,000.00 USD | 302,190.00 USD | 0.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.20` | 1,260,000.00 USD | 1,260,000.00 USD | 72,600.00 USD | 35,780.00 USD | 40,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.20` | 2,660,000.00 USD | 2,660,000.00 USD | 205,060.00 USD | 5,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.30` | 1,110,000.00 USD | 1,110,000.00 USD | 46,340.00 USD | 30,990.00 USD | 15,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.30` | 2,450,000.00 USD | 2,450,000.00 USD | 381,380.00 USD | 43,780.00 USD | 181,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.40` | 1,020,000.00 USD | 1,020,000.00 USD | 62,350.00 USD | 92,560.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.40` | 1,840,000.00 USD | 1,840,000.00 USD | 304,270.00 USD | 63,170.00 USD | 92,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.50` | 861,380.00 USD | 861,380.00 USD | 24,100.00 USD | 64,250.00 USD | 9,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.50` | 1,380,000.00 USD | 1,380,000.00 USD | 159,720.00 USD | 35,580.00 USD | 239,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.60` | 763,930.00 USD | 763,930.00 USD | 913.17 USD | 25,490.00 USD | 43,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.60` | 944,400.00 USD | 944,400.00 USD | 18,530.00 USD | 1,930.00 USD | 131,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.70` | 693,940.00 USD | 693,940.00 USD | 6,600.00 USD | 23,060.00 USD | 105,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.70` | 792,560.00 USD | 792,560.00 USD | 0.00 USD | 3,600.00 USD | 41,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.80` | 558,480.00 USD | 558,480.00 USD | 0.00 USD | 48,420.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.80` | 747,650.00 USD | 747,650.00 USD | 0.00 USD | 35,700.00 USD | 26,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.90` | 486,140.00 USD | 486,140.00 USD | 66,900.00 USD | 65,440.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.90` | 685,510.00 USD | 685,510.00 USD | 0.00 USD | 112,280.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.00` | 342,950.00 USD | 342,950.00 USD | 40,710.00 USD | 54,150.00 USD | 55,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.00` | 524,940.00 USD | 524,940.00 USD | 97,700.00 USD | 2,830.00 USD | 19,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.10` | 192,890.00 USD | 192,890.00 USD | 50,530.00 USD | 62,170.00 USD | 80,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.10` | 405,060.00 USD | 405,060.00 USD | 54,590.00 USD | 18,510.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.20` | 113,680.00 USD | 113,680.00 USD | 39,390.00 USD | 7,890.00 USD | 66,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.20` | 227,360.00 USD | 227,360.00 USD | 39,390.00 USD | 7,890.00 USD | 66,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.20` | 267,270.00 USD | 267,270.00 USD | 57,400.00 USD | 59,710.00 USD | 150,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.30` | 354,920.00 USD | 354,920.00 USD | 52,860.00 USD | 15,520.00 USD | 59,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.30` | 23,140.00 USD | 23,140.00 USD | 23,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.30` | 46,280.00 USD | 46,280.00 USD | 23,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.40` | 51,080.00 USD | 51,080.00 USD | 0.00 USD | 0.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.50` | 360,420.00 USD | 360,420.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.70` | 368,730.00 USD | 368,730.00 USD | 0.00 USD | 7,700.00 USD | 613.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.70` | 257,510.00 USD | 257,510.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.80` | 371,910.00 USD | 371,910.00 USD | 0.00 USD | 0.00 USD | 3,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.80` | 348,480.00 USD | 348,480.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.90` | 424,970.00 USD | 424,970.00 USD | 51,520.00 USD | 0.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.90` | 489,800.00 USD | 489,800.00 USD | 141,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.00` | 429,350.00 USD | 429,350.00 USD | 0.00 USD | 0.00 USD | 4,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.00` | 660,920.00 USD | 660,920.00 USD | 2,590.00 USD | 0.00 USD | 168,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.20` | 740,860.00 USD | 740,860.00 USD | 0.00 USD | 79,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `56.25` | 700.88 USD | 700.88 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `56.30` | 439,170.00 USD | 439,170.00 USD | 0.00 USD | 5,870.00 USD | 3,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.30` | 743,460.00 USD | 743,460.00 USD | 0.00 USD | 0.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.40` | 483,810.00 USD | 483,810.00 USD | 5,040.00 USD | 37,100.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.40` | 762,350.00 USD | 762,350.00 USD | 2,650.00 USD | 16,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.50` | 940,610.00 USD | 940,610.00 USD | 169,280.00 USD | 132,970.00 USD | 154,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.50` | 1,130,000.00 USD | 1,130,000.00 USD | 170,750.00 USD | 187,200.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.60` | 1,240,000.00 USD | 1,240,000.00 USD | 61,400.00 USD | 161,300.00 USD | 81,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.60` | 1,680,000.00 USD | 1,680,000.00 USD | 363,190.00 USD | 185,910.00 USD | 507.54 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.70` | 1,720,000.00 USD | 1,720,000.00 USD | 114,230.00 USD | 45,300.00 USD | 315,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.70` | 2,030,000.00 USD | 2,030,000.00 USD | 117,290.00 USD | 141,830.00 USD | 98,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.80` | 1,960,000.00 USD | 1,960,000.00 USD | 117,760.00 USD | 20,790.00 USD | 106,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.80` | 2,620,000.00 USD | 2,620,000.00 USD | 172,110.00 USD | 92,780.00 USD | 318,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.90` | 2,060,000.00 USD | 2,060,000.00 USD | 45,140.00 USD | 17,930.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.90` | 3,090,000.00 USD | 3,090,000.00 USD | 113,780.00 USD | 52,200.00 USD | 307,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.00` | 2,140,000.00 USD | 2,140,000.00 USD | 6,480.00 USD | 43,030.00 USD | 29,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.00` | 3,410,000.00 USD | 3,410,000.00 USD | 88,680.00 USD | 56,390.00 USD | 178,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.10` | 2,340,000.00 USD | 2,340,000.00 USD | 77,000.00 USD | 77,400.00 USD | 46,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.10` | 3,550,000.00 USD | 3,550,000.00 USD | 36,580.00 USD | 79,290.00 USD | 21,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.20` | 2,600,000.00 USD | 2,600,000.00 USD | 53,080.00 USD | 78,490.00 USD | 120,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.20` | 3,720,000.00 USD | 3,720,000.00 USD | 118,850.00 USD | 23,920.00 USD | 23,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.30` | 2,800,000.00 USD | 2,800,000.00 USD | 70,930.00 USD | 44,630.00 USD | 87,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.30` | 3,920,000.00 USD | 3,920,000.00 USD | 76,940.00 USD | 28,570.00 USD | 98,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.40` | 3,010,000.00 USD | 3,010,000.00 USD | 84,960.00 USD | 52,400.00 USD | 78,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.40` | 4,380,000.00 USD | 4,380,000.00 USD | 124,180.00 USD | 72,180.00 USD | 257,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.50` | 3,450,000.00 USD | 3,450,000.00 USD | 197,830.00 USD | 58,480.00 USD | 174,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.50` | 4,510,000.00 USD | 4,510,000.00 USD | 99,810.00 USD | 34,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.60` | 3,640,000.00 USD | 3,640,000.00 USD | 85,090.00 USD | 39,540.00 USD | 67,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.60` | 4,750,000.00 USD | 4,750,000.00 USD | 149,560.00 USD | 62,320.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.70` | 3,830,000.00 USD | 3,830,000.00 USD | 42,540.00 USD | 54,600.00 USD | 96,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.70` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 30,070.00 USD | 57,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.75` | 155.35 USD | 856.22 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `57.80` | 3,950,000.00 USD | 3,950,000.00 USD | 18,150.00 USD | 22,650.00 USD | 77,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.80` | 4,920,000.00 USD | 4,920,000.00 USD | 9,650.00 USD | 24,520.00 USD | 49,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.90` | 4,010,000.00 USD | 4,010,000.00 USD | 13,000.00 USD | 15,870.00 USD | 28,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.90` | 4,970,000.00 USD | 4,970,000.00 USD | 14,390.00 USD | 963.90 USD | 30,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.95` | 125.75 USD | 981.97 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.00` | 4,040,000.00 USD | 4,040,000.00 USD | 7,880.00 USD | 9,480.00 USD | 15,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.00` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 5,470.00 USD | 107,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.10` | 4,110,000.00 USD | 4,110,000.00 USD | 31,400.00 USD | 17,830.00 USD | 21,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.10` | 5,120,000.00 USD | 5,120,000.00 USD | 5,470.00 USD | 19,160.00 USD | 14,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.20` | 4,190,000.00 USD | 4,190,000.00 USD | 36,640.00 USD | 34,800.00 USD | 4,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.20` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 31,590.00 USD | 302.55 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.30` | 4,320,000.00 USD | 4,320,000.00 USD | 33,360.00 USD | 38,620.00 USD | 64,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.30` | 5,250,000.00 USD | 5,250,000.00 USD | 48,850.00 USD | 11,000.00 USD | 36,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.40` | 4,420,000.00 USD | 4,420,000.00 USD | 26,490.00 USD | 18,940.00 USD | 49,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.40` | 5,370,000.00 USD | 5,370,000.00 USD | 27,290.00 USD | 9,260.00 USD | 86,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.50` | 4,430,000.00 USD | 4,430,000.00 USD | 7,370.00 USD | 1,200.00 USD | 124.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.50` | 5,400,000.00 USD | 5,400,000.00 USD | 2,060.00 USD | 24,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.60` | 4,500,000.00 USD | 4,500,000.00 USD | 21,940.00 USD | 5,920.00 USD | 40,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.60` | 5,500,000.00 USD | 5,500,000.00 USD | 30,680.00 USD | 20,260.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.70` | 4,580,000.00 USD | 4,580,000.00 USD | 44,920.00 USD | 10,120.00 USD | 29,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.70` | 5,560,000.00 USD | 5,560,000.00 USD | 15,810.00 USD | 11,600.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.80` | 4,650,000.00 USD | 4,650,000.00 USD | 36,630.00 USD | 9,890.00 USD | 23,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.80` | 5,570,000.00 USD | 5,570,000.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `58.85` | 1,480.00 USD | 2,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.90` | 4,820,000.00 USD | 4,820,000.00 USD | 22,130.00 USD | 60,970.00 USD | 90,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.90` | 5,710,000.00 USD | 5,710,000.00 USD | 2,140.00 USD | 54,240.00 USD | 83,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.00` | 5,140,000.00 USD | 5,140,000.00 USD | 129,990.00 USD | 58,870.00 USD | 129,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.00` | 6,160,000.00 USD | 6,160,000.00 USD | 259,280.00 USD | 65,270.00 USD | 118,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.10` | 5,440,000.00 USD | 5,440,000.00 USD | 92,780.00 USD | 39,740.00 USD | 163,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.10` | 6,460,000.00 USD | 6,460,000.00 USD | 93,390.00 USD | 45,400.00 USD | 158,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.20` | 5,650,000.00 USD | 5,650,000.00 USD | 102,940.00 USD | 59,320.00 USD | 49,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.20` | 6,800,000.00 USD | 6,800,000.00 USD | 153,580.00 USD | 18,540.00 USD | 174,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.30` | 5,890,000.00 USD | 5,890,000.00 USD | 146,220.00 USD | 30,070.00 USD | 66,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.30` | 7,070,000.00 USD | 7,070,000.00 USD | 88,710.00 USD | 67,460.00 USD | 114,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.35` | 9,440.00 USD | 11,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.40` | 6,010,000.00 USD | 6,010,000.00 USD | 35,110.00 USD | 30,410.00 USD | 49,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.40` | 7,390,000.00 USD | 7,390,000.00 USD | 107,040.00 USD | 73,620.00 USD | 137,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.45` | 213.43 USD | 12,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.50` | 6,150,000.00 USD | 6,150,000.00 USD | 78,730.00 USD | 34,150.00 USD | 28,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.50` | 7,540,000.00 USD | 7,540,000.00 USD | 67,060.00 USD | 61,370.00 USD | 21,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.55` | 213.78 USD | 12,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.60` | 6,240,000.00 USD | 6,240,000.00 USD | 34,500.00 USD | 50,850.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.60` | 7,980,000.00 USD | 7,980,000.00 USD | 236,760.00 USD | 128,050.00 USD | 72,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.70` | 6,320,000.00 USD | 6,320,000.00 USD | 3,450.00 USD | 15,700.00 USD | 62,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.70` | 8,300,000.00 USD | 8,300,000.00 USD | 55,510.00 USD | 99,970.00 USD | 162,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.80` | 6,370,000.00 USD | 6,370,000.00 USD | 26,350.00 USD | 26,470.00 USD | 177.92 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.80` | 8,660,000.00 USD | 8,660,000.00 USD | 118,240.00 USD | 91,980.00 USD | 154,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.90` | 6,540,000.00 USD | 6,540,000.00 USD | 102,020.00 USD | 17,810.00 USD | 50,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.90` | 8,870,000.00 USD | 8,870,000.00 USD | 142,290.00 USD | 34,490.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.95` | 215.22 USD | 12,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.00` | 6,780,000.00 USD | 6,780,000.00 USD | 162,340.00 USD | 29,090.00 USD | 50,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.00` | 9,120,000.00 USD | 9,120,000.00 USD | 100,570.00 USD | 67,520.00 USD | 83,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.10` | 6,930,000.00 USD | 6,930,000.00 USD | 64,550.00 USD | 28,140.00 USD | 57,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.10` | 9,500,000.00 USD | 9,500,000.00 USD | 200,540.00 USD | 84,980.00 USD | 95,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.15` | 208,880.00 USD | 221,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.20` | 7,100,000.00 USD | 7,100,000.00 USD | 58,500.00 USD | 19,740.00 USD | 82,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.20` | 9,870,000.00 USD | 9,870,000.00 USD | 162,230.00 USD | 99,360.00 USD | 108,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.30` | 7,200,000.00 USD | 7,200,000.00 USD | 51,410.00 USD | 31,630.00 USD | 26,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.30` | 10,280,000.00 USD | 10,280,000.00 USD | 133,350.00 USD | 100,380.00 USD | 170,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.40` | 7,330,000.00 USD | 7,330,000.00 USD | 66,740.00 USD | 13,730.00 USD | 42,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.40` | 10,640,000.00 USD | 10,640,000.00 USD | 64,850.00 USD | 100,560.00 USD | 202,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.50` | 7,410,000.00 USD | 7,410,000.00 USD | 22,700.00 USD | 19,320.00 USD | 36,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.50` | 11,010,000.00 USD | 11,010,000.00 USD | 115,390.00 USD | 80,510.00 USD | 175,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.55` | 217.37 USD | 221,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.60` | 7,470,000.00 USD | 7,470,000.00 USD | 40,710.00 USD | 19,140.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.60` | 11,400,000.00 USD | 11,400,000.00 USD | 251,100.00 USD | 16,970.00 USD | 118,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.65` | 217.73 USD | 221,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.70` | 7,530,000.00 USD | 7,530,000.00 USD | 31,880.00 USD | 23,510.00 USD | 3,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.70` | 11,570,000.00 USD | 11,570,000.00 USD | 102,230.00 USD | 47,600.00 USD | 15,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.80` | 7,600,000.00 USD | 7,600,000.00 USD | 11,060.00 USD | 14,670.00 USD | 47,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.80` | 11,720,000.00 USD | 11,720,000.00 USD | 46,960.00 USD | 28,960.00 USD | 76,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.85` | 218.45 USD | 222,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.90` | 7,690,000.00 USD | 7,690,000.00 USD | 37,840.00 USD | 26,790.00 USD | 24,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.90` | 11,930,000.00 USD | 11,930,000.00 USD | 105,970.00 USD | 38,330.00 USD | 64,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.95` | 397.39 USD | 222,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.00` | 7,760,000.00 USD | 7,760,000.00 USD | 43,930.00 USD | 6,430.00 USD | 18,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 11,980,000.00 USD | 11,980,000.00 USD | 43,120.00 USD | 11,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.10` | 7,800,000.00 USD | 7,800,000.00 USD | 13,020.00 USD | 14,950.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 12,020,000.00 USD | 12,020,000.00 USD | 31,540.00 USD | 10,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.20` | 7,910,000.00 USD | 7,910,000.00 USD | 74,360.00 USD | 1,880.00 USD | 39,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.20` | 12,140,000.00 USD | 12,140,000.00 USD | 49,090.00 USD | 20,920.00 USD | 47,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.30` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 4,040.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.30` | 12,190,000.00 USD | 12,190,000.00 USD | 14,390.00 USD | 13,210.00 USD | 24,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.40` | 7,930,000.00 USD | 7,930,000.00 USD | 1,190.00 USD | 709.61 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.40` | 12,330,000.00 USD | 12,330,000.00 USD | 62,340.00 USD | 25,720.00 USD | 43,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.50` | 7,940,000.00 USD | 7,940,000.00 USD | 1,060.00 USD | 3,880.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.50` | 12,430,000.00 USD | 12,430,000.00 USD | 17,710.00 USD | 42,440.00 USD | 41,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.55` | 220.96 USD | 222,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.60` | 7,950,000.00 USD | 7,950,000.00 USD | 6,660.00 USD | 2,490.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.60` | 12,640,000.00 USD | 12,640,000.00 USD | 32,920.00 USD | 58,350.00 USD | 121,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.70` | 7,960,000.00 USD | 7,960,000.00 USD | 7,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.70` | 12,830,000.00 USD | 12,830,000.00 USD | 82,860.00 USD | 10,880.00 USD | 99,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.80` | 13,100,000.00 USD | 13,100,000.00 USD | 169,680.00 USD | 25,670.00 USD | 71,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.90` | 13,250,000.00 USD | 13,250,000.00 USD | 73,690.00 USD | 32,820.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.00` | 13,350,000.00 USD | 13,350,000.00 USD | 50,080.00 USD | 8,550.00 USD | 40,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `62.05` | 222.76 USD | 222,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `62.10` | 13,360,000.00 USD | 13,360,000.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.20` | 13,470,000.00 USD | 13,470,000.00 USD | 37,600.00 USD | 34,620.00 USD | 41,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.30` | 13,620,000.00 USD | 13,620,000.00 USD | 25,910.00 USD | 23,450.00 USD | 97,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.40` | 13,750,000.00 USD | 13,750,000.00 USD | 74,860.00 USD | 27,560.00 USD | 25,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.50` | 13,820,000.00 USD | 13,820,000.00 USD | 36,690.00 USD | 12,720.00 USD | 25,700.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `11.35` | 3,050,000.00 USD | 0.00 USD | 136.20 USD | `-79.46%` | `12.00` |
| `Live` | `Long` | `12.25` | 3,050,000.00 USD | 0.00 USD | 122.50 USD | `-77.83%` | `10.00` |
| `Live` | `Long` | `12.75` | 3,050,000.00 USD | 0.00 USD | 2,560.00 USD | `-76.92%` | `200.43` |
| `Live` | `Long` | `13.15` | 3,050,000.00 USD | 0.00 USD | 2,220.00 USD | `-76.20%` | `168.79` |
| `Live` | `Long` | `13.65` | 3,050,000.00 USD | 0.00 USD | 150.15 USD | `-75.29%` | `11.00` |
| `Live` | `Long` | `17.85` | 3,050,000.00 USD | 0.00 USD | 16,600.00 USD | `-67.69%` | `930.00` |
| `Live` | `Long` | `18.15` | 3,030,000.00 USD | 0.00 USD | 2,730.00 USD | `-67.15%` | `150.57` |
| `Live` | `Long` | `18.35` | 3,030,000.00 USD | 0.00 USD | 165.52 USD | `-66.79%` | `9.02` |
| `Live` | `Long` | `18.55` | 3,030,000.00 USD | 0.00 USD | 2,230.00 USD | `-66.43%` | `120.00` |
| `Live` | `Long` | `19.05` | 3,030,000.00 USD | 0.00 USD | 3,470.00 USD | `-65.52%` | `182.00` |
| `Live` | `Long` | `19.45` | 3,020,000.00 USD | 0.00 USD | 2,010.00 USD | `-64.80%` | `103.47` |
| `Live` | `Long` | `20.65` | 3,020,000.00 USD | 0.00 USD | 136.29 USD | `-62.62%` | `6.60` |
| `Live` | `Long` | `21.85` | 3,020,000.00 USD | 0.00 USD | 4,260.00 USD | `-60.45%` | `195.03` |
| `Live` | `Long` | `22.05` | 3,020,000.00 USD | 0.00 USD | 1,320.00 USD | `-60.09%` | `60.00` |
| `Live` | `Long` | `22.45` | 3,010,000.00 USD | 0.00 USD | 362.12 USD | `-59.37%` | `16.13` |
| `Live` | `Long` | `23.05` | 3,010,000.00 USD | 0.00 USD | 978.01 USD | `-58.28%` | `42.43` |
| `Live` | `Long` | `23.35` | 3,010,000.00 USD | 0.00 USD | 519.30 USD | `-57.74%` | `22.24` |
| `Live` | `Long` | `23.85` | 3,010,000.00 USD | 0.00 USD | 195.57 USD | `-56.83%` | `8.20` |
| `Live` | `Long` | `24.05` | 3,010,000.00 USD | 0.00 USD | 380.47 USD | `-56.47%` | `15.82` |
| `Live` | `Long` | `24.65` | 3,010,000.00 USD | 0.00 USD | 447.40 USD | `-55.38%` | `18.15` |
| `Live` | `Long` | `25.15` | 3,010,000.00 USD | 0.00 USD | 696.91 USD | `-54.48%` | `27.71` |
| `Live` | `Long` | `25.25` | 3,010,000.00 USD | 0.00 USD | 277,980.00 USD | `-54.30%` | `11,009.19` |
| `Live` | `Long` | `25.35` | 2,730,000.00 USD | 0.00 USD | 115,940.00 USD | `-54.12%` | `4,573.50` |
| `Live` | `Long` | `25.55` | 2,620,000.00 USD | 0.00 USD | 50,740.00 USD | `-53.76%` | `1,985.99` |
| `Live` | `Long` | `25.65` | 2,570,000.00 USD | 0.00 USD | 530.70 USD | `-53.57%` | `20.69` |
| `Live` | `Long` | `25.95` | 2,570,000.00 USD | 0.00 USD | 8,020.00 USD | `-53.03%` | `309.09` |
| `Live` | `Long` | `27.05` | 2,560,000.00 USD | 0.00 USD | 5,510.00 USD | `-51.04%` | `203.85` |
| `Live` | `Long` | `27.55` | 2,550,000.00 USD | 0.00 USD | 272.75 USD | `-50.14%` | `9.90` |
| `Live` | `Long` | `27.75` | 2,550,000.00 USD | 0.00 USD | 1,080.00 USD | `-49.77%` | `38.92` |
| `Live` | `Long` | `27.95` | 2,550,000.00 USD | 0.00 USD | 173.85 USD | `-49.41%` | `6.22` |
| `Live` | `Long` | `29.05` | 2,550,000.00 USD | 0.00 USD | 171.69 USD | `-47.42%` | `5.91` |
| `Live` | `Long` | `29.15` | 2,550,000.00 USD | 0.00 USD | 583.00 USD | `-47.24%` | `20.00` |
| `Live` | `Long` | `29.75` | 2,550,000.00 USD | 0.00 USD | 297,500.00 USD | `-46.15%` | `10,000.00` |
| `Live` | `Long` | `30.05` | 2,250,000.00 USD | 0.00 USD | 218.46 USD | `-45.61%` | `7.27` |
| `Live` | `Long` | `30.55` | 2,250,000.00 USD | 0.00 USD | 152.75 USD | `-44.71%` | `5.00` |
| `Live` | `Long` | `30.65` | 2,250,000.00 USD | 0.00 USD | 1,540.00 USD | `-44.52%` | `50.19` |
| `Live` | `Long` | `30.95` | 2,250,000.00 USD | 0.00 USD | 538.53 USD | `-43.98%` | `17.40` |
| `Live` | `Long` | `31.15` | 2,250,000.00 USD | 0.00 USD | 27,620.00 USD | `-43.62%` | `886.80` |
| `Live` | `Long` | `31.55` | 2,220,000.00 USD | 0.00 USD | 1,290.00 USD | `-42.90%` | `40.85` |
| `Live` | `Long` | `31.65` | 2,220,000.00 USD | 0.00 USD | 4,640.00 USD | `-42.71%` | `146.53` |
| `Live` | `Long` | `31.85` | 2,220,000.00 USD | 0.00 USD | 2,870.00 USD | `-42.35%` | `90.00` |
| `Live` | `Long` | `31.95` | 2,210,000.00 USD | 0.00 USD | 125.24 USD | `-42.17%` | `3.92` |
| `Live` | `Long` | `32.15` | 2,210,000.00 USD | 0.00 USD | 450.10 USD | `-41.81%` | `14.00` |
| `Live` | `Long` | `32.25` | 2,210,000.00 USD | 0.00 USD | 225.75 USD | `-41.63%` | `7.00` |
| `Live` | `Long` | `32.35` | 2,210,000.00 USD | 0.00 USD | 172.10 USD | `-41.45%` | `5.32` |
| `Live` | `Long` | `32.45` | 2,210,000.00 USD | 0.00 USD | 9,730.00 USD | `-41.27%` | `300.00` |
| `Live` | `Long` | `32.65` | 2,200,000.00 USD | 0.00 USD | 653.00 USD | `-40.90%` | `20.00` |
| `Live` | `Long` | `32.75` | 2,200,000.00 USD | 0.00 USD | 953.68 USD | `-40.72%` | `29.12` |
| `Live` | `Long` | `32.95` | 2,200,000.00 USD | 0.00 USD | 35,770.00 USD | `-40.36%` | `1,085.44` |
| `Live` | `Long` | `33.05` | 2,170,000.00 USD | 0.00 USD | 4,100.00 USD | `-40.18%` | `124.01` |
| `Live` | `Long` | `33.25` | 2,160,000.00 USD | 0.00 USD | 255.03 USD | `-39.82%` | `7.67` |
| `Live` | `Long` | `33.55` | 2,160,000.00 USD | 0.00 USD | 5,850.00 USD | `-39.28%` | `174.22` |
| `Live` | `Long` | `33.65` | 2,160,000.00 USD | 0.00 USD | 257.76 USD | `-39.10%` | `7.66` |
| `Live` | `Long` | `33.75` | 2,150,000.00 USD | 0.00 USD | 1,690.00 USD | `-38.91%` | `50.00` |
| `Live` | `Long` | `34.05` | 2,150,000.00 USD | 0.00 USD | 182.85 USD | `-38.37%` | `5.37` |
| `Live` | `Long` | `34.15` | 2,150,000.00 USD | 0.00 USD | 126.70 USD | `-38.19%` | `3.71` |
| `Live` | `Long` | `34.45` | 2,150,000.00 USD | 0.00 USD | 65,890.00 USD | `-37.65%` | `1,912.61` |
| `Live` | `Long` | `34.65` | 2,090,000.00 USD | 0.00 USD | 3,240.00 USD | `-37.29%` | `93.56` |
| `Live` | `Long` | `34.95` | 2,080,000.00 USD | 0.00 USD | 4,670.00 USD | `-36.74%` | `133.63` |
| `Live` | `Long` | `35.05` | 2,080,000.00 USD | 0.00 USD | 166.49 USD | `-36.56%` | `4.75` |
| `Live` | `Long` | `35.15` | 2,080,000.00 USD | 0.00 USD | 439.02 USD | `-36.38%` | `12.49` |
| `Live` | `Long` | `36.05` | 2,080,000.00 USD | 0.00 USD | 429.72 USD | `-34.75%` | `11.92` |
| `Live` | `Long` | `36.35` | 2,080,000.00 USD | 0.00 USD | 3,020.00 USD | `-34.21%` | `83.03` |
| `Live` | `Long` | `36.45` | 2,070,000.00 USD | 0.00 USD | 423.18 USD | `-34.03%` | `11.61` |
| `Live` | `Long` | `36.65` | 2,070,000.00 USD | 0.00 USD | 109.58 USD | `-33.67%` | `2.99` |
| `Live` | `Long` | `36.75` | 2,070,000.00 USD | 0.00 USD | 3,110.00 USD | `-33.48%` | `84.68` |
| `Live` | `Long` | `37.05` | 2,070,000.00 USD | 0.00 USD | 290.10 USD | `-32.94%` | `7.83` |
| `Live` | `Long` | `37.15` | 2,070,000.00 USD | 0.00 USD | 438.74 USD | `-32.76%` | `11.81` |
| `Live` | `Long` | `37.25` | 2,070,000.00 USD | 0.00 USD | 1,050.00 USD | `-32.58%` | `28.27` |
| `Live` | `Long` | `37.35` | 2,070,000.00 USD | 0.00 USD | 9,260.00 USD | `-32.40%` | `247.91` |
| `Live` | `Long` | `37.55` | 2,060,000.00 USD | 0.00 USD | 3,530.00 USD | `-32.04%` | `94.04` |
| `Live` | `Long` | `37.65` | 2,060,000.00 USD | 0.00 USD | 978.90 USD | `-31.86%` | `26.00` |
| `Live` | `Long` | `37.75` | 2,060,000.00 USD | 0.00 USD | 377.50 USD | `-31.67%` | `10.00` |
| `Live` | `Long` | `37.85` | 2,060,000.00 USD | 0.00 USD | 6,210.00 USD | `-31.49%` | `164.03` |
| `Live` | `Long` | `37.95` | 2,050,000.00 USD | 0.00 USD | 446.67 USD | `-31.31%` | `11.77` |
| `Live` | `Long` | `38.25` | 2,050,000.00 USD | 0.00 USD | 695.38 USD | `-30.77%` | `18.18` |
| `Live` | `Long` | `38.35` | 2,050,000.00 USD | 0.00 USD | 847.54 USD | `-30.59%` | `22.10` |
| `Live` | `Long` | `38.45` | 2,050,000.00 USD | 0.00 USD | 2,400.00 USD | `-30.41%` | `62.34` |
| `Live` | `Long` | `38.55` | 2,040,000.00 USD | 0.00 USD | 993.82 USD | `-30.23%` | `25.78` |
| `Live` | `Long` | `38.65` | 2,040,000.00 USD | 0.00 USD | 4,280.00 USD | `-30.05%` | `110.74` |
| `Live` | `Long` | `38.95` | 2,040,000.00 USD | 0.00 USD | 3,700.00 USD | `-29.50%` | `95.00` |
| `Live` | `Long` | `39.05` | 2,040,000.00 USD | 0.00 USD | 664,760.00 USD | `-29.32%` | `17,023.28` |
| `Live` | `Long` | `39.15` | 1,370,000.00 USD | 0.00 USD | 570.02 USD | `-29.14%` | `14.56` |
| `Live` | `Long` | `39.35` | 1,370,000.00 USD | 0.00 USD | 264.83 USD | `-28.78%` | `6.73` |
| `Live` | `Long` | `39.45` | 1,370,000.00 USD | 0.00 USD | 716.41 USD | `-28.60%` | `18.16` |
| `Live` | `Long` | `39.55` | 1,370,000.00 USD | 0.00 USD | 655.34 USD | `-28.42%` | `16.57` |
| `Live` | `Long` | `39.65` | 1,370,000.00 USD | 0.00 USD | 5,900.00 USD | `-28.24%` | `148.78` |
| `Live` | `Long` | `39.75` | 1,360,000.00 USD | 0.00 USD | 1,180.00 USD | `-28.05%` | `29.57` |
| `Live` | `Long` | `39.85` | 1,360,000.00 USD | 0.00 USD | 133.10 USD | `-27.87%` | `3.34` |
| `Live` | `Long` | `40.05` | 1,360,000.00 USD | 0.00 USD | 2,160.00 USD | `-27.51%` | `53.97` |
| `Live` | `Long` | `40.45` | 1,360,000.00 USD | 0.00 USD | 1,010.00 USD | `-26.79%` | `24.92` |
| `Live` | `Long` | `40.55` | 1,360,000.00 USD | 0.00 USD | 133.00 USD | `-26.61%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,360,000.00 USD | 0.00 USD | 274.39 USD | `-26.43%` | `6.75` |
| `Live` | `Long` | `40.85` | 1,360,000.00 USD | 0.00 USD | 6,340.00 USD | `-26.06%` | `155.23` |
| `Live` | `Long` | `40.95` | 1,350,000.00 USD | 0.00 USD | 509.01 USD | `-25.88%` | `12.43` |
| `Live` | `Long` | `41.05` | 1,350,000.00 USD | 0.00 USD | 396.54 USD | `-25.70%` | `9.66` |
| `Live` | `Long` | `41.15` | 1,350,000.00 USD | 0.00 USD | 5,430.00 USD | `-25.52%` | `131.94` |
| `Live` | `Long` | `41.25` | 1,350,000.00 USD | 0.00 USD | 14,850.00 USD | `-25.34%` | `359.91` |
| `Live` | `Long` | `41.45` | 1,330,000.00 USD | 0.00 USD | 644.96 USD | `-24.98%` | `15.56` |
| `Live` | `Long` | `41.85` | 1,330,000.00 USD | 0.00 USD | 9,210.00 USD | `-24.25%` | `220.00` |
| `Live` | `Long` | `41.95` | 1,320,000.00 USD | 0.00 USD | 1,050.00 USD | `-24.07%` | `24.93` |
| `Live` | `Long` | `42.05` | 1,320,000.00 USD | 0.00 USD | 201.00 USD | `-23.89%` | `4.78` |
| `Live` | `Long` | `42.15` | 1,320,000.00 USD | 0.00 USD | 66,300.00 USD | `-23.71%` | `1,572.94` |
| `Live` | `Long` | `42.25` | 1,250,000.00 USD | 0.00 USD | 35,410.00 USD | `-23.53%` | `838.00` |
| `Live` | `Long` | `42.45` | 1,220,000.00 USD | 0.00 USD | 302.67 USD | `-23.17%` | `7.13` |
| `Live` | `Long` | `42.55` | 1,220,000.00 USD | 0.00 USD | 339.97 USD | `-22.99%` | `7.99` |
| `Live` | `Long` | `42.65` | 1,220,000.00 USD | 0.00 USD | 1,910.00 USD | `-22.81%` | `44.75` |
| `Live` | `Long` | `42.75` | 1,220,000.00 USD | 0.00 USD | 3,800.00 USD | `-22.62%` | `88.83` |
| `Live` | `Long` | `42.85` | 1,210,000.00 USD | 0.00 USD | 5,800.00 USD | `-22.44%` | `135.38` |
| `Live` | `Long` | `42.95` | 1,210,000.00 USD | 0.00 USD | 2,000.00 USD | `-22.26%` | `46.65` |
| `Live` | `Long` | `43.05` | 1,200,000.00 USD | 0.00 USD | 9,080.00 USD | `-22.08%` | `211.00` |
| `Live` | `Long` | `43.15` | 1,190,000.00 USD | 0.00 USD | 1,580.00 USD | `-21.90%` | `36.59` |
| `Live` | `Long` | `43.25` | 1,190,000.00 USD | 0.00 USD | 121,210.00 USD | `-21.72%` | `2,802.44` |
| `Live` | `Long` | `43.35` | 1,070,000.00 USD | 0.00 USD | 5,700.00 USD | `-21.54%` | `131.46` |
| `Live` | `Long` | `43.45` | 1,070,000.00 USD | 0.00 USD | 1,040.00 USD | `-21.36%` | `23.86` |
| `Live` | `Long` | `43.65` | 1,060,000.00 USD | 0.00 USD | 426.02 USD | `-21.00%` | `9.76` |
| `Live` | `Long` | `43.75` | 1,060,000.00 USD | 0.00 USD | 21,880.00 USD | `-20.81%` | `500.00` |
| `Live` | `Long` | `43.85` | 1,040,000.00 USD | 0.00 USD | 801.14 USD | `-20.63%` | `18.27` |
| `Live` | `Long` | `44.05` | 1,040,000.00 USD | 0.00 USD | 3,500.00 USD | `-20.27%` | `79.49` |
| `Live` | `Long` | `44.15` | 1,040,000.00 USD | 0.00 USD | 2,380.00 USD | `-20.09%` | `53.99` |
| `Live` | `Long` | `44.35` | 1,040,000.00 USD | 0.00 USD | 84,440.00 USD | `-19.73%` | `1,903.87` |
| `Live` | `Long` | `44.45` | 951,530.00 USD | 0.00 USD | 5,720.00 USD | `-19.55%` | `128.71` |
| `Live` | `Long` | `44.55` | 945,800.00 USD | 0.00 USD | 842.44 USD | `-19.37%` | `18.91` |
| `Live` | `Long` | `44.75` | 944,960.00 USD | 0.00 USD | 4,230.00 USD | `-19.00%` | `94.55` |
| `Live` | `Long` | `44.85` | 940,730.00 USD | 0.00 USD | 134.55 USD | `-18.82%` | `3.00` |
| `Live` | `Long` | `44.95` | 940,600.00 USD | 0.00 USD | 3,960.00 USD | `-18.64%` | `88.18` |
| `Live` | `Long` | `45.05` | 936,630.00 USD | 0.00 USD | 4,830.00 USD | `-18.46%` | `107.31` |
| `Live` | `Long` | `45.15` | 931,800.00 USD | 0.00 USD | 8,710.00 USD | `-18.28%` | `193.00` |
| `Live` | `Long` | `45.25` | 923,080.00 USD | 0.00 USD | 3,180.00 USD | `-18.10%` | `70.37` |
| `Live` | `Long` | `45.35` | 919,900.00 USD | 0.00 USD | 3,540.00 USD | `-17.92%` | `78.02` |
| `Live` | `Long` | `45.45` | 916,360.00 USD | 0.00 USD | 23,940.00 USD | `-17.74%` | `526.65` |
| `Live` | `Long` | `45.55` | 892,430.00 USD | 0.00 USD | 12,060.00 USD | `-17.56%` | `264.81` |
| `Live` | `Long` | `45.65` | 880,360.00 USD | 0.00 USD | 42,180.00 USD | `-17.38%` | `924.03` |
| `Live` | `Long` | `45.95` | 838,180.00 USD | 0.00 USD | 76,920.00 USD | `-16.83%` | `1,673.93` |
| `Live` | `Long` | `46.05` | 761,260.00 USD | 0.00 USD | 706.41 USD | `-16.65%` | `15.34` |
| `Live` | `Long` | `46.35` | 760,560.00 USD | 0.00 USD | 561.76 USD | `-16.11%` | `12.12` |
| `Live` | `Long` | `46.55` | 760,000.00 USD | 0.00 USD | 24,930.00 USD | `-15.75%` | `535.66` |
| `Live` | `Long` | `46.65` | 735,060.00 USD | 0.00 USD | 3,980.00 USD | `-15.57%` | `85.41` |
| `Live` | `Long` | `46.85` | 731,080.00 USD | 0.00 USD | 358.40 USD | `-15.20%` | `7.65` |
| `Live` | `Long` | `46.95` | 730,720.00 USD | 0.00 USD | 158.22 USD | `-15.02%` | `3.37` |
| `Live` | `Long` | `47.05` | 730,560.00 USD | 0.00 USD | 2,140.00 USD | `-14.84%` | `45.57` |
| `Live` | `Long` | `47.15` | 728,420.00 USD | 0.00 USD | 1,980.00 USD | `-14.66%` | `42.07` |
| `Live` | `Long` | `47.25` | 726,430.00 USD | 0.00 USD | 9,030.00 USD | `-14.48%` | `191.21` |
| `Live` | `Long` | `47.35` | 717,400.00 USD | 0.00 USD | 43,920.00 USD | `-14.30%` | `927.56` |
| `Live` | `Long` | `47.45` | 673,480.00 USD | 0.00 USD | 2,590.00 USD | `-14.12%` | `54.54` |
| `Live` | `Long` | `47.55` | 670,890.00 USD | 0.00 USD | 4,450.00 USD | `-13.94%` | `93.69` |
| `Live` | `Long` | `47.75` | 666,430.00 USD | 0.00 USD | 47,750.00 USD | `-13.57%` | `1,000.00` |
| `Live` | `Long` | `48.05` | 618,680.00 USD | 0.00 USD | 381.04 USD | `-13.03%` | `7.93` |
| `Live` | `Long` | `48.15` | 618,300.00 USD | 0.00 USD | 1,690.00 USD | `-12.85%` | `35.03` |
| `Live` | `Long` | `48.25` | 616,620.00 USD | 0.00 USD | 110.49 USD | `-12.67%` | `2.29` |
| `Live` | `Long` | `48.55` | 616,510.00 USD | 0.00 USD | 10,020.00 USD | `-12.13%` | `206.43` |
| `Live` | `Long` | `48.65` | 606,480.00 USD | 0.00 USD | 273.90 USD | `-11.95%` | `5.63` |
| `Live` | `Long` | `48.75` | 606,210.00 USD | 0.00 USD | 333.94 USD | `-11.76%` | `6.85` |
| `Live` | `Long` | `48.95` | 605,880.00 USD | 0.00 USD | 252.58 USD | `-11.40%` | `5.16` |
| `Live` | `Long` | `49.05` | 605,620.00 USD | 0.00 USD | 1,580.00 USD | `-11.22%` | `32.25` |
| `Live` | `Long` | `49.15` | 604,040.00 USD | 0.00 USD | 5,740.00 USD | `-11.04%` | `116.83` |
| `Live` | `Long` | `49.35` | 598,300.00 USD | 0.00 USD | 24,210.00 USD | `-10.68%` | `490.66` |
| `Live` | `Long` | `49.45` | 574,090.00 USD | 0.00 USD | 419.34 USD | `-10.50%` | `8.48` |
| `Live` | `Long` | `49.55` | 573,670.00 USD | 0.00 USD | 18,010.00 USD | `-10.32%` | `363.57` |
| `Live` | `Long` | `49.65` | 555,650.00 USD | 0.00 USD | 73,260.00 USD | `-10.14%` | `1,475.52` |
| `Live` | `Long` | `49.75` | 482,390.00 USD | 0.00 USD | 3,180.00 USD | `-9.95%` | `63.85` |
| `Live` | `Long` | `49.95` | 479,220.00 USD | 0.00 USD | 19,920.00 USD | `-9.59%` | `398.70` |
| `Live` | `Long` | `50.05` | 459,300.00 USD | 0.00 USD | 1,820.00 USD | `-9.41%` | `36.43` |
| `Live` | `Long` | `50.25` | 457,480.00 USD | 0.00 USD | 102.51 USD | `-9.05%` | `2.04` |
| `Live` | `Long` | `50.35` | 457,370.00 USD | 0.00 USD | 1,140.00 USD | `-8.87%` | `22.67` |
| `Live` | `Long` | `50.45` | 456,230.00 USD | 0.00 USD | 4,720.00 USD | `-8.69%` | `93.64` |
| `Live` | `Long` | `50.55` | 451,510.00 USD | 0.00 USD | 84,100.00 USD | `-8.51%` | `1,663.61` |
| `Live` | `Long` | `50.75` | 367,410.00 USD | 0.00 USD | 9,650.00 USD | `-8.14%` | `190.07` |
| `Live` | `Long` | `50.95` | 357,770.00 USD | 0.00 USD | 431.55 USD | `-7.78%` | `8.47` |
| `Live` | `Long` | `51.15` | 357,340.00 USD | 0.00 USD | 219,370.00 USD | `-7.42%` | `4,288.79` |
| `Live` | `Long` | `51.25` | 137,960.00 USD | 0.00 USD | 202.44 USD | `-7.24%` | `3.95` |
| `Live` | `Long` | `51.35` | 137,760.00 USD | 0.00 USD | 453.93 USD | `-7.06%` | `8.84` |
| `Live` | `Long` | `51.45` | 137,310.00 USD | 0.00 USD | 27,210.00 USD | `-6.88%` | `528.81` |
| `Live` | `Long` | `51.55` | 110,100.00 USD | 0.00 USD | 551.07 USD | `-6.70%` | `10.69` |
| `Live` | `Long` | `51.65` | 109,550.00 USD | 0.00 USD | 9,100.00 USD | `-6.52%` | `176.09` |
| `Live` | `Long` | `51.75` | 100,450.00 USD | 0.00 USD | 6,480.00 USD | `-6.33%` | `125.17` |
| `Live` | `Long` | `51.85` | 93,980.00 USD | 0.00 USD | 13,680.00 USD | `-6.15%` | `263.89` |
| `Live` | `Long` | `51.95` | 80,290.00 USD | 0.00 USD | 13,950.00 USD | `-5.97%` | `268.48` |
| `Live` | `Long` | `52.05` | 66,350.00 USD | 0.00 USD | 2,860.00 USD | `-5.79%` | `55.00` |
| `Live` | `Long` | `52.15` | 63,480.00 USD | 0.00 USD | 1,900.00 USD | `-5.61%` | `36.36` |
| `Live` | `Long` | `52.25` | 61,590.00 USD | 0.00 USD | 4,930.00 USD | `-5.43%` | `94.33` |
| `Live` | `Long` | `52.35` | 56,660.00 USD | 0.00 USD | 134.02 USD | `-5.25%` | `2.56` |
| `Live` | `Long` | `52.45` | 56,530.00 USD | 0.00 USD | 5,820.00 USD | `-5.07%` | `110.91` |
| `Live` | `Long` | `52.55` | 50,710.00 USD | 0.00 USD | 8,700.00 USD | `-4.89%` | `165.49` |
| `Live` | `Long` | `52.65` | 42,010.00 USD | 0.00 USD | 1,050.00 USD | `-4.71%` | `20.00` |
| `Live` | `Long` | `52.75` | 40,960.00 USD | 0.00 USD | 30,280.00 USD | `-4.52%` | `574.00` |
| `Live` | `Long` | `52.85` | 10,680.00 USD | 0.00 USD | 5,950.00 USD | `-4.34%` | `112.64` |
| `Live` | `Long` | `52.95` | 4,730.00 USD | 0.00 USD | 531.09 USD | `-4.16%` | `10.03` |
| `Live` | `Long` | `53.05` | 4,200.00 USD | 0.00 USD | 202.12 USD | `-3.98%` | `3.81` |
| `Live` | `Long` | `53.15` | 3,990.00 USD | 0.00 USD | 2,030.00 USD | `-3.80%` | `38.15` |
| `Live` | `Long` | `53.25` | 1,970.00 USD | 0.00 USD | 1,030.00 USD | `-3.62%` | `19.25` |
| `Live` | `Long` | `53.35` | 941.09 USD | 0.00 USD | 941.09 USD | `-3.44%` | `17.64` |
| `Live` | `Short` | `57.75` | 155.35 USD | 155.35 USD | 0.00 USD | `+4.52%` | `2.69` |
| `Live` | `Short` | `57.95` | 281.10 USD | 125.75 USD | 0.00 USD | `+4.89%` | `2.17` |
| `Live` | `Short` | `58.85` | 1,760.00 USD | 1,480.00 USD | 0.00 USD | `+6.52%` | `25.13` |
| `Live` | `Short` | `59.25` | 1,970.00 USD | 213.89 USD | 0.00 USD | `+7.24%` | `3.61` |
| `Live` | `Short` | `59.35` | 11,420.00 USD | 9,440.00 USD | 0.00 USD | `+7.42%` | `159.09` |
| `Live` | `Short` | `59.45` | 11,630.00 USD | 214.02 USD | 0.00 USD | `+7.60%` | `3.60` |
| `Live` | `Short` | `59.65` | 11,850.00 USD | 215.34 USD | 0.00 USD | `+7.96%` | `3.61` |
| `Live` | `Short` | `60.15` | 220,730.00 USD | 208,880.00 USD | 0.00 USD | `+8.87%` | `3,472.67` |
| `Live` | `Short` | `60.45` | 220,960.00 USD | 230.92 USD | 0.00 USD | `+9.41%` | `3.82` |
| `Live` | `Short` | `60.55` | 221,390.00 USD | 435.96 USD | 0.00 USD | `+9.59%` | `7.20` |
| `Live` | `Short` | `60.75` | 221,610.00 USD | 218.70 USD | 0.00 USD | `+9.95%` | `3.60` |
| `Live` | `Short` | `60.95` | 222,010.00 USD | 397.39 USD | 0.00 USD | `+10.32%` | `6.52` |
| `Live` | `Short` | `61.55` | 222,230.00 USD | 222.20 USD | 0.00 USD | `+11.40%` | `3.61` |
| `Live` | `Short` | `62.05` | 222,450.00 USD | 223.38 USD | 0.00 USD | `+12.31%` | `3.60` |
| `Live` | `Short` | `62.95` | 222,590.00 USD | 138.49 USD | 0.00 USD | `+13.94%` | `2.20` |
| `Live` | `Short` | `63.45` | 225,950.00 USD | 3,350.00 USD | 0.00 USD | `+14.84%` | `52.83` |
| `Live` | `Short` | `63.55` | 234,120.00 USD | 8,180.00 USD | 0.00 USD | `+15.02%` | `128.67` |
| `Live` | `Short` | `67.05` | 234,240.00 USD | 121.36 USD | 0.00 USD | `+21.36%` | `1.81` |
| `Live` | `Short` | `67.85` | 234,950.00 USD | 709.03 USD | 0.00 USD | `+22.81%` | `10.45` |
| `Live` | `Short` | `70.25` | 275,560.00 USD | 40,610.00 USD | 0.00 USD | `+27.15%` | `578.10` |
| `Live` | `Short` | `76.35` | 283,950.00 USD | 8,380.00 USD | 0.00 USD | `+38.19%` | `109.80` |
| `Live` | `Short` | `77.65` | 284,060.00 USD | 111.04 USD | 0.00 USD | `+40.54%` | `1.43` |
| `Live` | `Short` | `77.75` | 862,520.00 USD | 578,460.00 USD | 0.00 USD | `+40.72%` | `7,440.05` |
| `Live` | `Short` | `77.85` | 863,130.00 USD | 602.56 USD | 0.00 USD | `+40.90%` | `7.74` |
| `Live` | `Short` | `79.95` | 866,320.00 USD | 3,200.00 USD | 0.00 USD | `+44.71%` | `40.00` |
| `Live` | `Short` | `80.75` | 866,970.00 USD | 646.00 USD | 0.00 USD | `+46.15%` | `8.00` |
| `Live` | `Short` | `81.05` | 885,970.00 USD | 19,000.00 USD | 0.00 USD | `+46.70%` | `234.42` |
| `Live` | `Short` | `81.55` | 886,090.00 USD | 123.96 USD | 0.00 USD | `+47.60%` | `1.52` |
| `Live` | `Short` | `81.75` | 886,830.00 USD | 741.47 USD | 0.00 USD | `+47.96%` | `9.07` |
| `Live` | `Short` | `82.25` | 887,710.00 USD | 874.32 USD | 0.00 USD | `+48.87%` | `10.63` |
| `Live` | `Short` | `82.75` | 887,920.00 USD | 214.32 USD | 0.00 USD | `+49.77%` | `2.59` |
| `Live` | `Short` | `83.05` | 890,660.00 USD | 2,740.00 USD | 0.00 USD | `+50.32%` | `33.00` |
| `Live` | `Short` | `84.25` | 913,140.00 USD | 22,480.00 USD | 0.00 USD | `+52.49%` | `266.81` |
| `Live` | `Short` | `89.55` | 913,240.00 USD | 100.30 USD | 0.00 USD | `+62.08%` | `1.12` |
| `Live` | `Short` | `92.55` | 913,360.00 USD | 122.17 USD | 0.00 USD | `+67.51%` | `1.32` |
| `Live` | `Short` | `98.15` | 915,820.00 USD | 2,450.00 USD | 0.00 USD | `+77.65%` | `25.00` |
| `Live` | `Short` | `98.35` | 915,980.00 USD | 166.21 USD | 0.00 USD | `+78.01%` | `1.69` |
| `Live` | `Short` | `103.55` | 947,050.00 USD | 31,070.00 USD | 0.00 USD | `+87.42%` | `300.00` |
| `Live` | `Short` | `104.25` | 947,260.00 USD | 213.71 USD | 0.00 USD | `+88.69%` | `2.05` |
| `Live` | `Short` | `104.85` | 949,580.00 USD | 2,320.00 USD | 0.00 USD | `+89.77%` | `22.13` |
| `Live` | `Short` | `104.95` | 1,300,000.00 USD | 354,100.00 USD | 0.00 USD | `+89.95%` | `3,374.01` |
| `Live` | `Short` | `106.75` | 1,310,000.00 USD | 1,620.00 USD | 0.00 USD | `+93.21%` | `15.16` |
| `Live` | `Short` | `106.85` | 1,310,000.00 USD | 1,860.00 USD | 0.00 USD | `+93.39%` | `17.43` |
| `Live` | `Short` | `107.25` | 1,310,000.00 USD | 199.48 USD | 0.00 USD | `+94.12%` | `1.86` |
| `Live` | `Short` | `108.05` | 1,310,000.00 USD | 6,470.00 USD | 0.00 USD | `+95.57%` | `59.91` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 840,310.00 USD | 0.00 USD | 392.18 USD | `-63.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 839,910.00 USD | 0.00 USD | 2,310.00 USD | `-60.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 837,610.00 USD | 0.00 USD | 806.86 USD | `-54.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 836,800.00 USD | 0.00 USD | 1,560.00 USD | `-54.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 835,240.00 USD | 0.00 USD | 410.25 USD | `-50.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 834,830.00 USD | 0.00 USD | 281.57 USD | `-45.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 834,550.00 USD | 0.00 USD | 36,050.00 USD | `-34.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 798,500.00 USD | 0.00 USD | 37,550.00 USD | `-32.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 760,950.00 USD | 0.00 USD | 447.01 USD | `-31.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.35` | 760,500.00 USD | 0.00 USD | 73,350.00 USD | `-30.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 687,150.00 USD | 0.00 USD | 40,560.00 USD | `-29.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 646,600.00 USD | 0.00 USD | 489.57 USD | `-28.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 646,110.00 USD | 0.00 USD | 1,180.00 USD | `-27.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 644,930.00 USD | 0.00 USD | 9,840.00 USD | `-27.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 635,090.00 USD | 0.00 USD | 2,060.00 USD | `-25.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.05` | 633,040.00 USD | 0.00 USD | 2,060.00 USD | `-25.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 630,970.00 USD | 0.00 USD | 2,960.00 USD | `-24.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 628,020.00 USD | 0.00 USD | 4,010.00 USD | `-23.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.65` | 624,000.00 USD | 0.00 USD | 3,000.00 USD | `-22.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 621,000.00 USD | 0.00 USD | 5,680.00 USD | `-22.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 615,320.00 USD | 0.00 USD | 672.22 USD | `-20.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.35` | 614,650.00 USD | 0.00 USD | 329,970.00 USD | `-19.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 284,680.00 USD | 0.00 USD | 569.85 USD | `-19.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 284,110.00 USD | 0.00 USD | 223.20 USD | `-19.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 283,890.00 USD | 0.00 USD | 391.13 USD | `-19.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 283,500.00 USD | 0.00 USD | 7,080.00 USD | `-18.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 276,420.00 USD | 0.00 USD | 1,370.00 USD | `-17.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 275,060.00 USD | 0.00 USD | 553.80 USD | `-16.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.35` | 274,500.00 USD | 0.00 USD | 2,970.00 USD | `-16.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.45` | 271,530.00 USD | 0.00 USD | 3,080.00 USD | `-15.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 268,450.00 USD | 0.00 USD | 14,000.00 USD | `-15.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 254,460.00 USD | 0.00 USD | 158.56 USD | `-14.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 254,300.00 USD | 0.00 USD | 373.28 USD | `-14.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 253,930.00 USD | 0.00 USD | 849.46 USD | `-14.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 253,080.00 USD | 0.00 USD | 1,150.00 USD | `-13.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 251,930.00 USD | 0.00 USD | 129.25 USD | `-13.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.15` | 251,800.00 USD | 0.00 USD | 303.35 USD | `-12.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 251,490.00 USD | 0.00 USD | 1,740.00 USD | `-11.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 249,750.00 USD | 0.00 USD | 981.00 USD | `-11.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.35` | 248,770.00 USD | 0.00 USD | 817.24 USD | `-10.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 247,960.00 USD | 0.00 USD | 237.85 USD | `-10.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.55` | 247,720.00 USD | 0.00 USD | 879.51 USD | `-10.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.85` | 246,840.00 USD | 0.00 USD | 108.17 USD | `-9.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 246,730.00 USD | 0.00 USD | 298.20 USD | `-9.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 246,430.00 USD | 0.00 USD | 34,670.00 USD | `-9.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 211,760.00 USD | 0.00 USD | 6,410.00 USD | `-9.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 205,340.00 USD | 0.00 USD | 459.70 USD | `-8.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 204,880.00 USD | 0.00 USD | 236.57 USD | `-8.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 204,650.00 USD | 0.00 USD | 1,020.00 USD | `-7.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 203,630.00 USD | 0.00 USD | 439.89 USD | `-7.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.45` | 203,190.00 USD | 0.00 USD | 204.26 USD | `-6.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 202,980.00 USD | 0.00 USD | 11,560.00 USD | `-6.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.85` | 191,420.00 USD | 0.00 USD | 106.29 USD | `-6.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.95` | 191,320.00 USD | 0.00 USD | 8,700.00 USD | `-5.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 182,610.00 USD | 0.00 USD | 27,140.00 USD | `-5.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.25` | 155,480.00 USD | 0.00 USD | 140.03 USD | `-5.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 155,340.00 USD | 0.00 USD | 18,390.00 USD | `-4.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 136,940.00 USD | 0.00 USD | 5,460.00 USD | `-4.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 131,490.00 USD | 0.00 USD | 271.13 USD | `-4.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.85` | 131,210.00 USD | 0.00 USD | 2,840.00 USD | `-4.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 128,370.00 USD | 0.00 USD | 115.43 USD | `-4.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 128,260.00 USD | 0.00 USD | 9,240.00 USD | `-3.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 119,010.00 USD | 0.00 USD | 2,660.00 USD | `-3.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.25` | 116,360.00 USD | 0.00 USD | 881.82 USD | `-3.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.35` | 115,470.00 USD | 0.00 USD | 25,130.00 USD | `-3.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 90,350.00 USD | 0.00 USD | 566.57 USD | `-3.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 89,780.00 USD | 0.00 USD | 5,950.00 USD | `-3.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 83,830.00 USD | 0.00 USD | 1,370.00 USD | `-2.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.75` | 82,460.00 USD | 0.00 USD | 52,980.00 USD | `-2.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 29,480.00 USD | 0.00 USD | 462.03 USD | `-2.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 29,020.00 USD | 0.00 USD | 6,010.00 USD | `-2.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.15` | 23,010.00 USD | 0.00 USD | 398.54 USD | `-1.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 22,610.00 USD | 0.00 USD | 3,090.00 USD | `-1.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 19,520.00 USD | 0.00 USD | 958.73 USD | `-1.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.45` | 18,560.00 USD | 0.00 USD | 144.29 USD | `-1.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.55` | 18,420.00 USD | 0.00 USD | 788.25 USD | `-1.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.65` | 17,630.00 USD | 0.00 USD | 13,660.00 USD | `-1.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.75` | 3,970.00 USD | 0.00 USD | 198.74 USD | `-0.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 3,770.00 USD | 0.00 USD | 398.21 USD | `-0.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.95` | 3,370.00 USD | 0.00 USD | 909.97 USD | `-0.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 2,460.00 USD | 0.00 USD | 550.50 USD | `-0.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.15` | 1,910.00 USD | 0.00 USD | 596.17 USD | `-0.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.25` | 1,310.00 USD | 0.00 USD | 1,310.00 USD | `+0.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.35` | 198.71 USD | 198.71 USD | 0.00 USD | `+0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.45` | 1,390.00 USD | 1,190.00 USD | 0.00 USD | `+0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.55` | 1,550.00 USD | 156.65 USD | 0.00 USD | `+0.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.65` | 2,110.00 USD | 556.50 USD | 0.00 USD | `+0.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.75` | 2,500.00 USD | 398.06 USD | 0.00 USD | `+0.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.85` | 3,300.00 USD | 797.54 USD | 0.00 USD | `+1.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.95` | 3,490.00 USD | 193.03 USD | 0.00 USD | `+1.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.05` | 4,130.00 USD | 632.24 USD | 0.00 USD | `+1.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.15` | 4,320.00 USD | 197.65 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.25` | 4,530.00 USD | 204.19 USD | 0.00 USD | `+1.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.35` | 4,940.00 USD | 406.85 USD | 0.00 USD | `+1.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.45` | 5,340.00 USD | 407.57 USD | 0.00 USD | `+2.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.55` | 5,550.00 USD | 204.15 USD | 0.00 USD | `+2.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.65` | 6,080.00 USD | 529.11 USD | 0.00 USD | `+2.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.75` | 6,280.00 USD | 203.73 USD | 0.00 USD | `+2.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.85` | 6,480.00 USD | 204.09 USD | 0.00 USD | `+2.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.95` | 7,250.00 USD | 765.41 USD | 0.00 USD | `+3.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.05` | 7,850.00 USD | 596.17 USD | 0.00 USD | `+3.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.15` | 8,050.00 USD | 204.03 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.25` | 9,490.00 USD | 1,440.00 USD | 0.00 USD | `+3.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.35` | 9,700.00 USD | 207.03 USD | 0.00 USD | `+3.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.45` | 10,040.00 USD | 344.70 USD | 0.00 USD | `+3.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.55` | 10,260.00 USD | 218.69 USD | 0.00 USD | `+4.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.65` | 10,380.00 USD | 118.18 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.75` | 10,500.00 USD | 119.54 USD | 0.00 USD | `+4.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 11,240.00 USD | 747.68 USD | 0.00 USD | `+5.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 11,440.00 USD | 200.04 USD | 0.00 USD | `+5.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 11,650.00 USD | 200.96 USD | 0.00 USD | `+5.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 11,770.00 USD | 123.70 USD | 0.00 USD | `+5.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 12,370.00 USD | 601.45 USD | 0.00 USD | `+5.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 12,590.00 USD | 223.66 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 13,090.00 USD | 491.15 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 16,030.00 USD | 2,940.00 USD | 0.00 USD | `+6.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 16,160.00 USD | 129.69 USD | 0.00 USD | `+6.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 20,960.00 USD | 4,800.00 USD | 0.00 USD | `+6.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 22,240.00 USD | 1,280.00 USD | 0.00 USD | `+7.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.25` | 22,450.00 USD | 210.34 USD | 0.00 USD | `+7.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 22,910.00 USD | 461.74 USD | 0.00 USD | `+7.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 23,070.00 USD | 159.92 USD | 0.00 USD | `+7.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 23,790.00 USD | 724.75 USD | 0.00 USD | `+7.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 23,950.00 USD | 158.00 USD | 0.00 USD | `+8.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 24,120.00 USD | 171.14 USD | 0.00 USD | `+8.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 24,670.00 USD | 551.00 USD | 0.00 USD | `+9.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.45` | 24,830.00 USD | 155.36 USD | 0.00 USD | `+9.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 25,710.00 USD | 878.58 USD | 0.00 USD | `+9.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 27,090.00 USD | 1,390.00 USD | 0.00 USD | `+9.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 28,080.00 USD | 986.99 USD | 0.00 USD | `+10.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 28,760.00 USD | 674.72 USD | 0.00 USD | `+10.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 31,120.00 USD | 2,360.00 USD | 0.00 USD | `+10.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 31,240.00 USD | 125.56 USD | 0.00 USD | `+10.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 34,840.00 USD | 3,600.00 USD | 0.00 USD | `+11.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 35,480.00 USD | 643.20 USD | 0.00 USD | `+11.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 35,610.00 USD | 130.31 USD | 0.00 USD | `+12.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.35` | 36,710.00 USD | 1,100.00 USD | 0.00 USD | `+12.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.55` | 37,960.00 USD | 1,250.00 USD | 0.00 USD | `+13.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 38,680.00 USD | 716.72 USD | 0.00 USD | `+13.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 38,910.00 USD | 231.39 USD | 0.00 USD | `+14.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 39,540.00 USD | 630.87 USD | 0.00 USD | `+14.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 40,250.00 USD | 703.97 USD | 0.00 USD | `+14.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 40,910.00 USD | 668.13 USD | 0.00 USD | `+14.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 51,340.00 USD | 10,420.00 USD | 0.00 USD | `+15.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 51,890.00 USD | 555.03 USD | 0.00 USD | `+15.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 52,420.00 USD | 531.62 USD | 0.00 USD | `+15.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.35` | 53,090.00 USD | 664.09 USD | 0.00 USD | `+16.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.45` | 53,750.00 USD | 665.12 USD | 0.00 USD | `+16.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 53,960.00 USD | 202.69 USD | 0.00 USD | `+16.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 54,250.00 USD | 298.04 USD | 0.00 USD | `+17.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 54,360.00 USD | 102.13 USD | 0.00 USD | `+17.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 54,900.00 USD | 540.09 USD | 0.00 USD | `+17.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 55,000.00 USD | 100.79 USD | 0.00 USD | `+18.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 55,260.00 USD | 262.20 USD | 0.00 USD | `+18.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 55,630.00 USD | 371.49 USD | 0.00 USD | `+19.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 56,330.00 USD | 696.17 USD | 0.00 USD | `+19.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 56,860.00 USD | 534.00 USD | 0.00 USD | `+20.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 67,940.00 USD | 11,080.00 USD | 0.00 USD | `+21.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 74,640.00 USD | 6,710.00 USD | 0.00 USD | `+21.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.05` | 77,010.00 USD | 2,360.00 USD | 0.00 USD | `+23.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 81,870.00 USD | 4,860.00 USD | 0.00 USD | `+23.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 82,070.00 USD | 204.48 USD | 0.00 USD | `+25.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.65` | 600,270.00 USD | 518,200.00 USD | 0.00 USD | `+26.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 601,080.00 USD | 810.02 USD | 0.00 USD | `+26.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 920,980.00 USD | 319,890.00 USD | 0.00 USD | `+26.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 921,150.00 USD | 170.04 USD | 0.00 USD | `+28.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 926,910.00 USD | 5,770.00 USD | 0.00 USD | `+28.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 927,180.00 USD | 269.28 USD | 0.00 USD | `+28.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 927,470.00 USD | 291.40 USD | 0.00 USD | `+30.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 934,690.00 USD | 7,220.00 USD | 0.00 USD | `+30.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 934,850.00 USD | 156.78 USD | 0.00 USD | `+30.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 938,070.00 USD | 3,220.00 USD | 0.00 USD | `+31.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 938,480.00 USD | 411.14 USD | 0.00 USD | `+33.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 1,060,000.00 USD | 123,190.00 USD | 0.00 USD | `+34.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 1,060,000.00 USD | 1,020.00 USD | 0.00 USD | `+34.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.75` | 1,060,000.00 USD | 811.04 USD | 0.00 USD | `+35.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 1,060,000.00 USD | 104.93 USD | 0.00 USD | `+35.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 1,060,000.00 USD | 133.59 USD | 0.00 USD | `+35.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 1,060,000.00 USD | 402.59 USD | 0.00 USD | `+36.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.85` | 1,060,000.00 USD | 308.71 USD | 0.00 USD | `+37.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 1,060,000.00 USD | 315.18 USD | 0.00 USD | `+39.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 1,120,000.00 USD | 59,310.00 USD | 0.00 USD | `+42.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 1,130,000.00 USD | 3,160.00 USD | 0.00 USD | `+43.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.35` | 1,130,000.00 USD | 5,260.00 USD | 0.00 USD | `+43.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 1,140,000.00 USD | 5,690.00 USD | 0.00 USD | `+44.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 1,170,000.00 USD | 36,590.00 USD | 0.00 USD | `+44.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 1,180,000.00 USD | 433.89 USD | 0.00 USD | `+46.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 1,180,000.00 USD | 172.64 USD | 0.00 USD | `+46.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 1,180,000.00 USD | 164.10 USD | 0.00 USD | `+48.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 1,180,000.00 USD | 546.81 USD | 0.00 USD | `+49.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 1,180,000.00 USD | 2,300.00 USD | 0.00 USD | `+52.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 1,190,000.00 USD | 12,070.00 USD | 0.00 USD | `+53.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.05` | 1,210,000.00 USD | 20,230.00 USD | 0.00 USD | `+57.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 1,210,000.00 USD | 1,580.00 USD | 0.00 USD | `+59.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 1,250,000.00 USD | 37,000.00 USD | 0.00 USD | `+59.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 1,250,000.00 USD | 473.21 USD | 0.00 USD | `+61.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 1,250,000.00 USD | 422.99 USD | 0.00 USD | `+61.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 1,250,000.00 USD | 1,630.00 USD | 0.00 USD | `+61.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 1,260,000.00 USD | 4,870.00 USD | 0.00 USD | `+62.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 1,260,000.00 USD | 481.55 USD | 0.00 USD | `+65.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 1,260,000.00 USD | 1,330.00 USD | 0.00 USD | `+66.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 1,260,000.00 USD | 281.21 USD | 0.00 USD | `+70.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,520,000.00 USD | 266,140.00 USD | 0.00 USD | `+72.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,530,000.00 USD | 3,400.00 USD | 0.00 USD | `+72.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,550,000.00 USD | 21,930.00 USD | 0.00 USD | `+73.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,550,000.00 USD | 294.15 USD | 0.00 USD | `+77.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 1,570,000.00 USD | 15,380.00 USD | 0.00 USD | `+79.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,570,000.00 USD | 3,660.00 USD | 0.00 USD | `+81.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,570,000.00 USD | 306.15 USD | 0.00 USD | `+84.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,570,000.00 USD | 936.72 USD | 0.00 USD | `+86.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,570,000.00 USD | 2,920.00 USD | 0.00 USD | `+86.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,570,000.00 USD | 324.15 USD | 0.00 USD | `+95.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 1,570,000.00 USD | 123.23 USD | 0.00 USD | `+97.38%` | `TACTICAL (Retail Cluster)` |

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
| `7D` | `49.40` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD |
| `7D` | `49.50` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 2,830.00 USD | 7,770.00 USD | 0.00 USD |
| `7D` | `49.60` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD |
| `1D` | `49.70` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 11,870.00 USD | 17,470.00 USD | 24,260.00 USD |
| `7D` | `49.70` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 12,090.00 USD | 0.00 USD | 5,410.00 USD |
| `1D` | `49.80` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 6,420.00 USD | 6,910.00 USD | 21,860.00 USD |
| `7D` | `49.80` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 9,930.00 USD | 8,220.00 USD | 0.00 USD |
| `1D` | `49.90` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 24,520.00 USD | 13,560.00 USD | 24,800.00 USD |
| `7D` | `49.90` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 45,030.00 USD | 13,920.00 USD | 4,700.00 USD |
| `1D` | `50.00` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 13,200.00 USD | 16,830.00 USD | 40,730.00 USD |
| `7D` | `50.00` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 22,100.00 USD | 19,810.00 USD | 24,920.00 USD |
| `1D` | `50.10` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 3,780.00 USD | 4,040.00 USD | 7,600.00 USD |
| `7D` | `50.10` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 363.50 USD | 682.90 USD | 8,340.00 USD |
| `1D` | `50.20` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 177.10 USD | 709.61 USD | 5,230.00 USD |
| `7D` | `50.20` | 7,880,000.00 USD | 0.00 USD | 7,880,000.00 USD | 6,960.00 USD | 500.40 USD | 42,940.00 USD |
| `1D` | `50.30` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 171.03 USD | 3,880.00 USD | 2,500.00 USD |
| `7D` | `50.30` | 7,830,000.00 USD | 0.00 USD | 7,830,000.00 USD | 16,270.00 USD | 10,780.00 USD | 7,240.00 USD |
| `1D` | `50.40` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 8,260.00 USD | 11,890.00 USD | 1,150.00 USD |
| `7D` | `50.40` | 7,790,000.00 USD | 0.00 USD | 7,790,000.00 USD | 28,280.00 USD | 26,580.00 USD | 33,450.00 USD |
| `1D` | `50.50` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 8,910.00 USD | 8,790.00 USD | 10,530.00 USD |
| `7D` | `50.50` | 7,700,000.00 USD | 0.00 USD | 7,700,000.00 USD | 32,490.00 USD | 6,790.00 USD | 44,380.00 USD |
| `1D` | `50.60` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 7,330.00 USD | 3,440.00 USD | 10,850.00 USD |
| `7D` | `50.60` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 67,580.00 USD | 21,530.00 USD | 31,730.00 USD |
| `1D` | `50.70` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 8,170.00 USD | 2,300.00 USD | 11,770.00 USD |
| `7D` | `50.70` | 7,500,000.00 USD | 0.00 USD | 7,500,000.00 USD | 65,920.00 USD | 32,820.00 USD | 41,580.00 USD |
| `1D` | `50.80` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 12,550.00 USD | 3,100.00 USD | 8,280.00 USD |
| `7D` | `50.80` | 7,360,000.00 USD | 0.00 USD | 7,360,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD |
| `1D` | `50.90` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 826.24 USD | 260.05 USD | 8,390.00 USD |
| `7D` | `50.90` | 7,260,000.00 USD | 0.00 USD | 7,260,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD |
| `1D` | `51.00` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 5,040.00 USD | 0.00 USD | 430.77 USD |
| `7D` | `51.00` | 7,010,000.00 USD | 0.00 USD | 7,010,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `51.10` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 9,210.00 USD | 6,650.00 USD | 0.00 USD |
| `7D` | `51.10` | 6,880,000.00 USD | 0.00 USD | 6,880,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD |
| `1D` | `51.20` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 1,770.00 USD | 1,130.00 USD | 19,220.00 USD |
| `7D` | `51.20` | 6,800,000.00 USD | 0.00 USD | 6,800,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD |
| `1D` | `51.30` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 8,650.00 USD | 9,710.00 USD | 0.00 USD |
| `7D` | `51.30` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 28,400.00 USD | 26,720.00 USD | 47,090.00 USD |
| `1D` | `51.40` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 3,250.00 USD | 5,460.00 USD | 416.23 USD |
| `7D` | `51.40` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 73,130.00 USD | 42,820.00 USD | 46,140.00 USD |
| `1D` | `51.50` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 6,950.00 USD | 10,010.00 USD | 41,580.00 USD |
| `7D` | `51.50` | 6,470,000.00 USD | 0.00 USD | 6,470,000.00 USD | 38,520.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `51.60` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 7,150.00 USD | 18,350.00 USD | 731.68 USD |
| `7D` | `51.60` | 6,370,000.00 USD | 0.00 USD | 6,370,000.00 USD | 37,880.00 USD | 36,790.00 USD | 41,490.00 USD |
| `1D` | `51.70` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 2,660.00 USD | 12,840.00 USD | 44.86 USD |
| `7D` | `51.70` | 6,260,000.00 USD | 0.00 USD | 6,260,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `51.80` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 10,010.00 USD | 19,520.00 USD | 13,490.00 USD |
| `7D` | `51.80` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD |
| `1D` | `51.90` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 10,140.00 USD | 19,910.00 USD | 23,480.00 USD |
| `7D` | `51.90` | 6,160,000.00 USD | 0.00 USD | 6,160,000.00 USD | 5,870.00 USD | 25,410.00 USD | 28,190.00 USD |
| `1D` | `52.00` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 20,980.00 USD | 25,620.00 USD | 24,820.00 USD |
| `7D` | `52.00` | 6,100,000.00 USD | 0.00 USD | 6,100,000.00 USD | 65,840.00 USD | 26,440.00 USD | 11,880.00 USD |
| `1D` | `52.10` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 34,970.00 USD | 17,300.00 USD | 50,500.00 USD |
| `7D` | `52.10` | 6,000,000.00 USD | 0.00 USD | 6,000,000.00 USD | 24,220.00 USD | 28,090.00 USD | 37,880.00 USD |
| `1D` | `52.20` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 15,890.00 USD | 7,630.00 USD | 49,960.00 USD |
| `7D` | `52.20` | 5,910,000.00 USD | 0.00 USD | 5,910,000.00 USD | 38,380.00 USD | 13,960.00 USD | 25,270.00 USD |
| `1D` | `52.30` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 26,510.00 USD | 22,090.00 USD | 11,210.00 USD |
| `7D` | `52.30` | 5,830,000.00 USD | 0.00 USD | 5,830,000.00 USD | 26,450.00 USD | 40,700.00 USD | 7,980.00 USD |
| `1D` | `52.40` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 14,800.00 USD | 15,400.00 USD | 7,040.00 USD |
| `7D` | `52.40` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 20,580.00 USD | 38,950.00 USD | 22,030.00 USD |
| `1D` | `52.50` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 53,990.00 USD | 30,000.00 USD | 79,400.00 USD |
| `7D` | `52.50` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 39,410.00 USD | 0.00 USD | 11,240.00 USD |
| `1D` | `52.60` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 9,060.00 USD | 43,700.00 USD | 5,450.00 USD |
| `7D` | `52.60` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 67,180.00 USD | 32,590.00 USD | 59,410.00 USD |
| `1D` | `52.70` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 18,270.00 USD | 19,780.00 USD | 40,000.00 USD |
| `7D` | `52.70` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 19,550.00 USD | 75,910.00 USD | 108,640.00 USD |
| `1D` | `52.80` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 28,000.00 USD | 50,850.00 USD | 72,920.00 USD |
| `7D` | `52.80` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 30,590.00 USD | 25,700.00 USD | 0.00 USD |
| `1D` | `52.90` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 43,760.00 USD | 52,850.00 USD | 30,100.00 USD |
| `7D` | `52.90` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 30,900.00 USD | 11,650.00 USD | 34,400.00 USD |
| `1D` | `53.00` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 26,800.00 USD | 33,430.00 USD | 52,230.00 USD |
| `7D` | `53.00` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 39,690.00 USD | 22,700.00 USD | 77,700.00 USD |
| `1D` | `53.10` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 12,590.00 USD | 53,180.00 USD | 85,180.00 USD |
| `7D` | `53.10` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 45,320.00 USD | 20,560.00 USD | 0.00 USD |
| `1D` | `53.20` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 36,030.00 USD | 22,000.00 USD | 46,930.00 USD |
| `7D` | `53.20` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 162,460.00 USD | 50,210.00 USD | 23,350.00 USD |
| `1D` | `53.30` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 8,140.00 USD | 28,530.00 USD | 5,690.00 USD |
| `7D` | `53.30` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 59,390.00 USD | 49,210.00 USD | 35,070.00 USD |
| `1D` | `53.40` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 12,600.00 USD | 10,640.00 USD | 4,540.00 USD |
| `7D` | `53.40` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 44,030.00 USD | 17,420.00 USD | 91,220.00 USD |
| `1D` | `53.50` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 9,170.00 USD | 5,700.00 USD | 22,000.00 USD |
| `7D` | `53.50` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 60,260.00 USD | 3,440.00 USD | 28,500.00 USD |
| `1D` | `53.60` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 75,950.00 USD | 3,830.00 USD | 20,970.00 USD |
| `7D` | `53.60` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 52,800.00 USD | 3,780.00 USD | 20,660.00 USD |
| `1D` | `53.70` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 6,210.00 USD | 11,100.00 USD | 11,960.00 USD |
| `7D` | `53.70` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 131,400.00 USD | 21,330.00 USD | 13,220.00 USD |
| `1D` | `53.80` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 53,640.00 USD | 28,920.00 USD | 4,830.00 USD |
| `7D` | `53.80` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 99,150.00 USD | 43,900.00 USD | 302.55 USD |
| `1D` | `53.90` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 51,060.00 USD | 39,560.00 USD | 27,830.00 USD |
| `7D` | `53.90` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 160,820.00 USD | 22,780.00 USD | 9,680.00 USD |
| `1D` | `54.00` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 76,010.00 USD | 25,380.00 USD | 86,580.00 USD |
| `7D` | `54.00` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 380,340.00 USD | 71,820.00 USD | 304,530.00 USD |
| `1D` | `54.10` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 94,870.00 USD | 25,040.00 USD | 74,440.00 USD |
| `7D` | `54.10` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 302,190.00 USD | 0.00 USD | 2,590.00 USD |
| `1D` | `54.20` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 72,600.00 USD | 35,780.00 USD | 40,150.00 USD |
| `7D` | `54.20` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 205,060.00 USD | 5,200.00 USD | 0.00 USD |
| `1D` | `54.30` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 46,340.00 USD | 30,990.00 USD | 15,110.00 USD |
| `7D` | `54.30` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 381,380.00 USD | 43,780.00 USD | 181,420.00 USD |
| `1D` | `54.40` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 62,350.00 USD | 92,560.00 USD | 3,290.00 USD |
| `7D` | `54.40` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 304,270.00 USD | 63,170.00 USD | 92,650.00 USD |
| `1D` | `54.50` | 855,480.00 USD | 0.00 USD | 855,480.00 USD | 24,100.00 USD | 64,250.00 USD | 9,090.00 USD |
| `7D` | `54.50` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 159,720.00 USD | 35,580.00 USD | 239,890.00 USD |
| `1D` | `54.60` | 758,030.00 USD | 0.00 USD | 758,030.00 USD | 913.17 USD | 25,490.00 USD | 43,580.00 USD |
| `7D` | `54.60` | 944,400.00 USD | 0.00 USD | 944,400.00 USD | 18,530.00 USD | 1,930.00 USD | 131,380.00 USD |
| `1D` | `54.70` | 688,040.00 USD | 0.00 USD | 688,040.00 USD | 6,600.00 USD | 23,060.00 USD | 105,800.00 USD |
| `7D` | `54.70` | 792,560.00 USD | 0.00 USD | 792,560.00 USD | 0.00 USD | 3,600.00 USD | 41,310.00 USD |
| `1D` | `54.80` | 552,580.00 USD | 0.00 USD | 552,580.00 USD | 0.00 USD | 48,420.00 USD | 23,920.00 USD |
| `7D` | `54.80` | 747,650.00 USD | 0.00 USD | 747,650.00 USD | 0.00 USD | 35,700.00 USD | 26,440.00 USD |
| `1D` | `54.90` | 480,250.00 USD | 0.00 USD | 480,250.00 USD | 66,900.00 USD | 65,440.00 USD | 10,850.00 USD |
| `7D` | `54.90` | 685,510.00 USD | 0.00 USD | 685,510.00 USD | 0.00 USD | 112,280.00 USD | 48,290.00 USD |
| `1D` | `55.00` | 337,060.00 USD | 0.00 USD | 337,060.00 USD | 40,710.00 USD | 54,150.00 USD | 55,190.00 USD |
| `7D` | `55.00` | 524,940.00 USD | 0.00 USD | 524,940.00 USD | 97,700.00 USD | 2,830.00 USD | 19,360.00 USD |
| `1D` | `55.10` | 187,000.00 USD | 0.00 USD | 187,000.00 USD | 50,530.00 USD | 56,280.00 USD | 80,200.00 USD |
| `7D` | `55.10` | 405,060.00 USD | 0.00 USD | 405,060.00 USD | 54,590.00 USD | 18,510.00 USD | 64,690.00 USD |
| `1D` | `55.20` | 47,630.00 USD | 47,630.00 USD | 0.00 USD | 39,390.00 USD | 7,890.00 USD | 352.80 USD |
| `1D` | `55.20` | 95,260.00 USD | 95,260.00 USD | 0.00 USD | 39,390.00 USD | 7,890.00 USD | 352.80 USD |
| `7D` | `55.20` | 267,270.00 USD | 0.00 USD | 267,270.00 USD | 57,400.00 USD | 59,710.00 USD | 150,160.00 USD |
| `1D` | `55.30` | 222,810.00 USD | 222,810.00 USD | 0.00 USD | 52,860.00 USD | 15,520.00 USD | 59,180.00 USD |
| `7D` | `55.30` | 23,140.00 USD | 23,140.00 USD | 0.00 USD | 23,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.30` | 46,280.00 USD | 46,280.00 USD | 0.00 USD | 23,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.40` | 51,080.00 USD | 51,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,800.00 USD |
| `1D` | `55.50` | 228,310.00 USD | 228,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD |
| `1D` | `55.70` | 236,630.00 USD | 236,630.00 USD | 0.00 USD | 0.00 USD | 7,700.00 USD | 613.46 USD |
| `7D` | `55.70` | 257,510.00 USD | 257,510.00 USD | 0.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD |
| `1D` | `55.80` | 239,800.00 USD | 239,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,170.00 USD |
| `7D` | `55.80` | 348,480.00 USD | 348,480.00 USD | 0.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD |
| `1D` | `55.90` | 292,860.00 USD | 292,860.00 USD | 0.00 USD | 51,520.00 USD | 0.00 USD | 1,550.00 USD |
| `7D` | `55.90` | 489,800.00 USD | 489,800.00 USD | 0.00 USD | 141,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `56.00` | 297,240.00 USD | 297,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,380.00 USD |
| `7D` | `56.00` | 660,920.00 USD | 660,920.00 USD | 0.00 USD | 2,590.00 USD | 0.00 USD | 168,520.00 USD |
| `1D` | `56.20` | 301,180.00 USD | 301,180.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD | 0.00 USD |
| `7D` | `56.20` | 740,860.00 USD | 740,860.00 USD | 0.00 USD | 0.00 USD | 79,940.00 USD | 0.00 USD |
| `1D` | `56.30` | 336,280.00 USD | 336,280.00 USD | 0.00 USD | 0.00 USD | 5,870.00 USD | 29,230.00 USD |
| `7D` | `56.30` | 743,460.00 USD | 743,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,590.00 USD |
| `1D` | `56.40` | 380,920.00 USD | 380,920.00 USD | 0.00 USD | 5,040.00 USD | 37,100.00 USD | 2,500.00 USD |
| `7D` | `56.40` | 762,350.00 USD | 762,350.00 USD | 0.00 USD | 2,650.00 USD | 16,240.00 USD | 0.00 USD |
| `1D` | `56.50` | 837,720.00 USD | 837,720.00 USD | 0.00 USD | 169,280.00 USD | 132,970.00 USD | 154,560.00 USD |
| `7D` | `56.50` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 170,750.00 USD | 187,200.00 USD | 6,150.00 USD |
| `1D` | `56.60` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 61,400.00 USD | 161,300.00 USD | 81,070.00 USD |
| `7D` | `56.60` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 363,190.00 USD | 185,910.00 USD | 507.54 USD |
| `1D` | `56.70` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 114,230.00 USD | 45,300.00 USD | 315,590.00 USD |
| `7D` | `56.70` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 117,290.00 USD | 141,830.00 USD | 98,950.00 USD |
| `1D` | `56.80` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 117,760.00 USD | 20,790.00 USD | 106,140.00 USD |
| `7D` | `56.80` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 172,110.00 USD | 92,780.00 USD | 318,330.00 USD |
| `1D` | `56.90` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 45,140.00 USD | 17,930.00 USD | 35,720.00 USD |
| `7D` | `56.90` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 113,780.00 USD | 52,200.00 USD | 307,930.00 USD |
| `1D` | `57.00` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 6,480.00 USD | 43,030.00 USD | 29,740.00 USD |
| `7D` | `57.00` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 88,680.00 USD | 56,390.00 USD | 178,370.00 USD |
| `1D` | `57.10` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 77,000.00 USD | 77,400.00 USD | 46,610.00 USD |
| `7D` | `57.10` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 36,580.00 USD | 79,290.00 USD | 21,040.00 USD |
| `1D` | `57.20` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 53,080.00 USD | 78,490.00 USD | 120,900.00 USD |
| `7D` | `57.20` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 118,850.00 USD | 23,920.00 USD | 23,060.00 USD |
| `1D` | `57.30` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 70,930.00 USD | 46,600.00 USD | 87,180.00 USD |
| `7D` | `57.30` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 76,940.00 USD | 28,570.00 USD | 98,930.00 USD |
| `1D` | `57.40` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 84,960.00 USD | 52,400.00 USD | 91,040.00 USD |
| `7D` | `57.40` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 124,180.00 USD | 72,180.00 USD | 257,020.00 USD |
| `1D` | `57.50` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 197,830.00 USD | 58,480.00 USD | 174,760.00 USD |
| `7D` | `57.50` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 99,810.00 USD | 34,430.00 USD | 0.00 USD |
| `1D` | `57.60` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 85,090.00 USD | 39,540.00 USD | 67,390.00 USD |
| `7D` | `57.60` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 149,560.00 USD | 62,320.00 USD | 28,320.00 USD |
| `1D` | `57.70` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 42,540.00 USD | 54,600.00 USD | 96,430.00 USD |
| `7D` | `57.70` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 30,070.00 USD | 57,580.00 USD |
| `1D` | `57.80` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 18,150.00 USD | 22,650.00 USD | 77,220.00 USD |
| `7D` | `57.80` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 9,650.00 USD | 24,520.00 USD | 49,480.00 USD |
| `1D` | `57.90` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 13,000.00 USD | 15,870.00 USD | 28,950.00 USD |
| `7D` | `57.90` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 14,390.00 USD | 963.90 USD | 30,010.00 USD |
| `1D` | `58.00` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 9,620.00 USD | 9,480.00 USD | 15,330.00 USD |
| `7D` | `58.00` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD | 107,350.00 USD |
| `1D` | `58.10` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 31,400.00 USD | 17,830.00 USD | 21,300.00 USD |
| `7D` | `58.10` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 5,470.00 USD | 19,160.00 USD | 14,070.00 USD |
| `1D` | `58.20` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 36,640.00 USD | 34,800.00 USD | 4,940.00 USD |
| `7D` | `58.20` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 31,590.00 USD | 302.55 USD |
| `1D` | `58.30` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 33,360.00 USD | 38,620.00 USD | 64,380.00 USD |
| `7D` | `58.30` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 48,850.00 USD | 11,000.00 USD | 36,500.00 USD |
| `1D` | `58.40` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 26,490.00 USD | 18,940.00 USD | 49,980.00 USD |
| `7D` | `58.40` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 27,290.00 USD | 9,260.00 USD | 86,460.00 USD |
| `1D` | `58.50` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 3,900.00 USD | 1,200.00 USD | 124.02 USD |
| `7D` | `58.50` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 2,060.00 USD | 24,530.00 USD | 0.00 USD |
| `1D` | `58.60` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 21,940.00 USD | 5,920.00 USD | 40,890.00 USD |
| `7D` | `58.60` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 30,680.00 USD | 20,260.00 USD | 51,650.00 USD |
| `1D` | `58.70` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 44,920.00 USD | 10,120.00 USD | 29,940.00 USD |
| `7D` | `58.70` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 15,810.00 USD | 11,600.00 USD | 35,320.00 USD |
| `1D` | `58.80` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 36,630.00 USD | 9,890.00 USD | 23,340.00 USD |
| `7D` | `58.80` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD |
| `1D` | `58.90` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 23,430.00 USD | 60,970.00 USD | 90,490.00 USD |
| `7D` | `58.90` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 2,140.00 USD | 54,240.00 USD | 83,500.00 USD |
| `1D` | `59.00` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 129,990.00 USD | 58,870.00 USD | 129,440.00 USD |
| `7D` | `59.00` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 259,280.00 USD | 65,270.00 USD | 118,570.00 USD |
| `1D` | `59.10` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 92,780.00 USD | 39,740.00 USD | 163,590.00 USD |
| `7D` | `59.10` | 6,460,000.00 USD | 6,460,000.00 USD | 0.00 USD | 93,390.00 USD | 45,400.00 USD | 158,780.00 USD |
| `1D` | `59.20` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 102,940.00 USD | 59,320.00 USD | 49,210.00 USD |
| `7D` | `59.20` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 153,580.00 USD | 18,540.00 USD | 174,600.00 USD |
| `1D` | `59.30` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 146,220.00 USD | 30,070.00 USD | 66,050.00 USD |
| `7D` | `59.30` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 88,710.00 USD | 67,460.00 USD | 114,310.00 USD |
| `1D` | `59.40` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 35,110.00 USD | 30,410.00 USD | 49,030.00 USD |
| `7D` | `59.40` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 107,040.00 USD | 73,620.00 USD | 137,500.00 USD |
| `1D` | `59.50` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 78,730.00 USD | 34,150.00 USD | 28,530.00 USD |
| `7D` | `59.50` | 7,540,000.00 USD | 7,540,000.00 USD | 0.00 USD | 67,060.00 USD | 61,370.00 USD | 21,090.00 USD |
| `1D` | `59.60` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 34,500.00 USD | 50,610.00 USD | 5,210.00 USD |
| `7D` | `59.60` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 236,760.00 USD | 128,050.00 USD | 72,920.00 USD |
| `1D` | `59.70` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 1,710.00 USD | 15,700.00 USD | 60,900.00 USD |
| `7D` | `59.70` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 55,510.00 USD | 99,970.00 USD | 162,850.00 USD |
| `1D` | `59.80` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 22,720.00 USD | 26,470.00 USD | 177.92 USD |
| `7D` | `59.80` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 118,240.00 USD | 91,980.00 USD | 154,560.00 USD |
| `1D` | `59.90` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 102,020.00 USD | 17,810.00 USD | 50,060.00 USD |
| `7D` | `59.90` | 8,870,000.00 USD | 8,870,000.00 USD | 0.00 USD | 142,290.00 USD | 34,490.00 USD | 29,380.00 USD |
| `1D` | `60.00` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 162,340.00 USD | 29,090.00 USD | 50,570.00 USD |
| `7D` | `60.00` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 100,570.00 USD | 67,520.00 USD | 83,920.00 USD |
| `1D` | `60.10` | 6,840,000.00 USD | 6,840,000.00 USD | 0.00 USD | 64,550.00 USD | 28,140.00 USD | 57,080.00 USD |
| `7D` | `60.10` | 9,500,000.00 USD | 9,500,000.00 USD | 0.00 USD | 200,540.00 USD | 84,980.00 USD | 95,670.00 USD |
| `1D` | `60.20` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 58,500.00 USD | 19,740.00 USD | 82,270.00 USD |
| `7D` | `60.20` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 162,230.00 USD | 99,360.00 USD | 108,990.00 USD |
| `1D` | `60.30` | 7,110,000.00 USD | 7,110,000.00 USD | 0.00 USD | 51,410.00 USD | 31,630.00 USD | 26,470.00 USD |
| `7D` | `60.30` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 133,350.00 USD | 100,380.00 USD | 170,480.00 USD |
| `1D` | `60.40` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 66,740.00 USD | 13,730.00 USD | 42,520.00 USD |
| `7D` | `60.40` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 64,850.00 USD | 100,560.00 USD | 202,370.00 USD |
| `1D` | `60.50` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 22,700.00 USD | 19,320.00 USD | 36,200.00 USD |
| `7D` | `60.50` | 11,010,000.00 USD | 11,010,000.00 USD | 0.00 USD | 115,390.00 USD | 80,510.00 USD | 175,550.00 USD |
| `1D` | `60.60` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 40,710.00 USD | 19,510.00 USD | 3,930.00 USD |
| `7D` | `60.60` | 11,400,000.00 USD | 11,400,000.00 USD | 0.00 USD | 251,100.00 USD | 16,970.00 USD | 118,680.00 USD |
| `1D` | `60.70` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 32,330.00 USD | 23,510.00 USD | 8,180.00 USD |
| `7D` | `60.70` | 11,570,000.00 USD | 11,570,000.00 USD | 0.00 USD | 102,230.00 USD | 47,600.00 USD | 15,880.00 USD |
| `1D` | `60.80` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 11,060.00 USD | 14,670.00 USD | 47,810.00 USD |
| `7D` | `60.80` | 11,720,000.00 USD | 11,720,000.00 USD | 0.00 USD | 46,960.00 USD | 28,960.00 USD | 76,200.00 USD |
| `1D` | `60.90` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 37,840.00 USD | 26,790.00 USD | 24,800.00 USD |
| `7D` | `60.90` | 11,930,000.00 USD | 11,930,000.00 USD | 0.00 USD | 105,970.00 USD | 38,330.00 USD | 64,920.00 USD |
| `1D` | `61.00` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 43,930.00 USD | 6,430.00 USD | 18,420.00 USD |
| `7D` | `61.00` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 43,120.00 USD | 11,530.00 USD | 0.00 USD |
| `1D` | `61.10` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 13,020.00 USD | 14,950.00 USD | 11,520.00 USD |
| `7D` | `61.10` | 12,020,000.00 USD | 12,020,000.00 USD | 0.00 USD | 31,540.00 USD | 10,430.00 USD | 0.00 USD |
| `1D` | `61.20` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 74,360.00 USD | 1,880.00 USD | 39,080.00 USD |
| `7D` | `61.20` | 12,140,000.00 USD | 12,140,000.00 USD | 0.00 USD | 49,090.00 USD | 20,920.00 USD | 47,810.00 USD |
| `1D` | `61.30` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 0.00 USD | 4,040.00 USD | 7,600.00 USD |
| `7D` | `61.30` | 12,190,000.00 USD | 12,190,000.00 USD | 0.00 USD | 14,390.00 USD | 13,210.00 USD | 24,230.00 USD |
| `1D` | `61.40` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 1,190.00 USD | 709.61 USD | 5,230.00 USD |
| `7D` | `61.40` | 12,330,000.00 USD | 12,330,000.00 USD | 0.00 USD | 62,340.00 USD | 25,720.00 USD | 43,510.00 USD |
| `1D` | `61.50` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 1,060.00 USD | 3,880.00 USD | 2,290.00 USD |
| `7D` | `61.50` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 17,710.00 USD | 42,440.00 USD | 41,390.00 USD |
| `1D` | `61.60` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 6,660.00 USD | 2,490.00 USD | 1,150.00 USD |
| `7D` | `61.60` | 12,640,000.00 USD | 12,640,000.00 USD | 0.00 USD | 32,920.00 USD | 58,350.00 USD | 121,470.00 USD |
| `1D` | `61.70` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 7,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `61.70` | 12,830,000.00 USD | 12,830,000.00 USD | 0.00 USD | 82,860.00 USD | 10,880.00 USD | 99,740.00 USD |
| `7D` | `61.80` | 13,100,000.00 USD | 13,100,000.00 USD | 0.00 USD | 169,680.00 USD | 25,670.00 USD | 71,530.00 USD |
| `7D` | `61.90` | 13,250,000.00 USD | 13,250,000.00 USD | 0.00 USD | 73,690.00 USD | 32,820.00 USD | 41,580.00 USD |
| `7D` | `62.00` | 13,350,000.00 USD | 13,350,000.00 USD | 0.00 USD | 50,080.00 USD | 8,550.00 USD | 40,590.00 USD |
| `7D` | `62.10` | 13,360,000.00 USD | 13,360,000.00 USD | 0.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.20` | 13,470,000.00 USD | 13,470,000.00 USD | 0.00 USD | 37,600.00 USD | 34,620.00 USD | 41,360.00 USD |
| `7D` | `62.30` | 13,620,000.00 USD | 13,620,000.00 USD | 0.00 USD | 25,910.00 USD | 23,450.00 USD | 97,450.00 USD |
| `7D` | `62.40` | 13,750,000.00 USD | 13,750,000.00 USD | 0.00 USD | 74,860.00 USD | 27,560.00 USD | 25,440.00 USD |
| `7D` | `62.50` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 36,690.00 USD | 12,720.00 USD | 25,700.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `407.77M` | Total OI Tokens: `7,384,595.8 LTC`
  * 1h OI Change: `-0.42%` | 4h OI Change: `-2.13%` | 24h OI Change: `-9.38%`
  * Exchange Breakdown: Binance=`72.12M` | Bybit=`66.35M` | OKX=`34.26M` | Hyperliquid=`22.07M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `9.17K` | Last 24h: `29.34K` | Last 3d: `56.60K` | Last 7d: `113.64K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0004%` |
| **USDT Bybit** | `0.0025%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0010%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `51.65%` | `48.35%` | `1.07` | 1,220,000.00 USD |
| `15M` | `Binance` | `39.78%` | `60.22%` | `0.66` | 340,360.00 USD |
| `15M` | `OKX` | `53.7%` | `46.3%` | `1.16` | 99,110.00 USD |
| `15M` | `Bybit` | `42.72%` | `57.28%` | `0.75` | 51,140.00 USD |
| `15M` | `KuCoin` | `54.22%` | `45.78%` | `1.18` | 103,480.00 USD |
| `15M` | `Gate` | `40.22%` | `59.78%` | `0.67` | 17,900.00 USD |
| `15M` | `Bitget` | `22.57%` | `77.43%` | `0.29` | 21,590.00 USD |
| `15M` | `BingX` | `48.28%` | `51.72%` | `0.93` | 104,410.00 USD |
| `15M` | `MEXC` | `38.44%` | `61.56%` | `0.62` | 41,870.00 USD |
| `15M` | `Bitunix` | `54.07%` | `45.93%` | `1.18` | 41,470.00 USD |
| `15M` | `Hyperliquid` | `15.26%` | `84.74%` | `0.18` | 4,140.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.56%` | `49.44%` | `1.02` | 248,030.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `96.6%` | `3.4%` | `28.41` | 135,570.00 USD |
| `15M` | `HTX` | `38.92%` | `61.08%` | `0.64` | 657.18 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `24.78%` | `75.22%` | `0.33` | 5,480.00 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 655.05 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `80.2%` | `19.8%` | `4.05` | 6,230.00 USD |
| `15M` | `Whale Positions` | `39.78%` | `60.22%` | `0.66` | 340,360.00 USD |
| `15M` | `Global Accounts` | `51.65%` | `48.35%` | `1.07` | 1,220,000.00 USD |
| `1H` | `LTC` | `50.84%` | `49.16%` | `1.03` | 7,340,000.00 USD |
| `1H` | `Binance` | `36.78%` | `63.22%` | `0.58` | 1,390,000.00 USD |
| `1H` | `OKX` | `47.97%` | `52.03%` | `0.92` | 549,060.00 USD |
| `1H` | `Bybit` | `40.27%` | `59.73%` | `0.67` | 383,140.00 USD |
| `1H` | `KuCoin` | `50.18%` | `49.82%` | `1.01` | 309,400.00 USD |
| `1H` | `Gate` | `56.86%` | `43.14%` | `1.32` | 113,080.00 USD |
| `1H` | `Bitget` | `64.2%` | `35.8%` | `1.79` | 160,830.00 USD |
| `1H` | `BingX` | `49.62%` | `50.38%` | `0.98` | 400,390.00 USD |
| `1H` | `MEXC` | `39.66%` | `60.34%` | `0.66` | 185,920.00 USD |
| `1H` | `Bitunix` | `48.3%` | `51.7%` | `0.93` | 120,070.00 USD |
| `1H` | `Hyperliquid` | `21.6%` | `78.4%` | `0.28` | 103,690.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50%` | `50%` | `1.00` | 2,740,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `86.95%` | `13.05%` | `6.66` | 829,430.00 USD |
| `1H` | `HTX` | `27.32%` | `72.68%` | `0.38` | 3,990.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `51.09%` | `48.91%` | `1.04` | 24,690.00 USD |
| `1H` | `Aster` | `0%` | `100%` | `0.00` | 666.14 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `91.58%` | `8.42%` | `10.88` | 22,020.00 USD |
| `1H` | `Whale Positions` | `36.78%` | `63.22%` | `0.58` | 1,390,000.00 USD |
| `1H` | `Global Accounts` | `50.84%` | `49.16%` | `1.03` | 7,340,000.00 USD |
| `4H` | `LTC` | `46.68%` | `53.32%` | `0.88` | 41,470,000.00 USD |
| `4H` | `Binance` | `48.31%` | `51.69%` | `0.93` | 11,340,000.00 USD |
| `4H` | `OKX` | `37.36%` | `62.64%` | `0.60` | 4,020,000.00 USD |
| `4H` | `Bybit` | `51.6%` | `48.4%` | `1.07` | 3,070,000.00 USD |
| `4H` | `KuCoin` | `45.78%` | `54.22%` | `0.84` | 333,600.00 USD |
| `4H` | `Gate` | `50.88%` | `49.12%` | `1.04` | 3,950,000.00 USD |
| `4H` | `Bitget` | `42.59%` | `57.41%` | `0.74` | 1,270,000.00 USD |
| `4H` | `BingX` | `33.56%` | `66.44%` | `0.51` | 10,480,000.00 USD |
| `4H` | `MEXC` | `57.74%` | `42.26%` | `1.37` | 1,060,000.00 USD |
| `4H` | `Bitunix` | `44.69%` | `55.31%` | `0.81` | 881,660.00 USD |
| `4H` | `Hyperliquid` | `44.75%` | `55.25%` | `0.81` | 354,780.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.86%` | `49.14%` | `1.04` | 976,590.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `91.67%` | `8.33%` | `11.00` | 2,900,000.00 USD |
| `4H` | `HTX` | `43.94%` | `56.06%` | `0.78` | 81,540.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `36.92%` | `63.08%` | `0.59` | 108,250.00 USD |
| `4H` | `Aster` | `46.22%` | `53.78%` | `0.86` | 20,750.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `27.88%` | `72.12%` | `0.39` | 634,930.00 USD |
| `4H` | `Whale Positions` | `48.31%` | `51.69%` | `0.93` | 11,340,000.00 USD |
| `4H` | `Global Accounts` | `46.68%` | `53.32%` | `0.88` | 41,470,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `55.91` | `55.98` | `55.91` | `56.12` | `55.78` | 818,601.42 USD | 432,159.31 USD | 386,442.11 USD | 45,717.20 USD | `+5.58%` | `3B / 5S` |
| `0:00 UTC` | `55.77` | `55.81` | `55.77` | `56.00` | `55.66` | 705,526.23 USD | 343,392.26 USD | 362,133.97 USD | -18,741.70 USD | `-2.66%` | `2B / 3S` |
| `5:00 UTC` | `55.64` | `55.76` | `55.64` | `55.98` | `55.62` | 705,697.21 USD | 170,266.34 USD | 535,430.87 USD | -365,164.53 USD | `-51.75%` | `2B / 13S` |
| `0:00 UTC` | `55.70` | `55.69` | `55.70` | `55.78` | `55.55` | 839,476.56 USD | 572,886.16 USD | 266,590.39 USD | 306,295.77 USD | `+36.49%` | `1B / 5S` |
| `5:00 UTC` | `55.59` | `55.60` | `55.59` | `55.70` | `55.52` | 436,166.22 USD | 242,135.61 USD | 194,030.61 USD | 48,104.99 USD | `+11.03%` | `3B / 4S` |
| `0:00 UTC` | `55.50` | `55.53` | `55.50` | `55.70` | `55.44` | 464,437.63 USD | 192,555.45 USD | 271,882.18 USD | -79,326.74 USD | `-17.08%` | `3B / 5S` |
| `5:00 UTC` | `55.42` | `55.46` | `55.42` | `55.59` | `55.39` | 371,902.17 USD | 185,679.40 USD | 186,222.77 USD | -543.37 USD | `-0.15%` | `2B / 4S` |
| `0:00 UTC` | `55.39` | `55.44` | `55.39` | `55.55` | `55.34` | 379,922.90 USD | 203,005.18 USD | 176,917.72 USD | 26,087.46 USD | `+6.87%` | `4B / 0S` |
| `5:00 UTC` | `55.42` | `55.40` | `55.42` | `55.52` | `55.27` | 934,212.03 USD | 256,275.15 USD | 677,936.88 USD | -421,661.72 USD | `-45.14%` | `0B / 6S` |
| `0:00 UTC` | `55.25` | `55.29` | `55.25` | `55.41` | `55.22` | 175,777.10 USD | 74,558.26 USD | 101,218.85 USD | -26,660.59 USD | `-15.17%` | `1B / 6S` |

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
| `5m` | -23,760.00 USD | -78,500.00 USD | **`DISTRIBUTION`** |
| `15m` | -33,170.00 USD | -507,210.00 USD | **`DISTRIBUTION`** |
| `30m` | -168,790.00 USD | -701,790.00 USD | **`DISTRIBUTION`** |
| `1h` | -154,650.00 USD | -747,490.00 USD | **`DISTRIBUTION`** |
| `2h` | -329,850.00 USD | -761,950.00 USD | **`DISTRIBUTION`** |
| `4h` | -50,740.00 USD | -1,200,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 248,690.00 USD | -1,180,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 469,060.00 USD | -2,620,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 142,900.00 USD | -4,810,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 645,760.00 USD | -5,840,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 4,200,000.00 USD | -25,030,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -24,560,000.00 USD | -198,870,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-23.76K` | 15m=`-33.17K` | 1h=`-154.65K` | 24h=`+645.76K`
* Futures Capital Netflows: 5m=`-78.50K` | 15m=`-507.21K` | 1h=`-747.49K` | 24h=`-5.84M`
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
  * `2026-10-30 15:33:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:19:00 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:00 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:00 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:00 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `53.79` (Risk Distance: `0.8180` pts)
  * +2.5R Take Profit: `56.66`
  * Mathematical Lot Sizing: **`12.22 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `56.12` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `56.94` (Risk Distance: `0.8180` pts)
  * +2.5R Take Profit: `54.07`
  * Mathematical Lot Sizing: **`12.22 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`55.64`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
