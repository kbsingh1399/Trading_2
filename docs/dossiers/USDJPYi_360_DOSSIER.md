# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USDJPY
**Canonical Key**: `USDJPY` | **Broker Instrument**: `USDJPY.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 11:35:25 IST` (`2026-10-30 06:05:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `157.60` | **Live Ask Quote**: `157.60` | **Mid Price**: `157.60`
- **Spread Points**: `2.00` | **Spread BPS**: `0.13 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `100,000.0` | Digits: `3` | Point: `0.001`
  * Point Value (1.0 Lot): `100.00 USD` | Point Value (0.01 Lot): `1.0000 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`50.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `157.45` | VWAP Z-Score: `+1.32` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1398` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `55.29` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `157.84` | Lower -3.00σ Band: `157.05`
  * Upper +2.51σ Band: `157.78` | Lower -2.51σ Band: `157.12`
  * Upper +2.01σ Band: `157.71` | Lower -2.01σ Band: `157.18`
  * Upper +2.00σ Band: `157.71` | Lower -2.00σ Band: `157.18`
  * Upper +1.28σ Band: `157.62` | Lower -1.28σ Band: `157.28`
  * Upper +1.00σ Band: `157.58` | Lower -1.00σ Band: `157.32`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`157.51` | EMA-20=`157.49` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`157.59` (Slope: `+0.0000`) | EMA-100=`157.70`
  * Institutional Anchors: EMA-144=`157.74` | EMA-200=`157.77` (Slope: `-0.0279`) | EMA-233=`157.78`
- **Range Boundaries**: 24H High=`158.13` | 24H Low=`157.12` | Weekly High=`158.35` | Weekly Low=`157.12`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `157.61` (Distance: `-0.01%`)
  * Point of Control (POC) = `157.45` (Distance: `+0.10%`)
  * Value Area Low (VAL) = `157.24` (Distance: `+0.23%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`157.99` | POC=`157.87` | VAL=`157.76`
  * Prior Day Extremes: PDH=`158.13` | PDL=`157.60` | PDC=`157.69`
  * Monday Range Blueprint: High=`157.64` | Mid=`157.15` | Low=`156.65`
  * Developing Weekly Value Area: Weekly VAH=`158.06` | Weekly POC=`157.87` | Weekly VAL=`157.44`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`157.90` | Low=`157.12`
  * London Session (08:00-16:00 UTC): High=`157.70` | Low=`157.40`
  * New York Session (13:00-21:00 UTC): High=`158.54` | Low=`156.65`
  * Initial Balance (First Hour): IB High=`157.70` | IB Low=`157.40`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `156.97` - `158.23`
  * Optimal Trade Entry (OTE 0.705): `157.91`
  * Structural Invalidation Anchor (0.786): `158.86`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `157.48` | `157.53` | `157.46` | `157.48` | `488` | 76,849.26 USD | -20,310.16 USD | `-26.43%` | 486,470.03 USD | `-0.22` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `157.48` | `157.53` | `157.47` | `157.49` | `335` | 52,758.14 USD | -9,255.81 USD | `-17.54%` | 477,214.21 USD | `-0.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `157.49` | `157.51` | `157.43` | `157.46` | `282` | 44,402.59 USD | -16,584.10 USD | `-37.35%` | 460,630.11 USD | `-0.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `157.43` | `157.55` | `157.42` | `157.46` | `2,804` | 441,523.45 USD | -18,679.84 USD | `-4.23%` | -42,770.59 USD | `-0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `157.46` | `157.53` | `157.45` | `157.48` | `1,669` | 262,839.13 USD | 7,467.02 USD | `+2.84%` | -35,303.56 USD | `+0.11` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `157.48` | `157.53` | `157.43` | `157.46` | `1,105` | 173,988.88 USD | -65,245.83 USD | `-37.50%` | -100,549.39 USD | `-0.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `157.81` | `157.90` | `157.31` | `157.36` | `12,235` | 1,925,262.90 USD | -1,548,081.92 USD | `-80.41%` | -1,144,679.06 USD | `-2.67` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `157.36` | `157.50` | `157.19` | `157.42` | `16,438` | 2,587,735.71 USD | 925,962.94 USD | `+35.78%` | -218,716.12 USD | `+1.55` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `157.43` | `157.59` | `157.42` | `157.58` | `6,490` | 1,022,687.71 USD | 869,872.31 USD | `+85.06%` | 651,156.18 USD | `+1.31` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `157.88` | `157.98` | `157.63` | `157.69` | `20,300` | 3,201,147.60 USD | -1,948,126.97 USD | `-60.86%` | -212,851.23 USD | `-0.93` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.64` | `157.90` | `157.31` | `157.36` | `20,459` | 3,219,366.86 USD | -2,125,220.88 USD | `-66.01%` | -2,338,072.11 USD | `-0.83` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.36` | `157.63` | `157.12` | `157.43` | `39,720` | 6,253,000.44 USD | 1,103,833.41 USD | `+17.65%` | -1,234,238.70 USD | `+0.68` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `157.87` | `158.08` | `157.81` | `158.06` | `23,822` | 3,765,376.79 USD | 3,094,533.80 USD | `+82.18%` | 3,521,504.93 USD | `+1.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `158.06` | `158.13` | `157.71` | `157.88` | `37,561` | 5,930,280.92 USD | -1,786,229.19 USD | `-30.12%` | 1,735,275.74 USD | `-1.19` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.88` | `157.98` | `157.63` | `157.69` | `20,300` | 3,201,147.60 USD | -1,948,126.97 USD | `-60.86%` | -212,851.23 USD | `-0.93` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.64` | `157.90` | `157.31` | `157.36` | `20,459` | 3,219,366.86 USD | -2,125,220.88 USD | `-66.01%` | -2,338,072.11 USD | `-0.83` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.36` | `157.63` | `157.12` | `157.43` | `39,720` | 6,253,000.44 USD | 1,103,833.41 USD | `+17.65%` | -1,234,238.70 USD | `+0.68` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `BID/ASK` | None | `0.0000` | 0.00 USD | `0.00%` | Unarmored | `0.0%` | Interbank L2 | NONE |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Hyperdash | Resting Book | - | - | - | Normal Interbank Book | - | - |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `205` | `0x0911...129a` | `SHORT` | 10,432,802.93 USD | `66,223.20` | `156.58` | `157.56` | `167.72` | -63,782.70 USD | `-0.61%` | `20X Isolated` |
| `1020` | `0x9dea...d617` | `LONG` | 2,137,477.70 USD | `13,566.98` | `157.66` | `157.56` | `149.22` | -1,536.05 USD | `-0.07%` | `50X Isolated` |
| `1103` | `0xec0b...b078` | `SHORT` | 1,987,885.55 USD | `12,617.49` | `158.22` | `157.56` | `162.95` | 8,480.12 USD | `+0.43%` | `20X Isolated` |
| `1146` | `0xc966...f6b6` | `SHORT` | 1,933,596.97 USD | `12,272.91` | `157.61` | `157.56` | `215.27` | 680.68 USD | `+0.04%` | `5X Isolated` |
| `1185` | `0xbef1...d2e5` | `LONG` | 1,862,326.03 USD | `11,821.29` | `157.63` | `157.56` | `155.50` | -1,034.58 USD | `-0.06%` | `50X Isolated` |
| `1877` | `0x3d89...eb14` | `LONG` | 1,087,095.00 USD | `6,900.00` | `158.17` | `157.56` | `127.35` | -4,294.60 USD | `-0.40%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Matrix | Interbank Flow | - | - | - | - | - | - | Interbank Tier |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Map | Near Money | - | - | - | - | 0.00% | - |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `141.50` | 90,340.00 USD | 0.00 USD | 90,340.00 USD | 0.00 USD | 0.00 USD | 5.35 USD |
| `1D` | `141.60` | 6,500.00 USD | 0.00 USD | 6,500.00 USD | 0.00 USD | 0.00 USD | 127.68 USD |
| `7D` | `141.67` | 90,340.00 USD | 0.00 USD | 90,340.00 USD | 0.00 USD | 0.00 USD | 161.17 USD |
| `1D` | `141.76` | 6,380.00 USD | 0.00 USD | 6,380.00 USD | 0.00 USD | 0.00 USD | 46.11 USD |
| `7D` | `141.84` | 90,170.00 USD | 0.00 USD | 90,170.00 USD | 0.00 USD | 0.00 USD | 1,410.00 USD |
| `1D` | `141.92` | 6,330.00 USD | 0.00 USD | 6,330.00 USD | 0.00 USD | 0.00 USD | 155.35 USD |
| `7D` | `142.01` | 88,760.00 USD | 0.00 USD | 88,760.00 USD | 0.00 USD | 0.00 USD | 1,850.00 USD |
| `1D` | `142.08` | 6,170.00 USD | 0.00 USD | 6,170.00 USD | 0.00 USD | 0.00 USD | 3.39 USD |
| `7D` | `142.18` | 86,920.00 USD | 0.00 USD | 86,920.00 USD | 0.00 USD | 0.00 USD | 882.31 USD |
| `7D` | `150.34` | 86,040.00 USD | 0.00 USD | 86,040.00 USD | 0.00 USD | 0.00 USD | 9.96 USD |
| `7D` | `150.51` | 86,030.00 USD | 0.00 USD | 86,030.00 USD | 0.00 USD | 0.00 USD | 537.66 USD |
| `7D` | `150.68` | 85,490.00 USD | 0.00 USD | 85,490.00 USD | 0.00 USD | 0.00 USD | 119.34 USD |
| `7D` | `150.85` | 85,370.00 USD | 0.00 USD | 85,370.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `1D` | `150.88` | 6,170.00 USD | 0.00 USD | 6,170.00 USD | 0.00 USD | 0.00 USD | 17.97 USD |
| `7D` | `151.02` | 85,360.00 USD | 0.00 USD | 85,360.00 USD | 0.00 USD | 0.00 USD | 55.10 USD |
| `1D` | `151.04` | 6,150.00 USD | 0.00 USD | 6,150.00 USD | 0.00 USD | 0.00 USD | 323.31 USD |
| `7D` | `151.19` | 85,300.00 USD | 0.00 USD | 85,300.00 USD | 0.00 USD | 0.00 USD | 567.29 USD |
| `1D` | `151.20` | 5,830.00 USD | 0.00 USD | 5,830.00 USD | 0.00 USD | 0.00 USD | 115.34 USD |
| `1D` | `151.36` | 5,710.00 USD | 0.00 USD | 5,710.00 USD | 0.00 USD | 0.00 USD | 408.85 USD |
| `7D` | `151.36` | 84,730.00 USD | 0.00 USD | 84,730.00 USD | 0.00 USD | 0.00 USD | 5,480.00 USD |
| `1D` | `151.52` | 5,300.00 USD | 0.00 USD | 5,300.00 USD | 0.00 USD | 0.00 USD | 16.01 USD |
| `7D` | `151.53` | 79,250.00 USD | 0.00 USD | 79,250.00 USD | 0.00 USD | 0.00 USD | 2,780.00 USD |
| `7D` | `151.70` | 76,480.00 USD | 0.00 USD | 76,480.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD |
| `7D` | `153.57` | 73,740.00 USD | 0.00 USD | 73,740.00 USD | 0.00 USD | 0.00 USD | 841.62 USD |
| `7D` | `153.74` | 72,900.00 USD | 0.00 USD | 72,900.00 USD | 0.00 USD | 0.00 USD | 492.31 USD |
| `1D` | `154.08` | 5,290.00 USD | 0.00 USD | 5,290.00 USD | 0.00 USD | 0.00 USD | 68.74 USD |
| `7D` | `154.08` | 72,410.00 USD | 0.00 USD | 72,410.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `1D` | `154.24` | 5,220.00 USD | 0.00 USD | 5,220.00 USD | 0.00 USD | 0.00 USD | 668.64 USD |
| `7D` | `154.25` | 72,380.00 USD | 0.00 USD | 72,380.00 USD | 0.00 USD | 0.00 USD | 805.82 USD |
| `1D` | `154.40` | 4,550.00 USD | 0.00 USD | 4,550.00 USD | 0.00 USD | 0.00 USD | 674.24 USD |
| `7D` | `154.42` | 71,580.00 USD | 0.00 USD | 71,580.00 USD | 0.00 USD | 0.00 USD | 5,590.00 USD |
| `1D` | `154.56` | 3,880.00 USD | 0.00 USD | 3,880.00 USD | 0.00 USD | 0.00 USD | 351.35 USD |
| `7D` | `154.59` | 65,990.00 USD | 0.00 USD | 65,990.00 USD | 0.00 USD | 0.00 USD | 9,250.00 USD |
| `7D` | `154.76` | 56,740.00 USD | 0.00 USD | 56,740.00 USD | 0.00 USD | 0.00 USD | 7,570.00 USD |
| `7D` | `155.10` | 49,160.00 USD | 0.00 USD | 49,160.00 USD | 0.00 USD | 0.00 USD | 954.59 USD |
| `7D` | `155.27` | 48,210.00 USD | 0.00 USD | 48,210.00 USD | 0.00 USD | 0.00 USD | 1,240.00 USD |
| `7D` | `155.44` | 46,970.00 USD | 0.00 USD | 46,970.00 USD | 0.00 USD | 0.00 USD | 477.37 USD |
| `7D` | `155.61` | 46,500.00 USD | 0.00 USD | 46,500.00 USD | 0.00 USD | 0.00 USD | 53.53 USD |
| `1D` | `155.68` | 3,530.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD | 0.00 USD | 1,260.00 USD |
| `7D` | `155.78` | 46,440.00 USD | 0.00 USD | 46,440.00 USD | 0.00 USD | 0.00 USD | 977.64 USD |
| `1D` | `155.84` | 2,270.00 USD | 0.00 USD | 2,270.00 USD | 0.00 USD | 0.00 USD | 239.05 USD |
| `7D` | `155.95` | 45,460.00 USD | 0.00 USD | 45,460.00 USD | 0.00 USD | 0.00 USD | 4,090.00 USD |
| `1D` | `156.00` | 2,030.00 USD | 0.00 USD | 2,030.00 USD | 0.00 USD | 0.00 USD | 1,850.00 USD |
| `7D` | `156.12` | 41,370.00 USD | 0.00 USD | 41,370.00 USD | 0.00 USD | 0.00 USD | 20,340.00 USD |
| `1D` | `156.16` | 179.88 USD | 0.00 USD | 179.88 USD | 0.00 USD | 0.00 USD | 179.88 USD |
| `7D` | `156.29` | 21,030.00 USD | 0.00 USD | 21,030.00 USD | 0.00 USD | 0.00 USD | 10,100.00 USD |
| `7D` | `156.46` | 10,940.00 USD | 0.00 USD | 10,940.00 USD | 0.00 USD | 0.00 USD | 10,940.00 USD |
| `1D` | `157.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `157.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `158.33` | 2,190.00 USD | 2,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,190.00 USD |
| `7D` | `158.50` | 2,670.00 USD | 2,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 482.11 USD |
| `7D` | `158.67` | 2,720.00 USD | 2,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 53.53 USD |
| `1D` | `158.72` | 62.55 USD | 62.55 USD | 0.00 USD | 0.00 USD | 0.00 USD | 62.55 USD |
| `7D` | `158.84` | 2,940.00 USD | 2,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 220.39 USD |
| `1D` | `158.88` | 1,290.00 USD | 1,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,220.00 USD |
| `7D` | `159.01` | 4,940.00 USD | 4,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,000.00 USD |
| `1D` | `159.04` | 1,550.00 USD | 1,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 262.70 USD |
| `7D` | `159.18` | 19,080.00 USD | 19,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,150.00 USD |
| `1D` | `159.20` | 3,450.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,900.00 USD |
| `7D` | `159.35` | 38,230.00 USD | 38,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,140.00 USD |
| `1D` | `159.36` | 3,530.00 USD | 3,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 79.79 USD |
| `7D` | `159.52` | 49,160.00 USD | 49,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,940.00 USD |
| `7D` | `159.86` | 50,250.00 USD | 50,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,090.00 USD |
| `7D` | `160.03` | 50,500.00 USD | 50,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 245.76 USD |
| `7D` | `160.20` | 50,520.00 USD | 50,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `1D` | `160.32` | 3,560.00 USD | 3,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 35.94 USD |
| `1D` | `160.48` | 4,210.00 USD | 4,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 646.62 USD |
| `7D` | `160.54` | 51,330.00 USD | 51,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 805.82 USD |
| `1D` | `160.64` | 4,400.00 USD | 4,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 192.64 USD |
| `7D` | `160.71` | 56,790.00 USD | 56,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,460.00 USD |
| `1D` | `160.80` | 5,260.00 USD | 5,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 855.74 USD |
| `7D` | `160.88` | 66,170.00 USD | 66,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,390.00 USD |
| `1D` | `160.96` | 5,290.00 USD | 5,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 32.03 USD |
| `7D` | `161.05` | 69,330.00 USD | 69,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,160.00 USD |
| `7D` | `161.22` | 73,740.00 USD | 73,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,410.00 USD |
| `7D` | `162.92` | 73,840.00 USD | 73,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 99.58 USD |
| `7D` | `163.09` | 74,290.00 USD | 74,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 448.04 USD |
| `7D` | `163.26` | 74,410.00 USD | 74,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 119.34 USD |
| `7D` | `163.43` | 74,420.00 USD | 74,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `1D` | `163.52` | 5,320.00 USD | 5,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 34.37 USD |
| `7D` | `163.60` | 74,480.00 USD | 74,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 55.10 USD |
| `1D` | `163.68` | 5,630.00 USD | 5,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 306.91 USD |
| `7D` | `163.77` | 75,020.00 USD | 75,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 535.86 USD |
| `1D` | `163.84` | 5,990.00 USD | 5,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 364.55 USD |
| `7D` | `163.94` | 79,250.00 USD | 79,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,230.00 USD |
| `1D` | `164.00` | 6,160.00 USD | 6,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 167.17 USD |
| `7D` | `164.11` | 83,300.00 USD | 83,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,050.00 USD |
| `1D` | `164.16` | 6,170.00 USD | 6,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8.48 USD |
| `7D` | `164.28` | 86,040.00 USD | 86,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD |
| `7D` | `172.27` | 86,050.00 USD | 86,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.36 USD |
| `7D` | `172.44` | 86,250.00 USD | 86,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 203.76 USD |
| `7D` | `172.61` | 86,300.00 USD | 86,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 47.74 USD |
| `7D` | `172.78` | 86,310.00 USD | 86,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.35 USD |
| `1D` | `172.96` | 6,300.00 USD | 6,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 126.03 USD |
| `1D` | `173.12` | 6,300.00 USD | 6,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7.90 USD |
| `7D` | `173.12` | 86,470.00 USD | 86,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 161.17 USD |
| `1D` | `173.16` | 6,320.00 USD | 6,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16.63 USD |
| `7D` | `173.29` | 87,280.00 USD | 87,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 809.57 USD |
| `7D` | `173.46` | 88,700.00 USD | 88,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,420.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-31.54` | Last 24h: `-624.43` | Last 3d: `-912.05` | Last 7d: `-912.05`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-0.0117%` | **USDT BingX** | `-` |
| **USDT Gate** | `-` | **USDT Bitget** | `-` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Multi-TF | Interbank Desk | 50.0% | 50.0% | 1.00 | Normal Balanced Liquidity |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `05:15:00` | `157.49` | `157.49` | `157.49` | `157.49` | `157.45` | 98,272.51 USD | 81,022.55 USD | 17,249.96 USD | 63,772.59 USD | `+64.89%` | `1B / 0S` |
| `05:20:00` | `157.50` | `157.50` | `157.50` | `157.53` | `157.46` | 83,002.50 USD | 47,207.67 USD | 35,794.83 USD | 11,412.84 USD | `+13.75%` | `1B / 0S` |
| `05:25:00` | `157.48` | `157.48` | `157.48` | `157.50` | `157.47` | 81,576.19 USD | 22,579.13 USD | 58,997.07 USD | -36,417.94 USD | `-44.64%` | `0B / 1S` |
| `05:30:00` | `157.48` | `157.48` | `157.48` | `157.53` | `157.46` | 76,849.26 USD | 28,269.55 USD | 48,579.71 USD | -20,310.16 USD | `-26.43%` | `0B / 1S` |
| `05:30:00` | `157.46` | `157.46` | `157.46` | `157.53` | `157.43` | 173,988.88 USD | 54,371.52 USD | 119,617.36 USD | -65,245.83 USD | `-37.50%` | `0B / 1S` |
| `05:35:00` | `157.49` | `157.49` | `157.49` | `157.53` | `157.47` | 52,758.14 USD | 21,751.17 USD | 31,006.98 USD | -9,255.81 USD | `-17.54%` | `0B / 1S` |
| `05:40:00` | `157.46` | `157.46` | `157.46` | `157.51` | `157.43` | 44,402.59 USD | 13,909.25 USD | 30,493.35 USD | -16,584.10 USD | `-37.35%` | `0B / 1S` |
| `05:45:00` | `157.58` | `157.58` | `157.58` | `157.59` | `157.43` | 143,712.05 USD | 127,598.88 USD | 16,113.17 USD | 111,485.71 USD | `+77.58%` | `1B / 0S` |
| `05:45:00` | `157.45` | `157.45` | `157.45` | `157.48` | `157.43` | 28,184.09 USD | 13,358.08 USD | 14,826.00 USD | -1,467.92 USD | `-5.21%` | `0B / 1S` |
| `05:50:00` | `157.47` | `157.47` | `157.47` | `157.47` | `157.44` | 30,548.40 USD | 26,142.38 USD | 4,406.02 USD | 21,736.36 USD | `+71.15%` | `1B / 0S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `2026-10-28 17:30:00 IST` | `4h` | `AGGRESSIVE BUYING` | **`BULLISH`** | USDJPY Macro Delta Flow: AGGRESSIVE BUYI | `157.95` | 2,346,385.47 USD | 2,346,385.47 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `15m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `2h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `4h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `6h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `8h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `12h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `24h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1w` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30d` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
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
  * Execution Entry: `157.24` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `157.07` (Risk Distance: `0.1708` pts)
  * +2.5R Take Profit: `157.66`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.17 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `157.61` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `157.78` (Risk Distance: `0.1708` pts)
  * +2.5R Take Profit: `157.19`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.17 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`158.86`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
