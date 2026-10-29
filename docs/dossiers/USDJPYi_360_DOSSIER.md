# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USDJPY
**Canonical Key**: `USDJPY` | **Broker Instrument**: `USDJPY.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 02:45:50 IST` (`2026-10-29 21:15:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `157.65` | **Live Ask Quote**: `157.71` | **Mid Price**: `157.68`
- **Spread Points**: `62.00` | **Spread BPS**: `3.93 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `157.87` | VWAP Z-Score: `-2.31` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0838` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `34.87` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `158.16` | Lower -3.00σ Band: `157.58`
  * Upper +2.51σ Band: `158.12` | Lower -2.51σ Band: `157.63`
  * Upper +2.01σ Band: `158.07` | Lower -2.01σ Band: `157.68`
  * Upper +2.00σ Band: `158.07` | Lower -2.00σ Band: `157.68`
  * Upper +1.28σ Band: `158.00` | Lower -1.28σ Band: `157.75`
  * Upper +1.00σ Band: `157.97` | Lower -1.00σ Band: `157.78`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`157.75` | EMA-20=`157.82` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`157.86` (Slope: `+0.0000`) | EMA-100=`157.88`
  * Institutional Anchors: EMA-144=`157.87` | EMA-200=`157.85` (Slope: `-0.0023`) | EMA-233=`157.85`
- **Range Boundaries**: 24H High=`158.13` | 24H Low=`157.60` | Weekly High=`158.35` | Weekly Low=`157.37`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `157.68` (Distance: `-0.00%`)
  * Point of Control (POC) = `157.65` (Distance: `+0.02%`)
  * Value Area Low (VAL) = `157.65` (Distance: `+0.02%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`157.99` | POC=`157.87` | VAL=`157.76`
  * Prior Day Extremes: PDH=`158.13` | PDL=`157.60` | PDC=`157.69`
  * Monday Range Blueprint: High=`157.64` | Mid=`157.15` | Low=`156.65`
  * Developing Weekly Value Area: Weekly VAH=`158.08` | Weekly POC=`157.87` | Weekly VAL=`157.48`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`157.68` | Low=`157.64`
  * London Session (08:00-16:00 UTC): High=`158.31` | Low=`157.05`
  * New York Session (13:00-21:00 UTC): High=`158.63` | Low=`156.73`
  * Initial Balance (First Hour): IB High=`158.15` | IB Low=`157.21`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `157.05` - `158.31`
  * Optimal Trade Entry (OTE 0.705): `158.00`
  * Structural Invalidation Anchor (0.786): `158.94`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `157.89` | `157.89` | `157.87` | `157.87` | `381` | 60,149.23 USD | -49,688.50 USD | `-82.61%` | -610,496.54 USD | `-1.29` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `157.87` | `157.87` | `157.84` | `157.85` | `319` | 50,353.19 USD | -33,831.05 USD | `-67.19%` | -644,327.59 USD | `-0.81` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `157.85` | `157.88` | `157.84` | `157.85` | `356` | 56,194.24 USD | -10,351.57 USD | `-18.42%` | -654,679.17 USD | `-0.23` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `157.88` | `157.92` | `157.85` | `157.90` | `946` | 149,377.18 USD | 59,341.62 USD | `+39.73%` | -1,157,195.50 USD | `+0.48` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `157.90` | `157.91` | `157.84` | `157.85` | `1,024` | 161,635.33 USD | -133,038.31 USD | `-82.31%` | -1,290,233.81 USD | `-0.67` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `157.85` | `157.91` | `157.84` | `157.90` | `1,039` | 164,057.06 USD | 131,000.79 USD | `+79.85%` | -1,159,233.02 USD | `+0.90` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `157.82` | `157.93` | `157.76` | `157.88` | `4,599` | 726,108.52 USD | 298,606.76 USD | `+41.12%` | -1,224,569.65 USD | `+0.57` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `157.88` | `157.94` | `157.85` | `157.90` | `4,730` | 746,885.92 USD | 143,020.71 USD | `+19.15%` | -1,081,548.94 USD | `+0.23` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `157.90` | `157.97` | `157.84` | `157.96` | `3,894` | 615,100.13 USD | 406,153.91 USD | `+66.03%` | -675,395.03 USD | `+0.71` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `157.87` | `158.08` | `157.81` | `158.06` | `23,822` | 3,765,376.79 USD | 3,094,533.80 USD | `+82.18%` | 4,207,442.50 USD | `+1.47` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `158.06` | `158.13` | `157.71` | `157.88` | `37,561` | 5,930,280.92 USD | -1,786,229.19 USD | `-30.12%` | 2,421,213.31 USD | `-1.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.88` | `157.98` | `157.63` | `157.69` | `20,300` | 3,201,147.60 USD | -1,948,126.97 USD | `-60.86%` | 473,086.34 USD | `-1.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.97` | `158.00` | `157.60` | `157.82` | `28,963` | 4,570,824.81 USD | -704,091.70 USD | `-15.40%` | 685,937.57 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.82` | `157.97` | `157.77` | `157.87` | `20,616` | 3,254,647.92 USD | 426,971.14 USD | `+13.12%` | 1,112,908.71 USD | `+0.07` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `157.87` | `158.08` | `157.81` | `158.06` | `23,822` | 3,765,376.79 USD | 3,094,533.80 USD | `+82.18%` | 4,207,442.50 USD | `+1.47` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `158.06` | `158.13` | `157.71` | `157.88` | `37,561` | 5,930,280.92 USD | -1,786,229.19 USD | `-30.12%` | 2,421,213.31 USD | `-1.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.88` | `157.98` | `157.63` | `157.69` | `20,300` | 3,201,147.60 USD | -1,948,126.97 USD | `-60.86%` | 473,086.34 USD | `-1.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `204` | `0x0911...129a` | `SHORT` | 10,441,411.94 USD | `66,223.20` | `156.58` | `157.66` | `167.72` | -72,391.71 USD | `-0.69%` | `20X Isolated` |
| `1105` | `0xec0b...b078` | `SHORT` | 1,989,399.65 USD | `12,617.49` | `158.22` | `157.66` | `162.95` | 6,966.02 USD | `+0.35%` | `20X Isolated` |
| `1130` | `0xc966...f6b6` | `SHORT` | 1,964,205.53 USD | `12,458.49` | `157.61` | `157.66` | `215.28` | -679.46 USD | `-0.03%` | `5X Isolated` |
| `1166` | `0x9dea...d617` | `LONG` | 1,909,257.56 USD | `12,109.20` | `157.68` | `157.66` | `148.42` | -124.67 USD | `-0.01%` | `50X Isolated` |
| `1189` | `0xbef1...d2e5` | `LONG` | 1,863,744.58 USD | `11,821.29` | `157.63` | `157.66` | `155.51` | 383.97 USD | `+0.02%` | `50X Isolated` |
| `1846` | `0x3d89...eb14` | `LONG` | 1,087,854.00 USD | `6,900.00` | `158.17` | `157.66` | `127.36` | -3,535.60 USD | `-0.33%` | `5X Isolated` |

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
| `7D` | `141.79` | 89,630.00 USD | 0.00 USD | 89,630.00 USD | 0.00 USD | 0.00 USD | 872.97 USD |
| `1D` | `141.80` | 3,550.00 USD | 0.00 USD | 3,550.00 USD | 0.00 USD | 0.00 USD | 129.32 USD |
| `7D` | `141.95` | 88,760.00 USD | 0.00 USD | 88,760.00 USD | 0.00 USD | 0.00 USD | 2,030.00 USD |
| `1D` | `141.96` | 3,420.00 USD | 0.00 USD | 3,420.00 USD | 0.00 USD | 0.00 USD | 47.85 USD |
| `7D` | `142.11` | 86,740.00 USD | 0.00 USD | 86,740.00 USD | 0.00 USD | 0.00 USD | 1,300.00 USD |
| `7D` | `150.43` | 85,430.00 USD | 0.00 USD | 85,430.00 USD | 0.00 USD | 0.00 USD | 420.80 USD |
| `7D` | `150.59` | 85,010.00 USD | 0.00 USD | 85,010.00 USD | 0.00 USD | 0.00 USD | 141.18 USD |
| `7D` | `150.75` | 84,870.00 USD | 0.00 USD | 84,870.00 USD | 0.00 USD | 0.00 USD | 137.75 USD |
| `7D` | `150.91` | 84,730.00 USD | 0.00 USD | 84,730.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `7D` | `151.07` | 84,720.00 USD | 0.00 USD | 84,720.00 USD | 0.00 USD | 0.00 USD | 167.19 USD |
| `7D` | `151.23` | 84,550.00 USD | 0.00 USD | 84,550.00 USD | 0.00 USD | 0.00 USD | 1,020.00 USD |
| `1D` | `151.24` | 3,370.00 USD | 0.00 USD | 3,370.00 USD | 0.00 USD | 0.00 USD | 350.31 USD |
| `7D` | `151.39` | 83,530.00 USD | 0.00 USD | 83,530.00 USD | 0.00 USD | 0.00 USD | 5,040.00 USD |
| `1D` | `151.40` | 3,020.00 USD | 0.00 USD | 3,020.00 USD | 0.00 USD | 0.00 USD | 131.80 USD |
| `7D` | `151.55` | 78,490.00 USD | 0.00 USD | 78,490.00 USD | 0.00 USD | 0.00 USD | 2,520.00 USD |
| `7D` | `151.71` | 75,960.00 USD | 0.00 USD | 75,960.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD |
| `7D` | `153.47` | 73,230.00 USD | 0.00 USD | 73,230.00 USD | 0.00 USD | 0.00 USD | 19.92 USD |
| `7D` | `153.63` | 73,210.00 USD | 0.00 USD | 73,210.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD |
| `7D` | `153.79` | 72,130.00 USD | 0.00 USD | 72,130.00 USD | 0.00 USD | 0.00 USD | 267.41 USD |
| `7D` | `153.95` | 71,860.00 USD | 0.00 USD | 71,860.00 USD | 0.00 USD | 0.00 USD | 63.58 USD |
| `7D` | `154.11` | 71,800.00 USD | 0.00 USD | 71,800.00 USD | 0.00 USD | 0.00 USD | 110.19 USD |
| `7D` | `154.27` | 71,690.00 USD | 0.00 USD | 71,690.00 USD | 0.00 USD | 0.00 USD | 668.20 USD |
| `1D` | `154.28` | 2,890.00 USD | 0.00 USD | 2,890.00 USD | 0.00 USD | 0.00 USD | 89.05 USD |
| `7D` | `154.43` | 71,020.00 USD | 0.00 USD | 71,020.00 USD | 0.00 USD | 0.00 USD | 6,930.00 USD |
| `1D` | `154.44` | 2,800.00 USD | 0.00 USD | 2,800.00 USD | 0.00 USD | 0.00 USD | 724.11 USD |
| `7D` | `154.59` | 64,090.00 USD | 0.00 USD | 64,090.00 USD | 0.00 USD | 0.00 USD | 7,700.00 USD |
| `1D` | `154.60` | 2,080.00 USD | 0.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD | 151.15 USD |
| `7D` | `154.75` | 56,390.00 USD | 0.00 USD | 56,390.00 USD | 0.00 USD | 0.00 USD | 7,570.00 USD |
| `7D` | `155.07` | 48,820.00 USD | 0.00 USD | 48,820.00 USD | 0.00 USD | 0.00 USD | 398.36 USD |
| `7D` | `155.23` | 48,420.00 USD | 0.00 USD | 48,420.00 USD | 0.00 USD | 0.00 USD | 1,790.00 USD |
| `7D` | `155.39` | 46,630.00 USD | 0.00 USD | 46,630.00 USD | 0.00 USD | 0.00 USD | 608.44 USD |
| `7D` | `155.55` | 46,020.00 USD | 0.00 USD | 46,020.00 USD | 0.00 USD | 0.00 USD | 53.53 USD |
| `7D` | `155.71` | 45,970.00 USD | 0.00 USD | 45,970.00 USD | 0.00 USD | 0.00 USD | 220.39 USD |
| `7D` | `155.87` | 45,750.00 USD | 0.00 USD | 45,750.00 USD | 0.00 USD | 0.00 USD | 1,690.00 USD |
| `1D` | `155.88` | 1,930.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD | 0.00 USD | 296.26 USD |
| `7D` | `156.03` | 44,060.00 USD | 0.00 USD | 44,060.00 USD | 0.00 USD | 0.00 USD | 14,890.00 USD |
| `1D` | `156.04` | 1,630.00 USD | 0.00 USD | 1,630.00 USD | 0.00 USD | 0.00 USD | 1,410.00 USD |
| `7D` | `156.19` | 29,170.00 USD | 0.00 USD | 29,170.00 USD | 0.00 USD | 0.00 USD | 18,240.00 USD |
| `1D` | `156.20` | 218.91 USD | 0.00 USD | 218.91 USD | 0.00 USD | 0.00 USD | 218.91 USD |
| `7D` | `156.35` | 10,940.00 USD | 0.00 USD | 10,940.00 USD | 0.00 USD | 0.00 USD | 10,940.00 USD |
| `1D` | `157.45` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `157.45` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `158.27` | 1,680.00 USD | 1,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,680.00 USD |
| `7D` | `158.43` | 2,250.00 USD | 2,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 564.68 USD |
| `7D` | `158.59` | 2,800.00 USD | 2,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 551.01 USD |
| `7D` | `158.75` | 2,850.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 53.53 USD |
| `7D` | `158.91` | 3,520.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 668.76 USD |
| `7D` | `159.07` | 5,030.00 USD | 5,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `159.08` | 554.11 USD | 554.11 USD | 0.00 USD | 0.00 USD | 0.00 USD | 554.11 USD |
| `7D` | `159.23` | 26,530.00 USD | 26,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21,500.00 USD |
| `1D` | `159.24` | 1,920.00 USD | 1,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,370.00 USD |
| `7D` | `159.39` | 37,880.00 USD | 37,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,350.00 USD |
| `1D` | `159.40` | 1,930.00 USD | 1,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6.05 USD |
| `7D` | `159.55` | 48,820.00 USD | 48,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,940.00 USD |
| `7D` | `159.87` | 49,910.00 USD | 49,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,090.00 USD |
| `7D` | `160.03` | 50,180.00 USD | 50,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 274.48 USD |
| `7D` | `160.19` | 50,220.00 USD | 50,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 36.82 USD |
| `7D` | `160.35` | 50,240.00 USD | 50,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `7D` | `160.51` | 50,580.00 USD | 50,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 334.38 USD |
| `7D` | `160.67` | 51,540.00 USD | 51,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 960.93 USD |
| `1D` | `160.68` | 2,600.00 USD | 2,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 669.09 USD |
| `7D` | `160.83` | 62,590.00 USD | 62,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,050.00 USD |
| `1D` | `160.84` | 2,890.00 USD | 2,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 295.22 USD |
| `7D` | `160.99` | 67,760.00 USD | 67,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `161.15` | 73,230.00 USD | 73,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD |
| `7D` | `162.91` | 73,330.00 USD | 73,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 99.58 USD |
| `7D` | `163.07` | 73,780.00 USD | 73,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 448.04 USD |
| `7D` | `163.23` | 73,930.00 USD | 73,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 152.11 USD |
| `7D` | `163.39` | 73,940.00 USD | 73,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `7D` | `163.55` | 74,000.00 USD | 74,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 55.10 USD |
| `7D` | `163.71` | 74,270.00 USD | 74,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 270.59 USD |
| `1D` | `163.72` | 2,900.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11.18 USD |
| `7D` | `163.87` | 77,060.00 USD | 77,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,790.00 USD |
| `1D` | `163.88` | 3,300.00 USD | 3,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 392.82 USD |
| `7D` | `164.03` | 81,650.00 USD | 81,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,580.00 USD |
| `1D` | `164.04` | 3,370.00 USD | 3,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 78.11 USD |
| `7D` | `164.19` | 82,700.00 USD | 82,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,050.00 USD |
| `7D` | `164.35` | 85,430.00 USD | 85,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD |
| `7D` | `172.35` | 85,530.00 USD | 85,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 94.01 USD |
| `7D` | `172.51` | 85,650.00 USD | 85,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 123.11 USD |
| `7D` | `172.67` | 85,710.00 USD | 85,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 60.84 USD |
| `7D` | `172.83` | 85,720.00 USD | 85,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.35 USD |
| `7D` | `172.99` | 85,740.00 USD | 85,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22.04 USD |
| `7D` | `173.15` | 85,850.00 USD | 85,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 108.24 USD |
| `1D` | `173.16` | 3,380.00 USD | 3,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2.43 USD |
| `7D` | `173.31` | 86,660.00 USD | 86,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 809.57 USD |
| `1D` | `173.32` | 3,500.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 126.89 USD |
| `1D` | `173.43` | 3,550.00 USD | 3,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 47.24 USD |
| `7D` | `173.47` | 88,090.00 USD | 88,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,440.00 USD |
| `7D` | `173.54` | 89,100.00 USD | 89,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,010.00 USD |

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
  * Current Rate: `-52.11` | Last 24h: `-640.25` | Last 3d: `-882.53` | Last 7d: `-882.53`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-0.0145%` | **USDT BingX** | `-` |
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
| `20:35:00` | `157.93` | `157.93` | `157.93` | `157.93` | `157.91` | 70,434.55 USD | 44,373.77 USD | 26,060.78 USD | 18,312.98 USD | `+26.00%` | `1B / 0S` |
| `20:40:00` | `157.88` | `157.88` | `157.88` | `157.93` | `157.87` | 67,258.16 USD | 10,088.72 USD | 57,169.43 USD | -47,080.71 USD | `-70.00%` | `0B / 1S` |
| `20:45:00` | `157.90` | `157.90` | `157.90` | `157.92` | `157.85` | 149,377.18 USD | 104,359.40 USD | 45,017.78 USD | 59,341.62 USD | `+39.73%` | `1B / 0S` |
| `20:45:00` | `157.88` | `157.88` | `157.88` | `157.89` | `157.85` | 42,152.89 USD | 22,618.62 USD | 19,534.27 USD | 3,084.36 USD | `+7.32%` | `1B / 0S` |
| `20:50:00` | `157.88` | `157.88` | `157.88` | `157.89` | `157.87` | 59,046.00 USD | 26,313.98 USD | 32,732.02 USD | -6,418.04 USD | `-10.87%` | `0B / 1S` |
| `20:55:00` | `157.90` | `157.90` | `157.90` | `157.92` | `157.88` | 48,160.72 USD | 33,558.80 USD | 14,601.92 USD | 18,956.88 USD | `+39.36%` | `1B / 0S` |
| `21:00:00` | `157.96` | `157.96` | `157.96` | `157.97` | `157.84` | 615,100.13 USD | 510,627.02 USD | 104,473.11 USD | 406,153.91 USD | `+66.03%` | `1B / 0S` |
| `21:00:00` | `157.89` | `157.89` | `157.89` | `157.91` | `157.89` | 51,156.04 USD | 7,404.16 USD | 43,751.87 USD | -36,347.71 USD | `-71.05%` | `0B / 1S` |
| `21:00:00` | `157.85` | `157.85` | `157.85` | `157.91` | `157.84` | 161,635.33 USD | 14,298.51 USD | 147,336.82 USD | -133,038.31 USD | `-82.31%` | `0B / 1S` |
| `21:05:00` | `157.87` | `157.87` | `157.87` | `157.89` | `157.87` | 60,149.23 USD | 5,230.37 USD | 54,918.86 USD | -49,688.50 USD | `-82.61%` | `0B / 1S` |

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
  * `2026-10-30 02:15:06 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:40:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `157.65` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `157.46` (Risk Distance: `0.1936` pts)
  * +2.5R Take Profit: `158.13`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.19 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `157.68` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `157.87` (Risk Distance: `0.1936` pts)
  * +2.5R Take Profit: `157.20`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.19 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`158.94`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
