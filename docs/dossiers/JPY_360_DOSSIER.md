# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USDJPY
**Canonical Key**: `USDJPY` | **Broker Instrument**: `USDJPY.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 03:55:35 IST` (`2026-10-29 22:25:35 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `157.66` | **Live Ask Quote**: `157.66` | **Mid Price**: `157.66`
- **Spread Points**: `3.00` | **Spread BPS**: `0.19 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `157.87` | VWAP Z-Score: `-2.62` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0740` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `33.40` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `158.17` | Lower -3.00σ Band: `157.58`
  * Upper +2.51σ Band: `158.12` | Lower -2.51σ Band: `157.63`
  * Upper +2.01σ Band: `158.07` | Lower -2.01σ Band: `157.67`
  * Upper +2.00σ Band: `158.07` | Lower -2.00σ Band: `157.68`
  * Upper +1.28σ Band: `158.00` | Lower -1.28σ Band: `157.75`
  * Upper +1.00σ Band: `157.97` | Lower -1.00σ Band: `157.77`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`157.69` | EMA-20=`157.76` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`157.83` (Slope: `+0.0000`) | EMA-100=`157.86`
  * Institutional Anchors: EMA-144=`157.86` | EMA-200=`157.84` (Slope: `-0.0096`) | EMA-233=`157.85`
- **Range Boundaries**: 24H High=`158.13` | 24H Low=`157.60` | Weekly High=`158.35` | Weekly Low=`157.42`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `157.68` (Distance: `-0.02%`)
  * Point of Control (POC) = `157.66` (Distance: `-0.00%`)
  * Value Area Low (VAL) = `157.63` (Distance: `+0.02%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`157.99` | POC=`157.87` | VAL=`157.76`
  * Prior Day Extremes: PDH=`158.13` | PDL=`157.60` | PDC=`157.69`
  * Monday Range Blueprint: High=`157.64` | Mid=`157.15` | Low=`156.65`
  * Developing Weekly Value Area: Weekly VAH=`158.08` | Weekly POC=`157.87` | Weekly VAL=`157.48`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`157.70` | Low=`157.60`
  * London Session (08:00-16:00 UTC): High=`158.29` | Low=`157.03`
  * New York Session (13:00-21:00 UTC): High=`158.60` | Low=`156.71`
  * Initial Balance (First Hour): IB High=`158.13` | IB Low=`157.18`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `157.03` - `158.29`
  * Optimal Trade Entry (OTE 0.705): `157.97`
  * Structural Invalidation Anchor (0.786): `158.92`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `157.95` | `157.95` | `157.92` | `157.93` | `425` | 67,120.25 USD | -32,361.55 USD | `-48.21%` | 524,140.72 USD | `-0.92` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `157.93` | `157.94` | `157.91` | `157.92` | `382` | 60,326.59 USD | -14,478.38 USD | `-24.00%` | 509,662.34 USD | `-0.45` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `157.92` | `157.92` | `157.90` | `157.91` | `229` | 36,160.25 USD | -20,861.68 USD | `-57.69%` | 488,800.66 USD | `-0.61` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `157.93` | `157.97` | `157.92` | `157.96` | `1,009` | 159,382.65 USD | 111,235.81 USD | `+69.79%` | 89,619.11 USD | `+0.76` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `157.96` | `157.97` | `157.91` | `157.95` | `1,253` | 197,907.59 USD | 14,843.07 USD | `+7.50%` | 104,462.18 USD | `+0.28` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `157.95` | `157.95` | `157.90` | `157.91` | `1,036` | 163,589.58 USD | -126,701.73 USD | `-77.45%` | -22,239.55 USD | `-1.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `157.88` | `157.94` | `157.85` | `157.90` | `4,730` | 746,885.92 USD | 143,020.71 USD | `+19.15%` | 66,613.67 USD | `+0.23` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `157.90` | `157.97` | `157.84` | `157.96` | `3,894` | 615,100.13 USD | 406,153.91 USD | `+66.03%` | 472,767.57 USD | `+0.71` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `157.96` | `157.98` | `157.89` | `157.96` | `4,930` | 778,752.66 USD | 217,231.01 USD | `+27.89%` | 689,998.58 USD | `+0.35` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `210` | `0x0911...129a` | `SHORT` | 10,434,127.39 USD | `66,223.20` | `156.58` | `157.56` | `167.72` | -65,107.16 USD | `-0.62%` | `20X Isolated` |
| `1093` | `0x9dea...d617` | `LONG` | 2,013,144.12 USD | `12,777.00` | `157.68` | `157.56` | `148.81` | -1,489.82 USD | `-0.07%` | `50X Isolated` |
| `1116` | `0xec0b...b078` | `SHORT` | 1,988,011.72 USD | `12,617.49` | `158.22` | `157.56` | `162.95` | 8,353.95 USD | `+0.42%` | `20X Isolated` |
| `1145` | `0xc966...f6b6` | `SHORT` | 1,949,360.68 USD | `12,372.18` | `157.61` | `157.56` | `215.28` | 562.47 USD | `+0.03%` | `5X Isolated` |
| `1195` | `0xbef1...d2e5` | `LONG` | 1,862,562.45 USD | `11,821.29` | `157.63` | `157.56` | `155.51` | -798.16 USD | `-0.04%` | `50X Isolated` |
| `1874` | `0x3d89...eb14` | `LONG` | 1,087,164.00 USD | `6,900.00` | `158.17` | `157.56` | `127.36` | -4,225.60 USD | `-0.39%` | `5X Isolated` |

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
| `7D` | `141.77` | 89,540.00 USD | 0.00 USD | 89,540.00 USD | 0.00 USD | 0.00 USD | 248.84 USD |
| `1D` | `141.78` | 3,480.00 USD | 0.00 USD | 3,480.00 USD | 0.00 USD | 0.00 USD | 102.85 USD |
| `7D` | `141.93` | 89,300.00 USD | 0.00 USD | 89,300.00 USD | 0.00 USD | 0.00 USD | 2,060.00 USD |
| `1D` | `141.94` | 3,370.00 USD | 0.00 USD | 3,370.00 USD | 0.00 USD | 0.00 USD | 70.13 USD |
| `7D` | `142.09` | 87,230.00 USD | 0.00 USD | 87,230.00 USD | 0.00 USD | 0.00 USD | 1,010.00 USD |
| `7D` | `142.25` | 86,220.00 USD | 0.00 USD | 86,220.00 USD | 0.00 USD | 0.00 USD | 882.48 USD |
| `7D` | `150.41` | 85,340.00 USD | 0.00 USD | 85,340.00 USD | 0.00 USD | 0.00 USD | 253.17 USD |
| `7D` | `150.57` | 85,090.00 USD | 0.00 USD | 85,090.00 USD | 0.00 USD | 0.00 USD | 413.75 USD |
| `7D` | `150.73` | 84,670.00 USD | 0.00 USD | 84,670.00 USD | 0.00 USD | 0.00 USD | 18.41 USD |
| `7D` | `150.89` | 84,660.00 USD | 0.00 USD | 84,660.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `7D` | `151.05` | 84,640.00 USD | 0.00 USD | 84,640.00 USD | 0.00 USD | 0.00 USD | 167.17 USD |
| `7D` | `151.21` | 84,480.00 USD | 0.00 USD | 84,480.00 USD | 0.00 USD | 0.00 USD | 687.73 USD |
| `1D` | `151.22` | 3,300.00 USD | 0.00 USD | 3,300.00 USD | 0.00 USD | 0.00 USD | 150.24 USD |
| `7D` | `151.37` | 83,790.00 USD | 0.00 USD | 83,790.00 USD | 0.00 USD | 0.00 USD | 5,340.00 USD |
| `1D` | `151.38` | 3,150.00 USD | 0.00 USD | 3,150.00 USD | 0.00 USD | 0.00 USD | 321.48 USD |
| `7D` | `151.53` | 78,450.00 USD | 0.00 USD | 78,450.00 USD | 0.00 USD | 0.00 USD | 1,430.00 USD |
| `7D` | `151.69` | 77,020.00 USD | 0.00 USD | 77,020.00 USD | 0.00 USD | 0.00 USD | 3,870.00 USD |
| `7D` | `153.61` | 73,150.00 USD | 0.00 USD | 73,150.00 USD | 0.00 USD | 0.00 USD | 1,090.00 USD |
| `7D` | `153.77` | 72,060.00 USD | 0.00 USD | 72,060.00 USD | 0.00 USD | 0.00 USD | 240.95 USD |
| `7D` | `153.93` | 71,820.00 USD | 0.00 USD | 71,820.00 USD | 0.00 USD | 0.00 USD | 63.58 USD |
| `7D` | `154.09` | 71,750.00 USD | 0.00 USD | 71,750.00 USD | 0.00 USD | 0.00 USD | 110.19 USD |
| `7D` | `154.25` | 71,640.00 USD | 0.00 USD | 71,640.00 USD | 0.00 USD | 0.00 USD | 541.18 USD |
| `7D` | `154.41` | 71,100.00 USD | 0.00 USD | 71,100.00 USD | 0.00 USD | 0.00 USD | 5,510.00 USD |
| `1D` | `154.42` | 2,830.00 USD | 0.00 USD | 2,830.00 USD | 0.00 USD | 0.00 USD | 740.09 USD |
| `7D` | `154.57` | 65,590.00 USD | 0.00 USD | 65,590.00 USD | 0.00 USD | 0.00 USD | 6,330.00 USD |
| `1D` | `154.58` | 2,090.00 USD | 0.00 USD | 2,090.00 USD | 0.00 USD | 0.00 USD | 203.39 USD |
| `7D` | `154.73` | 59,270.00 USD | 0.00 USD | 59,270.00 USD | 0.00 USD | 0.00 USD | 5,030.00 USD |
| `7D` | `154.89` | 54,240.00 USD | 0.00 USD | 54,240.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD |
| `7D` | `155.05` | 48,770.00 USD | 0.00 USD | 48,770.00 USD | 0.00 USD | 0.00 USD | 236.38 USD |
| `7D` | `155.21` | 48,530.00 USD | 0.00 USD | 48,530.00 USD | 0.00 USD | 0.00 USD | 1,950.00 USD |
| `7D` | `155.37` | 46,580.00 USD | 0.00 USD | 46,580.00 USD | 0.00 USD | 0.00 USD | 477.16 USD |
| `7D` | `155.53` | 46,100.00 USD | 0.00 USD | 46,100.00 USD | 0.00 USD | 0.00 USD | 127.16 USD |
| `7D` | `155.69` | 45,970.00 USD | 0.00 USD | 45,970.00 USD | 0.00 USD | 0.00 USD | 220.37 USD |
| `7D` | `155.85` | 45,750.00 USD | 0.00 USD | 45,750.00 USD | 0.00 USD | 0.00 USD | 1,200.00 USD |
| `1D` | `155.86` | 1,890.00 USD | 0.00 USD | 1,890.00 USD | 0.00 USD | 0.00 USD | 187.01 USD |
| `7D` | `156.01` | 44,560.00 USD | 0.00 USD | 44,560.00 USD | 0.00 USD | 0.00 USD | 14,270.00 USD |
| `1D` | `156.02` | 1,700.00 USD | 0.00 USD | 1,700.00 USD | 0.00 USD | 0.00 USD | 1,430.00 USD |
| `7D` | `156.17` | 30,290.00 USD | 0.00 USD | 30,290.00 USD | 0.00 USD | 0.00 USD | 9,290.00 USD |
| `1D` | `156.18` | 270.90 USD | 0.00 USD | 270.90 USD | 0.00 USD | 0.00 USD | 270.90 USD |
| `7D` | `156.33` | 21,000.00 USD | 0.00 USD | 21,000.00 USD | 0.00 USD | 0.00 USD | 12,170.00 USD |
| `7D` | `156.49` | 8,820.00 USD | 0.00 USD | 8,820.00 USD | 0.00 USD | 0.00 USD | 8,820.00 USD |
| `1D` | `157.44` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `157.44` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `158.25` | 1,010.00 USD | 1,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,010.00 USD |
| `7D` | `158.41` | 2,670.00 USD | 2,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,650.00 USD |
| `7D` | `158.57` | 2,740.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 73.64 USD |
| `7D` | `158.73` | 2,790.00 USD | 2,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 53.52 USD |
| `7D` | `158.89` | 3,460.00 USD | 3,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 668.68 USD |
| `7D` | `159.05` | 5,510.00 USD | 5,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,050.00 USD |
| `1D` | `159.06` | 473.77 USD | 473.77 USD | 0.00 USD | 0.00 USD | 0.00 USD | 473.77 USD |
| `7D` | `159.21` | 24,610.00 USD | 24,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,100.00 USD |
| `1D` | `159.22` | 1,630.00 USD | 1,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,160.00 USD |
| `7D` | `159.37` | 33,280.00 USD | 33,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,670.00 USD |
| `1D` | `159.38` | 1,890.00 USD | 1,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 254.68 USD |
| `7D` | `159.53` | 48,770.00 USD | 48,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,490.00 USD |
| `7D` | `159.85` | 49,750.00 USD | 49,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 982.65 USD |
| `7D` | `160.01` | 50,100.00 USD | 50,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 351.19 USD |
| `7D` | `160.17` | 50,140.00 USD | 50,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 36.82 USD |
| `7D` | `160.33` | 50,160.00 USD | 50,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `7D` | `160.49` | 50,500.00 USD | 50,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 334.35 USD |
| `7D` | `160.65` | 51,660.00 USD | 51,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,170.00 USD |
| `1D` | `160.66` | 2,160.00 USD | 2,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 277.44 USD |
| `7D` | `160.81` | 62,370.00 USD | 62,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,710.00 USD |
| `1D` | `160.82` | 2,830.00 USD | 2,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 663.01 USD |
| `7D` | `160.97` | 65,410.00 USD | 65,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,040.00 USD |
| `1D` | `160.98` | 2,830.00 USD | 2,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.03 USD |
| `7D` | `161.13` | 73,150.00 USD | 73,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,740.00 USD |
| `7D` | `162.89` | 73,210.00 USD | 73,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 59.10 USD |
| `7D` | `163.05` | 73,700.00 USD | 73,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 488.53 USD |
| `7D` | `163.21` | 73,820.00 USD | 73,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 119.29 USD |
| `7D` | `163.37` | 73,850.00 USD | 73,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31.79 USD |
| `7D` | `163.53` | 73,900.00 USD | 73,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 55.09 USD |
| `7D` | `163.69` | 74,170.00 USD | 74,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 270.59 USD |
| `7D` | `163.85` | 76,860.00 USD | 76,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,690.00 USD |
| `1D` | `163.86` | 3,170.00 USD | 3,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 338.49 USD |
| `7D` | `164.01` | 80,080.00 USD | 80,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,220.00 USD |
| `1D` | `164.02` | 3,300.00 USD | 3,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 133.23 USD |
| `7D` | `164.17` | 81,470.00 USD | 81,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,390.00 USD |
| `7D` | `164.33` | 85,340.00 USD | 85,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,870.00 USD |
| `7D` | `172.33` | 85,400.00 USD | 85,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 57.70 USD |
| `7D` | `172.49` | 85,610.00 USD | 85,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 207.16 USD |
| `7D` | `172.65` | 85,610.00 USD | 85,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7.36 USD |
| `7D` | `172.81` | 85,620.00 USD | 85,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.35 USD |
| `7D` | `172.97` | 85,640.00 USD | 85,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22.04 USD |
| `7D` | `173.13` | 85,750.00 USD | 85,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 108.23 USD |
| `7D` | `173.29` | 86,790.00 USD | 86,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,040.00 USD |
| `1D` | `173.30` | 3,410.00 USD | 3,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 107.90 USD |
| `1D` | `173.38` | 3,450.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 37.99 USD |
| `7D` | `173.45` | 87,980.00 USD | 87,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,190.00 USD |
| `7D` | `173.55` | 88,130.00 USD | 88,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 149.65 USD |

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
  * Current Rate: `-2.10` | Last 24h: `-640.25` | Last 3d: `-882.53` | Last 7d: `-882.53`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-0.0121%` | **USDT BingX** | `-` |
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
| `21:45:00` | `157.94` | `157.94` | `157.94` | `157.94` | `157.92` | 40,590.07 USD | 34,715.19 USD | 5,874.88 USD | 28,840.31 USD | `+71.05%` | `1B / 0S` |
| `21:50:00` | `157.94` | `157.94` | `157.94` | `157.97` | `157.92` | 62,543.84 USD | 26,059.93 USD | 36,483.91 USD | -10,423.97 USD | `-16.67%` | `0B / 1S` |
| `21:55:00` | `157.96` | `157.96` | `157.96` | `157.96` | `157.92` | 56,234.12 USD | 47,865.94 USD | 8,368.17 USD | 39,497.77 USD | `+70.24%` | `1B / 0S` |
| `22:00:00` | `157.96` | `157.96` | `157.96` | `157.98` | `157.89` | 778,752.66 USD | 497,991.83 USD | 280,760.83 USD | 217,231.01 USD | `+27.89%` | `1B / 0S` |
| `22:00:00` | `157.95` | `157.95` | `157.95` | `157.97` | `157.91` | 197,907.59 USD | 106,375.33 USD | 91,532.26 USD | 14,843.07 USD | `+7.50%` | `1B / 0S` |
| `22:00:00` | `157.92` | `157.92` | `157.92` | `157.96` | `157.92` | 76,908.99 USD | 7,324.67 USD | 69,584.32 USD | -62,259.66 USD | `-80.95%` | `0B / 1S` |
| `22:05:00` | `157.94` | `157.94` | `157.94` | `157.94` | `157.91` | 52,910.91 USD | 46,475.79 USD | 6,435.11 USD | 40,040.68 USD | `+75.68%` | `1B / 0S` |
| `22:10:00` | `157.95` | `157.95` | `157.95` | `157.97` | `157.93` | 68,075.16 USD | 34,037.58 USD | 34,037.58 USD | 0.00 USD | `+0.00%` | `0B / 0S` |
| `22:15:00` | `157.93` | `157.93` | `157.93` | `157.95` | `157.92` | 67,120.25 USD | 17,379.35 USD | 49,740.90 USD | -32,361.55 USD | `-48.21%` | `0B / 1S` |
| `22:15:00` | `157.91` | `157.91` | `157.91` | `157.95` | `157.90` | 163,589.58 USD | 18,443.92 USD | 145,145.66 USD | -126,701.73 USD | `-77.45%` | `0B / 1S` |

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
  * `2026-10-30 03:30:02 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:54:02 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:51:02 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:50:02 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:50:02 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:52:02 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:52:02 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:02 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:02 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:02 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `157.63` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `157.54` (Risk Distance: `0.0933` pts)
  * +2.5R Take Profit: `157.86`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.09 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `157.68` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `157.77` (Risk Distance: `0.0933` pts)
  * +2.5R Take Profit: `157.45`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.09 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`158.92`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
