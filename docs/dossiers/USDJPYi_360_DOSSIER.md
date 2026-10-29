# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USDJPY
**Canonical Key**: `USDJPY` | **Broker Instrument**: `USDJPY.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 03:19:13 IST` (`2026-10-29 21:49:13 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `157.67` | **Live Ask Quote**: `157.74` | **Mid Price**: `157.71`
- **Spread Points**: `75.00` | **Spread BPS**: `4.76 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `157.87` | VWAP Z-Score: `-2.12` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0822` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `36.73` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `158.16` | Lower -3.00σ Band: `157.58`
  * Upper +2.51σ Band: `158.12` | Lower -2.51σ Band: `157.63`
  * Upper +2.01σ Band: `158.07` | Lower -2.01σ Band: `157.68`
  * Upper +2.00σ Band: `158.07` | Lower -2.00σ Band: `157.68`
  * Upper +1.28σ Band: `158.00` | Lower -1.28σ Band: `157.75`
  * Upper +1.00σ Band: `157.97` | Lower -1.00σ Band: `157.78`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`157.74` | EMA-20=`157.80` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`157.85` (Slope: `+0.0000`) | EMA-100=`157.87`
  * Institutional Anchors: EMA-144=`157.87` | EMA-200=`157.85` (Slope: `-0.0038`) | EMA-233=`157.85`
- **Range Boundaries**: 24H High=`158.13` | 24H Low=`157.60` | Weekly High=`158.35` | Weekly Low=`157.37`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `157.68` (Distance: `+0.01%`)
  * Point of Control (POC) = `157.66` (Distance: `+0.02%`)
  * Value Area Low (VAL) = `157.66` (Distance: `+0.02%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`157.99` | POC=`157.87` | VAL=`157.76`
  * Prior Day Extremes: PDH=`158.13` | PDL=`157.60` | PDC=`157.69`
  * Monday Range Blueprint: High=`157.64` | Mid=`157.15` | Low=`156.65`
  * Developing Weekly Value Area: Weekly VAH=`158.08` | Weekly POC=`157.87` | Weekly VAL=`157.48`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`157.70` | Low=`157.64`
  * London Session (08:00-16:00 UTC): High=`158.34` | Low=`157.08`
  * New York Session (13:00-21:00 UTC): High=`158.65` | Low=`156.76`
  * Initial Balance (First Hour): IB High=`158.18` | IB Low=`157.23`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `157.08` - `158.34`
  * Optimal Trade Entry (OTE 0.705): `158.02`
  * Structural Invalidation Anchor (0.786): `158.97`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `157.90` | `157.93` | `157.90` | `157.93` | `232` | 36,639.99 USD | 32,975.99 USD | `+90.00%` | -27,623.35 USD | `+0.99` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `157.93` | `157.95` | `157.93` | `157.95` | `309` | 48,807.48 USD | 43,926.73 USD | `+90.00%` | 16,303.38 USD | `+1.17` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `157.95` | `157.95` | `157.91` | `157.93` | `281` | 44,378.05 USD | -15,849.30 USD | `-35.71%` | 454.08 USD | `-0.40` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `157.90` | `157.91` | `157.84` | `157.85` | `1,024` | 161,635.33 USD | -133,038.31 USD | `-82.31%` | -231,494.16 USD | `-0.67` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `157.85` | `157.91` | `157.84` | `157.90` | `1,039` | 164,057.06 USD | 131,000.79 USD | `+79.85%` | -100,493.37 USD | `+0.90` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `157.90` | `157.95` | `157.90` | `157.93` | `822` | 129,817.64 USD | 45,204.36 USD | `+34.82%` | -55,289.01 USD | `+0.28` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `211` | `0x0911...129a` | `SHORT` | 10,440,087.48 USD | `66,223.20` | `156.58` | `157.65` | `167.72` | -71,067.25 USD | `-0.68%` | `20X Isolated` |
| `1129` | `0xec0b...b078` | `SHORT` | 1,989,021.12 USD | `12,617.49` | `158.22` | `157.65` | `162.95` | 7,344.55 USD | `+0.37%` | `20X Isolated` |
| `1165` | `0xc966...f6b6` | `SHORT` | 1,950,350.46 USD | `12,372.18` | `157.61` | `157.65` | `215.28` | -427.31 USD | `-0.02%` | `5X Isolated` |
| `1176` | `0x9dea...d617` | `LONG` | 1,935,846.00 USD | `12,280.17` | `157.68` | `157.65` | `148.52` | -482.82 USD | `-0.02%` | `50X Isolated` |
| `1214` | `0xbef1...d2e5` | `LONG` | 1,863,744.58 USD | `11,821.29` | `157.63` | `157.65` | `155.51` | 383.97 USD | `+0.02%` | `50X Isolated` |
| `1885` | `0x3d89...eb14` | `LONG` | 1,087,785.00 USD | `6,900.00` | `158.17` | `157.65` | `127.36` | -3,604.60 USD | `-0.33%` | `5X Isolated` |

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
| `7D` | `141.79` | 89,570.00 USD | 0.00 USD | 89,570.00 USD | 0.00 USD | 0.00 USD | 1,060.00 USD |
| `1D` | `141.80` | 3,510.00 USD | 0.00 USD | 3,510.00 USD | 0.00 USD | 0.00 USD | 137.28 USD |
| `7D` | `141.95` | 88,510.00 USD | 0.00 USD | 88,510.00 USD | 0.00 USD | 0.00 USD | 1,650.00 USD |
| `1D` | `141.96` | 3,370.00 USD | 0.00 USD | 3,370.00 USD | 0.00 USD | 0.00 USD | 37.41 USD |
| `7D` | `142.11` | 86,870.00 USD | 0.00 USD | 86,870.00 USD | 0.00 USD | 0.00 USD | 551.13 USD |
| `7D` | `142.27` | 86,310.00 USD | 0.00 USD | 86,310.00 USD | 0.00 USD | 0.00 USD | 882.43 USD |
| `7D` | `150.43` | 85,430.00 USD | 0.00 USD | 85,430.00 USD | 0.00 USD | 0.00 USD | 451.40 USD |
| `7D` | `150.59` | 84,980.00 USD | 0.00 USD | 84,980.00 USD | 0.00 USD | 0.00 USD | 229.86 USD |
| `7D` | `150.75` | 84,750.00 USD | 0.00 USD | 84,750.00 USD | 0.00 USD | 0.00 USD | 18.41 USD |
| `7D` | `150.91` | 84,730.00 USD | 0.00 USD | 84,730.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `7D` | `151.07` | 84,720.00 USD | 0.00 USD | 84,720.00 USD | 0.00 USD | 0.00 USD | 325.66 USD |
| `7D` | `151.23` | 84,390.00 USD | 0.00 USD | 84,390.00 USD | 0.00 USD | 0.00 USD | 859.42 USD |
| `1D` | `151.24` | 3,330.00 USD | 0.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD | 377.85 USD |
| `7D` | `151.39` | 83,530.00 USD | 0.00 USD | 83,530.00 USD | 0.00 USD | 0.00 USD | 5,010.00 USD |
| `1D` | `151.40` | 2,950.00 USD | 0.00 USD | 2,950.00 USD | 0.00 USD | 0.00 USD | 98.11 USD |
| `7D` | `151.55` | 78,520.00 USD | 0.00 USD | 78,520.00 USD | 0.00 USD | 0.00 USD | 2,560.00 USD |
| `7D` | `151.71` | 75,960.00 USD | 0.00 USD | 75,960.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD |
| `7D` | `153.47` | 73,230.00 USD | 0.00 USD | 73,230.00 USD | 0.00 USD | 0.00 USD | 27.14 USD |
| `7D` | `153.63` | 73,200.00 USD | 0.00 USD | 73,200.00 USD | 0.00 USD | 0.00 USD | 1,070.00 USD |
| `7D` | `153.79` | 72,130.00 USD | 0.00 USD | 72,130.00 USD | 0.00 USD | 0.00 USD | 267.33 USD |
| `7D` | `153.95` | 71,870.00 USD | 0.00 USD | 71,870.00 USD | 0.00 USD | 0.00 USD | 63.58 USD |
| `7D` | `154.11` | 71,800.00 USD | 0.00 USD | 71,800.00 USD | 0.00 USD | 0.00 USD | 110.19 USD |
| `7D` | `154.27` | 71,690.00 USD | 0.00 USD | 71,690.00 USD | 0.00 USD | 0.00 USD | 724.63 USD |
| `1D` | `154.28` | 2,860.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD | 0.00 USD | 19.48 USD |
| `7D` | `154.43` | 70,970.00 USD | 0.00 USD | 70,970.00 USD | 0.00 USD | 0.00 USD | 6,960.00 USD |
| `1D` | `154.44` | 2,840.00 USD | 0.00 USD | 2,840.00 USD | 0.00 USD | 0.00 USD | 752.74 USD |
| `7D` | `154.59` | 64,000.00 USD | 0.00 USD | 64,000.00 USD | 0.00 USD | 0.00 USD | 6,960.00 USD |
| `1D` | `154.60` | 2,080.00 USD | 0.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD | 179.78 USD |
| `7D` | `154.75` | 57,040.00 USD | 0.00 USD | 57,040.00 USD | 0.00 USD | 0.00 USD | 3,810.00 USD |
| `7D` | `154.91` | 53,230.00 USD | 0.00 USD | 53,230.00 USD | 0.00 USD | 0.00 USD | 4,410.00 USD |
| `7D` | `155.07` | 48,820.00 USD | 0.00 USD | 48,820.00 USD | 0.00 USD | 0.00 USD | 698.23 USD |
| `7D` | `155.23` | 48,120.00 USD | 0.00 USD | 48,120.00 USD | 0.00 USD | 0.00 USD | 1,490.00 USD |
| `7D` | `155.39` | 46,630.00 USD | 0.00 USD | 46,630.00 USD | 0.00 USD | 0.00 USD | 608.29 USD |
| `7D` | `155.55` | 46,020.00 USD | 0.00 USD | 46,020.00 USD | 0.00 USD | 0.00 USD | 53.52 USD |
| `7D` | `155.71` | 45,970.00 USD | 0.00 USD | 45,970.00 USD | 0.00 USD | 0.00 USD | 220.37 USD |
| `7D` | `155.87` | 45,750.00 USD | 0.00 USD | 45,750.00 USD | 0.00 USD | 0.00 USD | 1,690.00 USD |
| `1D` | `155.88` | 1,900.00 USD | 0.00 USD | 1,900.00 USD | 0.00 USD | 0.00 USD | 165.30 USD |
| `7D` | `156.03` | 44,060.00 USD | 0.00 USD | 44,060.00 USD | 0.00 USD | 0.00 USD | 19,180.00 USD |
| `1D` | `156.04` | 1,740.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD | 0.00 USD | 1,480.00 USD |
| `7D` | `156.19` | 24,880.00 USD | 0.00 USD | 24,880.00 USD | 0.00 USD | 0.00 USD | 13,940.00 USD |
| `1D` | `156.20` | 258.26 USD | 0.00 USD | 258.26 USD | 0.00 USD | 0.00 USD | 258.26 USD |
| `7D` | `156.35` | 10,940.00 USD | 0.00 USD | 10,940.00 USD | 0.00 USD | 0.00 USD | 10,940.00 USD |
| `1D` | `157.45` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `157.45` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `158.27` | 1,810.00 USD | 1,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,810.00 USD |
| `7D` | `158.43` | 2,730.00 USD | 2,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 919.42 USD |
| `7D` | `158.59` | 2,800.00 USD | 2,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 73.64 USD |
| `7D` | `158.75` | 2,850.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 53.52 USD |
| `7D` | `158.91` | 3,520.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 668.68 USD |
| `7D` | `159.07` | 4,950.00 USD | 4,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,430.00 USD |
| `1D` | `159.08` | 486.61 USD | 486.61 USD | 0.00 USD | 0.00 USD | 0.00 USD | 486.61 USD |
| `7D` | `159.23` | 24,580.00 USD | 24,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,630.00 USD |
| `1D` | `159.24` | 1,840.00 USD | 1,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,350.00 USD |
| `7D` | `159.39` | 37,880.00 USD | 37,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,300.00 USD |
| `1D` | `159.40` | 1,900.00 USD | 1,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 64.05 USD |
| `7D` | `159.55` | 48,820.00 USD | 48,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,940.00 USD |
| `7D` | `159.87` | 49,910.00 USD | 49,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,090.00 USD |
| `7D` | `160.03` | 50,180.00 USD | 50,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 269.70 USD |
| `7D` | `160.19` | 50,240.00 USD | 50,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 63.58 USD |
| `7D` | `160.51` | 50,900.00 USD | 50,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 651.33 USD |
| `7D` | `160.67` | 52,030.00 USD | 52,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,140.00 USD |
| `1D` | `160.68` | 2,550.00 USD | 2,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 650.21 USD |
| `7D` | `160.83` | 62,360.00 USD | 62,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,320.00 USD |
| `1D` | `160.84` | 2,840.00 USD | 2,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 284.83 USD |
| `7D` | `160.99` | 67,760.00 USD | 67,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,400.00 USD |
| `1D` | `161.00` | 2,860.00 USD | 2,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16.96 USD |
| `7D` | `161.15` | 73,230.00 USD | 73,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD |
| `7D` | `162.91` | 73,400.00 USD | 73,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 174.55 USD |
| `7D` | `163.07` | 73,780.00 USD | 73,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 373.05 USD |
| `7D` | `163.23` | 73,930.00 USD | 73,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 152.07 USD |
| `7D` | `163.39` | 73,940.00 USD | 73,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `7D` | `163.55` | 74,000.00 USD | 74,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 55.09 USD |
| `7D` | `163.71` | 74,290.00 USD | 74,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 298.81 USD |
| `7D` | `163.87` | 77,840.00 USD | 77,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,540.00 USD |
| `1D` | `163.88` | 3,240.00 USD | 3,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 383.53 USD |
| `7D` | `164.03` | 81,320.00 USD | 81,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,480.00 USD |
| `1D` | `164.04` | 3,330.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 92.43 USD |
| `7D` | `164.19` | 82,700.00 USD | 82,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,380.00 USD |
| `7D` | `164.35` | 85,430.00 USD | 85,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD |
| `7D` | `172.35` | 85,540.00 USD | 85,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 104.18 USD |
| `7D` | `172.51` | 85,700.00 USD | 85,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 160.68 USD |
| `7D` | `172.67` | 85,710.00 USD | 85,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.10 USD |
| `7D` | `172.83` | 85,720.00 USD | 85,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.35 USD |
| `7D` | `172.99` | 85,740.00 USD | 85,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22.04 USD |
| `7D` | `173.15` | 85,850.00 USD | 85,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 108.23 USD |
| `7D` | `173.31` | 86,910.00 USD | 86,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,060.00 USD |
| `1D` | `173.32` | 3,470.00 USD | 3,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 137.28 USD |
| `1D` | `173.42` | 3,500.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31.01 USD |
| `7D` | `173.47` | 88,080.00 USD | 88,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,170.00 USD |
| `7D` | `173.54` | 88,680.00 USD | 88,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 603.79 USD |

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
  * Current Rate: `-16.08` | Last 24h: `-640.25` | Last 3d: `-882.53` | Last 7d: `-882.53`
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
| `21:00:00` | `157.96` | `157.96` | `157.96` | `157.97` | `157.84` | 615,100.13 USD | 510,627.02 USD | 104,473.11 USD | 406,153.91 USD | `+66.03%` | `1B / 0S` |
| `21:00:00` | `157.89` | `157.89` | `157.89` | `157.91` | `157.89` | 51,156.04 USD | 7,404.16 USD | 43,751.87 USD | -36,347.71 USD | `-71.05%` | `0B / 1S` |
| `21:05:00` | `157.87` | `157.87` | `157.87` | `157.89` | `157.87` | 60,149.23 USD | 5,230.37 USD | 54,918.86 USD | -49,688.50 USD | `-82.61%` | `0B / 1S` |
| `21:10:00` | `157.85` | `157.85` | `157.85` | `157.87` | `157.84` | 50,353.19 USD | 8,261.07 USD | 42,092.12 USD | -33,831.05 USD | `-67.19%` | `0B / 1S` |
| `21:15:00` | `157.90` | `157.90` | `157.90` | `157.91` | `157.84` | 164,057.06 USD | 147,528.92 USD | 16,528.14 USD | 131,000.79 USD | `+79.85%` | `1B / 0S` |
| `21:15:00` | `157.85` | `157.85` | `157.85` | `157.88` | `157.84` | 56,194.24 USD | 22,921.34 USD | 33,272.91 USD | -10,351.57 USD | `-18.42%` | `0B / 1S` |
| `21:20:00` | `157.87` | `157.87` | `157.87` | `157.90` | `157.84` | 51,466.92 USD | 33,802.43 USD | 17,664.50 USD | 16,137.93 USD | `+31.36%` | `1B / 0S` |
| `21:25:00` | `157.90` | `157.90` | `157.90` | `157.91` | `157.87` | 56,369.94 USD | 47,914.45 USD | 8,455.49 USD | 39,458.96 USD | `+70.00%` | `1B / 0S` |
| `21:30:00` | `157.93` | `157.93` | `157.93` | `157.93` | `157.90` | 36,639.99 USD | 34,807.99 USD | 1,832.00 USD | 32,975.99 USD | `+90.00%` | `1B / 0S` |
| `21:30:00` | `157.93` | `157.93` | `157.93` | `157.95` | `157.90` | 129,817.64 USD | 87,511.00 USD | 42,306.64 USD | 45,204.36 USD | `+34.82%` | `1B / 0S` |

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
  * `2026-10-30 02:54:26 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:10:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:11:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:11:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:11:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `157.66` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `157.45` (Risk Distance: `0.2111` pts)
  * +2.5R Take Profit: `158.19`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.21 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `157.68` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `157.89` (Risk Distance: `0.2111` pts)
  * +2.5R Take Profit: `157.15`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.21 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`158.97`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
