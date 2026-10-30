# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 11:44:30 IST` (`2026-10-30 06:14:30 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `56.01` | **Live Ask Quote**: `56.30` | **Mid Price**: `56.16`
- **Spread Points**: `300.00` | **Spread BPS**: `53.42 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `54.54` | VWAP Z-Score: `+1.48` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.4111` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `56.01` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `57.26` | Lower -3.00σ Band: `51.82`
  * Upper +2.51σ Band: `56.81` | Lower -2.51σ Band: `52.27`
  * Upper +2.01σ Band: `56.36` | Lower -2.01σ Band: `52.72`
  * Upper +2.00σ Band: `56.35` | Lower -2.00σ Band: `52.73`
  * Upper +1.28σ Band: `55.70` | Lower -1.28σ Band: `53.38`
  * Upper +1.00σ Band: `55.45` | Lower -1.00σ Band: `53.64`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`55.83` | EMA-20=`55.54` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`55.77` (Slope: `+0.0000`) | EMA-100=`56.35`
  * Institutional Anchors: EMA-144=`56.60` | EMA-200=`56.68` (Slope: `-0.1940`) | EMA-233=`56.73`
- **Range Boundaries**: 24H High=`58.72` | 24H Low=`52.64` | Weekly High=`59.62` | Weekly Low=`52.64`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `56.18` (Distance: `-0.11%`)
  * Point of Control (POC) = `55.27` (Distance: `+1.53%`)
  * Value Area Low (VAL) = `54.32` (Distance: `+3.31%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.40` | POC=`57.72` | VAL=`56.83`
  * Prior Day Extremes: PDH=`59.52` | PDL=`54.18` | PDC=`54.46`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`58.29` | Weekly POC=`56.43` | Weekly VAL=`55.87`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`56.03` | Low=`52.64`
  * London Session (08:00-16:00 UTC): High=`56.22` | Low=`55.73`
  * New York Session (13:00-21:00 UTC): High=`56.49` | Low=`55.82`
  * Initial Balance (First Hour): IB High=`56.22` | IB Low=`55.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `55.93` - `56.38`
  * Optimal Trade Entry (OTE 0.705): `56.27`
  * Structural Invalidation Anchor (0.786): `56.60`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `56.13` | `56.21` | `55.97` | `56.02` | `5,098` | 285,881.50 USD | -36,358.99 USD | `-12.72%` | -4,615,206.38 USD | `-0.75` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `56.02` | `56.16` | `55.99` | `56.04` | `5,340` | 299,527.44 USD | 62,641.64 USD | `+20.91%` | -4,552,564.74 USD | `+1.72` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `56.05` | `56.28` | `56.04` | `56.21` | `5,154` | 289,618.92 USD | 31,770.61 USD | `+10.97%` | -4,520,794.13 USD | `+0.85` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `56.38` | `56.46` | `56.25` | `56.32` | `17,533` | 988,298.96 USD | -47,103.33 USD | `-4.77%` | -4,545,144.07 USD | `+0.23` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `56.33` | `56.44` | `56.08` | `56.12` | `13,091` | 737,190.46 USD | -33,703.31 USD | `-4.57%` | -4,578,847.39 USD | `+0.32` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `56.13` | `56.28` | `55.97` | `56.21` | `15,593` | 875,027.85 USD | 58,053.25 USD | `+6.63%` | -4,520,794.13 USD | `+0.97` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `56.25` | `56.29` | `55.73` | `55.98` | `57,057` | 3,198,717.26 USD | -379,690.29 USD | `-11.87%` | -4,669,597.06 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `55.99` | `56.46` | `55.98` | `56.12` | `50,953` | 2,868,373.53 USD | -16,856.34 USD | `-0.59%` | -4,686,453.41 USD | `+0.31` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `56.13` | `56.28` | `55.97` | `56.21` | `15,593` | 875,027.85 USD | 58,053.25 USD | `+6.63%` | -4,628,400.15 USD | `+0.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,423,359.63 USD | `-1.73` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -4,601,875.81 USD | `-0.83` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.46` | `55.73` | `56.21` | `123,602` | 6,942,118.65 USD | -338,493.38 USD | `-4.88%` | -4,940,369.19 USD | `+0.35` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | 701,394.73 USD | `-1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | 840,681.28 USD | `-1.08` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,423,359.63 USD | `-1.73` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -4,601,875.81 USD | `-0.83` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.46` | `55.73` | `56.21` | `123,602` | 6,942,118.65 USD | -338,493.38 USD | `-4.88%` | -4,940,369.19 USD | `+0.35` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`56.16`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:43:56 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1064` | `0xeadc...9d55` | `LONG` | 2,043,057.74 USD | `36,463.77` | `52.78` | `56.03` | `0.000000` | 118,381.79 USD | `+5.79%` | `10X Cross` |
| `1077` | `0x9aa5...58af` | `SHORT` | 2,025,984.58 USD | `36,177.65` | `71.22` | `56.03` | `303.42` | 550,502.09 USD | `+27.17%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `57.30` | 7,509.61 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 57.2990 USD [API] | `2026-10-29 03:24:56` |
| `ANNOUNCEMENT` | `INFO` | `57.33` | 7,509.53 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 7.51K USD at 57.3290 USD [API] | `2026-10-29 03:35:48` |
| `ANNOUNCEMENT` | `INFO` | `57.20` | 6,036.00 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 6.04K USD at 57.1970 USD [API] | `2026-10-29 03:58:49` |
| `ANNOUNCEMENT` | `INFO` | `51.38` | 63.20 USD | `-` | `NEWS_INTEL` | `-` | #LTC Liquidated Short: 0.06K USD at 51.3800 USD [API] | `2026-05-28 03:18:06` |
| `ANNOUNCEMENT` | `INFO` | `51.38` | 192.68 USD | `-` | `NEWS_INTEL` | `-` | #LTC Liquidated Short: 0.19K USD at 51.3800 USD [API] | `2026-05-28 03:18:06` |
| `ANNOUNCEMENT` | `INFO` | `57.15` | 7,508.68 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 57.1480 USD [API] | `2026-10-29 08:12:16` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`56.49` (Vol: 204,200.00 USD, Dist: `+0.27%`) | Long MP=`54.13` (Vol: 113,000.00 USD, Dist: `--3.92%`)
  * 48H Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+4.72%`) | Long MP=`54.12` (Vol: 113,000.00 USD, Dist: `--3.95%`)
  * 3D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+4.72%`) | Long MP=`54.12` (Vol: 113,000.00 USD, Dist: `--3.95%`)
  * 7D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+4.72%`) | Long MP=`54.12` (Vol: 113,000.00 USD, Dist: `--3.95%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `11.35` | 136.20 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.25` | 122.50 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.75` | 2,560.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.15` | 2,220.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.65` | 150.15 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `15.75` | 2,370.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `16.65` | 370.30 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `17.15` | 128.11 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `17.45` | 140.47 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `17.85` | 2,140.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.25` | 164.61 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.05` | 3,470.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.45` | 2,010.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.95` | 18,550.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.25` | 133.65 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.75` | 4,050.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.15` | 1,330.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.45` | 362.12 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.55` | 466.56 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.35` | 990.74 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.45` | 370.98 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.65` | 920.46 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.85` | 195.57 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.55` | 7,230.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.65` | 113,020.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 277,980.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 173.39 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.45` | 7,640.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 50,740.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 374.20 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.05` | 721.85 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.05` | 5,510.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 435.57 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 173.85 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 583.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 297,500.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 218.46 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 725.56 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.65` | 1,750.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 538.53 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 27,620.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 1,060.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.65` | 7,340.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 2,870.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 125.24 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 450.10 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.25` | 4,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.35` | 172.10 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.45` | 405.30 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 653.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 953.68 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 32,850.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.05` | 5,760.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 257.76 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.75` | 402.30 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.95` | 4,430.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 182.85 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 126.70 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.45` | 65,890.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 3,240.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 104.85 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 440.93 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.95` | 275.74 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 3,020.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 1,690.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.55` | 1,830.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 101.80 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 1,050.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 438.74 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 9,260.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 3,530.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 377.50 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 6,210.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 446.67 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.25` | 695.38 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 847.54 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 2,400.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 993.82 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 4,280.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 3,700.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 664,760.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 570.02 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 264.83 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 716.41 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 312.44 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 5,900.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 1,180.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 133.10 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 2,160.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.35` | 8,880.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 1,010.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 133.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 274.39 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 6,340.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 5,910.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 396.54 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 17,770.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 940.50 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.75` | 313.12 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.85` | 5,390.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 982.29 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 108,450.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 35,410.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.45` | 3,850.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 1,570.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 5,800.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 2,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 9,080.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 122,400.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 417.80 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 5,390.00 USD | 999,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 710.84 USD | 994,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 426.02 USD | 993,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 21,880.00 USD | 993,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 801.14 USD | 971,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 2,380.00 USD | 970,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 1,330.00 USD | 968,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 85,770.00 USD | 967,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 842.44 USD | 881,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 4,230.00 USD | 880,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 134.55 USD | 876,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 2,620.00 USD | 876,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 4,830.00 USD | 873,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 8,710.00 USD | 868,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 3,180.00 USD | 859,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 2,180.00 USD | 856,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 23,940.00 USD | 854,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 12,060.00 USD | 830,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 42,180.00 USD | 818,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.75` | 27,480.00 USD | 776,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.85` | 176.06 USD | 748,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 2,940.00 USD | 748,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 706.41 USD | 745,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.25` | 22,380.00 USD | 745,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.35` | 383.78 USD | 722,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 2,140.00 USD | 722,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 3,980.00 USD | 720,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.75` | 269.28 USD | 716,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 358.40 USD | 715,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 533.35 USD | 715,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.10` | 9,260,000.00 USD | 9,260,000.00 USD | 16,740.00 USD | 12,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.15` | 1,980.00 USD | 715,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.20` | 9,230,000.00 USD | 9,230,000.00 USD | 8,940.00 USD | 1,090.00 USD | 114.09 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.25` | 646.85 USD | 713,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.30` | 9,220,000.00 USD | 9,220,000.00 USD | 692.33 USD | 4,740.00 USD | 6,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.35` | 43,920.00 USD | 712,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.40` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 1,520.00 USD | 28,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.45` | 2,590.00 USD | 668,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.50` | 9,170,000.00 USD | 9,170,000.00 USD | 11,830.00 USD | 0.00 USD | 7,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.55` | 4,450.00 USD | 665,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 47,750.00 USD | 661,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.95` | 7,890.00 USD | 613,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 1,340.00 USD | 605,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.10` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.15` | 1,690.00 USD | 604,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.20` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.25` | 110.49 USD | 602,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.40` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 6,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.55` | 2,560.00 USD | 602,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.60` | 9,140,000.00 USD | 9,140,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.65` | 273.90 USD | 600,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 2,220.00 USD | 599,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.80` | 9,130,000.00 USD | 9,130,000.00 USD | 1,780.00 USD | 2,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `48.90` | 9,130,000.00 USD | 9,130,000.00 USD | 0.00 USD | 0.00 USD | 960.40 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.95` | 252.58 USD | 597,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,580.00 USD | 597,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,740.00 USD | 595,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.30` | 9,130,000.00 USD | 9,130,000.00 USD | 15,190.00 USD | 4,490.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.35` | 5,230.00 USD | 590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.40` | 9,090,000.00 USD | 9,090,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.45` | 419.34 USD | 584,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.50` | 9,090,000.00 USD | 9,090,000.00 USD | 2,830.00 USD | 7,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.55` | 18,010.00 USD | 584,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.60` | 9,080,000.00 USD | 9,080,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.65` | 73,260.00 USD | 566,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.70` | 9,060,000.00 USD | 9,060,000.00 USD | 12,090.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.75` | 20,710.00 USD | 493,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.80` | 9,040,000.00 USD | 9,040,000.00 USD | 9,930.00 USD | 8,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.90` | 9,030,000.00 USD | 9,030,000.00 USD | 45,030.00 USD | 7,170.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.95` | 19,920.00 USD | 472,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.00` | 8,970,000.00 USD | 8,970,000.00 USD | 22,100.00 USD | 7,630.00 USD | 24,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.05` | 1,820.00 USD | 452,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.10` | 8,910,000.00 USD | 8,910,000.00 USD | 363.50 USD | 682.90 USD | 8,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.20` | 3,420,000.00 USD | 3,420,000.00 USD | 4,490.00 USD | 5,820.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.20` | 8,900,000.00 USD | 8,900,000.00 USD | 6,960.00 USD | 500.40 USD | 34,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.25` | 102.51 USD | 450,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.30` | 3,410,000.00 USD | 3,410,000.00 USD | 171.03 USD | 1,290.00 USD | 2,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.30` | 8,860,000.00 USD | 8,860,000.00 USD | 16,270.00 USD | 3,640.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.35` | 1,140.00 USD | 450,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.40` | 3,400,000.00 USD | 3,400,000.00 USD | 4,370.00 USD | 3,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.40` | 8,840,000.00 USD | 8,840,000.00 USD | 28,280.00 USD | 20,470.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,720.00 USD | 449,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.50` | 3,400,000.00 USD | 3,400,000.00 USD | 5,790.00 USD | 2,110.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.50` | 8,760,000.00 USD | 8,760,000.00 USD | 32,450.00 USD | 6,790.00 USD | 44,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.55` | 84,100.00 USD | 444,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.60` | 3,380,000.00 USD | 3,380,000.00 USD | 1,660.00 USD | 2,640.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.60` | 8,670,000.00 USD | 8,670,000.00 USD | 56,670.00 USD | 21,530.00 USD | 31,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.70` | 3,370,000.00 USD | 3,370,000.00 USD | 4,820.00 USD | 1,440.00 USD | 11,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.70` | 8,560,000.00 USD | 8,560,000.00 USD | 65,150.00 USD | 32,820.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.75` | 9,050.00 USD | 360,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.80` | 3,350,000.00 USD | 3,350,000.00 USD | 12,550.00 USD | 3,100.00 USD | 8,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.80` | 8,430,000.00 USD | 8,430,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.90` | 3,330,000.00 USD | 3,330,000.00 USD | 826.24 USD | 260.05 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.90` | 8,330,000.00 USD | 8,330,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.95` | 431.55 USD | 351,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.00` | 3,320,000.00 USD | 3,320,000.00 USD | 5,040.00 USD | 0.00 USD | 430.77 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.00` | 8,070,000.00 USD | 8,070,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.10` | 3,310,000.00 USD | 3,310,000.00 USD | 9,210.00 USD | 6,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.10` | 7,950,000.00 USD | 7,950,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.15` | 219,370.00 USD | 351,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.20` | 3,300,000.00 USD | 3,300,000.00 USD | 2,360.00 USD | 1,130.00 USD | 17,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.20` | 7,870,000.00 USD | 7,870,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.25` | 202.44 USD | 131,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.30` | 3,270,000.00 USD | 3,270,000.00 USD | 16,790.00 USD | 14,100.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.30` | 7,800,000.00 USD | 7,800,000.00 USD | 28,400.00 USD | 26,720.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.35` | 453.93 USD | 131,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.40` | 3,230,000.00 USD | 3,230,000.00 USD | 13,750.00 USD | 11,490.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.40` | 7,700,000.00 USD | 7,700,000.00 USD | 73,130.00 USD | 42,820.00 USD | 46,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.45` | 27,210.00 USD | 131,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.50` | 3,200,000.00 USD | 3,200,000.00 USD | 7,880.00 USD | 10,980.00 USD | 37,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.50` | 7,540,000.00 USD | 7,540,000.00 USD | 38,520.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.55` | 551.07 USD | 103,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.60` | 3,150,000.00 USD | 3,150,000.00 USD | 9,060.00 USD | 18,490.00 USD | 757.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.60` | 7,440,000.00 USD | 7,440,000.00 USD | 37,880.00 USD | 36,790.00 USD | 41,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.65` | 9,100.00 USD | 103,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.70` | 3,120,000.00 USD | 3,120,000.00 USD | 2,890.00 USD | 13,810.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.70` | 7,320,000.00 USD | 7,320,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.75` | 6,480.00 USD | 94,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.80` | 3,080,000.00 USD | 3,080,000.00 USD | 12,590.00 USD | 19,270.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.80` | 7,290,000.00 USD | 7,290,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.85` | 16,530.00 USD | 87,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.90` | 3,030,000.00 USD | 3,030,000.00 USD | 9,460.00 USD | 19,910.00 USD | 23,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.90` | 7,230,000.00 USD | 7,230,000.00 USD | 5,870.00 USD | 25,410.00 USD | 28,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.95` | 13,950.00 USD | 71,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.00` | 2,980,000.00 USD | 2,980,000.00 USD | 20,980.00 USD | 25,480.00 USD | 25,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.00` | 7,170,000.00 USD | 7,170,000.00 USD | 64,300.00 USD | 26,440.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.10` | 2,910,000.00 USD | 2,910,000.00 USD | 34,880.00 USD | 17,130.00 USD | 50,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 7,070,000.00 USD | 7,070,000.00 USD | 24,220.00 USD | 28,090.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.15` | 1,900.00 USD | 57,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.20` | 2,810,000.00 USD | 2,810,000.00 USD | 15,020.00 USD | 7,630.00 USD | 46,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 6,980,000.00 USD | 6,980,000.00 USD | 38,380.00 USD | 13,960.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.25` | 4,930.00 USD | 55,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.30` | 2,740,000.00 USD | 2,740,000.00 USD | 26,510.00 USD | 21,640.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 6,900,000.00 USD | 6,900,000.00 USD | 24,840.00 USD | 41,300.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.35` | 134.02 USD | 50,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.40` | 2,680,000.00 USD | 2,680,000.00 USD | 12,460.00 USD | 15,120.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 6,830,000.00 USD | 6,830,000.00 USD | 20,580.00 USD | 38,950.00 USD | 22,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.45` | 2,470.00 USD | 50,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.50` | 2,640,000.00 USD | 2,640,000.00 USD | 53,350.00 USD | 29,580.00 USD | 74,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.50` | 6,740,000.00 USD | 6,740,000.00 USD | 38,720.00 USD | 667.05 USD | 11,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.55` | 8,700.00 USD | 47,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.60` | 2,490,000.00 USD | 2,490,000.00 USD | 8,330.00 USD | 40,700.00 USD | 717.10 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.60` | 6,690,000.00 USD | 6,690,000.00 USD | 74,610.00 USD | 32,590.00 USD | 59,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.70` | 2,440,000.00 USD | 2,440,000.00 USD | 16,690.00 USD | 19,440.00 USD | 28,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.70` | 6,530,000.00 USD | 6,530,000.00 USD | 20,250.00 USD | 92,920.00 USD | 108,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.75` | 4,240.00 USD | 39,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.80` | 2,370,000.00 USD | 2,370,000.00 USD | 27,090.00 USD | 50,290.00 USD | 102,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.80` | 6,310,000.00 USD | 6,310,000.00 USD | 39,200.00 USD | 35,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.85` | 5,950.00 USD | 34,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.90` | 2,190,000.00 USD | 2,190,000.00 USD | 43,760.00 USD | 50,040.00 USD | 26,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.90` | 6,230,000.00 USD | 6,230,000.00 USD | 39,680.00 USD | 28,710.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.95` | 25,840.00 USD | 28,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.00` | 2,070,000.00 USD | 2,070,000.00 USD | 26,670.00 USD | 30,500.00 USD | 39,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.00` | 6,130,000.00 USD | 6,130,000.00 USD | 39,690.00 USD | 25,810.00 USD | 81,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.10` | 1,980,000.00 USD | 1,980,000.00 USD | 14,570.00 USD | 42,760.00 USD | 87,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.10` | 5,980,000.00 USD | 5,980,000.00 USD | 45,320.00 USD | 17,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.15` | 1,720.00 USD | 3,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.20` | 1,830,000.00 USD | 1,830,000.00 USD | 24,240.00 USD | 6,510.00 USD | 41,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.20` | 5,920,000.00 USD | 5,920,000.00 USD | 162,460.00 USD | 28,320.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.25` | 405.76 USD | 1,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.30` | 1,760,000.00 USD | 1,760,000.00 USD | 4,060.00 USD | 0.00 USD | 5,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.30` | 5,700,000.00 USD | 5,700,000.00 USD | 57,250.00 USD | 24,540.00 USD | 34,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.35` | 941.09 USD | 941.09 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.40` | 1,750,000.00 USD | 1,750,000.00 USD | 3,460.00 USD | 1,850.00 USD | 657.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.40` | 5,590,000.00 USD | 5,590,000.00 USD | 44,030.00 USD | 7,250.00 USD | 91,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.50` | 1,740,000.00 USD | 1,740,000.00 USD | 9,110.00 USD | 3,940.00 USD | 2,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.50` | 5,440,000.00 USD | 5,440,000.00 USD | 48,660.00 USD | 3,440.00 USD | 20,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.60` | 1,730,000.00 USD | 1,730,000.00 USD | 72,650.00 USD | 220.65 USD | 13,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.60` | 5,370,000.00 USD | 5,370,000.00 USD | 52,800.00 USD | 1,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.70` | 1,640,000.00 USD | 1,640,000.00 USD | 6,210.00 USD | 2,400.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.70` | 5,320,000.00 USD | 5,320,000.00 USD | 131,400.00 USD | 3,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.80` | 1,630,000.00 USD | 1,630,000.00 USD | 44,920.00 USD | 3,640.00 USD | 250.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.80` | 5,180,000.00 USD | 5,180,000.00 USD | 99,150.00 USD | 17,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.90` | 1,580,000.00 USD | 1,580,000.00 USD | 43,240.00 USD | 18,200.00 USD | 15,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.90` | 5,070,000.00 USD | 5,070,000.00 USD | 148,940.00 USD | 21,360.00 USD | 1,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.00` | 1,500,000.00 USD | 1,500,000.00 USD | 45,350.00 USD | 15,370.00 USD | 68,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.00` | 4,890,000.00 USD | 4,890,000.00 USD | 353,050.00 USD | 71,820.00 USD | 296,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.10` | 1,370,000.00 USD | 1,370,000.00 USD | 91,490.00 USD | 19,160.00 USD | 45,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.10` | 4,170,000.00 USD | 4,170,000.00 USD | 302,190.00 USD | 0.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.20` | 1,220,000.00 USD | 1,220,000.00 USD | 72,600.00 USD | 15,510.00 USD | 40,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.20` | 3,870,000.00 USD | 3,870,000.00 USD | 205,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.30` | 1,090,000.00 USD | 1,090,000.00 USD | 15,600.00 USD | 0.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.30` | 3,660,000.00 USD | 3,660,000.00 USD | 381,380.00 USD | 0.00 USD | 181,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.40` | 1,070,000.00 USD | 1,070,000.00 USD | 51,570.00 USD | 35,500.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.40` | 3,100,000.00 USD | 3,100,000.00 USD | 304,270.00 USD | 13,830.00 USD | 92,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.50` | 976,600.00 USD | 976,600.00 USD | 9,670.00 USD | 46,240.00 USD | 1,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.50` | 2,690,000.00 USD | 2,690,000.00 USD | 159,720.00 USD | 15,240.00 USD | 239,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.60` | 919,370.00 USD | 919,370.00 USD | 913.17 USD | 21,680.00 USD | 5,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.60` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 1,930.00 USD | 116,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.70` | 891,210.00 USD | 891,210.00 USD | 0.00 USD | 15,420.00 USD | 82,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.80` | 793,340.00 USD | 793,340.00 USD | 0.00 USD | 30,590.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.90` | 750,690.00 USD | 750,690.00 USD | 49,450.00 USD | 14,710.00 USD | 1,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.90` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 58,990.00 USD | 47,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.00` | 684,840.00 USD | 684,840.00 USD | 25,080.00 USD | 11,440.00 USD | 59,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.00` | 2,050,000.00 USD | 2,050,000.00 USD | 73,940.00 USD | 0.00 USD | 2,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.10` | 588,820.00 USD | 588,820.00 USD | 3,850.00 USD | 53,510.00 USD | 51,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.10` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 18,510.00 USD | 47,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.20` | 479,890.00 USD | 479,890.00 USD | 24,740.00 USD | 7,520.00 USD | 58,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.20` | 1,910,000.00 USD | 1,910,000.00 USD | 57,400.00 USD | 59,710.00 USD | 150,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.30` | 389,110.00 USD | 389,110.00 USD | 39,800.00 USD | 22,650.00 USD | 51,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.30` | 1,640,000.00 USD | 1,640,000.00 USD | 23,140.00 USD | 11,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.40` | 274,890.00 USD | 274,890.00 USD | 0.00 USD | 6,510.00 USD | 742.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.40` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 18,550.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.50` | 267,640.00 USD | 267,640.00 USD | 0.00 USD | 9,250.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.50` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 33,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.60` | 1,550,000.00 USD | 1,550,000.00 USD | 426,340.00 USD | 13,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.70` | 252,890.00 USD | 252,890.00 USD | 0.00 USD | 7,490.00 USD | 613.46 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.70` | 1,110,000.00 USD | 1,110,000.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.80` | 244,780.00 USD | 244,780.00 USD | 6,170.00 USD | 26,160.00 USD | 3,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.80` | 903,020.00 USD | 903,020.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.90` | 209,110.00 USD | 209,110.00 USD | 103,700.00 USD | 11,780.00 USD | 89,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.90` | 812,050.00 USD | 812,050.00 USD | 141,330.00 USD | 101,960.00 USD | 117,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.00` | 4,510.00 USD | 4,510.00 USD | 0.00 USD | 0.00 USD | 4,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.00` | 451,100.00 USD | 451,100.00 USD | 2,590.00 USD | 118,560.00 USD | 171,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.10` | 74,130.00 USD | 74,130.00 USD | 68,240.00 USD | 5,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.10` | 148,270.00 USD | 148,270.00 USD | 68,240.00 USD | 5,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.10` | 158,840.00 USD | 158,840.00 USD | 3,980.00 USD | 154,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.20` | 79,940.00 USD | 79,940.00 USD | 0.00 USD | 79,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.20` | 159,890.00 USD | 159,890.00 USD | 0.00 USD | 79,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.30` | 196,590.00 USD | 196,590.00 USD | 0.00 USD | 44,360.00 USD | 3,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.30` | 163,750.00 USD | 163,750.00 USD | 1,270.00 USD | 0.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.40` | 221,790.00 USD | 221,790.00 USD | 5,040.00 USD | 17,690.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.40` | 177,440.00 USD | 177,440.00 USD | 2,650.00 USD | 11,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.50` | 606,910.00 USD | 606,910.00 USD | 138,540.00 USD | 101,980.00 USD | 144,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.50` | 497,760.00 USD | 497,760.00 USD | 170,750.00 USD | 143,420.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.60` | 841,620.00 USD | 841,620.00 USD | 49,560.00 USD | 104,240.00 USD | 80,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.60` | 997,520.00 USD | 997,520.00 USD | 363,190.00 USD | 136,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.70` | 1,270,000.00 USD | 1,270,000.00 USD | 97,300.00 USD | 27,730.00 USD | 307,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.70` | 1,340,000.00 USD | 1,340,000.00 USD | 117,290.00 USD | 121,500.00 USD | 98,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.80` | 1,480,000.00 USD | 1,480,000.00 USD | 117,760.00 USD | 17,250.00 USD | 68,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.80` | 1,880,000.00 USD | 1,880,000.00 USD | 153,580.00 USD | 92,780.00 USD | 303,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.90` | 1,550,000.00 USD | 1,550,000.00 USD | 38,540.00 USD | 10,710.00 USD | 22,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.90` | 2,310,000.00 USD | 2,310,000.00 USD | 113,780.00 USD | 48,600.00 USD | 266,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.00` | 1,590,000.00 USD | 1,590,000.00 USD | 6,480.00 USD | 23,050.00 USD | 13,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.00` | 2,570,000.00 USD | 2,570,000.00 USD | 88,680.00 USD | 20,690.00 USD | 151,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.10` | 1,700,000.00 USD | 1,700,000.00 USD | 59,550.00 USD | 26,670.00 USD | 26,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.10` | 2,660,000.00 USD | 2,660,000.00 USD | 36,580.00 USD | 26,000.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.20` | 1,870,000.00 USD | 1,870,000.00 USD | 37,450.00 USD | 35,770.00 USD | 95,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.20` | 2,780,000.00 USD | 2,780,000.00 USD | 95,090.00 USD | 21,090.00 USD | 5,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.30` | 1,990,000.00 USD | 1,990,000.00 USD | 24,260.00 USD | 36,820.00 USD | 58,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.30` | 2,910,000.00 USD | 2,910,000.00 USD | 22,360.00 USD | 28,570.00 USD | 82,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.40` | 2,180,000.00 USD | 2,180,000.00 USD | 70,320.00 USD | 45,150.00 USD | 70,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.40` | 3,370,000.00 USD | 3,370,000.00 USD | 124,180.00 USD | 72,180.00 USD | 257,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.50` | 2,580,000.00 USD | 2,580,000.00 USD | 184,770.00 USD | 48,350.00 USD | 167,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.50` | 3,500,000.00 USD | 3,500,000.00 USD | 99,810.00 USD | 31,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.60` | 2,740,000.00 USD | 2,740,000.00 USD | 69,720.00 USD | 24,050.00 USD | 62,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.60` | 3,720,000.00 USD | 3,720,000.00 USD | 149,560.00 USD | 40,430.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.70` | 2,890,000.00 USD | 2,890,000.00 USD | 36,620.00 USD | 26,070.00 USD | 96,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.70` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 5,400.00 USD | 57,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.75` | 155.35 USD | 155.35 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `57.80` | 2,990,000.00 USD | 2,990,000.00 USD | 9,690.00 USD | 13,860.00 USD | 73,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.80` | 3,850,000.00 USD | 3,850,000.00 USD | 9,650.00 USD | 14,360.00 USD | 49,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.90` | 3,030,000.00 USD | 3,030,000.00 USD | 13,000.00 USD | 14,100.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.90` | 3,880,000.00 USD | 3,880,000.00 USD | 5,120.00 USD | 963.90 USD | 22,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.95` | 125.75 USD | 281.10 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.00` | 3,050,000.00 USD | 3,050,000.00 USD | 4,580.00 USD | 5,870.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.00` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 3,670.00 USD | 86,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.10` | 3,100,000.00 USD | 3,100,000.00 USD | 31,400.00 USD | 9,120.00 USD | 15,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.10` | 3,980,000.00 USD | 3,980,000.00 USD | 5,470.00 USD | 1,310.00 USD | 848.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.20` | 3,140,000.00 USD | 3,140,000.00 USD | 27,190.00 USD | 9,520.00 USD | 487.60 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.20` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 4,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.30` | 3,230,000.00 USD | 3,230,000.00 USD | 23,960.00 USD | 17,260.00 USD | 51,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.30` | 4,060,000.00 USD | 4,060,000.00 USD | 36,970.00 USD | 9,580.00 USD | 27,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.40` | 3,290,000.00 USD | 3,290,000.00 USD | 2,240.00 USD | 15,040.00 USD | 35,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.40` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 9,260.00 USD | 78,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.50` | 3,320,000.00 USD | 3,320,000.00 USD | 21,130.00 USD | 8,030.00 USD | 124.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.50` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.60` | 3,370,000.00 USD | 3,370,000.00 USD | 14,490.00 USD | 3,760.00 USD | 36,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.60` | 4,270,000.00 USD | 4,270,000.00 USD | 30,680.00 USD | 20,260.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.70` | 3,440,000.00 USD | 3,440,000.00 USD | 38,020.00 USD | 10,060.00 USD | 26,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.70` | 4,340,000.00 USD | 4,340,000.00 USD | 15,810.00 USD | 11,600.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.80` | 3,520,000.00 USD | 3,520,000.00 USD | 35,830.00 USD | 14,730.00 USD | 23,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.80` | 4,350,000.00 USD | 4,350,000.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.90` | 3,690,000.00 USD | 3,690,000.00 USD | 22,130.00 USD | 60,920.00 USD | 90,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.90` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 54,240.00 USD | 83,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.00` | 4,010,000.00 USD | 4,010,000.00 USD | 129,180.00 USD | 58,790.00 USD | 127,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.00` | 4,930,000.00 USD | 4,930,000.00 USD | 259,280.00 USD | 65,270.00 USD | 118,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.10` | 4,300,000.00 USD | 4,300,000.00 USD | 91,380.00 USD | 39,780.00 USD | 163,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.10` | 5,230,000.00 USD | 5,230,000.00 USD | 91,060.00 USD | 45,400.00 USD | 158,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.20` | 4,510,000.00 USD | 4,510,000.00 USD | 101,760.00 USD | 59,450.00 USD | 49,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.20` | 5,570,000.00 USD | 5,570,000.00 USD | 153,580.00 USD | 18,540.00 USD | 174,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.30` | 4,820,000.00 USD | 4,820,000.00 USD | 171,630.00 USD | 45,010.00 USD | 94,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.30` | 5,850,000.00 USD | 5,850,000.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.35` | 9,440.00 USD | 9,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.40` | 4,990,000.00 USD | 4,990,000.00 USD | 64,900.00 USD | 45,810.00 USD | 59,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.40` | 6,160,000.00 USD | 6,160,000.00 USD | 105,490.00 USD | 73,620.00 USD | 137,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.50` | 5,150,000.00 USD | 5,150,000.00 USD | 89,030.00 USD | 38,560.00 USD | 33,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.50` | 6,320,000.00 USD | 6,320,000.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.60` | 5,260,000.00 USD | 5,260,000.00 USD | 43,670.00 USD | 53,100.00 USD | 7,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.60` | 6,820,000.00 USD | 6,820,000.00 USD | 270,460.00 USD | 147,800.00 USD | 86,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.70` | 5,370,000.00 USD | 5,370,000.00 USD | 13,470.00 USD | 19,120.00 USD | 78,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.70` | 7,220,000.00 USD | 7,220,000.00 USD | 55,510.00 USD | 180,620.00 USD | 162,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.80` | 5,440,000.00 USD | 5,440,000.00 USD | 31,530.00 USD | 26,470.00 USD | 10,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.80` | 7,590,000.00 USD | 7,590,000.00 USD | 118,240.00 USD | 97,600.00 USD | 154,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.90` | 5,620,000.00 USD | 5,620,000.00 USD | 112,000.00 USD | 20,240.00 USD | 50,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.90` | 7,930,000.00 USD | 7,930,000.00 USD | 209,780.00 USD | 83,540.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.00` | 5,860,000.00 USD | 5,860,000.00 USD | 164,190.00 USD | 29,090.00 USD | 50,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.00` | 8,330,000.00 USD | 8,330,000.00 USD | 154,790.00 USD | 152,810.00 USD | 94,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.10` | 6,010,000.00 USD | 6,010,000.00 USD | 64,090.00 USD | 28,140.00 USD | 57,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.10` | 8,760,000.00 USD | 8,760,000.00 USD | 217,190.00 USD | 100,570.00 USD | 113,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.15` | 208,880.00 USD | 218,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.20` | 6,170,000.00 USD | 6,170,000.00 USD | 59,560.00 USD | 19,740.00 USD | 82,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.20` | 9,130,000.00 USD | 9,130,000.00 USD | 162,230.00 USD | 99,360.00 USD | 108,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.30` | 6,280,000.00 USD | 6,280,000.00 USD | 53,910.00 USD | 30,600.00 USD | 24,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.30` | 9,530,000.00 USD | 9,530,000.00 USD | 133,350.00 USD | 100,380.00 USD | 170,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.40` | 6,400,000.00 USD | 6,400,000.00 USD | 66,740.00 USD | 13,730.00 USD | 39,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.40` | 9,910,000.00 USD | 9,910,000.00 USD | 64,850.00 USD | 108,300.00 USD | 204,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.50` | 6,480,000.00 USD | 6,480,000.00 USD | 22,700.00 USD | 19,320.00 USD | 36,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.50` | 10,290,000.00 USD | 10,290,000.00 USD | 115,390.00 USD | 86,870.00 USD | 175,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.60` | 6,550,000.00 USD | 6,550,000.00 USD | 40,710.00 USD | 19,140.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.60` | 10,680,000.00 USD | 10,680,000.00 USD | 251,100.00 USD | 18,640.00 USD | 118,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.70` | 6,610,000.00 USD | 6,610,000.00 USD | 34,230.00 USD | 22,330.00 USD | 3,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.70` | 10,880,000.00 USD | 10,880,000.00 USD | 119,080.00 USD | 57,480.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.80` | 6,680,000.00 USD | 6,680,000.00 USD | 15,430.00 USD | 12,060.00 USD | 47,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.80` | 11,070,000.00 USD | 11,070,000.00 USD | 46,960.00 USD | 69,290.00 USD | 76,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.90` | 6,760,000.00 USD | 6,760,000.00 USD | 35,570.00 USD | 21,920.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.90` | 11,270,000.00 USD | 11,270,000.00 USD | 105,970.00 USD | 34,400.00 USD | 65,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.95` | 397.39 USD | 219,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.00` | 6,830,000.00 USD | 6,830,000.00 USD | 44,070.00 USD | 6,430.00 USD | 18,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 11,390,000.00 USD | 11,390,000.00 USD | 77,670.00 USD | 36,060.00 USD | 5,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.10` | 6,860,000.00 USD | 6,860,000.00 USD | 12,010.00 USD | 6,270.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 11,430,000.00 USD | 11,430,000.00 USD | 31,540.00 USD | 1,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.20` | 6,970,000.00 USD | 6,970,000.00 USD | 72,520.00 USD | 0.00 USD | 38,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.20` | 11,620,000.00 USD | 11,620,000.00 USD | 78,320.00 USD | 60,240.00 USD | 52,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.30` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 3,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.30` | 11,700,000.00 USD | 11,700,000.00 USD | 27,780.00 USD | 21,000.00 USD | 33,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.40` | 6,980,000.00 USD | 6,980,000.00 USD | 1,190.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.40` | 11,830,000.00 USD | 11,830,000.00 USD | 66,470.00 USD | 25,720.00 USD | 35,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.50` | 6,980,000.00 USD | 6,980,000.00 USD | 1,060.00 USD | 1,290.00 USD | 2,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.50` | 11,920,000.00 USD | 11,920,000.00 USD | 19,810.00 USD | 35,300.00 USD | 36,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.60` | 6,990,000.00 USD | 6,990,000.00 USD | 5,360.00 USD | 3,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.60` | 12,130,000.00 USD | 12,130,000.00 USD | 38,370.00 USD | 52,240.00 USD | 121,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.70` | 7,010,000.00 USD | 7,010,000.00 USD | 10,770.00 USD | 2,110.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.70` | 12,320,000.00 USD | 12,320,000.00 USD | 82,820.00 USD | 10,880.00 USD | 99,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.80` | 7,030,000.00 USD | 7,030,000.00 USD | 3,480.00 USD | 2,640.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.80` | 12,580,000.00 USD | 12,580,000.00 USD | 158,760.00 USD | 25,670.00 USD | 71,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.90` | 7,040,000.00 USD | 7,040,000.00 USD | 4,800.00 USD | 1,440.00 USD | 11,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.90` | 12,730,000.00 USD | 12,730,000.00 USD | 72,920.00 USD | 32,820.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.00` | 7,070,000.00 USD | 7,070,000.00 USD | 15,300.00 USD | 3,100.00 USD | 8,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.00` | 12,830,000.00 USD | 12,830,000.00 USD | 50,080.00 USD | 8,550.00 USD | 40,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.10` | 7,070,000.00 USD | 7,070,000.00 USD | 2,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.10` | 12,840,000.00 USD | 12,840,000.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.20` | 12,950,000.00 USD | 12,950,000.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.30` | 13,100,000.00 USD | 13,100,000.00 USD | 29,050.00 USD | 23,450.00 USD | 97,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.40` | 13,240,000.00 USD | 13,240,000.00 USD | 77,960.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.50` | 13,320,000.00 USD | 13,320,000.00 USD | 42,730.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.60` | 13,390,000.00 USD | 13,390,000.00 USD | 33,900.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.70` | 13,470,000.00 USD | 13,470,000.00 USD | 22,020.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.80` | 13,620,000.00 USD | 13,620,000.00 USD | 71,230.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.90` | 13,710,000.00 USD | 13,710,000.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `62.95` | 138.49 USD | 219,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `63.00` | 13,770,000.00 USD | 13,770,000.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.10` | 13,810,000.00 USD | 13,810,000.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.30` | 13,850,000.00 USD | 13,850,000.00 USD | 15,010.00 USD | 11,500.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.40` | 13,870,000.00 USD | 13,870,000.00 USD | 11,980.00 USD | 1,320.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `63.45` | 3,350.00 USD | 222,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `63.50` | 13,900,000.00 USD | 13,900,000.00 USD | 5,430.00 USD | 15,810.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `63.55` | 8,180.00 USD | 230,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `63.60` | 13,990,000.00 USD | 13,990,000.00 USD | 63,480.00 USD | 20,800.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.70` | 14,070,000.00 USD | 14,070,000.00 USD | 18,220.00 USD | 18,810.00 USD | 34,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `66.95` | 121.18 USD | 230,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.85` | 709.03 USD | 231,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `70.55` | 40,780.00 USD | 272,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `71.35` | 112.02 USD | 272,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `76.35` | 8,380.00 USD | 280,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.75` | 578,460.00 USD | 859,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.85` | 602.56 USD | 859,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.95` | 136.41 USD | 859,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.75` | 646.00 USD | 860,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.05` | 19,000.00 USD | 879,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.55` | 123.96 USD | 879,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.45` | 3,300.00 USD | 883,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.75` | 214.32 USD | 883,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `84.35` | 2,780.00 USD | 886,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `85.75` | 777.75 USD | 886,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `87.45` | 23,330.00 USD | 910,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `88.45` | 116.75 USD | 910,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `89.55` | 951.92 USD | 911,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `90.35` | 101.19 USD | 911,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `91.95` | 155.40 USD | 911,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `97.85` | 2,450.00 USD | 913,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.35` | 31,010.00 USD | 944,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.25` | 213.71 USD | 945,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.85` | 2,320.00 USD | 947,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.55` | 356,130.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.75` | 1,620.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.85` | 1,860.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.15` | 199.30 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.05` | 6,470.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 664.59 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `11.35` | 3,020,000.00 USD | 0.00 USD | 136.20 USD | `-79.78%` | `12.00` |
| `Live` | `Long` | `12.25` | 3,020,000.00 USD | 0.00 USD | 122.50 USD | `-78.17%` | `10.00` |
| `Live` | `Long` | `12.75` | 3,020,000.00 USD | 0.00 USD | 2,560.00 USD | `-77.28%` | `200.43` |
| `Live` | `Long` | `13.15` | 3,020,000.00 USD | 0.00 USD | 2,220.00 USD | `-76.57%` | `168.79` |
| `Live` | `Long` | `13.65` | 3,020,000.00 USD | 0.00 USD | 150.15 USD | `-75.68%` | `11.00` |
| `Live` | `Long` | `15.75` | 3,020,000.00 USD | 0.00 USD | 2,370.00 USD | `-71.94%` | `150.57` |
| `Live` | `Long` | `16.65` | 3,010,000.00 USD | 0.00 USD | 370.30 USD | `-70.33%` | `22.24` |
| `Live` | `Long` | `17.15` | 3,010,000.00 USD | 0.00 USD | 128.11 USD | `-69.44%` | `7.47` |
| `Live` | `Long` | `17.45` | 3,010,000.00 USD | 0.00 USD | 140.47 USD | `-68.91%` | `8.05` |
| `Live` | `Long` | `17.85` | 3,010,000.00 USD | 0.00 USD | 2,140.00 USD | `-68.19%` | `120.00` |
| `Live` | `Long` | `18.25` | 3,010,000.00 USD | 0.00 USD | 164.61 USD | `-67.48%` | `9.02` |
| `Live` | `Long` | `19.05` | 3,010,000.00 USD | 0.00 USD | 3,470.00 USD | `-66.06%` | `182.00` |
| `Live` | `Long` | `19.45` | 3,010,000.00 USD | 0.00 USD | 2,010.00 USD | `-65.34%` | `103.47` |
| `Live` | `Long` | `19.95` | 3,010,000.00 USD | 0.00 USD | 18,550.00 USD | `-64.45%` | `930.00` |
| `Live` | `Long` | `20.25` | 2,990,000.00 USD | 0.00 USD | 133.65 USD | `-63.92%` | `6.60` |
| `Live` | `Long` | `20.75` | 2,990,000.00 USD | 0.00 USD | 4,050.00 USD | `-63.03%` | `195.03` |
| `Live` | `Long` | `22.15` | 2,980,000.00 USD | 0.00 USD | 1,330.00 USD | `-60.53%` | `60.00` |
| `Live` | `Long` | `22.45` | 2,980,000.00 USD | 0.00 USD | 362.12 USD | `-60.00%` | `16.13` |
| `Live` | `Long` | `22.55` | 2,980,000.00 USD | 0.00 USD | 466.56 USD | `-59.82%` | `20.69` |
| `Live` | `Long` | `23.35` | 2,980,000.00 USD | 0.00 USD | 990.74 USD | `-58.39%` | `42.43` |
| `Live` | `Long` | `23.45` | 2,980,000.00 USD | 0.00 USD | 370.98 USD | `-58.22%` | `15.82` |
| `Live` | `Long` | `23.65` | 2,980,000.00 USD | 0.00 USD | 920.46 USD | `-57.86%` | `38.92` |
| `Live` | `Long` | `23.85` | 2,980,000.00 USD | 0.00 USD | 195.57 USD | `-57.50%` | `8.20` |
| `Live` | `Long` | `24.55` | 2,980,000.00 USD | 0.00 USD | 7,230.00 USD | `-56.26%` | `294.67` |
| `Live` | `Long` | `24.65` | 2,970,000.00 USD | 0.00 USD | 113,020.00 USD | `-56.08%` | `4,584.81` |
| `Live` | `Long` | `25.25` | 2,860,000.00 USD | 0.00 USD | 277,980.00 USD | `-55.01%` | `11,009.19` |
| `Live` | `Long` | `25.35` | 2,580,000.00 USD | 0.00 USD | 173.39 USD | `-54.83%` | `6.84` |
| `Live` | `Long` | `25.45` | 2,580,000.00 USD | 0.00 USD | 7,640.00 USD | `-54.65%` | `300.00` |
| `Live` | `Long` | `25.55` | 2,570,000.00 USD | 0.00 USD | 50,740.00 USD | `-54.47%` | `1,985.99` |
| `Live` | `Long` | `25.95` | 2,520,000.00 USD | 0.00 USD | 374.20 USD | `-53.76%` | `14.42` |
| `Live` | `Long` | `26.05` | 2,520,000.00 USD | 0.00 USD | 721.85 USD | `-53.58%` | `27.71` |
| `Live` | `Long` | `27.05` | 2,520,000.00 USD | 0.00 USD | 5,510.00 USD | `-51.80%` | `203.85` |
| `Live` | `Long` | `27.55` | 2,520,000.00 USD | 0.00 USD | 435.57 USD | `-50.91%` | `15.81` |
| `Live` | `Long` | `27.95` | 2,520,000.00 USD | 0.00 USD | 173.85 USD | `-50.20%` | `6.22` |
| `Live` | `Long` | `29.15` | 2,520,000.00 USD | 0.00 USD | 583.00 USD | `-48.06%` | `20.00` |
| `Live` | `Long` | `29.75` | 2,510,000.00 USD | 0.00 USD | 297,500.00 USD | `-46.99%` | `10,000.00` |
| `Live` | `Long` | `30.05` | 2,220,000.00 USD | 0.00 USD | 218.46 USD | `-46.46%` | `7.27` |
| `Live` | `Long` | `30.55` | 2,220,000.00 USD | 0.00 USD | 725.56 USD | `-45.57%` | `23.75` |
| `Live` | `Long` | `30.65` | 2,220,000.00 USD | 0.00 USD | 1,750.00 USD | `-45.39%` | `57.19` |
| `Live` | `Long` | `30.95` | 2,210,000.00 USD | 0.00 USD | 538.53 USD | `-44.85%` | `17.40` |
| `Live` | `Long` | `31.15` | 2,210,000.00 USD | 0.00 USD | 27,620.00 USD | `-44.50%` | `886.80` |
| `Live` | `Long` | `31.55` | 2,190,000.00 USD | 0.00 USD | 1,060.00 USD | `-43.78%` | `33.49` |
| `Live` | `Long` | `31.65` | 2,190,000.00 USD | 0.00 USD | 7,340.00 USD | `-43.61%` | `231.96` |
| `Live` | `Long` | `31.85` | 2,180,000.00 USD | 0.00 USD | 2,870.00 USD | `-43.25%` | `90.00` |
| `Live` | `Long` | `31.95` | 2,170,000.00 USD | 0.00 USD | 125.24 USD | `-43.07%` | `3.92` |
| `Live` | `Long` | `32.15` | 2,170,000.00 USD | 0.00 USD | 450.10 USD | `-42.72%` | `14.00` |
| `Live` | `Long` | `32.25` | 2,170,000.00 USD | 0.00 USD | 4,000.00 USD | `-42.54%` | `124.01` |
| `Live` | `Long` | `32.35` | 2,170,000.00 USD | 0.00 USD | 172.10 USD | `-42.36%` | `5.32` |
| `Live` | `Long` | `32.45` | 2,170,000.00 USD | 0.00 USD | 405.30 USD | `-42.18%` | `12.49` |
| `Live` | `Long` | `32.65` | 2,170,000.00 USD | 0.00 USD | 653.00 USD | `-41.82%` | `20.00` |
| `Live` | `Long` | `32.75` | 2,170,000.00 USD | 0.00 USD | 953.68 USD | `-41.65%` | `29.12` |
| `Live` | `Long` | `32.85` | 2,170,000.00 USD | 0.00 USD | 32,850.00 USD | `-41.47%` | `1,000.01` |
| `Live` | `Long` | `33.05` | 2,140,000.00 USD | 0.00 USD | 5,760.00 USD | `-41.11%` | `174.22` |
| `Live` | `Long` | `33.65` | 2,130,000.00 USD | 0.00 USD | 257.76 USD | `-40.04%` | `7.66` |
| `Live` | `Long` | `33.75` | 2,130,000.00 USD | 0.00 USD | 402.30 USD | `-39.86%` | `11.92` |
| `Live` | `Long` | `33.95` | 2,130,000.00 USD | 0.00 USD | 4,430.00 USD | `-39.51%` | `130.63` |
| `Live` | `Long` | `34.05` | 2,120,000.00 USD | 0.00 USD | 182.85 USD | `-39.33%` | `5.37` |
| `Live` | `Long` | `34.15` | 2,120,000.00 USD | 0.00 USD | 126.70 USD | `-39.15%` | `3.71` |
| `Live` | `Long` | `34.45` | 2,120,000.00 USD | 0.00 USD | 65,890.00 USD | `-38.62%` | `1,912.61` |
| `Live` | `Long` | `34.65` | 2,060,000.00 USD | 0.00 USD | 3,240.00 USD | `-38.26%` | `93.56` |
| `Live` | `Long` | `34.95` | 2,050,000.00 USD | 0.00 USD | 104.85 USD | `-37.73%` | `3.00` |
| `Live` | `Long` | `35.05` | 2,050,000.00 USD | 0.00 USD | 440.93 USD | `-37.55%` | `12.58` |
| `Live` | `Long` | `35.95` | 2,050,000.00 USD | 0.00 USD | 275.74 USD | `-35.94%` | `7.67` |
| `Live` | `Long` | `36.35` | 2,050,000.00 USD | 0.00 USD | 3,020.00 USD | `-35.23%` | `83.03` |
| `Live` | `Long` | `36.45` | 2,050,000.00 USD | 0.00 USD | 1,690.00 USD | `-35.05%` | `46.28` |
| `Live` | `Long` | `36.55` | 2,050,000.00 USD | 0.00 USD | 1,830.00 USD | `-34.88%` | `50.00` |
| `Live` | `Long` | `36.75` | 2,050,000.00 USD | 0.00 USD | 101.80 USD | `-34.52%` | `2.77` |
| `Live` | `Long` | `37.05` | 2,050,000.00 USD | 0.00 USD | 1,050.00 USD | `-33.98%` | `28.27` |
| `Live` | `Long` | `37.15` | 2,050,000.00 USD | 0.00 USD | 438.74 USD | `-33.81%` | `11.81` |
| `Live` | `Long` | `37.35` | 2,050,000.00 USD | 0.00 USD | 9,260.00 USD | `-33.45%` | `247.91` |
| `Live` | `Long` | `37.55` | 2,040,000.00 USD | 0.00 USD | 3,530.00 USD | `-33.09%` | `94.04` |
| `Live` | `Long` | `37.75` | 2,030,000.00 USD | 0.00 USD | 377.50 USD | `-32.74%` | `10.00` |
| `Live` | `Long` | `37.85` | 2,030,000.00 USD | 0.00 USD | 6,210.00 USD | `-32.56%` | `164.03` |
| `Live` | `Long` | `37.95` | 2,030,000.00 USD | 0.00 USD | 446.67 USD | `-32.38%` | `11.77` |
| `Live` | `Long` | `38.25` | 2,030,000.00 USD | 0.00 USD | 695.38 USD | `-31.85%` | `18.18` |
| `Live` | `Long` | `38.35` | 2,030,000.00 USD | 0.00 USD | 847.54 USD | `-31.67%` | `22.10` |
| `Live` | `Long` | `38.45` | 2,020,000.00 USD | 0.00 USD | 2,400.00 USD | `-31.49%` | `62.34` |
| `Live` | `Long` | `38.55` | 2,020,000.00 USD | 0.00 USD | 993.82 USD | `-31.31%` | `25.78` |
| `Live` | `Long` | `38.65` | 2,020,000.00 USD | 0.00 USD | 4,280.00 USD | `-31.13%` | `110.74` |
| `Live` | `Long` | `38.95` | 2,020,000.00 USD | 0.00 USD | 3,700.00 USD | `-30.60%` | `94.93` |
| `Live` | `Long` | `39.05` | 2,010,000.00 USD | 0.00 USD | 664,760.00 USD | `-30.42%` | `17,023.28` |
| `Live` | `Long` | `39.15` | 1,350,000.00 USD | 0.00 USD | 570.02 USD | `-30.24%` | `14.56` |
| `Live` | `Long` | `39.35` | 1,350,000.00 USD | 0.00 USD | 264.83 USD | `-29.89%` | `6.73` |
| `Live` | `Long` | `39.45` | 1,350,000.00 USD | 0.00 USD | 716.41 USD | `-29.71%` | `18.16` |
| `Live` | `Long` | `39.55` | 1,350,000.00 USD | 0.00 USD | 312.44 USD | `-29.53%` | `7.90` |
| `Live` | `Long` | `39.65` | 1,350,000.00 USD | 0.00 USD | 5,900.00 USD | `-29.35%` | `148.78` |
| `Live` | `Long` | `39.75` | 1,340,000.00 USD | 0.00 USD | 1,180.00 USD | `-29.17%` | `29.57` |
| `Live` | `Long` | `39.85` | 1,340,000.00 USD | 0.00 USD | 133.10 USD | `-29.00%` | `3.34` |
| `Live` | `Long` | `40.05` | 1,340,000.00 USD | 0.00 USD | 2,160.00 USD | `-28.64%` | `53.97` |
| `Live` | `Long` | `40.35` | 1,340,000.00 USD | 0.00 USD | 8,880.00 USD | `-28.10%` | `220.00` |
| `Live` | `Long` | `40.45` | 1,330,000.00 USD | 0.00 USD | 1,010.00 USD | `-27.93%` | `24.92` |
| `Live` | `Long` | `40.55` | 1,330,000.00 USD | 0.00 USD | 133.00 USD | `-27.75%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,330,000.00 USD | 0.00 USD | 274.39 USD | `-27.57%` | `6.75` |
| `Live` | `Long` | `40.85` | 1,330,000.00 USD | 0.00 USD | 6,340.00 USD | `-27.21%` | `155.23` |
| `Live` | `Long` | `40.95` | 1,320,000.00 USD | 0.00 USD | 5,910.00 USD | `-27.04%` | `144.37` |
| `Live` | `Long` | `41.05` | 1,310,000.00 USD | 0.00 USD | 396.54 USD | `-26.86%` | `9.66` |
| `Live` | `Long` | `41.25` | 1,310,000.00 USD | 0.00 USD | 17,770.00 USD | `-26.50%` | `430.75` |
| `Live` | `Long` | `41.45` | 1,300,000.00 USD | 0.00 USD | 940.50 USD | `-26.14%` | `22.69` |
| `Live` | `Long` | `41.75` | 1,300,000.00 USD | 0.00 USD | 313.12 USD | `-25.61%` | `7.50` |
| `Live` | `Long` | `41.85` | 1,300,000.00 USD | 0.00 USD | 5,390.00 USD | `-25.43%` | `128.71` |
| `Live` | `Long` | `42.05` | 1,290,000.00 USD | 0.00 USD | 982.29 USD | `-25.08%` | `23.36` |
| `Live` | `Long` | `42.15` | 1,290,000.00 USD | 0.00 USD | 108,450.00 USD | `-24.90%` | `2,572.94` |
| `Live` | `Long` | `42.25` | 1,180,000.00 USD | 0.00 USD | 35,410.00 USD | `-24.72%` | `838.00` |
| `Live` | `Long` | `42.45` | 1,150,000.00 USD | 0.00 USD | 3,850.00 USD | `-24.36%` | `90.60` |
| `Live` | `Long` | `42.65` | 1,140,000.00 USD | 0.00 USD | 1,570.00 USD | `-24.01%` | `36.70` |
| `Live` | `Long` | `42.85` | 1,140,000.00 USD | 0.00 USD | 5,800.00 USD | `-23.65%` | `135.38` |
| `Live` | `Long` | `42.95` | 1,130,000.00 USD | 0.00 USD | 2,000.00 USD | `-23.47%` | `46.65` |
| `Live` | `Long` | `43.05` | 1,130,000.00 USD | 0.00 USD | 9,080.00 USD | `-23.29%` | `211.00` |
| `Live` | `Long` | `43.15` | 1,120,000.00 USD | 0.00 USD | 122,400.00 USD | `-23.12%` | `2,836.59` |
| `Live` | `Long` | `43.25` | 1,000,000.00 USD | 0.00 USD | 417.80 USD | `-22.94%` | `9.66` |
| `Live` | `Long` | `43.35` | 999,960.00 USD | 0.00 USD | 5,390.00 USD | `-22.76%` | `124.24` |
| `Live` | `Long` | `43.45` | 994,570.00 USD | 0.00 USD | 710.84 USD | `-22.58%` | `16.36` |
| `Live` | `Long` | `43.65` | 993,860.00 USD | 0.00 USD | 426.02 USD | `-22.22%` | `9.76` |
| `Live` | `Long` | `43.75` | 993,430.00 USD | 0.00 USD | 21,880.00 USD | `-22.05%` | `500.00` |
| `Live` | `Long` | `43.85` | 971,560.00 USD | 0.00 USD | 801.14 USD | `-21.87%` | `18.27` |
| `Live` | `Long` | `44.15` | 970,760.00 USD | 0.00 USD | 2,380.00 USD | `-21.33%` | `53.99` |
| `Live` | `Long` | `44.25` | 968,370.00 USD | 0.00 USD | 1,330.00 USD | `-21.16%` | `30.00` |
| `Live` | `Long` | `44.35` | 967,050.00 USD | 0.00 USD | 85,770.00 USD | `-20.98%` | `1,933.87` |
| `Live` | `Long` | `44.55` | 881,280.00 USD | 0.00 USD | 842.44 USD | `-20.62%` | `18.91` |
| `Live` | `Long` | `44.75` | 880,440.00 USD | 0.00 USD | 4,230.00 USD | `-20.26%` | `94.55` |
| `Live` | `Long` | `44.85` | 876,210.00 USD | 0.00 USD | 134.55 USD | `-20.09%` | `3.00` |
| `Live` | `Long` | `44.95` | 876,070.00 USD | 0.00 USD | 2,620.00 USD | `-19.91%` | `58.18` |
| `Live` | `Long` | `45.05` | 873,460.00 USD | 0.00 USD | 4,830.00 USD | `-19.73%` | `107.31` |
| `Live` | `Long` | `45.15` | 868,620.00 USD | 0.00 USD | 8,710.00 USD | `-19.55%` | `193.00` |
| `Live` | `Long` | `45.25` | 859,910.00 USD | 0.00 USD | 3,180.00 USD | `-19.37%` | `70.37` |
| `Live` | `Long` | `45.35` | 856,720.00 USD | 0.00 USD | 2,180.00 USD | `-19.20%` | `48.02` |
| `Live` | `Long` | `45.45` | 854,550.00 USD | 0.00 USD | 23,940.00 USD | `-19.02%` | `526.65` |
| `Live` | `Long` | `45.55` | 830,610.00 USD | 0.00 USD | 12,060.00 USD | `-18.84%` | `264.81` |
| `Live` | `Long` | `45.65` | 818,550.00 USD | 0.00 USD | 42,180.00 USD | `-18.66%` | `924.03` |
| `Live` | `Long` | `45.75` | 776,370.00 USD | 0.00 USD | 27,480.00 USD | `-18.48%` | `600.68` |
| `Live` | `Long` | `45.85` | 748,880.00 USD | 0.00 USD | 176.06 USD | `-18.30%` | `3.84` |
| `Live` | `Long` | `45.95` | 748,710.00 USD | 0.00 USD | 2,940.00 USD | `-18.13%` | `64.09` |
| `Live` | `Long` | `46.05` | 745,760.00 USD | 0.00 USD | 706.41 USD | `-17.95%` | `15.34` |
| `Live` | `Long` | `46.25` | 745,060.00 USD | 0.00 USD | 22,380.00 USD | `-17.59%` | `483.97` |
| `Live` | `Long` | `46.35` | 722,670.00 USD | 0.00 USD | 383.78 USD | `-17.41%` | `8.28` |
| `Live` | `Long` | `46.55` | 722,290.00 USD | 0.00 USD | 2,140.00 USD | `-17.06%` | `45.93` |
| `Live` | `Long` | `46.65` | 720,150.00 USD | 0.00 USD | 3,980.00 USD | `-16.88%` | `85.41` |
| `Live` | `Long` | `46.75` | 716,170.00 USD | 0.00 USD | 269.28 USD | `-16.70%` | `5.76` |
| `Live` | `Long` | `46.85` | 715,900.00 USD | 0.00 USD | 358.40 USD | `-16.52%` | `7.65` |
| `Live` | `Long` | `46.95` | 715,540.00 USD | 0.00 USD | 533.35 USD | `-16.34%` | `11.36` |
| `Live` | `Long` | `47.15` | 715,010.00 USD | 0.00 USD | 1,980.00 USD | `-15.99%` | `42.07` |
| `Live` | `Long` | `47.25` | 713,020.00 USD | 0.00 USD | 646.85 USD | `-15.81%` | `13.69` |
| `Live` | `Long` | `47.35` | 712,380.00 USD | 0.00 USD | 43,920.00 USD | `-15.63%` | `927.56` |
| `Live` | `Long` | `47.45` | 668,460.00 USD | 0.00 USD | 2,590.00 USD | `-15.45%` | `54.54` |
| `Live` | `Long` | `47.55` | 665,870.00 USD | 0.00 USD | 4,450.00 USD | `-15.28%` | `93.69` |
| `Live` | `Long` | `47.75` | 661,410.00 USD | 0.00 USD | 47,750.00 USD | `-14.92%` | `1,000.00` |
| `Live` | `Long` | `47.95` | 613,660.00 USD | 0.00 USD | 7,890.00 USD | `-14.56%` | `164.58` |
| `Live` | `Long` | `48.05` | 605,770.00 USD | 0.00 USD | 1,340.00 USD | `-14.38%` | `27.93` |
| `Live` | `Long` | `48.15` | 604,430.00 USD | 0.00 USD | 1,690.00 USD | `-14.21%` | `35.03` |
| `Live` | `Long` | `48.25` | 602,740.00 USD | 0.00 USD | 110.49 USD | `-14.03%` | `2.29` |
| `Live` | `Long` | `48.55` | 602,630.00 USD | 0.00 USD | 2,560.00 USD | `-13.49%` | `52.70` |
| `Live` | `Long` | `48.65` | 600,070.00 USD | 0.00 USD | 273.90 USD | `-13.32%` | `5.63` |
| `Live` | `Long` | `48.75` | 599,800.00 USD | 0.00 USD | 2,220.00 USD | `-13.14%` | `45.64` |
| `Live` | `Long` | `48.95` | 597,580.00 USD | 0.00 USD | 252.58 USD | `-12.78%` | `5.16` |
| `Live` | `Long` | `49.05` | 597,320.00 USD | 0.00 USD | 1,580.00 USD | `-12.60%` | `32.25` |
| `Live` | `Long` | `49.15` | 595,740.00 USD | 0.00 USD | 5,740.00 USD | `-12.42%` | `116.83` |
| `Live` | `Long` | `49.35` | 590,000.00 USD | 0.00 USD | 5,230.00 USD | `-12.07%` | `105.97` |
| `Live` | `Long` | `49.45` | 584,770.00 USD | 0.00 USD | 419.34 USD | `-11.89%` | `8.48` |
| `Live` | `Long` | `49.55` | 584,350.00 USD | 0.00 USD | 18,010.00 USD | `-11.71%` | `363.57` |
| `Live` | `Long` | `49.65` | 566,330.00 USD | 0.00 USD | 73,260.00 USD | `-11.53%` | `1,475.52` |
| `Live` | `Long` | `49.75` | 493,080.00 USD | 0.00 USD | 20,710.00 USD | `-11.36%` | `416.36` |
| `Live` | `Long` | `49.95` | 472,360.00 USD | 0.00 USD | 19,920.00 USD | `-11.00%` | `398.70` |
| `Live` | `Long` | `50.05` | 452,450.00 USD | 0.00 USD | 1,820.00 USD | `-10.82%` | `36.43` |
| `Live` | `Long` | `50.25` | 450,620.00 USD | 0.00 USD | 102.51 USD | `-10.46%` | `2.04` |
| `Live` | `Long` | `50.35` | 450,520.00 USD | 0.00 USD | 1,140.00 USD | `-10.29%` | `22.67` |
| `Live` | `Long` | `50.45` | 449,380.00 USD | 0.00 USD | 4,720.00 USD | `-10.11%` | `93.64` |
| `Live` | `Long` | `50.55` | 444,650.00 USD | 0.00 USD | 84,100.00 USD | `-9.93%` | `1,663.61` |
| `Live` | `Long` | `50.75` | 360,560.00 USD | 0.00 USD | 9,050.00 USD | `-9.57%` | `178.28` |
| `Live` | `Long` | `50.95` | 351,510.00 USD | 0.00 USD | 431.55 USD | `-9.22%` | `8.47` |
| `Live` | `Long` | `51.15` | 351,080.00 USD | 0.00 USD | 219,370.00 USD | `-8.86%` | `4,288.79` |
| `Live` | `Long` | `51.25` | 131,710.00 USD | 0.00 USD | 202.44 USD | `-8.68%` | `3.95` |
| `Live` | `Long` | `51.35` | 131,510.00 USD | 0.00 USD | 453.93 USD | `-8.50%` | `8.84` |
| `Live` | `Long` | `51.45` | 131,050.00 USD | 0.00 USD | 27,210.00 USD | `-8.33%` | `528.81` |
| `Live` | `Long` | `51.55` | 103,840.00 USD | 0.00 USD | 551.07 USD | `-8.15%` | `10.69` |
| `Live` | `Long` | `51.65` | 103,290.00 USD | 0.00 USD | 9,100.00 USD | `-7.97%` | `176.09` |
| `Live` | `Long` | `51.75` | 94,200.00 USD | 0.00 USD | 6,480.00 USD | `-7.79%` | `125.17` |
| `Live` | `Long` | `51.85` | 87,720.00 USD | 0.00 USD | 16,530.00 USD | `-7.61%` | `318.89` |
| `Live` | `Long` | `51.95` | 71,190.00 USD | 0.00 USD | 13,950.00 USD | `-7.44%` | `268.48` |
| `Live` | `Long` | `52.15` | 57,240.00 USD | 0.00 USD | 1,900.00 USD | `-7.08%` | `36.36` |
| `Live` | `Long` | `52.25` | 55,340.00 USD | 0.00 USD | 4,930.00 USD | `-6.90%` | `94.33` |
| `Live` | `Long` | `52.35` | 50,410.00 USD | 0.00 USD | 134.02 USD | `-6.72%` | `2.56` |
| `Live` | `Long` | `52.45` | 50,280.00 USD | 0.00 USD | 2,470.00 USD | `-6.54%` | `47.16` |
| `Live` | `Long` | `52.55` | 47,810.00 USD | 0.00 USD | 8,700.00 USD | `-6.37%` | `165.49` |
| `Live` | `Long` | `52.75` | 39,110.00 USD | 0.00 USD | 4,240.00 USD | `-6.01%` | `80.44` |
| `Live` | `Long` | `52.85` | 34,870.00 USD | 0.00 USD | 5,950.00 USD | `-5.83%` | `112.64` |
| `Live` | `Long` | `52.95` | 28,910.00 USD | 0.00 USD | 25,840.00 USD | `-5.65%` | `488.06` |
| `Live` | `Long` | `53.15` | 3,070.00 USD | 0.00 USD | 1,720.00 USD | `-5.30%` | `32.44` |
| `Live` | `Long` | `53.25` | 1,350.00 USD | 0.00 USD | 405.76 USD | `-5.12%` | `7.62` |
| `Live` | `Long` | `53.35` | 941.09 USD | 0.00 USD | 941.09 USD | `-4.94%` | `17.64` |
| `Live` | `Short` | `57.75` | 155.35 USD | 155.35 USD | 0.00 USD | `+2.90%` | `2.69` |
| `Live` | `Short` | `57.95` | 281.10 USD | 125.75 USD | 0.00 USD | `+3.26%` | `2.17` |
| `Live` | `Short` | `59.35` | 9,720.00 USD | 9,440.00 USD | 0.00 USD | `+5.75%` | `159.09` |
| `Live` | `Short` | `60.15` | 218,600.00 USD | 208,880.00 USD | 0.00 USD | `+7.18%` | `3,472.67` |
| `Live` | `Short` | `60.95` | 219,000.00 USD | 397.39 USD | 0.00 USD | `+8.60%` | `6.52` |
| `Live` | `Short` | `62.95` | 219,140.00 USD | 138.49 USD | 0.00 USD | `+12.16%` | `2.20` |
| `Live` | `Short` | `63.45` | 222,490.00 USD | 3,350.00 USD | 0.00 USD | `+13.06%` | `52.83` |
| `Live` | `Short` | `63.55` | 230,670.00 USD | 8,180.00 USD | 0.00 USD | `+13.23%` | `128.67` |
| `Live` | `Short` | `66.95` | 230,790.00 USD | 121.18 USD | 0.00 USD | `+19.29%` | `1.81` |
| `Live` | `Short` | `67.85` | 231,500.00 USD | 709.03 USD | 0.00 USD | `+20.90%` | `10.45` |
| `Live` | `Short` | `70.55` | 272,280.00 USD | 40,780.00 USD | 0.00 USD | `+25.71%` | `578.10` |
| `Live` | `Short` | `71.35` | 272,400.00 USD | 112.02 USD | 0.00 USD | `+27.13%` | `1.57` |
| `Live` | `Short` | `76.35` | 280,780.00 USD | 8,380.00 USD | 0.00 USD | `+36.04%` | `109.80` |
| `Live` | `Short` | `77.75` | 859,240.00 USD | 578,460.00 USD | 0.00 USD | `+38.54%` | `7,440.05` |
| `Live` | `Short` | `77.85` | 859,850.00 USD | 602.56 USD | 0.00 USD | `+38.71%` | `7.74` |
| `Live` | `Short` | `77.95` | 859,980.00 USD | 136.41 USD | 0.00 USD | `+38.89%` | `1.75` |
| `Live` | `Short` | `80.75` | 860,630.00 USD | 646.00 USD | 0.00 USD | `+43.88%` | `8.00` |
| `Live` | `Short` | `81.05` | 879,630.00 USD | 19,000.00 USD | 0.00 USD | `+44.41%` | `234.42` |
| `Live` | `Short` | `81.55` | 879,750.00 USD | 123.96 USD | 0.00 USD | `+45.31%` | `1.52` |
| `Live` | `Short` | `82.45` | 883,050.00 USD | 3,300.00 USD | 0.00 USD | `+46.91%` | `40.00` |
| `Live` | `Short` | `82.75` | 883,260.00 USD | 214.32 USD | 0.00 USD | `+47.44%` | `2.59` |
| `Live` | `Short` | `84.35` | 886,050.00 USD | 2,780.00 USD | 0.00 USD | `+50.29%` | `33.00` |
| `Live` | `Short` | `85.75` | 886,830.00 USD | 777.75 USD | 0.00 USD | `+52.79%` | `9.07` |
| `Live` | `Short` | `87.45` | 910,160.00 USD | 23,330.00 USD | 0.00 USD | `+55.82%` | `266.81` |
| `Live` | `Short` | `88.45` | 910,280.00 USD | 116.75 USD | 0.00 USD | `+57.60%` | `1.32` |
| `Live` | `Short` | `89.55` | 911,230.00 USD | 951.92 USD | 0.00 USD | `+59.56%` | `10.63` |
| `Live` | `Short` | `90.35` | 911,330.00 USD | 101.19 USD | 0.00 USD | `+60.99%` | `1.12` |
| `Live` | `Short` | `91.95` | 911,480.00 USD | 155.40 USD | 0.00 USD | `+63.84%` | `1.69` |
| `Live` | `Short` | `97.85` | 913,930.00 USD | 2,450.00 USD | 0.00 USD | `+74.35%` | `25.00` |
| `Live` | `Short` | `103.35` | 944,930.00 USD | 31,010.00 USD | 0.00 USD | `+84.15%` | `300.00` |
| `Live` | `Short` | `104.25` | 945,150.00 USD | 213.71 USD | 0.00 USD | `+85.75%` | `2.05` |
| `Live` | `Short` | `104.85` | 947,470.00 USD | 2,320.00 USD | 0.00 USD | `+86.82%` | `22.13` |
| `Live` | `Short` | `105.55` | 1,300,000.00 USD | 356,130.00 USD | 0.00 USD | `+88.07%` | `3,374.01` |
| `Live` | `Short` | `106.75` | 1,310,000.00 USD | 1,620.00 USD | 0.00 USD | `+90.21%` | `15.16` |
| `Live` | `Short` | `106.85` | 1,310,000.00 USD | 1,860.00 USD | 0.00 USD | `+90.39%` | `17.43` |
| `Live` | `Short` | `107.15` | 1,310,000.00 USD | 199.30 USD | 0.00 USD | `+90.92%` | `1.86` |
| `Live` | `Short` | `108.05` | 1,310,000.00 USD | 6,470.00 USD | 0.00 USD | `+92.52%` | `59.91` |
| `Live` | `Short` | `110.95` | 1,310,000.00 USD | 664.59 USD | 0.00 USD | `+97.69%` | `5.99` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 821,330.00 USD | 0.00 USD | 392.18 USD | `-64.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 820,940.00 USD | 0.00 USD | 2,310.00 USD | `-60.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 818,630.00 USD | 0.00 USD | 806.86 USD | `-55.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 817,820.00 USD | 0.00 USD | 1,560.00 USD | `-54.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 816,260.00 USD | 0.00 USD | 410.25 USD | `-51.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 815,850.00 USD | 0.00 USD | 281.57 USD | `-46.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 815,570.00 USD | 0.00 USD | 36,050.00 USD | `-35.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 779,520.00 USD | 0.00 USD | 37,550.00 USD | `-33.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 741,970.00 USD | 0.00 USD | 447.01 USD | `-32.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.35` | 741,530.00 USD | 0.00 USD | 73,350.00 USD | `-31.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 668,180.00 USD | 0.00 USD | 40,560.00 USD | `-30.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 627,620.00 USD | 0.00 USD | 489.57 USD | `-29.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 627,130.00 USD | 0.00 USD | 1,180.00 USD | `-28.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 625,950.00 USD | 0.00 USD | 9,840.00 USD | `-28.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 616,110.00 USD | 0.00 USD | 2,060.00 USD | `-27.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.05` | 614,060.00 USD | 0.00 USD | 2,060.00 USD | `-26.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 612,000.00 USD | 0.00 USD | 2,960.00 USD | `-25.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 609,040.00 USD | 0.00 USD | 4,010.00 USD | `-25.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.65` | 605,030.00 USD | 0.00 USD | 3,000.00 USD | `-24.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 602,020.00 USD | 0.00 USD | 5,680.00 USD | `-23.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 596,340.00 USD | 0.00 USD | 672.22 USD | `-21.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.35` | 595,670.00 USD | 0.00 USD | 329,970.00 USD | `-20.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 265,710.00 USD | 0.00 USD | 213.80 USD | `-20.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 265,490.00 USD | 0.00 USD | 223.20 USD | `-20.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 265,270.00 USD | 0.00 USD | 391.13 USD | `-20.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 264,880.00 USD | 0.00 USD | 7,080.00 USD | `-19.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 257,800.00 USD | 0.00 USD | 1,370.00 USD | `-18.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 256,430.00 USD | 0.00 USD | 553.80 USD | `-17.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.35` | 255,880.00 USD | 0.00 USD | 2,970.00 USD | `-17.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.45` | 252,910.00 USD | 0.00 USD | 3,080.00 USD | `-17.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 249,830.00 USD | 0.00 USD | 14,000.00 USD | `-16.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 235,840.00 USD | 0.00 USD | 158.56 USD | `-16.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 235,680.00 USD | 0.00 USD | 373.28 USD | `-15.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 235,310.00 USD | 0.00 USD | 849.46 USD | `-15.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 234,460.00 USD | 0.00 USD | 1,150.00 USD | `-14.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 233,310.00 USD | 0.00 USD | 129.25 USD | `-14.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.15` | 233,180.00 USD | 0.00 USD | 303.35 USD | `-14.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 232,870.00 USD | 0.00 USD | 1,740.00 USD | `-12.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 231,130.00 USD | 0.00 USD | 981.00 USD | `-12.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.35` | 230,150.00 USD | 0.00 USD | 817.24 USD | `-12.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 229,330.00 USD | 0.00 USD | 237.85 USD | `-11.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.55` | 229,100.00 USD | 0.00 USD | 1,420.00 USD | `-11.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.85` | 227,680.00 USD | 0.00 USD | 108.17 USD | `-11.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 227,570.00 USD | 0.00 USD | 298.20 USD | `-11.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 227,270.00 USD | 0.00 USD | 35,050.00 USD | `-10.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 192,230.00 USD | 0.00 USD | 6,410.00 USD | `-10.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 185,810.00 USD | 0.00 USD | 459.70 USD | `-10.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 185,350.00 USD | 0.00 USD | 236.57 USD | `-9.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 185,110.00 USD | 0.00 USD | 1,020.00 USD | `-9.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 184,090.00 USD | 0.00 USD | 439.89 USD | `-8.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.45` | 183,650.00 USD | 0.00 USD | 204.26 USD | `-8.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 183,450.00 USD | 0.00 USD | 11,560.00 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.85` | 171,890.00 USD | 0.00 USD | 106.29 USD | `-7.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.95` | 171,780.00 USD | 0.00 USD | 8,700.00 USD | `-7.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 163,080.00 USD | 0.00 USD | 27,140.00 USD | `-7.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.25` | 135,940.00 USD | 0.00 USD | 140.03 USD | `-6.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 135,800.00 USD | 0.00 USD | 70,190.00 USD | `-6.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 65,610.00 USD | 0.00 USD | 5,460.00 USD | `-6.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 60,150.00 USD | 0.00 USD | 271.13 USD | `-6.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.85` | 59,880.00 USD | 0.00 USD | 2,840.00 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 57,040.00 USD | 0.00 USD | 115.43 USD | `-5.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 56,920.00 USD | 0.00 USD | 15,140.00 USD | `-5.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 41,780.00 USD | 0.00 USD | 2,660.00 USD | `-5.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.25` | 39,120.00 USD | 0.00 USD | 881.82 USD | `-5.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 38,240.00 USD | 0.00 USD | 566.57 USD | `-4.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 37,680.00 USD | 0.00 USD | 5,950.00 USD | `-4.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 31,730.00 USD | 0.00 USD | 1,370.00 USD | `-4.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.75` | 30,360.00 USD | 0.00 USD | 1,120.00 USD | `-4.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 29,230.00 USD | 0.00 USD | 462.03 USD | `-4.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 28,770.00 USD | 0.00 USD | 895.07 USD | `-3.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.15` | 27,880.00 USD | 0.00 USD | 398.54 USD | `-3.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 27,480.00 USD | 0.00 USD | 3,090.00 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 24,390.00 USD | 0.00 USD | 958.73 USD | `-3.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.45` | 23,430.00 USD | 0.00 USD | 144.29 USD | `-2.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.55` | 23,290.00 USD | 0.00 USD | 1,690.00 USD | `-2.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.65` | 21,600.00 USD | 0.00 USD | 13,660.00 USD | `-2.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.75` | 7,930.00 USD | 0.00 USD | 198.74 USD | `-2.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 7,730.00 USD | 0.00 USD | 398.21 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.95` | 7,340.00 USD | 0.00 USD | 397.84 USD | `-2.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 6,940.00 USD | 0.00 USD | 160.75 USD | `-1.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.15` | 6,780.00 USD | 0.00 USD | 101.48 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.25` | 6,680.00 USD | 0.00 USD | 914.94 USD | `-1.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.35` | 5,760.00 USD | 0.00 USD | 407.38 USD | `-1.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.45` | 5,350.00 USD | 0.00 USD | 408.11 USD | `-1.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.55` | 4,950.00 USD | 0.00 USD | 156.65 USD | `-1.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.65` | 4,790.00 USD | 0.00 USD | 3,610.00 USD | `-0.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.75` | 1,180.00 USD | 0.00 USD | 202.37 USD | `-0.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.85` | 974.95 USD | 0.00 USD | 149.68 USD | `-0.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.95` | 825.27 USD | 0.00 USD | 193.03 USD | `-0.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 632.24 USD | 0.00 USD | 632.24 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.15` | 197.65 USD | 197.65 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.25` | 401.84 USD | 204.19 USD | 0.00 USD | `+0.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.35` | 788.96 USD | 387.12 USD | 0.00 USD | `+0.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.45` | 1,200.00 USD | 407.57 USD | 0.00 USD | `+0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.55` | 3,830.00 USD | 2,640.00 USD | 0.00 USD | `+0.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.65` | 3,960.00 USD | 121.23 USD | 0.00 USD | `+0.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.75` | 4,060.00 USD | 104.42 USD | 0.00 USD | `+1.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.85` | 22,090.00 USD | 18,030.00 USD | 0.00 USD | `+1.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.95` | 22,480.00 USD | 390.68 USD | 0.00 USD | `+1.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.15` | 22,870.00 USD | 392.05 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.25` | 23,070.00 USD | 201.52 USD | 0.00 USD | `+2.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.35` | 23,280.00 USD | 207.03 USD | 0.00 USD | `+2.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.45` | 23,620.00 USD | 344.70 USD | 0.00 USD | `+2.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.55` | 43,980.00 USD | 20,360.00 USD | 0.00 USD | `+2.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.65` | 44,100.00 USD | 118.18 USD | 0.00 USD | `+2.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.75` | 44,220.00 USD | 119.54 USD | 0.00 USD | `+2.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 44,970.00 USD | 747.68 USD | 0.00 USD | `+3.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 45,170.00 USD | 200.04 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 45,370.00 USD | 200.96 USD | 0.00 USD | `+3.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 45,490.00 USD | 123.70 USD | 0.00 USD | `+3.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 46,090.00 USD | 601.45 USD | 0.00 USD | `+4.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 46,710.00 USD | 611.85 USD | 0.00 USD | `+4.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.65` | 46,980.00 USD | 274.48 USD | 0.00 USD | `+4.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 47,470.00 USD | 491.15 USD | 0.00 USD | `+4.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 50,410.00 USD | 2,940.00 USD | 0.00 USD | `+4.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 50,540.00 USD | 129.69 USD | 0.00 USD | `+5.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 55,340.00 USD | 4,800.00 USD | 0.00 USD | `+5.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 56,620.00 USD | 1,280.00 USD | 0.00 USD | `+5.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.25` | 56,830.00 USD | 210.34 USD | 0.00 USD | `+5.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 57,300.00 USD | 461.74 USD | 0.00 USD | `+5.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 57,460.00 USD | 159.92 USD | 0.00 USD | `+5.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.55` | 57,950.00 USD | 496.65 USD | 0.00 USD | `+6.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 58,680.00 USD | 724.75 USD | 0.00 USD | `+6.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 58,840.00 USD | 158.00 USD | 0.00 USD | `+6.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 59,010.00 USD | 171.14 USD | 0.00 USD | `+7.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 59,560.00 USD | 551.00 USD | 0.00 USD | `+7.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.45` | 59,710.00 USD | 155.36 USD | 0.00 USD | `+7.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 60,590.00 USD | 878.58 USD | 0.00 USD | `+7.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 61,980.00 USD | 1,390.00 USD | 0.00 USD | `+8.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 62,960.00 USD | 986.99 USD | 0.00 USD | `+8.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 63,640.00 USD | 674.72 USD | 0.00 USD | `+8.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 66,000.00 USD | 2,360.00 USD | 0.00 USD | `+8.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 66,130.00 USD | 125.56 USD | 0.00 USD | `+9.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 69,720.00 USD | 3,600.00 USD | 0.00 USD | `+9.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 70,370.00 USD | 643.20 USD | 0.00 USD | `+9.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 70,500.00 USD | 130.31 USD | 0.00 USD | `+10.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.35` | 71,600.00 USD | 1,100.00 USD | 0.00 USD | `+11.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 72,310.00 USD | 716.72 USD | 0.00 USD | `+11.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 72,540.00 USD | 231.39 USD | 0.00 USD | `+12.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 73,180.00 USD | 630.87 USD | 0.00 USD | `+12.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 73,880.00 USD | 703.97 USD | 0.00 USD | `+12.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 74,550.00 USD | 668.13 USD | 0.00 USD | `+13.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 84,970.00 USD | 10,420.00 USD | 0.00 USD | `+13.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 85,520.00 USD | 555.03 USD | 0.00 USD | `+13.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 86,060.00 USD | 531.62 USD | 0.00 USD | `+14.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.35` | 86,720.00 USD | 664.09 USD | 0.00 USD | `+14.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.45` | 87,380.00 USD | 665.12 USD | 0.00 USD | `+14.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 87,590.00 USD | 202.69 USD | 0.00 USD | `+15.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 87,890.00 USD | 298.04 USD | 0.00 USD | `+15.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 87,990.00 USD | 102.13 USD | 0.00 USD | `+15.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 88,530.00 USD | 540.09 USD | 0.00 USD | `+16.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 88,630.00 USD | 100.79 USD | 0.00 USD | `+16.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 88,890.00 USD | 262.20 USD | 0.00 USD | `+16.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 89,260.00 USD | 371.49 USD | 0.00 USD | `+17.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 89,960.00 USD | 696.17 USD | 0.00 USD | `+17.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 90,490.00 USD | 534.00 USD | 0.00 USD | `+18.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 101,570.00 USD | 11,080.00 USD | 0.00 USD | `+19.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 108,280.00 USD | 6,710.00 USD | 0.00 USD | `+19.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.05` | 110,640.00 USD | 2,360.00 USD | 0.00 USD | `+21.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 115,500.00 USD | 4,860.00 USD | 0.00 USD | `+21.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 115,710.00 USD | 204.48 USD | 0.00 USD | `+23.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.65` | 633,900.00 USD | 518,200.00 USD | 0.00 USD | `+24.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 634,710.00 USD | 810.02 USD | 0.00 USD | `+24.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 954,610.00 USD | 319,890.00 USD | 0.00 USD | `+24.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 954,780.00 USD | 170.04 USD | 0.00 USD | `+26.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 960,550.00 USD | 5,770.00 USD | 0.00 USD | `+26.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 960,810.00 USD | 269.28 USD | 0.00 USD | `+26.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 961,110.00 USD | 291.40 USD | 0.00 USD | `+28.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 968,320.00 USD | 7,220.00 USD | 0.00 USD | `+28.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 968,480.00 USD | 156.78 USD | 0.00 USD | `+28.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 971,700.00 USD | 3,220.00 USD | 0.00 USD | `+29.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 972,110.00 USD | 411.14 USD | 0.00 USD | `+31.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 1,100,000.00 USD | 123,190.00 USD | 0.00 USD | `+31.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 1,100,000.00 USD | 1,020.00 USD | 0.00 USD | `+32.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.75` | 1,100,000.00 USD | 811.04 USD | 0.00 USD | `+33.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 1,100,000.00 USD | 104.93 USD | 0.00 USD | `+33.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 1,100,000.00 USD | 133.59 USD | 0.00 USD | `+33.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 1,100,000.00 USD | 402.59 USD | 0.00 USD | `+34.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.85` | 1,100,000.00 USD | 308.71 USD | 0.00 USD | `+35.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 1,100,000.00 USD | 315.18 USD | 0.00 USD | `+37.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 1,160,000.00 USD | 59,310.00 USD | 0.00 USD | `+40.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 1,160,000.00 USD | 3,160.00 USD | 0.00 USD | `+40.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.35` | 1,170,000.00 USD | 5,260.00 USD | 0.00 USD | `+41.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 1,170,000.00 USD | 5,690.00 USD | 0.00 USD | `+42.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 1,210,000.00 USD | 36,590.00 USD | 0.00 USD | `+42.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 1,210,000.00 USD | 433.89 USD | 0.00 USD | `+44.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 1,210,000.00 USD | 172.64 USD | 0.00 USD | `+44.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 1,210,000.00 USD | 164.10 USD | 0.00 USD | `+46.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 1,210,000.00 USD | 546.81 USD | 0.00 USD | `+47.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 1,210,000.00 USD | 2,300.00 USD | 0.00 USD | `+49.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 1,220,000.00 USD | 12,070.00 USD | 0.00 USD | `+51.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.05` | 1,240,000.00 USD | 20,230.00 USD | 0.00 USD | `+55.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 1,250,000.00 USD | 1,580.00 USD | 0.00 USD | `+56.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 1,280,000.00 USD | 37,000.00 USD | 0.00 USD | `+56.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 1,280,000.00 USD | 473.21 USD | 0.00 USD | `+58.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 1,280,000.00 USD | 422.99 USD | 0.00 USD | `+58.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 1,290,000.00 USD | 1,630.00 USD | 0.00 USD | `+59.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 1,290,000.00 USD | 4,870.00 USD | 0.00 USD | `+60.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 1,290,000.00 USD | 481.55 USD | 0.00 USD | `+63.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 1,290,000.00 USD | 1,330.00 USD | 0.00 USD | `+64.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 1,290,000.00 USD | 205.97 USD | 0.00 USD | `+67.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,560,000.00 USD | 266,140.00 USD | 0.00 USD | `+69.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,560,000.00 USD | 3,400.00 USD | 0.00 USD | `+69.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,580,000.00 USD | 21,930.00 USD | 0.00 USD | `+71.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,580,000.00 USD | 294.15 USD | 0.00 USD | `+74.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 1,600,000.00 USD | 15,380.00 USD | 0.00 USD | `+76.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,600,000.00 USD | 3,660.00 USD | 0.00 USD | `+78.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,600,000.00 USD | 306.15 USD | 0.00 USD | `+81.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,600,000.00 USD | 936.72 USD | 0.00 USD | `+83.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,610,000.00 USD | 2,920.00 USD | 0.00 USD | `+83.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,610,000.00 USD | 324.15 USD | 0.00 USD | `+92.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 1,610,000.00 USD | 123.23 USD | 0.00 USD | `+94.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 1,700,000.00 USD | 89,110.00 USD | 0.00 USD | `+97.87%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `47.10` | 9,260,000.00 USD | 0.00 USD | 9,260,000.00 USD | 16,740.00 USD | 12,890.00 USD | 0.00 USD |
| `7D` | `47.20` | 9,230,000.00 USD | 0.00 USD | 9,230,000.00 USD | 8,940.00 USD | 1,090.00 USD | 114.09 USD |
| `7D` | `47.30` | 9,220,000.00 USD | 0.00 USD | 9,220,000.00 USD | 692.33 USD | 4,740.00 USD | 6,740.00 USD |
| `7D` | `47.40` | 9,200,000.00 USD | 0.00 USD | 9,200,000.00 USD | 0.00 USD | 1,520.00 USD | 28,650.00 USD |
| `7D` | `47.50` | 9,170,000.00 USD | 0.00 USD | 9,170,000.00 USD | 11,830.00 USD | 0.00 USD | 7,960.00 USD |
| `7D` | `48.10` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD |
| `7D` | `48.20` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD |
| `7D` | `48.40` | 9,140,000.00 USD | 0.00 USD | 9,140,000.00 USD | 0.00 USD | 6,080.00 USD | 0.00 USD |
| `7D` | `48.60` | 9,140,000.00 USD | 0.00 USD | 9,140,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `48.80` | 9,130,000.00 USD | 0.00 USD | 9,130,000.00 USD | 1,780.00 USD | 2,250.00 USD | 0.00 USD |
| `7D` | `48.90` | 9,130,000.00 USD | 0.00 USD | 9,130,000.00 USD | 0.00 USD | 0.00 USD | 960.40 USD |
| `7D` | `49.30` | 9,130,000.00 USD | 0.00 USD | 9,130,000.00 USD | 15,190.00 USD | 4,490.00 USD | 14,870.00 USD |
| `7D` | `49.40` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD |
| `7D` | `49.50` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 2,830.00 USD | 7,770.00 USD | 0.00 USD |
| `7D` | `49.60` | 9,080,000.00 USD | 0.00 USD | 9,080,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD |
| `7D` | `49.70` | 9,060,000.00 USD | 0.00 USD | 9,060,000.00 USD | 12,090.00 USD | 0.00 USD | 5,410.00 USD |
| `7D` | `49.80` | 9,040,000.00 USD | 0.00 USD | 9,040,000.00 USD | 9,930.00 USD | 8,220.00 USD | 0.00 USD |
| `7D` | `49.90` | 9,030,000.00 USD | 0.00 USD | 9,030,000.00 USD | 45,030.00 USD | 7,170.00 USD | 4,700.00 USD |
| `7D` | `50.00` | 8,970,000.00 USD | 0.00 USD | 8,970,000.00 USD | 22,100.00 USD | 7,630.00 USD | 24,920.00 USD |
| `7D` | `50.10` | 8,910,000.00 USD | 0.00 USD | 8,910,000.00 USD | 363.50 USD | 682.90 USD | 8,340.00 USD |
| `1D` | `50.20` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 4,490.00 USD | 5,820.00 USD | 3,500.00 USD |
| `7D` | `50.20` | 8,900,000.00 USD | 0.00 USD | 8,900,000.00 USD | 6,960.00 USD | 500.40 USD | 34,680.00 USD |
| `1D` | `50.30` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 171.03 USD | 1,290.00 USD | 2,390.00 USD |
| `7D` | `50.30` | 8,860,000.00 USD | 0.00 USD | 8,860,000.00 USD | 16,270.00 USD | 3,640.00 USD | 1,950.00 USD |
| `1D` | `50.40` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 4,370.00 USD | 3,070.00 USD | 0.00 USD |
| `7D` | `50.40` | 8,840,000.00 USD | 0.00 USD | 8,840,000.00 USD | 28,280.00 USD | 20,470.00 USD | 33,450.00 USD |
| `1D` | `50.50` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 5,790.00 USD | 2,110.00 USD | 5,950.00 USD |
| `7D` | `50.50` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 32,450.00 USD | 6,790.00 USD | 44,160.00 USD |
| `1D` | `50.60` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 1,660.00 USD | 2,640.00 USD | 9,380.00 USD |
| `7D` | `50.60` | 8,670,000.00 USD | 0.00 USD | 8,670,000.00 USD | 56,670.00 USD | 21,530.00 USD | 31,730.00 USD |
| `1D` | `50.70` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 4,820.00 USD | 1,440.00 USD | 11,700.00 USD |
| `7D` | `50.70` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 65,150.00 USD | 32,820.00 USD | 41,580.00 USD |
| `1D` | `50.80` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 12,550.00 USD | 3,100.00 USD | 8,280.00 USD |
| `7D` | `50.80` | 8,430,000.00 USD | 0.00 USD | 8,430,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD |
| `1D` | `50.90` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 826.24 USD | 260.05 USD | 8,390.00 USD |
| `7D` | `50.90` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD |
| `1D` | `51.00` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 5,040.00 USD | 0.00 USD | 430.77 USD |
| `7D` | `51.00` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `51.10` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 9,210.00 USD | 6,560.00 USD | 0.00 USD |
| `7D` | `51.10` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD |
| `1D` | `51.20` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 2,360.00 USD | 1,130.00 USD | 17,310.00 USD |
| `7D` | `51.20` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD |
| `1D` | `51.30` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 16,790.00 USD | 14,100.00 USD | 10,670.00 USD |
| `7D` | `51.30` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 28,400.00 USD | 26,720.00 USD | 47,090.00 USD |
| `1D` | `51.40` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 13,750.00 USD | 11,490.00 USD | 4,890.00 USD |
| `7D` | `51.40` | 7,700,000.00 USD | 0.00 USD | 7,700,000.00 USD | 73,130.00 USD | 42,820.00 USD | 46,140.00 USD |
| `1D` | `51.50` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 7,880.00 USD | 10,980.00 USD | 37,710.00 USD |
| `7D` | `51.50` | 7,540,000.00 USD | 0.00 USD | 7,540,000.00 USD | 38,520.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `51.60` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 9,060.00 USD | 18,490.00 USD | 757.87 USD |
| `7D` | `51.60` | 7,440,000.00 USD | 0.00 USD | 7,440,000.00 USD | 37,880.00 USD | 36,790.00 USD | 41,490.00 USD |
| `1D` | `51.70` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 2,890.00 USD | 13,810.00 USD | 21,320.00 USD |
| `7D` | `51.70` | 7,320,000.00 USD | 0.00 USD | 7,320,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `51.80` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 12,590.00 USD | 19,270.00 USD | 14,170.00 USD |
| `7D` | `51.80` | 7,290,000.00 USD | 0.00 USD | 7,290,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD |
| `1D` | `51.90` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 9,460.00 USD | 19,910.00 USD | 23,480.00 USD |
| `7D` | `51.90` | 7,230,000.00 USD | 0.00 USD | 7,230,000.00 USD | 5,870.00 USD | 25,410.00 USD | 28,190.00 USD |
| `1D` | `52.00` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 20,980.00 USD | 25,480.00 USD | 25,740.00 USD |
| `7D` | `52.00` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 64,300.00 USD | 26,440.00 USD | 11,880.00 USD |
| `1D` | `52.10` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 34,880.00 USD | 17,130.00 USD | 50,300.00 USD |
| `7D` | `52.10` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 24,220.00 USD | 28,090.00 USD | 37,880.00 USD |
| `1D` | `52.20` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 15,020.00 USD | 7,630.00 USD | 46,100.00 USD |
| `7D` | `52.20` | 6,980,000.00 USD | 0.00 USD | 6,980,000.00 USD | 38,380.00 USD | 13,960.00 USD | 25,270.00 USD |
| `1D` | `52.30` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 26,510.00 USD | 21,640.00 USD | 11,210.00 USD |
| `7D` | `52.30` | 6,900,000.00 USD | 0.00 USD | 6,900,000.00 USD | 24,840.00 USD | 41,300.00 USD | 8,940.00 USD |
| `1D` | `52.40` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 12,460.00 USD | 15,120.00 USD | 7,040.00 USD |
| `7D` | `52.40` | 6,830,000.00 USD | 0.00 USD | 6,830,000.00 USD | 20,580.00 USD | 38,950.00 USD | 22,030.00 USD |
| `1D` | `52.50` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 53,350.00 USD | 29,580.00 USD | 74,280.00 USD |
| `7D` | `52.50` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 38,720.00 USD | 667.05 USD | 11,240.00 USD |
| `1D` | `52.60` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 8,330.00 USD | 40,700.00 USD | 717.10 USD |
| `7D` | `52.60` | 6,690,000.00 USD | 0.00 USD | 6,690,000.00 USD | 74,610.00 USD | 32,590.00 USD | 59,410.00 USD |
| `1D` | `52.70` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 16,690.00 USD | 19,440.00 USD | 28,640.00 USD |
| `7D` | `52.70` | 6,530,000.00 USD | 0.00 USD | 6,530,000.00 USD | 20,250.00 USD | 92,920.00 USD | 108,640.00 USD |
| `1D` | `52.80` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 27,090.00 USD | 50,290.00 USD | 102,590.00 USD |
| `7D` | `52.80` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 39,200.00 USD | 35,280.00 USD | 0.00 USD |
| `1D` | `52.90` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 43,760.00 USD | 50,040.00 USD | 26,190.00 USD |
| `7D` | `52.90` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 39,680.00 USD | 28,710.00 USD | 34,400.00 USD |
| `1D` | `53.00` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 26,670.00 USD | 30,500.00 USD | 39,600.00 USD |
| `7D` | `53.00` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 39,690.00 USD | 25,810.00 USD | 81,210.00 USD |
| `1D` | `53.10` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 14,570.00 USD | 42,760.00 USD | 87,010.00 USD |
| `7D` | `53.10` | 5,980,000.00 USD | 0.00 USD | 5,980,000.00 USD | 45,320.00 USD | 17,950.00 USD | 0.00 USD |
| `1D` | `53.20` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 24,240.00 USD | 6,510.00 USD | 41,660.00 USD |
| `7D` | `53.20` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 162,460.00 USD | 28,320.00 USD | 23,350.00 USD |
| `1D` | `53.30` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 4,060.00 USD | 0.00 USD | 5,610.00 USD |
| `7D` | `53.30` | 5,700,000.00 USD | 0.00 USD | 5,700,000.00 USD | 57,250.00 USD | 24,540.00 USD | 34,820.00 USD |
| `1D` | `53.40` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 3,460.00 USD | 1,850.00 USD | 657.14 USD |
| `7D` | `53.40` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 44,030.00 USD | 7,250.00 USD | 91,220.00 USD |
| `1D` | `53.50` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 9,110.00 USD | 3,940.00 USD | 2,990.00 USD |
| `7D` | `53.50` | 5,440,000.00 USD | 0.00 USD | 5,440,000.00 USD | 48,660.00 USD | 3,440.00 USD | 20,840.00 USD |
| `1D` | `53.60` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 72,650.00 USD | 220.65 USD | 13,180.00 USD |
| `7D` | `53.60` | 5,370,000.00 USD | 0.00 USD | 5,370,000.00 USD | 52,800.00 USD | 1,980.00 USD | 0.00 USD |
| `1D` | `53.70` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 6,210.00 USD | 2,400.00 USD | 6,030.00 USD |
| `7D` | `53.70` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 131,400.00 USD | 3,480.00 USD | 0.00 USD |
| `1D` | `53.80` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 44,920.00 USD | 3,640.00 USD | 250.42 USD |
| `7D` | `53.80` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 99,150.00 USD | 17,260.00 USD | 0.00 USD |
| `1D` | `53.90` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 43,240.00 USD | 18,200.00 USD | 15,150.00 USD |
| `7D` | `53.90` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 148,940.00 USD | 21,360.00 USD | 1,130.00 USD |
| `1D` | `54.00` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 45,350.00 USD | 15,370.00 USD | 68,320.00 USD |
| `7D` | `54.00` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 353,050.00 USD | 71,820.00 USD | 296,180.00 USD |
| `1D` | `54.10` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 91,490.00 USD | 19,160.00 USD | 45,460.00 USD |
| `7D` | `54.10` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 302,190.00 USD | 0.00 USD | 2,590.00 USD |
| `1D` | `54.20` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 72,600.00 USD | 15,510.00 USD | 40,120.00 USD |
| `7D` | `54.20` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 205,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `54.30` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 15,600.00 USD | 0.00 USD | 5,350.00 USD |
| `7D` | `54.30` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 381,380.00 USD | 0.00 USD | 181,420.00 USD |
| `1D` | `54.40` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 51,570.00 USD | 35,500.00 USD | 3,130.00 USD |
| `7D` | `54.40` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 304,270.00 USD | 13,830.00 USD | 92,140.00 USD |
| `1D` | `54.50` | 976,600.00 USD | 0.00 USD | 976,600.00 USD | 9,670.00 USD | 46,240.00 USD | 1,310.00 USD |
| `7D` | `54.50` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 159,720.00 USD | 15,240.00 USD | 239,890.00 USD |
| `1D` | `54.60` | 919,370.00 USD | 0.00 USD | 919,370.00 USD | 913.17 USD | 21,680.00 USD | 5,570.00 USD |
| `7D` | `54.60` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 0.00 USD | 1,930.00 USD | 116,060.00 USD |
| `1D` | `54.70` | 891,210.00 USD | 0.00 USD | 891,210.00 USD | 0.00 USD | 15,420.00 USD | 82,460.00 USD |
| `1D` | `54.80` | 793,340.00 USD | 0.00 USD | 793,340.00 USD | 0.00 USD | 30,590.00 USD | 12,050.00 USD |
| `1D` | `54.90` | 750,690.00 USD | 0.00 USD | 750,690.00 USD | 49,450.00 USD | 14,710.00 USD | 1,690.00 USD |
| `7D` | `54.90` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 0.00 USD | 58,990.00 USD | 47,680.00 USD |
| `1D` | `55.00` | 684,840.00 USD | 0.00 USD | 684,840.00 USD | 25,080.00 USD | 11,440.00 USD | 59,500.00 USD |
| `7D` | `55.00` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 73,940.00 USD | 0.00 USD | 2,260.00 USD |
| `1D` | `55.10` | 588,820.00 USD | 0.00 USD | 588,820.00 USD | 3,850.00 USD | 53,510.00 USD | 51,570.00 USD |
| `7D` | `55.10` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 0.00 USD | 18,510.00 USD | 47,980.00 USD |
| `1D` | `55.20` | 479,890.00 USD | 0.00 USD | 479,890.00 USD | 24,740.00 USD | 7,520.00 USD | 58,520.00 USD |
| `7D` | `55.20` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 57,400.00 USD | 59,710.00 USD | 150,160.00 USD |
| `1D` | `55.30` | 389,110.00 USD | 0.00 USD | 389,110.00 USD | 39,800.00 USD | 22,650.00 USD | 51,760.00 USD |
| `7D` | `55.30` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 23,140.00 USD | 11,270.00 USD | 0.00 USD |
| `1D` | `55.40` | 274,890.00 USD | 0.00 USD | 274,890.00 USD | 0.00 USD | 6,510.00 USD | 742.75 USD |
| `7D` | `55.40` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 0.00 USD | 18,550.00 USD | 4,800.00 USD |
| `1D` | `55.50` | 267,640.00 USD | 0.00 USD | 267,640.00 USD | 0.00 USD | 9,250.00 USD | 5,500.00 USD |
| `7D` | `55.50` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 0.00 USD | 33,460.00 USD | 0.00 USD |
| `7D` | `55.60` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 426,340.00 USD | 13,860.00 USD | 0.00 USD |
| `1D` | `55.70` | 252,890.00 USD | 0.00 USD | 252,890.00 USD | 0.00 USD | 7,490.00 USD | 613.46 USD |
| `7D` | `55.70` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD |
| `1D` | `55.80` | 244,780.00 USD | 0.00 USD | 244,780.00 USD | 6,170.00 USD | 26,160.00 USD | 3,340.00 USD |
| `7D` | `55.80` | 903,020.00 USD | 0.00 USD | 903,020.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD |
| `1D` | `55.90` | 209,110.00 USD | 0.00 USD | 209,110.00 USD | 103,700.00 USD | 11,780.00 USD | 89,130.00 USD |
| `7D` | `55.90` | 812,050.00 USD | 0.00 USD | 812,050.00 USD | 141,330.00 USD | 101,960.00 USD | 117,660.00 USD |
| `1D` | `56.00` | 4,510.00 USD | 0.00 USD | 4,510.00 USD | 0.00 USD | 0.00 USD | 4,510.00 USD |
| `7D` | `56.00` | 451,100.00 USD | 0.00 USD | 451,100.00 USD | 2,590.00 USD | 118,560.00 USD | 171,110.00 USD |
| `1D` | `56.10` | 74,130.00 USD | 74,130.00 USD | 0.00 USD | 68,240.00 USD | 5,890.00 USD | 0.00 USD |
| `1D` | `56.10` | 148,270.00 USD | 148,270.00 USD | 0.00 USD | 68,240.00 USD | 5,890.00 USD | 0.00 USD |
| `7D` | `56.10` | 158,840.00 USD | 0.00 USD | 158,840.00 USD | 3,980.00 USD | 154,860.00 USD | 0.00 USD |
| `7D` | `56.20` | 79,940.00 USD | 79,940.00 USD | 0.00 USD | 0.00 USD | 79,940.00 USD | 0.00 USD |
| `7D` | `56.20` | 159,890.00 USD | 159,890.00 USD | 0.00 USD | 0.00 USD | 79,940.00 USD | 0.00 USD |
| `1D` | `56.30` | 196,590.00 USD | 196,590.00 USD | 0.00 USD | 0.00 USD | 44,360.00 USD | 3,950.00 USD |
| `7D` | `56.30` | 163,750.00 USD | 163,750.00 USD | 0.00 USD | 1,270.00 USD | 0.00 USD | 2,590.00 USD |
| `1D` | `56.40` | 221,790.00 USD | 221,790.00 USD | 0.00 USD | 5,040.00 USD | 17,690.00 USD | 2,470.00 USD |
| `7D` | `56.40` | 177,440.00 USD | 177,440.00 USD | 0.00 USD | 2,650.00 USD | 11,040.00 USD | 0.00 USD |
| `1D` | `56.50` | 606,910.00 USD | 606,910.00 USD | 0.00 USD | 138,540.00 USD | 101,980.00 USD | 144,610.00 USD |
| `7D` | `56.50` | 497,760.00 USD | 497,760.00 USD | 0.00 USD | 170,750.00 USD | 143,420.00 USD | 6,150.00 USD |
| `1D` | `56.60` | 841,620.00 USD | 841,620.00 USD | 0.00 USD | 49,560.00 USD | 104,240.00 USD | 80,910.00 USD |
| `7D` | `56.60` | 997,520.00 USD | 997,520.00 USD | 0.00 USD | 363,190.00 USD | 136,570.00 USD | 0.00 USD |
| `1D` | `56.70` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 97,300.00 USD | 27,730.00 USD | 307,810.00 USD |
| `7D` | `56.70` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 117,290.00 USD | 121,500.00 USD | 98,950.00 USD |
| `1D` | `56.80` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 117,760.00 USD | 17,250.00 USD | 68,120.00 USD |
| `7D` | `56.80` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 153,580.00 USD | 92,780.00 USD | 303,010.00 USD |
| `1D` | `56.90` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 38,540.00 USD | 10,710.00 USD | 22,790.00 USD |
| `7D` | `56.90` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 113,780.00 USD | 48,600.00 USD | 266,610.00 USD |
| `1D` | `57.00` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 6,480.00 USD | 23,050.00 USD | 13,150.00 USD |
| `7D` | `57.00` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 88,680.00 USD | 20,690.00 USD | 151,930.00 USD |
| `1D` | `57.10` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 59,550.00 USD | 26,670.00 USD | 26,090.00 USD |
| `7D` | `57.10` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 36,580.00 USD | 26,000.00 USD | 20,440.00 USD |
| `1D` | `57.20` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 37,450.00 USD | 35,770.00 USD | 95,530.00 USD |
| `7D` | `57.20` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 95,090.00 USD | 21,090.00 USD | 5,960.00 USD |
| `1D` | `57.30` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 24,260.00 USD | 36,820.00 USD | 58,540.00 USD |
| `7D` | `57.30` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 22,360.00 USD | 28,570.00 USD | 82,230.00 USD |
| `1D` | `57.40` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 70,320.00 USD | 45,150.00 USD | 70,520.00 USD |
| `7D` | `57.40` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 124,180.00 USD | 72,180.00 USD | 257,400.00 USD |
| `1D` | `57.50` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 184,770.00 USD | 48,350.00 USD | 167,330.00 USD |
| `7D` | `57.50` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 99,810.00 USD | 31,830.00 USD | 0.00 USD |
| `1D` | `57.60` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 69,720.00 USD | 24,050.00 USD | 62,510.00 USD |
| `7D` | `57.60` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 149,560.00 USD | 40,430.00 USD | 28,320.00 USD |
| `1D` | `57.70` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 36,620.00 USD | 26,070.00 USD | 96,350.00 USD |
| `7D` | `57.70` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 5,400.00 USD | 57,330.00 USD |
| `1D` | `57.80` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 9,690.00 USD | 13,860.00 USD | 73,330.00 USD |
| `7D` | `57.80` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 9,650.00 USD | 14,360.00 USD | 49,480.00 USD |
| `1D` | `57.90` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 13,000.00 USD | 14,100.00 USD | 9,940.00 USD |
| `7D` | `57.90` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 5,120.00 USD | 963.90 USD | 22,350.00 USD |
| `1D` | `58.00` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 4,580.00 USD | 5,870.00 USD | 7,540.00 USD |
| `7D` | `58.00` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 3,670.00 USD | 86,690.00 USD |
| `1D` | `58.10` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 31,400.00 USD | 9,120.00 USD | 15,370.00 USD |
| `7D` | `58.10` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 5,470.00 USD | 1,310.00 USD | 848.40 USD |
| `1D` | `58.20` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 27,190.00 USD | 9,520.00 USD | 487.60 USD |
| `7D` | `58.20` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 4,940.00 USD | 0.00 USD |
| `1D` | `58.30` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 23,960.00 USD | 17,260.00 USD | 51,700.00 USD |
| `7D` | `58.30` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 36,970.00 USD | 9,580.00 USD | 27,950.00 USD |
| `1D` | `58.40` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 2,240.00 USD | 15,040.00 USD | 35,850.00 USD |
| `7D` | `58.40` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 9,260.00 USD | 78,110.00 USD |
| `1D` | `58.50` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 21,130.00 USD | 8,030.00 USD | 124.02 USD |
| `7D` | `58.50` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD |
| `1D` | `58.60` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 14,490.00 USD | 3,760.00 USD | 36,180.00 USD |
| `7D` | `58.60` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 30,680.00 USD | 20,260.00 USD | 51,650.00 USD |
| `1D` | `58.70` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 38,020.00 USD | 10,060.00 USD | 26,240.00 USD |
| `7D` | `58.70` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 15,810.00 USD | 11,600.00 USD | 35,320.00 USD |
| `1D` | `58.80` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 35,830.00 USD | 14,730.00 USD | 23,340.00 USD |
| `7D` | `58.80` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD |
| `1D` | `58.90` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 22,130.00 USD | 60,920.00 USD | 90,490.00 USD |
| `7D` | `58.90` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 54,240.00 USD | 83,500.00 USD |
| `1D` | `59.00` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 129,180.00 USD | 58,790.00 USD | 127,880.00 USD |
| `7D` | `59.00` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 259,280.00 USD | 65,270.00 USD | 118,570.00 USD |
| `1D` | `59.10` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 91,380.00 USD | 39,780.00 USD | 163,590.00 USD |
| `7D` | `59.10` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 91,060.00 USD | 45,400.00 USD | 158,780.00 USD |
| `1D` | `59.20` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 101,760.00 USD | 59,450.00 USD | 49,290.00 USD |
| `7D` | `59.20` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 153,580.00 USD | 18,540.00 USD | 174,600.00 USD |
| `1D` | `59.30` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 171,630.00 USD | 45,010.00 USD | 94,100.00 USD |
| `7D` | `59.30` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD |
| `1D` | `59.40` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 64,900.00 USD | 45,810.00 USD | 59,430.00 USD |
| `7D` | `59.40` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 105,490.00 USD | 73,620.00 USD | 137,500.00 USD |
| `1D` | `59.50` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 89,030.00 USD | 38,560.00 USD | 33,840.00 USD |
| `7D` | `59.50` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD |
| `1D` | `59.60` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 43,670.00 USD | 53,100.00 USD | 7,010.00 USD |
| `7D` | `59.60` | 6,820,000.00 USD | 6,820,000.00 USD | 0.00 USD | 270,460.00 USD | 147,800.00 USD | 86,840.00 USD |
| `1D` | `59.70` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 13,470.00 USD | 19,120.00 USD | 78,050.00 USD |
| `7D` | `59.70` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 55,510.00 USD | 180,620.00 USD | 162,850.00 USD |
| `1D` | `59.80` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 31,530.00 USD | 26,470.00 USD | 10,630.00 USD |
| `7D` | `59.80` | 7,590,000.00 USD | 7,590,000.00 USD | 0.00 USD | 118,240.00 USD | 97,600.00 USD | 154,930.00 USD |
| `1D` | `59.90` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 112,000.00 USD | 20,240.00 USD | 50,060.00 USD |
| `7D` | `59.90` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 209,780.00 USD | 83,540.00 USD | 39,820.00 USD |
| `1D` | `60.00` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 164,190.00 USD | 29,090.00 USD | 50,570.00 USD |
| `7D` | `60.00` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 154,790.00 USD | 152,810.00 USD | 94,160.00 USD |
| `1D` | `60.10` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 64,090.00 USD | 28,140.00 USD | 57,080.00 USD |
| `7D` | `60.10` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 217,190.00 USD | 100,570.00 USD | 113,260.00 USD |
| `1D` | `60.20` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 59,560.00 USD | 19,740.00 USD | 82,270.00 USD |
| `7D` | `60.20` | 9,130,000.00 USD | 9,130,000.00 USD | 0.00 USD | 162,230.00 USD | 99,360.00 USD | 108,990.00 USD |
| `1D` | `60.30` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 53,910.00 USD | 30,600.00 USD | 24,580.00 USD |
| `7D` | `60.30` | 9,530,000.00 USD | 9,530,000.00 USD | 0.00 USD | 133,350.00 USD | 100,380.00 USD | 170,480.00 USD |
| `1D` | `60.40` | 6,400,000.00 USD | 6,400,000.00 USD | 0.00 USD | 66,740.00 USD | 13,730.00 USD | 39,240.00 USD |
| `7D` | `60.40` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 64,850.00 USD | 108,300.00 USD | 204,780.00 USD |
| `1D` | `60.50` | 6,480,000.00 USD | 6,480,000.00 USD | 0.00 USD | 22,700.00 USD | 19,320.00 USD | 36,200.00 USD |
| `7D` | `60.50` | 10,290,000.00 USD | 10,290,000.00 USD | 0.00 USD | 115,390.00 USD | 86,870.00 USD | 175,550.00 USD |
| `1D` | `60.60` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 40,710.00 USD | 19,140.00 USD | 3,930.00 USD |
| `7D` | `60.60` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 251,100.00 USD | 18,640.00 USD | 118,680.00 USD |
| `1D` | `60.70` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 34,230.00 USD | 22,330.00 USD | 3,120.00 USD |
| `7D` | `60.70` | 10,880,000.00 USD | 10,880,000.00 USD | 0.00 USD | 119,080.00 USD | 57,480.00 USD | 22,840.00 USD |
| `1D` | `60.80` | 6,680,000.00 USD | 6,680,000.00 USD | 0.00 USD | 15,430.00 USD | 12,060.00 USD | 47,810.00 USD |
| `7D` | `60.80` | 11,070,000.00 USD | 11,070,000.00 USD | 0.00 USD | 46,960.00 USD | 69,290.00 USD | 76,200.00 USD |
| `1D` | `60.90` | 6,760,000.00 USD | 6,760,000.00 USD | 0.00 USD | 35,570.00 USD | 21,920.00 USD | 22,850.00 USD |
| `7D` | `60.90` | 11,270,000.00 USD | 11,270,000.00 USD | 0.00 USD | 105,970.00 USD | 34,400.00 USD | 65,110.00 USD |
| `1D` | `61.00` | 6,830,000.00 USD | 6,830,000.00 USD | 0.00 USD | 44,070.00 USD | 6,430.00 USD | 18,420.00 USD |
| `7D` | `61.00` | 11,390,000.00 USD | 11,390,000.00 USD | 0.00 USD | 77,670.00 USD | 36,060.00 USD | 5,220.00 USD |
| `1D` | `61.10` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 12,010.00 USD | 6,270.00 USD | 11,490.00 USD |
| `7D` | `61.10` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 31,540.00 USD | 1,560.00 USD | 0.00 USD |
| `1D` | `61.20` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 72,520.00 USD | 0.00 USD | 38,940.00 USD |
| `7D` | `61.20` | 11,620,000.00 USD | 11,620,000.00 USD | 0.00 USD | 78,320.00 USD | 60,240.00 USD | 52,930.00 USD |
| `1D` | `61.30` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 0.00 USD | 3,330.00 USD | 0.00 USD |
| `7D` | `61.30` | 11,700,000.00 USD | 11,700,000.00 USD | 0.00 USD | 27,780.00 USD | 21,000.00 USD | 33,030.00 USD |
| `1D` | `61.40` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 1,190.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `61.40` | 11,830,000.00 USD | 11,830,000.00 USD | 0.00 USD | 66,470.00 USD | 25,720.00 USD | 35,250.00 USD |
| `1D` | `61.50` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 1,060.00 USD | 1,290.00 USD | 2,390.00 USD |
| `7D` | `61.50` | 11,920,000.00 USD | 11,920,000.00 USD | 0.00 USD | 19,810.00 USD | 35,300.00 USD | 36,110.00 USD |
| `1D` | `61.60` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 5,360.00 USD | 3,070.00 USD | 0.00 USD |
| `7D` | `61.60` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 38,370.00 USD | 52,240.00 USD | 121,470.00 USD |
| `1D` | `61.70` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 10,770.00 USD | 2,110.00 USD | 5,950.00 USD |
| `7D` | `61.70` | 12,320,000.00 USD | 12,320,000.00 USD | 0.00 USD | 82,820.00 USD | 10,880.00 USD | 99,520.00 USD |
| `1D` | `61.80` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 3,480.00 USD | 2,640.00 USD | 9,380.00 USD |
| `7D` | `61.80` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 158,760.00 USD | 25,670.00 USD | 71,530.00 USD |
| `1D` | `61.90` | 7,040,000.00 USD | 7,040,000.00 USD | 0.00 USD | 4,800.00 USD | 1,440.00 USD | 11,700.00 USD |
| `7D` | `61.90` | 12,730,000.00 USD | 12,730,000.00 USD | 0.00 USD | 72,920.00 USD | 32,820.00 USD | 41,580.00 USD |
| `1D` | `62.00` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 15,300.00 USD | 3,100.00 USD | 8,280.00 USD |
| `7D` | `62.00` | 12,830,000.00 USD | 12,830,000.00 USD | 0.00 USD | 50,080.00 USD | 8,550.00 USD | 40,590.00 USD |
| `1D` | `62.10` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 2,530.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.10` | 12,840,000.00 USD | 12,840,000.00 USD | 0.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.20` | 12,950,000.00 USD | 12,950,000.00 USD | 0.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD |
| `7D` | `62.30` | 13,100,000.00 USD | 13,100,000.00 USD | 0.00 USD | 29,050.00 USD | 23,450.00 USD | 97,450.00 USD |
| `7D` | `62.40` | 13,240,000.00 USD | 13,240,000.00 USD | 0.00 USD | 77,960.00 USD | 27,560.00 USD | 30,890.00 USD |
| `7D` | `62.50` | 13,320,000.00 USD | 13,320,000.00 USD | 0.00 USD | 42,730.00 USD | 14,320.00 USD | 26,610.00 USD |
| `7D` | `62.60` | 13,390,000.00 USD | 13,390,000.00 USD | 0.00 USD | 33,900.00 USD | 7,830.00 USD | 27,730.00 USD |
| `7D` | `62.70` | 13,470,000.00 USD | 13,470,000.00 USD | 0.00 USD | 22,020.00 USD | 12,490.00 USD | 47,090.00 USD |
| `7D` | `62.80` | 13,620,000.00 USD | 13,620,000.00 USD | 0.00 USD | 71,230.00 USD | 28,960.00 USD | 45,150.00 USD |
| `7D` | `62.90` | 13,710,000.00 USD | 13,710,000.00 USD | 0.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD |
| `7D` | `63.00` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD |
| `7D` | `63.10` | 13,810,000.00 USD | 13,810,000.00 USD | 0.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD |
| `7D` | `63.30` | 13,850,000.00 USD | 13,850,000.00 USD | 0.00 USD | 15,010.00 USD | 11,500.00 USD | 9,730.00 USD |
| `7D` | `63.40` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 11,980.00 USD | 1,320.00 USD | 9,960.00 USD |
| `7D` | `63.50` | 13,900,000.00 USD | 13,900,000.00 USD | 0.00 USD | 5,430.00 USD | 15,810.00 USD | 4,760.00 USD |
| `7D` | `63.60` | 13,990,000.00 USD | 13,990,000.00 USD | 0.00 USD | 63,480.00 USD | 20,800.00 USD | 11,880.00 USD |
| `7D` | `63.70` | 14,070,000.00 USD | 14,070,000.00 USD | 0.00 USD | 18,220.00 USD | 18,810.00 USD | 34,980.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `415.37M` | Total OI Tokens: `7,420,021.5 LTC`
  * 1h OI Change: `-0.81%` | 4h OI Change: `+2.48%` | 24h OI Change: `-8.30%`
  * Exchange Breakdown: Binance=`73.54M` | Bybit=`66.95M` | OKX=`33.92M` | Hyperliquid=`22.37M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `12.83K` | Last 24h: `31.76K` | Last 3d: `59.78K` | Last 7d: `115.16K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0028%` |
| **USDT Bybit** | `0.0079%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0018%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `30.41%` | `69.59%` | `0.44` | 28,280,000.00 USD |
| `15M` | `Binance` | `34.41%` | `65.59%` | `0.52` | 10,300,000.00 USD |
| `15M` | `OKX` | `32.14%` | `67.86%` | `0.47` | 3,560,000.00 USD |
| `15M` | `Bybit` | `35.19%` | `64.81%` | `0.54` | 3,640,000.00 USD |
| `15M` | `KuCoin` | `40.02%` | `59.98%` | `0.67` | 122,630.00 USD |
| `15M` | `Gate` | `24.97%` | `75.03%` | `0.33` | 722,690.00 USD |
| `15M` | `Bitget` | `26.34%` | `73.66%` | `0.36` | 1,570,000.00 USD |
| `15M` | `BingX` | `16.74%` | `83.26%` | `0.20` | 2,800,000.00 USD |
| `15M` | `MEXC` | `28.97%` | `71.03%` | `0.41` | 1,480,000.00 USD |
| `15M` | `Bitunix` | `22.52%` | `77.48%` | `0.29` | 585,500.00 USD |
| `15M` | `Hyperliquid` | `20.47%` | `79.53%` | `0.26` | 2,490,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `35.88%` | `64.12%` | `0.56` | 131,740.00 USD |
| `15M` | `Crypto.com` | `75%` | `25%` | `3.00` | 1,560.00 USD |
| `15M` | `WhiteBIT` | `97.93%` | `2.07%` | `47.31` | 336,230.00 USD |
| `15M` | `HTX` | `29.21%` | `70.79%` | `0.41` | 59,980.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `16.45%` | `83.55%` | `0.20` | 138,760.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `8.52%` | `91.48%` | `0.09` | 331,120.00 USD |
| `15M` | `Whale Positions` | `34.41%` | `65.59%` | `0.52` | 10,300,000.00 USD |
| `15M` | `Global Accounts` | `30.41%` | `69.59%` | `0.44` | 28,280,000.00 USD |
| `1H` | `LTC` | `38.56%` | `61.44%` | `0.63` | 74,690,000.00 USD |
| `1H` | `Binance` | `41.8%` | `58.2%` | `0.72` | 26,730,000.00 USD |
| `1H` | `OKX` | `37.96%` | `62.04%` | `0.61` | 10,370,000.00 USD |
| `1H` | `Bybit` | `38.39%` | `61.61%` | `0.62` | 10,230,000.00 USD |
| `1H` | `KuCoin` | `29.67%` | `70.33%` | `0.42` | 543,800.00 USD |
| `1H` | `Gate` | `41.81%` | `58.19%` | `0.72` | 1,910,000.00 USD |
| `1H` | `Bitget` | `35.95%` | `64.05%` | `0.56` | 4,730,000.00 USD |
| `1H` | `BingX` | `28.38%` | `71.62%` | `0.40` | 5,080,000.00 USD |
| `1H` | `MEXC` | `37.94%` | `62.06%` | `0.61` | 3,790,000.00 USD |
| `1H` | `Bitunix` | `34.29%` | `65.71%` | `0.52` | 2,010,000.00 USD |
| `1H` | `Hyperliquid` | `30.62%` | `69.38%` | `0.44` | 7,020,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `38.28%` | `61.72%` | `0.62` | 417,440.00 USD |
| `1H` | `Crypto.com` | `46.97%` | `53.03%` | `0.89` | 3,020.00 USD |
| `1H` | `WhiteBIT` | `99.55%` | `0.45%` | `221.22` | 1,060,000.00 USD |
| `1H` | `HTX` | `25.2%` | `74.8%` | `0.34` | 73,610.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `28.87%` | `71.13%` | `0.41` | 267,120.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `14.66%` | `85.34%` | `0.17` | 448,700.00 USD |
| `1H` | `Whale Positions` | `41.8%` | `58.2%` | `0.72` | 26,730,000.00 USD |
| `1H` | `Global Accounts` | `38.56%` | `61.44%` | `0.63` | 74,690,000.00 USD |
| `4H` | `LTC` | `52.89%` | `47.11%` | `1.12` | 302,310,000.00 USD |
| `4H` | `Binance` | `52.05%` | `47.95%` | `1.09` | 120,030,000.00 USD |
| `4H` | `OKX` | `52.67%` | `47.33%` | `1.11` | 37,580,000.00 USD |
| `4H` | `Bybit` | `52.5%` | `47.5%` | `1.11` | 41,350,000.00 USD |
| `4H` | `KuCoin` | `48.93%` | `51.07%` | `0.96` | 2,030,000.00 USD |
| `4H` | `Gate` | `54.21%` | `45.79%` | `1.18` | 11,420,000.00 USD |
| `4H` | `Bitget` | `51.05%` | `48.95%` | `1.04` | 17,710,000.00 USD |
| `4H` | `BingX` | `51.7%` | `48.3%` | `1.07` | 18,240,000.00 USD |
| `4H` | `MEXC` | `49.89%` | `50.11%` | `1.00` | 10,690,000.00 USD |
| `4H` | `Bitunix` | `49.53%` | `50.47%` | `0.98` | 7,190,000.00 USD |
| `4H` | `Hyperliquid` | `54.71%` | `45.29%` | `1.21` | 26,670,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.58%` | `51.42%` | `0.94` | 1,670,000.00 USD |
| `4H` | `Crypto.com` | `51.64%` | `48.36%` | `1.07` | 20,680.00 USD |
| `4H` | `WhiteBIT` | `92.58%` | `7.42%` | `12.48` | 4,930,000.00 USD |
| `4H` | `HTX` | `44.26%` | `55.74%` | `0.79` | 213,770.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `81.08%` | `18.92%` | `4.29` | 280,460.00 USD |
| `4H` | `Aster` | `52.52%` | `47.48%` | `1.11` | 627,950.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `43.83%` | `56.17%` | `0.78` | 1,660,000.00 USD |
| `4H` | `Whale Positions` | `52.05%` | `47.95%` | `1.09` | 120,030,000.00 USD |
| `4H` | `Global Accounts` | `52.89%` | `47.11%` | `1.12` | 302,310,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `56.20` | `56.14` | `56.20` | `56.27` | `55.95` | 941,863.07 USD | 405,285.65 USD | 536,577.42 USD | -131,291.77 USD | `-13.94%` | `0B / 5S` |
| `0:00 UTC` | `56.03` | `55.95` | `56.03` | `56.28` | `55.73` | 1,432,521.27 USD | 626,753.60 USD | 805,767.67 USD | -179,014.08 USD | `-12.50%` | `6B / 18S` |
| `5:00 UTC` | `56.11` | `56.13` | `56.11` | `56.30` | `56.02` | 517,114.54 USD | 217,529.34 USD | 299,585.20 USD | -82,055.86 USD | `-15.87%` | `3B / 3S` |
| `0:00 UTC` | `56.22` | `56.21` | `56.22` | `56.28` | `56.12` | 645,876.21 USD | 293,840.75 USD | 352,035.46 USD | -58,194.71 USD | `-9.01%` | `0B / 1S` |
| `5:00 UTC` | `56.22` | `56.13` | `56.22` | `56.25` | `55.98` | 603,205.25 USD | 271,389.80 USD | 331,815.45 USD | -60,425.65 USD | `-10.02%` | `2B / 7S` |
| `0:00 UTC` | `56.23` | `56.20` | `56.23` | `56.36` | `55.98` | 638,187.75 USD | 362,537.55 USD | 275,650.21 USD | 86,887.34 USD | `+13.61%` | `9B / 3S` |
| `5:00 UTC` | `56.20` | `56.26` | `56.20` | `56.41` | `56.12` | 504,696.37 USD | 240,879.66 USD | 263,816.70 USD | -22,937.04 USD | `-4.54%` | `3B / 4S` |
| `0:00 UTC` | `56.41` | `56.37` | `56.41` | `56.47` | `56.25` | 988,298.96 USD | 470,597.81 USD | 517,701.15 USD | -47,103.33 USD | `-4.77%` | `2B / 2S` |
| `5:00 UTC` | `56.39` | `56.32` | `56.39` | `56.45` | `56.09` | 737,190.46 USD | 351,743.57 USD | 385,446.89 USD | -33,703.31 USD | `-4.57%` | `2B / 8S` |
| `0:00 UTC` | `56.14` | `56.09` | `56.14` | `56.22` | `55.97` | 585,408.94 USD | 305,845.79 USD | 279,563.15 USD | 26,282.65 USD | `+4.49%` | `5B / 3S` |

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
| `5m` | -24,110.00 USD | 196,300.00 USD | **`ACCUMULATION`** |
| `15m` | -48,870.00 USD | -32,540.00 USD | **`DISTRIBUTION`** |
| `30m` | -15,270.00 USD | -462,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 69,370.00 USD | -190,730.00 USD | **`DISTRIBUTION`** |
| `2h` | 241,320.00 USD | -245,140.00 USD | **`DISTRIBUTION`** |
| `4h` | 479,470.00 USD | -1,630,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -606,700.00 USD | -3,710,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 116,740.00 USD | -4,360,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,860,000.00 USD | -6,670,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 888,210.00 USD | -3,310,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 3,520,000.00 USD | -25,160,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -23,490,000.00 USD | -196,670,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-24.11K` | 15m=`-48.87K` | 1h=`+69.37K` | 24h=`+888.21K`
* Futures Capital Netflows: 5m=`+196.30K` | 15m=`-32.54K` | 1h=`-190.73K` | 24h=`-3.31M`
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
  * `2026-10-30 11:03:46 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:38:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:37:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:39:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `54.32` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `53.38` (Risk Distance: `0.9433` pts)
  * +2.5R Take Profit: `56.68`
  * Mathematical Lot Sizing: **`10.60 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `56.18` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `57.12` (Risk Distance: `0.9433` pts)
  * +2.5R Take Profit: `53.82`
  * Mathematical Lot Sizing: **`10.60 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`56.60`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
