# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 07:45:23 IST` (`2026-10-30 02:15:23 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `54.23` | **Live Ask Quote**: `54.53` | **Mid Price**: `54.38`
- **Spread Points**: `300.00` | **Spread BPS**: `55.17 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `53.88` | VWAP Z-Score: `+0.50` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.5908` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `37.36` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `55.06` | Lower -3.00σ Band: `52.70`
  * Upper +2.51σ Band: `54.87` | Lower -2.51σ Band: `52.89`
  * Upper +2.01σ Band: `54.67` | Lower -2.01σ Band: `53.09`
  * Upper +2.00σ Band: `54.67` | Lower -2.00σ Band: `53.09`
  * Upper +1.28σ Band: `54.39` | Lower -1.28σ Band: `53.38`
  * Upper +1.00σ Band: `54.28` | Lower -1.00σ Band: `53.49`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`54.23` | EMA-20=`54.79` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`55.90` (Slope: `+0.0000`) | EMA-100=`56.64`
  * Institutional Anchors: EMA-144=`56.86` | EMA-200=`56.86` (Slope: `-0.5676`) | EMA-233=`56.89`
- **Range Boundaries**: 24H High=`58.72` | 24H Low=`52.64` | Weekly High=`59.62` | Weekly Low=`52.64`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `55.86` (Distance: `-2.64%`)
  * Point of Control (POC) = `55.27` (Distance: `-1.61%`)
  * Value Area Low (VAL) = `54.08` (Distance: `+0.56%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.40` | POC=`57.72` | VAL=`56.83`
  * Prior Day Extremes: PDH=`59.52` | PDL=`54.18` | PDC=`54.46`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`58.25` | Weekly POC=`56.43` | Weekly VAL=`55.97`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`55.89` | Low=`52.64`
  * London Session (08:00-16:00 UTC): High=`54.60` | Low=`54.16`
  * New York Session (13:00-21:00 UTC): High=`54.71` | Low=`54.05`
  * Initial Balance (First Hour): IB High=`54.54` | IB Low=`54.22`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `54.16` - `54.60`
  * Optimal Trade Entry (OTE 0.705): `54.49`
  * Structural Invalidation Anchor (0.786): `54.82`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `54.30` | `54.37` | `53.92` | `53.92` | `4,260` | 230,793.64 USD | -36,260.72 USD | `-15.71%` | -4,007,766.25 USD | `-0.32` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `53.92` | `54.31` | `53.91` | `54.27` | `4,032` | 218,101.99 USD | 41,252.37 USD | `+18.91%` | -3,966,513.88 USD | `+0.44` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `54.28` | `54.53` | `54.28` | `54.46` | `2,878` | 156,691.69 USD | 1,143.96 USD | `+0.73%` | -3,965,369.92 USD | `+0.06` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `54.14` | `54.54` | `53.64` | `54.39` | `32,927` | 1,780,531.79 USD | 231,283.53 USD | `+12.99%` | -3,965,066.64 USD | `+0.66` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `54.39` | `54.41` | `54.11` | `54.29` | `14,325` | 777,440.60 USD | -6,438.89 USD | `-0.83%` | -3,971,505.53 USD | `+0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `54.30` | `54.53` | `53.91` | `54.46` | `11,165` | 605,316.00 USD | 5,864.29 USD | `+0.97%` | -3,965,641.24 USD | `+0.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `54.92` | `55.02` | `52.77` | `54.37` | `295,042` | 15,877,230.39 USD | -1,113,823.94 USD | `-7.02%` | -3,765,391.81 USD | `-1.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `54.36` | `54.62` | `53.64` | `54.29` | `95,012` | 5,151,310.38 USD | -124,905.13 USD | `-2.42%` | -3,890,296.94 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `54.30` | `54.53` | `53.91` | `54.46` | `11,165` | 605,316.00 USD | 5,864.29 USD | `+0.97%` | -3,884,432.65 USD | `+0.21` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | 340,473.45 USD | `+0.15` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,923,567.46 USD | `-1.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `55.02` | `52.77` | `54.46` | `401,219` | 21,633,856.77 USD | -1,232,864.79 USD | `-5.70%` | -4,156,432.24 USD | `-0.42` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `57.04` | `58.16` | `56.85` | `58.00` | `178,996` | 10,300,529.12 USD | 452,809.17 USD | `+4.40%` | -47,398.66 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | 201,186.90 USD | `+0.44` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | 340,473.45 USD | `+0.15` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,923,567.46 USD | `-1.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `55.02` | `52.77` | `54.46` | `401,219` | 21,633,856.77 USD | -1,232,864.79 USD | `-5.70%` | -4,156,432.24 USD | `-0.42` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`54.38`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:43:27 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1080` | `0xeadc...9d55` | `LONG` | 1,979,581.61 USD | `36,463.77` | `52.78` | `54.32` | `0.000000` | 54,905.66 USD | `+2.77%` | `10X Cross` |
| `1090` | `0x9aa5...58af` | `SHORT` | 1,963,180.18 USD | `36,177.65` | `71.22` | `54.32` | `318.16` | 613,306.49 USD | `+31.24%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `58.96` | 5,271.85 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.27K USD at 58.9560 USD [API] | `2026-10-28 20:23:16` |
| `ANNOUNCEMENT` | `INFO` | `59.36` | 7,245.48 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.25K USD at 59.3600 USD [API] | `2026-10-28 21:23:31` |
| `ANNOUNCEMENT` | `INFO` | `59.35` | 7,506.71 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 59.3510 USD [API] | `2026-10-28 21:23:31` |
| `ANNOUNCEMENT` | `INFO` | `59.23` | 5,285.54 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.29K USD at 59.2350 USD [API] | `2026-10-28 22:05:44` |
| `ANNOUNCEMENT` | `INFO` | `59.50` | 5,882.07 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 5.88K USD at 59.4990 USD [API] | `2026-10-28 22:34:27` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.56%`) | Long MP=`54.26` (Vol: 204,200.00 USD, Dist: `--2.00%`)
  * 48H Horizon: Short MP=`58.99` (Vol: 284,700.00 USD, Dist: `+6.53%`) | Long MP=`54.29` (Vol: 204,200.00 USD, Dist: `--1.95%`)
  * 3D Horizon: Short MP=`58.99` (Vol: 284,700.00 USD, Dist: `+6.53%`) | Long MP=`54.29` (Vol: 204,200.00 USD, Dist: `--1.95%`)
  * 7D Horizon: Short MP=`58.99` (Vol: 284,700.00 USD, Dist: `+6.53%`) | Long MP=`54.29` (Vol: 204,200.00 USD, Dist: `--1.95%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `11.35` | 136.20 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.25` | 122.50 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.65` | 404.80 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.75` | 2,560.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.15` | 2,220.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.65` | 150.15 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `16.05` | 187.14 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `16.35` | 425.92 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.05` | 361.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.25` | 114.97 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.75` | 2,520.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.05` | 3,470.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.45` | 2,010.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.35` | 357.40 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.05` | 185.55 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.25` | 375.02 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.55` | 21,900.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.65` | 4,610.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.75` | 3,580.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.85` | 195.57 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.65` | 491.77 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 279,500.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 173.39 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.45` | 7,500.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 167,420.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 374.20 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.75` | 176.55 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.05` | 5,510.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.25` | 245.79 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 272.75 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.65` | 1,080.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 173.85 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 583.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 297,680.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 781.90 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 538.53 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 5,880.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.25` | 494.38 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.35` | 21,880.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 5,680.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 2,870.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 835.81 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.05` | 9,620.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 450.10 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.35` | 172.10 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 653.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 953.68 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 32,850.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.25` | 4,120.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 257.76 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 182.85 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 126.70 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.35` | 1,370.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.45` | 65,890.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.55` | 172.75 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 3,240.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 1,070.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 166.49 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 3,020.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 5,180.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.55` | 255.85 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 101.80 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.85` | 64,720.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 359.76 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 438.74 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 9,260.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 3,530.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.65` | 1,060.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 377.50 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 6,210.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 446.67 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.25` | 1,080.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 341.70 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 2,400.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 993.82 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 4,280.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.75` | 461.90 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 2,730.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 664,760.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 570.02 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 264.83 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 865.53 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 1,190.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 6,230.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 1,180.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 133.10 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 2,160.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.35` | 5,320.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 1,010.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 133.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 274.39 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.75` | 319.07 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 6,340.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 509.01 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 396.54 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 14,490.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 644.96 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 982.29 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 69,270.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 35,410.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.35` | 9,320.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 1,570.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 5,800.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 2,000.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 9,080.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 122,400.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 417.80 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 5,390.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 980.67 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 26,650.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 21,880.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 801.14 USD | 990,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 2,380.00 USD | 989,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 84,440.00 USD | 987,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 7,250.00 USD | 902,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 4,230.00 USD | 895,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 668.27 USD | 891,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 3,960.00 USD | 890,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 4,830.00 USD | 886,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 9,040.00 USD | 881,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 7,050.00 USD | 872,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 2,180.00 USD | 865,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 23,940.00 USD | 863,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 12,060.00 USD | 839,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 706.41 USD | 827,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.15` | 5,940.00 USD | 826,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.25` | 842.21 USD | 820,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.35` | 9,610.00 USD | 819,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 24,670.00 USD | 810,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 3,980.00 USD | 785,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 358.40 USD | 781,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 158.22 USD | 781,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 49,130.00 USD | 781,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 1,220.00 USD | 732,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.35` | 43,340.00 USD | 730,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.45` | 5,100.00 USD | 687,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 1,770.00 USD | 682,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 47,750.00 USD | 680,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.85` | 358.88 USD | 632,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 1,340.00 USD | 632,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 7,200.00 USD | 631,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 525.44 USD | 623,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 2,560.00 USD | 623,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 273.90 USD | 620,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 8,360.00 USD | 620,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 252.58 USD | 612,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,580.00 USD | 612,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,740.00 USD | 610,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.25` | 18,950.00 USD | 604,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.30` | 2,870,000.00 USD | 2,870,000.00 USD | 13,300.00 USD | 4,090.00 USD | 367.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.30` | 8,100,000.00 USD | 8,100,000.00 USD | 15,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.35` | 30,090.00 USD | 585,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.40` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 626.48 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.40` | 8,080,000.00 USD | 8,080,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.45` | 419.34 USD | 555,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.50` | 2,850,000.00 USD | 2,850,000.00 USD | 1,180.00 USD | 4,200.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.50` | 8,070,000.00 USD | 8,070,000.00 USD | 1,130.00 USD | 6,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.55` | 18,010.00 USD | 555,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.60` | 2,830,000.00 USD | 2,830,000.00 USD | 980.75 USD | 4,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.60` | 8,070,000.00 USD | 8,070,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.65` | 73,260.00 USD | 537,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.70` | 2,820,000.00 USD | 2,820,000.00 USD | 3,550.00 USD | 1,980.00 USD | 416.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.70` | 8,050,000.00 USD | 8,050,000.00 USD | 788.92 USD | 0.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.75` | 1,580.00 USD | 463,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.80` | 2,820,000.00 USD | 2,820,000.00 USD | 2,920.00 USD | 388.95 USD | 14,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.80` | 8,040,000.00 USD | 8,040,000.00 USD | 8,590.00 USD | 8,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `49.90` | 2,800,000.00 USD | 2,800,000.00 USD | 17,280.00 USD | 8,370.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.90` | 8,030,000.00 USD | 8,030,000.00 USD | 45,030.00 USD | 7,170.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.95` | 19,920.00 USD | 462,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.00` | 2,750,000.00 USD | 2,750,000.00 USD | 7,520.00 USD | 6,290.00 USD | 40,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.00` | 7,970,000.00 USD | 7,970,000.00 USD | 22,100.00 USD | 7,630.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.05` | 3,760.00 USD | 442,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.10` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.10` | 7,920,000.00 USD | 7,920,000.00 USD | 363.50 USD | 682.90 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.20` | 7,920,000.00 USD | 7,920,000.00 USD | 6,960.00 USD | 500.40 USD | 34,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.25` | 102.51 USD | 438,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.30` | 7,870,000.00 USD | 7,870,000.00 USD | 16,270.00 USD | 3,640.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.35` | 1,140.00 USD | 438,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.40` | 2,690,000.00 USD | 2,690,000.00 USD | 349.63 USD | 2,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.40` | 7,850,000.00 USD | 7,850,000.00 USD | 23,520.00 USD | 19,110.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,720.00 USD | 437,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.50` | 7,780,000.00 USD | 7,780,000.00 USD | 24,840.00 USD | 6,790.00 USD | 43,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.55` | 84,100.00 USD | 432,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.60` | 7,700,000.00 USD | 7,700,000.00 USD | 52,670.00 USD | 17,830.00 USD | 22,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.65` | 730.88 USD | 348,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.70` | 7,610,000.00 USD | 7,610,000.00 USD | 53,670.00 USD | 24,710.00 USD | 32,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.75` | 9,050.00 USD | 347,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.80` | 2,690,000.00 USD | 2,690,000.00 USD | 5,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.80` | 7,500,000.00 USD | 7,500,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.90` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 497.60 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.90` | 7,400,000.00 USD | 7,400,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.95` | 431.55 USD | 338,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.00` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 129.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.00` | 7,150,000.00 USD | 7,150,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.10` | 2,680,000.00 USD | 2,680,000.00 USD | 263.90 USD | 1,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.10` | 7,020,000.00 USD | 7,020,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.15` | 219,370.00 USD | 338,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.20` | 2,680,000.00 USD | 2,680,000.00 USD | 1,100.00 USD | 1,130.00 USD | 327.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.20` | 6,940,000.00 USD | 6,940,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.25` | 202.44 USD | 119,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.30` | 2,670,000.00 USD | 2,670,000.00 USD | 20,430.00 USD | 5,180.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.30` | 6,870,000.00 USD | 6,870,000.00 USD | 19,510.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.35` | 453.93 USD | 118,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.40` | 2,630,000.00 USD | 2,630,000.00 USD | 17,800.00 USD | 7,000.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.40` | 6,800,000.00 USD | 6,800,000.00 USD | 73,130.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.45` | 20,890.00 USD | 118,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.50` | 2,590,000.00 USD | 2,590,000.00 USD | 11,810.00 USD | 9,610.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.50` | 6,650,000.00 USD | 6,650,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.55` | 551.07 USD | 97,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.60` | 2,570,000.00 USD | 2,570,000.00 USD | 9,850.00 USD | 8,110.00 USD | 4,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.60` | 6,560,000.00 USD | 6,560,000.00 USD | 35,880.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.65` | 8,810.00 USD | 96,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.70` | 2,550,000.00 USD | 2,550,000.00 USD | 5,340.00 USD | 3,950.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.70` | 6,490,000.00 USD | 6,490,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.75` | 6,480.00 USD | 88,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.80` | 2,530,000.00 USD | 2,530,000.00 USD | 13,220.00 USD | 2,980.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.80` | 6,450,000.00 USD | 6,450,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.85` | 13,890.00 USD | 81,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.90` | 2,500,000.00 USD | 2,500,000.00 USD | 12,520.00 USD | 19,700.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.90` | 6,400,000.00 USD | 6,400,000.00 USD | 5,870.00 USD | 15,810.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.95` | 13,950.00 USD | 67,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.00` | 2,460,000.00 USD | 2,460,000.00 USD | 25,510.00 USD | 8,240.00 USD | 23,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.00` | 6,370,000.00 USD | 6,370,000.00 USD | 64,300.00 USD | 20,800.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.10` | 2,400,000.00 USD | 2,400,000.00 USD | 27,630.00 USD | 6,280.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 6,270,000.00 USD | 6,270,000.00 USD | 24,220.00 USD | 18,810.00 USD | 35,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.15` | 1,900.00 USD | 53,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.20` | 2,340,000.00 USD | 2,340,000.00 USD | 20,520.00 USD | 11,250.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 6,190,000.00 USD | 6,190,000.00 USD | 38,380.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.25` | 2,990.00 USD | 51,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.30` | 2,290,000.00 USD | 2,290,000.00 USD | 39,260.00 USD | 7,260.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 6,130,000.00 USD | 6,130,000.00 USD | 21,450.00 USD | 12,840.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.35` | 1,860.00 USD | 48,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.40` | 2,230,000.00 USD | 2,230,000.00 USD | 11,920.00 USD | 7,830.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 6,080,000.00 USD | 6,080,000.00 USD | 20,580.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.45` | 2,360.00 USD | 47,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `55.85` | 1,150.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `55.90` | 344,790.00 USD | 344,790.00 USD | 137,200.00 USD | 2,990.00 USD | 140,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.90` | 930,900.00 USD | 930,900.00 USD | 141,330.00 USD | 65,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `55.95` | 770.99 USD | 1,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `56.00` | 544,060.00 USD | 544,060.00 USD | 139,840.00 USD | 0.00 USD | 59,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.00` | 1,360,000.00 USD | 1,360,000.00 USD | 181,230.00 USD | 98,600.00 USD | 147,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `56.05` | 1,570.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `56.75` | 2,100.00 USD | 5,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `56.80` | 3,080,000.00 USD | 3,080,000.00 USD | 191,190.00 USD | 18,260.00 USD | 115,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.80` | 4,570,000.00 USD | 4,570,000.00 USD | 153,580.00 USD | 92,780.00 USD | 261,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `56.85` | 3,770.00 USD | 9,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `56.90` | 3,120,000.00 USD | 3,120,000.00 USD | 33,240.00 USD | 8,700.00 USD | 1,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.90` | 4,990,000.00 USD | 4,990,000.00 USD | 108,440.00 USD | 48,600.00 USD | 266,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.00` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 10,920.00 USD | 659.87 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.00` | 5,170,000.00 USD | 5,170,000.00 USD | 88,680.00 USD | 2,620.00 USD | 93,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.10` | 3,160,000.00 USD | 3,160,000.00 USD | 7,480.00 USD | 10,560.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.10` | 5,250,000.00 USD | 5,250,000.00 USD | 36,580.00 USD | 16,110.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.15` | 146.88 USD | 9,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `57.95` | 125.75 USD | 9,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.00` | 4,000,000.00 USD | 4,000,000.00 USD | 4,040.00 USD | 5,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.00` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 3,670.00 USD | 86,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `58.05` | 200,340.00 USD | 209,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `59.35` | 9,440.00 USD | 219,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `60.95` | 397.39 USD | 219,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.00` | 9,120,000.00 USD | 9,120,000.00 USD | 46,000.00 USD | 7,600.00 USD | 28,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 14,000,000.00 USD | 14,000,000.00 USD | 96,160.00 USD | 36,500.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.10` | 9,160,000.00 USD | 9,160,000.00 USD | 13,630.00 USD | 5,800.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 14,040,000.00 USD | 14,040,000.00 USD | 31,540.00 USD | 1,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.15` | 3,870.00 USD | 223,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `62.95` | 138.49 USD | 223,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `63.00` | 16,670,000.00 USD | 16,670,000.00 USD | 34,730.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.10` | 16,700,000.00 USD | 16,700,000.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.30` | 16,740,000.00 USD | 16,740,000.00 USD | 17,050.00 USD | 11,500.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.40` | 16,770,000.00 USD | 16,770,000.00 USD | 13,220.00 USD | 1,320.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `63.45` | 3,350.00 USD | 227,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `66.45` | 44,010.00 USD | 271,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.65` | 5,400.00 USD | 276,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.95` | 121.18 USD | 276,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.85` | 709.03 USD | 277,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `73.35` | 253.06 USD | 277,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `76.35` | 8,380.00 USD | 286,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.85` | 602.56 USD | 286,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.95` | 136.41 USD | 286,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `79.75` | 3,190.00 USD | 289,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.75` | 646.00 USD | 290,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.85` | 21,570.00 USD | 312,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.05` | 19,000.00 USD | 331,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.55` | 123.96 USD | 331,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.75` | 214.32 USD | 331,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.95` | 2,740.00 USD | 334,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `83.65` | 3,900.00 USD | 338,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `86.75` | 922.15 USD | 339,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.65` | 130.22 USD | 339,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.15` | 2,500.00 USD | 341,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `102.75` | 931.94 USD | 342,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.25` | 213.71 USD | 342,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.15` | 354,780.00 USD | 697,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.35` | 726.37 USD | 698,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.75` | 1,620.00 USD | 699,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.85` | 1,860.00 USD | 701,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.15` | 199.30 USD | 702,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.05` | 6,470.00 USD | 708,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `11.05` | 3,110,000.00 USD | 0.00 USD | 20,670.00 USD | `-79.64%` | `1,870.59` |
| `Live` | `Long` | `11.35` | 3,080,000.00 USD | 0.00 USD | 136.20 USD | `-79.09%` | `12.00` |
| `Live` | `Long` | `11.95` | 3,080,000.00 USD | 0.00 USD | 268.88 USD | `-77.99%` | `22.50` |
| `Live` | `Long` | `12.25` | 3,080,000.00 USD | 0.00 USD | 122.50 USD | `-77.43%` | `10.00` |
| `Live` | `Long` | `12.75` | 3,080,000.00 USD | 0.00 USD | 2,560.00 USD | `-76.51%` | `200.43` |
| `Live` | `Long` | `13.15` | 3,080,000.00 USD | 0.00 USD | 2,220.00 USD | `-75.78%` | `168.79` |
| `Live` | `Long` | `13.65` | 3,080,000.00 USD | 0.00 USD | 150.15 USD | `-74.85%` | `11.00` |
| `Live` | `Long` | `16.65` | 3,080,000.00 USD | 0.00 USD | 433.73 USD | `-69.33%` | `26.05` |
| `Live` | `Long` | `18.25` | 3,080,000.00 USD | 0.00 USD | 13,760.00 USD | `-66.38%` | `754.07` |
| `Live` | `Long` | `18.45` | 3,060,000.00 USD | 0.00 USD | 215.13 USD | `-66.01%` | `11.66` |
| `Live` | `Long` | `18.65` | 3,060,000.00 USD | 0.00 USD | 373.00 USD | `-65.64%` | `20.00` |
| `Live` | `Long` | `19.05` | 3,060,000.00 USD | 0.00 USD | 3,470.00 USD | `-64.91%` | `182.00` |
| `Live` | `Long` | `19.15` | 3,060,000.00 USD | 0.00 USD | 2,300.00 USD | `-64.72%` | `120.00` |
| `Live` | `Long` | `19.45` | 3,060,000.00 USD | 0.00 USD | 2,010.00 USD | `-64.17%` | `103.47` |
| `Live` | `Long` | `21.55` | 3,060,000.00 USD | 0.00 USD | 21,570.00 USD | `-60.30%` | `1,000.85` |
| `Live` | `Long` | `21.65` | 3,030,000.00 USD | 0.00 USD | 20,130.00 USD | `-60.12%` | `930.00` |
| `Live` | `Long` | `23.25` | 3,010,000.00 USD | 0.00 USD | 3,500.00 USD | `-57.17%` | `150.57` |
| `Live` | `Long` | `23.35` | 3,010,000.00 USD | 0.00 USD | 376.64 USD | `-56.98%` | `16.13` |
| `Live` | `Long` | `23.85` | 3,010,000.00 USD | 0.00 USD | 195.57 USD | `-56.06%` | `8.20` |
| `Live` | `Long` | `23.95` | 3,010,000.00 USD | 0.00 USD | 4,670.00 USD | `-55.88%` | `195.03` |
| `Live` | `Long` | `24.15` | 3,010,000.00 USD | 0.00 USD | 404.27 USD | `-55.51%` | `16.74` |
| `Live` | `Long` | `24.45` | 3,010,000.00 USD | 0.00 USD | 196.82 USD | `-54.96%` | `8.05` |
| `Live` | `Long` | `24.65` | 3,010,000.00 USD | 0.00 USD | 491.77 USD | `-54.59%` | `19.95` |
| `Live` | `Long` | `25.25` | 3,000,000.00 USD | 0.00 USD | 277,980.00 USD | `-53.48%` | `11,009.19` |
| `Live` | `Long` | `25.35` | 2,730,000.00 USD | 0.00 USD | 173.39 USD | `-53.30%` | `6.84` |
| `Live` | `Long` | `25.55` | 2,730,000.00 USD | 0.00 USD | 50,740.00 USD | `-52.93%` | `1,985.99` |
| `Live` | `Long` | `25.75` | 2,680,000.00 USD | 0.00 USD | 1,950.00 USD | `-52.56%` | `75.82` |
| `Live` | `Long` | `25.95` | 2,670,000.00 USD | 0.00 USD | 374.20 USD | `-52.19%` | `14.42` |
| `Live` | `Long` | `27.05` | 2,670,000.00 USD | 0.00 USD | 5,690.00 USD | `-50.17%` | `210.45` |
| `Live` | `Long` | `27.55` | 2,670,000.00 USD | 0.00 USD | 272.75 USD | `-49.25%` | `9.90` |
| `Live` | `Long` | `27.65` | 2,670,000.00 USD | 0.00 USD | 126,270.00 USD | `-49.06%` | `4,566.66` |
| `Live` | `Long` | `27.95` | 2,540,000.00 USD | 0.00 USD | 173.85 USD | `-48.51%` | `6.22` |
| `Live` | `Long` | `28.05` | 2,540,000.00 USD | 0.00 USD | 8,270.00 USD | `-48.33%` | `294.67` |
| `Live` | `Long` | `29.15` | 2,530,000.00 USD | 0.00 USD | 583.00 USD | `-46.30%` | `20.00` |
| `Live` | `Long` | `29.35` | 2,530,000.00 USD | 0.00 USD | 1,690.00 USD | `-45.93%` | `57.67` |
| `Live` | `Long` | `29.55` | 2,530,000.00 USD | 0.00 USD | 425.52 USD | `-45.56%` | `14.40` |
| `Live` | `Long` | `29.75` | 2,530,000.00 USD | 0.00 USD | 297,680.00 USD | `-45.19%` | `10,005.91` |
| `Live` | `Long` | `30.05` | 2,230,000.00 USD | 0.00 USD | 218.46 USD | `-44.64%` | `7.27` |
| `Live` | `Long` | `30.95` | 2,230,000.00 USD | 0.00 USD | 9,820.00 USD | `-42.98%` | `317.40` |
| `Live` | `Long` | `31.15` | 2,220,000.00 USD | 0.00 USD | 5,880.00 USD | `-42.62%` | `188.85` |
| `Live` | `Long` | `31.55` | 2,220,000.00 USD | 0.00 USD | 1,060.00 USD | `-41.88%` | `33.49` |
| `Live` | `Long` | `31.65` | 2,220,000.00 USD | 0.00 USD | 26,730.00 USD | `-41.69%` | `844.48` |
| `Live` | `Long` | `31.85` | 2,190,000.00 USD | 0.00 USD | 2,870.00 USD | `-41.33%` | `90.00` |
| `Live` | `Long` | `31.95` | 2,190,000.00 USD | 0.00 USD | 125.24 USD | `-41.14%` | `3.92` |
| `Live` | `Long` | `32.15` | 2,190,000.00 USD | 0.00 USD | 740.09 USD | `-40.77%` | `23.02` |
| `Live` | `Long` | `32.35` | 2,190,000.00 USD | 0.00 USD | 172.10 USD | `-40.40%` | `5.32` |
| `Live` | `Long` | `32.65` | 2,180,000.00 USD | 0.00 USD | 653.00 USD | `-39.85%` | `20.00` |
| `Live` | `Long` | `32.75` | 2,180,000.00 USD | 0.00 USD | 953.68 USD | `-39.67%` | `29.12` |
| `Live` | `Long` | `32.85` | 2,180,000.00 USD | 0.00 USD | 32,850.00 USD | `-39.48%` | `1,000.01` |
| `Live` | `Long` | `33.55` | 2,150,000.00 USD | 0.00 USD | 1,680.00 USD | `-38.19%` | `50.00` |
| `Live` | `Long` | `33.65` | 2,150,000.00 USD | 0.00 USD | 3,130.00 USD | `-38.01%` | `93.09` |
| `Live` | `Long` | `34.05` | 2,150,000.00 USD | 0.00 USD | 182.85 USD | `-37.27%` | `5.37` |
| `Live` | `Long` | `34.15` | 2,150,000.00 USD | 0.00 USD | 126.70 USD | `-37.09%` | `3.71` |
| `Live` | `Long` | `34.25` | 2,150,000.00 USD | 0.00 USD | 4,250.00 USD | `-36.90%` | `124.01` |
| `Live` | `Long` | `34.45` | 2,140,000.00 USD | 0.00 USD | 65,890.00 USD | `-36.54%` | `1,912.61` |
| `Live` | `Long` | `34.55` | 2,080,000.00 USD | 0.00 USD | 103.65 USD | `-36.35%` | `3.00` |
| `Live` | `Long` | `34.65` | 2,080,000.00 USD | 0.00 USD | 3,240.00 USD | `-36.17%` | `93.56` |
| `Live` | `Long` | `34.95` | 2,070,000.00 USD | 0.00 USD | 104.85 USD | `-35.62%` | `3.00` |
| `Live` | `Long` | `35.05` | 2,070,000.00 USD | 0.00 USD | 341.74 USD | `-35.43%` | `9.75` |
| `Live` | `Long` | `35.45` | 2,070,000.00 USD | 0.00 USD | 982.32 USD | `-34.69%` | `27.71` |
| `Live` | `Long` | `35.75` | 2,070,000.00 USD | 0.00 USD | 795.08 USD | `-34.14%` | `22.24` |
| `Live` | `Long` | `36.35` | 2,070,000.00 USD | 0.00 USD | 3,020.00 USD | `-33.04%` | `83.03` |
| `Live` | `Long` | `36.45` | 2,070,000.00 USD | 0.00 USD | 423.18 USD | `-32.85%` | `11.61` |
| `Live` | `Long` | `36.65` | 2,070,000.00 USD | 0.00 USD | 4,790.00 USD | `-32.48%` | `130.63` |
| `Live` | `Long` | `36.75` | 2,060,000.00 USD | 0.00 USD | 101.80 USD | `-32.30%` | `2.77` |
| `Live` | `Long` | `37.15` | 2,060,000.00 USD | 0.00 USD | 438.74 USD | `-31.56%` | `11.81` |
| `Live` | `Long` | `37.35` | 2,060,000.00 USD | 0.00 USD | 9,260.00 USD | `-31.19%` | `247.91` |
| `Live` | `Long` | `37.55` | 2,050,000.00 USD | 0.00 USD | 3,530.00 USD | `-30.83%` | `94.04` |
| `Live` | `Long` | `37.65` | 2,050,000.00 USD | 0.00 USD | 1,060.00 USD | `-30.64%` | `28.27` |
| `Live` | `Long` | `37.75` | 2,050,000.00 USD | 0.00 USD | 377.50 USD | `-30.46%` | `10.00` |
| `Live` | `Long` | `37.85` | 2,050,000.00 USD | 0.00 USD | 6,210.00 USD | `-30.27%` | `164.03` |
| `Live` | `Long` | `37.95` | 2,040,000.00 USD | 0.00 USD | 446.67 USD | `-30.09%` | `11.77` |
| `Live` | `Long` | `38.25` | 2,040,000.00 USD | 0.00 USD | 695.38 USD | `-29.54%` | `18.18` |
| `Live` | `Long` | `38.35` | 2,040,000.00 USD | 0.00 USD | 847.54 USD | `-29.35%` | `22.10` |
| `Live` | `Long` | `38.45` | 2,040,000.00 USD | 0.00 USD | 2,400.00 USD | `-29.17%` | `62.34` |
| `Live` | `Long` | `38.55` | 2,040,000.00 USD | 0.00 USD | 2,080.00 USD | `-28.98%` | `54.05` |
| `Live` | `Long` | `38.65` | 2,030,000.00 USD | 0.00 USD | 4,280.00 USD | `-28.80%` | `110.74` |
| `Live` | `Long` | `38.95` | 2,030,000.00 USD | 0.00 USD | 2,730.00 USD | `-28.25%` | `70.00` |
| `Live` | `Long` | `39.05` | 2,030,000.00 USD | 0.00 USD | 664,760.00 USD | `-28.06%` | `17,023.28` |
| `Live` | `Long` | `39.15` | 1,360,000.00 USD | 0.00 USD | 570.02 USD | `-27.88%` | `14.56` |
| `Live` | `Long` | `39.35` | 1,360,000.00 USD | 0.00 USD | 264.83 USD | `-27.51%` | `6.73` |
| `Live` | `Long` | `39.45` | 1,360,000.00 USD | 0.00 USD | 716.41 USD | `-27.33%` | `18.16` |
| `Live` | `Long` | `39.55` | 1,360,000.00 USD | 0.00 USD | 312.44 USD | `-27.14%` | `7.90` |
| `Live` | `Long` | `39.65` | 1,360,000.00 USD | 0.00 USD | 6,180.00 USD | `-26.96%` | `155.78` |
| `Live` | `Long` | `39.75` | 1,350,000.00 USD | 0.00 USD | 1,180.00 USD | `-26.77%` | `29.57` |
| `Live` | `Long` | `39.85` | 1,350,000.00 USD | 0.00 USD | 608.11 USD | `-26.59%` | `15.26` |
| `Live` | `Long` | `40.05` | 1,350,000.00 USD | 0.00 USD | 2,160.00 USD | `-26.22%` | `53.97` |
| `Live` | `Long` | `40.25` | 1,350,000.00 USD | 0.00 USD | 1,050.00 USD | `-25.85%` | `26.00` |
| `Live` | `Long` | `40.45` | 1,350,000.00 USD | 0.00 USD | 1,010.00 USD | `-25.48%` | `24.92` |
| `Live` | `Long` | `40.55` | 1,350,000.00 USD | 0.00 USD | 133.00 USD | `-25.30%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,350,000.00 USD | 0.00 USD | 274.39 USD | `-25.11%` | `6.75` |
| `Live` | `Long` | `40.85` | 1,350,000.00 USD | 0.00 USD | 13,460.00 USD | `-24.75%` | `329.45` |
| `Live` | `Long` | `40.95` | 1,330,000.00 USD | 0.00 USD | 509.01 USD | `-24.56%` | `12.43` |
| `Live` | `Long` | `41.05` | 1,330,000.00 USD | 0.00 USD | 396.54 USD | `-24.38%` | `9.66` |
| `Live` | `Long` | `41.15` | 1,330,000.00 USD | 0.00 USD | 322.20 USD | `-24.19%` | `7.83` |
| `Live` | `Long` | `41.25` | 1,330,000.00 USD | 0.00 USD | 55,740.00 USD | `-24.01%` | `1,351.26` |
| `Live` | `Long` | `41.35` | 1,280,000.00 USD | 0.00 USD | 349.41 USD | `-23.83%` | `8.45` |
| `Live` | `Long` | `41.45` | 1,280,000.00 USD | 0.00 USD | 644.96 USD | `-23.64%` | `15.56` |
| `Live` | `Long` | `41.65` | 1,280,000.00 USD | 0.00 USD | 5,500.00 USD | `-23.27%` | `131.94` |
| `Live` | `Long` | `42.05` | 1,270,000.00 USD | 0.00 USD | 982.29 USD | `-22.54%` | `23.36` |
| `Live` | `Long` | `42.15` | 1,270,000.00 USD | 0.00 USD | 69,270.00 USD | `-22.35%` | `1,643.33` |
| `Live` | `Long` | `42.25` | 1,200,000.00 USD | 0.00 USD | 35,410.00 USD | `-22.17%` | `838.00` |
| `Live` | `Long` | `42.65` | 1,170,000.00 USD | 0.00 USD | 1,570.00 USD | `-21.43%` | `36.70` |
| `Live` | `Long` | `42.85` | 1,160,000.00 USD | 0.00 USD | 5,800.00 USD | `-21.06%` | `135.38` |
| `Live` | `Long` | `42.95` | 1,160,000.00 USD | 0.00 USD | 11,450.00 USD | `-20.88%` | `266.65` |
| `Live` | `Long` | `43.05` | 1,150,000.00 USD | 0.00 USD | 9,080.00 USD | `-20.69%` | `211.00` |
| `Live` | `Long` | `43.15` | 1,140,000.00 USD | 0.00 USD | 122,400.00 USD | `-20.51%` | `2,836.59` |
| `Live` | `Long` | `43.25` | 1,010,000.00 USD | 0.00 USD | 417.80 USD | `-20.32%` | `9.66` |
| `Live` | `Long` | `43.35` | 1,010,000.00 USD | 0.00 USD | 5,390.00 USD | `-20.14%` | `124.24` |
| `Live` | `Long` | `43.45` | 1,010,000.00 USD | 0.00 USD | 980.67 USD | `-19.96%` | `22.57` |
| `Live` | `Long` | `43.65` | 1,010,000.00 USD | 0.00 USD | 26,650.00 USD | `-19.59%` | `610.44` |
| `Live` | `Long` | `43.75` | 981,440.00 USD | 0.00 USD | 21,880.00 USD | `-19.40%` | `500.00` |
| `Live` | `Long` | `43.85` | 959,570.00 USD | 0.00 USD | 801.14 USD | `-19.22%` | `18.27` |
| `Live` | `Long` | `44.15` | 958,760.00 USD | 0.00 USD | 2,380.00 USD | `-18.67%` | `53.99` |
| `Live` | `Long` | `44.35` | 956,380.00 USD | 0.00 USD | 84,440.00 USD | `-18.30%` | `1,903.87` |
| `Live` | `Long` | `44.55` | 871,940.00 USD | 0.00 USD | 842.44 USD | `-17.93%` | `18.91` |
| `Live` | `Long` | `44.65` | 871,100.00 USD | 0.00 USD | 4,050.00 USD | `-17.75%` | `90.60` |
| `Live` | `Long` | `44.75` | 867,060.00 USD | 0.00 USD | 7,200.00 USD | `-17.56%` | `160.80` |
| `Live` | `Long` | `44.85` | 859,860.00 USD | 0.00 USD | 134.55 USD | `-17.38%` | `3.00` |
| `Live` | `Long` | `44.95` | 859,730.00 USD | 0.00 USD | 3,150.00 USD | `-17.19%` | `70.08` |
| `Live` | `Long` | `45.05` | 856,580.00 USD | 0.00 USD | 4,830.00 USD | `-17.01%` | `107.31` |
| `Live` | `Long` | `45.15` | 851,740.00 USD | 0.00 USD | 10,070.00 USD | `-16.82%` | `223.00` |
| `Live` | `Long` | `45.25` | 841,670.00 USD | 0.00 USD | 3,180.00 USD | `-16.64%` | `70.37` |
| `Live` | `Long` | `45.35` | 838,490.00 USD | 0.00 USD | 4,740.00 USD | `-16.46%` | `104.53` |
| `Live` | `Long` | `45.45` | 833,750.00 USD | 0.00 USD | 23,940.00 USD | `-16.27%` | `526.65` |
| `Live` | `Long` | `45.55` | 809,810.00 USD | 0.00 USD | 12,060.00 USD | `-16.09%` | `264.81` |
| `Live` | `Long` | `45.65` | 797,750.00 USD | 0.00 USD | 42,180.00 USD | `-15.90%` | `924.03` |
| `Live` | `Long` | `45.95` | 755,570.00 USD | 0.00 USD | 183.80 USD | `-15.35%` | `4.00` |
| `Live` | `Long` | `46.05` | 755,380.00 USD | 0.00 USD | 706.41 USD | `-15.17%` | `15.34` |
| `Live` | `Long` | `46.25` | 754,680.00 USD | 0.00 USD | 842.21 USD | `-14.80%` | `18.21` |
| `Live` | `Long` | `46.35` | 753,840.00 USD | 0.00 USD | 383.78 USD | `-14.61%` | `8.28` |
| `Live` | `Long` | `46.55` | 753,450.00 USD | 0.00 USD | 2,140.00 USD | `-14.25%` | `45.93` |
| `Live` | `Long` | `46.65` | 751,310.00 USD | 0.00 USD | 3,980.00 USD | `-14.06%` | `85.41` |
| `Live` | `Long` | `46.75` | 747,330.00 USD | 0.00 USD | 24,030.00 USD | `-13.88%` | `513.97` |
| `Live` | `Long` | `46.85` | 723,300.00 USD | 0.00 USD | 358.40 USD | `-13.69%` | `7.65` |
| `Live` | `Long` | `46.95` | 722,940.00 USD | 0.00 USD | 158.22 USD | `-13.51%` | `3.37` |
| `Live` | `Long` | `47.05` | 722,780.00 USD | 0.00 USD | 335.47 USD | `-13.32%` | `7.13` |
| `Live` | `Long` | `47.15` | 722,450.00 USD | 0.00 USD | 1,980.00 USD | `-13.14%` | `42.07` |
| `Live` | `Long` | `47.25` | 720,470.00 USD | 0.00 USD | 1,220.00 USD | `-12.96%` | `25.84` |
| `Live` | `Long` | `47.35` | 719,240.00 USD | 0.00 USD | 43,340.00 USD | `-12.77%` | `915.41` |
| `Live` | `Long` | `47.45` | 675,900.00 USD | 0.00 USD | 4,820.00 USD | `-12.59%` | `101.62` |
| `Live` | `Long` | `47.55` | 671,080.00 USD | 0.00 USD | 1,770.00 USD | `-12.40%` | `37.28` |
| `Live` | `Long` | `47.75` | 669,310.00 USD | 0.00 USD | 53,900.00 USD | `-12.04%` | `1,128.71` |
| `Live` | `Long` | `48.05` | 615,410.00 USD | 0.00 USD | 2,540.00 USD | `-11.48%` | `52.86` |
| `Live` | `Long` | `48.15` | 612,870.00 USD | 0.00 USD | 1,690.00 USD | `-11.30%` | `35.03` |
| `Live` | `Long` | `48.25` | 611,180.00 USD | 0.00 USD | 525.44 USD | `-11.11%` | `10.89` |
| `Live` | `Long` | `48.55` | 610,660.00 USD | 0.00 USD | 2,560.00 USD | `-10.56%` | `52.70` |
| `Live` | `Long` | `48.65` | 608,100.00 USD | 0.00 USD | 554.12 USD | `-10.38%` | `11.39` |
| `Live` | `Long` | `48.75` | 607,540.00 USD | 0.00 USD | 333.94 USD | `-10.19%` | `6.85` |
| `Live` | `Long` | `48.95` | 607,210.00 USD | 0.00 USD | 252.58 USD | `-9.82%` | `5.16` |
| `Live` | `Long` | `49.05` | 606,960.00 USD | 0.00 USD | 1,580.00 USD | `-9.64%` | `32.25` |
| `Live` | `Long` | `49.15` | 605,380.00 USD | 0.00 USD | 5,740.00 USD | `-9.46%` | `116.83` |
| `Live` | `Long` | `49.25` | 599,630.00 USD | 0.00 USD | 18,950.00 USD | `-9.27%` | `384.69` |
| `Live` | `Long` | `49.35` | 580,690.00 USD | 0.00 USD | 5,230.00 USD | `-9.09%` | `105.97` |
| `Live` | `Long` | `49.45` | 575,460.00 USD | 0.00 USD | 419.34 USD | `-8.90%` | `8.48` |
| `Live` | `Long` | `49.55` | 575,040.00 USD | 0.00 USD | 26,170.00 USD | `-8.72%` | `528.15` |
| `Live` | `Long` | `49.65` | 548,870.00 USD | 0.00 USD | 73,260.00 USD | `-8.53%` | `1,475.52` |
| `Live` | `Long` | `49.75` | 475,610.00 USD | 0.00 USD | 1,580.00 USD | `-8.35%` | `31.67` |
| `Live` | `Long` | `49.95` | 474,030.00 USD | 0.00 USD | 20,290.00 USD | `-7.98%` | `406.20` |
| `Live` | `Long` | `50.05` | 453,740.00 USD | 0.00 USD | 3,760.00 USD | `-7.80%` | `75.22` |
| `Live` | `Long` | `50.25` | 449,980.00 USD | 0.00 USD | 4,100.00 USD | `-7.43%` | `81.53` |
| `Live` | `Long` | `50.35` | 445,880.00 USD | 0.00 USD | 1,140.00 USD | `-7.25%` | `22.67` |
| `Live` | `Long` | `50.45` | 444,740.00 USD | 0.00 USD | 4,720.00 USD | `-7.06%` | `93.64` |
| `Live` | `Long` | `50.55` | 440,020.00 USD | 0.00 USD | 84,290.00 USD | `-6.88%` | `1,667.45` |
| `Live` | `Long` | `50.75` | 355,730.00 USD | 0.00 USD | 9,050.00 USD | `-6.51%` | `178.28` |
| `Live` | `Long` | `50.95` | 346,680.00 USD | 0.00 USD | 431.55 USD | `-6.14%` | `8.47` |
| `Live` | `Long` | `51.15` | 346,250.00 USD | 0.00 USD | 219,370.00 USD | `-5.77%` | `4,288.79` |
| `Live` | `Long` | `51.25` | 126,880.00 USD | 0.00 USD | 202.44 USD | `-5.59%` | `3.95` |
| `Live` | `Long` | `51.35` | 126,670.00 USD | 0.00 USD | 1,400.00 USD | `-5.40%` | `27.36` |
| `Live` | `Long` | `51.45` | 125,270.00 USD | 0.00 USD | 27,010.00 USD | `-5.22%` | `525.02` |
| `Live` | `Long` | `51.55` | 98,260.00 USD | 0.00 USD | 1,020.00 USD | `-5.03%` | `19.85` |
| `Live` | `Long` | `51.65` | 97,230.00 USD | 0.00 USD | 8,810.00 USD | `-4.85%` | `170.51` |
| `Live` | `Long` | `51.75` | 88,430.00 USD | 0.00 USD | 6,480.00 USD | `-4.67%` | `125.17` |
| `Live` | `Long` | `51.85` | 81,950.00 USD | 0.00 USD | 13,890.00 USD | `-4.48%` | `267.97` |
| `Live` | `Long` | `51.95` | 68,060.00 USD | 0.00 USD | 13,950.00 USD | `-4.30%` | `268.48` |
| `Live` | `Long` | `52.15` | 54,110.00 USD | 0.00 USD | 1,900.00 USD | `-3.93%` | `36.36` |
| `Live` | `Long` | `52.25` | 52,210.00 USD | 0.00 USD | 4,980.00 USD | `-3.75%` | `95.40` |
| `Live` | `Long` | `52.35` | 47,230.00 USD | 0.00 USD | 134.02 USD | `-3.56%` | `2.56` |
| `Live` | `Long` | `52.45` | 47,090.00 USD | 0.00 USD | 2,360.00 USD | `-3.38%` | `44.95` |
| `Live` | `Long` | `52.55` | 44,740.00 USD | 0.00 USD | 8,700.00 USD | `-3.19%` | `165.49` |
| `Live` | `Long` | `52.75` | 36,040.00 USD | 0.00 USD | 4,240.00 USD | `-2.82%` | `80.44` |
| `Live` | `Long` | `52.85` | 31,800.00 USD | 0.00 USD | 5,950.00 USD | `-2.64%` | `112.64` |
| `Live` | `Long` | `52.95` | 25,840.00 USD | 0.00 USD | 25,840.00 USD | `-2.46%` | `488.06` |
| `Live` | `Short` | `56.05` | 2,410.00 USD | 2,410.00 USD | 0.00 USD | `+3.26%` | `43.06` |
| `Live` | `Short` | `56.95` | 2,580.00 USD | 166.29 USD | 0.00 USD | `+4.91%` | `2.92` |
| `Live` | `Short` | `57.95` | 2,710.00 USD | 125.75 USD | 0.00 USD | `+6.76%` | `2.17` |
| `Live` | `Short` | `58.05` | 204,620.00 USD | 201,910.00 USD | 0.00 USD | `+6.94%` | `3,478.21` |
| `Live` | `Short` | `58.85` | 204,830.00 USD | 216.57 USD | 0.00 USD | `+8.41%` | `3.68` |
| `Live` | `Short` | `59.35` | 214,270.00 USD | 9,440.00 USD | 0.00 USD | `+9.33%` | `159.09` |
| `Live` | `Short` | `60.25` | 214,500.00 USD | 221.72 USD | 0.00 USD | `+10.99%` | `3.68` |
| `Live` | `Short` | `60.95` | 214,890.00 USD | 397.39 USD | 0.00 USD | `+12.28%` | `6.52` |
| `Live` | `Short` | `61.15` | 218,760.00 USD | 3,870.00 USD | 0.00 USD | `+12.65%` | `63.26` |
| `Live` | `Short` | `62.25` | 219,090.00 USD | 328.06 USD | 0.00 USD | `+14.68%` | `5.27` |
| `Live` | `Short` | `62.95` | 219,230.00 USD | 138.49 USD | 0.00 USD | `+15.97%` | `2.20` |
| `Live` | `Short` | `63.45` | 222,580.00 USD | 3,350.00 USD | 0.00 USD | `+16.89%` | `52.83` |
| `Live` | `Short` | `66.15` | 229,330.00 USD | 6,750.00 USD | 0.00 USD | `+21.86%` | `102.07` |
| `Live` | `Short` | `66.55` | 273,410.00 USD | 44,080.00 USD | 0.00 USD | `+22.60%` | `662.35` |
| `Live` | `Short` | `66.95` | 273,530.00 USD | 121.18 USD | 0.00 USD | `+23.34%` | `1.81` |
| `Live` | `Short` | `67.85` | 274,240.00 USD | 709.03 USD | 0.00 USD | `+24.99%` | `10.45` |
| `Live` | `Short` | `75.55` | 274,500.00 USD | 260.65 USD | 0.00 USD | `+39.18%` | `3.45` |
| `Live` | `Short` | `76.35` | 282,890.00 USD | 8,380.00 USD | 0.00 USD | `+40.65%` | `109.80` |
| `Live` | `Short` | `77.75` | 861,350.00 USD | 578,460.00 USD | 0.00 USD | `+43.23%` | `7,440.05` |
| `Live` | `Short` | `77.85` | 861,950.00 USD | 602.56 USD | 0.00 USD | `+43.42%` | `7.74` |
| `Live` | `Short` | `77.95` | 862,090.00 USD | 136.41 USD | 0.00 USD | `+43.60%` | `1.75` |
| `Live` | `Short` | `79.35` | 865,260.00 USD | 3,170.00 USD | 0.00 USD | `+46.18%` | `40.00` |
| `Live` | `Short` | `80.15` | 886,650.00 USD | 21,380.00 USD | 0.00 USD | `+47.65%` | `266.81` |
| `Live` | `Short` | `80.75` | 887,290.00 USD | 646.00 USD | 0.00 USD | `+48.76%` | `8.00` |
| `Live` | `Short` | `81.05` | 906,290.00 USD | 19,000.00 USD | 0.00 USD | `+49.31%` | `234.42` |
| `Live` | `Short` | `81.55` | 906,420.00 USD | 123.96 USD | 0.00 USD | `+50.23%` | `1.52` |
| `Live` | `Short` | `82.75` | 906,630.00 USD | 214.32 USD | 0.00 USD | `+52.44%` | `2.59` |
| `Live` | `Short` | `84.95` | 909,430.00 USD | 2,800.00 USD | 0.00 USD | `+56.49%` | `33.00` |
| `Live` | `Short` | `87.75` | 910,230.00 USD | 795.89 USD | 0.00 USD | `+61.65%` | `9.07` |
| `Live` | `Short` | `88.95` | 911,180.00 USD | 945.54 USD | 0.00 USD | `+63.86%` | `10.63` |
| `Live` | `Short` | `97.95` | 911,310.00 USD | 129.29 USD | 0.00 USD | `+80.44%` | `1.32` |
| `Live` | `Short` | `99.85` | 913,800.00 USD | 2,500.00 USD | 0.00 USD | `+83.94%` | `25.00` |
| `Live` | `Short` | `104.25` | 914,020.00 USD | 213.71 USD | 0.00 USD | `+92.05%` | `2.05` |
| `Live` | `Short` | `105.35` | 1,270,000.00 USD | 355,450.00 USD | 0.00 USD | `+94.08%` | `3,374.01` |
| `Live` | `Short` | `106.75` | 1,270,000.00 USD | 1,620.00 USD | 0.00 USD | `+96.65%` | `15.16` |
| `Live` | `Short` | `106.85` | 1,270,000.00 USD | 1,860.00 USD | 0.00 USD | `+96.84%` | `17.43` |
| `Live` | `Short` | `107.15` | 1,270,000.00 USD | 199.30 USD | 0.00 USD | `+97.39%` | `1.86` |
| `Live` | `Short` | `108.05` | 1,280,000.00 USD | 6,470.00 USD | 0.00 USD | `+99.05%` | `59.91` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 741,720.00 USD | 0.00 USD | 392.18 USD | `-63.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 741,330.00 USD | 0.00 USD | 2,310.00 USD | `-59.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 739,030.00 USD | 0.00 USD | 806.86 USD | `-53.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 738,220.00 USD | 0.00 USD | 1,560.00 USD | `-53.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 736,660.00 USD | 0.00 USD | 410.25 USD | `-49.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 736,250.00 USD | 0.00 USD | 281.57 USD | `-44.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 735,970.00 USD | 0.00 USD | 36,050.00 USD | `-33.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 699,920.00 USD | 0.00 USD | 37,550.00 USD | `-30.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 662,370.00 USD | 0.00 USD | 447.01 USD | `-30.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.35` | 661,920.00 USD | 0.00 USD | 73,350.00 USD | `-29.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 588,570.00 USD | 0.00 USD | 40,560.00 USD | `-28.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 548,020.00 USD | 0.00 USD | 489.57 USD | `-27.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 547,530.00 USD | 0.00 USD | 1,180.00 USD | `-26.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 546,350.00 USD | 0.00 USD | 9,840.00 USD | `-26.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 536,510.00 USD | 0.00 USD | 2,060.00 USD | `-24.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 534,450.00 USD | 0.00 USD | 2,960.00 USD | `-23.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 531,500.00 USD | 0.00 USD | 4,010.00 USD | `-22.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.65` | 527,480.00 USD | 0.00 USD | 3,000.00 USD | `-21.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 524,480.00 USD | 0.00 USD | 5,680.00 USD | `-20.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 518,800.00 USD | 0.00 USD | 672.22 USD | `-19.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.35` | 518,130.00 USD | 0.00 USD | 329,970.00 USD | `-18.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 188,160.00 USD | 0.00 USD | 213.80 USD | `-18.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 187,950.00 USD | 0.00 USD | 223.20 USD | `-17.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 187,730.00 USD | 0.00 USD | 391.13 USD | `-17.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 187,330.00 USD | 0.00 USD | 7,080.00 USD | `-17.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 180,260.00 USD | 0.00 USD | 1,370.00 USD | `-16.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 178,890.00 USD | 0.00 USD | 553.80 USD | `-14.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.45` | 178,340.00 USD | 0.00 USD | 3,080.00 USD | `-14.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 175,260.00 USD | 0.00 USD | 14,000.00 USD | `-14.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 161,260.00 USD | 0.00 USD | 158.56 USD | `-13.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 161,110.00 USD | 0.00 USD | 373.28 USD | `-12.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 160,730.00 USD | 0.00 USD | 849.46 USD | `-12.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 159,880.00 USD | 0.00 USD | 1,150.00 USD | `-11.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.15` | 158,730.00 USD | 0.00 USD | 303.35 USD | `-11.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 158,430.00 USD | 0.00 USD | 1,740.00 USD | `-10.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 156,690.00 USD | 0.00 USD | 981.00 USD | `-9.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.35` | 155,710.00 USD | 0.00 USD | 817.24 USD | `-9.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 154,890.00 USD | 0.00 USD | 237.85 USD | `-8.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.55` | 154,650.00 USD | 0.00 USD | 1,420.00 USD | `-8.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.85` | 153,240.00 USD | 0.00 USD | 108.17 USD | `-8.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 153,130.00 USD | 0.00 USD | 298.20 USD | `-7.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 152,830.00 USD | 0.00 USD | 14,650.00 USD | `-7.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 138,180.00 USD | 0.00 USD | 6,410.00 USD | `-7.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 131,760.00 USD | 0.00 USD | 459.70 USD | `-7.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 131,300.00 USD | 0.00 USD | 236.57 USD | `-6.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 131,060.00 USD | 0.00 USD | 1,020.00 USD | `-5.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 130,040.00 USD | 0.00 USD | 439.89 USD | `-5.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.45` | 129,600.00 USD | 0.00 USD | 204.26 USD | `-5.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 129,400.00 USD | 0.00 USD | 10,190.00 USD | `-4.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.85` | 119,210.00 USD | 0.00 USD | 106.29 USD | `-4.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.95` | 119,110.00 USD | 0.00 USD | 8,700.00 USD | `-4.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 110,410.00 USD | 0.00 USD | 26,490.00 USD | `-4.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 83,920.00 USD | 0.00 USD | 51,800.00 USD | `-3.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 32,120.00 USD | 0.00 USD | 5,460.00 USD | `-3.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 26,660.00 USD | 0.00 USD | 271.13 USD | `-2.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.85` | 26,390.00 USD | 0.00 USD | 135.82 USD | `-2.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 26,250.00 USD | 0.00 USD | 115.43 USD | `-2.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 26,140.00 USD | 0.00 USD | 9,240.00 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 16,890.00 USD | 0.00 USD | 2,660.00 USD | `-2.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.25` | 14,240.00 USD | 0.00 USD | 881.82 USD | `-1.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 13,350.00 USD | 0.00 USD | 566.57 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 12,790.00 USD | 0.00 USD | 5,950.00 USD | `-1.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 6,840.00 USD | 0.00 USD | 1,370.00 USD | `-1.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.75` | 5,470.00 USD | 0.00 USD | 1,120.00 USD | `-0.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 4,350.00 USD | 0.00 USD | 462.03 USD | `-0.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 3,880.00 USD | 0.00 USD | 397.81 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.15` | 3,490.00 USD | 0.00 USD | 398.54 USD | `-0.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 3,090.00 USD | 0.00 USD | 3,090.00 USD | `-0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `54.35` | 156.53 USD | 156.53 USD | 0.00 USD | `+0.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `54.45` | 300.82 USD | 144.29 USD | 0.00 USD | `+0.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `54.55` | 1,990.00 USD | 1,690.00 USD | 0.00 USD | `+0.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `54.65` | 2,190.00 USD | 198.38 USD | 0.00 USD | `+0.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `54.75` | 2,390.00 USD | 198.74 USD | 0.00 USD | `+0.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `54.85` | 35,670.00 USD | 33,280.00 USD | 0.00 USD | `+1.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `54.95` | 36,060.00 USD | 397.84 USD | 0.00 USD | `+1.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.05` | 36,230.00 USD | 160.75 USD | 0.00 USD | `+1.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.15` | 36,620.00 USD | 398.18 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.25` | 37,020.00 USD | 398.90 USD | 0.00 USD | `+1.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.35` | 37,430.00 USD | 407.38 USD | 0.00 USD | `+1.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.45` | 37,840.00 USD | 408.11 USD | 0.00 USD | `+2.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.55` | 37,990.00 USD | 156.65 USD | 0.00 USD | `+2.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.65` | 41,610.00 USD | 3,610.00 USD | 0.00 USD | `+2.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.75` | 41,810.00 USD | 202.37 USD | 0.00 USD | `+2.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.85` | 42,010.00 USD | 196.59 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.95` | 42,200.00 USD | 193.03 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.05` | 42,830.00 USD | 632.24 USD | 0.00 USD | `+3.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.15` | 43,020.00 USD | 193.72 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.25` | 43,230.00 USD | 204.19 USD | 0.00 USD | `+3.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.35` | 43,620.00 USD | 387.12 USD | 0.00 USD | `+3.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.45` | 44,020.00 USD | 407.57 USD | 0.00 USD | `+3.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.55` | 46,660.00 USD | 2,640.00 USD | 0.00 USD | `+4.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.65` | 46,780.00 USD | 121.23 USD | 0.00 USD | `+4.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.75` | 47,010.00 USD | 228.70 USD | 0.00 USD | `+4.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.85` | 65,040.00 USD | 18,030.00 USD | 0.00 USD | `+4.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.95` | 65,430.00 USD | 390.68 USD | 0.00 USD | `+4.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.05` | 71,230.00 USD | 5,800.00 USD | 0.00 USD | `+5.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.15` | 71,620.00 USD | 392.05 USD | 0.00 USD | `+5.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.25` | 71,830.00 USD | 201.52 USD | 0.00 USD | `+5.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.35` | 72,030.00 USD | 207.03 USD | 0.00 USD | `+5.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.45` | 72,380.00 USD | 344.70 USD | 0.00 USD | `+5.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.55` | 92,740.00 USD | 20,360.00 USD | 0.00 USD | `+6.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.65` | 92,860.00 USD | 118.18 USD | 0.00 USD | `+6.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.75` | 92,970.00 USD | 119.54 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.95` | 93,100.00 USD | 128.65 USD | 0.00 USD | `+6.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 93,850.00 USD | 747.68 USD | 0.00 USD | `+6.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 94,050.00 USD | 200.04 USD | 0.00 USD | `+7.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 94,250.00 USD | 200.96 USD | 0.00 USD | `+7.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 94,380.00 USD | 123.70 USD | 0.00 USD | `+7.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 94,980.00 USD | 601.45 USD | 0.00 USD | `+7.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 95,590.00 USD | 611.85 USD | 0.00 USD | `+7.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.65` | 95,860.00 USD | 274.48 USD | 0.00 USD | `+8.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 96,350.00 USD | 491.15 USD | 0.00 USD | `+8.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 99,300.00 USD | 2,940.00 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 99,430.00 USD | 129.69 USD | 0.00 USD | `+8.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 104,230.00 USD | 4,800.00 USD | 0.00 USD | `+8.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 105,510.00 USD | 1,280.00 USD | 0.00 USD | `+8.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.25` | 105,720.00 USD | 210.34 USD | 0.00 USD | `+9.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 106,180.00 USD | 461.74 USD | 0.00 USD | `+9.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 106,340.00 USD | 159.92 USD | 0.00 USD | `+9.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.55` | 106,830.00 USD | 496.65 USD | 0.00 USD | `+9.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 107,560.00 USD | 724.75 USD | 0.00 USD | `+9.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.75` | 107,670.00 USD | 113.53 USD | 0.00 USD | `+10.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 107,830.00 USD | 158.00 USD | 0.00 USD | `+10.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 108,000.00 USD | 171.14 USD | 0.00 USD | `+10.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 108,550.00 USD | 551.00 USD | 0.00 USD | `+11.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.45` | 108,710.00 USD | 155.36 USD | 0.00 USD | `+11.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 109,590.00 USD | 878.58 USD | 0.00 USD | `+11.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 110,970.00 USD | 1,390.00 USD | 0.00 USD | `+11.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 111,960.00 USD | 986.99 USD | 0.00 USD | `+12.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 112,640.00 USD | 674.72 USD | 0.00 USD | `+12.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 115,000.00 USD | 2,360.00 USD | 0.00 USD | `+12.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 115,120.00 USD | 125.56 USD | 0.00 USD | `+12.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 118,720.00 USD | 3,600.00 USD | 0.00 USD | `+13.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 119,360.00 USD | 643.20 USD | 0.00 USD | `+13.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.95` | 121,480.00 USD | 2,120.00 USD | 0.00 USD | `+14.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 121,610.00 USD | 130.31 USD | 0.00 USD | `+14.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.55` | 121,960.00 USD | 347.15 USD | 0.00 USD | `+15.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 122,680.00 USD | 716.72 USD | 0.00 USD | `+15.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.75` | 122,820.00 USD | 141.19 USD | 0.00 USD | `+15.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 123,050.00 USD | 231.39 USD | 0.00 USD | `+16.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 123,680.00 USD | 630.87 USD | 0.00 USD | `+16.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 124,380.00 USD | 703.97 USD | 0.00 USD | `+16.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.35` | 124,520.00 USD | 140.64 USD | 0.00 USD | `+16.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 125,190.00 USD | 668.13 USD | 0.00 USD | `+16.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 133,920.00 USD | 8,730.00 USD | 0.00 USD | `+17.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 134,480.00 USD | 555.03 USD | 0.00 USD | `+17.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 135,010.00 USD | 531.62 USD | 0.00 USD | `+17.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.35` | 135,670.00 USD | 664.09 USD | 0.00 USD | `+18.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.45` | 136,340.00 USD | 665.12 USD | 0.00 USD | `+18.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 136,540.00 USD | 202.69 USD | 0.00 USD | `+18.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 136,840.00 USD | 298.04 USD | 0.00 USD | `+19.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 136,940.00 USD | 102.13 USD | 0.00 USD | `+19.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 137,480.00 USD | 540.09 USD | 0.00 USD | `+20.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 137,580.00 USD | 100.79 USD | 0.00 USD | `+20.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 137,850.00 USD | 262.20 USD | 0.00 USD | `+20.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 138,220.00 USD | 371.49 USD | 0.00 USD | `+21.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.85` | 139,100.00 USD | 881.07 USD | 0.00 USD | `+21.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 139,790.00 USD | 696.17 USD | 0.00 USD | `+21.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 140,330.00 USD | 534.00 USD | 0.00 USD | `+22.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 151,410.00 USD | 11,080.00 USD | 0.00 USD | `+23.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 158,110.00 USD | 6,710.00 USD | 0.00 USD | `+23.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.05` | 160,470.00 USD | 2,360.00 USD | 0.00 USD | `+25.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 165,340.00 USD | 4,860.00 USD | 0.00 USD | `+25.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 165,540.00 USD | 204.48 USD | 0.00 USD | `+28.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.65` | 683,740.00 USD | 518,200.00 USD | 0.00 USD | `+28.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 684,550.00 USD | 810.02 USD | 0.00 USD | `+28.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 1,010,000.00 USD | 323,460.00 USD | 0.00 USD | `+29.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 1,010,000.00 USD | 170.04 USD | 0.00 USD | `+30.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 1,010,000.00 USD | 5,770.00 USD | 0.00 USD | `+30.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 1,010,000.00 USD | 269.28 USD | 0.00 USD | `+30.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 1,010,000.00 USD | 291.40 USD | 0.00 USD | `+32.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 1,020,000.00 USD | 7,220.00 USD | 0.00 USD | `+32.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 1,020,000.00 USD | 156.78 USD | 0.00 USD | `+33.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 1,030,000.00 USD | 3,220.00 USD | 0.00 USD | `+33.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 1,030,000.00 USD | 411.14 USD | 0.00 USD | `+35.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 1,150,000.00 USD | 123,190.00 USD | 0.00 USD | `+36.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 1,150,000.00 USD | 1,020.00 USD | 0.00 USD | `+37.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.75` | 1,150,000.00 USD | 811.04 USD | 0.00 USD | `+37.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 1,150,000.00 USD | 104.93 USD | 0.00 USD | `+38.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 1,150,000.00 USD | 133.59 USD | 0.00 USD | `+38.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 1,150,000.00 USD | 402.59 USD | 0.00 USD | `+38.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.85` | 1,150,000.00 USD | 308.71 USD | 0.00 USD | `+39.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 1,150,000.00 USD | 315.18 USD | 0.00 USD | `+42.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 1,210,000.00 USD | 59,310.00 USD | 0.00 USD | `+44.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 1,210,000.00 USD | 3,160.00 USD | 0.00 USD | `+45.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.35` | 1,220,000.00 USD | 5,260.00 USD | 0.00 USD | `+46.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 1,230,000.00 USD | 5,690.00 USD | 0.00 USD | `+46.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 1,260,000.00 USD | 36,590.00 USD | 0.00 USD | `+47.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 1,260,000.00 USD | 433.89 USD | 0.00 USD | `+49.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 1,260,000.00 USD | 172.64 USD | 0.00 USD | `+49.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 1,260,000.00 USD | 164.10 USD | 0.00 USD | `+51.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 1,260,000.00 USD | 546.81 USD | 0.00 USD | `+52.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 1,270,000.00 USD | 2,300.00 USD | 0.00 USD | `+54.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 1,280,000.00 USD | 12,070.00 USD | 0.00 USD | `+56.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.05` | 1,300,000.00 USD | 20,230.00 USD | 0.00 USD | `+60.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 1,300,000.00 USD | 1,580.00 USD | 0.00 USD | `+62.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 1,340,000.00 USD | 37,000.00 USD | 0.00 USD | `+62.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 1,340,000.00 USD | 473.21 USD | 0.00 USD | `+63.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 1,340,000.00 USD | 422.99 USD | 0.00 USD | `+64.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 1,340,000.00 USD | 1,630.00 USD | 0.00 USD | `+64.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 1,340,000.00 USD | 4,870.00 USD | 0.00 USD | `+65.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 1,340,000.00 USD | 481.55 USD | 0.00 USD | `+68.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 1,350,000.00 USD | 1,330.00 USD | 0.00 USD | `+69.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 1,350,000.00 USD | 188.10 USD | 0.00 USD | `+73.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,610,000.00 USD | 266,140.00 USD | 0.00 USD | `+75.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,620,000.00 USD | 3,400.00 USD | 0.00 USD | `+75.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,640,000.00 USD | 21,930.00 USD | 0.00 USD | `+76.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,640,000.00 USD | 294.15 USD | 0.00 USD | `+80.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 1,650,000.00 USD | 15,380.00 USD | 0.00 USD | `+82.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,660,000.00 USD | 3,660.00 USD | 0.00 USD | `+84.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,660,000.00 USD | 306.15 USD | 0.00 USD | `+88.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,660,000.00 USD | 936.72 USD | 0.00 USD | `+89.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,660,000.00 USD | 2,920.00 USD | 0.00 USD | `+90.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,660,000.00 USD | 324.15 USD | 0.00 USD | `+99.05%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `407.72M` | Total OI Tokens: `7,510,969.2 LTC`
  * 1h OI Change: `-0.30%` | 4h OI Change: `-2.20%` | 24h OI Change: `-11.32%`
  * Exchange Breakdown: Binance=`72.25M` | Bybit=`64.86M` | OKX=`33.67M` | Hyperliquid=`21.93M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `8.75K` | Last 24h: `31.76K` | Last 3d: `59.78K` | Last 7d: `115.16K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0041%` | **USDT OKX** | `-0.0007%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0040%` |
| **USDT MEXC** | `0.0041%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0002%` | **USDT Bitget** | `-0.0032%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `55.49%` | `44.51%` | `1.25` | 18,850,000.00 USD |
| `15M` | `Binance` | `57.04%` | `42.96%` | `1.33` | 8,080,000.00 USD |
| `15M` | `OKX` | `49.9%` | `50.1%` | `1.00` | 2,580,000.00 USD |
| `15M` | `Bybit` | `53.96%` | `46.04%` | `1.17` | 2,110,000.00 USD |
| `15M` | `KuCoin` | `63.46%` | `36.54%` | `1.74` | 154,150.00 USD |
| `15M` | `Gate` | `71.21%` | `28.79%` | `2.47` | 617,440.00 USD |
| `15M` | `Bitget` | `45.01%` | `54.99%` | `0.82` | 1,340,000.00 USD |
| `15M` | `BingX` | `52.42%` | `47.58%` | `1.10` | 693,570.00 USD |
| `15M` | `MEXC` | `59.09%` | `40.91%` | `1.44` | 489,560.00 USD |
| `15M` | `Bitunix` | `51.01%` | `48.99%` | `1.04` | 295,140.00 USD |
| `15M` | `Hyperliquid` | `53.59%` | `46.41%` | `1.15` | 1,820,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `56.36%` | `43.64%` | `1.29` | 87,910.00 USD |
| `15M` | `Crypto.com` | `43.65%` | `56.35%` | `0.77` | 853.14 USD |
| `15M` | `WhiteBIT` | `91.13%` | `8.87%` | `10.27` | 380,600.00 USD |
| `15M` | `HTX` | `65.02%` | `34.98%` | `1.86` | 11,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `49.81%` | `50.19%` | `0.99` | 116,100.00 USD |
| `15M` | `Aster` | `64.64%` | `35.36%` | `1.83` | 60,210.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `44.7%` | `55.3%` | `0.81` | 19,000.00 USD |
| `15M` | `Whale Positions` | `57.04%` | `42.96%` | `1.33` | 8,080,000.00 USD |
| `15M` | `Global Accounts` | `55.49%` | `44.51%` | `1.25` | 18,850,000.00 USD |
| `1H` | `LTC` | `49.17%` | `50.83%` | `0.97` | 10,730,000.00 USD |
| `1H` | `Binance` | `49.2%` | `50.8%` | `0.97` | 4,190,000.00 USD |
| `1H` | `OKX` | `59.99%` | `40.01%` | `1.50` | 1,300,000.00 USD |
| `1H` | `Bybit` | `45.97%` | `54.03%` | `0.85` | 795,460.00 USD |
| `1H` | `KuCoin` | `43.82%` | `56.18%` | `0.78` | 656,290.00 USD |
| `1H` | `Gate` | `47.43%` | `52.57%` | `0.90` | 336,630.00 USD |
| `1H` | `Bitget` | `40.89%` | `59.11%` | `0.69` | 301,600.00 USD |
| `1H` | `BingX` | `24.65%` | `75.35%` | `0.33` | 771,910.00 USD |
| `1H` | `MEXC` | `57.15%` | `42.85%` | `1.33` | 630,060.00 USD |
| `1H` | `Bitunix` | `46.1%` | `53.9%` | `0.86` | 264,450.00 USD |
| `1H` | `Hyperliquid` | `49.05%` | `50.95%` | `0.96` | 148,150.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.65%` | `50.35%` | `0.99` | 996,760.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `99.5%` | `0.5%` | `199.00` | 238,150.00 USD |
| `1H` | `HTX` | `34.53%` | `65.47%` | `0.53` | 10,580.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `23.65%` | `76.35%` | `0.31` | 82,200.00 USD |
| `1H` | `Aster` | `1.4%` | `98.6%` | `0.01` | 10,270.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `49.2%` | `50.8%` | `0.97` | 4,190,000.00 USD |
| `1H` | `Global Accounts` | `49.17%` | `50.83%` | `0.97` | 10,730,000.00 USD |
| `4H` | `LTC` | `46.49%` | `53.51%` | `0.87` | 597,730,000.00 USD |
| `4H` | `Binance` | `47.69%` | `52.31%` | `0.91` | 233,950,000.00 USD |
| `4H` | `OKX` | `48.68%` | `51.32%` | `0.95` | 67,400,000.00 USD |
| `4H` | `Bybit` | `46.71%` | `53.29%` | `0.88` | 80,070,000.00 USD |
| `4H` | `KuCoin` | `44.3%` | `55.7%` | `0.80` | 4,040,000.00 USD |
| `4H` | `Gate` | `42.24%` | `57.76%` | `0.73` | 16,670,000.00 USD |
| `4H` | `Bitget` | `48.6%` | `51.4%` | `0.95` | 25,590,000.00 USD |
| `4H` | `BingX` | `45.18%` | `54.82%` | `0.82` | 19,610,000.00 USD |
| `4H` | `MEXC` | `43.91%` | `56.09%` | `0.78` | 27,880,000.00 USD |
| `4H` | `Bitunix` | `47.93%` | `52.07%` | `0.92` | 10,110,000.00 USD |
| `4H` | `Hyperliquid` | `39.44%` | `60.56%` | `0.65` | 86,070,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.81%` | `47.19%` | `1.12` | 2,080,000.00 USD |
| `4H` | `Crypto.com` | `46.49%` | `53.51%` | `0.87` | 24,950.00 USD |
| `4H` | `WhiteBIT` | `81.06%` | `18.94%` | `4.28` | 11,660,000.00 USD |
| `4H` | `HTX` | `37.03%` | `62.97%` | `0.59` | 1,070,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `40.24%` | `59.76%` | `0.67` | 4,100,000.00 USD |
| `4H` | `Aster` | `18.52%` | `81.48%` | `0.23` | 3,620,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `44%` | `56%` | `0.79` | 3,770,000.00 USD |
| `4H` | `Whale Positions` | `47.69%` | `52.31%` | `0.91` | 233,950,000.00 USD |
| `4H` | `Global Accounts` | `46.49%` | `53.51%` | `0.87` | 597,730,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `54.95` | `55.00` | `54.95` | `55.16` | `54.84` | 1,116,493.17 USD | 544,065.41 USD | 572,427.76 USD | -28,362.36 USD | `-2.54%` | `1B / 2S` |
| `0:00 UTC` | `54.78` | `54.81` | `54.78` | `55.03` | `54.59` | 2,311,809.84 USD | 1,167,618.18 USD | 1,144,191.66 USD | 23,426.51 USD | `+1.01%` | `4B / 7S` |
| `5:00 UTC` | `52.92` | `53.63` | `52.92` | `54.96` | `52.78` | 9,644,230.66 USD | 4,219,507.37 USD | 5,424,723.28 USD | -1,205,215.91 USD | `-12.50%` | `3B / 25S` |
| `0:00 UTC` | `53.92` | `53.53` | `53.92` | `53.97` | `53.03` | 2,679,572.06 USD | 1,410,180.46 USD | 1,269,391.60 USD | 140,788.86 USD | `+5.25%` | `16B / 8S` |
| `5:00 UTC` | `54.28` | `54.12` | `54.28` | `54.38` | `53.70` | 1,241,557.04 USD | 584,397.22 USD | 657,159.82 USD | -72,762.60 USD | `-5.86%` | `12B / 6S` |
| `0:00 UTC` | `54.30` | `54.36` | `54.30` | `54.62` | `54.16` | 1,483,061.64 USD | 620,330.38 USD | 862,731.26 USD | -242,400.88 USD | `-16.34%` | `4B / 6S` |
| `5:00 UTC` | `54.11` | `54.23` | `54.11` | `54.50` | `54.03` | 1,110,276.34 USD | 501,463.73 USD | 608,812.62 USD | -107,348.89 USD | `-9.67%` | `2B / 8S` |
| `0:00 UTC` | `53.86` | `54.08` | `53.86` | `54.55` | `53.64` | 1,780,531.79 USD | 1,005,907.66 USD | 774,624.13 USD | 231,283.53 USD | `+12.99%` | `11B / 6S` |
| `5:00 UTC` | `54.34` | `54.28` | `54.34` | `54.41` | `54.11` | 777,440.60 USD | 385,500.86 USD | 391,939.75 USD | -6,438.89 USD | `-0.83%` | `0B / 4S` |
| `0:00 UTC` | `54.03` | `54.14` | `54.03` | `54.38` | `53.91` | 446,478.31 USD | 226,443.59 USD | 220,034.72 USD | 6,408.86 USD | `+1.44%` | `6B / 5S` |

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
| `5m` | 47,110.00 USD | 69,410.00 USD | **`ACCUMULATION`** |
| `15m` | 15,790.00 USD | 43,200.00 USD | **`ACCUMULATION`** |
| `30m` | -50,030.00 USD | 132,830.00 USD | **`ACCUMULATION`** |
| `1h` | -152,150.00 USD | 124,500.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,150,000.00 USD | -1,960,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -340,740.00 USD | -2,240,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -2,180,000.00 USD | -5,100,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,350,000.00 USD | -5,890,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -356,190.00 USD | -5,530,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -26,120.00 USD | -4,410,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 3,220,000.00 USD | -25,150,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -23,520,000.00 USD | -194,290,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+47.11K` | 15m=`+15.79K` | 1h=`-152.15K` | 24h=`-26.12K`
* Futures Capital Netflows: 5m=`+69.41K` | 15m=`+43.20K` | 1h=`+124.50K` | 24h=`-4.41M`
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
  * `2026-10-30 07:16:34 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:38:34 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:38:34 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 07:38:34 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 07:38:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:37:34 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 07:37:34 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 07:37:34 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 07:37:34 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 07:37:34 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:39:34 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:34 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:34 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:39:34 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:34 IST`: [sec.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `54.08` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `52.92` (Risk Distance: `1.16` pts)
  * +2.5R Take Profit: `56.98`
  * Mathematical Lot Sizing: **`8.62 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `55.86` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `57.02` (Risk Distance: `1.16` pts)
  * +2.5R Take Profit: `52.96`
  * Mathematical Lot Sizing: **`8.62 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`54.82`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
