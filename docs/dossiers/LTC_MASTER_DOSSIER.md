# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 02:33:42 IST` (`2026-10-29 21:03:42 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `55.06` | **Live Ask Quote**: `55.37` | **Mid Price**: `55.22`
- **Spread Points**: `300.00` | **Spread BPS**: `54.33 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `57.69` | VWAP Z-Score: `-3.48` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.4776` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `21.50` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `59.81` | Lower -3.00σ Band: `55.58`
  * Upper +2.51σ Band: `59.46` | Lower -2.51σ Band: `55.92`
  * Upper +2.01σ Band: `59.11` | Lower -2.01σ Band: `56.27`
  * Upper +2.00σ Band: `59.10` | Lower -2.00σ Band: `56.28`
  * Upper +1.28σ Band: `58.59` | Lower -1.28σ Band: `56.79`
  * Upper +1.00σ Band: `58.40` | Lower -1.00σ Band: `56.99`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`57.02` | EMA-20=`57.41` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`57.62` (Slope: `+0.0000`) | EMA-100=`57.68`
  * Institutional Anchors: EMA-144=`57.62` | EMA-200=`57.43` (Slope: `-0.0309`) | EMA-233=`57.28`
- **Range Boundaries**: 24H High=`59.52` | 24H Low=`55.23` | Weekly High=`59.62` | Weekly Low=`55.23`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `58.36` (Distance: `-5.35%`)
  * Point of Control (POC) = `57.72` (Distance: `-4.30%`)
  * Value Area Low (VAL) = `56.83` (Distance: `-2.81%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.44` | POC=`57.22` | VAL=`56.70`
  * Prior Day Extremes: PDH=`59.62` | PDL=`56.37` | PDC=`58.69`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`57.79` | Weekly POC=`56.45` | Weekly VAL=`56.01`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`59.52` | Low=`56.73`
  * London Session (08:00-16:00 UTC): High=`58.12` | Low=`56.67`
  * New York Session (13:00-21:00 UTC): High=`58.72` | Low=`57.04`
  * Initial Balance (First Hour): IB High=`58.02` | IB Low=`57.29`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `54.99` - `55.44`
  * Optimal Trade Entry (OTE 0.705): `55.33`
  * Structural Invalidation Anchor (0.786): `55.66`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `55.42` | `55.49` | `54.17` | `54.90` | `139,304` | 7,642,527.81 USD | -2,076,440.50 USD | `-27.17%` | -4,394,465.22 USD | `-3.84` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `54.89` | `55.58` | `54.86` | `55.19` | `34,877` | 1,929,596.99 USD | 447,839.62 USD | `+23.21%` | -3,946,625.60 USD | `+1.18` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `55.18` | `55.27` | `55.14` | `55.23` | `1,956` | 108,012.28 USD | 9,520.86 USD | `+8.81%` | -3,937,104.73 USD | `+0.33` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `57.36` | `57.45` | `57.14` | `57.17` | `10,794` | 618,298.97 USD | 92,216.13 USD | `+14.91%` | -1,152,873.24 USD | `+0.52` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `57.16` | `57.31` | `55.29` | `55.41` | `127,847` | 7,177,688.25 USD | -1,165,151.48 USD | `-16.23%` | -2,318,024.72 USD | `-3.22` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `55.42` | `55.58` | `54.17` | `55.24` | `176,194` | 9,683,294.87 USD | -1,617,078.40 USD | `-16.70%` | -3,935,103.12 USD | `-3.07` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `57.72` | `57.92` | `57.43` | `57.74` | `47,138` | 2,718,274.03 USD | 101,628.42 USD | `+3.74%` | -910,014.20 USD | `+0.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `57.74` | `58.16` | `57.54` | `57.98` | `28,429` | 1,644,456.85 USD | 223,797.34 USD | `+13.61%` | -686,216.86 USD | `+0.74` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `57.98` | `58.01` | `54.17` | `55.23` | `372,969` | 20,809,917.59 USD | -3,250,887.87 USD | `-15.62%` | -3,937,104.73 USD | `-3.89` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | -1,031,107.81 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | -891,821.26 USD | `+0.52` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `55.23` | `372,930` | 20,807,783.78 USD | -3,252,974.08 USD | `-15.63%` | -4,144,795.34 USD | `-2.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `57.20` | `58.23` | `56.92` | `57.04` | `229,127` | 13,178,164.26 USD | -500,207.83 USD | `-3.80%` | -1,732,502.54 USD | `+1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `57.04` | `58.16` | `56.85` | `58.00` | `178,996` | 10,300,529.12 USD | 452,809.17 USD | `+4.40%` | -1,279,693.37 USD | `+1.27` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | -1,031,107.81 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | -891,821.26 USD | `+0.52` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `55.23` | `372,930` | 20,807,783.78 USD | -3,252,974.08 USD | `-15.63%` | -4,144,795.34 USD | `-2.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`55.22`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:26:17 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1065` | `0xeadc...9d55` | `LONG` | 2,080,659.18 USD | `36,463.77` | `52.78` | `54.87` | `0.000000` | 155,983.23 USD | `+7.50%` | `10X Cross` |
| `1069` | `0x9aa5...58af` | `SHORT` | 2,069,361.58 USD | `36,177.65` | `71.22` | `54.87` | `272.55` | 507,125.09 USD | `+24.51%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `57.71` | 6,835.28 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 6.84K USD at 57.7060 USD [API] | `2026-10-28 03:32:40` |
| `ANNOUNCEMENT` | `INFO` | `57.68` | 6,981.37 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 6.98K USD at 57.6830 USD [API] | `2026-10-28 03:40:52` |
| `ANNOUNCEMENT` | `INFO` | `57.62` | 5,689.97 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.69K USD at 57.6200 USD [API] | `2026-10-28 08:22:51` |
| `ANNOUNCEMENT` | `INFO` | `57.66` | 6,834.46 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 6.83K USD at 57.6650 USD [API] | `2026-10-28 09:03:25` |
| `ANNOUNCEMENT` | `INFO` | `57.79` | 5,189.94 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.19K USD at 57.7880 USD [API] | `2026-10-28 10:16:37` |
| `ANNOUNCEMENT` | `INFO` | `57.79` | 5,114.41 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.11K USD at 57.7900 USD [API] | `2026-10-28 10:16:37` |
| `ANNOUNCEMENT` | `INFO` | `57.85` | 7,509.64 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 57.8510 USD [API] | `2026-10-28 10:22:44` |
| `ANNOUNCEMENT` | `INFO` | `57.85` | 5,530.08 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 5.53K USD at 57.8460 USD [API] | `2026-10-28 10:22:44` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`59.03` (Vol: 256,600.00 USD, Dist: `+3.00%`) | Long MP=`56.68` (Vol: 327,300.00 USD, Dist: `--1.09%`)
  * 48H Horizon: Short MP=`59.00` (Vol: 285,100.00 USD, Dist: `+2.96%`) | Long MP=`56.72` (Vol: 274,000.00 USD, Dist: `--1.04%`)
  * 3D Horizon: Short MP=`59.01` (Vol: 285,100.00 USD, Dist: `+2.96%`) | Long MP=`56.70` (Vol: 302,600.00 USD, Dist: `--1.07%`)
  * 7D Horizon: Short MP=`59.04` (Vol: 256,600.00 USD, Dist: `+3.01%`) | Long MP=`55.27` (Vol: 344,500.00 USD, Dist: `--3.57%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `11.35` | 136.20 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `11.55` | 231.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.25` | 514.50 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.35` | 236.13 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.75` | 2,560.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.05` | 2,200.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.65` | 150.15 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `15.25` | 4,490.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `15.95` | 1,910.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `16.75` | 473.52 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `17.05` | 3,330.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `17.75` | 690.83 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.05` | 3,470.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.45` | 3,180.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.95` | 406.64 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.45` | 19,950.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.55` | 347.60 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.45` | 132.68 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.65` | 5,100.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.75` | 237.50 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.85` | 195.57 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.05` | 421.36 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 277,980.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 173.39 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 50,740.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 374.20 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.45` | 732.93 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.95` | 5,490.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.45` | 546.53 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 272.75 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 173.85 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.15` | 8,890.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.45` | 4,100.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.55` | 223.55 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.85` | 3,580.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 583.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.35` | 996.14 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.55` | 108.74 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 297,600.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 910.82 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 538.53 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 31,690.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 5,680.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 2,870.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 125.24 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.05` | 2,550.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 1,450.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.45` | 166.47 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.55` | 811.47 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 653.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 953.68 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 32,850.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.15` | 395.15 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.55` | 4,430.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 257.76 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 182.85 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 126.70 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 3,240.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 17,580.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 166.49 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.45` | 6,180.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.65` | 926.90 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 3,020.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 423.18 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 101.80 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 1,050.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 438.74 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.25` | 8,510.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 9,260.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 3,530.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 4,860.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 6,210.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 446.67 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.05` | 7,570.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 341.70 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 575.98 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 4,880.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 384.57 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 4,840.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 664,760.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 570.02 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 1,150.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 162.95 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 5,900.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 1,550.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 133.10 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 2,160.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.25` | 1,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 1,160.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 133.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 274.39 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 6,340.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 509.01 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 396.54 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.15` | 213.16 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 15,170.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 644.96 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.55` | 41,550.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.85` | 3,580.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 3,090.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 64,190.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 35,410.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 1,570.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 5,800.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 2,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 8,950.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 120,820.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 1,860.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 5,390.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 2,230.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 426.02 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 21,880.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 801.14 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 1,580.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 2,380.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 17,550.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 84,440.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 38,220.00 USD | 929,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.65` | 277.28 USD | 891,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 4,230.00 USD | 891,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 134.55 USD | 887,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 2,620.00 USD | 886,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 329.32 USD | 884,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 135.00 USD | 884,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 10,630.00 USD | 883,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 2,180.00 USD | 873,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 23,940.00 USD | 871,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 318.39 USD | 847,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 704.87 USD | 846,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 10,640.00 USD | 846,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.25` | 39,320.00 USD | 835,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.35` | 383.78 USD | 796,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.45` | 11,580.00 USD | 795,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 465.50 USD | 784,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 936.73 USD | 783,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 358.40 USD | 782,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 158.22 USD | 782,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 1,980.00 USD | 782,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 574.09 USD | 780,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.35` | 2,600.00 USD | 779,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.45` | 2,180.00 USD | 777,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 1,770.00 USD | 774,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 5,030.00 USD | 773,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.95` | 2,420.00 USD | 768,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 1,860.00 USD | 765,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 2,680.00 USD | 763,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 4,390.00 USD | 761,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 2,030.00 USD | 756,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 273.90 USD | 754,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 231.56 USD | 754,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 1,910.00 USD | 754,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 8,640.00 USD | 752,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.10` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 242.30 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,740.00 USD | 743,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.20` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 3,260.00 USD | 367.32 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.35` | 5,230.00 USD | 737,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.40` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 626.48 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.40` | 6,670,000.00 USD | 6,670,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.45` | 1,960.00 USD | 732,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.50` | 1,240,000.00 USD | 1,240,000.00 USD | 1,180.00 USD | 4,790.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.50` | 6,660,000.00 USD | 6,660,000.00 USD | 1,130.00 USD | 5,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.55` | 18,010.00 USD | 730,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.60` | 1,220,000.00 USD | 1,220,000.00 USD | 785.85 USD | 2,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.60` | 6,650,000.00 USD | 6,650,000.00 USD | 1,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.65` | 4,890.00 USD | 712,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.70` | 1,210,000.00 USD | 1,210,000.00 USD | 1,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.70` | 6,650,000.00 USD | 6,650,000.00 USD | 788.92 USD | 0.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.75` | 1,250.00 USD | 707,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.80` | 1,210,000.00 USD | 1,210,000.00 USD | 667.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.80` | 6,650,000.00 USD | 6,650,000.00 USD | 7,660.00 USD | 8,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `49.90` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 2,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.90` | 6,630,000.00 USD | 6,630,000.00 USD | 24,600.00 USD | 0.00 USD | 3,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.95` | 28,540.00 USD | 706,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.00` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.00` | 6,600,000.00 USD | 6,600,000.00 USD | 22,100.00 USD | 838.65 USD | 5,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.05` | 1,820.00 USD | 678,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.10` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 315.50 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.10` | 6,570,000.00 USD | 6,570,000.00 USD | 363.50 USD | 682.90 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.15` | 172.01 USD | 676,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.20` | 6,570,000.00 USD | 6,570,000.00 USD | 6,960.00 USD | 500.40 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.25` | 102.51 USD | 676,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.30` | 6,570,000.00 USD | 6,570,000.00 USD | 16,270.00 USD | 3,640.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.35` | 36,230.00 USD | 675,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.40` | 1,200,000.00 USD | 1,200,000.00 USD | 349.63 USD | 2,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.40` | 6,540,000.00 USD | 6,540,000.00 USD | 23,520.00 USD | 19,110.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,720.00 USD | 639,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.50` | 6,470,000.00 USD | 6,470,000.00 USD | 24,840.00 USD | 6,790.00 USD | 43,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.55` | 84,100.00 USD | 635,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `50.60` | 6,390,000.00 USD | 6,390,000.00 USD | 52,670.00 USD | 17,830.00 USD | 22,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.70` | 6,300,000.00 USD | 6,300,000.00 USD | 53,670.00 USD | 24,710.00 USD | 32,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.75` | 9,050.00 USD | 550,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.80` | 1,190,000.00 USD | 1,190,000.00 USD | 5,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.80` | 6,190,000.00 USD | 6,190,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.90` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 260.05 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.90` | 6,090,000.00 USD | 6,090,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.95` | 245.07 USD | 541,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.00` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 129.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.00` | 5,840,000.00 USD | 5,840,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.05` | 3,320.00 USD | 541,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.10` | 1,180,000.00 USD | 1,180,000.00 USD | 263.90 USD | 1,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.10` | 5,710,000.00 USD | 5,710,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.15` | 219,370.00 USD | 538,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.20` | 1,180,000.00 USD | 1,180,000.00 USD | 1,100.00 USD | 1,130.00 USD | 327.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.20` | 5,630,000.00 USD | 5,630,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.30` | 1,180,000.00 USD | 1,180,000.00 USD | 20,430.00 USD | 5,150.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.30` | 5,570,000.00 USD | 5,570,000.00 USD | 19,510.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.40` | 1,130,000.00 USD | 1,130,000.00 USD | 17,510.00 USD | 7,090.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.40` | 5,490,000.00 USD | 5,490,000.00 USD | 71,090.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.45` | 22,270.00 USD | 318,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.50` | 1,100,000.00 USD | 1,100,000.00 USD | 10,410.00 USD | 8,980.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.50` | 5,340,000.00 USD | 5,340,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.55` | 551.07 USD | 296,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.60` | 1,070,000.00 USD | 1,070,000.00 USD | 8,800.00 USD | 7,990.00 USD | 4,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.60` | 5,250,000.00 USD | 5,250,000.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.65` | 155.47 USD | 296,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.70` | 1,050,000.00 USD | 1,050,000.00 USD | 3,490.00 USD | 4,150.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.70` | 5,190,000.00 USD | 5,190,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.75` | 6,450.00 USD | 295,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.80` | 1,040,000.00 USD | 1,040,000.00 USD | 12,210.00 USD | 2,080.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.80` | 5,150,000.00 USD | 5,150,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.85` | 29,510.00 USD | 289,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.90` | 1,010,000.00 USD | 1,010,000.00 USD | 12,520.00 USD | 21,470.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.90` | 5,090,000.00 USD | 5,090,000.00 USD | 5,870.00 USD | 15,810.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.95` | 12,070.00 USD | 260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.00` | 968,990.00 USD | 968,990.00 USD | 25,150.00 USD | 8,230.00 USD | 23,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.00` | 5,070,000.00 USD | 5,070,000.00 USD | 64,300.00 USD | 20,800.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.05` | 179.57 USD | 247,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.10` | 912,270.00 USD | 912,270.00 USD | 27,630.00 USD | 5,780.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 4,970,000.00 USD | 4,970,000.00 USD | 24,220.00 USD | 18,810.00 USD | 35,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.20` | 843,640.00 USD | 843,640.00 USD | 20,520.00 USD | 10,450.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 4,890,000.00 USD | 4,890,000.00 USD | 38,380.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.25` | 358.96 USD | 247,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.30` | 798,280.00 USD | 798,280.00 USD | 38,870.00 USD | 8,170.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 4,820,000.00 USD | 4,820,000.00 USD | 18,740.00 USD | 12,840.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.35` | 1,470.00 USD | 247,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.40` | 735,130.00 USD | 735,130.00 USD | 10,040.00 USD | 7,510.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 4,780,000.00 USD | 4,780,000.00 USD | 20,580.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.45` | 3,830.00 USD | 245,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.50` | 711,290.00 USD | 711,290.00 USD | 15,070.00 USD | 13,510.00 USD | 998.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.50` | 4,730,000.00 USD | 4,730,000.00 USD | 33,240.00 USD | 667.05 USD | 10,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.55` | 8,700.00 USD | 242,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.60` | 681,710.00 USD | 681,710.00 USD | 2,760.00 USD | 8,750.00 USD | 273.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.60` | 4,680,000.00 USD | 4,680,000.00 USD | 36,640.00 USD | 14,530.00 USD | 584.77 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.70` | 669,920.00 USD | 669,920.00 USD | 4,930.00 USD | 7,610.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.70` | 4,630,000.00 USD | 4,630,000.00 USD | 20,250.00 USD | 43,820.00 USD | 62,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.75` | 7,450.00 USD | 233,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.80` | 642,300.00 USD | 642,300.00 USD | 14,400.00 USD | 14,660.00 USD | 60,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.80` | 4,510,000.00 USD | 4,510,000.00 USD | 46,600.00 USD | 27,850.00 USD | 108.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.85` | 5,950.00 USD | 225,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.90` | 552,910.00 USD | 552,910.00 USD | 28,000.00 USD | 7,150.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.90` | 4,430,000.00 USD | 4,430,000.00 USD | 51,920.00 USD | 23,030.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.95` | 4,320.00 USD | 220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.00` | 511,640.00 USD | 511,640.00 USD | 4,280.00 USD | 1,860.00 USD | 936.80 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.00` | 4,350,000.00 USD | 4,350,000.00 USD | 18,990.00 USD | 8,880.00 USD | 32,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.05` | 900.26 USD | 215,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.10` | 504,580.00 USD | 504,580.00 USD | 3,280.00 USD | 2,540.00 USD | 669.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.10` | 4,290,000.00 USD | 4,290,000.00 USD | 52,760.00 USD | 29,200.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.15` | 22,150.00 USD | 214,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.20` | 498,090.00 USD | 498,090.00 USD | 9,780.00 USD | 13,340.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.20` | 4,200,000.00 USD | 4,200,000.00 USD | 90,340.00 USD | 17,580.00 USD | 25,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.25` | 1,030.00 USD | 192,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.30` | 468,610.00 USD | 468,610.00 USD | 17,240.00 USD | 4,110.00 USD | 36,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.30` | 4,070,000.00 USD | 4,070,000.00 USD | 63,050.00 USD | 14,250.00 USD | 37,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.35` | 1,910.00 USD | 191,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.40` | 411,010.00 USD | 411,010.00 USD | 13,040.00 USD | 3,050.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.40` | 3,950,000.00 USD | 3,950,000.00 USD | 48,760.00 USD | 4,350.00 USD | 48,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.45` | 4,880.00 USD | 189,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.50` | 389,990.00 USD | 389,990.00 USD | 8,970.00 USD | 4,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.50` | 3,850,000.00 USD | 3,850,000.00 USD | 49,490.00 USD | 11,660.00 USD | 22,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.60` | 376,670.00 USD | 376,670.00 USD | 12,620.00 USD | 21,080.00 USD | 8,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.60` | 3,770,000.00 USD | 3,770,000.00 USD | 53,580.00 USD | 6,140.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.65` | 533.82 USD | 184,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.70` | 334,660.00 USD | 334,660.00 USD | 5,710.00 USD | 1,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.70` | 3,700,000.00 USD | 3,700,000.00 USD | 64,150.00 USD | 16,400.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.75` | 332.71 USD | 184,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.80` | 327,840.00 USD | 327,840.00 USD | 1,830.00 USD | 5,480.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.80` | 3,600,000.00 USD | 3,600,000.00 USD | 99,150.00 USD | 80,510.00 USD | 126,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.85` | 25,590.00 USD | 183,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.90` | 317,400.00 USD | 317,400.00 USD | 7,480.00 USD | 23,960.00 USD | 98,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.90` | 3,300,000.00 USD | 3,300,000.00 USD | 111,970.00 USD | 52,650.00 USD | 123,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.95` | 27,050.00 USD | 158,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.00` | 187,710.00 USD | 187,710.00 USD | 4,010.00 USD | 13,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.00` | 3,010,000.00 USD | 3,010,000.00 USD | 344,710.00 USD | 142,130.00 USD | 210,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.05` | 219.44 USD | 131,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.10` | 170,070.00 USD | 170,070.00 USD | 23,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.10` | 2,310,000.00 USD | 2,310,000.00 USD | 234,120.00 USD | 45,470.00 USD | 138,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.15` | 13,210.00 USD | 131,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.20` | 146,240.00 USD | 146,240.00 USD | 14,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.20` | 1,900,000.00 USD | 1,900,000.00 USD | 234,980.00 USD | 141,240.00 USD | 128,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.25` | 2,400.00 USD | 117,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.30` | 131,280.00 USD | 131,280.00 USD | 9,970.00 USD | 12,300.00 USD | 28,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.30` | 1,390,000.00 USD | 1,390,000.00 USD | 237,140.00 USD | 89,820.00 USD | 181,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.40` | 80,370.00 USD | 80,370.00 USD | 17,060.00 USD | 0.00 USD | 57,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.40` | 882,110.00 USD | 882,110.00 USD | 304,270.00 USD | 6,020.00 USD | 92,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.45` | 186.76 USD | 115,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.50` | 5,550.00 USD | 5,550.00 USD | 3,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.50` | 479,680.00 USD | 479,680.00 USD | 159,720.00 USD | 8,200.00 USD | 140,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.55` | 2,470.00 USD | 115,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.60` | 2,510.00 USD | 2,510.00 USD | 2,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.60` | 170,830.00 USD | 170,830.00 USD | 98,430.00 USD | 0.00 USD | 72,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.65` | 2,380.00 USD | 112,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `54.70` | 117,110.00 USD | 117,110.00 USD | 60,000.00 USD | 0.00 USD | 57,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `54.70` | 234,210.00 USD | 234,210.00 USD | 60,000.00 USD | 0.00 USD | 57,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `54.70` | 118,580.00 USD | 118,580.00 USD | 118,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `54.70` | 237,150.00 USD | 237,150.00 USD | 118,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.75` | 470.85 USD | 110,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `54.80` | 278,340.00 USD | 278,340.00 USD | 44,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `54.80` | 529,770.00 USD | 529,770.00 USD | 292,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.85` | 12,540.00 USD | 109,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `54.90` | 324,430.00 USD | 324,430.00 USD | 46,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `54.90` | 771,510.00 USD | 771,510.00 USD | 241,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.95` | 7,220.00 USD | 97,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `55.00` | 359,160.00 USD | 359,160.00 USD | 34,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.00` | 1,030,000.00 USD | 1,030,000.00 USD | 255,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.05` | 1,500.00 USD | 90,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `55.10` | 375,790.00 USD | 375,790.00 USD | 16,450.00 USD | 0.00 USD | 189.61 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.10` | 1,380,000.00 USD | 1,380,000.00 USD | 348,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.15` | 5,400.00 USD | 88,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `55.20` | 387,310.00 USD | 387,310.00 USD | 11,100.00 USD | 0.00 USD | 420.67 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.20` | 1,710,000.00 USD | 1,710,000.00 USD | 336,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.25` | 1,660.00 USD | 83,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `55.30` | 463,770.00 USD | 463,770.00 USD | 52,250.00 USD | 0.00 USD | 24,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.30` | 2,280,000.00 USD | 2,280,000.00 USD | 359,480.00 USD | 17,490.00 USD | 187,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.35` | 1,610.00 USD | 81,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `55.40` | 2,820,000.00 USD | 2,820,000.00 USD | 300,790.00 USD | 0.00 USD | 238,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.45` | 424.19 USD | 80,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `55.50` | 491,100.00 USD | 491,100.00 USD | 0.00 USD | 27,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.50` | 3,700,000.00 USD | 3,700,000.00 USD | 326,800.00 USD | 167,870.00 USD | 385,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.55` | 1,390.00 USD | 79,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `55.60` | 512,340.00 USD | 512,340.00 USD | 755.00 USD | 20,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.60` | 4,620,000.00 USD | 4,620,000.00 USD | 426,340.00 USD | 245,070.00 USD | 248,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.70` | 548,540.00 USD | 548,540.00 USD | 0.00 USD | 35,800.00 USD | 407.86 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.70` | 5,090,000.00 USD | 5,090,000.00 USD | 174,240.00 USD | 32,180.00 USD | 269,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.80` | 734,290.00 USD | 734,290.00 USD | 122,760.00 USD | 16,300.00 USD | 46,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.80` | 5,320,000.00 USD | 5,320,000.00 USD | 60,840.00 USD | 28,930.00 USD | 142,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.90` | 1,010,000.00 USD | 1,010,000.00 USD | 137,200.00 USD | 1,100.00 USD | 139,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.90` | 5,690,000.00 USD | 5,690,000.00 USD | 65,400.00 USD | 65,840.00 USD | 234,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.00` | 1,200,000.00 USD | 1,200,000.00 USD | 124,870.00 USD | 0.00 USD | 59,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.00` | 6,120,000.00 USD | 6,120,000.00 USD | 181,230.00 USD | 98,600.00 USD | 147,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.10` | 1,470,000.00 USD | 1,470,000.00 USD | 105,950.00 USD | 23,960.00 USD | 146,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.10` | 6,440,000.00 USD | 6,440,000.00 USD | 121,920.00 USD | 140,020.00 USD | 61,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `56.15` | 78,230.00 USD | 78,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `56.20` | 1,690,000.00 USD | 1,690,000.00 USD | 72,300.00 USD | 73,200.00 USD | 71,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.20` | 6,790,000.00 USD | 6,790,000.00 USD | 104,510.00 USD | 66,120.00 USD | 179,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.30` | 1,760,000.00 USD | 1,760,000.00 USD | 464.20 USD | 31,280.00 USD | 36,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.30` | 7,100,000.00 USD | 7,100,000.00 USD | 91,850.00 USD | 128,970.00 USD | 85,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.40` | 1,910,000.00 USD | 1,910,000.00 USD | 579.50 USD | 30,930.00 USD | 117,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.40` | 7,550,000.00 USD | 7,550,000.00 USD | 215,940.00 USD | 102,460.00 USD | 137,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.50` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 118,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.50` | 7,660,000.00 USD | 7,660,000.00 USD | 26,520.00 USD | 83,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.60` | 2,160,000.00 USD | 2,160,000.00 USD | 13,870.00 USD | 58,070.00 USD | 57,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.60` | 8,140,000.00 USD | 8,140,000.00 USD | 363,190.00 USD | 119,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.70` | 2,550,000.00 USD | 2,550,000.00 USD | 197,080.00 USD | 0.00 USD | 201,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.70` | 8,350,000.00 USD | 8,350,000.00 USD | 110,940.00 USD | 92,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.80` | 2,850,000.00 USD | 2,850,000.00 USD | 180,420.00 USD | 2,180.00 USD | 113,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.80` | 8,850,000.00 USD | 8,850,000.00 USD | 153,580.00 USD | 90,850.00 USD | 261,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.90` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 8,150.00 USD | 1,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.90` | 9,100,000.00 USD | 9,100,000.00 USD | 108,440.00 USD | 48,600.00 USD | 92,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.00` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 552.05 USD | 427.23 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.00` | 9,250,000.00 USD | 9,250,000.00 USD | 50,710.00 USD | 2,620.00 USD | 93,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.10` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 10,960.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.10` | 9,320,000.00 USD | 9,320,000.00 USD | 36,580.00 USD | 16,110.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.20` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 11,980.00 USD | 49,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.20` | 9,360,000.00 USD | 9,360,000.00 USD | 21,160.00 USD | 13,670.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.30` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 7,220.00 USD | 386.57 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.30` | 9,390,000.00 USD | 9,390,000.00 USD | 22,360.00 USD | 0.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.40` | 2,990,000.00 USD | 2,990,000.00 USD | 19,650.00 USD | 25,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.40` | 9,590,000.00 USD | 9,590,000.00 USD | 38,520.00 USD | 30,000.00 USD | 129,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.50` | 3,150,000.00 USD | 3,150,000.00 USD | 108,670.00 USD | 12,870.00 USD | 36,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.50` | 9,690,000.00 USD | 9,690,000.00 USD | 76,670.00 USD | 23,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.60` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 6,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.60` | 9,800,000.00 USD | 9,800,000.00 USD | 72,680.00 USD | 15,090.00 USD | 26,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.70` | 3,260,000.00 USD | 3,260,000.00 USD | 17,800.00 USD | 1,300.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.70` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 1,500.00 USD | 57,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.80` | 3,270,000.00 USD | 3,270,000.00 USD | 2,360.00 USD | 0.00 USD | 648.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.80` | 9,860,000.00 USD | 9,860,000.00 USD | 2,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.90` | 3,270,000.00 USD | 3,270,000.00 USD | 1,570.00 USD | 6,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.90` | 9,870,000.00 USD | 9,870,000.00 USD | 2,410.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.00` | 3,280,000.00 USD | 3,280,000.00 USD | 2,170.00 USD | 5,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.00` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 3,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.10` | 3,320,000.00 USD | 3,320,000.00 USD | 29,450.00 USD | 1,180.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.10` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 1,310.00 USD | 848.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.20` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 5,880.00 USD | 350.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.30` | 3,390,000.00 USD | 3,390,000.00 USD | 8,940.00 USD | 11,540.00 USD | 36,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.30` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 9,580.00 USD | 26,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.40` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 4,990.00 USD | 33,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.40` | 9,960,000.00 USD | 9,960,000.00 USD | 0.00 USD | 0.00 USD | 54,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.50` | 3,490,000.00 USD | 3,490,000.00 USD | 48,820.00 USD | 21,280.00 USD | 379.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.50` | 9,990,000.00 USD | 9,990,000.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.60` | 9,990,000.00 USD | 9,990,000.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.70` | 3,520,000.00 USD | 3,520,000.00 USD | 15,850.00 USD | 8,070.00 USD | 355.85 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.70` | 10,030,000.00 USD | 10,030,000.00 USD | 1,700.00 USD | 5,910.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.80` | 3,590,000.00 USD | 3,590,000.00 USD | 35,140.00 USD | 14,730.00 USD | 23,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.80` | 10,040,000.00 USD | 10,040,000.00 USD | 1,810.00 USD | 3,320.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.90` | 3,830,000.00 USD | 3,830,000.00 USD | 18,240.00 USD | 124,640.00 USD | 91,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.90` | 10,170,000.00 USD | 10,170,000.00 USD | 0.00 USD | 48,700.00 USD | 83,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.00` | 4,170,000.00 USD | 4,170,000.00 USD | 151,460.00 USD | 57,070.00 USD | 134,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.00` | 10,610,000.00 USD | 10,610,000.00 USD | 255,180.00 USD | 65,270.00 USD | 118,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.10` | 4,590,000.00 USD | 4,590,000.00 USD | 189,650.00 USD | 49,050.00 USD | 186,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.10` | 10,910,000.00 USD | 10,910,000.00 USD | 91,060.00 USD | 45,400.00 USD | 158,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.20` | 4,920,000.00 USD | 4,920,000.00 USD | 158,420.00 USD | 75,700.00 USD | 96,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.20` | 11,250,000.00 USD | 11,250,000.00 USD | 153,580.00 USD | 12,460.00 USD | 174,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.30` | 5,450,000.00 USD | 5,450,000.00 USD | 306,360.00 USD | 73,680.00 USD | 143,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.30` | 11,530,000.00 USD | 11,530,000.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.40` | 5,660,000.00 USD | 5,660,000.00 USD | 78,510.00 USD | 57,010.00 USD | 76,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.40` | 11,840,000.00 USD | 11,840,000.00 USD | 103,370.00 USD | 73,620.00 USD | 137,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.50` | 5,870,000.00 USD | 5,870,000.00 USD | 119,350.00 USD | 57,690.00 USD | 28,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.50` | 11,990,000.00 USD | 11,990,000.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.60` | 6,020,000.00 USD | 6,020,000.00 USD | 62,780.00 USD | 68,870.00 USD | 18,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.60` | 12,490,000.00 USD | 12,490,000.00 USD | 268,680.00 USD | 145,550.00 USD | 86,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.70` | 6,160,000.00 USD | 6,160,000.00 USD | 20,820.00 USD | 30,890.00 USD | 94,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.70` | 12,890,000.00 USD | 12,890,000.00 USD | 55,510.00 USD | 180,620.00 USD | 161,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.80` | 6,250,000.00 USD | 6,250,000.00 USD | 40,970.00 USD | 37,360.00 USD | 10,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.80` | 13,260,000.00 USD | 13,260,000.00 USD | 118,240.00 USD | 97,600.00 USD | 155,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.90` | 6,470,000.00 USD | 6,470,000.00 USD | 112,870.00 USD | 21,300.00 USD | 80,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.90` | 13,630,000.00 USD | 13,630,000.00 USD | 246,770.00 USD | 84,430.00 USD | 40,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.00` | 6,780,000.00 USD | 6,780,000.00 USD | 182,880.00 USD | 64,320.00 USD | 69,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.00` | 14,140,000.00 USD | 14,140,000.00 USD | 231,370.00 USD | 183,130.00 USD | 94,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.10` | 6,990,000.00 USD | 6,990,000.00 USD | 95,780.00 USD | 40,300.00 USD | 71,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.10` | 14,710,000.00 USD | 14,710,000.00 USD | 263,890.00 USD | 129,860.00 USD | 174,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.20` | 7,230,000.00 USD | 7,230,000.00 USD | 105,780.00 USD | 41,350.00 USD | 96,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.20` | 15,210,000.00 USD | 15,210,000.00 USD | 207,990.00 USD | 131,530.00 USD | 157,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.30` | 7,490,000.00 USD | 7,490,000.00 USD | 97,720.00 USD | 76,060.00 USD | 83,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.30` | 15,580,000.00 USD | 15,580,000.00 USD | 118,160.00 USD | 95,890.00 USD | 155,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.40` | 7,800,000.00 USD | 7,800,000.00 USD | 168,700.00 USD | 54,240.00 USD | 84,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.40` | 16,030,000.00 USD | 16,030,000.00 USD | 93,890.00 USD | 133,310.00 USD | 226,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.45` | 589.39 USD | 589.39 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.50` | 7,980,000.00 USD | 7,980,000.00 USD | 79,160.00 USD | 43,330.00 USD | 63,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.50` | 16,470,000.00 USD | 16,470,000.00 USD | 147,230.00 USD | 88,570.00 USD | 207,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.60` | 8,100,000.00 USD | 8,100,000.00 USD | 80,330.00 USD | 34,850.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.60` | 16,990,000.00 USD | 16,990,000.00 USD | 266,850.00 USD | 98,770.00 USD | 155,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.70` | 8,260,000.00 USD | 8,260,000.00 USD | 74,340.00 USD | 45,070.00 USD | 33,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.70` | 17,220,000.00 USD | 17,220,000.00 USD | 129,660.00 USD | 67,510.00 USD | 28,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.75` | 1,040.00 USD | 1,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.80` | 8,330,000.00 USD | 8,330,000.00 USD | 22,530.00 USD | 11,950.00 USD | 43,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.80` | 17,450,000.00 USD | 17,450,000.00 USD | 54,870.00 USD | 78,710.00 USD | 94,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.90` | 8,400,000.00 USD | 8,400,000.00 USD | 40,050.00 USD | 21,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.90` | 17,730,000.00 USD | 17,730,000.00 USD | 139,720.00 USD | 52,860.00 USD | 92,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.95` | 794.18 USD | 2,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.00` | 8,480,000.00 USD | 8,480,000.00 USD | 46,000.00 USD | 6,970.00 USD | 28,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 17,870,000.00 USD | 17,870,000.00 USD | 96,160.00 USD | 36,500.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.05` | 482.91 USD | 2,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.10` | 8,490,000.00 USD | 8,490,000.00 USD | 6,110.00 USD | 0.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 17,900,000.00 USD | 17,900,000.00 USD | 31,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.15` | 3,870.00 USD | 6,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.20` | 8,590,000.00 USD | 8,590,000.00 USD | 75,930.00 USD | 1,160.00 USD | 19,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.20` | 18,120,000.00 USD | 18,120,000.00 USD | 116,610.00 USD | 70,180.00 USD | 33,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.30` | 8,610,000.00 USD | 8,610,000.00 USD | 9,540.00 USD | 6,080.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.30` | 18,270,000.00 USD | 18,270,000.00 USD | 51,130.00 USD | 35,650.00 USD | 55,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.40` | 8,620,000.00 USD | 8,620,000.00 USD | 6,350.00 USD | 7,530.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.40` | 18,420,000.00 USD | 18,420,000.00 USD | 89,350.00 USD | 41,800.00 USD | 24,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.50` | 8,670,000.00 USD | 8,670,000.00 USD | 9,120.00 USD | 19,960.00 USD | 17,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.50` | 18,510,000.00 USD | 18,510,000.00 USD | 19,810.00 USD | 35,300.00 USD | 36,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.60` | 8,730,000.00 USD | 8,730,000.00 USD | 24,180.00 USD | 14,990.00 USD | 20,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.60` | 18,760,000.00 USD | 18,760,000.00 USD | 54,240.00 USD | 63,390.00 USD | 132,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.65` | 211,210.00 USD | 217,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.70` | 8,790,000.00 USD | 8,790,000.00 USD | 37,720.00 USD | 9,670.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.70` | 18,980,000.00 USD | 18,980,000.00 USD | 91,980.00 USD | 12,880.00 USD | 114,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.80` | 8,820,000.00 USD | 8,820,000.00 USD | 23,640.00 USD | 8,420.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.80` | 19,300,000.00 USD | 19,300,000.00 USD | 167,990.00 USD | 62,660.00 USD | 86,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.90` | 8,880,000.00 USD | 8,880,000.00 USD | 28,490.00 USD | 11,940.00 USD | 16,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.90` | 19,440,000.00 USD | 19,440,000.00 USD | 72,380.00 USD | 29,730.00 USD | 35,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.00` | 8,900,000.00 USD | 8,900,000.00 USD | 14,630.00 USD | 911.46 USD | 2,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.00` | 19,560,000.00 USD | 19,560,000.00 USD | 56,450.00 USD | 13,260.00 USD | 49,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.10` | 8,910,000.00 USD | 8,910,000.00 USD | 12,050.00 USD | 945.47 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.10` | 19,620,000.00 USD | 19,620,000.00 USD | 36,500.00 USD | 12,820.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.20` | 8,920,000.00 USD | 8,920,000.00 USD | 3,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.20` | 19,740,000.00 USD | 19,740,000.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.30` | 8,920,000.00 USD | 8,920,000.00 USD | 464.20 USD | 260.05 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.30` | 19,890,000.00 USD | 19,890,000.00 USD | 35,280.00 USD | 23,450.00 USD | 97,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.40` | 8,930,000.00 USD | 8,930,000.00 USD | 1,150.00 USD | 0.00 USD | 129.78 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.40` | 20,030,000.00 USD | 20,030,000.00 USD | 79,620.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.50` | 8,930,000.00 USD | 8,930,000.00 USD | 263.90 USD | 1,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.50` | 20,120,000.00 USD | 20,120,000.00 USD | 44,300.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.60` | 8,930,000.00 USD | 8,930,000.00 USD | 1,100.00 USD | 1,130.00 USD | 327.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.60` | 20,190,000.00 USD | 20,190,000.00 USD | 34,910.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.70` | 8,970,000.00 USD | 8,970,000.00 USD | 19,390.00 USD | 5,150.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.70` | 20,270,000.00 USD | 20,270,000.00 USD | 22,020.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.80` | 9,010,000.00 USD | 9,010,000.00 USD | 16,430.00 USD | 7,090.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.80` | 20,410,000.00 USD | 20,410,000.00 USD | 72,250.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.90` | 9,030,000.00 USD | 9,030,000.00 USD | 8,780.00 USD | 8,980.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.90` | 20,510,000.00 USD | 20,510,000.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.00` | 9,050,000.00 USD | 9,050,000.00 USD | 7,800.00 USD | 7,990.00 USD | 4,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.00` | 20,570,000.00 USD | 20,570,000.00 USD | 34,730.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.10` | 9,060,000.00 USD | 9,060,000.00 USD | 4,260.00 USD | 4,150.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.10` | 20,610,000.00 USD | 20,610,000.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.20` | 9,070,000.00 USD | 9,070,000.00 USD | 2,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.30` | 9,070,000.00 USD | 9,070,000.00 USD | 4,590.00 USD | 594.25 USD | 2,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.30` | 20,650,000.00 USD | 20,650,000.00 USD | 19,680.00 USD | 11,500.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.40` | 9,090,000.00 USD | 9,090,000.00 USD | 8,400.00 USD | 1,480.00 USD | 7,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.40` | 20,680,000.00 USD | 20,680,000.00 USD | 13,220.00 USD | 1,320.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.50` | 9,130,000.00 USD | 9,130,000.00 USD | 12,520.00 USD | 21,470.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.50` | 20,700,000.00 USD | 20,700,000.00 USD | 6,620.00 USD | 15,810.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.60` | 9,190,000.00 USD | 9,190,000.00 USD | 25,150.00 USD | 8,230.00 USD | 23,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.60` | 20,800,000.00 USD | 20,800,000.00 USD | 63,480.00 USD | 20,800.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.70` | 9,260,000.00 USD | 9,260,000.00 USD | 27,630.00 USD | 5,780.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.70` | 20,870,000.00 USD | 20,870,000.00 USD | 21,940.00 USD | 18,810.00 USD | 35,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.80` | 9,300,000.00 USD | 9,300,000.00 USD | 19,730.00 USD | 10,450.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.80` | 20,940,000.00 USD | 20,940,000.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.90` | 9,360,000.00 USD | 9,360,000.00 USD | 34,930.00 USD | 8,170.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.90` | 20,970,000.00 USD | 20,970,000.00 USD | 7,650.00 USD | 12,840.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.00` | 9,380,000.00 USD | 9,380,000.00 USD | 7,880.00 USD | 6,900.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.00` | 21,010,000.00 USD | 21,010,000.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.10` | 9,400,000.00 USD | 9,400,000.00 USD | 13,740.00 USD | 5,360.00 USD | 80.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.10` | 21,040,000.00 USD | 21,040,000.00 USD | 20,350.00 USD | 667.05 USD | 10,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.20` | 9,420,000.00 USD | 9,420,000.00 USD | 2,760.00 USD | 8,200.00 USD | 273.52 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.20` | 21,090,000.00 USD | 21,090,000.00 USD | 28,840.00 USD | 14,530.00 USD | 584.77 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.40` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 946.37 USD | 13,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.40` | 21,140,000.00 USD | 21,140,000.00 USD | 2,540.00 USD | 20,590.00 USD | 29,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.50` | 21,170,000.00 USD | 21,170,000.00 USD | 7,700.00 USD | 7,120.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.60` | 21,210,000.00 USD | 21,210,000.00 USD | 32,220.00 USD | 14,180.00 USD | 108.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.70` | 21,280,000.00 USD | 21,280,000.00 USD | 39,430.00 USD | 23,030.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.80` | 21,320,000.00 USD | 21,320,000.00 USD | 7,540.00 USD | 8,210.00 USD | 20,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.90` | 21,360,000.00 USD | 21,360,000.00 USD | 25,320.00 USD | 8,010.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.00` | 21,380,000.00 USD | 21,380,000.00 USD | 1,790.00 USD | 9,480.00 USD | 13,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.10` | 21,440,000.00 USD | 21,440,000.00 USD | 5,810.00 USD | 14,250.00 USD | 37,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.20` | 21,480,000.00 USD | 21,480,000.00 USD | 10,380.00 USD | 2,250.00 USD | 28,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.30` | 21,530,000.00 USD | 21,530,000.00 USD | 22,330.00 USD | 9,180.00 USD | 22,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `65.95` | 1,160.00 USD | 219,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.85` | 33,950.00 USD | 253,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.95` | 121.18 USD | 253,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.85` | 709.03 USD | 253,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `69.45` | 414.62 USD | 254,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `70.45` | 5,270.00 USD | 259,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `72.95` | 666.03 USD | 260,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `76.35` | 8,380.00 USD | 268,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.85` | 602.56 USD | 269,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.95` | 136.41 USD | 269,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.75` | 646.00 USD | 270,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.05` | 19,000.00 USD | 289,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.55` | 123.96 USD | 289,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.65` | 3,850.00 USD | 293,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.75` | 214.32 USD | 293,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `84.65` | 862.58 USD | 294,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `85.45` | 2,820.00 USD | 296,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `86.35` | 3,450.00 USD | 300,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `87.45` | 23,330.00 USD | 323,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `96.35` | 2,410.00 USD | 326,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.05` | 669.68 USD | 326,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.45` | 1,050.00 USD | 327,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.85` | 353,760.00 USD | 681,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.45` | 21,090.00 USD | 702,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.25` | 21,850.00 USD | 724,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.45` | 131.44 USD | 724,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.55` | 1,120.00 USD | 725,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.65` | 973.72 USD | 726,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.75` | 3,860.00 USD | 730,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 664.59 USD | 731,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.65` | 420.77 USD | 731,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `11.35` | 2,930,000.00 USD | 0.00 USD | 136.20 USD | `-80.44%` | `12.00` |
| `Live` | `Long` | `11.55` | 2,930,000.00 USD | 0.00 USD | 231.00 USD | `-80.09%` | `20.00` |
| `Live` | `Long` | `12.25` | 2,930,000.00 USD | 0.00 USD | 514.50 USD | `-78.89%` | `42.00` |
| `Live` | `Long` | `12.35` | 2,930,000.00 USD | 0.00 USD | 236.13 USD | `-78.71%` | `19.12` |
| `Live` | `Long` | `12.75` | 2,930,000.00 USD | 0.00 USD | 2,560.00 USD | `-78.02%` | `200.43` |
| `Live` | `Long` | `13.05` | 2,930,000.00 USD | 0.00 USD | 2,200.00 USD | `-77.51%` | `168.79` |
| `Live` | `Long` | `13.65` | 2,930,000.00 USD | 0.00 USD | 150.15 USD | `-76.47%` | `11.00` |
| `Live` | `Long` | `15.25` | 2,930,000.00 USD | 0.00 USD | 4,490.00 USD | `-73.71%` | `294.67` |
| `Live` | `Long` | `15.95` | 2,920,000.00 USD | 0.00 USD | 1,910.00 USD | `-72.51%` | `120.00` |
| `Live` | `Long` | `16.75` | 2,920,000.00 USD | 0.00 USD | 473.52 USD | `-71.13%` | `28.27` |
| `Live` | `Long` | `17.05` | 2,920,000.00 USD | 0.00 USD | 3,330.00 USD | `-70.61%` | `195.03` |
| `Live` | `Long` | `17.75` | 2,920,000.00 USD | 0.00 USD | 690.83 USD | `-69.41%` | `38.92` |
| `Live` | `Long` | `19.05` | 2,910,000.00 USD | 0.00 USD | 3,470.00 USD | `-67.16%` | `182.00` |
| `Live` | `Long` | `19.45` | 2,910,000.00 USD | 0.00 USD | 3,180.00 USD | `-66.48%` | `163.47` |
| `Live` | `Long` | `20.95` | 2,910,000.00 USD | 0.00 USD | 406.64 USD | `-63.89%` | `19.41` |
| `Live` | `Long` | `21.45` | 2,910,000.00 USD | 0.00 USD | 19,950.00 USD | `-63.03%` | `930.00` |
| `Live` | `Long` | `21.55` | 2,890,000.00 USD | 0.00 USD | 347.60 USD | `-62.86%` | `16.13` |
| `Live` | `Long` | `22.45` | 2,890,000.00 USD | 0.00 USD | 132.68 USD | `-61.30%` | `5.91` |
| `Live` | `Long` | `22.65` | 2,890,000.00 USD | 0.00 USD | 5,100.00 USD | `-60.96%` | `225.00` |
| `Live` | `Long` | `23.75` | 2,880,000.00 USD | 0.00 USD | 237.50 USD | `-59.06%` | `10.00` |
| `Live` | `Long` | `23.85` | 2,880,000.00 USD | 0.00 USD | 195.57 USD | `-58.89%` | `8.20` |
| `Live` | `Long` | `24.05` | 2,880,000.00 USD | 0.00 USD | 421.36 USD | `-58.55%` | `17.52` |
| `Live` | `Long` | `25.25` | 2,880,000.00 USD | 0.00 USD | 277,980.00 USD | `-56.48%` | `11,009.19` |
| `Live` | `Long` | `25.35` | 2,600,000.00 USD | 0.00 USD | 173.39 USD | `-56.31%` | `6.84` |
| `Live` | `Long` | `25.55` | 2,600,000.00 USD | 0.00 USD | 50,740.00 USD | `-55.96%` | `1,985.99` |
| `Live` | `Long` | `25.95` | 2,550,000.00 USD | 0.00 USD | 374.20 USD | `-55.27%` | `14.42` |
| `Live` | `Long` | `26.45` | 2,550,000.00 USD | 0.00 USD | 732.93 USD | `-54.41%` | `27.71` |
| `Live` | `Long` | `26.95` | 2,550,000.00 USD | 0.00 USD | 5,490.00 USD | `-53.55%` | `203.85` |
| `Live` | `Long` | `27.45` | 2,550,000.00 USD | 0.00 USD | 546.53 USD | `-52.69%` | `19.91` |
| `Live` | `Long` | `27.55` | 2,550,000.00 USD | 0.00 USD | 272.75 USD | `-52.51%` | `9.90` |
| `Live` | `Long` | `27.95` | 2,540,000.00 USD | 0.00 USD | 173.85 USD | `-51.82%` | `6.22` |
| `Live` | `Long` | `28.15` | 2,540,000.00 USD | 0.00 USD | 8,890.00 USD | `-51.48%` | `315.82` |
| `Live` | `Long` | `28.45` | 2,540,000.00 USD | 0.00 USD | 4,100.00 USD | `-50.96%` | `144.17` |
| `Live` | `Long` | `28.55` | 2,530,000.00 USD | 0.00 USD | 223.55 USD | `-50.79%` | `7.83` |
| `Live` | `Long` | `28.85` | 2,530,000.00 USD | 0.00 USD | 3,580.00 USD | `-50.27%` | `124.01` |
| `Live` | `Long` | `29.15` | 2,530,000.00 USD | 0.00 USD | 583.00 USD | `-49.76%` | `20.00` |
| `Live` | `Long` | `29.35` | 2,530,000.00 USD | 0.00 USD | 996.14 USD | `-49.41%` | `33.94` |
| `Live` | `Long` | `29.55` | 2,530,000.00 USD | 0.00 USD | 108.74 USD | `-49.07%` | `3.68` |
| `Live` | `Long` | `29.75` | 2,530,000.00 USD | 0.00 USD | 297,600.00 USD | `-48.72%` | `10,003.44` |
| `Live` | `Long` | `30.05` | 2,230,000.00 USD | 0.00 USD | 910.82 USD | `-48.20%` | `30.31` |
| `Live` | `Long` | `30.95` | 2,230,000.00 USD | 0.00 USD | 538.53 USD | `-46.65%` | `17.40` |
| `Live` | `Long` | `31.15` | 2,230,000.00 USD | 0.00 USD | 31,690.00 USD | `-46.31%` | `1,017.43` |
| `Live` | `Long` | `31.55` | 2,200,000.00 USD | 0.00 USD | 5,680.00 USD | `-45.62%` | `180.02` |
| `Live` | `Long` | `31.85` | 2,190,000.00 USD | 0.00 USD | 2,870.00 USD | `-45.10%` | `90.00` |
| `Live` | `Long` | `31.95` | 2,190,000.00 USD | 0.00 USD | 125.24 USD | `-44.93%` | `3.92` |
| `Live` | `Long` | `32.05` | 2,190,000.00 USD | 0.00 USD | 2,550.00 USD | `-44.76%` | `79.49` |
| `Live` | `Long` | `32.15` | 2,180,000.00 USD | 0.00 USD | 1,450.00 USD | `-44.59%` | `45.01` |
| `Live` | `Long` | `32.45` | 2,180,000.00 USD | 0.00 USD | 166.47 USD | `-44.07%` | `5.13` |
| `Live` | `Long` | `32.55` | 2,180,000.00 USD | 0.00 USD | 811.47 USD | `-43.90%` | `24.93` |
| `Live` | `Long` | `32.65` | 2,180,000.00 USD | 0.00 USD | 653.00 USD | `-43.72%` | `20.00` |
| `Live` | `Long` | `32.75` | 2,180,000.00 USD | 0.00 USD | 953.68 USD | `-43.55%` | `29.12` |
| `Live` | `Long` | `32.85` | 2,180,000.00 USD | 0.00 USD | 32,850.00 USD | `-43.38%` | `1,000.01` |
| `Live` | `Long` | `33.15` | 2,150,000.00 USD | 0.00 USD | 395.15 USD | `-42.86%` | `11.92` |
| `Live` | `Long` | `33.55` | 2,150,000.00 USD | 0.00 USD | 4,430.00 USD | `-42.17%` | `131.94` |
| `Live` | `Long` | `33.65` | 2,140,000.00 USD | 0.00 USD | 257.76 USD | `-42.00%` | `7.66` |
| `Live` | `Long` | `34.05` | 2,140,000.00 USD | 0.00 USD | 182.85 USD | `-41.31%` | `5.37` |
| `Live` | `Long` | `34.15` | 2,140,000.00 USD | 0.00 USD | 126.70 USD | `-41.14%` | `3.71` |
| `Live` | `Long` | `34.65` | 2,140,000.00 USD | 0.00 USD | 3,240.00 USD | `-40.28%` | `93.56` |
| `Live` | `Long` | `34.95` | 2,140,000.00 USD | 0.00 USD | 17,580.00 USD | `-39.76%` | `503.00` |
| `Live` | `Long` | `35.05` | 2,120,000.00 USD | 0.00 USD | 166.49 USD | `-39.59%` | `4.75` |
| `Live` | `Long` | `35.45` | 2,120,000.00 USD | 0.00 USD | 6,180.00 USD | `-38.90%` | `174.22` |
| `Live` | `Long` | `35.65` | 2,110,000.00 USD | 0.00 USD | 926.90 USD | `-38.55%` | `26.00` |
| `Live` | `Long` | `36.35` | 2,110,000.00 USD | 0.00 USD | 3,020.00 USD | `-37.35%` | `83.03` |
| `Live` | `Long` | `36.45` | 2,110,000.00 USD | 0.00 USD | 423.18 USD | `-37.17%` | `11.61` |
| `Live` | `Long` | `36.75` | 2,110,000.00 USD | 0.00 USD | 101.80 USD | `-36.66%` | `2.77` |
| `Live` | `Long` | `37.05` | 2,110,000.00 USD | 0.00 USD | 1,050.00 USD | `-36.14%` | `28.46` |
| `Live` | `Long` | `37.15` | 2,110,000.00 USD | 0.00 USD | 438.74 USD | `-35.97%` | `11.81` |
| `Live` | `Long` | `37.25` | 2,110,000.00 USD | 0.00 USD | 8,510.00 USD | `-35.79%` | `228.45` |
| `Live` | `Long` | `37.35` | 2,100,000.00 USD | 0.00 USD | 9,260.00 USD | `-35.62%` | `247.91` |
| `Live` | `Long` | `37.55` | 2,090,000.00 USD | 0.00 USD | 3,530.00 USD | `-35.28%` | `94.04` |
| `Live` | `Long` | `37.75` | 2,090,000.00 USD | 0.00 USD | 4,860.00 USD | `-34.93%` | `128.71` |
| `Live` | `Long` | `37.85` | 2,080,000.00 USD | 0.00 USD | 6,210.00 USD | `-34.76%` | `164.03` |
| `Live` | `Long` | `37.95` | 2,080,000.00 USD | 0.00 USD | 446.67 USD | `-34.59%` | `11.77` |
| `Live` | `Long` | `38.05` | 2,080,000.00 USD | 0.00 USD | 7,570.00 USD | `-34.42%` | `198.87` |
| `Live` | `Long` | `38.35` | 2,070,000.00 USD | 0.00 USD | 341.70 USD | `-33.90%` | `8.91` |
| `Live` | `Long` | `38.45` | 2,070,000.00 USD | 0.00 USD | 575.98 USD | `-33.73%` | `14.98` |
| `Live` | `Long` | `38.55` | 2,070,000.00 USD | 0.00 USD | 4,880.00 USD | `-33.55%` | `126.57` |
| `Live` | `Long` | `38.65` | 2,060,000.00 USD | 0.00 USD | 384.57 USD | `-33.38%` | `9.95` |
| `Live` | `Long` | `38.95` | 2,060,000.00 USD | 0.00 USD | 4,840.00 USD | `-32.86%` | `124.26` |
| `Live` | `Long` | `39.05` | 2,060,000.00 USD | 0.00 USD | 664,760.00 USD | `-32.69%` | `17,023.28` |
| `Live` | `Long` | `39.15` | 1,390,000.00 USD | 0.00 USD | 570.02 USD | `-32.52%` | `14.56` |
| `Live` | `Long` | `39.45` | 1,390,000.00 USD | 0.00 USD | 1,150.00 USD | `-32.00%` | `29.07` |
| `Live` | `Long` | `39.55` | 1,390,000.00 USD | 0.00 USD | 162.95 USD | `-31.83%` | `4.12` |
| `Live` | `Long` | `39.65` | 1,390,000.00 USD | 0.00 USD | 5,900.00 USD | `-31.66%` | `148.78` |
| `Live` | `Long` | `39.75` | 1,380,000.00 USD | 0.00 USD | 1,550.00 USD | `-31.49%` | `38.90` |
| `Live` | `Long` | `39.85` | 1,380,000.00 USD | 0.00 USD | 133.10 USD | `-31.31%` | `3.34` |
| `Live` | `Long` | `40.05` | 1,380,000.00 USD | 0.00 USD | 2,160.00 USD | `-30.97%` | `53.97` |
| `Live` | `Long` | `40.25` | 1,380,000.00 USD | 0.00 USD | 1,000.00 USD | `-30.62%` | `24.88` |
| `Live` | `Long` | `40.45` | 1,380,000.00 USD | 0.00 USD | 1,160.00 USD | `-30.28%` | `28.76` |
| `Live` | `Long` | `40.55` | 1,380,000.00 USD | 0.00 USD | 133.00 USD | `-30.11%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,380,000.00 USD | 0.00 USD | 274.39 USD | `-29.93%` | `6.75` |
| `Live` | `Long` | `40.85` | 1,380,000.00 USD | 0.00 USD | 6,340.00 USD | `-29.59%` | `155.23` |
| `Live` | `Long` | `40.95` | 1,370,000.00 USD | 0.00 USD | 509.01 USD | `-29.42%` | `12.43` |
| `Live` | `Long` | `41.05` | 1,370,000.00 USD | 0.00 USD | 396.54 USD | `-29.24%` | `9.66` |
| `Live` | `Long` | `41.15` | 1,370,000.00 USD | 0.00 USD | 213.16 USD | `-29.07%` | `5.18` |
| `Live` | `Long` | `41.25` | 1,370,000.00 USD | 0.00 USD | 15,170.00 USD | `-28.90%` | `367.73` |
| `Live` | `Long` | `41.45` | 1,360,000.00 USD | 0.00 USD | 644.96 USD | `-28.56%` | `15.56` |
| `Live` | `Long` | `41.55` | 1,360,000.00 USD | 0.00 USD | 41,550.00 USD | `-28.38%` | `1,000.00` |
| `Live` | `Long` | `41.85` | 1,310,000.00 USD | 0.00 USD | 3,580.00 USD | `-27.87%` | `85.43` |
| `Live` | `Long` | `42.05` | 1,310,000.00 USD | 0.00 USD | 3,090.00 USD | `-27.52%` | `73.52` |
| `Live` | `Long` | `42.15` | 1,310,000.00 USD | 0.00 USD | 64,190.00 USD | `-27.35%` | `1,522.78` |
| `Live` | `Long` | `42.25` | 1,240,000.00 USD | 0.00 USD | 35,410.00 USD | `-27.18%` | `838.00` |
| `Live` | `Long` | `42.65` | 1,210,000.00 USD | 0.00 USD | 1,570.00 USD | `-26.49%` | `36.70` |
| `Live` | `Long` | `42.85` | 1,210,000.00 USD | 0.00 USD | 5,800.00 USD | `-26.14%` | `135.38` |
| `Live` | `Long` | `42.95` | 1,200,000.00 USD | 0.00 USD | 2,000.00 USD | `-25.97%` | `46.65` |
| `Live` | `Long` | `43.05` | 1,200,000.00 USD | 0.00 USD | 8,950.00 USD | `-25.80%` | `208.00` |
| `Live` | `Long` | `43.15` | 1,190,000.00 USD | 0.00 USD | 120,820.00 USD | `-25.63%` | `2,800.00` |
| `Live` | `Long` | `43.25` | 1,070,000.00 USD | 0.00 USD | 1,860.00 USD | `-25.45%` | `42.98` |
| `Live` | `Long` | `43.35` | 1,070,000.00 USD | 0.00 USD | 5,390.00 USD | `-25.28%` | `124.24` |
| `Live` | `Long` | `43.45` | 1,060,000.00 USD | 0.00 USD | 2,230.00 USD | `-25.11%` | `51.25` |
| `Live` | `Long` | `43.65` | 1,060,000.00 USD | 0.00 USD | 426.02 USD | `-24.76%` | `9.76` |
| `Live` | `Long` | `43.75` | 1,060,000.00 USD | 0.00 USD | 21,880.00 USD | `-24.59%` | `500.00` |
| `Live` | `Long` | `43.85` | 1,040,000.00 USD | 0.00 USD | 801.14 USD | `-24.42%` | `18.27` |
| `Live` | `Long` | `43.95` | 1,040,000.00 USD | 0.00 USD | 1,580.00 USD | `-24.25%` | `35.97` |
| `Live` | `Long` | `44.15` | 1,030,000.00 USD | 0.00 USD | 2,380.00 USD | `-23.90%` | `53.99` |
| `Live` | `Long` | `44.25` | 1,030,000.00 USD | 0.00 USD | 17,550.00 USD | `-23.73%` | `396.65` |
| `Live` | `Long` | `44.35` | 1,010,000.00 USD | 0.00 USD | 84,440.00 USD | `-23.56%` | `1,903.87` |
| `Live` | `Long` | `44.55` | 929,810.00 USD | 0.00 USD | 38,220.00 USD | `-23.21%` | `857.83` |
| `Live` | `Long` | `44.65` | 891,600.00 USD | 0.00 USD | 277.28 USD | `-23.04%` | `6.21` |
| `Live` | `Long` | `44.75` | 891,320.00 USD | 0.00 USD | 4,230.00 USD | `-22.87%` | `94.55` |
| `Live` | `Long` | `44.85` | 887,090.00 USD | 0.00 USD | 134.55 USD | `-22.70%` | `3.00` |
| `Live` | `Long` | `44.95` | 886,950.00 USD | 0.00 USD | 2,620.00 USD | `-22.52%` | `58.18` |
| `Live` | `Long` | `45.05` | 884,340.00 USD | 0.00 USD | 329.32 USD | `-22.35%` | `7.31` |
| `Live` | `Long` | `45.15` | 884,010.00 USD | 0.00 USD | 135.00 USD | `-22.18%` | `2.99` |
| `Live` | `Long` | `45.25` | 883,870.00 USD | 0.00 USD | 10,630.00 USD | `-22.01%` | `234.95` |
| `Live` | `Long` | `45.35` | 873,240.00 USD | 0.00 USD | 2,180.00 USD | `-21.83%` | `48.02` |
| `Live` | `Long` | `45.45` | 871,060.00 USD | 0.00 USD | 23,940.00 USD | `-21.66%` | `526.65` |
| `Live` | `Long` | `45.55` | 847,130.00 USD | 0.00 USD | 318.39 USD | `-21.49%` | `6.99` |
| `Live` | `Long` | `45.95` | 846,810.00 USD | 0.00 USD | 704.87 USD | `-20.80%` | `15.34` |
| `Live` | `Long` | `46.05` | 846,100.00 USD | 0.00 USD | 10,640.00 USD | `-20.63%` | `231.02` |
| `Live` | `Long` | `46.25` | 835,470.00 USD | 0.00 USD | 39,320.00 USD | `-20.28%` | `850.21` |
| `Live` | `Long` | `46.35` | 796,140.00 USD | 0.00 USD | 383.78 USD | `-20.11%` | `8.28` |
| `Live` | `Long` | `46.45` | 795,760.00 USD | 0.00 USD | 11,580.00 USD | `-19.94%` | `249.31` |
| `Live` | `Long` | `46.55` | 784,180.00 USD | 0.00 USD | 465.50 USD | `-19.76%` | `10.00` |
| `Live` | `Long` | `46.65` | 783,710.00 USD | 0.00 USD | 936.73 USD | `-19.59%` | `20.08` |
| `Live` | `Long` | `46.85` | 782,780.00 USD | 0.00 USD | 358.40 USD | `-19.25%` | `7.65` |
| `Live` | `Long` | `46.95` | 782,420.00 USD | 0.00 USD | 158.22 USD | `-19.08%` | `3.37` |
| `Live` | `Long` | `47.15` | 782,260.00 USD | 0.00 USD | 1,980.00 USD | `-18.73%` | `42.07` |
| `Live` | `Long` | `47.25` | 780,280.00 USD | 0.00 USD | 574.09 USD | `-18.56%` | `12.15` |
| `Live` | `Long` | `47.35` | 779,700.00 USD | 0.00 USD | 2,600.00 USD | `-18.39%` | `55.00` |
| `Live` | `Long` | `47.45` | 777,100.00 USD | 0.00 USD | 2,180.00 USD | `-18.21%` | `45.94` |
| `Live` | `Long` | `47.55` | 774,920.00 USD | 0.00 USD | 1,770.00 USD | `-18.04%` | `37.28` |
| `Live` | `Long` | `47.75` | 773,150.00 USD | 0.00 USD | 5,030.00 USD | `-17.70%` | `105.44` |
| `Live` | `Long` | `47.95` | 768,110.00 USD | 0.00 USD | 2,420.00 USD | `-17.35%` | `50.39` |
| `Live` | `Long` | `48.05` | 765,700.00 USD | 0.00 USD | 1,860.00 USD | `-17.18%` | `38.61` |
| `Live` | `Long` | `48.15` | 763,840.00 USD | 0.00 USD | 2,680.00 USD | `-17.01%` | `55.56` |
| `Live` | `Long` | `48.25` | 761,160.00 USD | 0.00 USD | 4,390.00 USD | `-16.83%` | `90.89` |
| `Live` | `Long` | `48.55` | 756,780.00 USD | 0.00 USD | 2,030.00 USD | `-16.32%` | `41.85` |
| `Live` | `Long` | `48.65` | 754,750.00 USD | 0.00 USD | 273.90 USD | `-16.15%` | `5.63` |
| `Live` | `Long` | `48.75` | 754,470.00 USD | 0.00 USD | 231.56 USD | `-15.97%` | `4.75` |
| `Live` | `Long` | `48.95` | 754,240.00 USD | 0.00 USD | 1,910.00 USD | `-15.63%` | `39.11` |
| `Live` | `Long` | `49.05` | 752,330.00 USD | 0.00 USD | 8,640.00 USD | `-15.46%` | `176.06` |
| `Live` | `Long` | `49.15` | 743,690.00 USD | 0.00 USD | 5,740.00 USD | `-15.28%` | `116.83` |
| `Live` | `Long` | `49.35` | 737,950.00 USD | 0.00 USD | 5,230.00 USD | `-14.94%` | `105.97` |
| `Live` | `Long` | `49.45` | 732,720.00 USD | 0.00 USD | 1,960.00 USD | `-14.77%` | `39.73` |
| `Live` | `Long` | `49.55` | 730,760.00 USD | 0.00 USD | 18,010.00 USD | `-14.59%` | `363.57` |
| `Live` | `Long` | `49.65` | 712,740.00 USD | 0.00 USD | 4,890.00 USD | `-14.42%` | `98.52` |
| `Live` | `Long` | `49.75` | 707,850.00 USD | 0.00 USD | 1,250.00 USD | `-14.25%` | `25.06` |
| `Live` | `Long` | `49.95` | 706,600.00 USD | 0.00 USD | 28,540.00 USD | `-13.90%` | `571.31` |
| `Live` | `Long` | `50.05` | 678,070.00 USD | 0.00 USD | 1,820.00 USD | `-13.73%` | `36.43` |
| `Live` | `Long` | `50.15` | 676,240.00 USD | 0.00 USD | 172.01 USD | `-13.56%` | `3.43` |
| `Live` | `Long` | `50.25` | 676,070.00 USD | 0.00 USD | 102.51 USD | `-13.39%` | `2.04` |
| `Live` | `Long` | `50.35` | 675,970.00 USD | 0.00 USD | 36,230.00 USD | `-13.22%` | `719.62` |
| `Live` | `Long` | `50.45` | 639,730.00 USD | 0.00 USD | 4,720.00 USD | `-13.04%` | `93.64` |
| `Live` | `Long` | `50.55` | 635,010.00 USD | 0.00 USD | 84,100.00 USD | `-12.87%` | `1,663.61` |
| `Live` | `Long` | `50.75` | 550,920.00 USD | 0.00 USD | 9,050.00 USD | `-12.53%` | `178.28` |
| `Live` | `Long` | `50.95` | 541,870.00 USD | 0.00 USD | 245.07 USD | `-12.18%` | `4.81` |
| `Live` | `Long` | `51.05` | 541,620.00 USD | 0.00 USD | 3,320.00 USD | `-12.01%` | `65.00` |
| `Live` | `Long` | `51.15` | 538,300.00 USD | 0.00 USD | 219,370.00 USD | `-11.84%` | `4,288.79` |
| `Live` | `Long` | `51.45` | 318,930.00 USD | 0.00 USD | 22,270.00 USD | `-11.32%` | `432.80` |
| `Live` | `Long` | `51.55` | 296,660.00 USD | 0.00 USD | 551.07 USD | `-11.15%` | `10.69` |
| `Live` | `Long` | `51.65` | 296,110.00 USD | 0.00 USD | 155.47 USD | `-10.97%` | `3.01` |
| `Live` | `Long` | `51.75` | 295,960.00 USD | 0.00 USD | 6,450.00 USD | `-10.80%` | `124.64` |
| `Live` | `Long` | `51.85` | 289,510.00 USD | 0.00 USD | 29,510.00 USD | `-10.63%` | `569.10` |
| `Live` | `Long` | `51.95` | 260,000.00 USD | 0.00 USD | 12,070.00 USD | `-10.46%` | `232.41` |
| `Live` | `Long` | `52.05` | 247,930.00 USD | 0.00 USD | 179.57 USD | `-10.28%` | `3.45` |
| `Live` | `Long` | `52.25` | 247,750.00 USD | 0.00 USD | 358.96 USD | `-9.94%` | `6.87` |
| `Live` | `Long` | `52.35` | 247,390.00 USD | 0.00 USD | 1,470.00 USD | `-9.77%` | `28.09` |
| `Live` | `Long` | `52.45` | 245,920.00 USD | 0.00 USD | 3,830.00 USD | `-9.60%` | `72.95` |
| `Live` | `Long` | `52.55` | 242,090.00 USD | 0.00 USD | 8,700.00 USD | `-9.42%` | `165.49` |
| `Live` | `Long` | `52.75` | 233,390.00 USD | 0.00 USD | 7,450.00 USD | `-9.08%` | `141.16` |
| `Live` | `Long` | `52.85` | 225,950.00 USD | 0.00 USD | 5,950.00 USD | `-8.91%` | `112.64` |
| `Live` | `Long` | `52.95` | 220,000.00 USD | 0.00 USD | 4,320.00 USD | `-8.73%` | `81.62` |
| `Live` | `Long` | `53.05` | 215,670.00 USD | 0.00 USD | 900.26 USD | `-8.56%` | `16.97` |
| `Live` | `Long` | `53.15` | 214,770.00 USD | 0.00 USD | 22,150.00 USD | `-8.39%` | `416.71` |
| `Live` | `Long` | `53.25` | 192,630.00 USD | 0.00 USD | 1,030.00 USD | `-8.22%` | `19.27` |
| `Live` | `Long` | `53.35` | 191,600.00 USD | 0.00 USD | 1,910.00 USD | `-8.04%` | `35.71` |
| `Live` | `Long` | `53.45` | 189,690.00 USD | 0.00 USD | 4,880.00 USD | `-7.87%` | `91.21` |
| `Live` | `Long` | `53.65` | 184,820.00 USD | 0.00 USD | 533.82 USD | `-7.53%` | `9.95` |
| `Live` | `Long` | `53.75` | 184,290.00 USD | 0.00 USD | 332.71 USD | `-7.35%` | `6.19` |
| `Live` | `Long` | `53.85` | 183,950.00 USD | 0.00 USD | 25,590.00 USD | `-7.18%` | `475.29` |
| `Live` | `Long` | `53.95` | 158,360.00 USD | 0.00 USD | 27,050.00 USD | `-7.01%` | `501.35` |
| `Live` | `Long` | `54.05` | 131,310.00 USD | 0.00 USD | 219.44 USD | `-6.84%` | `4.06` |
| `Live` | `Long` | `54.15` | 131,090.00 USD | 0.00 USD | 13,210.00 USD | `-6.67%` | `243.97` |
| `Live` | `Long` | `54.25` | 117,880.00 USD | 0.00 USD | 2,400.00 USD | `-6.49%` | `44.18` |
| `Live` | `Long` | `54.45` | 115,480.00 USD | 0.00 USD | 186.76 USD | `-6.15%` | `3.43` |
| `Live` | `Long` | `54.55` | 115,300.00 USD | 0.00 USD | 2,470.00 USD | `-5.98%` | `45.19` |
| `Live` | `Long` | `54.65` | 112,830.00 USD | 0.00 USD | 2,380.00 USD | `-5.80%` | `43.63` |
| `Live` | `Long` | `54.75` | 110,450.00 USD | 0.00 USD | 470.85 USD | `-5.63%` | `8.60` |
| `Live` | `Long` | `54.85` | 109,980.00 USD | 0.00 USD | 12,540.00 USD | `-5.46%` | `228.63` |
| `Live` | `Long` | `54.95` | 97,440.00 USD | 0.00 USD | 7,220.00 USD | `-5.29%` | `131.47` |
| `Live` | `Long` | `55.05` | 90,210.00 USD | 0.00 USD | 1,500.00 USD | `-5.11%` | `27.16` |
| `Live` | `Long` | `55.15` | 88,720.00 USD | 0.00 USD | 5,400.00 USD | `-4.94%` | `98.00` |
| `Live` | `Long` | `55.25` | 83,310.00 USD | 0.00 USD | 1,660.00 USD | `-4.77%` | `30.00` |
| `Live` | `Long` | `55.35` | 81,650.00 USD | 0.00 USD | 1,610.00 USD | `-4.60%` | `29.05` |
| `Live` | `Long` | `55.45` | 80,050.00 USD | 0.00 USD | 424.19 USD | `-4.42%` | `7.65` |
| `Live` | `Long` | `55.55` | 79,620.00 USD | 0.00 USD | 1,390.00 USD | `-4.25%` | `25.05` |
| `Live` | `Long` | `56.15` | 78,230.00 USD | 0.00 USD | 78,230.00 USD | `-3.22%` | `1,393.24` |
| `Live` | `Short` | `60.45` | 589.39 USD | 589.39 USD | 0.00 USD | `+4.19%` | `9.75` |
| `Live` | `Short` | `60.75` | 1,630.00 USD | 1,040.00 USD | 0.00 USD | `+4.71%` | `17.16` |
| `Live` | `Short` | `60.95` | 2,430.00 USD | 794.18 USD | 0.00 USD | `+5.06%` | `13.03` |
| `Live` | `Short` | `61.05` | 2,910.00 USD | 482.91 USD | 0.00 USD | `+5.23%` | `7.91` |
| `Live` | `Short` | `61.15` | 6,780.00 USD | 3,870.00 USD | 0.00 USD | `+5.40%` | `63.26` |
| `Live` | `Short` | `61.65` | 217,980.00 USD | 211,210.00 USD | 0.00 USD | `+6.26%` | `3,425.89` |
| `Live` | `Short` | `65.95` | 219,140.00 USD | 1,160.00 USD | 0.00 USD | `+13.67%` | `17.59` |
| `Live` | `Short` | `66.85` | 253,090.00 USD | 33,950.00 USD | 0.00 USD | `+15.22%` | `507.83` |
| `Live` | `Short` | `66.95` | 253,210.00 USD | 121.18 USD | 0.00 USD | `+15.40%` | `1.81` |
| `Live` | `Short` | `67.85` | 253,920.00 USD | 709.03 USD | 0.00 USD | `+16.95%` | `10.45` |
| `Live` | `Short` | `69.45` | 254,340.00 USD | 414.62 USD | 0.00 USD | `+19.71%` | `5.97` |
| `Live` | `Short` | `70.45` | 259,600.00 USD | 5,270.00 USD | 0.00 USD | `+21.43%` | `74.74` |
| `Live` | `Short` | `72.95` | 260,270.00 USD | 666.03 USD | 0.00 USD | `+25.74%` | `9.13` |
| `Live` | `Short` | `76.35` | 268,650.00 USD | 8,380.00 USD | 0.00 USD | `+31.60%` | `109.80` |
| `Live` | `Short` | `77.85` | 269,250.00 USD | 602.56 USD | 0.00 USD | `+34.18%` | `7.74` |
| `Live` | `Short` | `77.95` | 269,390.00 USD | 136.41 USD | 0.00 USD | `+34.36%` | `1.75` |
| `Live` | `Short` | `80.75` | 270,040.00 USD | 646.00 USD | 0.00 USD | `+39.18%` | `8.00` |
| `Live` | `Short` | `81.05` | 289,040.00 USD | 19,000.00 USD | 0.00 USD | `+39.70%` | `234.42` |
| `Live` | `Short` | `81.55` | 289,160.00 USD | 123.96 USD | 0.00 USD | `+40.56%` | `1.52` |
| `Live` | `Short` | `82.65` | 293,010.00 USD | 3,850.00 USD | 0.00 USD | `+42.46%` | `46.61` |
| `Live` | `Short` | `82.75` | 293,230.00 USD | 214.32 USD | 0.00 USD | `+42.63%` | `2.59` |
| `Live` | `Short` | `84.65` | 294,090.00 USD | 862.58 USD | 0.00 USD | `+45.91%` | `10.19` |
| `Live` | `Short` | `85.45` | 296,910.00 USD | 2,820.00 USD | 0.00 USD | `+47.28%` | `33.00` |
| `Live` | `Short` | `86.35` | 300,360.00 USD | 3,450.00 USD | 0.00 USD | `+48.84%` | `40.00` |
| `Live` | `Short` | `87.45` | 323,700.00 USD | 23,330.00 USD | 0.00 USD | `+50.73%` | `266.81` |
| `Live` | `Short` | `96.35` | 326,100.00 USD | 2,410.00 USD | 0.00 USD | `+66.07%` | `25.00` |
| `Live` | `Short` | `98.05` | 326,770.00 USD | 669.68 USD | 0.00 USD | `+69.00%` | `6.83` |
| `Live` | `Short` | `98.45` | 327,820.00 USD | 1,050.00 USD | 0.00 USD | `+69.69%` | `10.63` |
| `Live` | `Short` | `104.85` | 681,590.00 USD | 353,760.00 USD | 0.00 USD | `+80.72%` | `3,374.01` |
| `Live` | `Short` | `105.45` | 702,680.00 USD | 21,090.00 USD | 0.00 USD | `+81.76%` | `200.00` |
| `Live` | `Short` | `109.25` | 724,530.00 USD | 21,850.00 USD | 0.00 USD | `+88.31%` | `200.00` |
| `Live` | `Short` | `110.45` | 724,660.00 USD | 131.44 USD | 0.00 USD | `+90.38%` | `1.19` |
| `Live` | `Short` | `110.55` | 725,770.00 USD | 1,120.00 USD | 0.00 USD | `+90.55%` | `10.11` |
| `Live` | `Short` | `110.65` | 726,750.00 USD | 973.72 USD | 0.00 USD | `+90.72%` | `8.80` |
| `Live` | `Short` | `110.75` | 730,610.00 USD | 3,860.00 USD | 0.00 USD | `+90.89%` | `34.86` |
| `Live` | `Short` | `110.95` | 731,270.00 USD | 664.59 USD | 0.00 USD | `+91.24%` | `5.99` |
| `Live` | `Short` | `114.65` | 731,690.00 USD | 420.77 USD | 0.00 USD | `+97.61%` | `3.67` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 491,480.00 USD | 0.00 USD | 392.18 USD | `-65.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 491,090.00 USD | 0.00 USD | 2,310.00 USD | `-61.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 488,780.00 USD | 0.00 USD | 122.24 USD | `-56.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 488,660.00 USD | 0.00 USD | 1,560.00 USD | `-56.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 487,100.00 USD | 0.00 USD | 410.25 USD | `-52.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 486,690.00 USD | 0.00 USD | 281.57 USD | `-48.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 486,410.00 USD | 0.00 USD | 36,050.00 USD | `-37.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 450,360.00 USD | 0.00 USD | 37,550.00 USD | `-35.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 412,810.00 USD | 0.00 USD | 447.01 USD | `-34.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 412,360.00 USD | 0.00 USD | 40,560.00 USD | `-32.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 371,810.00 USD | 0.00 USD | 489.57 USD | `-32.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 371,320.00 USD | 0.00 USD | 1,550.00 USD | `-31.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 369,760.00 USD | 0.00 USD | 9,500.00 USD | `-30.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 360,260.00 USD | 0.00 USD | 2,060.00 USD | `-29.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 358,200.00 USD | 0.00 USD | 2,960.00 USD | `-28.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 355,250.00 USD | 0.00 USD | 6,050.00 USD | `-27.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 349,200.00 USD | 0.00 USD | 5,680.00 USD | `-25.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 343,520.00 USD | 0.00 USD | 672.22 USD | `-24.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 342,840.00 USD | 0.00 USD | 213.80 USD | `-23.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 342,630.00 USD | 0.00 USD | 223.20 USD | `-23.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 342,410.00 USD | 0.00 USD | 391.13 USD | `-23.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 342,020.00 USD | 0.00 USD | 7,080.00 USD | `-22.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 334,940.00 USD | 0.00 USD | 1,370.00 USD | `-21.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 333,570.00 USD | 0.00 USD | 553.80 USD | `-20.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 333,020.00 USD | 0.00 USD | 14,000.00 USD | `-19.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 319,020.00 USD | 0.00 USD | 158.56 USD | `-18.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 318,860.00 USD | 0.00 USD | 373.28 USD | `-18.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 318,490.00 USD | 0.00 USD | 849.46 USD | `-18.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 317,640.00 USD | 0.00 USD | 1,150.00 USD | `-17.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 316,490.00 USD | 0.00 USD | 1,740.00 USD | `-15.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 314,750.00 USD | 0.00 USD | 981.00 USD | `-15.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 313,770.00 USD | 0.00 USD | 1,150.00 USD | `-14.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 312,620.00 USD | 0.00 USD | 298.20 USD | `-13.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 312,320.00 USD | 0.00 USD | 14,650.00 USD | `-13.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 297,670.00 USD | 0.00 USD | 6,410.00 USD | `-13.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 291,260.00 USD | 0.00 USD | 459.70 USD | `-13.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 290,800.00 USD | 0.00 USD | 1,020.00 USD | `-12.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 289,780.00 USD | 0.00 USD | 439.89 USD | `-11.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 289,340.00 USD | 0.00 USD | 3,700.00 USD | `-10.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 285,640.00 USD | 0.00 USD | 27,730.00 USD | `-10.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 257,910.00 USD | 0.00 USD | 51,800.00 USD | `-9.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 206,110.00 USD | 0.00 USD | 10,530.00 USD | `-9.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 195,580.00 USD | 0.00 USD | 271.13 USD | `-9.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 195,300.00 USD | 0.00 USD | 5,050.00 USD | `-8.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 190,260.00 USD | 0.00 USD | 1,060.00 USD | `-8.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 189,200.00 USD | 0.00 USD | 460.81 USD | `-8.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 188,730.00 USD | 0.00 USD | 184.21 USD | `-7.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 188,550.00 USD | 0.00 USD | 1,370.00 USD | `-7.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 187,180.00 USD | 0.00 USD | 462.03 USD | `-7.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 186,720.00 USD | 0.00 USD | 601.58 USD | `-6.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 186,120.00 USD | 0.00 USD | 3,090.00 USD | `-6.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 183,030.00 USD | 0.00 USD | 156.53 USD | `-6.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.45` | 182,870.00 USD | 0.00 USD | 570.09 USD | `-6.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.55` | 182,300.00 USD | 0.00 USD | 1,690.00 USD | `-5.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.65` | 180,610.00 USD | 0.00 USD | 4,110.00 USD | `-5.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 176,510.00 USD | 0.00 USD | 33,280.00 USD | `-5.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.95` | 143,230.00 USD | 0.00 USD | 1,410.00 USD | `-5.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 141,820.00 USD | 0.00 USD | 1,580.00 USD | `-5.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.25` | 140,240.00 USD | 0.00 USD | 429.85 USD | `-4.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.35` | 139,810.00 USD | 0.00 USD | 2,140.00 USD | `-4.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.55` | 137,670.00 USD | 0.00 USD | 113.88 USD | `-4.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.65` | 137,550.00 USD | 0.00 USD | 4,930.00 USD | `-4.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.75` | 132,630.00 USD | 0.00 USD | 1,820.00 USD | `-3.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.85` | 130,810.00 USD | 0.00 USD | 196.59 USD | `-3.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.95` | 130,620.00 USD | 0.00 USD | 193.03 USD | `-3.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 130,420.00 USD | 0.00 USD | 587.96 USD | `-3.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 129,830.00 USD | 0.00 USD | 1,070.00 USD | `-3.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.35` | 128,760.00 USD | 0.00 USD | 78,570.00 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.45` | 50,190.00 USD | 0.00 USD | 694.90 USD | `-2.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.55` | 49,490.00 USD | 0.00 USD | 2,640.00 USD | `-2.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.65` | 46,860.00 USD | 0.00 USD | 195.44 USD | `-2.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.75` | 46,660.00 USD | 0.00 USD | 228.70 USD | `-2.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.85` | 46,430.00 USD | 0.00 USD | 18,030.00 USD | `-2.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.95` | 28,400.00 USD | 0.00 USD | 390.68 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.05` | 28,010.00 USD | 0.00 USD | 5,800.00 USD | `-1.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.15` | 22,210.00 USD | 0.00 USD | 392.05 USD | `-1.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.25` | 21,820.00 USD | 0.00 USD | 196.37 USD | `-1.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.45` | 21,620.00 USD | 0.00 USD | 344.70 USD | `-0.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.55` | 21,280.00 USD | 0.00 USD | 20,360.00 USD | `-0.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.65` | 919.00 USD | 0.00 USD | 198.89 USD | `-0.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.75` | 720.11 USD | 0.00 USD | 199.24 USD | `-0.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.85` | 520.87 USD | 0.00 USD | 392.22 USD | `-0.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.95` | 128.65 USD | 0.00 USD | 128.65 USD | `-0.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 1,980.00 USD | 1,980.00 USD | 0.00 USD | `+0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 2,180.00 USD | 200.04 USD | 0.00 USD | `+0.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 2,380.00 USD | 200.96 USD | 0.00 USD | `+0.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 2,500.00 USD | 123.70 USD | 0.00 USD | `+0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 3,100.00 USD | 601.45 USD | 0.00 USD | `+0.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 3,510.00 USD | 401.65 USD | 0.00 USD | `+0.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.65` | 3,780.00 USD | 274.48 USD | 0.00 USD | `+1.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 3,900.00 USD | 124.55 USD | 0.00 USD | `+1.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 6,850.00 USD | 2,940.00 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 7,050.00 USD | 203.38 USD | 0.00 USD | `+1.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 11,850.00 USD | 4,800.00 USD | 0.00 USD | `+1.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 13,130.00 USD | 1,280.00 USD | 0.00 USD | `+1.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.25` | 13,440.00 USD | 307.51 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 13,900.00 USD | 461.74 USD | 0.00 USD | `+2.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 14,100.00 USD | 200.35 USD | 0.00 USD | `+2.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.55` | 14,600.00 USD | 496.65 USD | 0.00 USD | `+2.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 15,320.00 USD | 724.75 USD | 0.00 USD | `+2.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.75` | 15,430.00 USD | 113.53 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 15,590.00 USD | 158.00 USD | 0.00 USD | `+3.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.95` | 30,960.00 USD | 15,360.00 USD | 0.00 USD | `+3.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 32,110.00 USD | 1,160.00 USD | 0.00 USD | `+3.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 32,670.00 USD | 551.00 USD | 0.00 USD | `+4.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.45` | 316,770.00 USD | 284,100.00 USD | 0.00 USD | `+4.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 317,650.00 USD | 878.58 USD | 0.00 USD | `+4.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 319,030.00 USD | 1,390.00 USD | 0.00 USD | `+4.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.75` | 319,440.00 USD | 407.63 USD | 0.00 USD | `+4.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 320,640.00 USD | 1,190.00 USD | 0.00 USD | `+4.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 321,520.00 USD | 882.56 USD | 0.00 USD | `+5.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 323,880.00 USD | 2,360.00 USD | 0.00 USD | `+5.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 324,010.00 USD | 125.56 USD | 0.00 USD | `+5.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.35` | 324,240.00 USD | 236.20 USD | 0.00 USD | `+5.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 327,840.00 USD | 3,600.00 USD | 0.00 USD | `+5.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 328,480.00 USD | 643.20 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.95` | 330,600.00 USD | 2,120.00 USD | 0.00 USD | `+6.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 330,710.00 USD | 106.11 USD | 0.00 USD | `+6.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.25` | 330,830.00 USD | 117.03 USD | 0.00 USD | `+7.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.45` | 331,040.00 USD | 217.95 USD | 0.00 USD | `+7.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.55` | 331,390.00 USD | 347.15 USD | 0.00 USD | `+7.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 332,110.00 USD | 716.72 USD | 0.00 USD | `+7.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.75` | 332,250.00 USD | 141.19 USD | 0.00 USD | `+8.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 333,030.00 USD | 781.19 USD | 0.00 USD | `+8.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 333,930.00 USD | 900.52 USD | 0.00 USD | `+8.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 334,630.00 USD | 703.97 USD | 0.00 USD | `+9.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.35` | 334,770.00 USD | 140.64 USD | 0.00 USD | `+9.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 335,440.00 USD | 668.13 USD | 0.00 USD | `+9.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 339,990.00 USD | 4,550.00 USD | 0.00 USD | `+9.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 340,550.00 USD | 555.03 USD | 0.00 USD | `+9.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 341,080.00 USD | 531.62 USD | 0.00 USD | `+10.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 341,280.00 USD | 202.69 USD | 0.00 USD | `+11.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 341,580.00 USD | 298.04 USD | 0.00 USD | `+11.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 341,680.00 USD | 102.13 USD | 0.00 USD | `+12.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 342,220.00 USD | 540.09 USD | 0.00 USD | `+12.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 342,320.00 USD | 100.79 USD | 0.00 USD | `+12.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 342,590.00 USD | 262.20 USD | 0.00 USD | `+12.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.65` | 342,900.00 USD | 315.12 USD | 0.00 USD | `+13.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 343,270.00 USD | 371.49 USD | 0.00 USD | `+13.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.85` | 344,150.00 USD | 881.07 USD | 0.00 USD | `+13.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 344,850.00 USD | 696.17 USD | 0.00 USD | `+13.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 345,380.00 USD | 534.00 USD | 0.00 USD | `+15.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 356,460.00 USD | 11,080.00 USD | 0.00 USD | `+15.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 369,870.00 USD | 13,410.00 USD | 0.00 USD | `+15.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.05` | 372,230.00 USD | 2,360.00 USD | 0.00 USD | `+17.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 377,100.00 USD | 4,860.00 USD | 0.00 USD | `+17.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 377,300.00 USD | 204.48 USD | 0.00 USD | `+19.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 378,230.00 USD | 929.64 USD | 0.00 USD | `+20.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 698,130.00 USD | 319,890.00 USD | 0.00 USD | `+20.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 698,300.00 USD | 170.04 USD | 0.00 USD | `+22.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 704,060.00 USD | 5,770.00 USD | 0.00 USD | `+22.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 704,620.00 USD | 555.61 USD | 0.00 USD | `+22.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 705,770.00 USD | 1,150.00 USD | 0.00 USD | `+24.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 708,470.00 USD | 2,700.00 USD | 0.00 USD | `+24.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 708,630.00 USD | 156.78 USD | 0.00 USD | `+24.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 711,850.00 USD | 3,220.00 USD | 0.00 USD | `+25.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 712,260.00 USD | 411.14 USD | 0.00 USD | `+26.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 835,450.00 USD | 123,190.00 USD | 0.00 USD | `+27.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 836,470.00 USD | 1,020.00 USD | 0.00 USD | `+28.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 836,580.00 USD | 104.93 USD | 0.00 USD | `+29.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 836,970.00 USD | 392.51 USD | 0.00 USD | `+29.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 837,370.00 USD | 402.59 USD | 0.00 USD | `+29.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 837,690.00 USD | 315.18 USD | 0.00 USD | `+33.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 896,990.00 USD | 59,310.00 USD | 0.00 USD | `+35.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 900,160.00 USD | 3,160.00 USD | 0.00 USD | `+36.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 905,840.00 USD | 5,690.00 USD | 0.00 USD | `+37.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 943,460.00 USD | 37,620.00 USD | 0.00 USD | `+37.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 943,900.00 USD | 433.89 USD | 0.00 USD | `+39.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 984,600.00 USD | 40,700.00 USD | 0.00 USD | `+39.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 984,760.00 USD | 164.10 USD | 0.00 USD | `+41.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 985,310.00 USD | 546.81 USD | 0.00 USD | `+42.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 987,610.00 USD | 2,300.00 USD | 0.00 USD | `+44.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 999,680.00 USD | 12,070.00 USD | 0.00 USD | `+46.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.75` | 1,010,000.00 USD | 12,330.00 USD | 0.00 USD | `+47.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.25` | 1,010,000.00 USD | 435.38 USD | 0.00 USD | `+50.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 1,010,000.00 USD | 1,580.00 USD | 0.00 USD | `+51.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 1,050,000.00 USD | 37,000.00 USD | 0.00 USD | `+51.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 1,050,000.00 USD | 473.21 USD | 0.00 USD | `+53.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 1,050,000.00 USD | 1,270.00 USD | 0.00 USD | `+53.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 1,050,000.00 USD | 1,630.00 USD | 0.00 USD | `+54.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 1,080,000.00 USD | 21,060.00 USD | 0.00 USD | `+55.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 1,080,000.00 USD | 481.55 USD | 0.00 USD | `+57.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 1,080,000.00 USD | 1,330.00 USD | 0.00 USD | `+58.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 1,080,000.00 USD | 188.10 USD | 0.00 USD | `+62.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,340,000.00 USD | 266,140.00 USD | 0.00 USD | `+63.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,350,000.00 USD | 3,400.00 USD | 0.00 USD | `+64.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,370,000.00 USD | 21,930.00 USD | 0.00 USD | `+65.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,370,000.00 USD | 294.15 USD | 0.00 USD | `+69.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,370,000.00 USD | 4,010.00 USD | 0.00 USD | `+72.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,370,000.00 USD | 306.15 USD | 0.00 USD | `+75.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,370,000.00 USD | 936.72 USD | 0.00 USD | `+77.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,380,000.00 USD | 2,920.00 USD | 0.00 USD | `+77.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,380,000.00 USD | 324.15 USD | 0.00 USD | `+86.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 1,380,000.00 USD | 123.23 USD | 0.00 USD | `+87.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 1,470,000.00 USD | 89,110.00 USD | 0.00 USD | `+91.41%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `49.10` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 242.30 USD | 0.00 USD |
| `1D` | `49.20` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 3,260.00 USD | 367.32 USD |
| `1D` | `49.40` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 626.48 USD |
| `7D` | `49.40` | 6,670,000.00 USD | 0.00 USD | 6,670,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD |
| `1D` | `49.50` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 1,180.00 USD | 4,790.00 USD | 13,790.00 USD |
| `7D` | `49.50` | 6,660,000.00 USD | 0.00 USD | 6,660,000.00 USD | 1,130.00 USD | 5,470.00 USD | 0.00 USD |
| `1D` | `49.60` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 785.85 USD | 2,670.00 USD | 0.00 USD |
| `7D` | `49.60` | 6,650,000.00 USD | 0.00 USD | 6,650,000.00 USD | 1,200.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `49.70` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 1,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `49.70` | 6,650,000.00 USD | 0.00 USD | 6,650,000.00 USD | 788.92 USD | 0.00 USD | 4,900.00 USD |
| `1D` | `49.80` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 667.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `49.80` | 6,650,000.00 USD | 0.00 USD | 6,650,000.00 USD | 7,660.00 USD | 8,220.00 USD | 0.00 USD |
| `1D` | `49.90` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 0.00 USD | 2,460.00 USD | 0.00 USD |
| `7D` | `49.90` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 24,600.00 USD | 0.00 USD | 3,950.00 USD |
| `1D` | `50.00` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 11,490.00 USD |
| `7D` | `50.00` | 6,600,000.00 USD | 0.00 USD | 6,600,000.00 USD | 22,100.00 USD | 838.65 USD | 5,340.00 USD |
| `1D` | `50.10` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 0.00 USD | 315.50 USD | 0.00 USD |
| `7D` | `50.10` | 6,570,000.00 USD | 0.00 USD | 6,570,000.00 USD | 363.50 USD | 682.90 USD | 0.00 USD |
| `7D` | `50.20` | 6,570,000.00 USD | 0.00 USD | 6,570,000.00 USD | 6,960.00 USD | 500.40 USD | 0.00 USD |
| `7D` | `50.30` | 6,570,000.00 USD | 0.00 USD | 6,570,000.00 USD | 16,270.00 USD | 3,640.00 USD | 1,950.00 USD |
| `1D` | `50.40` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 349.63 USD | 2,190.00 USD | 0.00 USD |
| `7D` | `50.40` | 6,540,000.00 USD | 0.00 USD | 6,540,000.00 USD | 23,520.00 USD | 19,110.00 USD | 33,450.00 USD |
| `7D` | `50.50` | 6,470,000.00 USD | 0.00 USD | 6,470,000.00 USD | 24,840.00 USD | 6,790.00 USD | 43,710.00 USD |
| `7D` | `50.60` | 6,390,000.00 USD | 0.00 USD | 6,390,000.00 USD | 52,670.00 USD | 17,830.00 USD | 22,250.00 USD |
| `7D` | `50.70` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 53,670.00 USD | 24,710.00 USD | 32,520.00 USD |
| `1D` | `50.80` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 5,630.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `50.80` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD |
| `1D` | `50.90` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 260.05 USD | 8,390.00 USD |
| `7D` | `50.90` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD |
| `1D` | `51.00` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 129.78 USD |
| `7D` | `51.00` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `51.10` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 263.90 USD | 1,160.00 USD | 0.00 USD |
| `7D` | `51.10` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD |
| `1D` | `51.20` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 1,100.00 USD | 1,130.00 USD | 327.72 USD |
| `7D` | `51.20` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD |
| `1D` | `51.30` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 20,430.00 USD | 5,150.00 USD | 18,640.00 USD |
| `7D` | `51.30` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 19,510.00 USD | 12,490.00 USD | 47,090.00 USD |
| `1D` | `51.40` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 17,510.00 USD | 7,090.00 USD | 10,780.00 USD |
| `7D` | `51.40` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 71,090.00 USD | 28,960.00 USD | 45,150.00 USD |
| `1D` | `51.50` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 10,410.00 USD | 8,980.00 USD | 4,080.00 USD |
| `7D` | `51.50` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `51.60` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 8,800.00 USD | 7,990.00 USD | 4,820.00 USD |
| `7D` | `51.60` | 5,250,000.00 USD | 0.00 USD | 5,250,000.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD |
| `1D` | `51.70` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 3,490.00 USD | 4,150.00 USD | 6,480.00 USD |
| `7D` | `51.70` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `51.80` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 12,210.00 USD | 2,080.00 USD | 10,050.00 USD |
| `7D` | `51.80` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD |
| `1D` | `51.90` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 12,520.00 USD | 21,470.00 USD | 9,190.00 USD |
| `7D` | `51.90` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 5,870.00 USD | 15,810.00 USD | 4,760.00 USD |
| `1D` | `52.00` | 968,990.00 USD | 0.00 USD | 968,990.00 USD | 25,150.00 USD | 8,230.00 USD | 23,340.00 USD |
| `7D` | `52.00` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 64,300.00 USD | 20,800.00 USD | 11,880.00 USD |
| `1D` | `52.10` | 912,270.00 USD | 0.00 USD | 912,270.00 USD | 27,630.00 USD | 5,780.00 USD | 35,220.00 USD |
| `7D` | `52.10` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 24,220.00 USD | 18,810.00 USD | 35,480.00 USD |
| `1D` | `52.20` | 843,640.00 USD | 0.00 USD | 843,640.00 USD | 20,520.00 USD | 10,450.00 USD | 14,390.00 USD |
| `7D` | `52.20` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 38,380.00 USD | 4,340.00 USD | 25,270.00 USD |
| `1D` | `52.30` | 798,280.00 USD | 0.00 USD | 798,280.00 USD | 38,870.00 USD | 8,170.00 USD | 16,110.00 USD |
| `7D` | `52.30` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 18,740.00 USD | 12,840.00 USD | 8,940.00 USD |
| `1D` | `52.40` | 735,130.00 USD | 0.00 USD | 735,130.00 USD | 10,040.00 USD | 7,510.00 USD | 6,280.00 USD |
| `7D` | `52.40` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 20,580.00 USD | 11,230.00 USD | 20,050.00 USD |
| `1D` | `52.50` | 711,290.00 USD | 0.00 USD | 711,290.00 USD | 15,070.00 USD | 13,510.00 USD | 998.32 USD |
| `7D` | `52.50` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 33,240.00 USD | 667.05 USD | 10,640.00 USD |
| `1D` | `52.60` | 681,710.00 USD | 0.00 USD | 681,710.00 USD | 2,760.00 USD | 8,750.00 USD | 273.52 USD |
| `7D` | `52.60` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 36,640.00 USD | 14,530.00 USD | 584.77 USD |
| `1D` | `52.70` | 669,920.00 USD | 0.00 USD | 669,920.00 USD | 4,930.00 USD | 7,610.00 USD | 15,080.00 USD |
| `7D` | `52.70` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 20,250.00 USD | 43,820.00 USD | 62,360.00 USD |
| `1D` | `52.80` | 642,300.00 USD | 0.00 USD | 642,300.00 USD | 14,400.00 USD | 14,660.00 USD | 60,330.00 USD |
| `7D` | `52.80` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 46,600.00 USD | 27,850.00 USD | 108.50 USD |
| `1D` | `52.90` | 552,910.00 USD | 0.00 USD | 552,910.00 USD | 28,000.00 USD | 7,150.00 USD | 6,120.00 USD |
| `7D` | `52.90` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 51,920.00 USD | 23,030.00 USD | 3,870.00 USD |
| `1D` | `53.00` | 511,640.00 USD | 0.00 USD | 511,640.00 USD | 4,280.00 USD | 1,860.00 USD | 936.80 USD |
| `7D` | `53.00` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 18,990.00 USD | 8,880.00 USD | 32,670.00 USD |
| `1D` | `53.10` | 504,580.00 USD | 0.00 USD | 504,580.00 USD | 3,280.00 USD | 2,540.00 USD | 669.73 USD |
| `7D` | `53.10` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 52,760.00 USD | 29,200.00 USD | 9,860.00 USD |
| `1D` | `53.20` | 498,090.00 USD | 0.00 USD | 498,090.00 USD | 9,780.00 USD | 13,340.00 USD | 6,370.00 USD |
| `7D` | `53.20` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 90,340.00 USD | 17,580.00 USD | 25,530.00 USD |
| `1D` | `53.30` | 468,610.00 USD | 0.00 USD | 468,610.00 USD | 17,240.00 USD | 4,110.00 USD | 36,250.00 USD |
| `7D` | `53.30` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 63,050.00 USD | 14,250.00 USD | 37,140.00 USD |
| `1D` | `53.40` | 411,010.00 USD | 0.00 USD | 411,010.00 USD | 13,040.00 USD | 3,050.00 USD | 4,930.00 USD |
| `7D` | `53.40` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 48,760.00 USD | 4,350.00 USD | 48,020.00 USD |
| `1D` | `53.50` | 389,990.00 USD | 0.00 USD | 389,990.00 USD | 8,970.00 USD | 4,350.00 USD | 0.00 USD |
| `7D` | `53.50` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 49,490.00 USD | 11,660.00 USD | 22,130.00 USD |
| `1D` | `53.60` | 376,670.00 USD | 0.00 USD | 376,670.00 USD | 12,620.00 USD | 21,080.00 USD | 8,310.00 USD |
| `7D` | `53.60` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 53,580.00 USD | 6,140.00 USD | 10,670.00 USD |
| `1D` | `53.70` | 334,660.00 USD | 0.00 USD | 334,660.00 USD | 5,710.00 USD | 1,100.00 USD | 0.00 USD |
| `7D` | `53.70` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 64,150.00 USD | 16,400.00 USD | 12,890.00 USD |
| `1D` | `53.80` | 327,840.00 USD | 0.00 USD | 327,840.00 USD | 1,830.00 USD | 5,480.00 USD | 3,130.00 USD |
| `7D` | `53.80` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 99,150.00 USD | 80,510.00 USD | 126,140.00 USD |
| `1D` | `53.90` | 317,400.00 USD | 0.00 USD | 317,400.00 USD | 7,480.00 USD | 23,960.00 USD | 98,250.00 USD |
| `7D` | `53.90` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 111,970.00 USD | 52,650.00 USD | 123,850.00 USD |
| `1D` | `54.00` | 187,710.00 USD | 0.00 USD | 187,710.00 USD | 4,010.00 USD | 13,640.00 USD | 0.00 USD |
| `7D` | `54.00` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 344,710.00 USD | 142,130.00 USD | 210,440.00 USD |
| `1D` | `54.10` | 170,070.00 USD | 0.00 USD | 170,070.00 USD | 23,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.10` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 234,120.00 USD | 45,470.00 USD | 138,110.00 USD |
| `1D` | `54.20` | 146,240.00 USD | 0.00 USD | 146,240.00 USD | 14,960.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.20` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 234,980.00 USD | 141,240.00 USD | 128,910.00 USD |
| `1D` | `54.30` | 131,280.00 USD | 0.00 USD | 131,280.00 USD | 9,970.00 USD | 12,300.00 USD | 28,640.00 USD |
| `7D` | `54.30` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 237,140.00 USD | 89,820.00 USD | 181,420.00 USD |
| `1D` | `54.40` | 80,370.00 USD | 0.00 USD | 80,370.00 USD | 17,060.00 USD | 0.00 USD | 57,760.00 USD |
| `7D` | `54.40` | 882,110.00 USD | 0.00 USD | 882,110.00 USD | 304,270.00 USD | 6,020.00 USD | 92,140.00 USD |
| `1D` | `54.50` | 5,550.00 USD | 0.00 USD | 5,550.00 USD | 3,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.50` | 479,680.00 USD | 0.00 USD | 479,680.00 USD | 159,720.00 USD | 8,200.00 USD | 140,930.00 USD |
| `1D` | `54.60` | 2,510.00 USD | 0.00 USD | 2,510.00 USD | 2,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.60` | 170,830.00 USD | 0.00 USD | 170,830.00 USD | 98,430.00 USD | 0.00 USD | 72,400.00 USD |
| `1D` | `54.70` | 117,110.00 USD | 117,110.00 USD | 0.00 USD | 60,000.00 USD | 0.00 USD | 57,100.00 USD |
| `1D` | `54.70` | 234,210.00 USD | 234,210.00 USD | 0.00 USD | 60,000.00 USD | 0.00 USD | 57,100.00 USD |
| `7D` | `54.70` | 118,580.00 USD | 118,580.00 USD | 0.00 USD | 118,580.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.70` | 237,150.00 USD | 237,150.00 USD | 0.00 USD | 118,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `54.80` | 278,340.00 USD | 278,340.00 USD | 0.00 USD | 44,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.80` | 529,770.00 USD | 529,770.00 USD | 0.00 USD | 292,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `54.90` | 324,430.00 USD | 324,430.00 USD | 0.00 USD | 46,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.90` | 771,510.00 USD | 771,510.00 USD | 0.00 USD | 241,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `55.00` | 359,160.00 USD | 359,160.00 USD | 0.00 USD | 34,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.00` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 255,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `55.10` | 375,790.00 USD | 375,790.00 USD | 0.00 USD | 16,450.00 USD | 0.00 USD | 189.61 USD |
| `7D` | `55.10` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 348,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `55.20` | 387,310.00 USD | 387,310.00 USD | 0.00 USD | 11,100.00 USD | 0.00 USD | 420.67 USD |
| `7D` | `55.20` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 336,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `55.30` | 463,770.00 USD | 463,770.00 USD | 0.00 USD | 52,250.00 USD | 0.00 USD | 24,210.00 USD |
| `7D` | `55.30` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 359,480.00 USD | 17,490.00 USD | 187,300.00 USD |
| `7D` | `55.40` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 300,790.00 USD | 0.00 USD | 238,510.00 USD |
| `1D` | `55.50` | 491,100.00 USD | 491,100.00 USD | 0.00 USD | 0.00 USD | 27,320.00 USD | 0.00 USD |
| `7D` | `55.50` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 326,800.00 USD | 167,870.00 USD | 385,110.00 USD |
| `1D` | `55.60` | 512,340.00 USD | 512,340.00 USD | 0.00 USD | 755.00 USD | 20,490.00 USD | 0.00 USD |
| `7D` | `55.60` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 426,340.00 USD | 245,070.00 USD | 248,650.00 USD |
| `1D` | `55.70` | 548,540.00 USD | 548,540.00 USD | 0.00 USD | 0.00 USD | 35,800.00 USD | 407.86 USD |
| `7D` | `55.70` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 174,240.00 USD | 32,180.00 USD | 269,560.00 USD |
| `1D` | `55.80` | 734,290.00 USD | 734,290.00 USD | 0.00 USD | 122,760.00 USD | 16,300.00 USD | 46,680.00 USD |
| `7D` | `55.80` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 60,840.00 USD | 28,930.00 USD | 142,890.00 USD |
| `1D` | `55.90` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 137,200.00 USD | 1,100.00 USD | 139,640.00 USD |
| `7D` | `55.90` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 65,400.00 USD | 65,840.00 USD | 234,280.00 USD |
| `1D` | `56.00` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 124,870.00 USD | 0.00 USD | 59,430.00 USD |
| `7D` | `56.00` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 181,230.00 USD | 98,600.00 USD | 147,270.00 USD |
| `1D` | `56.10` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 105,950.00 USD | 23,960.00 USD | 146,900.00 USD |
| `7D` | `56.10` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 121,920.00 USD | 140,020.00 USD | 61,210.00 USD |
| `1D` | `56.20` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 72,300.00 USD | 73,200.00 USD | 71,790.00 USD |
| `7D` | `56.20` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 104,510.00 USD | 66,120.00 USD | 179,680.00 USD |
| `1D` | `56.30` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 464.20 USD | 31,280.00 USD | 36,880.00 USD |
| `7D` | `56.30` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 91,850.00 USD | 128,970.00 USD | 85,420.00 USD |
| `1D` | `56.40` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 579.50 USD | 30,930.00 USD | 117,360.00 USD |
| `7D` | `56.40` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 215,940.00 USD | 102,460.00 USD | 137,070.00 USD |
| `1D` | `56.50` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 118,430.00 USD | 0.00 USD |
| `7D` | `56.50` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 26,520.00 USD | 83,470.00 USD | 0.00 USD |
| `1D` | `56.60` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 13,870.00 USD | 58,070.00 USD | 57,440.00 USD |
| `7D` | `56.60` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 363,190.00 USD | 119,150.00 USD | 0.00 USD |
| `1D` | `56.70` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 197,080.00 USD | 0.00 USD | 201,730.00 USD |
| `7D` | `56.70` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 110,940.00 USD | 92,780.00 USD | 0.00 USD |
| `1D` | `56.80` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 180,420.00 USD | 2,180.00 USD | 113,990.00 USD |
| `7D` | `56.80` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 153,580.00 USD | 90,850.00 USD | 261,330.00 USD |
| `1D` | `56.90` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 8,150.00 USD | 1,780.00 USD |
| `7D` | `56.90` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 108,440.00 USD | 48,600.00 USD | 92,630.00 USD |
| `1D` | `57.00` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 552.05 USD | 427.23 USD |
| `7D` | `57.00` | 9,250,000.00 USD | 9,250,000.00 USD | 0.00 USD | 50,710.00 USD | 2,620.00 USD | 93,100.00 USD |
| `1D` | `57.10` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 10,960.00 USD | 5,950.00 USD |
| `7D` | `57.10` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 36,580.00 USD | 16,110.00 USD | 20,440.00 USD |
| `1D` | `57.20` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 11,980.00 USD | 49,380.00 USD |
| `7D` | `57.20` | 9,360,000.00 USD | 9,360,000.00 USD | 0.00 USD | 21,160.00 USD | 13,670.00 USD | 3,700.00 USD |
| `1D` | `57.30` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 7,220.00 USD | 386.57 USD |
| `7D` | `57.30` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 22,360.00 USD | 0.00 USD | 3,710.00 USD |
| `1D` | `57.40` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 19,650.00 USD | 25,750.00 USD | 0.00 USD |
| `7D` | `57.40` | 9,590,000.00 USD | 9,590,000.00 USD | 0.00 USD | 38,520.00 USD | 30,000.00 USD | 129,940.00 USD |
| `1D` | `57.50` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 108,670.00 USD | 12,870.00 USD | 36,450.00 USD |
| `7D` | `57.50` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 76,670.00 USD | 23,070.00 USD | 0.00 USD |
| `1D` | `57.60` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 6,150.00 USD | 0.00 USD |
| `7D` | `57.60` | 9,800,000.00 USD | 9,800,000.00 USD | 0.00 USD | 72,680.00 USD | 15,090.00 USD | 26,440.00 USD |
| `1D` | `57.70` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 17,800.00 USD | 1,300.00 USD | 85,990.00 USD |
| `7D` | `57.70` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 0.00 USD | 1,500.00 USD | 57,330.00 USD |
| `1D` | `57.80` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 2,360.00 USD | 0.00 USD | 648.90 USD |
| `7D` | `57.80` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 2,260.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `57.90` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 1,570.00 USD | 6,570.00 USD | 0.00 USD |
| `7D` | `57.90` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `58.00` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 2,170.00 USD | 5,650.00 USD | 0.00 USD |
| `7D` | `58.00` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD | 3,670.00 USD | 0.00 USD |
| `1D` | `58.10` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 29,450.00 USD | 1,180.00 USD | 9,350.00 USD |
| `7D` | `58.10` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD | 848.40 USD |
| `1D` | `58.20` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 5,880.00 USD | 350.42 USD |
| `1D` | `58.30` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 8,940.00 USD | 11,540.00 USD | 36,830.00 USD |
| `7D` | `58.30` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 0.00 USD | 9,580.00 USD | 26,820.00 USD |
| `1D` | `58.40` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 4,990.00 USD | 33,950.00 USD |
| `7D` | `58.40` | 9,960,000.00 USD | 9,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 54,120.00 USD |
| `1D` | `58.50` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 48,820.00 USD | 21,280.00 USD | 379.22 USD |
| `7D` | `58.50` | 9,990,000.00 USD | 9,990,000.00 USD | 0.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD |
| `7D` | `58.60` | 9,990,000.00 USD | 9,990,000.00 USD | 0.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `58.70` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 15,850.00 USD | 8,070.00 USD | 355.85 USD |
| `7D` | `58.70` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 1,700.00 USD | 5,910.00 USD | 35,320.00 USD |
| `1D` | `58.80` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 35,140.00 USD | 14,730.00 USD | 23,630.00 USD |
| `7D` | `58.80` | 10,040,000.00 USD | 10,040,000.00 USD | 0.00 USD | 1,810.00 USD | 3,320.00 USD | 6,410.00 USD |
| `1D` | `58.90` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 18,240.00 USD | 124,640.00 USD | 91,310.00 USD |
| `7D` | `58.90` | 10,170,000.00 USD | 10,170,000.00 USD | 0.00 USD | 0.00 USD | 48,700.00 USD | 83,500.00 USD |
| `1D` | `59.00` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 151,460.00 USD | 57,070.00 USD | 134,010.00 USD |
| `7D` | `59.00` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 255,180.00 USD | 65,270.00 USD | 118,570.00 USD |
| `1D` | `59.10` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 189,650.00 USD | 49,050.00 USD | 186,370.00 USD |
| `7D` | `59.10` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 91,060.00 USD | 45,400.00 USD | 158,780.00 USD |
| `1D` | `59.20` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 158,420.00 USD | 75,700.00 USD | 96,020.00 USD |
| `7D` | `59.20` | 11,250,000.00 USD | 11,250,000.00 USD | 0.00 USD | 153,580.00 USD | 12,460.00 USD | 174,600.00 USD |
| `1D` | `59.30` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 306,360.00 USD | 73,680.00 USD | 143,250.00 USD |
| `7D` | `59.30` | 11,530,000.00 USD | 11,530,000.00 USD | 0.00 USD | 88,710.00 USD | 67,460.00 USD | 119,140.00 USD |
| `1D` | `59.40` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 78,510.00 USD | 57,010.00 USD | 76,960.00 USD |
| `7D` | `59.40` | 11,840,000.00 USD | 11,840,000.00 USD | 0.00 USD | 103,370.00 USD | 73,620.00 USD | 137,500.00 USD |
| `1D` | `59.50` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 119,350.00 USD | 57,690.00 USD | 28,370.00 USD |
| `7D` | `59.50` | 11,990,000.00 USD | 11,990,000.00 USD | 0.00 USD | 67,060.00 USD | 64,710.00 USD | 21,090.00 USD |
| `1D` | `59.60` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 62,780.00 USD | 68,870.00 USD | 18,340.00 USD |
| `7D` | `59.60` | 12,490,000.00 USD | 12,490,000.00 USD | 0.00 USD | 268,680.00 USD | 145,550.00 USD | 86,840.00 USD |
| `1D` | `59.70` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 20,820.00 USD | 30,890.00 USD | 94,130.00 USD |
| `7D` | `59.70` | 12,890,000.00 USD | 12,890,000.00 USD | 0.00 USD | 55,510.00 USD | 180,620.00 USD | 161,880.00 USD |
| `1D` | `59.80` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 40,970.00 USD | 37,360.00 USD | 10,870.00 USD |
| `7D` | `59.80` | 13,260,000.00 USD | 13,260,000.00 USD | 0.00 USD | 118,240.00 USD | 97,600.00 USD | 155,270.00 USD |
| `1D` | `59.90` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 112,870.00 USD | 21,300.00 USD | 80,370.00 USD |
| `7D` | `59.90` | 13,630,000.00 USD | 13,630,000.00 USD | 0.00 USD | 246,770.00 USD | 84,430.00 USD | 40,130.00 USD |
| `1D` | `60.00` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 182,880.00 USD | 64,320.00 USD | 69,570.00 USD |
| `7D` | `60.00` | 14,140,000.00 USD | 14,140,000.00 USD | 0.00 USD | 231,370.00 USD | 183,130.00 USD | 94,160.00 USD |
| `1D` | `60.10` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 95,780.00 USD | 40,300.00 USD | 71,530.00 USD |
| `7D` | `60.10` | 14,710,000.00 USD | 14,710,000.00 USD | 0.00 USD | 263,890.00 USD | 129,860.00 USD | 174,140.00 USD |
| `1D` | `60.20` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 105,780.00 USD | 41,350.00 USD | 96,900.00 USD |
| `7D` | `60.20` | 15,210,000.00 USD | 15,210,000.00 USD | 0.00 USD | 207,990.00 USD | 131,530.00 USD | 157,150.00 USD |
| `1D` | `60.30` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 97,720.00 USD | 76,060.00 USD | 83,130.00 USD |
| `7D` | `60.30` | 15,580,000.00 USD | 15,580,000.00 USD | 0.00 USD | 118,160.00 USD | 95,890.00 USD | 155,610.00 USD |
| `1D` | `60.40` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 168,700.00 USD | 54,240.00 USD | 84,380.00 USD |
| `7D` | `60.40` | 16,030,000.00 USD | 16,030,000.00 USD | 0.00 USD | 93,890.00 USD | 133,310.00 USD | 226,940.00 USD |
| `1D` | `60.50` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 79,160.00 USD | 43,330.00 USD | 63,520.00 USD |
| `7D` | `60.50` | 16,470,000.00 USD | 16,470,000.00 USD | 0.00 USD | 147,230.00 USD | 88,570.00 USD | 207,100.00 USD |
| `1D` | `60.60` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 80,330.00 USD | 34,850.00 USD | 5,340.00 USD |
| `7D` | `60.60` | 16,990,000.00 USD | 16,990,000.00 USD | 0.00 USD | 266,850.00 USD | 98,770.00 USD | 155,390.00 USD |
| `1D` | `60.70` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 74,340.00 USD | 45,070.00 USD | 33,070.00 USD |
| `7D` | `60.70` | 17,220,000.00 USD | 17,220,000.00 USD | 0.00 USD | 129,660.00 USD | 67,510.00 USD | 28,990.00 USD |
| `1D` | `60.80` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 22,530.00 USD | 11,950.00 USD | 43,340.00 USD |
| `7D` | `60.80` | 17,450,000.00 USD | 17,450,000.00 USD | 0.00 USD | 54,870.00 USD | 78,710.00 USD | 94,850.00 USD |
| `1D` | `60.90` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 40,050.00 USD | 21,020.00 USD | 0.00 USD |
| `7D` | `60.90` | 17,730,000.00 USD | 17,730,000.00 USD | 0.00 USD | 139,720.00 USD | 52,860.00 USD | 92,420.00 USD |
| `1D` | `61.00` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 46,000.00 USD | 6,970.00 USD | 28,080.00 USD |
| `7D` | `61.00` | 17,870,000.00 USD | 17,870,000.00 USD | 0.00 USD | 96,160.00 USD | 36,500.00 USD | 5,370.00 USD |
| `1D` | `61.10` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 6,110.00 USD | 0.00 USD | 11,490.00 USD |
| `7D` | `61.10` | 17,900,000.00 USD | 17,900,000.00 USD | 0.00 USD | 31,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `61.20` | 8,590,000.00 USD | 8,590,000.00 USD | 0.00 USD | 75,930.00 USD | 1,160.00 USD | 19,110.00 USD |
| `7D` | `61.20` | 18,120,000.00 USD | 18,120,000.00 USD | 0.00 USD | 116,610.00 USD | 70,180.00 USD | 33,350.00 USD |
| `1D` | `61.30` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 9,540.00 USD | 6,080.00 USD | 2,340.00 USD |
| `7D` | `61.30` | 18,270,000.00 USD | 18,270,000.00 USD | 0.00 USD | 51,130.00 USD | 35,650.00 USD | 55,130.00 USD |
| `1D` | `61.40` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 6,350.00 USD | 7,530.00 USD | 1,670.00 USD |
| `7D` | `61.40` | 18,420,000.00 USD | 18,420,000.00 USD | 0.00 USD | 89,350.00 USD | 41,800.00 USD | 24,650.00 USD |
| `1D` | `61.50` | 8,670,000.00 USD | 8,670,000.00 USD | 0.00 USD | 9,120.00 USD | 19,960.00 USD | 17,790.00 USD |
| `7D` | `61.50` | 18,510,000.00 USD | 18,510,000.00 USD | 0.00 USD | 19,810.00 USD | 35,300.00 USD | 36,110.00 USD |
| `1D` | `61.60` | 8,730,000.00 USD | 8,730,000.00 USD | 0.00 USD | 24,180.00 USD | 14,990.00 USD | 20,400.00 USD |
| `7D` | `61.60` | 18,760,000.00 USD | 18,760,000.00 USD | 0.00 USD | 54,240.00 USD | 63,390.00 USD | 132,550.00 USD |
| `1D` | `61.70` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 37,720.00 USD | 9,670.00 USD | 12,390.00 USD |
| `7D` | `61.70` | 18,980,000.00 USD | 18,980,000.00 USD | 0.00 USD | 91,980.00 USD | 12,880.00 USD | 114,850.00 USD |
| `1D` | `61.80` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 23,640.00 USD | 8,420.00 USD | 1,570.00 USD |
| `7D` | `61.80` | 19,300,000.00 USD | 19,300,000.00 USD | 0.00 USD | 167,990.00 USD | 62,660.00 USD | 86,520.00 USD |
| `1D` | `61.90` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 28,490.00 USD | 11,940.00 USD | 16,200.00 USD |
| `7D` | `61.90` | 19,440,000.00 USD | 19,440,000.00 USD | 0.00 USD | 72,380.00 USD | 29,730.00 USD | 35,860.00 USD |
| `1D` | `62.00` | 8,900,000.00 USD | 8,900,000.00 USD | 0.00 USD | 14,630.00 USD | 911.46 USD | 2,750.00 USD |
| `7D` | `62.00` | 19,560,000.00 USD | 19,560,000.00 USD | 0.00 USD | 56,450.00 USD | 13,260.00 USD | 49,920.00 USD |
| `1D` | `62.10` | 8,910,000.00 USD | 8,910,000.00 USD | 0.00 USD | 12,050.00 USD | 945.47 USD | 0.00 USD |
| `7D` | `62.10` | 19,620,000.00 USD | 19,620,000.00 USD | 0.00 USD | 36,500.00 USD | 12,820.00 USD | 13,950.00 USD |
| `1D` | `62.20` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 3,350.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.20` | 19,740,000.00 USD | 19,740,000.00 USD | 0.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD |
| `1D` | `62.30` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 464.20 USD | 260.05 USD | 8,390.00 USD |
| `7D` | `62.30` | 19,890,000.00 USD | 19,890,000.00 USD | 0.00 USD | 35,280.00 USD | 23,450.00 USD | 97,450.00 USD |
| `1D` | `62.40` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 1,150.00 USD | 0.00 USD | 129.78 USD |
| `7D` | `62.40` | 20,030,000.00 USD | 20,030,000.00 USD | 0.00 USD | 79,620.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `62.50` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 263.90 USD | 1,160.00 USD | 0.00 USD |
| `7D` | `62.50` | 20,120,000.00 USD | 20,120,000.00 USD | 0.00 USD | 44,300.00 USD | 14,320.00 USD | 26,610.00 USD |
| `1D` | `62.60` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 1,100.00 USD | 1,130.00 USD | 327.72 USD |
| `7D` | `62.60` | 20,190,000.00 USD | 20,190,000.00 USD | 0.00 USD | 34,910.00 USD | 7,830.00 USD | 27,730.00 USD |
| `1D` | `62.70` | 8,970,000.00 USD | 8,970,000.00 USD | 0.00 USD | 19,390.00 USD | 5,150.00 USD | 18,640.00 USD |
| `7D` | `62.70` | 20,270,000.00 USD | 20,270,000.00 USD | 0.00 USD | 22,020.00 USD | 12,490.00 USD | 47,090.00 USD |
| `1D` | `62.80` | 9,010,000.00 USD | 9,010,000.00 USD | 0.00 USD | 16,430.00 USD | 7,090.00 USD | 10,780.00 USD |
| `7D` | `62.80` | 20,410,000.00 USD | 20,410,000.00 USD | 0.00 USD | 72,250.00 USD | 28,960.00 USD | 45,150.00 USD |
| `1D` | `62.90` | 9,030,000.00 USD | 9,030,000.00 USD | 0.00 USD | 8,780.00 USD | 8,980.00 USD | 4,080.00 USD |
| `7D` | `62.90` | 20,510,000.00 USD | 20,510,000.00 USD | 0.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `63.00` | 9,050,000.00 USD | 9,050,000.00 USD | 0.00 USD | 7,800.00 USD | 7,990.00 USD | 4,820.00 USD |
| `7D` | `63.00` | 20,570,000.00 USD | 20,570,000.00 USD | 0.00 USD | 34,730.00 USD | 12,240.00 USD | 17,650.00 USD |
| `1D` | `63.10` | 9,060,000.00 USD | 9,060,000.00 USD | 0.00 USD | 4,260.00 USD | 4,150.00 USD | 6,480.00 USD |
| `7D` | `63.10` | 20,610,000.00 USD | 20,610,000.00 USD | 0.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `63.20` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 2,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `63.30` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 4,590.00 USD | 594.25 USD | 2,790.00 USD |
| `7D` | `63.30` | 20,650,000.00 USD | 20,650,000.00 USD | 0.00 USD | 19,680.00 USD | 11,500.00 USD | 9,730.00 USD |
| `1D` | `63.40` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 8,400.00 USD | 1,480.00 USD | 7,260.00 USD |
| `7D` | `63.40` | 20,680,000.00 USD | 20,680,000.00 USD | 0.00 USD | 13,220.00 USD | 1,320.00 USD | 9,960.00 USD |
| `1D` | `63.50` | 9,130,000.00 USD | 9,130,000.00 USD | 0.00 USD | 12,520.00 USD | 21,470.00 USD | 9,190.00 USD |
| `7D` | `63.50` | 20,700,000.00 USD | 20,700,000.00 USD | 0.00 USD | 6,620.00 USD | 15,810.00 USD | 4,760.00 USD |
| `1D` | `63.60` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 25,150.00 USD | 8,230.00 USD | 23,340.00 USD |
| `7D` | `63.60` | 20,800,000.00 USD | 20,800,000.00 USD | 0.00 USD | 63,480.00 USD | 20,800.00 USD | 11,880.00 USD |
| `1D` | `63.70` | 9,260,000.00 USD | 9,260,000.00 USD | 0.00 USD | 27,630.00 USD | 5,780.00 USD | 35,220.00 USD |
| `7D` | `63.70` | 20,870,000.00 USD | 20,870,000.00 USD | 0.00 USD | 21,940.00 USD | 18,810.00 USD | 35,480.00 USD |
| `1D` | `63.80` | 9,300,000.00 USD | 9,300,000.00 USD | 0.00 USD | 19,730.00 USD | 10,450.00 USD | 14,390.00 USD |
| `7D` | `63.80` | 20,940,000.00 USD | 20,940,000.00 USD | 0.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD |
| `1D` | `63.90` | 9,360,000.00 USD | 9,360,000.00 USD | 0.00 USD | 34,930.00 USD | 8,170.00 USD | 16,110.00 USD |
| `7D` | `63.90` | 20,970,000.00 USD | 20,970,000.00 USD | 0.00 USD | 7,650.00 USD | 12,840.00 USD | 8,940.00 USD |
| `1D` | `64.00` | 9,380,000.00 USD | 9,380,000.00 USD | 0.00 USD | 7,880.00 USD | 6,900.00 USD | 6,280.00 USD |
| `7D` | `64.00` | 21,010,000.00 USD | 21,010,000.00 USD | 0.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD |
| `1D` | `64.10` | 9,400,000.00 USD | 9,400,000.00 USD | 0.00 USD | 13,740.00 USD | 5,360.00 USD | 80.02 USD |
| `7D` | `64.10` | 21,040,000.00 USD | 21,040,000.00 USD | 0.00 USD | 20,350.00 USD | 667.05 USD | 10,640.00 USD |
| `1D` | `64.20` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 2,760.00 USD | 8,200.00 USD | 273.52 USD |
| `7D` | `64.20` | 21,090,000.00 USD | 21,090,000.00 USD | 0.00 USD | 28,840.00 USD | 14,530.00 USD | 584.77 USD |
| `1D` | `64.40` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 0.00 USD | 946.37 USD | 13,440.00 USD |
| `7D` | `64.40` | 21,140,000.00 USD | 21,140,000.00 USD | 0.00 USD | 2,540.00 USD | 20,590.00 USD | 29,110.00 USD |
| `7D` | `64.50` | 21,170,000.00 USD | 21,170,000.00 USD | 0.00 USD | 7,700.00 USD | 7,120.00 USD | 13,310.00 USD |
| `7D` | `64.60` | 21,210,000.00 USD | 21,210,000.00 USD | 0.00 USD | 32,220.00 USD | 14,180.00 USD | 108.50 USD |
| `7D` | `64.70` | 21,280,000.00 USD | 21,280,000.00 USD | 0.00 USD | 39,430.00 USD | 23,030.00 USD | 3,870.00 USD |
| `7D` | `64.80` | 21,320,000.00 USD | 21,320,000.00 USD | 0.00 USD | 7,540.00 USD | 8,210.00 USD | 20,430.00 USD |
| `7D` | `64.90` | 21,360,000.00 USD | 21,360,000.00 USD | 0.00 USD | 25,320.00 USD | 8,010.00 USD | 9,860.00 USD |
| `7D` | `65.00` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 1,790.00 USD | 9,480.00 USD | 13,480.00 USD |
| `7D` | `65.10` | 21,440,000.00 USD | 21,440,000.00 USD | 0.00 USD | 5,810.00 USD | 14,250.00 USD | 37,140.00 USD |
| `7D` | `65.20` | 21,480,000.00 USD | 21,480,000.00 USD | 0.00 USD | 10,380.00 USD | 2,250.00 USD | 28,420.00 USD |
| `7D` | `65.30` | 21,530,000.00 USD | 21,530,000.00 USD | 0.00 USD | 22,330.00 USD | 9,180.00 USD | 22,130.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `414.45M` | Total OI Tokens: `7,569,977.2 LTC`
  * 1h OI Change: `-8.04%` | 4h OI Change: `-9.33%` | 24h OI Change: `-11.03%`
  * Exchange Breakdown: Binance=`75.82M` | Bybit=`64.77M` | OKX=`33.29M` | Hyperliquid=`21.37M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `13.43K` | Last 24h: `36.85K` | Last 3d: `60.07K` | Last 7d: `106.71K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0098%` | **USDT OKX** | `0.0022%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0073%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0060%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `45.54%` | `54.46%` | `0.84` | 42,950,000.00 USD |
| `15M` | `Binance` | `41.76%` | `58.24%` | `0.72` | 15,900,000.00 USD |
| `15M` | `OKX` | `47.6%` | `52.4%` | `0.91` | 5,650,000.00 USD |
| `15M` | `Bybit` | `44.93%` | `55.07%` | `0.82` | 5,900,000.00 USD |
| `15M` | `KuCoin` | `43.19%` | `56.81%` | `0.76` | 855,440.00 USD |
| `15M` | `Gate` | `56.23%` | `43.77%` | `1.28` | 4,060,000.00 USD |
| `15M` | `Bitget` | `50.96%` | `49.04%` | `1.04` | 2,470,000.00 USD |
| `15M` | `BingX` | `39.23%` | `60.77%` | `0.65` | 823,250.00 USD |
| `15M` | `MEXC` | `39.3%` | `60.7%` | `0.65` | 2,290,000.00 USD |
| `15M` | `Bitunix` | `45.93%` | `54.07%` | `0.85` | 1,210,000.00 USD |
| `15M` | `Hyperliquid` | `53.32%` | `46.68%` | `1.14` | 948,080.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.61%` | `49.39%` | `1.02` | 2,450,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `17.51%` | `82.49%` | `0.21` | 138,460.00 USD |
| `15M` | `HTX` | `57.55%` | `42.45%` | `1.36` | 77,480.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `37.35%` | `62.65%` | `0.60` | 117,030.00 USD |
| `15M` | `Aster` | `52.04%` | `47.96%` | `1.09` | 67,810.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `41.76%` | `58.24%` | `0.72` | 15,900,000.00 USD |
| `15M` | `Global Accounts` | `45.54%` | `54.46%` | `0.84` | 42,950,000.00 USD |
| `1H` | `LTC` | `44.22%` | `55.78%` | `0.79` | 69,130,000.00 USD |
| `1H` | `Binance` | `42.44%` | `57.56%` | `0.74` | 25,480,000.00 USD |
| `1H` | `OKX` | `46.18%` | `53.82%` | `0.86` | 8,590,000.00 USD |
| `1H` | `Bybit` | `41.18%` | `58.82%` | `0.70` | 9,050,000.00 USD |
| `1H` | `KuCoin` | `44.56%` | `55.44%` | `0.80` | 1,390,000.00 USD |
| `1H` | `Gate` | `53.16%` | `46.84%` | `1.13` | 6,900,000.00 USD |
| `1H` | `Bitget` | `46.99%` | `53.01%` | `0.89` | 3,810,000.00 USD |
| `1H` | `BingX` | `39.08%` | `60.92%` | `0.64` | 1,360,000.00 USD |
| `1H` | `MEXC` | `38.5%` | `61.5%` | `0.63` | 4,100,000.00 USD |
| `1H` | `Bitunix` | `45.95%` | `54.05%` | `0.85` | 1,980,000.00 USD |
| `1H` | `Hyperliquid` | `49.06%` | `50.94%` | `0.96` | 1,460,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.19%` | `52.81%` | `0.89` | 4,170,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `18.67%` | `81.33%` | `0.23` | 421,180.00 USD |
| `1H` | `HTX` | `52.2%` | `47.8%` | `1.09` | 106,080.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `47.84%` | `52.16%` | `0.92` | 222,030.00 USD |
| `1H` | `Aster` | `45.63%` | `54.37%` | `0.84` | 88,620.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `42.44%` | `57.56%` | `0.74` | 25,480,000.00 USD |
| `1H` | `Global Accounts` | `44.22%` | `55.78%` | `0.79` | 69,130,000.00 USD |
| `4H` | `LTC` | `45.19%` | `54.81%` | `0.82` | 93,360,000.00 USD |
| `4H` | `Binance` | `44.37%` | `55.63%` | `0.80` | 34,370,000.00 USD |
| `4H` | `OKX` | `46.93%` | `53.07%` | `0.88` | 10,730,000.00 USD |
| `4H` | `Bybit` | `42.78%` | `57.22%` | `0.75` | 11,110,000.00 USD |
| `4H` | `KuCoin` | `47.15%` | `52.85%` | `0.89` | 2,610,000.00 USD |
| `4H` | `Gate` | `52.08%` | `47.92%` | `1.09` | 7,990,000.00 USD |
| `4H` | `Bitget` | `47.88%` | `52.12%` | `0.92` | 4,590,000.00 USD |
| `4H` | `BingX` | `40.65%` | `59.35%` | `0.68` | 3,190,000.00 USD |
| `4H` | `MEXC` | `41.36%` | `58.64%` | `0.71` | 5,440,000.00 USD |
| `4H` | `Bitunix` | `47.09%` | `52.91%` | `0.89` | 2,480,000.00 USD |
| `4H` | `Hyperliquid` | `45.15%` | `54.85%` | `0.82` | 1,740,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.35%` | `50.65%` | `0.97` | 7,340,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `14.46%` | `85.54%` | `0.17` | 1,240,000.00 USD |
| `4H` | `HTX` | `52.99%` | `47.01%` | `1.13` | 126,200.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `48.8%` | `51.2%` | `0.95` | 307,060.00 USD |
| `4H` | `Aster` | `43.91%` | `56.09%` | `0.78` | 98,940.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `44.37%` | `55.63%` | `0.80` | 34,370,000.00 USD |
| `4H` | `Global Accounts` | `45.19%` | `54.81%` | `0.82` | 93,360,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `57.59` | `57.70` | `57.59` | `57.88` | `57.55` | 407,665.08 USD | 260,874.04 USD | 146,791.04 USD | 114,082.99 USD | `+27.98%` | `15B / 1S` |
| `0:00 UTC` | `57.56` | `57.61` | `57.56` | `57.77` | `57.55` | 421,492.76 USD | 256,306.11 USD | 165,186.65 USD | 91,119.46 USD | `+21.62%` | `3B / 4S` |
| `5:00 UTC` | `57.83` | `57.80` | `57.83` | `57.94` | `57.61` | 405,316.11 USD | 265,776.17 USD | 139,539.93 USD | 126,236.24 USD | `+31.15%` | `10B / 0S` |
| `0:00 UTC` | `57.98` | `57.97` | `57.98` | `58.05` | `57.84` | 364,891.83 USD | 190,130.13 USD | 174,761.70 USD | 15,368.44 USD | `+4.21%` | `2B / 2S` |
| `5:00 UTC` | `58.02` | `58.02` | `58.02` | `58.16` | `57.89` | 452,756.15 USD | 221,914.68 USD | 230,841.47 USD | -8,926.79 USD | `-1.97%` | `3B / 4S` |
| `0:00 UTC` | `57.00` | `57.30` | `57.00` | `58.02` | `56.86` | 3,333,793.29 USD | 1,387,460.39 USD | 1,946,332.90 USD | -558,872.51 USD | `-16.76%` | `8B / 29S` |
| `5:00 UTC` | `57.25` | `57.29` | `57.25` | `57.45` | `57.14` | 618,298.97 USD | 355,257.55 USD | 263,041.42 USD | 92,216.13 USD | `+14.91%` | `5B / 2S` |
| `0:00 UTC` | `56.60` | `56.15` | `56.60` | `57.32` | `55.30` | 7,177,688.25 USD | 3,006,268.39 USD | 4,171,419.87 USD | -1,165,151.48 USD | `-16.23%` | `6B / 23S` |
| `5:00 UTC` | `55.00` | `54.96` | `55.00` | `55.59` | `54.17` | 11,110,862.71 USD | 4,658,705.25 USD | 6,452,157.46 USD | -1,793,452.21 USD | `-16.14%` | `3B / 23S` |
| `0:00 UTC` | `54.81` | `54.83` | `54.81` | `55.19` | `54.53` | 1,118,511.65 USD | 730,071.44 USD | 388,440.22 USD | 341,631.22 USD | `+30.54%` | `17B / 5S` |

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
| `5m` | -149,780.00 USD | 1,110,000.00 USD | **`ACCUMULATION`** |
| `15m` | -1,770,000.00 USD | -4,460,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -2,040,000.00 USD | -5,520,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,160,000.00 USD | -6,250,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -2,150,000.00 USD | -5,470,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,760,000.00 USD | -6,190,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -784,290.00 USD | -5,550,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -691,870.00 USD | -3,900,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 283,630.00 USD | -2,780,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -128,150.00 USD | -7,360,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 3,480,000.00 USD | -26,250,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -22,200,000.00 USD | -194,910,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-149.78K` | 15m=`-1.77M` | 1h=`-2.16M` | 24h=`-128.15K`
* Futures Capital Netflows: 5m=`+1.11M` | 15m=`-4.46M` | 1h=`-6.25M` | 24h=`-7.36M`
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
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:30:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `56.83` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `55.81` (Risk Distance: `1.02` pts)
  * +2.5R Take Profit: `59.39`
  * Mathematical Lot Sizing: **`9.77 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `58.36` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `59.38` (Risk Distance: `1.02` pts)
  * +2.5R Take Profit: `55.80`
  * Mathematical Lot Sizing: **`9.77 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`55.66`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
