# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 04:38:02 IST` (`2026-10-29 23:08:02 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `54.98` | **Live Ask Quote**: `55.28` | **Mid Price**: `55.13`
- **Spread Points**: `300.00` | **Spread BPS**: `54.42 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `55.13` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `55.52` | Lower -3.00σ Band: `54.74`
  * Upper +2.51σ Band: `55.43` | Lower -2.51σ Band: `54.83`
  * Upper +2.01σ Band: `55.36` | Lower -2.01σ Band: `54.90`
  * Upper +2.00σ Band: `55.35` | Lower -2.00σ Band: `54.91`
  * Upper +1.28σ Band: `55.28` | Lower -1.28σ Band: `54.98`
  * Upper +1.00σ Band: `55.24` | Lower -1.00σ Band: `55.02`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`55.13` | EMA-20=`55.13` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`55.13` (Slope: `+0.0000`) | EMA-100=`55.13`
  * Institutional Anchors: EMA-144=`55.13` | EMA-200=`55.13` (Slope: `+0.0000`) | EMA-233=`55.13`
- **Range Boundaries**: 24H High=`55.68` | 24H Low=`54.58` | Weekly High=`56.23` | Weekly Low=`54.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `55.60` (Distance: `-0.77%`)
  * Point of Control (POC) = `55.28` (Distance: `-0.21%`)
  * Value Area Low (VAL) = `55.03` (Distance: `+0.24%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.40` | POC=`57.72` | VAL=`56.83`
  * Prior Day Extremes: PDH=`59.52` | PDL=`54.18` | PDC=`54.46`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`57.97` | Weekly POC=`56.45` | Weekly VAL=`56.01`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`55.89` | Low=`54.61`
  * London Session (08:00-16:00 UTC): High=`55.35` | Low=`54.91`
  * New York Session (13:00-21:00 UTC): High=`55.46` | Low=`54.80`
  * Initial Balance (First Hour): IB High=`55.30` | IB Low=`54.96`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `54.91` - `55.35`
  * Optimal Trade Entry (OTE 0.705): `55.24`
  * Structural Invalidation Anchor (0.786): `55.57`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `55.41` | `55.50` | `55.33` | `55.42` | `4,239` | 234,798.70 USD | 27,941.94 USD | `+11.90%` | -3,568,654.12 USD | `+0.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `55.43` | `55.51` | `55.17` | `55.24` | `7,574` | 418,786.49 USD | -92,243.77 USD | `-22.03%` | -3,660,897.89 USD | `-0.32` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `55.24` | `55.25` | `55.19` | `55.20` | `1,176` | 64,941.53 USD | 8,184.62 USD | `+12.60%` | -3,652,713.27 USD | `+0.38` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `55.57` | `55.86` | `55.48` | `55.67` | `16,740` | 931,905.62 USD | 8,281.08 USD | `+0.89%` | -3,438,420.69 USD | `+0.24` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `55.66` | `55.67` | `55.33` | `55.42` | `16,479` | 914,407.56 USD | -146,552.93 USD | `-16.03%` | -3,584,973.62 USD | `-0.04` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `55.43` | `55.51` | `55.17` | `55.21` | `8,844` | 488,871.16 USD | -87,524.90 USD | `-17.90%` | -3,672,498.52 USD | `+0.08` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `54.64` | `56.10` | `54.52` | `55.28` | `203,261` | 11,266,201.42 USD | 431,317.68 USD | `+3.83%` | -3,885,763.65 USD | `+0.71` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `55.28` | `55.86` | `54.79` | `55.42` | `91,727` | 5,080,550.36 USD | 162,577.09 USD | `+3.20%` | -3,723,186.55 USD | `+0.33` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `55.43` | `55.51` | `55.17` | `55.19` | `8,712` | 481,602.82 USD | -86,124.40 USD | `-17.88%` | -3,809,310.96 USD | `+0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | -1,031,107.81 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | -891,821.26 USD | `+0.52` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `55.21` | `702,792` | 39,072,905.31 USD | -2,915,529.34 USD | `-7.46%` | -3,807,350.60 USD | `-1.96` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `57.20` | `58.23` | `56.92` | `57.04` | `229,127` | 13,178,164.26 USD | -500,207.83 USD | `-3.80%` | -1,732,502.54 USD | `+1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `57.04` | `58.16` | `56.85` | `58.00` | `178,996` | 10,300,529.12 USD | 452,809.17 USD | `+4.40%` | -1,279,693.37 USD | `+1.27` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | -1,031,107.81 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | -891,821.26 USD | `+0.52` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `55.21` | `702,792` | 39,072,905.31 USD | -2,915,529.34 USD | `-7.46%` | -3,807,350.60 USD | `-1.96` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`55.13`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:36:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1082` | `0xeadc...9d55` | `LONG` | 2,018,998.94 USD | `36,463.77` | `52.78` | `55.36` | `0.000000` | 94,323.00 USD | `+4.67%` | `10X Cross` |
| `1101` | `0x9aa5...58af` | `SHORT` | 2,002,903.24 USD | `36,177.65` | `71.22` | `55.36` | `305.49` | 573,583.43 USD | `+28.64%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `58.48` | 6,839.59 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 6.84K USD at 58.4830 USD [API] | `2026-10-28 17:30:23` |
| `ANNOUNCEMENT` | `INFO` | `58.49` | 5,232.43 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.23K USD at 58.4890 USD [API] | `2026-10-28 17:30:23` |
| `ANNOUNCEMENT` | `INFO` | `58.55` | 5,269.68 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.27K USD at 58.5520 USD [API] | `2026-10-28 17:40:25` |
| `ANNOUNCEMENT` | `INFO` | `58.13` | 7,507.30 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 58.1330 USD [API] | `2026-10-28 18:16:41` |
| `ANNOUNCEMENT` | `INFO` | `59.03` | 2,999.90 USD | `-` | `NEWS_INTEL` | `-` | #LTC Liquidated Long: 3.00K USD at 59.0300 USD [API] | `2026-10-28 16:25:44` |
| `ANNOUNCEMENT` | `INFO` | `58.46` | 7,506.46 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 58.4570 USD [API] | `2026-10-28 18:52:14` |
| `ANNOUNCEMENT` | `INFO` | `58.46` | 7,506.46 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 58.4570 USD [API] | `2026-10-28 18:52:14` |
| `ANNOUNCEMENT` | `INFO` | `58.46` | 5,364.51 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 5.36K USD at 58.4560 USD [API] | `2026-10-28 18:52:14` |
| `ANNOUNCEMENT` | `INFO` | `59.08` | 6,432.04 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 6.43K USD at 59.0800 USD [API] | `2026-10-28 19:23:55` |
| `ANNOUNCEMENT` | `INFO` | `59.10` | 7,180.65 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 7.18K USD at 59.1000 USD [API] | `2026-10-28 19:28:02` |
| `ANNOUNCEMENT` | `INFO` | `59.44` | 7,505.45 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 7.51K USD at 59.4350 USD [API] | `2026-10-28 19:51:29` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.13%`) | Long MP=`54.26` (Vol: 204,200.00 USD, Dist: `--2.39%`)
  * 48H Horizon: Short MP=`58.99` (Vol: 284,700.00 USD, Dist: `+6.11%`) | Long MP=`54.29` (Vol: 204,200.00 USD, Dist: `--2.34%`)
  * 3D Horizon: Short MP=`58.99` (Vol: 284,700.00 USD, Dist: `+6.11%`) | Long MP=`54.29` (Vol: 204,200.00 USD, Dist: `--2.34%`)
  * 7D Horizon: Short MP=`58.99` (Vol: 284,700.00 USD, Dist: `+6.11%`) | Long MP=`54.29` (Vol: 204,200.00 USD, Dist: `--2.34%`)
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
| `Live` | `Long Liquidation` | `49.15` | 5,740.00 USD | 669,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.25` | 263.49 USD | 664,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.30` | 2,740,000.00 USD | 2,740,000.00 USD | 13,300.00 USD | 3,500.00 USD | 367.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.30` | 8,000,000.00 USD | 8,000,000.00 USD | 15,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.35` | 5,230.00 USD | 663,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.40` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 626.48 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.40` | 7,980,000.00 USD | 7,980,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.45` | 1,960.00 USD | 658,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.50` | 2,720,000.00 USD | 2,720,000.00 USD | 1,180.00 USD | 4,790.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.50` | 7,980,000.00 USD | 7,980,000.00 USD | 1,130.00 USD | 6,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.55` | 18,010.00 USD | 656,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.60` | 2,700,000.00 USD | 2,700,000.00 USD | 785.85 USD | 4,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.60` | 7,970,000.00 USD | 7,970,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.65` | 92,360.00 USD | 638,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.70` | 2,700,000.00 USD | 2,700,000.00 USD | 1,320.00 USD | 0.00 USD | 301.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.70` | 7,950,000.00 USD | 7,950,000.00 USD | 788.92 USD | 0.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.75` | 1,580.00 USD | 546,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.80` | 2,690,000.00 USD | 2,690,000.00 USD | 667.20 USD | 733.27 USD | 11,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.80` | 7,950,000.00 USD | 7,950,000.00 USD | 7,660.00 USD | 8,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `49.90` | 2,680,000.00 USD | 2,680,000.00 USD | 17,040.00 USD | 7,110.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.90` | 7,930,000.00 USD | 7,930,000.00 USD | 45,030.00 USD | 5,410.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.95` | 28,540.00 USD | 544,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.00` | 2,630,000.00 USD | 2,630,000.00 USD | 4,470.00 USD | 5,550.00 USD | 40,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.00` | 7,880,000.00 USD | 7,880,000.00 USD | 22,100.00 USD | 7,630.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.05` | 1,820.00 USD | 516,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.10` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 3,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.10` | 7,820,000.00 USD | 7,820,000.00 USD | 363.50 USD | 682.90 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.20` | 7,820,000.00 USD | 7,820,000.00 USD | 6,960.00 USD | 500.40 USD | 34,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.25` | 102.51 USD | 514,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.30` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 333.03 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.30` | 7,780,000.00 USD | 7,780,000.00 USD | 16,270.00 USD | 3,640.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.35` | 1,030.00 USD | 514,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.40` | 2,580,000.00 USD | 2,580,000.00 USD | 349.63 USD | 2,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.40` | 7,760,000.00 USD | 7,760,000.00 USD | 23,520.00 USD | 19,110.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,720.00 USD | 513,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.50` | 7,680,000.00 USD | 7,680,000.00 USD | 24,840.00 USD | 6,790.00 USD | 43,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.55` | 84,100.00 USD | 508,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.60` | 7,610,000.00 USD | 7,610,000.00 USD | 52,670.00 USD | 17,830.00 USD | 22,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.70` | 7,510,000.00 USD | 7,510,000.00 USD | 53,670.00 USD | 24,710.00 USD | 32,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.75` | 9,050.00 USD | 424,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.80` | 2,580,000.00 USD | 2,580,000.00 USD | 5,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.80` | 7,400,000.00 USD | 7,400,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.85` | 263.40 USD | 415,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.90` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 260.05 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.90` | 7,310,000.00 USD | 7,310,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.95` | 245.07 USD | 414,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.00` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 129.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.00` | 7,050,000.00 USD | 7,050,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.10` | 2,560,000.00 USD | 2,560,000.00 USD | 263.90 USD | 1,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.10` | 6,930,000.00 USD | 6,930,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.15` | 219,370.00 USD | 414,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.20` | 2,560,000.00 USD | 2,560,000.00 USD | 1,100.00 USD | 1,130.00 USD | 327.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.20` | 6,850,000.00 USD | 6,850,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.30` | 2,560,000.00 USD | 2,560,000.00 USD | 20,430.00 USD | 5,150.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.30` | 6,780,000.00 USD | 6,780,000.00 USD | 19,510.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.40` | 2,510,000.00 USD | 2,510,000.00 USD | 17,510.00 USD | 7,090.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.40` | 6,700,000.00 USD | 6,700,000.00 USD | 71,090.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.45` | 20,410.00 USD | 195,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.50` | 2,480,000.00 USD | 2,480,000.00 USD | 11,450.00 USD | 8,980.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.50` | 6,560,000.00 USD | 6,560,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.55` | 551.07 USD | 174,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.60` | 2,450,000.00 USD | 2,450,000.00 USD | 8,800.00 USD | 7,990.00 USD | 4,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.60` | 6,460,000.00 USD | 6,460,000.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.65` | 8,810.00 USD | 174,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.70` | 2,430,000.00 USD | 2,430,000.00 USD | 4,980.00 USD | 4,150.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.70` | 6,400,000.00 USD | 6,400,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.75` | 6,480.00 USD | 165,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.80` | 2,420,000.00 USD | 2,420,000.00 USD | 13,220.00 USD | 2,080.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.80` | 6,360,000.00 USD | 6,360,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.85` | 13,890.00 USD | 159,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.90` | 2,390,000.00 USD | 2,390,000.00 USD | 12,520.00 USD | 21,470.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.90` | 6,310,000.00 USD | 6,310,000.00 USD | 5,870.00 USD | 15,810.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.95` | 19,580.00 USD | 145,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.00` | 2,350,000.00 USD | 2,350,000.00 USD | 25,510.00 USD | 8,240.00 USD | 23,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.00` | 6,280,000.00 USD | 6,280,000.00 USD | 64,300.00 USD | 20,800.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.05` | 283.15 USD | 125,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.10` | 2,290,000.00 USD | 2,290,000.00 USD | 27,630.00 USD | 5,780.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 6,180,000.00 USD | 6,180,000.00 USD | 24,220.00 USD | 18,810.00 USD | 35,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.15` | 7,510.00 USD | 125,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.20` | 2,220,000.00 USD | 2,220,000.00 USD | 20,520.00 USD | 10,460.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 6,100,000.00 USD | 6,100,000.00 USD | 38,380.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.25` | 3,620.00 USD | 117,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.30` | 2,180,000.00 USD | 2,180,000.00 USD | 38,870.00 USD | 8,170.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 6,040,000.00 USD | 6,040,000.00 USD | 18,740.00 USD | 12,840.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.35` | 3,020.00 USD | 114,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.40` | 2,110,000.00 USD | 2,110,000.00 USD | 11,440.00 USD | 7,510.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 6,000,000.00 USD | 6,000,000.00 USD | 20,580.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.45` | 3,830.00 USD | 111,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.50` | 2,090,000.00 USD | 2,090,000.00 USD | 48,310.00 USD | 13,510.00 USD | 998.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.50` | 5,940,000.00 USD | 5,940,000.00 USD | 33,240.00 USD | 667.05 USD | 11,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.55` | 8,700.00 USD | 107,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.60` | 2,030,000.00 USD | 2,030,000.00 USD | 4,750.00 USD | 9,470.00 USD | 506.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.60` | 5,900,000.00 USD | 5,900,000.00 USD | 74,610.00 USD | 14,530.00 USD | 584.77 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.70` | 2,010,000.00 USD | 2,010,000.00 USD | 13,770.00 USD | 7,610.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.70` | 5,810,000.00 USD | 5,810,000.00 USD | 20,250.00 USD | 43,820.00 USD | 62,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.75` | 7,290.00 USD | 98,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.80` | 1,970,000.00 USD | 1,970,000.00 USD | 14,400.00 USD | 16,680.00 USD | 74,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.80` | 5,680,000.00 USD | 5,680,000.00 USD | 46,600.00 USD | 29,900.00 USD | 108.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.85` | 21,120.00 USD | 91,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.90` | 1,870,000.00 USD | 1,870,000.00 USD | 40,590.00 USD | 12,380.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.90` | 5,610,000.00 USD | 5,610,000.00 USD | 51,920.00 USD | 26,170.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.95` | 25,840.00 USD | 70,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.00` | 1,810,000.00 USD | 1,810,000.00 USD | 4,280.00 USD | 4,790.00 USD | 1,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.00` | 5,490,000.00 USD | 5,490,000.00 USD | 18,990.00 USD | 8,880.00 USD | 55,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.05` | 900.26 USD | 44,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.10` | 1,800,000.00 USD | 1,800,000.00 USD | 22,820.00 USD | 8,110.00 USD | 54,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.10` | 5,410,000.00 USD | 5,410,000.00 USD | 52,760.00 USD | 36,340.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.15` | 2,640.00 USD | 43,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.20` | 1,710,000.00 USD | 1,710,000.00 USD | 68,490.00 USD | 24,650.00 USD | 63,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.20` | 5,310,000.00 USD | 5,310,000.00 USD | 141,420.00 USD | 38,500.00 USD | 27,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.25` | 911.64 USD | 40,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.30` | 1,560,000.00 USD | 1,560,000.00 USD | 27,380.00 USD | 24,540.00 USD | 41,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.30` | 5,100,000.00 USD | 5,100,000.00 USD | 63,050.00 USD | 18,150.00 USD | 37,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.35` | 2,120.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.40` | 1,460,000.00 USD | 1,460,000.00 USD | 14,390.00 USD | 14,900.00 USD | 75,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.40` | 4,990,000.00 USD | 4,990,000.00 USD | 48,160.00 USD | 18,090.00 USD | 95,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.45` | 4,880.00 USD | 37,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.50` | 1,360,000.00 USD | 1,360,000.00 USD | 14,780.00 USD | 11,880.00 USD | 7,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.50` | 4,820,000.00 USD | 4,820,000.00 USD | 49,490.00 USD | 8,960.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.60` | 1,320,000.00 USD | 1,320,000.00 USD | 74,660.00 USD | 18,710.00 USD | 1,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.60` | 4,750,000.00 USD | 4,750,000.00 USD | 53,580.00 USD | 6,140.00 USD | 98,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.65` | 350.87 USD | 32,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.70` | 1,230,000.00 USD | 1,230,000.00 USD | 5,710.00 USD | 8,090.00 USD | 465.28 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.70` | 4,590,000.00 USD | 4,590,000.00 USD | 131,400.00 USD | 16,400.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.75` | 148.35 USD | 32,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.80` | 1,220,000.00 USD | 1,220,000.00 USD | 16,800.00 USD | 5,480.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.80` | 4,430,000.00 USD | 4,430,000.00 USD | 99,150.00 USD | 80,510.00 USD | 126,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.85` | 2,130.00 USD | 32,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.90` | 1,190,000.00 USD | 1,190,000.00 USD | 7,480.00 USD | 28,010.00 USD | 125,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.90` | 4,130,000.00 USD | 4,130,000.00 USD | 111,970.00 USD | 56,750.00 USD | 123,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.95` | 27,050.00 USD | 30,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.00` | 1,030,000.00 USD | 1,030,000.00 USD | 28,730.00 USD | 24,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.00` | 3,830,000.00 USD | 3,830,000.00 USD | 344,710.00 USD | 148,420.00 USD | 271,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.05` | 219.44 USD | 3,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.10` | 975,740.00 USD | 975,740.00 USD | 23,830.00 USD | 5,860.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.10` | 3,070,000.00 USD | 3,070,000.00 USD | 234,120.00 USD | 45,470.00 USD | 184,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.15` | 3,080.00 USD | 3,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.20` | 944,540.00 USD | 944,540.00 USD | 54,060.00 USD | 12,370.00 USD | 108,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.20` | 2,600,000.00 USD | 2,600,000.00 USD | 234,980.00 USD | 155,540.00 USD | 128,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.30` | 769,790.00 USD | 769,790.00 USD | 127,400.00 USD | 36,500.00 USD | 142,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.30` | 2,080,000.00 USD | 2,080,000.00 USD | 339,300.00 USD | 131,670.00 USD | 185,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.40` | 463,000.00 USD | 463,000.00 USD | 37,530.00 USD | 43,760.00 USD | 78,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.40` | 1,430,000.00 USD | 1,430,000.00 USD | 304,270.00 USD | 13,830.00 USD | 92,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.50` | 303,430.00 USD | 303,430.00 USD | 9,670.00 USD | 24,030.00 USD | 144,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.50` | 1,020,000.00 USD | 1,020,000.00 USD | 159,720.00 USD | 36,920.00 USD | 237,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.60` | 125,680.00 USD | 125,680.00 USD | 18,470.00 USD | 15,070.00 USD | 14,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.60` | 584,340.00 USD | 584,340.00 USD | 0.00 USD | 1,930.00 USD | 72,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.70` | 77,810.00 USD | 77,810.00 USD | 0.00 USD | 0.00 USD | 57,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.70` | 510,010.00 USD | 510,010.00 USD | 0.00 USD | 0.00 USD | 173,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.80` | 20,710.00 USD | 20,710.00 USD | 0.00 USD | 9,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.10` | 11,290.00 USD | 11,290.00 USD | 0.00 USD | 0.00 USD | 189.61 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.20` | 11,100.00 USD | 11,100.00 USD | 11,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.20` | 336,630.00 USD | 336,630.00 USD | 336,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.50` | 326,800.00 USD | 326,800.00 USD | 326,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.60` | 753,140.00 USD | 753,140.00 USD | 426,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.70` | 407.86 USD | 407.86 USD | 0.00 USD | 0.00 USD | 407.86 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.70` | 959,560.00 USD | 959,560.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.80` | 63,390.00 USD | 63,390.00 USD | 0.00 USD | 16,300.00 USD | 46,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.80` | 1,050,000.00 USD | 1,050,000.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.90` | 342,140.00 USD | 342,140.00 USD | 137,200.00 USD | 1,440.00 USD | 140,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.90` | 1,260,000.00 USD | 1,260,000.00 USD | 141,330.00 USD | 65,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.00` | 541,410.00 USD | 541,410.00 USD | 139,840.00 USD | 0.00 USD | 59,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.00` | 1,680,000.00 USD | 1,680,000.00 USD | 181,230.00 USD | 98,600.00 USD | 147,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.10` | 849,920.00 USD | 849,920.00 USD | 105,950.00 USD | 28,010.00 USD | 174,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.10` | 2,010,000.00 USD | 2,010,000.00 USD | 121,920.00 USD | 144,120.00 USD | 61,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.20` | 1,100,000.00 USD | 1,100,000.00 USD | 96,820.00 USD | 83,660.00 USD | 71,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.20` | 2,430,000.00 USD | 2,430,000.00 USD | 104,510.00 USD | 72,410.00 USD | 240,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.30` | 1,180,000.00 USD | 1,180,000.00 USD | 464.20 USD | 37,150.00 USD | 38,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.30` | 2,780,000.00 USD | 2,780,000.00 USD | 91,850.00 USD | 128,970.00 USD | 131,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.40` | 1,490,000.00 USD | 1,490,000.00 USD | 39,090.00 USD | 43,300.00 USD | 225,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.40` | 3,250,000.00 USD | 3,250,000.00 USD | 215,940.00 USD | 116,750.00 USD | 137,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.50` | 1,860,000.00 USD | 1,860,000.00 USD | 117,430.00 USD | 142,630.00 USD | 114,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.50` | 3,510,000.00 USD | 3,510,000.00 USD | 128,680.00 USD | 125,310.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.60` | 2,070,000.00 USD | 2,070,000.00 USD | 34,340.00 USD | 101,890.00 USD | 77,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.60` | 4,000,000.00 USD | 4,000,000.00 USD | 363,190.00 USD | 126,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.70` | 2,650,000.00 USD | 2,650,000.00 USD | 203,710.00 USD | 24,030.00 USD | 345,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.70` | 4,330,000.00 USD | 4,330,000.00 USD | 110,940.00 USD | 121,500.00 USD | 96,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.80` | 2,980,000.00 USD | 2,980,000.00 USD | 196,380.00 USD | 17,250.00 USD | 116,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.80` | 4,840,000.00 USD | 4,840,000.00 USD | 153,580.00 USD | 92,780.00 USD | 261,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.90` | 3,020,000.00 USD | 3,020,000.00 USD | 33,240.00 USD | 8,150.00 USD | 1,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.90` | 5,260,000.00 USD | 5,260,000.00 USD | 108,440.00 USD | 48,600.00 USD | 266,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.00` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 12,360.00 USD | 659.87 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.00` | 5,440,000.00 USD | 5,440,000.00 USD | 88,680.00 USD | 2,620.00 USD | 93,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.10` | 3,060,000.00 USD | 3,060,000.00 USD | 7,480.00 USD | 10,960.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.10` | 5,520,000.00 USD | 5,520,000.00 USD | 36,580.00 USD | 16,110.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.20` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 14,000.00 USD | 63,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.20` | 5,560,000.00 USD | 5,560,000.00 USD | 21,160.00 USD | 15,720.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.30` | 3,160,000.00 USD | 3,160,000.00 USD | 12,360.00 USD | 12,450.00 USD | 386.57 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.30` | 5,620,000.00 USD | 5,620,000.00 USD | 22,360.00 USD | 3,150.00 USD | 34,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.40` | 3,210,000.00 USD | 3,210,000.00 USD | 19,650.00 USD | 28,690.00 USD | 754.29 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.40` | 5,840,000.00 USD | 5,840,000.00 USD | 38,520.00 USD | 30,000.00 USD | 153,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.50` | 3,450,000.00 USD | 3,450,000.00 USD | 128,210.00 USD | 19,060.00 USD | 90,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.50` | 5,950,000.00 USD | 5,950,000.00 USD | 76,670.00 USD | 30,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.60` | 3,580,000.00 USD | 3,580,000.00 USD | 58,710.00 USD | 18,250.00 USD | 57,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.60` | 6,130,000.00 USD | 6,130,000.00 USD | 123,760.00 USD | 36,020.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.70` | 3,730,000.00 USD | 3,730,000.00 USD | 28,040.00 USD | 23,180.00 USD | 96,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.70` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 5,400.00 USD | 57,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.80` | 3,820,000.00 USD | 3,820,000.00 USD | 5,680.00 USD | 12,010.00 USD | 72,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.80` | 6,260,000.00 USD | 6,260,000.00 USD | 2,260.00 USD | 14,360.00 USD | 48,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.90` | 3,850,000.00 USD | 3,850,000.00 USD | 9,550.00 USD | 14,100.00 USD | 7,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.90` | 6,270,000.00 USD | 6,270,000.00 USD | 2,410.00 USD | 963.90 USD | 1,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.95` | 978.20 USD | 978.20 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.00` | 3,860,000.00 USD | 3,860,000.00 USD | 3,570.00 USD | 5,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.00` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 3,670.00 USD | 86,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.10` | 3,910,000.00 USD | 3,910,000.00 USD | 29,450.00 USD | 6,730.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.10` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 1,310.00 USD | 848.40 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `58.15` | 199,650.00 USD | 200,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.20` | 3,910,000.00 USD | 3,910,000.00 USD | 1,980.00 USD | 5,880.00 USD | 350.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.30` | 3,970,000.00 USD | 3,970,000.00 USD | 10,290.00 USD | 11,540.00 USD | 36,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.30` | 6,400,000.00 USD | 6,400,000.00 USD | 0.00 USD | 9,580.00 USD | 26,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.40` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 4,990.00 USD | 33,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.40` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 0.00 USD | 54,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.50` | 4,080,000.00 USD | 4,080,000.00 USD | 49,290.00 USD | 21,280.00 USD | 379.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.50` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.60` | 6,480,000.00 USD | 6,480,000.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.70` | 4,110,000.00 USD | 4,110,000.00 USD | 15,850.00 USD | 8,070.00 USD | 355.85 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.70` | 6,520,000.00 USD | 6,520,000.00 USD | 1,700.00 USD | 5,910.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `58.75` | 213.26 USD | 200,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.80` | 4,180,000.00 USD | 4,180,000.00 USD | 35,140.00 USD | 14,730.00 USD | 23,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.80` | 6,530,000.00 USD | 6,530,000.00 USD | 1,810.00 USD | 3,320.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.90` | 4,420,000.00 USD | 4,420,000.00 USD | 19,290.00 USD | 124,640.00 USD | 91,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.90` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 48,700.00 USD | 83,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.00` | 4,760,000.00 USD | 4,760,000.00 USD | 151,460.00 USD | 57,130.00 USD | 134,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.00` | 7,100,000.00 USD | 7,100,000.00 USD | 255,180.00 USD | 65,270.00 USD | 118,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.05` | 213.76 USD | 201,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.10` | 5,180,000.00 USD | 5,180,000.00 USD | 191,140.00 USD | 49,070.00 USD | 186,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.10` | 7,400,000.00 USD | 7,400,000.00 USD | 91,060.00 USD | 45,400.00 USD | 158,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.20` | 5,520,000.00 USD | 5,520,000.00 USD | 159,440.00 USD | 75,750.00 USD | 96,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.20` | 7,740,000.00 USD | 7,740,000.00 USD | 153,580.00 USD | 12,460.00 USD | 174,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.30` | 6,040,000.00 USD | 6,040,000.00 USD | 306,360.00 USD | 73,700.00 USD | 143,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.30` | 8,010,000.00 USD | 8,010,000.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.35` | 9,440.00 USD | 210,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.40` | 6,250,000.00 USD | 6,250,000.00 USD | 78,860.00 USD | 57,010.00 USD | 76,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.40` | 8,330,000.00 USD | 8,330,000.00 USD | 103,370.00 USD | 73,620.00 USD | 137,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.50` | 6,460,000.00 USD | 6,460,000.00 USD | 119,350.00 USD | 57,690.00 USD | 28,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.50` | 8,480,000.00 USD | 8,480,000.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.60` | 6,610,000.00 USD | 6,610,000.00 USD | 62,780.00 USD | 68,870.00 USD | 18,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.60` | 8,980,000.00 USD | 8,980,000.00 USD | 268,680.00 USD | 145,550.00 USD | 86,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.70` | 6,750,000.00 USD | 6,750,000.00 USD | 20,820.00 USD | 30,890.00 USD | 94,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.70` | 9,380,000.00 USD | 9,380,000.00 USD | 55,510.00 USD | 180,620.00 USD | 161,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.80` | 6,840,000.00 USD | 6,840,000.00 USD | 40,970.00 USD | 37,360.00 USD | 10,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.80` | 9,750,000.00 USD | 9,750,000.00 USD | 118,240.00 USD | 97,600.00 USD | 155,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.90` | 7,060,000.00 USD | 7,060,000.00 USD | 112,870.00 USD | 21,300.00 USD | 80,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.90` | 10,120,000.00 USD | 10,120,000.00 USD | 246,770.00 USD | 84,430.00 USD | 40,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.00` | 7,370,000.00 USD | 7,370,000.00 USD | 182,880.00 USD | 64,320.00 USD | 69,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.00` | 10,630,000.00 USD | 10,630,000.00 USD | 231,370.00 USD | 183,130.00 USD | 94,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.05` | 217.98 USD | 210,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.10` | 7,580,000.00 USD | 7,580,000.00 USD | 95,780.00 USD | 40,330.00 USD | 71,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.10` | 11,200,000.00 USD | 11,200,000.00 USD | 263,890.00 USD | 129,860.00 USD | 174,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.20` | 7,840,000.00 USD | 7,840,000.00 USD | 119,070.00 USD | 37,570.00 USD | 96,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.20` | 11,700,000.00 USD | 11,700,000.00 USD | 207,990.00 USD | 131,530.00 USD | 157,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.30` | 8,090,000.00 USD | 8,090,000.00 USD | 97,720.00 USD | 71,550.00 USD | 82,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.30` | 12,080,000.00 USD | 12,080,000.00 USD | 133,350.00 USD | 95,890.00 USD | 155,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.35` | 218.47 USD | 210,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.40` | 8,360,000.00 USD | 8,360,000.00 USD | 168,700.00 USD | 45,260.00 USD | 60,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.40` | 12,530,000.00 USD | 12,530,000.00 USD | 93,890.00 USD | 133,310.00 USD | 226,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.50` | 8,530,000.00 USD | 8,530,000.00 USD | 69,310.00 USD | 42,290.00 USD | 57,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.50` | 12,960,000.00 USD | 12,960,000.00 USD | 131,870.00 USD | 86,290.00 USD | 206,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.60` | 8,640,000.00 USD | 8,640,000.00 USD | 69,460.00 USD | 33,050.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.60` | 13,400,000.00 USD | 13,400,000.00 USD | 251,100.00 USD | 52,650.00 USD | 134,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.70` | 8,720,000.00 USD | 8,720,000.00 USD | 45,500.00 USD | 33,220.00 USD | 985.52 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.70` | 13,620,000.00 USD | 13,620,000.00 USD | 129,660.00 USD | 67,510.00 USD | 28,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.80` | 8,810,000.00 USD | 8,810,000.00 USD | 22,530.00 USD | 12,680.00 USD | 55,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.80` | 13,850,000.00 USD | 13,850,000.00 USD | 54,870.00 USD | 78,710.00 USD | 94,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.90` | 8,920,000.00 USD | 8,920,000.00 USD | 57,090.00 USD | 25,670.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.90` | 14,110,000.00 USD | 14,110,000.00 USD | 116,730.00 USD | 58,270.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.00` | 9,000,000.00 USD | 9,000,000.00 USD | 46,000.00 USD | 6,970.00 USD | 28,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 14,240,000.00 USD | 14,240,000.00 USD | 96,160.00 USD | 36,500.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.10` | 9,020,000.00 USD | 9,020,000.00 USD | 10,580.00 USD | 5,550.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 14,280,000.00 USD | 14,280,000.00 USD | 31,540.00 USD | 1,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.15` | 3,870.00 USD | 214,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.20` | 9,150,000.00 USD | 9,150,000.00 USD | 75,930.00 USD | 1,160.00 USD | 47,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.20` | 14,520,000.00 USD | 14,520,000.00 USD | 116,610.00 USD | 75,410.00 USD | 52,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.30` | 9,170,000.00 USD | 9,170,000.00 USD | 9,540.00 USD | 9,090.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.30` | 14,660,000.00 USD | 14,660,000.00 USD | 51,130.00 USD | 35,650.00 USD | 55,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.40` | 9,180,000.00 USD | 9,180,000.00 USD | 6,350.00 USD | 5,640.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.40` | 14,850,000.00 USD | 14,850,000.00 USD | 89,350.00 USD | 41,800.00 USD | 59,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.50` | 9,230,000.00 USD | 9,230,000.00 USD | 9,120.00 USD | 18,030.00 USD | 17,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.50` | 14,950,000.00 USD | 14,950,000.00 USD | 19,810.00 USD | 35,300.00 USD | 36,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.60` | 9,270,000.00 USD | 9,270,000.00 USD | 24,180.00 USD | 10,500.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.60` | 15,200,000.00 USD | 15,200,000.00 USD | 54,240.00 USD | 63,390.00 USD | 132,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.70` | 9,320,000.00 USD | 9,320,000.00 USD | 31,820.00 USD | 9,150.00 USD | 9,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.70` | 15,410,000.00 USD | 15,410,000.00 USD | 84,300.00 USD | 11,330.00 USD | 114,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.80` | 9,350,000.00 USD | 9,350,000.00 USD | 18,210.00 USD | 4,670.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.80` | 15,670,000.00 USD | 15,670,000.00 USD | 160,110.00 USD | 38,970.00 USD | 69,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.90` | 15,810,000.00 USD | 15,810,000.00 USD | 72,380.00 USD | 29,730.00 USD | 35,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.00` | 15,930,000.00 USD | 15,930,000.00 USD | 56,450.00 USD | 13,260.00 USD | 49,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.10` | 15,970,000.00 USD | 15,970,000.00 USD | 14,790.00 USD | 12,820.00 USD | 7,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.20` | 16,080,000.00 USD | 16,080,000.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.30` | 16,230,000.00 USD | 16,230,000.00 USD | 31,770.00 USD | 23,450.00 USD | 97,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.40` | 16,370,000.00 USD | 16,370,000.00 USD | 79,620.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.50` | 16,460,000.00 USD | 16,460,000.00 USD | 44,300.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.60` | 16,530,000.00 USD | 16,530,000.00 USD | 34,910.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `62.65` | 142.84 USD | 214,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `62.70` | 16,610,000.00 USD | 16,610,000.00 USD | 22,020.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.80` | 16,760,000.00 USD | 16,760,000.00 USD | 72,250.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.90` | 16,850,000.00 USD | 16,850,000.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.00` | 16,910,000.00 USD | 16,910,000.00 USD | 34,730.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.10` | 16,950,000.00 USD | 16,950,000.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `63.25` | 1,330.00 USD | 216,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `63.30` | 16,990,000.00 USD | 16,990,000.00 USD | 17,050.00 USD | 11,500.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.40` | 17,010,000.00 USD | 17,010,000.00 USD | 13,220.00 USD | 1,320.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.50` | 17,040,000.00 USD | 17,040,000.00 USD | 6,620.00 USD | 15,810.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.60` | 17,140,000.00 USD | 17,140,000.00 USD | 63,480.00 USD | 20,800.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.70` | 17,210,000.00 USD | 17,210,000.00 USD | 21,940.00 USD | 18,810.00 USD | 35,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.80` | 17,280,000.00 USD | 17,280,000.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.90` | 17,310,000.00 USD | 17,310,000.00 USD | 7,650.00 USD | 12,840.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.00` | 17,350,000.00 USD | 17,350,000.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.10` | 17,380,000.00 USD | 17,380,000.00 USD | 20,350.00 USD | 667.05 USD | 10,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.20` | 17,420,000.00 USD | 17,420,000.00 USD | 28,840.00 USD | 14,530.00 USD | 584.77 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.40` | 17,480,000.00 USD | 17,480,000.00 USD | 2,540.00 USD | 20,590.00 USD | 29,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.50` | 17,510,000.00 USD | 17,510,000.00 USD | 7,700.00 USD | 7,120.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.60` | 17,550,000.00 USD | 17,550,000.00 USD | 32,220.00 USD | 14,180.00 USD | 108.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.70` | 17,620,000.00 USD | 17,620,000.00 USD | 39,430.00 USD | 23,030.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.80` | 17,650,000.00 USD | 17,650,000.00 USD | 7,540.00 USD | 8,210.00 USD | 20,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.90` | 17,700,000.00 USD | 17,700,000.00 USD | 25,320.00 USD | 8,010.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.00` | 17,720,000.00 USD | 17,720,000.00 USD | 1,790.00 USD | 9,480.00 USD | 13,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.10` | 17,780,000.00 USD | 17,780,000.00 USD | 5,810.00 USD | 14,250.00 USD | 37,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.20` | 17,820,000.00 USD | 17,820,000.00 USD | 9,780.00 USD | 1,630.00 USD | 28,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `65.25` | 186.61 USD | 216,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `65.30` | 17,860,000.00 USD | 17,860,000.00 USD | 22,330.00 USD | 5,510.00 USD | 17,890.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `11.35` | 2,840,000.00 USD | 0.00 USD | 136.20 USD | `-79.52%` | `12.00` |
| `Live` | `Long` | `11.65` | 2,840,000.00 USD | 0.00 USD | 195.02 USD | `-78.98%` | `16.74` |
| `Live` | `Long` | `12.25` | 2,840,000.00 USD | 0.00 USD | 122.50 USD | `-77.90%` | `10.00` |
| `Live` | `Long` | `12.35` | 2,840,000.00 USD | 0.00 USD | 395.20 USD | `-77.72%` | `32.00` |
| `Live` | `Long` | `12.75` | 2,840,000.00 USD | 0.00 USD | 2,560.00 USD | `-76.99%` | `200.43` |
| `Live` | `Long` | `13.15` | 2,840,000.00 USD | 0.00 USD | 2,220.00 USD | `-76.27%` | `168.79` |
| `Live` | `Long` | `13.65` | 2,840,000.00 USD | 0.00 USD | 150.15 USD | `-75.37%` | `11.00` |
| `Live` | `Long` | `14.35` | 2,840,000.00 USD | 0.00 USD | 129.44 USD | `-74.11%` | `9.02` |
| `Live` | `Long` | `16.05` | 2,840,000.00 USD | 0.00 USD | 169.17 USD | `-71.04%` | `10.54` |
| `Live` | `Long` | `16.35` | 2,840,000.00 USD | 0.00 USD | 327.00 USD | `-70.50%` | `20.00` |
| `Live` | `Long` | `17.45` | 2,840,000.00 USD | 0.00 USD | 2,090.00 USD | `-68.51%` | `120.00` |
| `Live` | `Long` | `18.85` | 2,840,000.00 USD | 0.00 USD | 2,840.00 USD | `-65.99%` | `150.57` |
| `Live` | `Long` | `19.05` | 2,830,000.00 USD | 0.00 USD | 3,470.00 USD | `-65.63%` | `182.00` |
| `Live` | `Long` | `19.45` | 2,830,000.00 USD | 0.00 USD | 2,170.00 USD | `-64.90%` | `111.52` |
| `Live` | `Long` | `21.05` | 2,830,000.00 USD | 0.00 USD | 6,360.00 USD | `-62.02%` | `302.15` |
| `Live` | `Long` | `22.75` | 2,820,000.00 USD | 0.00 USD | 366.96 USD | `-58.95%` | `16.13` |
| `Live` | `Long` | `22.85` | 2,820,000.00 USD | 0.00 USD | 4,460.00 USD | `-58.77%` | `195.03` |
| `Live` | `Long` | `23.45` | 2,820,000.00 USD | 0.00 USD | 1,410.00 USD | `-57.69%` | `60.00` |
| `Live` | `Long` | `23.65` | 2,820,000.00 USD | 0.00 USD | 156.09 USD | `-57.33%` | `6.60` |
| `Live` | `Long` | `23.85` | 2,810,000.00 USD | 0.00 USD | 195.57 USD | `-56.96%` | `8.20` |
| `Live` | `Long` | `24.25` | 2,810,000.00 USD | 0.00 USD | 943.81 USD | `-56.24%` | `38.92` |
| `Live` | `Long` | `24.65` | 2,810,000.00 USD | 0.00 USD | 1,040.00 USD | `-55.52%` | `42.19` |
| `Live` | `Long` | `24.75` | 2,810,000.00 USD | 0.00 USD | 23,020.00 USD | `-55.34%` | `930.00` |
| `Live` | `Long` | `25.25` | 2,790,000.00 USD | 0.00 USD | 277,980.00 USD | `-54.44%` | `11,009.19` |
| `Live` | `Long` | `25.35` | 2,510,000.00 USD | 0.00 USD | 173.39 USD | `-54.26%` | `6.84` |
| `Live` | `Long` | `25.55` | 2,510,000.00 USD | 0.00 USD | 50,890.00 USD | `-53.90%` | `1,991.90` |
| `Live` | `Long` | `25.95` | 2,460,000.00 USD | 0.00 USD | 6,210.00 USD | `-53.18%` | `239.42` |
| `Live` | `Long` | `26.95` | 2,450,000.00 USD | 0.00 USD | 5,490.00 USD | `-51.37%` | `203.85` |
| `Live` | `Long` | `27.55` | 2,450,000.00 USD | 0.00 USD | 272.75 USD | `-50.29%` | `9.90` |
| `Live` | `Long` | `27.85` | 2,450,000.00 USD | 0.00 USD | 233.94 USD | `-49.75%` | `8.40` |
| `Live` | `Long` | `27.95` | 2,450,000.00 USD | 0.00 USD | 173.85 USD | `-49.57%` | `6.22` |
| `Live` | `Long` | `28.85` | 2,450,000.00 USD | 0.00 USD | 458.14 USD | `-47.94%` | `15.88` |
| `Live` | `Long` | `28.95` | 2,450,000.00 USD | 0.00 USD | 36,370.00 USD | `-47.76%` | `1,256.40` |
| `Live` | `Long` | `29.15` | 2,410,000.00 USD | 0.00 USD | 583.00 USD | `-47.40%` | `20.00` |
| `Live` | `Long` | `29.75` | 2,410,000.00 USD | 0.00 USD | 297,600.00 USD | `-46.32%` | `10,003.44` |
| `Live` | `Long` | `30.05` | 2,110,000.00 USD | 0.00 USD | 693.85 USD | `-45.78%` | `23.09` |
| `Live` | `Long` | `30.95` | 2,110,000.00 USD | 0.00 USD | 538.53 USD | `-44.15%` | `17.40` |
| `Live` | `Long` | `31.15` | 2,110,000.00 USD | 0.00 USD | 5,880.00 USD | `-43.79%` | `188.85` |
| `Live` | `Long` | `31.25` | 2,110,000.00 USD | 0.00 USD | 3,880.00 USD | `-43.61%` | `124.01` |
| `Live` | `Long` | `31.55` | 2,100,000.00 USD | 0.00 USD | 5,680.00 USD | `-43.07%` | `180.02` |
| `Live` | `Long` | `31.75` | 2,100,000.00 USD | 0.00 USD | 22,160.00 USD | `-42.71%` | `697.95` |
| `Live` | `Long` | `31.85` | 2,070,000.00 USD | 0.00 USD | 2,870.00 USD | `-42.53%` | `90.00` |
| `Live` | `Long` | `31.95` | 2,070,000.00 USD | 0.00 USD | 125.24 USD | `-42.35%` | `3.92` |
| `Live` | `Long` | `32.15` | 2,070,000.00 USD | 0.00 USD | 1,360.00 USD | `-41.99%` | `42.27` |
| `Live` | `Long` | `32.35` | 2,070,000.00 USD | 0.00 USD | 1,070.00 USD | `-41.63%` | `33.03` |
| `Live` | `Long` | `32.65` | 2,070,000.00 USD | 0.00 USD | 2,290.00 USD | `-41.09%` | `70.00` |
| `Live` | `Long` | `32.75` | 2,070,000.00 USD | 0.00 USD | 953.68 USD | `-40.91%` | `29.12` |
| `Live` | `Long` | `32.85` | 2,070,000.00 USD | 0.00 USD | 32,850.00 USD | `-40.73%` | `1,000.01` |
| `Live` | `Long` | `33.45` | 2,030,000.00 USD | 0.00 USD | 627.19 USD | `-39.64%` | `18.75` |
| `Live` | `Long` | `33.65` | 2,030,000.00 USD | 0.00 USD | 257.76 USD | `-39.28%` | `7.66` |
| `Live` | `Long` | `33.75` | 2,030,000.00 USD | 0.00 USD | 4,410.00 USD | `-39.10%` | `130.63` |
| `Live` | `Long` | `33.95` | 2,030,000.00 USD | 0.00 USD | 237.65 USD | `-38.74%` | `7.00` |
| `Live` | `Long` | `34.05` | 2,030,000.00 USD | 0.00 USD | 182.85 USD | `-38.56%` | `5.37` |
| `Live` | `Long` | `34.15` | 2,030,000.00 USD | 0.00 USD | 126.70 USD | `-38.38%` | `3.71` |
| `Live` | `Long` | `34.65` | 2,030,000.00 USD | 0.00 USD | 3,240.00 USD | `-37.48%` | `93.56` |
| `Live` | `Long` | `34.95` | 2,020,000.00 USD | 0.00 USD | 104.85 USD | `-36.94%` | `3.00` |
| `Live` | `Long` | `35.05` | 2,020,000.00 USD | 0.00 USD | 166.49 USD | `-36.76%` | `4.75` |
| `Live` | `Long` | `35.15` | 2,020,000.00 USD | 0.00 USD | 175.75 USD | `-36.58%` | `5.00` |
| `Live` | `Long` | `36.05` | 2,020,000.00 USD | 0.00 USD | 10,810.00 USD | `-34.95%` | `300.00` |
| `Live` | `Long` | `36.35` | 2,010,000.00 USD | 0.00 USD | 3,020.00 USD | `-34.41%` | `83.03` |
| `Live` | `Long` | `36.45` | 2,010,000.00 USD | 0.00 USD | 423.18 USD | `-34.23%` | `11.61` |
| `Live` | `Long` | `36.75` | 2,010,000.00 USD | 0.00 USD | 389.55 USD | `-33.69%` | `10.60` |
| `Live` | `Long` | `37.05` | 2,010,000.00 USD | 0.00 USD | 359.76 USD | `-33.15%` | `9.71` |
| `Live` | `Long` | `37.15` | 2,010,000.00 USD | 0.00 USD | 438.74 USD | `-32.97%` | `11.81` |
| `Live` | `Long` | `37.35` | 2,010,000.00 USD | 0.00 USD | 10,320.00 USD | `-32.61%` | `276.18` |
| `Live` | `Long` | `37.55` | 2,000,000.00 USD | 0.00 USD | 3,980.00 USD | `-32.24%` | `105.96` |
| `Live` | `Long` | `37.85` | 1,990,000.00 USD | 0.00 USD | 6,210.00 USD | `-31.70%` | `164.03` |
| `Live` | `Long` | `37.95` | 1,990,000.00 USD | 0.00 USD | 446.67 USD | `-31.52%` | `11.77` |
| `Live` | `Long` | `38.25` | 1,990,000.00 USD | 0.00 USD | 5,050.00 USD | `-30.98%` | `131.94` |
| `Live` | `Long` | `38.35` | 1,980,000.00 USD | 0.00 USD | 341.70 USD | `-30.80%` | `8.91` |
| `Live` | `Long` | `38.45` | 1,980,000.00 USD | 0.00 USD | 2,400.00 USD | `-30.62%` | `62.34` |
| `Live` | `Long` | `38.55` | 1,980,000.00 USD | 0.00 USD | 4,880.00 USD | `-30.44%` | `126.57` |
| `Live` | `Long` | `38.65` | 1,970,000.00 USD | 0.00 USD | 384.57 USD | `-30.26%` | `9.95` |
| `Live` | `Long` | `38.95` | 1,970,000.00 USD | 0.00 USD | 2,730.00 USD | `-29.72%` | `70.00` |
| `Live` | `Long` | `39.05` | 1,970,000.00 USD | 0.00 USD | 664,760.00 USD | `-29.54%` | `17,023.28` |
| `Live` | `Long` | `39.15` | 1,310,000.00 USD | 0.00 USD | 940.77 USD | `-29.36%` | `24.03` |
| `Live` | `Long` | `39.35` | 1,310,000.00 USD | 0.00 USD | 264.83 USD | `-29.00%` | `6.73` |
| `Live` | `Long` | `39.45` | 1,310,000.00 USD | 0.00 USD | 865.53 USD | `-28.82%` | `21.94` |
| `Live` | `Long` | `39.55` | 1,300,000.00 USD | 0.00 USD | 162.95 USD | `-28.64%` | `4.12` |
| `Live` | `Long` | `39.65` | 1,300,000.00 USD | 0.00 USD | 5,900.00 USD | `-28.46%` | `148.78` |
| `Live` | `Long` | `39.75` | 1,300,000.00 USD | 0.00 USD | 2,580.00 USD | `-28.27%` | `64.90` |
| `Live` | `Long` | `39.85` | 1,300,000.00 USD | 0.00 USD | 8,900.00 USD | `-28.09%` | `223.34` |
| `Live` | `Long` | `39.95` | 1,290,000.00 USD | 0.00 USD | 337.58 USD | `-27.91%` | `8.45` |
| `Live` | `Long` | `40.05` | 1,290,000.00 USD | 0.00 USD | 2,160.00 USD | `-27.73%` | `53.97` |
| `Live` | `Long` | `40.45` | 1,280,000.00 USD | 0.00 USD | 1,010.00 USD | `-27.01%` | `24.92` |
| `Live` | `Long` | `40.55` | 1,280,000.00 USD | 0.00 USD | 133.00 USD | `-26.83%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,280,000.00 USD | 0.00 USD | 1,650.00 USD | `-26.65%` | `40.69` |
| `Live` | `Long` | `40.85` | 1,280,000.00 USD | 0.00 USD | 6,340.00 USD | `-26.29%` | `155.23` |
| `Live` | `Long` | `40.95` | 1,280,000.00 USD | 0.00 USD | 509.01 USD | `-26.11%` | `12.43` |
| `Live` | `Long` | `41.05` | 1,270,000.00 USD | 0.00 USD | 396.54 USD | `-25.93%` | `9.66` |
| `Live` | `Long` | `41.25` | 1,270,000.00 USD | 0.00 USD | 14,490.00 USD | `-25.57%` | `351.26` |
| `Live` | `Long` | `41.45` | 1,260,000.00 USD | 0.00 USD | 644.96 USD | `-25.21%` | `15.56` |
| `Live` | `Long` | `41.55` | 1,260,000.00 USD | 0.00 USD | 41,550.00 USD | `-25.03%` | `1,000.00` |
| `Live` | `Long` | `41.65` | 1,220,000.00 USD | 0.00 USD | 5,360.00 USD | `-24.85%` | `128.71` |
| `Live` | `Long` | `41.95` | 1,210,000.00 USD | 0.00 USD | 1,050.00 USD | `-24.31%` | `24.93` |
| `Live` | `Long` | `42.05` | 1,210,000.00 USD | 0.00 USD | 6,200.00 USD | `-24.12%` | `147.50` |
| `Live` | `Long` | `42.15` | 1,210,000.00 USD | 0.00 USD | 66,300.00 USD | `-23.94%` | `1,572.94` |
| `Live` | `Long` | `42.25` | 1,140,000.00 USD | 0.00 USD | 35,410.00 USD | `-23.76%` | `838.00` |
| `Live` | `Long` | `42.65` | 1,100,000.00 USD | 0.00 USD | 1,570.00 USD | `-23.04%` | `36.70` |
| `Live` | `Long` | `42.85` | 1,100,000.00 USD | 0.00 USD | 5,800.00 USD | `-22.68%` | `135.38` |
| `Live` | `Long` | `42.95` | 1,100,000.00 USD | 0.00 USD | 2,000.00 USD | `-22.50%` | `46.65` |
| `Live` | `Long` | `43.05` | 1,090,000.00 USD | 0.00 USD | 8,950.00 USD | `-22.32%` | `208.00` |
| `Live` | `Long` | `43.15` | 1,090,000.00 USD | 0.00 USD | 126,620.00 USD | `-22.14%` | `2,934.32` |
| `Live` | `Long` | `43.25` | 958,410.00 USD | 0.00 USD | 7,850.00 USD | `-21.96%` | `181.44` |
| `Live` | `Long` | `43.35` | 950,560.00 USD | 0.00 USD | 5,390.00 USD | `-21.78%` | `124.24` |
| `Live` | `Long` | `43.45` | 945,180.00 USD | 0.00 USD | 706.06 USD | `-21.60%` | `16.25` |
| `Live` | `Long` | `43.65` | 944,470.00 USD | 0.00 USD | 26,650.00 USD | `-21.24%` | `610.44` |
| `Live` | `Long` | `43.75` | 917,830.00 USD | 0.00 USD | 21,880.00 USD | `-21.06%` | `500.00` |
| `Live` | `Long` | `43.85` | 895,950.00 USD | 0.00 USD | 801.14 USD | `-20.88%` | `18.27` |
| `Live` | `Long` | `44.15` | 895,150.00 USD | 0.00 USD | 3,180.00 USD | `-20.34%` | `71.99` |
| `Live` | `Long` | `44.35` | 891,970.00 USD | 0.00 USD | 85,770.00 USD | `-19.97%` | `1,933.87` |
| `Live` | `Long` | `44.45` | 806,200.00 USD | 0.00 USD | 3,800.00 USD | `-19.79%` | `85.43` |
| `Live` | `Long` | `44.55` | 802,410.00 USD | 0.00 USD | 842.44 USD | `-19.61%` | `18.91` |
| `Live` | `Long` | `44.75` | 801,560.00 USD | 0.00 USD | 4,230.00 USD | `-19.25%` | `94.55` |
| `Live` | `Long` | `44.85` | 797,330.00 USD | 0.00 USD | 134.55 USD | `-19.07%` | `3.00` |
| `Live` | `Long` | `44.95` | 797,200.00 USD | 0.00 USD | 2,620.00 USD | `-18.89%` | `58.18` |
| `Live` | `Long` | `45.05` | 794,580.00 USD | 0.00 USD | 329.32 USD | `-18.71%` | `7.31` |
| `Live` | `Long` | `45.15` | 794,250.00 USD | 0.00 USD | 1,060.00 USD | `-18.53%` | `23.38` |
| `Live` | `Long` | `45.25` | 793,200.00 USD | 0.00 USD | 3,180.00 USD | `-18.35%` | `70.37` |
| `Live` | `Long` | `45.35` | 790,010.00 USD | 0.00 USD | 2,180.00 USD | `-18.17%` | `48.02` |
| `Live` | `Long` | `45.45` | 787,840.00 USD | 0.00 USD | 24,110.00 USD | `-17.99%` | `530.49` |
| `Live` | `Long` | `45.55` | 763,730.00 USD | 0.00 USD | 11,950.00 USD | `-17.81%` | `262.40` |
| `Live` | `Long` | `45.65` | 751,770.00 USD | 0.00 USD | 342.38 USD | `-17.63%` | `7.50` |
| `Live` | `Long` | `46.05` | 751,430.00 USD | 0.00 USD | 971.65 USD | `-16.91%` | `21.10` |
| `Live` | `Long` | `46.35` | 750,460.00 USD | 0.00 USD | 383.78 USD | `-16.37%` | `8.28` |
| `Live` | `Long` | `46.65` | 750,080.00 USD | 0.00 USD | 2,530.00 USD | `-15.82%` | `54.16` |
| `Live` | `Long` | `46.85` | 747,550.00 USD | 0.00 USD | 2,000.00 USD | `-15.46%` | `42.65` |
| `Live` | `Long` | `46.95` | 745,550.00 USD | 0.00 USD | 158.22 USD | `-15.28%` | `3.37` |
| `Live` | `Long` | `47.15` | 745,390.00 USD | 0.00 USD | 9,740.00 USD | `-14.92%` | `206.65` |
| `Live` | `Long` | `47.25` | 735,650.00 USD | 0.00 USD | 574.09 USD | `-14.74%` | `12.15` |
| `Live` | `Long` | `47.35` | 735,070.00 USD | 0.00 USD | 43,340.00 USD | `-14.56%` | `915.41` |
| `Live` | `Long` | `47.45` | 691,730.00 USD | 0.00 USD | 4,820.00 USD | `-14.38%` | `101.62` |
| `Live` | `Long` | `47.55` | 686,910.00 USD | 0.00 USD | 1,770.00 USD | `-14.20%` | `37.28` |
| `Live` | `Long` | `47.75` | 685,140.00 USD | 0.00 USD | 4,780.00 USD | `-13.84%` | `100.00` |
| `Live` | `Long` | `48.05` | 680,360.00 USD | 0.00 USD | 1,340.00 USD | `-13.30%` | `27.93` |
| `Live` | `Long` | `48.15` | 679,020.00 USD | 0.00 USD | 1,690.00 USD | `-13.12%` | `35.03` |
| `Live` | `Long` | `48.25` | 677,330.00 USD | 0.00 USD | 525.44 USD | `-12.94%` | `10.89` |
| `Live` | `Long` | `48.55` | 676,810.00 USD | 0.00 USD | 2,030.00 USD | `-12.40%` | `41.85` |
| `Live` | `Long` | `48.65` | 674,770.00 USD | 0.00 USD | 273.90 USD | `-12.22%` | `5.63` |
| `Live` | `Long` | `48.75` | 674,500.00 USD | 0.00 USD | 333.94 USD | `-12.04%` | `6.85` |
| `Live` | `Long` | `48.95` | 674,170.00 USD | 0.00 USD | 797.40 USD | `-11.67%` | `16.29` |
| `Live` | `Long` | `49.05` | 673,370.00 USD | 0.00 USD | 1,580.00 USD | `-11.49%` | `32.25` |
| `Live` | `Long` | `49.15` | 671,790.00 USD | 0.00 USD | 5,740.00 USD | `-11.31%` | `116.83` |
| `Live` | `Long` | `49.25` | 666,050.00 USD | 0.00 USD | 263.49 USD | `-11.13%` | `5.35` |
| `Live` | `Long` | `49.35` | 665,780.00 USD | 0.00 USD | 24,210.00 USD | `-10.95%` | `490.66` |
| `Live` | `Long` | `49.45` | 641,570.00 USD | 0.00 USD | 1,960.00 USD | `-10.77%` | `39.73` |
| `Live` | `Long` | `49.55` | 639,600.00 USD | 0.00 USD | 18,010.00 USD | `-10.59%` | `363.57` |
| `Live` | `Long` | `49.65` | 621,590.00 USD | 0.00 USD | 73,260.00 USD | `-10.41%` | `1,475.52` |
| `Live` | `Long` | `49.75` | 548,330.00 USD | 0.00 USD | 1,580.00 USD | `-10.23%` | `31.67` |
| `Live` | `Long` | `49.85` | 546,750.00 USD | 0.00 USD | 1,930.00 USD | `-10.05%` | `38.79` |
| `Live` | `Long` | `49.95` | 544,820.00 USD | 0.00 USD | 28,540.00 USD | `-9.87%` | `571.31` |
| `Live` | `Long` | `50.05` | 516,280.00 USD | 0.00 USD | 1,820.00 USD | `-9.69%` | `36.43` |
| `Live` | `Long` | `50.25` | 514,460.00 USD | 0.00 USD | 102.51 USD | `-9.33%` | `2.04` |
| `Live` | `Long` | `50.35` | 514,360.00 USD | 0.00 USD | 1,030.00 USD | `-9.15%` | `20.49` |
| `Live` | `Long` | `50.45` | 513,330.00 USD | 0.00 USD | 4,720.00 USD | `-8.97%` | `93.64` |
| `Live` | `Long` | `50.55` | 508,600.00 USD | 0.00 USD | 84,100.00 USD | `-8.79%` | `1,663.61` |
| `Live` | `Long` | `50.75` | 424,510.00 USD | 0.00 USD | 9,050.00 USD | `-8.43%` | `178.28` |
| `Live` | `Long` | `50.95` | 415,460.00 USD | 0.00 USD | 245.07 USD | `-8.07%` | `4.81` |
| `Live` | `Long` | `51.15` | 415,210.00 USD | 0.00 USD | 219,370.00 USD | `-7.70%` | `4,288.79` |
| `Live` | `Long` | `51.45` | 195,840.00 USD | 0.00 USD | 20,410.00 USD | `-7.16%` | `396.78` |
| `Live` | `Long` | `51.55` | 175,430.00 USD | 0.00 USD | 551.07 USD | `-6.98%` | `10.69` |
| `Live` | `Long` | `51.65` | 174,880.00 USD | 0.00 USD | 8,810.00 USD | `-6.80%` | `170.51` |
| `Live` | `Long` | `51.75` | 166,070.00 USD | 0.00 USD | 9,580.00 USD | `-6.62%` | `185.17` |
| `Live` | `Long` | `51.85` | 156,490.00 USD | 0.00 USD | 13,890.00 USD | `-6.44%` | `267.97` |
| `Live` | `Long` | `51.95` | 142,590.00 USD | 0.00 USD | 13,950.00 USD | `-6.26%` | `268.48` |
| `Live` | `Long` | `52.15` | 128,640.00 USD | 0.00 USD | 13,180.00 USD | `-5.90%` | `252.78` |
| `Live` | `Long` | `52.25` | 115,460.00 USD | 0.00 USD | 227.81 USD | `-5.72%` | `4.36` |
| `Live` | `Long` | `52.35` | 115,230.00 USD | 0.00 USD | 3,020.00 USD | `-5.54%` | `57.70` |
| `Live` | `Long` | `52.45` | 112,210.00 USD | 0.00 USD | 2,360.00 USD | `-5.36%` | `44.95` |
| `Live` | `Long` | `52.55` | 109,860.00 USD | 0.00 USD | 8,700.00 USD | `-5.18%` | `165.49` |
| `Live` | `Long` | `52.75` | 101,160.00 USD | 0.00 USD | 6,670.00 USD | `-4.82%` | `126.37` |
| `Live` | `Long` | `52.85` | 94,490.00 USD | 0.00 USD | 7,290.00 USD | `-4.64%` | `137.97` |
| `Live` | `Long` | `52.95` | 87,200.00 USD | 0.00 USD | 42,490.00 USD | `-4.46%` | `802.50` |
| `Live` | `Long` | `53.05` | 44,710.00 USD | 0.00 USD | 900.26 USD | `-4.28%` | `16.97` |
| `Live` | `Long` | `53.15` | 43,810.00 USD | 0.00 USD | 2,640.00 USD | `-4.10%` | `49.69` |
| `Live` | `Long` | `53.25` | 41,170.00 USD | 0.00 USD | 911.64 USD | `-3.92%` | `17.12` |
| `Live` | `Long` | `53.35` | 40,260.00 USD | 0.00 USD | 2,120.00 USD | `-3.74%` | `39.78` |
| `Live` | `Long` | `53.45` | 38,130.00 USD | 0.00 USD | 4,880.00 USD | `-3.55%` | `91.21` |
| `Live` | `Long` | `53.65` | 33,260.00 USD | 0.00 USD | 350.87 USD | `-3.19%` | `6.54` |
| `Live` | `Long` | `53.75` | 32,910.00 USD | 0.00 USD | 148.35 USD | `-3.01%` | `2.76` |
| `Live` | `Long` | `53.85` | 32,760.00 USD | 0.00 USD | 2,130.00 USD | `-2.83%` | `39.58` |
| `Live` | `Long` | `53.95` | 30,630.00 USD | 0.00 USD | 27,330.00 USD | `-2.65%` | `506.53` |
| `Live` | `Long` | `54.05` | 3,300.00 USD | 0.00 USD | 219.44 USD | `-2.47%` | `4.06` |
| `Live` | `Long` | `54.15` | 3,080.00 USD | 0.00 USD | 3,080.00 USD | `-2.29%` | `56.91` |
| `Live` | `Short` | `57.75` | 1,250.00 USD | 1,250.00 USD | 0.00 USD | `+4.20%` | `21.61` |
| `Live` | `Short` | `57.95` | 2,230.00 USD | 978.20 USD | 0.00 USD | `+4.57%` | `16.88` |
| `Live` | `Short` | `58.15` | 201,440.00 USD | 199,220.00 USD | 0.00 USD | `+4.93%` | `3,425.89` |
| `Live` | `Short` | `58.25` | 202,110.00 USD | 668.13 USD | 0.00 USD | `+5.11%` | `11.47` |
| `Live` | `Short` | `58.75` | 202,320.00 USD | 213.26 USD | 0.00 USD | `+6.01%` | `3.63` |
| `Live` | `Short` | `59.35` | 212,190.00 USD | 9,870.00 USD | 0.00 USD | `+7.09%` | `166.31` |
| `Live` | `Short` | `59.45` | 212,410.00 USD | 214.61 USD | 0.00 USD | `+7.27%` | `3.61` |
| `Live` | `Short` | `60.05` | 212,630.00 USD | 217.98 USD | 0.00 USD | `+8.35%` | `3.63` |
| `Live` | `Short` | `60.65` | 212,850.00 USD | 218.95 USD | 0.00 USD | `+9.44%` | `3.61` |
| `Live` | `Short` | `60.95` | 213,240.00 USD | 397.39 USD | 0.00 USD | `+9.98%` | `6.52` |
| `Live` | `Short` | `61.15` | 217,110.00 USD | 3,870.00 USD | 0.00 USD | `+10.34%` | `63.26` |
| `Live` | `Short` | `62.65` | 217,250.00 USD | 142.84 USD | 0.00 USD | `+13.05%` | `2.28` |
| `Live` | `Short` | `62.95` | 217,390.00 USD | 138.49 USD | 0.00 USD | `+13.59%` | `2.20` |
| `Live` | `Short` | `63.45` | 220,740.00 USD | 3,350.00 USD | 0.00 USD | `+14.49%` | `52.83` |
| `Live` | `Short` | `65.25` | 220,930.00 USD | 186.61 USD | 0.00 USD | `+17.74%` | `2.86` |
| `Live` | `Short` | `65.35` | 221,080.00 USD | 150.96 USD | 0.00 USD | `+17.92%` | `2.31` |
| `Live` | `Short` | `66.85` | 255,030.00 USD | 33,950.00 USD | 0.00 USD | `+20.62%` | `507.83` |
| `Live` | `Short` | `66.95` | 255,150.00 USD | 121.18 USD | 0.00 USD | `+20.80%` | `1.81` |
| `Live` | `Short` | `67.85` | 255,860.00 USD | 709.03 USD | 0.00 USD | `+22.43%` | `10.45` |
| `Live` | `Short` | `70.45` | 260,390.00 USD | 4,530.00 USD | 0.00 USD | `+27.12%` | `64.29` |
| `Live` | `Short` | `75.45` | 260,650.00 USD | 260.30 USD | 0.00 USD | `+36.14%` | `3.45` |
| `Live` | `Short` | `76.35` | 269,030.00 USD | 8,380.00 USD | 0.00 USD | `+37.77%` | `109.80` |
| `Live` | `Short` | `77.85` | 269,640.00 USD | 602.56 USD | 0.00 USD | `+40.47%` | `7.74` |
| `Live` | `Short` | `77.95` | 269,770.00 USD | 136.41 USD | 0.00 USD | `+40.65%` | `1.75` |
| `Live` | `Short` | `78.85` | 290,810.00 USD | 21,040.00 USD | 0.00 USD | `+42.28%` | `266.81` |
| `Live` | `Short` | `79.75` | 291,540.00 USD | 728.12 USD | 0.00 USD | `+43.90%` | `9.13` |
| `Live` | `Short` | `80.75` | 295,410.00 USD | 3,880.00 USD | 0.00 USD | `+45.71%` | `48.00` |
| `Live` | `Short` | `81.05` | 314,410.00 USD | 19,000.00 USD | 0.00 USD | `+46.25%` | `234.42` |
| `Live` | `Short` | `81.55` | 314,540.00 USD | 123.96 USD | 0.00 USD | `+47.15%` | `1.52` |
| `Live` | `Short` | `82.65` | 318,390.00 USD | 3,850.00 USD | 0.00 USD | `+49.13%` | `46.61` |
| `Live` | `Short` | `82.75` | 321,340.00 USD | 2,950.00 USD | 0.00 USD | `+49.31%` | `35.59` |
| `Live` | `Short` | `84.65` | 322,200.00 USD | 862.58 USD | 0.00 USD | `+52.74%` | `10.19` |
| `Live` | `Short` | `86.25` | 323,110.00 USD | 916.84 USD | 0.00 USD | `+55.63%` | `10.63` |
| `Live` | `Short` | `93.85` | 323,240.00 USD | 123.88 USD | 0.00 USD | `+69.34%` | `1.32` |
| `Live` | `Short` | `100.45` | 325,750.00 USD | 2,510.00 USD | 0.00 USD | `+81.25%` | `25.00` |
| `Live` | `Short` | `104.25` | 326,460.00 USD | 712.03 USD | 0.00 USD | `+88.11%` | `6.83` |
| `Live` | `Short` | `105.85` | 683,600.00 USD | 357,140.00 USD | 0.00 USD | `+91.00%` | `3,374.01` |
| `Live` | `Short` | `108.45` | 716,140.00 USD | 32,530.00 USD | 0.00 USD | `+95.69%` | `300.00` |
| `Live` | `Short` | `110.45` | 716,270.00 USD | 131.44 USD | 0.00 USD | `+99.30%` | `1.19` |
| `Live` | `Short` | `110.55` | 717,390.00 USD | 1,120.00 USD | 0.00 USD | `+99.48%` | `10.11` |
| `Live` | `Short` | `110.65` | 718,360.00 USD | 973.72 USD | 0.00 USD | `+99.66%` | `8.80` |
| `Live` | `Short` | `110.75` | 722,220.00 USD | 3,860.00 USD | 0.00 USD | `+99.84%` | `34.86` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 379,220.00 USD | 0.00 USD | 392.18 USD | `-63.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 378,830.00 USD | 0.00 USD | 2,310.00 USD | `-60.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 376,520.00 USD | 0.00 USD | 806.86 USD | `-54.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 375,710.00 USD | 0.00 USD | 1,560.00 USD | `-54.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 374,150.00 USD | 0.00 USD | 410.25 USD | `-50.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 373,740.00 USD | 0.00 USD | 281.57 USD | `-45.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 373,460.00 USD | 0.00 USD | 36,050.00 USD | `-34.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 337,410.00 USD | 0.00 USD | 37,550.00 USD | `-32.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 299,860.00 USD | 0.00 USD | 447.01 USD | `-31.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 299,420.00 USD | 0.00 USD | 40,560.00 USD | `-29.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 258,860.00 USD | 0.00 USD | 489.57 USD | `-28.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 258,370.00 USD | 0.00 USD | 1,550.00 USD | `-27.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 256,820.00 USD | 0.00 USD | 9,840.00 USD | `-27.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 246,980.00 USD | 0.00 USD | 2,060.00 USD | `-26.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 244,920.00 USD | 0.00 USD | 2,960.00 USD | `-25.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 241,970.00 USD | 0.00 USD | 6,050.00 USD | `-24.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 235,910.00 USD | 0.00 USD | 5,680.00 USD | `-22.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 230,230.00 USD | 0.00 USD | 672.22 USD | `-20.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 229,560.00 USD | 0.00 USD | 213.80 USD | `-19.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 229,350.00 USD | 0.00 USD | 223.20 USD | `-19.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 229,130.00 USD | 0.00 USD | 391.13 USD | `-19.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 228,730.00 USD | 0.00 USD | 7,080.00 USD | `-18.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 221,660.00 USD | 0.00 USD | 1,370.00 USD | `-17.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 220,290.00 USD | 0.00 USD | 553.80 USD | `-16.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 219,740.00 USD | 0.00 USD | 14,000.00 USD | `-15.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 205,740.00 USD | 0.00 USD | 158.56 USD | `-15.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 205,580.00 USD | 0.00 USD | 373.28 USD | `-14.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 205,210.00 USD | 0.00 USD | 849.46 USD | `-14.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 204,360.00 USD | 0.00 USD | 1,150.00 USD | `-13.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 203,210.00 USD | 0.00 USD | 1,740.00 USD | `-11.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 201,470.00 USD | 0.00 USD | 981.00 USD | `-11.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.35` | 200,490.00 USD | 0.00 USD | 817.24 USD | `-10.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 199,670.00 USD | 0.00 USD | 237.85 USD | `-10.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.55` | 199,430.00 USD | 0.00 USD | 1,250.00 USD | `-10.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 198,180.00 USD | 0.00 USD | 298.20 USD | `-9.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 197,890.00 USD | 0.00 USD | 14,650.00 USD | `-9.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 183,230.00 USD | 0.00 USD | 6,410.00 USD | `-9.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 176,820.00 USD | 0.00 USD | 459.70 USD | `-9.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 176,360.00 USD | 0.00 USD | 144.57 USD | `-8.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 176,210.00 USD | 0.00 USD | 1,020.00 USD | `-7.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 175,190.00 USD | 0.00 USD | 439.89 USD | `-7.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.45` | 174,750.00 USD | 0.00 USD | 204.26 USD | `-7.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 174,550.00 USD | 0.00 USD | 7,320.00 USD | `-6.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.95` | 167,230.00 USD | 0.00 USD | 8,700.00 USD | `-6.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 158,520.00 USD | 0.00 USD | 27,730.00 USD | `-6.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 130,790.00 USD | 0.00 USD | 51,800.00 USD | `-5.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 78,990.00 USD | 0.00 USD | 10,530.00 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 68,460.00 USD | 0.00 USD | 271.13 USD | `-4.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 68,190.00 USD | 0.00 USD | 1,100.00 USD | `-4.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 67,090.00 USD | 0.00 USD | 12,330.00 USD | `-4.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 54,760.00 USD | 0.00 USD | 460.81 USD | `-4.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.25` | 54,300.00 USD | 0.00 USD | 881.82 USD | `-3.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 53,420.00 USD | 0.00 USD | 566.57 USD | `-3.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 52,850.00 USD | 0.00 USD | 5,950.00 USD | `-3.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 46,910.00 USD | 0.00 USD | 1,370.00 USD | `-3.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.75` | 45,540.00 USD | 0.00 USD | 234.35 USD | `-3.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 45,300.00 USD | 0.00 USD | 462.03 USD | `-2.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 44,840.00 USD | 0.00 USD | 746.97 USD | `-2.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 44,090.00 USD | 0.00 USD | 3,090.00 USD | `-2.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 41,000.00 USD | 0.00 USD | 156.53 USD | `-1.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.45` | 40,850.00 USD | 0.00 USD | 570.09 USD | `-1.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.55` | 40,280.00 USD | 0.00 USD | 1,690.00 USD | `-1.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.65` | 38,590.00 USD | 0.00 USD | 198.38 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.75` | 38,390.00 USD | 0.00 USD | 198.74 USD | `-1.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 38,190.00 USD | 0.00 USD | 33,280.00 USD | `-1.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.95` | 4,910.00 USD | 0.00 USD | 397.84 USD | `-0.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 4,510.00 USD | 0.00 USD | 1,580.00 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.15` | 2,940.00 USD | 0.00 USD | 398.18 USD | `-0.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.25` | 2,540.00 USD | 0.00 USD | 398.90 USD | `-0.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.35` | 2,140.00 USD | 0.00 USD | 2,140.00 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.55` | 113.88 USD | 113.88 USD | 0.00 USD | `+0.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.65` | 3,730.00 USD | 3,610.00 USD | 0.00 USD | `+0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.75` | 3,930.00 USD | 202.37 USD | 0.00 USD | `+0.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.85` | 4,120.00 USD | 196.59 USD | 0.00 USD | `+0.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.95` | 4,320.00 USD | 193.03 USD | 0.00 USD | `+0.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.05` | 4,910.00 USD | 587.96 USD | 0.00 USD | `+1.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.15` | 5,300.00 USD | 397.54 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.25` | 5,510.00 USD | 204.19 USD | 0.00 USD | `+1.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.35` | 6,040.00 USD | 535.33 USD | 0.00 USD | `+1.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.45` | 6,450.00 USD | 407.57 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.55` | 9,090.00 USD | 2,640.00 USD | 0.00 USD | `+2.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.65` | 9,210.00 USD | 121.23 USD | 0.00 USD | `+2.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.75` | 9,440.00 USD | 228.70 USD | 0.00 USD | `+2.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.85` | 27,470.00 USD | 18,030.00 USD | 0.00 USD | `+2.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.95` | 27,860.00 USD | 390.68 USD | 0.00 USD | `+2.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.05` | 33,660.00 USD | 5,800.00 USD | 0.00 USD | `+2.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.15` | 34,050.00 USD | 392.05 USD | 0.00 USD | `+3.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.25` | 34,250.00 USD | 201.52 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.45` | 34,600.00 USD | 344.70 USD | 0.00 USD | `+3.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.55` | 54,960.00 USD | 20,360.00 USD | 0.00 USD | `+3.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.65` | 55,160.00 USD | 198.89 USD | 0.00 USD | `+4.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.75` | 55,280.00 USD | 119.54 USD | 0.00 USD | `+4.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.95` | 55,400.00 USD | 128.65 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 56,030.00 USD | 621.13 USD | 0.00 USD | `+4.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 56,230.00 USD | 200.04 USD | 0.00 USD | `+4.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 56,430.00 USD | 200.96 USD | 0.00 USD | `+5.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 56,550.00 USD | 123.70 USD | 0.00 USD | `+5.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 57,150.00 USD | 601.45 USD | 0.00 USD | `+5.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 57,550.00 USD | 401.65 USD | 0.00 USD | `+5.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.65` | 57,830.00 USD | 274.48 USD | 0.00 USD | `+5.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 58,320.00 USD | 491.15 USD | 0.00 USD | `+6.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 61,260.00 USD | 2,940.00 USD | 0.00 USD | `+6.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 61,390.00 USD | 129.69 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 66,190.00 USD | 4,800.00 USD | 0.00 USD | `+6.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 67,470.00 USD | 1,280.00 USD | 0.00 USD | `+6.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.25` | 67,780.00 USD | 307.51 USD | 0.00 USD | `+6.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 68,240.00 USD | 461.74 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 68,400.00 USD | 159.92 USD | 0.00 USD | `+7.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.55` | 68,900.00 USD | 496.65 USD | 0.00 USD | `+7.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 69,620.00 USD | 724.75 USD | 0.00 USD | `+7.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.75` | 69,730.00 USD | 113.53 USD | 0.00 USD | `+7.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 69,890.00 USD | 158.00 USD | 0.00 USD | `+7.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 70,060.00 USD | 171.14 USD | 0.00 USD | `+8.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 70,610.00 USD | 551.00 USD | 0.00 USD | `+8.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 71,490.00 USD | 878.58 USD | 0.00 USD | `+9.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 72,880.00 USD | 1,390.00 USD | 0.00 USD | `+9.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 73,870.00 USD | 986.99 USD | 0.00 USD | `+9.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 74,540.00 USD | 674.72 USD | 0.00 USD | `+9.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 76,900.00 USD | 2,360.00 USD | 0.00 USD | `+10.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 77,030.00 USD | 125.56 USD | 0.00 USD | `+10.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 80,620.00 USD | 3,600.00 USD | 0.00 USD | `+10.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 81,270.00 USD | 643.20 USD | 0.00 USD | `+11.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.95` | 83,390.00 USD | 2,120.00 USD | 0.00 USD | `+11.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 83,520.00 USD | 130.31 USD | 0.00 USD | `+11.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.45` | 83,740.00 USD | 217.95 USD | 0.00 USD | `+12.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.55` | 84,080.00 USD | 347.15 USD | 0.00 USD | `+12.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 84,800.00 USD | 716.72 USD | 0.00 USD | `+13.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.75` | 84,940.00 USD | 141.19 USD | 0.00 USD | `+13.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 85,170.00 USD | 231.39 USD | 0.00 USD | `+13.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 85,680.00 USD | 508.36 USD | 0.00 USD | `+13.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 86,380.00 USD | 703.97 USD | 0.00 USD | `+14.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.35` | 86,530.00 USD | 140.64 USD | 0.00 USD | `+14.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 87,190.00 USD | 668.13 USD | 0.00 USD | `+14.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 91,740.00 USD | 4,550.00 USD | 0.00 USD | `+14.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 92,300.00 USD | 555.03 USD | 0.00 USD | `+14.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 92,830.00 USD | 531.62 USD | 0.00 USD | `+15.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.35` | 93,490.00 USD | 664.09 USD | 0.00 USD | `+16.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.45` | 94,160.00 USD | 665.12 USD | 0.00 USD | `+16.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 94,360.00 USD | 202.69 USD | 0.00 USD | `+16.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 94,660.00 USD | 298.04 USD | 0.00 USD | `+16.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 94,760.00 USD | 102.13 USD | 0.00 USD | `+17.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 95,300.00 USD | 540.09 USD | 0.00 USD | `+17.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 95,400.00 USD | 100.79 USD | 0.00 USD | `+18.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 95,670.00 USD | 262.20 USD | 0.00 USD | `+18.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 96,040.00 USD | 371.49 USD | 0.00 USD | `+18.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.85` | 96,920.00 USD | 881.07 USD | 0.00 USD | `+18.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 97,610.00 USD | 696.17 USD | 0.00 USD | `+19.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 98,150.00 USD | 534.00 USD | 0.00 USD | `+20.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 109,230.00 USD | 11,080.00 USD | 0.00 USD | `+20.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 122,640.00 USD | 13,410.00 USD | 0.00 USD | `+20.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.05` | 125,000.00 USD | 2,360.00 USD | 0.00 USD | `+22.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 129,860.00 USD | 4,860.00 USD | 0.00 USD | `+23.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 130,070.00 USD | 204.48 USD | 0.00 USD | `+25.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 130,880.00 USD | 810.02 USD | 0.00 USD | `+26.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 450,770.00 USD | 319,890.00 USD | 0.00 USD | `+26.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 450,940.00 USD | 170.04 USD | 0.00 USD | `+27.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 456,710.00 USD | 5,770.00 USD | 0.00 USD | `+28.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 456,980.00 USD | 269.28 USD | 0.00 USD | `+28.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 457,270.00 USD | 291.40 USD | 0.00 USD | `+29.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 464,840.00 USD | 7,580.00 USD | 0.00 USD | `+30.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 465,000.00 USD | 156.78 USD | 0.00 USD | `+30.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 468,220.00 USD | 3,220.00 USD | 0.00 USD | `+31.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 468,630.00 USD | 411.14 USD | 0.00 USD | `+32.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 591,820.00 USD | 123,190.00 USD | 0.00 USD | `+33.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 592,840.00 USD | 1,020.00 USD | 0.00 USD | `+34.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 592,950.00 USD | 104.93 USD | 0.00 USD | `+35.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 601,160.00 USD | 8,210.00 USD | 0.00 USD | `+35.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 601,560.00 USD | 402.59 USD | 0.00 USD | `+35.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.85` | 601,870.00 USD | 308.71 USD | 0.00 USD | `+36.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 602,180.00 USD | 315.18 USD | 0.00 USD | `+39.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 661,490.00 USD | 59,310.00 USD | 0.00 USD | `+41.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 664,650.00 USD | 3,160.00 USD | 0.00 USD | `+42.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 670,340.00 USD | 5,690.00 USD | 0.00 USD | `+43.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 706,930.00 USD | 36,590.00 USD | 0.00 USD | `+44.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 707,370.00 USD | 433.89 USD | 0.00 USD | `+46.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 707,540.00 USD | 172.64 USD | 0.00 USD | `+46.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 707,700.00 USD | 164.10 USD | 0.00 USD | `+48.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 708,250.00 USD | 546.81 USD | 0.00 USD | `+49.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 710,550.00 USD | 2,300.00 USD | 0.00 USD | `+51.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 722,620.00 USD | 12,070.00 USD | 0.00 USD | `+53.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.75` | 734,950.00 USD | 12,330.00 USD | 0.00 USD | `+54.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.05` | 755,180.00 USD | 20,230.00 USD | 0.00 USD | `+57.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.25` | 755,620.00 USD | 435.38 USD | 0.00 USD | `+57.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 757,200.00 USD | 1,580.00 USD | 0.00 USD | `+58.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 794,200.00 USD | 37,000.00 USD | 0.00 USD | `+58.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 794,670.00 USD | 473.21 USD | 0.00 USD | `+60.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 795,940.00 USD | 1,270.00 USD | 0.00 USD | `+60.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 797,570.00 USD | 1,630.00 USD | 0.00 USD | `+61.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 816,320.00 USD | 18,740.00 USD | 0.00 USD | `+62.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 816,800.00 USD | 481.55 USD | 0.00 USD | `+65.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 818,130.00 USD | 1,330.00 USD | 0.00 USD | `+66.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 818,310.00 USD | 188.10 USD | 0.00 USD | `+69.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,080,000.00 USD | 266,140.00 USD | 0.00 USD | `+71.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,090,000.00 USD | 3,400.00 USD | 0.00 USD | `+72.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,110,000.00 USD | 21,930.00 USD | 0.00 USD | `+73.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,110,000.00 USD | 294.15 USD | 0.00 USD | `+76.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,110,000.00 USD | 4,010.00 USD | 0.00 USD | `+80.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,110,000.00 USD | 306.15 USD | 0.00 USD | `+84.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,120,000.00 USD | 936.72 USD | 0.00 USD | `+85.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,120,000.00 USD | 2,920.00 USD | 0.00 USD | `+86.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,120,000.00 USD | 324.15 USD | 0.00 USD | `+94.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 1,120,000.00 USD | 123.23 USD | 0.00 USD | `+96.77%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `49.30` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 13,300.00 USD | 3,500.00 USD | 367.32 USD |
| `7D` | `49.30` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 15,190.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `49.40` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 626.48 USD |
| `7D` | `49.40` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD |
| `1D` | `49.50` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 1,180.00 USD | 4,790.00 USD | 13,790.00 USD |
| `7D` | `49.50` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 1,130.00 USD | 6,290.00 USD | 0.00 USD |
| `1D` | `49.60` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 785.85 USD | 4,760.00 USD | 0.00 USD |
| `7D` | `49.60` | 7,970,000.00 USD | 0.00 USD | 7,970,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD |
| `1D` | `49.70` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 1,320.00 USD | 0.00 USD | 301.72 USD |
| `7D` | `49.70` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 788.92 USD | 0.00 USD | 4,900.00 USD |
| `1D` | `49.80` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 667.20 USD | 733.27 USD | 11,870.00 USD |
| `7D` | `49.80` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 7,660.00 USD | 8,220.00 USD | 0.00 USD |
| `1D` | `49.90` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 17,040.00 USD | 7,110.00 USD | 22,850.00 USD |
| `7D` | `49.90` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 45,030.00 USD | 5,410.00 USD | 4,700.00 USD |
| `1D` | `50.00` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 4,470.00 USD | 5,550.00 USD | 40,300.00 USD |
| `7D` | `50.00` | 7,880,000.00 USD | 0.00 USD | 7,880,000.00 USD | 22,100.00 USD | 7,630.00 USD | 24,550.00 USD |
| `1D` | `50.10` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 0.00 USD | 3,330.00 USD | 0.00 USD |
| `7D` | `50.10` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 363.50 USD | 682.90 USD | 0.00 USD |
| `7D` | `50.20` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 6,960.00 USD | 500.40 USD | 34,680.00 USD |
| `1D` | `50.30` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 0.00 USD | 333.03 USD | 0.00 USD |
| `7D` | `50.30` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 16,270.00 USD | 3,640.00 USD | 1,950.00 USD |
| `1D` | `50.40` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 349.63 USD | 2,190.00 USD | 0.00 USD |
| `7D` | `50.40` | 7,760,000.00 USD | 0.00 USD | 7,760,000.00 USD | 23,520.00 USD | 19,110.00 USD | 33,450.00 USD |
| `7D` | `50.50` | 7,680,000.00 USD | 0.00 USD | 7,680,000.00 USD | 24,840.00 USD | 6,790.00 USD | 43,710.00 USD |
| `7D` | `50.60` | 7,610,000.00 USD | 0.00 USD | 7,610,000.00 USD | 52,670.00 USD | 17,830.00 USD | 22,250.00 USD |
| `7D` | `50.70` | 7,510,000.00 USD | 0.00 USD | 7,510,000.00 USD | 53,670.00 USD | 24,710.00 USD | 32,520.00 USD |
| `1D` | `50.80` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 5,630.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `50.80` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD |
| `1D` | `50.90` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 0.00 USD | 260.05 USD | 8,390.00 USD |
| `7D` | `50.90` | 7,310,000.00 USD | 0.00 USD | 7,310,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD |
| `1D` | `51.00` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 129.78 USD |
| `7D` | `51.00` | 7,050,000.00 USD | 0.00 USD | 7,050,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `51.10` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 263.90 USD | 1,160.00 USD | 0.00 USD |
| `7D` | `51.10` | 6,930,000.00 USD | 0.00 USD | 6,930,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD |
| `1D` | `51.20` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 1,100.00 USD | 1,130.00 USD | 327.72 USD |
| `7D` | `51.20` | 6,850,000.00 USD | 0.00 USD | 6,850,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD |
| `1D` | `51.30` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 20,430.00 USD | 5,150.00 USD | 18,640.00 USD |
| `7D` | `51.30` | 6,780,000.00 USD | 0.00 USD | 6,780,000.00 USD | 19,510.00 USD | 12,490.00 USD | 47,090.00 USD |
| `1D` | `51.40` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 17,510.00 USD | 7,090.00 USD | 10,780.00 USD |
| `7D` | `51.40` | 6,700,000.00 USD | 0.00 USD | 6,700,000.00 USD | 71,090.00 USD | 28,960.00 USD | 45,150.00 USD |
| `1D` | `51.50` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 11,450.00 USD | 8,980.00 USD | 4,080.00 USD |
| `7D` | `51.50` | 6,560,000.00 USD | 0.00 USD | 6,560,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `51.60` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 8,800.00 USD | 7,990.00 USD | 4,820.00 USD |
| `7D` | `51.60` | 6,460,000.00 USD | 0.00 USD | 6,460,000.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD |
| `1D` | `51.70` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 4,980.00 USD | 4,150.00 USD | 6,480.00 USD |
| `7D` | `51.70` | 6,400,000.00 USD | 0.00 USD | 6,400,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `51.80` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 13,220.00 USD | 2,080.00 USD | 10,050.00 USD |
| `7D` | `51.80` | 6,360,000.00 USD | 0.00 USD | 6,360,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD |
| `1D` | `51.90` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 12,520.00 USD | 21,470.00 USD | 9,190.00 USD |
| `7D` | `51.90` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 5,870.00 USD | 15,810.00 USD | 4,760.00 USD |
| `1D` | `52.00` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 25,510.00 USD | 8,240.00 USD | 23,340.00 USD |
| `7D` | `52.00` | 6,280,000.00 USD | 0.00 USD | 6,280,000.00 USD | 64,300.00 USD | 20,800.00 USD | 11,880.00 USD |
| `1D` | `52.10` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 27,630.00 USD | 5,780.00 USD | 35,220.00 USD |
| `7D` | `52.10` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 24,220.00 USD | 18,810.00 USD | 35,480.00 USD |
| `1D` | `52.20` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 20,520.00 USD | 10,460.00 USD | 14,390.00 USD |
| `7D` | `52.20` | 6,100,000.00 USD | 0.00 USD | 6,100,000.00 USD | 38,380.00 USD | 4,340.00 USD | 25,270.00 USD |
| `1D` | `52.30` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 38,870.00 USD | 8,170.00 USD | 16,110.00 USD |
| `7D` | `52.30` | 6,040,000.00 USD | 0.00 USD | 6,040,000.00 USD | 18,740.00 USD | 12,840.00 USD | 8,940.00 USD |
| `1D` | `52.40` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 11,440.00 USD | 7,510.00 USD | 6,280.00 USD |
| `7D` | `52.40` | 6,000,000.00 USD | 0.00 USD | 6,000,000.00 USD | 20,580.00 USD | 11,230.00 USD | 20,050.00 USD |
| `1D` | `52.50` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 48,310.00 USD | 13,510.00 USD | 998.32 USD |
| `7D` | `52.50` | 5,940,000.00 USD | 0.00 USD | 5,940,000.00 USD | 33,240.00 USD | 667.05 USD | 11,240.00 USD |
| `1D` | `52.60` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 4,750.00 USD | 9,470.00 USD | 506.16 USD |
| `7D` | `52.60` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 74,610.00 USD | 14,530.00 USD | 584.77 USD |
| `1D` | `52.70` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 13,770.00 USD | 7,610.00 USD | 15,080.00 USD |
| `7D` | `52.70` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 20,250.00 USD | 43,820.00 USD | 62,360.00 USD |
| `1D` | `52.80` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 14,400.00 USD | 16,680.00 USD | 74,160.00 USD |
| `7D` | `52.80` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 46,600.00 USD | 29,900.00 USD | 108.50 USD |
| `1D` | `52.90` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 40,590.00 USD | 12,380.00 USD | 6,120.00 USD |
| `7D` | `52.90` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 51,920.00 USD | 26,170.00 USD | 34,400.00 USD |
| `1D` | `53.00` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 4,280.00 USD | 4,790.00 USD | 1,690.00 USD |
| `7D` | `53.00` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 18,990.00 USD | 8,880.00 USD | 55,850.00 USD |
| `1D` | `53.10` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 22,820.00 USD | 8,110.00 USD | 54,830.00 USD |
| `7D` | `53.10` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 52,760.00 USD | 36,340.00 USD | 9,860.00 USD |
| `1D` | `53.20` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 68,490.00 USD | 24,650.00 USD | 63,450.00 USD |
| `7D` | `53.20` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 141,420.00 USD | 38,500.00 USD | 27,410.00 USD |
| `1D` | `53.30` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 27,380.00 USD | 24,540.00 USD | 41,770.00 USD |
| `7D` | `53.30` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 63,050.00 USD | 18,150.00 USD | 37,140.00 USD |
| `1D` | `53.40` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 14,390.00 USD | 14,900.00 USD | 75,840.00 USD |
| `7D` | `53.40` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 48,160.00 USD | 18,090.00 USD | 95,920.00 USD |
| `1D` | `53.50` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 14,780.00 USD | 11,880.00 USD | 7,160.00 USD |
| `7D` | `53.50` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 49,490.00 USD | 8,960.00 USD | 17,890.00 USD |
| `1D` | `53.60` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 74,660.00 USD | 18,710.00 USD | 1,840.00 USD |
| `7D` | `53.60` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 53,580.00 USD | 6,140.00 USD | 98,560.00 USD |
| `1D` | `53.70` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 5,710.00 USD | 8,090.00 USD | 465.28 USD |
| `7D` | `53.70` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 131,400.00 USD | 16,400.00 USD | 10,200.00 USD |
| `1D` | `53.80` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 16,800.00 USD | 5,480.00 USD | 3,130.00 USD |
| `7D` | `53.80` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 99,150.00 USD | 80,510.00 USD | 126,140.00 USD |
| `1D` | `53.90` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 7,480.00 USD | 28,010.00 USD | 125,910.00 USD |
| `7D` | `53.90` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 111,970.00 USD | 56,750.00 USD | 123,850.00 USD |
| `1D` | `54.00` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 28,730.00 USD | 24,090.00 USD | 0.00 USD |
| `7D` | `54.00` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 344,710.00 USD | 148,420.00 USD | 271,500.00 USD |
| `1D` | `54.10` | 975,740.00 USD | 0.00 USD | 975,740.00 USD | 23,830.00 USD | 5,860.00 USD | 1,510.00 USD |
| `7D` | `54.10` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 234,120.00 USD | 45,470.00 USD | 184,480.00 USD |
| `1D` | `54.20` | 944,540.00 USD | 0.00 USD | 944,540.00 USD | 54,060.00 USD | 12,370.00 USD | 108,330.00 USD |
| `7D` | `54.20` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 234,980.00 USD | 155,540.00 USD | 128,910.00 USD |
| `1D` | `54.30` | 769,790.00 USD | 0.00 USD | 769,790.00 USD | 127,400.00 USD | 36,500.00 USD | 142,890.00 USD |
| `7D` | `54.30` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 339,300.00 USD | 131,670.00 USD | 185,160.00 USD |
| `1D` | `54.40` | 463,000.00 USD | 0.00 USD | 463,000.00 USD | 37,530.00 USD | 43,760.00 USD | 78,270.00 USD |
| `7D` | `54.40` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 304,270.00 USD | 13,830.00 USD | 92,140.00 USD |
| `1D` | `54.50` | 303,430.00 USD | 0.00 USD | 303,430.00 USD | 9,670.00 USD | 24,030.00 USD | 144,050.00 USD |
| `7D` | `54.50` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 159,720.00 USD | 36,920.00 USD | 237,000.00 USD |
| `1D` | `54.60` | 125,680.00 USD | 0.00 USD | 125,680.00 USD | 18,470.00 USD | 15,070.00 USD | 14,320.00 USD |
| `7D` | `54.60` | 584,340.00 USD | 0.00 USD | 584,340.00 USD | 0.00 USD | 1,930.00 USD | 72,400.00 USD |
| `1D` | `54.70` | 77,810.00 USD | 0.00 USD | 77,810.00 USD | 0.00 USD | 0.00 USD | 57,100.00 USD |
| `7D` | `54.70` | 510,010.00 USD | 0.00 USD | 510,010.00 USD | 0.00 USD | 0.00 USD | 173,390.00 USD |
| `1D` | `54.80` | 20,710.00 USD | 0.00 USD | 20,710.00 USD | 0.00 USD | 9,420.00 USD | 0.00 USD |
| `1D` | `55.10` | 11,290.00 USD | 0.00 USD | 11,290.00 USD | 0.00 USD | 0.00 USD | 189.61 USD |
| `1D` | `55.20` | 11,100.00 USD | 0.00 USD | 11,100.00 USD | 11,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.20` | 336,630.00 USD | 0.00 USD | 336,630.00 USD | 336,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `55.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.50` | 326,800.00 USD | 326,800.00 USD | 0.00 USD | 326,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.60` | 753,140.00 USD | 753,140.00 USD | 0.00 USD | 426,340.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `55.70` | 407.86 USD | 407.86 USD | 0.00 USD | 0.00 USD | 0.00 USD | 407.86 USD |
| `7D` | `55.70` | 959,560.00 USD | 959,560.00 USD | 0.00 USD | 174,240.00 USD | 32,180.00 USD | 0.00 USD |
| `1D` | `55.80` | 63,390.00 USD | 63,390.00 USD | 0.00 USD | 0.00 USD | 16,300.00 USD | 46,680.00 USD |
| `7D` | `55.80` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD |
| `1D` | `55.90` | 342,140.00 USD | 342,140.00 USD | 0.00 USD | 137,200.00 USD | 1,440.00 USD | 140,110.00 USD |
| `7D` | `55.90` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 141,330.00 USD | 65,840.00 USD | 0.00 USD |
| `1D` | `56.00` | 541,410.00 USD | 541,410.00 USD | 0.00 USD | 139,840.00 USD | 0.00 USD | 59,430.00 USD |
| `7D` | `56.00` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 181,230.00 USD | 98,600.00 USD | 147,270.00 USD |
| `1D` | `56.10` | 849,920.00 USD | 849,920.00 USD | 0.00 USD | 105,950.00 USD | 28,010.00 USD | 174,550.00 USD |
| `7D` | `56.10` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 121,920.00 USD | 144,120.00 USD | 61,210.00 USD |
| `1D` | `56.20` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 96,820.00 USD | 83,660.00 USD | 71,790.00 USD |
| `7D` | `56.20` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 104,510.00 USD | 72,410.00 USD | 240,740.00 USD |
| `1D` | `56.30` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 464.20 USD | 37,150.00 USD | 38,390.00 USD |
| `7D` | `56.30` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 91,850.00 USD | 128,970.00 USD | 131,790.00 USD |
| `1D` | `56.40` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 39,090.00 USD | 43,300.00 USD | 225,690.00 USD |
| `7D` | `56.40` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 215,940.00 USD | 116,750.00 USD | 137,070.00 USD |
| `1D` | `56.50` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 117,430.00 USD | 142,630.00 USD | 114,250.00 USD |
| `7D` | `56.50` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 128,680.00 USD | 125,310.00 USD | 3,750.00 USD |
| `1D` | `56.60` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 34,340.00 USD | 101,890.00 USD | 77,950.00 USD |
| `7D` | `56.60` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 363,190.00 USD | 126,950.00 USD | 0.00 USD |
| `1D` | `56.70` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 203,710.00 USD | 24,030.00 USD | 345,780.00 USD |
| `7D` | `56.70` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 110,940.00 USD | 121,500.00 USD | 96,070.00 USD |
| `1D` | `56.80` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 196,380.00 USD | 17,250.00 USD | 116,650.00 USD |
| `7D` | `56.80` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 153,580.00 USD | 92,780.00 USD | 261,330.00 USD |
| `1D` | `56.90` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 33,240.00 USD | 8,150.00 USD | 1,780.00 USD |
| `7D` | `56.90` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 108,440.00 USD | 48,600.00 USD | 266,610.00 USD |
| `1D` | `57.00` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 12,360.00 USD | 659.87 USD |
| `7D` | `57.00` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 88,680.00 USD | 2,620.00 USD | 93,100.00 USD |
| `1D` | `57.10` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 7,480.00 USD | 10,960.00 USD | 5,950.00 USD |
| `7D` | `57.10` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 36,580.00 USD | 16,110.00 USD | 20,440.00 USD |
| `1D` | `57.20` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 14,000.00 USD | 63,210.00 USD |
| `7D` | `57.20` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 21,160.00 USD | 15,720.00 USD | 3,700.00 USD |
| `1D` | `57.30` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 12,360.00 USD | 12,450.00 USD | 386.57 USD |
| `7D` | `57.30` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 22,360.00 USD | 3,150.00 USD | 34,250.00 USD |
| `1D` | `57.40` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 19,650.00 USD | 28,690.00 USD | 754.29 USD |
| `7D` | `57.40` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 38,520.00 USD | 30,000.00 USD | 153,130.00 USD |
| `1D` | `57.50` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 128,210.00 USD | 19,060.00 USD | 90,610.00 USD |
| `7D` | `57.50` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 76,670.00 USD | 30,210.00 USD | 0.00 USD |
| `1D` | `57.60` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 58,710.00 USD | 18,250.00 USD | 57,130.00 USD |
| `7D` | `57.60` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 123,760.00 USD | 36,020.00 USD | 28,320.00 USD |
| `1D` | `57.70` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 28,040.00 USD | 23,180.00 USD | 96,250.00 USD |
| `7D` | `57.70` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 0.00 USD | 5,400.00 USD | 57,330.00 USD |
| `1D` | `57.80` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 5,680.00 USD | 12,010.00 USD | 72,680.00 USD |
| `7D` | `57.80` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 2,260.00 USD | 14,360.00 USD | 48,030.00 USD |
| `1D` | `57.90` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 9,550.00 USD | 14,100.00 USD | 7,160.00 USD |
| `7D` | `57.90` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 2,410.00 USD | 963.90 USD | 1,510.00 USD |
| `1D` | `58.00` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 3,570.00 USD | 5,650.00 USD | 0.00 USD |
| `7D` | `58.00` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 3,670.00 USD | 86,690.00 USD |
| `1D` | `58.10` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 29,450.00 USD | 6,730.00 USD | 9,350.00 USD |
| `7D` | `58.10` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD | 848.40 USD |
| `1D` | `58.20` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 1,980.00 USD | 5,880.00 USD | 350.42 USD |
| `1D` | `58.30` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 10,290.00 USD | 11,540.00 USD | 36,830.00 USD |
| `7D` | `58.30` | 6,400,000.00 USD | 6,400,000.00 USD | 0.00 USD | 0.00 USD | 9,580.00 USD | 26,820.00 USD |
| `1D` | `58.40` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 4,990.00 USD | 33,950.00 USD |
| `7D` | `58.40` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 54,120.00 USD |
| `1D` | `58.50` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 49,290.00 USD | 21,280.00 USD | 379.22 USD |
| `7D` | `58.50` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD |
| `7D` | `58.60` | 6,480,000.00 USD | 6,480,000.00 USD | 0.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `58.70` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 15,850.00 USD | 8,070.00 USD | 355.85 USD |
| `7D` | `58.70` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 1,700.00 USD | 5,910.00 USD | 35,320.00 USD |
| `1D` | `58.80` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 35,140.00 USD | 14,730.00 USD | 23,630.00 USD |
| `7D` | `58.80` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 1,810.00 USD | 3,320.00 USD | 6,410.00 USD |
| `1D` | `58.90` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 19,290.00 USD | 124,640.00 USD | 91,310.00 USD |
| `7D` | `58.90` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 0.00 USD | 48,700.00 USD | 83,500.00 USD |
| `1D` | `59.00` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 151,460.00 USD | 57,130.00 USD | 134,010.00 USD |
| `7D` | `59.00` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 255,180.00 USD | 65,270.00 USD | 118,570.00 USD |
| `1D` | `59.10` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 191,140.00 USD | 49,070.00 USD | 186,370.00 USD |
| `7D` | `59.10` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 91,060.00 USD | 45,400.00 USD | 158,780.00 USD |
| `1D` | `59.20` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 159,440.00 USD | 75,750.00 USD | 96,020.00 USD |
| `7D` | `59.20` | 7,740,000.00 USD | 7,740,000.00 USD | 0.00 USD | 153,580.00 USD | 12,460.00 USD | 174,600.00 USD |
| `1D` | `59.30` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 306,360.00 USD | 73,700.00 USD | 143,250.00 USD |
| `7D` | `59.30` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD |
| `1D` | `59.40` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 78,860.00 USD | 57,010.00 USD | 76,960.00 USD |
| `7D` | `59.40` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 103,370.00 USD | 73,620.00 USD | 137,500.00 USD |
| `1D` | `59.50` | 6,460,000.00 USD | 6,460,000.00 USD | 0.00 USD | 119,350.00 USD | 57,690.00 USD | 28,370.00 USD |
| `7D` | `59.50` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD |
| `1D` | `59.60` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 62,780.00 USD | 68,870.00 USD | 18,340.00 USD |
| `7D` | `59.60` | 8,980,000.00 USD | 8,980,000.00 USD | 0.00 USD | 268,680.00 USD | 145,550.00 USD | 86,840.00 USD |
| `1D` | `59.70` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 20,820.00 USD | 30,890.00 USD | 94,130.00 USD |
| `7D` | `59.70` | 9,380,000.00 USD | 9,380,000.00 USD | 0.00 USD | 55,510.00 USD | 180,620.00 USD | 161,880.00 USD |
| `1D` | `59.80` | 6,840,000.00 USD | 6,840,000.00 USD | 0.00 USD | 40,970.00 USD | 37,360.00 USD | 10,870.00 USD |
| `7D` | `59.80` | 9,750,000.00 USD | 9,750,000.00 USD | 0.00 USD | 118,240.00 USD | 97,600.00 USD | 155,270.00 USD |
| `1D` | `59.90` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 112,870.00 USD | 21,300.00 USD | 80,370.00 USD |
| `7D` | `59.90` | 10,120,000.00 USD | 10,120,000.00 USD | 0.00 USD | 246,770.00 USD | 84,430.00 USD | 40,130.00 USD |
| `1D` | `60.00` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 182,880.00 USD | 64,320.00 USD | 69,570.00 USD |
| `7D` | `60.00` | 10,630,000.00 USD | 10,630,000.00 USD | 0.00 USD | 231,370.00 USD | 183,130.00 USD | 94,160.00 USD |
| `1D` | `60.10` | 7,580,000.00 USD | 7,580,000.00 USD | 0.00 USD | 95,780.00 USD | 40,330.00 USD | 71,530.00 USD |
| `7D` | `60.10` | 11,200,000.00 USD | 11,200,000.00 USD | 0.00 USD | 263,890.00 USD | 129,860.00 USD | 174,140.00 USD |
| `1D` | `60.20` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 119,070.00 USD | 37,570.00 USD | 96,900.00 USD |
| `7D` | `60.20` | 11,700,000.00 USD | 11,700,000.00 USD | 0.00 USD | 207,990.00 USD | 131,530.00 USD | 157,150.00 USD |
| `1D` | `60.30` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 97,720.00 USD | 71,550.00 USD | 82,910.00 USD |
| `7D` | `60.30` | 12,080,000.00 USD | 12,080,000.00 USD | 0.00 USD | 133,350.00 USD | 95,890.00 USD | 155,610.00 USD |
| `1D` | `60.40` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 168,700.00 USD | 45,260.00 USD | 60,640.00 USD |
| `7D` | `60.40` | 12,530,000.00 USD | 12,530,000.00 USD | 0.00 USD | 93,890.00 USD | 133,310.00 USD | 226,940.00 USD |
| `1D` | `60.50` | 8,530,000.00 USD | 8,530,000.00 USD | 0.00 USD | 69,310.00 USD | 42,290.00 USD | 57,940.00 USD |
| `7D` | `60.50` | 12,960,000.00 USD | 12,960,000.00 USD | 0.00 USD | 131,870.00 USD | 86,290.00 USD | 206,240.00 USD |
| `1D` | `60.60` | 8,640,000.00 USD | 8,640,000.00 USD | 0.00 USD | 69,460.00 USD | 33,050.00 USD | 5,340.00 USD |
| `7D` | `60.60` | 13,400,000.00 USD | 13,400,000.00 USD | 0.00 USD | 251,100.00 USD | 52,650.00 USD | 134,260.00 USD |
| `1D` | `60.70` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 45,500.00 USD | 33,220.00 USD | 985.52 USD |
| `7D` | `60.70` | 13,620,000.00 USD | 13,620,000.00 USD | 0.00 USD | 129,660.00 USD | 67,510.00 USD | 28,990.00 USD |
| `1D` | `60.80` | 8,810,000.00 USD | 8,810,000.00 USD | 0.00 USD | 22,530.00 USD | 12,680.00 USD | 55,210.00 USD |
| `7D` | `60.80` | 13,850,000.00 USD | 13,850,000.00 USD | 0.00 USD | 54,870.00 USD | 78,710.00 USD | 94,850.00 USD |
| `1D` | `60.90` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 57,090.00 USD | 25,670.00 USD | 22,850.00 USD |
| `7D` | `60.90` | 14,110,000.00 USD | 14,110,000.00 USD | 0.00 USD | 116,730.00 USD | 58,270.00 USD | 79,720.00 USD |
| `1D` | `61.00` | 9,000,000.00 USD | 9,000,000.00 USD | 0.00 USD | 46,000.00 USD | 6,970.00 USD | 28,080.00 USD |
| `7D` | `61.00` | 14,240,000.00 USD | 14,240,000.00 USD | 0.00 USD | 96,160.00 USD | 36,500.00 USD | 5,370.00 USD |
| `1D` | `61.10` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 10,580.00 USD | 5,550.00 USD | 11,490.00 USD |
| `7D` | `61.10` | 14,280,000.00 USD | 14,280,000.00 USD | 0.00 USD | 31,540.00 USD | 1,560.00 USD | 0.00 USD |
| `1D` | `61.20` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 75,930.00 USD | 1,160.00 USD | 47,920.00 USD |
| `7D` | `61.20` | 14,520,000.00 USD | 14,520,000.00 USD | 0.00 USD | 116,610.00 USD | 75,410.00 USD | 52,570.00 USD |
| `1D` | `61.30` | 9,170,000.00 USD | 9,170,000.00 USD | 0.00 USD | 9,540.00 USD | 9,090.00 USD | 2,340.00 USD |
| `7D` | `61.30` | 14,660,000.00 USD | 14,660,000.00 USD | 0.00 USD | 51,130.00 USD | 35,650.00 USD | 55,130.00 USD |
| `1D` | `61.40` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 6,350.00 USD | 5,640.00 USD | 1,670.00 USD |
| `7D` | `61.40` | 14,850,000.00 USD | 14,850,000.00 USD | 0.00 USD | 89,350.00 USD | 41,800.00 USD | 59,330.00 USD |
| `1D` | `61.50` | 9,230,000.00 USD | 9,230,000.00 USD | 0.00 USD | 9,120.00 USD | 18,030.00 USD | 17,680.00 USD |
| `7D` | `61.50` | 14,950,000.00 USD | 14,950,000.00 USD | 0.00 USD | 19,810.00 USD | 35,300.00 USD | 36,110.00 USD |
| `1D` | `61.60` | 9,270,000.00 USD | 9,270,000.00 USD | 0.00 USD | 24,180.00 USD | 10,500.00 USD | 8,530.00 USD |
| `7D` | `61.60` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 54,240.00 USD | 63,390.00 USD | 132,550.00 USD |
| `1D` | `61.70` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 31,820.00 USD | 9,150.00 USD | 9,600.00 USD |
| `7D` | `61.70` | 15,410,000.00 USD | 15,410,000.00 USD | 0.00 USD | 84,300.00 USD | 11,330.00 USD | 114,420.00 USD |
| `1D` | `61.80` | 9,350,000.00 USD | 9,350,000.00 USD | 0.00 USD | 18,210.00 USD | 4,670.00 USD | 1,570.00 USD |
| `7D` | `61.80` | 15,670,000.00 USD | 15,670,000.00 USD | 0.00 USD | 160,110.00 USD | 38,970.00 USD | 69,850.00 USD |
| `7D` | `61.90` | 15,810,000.00 USD | 15,810,000.00 USD | 0.00 USD | 72,380.00 USD | 29,730.00 USD | 35,860.00 USD |
| `7D` | `62.00` | 15,930,000.00 USD | 15,930,000.00 USD | 0.00 USD | 56,450.00 USD | 13,260.00 USD | 49,920.00 USD |
| `7D` | `62.10` | 15,970,000.00 USD | 15,970,000.00 USD | 0.00 USD | 14,790.00 USD | 12,820.00 USD | 7,220.00 USD |
| `7D` | `62.20` | 16,080,000.00 USD | 16,080,000.00 USD | 0.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD |
| `7D` | `62.30` | 16,230,000.00 USD | 16,230,000.00 USD | 0.00 USD | 31,770.00 USD | 23,450.00 USD | 97,450.00 USD |
| `7D` | `62.40` | 16,370,000.00 USD | 16,370,000.00 USD | 0.00 USD | 79,620.00 USD | 27,560.00 USD | 30,890.00 USD |
| `7D` | `62.50` | 16,460,000.00 USD | 16,460,000.00 USD | 0.00 USD | 44,300.00 USD | 14,320.00 USD | 26,610.00 USD |
| `7D` | `62.60` | 16,530,000.00 USD | 16,530,000.00 USD | 0.00 USD | 34,910.00 USD | 7,830.00 USD | 27,730.00 USD |
| `7D` | `62.70` | 16,610,000.00 USD | 16,610,000.00 USD | 0.00 USD | 22,020.00 USD | 12,490.00 USD | 47,090.00 USD |
| `7D` | `62.80` | 16,760,000.00 USD | 16,760,000.00 USD | 0.00 USD | 72,250.00 USD | 28,960.00 USD | 45,150.00 USD |
| `7D` | `62.90` | 16,850,000.00 USD | 16,850,000.00 USD | 0.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD |
| `7D` | `63.00` | 16,910,000.00 USD | 16,910,000.00 USD | 0.00 USD | 34,730.00 USD | 12,240.00 USD | 17,650.00 USD |
| `7D` | `63.10` | 16,950,000.00 USD | 16,950,000.00 USD | 0.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD |
| `7D` | `63.30` | 16,990,000.00 USD | 16,990,000.00 USD | 0.00 USD | 17,050.00 USD | 11,500.00 USD | 9,730.00 USD |
| `7D` | `63.40` | 17,010,000.00 USD | 17,010,000.00 USD | 0.00 USD | 13,220.00 USD | 1,320.00 USD | 9,960.00 USD |
| `7D` | `63.50` | 17,040,000.00 USD | 17,040,000.00 USD | 0.00 USD | 6,620.00 USD | 15,810.00 USD | 4,760.00 USD |
| `7D` | `63.60` | 17,140,000.00 USD | 17,140,000.00 USD | 0.00 USD | 63,480.00 USD | 20,800.00 USD | 11,880.00 USD |
| `7D` | `63.70` | 17,210,000.00 USD | 17,210,000.00 USD | 0.00 USD | 21,940.00 USD | 18,810.00 USD | 35,480.00 USD |
| `7D` | `63.80` | 17,280,000.00 USD | 17,280,000.00 USD | 0.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD |
| `7D` | `63.90` | 17,310,000.00 USD | 17,310,000.00 USD | 0.00 USD | 7,650.00 USD | 12,840.00 USD | 8,940.00 USD |
| `7D` | `64.00` | 17,350,000.00 USD | 17,350,000.00 USD | 0.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD |
| `7D` | `64.10` | 17,380,000.00 USD | 17,380,000.00 USD | 0.00 USD | 20,350.00 USD | 667.05 USD | 10,640.00 USD |
| `7D` | `64.20` | 17,420,000.00 USD | 17,420,000.00 USD | 0.00 USD | 28,840.00 USD | 14,530.00 USD | 584.77 USD |
| `7D` | `64.40` | 17,480,000.00 USD | 17,480,000.00 USD | 0.00 USD | 2,540.00 USD | 20,590.00 USD | 29,110.00 USD |
| `7D` | `64.50` | 17,510,000.00 USD | 17,510,000.00 USD | 0.00 USD | 7,700.00 USD | 7,120.00 USD | 13,310.00 USD |
| `7D` | `64.60` | 17,550,000.00 USD | 17,550,000.00 USD | 0.00 USD | 32,220.00 USD | 14,180.00 USD | 108.50 USD |
| `7D` | `64.70` | 17,620,000.00 USD | 17,620,000.00 USD | 0.00 USD | 39,430.00 USD | 23,030.00 USD | 3,870.00 USD |
| `7D` | `64.80` | 17,650,000.00 USD | 17,650,000.00 USD | 0.00 USD | 7,540.00 USD | 8,210.00 USD | 20,430.00 USD |
| `7D` | `64.90` | 17,700,000.00 USD | 17,700,000.00 USD | 0.00 USD | 25,320.00 USD | 8,010.00 USD | 9,860.00 USD |
| `7D` | `65.00` | 17,720,000.00 USD | 17,720,000.00 USD | 0.00 USD | 1,790.00 USD | 9,480.00 USD | 13,480.00 USD |
| `7D` | `65.10` | 17,780,000.00 USD | 17,780,000.00 USD | 0.00 USD | 5,810.00 USD | 14,250.00 USD | 37,140.00 USD |
| `7D` | `65.20` | 17,820,000.00 USD | 17,820,000.00 USD | 0.00 USD | 9,780.00 USD | 1,630.00 USD | 28,280.00 USD |
| `7D` | `65.30` | 17,860,000.00 USD | 17,860,000.00 USD | 0.00 USD | 22,330.00 USD | 5,510.00 USD | 17,890.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `418.28M` | Total OI Tokens: `7,555,439.1 LTC`
  * 1h OI Change: `-0.32%` | 4h OI Change: `-7.13%` | 24h OI Change: `-12.00%`
  * Exchange Breakdown: Binance=`75.77M` | Bybit=`66.18M` | OKX=`33.89M` | Hyperliquid=`21.64M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `5.76K` | Last 24h: `36.85K` | Last 3d: `60.07K` | Last 7d: `106.71K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0033%` | **USDT OKX** | `-0.0029%` |
