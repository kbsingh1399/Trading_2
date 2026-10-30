# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 09:40:22 IST` (`2026-10-30 04:10:22 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `55.72` | **Live Ask Quote**: `56.02` | **Mid Price**: `55.87`
- **Spread Points**: `300.00` | **Spread BPS**: `53.70 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `54.22` | VWAP Z-Score: `+2.64` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.5074` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `60.75` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `56.25` | Lower -3.00σ Band: `52.19`
  * Upper +2.51σ Band: `55.91` | Lower -2.51σ Band: `52.52`
  * Upper +2.01σ Band: `55.58` | Lower -2.01σ Band: `52.86`
  * Upper +2.00σ Band: `55.57` | Lower -2.00σ Band: `52.87`
  * Upper +1.28σ Band: `55.08` | Lower -1.28σ Band: `53.35`
  * Upper +1.00σ Band: `54.89` | Lower -1.00σ Band: `53.54`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`55.20` | EMA-20=`55.05` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`55.70` (Slope: `+0.0000`) | EMA-100=`56.42`
  * Institutional Anchors: EMA-144=`56.68` | EMA-200=`56.72` (Slope: `-0.4243`) | EMA-233=`56.79`
- **Range Boundaries**: 24H High=`58.72` | 24H Low=`52.64` | Weekly High=`59.62` | Weekly Low=`52.64`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `55.87` (Distance: `+0.00%`)
  * Point of Control (POC) = `55.28` (Distance: `+1.06%`)
  * Value Area Low (VAL) = `54.16` (Distance: `+3.16%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.40` | POC=`57.72` | VAL=`56.83`
  * Prior Day Extremes: PDH=`59.52` | PDL=`54.18` | PDC=`54.46`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`58.34` | Weekly POC=`56.43` | Weekly VAL=`55.97`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`56.02` | Low=`52.64`
  * London Session (08:00-16:00 UTC): High=`56.09` | Low=`55.64`
  * New York Session (13:00-21:00 UTC): High=`56.20` | Low=`55.53`
  * Initial Balance (First Hour): IB High=`56.03` | IB Low=`55.70`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `55.64` - `56.09`
  * Optimal Trade Entry (OTE 0.705): `55.98`
  * Structural Invalidation Anchor (0.786): `56.31`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `55.83` | `56.04` | `55.79` | `55.99` | `8,835` | 494,251.60 USD | 16,413.15 USD | `+3.32%` | -4,918,311.90 USD | `+0.56` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `56.00` | `56.07` | `55.96` | `56.01` | `6,025` | 337,441.76 USD | -64,687.08 USD | `-19.17%` | -4,982,998.99 USD | `-0.27` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `56.02` | `56.13` | `55.95` | `56.13` | `5,106` | 286,193.29 USD | -20,659.83 USD | `-7.22%` | -5,003,658.82 USD | `+0.22` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `55.22` | `55.69` | `55.19` | `55.66` | `15,680` | 870,084.16 USD | -47,733.14 USD | `-5.49%` | -4,803,684.64 USD | `+0.27` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `55.67` | `56.07` | `55.64` | `56.01` | `25,256` | 1,411,324.18 USD | -167,107.24 USD | `-11.84%` | -4,970,791.87 USD | `-0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `56.02` | `56.13` | `55.95` | `56.13` | `5,106` | 286,193.29 USD | -20,659.83 USD | `-7.22%` | -4,991,451.70 USD | `+0.37` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `54.36` | `54.62` | `53.64` | `54.29` | `95,012` | 5,151,310.38 USD | -124,905.13 USD | `-2.42%` | -4,162,296.53 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `54.30` | `55.34` | `53.91` | `55.13` | `78,887` | 4,333,440.29 USD | -426,625.42 USD | `-9.84%` | -4,588,921.95 USD | `-0.29` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `55.13` | `56.13` | `55.11` | `56.12` | `65,002` | 3,616,609.89 USD | -412,712.09 USD | `-11.41%` | -5,001,634.04 USD | `-0.23` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | 340,473.45 USD | `+0.15` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,923,567.46 USD | `-1.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `56.13` | `52.77` | `56.13` | `533,732` | 28,966,763.44 USD | -2,067,884.24 USD | `-7.14%` | -4,991,451.70 USD | `-0.90` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `57.04` | `58.16` | `56.85` | `58.00` | `178,996` | 10,300,529.12 USD | 452,809.17 USD | `+4.40%` | -47,398.66 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | 201,186.90 USD | `+0.44` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | 340,473.45 USD | `+0.15` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,923,567.46 USD | `-1.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `56.13` | `52.77` | `56.13` | `533,732` | 28,966,763.44 USD | -2,067,884.24 USD | `-7.14%` | -4,991,451.70 USD | `-0.90` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`55.87`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:33:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1059` | `0xeadc...9d55` | `LONG` | 2,038,105.96 USD | `36,463.77` | `52.78` | `55.88` | `0.000000` | 113,430.01 USD | `+5.57%` | `10X Cross` |
| `1076` | `0x9aa5...58af` | `SHORT` | 2,020,738.82 USD | `36,177.65` | `71.22` | `55.88` | `307.10` | 555,747.85 USD | `+27.50%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`59.03` (Vol: 286,000.00 USD, Dist: `+5.36%`) | Long MP=`54.13` (Vol: 113,000.00 USD, Dist: `--3.38%`)
  * 48H Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+5.30%`) | Long MP=`54.12` (Vol: 113,000.00 USD, Dist: `--3.42%`)
  * 3D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+5.30%`) | Long MP=`54.12` (Vol: 113,000.00 USD, Dist: `--3.42%`)
  * 7D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+5.30%`) | Long MP=`54.12` (Vol: 113,000.00 USD, Dist: `--3.42%`)
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
| `Live` | `Long` | `11.35` | 3,040,000.00 USD | 0.00 USD | 136.20 USD | `-79.82%` | `12.00` |
| `Live` | `Long` | `12.25` | 3,040,000.00 USD | 0.00 USD | 265.33 USD | `-78.22%` | `21.66` |
| `Live` | `Long` | `12.75` | 3,040,000.00 USD | 0.00 USD | 2,560.00 USD | `-77.33%` | `200.43` |
| `Live` | `Long` | `13.15` | 3,030,000.00 USD | 0.00 USD | 2,220.00 USD | `-76.62%` | `168.79` |
| `Live` | `Long` | `13.65` | 3,030,000.00 USD | 0.00 USD | 150.15 USD | `-75.73%` | `11.00` |
| `Live` | `Long` | `16.95` | 3,030,000.00 USD | 0.00 USD | 2,550.00 USD | `-69.87%` | `150.57` |
| `Live` | `Long` | `18.25` | 3,030,000.00 USD | 0.00 USD | 2,190.00 USD | `-67.55%` | `120.00` |
| `Live` | `Long` | `19.05` | 3,030,000.00 USD | 0.00 USD | 3,470.00 USD | `-66.13%` | `182.00` |
| `Live` | `Long` | `19.35` | 3,020,000.00 USD | 0.00 USD | 155.77 USD | `-65.60%` | `8.05` |
| `Live` | `Long` | `19.45` | 3,020,000.00 USD | 0.00 USD | 2,010.00 USD | `-65.42%` | `103.47` |
| `Live` | `Long` | `20.45` | 3,020,000.00 USD | 0.00 USD | 19,020.00 USD | `-63.64%` | `930.00` |
| `Live` | `Long` | `20.95` | 3,000,000.00 USD | 0.00 USD | 465.93 USD | `-62.75%` | `22.24` |
| `Live` | `Long` | `21.65` | 3,000,000.00 USD | 0.00 USD | 4,220.00 USD | `-61.51%` | `195.03` |
| `Live` | `Long` | `22.35` | 3,000,000.00 USD | 0.00 USD | 147.51 USD | `-60.27%` | `6.60` |
| `Live` | `Long` | `22.75` | 3,000,000.00 USD | 0.00 USD | 366.96 USD | `-59.55%` | `16.13` |
| `Live` | `Long` | `23.55` | 3,000,000.00 USD | 0.00 USD | 1,410.00 USD | `-58.13%` | `60.00` |
| `Live` | `Long` | `23.65` | 3,000,000.00 USD | 0.00 USD | 1,220.00 USD | `-57.95%` | `51.45` |
| `Live` | `Long` | `23.85` | 3,000,000.00 USD | 0.00 USD | 195.57 USD | `-57.60%` | `8.20` |
| `Live` | `Long` | `24.05` | 2,990,000.00 USD | 0.00 USD | 380.47 USD | `-57.24%` | `15.82` |
| `Live` | `Long` | `24.65` | 2,990,000.00 USD | 0.00 USD | 466.13 USD | `-56.18%` | `18.91` |
| `Live` | `Long` | `25.25` | 2,990,000.00 USD | 0.00 USD | 277,980.00 USD | `-55.11%` | `11,009.19` |
| `Live` | `Long` | `25.35` | 2,720,000.00 USD | 0.00 USD | 173.39 USD | `-54.93%` | `6.84` |
| `Live` | `Long` | `25.45` | 2,720,000.00 USD | 0.00 USD | 7,500.00 USD | `-54.75%` | `294.67` |
| `Live` | `Long` | `25.55` | 2,710,000.00 USD | 0.00 USD | 50,740.00 USD | `-54.58%` | `1,985.99` |
| `Live` | `Long` | `25.75` | 2,660,000.00 USD | 0.00 USD | 117,590.00 USD | `-54.22%` | `4,566.66` |
| `Live` | `Long` | `25.95` | 2,540,000.00 USD | 0.00 USD | 374.20 USD | `-53.87%` | `14.42` |
| `Live` | `Long` | `26.05` | 2,540,000.00 USD | 0.00 USD | 1,010.00 USD | `-53.69%` | `38.92` |
| `Live` | `Long` | `27.05` | 2,540,000.00 USD | 0.00 USD | 5,510.00 USD | `-51.91%` | `203.85` |
| `Live` | `Long` | `27.55` | 2,530,000.00 USD | 0.00 USD | 272.75 USD | `-51.02%` | `9.90` |
| `Live` | `Long` | `27.95` | 2,530,000.00 USD | 0.00 USD | 173.85 USD | `-50.31%` | `6.22` |
| `Live` | `Long` | `28.15` | 2,530,000.00 USD | 0.00 USD | 166.37 USD | `-49.95%` | `5.91` |
| `Live` | `Long` | `28.25` | 2,530,000.00 USD | 0.00 USD | 8,470.00 USD | `-49.78%` | `300.00` |
| `Live` | `Long` | `28.95` | 2,520,000.00 USD | 0.00 USD | 802.20 USD | `-48.53%` | `27.71` |
| `Live` | `Long` | `29.15` | 2,520,000.00 USD | 0.00 USD | 583.00 USD | `-48.18%` | `20.00` |
| `Live` | `Long` | `29.75` | 2,520,000.00 USD | 0.00 USD | 297,500.00 USD | `-47.11%` | `10,000.00` |
| `Live` | `Long` | `30.05` | 2,230,000.00 USD | 0.00 USD | 218.46 USD | `-46.58%` | `7.27` |
| `Live` | `Long` | `30.65` | 2,230,000.00 USD | 0.00 USD | 1,540.00 USD | `-45.51%` | `50.19` |
| `Live` | `Long` | `30.95` | 2,220,000.00 USD | 0.00 USD | 538.53 USD | `-44.98%` | `17.40` |
| `Live` | `Long` | `31.15` | 2,220,000.00 USD | 0.00 USD | 5,880.00 USD | `-44.62%` | `188.85` |
| `Live` | `Long` | `31.55` | 2,220,000.00 USD | 0.00 USD | 1,060.00 USD | `-43.91%` | `33.49` |
| `Live` | `Long` | `31.65` | 2,220,000.00 USD | 0.00 USD | 4,640.00 USD | `-43.73%` | `146.53` |
| `Live` | `Long` | `31.85` | 2,210,000.00 USD | 0.00 USD | 3,460.00 USD | `-43.38%` | `108.75` |
| `Live` | `Long` | `31.95` | 2,210,000.00 USD | 0.00 USD | 125.24 USD | `-43.20%` | `3.92` |
| `Live` | `Long` | `32.05` | 2,210,000.00 USD | 0.00 USD | 2,740.00 USD | `-43.02%` | `85.43` |
| `Live` | `Long` | `32.15` | 2,210,000.00 USD | 0.00 USD | 450.10 USD | `-42.84%` | `14.00` |
| `Live` | `Long` | `32.35` | 2,200,000.00 USD | 0.00 USD | 22,750.00 USD | `-42.49%` | `703.27` |
| `Live` | `Long` | `32.65` | 2,180,000.00 USD | 0.00 USD | 653.00 USD | `-41.95%` | `20.00` |
| `Live` | `Long` | `32.75` | 2,180,000.00 USD | 0.00 USD | 5,020.00 USD | `-41.78%` | `153.13` |
| `Live` | `Long` | `32.85` | 2,180,000.00 USD | 0.00 USD | 32,850.00 USD | `-41.60%` | `1,000.01` |
| `Live` | `Long` | `33.15` | 2,140,000.00 USD | 0.00 USD | 232.05 USD | `-41.07%` | `7.00` |
| `Live` | `Long` | `33.65` | 2,140,000.00 USD | 0.00 USD | 257.76 USD | `-40.18%` | `7.66` |
| `Live` | `Long` | `33.95` | 2,140,000.00 USD | 0.00 USD | 5,910.00 USD | `-39.64%` | `174.22` |
| `Live` | `Long` | `34.05` | 2,140,000.00 USD | 0.00 USD | 182.85 USD | `-39.47%` | `5.37` |
| `Live` | `Long` | `34.15` | 2,140,000.00 USD | 0.00 USD | 126.70 USD | `-39.29%` | `3.71` |
| `Live` | `Long` | `34.45` | 2,140,000.00 USD | 0.00 USD | 65,890.00 USD | `-38.75%` | `1,912.61` |
| `Live` | `Long` | `34.65` | 2,070,000.00 USD | 0.00 USD | 7,770.00 USD | `-38.40%` | `224.19` |
| `Live` | `Long` | `34.95` | 2,060,000.00 USD | 0.00 USD | 104.85 USD | `-37.87%` | `3.00` |
| `Live` | `Long` | `35.05` | 2,060,000.00 USD | 0.00 USD | 166.49 USD | `-37.69%` | `4.75` |
| `Live` | `Long` | `35.45` | 2,060,000.00 USD | 0.00 USD | 422.56 USD | `-36.98%` | `11.92` |
| `Live` | `Long` | `35.65` | 2,060,000.00 USD | 0.00 USD | 178.25 USD | `-36.62%` | `5.00` |
| `Live` | `Long` | `36.35` | 2,060,000.00 USD | 0.00 USD | 3,020.00 USD | `-35.38%` | `83.03` |
| `Live` | `Long` | `36.45` | 2,060,000.00 USD | 0.00 USD | 708.59 USD | `-35.20%` | `19.44` |
| `Live` | `Long` | `36.75` | 2,060,000.00 USD | 0.00 USD | 101.80 USD | `-34.67%` | `2.77` |
| `Live` | `Long` | `36.85` | 2,060,000.00 USD | 0.00 USD | 319.49 USD | `-34.49%` | `8.67` |
| `Live` | `Long` | `37.15` | 2,060,000.00 USD | 0.00 USD | 438.74 USD | `-33.95%` | `11.81` |
| `Live` | `Long` | `37.25` | 2,060,000.00 USD | 0.00 USD | 1,050.00 USD | `-33.78%` | `28.27` |
| `Live` | `Long` | `37.35` | 2,060,000.00 USD | 0.00 USD | 9,260.00 USD | `-33.60%` | `247.91` |
| `Live` | `Long` | `37.55` | 2,050,000.00 USD | 0.00 USD | 3,530.00 USD | `-33.24%` | `94.04` |
| `Live` | `Long` | `37.75` | 2,040,000.00 USD | 0.00 USD | 377.50 USD | `-32.89%` | `10.00` |
| `Live` | `Long` | `37.85` | 2,040,000.00 USD | 0.00 USD | 6,210.00 USD | `-32.71%` | `164.03` |
| `Live` | `Long` | `37.95` | 2,040,000.00 USD | 0.00 USD | 446.67 USD | `-32.53%` | `11.77` |
| `Live` | `Long` | `38.25` | 2,040,000.00 USD | 0.00 USD | 695.38 USD | `-32.00%` | `18.18` |
| `Live` | `Long` | `38.35` | 2,040,000.00 USD | 0.00 USD | 2,770.00 USD | `-31.82%` | `72.10` |
| `Live` | `Long` | `38.45` | 2,030,000.00 USD | 0.00 USD | 2,400.00 USD | `-31.64%` | `62.34` |
| `Live` | `Long` | `38.55` | 2,030,000.00 USD | 0.00 USD | 993.82 USD | `-31.47%` | `25.78` |
| `Live` | `Long` | `38.65` | 2,030,000.00 USD | 0.00 USD | 5,290.00 USD | `-31.29%` | `136.74` |
| `Live` | `Long` | `38.95` | 2,020,000.00 USD | 0.00 USD | 2,730.00 USD | `-30.75%` | `70.00` |
| `Live` | `Long` | `39.05` | 2,020,000.00 USD | 0.00 USD | 664,760.00 USD | `-30.58%` | `17,023.28` |
| `Live` | `Long` | `39.15` | 1,360,000.00 USD | 0.00 USD | 570.02 USD | `-30.40%` | `14.56` |
| `Live` | `Long` | `39.35` | 1,360,000.00 USD | 0.00 USD | 264.83 USD | `-30.04%` | `6.73` |
| `Live` | `Long` | `39.45` | 1,360,000.00 USD | 0.00 USD | 716.41 USD | `-29.87%` | `18.16` |
| `Live` | `Long` | `39.55` | 1,360,000.00 USD | 0.00 USD | 312.44 USD | `-29.69%` | `7.90` |
| `Live` | `Long` | `39.65` | 1,360,000.00 USD | 0.00 USD | 5,900.00 USD | `-29.51%` | `148.78` |
| `Live` | `Long` | `39.75` | 1,350,000.00 USD | 0.00 USD | 1,180.00 USD | `-29.33%` | `29.57` |
| `Live` | `Long` | `39.85` | 1,350,000.00 USD | 0.00 USD | 133.10 USD | `-29.15%` | `3.34` |
| `Live` | `Long` | `40.05` | 1,350,000.00 USD | 0.00 USD | 2,160.00 USD | `-28.80%` | `53.97` |
| `Live` | `Long` | `40.45` | 1,350,000.00 USD | 0.00 USD | 1,010.00 USD | `-28.09%` | `24.92` |
| `Live` | `Long` | `40.55` | 1,340,000.00 USD | 0.00 USD | 133.00 USD | `-27.91%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,340,000.00 USD | 0.00 USD | 274.39 USD | `-27.73%` | `6.75` |
| `Live` | `Long` | `40.85` | 1,340,000.00 USD | 0.00 USD | 6,340.00 USD | `-27.38%` | `155.23` |
| `Live` | `Long` | `40.95` | 1,340,000.00 USD | 0.00 USD | 509.01 USD | `-27.20%` | `12.43` |
| `Live` | `Long` | `41.05` | 1,340,000.00 USD | 0.00 USD | 9,430.00 USD | `-27.02%` | `229.66` |
| `Live` | `Long` | `41.15` | 1,330,000.00 USD | 0.00 USD | 5,430.00 USD | `-26.84%` | `131.94` |
| `Live` | `Long` | `41.25` | 1,320,000.00 USD | 0.00 USD | 14,490.00 USD | `-26.67%` | `351.26` |
| `Live` | `Long` | `41.45` | 1,310,000.00 USD | 0.00 USD | 1,680.00 USD | `-26.31%` | `40.49` |
| `Live` | `Long` | `42.05` | 1,310,000.00 USD | 0.00 USD | 982.29 USD | `-25.24%` | `23.36` |
| `Live` | `Long` | `42.15` | 1,310,000.00 USD | 0.00 USD | 66,300.00 USD | `-25.07%` | `1,572.94` |
| `Live` | `Long` | `42.25` | 1,240,000.00 USD | 0.00 USD | 35,410.00 USD | `-24.89%` | `838.00` |
| `Live` | `Long` | `42.65` | 1,200,000.00 USD | 0.00 USD | 1,570.00 USD | `-24.18%` | `36.70` |
| `Live` | `Long` | `42.85` | 1,200,000.00 USD | 0.00 USD | 5,800.00 USD | `-23.82%` | `135.38` |
| `Live` | `Long` | `42.95` | 1,200,000.00 USD | 0.00 USD | 2,000.00 USD | `-23.64%` | `46.65` |
| `Live` | `Long` | `43.05` | 1,190,000.00 USD | 0.00 USD | 56,340.00 USD | `-23.47%` | `1,308.73` |
| `Live` | `Long` | `43.15` | 1,140,000.00 USD | 0.00 USD | 122,400.00 USD | `-23.29%` | `2,836.59` |
| `Live` | `Long` | `43.25` | 1,020,000.00 USD | 0.00 USD | 417.80 USD | `-23.11%` | `9.66` |
| `Live` | `Long` | `43.35` | 1,020,000.00 USD | 0.00 USD | 5,390.00 USD | `-22.93%` | `124.24` |
| `Live` | `Long` | `43.45` | 1,010,000.00 USD | 0.00 USD | 6,900.00 USD | `-22.75%` | `158.78` |
| `Live` | `Long` | `43.65` | 1,000,000.00 USD | 0.00 USD | 426.02 USD | `-22.40%` | `9.76` |
| `Live` | `Long` | `43.75` | 1,000,000.00 USD | 0.00 USD | 21,880.00 USD | `-22.22%` | `500.00` |
| `Live` | `Long` | `43.85` | 980,720.00 USD | 0.00 USD | 801.14 USD | `-22.04%` | `18.27` |
| `Live` | `Long` | `43.95` | 979,910.00 USD | 0.00 USD | 3,490.00 USD | `-21.87%` | `79.49` |
| `Live` | `Long` | `44.15` | 976,420.00 USD | 0.00 USD | 2,910.00 USD | `-21.51%` | `65.89` |
| `Live` | `Long` | `44.35` | 973,510.00 USD | 0.00 USD | 84,440.00 USD | `-21.15%` | `1,903.87` |
| `Live` | `Long` | `44.45` | 889,080.00 USD | 0.00 USD | 1,330.00 USD | `-20.98%` | `30.00` |
| `Live` | `Long` | `44.55` | 887,740.00 USD | 0.00 USD | 842.44 USD | `-20.80%` | `18.91` |
| `Live` | `Long` | `44.75` | 886,900.00 USD | 0.00 USD | 4,230.00 USD | `-20.44%` | `94.55` |
| `Live` | `Long` | `44.85` | 882,670.00 USD | 0.00 USD | 134.55 USD | `-20.27%` | `3.00` |
| `Live` | `Long` | `44.95` | 882,530.00 USD | 0.00 USD | 2,620.00 USD | `-20.09%` | `58.18` |
| `Live` | `Long` | `45.05` | 879,920.00 USD | 0.00 USD | 6,190.00 USD | `-19.91%` | `137.31` |
| `Live` | `Long` | `45.15` | 873,730.00 USD | 0.00 USD | 8,710.00 USD | `-19.73%` | `193.00` |
| `Live` | `Long` | `45.25` | 865,020.00 USD | 0.00 USD | 30,370.00 USD | `-19.55%` | `671.05` |
| `Live` | `Long` | `45.35` | 834,650.00 USD | 0.00 USD | 2,180.00 USD | `-19.38%` | `48.02` |
| `Live` | `Long` | `45.45` | 832,480.00 USD | 0.00 USD | 23,940.00 USD | `-19.20%` | `526.65` |
| `Live` | `Long` | `45.55` | 808,540.00 USD | 0.00 USD | 12,060.00 USD | `-19.02%` | `264.81` |
| `Live` | `Long` | `45.65` | 796,480.00 USD | 0.00 USD | 42,180.00 USD | `-18.84%` | `924.03` |
| `Live` | `Long` | `45.95` | 754,300.00 USD | 0.00 USD | 2,940.00 USD | `-18.31%` | `64.09` |
| `Live` | `Long` | `46.05` | 751,350.00 USD | 0.00 USD | 706.41 USD | `-18.13%` | `15.34` |
| `Live` | `Long` | `46.15` | 750,640.00 USD | 0.00 USD | 1,070.00 USD | `-17.95%` | `23.23` |
| `Live` | `Long` | `46.25` | 749,570.00 USD | 0.00 USD | 842.21 USD | `-17.78%` | `18.21` |
| `Live` | `Long` | `46.35` | 748,730.00 USD | 0.00 USD | 22,820.00 USD | `-17.60%` | `492.25` |
| `Live` | `Long` | `46.55` | 725,910.00 USD | 0.00 USD | 2,140.00 USD | `-17.24%` | `45.93` |
| `Live` | `Long` | `46.65` | 723,780.00 USD | 0.00 USD | 3,980.00 USD | `-17.07%` | `85.41` |
| `Live` | `Long` | `46.85` | 719,790.00 USD | 0.00 USD | 358.40 USD | `-16.71%` | `7.65` |
| `Live` | `Long` | `46.95` | 719,430.00 USD | 0.00 USD | 158.22 USD | `-16.53%` | `3.37` |
| `Live` | `Long` | `47.15` | 719,280.00 USD | 0.00 USD | 1,980.00 USD | `-16.18%` | `42.07` |
| `Live` | `Long` | `47.25` | 717,290.00 USD | 0.00 USD | 1,220.00 USD | `-16.00%` | `25.84` |
| `Live` | `Long` | `47.35` | 716,070.00 USD | 0.00 USD | 43,340.00 USD | `-15.82%` | `915.41` |
| `Live` | `Long` | `47.45` | 672,730.00 USD | 0.00 USD | 2,860.00 USD | `-15.64%` | `60.30` |
| `Live` | `Long` | `47.55` | 669,860.00 USD | 0.00 USD | 4,450.00 USD | `-15.47%` | `93.69` |
| `Live` | `Long` | `47.75` | 665,410.00 USD | 0.00 USD | 47,930.00 USD | `-15.11%` | `1,003.84` |
| `Live` | `Long` | `48.05` | 617,480.00 USD | 0.00 USD | 1,340.00 USD | `-14.58%` | `27.93` |
| `Live` | `Long` | `48.15` | 616,130.00 USD | 0.00 USD | 1,690.00 USD | `-14.40%` | `35.03` |
| `Live` | `Long` | `48.25` | 614,450.00 USD | 0.00 USD | 110.49 USD | `-14.22%` | `2.29` |
| `Live` | `Long` | `48.35` | 614,340.00 USD | 0.00 USD | 7,960.00 USD | `-14.04%` | `164.58` |
| `Live` | `Long` | `48.55` | 606,380.00 USD | 0.00 USD | 2,560.00 USD | `-13.69%` | `52.70` |
| `Live` | `Long` | `48.65` | 603,820.00 USD | 0.00 USD | 2,160.00 USD | `-13.51%` | `44.42` |
| `Live` | `Long` | `48.75` | 601,660.00 USD | 0.00 USD | 333.94 USD | `-13.33%` | `6.85` |
| `Live` | `Long` | `48.95` | 601,330.00 USD | 0.00 USD | 252.58 USD | `-12.98%` | `5.16` |
| `Live` | `Long` | `49.05` | 601,070.00 USD | 0.00 USD | 1,580.00 USD | `-12.80%` | `32.25` |
| `Live` | `Long` | `49.15` | 599,490.00 USD | 0.00 USD | 5,740.00 USD | `-12.62%` | `116.83` |
| `Live` | `Long` | `49.35` | 593,750.00 USD | 0.00 USD | 5,230.00 USD | `-12.27%` | `105.97` |
| `Live` | `Long` | `49.45` | 588,520.00 USD | 0.00 USD | 419.34 USD | `-12.09%` | `8.48` |
| `Live` | `Long` | `49.55` | 588,100.00 USD | 0.00 USD | 18,010.00 USD | `-11.91%` | `363.57` |
| `Live` | `Long` | `49.65` | 570,090.00 USD | 0.00 USD | 73,260.00 USD | `-11.73%` | `1,475.52` |
| `Live` | `Long` | `49.75` | 496,830.00 USD | 0.00 USD | 20,710.00 USD | `-11.55%` | `416.36` |
| `Live` | `Long` | `49.95` | 476,110.00 USD | 0.00 USD | 19,920.00 USD | `-11.20%` | `398.70` |
| `Live` | `Long` | `50.05` | 456,200.00 USD | 0.00 USD | 1,820.00 USD | `-11.02%` | `36.43` |
| `Live` | `Long` | `50.25` | 454,370.00 USD | 0.00 USD | 102.51 USD | `-10.67%` | `2.04` |
| `Live` | `Long` | `50.35` | 454,270.00 USD | 0.00 USD | 1,140.00 USD | `-10.49%` | `22.67` |
| `Live` | `Long` | `50.45` | 453,130.00 USD | 0.00 USD | 4,720.00 USD | `-10.31%` | `93.64` |
| `Live` | `Long` | `50.55` | 448,410.00 USD | 0.00 USD | 84,100.00 USD | `-10.13%` | `1,663.61` |
| `Live` | `Long` | `50.75` | 364,310.00 USD | 0.00 USD | 9,050.00 USD | `-9.78%` | `178.28` |
| `Live` | `Long` | `50.95` | 355,260.00 USD | 0.00 USD | 431.55 USD | `-9.42%` | `8.47` |
| `Live` | `Long` | `51.15` | 354,830.00 USD | 0.00 USD | 219,370.00 USD | `-9.07%` | `4,288.79` |
| `Live` | `Long` | `51.25` | 135,460.00 USD | 0.00 USD | 202.44 USD | `-8.89%` | `3.95` |
| `Live` | `Long` | `51.35` | 135,260.00 USD | 0.00 USD | 453.93 USD | `-8.71%` | `8.84` |
| `Live` | `Long` | `51.45` | 134,800.00 USD | 0.00 USD | 27,210.00 USD | `-8.53%` | `528.81` |
| `Live` | `Long` | `51.55` | 107,600.00 USD | 0.00 USD | 551.07 USD | `-8.35%` | `10.69` |
| `Live` | `Long` | `51.65` | 107,040.00 USD | 0.00 USD | 9,100.00 USD | `-8.18%` | `176.09` |
| `Live` | `Long` | `51.75` | 97,950.00 USD | 0.00 USD | 6,480.00 USD | `-8.00%` | `125.17` |
| `Live` | `Long` | `51.85` | 91,470.00 USD | 0.00 USD | 13,680.00 USD | `-7.82%` | `263.89` |
| `Live` | `Long` | `51.95` | 77,790.00 USD | 0.00 USD | 16,800.00 USD | `-7.64%` | `323.48` |
| `Live` | `Long` | `52.15` | 60,980.00 USD | 0.00 USD | 1,900.00 USD | `-7.29%` | `36.36` |
| `Live` | `Long` | `52.25` | 59,090.00 USD | 0.00 USD | 4,930.00 USD | `-7.11%` | `94.33` |
| `Live` | `Long` | `52.35` | 54,160.00 USD | 0.00 USD | 134.02 USD | `-6.93%` | `2.56` |
| `Live` | `Long` | `52.45` | 54,030.00 USD | 0.00 USD | 7,570.00 USD | `-6.75%` | `144.25` |
| `Live` | `Long` | `52.55` | 46,460.00 USD | 0.00 USD | 8,700.00 USD | `-6.58%` | `165.49` |
| `Live` | `Long` | `52.75` | 37,760.00 USD | 0.00 USD | 4,240.00 USD | `-6.22%` | `80.44` |
| `Live` | `Long` | `52.85` | 33,520.00 USD | 0.00 USD | 5,950.00 USD | `-6.04%` | `112.64` |
| `Live` | `Long` | `52.95` | 27,570.00 USD | 0.00 USD | 25,840.00 USD | `-5.86%` | `488.06` |
| `Live` | `Long` | `53.15` | 1,720.00 USD | 0.00 USD | 1,720.00 USD | `-5.51%` | `32.44` |
| `Live` | `Short` | `57.75` | 155.35 USD | 155.35 USD | 0.00 USD | `+2.67%` | `2.69` |
| `Live` | `Short` | `57.95` | 281.10 USD | 125.75 USD | 0.00 USD | `+3.02%` | `2.17` |
| `Live` | `Short` | `58.05` | 201,870.00 USD | 201,590.00 USD | 0.00 USD | `+3.20%` | `3,472.67` |
| `Live` | `Short` | `59.35` | 211,310.00 USD | 9,440.00 USD | 0.00 USD | `+5.51%` | `159.09` |
| `Live` | `Short` | `60.95` | 211,710.00 USD | 397.39 USD | 0.00 USD | `+8.36%` | `6.52` |
| `Live` | `Short` | `61.15` | 215,580.00 USD | 3,870.00 USD | 0.00 USD | `+8.71%` | `63.26` |
| `Live` | `Short` | `62.95` | 215,720.00 USD | 138.49 USD | 0.00 USD | `+11.91%` | `2.20` |
| `Live` | `Short` | `63.45` | 219,070.00 USD | 3,350.00 USD | 0.00 USD | `+12.80%` | `52.83` |
| `Live` | `Short` | `65.95` | 219,310.00 USD | 246.65 USD | 0.00 USD | `+17.25%` | `3.74` |
| `Live` | `Short` | `66.15` | 226,070.00 USD | 6,750.00 USD | 0.00 USD | `+17.60%` | `102.07` |
| `Live` | `Short` | `66.95` | 226,190.00 USD | 121.18 USD | 0.00 USD | `+19.02%` | `1.81` |
| `Live` | `Short` | `67.85` | 226,900.00 USD | 709.03 USD | 0.00 USD | `+20.62%` | `10.45` |
| `Live` | `Short` | `69.85` | 267,280.00 USD | 40,380.00 USD | 0.00 USD | `+24.18%` | `578.10` |
| `Live` | `Short` | `76.35` | 275,660.00 USD | 8,380.00 USD | 0.00 USD | `+35.74%` | `109.80` |
| `Live` | `Short` | `77.75` | 854,120.00 USD | 578,460.00 USD | 0.00 USD | `+38.22%` | `7,440.05` |
| `Live` | `Short` | `77.85` | 854,730.00 USD | 602.56 USD | 0.00 USD | `+38.40%` | `7.74` |
| `Live` | `Short` | `77.95` | 854,860.00 USD | 136.41 USD | 0.00 USD | `+38.58%` | `1.75` |
| `Live` | `Short` | `80.45` | 855,590.00 USD | 729.68 USD | 0.00 USD | `+43.02%` | `9.07` |
| `Live` | `Short` | `80.75` | 856,240.00 USD | 646.00 USD | 0.00 USD | `+43.56%` | `8.00` |
| `Live` | `Short` | `80.95` | 858,910.00 USD | 2,670.00 USD | 0.00 USD | `+43.91%` | `33.00` |
| `Live` | `Short` | `81.05` | 877,910.00 USD | 19,000.00 USD | 0.00 USD | `+44.09%` | `234.42` |
| `Live` | `Short` | `81.55` | 878,030.00 USD | 123.96 USD | 0.00 USD | `+44.98%` | `1.52` |
| `Live` | `Short` | `82.75` | 881,560.00 USD | 3,520.00 USD | 0.00 USD | `+47.11%` | `42.59` |
| `Live` | `Short` | `87.45` | 904,890.00 USD | 23,330.00 USD | 0.00 USD | `+55.47%` | `266.81` |
| `Live` | `Short` | `90.95` | 905,010.00 USD | 120.05 USD | 0.00 USD | `+61.69%` | `1.32` |
| `Live` | `Short` | `91.65` | 905,980.00 USD | 974.24 USD | 0.00 USD | `+62.94%` | `10.63` |
| `Live` | `Short` | `98.65` | 908,450.00 USD | 2,470.00 USD | 0.00 USD | `+75.38%` | `25.00` |
| `Live` | `Short` | `104.25` | 908,660.00 USD | 213.71 USD | 0.00 USD | `+85.34%` | `2.05` |
| `Live` | `Short` | `104.85` | 910,990.00 USD | 2,320.00 USD | 0.00 USD | `+86.40%` | `22.13` |
| `Live` | `Short` | `105.25` | 1,270,000.00 USD | 355,110.00 USD | 0.00 USD | `+87.11%` | `3,374.01` |
| `Live` | `Short` | `105.35` | 1,300,000.00 USD | 31,610.00 USD | 0.00 USD | `+87.29%` | `300.00` |
| `Live` | `Short` | `106.75` | 1,300,000.00 USD | 1,620.00 USD | 0.00 USD | `+89.78%` | `15.16` |
| `Live` | `Short` | `106.85` | 1,300,000.00 USD | 1,860.00 USD | 0.00 USD | `+89.96%` | `17.43` |
| `Live` | `Short` | `107.15` | 1,300,000.00 USD | 199.30 USD | 0.00 USD | `+90.49%` | `1.86` |
| `Live` | `Short` | `108.05` | 1,310,000.00 USD | 6,470.00 USD | 0.00 USD | `+92.09%` | `59.91` |
| `Live` | `Short` | `110.95` | 1,310,000.00 USD | 664.59 USD | 0.00 USD | `+97.25%` | `5.99` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 813,690.00 USD | 0.00 USD | 392.18 USD | `-64.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 813,290.00 USD | 0.00 USD | 2,310.00 USD | `-60.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 810,990.00 USD | 0.00 USD | 806.86 USD | `-55.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 810,180.00 USD | 0.00 USD | 1,560.00 USD | `-54.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 808,620.00 USD | 0.00 USD | 410.25 USD | `-51.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 808,210.00 USD | 0.00 USD | 281.57 USD | `-46.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 807,930.00 USD | 0.00 USD | 36,050.00 USD | `-35.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 771,880.00 USD | 0.00 USD | 37,550.00 USD | `-33.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 734,330.00 USD | 0.00 USD | 447.01 USD | `-32.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.35` | 733,880.00 USD | 0.00 USD | 73,350.00 USD | `-31.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 660,540.00 USD | 0.00 USD | 40,560.00 USD | `-30.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 619,980.00 USD | 0.00 USD | 489.57 USD | `-29.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 619,490.00 USD | 0.00 USD | 1,180.00 USD | `-28.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 618,310.00 USD | 0.00 USD | 9,840.00 USD | `-28.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 608,470.00 USD | 0.00 USD | 2,060.00 USD | `-27.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.05` | 606,420.00 USD | 0.00 USD | 2,060.00 USD | `-27.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 604,360.00 USD | 0.00 USD | 2,960.00 USD | `-26.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 601,400.00 USD | 0.00 USD | 4,010.00 USD | `-25.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.65` | 597,390.00 USD | 0.00 USD | 3,000.00 USD | `-24.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 594,380.00 USD | 0.00 USD | 5,680.00 USD | `-23.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 588,700.00 USD | 0.00 USD | 672.22 USD | `-22.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.35` | 588,030.00 USD | 0.00 USD | 329,970.00 USD | `-21.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 258,060.00 USD | 0.00 USD | 213.80 USD | `-20.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 257,850.00 USD | 0.00 USD | 223.20 USD | `-20.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 257,630.00 USD | 0.00 USD | 391.13 USD | `-20.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 257,240.00 USD | 0.00 USD | 7,080.00 USD | `-19.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 250,160.00 USD | 0.00 USD | 1,370.00 USD | `-19.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 248,790.00 USD | 0.00 USD | 553.80 USD | `-17.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.35` | 248,240.00 USD | 0.00 USD | 2,970.00 USD | `-17.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.45` | 245,270.00 USD | 0.00 USD | 3,080.00 USD | `-17.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 242,190.00 USD | 0.00 USD | 14,000.00 USD | `-17.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 228,200.00 USD | 0.00 USD | 158.56 USD | `-16.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 228,040.00 USD | 0.00 USD | 373.28 USD | `-16.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 227,660.00 USD | 0.00 USD | 849.46 USD | `-15.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 226,810.00 USD | 0.00 USD | 1,150.00 USD | `-14.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 225,660.00 USD | 0.00 USD | 129.25 USD | `-14.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.15` | 225,540.00 USD | 0.00 USD | 303.35 USD | `-14.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 225,230.00 USD | 0.00 USD | 1,740.00 USD | `-13.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 223,490.00 USD | 0.00 USD | 981.00 USD | `-12.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.35` | 222,510.00 USD | 0.00 USD | 817.24 USD | `-12.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 221,690.00 USD | 0.00 USD | 237.85 USD | `-12.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.55` | 221,460.00 USD | 0.00 USD | 1,420.00 USD | `-11.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.85` | 220,040.00 USD | 0.00 USD | 108.17 USD | `-11.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 219,930.00 USD | 0.00 USD | 298.20 USD | `-11.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 219,630.00 USD | 0.00 USD | 34,670.00 USD | `-11.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 184,960.00 USD | 0.00 USD | 6,410.00 USD | `-10.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 178,540.00 USD | 0.00 USD | 459.70 USD | `-10.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 178,080.00 USD | 0.00 USD | 236.57 USD | `-10.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 177,850.00 USD | 0.00 USD | 1,020.00 USD | `-9.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 176,830.00 USD | 0.00 USD | 439.89 USD | `-9.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.45` | 176,390.00 USD | 0.00 USD | 204.26 USD | `-8.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 176,180.00 USD | 0.00 USD | 10,190.00 USD | `-8.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.85` | 166,000.00 USD | 0.00 USD | 106.29 USD | `-7.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.95` | 165,890.00 USD | 0.00 USD | 8,700.00 USD | `-7.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 157,190.00 USD | 0.00 USD | 26,490.00 USD | `-7.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.25` | 130,700.00 USD | 0.00 USD | 140.03 USD | `-7.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 130,560.00 USD | 0.00 USD | 70,190.00 USD | `-6.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 60,370.00 USD | 0.00 USD | 5,460.00 USD | `-6.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 54,910.00 USD | 0.00 USD | 271.13 USD | `-6.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.85` | 54,640.00 USD | 0.00 USD | 2,840.00 USD | `-6.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 51,790.00 USD | 0.00 USD | 115.43 USD | `-5.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 51,680.00 USD | 0.00 USD | 9,240.00 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 42,440.00 USD | 0.00 USD | 2,660.00 USD | `-5.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.25` | 39,780.00 USD | 0.00 USD | 881.82 USD | `-5.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 38,900.00 USD | 0.00 USD | 566.57 USD | `-4.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 38,330.00 USD | 0.00 USD | 5,950.00 USD | `-4.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 32,380.00 USD | 0.00 USD | 1,370.00 USD | `-4.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.75` | 31,010.00 USD | 0.00 USD | 1,120.00 USD | `-4.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 29,890.00 USD | 0.00 USD | 462.03 USD | `-4.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 29,430.00 USD | 0.00 USD | 895.07 USD | `-3.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.15` | 28,530.00 USD | 0.00 USD | 398.54 USD | `-3.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 28,130.00 USD | 0.00 USD | 3,090.00 USD | `-3.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 25,050.00 USD | 0.00 USD | 156.53 USD | `-3.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.45` | 24,890.00 USD | 0.00 USD | 144.29 USD | `-3.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.55` | 24,750.00 USD | 0.00 USD | 1,690.00 USD | `-3.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.65` | 23,050.00 USD | 0.00 USD | 14,930.00 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.75` | 8,120.00 USD | 0.00 USD | 198.74 USD | `-2.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 7,920.00 USD | 0.00 USD | 398.21 USD | `-2.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.95` | 7,520.00 USD | 0.00 USD | 397.84 USD | `-2.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 7,130.00 USD | 0.00 USD | 160.75 USD | `-2.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.15` | 6,970.00 USD | 0.00 USD | 398.18 USD | `-1.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.25` | 6,570.00 USD | 0.00 USD | 398.90 USD | `-1.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.35` | 6,170.00 USD | 0.00 USD | 407.38 USD | `-1.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.45` | 5,760.00 USD | 0.00 USD | 408.11 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.55` | 5,350.00 USD | 0.00 USD | 156.65 USD | `-1.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.65` | 5,200.00 USD | 0.00 USD | 3,610.00 USD | `-1.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.75` | 1,580.00 USD | 0.00 USD | 202.37 USD | `-0.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.85` | 1,380.00 USD | 0.00 USD | 149.68 USD | `-0.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.95` | 1,230.00 USD | 0.00 USD | 193.03 USD | `-0.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 1,040.00 USD | 0.00 USD | 632.24 USD | `-0.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 407.65 USD | 0.00 USD | 407.65 USD | `-0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.25` | 204.19 USD | 204.19 USD | 0.00 USD | `+0.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.35` | 591.31 USD | 387.12 USD | 0.00 USD | `+0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.45` | 998.88 USD | 407.57 USD | 0.00 USD | `+0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.55` | 3,640.00 USD | 2,640.00 USD | 0.00 USD | `+0.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.65` | 3,760.00 USD | 121.23 USD | 0.00 USD | `+0.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.75` | 3,990.00 USD | 228.70 USD | 0.00 USD | `+0.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.85` | 22,020.00 USD | 18,030.00 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.95` | 22,410.00 USD | 390.68 USD | 0.00 USD | `+1.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.15` | 22,800.00 USD | 392.05 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.25` | 23,000.00 USD | 201.52 USD | 0.00 USD | `+1.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.35` | 23,210.00 USD | 207.03 USD | 0.00 USD | `+1.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.45` | 23,550.00 USD | 344.70 USD | 0.00 USD | `+2.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.55` | 43,910.00 USD | 20,360.00 USD | 0.00 USD | `+2.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.65` | 44,030.00 USD | 118.18 USD | 0.00 USD | `+2.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.75` | 44,150.00 USD | 119.54 USD | 0.00 USD | `+2.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.95` | 44,280.00 USD | 128.65 USD | 0.00 USD | `+3.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 45,020.00 USD | 747.68 USD | 0.00 USD | `+3.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 45,220.00 USD | 200.04 USD | 0.00 USD | `+3.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 45,430.00 USD | 200.96 USD | 0.00 USD | `+3.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 45,550.00 USD | 123.70 USD | 0.00 USD | `+3.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 46,150.00 USD | 601.45 USD | 0.00 USD | `+3.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 46,760.00 USD | 611.85 USD | 0.00 USD | `+4.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.65` | 47,040.00 USD | 274.48 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 47,530.00 USD | 491.15 USD | 0.00 USD | `+4.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 50,470.00 USD | 2,940.00 USD | 0.00 USD | `+4.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 50,600.00 USD | 129.69 USD | 0.00 USD | `+4.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 55,400.00 USD | 4,800.00 USD | 0.00 USD | `+4.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 56,680.00 USD | 1,280.00 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.25` | 56,890.00 USD | 210.34 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 57,350.00 USD | 461.74 USD | 0.00 USD | `+5.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 57,510.00 USD | 159.92 USD | 0.00 USD | `+5.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.55` | 58,010.00 USD | 496.65 USD | 0.00 USD | `+5.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 58,730.00 USD | 724.75 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 58,890.00 USD | 158.00 USD | 0.00 USD | `+6.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 59,060.00 USD | 171.14 USD | 0.00 USD | `+6.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 59,610.00 USD | 551.00 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.45` | 59,770.00 USD | 155.36 USD | 0.00 USD | `+7.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 60,650.00 USD | 878.58 USD | 0.00 USD | `+7.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 62,030.00 USD | 1,390.00 USD | 0.00 USD | `+7.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 63,020.00 USD | 986.99 USD | 0.00 USD | `+8.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 63,690.00 USD | 674.72 USD | 0.00 USD | `+8.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 66,060.00 USD | 2,360.00 USD | 0.00 USD | `+8.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 66,180.00 USD | 125.56 USD | 0.00 USD | `+8.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 69,780.00 USD | 3,600.00 USD | 0.00 USD | `+9.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 70,420.00 USD | 643.20 USD | 0.00 USD | `+9.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 70,550.00 USD | 130.31 USD | 0.00 USD | `+10.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 71,270.00 USD | 716.72 USD | 0.00 USD | `+11.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 71,500.00 USD | 231.39 USD | 0.00 USD | `+12.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 72,130.00 USD | 630.87 USD | 0.00 USD | `+12.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 72,830.00 USD | 703.97 USD | 0.00 USD | `+12.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 73,500.00 USD | 668.13 USD | 0.00 USD | `+12.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 82,230.00 USD | 8,730.00 USD | 0.00 USD | `+12.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 82,790.00 USD | 555.03 USD | 0.00 USD | `+13.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 83,320.00 USD | 531.62 USD | 0.00 USD | `+13.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.35` | 83,980.00 USD | 664.09 USD | 0.00 USD | `+14.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.45` | 84,650.00 USD | 665.12 USD | 0.00 USD | `+14.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 84,850.00 USD | 202.69 USD | 0.00 USD | `+14.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 85,150.00 USD | 298.04 USD | 0.00 USD | `+14.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 85,250.00 USD | 102.13 USD | 0.00 USD | `+15.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 85,790.00 USD | 540.09 USD | 0.00 USD | `+15.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 85,890.00 USD | 100.79 USD | 0.00 USD | `+16.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 86,160.00 USD | 262.20 USD | 0.00 USD | `+16.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 86,530.00 USD | 371.49 USD | 0.00 USD | `+16.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 87,220.00 USD | 696.17 USD | 0.00 USD | `+17.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 87,760.00 USD | 534.00 USD | 0.00 USD | `+18.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 98,840.00 USD | 11,080.00 USD | 0.00 USD | `+19.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 105,540.00 USD | 6,710.00 USD | 0.00 USD | `+19.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.05` | 107,900.00 USD | 2,360.00 USD | 0.00 USD | `+20.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 112,770.00 USD | 4,860.00 USD | 0.00 USD | `+21.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 112,970.00 USD | 204.48 USD | 0.00 USD | `+23.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.65` | 631,170.00 USD | 518,200.00 USD | 0.00 USD | `+23.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 631,980.00 USD | 810.02 USD | 0.00 USD | `+24.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 955,440.00 USD | 323,460.00 USD | 0.00 USD | `+24.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 955,610.00 USD | 170.04 USD | 0.00 USD | `+25.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 961,370.00 USD | 5,770.00 USD | 0.00 USD | `+26.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 961,640.00 USD | 269.28 USD | 0.00 USD | `+26.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 961,930.00 USD | 291.40 USD | 0.00 USD | `+27.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 969,150.00 USD | 7,220.00 USD | 0.00 USD | `+28.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 969,310.00 USD | 156.78 USD | 0.00 USD | `+28.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 972,530.00 USD | 3,220.00 USD | 0.00 USD | `+29.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 972,940.00 USD | 411.14 USD | 0.00 USD | `+30.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 1,100,000.00 USD | 123,190.00 USD | 0.00 USD | `+31.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 1,100,000.00 USD | 1,020.00 USD | 0.00 USD | `+32.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.75` | 1,100,000.00 USD | 811.04 USD | 0.00 USD | `+32.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 1,100,000.00 USD | 104.93 USD | 0.00 USD | `+33.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 1,100,000.00 USD | 133.59 USD | 0.00 USD | `+33.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 1,100,000.00 USD | 402.59 USD | 0.00 USD | `+33.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.85` | 1,100,000.00 USD | 308.71 USD | 0.00 USD | `+34.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 1,100,000.00 USD | 315.18 USD | 0.00 USD | `+37.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 1,160,000.00 USD | 59,310.00 USD | 0.00 USD | `+39.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 1,160,000.00 USD | 3,160.00 USD | 0.00 USD | `+40.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.35` | 1,170,000.00 USD | 5,260.00 USD | 0.00 USD | `+41.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 1,170,000.00 USD | 5,690.00 USD | 0.00 USD | `+41.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 1,210,000.00 USD | 36,590.00 USD | 0.00 USD | `+42.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 1,210,000.00 USD | 433.89 USD | 0.00 USD | `+43.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 1,210,000.00 USD | 172.64 USD | 0.00 USD | `+44.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 1,210,000.00 USD | 164.10 USD | 0.00 USD | `+45.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 1,210,000.00 USD | 546.81 USD | 0.00 USD | `+47.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 1,210,000.00 USD | 2,300.00 USD | 0.00 USD | `+49.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 1,220,000.00 USD | 12,070.00 USD | 0.00 USD | `+51.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.05` | 1,250,000.00 USD | 20,230.00 USD | 0.00 USD | `+54.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 1,250,000.00 USD | 1,580.00 USD | 0.00 USD | `+56.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 1,280,000.00 USD | 37,000.00 USD | 0.00 USD | `+56.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 1,280,000.00 USD | 473.21 USD | 0.00 USD | `+58.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 1,280,000.00 USD | 422.99 USD | 0.00 USD | `+58.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 1,290,000.00 USD | 1,630.00 USD | 0.00 USD | `+59.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 1,290,000.00 USD | 4,870.00 USD | 0.00 USD | `+60.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 1,290,000.00 USD | 481.55 USD | 0.00 USD | `+62.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 1,290,000.00 USD | 1,330.00 USD | 0.00 USD | `+63.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 1,290,000.00 USD | 188.10 USD | 0.00 USD | `+67.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,560,000.00 USD | 266,140.00 USD | 0.00 USD | `+68.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,560,000.00 USD | 3,400.00 USD | 0.00 USD | `+69.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,580,000.00 USD | 21,930.00 USD | 0.00 USD | `+70.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,580,000.00 USD | 294.15 USD | 0.00 USD | `+74.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 1,600,000.00 USD | 15,380.00 USD | 0.00 USD | `+76.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,600,000.00 USD | 3,660.00 USD | 0.00 USD | `+77.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,600,000.00 USD | 306.15 USD | 0.00 USD | `+81.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,610,000.00 USD | 936.72 USD | 0.00 USD | `+83.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,610,000.00 USD | 2,920.00 USD | 0.00 USD | `+83.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,610,000.00 USD | 324.15 USD | 0.00 USD | `+92.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 1,610,000.00 USD | 123.23 USD | 0.00 USD | `+93.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 1,700,000.00 USD | 89,110.00 USD | 0.00 USD | `+97.43%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `417.48M` | Total OI Tokens: `7,484,064.3 LTC`
  * 1h OI Change: `+0.51%` | 4h OI Change: `+0.45%` | 24h OI Change: `-6.61%`
  * Exchange Breakdown: Binance=`73.54M` | Bybit=`66.34M` | OKX=`33.83M` | Hyperliquid=`22.30M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `11.63K` | Last 24h: `31.76K` | Last 3d: `59.78K` | Last 7d: `115.16K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0024%` |
| **USDT Bybit** | `0.0066%` | **USDT KuCoin** | `0.0073%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0058%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `44.34%` | `55.66%` | `0.80` | 10,290,000.00 USD |
| `15M` | `Binance` | `44.07%` | `55.93%` | `0.79` | 4,650,000.00 USD |
| `15M` | `OKX` | `46.53%` | `53.47%` | `0.87` | 1,300,000.00 USD |
| `15M` | `Bybit` | `51.39%` | `48.61%` | `1.06` | 1,900,000.00 USD |
| `15M` | `KuCoin` | `44.52%` | `55.48%` | `0.80` | 95,680.00 USD |
| `15M` | `Gate` | `45.12%` | `54.88%` | `0.82` | 228,440.00 USD |
| `15M` | `Bitget` | `30.63%` | `69.37%` | `0.44` | 328,210.00 USD |
| `15M` | `BingX` | `14.08%` | `85.92%` | `0.16` | 257,330.00 USD |
| `15M` | `MEXC` | `41.63%` | `58.37%` | `0.71` | 715,660.00 USD |
| `15M` | `Bitunix` | `30.11%` | `69.89%` | `0.43` | 434,480.00 USD |
| `15M` | `Hyperliquid` | `20.36%` | `79.64%` | `0.26` | 149,040.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `74.06%` | `25.94%` | `2.86` | 118,830.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 65,420.00 USD |
| `15M` | `HTX` | `34.07%` | `65.93%` | `0.52` | 6,250.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `77.22%` | `22.78%` | `3.39` | 45,970.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `56.49%` | `43.51%` | `1.30` | 10,820.00 USD |
| `15M` | `Whale Positions` | `44.07%` | `55.93%` | `0.79` | 4,650,000.00 USD |
| `15M` | `Global Accounts` | `44.34%` | `55.66%` | `0.80` | 10,290,000.00 USD |
| `1H` | `LTC` | `47.91%` | `52.09%` | `0.92` | 41,230,000.00 USD |
| `1H` | `Binance` | `48.82%` | `51.18%` | `0.95` | 16,900,000.00 USD |
| `1H` | `OKX` | `50.45%` | `49.55%` | `1.02` | 4,600,000.00 USD |
| `1H` | `Bybit` | `54.07%` | `45.93%` | `1.18` | 8,060,000.00 USD |
| `1H` | `KuCoin` | `49.78%` | `50.22%` | `0.99` | 700,300.00 USD |
| `1H` | `Gate` | `33.33%` | `66.67%` | `0.50` | 4,820,000.00 USD |
| `1H` | `Bitget` | `45.21%` | `54.79%` | `0.83` | 2,780,000.00 USD |
| `1H` | `BingX` | `27.28%` | `72.72%` | `0.38` | 344,200.00 USD |
| `1H` | `MEXC` | `47.7%` | `52.3%` | `0.91` | 615,980.00 USD |
| `1H` | `Bitunix` | `47.7%` | `52.3%` | `0.91` | 492,930.00 USD |
| `1H` | `Hyperliquid` | `67.18%` | `32.82%` | `2.05` | 688,110.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `41.95%` | `58.05%` | `0.72` | 553,200.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `37.23%` | `62.77%` | `0.59` | 142,680.00 USD |
| `1H` | `HTX` | `42.52%` | `57.48%` | `0.74` | 189,970.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `54.8%` | `45.2%` | `1.21` | 1,880.00 USD |
| `1H` | `Aster` | `39.13%` | `60.87%` | `0.64` | 45,340.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `47.51%` | `52.49%` | `0.91` | 304,280.00 USD |
| `1H` | `Whale Positions` | `48.82%` | `51.18%` | `0.95` | 16,900,000.00 USD |
| `1H` | `Global Accounts` | `47.91%` | `52.09%` | `0.92` | 41,230,000.00 USD |
| `4H` | `LTC` | `47.80%` | `52.20%` | `0.92` | 118,450,000.00 USD |
| `4H` | `Binance` | `49.63%` | `50.37%` | `0.99` | 45,590,000.00 USD |
| `4H` | `OKX` | `49.54%` | `50.46%` | `0.98` | 7,350,000.00 USD |
| `4H` | `Bybit` | `47.65%` | `52.35%` | `0.91` | 10,660,000.00 USD |
| `4H` | `KuCoin` | `44.89%` | `55.11%` | `0.81` | 1,790,000.00 USD |
| `4H` | `Gate` | `44.58%` | `55.42%` | `0.80` | 3,390,000.00 USD |
| `4H` | `Bitget` | `44.38%` | `55.62%` | `0.80` | 4,060,000.00 USD |
| `4H` | `BingX` | `43.24%` | `56.76%` | `0.76` | 14,710,000.00 USD |
| `4H` | `MEXC` | `46.35%` | `53.65%` | `0.86` | 3,960,000.00 USD |
| `4H` | `Bitunix` | `49.29%` | `50.71%` | `0.97` | 3,450,000.00 USD |
| `4H` | `Hyperliquid` | `46.32%` | `53.68%` | `0.86` | 3,200,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.04%` | `50.96%` | `0.96` | 18,210,000.00 USD |
| `4H` | `Crypto.com` | `29.23%` | `70.77%` | `0.41` | 22,460.00 USD |
| `4H` | `WhiteBIT` | `32.28%` | `67.72%` | `0.48` | 881,650.00 USD |
| `4H` | `HTX` | `56.11%` | `43.89%` | `1.28` | 64,410.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `48.52%` | `51.48%` | `0.94` | 506,070.00 USD |
| `4H` | `Aster` | `49.84%` | `50.16%` | `0.99` | 233,790.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `41.56%` | `58.44%` | `0.71` | 364,080.00 USD |
| `4H` | `Whale Positions` | `49.63%` | `50.37%` | `0.99` | 45,590,000.00 USD |
| `4H` | `Global Accounts` | `47.80%` | `52.20%` | `0.92` | 118,450,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `54.34` | `54.28` | `54.34` | `54.41` | `54.11` | 777,440.60 USD | 385,500.86 USD | 391,939.75 USD | -6,438.89 USD | `-0.83%` | `0B / 4S` |
| `0:00 UTC` | `54.52` | `54.26` | `54.52` | `54.55` | `53.91` | 698,950.15 USD | 352,602.70 USD | 346,347.45 USD | 6,255.26 USD | `+0.89%` | `7B / 7S` |
| `5:00 UTC` | `55.09` | `54.88` | `55.09` | `55.16` | `54.53` | 1,113,307.98 USD | 534,835.45 USD | 578,472.53 USD | -43,637.08 USD | `-3.92%` | `11B / 6S` |
| `0:00 UTC` | `55.17` | `55.17` | `55.17` | `55.34` | `55.00` | 1,657,433.83 USD | 827,264.59 USD | 830,169.24 USD | -2,904.65 USD | `-0.18%` | `3B / 4S` |
| `5:00 UTC` | `55.09` | `55.12` | `55.09` | `55.28` | `54.97` | 863,748.33 USD | 238,704.69 USD | 625,043.64 USD | -386,338.95 USD | `-44.73%` | `0B / 13S` |
| `0:00 UTC` | `55.41` | `55.33` | `55.41` | `55.44` | `55.11` | 1,037,180.75 USD | 435,075.60 USD | 602,105.15 USD | -167,029.55 USD | `-16.10%` | `6B / 3S` |
| `5:00 UTC` | `55.56` | `55.49` | `55.56` | `55.70` | `55.20` | 870,084.16 USD | 411,175.51 USD | 458,908.65 USD | -47,733.14 USD | `-5.49%` | `12B / 6S` |
| `0:00 UTC` | `55.98` | `55.89` | `55.98` | `56.08` | `55.64` | 1,411,324.18 USD | 622,108.47 USD | 789,215.71 USD | -167,107.24 USD | `-11.84%` | `7B / 3S` |
| `5:00 UTC` | `56.20` | `56.14` | `56.20` | `56.27` | `55.95` | 941,863.07 USD | 405,285.65 USD | 536,577.42 USD | -131,291.77 USD | `-13.94%` | `0B / 5S` |
| `0:00 UTC` | `56.28` | `56.26` | `56.28` | `56.28` | `56.20` | 49,411.26 USD | 20,001.00 USD | 29,410.26 USD | -9,409.27 USD | `-19.04%` | `1B / 3S` |

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
| `5m` | -74,820.00 USD | -168,040.00 USD | **`DISTRIBUTION`** |
| `15m` | -76,830.00 USD | -564,130.00 USD | **`DISTRIBUTION`** |
| `30m` | -154,650.00 USD | -498,420.00 USD | **`DISTRIBUTION`** |
| `1h` | 88,040.00 USD | -735,510.00 USD | **`DISTRIBUTION`** |
| `2h` | 315,300.00 USD | -1,160,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -812,300.00 USD | -2,940,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -141,130.00 USD | -3,210,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,030,000.00 USD | -6,080,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,190,000.00 USD | -6,630,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 913,640.00 USD | -4,430,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 3,340,000.00 USD | -25,330,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -23,320,000.00 USD | -195,090,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-74.82K` | 15m=`-76.83K` | 1h=`+88.04K` | 24h=`+913.64K`
* Futures Capital Netflows: 5m=`-168.04K` | 15m=`-564.13K` | 1h=`-735.51K` | 24h=`-4.43M`
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
  * `2026-10-30 09:09:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:28:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:29:56 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `54.16` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `53.10` (Risk Distance: `1.06` pts)
  * +2.5R Take Profit: `56.81`
  * Mathematical Lot Sizing: **`9.44 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `55.87` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `56.93` (Risk Distance: `1.06` pts)
  * +2.5R Take Profit: `53.22`
  * Mathematical Lot Sizing: **`9.44 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`56.31`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
