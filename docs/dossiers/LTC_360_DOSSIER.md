# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 04:10:46 IST` (`2026-10-29 22:40:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `55.47` | **Live Ask Quote**: `55.77` | **Mid Price**: `55.62`
- **Spread Points**: `300.00` | **Spread BPS**: `53.94 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `57.26` | VWAP Z-Score: `-1.61` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.5702` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `35.89` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `60.76` | Lower -3.00σ Band: `53.76`
  * Upper +2.51σ Band: `60.19` | Lower -2.51σ Band: `54.33`
  * Upper +2.01σ Band: `59.60` | Lower -2.01σ Band: `54.91`
  * Upper +2.00σ Band: `59.59` | Lower -2.00σ Band: `54.92`
  * Upper +1.28σ Band: `58.75` | Lower -1.28σ Band: `55.76`
  * Upper +1.00σ Band: `58.42` | Lower -1.00σ Band: `56.09`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`55.60` | EMA-20=`56.29` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`57.02` (Slope: `+0.0000`) | EMA-100=`57.35`
  * Institutional Anchors: EMA-144=`57.39` | EMA-200=`57.26` (Slope: `-0.3028`) | EMA-233=`57.17`
- **Range Boundaries**: 24H High=`59.52` | 24H Low=`54.18` | Weekly High=`59.62` | Weekly Low=`54.18`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `55.56` (Distance: `+0.18%`)
  * Point of Control (POC) = `55.28` (Distance: `+0.69%`)
  * Value Area Low (VAL) = `54.92` (Distance: `+1.34%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.40` | POC=`57.72` | VAL=`56.83`
  * Prior Day Extremes: PDH=`59.52` | PDL=`54.18` | PDC=`54.46`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`57.90` | Weekly POC=`56.45` | Weekly VAL=`56.01`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`55.89` | Low=`54.61`
  * London Session (08:00-16:00 UTC): High=`55.84` | Low=`55.39`
  * New York Session (13:00-21:00 UTC): High=`55.95` | Low=`55.28`
  * Initial Balance (First Hour): IB High=`55.78` | IB Low=`55.45`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `55.39` - `55.84`
  * Optimal Trade Entry (OTE 0.705): `55.73`
  * Structural Invalidation Anchor (0.786): `56.06`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `55.50` | `55.69` | `55.40` | `55.64` | `5,588` | 310,412.70 USD | 39,783.23 USD | `+12.82%` | -3,617,984.40 USD | `+0.18` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `55.65` | `55.79` | `55.58` | `55.58` | `5,864` | 326,636.34 USD | 27,190.45 USD | `+8.32%` | -3,590,793.95 USD | `-0.09` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `55.57` | `55.75` | `55.48` | `55.71` | `7,060` | 392,731.24 USD | 19,576.38 USD | `+4.98%` | -3,571,217.57 USD | `-0.04` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `55.28` | `55.55` | `54.79` | `55.35` | `35,836` | 1,975,627.97 USD | 166,914.68 USD | `+8.45%` | -3,679,208.86 USD | `+0.53` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `55.34` | `55.79` | `55.11` | `55.58` | `22,671` | 1,258,609.21 USD | 133,934.26 USD | `+10.64%` | -3,545,274.60 USD | `+0.46` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `55.57` | `55.75` | `55.48` | `55.71` | `7,060` | 392,731.24 USD | 19,576.38 USD | `+4.98%` | -3,525,698.22 USD | `+0.26` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `57.98` | `58.01` | `54.17` | `54.65` | `399,021` | 22,240,643.23 USD | -3,425,260.07 USD | `-15.40%` | -4,121,559.43 USD | `-3.93` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `54.64` | `56.10` | `54.52` | `55.28` | `203,261` | 11,266,201.42 USD | 431,317.68 USD | `+3.83%` | -3,690,241.75 USD | `+0.71` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `55.28` | `55.79` | `54.79` | `55.71` | `65,595` | 3,628,472.51 USD | 321,885.62 USD | `+8.87%` | -3,368,356.13 USD | `+0.52` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | -1,031,107.81 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | -891,821.26 USD | `+0.52` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `55.71` | `667,850` | 37,133,813.07 USD | -2,673,517.06 USD | `-7.20%` | -3,565,338.32 USD | `-1.91` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `57.20` | `58.23` | `56.92` | `57.04` | `229,127` | 13,178,164.26 USD | -500,207.83 USD | `-3.80%` | -1,732,502.54 USD | `+1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `57.04` | `58.16` | `56.85` | `58.00` | `178,996` | 10,300,529.12 USD | 452,809.17 USD | `+4.40%` | -1,279,693.37 USD | `+1.27` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | -1,031,107.81 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | -891,821.26 USD | `+0.52` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `55.71` | `667,850` | 37,133,813.07 USD | -2,673,517.06 USD | `-7.20%` | -3,565,338.32 USD | `-1.91` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`55.62`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:05:52 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1078` | `0xeadc...9d55` | `LONG` | 2,030,521.50 USD | `36,463.77` | `52.78` | `55.70` | `0.000000` | 105,845.55 USD | `+5.21%` | `10X Cross` |
| `1094` | `0x9aa5...58af` | `SHORT` | 2,011,368.81 USD | `36,177.65` | `71.22` | `55.70` | `301.30` | 565,117.86 USD | `+28.10%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `57.33` | 7,510.23 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 57.3300 USD [API] | `2026-10-28 14:13:48` |
| `ANNOUNCEMENT` | `INFO` | `59.08` | 5,576.94 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 5.58K USD at 59.0840 USD [API] | `2026-10-28 16:25:48` |
| `ANNOUNCEMENT` | `INFO` | `59.08` | 5,808.45 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 5.81K USD at 59.0830 USD [API] | `2026-10-28 16:25:48` |
| `ANNOUNCEMENT` | `INFO` | `59.15` | 7,510.02 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 7.51K USD at 59.1480 USD [API] | `2026-10-28 16:27:53` |
| `ANNOUNCEMENT` | `INFO` | `59.08` | 1,467.06 USD | `-` | `NEWS_INTEL` | `-` | #LTC Liquidated Long: 1.47K USD at 59.0840 USD [API] | `2026-10-28 16:25:48` |
| `ANNOUNCEMENT` | `INFO` | `59.03` | 4,420.09 USD | `-` | `NEWS_INTEL` | `-` | #LTC Liquidated Long: 4.42K USD at 59.0290 USD [API] | `2026-10-28 16:25:44` |
| `ANNOUNCEMENT` | `INFO` | `59.03` | 20.66 USD | `-` | `NEWS_INTEL` | `-` | #LTC Liquidated Long: 0.02K USD at 59.0290 USD [API] | `2026-10-28 16:25:44` |
| `ANNOUNCEMENT` | `INFO` | `58.48` | 6,839.59 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 6.84K USD at 58.4830 USD [API] | `2026-10-28 17:30:23` |
| `ANNOUNCEMENT` | `INFO` | `58.49` | 5,232.43 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.23K USD at 58.4890 USD [API] | `2026-10-28 17:30:23` |
| `ANNOUNCEMENT` | `INFO` | `58.55` | 5,269.68 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.27K USD at 58.5520 USD [API] | `2026-10-28 17:40:25` |
| `ANNOUNCEMENT` | `INFO` | `58.13` | 7,507.30 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 58.1330 USD [API] | `2026-10-28 18:16:41` |
| `ANNOUNCEMENT` | `INFO` | `59.03` | 2,999.90 USD | `-` | `NEWS_INTEL` | `-` | #LTC Liquidated Long: 3.00K USD at 59.0300 USD [API] | `2026-10-28 16:25:44` |
| `ANNOUNCEMENT` | `INFO` | `58.46` | 7,506.46 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 58.4570 USD [API] | `2026-10-28 18:52:14` |
| `ANNOUNCEMENT` | `INFO` | `58.46` | 7,506.46 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 58.4570 USD [API] | `2026-10-28 18:52:14` |
| `ANNOUNCEMENT` | `INFO` | `58.46` | 5,364.51 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 5.36K USD at 58.4560 USD [API] | `2026-10-28 18:52:14` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.33%`) | Long MP=`54.26` (Vol: 204,200.00 USD, Dist: `--2.22%`)
  * 48H Horizon: Short MP=`58.99` (Vol: 284,700.00 USD, Dist: `+6.30%`) | Long MP=`54.29` (Vol: 204,200.00 USD, Dist: `--2.16%`)
  * 3D Horizon: Short MP=`58.99` (Vol: 284,700.00 USD, Dist: `+6.30%`) | Long MP=`54.29` (Vol: 204,200.00 USD, Dist: `--2.16%`)
  * 7D Horizon: Short MP=`58.99` (Vol: 284,700.00 USD, Dist: `+6.30%`) | Long MP=`54.29` (Vol: 204,200.00 USD, Dist: `--2.16%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `11.35` | 136.20 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `11.65` | 105.08 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.25` | 122.50 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.45` | 398.40 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.75` | 2,560.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.15` | 2,220.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.65` | 150.15 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `15.75` | 166.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `17.45` | 2,090.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.05` | 506.30 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.95` | 2,850.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.05` | 3,890.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.45` | 2,010.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.65` | 6,080.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.45` | 141.57 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.25` | 4,340.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.55` | 20,970.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.65` | 365.34 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.85` | 1,370.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.55` | 916.57 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.85` | 195.57 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.15` | 432.77 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.45` | 5,500.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 277,980.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 323.21 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 50,740.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 374.20 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.75` | 224.70 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.95` | 5,920.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 272.75 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 173.85 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.45` | 804.28 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 583.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.65` | 469.06 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 297,600.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 218.46 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 2,090.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 5,880.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.35` | 3,890.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 5,680.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 2,870.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 125.24 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 450.10 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.35` | 172.10 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.45` | 227.15 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 653.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 953.68 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 32,850.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.55` | 629.06 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 1,190.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.85` | 4,420.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 182.85 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 126.70 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.55` | 50,130.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 3,240.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 104.85 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 166.49 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.35` | 35,280.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.45` | 177.25 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 3,300.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 423.18 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 101.80 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.85` | 439.25 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 359.76 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 1,490.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 9,260.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 3,530.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 6,210.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 446.67 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.25` | 5,410.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 341.70 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 2,400.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 4,880.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 384.57 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 2,730.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 665,770.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 1,900.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 264.83 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 865.53 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 497.14 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 5,900.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 1,550.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 8,900.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 2,160.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 1,010.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 133.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 274.39 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.75` | 1,020.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 6,340.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 509.01 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 3,660.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 14,490.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.35` | 5,320.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 644.96 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.55` | 41,550.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 3,090.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 64,190.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 35,410.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.35` | 301.96 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 9,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 5,800.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 6,670.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 8,950.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 122,400.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 312.26 USD | 905,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 5,390.00 USD | 905,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 706.06 USD | 899,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 26,650.00 USD | 899,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 21,880.00 USD | 872,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 801.14 USD | 850,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 329.62 USD | 849,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 2,380.00 USD | 849,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 3,780.00 USD | 847,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 85,770.00 USD | 843,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 842.44 USD | 757,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 4,230.00 USD | 756,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 306.77 USD | 752,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 2,620.00 USD | 752,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 1,250.00 USD | 749,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 135.00 USD | 748,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 3,180.00 USD | 748,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 2,180.00 USD | 745,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 23,940.00 USD | 742,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 318.39 USD | 718,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 10,690.00 USD | 718,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.35` | 383.78 USD | 707,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 1,630.00 USD | 707,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 2,530.00 USD | 705,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 358.40 USD | 703,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 158.22 USD | 703,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.05` | 126.09 USD | 702,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 9,740.00 USD | 702,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 574.09 USD | 693,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.35` | 840.46 USD | 692,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.45` | 4,820.00 USD | 691,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 1,770.00 USD | 686,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 4,780.00 USD | 685,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 1,340.00 USD | 680,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 1,690.00 USD | 678,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 525.44 USD | 677,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 2,030.00 USD | 676,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 273.90 USD | 674,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 333.94 USD | 674,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 2,700.00 USD | 674,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,580.00 USD | 671,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.10` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 242.30 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,740.00 USD | 669,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.20` | 2,610,000.00 USD | 2,610,000.00 USD | 13,300.00 USD | 3,260.00 USD | 367.32 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.25` | 263.49 USD | 664,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.30` | 8,320,000.00 USD | 8,320,000.00 USD | 15,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.35` | 5,230.00 USD | 663,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.40` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 626.48 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.40` | 8,300,000.00 USD | 8,300,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.45` | 1,960.00 USD | 658,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.50` | 2,590,000.00 USD | 2,590,000.00 USD | 1,180.00 USD | 4,790.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.50` | 8,290,000.00 USD | 8,290,000.00 USD | 1,130.00 USD | 6,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.55` | 18,010.00 USD | 656,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.60` | 2,570,000.00 USD | 2,570,000.00 USD | 785.85 USD | 4,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.60` | 8,290,000.00 USD | 8,290,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.65` | 92,360.00 USD | 638,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.70` | 2,570,000.00 USD | 2,570,000.00 USD | 1,320.00 USD | 0.00 USD | 301.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.70` | 8,270,000.00 USD | 8,270,000.00 USD | 788.92 USD | 0.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.75` | 1,580.00 USD | 546,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.80` | 2,570,000.00 USD | 2,570,000.00 USD | 667.20 USD | 733.27 USD | 11,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.80` | 8,270,000.00 USD | 8,270,000.00 USD | 7,660.00 USD | 8,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `49.90` | 2,550,000.00 USD | 2,550,000.00 USD | 17,040.00 USD | 5,020.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.90` | 8,250,000.00 USD | 8,250,000.00 USD | 45,030.00 USD | 5,410.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.95` | 28,540.00 USD | 544,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.00` | 2,510,000.00 USD | 2,510,000.00 USD | 4,340.00 USD | 3,060.00 USD | 40,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.00` | 8,200,000.00 USD | 8,200,000.00 USD | 22,100.00 USD | 5,170.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.05` | 1,820.00 USD | 516,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.10` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 315.50 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.10` | 8,140,000.00 USD | 8,140,000.00 USD | 363.50 USD | 682.90 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.20` | 8,140,000.00 USD | 8,140,000.00 USD | 6,960.00 USD | 500.40 USD | 34,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.25` | 102.51 USD | 514,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.30` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 333.03 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.30` | 8,100,000.00 USD | 8,100,000.00 USD | 16,270.00 USD | 3,640.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.35` | 1,030.00 USD | 514,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.40` | 2,460,000.00 USD | 2,460,000.00 USD | 349.63 USD | 2,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.40` | 8,080,000.00 USD | 8,080,000.00 USD | 23,520.00 USD | 19,110.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,720.00 USD | 513,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.50` | 8,000,000.00 USD | 8,000,000.00 USD | 24,840.00 USD | 6,790.00 USD | 43,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.55` | 84,100.00 USD | 508,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.60` | 7,930,000.00 USD | 7,930,000.00 USD | 52,670.00 USD | 17,830.00 USD | 22,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.70` | 7,830,000.00 USD | 7,830,000.00 USD | 53,670.00 USD | 24,710.00 USD | 32,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.75` | 9,050.00 USD | 424,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.80` | 2,460,000.00 USD | 2,460,000.00 USD | 5,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.80` | 7,720,000.00 USD | 7,720,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.85` | 263.40 USD | 415,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.90` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 260.05 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.90` | 7,630,000.00 USD | 7,630,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.95` | 245.07 USD | 414,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.00` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 129.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.00` | 7,370,000.00 USD | 7,370,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.10` | 2,440,000.00 USD | 2,440,000.00 USD | 263.90 USD | 1,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.10` | 7,250,000.00 USD | 7,250,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.15` | 219,370.00 USD | 414,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.20` | 2,440,000.00 USD | 2,440,000.00 USD | 1,100.00 USD | 1,130.00 USD | 327.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.20` | 7,170,000.00 USD | 7,170,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.30` | 2,440,000.00 USD | 2,440,000.00 USD | 20,430.00 USD | 5,150.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.30` | 7,100,000.00 USD | 7,100,000.00 USD | 19,510.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.40` | 2,400,000.00 USD | 2,400,000.00 USD | 17,510.00 USD | 7,090.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.40` | 7,020,000.00 USD | 7,020,000.00 USD | 71,090.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.45` | 20,410.00 USD | 195,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.50` | 2,360,000.00 USD | 2,360,000.00 USD | 11,450.00 USD | 8,980.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.50` | 6,880,000.00 USD | 6,880,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.55` | 551.07 USD | 174,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.60` | 2,340,000.00 USD | 2,340,000.00 USD | 8,800.00 USD | 7,990.00 USD | 4,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.60` | 6,780,000.00 USD | 6,780,000.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.65` | 8,810.00 USD | 174,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.70` | 2,310,000.00 USD | 2,310,000.00 USD | 4,980.00 USD | 4,150.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.70` | 6,720,000.00 USD | 6,720,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.75` | 6,480.00 USD | 165,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.80` | 2,300,000.00 USD | 2,300,000.00 USD | 12,580.00 USD | 2,080.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.80` | 6,680,000.00 USD | 6,680,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.85` | 13,890.00 USD | 159,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.90` | 2,270,000.00 USD | 2,270,000.00 USD | 12,520.00 USD | 21,470.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.90` | 6,630,000.00 USD | 6,630,000.00 USD | 5,870.00 USD | 15,810.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.95` | 19,580.00 USD | 145,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.00` | 2,230,000.00 USD | 2,230,000.00 USD | 25,150.00 USD | 8,240.00 USD | 23,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.00` | 6,600,000.00 USD | 6,600,000.00 USD | 64,300.00 USD | 20,800.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.05` | 283.15 USD | 125,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.10` | 2,170,000.00 USD | 2,170,000.00 USD | 27,630.00 USD | 5,780.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 6,500,000.00 USD | 6,500,000.00 USD | 24,220.00 USD | 18,810.00 USD | 35,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.15` | 7,510.00 USD | 125,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.20` | 2,100,000.00 USD | 2,100,000.00 USD | 20,520.00 USD | 10,460.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 6,420,000.00 USD | 6,420,000.00 USD | 38,380.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.25` | 3,620.00 USD | 117,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.30` | 2,060,000.00 USD | 2,060,000.00 USD | 38,870.00 USD | 8,170.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 6,360,000.00 USD | 6,360,000.00 USD | 18,740.00 USD | 12,840.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.35` | 3,020.00 USD | 114,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.40` | 2,000,000.00 USD | 2,000,000.00 USD | 11,440.00 USD | 7,510.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 6,320,000.00 USD | 6,320,000.00 USD | 20,580.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.45` | 3,830.00 USD | 111,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.50` | 1,970,000.00 USD | 1,970,000.00 USD | 48,310.00 USD | 13,510.00 USD | 998.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.50` | 6,260,000.00 USD | 6,260,000.00 USD | 33,240.00 USD | 667.05 USD | 11,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.55` | 8,700.00 USD | 107,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.60` | 1,910,000.00 USD | 1,910,000.00 USD | 4,750.00 USD | 9,470.00 USD | 506.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.60` | 6,220,000.00 USD | 6,220,000.00 USD | 74,610.00 USD | 14,530.00 USD | 584.77 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.70` | 1,890,000.00 USD | 1,890,000.00 USD | 12,910.00 USD | 7,610.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.70` | 6,130,000.00 USD | 6,130,000.00 USD | 20,250.00 USD | 43,820.00 USD | 62,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.75` | 7,290.00 USD | 98,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.80` | 1,860,000.00 USD | 1,860,000.00 USD | 14,400.00 USD | 16,680.00 USD | 74,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.80` | 6,000,000.00 USD | 6,000,000.00 USD | 46,600.00 USD | 29,900.00 USD | 108.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.85` | 21,120.00 USD | 91,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.90` | 1,750,000.00 USD | 1,750,000.00 USD | 40,120.00 USD | 12,380.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.90` | 5,930,000.00 USD | 5,930,000.00 USD | 51,920.00 USD | 26,170.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.95` | 25,840.00 USD | 70,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.00` | 1,690,000.00 USD | 1,690,000.00 USD | 4,280.00 USD | 4,790.00 USD | 1,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.00` | 5,810,000.00 USD | 5,810,000.00 USD | 18,990.00 USD | 8,880.00 USD | 55,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.05` | 900.26 USD | 44,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.10` | 1,680,000.00 USD | 1,680,000.00 USD | 22,820.00 USD | 8,110.00 USD | 54,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.10` | 5,730,000.00 USD | 5,730,000.00 USD | 52,760.00 USD | 36,340.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.15` | 2,640.00 USD | 43,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.20` | 1,600,000.00 USD | 1,600,000.00 USD | 65,380.00 USD | 19,420.00 USD | 63,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.20` | 5,630,000.00 USD | 5,630,000.00 USD | 141,420.00 USD | 38,500.00 USD | 27,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.25` | 911.64 USD | 40,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.30` | 1,450,000.00 USD | 1,450,000.00 USD | 27,380.00 USD | 17,640.00 USD | 41,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.30` | 5,420,000.00 USD | 5,420,000.00 USD | 63,050.00 USD | 14,250.00 USD | 37,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.35` | 2,120.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.40` | 1,360,000.00 USD | 1,360,000.00 USD | 11,070.00 USD | 11,670.00 USD | 76,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.40` | 5,310,000.00 USD | 5,310,000.00 USD | 48,760.00 USD | 14,570.00 USD | 95,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.45` | 4,880.00 USD | 37,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.50` | 1,260,000.00 USD | 1,260,000.00 USD | 11,320.00 USD | 4,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.50` | 5,150,000.00 USD | 5,150,000.00 USD | 49,490.00 USD | 12,620.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.60` | 1,250,000.00 USD | 1,250,000.00 USD | 76,890.00 USD | 19,300.00 USD | 1,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.60` | 5,070,000.00 USD | 5,070,000.00 USD | 53,580.00 USD | 6,140.00 USD | 98,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.65` | 350.87 USD | 32,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.70` | 1,150,000.00 USD | 1,150,000.00 USD | 5,710.00 USD | 8,090.00 USD | 465.28 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.70` | 4,910,000.00 USD | 4,910,000.00 USD | 140,080.00 USD | 16,400.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.75` | 148.35 USD | 32,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.80` | 1,130,000.00 USD | 1,130,000.00 USD | 16,800.00 USD | 5,480.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.80` | 4,740,000.00 USD | 4,740,000.00 USD | 99,150.00 USD | 80,510.00 USD | 126,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.85` | 2,130.00 USD | 32,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.90` | 1,110,000.00 USD | 1,110,000.00 USD | 7,480.00 USD | 28,010.00 USD | 125,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.90` | 4,440,000.00 USD | 4,440,000.00 USD | 111,970.00 USD | 56,750.00 USD | 123,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.95` | 27,050.00 USD | 30,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.00` | 948,110.00 USD | 948,110.00 USD | 28,730.00 USD | 24,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.00` | 4,140,000.00 USD | 4,140,000.00 USD | 344,710.00 USD | 148,420.00 USD | 271,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.05` | 219.44 USD | 3,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.10` | 895,300.00 USD | 895,300.00 USD | 23,830.00 USD | 5,860.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.10` | 3,380,000.00 USD | 3,380,000.00 USD | 234,120.00 USD | 45,470.00 USD | 184,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.15` | 3,080.00 USD | 3,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.20` | 864,100.00 USD | 864,100.00 USD | 54,060.00 USD | 12,370.00 USD | 108,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.20` | 2,920,000.00 USD | 2,920,000.00 USD | 234,980.00 USD | 155,540.00 USD | 128,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.30` | 689,340.00 USD | 689,340.00 USD | 121,180.00 USD | 26,040.00 USD | 142,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.30` | 2,400,000.00 USD | 2,400,000.00 USD | 339,300.00 USD | 131,670.00 USD | 185,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.40` | 399,220.00 USD | 399,220.00 USD | 37,530.00 USD | 29,730.00 USD | 78,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.40` | 1,740,000.00 USD | 1,740,000.00 USD | 304,270.00 USD | 6,020.00 USD | 92,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.50` | 253,680.00 USD | 253,680.00 USD | 3,040.00 USD | 17,230.00 USD | 144,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.50` | 1,340,000.00 USD | 1,340,000.00 USD | 159,720.00 USD | 29,880.00 USD | 237,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.60` | 89,360.00 USD | 89,360.00 USD | 11,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.60` | 911,140.00 USD | 911,140.00 USD | 0.00 USD | 1,930.00 USD | 72,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.70` | 77,810.00 USD | 77,810.00 USD | 0.00 USD | 0.00 USD | 57,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.70` | 836,810.00 USD | 836,810.00 USD | 0.00 USD | 0.00 USD | 173,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.80` | 20,710.00 USD | 20,710.00 USD | 0.00 USD | 9,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.10` | 11,290.00 USD | 11,290.00 USD | 0.00 USD | 0.00 USD | 189.61 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.20` | 11,100.00 USD | 11,100.00 USD | 11,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.20` | 663,420.00 USD | 663,420.00 USD | 336,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.50` | 326,800.00 USD | 326,800.00 USD | 326,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.60` | 755.00 USD | 755.00 USD | 755.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.60` | 1,510.00 USD | 1,510.00 USD | 755.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.60` | 426,340.00 USD | 426,340.00 USD | 426,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.60` | 852,690.00 USD | 852,690.00 USD | 426,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.70` | 3,130.00 USD | 3,130.00 USD | 0.00 USD | 1,210.00 USD | 407.86 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.70` | 1,060,000.00 USD | 1,060,000.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.80` | 255,350.00 USD | 255,350.00 USD | 189,240.00 USD | 16,300.00 USD | 46,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.80` | 1,150,000.00 USD | 1,150,000.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.90` | 534,100.00 USD | 534,100.00 USD | 137,200.00 USD | 1,440.00 USD | 140,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.90` | 1,360,000.00 USD | 1,360,000.00 USD | 141,330.00 USD | 65,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.00` | 733,380.00 USD | 733,380.00 USD | 139,840.00 USD | 0.00 USD | 59,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.00` | 1,780,000.00 USD | 1,780,000.00 USD | 181,230.00 USD | 98,600.00 USD | 147,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.10` | 1,040,000.00 USD | 1,040,000.00 USD | 105,950.00 USD | 28,010.00 USD | 174,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.10` | 2,110,000.00 USD | 2,110,000.00 USD | 121,920.00 USD | 144,120.00 USD | 61,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.20` | 1,290,000.00 USD | 1,290,000.00 USD | 96,820.00 USD | 83,660.00 USD | 71,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.20` | 2,530,000.00 USD | 2,530,000.00 USD | 104,510.00 USD | 72,410.00 USD | 240,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.30` | 1,370,000.00 USD | 1,370,000.00 USD | 464.20 USD | 37,150.00 USD | 38,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.30` | 2,880,000.00 USD | 2,880,000.00 USD | 91,850.00 USD | 128,970.00 USD | 131,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.40` | 1,680,000.00 USD | 1,680,000.00 USD | 39,500.00 USD | 43,300.00 USD | 225,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.40` | 3,350,000.00 USD | 3,350,000.00 USD | 215,940.00 USD | 116,750.00 USD | 137,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.50` | 2,040,000.00 USD | 2,040,000.00 USD | 111,210.00 USD | 132,180.00 USD | 114,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.50` | 3,610,000.00 USD | 3,610,000.00 USD | 128,680.00 USD | 125,310.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.60` | 2,240,000.00 USD | 2,240,000.00 USD | 34,340.00 USD | 87,860.00 USD | 77,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.60` | 4,090,000.00 USD | 4,090,000.00 USD | 363,190.00 USD | 119,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.70` | 2,800,000.00 USD | 2,800,000.00 USD | 197,080.00 USD | 17,230.00 USD | 345,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.70` | 4,410,000.00 USD | 4,410,000.00 USD | 110,940.00 USD | 114,460.00 USD | 96,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.80` | 3,090,000.00 USD | 3,090,000.00 USD | 189,460.00 USD | 2,180.00 USD | 102,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.80` | 4,920,000.00 USD | 4,920,000.00 USD | 153,580.00 USD | 92,780.00 USD | 261,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.90` | 3,130,000.00 USD | 3,130,000.00 USD | 33,240.00 USD | 8,150.00 USD | 1,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.90` | 5,340,000.00 USD | 5,340,000.00 USD | 108,440.00 USD | 48,600.00 USD | 266,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.00` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 12,360.00 USD | 659.87 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.00` | 5,530,000.00 USD | 5,530,000.00 USD | 88,680.00 USD | 2,620.00 USD | 93,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.10` | 3,170,000.00 USD | 3,170,000.00 USD | 7,480.00 USD | 10,960.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.10` | 5,600,000.00 USD | 5,600,000.00 USD | 36,580.00 USD | 16,110.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.20` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 14,000.00 USD | 63,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.20` | 5,640,000.00 USD | 5,640,000.00 USD | 21,160.00 USD | 15,720.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.30` | 3,270,000.00 USD | 3,270,000.00 USD | 12,360.00 USD | 12,450.00 USD | 386.57 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.30` | 5,700,000.00 USD | 5,700,000.00 USD | 22,360.00 USD | 3,150.00 USD | 34,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.40` | 3,320,000.00 USD | 3,320,000.00 USD | 19,650.00 USD | 28,690.00 USD | 754.29 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.40` | 5,920,000.00 USD | 5,920,000.00 USD | 38,520.00 USD | 30,000.00 USD | 153,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.50` | 3,560,000.00 USD | 3,560,000.00 USD | 128,210.00 USD | 19,060.00 USD | 90,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.50` | 6,030,000.00 USD | 6,030,000.00 USD | 76,670.00 USD | 30,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.60` | 3,690,000.00 USD | 3,690,000.00 USD | 55,610.00 USD | 13,020.00 USD | 57,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.60` | 6,220,000.00 USD | 6,220,000.00 USD | 123,760.00 USD | 36,020.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.70` | 3,830,000.00 USD | 3,830,000.00 USD | 28,040.00 USD | 16,170.00 USD | 96,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.70` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 1,500.00 USD | 57,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.80` | 3,910,000.00 USD | 3,910,000.00 USD | 2,360.00 USD | 8,620.00 USD | 72,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.80` | 6,340,000.00 USD | 6,340,000.00 USD | 2,260.00 USD | 10,840.00 USD | 48,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.90` | 3,920,000.00 USD | 3,920,000.00 USD | 6,090.00 USD | 6,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.90` | 6,340,000.00 USD | 6,340,000.00 USD | 2,410.00 USD | 963.90 USD | 1,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.95` | 978.20 USD | 978.20 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.00` | 3,930,000.00 USD | 3,930,000.00 USD | 3,570.00 USD | 5,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.00` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 3,670.00 USD | 86,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.10` | 3,980,000.00 USD | 3,980,000.00 USD | 29,450.00 USD | 6,730.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.10` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 1,310.00 USD | 848.40 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `58.15` | 199,650.00 USD | 200,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.20` | 3,990,000.00 USD | 3,990,000.00 USD | 1,980.00 USD | 5,880.00 USD | 350.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.30` | 4,040,000.00 USD | 4,040,000.00 USD | 9,430.00 USD | 11,540.00 USD | 36,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.30` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 9,580.00 USD | 26,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.40` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 4,990.00 USD | 33,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.40` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 0.00 USD | 54,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.50` | 4,150,000.00 USD | 4,150,000.00 USD | 48,820.00 USD | 21,280.00 USD | 379.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.50` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.60` | 6,550,000.00 USD | 6,550,000.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.70` | 4,180,000.00 USD | 4,180,000.00 USD | 15,850.00 USD | 8,070.00 USD | 355.85 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.70` | 6,600,000.00 USD | 6,600,000.00 USD | 1,700.00 USD | 5,910.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `58.75` | 213.26 USD | 200,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.80` | 4,250,000.00 USD | 4,250,000.00 USD | 35,140.00 USD | 14,730.00 USD | 23,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.80` | 6,610,000.00 USD | 6,610,000.00 USD | 1,810.00 USD | 3,320.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.90` | 4,490,000.00 USD | 4,490,000.00 USD | 19,290.00 USD | 124,640.00 USD | 91,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.90` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 48,700.00 USD | 83,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.00` | 4,830,000.00 USD | 4,830,000.00 USD | 151,460.00 USD | 57,130.00 USD | 134,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.00` | 7,180,000.00 USD | 7,180,000.00 USD | 255,180.00 USD | 65,270.00 USD | 118,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.05` | 213.76 USD | 201,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.10` | 5,260,000.00 USD | 5,260,000.00 USD | 191,140.00 USD | 49,070.00 USD | 186,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.10` | 7,470,000.00 USD | 7,470,000.00 USD | 91,060.00 USD | 45,400.00 USD | 158,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.20` | 5,590,000.00 USD | 5,590,000.00 USD | 158,790.00 USD | 75,750.00 USD | 96,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.20` | 7,810,000.00 USD | 7,810,000.00 USD | 153,580.00 USD | 12,460.00 USD | 174,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.30` | 6,110,000.00 USD | 6,110,000.00 USD | 306,360.00 USD | 73,700.00 USD | 143,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.30` | 8,090,000.00 USD | 8,090,000.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.35` | 9,440.00 USD | 210,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.40` | 6,320,000.00 USD | 6,320,000.00 USD | 78,510.00 USD | 57,010.00 USD | 76,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.40` | 8,400,000.00 USD | 8,400,000.00 USD | 103,370.00 USD | 73,620.00 USD | 137,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.50` | 6,530,000.00 USD | 6,530,000.00 USD | 119,350.00 USD | 57,690.00 USD | 28,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.50` | 8,560,000.00 USD | 8,560,000.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.60` | 6,680,000.00 USD | 6,680,000.00 USD | 62,780.00 USD | 68,870.00 USD | 18,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.60` | 9,060,000.00 USD | 9,060,000.00 USD | 268,680.00 USD | 145,550.00 USD | 86,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.70` | 6,820,000.00 USD | 6,820,000.00 USD | 20,820.00 USD | 30,890.00 USD | 94,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.70` | 9,460,000.00 USD | 9,460,000.00 USD | 55,510.00 USD | 180,620.00 USD | 161,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.80` | 6,910,000.00 USD | 6,910,000.00 USD | 40,970.00 USD | 37,360.00 USD | 10,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.80` | 9,830,000.00 USD | 9,830,000.00 USD | 118,240.00 USD | 97,600.00 USD | 155,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.90` | 7,130,000.00 USD | 7,130,000.00 USD | 112,870.00 USD | 21,300.00 USD | 80,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.90` | 10,200,000.00 USD | 10,200,000.00 USD | 246,770.00 USD | 84,430.00 USD | 40,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.00` | 7,440,000.00 USD | 7,440,000.00 USD | 182,880.00 USD | 64,320.00 USD | 69,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.00` | 10,710,000.00 USD | 10,710,000.00 USD | 231,370.00 USD | 183,130.00 USD | 94,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.05` | 217.98 USD | 210,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.10` | 7,650,000.00 USD | 7,650,000.00 USD | 95,780.00 USD | 40,330.00 USD | 71,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.10` | 11,280,000.00 USD | 11,280,000.00 USD | 263,890.00 USD | 129,860.00 USD | 174,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.20` | 7,900,000.00 USD | 7,900,000.00 USD | 119,070.00 USD | 37,570.00 USD | 96,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.20` | 11,770,000.00 USD | 11,770,000.00 USD | 207,990.00 USD | 131,530.00 USD | 157,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.30` | 8,160,000.00 USD | 8,160,000.00 USD | 97,720.00 USD | 71,550.00 USD | 82,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.30` | 12,160,000.00 USD | 12,160,000.00 USD | 133,350.00 USD | 95,890.00 USD | 155,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.35` | 218.47 USD | 210,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.40` | 8,430,000.00 USD | 8,430,000.00 USD | 168,700.00 USD | 45,820.00 USD | 60,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.40` | 12,610,000.00 USD | 12,610,000.00 USD | 93,890.00 USD | 133,310.00 USD | 226,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.50` | 8,610,000.00 USD | 8,610,000.00 USD | 69,310.00 USD | 43,330.00 USD | 63,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.50` | 13,040,000.00 USD | 13,040,000.00 USD | 131,870.00 USD | 86,290.00 USD | 206,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.60` | 8,720,000.00 USD | 8,720,000.00 USD | 69,460.00 USD | 36,940.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.60` | 13,490,000.00 USD | 13,490,000.00 USD | 251,100.00 USD | 70,980.00 USD | 134,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.70` | 8,810,000.00 USD | 8,810,000.00 USD | 56,630.00 USD | 36,190.00 USD | 985.52 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.70` | 13,720,000.00 USD | 13,720,000.00 USD | 129,660.00 USD | 67,510.00 USD | 28,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.80` | 8,900,000.00 USD | 8,900,000.00 USD | 22,530.00 USD | 12,680.00 USD | 55,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.80` | 13,950,000.00 USD | 13,950,000.00 USD | 54,870.00 USD | 78,710.00 USD | 94,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.90` | 9,010,000.00 USD | 9,010,000.00 USD | 57,090.00 USD | 23,580.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.90` | 14,260,000.00 USD | 14,260,000.00 USD | 160,150.00 USD | 58,270.00 USD | 93,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.00` | 9,090,000.00 USD | 9,090,000.00 USD | 46,000.00 USD | 6,970.00 USD | 28,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 14,400,000.00 USD | 14,400,000.00 USD | 96,160.00 USD | 36,500.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.10` | 9,110,000.00 USD | 9,110,000.00 USD | 10,450.00 USD | 3,060.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 14,430,000.00 USD | 14,430,000.00 USD | 31,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.15` | 3,870.00 USD | 214,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.20` | 9,240,000.00 USD | 9,240,000.00 USD | 75,930.00 USD | 1,160.00 USD | 47,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.20` | 14,670,000.00 USD | 14,670,000.00 USD | 116,610.00 USD | 74,510.00 USD | 52,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.30` | 9,260,000.00 USD | 9,260,000.00 USD | 9,540.00 USD | 6,080.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.30` | 14,810,000.00 USD | 14,810,000.00 USD | 51,130.00 USD | 35,650.00 USD | 55,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.40` | 9,270,000.00 USD | 9,270,000.00 USD | 6,350.00 USD | 5,640.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.40` | 15,000,000.00 USD | 15,000,000.00 USD | 89,350.00 USD | 41,800.00 USD | 59,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.50` | 9,310,000.00 USD | 9,310,000.00 USD | 9,120.00 USD | 18,030.00 USD | 17,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.50` | 15,100,000.00 USD | 15,100,000.00 USD | 19,810.00 USD | 35,300.00 USD | 36,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.60` | 9,360,000.00 USD | 9,360,000.00 USD | 24,180.00 USD | 10,780.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.60` | 15,350,000.00 USD | 15,350,000.00 USD | 54,240.00 USD | 63,390.00 USD | 132,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.70` | 9,410,000.00 USD | 9,410,000.00 USD | 31,820.00 USD | 9,670.00 USD | 12,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.70` | 15,560,000.00 USD | 15,560,000.00 USD | 84,300.00 USD | 11,330.00 USD | 114,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.80` | 9,440,000.00 USD | 9,440,000.00 USD | 18,210.00 USD | 8,420.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.80` | 15,830,000.00 USD | 15,830,000.00 USD | 160,110.00 USD | 48,140.00 USD | 69,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.90` | 9,470,000.00 USD | 9,470,000.00 USD | 19,520.00 USD | 7,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.90` | 15,970,000.00 USD | 15,970,000.00 USD | 72,380.00 USD | 29,730.00 USD | 35,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.00` | 9,490,000.00 USD | 9,490,000.00 USD | 14,630.00 USD | 911.46 USD | 2,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.00` | 16,090,000.00 USD | 16,090,000.00 USD | 56,450.00 USD | 13,260.00 USD | 49,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.10` | 9,500,000.00 USD | 9,500,000.00 USD | 12,050.00 USD | 945.47 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.10` | 16,150,000.00 USD | 16,150,000.00 USD | 36,500.00 USD | 12,820.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.20` | 9,500,000.00 USD | 9,500,000.00 USD | 3,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.20` | 16,270,000.00 USD | 16,270,000.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.30` | 9,510,000.00 USD | 9,510,000.00 USD | 464.20 USD | 260.05 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.30` | 16,420,000.00 USD | 16,420,000.00 USD | 33,560.00 USD | 23,450.00 USD | 97,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.40` | 9,510,000.00 USD | 9,510,000.00 USD | 974.27 USD | 0.00 USD | 129.78 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.40` | 16,560,000.00 USD | 16,560,000.00 USD | 79,620.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.50` | 9,510,000.00 USD | 9,510,000.00 USD | 263.90 USD | 1,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.50` | 16,650,000.00 USD | 16,650,000.00 USD | 44,300.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.60` | 9,520,000.00 USD | 9,520,000.00 USD | 1,100.00 USD | 1,130.00 USD | 327.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.60` | 16,720,000.00 USD | 16,720,000.00 USD | 34,910.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `62.65` | 142.84 USD | 214,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `62.70` | 9,560,000.00 USD | 9,560,000.00 USD | 18,660.00 USD | 5,150.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.70` | 16,800,000.00 USD | 16,800,000.00 USD | 22,020.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.80` | 9,590,000.00 USD | 9,590,000.00 USD | 16,430.00 USD | 7,090.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.80` | 16,950,000.00 USD | 16,950,000.00 USD | 72,250.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.90` | 9,610,000.00 USD | 9,610,000.00 USD | 8,780.00 USD | 8,980.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.90` | 17,040,000.00 USD | 17,040,000.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.00` | 9,630,000.00 USD | 9,630,000.00 USD | 7,800.00 USD | 7,990.00 USD | 4,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.00` | 17,100,000.00 USD | 17,100,000.00 USD | 34,730.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.10` | 9,650,000.00 USD | 9,650,000.00 USD | 4,260.00 USD | 4,150.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.10` | 17,140,000.00 USD | 17,140,000.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.20` | 9,650,000.00 USD | 9,650,000.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `63.25` | 1,330.00 USD | 216,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `63.30` | 9,660,000.00 USD | 9,660,000.00 USD | 4,590.00 USD | 594.25 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.30` | 17,180,000.00 USD | 17,180,000.00 USD | 18,390.00 USD | 11,500.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.40` | 9,670,000.00 USD | 9,670,000.00 USD | 6,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.40` | 17,210,000.00 USD | 17,210,000.00 USD | 13,220.00 USD | 1,320.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.50` | 17,230,000.00 USD | 17,230,000.00 USD | 6,620.00 USD | 15,810.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.60` | 17,330,000.00 USD | 17,330,000.00 USD | 63,480.00 USD | 20,800.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.70` | 17,410,000.00 USD | 17,410,000.00 USD | 21,940.00 USD | 18,810.00 USD | 35,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.80` | 17,470,000.00 USD | 17,470,000.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.90` | 17,500,000.00 USD | 17,500,000.00 USD | 7,650.00 USD | 12,840.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.00` | 17,540,000.00 USD | 17,540,000.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.10` | 17,570,000.00 USD | 17,570,000.00 USD | 20,350.00 USD | 667.05 USD | 10,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.20` | 17,620,000.00 USD | 17,620,000.00 USD | 28,840.00 USD | 14,530.00 USD | 584.77 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.40` | 17,670,000.00 USD | 17,670,000.00 USD | 2,540.00 USD | 20,590.00 USD | 29,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.50` | 17,700,000.00 USD | 17,700,000.00 USD | 7,700.00 USD | 7,120.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.60` | 17,740,000.00 USD | 17,740,000.00 USD | 32,220.00 USD | 14,180.00 USD | 108.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.70` | 17,810,000.00 USD | 17,810,000.00 USD | 39,430.00 USD | 23,030.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.80` | 17,850,000.00 USD | 17,850,000.00 USD | 7,540.00 USD | 8,210.00 USD | 20,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.90` | 17,890,000.00 USD | 17,890,000.00 USD | 25,320.00 USD | 8,010.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.00` | 17,910,000.00 USD | 17,910,000.00 USD | 1,790.00 USD | 9,480.00 USD | 13,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.10` | 17,970,000.00 USD | 17,970,000.00 USD | 5,810.00 USD | 14,250.00 USD | 37,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.20` | 18,010,000.00 USD | 18,010,000.00 USD | 10,380.00 USD | 1,630.00 USD | 28,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `65.25` | 186.61 USD | 216,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `65.30` | 18,060,000.00 USD | 18,060,000.00 USD | 22,330.00 USD | 9,180.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `65.35` | 150.96 USD | 216,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.85` | 33,950.00 USD | 250,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.95` | 121.18 USD | 250,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.85` | 709.03 USD | 251,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `68.95` | 449.55 USD | 251,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `70.45` | 4,530.00 USD | 256,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `71.35` | 348.19 USD | 256,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `74.45` | 19,860.00 USD | 276,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `75.45` | 260.30 USD | 276,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `76.35` | 8,380.00 USD | 285,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.85` | 602.56 USD | 285,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.95` | 136.41 USD | 285,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `79.75` | 728.12 USD | 286,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.75` | 646.00 USD | 287,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.05` | 19,000.00 USD | 306,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.55` | 123.96 USD | 306,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.65` | 3,850.00 USD | 310,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.75` | 214.32 USD | 310,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `83.05` | 3,320.00 USD | 313,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `83.95` | 2,770.00 USD | 316,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `84.65` | 862.58 USD | 317,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `91.25` | 969.99 USD | 318,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `91.95` | 121.37 USD | 318,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.45` | 2,460.00 USD | 321,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.15` | 711.34 USD | 321,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.35` | 216.00 USD | 321,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.45` | 355,790.00 USD | 677,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.45` | 131.44 USD | 677,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.55` | 1,120.00 USD | 679,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `11.35` | 2,810,000.00 USD | 0.00 USD | 136.20 USD | `-79.47%` | `12.00` |
| `Live` | `Long` | `11.65` | 2,810,000.00 USD | 0.00 USD | 105.08 USD | `-78.93%` | `9.02` |
| `Live` | `Long` | `12.25` | 2,810,000.00 USD | 0.00 USD | 122.50 USD | `-77.85%` | `10.00` |
| `Live` | `Long` | `12.45` | 2,810,000.00 USD | 0.00 USD | 398.40 USD | `-77.48%` | `32.00` |
| `Live` | `Long` | `12.75` | 2,810,000.00 USD | 0.00 USD | 2,560.00 USD | `-76.94%` | `200.43` |
| `Live` | `Long` | `13.15` | 2,810,000.00 USD | 0.00 USD | 2,220.00 USD | `-76.22%` | `168.79` |
| `Live` | `Long` | `13.65` | 2,810,000.00 USD | 0.00 USD | 150.15 USD | `-75.31%` | `11.00` |
| `Live` | `Long` | `15.75` | 2,800,000.00 USD | 0.00 USD | 166.00 USD | `-71.52%` | `10.54` |
| `Live` | `Long` | `17.45` | 2,800,000.00 USD | 0.00 USD | 2,090.00 USD | `-68.44%` | `120.00` |
| `Live` | `Long` | `18.05` | 2,800,000.00 USD | 0.00 USD | 506.30 USD | `-67.36%` | `28.05` |
| `Live` | `Long` | `18.95` | 2,800,000.00 USD | 0.00 USD | 2,850.00 USD | `-65.73%` | `150.57` |
| `Live` | `Long` | `19.05` | 2,800,000.00 USD | 0.00 USD | 3,890.00 USD | `-65.55%` | `204.24` |
| `Live` | `Long` | `19.45` | 2,800,000.00 USD | 0.00 USD | 2,010.00 USD | `-64.83%` | `103.47` |
| `Live` | `Long` | `20.65` | 2,790,000.00 USD | 0.00 USD | 6,080.00 USD | `-62.66%` | `294.67` |
| `Live` | `Long` | `21.45` | 2,790,000.00 USD | 0.00 USD | 141.57 USD | `-61.21%` | `6.60` |
| `Live` | `Long` | `22.25` | 2,790,000.00 USD | 0.00 USD | 4,340.00 USD | `-59.76%` | `195.03` |
| `Live` | `Long` | `22.55` | 2,780,000.00 USD | 0.00 USD | 20,970.00 USD | `-59.22%` | `930.00` |
| `Live` | `Long` | `22.65` | 2,760,000.00 USD | 0.00 USD | 365.34 USD | `-59.04%` | `16.13` |
| `Live` | `Long` | `22.85` | 2,760,000.00 USD | 0.00 USD | 1,370.00 USD | `-58.68%` | `60.00` |
| `Live` | `Long` | `23.55` | 2,760,000.00 USD | 0.00 USD | 916.57 USD | `-57.41%` | `38.92` |
| `Live` | `Long` | `23.85` | 2,760,000.00 USD | 0.00 USD | 195.57 USD | `-56.87%` | `8.20` |
| `Live` | `Long` | `24.15` | 2,760,000.00 USD | 0.00 USD | 432.77 USD | `-56.33%` | `17.92` |
| `Live` | `Long` | `24.45` | 2,760,000.00 USD | 0.00 USD | 5,500.00 USD | `-55.78%` | `225.00` |
| `Live` | `Long` | `25.25` | 2,750,000.00 USD | 0.00 USD | 277,980.00 USD | `-54.34%` | `11,009.19` |
| `Live` | `Long` | `25.35` | 2,480,000.00 USD | 0.00 USD | 323.21 USD | `-54.16%` | `12.75` |
| `Live` | `Long` | `25.55` | 2,470,000.00 USD | 0.00 USD | 50,740.00 USD | `-53.79%` | `1,985.99` |
| `Live` | `Long` | `25.95` | 2,420,000.00 USD | 0.00 USD | 374.20 USD | `-53.07%` | `14.42` |
| `Live` | `Long` | `26.75` | 2,420,000.00 USD | 0.00 USD | 224.70 USD | `-51.62%` | `8.40` |
| `Live` | `Long` | `26.95` | 2,420,000.00 USD | 0.00 USD | 5,920.00 USD | `-51.26%` | `219.73` |
| `Live` | `Long` | `27.55` | 2,420,000.00 USD | 0.00 USD | 272.75 USD | `-50.18%` | `9.90` |
| `Live` | `Long` | `27.95` | 2,420,000.00 USD | 0.00 USD | 173.85 USD | `-49.45%` | `6.22` |
| `Live` | `Long` | `28.45` | 2,420,000.00 USD | 0.00 USD | 804.28 USD | `-48.55%` | `28.27` |
| `Live` | `Long` | `29.15` | 2,420,000.00 USD | 0.00 USD | 583.00 USD | `-47.28%` | `20.00` |
| `Live` | `Long` | `29.65` | 2,420,000.00 USD | 0.00 USD | 469.06 USD | `-46.38%` | `15.82` |
| `Live` | `Long` | `29.75` | 2,420,000.00 USD | 0.00 USD | 297,600.00 USD | `-46.20%` | `10,003.44` |
| `Live` | `Long` | `30.05` | 2,120,000.00 USD | 0.00 USD | 218.46 USD | `-45.66%` | `7.27` |
| `Live` | `Long` | `30.95` | 2,120,000.00 USD | 0.00 USD | 2,090.00 USD | `-44.03%` | `67.40` |
| `Live` | `Long` | `31.15` | 2,120,000.00 USD | 0.00 USD | 5,880.00 USD | `-43.67%` | `188.85` |
| `Live` | `Long` | `31.35` | 2,110,000.00 USD | 0.00 USD | 3,890.00 USD | `-43.31%` | `124.01` |
| `Live` | `Long` | `31.55` | 2,110,000.00 USD | 0.00 USD | 5,680.00 USD | `-42.94%` | `180.02` |
| `Live` | `Long` | `31.85` | 2,100,000.00 USD | 0.00 USD | 2,870.00 USD | `-42.40%` | `90.00` |
| `Live` | `Long` | `31.95` | 2,100,000.00 USD | 0.00 USD | 125.24 USD | `-42.22%` | `3.92` |
| `Live` | `Long` | `32.15` | 2,100,000.00 USD | 0.00 USD | 450.10 USD | `-41.86%` | `14.00` |
| `Live` | `Long` | `32.35` | 2,100,000.00 USD | 0.00 USD | 172.10 USD | `-41.50%` | `5.32` |
| `Live` | `Long` | `32.45` | 2,100,000.00 USD | 0.00 USD | 227.15 USD | `-41.32%` | `7.00` |
| `Live` | `Long` | `32.65` | 2,100,000.00 USD | 0.00 USD | 653.00 USD | `-40.95%` | `20.00` |
| `Live` | `Long` | `32.75` | 2,100,000.00 USD | 0.00 USD | 953.68 USD | `-40.77%` | `29.12` |
| `Live` | `Long` | `32.85` | 2,090,000.00 USD | 0.00 USD | 32,850.00 USD | `-40.59%` | `1,000.01` |
| `Live` | `Long` | `33.55` | 2,060,000.00 USD | 0.00 USD | 629.06 USD | `-39.33%` | `18.75` |
| `Live` | `Long` | `33.65` | 2,060,000.00 USD | 0.00 USD | 1,190.00 USD | `-39.15%` | `35.37` |
| `Live` | `Long` | `33.85` | 2,060,000.00 USD | 0.00 USD | 4,420.00 USD | `-38.78%` | `130.63` |
| `Live` | `Long` | `34.05` | 2,060,000.00 USD | 0.00 USD | 182.85 USD | `-38.42%` | `5.37` |
| `Live` | `Long` | `34.15` | 2,060,000.00 USD | 0.00 USD | 126.70 USD | `-38.24%` | `3.71` |
| `Live` | `Long` | `34.55` | 2,050,000.00 USD | 0.00 USD | 50,130.00 USD | `-37.52%` | `1,451.04` |
| `Live` | `Long` | `34.65` | 2,000,000.00 USD | 0.00 USD | 3,240.00 USD | `-37.34%` | `93.56` |
| `Live` | `Long` | `34.95` | 2,000,000.00 USD | 0.00 USD | 104.85 USD | `-36.79%` | `3.00` |
| `Live` | `Long` | `35.05` | 2,000,000.00 USD | 0.00 USD | 166.49 USD | `-36.61%` | `4.75` |
| `Live` | `Long` | `35.35` | 2,000,000.00 USD | 0.00 USD | 35,280.00 USD | `-36.07%` | `997.95` |
| `Live` | `Long` | `35.45` | 1,970,000.00 USD | 0.00 USD | 177.25 USD | `-35.89%` | `5.00` |
| `Live` | `Long` | `36.35` | 1,970,000.00 USD | 0.00 USD | 3,300.00 USD | `-34.26%` | `90.86` |
| `Live` | `Long` | `36.45` | 1,960,000.00 USD | 0.00 USD | 423.18 USD | `-34.08%` | `11.61` |
| `Live` | `Long` | `36.75` | 1,960,000.00 USD | 0.00 USD | 101.80 USD | `-33.54%` | `2.77` |
| `Live` | `Long` | `36.85` | 1,960,000.00 USD | 0.00 USD | 439.25 USD | `-33.36%` | `11.92` |
| `Live` | `Long` | `37.05` | 1,960,000.00 USD | 0.00 USD | 359.76 USD | `-33.00%` | `9.71` |
| `Live` | `Long` | `37.15` | 1,960,000.00 USD | 0.00 USD | 1,490.00 USD | `-32.82%` | `40.08` |
| `Live` | `Long` | `37.35` | 1,960,000.00 USD | 0.00 USD | 9,260.00 USD | `-32.45%` | `247.91` |
| `Live` | `Long` | `37.55` | 1,950,000.00 USD | 0.00 USD | 3,530.00 USD | `-32.09%` | `94.04` |
| `Live` | `Long` | `37.85` | 1,950,000.00 USD | 0.00 USD | 6,210.00 USD | `-31.55%` | `164.03` |
| `Live` | `Long` | `37.95` | 1,940,000.00 USD | 0.00 USD | 446.67 USD | `-31.37%` | `11.77` |
| `Live` | `Long` | `38.25` | 1,940,000.00 USD | 0.00 USD | 5,410.00 USD | `-30.83%` | `141.41` |
| `Live` | `Long` | `38.35` | 1,930,000.00 USD | 0.00 USD | 341.70 USD | `-30.65%` | `8.91` |
| `Live` | `Long` | `38.45` | 1,930,000.00 USD | 0.00 USD | 2,400.00 USD | `-30.47%` | `62.34` |
| `Live` | `Long` | `38.55` | 1,930,000.00 USD | 0.00 USD | 4,880.00 USD | `-30.28%` | `126.57` |
| `Live` | `Long` | `38.65` | 1,930,000.00 USD | 0.00 USD | 384.57 USD | `-30.10%` | `9.95` |
| `Live` | `Long` | `38.95` | 1,930,000.00 USD | 0.00 USD | 2,730.00 USD | `-29.56%` | `70.00` |
| `Live` | `Long` | `39.05` | 1,920,000.00 USD | 0.00 USD | 665,770.00 USD | `-29.38%` | `17,049.28` |
| `Live` | `Long` | `39.15` | 1,260,000.00 USD | 0.00 USD | 1,900.00 USD | `-29.20%` | `48.50` |
| `Live` | `Long` | `39.35` | 1,260,000.00 USD | 0.00 USD | 264.83 USD | `-28.84%` | `6.73` |
| `Live` | `Long` | `39.45` | 1,260,000.00 USD | 0.00 USD | 865.53 USD | `-28.66%` | `21.94` |
| `Live` | `Long` | `39.55` | 1,260,000.00 USD | 0.00 USD | 497.14 USD | `-28.48%` | `12.57` |
| `Live` | `Long` | `39.65` | 1,250,000.00 USD | 0.00 USD | 5,900.00 USD | `-28.29%` | `148.78` |
| `Live` | `Long` | `39.75` | 1,250,000.00 USD | 0.00 USD | 1,550.00 USD | `-28.11%` | `38.90` |
| `Live` | `Long` | `39.85` | 1,250,000.00 USD | 0.00 USD | 8,900.00 USD | `-27.93%` | `223.34` |
| `Live` | `Long` | `40.05` | 1,240,000.00 USD | 0.00 USD | 2,160.00 USD | `-27.57%` | `53.97` |
| `Live` | `Long` | `40.45` | 1,240,000.00 USD | 0.00 USD | 1,010.00 USD | `-26.85%` | `24.92` |
| `Live` | `Long` | `40.55` | 1,240,000.00 USD | 0.00 USD | 133.00 USD | `-26.67%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,240,000.00 USD | 0.00 USD | 274.39 USD | `-26.49%` | `6.75` |
| `Live` | `Long` | `40.75` | 1,230,000.00 USD | 0.00 USD | 1,020.00 USD | `-26.31%` | `24.93` |
| `Live` | `Long` | `40.85` | 1,230,000.00 USD | 0.00 USD | 6,340.00 USD | `-26.12%` | `155.23` |
| `Live` | `Long` | `40.95` | 1,230,000.00 USD | 0.00 USD | 509.01 USD | `-25.94%` | `12.43` |
| `Live` | `Long` | `41.05` | 1,230,000.00 USD | 0.00 USD | 3,660.00 USD | `-25.76%` | `89.15` |
| `Live` | `Long` | `41.25` | 1,220,000.00 USD | 0.00 USD | 14,490.00 USD | `-25.40%` | `351.26` |
| `Live` | `Long` | `41.35` | 1,210,000.00 USD | 0.00 USD | 5,320.00 USD | `-25.22%` | `128.71` |
| `Live` | `Long` | `41.45` | 1,200,000.00 USD | 0.00 USD | 644.96 USD | `-25.04%` | `15.56` |
| `Live` | `Long` | `41.55` | 1,200,000.00 USD | 0.00 USD | 41,550.00 USD | `-24.86%` | `1,000.00` |
| `Live` | `Long` | `42.05` | 1,160,000.00 USD | 0.00 USD | 3,090.00 USD | `-23.95%` | `73.52` |
| `Live` | `Long` | `42.15` | 1,160,000.00 USD | 0.00 USD | 64,190.00 USD | `-23.77%` | `1,522.78` |
| `Live` | `Long` | `42.25` | 1,090,000.00 USD | 0.00 USD | 35,410.00 USD | `-23.59%` | `838.00` |
| `Live` | `Long` | `42.35` | 1,060,000.00 USD | 0.00 USD | 301.96 USD | `-23.41%` | `7.13` |
| `Live` | `Long` | `42.65` | 1,060,000.00 USD | 0.00 USD | 9,000.00 USD | `-22.87%` | `210.92` |
| `Live` | `Long` | `42.85` | 1,050,000.00 USD | 0.00 USD | 5,800.00 USD | `-22.51%` | `135.38` |
| `Live` | `Long` | `42.95` | 1,040,000.00 USD | 0.00 USD | 6,670.00 USD | `-22.33%` | `155.25` |
| `Live` | `Long` | `43.05` | 1,040,000.00 USD | 0.00 USD | 8,950.00 USD | `-22.15%` | `208.00` |
| `Live` | `Long` | `43.15` | 1,030,000.00 USD | 0.00 USD | 122,400.00 USD | `-21.97%` | `2,836.59` |
| `Live` | `Long` | `43.25` | 905,610.00 USD | 0.00 USD | 312.26 USD | `-21.78%` | `7.22` |
| `Live` | `Long` | `43.35` | 905,300.00 USD | 0.00 USD | 5,390.00 USD | `-21.60%` | `124.24` |
| `Live` | `Long` | `43.45` | 899,920.00 USD | 0.00 USD | 706.06 USD | `-21.42%` | `16.25` |
| `Live` | `Long` | `43.65` | 899,210.00 USD | 0.00 USD | 26,650.00 USD | `-21.06%` | `610.44` |
| `Live` | `Long` | `43.75` | 872,560.00 USD | 0.00 USD | 21,880.00 USD | `-20.88%` | `500.00` |
| `Live` | `Long` | `43.85` | 850,690.00 USD | 0.00 USD | 801.14 USD | `-20.70%` | `18.27` |
| `Live` | `Long` | `43.95` | 849,890.00 USD | 0.00 USD | 329.62 USD | `-20.52%` | `7.50` |
| `Live` | `Long` | `44.15` | 849,560.00 USD | 0.00 USD | 2,380.00 USD | `-20.16%` | `53.99` |
| `Live` | `Long` | `44.25` | 847,170.00 USD | 0.00 USD | 3,780.00 USD | `-19.98%` | `85.43` |
| `Live` | `Long` | `44.35` | 843,390.00 USD | 0.00 USD | 85,770.00 USD | `-19.80%` | `1,933.87` |
| `Live` | `Long` | `44.55` | 757,630.00 USD | 0.00 USD | 842.44 USD | `-19.43%` | `18.91` |
| `Live` | `Long` | `44.75` | 756,780.00 USD | 0.00 USD | 4,230.00 USD | `-19.07%` | `94.55` |
| `Live` | `Long` | `44.85` | 752,550.00 USD | 0.00 USD | 306.77 USD | `-18.89%` | `6.84` |
| `Live` | `Long` | `44.95` | 752,250.00 USD | 0.00 USD | 2,620.00 USD | `-18.71%` | `58.18` |
| `Live` | `Long` | `45.05` | 749,630.00 USD | 0.00 USD | 1,250.00 USD | `-18.53%` | `27.70` |
| `Live` | `Long` | `45.15` | 748,380.00 USD | 0.00 USD | 135.00 USD | `-18.35%` | `2.99` |
| `Live` | `Long` | `45.25` | 748,250.00 USD | 0.00 USD | 3,180.00 USD | `-18.17%` | `70.37` |
| `Live` | `Long` | `45.35` | 745,060.00 USD | 0.00 USD | 2,180.00 USD | `-17.99%` | `48.02` |
| `Live` | `Long` | `45.45` | 742,890.00 USD | 0.00 USD | 23,940.00 USD | `-17.81%` | `526.65` |
| `Live` | `Long` | `45.55` | 718,950.00 USD | 0.00 USD | 318.39 USD | `-17.63%` | `6.99` |
| `Live` | `Long` | `46.05` | 718,630.00 USD | 0.00 USD | 10,690.00 USD | `-16.72%` | `232.05` |
| `Live` | `Long` | `46.35` | 707,950.00 USD | 0.00 USD | 383.78 USD | `-16.18%` | `8.28` |
| `Live` | `Long` | `46.55` | 707,560.00 USD | 0.00 USD | 1,630.00 USD | `-15.82%` | `35.00` |
| `Live` | `Long` | `46.65` | 705,930.00 USD | 0.00 USD | 2,530.00 USD | `-15.64%` | `54.16` |
| `Live` | `Long` | `46.85` | 703,410.00 USD | 0.00 USD | 358.40 USD | `-15.27%` | `7.65` |
| `Live` | `Long` | `46.95` | 703,050.00 USD | 0.00 USD | 158.22 USD | `-15.09%` | `3.37` |
| `Live` | `Long` | `47.05` | 702,890.00 USD | 0.00 USD | 126.09 USD | `-14.91%` | `2.68` |
| `Live` | `Long` | `47.15` | 702,760.00 USD | 0.00 USD | 9,740.00 USD | `-14.73%` | `206.65` |
| `Live` | `Long` | `47.25` | 693,020.00 USD | 0.00 USD | 574.09 USD | `-14.55%` | `12.15` |
| `Live` | `Long` | `47.35` | 692,450.00 USD | 0.00 USD | 840.46 USD | `-14.37%` | `17.75` |
| `Live` | `Long` | `47.45` | 691,610.00 USD | 0.00 USD | 4,820.00 USD | `-14.19%` | `101.62` |
| `Live` | `Long` | `47.55` | 686,780.00 USD | 0.00 USD | 1,770.00 USD | `-14.01%` | `37.28` |
| `Live` | `Long` | `47.75` | 685,010.00 USD | 0.00 USD | 4,780.00 USD | `-13.65%` | `100.00` |
| `Live` | `Long` | `48.05` | 680,240.00 USD | 0.00 USD | 1,340.00 USD | `-13.10%` | `27.93` |
| `Live` | `Long` | `48.15` | 678,890.00 USD | 0.00 USD | 1,690.00 USD | `-12.92%` | `35.03` |
| `Live` | `Long` | `48.25` | 677,210.00 USD | 0.00 USD | 525.44 USD | `-12.74%` | `10.89` |
| `Live` | `Long` | `48.55` | 676,680.00 USD | 0.00 USD | 2,030.00 USD | `-12.20%` | `41.85` |
| `Live` | `Long` | `48.65` | 674,650.00 USD | 0.00 USD | 273.90 USD | `-12.02%` | `5.63` |
| `Live` | `Long` | `48.75` | 674,380.00 USD | 0.00 USD | 333.94 USD | `-11.84%` | `6.85` |
| `Live` | `Long` | `48.95` | 674,040.00 USD | 0.00 USD | 2,700.00 USD | `-11.48%` | `55.08` |
| `Live` | `Long` | `49.05` | 671,350.00 USD | 0.00 USD | 1,580.00 USD | `-11.30%` | `32.25` |
| `Live` | `Long` | `49.15` | 669,760.00 USD | 0.00 USD | 5,740.00 USD | `-11.11%` | `116.83` |
| `Live` | `Long` | `49.25` | 664,020.00 USD | 0.00 USD | 263.49 USD | `-10.93%` | `5.35` |
| `Live` | `Long` | `49.35` | 663,760.00 USD | 0.00 USD | 5,230.00 USD | `-10.75%` | `105.97` |
| `Live` | `Long` | `49.45` | 658,530.00 USD | 0.00 USD | 1,960.00 USD | `-10.57%` | `39.73` |
| `Live` | `Long` | `49.55` | 656,560.00 USD | 0.00 USD | 18,010.00 USD | `-10.39%` | `363.57` |
| `Live` | `Long` | `49.65` | 638,550.00 USD | 0.00 USD | 92,360.00 USD | `-10.21%` | `1,860.21` |
| `Live` | `Long` | `49.75` | 546,190.00 USD | 0.00 USD | 1,580.00 USD | `-10.03%` | `31.67` |
| `Live` | `Long` | `49.95` | 544,610.00 USD | 0.00 USD | 28,540.00 USD | `-9.67%` | `571.31` |
| `Live` | `Long` | `50.05` | 516,080.00 USD | 0.00 USD | 1,820.00 USD | `-9.49%` | `36.43` |
| `Live` | `Long` | `50.25` | 514,250.00 USD | 0.00 USD | 102.51 USD | `-9.13%` | `2.04` |
| `Live` | `Long` | `50.35` | 514,150.00 USD | 0.00 USD | 1,030.00 USD | `-8.94%` | `20.49` |
| `Live` | `Long` | `50.45` | 513,120.00 USD | 0.00 USD | 4,720.00 USD | `-8.76%` | `93.64` |
| `Live` | `Long` | `50.55` | 508,400.00 USD | 0.00 USD | 84,100.00 USD | `-8.58%` | `1,663.61` |
| `Live` | `Long` | `50.75` | 424,300.00 USD | 0.00 USD | 9,050.00 USD | `-8.22%` | `178.28` |
| `Live` | `Long` | `50.85` | 415,250.00 USD | 0.00 USD | 263.40 USD | `-8.04%` | `5.18` |
| `Live` | `Long` | `50.95` | 414,990.00 USD | 0.00 USD | 245.07 USD | `-7.86%` | `4.81` |
| `Live` | `Long` | `51.15` | 414,740.00 USD | 0.00 USD | 219,370.00 USD | `-7.50%` | `4,288.79` |
| `Live` | `Long` | `51.45` | 195,370.00 USD | 0.00 USD | 20,410.00 USD | `-6.96%` | `396.78` |
| `Live` | `Long` | `51.55` | 174,960.00 USD | 0.00 USD | 551.07 USD | `-6.77%` | `10.69` |
| `Live` | `Long` | `51.65` | 174,410.00 USD | 0.00 USD | 8,810.00 USD | `-6.59%` | `170.51` |
| `Live` | `Long` | `51.75` | 165,600.00 USD | 0.00 USD | 6,480.00 USD | `-6.41%` | `125.17` |
| `Live` | `Long` | `51.85` | 159,120.00 USD | 0.00 USD | 13,890.00 USD | `-6.23%` | `267.97` |
| `Live` | `Long` | `51.95` | 145,230.00 USD | 0.00 USD | 19,580.00 USD | `-6.05%` | `376.99` |
| `Live` | `Long` | `52.05` | 125,640.00 USD | 0.00 USD | 283.15 USD | `-5.87%` | `5.44` |
| `Live` | `Long` | `52.15` | 125,360.00 USD | 0.00 USD | 7,510.00 USD | `-5.69%` | `143.99` |
| `Live` | `Long` | `52.25` | 117,850.00 USD | 0.00 USD | 3,620.00 USD | `-5.51%` | `69.36` |
| `Live` | `Long` | `52.35` | 114,230.00 USD | 0.00 USD | 3,020.00 USD | `-5.33%` | `57.70` |
| `Live` | `Long` | `52.45` | 111,210.00 USD | 0.00 USD | 3,830.00 USD | `-5.15%` | `72.95` |
| `Live` | `Long` | `52.55` | 107,380.00 USD | 0.00 USD | 8,700.00 USD | `-4.97%` | `165.49` |
| `Live` | `Long` | `52.75` | 98,680.00 USD | 0.00 USD | 7,290.00 USD | `-4.60%` | `138.28` |
| `Live` | `Long` | `52.85` | 91,390.00 USD | 0.00 USD | 21,120.00 USD | `-4.42%` | `399.58` |
| `Live` | `Long` | `52.95` | 70,270.00 USD | 0.00 USD | 25,840.00 USD | `-4.24%` | `488.06` |
| `Live` | `Long` | `53.05` | 44,430.00 USD | 0.00 USD | 900.26 USD | `-4.06%` | `16.97` |
| `Live` | `Long` | `53.15` | 43,530.00 USD | 0.00 USD | 2,640.00 USD | `-3.88%` | `49.69` |
| `Live` | `Long` | `53.25` | 40,890.00 USD | 0.00 USD | 911.64 USD | `-3.70%` | `17.12` |
| `Live` | `Long` | `53.35` | 39,980.00 USD | 0.00 USD | 2,120.00 USD | `-3.52%` | `39.78` |
| `Live` | `Long` | `53.45` | 37,850.00 USD | 0.00 USD | 4,880.00 USD | `-3.34%` | `91.21` |
| `Live` | `Long` | `53.65` | 32,980.00 USD | 0.00 USD | 350.87 USD | `-2.98%` | `6.54` |
| `Live` | `Long` | `53.75` | 32,630.00 USD | 0.00 USD | 148.35 USD | `-2.80%` | `2.76` |
| `Live` | `Long` | `53.85` | 32,480.00 USD | 0.00 USD | 2,130.00 USD | `-2.62%` | `39.58` |
| `Live` | `Long` | `53.95` | 30,350.00 USD | 0.00 USD | 27,050.00 USD | `-2.43%` | `501.35` |
| `Live` | `Long` | `54.05` | 3,300.00 USD | 0.00 USD | 219.44 USD | `-2.25%` | `4.06` |
| `Live` | `Long` | `54.15` | 3,080.00 USD | 0.00 USD | 3,080.00 USD | `-2.07%` | `56.91` |
| `Live` | `Short` | `57.95` | 978.20 USD | 978.20 USD | 0.00 USD | `+4.80%` | `16.88` |
| `Live` | `Short` | `58.15` | 200,630.00 USD | 199,650.00 USD | 0.00 USD | `+5.16%` | `3,433.33` |
| `Live` | `Short` | `58.75` | 200,840.00 USD | 213.26 USD | 0.00 USD | `+6.25%` | `3.63` |
| `Live` | `Short` | `59.05` | 201,050.00 USD | 213.76 USD | 0.00 USD | `+6.79%` | `3.62` |
| `Live` | `Short` | `59.35` | 210,500.00 USD | 9,440.00 USD | 0.00 USD | `+7.33%` | `159.09` |
| `Live` | `Short` | `60.05` | 210,710.00 USD | 217.98 USD | 0.00 USD | `+8.60%` | `3.63` |
| `Live` | `Short` | `60.35` | 210,930.00 USD | 218.47 USD | 0.00 USD | `+9.14%` | `3.62` |
| `Live` | `Short` | `61.15` | 214,800.00 USD | 3,870.00 USD | 0.00 USD | `+10.59%` | `63.26` |
| `Live` | `Short` | `62.65` | 214,940.00 USD | 142.84 USD | 0.00 USD | `+13.30%` | `2.28` |
| `Live` | `Short` | `63.25` | 216,270.00 USD | 1,330.00 USD | 0.00 USD | `+14.38%` | `21.02` |
| `Live` | `Short` | `65.25` | 216,460.00 USD | 186.61 USD | 0.00 USD | `+18.00%` | `2.86` |
| `Live` | `Short` | `65.35` | 216,610.00 USD | 150.96 USD | 0.00 USD | `+18.18%` | `2.31` |
| `Live` | `Short` | `66.85` | 250,560.00 USD | 33,950.00 USD | 0.00 USD | `+20.89%` | `507.83` |
| `Live` | `Short` | `66.95` | 250,680.00 USD | 121.18 USD | 0.00 USD | `+21.08%` | `1.81` |
| `Live` | `Short` | `67.85` | 251,390.00 USD | 709.03 USD | 0.00 USD | `+22.70%` | `10.45` |
| `Live` | `Short` | `68.95` | 251,840.00 USD | 449.55 USD | 0.00 USD | `+24.69%` | `6.52` |
| `Live` | `Short` | `70.45` | 256,370.00 USD | 4,530.00 USD | 0.00 USD | `+27.41%` | `64.29` |
| `Live` | `Short` | `71.35` | 256,720.00 USD | 348.19 USD | 0.00 USD | `+29.03%` | `4.88` |
| `Live` | `Short` | `74.45` | 276,580.00 USD | 19,860.00 USD | 0.00 USD | `+34.64%` | `266.81` |
| `Live` | `Short` | `75.45` | 276,840.00 USD | 260.30 USD | 0.00 USD | `+36.45%` | `3.45` |
| `Live` | `Short` | `76.35` | 285,220.00 USD | 8,380.00 USD | 0.00 USD | `+38.08%` | `109.80` |
| `Live` | `Short` | `77.85` | 285,830.00 USD | 602.56 USD | 0.00 USD | `+40.79%` | `7.74` |
| `Live` | `Short` | `77.95` | 285,960.00 USD | 136.41 USD | 0.00 USD | `+40.97%` | `1.75` |
| `Live` | `Short` | `79.75` | 286,690.00 USD | 728.12 USD | 0.00 USD | `+44.22%` | `9.13` |
| `Live` | `Short` | `80.75` | 287,340.00 USD | 646.00 USD | 0.00 USD | `+46.03%` | `8.00` |
| `Live` | `Short` | `81.05` | 306,340.00 USD | 19,000.00 USD | 0.00 USD | `+46.57%` | `234.42` |
| `Live` | `Short` | `81.55` | 306,460.00 USD | 123.96 USD | 0.00 USD | `+47.48%` | `1.52` |
| `Live` | `Short` | `82.65` | 310,310.00 USD | 3,850.00 USD | 0.00 USD | `+49.47%` | `46.61` |
| `Live` | `Short` | `82.75` | 310,530.00 USD | 214.32 USD | 0.00 USD | `+49.65%` | `2.59` |
| `Live` | `Short` | `83.05` | 313,850.00 USD | 3,320.00 USD | 0.00 USD | `+50.19%` | `40.00` |
| `Live` | `Short` | `83.95` | 316,620.00 USD | 2,770.00 USD | 0.00 USD | `+51.82%` | `33.00` |
| `Live` | `Short` | `84.65` | 317,480.00 USD | 862.58 USD | 0.00 USD | `+53.09%` | `10.19` |
| `Live` | `Short` | `91.25` | 318,450.00 USD | 969.99 USD | 0.00 USD | `+65.02%` | `10.63` |
| `Live` | `Short` | `91.95` | 318,570.00 USD | 121.37 USD | 0.00 USD | `+66.29%` | `1.32` |
| `Live` | `Short` | `98.45` | 321,030.00 USD | 2,460.00 USD | 0.00 USD | `+78.04%` | `25.00` |
| `Live` | `Short` | `104.15` | 321,750.00 USD | 711.34 USD | 0.00 USD | `+88.35%` | `6.83` |
| `Live` | `Short` | `104.35` | 321,960.00 USD | 216.00 USD | 0.00 USD | `+88.71%` | `2.07` |
| `Live` | `Short` | `105.45` | 677,750.00 USD | 355,790.00 USD | 0.00 USD | `+90.70%` | `3,374.01` |
| `Live` | `Short` | `110.45` | 677,880.00 USD | 131.44 USD | 0.00 USD | `+99.74%` | `1.19` |
| `Live` | `Short` | `110.55` | 679,000.00 USD | 1,120.00 USD | 0.00 USD | `+99.92%` | `10.11` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 375,940.00 USD | 0.00 USD | 392.18 USD | `-63.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 375,550.00 USD | 0.00 USD | 2,310.00 USD | `-60.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 373,240.00 USD | 0.00 USD | 806.86 USD | `-54.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 372,430.00 USD | 0.00 USD | 1,560.00 USD | `-54.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 370,870.00 USD | 0.00 USD | 410.25 USD | `-50.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 370,460.00 USD | 0.00 USD | 281.57 USD | `-45.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 370,180.00 USD | 0.00 USD | 36,050.00 USD | `-34.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 334,130.00 USD | 0.00 USD | 37,550.00 USD | `-32.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 296,580.00 USD | 0.00 USD | 447.01 USD | `-31.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 296,140.00 USD | 0.00 USD | 40,560.00 USD | `-29.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 255,580.00 USD | 0.00 USD | 489.57 USD | `-28.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 255,090.00 USD | 0.00 USD | 1,550.00 USD | `-27.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 253,540.00 USD | 0.00 USD | 9,840.00 USD | `-27.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 243,700.00 USD | 0.00 USD | 2,060.00 USD | `-25.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 241,640.00 USD | 0.00 USD | 2,960.00 USD | `-24.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 238,690.00 USD | 0.00 USD | 6,050.00 USD | `-23.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 232,630.00 USD | 0.00 USD | 5,680.00 USD | `-22.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 226,950.00 USD | 0.00 USD | 672.22 USD | `-20.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 226,280.00 USD | 0.00 USD | 213.80 USD | `-19.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 226,070.00 USD | 0.00 USD | 223.20 USD | `-19.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 225,850.00 USD | 0.00 USD | 391.13 USD | `-19.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 225,450.00 USD | 0.00 USD | 7,080.00 USD | `-18.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 218,380.00 USD | 0.00 USD | 1,370.00 USD | `-17.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 217,010.00 USD | 0.00 USD | 553.80 USD | `-16.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 216,460.00 USD | 0.00 USD | 14,000.00 USD | `-15.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 202,460.00 USD | 0.00 USD | 158.56 USD | `-14.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 202,300.00 USD | 0.00 USD | 373.28 USD | `-14.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 201,930.00 USD | 0.00 USD | 849.46 USD | `-14.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 201,080.00 USD | 0.00 USD | 1,150.00 USD | `-13.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 199,930.00 USD | 0.00 USD | 1,740.00 USD | `-11.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 198,190.00 USD | 0.00 USD | 981.00 USD | `-11.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.35` | 197,210.00 USD | 0.00 USD | 817.24 USD | `-10.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 196,390.00 USD | 0.00 USD | 237.85 USD | `-10.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.55` | 196,150.00 USD | 0.00 USD | 1,250.00 USD | `-10.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 194,900.00 USD | 0.00 USD | 298.20 USD | `-9.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 194,610.00 USD | 0.00 USD | 14,650.00 USD | `-9.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 179,950.00 USD | 0.00 USD | 6,410.00 USD | `-9.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 173,540.00 USD | 0.00 USD | 459.70 USD | `-8.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 173,080.00 USD | 0.00 USD | 144.57 USD | `-8.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 172,930.00 USD | 0.00 USD | 1,020.00 USD | `-7.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 171,910.00 USD | 0.00 USD | 439.89 USD | `-7.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.45` | 171,470.00 USD | 0.00 USD | 204.26 USD | `-6.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 171,270.00 USD | 0.00 USD | 7,320.00 USD | `-6.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.95` | 163,950.00 USD | 0.00 USD | 8,810.00 USD | `-6.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 155,140.00 USD | 0.00 USD | 27,730.00 USD | `-5.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 127,410.00 USD | 0.00 USD | 51,800.00 USD | `-4.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 75,610.00 USD | 0.00 USD | 10,530.00 USD | `-4.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 65,080.00 USD | 0.00 USD | 271.13 USD | `-4.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 64,800.00 USD | 0.00 USD | 1,100.00 USD | `-4.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 63,710.00 USD | 0.00 USD | 12,330.00 USD | `-4.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 51,370.00 USD | 0.00 USD | 460.81 USD | `-3.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 50,910.00 USD | 0.00 USD | 566.57 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 50,350.00 USD | 0.00 USD | 5,950.00 USD | `-3.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 44,400.00 USD | 0.00 USD | 1,370.00 USD | `-2.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.75` | 43,030.00 USD | 0.00 USD | 234.35 USD | `-2.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 42,800.00 USD | 0.00 USD | 462.03 USD | `-2.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 42,330.00 USD | 0.00 USD | 746.97 USD | `-2.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 41,590.00 USD | 0.00 USD | 3,090.00 USD | `-1.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 38,500.00 USD | 0.00 USD | 156.53 USD | `-1.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.45` | 38,340.00 USD | 0.00 USD | 570.09 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.55` | 37,770.00 USD | 0.00 USD | 1,690.00 USD | `-1.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.65` | 36,080.00 USD | 0.00 USD | 198.38 USD | `-1.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.75` | 35,880.00 USD | 0.00 USD | 198.74 USD | `-0.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 35,680.00 USD | 0.00 USD | 33,280.00 USD | `-0.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.95` | 2,410.00 USD | 0.00 USD | 397.84 USD | `-0.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 2,010.00 USD | 0.00 USD | 1,580.00 USD | `-0.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.25` | 429.85 USD | 0.00 USD | 429.85 USD | `-0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.35` | 2,140.00 USD | 2,140.00 USD | 0.00 USD | `+0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.55` | 2,250.00 USD | 113.88 USD | 0.00 USD | `+0.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.65` | 5,860.00 USD | 3,610.00 USD | 0.00 USD | `+0.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.75` | 6,070.00 USD | 202.37 USD | 0.00 USD | `+0.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.85` | 6,260.00 USD | 196.59 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.95` | 6,460.00 USD | 193.03 USD | 0.00 USD | `+1.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.05` | 7,040.00 USD | 587.96 USD | 0.00 USD | `+1.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.15` | 7,440.00 USD | 397.54 USD | 0.00 USD | `+1.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.25` | 8,050.00 USD | 611.44 USD | 0.00 USD | `+1.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.35` | 8,180.00 USD | 128.48 USD | 0.00 USD | `+1.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.55` | 10,820.00 USD | 2,640.00 USD | 0.00 USD | `+2.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.65` | 10,940.00 USD | 121.23 USD | 0.00 USD | `+2.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.75` | 11,170.00 USD | 228.70 USD | 0.00 USD | `+2.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.85` | 29,200.00 USD | 18,030.00 USD | 0.00 USD | `+2.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.95` | 29,590.00 USD | 390.68 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.05` | 35,390.00 USD | 5,800.00 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.15` | 35,780.00 USD | 392.05 USD | 0.00 USD | `+3.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.25` | 35,980.00 USD | 201.52 USD | 0.00 USD | `+3.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.45` | 36,330.00 USD | 344.70 USD | 0.00 USD | `+3.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.55` | 56,690.00 USD | 20,360.00 USD | 0.00 USD | `+4.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.65` | 56,890.00 USD | 198.89 USD | 0.00 USD | `+4.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.75` | 57,010.00 USD | 119.54 USD | 0.00 USD | `+4.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.95` | 57,130.00 USD | 128.65 USD | 0.00 USD | `+4.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 57,760.00 USD | 621.13 USD | 0.00 USD | `+4.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 57,960.00 USD | 200.04 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 58,160.00 USD | 200.96 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 58,280.00 USD | 123.70 USD | 0.00 USD | `+5.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 58,880.00 USD | 601.45 USD | 0.00 USD | `+5.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 59,280.00 USD | 401.65 USD | 0.00 USD | `+5.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.65` | 59,560.00 USD | 274.48 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 60,050.00 USD | 491.15 USD | 0.00 USD | `+6.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 62,990.00 USD | 2,940.00 USD | 0.00 USD | `+6.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 63,120.00 USD | 129.69 USD | 0.00 USD | `+6.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 67,920.00 USD | 4,800.00 USD | 0.00 USD | `+6.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 69,200.00 USD | 1,280.00 USD | 0.00 USD | `+6.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.25` | 69,510.00 USD | 307.51 USD | 0.00 USD | `+7.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 69,970.00 USD | 461.74 USD | 0.00 USD | `+7.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 70,130.00 USD | 159.92 USD | 0.00 USD | `+7.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.55` | 70,630.00 USD | 496.65 USD | 0.00 USD | `+7.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 71,350.00 USD | 724.75 USD | 0.00 USD | `+7.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.75` | 71,460.00 USD | 113.53 USD | 0.00 USD | `+8.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 71,620.00 USD | 158.00 USD | 0.00 USD | `+8.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 71,790.00 USD | 171.14 USD | 0.00 USD | `+8.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 72,340.00 USD | 551.00 USD | 0.00 USD | `+9.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 73,220.00 USD | 878.58 USD | 0.00 USD | `+9.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 74,610.00 USD | 1,390.00 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.75` | 75,020.00 USD | 407.63 USD | 0.00 USD | `+9.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 76,000.00 USD | 986.99 USD | 0.00 USD | `+10.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 76,680.00 USD | 674.72 USD | 0.00 USD | `+10.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 79,040.00 USD | 2,360.00 USD | 0.00 USD | `+10.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 79,170.00 USD | 125.56 USD | 0.00 USD | `+10.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.35` | 79,400.00 USD | 236.20 USD | 0.00 USD | `+10.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 83,000.00 USD | 3,600.00 USD | 0.00 USD | `+11.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 83,640.00 USD | 643.20 USD | 0.00 USD | `+11.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.95` | 85,760.00 USD | 2,120.00 USD | 0.00 USD | `+12.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 85,890.00 USD | 130.31 USD | 0.00 USD | `+12.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.25` | 86,010.00 USD | 117.03 USD | 0.00 USD | `+12.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.45` | 86,230.00 USD | 217.95 USD | 0.00 USD | `+12.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.55` | 86,570.00 USD | 347.15 USD | 0.00 USD | `+13.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 87,290.00 USD | 716.72 USD | 0.00 USD | `+13.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.75` | 87,430.00 USD | 141.19 USD | 0.00 USD | `+13.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 87,660.00 USD | 231.39 USD | 0.00 USD | `+14.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 88,170.00 USD | 508.36 USD | 0.00 USD | `+14.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 88,880.00 USD | 703.97 USD | 0.00 USD | `+14.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.35` | 89,020.00 USD | 140.64 USD | 0.00 USD | `+14.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 89,690.00 USD | 668.13 USD | 0.00 USD | `+14.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 94,240.00 USD | 4,550.00 USD | 0.00 USD | `+14.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 94,790.00 USD | 555.03 USD | 0.00 USD | `+15.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 95,320.00 USD | 531.62 USD | 0.00 USD | `+15.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.45` | 95,990.00 USD | 665.12 USD | 0.00 USD | `+16.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 96,190.00 USD | 202.69 USD | 0.00 USD | `+16.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 96,490.00 USD | 298.04 USD | 0.00 USD | `+16.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 96,590.00 USD | 102.13 USD | 0.00 USD | `+17.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 97,130.00 USD | 540.09 USD | 0.00 USD | `+17.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 97,230.00 USD | 100.79 USD | 0.00 USD | `+18.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 97,490.00 USD | 262.20 USD | 0.00 USD | `+18.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.65` | 97,810.00 USD | 315.12 USD | 0.00 USD | `+18.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 98,180.00 USD | 371.49 USD | 0.00 USD | `+18.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.85` | 99,060.00 USD | 881.07 USD | 0.00 USD | `+19.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 99,760.00 USD | 696.17 USD | 0.00 USD | `+19.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 100,290.00 USD | 534.00 USD | 0.00 USD | `+20.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 111,370.00 USD | 11,080.00 USD | 0.00 USD | `+21.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 124,780.00 USD | 13,410.00 USD | 0.00 USD | `+21.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.05` | 127,140.00 USD | 2,360.00 USD | 0.00 USD | `+23.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 132,000.00 USD | 4,860.00 USD | 0.00 USD | `+23.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 132,210.00 USD | 204.48 USD | 0.00 USD | `+25.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 133,020.00 USD | 810.02 USD | 0.00 USD | `+26.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 452,910.00 USD | 319,890.00 USD | 0.00 USD | `+26.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 453,080.00 USD | 170.04 USD | 0.00 USD | `+28.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 458,850.00 USD | 5,770.00 USD | 0.00 USD | `+28.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 459,120.00 USD | 269.28 USD | 0.00 USD | `+28.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 459,410.00 USD | 291.40 USD | 0.00 USD | `+30.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 466,990.00 USD | 7,580.00 USD | 0.00 USD | `+30.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 467,140.00 USD | 156.78 USD | 0.00 USD | `+30.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 470,370.00 USD | 3,220.00 USD | 0.00 USD | `+31.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 470,780.00 USD | 411.14 USD | 0.00 USD | `+33.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 593,970.00 USD | 123,190.00 USD | 0.00 USD | `+33.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 594,980.00 USD | 1,020.00 USD | 0.00 USD | `+34.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 595,090.00 USD | 104.93 USD | 0.00 USD | `+35.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 603,300.00 USD | 8,210.00 USD | 0.00 USD | `+35.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 603,700.00 USD | 402.59 USD | 0.00 USD | `+36.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.85` | 604,010.00 USD | 308.71 USD | 0.00 USD | `+37.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 604,330.00 USD | 315.18 USD | 0.00 USD | `+39.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 663,630.00 USD | 59,310.00 USD | 0.00 USD | `+42.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 666,800.00 USD | 3,160.00 USD | 0.00 USD | `+42.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 672,480.00 USD | 5,690.00 USD | 0.00 USD | `+44.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 709,080.00 USD | 36,590.00 USD | 0.00 USD | `+44.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 709,510.00 USD | 433.89 USD | 0.00 USD | `+46.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 709,680.00 USD | 172.64 USD | 0.00 USD | `+46.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 709,850.00 USD | 164.10 USD | 0.00 USD | `+48.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 710,390.00 USD | 546.81 USD | 0.00 USD | `+49.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 712,700.00 USD | 2,300.00 USD | 0.00 USD | `+52.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 724,770.00 USD | 12,070.00 USD | 0.00 USD | `+53.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.75` | 737,090.00 USD | 12,330.00 USD | 0.00 USD | `+55.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.05` | 757,330.00 USD | 20,230.00 USD | 0.00 USD | `+57.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.25` | 757,760.00 USD | 435.38 USD | 0.00 USD | `+57.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 759,340.00 USD | 1,580.00 USD | 0.00 USD | `+59.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 796,340.00 USD | 37,000.00 USD | 0.00 USD | `+59.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 796,810.00 USD | 473.21 USD | 0.00 USD | `+60.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 798,080.00 USD | 1,270.00 USD | 0.00 USD | `+61.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 799,720.00 USD | 1,630.00 USD | 0.00 USD | `+61.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 818,460.00 USD | 18,740.00 USD | 0.00 USD | `+62.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 818,940.00 USD | 481.55 USD | 0.00 USD | `+65.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 820,270.00 USD | 1,330.00 USD | 0.00 USD | `+66.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 820,460.00 USD | 188.10 USD | 0.00 USD | `+70.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,090,000.00 USD | 266,140.00 USD | 0.00 USD | `+71.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,090,000.00 USD | 3,400.00 USD | 0.00 USD | `+72.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,110,000.00 USD | 21,930.00 USD | 0.00 USD | `+73.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,110,000.00 USD | 294.15 USD | 0.00 USD | `+77.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,120,000.00 USD | 4,010.00 USD | 0.00 USD | `+80.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,120,000.00 USD | 306.15 USD | 0.00 USD | `+84.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,120,000.00 USD | 936.72 USD | 0.00 USD | `+86.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,120,000.00 USD | 2,920.00 USD | 0.00 USD | `+86.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,120,000.00 USD | 324.15 USD | 0.00 USD | `+95.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 1,120,000.00 USD | 123.23 USD | 0.00 USD | `+97.21%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `49.10` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 0.00 USD | 242.30 USD | 0.00 USD |
| `1D` | `49.20` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 13,300.00 USD | 3,260.00 USD | 367.32 USD |
| `7D` | `49.30` | 8,320,000.00 USD | 0.00 USD | 8,320,000.00 USD | 15,190.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `49.40` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 626.48 USD |
| `7D` | `49.40` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD |
| `1D` | `49.50` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 1,180.00 USD | 4,790.00 USD | 13,790.00 USD |
| `7D` | `49.50` | 8,290,000.00 USD | 0.00 USD | 8,290,000.00 USD | 1,130.00 USD | 6,290.00 USD | 0.00 USD |
| `1D` | `49.60` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 785.85 USD | 4,760.00 USD | 0.00 USD |
| `7D` | `49.60` | 8,290,000.00 USD | 0.00 USD | 8,290,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD |
| `1D` | `49.70` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,320.00 USD | 0.00 USD | 301.72 USD |
| `7D` | `49.70` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 788.92 USD | 0.00 USD | 4,900.00 USD |
| `1D` | `49.80` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 667.20 USD | 733.27 USD | 11,870.00 USD |
| `7D` | `49.80` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 7,660.00 USD | 8,220.00 USD | 0.00 USD |
| `1D` | `49.90` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 17,040.00 USD | 5,020.00 USD | 22,850.00 USD |
| `7D` | `49.90` | 8,250,000.00 USD | 0.00 USD | 8,250,000.00 USD | 45,030.00 USD | 5,410.00 USD | 4,700.00 USD |
| `1D` | `50.00` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 4,340.00 USD | 3,540.00 USD | 40,300.00 USD |
| `7D` | `50.00` | 8,200,000.00 USD | 0.00 USD | 8,200,000.00 USD | 22,100.00 USD | 5,170.00 USD | 24,550.00 USD |
| `1D` | `50.10` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 0.00 USD | 2,170.00 USD | 0.00 USD |
| `7D` | `50.10` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 363.50 USD | 682.90 USD | 0.00 USD |
| `7D` | `50.20` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 6,960.00 USD | 500.40 USD | 34,680.00 USD |
| `1D` | `50.30` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 0.00 USD | 333.03 USD | 0.00 USD |
| `7D` | `50.30` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 16,270.00 USD | 3,640.00 USD | 1,950.00 USD |
| `1D` | `50.40` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 349.63 USD | 2,190.00 USD | 0.00 USD |
| `7D` | `50.40` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 23,520.00 USD | 19,110.00 USD | 33,450.00 USD |
| `7D` | `50.50` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 24,840.00 USD | 6,790.00 USD | 43,710.00 USD |
| `7D` | `50.60` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 52,670.00 USD | 17,830.00 USD | 22,250.00 USD |
| `7D` | `50.70` | 7,830,000.00 USD | 0.00 USD | 7,830,000.00 USD | 53,670.00 USD | 24,710.00 USD | 32,520.00 USD |
| `1D` | `50.80` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 5,630.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `50.80` | 7,720,000.00 USD | 0.00 USD | 7,720,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD |
| `1D` | `50.90` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 0.00 USD | 260.05 USD | 8,390.00 USD |
| `7D` | `50.90` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD |
| `1D` | `51.00` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 129.78 USD |
| `7D` | `51.00` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `51.10` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 263.90 USD | 1,160.00 USD | 0.00 USD |
| `7D` | `51.10` | 7,250,000.00 USD | 0.00 USD | 7,250,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD |
| `1D` | `51.20` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 1,100.00 USD | 1,130.00 USD | 327.72 USD |
| `7D` | `51.20` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD |
| `1D` | `51.30` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 20,430.00 USD | 5,150.00 USD | 18,640.00 USD |
| `7D` | `51.30` | 7,100,000.00 USD | 0.00 USD | 7,100,000.00 USD | 19,510.00 USD | 12,490.00 USD | 47,090.00 USD |
| `1D` | `51.40` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 17,510.00 USD | 7,090.00 USD | 10,780.00 USD |
| `7D` | `51.40` | 7,020,000.00 USD | 0.00 USD | 7,020,000.00 USD | 71,090.00 USD | 28,960.00 USD | 45,150.00 USD |
| `1D` | `51.50` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 11,450.00 USD | 8,980.00 USD | 4,080.00 USD |
| `7D` | `51.50` | 6,880,000.00 USD | 0.00 USD | 6,880,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `51.60` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 8,800.00 USD | 7,990.00 USD | 4,820.00 USD |
| `7D` | `51.60` | 6,780,000.00 USD | 0.00 USD | 6,780,000.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD |
| `1D` | `51.70` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 4,980.00 USD | 4,150.00 USD | 6,480.00 USD |
| `7D` | `51.70` | 6,720,000.00 USD | 0.00 USD | 6,720,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `51.80` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 12,930.00 USD | 2,080.00 USD | 10,050.00 USD |
| `7D` | `51.80` | 6,680,000.00 USD | 0.00 USD | 6,680,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD |
| `1D` | `51.90` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 12,520.00 USD | 21,470.00 USD | 9,190.00 USD |
| `7D` | `51.90` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 5,870.00 USD | 15,810.00 USD | 4,760.00 USD |
| `1D` | `52.00` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 25,510.00 USD | 8,240.00 USD | 23,340.00 USD |
| `7D` | `52.00` | 6,600,000.00 USD | 0.00 USD | 6,600,000.00 USD | 64,300.00 USD | 20,800.00 USD | 11,880.00 USD |
| `1D` | `52.10` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 27,630.00 USD | 5,780.00 USD | 35,220.00 USD |
| `7D` | `52.10` | 6,500,000.00 USD | 0.00 USD | 6,500,000.00 USD | 24,220.00 USD | 18,810.00 USD | 35,480.00 USD |
| `1D` | `52.20` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 20,520.00 USD | 10,460.00 USD | 14,390.00 USD |
| `7D` | `52.20` | 6,420,000.00 USD | 0.00 USD | 6,420,000.00 USD | 38,380.00 USD | 4,340.00 USD | 25,270.00 USD |
| `1D` | `52.30` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 38,870.00 USD | 8,170.00 USD | 16,110.00 USD |
| `7D` | `52.30` | 6,360,000.00 USD | 0.00 USD | 6,360,000.00 USD | 18,740.00 USD | 12,840.00 USD | 8,940.00 USD |
| `1D` | `52.40` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 11,440.00 USD | 7,510.00 USD | 6,280.00 USD |
| `7D` | `52.40` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 20,580.00 USD | 11,230.00 USD | 20,050.00 USD |
| `1D` | `52.50` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 48,310.00 USD | 13,510.00 USD | 998.32 USD |
| `7D` | `52.50` | 6,260,000.00 USD | 0.00 USD | 6,260,000.00 USD | 33,240.00 USD | 667.05 USD | 11,240.00 USD |
| `1D` | `52.60` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 4,750.00 USD | 9,470.00 USD | 506.16 USD |
| `7D` | `52.60` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 74,610.00 USD | 14,530.00 USD | 584.77 USD |
| `1D` | `52.70` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 13,370.00 USD | 7,610.00 USD | 15,080.00 USD |
| `7D` | `52.70` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 20,250.00 USD | 43,820.00 USD | 62,360.00 USD |
| `1D` | `52.80` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 14,400.00 USD | 16,680.00 USD | 74,160.00 USD |
| `7D` | `52.80` | 6,000,000.00 USD | 0.00 USD | 6,000,000.00 USD | 46,600.00 USD | 29,900.00 USD | 108.50 USD |
| `1D` | `52.90` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 40,590.00 USD | 12,380.00 USD | 6,120.00 USD |
| `7D` | `52.90` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 51,920.00 USD | 26,170.00 USD | 34,400.00 USD |
| `1D` | `53.00` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 4,280.00 USD | 4,790.00 USD | 1,690.00 USD |
| `7D` | `53.00` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 18,990.00 USD | 8,880.00 USD | 55,850.00 USD |
| `1D` | `53.10` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 22,820.00 USD | 8,110.00 USD | 54,830.00 USD |
| `7D` | `53.10` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 52,760.00 USD | 36,340.00 USD | 9,860.00 USD |
| `1D` | `53.20` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 65,380.00 USD | 19,420.00 USD | 63,450.00 USD |
| `7D` | `53.20` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 141,420.00 USD | 38,500.00 USD | 27,410.00 USD |
| `1D` | `53.30` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 27,380.00 USD | 18,850.00 USD | 41,770.00 USD |
| `7D` | `53.30` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 63,050.00 USD | 14,250.00 USD | 37,140.00 USD |
| `1D` | `53.40` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 11,070.00 USD | 13,340.00 USD | 76,880.00 USD |
| `7D` | `53.40` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 48,760.00 USD | 14,570.00 USD | 95,920.00 USD |
| `1D` | `53.50` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 11,320.00 USD | 8,980.00 USD | 7,160.00 USD |
| `7D` | `53.50` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 49,490.00 USD | 12,620.00 USD | 17,890.00 USD |
| `1D` | `53.60` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 76,890.00 USD | 19,300.00 USD | 1,840.00 USD |
| `7D` | `53.60` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 53,580.00 USD | 6,140.00 USD | 98,560.00 USD |
| `1D` | `53.70` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 5,710.00 USD | 8,090.00 USD | 465.28 USD |
| `7D` | `53.70` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 140,080.00 USD | 16,400.00 USD | 12,890.00 USD |
| `1D` | `53.80` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 16,800.00 USD | 5,480.00 USD | 3,130.00 USD |
| `7D` | `53.80` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 99,150.00 USD | 80,510.00 USD | 126,140.00 USD |
| `1D` | `53.90` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 7,480.00 USD | 28,010.00 USD | 125,910.00 USD |
| `7D` | `53.90` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 111,970.00 USD | 56,750.00 USD | 123,850.00 USD |
| `1D` | `54.00` | 977,460.00 USD | 0.00 USD | 977,460.00 USD | 28,730.00 USD | 24,090.00 USD | 0.00 USD |
| `7D` | `54.00` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 344,710.00 USD | 148,420.00 USD | 271,500.00 USD |
| `1D` | `54.10` | 924,640.00 USD | 0.00 USD | 924,640.00 USD | 23,830.00 USD | 5,860.00 USD | 1,510.00 USD |
| `7D` | `54.10` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 234,120.00 USD | 45,470.00 USD | 184,480.00 USD |
| `1D` | `54.20` | 893,440.00 USD | 0.00 USD | 893,440.00 USD | 54,060.00 USD | 12,370.00 USD | 108,330.00 USD |
| `7D` | `54.20` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 234,980.00 USD | 155,540.00 USD | 128,910.00 USD |
| `1D` | `54.30` | 718,690.00 USD | 0.00 USD | 718,690.00 USD | 121,180.00 USD | 26,040.00 USD | 142,890.00 USD |
| `7D` | `54.30` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 339,300.00 USD | 131,670.00 USD | 185,160.00 USD |
| `1D` | `54.40` | 428,570.00 USD | 0.00 USD | 428,570.00 USD | 37,530.00 USD | 32,150.00 USD | 78,270.00 USD |
| `7D` | `54.40` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 304,270.00 USD | 6,020.00 USD | 92,140.00 USD |
| `1D` | `54.50` | 280,610.00 USD | 0.00 USD | 280,610.00 USD | 3,040.00 USD | 20,570.00 USD | 144,050.00 USD |
| `7D` | `54.50` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 159,720.00 USD | 29,880.00 USD | 237,000.00 USD |
| `1D` | `54.60` | 112,950.00 USD | 0.00 USD | 112,950.00 USD | 11,550.00 USD | 9,270.00 USD | 14,320.00 USD |
| `7D` | `54.60` | 911,140.00 USD | 0.00 USD | 911,140.00 USD | 0.00 USD | 1,930.00 USD | 72,400.00 USD |
| `1D` | `54.70` | 77,810.00 USD | 0.00 USD | 77,810.00 USD | 0.00 USD | 0.00 USD | 57,100.00 USD |
| `7D` | `54.70` | 836,810.00 USD | 0.00 USD | 836,810.00 USD | 0.00 USD | 0.00 USD | 173,390.00 USD |
| `1D` | `54.80` | 20,710.00 USD | 0.00 USD | 20,710.00 USD | 0.00 USD | 9,420.00 USD | 0.00 USD |
| `1D` | `55.10` | 11,290.00 USD | 0.00 USD | 11,290.00 USD | 0.00 USD | 0.00 USD | 189.61 USD |
| `1D` | `55.20` | 11,100.00 USD | 0.00 USD | 11,100.00 USD | 11,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.20` | 663,420.00 USD | 0.00 USD | 663,420.00 USD | 336,630.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.50` | 326,800.00 USD | 0.00 USD | 326,800.00 USD | 326,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.60` | 426,340.00 USD | 426,340.00 USD | 0.00 USD | 426,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.60` | 852,690.00 USD | 852,690.00 USD | 0.00 USD | 426,340.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `55.70` | 407.86 USD | 407.86 USD | 0.00 USD | 0.00 USD | 0.00 USD | 407.86 USD |
| `1D` | `55.70` | 815.72 USD | 815.72 USD | 0.00 USD | 0.00 USD | 0.00 USD | 407.86 USD |
| `7D` | `55.70` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD |
| `1D` | `55.80` | 253,040.00 USD | 253,040.00 USD | 0.00 USD | 189,240.00 USD | 16,300.00 USD | 46,680.00 USD |
| `7D` | `55.80` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD |
| `1D` | `55.90` | 531,790.00 USD | 531,790.00 USD | 0.00 USD | 137,200.00 USD | 1,440.00 USD | 140,110.00 USD |
| `7D` | `55.90` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 141,330.00 USD | 65,840.00 USD | 0.00 USD |
| `1D` | `56.00` | 731,060.00 USD | 731,060.00 USD | 0.00 USD | 139,840.00 USD | 0.00 USD | 59,430.00 USD |
| `7D` | `56.00` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 181,230.00 USD | 98,600.00 USD | 147,270.00 USD |
| `1D` | `56.10` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 105,950.00 USD | 28,010.00 USD | 174,550.00 USD |
| `7D` | `56.10` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 121,920.00 USD | 144,120.00 USD | 61,210.00 USD |
| `1D` | `56.20` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 96,820.00 USD | 83,660.00 USD | 71,790.00 USD |
| `7D` | `56.20` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 104,510.00 USD | 72,410.00 USD | 240,740.00 USD |
| `1D` | `56.30` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 464.20 USD | 37,150.00 USD | 38,390.00 USD |
| `7D` | `56.30` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 91,850.00 USD | 128,970.00 USD | 131,790.00 USD |
| `1D` | `56.40` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 39,090.00 USD | 43,300.00 USD | 225,690.00 USD |
| `7D` | `56.40` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 215,940.00 USD | 116,750.00 USD | 137,070.00 USD |
| `1D` | `56.50` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 111,210.00 USD | 132,180.00 USD | 114,250.00 USD |
| `7D` | `56.50` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 128,680.00 USD | 125,310.00 USD | 3,750.00 USD |
| `1D` | `56.60` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 34,340.00 USD | 90,280.00 USD | 77,950.00 USD |
| `7D` | `56.60` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 363,190.00 USD | 119,150.00 USD | 0.00 USD |
| `1D` | `56.70` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 197,080.00 USD | 20,570.00 USD | 345,780.00 USD |
| `7D` | `56.70` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 110,940.00 USD | 114,460.00 USD | 96,070.00 USD |
| `1D` | `56.80` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 189,460.00 USD | 11,450.00 USD | 116,650.00 USD |
| `7D` | `56.80` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 153,580.00 USD | 92,780.00 USD | 261,330.00 USD |
| `1D` | `56.90` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 33,240.00 USD | 8,150.00 USD | 1,780.00 USD |
| `7D` | `56.90` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 108,440.00 USD | 48,600.00 USD | 266,610.00 USD |
| `1D` | `57.00` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 12,360.00 USD | 659.87 USD |
| `7D` | `57.00` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 88,680.00 USD | 2,620.00 USD | 93,100.00 USD |
| `1D` | `57.10` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 7,480.00 USD | 10,960.00 USD | 5,950.00 USD |
| `7D` | `57.10` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 36,580.00 USD | 16,110.00 USD | 20,440.00 USD |
| `1D` | `57.20` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 14,000.00 USD | 63,210.00 USD |
| `7D` | `57.20` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 21,160.00 USD | 15,720.00 USD | 3,700.00 USD |
| `1D` | `57.30` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 12,360.00 USD | 12,450.00 USD | 386.57 USD |
| `7D` | `57.30` | 5,700,000.00 USD | 5,700,000.00 USD | 0.00 USD | 22,360.00 USD | 3,150.00 USD | 34,250.00 USD |
| `1D` | `57.40` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 19,650.00 USD | 28,690.00 USD | 754.29 USD |
| `7D` | `57.40` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 38,520.00 USD | 30,000.00 USD | 153,130.00 USD |
| `1D` | `57.50` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 128,210.00 USD | 19,060.00 USD | 90,610.00 USD |
| `7D` | `57.50` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 76,670.00 USD | 30,210.00 USD | 0.00 USD |
| `1D` | `57.60` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 55,610.00 USD | 13,020.00 USD | 57,130.00 USD |
| `7D` | `57.60` | 6,220,000.00 USD | 6,220,000.00 USD | 0.00 USD | 123,760.00 USD | 36,020.00 USD | 28,320.00 USD |
| `1D` | `57.70` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 28,040.00 USD | 17,370.00 USD | 96,250.00 USD |
| `7D` | `57.70` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 1,500.00 USD | 57,330.00 USD |
| `1D` | `57.80` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 2,360.00 USD | 10,290.00 USD | 72,680.00 USD |
| `7D` | `57.80` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 2,260.00 USD | 10,840.00 USD | 48,030.00 USD |
| `1D` | `57.90` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 6,090.00 USD | 11,200.00 USD | 7,160.00 USD |
| `7D` | `57.90` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 2,410.00 USD | 963.90 USD | 1,510.00 USD |
| `1D` | `58.00` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 3,570.00 USD | 5,650.00 USD | 0.00 USD |
| `7D` | `58.00` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 0.00 USD | 3,670.00 USD | 86,690.00 USD |
| `1D` | `58.10` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 29,450.00 USD | 6,730.00 USD | 9,350.00 USD |
| `7D` | `58.10` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD | 848.40 USD |
| `1D` | `58.20` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 1,980.00 USD | 5,880.00 USD | 350.42 USD |
| `1D` | `58.30` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 9,890.00 USD | 11,540.00 USD | 36,830.00 USD |
| `7D` | `58.30` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 9,580.00 USD | 26,820.00 USD |
| `1D` | `58.40` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 4,990.00 USD | 33,950.00 USD |
| `7D` | `58.40` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 54,120.00 USD |
| `1D` | `58.50` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 49,290.00 USD | 21,280.00 USD | 379.22 USD |
| `7D` | `58.50` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD |
| `7D` | `58.60` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `58.70` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 15,850.00 USD | 8,070.00 USD | 355.85 USD |
| `7D` | `58.70` | 6,600,000.00 USD | 6,600,000.00 USD | 0.00 USD | 1,700.00 USD | 5,910.00 USD | 35,320.00 USD |
| `1D` | `58.80` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 35,140.00 USD | 14,730.00 USD | 23,630.00 USD |
| `7D` | `58.80` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 1,810.00 USD | 3,320.00 USD | 6,410.00 USD |
| `1D` | `58.90` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 19,290.00 USD | 124,640.00 USD | 91,310.00 USD |
| `7D` | `58.90` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 48,700.00 USD | 83,500.00 USD |
| `1D` | `59.00` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 151,460.00 USD | 57,130.00 USD | 134,010.00 USD |
| `7D` | `59.00` | 7,180,000.00 USD | 7,180,000.00 USD | 0.00 USD | 255,180.00 USD | 65,270.00 USD | 118,570.00 USD |
| `1D` | `59.10` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 191,140.00 USD | 49,070.00 USD | 186,370.00 USD |
| `7D` | `59.10` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 91,060.00 USD | 45,400.00 USD | 158,780.00 USD |
| `1D` | `59.20` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 159,140.00 USD | 75,750.00 USD | 96,020.00 USD |
| `7D` | `59.20` | 7,810,000.00 USD | 7,810,000.00 USD | 0.00 USD | 153,580.00 USD | 12,460.00 USD | 174,600.00 USD |
| `1D` | `59.30` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 306,360.00 USD | 73,700.00 USD | 143,250.00 USD |
| `7D` | `59.30` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD |
| `1D` | `59.40` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 78,860.00 USD | 57,010.00 USD | 76,960.00 USD |
| `7D` | `59.40` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 103,370.00 USD | 73,620.00 USD | 137,500.00 USD |
| `1D` | `59.50` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 119,350.00 USD | 57,690.00 USD | 28,370.00 USD |
| `7D` | `59.50` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD |
| `1D` | `59.60` | 6,720,000.00 USD | 6,720,000.00 USD | 0.00 USD | 62,780.00 USD | 68,870.00 USD | 18,340.00 USD |
| `7D` | `59.60` | 9,060,000.00 USD | 9,060,000.00 USD | 0.00 USD | 268,680.00 USD | 145,550.00 USD | 86,840.00 USD |
| `1D` | `59.70` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 20,820.00 USD | 30,890.00 USD | 94,130.00 USD |
| `7D` | `59.70` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 55,510.00 USD | 180,620.00 USD | 161,880.00 USD |
| `1D` | `59.80` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 40,970.00 USD | 37,360.00 USD | 10,870.00 USD |
| `7D` | `59.80` | 9,830,000.00 USD | 9,830,000.00 USD | 0.00 USD | 118,240.00 USD | 97,600.00 USD | 155,270.00 USD |
| `1D` | `59.90` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 112,870.00 USD | 21,300.00 USD | 80,370.00 USD |
| `7D` | `59.90` | 10,200,000.00 USD | 10,200,000.00 USD | 0.00 USD | 246,770.00 USD | 84,430.00 USD | 40,130.00 USD |
| `1D` | `60.00` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 182,880.00 USD | 64,320.00 USD | 69,570.00 USD |
| `7D` | `60.00` | 10,710,000.00 USD | 10,710,000.00 USD | 0.00 USD | 231,370.00 USD | 183,130.00 USD | 94,160.00 USD |
| `1D` | `60.10` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 95,780.00 USD | 40,330.00 USD | 71,530.00 USD |
| `7D` | `60.10` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 263,890.00 USD | 129,860.00 USD | 174,140.00 USD |
| `1D` | `60.20` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 119,070.00 USD | 37,570.00 USD | 96,900.00 USD |
| `7D` | `60.20` | 11,770,000.00 USD | 11,770,000.00 USD | 0.00 USD | 207,990.00 USD | 131,530.00 USD | 157,150.00 USD |
| `1D` | `60.30` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 97,720.00 USD | 71,550.00 USD | 82,910.00 USD |
| `7D` | `60.30` | 12,160,000.00 USD | 12,160,000.00 USD | 0.00 USD | 133,350.00 USD | 95,890.00 USD | 155,610.00 USD |
| `1D` | `60.40` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 168,700.00 USD | 45,820.00 USD | 60,640.00 USD |
| `7D` | `60.40` | 12,610,000.00 USD | 12,610,000.00 USD | 0.00 USD | 93,890.00 USD | 133,310.00 USD | 226,940.00 USD |
| `1D` | `60.50` | 8,650,000.00 USD | 8,650,000.00 USD | 0.00 USD | 69,310.00 USD | 43,330.00 USD | 63,140.00 USD |
| `7D` | `60.50` | 13,040,000.00 USD | 13,040,000.00 USD | 0.00 USD | 131,870.00 USD | 86,290.00 USD | 206,240.00 USD |
| `1D` | `60.60` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 69,460.00 USD | 36,940.00 USD | 5,340.00 USD |
| `7D` | `60.60` | 13,490,000.00 USD | 13,490,000.00 USD | 0.00 USD | 251,100.00 USD | 70,980.00 USD | 134,260.00 USD |
| `1D` | `60.70` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 56,630.00 USD | 36,190.00 USD | 985.52 USD |
| `7D` | `60.70` | 13,720,000.00 USD | 13,720,000.00 USD | 0.00 USD | 129,660.00 USD | 67,510.00 USD | 28,990.00 USD |
| `1D` | `60.80` | 8,950,000.00 USD | 8,950,000.00 USD | 0.00 USD | 22,530.00 USD | 12,680.00 USD | 55,210.00 USD |
| `7D` | `60.80` | 13,950,000.00 USD | 13,950,000.00 USD | 0.00 USD | 54,870.00 USD | 78,710.00 USD | 94,850.00 USD |
| `1D` | `60.90` | 9,050,000.00 USD | 9,050,000.00 USD | 0.00 USD | 57,090.00 USD | 23,580.00 USD | 22,850.00 USD |
| `7D` | `60.90` | 14,260,000.00 USD | 14,260,000.00 USD | 0.00 USD | 160,150.00 USD | 58,270.00 USD | 93,170.00 USD |
| `1D` | `61.00` | 9,130,000.00 USD | 9,130,000.00 USD | 0.00 USD | 46,000.00 USD | 6,970.00 USD | 28,080.00 USD |
| `7D` | `61.00` | 14,400,000.00 USD | 14,400,000.00 USD | 0.00 USD | 96,160.00 USD | 36,500.00 USD | 5,370.00 USD |
| `1D` | `61.10` | 9,160,000.00 USD | 9,160,000.00 USD | 0.00 USD | 10,450.00 USD | 3,540.00 USD | 11,490.00 USD |
| `7D` | `61.10` | 14,430,000.00 USD | 14,430,000.00 USD | 0.00 USD | 31,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `61.20` | 9,280,000.00 USD | 9,280,000.00 USD | 0.00 USD | 75,930.00 USD | 1,160.00 USD | 47,920.00 USD |
| `7D` | `61.20` | 14,670,000.00 USD | 14,670,000.00 USD | 0.00 USD | 116,610.00 USD | 74,510.00 USD | 52,570.00 USD |
| `1D` | `61.30` | 9,300,000.00 USD | 9,300,000.00 USD | 0.00 USD | 9,540.00 USD | 7,930.00 USD | 2,340.00 USD |
| `7D` | `61.30` | 14,810,000.00 USD | 14,810,000.00 USD | 0.00 USD | 51,130.00 USD | 35,650.00 USD | 55,130.00 USD |
| `1D` | `61.40` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 6,350.00 USD | 5,640.00 USD | 1,670.00 USD |
| `7D` | `61.40` | 15,000,000.00 USD | 15,000,000.00 USD | 0.00 USD | 89,350.00 USD | 41,800.00 USD | 59,330.00 USD |
| `1D` | `61.50` | 9,360,000.00 USD | 9,360,000.00 USD | 0.00 USD | 9,120.00 USD | 18,030.00 USD | 17,680.00 USD |
| `7D` | `61.50` | 15,100,000.00 USD | 15,100,000.00 USD | 0.00 USD | 19,810.00 USD | 35,300.00 USD | 36,110.00 USD |
| `1D` | `61.60` | 9,400,000.00 USD | 9,400,000.00 USD | 0.00 USD | 24,180.00 USD | 10,780.00 USD | 8,530.00 USD |
| `7D` | `61.60` | 15,350,000.00 USD | 15,350,000.00 USD | 0.00 USD | 54,240.00 USD | 63,390.00 USD | 132,550.00 USD |
| `1D` | `61.70` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 31,820.00 USD | 9,670.00 USD | 12,200.00 USD |
| `7D` | `61.70` | 15,560,000.00 USD | 15,560,000.00 USD | 0.00 USD | 84,300.00 USD | 11,330.00 USD | 114,420.00 USD |
| `1D` | `61.80` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 18,210.00 USD | 8,420.00 USD | 1,570.00 USD |
| `7D` | `61.80` | 15,830,000.00 USD | 15,830,000.00 USD | 0.00 USD | 160,110.00 USD | 48,140.00 USD | 69,850.00 USD |
| `1D` | `61.90` | 9,510,000.00 USD | 9,510,000.00 USD | 0.00 USD | 19,520.00 USD | 7,490.00 USD | 0.00 USD |
| `7D` | `61.90` | 15,970,000.00 USD | 15,970,000.00 USD | 0.00 USD | 72,380.00 USD | 29,730.00 USD | 35,860.00 USD |
| `1D` | `62.00` | 9,530,000.00 USD | 9,530,000.00 USD | 0.00 USD | 14,630.00 USD | 911.46 USD | 2,750.00 USD |
| `7D` | `62.00` | 16,090,000.00 USD | 16,090,000.00 USD | 0.00 USD | 56,450.00 USD | 13,260.00 USD | 49,920.00 USD |
| `1D` | `62.10` | 9,540,000.00 USD | 9,540,000.00 USD | 0.00 USD | 12,050.00 USD | 945.47 USD | 0.00 USD |
| `7D` | `62.10` | 16,150,000.00 USD | 16,150,000.00 USD | 0.00 USD | 36,500.00 USD | 12,820.00 USD | 13,950.00 USD |
| `1D` | `62.20` | 9,550,000.00 USD | 9,550,000.00 USD | 0.00 USD | 3,160.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.20` | 16,270,000.00 USD | 16,270,000.00 USD | 0.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD |
| `1D` | `62.30` | 9,560,000.00 USD | 9,560,000.00 USD | 0.00 USD | 464.20 USD | 260.05 USD | 8,390.00 USD |
| `7D` | `62.30` | 16,420,000.00 USD | 16,420,000.00 USD | 0.00 USD | 33,560.00 USD | 23,450.00 USD | 97,450.00 USD |
| `1D` | `62.40` | 9,560,000.00 USD | 9,560,000.00 USD | 0.00 USD | 565.97 USD | 0.00 USD | 129.78 USD |
| `7D` | `62.40` | 16,560,000.00 USD | 16,560,000.00 USD | 0.00 USD | 79,620.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `62.50` | 9,560,000.00 USD | 9,560,000.00 USD | 0.00 USD | 0.00 USD | 918.15 USD | 0.00 USD |
| `7D` | `62.50` | 16,650,000.00 USD | 16,650,000.00 USD | 0.00 USD | 44,300.00 USD | 14,320.00 USD | 26,610.00 USD |
| `7D` | `62.60` | 16,720,000.00 USD | 16,720,000.00 USD | 0.00 USD | 34,910.00 USD | 7,830.00 USD | 27,730.00 USD |
| `7D` | `62.70` | 16,800,000.00 USD | 16,800,000.00 USD | 0.00 USD | 22,020.00 USD | 12,490.00 USD | 47,090.00 USD |
| `7D` | `62.80` | 16,950,000.00 USD | 16,950,000.00 USD | 0.00 USD | 72,250.00 USD | 28,960.00 USD | 45,150.00 USD |
| `7D` | `62.90` | 17,040,000.00 USD | 17,040,000.00 USD | 0.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD |
| `7D` | `63.00` | 17,100,000.00 USD | 17,100,000.00 USD | 0.00 USD | 34,730.00 USD | 12,240.00 USD | 17,650.00 USD |
| `7D` | `63.10` | 17,140,000.00 USD | 17,140,000.00 USD | 0.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD |
| `7D` | `63.30` | 17,180,000.00 USD | 17,180,000.00 USD | 0.00 USD | 18,390.00 USD | 11,500.00 USD | 9,730.00 USD |
| `7D` | `63.40` | 17,210,000.00 USD | 17,210,000.00 USD | 0.00 USD | 13,220.00 USD | 1,320.00 USD | 9,960.00 USD |
| `7D` | `63.50` | 17,230,000.00 USD | 17,230,000.00 USD | 0.00 USD | 6,620.00 USD | 15,810.00 USD | 4,760.00 USD |
| `7D` | `63.60` | 17,330,000.00 USD | 17,330,000.00 USD | 0.00 USD | 63,480.00 USD | 20,800.00 USD | 11,880.00 USD |
| `7D` | `63.70` | 17,410,000.00 USD | 17,410,000.00 USD | 0.00 USD | 21,940.00 USD | 18,810.00 USD | 35,480.00 USD |
| `7D` | `63.80` | 17,470,000.00 USD | 17,470,000.00 USD | 0.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD |
| `7D` | `63.90` | 17,500,000.00 USD | 17,500,000.00 USD | 0.00 USD | 7,650.00 USD | 12,840.00 USD | 8,940.00 USD |
| `7D` | `64.00` | 17,540,000.00 USD | 17,540,000.00 USD | 0.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD |
| `7D` | `64.10` | 17,570,000.00 USD | 17,570,000.00 USD | 0.00 USD | 20,350.00 USD | 667.05 USD | 10,640.00 USD |
| `7D` | `64.20` | 17,620,000.00 USD | 17,620,000.00 USD | 0.00 USD | 28,840.00 USD | 14,530.00 USD | 584.77 USD |
| `7D` | `64.40` | 17,670,000.00 USD | 17,670,000.00 USD | 0.00 USD | 2,540.00 USD | 20,590.00 USD | 29,110.00 USD |
| `7D` | `64.50` | 17,700,000.00 USD | 17,700,000.00 USD | 0.00 USD | 7,700.00 USD | 7,120.00 USD | 13,310.00 USD |
| `7D` | `64.60` | 17,740,000.00 USD | 17,740,000.00 USD | 0.00 USD | 32,220.00 USD | 14,180.00 USD | 108.50 USD |
| `7D` | `64.70` | 17,810,000.00 USD | 17,810,000.00 USD | 0.00 USD | 39,430.00 USD | 23,030.00 USD | 3,870.00 USD |
| `7D` | `64.80` | 17,850,000.00 USD | 17,850,000.00 USD | 0.00 USD | 7,540.00 USD | 8,210.00 USD | 20,430.00 USD |
| `7D` | `64.90` | 17,890,000.00 USD | 17,890,000.00 USD | 0.00 USD | 25,320.00 USD | 8,010.00 USD | 9,860.00 USD |
| `7D` | `65.00` | 17,910,000.00 USD | 17,910,000.00 USD | 0.00 USD | 1,790.00 USD | 9,480.00 USD | 13,480.00 USD |
| `7D` | `65.10` | 17,970,000.00 USD | 17,970,000.00 USD | 0.00 USD | 5,810.00 USD | 14,250.00 USD | 37,140.00 USD |
| `7D` | `65.20` | 18,010,000.00 USD | 18,010,000.00 USD | 0.00 USD | 10,380.00 USD | 1,630.00 USD | 28,280.00 USD |
| `7D` | `65.30` | 18,060,000.00 USD | 18,060,000.00 USD | 0.00 USD | 22,330.00 USD | 9,180.00 USD | 17,890.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `421.26M` | Total OI Tokens: `7,557,612.7 LTC`
  * 1h OI Change: `-0.71%` | 4h OI Change: `-6.22%` | 24h OI Change: `-11.07%`
  * Exchange Breakdown: Binance=`76.31M` | Bybit=`66.60M` | OKX=`33.99M` | Hyperliquid=`21.80M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.23K` | Last 24h: `36.85K` | Last 3d: `60.07K` | Last 7d: `106.71K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0031%` | **USDT OKX** | `-0.0025%` |
| **USDT Bybit** | `0.0072%` | **USDT KuCoin** | `0.0058%` |
| **USDT MEXC** | `0.0031%` | **USDT BingX** | `0.0097%` |
| **USDT Gate** | `0.0017%` | **USDT Bitget** | `0.0096%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `54.92%` | `45.08%` | `1.22` | 3,510,000.00 USD |
| `15M` | `Binance` | `52.84%` | `47.16%` | `1.12` | 1,130,000.00 USD |
| `15M` | `OKX` | `48.23%` | `51.77%` | `0.93` | 362,720.00 USD |
| `15M` | `Bybit` | `50.26%` | `49.74%` | `1.01` | 271,570.00 USD |
| `15M` | `KuCoin` | `47.73%` | `52.27%` | `0.91` | 146,310.00 USD |
| `15M` | `Gate` | `56.97%` | `43.03%` | `1.32` | 484,520.00 USD |
| `15M` | `Bitget` | `30.91%` | `69.09%` | `0.45` | 63,540.00 USD |
| `15M` | `BingX` | `48.99%` | `51.01%` | `0.96` | 143,770.00 USD |
| `15M` | `MEXC` | `56.51%` | `43.49%` | `1.30` | 187,700.00 USD |
| `15M` | `Bitunix` | `52.97%` | `47.03%` | `1.13` | 67,670.00 USD |
| `15M` | `Hyperliquid` | `38.47%` | `61.53%` | `0.63` | 52,540.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.6%` | `51.4%` | `0.95` | 212,080.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `83.33%` | `16.67%` | `5.00` | 334,230.00 USD |
| `15M` | `HTX` | `49.9%` | `50.1%` | `1.00` | 2,050.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `77.82%` | `22.18%` | `3.51` | 47,430.00 USD |
| `15M` | `Aster` | `33.24%` | `66.76%` | `0.50` | 1,840.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `52.84%` | `47.16%` | `1.12` | 1,130,000.00 USD |
| `15M` | `Global Accounts` | `54.92%` | `45.08%` | `1.22` | 3,510,000.00 USD |
| `1H` | `LTC` | `50.23%` | `49.77%` | `1.01` | 16,560,000.00 USD |
| `1H` | `Binance` | `44.14%` | `55.86%` | `0.79` | 6,350,000.00 USD |
| `1H` | `OKX` | `50.6%` | `49.4%` | `1.02` | 1,480,000.00 USD |
| `1H` | `Bybit` | `50.49%` | `49.51%` | `1.02` | 1,320,000.00 USD |
| `1H` | `KuCoin` | `45.02%` | `54.98%` | `0.82` | 591,720.00 USD |
| `1H` | `Gate` | `51.21%` | `48.79%` | `1.05` | 1,460,000.00 USD |
| `1H` | `Bitget` | `30.5%` | `69.5%` | `0.44` | 323,940.00 USD |
| `1H` | `BingX` | `53.22%` | `46.78%` | `1.14` | 557,750.00 USD |
| `1H` | `MEXC` | `48.89%` | `51.11%` | `0.96` | 923,080.00 USD |
| `1H` | `Bitunix` | `47%` | `53%` | `0.89` | 338,710.00 USD |
| `1H` | `Hyperliquid` | `36.61%` | `63.39%` | `0.58` | 163,050.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.43%` | `50.57%` | `0.98` | 1,540,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `93.18%` | `6.82%` | `13.66` | 1,220,000.00 USD |
| `1H` | `HTX` | `50.02%` | `49.98%` | `1.00` | 7,140.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `41.67%` | `58.33%` | `0.71` | 237,270.00 USD |
| `1H` | `Aster` | `15.84%` | `84.16%` | `0.19` | 25,110.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `44.14%` | `55.86%` | `0.79` | 6,350,000.00 USD |
| `1H` | `Global Accounts` | `50.23%` | `49.77%` | `1.01` | 16,560,000.00 USD |
| `4H` | `LTC` | `47.67%` | `52.33%` | `0.91` | 112,470,000.00 USD |
| `4H` | `Binance` | `45.1%` | `54.9%` | `0.82` | 41,550,000.00 USD |
| `4H` | `OKX` | `49.71%` | `50.29%` | `0.99` | 12,490,000.00 USD |
| `4H` | `Bybit` | `45.2%` | `54.8%` | `0.82` | 12,760,000.00 USD |
| `4H` | `KuCoin` | `47.58%` | `52.42%` | `0.91` | 2,780,000.00 USD |
| `4H` | `Gate` | `54.06%` | `45.94%` | `1.18` | 10,690,000.00 USD |
| `4H` | `Bitget` | `47.26%` | `52.74%` | `0.90` | 5,190,000.00 USD |
| `4H` | `BingX` | `46.45%` | `53.55%` | `0.87` | 3,030,000.00 USD |
| `4H` | `MEXC` | `44.88%` | `55.12%` | `0.81` | 6,880,000.00 USD |
| `4H` | `Bitunix` | `47.57%` | `52.43%` | `0.91` | 2,900,000.00 USD |
| `4H` | `Hyperliquid` | `50.91%` | `49.09%` | `1.04` | 1,960,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.63%` | `50.37%` | `0.99` | 8,850,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `66.33%` | `33.67%` | `1.97` | 2,500,000.00 USD |
| `4H` | `HTX` | `51.1%` | `48.9%` | `1.04` | 123,670.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `47.54%` | `52.46%` | `0.91` | 642,310.00 USD |
| `4H` | `Aster` | `39.96%` | `60.04%` | `0.67` | 124,680.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `45.1%` | `54.9%` | `0.82` | 41,550,000.00 USD |
| `4H` | `Global Accounts` | `47.67%` | `52.33%` | `0.91` | 112,470,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `57.25` | `57.29` | `57.25` | `57.45` | `57.14` | 618,298.97 USD | 355,257.55 USD | 263,041.42 USD | 92,216.13 USD | `+14.91%` | `5B / 2S` |
| `0:00 UTC` | `56.60` | `56.15` | `56.60` | `57.32` | `55.30` | 7,177,688.25 USD | 3,006,268.39 USD | 4,171,419.87 USD | -1,165,151.48 USD | `-16.23%` | `6B / 23S` |
| `5:00 UTC` | `55.00` | `54.96` | `55.00` | `55.59` | `54.17` | 11,110,862.71 USD | 4,658,705.25 USD | 6,452,157.46 USD | -1,793,452.21 USD | `-16.14%` | `3B / 23S` |
| `0:00 UTC` | `55.38` | `55.12` | `55.38` | `55.47` | `54.53` | 4,979,082.77 USD | 3,102,786.44 USD | 1,876,296.33 USD | 1,226,490.12 USD | `+24.63%` | `16B / 3S` |
| `5:00 UTC` | `55.59` | `55.69` | `55.59` | `56.05` | `55.36` | 3,537,942.18 USD | 1,760,395.33 USD | 1,777,546.85 USD | -17,151.52 USD | `-0.48%` | `7B / 9S` |
| `0:00 UTC` | `55.81` | `55.87` | `55.81` | `56.11` | `55.47` | 1,595,751.03 USD | 493,401.32 USD | 1,102,349.71 USD | -608,948.39 USD | `-38.16%` | `2B / 24S` |
| `5:00 UTC` | `55.47` | `55.42` | `55.47` | `55.61` | `55.22` | 1,153,425.44 USD | 492,176.46 USD | 661,248.98 USD | -169,072.53 USD | `-14.66%` | `1B / 7S` |
| `0:00 UTC` | `55.25` | `55.13` | `55.25` | `55.55` | `54.80` | 1,975,627.97 USD | 1,071,271.32 USD | 904,356.64 USD | 166,914.68 USD | `+8.45%` | `21B / 8S` |
| `5:00 UTC` | `55.64` | `55.52` | `55.64` | `55.80` | `55.11` | 1,258,609.21 USD | 696,271.74 USD | 562,337.48 USD | 133,934.26 USD | `+10.64%` | `12B / 7S` |
| `0:00 UTC` | `55.55` | `55.60` | `55.55` | `55.75` | `55.48` | 210,332.85 USD | 108,164.13 USD | 102,168.72 USD | 5,995.42 USD | `+2.85%` | `8B / 1S` |

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
| `5m` | 35,200.00 USD | 7,230.00 USD | **`ACCUMULATION`** |
| `15m` | 146,940.00 USD | 235,330.00 USD | **`ACCUMULATION`** |
| `30m` | 190,560.00 USD | 492,260.00 USD | **`ACCUMULATION`** |
| `1h` | 205,870.00 USD | 23,150.00 USD | **`ACCUMULATION`** |
| `2h` | -1,840,000.00 USD | -2,820,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,680,000.00 USD | -2,640,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,430,000.00 USD | -3,480,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -222,700.00 USD | -3,020,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 512,780.00 USD | -437,030.00 USD | **`ACCUMULATION`** |
| `24h` | 408,510.00 USD | -4,790,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 3,740,000.00 USD | -23,640,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -21,780,000.00 USD | -191,570,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+35.20K` | 15m=`+146.94K` | 1h=`+205.87K` | 24h=`+408.51K`
* Futures Capital Netflows: 5m=`+7.23K` | 15m=`+235.33K` | 1h=`+23.15K` | 24h=`-4.79M`
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
  * `2026-10-30 03:29:36 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:00:36 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:00:36 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:59:36 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:01:36 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:01:36 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:01:36 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:36 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:36 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:36 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:01:36 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `54.92` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `53.79` (Risk Distance: `1.13` pts)
  * +2.5R Take Profit: `57.76`
  * Mathematical Lot Sizing: **`8.81 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `55.56` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `56.70` (Risk Distance: `1.13` pts)
  * +2.5R Take Profit: `52.73`
  * Mathematical Lot Sizing: **`8.81 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`56.06`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
