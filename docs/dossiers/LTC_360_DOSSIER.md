# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 11:35:24 IST` (`2026-10-30 06:05:24 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `55.80` | **Live Ask Quote**: `56.09` | **Mid Price**: `55.95`
- **Spread Points**: `300.00` | **Spread BPS**: `53.62 bps` (Charter Threshold: `25.00 bps`)
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
  * Value Area High (VAH) = `56.18` (Distance: `-0.42%`)
  * Point of Control (POC) = `55.27` (Distance: `+1.21%`)
  * Value Area Low (VAL) = `54.30` (Distance: `+3.04%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.40` | POC=`57.72` | VAL=`56.83`
  * Prior Day Extremes: PDH=`59.52` | PDL=`54.18` | PDC=`54.46`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`58.29` | Weekly POC=`56.43` | Weekly VAL=`55.87`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`56.03` | Low=`52.64`
  * London Session (08:00-16:00 UTC): High=`56.22` | Low=`55.73`
  * New York Session (13:00-21:00 UTC): High=`56.28` | Low=`55.61`
  * Initial Balance (First Hour): IB High=`56.22` | IB Low=`55.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `55.72` - `56.17`
  * Optimal Trade Entry (OTE 0.705): `56.06`
  * Structural Invalidation Anchor (0.786): `56.39`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `56.38` | `56.46` | `56.32` | `56.37` | `5,831` | 328,815.25 USD | -30,978.25 USD | `-9.42%` | -5,010,026.92 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `56.37` | `56.43` | `56.30` | `56.32` | `2,669` | 150,451.08 USD | 3,413.21 USD | `+2.27%` | -5,006,613.71 USD | `+0.31` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `56.32` | `56.44` | `56.25` | `56.33` | `8,132` | 458,244.00 USD | -33,041.03 USD | `-7.21%` | -5,039,654.74 USD | `-0.68` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `55.99` | `56.36` | `55.98` | `56.20` | `11,356` | 638,187.75 USD | 86,887.34 USD | `+13.61%` | -4,956,111.64 USD | `+0.76` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `56.21` | `56.40` | `56.12` | `56.38` | `8,972` | 504,696.37 USD | -22,937.04 USD | `-4.54%` | -4,979,048.67 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `56.38` | `56.46` | `56.25` | `56.33` | `16,632` | 937,510.33 USD | -60,606.06 USD | `-6.46%` | -5,039,654.74 USD | `+0.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `55.13` | `56.26` | `55.11` | `56.25` | `76,464` | 4,260,452.16 USD | -513,161.69 USD | `-12.04%` | -4,553,852.57 USD | `-0.35` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `56.25` | `56.29` | `55.73` | `55.98` | `57,057` | 3,198,717.26 USD | -379,690.29 USD | `-11.87%` | -4,933,542.86 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `55.99` | `56.46` | `55.98` | `56.36` | `36,894` | 2,076,683.16 USD | 3,572.87 USD | `+0.17%` | -4,929,969.99 USD | `+0.33` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,423,359.63 USD | `-1.73` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -4,601,875.81 USD | `-0.83` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.46` | `55.73` | `56.33` | `94,017` | 5,279,111.71 USD | -376,346.05 USD | `-7.13%` | -4,978,221.86 USD | `+0.32` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | 701,394.73 USD | `-1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | 840,681.28 USD | `-1.08` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,423,359.63 USD | `-1.73` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -4,601,875.81 USD | `-0.83` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.46` | `55.73` | `56.30` | `104,153` | 5,850,433.15 USD | -325,256.73 USD | `-5.56%` | -4,927,132.54 USD | `+0.35` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`55.95`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:33:47 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1059` | `0xeadc...9d55` | `LONG` | 2,052,538.32 USD | `36,463.77` | `52.78` | `56.25` | `0.000000` | 127,862.37 USD | `+6.23%` | `10X Cross` |
| `1072` | `0x9aa5...58af` | `SHORT` | 2,034,848.10 USD | `36,177.65` | `71.22` | `56.25` | `302.98` | 541,638.56 USD | `+26.62%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `57.30` | 7,509.61 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 57.2990 USD [API] | `2026-10-29 03:24:56` |
| `ANNOUNCEMENT` | `INFO` | `57.33` | 7,509.53 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 7.51K USD at 57.3290 USD [API] | `2026-10-29 03:35:48` |
| `ANNOUNCEMENT` | `INFO` | `57.20` | 6,036.00 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 6.04K USD at 57.1970 USD [API] | `2026-10-29 03:58:49` |
| `ANNOUNCEMENT` | `INFO` | `51.38` | 63.20 USD | `-` | `NEWS_INTEL` | `-` | #LTC Liquidated Short: 0.06K USD at 51.3800 USD [API] | `2026-05-28 03:18:06` |
| `ANNOUNCEMENT` | `INFO` | `51.38` | 192.68 USD | `-` | `NEWS_INTEL` | `-` | #LTC Liquidated Short: 0.19K USD at 51.3800 USD [API] | `2026-05-28 03:18:06` |


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
| `Live` | `Long Liquidation` | `11.35` | 268.54 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.25` | 122.50 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.75` | 2,560.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.15` | 2,220.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.65` | 150.15 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `16.75` | 2,520.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.05` | 2,170.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.45` | 148.52 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.05` | 3,470.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.45` | 2,010.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.85` | 18,900.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.65` | 136.29 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.15` | 4,120.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.85` | 197.09 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.65` | 365.34 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.05` | 1,380.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.55` | 999.23 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.75` | 375.73 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.85` | 195.57 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.65` | 453.56 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.75` | 963.27 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.95` | 516.22 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.05` | 114,390.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 277,980.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 173.39 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 50,740.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.85` | 7,620.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 374.20 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.65` | 738.47 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.05` | 5,510.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 8,540.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.85` | 164.59 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 173.85 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 583.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 297,500.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 218.46 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.65` | 1,540.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.85` | 578.44 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 538.53 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 5,880.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 1,060.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.65` | 4,640.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 2,870.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 3,080.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 450.10 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.35` | 26,760.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 653.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 953.68 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 32,850.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.35` | 5,810.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 257.76 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 182.85 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 126.70 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.25` | 4,470.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.45` | 65,890.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 3,240.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.85` | 415.41 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 104.85 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 166.49 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.75` | 279.92 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.25` | 181.25 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 3,020.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 423.18 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.65` | 317.76 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 101.80 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 1,490.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.25` | 2,830.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 9,260.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 3,530.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 377.50 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 6,210.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 446.67 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.25` | 695.38 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 847.54 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 2,400.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 993.82 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 4,280.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 2,730.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 665,110.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 570.02 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 264.83 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 716.41 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 312.44 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 5,900.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 1,180.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 133.10 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 3,160.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 1,010.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 133.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 274.39 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.75` | 8,960.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 6,340.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 509.01 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 396.54 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 19,930.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 644.96 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 982.29 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 66,300.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 35,410.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.35` | 301.96 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.55` | 3,380.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 1,890.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.75` | 46,620.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 11,320.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 2,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 9,080.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 122,400.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 417.80 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 5,390.00 USD | 999,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 980.67 USD | 994,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 426.02 USD | 993,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 21,880.00 USD | 992,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 801.14 USD | 971,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 2,380.00 USD | 970,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 84,440.00 USD | 967,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.45` | 1,330.00 USD | 883,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 842.44 USD | 882,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 4,230.00 USD | 881,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 1,480.00 USD | 877,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 2,620.00 USD | 875,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 4,830.00 USD | 872,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 8,710.00 USD | 868,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 3,180.00 USD | 859,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 2,180.00 USD | 856,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 23,940.00 USD | 854,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 12,060.00 USD | 830,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 42,180.00 USD | 818,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.75` | 27,480.00 USD | 775,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 2,940.00 USD | 748,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 706.41 USD | 745,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.15` | 177.22 USD | 744,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.25` | 842.21 USD | 744,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.35` | 22,820.00 USD | 743,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 2,140.00 USD | 720,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 3,980.00 USD | 718,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 358.40 USD | 714,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 158.22 USD | 714,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.05` | 271.01 USD | 714,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.10` | 9,130,000.00 USD | 9,130,000.00 USD | 17,230.00 USD | 12,890.00 USD | 6,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.15` | 1,980.00 USD | 714,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.20` | 9,090,000.00 USD | 9,090,000.00 USD | 8,940.00 USD | 1,090.00 USD | 114.09 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.25` | 1,220.00 USD | 712,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.30` | 9,080,000.00 USD | 9,080,000.00 USD | 692.33 USD | 4,740.00 USD | 6,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.35` | 43,340.00 USD | 710,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.40` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 1,520.00 USD | 28,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.45` | 2,590.00 USD | 667,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `47.50` | 9,040,000.00 USD | 9,040,000.00 USD | 11,830.00 USD | 0.00 USD | 7,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `47.55` | 4,450.00 USD | 664,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 47,750.00 USD | 660,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 9,250.00 USD | 612,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.10` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.15` | 1,690.00 USD | 603,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.20` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.25` | 110.49 USD | 601,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.40` | 9,010,000.00 USD | 9,010,000.00 USD | 0.00 USD | 6,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.55` | 4,440.00 USD | 601,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.60` | 9,000,000.00 USD | 9,000,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.65` | 273.90 USD | 597,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 333.94 USD | 596,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.80` | 9,000,000.00 USD | 9,000,000.00 USD | 1,780.00 USD | 2,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `48.90` | 9,000,000.00 USD | 9,000,000.00 USD | 0.00 USD | 0.00 USD | 960.40 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.95` | 252.58 USD | 596,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,580.00 USD | 596,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,740.00 USD | 594,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.30` | 9,000,000.00 USD | 9,000,000.00 USD | 15,190.00 USD | 4,490.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.35` | 5,230.00 USD | 588,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.40` | 8,960,000.00 USD | 8,960,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.45` | 419.34 USD | 583,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.50` | 8,950,000.00 USD | 8,950,000.00 USD | 2,830.00 USD | 7,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.55` | 18,010.00 USD | 583,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.60` | 8,940,000.00 USD | 8,940,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.65` | 73,260.00 USD | 565,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.70` | 8,930,000.00 USD | 8,930,000.00 USD | 12,090.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.75` | 1,580.00 USD | 492,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.80` | 8,910,000.00 USD | 8,910,000.00 USD | 9,930.00 USD | 8,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.85` | 19,180.00 USD | 490,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.90` | 8,890,000.00 USD | 8,890,000.00 USD | 45,030.00 USD | 7,170.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.95` | 19,920.00 USD | 471,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.00` | 8,840,000.00 USD | 8,840,000.00 USD | 22,100.00 USD | 7,630.00 USD | 24,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.05` | 1,820.00 USD | 451,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.10` | 8,780,000.00 USD | 8,780,000.00 USD | 363.50 USD | 682.90 USD | 8,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.20` | 3,380,000.00 USD | 3,380,000.00 USD | 4,490.00 USD | 5,820.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.20` | 8,770,000.00 USD | 8,770,000.00 USD | 6,960.00 USD | 500.40 USD | 34,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.25` | 102.51 USD | 449,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.30` | 3,360,000.00 USD | 3,360,000.00 USD | 171.03 USD | 333.03 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.30` | 8,730,000.00 USD | 8,730,000.00 USD | 16,270.00 USD | 3,640.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.35` | 1,140.00 USD | 449,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.40` | 3,360,000.00 USD | 3,360,000.00 USD | 4,370.00 USD | 2,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.40` | 8,710,000.00 USD | 8,710,000.00 USD | 28,280.00 USD | 19,110.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,720.00 USD | 448,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.50` | 3,350,000.00 USD | 3,350,000.00 USD | 5,790.00 USD | 2,110.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.50` | 8,630,000.00 USD | 8,630,000.00 USD | 24,840.00 USD | 6,790.00 USD | 44,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.55` | 84,100.00 USD | 443,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.60` | 3,340,000.00 USD | 3,340,000.00 USD | 1,660.00 USD | 2,640.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.60` | 8,550,000.00 USD | 8,550,000.00 USD | 56,670.00 USD | 21,530.00 USD | 22,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.70` | 3,330,000.00 USD | 3,330,000.00 USD | 4,820.00 USD | 1,440.00 USD | 11,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.70` | 8,450,000.00 USD | 8,450,000.00 USD | 65,150.00 USD | 32,820.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.75` | 9,050.00 USD | 359,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.80` | 3,310,000.00 USD | 3,310,000.00 USD | 12,550.00 USD | 3,100.00 USD | 8,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.80` | 8,310,000.00 USD | 8,310,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.90` | 3,290,000.00 USD | 3,290,000.00 USD | 826.24 USD | 260.05 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.90` | 8,210,000.00 USD | 8,210,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.95` | 431.55 USD | 350,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.00` | 3,280,000.00 USD | 3,280,000.00 USD | 5,040.00 USD | 0.00 USD | 430.77 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.00` | 7,960,000.00 USD | 7,960,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.10` | 3,270,000.00 USD | 3,270,000.00 USD | 9,210.00 USD | 6,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.10` | 7,840,000.00 USD | 7,840,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.15` | 219,370.00 USD | 350,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.20` | 3,260,000.00 USD | 3,260,000.00 USD | 2,360.00 USD | 1,130.00 USD | 17,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.20` | 7,750,000.00 USD | 7,750,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.25` | 202.44 USD | 130,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.30` | 3,230,000.00 USD | 3,230,000.00 USD | 16,790.00 USD | 14,100.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.30` | 7,690,000.00 USD | 7,690,000.00 USD | 28,400.00 USD | 26,720.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.35` | 453.93 USD | 130,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.40` | 3,190,000.00 USD | 3,190,000.00 USD | 13,750.00 USD | 11,490.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.40` | 7,590,000.00 USD | 7,590,000.00 USD | 73,130.00 USD | 42,820.00 USD | 46,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.45` | 27,210.00 USD | 130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.50` | 3,160,000.00 USD | 3,160,000.00 USD | 7,880.00 USD | 10,980.00 USD | 37,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.50` | 7,430,000.00 USD | 7,430,000.00 USD | 38,520.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.55` | 551.07 USD | 102,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.60` | 3,110,000.00 USD | 3,110,000.00 USD | 9,060.00 USD | 18,490.00 USD | 757.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.60` | 7,330,000.00 USD | 7,330,000.00 USD | 37,880.00 USD | 36,790.00 USD | 41,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.65` | 9,100.00 USD | 102,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.70` | 3,080,000.00 USD | 3,080,000.00 USD | 2,890.00 USD | 13,810.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.70` | 7,210,000.00 USD | 7,210,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.75` | 6,480.00 USD | 93,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.80` | 3,040,000.00 USD | 3,040,000.00 USD | 12,590.00 USD | 19,270.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.80` | 7,170,000.00 USD | 7,170,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.85` | 13,680.00 USD | 86,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.90` | 2,990,000.00 USD | 2,990,000.00 USD | 9,460.00 USD | 24,890.00 USD | 23,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.90` | 7,120,000.00 USD | 7,120,000.00 USD | 5,870.00 USD | 25,410.00 USD | 28,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.95` | 16,800.00 USD | 72,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.00` | 2,940,000.00 USD | 2,940,000.00 USD | 20,980.00 USD | 25,480.00 USD | 25,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.00` | 7,060,000.00 USD | 7,060,000.00 USD | 64,300.00 USD | 26,440.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.10` | 2,860,000.00 USD | 2,860,000.00 USD | 34,880.00 USD | 17,130.00 USD | 50,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 6,960,000.00 USD | 6,960,000.00 USD | 24,220.00 USD | 28,090.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.15` | 1,900.00 USD | 56,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.20` | 2,760,000.00 USD | 2,760,000.00 USD | 15,020.00 USD | 7,630.00 USD | 46,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 6,870,000.00 USD | 6,870,000.00 USD | 38,380.00 USD | 13,960.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.25` | 4,930.00 USD | 54,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.30` | 2,690,000.00 USD | 2,690,000.00 USD | 26,510.00 USD | 21,640.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 6,790,000.00 USD | 6,790,000.00 USD | 24,840.00 USD | 41,300.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.35` | 134.02 USD | 49,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.40` | 2,630,000.00 USD | 2,630,000.00 USD | 12,460.00 USD | 15,120.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 6,710,000.00 USD | 6,710,000.00 USD | 20,580.00 USD | 38,950.00 USD | 22,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.45` | 2,360.00 USD | 49,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.50` | 2,600,000.00 USD | 2,600,000.00 USD | 53,350.00 USD | 29,580.00 USD | 74,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.50` | 6,630,000.00 USD | 6,630,000.00 USD | 38,720.00 USD | 667.05 USD | 11,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.55` | 8,700.00 USD | 46,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.60` | 2,440,000.00 USD | 2,440,000.00 USD | 8,330.00 USD | 40,700.00 USD | 717.10 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.60` | 6,580,000.00 USD | 6,580,000.00 USD | 74,610.00 USD | 32,590.00 USD | 59,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.70` | 2,390,000.00 USD | 2,390,000.00 USD | 16,690.00 USD | 19,440.00 USD | 28,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.70` | 6,410,000.00 USD | 6,410,000.00 USD | 20,250.00 USD | 92,920.00 USD | 108,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.75` | 4,240.00 USD | 38,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.80` | 2,330,000.00 USD | 2,330,000.00 USD | 27,090.00 USD | 50,290.00 USD | 102,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.80` | 6,190,000.00 USD | 6,190,000.00 USD | 39,200.00 USD | 35,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.85` | 5,950.00 USD | 33,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.90` | 2,150,000.00 USD | 2,150,000.00 USD | 43,760.00 USD | 50,040.00 USD | 26,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.90` | 6,120,000.00 USD | 6,120,000.00 USD | 44,800.00 USD | 28,710.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.95` | 25,840.00 USD | 27,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.00` | 2,030,000.00 USD | 2,030,000.00 USD | 26,670.00 USD | 30,500.00 USD | 39,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.00` | 6,010,000.00 USD | 6,010,000.00 USD | 39,690.00 USD | 25,810.00 USD | 81,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.10` | 1,930,000.00 USD | 1,930,000.00 USD | 14,570.00 USD | 42,760.00 USD | 87,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.10` | 5,860,000.00 USD | 5,860,000.00 USD | 45,320.00 USD | 17,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.15` | 1,720.00 USD | 2,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.20` | 1,790,000.00 USD | 1,790,000.00 USD | 24,240.00 USD | 6,510.00 USD | 41,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.20` | 5,800,000.00 USD | 5,800,000.00 USD | 162,460.00 USD | 28,320.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.25` | 405.76 USD | 405.76 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.30` | 1,710,000.00 USD | 1,710,000.00 USD | 4,060.00 USD | 0.00 USD | 5,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.30` | 5,590,000.00 USD | 5,590,000.00 USD | 57,250.00 USD | 24,540.00 USD | 34,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.40` | 1,700,000.00 USD | 1,700,000.00 USD | 3,460.00 USD | 1,850.00 USD | 657.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.40` | 5,470,000.00 USD | 5,470,000.00 USD | 44,030.00 USD | 7,250.00 USD | 91,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.50` | 1,700,000.00 USD | 1,700,000.00 USD | 9,110.00 USD | 3,940.00 USD | 2,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.50` | 5,330,000.00 USD | 5,330,000.00 USD | 48,660.00 USD | 3,440.00 USD | 20,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.60` | 1,680,000.00 USD | 1,680,000.00 USD | 72,650.00 USD | 220.65 USD | 13,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.60` | 5,250,000.00 USD | 5,250,000.00 USD | 52,800.00 USD | 1,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.70` | 1,600,000.00 USD | 1,600,000.00 USD | 6,210.00 USD | 0.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.70` | 5,200,000.00 USD | 5,200,000.00 USD | 131,400.00 USD | 3,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.80` | 1,580,000.00 USD | 1,580,000.00 USD | 44,920.00 USD | 2,830.00 USD | 168.97 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.80` | 5,060,000.00 USD | 5,060,000.00 USD | 99,150.00 USD | 13,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.90` | 1,540,000.00 USD | 1,540,000.00 USD | 40,670.00 USD | 18,200.00 USD | 4,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.90` | 4,950,000.00 USD | 4,950,000.00 USD | 129,920.00 USD | 21,360.00 USD | 1,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.00` | 1,470,000.00 USD | 1,470,000.00 USD | 45,350.00 USD | 15,370.00 USD | 68,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.00` | 4,800,000.00 USD | 4,800,000.00 USD | 353,050.00 USD | 71,820.00 USD | 272,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.10` | 1,340,000.00 USD | 1,340,000.00 USD | 91,490.00 USD | 19,160.00 USD | 45,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.10` | 4,100,000.00 USD | 4,100,000.00 USD | 302,190.00 USD | 0.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.20` | 1,190,000.00 USD | 1,190,000.00 USD | 72,600.00 USD | 15,510.00 USD | 40,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.20` | 3,800,000.00 USD | 3,800,000.00 USD | 205,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.30` | 1,060,000.00 USD | 1,060,000.00 USD | 15,600.00 USD | 0.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.30` | 3,590,000.00 USD | 3,590,000.00 USD | 381,380.00 USD | 0.00 USD | 181,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.40` | 1,040,000.00 USD | 1,040,000.00 USD | 51,570.00 USD | 35,500.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.40` | 3,030,000.00 USD | 3,030,000.00 USD | 304,270.00 USD | 13,830.00 USD | 92,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.50` | 948,180.00 USD | 948,180.00 USD | 9,670.00 USD | 46,240.00 USD | 1,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.50` | 2,620,000.00 USD | 2,620,000.00 USD | 159,720.00 USD | 15,240.00 USD | 239,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.60` | 890,960.00 USD | 890,960.00 USD | 913.17 USD | 21,680.00 USD | 5,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.60` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 1,930.00 USD | 116,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.70` | 862,800.00 USD | 862,800.00 USD | 0.00 USD | 15,420.00 USD | 82,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.80` | 764,920.00 USD | 764,920.00 USD | 0.00 USD | 25,800.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.90` | 727,350.00 USD | 727,350.00 USD | 49,450.00 USD | 13,090.00 USD | 1,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.90` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 52,180.00 USD | 47,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.00` | 663,280.00 USD | 663,280.00 USD | 19,950.00 USD | 11,440.00 USD | 38,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.00` | 1,990,000.00 USD | 1,990,000.00 USD | 35,900.00 USD | 0.00 USD | 2,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.10` | 593,450.00 USD | 593,450.00 USD | 3,850.00 USD | 53,510.00 USD | 51,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.10` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 18,510.00 USD | 602.10 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.20` | 484,520.00 USD | 484,520.00 USD | 24,740.00 USD | 7,520.00 USD | 58,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.20` | 1,930,000.00 USD | 1,930,000.00 USD | 57,400.00 USD | 59,710.00 USD | 150,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.30` | 393,730.00 USD | 393,730.00 USD | 39,800.00 USD | 22,650.00 USD | 51,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.30` | 1,660,000.00 USD | 1,660,000.00 USD | 23,140.00 USD | 11,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.40` | 279,520.00 USD | 279,520.00 USD | 0.00 USD | 6,510.00 USD | 742.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.40` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 18,550.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.50` | 272,270.00 USD | 272,270.00 USD | 0.00 USD | 9,250.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.50` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 33,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.60` | 1,570,000.00 USD | 1,570,000.00 USD | 426,340.00 USD | 13,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.70` | 257,510.00 USD | 257,510.00 USD | 0.00 USD | 7,490.00 USD | 613.46 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.70` | 1,130,000.00 USD | 1,130,000.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.80` | 249,410.00 USD | 249,410.00 USD | 6,170.00 USD | 26,160.00 USD | 3,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.80` | 922,810.00 USD | 922,810.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.90` | 213,740.00 USD | 213,740.00 USD | 103,700.00 USD | 13,230.00 USD | 89,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.90` | 831,840.00 USD | 831,840.00 USD | 141,330.00 USD | 101,960.00 USD | 117,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.00` | 7,690.00 USD | 7,690.00 USD | 0.00 USD | 3,180.00 USD | 4,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.00` | 470,900.00 USD | 470,900.00 USD | 181,230.00 USD | 118,560.00 USD | 171,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.10` | 74,130.00 USD | 74,130.00 USD | 68,240.00 USD | 5,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.10` | 148,270.00 USD | 148,270.00 USD | 68,240.00 USD | 5,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.10` | 338,000.00 USD | 338,000.00 USD | 121,920.00 USD | 154,860.00 USD | 61,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.10` | 675,990.00 USD | 675,990.00 USD | 121,920.00 USD | 154,860.00 USD | 61,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.20` | 996,680.00 USD | 996,680.00 USD | 0.00 USD | 79,940.00 USD | 240,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.30` | 196,590.00 USD | 196,590.00 USD | 0.00 USD | 44,360.00 USD | 3,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.30` | 1,000,000.00 USD | 1,000,000.00 USD | 1,270.00 USD | 0.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.40` | 222,080.00 USD | 222,080.00 USD | 5,040.00 USD | 17,690.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.40` | 1,010,000.00 USD | 1,010,000.00 USD | 2,650.00 USD | 11,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.50` | 636,660.00 USD | 636,660.00 USD | 138,540.00 USD | 131,430.00 USD | 144,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.50` | 1,330,000.00 USD | 1,330,000.00 USD | 170,750.00 USD | 143,420.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.60` | 871,360.00 USD | 871,360.00 USD | 49,560.00 USD | 104,240.00 USD | 80,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.60` | 1,830,000.00 USD | 1,830,000.00 USD | 363,190.00 USD | 136,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.70` | 1,300,000.00 USD | 1,300,000.00 USD | 97,300.00 USD | 27,730.00 USD | 307,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.70` | 2,170,000.00 USD | 2,170,000.00 USD | 117,290.00 USD | 121,500.00 USD | 98,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.80` | 1,510,000.00 USD | 1,510,000.00 USD | 117,760.00 USD | 17,250.00 USD | 68,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.80` | 2,720,000.00 USD | 2,720,000.00 USD | 153,580.00 USD | 92,780.00 USD | 303,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.90` | 1,580,000.00 USD | 1,580,000.00 USD | 38,540.00 USD | 10,710.00 USD | 22,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.90` | 3,150,000.00 USD | 3,150,000.00 USD | 113,780.00 USD | 48,600.00 USD | 266,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.00` | 1,620,000.00 USD | 1,620,000.00 USD | 6,480.00 USD | 18,250.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.00` | 3,410,000.00 USD | 3,410,000.00 USD | 88,680.00 USD | 20,690.00 USD | 151,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.10` | 1,730,000.00 USD | 1,730,000.00 USD | 59,550.00 USD | 25,050.00 USD | 25,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.10` | 3,490,000.00 USD | 3,490,000.00 USD | 36,580.00 USD | 19,180.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.20` | 1,870,000.00 USD | 1,870,000.00 USD | 32,320.00 USD | 35,770.00 USD | 74,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.20` | 3,570,000.00 USD | 3,570,000.00 USD | 57,060.00 USD | 21,090.00 USD | 5,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.30` | 1,990,000.00 USD | 1,990,000.00 USD | 24,260.00 USD | 36,820.00 USD | 58,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.30` | 3,660,000.00 USD | 3,660,000.00 USD | 22,360.00 USD | 28,570.00 USD | 34,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.40` | 2,180,000.00 USD | 2,180,000.00 USD | 70,320.00 USD | 45,150.00 USD | 70,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.40` | 4,110,000.00 USD | 4,110,000.00 USD | 124,180.00 USD | 72,180.00 USD | 257,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.50` | 2,580,000.00 USD | 2,580,000.00 USD | 184,770.00 USD | 48,350.00 USD | 167,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.50` | 4,240,000.00 USD | 4,240,000.00 USD | 99,810.00 USD | 31,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.60` | 2,730,000.00 USD | 2,730,000.00 USD | 69,720.00 USD | 24,050.00 USD | 62,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.60` | 4,460,000.00 USD | 4,460,000.00 USD | 149,560.00 USD | 40,430.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.70` | 2,890,000.00 USD | 2,890,000.00 USD | 36,620.00 USD | 26,070.00 USD | 96,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.70` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 5,400.00 USD | 57,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.75` | 155.35 USD | 155.35 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `57.80` | 2,990,000.00 USD | 2,990,000.00 USD | 9,690.00 USD | 13,860.00 USD | 73,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.80` | 4,600,000.00 USD | 4,600,000.00 USD | 9,650.00 USD | 14,360.00 USD | 49,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.90` | 3,030,000.00 USD | 3,030,000.00 USD | 13,000.00 USD | 14,100.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.90` | 4,630,000.00 USD | 4,630,000.00 USD | 5,120.00 USD | 963.90 USD | 22,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.95` | 125.75 USD | 281.10 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.00` | 3,040,000.00 USD | 3,040,000.00 USD | 4,580.00 USD | 5,870.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.00` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 3,670.00 USD | 86,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.10` | 3,100,000.00 USD | 3,100,000.00 USD | 31,400.00 USD | 6,730.00 USD | 15,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.10` | 4,720,000.00 USD | 4,720,000.00 USD | 5,470.00 USD | 1,310.00 USD | 848.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.20` | 3,130,000.00 USD | 3,130,000.00 USD | 27,190.00 USD | 8,710.00 USD | 406.15 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.20` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 1,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.30` | 3,210,000.00 USD | 3,210,000.00 USD | 21,400.00 USD | 17,260.00 USD | 41,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.30` | 4,780,000.00 USD | 4,780,000.00 USD | 17,950.00 USD | 9,580.00 USD | 27,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.40` | 3,270,000.00 USD | 3,270,000.00 USD | 2,240.00 USD | 15,040.00 USD | 35,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.40` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 9,260.00 USD | 54,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.50` | 3,300,000.00 USD | 3,300,000.00 USD | 21,130.00 USD | 8,030.00 USD | 124.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.50` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.60` | 3,350,000.00 USD | 3,350,000.00 USD | 14,490.00 USD | 3,760.00 USD | 36,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.60` | 4,970,000.00 USD | 4,970,000.00 USD | 30,680.00 USD | 20,260.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.70` | 3,420,000.00 USD | 3,420,000.00 USD | 38,020.00 USD | 10,060.00 USD | 26,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.70` | 5,040,000.00 USD | 5,040,000.00 USD | 15,810.00 USD | 11,600.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.80` | 3,500,000.00 USD | 3,500,000.00 USD | 35,830.00 USD | 14,730.00 USD | 23,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.80` | 5,050,000.00 USD | 5,050,000.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.90` | 3,700,000.00 USD | 3,700,000.00 USD | 22,130.00 USD | 91,210.00 USD | 90,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.90` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 54,240.00 USD | 83,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.00` | 4,020,000.00 USD | 4,020,000.00 USD | 129,180.00 USD | 58,790.00 USD | 127,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.00` | 5,630,000.00 USD | 5,630,000.00 USD | 259,280.00 USD | 65,270.00 USD | 118,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.10` | 4,310,000.00 USD | 4,310,000.00 USD | 91,380.00 USD | 39,780.00 USD | 163,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.10` | 5,920,000.00 USD | 5,920,000.00 USD | 91,060.00 USD | 45,400.00 USD | 158,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.20` | 4,520,000.00 USD | 4,520,000.00 USD | 101,760.00 USD | 59,450.00 USD | 49,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.20` | 6,270,000.00 USD | 6,270,000.00 USD | 153,580.00 USD | 18,540.00 USD | 174,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.30` | 4,830,000.00 USD | 4,830,000.00 USD | 171,630.00 USD | 45,010.00 USD | 94,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.30` | 6,550,000.00 USD | 6,550,000.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.35` | 9,440.00 USD | 9,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.40` | 5,000,000.00 USD | 5,000,000.00 USD | 64,900.00 USD | 45,810.00 USD | 59,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.40` | 6,860,000.00 USD | 6,860,000.00 USD | 105,490.00 USD | 73,620.00 USD | 137,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.50` | 5,170,000.00 USD | 5,170,000.00 USD | 89,030.00 USD | 38,560.00 USD | 33,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.50` | 7,020,000.00 USD | 7,020,000.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.60` | 5,270,000.00 USD | 5,270,000.00 USD | 43,670.00 USD | 53,100.00 USD | 7,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.60` | 7,520,000.00 USD | 7,520,000.00 USD | 270,460.00 USD | 147,800.00 USD | 86,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.70` | 5,380,000.00 USD | 5,380,000.00 USD | 13,470.00 USD | 19,120.00 USD | 78,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.70` | 7,920,000.00 USD | 7,920,000.00 USD | 55,510.00 USD | 180,620.00 USD | 162,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.80` | 5,450,000.00 USD | 5,450,000.00 USD | 31,530.00 USD | 26,470.00 USD | 10,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.80` | 8,290,000.00 USD | 8,290,000.00 USD | 118,240.00 USD | 97,600.00 USD | 155,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.90` | 5,630,000.00 USD | 5,630,000.00 USD | 112,000.00 USD | 20,240.00 USD | 50,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.90` | 8,620,000.00 USD | 8,620,000.00 USD | 209,780.00 USD | 83,540.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.00` | 5,890,000.00 USD | 5,890,000.00 USD | 164,190.00 USD | 44,230.00 USD | 50,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.00` | 9,070,000.00 USD | 9,070,000.00 USD | 195,800.00 USD | 152,810.00 USD | 94,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.10` | 6,040,000.00 USD | 6,040,000.00 USD | 64,090.00 USD | 28,140.00 USD | 57,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.10` | 9,500,000.00 USD | 9,500,000.00 USD | 217,190.00 USD | 100,570.00 USD | 113,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.15` | 208,880.00 USD | 218,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.20` | 6,200,000.00 USD | 6,200,000.00 USD | 59,560.00 USD | 19,740.00 USD | 82,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.20` | 9,870,000.00 USD | 9,870,000.00 USD | 162,230.00 USD | 99,360.00 USD | 108,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.30` | 6,310,000.00 USD | 6,310,000.00 USD | 53,910.00 USD | 30,600.00 USD | 24,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.30` | 10,270,000.00 USD | 10,270,000.00 USD | 133,350.00 USD | 100,380.00 USD | 170,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.40` | 6,430,000.00 USD | 6,430,000.00 USD | 66,740.00 USD | 13,730.00 USD | 39,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.40` | 10,650,000.00 USD | 10,650,000.00 USD | 64,850.00 USD | 108,300.00 USD | 204,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.50` | 6,510,000.00 USD | 6,510,000.00 USD | 22,700.00 USD | 19,320.00 USD | 36,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.50` | 11,030,000.00 USD | 11,030,000.00 USD | 115,390.00 USD | 86,870.00 USD | 175,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.60` | 6,570,000.00 USD | 6,570,000.00 USD | 40,710.00 USD | 19,140.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.60` | 11,420,000.00 USD | 11,420,000.00 USD | 251,100.00 USD | 18,640.00 USD | 118,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.70` | 6,630,000.00 USD | 6,630,000.00 USD | 34,230.00 USD | 22,330.00 USD | 3,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.70` | 11,620,000.00 USD | 11,620,000.00 USD | 119,080.00 USD | 57,480.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.80` | 6,710,000.00 USD | 6,710,000.00 USD | 15,430.00 USD | 12,060.00 USD | 47,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.80` | 11,810,000.00 USD | 11,810,000.00 USD | 46,960.00 USD | 69,290.00 USD | 76,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.90` | 6,790,000.00 USD | 6,790,000.00 USD | 35,570.00 USD | 21,920.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.90` | 12,010,000.00 USD | 12,010,000.00 USD | 105,970.00 USD | 34,400.00 USD | 65,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.95` | 397.39 USD | 219,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.00` | 6,860,000.00 USD | 6,860,000.00 USD | 44,070.00 USD | 6,430.00 USD | 18,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 12,130,000.00 USD | 12,130,000.00 USD | 77,670.00 USD | 36,060.00 USD | 5,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.10` | 6,890,000.00 USD | 6,890,000.00 USD | 12,010.00 USD | 6,270.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 12,170,000.00 USD | 12,170,000.00 USD | 31,540.00 USD | 1,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.15` | 3,870.00 USD | 222,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.20` | 7,000,000.00 USD | 7,000,000.00 USD | 72,520.00 USD | 0.00 USD | 38,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.20` | 12,380,000.00 USD | 12,380,000.00 USD | 98,820.00 USD | 60,240.00 USD | 52,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.30` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 3,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.30` | 12,460,000.00 USD | 12,460,000.00 USD | 27,780.00 USD | 21,000.00 USD | 33,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.40` | 7,000,000.00 USD | 7,000,000.00 USD | 1,190.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.40` | 12,590,000.00 USD | 12,590,000.00 USD | 66,470.00 USD | 25,720.00 USD | 35,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.50` | 7,010,000.00 USD | 7,010,000.00 USD | 1,060.00 USD | 333.03 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.50` | 12,680,000.00 USD | 12,680,000.00 USD | 19,810.00 USD | 35,300.00 USD | 36,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.60` | 7,020,000.00 USD | 7,020,000.00 USD | 5,360.00 USD | 2,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.60` | 12,890,000.00 USD | 12,890,000.00 USD | 38,370.00 USD | 50,880.00 USD | 121,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.70` | 7,030,000.00 USD | 7,030,000.00 USD | 10,770.00 USD | 2,110.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.70` | 13,080,000.00 USD | 13,080,000.00 USD | 75,210.00 USD | 10,880.00 USD | 99,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.80` | 7,050,000.00 USD | 7,050,000.00 USD | 3,480.00 USD | 2,640.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.80` | 13,320,000.00 USD | 13,320,000.00 USD | 158,760.00 USD | 25,670.00 USD | 62,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.90` | 7,060,000.00 USD | 7,060,000.00 USD | 4,800.00 USD | 1,440.00 USD | 11,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.90` | 13,470,000.00 USD | 13,470,000.00 USD | 72,920.00 USD | 32,820.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.00` | 7,090,000.00 USD | 7,090,000.00 USD | 15,300.00 USD | 3,100.00 USD | 8,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.00` | 13,570,000.00 USD | 13,570,000.00 USD | 50,080.00 USD | 8,550.00 USD | 40,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.10` | 7,090,000.00 USD | 7,090,000.00 USD | 2,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.10` | 13,580,000.00 USD | 13,580,000.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.20` | 13,690,000.00 USD | 13,690,000.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.30` | 13,840,000.00 USD | 13,840,000.00 USD | 29,050.00 USD | 23,450.00 USD | 97,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.40` | 13,980,000.00 USD | 13,980,000.00 USD | 77,960.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.50` | 14,060,000.00 USD | 14,060,000.00 USD | 42,730.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.60` | 14,130,000.00 USD | 14,130,000.00 USD | 33,900.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.70` | 14,210,000.00 USD | 14,210,000.00 USD | 22,020.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.80` | 14,360,000.00 USD | 14,360,000.00 USD | 71,230.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.90` | 14,450,000.00 USD | 14,450,000.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `62.95` | 138.49 USD | 223,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `63.00` | 14,510,000.00 USD | 14,510,000.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.10` | 14,550,000.00 USD | 14,550,000.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.30` | 14,590,000.00 USD | 14,590,000.00 USD | 15,010.00 USD | 11,500.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.40` | 14,610,000.00 USD | 14,610,000.00 USD | 11,980.00 USD | 1,320.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `63.45` | 3,350.00 USD | 226,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `63.50` | 14,640,000.00 USD | 14,640,000.00 USD | 5,430.00 USD | 15,810.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.60` | 14,740,000.00 USD | 14,740,000.00 USD | 63,480.00 USD | 20,800.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.70` | 14,810,000.00 USD | 14,810,000.00 USD | 21,940.00 USD | 18,810.00 USD | 35,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.80` | 14,880,000.00 USD | 14,880,000.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.90` | 14,900,000.00 USD | 14,900,000.00 USD | 7,650.00 USD | 12,840.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.00` | 14,950,000.00 USD | 14,950,000.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.10` | 14,980,000.00 USD | 14,980,000.00 USD | 20,350.00 USD | 667.05 USD | 10,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.20` | 15,020,000.00 USD | 15,020,000.00 USD | 28,840.00 USD | 14,530.00 USD | 584.77 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.40` | 15,070,000.00 USD | 15,070,000.00 USD | 0.00 USD | 17,760.00 USD | 29,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `66.15` | 6,750.00 USD | 233,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.95` | 121.18 USD | 233,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.85` | 709.03 USD | 233,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `69.95` | 40,440.00 USD | 274,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `76.35` | 8,380.00 USD | 282,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.75` | 578,460.00 USD | 861,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.85` | 602.56 USD | 861,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.95` | 136.41 USD | 861,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.75` | 646.00 USD | 862,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.05` | 19,000.00 USD | 881,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.55` | 123.96 USD | 881,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.75` | 2,700.00 USD | 884,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.75` | 3,520.00 USD | 887,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `83.95` | 761.43 USD | 888,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `87.95` | 23,470.00 USD | 912,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `89.85` | 955.11 USD | 913,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `89.95` | 118.73 USD | 913,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `92.05` | 155.56 USD | 913,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.65` | 2,470.00 USD | 915,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.95` | 31,180.00 USD | 947,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.25` | 213.71 USD | 947,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.85` | 2,320.00 USD | 949,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.25` | 355,110.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.75` | 1,620.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.85` | 1,860.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.15` | 199.30 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.05` | 6,470.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 664.59 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `11.35` | 3,020,000.00 USD | 0.00 USD | 136.20 USD | `-79.79%` | `12.00` |
| `Live` | `Long` | `12.25` | 3,020,000.00 USD | 0.00 USD | 122.50 USD | `-78.19%` | `10.00` |
| `Live` | `Long` | `12.75` | 3,020,000.00 USD | 0.00 USD | 2,560.00 USD | `-77.30%` | `200.43` |
| `Live` | `Long` | `13.15` | 3,020,000.00 USD | 0.00 USD | 2,220.00 USD | `-76.59%` | `168.79` |
| `Live` | `Long` | `13.65` | 3,020,000.00 USD | 0.00 USD | 150.15 USD | `-75.70%` | `11.00` |
| `Live` | `Long` | `15.75` | 3,020,000.00 USD | 0.00 USD | 2,370.00 USD | `-71.96%` | `150.57` |
| `Live` | `Long` | `16.65` | 3,010,000.00 USD | 0.00 USD | 370.30 USD | `-70.36%` | `22.24` |
| `Live` | `Long` | `17.15` | 3,010,000.00 USD | 0.00 USD | 128.11 USD | `-69.47%` | `7.47` |
| `Live` | `Long` | `17.45` | 3,010,000.00 USD | 0.00 USD | 140.47 USD | `-68.93%` | `8.05` |
| `Live` | `Long` | `17.85` | 3,010,000.00 USD | 0.00 USD | 2,140.00 USD | `-68.22%` | `120.00` |
| `Live` | `Long` | `18.25` | 3,010,000.00 USD | 0.00 USD | 164.61 USD | `-67.51%` | `9.02` |
| `Live` | `Long` | `19.05` | 3,010,000.00 USD | 0.00 USD | 3,470.00 USD | `-66.08%` | `182.00` |
| `Live` | `Long` | `19.45` | 3,010,000.00 USD | 0.00 USD | 2,010.00 USD | `-65.37%` | `103.47` |
| `Live` | `Long` | `19.95` | 3,010,000.00 USD | 0.00 USD | 18,550.00 USD | `-64.48%` | `930.00` |
| `Live` | `Long` | `20.25` | 2,990,000.00 USD | 0.00 USD | 133.65 USD | `-63.95%` | `6.60` |
| `Live` | `Long` | `20.75` | 2,990,000.00 USD | 0.00 USD | 4,050.00 USD | `-63.06%` | `195.03` |
| `Live` | `Long` | `22.15` | 2,980,000.00 USD | 0.00 USD | 1,330.00 USD | `-60.56%` | `60.00` |
| `Live` | `Long` | `22.45` | 2,980,000.00 USD | 0.00 USD | 362.12 USD | `-60.03%` | `16.13` |
| `Live` | `Long` | `22.55` | 2,980,000.00 USD | 0.00 USD | 466.56 USD | `-59.85%` | `20.69` |
| `Live` | `Long` | `23.35` | 2,980,000.00 USD | 0.00 USD | 990.74 USD | `-58.43%` | `42.43` |
| `Live` | `Long` | `23.45` | 2,980,000.00 USD | 0.00 USD | 370.98 USD | `-58.25%` | `15.82` |
| `Live` | `Long` | `23.65` | 2,980,000.00 USD | 0.00 USD | 920.46 USD | `-57.89%` | `38.92` |
| `Live` | `Long` | `23.85` | 2,980,000.00 USD | 0.00 USD | 195.57 USD | `-57.54%` | `8.20` |
| `Live` | `Long` | `24.55` | 2,980,000.00 USD | 0.00 USD | 7,230.00 USD | `-56.29%` | `294.67` |
| `Live` | `Long` | `24.65` | 2,970,000.00 USD | 0.00 USD | 113,020.00 USD | `-56.11%` | `4,584.81` |
| `Live` | `Long` | `25.25` | 2,860,000.00 USD | 0.00 USD | 277,980.00 USD | `-55.04%` | `11,009.19` |
| `Live` | `Long` | `25.35` | 2,580,000.00 USD | 0.00 USD | 173.39 USD | `-54.87%` | `6.84` |
| `Live` | `Long` | `25.45` | 2,580,000.00 USD | 0.00 USD | 7,640.00 USD | `-54.69%` | `300.00` |
| `Live` | `Long` | `25.55` | 2,570,000.00 USD | 0.00 USD | 50,740.00 USD | `-54.51%` | `1,985.99` |
| `Live` | `Long` | `25.95` | 2,520,000.00 USD | 0.00 USD | 374.20 USD | `-53.80%` | `14.42` |
| `Live` | `Long` | `26.05` | 2,520,000.00 USD | 0.00 USD | 721.85 USD | `-53.62%` | `27.71` |
| `Live` | `Long` | `27.05` | 2,520,000.00 USD | 0.00 USD | 5,510.00 USD | `-51.84%` | `203.85` |
| `Live` | `Long` | `27.55` | 2,520,000.00 USD | 0.00 USD | 435.57 USD | `-50.95%` | `15.81` |
| `Live` | `Long` | `27.95` | 2,520,000.00 USD | 0.00 USD | 173.85 USD | `-50.24%` | `6.22` |
| `Live` | `Long` | `29.15` | 2,520,000.00 USD | 0.00 USD | 583.00 USD | `-48.10%` | `20.00` |
| `Live` | `Long` | `29.75` | 2,510,000.00 USD | 0.00 USD | 297,500.00 USD | `-47.03%` | `10,000.00` |
| `Live` | `Long` | `30.05` | 2,220,000.00 USD | 0.00 USD | 218.46 USD | `-46.50%` | `7.27` |
| `Live` | `Long` | `30.55` | 2,220,000.00 USD | 0.00 USD | 725.56 USD | `-45.61%` | `23.75` |
| `Live` | `Long` | `30.65` | 2,220,000.00 USD | 0.00 USD | 1,750.00 USD | `-45.43%` | `57.19` |
| `Live` | `Long` | `30.95` | 2,210,000.00 USD | 0.00 USD | 538.53 USD | `-44.90%` | `17.40` |
| `Live` | `Long` | `31.15` | 2,210,000.00 USD | 0.00 USD | 27,620.00 USD | `-44.54%` | `886.80` |
| `Live` | `Long` | `31.55` | 2,190,000.00 USD | 0.00 USD | 1,060.00 USD | `-43.83%` | `33.49` |
| `Live` | `Long` | `31.65` | 2,190,000.00 USD | 0.00 USD | 7,340.00 USD | `-43.65%` | `231.96` |
| `Live` | `Long` | `31.85` | 2,180,000.00 USD | 0.00 USD | 2,870.00 USD | `-43.29%` | `90.00` |
| `Live` | `Long` | `31.95` | 2,170,000.00 USD | 0.00 USD | 125.24 USD | `-43.12%` | `3.92` |
| `Live` | `Long` | `32.15` | 2,170,000.00 USD | 0.00 USD | 450.10 USD | `-42.76%` | `14.00` |
| `Live` | `Long` | `32.25` | 2,170,000.00 USD | 0.00 USD | 4,000.00 USD | `-42.58%` | `124.01` |
| `Live` | `Long` | `32.35` | 2,170,000.00 USD | 0.00 USD | 172.10 USD | `-42.40%` | `5.32` |
| `Live` | `Long` | `32.45` | 2,170,000.00 USD | 0.00 USD | 405.30 USD | `-42.23%` | `12.49` |
| `Live` | `Long` | `32.65` | 2,170,000.00 USD | 0.00 USD | 653.00 USD | `-41.87%` | `20.00` |
| `Live` | `Long` | `32.75` | 2,170,000.00 USD | 0.00 USD | 953.68 USD | `-41.69%` | `29.12` |
| `Live` | `Long` | `32.85` | 2,170,000.00 USD | 0.00 USD | 32,850.00 USD | `-41.51%` | `1,000.01` |
| `Live` | `Long` | `33.05` | 2,140,000.00 USD | 0.00 USD | 5,760.00 USD | `-41.16%` | `174.22` |
| `Live` | `Long` | `33.65` | 2,130,000.00 USD | 0.00 USD | 257.76 USD | `-40.09%` | `7.66` |
| `Live` | `Long` | `33.75` | 2,130,000.00 USD | 0.00 USD | 402.30 USD | `-39.91%` | `11.92` |
| `Live` | `Long` | `33.95` | 2,130,000.00 USD | 0.00 USD | 4,430.00 USD | `-39.55%` | `130.63` |
| `Live` | `Long` | `34.05` | 2,120,000.00 USD | 0.00 USD | 182.85 USD | `-39.38%` | `5.37` |
| `Live` | `Long` | `34.15` | 2,120,000.00 USD | 0.00 USD | 126.70 USD | `-39.20%` | `3.71` |
| `Live` | `Long` | `34.45` | 2,120,000.00 USD | 0.00 USD | 65,890.00 USD | `-38.66%` | `1,912.61` |
| `Live` | `Long` | `34.65` | 2,060,000.00 USD | 0.00 USD | 3,240.00 USD | `-38.31%` | `93.56` |
| `Live` | `Long` | `34.95` | 2,050,000.00 USD | 0.00 USD | 104.85 USD | `-37.77%` | `3.00` |
| `Live` | `Long` | `35.05` | 2,050,000.00 USD | 0.00 USD | 440.93 USD | `-37.60%` | `12.58` |
| `Live` | `Long` | `35.95` | 2,050,000.00 USD | 0.00 USD | 275.74 USD | `-35.99%` | `7.67` |
| `Live` | `Long` | `36.35` | 2,050,000.00 USD | 0.00 USD | 3,020.00 USD | `-35.28%` | `83.03` |
| `Live` | `Long` | `36.45` | 2,050,000.00 USD | 0.00 USD | 1,690.00 USD | `-35.10%` | `46.28` |
| `Live` | `Long` | `36.55` | 2,050,000.00 USD | 0.00 USD | 1,830.00 USD | `-34.93%` | `50.00` |
| `Live` | `Long` | `36.75` | 2,050,000.00 USD | 0.00 USD | 101.80 USD | `-34.57%` | `2.77` |
| `Live` | `Long` | `37.05` | 2,050,000.00 USD | 0.00 USD | 1,050.00 USD | `-34.04%` | `28.27` |
| `Live` | `Long` | `37.15` | 2,050,000.00 USD | 0.00 USD | 438.74 USD | `-33.86%` | `11.81` |
| `Live` | `Long` | `37.35` | 2,050,000.00 USD | 0.00 USD | 9,260.00 USD | `-33.50%` | `247.91` |
| `Live` | `Long` | `37.55` | 2,040,000.00 USD | 0.00 USD | 3,530.00 USD | `-33.15%` | `94.04` |
| `Live` | `Long` | `37.75` | 2,030,000.00 USD | 0.00 USD | 377.50 USD | `-32.79%` | `10.00` |
| `Live` | `Long` | `37.85` | 2,030,000.00 USD | 0.00 USD | 6,210.00 USD | `-32.61%` | `164.03` |
| `Live` | `Long` | `37.95` | 2,030,000.00 USD | 0.00 USD | 446.67 USD | `-32.43%` | `11.77` |
| `Live` | `Long` | `38.25` | 2,030,000.00 USD | 0.00 USD | 695.38 USD | `-31.90%` | `18.18` |
| `Live` | `Long` | `38.35` | 2,030,000.00 USD | 0.00 USD | 847.54 USD | `-31.72%` | `22.10` |
| `Live` | `Long` | `38.45` | 2,020,000.00 USD | 0.00 USD | 2,400.00 USD | `-31.54%` | `62.34` |
| `Live` | `Long` | `38.55` | 2,020,000.00 USD | 0.00 USD | 993.82 USD | `-31.36%` | `25.78` |
| `Live` | `Long` | `38.65` | 2,020,000.00 USD | 0.00 USD | 4,280.00 USD | `-31.19%` | `110.74` |
| `Live` | `Long` | `38.95` | 2,020,000.00 USD | 0.00 USD | 3,700.00 USD | `-30.65%` | `94.93` |
| `Live` | `Long` | `39.05` | 2,010,000.00 USD | 0.00 USD | 664,760.00 USD | `-30.47%` | `17,023.28` |
| `Live` | `Long` | `39.15` | 1,350,000.00 USD | 0.00 USD | 570.02 USD | `-30.30%` | `14.56` |
| `Live` | `Long` | `39.35` | 1,350,000.00 USD | 0.00 USD | 264.83 USD | `-29.94%` | `6.73` |
| `Live` | `Long` | `39.45` | 1,350,000.00 USD | 0.00 USD | 716.41 USD | `-29.76%` | `18.16` |
| `Live` | `Long` | `39.55` | 1,350,000.00 USD | 0.00 USD | 312.44 USD | `-29.58%` | `7.90` |
| `Live` | `Long` | `39.65` | 1,350,000.00 USD | 0.00 USD | 5,900.00 USD | `-29.41%` | `148.78` |
| `Live` | `Long` | `39.75` | 1,340,000.00 USD | 0.00 USD | 1,180.00 USD | `-29.23%` | `29.57` |
| `Live` | `Long` | `39.85` | 1,340,000.00 USD | 0.00 USD | 133.10 USD | `-29.05%` | `3.34` |
| `Live` | `Long` | `40.05` | 1,340,000.00 USD | 0.00 USD | 2,160.00 USD | `-28.69%` | `53.97` |
| `Live` | `Long` | `40.35` | 1,340,000.00 USD | 0.00 USD | 8,880.00 USD | `-28.16%` | `220.00` |
| `Live` | `Long` | `40.45` | 1,330,000.00 USD | 0.00 USD | 1,010.00 USD | `-27.98%` | `24.92` |
| `Live` | `Long` | `40.55` | 1,330,000.00 USD | 0.00 USD | 133.00 USD | `-27.80%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,330,000.00 USD | 0.00 USD | 274.39 USD | `-27.63%` | `6.75` |
| `Live` | `Long` | `40.85` | 1,330,000.00 USD | 0.00 USD | 6,340.00 USD | `-27.27%` | `155.23` |
| `Live` | `Long` | `40.95` | 1,320,000.00 USD | 0.00 USD | 5,910.00 USD | `-27.09%` | `144.37` |
| `Live` | `Long` | `41.05` | 1,310,000.00 USD | 0.00 USD | 396.54 USD | `-26.91%` | `9.66` |
| `Live` | `Long` | `41.25` | 1,310,000.00 USD | 0.00 USD | 17,770.00 USD | `-26.56%` | `430.75` |
| `Live` | `Long` | `41.45` | 1,300,000.00 USD | 0.00 USD | 940.50 USD | `-26.20%` | `22.69` |
| `Live` | `Long` | `41.75` | 1,300,000.00 USD | 0.00 USD | 313.12 USD | `-25.67%` | `7.50` |
| `Live` | `Long` | `41.85` | 1,300,000.00 USD | 0.00 USD | 5,390.00 USD | `-25.49%` | `128.71` |
| `Live` | `Long` | `42.05` | 1,290,000.00 USD | 0.00 USD | 982.29 USD | `-25.13%` | `23.36` |
| `Live` | `Long` | `42.15` | 1,290,000.00 USD | 0.00 USD | 108,450.00 USD | `-24.96%` | `2,572.94` |
| `Live` | `Long` | `42.25` | 1,180,000.00 USD | 0.00 USD | 35,410.00 USD | `-24.78%` | `838.00` |
| `Live` | `Long` | `42.45` | 1,150,000.00 USD | 0.00 USD | 3,850.00 USD | `-24.42%` | `90.60` |
| `Live` | `Long` | `42.65` | 1,140,000.00 USD | 0.00 USD | 1,570.00 USD | `-24.07%` | `36.70` |
| `Live` | `Long` | `42.85` | 1,140,000.00 USD | 0.00 USD | 5,800.00 USD | `-23.71%` | `135.38` |
| `Live` | `Long` | `42.95` | 1,130,000.00 USD | 0.00 USD | 2,000.00 USD | `-23.53%` | `46.65` |
| `Live` | `Long` | `43.05` | 1,130,000.00 USD | 0.00 USD | 9,080.00 USD | `-23.35%` | `211.00` |
| `Live` | `Long` | `43.15` | 1,120,000.00 USD | 0.00 USD | 122,400.00 USD | `-23.17%` | `2,836.59` |
| `Live` | `Long` | `43.25` | 1,000,000.00 USD | 0.00 USD | 417.80 USD | `-23.00%` | `9.66` |
| `Live` | `Long` | `43.35` | 999,960.00 USD | 0.00 USD | 5,390.00 USD | `-22.82%` | `124.24` |
| `Live` | `Long` | `43.45` | 994,570.00 USD | 0.00 USD | 710.84 USD | `-22.64%` | `16.36` |
| `Live` | `Long` | `43.65` | 993,860.00 USD | 0.00 USD | 426.02 USD | `-22.28%` | `9.76` |
| `Live` | `Long` | `43.75` | 993,430.00 USD | 0.00 USD | 21,880.00 USD | `-22.11%` | `500.00` |
| `Live` | `Long` | `43.85` | 971,560.00 USD | 0.00 USD | 801.14 USD | `-21.93%` | `18.27` |
| `Live` | `Long` | `44.15` | 970,760.00 USD | 0.00 USD | 2,380.00 USD | `-21.39%` | `53.99` |
| `Live` | `Long` | `44.25` | 968,370.00 USD | 0.00 USD | 1,330.00 USD | `-21.22%` | `30.00` |
| `Live` | `Long` | `44.35` | 967,050.00 USD | 0.00 USD | 85,770.00 USD | `-21.04%` | `1,933.87` |
| `Live` | `Long` | `44.55` | 881,280.00 USD | 0.00 USD | 842.44 USD | `-20.68%` | `18.91` |
| `Live` | `Long` | `44.75` | 880,440.00 USD | 0.00 USD | 4,230.00 USD | `-20.33%` | `94.55` |
| `Live` | `Long` | `44.85` | 876,210.00 USD | 0.00 USD | 134.55 USD | `-20.15%` | `3.00` |
| `Live` | `Long` | `44.95` | 876,070.00 USD | 0.00 USD | 2,620.00 USD | `-19.97%` | `58.18` |
| `Live` | `Long` | `45.05` | 873,460.00 USD | 0.00 USD | 4,830.00 USD | `-19.79%` | `107.31` |
| `Live` | `Long` | `45.15` | 868,620.00 USD | 0.00 USD | 8,710.00 USD | `-19.61%` | `193.00` |
| `Live` | `Long` | `45.25` | 859,910.00 USD | 0.00 USD | 3,180.00 USD | `-19.44%` | `70.37` |
| `Live` | `Long` | `45.35` | 856,720.00 USD | 0.00 USD | 2,180.00 USD | `-19.26%` | `48.02` |
| `Live` | `Long` | `45.45` | 854,550.00 USD | 0.00 USD | 23,940.00 USD | `-19.08%` | `526.65` |
| `Live` | `Long` | `45.55` | 830,610.00 USD | 0.00 USD | 12,060.00 USD | `-18.90%` | `264.81` |
| `Live` | `Long` | `45.65` | 818,550.00 USD | 0.00 USD | 42,180.00 USD | `-18.72%` | `924.03` |
| `Live` | `Long` | `45.75` | 776,370.00 USD | 0.00 USD | 27,480.00 USD | `-18.55%` | `600.68` |
| `Live` | `Long` | `45.85` | 748,880.00 USD | 0.00 USD | 176.06 USD | `-18.37%` | `3.84` |
| `Live` | `Long` | `45.95` | 748,710.00 USD | 0.00 USD | 2,940.00 USD | `-18.19%` | `64.09` |
| `Live` | `Long` | `46.05` | 745,760.00 USD | 0.00 USD | 706.41 USD | `-18.01%` | `15.34` |
| `Live` | `Long` | `46.25` | 745,060.00 USD | 0.00 USD | 22,380.00 USD | `-17.66%` | `483.97` |
| `Live` | `Long` | `46.35` | 722,670.00 USD | 0.00 USD | 383.78 USD | `-17.48%` | `8.28` |
| `Live` | `Long` | `46.55` | 722,290.00 USD | 0.00 USD | 2,140.00 USD | `-17.12%` | `45.93` |
| `Live` | `Long` | `46.65` | 720,150.00 USD | 0.00 USD | 3,980.00 USD | `-16.94%` | `85.41` |
| `Live` | `Long` | `46.75` | 716,170.00 USD | 0.00 USD | 269.28 USD | `-16.77%` | `5.76` |
| `Live` | `Long` | `46.85` | 715,900.00 USD | 0.00 USD | 358.40 USD | `-16.59%` | `7.65` |
| `Live` | `Long` | `46.95` | 715,540.00 USD | 0.00 USD | 533.35 USD | `-16.41%` | `11.36` |
| `Live` | `Long` | `47.15` | 715,010.00 USD | 0.00 USD | 1,980.00 USD | `-16.05%` | `42.07` |
| `Live` | `Long` | `47.25` | 713,020.00 USD | 0.00 USD | 646.85 USD | `-15.88%` | `13.69` |
| `Live` | `Long` | `47.35` | 712,380.00 USD | 0.00 USD | 43,920.00 USD | `-15.70%` | `927.56` |
| `Live` | `Long` | `47.45` | 668,460.00 USD | 0.00 USD | 2,590.00 USD | `-15.52%` | `54.54` |
| `Live` | `Long` | `47.55` | 665,870.00 USD | 0.00 USD | 4,450.00 USD | `-15.34%` | `93.69` |
| `Live` | `Long` | `47.75` | 661,410.00 USD | 0.00 USD | 47,750.00 USD | `-14.98%` | `1,000.00` |
| `Live` | `Long` | `47.95` | 613,660.00 USD | 0.00 USD | 7,890.00 USD | `-14.63%` | `164.58` |
| `Live` | `Long` | `48.05` | 605,770.00 USD | 0.00 USD | 1,340.00 USD | `-14.45%` | `27.93` |
| `Live` | `Long` | `48.15` | 604,430.00 USD | 0.00 USD | 1,690.00 USD | `-14.27%` | `35.03` |
| `Live` | `Long` | `48.25` | 602,740.00 USD | 0.00 USD | 110.49 USD | `-14.09%` | `2.29` |
| `Live` | `Long` | `48.55` | 602,630.00 USD | 0.00 USD | 2,560.00 USD | `-13.56%` | `52.70` |
| `Live` | `Long` | `48.65` | 600,070.00 USD | 0.00 USD | 273.90 USD | `-13.38%` | `5.63` |
| `Live` | `Long` | `48.75` | 599,800.00 USD | 0.00 USD | 2,220.00 USD | `-13.20%` | `45.64` |
| `Live` | `Long` | `48.95` | 597,580.00 USD | 0.00 USD | 252.58 USD | `-12.85%` | `5.16` |
| `Live` | `Long` | `49.05` | 597,320.00 USD | 0.00 USD | 1,580.00 USD | `-12.67%` | `32.25` |
| `Live` | `Long` | `49.15` | 595,740.00 USD | 0.00 USD | 5,740.00 USD | `-12.49%` | `116.83` |
| `Live` | `Long` | `49.35` | 590,000.00 USD | 0.00 USD | 5,230.00 USD | `-12.14%` | `105.97` |
| `Live` | `Long` | `49.45` | 584,770.00 USD | 0.00 USD | 419.34 USD | `-11.96%` | `8.48` |
| `Live` | `Long` | `49.55` | 584,350.00 USD | 0.00 USD | 18,010.00 USD | `-11.78%` | `363.57` |
| `Live` | `Long` | `49.65` | 566,330.00 USD | 0.00 USD | 73,260.00 USD | `-11.60%` | `1,475.52` |
| `Live` | `Long` | `49.75` | 493,080.00 USD | 0.00 USD | 20,710.00 USD | `-11.42%` | `416.36` |
| `Live` | `Long` | `49.95` | 472,360.00 USD | 0.00 USD | 19,920.00 USD | `-11.07%` | `398.70` |
| `Live` | `Long` | `50.05` | 452,450.00 USD | 0.00 USD | 1,820.00 USD | `-10.89%` | `36.43` |
| `Live` | `Long` | `50.25` | 450,620.00 USD | 0.00 USD | 102.51 USD | `-10.53%` | `2.04` |
| `Live` | `Long` | `50.35` | 450,520.00 USD | 0.00 USD | 1,140.00 USD | `-10.36%` | `22.67` |
| `Live` | `Long` | `50.45` | 449,380.00 USD | 0.00 USD | 4,720.00 USD | `-10.18%` | `93.64` |
| `Live` | `Long` | `50.55` | 444,650.00 USD | 0.00 USD | 84,100.00 USD | `-10.00%` | `1,663.61` |
| `Live` | `Long` | `50.75` | 360,560.00 USD | 0.00 USD | 9,050.00 USD | `-9.64%` | `178.28` |
| `Live` | `Long` | `50.95` | 351,510.00 USD | 0.00 USD | 431.55 USD | `-9.29%` | `8.47` |
| `Live` | `Long` | `51.15` | 351,080.00 USD | 0.00 USD | 219,370.00 USD | `-8.93%` | `4,288.79` |
| `Live` | `Long` | `51.25` | 131,710.00 USD | 0.00 USD | 202.44 USD | `-8.75%` | `3.95` |
| `Live` | `Long` | `51.35` | 131,510.00 USD | 0.00 USD | 453.93 USD | `-8.58%` | `8.84` |
| `Live` | `Long` | `51.45` | 131,050.00 USD | 0.00 USD | 27,210.00 USD | `-8.40%` | `528.81` |
| `Live` | `Long` | `51.55` | 103,840.00 USD | 0.00 USD | 551.07 USD | `-8.22%` | `10.69` |
| `Live` | `Long` | `51.65` | 103,290.00 USD | 0.00 USD | 9,100.00 USD | `-8.04%` | `176.09` |
| `Live` | `Long` | `51.75` | 94,200.00 USD | 0.00 USD | 6,480.00 USD | `-7.86%` | `125.17` |
| `Live` | `Long` | `51.85` | 87,720.00 USD | 0.00 USD | 16,530.00 USD | `-7.69%` | `318.89` |
| `Live` | `Long` | `51.95` | 71,190.00 USD | 0.00 USD | 13,950.00 USD | `-7.51%` | `268.48` |
| `Live` | `Long` | `52.15` | 57,240.00 USD | 0.00 USD | 1,900.00 USD | `-7.15%` | `36.36` |
| `Live` | `Long` | `52.25` | 55,340.00 USD | 0.00 USD | 4,930.00 USD | `-6.97%` | `94.33` |
| `Live` | `Long` | `52.35` | 50,410.00 USD | 0.00 USD | 134.02 USD | `-6.79%` | `2.56` |
| `Live` | `Long` | `52.45` | 50,280.00 USD | 0.00 USD | 2,470.00 USD | `-6.62%` | `47.16` |
| `Live` | `Long` | `52.55` | 47,810.00 USD | 0.00 USD | 8,700.00 USD | `-6.44%` | `165.49` |
| `Live` | `Long` | `52.75` | 39,110.00 USD | 0.00 USD | 4,240.00 USD | `-6.08%` | `80.44` |
| `Live` | `Long` | `52.85` | 34,870.00 USD | 0.00 USD | 5,950.00 USD | `-5.90%` | `112.64` |
| `Live` | `Long` | `52.95` | 28,910.00 USD | 0.00 USD | 25,840.00 USD | `-5.73%` | `488.06` |
| `Live` | `Long` | `53.15` | 3,070.00 USD | 0.00 USD | 1,720.00 USD | `-5.37%` | `32.44` |
| `Live` | `Long` | `53.25` | 1,350.00 USD | 0.00 USD | 405.76 USD | `-5.19%` | `7.62` |
| `Live` | `Long` | `53.35` | 941.09 USD | 0.00 USD | 941.09 USD | `-5.01%` | `17.64` |
| `Live` | `Short` | `57.75` | 155.35 USD | 155.35 USD | 0.00 USD | `+2.82%` | `2.69` |
| `Live` | `Short` | `57.95` | 281.10 USD | 125.75 USD | 0.00 USD | `+3.18%` | `2.17` |
| `Live` | `Short` | `59.35` | 9,720.00 USD | 9,440.00 USD | 0.00 USD | `+5.67%` | `159.09` |
| `Live` | `Short` | `60.15` | 218,600.00 USD | 208,880.00 USD | 0.00 USD | `+7.09%` | `3,472.67` |
| `Live` | `Short` | `60.95` | 219,000.00 USD | 397.39 USD | 0.00 USD | `+8.52%` | `6.52` |
| `Live` | `Short` | `62.95` | 219,140.00 USD | 138.49 USD | 0.00 USD | `+12.08%` | `2.20` |
| `Live` | `Short` | `63.45` | 222,490.00 USD | 3,350.00 USD | 0.00 USD | `+12.97%` | `52.83` |
| `Live` | `Short` | `63.55` | 230,670.00 USD | 8,180.00 USD | 0.00 USD | `+13.15%` | `128.67` |
| `Live` | `Short` | `66.95` | 230,790.00 USD | 121.18 USD | 0.00 USD | `+19.20%` | `1.81` |
| `Live` | `Short` | `67.85` | 231,500.00 USD | 709.03 USD | 0.00 USD | `+20.80%` | `10.45` |
| `Live` | `Short` | `70.55` | 272,280.00 USD | 40,780.00 USD | 0.00 USD | `+25.61%` | `578.10` |
| `Live` | `Short` | `71.35` | 272,400.00 USD | 112.02 USD | 0.00 USD | `+27.03%` | `1.57` |
| `Live` | `Short` | `76.35` | 280,780.00 USD | 8,380.00 USD | 0.00 USD | `+35.94%` | `109.80` |
| `Live` | `Short` | `77.75` | 859,240.00 USD | 578,460.00 USD | 0.00 USD | `+38.43%` | `7,440.05` |
| `Live` | `Short` | `77.85` | 859,850.00 USD | 602.56 USD | 0.00 USD | `+38.61%` | `7.74` |
| `Live` | `Short` | `77.95` | 859,980.00 USD | 136.41 USD | 0.00 USD | `+38.78%` | `1.75` |
| `Live` | `Short` | `80.75` | 860,630.00 USD | 646.00 USD | 0.00 USD | `+43.77%` | `8.00` |
| `Live` | `Short` | `81.05` | 879,630.00 USD | 19,000.00 USD | 0.00 USD | `+44.30%` | `234.42` |
| `Live` | `Short` | `81.55` | 879,750.00 USD | 123.96 USD | 0.00 USD | `+45.19%` | `1.52` |
| `Live` | `Short` | `82.45` | 883,050.00 USD | 3,300.00 USD | 0.00 USD | `+46.80%` | `40.00` |
| `Live` | `Short` | `82.75` | 883,260.00 USD | 214.32 USD | 0.00 USD | `+47.33%` | `2.59` |
| `Live` | `Short` | `84.35` | 886,050.00 USD | 2,780.00 USD | 0.00 USD | `+50.18%` | `33.00` |
| `Live` | `Short` | `85.75` | 886,830.00 USD | 777.75 USD | 0.00 USD | `+52.67%` | `9.07` |
| `Live` | `Short` | `87.45` | 910,160.00 USD | 23,330.00 USD | 0.00 USD | `+55.70%` | `266.81` |
| `Live` | `Short` | `88.45` | 910,280.00 USD | 116.75 USD | 0.00 USD | `+57.48%` | `1.32` |
| `Live` | `Short` | `89.55` | 911,230.00 USD | 951.92 USD | 0.00 USD | `+59.44%` | `10.63` |
| `Live` | `Short` | `90.35` | 911,330.00 USD | 101.19 USD | 0.00 USD | `+60.86%` | `1.12` |
| `Live` | `Short` | `91.95` | 911,480.00 USD | 155.40 USD | 0.00 USD | `+63.71%` | `1.69` |
| `Live` | `Short` | `97.85` | 913,930.00 USD | 2,450.00 USD | 0.00 USD | `+74.21%` | `25.00` |
| `Live` | `Short` | `103.35` | 944,930.00 USD | 31,010.00 USD | 0.00 USD | `+84.01%` | `300.00` |
| `Live` | `Short` | `104.25` | 945,150.00 USD | 213.71 USD | 0.00 USD | `+85.61%` | `2.05` |
| `Live` | `Short` | `104.85` | 947,470.00 USD | 2,320.00 USD | 0.00 USD | `+86.68%` | `22.13` |
| `Live` | `Short` | `105.55` | 1,300,000.00 USD | 356,130.00 USD | 0.00 USD | `+87.92%` | `3,374.01` |
| `Live` | `Short` | `106.75` | 1,310,000.00 USD | 1,620.00 USD | 0.00 USD | `+90.06%` | `15.16` |
| `Live` | `Short` | `106.85` | 1,310,000.00 USD | 1,860.00 USD | 0.00 USD | `+90.24%` | `17.43` |
| `Live` | `Short` | `107.15` | 1,310,000.00 USD | 199.30 USD | 0.00 USD | `+90.77%` | `1.86` |
| `Live` | `Short` | `108.05` | 1,310,000.00 USD | 6,470.00 USD | 0.00 USD | `+92.37%` | `59.91` |
| `Live` | `Short` | `110.95` | 1,310,000.00 USD | 664.59 USD | 0.00 USD | `+97.54%` | `5.99` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 812,820.00 USD | 0.00 USD | 392.18 USD | `-64.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 812,420.00 USD | 0.00 USD | 2,310.00 USD | `-60.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 810,120.00 USD | 0.00 USD | 806.86 USD | `-55.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 809,310.00 USD | 0.00 USD | 1,560.00 USD | `-54.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 807,750.00 USD | 0.00 USD | 410.25 USD | `-51.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 807,340.00 USD | 0.00 USD | 281.57 USD | `-46.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 807,060.00 USD | 0.00 USD | 36,050.00 USD | `-35.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 771,010.00 USD | 0.00 USD | 37,550.00 USD | `-33.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 733,460.00 USD | 0.00 USD | 447.01 USD | `-32.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.35` | 733,010.00 USD | 0.00 USD | 73,350.00 USD | `-31.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 659,660.00 USD | 0.00 USD | 40,560.00 USD | `-30.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 619,110.00 USD | 0.00 USD | 489.57 USD | `-29.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 618,620.00 USD | 0.00 USD | 1,180.00 USD | `-28.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 617,440.00 USD | 0.00 USD | 9,840.00 USD | `-28.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 607,600.00 USD | 0.00 USD | 2,060.00 USD | `-27.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.05` | 605,550.00 USD | 0.00 USD | 2,060.00 USD | `-26.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 603,480.00 USD | 0.00 USD | 2,960.00 USD | `-26.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 600,530.00 USD | 0.00 USD | 4,010.00 USD | `-25.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.65` | 596,510.00 USD | 0.00 USD | 3,000.00 USD | `-24.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 593,510.00 USD | 0.00 USD | 5,680.00 USD | `-23.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 587,830.00 USD | 0.00 USD | 672.22 USD | `-21.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.35` | 587,160.00 USD | 0.00 USD | 329,970.00 USD | `-21.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 257,190.00 USD | 0.00 USD | 213.80 USD | `-20.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 256,980.00 USD | 0.00 USD | 223.20 USD | `-20.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 256,760.00 USD | 0.00 USD | 391.13 USD | `-20.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 256,370.00 USD | 0.00 USD | 7,080.00 USD | `-19.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 249,290.00 USD | 0.00 USD | 1,370.00 USD | `-18.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 247,920.00 USD | 0.00 USD | 553.80 USD | `-17.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.35` | 247,370.00 USD | 0.00 USD | 2,970.00 USD | `-17.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.45` | 244,400.00 USD | 0.00 USD | 3,080.00 USD | `-17.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 241,320.00 USD | 0.00 USD | 14,000.00 USD | `-16.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 227,320.00 USD | 0.00 USD | 158.56 USD | `-16.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 227,170.00 USD | 0.00 USD | 373.28 USD | `-15.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 226,790.00 USD | 0.00 USD | 849.46 USD | `-15.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 225,940.00 USD | 0.00 USD | 1,150.00 USD | `-14.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 224,790.00 USD | 0.00 USD | 129.25 USD | `-14.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.15` | 224,660.00 USD | 0.00 USD | 303.35 USD | `-14.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 224,360.00 USD | 0.00 USD | 1,740.00 USD | `-13.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 222,620.00 USD | 0.00 USD | 981.00 USD | `-12.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.35` | 221,640.00 USD | 0.00 USD | 817.24 USD | `-12.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 220,820.00 USD | 0.00 USD | 237.85 USD | `-11.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.55` | 220,580.00 USD | 0.00 USD | 1,420.00 USD | `-11.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.85` | 219,170.00 USD | 0.00 USD | 108.17 USD | `-11.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 219,060.00 USD | 0.00 USD | 298.20 USD | `-11.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 218,760.00 USD | 0.00 USD | 34,670.00 USD | `-10.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 184,090.00 USD | 0.00 USD | 6,410.00 USD | `-10.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 177,670.00 USD | 0.00 USD | 459.70 USD | `-10.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 177,210.00 USD | 0.00 USD | 236.57 USD | `-10.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 176,980.00 USD | 0.00 USD | 1,020.00 USD | `-9.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 175,960.00 USD | 0.00 USD | 439.89 USD | `-8.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.45` | 175,520.00 USD | 0.00 USD | 204.26 USD | `-8.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 175,310.00 USD | 0.00 USD | 10,190.00 USD | `-8.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.85` | 165,120.00 USD | 0.00 USD | 106.29 USD | `-7.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.95` | 165,020.00 USD | 0.00 USD | 8,700.00 USD | `-7.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 156,320.00 USD | 0.00 USD | 26,490.00 USD | `-7.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.25` | 129,830.00 USD | 0.00 USD | 140.03 USD | `-6.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 129,690.00 USD | 0.00 USD | 70,190.00 USD | `-6.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 59,490.00 USD | 0.00 USD | 5,460.00 USD | `-6.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 54,040.00 USD | 0.00 USD | 271.13 USD | `-6.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.85` | 53,770.00 USD | 0.00 USD | 2,840.00 USD | `-5.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 50,920.00 USD | 0.00 USD | 115.43 USD | `-5.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 50,810.00 USD | 0.00 USD | 9,240.00 USD | `-5.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 41,570.00 USD | 0.00 USD | 2,660.00 USD | `-5.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.25` | 38,910.00 USD | 0.00 USD | 881.82 USD | `-5.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 38,030.00 USD | 0.00 USD | 566.57 USD | `-4.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 37,460.00 USD | 0.00 USD | 5,950.00 USD | `-4.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 31,510.00 USD | 0.00 USD | 1,370.00 USD | `-4.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.75` | 30,140.00 USD | 0.00 USD | 1,120.00 USD | `-4.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 29,020.00 USD | 0.00 USD | 462.03 USD | `-4.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 28,560.00 USD | 0.00 USD | 895.07 USD | `-3.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.15` | 27,660.00 USD | 0.00 USD | 398.54 USD | `-3.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 27,260.00 USD | 0.00 USD | 3,090.00 USD | `-3.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 24,170.00 USD | 0.00 USD | 156.53 USD | `-3.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.45` | 24,020.00 USD | 0.00 USD | 144.29 USD | `-3.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.55` | 23,870.00 USD | 0.00 USD | 1,690.00 USD | `-2.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.65` | 22,180.00 USD | 0.00 USD | 14,570.00 USD | `-2.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.75` | 7,610.00 USD | 0.00 USD | 198.74 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 7,420.00 USD | 0.00 USD | 398.21 USD | `-2.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.95` | 7,020.00 USD | 0.00 USD | 397.84 USD | `-2.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 6,620.00 USD | 0.00 USD | 160.75 USD | `-1.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.15` | 6,460.00 USD | 0.00 USD | 101.48 USD | `-1.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.25` | 6,360.00 USD | 0.00 USD | 398.90 USD | `-1.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.35` | 5,960.00 USD | 0.00 USD | 407.38 USD | `-1.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.45` | 5,550.00 USD | 0.00 USD | 408.11 USD | `-1.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.55` | 5,140.00 USD | 0.00 USD | 156.65 USD | `-1.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.65` | 4,990.00 USD | 0.00 USD | 3,610.00 USD | `-0.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.75` | 1,370.00 USD | 0.00 USD | 202.37 USD | `-0.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.85` | 1,170.00 USD | 0.00 USD | 149.68 USD | `-0.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.95` | 1,020.00 USD | 0.00 USD | 193.03 USD | `-0.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 829.89 USD | 0.00 USD | 632.24 USD | `-0.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 197.65 USD | 0.00 USD | 197.65 USD | `-0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.25` | 204.19 USD | 204.19 USD | 0.00 USD | `+0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.35` | 591.31 USD | 387.12 USD | 0.00 USD | `+0.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.45` | 998.88 USD | 407.57 USD | 0.00 USD | `+0.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.55` | 3,640.00 USD | 2,640.00 USD | 0.00 USD | `+0.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.65` | 3,760.00 USD | 121.23 USD | 0.00 USD | `+0.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.75` | 3,860.00 USD | 104.42 USD | 0.00 USD | `+1.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.85` | 21,890.00 USD | 18,030.00 USD | 0.00 USD | `+1.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.95` | 22,280.00 USD | 390.68 USD | 0.00 USD | `+1.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.15` | 22,670.00 USD | 392.05 USD | 0.00 USD | `+1.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.25` | 22,880.00 USD | 201.52 USD | 0.00 USD | `+1.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.35` | 23,080.00 USD | 207.03 USD | 0.00 USD | `+2.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.45` | 23,430.00 USD | 344.70 USD | 0.00 USD | `+2.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.55` | 43,790.00 USD | 20,360.00 USD | 0.00 USD | `+2.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.65` | 43,900.00 USD | 118.18 USD | 0.00 USD | `+2.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.75` | 44,020.00 USD | 119.54 USD | 0.00 USD | `+2.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 44,770.00 USD | 747.68 USD | 0.00 USD | `+3.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 44,970.00 USD | 200.04 USD | 0.00 USD | `+3.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 45,170.00 USD | 200.96 USD | 0.00 USD | `+3.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 45,300.00 USD | 123.70 USD | 0.00 USD | `+3.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 45,900.00 USD | 601.45 USD | 0.00 USD | `+4.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 46,510.00 USD | 611.85 USD | 0.00 USD | `+4.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.65` | 46,780.00 USD | 274.48 USD | 0.00 USD | `+4.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 47,270.00 USD | 491.15 USD | 0.00 USD | `+4.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 50,220.00 USD | 2,940.00 USD | 0.00 USD | `+4.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 50,350.00 USD | 129.69 USD | 0.00 USD | `+4.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 55,150.00 USD | 4,800.00 USD | 0.00 USD | `+5.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 56,430.00 USD | 1,280.00 USD | 0.00 USD | `+5.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.25` | 56,640.00 USD | 210.34 USD | 0.00 USD | `+5.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 57,100.00 USD | 461.74 USD | 0.00 USD | `+5.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 57,260.00 USD | 159.92 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.55` | 57,750.00 USD | 496.65 USD | 0.00 USD | `+6.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 58,480.00 USD | 724.75 USD | 0.00 USD | `+6.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 58,640.00 USD | 158.00 USD | 0.00 USD | `+6.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 58,810.00 USD | 171.14 USD | 0.00 USD | `+6.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 59,360.00 USD | 551.00 USD | 0.00 USD | `+7.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.45` | 59,510.00 USD | 155.36 USD | 0.00 USD | `+7.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 60,390.00 USD | 878.58 USD | 0.00 USD | `+7.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 61,780.00 USD | 1,390.00 USD | 0.00 USD | `+7.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 62,770.00 USD | 986.99 USD | 0.00 USD | `+8.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 63,440.00 USD | 674.72 USD | 0.00 USD | `+8.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 65,800.00 USD | 2,360.00 USD | 0.00 USD | `+8.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 65,930.00 USD | 125.56 USD | 0.00 USD | `+9.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 69,530.00 USD | 3,600.00 USD | 0.00 USD | `+9.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 70,170.00 USD | 643.20 USD | 0.00 USD | `+9.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 70,300.00 USD | 130.31 USD | 0.00 USD | `+10.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 71,020.00 USD | 716.72 USD | 0.00 USD | `+11.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 71,250.00 USD | 231.39 USD | 0.00 USD | `+12.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 71,880.00 USD | 630.87 USD | 0.00 USD | `+12.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 72,580.00 USD | 703.97 USD | 0.00 USD | `+12.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 73,250.00 USD | 668.13 USD | 0.00 USD | `+12.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 81,980.00 USD | 8,730.00 USD | 0.00 USD | `+13.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 82,540.00 USD | 555.03 USD | 0.00 USD | `+13.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 83,070.00 USD | 531.62 USD | 0.00 USD | `+14.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.35` | 83,730.00 USD | 664.09 USD | 0.00 USD | `+14.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.45` | 84,400.00 USD | 665.12 USD | 0.00 USD | `+14.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 84,600.00 USD | 202.69 USD | 0.00 USD | `+14.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 84,900.00 USD | 298.04 USD | 0.00 USD | `+15.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 85,000.00 USD | 102.13 USD | 0.00 USD | `+15.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 85,540.00 USD | 540.09 USD | 0.00 USD | `+15.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 85,640.00 USD | 100.79 USD | 0.00 USD | `+16.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 85,900.00 USD | 262.20 USD | 0.00 USD | `+16.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 86,270.00 USD | 371.49 USD | 0.00 USD | `+17.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 86,970.00 USD | 696.17 USD | 0.00 USD | `+17.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 87,500.00 USD | 534.00 USD | 0.00 USD | `+18.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 98,580.00 USD | 11,080.00 USD | 0.00 USD | `+19.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 105,290.00 USD | 6,710.00 USD | 0.00 USD | `+19.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.05` | 107,650.00 USD | 2,360.00 USD | 0.00 USD | `+21.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 112,510.00 USD | 4,860.00 USD | 0.00 USD | `+21.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 112,720.00 USD | 204.48 USD | 0.00 USD | `+23.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.65` | 630,920.00 USD | 518,200.00 USD | 0.00 USD | `+24.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 631,730.00 USD | 810.02 USD | 0.00 USD | `+24.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 951,620.00 USD | 319,890.00 USD | 0.00 USD | `+24.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 951,790.00 USD | 170.04 USD | 0.00 USD | `+26.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 957,560.00 USD | 5,770.00 USD | 0.00 USD | `+26.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 957,830.00 USD | 269.28 USD | 0.00 USD | `+26.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 958,120.00 USD | 291.40 USD | 0.00 USD | `+28.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 965,330.00 USD | 7,220.00 USD | 0.00 USD | `+28.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 965,490.00 USD | 156.78 USD | 0.00 USD | `+28.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 968,710.00 USD | 3,220.00 USD | 0.00 USD | `+29.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 969,120.00 USD | 411.14 USD | 0.00 USD | `+30.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 1,090,000.00 USD | 123,190.00 USD | 0.00 USD | `+31.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 1,090,000.00 USD | 1,020.00 USD | 0.00 USD | `+32.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.75` | 1,090,000.00 USD | 811.04 USD | 0.00 USD | `+33.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 1,090,000.00 USD | 104.93 USD | 0.00 USD | `+33.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 1,090,000.00 USD | 133.59 USD | 0.00 USD | `+33.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 1,090,000.00 USD | 402.59 USD | 0.00 USD | `+33.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.85` | 1,100,000.00 USD | 308.71 USD | 0.00 USD | `+35.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 1,100,000.00 USD | 315.18 USD | 0.00 USD | `+37.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 1,150,000.00 USD | 59,310.00 USD | 0.00 USD | `+40.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 1,160,000.00 USD | 3,160.00 USD | 0.00 USD | `+40.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.35` | 1,160,000.00 USD | 5,260.00 USD | 0.00 USD | `+41.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 1,170,000.00 USD | 5,690.00 USD | 0.00 USD | `+41.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 1,210,000.00 USD | 36,590.00 USD | 0.00 USD | `+42.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 1,210,000.00 USD | 433.89 USD | 0.00 USD | `+44.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 1,210,000.00 USD | 172.64 USD | 0.00 USD | `+44.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 1,210,000.00 USD | 164.10 USD | 0.00 USD | `+46.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 1,210,000.00 USD | 546.81 USD | 0.00 USD | `+47.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 1,210,000.00 USD | 2,300.00 USD | 0.00 USD | `+49.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 1,220,000.00 USD | 12,070.00 USD | 0.00 USD | `+51.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.05` | 1,240,000.00 USD | 20,230.00 USD | 0.00 USD | `+54.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 1,240,000.00 USD | 1,580.00 USD | 0.00 USD | `+56.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 1,280,000.00 USD | 37,000.00 USD | 0.00 USD | `+56.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 1,280,000.00 USD | 473.21 USD | 0.00 USD | `+58.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 1,280,000.00 USD | 422.99 USD | 0.00 USD | `+58.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 1,280,000.00 USD | 1,630.00 USD | 0.00 USD | `+59.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 1,290,000.00 USD | 4,870.00 USD | 0.00 USD | `+60.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 1,290,000.00 USD | 481.55 USD | 0.00 USD | `+63.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 1,290,000.00 USD | 1,330.00 USD | 0.00 USD | `+63.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 1,290,000.00 USD | 188.10 USD | 0.00 USD | `+67.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,560,000.00 USD | 266,140.00 USD | 0.00 USD | `+69.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,560,000.00 USD | 3,400.00 USD | 0.00 USD | `+69.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,580,000.00 USD | 21,930.00 USD | 0.00 USD | `+71.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,580,000.00 USD | 294.15 USD | 0.00 USD | `+74.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 1,600,000.00 USD | 15,380.00 USD | 0.00 USD | `+76.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,600,000.00 USD | 3,660.00 USD | 0.00 USD | `+78.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,600,000.00 USD | 306.15 USD | 0.00 USD | `+81.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,600,000.00 USD | 936.72 USD | 0.00 USD | `+83.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,600,000.00 USD | 2,920.00 USD | 0.00 USD | `+83.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,600,000.00 USD | 324.15 USD | 0.00 USD | `+92.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 1,600,000.00 USD | 123.23 USD | 0.00 USD | `+94.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 1,690,000.00 USD | 89,110.00 USD | 0.00 USD | `+97.72%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `47.10` | 9,130,000.00 USD | 0.00 USD | 9,130,000.00 USD | 17,230.00 USD | 12,890.00 USD | 6,630.00 USD |
| `7D` | `47.20` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 8,940.00 USD | 1,090.00 USD | 114.09 USD |
| `7D` | `47.30` | 9,080,000.00 USD | 0.00 USD | 9,080,000.00 USD | 692.33 USD | 4,740.00 USD | 6,740.00 USD |
| `7D` | `47.40` | 9,070,000.00 USD | 0.00 USD | 9,070,000.00 USD | 0.00 USD | 1,520.00 USD | 28,650.00 USD |
| `7D` | `47.50` | 9,040,000.00 USD | 0.00 USD | 9,040,000.00 USD | 11,830.00 USD | 0.00 USD | 7,960.00 USD |
| `7D` | `48.10` | 9,020,000.00 USD | 0.00 USD | 9,020,000.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD |
| `7D` | `48.20` | 9,020,000.00 USD | 0.00 USD | 9,020,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD |
| `7D` | `48.40` | 9,010,000.00 USD | 0.00 USD | 9,010,000.00 USD | 0.00 USD | 6,080.00 USD | 0.00 USD |
| `7D` | `48.60` | 9,000,000.00 USD | 0.00 USD | 9,000,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `48.80` | 9,000,000.00 USD | 0.00 USD | 9,000,000.00 USD | 1,780.00 USD | 2,250.00 USD | 0.00 USD |
| `7D` | `48.90` | 9,000,000.00 USD | 0.00 USD | 9,000,000.00 USD | 0.00 USD | 0.00 USD | 960.40 USD |
| `7D` | `49.30` | 9,000,000.00 USD | 0.00 USD | 9,000,000.00 USD | 15,190.00 USD | 4,490.00 USD | 14,870.00 USD |
| `7D` | `49.40` | 8,960,000.00 USD | 0.00 USD | 8,960,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD |
| `7D` | `49.50` | 8,950,000.00 USD | 0.00 USD | 8,950,000.00 USD | 2,830.00 USD | 7,770.00 USD | 0.00 USD |
| `7D` | `49.60` | 8,940,000.00 USD | 0.00 USD | 8,940,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD |
| `7D` | `49.70` | 8,930,000.00 USD | 0.00 USD | 8,930,000.00 USD | 12,090.00 USD | 0.00 USD | 5,410.00 USD |
| `7D` | `49.80` | 8,910,000.00 USD | 0.00 USD | 8,910,000.00 USD | 9,930.00 USD | 8,220.00 USD | 0.00 USD |
| `7D` | `49.90` | 8,890,000.00 USD | 0.00 USD | 8,890,000.00 USD | 45,030.00 USD | 7,170.00 USD | 4,700.00 USD |
| `7D` | `50.00` | 8,840,000.00 USD | 0.00 USD | 8,840,000.00 USD | 22,100.00 USD | 7,630.00 USD | 24,920.00 USD |
| `7D` | `50.10` | 8,780,000.00 USD | 0.00 USD | 8,780,000.00 USD | 363.50 USD | 682.90 USD | 8,340.00 USD |
| `1D` | `50.20` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 4,490.00 USD | 5,820.00 USD | 3,500.00 USD |
| `7D` | `50.20` | 8,770,000.00 USD | 0.00 USD | 8,770,000.00 USD | 6,960.00 USD | 500.40 USD | 34,680.00 USD |
| `1D` | `50.30` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 171.03 USD | 333.03 USD | 2,340.00 USD |
| `7D` | `50.30` | 8,730,000.00 USD | 0.00 USD | 8,730,000.00 USD | 16,270.00 USD | 3,640.00 USD | 1,950.00 USD |
| `1D` | `50.40` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 4,370.00 USD | 2,740.00 USD | 0.00 USD |
| `7D` | `50.40` | 8,710,000.00 USD | 0.00 USD | 8,710,000.00 USD | 28,280.00 USD | 19,110.00 USD | 33,450.00 USD |
| `1D` | `50.50` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 5,790.00 USD | 2,110.00 USD | 1,740.00 USD |
| `7D` | `50.50` | 8,630,000.00 USD | 0.00 USD | 8,630,000.00 USD | 24,840.00 USD | 6,790.00 USD | 44,160.00 USD |
| `1D` | `50.60` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 1,660.00 USD | 2,640.00 USD | 9,380.00 USD |
| `7D` | `50.60` | 8,550,000.00 USD | 0.00 USD | 8,550,000.00 USD | 56,670.00 USD | 21,530.00 USD | 22,250.00 USD |
| `1D` | `50.70` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 4,820.00 USD | 1,440.00 USD | 11,700.00 USD |
| `7D` | `50.70` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 65,150.00 USD | 32,820.00 USD | 41,580.00 USD |
| `1D` | `50.80` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 12,550.00 USD | 3,100.00 USD | 8,280.00 USD |
| `7D` | `50.80` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD |
| `1D` | `50.90` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 826.24 USD | 260.05 USD | 8,390.00 USD |
| `7D` | `50.90` | 8,210,000.00 USD | 0.00 USD | 8,210,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD |
| `1D` | `51.00` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 5,040.00 USD | 0.00 USD | 430.77 USD |
| `7D` | `51.00` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `51.10` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 9,210.00 USD | 6,560.00 USD | 0.00 USD |
| `7D` | `51.10` | 7,840,000.00 USD | 0.00 USD | 7,840,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD |
| `1D` | `51.20` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 2,360.00 USD | 1,130.00 USD | 17,310.00 USD |
| `7D` | `51.20` | 7,750,000.00 USD | 0.00 USD | 7,750,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD |
| `1D` | `51.30` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 16,790.00 USD | 14,100.00 USD | 10,670.00 USD |
| `7D` | `51.30` | 7,690,000.00 USD | 0.00 USD | 7,690,000.00 USD | 28,400.00 USD | 26,720.00 USD | 47,090.00 USD |
| `1D` | `51.40` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 13,750.00 USD | 11,490.00 USD | 4,890.00 USD |
| `7D` | `51.40` | 7,590,000.00 USD | 0.00 USD | 7,590,000.00 USD | 73,130.00 USD | 42,820.00 USD | 46,140.00 USD |
| `1D` | `51.50` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 7,880.00 USD | 10,980.00 USD | 37,710.00 USD |
| `7D` | `51.50` | 7,430,000.00 USD | 0.00 USD | 7,430,000.00 USD | 38,520.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `51.60` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 9,060.00 USD | 18,490.00 USD | 757.87 USD |
| `7D` | `51.60` | 7,330,000.00 USD | 0.00 USD | 7,330,000.00 USD | 37,880.00 USD | 36,790.00 USD | 41,490.00 USD |
| `1D` | `51.70` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 2,890.00 USD | 13,810.00 USD | 21,320.00 USD |
| `7D` | `51.70` | 7,210,000.00 USD | 0.00 USD | 7,210,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `51.80` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 12,590.00 USD | 19,270.00 USD | 14,170.00 USD |
| `7D` | `51.80` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD |
| `1D` | `51.90` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 9,460.00 USD | 24,890.00 USD | 23,480.00 USD |
| `7D` | `51.90` | 7,120,000.00 USD | 0.00 USD | 7,120,000.00 USD | 5,870.00 USD | 25,410.00 USD | 28,190.00 USD |
| `1D` | `52.00` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 20,980.00 USD | 25,480.00 USD | 25,740.00 USD |
| `7D` | `52.00` | 7,060,000.00 USD | 0.00 USD | 7,060,000.00 USD | 64,300.00 USD | 26,440.00 USD | 11,880.00 USD |
| `1D` | `52.10` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 34,880.00 USD | 17,130.00 USD | 50,300.00 USD |
| `7D` | `52.10` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 24,220.00 USD | 28,090.00 USD | 37,880.00 USD |
| `1D` | `52.20` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 15,020.00 USD | 7,630.00 USD | 46,100.00 USD |
| `7D` | `52.20` | 6,870,000.00 USD | 0.00 USD | 6,870,000.00 USD | 38,380.00 USD | 13,960.00 USD | 25,270.00 USD |
| `1D` | `52.30` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 26,510.00 USD | 21,640.00 USD | 11,210.00 USD |
| `7D` | `52.30` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 24,840.00 USD | 41,300.00 USD | 8,940.00 USD |
| `1D` | `52.40` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 12,460.00 USD | 15,120.00 USD | 7,040.00 USD |
| `7D` | `52.40` | 6,710,000.00 USD | 0.00 USD | 6,710,000.00 USD | 20,580.00 USD | 38,950.00 USD | 22,030.00 USD |
| `1D` | `52.50` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 53,350.00 USD | 29,580.00 USD | 74,280.00 USD |
| `7D` | `52.50` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 38,720.00 USD | 667.05 USD | 11,240.00 USD |
| `1D` | `52.60` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 8,330.00 USD | 40,700.00 USD | 717.10 USD |
| `7D` | `52.60` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 74,610.00 USD | 32,590.00 USD | 59,410.00 USD |
| `1D` | `52.70` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 16,690.00 USD | 19,440.00 USD | 28,640.00 USD |
| `7D` | `52.70` | 6,410,000.00 USD | 0.00 USD | 6,410,000.00 USD | 20,250.00 USD | 92,920.00 USD | 108,640.00 USD |
| `1D` | `52.80` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 27,090.00 USD | 50,290.00 USD | 102,590.00 USD |
| `7D` | `52.80` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 39,200.00 USD | 35,280.00 USD | 0.00 USD |
| `1D` | `52.90` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 43,760.00 USD | 50,040.00 USD | 26,190.00 USD |
| `7D` | `52.90` | 6,120,000.00 USD | 0.00 USD | 6,120,000.00 USD | 44,800.00 USD | 28,710.00 USD | 34,400.00 USD |
| `1D` | `53.00` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 26,670.00 USD | 30,500.00 USD | 39,600.00 USD |
| `7D` | `53.00` | 6,010,000.00 USD | 0.00 USD | 6,010,000.00 USD | 39,690.00 USD | 25,810.00 USD | 81,210.00 USD |
| `1D` | `53.10` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 14,570.00 USD | 42,760.00 USD | 87,010.00 USD |
| `7D` | `53.10` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 45,320.00 USD | 17,950.00 USD | 0.00 USD |
| `1D` | `53.20` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 24,240.00 USD | 6,510.00 USD | 41,660.00 USD |
| `7D` | `53.20` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 162,460.00 USD | 28,320.00 USD | 23,350.00 USD |
| `1D` | `53.30` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 4,060.00 USD | 0.00 USD | 5,610.00 USD |
| `7D` | `53.30` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 57,250.00 USD | 24,540.00 USD | 34,820.00 USD |
| `1D` | `53.40` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 3,460.00 USD | 1,850.00 USD | 657.14 USD |
| `7D` | `53.40` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 44,030.00 USD | 7,250.00 USD | 91,220.00 USD |
| `1D` | `53.50` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 9,110.00 USD | 3,940.00 USD | 2,990.00 USD |
| `7D` | `53.50` | 5,330,000.00 USD | 0.00 USD | 5,330,000.00 USD | 48,660.00 USD | 3,440.00 USD | 20,840.00 USD |
| `1D` | `53.60` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 72,650.00 USD | 220.65 USD | 13,180.00 USD |
| `7D` | `53.60` | 5,250,000.00 USD | 0.00 USD | 5,250,000.00 USD | 52,800.00 USD | 1,980.00 USD | 0.00 USD |
| `1D` | `53.70` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 6,210.00 USD | 0.00 USD | 5,890.00 USD |
| `7D` | `53.70` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 131,400.00 USD | 3,480.00 USD | 0.00 USD |
| `1D` | `53.80` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 44,920.00 USD | 2,830.00 USD | 168.97 USD |
| `7D` | `53.80` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 99,150.00 USD | 13,850.00 USD | 0.00 USD |
| `1D` | `53.90` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 40,670.00 USD | 18,200.00 USD | 4,620.00 USD |
| `7D` | `53.90` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 129,920.00 USD | 21,360.00 USD | 1,130.00 USD |
| `1D` | `54.00` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 45,350.00 USD | 15,370.00 USD | 68,320.00 USD |
| `7D` | `54.00` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 353,050.00 USD | 71,820.00 USD | 272,490.00 USD |
| `1D` | `54.10` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 91,490.00 USD | 19,160.00 USD | 45,460.00 USD |
| `7D` | `54.10` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 302,190.00 USD | 0.00 USD | 2,590.00 USD |
| `1D` | `54.20` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 72,600.00 USD | 15,510.00 USD | 40,120.00 USD |
| `7D` | `54.20` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 205,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `54.30` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 15,600.00 USD | 0.00 USD | 5,350.00 USD |
| `7D` | `54.30` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 381,380.00 USD | 0.00 USD | 181,420.00 USD |
| `1D` | `54.40` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 51,570.00 USD | 35,500.00 USD | 3,130.00 USD |
| `7D` | `54.40` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 304,270.00 USD | 13,830.00 USD | 92,140.00 USD |
| `1D` | `54.50` | 948,180.00 USD | 0.00 USD | 948,180.00 USD | 9,670.00 USD | 46,240.00 USD | 1,310.00 USD |
| `7D` | `54.50` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 159,720.00 USD | 15,240.00 USD | 239,890.00 USD |
| `1D` | `54.60` | 890,960.00 USD | 0.00 USD | 890,960.00 USD | 913.17 USD | 21,680.00 USD | 5,570.00 USD |
| `7D` | `54.60` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 0.00 USD | 1,930.00 USD | 116,060.00 USD |
| `1D` | `54.70` | 862,800.00 USD | 0.00 USD | 862,800.00 USD | 0.00 USD | 15,420.00 USD | 82,460.00 USD |
| `1D` | `54.80` | 764,920.00 USD | 0.00 USD | 764,920.00 USD | 0.00 USD | 25,800.00 USD | 11,770.00 USD |
| `1D` | `54.90` | 727,350.00 USD | 0.00 USD | 727,350.00 USD | 49,450.00 USD | 13,090.00 USD | 1,530.00 USD |
| `7D` | `54.90` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 0.00 USD | 52,180.00 USD | 47,680.00 USD |
| `1D` | `55.00` | 663,280.00 USD | 0.00 USD | 663,280.00 USD | 19,950.00 USD | 11,440.00 USD | 38,450.00 USD |
| `7D` | `55.00` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 35,900.00 USD | 0.00 USD | 2,260.00 USD |
| `1D` | `55.10` | 593,450.00 USD | 0.00 USD | 593,450.00 USD | 3,850.00 USD | 53,510.00 USD | 51,570.00 USD |
| `7D` | `55.10` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 0.00 USD | 18,510.00 USD | 602.10 USD |
| `1D` | `55.20` | 484,520.00 USD | 0.00 USD | 484,520.00 USD | 24,740.00 USD | 7,520.00 USD | 58,520.00 USD |
| `7D` | `55.20` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 57,400.00 USD | 59,710.00 USD | 150,160.00 USD |
| `1D` | `55.30` | 393,730.00 USD | 0.00 USD | 393,730.00 USD | 39,800.00 USD | 22,650.00 USD | 51,760.00 USD |
| `7D` | `55.30` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 23,140.00 USD | 11,270.00 USD | 0.00 USD |
| `1D` | `55.40` | 279,520.00 USD | 0.00 USD | 279,520.00 USD | 0.00 USD | 6,510.00 USD | 742.75 USD |
| `7D` | `55.40` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 0.00 USD | 18,550.00 USD | 4,800.00 USD |
| `1D` | `55.50` | 272,270.00 USD | 0.00 USD | 272,270.00 USD | 0.00 USD | 9,250.00 USD | 5,500.00 USD |
| `7D` | `55.50` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 0.00 USD | 33,460.00 USD | 0.00 USD |
| `7D` | `55.60` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 426,340.00 USD | 13,860.00 USD | 0.00 USD |
| `1D` | `55.70` | 257,510.00 USD | 0.00 USD | 257,510.00 USD | 0.00 USD | 7,490.00 USD | 613.46 USD |
| `7D` | `55.70` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD |
| `1D` | `55.80` | 249,410.00 USD | 0.00 USD | 249,410.00 USD | 6,170.00 USD | 26,160.00 USD | 3,340.00 USD |
| `7D` | `55.80` | 922,810.00 USD | 0.00 USD | 922,810.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD |
| `1D` | `55.90` | 213,740.00 USD | 0.00 USD | 213,740.00 USD | 103,700.00 USD | 13,230.00 USD | 89,130.00 USD |
| `7D` | `55.90` | 831,840.00 USD | 0.00 USD | 831,840.00 USD | 141,330.00 USD | 101,960.00 USD | 117,660.00 USD |
| `1D` | `56.00` | 7,690.00 USD | 0.00 USD | 7,690.00 USD | 0.00 USD | 3,180.00 USD | 4,510.00 USD |
| `7D` | `56.00` | 470,900.00 USD | 0.00 USD | 470,900.00 USD | 181,230.00 USD | 118,560.00 USD | 171,110.00 USD |
| `1D` | `56.10` | 74,130.00 USD | 74,130.00 USD | 0.00 USD | 68,240.00 USD | 5,890.00 USD | 0.00 USD |
| `1D` | `56.10` | 148,270.00 USD | 148,270.00 USD | 0.00 USD | 68,240.00 USD | 5,890.00 USD | 0.00 USD |
| `7D` | `56.10` | 338,000.00 USD | 338,000.00 USD | 0.00 USD | 121,920.00 USD | 154,860.00 USD | 61,210.00 USD |
| `7D` | `56.10` | 675,990.00 USD | 675,990.00 USD | 0.00 USD | 121,920.00 USD | 154,860.00 USD | 61,210.00 USD |
| `7D` | `56.20` | 996,680.00 USD | 996,680.00 USD | 0.00 USD | 0.00 USD | 79,940.00 USD | 240,740.00 USD |
| `1D` | `56.30` | 196,590.00 USD | 196,590.00 USD | 0.00 USD | 0.00 USD | 44,360.00 USD | 3,950.00 USD |
| `7D` | `56.30` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 1,270.00 USD | 0.00 USD | 2,590.00 USD |
| `1D` | `56.40` | 222,080.00 USD | 222,080.00 USD | 0.00 USD | 5,040.00 USD | 17,690.00 USD | 2,760.00 USD |
| `7D` | `56.40` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 2,650.00 USD | 11,040.00 USD | 0.00 USD |
| `1D` | `56.50` | 636,660.00 USD | 636,660.00 USD | 0.00 USD | 138,540.00 USD | 131,430.00 USD | 144,610.00 USD |
| `7D` | `56.50` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 170,750.00 USD | 143,420.00 USD | 6,150.00 USD |
| `1D` | `56.60` | 871,360.00 USD | 871,360.00 USD | 0.00 USD | 49,560.00 USD | 104,240.00 USD | 80,910.00 USD |
| `7D` | `56.60` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 363,190.00 USD | 136,570.00 USD | 0.00 USD |
| `1D` | `56.70` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 97,300.00 USD | 27,730.00 USD | 307,810.00 USD |
| `7D` | `56.70` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 117,290.00 USD | 121,500.00 USD | 98,950.00 USD |
| `1D` | `56.80` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 117,760.00 USD | 17,250.00 USD | 68,120.00 USD |
| `7D` | `56.80` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 153,580.00 USD | 92,780.00 USD | 303,010.00 USD |
| `1D` | `56.90` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 38,540.00 USD | 10,710.00 USD | 22,790.00 USD |
| `7D` | `56.90` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 113,780.00 USD | 48,600.00 USD | 266,610.00 USD |
| `1D` | `57.00` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 6,480.00 USD | 18,250.00 USD | 12,860.00 USD |
| `7D` | `57.00` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 88,680.00 USD | 20,690.00 USD | 151,930.00 USD |
| `1D` | `57.10` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 59,550.00 USD | 25,050.00 USD | 25,930.00 USD |
| `7D` | `57.10` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 36,580.00 USD | 19,180.00 USD | 20,440.00 USD |
| `1D` | `57.20` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 32,320.00 USD | 35,770.00 USD | 74,480.00 USD |
| `7D` | `57.20` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 57,060.00 USD | 21,090.00 USD | 5,960.00 USD |
| `1D` | `57.30` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 24,260.00 USD | 36,820.00 USD | 58,540.00 USD |
| `7D` | `57.30` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 22,360.00 USD | 28,570.00 USD | 34,850.00 USD |
| `1D` | `57.40` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 70,320.00 USD | 45,150.00 USD | 70,520.00 USD |
| `7D` | `57.40` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 124,180.00 USD | 72,180.00 USD | 257,730.00 USD |
| `1D` | `57.50` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 184,770.00 USD | 48,350.00 USD | 167,330.00 USD |
| `7D` | `57.50` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 99,810.00 USD | 31,830.00 USD | 0.00 USD |
| `1D` | `57.60` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 69,720.00 USD | 24,050.00 USD | 62,510.00 USD |
| `7D` | `57.60` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 149,560.00 USD | 40,430.00 USD | 28,320.00 USD |
| `1D` | `57.70` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 36,620.00 USD | 26,070.00 USD | 96,350.00 USD |
| `7D` | `57.70` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 5,400.00 USD | 57,330.00 USD |
| `1D` | `57.80` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 9,690.00 USD | 13,860.00 USD | 73,330.00 USD |
| `7D` | `57.80` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 9,650.00 USD | 14,360.00 USD | 49,480.00 USD |
| `1D` | `57.90` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 13,000.00 USD | 14,100.00 USD | 9,940.00 USD |
| `7D` | `57.90` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 5,120.00 USD | 963.90 USD | 22,350.00 USD |
| `1D` | `58.00` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 4,580.00 USD | 5,870.00 USD | 7,540.00 USD |
| `7D` | `58.00` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 3,670.00 USD | 86,690.00 USD |
| `1D` | `58.10` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 31,400.00 USD | 6,730.00 USD | 15,230.00 USD |
| `7D` | `58.10` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 5,470.00 USD | 1,310.00 USD | 848.40 USD |
| `1D` | `58.20` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 27,190.00 USD | 8,710.00 USD | 406.15 USD |
| `7D` | `58.20` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 1,540.00 USD | 0.00 USD |
| `1D` | `58.30` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 21,400.00 USD | 17,260.00 USD | 41,170.00 USD |
| `7D` | `58.30` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 17,950.00 USD | 9,580.00 USD | 27,950.00 USD |
| `1D` | `58.40` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 2,240.00 USD | 15,040.00 USD | 35,850.00 USD |
| `7D` | `58.40` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 9,260.00 USD | 54,420.00 USD |
| `1D` | `58.50` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 21,130.00 USD | 8,030.00 USD | 124.02 USD |
| `7D` | `58.50` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD |
| `1D` | `58.60` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 14,490.00 USD | 3,760.00 USD | 36,180.00 USD |
| `7D` | `58.60` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 30,680.00 USD | 20,260.00 USD | 51,650.00 USD |
| `1D` | `58.70` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 38,020.00 USD | 10,060.00 USD | 26,240.00 USD |
| `7D` | `58.70` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 15,810.00 USD | 11,600.00 USD | 35,320.00 USD |
| `1D` | `58.80` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 35,830.00 USD | 14,730.00 USD | 23,630.00 USD |
| `7D` | `58.80` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD |
| `1D` | `58.90` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 22,130.00 USD | 91,210.00 USD | 90,490.00 USD |
| `7D` | `58.90` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 54,240.00 USD | 83,500.00 USD |
| `1D` | `59.00` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 129,180.00 USD | 58,790.00 USD | 127,880.00 USD |
| `7D` | `59.00` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 259,280.00 USD | 65,270.00 USD | 118,570.00 USD |
| `1D` | `59.10` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 91,380.00 USD | 39,780.00 USD | 163,590.00 USD |
| `7D` | `59.10` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 91,060.00 USD | 45,400.00 USD | 158,780.00 USD |
| `1D` | `59.20` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 101,760.00 USD | 59,450.00 USD | 49,290.00 USD |
| `7D` | `59.20` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 153,580.00 USD | 18,540.00 USD | 174,600.00 USD |
| `1D` | `59.30` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 171,630.00 USD | 45,010.00 USD | 94,100.00 USD |
| `7D` | `59.30` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD |
| `1D` | `59.40` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 64,900.00 USD | 45,810.00 USD | 59,430.00 USD |
| `7D` | `59.40` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 105,490.00 USD | 73,620.00 USD | 137,500.00 USD |
| `1D` | `59.50` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 89,030.00 USD | 38,560.00 USD | 33,840.00 USD |
| `7D` | `59.50` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD |
| `1D` | `59.60` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 43,670.00 USD | 53,100.00 USD | 7,010.00 USD |
| `7D` | `59.60` | 7,520,000.00 USD | 7,520,000.00 USD | 0.00 USD | 270,460.00 USD | 147,800.00 USD | 86,840.00 USD |
| `1D` | `59.70` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 13,470.00 USD | 19,120.00 USD | 78,050.00 USD |
| `7D` | `59.70` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 55,510.00 USD | 180,620.00 USD | 162,850.00 USD |
| `1D` | `59.80` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 31,530.00 USD | 26,470.00 USD | 10,630.00 USD |
| `7D` | `59.80` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 118,240.00 USD | 97,600.00 USD | 155,270.00 USD |
| `1D` | `59.90` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 112,000.00 USD | 20,240.00 USD | 50,210.00 USD |
| `7D` | `59.90` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 209,780.00 USD | 83,540.00 USD | 39,820.00 USD |
| `1D` | `60.00` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 164,190.00 USD | 44,230.00 USD | 50,570.00 USD |
| `7D` | `60.00` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 195,800.00 USD | 152,810.00 USD | 94,160.00 USD |
| `1D` | `60.10` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 64,090.00 USD | 28,140.00 USD | 57,080.00 USD |
| `7D` | `60.10` | 9,500,000.00 USD | 9,500,000.00 USD | 0.00 USD | 217,190.00 USD | 100,570.00 USD | 113,260.00 USD |
| `1D` | `60.20` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 59,560.00 USD | 19,740.00 USD | 82,270.00 USD |
| `7D` | `60.20` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 162,230.00 USD | 99,360.00 USD | 108,990.00 USD |
| `1D` | `60.30` | 6,310,000.00 USD | 6,310,000.00 USD | 0.00 USD | 53,910.00 USD | 30,600.00 USD | 24,580.00 USD |
| `7D` | `60.30` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 133,350.00 USD | 100,380.00 USD | 170,480.00 USD |
| `1D` | `60.40` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 66,740.00 USD | 13,730.00 USD | 39,240.00 USD |
| `7D` | `60.40` | 10,650,000.00 USD | 10,650,000.00 USD | 0.00 USD | 64,850.00 USD | 108,300.00 USD | 204,780.00 USD |
| `1D` | `60.50` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 22,700.00 USD | 19,320.00 USD | 36,200.00 USD |
| `7D` | `60.50` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 115,390.00 USD | 86,870.00 USD | 175,550.00 USD |
| `1D` | `60.60` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 40,710.00 USD | 19,140.00 USD | 3,930.00 USD |
| `7D` | `60.60` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 251,100.00 USD | 18,640.00 USD | 118,680.00 USD |
| `1D` | `60.70` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 34,230.00 USD | 22,330.00 USD | 3,120.00 USD |
| `7D` | `60.70` | 11,620,000.00 USD | 11,620,000.00 USD | 0.00 USD | 119,080.00 USD | 57,480.00 USD | 22,840.00 USD |
| `1D` | `60.80` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 15,430.00 USD | 12,060.00 USD | 47,810.00 USD |
| `7D` | `60.80` | 11,810,000.00 USD | 11,810,000.00 USD | 0.00 USD | 46,960.00 USD | 69,290.00 USD | 76,200.00 USD |
| `1D` | `60.90` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 35,570.00 USD | 21,920.00 USD | 22,850.00 USD |
| `7D` | `60.90` | 12,010,000.00 USD | 12,010,000.00 USD | 0.00 USD | 105,970.00 USD | 34,400.00 USD | 65,270.00 USD |
| `1D` | `61.00` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 44,070.00 USD | 6,430.00 USD | 18,420.00 USD |
| `7D` | `61.00` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 77,670.00 USD | 36,060.00 USD | 5,220.00 USD |
| `1D` | `61.10` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 12,010.00 USD | 6,270.00 USD | 11,490.00 USD |
| `7D` | `61.10` | 12,170,000.00 USD | 12,170,000.00 USD | 0.00 USD | 31,540.00 USD | 1,560.00 USD | 0.00 USD |
| `1D` | `61.20` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 72,520.00 USD | 0.00 USD | 38,940.00 USD |
| `7D` | `61.20` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 98,820.00 USD | 60,240.00 USD | 52,930.00 USD |
| `1D` | `61.30` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 0.00 USD | 3,330.00 USD | 0.00 USD |
| `7D` | `61.30` | 12,460,000.00 USD | 12,460,000.00 USD | 0.00 USD | 27,780.00 USD | 21,000.00 USD | 33,030.00 USD |
| `1D` | `61.40` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 1,190.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `61.40` | 12,590,000.00 USD | 12,590,000.00 USD | 0.00 USD | 66,470.00 USD | 25,720.00 USD | 35,250.00 USD |
| `1D` | `61.50` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 1,060.00 USD | 333.03 USD | 2,340.00 USD |
| `7D` | `61.50` | 12,680,000.00 USD | 12,680,000.00 USD | 0.00 USD | 19,810.00 USD | 35,300.00 USD | 36,110.00 USD |
| `1D` | `61.60` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 5,360.00 USD | 2,740.00 USD | 0.00 USD |
| `7D` | `61.60` | 12,890,000.00 USD | 12,890,000.00 USD | 0.00 USD | 38,370.00 USD | 50,880.00 USD | 121,470.00 USD |
| `1D` | `61.70` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 10,770.00 USD | 2,110.00 USD | 1,740.00 USD |
| `7D` | `61.70` | 13,080,000.00 USD | 13,080,000.00 USD | 0.00 USD | 75,210.00 USD | 10,880.00 USD | 99,520.00 USD |
| `1D` | `61.80` | 7,050,000.00 USD | 7,050,000.00 USD | 0.00 USD | 3,480.00 USD | 2,640.00 USD | 9,380.00 USD |
| `7D` | `61.80` | 13,320,000.00 USD | 13,320,000.00 USD | 0.00 USD | 158,760.00 USD | 25,670.00 USD | 62,060.00 USD |
| `1D` | `61.90` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 4,800.00 USD | 1,440.00 USD | 11,700.00 USD |
| `7D` | `61.90` | 13,470,000.00 USD | 13,470,000.00 USD | 0.00 USD | 72,920.00 USD | 32,820.00 USD | 41,580.00 USD |
| `1D` | `62.00` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 15,300.00 USD | 3,100.00 USD | 8,280.00 USD |
| `7D` | `62.00` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 50,080.00 USD | 8,550.00 USD | 40,590.00 USD |
| `1D` | `62.10` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 2,530.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.10` | 13,580,000.00 USD | 13,580,000.00 USD | 0.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.20` | 13,690,000.00 USD | 13,690,000.00 USD | 0.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD |
| `7D` | `62.30` | 13,840,000.00 USD | 13,840,000.00 USD | 0.00 USD | 29,050.00 USD | 23,450.00 USD | 97,450.00 USD |
| `7D` | `62.40` | 13,980,000.00 USD | 13,980,000.00 USD | 0.00 USD | 77,960.00 USD | 27,560.00 USD | 30,890.00 USD |
| `7D` | `62.50` | 14,060,000.00 USD | 14,060,000.00 USD | 0.00 USD | 42,730.00 USD | 14,320.00 USD | 26,610.00 USD |
| `7D` | `62.60` | 14,130,000.00 USD | 14,130,000.00 USD | 0.00 USD | 33,900.00 USD | 7,830.00 USD | 27,730.00 USD |
| `7D` | `62.70` | 14,210,000.00 USD | 14,210,000.00 USD | 0.00 USD | 22,020.00 USD | 12,490.00 USD | 47,090.00 USD |
| `7D` | `62.80` | 14,360,000.00 USD | 14,360,000.00 USD | 0.00 USD | 71,230.00 USD | 28,960.00 USD | 45,150.00 USD |
| `7D` | `62.90` | 14,450,000.00 USD | 14,450,000.00 USD | 0.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD |
| `7D` | `63.00` | 14,510,000.00 USD | 14,510,000.00 USD | 0.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD |
| `7D` | `63.10` | 14,550,000.00 USD | 14,550,000.00 USD | 0.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD |
| `7D` | `63.30` | 14,590,000.00 USD | 14,590,000.00 USD | 0.00 USD | 15,010.00 USD | 11,500.00 USD | 9,730.00 USD |
| `7D` | `63.40` | 14,610,000.00 USD | 14,610,000.00 USD | 0.00 USD | 11,980.00 USD | 1,320.00 USD | 9,960.00 USD |
| `7D` | `63.50` | 14,640,000.00 USD | 14,640,000.00 USD | 0.00 USD | 5,430.00 USD | 15,810.00 USD | 4,760.00 USD |
| `7D` | `63.60` | 14,740,000.00 USD | 14,740,000.00 USD | 0.00 USD | 63,480.00 USD | 20,800.00 USD | 11,880.00 USD |
| `7D` | `63.70` | 14,810,000.00 USD | 14,810,000.00 USD | 0.00 USD | 21,940.00 USD | 18,810.00 USD | 35,480.00 USD |
| `7D` | `63.80` | 14,880,000.00 USD | 14,880,000.00 USD | 0.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD |
| `7D` | `63.90` | 14,900,000.00 USD | 14,900,000.00 USD | 0.00 USD | 7,650.00 USD | 12,840.00 USD | 8,940.00 USD |
| `7D` | `64.00` | 14,950,000.00 USD | 14,950,000.00 USD | 0.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD |
| `7D` | `64.10` | 14,980,000.00 USD | 14,980,000.00 USD | 0.00 USD | 20,350.00 USD | 667.05 USD | 10,640.00 USD |
| `7D` | `64.20` | 15,020,000.00 USD | 15,020,000.00 USD | 0.00 USD | 28,840.00 USD | 14,530.00 USD | 584.77 USD |
| `7D` | `64.40` | 15,070,000.00 USD | 15,070,000.00 USD | 0.00 USD | 0.00 USD | 17,760.00 USD | 29,110.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `417.62M` | Total OI Tokens: `7,431,627.1 LTC`
  * 1h OI Change: `-0.07%` | 4h OI Change: `+2.37%` | 24h OI Change: `-7.97%`
  * Exchange Breakdown: Binance=`73.86M` | Bybit=`67.06M` | OKX=`34.23M` | Hyperliquid=`22.46M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `13.71K` | Last 24h: `31.76K` | Last 3d: `59.78K` | Last 7d: `115.16K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0033%` |
| **USDT Bybit** | `0.0090%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0034%` | **USDT Bitget** | `0.0100%` |
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
| `4H` | `LTC` | `48.65%` | `51.35%` | `0.95` | 52,430,000.00 USD |
| `4H` | `Binance` | `46.26%` | `53.74%` | `0.86` | 16,910,000.00 USD |
| `4H` | `OKX` | `45.26%` | `54.74%` | `0.83` | 6,760,000.00 USD |
| `4H` | `Bybit` | `54.55%` | `45.45%` | `1.20` | 4,260,000.00 USD |
| `4H` | `KuCoin` | `51.69%` | `48.31%` | `1.07` | 448,310.00 USD |
| `4H` | `Gate` | `47.18%` | `52.82%` | `0.89` | 4,790,000.00 USD |
| `4H` | `Bitget` | `57.37%` | `42.63%` | `1.35` | 1,700,000.00 USD |
| `4H` | `BingX` | `40.93%` | `59.07%` | `0.69` | 9,500,000.00 USD |
| `4H` | `MEXC` | `51.98%` | `48.02%` | `1.08` | 2,520,000.00 USD |
| `4H` | `Bitunix` | `49.85%` | `50.15%` | `0.99` | 1,520,000.00 USD |
| `4H` | `Hyperliquid` | `72.53%` | `27.47%` | `2.64` | 959,630.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.02%` | `49.98%` | `1.00` | 1,550,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `98.67%` | `1.33%` | `74.19` | 1,280,000.00 USD |
| `4H` | `HTX` | `54.94%` | `45.06%` | `1.22` | 111,180.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `35.28%` | `64.72%` | `0.55` | 6,300.00 USD |
| `4H` | `Aster` | `67.01%` | `32.99%` | `2.03` | 88,840.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `81.98%` | `18.02%` | `4.55` | 24,890.00 USD |
| `4H` | `Whale Positions` | `46.26%` | `53.74%` | `0.86` | 16,910,000.00 USD |
| `4H` | `Global Accounts` | `48.65%` | `51.35%` | `0.95` | 52,430,000.00 USD |


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
| `0:00 UTC` | `56.14` | `56.15` | `56.14` | `56.19` | `56.14` | 28,533.32 USD | 19,723.27 USD | 8,810.04 USD | 10,913.23 USD | `+38.25%` | `0B / 1S` |

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
| `5m` | 28,640.00 USD | 196,300.00 USD | **`ACCUMULATION`** |
| `15m` | 80,400.00 USD | -32,540.00 USD | **`ACCUMULATION`** |
| `30m` | 166,820.00 USD | -462,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 145,400.00 USD | -190,730.00 USD | **`DISTRIBUTION`** |
| `2h` | 252,610.00 USD | -245,140.00 USD | **`ACCUMULATION`** |
| `4h` | 587,990.00 USD | -1,630,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -539,850.00 USD | -3,710,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 130,800.00 USD | -4,360,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,660,000.00 USD | -6,670,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 972,510.00 USD | -3,310,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 3,600,000.00 USD | -25,160,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -23,440,000.00 USD | -196,670,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+28.64K` | 15m=`+80.40K` | 1h=`+145.40K` | 24h=`+972.51K`
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
  * `2026-10-30 11:03:56 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:28:56 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:29:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `54.30` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `53.35` (Risk Distance: `0.9433` pts)
  * +2.5R Take Profit: `56.65`
  * Mathematical Lot Sizing: **`10.60 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `56.18` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `57.12` (Risk Distance: `0.9433` pts)
  * +2.5R Take Profit: `53.82`
  * Mathematical Lot Sizing: **`10.60 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`56.39`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
