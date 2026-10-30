# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 07:39:18 IST` (`2026-10-30 02:09:18 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `54.01` | **Live Ask Quote**: `54.31` | **Mid Price**: `54.16`
- **Spread Points**: `300.00` | **Spread BPS**: `55.39 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `53.86` | VWAP Z-Score: `-1.46` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.6140` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `38.18` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `61.14` | Lower -3.00σ Band: `51.77`
  * Upper +2.51σ Band: `60.37` | Lower -2.51σ Band: `52.54`
  * Upper +2.01σ Band: `59.59` | Lower -2.01σ Band: `53.32`
  * Upper +2.00σ Band: `59.58` | Lower -2.00σ Band: `53.33`
  * Upper +1.28σ Band: `58.45` | Lower -1.28σ Band: `54.46`
  * Upper +1.00σ Band: `58.02` | Lower -1.00σ Band: `54.89`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`54.26` | EMA-20=`54.86` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`55.97` (Slope: `+0.0000`) | EMA-100=`56.69`
  * Institutional Anchors: EMA-144=`56.90` | EMA-200=`56.89` (Slope: `-0.5535`) | EMA-233=`56.91`
- **Range Boundaries**: 24H High=`58.91` | 24H Low=`52.64` | Weekly High=`59.62` | Weekly Low=`52.64`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `55.86` (Distance: `-3.00%`)
  * Point of Control (POC) = `55.27` (Distance: `-1.98%`)
  * Value Area Low (VAL) = `54.12` (Distance: `+0.10%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.40` | POC=`57.72` | VAL=`56.83`
  * Prior Day Extremes: PDH=`59.52` | PDL=`54.18` | PDC=`54.46`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`58.25` | Weekly POC=`56.43` | Weekly VAL=`55.97`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`55.89` | Low=`52.64`
  * London Session (08:00-16:00 UTC): High=`54.38` | Low=`53.94`
  * New York Session (13:00-21:00 UTC): High=`54.48` | Low=`53.84`
  * Initial Balance (First Hour): IB High=`54.32` | IB Low=`54.00`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `53.94` - `54.38`
  * Optimal Trade Entry (OTE 0.705): `54.27`
  * Structural Invalidation Anchor (0.786): `54.59`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `54.39` | `54.41` | `54.13` | `54.32` | `4,257` | 230,926.92 USD | -47,729.19 USD | `-20.67%` | -4,831,288.56 USD | `+0.08` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `54.33` | `54.35` | `54.11` | `54.31` | `4,921` | 266,986.16 USD | -10,710.74 USD | `-4.01%` | -4,841,999.30 USD | `+0.19` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `54.32` | `54.36` | `54.20` | `54.23` | `3,003` | 163,118.25 USD | 43,978.03 USD | `+26.96%` | -4,798,021.27 USD | `+0.46` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `54.50` | `54.50` | `54.03` | `54.13` | `20,476` | 1,110,276.34 USD | -107,348.89 USD | `-9.67%` | -5,014,842.90 USD | `+0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `54.14` | `54.54` | `53.64` | `54.39` | `32,927` | 1,780,531.79 USD | 231,283.53 USD | `+12.99%` | -4,783,559.37 USD | `+0.66` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `54.39` | `54.41` | `54.11` | `54.22` | `12,084` | 655,762.52 USD | -11,000.14 USD | `-1.68%` | -4,794,559.52 USD | `+0.10` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `55.43` | `55.56` | `54.84` | `54.92` | `72,918` | 4,028,662.41 USD | -432,675.62 USD | `-10.74%` | -3,551,269.19 USD | `-0.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `54.92` | `55.02` | `52.77` | `54.37` | `295,042` | 15,877,230.39 USD | -1,113,823.94 USD | `-7.02%` | -4,665,093.13 USD | `-1.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `54.36` | `54.62` | `53.64` | `54.24` | `92,776` | 5,029,944.31 USD | -129,154.36 USD | `-2.57%` | -4,794,247.49 USD | `+0.06` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | 340,473.45 USD | `+0.15` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,923,567.46 USD | `-1.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `55.02` | `52.77` | `54.21` | `387,804` | 20,906,431.64 USD | -1,243,078.44 USD | `-5.95%` | -4,166,645.90 USD | `-0.43` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `57.04` | `58.16` | `56.85` | `58.00` | `178,996` | 10,300,529.12 USD | 452,809.17 USD | `+4.40%` | -47,398.66 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | 201,186.90 USD | `+0.44` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | 340,473.45 USD | `+0.15` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,923,567.46 USD | `-1.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `55.02` | `52.77` | `54.21` | `387,804` | 20,906,431.64 USD | -1,243,078.44 USD | `-5.95%` | -4,166,645.90 USD | `-0.43` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`54.16`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:28:02 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1080` | `0xeadc...9d55` | `LONG` | 1,979,581.61 USD | `36,463.77` | `52.78` | `54.32` | `0.000000` | 54,905.66 USD | `+2.77%` | `10X Cross` |
| `1090` | `0x9aa5...58af` | `SHORT` | 1,963,180.18 USD | `36,177.65` | `71.22` | `54.32` | `318.16` | 613,306.49 USD | `+31.24%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `59.08` | 6,432.04 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 6.43K USD at 59.0800 USD [API] | `2026-10-28 19:23:55` |
| `ANNOUNCEMENT` | `INFO` | `59.10` | 7,180.65 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 7.18K USD at 59.1000 USD [API] | `2026-10-28 19:28:02` |
| `ANNOUNCEMENT` | `INFO` | `59.44` | 7,505.45 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 7.51K USD at 59.4350 USD [API] | `2026-10-28 19:51:29` |
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
| `Live` | `Long Liquidation` | `11.35` | 136.20 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `11.65` | 195.02 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.25` | 122.50 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.35` | 395.20 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.75` | 2,560.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.15` | 2,220.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.65` | 150.15 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `14.35` | 129.44 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `16.05` | 169.17 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `16.35` | 327.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `17.45` | 2,090.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.85` | 2,840.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.05` | 3,470.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.45` | 2,170.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.05` | 6,360.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.75` | 366.96 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.85` | 4,460.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.45` | 1,410.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.65` | 156.09 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.85` | 195.57 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.25` | 943.81 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.65` | 1,040.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.75` | 23,020.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 277,980.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 173.39 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 50,890.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 6,210.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.95` | 5,490.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 272.75 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.85` | 233.94 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 173.85 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.85` | 458.14 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.95` | 36,370.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 583.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 297,600.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 693.85 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 538.53 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 5,880.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.25` | 3,880.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 5,680.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.75` | 22,160.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 2,870.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 125.24 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 1,360.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.35` | 1,070.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 2,290.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 953.68 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 32,850.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.45` | 627.19 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 257.76 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.75` | 4,410.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.95` | 237.65 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 182.85 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 126.70 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 3,240.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 104.85 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 166.49 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.15` | 175.75 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.05` | 10,810.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 3,020.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 423.18 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 389.55 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 359.76 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 438.74 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 10,320.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 3,980.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 6,210.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 446.67 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.25` | 5,050.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 341.70 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 2,400.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 4,880.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 384.57 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 2,730.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 664,760.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 940.77 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 264.83 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 865.53 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 162.95 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 5,900.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 2,580.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 8,900.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.95` | 337.58 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 2,160.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 1,010.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 133.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 1,650.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 6,340.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 509.01 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 396.54 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 14,490.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 644.96 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.55` | 41,550.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.65` | 5,360.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.95` | 1,050.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 6,200.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 66,300.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 35,410.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 1,570.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 5,800.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 2,000.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 8,950.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 126,620.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 7,850.00 USD | 958,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 5,390.00 USD | 950,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 706.06 USD | 945,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 26,650.00 USD | 944,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 21,880.00 USD | 917,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 801.14 USD | 895,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 3,180.00 USD | 895,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 85,770.00 USD | 891,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.45` | 3,800.00 USD | 806,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 842.44 USD | 802,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 4,230.00 USD | 801,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 134.55 USD | 797,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 2,620.00 USD | 797,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 329.32 USD | 794,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 1,060.00 USD | 794,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 3,180.00 USD | 793,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 2,180.00 USD | 790,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 24,110.00 USD | 787,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 11,950.00 USD | 763,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 342.38 USD | 751,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 971.65 USD | 751,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.35` | 383.78 USD | 750,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 2,530.00 USD | 750,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 2,000.00 USD | 747,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 158.22 USD | 745,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 9,740.00 USD | 745,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 574.09 USD | 735,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.35` | 43,340.00 USD | 735,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.45` | 4,820.00 USD | 691,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 1,770.00 USD | 686,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 4,780.00 USD | 685,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 1,340.00 USD | 680,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 1,690.00 USD | 679,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 525.44 USD | 677,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 2,030.00 USD | 676,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 273.90 USD | 674,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 333.94 USD | 674,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 797.40 USD | 674,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,580.00 USD | 673,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,740.00 USD | 671,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.25` | 263.49 USD | 666,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.30` | 2,870,000.00 USD | 2,870,000.00 USD | 13,300.00 USD | 4,090.00 USD | 367.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.30` | 8,100,000.00 USD | 8,100,000.00 USD | 15,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.35` | 24,210.00 USD | 665,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.40` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 626.48 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.40` | 8,080,000.00 USD | 8,080,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.45` | 1,960.00 USD | 641,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.50` | 2,850,000.00 USD | 2,850,000.00 USD | 1,180.00 USD | 4,200.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.50` | 8,070,000.00 USD | 8,070,000.00 USD | 1,130.00 USD | 6,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.55` | 18,010.00 USD | 639,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.60` | 2,830,000.00 USD | 2,830,000.00 USD | 980.75 USD | 4,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.60` | 8,070,000.00 USD | 8,070,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.65` | 73,260.00 USD | 621,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.70` | 2,820,000.00 USD | 2,820,000.00 USD | 3,550.00 USD | 1,980.00 USD | 416.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.70` | 8,050,000.00 USD | 8,050,000.00 USD | 788.92 USD | 0.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.75` | 1,580.00 USD | 548,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.80` | 2,820,000.00 USD | 2,820,000.00 USD | 2,920.00 USD | 388.95 USD | 14,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.80` | 8,040,000.00 USD | 8,040,000.00 USD | 8,590.00 USD | 8,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.85` | 1,930.00 USD | 546,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.90` | 2,800,000.00 USD | 2,800,000.00 USD | 17,280.00 USD | 8,370.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.90` | 8,030,000.00 USD | 8,030,000.00 USD | 45,030.00 USD | 7,170.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.95` | 28,540.00 USD | 544,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.00` | 2,750,000.00 USD | 2,750,000.00 USD | 7,520.00 USD | 6,290.00 USD | 40,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.00` | 7,970,000.00 USD | 7,970,000.00 USD | 22,100.00 USD | 7,630.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.05` | 1,820.00 USD | 516,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.10` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.10` | 7,920,000.00 USD | 7,920,000.00 USD | 363.50 USD | 682.90 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.20` | 7,920,000.00 USD | 7,920,000.00 USD | 6,960.00 USD | 500.40 USD | 34,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.25` | 102.51 USD | 514,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.30` | 7,870,000.00 USD | 7,870,000.00 USD | 16,270.00 USD | 3,640.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.35` | 1,030.00 USD | 514,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.40` | 2,690,000.00 USD | 2,690,000.00 USD | 349.63 USD | 2,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.40` | 7,850,000.00 USD | 7,850,000.00 USD | 23,520.00 USD | 19,110.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,720.00 USD | 513,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.50` | 7,780,000.00 USD | 7,780,000.00 USD | 24,840.00 USD | 6,790.00 USD | 43,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.55` | 84,100.00 USD | 508,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.60` | 7,700,000.00 USD | 7,700,000.00 USD | 52,670.00 USD | 17,830.00 USD | 22,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.70` | 7,610,000.00 USD | 7,610,000.00 USD | 53,670.00 USD | 24,710.00 USD | 32,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.75` | 9,050.00 USD | 424,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.80` | 2,690,000.00 USD | 2,690,000.00 USD | 5,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.80` | 7,500,000.00 USD | 7,500,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.90` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 497.60 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.90` | 7,400,000.00 USD | 7,400,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.95` | 245.07 USD | 415,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.00` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 129.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.00` | 7,150,000.00 USD | 7,150,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.10` | 2,680,000.00 USD | 2,680,000.00 USD | 263.90 USD | 1,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.10` | 7,020,000.00 USD | 7,020,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.15` | 219,370.00 USD | 415,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.20` | 2,680,000.00 USD | 2,680,000.00 USD | 1,100.00 USD | 1,130.00 USD | 327.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.20` | 6,940,000.00 USD | 6,940,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.30` | 2,670,000.00 USD | 2,670,000.00 USD | 20,430.00 USD | 5,180.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.30` | 6,870,000.00 USD | 6,870,000.00 USD | 19,510.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.40` | 2,630,000.00 USD | 2,630,000.00 USD | 17,800.00 USD | 7,000.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.40` | 6,800,000.00 USD | 6,800,000.00 USD | 73,130.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.45` | 20,410.00 USD | 195,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.50` | 2,590,000.00 USD | 2,590,000.00 USD | 11,810.00 USD | 9,610.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.50` | 6,650,000.00 USD | 6,650,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.55` | 551.07 USD | 175,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.60` | 2,570,000.00 USD | 2,570,000.00 USD | 9,850.00 USD | 8,110.00 USD | 4,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.60` | 6,560,000.00 USD | 6,560,000.00 USD | 35,880.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.65` | 8,810.00 USD | 174,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.70` | 2,550,000.00 USD | 2,550,000.00 USD | 5,340.00 USD | 3,950.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.70` | 6,490,000.00 USD | 6,490,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.75` | 9,580.00 USD | 166,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.80` | 2,530,000.00 USD | 2,530,000.00 USD | 13,220.00 USD | 2,980.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.80` | 6,450,000.00 USD | 6,450,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.85` | 13,890.00 USD | 156,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.90` | 2,500,000.00 USD | 2,500,000.00 USD | 12,520.00 USD | 19,700.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.90` | 6,400,000.00 USD | 6,400,000.00 USD | 5,870.00 USD | 15,810.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.95` | 13,950.00 USD | 142,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.00` | 2,460,000.00 USD | 2,460,000.00 USD | 25,510.00 USD | 8,240.00 USD | 23,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.00` | 6,370,000.00 USD | 6,370,000.00 USD | 64,300.00 USD | 20,800.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.10` | 2,400,000.00 USD | 2,400,000.00 USD | 27,630.00 USD | 6,280.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 6,270,000.00 USD | 6,270,000.00 USD | 24,220.00 USD | 18,810.00 USD | 35,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.15` | 13,180.00 USD | 128,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.20` | 2,340,000.00 USD | 2,340,000.00 USD | 20,520.00 USD | 11,250.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 6,190,000.00 USD | 6,190,000.00 USD | 38,380.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.25` | 227.81 USD | 115,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.30` | 2,290,000.00 USD | 2,290,000.00 USD | 39,260.00 USD | 7,260.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 6,130,000.00 USD | 6,130,000.00 USD | 21,450.00 USD | 12,840.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.35` | 3,020.00 USD | 115,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.40` | 2,230,000.00 USD | 2,230,000.00 USD | 11,920.00 USD | 7,830.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 6,080,000.00 USD | 6,080,000.00 USD | 20,580.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.45` | 2,360.00 USD | 112,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.50` | 2,200,000.00 USD | 2,200,000.00 USD | 49,720.00 USD | 13,570.00 USD | 998.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.50` | 6,030,000.00 USD | 6,030,000.00 USD | 36,050.00 USD | 667.05 USD | 11,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.55` | 8,700.00 USD | 109,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.60` | 2,140,000.00 USD | 2,140,000.00 USD | 5,230.00 USD | 9,230.00 USD | 506.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.60` | 5,980,000.00 USD | 5,980,000.00 USD | 74,610.00 USD | 14,530.00 USD | 584.77 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.70` | 2,120,000.00 USD | 2,120,000.00 USD | 13,770.00 USD | 8,280.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.70` | 5,890,000.00 USD | 5,890,000.00 USD | 20,250.00 USD | 43,820.00 USD | 62,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.75` | 6,670.00 USD | 101,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.80` | 2,080,000.00 USD | 2,080,000.00 USD | 14,400.00 USD | 16,180.00 USD | 74,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.80` | 5,770,000.00 USD | 5,770,000.00 USD | 46,600.00 USD | 29,900.00 USD | 108.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.85` | 7,290.00 USD | 94,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.90` | 1,980,000.00 USD | 1,980,000.00 USD | 40,590.00 USD | 10,870.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.90` | 5,690,000.00 USD | 5,690,000.00 USD | 51,920.00 USD | 26,170.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.95` | 42,490.00 USD | 87,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.00` | 1,920,000.00 USD | 1,920,000.00 USD | 9,470.00 USD | 10,940.00 USD | 4,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.00` | 5,580,000.00 USD | 5,580,000.00 USD | 18,990.00 USD | 10,540.00 USD | 55,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.05` | 900.26 USD | 44,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.10` | 1,900,000.00 USD | 1,900,000.00 USD | 27,870.00 USD | 10,120.00 USD | 60,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.10` | 5,490,000.00 USD | 5,490,000.00 USD | 52,760.00 USD | 37,960.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.15` | 2,640.00 USD | 43,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.20` | 1,800,000.00 USD | 1,800,000.00 USD | 68,380.00 USD | 25,970.00 USD | 63,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.20` | 5,390,000.00 USD | 5,390,000.00 USD | 162,460.00 USD | 42,920.00 USD | 27,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.25` | 911.64 USD | 41,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.30` | 1,640,000.00 USD | 1,640,000.00 USD | 32,910.00 USD | 26,340.00 USD | 41,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.30` | 5,160,000.00 USD | 5,160,000.00 USD | 63,050.00 USD | 18,150.00 USD | 37,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.35` | 2,120.00 USD | 40,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.40` | 1,540,000.00 USD | 1,540,000.00 USD | 14,390.00 USD | 16,470.00 USD | 75,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.40` | 5,040,000.00 USD | 5,040,000.00 USD | 48,160.00 USD | 18,090.00 USD | 95,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.45` | 4,880.00 USD | 38,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.50` | 1,430,000.00 USD | 1,430,000.00 USD | 14,780.00 USD | 11,880.00 USD | 7,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.50` | 4,880,000.00 USD | 4,880,000.00 USD | 49,490.00 USD | 8,960.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.60` | 1,400,000.00 USD | 1,400,000.00 USD | 74,660.00 USD | 19,660.00 USD | 1,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.60` | 4,800,000.00 USD | 4,800,000.00 USD | 53,580.00 USD | 5,690.00 USD | 98,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.65` | 350.87 USD | 33,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.70` | 1,300,000.00 USD | 1,300,000.00 USD | 5,710.00 USD | 7,700.00 USD | 465.28 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.70` | 4,640,000.00 USD | 4,640,000.00 USD | 131,400.00 USD | 14,420.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.75` | 148.35 USD | 32,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.80` | 1,290,000.00 USD | 1,290,000.00 USD | 16,800.00 USD | 5,280.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.80` | 4,490,000.00 USD | 4,490,000.00 USD | 99,150.00 USD | 80,510.00 USD | 126,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.85` | 2,130.00 USD | 32,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.90` | 1,260,000.00 USD | 1,260,000.00 USD | 7,480.00 USD | 26,500.00 USD | 125,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.90` | 4,180,000.00 USD | 4,180,000.00 USD | 111,970.00 USD | 56,750.00 USD | 123,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.95` | 27,330.00 USD | 30,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.00` | 1,100,000.00 USD | 1,100,000.00 USD | 28,730.00 USD | 21,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.00` | 3,890,000.00 USD | 3,890,000.00 USD | 344,710.00 USD | 148,420.00 USD | 271,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.05` | 219.44 USD | 3,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.10` | 1,050,000.00 USD | 1,050,000.00 USD | 34,220.00 USD | 18,680.00 USD | 6,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.10` | 3,130,000.00 USD | 3,130,000.00 USD | 234,120.00 USD | 48,800.00 USD | 184,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.15` | 3,080.00 USD | 3,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `1D` | `Short Liquidation` | `55.90` | 344,790.00 USD | 344,790.00 USD | 137,200.00 USD | 2,990.00 USD | 140,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.90` | 930,900.00 USD | 930,900.00 USD | 141,330.00 USD | 65,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.00` | 544,060.00 USD | 544,060.00 USD | 139,840.00 USD | 0.00 USD | 59,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.00` | 1,360,000.00 USD | 1,360,000.00 USD | 181,230.00 USD | 98,600.00 USD | 147,270.00 USD | `Tier 1 CEX` |
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
| `Live` | `Short Liquidation` | `57.75` | 1,250.00 USD | 1,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `57.80` | 3,960,000.00 USD | 3,960,000.00 USD | 5,680.00 USD | 13,220.00 USD | 72,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.80` | 6,020,000.00 USD | 6,020,000.00 USD | 2,260.00 USD | 14,360.00 USD | 48,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.90` | 3,990,000.00 USD | 3,990,000.00 USD | 9,940.00 USD | 14,110.00 USD | 7,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.90` | 6,030,000.00 USD | 6,030,000.00 USD | 5,120.00 USD | 963.90 USD | 1,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.95` | 978.20 USD | 2,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.00` | 4,000,000.00 USD | 4,000,000.00 USD | 4,040.00 USD | 5,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.00` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 3,670.00 USD | 86,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.10` | 4,070,000.00 USD | 4,070,000.00 USD | 30,850.00 USD | 29,810.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.10` | 6,120,000.00 USD | 6,120,000.00 USD | 2,810.00 USD | 1,310.00 USD | 848.40 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `58.15` | 199,220.00 USD | 201,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.20` | 4,080,000.00 USD | 4,080,000.00 USD | 2,470.00 USD | 6,140.00 USD | 350.42 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `58.25` | 668.13 USD | 202,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.30` | 4,140,000.00 USD | 4,140,000.00 USD | 10,290.00 USD | 11,540.00 USD | 36,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.30` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 9,580.00 USD | 26,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.40` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 4,720.00 USD | 33,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.40` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 54,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.50` | 4,250,000.00 USD | 4,250,000.00 USD | 49,290.00 USD | 20,280.00 USD | 379.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.50` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.60` | 6,240,000.00 USD | 6,240,000.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.70` | 4,270,000.00 USD | 4,270,000.00 USD | 15,850.00 USD | 7,050.00 USD | 355.85 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.70` | 6,280,000.00 USD | 6,280,000.00 USD | 1,700.00 USD | 5,910.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `58.75` | 213.26 USD | 202,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `59.35` | 9,870.00 USD | 212,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.40` | 6,420,000.00 USD | 6,420,000.00 USD | 78,860.00 USD | 57,570.00 USD | 76,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.40` | 8,100,000.00 USD | 8,100,000.00 USD | 103,370.00 USD | 73,620.00 USD | 137,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.45` | 214.61 USD | 212,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `60.05` | 217.98 USD | 212,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `60.65` | 218.95 USD | 212,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.70` | 8,840,000.00 USD | 8,840,000.00 USD | 47,740.00 USD | 33,330.00 USD | 1,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.70` | 13,390,000.00 USD | 13,390,000.00 USD | 129,660.00 USD | 67,510.00 USD | 28,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.80` | 8,940,000.00 USD | 8,940,000.00 USD | 24,780.00 USD | 14,010.00 USD | 57,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.80` | 13,620,000.00 USD | 13,620,000.00 USD | 55,810.00 USD | 76,460.00 USD | 94,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.90` | 9,040,000.00 USD | 9,040,000.00 USD | 57,330.00 USD | 26,930.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.90` | 13,860,000.00 USD | 13,860,000.00 USD | 116,730.00 USD | 50,120.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.95` | 397.39 USD | 213,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.00` | 9,120,000.00 USD | 9,120,000.00 USD | 46,000.00 USD | 7,600.00 USD | 28,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 14,000,000.00 USD | 14,000,000.00 USD | 96,160.00 USD | 36,500.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.10` | 9,160,000.00 USD | 9,160,000.00 USD | 13,630.00 USD | 5,800.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 14,040,000.00 USD | 14,040,000.00 USD | 31,540.00 USD | 1,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.15` | 3,870.00 USD | 217,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `62.65` | 142.84 USD | 217,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `62.70` | 16,360,000.00 USD | 16,360,000.00 USD | 22,020.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.80` | 16,510,000.00 USD | 16,510,000.00 USD | 72,250.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.90` | 16,600,000.00 USD | 16,600,000.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `62.95` | 138.49 USD | 217,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `63.00` | 16,670,000.00 USD | 16,670,000.00 USD | 34,730.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.10` | 16,700,000.00 USD | 16,700,000.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.30` | 16,740,000.00 USD | 16,740,000.00 USD | 17,050.00 USD | 11,500.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.40` | 16,770,000.00 USD | 16,770,000.00 USD | 13,220.00 USD | 1,320.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `63.45` | 3,350.00 USD | 220,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `65.25` | 186.61 USD | 220,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `65.30` | 17,620,000.00 USD | 17,620,000.00 USD | 22,330.00 USD | 5,510.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `65.35` | 150.96 USD | 221,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.85` | 33,950.00 USD | 255,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.95` | 121.18 USD | 255,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.85` | 709.03 USD | 255,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `70.45` | 4,530.00 USD | 260,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `75.45` | 260.30 USD | 260,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `76.35` | 8,380.00 USD | 269,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.85` | 602.56 USD | 269,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.95` | 136.41 USD | 269,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `78.85` | 21,040.00 USD | 290,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `79.75` | 728.12 USD | 291,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.75` | 3,880.00 USD | 295,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.05` | 19,000.00 USD | 314,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.55` | 123.96 USD | 314,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.65` | 3,850.00 USD | 318,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.75` | 2,950.00 USD | 321,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `84.65` | 862.58 USD | 322,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `86.25` | 916.84 USD | 323,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `93.85` | 123.88 USD | 323,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.45` | 2,510.00 USD | 325,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.25` | 712.03 USD | 326,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.85` | 357,140.00 USD | 683,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.45` | 32,530.00 USD | 716,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.45` | 131.44 USD | 716,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.55` | 1,120.00 USD | 717,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.65` | 973.72 USD | 718,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.75` | 3,860.00 USD | 722,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `11.35` | 3,080,000.00 USD | 0.00 USD | 136.20 USD | `-79.12%` | `12.00` |
| `Live` | `Long` | `12.25` | 3,080,000.00 USD | 0.00 USD | 122.50 USD | `-77.47%` | `10.00` |
| `Live` | `Long` | `12.65` | 3,080,000.00 USD | 0.00 USD | 404.80 USD | `-76.73%` | `32.00` |
| `Live` | `Long` | `12.75` | 3,080,000.00 USD | 0.00 USD | 2,560.00 USD | `-76.55%` | `200.43` |
| `Live` | `Long` | `13.15` | 3,080,000.00 USD | 0.00 USD | 2,220.00 USD | `-75.81%` | `168.79` |
| `Live` | `Long` | `13.65` | 3,080,000.00 USD | 0.00 USD | 150.15 USD | `-74.89%` | `11.00` |
| `Live` | `Long` | `16.05` | 3,080,000.00 USD | 0.00 USD | 187.14 USD | `-70.48%` | `11.66` |
| `Live` | `Long` | `16.35` | 3,080,000.00 USD | 0.00 USD | 425.92 USD | `-69.93%` | `26.05` |
| `Live` | `Long` | `18.05` | 3,080,000.00 USD | 0.00 USD | 361.00 USD | `-66.80%` | `20.00` |
| `Live` | `Long` | `18.25` | 3,080,000.00 USD | 0.00 USD | 114.97 USD | `-66.43%` | `6.30` |
| `Live` | `Long` | `18.75` | 3,080,000.00 USD | 0.00 USD | 2,520.00 USD | `-65.51%` | `134.40` |
| `Live` | `Long` | `19.05` | 3,070,000.00 USD | 0.00 USD | 3,470.00 USD | `-64.96%` | `182.00` |
| `Live` | `Long` | `19.45` | 3,070,000.00 USD | 0.00 USD | 2,010.00 USD | `-64.22%` | `103.47` |
| `Live` | `Long` | `21.35` | 3,070,000.00 USD | 0.00 USD | 357.40 USD | `-60.73%` | `16.74` |
| `Live` | `Long` | `23.05` | 3,070,000.00 USD | 0.00 USD | 185.55 USD | `-57.60%` | `8.05` |
| `Live` | `Long` | `23.25` | 3,070,000.00 USD | 0.00 USD | 375.02 USD | `-57.24%` | `16.13` |
| `Live` | `Long` | `23.55` | 3,070,000.00 USD | 0.00 USD | 21,900.00 USD | `-56.68%` | `930.00` |
| `Live` | `Long` | `23.65` | 3,050,000.00 USD | 0.00 USD | 4,610.00 USD | `-56.50%` | `195.03` |
| `Live` | `Long` | `23.75` | 3,040,000.00 USD | 0.00 USD | 3,580.00 USD | `-56.32%` | `150.57` |
| `Live` | `Long` | `23.85` | 3,040,000.00 USD | 0.00 USD | 195.57 USD | `-56.13%` | `8.20` |
| `Live` | `Long` | `24.65` | 3,040,000.00 USD | 0.00 USD | 491.77 USD | `-54.66%` | `19.95` |
| `Live` | `Long` | `25.25` | 3,040,000.00 USD | 0.00 USD | 279,500.00 USD | `-53.56%` | `11,069.19` |
| `Live` | `Long` | `25.35` | 2,760,000.00 USD | 0.00 USD | 173.39 USD | `-53.37%` | `6.84` |
| `Live` | `Long` | `25.45` | 2,760,000.00 USD | 0.00 USD | 7,500.00 USD | `-53.19%` | `294.67` |
| `Live` | `Long` | `25.55` | 2,750,000.00 USD | 0.00 USD | 167,420.00 USD | `-53.00%` | `6,552.65` |
| `Live` | `Long` | `25.95` | 2,580,000.00 USD | 0.00 USD | 374.20 USD | `-52.27%` | `14.42` |
| `Live` | `Long` | `26.75` | 2,580,000.00 USD | 0.00 USD | 176.55 USD | `-50.80%` | `6.60` |
| `Live` | `Long` | `27.05` | 2,580,000.00 USD | 0.00 USD | 5,510.00 USD | `-50.25%` | `203.85` |
| `Live` | `Long` | `27.25` | 2,580,000.00 USD | 0.00 USD | 245.79 USD | `-49.88%` | `9.02` |
| `Live` | `Long` | `27.55` | 2,580,000.00 USD | 0.00 USD | 272.75 USD | `-49.33%` | `9.90` |
| `Live` | `Long` | `27.65` | 2,580,000.00 USD | 0.00 USD | 1,080.00 USD | `-49.14%` | `38.92` |
| `Live` | `Long` | `27.95` | 2,570,000.00 USD | 0.00 USD | 173.85 USD | `-48.59%` | `6.22` |
| `Live` | `Long` | `29.15` | 2,570,000.00 USD | 0.00 USD | 583.00 USD | `-46.38%` | `20.00` |
| `Live` | `Long` | `29.75` | 2,570,000.00 USD | 0.00 USD | 297,680.00 USD | `-45.28%` | `10,005.91` |
| `Live` | `Long` | `30.05` | 2,280,000.00 USD | 0.00 USD | 781.90 USD | `-44.73%` | `26.02` |
| `Live` | `Long` | `30.95` | 2,270,000.00 USD | 0.00 USD | 538.53 USD | `-43.07%` | `17.40` |
| `Live` | `Long` | `31.15` | 2,270,000.00 USD | 0.00 USD | 5,880.00 USD | `-42.70%` | `188.85` |
| `Live` | `Long` | `31.25` | 2,270,000.00 USD | 0.00 USD | 494.38 USD | `-42.52%` | `15.82` |
| `Live` | `Long` | `31.35` | 2,270,000.00 USD | 0.00 USD | 21,880.00 USD | `-42.34%` | `697.95` |
| `Live` | `Long` | `31.55` | 2,250,000.00 USD | 0.00 USD | 5,680.00 USD | `-41.97%` | `180.02` |
| `Live` | `Long` | `31.85` | 2,240,000.00 USD | 0.00 USD | 2,870.00 USD | `-41.42%` | `90.00` |
| `Live` | `Long` | `31.95` | 2,240,000.00 USD | 0.00 USD | 835.81 USD | `-41.23%` | `26.16` |
| `Live` | `Long` | `32.05` | 2,240,000.00 USD | 0.00 USD | 9,620.00 USD | `-41.05%` | `300.00` |
| `Live` | `Long` | `32.15` | 2,230,000.00 USD | 0.00 USD | 450.10 USD | `-40.86%` | `14.00` |
| `Live` | `Long` | `32.35` | 2,230,000.00 USD | 0.00 USD | 172.10 USD | `-40.50%` | `5.32` |
| `Live` | `Long` | `32.65` | 2,230,000.00 USD | 0.00 USD | 653.00 USD | `-39.95%` | `20.00` |
| `Live` | `Long` | `32.75` | 2,230,000.00 USD | 0.00 USD | 953.68 USD | `-39.76%` | `29.12` |
| `Live` | `Long` | `32.85` | 2,220,000.00 USD | 0.00 USD | 32,850.00 USD | `-39.58%` | `1,000.01` |
| `Live` | `Long` | `33.25` | 2,190,000.00 USD | 0.00 USD | 4,120.00 USD | `-38.84%` | `124.01` |
| `Live` | `Long` | `33.65` | 2,190,000.00 USD | 0.00 USD | 257.76 USD | `-38.11%` | `7.66` |
| `Live` | `Long` | `34.05` | 2,190,000.00 USD | 0.00 USD | 182.85 USD | `-37.37%` | `5.37` |
| `Live` | `Long` | `34.15` | 2,190,000.00 USD | 0.00 USD | 126.70 USD | `-37.19%` | `3.71` |
| `Live` | `Long` | `34.35` | 2,190,000.00 USD | 0.00 USD | 1,370.00 USD | `-36.82%` | `40.00` |
| `Live` | `Long` | `34.45` | 2,190,000.00 USD | 0.00 USD | 65,890.00 USD | `-36.63%` | `1,912.61` |
| `Live` | `Long` | `34.55` | 2,120,000.00 USD | 0.00 USD | 172.75 USD | `-36.45%` | `5.00` |
| `Live` | `Long` | `34.65` | 2,120,000.00 USD | 0.00 USD | 3,240.00 USD | `-36.27%` | `93.56` |
| `Live` | `Long` | `34.95` | 2,120,000.00 USD | 0.00 USD | 1,070.00 USD | `-35.71%` | `30.71` |
| `Live` | `Long` | `35.05` | 2,120,000.00 USD | 0.00 USD | 166.49 USD | `-35.53%` | `4.75` |
| `Live` | `Long` | `36.35` | 2,120,000.00 USD | 0.00 USD | 3,020.00 USD | `-33.14%` | `83.03` |
| `Live` | `Long` | `36.45` | 2,110,000.00 USD | 0.00 USD | 5,180.00 USD | `-32.96%` | `142.24` |
| `Live` | `Long` | `36.55` | 2,110,000.00 USD | 0.00 USD | 255.85 USD | `-32.77%` | `7.00` |
| `Live` | `Long` | `36.75` | 2,110,000.00 USD | 0.00 USD | 101.80 USD | `-32.40%` | `2.77` |
| `Live` | `Long` | `36.85` | 2,110,000.00 USD | 0.00 USD | 64,720.00 USD | `-32.22%` | `1,756.40` |
| `Live` | `Long` | `37.05` | 2,040,000.00 USD | 0.00 USD | 359.76 USD | `-31.85%` | `9.71` |
| `Live` | `Long` | `37.15` | 2,040,000.00 USD | 0.00 USD | 438.74 USD | `-31.67%` | `11.81` |
| `Live` | `Long` | `37.35` | 2,040,000.00 USD | 0.00 USD | 9,260.00 USD | `-31.30%` | `247.91` |
| `Live` | `Long` | `37.55` | 2,030,000.00 USD | 0.00 USD | 3,530.00 USD | `-30.93%` | `94.04` |
| `Live` | `Long` | `37.65` | 2,030,000.00 USD | 0.00 USD | 1,060.00 USD | `-30.75%` | `28.27` |
| `Live` | `Long` | `37.75` | 2,030,000.00 USD | 0.00 USD | 377.50 USD | `-30.56%` | `10.00` |
| `Live` | `Long` | `37.85` | 2,030,000.00 USD | 0.00 USD | 6,210.00 USD | `-30.38%` | `164.03` |
| `Live` | `Long` | `37.95` | 2,020,000.00 USD | 0.00 USD | 446.67 USD | `-30.20%` | `11.77` |
| `Live` | `Long` | `38.25` | 2,020,000.00 USD | 0.00 USD | 1,080.00 USD | `-29.64%` | `28.27` |
| `Live` | `Long` | `38.35` | 2,020,000.00 USD | 0.00 USD | 341.70 USD | `-29.46%` | `8.91` |
| `Live` | `Long` | `38.45` | 2,020,000.00 USD | 0.00 USD | 2,400.00 USD | `-29.28%` | `62.34` |
| `Live` | `Long` | `38.55` | 2,020,000.00 USD | 0.00 USD | 993.82 USD | `-29.09%` | `25.78` |
| `Live` | `Long` | `38.65` | 2,020,000.00 USD | 0.00 USD | 4,280.00 USD | `-28.91%` | `110.74` |
| `Live` | `Long` | `38.75` | 2,010,000.00 USD | 0.00 USD | 461.90 USD | `-28.73%` | `11.92` |
| `Live` | `Long` | `38.95` | 2,010,000.00 USD | 0.00 USD | 2,730.00 USD | `-28.36%` | `70.00` |
| `Live` | `Long` | `39.05` | 2,010,000.00 USD | 0.00 USD | 664,760.00 USD | `-28.17%` | `17,023.28` |
| `Live` | `Long` | `39.15` | 1,340,000.00 USD | 0.00 USD | 570.02 USD | `-27.99%` | `14.56` |
| `Live` | `Long` | `39.35` | 1,340,000.00 USD | 0.00 USD | 264.83 USD | `-27.62%` | `6.73` |
| `Live` | `Long` | `39.45` | 1,340,000.00 USD | 0.00 USD | 865.53 USD | `-27.44%` | `21.94` |
| `Live` | `Long` | `39.55` | 1,340,000.00 USD | 0.00 USD | 1,190.00 USD | `-27.25%` | `30.12` |
| `Live` | `Long` | `39.65` | 1,340,000.00 USD | 0.00 USD | 6,230.00 USD | `-27.07%` | `157.23` |
| `Live` | `Long` | `39.75` | 1,330,000.00 USD | 0.00 USD | 1,180.00 USD | `-26.89%` | `29.57` |
| `Live` | `Long` | `39.85` | 1,330,000.00 USD | 0.00 USD | 133.10 USD | `-26.70%` | `3.34` |
| `Live` | `Long` | `40.05` | 1,330,000.00 USD | 0.00 USD | 2,160.00 USD | `-26.33%` | `53.97` |
| `Live` | `Long` | `40.35` | 1,330,000.00 USD | 0.00 USD | 5,320.00 USD | `-25.78%` | `131.94` |
| `Live` | `Long` | `40.45` | 1,330,000.00 USD | 0.00 USD | 1,010.00 USD | `-25.60%` | `24.92` |
| `Live` | `Long` | `40.55` | 1,320,000.00 USD | 0.00 USD | 133.00 USD | `-25.41%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,320,000.00 USD | 0.00 USD | 274.39 USD | `-25.23%` | `6.75` |
| `Live` | `Long` | `40.75` | 1,320,000.00 USD | 0.00 USD | 319.07 USD | `-25.05%` | `7.83` |
| `Live` | `Long` | `40.85` | 1,320,000.00 USD | 0.00 USD | 6,340.00 USD | `-24.86%` | `155.23` |
| `Live` | `Long` | `40.95` | 1,320,000.00 USD | 0.00 USD | 509.01 USD | `-24.68%` | `12.43` |
| `Live` | `Long` | `41.05` | 1,320,000.00 USD | 0.00 USD | 396.54 USD | `-24.49%` | `9.66` |
| `Live` | `Long` | `41.25` | 1,320,000.00 USD | 0.00 USD | 14,490.00 USD | `-24.13%` | `351.26` |
| `Live` | `Long` | `41.45` | 1,300,000.00 USD | 0.00 USD | 644.96 USD | `-23.76%` | `15.56` |
| `Live` | `Long` | `42.05` | 1,300,000.00 USD | 0.00 USD | 982.29 USD | `-22.66%` | `23.36` |
| `Live` | `Long` | `42.15` | 1,300,000.00 USD | 0.00 USD | 69,270.00 USD | `-22.47%` | `1,643.33` |
| `Live` | `Long` | `42.25` | 1,230,000.00 USD | 0.00 USD | 35,410.00 USD | `-22.29%` | `838.00` |
| `Live` | `Long` | `42.35` | 1,200,000.00 USD | 0.00 USD | 9,320.00 USD | `-22.10%` | `220.00` |
| `Live` | `Long` | `42.65` | 1,190,000.00 USD | 0.00 USD | 1,570.00 USD | `-21.55%` | `36.70` |
| `Live` | `Long` | `42.85` | 1,180,000.00 USD | 0.00 USD | 5,800.00 USD | `-21.18%` | `135.38` |
| `Live` | `Long` | `42.95` | 1,180,000.00 USD | 0.00 USD | 2,000.00 USD | `-21.00%` | `46.65` |
| `Live` | `Long` | `43.05` | 1,180,000.00 USD | 0.00 USD | 9,080.00 USD | `-20.82%` | `211.00` |
| `Live` | `Long` | `43.15` | 1,170,000.00 USD | 0.00 USD | 122,400.00 USD | `-20.63%` | `2,836.59` |
| `Live` | `Long` | `43.25` | 1,050,000.00 USD | 0.00 USD | 417.80 USD | `-20.45%` | `9.66` |
| `Live` | `Long` | `43.35` | 1,050,000.00 USD | 0.00 USD | 5,390.00 USD | `-20.26%` | `124.24` |
| `Live` | `Long` | `43.45` | 1,040,000.00 USD | 0.00 USD | 980.67 USD | `-20.08%` | `22.57` |
| `Live` | `Long` | `43.65` | 1,040,000.00 USD | 0.00 USD | 26,650.00 USD | `-19.71%` | `610.44` |
| `Live` | `Long` | `43.75` | 1,010,000.00 USD | 0.00 USD | 21,880.00 USD | `-19.53%` | `500.00` |
| `Live` | `Long` | `43.85` | 990,310.00 USD | 0.00 USD | 801.14 USD | `-19.34%` | `18.27` |
| `Live` | `Long` | `44.15` | 989,510.00 USD | 0.00 USD | 2,380.00 USD | `-18.79%` | `53.99` |
| `Live` | `Long` | `44.35` | 987,130.00 USD | 0.00 USD | 84,440.00 USD | `-18.42%` | `1,903.87` |
| `Live` | `Long` | `44.55` | 902,690.00 USD | 0.00 USD | 7,250.00 USD | `-18.06%` | `162.80` |
| `Live` | `Long` | `44.75` | 895,440.00 USD | 0.00 USD | 4,230.00 USD | `-17.69%` | `94.55` |
| `Live` | `Long` | `44.85` | 891,210.00 USD | 0.00 USD | 668.27 USD | `-17.51%` | `14.90` |
| `Live` | `Long` | `44.95` | 890,540.00 USD | 0.00 USD | 3,960.00 USD | `-17.32%` | `88.18` |
| `Live` | `Long` | `45.05` | 886,570.00 USD | 0.00 USD | 4,830.00 USD | `-17.14%` | `107.31` |
| `Live` | `Long` | `45.15` | 881,740.00 USD | 0.00 USD | 9,040.00 USD | `-16.95%` | `200.13` |
| `Live` | `Long` | `45.25` | 872,700.00 USD | 0.00 USD | 7,050.00 USD | `-16.77%` | `155.80` |
| `Live` | `Long` | `45.35` | 865,650.00 USD | 0.00 USD | 2,180.00 USD | `-16.59%` | `48.02` |
| `Live` | `Long` | `45.45` | 863,480.00 USD | 0.00 USD | 23,940.00 USD | `-16.40%` | `526.65` |
| `Live` | `Long` | `45.55` | 839,540.00 USD | 0.00 USD | 12,060.00 USD | `-16.22%` | `264.81` |
| `Live` | `Long` | `46.05` | 827,480.00 USD | 0.00 USD | 706.41 USD | `-15.30%` | `15.34` |
| `Live` | `Long` | `46.15` | 826,770.00 USD | 0.00 USD | 5,940.00 USD | `-15.11%` | `128.71` |
| `Live` | `Long` | `46.25` | 820,830.00 USD | 0.00 USD | 842.21 USD | `-14.93%` | `18.21` |
| `Live` | `Long` | `46.35` | 819,990.00 USD | 0.00 USD | 9,610.00 USD | `-14.75%` | `207.43` |
| `Live` | `Long` | `46.55` | 810,380.00 USD | 0.00 USD | 24,670.00 USD | `-14.38%` | `529.90` |
| `Live` | `Long` | `46.65` | 785,710.00 USD | 0.00 USD | 3,980.00 USD | `-14.19%` | `85.41` |
| `Live` | `Long` | `46.85` | 781,720.00 USD | 0.00 USD | 358.40 USD | `-13.83%` | `7.65` |
| `Live` | `Long` | `46.95` | 781,370.00 USD | 0.00 USD | 158.22 USD | `-13.64%` | `3.37` |
| `Live` | `Long` | `47.15` | 781,210.00 USD | 0.00 USD | 49,130.00 USD | `-13.27%` | `1,042.07` |
| `Live` | `Long` | `47.25` | 732,070.00 USD | 0.00 USD | 1,220.00 USD | `-13.09%` | `25.84` |
| `Live` | `Long` | `47.35` | 730,850.00 USD | 0.00 USD | 43,340.00 USD | `-12.91%` | `915.41` |
| `Live` | `Long` | `47.45` | 687,510.00 USD | 0.00 USD | 5,100.00 USD | `-12.72%` | `107.38` |
| `Live` | `Long` | `47.55` | 682,410.00 USD | 0.00 USD | 1,770.00 USD | `-12.54%` | `37.28` |
| `Live` | `Long` | `47.75` | 680,640.00 USD | 0.00 USD | 47,750.00 USD | `-12.17%` | `1,000.00` |
| `Live` | `Long` | `47.85` | 632,890.00 USD | 0.00 USD | 358.88 USD | `-11.99%` | `7.50` |
| `Live` | `Long` | `48.05` | 632,530.00 USD | 0.00 USD | 1,340.00 USD | `-11.62%` | `27.93` |
| `Live` | `Long` | `48.15` | 631,190.00 USD | 0.00 USD | 7,200.00 USD | `-11.44%` | `149.52` |
| `Live` | `Long` | `48.25` | 623,990.00 USD | 0.00 USD | 525.44 USD | `-11.25%` | `10.89` |
| `Live` | `Long` | `48.55` | 623,460.00 USD | 0.00 USD | 2,560.00 USD | `-10.70%` | `52.70` |
| `Live` | `Long` | `48.65` | 620,910.00 USD | 0.00 USD | 273.90 USD | `-10.52%` | `5.63` |
| `Live` | `Long` | `48.75` | 620,630.00 USD | 0.00 USD | 8,360.00 USD | `-10.33%` | `171.43` |
| `Live` | `Long` | `48.95` | 612,280.00 USD | 0.00 USD | 252.58 USD | `-9.96%` | `5.16` |
| `Live` | `Long` | `49.05` | 612,020.00 USD | 0.00 USD | 1,580.00 USD | `-9.78%` | `32.25` |
| `Live` | `Long` | `49.15` | 610,440.00 USD | 0.00 USD | 5,740.00 USD | `-9.60%` | `116.83` |
| `Live` | `Long` | `49.25` | 604,700.00 USD | 0.00 USD | 18,950.00 USD | `-9.41%` | `384.69` |
| `Live` | `Long` | `49.35` | 585,750.00 USD | 0.00 USD | 30,090.00 USD | `-9.23%` | `609.81` |
| `Live` | `Long` | `49.45` | 555,660.00 USD | 0.00 USD | 419.34 USD | `-9.04%` | `8.48` |
| `Live` | `Long` | `49.55` | 555,240.00 USD | 0.00 USD | 18,010.00 USD | `-8.86%` | `363.57` |
| `Live` | `Long` | `49.65` | 537,220.00 USD | 0.00 USD | 73,260.00 USD | `-8.68%` | `1,475.52` |
| `Live` | `Long` | `49.75` | 463,960.00 USD | 0.00 USD | 1,580.00 USD | `-8.49%` | `31.67` |
| `Live` | `Long` | `49.95` | 462,390.00 USD | 0.00 USD | 19,920.00 USD | `-8.12%` | `398.70` |
| `Live` | `Long` | `50.05` | 442,470.00 USD | 0.00 USD | 3,760.00 USD | `-7.94%` | `75.22` |
| `Live` | `Long` | `50.25` | 438,710.00 USD | 0.00 USD | 102.51 USD | `-7.57%` | `2.04` |
| `Live` | `Long` | `50.35` | 438,610.00 USD | 0.00 USD | 1,140.00 USD | `-7.39%` | `22.67` |
| `Live` | `Long` | `50.45` | 437,470.00 USD | 0.00 USD | 4,720.00 USD | `-7.20%` | `93.64` |
| `Live` | `Long` | `50.55` | 432,740.00 USD | 0.00 USD | 84,100.00 USD | `-7.02%` | `1,663.61` |
| `Live` | `Long` | `50.65` | 348,650.00 USD | 0.00 USD | 730.88 USD | `-6.84%` | `14.43` |
| `Live` | `Long` | `50.75` | 347,910.00 USD | 0.00 USD | 9,050.00 USD | `-6.65%` | `178.28` |
| `Live` | `Long` | `50.95` | 338,870.00 USD | 0.00 USD | 431.55 USD | `-6.29%` | `8.47` |
| `Live` | `Long` | `51.15` | 338,440.00 USD | 0.00 USD | 219,370.00 USD | `-5.92%` | `4,288.79` |
| `Live` | `Long` | `51.25` | 119,060.00 USD | 0.00 USD | 202.44 USD | `-5.73%` | `3.95` |
| `Live` | `Long` | `51.35` | 118,860.00 USD | 0.00 USD | 453.93 USD | `-5.55%` | `8.84` |
| `Live` | `Long` | `51.45` | 118,410.00 USD | 0.00 USD | 20,890.00 USD | `-5.37%` | `406.12` |
| `Live` | `Long` | `51.55` | 97,510.00 USD | 0.00 USD | 551.07 USD | `-5.18%` | `10.69` |
| `Live` | `Long` | `51.65` | 96,960.00 USD | 0.00 USD | 8,810.00 USD | `-5.00%` | `170.51` |
| `Live` | `Long` | `51.75` | 88,150.00 USD | 0.00 USD | 6,480.00 USD | `-4.81%` | `125.17` |
| `Live` | `Long` | `51.85` | 81,680.00 USD | 0.00 USD | 13,890.00 USD | `-4.63%` | `267.97` |
| `Live` | `Long` | `51.95` | 67,780.00 USD | 0.00 USD | 13,950.00 USD | `-4.45%` | `268.48` |
| `Live` | `Long` | `52.15` | 53,840.00 USD | 0.00 USD | 1,900.00 USD | `-4.08%` | `36.36` |
| `Live` | `Long` | `52.25` | 51,940.00 USD | 0.00 USD | 2,990.00 USD | `-3.89%` | `57.13` |
| `Live` | `Long` | `52.35` | 48,950.00 USD | 0.00 USD | 1,860.00 USD | `-3.71%` | `35.55` |
| `Live` | `Long` | `52.45` | 47,090.00 USD | 0.00 USD | 2,360.00 USD | `-3.53%` | `44.95` |
| `Live` | `Long` | `52.55` | 44,740.00 USD | 0.00 USD | 8,700.00 USD | `-3.34%` | `165.49` |
| `Live` | `Long` | `52.75` | 36,040.00 USD | 0.00 USD | 4,240.00 USD | `-2.97%` | `80.44` |
| `Live` | `Long` | `52.85` | 31,800.00 USD | 0.00 USD | 5,950.00 USD | `-2.79%` | `112.64` |
| `Live` | `Long` | `52.95` | 25,840.00 USD | 0.00 USD | 25,840.00 USD | `-2.61%` | `488.06` |
| `Live` | `Short` | `55.85` | 1,150.00 USD | 1,150.00 USD | 0.00 USD | `+2.73%` | `20.63` |
| `Live` | `Short` | `55.95` | 1,920.00 USD | 770.99 USD | 0.00 USD | `+2.91%` | `13.78` |
| `Live` | `Short` | `56.05` | 3,500.00 USD | 1,570.00 USD | 0.00 USD | `+3.10%` | `28.08` |
| `Live` | `Short` | `56.75` | 5,590.00 USD | 2,100.00 USD | 0.00 USD | `+4.38%` | `36.96` |
| `Live` | `Short` | `56.85` | 9,360.00 USD | 3,770.00 USD | 0.00 USD | `+4.57%` | `66.25` |
| `Live` | `Short` | `57.15` | 9,510.00 USD | 146.88 USD | 0.00 USD | `+5.12%` | `2.57` |
| `Live` | `Short` | `57.95` | 9,630.00 USD | 125.75 USD | 0.00 USD | `+6.59%` | `2.17` |
| `Live` | `Short` | `58.05` | 209,970.00 USD | 200,340.00 USD | 0.00 USD | `+6.77%` | `3,451.13` |
| `Live` | `Short` | `59.35` | 219,410.00 USD | 9,440.00 USD | 0.00 USD | `+9.17%` | `159.09` |
| `Live` | `Short` | `60.95` | 219,810.00 USD | 397.39 USD | 0.00 USD | `+12.11%` | `6.52` |
| `Live` | `Short` | `61.15` | 223,680.00 USD | 3,870.00 USD | 0.00 USD | `+12.48%` | `63.26` |
| `Live` | `Short` | `62.95` | 223,820.00 USD | 138.49 USD | 0.00 USD | `+15.79%` | `2.20` |
| `Live` | `Short` | `63.45` | 227,170.00 USD | 3,350.00 USD | 0.00 USD | `+16.71%` | `52.83` |
| `Live` | `Short` | `66.45` | 271,180.00 USD | 44,010.00 USD | 0.00 USD | `+22.22%` | `662.35` |
| `Live` | `Short` | `66.65` | 276,580.00 USD | 5,400.00 USD | 0.00 USD | `+22.59%` | `81.01` |
| `Live` | `Short` | `66.95` | 276,700.00 USD | 121.18 USD | 0.00 USD | `+23.14%` | `1.81` |
| `Live` | `Short` | `67.85` | 277,410.00 USD | 709.03 USD | 0.00 USD | `+24.80%` | `10.45` |
| `Live` | `Short` | `73.35` | 277,670.00 USD | 253.06 USD | 0.00 USD | `+34.92%` | `3.45` |
| `Live` | `Short` | `76.35` | 286,050.00 USD | 8,380.00 USD | 0.00 USD | `+40.43%` | `109.80` |
| `Live` | `Short` | `77.85` | 286,650.00 USD | 602.56 USD | 0.00 USD | `+43.19%` | `7.74` |
| `Live` | `Short` | `77.95` | 286,790.00 USD | 136.41 USD | 0.00 USD | `+43.38%` | `1.75` |
| `Live` | `Short` | `79.75` | 289,980.00 USD | 3,190.00 USD | 0.00 USD | `+46.69%` | `40.00` |
| `Live` | `Short` | `80.75` | 290,620.00 USD | 646.00 USD | 0.00 USD | `+48.53%` | `8.00` |
| `Live` | `Short` | `80.85` | 312,200.00 USD | 21,570.00 USD | 0.00 USD | `+48.71%` | `266.81` |
| `Live` | `Short` | `81.05` | 331,200.00 USD | 19,000.00 USD | 0.00 USD | `+49.08%` | `234.42` |
| `Live` | `Short` | `81.55` | 331,320.00 USD | 123.96 USD | 0.00 USD | `+50.00%` | `1.52` |
| `Live` | `Short` | `82.75` | 331,530.00 USD | 214.32 USD | 0.00 USD | `+52.21%` | `2.59` |
| `Live` | `Short` | `82.95` | 334,270.00 USD | 2,740.00 USD | 0.00 USD | `+52.57%` | `33.00` |
| `Live` | `Short` | `83.65` | 338,170.00 USD | 3,900.00 USD | 0.00 USD | `+53.86%` | `46.61` |
| `Live` | `Short` | `86.75` | 339,090.00 USD | 922.15 USD | 0.00 USD | `+59.56%` | `10.63` |
| `Live` | `Short` | `98.65` | 339,220.00 USD | 130.22 USD | 0.00 USD | `+81.45%` | `1.32` |
| `Live` | `Short` | `100.15` | 341,730.00 USD | 2,500.00 USD | 0.00 USD | `+84.21%` | `25.00` |
| `Live` | `Short` | `102.75` | 342,660.00 USD | 931.94 USD | 0.00 USD | `+88.99%` | `9.07` |
| `Live` | `Short` | `104.25` | 342,870.00 USD | 213.71 USD | 0.00 USD | `+91.75%` | `2.05` |
| `Live` | `Short` | `105.15` | 697,650.00 USD | 354,780.00 USD | 0.00 USD | `+93.41%` | `3,374.01` |
| `Live` | `Short` | `106.35` | 698,370.00 USD | 726.37 USD | 0.00 USD | `+95.61%` | `6.83` |
| `Live` | `Short` | `106.75` | 699,990.00 USD | 1,620.00 USD | 0.00 USD | `+96.35%` | `15.16` |
| `Live` | `Short` | `106.85` | 701,860.00 USD | 1,860.00 USD | 0.00 USD | `+96.53%` | `17.43` |
| `Live` | `Short` | `107.15` | 702,060.00 USD | 199.30 USD | 0.00 USD | `+97.09%` | `1.86` |
| `Live` | `Short` | `108.05` | 708,530.00 USD | 6,470.00 USD | 0.00 USD | `+98.74%` | `59.91` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 417,670.00 USD | 0.00 USD | 392.18 USD | `-63.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 417,280.00 USD | 0.00 USD | 2,310.00 USD | `-59.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 414,980.00 USD | 0.00 USD | 806.86 USD | `-53.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 414,170.00 USD | 0.00 USD | 1,560.00 USD | `-53.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 412,610.00 USD | 0.00 USD | 410.25 USD | `-49.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 412,200.00 USD | 0.00 USD | 281.57 USD | `-44.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 411,920.00 USD | 0.00 USD | 36,050.00 USD | `-33.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 375,870.00 USD | 0.00 USD | 37,550.00 USD | `-30.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 338,320.00 USD | 0.00 USD | 447.01 USD | `-30.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.35` | 337,870.00 USD | 0.00 USD | 73,350.00 USD | `-29.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 264,520.00 USD | 0.00 USD | 40,560.00 USD | `-28.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 223,970.00 USD | 0.00 USD | 489.57 USD | `-27.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 223,480.00 USD | 0.00 USD | 1,180.00 USD | `-26.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 222,300.00 USD | 0.00 USD | 9,840.00 USD | `-26.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 212,460.00 USD | 0.00 USD | 2,060.00 USD | `-24.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 210,400.00 USD | 0.00 USD | 2,960.00 USD | `-23.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 207,450.00 USD | 0.00 USD | 4,010.00 USD | `-22.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.65` | 203,430.00 USD | 0.00 USD | 3,000.00 USD | `-21.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 200,430.00 USD | 0.00 USD | 5,680.00 USD | `-20.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 194,750.00 USD | 0.00 USD | 672.22 USD | `-19.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 194,080.00 USD | 0.00 USD | 213.80 USD | `-18.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 193,870.00 USD | 0.00 USD | 223.20 USD | `-18.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 193,640.00 USD | 0.00 USD | 391.13 USD | `-17.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 193,250.00 USD | 0.00 USD | 7,080.00 USD | `-17.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 186,170.00 USD | 0.00 USD | 1,370.00 USD | `-16.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 184,810.00 USD | 0.00 USD | 553.80 USD | `-15.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.45` | 184,250.00 USD | 0.00 USD | 3,080.00 USD | `-14.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 181,180.00 USD | 0.00 USD | 14,000.00 USD | `-14.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 167,180.00 USD | 0.00 USD | 158.56 USD | `-13.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 167,020.00 USD | 0.00 USD | 373.28 USD | `-13.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 166,650.00 USD | 0.00 USD | 849.46 USD | `-12.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 165,800.00 USD | 0.00 USD | 1,150.00 USD | `-11.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.15` | 164,650.00 USD | 0.00 USD | 303.35 USD | `-11.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 164,350.00 USD | 0.00 USD | 1,740.00 USD | `-10.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 162,610.00 USD | 0.00 USD | 981.00 USD | `-9.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.35` | 161,620.00 USD | 0.00 USD | 817.24 USD | `-9.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 160,810.00 USD | 0.00 USD | 237.85 USD | `-9.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.55` | 160,570.00 USD | 0.00 USD | 1,420.00 USD | `-8.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.85` | 159,150.00 USD | 0.00 USD | 108.17 USD | `-8.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 159,040.00 USD | 0.00 USD | 298.20 USD | `-8.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 158,750.00 USD | 0.00 USD | 14,650.00 USD | `-7.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 144,090.00 USD | 0.00 USD | 6,410.00 USD | `-7.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 137,680.00 USD | 0.00 USD | 459.70 USD | `-7.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 137,220.00 USD | 0.00 USD | 236.57 USD | `-7.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 136,980.00 USD | 0.00 USD | 1,020.00 USD | `-6.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 135,960.00 USD | 0.00 USD | 439.89 USD | `-5.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.45` | 135,520.00 USD | 0.00 USD | 1,060.00 USD | `-5.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 134,460.00 USD | 0.00 USD | 7,320.00 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.85` | 127,140.00 USD | 0.00 USD | 106.29 USD | `-4.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.95` | 127,040.00 USD | 0.00 USD | 8,700.00 USD | `-4.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 118,330.00 USD | 0.00 USD | 26,490.00 USD | `-4.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 91,850.00 USD | 0.00 USD | 51,800.00 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 40,050.00 USD | 0.00 USD | 10,720.00 USD | `-3.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 29,320.00 USD | 0.00 USD | 271.13 USD | `-2.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.85` | 29,050.00 USD | 0.00 USD | 135.82 USD | `-2.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 28,920.00 USD | 0.00 USD | 115.43 USD | `-2.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 28,800.00 USD | 0.00 USD | 12,330.00 USD | `-2.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 16,470.00 USD | 0.00 USD | 2,130.00 USD | `-2.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.25` | 14,340.00 USD | 0.00 USD | 881.82 USD | `-2.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 13,460.00 USD | 0.00 USD | 566.57 USD | `-1.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 12,890.00 USD | 0.00 USD | 5,950.00 USD | `-1.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 6,950.00 USD | 0.00 USD | 1,370.00 USD | `-1.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.75` | 5,580.00 USD | 0.00 USD | 1,120.00 USD | `-1.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 4,450.00 USD | 0.00 USD | 462.03 USD | `-0.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 3,990.00 USD | 0.00 USD | 746.97 USD | `-0.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 3,240.00 USD | 0.00 USD | 3,090.00 USD | `-0.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 156.53 USD | 0.00 USD | 156.53 USD | `-0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `54.45` | 144.29 USD | 144.29 USD | 0.00 USD | `+0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `54.55` | 1,840.00 USD | 1,690.00 USD | 0.00 USD | `+0.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `54.65` | 2,030.00 USD | 198.38 USD | 0.00 USD | `+0.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `54.75` | 2,230.00 USD | 198.74 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `54.85` | 35,510.00 USD | 33,280.00 USD | 0.00 USD | `+0.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `54.95` | 35,910.00 USD | 397.84 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.05` | 37,490.00 USD | 1,580.00 USD | 0.00 USD | `+1.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.15` | 37,890.00 USD | 398.18 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.25` | 38,280.00 USD | 398.90 USD | 0.00 USD | `+1.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.35` | 40,420.00 USD | 2,140.00 USD | 0.00 USD | `+1.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.55` | 40,580.00 USD | 156.65 USD | 0.00 USD | `+2.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.65` | 44,190.00 USD | 3,610.00 USD | 0.00 USD | `+2.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.75` | 44,390.00 USD | 202.37 USD | 0.00 USD | `+2.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.85` | 44,590.00 USD | 196.59 USD | 0.00 USD | `+2.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.95` | 44,780.00 USD | 193.03 USD | 0.00 USD | `+2.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.05` | 45,420.00 USD | 632.24 USD | 0.00 USD | `+3.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.15` | 45,610.00 USD | 193.72 USD | 0.00 USD | `+3.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.25` | 45,810.00 USD | 204.19 USD | 0.00 USD | `+3.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.35` | 46,200.00 USD | 387.12 USD | 0.00 USD | `+3.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.45` | 46,610.00 USD | 407.57 USD | 0.00 USD | `+3.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.55` | 49,250.00 USD | 2,640.00 USD | 0.00 USD | `+4.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.65` | 49,370.00 USD | 121.23 USD | 0.00 USD | `+4.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.75` | 49,600.00 USD | 228.70 USD | 0.00 USD | `+4.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.85` | 67,620.00 USD | 18,030.00 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.95` | 68,010.00 USD | 390.68 USD | 0.00 USD | `+4.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.05` | 73,820.00 USD | 5,800.00 USD | 0.00 USD | `+4.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.15` | 74,210.00 USD | 392.05 USD | 0.00 USD | `+5.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.25` | 74,410.00 USD | 201.52 USD | 0.00 USD | `+5.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.35` | 74,620.00 USD | 207.03 USD | 0.00 USD | `+5.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.45` | 74,960.00 USD | 344.70 USD | 0.00 USD | `+5.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.55` | 95,320.00 USD | 20,360.00 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.65` | 95,440.00 USD | 118.18 USD | 0.00 USD | `+6.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.75` | 95,560.00 USD | 119.54 USD | 0.00 USD | `+6.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.95` | 95,690.00 USD | 128.65 USD | 0.00 USD | `+6.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 96,440.00 USD | 747.68 USD | 0.00 USD | `+6.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 96,640.00 USD | 200.04 USD | 0.00 USD | `+6.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 96,840.00 USD | 200.96 USD | 0.00 USD | `+7.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 96,960.00 USD | 123.70 USD | 0.00 USD | `+7.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 97,560.00 USD | 601.45 USD | 0.00 USD | `+7.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 98,170.00 USD | 611.85 USD | 0.00 USD | `+7.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.65` | 98,450.00 USD | 274.48 USD | 0.00 USD | `+7.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 98,940.00 USD | 491.15 USD | 0.00 USD | `+8.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 101,880.00 USD | 2,940.00 USD | 0.00 USD | `+8.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 102,010.00 USD | 129.69 USD | 0.00 USD | `+8.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 106,810.00 USD | 4,800.00 USD | 0.00 USD | `+8.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 108,090.00 USD | 1,280.00 USD | 0.00 USD | `+8.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.25` | 108,300.00 USD | 210.34 USD | 0.00 USD | `+8.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 108,760.00 USD | 461.74 USD | 0.00 USD | `+9.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 108,920.00 USD | 159.92 USD | 0.00 USD | `+9.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.55` | 109,420.00 USD | 496.65 USD | 0.00 USD | `+9.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 110,140.00 USD | 724.75 USD | 0.00 USD | `+9.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.75` | 110,260.00 USD | 113.53 USD | 0.00 USD | `+9.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 110,420.00 USD | 158.00 USD | 0.00 USD | `+10.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 110,590.00 USD | 171.14 USD | 0.00 USD | `+10.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 111,140.00 USD | 551.00 USD | 0.00 USD | `+11.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.45` | 111,290.00 USD | 155.36 USD | 0.00 USD | `+11.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 112,170.00 USD | 878.58 USD | 0.00 USD | `+11.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 113,560.00 USD | 1,390.00 USD | 0.00 USD | `+11.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 114,540.00 USD | 986.99 USD | 0.00 USD | `+11.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 115,220.00 USD | 674.72 USD | 0.00 USD | `+12.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 117,580.00 USD | 2,360.00 USD | 0.00 USD | `+12.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 117,710.00 USD | 125.56 USD | 0.00 USD | `+12.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 121,300.00 USD | 3,600.00 USD | 0.00 USD | `+13.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 121,950.00 USD | 643.20 USD | 0.00 USD | `+13.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.95` | 124,070.00 USD | 2,120.00 USD | 0.00 USD | `+13.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 124,200.00 USD | 130.31 USD | 0.00 USD | `+14.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.55` | 124,540.00 USD | 347.15 USD | 0.00 USD | `+15.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 125,260.00 USD | 716.72 USD | 0.00 USD | `+15.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.75` | 125,400.00 USD | 141.19 USD | 0.00 USD | `+15.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 125,630.00 USD | 231.39 USD | 0.00 USD | `+15.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 126,140.00 USD | 508.36 USD | 0.00 USD | `+16.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 126,850.00 USD | 703.97 USD | 0.00 USD | `+16.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.35` | 126,990.00 USD | 140.64 USD | 0.00 USD | `+16.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 127,650.00 USD | 668.13 USD | 0.00 USD | `+16.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 132,860.00 USD | 5,210.00 USD | 0.00 USD | `+16.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 133,420.00 USD | 555.03 USD | 0.00 USD | `+17.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 133,950.00 USD | 531.62 USD | 0.00 USD | `+17.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.35` | 134,610.00 USD | 664.09 USD | 0.00 USD | `+18.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.45` | 135,280.00 USD | 665.12 USD | 0.00 USD | `+18.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 135,480.00 USD | 202.69 USD | 0.00 USD | `+18.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 135,780.00 USD | 298.04 USD | 0.00 USD | `+18.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 135,880.00 USD | 102.13 USD | 0.00 USD | `+19.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 136,420.00 USD | 540.09 USD | 0.00 USD | `+19.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 136,520.00 USD | 100.79 USD | 0.00 USD | `+20.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 136,780.00 USD | 262.20 USD | 0.00 USD | `+20.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 137,150.00 USD | 371.49 USD | 0.00 USD | `+20.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.85` | 138,040.00 USD | 881.07 USD | 0.00 USD | `+21.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 138,730.00 USD | 696.17 USD | 0.00 USD | `+21.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 139,270.00 USD | 534.00 USD | 0.00 USD | `+22.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 150,340.00 USD | 11,080.00 USD | 0.00 USD | `+23.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 163,750.00 USD | 13,410.00 USD | 0.00 USD | `+23.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.05` | 166,120.00 USD | 2,360.00 USD | 0.00 USD | `+25.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 170,980.00 USD | 4,860.00 USD | 0.00 USD | `+25.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 171,180.00 USD | 204.48 USD | 0.00 USD | `+27.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 171,990.00 USD | 810.02 USD | 0.00 USD | `+28.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 495,450.00 USD | 323,460.00 USD | 0.00 USD | `+28.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 495,620.00 USD | 170.04 USD | 0.00 USD | `+30.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 501,390.00 USD | 5,770.00 USD | 0.00 USD | `+30.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 501,660.00 USD | 269.28 USD | 0.00 USD | `+30.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 501,950.00 USD | 291.40 USD | 0.00 USD | `+32.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 509,520.00 USD | 7,580.00 USD | 0.00 USD | `+32.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 509,680.00 USD | 156.78 USD | 0.00 USD | `+32.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 512,900.00 USD | 3,220.00 USD | 0.00 USD | `+33.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 513,310.00 USD | 411.14 USD | 0.00 USD | `+35.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 636,500.00 USD | 123,190.00 USD | 0.00 USD | `+36.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 637,520.00 USD | 1,020.00 USD | 0.00 USD | `+37.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.75` | 638,330.00 USD | 811.04 USD | 0.00 USD | `+37.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 638,440.00 USD | 104.93 USD | 0.00 USD | `+37.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 638,570.00 USD | 133.59 USD | 0.00 USD | `+38.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 638,970.00 USD | 402.59 USD | 0.00 USD | `+38.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.85` | 639,280.00 USD | 308.71 USD | 0.00 USD | `+39.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 639,600.00 USD | 315.18 USD | 0.00 USD | `+42.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 698,900.00 USD | 59,310.00 USD | 0.00 USD | `+44.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 702,070.00 USD | 3,160.00 USD | 0.00 USD | `+45.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.35` | 707,320.00 USD | 5,260.00 USD | 0.00 USD | `+45.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 713,010.00 USD | 5,690.00 USD | 0.00 USD | `+46.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 749,600.00 USD | 36,590.00 USD | 0.00 USD | `+47.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 750,040.00 USD | 433.89 USD | 0.00 USD | `+48.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 750,210.00 USD | 172.64 USD | 0.00 USD | `+49.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 750,370.00 USD | 164.10 USD | 0.00 USD | `+50.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 750,920.00 USD | 546.81 USD | 0.00 USD | `+52.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 753,220.00 USD | 2,300.00 USD | 0.00 USD | `+54.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 765,290.00 USD | 12,070.00 USD | 0.00 USD | `+56.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.05` | 785,530.00 USD | 20,230.00 USD | 0.00 USD | `+60.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 787,100.00 USD | 1,580.00 USD | 0.00 USD | `+61.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 824,110.00 USD | 37,000.00 USD | 0.00 USD | `+61.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 824,580.00 USD | 473.21 USD | 0.00 USD | `+63.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 825,000.00 USD | 422.99 USD | 0.00 USD | `+63.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 826,640.00 USD | 1,630.00 USD | 0.00 USD | `+64.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 831,510.00 USD | 4,870.00 USD | 0.00 USD | `+65.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 831,990.00 USD | 481.55 USD | 0.00 USD | `+68.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 833,320.00 USD | 1,330.00 USD | 0.00 USD | `+69.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 833,510.00 USD | 188.10 USD | 0.00 USD | `+72.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,100,000.00 USD | 266,140.00 USD | 0.00 USD | `+74.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,100,000.00 USD | 3,400.00 USD | 0.00 USD | `+75.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,120,000.00 USD | 21,930.00 USD | 0.00 USD | `+76.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,130,000.00 USD | 294.15 USD | 0.00 USD | `+80.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 1,140,000.00 USD | 15,380.00 USD | 0.00 USD | `+82.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,140,000.00 USD | 3,660.00 USD | 0.00 USD | `+84.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,140,000.00 USD | 306.15 USD | 0.00 USD | `+87.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,150,000.00 USD | 936.72 USD | 0.00 USD | `+89.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,150,000.00 USD | 2,920.00 USD | 0.00 USD | `+89.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,150,000.00 USD | 324.15 USD | 0.00 USD | `+98.74%` | `TACTICAL (Retail Cluster)` |

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
| `15M` | `LTC` | `44.00%` | `56.00%` | `0.79` | 4,390,000.00 USD |
| `15M` | `Binance` | `54%` | `46%` | `1.17` | 1,450,000.00 USD |
| `15M` | `OKX` | `36.85%` | `63.15%` | `0.58` | 178,340.00 USD |
| `15M` | `Bybit` | `56.95%` | `43.05%` | `1.32` | 221,420.00 USD |
| `15M` | `KuCoin` | `67.34%` | `32.66%` | `2.06` | 45,010.00 USD |
| `15M` | `Gate` | `32.11%` | `67.89%` | `0.47` | 76,170.00 USD |
| `15M` | `Bitget` | `49.66%` | `50.34%` | `0.99` | 50,600.00 USD |
| `15M` | `BingX` | `27.91%` | `72.09%` | `0.39` | 1,190,000.00 USD |
| `15M` | `MEXC` | `44.18%` | `55.82%` | `0.79` | 221,050.00 USD |
| `15M` | `Bitunix` | `42.4%` | `57.6%` | `0.74` | 88,900.00 USD |
| `15M` | `Hyperliquid` | `79.58%` | `20.42%` | `3.90` | 73,020.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `44.4%` | `55.6%` | `0.80` | 698,240.00 USD |
| `15M` | `Crypto.com` | `1.66%` | `98.34%` | `0.02` | 3,240.00 USD |
| `15M` | `WhiteBIT` | `10.14%` | `89.86%` | `0.11` | 41,890.00 USD |
| `15M` | `HTX` | `66.7%` | `33.3%` | `2.00` | 2,160.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `75.44%` | `24.56%` | `3.07` | 41,950.00 USD |
| `15M` | `Aster` | `14.65%` | `85.35%` | `0.17` | 335.48 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `56.02%` | `43.98%` | `1.27` | 8,930.00 USD |
| `15M` | `Whale Positions` | `54%` | `46%` | `1.17` | 1,450,000.00 USD |
| `15M` | `Global Accounts` | `44.00%` | `56.00%` | `0.79` | 4,390,000.00 USD |
| `1H` | `LTC` | `51.75%` | `48.25%` | `1.07` | 49,890,000.00 USD |
| `1H` | `Binance` | `48.89%` | `51.11%` | `0.96` | 19,080,000.00 USD |
| `1H` | `OKX` | `57.43%` | `42.57%` | `1.35` | 5,040,000.00 USD |
| `1H` | `Bybit` | `52.43%` | `47.57%` | `1.10` | 4,080,000.00 USD |
| `1H` | `KuCoin` | `52.26%` | `47.74%` | `1.09` | 228,060.00 USD |
| `1H` | `Gate` | `44.92%` | `55.08%` | `0.82` | 1,220,000.00 USD |
| `1H` | `Bitget` | `67.13%` | `32.87%` | `2.04` | 1,970,000.00 USD |
| `1H` | `BingX` | `45.54%` | `54.46%` | `0.84` | 594,720.00 USD |
| `1H` | `MEXC` | `52.76%` | `47.24%` | `1.12` | 13,070,000.00 USD |
| `1H` | `Bitunix` | `44.96%` | `55.04%` | `0.82` | 1,550,000.00 USD |
| `1H` | `Hyperliquid` | `45.49%` | `54.51%` | `0.83` | 1,080,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.31%` | `50.69%` | `0.97` | 1,120,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `78.89%` | `21.11%` | `3.74` | 190,740.00 USD |
| `1H` | `HTX` | `44.26%` | `55.74%` | `0.79` | 11,410.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `72.04%` | `27.96%` | `2.58` | 489,150.00 USD |
| `1H` | `Aster` | `65.52%` | `34.48%` | `1.90` | 50,670.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `20.72%` | `79.28%` | `0.26` | 128,500.00 USD |
| `1H` | `Whale Positions` | `48.89%` | `51.11%` | `0.96` | 19,080,000.00 USD |
| `1H` | `Global Accounts` | `51.75%` | `48.25%` | `1.07` | 49,890,000.00 USD |
| `4H` | `LTC` | `47.27%` | `52.73%` | `0.90` | 392,940,000.00 USD |
| `4H` | `Binance` | `46.96%` | `53.04%` | `0.89` | 155,980,000.00 USD |
| `4H` | `OKX` | `48.44%` | `51.56%` | `0.94` | 34,230,000.00 USD |
| `4H` | `Bybit` | `47.89%` | `52.11%` | `0.92` | 38,040,000.00 USD |
| `4H` | `KuCoin` | `41.64%` | `58.36%` | `0.71` | 2,370,000.00 USD |
| `4H` | `Gate` | `48.86%` | `51.14%` | `0.96` | 8,330,000.00 USD |
| `4H` | `Bitget` | `50.13%` | `49.87%` | `1.01` | 16,120,000.00 USD |
| `4H` | `BingX` | `42.26%` | `57.74%` | `0.73` | 7,760,000.00 USD |
| `4H` | `MEXC` | `49.38%` | `50.62%` | `0.98` | 73,710,000.00 USD |
| `4H` | `Bitunix` | `42.28%` | `57.72%` | `0.73` | 14,740,000.00 USD |
| `4H` | `Hyperliquid` | `36.71%` | `63.29%` | `0.58` | 23,530,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49%` | `51%` | `0.96` | 7,580,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `78.34%` | `21.66%` | `3.62` | 3,790,000.00 USD |
| `4H` | `HTX` | `41.9%` | `58.1%` | `0.72` | 154,070.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `53.43%` | `46.57%` | `1.15` | 3,840,000.00 USD |
| `4H` | `Aster` | `42.37%` | `57.63%` | `0.74` | 1,050,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `45.57%` | `54.43%` | `0.84` | 1,730,000.00 USD |
| `4H` | `Whale Positions` | `46.96%` | `53.04%` | `0.89` | 155,980,000.00 USD |
| `4H` | `Global Accounts` | `47.27%` | `52.73%` | `0.90` | 392,940,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `55.36` | `55.27` | `55.36` | `55.50` | `55.06` | 745,324.85 USD | 359,100.57 USD | 386,224.28 USD | -27,123.71 USD | `-3.64%` | `3B / 8S` |
| `5:00 UTC` | `54.95` | `55.00` | `54.95` | `55.16` | `54.84` | 1,116,493.17 USD | 544,065.41 USD | 572,427.76 USD | -28,362.36 USD | `-2.54%` | `1B / 2S` |
| `0:00 UTC` | `54.78` | `54.81` | `54.78` | `55.03` | `54.59` | 2,311,809.84 USD | 1,167,618.18 USD | 1,144,191.66 USD | 23,426.51 USD | `+1.01%` | `4B / 7S` |
| `5:00 UTC` | `52.92` | `53.63` | `52.92` | `54.96` | `52.78` | 9,644,230.66 USD | 4,219,507.37 USD | 5,424,723.28 USD | -1,205,215.91 USD | `-12.50%` | `3B / 25S` |
| `0:00 UTC` | `53.92` | `53.53` | `53.92` | `53.97` | `53.03` | 2,679,572.06 USD | 1,410,180.46 USD | 1,269,391.60 USD | 140,788.86 USD | `+5.25%` | `16B / 8S` |
| `5:00 UTC` | `54.28` | `54.12` | `54.28` | `54.38` | `53.70` | 1,241,557.04 USD | 584,397.22 USD | 657,159.82 USD | -72,762.60 USD | `-5.86%` | `12B / 6S` |
| `0:00 UTC` | `54.30` | `54.36` | `54.30` | `54.62` | `54.16` | 1,483,061.64 USD | 620,330.38 USD | 862,731.26 USD | -242,400.88 USD | `-16.34%` | `4B / 6S` |
| `5:00 UTC` | `54.11` | `54.23` | `54.11` | `54.50` | `54.03` | 1,110,276.34 USD | 501,463.73 USD | 608,812.62 USD | -107,348.89 USD | `-9.67%` | `2B / 8S` |
| `0:00 UTC` | `53.86` | `54.08` | `53.86` | `54.55` | `53.64` | 1,780,531.79 USD | 1,005,907.66 USD | 774,624.13 USD | 231,283.53 USD | `+12.99%` | `11B / 6S` |
| `5:00 UTC` | `54.25` | `54.25` | `54.25` | `54.41` | `54.11` | 481,365.25 USD | 206,412.75 USD | 274,952.50 USD | -68,539.75 USD | `-14.24%` | `0B / 6S` |

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
| `5m` | -16,310.00 USD | 75,230.00 USD | **`ACCUMULATION`** |
| `15m` | -65,820.00 USD | 68,180.00 USD | **`ACCUMULATION`** |
| `30m` | -52,180.00 USD | 253,120.00 USD | **`ACCUMULATION`** |
| `1h` | -94,740.00 USD | -189,910.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,140,000.00 USD | -1,840,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -437,260.00 USD | -2,300,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -2,410,000.00 USD | -6,040,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,140,000.00 USD | -5,990,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -436,050.00 USD | -5,460,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -429,720.00 USD | -6,280,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 3,110,000.00 USD | -25,540,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -23,540,000.00 USD | -194,590,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-16.31K` | 15m=`-65.82K` | 1h=`-94.74K` | 24h=`-429.72K`
* Futures Capital Netflows: 5m=`+75.23K` | 15m=`+68.18K` | 1h=`-189.91K` | 24h=`-6.28M`
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
  * `2026-10-30 05:01:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:15:10 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:01:10 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:02:10 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `54.12` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `52.94` (Risk Distance: `1.19` pts)
  * +2.5R Take Profit: `57.09`
  * Mathematical Lot Sizing: **`8.42 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `55.86` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `57.04` (Risk Distance: `1.19` pts)
  * +2.5R Take Profit: `52.89`
  * Mathematical Lot Sizing: **`8.42 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`54.59`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