| **USDT Bybit** | `0.0065%` | **USDT KuCoin** | `0.0062%` |
| **USDT MEXC** | `0.0032%` | **USDT BingX** | `0.0087%` |
| **USDT Gate** | `0.0027%` | **USDT Bitget** | `0.0086%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `52.42%` | `47.58%` | `1.10` | 2,900,000.00 USD |
| `15M` | `Binance` | `48.31%` | `51.69%` | `0.93` | 925,240.00 USD |
| `15M` | `OKX` | `55.96%` | `44.04%` | `1.27` | 315,950.00 USD |
| `15M` | `Bybit` | `55.68%` | `44.32%` | `1.26` | 228,220.00 USD |
| `15M` | `KuCoin` | `52.79%` | `47.21%` | `1.12` | 168,050.00 USD |
| `15M` | `Gate` | `47.96%` | `52.04%` | `0.92` | 29,500.00 USD |
| `15M` | `Bitget` | `37.05%` | `62.95%` | `0.59` | 34,010.00 USD |
| `15M` | `BingX` | `45.98%` | `54.02%` | `0.85` | 128,310.00 USD |
| `15M` | `MEXC` | `46.61%` | `53.39%` | `0.87` | 266,110.00 USD |
| `15M` | `Bitunix` | `50.36%` | `49.64%` | `1.01` | 58,090.00 USD |
| `15M` | `Hyperliquid` | `14.01%` | `85.99%` | `0.16` | 208,080.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.33%` | `49.67%` | `1.01` | 246,720.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `99.06%` | `0.94%` | `105.38` | 292,820.00 USD |
| `15M` | `HTX` | `47.01%` | `52.99%` | `0.89` | 520.89 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `6.05%` | `93.95%` | `0.06` | 510.96 USD |
| `15M` | `Aster` | `6.4%` | `93.6%` | `0.07` | 2,450.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `48.31%` | `51.69%` | `0.93` | 925,240.00 USD |
| `15M` | `Global Accounts` | `52.42%` | `47.58%` | `1.10` | 2,900,000.00 USD |
| `1H` | `LTC` | `54.40%` | `45.60%` | `1.19` | 12,170,000.00 USD |
| `1H` | `Binance` | `53.57%` | `46.43%` | `1.15` | 3,860,000.00 USD |
| `1H` | `OKX` | `51.99%` | `48.01%` | `1.08` | 1,240,000.00 USD |
| `1H` | `Bybit` | `53.43%` | `46.57%` | `1.15` | 1,000,000.00 USD |
| `1H` | `KuCoin` | `48.37%` | `51.63%` | `0.94` | 612,240.00 USD |
| `1H` | `Gate` | `46.61%` | `53.39%` | `0.87` | 1,010,000.00 USD |
| `1H` | `Bitget` | `34.24%` | `65.76%` | `0.52` | 194,980.00 USD |
| `1H` | `BingX` | `49.6%` | `50.4%` | `0.98` | 483,680.00 USD |
| `1H` | `MEXC` | `48.69%` | `51.31%` | `0.95` | 912,570.00 USD |
| `1H` | `Bitunix` | `58.9%` | `41.1%` | `1.43` | 274,430.00 USD |
| `1H` | `Hyperliquid` | `20.13%` | `79.87%` | `0.25` | 288,580.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.14%` | `50.86%` | `0.97` | 1,020,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `93.94%` | `6.06%` | `15.50` | 1,140,000.00 USD |
| `1H` | `HTX` | `37.29%` | `62.71%` | `0.59` | 4,180.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `48.45%` | `51.55%` | `0.94` | 112,670.00 USD |
| `1H` | `Aster` | `37.54%` | `62.46%` | `0.60` | 12,630.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `53.57%` | `46.43%` | `1.15` | 3,860,000.00 USD |
| `1H` | `Global Accounts` | `54.40%` | `45.60%` | `1.19` | 12,170,000.00 USD |
| `4H` | `LTC` | `48.07%` | `51.93%` | `0.93` | 755,660,000.00 USD |
| `4H` | `Binance` | `48%` | `52%` | `0.92` | 299,010,000.00 USD |
| `4H` | `OKX` | `48.87%` | `51.13%` | `0.96` | 88,310,000.00 USD |
| `4H` | `Bybit` | `49.98%` | `50.02%` | `1.00` | 101,140,000.00 USD |
| `4H` | `KuCoin` | `49.87%` | `50.13%` | `0.99` | 5,520,000.00 USD |
| `4H` | `Gate` | `47.78%` | `52.22%` | `0.91` | 10,470,000.00 USD |
| `4H` | `Bitget` | `46.53%` | `53.47%` | `0.87` | 30,680,000.00 USD |
| `4H` | `BingX` | `44.54%` | `55.46%` | `0.80` | 32,670,000.00 USD |
| `4H` | `MEXC` | `47.73%` | `52.27%` | `0.91` | 43,630,000.00 USD |
| `4H` | `Bitunix` | `50.34%` | `49.66%` | `1.01` | 18,080,000.00 USD |
| `4H` | `Hyperliquid` | `43.95%` | `56.05%` | `0.78` | 85,680,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.69%` | `49.31%` | `1.03` | 5,070,000.00 USD |
| `4H` | `Crypto.com` | `51.01%` | `48.99%` | `1.04` | 49,600.00 USD |
| `4H` | `WhiteBIT` | `64.47%` | `35.53%` | `1.81` | 14,010,000.00 USD |
| `4H` | `HTX` | `46.5%` | `53.5%` | `0.87` | 996,910.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `48.82%` | `51.18%` | `0.95` | 13,680,000.00 USD |
| `4H` | `Aster` | `51.65%` | `48.35%` | `1.07` | 2,400,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `43.6%` | `56.4%` | `0.77` | 4,290,000.00 USD |
| `4H` | `Whale Positions` | `48%` | `52%` | `0.92` | 299,010,000.00 USD |
| `4H` | `Global Accounts` | `48.07%` | `51.93%` | `0.93` | 755,660,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `55.00` | `54.96` | `55.00` | `55.59` | `54.17` | 11,110,862.71 USD | 4,658,705.25 USD | 6,452,157.46 USD | -1,793,452.21 USD | `-16.14%` | `3B / 23S` |
| `0:00 UTC` | `55.38` | `55.12` | `55.38` | `55.47` | `54.53` | 4,979,082.77 USD | 3,102,786.44 USD | 1,876,296.33 USD | 1,226,490.12 USD | `+24.63%` | `16B / 3S` |
| `5:00 UTC` | `55.59` | `55.69` | `55.59` | `56.05` | `55.36` | 3,537,942.18 USD | 1,760,395.33 USD | 1,777,546.85 USD | -17,151.52 USD | `-0.48%` | `7B / 9S` |
| `0:00 UTC` | `55.81` | `55.87` | `55.81` | `56.11` | `55.47` | 1,595,751.03 USD | 493,401.32 USD | 1,102,349.71 USD | -608,948.39 USD | `-38.16%` | `2B / 24S` |
| `5:00 UTC` | `55.47` | `55.42` | `55.47` | `55.61` | `55.22` | 1,153,425.44 USD | 492,176.46 USD | 661,248.98 USD | -169,072.53 USD | `-14.66%` | `1B / 7S` |
| `0:00 UTC` | `55.25` | `55.13` | `55.25` | `55.55` | `54.80` | 1,975,627.97 USD | 1,071,271.32 USD | 904,356.64 USD | 166,914.68 USD | `+8.45%` | `21B / 8S` |
| `5:00 UTC` | `55.64` | `55.52` | `55.64` | `55.80` | `55.11` | 1,258,609.21 USD | 696,271.74 USD | 562,337.48 USD | 133,934.26 USD | `+10.64%` | `12B / 7S` |
| `0:00 UTC` | `55.55` | `55.67` | `55.55` | `55.86` | `55.48` | 931,905.62 USD | 470,093.35 USD | 461,812.27 USD | 8,281.08 USD | `+0.89%` | `3B / 4S` |
| `5:00 UTC` | `55.50` | `55.49` | `55.50` | `55.67` | `55.34` | 914,407.56 USD | 383,927.32 USD | 530,480.25 USD | -146,552.93 USD | `-16.03%` | `1B / 5S` |
| `0:00 UTC` | `55.28` | `55.35` | `55.28` | `55.52` | `55.25` | 211,782.89 USD | 81,831.42 USD | 129,951.47 USD | -48,120.04 USD | `-22.72%` | `4B / 8S` |

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
| `5m` | 1,200.00 USD | -90,580.00 USD | **`DISTRIBUTION`** |
| `15m` | 42,950.00 USD | -153,970.00 USD | **`DISTRIBUTION`** |
| `30m` | 320,000.00 USD | -302,620.00 USD | **`ACCUMULATION`** |
| `1h` | 513,250.00 USD | 421,420.00 USD | **`ACCUMULATION`** |
| `2h` | 1,060,000.00 USD | 1,860,000.00 USD | **`ACCUMULATION`** |
| `4h` | -1,400,000.00 USD | -2,930,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,170,000.00 USD | -3,130,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -193,930.00 USD | -2,920,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 663,020.00 USD | -768,020.00 USD | **`DISTRIBUTION`** |
| `24h` | 691,860.00 USD | -4,920,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 3,960,000.00 USD | -24,350,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -21,540,000.00 USD | -190,830,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+1.20K` | 15m=`+42.95K` | 1h=`+513.25K` | 24h=`+691.86K`
* Futures Capital Netflows: 5m=`-90.58K` | 15m=`-153.97K` | 1h=`+421.42K` | 24h=`-4.92M`
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
  * `2026-10-30 04:14:42 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:42 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `55.03` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `53.38` (Risk Distance: `1.65` pts)
  * +2.5R Take Profit: `59.16`
  * Mathematical Lot Sizing: **`6.06 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `55.60` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `57.25` (Risk Distance: `1.65` pts)
  * +2.5R Take Profit: `51.47`
  * Mathematical Lot Sizing: **`6.06 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`55.57`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
