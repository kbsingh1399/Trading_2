# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-29 23:37:48 IST` (`2026-10-29 18:07:48 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `57.64` | **Live Ask Quote**: `57.94` | **Mid Price**: `57.79`
- **Spread Points**: `300.00` | **Spread BPS**: `51.91 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `57.84` | VWAP Z-Score: `-0.49` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.3393` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `42.44` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `59.69` | Lower -3.00σ Band: `55.99`
  * Upper +2.51σ Band: `59.39` | Lower -2.51σ Band: `56.29`
  * Upper +2.01σ Band: `59.08` | Lower -2.01σ Band: `56.60`
  * Upper +2.00σ Band: `59.08` | Lower -2.00σ Band: `56.61`
  * Upper +1.28σ Band: `58.63` | Lower -1.28σ Band: `57.05`
  * Upper +1.00σ Band: `58.46` | Lower -1.00σ Band: `57.22`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`57.96` | EMA-20=`57.95` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`57.84` (Slope: `+0.0000`) | EMA-100=`57.79`
  * Institutional Anchors: EMA-144=`57.69` | EMA-200=`57.48` (Slope: `+0.1470`) | EMA-233=`57.29`
- **Range Boundaries**: 24H High=`59.62` | 24H Low=`56.67` | Weekly High=`59.62` | Weekly Low=`55.48`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `58.52` (Distance: `-1.16%`)
  * Point of Control (POC) = `57.84` (Distance: `+0.01%`)
  * Value Area Low (VAL) = `56.98` (Distance: `+1.50%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.44` | POC=`57.22` | VAL=`56.70`
  * Prior Day Extremes: PDH=`59.62` | PDL=`56.37` | PDC=`58.69`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`57.76` | Weekly POC=`56.49` | Weekly VAL=`55.97`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`59.52` | Low=`56.73`
  * London Session (08:00-16:00 UTC): High=`58.12` | Low=`56.67`
  * New York Session (13:00-21:00 UTC): High=`58.72` | Low=`57.04`
  * Initial Balance (First Hour): IB High=`58.02` | IB Low=`57.29`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `57.56` - `58.02`
  * Optimal Trade Entry (OTE 0.705): `57.91`
  * Structural Invalidation Anchor (0.786): `58.25`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `57.59` | `57.73` | `57.54` | `57.71` | `3,090` | 178,127.35 USD | 77,032.52 USD | `+43.25%` | -1,459,070.25 USD | `+1.12` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `57.72` | `57.79` | `57.67` | `57.78` | `7,737` | 446,616.79 USD | -30,698.65 USD | `-6.87%` | -1,489,768.90 USD | `-0.09` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `57.78` | `57.84` | `57.76` | `57.82` | `842` | 48,678.28 USD | 28,757.98 USD | `+59.08%` | -1,461,010.93 USD | `+0.58` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `58.23` | `58.36` | `57.83` | `57.87` | `10,701` | 621,283.45 USD | -60,604.43 USD | `-9.75%` | -1,221,426.98 USD | `-0.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `57.87` | `57.90` | `57.50` | `57.71` | `20,606` | 1,187,641.81 USD | -229,794.02 USD | `-19.35%` | -1,451,221.01 USD | `-1.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `57.72` | `57.84` | `57.67` | `57.82` | `8,580` | 495,295.07 USD | -1,940.67 USD | `-0.39%` | -1,453,161.68 USD | `+0.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `58.63` | `58.93` | `58.31` | `58.43` | `105,448` | 6,183,662.04 USD | 224,464.05 USD | `+3.63%` | -674,901.06 USD | `+0.70` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `58.44` | `58.44` | `57.50` | `57.71` | `54,276` | 3,147,173.69 USD | -410,603.26 USD | `-13.05%` | -1,085,504.31 USD | `-0.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `57.72` | `57.84` | `57.67` | `57.82` | `8,580` | 495,295.07 USD | -1,940.67 USD | `-0.39%` | -1,087,444.99 USD | `+0.14` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `57.04` | `58.16` | `56.85` | `58.00` | `178,996` | 10,300,529.12 USD | 452,809.17 USD | `+4.40%` | -1,290,330.89 USD | `+1.24` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | -1,041,745.33 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.50` | `57.82` | `168,304` | 9,826,130.80 USD | -188,079.88 USD | `-1.91%` | -1,229,825.21 USD | `+0.03` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `59.19` | `59.70` | `56.95` | `57.21` | `387,394` | 22,568,170.72 USD | -1,232,294.71 USD | `-5.46%` | -1,242,932.23 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `57.20` | `58.23` | `56.92` | `57.04` | `229,127` | 13,178,164.26 USD | -500,207.83 USD | `-3.80%` | -1,743,140.06 USD | `+0.16` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `57.04` | `58.16` | `56.85` | `58.00` | `178,996` | 10,300,529.12 USD | 452,809.17 USD | `+4.40%` | -1,290,330.89 USD | `+1.24` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | -1,041,745.33 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.50` | `57.82` | `168,304` | 9,826,130.80 USD | -188,079.88 USD | `-1.91%` | -1,229,825.21 USD | `+0.03` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`57.79`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:36:01 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1062` | `0xeadc...9d55` | `LONG` | 2,111,033.50 USD | `36,463.77` | `52.78` | `57.87` | `0.000000` | 186,357.55 USD | `+8.83%` | `10X Cross` |
| `1074` | `0x9aa5...58af` | `SHORT` | 2,093,962.38 USD | `36,177.65` | `71.22` | `57.87` | `257.99` | 482,524.28 USD | `+23.04%` | `10X Cross` |
| `2011` | `0xcac1...26b3` | `SHORT` | 1,008,041.69 USD | `17,411.55` | `49.01` | `57.87` | `493.72` | -154,636.37 USD | `-15.34%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `57.00` | 7,510.28 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 57.0040 USD [API] | `2026-10-27 21:51:50` |
| `ANNOUNCEMENT` | `INFO` | `57.03` | 6,666.57 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 6.67K USD at 57.0280 USD [API] | `2026-10-27 22:17:57` |
| `ANNOUNCEMENT` | `INFO` | `56.91` | 6,835.37 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 6.84K USD at 56.9140 USD [API] | `2026-10-27 22:43:37` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`59.03` (Vol: 256,600.00 USD, Dist: `+2.16%`) | Long MP=`56.68` (Vol: 327,300.00 USD, Dist: `--1.90%`)
  * 48H Horizon: Short MP=`59.03` (Vol: 286,000.00 USD, Dist: `+2.16%`) | Long MP=`56.69` (Vol: 302,600.00 USD, Dist: `--1.89%`)
  * 3D Horizon: Short MP=`59.01` (Vol: 285,100.00 USD, Dist: `+2.12%`) | Long MP=`56.70` (Vol: 302,600.00 USD, Dist: `--1.88%`)
  * 7D Horizon: Short MP=`59.04` (Vol: 256,600.00 USD, Dist: `+2.17%`) | Long MP=`55.27` (Vol: 344,500.00 USD, Dist: `--4.35%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `12.25` | 122.50 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.75` | 2,560.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.05` | 2,200.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.65` | 150.15 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.95` | 446.40 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `14.45` | 4,260.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `15.15` | 589.64 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `15.45` | 3,010.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `15.65` | 1,880.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `17.35` | 1,040.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.95` | 5,690.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.05` | 3,470.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.45` | 2,010.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.95` | 4,490.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.45` | 566.67 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.15` | 341.15 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.35` | 491.90 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.45` | 19,950.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.55` | 127.36 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.75` | 194.75 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.05` | 421.36 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 277,980.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 173.39 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 51,610.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 374.20 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.25` | 205.54 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.95` | 5,490.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.05` | 966.50 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 272.75 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 173.85 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.15` | 3,490.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.45` | 4,100.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.55` | 2,270.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 583.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.55` | 108.74 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.65` | 3,870.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 298,340.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 218.46 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 305.50 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 538.53 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 27,620.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 5,680.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 7,070.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 125.24 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 1,450.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.45` | 166.47 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 653.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 953.68 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 32,850.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.15` | 5,780.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.25` | 249.38 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 658.87 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 182.85 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 126.70 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 4,140.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 17,580.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 462.66 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.15` | 4,650.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 3,020.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 423.18 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.65` | 8,060.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 101.80 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.95` | 608.57 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 359.76 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 438.74 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 9,260.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 3,530.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 976.97 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 6,210.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 446.67 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.05` | 7,570.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 341.70 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 287.61 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 4,880.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 384.57 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.75` | 148.80 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 4,840.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 664,760.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 570.02 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 865.53 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 162.95 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 6,890.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 1,550.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 133.10 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 2,160.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.15` | 33,680.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 1,010.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 133.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 274.39 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 6,340.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 509.01 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 396.54 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 18,010.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 644.96 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.65` | 416.50 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 3,090.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 65,900.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 35,410.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 1,570.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.75` | 26,780.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 5,800.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 7,120.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 10,250.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 120,820.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 312.26 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 5,390.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 706.06 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 426.02 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 801.14 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 1,850.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 2,380.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 12,190.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 84,440.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 11,950.00 USD | 938,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 12,490.00 USD | 926,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 134.55 USD | 913,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 2,620.00 USD | 913,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 329.32 USD | 910,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 135.00 USD | 910,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 3,830.00 USD | 910,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 1,780.00 USD | 906,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 23,940.00 USD | 904,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 318.39 USD | 880,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 704.87 USD | 880,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 9,710.00 USD | 879,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.25` | 39,320.00 USD | 870,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.35` | 383.78 USD | 830,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 936.73 USD | 830,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 358.40 USD | 829,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 158.22 USD | 829,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 49,130.00 USD | 829,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 574.09 USD | 779,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.35` | 2,600.00 USD | 779,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.45` | 2,180.00 USD | 776,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 1,770.00 USD | 774,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.65` | 6,850.00 USD | 772,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 4,780.00 USD | 765,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.85` | 975.66 USD | 761,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.95` | 1,440.00 USD | 760,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 1,860.00 USD | 758,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 2,680.00 USD | 756,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 4,390.00 USD | 754,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 2,030.00 USD | 749,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 273.90 USD | 747,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 231.56 USD | 747,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 1,390.00 USD | 747,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,580.00 USD | 745,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,740.00 USD | 744,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.35` | 5,230.00 USD | 738,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.45` | 1,960.00 USD | 733,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.55` | 18,010.00 USD | 731,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.65` | 4,890.00 USD | 713,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.75` | 1,250.00 USD | 708,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.85` | 18,920.00 USD | 707,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.95` | 28,540.00 USD | 688,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.05` | 1,820.00 USD | 659,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.25` | 102.51 USD | 657,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.35` | 1,030.00 USD | 657,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,720.00 USD | 656,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.55` | 103,540.00 USD | 652,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.65` | 25,330.00 USD | 548,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.75` | 9,050.00 USD | 523,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.95` | 245.07 USD | 514,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.05` | 550.32 USD | 513,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.10` | 19,100,000.00 USD | 19,100,000.00 USD | 114,000.00 USD | 49,240.00 USD | 98,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.15` | 219,370.00 USD | 513,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.20` | 18,840,000.00 USD | 18,840,000.00 USD | 25,820.00 USD | 7,100.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.30` | 18,780,000.00 USD | 18,780,000.00 USD | 17,810.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.40` | 18,700,000.00 USD | 18,700,000.00 USD | 69,290.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.45` | 22,090.00 USD | 294,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.50` | 18,560,000.00 USD | 18,560,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.55` | 551.07 USD | 271,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.60` | 18,470,000.00 USD | 18,470,000.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.65` | 155.47 USD | 271,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.70` | 6,240,000.00 USD | 6,240,000.00 USD | 10,880.00 USD | 11,120.00 USD | 11,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.70` | 18,400,000.00 USD | 18,400,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.75` | 6,450.00 USD | 271,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.80` | 6,210,000.00 USD | 6,210,000.00 USD | 6,440.00 USD | 1,820.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.80` | 18,370,000.00 USD | 18,370,000.00 USD | 22,510.00 USD | 12,820.00 USD | 19,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.85` | 3,580.00 USD | 264,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.90` | 6,190,000.00 USD | 6,190,000.00 USD | 10,280.00 USD | 20,560.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.90` | 18,310,000.00 USD | 18,310,000.00 USD | 5,870.00 USD | 15,810.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.95` | 12,070.00 USD | 261,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.00` | 6,150,000.00 USD | 6,150,000.00 USD | 23,100.00 USD | 7,230.00 USD | 21,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.00` | 18,280,000.00 USD | 18,280,000.00 USD | 64,300.00 USD | 17,390.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.10` | 6,100,000.00 USD | 6,100,000.00 USD | 27,410.00 USD | 6,070.00 USD | 30,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 18,190,000.00 USD | 18,190,000.00 USD | 24,220.00 USD | 18,810.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.20` | 6,030,000.00 USD | 6,030,000.00 USD | 23,560.00 USD | 10,410.00 USD | 14,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 18,130,000.00 USD | 18,130,000.00 USD | 35,740.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.30` | 5,990,000.00 USD | 5,990,000.00 USD | 34,020.00 USD | 12,920.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 18,060,000.00 USD | 18,060,000.00 USD | 14,070.00 USD | 12,840.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.35` | 1,470.00 USD | 249,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.40` | 5,920,000.00 USD | 5,920,000.00 USD | 7,880.00 USD | 10,970.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 18,030,000.00 USD | 18,030,000.00 USD | 20,580.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.45` | 3,620.00 USD | 247,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.50` | 5,900,000.00 USD | 5,900,000.00 USD | 13,740.00 USD | 7,370.00 USD | 158.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.50` | 17,970,000.00 USD | 17,970,000.00 USD | 33,240.00 USD | 667.05 USD | 10,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.55` | 8,700.00 USD | 244,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.60` | 5,880,000.00 USD | 5,880,000.00 USD | 2,760.00 USD | 13,230.00 USD | 6,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.60` | 17,930,000.00 USD | 17,930,000.00 USD | 36,640.00 USD | 14,530.00 USD | 584.77 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.70` | 5,850,000.00 USD | 5,850,000.00 USD | 18,580.00 USD | 8,600.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.70` | 17,880,000.00 USD | 17,880,000.00 USD | 20,660.00 USD | 27,720.00 USD | 42,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.75` | 7,450.00 USD | 235,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.80` | 5,800,000.00 USD | 5,800,000.00 USD | 18,390.00 USD | 2,680.00 USD | 11,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.80` | 17,790,000.00 USD | 17,790,000.00 USD | 47,130.00 USD | 17,020.00 USD | 108.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.85` | 5,950.00 USD | 227,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.90` | 5,770,000.00 USD | 5,770,000.00 USD | 28,470.00 USD | 2,430.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.90` | 17,720,000.00 USD | 17,720,000.00 USD | 51,920.00 USD | 23,030.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.95` | 11,500.00 USD | 221,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.00` | 5,730,000.00 USD | 5,730,000.00 USD | 3,880.00 USD | 2,200.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.00` | 17,640,000.00 USD | 17,640,000.00 USD | 19,580.00 USD | 8,880.00 USD | 32,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.05` | 900.26 USD | 210,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.10` | 5,730,000.00 USD | 5,730,000.00 USD | 9,600.00 USD | 2,780.00 USD | 882.41 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.10` | 17,580,000.00 USD | 17,580,000.00 USD | 51,920.00 USD | 29,200.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.15` | 23,340.00 USD | 209,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.20` | 5,710,000.00 USD | 5,710,000.00 USD | 11,160.00 USD | 8,090.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.20` | 17,490,000.00 USD | 17,490,000.00 USD | 90,340.00 USD | 17,580.00 USD | 25,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.25` | 1,500.00 USD | 186,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.30` | 5,690,000.00 USD | 5,690,000.00 USD | 10,170.00 USD | 4,410.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.30` | 17,360,000.00 USD | 17,360,000.00 USD | 63,050.00 USD | 14,250.00 USD | 37,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.35` | 1,910.00 USD | 184,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.40` | 5,660,000.00 USD | 5,660,000.00 USD | 24,480.00 USD | 4,490.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.40` | 17,240,000.00 USD | 17,240,000.00 USD | 49,250.00 USD | 4,350.00 USD | 48,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.45` | 4,880.00 USD | 182,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.50` | 5,620,000.00 USD | 5,620,000.00 USD | 9,130.00 USD | 2,350.00 USD | 83.29 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.50` | 17,140,000.00 USD | 17,140,000.00 USD | 50,210.00 USD | 13,810.00 USD | 22,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.60` | 5,610,000.00 USD | 5,610,000.00 USD | 19,360.00 USD | 5,030.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.60` | 17,060,000.00 USD | 17,060,000.00 USD | 51,280.00 USD | 8,450.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.65` | 533.82 USD | 177,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.70` | 5,570,000.00 USD | 5,570,000.00 USD | 4,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.70` | 16,980,000.00 USD | 16,980,000.00 USD | 64,150.00 USD | 15,090.00 USD | 12,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.75` | 148.35 USD | 177,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.80` | 5,570,000.00 USD | 5,570,000.00 USD | 1,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.80` | 16,890,000.00 USD | 16,890,000.00 USD | 99,150.00 USD | 48,300.00 USD | 86,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.85` | 2,130.00 USD | 177,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.90` | 5,570,000.00 USD | 5,570,000.00 USD | 6,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.90` | 16,660,000.00 USD | 16,660,000.00 USD | 111,970.00 USD | 25,310.00 USD | 123,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.95` | 28,950.00 USD | 175,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.00` | 5,560,000.00 USD | 5,560,000.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.00` | 16,400,000.00 USD | 16,400,000.00 USD | 344,710.00 USD | 142,130.00 USD | 210,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.05` | 19,340.00 USD | 146,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.10` | 5,560,000.00 USD | 5,560,000.00 USD | 11,440.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.10` | 15,700,000.00 USD | 15,700,000.00 USD | 232,410.00 USD | 45,470.00 USD | 138,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.15` | 13,030.00 USD | 126,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.20` | 5,550,000.00 USD | 5,550,000.00 USD | 15,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.20` | 15,290,000.00 USD | 15,290,000.00 USD | 234,980.00 USD | 141,240.00 USD | 133,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.25` | 3,260.00 USD | 113,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.30` | 5,530,000.00 USD | 5,530,000.00 USD | 4,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.30` | 14,780,000.00 USD | 14,780,000.00 USD | 245,850.00 USD | 89,080.00 USD | 257,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.40` | 5,530,000.00 USD | 5,530,000.00 USD | 2,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.40` | 14,180,000.00 USD | 14,180,000.00 USD | 319,640.00 USD | 106,460.00 USD | 105,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.45` | 14,120.00 USD | 110,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.50` | 5,520,000.00 USD | 5,520,000.00 USD | 2,500.00 USD | 126.10 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.50` | 13,650,000.00 USD | 13,650,000.00 USD | 169,910.00 USD | 53,460.00 USD | 142,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.55` | 1,060.00 USD | 96,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.60` | 5,520,000.00 USD | 5,520,000.00 USD | 3,300.00 USD | 601.45 USD | 944.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.60` | 13,290,000.00 USD | 13,290,000.00 USD | 108,280.00 USD | 43,430.00 USD | 73,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.65` | 488.57 USD | 95,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.70` | 5,520,000.00 USD | 5,520,000.00 USD | 51,940.00 USD | 15,810.00 USD | 52,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.70` | 13,060,000.00 USD | 13,060,000.00 USD | 123,210.00 USD | 50,560.00 USD | 172,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.75` | 470.85 USD | 94,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.80` | 5,400,000.00 USD | 5,400,000.00 USD | 47,390.00 USD | 18,410.00 USD | 26,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.80` | 12,710,000.00 USD | 12,710,000.00 USD | 309,200.00 USD | 104,820.00 USD | 156,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.90` | 5,300,000.00 USD | 5,300,000.00 USD | 52,180.00 USD | 21,230.00 USD | 5,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.90` | 12,140,000.00 USD | 12,140,000.00 USD | 257,210.00 USD | 162,220.00 USD | 276,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.95` | 7,160.00 USD | 94,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.00` | 5,220,000.00 USD | 5,220,000.00 USD | 38,800.00 USD | 24,110.00 USD | 12,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.00` | 11,450,000.00 USD | 11,450,000.00 USD | 269,610.00 USD | 81,220.00 USD | 310,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.05` | 1,100.00 USD | 87,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.10` | 5,150,000.00 USD | 5,150,000.00 USD | 26,630.00 USD | 10,460.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.10` | 10,790,000.00 USD | 10,790,000.00 USD | 362,320.00 USD | 145,730.00 USD | 171,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.15` | 3,010.00 USD | 86,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.20` | 5,090,000.00 USD | 5,090,000.00 USD | 19,810.00 USD | 4,030.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.20` | 10,110,000.00 USD | 10,110,000.00 USD | 338,950.00 USD | 177,110.00 USD | 279,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.30` | 5,060,000.00 USD | 5,060,000.00 USD | 12,080.00 USD | 5,120.00 USD | 18,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.30` | 9,310,000.00 USD | 9,310,000.00 USD | 367,680.00 USD | 68,970.00 USD | 256,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.35` | 1,610.00 USD | 83,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.40` | 5,020,000.00 USD | 5,020,000.00 USD | 29,970.00 USD | 57,700.00 USD | 25,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.40` | 8,620,000.00 USD | 8,620,000.00 USD | 302,780.00 USD | 188,590.00 USD | 237,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.45` | 1,090.00 USD | 81,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.50` | 4,910,000.00 USD | 4,910,000.00 USD | 70,830.00 USD | 25,990.00 USD | 61,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.50` | 7,890,000.00 USD | 7,890,000.00 USD | 329,130.00 USD | 178,270.00 USD | 529,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.55` | 1,390.00 USD | 80,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.60` | 4,750,000.00 USD | 4,750,000.00 USD | 97,100.00 USD | 21,410.00 USD | 82,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.60` | 6,850,000.00 USD | 6,850,000.00 USD | 426,340.00 USD | 261,500.00 USD | 243,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.65` | 676.15 USD | 79,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.70` | 4,550,000.00 USD | 4,550,000.00 USD | 90,090.00 USD | 49,390.00 USD | 47,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.70` | 5,920,000.00 USD | 5,920,000.00 USD | 174,240.00 USD | 32,180.00 USD | 273,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.75` | 153.87 USD | 78,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.80` | 4,360,000.00 USD | 4,360,000.00 USD | 120,170.00 USD | 47,920.00 USD | 42,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.80` | 5,440,000.00 USD | 5,440,000.00 USD | 60,840.00 USD | 54,060.00 USD | 144,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.90` | 4,150,000.00 USD | 4,150,000.00 USD | 116,440.00 USD | 62,020.00 USD | 130,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.90` | 5,180,000.00 USD | 5,180,000.00 USD | 65,400.00 USD | 94,580.00 USD | 280,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.00` | 3,840,000.00 USD | 3,840,000.00 USD | 125,000.00 USD | 60,260.00 USD | 56,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.00` | 4,740,000.00 USD | 4,740,000.00 USD | 181,230.00 USD | 88,840.00 USD | 107,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.10` | 3,600,000.00 USD | 3,600,000.00 USD | 98,040.00 USD | 77,440.00 USD | 26,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.10` | 4,360,000.00 USD | 4,360,000.00 USD | 121,920.00 USD | 133,900.00 USD | 46,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `56.15` | 78,230.00 USD | 78,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `56.20` | 3,400,000.00 USD | 3,400,000.00 USD | 73,120.00 USD | 60,830.00 USD | 87,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.20` | 4,060,000.00 USD | 4,060,000.00 USD | 104,510.00 USD | 80,130.00 USD | 205,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.30` | 3,180,000.00 USD | 3,180,000.00 USD | 77,950.00 USD | 44,480.00 USD | 65,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.30` | 3,670,000.00 USD | 3,670,000.00 USD | 91,850.00 USD | 140,830.00 USD | 85,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.40` | 2,990,000.00 USD | 2,990,000.00 USD | 185,180.00 USD | 35,450.00 USD | 122,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.40` | 3,350,000.00 USD | 3,350,000.00 USD | 215,940.00 USD | 124,050.00 USD | 139,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.50` | 2,650,000.00 USD | 2,650,000.00 USD | 69,340.00 USD | 122,360.00 USD | 53,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.50` | 2,870,000.00 USD | 2,870,000.00 USD | 26,520.00 USD | 101,420.00 USD | 47,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.60` | 2,400,000.00 USD | 2,400,000.00 USD | 161,590.00 USD | 60,330.00 USD | 124,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.60` | 2,700,000.00 USD | 2,700,000.00 USD | 363,190.00 USD | 113,010.00 USD | 128,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.70` | 2,060,000.00 USD | 2,060,000.00 USD | 204,190.00 USD | 65,860.00 USD | 190,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.70` | 2,090,000.00 USD | 2,090,000.00 USD | 110,940.00 USD | 105,810.00 USD | 138,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.80` | 1,600,000.00 USD | 1,600,000.00 USD | 189,690.00 USD | 111,830.00 USD | 122,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.80` | 1,740,000.00 USD | 1,740,000.00 USD | 153,580.00 USD | 97,670.00 USD | 262,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.90` | 1,170,000.00 USD | 1,170,000.00 USD | 299,280.00 USD | 94,950.00 USD | 119,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.90` | 1,220,000.00 USD | 1,220,000.00 USD | 108,440.00 USD | 65,260.00 USD | 94,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.00` | 658,180.00 USD | 658,180.00 USD | 34,380.00 USD | 24,060.00 USD | 44,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.00` | 954,870.00 USD | 954,870.00 USD | 50,710.00 USD | 111,780.00 USD | 91,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.10` | 555,030.00 USD | 555,030.00 USD | 73,260.00 USD | 25,570.00 USD | 4,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.10` | 700,980.00 USD | 700,980.00 USD | 36,580.00 USD | 14,880.00 USD | 500.18 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.20` | 451,820.00 USD | 451,820.00 USD | 27,530.00 USD | 40,100.00 USD | 256.90 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.20` | 649,020.00 USD | 649,020.00 USD | 21,160.00 USD | 50,300.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.30` | 383,930.00 USD | 383,930.00 USD | 0.00 USD | 15,520.00 USD | 51,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.30` | 573,870.00 USD | 573,870.00 USD | 22,360.00 USD | 27,320.00 USD | 45,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.40` | 316,500.00 USD | 316,500.00 USD | 19,650.00 USD | 26,470.00 USD | 1,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.40` | 478,660.00 USD | 478,660.00 USD | 38,520.00 USD | 30,000.00 USD | 129,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.50` | 269,040.00 USD | 269,040.00 USD | 80,510.00 USD | 12,870.00 USD | 36,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.50` | 280,200.00 USD | 280,200.00 USD | 76,670.00 USD | 23,070.00 USD | 68,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.60` | 138,820.00 USD | 138,820.00 USD | 138,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.60` | 111,570.00 USD | 111,570.00 USD | 70,040.00 USD | 15,090.00 USD | 26,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.20` | 638.03 USD | 638.03 USD | 0.00 USD | 0.00 USD | 638.03 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.40` | 24,790.00 USD | 24,790.00 USD | 0.00 USD | 0.00 USD | 24,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.40` | 54,120.00 USD | 54,120.00 USD | 0.00 USD | 0.00 USD | 54,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.50` | 94,790.00 USD | 94,790.00 USD | 48,820.00 USD | 20,920.00 USD | 255.20 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.50` | 78,650.00 USD | 78,650.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.70` | 102,850.00 USD | 102,850.00 USD | 0.00 USD | 8,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.70` | 118,400.00 USD | 118,400.00 USD | 0.00 USD | 4,430.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.80` | 125,050.00 USD | 125,050.00 USD | 0.00 USD | 10,240.00 USD | 11,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.80` | 127,280.00 USD | 127,280.00 USD | 0.00 USD | 3,320.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.90` | 291,210.00 USD | 291,210.00 USD | 0.00 USD | 115,410.00 USD | 50,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.90` | 206,140.00 USD | 206,140.00 USD | 0.00 USD | 47,950.00 USD | 30,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.00` | 607,480.00 USD | 607,480.00 USD | 141,660.00 USD | 51,970.00 USD | 122,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.00` | 628,090.00 USD | 628,090.00 USD | 255,180.00 USD | 48,210.00 USD | 118,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.10` | 1,000,000.00 USD | 1,000,000.00 USD | 189,650.00 USD | 41,340.00 USD | 164,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.10` | 854,730.00 USD | 854,730.00 USD | 91,060.00 USD | 45,400.00 USD | 90,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.20` | 1,320,000.00 USD | 1,320,000.00 USD | 149,140.00 USD | 72,500.00 USD | 96,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.20` | 1,190,000.00 USD | 1,190,000.00 USD | 153,580.00 USD | 10,620.00 USD | 174,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.30` | 1,810,000.00 USD | 1,810,000.00 USD | 283,630.00 USD | 73,090.00 USD | 133,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.30` | 1,470,000.00 USD | 1,470,000.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.40` | 2,020,000.00 USD | 2,020,000.00 USD | 78,510.00 USD | 56,810.00 USD | 76,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.40` | 1,780,000.00 USD | 1,780,000.00 USD | 103,370.00 USD | 73,620.00 USD | 137,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.50` | 2,200,000.00 USD | 2,200,000.00 USD | 114,880.00 USD | 51,920.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.50` | 1,920,000.00 USD | 1,920,000.00 USD | 67,060.00 USD | 59,920.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.60` | 2,340,000.00 USD | 2,340,000.00 USD | 62,260.00 USD | 66,510.00 USD | 13,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.60` | 2,420,000.00 USD | 2,420,000.00 USD | 268,680.00 USD | 145,550.00 USD | 86,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.70` | 2,490,000.00 USD | 2,490,000.00 USD | 20,820.00 USD | 35,670.00 USD | 94,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.70` | 2,820,000.00 USD | 2,820,000.00 USD | 53,810.00 USD | 180,620.00 USD | 161,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.80` | 2,710,000.00 USD | 2,710,000.00 USD | 100,280.00 USD | 51,160.00 USD | 68,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.80` | 3,190,000.00 USD | 3,190,000.00 USD | 118,240.00 USD | 96,860.00 USD | 155,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.90` | 2,940,000.00 USD | 2,940,000.00 USD | 113,050.00 USD | 26,580.00 USD | 84,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.90` | 3,570,000.00 USD | 3,570,000.00 USD | 246,770.00 USD | 98,620.00 USD | 39,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.00` | 3,320,000.00 USD | 3,320,000.00 USD | 226,310.00 USD | 70,520.00 USD | 88,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.00` | 4,070,000.00 USD | 4,070,000.00 USD | 231,370.00 USD | 183,130.00 USD | 82,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.10` | 3,530,000.00 USD | 3,530,000.00 USD | 98,470.00 USD | 39,900.00 USD | 66,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.10` | 4,630,000.00 USD | 4,630,000.00 USD | 263,890.00 USD | 122,370.00 USD | 174,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.20` | 3,790,000.00 USD | 3,790,000.00 USD | 136,940.00 USD | 38,140.00 USD | 86,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.20` | 5,090,000.00 USD | 5,090,000.00 USD | 207,990.00 USD | 131,530.00 USD | 123,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.30` | 4,100,000.00 USD | 4,100,000.00 USD | 113,360.00 USD | 95,210.00 USD | 101,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.30` | 5,460,000.00 USD | 5,460,000.00 USD | 118,160.00 USD | 95,890.00 USD | 155,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.40` | 4,430,000.00 USD | 4,430,000.00 USD | 164,430.00 USD | 73,810.00 USD | 92,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.40` | 5,900,000.00 USD | 5,900,000.00 USD | 89,500.00 USD | 126,870.00 USD | 226,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.50` | 4,740,000.00 USD | 4,740,000.00 USD | 147,700.00 USD | 56,930.00 USD | 104,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.50` | 6,360,000.00 USD | 6,360,000.00 USD | 160,180.00 USD | 89,250.00 USD | 207,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.60` | 4,860,000.00 USD | 4,860,000.00 USD | 78,970.00 USD | 40,280.00 USD | 6,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.60` | 6,930,000.00 USD | 6,930,000.00 USD | 294,830.00 USD | 109,510.00 USD | 167,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.70` | 5,050,000.00 USD | 5,050,000.00 USD | 84,870.00 USD | 58,850.00 USD | 48,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.70` | 7,180,000.00 USD | 7,180,000.00 USD | 142,880.00 USD | 79,060.00 USD | 28,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.75` | 1,040.00 USD | 1,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.80` | 5,210,000.00 USD | 5,210,000.00 USD | 45,710.00 USD | 15,720.00 USD | 90,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.80` | 7,410,000.00 USD | 7,410,000.00 USD | 54,870.00 USD | 78,710.00 USD | 94,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.85` | 469.76 USD | 1,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.90` | 5,340,000.00 USD | 5,340,000.00 USD | 72,210.00 USD | 25,460.00 USD | 33,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.90` | 7,700,000.00 USD | 7,700,000.00 USD | 139,720.00 USD | 52,860.00 USD | 92,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.00` | 5,440,000.00 USD | 5,440,000.00 USD | 55,630.00 USD | 10,730.00 USD | 32,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 7,840,000.00 USD | 7,840,000.00 USD | 96,160.00 USD | 43,600.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.10` | 5,440,000.00 USD | 5,440,000.00 USD | 5,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 7,870,000.00 USD | 7,870,000.00 USD | 31,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.15` | 1,180.00 USD | 2,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.20` | 5,580,000.00 USD | 5,580,000.00 USD | 100,130.00 USD | 6,410.00 USD | 31,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.20` | 8,090,000.00 USD | 8,090,000.00 USD | 116,610.00 USD | 70,180.00 USD | 33,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.30` | 5,600,000.00 USD | 5,600,000.00 USD | 13,090.00 USD | 6,960.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.30` | 8,240,000.00 USD | 8,240,000.00 USD | 51,130.00 USD | 36,170.00 USD | 55,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.40` | 5,640,000.00 USD | 5,640,000.00 USD | 23,410.00 USD | 8,360.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.40` | 8,390,000.00 USD | 8,390,000.00 USD | 87,050.00 USD | 41,800.00 USD | 24,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.45` | 267.31 USD | 2,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.50` | 5,710,000.00 USD | 5,710,000.00 USD | 20,390.00 USD | 23,040.00 USD | 26,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.50` | 8,480,000.00 USD | 8,480,000.00 USD | 21,320.00 USD | 34,770.00 USD | 35,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.60` | 5,770,000.00 USD | 5,770,000.00 USD | 25,020.00 USD | 13,550.00 USD | 26,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.60` | 8,730,000.00 USD | 8,730,000.00 USD | 56,380.00 USD | 63,390.00 USD | 132,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.70` | 5,900,000.00 USD | 5,900,000.00 USD | 70,350.00 USD | 13,270.00 USD | 39,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.70` | 8,960,000.00 USD | 8,960,000.00 USD | 100,140.00 USD | 15,950.00 USD | 114,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.80` | 5,930,000.00 USD | 5,930,000.00 USD | 23,150.00 USD | 8,420.00 USD | 1,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.80` | 9,310,000.00 USD | 9,310,000.00 USD | 185,050.00 USD | 68,030.00 USD | 92,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.90` | 5,990,000.00 USD | 5,990,000.00 USD | 36,420.00 USD | 11,940.00 USD | 16,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.90` | 9,460,000.00 USD | 9,460,000.00 USD | 79,630.00 USD | 35,500.00 USD | 35,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.00` | 6,030,000.00 USD | 6,030,000.00 USD | 22,240.00 USD | 1,560.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.00` | 9,580,000.00 USD | 9,580,000.00 USD | 57,760.00 USD | 13,260.00 USD | 49,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.10` | 6,050,000.00 USD | 6,050,000.00 USD | 12,050.00 USD | 945.47 USD | 2,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.10` | 9,640,000.00 USD | 9,640,000.00 USD | 36,500.00 USD | 12,820.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.20` | 6,050,000.00 USD | 6,050,000.00 USD | 4,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.20` | 9,760,000.00 USD | 9,760,000.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.30` | 6,050,000.00 USD | 6,050,000.00 USD | 464.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.30` | 9,910,000.00 USD | 9,910,000.00 USD | 38,120.00 USD | 23,450.00 USD | 85,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `62.35` | 213,600.00 USD | 216,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `62.40` | 6,060,000.00 USD | 6,060,000.00 USD | 3,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.40` | 10,050,000.00 USD | 10,050,000.00 USD | 81,060.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.50` | 6,060,000.00 USD | 6,060,000.00 USD | 4,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.50` | 10,130,000.00 USD | 10,130,000.00 USD | 45,440.00 USD | 14,320.00 USD | 26,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.60` | 6,060,000.00 USD | 6,060,000.00 USD | 2,090.00 USD | 0.00 USD | 327.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.60` | 10,200,000.00 USD | 10,200,000.00 USD | 35,940.00 USD | 7,100.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.70` | 6,100,000.00 USD | 6,100,000.00 USD | 17,140.00 USD | 4,920.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.70` | 10,290,000.00 USD | 10,290,000.00 USD | 22,860.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.80` | 6,140,000.00 USD | 6,140,000.00 USD | 16,330.00 USD | 7,010.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.80` | 10,430,000.00 USD | 10,430,000.00 USD | 74,100.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.90` | 6,150,000.00 USD | 6,150,000.00 USD | 8,780.00 USD | 6,670.00 USD | 63.10 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.90` | 10,530,000.00 USD | 10,530,000.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.00` | 6,170,000.00 USD | 6,170,000.00 USD | 7,650.00 USD | 7,040.00 USD | 4,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.00` | 10,590,000.00 USD | 10,590,000.00 USD | 35,710.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.10` | 6,190,000.00 USD | 6,190,000.00 USD | 3,990.00 USD | 4,070.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.10` | 10,630,000.00 USD | 10,630,000.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.20` | 6,190,000.00 USD | 6,190,000.00 USD | 2,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.30` | 6,200,000.00 USD | 6,200,000.00 USD | 4,440.00 USD | 594.25 USD | 2,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.30` | 10,670,000.00 USD | 10,670,000.00 USD | 20,280.00 USD | 11,500.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.40` | 6,210,000.00 USD | 6,210,000.00 USD | 3,520.00 USD | 1,230.00 USD | 7,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.40` | 10,700,000.00 USD | 10,700,000.00 USD | 14,300.00 USD | 1,320.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.50` | 6,250,000.00 USD | 6,250,000.00 USD | 10,280.00 USD | 20,560.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.50` | 10,730,000.00 USD | 10,730,000.00 USD | 6,620.00 USD | 15,810.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.60` | 6,300,000.00 USD | 6,300,000.00 USD | 23,100.00 USD | 7,230.00 USD | 21,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.60` | 10,820,000.00 USD | 10,820,000.00 USD | 63,480.00 USD | 17,390.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.70` | 6,370,000.00 USD | 6,370,000.00 USD | 28,180.00 USD | 6,070.00 USD | 30,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.70` | 10,880,000.00 USD | 10,880,000.00 USD | 21,940.00 USD | 18,810.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.80` | 6,410,000.00 USD | 6,410,000.00 USD | 23,560.00 USD | 10,410.00 USD | 14,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.80` | 10,940,000.00 USD | 10,940,000.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.90` | 6,480,000.00 USD | 6,480,000.00 USD | 34,020.00 USD | 12,920.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.90` | 10,970,000.00 USD | 10,970,000.00 USD | 7,650.00 USD | 12,840.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.00` | 6,500,000.00 USD | 6,500,000.00 USD | 7,880.00 USD | 10,970.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.00` | 11,020,000.00 USD | 11,020,000.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.10` | 6,520,000.00 USD | 6,520,000.00 USD | 13,740.00 USD | 7,370.00 USD | 158.87 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.10` | 11,050,000.00 USD | 11,050,000.00 USD | 20,350.00 USD | 667.05 USD | 10,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.20` | 6,550,000.00 USD | 6,550,000.00 USD | 2,760.00 USD | 13,230.00 USD | 6,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.20` | 11,090,000.00 USD | 11,090,000.00 USD | 28,840.00 USD | 14,530.00 USD | 584.77 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `64.25` | 735.02 USD | 217,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `64.40` | 6,560,000.00 USD | 6,560,000.00 USD | 1,140.00 USD | 1,940.00 USD | 13,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.40` | 11,140,000.00 USD | 11,140,000.00 USD | 2,540.00 USD | 20,590.00 USD | 29,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.50` | 6,600,000.00 USD | 6,600,000.00 USD | 17,440.00 USD | 6,670.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.50` | 11,170,000.00 USD | 11,170,000.00 USD | 8,110.00 USD | 7,120.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.60` | 6,630,000.00 USD | 6,630,000.00 USD | 18,390.00 USD | 2,680.00 USD | 11,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.60` | 11,220,000.00 USD | 11,220,000.00 USD | 32,750.00 USD | 17,020.00 USD | 108.50 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.70` | 6,660,000.00 USD | 6,660,000.00 USD | 28,470.00 USD | 2,430.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.70` | 11,290,000.00 USD | 11,290,000.00 USD | 39,430.00 USD | 23,030.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.80` | 6,670,000.00 USD | 6,670,000.00 USD | 3,880.00 USD | 2,200.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.80` | 11,330,000.00 USD | 11,330,000.00 USD | 8,140.00 USD | 8,210.00 USD | 20,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.90` | 6,680,000.00 USD | 6,680,000.00 USD | 6,320.00 USD | 2,780.00 USD | 669.73 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.90` | 11,370,000.00 USD | 11,370,000.00 USD | 25,750.00 USD | 8,010.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `65.00` | 6,690,000.00 USD | 6,690,000.00 USD | 4,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.00` | 11,390,000.00 USD | 11,390,000.00 USD | 0.00 USD | 9,480.00 USD | 13,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `65.95` | 1,160.00 USD | 218,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.85` | 33,950.00 USD | 252,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.95` | 121.18 USD | 252,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.85` | 709.03 USD | 253,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `69.45` | 414.62 USD | 253,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `70.45` | 6,740.00 USD | 260,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `71.75` | 5,110.00 USD | 265,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `72.35` | 660.56 USD | 266,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `76.35` | 8,380.00 USD | 274,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.85` | 602.56 USD | 275,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.95` | 136.41 USD | 275,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.75` | 646.00 USD | 275,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.05` | 19,000.00 USD | 294,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.55` | 123.96 USD | 295,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.65` | 3,850.00 USD | 298,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.75` | 214.32 USD | 299,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `84.65` | 862.58 USD | 299,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `87.55` | 2,890.00 USD | 302,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `88.05` | 3,520.00 USD | 306,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `89.15` | 23,790.00 USD | 330,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `89.65` | 1,830.00 USD | 332,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `95.05` | 649.19 USD | 332,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `95.55` | 2,390.00 USD | 335,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `97.55` | 1,040.00 USD | 336,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.15` | 20,630.00 USD | 356,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.35` | 20,870.00 USD | 377,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.55` | 352,750.00 USD | 730,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.45` | 131.44 USD | 730,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.55` | 1,120.00 USD | 731,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.65` | 4,830.00 USD | 736,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 333,510.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.65` | 817.14 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.65` | 420.77 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.35` | 763,270.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `12.25` | 2,950,000.00 USD | 0.00 USD | 122.50 USD | `-78.79%` | `10.00` |
| `Live` | `Long` | `12.75` | 2,950,000.00 USD | 0.00 USD | 2,560.00 USD | `-77.93%` | `200.43` |
| `Live` | `Long` | `13.05` | 2,940,000.00 USD | 0.00 USD | 2,200.00 USD | `-77.41%` | `168.79` |
| `Live` | `Long` | `13.25` | 2,940,000.00 USD | 0.00 USD | 681.18 USD | `-77.06%` | `51.41` |
| `Live` | `Long` | `13.65` | 2,940,000.00 USD | 0.00 USD | 150.15 USD | `-76.37%` | `11.00` |
| `Live` | `Long` | `14.15` | 2,940,000.00 USD | 0.00 USD | 4,170.00 USD | `-75.50%` | `294.67` |
| `Live` | `Long` | `14.85` | 2,940,000.00 USD | 0.00 USD | 419.81 USD | `-74.29%` | `28.27` |
| `Live` | `Long` | `15.25` | 2,940,000.00 USD | 0.00 USD | 305.00 USD | `-73.60%` | `20.00` |
| `Live` | `Long` | `15.95` | 2,940,000.00 USD | 0.00 USD | 1,910.00 USD | `-72.39%` | `120.00` |
| `Live` | `Long` | `16.65` | 2,930,000.00 USD | 0.00 USD | 3,250.00 USD | `-71.18%` | `195.03` |
| `Live` | `Long` | `17.95` | 2,930,000.00 USD | 0.00 USD | 698.61 USD | `-68.92%` | `38.92` |
| `Live` | `Long` | `18.95` | 2,930,000.00 USD | 0.00 USD | 1,140.00 USD | `-67.19%` | `60.00` |
| `Live` | `Long` | `19.05` | 2,930,000.00 USD | 0.00 USD | 3,470.00 USD | `-67.02%` | `182.00` |
| `Live` | `Long` | `19.25` | 2,930,000.00 USD | 0.00 USD | 192.50 USD | `-66.67%` | `10.00` |
| `Live` | `Long` | `19.45` | 2,930,000.00 USD | 0.00 USD | 2,010.00 USD | `-66.33%` | `103.47` |
| `Live` | `Long` | `21.45` | 2,920,000.00 USD | 0.00 USD | 345.99 USD | `-62.87%` | `16.13` |
| `Live` | `Long` | `21.85` | 2,920,000.00 USD | 0.00 USD | 4,920.00 USD | `-62.17%` | `225.00` |
| `Live` | `Long` | `22.25` | 2,920,000.00 USD | 0.00 USD | 131.50 USD | `-61.48%` | `5.91` |
| `Live` | `Long` | `22.75` | 2,920,000.00 USD | 0.00 USD | 21,160.00 USD | `-60.61%` | `930.00` |
| `Live` | `Long` | `23.75` | 2,900,000.00 USD | 0.00 USD | 194.75 USD | `-58.88%` | `8.20` |
| `Live` | `Long` | `24.05` | 2,900,000.00 USD | 0.00 USD | 421.36 USD | `-58.36%` | `17.52` |
| `Live` | `Long` | `24.15` | 2,900,000.00 USD | 0.00 USD | 669.20 USD | `-58.19%` | `27.71` |
| `Live` | `Long` | `25.25` | 2,900,000.00 USD | 0.00 USD | 277,980.00 USD | `-56.29%` | `11,009.19` |
| `Live` | `Long` | `25.35` | 2,620,000.00 USD | 0.00 USD | 173.39 USD | `-56.11%` | `6.84` |
| `Live` | `Long` | `25.55` | 2,620,000.00 USD | 0.00 USD | 50,740.00 USD | `-55.77%` | `1,985.99` |
| `Live` | `Long` | `25.95` | 2,570,000.00 USD | 0.00 USD | 8,160.00 USD | `-55.08%` | `314.42` |
| `Live` | `Long` | `26.95` | 2,560,000.00 USD | 0.00 USD | 5,490.00 USD | `-53.34%` | `203.85` |
| `Live` | `Long` | `27.35` | 2,550,000.00 USD | 0.00 USD | 1,170.00 USD | `-52.65%` | `42.95` |
| `Live` | `Long` | `27.55` | 2,550,000.00 USD | 0.00 USD | 272.75 USD | `-52.31%` | `9.90` |
| `Live` | `Long` | `27.75` | 2,550,000.00 USD | 0.00 USD | 439.00 USD | `-51.96%` | `15.82` |
| `Live` | `Long` | `27.95` | 2,550,000.00 USD | 0.00 USD | 173.85 USD | `-51.61%` | `6.22` |
| `Live` | `Long` | `28.05` | 2,550,000.00 USD | 0.00 USD | 219.63 USD | `-51.44%` | `7.83` |
| `Live` | `Long` | `28.15` | 2,550,000.00 USD | 0.00 USD | 955.41 USD | `-51.27%` | `33.94` |
| `Live` | `Long` | `28.45` | 2,550,000.00 USD | 0.00 USD | 4,100.00 USD | `-50.75%` | `144.17` |
| `Live` | `Long` | `28.85` | 2,550,000.00 USD | 0.00 USD | 3,580.00 USD | `-50.05%` | `124.01` |
| `Live` | `Long` | `29.15` | 2,540,000.00 USD | 0.00 USD | 583.00 USD | `-49.54%` | `20.00` |
| `Live` | `Long` | `29.35` | 2,540,000.00 USD | 0.00 USD | 101.55 USD | `-49.19%` | `3.46` |
| `Live` | `Long` | `29.55` | 2,540,000.00 USD | 0.00 USD | 108.74 USD | `-48.84%` | `3.68` |
| `Live` | `Long` | `29.75` | 2,540,000.00 USD | 0.00 USD | 297,600.00 USD | `-48.50%` | `10,003.44` |
| `Live` | `Long` | `30.05` | 2,240,000.00 USD | 0.00 USD | 218.46 USD | `-47.98%` | `7.27` |
| `Live` | `Long` | `30.55` | 2,240,000.00 USD | 0.00 USD | 305.50 USD | `-47.11%` | `10.00` |
| `Live` | `Long` | `30.75` | 2,240,000.00 USD | 0.00 USD | 4,020.00 USD | `-46.77%` | `130.63` |
| `Live` | `Long` | `30.95` | 2,240,000.00 USD | 0.00 USD | 3,000.00 USD | `-46.42%` | `96.89` |
| `Live` | `Long` | `31.15` | 2,240,000.00 USD | 0.00 USD | 27,620.00 USD | `-46.07%` | `886.80` |
| `Live` | `Long` | `31.55` | 2,210,000.00 USD | 0.00 USD | 5,680.00 USD | `-45.38%` | `180.02` |
| `Live` | `Long` | `31.65` | 2,200,000.00 USD | 0.00 USD | 789.03 USD | `-45.21%` | `24.93` |
| `Live` | `Long` | `31.85` | 2,200,000.00 USD | 0.00 USD | 2,870.00 USD | `-44.86%` | `90.00` |
| `Live` | `Long` | `31.95` | 2,200,000.00 USD | 0.00 USD | 125.24 USD | `-44.69%` | `3.92` |
| `Live` | `Long` | `32.15` | 2,200,000.00 USD | 0.00 USD | 1,830.00 USD | `-44.34%` | `56.93` |
| `Live` | `Long` | `32.45` | 2,200,000.00 USD | 0.00 USD | 166.47 USD | `-43.82%` | `5.13` |
| `Live` | `Long` | `32.65` | 2,200,000.00 USD | 0.00 USD | 653.00 USD | `-43.48%` | `20.00` |
| `Live` | `Long` | `32.75` | 2,200,000.00 USD | 0.00 USD | 953.68 USD | `-43.30%` | `29.12` |
| `Live` | `Long` | `32.85` | 2,200,000.00 USD | 0.00 USD | 32,850.00 USD | `-43.13%` | `1,000.01` |
| `Live` | `Long` | `33.05` | 2,160,000.00 USD | 0.00 USD | 4,360.00 USD | `-42.78%` | `131.94` |
| `Live` | `Long` | `33.65` | 2,160,000.00 USD | 0.00 USD | 257.76 USD | `-41.74%` | `7.66` |
| `Live` | `Long` | `34.05` | 2,160,000.00 USD | 0.00 USD | 182.85 USD | `-41.05%` | `5.37` |
| `Live` | `Long` | `34.15` | 2,160,000.00 USD | 0.00 USD | 126.70 USD | `-40.88%` | `3.71` |
| `Live` | `Long` | `34.35` | 2,160,000.00 USD | 0.00 USD | 257.62 USD | `-40.53%` | `7.50` |
| `Live` | `Long` | `34.65` | 2,160,000.00 USD | 0.00 USD | 3,240.00 USD | `-40.01%` | `93.56` |
| `Live` | `Long` | `34.85` | 2,150,000.00 USD | 0.00 USD | 6,070.00 USD | `-39.67%` | `174.22` |
| `Live` | `Long` | `34.95` | 2,150,000.00 USD | 0.00 USD | 17,580.00 USD | `-39.49%` | `503.00` |
| `Live` | `Long` | `35.05` | 2,130,000.00 USD | 0.00 USD | 166.49 USD | `-39.32%` | `4.75` |
| `Live` | `Long` | `35.45` | 2,130,000.00 USD | 0.00 USD | 921.70 USD | `-38.63%` | `26.00` |
| `Live` | `Long` | `36.35` | 2,130,000.00 USD | 0.00 USD | 3,020.00 USD | `-37.07%` | `83.03` |
| `Live` | `Long` | `36.45` | 2,130,000.00 USD | 0.00 USD | 731.19 USD | `-36.90%` | `20.06` |
| `Live` | `Long` | `36.75` | 2,130,000.00 USD | 0.00 USD | 101.80 USD | `-36.38%` | `2.77` |
| `Live` | `Long` | `36.95` | 2,130,000.00 USD | 0.00 USD | 692.81 USD | `-36.03%` | `18.75` |
| `Live` | `Long` | `37.05` | 2,130,000.00 USD | 0.00 USD | 359.76 USD | `-35.86%` | `9.71` |
| `Live` | `Long` | `37.15` | 2,130,000.00 USD | 0.00 USD | 5,220.00 USD | `-35.69%` | `140.52` |
| `Live` | `Long` | `37.25` | 2,120,000.00 USD | 0.00 USD | 8,200.00 USD | `-35.51%` | `220.00` |
| `Live` | `Long` | `37.35` | 2,110,000.00 USD | 0.00 USD | 9,260.00 USD | `-35.34%` | `247.91` |
| `Live` | `Long` | `37.55` | 2,100,000.00 USD | 0.00 USD | 3,530.00 USD | `-34.99%` | `94.04` |
| `Live` | `Long` | `37.85` | 2,100,000.00 USD | 0.00 USD | 6,210.00 USD | `-34.47%` | `164.03` |
| `Live` | `Long` | `37.95` | 2,090,000.00 USD | 0.00 USD | 446.67 USD | `-34.30%` | `11.77` |
| `Live` | `Long` | `38.05` | 2,090,000.00 USD | 0.00 USD | 7,570.00 USD | `-34.13%` | `198.87` |
| `Live` | `Long` | `38.35` | 2,080,000.00 USD | 0.00 USD | 341.70 USD | `-33.61%` | `8.91` |
| `Live` | `Long` | `38.45` | 2,080,000.00 USD | 0.00 USD | 561.75 USD | `-33.43%` | `14.61` |
| `Live` | `Long` | `38.55` | 2,080,000.00 USD | 0.00 USD | 4,880.00 USD | `-33.26%` | `126.57` |
| `Live` | `Long` | `38.65` | 2,080,000.00 USD | 0.00 USD | 384.57 USD | `-33.09%` | `9.95` |
| `Live` | `Long` | `38.95` | 2,080,000.00 USD | 0.00 USD | 4,840.00 USD | `-32.57%` | `124.26` |
| `Live` | `Long` | `39.05` | 2,070,000.00 USD | 0.00 USD | 664,760.00 USD | `-32.40%` | `17,023.28` |
| `Live` | `Long` | `39.15` | 1,410,000.00 USD | 0.00 USD | 570.02 USD | `-32.22%` | `14.56` |
| `Live` | `Long` | `39.45` | 1,410,000.00 USD | 0.00 USD | 865.53 USD | `-31.70%` | `21.94` |
| `Live` | `Long` | `39.55` | 1,410,000.00 USD | 0.00 USD | 162.95 USD | `-31.53%` | `4.12` |
| `Live` | `Long` | `39.65` | 1,410,000.00 USD | 0.00 USD | 5,900.00 USD | `-31.36%` | `148.78` |
| `Live` | `Long` | `39.75` | 1,400,000.00 USD | 0.00 USD | 1,550.00 USD | `-31.18%` | `38.90` |
| `Live` | `Long` | `39.85` | 1,400,000.00 USD | 0.00 USD | 1,120.00 USD | `-31.01%` | `28.22` |
| `Live` | `Long` | `40.05` | 1,400,000.00 USD | 0.00 USD | 2,160.00 USD | `-30.66%` | `53.97` |
| `Live` | `Long` | `40.25` | 1,400,000.00 USD | 0.00 USD | 154.56 USD | `-30.32%` | `3.84` |
| `Live` | `Long` | `40.45` | 1,400,000.00 USD | 0.00 USD | 1,010.00 USD | `-29.97%` | `24.92` |
| `Live` | `Long` | `40.55` | 1,400,000.00 USD | 0.00 USD | 133.00 USD | `-29.80%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,400,000.00 USD | 0.00 USD | 943.89 USD | `-29.63%` | `23.22` |
| `Live` | `Long` | `40.85` | 1,390,000.00 USD | 0.00 USD | 6,340.00 USD | `-29.28%` | `155.23` |
| `Live` | `Long` | `40.95` | 1,390,000.00 USD | 0.00 USD | 509.01 USD | `-29.11%` | `12.43` |
| `Live` | `Long` | `41.05` | 1,390,000.00 USD | 0.00 USD | 396.54 USD | `-28.93%` | `9.66` |
| `Live` | `Long` | `41.25` | 1,390,000.00 USD | 0.00 USD | 14,490.00 USD | `-28.59%` | `351.26` |
| `Live` | `Long` | `41.45` | 1,370,000.00 USD | 0.00 USD | 644.96 USD | `-28.24%` | `15.56` |
| `Live` | `Long` | `41.75` | 1,370,000.00 USD | 0.00 USD | 3,570.00 USD | `-27.72%` | `85.43` |
| `Live` | `Long` | `42.05` | 1,370,000.00 USD | 0.00 USD | 3,090.00 USD | `-27.20%` | `73.52` |
| `Live` | `Long` | `42.15` | 1,370,000.00 USD | 0.00 USD | 64,190.00 USD | `-27.03%` | `1,522.78` |
| `Live` | `Long` | `42.25` | 1,300,000.00 USD | 0.00 USD | 35,410.00 USD | `-26.86%` | `838.00` |
| `Live` | `Long` | `42.65` | 1,270,000.00 USD | 0.00 USD | 1,570.00 USD | `-26.16%` | `36.70` |
| `Live` | `Long` | `42.75` | 1,260,000.00 USD | 0.00 USD | 26,780.00 USD | `-25.99%` | `626.50` |
| `Live` | `Long` | `42.85` | 1,240,000.00 USD | 0.00 USD | 7,550.00 USD | `-25.82%` | `176.14` |
| `Live` | `Long` | `42.95` | 1,230,000.00 USD | 0.00 USD | 2,000.00 USD | `-25.64%` | `46.65` |
| `Live` | `Long` | `43.05` | 1,230,000.00 USD | 0.00 USD | 8,950.00 USD | `-25.47%` | `208.00` |
| `Live` | `Long` | `43.15` | 1,220,000.00 USD | 0.00 USD | 157,020.00 USD | `-25.30%` | `3,638.92` |
| `Live` | `Long` | `43.25` | 1,060,000.00 USD | 0.00 USD | 312.26 USD | `-25.13%` | `7.22` |
| `Live` | `Long` | `43.35` | 1,060,000.00 USD | 0.00 USD | 6,690.00 USD | `-24.95%` | `154.24` |
| `Live` | `Long` | `43.45` | 1,060,000.00 USD | 0.00 USD | 706.06 USD | `-24.78%` | `16.25` |
| `Live` | `Long` | `43.65` | 1,050,000.00 USD | 0.00 USD | 5,620.00 USD | `-24.43%` | `128.84` |
| `Live` | `Long` | `43.85` | 1,050,000.00 USD | 0.00 USD | 801.14 USD | `-24.09%` | `18.27` |
| `Live` | `Long` | `43.95` | 1,050,000.00 USD | 0.00 USD | 1,580.00 USD | `-23.91%` | `35.97` |
| `Live` | `Long` | `44.15` | 1,050,000.00 USD | 0.00 USD | 2,380.00 USD | `-23.57%` | `53.99` |
| `Live` | `Long` | `44.25` | 1,040,000.00 USD | 0.00 USD | 12,470.00 USD | `-23.39%` | `281.80` |
| `Live` | `Long` | `44.35` | 1,030,000.00 USD | 0.00 USD | 84,440.00 USD | `-23.22%` | `1,903.87` |
| `Live` | `Long` | `44.55` | 947,050.00 USD | 0.00 USD | 842.44 USD | `-22.87%` | `18.91` |
| `Live` | `Long` | `44.75` | 946,210.00 USD | 0.00 USD | 4,680.00 USD | `-22.53%` | `104.55` |
| `Live` | `Long` | `44.85` | 941,530.00 USD | 0.00 USD | 134.55 USD | `-22.36%` | `3.00` |
| `Live` | `Long` | `44.95` | 941,390.00 USD | 0.00 USD | 2,620.00 USD | `-22.18%` | `58.18` |
| `Live` | `Long` | `45.05` | 938,780.00 USD | 0.00 USD | 329.32 USD | `-22.01%` | `7.31` |
| `Live` | `Long` | `45.15` | 938,450.00 USD | 0.00 USD | 135.00 USD | `-21.84%` | `2.99` |
| `Live` | `Long` | `45.25` | 938,310.00 USD | 0.00 USD | 11,030.00 USD | `-21.66%` | `243.69` |
| `Live` | `Long` | `45.35` | 927,290.00 USD | 0.00 USD | 1,780.00 USD | `-21.49%` | `39.28` |
| `Live` | `Long` | `45.45` | 925,500.00 USD | 0.00 USD | 23,940.00 USD | `-21.32%` | `526.65` |
| `Live` | `Long` | `45.55` | 901,570.00 USD | 0.00 USD | 318.39 USD | `-21.14%` | `6.99` |
| `Live` | `Long` | `45.95` | 901,250.00 USD | 0.00 USD | 12,160.00 USD | `-20.45%` | `264.65` |
| `Live` | `Long` | `46.05` | 889,090.00 USD | 0.00 USD | 9,710.00 USD | `-20.28%` | `210.95` |
| `Live` | `Long` | `46.25` | 879,380.00 USD | 0.00 USD | 40,250.00 USD | `-19.93%` | `870.28` |
| `Live` | `Long` | `46.35` | 839,120.00 USD | 0.00 USD | 383.78 USD | `-19.76%` | `8.28` |
| `Live` | `Long` | `46.65` | 838,740.00 USD | 0.00 USD | 936.73 USD | `-19.24%` | `20.08` |
| `Live` | `Long` | `46.85` | 837,800.00 USD | 0.00 USD | 358.40 USD | `-18.89%` | `7.65` |
| `Live` | `Long` | `46.95` | 837,450.00 USD | 0.00 USD | 158.22 USD | `-18.72%` | `3.37` |
| `Live` | `Long` | `47.15` | 837,290.00 USD | 0.00 USD | 1,980.00 USD | `-18.37%` | `42.07` |
| `Live` | `Long` | `47.25` | 835,300.00 USD | 0.00 USD | 574.09 USD | `-18.20%` | `12.15` |
| `Live` | `Long` | `47.35` | 834,730.00 USD | 0.00 USD | 2,600.00 USD | `-18.03%` | `55.00` |
| `Live` | `Long` | `47.45` | 832,130.00 USD | 0.00 USD | 2,180.00 USD | `-17.85%` | `45.94` |
| `Live` | `Long` | `47.55` | 829,950.00 USD | 0.00 USD | 1,770.00 USD | `-17.68%` | `37.28` |
| `Live` | `Long` | `47.65` | 828,170.00 USD | 0.00 USD | 259.22 USD | `-17.51%` | `5.44` |
| `Live` | `Long` | `47.75` | 827,910.00 USD | 0.00 USD | 4,780.00 USD | `-17.33%` | `100.00` |
| `Live` | `Long` | `47.85` | 823,140.00 USD | 0.00 USD | 975.66 USD | `-17.16%` | `20.39` |
| `Live` | `Long` | `47.95` | 822,160.00 USD | 0.00 USD | 1,440.00 USD | `-16.99%` | `30.00` |
| `Live` | `Long` | `48.05` | 820,720.00 USD | 0.00 USD | 1,860.00 USD | `-16.82%` | `38.61` |
| `Live` | `Long` | `48.15` | 818,870.00 USD | 0.00 USD | 2,680.00 USD | `-16.64%` | `55.56` |
| `Live` | `Long` | `48.25` | 816,190.00 USD | 0.00 USD | 4,390.00 USD | `-16.47%` | `90.89` |
| `Live` | `Long` | `48.55` | 811,810.00 USD | 0.00 USD | 2,030.00 USD | `-15.95%` | `41.85` |
| `Live` | `Long` | `48.65` | 809,780.00 USD | 0.00 USD | 273.90 USD | `-15.78%` | `5.63` |
| `Live` | `Long` | `48.75` | 809,500.00 USD | 0.00 USD | 231.56 USD | `-15.60%` | `4.75` |
| `Live` | `Long` | `48.95` | 809,270.00 USD | 0.00 USD | 8,430.00 USD | `-15.26%` | `172.14` |
| `Live` | `Long` | `49.05` | 800,850.00 USD | 0.00 USD | 1,580.00 USD | `-15.08%` | `32.25` |
| `Live` | `Long` | `49.15` | 799,260.00 USD | 0.00 USD | 5,740.00 USD | `-14.91%` | `116.83` |
| `Live` | `Long` | `49.25` | 793,520.00 USD | 0.00 USD | 49,250.00 USD | `-14.74%` | `1,000.00` |
| `Live` | `Long` | `49.35` | 744,270.00 USD | 0.00 USD | 5,230.00 USD | `-14.56%` | `105.97` |
| `Live` | `Long` | `49.45` | 739,040.00 USD | 0.00 USD | 1,960.00 USD | `-14.39%` | `39.73` |
| `Live` | `Long` | `49.55` | 737,080.00 USD | 0.00 USD | 18,010.00 USD | `-14.22%` | `363.57` |
| `Live` | `Long` | `49.65` | 719,060.00 USD | 0.00 USD | 4,890.00 USD | `-14.05%` | `98.52` |
| `Live` | `Long` | `49.75` | 714,170.00 USD | 0.00 USD | 1,250.00 USD | `-13.87%` | `25.06` |
| `Live` | `Long` | `49.95` | 712,920.00 USD | 0.00 USD | 29,080.00 USD | `-13.53%` | `582.09` |
| `Live` | `Long` | `50.05` | 683,850.00 USD | 0.00 USD | 1,820.00 USD | `-13.35%` | `36.43` |
| `Live` | `Long` | `50.15` | 682,030.00 USD | 0.00 USD | 172.01 USD | `-13.18%` | `3.43` |
| `Live` | `Long` | `50.25` | 681,850.00 USD | 0.00 USD | 102.51 USD | `-13.01%` | `2.04` |
| `Live` | `Long` | `50.35` | 681,750.00 USD | 0.00 USD | 1,030.00 USD | `-12.83%` | `20.49` |
| `Live` | `Long` | `50.45` | 680,720.00 USD | 0.00 USD | 40,000.00 USD | `-12.66%` | `792.77` |
| `Live` | `Long` | `50.55` | 640,720.00 USD | 0.00 USD | 87,380.00 USD | `-12.49%` | `1,728.61` |
| `Live` | `Long` | `50.75` | 553,340.00 USD | 0.00 USD | 9,050.00 USD | `-12.14%` | `178.28` |
| `Live` | `Long` | `50.95` | 544,290.00 USD | 0.00 USD | 245.07 USD | `-11.79%` | `4.81` |
| `Live` | `Long` | `51.15` | 544,050.00 USD | 0.00 USD | 219,370.00 USD | `-11.45%` | `4,288.79` |
| `Live` | `Long` | `51.45` | 324,680.00 USD | 0.00 USD | 22,270.00 USD | `-10.93%` | `432.80` |
| `Live` | `Long` | `51.55` | 302,410.00 USD | 0.00 USD | 26,330.00 USD | `-10.76%` | `510.69` |
| `Live` | `Long` | `51.65` | 276,080.00 USD | 0.00 USD | 155.47 USD | `-10.58%` | `3.01` |
| `Live` | `Long` | `51.75` | 275,930.00 USD | 0.00 USD | 6,450.00 USD | `-10.41%` | `124.64` |
| `Live` | `Long` | `51.85` | 269,480.00 USD | 0.00 USD | 3,580.00 USD | `-10.24%` | `69.10` |
| `Live` | `Long` | `51.95` | 265,900.00 USD | 0.00 USD | 12,070.00 USD | `-10.06%` | `232.41` |
| `Live` | `Long` | `52.25` | 253,820.00 USD | 0.00 USD | 179.22 USD | `-9.54%` | `3.43` |
| `Live` | `Long` | `52.35` | 253,640.00 USD | 0.00 USD | 1,470.00 USD | `-9.37%` | `28.09` |
| `Live` | `Long` | `52.45` | 252,170.00 USD | 0.00 USD | 3,830.00 USD | `-9.20%` | `72.95` |
| `Live` | `Long` | `52.55` | 248,350.00 USD | 0.00 USD | 8,700.00 USD | `-9.02%` | `165.49` |
| `Live` | `Long` | `52.75` | 239,650.00 USD | 0.00 USD | 7,450.00 USD | `-8.68%` | `141.16` |
| `Live` | `Long` | `52.85` | 232,200.00 USD | 0.00 USD | 29,320.00 USD | `-8.51%` | `554.84` |
| `Live` | `Long` | `52.95` | 202,880.00 USD | 0.00 USD | 11,680.00 USD | `-8.33%` | `220.59` |
| `Live` | `Long` | `53.05` | 191,200.00 USD | 0.00 USD | 900.26 USD | `-8.16%` | `16.97` |
| `Live` | `Long` | `53.15` | 190,300.00 USD | 0.00 USD | 181.24 USD | `-7.99%` | `3.41` |
| `Live` | `Long` | `53.25` | 190,120.00 USD | 0.00 USD | 1,500.00 USD | `-7.81%` | `28.15` |
| `Live` | `Long` | `53.35` | 188,620.00 USD | 0.00 USD | 1,910.00 USD | `-7.64%` | `35.71` |
| `Live` | `Long` | `53.45` | 186,710.00 USD | 0.00 USD | 4,880.00 USD | `-7.47%` | `91.21` |
| `Live` | `Long` | `53.55` | 181,840.00 USD | 0.00 USD | 23,330.00 USD | `-7.29%` | `435.71` |
| `Live` | `Long` | `53.65` | 158,510.00 USD | 0.00 USD | 533.82 USD | `-7.12%` | `9.95` |
| `Live` | `Long` | `53.75` | 157,970.00 USD | 0.00 USD | 332.71 USD | `-6.95%` | `6.19` |
| `Live` | `Long` | `53.85` | 157,640.00 USD | 0.00 USD | 2,130.00 USD | `-6.77%` | `39.58` |
| `Live` | `Long` | `53.95` | 155,510.00 USD | 0.00 USD | 27,050.00 USD | `-6.60%` | `501.35` |
| `Live` | `Long` | `54.05` | 128,460.00 USD | 0.00 USD | 219.44 USD | `-6.43%` | `4.06` |
| `Live` | `Long` | `54.15` | 128,240.00 USD | 0.00 USD | 13,210.00 USD | `-6.25%` | `243.97` |
| `Live` | `Long` | `54.25` | 115,030.00 USD | 0.00 USD | 2,400.00 USD | `-6.08%` | `44.18` |
| `Live` | `Long` | `54.45` | 112,630.00 USD | 0.00 USD | 186.76 USD | `-5.74%` | `3.43` |
| `Live` | `Long` | `54.55` | 112,450.00 USD | 0.00 USD | 13,530.00 USD | `-5.56%` | `248.12` |
| `Live` | `Long` | `54.65` | 98,910.00 USD | 0.00 USD | 488.57 USD | `-5.39%` | `8.94` |
| `Live` | `Long` | `54.75` | 98,420.00 USD | 0.00 USD | 470.85 USD | `-5.22%` | `8.60` |
| `Live` | `Long` | `54.95` | 97,950.00 USD | 0.00 USD | 6,890.00 USD | `-4.87%` | `125.47` |
| `Live` | `Long` | `55.05` | 91,060.00 USD | 0.00 USD | 1,100.00 USD | `-4.70%` | `19.96` |
| `Live` | `Long` | `55.15` | 89,960.00 USD | 0.00 USD | 4,950.00 USD | `-4.52%` | `89.80` |
| `Live` | `Long` | `55.25` | 85,010.00 USD | 0.00 USD | 3,350.00 USD | `-4.35%` | `60.69` |
| `Live` | `Long` | `55.35` | 81,650.00 USD | 0.00 USD | 1,610.00 USD | `-4.18%` | `29.05` |
| `Live` | `Long` | `55.45` | 80,050.00 USD | 0.00 USD | 424.19 USD | `-4.00%` | `7.65` |
| `Live` | `Long` | `55.55` | 79,620.00 USD | 0.00 USD | 1,390.00 USD | `-3.83%` | `25.05` |
| `Live` | `Long` | `56.15` | 78,230.00 USD | 0.00 USD | 78,230.00 USD | `-2.79%` | `1,393.24` |
| `Live` | `Short` | `60.75` | 1,040.00 USD | 1,040.00 USD | 0.00 USD | `+5.17%` | `17.16` |
| `Live` | `Short` | `60.95` | 1,840.00 USD | 794.18 USD | 0.00 USD | `+5.52%` | `13.03` |
| `Live` | `Short` | `61.05` | 1,950.00 USD | 116.61 USD | 0.00 USD | `+5.69%` | `1.91` |
| `Live` | `Short` | `61.15` | 6,730.00 USD | 4,770.00 USD | 0.00 USD | `+5.86%` | `78.06` |
| `Live` | `Short` | `61.45` | 6,990.00 USD | 267.31 USD | 0.00 USD | `+6.38%` | `4.35` |
| `Live` | `Short` | `61.65` | 218,200.00 USD | 211,210.00 USD | 0.00 USD | `+6.73%` | `3,425.89` |
| `Live` | `Short` | `65.95` | 219,360.00 USD | 1,160.00 USD | 0.00 USD | `+14.17%` | `17.59` |
| `Live` | `Short` | `66.85` | 253,310.00 USD | 33,950.00 USD | 0.00 USD | `+15.73%` | `507.83` |
| `Live` | `Short` | `66.95` | 253,430.00 USD | 121.18 USD | 0.00 USD | `+15.90%` | `1.81` |
| `Live` | `Short` | `67.85` | 254,140.00 USD | 709.03 USD | 0.00 USD | `+17.46%` | `10.45` |
| `Live` | `Short` | `69.45` | 254,550.00 USD | 414.62 USD | 0.00 USD | `+20.23%` | `5.97` |
| `Live` | `Short` | `70.45` | 261,290.00 USD | 6,740.00 USD | 0.00 USD | `+21.96%` | `95.63` |
| `Live` | `Short` | `71.75` | 266,400.00 USD | 5,110.00 USD | 0.00 USD | `+24.21%` | `71.15` |
| `Live` | `Short` | `72.95` | 267,060.00 USD | 666.03 USD | 0.00 USD | `+26.29%` | `9.13` |
| `Live` | `Short` | `76.35` | 275,440.00 USD | 8,380.00 USD | 0.00 USD | `+32.18%` | `109.80` |
| `Live` | `Short` | `77.85` | 276,050.00 USD | 602.56 USD | 0.00 USD | `+34.77%` | `7.74` |
| `Live` | `Short` | `77.95` | 276,180.00 USD | 136.41 USD | 0.00 USD | `+34.95%` | `1.75` |
| `Live` | `Short` | `80.75` | 276,830.00 USD | 646.00 USD | 0.00 USD | `+39.80%` | `8.00` |
| `Live` | `Short` | `81.05` | 295,830.00 USD | 19,000.00 USD | 0.00 USD | `+40.31%` | `234.42` |
| `Live` | `Short` | `81.55` | 295,950.00 USD | 123.96 USD | 0.00 USD | `+41.18%` | `1.52` |
| `Live` | `Short` | `82.65` | 299,810.00 USD | 3,850.00 USD | 0.00 USD | `+43.08%` | `46.61` |
| `Live` | `Short` | `82.75` | 300,020.00 USD | 214.32 USD | 0.00 USD | `+43.26%` | `2.59` |
| `Live` | `Short` | `84.65` | 300,880.00 USD | 862.58 USD | 0.00 USD | `+46.55%` | `10.19` |
| `Live` | `Short` | `86.75` | 324,030.00 USD | 23,150.00 USD | 0.00 USD | `+50.18%` | `266.81` |
| `Live` | `Short` | `87.15` | 326,900.00 USD | 2,880.00 USD | 0.00 USD | `+50.88%` | `33.00` |
| `Live` | `Short` | `87.65` | 330,410.00 USD | 3,510.00 USD | 0.00 USD | `+51.74%` | `40.00` |
| `Live` | `Short` | `89.65` | 332,240.00 USD | 1,830.00 USD | 0.00 USD | `+55.20%` | `20.39` |
| `Live` | `Short` | `96.35` | 334,650.00 USD | 2,410.00 USD | 0.00 USD | `+66.80%` | `25.00` |
| `Live` | `Short` | `97.15` | 335,310.00 USD | 663.53 USD | 0.00 USD | `+68.19%` | `6.83` |
| `Live` | `Short` | `97.95` | 336,350.00 USD | 1,040.00 USD | 0.00 USD | `+69.57%` | `10.63` |
| `Live` | `Short` | `104.65` | 689,440.00 USD | 353,090.00 USD | 0.00 USD | `+81.17%` | `3,374.01` |
| `Live` | `Short` | `105.35` | 710,510.00 USD | 21,070.00 USD | 0.00 USD | `+82.38%` | `200.00` |
| `Live` | `Short` | `109.15` | 732,340.00 USD | 21,830.00 USD | 0.00 USD | `+88.96%` | `200.00` |
| `Live` | `Short` | `110.45` | 732,470.00 USD | 131.44 USD | 0.00 USD | `+91.21%` | `1.19` |
| `Live` | `Short` | `110.55` | 733,590.00 USD | 1,120.00 USD | 0.00 USD | `+91.39%` | `10.11` |
| `Live` | `Short` | `110.65` | 738,420.00 USD | 4,830.00 USD | 0.00 USD | `+91.56%` | `43.66` |
| `Live` | `Short` | `110.95` | 739,090.00 USD | 664.59 USD | 0.00 USD | `+92.08%` | `5.99` |
| `Live` | `Short` | `114.65` | 739,510.00 USD | 420.77 USD | 0.00 USD | `+98.48%` | `3.67` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 520,880.00 USD | 0.00 USD | 392.18 USD | `-65.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 520,490.00 USD | 0.00 USD | 2,310.00 USD | `-61.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 518,180.00 USD | 0.00 USD | 122.24 USD | `-56.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 518,060.00 USD | 0.00 USD | 1,560.00 USD | `-56.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 516,510.00 USD | 0.00 USD | 410.25 USD | `-52.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 516,090.00 USD | 0.00 USD | 281.57 USD | `-47.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 515,810.00 USD | 0.00 USD | 36,050.00 USD | `-37.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 479,760.00 USD | 0.00 USD | 37,550.00 USD | `-34.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 442,210.00 USD | 0.00 USD | 447.01 USD | `-34.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 441,770.00 USD | 0.00 USD | 40,560.00 USD | `-32.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 401,210.00 USD | 0.00 USD | 489.57 USD | `-31.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 400,720.00 USD | 0.00 USD | 1,550.00 USD | `-30.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 399,170.00 USD | 0.00 USD | 9,500.00 USD | `-30.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 389,660.00 USD | 0.00 USD | 2,060.00 USD | `-29.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 387,610.00 USD | 0.00 USD | 2,960.00 USD | `-28.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 384,650.00 USD | 0.00 USD | 6,050.00 USD | `-27.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 378,600.00 USD | 0.00 USD | 5,680.00 USD | `-25.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 372,920.00 USD | 0.00 USD | 672.22 USD | `-24.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 372,250.00 USD | 0.00 USD | 213.80 USD | `-23.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 372,030.00 USD | 0.00 USD | 223.20 USD | `-22.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 371,810.00 USD | 0.00 USD | 391.13 USD | `-22.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 371,420.00 USD | 0.00 USD | 7,080.00 USD | `-22.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 364,340.00 USD | 0.00 USD | 1,370.00 USD | `-21.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 362,980.00 USD | 0.00 USD | 553.80 USD | `-20.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 362,420.00 USD | 0.00 USD | 14,000.00 USD | `-19.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 348,430.00 USD | 0.00 USD | 158.56 USD | `-18.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 348,270.00 USD | 0.00 USD | 373.28 USD | `-18.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 347,900.00 USD | 0.00 USD | 849.46 USD | `-18.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 347,050.00 USD | 0.00 USD | 1,150.00 USD | `-16.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 345,900.00 USD | 0.00 USD | 1,740.00 USD | `-15.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 344,160.00 USD | 0.00 USD | 981.00 USD | `-15.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 343,170.00 USD | 0.00 USD | 1,150.00 USD | `-14.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 342,030.00 USD | 0.00 USD | 298.20 USD | `-13.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 341,730.00 USD | 0.00 USD | 14,650.00 USD | `-13.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 327,080.00 USD | 0.00 USD | 6,410.00 USD | `-13.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 320,660.00 USD | 0.00 USD | 459.70 USD | `-12.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 320,200.00 USD | 0.00 USD | 1,020.00 USD | `-11.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 319,180.00 USD | 0.00 USD | 439.89 USD | `-11.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 318,740.00 USD | 0.00 USD | 3,700.00 USD | `-10.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.75` | 315,040.00 USD | 0.00 USD | 107.64 USD | `-10.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 314,930.00 USD | 0.00 USD | 27,730.00 USD | `-9.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 287,200.00 USD | 0.00 USD | 51,800.00 USD | `-9.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 235,400.00 USD | 0.00 USD | 10,530.00 USD | `-8.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 224,870.00 USD | 0.00 USD | 271.13 USD | `-8.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 224,600.00 USD | 0.00 USD | 12,410.00 USD | `-8.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 212,200.00 USD | 0.00 USD | 1,060.00 USD | `-8.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 211,130.00 USD | 0.00 USD | 460.81 USD | `-7.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 210,670.00 USD | 0.00 USD | 184.21 USD | `-7.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 210,490.00 USD | 0.00 USD | 1,370.00 USD | `-7.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 209,120.00 USD | 0.00 USD | 462.03 USD | `-6.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 208,660.00 USD | 0.00 USD | 601.58 USD | `-6.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 208,060.00 USD | 0.00 USD | 3,090.00 USD | `-6.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 204,970.00 USD | 0.00 USD | 156.53 USD | `-5.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.45` | 204,810.00 USD | 0.00 USD | 570.09 USD | `-5.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.55` | 204,240.00 USD | 0.00 USD | 1,690.00 USD | `-5.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.65` | 202,550.00 USD | 0.00 USD | 2,210.00 USD | `-5.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 200,340.00 USD | 0.00 USD | 33,280.00 USD | `-5.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.95` | 167,060.00 USD | 0.00 USD | 219.80 USD | `-4.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 166,840.00 USD | 0.00 USD | 21,090.00 USD | `-4.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.25` | 145,760.00 USD | 0.00 USD | 429.85 USD | `-4.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.35` | 145,330.00 USD | 0.00 USD | 2,140.00 USD | `-4.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.55` | 143,190.00 USD | 0.00 USD | 113.88 USD | `-3.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.65` | 143,070.00 USD | 0.00 USD | 4,930.00 USD | `-3.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.75` | 138,150.00 USD | 0.00 USD | 1,820.00 USD | `-3.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.85` | 136,330.00 USD | 0.00 USD | 196.59 USD | `-3.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.95` | 136,140.00 USD | 0.00 USD | 193.03 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 135,940.00 USD | 0.00 USD | 587.96 USD | `-2.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 135,350.00 USD | 0.00 USD | 1,070.00 USD | `-2.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.35` | 134,280.00 USD | 0.00 USD | 78,570.00 USD | `-2.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.45` | 55,710.00 USD | 0.00 USD | 694.90 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.55` | 55,010.00 USD | 0.00 USD | 2,640.00 USD | `-2.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.65` | 52,380.00 USD | 0.00 USD | 1,230.00 USD | `-1.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.75` | 51,150.00 USD | 0.00 USD | 1,200.00 USD | `-1.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.85` | 49,940.00 USD | 0.00 USD | 17,440.00 USD | `-1.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.95` | 32,500.00 USD | 0.00 USD | 474.96 USD | `-1.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.05` | 32,020.00 USD | 0.00 USD | 5,800.00 USD | `-1.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.15` | 26,220.00 USD | 0.00 USD | 4,030.00 USD | `-1.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.25` | 22,190.00 USD | 0.00 USD | 150.00 USD | `-0.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.35` | 22,040.00 USD | 0.00 USD | 444.46 USD | `-0.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.45` | 21,600.00 USD | 0.00 USD | 877.26 USD | `-0.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.55` | 20,720.00 USD | 0.00 USD | 20,360.00 USD | `-0.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.65` | 359.50 USD | 0.00 USD | 160.27 USD | `-0.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.75` | 199.24 USD | 0.00 USD | 199.24 USD | `-0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.85` | 392.22 USD | 392.22 USD | 0.00 USD | `+0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.95` | 520.87 USD | 128.65 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 2,500.00 USD | 1,980.00 USD | 0.00 USD | `+0.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 3,210.00 USD | 706.52 USD | 0.00 USD | `+0.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 4,290.00 USD | 1,080.00 USD | 0.00 USD | `+0.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 4,410.00 USD | 123.70 USD | 0.00 USD | `+1.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 4,510.00 USD | 101.12 USD | 0.00 USD | `+1.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 4,610.00 USD | 100.71 USD | 0.00 USD | `+1.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.65` | 4,890.00 USD | 274.48 USD | 0.00 USD | `+1.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 5,010.00 USD | 124.55 USD | 0.00 USD | `+1.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 7,960.00 USD | 2,940.00 USD | 0.00 USD | `+1.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 13,050.00 USD | 5,100.00 USD | 0.00 USD | `+2.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 17,850.00 USD | 4,800.00 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 19,130.00 USD | 1,280.00 USD | 0.00 USD | `+2.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 19,590.00 USD | 461.74 USD | 0.00 USD | `+2.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 19,790.00 USD | 200.35 USD | 0.00 USD | `+2.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.55` | 20,290.00 USD | 496.65 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 21,020.00 USD | 724.75 USD | 0.00 USD | `+3.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.75` | 21,130.00 USD | 113.53 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 21,550.00 USD | 418.35 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.95` | 36,910.00 USD | 15,360.00 USD | 0.00 USD | `+3.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 37,540.00 USD | 627.52 USD | 0.00 USD | `+3.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.15` | 39,340.00 USD | 1,800.00 USD | 0.00 USD | `+4.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 39,890.00 USD | 551.00 USD | 0.00 USD | `+4.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.45` | 324,000.00 USD | 284,100.00 USD | 0.00 USD | `+4.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 324,460.00 USD | 463.21 USD | 0.00 USD | `+4.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 325,260.00 USD | 795.12 USD | 0.00 USD | `+5.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.75` | 325,660.00 USD | 407.63 USD | 0.00 USD | `+5.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 326,860.00 USD | 1,190.00 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 327,740.00 USD | 882.56 USD | 0.00 USD | `+5.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 330,100.00 USD | 2,360.00 USD | 0.00 USD | `+5.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 330,230.00 USD | 125.56 USD | 0.00 USD | `+6.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.35` | 330,470.00 USD | 236.20 USD | 0.00 USD | `+6.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 334,060.00 USD | 3,600.00 USD | 0.00 USD | `+6.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 334,700.00 USD | 643.20 USD | 0.00 USD | `+6.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.95` | 336,820.00 USD | 2,120.00 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 336,930.00 USD | 106.11 USD | 0.00 USD | `+7.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.25` | 337,050.00 USD | 117.03 USD | 0.00 USD | `+7.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.35` | 337,530.00 USD | 483.21 USD | 0.00 USD | `+7.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.45` | 337,750.00 USD | 217.95 USD | 0.00 USD | `+8.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.55` | 338,100.00 USD | 347.15 USD | 0.00 USD | `+8.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 338,810.00 USD | 716.72 USD | 0.00 USD | `+8.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.75` | 338,950.00 USD | 141.19 USD | 0.00 USD | `+8.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 340,300.00 USD | 1,340.00 USD | 0.00 USD | `+9.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 341,200.00 USD | 900.52 USD | 0.00 USD | `+9.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 341,900.00 USD | 703.97 USD | 0.00 USD | `+9.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.35` | 342,040.00 USD | 140.64 USD | 0.00 USD | `+9.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 342,710.00 USD | 668.13 USD | 0.00 USD | `+9.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 347,260.00 USD | 4,550.00 USD | 0.00 USD | `+10.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 347,810.00 USD | 555.03 USD | 0.00 USD | `+10.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 348,350.00 USD | 531.62 USD | 0.00 USD | `+10.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 348,550.00 USD | 202.69 USD | 0.00 USD | `+11.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 348,850.00 USD | 298.04 USD | 0.00 USD | `+11.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 348,950.00 USD | 102.13 USD | 0.00 USD | `+12.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 349,490.00 USD | 540.09 USD | 0.00 USD | `+12.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 349,590.00 USD | 100.79 USD | 0.00 USD | `+13.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 349,850.00 USD | 262.20 USD | 0.00 USD | `+13.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.65` | 350,170.00 USD | 315.12 USD | 0.00 USD | `+13.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 350,540.00 USD | 371.49 USD | 0.00 USD | `+13.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.85` | 351,420.00 USD | 881.07 USD | 0.00 USD | `+14.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 352,250.00 USD | 825.63 USD | 0.00 USD | `+14.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 352,780.00 USD | 534.00 USD | 0.00 USD | `+15.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 363,860.00 USD | 11,080.00 USD | 0.00 USD | `+15.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 377,270.00 USD | 13,410.00 USD | 0.00 USD | `+16.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 382,130.00 USD | 4,860.00 USD | 0.00 USD | `+18.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 382,340.00 USD | 204.48 USD | 0.00 USD | `+20.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 383,270.00 USD | 929.64 USD | 0.00 USD | `+21.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 703,160.00 USD | 319,890.00 USD | 0.00 USD | `+21.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 703,330.00 USD | 170.04 USD | 0.00 USD | `+22.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 709,100.00 USD | 5,770.00 USD | 0.00 USD | `+22.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 709,650.00 USD | 555.61 USD | 0.00 USD | `+23.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 710,800.00 USD | 1,150.00 USD | 0.00 USD | `+24.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 713,510.00 USD | 2,700.00 USD | 0.00 USD | `+24.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 713,660.00 USD | 156.78 USD | 0.00 USD | `+25.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 716,890.00 USD | 3,220.00 USD | 0.00 USD | `+25.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 717,300.00 USD | 411.14 USD | 0.00 USD | `+27.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 840,490.00 USD | 123,190.00 USD | 0.00 USD | `+28.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 841,510.00 USD | 1,020.00 USD | 0.00 USD | `+29.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 841,610.00 USD | 104.93 USD | 0.00 USD | `+29.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 842,000.00 USD | 392.51 USD | 0.00 USD | `+29.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 842,410.00 USD | 402.59 USD | 0.00 USD | `+30.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 842,720.00 USD | 315.18 USD | 0.00 USD | `+33.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 902,030.00 USD | 59,310.00 USD | 0.00 USD | `+36.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 905,190.00 USD | 3,160.00 USD | 0.00 USD | `+36.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 910,880.00 USD | 5,690.00 USD | 0.00 USD | `+38.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 948,500.00 USD | 37,620.00 USD | 0.00 USD | `+38.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 948,930.00 USD | 433.89 USD | 0.00 USD | `+40.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 989,630.00 USD | 40,700.00 USD | 0.00 USD | `+40.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 989,790.00 USD | 164.10 USD | 0.00 USD | `+42.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 990,340.00 USD | 546.81 USD | 0.00 USD | `+43.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 992,640.00 USD | 2,300.00 USD | 0.00 USD | `+45.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 1,000,000.00 USD | 12,070.00 USD | 0.00 USD | `+47.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.75` | 1,020,000.00 USD | 12,330.00 USD | 0.00 USD | `+48.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.25` | 1,020,000.00 USD | 435.38 USD | 0.00 USD | `+51.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 1,020,000.00 USD | 1,580.00 USD | 0.00 USD | `+52.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 1,060,000.00 USD | 37,000.00 USD | 0.00 USD | `+52.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 1,060,000.00 USD | 473.21 USD | 0.00 USD | `+53.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 1,060,000.00 USD | 1,270.00 USD | 0.00 USD | `+54.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 1,060,000.00 USD | 1,630.00 USD | 0.00 USD | `+54.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 1,080,000.00 USD | 18,740.00 USD | 0.00 USD | `+55.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 1,080,000.00 USD | 481.55 USD | 0.00 USD | `+58.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 1,080,000.00 USD | 1,330.00 USD | 0.00 USD | `+59.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 1,080,000.00 USD | 188.10 USD | 0.00 USD | `+62.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,350,000.00 USD | 266,140.00 USD | 0.00 USD | `+64.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,350,000.00 USD | 3,400.00 USD | 0.00 USD | `+65.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,370,000.00 USD | 21,930.00 USD | 0.00 USD | `+66.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,370,000.00 USD | 294.15 USD | 0.00 USD | `+69.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,380,000.00 USD | 4,010.00 USD | 0.00 USD | `+73.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,380,000.00 USD | 306.15 USD | 0.00 USD | `+76.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,380,000.00 USD | 936.72 USD | 0.00 USD | `+78.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,380,000.00 USD | 2,920.00 USD | 0.00 USD | `+78.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,380,000.00 USD | 324.15 USD | 0.00 USD | `+87.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 1,380,000.00 USD | 123.23 USD | 0.00 USD | `+88.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 1,470,000.00 USD | 89,110.00 USD | 0.00 USD | `+92.25%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `51.10` | 19,100,000.00 USD | 0.00 USD | 19,100,000.00 USD | 114,000.00 USD | 49,240.00 USD | 98,810.00 USD |
| `7D` | `51.20` | 18,840,000.00 USD | 0.00 USD | 18,840,000.00 USD | 25,820.00 USD | 7,100.00 USD | 27,730.00 USD |
| `7D` | `51.30` | 18,780,000.00 USD | 0.00 USD | 18,780,000.00 USD | 17,810.00 USD | 12,490.00 USD | 47,090.00 USD |
| `7D` | `51.40` | 18,700,000.00 USD | 0.00 USD | 18,700,000.00 USD | 69,290.00 USD | 28,960.00 USD | 45,150.00 USD |
| `7D` | `51.50` | 18,560,000.00 USD | 0.00 USD | 18,560,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD |
| `7D` | `51.60` | 18,470,000.00 USD | 0.00 USD | 18,470,000.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD |
| `1D` | `51.70` | 6,240,000.00 USD | 0.00 USD | 6,240,000.00 USD | 10,880.00 USD | 11,120.00 USD | 11,300.00 USD |
| `7D` | `51.70` | 18,400,000.00 USD | 0.00 USD | 18,400,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `51.80` | 6,210,000.00 USD | 0.00 USD | 6,210,000.00 USD | 6,440.00 USD | 1,820.00 USD | 9,990.00 USD |
| `7D` | `51.80` | 18,370,000.00 USD | 0.00 USD | 18,370,000.00 USD | 22,510.00 USD | 12,820.00 USD | 19,510.00 USD |
| `1D` | `51.90` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 10,280.00 USD | 20,560.00 USD | 9,190.00 USD |
| `7D` | `51.90` | 18,310,000.00 USD | 0.00 USD | 18,310,000.00 USD | 5,870.00 USD | 15,810.00 USD | 4,760.00 USD |
| `1D` | `52.00` | 6,150,000.00 USD | 0.00 USD | 6,150,000.00 USD | 23,100.00 USD | 7,230.00 USD | 21,130.00 USD |
| `7D` | `52.00` | 18,280,000.00 USD | 0.00 USD | 18,280,000.00 USD | 64,300.00 USD | 17,390.00 USD | 11,880.00 USD |
| `1D` | `52.10` | 6,100,000.00 USD | 0.00 USD | 6,100,000.00 USD | 27,410.00 USD | 6,070.00 USD | 30,810.00 USD |
| `7D` | `52.10` | 18,190,000.00 USD | 0.00 USD | 18,190,000.00 USD | 24,220.00 USD | 18,810.00 USD | 21,910.00 USD |
| `1D` | `52.20` | 6,030,000.00 USD | 0.00 USD | 6,030,000.00 USD | 23,560.00 USD | 10,410.00 USD | 14,490.00 USD |
| `7D` | `52.20` | 18,130,000.00 USD | 0.00 USD | 18,130,000.00 USD | 35,740.00 USD | 4,340.00 USD | 25,270.00 USD |
| `1D` | `52.30` | 5,990,000.00 USD | 0.00 USD | 5,990,000.00 USD | 34,020.00 USD | 12,920.00 USD | 16,110.00 USD |
| `7D` | `52.30` | 18,060,000.00 USD | 0.00 USD | 18,060,000.00 USD | 14,070.00 USD | 12,840.00 USD | 8,940.00 USD |
| `1D` | `52.40` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 7,880.00 USD | 10,970.00 USD | 6,280.00 USD |
| `7D` | `52.40` | 18,030,000.00 USD | 0.00 USD | 18,030,000.00 USD | 20,580.00 USD | 11,230.00 USD | 20,050.00 USD |
| `1D` | `52.50` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 13,740.00 USD | 7,370.00 USD | 158.87 USD |
| `7D` | `52.50` | 17,970,000.00 USD | 0.00 USD | 17,970,000.00 USD | 33,240.00 USD | 667.05 USD | 10,640.00 USD |
| `1D` | `52.60` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 2,760.00 USD | 13,230.00 USD | 6,220.00 USD |
| `7D` | `52.60` | 17,930,000.00 USD | 0.00 USD | 17,930,000.00 USD | 36,640.00 USD | 14,530.00 USD | 584.77 USD |
| `1D` | `52.70` | 5,850,000.00 USD | 0.00 USD | 5,850,000.00 USD | 18,580.00 USD | 8,600.00 USD | 23,040.00 USD |
| `7D` | `52.70` | 17,880,000.00 USD | 0.00 USD | 17,880,000.00 USD | 20,660.00 USD | 27,720.00 USD | 42,430.00 USD |
| `1D` | `52.80` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 18,390.00 USD | 2,680.00 USD | 11,200.00 USD |
| `7D` | `52.80` | 17,790,000.00 USD | 0.00 USD | 17,790,000.00 USD | 47,130.00 USD | 17,020.00 USD | 108.50 USD |
| `1D` | `52.90` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 28,470.00 USD | 2,430.00 USD | 6,120.00 USD |
| `7D` | `52.90` | 17,720,000.00 USD | 0.00 USD | 17,720,000.00 USD | 51,920.00 USD | 23,030.00 USD | 3,870.00 USD |
| `1D` | `53.00` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 3,880.00 USD | 2,200.00 USD | 1,010.00 USD |
| `7D` | `53.00` | 17,640,000.00 USD | 0.00 USD | 17,640,000.00 USD | 19,580.00 USD | 8,880.00 USD | 32,670.00 USD |
| `1D` | `53.10` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 9,600.00 USD | 2,780.00 USD | 882.41 USD |
| `7D` | `53.10` | 17,580,000.00 USD | 0.00 USD | 17,580,000.00 USD | 51,920.00 USD | 29,200.00 USD | 9,860.00 USD |
| `1D` | `53.20` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 11,160.00 USD | 8,090.00 USD | 6,480.00 USD |
| `7D` | `53.20` | 17,490,000.00 USD | 0.00 USD | 17,490,000.00 USD | 90,340.00 USD | 17,580.00 USD | 25,530.00 USD |
| `1D` | `53.30` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 10,170.00 USD | 4,410.00 USD | 9,870.00 USD |
| `7D` | `53.30` | 17,360,000.00 USD | 0.00 USD | 17,360,000.00 USD | 63,050.00 USD | 14,250.00 USD | 37,140.00 USD |
| `1D` | `53.40` | 5,660,000.00 USD | 0.00 USD | 5,660,000.00 USD | 24,480.00 USD | 4,490.00 USD | 14,390.00 USD |
| `7D` | `53.40` | 17,240,000.00 USD | 0.00 USD | 17,240,000.00 USD | 49,250.00 USD | 4,350.00 USD | 48,070.00 USD |
| `1D` | `53.50` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 9,130.00 USD | 2,350.00 USD | 83.29 USD |
| `7D` | `53.50` | 17,140,000.00 USD | 0.00 USD | 17,140,000.00 USD | 50,210.00 USD | 13,810.00 USD | 22,130.00 USD |
| `1D` | `53.60` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 19,360.00 USD | 5,030.00 USD | 10,180.00 USD |
| `7D` | `53.60` | 17,060,000.00 USD | 0.00 USD | 17,060,000.00 USD | 51,280.00 USD | 8,450.00 USD | 10,670.00 USD |
| `1D` | `53.70` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 4,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `53.70` | 16,980,000.00 USD | 0.00 USD | 16,980,000.00 USD | 64,150.00 USD | 15,090.00 USD | 12,040.00 USD |
| `1D` | `53.80` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 1,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `53.80` | 16,890,000.00 USD | 0.00 USD | 16,890,000.00 USD | 99,150.00 USD | 48,300.00 USD | 86,270.00 USD |
| `1D` | `53.90` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 6,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `53.90` | 16,660,000.00 USD | 0.00 USD | 16,660,000.00 USD | 111,970.00 USD | 25,310.00 USD | 123,850.00 USD |
| `1D` | `54.00` | 5,560,000.00 USD | 0.00 USD | 5,560,000.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.00` | 16,400,000.00 USD | 0.00 USD | 16,400,000.00 USD | 344,710.00 USD | 142,130.00 USD | 210,440.00 USD |
| `1D` | `54.10` | 5,560,000.00 USD | 0.00 USD | 5,560,000.00 USD | 11,440.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.10` | 15,700,000.00 USD | 0.00 USD | 15,700,000.00 USD | 232,410.00 USD | 45,470.00 USD | 138,110.00 USD |
| `1D` | `54.20` | 5,550,000.00 USD | 0.00 USD | 5,550,000.00 USD | 15,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.20` | 15,290,000.00 USD | 0.00 USD | 15,290,000.00 USD | 234,980.00 USD | 141,240.00 USD | 133,320.00 USD |
| `1D` | `54.30` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 4,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.30` | 14,780,000.00 USD | 0.00 USD | 14,780,000.00 USD | 245,850.00 USD | 89,080.00 USD | 257,030.00 USD |
| `1D` | `54.40` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 2,750.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.40` | 14,180,000.00 USD | 0.00 USD | 14,180,000.00 USD | 319,640.00 USD | 106,460.00 USD | 105,880.00 USD |
| `1D` | `54.50` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 2,500.00 USD | 126.10 USD | 0.00 USD |
| `7D` | `54.50` | 13,650,000.00 USD | 0.00 USD | 13,650,000.00 USD | 169,910.00 USD | 53,460.00 USD | 142,750.00 USD |
| `1D` | `54.60` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 3,300.00 USD | 601.45 USD | 944.92 USD |
| `7D` | `54.60` | 13,290,000.00 USD | 0.00 USD | 13,290,000.00 USD | 108,280.00 USD | 43,430.00 USD | 73,330.00 USD |
| `1D` | `54.70` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 51,940.00 USD | 15,810.00 USD | 52,670.00 USD |
| `7D` | `54.70` | 13,060,000.00 USD | 0.00 USD | 13,060,000.00 USD | 123,210.00 USD | 50,560.00 USD | 172,060.00 USD |
| `1D` | `54.80` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 47,390.00 USD | 18,410.00 USD | 26,940.00 USD |
| `7D` | `54.80` | 12,710,000.00 USD | 0.00 USD | 12,710,000.00 USD | 309,200.00 USD | 104,820.00 USD | 156,690.00 USD |
| `1D` | `54.90` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 52,180.00 USD | 21,230.00 USD | 5,570.00 USD |
| `7D` | `54.90` | 12,140,000.00 USD | 0.00 USD | 12,140,000.00 USD | 257,210.00 USD | 162,220.00 USD | 276,830.00 USD |
| `1D` | `55.00` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 38,800.00 USD | 24,110.00 USD | 12,080.00 USD |
| `7D` | `55.00` | 11,450,000.00 USD | 0.00 USD | 11,450,000.00 USD | 269,610.00 USD | 81,220.00 USD | 310,900.00 USD |
| `1D` | `55.10` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 26,630.00 USD | 10,460.00 USD | 18,380.00 USD |
| `7D` | `55.10` | 10,790,000.00 USD | 0.00 USD | 10,790,000.00 USD | 362,320.00 USD | 145,730.00 USD | 171,990.00 USD |
| `1D` | `55.20` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 19,810.00 USD | 4,030.00 USD | 10,700.00 USD |
| `7D` | `55.20` | 10,110,000.00 USD | 0.00 USD | 10,110,000.00 USD | 338,950.00 USD | 177,110.00 USD | 279,820.00 USD |
| `1D` | `55.30` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 12,080.00 USD | 5,120.00 USD | 18,370.00 USD |
| `7D` | `55.30` | 9,310,000.00 USD | 0.00 USD | 9,310,000.00 USD | 367,680.00 USD | 68,970.00 USD | 256,220.00 USD |
| `1D` | `55.40` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 29,970.00 USD | 57,700.00 USD | 25,370.00 USD |
| `7D` | `55.40` | 8,620,000.00 USD | 0.00 USD | 8,620,000.00 USD | 302,780.00 USD | 188,590.00 USD | 237,150.00 USD |
| `1D` | `55.50` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 70,830.00 USD | 25,990.00 USD | 61,320.00 USD |
| `7D` | `55.50` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 329,130.00 USD | 178,270.00 USD | 529,720.00 USD |
| `1D` | `55.60` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 97,100.00 USD | 21,410.00 USD | 82,110.00 USD |
| `7D` | `55.60` | 6,850,000.00 USD | 0.00 USD | 6,850,000.00 USD | 426,340.00 USD | 261,500.00 USD | 243,460.00 USD |
| `1D` | `55.70` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 90,090.00 USD | 49,390.00 USD | 47,990.00 USD |
| `7D` | `55.70` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 174,240.00 USD | 32,180.00 USD | 273,340.00 USD |
| `1D` | `55.80` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 120,170.00 USD | 47,920.00 USD | 42,220.00 USD |
| `7D` | `55.80` | 5,440,000.00 USD | 0.00 USD | 5,440,000.00 USD | 60,840.00 USD | 54,060.00 USD | 144,450.00 USD |
| `1D` | `55.90` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 116,440.00 USD | 62,020.00 USD | 130,300.00 USD |
| `7D` | `55.90` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 65,400.00 USD | 94,580.00 USD | 280,140.00 USD |
| `1D` | `56.00` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 125,000.00 USD | 60,260.00 USD | 56,270.00 USD |
| `7D` | `56.00` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 181,230.00 USD | 88,840.00 USD | 107,640.00 USD |
| `1D` | `56.10` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 98,040.00 USD | 77,440.00 USD | 26,680.00 USD |
| `7D` | `56.10` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 121,920.00 USD | 133,900.00 USD | 46,880.00 USD |
| `1D` | `56.20` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 73,120.00 USD | 60,830.00 USD | 87,150.00 USD |
| `7D` | `56.20` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 104,510.00 USD | 80,130.00 USD | 205,740.00 USD |
| `1D` | `56.30` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 77,950.00 USD | 44,480.00 USD | 65,840.00 USD |
| `7D` | `56.30` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 91,850.00 USD | 140,830.00 USD | 85,420.00 USD |
| `1D` | `56.40` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 185,180.00 USD | 35,450.00 USD | 122,450.00 USD |
| `7D` | `56.40` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 215,940.00 USD | 124,050.00 USD | 139,370.00 USD |
| `1D` | `56.50` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 69,340.00 USD | 122,360.00 USD | 53,280.00 USD |
| `7D` | `56.50` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 26,520.00 USD | 101,420.00 USD | 47,880.00 USD |
| `1D` | `56.60` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 161,590.00 USD | 60,330.00 USD | 124,840.00 USD |
| `7D` | `56.60` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 363,190.00 USD | 113,010.00 USD | 128,320.00 USD |
| `1D` | `56.70` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 204,190.00 USD | 65,860.00 USD | 190,800.00 USD |
| `7D` | `56.70` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 110,940.00 USD | 105,810.00 USD | 138,660.00 USD |
| `1D` | `56.80` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 189,690.00 USD | 111,830.00 USD | 122,250.00 USD |
| `7D` | `56.80` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 153,580.00 USD | 97,670.00 USD | 262,620.00 USD |
| `1D` | `56.90` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 299,280.00 USD | 94,950.00 USD | 119,830.00 USD |
| `7D` | `56.90` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 108,440.00 USD | 65,260.00 USD | 94,810.00 USD |
| `1D` | `57.00` | 658,180.00 USD | 0.00 USD | 658,180.00 USD | 34,380.00 USD | 24,060.00 USD | 44,710.00 USD |
| `7D` | `57.00` | 954,870.00 USD | 0.00 USD | 954,870.00 USD | 50,710.00 USD | 111,780.00 USD | 91,400.00 USD |
| `1D` | `57.10` | 555,030.00 USD | 0.00 USD | 555,030.00 USD | 73,260.00 USD | 25,570.00 USD | 4,390.00 USD |
| `7D` | `57.10` | 700,980.00 USD | 0.00 USD | 700,980.00 USD | 36,580.00 USD | 14,880.00 USD | 500.18 USD |
| `1D` | `57.20` | 451,820.00 USD | 0.00 USD | 451,820.00 USD | 27,530.00 USD | 40,100.00 USD | 256.90 USD |
| `7D` | `57.20` | 649,020.00 USD | 0.00 USD | 649,020.00 USD | 21,160.00 USD | 50,300.00 USD | 3,700.00 USD |
| `1D` | `57.30` | 383,930.00 USD | 0.00 USD | 383,930.00 USD | 0.00 USD | 15,520.00 USD | 51,900.00 USD |
| `7D` | `57.30` | 573,870.00 USD | 0.00 USD | 573,870.00 USD | 22,360.00 USD | 27,320.00 USD | 45,530.00 USD |
| `1D` | `57.40` | 316,500.00 USD | 0.00 USD | 316,500.00 USD | 19,650.00 USD | 26,470.00 USD | 1,340.00 USD |
| `7D` | `57.40` | 478,660.00 USD | 0.00 USD | 478,660.00 USD | 38,520.00 USD | 30,000.00 USD | 129,940.00 USD |
| `1D` | `57.50` | 269,040.00 USD | 0.00 USD | 269,040.00 USD | 80,510.00 USD | 12,870.00 USD | 36,850.00 USD |
| `7D` | `57.50` | 280,200.00 USD | 0.00 USD | 280,200.00 USD | 76,670.00 USD | 23,070.00 USD | 68,890.00 USD |
| `1D` | `57.60` | 138,820.00 USD | 0.00 USD | 138,820.00 USD | 138,820.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `57.60` | 111,570.00 USD | 0.00 USD | 111,570.00 USD | 70,040.00 USD | 15,090.00 USD | 26,440.00 USD |
| `1D` | `57.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `57.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `58.20` | 638.03 USD | 638.03 USD | 0.00 USD | 0.00 USD | 0.00 USD | 638.03 USD |
| `1D` | `58.40` | 24,790.00 USD | 24,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,150.00 USD |
| `7D` | `58.40` | 54,120.00 USD | 54,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 54,120.00 USD |
| `1D` | `58.50` | 94,790.00 USD | 94,790.00 USD | 0.00 USD | 48,820.00 USD | 20,920.00 USD | 255.20 USD |
| `7D` | `58.50` | 78,650.00 USD | 78,650.00 USD | 0.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD |
| `1D` | `58.70` | 102,850.00 USD | 102,850.00 USD | 0.00 USD | 0.00 USD | 8,070.00 USD | 0.00 USD |
| `7D` | `58.70` | 118,400.00 USD | 118,400.00 USD | 0.00 USD | 0.00 USD | 4,430.00 USD | 35,320.00 USD |
| `1D` | `58.80` | 125,050.00 USD | 125,050.00 USD | 0.00 USD | 0.00 USD | 10,240.00 USD | 11,960.00 USD |
| `7D` | `58.80` | 127,280.00 USD | 127,280.00 USD | 0.00 USD | 0.00 USD | 3,320.00 USD | 5,560.00 USD |
| `1D` | `58.90` | 291,210.00 USD | 291,210.00 USD | 0.00 USD | 0.00 USD | 115,410.00 USD | 50,750.00 USD |
| `7D` | `58.90` | 206,140.00 USD | 206,140.00 USD | 0.00 USD | 0.00 USD | 47,950.00 USD | 30,910.00 USD |
| `1D` | `59.00` | 607,480.00 USD | 607,480.00 USD | 0.00 USD | 141,660.00 USD | 51,970.00 USD | 122,640.00 USD |
| `7D` | `59.00` | 628,090.00 USD | 628,090.00 USD | 0.00 USD | 255,180.00 USD | 48,210.00 USD | 118,570.00 USD |
| `1D` | `59.10` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 189,650.00 USD | 41,340.00 USD | 164,220.00 USD |
| `7D` | `59.10` | 854,730.00 USD | 854,730.00 USD | 0.00 USD | 91,060.00 USD | 45,400.00 USD | 90,180.00 USD |
| `1D` | `59.20` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 149,140.00 USD | 72,500.00 USD | 96,020.00 USD |
| `7D` | `59.20` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 153,580.00 USD | 10,620.00 USD | 174,600.00 USD |
| `1D` | `59.30` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 283,630.00 USD | 73,090.00 USD | 133,320.00 USD |
| `7D` | `59.30` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD |
| `1D` | `59.40` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 78,510.00 USD | 56,810.00 USD | 76,850.00 USD |
| `7D` | `59.40` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 103,370.00 USD | 73,620.00 USD | 137,500.00 USD |
| `1D` | `59.50` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 114,880.00 USD | 51,920.00 USD | 9,950.00 USD |
| `7D` | `59.50` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 67,060.00 USD | 59,920.00 USD | 7,680.00 USD |
| `1D` | `59.60` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 62,260.00 USD | 66,510.00 USD | 13,440.00 USD |
| `7D` | `59.60` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 268,680.00 USD | 145,550.00 USD | 86,840.00 USD |
| `1D` | `59.70` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 20,820.00 USD | 35,670.00 USD | 94,060.00 USD |
| `7D` | `59.70` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 53,810.00 USD | 180,620.00 USD | 161,880.00 USD |
| `1D` | `59.80` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 100,280.00 USD | 51,160.00 USD | 68,860.00 USD |
| `7D` | `59.80` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 118,240.00 USD | 96,860.00 USD | 155,270.00 USD |
| `1D` | `59.90` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 113,050.00 USD | 26,580.00 USD | 84,220.00 USD |
| `7D` | `59.90` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 246,770.00 USD | 98,620.00 USD | 39,700.00 USD |
| `1D` | `60.00` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 226,310.00 USD | 70,520.00 USD | 88,150.00 USD |
| `7D` | `60.00` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 231,370.00 USD | 183,130.00 USD | 82,190.00 USD |
| `1D` | `60.10` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 98,470.00 USD | 39,900.00 USD | 66,380.00 USD |
| `7D` | `60.10` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 263,890.00 USD | 122,370.00 USD | 174,140.00 USD |
| `1D` | `60.20` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 136,940.00 USD | 38,140.00 USD | 86,520.00 USD |
| `7D` | `60.20` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 207,990.00 USD | 131,530.00 USD | 123,230.00 USD |
| `1D` | `60.30` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 113,360.00 USD | 95,210.00 USD | 101,150.00 USD |
| `7D` | `60.30` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 118,160.00 USD | 95,890.00 USD | 155,610.00 USD |
| `1D` | `60.40` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 164,430.00 USD | 73,810.00 USD | 92,850.00 USD |
| `7D` | `60.40` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 89,500.00 USD | 126,870.00 USD | 226,430.00 USD |
| `1D` | `60.50` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 147,700.00 USD | 56,930.00 USD | 104,230.00 USD |
| `7D` | `60.50` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 160,180.00 USD | 89,250.00 USD | 207,360.00 USD |
| `1D` | `60.60` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 78,970.00 USD | 40,280.00 USD | 6,040.00 USD |
| `7D` | `60.60` | 6,930,000.00 USD | 6,930,000.00 USD | 0.00 USD | 294,830.00 USD | 109,510.00 USD | 167,360.00 USD |
| `1D` | `60.70` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 84,870.00 USD | 58,850.00 USD | 48,530.00 USD |
| `7D` | `60.70` | 7,180,000.00 USD | 7,180,000.00 USD | 0.00 USD | 142,880.00 USD | 79,060.00 USD | 28,990.00 USD |
| `1D` | `60.80` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 45,710.00 USD | 15,720.00 USD | 90,940.00 USD |
| `7D` | `60.80` | 7,410,000.00 USD | 7,410,000.00 USD | 0.00 USD | 54,870.00 USD | 78,710.00 USD | 94,850.00 USD |
| `1D` | `60.90` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 72,210.00 USD | 25,460.00 USD | 33,550.00 USD |
| `7D` | `60.90` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 139,720.00 USD | 52,860.00 USD | 92,420.00 USD |
| `1D` | `61.00` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 55,630.00 USD | 10,730.00 USD | 32,920.00 USD |
| `7D` | `61.00` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 96,160.00 USD | 43,600.00 USD | 5,370.00 USD |
| `1D` | `61.10` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 5,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `61.10` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 31,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `61.20` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 100,130.00 USD | 6,410.00 USD | 31,390.00 USD |
| `7D` | `61.20` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 116,610.00 USD | 70,180.00 USD | 33,350.00 USD |
| `1D` | `61.30` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 13,090.00 USD | 6,960.00 USD | 2,530.00 USD |
| `7D` | `61.30` | 8,240,000.00 USD | 8,240,000.00 USD | 0.00 USD | 51,130.00 USD | 36,170.00 USD | 55,130.00 USD |
| `1D` | `61.40` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 23,410.00 USD | 8,360.00 USD | 2,210.00 USD |
| `7D` | `61.40` | 8,390,000.00 USD | 8,390,000.00 USD | 0.00 USD | 87,050.00 USD | 41,800.00 USD | 24,650.00 USD |
| `1D` | `61.50` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 20,390.00 USD | 23,040.00 USD | 26,580.00 USD |
| `7D` | `61.50` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 21,320.00 USD | 34,770.00 USD | 35,770.00 USD |
| `1D` | `61.60` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 25,020.00 USD | 13,550.00 USD | 26,260.00 USD |
| `7D` | `61.60` | 8,730,000.00 USD | 8,730,000.00 USD | 0.00 USD | 56,380.00 USD | 63,390.00 USD | 132,550.00 USD |
| `1D` | `61.70` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 70,350.00 USD | 13,270.00 USD | 39,640.00 USD |
| `7D` | `61.70` | 8,960,000.00 USD | 8,960,000.00 USD | 0.00 USD | 100,140.00 USD | 15,950.00 USD | 114,970.00 USD |
| `1D` | `61.80` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 23,150.00 USD | 8,420.00 USD | 1,830.00 USD |
| `7D` | `61.80` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 185,050.00 USD | 68,030.00 USD | 92,510.00 USD |
| `1D` | `61.90` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 36,420.00 USD | 11,940.00 USD | 16,490.00 USD |
| `7D` | `61.90` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 79,630.00 USD | 35,500.00 USD | 35,860.00 USD |
| `1D` | `62.00` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 22,240.00 USD | 1,560.00 USD | 13,970.00 USD |
| `7D` | `62.00` | 9,580,000.00 USD | 9,580,000.00 USD | 0.00 USD | 57,760.00 USD | 13,260.00 USD | 49,920.00 USD |
| `1D` | `62.10` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 12,050.00 USD | 945.47 USD | 2,230.00 USD |
| `7D` | `62.10` | 9,640,000.00 USD | 9,640,000.00 USD | 0.00 USD | 36,500.00 USD | 12,820.00 USD | 13,950.00 USD |
| `1D` | `62.20` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 4,170.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.20` | 9,760,000.00 USD | 9,760,000.00 USD | 0.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD |
| `1D` | `62.30` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 464.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.30` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 38,120.00 USD | 23,450.00 USD | 85,980.00 USD |
| `1D` | `62.40` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 3,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.40` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 81,060.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `62.50` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 4,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.50` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 45,440.00 USD | 14,320.00 USD | 26,310.00 USD |
| `1D` | `62.60` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 2,090.00 USD | 0.00 USD | 327.72 USD |
| `7D` | `62.60` | 10,200,000.00 USD | 10,200,000.00 USD | 0.00 USD | 35,940.00 USD | 7,100.00 USD | 27,730.00 USD |
| `1D` | `62.70` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 17,140.00 USD | 4,920.00 USD | 18,640.00 USD |
| `7D` | `62.70` | 10,290,000.00 USD | 10,290,000.00 USD | 0.00 USD | 22,860.00 USD | 12,490.00 USD | 47,090.00 USD |
| `1D` | `62.80` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 16,330.00 USD | 7,010.00 USD | 10,780.00 USD |
| `7D` | `62.80` | 10,430,000.00 USD | 10,430,000.00 USD | 0.00 USD | 74,100.00 USD | 28,960.00 USD | 45,150.00 USD |
| `1D` | `62.90` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 8,780.00 USD | 6,670.00 USD | 63.10 USD |
| `7D` | `62.90` | 10,530,000.00 USD | 10,530,000.00 USD | 0.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `63.00` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 7,650.00 USD | 7,040.00 USD | 4,820.00 USD |
| `7D` | `63.00` | 10,590,000.00 USD | 10,590,000.00 USD | 0.00 USD | 35,710.00 USD | 12,240.00 USD | 17,650.00 USD |
| `1D` | `63.10` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 3,990.00 USD | 4,070.00 USD | 6,480.00 USD |
| `7D` | `63.10` | 10,630,000.00 USD | 10,630,000.00 USD | 0.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `63.20` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 2,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `63.30` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 4,440.00 USD | 594.25 USD | 2,730.00 USD |
| `7D` | `63.30` | 10,670,000.00 USD | 10,670,000.00 USD | 0.00 USD | 20,280.00 USD | 11,500.00 USD | 9,730.00 USD |
| `1D` | `63.40` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 3,520.00 USD | 1,230.00 USD | 7,260.00 USD |
| `7D` | `63.40` | 10,700,000.00 USD | 10,700,000.00 USD | 0.00 USD | 14,300.00 USD | 1,320.00 USD | 9,790.00 USD |
| `1D` | `63.50` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 10,280.00 USD | 20,560.00 USD | 9,190.00 USD |
| `7D` | `63.50` | 10,730,000.00 USD | 10,730,000.00 USD | 0.00 USD | 6,620.00 USD | 15,810.00 USD | 4,760.00 USD |
| `1D` | `63.60` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 23,100.00 USD | 7,230.00 USD | 21,130.00 USD |
| `7D` | `63.60` | 10,820,000.00 USD | 10,820,000.00 USD | 0.00 USD | 63,480.00 USD | 17,390.00 USD | 11,880.00 USD |
| `1D` | `63.70` | 6,370,000.00 USD | 6,370,000.00 USD | 0.00 USD | 28,180.00 USD | 6,070.00 USD | 30,810.00 USD |
| `7D` | `63.70` | 10,880,000.00 USD | 10,880,000.00 USD | 0.00 USD | 21,940.00 USD | 18,810.00 USD | 21,910.00 USD |
| `1D` | `63.80` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 23,560.00 USD | 10,410.00 USD | 14,490.00 USD |
| `7D` | `63.80` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD |
| `1D` | `63.90` | 6,480,000.00 USD | 6,480,000.00 USD | 0.00 USD | 34,020.00 USD | 12,920.00 USD | 16,110.00 USD |
| `7D` | `63.90` | 10,970,000.00 USD | 10,970,000.00 USD | 0.00 USD | 7,650.00 USD | 12,840.00 USD | 8,940.00 USD |
| `1D` | `64.00` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 7,880.00 USD | 10,970.00 USD | 6,280.00 USD |
| `7D` | `64.00` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD |
| `1D` | `64.10` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 13,740.00 USD | 7,370.00 USD | 158.87 USD |
| `7D` | `64.10` | 11,050,000.00 USD | 11,050,000.00 USD | 0.00 USD | 20,350.00 USD | 667.05 USD | 10,640.00 USD |
| `1D` | `64.20` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 2,760.00 USD | 13,230.00 USD | 6,220.00 USD |
| `7D` | `64.20` | 11,090,000.00 USD | 11,090,000.00 USD | 0.00 USD | 28,840.00 USD | 14,530.00 USD | 584.77 USD |
| `1D` | `64.40` | 6,560,000.00 USD | 6,560,000.00 USD | 0.00 USD | 1,140.00 USD | 1,940.00 USD | 13,680.00 USD |
| `7D` | `64.40` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 2,540.00 USD | 20,590.00 USD | 29,110.00 USD |
| `1D` | `64.50` | 6,600,000.00 USD | 6,600,000.00 USD | 0.00 USD | 17,440.00 USD | 6,670.00 USD | 9,360.00 USD |
| `7D` | `64.50` | 11,170,000.00 USD | 11,170,000.00 USD | 0.00 USD | 8,110.00 USD | 7,120.00 USD | 13,310.00 USD |
| `1D` | `64.60` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 18,390.00 USD | 2,680.00 USD | 11,200.00 USD |
| `7D` | `64.60` | 11,220,000.00 USD | 11,220,000.00 USD | 0.00 USD | 32,750.00 USD | 17,020.00 USD | 108.50 USD |
| `1D` | `64.70` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 28,470.00 USD | 2,430.00 USD | 6,120.00 USD |
| `7D` | `64.70` | 11,290,000.00 USD | 11,290,000.00 USD | 0.00 USD | 39,430.00 USD | 23,030.00 USD | 3,870.00 USD |
| `1D` | `64.80` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 3,880.00 USD | 2,200.00 USD | 1,010.00 USD |
| `7D` | `64.80` | 11,330,000.00 USD | 11,330,000.00 USD | 0.00 USD | 8,140.00 USD | 8,210.00 USD | 20,430.00 USD |
| `1D` | `64.90` | 6,680,000.00 USD | 6,680,000.00 USD | 0.00 USD | 6,320.00 USD | 2,780.00 USD | 669.73 USD |
| `7D` | `64.90` | 11,370,000.00 USD | 11,370,000.00 USD | 0.00 USD | 25,750.00 USD | 8,010.00 USD | 9,860.00 USD |
| `1D` | `65.00` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 4,580.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `65.00` | 11,390,000.00 USD | 11,390,000.00 USD | 0.00 USD | 0.00 USD | 9,480.00 USD | 13,480.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `455.58M` | Total OI Tokens: `7,828,872.8 LTC`
  * 1h OI Change: `-0.75%` | 4h OI Change: `+0.10%` | 24h OI Change: `-2.62%`
  * Exchange Breakdown: Binance=`82.78M` | Bybit=`70.09M` | OKX=`35.14M` | Hyperliquid=`23.03M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `17.06K` | Last 24h: `36.85K` | Last 3d: `60.07K` | Last 7d: `106.71K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `59.36%` | `40.64%` | `1.46` | 3,400,000.00 USD |
| `15M` | `Binance` | `53.86%` | `46.14%` | `1.17` | 1,110,000.00 USD |
| `15M` | `OKX` | `66.09%` | `33.91%` | `1.95` | 271,150.00 USD |
| `15M` | `Bybit` | `55.37%` | `44.63%` | `1.24` | 281,820.00 USD |
| `15M` | `KuCoin` | `71.89%` | `28.11%` | `2.56` | 22,210.00 USD |
| `15M` | `Gate` | `51.32%` | `48.68%` | `1.05` | 498,150.00 USD |
| `15M` | `Bitget` | `58.98%` | `41.02%` | `1.44` | 77,450.00 USD |
| `15M` | `BingX` | `51.64%` | `48.36%` | `1.07` | 508,300.00 USD |
| `15M` | `MEXC` | `43.44%` | `56.56%` | `0.77` | 126,560.00 USD |
| `15M` | `Bitunix` | `55.72%` | `44.28%` | `1.26` | 45,160.00 USD |
| `15M` | `Hyperliquid` | `76.63%` | `23.37%` | `3.28` | 10,620.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `53.81%` | `46.19%` | `1.16` | 33,580.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `99.36%` | `0.64%` | `155.25` | 396,830.00 USD |
| `15M` | `HTX` | `32.8%` | `67.2%` | `0.49` | 2,970.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `85.66%` | `14.34%` | `5.97` | 5,480.00 USD |
| `15M` | `Aster` | `93.73%` | `6.27%` | `14.95` | 4,480.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0.59%` | `99.41%` | `0.01` | 14,140.00 USD |
| `15M` | `Whale Positions` | `53.86%` | `46.14%` | `1.17` | 1,110,000.00 USD |
| `15M` | `Global Accounts` | `59.36%` | `40.64%` | `1.46` | 3,400,000.00 USD |
| `1H` | `LTC` | `51.53%` | `48.47%` | `1.06` | 12,780,000.00 USD |
| `1H` | `Binance` | `47.21%` | `52.79%` | `0.89` | 3,440,000.00 USD |
| `1H` | `OKX` | `47.83%` | `52.17%` | `0.92` | 1,280,000.00 USD |
| `1H` | `Bybit` | `42.32%` | `57.68%` | `0.73` | 1,070,000.00 USD |
| `1H` | `KuCoin` | `40.05%` | `59.95%` | `0.67` | 135,730.00 USD |
| `1H` | `Gate` | `50.52%` | `49.48%` | `1.02` | 1,660,000.00 USD |
| `1H` | `Bitget` | `59.72%` | `40.28%` | `1.48` | 227,240.00 USD |
| `1H` | `BingX` | `44.31%` | `55.69%` | `0.80` | 2,390,000.00 USD |
| `1H` | `MEXC` | `43.73%` | `56.27%` | `0.78` | 560,720.00 USD |
| `1H` | `Bitunix` | `45.25%` | `54.75%` | `0.83` | 170,660.00 USD |
| `1H` | `Hyperliquid` | `37.1%` | `62.9%` | `0.59` | 87,390.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.27%` | `50.73%` | `0.97` | 378,840.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `98.63%` | `1.37%` | `71.99` | 1,250,000.00 USD |
| `1H` | `HTX` | `33.19%` | `66.81%` | `0.50` | 53,450.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `36.86%` | `63.14%` | `0.58` | 31,610.00 USD |
| `1H` | `Aster` | `58.97%` | `41.03%` | `1.44` | 7,600.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0.39%` | `99.61%` | `0.00` | 28,830.00 USD |
| `1H` | `Whale Positions` | `47.21%` | `52.79%` | `0.89` | 3,440,000.00 USD |
| `1H` | `Global Accounts` | `51.53%` | `48.47%` | `1.06` | 12,780,000.00 USD |
| `4H` | `LTC` | `53.21%` | `46.79%` | `1.14` | 63,670,000.00 USD |
| `4H` | `Binance` | `48.52%` | `51.48%` | `0.94` | 19,740,000.00 USD |
| `4H` | `OKX` | `49.68%` | `50.32%` | `0.99` | 7,490,000.00 USD |
| `4H` | `Bybit` | `53.83%` | `46.17%` | `1.17` | 4,990,000.00 USD |
| `4H` | `KuCoin` | `45.13%` | `54.87%` | `0.82` | 520,990.00 USD |
| `4H` | `Gate` | `49.44%` | `50.56%` | `0.98` | 8,470,000.00 USD |
| `4H` | `Bitget` | `43.51%` | `56.49%` | `0.77` | 1,280,000.00 USD |
| `4H` | `BingX` | `46.49%` | `53.51%` | `0.87` | 9,460,000.00 USD |
| `4H` | `MEXC` | `50.64%` | `49.36%` | `1.03` | 1,600,000.00 USD |
| `4H` | `Bitunix` | `48.39%` | `51.61%` | `0.94` | 1,030,000.00 USD |
| `4H` | `Hyperliquid` | `55.06%` | `44.94%` | `1.23` | 399,700.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.4%` | `49.6%` | `1.02` | 2,400,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `96.25%` | `3.75%` | `25.67` | 5,720,000.00 USD |
| `4H` | `HTX` | `45.5%` | `54.5%` | `0.83` | 130,200.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `42.88%` | `57.12%` | `0.75` | 259,760.00 USD |
| `4H` | `Aster` | `66.9%` | `33.1%` | `2.02` | 118,140.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `31.24%` | `68.76%` | `0.45` | 51,980.00 USD |
| `4H` | `Whale Positions` | `48.52%` | `51.48%` | `0.94` | 19,740,000.00 USD |
| `4H` | `Global Accounts` | `53.21%` | `46.79%` | `1.14` | 63,670,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `58.56` | `58.55` | `58.56` | `58.69` | `58.45` | 786,561.16 USD | 351,968.92 USD | 434,592.24 USD | -82,623.32 USD | `-10.50%` | `1B / 7S` |
| `0:00 UTC` | `58.75` | `58.71` | `58.75` | `58.94` | `58.39` | 3,012,388.15 USD | 1,829,068.33 USD | 1,183,319.82 USD | 645,748.50 USD | `+21.44%` | `9B / 5S` |
| `5:00 UTC` | `58.62` | `58.67` | `58.62` | `58.89` | `58.47` | 1,800,374.76 USD | 710,155.53 USD | 1,090,219.24 USD | -380,063.71 USD | `-21.11%` | `7B / 10S` |
| `0:00 UTC` | `58.62` | `58.52` | `58.62` | `58.69` | `58.38` | 676,217.74 USD | 290,207.52 USD | 386,010.22 USD | -95,802.70 USD | `-14.17%` | `4B / 7S` |
| `5:00 UTC` | `58.47` | `58.42` | `58.47` | `58.53` | `58.31` | 694,681.39 USD | 374,631.67 USD | 320,049.71 USD | 54,581.96 USD | `+7.86%` | `5B / 5S` |
| `0:00 UTC` | `58.41` | `58.31` | `58.41` | `58.45` | `58.17` | 879,667.69 USD | 349,324.06 USD | 530,343.63 USD | -181,019.57 USD | `-20.58%` | `0B / 5S` |
| `5:00 UTC` | `58.17` | `58.19` | `58.17` | `58.30` | `58.09` | 458,580.74 USD | 259,697.75 USD | 198,882.99 USD | 60,814.77 USD | `+13.26%` | `2B / 2S` |
| `0:00 UTC` | `57.89` | `58.07` | `57.89` | `58.36` | `57.84` | 621,283.45 USD | 280,339.51 USD | 340,943.94 USD | -60,604.43 USD | `-9.75%` | `5B / 14S` |
| `5:00 UTC` | `57.58` | `57.64` | `57.58` | `57.91` | `57.50` | 1,187,641.81 USD | 478,923.89 USD | 708,717.92 USD | -229,794.02 USD | `-19.35%` | `2B / 11S` |
| `0:00 UTC` | `57.78` | `57.74` | `57.78` | `57.80` | `57.67` | 136,644.04 USD | 97,051.18 USD | 39,592.86 USD | 57,458.32 USD | `+42.05%` | `6B / 0S` |

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
| `5m` | 158,380.00 USD | -47,350.00 USD | **`ACCUMULATION`** |
| `15m` | 282,440.00 USD | 172,280.00 USD | **`ACCUMULATION`** |
| `30m` | 346,390.00 USD | -355,860.00 USD | **`DISTRIBUTION`** |
| `1h` | 432,800.00 USD | -398,170.00 USD | **`ACCUMULATION`** |
| `2h` | 839,160.00 USD | -266,950.00 USD | **`ACCUMULATION`** |
| `4h` | 1,970,000.00 USD | -332,140.00 USD | **`ACCUMULATION`** |
| `6h` | 1,900,000.00 USD | 1,340,000.00 USD | **`ACCUMULATION`** |
| `8h` | 2,580,000.00 USD | 2,290,000.00 USD | **`ACCUMULATION`** |
| `12h` | 2,790,000.00 USD | 3,370,000.00 USD | **`ACCUMULATION`** |
| `24h` | 2,090,000.00 USD | -4,010,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 5,900,000.00 USD | -19,490,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -19,750,000.00 USD | -188,730,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+158.38K` | 15m=`+282.44K` | 1h=`+432.80K` | 24h=`+2.09M`
* Futures Capital Netflows: 5m=`-47.35K` | 15m=`+172.28K` | 1h=`-398.17K` | 24h=`-4.01M`
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
  * `2026-10-29 23:31:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:35 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:35 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:35 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:35 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:35 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:35 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `56.98` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `56.13` (Risk Distance: `0.8571` pts)
  * +2.5R Take Profit: `59.13`
  * Mathematical Lot Sizing: **`11.66 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `58.52` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `59.38` (Risk Distance: `0.8571` pts)
  * +2.5R Take Profit: `56.38`
  * Mathematical Lot Sizing: **`11.66 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`58.25`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
