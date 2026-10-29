# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 04:47:08 IST` (`2026-10-29 23:17:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.30` | **Live Ask Quote**: `8.33` | **Mid Price**: `8.32`
- **Spread Points**: `3.00` | **Spread BPS**: `36.08 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `4` | Point: `0.0001`
  * Point Value (1.0 Lot): `0.00 USD` | Point Value (0.01 Lot): `0.0000 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `8.65` | VWAP Z-Score: `-1.75` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0966` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `26.32` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `9.25` | Lower -3.00σ Band: `8.05`
  * Upper +2.51σ Band: `9.15` | Lower -2.51σ Band: `8.15`
  * Upper +2.01σ Band: `9.05` | Lower -2.01σ Band: `8.25`
  * Upper +2.00σ Band: `9.05` | Lower -2.00σ Band: `8.25`
  * Upper +1.28σ Band: `8.91` | Lower -1.28σ Band: `8.39`
  * Upper +1.00σ Band: `8.85` | Lower -1.00σ Band: `8.45`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.39` | EMA-20=`8.52` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.65` (Slope: `+0.0000`) | EMA-100=`8.72`
  * Institutional Anchors: EMA-144=`8.75` | EMA-200=`8.77` (Slope: `-0.5341`) | EMA-233=`8.79`
- **Range Boundaries**: 24H High=`9.06` | 24H Low=`8.23` | Weekly High=`9.14` | Weekly Low=`8.23`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.43` (Distance: `-1.29%`)
  * Point of Control (POC) = `8.32` (Distance: `+0.06%`)
  * Value Area Low (VAL) = `8.27` (Distance: `+0.65%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`8.90` | POC=`8.74` | VAL=`8.55`
  * Prior Day Extremes: PDH=`9.06` | PDL=`8.24` | PDC=`8.33`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`8.99` | Weekly POC=`8.92` | Weekly VAL=`8.74`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`8.58` | Low=`8.23`
  * London Session (08:00-16:00 UTC): High=`8.35` | Low=`8.28`
  * New York Session (13:00-21:00 UTC): High=`8.36` | Low=`8.27`
  * Initial Balance (First Hour): IB High=`8.34` | IB Low=`8.29`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.28` - `8.35`
  * Optimal Trade Entry (OTE 0.705): `8.33`
  * Structural Invalidation Anchor (0.786): `8.38`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.29` | `8.31` | `8.26` | `8.30` | `198,988` | 1,648,497.71 USD | 207,134.73 USD | `+12.57%` | -7,704,359.12 USD | `+0.24` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `8.30` | `8.35` | `8.29` | `8.34` | `91,769` | 763,246.48 USD | 104,731.81 USD | `+13.72%` | -7,599,627.31 USD | `-0.09` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `8.34` | `8.34` | `8.32` | `8.33` | `16,993` | 141,561.86 USD | 13,597.29 USD | `+9.61%` | -7,586,030.02 USD | `-0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `8.37` | `8.37` | `8.32` | `8.35` | `466,028` | 3,889,099.59 USD | 899,295.70 USD | `+23.12%` | -7,639,081.69 USD | `+0.89` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `8.35` | `8.36` | `8.26` | `8.34` | `603,478` | 5,007,062.71 USD | -49,259.60 USD | `-0.98%` | -7,688,341.29 USD | `+0.09` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `8.34` | `8.34` | `8.32` | `8.33` | `16,993` | 141,561.86 USD | 13,597.29 USD | `+9.61%` | -7,674,744.01 USD | `+0.14` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `8.35` | `8.60` | `8.31` | `8.43` | `1,902,791` | 16,105,514.90 USD | 1,294,377.61 USD | `+8.04%` | -9,812,377.23 USD | `+1.16` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `8.43` | `8.45` | `8.30` | `8.35` | `2,136,996` | 17,893,618.62 USD | 2,059,807.18 USD | `+11.51%` | -7,752,570.05 USD | `+1.48` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `8.35` | `8.36` | `8.26` | `8.32` | `618,057` | 5,128,519.71 USD | -45,718.78 USD | `-0.89%` | -7,798,288.83 USD | `+0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -2,154,015.33 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -4,666,010.97 USD | `-1.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.25` | `8.33` | `9,140,965` | 77,187,147.54 USD | -3,122,221.39 USD | `-4.05%` | -7,788,232.36 USD | `-1.30` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.59` | `8.80` | `8.57` | `8.62` | `1,816,830` | 15,790,058.74 USD | 58,580.54 USD | `+0.37%` | -2,364,450.84 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | -2,100,193.35 USD | `+0.79` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -2,154,015.33 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -4,666,010.97 USD | `-1.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.25` | `8.33` | `9,140,965` | 77,187,147.54 USD | -3,122,221.39 USD | `-4.05%` | -7,788,232.36 USD | `-1.30` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`8.32`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:46:31 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1517` | `0x7737...bf66` | `SHORT` | 1,430,911.93 USD | `171,568.06` | `7.43` | `8.29` | `104.49` | -155,366.92 USD | `-10.86%` | `10X Cross` |
| `1613` | `0xeadc...9d55` | `LONG` | 1,334,492.25 USD | `160,070.56` | `8.11` | `8.29` | `0.000000` | 36,854.68 USD | `+2.76%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `8.94` | 10,136.93 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 10.14K USD at 8.9443 USD [API] | `2026-10-28 19:39:23` |
| `ANNOUNCEMENT` | `INFO` | `9.03` | 10,191.71 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 10.19K USD at 9.0280 USD [API] | `2026-10-28 19:56:24` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`9.10` (Vol: 233,400.00 USD, Dist: `+8.96%`) | Long MP=`8.23` (Vol: 195,200.00 USD, Dist: `--1.50%`)
  * 48H Horizon: Short MP=`9.10` (Vol: 233,400.00 USD, Dist: `+8.98%`) | Long MP=`8.23` (Vol: 195,200.00 USD, Dist: `--1.48%`)
  * 3D Horizon: Short MP=`9.22` (Vol: 251,900.00 USD, Dist: `+10.46%`) | Long MP=`8.23` (Vol: 195,200.00 USD, Dist: `--1.48%`)
  * 7D Horizon: Short MP=`9.28` (Vol: 426,900.00 USD, Dist: `+11.16%`) | Long MP=`8.22` (Vol: 195,200.00 USD, Dist: `--1.54%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `1.68` | 788.62 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 702.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.76` | 194.15 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 2,540.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.89` | 208.88 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 234.37 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.94` | 212.85 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 598.85 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.96` | 13,480.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 159.60 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 110.52 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 4,920.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 8,700.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 164.15 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 814.80 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 275.55 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 150.77 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 19,330.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 147.42 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 232.67 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 44,510.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 111.12 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 762.99 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 122.53 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 534.93 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 3,560.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 1,360.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 233.53 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,500.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.79` | 948.75 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.14` | 159.29 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.17` | 438.38 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.18` | 174.89 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 169.40 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 806.51 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.29` | 8,590.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.30` | 2,870.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.37` | 188.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 110.77 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.61` | 525.43 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 486.93 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 2,680.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.64` | 433.47 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 105.11 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 3,280.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 8,380.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.70` | 7,340.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 467.01 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.88` | 18,460.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.89` | 489.50 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 3,880.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 1,230.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 115.54 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 4,430.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.00` | 213.56 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.03` | 167.78 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 314.59 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 736.47 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 504.74 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 318.46 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.11` | 529.54 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 250.20 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 396.06 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.16` | 119.60 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 5,610.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 2,250.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 1,050.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 161,490.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.32` | 232.85 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 1,230.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 660.46 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 20,160.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 160,400.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,360.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.47` | 1,320.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.51` | 367.41 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 121.38 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 2,760.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.59` | 35,940.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 468.55 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.64` | 229.24 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.72` | 2,390.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 238.86 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 3,190.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 801.40 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 2,890.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 736.72 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.80` | 696.60 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 106.65 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.83` | 145.88 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.84` | 561.53 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.86` | 2,110.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 984.70 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.92` | 277.35 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.93` | 147.19 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 11,720.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.99` | 447.98 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 331.68 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 105.61 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 265.10 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 1,690.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 405.14 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,130.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 1,140.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 2,160.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 4,390.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.24` | 300.65 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 2,410.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 972.65 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 2,510.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.32` | 277.04 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,470.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 348,420.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 11,550.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 3,830.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 306.32 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 1,980.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 6,780.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 2,510.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.47` | 362,980.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 3,620.00 USD | 797,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 794,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.57` | 1,530.00 USD | 785,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 537.37 USD | 783,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 1,770.00 USD | 783,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.59` | 1,100.00 USD | 781,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 780,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 364.90 USD | 778,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.67` | 1,640.00 USD | 777,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.70` | 1,700.00 USD | 776,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 16,070.00 USD | 774,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 6,180.00 USD | 758,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 752,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 6,780.00 USD | 751,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 16,960.00 USD | 744,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 4,930.00 USD | 727,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 1,500.00 USD | 722,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 2,670.00 USD | 720,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 158.14 USD | 718,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 4,410.00 USD | 718,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.86` | 19,810.00 USD | 713,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,340.00 USD | 693,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 1,580.00 USD | 690,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.91` | 269.30 USD | 688,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 3,760.00 USD | 688,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 3,480.00 USD | 684,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 636.74 USD | 681,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.97` | 2,810.00 USD | 680,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.99` | 1,100.00 USD | 677,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 746.58 USD | 676,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 20,860.00 USD | 676,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.01` | 281.86 USD | 655,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.03` | 1,370.00 USD | 654,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.04` | 704.50 USD | 653,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 354.23 USD | 652,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.07` | 1,260.00 USD | 652,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 6,700.00 USD | 651,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 1,420.00 USD | 644,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.09` | 3,020.00 USD | 643,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 28,230.00 USD | 640,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 611,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 777.50 USD | 611,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,270.00 USD | 610,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.16` | 2,370.00 USD | 590,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.17` | 215.59 USD | 588,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.17` | 1,440.00 USD | 587,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.18` | 1,440.00 USD | 586,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 7,950.00 USD | 585,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 29,440.00 USD | 577,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.24` | 179.65 USD | 547,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 185.83 USD | 547,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 21,280.00 USD | 547,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.26` | 419.41 USD | 525,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 38,110.00 USD | 525,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.33` | 4,910.00 USD | 487,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.34` | 4,370.00 USD | 482,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.36` | 3,320,000.00 USD | 3,320,000.00 USD | 6,810.00 USD | 2,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.37` | 6,420.00 USD | 478,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 5,020.00 USD | 471,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 13,200.00 USD | 466,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.39` | 1,550.00 USD | 453,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.40` | 3,310,000.00 USD | 3,310,000.00 USD | 6,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.42` | 338.94 USD | 452,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.42` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 48.44 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.42` | 147.61 USD | 451,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.43` | 2,880.00 USD | 451,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.44` | 3,090,000.00 USD | 3,090,000.00 USD | 196.00 USD | 0.00 USD | 18,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.44` | 3,300,000.00 USD | 3,300,000.00 USD | 331.70 USD | 1,680.00 USD | 15.01 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.45` | 210.99 USD | 448,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 1,620.00 USD | 448,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.46` | 3,070,000.00 USD | 3,070,000.00 USD | 723.17 USD | 0.00 USD | 31,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.46` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 1,410.00 USD | 24,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.46` | 4,590.00 USD | 446,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 1,120.00 USD | 442,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.48` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 11,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.48` | 3,280,000.00 USD | 3,280,000.00 USD | 9,120.00 USD | 0.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.49` | 1,050.00 USD | 441,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 962.81 USD | 440,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.50` | 3,030,000.00 USD | 3,030,000.00 USD | 717.40 USD | 4,920.00 USD | 24,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 421.78 USD | 439,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.52` | 3,000,000.00 USD | 3,000,000.00 USD | 26,110.00 USD | 9,580.00 USD | 36,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.52` | 3,250,000.00 USD | 3,250,000.00 USD | 1,150.00 USD | 14,470.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 438,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.54` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 62.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.54` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 4,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.54` | 1,510.00 USD | 434,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 572.67 USD | 432,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.56` | 2,930,000.00 USD | 2,930,000.00 USD | 15,020.00 USD | 4,270.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.56` | 3,210,000.00 USD | 3,210,000.00 USD | 19,530.00 USD | 4,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.57` | 25,060.00 USD | 432,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.58` | 118.25 USD | 407,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.58` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 91.65 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.59` | 24,760.00 USD | 407,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.60` | 2,910,000.00 USD | 2,910,000.00 USD | 405.20 USD | 3,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.61` | 1,520.00 USD | 382,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.62` | 878.24 USD | 380,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.62` | 2,900,000.00 USD | 2,900,000.00 USD | 583.80 USD | 0.00 USD | 11,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 380,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.63` | 378.93 USD | 379,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.64` | 2,890,000.00 USD | 2,890,000.00 USD | 17,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.64` | 3,180,000.00 USD | 3,180,000.00 USD | 812.40 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.66` | 1,410.00 USD | 378,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.66` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 9,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.66` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 23,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 1,740.00 USD | 377,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.67` | 1,890.00 USD | 375,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.68` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.68` | 1,120.00 USD | 373,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.70` | 1,460.00 USD | 372,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.70` | 2,860,000.00 USD | 2,860,000.00 USD | 321.75 USD | 2,390.00 USD | 14,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.72` | 2,850,000.00 USD | 2,850,000.00 USD | 4,600.00 USD | 1,630.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.72` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.74` | 2,830,000.00 USD | 2,830,000.00 USD | 3,340.00 USD | 4,580.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.74` | 3,120,000.00 USD | 3,120,000.00 USD | 976.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.76` | 2,820,000.00 USD | 2,820,000.00 USD | 1,510.00 USD | 1,100.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.76` | 3,120,000.00 USD | 3,120,000.00 USD | 812.95 USD | 5,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 371,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.78` | 695.32 USD | 370,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.78` | 2,810,000.00 USD | 2,810,000.00 USD | 44,950.00 USD | 3,730.00 USD | 9,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.78` | 3,110,000.00 USD | 3,110,000.00 USD | 43,620.00 USD | 4,900.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 2,870.00 USD | 370,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.79` | 12,800.00 USD | 367,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.80` | 2,750,000.00 USD | 2,750,000.00 USD | 39,070.00 USD | 10,860.00 USD | 8,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.80` | 3,040,000.00 USD | 3,040,000.00 USD | 14,770.00 USD | 12,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.82` | 3,130.00 USD | 354,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.82` | 2,690,000.00 USD | 2,690,000.00 USD | 5,100.00 USD | 7,610.00 USD | 5,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.82` | 3,010,000.00 USD | 3,010,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.84` | 2,670,000.00 USD | 2,670,000.00 USD | 2,680.00 USD | 4,910.00 USD | 12,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.84` | 3,000,000.00 USD | 3,000,000.00 USD | 30,950.00 USD | 2,380.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 24,340.00 USD | 351,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.86` | 2,650,000.00 USD | 2,650,000.00 USD | 15,790.00 USD | 1,680.00 USD | 16,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.86` | 2,940,000.00 USD | 2,940,000.00 USD | 25,770.00 USD | 5,460.00 USD | 17,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 326,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.88` | 2,620,000.00 USD | 2,620,000.00 USD | 46,100.00 USD | 9,570.00 USD | 22,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.88` | 2,890,000.00 USD | 2,890,000.00 USD | 58,120.00 USD | 12,780.00 USD | 30,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.90` | 2,540,000.00 USD | 2,540,000.00 USD | 14,150.00 USD | 7,630.00 USD | 7,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.90` | 2,790,000.00 USD | 2,790,000.00 USD | 33,680.00 USD | 12,890.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 505.13 USD | 326,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.92` | 2,510,000.00 USD | 2,510,000.00 USD | 24,660.00 USD | 2,950.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.92` | 2,730,000.00 USD | 2,730,000.00 USD | 55,490.00 USD | 8,420.00 USD | 14,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 16,340.00 USD | 325,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 2,480,000.00 USD | 2,480,000.00 USD | 20,330.00 USD | 6,860.00 USD | 48,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.94` | 2,650,000.00 USD | 2,650,000.00 USD | 51,390.00 USD | 9,960.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 127,110.00 USD | 309,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.96` | 4,090.00 USD | 182,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 2,400,000.00 USD | 2,400,000.00 USD | 2,830.00 USD | 11,220.00 USD | 97,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.96` | 2,560,000.00 USD | 2,560,000.00 USD | 21,840.00 USD | 6,920.00 USD | 86,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 4,520.00 USD | 178,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.97` | 10,990.00 USD | 173,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.98` | 2,290,000.00 USD | 2,290,000.00 USD | 17,030.00 USD | 3,300.00 USD | 37,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.98` | 2,440,000.00 USD | 2,440,000.00 USD | 56,660.00 USD | 26,790.00 USD | 121,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 17,430.00 USD | 162,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.00` | 2,740.00 USD | 145,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 2,230,000.00 USD | 2,230,000.00 USD | 1,500.00 USD | 16,670.00 USD | 62,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.00` | 2,240,000.00 USD | 2,240,000.00 USD | 61,850.00 USD | 10,300.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.01` | 284.42 USD | 142,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.02` | 235.80 USD | 142,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.02` | 2,150,000.00 USD | 2,150,000.00 USD | 81,330.00 USD | 10,580.00 USD | 82,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.02` | 2,160,000.00 USD | 2,160,000.00 USD | 20,910.00 USD | 46,670.00 USD | 57,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 957.70 USD | 142,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.04` | 89,210.00 USD | 141,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.04` | 1,980,000.00 USD | 1,980,000.00 USD | 33,700.00 USD | 17,810.00 USD | 14,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.04` | 2,030,000.00 USD | 2,030,000.00 USD | 152,340.00 USD | 56,910.00 USD | 86,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 10,430.00 USD | 51,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 1,370.00 USD | 41,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.06` | 1,910,000.00 USD | 1,910,000.00 USD | 76,840.00 USD | 22,300.00 USD | 18,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.06` | 1,740,000.00 USD | 1,740,000.00 USD | 122,100.00 USD | 20,850.00 USD | 86,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.06` | 4,380.00 USD | 40,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.07` | 232.96 USD | 35,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.08` | 1,790,000.00 USD | 1,790,000.00 USD | 36,720.00 USD | 6,070.00 USD | 13,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.08` | 1,510,000.00 USD | 1,510,000.00 USD | 7,170.00 USD | 8,710.00 USD | 20,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.09` | 3,420.00 USD | 35,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.10` | 886.24 USD | 32,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.10` | 1,740,000.00 USD | 1,740,000.00 USD | 32,890.00 USD | 14,990.00 USD | 96,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.10` | 1,470,000.00 USD | 1,470,000.00 USD | 61,500.00 USD | 19,700.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.11` | 6,000.00 USD | 31,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.12` | 241.26 USD | 25,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.12` | 1,590,000.00 USD | 1,590,000.00 USD | 75,310.00 USD | 12,270.00 USD | 215,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.12` | 1,380,000.00 USD | 1,380,000.00 USD | 27,520.00 USD | 10,810.00 USD | 142,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 843.86 USD | 25,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.13` | 855.64 USD | 24,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.14` | 1,290,000.00 USD | 1,290,000.00 USD | 12,410.00 USD | 0.00 USD | 58,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.14` | 1,200,000.00 USD | 1,200,000.00 USD | 72,460.00 USD | 25,370.00 USD | 142,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.16` | 1,220,000.00 USD | 1,220,000.00 USD | 44,830.00 USD | 29,660.00 USD | 159,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.16` | 956,630.00 USD | 956,630.00 USD | 38,430.00 USD | 5,510.00 USD | 30,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.16` | 871.61 USD | 23,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.18` | 984,710.00 USD | 984,710.00 USD | 133,120.00 USD | 19,620.00 USD | 175,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.18` | 881,870.00 USD | 881,870.00 USD | 39,830.00 USD | 43,260.00 USD | 175,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.20` | 8,590.00 USD | 22,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.20` | 656,430.00 USD | 656,430.00 USD | 33,560.00 USD | 32,530.00 USD | 16,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.20` | 623,100.00 USD | 623,100.00 USD | 92,320.00 USD | 58,100.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 1,910.00 USD | 13,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.21` | 147.87 USD | 11,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.22` | 573,540.00 USD | 573,540.00 USD | 32,330.00 USD | 39,650.00 USD | 35,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.22` | 462,810.00 USD | 462,810.00 USD | 117,230.00 USD | 21,570.00 USD | 10,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.22` | 2,100.00 USD | 11,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.24` | 465,770.00 USD | 465,770.00 USD | 163,080.00 USD | 10,300.00 USD | 69,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.24` | 313,210.00 USD | 313,210.00 USD | 39,950.00 USD | 3,480.00 USD | 107,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.26` | 9,710.00 USD | 9,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.26` | 222,530.00 USD | 222,530.00 USD | 15,150.00 USD | 15,590.00 USD | 16,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.26` | 162,700.00 USD | 162,700.00 USD | 30,490.00 USD | 5,750.00 USD | 1,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.28` | 175,200.00 USD | 175,200.00 USD | 175,140.00 USD | 0.00 USD | 57.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.28` | 124,740.00 USD | 124,740.00 USD | 122,850.00 USD | 0.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.30` | 183,820.00 USD | 183,820.00 USD | 183,720.00 USD | 0.00 USD | 107.30 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.30` | 367,650.00 USD | 367,650.00 USD | 183,720.00 USD | 0.00 USD | 107.30 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.30` | 154,020.00 USD | 154,020.00 USD | 152,370.00 USD | 0.00 USD | 1,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.30` | 308,040.00 USD | 308,040.00 USD | 152,370.00 USD | 0.00 USD | 1,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.32` | 422,910.00 USD | 422,910.00 USD | 55,190.00 USD | 0.00 USD | 77.98 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.32` | 356,000.00 USD | 356,000.00 USD | 42,900.00 USD | 0.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.34` | 360,490.00 USD | 360,490.00 USD | 0.00 USD | 0.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.36` | 423,040.00 USD | 423,040.00 USD | 0.00 USD | 0.00 USD | 128.12 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.36` | 378,390.00 USD | 378,390.00 USD | 0.00 USD | 0.00 USD | 17,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.38` | 423,740.00 USD | 423,740.00 USD | 691.75 USD | 0.00 USD | 9.52 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.38` | 436,130.00 USD | 436,130.00 USD | 0.00 USD | 0.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.40` | 469,270.00 USD | 469,270.00 USD | 0.00 USD | 0.00 USD | 33,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.42` | 424,530.00 USD | 424,530.00 USD | 788.46 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.42` | 485,340.00 USD | 485,340.00 USD | 16,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.44` | 514,510.00 USD | 514,510.00 USD | 0.00 USD | 0.00 USD | 89,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.44` | 495,820.00 USD | 495,820.00 USD | 10,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.46` | 702,750.00 USD | 702,750.00 USD | 0.00 USD | 4,700.00 USD | 183,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.46` | 983,910.00 USD | 983,910.00 USD | 365,050.00 USD | 0.00 USD | 123,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.48` | 800,510.00 USD | 800,510.00 USD | 0.00 USD | 39,180.00 USD | 58,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.48` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 49,360.00 USD | 104,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.50` | 1,080,000.00 USD | 1,080,000.00 USD | 66,120.00 USD | 88,980.00 USD | 120,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.50` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 100,070.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.52` | 1,510,000.00 USD | 1,510,000.00 USD | 203,080.00 USD | 69,980.00 USD | 164,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.52` | 1,470,000.00 USD | 1,470,000.00 USD | 2,990.00 USD | 135,400.00 USD | 92,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.54` | 1,620,000.00 USD | 1,620,000.00 USD | 61,500.00 USD | 32,530.00 USD | 16,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.54` | 1,680,000.00 USD | 1,680,000.00 USD | 71,540.00 USD | 136,470.00 USD | 2,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.56` | 1,840,000.00 USD | 1,840,000.00 USD | 183,280.00 USD | 33,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.56` | 2,490,000.00 USD | 2,490,000.00 USD | 691,140.00 USD | 122,650.00 USD | 790.79 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.58` | 2,260,000.00 USD | 2,260,000.00 USD | 234,090.00 USD | 5,060.00 USD | 179,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.58` | 3,260,000.00 USD | 3,260,000.00 USD | 599,490.00 USD | 164,810.00 USD | 801.88 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.60` | 2,350.00 USD | 2,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.60` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 57,190.00 USD | 120,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.60` | 3,380,000.00 USD | 3,380,000.00 USD | 75,040.00 USD | 39,160.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.62` | 2,710,000.00 USD | 2,710,000.00 USD | 65,710.00 USD | 57,150.00 USD | 149,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.62` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 43,670.00 USD | 86,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.64` | 2,860,000.00 USD | 2,860,000.00 USD | 89,460.00 USD | 30,330.00 USD | 29,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.64` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 12,800.00 USD | 51,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.66` | 3,060,000.00 USD | 3,060,000.00 USD | 78,620.00 USD | 14,830.00 USD | 108,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.66` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 16,520.00 USD | 950.21 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.68` | 3,350,000.00 USD | 3,350,000.00 USD | 65,090.00 USD | 9,810.00 USD | 212,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.68` | 4,170,000.00 USD | 4,170,000.00 USD | 207,090.00 USD | 43,100.00 USD | 335,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.70` | 3,450,000.00 USD | 3,450,000.00 USD | 50,130.00 USD | 16,260.00 USD | 30,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.70` | 4,290,000.00 USD | 4,290,000.00 USD | 29,260.00 USD | 41,840.00 USD | 46,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.72` | 3,510,000.00 USD | 3,510,000.00 USD | 18,250.00 USD | 0.00 USD | 50,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.74` | 3,610,000.00 USD | 3,610,000.00 USD | 49,110.00 USD | 28,810.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.74` | 4,370,000.00 USD | 4,370,000.00 USD | 48,810.00 USD | 30,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.76` | 373.93 USD | 2,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.76` | 3,730,000.00 USD | 3,730,000.00 USD | 112,960.00 USD | 2,530.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.76` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 22,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.78` | 1,230.00 USD | 3,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.78` | 3,890,000.00 USD | 3,890,000.00 USD | 108,350.00 USD | 11,500.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.78` | 4,450,000.00 USD | 4,450,000.00 USD | 2,300.00 USD | 0.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.80` | 4,090,000.00 USD | 4,090,000.00 USD | 125,120.00 USD | 22,330.00 USD | 53,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.80` | 4,550,000.00 USD | 4,550,000.00 USD | 27,360.00 USD | 33,750.00 USD | 32,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.82` | 4,110,000.00 USD | 4,110,000.00 USD | 19,020.00 USD | 0.00 USD | 203.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.82` | 4,650,000.00 USD | 4,650,000.00 USD | 103,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.82` | 6,000.00 USD | 9,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.84` | 541.67 USD | 10,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.84` | 4,230,000.00 USD | 4,230,000.00 USD | 40,640.00 USD | 8,820.00 USD | 73,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.86` | 4,260,000.00 USD | 4,260,000.00 USD | 13,620.00 USD | 2,250.00 USD | 10,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.86` | 4,760,000.00 USD | 4,760,000.00 USD | 29,310.00 USD | 0.00 USD | 82,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.88` | 4,270,000.00 USD | 4,270,000.00 USD | 1,170.00 USD | 8,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.88` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 0.00 USD | 28,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.90` | 4,430,000.00 USD | 4,430,000.00 USD | 31,860.00 USD | 8,140.00 USD | 122,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.90` | 4,910,000.00 USD | 4,910,000.00 USD | 2,440.00 USD | 0.00 USD | 115,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 4,490,000.00 USD | 4,490,000.00 USD | 40,710.00 USD | 7,360.00 USD | 17,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.92` | 4,930,000.00 USD | 4,930,000.00 USD | 1,730.00 USD | 0.00 USD | 17,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.94` | 4,570,000.00 USD | 4,570,000.00 USD | 41,740.00 USD | 12,260.00 USD | 18,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.94` | 4,990,000.00 USD | 4,990,000.00 USD | 58,330.00 USD | 0.00 USD | 433.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.96` | 4,570,000.00 USD | 4,570,000.00 USD | 2,010.00 USD | 0.00 USD | 152.79 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.96` | 4,990,000.00 USD | 4,990,000.00 USD | 1,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.98` | 4,620,000.00 USD | 4,620,000.00 USD | 25,040.00 USD | 5,550.00 USD | 19,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.98` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 9,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.00` | 4,750,000.00 USD | 4,750,000.00 USD | 85,360.00 USD | 30,520.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.00` | 5,330,000.00 USD | 5,330,000.00 USD | 297,650.00 USD | 11,360.00 USD | 20,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 4,850,000.00 USD | 4,850,000.00 USD | 40,920.00 USD | 43,160.00 USD | 18,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.02` | 5,420,000.00 USD | 5,420,000.00 USD | 34,650.00 USD | 56,120.00 USD | 749.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 5,020,000.00 USD | 5,020,000.00 USD | 87,540.00 USD | 43,590.00 USD | 38,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.04` | 5,600,000.00 USD | 5,600,000.00 USD | 90,520.00 USD | 74,750.00 USD | 15,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.06` | 5,150,000.00 USD | 5,150,000.00 USD | 35,620.00 USD | 33,420.00 USD | 60,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.06` | 5,670,000.00 USD | 5,670,000.00 USD | 7,440.00 USD | 14,960.00 USD | 53,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.06` | 434.94 USD | 10,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.08` | 5,280,000.00 USD | 5,280,000.00 USD | 28,800.00 USD | 29,710.00 USD | 71,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.08` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.10` | 5,600,000.00 USD | 5,600,000.00 USD | 197,760.00 USD | 43,240.00 USD | 81,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.10` | 6,950,000.00 USD | 6,950,000.00 USD | 826,500.00 USD | 35,760.00 USD | 334,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 5,890,000.00 USD | 5,890,000.00 USD | 160,000.00 USD | 47,350.00 USD | 87,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.12` | 7,970,000.00 USD | 7,970,000.00 USD | 490,020.00 USD | 24,170.00 USD | 503,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.14` | 6,120,000.00 USD | 6,120,000.00 USD | 118,520.00 USD | 23,510.00 USD | 79,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.14` | 9,020,000.00 USD | 9,020,000.00 USD | 536,560.00 USD | 18,540.00 USD | 500,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 6,350,000.00 USD | 6,350,000.00 USD | 121,810.00 USD | 44,640.00 USD | 63,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.16` | 9,620,000.00 USD | 9,620,000.00 USD | 358,370.00 USD | 44,360.00 USD | 195,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 6,690,000.00 USD | 6,690,000.00 USD | 188,150.00 USD | 48,600.00 USD | 107,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.18` | 10,640,000.00 USD | 10,640,000.00 USD | 565,140.00 USD | 162,460.00 USD | 292,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.19` | 1,590.00 USD | 12,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.20` | 6,930,000.00 USD | 6,930,000.00 USD | 145,450.00 USD | 43,540.00 USD | 54,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.20` | 11,560,000.00 USD | 11,560,000.00 USD | 549,250.00 USD | 134,550.00 USD | 238,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.21` | 1,870.00 USD | 14,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.22` | 7,040,000.00 USD | 7,040,000.00 USD | 86,390.00 USD | 10,580.00 USD | 13,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.22` | 12,710,000.00 USD | 12,710,000.00 USD | 585,170.00 USD | 144,840.00 USD | 416,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 7,100,000.00 USD | 7,100,000.00 USD | 47,010.00 USD | 4,270.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.24` | 13,280,000.00 USD | 13,280,000.00 USD | 335,740.00 USD | 56,410.00 USD | 174,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 7,150,000.00 USD | 7,150,000.00 USD | 35,150.00 USD | 8,290.00 USD | 9,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.26` | 13,710,000.00 USD | 13,710,000.00 USD | 273,920.00 USD | 96,980.00 USD | 60,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 7,210,000.00 USD | 7,210,000.00 USD | 44,530.00 USD | 10,920.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.28` | 14,410,000.00 USD | 14,410,000.00 USD | 428,160.00 USD | 103,490.00 USD | 170,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 100.93 USD | 14,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.30` | 7,310,000.00 USD | 7,310,000.00 USD | 59,470.00 USD | 13,560.00 USD | 29,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.30` | 14,970,000.00 USD | 14,970,000.00 USD | 199,810.00 USD | 97,780.00 USD | 262,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 7,380,000.00 USD | 7,380,000.00 USD | 37,200.00 USD | 4,250.00 USD | 23,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.32` | 15,640,000.00 USD | 15,640,000.00 USD | 271,660.00 USD | 59,310.00 USD | 337,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 7,440,000.00 USD | 7,440,000.00 USD | 40,730.00 USD | 9,520.00 USD | 11,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.34` | 15,970,000.00 USD | 15,970,000.00 USD | 204,260.00 USD | 53,150.00 USD | 70,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.36` | 7,550,000.00 USD | 7,550,000.00 USD | 59,430.00 USD | 12,270.00 USD | 34,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.36` | 16,380,000.00 USD | 16,380,000.00 USD | 247,120.00 USD | 73,430.00 USD | 97,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 7,600,000.00 USD | 7,600,000.00 USD | 31,430.00 USD | 7,320.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.38` | 16,920,000.00 USD | 16,920,000.00 USD | 383,530.00 USD | 55,400.00 USD | 94,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.40` | 7,630,000.00 USD | 7,630,000.00 USD | 31,880.00 USD | 0.00 USD | 7.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.40` | 17,320,000.00 USD | 17,320,000.00 USD | 234,760.00 USD | 42,520.00 USD | 124,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.40` | 28,220.00 USD | 42,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.41` | 440.06 USD | 43,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.42` | 7,660,000.00 USD | 7,660,000.00 USD | 10,810.00 USD | 2,390.00 USD | 14,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.42` | 17,590,000.00 USD | 17,590,000.00 USD | 176,920.00 USD | 19,780.00 USD | 70,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.44` | 7,680,000.00 USD | 7,680,000.00 USD | 10,560.00 USD | 1,630.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.44` | 17,700,000.00 USD | 17,700,000.00 USD | 41,250.00 USD | 19,420.00 USD | 56,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.46` | 7,690,000.00 USD | 7,690,000.00 USD | 1,350.00 USD | 4,580.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.46` | 17,810,000.00 USD | 17,810,000.00 USD | 60,020.00 USD | 29,830.00 USD | 19,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.48` | 7,700,000.00 USD | 7,700,000.00 USD | 1,050.00 USD | 1,100.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.48` | 17,880,000.00 USD | 17,880,000.00 USD | 12,180.00 USD | 27,840.00 USD | 25,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.49` | 7,740,000.00 USD | 7,740,000.00 USD | 29,020.00 USD | 572.85 USD | 8,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.50` | 18,050,000.00 USD | 18,050,000.00 USD | 89,460.00 USD | 33,210.00 USD | 45,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.52` | 18,230,000.00 USD | 18,230,000.00 USD | 102,150.00 USD | 29,320.00 USD | 51,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.54` | 18,450,000.00 USD | 18,450,000.00 USD | 192,090.00 USD | 25,090.00 USD | 930.52 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.56` | 18,560,000.00 USD | 18,560,000.00 USD | 88,510.00 USD | 5,260.00 USD | 13,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.58` | 18,630,000.00 USD | 18,630,000.00 USD | 35,340.00 USD | 14,530.00 USD | 27,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.60` | 18,700,000.00 USD | 18,700,000.00 USD | 38,740.00 USD | 5,460.00 USD | 18,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.62` | 18,780,000.00 USD | 18,780,000.00 USD | 70,470.00 USD | 1,540.00 USD | 10,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.62` | 253.04 USD | 43,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.64` | 18,850,000.00 USD | 18,850,000.00 USD | 35,210.00 USD | 17,650.00 USD | 19,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.64` | 1,930.00 USD | 45,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.66` | 18,930,000.00 USD | 18,930,000.00 USD | 37,340.00 USD | 21,280.00 USD | 18,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.68` | 19,030,000.00 USD | 19,030,000.00 USD | 68,230.00 USD | 20,310.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.70` | 929.65 USD | 46,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.70` | 19,160,000.00 USD | 19,160,000.00 USD | 77,860.00 USD | 12,990.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.72` | 19,260,000.00 USD | 19,260,000.00 USD | 70,300.00 USD | 6,920.00 USD | 26,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 46,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.74` | 19,310,000.00 USD | 19,310,000.00 USD | 21,230.00 USD | 7,200.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.76` | 19,410,000.00 USD | 19,410,000.00 USD | 35,520.00 USD | 12,480.00 USD | 52,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.78` | 19,490,000.00 USD | 19,490,000.00 USD | 65,390.00 USD | 10,300.00 USD | 5,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.80` | 19,550,000.00 USD | 19,550,000.00 USD | 18,630.00 USD | 28,440.00 USD | 10,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.82` | 19,780,000.00 USD | 19,780,000.00 USD | 121,860.00 USD | 27,860.00 USD | 86,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.84` | 19,810,000.00 USD | 19,810,000.00 USD | 9,730.00 USD | 7,850.00 USD | 14,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.86` | 19,950,000.00 USD | 19,950,000.00 USD | 58,130.00 USD | 2,210.00 USD | 71,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.88` | 19,980,000.00 USD | 19,980,000.00 USD | 7,170.00 USD | 8,710.00 USD | 20,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.90` | 20,070,000.00 USD | 20,070,000.00 USD | 55,970.00 USD | 19,700.00 USD | 14,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.92` | 20,120,000.00 USD | 20,120,000.00 USD | 27,710.00 USD | 10,810.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.94` | 20,250,000.00 USD | 20,250,000.00 USD | 69,320.00 USD | 11,150.00 USD | 51,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.96` | 20,300,000.00 USD | 20,300,000.00 USD | 29,800.00 USD | 1,360.00 USD | 11,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.98` | 20,330,000.00 USD | 20,330,000.00 USD | 840.10 USD | 4,150.00 USD | 29,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.00` | 20,340,000.00 USD | 20,340,000.00 USD | 0.00 USD | 6,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.02` | 20,370,000.00 USD | 20,370,000.00 USD | 16,100.00 USD | 3,650.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.04` | 20,390,000.00 USD | 20,390,000.00 USD | 1,080.00 USD | 3,590.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.06` | 20,410,000.00 USD | 20,410,000.00 USD | 0.00 USD | 3,480.00 USD | 17,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.08` | 20,430,000.00 USD | 20,430,000.00 USD | 23,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.11` | 568.81 USD | 47,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.12` | 487.01 USD | 47,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.18` | 249,590.00 USD | 297,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.21` | 3,230.00 USD | 300,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.32` | 258,130.00 USD | 558,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.35` | 2,650.00 USD | 561,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 561,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.71` | 218.91 USD | 561,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.93` | 117.23 USD | 561,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.96` | 1,920.00 USD | 563,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 6,970.00 USD | 570,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.22` | 112,250.00 USD | 683,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 11,670.00 USD | 694,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,140.00 USD | 706,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.69` | 296,760.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.74` | 40,670.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.93` | 505.74 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.95` | 1,050.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.96` | 59,780.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.04` | 802.20 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.04` | 444.49 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.18` | 40,820.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.31` | 282.43 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.45` | 237.04 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.46` | 16,190.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.71` | 5,160.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.77` | 4,100.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.90` | 321.20 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.27` | 2,540.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 484.60 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.38` | 20,000.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.64` | 9,180.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.32` | 22,420.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.32` | 116.07 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.38` | 265,410.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `1.68` | 2,350,000.00 USD | 0.00 USD | 788.62 USD | `-79.92%` | `470.82` |
| `Live` | `Long` | `1.75` | 2,350,000.00 USD | 0.00 USD | 702.00 USD | `-78.97%` | `400.00` |
| `Live` | `Long` | `1.76` | 2,350,000.00 USD | 0.00 USD | 194.15 USD | `-78.85%` | `110.00` |
| `Live` | `Long` | `1.81` | 2,350,000.00 USD | 0.00 USD | 2,540.00 USD | `-78.25%` | `1,398.03` |
| `Live` | `Long` | `1.89` | 2,350,000.00 USD | 0.00 USD | 208.88 USD | `-77.41%` | `110.81` |
| `Live` | `Long` | `1.93` | 2,350,000.00 USD | 0.00 USD | 234.37 USD | `-76.93%` | `121.75` |
| `Live` | `Long` | `1.94` | 2,350,000.00 USD | 0.00 USD | 212.85 USD | `-76.81%` | `110.00` |
| `Live` | `Long` | `1.95` | 2,350,000.00 USD | 0.00 USD | 598.85 USD | `-76.69%` | `307.89` |
| `Live` | `Long` | `1.96` | 2,350,000.00 USD | 0.00 USD | 13,480.00 USD | `-76.57%` | `6,895.73` |
| `Live` | `Long` | `2.00` | 2,330,000.00 USD | 0.00 USD | 159.60 USD | `-76.09%` | `80.00` |
| `Live` | `Long` | `2.04` | 2,330,000.00 USD | 0.00 USD | 110.52 USD | `-75.61%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,330,000.00 USD | 0.00 USD | 4,920.00 USD | `-75.25%` | `2,382.76` |
| `Live` | `Long` | `2.19` | 2,330,000.00 USD | 0.00 USD | 8,700.00 USD | `-73.81%` | `3,981.48` |
| `Live` | `Long` | `2.35` | 2,320,000.00 USD | 0.00 USD | 164.15 USD | `-71.89%` | `70.00` |
| `Live` | `Long` | `2.42` | 2,320,000.00 USD | 0.00 USD | 814.80 USD | `-70.94%` | `336.00` |
| `Live` | `Long` | `2.50` | 2,320,000.00 USD | 0.00 USD | 275.55 USD | `-69.98%` | `110.00` |
| `Live` | `Long` | `2.58` | 2,320,000.00 USD | 0.00 USD | 150.77 USD | `-69.14%` | `58.55` |
| `Live` | `Long` | `2.77` | 2,320,000.00 USD | 0.00 USD | 19,330.00 USD | `-66.86%` | `6,990.57` |
| `Live` | `Long` | `2.83` | 2,300,000.00 USD | 0.00 USD | 147.42 USD | `-66.02%` | `52.00` |
| `Live` | `Long` | `2.87` | 2,300,000.00 USD | 0.00 USD | 232.67 USD | `-65.66%` | `81.21` |
| `Live` | `Long` | `2.94` | 2,300,000.00 USD | 0.00 USD | 44,510.00 USD | `-64.82%` | `15,165.76` |
| `Live` | `Long` | `2.98` | 2,250,000.00 USD | 0.00 USD | 111.12 USD | `-64.34%` | `37.35` |
| `Live` | `Long` | `3.12` | 2,250,000.00 USD | 0.00 USD | 762.99 USD | `-62.67%` | `244.94` |
| `Live` | `Long` | `3.25` | 2,250,000.00 USD | 0.00 USD | 122.53 USD | `-61.11%` | `37.76` |
| `Live` | `Long` | `3.29` | 2,250,000.00 USD | 0.00 USD | 534.93 USD | `-60.63%` | `162.84` |
| `Live` | `Long` | `3.37` | 2,250,000.00 USD | 0.00 USD | 389.53 USD | `-59.67%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,250,000.00 USD | 0.00 USD | 3,560.00 USD | `-59.55%` | `1,055.81` |
| `Live` | `Long` | `3.60` | 2,250,000.00 USD | 0.00 USD | 1,360.00 USD | `-56.79%` | `377.71` |
| `Live` | `Long` | `3.67` | 2,250,000.00 USD | 0.00 USD | 233.53 USD | `-56.07%` | `63.72` |
| `Live` | `Long` | `3.75` | 2,250,000.00 USD | 0.00 USD | 1,500.00 USD | `-54.99%` | `400.00` |
| `Live` | `Long` | `3.79` | 2,240,000.00 USD | 0.00 USD | 948.75 USD | `-54.52%` | `250.00` |
| `Live` | `Long` | `3.90` | 2,240,000.00 USD | 0.00 USD | 131.73 USD | `-53.32%` | `33.82` |
| `Live` | `Long` | `4.03` | 2,240,000.00 USD | 0.00 USD | 402.70 USD | `-51.76%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,240,000.00 USD | 0.00 USD | 152.29 USD | `-51.52%` | `37.65` |
| `Live` | `Long` | `4.14` | 2,240,000.00 USD | 0.00 USD | 159.29 USD | `-50.32%` | `38.43` |
| `Live` | `Long` | `4.17` | 2,240,000.00 USD | 0.00 USD | 438.38 USD | `-49.96%` | `105.00` |
| `Live` | `Long` | `4.18` | 2,240,000.00 USD | 0.00 USD | 174.89 USD | `-49.84%` | `41.79` |
| `Live` | `Long` | `4.24` | 2,240,000.00 USD | 0.00 USD | 169.40 USD | `-49.24%` | `40.00` |
| `Live` | `Long` | `4.25` | 2,240,000.00 USD | 0.00 USD | 806.51 USD | `-49.12%` | `189.99` |
| `Live` | `Long` | `4.29` | 2,240,000.00 USD | 0.00 USD | 8,590.00 USD | `-48.52%` | `2,000.00` |
| `Live` | `Long` | `4.30` | 2,230,000.00 USD | 0.00 USD | 2,870.00 USD | `-48.40%` | `666.20` |
| `Live` | `Long` | `4.37` | 2,230,000.00 USD | 0.00 USD | 188.00 USD | `-47.68%` | `43.07` |
| `Live` | `Long` | `4.45` | 2,230,000.00 USD | 0.00 USD | 110.77 USD | `-46.72%` | `24.92` |
| `Live` | `Long` | `4.59` | 2,230,000.00 USD | 0.00 USD | 30,970.00 USD | `-44.93%` | `6,740.93` |
| `Live` | `Long` | `4.61` | 2,200,000.00 USD | 0.00 USD | 525.43 USD | `-44.81%` | `114.10` |
| `Live` | `Long` | `4.62` | 2,200,000.00 USD | 0.00 USD | 486.93 USD | `-44.69%` | `105.51` |
| `Live` | `Long` | `4.62` | 2,200,000.00 USD | 0.00 USD | 2,680.00 USD | `-44.57%` | `579.06` |
| `Live` | `Long` | `4.64` | 2,190,000.00 USD | 0.00 USD | 433.47 USD | `-44.33%` | `93.32` |
| `Live` | `Long` | `4.66` | 2,190,000.00 USD | 0.00 USD | 105.11 USD | `-44.21%` | `22.58` |
| `Live` | `Long` | `4.67` | 2,190,000.00 USD | 0.00 USD | 3,280.00 USD | `-44.09%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,190,000.00 USD | 0.00 USD | 1,490.00 USD | `-43.97%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,190,000.00 USD | 0.00 USD | 8,380.00 USD | `-43.85%` | `1,787.97` |
| `Live` | `Long` | `4.70` | 2,180,000.00 USD | 0.00 USD | 7,340.00 USD | `-43.73%` | `1,563.75` |
| `Live` | `Long` | `4.76` | 2,170,000.00 USD | 0.00 USD | 105.64 USD | `-42.89%` | `22.17` |
| `Live` | `Long` | `4.83` | 2,170,000.00 USD | 0.00 USD | 467.01 USD | `-42.05%` | `96.59` |
| `Live` | `Long` | `4.88` | 2,170,000.00 USD | 0.00 USD | 18,460.00 USD | `-41.57%` | `3,786.00` |
| `Live` | `Long` | `4.89` | 2,150,000.00 USD | 0.00 USD | 489.50 USD | `-41.33%` | `100.00` |
| `Live` | `Long` | `4.91` | 2,150,000.00 USD | 0.00 USD | 3,880.00 USD | `-41.21%` | `790.61` |
| `Live` | `Long` | `4.92` | 2,150,000.00 USD | 0.00 USD | 1,230.00 USD | `-41.09%` | `251.00` |
| `Live` | `Long` | `4.92` | 2,150,000.00 USD | 0.00 USD | 115.54 USD | `-40.97%` | `23.46` |
| `Live` | `Long` | `4.96` | 2,150,000.00 USD | 0.00 USD | 945.36 USD | `-40.61%` | `190.79` |
| `Live` | `Long` | `4.96` | 2,150,000.00 USD | 0.00 USD | 4,430.00 USD | `-40.49%` | `893.25` |
| `Live` | `Long` | `4.97` | 2,140,000.00 USD | 0.00 USD | 282.23 USD | `-40.37%` | `56.73` |
| `Live` | `Long` | `5.00` | 2,140,000.00 USD | 0.00 USD | 213.56 USD | `-40.01%` | `42.67` |
| `Live` | `Long` | `5.01` | 2,140,000.00 USD | 0.00 USD | 56,390.00 USD | `-39.89%` | `11,243.48` |
| `Live` | `Long` | `5.03` | 2,090,000.00 USD | 0.00 USD | 167.78 USD | `-39.77%` | `33.39` |
| `Live` | `Long` | `5.04` | 2,090,000.00 USD | 0.00 USD | 314.59 USD | `-39.65%` | `62.48` |
| `Live` | `Long` | `5.04` | 2,090,000.00 USD | 0.00 USD | 736.47 USD | `-39.53%` | `145.98` |
| `Live` | `Long` | `5.05` | 2,090,000.00 USD | 0.00 USD | 504.74 USD | `-39.41%` | `99.85` |
| `Live` | `Long` | `5.08` | 2,090,000.00 USD | 0.00 USD | 318.46 USD | `-39.17%` | `62.75` |
| `Live` | `Long` | `5.11` | 2,080,000.00 USD | 0.00 USD | 529.54 USD | `-38.81%` | `103.73` |
| `Live` | `Long` | `5.12` | 2,080,000.00 USD | 0.00 USD | 250.20 USD | `-38.57%` | `48.82` |
| `Live` | `Long` | `5.13` | 2,080,000.00 USD | 0.00 USD | 396.06 USD | `-38.46%` | `77.13` |
| `Live` | `Long` | `5.16` | 2,080,000.00 USD | 0.00 USD | 119.60 USD | `-38.22%` | `23.20` |
| `Live` | `Long` | `5.17` | 2,080,000.00 USD | 0.00 USD | 1,620.00 USD | `-37.98%` | `312.94` |
| `Live` | `Long` | `5.18` | 2,080,000.00 USD | 0.00 USD | 5,610.00 USD | `-37.86%` | `1,082.04` |
| `Live` | `Long` | `5.21` | 2,080,000.00 USD | 0.00 USD | 2,250.00 USD | `-37.50%` | `431.24` |
| `Live` | `Long` | `5.25` | 2,070,000.00 USD | 0.00 USD | 1,050.00 USD | `-37.02%` | `200.00` |
| `Live` | `Long` | `5.29` | 2,070,000.00 USD | 0.00 USD | 161,490.00 USD | `-36.66%` | `30,556.43` |
| `Live` | `Long` | `5.32` | 1,910,000.00 USD | 0.00 USD | 232.85 USD | `-36.30%` | `43.81` |
| `Live` | `Long` | `5.33` | 1,910,000.00 USD | 0.00 USD | 1,230.00 USD | `-36.18%` | `230.53` |
| `Live` | `Long` | `5.39` | 1,910,000.00 USD | 0.00 USD | 660.46 USD | `-35.34%` | `122.42` |
| `Live` | `Long` | `5.42` | 1,910,000.00 USD | 0.00 USD | 20,160.00 USD | `-35.10%` | `3,723.69` |
| `Live` | `Long` | `5.42` | 1,890,000.00 USD | 0.00 USD | 160,400.00 USD | `-34.98%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,730,000.00 USD | 0.00 USD | 1,360.00 USD | `-34.86%` | `250.00` |
| `Live` | `Long` | `5.46` | 1,730,000.00 USD | 0.00 USD | 264.72 USD | `-34.50%` | `48.44` |
| `Live` | `Long` | `5.47` | 1,730,000.00 USD | 0.00 USD | 1,320.00 USD | `-34.38%` | `240.95` |
| `Live` | `Long` | `5.49` | 1,730,000.00 USD | 0.00 USD | 354.06 USD | `-34.26%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,730,000.00 USD | 0.00 USD | 19,290.00 USD | `-34.14%` | `3,510.41` |
| `Live` | `Long` | `5.51` | 1,710,000.00 USD | 0.00 USD | 367.41 USD | `-33.90%` | `66.62` |
| `Live` | `Long` | `5.54` | 1,710,000.00 USD | 0.00 USD | 121.38 USD | `-33.66%` | `21.93` |
| `Live` | `Long` | `5.54` | 1,710,000.00 USD | 0.00 USD | 2,760.00 USD | `-33.54%` | `497.70` |
| `Live` | `Long` | `5.58` | 1,700,000.00 USD | 0.00 USD | 63,260.00 USD | `-33.18%` | `11,347.58` |
| `Live` | `Long` | `5.59` | 1,640,000.00 USD | 0.00 USD | 35,940.00 USD | `-32.94%` | `6,423.60` |
| `Live` | `Long` | `5.63` | 1,600,000.00 USD | 0.00 USD | 468.55 USD | `-32.46%` | `83.15` |
| `Live` | `Long` | `5.64` | 1,600,000.00 USD | 0.00 USD | 229.24 USD | `-32.34%` | `40.61` |
| `Live` | `Long` | `5.72` | 1,600,000.00 USD | 0.00 USD | 2,390.00 USD | `-31.38%` | `417.17` |
| `Live` | `Long` | `5.74` | 1,600,000.00 USD | 0.00 USD | 238.86 USD | `-31.26%` | `41.65` |
| `Live` | `Long` | `5.75` | 1,600,000.00 USD | 0.00 USD | 125.70 USD | `-31.14%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,600,000.00 USD | 0.00 USD | 3,190.00 USD | `-31.02%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,600,000.00 USD | 0.00 USD | 10,850.00 USD | `-30.90%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,590,000.00 USD | 0.00 USD | 801.40 USD | `-30.78%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,590,000.00 USD | 0.00 USD | 2,890.00 USD | `-30.66%` | `500.00` |
| `Live` | `Long` | `5.79` | 1,580,000.00 USD | 0.00 USD | 736.72 USD | `-30.54%` | `127.13` |
| `Live` | `Long` | `5.80` | 1,580,000.00 USD | 0.00 USD | 696.60 USD | `-30.42%` | `120.00` |
| `Live` | `Long` | `5.82` | 1,580,000.00 USD | 0.00 USD | 106.65 USD | `-30.31%` | `18.34` |
| `Live` | `Long` | `5.83` | 1,580,000.00 USD | 0.00 USD | 145.88 USD | `-30.07%` | `25.00` |
| `Live` | `Long` | `5.84` | 1,580,000.00 USD | 0.00 USD | 561.53 USD | `-29.95%` | `96.07` |
| `Live` | `Long` | `5.86` | 1,580,000.00 USD | 0.00 USD | 2,110.00 USD | `-29.83%` | `360.33` |
| `Live` | `Long` | `5.89` | 1,580,000.00 USD | 0.00 USD | 984.70 USD | `-29.35%` | `167.04` |
| `Live` | `Long` | `5.91` | 1,580,000.00 USD | 0.00 USD | 399.18 USD | `-29.23%` | `67.60` |
| `Live` | `Long` | `5.92` | 1,580,000.00 USD | 0.00 USD | 277.35 USD | `-29.11%` | `46.89` |
| `Live` | `Long` | `5.93` | 1,580,000.00 USD | 0.00 USD | 147.19 USD | `-28.87%` | `24.80` |
| `Live` | `Long` | `5.96` | 1,580,000.00 USD | 0.00 USD | 11,720.00 USD | `-28.63%` | `1,968.19` |
| `Live` | `Long` | `5.97` | 1,560,000.00 USD | 0.00 USD | 585.97 USD | `-28.39%` | `98.07` |
| `Live` | `Long` | `5.99` | 1,560,000.00 USD | 0.00 USD | 447.98 USD | `-28.27%` | `74.85` |
| `Live` | `Long` | `6.00` | 1,560,000.00 USD | 0.00 USD | 341.56 USD | `-28.03%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,560,000.00 USD | 0.00 USD | 446.85 USD | `-27.91%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,560,000.00 USD | 0.00 USD | 331.68 USD | `-27.67%` | `54.96` |
| `Live` | `Long` | `6.04` | 1,560,000.00 USD | 0.00 USD | 105.61 USD | `-27.55%` | `17.47` |
| `Live` | `Long` | `6.05` | 1,560,000.00 USD | 0.00 USD | 1,310.00 USD | `-27.43%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,560,000.00 USD | 0.00 USD | 265.10 USD | `-27.31%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,560,000.00 USD | 0.00 USD | 1,690.00 USD | `-27.19%` | `278.94` |
| `Live` | `Long` | `6.08` | 1,560,000.00 USD | 0.00 USD | 405.14 USD | `-27.07%` | `66.58` |
| `Live` | `Long` | `6.09` | 1,560,000.00 USD | 0.00 USD | 3,130.00 USD | `-26.95%` | `512.81` |
| `Live` | `Long` | `6.12` | 1,560,000.00 USD | 0.00 USD | 1,140.00 USD | `-26.71%` | `185.96` |
| `Live` | `Long` | `6.12` | 1,550,000.00 USD | 0.00 USD | 2,160.00 USD | `-26.59%` | `353.02` |
| `Live` | `Long` | `6.14` | 1,550,000.00 USD | 0.00 USD | 238.61 USD | `-26.35%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,550,000.00 USD | 0.00 USD | 4,390.00 USD | `-26.23%` | `713.75` |
| `Live` | `Long` | `6.17` | 1,550,000.00 USD | 0.00 USD | 104.36 USD | `-25.99%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,550,000.00 USD | 0.00 USD | 310.25 USD | `-25.63%` | `50.00` |
| `Live` | `Long` | `6.24` | 1,550,000.00 USD | 0.00 USD | 300.65 USD | `-25.27%` | `48.22` |
| `Live` | `Long` | `6.25` | 1,550,000.00 USD | 0.00 USD | 2,410.00 USD | `-25.15%` | `386.46` |
| `Live` | `Long` | `6.25` | 1,540,000.00 USD | 0.00 USD | 972.65 USD | `-25.03%` | `155.50` |
| `Live` | `Long` | `6.28` | 1,540,000.00 USD | 0.00 USD | 2,510.00 USD | `-24.79%` | `400.00` |
| `Live` | `Long` | `6.32` | 1,540,000.00 USD | 0.00 USD | 277.04 USD | `-24.31%` | `43.87` |
| `Live` | `Long` | `6.36` | 1,540,000.00 USD | 0.00 USD | 4,470.00 USD | `-23.83%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,540,000.00 USD | 0.00 USD | 348,420.00 USD | `-23.71%` | `54,740.07` |
| `Live` | `Long` | `6.38` | 1,190,000.00 USD | 0.00 USD | 11,550.00 USD | `-23.59%` | `1,812.24` |
| `Live` | `Long` | `6.38` | 1,180,000.00 USD | 0.00 USD | 3,830.00 USD | `-23.47%` | `600.00` |
| `Live` | `Long` | `6.42` | 1,170,000.00 USD | 0.00 USD | 306.32 USD | `-23.11%` | `47.75` |
| `Live` | `Long` | `6.42` | 1,170,000.00 USD | 0.00 USD | 1,980.00 USD | `-22.99%` | `307.60` |
| `Live` | `Long` | `6.43` | 1,170,000.00 USD | 0.00 USD | 6,780.00 USD | `-22.87%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 1,160,000.00 USD | 0.00 USD | 2,510.00 USD | `-22.51%` | `387.89` |
| `Live` | `Long` | `6.47` | 1,160,000.00 USD | 0.00 USD | 362,980.00 USD | `-22.39%` | `56,059.40` |
| `Live` | `Long` | `6.54` | 797,990.00 USD | 0.00 USD | 3,620.00 USD | `-21.68%` | `554.55` |
| `Live` | `Long` | `6.54` | 794,360.00 USD | 0.00 USD | 8,970.00 USD | `-21.56%` | `1,370.89` |
| `Live` | `Long` | `6.57` | 785,390.00 USD | 0.00 USD | 1,530.00 USD | `-21.32%` | `233.60` |
| `Live` | `Long` | `6.58` | 783,860.00 USD | 0.00 USD | 537.37 USD | `-21.20%` | `81.73` |
| `Live` | `Long` | `6.58` | 783,320.00 USD | 0.00 USD | 1,770.00 USD | `-21.08%` | `269.14` |
| `Live` | `Long` | `6.59` | 781,550.00 USD | 0.00 USD | 1,100.00 USD | `-20.96%` | `166.55` |
| `Live` | `Long` | `6.62` | 780,450.00 USD | 0.00 USD | 2,110.00 USD | `-20.72%` | `318.57` |
| `Live` | `Long` | `6.62` | 778,340.00 USD | 0.00 USD | 364.90 USD | `-20.60%` | `55.08` |
| `Live` | `Long` | `6.67` | 777,980.00 USD | 0.00 USD | 1,640.00 USD | `-20.00%` | `245.42` |
| `Live` | `Long` | `6.70` | 776,340.00 USD | 0.00 USD | 1,700.00 USD | `-19.76%` | `254.63` |
| `Live` | `Long` | `6.71` | 774,630.00 USD | 0.00 USD | 16,070.00 USD | `-19.64%` | `2,396.06` |
| `Live` | `Long` | `6.71` | 758,570.00 USD | 0.00 USD | 6,180.00 USD | `-19.52%` | `920.74` |
| `Live` | `Long` | `6.75` | 752,390.00 USD | 0.00 USD | 1,330.00 USD | `-19.16%` | `196.95` |
| `Live` | `Long` | `6.78` | 751,060.00 USD | 0.00 USD | 6,780.00 USD | `-18.80%` | `1,000.00` |
| `Live` | `Long` | `6.79` | 744,280.00 USD | 0.00 USD | 16,960.00 USD | `-18.68%` | `2,500.00` |
| `Live` | `Long` | `6.79` | 727,320.00 USD | 0.00 USD | 4,930.00 USD | `-18.56%` | `726.24` |
| `Live` | `Long` | `6.80` | 722,380.00 USD | 0.00 USD | 1,500.00 USD | `-18.44%` | `220.95` |
| `Live` | `Long` | `6.82` | 720,880.00 USD | 0.00 USD | 2,670.00 USD | `-18.32%` | `391.11` |
| `Live` | `Long` | `6.83` | 718,220.00 USD | 0.00 USD | 158.14 USD | `-18.20%` | `23.17` |
| `Live` | `Long` | `6.83` | 718,060.00 USD | 0.00 USD | 4,410.00 USD | `-18.08%` | `644.73` |
| `Live` | `Long` | `6.86` | 713,650.00 USD | 0.00 USD | 19,810.00 USD | `-17.84%` | `2,889.24` |
| `Live` | `Long` | `6.87` | 693,840.00 USD | 0.00 USD | 3,340.00 USD | `-17.72%` | `486.46` |
| `Live` | `Long` | `6.88` | 690,510.00 USD | 0.00 USD | 1,580.00 USD | `-17.48%` | `229.18` |
| `Live` | `Long` | `6.91` | 688,930.00 USD | 0.00 USD | 269.30 USD | `-17.24%` | `39.00` |
| `Live` | `Long` | `6.95` | 688,660.00 USD | 0.00 USD | 3,760.00 USD | `-16.76%` | `541.68` |
| `Live` | `Long` | `6.96` | 684,900.00 USD | 0.00 USD | 3,480.00 USD | `-16.64%` | `500.00` |
| `Live` | `Long` | `6.96` | 681,420.00 USD | 0.00 USD | 636.74 USD | `-16.52%` | `91.42` |
| `Live` | `Long` | `6.97` | 680,780.00 USD | 0.00 USD | 2,810.00 USD | `-16.40%` | `403.02` |
| `Live` | `Long` | `6.99` | 677,970.00 USD | 0.00 USD | 1,100.00 USD | `-16.28%` | `157.09` |
| `Live` | `Long` | `7.00` | 676,870.00 USD | 0.00 USD | 746.58 USD | `-16.16%` | `106.73` |
| `Live` | `Long` | `7.00` | 676,130.00 USD | 0.00 USD | 20,860.00 USD | `-16.04%` | `2,978.11` |
| `Live` | `Long` | `7.01` | 655,270.00 USD | 0.00 USD | 281.86 USD | `-15.92%` | `40.18` |
| `Live` | `Long` | `7.03` | 654,980.00 USD | 0.00 USD | 1,370.00 USD | `-15.80%` | `194.51` |
| `Live` | `Long` | `7.04` | 653,620.00 USD | 0.00 USD | 704.50 USD | `-15.56%` | `100.00` |
| `Live` | `Long` | `7.05` | 652,910.00 USD | 0.00 USD | 354.23 USD | `-15.44%` | `50.21` |
| `Live` | `Long` | `7.07` | 652,560.00 USD | 0.00 USD | 1,260.00 USD | `-15.32%` | `178.91` |
| `Live` | `Long` | `7.08` | 651,290.00 USD | 0.00 USD | 6,700.00 USD | `-15.20%` | `947.44` |
| `Live` | `Long` | `7.08` | 644,590.00 USD | 0.00 USD | 1,420.00 USD | `-15.08%` | `201.02` |
| `Live` | `Long` | `7.09` | 643,170.00 USD | 0.00 USD | 3,020.00 USD | `-14.96%` | `425.89` |
| `Live` | `Long` | `7.11` | 640,150.00 USD | 0.00 USD | 28,230.00 USD | `-14.84%` | `3,972.61` |
| `Live` | `Long` | `7.12` | 611,920.00 USD | 0.00 USD | 379.66 USD | `-14.72%` | `53.36` |
| `Live` | `Long` | `7.13` | 611,540.00 USD | 0.00 USD | 777.50 USD | `-14.48%` | `108.97` |
| `Live` | `Long` | `7.14` | 610,760.00 USD | 0.00 USD | 20,270.00 USD | `-14.36%` | `2,837.00` |
| `Live` | `Long` | `7.16` | 590,490.00 USD | 0.00 USD | 2,370.00 USD | `-14.24%` | `331.12` |
| `Live` | `Long` | `7.17` | 588,120.00 USD | 0.00 USD | 215.59 USD | `-14.12%` | `30.09` |
| `Live` | `Long` | `7.17` | 587,910.00 USD | 0.00 USD | 1,440.00 USD | `-14.00%` | `200.00` |
| `Live` | `Long` | `7.18` | 586,470.00 USD | 0.00 USD | 1,440.00 USD | `-13.89%` | `200.00` |
| `Live` | `Long` | `7.21` | 585,040.00 USD | 0.00 USD | 7,950.00 USD | `-13.65%` | `1,103.97` |
| `Live` | `Long` | `7.21` | 577,080.00 USD | 0.00 USD | 29,440.00 USD | `-13.53%` | `4,080.53` |
| `Live` | `Long` | `7.24` | 547,640.00 USD | 0.00 USD | 179.65 USD | `-13.29%` | `24.83` |
| `Live` | `Long` | `7.25` | 547,460.00 USD | 0.00 USD | 185.83 USD | `-13.17%` | `25.65` |
| `Live` | `Long` | `7.25` | 547,270.00 USD | 0.00 USD | 21,280.00 USD | `-13.05%` | `2,933.17` |
| `Live` | `Long` | `7.26` | 525,990.00 USD | 0.00 USD | 419.41 USD | `-12.93%` | `57.73` |
| `Live` | `Long` | `7.29` | 525,580.00 USD | 0.00 USD | 38,110.00 USD | `-12.69%` | `5,230.97` |
| `Live` | `Long` | `7.33` | 487,470.00 USD | 0.00 USD | 4,910.00 USD | `-12.21%` | `669.93` |
| `Live` | `Long` | `7.34` | 482,560.00 USD | 0.00 USD | 4,370.00 USD | `-11.97%` | `594.84` |
| `Live` | `Long` | `7.37` | 478,190.00 USD | 0.00 USD | 6,420.00 USD | `-11.73%` | `871.98` |
| `Live` | `Long` | `7.38` | 471,770.00 USD | 0.00 USD | 5,020.00 USD | `-11.61%` | `680.40` |
| `Live` | `Long` | `7.38` | 466,750.00 USD | 0.00 USD | 13,200.00 USD | `-11.49%` | `1,787.05` |
| `Live` | `Long` | `7.39` | 453,550.00 USD | 0.00 USD | 1,550.00 USD | `-11.37%` | `210.17` |
| `Live` | `Long` | `7.42` | 452,000.00 USD | 0.00 USD | 338.94 USD | `-11.13%` | `45.71` |
| `Live` | `Long` | `7.42` | 451,660.00 USD | 0.00 USD | 147.61 USD | `-11.01%` | `19.88` |
| `Live` | `Long` | `7.43` | 451,510.00 USD | 0.00 USD | 2,880.00 USD | `-10.89%` | `387.61` |
| `Live` | `Long` | `7.45` | 448,630.00 USD | 0.00 USD | 210.99 USD | `-10.77%` | `28.34` |
| `Live` | `Long` | `7.46` | 448,420.00 USD | 0.00 USD | 1,620.00 USD | `-10.65%` | `217.70` |
| `Live` | `Long` | `7.46` | 446,800.00 USD | 0.00 USD | 4,590.00 USD | `-10.53%` | `614.36` |
| `Live` | `Long` | `7.47` | 442,210.00 USD | 0.00 USD | 1,120.00 USD | `-10.41%` | `149.52` |
| `Live` | `Long` | `7.49` | 441,090.00 USD | 0.00 USD | 1,050.00 USD | `-10.29%` | `140.00` |
| `Live` | `Long` | `7.50` | 440,050.00 USD | 0.00 USD | 962.81 USD | `-10.17%` | `128.46` |
| `Live` | `Long` | `7.50` | 439,080.00 USD | 0.00 USD | 421.78 USD | `-10.05%` | `56.20` |
| `Live` | `Long` | `7.54` | 438,660.00 USD | 0.00 USD | 4,210.00 USD | `-9.69%` | `559.01` |
| `Live` | `Long` | `7.54` | 434,450.00 USD | 0.00 USD | 1,510.00 USD | `-9.57%` | `200.00` |
| `Live` | `Long` | `7.55` | 432,940.00 USD | 0.00 USD | 572.67 USD | `-9.45%` | `75.80` |
| `Live` | `Long` | `7.57` | 432,370.00 USD | 0.00 USD | 25,060.00 USD | `-9.33%` | `3,312.23` |
| `Live` | `Long` | `7.58` | 407,310.00 USD | 0.00 USD | 118.25 USD | `-9.21%` | `15.61` |
| `Live` | `Long` | `7.59` | 407,190.00 USD | 0.00 USD | 24,760.00 USD | `-8.97%` | `3,260.14` |
| `Live` | `Long` | `7.61` | 382,430.00 USD | 0.00 USD | 1,520.00 USD | `-8.85%` | `199.85` |
| `Live` | `Long` | `7.62` | 380,910.00 USD | 0.00 USD | 878.24 USD | `-8.73%` | `115.33` |
| `Live` | `Long` | `7.62` | 380,030.00 USD | 0.00 USD | 787.51 USD | `-8.61%` | `103.28` |
| `Live` | `Long` | `7.63` | 379,250.00 USD | 0.00 USD | 378.93 USD | `-8.49%` | `49.63` |
| `Live` | `Long` | `7.66` | 378,870.00 USD | 0.00 USD | 1,410.00 USD | `-8.25%` | `184.81` |
| `Live` | `Long` | `7.67` | 377,450.00 USD | 0.00 USD | 1,740.00 USD | `-8.13%` | `226.45` |
| `Live` | `Long` | `7.67` | 375,720.00 USD | 0.00 USD | 1,890.00 USD | `-8.01%` | `246.71` |
| `Live` | `Long` | `7.68` | 373,820.00 USD | 0.00 USD | 1,120.00 USD | `-7.89%` | `145.25` |
| `Live` | `Long` | `7.70` | 372,710.00 USD | 0.00 USD | 1,460.00 USD | `-7.77%` | `190.36` |
| `Live` | `Long` | `7.76` | 371,240.00 USD | 0.00 USD | 455.73 USD | `-6.93%` | `58.69` |
| `Live` | `Long` | `7.78` | 370,790.00 USD | 0.00 USD | 695.32 USD | `-6.81%` | `89.43` |
| `Live` | `Long` | `7.79` | 370,090.00 USD | 0.00 USD | 2,870.00 USD | `-6.69%` | `368.38` |
| `Live` | `Long` | `7.79` | 367,220.00 USD | 0.00 USD | 12,800.00 USD | `-6.57%` | `1,642.37` |
| `Live` | `Long` | `7.82` | 354,420.00 USD | 0.00 USD | 3,130.00 USD | `-6.33%` | `400.00` |
| `Live` | `Long` | `7.84` | 351,290.00 USD | 0.00 USD | 24,340.00 USD | `-5.97%` | `3,102.56` |
| `Live` | `Long` | `7.88` | 326,950.00 USD | 0.00 USD | 555.19 USD | `-5.62%` | `70.50` |
| `Live` | `Long` | `7.91` | 326,400.00 USD | 0.00 USD | 505.13 USD | `-5.26%` | `63.90` |
| `Live` | `Long` | `7.93` | 325,890.00 USD | 0.00 USD | 16,340.00 USD | `-4.90%` | `2,059.56` |
| `Live` | `Long` | `7.95` | 309,550.00 USD | 0.00 USD | 127,110.00 USD | `-4.78%` | `15,999.24` |
| `Live` | `Long` | `7.96` | 182,440.00 USD | 0.00 USD | 4,090.00 USD | `-4.66%` | `514.43` |
| `Live` | `Long` | `7.96` | 178,350.00 USD | 0.00 USD | 4,520.00 USD | `-4.54%` | `567.62` |
| `Live` | `Long` | `7.97` | 173,820.00 USD | 0.00 USD | 10,990.00 USD | `-4.42%` | `1,377.56` |
| `Live` | `Long` | `7.99` | 162,840.00 USD | 0.00 USD | 17,430.00 USD | `-4.30%` | `2,182.57` |
| `Live` | `Long` | `8.00` | 145,410.00 USD | 0.00 USD | 2,740.00 USD | `-4.18%` | `342.47` |
| `Live` | `Long` | `8.01` | 142,670.00 USD | 0.00 USD | 284.42 USD | `-4.06%` | `35.53` |
| `Live` | `Long` | `8.02` | 142,390.00 USD | 0.00 USD | 235.80 USD | `-3.94%` | `29.42` |
| `Live` | `Long` | `8.03` | 142,150.00 USD | 0.00 USD | 957.70 USD | `-3.82%` | `119.34` |
| `Live` | `Long` | `8.04` | 141,190.00 USD | 0.00 USD | 89,210.00 USD | `-3.70%` | `11,102.89` |
| `Live` | `Long` | `8.04` | 51,980.00 USD | 0.00 USD | 10,430.00 USD | `-3.58%` | `1,296.59` |
| `Live` | `Long` | `8.05` | 41,550.00 USD | 0.00 USD | 1,370.00 USD | `-3.46%` | `169.50` |
| `Live` | `Long` | `8.06` | 40,190.00 USD | 0.00 USD | 4,380.00 USD | `-3.34%` | `543.69` |
| `Live` | `Long` | `8.07` | 35,800.00 USD | 0.00 USD | 232.96 USD | `-3.22%` | `28.85` |
| `Live` | `Long` | `8.09` | 35,570.00 USD | 0.00 USD | 3,420.00 USD | `-3.10%` | `422.54` |
| `Live` | `Long` | `8.10` | 32,150.00 USD | 0.00 USD | 886.24 USD | `-2.98%` | `109.48` |
| `Live` | `Long` | `8.11` | 31,270.00 USD | 0.00 USD | 6,000.00 USD | `-2.86%` | `739.81` |
| `Live` | `Long` | `8.12` | 25,270.00 USD | 0.00 USD | 241.26 USD | `-2.74%` | `29.73` |
| `Live` | `Long` | `8.12` | 25,030.00 USD | 0.00 USD | 843.86 USD | `-2.62%` | `103.86` |
| `Live` | `Long` | `8.13` | 24,190.00 USD | 0.00 USD | 855.64 USD | `-2.50%` | `105.18` |
| `Live` | `Long` | `8.16` | 23,330.00 USD | 0.00 USD | 871.61 USD | `-2.14%` | `106.75` |
| `Live` | `Long` | `8.20` | 22,460.00 USD | 0.00 USD | 8,590.00 USD | `-1.78%` | `1,048.60` |
| `Live` | `Long` | `8.21` | 13,860.00 USD | 0.00 USD | 1,910.00 USD | `-1.66%` | `232.19` |
| `Live` | `Long` | `8.21` | 11,960.00 USD | 0.00 USD | 147.87 USD | `-1.54%` | `18.00` |
| `Live` | `Long` | `8.22` | 11,810.00 USD | 0.00 USD | 2,100.00 USD | `-1.42%` | `255.16` |
| `Live` | `Long` | `8.26` | 9,710.00 USD | 0.00 USD | 9,710.00 USD | `-1.06%` | `1,176.61` |
| `Live` | `Short` | `8.60` | 2,350.00 USD | 2,350.00 USD | 0.00 USD | `+3.01%` | `273.42` |
| `Live` | `Short` | `8.76` | 2,720.00 USD | 373.93 USD | 0.00 USD | `+4.93%` | `42.71` |
| `Live` | `Short` | `8.78` | 3,960.00 USD | 1,230.00 USD | 0.00 USD | `+5.17%` | `140.62` |
| `Live` | `Short` | `8.82` | 9,960.00 USD | 6,000.00 USD | 0.00 USD | `+5.77%` | `680.16` |
| `Live` | `Short` | `8.84` | 10,500.00 USD | 541.67 USD | 0.00 USD | `+5.89%` | `61.31` |
| `Live` | `Short` | `9.06` | 10,940.00 USD | 434.94 USD | 0.00 USD | `+8.65%` | `47.98` |
| `Live` | `Short` | `9.19` | 12,530.00 USD | 1,590.00 USD | 0.00 USD | `+10.09%` | `173.30` |
| `Live` | `Short` | `9.21` | 14,400.00 USD | 1,870.00 USD | 0.00 USD | `+10.45%` | `202.76` |
| `Live` | `Short` | `9.29` | 14,500.00 USD | 100.93 USD | 0.00 USD | `+11.28%` | `10.87` |
| `Live` | `Short` | `9.40` | 42,710.00 USD | 28,220.00 USD | 0.00 USD | `+12.72%` | `3,000.00` |
| `Live` | `Short` | `9.41` | 43,150.00 USD | 440.06 USD | 0.00 USD | `+12.84%` | `46.74` |
| `Live` | `Short` | `9.62` | 43,410.00 USD | 253.04 USD | 0.00 USD | `+15.36%` | `26.29` |
| `Live` | `Short` | `9.64` | 45,340.00 USD | 1,930.00 USD | 0.00 USD | `+15.60%` | `200.61` |
| `Live` | `Short` | `9.70` | 46,270.00 USD | 929.65 USD | 0.00 USD | `+16.20%` | `95.89` |
| `Live` | `Short` | `9.73` | 46,460.00 USD | 192.95 USD | 0.00 USD | `+16.68%` | `19.82` |
| `Live` | `Short` | `10.11` | 47,030.00 USD | 568.81 USD | 0.00 USD | `+21.11%` | `56.29` |
| `Live` | `Short` | `10.12` | 47,520.00 USD | 487.01 USD | 0.00 USD | `+21.35%` | `48.10` |
| `Live` | `Short` | `10.18` | 297,110.00 USD | 249,590.00 USD | 0.00 USD | `+21.95%` | `24,529.43` |
| `Live` | `Short` | `10.21` | 300,340.00 USD | 3,230.00 USD | 0.00 USD | `+22.43%` | `316.22` |
| `Live` | `Short` | `10.32` | 558,470.00 USD | 258,130.00 USD | 0.00 USD | `+23.75%` | `25,000.94` |
| `Live` | `Short` | `10.35` | 561,130.00 USD | 2,650.00 USD | 0.00 USD | `+23.99%` | `256.58` |
| `Live` | `Short` | `10.56` | 561,650.00 USD | 523.81 USD | 0.00 USD | `+26.63%` | `49.58` |
| `Live` | `Short` | `10.71` | 561,870.00 USD | 218.91 USD | 0.00 USD | `+28.42%` | `20.43` |
| `Live` | `Short` | `10.93` | 561,990.00 USD | 117.23 USD | 0.00 USD | `+30.94%` | `10.73` |
| `Live` | `Short` | `10.96` | 563,900.00 USD | 1,920.00 USD | 0.00 USD | `+31.42%` | `174.67` |
| `Live` | `Short` | `11.01` | 570,870.00 USD | 6,970.00 USD | 0.00 USD | `+31.90%` | `633.00` |
| `Live` | `Short` | `11.22` | 683,120.00 USD | 112,250.00 USD | 0.00 USD | `+34.54%` | `10,000.00` |
| `Live` | `Short` | `11.27` | 694,790.00 USD | 11,670.00 USD | 0.00 USD | `+35.02%` | `1,035.87` |
| `Live` | `Short` | `11.62` | 706,920.00 USD | 12,140.00 USD | 0.00 USD | `+39.33%` | `1,043.90` |
| `Live` | `Short` | `11.69` | 1,000,000.00 USD | 296,760.00 USD | 0.00 USD | `+40.05%` | `25,397.02` |
| `Live` | `Short` | `11.74` | 1,040,000.00 USD | 40,670.00 USD | 0.00 USD | `+40.77%` | `3,462.73` |
| `Live` | `Short` | `11.93` | 1,040,000.00 USD | 505.74 USD | 0.00 USD | `+42.93%` | `42.41` |
| `Live` | `Short` | `11.95` | 1,050,000.00 USD | 1,050.00 USD | 0.00 USD | `+43.17%` | `87.54` |
| `Live` | `Short` | `11.96` | 1,110,000.00 USD | 59,780.00 USD | 0.00 USD | `+43.29%` | `5,000.00` |
| `Live` | `Short` | `12.04` | 1,110,000.00 USD | 802.20 USD | 0.00 USD | `+44.36%` | `66.60` |
| `Live` | `Short` | `12.30` | 1,110,000.00 USD | 1,730.00 USD | 0.00 USD | `+47.48%` | `140.71` |
| `Live` | `Short` | `12.40` | 1,110,000.00 USD | 343.62 USD | 0.00 USD | `+48.68%` | `27.70` |
| `Live` | `Short` | `13.04` | 1,110,000.00 USD | 444.49 USD | 0.00 USD | `+56.23%` | `34.10` |
| `Live` | `Short` | `13.20` | 1,200,000.00 USD | 87,940.00 USD | 0.00 USD | `+58.15%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 1,200,000.00 USD | 3,810.00 USD | 0.00 USD | `+59.35%` | `286.56` |
| `Live` | `Short` | `13.46` | 1,200,000.00 USD | 430.34 USD | 0.00 USD | `+61.38%` | `31.96` |
| `Live` | `Short` | `13.69` | 1,200,000.00 USD | 172.29 USD | 0.00 USD | `+64.02%` | `12.59` |
| `Live` | `Short` | `14.18` | 1,240,000.00 USD | 40,820.00 USD | 0.00 USD | `+69.89%` | `2,879.71` |
| `Live` | `Short` | `14.31` | 1,240,000.00 USD | 282.43 USD | 0.00 USD | `+71.57%` | `19.73` |
| `Live` | `Short` | `14.45` | 1,240,000.00 USD | 237.04 USD | 0.00 USD | `+73.13%` | `16.41` |
| `Live` | `Short` | `14.46` | 1,260,000.00 USD | 16,190.00 USD | 0.00 USD | `+73.25%` | `1,120.14` |
| `Live` | `Short` | `14.66` | 1,260,000.00 USD | 823.29 USD | 0.00 USD | `+75.77%` | `56.14` |
| `Live` | `Short` | `14.71` | 1,260,000.00 USD | 5,160.00 USD | 0.00 USD | `+76.24%` | `350.86` |
| `Live` | `Short` | `14.77` | 1,270,000.00 USD | 4,100.00 USD | 0.00 USD | `+76.96%` | `277.54` |
| `Live` | `Short` | `14.90` | 1,270,000.00 USD | 321.20 USD | 0.00 USD | `+78.64%` | `21.55` |
| `Live` | `Short` | `15.27` | 1,270,000.00 USD | 2,540.00 USD | 0.00 USD | `+82.96%` | `166.16` |
| `Live` | `Short` | `15.29` | 1,270,000.00 USD | 229.43 USD | 0.00 USD | `+83.32%` | `15.00` |
| `Live` | `Short` | `15.35` | 1,270,000.00 USD | 484.60 USD | 0.00 USD | `+83.92%` | `31.58` |
| `Live` | `Short` | `15.38` | 1,290,000.00 USD | 20,000.00 USD | 0.00 USD | `+84.40%` | `1,300.00` |
| `Live` | `Short` | `15.64` | 1,300,000.00 USD | 9,180.00 USD | 0.00 USD | `+87.51%` | `587.04` |
| `Live` | `Short` | `16.32` | 1,320,000.00 USD | 22,420.00 USD | 0.00 USD | `+95.54%` | `1,373.91` |
| `Live` | `Short` | `16.32` | 1,320,000.00 USD | 116.07 USD | 0.00 USD | `+95.66%` | `7.11` |
| `Live` | `Short` | `16.38` | 1,590,000.00 USD | 265,410.00 USD | 0.00 USD | `+96.26%` | `16,208.00` |
| `Live` | `Short` | `16.52` | 1,590,000.00 USD | 190.91 USD | 0.00 USD | `+97.94%` | `11.56` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 269,620.00 USD | 0.00 USD | 611.73 USD | `-72.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 269,010.00 USD | 0.00 USD | 793.75 USD | `-52.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.49` | 268,220.00 USD | 0.00 USD | 105.04 USD | `-46.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 268,110.00 USD | 0.00 USD | 67,970.00 USD | `-40.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 200,140.00 USD | 0.00 USD | 205.30 USD | `-36.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 199,940.00 USD | 0.00 USD | 465.42 USD | `-34.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 199,470.00 USD | 0.00 USD | 349.35 USD | `-34.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.54` | 199,120.00 USD | 0.00 USD | 1,020.00 USD | `-33.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 198,110.00 USD | 0.00 USD | 1,330.00 USD | `-30.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 196,780.00 USD | 0.00 USD | 493.50 USD | `-28.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 196,290.00 USD | 0.00 USD | 100.98 USD | `-28.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 196,180.00 USD | 0.00 USD | 500.70 USD | `-28.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 195,680.00 USD | 0.00 USD | 4,160.00 USD | `-26.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 191,530.00 USD | 0.00 USD | 6,500.00 USD | `-25.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 185,030.00 USD | 0.00 USD | 864.38 USD | `-24.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 184,160.00 USD | 0.00 USD | 1,760.00 USD | `-22.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 182,410.00 USD | 0.00 USD | 4,340.00 USD | `-21.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 178,070.00 USD | 0.00 USD | 5,520.00 USD | `-19.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 172,540.00 USD | 0.00 USD | 100.72 USD | `-19.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 172,440.00 USD | 0.00 USD | 296.34 USD | `-19.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 172,150.00 USD | 0.00 USD | 921.19 USD | `-18.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 171,220.00 USD | 0.00 USD | 709.98 USD | `-17.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.92` | 170,510.00 USD | 0.00 USD | 691.50 USD | `-17.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 169,820.00 USD | 0.00 USD | 262.44 USD | `-16.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 169,560.00 USD | 0.00 USD | 22,830.00 USD | `-16.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 146,730.00 USD | 0.00 USD | 6,790.00 USD | `-14.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 139,940.00 USD | 0.00 USD | 9,770.00 USD | `-14.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 130,170.00 USD | 0.00 USD | 103.46 USD | `-13.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 130,070.00 USD | 0.00 USD | 603.44 USD | `-13.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 129,460.00 USD | 0.00 USD | 891.57 USD | `-13.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 128,570.00 USD | 0.00 USD | 2,090.00 USD | `-12.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 126,480.00 USD | 0.00 USD | 129.58 USD | `-12.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 126,350.00 USD | 0.00 USD | 114.65 USD | `-12.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.39` | 126,230.00 USD | 0.00 USD | 702.75 USD | `-11.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 125,530.00 USD | 0.00 USD | 199.39 USD | `-10.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 125,330.00 USD | 0.00 USD | 6,270.00 USD | `-10.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 119,070.00 USD | 0.00 USD | 37,420.00 USD | `-10.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 81,640.00 USD | 0.00 USD | 2,120.00 USD | `-10.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 79,520.00 USD | 0.00 USD | 799.83 USD | `-9.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.54` | 78,720.00 USD | 0.00 USD | 820.44 USD | `-9.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.57` | 77,900.00 USD | 0.00 USD | 103.41 USD | `-9.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 77,800.00 USD | 0.00 USD | 1,370.00 USD | `-9.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.62` | 76,420.00 USD | 0.00 USD | 915.17 USD | `-8.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 75,510.00 USD | 0.00 USD | 360.13 USD | `-7.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 75,150.00 USD | 0.00 USD | 578.04 USD | `-7.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 74,570.00 USD | 0.00 USD | 175.42 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 74,390.00 USD | 0.00 USD | 3,390.00 USD | `-6.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 71,010.00 USD | 0.00 USD | 143.51 USD | `-5.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 70,860.00 USD | 0.00 USD | 183.33 USD | `-5.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.88` | 70,680.00 USD | 0.00 USD | 194.52 USD | `-5.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 70,490.00 USD | 0.00 USD | 394.75 USD | `-5.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 70,090.00 USD | 0.00 USD | 2,050.00 USD | `-5.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 68,050.00 USD | 0.00 USD | 5,710.00 USD | `-5.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 62,340.00 USD | 0.00 USD | 1,590.00 USD | `-5.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 60,750.00 USD | 0.00 USD | 898.42 USD | `-4.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.99` | 59,850.00 USD | 0.00 USD | 3,990.00 USD | `-4.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 55,860.00 USD | 0.00 USD | 1,350.00 USD | `-4.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 54,510.00 USD | 0.00 USD | 9,650.00 USD | `-4.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 44,860.00 USD | 0.00 USD | 123.58 USD | `-3.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 44,740.00 USD | 0.00 USD | 2,110.00 USD | `-3.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 42,630.00 USD | 0.00 USD | 563.85 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 42,070.00 USD | 0.00 USD | 121.69 USD | `-3.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 41,950.00 USD | 0.00 USD | 477.36 USD | `-2.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 41,470.00 USD | 0.00 USD | 924.78 USD | `-2.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 40,540.00 USD | 0.00 USD | 329.06 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 40,210.00 USD | 0.00 USD | 6,500.00 USD | `-2.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 33,710.00 USD | 0.00 USD | 968.39 USD | `-2.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 32,750.00 USD | 0.00 USD | 654.53 USD | `-2.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 32,090.00 USD | 0.00 USD | 1,430.00 USD | `-2.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 30,660.00 USD | 0.00 USD | 3,080.00 USD | `-2.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 27,570.00 USD | 0.00 USD | 520.75 USD | `-2.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 27,050.00 USD | 0.00 USD | 3,020.00 USD | `-1.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 24,030.00 USD | 0.00 USD | 141.04 USD | `-1.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 23,890.00 USD | 0.00 USD | 3,840.00 USD | `-1.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 20,050.00 USD | 0.00 USD | 515.66 USD | `-1.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 19,540.00 USD | 0.00 USD | 629.15 USD | `-1.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.24` | 18,910.00 USD | 0.00 USD | 3,510.00 USD | `-1.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.26` | 15,400.00 USD | 0.00 USD | 9,110.00 USD | `-1.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.27` | 6,280.00 USD | 0.00 USD | 353.00 USD | `-0.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 5,930.00 USD | 0.00 USD | 168.64 USD | `-0.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 5,760.00 USD | 0.00 USD | 201.49 USD | `-0.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 5,560.00 USD | 0.00 USD | 397.99 USD | `-0.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 5,160.00 USD | 0.00 USD | 242.42 USD | `-0.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 4,920.00 USD | 0.00 USD | 2,920.00 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 2,000.00 USD | 0.00 USD | 2,000.00 USD | `-0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.35` | 756.06 USD | 756.06 USD | 0.00 USD | `+0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.36` | 1,730.00 USD | 970.35 USD | 0.00 USD | `+0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 2,150.00 USD | 419.25 USD | 0.00 USD | `+0.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.39` | 4,110.00 USD | 1,970.00 USD | 0.00 USD | `+0.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.40` | 7,060.00 USD | 2,950.00 USD | 0.00 USD | `+0.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.41` | 7,420.00 USD | 358.56 USD | 0.00 USD | `+0.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.43` | 9,300.00 USD | 1,880.00 USD | 0.00 USD | `+0.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.44` | 9,820.00 USD | 517.15 USD | 0.00 USD | `+1.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.45` | 9,960.00 USD | 138.24 USD | 0.00 USD | `+1.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.46` | 10,910.00 USD | 954.23 USD | 0.00 USD | `+1.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.47` | 11,680.00 USD | 769.61 USD | 0.00 USD | `+1.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.48` | 12,170.00 USD | 489.58 USD | 0.00 USD | `+1.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.51` | 13,620.00 USD | 1,440.00 USD | 0.00 USD | `+1.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.52` | 14,030.00 USD | 408.55 USD | 0.00 USD | `+2.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.53` | 15,150.00 USD | 1,130.00 USD | 0.00 USD | `+2.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 15,660.00 USD | 510.39 USD | 0.00 USD | `+2.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 20,070.00 USD | 4,400.00 USD | 0.00 USD | `+2.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.55` | 20,310.00 USD | 243.82 USD | 0.00 USD | `+2.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.56` | 21,810.00 USD | 1,500.00 USD | 0.00 USD | `+2.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.57` | 22,240.00 USD | 428.58 USD | 0.00 USD | `+2.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.59` | 24,740.00 USD | 2,500.00 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.60` | 25,870.00 USD | 1,130.00 USD | 0.00 USD | `+3.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 26,940.00 USD | 1,080.00 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 28,440.00 USD | 1,490.00 USD | 0.00 USD | `+3.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 31,180.00 USD | 2,740.00 USD | 0.00 USD | `+3.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.63` | 31,380.00 USD | 201.97 USD | 0.00 USD | `+3.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.64` | 31,490.00 USD | 103.31 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 33,390.00 USD | 1,900.00 USD | 0.00 USD | `+3.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 33,700.00 USD | 307.87 USD | 0.00 USD | `+3.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.68` | 33,920.00 USD | 223.82 USD | 0.00 USD | `+3.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.69` | 34,910.00 USD | 990.09 USD | 0.00 USD | `+4.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.70` | 39,920.00 USD | 5,010.00 USD | 0.00 USD | `+4.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 40,230.00 USD | 309.29 USD | 0.00 USD | `+4.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 40,370.00 USD | 134.30 USD | 0.00 USD | `+4.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.72` | 41,190.00 USD | 819.28 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.73` | 41,520.00 USD | 333.07 USD | 0.00 USD | `+4.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.74` | 45,890.00 USD | 4,370.00 USD | 0.00 USD | `+4.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.76` | 52,190.00 USD | 6,300.00 USD | 0.00 USD | `+4.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.77` | 92,000.00 USD | 39,810.00 USD | 0.00 USD | `+5.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.78` | 92,210.00 USD | 215.16 USD | 0.00 USD | `+5.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 92,600.00 USD | 388.12 USD | 0.00 USD | `+5.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 93,310.00 USD | 711.78 USD | 0.00 USD | `+5.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 119,730.00 USD | 26,410.00 USD | 0.00 USD | `+5.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.81` | 120,430.00 USD | 705.20 USD | 0.00 USD | `+5.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.82` | 122,470.00 USD | 2,030.00 USD | 0.00 USD | `+5.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.84` | 122,710.00 USD | 243.40 USD | 0.00 USD | `+5.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 128,470.00 USD | 5,760.00 USD | 0.00 USD | `+6.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 128,590.00 USD | 110.33 USD | 0.00 USD | `+6.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 129,200.00 USD | 614.88 USD | 0.00 USD | `+6.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 129,310.00 USD | 110.58 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 130,410.00 USD | 1,100.00 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 130,600.00 USD | 188.66 USD | 0.00 USD | `+6.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 131,390.00 USD | 788.72 USD | 0.00 USD | `+6.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 133,330.00 USD | 1,940.00 USD | 0.00 USD | `+6.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 133,490.00 USD | 163.33 USD | 0.00 USD | `+6.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 134,280.00 USD | 782.17 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 134,500.00 USD | 223.62 USD | 0.00 USD | `+7.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 134,680.00 USD | 180.53 USD | 0.00 USD | `+7.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 135,080.00 USD | 401.63 USD | 0.00 USD | `+7.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 450,230.00 USD | 315,150.00 USD | 0.00 USD | `+7.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.98` | 450,340.00 USD | 104.59 USD | 0.00 USD | `+7.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 450,600.00 USD | 262.56 USD | 0.00 USD | `+7.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 450,730.00 USD | 130.03 USD | 0.00 USD | `+7.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 452,110.00 USD | 1,380.00 USD | 0.00 USD | `+8.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 453,200.00 USD | 1,090.00 USD | 0.00 USD | `+8.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 453,810.00 USD | 616.37 USD | 0.00 USD | `+8.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 453,910.00 USD | 102.03 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 454,370.00 USD | 453.84 USD | 0.00 USD | `+8.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 454,530.00 USD | 160.99 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 454,940.00 USD | 415.00 USD | 0.00 USD | `+8.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 456,450.00 USD | 1,510.00 USD | 0.00 USD | `+8.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 457,070.00 USD | 619.64 USD | 0.00 USD | `+9.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 684,710.00 USD | 227,630.00 USD | 0.00 USD | `+9.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 689,260.00 USD | 4,560.00 USD | 0.00 USD | `+9.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 691,260.00 USD | 2,000.00 USD | 0.00 USD | `+9.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 1,090,000.00 USD | 394,210.00 USD | 0.00 USD | `+9.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,090,000.00 USD | 119.24 USD | 0.00 USD | `+9.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.20` | 1,090,000.00 USD | 1,590.00 USD | 0.00 USD | `+10.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,090,000.00 USD | 2,660.00 USD | 0.00 USD | `+10.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,090,000.00 USD | 131.87 USD | 0.00 USD | `+10.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,090,000.00 USD | 687.91 USD | 0.00 USD | `+10.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,090,000.00 USD | 954.71 USD | 0.00 USD | `+10.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,320,000.00 USD | 231,380.00 USD | 0.00 USD | `+10.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.27` | 1,320,000.00 USD | 205.87 USD | 0.00 USD | `+11.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,330,000.00 USD | 1,960.00 USD | 0.00 USD | `+11.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,330,000.00 USD | 434.45 USD | 0.00 USD | `+11.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,340,000.00 USD | 18,610.00 USD | 0.00 USD | `+11.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,340,000.00 USD | 166.83 USD | 0.00 USD | `+11.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,350,000.00 USD | 2,180.00 USD | 0.00 USD | `+11.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,350,000.00 USD | 579.86 USD | 0.00 USD | `+12.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,350,000.00 USD | 109.36 USD | 0.00 USD | `+12.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,350,000.00 USD | 116.69 USD | 0.00 USD | `+12.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,350,000.00 USD | 163.41 USD | 0.00 USD | `+12.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,350,000.00 USD | 1,150.00 USD | 0.00 USD | `+12.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,350,000.00 USD | 660.84 USD | 0.00 USD | `+12.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,350,000.00 USD | 820.59 USD | 0.00 USD | `+12.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,350,000.00 USD | 928.13 USD | 0.00 USD | `+12.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.43` | 1,350,000.00 USD | 102.45 USD | 0.00 USD | `+12.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,350,000.00 USD | 219.84 USD | 0.00 USD | `+13.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.45` | 1,350,000.00 USD | 140.35 USD | 0.00 USD | `+13.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,350,000.00 USD | 1,890.00 USD | 0.00 USD | `+13.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.47` | 1,360,000.00 USD | 1,780.00 USD | 0.00 USD | `+13.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,360,000.00 USD | 2,210.00 USD | 0.00 USD | `+13.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,360,000.00 USD | 288.46 USD | 0.00 USD | `+13.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.51` | 1,360,000.00 USD | 1,600.00 USD | 0.00 USD | `+13.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,360,000.00 USD | 223.46 USD | 0.00 USD | `+14.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,360,000.00 USD | 231.00 USD | 0.00 USD | `+14.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,360,000.00 USD | 221.07 USD | 0.00 USD | `+15.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,360,000.00 USD | 1,470.00 USD | 0.00 USD | `+15.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,360,000.00 USD | 148.48 USD | 0.00 USD | `+15.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,360,000.00 USD | 191.36 USD | 0.00 USD | `+15.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,360,000.00 USD | 446.58 USD | 0.00 USD | `+16.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,360,000.00 USD | 108.21 USD | 0.00 USD | `+16.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,360,000.00 USD | 169.68 USD | 0.00 USD | `+16.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.74` | 1,360,000.00 USD | 574.66 USD | 0.00 USD | `+16.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,360,000.00 USD | 121.87 USD | 0.00 USD | `+17.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.80` | 1,360,000.00 USD | 619.28 USD | 0.00 USD | `+17.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,370,000.00 USD | 5,030.00 USD | 0.00 USD | `+18.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,370,000.00 USD | 340.05 USD | 0.00 USD | `+18.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,370,000.00 USD | 742.12 USD | 0.00 USD | `+18.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,370,000.00 USD | 899.47 USD | 0.00 USD | `+18.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,440,000.00 USD | 70,020.00 USD | 0.00 USD | `+18.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,440,000.00 USD | 373.97 USD | 0.00 USD | `+18.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,450,000.00 USD | 5,050.00 USD | 0.00 USD | `+19.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,450,000.00 USD | 6,370.00 USD | 0.00 USD | `+20.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,450,000.00 USD | 202.10 USD | 0.00 USD | `+21.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,660,000.00 USD | 210,980.00 USD | 0.00 USD | `+21.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,670,000.00 USD | 1,150.00 USD | 0.00 USD | `+21.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 1,670,000.00 USD | 172.16 USD | 0.00 USD | `+22.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 1,670,000.00 USD | 895.21 USD | 0.00 USD | `+23.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 1,670,000.00 USD | 489.40 USD | 0.00 USD | `+23.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 1,670,000.00 USD | 1,200.00 USD | 0.00 USD | `+24.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 1,670,000.00 USD | 118.01 USD | 0.00 USD | `+24.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 1,670,000.00 USD | 312.31 USD | 0.00 USD | `+25.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 1,670,000.00 USD | 2,290.00 USD | 0.00 USD | `+26.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 1,670,000.00 USD | 178.46 USD | 0.00 USD | `+26.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.62` | 1,670,000.00 USD | 153.11 USD | 0.00 USD | `+27.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 1,670,000.00 USD | 173.42 USD | 0.00 USD | `+28.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 1,670,000.00 USD | 184.75 USD | 0.00 USD | `+28.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 1,670,000.00 USD | 135.78 USD | 0.00 USD | `+29.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 1,670,000.00 USD | 127.96 USD | 0.00 USD | `+29.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 1,670,000.00 USD | 476.43 USD | 0.00 USD | `+30.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 1,670,000.00 USD | 869.35 USD | 0.00 USD | `+30.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 1,670,000.00 USD | 118.97 USD | 0.00 USD | `+30.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 1,670,000.00 USD | 251.06 USD | 0.00 USD | `+30.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 1,670,000.00 USD | 552.44 USD | 0.00 USD | `+31.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 1,670,000.00 USD | 537.26 USD | 0.00 USD | `+31.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 1,670,000.00 USD | 320.29 USD | 0.00 USD | `+33.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 1,680,000.00 USD | 1,100.00 USD | 0.00 USD | `+33.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 1,680,000.00 USD | 2,610.00 USD | 0.00 USD | `+34.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 1,680,000.00 USD | 1,270.00 USD | 0.00 USD | `+34.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 1,680,000.00 USD | 1,380.00 USD | 0.00 USD | `+36.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 1,680,000.00 USD | 2,410.00 USD | 0.00 USD | `+36.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 1,690,000.00 USD | 9,520.00 USD | 0.00 USD | `+37.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.48` | 1,700,000.00 USD | 3,250.00 USD | 0.00 USD | `+37.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 1,700,000.00 USD | 529.11 USD | 0.00 USD | `+37.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 1,700,000.00 USD | 7,700.00 USD | 0.00 USD | `+38.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 1,710,000.00 USD | 1,130.00 USD | 0.00 USD | `+41.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 1,710,000.00 USD | 434.61 USD | 0.00 USD | `+42.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 1,710,000.00 USD | 163.52 USD | 0.00 USD | `+42.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 1,830,000.00 USD | 123,650.00 USD | 0.00 USD | `+43.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.51` | 1,830,000.00 USD | 2,770.00 USD | 0.00 USD | `+49.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 1,840,000.00 USD | 3,350.00 USD | 0.00 USD | `+52.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 1,840,000.00 USD | 197.97 USD | 0.00 USD | `+53.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 1,840,000.00 USD | 3,200.00 USD | 0.00 USD | `+54.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 1,840,000.00 USD | 179.58 USD | 0.00 USD | `+55.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 1,840,000.00 USD | 720.74 USD | 0.00 USD | `+55.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.07` | 1,840,000.00 USD | 504.17 USD | 0.00 USD | `+56.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 1,840,000.00 USD | 169.57 USD | 0.00 USD | `+57.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.30` | 1,840,000.00 USD | 159.66 USD | 0.00 USD | `+59.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 1,840,000.00 USD | 446.52 USD | 0.00 USD | `+60.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.46` | 1,840,000.00 USD | 1,710.00 USD | 0.00 USD | `+61.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 1,850,000.00 USD | 5,320.00 USD | 0.00 USD | `+61.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,060,000.00 USD | 210,750.00 USD | 0.00 USD | `+61.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,060,000.00 USD | 407.95 USD | 0.00 USD | `+64.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,060,000.00 USD | 174.91 USD | 0.00 USD | `+65.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,070,000.00 USD | 8,370.00 USD | 0.00 USD | `+67.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,070,000.00 USD | 960.26 USD | 0.00 USD | `+70.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,070,000.00 USD | 2,710.00 USD | 0.00 USD | `+72.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,070,000.00 USD | 805.90 USD | 0.00 USD | `+73.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,070,000.00 USD | 655.55 USD | 0.00 USD | `+76.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,080,000.00 USD | 4,890.00 USD | 0.00 USD | `+77.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,080,000.00 USD | 471.09 USD | 0.00 USD | `+78.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,080,000.00 USD | 383.85 USD | 0.00 USD | `+79.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 2,730,000.00 USD | 652,670.00 USD | 0.00 USD | `+79.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.06` | 2,730,000.00 USD | 1,510.00 USD | 0.00 USD | `+80.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 2,730,000.00 USD | 111.87 USD | 0.00 USD | `+89.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 2,730,000.00 USD | 219.91 USD | 0.00 USD | `+91.83%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.36` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 6,810.00 USD | 2,430.00 USD | 0.00 USD |
| `7D` | `7.40` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 6,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.42` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 48.44 USD |
| `1D` | `7.44` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 196.00 USD | 0.00 USD | 18,000.00 USD |
| `7D` | `7.44` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 331.70 USD | 1,680.00 USD | 15.01 USD |
| `1D` | `7.46` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 723.17 USD | 0.00 USD | 31,920.00 USD |
| `7D` | `7.46` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 0.00 USD | 1,410.00 USD | 24,000.00 USD |
| `1D` | `7.48` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 11,710.00 USD |
| `7D` | `7.48` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 9,120.00 USD | 0.00 USD | 20,570.00 USD |
| `1D` | `7.50` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 717.40 USD | 4,920.00 USD | 24,120.00 USD |
| `1D` | `7.52` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 26,110.00 USD | 9,580.00 USD | 36,440.00 USD |
| `7D` | `7.52` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 1,150.00 USD | 14,470.00 USD | 18,280.00 USD |
| `1D` | `7.54` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 62.12 USD |
| `7D` | `7.54` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 0.00 USD | 4,450.00 USD | 0.00 USD |
| `1D` | `7.56` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 15,020.00 USD | 4,270.00 USD | 3,090.00 USD |
| `7D` | `7.56` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 19,530.00 USD | 4,310.00 USD | 0.00 USD |
| `1D` | `7.58` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 91.65 USD |
| `1D` | `7.60` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 405.20 USD | 3,770.00 USD | 0.00 USD |
| `1D` | `7.62` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 583.80 USD | 0.00 USD | 11,600.00 USD |
| `1D` | `7.64` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 17,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.64` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 812.40 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.66` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 9,550.00 USD |
| `7D` | `7.66` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 23,280.00 USD |
| `7D` | `7.68` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 9,280.00 USD |
| `1D` | `7.70` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 321.75 USD | 2,390.00 USD | 14,120.00 USD |
| `1D` | `7.72` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 4,600.00 USD | 1,630.00 USD | 12,390.00 USD |
| `7D` | `7.72` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 32,590.00 USD |
| `1D` | `7.74` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 3,340.00 USD | 4,580.00 USD | 2,430.00 USD |
| `7D` | `7.74` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 976.80 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.76` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 1,510.00 USD | 1,100.00 USD | 5,190.00 USD |
| `7D` | `7.76` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 812.95 USD | 5,760.00 USD | 0.00 USD |
| `1D` | `7.78` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 44,950.00 USD | 3,730.00 USD | 9,070.00 USD |
| `7D` | `7.78` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 43,620.00 USD | 4,900.00 USD | 20,150.00 USD |
| `1D` | `7.80` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 39,070.00 USD | 10,860.00 USD | 8,670.00 USD |
| `7D` | `7.80` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 14,770.00 USD | 12,980.00 USD | 0.00 USD |
| `1D` | `7.82` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 5,100.00 USD | 7,610.00 USD | 5,740.00 USD |
| `7D` | `7.82` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,710.00 USD |
| `1D` | `7.84` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 2,680.00 USD | 4,910.00 USD | 12,790.00 USD |
| `7D` | `7.84` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 30,950.00 USD | 2,380.00 USD | 25,450.00 USD |
| `1D` | `7.86` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 15,790.00 USD | 1,680.00 USD | 16,400.00 USD |
| `7D` | `7.86` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 25,770.00 USD | 5,460.00 USD | 17,740.00 USD |
| `1D` | `7.88` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 46,100.00 USD | 9,570.00 USD | 22,420.00 USD |
| `7D` | `7.88` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 58,120.00 USD | 12,780.00 USD | 30,160.00 USD |
| `1D` | `7.90` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 14,150.00 USD | 7,630.00 USD | 7,430.00 USD |
| `7D` | `7.90` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 33,680.00 USD | 12,890.00 USD | 17,650.00 USD |
| `1D` | `7.92` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 24,660.00 USD | 2,950.00 USD | 6,370.00 USD |
| `7D` | `7.92` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 55,490.00 USD | 8,420.00 USD | 14,900.00 USD |
| `1D` | `7.94` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 20,330.00 USD | 6,860.00 USD | 48,750.00 USD |
| `7D` | `7.94` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 51,390.00 USD | 9,960.00 USD | 31,670.00 USD |
| `1D` | `7.96` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 2,830.00 USD | 11,220.00 USD | 97,230.00 USD |
| `7D` | `7.96` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 21,840.00 USD | 6,920.00 USD | 86,840.00 USD |
| `1D` | `7.98` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 17,030.00 USD | 3,300.00 USD | 37,960.00 USD |
| `7D` | `7.98` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 56,660.00 USD | 26,790.00 USD | 121,650.00 USD |
| `1D` | `8.00` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 1,500.00 USD | 16,670.00 USD | 62,290.00 USD |
| `7D` | `8.00` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 61,850.00 USD | 10,300.00 USD | 5,130.00 USD |
| `1D` | `8.02` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 81,330.00 USD | 10,580.00 USD | 82,400.00 USD |
| `7D` | `8.02` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 20,910.00 USD | 46,670.00 USD | 57,060.00 USD |
| `1D` | `8.04` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 33,700.00 USD | 17,810.00 USD | 14,580.00 USD |
| `7D` | `8.04` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 152,340.00 USD | 56,910.00 USD | 86,550.00 USD |
| `1D` | `8.06` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 76,840.00 USD | 22,300.00 USD | 18,840.00 USD |
| `7D` | `8.06` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 122,100.00 USD | 20,850.00 USD | 86,170.00 USD |
| `1D` | `8.08` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 36,720.00 USD | 6,070.00 USD | 13,740.00 USD |
| `7D` | `8.08` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 7,170.00 USD | 8,710.00 USD | 20,860.00 USD |
| `1D` | `8.10` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 32,890.00 USD | 14,990.00 USD | 96,920.00 USD |
| `7D` | `8.10` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 61,500.00 USD | 19,700.00 USD | 14,170.00 USD |
| `1D` | `8.12` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 75,310.00 USD | 12,270.00 USD | 215,820.00 USD |
| `7D` | `8.12` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 27,520.00 USD | 10,810.00 USD | 142,370.00 USD |
| `1D` | `8.14` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 12,410.00 USD | 0.00 USD | 58,580.00 USD |
| `7D` | `8.14` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 72,460.00 USD | 25,370.00 USD | 142,650.00 USD |
| `1D` | `8.16` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 44,830.00 USD | 29,660.00 USD | 159,110.00 USD |
| `7D` | `8.16` | 956,630.00 USD | 0.00 USD | 956,630.00 USD | 38,430.00 USD | 5,510.00 USD | 30,810.00 USD |
| `1D` | `8.18` | 984,710.00 USD | 0.00 USD | 984,710.00 USD | 133,120.00 USD | 19,620.00 USD | 175,550.00 USD |
| `7D` | `8.18` | 881,870.00 USD | 0.00 USD | 881,870.00 USD | 39,830.00 USD | 43,260.00 USD | 175,680.00 USD |
| `1D` | `8.20` | 656,430.00 USD | 0.00 USD | 656,430.00 USD | 33,560.00 USD | 32,530.00 USD | 16,800.00 USD |
| `7D` | `8.20` | 623,100.00 USD | 0.00 USD | 623,100.00 USD | 92,320.00 USD | 58,100.00 USD | 9,870.00 USD |
| `1D` | `8.22` | 573,540.00 USD | 0.00 USD | 573,540.00 USD | 32,330.00 USD | 39,650.00 USD | 35,790.00 USD |
| `7D` | `8.22` | 462,810.00 USD | 0.00 USD | 462,810.00 USD | 117,230.00 USD | 21,570.00 USD | 10,790.00 USD |
| `1D` | `8.24` | 465,770.00 USD | 0.00 USD | 465,770.00 USD | 163,080.00 USD | 10,300.00 USD | 69,860.00 USD |
| `7D` | `8.24` | 313,210.00 USD | 0.00 USD | 313,210.00 USD | 39,950.00 USD | 3,480.00 USD | 107,080.00 USD |
| `1D` | `8.26` | 222,530.00 USD | 0.00 USD | 222,530.00 USD | 15,150.00 USD | 15,590.00 USD | 16,600.00 USD |
| `7D` | `8.26` | 162,700.00 USD | 0.00 USD | 162,700.00 USD | 30,490.00 USD | 5,750.00 USD | 1,710.00 USD |
| `1D` | `8.28` | 175,200.00 USD | 0.00 USD | 175,200.00 USD | 175,140.00 USD | 0.00 USD | 57.32 USD |
| `7D` | `8.28` | 124,740.00 USD | 0.00 USD | 124,740.00 USD | 122,850.00 USD | 0.00 USD | 1,890.00 USD |
| `1D` | `8.30` | 183,820.00 USD | 183,820.00 USD | 0.00 USD | 183,720.00 USD | 0.00 USD | 107.30 USD |
| `1D` | `8.30` | 367,650.00 USD | 367,650.00 USD | 0.00 USD | 183,720.00 USD | 0.00 USD | 107.30 USD |
| `7D` | `8.30` | 154,020.00 USD | 154,020.00 USD | 0.00 USD | 152,370.00 USD | 0.00 USD | 1,650.00 USD |
| `7D` | `8.30` | 308,040.00 USD | 308,040.00 USD | 0.00 USD | 152,370.00 USD | 0.00 USD | 1,650.00 USD |
| `1D` | `8.32` | 422,910.00 USD | 422,910.00 USD | 0.00 USD | 55,190.00 USD | 0.00 USD | 77.98 USD |
| `7D` | `8.32` | 356,000.00 USD | 356,000.00 USD | 0.00 USD | 42,900.00 USD | 0.00 USD | 5,060.00 USD |
| `7D` | `8.34` | 360,490.00 USD | 360,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,490.00 USD |
| `1D` | `8.36` | 423,040.00 USD | 423,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 128.12 USD |
| `7D` | `8.36` | 378,390.00 USD | 378,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,900.00 USD |
| `1D` | `8.38` | 423,740.00 USD | 423,740.00 USD | 0.00 USD | 691.75 USD | 0.00 USD | 9.52 USD |
| `7D` | `8.38` | 436,130.00 USD | 436,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 57,740.00 USD |
| `7D` | `8.40` | 469,270.00 USD | 469,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33,140.00 USD |
| `1D` | `8.42` | 424,530.00 USD | 424,530.00 USD | 0.00 USD | 788.46 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.42` | 485,340.00 USD | 485,340.00 USD | 0.00 USD | 16,070.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.44` | 514,510.00 USD | 514,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 89,980.00 USD |
| `7D` | `8.44` | 495,820.00 USD | 495,820.00 USD | 0.00 USD | 10,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.46` | 702,750.00 USD | 702,750.00 USD | 0.00 USD | 0.00 USD | 4,700.00 USD | 183,540.00 USD |
| `7D` | `8.46` | 983,910.00 USD | 983,910.00 USD | 0.00 USD | 365,050.00 USD | 0.00 USD | 123,040.00 USD |
| `1D` | `8.48` | 800,510.00 USD | 800,510.00 USD | 0.00 USD | 0.00 USD | 39,180.00 USD | 58,580.00 USD |
| `7D` | `8.48` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 49,360.00 USD | 104,250.00 USD |
| `1D` | `8.50` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 66,120.00 USD | 88,980.00 USD | 120,620.00 USD |
| `7D` | `8.50` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 100,070.00 USD | 1,470.00 USD |
| `1D` | `8.52` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 203,080.00 USD | 69,980.00 USD | 164,920.00 USD |
| `7D` | `8.52` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 2,990.00 USD | 135,400.00 USD | 92,600.00 USD |
| `1D` | `8.54` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 61,500.00 USD | 32,530.00 USD | 16,750.00 USD |
| `7D` | `8.54` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 71,540.00 USD | 136,470.00 USD | 2,010.00 USD |
| `1D` | `8.56` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 183,280.00 USD | 33,670.00 USD | 0.00 USD |
| `7D` | `8.56` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 691,140.00 USD | 122,650.00 USD | 790.79 USD |
| `1D` | `8.58` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 234,090.00 USD | 5,060.00 USD | 179,360.00 USD |
| `7D` | `8.58` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 599,490.00 USD | 164,810.00 USD | 801.88 USD |
| `1D` | `8.60` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 57,190.00 USD | 120,500.00 USD |
| `7D` | `8.60` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 75,040.00 USD | 39,160.00 USD | 1,110.00 USD |
| `1D` | `8.62` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 65,710.00 USD | 57,150.00 USD | 149,780.00 USD |
| `7D` | `8.62` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 43,670.00 USD | 86,620.00 USD |
| `1D` | `8.64` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 89,460.00 USD | 30,330.00 USD | 29,280.00 USD |
| `7D` | `8.64` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 12,800.00 USD | 51,440.00 USD |
| `1D` | `8.66` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 78,620.00 USD | 14,830.00 USD | 108,320.00 USD |
| `7D` | `8.66` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 16,520.00 USD | 950.21 USD |
| `1D` | `8.68` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 65,090.00 USD | 9,810.00 USD | 212,540.00 USD |
| `7D` | `8.68` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 207,090.00 USD | 43,100.00 USD | 335,750.00 USD |
| `1D` | `8.70` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 50,130.00 USD | 16,260.00 USD | 30,560.00 USD |
| `7D` | `8.70` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 29,260.00 USD | 41,840.00 USD | 46,400.00 USD |
| `1D` | `8.72` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 18,250.00 USD | 0.00 USD | 50,540.00 USD |
| `1D` | `8.74` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 49,110.00 USD | 28,810.00 USD | 12,900.00 USD |
| `7D` | `8.74` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 48,810.00 USD | 30,470.00 USD | 0.00 USD |
| `1D` | `8.76` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 112,960.00 USD | 2,530.00 USD | 9,960.00 USD |
| `7D` | `8.76` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,400.00 USD |
| `1D` | `8.78` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 108,350.00 USD | 11,500.00 USD | 35,750.00 USD |
| `7D` | `8.78` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 2,300.00 USD | 0.00 USD | 58,840.00 USD |
| `1D` | `8.80` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 125,120.00 USD | 22,330.00 USD | 53,030.00 USD |
| `7D` | `8.80` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 27,360.00 USD | 33,750.00 USD | 32,140.00 USD |
| `1D` | `8.82` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 19,020.00 USD | 0.00 USD | 203.82 USD |
| `7D` | `8.82` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 103,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.84` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 40,640.00 USD | 8,820.00 USD | 73,570.00 USD |
| `1D` | `8.86` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 13,620.00 USD | 2,250.00 USD | 10,690.00 USD |
| `7D` | `8.86` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 29,310.00 USD | 0.00 USD | 82,390.00 USD |
| `1D` | `8.88` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 1,170.00 USD | 8,950.00 USD | 0.00 USD |
| `7D` | `8.88` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,570.00 USD |
| `1D` | `8.90` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 31,860.00 USD | 8,140.00 USD | 122,720.00 USD |
| `7D` | `8.90` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 2,440.00 USD | 0.00 USD | 115,480.00 USD |
| `1D` | `8.92` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 40,710.00 USD | 7,360.00 USD | 17,130.00 USD |
| `7D` | `8.92` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 1,730.00 USD | 0.00 USD | 17,620.00 USD |
| `1D` | `8.94` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 41,740.00 USD | 12,260.00 USD | 18,000.00 USD |
| `7D` | `8.94` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 58,330.00 USD | 0.00 USD | 433.10 USD |
| `1D` | `8.96` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 2,010.00 USD | 0.00 USD | 152.79 USD |
| `7D` | `8.96` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.98` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 25,040.00 USD | 5,550.00 USD | 19,550.00 USD |
| `7D` | `8.98` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,090.00 USD |
| `1D` | `9.00` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 85,360.00 USD | 30,520.00 USD | 11,130.00 USD |
| `7D` | `9.00` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 297,650.00 USD | 11,360.00 USD | 20,780.00 USD |
| `1D` | `9.02` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 40,920.00 USD | 43,160.00 USD | 18,720.00 USD |
| `7D` | `9.02` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 34,650.00 USD | 56,120.00 USD | 749.72 USD |
| `1D` | `9.04` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 87,540.00 USD | 43,590.00 USD | 38,200.00 USD |
| `7D` | `9.04` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 90,520.00 USD | 74,750.00 USD | 15,140.00 USD |
| `1D` | `9.06` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 35,620.00 USD | 33,420.00 USD | 60,040.00 USD |
| `7D` | `9.06` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 7,440.00 USD | 14,960.00 USD | 53,420.00 USD |
| `1D` | `9.08` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 28,800.00 USD | 29,710.00 USD | 71,700.00 USD |
| `7D` | `9.08` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD |
| `1D` | `9.10` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 197,760.00 USD | 43,240.00 USD | 81,450.00 USD |
| `7D` | `9.10` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 826,500.00 USD | 35,760.00 USD | 334,020.00 USD |
| `1D` | `9.12` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 160,000.00 USD | 47,350.00 USD | 87,950.00 USD |
| `7D` | `9.12` | 7,970,000.00 USD | 7,970,000.00 USD | 0.00 USD | 490,020.00 USD | 24,170.00 USD | 503,360.00 USD |
| `1D` | `9.14` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 118,520.00 USD | 23,510.00 USD | 79,080.00 USD |
| `7D` | `9.14` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 536,560.00 USD | 18,540.00 USD | 500,290.00 USD |
| `1D` | `9.16` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 121,810.00 USD | 44,640.00 USD | 63,920.00 USD |
| `7D` | `9.16` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 358,370.00 USD | 44,360.00 USD | 195,800.00 USD |
| `1D` | `9.18` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 188,150.00 USD | 48,600.00 USD | 107,750.00 USD |
| `7D` | `9.18` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 565,140.00 USD | 162,460.00 USD | 292,040.00 USD |
| `1D` | `9.20` | 6,930,000.00 USD | 6,930,000.00 USD | 0.00 USD | 145,450.00 USD | 43,540.00 USD | 54,260.00 USD |
| `7D` | `9.20` | 11,560,000.00 USD | 11,560,000.00 USD | 0.00 USD | 549,250.00 USD | 134,550.00 USD | 238,840.00 USD |
| `1D` | `9.22` | 7,040,000.00 USD | 7,040,000.00 USD | 0.00 USD | 86,390.00 USD | 10,580.00 USD | 13,460.00 USD |
| `7D` | `9.22` | 12,710,000.00 USD | 12,710,000.00 USD | 0.00 USD | 585,170.00 USD | 144,840.00 USD | 416,230.00 USD |
| `1D` | `9.24` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 47,010.00 USD | 4,270.00 USD | 3,500.00 USD |
| `7D` | `9.24` | 13,280,000.00 USD | 13,280,000.00 USD | 0.00 USD | 335,740.00 USD | 56,410.00 USD | 174,910.00 USD |
| `1D` | `9.26` | 7,150,000.00 USD | 7,150,000.00 USD | 0.00 USD | 35,150.00 USD | 8,290.00 USD | 9,910.00 USD |
| `7D` | `9.26` | 13,710,000.00 USD | 13,710,000.00 USD | 0.00 USD | 273,920.00 USD | 96,980.00 USD | 60,730.00 USD |
| `1D` | `9.28` | 7,210,000.00 USD | 7,210,000.00 USD | 0.00 USD | 44,530.00 USD | 10,920.00 USD | 2,700.00 USD |
| `7D` | `9.28` | 14,410,000.00 USD | 14,410,000.00 USD | 0.00 USD | 428,160.00 USD | 103,490.00 USD | 170,610.00 USD |
| `1D` | `9.30` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 59,470.00 USD | 13,560.00 USD | 29,530.00 USD |
| `7D` | `9.30` | 14,970,000.00 USD | 14,970,000.00 USD | 0.00 USD | 199,810.00 USD | 97,780.00 USD | 262,830.00 USD |
| `1D` | `9.32` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 37,200.00 USD | 4,250.00 USD | 23,730.00 USD |
| `7D` | `9.32` | 15,640,000.00 USD | 15,640,000.00 USD | 0.00 USD | 271,660.00 USD | 59,310.00 USD | 337,940.00 USD |
| `1D` | `9.34` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 40,730.00 USD | 9,520.00 USD | 11,380.00 USD |
| `7D` | `9.34` | 15,970,000.00 USD | 15,970,000.00 USD | 0.00 USD | 204,260.00 USD | 53,150.00 USD | 70,540.00 USD |
| `1D` | `9.36` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 59,430.00 USD | 12,270.00 USD | 34,350.00 USD |
| `7D` | `9.36` | 16,380,000.00 USD | 16,380,000.00 USD | 0.00 USD | 247,120.00 USD | 73,430.00 USD | 97,710.00 USD |
| `1D` | `9.38` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 31,430.00 USD | 7,320.00 USD | 16,250.00 USD |
| `7D` | `9.38` | 16,920,000.00 USD | 16,920,000.00 USD | 0.00 USD | 383,530.00 USD | 55,400.00 USD | 94,530.00 USD |
| `1D` | `9.40` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 31,880.00 USD | 0.00 USD | 7.66 USD |
| `7D` | `9.40` | 17,320,000.00 USD | 17,320,000.00 USD | 0.00 USD | 234,760.00 USD | 42,520.00 USD | 124,730.00 USD |
| `1D` | `9.42` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 10,810.00 USD | 2,390.00 USD | 14,330.00 USD |
| `7D` | `9.42` | 17,590,000.00 USD | 17,590,000.00 USD | 0.00 USD | 176,920.00 USD | 19,780.00 USD | 70,640.00 USD |
| `1D` | `9.44` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 10,560.00 USD | 1,630.00 USD | 12,390.00 USD |
| `7D` | `9.44` | 17,700,000.00 USD | 17,700,000.00 USD | 0.00 USD | 41,250.00 USD | 19,420.00 USD | 56,670.00 USD |
| `1D` | `9.46` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 1,350.00 USD | 4,580.00 USD | 2,430.00 USD |
| `7D` | `9.46` | 17,810,000.00 USD | 17,810,000.00 USD | 0.00 USD | 60,020.00 USD | 29,830.00 USD | 19,460.00 USD |
| `1D` | `9.48` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 1,050.00 USD | 1,100.00 USD | 5,190.00 USD |
| `7D` | `9.48` | 17,880,000.00 USD | 17,880,000.00 USD | 0.00 USD | 12,180.00 USD | 27,840.00 USD | 25,250.00 USD |
| `1D` | `9.49` | 7,740,000.00 USD | 7,740,000.00 USD | 0.00 USD | 29,020.00 USD | 572.85 USD | 8,950.00 USD |
| `7D` | `9.50` | 18,050,000.00 USD | 18,050,000.00 USD | 0.00 USD | 89,460.00 USD | 33,210.00 USD | 45,440.00 USD |
| `7D` | `9.52` | 18,230,000.00 USD | 18,230,000.00 USD | 0.00 USD | 102,150.00 USD | 29,320.00 USD | 51,740.00 USD |
| `7D` | `9.54` | 18,450,000.00 USD | 18,450,000.00 USD | 0.00 USD | 192,090.00 USD | 25,090.00 USD | 930.52 USD |
| `7D` | `9.56` | 18,560,000.00 USD | 18,560,000.00 USD | 0.00 USD | 88,510.00 USD | 5,260.00 USD | 13,550.00 USD |
| `7D` | `9.58` | 18,630,000.00 USD | 18,630,000.00 USD | 0.00 USD | 35,340.00 USD | 14,530.00 USD | 27,300.00 USD |
| `7D` | `9.60` | 18,700,000.00 USD | 18,700,000.00 USD | 0.00 USD | 38,740.00 USD | 5,460.00 USD | 18,930.00 USD |
| `7D` | `9.62` | 18,780,000.00 USD | 18,780,000.00 USD | 0.00 USD | 70,470.00 USD | 1,540.00 USD | 10,980.00 USD |
| `7D` | `9.64` | 18,850,000.00 USD | 18,850,000.00 USD | 0.00 USD | 35,210.00 USD | 17,650.00 USD | 19,940.00 USD |
| `7D` | `9.66` | 18,930,000.00 USD | 18,930,000.00 USD | 0.00 USD | 37,340.00 USD | 21,280.00 USD | 18,480.00 USD |
| `7D` | `9.68` | 19,030,000.00 USD | 19,030,000.00 USD | 0.00 USD | 68,230.00 USD | 20,310.00 USD | 15,070.00 USD |
| `7D` | `9.70` | 19,160,000.00 USD | 19,160,000.00 USD | 0.00 USD | 77,860.00 USD | 12,990.00 USD | 31,670.00 USD |
| `7D` | `9.72` | 19,260,000.00 USD | 19,260,000.00 USD | 0.00 USD | 70,300.00 USD | 6,920.00 USD | 26,680.00 USD |
| `7D` | `9.74` | 19,310,000.00 USD | 19,310,000.00 USD | 0.00 USD | 21,230.00 USD | 7,200.00 USD | 19,500.00 USD |
| `7D` | `9.76` | 19,410,000.00 USD | 19,410,000.00 USD | 0.00 USD | 35,520.00 USD | 12,480.00 USD | 52,240.00 USD |
| `7D` | `9.78` | 19,490,000.00 USD | 19,490,000.00 USD | 0.00 USD | 65,390.00 USD | 10,300.00 USD | 5,270.00 USD |
| `7D` | `9.80` | 19,550,000.00 USD | 19,550,000.00 USD | 0.00 USD | 18,630.00 USD | 28,440.00 USD | 10,630.00 USD |
| `7D` | `9.82` | 19,780,000.00 USD | 19,780,000.00 USD | 0.00 USD | 121,860.00 USD | 27,860.00 USD | 86,290.00 USD |
| `7D` | `9.84` | 19,810,000.00 USD | 19,810,000.00 USD | 0.00 USD | 9,730.00 USD | 7,850.00 USD | 14,230.00 USD |
| `7D` | `9.86` | 19,950,000.00 USD | 19,950,000.00 USD | 0.00 USD | 58,130.00 USD | 2,210.00 USD | 71,950.00 USD |
| `7D` | `9.88` | 19,980,000.00 USD | 19,980,000.00 USD | 0.00 USD | 7,170.00 USD | 8,710.00 USD | 20,860.00 USD |
| `7D` | `9.90` | 20,070,000.00 USD | 20,070,000.00 USD | 0.00 USD | 55,970.00 USD | 19,700.00 USD | 14,310.00 USD |
| `7D` | `9.92` | 20,120,000.00 USD | 20,120,000.00 USD | 0.00 USD | 27,710.00 USD | 10,810.00 USD | 9,370.00 USD |
| `7D` | `9.94` | 20,250,000.00 USD | 20,250,000.00 USD | 0.00 USD | 69,320.00 USD | 11,150.00 USD | 51,780.00 USD |
| `7D` | `9.96` | 20,300,000.00 USD | 20,300,000.00 USD | 0.00 USD | 29,800.00 USD | 1,360.00 USD | 11,160.00 USD |
| `7D` | `9.98` | 20,330,000.00 USD | 20,330,000.00 USD | 0.00 USD | 840.10 USD | 4,150.00 USD | 29,280.00 USD |
| `7D` | `10.00` | 20,340,000.00 USD | 20,340,000.00 USD | 0.00 USD | 0.00 USD | 6,790.00 USD | 0.00 USD |
| `7D` | `10.02` | 20,370,000.00 USD | 20,370,000.00 USD | 0.00 USD | 16,100.00 USD | 3,650.00 USD | 15,030.00 USD |
| `7D` | `10.04` | 20,390,000.00 USD | 20,390,000.00 USD | 0.00 USD | 1,080.00 USD | 3,590.00 USD | 9,540.00 USD |
| `7D` | `10.06` | 20,410,000.00 USD | 20,410,000.00 USD | 0.00 USD | 0.00 USD | 3,480.00 USD | 17,230.00 USD |
| `7D` | `10.08` | 20,430,000.00 USD | 20,430,000.00 USD | 0.00 USD | 23,580.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `350.35M` | Total OI Tokens: `42,373,203.8 AVAX`
  * 1h OI Change: `-1.03%` | 4h OI Change: `-7.74%` | 24h OI Change: `-11.18%`
  * Exchange Breakdown: Binance=`80.82M` | Bybit=`56.90M` | OKX=`11.68M` | Hyperliquid=`16.49M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-2.08K` | Last 24h: `33.77K` | Last 3d: `72.05K` | Last 7d: `92.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0017%` | **USDT OKX** | `0.0008%` |
| **USDT Bybit** | `-0.0064%` | **USDT KuCoin** | `0.0013%` |
| **USDT MEXC** | `0.0015%` | **USDT BingX** | `0.0020%` |
| **USDT Gate** | `-0.0050%` | **USDT Bitget** | `0.0020%` |
| **CoinM Binance** | `0.0083%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `45.67%` | `54.33%` | `0.84` | 27,960,000.00 USD |
| `15M` | `Binance` | `47.63%` | `52.37%` | `0.91` | 9,870,000.00 USD |
| `15M` | `OKX` | `42.79%` | `57.21%` | `0.75` | 2,050,000.00 USD |
| `15M` | `Bybit` | `54.27%` | `45.73%` | `1.19` | 2,890,000.00 USD |
| `15M` | `KuCoin` | `57.82%` | `42.18%` | `1.37` | 87,570.00 USD |
| `15M` | `Gate` | `43.48%` | `56.52%` | `0.77` | 613,560.00 USD |
| `15M` | `Bitget` | `51.08%` | `48.92%` | `1.04` | 876,960.00 USD |
| `15M` | `BingX` | `34.79%` | `65.21%` | `0.53` | 513,710.00 USD |
| `15M` | `MEXC` | `47.83%` | `52.17%` | `0.92` | 4,730,000.00 USD |
| `15M` | `Bitunix` | `47.72%` | `52.28%` | `0.91` | 1,220,000.00 USD |
| `15M` | `Hyperliquid` | `24.21%` | `75.79%` | `0.32` | 3,700,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.64%` | `50.36%` | `0.99` | 526,820.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `91.76%` | `8.24%` | `11.14` | 447,000.00 USD |
| `15M` | `HTX` | `42.76%` | `57.24%` | `0.75` | 1,940.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `52.68%` | `47.32%` | `1.11` | 159,480.00 USD |
| `15M` | `Aster` | `75.79%` | `24.21%` | `3.13` | 70,930.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `63.4%` | `36.6%` | `1.73` | 198,950.00 USD |
| `15M` | `Whale Positions` | `47.63%` | `52.37%` | `0.91` | 9,870,000.00 USD |
| `15M` | `Global Accounts` | `45.67%` | `54.33%` | `0.84` | 27,960,000.00 USD |
| `1H` | `AVAX` | `45.25%` | `54.75%` | `0.83` | 131,880,000.00 USD |
| `1H` | `Binance` | `42.55%` | `57.45%` | `0.74` | 53,660,000.00 USD |
| `1H` | `OKX` | `45.94%` | `54.06%` | `0.85` | 10,410,000.00 USD |
| `1H` | `Bybit` | `50.62%` | `49.38%` | `1.03` | 12,840,000.00 USD |
| `1H` | `KuCoin` | `44.3%` | `55.7%` | `0.80` | 554,460.00 USD |
| `1H` | `Gate` | `49.82%` | `50.18%` | `0.99` | 3,080,000.00 USD |
| `1H` | `Bitget` | `48.27%` | `51.73%` | `0.93` | 5,220,000.00 USD |
| `1H` | `BingX` | `44.04%` | `55.96%` | `0.79` | 2,020,000.00 USD |
| `1H` | `MEXC` | `49.35%` | `50.65%` | `0.97` | 22,830,000.00 USD |
| `1H` | `Bitunix` | `45.39%` | `54.61%` | `0.83` | 4,450,000.00 USD |
| `1H` | `Hyperliquid` | `28.54%` | `71.46%` | `0.40` | 9,470,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.46%` | `49.54%` | `1.02` | 2,980,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `85.99%` | `14.01%` | `6.14` | 2,020,000.00 USD |
| `1H` | `HTX` | `38.82%` | `61.18%` | `0.63` | 25,760.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `47.68%` | `52.32%` | `0.91` | 1,030,000.00 USD |
| `1H` | `Aster` | `37.67%` | `62.33%` | `0.60` | 388,360.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `55.44%` | `44.56%` | `1.24` | 878,800.00 USD |
| `1H` | `Whale Positions` | `42.55%` | `57.45%` | `0.74` | 53,660,000.00 USD |
| `1H` | `Global Accounts` | `45.25%` | `54.75%` | `0.83` | 131,880,000.00 USD |
| `4H` | `AVAX` | `49.24%` | `50.76%` | `0.97` | 578,050,000.00 USD |
| `4H` | `Binance` | `49.82%` | `50.18%` | `0.99` | 239,900,000.00 USD |
| `4H` | `OKX` | `51.51%` | `48.49%` | `1.06` | 66,020,000.00 USD |
| `4H` | `Bybit` | `49.77%` | `50.23%` | `0.99` | 116,890,000.00 USD |
| `4H` | `KuCoin` | `54.92%` | `45.08%` | `1.22` | 3,000,000.00 USD |
| `4H` | `Gate` | `46.55%` | `53.45%` | `0.87` | 22,370,000.00 USD |
| `4H` | `Bitget` | `53.61%` | `46.39%` | `1.16` | 17,050,000.00 USD |
| `4H` | `BingX` | `38.6%` | `61.4%` | `0.63` | 8,340,000.00 USD |
| `4H` | `MEXC` | `44.51%` | `55.49%` | `0.80` | 7,900,000.00 USD |
| `4H` | `Bitunix` | `54.41%` | `45.59%` | `1.19` | 9,040,000.00 USD |
| `4H` | `Hyperliquid` | `52.57%` | `47.43%` | `1.11` | 30,800,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.25%` | `47.75%` | `1.09` | 13,250,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `32.53%` | `67.47%` | `0.48` | 32,400,000.00 USD |
| `4H` | `HTX` | `53.93%` | `46.07%` | `1.17` | 1,940,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `63.89%` | `36.11%` | `1.77` | 3,550,000.00 USD |
| `4H` | `Aster` | `64.75%` | `35.25%` | `1.84` | 2,790,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.43%` | `52.57%` | `0.90` | 2,790,000.00 USD |
| `4H` | `Whale Positions` | `49.82%` | `50.18%` | `0.99` | 239,900,000.00 USD |
| `4H` | `Global Accounts` | `49.24%` | `50.76%` | `0.97` | 578,050,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `8.26` | `8.35` | `8.26` | `8.48` | `8.25` | 17,210,058.04 USD | 7,276,281.50 USD | 9,933,776.55 USD | -2,657,495.05 USD | `-15.44%` | `5B / 17S` |
| `0:00 UTC` | `8.44` | `8.39` | `8.44` | `8.47` | `8.31` | 5,735,994.33 USD | 3,091,126.19 USD | 2,644,868.14 USD | 446,258.06 USD | `+7.78%` | `31B / 8S` |
| `5:00 UTC` | `8.57` | `8.52` | `8.57` | `8.60` | `8.44` | 5,418,565.28 USD | 2,882,511.31 USD | 2,536,053.98 USD | 346,457.33 USD | `+6.39%` | `29B / 7S` |
| `0:00 UTC` | `8.49` | `8.53` | `8.49` | `8.57` | `8.47` | 2,187,831.94 USD | 1,148,223.68 USD | 1,039,608.27 USD | 108,615.41 USD | `+4.96%` | `15B / 18S` |
| `5:00 UTC` | `8.46` | `8.45` | `8.46` | `8.48` | `8.42` | 2,763,123.34 USD | 1,578,085.08 USD | 1,185,038.26 USD | 393,046.81 USD | `+14.22%` | `14B / 6S` |
| `0:00 UTC` | `8.38` | `8.39` | `8.38` | `8.45` | `8.32` | 6,384,975.85 USD | 3,950,900.17 USD | 2,434,075.68 USD | 1,516,824.48 USD | `+23.76%` | `27B / 6S` |
| `5:00 UTC` | `8.39` | `8.36` | `8.39` | `8.43` | `8.30` | 4,694,228.85 USD | 2,250,331.95 USD | 2,443,896.90 USD | -193,564.95 USD | `-4.12%` | `23B / 20S` |
| `0:00 UTC` | `8.38` | `8.39` | `8.38` | `8.43` | `8.34` | 2,925,314.33 USD | 1,381,283.14 USD | 1,544,031.19 USD | -162,748.05 USD | `-5.56%` | `9B / 9S` |
| `5:00 UTC` | `8.35` | `8.35` | `8.35` | `8.37` | `8.32` | 3,889,099.59 USD | 2,394,197.64 USD | 1,494,901.94 USD | 899,295.70 USD | `+23.12%` | `8B / 3S` |
| `0:00 UTC` | `8.29` | `8.30` | `8.29` | `8.36` | `8.26` | 4,675,690.36 USD | 2,298,370.71 USD | 2,377,319.66 USD | -78,948.95 USD | `-1.69%` | `15B / 15S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:30` | `Range 0.025` | `Divergence` | **`BEARISH`** | Rally without taker buying | `8.88` | 0.00 USD | 0.00 USD |
| `10-28 20:17` | `Volume 200K AVAX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `8.88` | 0.00 USD | 0.00 USD |
| `10-28 19:50` | `Volume 200K AVAX` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `8.79` | 0.00 USD | 0.00 USD |
| `10-28 19:17` | `Volume 200K AVAX` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `8.81` | 35,000.00 USD | 0.00 USD |
| `10-28 19:17` | `Range 0.025` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `8.81` | 35,000.00 USD | 0.00 USD |
| `10-28 19:17` | `Range 0.025` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `8.81` | 28,000.00 USD | 0.00 USD |
| `10-28 19:05` | `Volume 200K AVAX` | `Divergence` | **`BULLISH`** | Drop without taker selling | `8.86` | 0.00 USD | 0.00 USD |
| `10-28 18:17` | `Range 0.025` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `8.85` | 15,000.00 USD | 0.00 USD |
| `10-28 18:17` | `Range 0.025` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `8.85` | 15,000.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 200K AVAX` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `8.90` | 0.00 USD | 0.00 USD |
| `10-28 17:35` | `Volume 200K AVAX` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `8.96` | 41,000.00 USD | 0.00 USD |
| `10-28 15:02` | `Range 0.025` | `Divergence` | **`BEARISH`** | Rally without taker buying | `9.02` | 0.00 USD | 0.00 USD |
| `10-28 15:02` | `Range 0.025` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `8.99` | 0.00 USD | 0.00 USD |
| `10-28 14:06` | `Range 0.025` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `9.08` | 114,000.00 USD | 0.00 USD |
| `10-28 14:01` | `Volume 200K AVAX` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `9.08` | 125,000.00 USD | 0.00 USD |
| `10-28 13:57` | `Range 0.025` | `Divergence` | **`BULLISH`** | Drop without taker selling | `9.03` | 0.00 USD | 0.00 USD |
| `10-28 13:44` | `Range 0.025` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `9.00` | 16,000.00 USD | 0.00 USD |
| `10-28 12:46` | `Range 0.025` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `8.95` | 0.00 USD | 0.00 USD |
| `10-28 09:02` | `Volume 200K AVAX` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `9.08` | 38,000.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.025` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `9.07` | 0.00 USD | 0.00 USD |
| `10-28 06:13` | `Range 0.025` | `Divergence` | **`BEARISH`** | Rally without taker buying | `8.98` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 45,010.00 USD | -798,970.00 USD | **`DISTRIBUTION`** |
| `15m` | 62,790.00 USD | -924,460.00 USD | **`DISTRIBUTION`** |
| `30m` | 272,540.00 USD | -1,010,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 543,930.00 USD | -396,950.00 USD | **`ACCUMULATION`** |
| `2h` | 463,570.00 USD | 1,200,000.00 USD | **`ACCUMULATION`** |
| `4h` | -1,430,000.00 USD | -6,290,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,520,000.00 USD | -8,440,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,430,000.00 USD | -9,360,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,300,000.00 USD | -9,260,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,190,000.00 USD | -12,660,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,120,000.00 USD | -50,120,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -54,990,000.00 USD | -276,280,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+45.01K` | 15m=`+62.79K` | 1h=`+543.93K` | 24h=`-1.19M`
* Futures Capital Netflows: 5m=`-798.97K` | 15m=`-924.46K` | 1h=`-396.95K` | 24h=`-12.66M`
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
  * `2026-10-30 04:15:34 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:40:34 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:34 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `8.27` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `8.11` (Risk Distance: `0.1609` pts)
  * +2.5R Take Profit: `8.67`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.43` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `8.59` (Risk Distance: `0.1609` pts)
  * +2.5R Take Profit: `8.03`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.38`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
