# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USDJPY
**Canonical Key**: `USDJPY` | **Broker Instrument**: `USDJPY.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-29 22:30:50 IST` (`2026-10-29 17:00:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `157.91` | **Live Ask Quote**: `157.91` | **Mid Price**: `157.91`
- **Spread Points**: `1.00` | **Spread BPS**: `0.06 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `157.88` | VWAP Z-Score: `-0.46` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1057` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `40.11` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `158.20` | Lower -3.00σ Band: `157.56`
  * Upper +2.51σ Band: `158.15` | Lower -2.51σ Band: `157.61`
  * Upper +2.01σ Band: `158.10` | Lower -2.01σ Band: `157.66`
  * Upper +2.00σ Band: `158.09` | Lower -2.00σ Band: `157.67`
  * Upper +1.28σ Band: `158.02` | Lower -1.28σ Band: `157.74`
  * Upper +1.00σ Band: `157.99` | Lower -1.00σ Band: `157.77`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`157.96` | EMA-20=`157.96` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`157.92` (Slope: `+0.0000`) | EMA-100=`157.91`
  * Institutional Anchors: EMA-144=`157.89` | EMA-200=`157.85` (Slope: `+0.0108`) | EMA-233=`157.82`
- **Range Boundaries**: 24H High=`158.35` | 24H Low=`157.60` | Weekly High=`158.35` | Weekly Low=`157.24`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `157.98` (Distance: `-0.04%`)
  * Point of Control (POC) = `157.86` (Distance: `+0.04%`)
  * Value Area Low (VAL) = `157.73` (Distance: `+0.12%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`158.04` | POC=`157.89` | VAL=`157.79`
  * Prior Day Extremes: PDH=`158.35` | PDL=`157.65` | PDC=`157.82`
  * Monday Range Blueprint: High=`157.64` | Mid=`157.15` | Low=`156.65`
  * Developing Weekly Value Area: Weekly VAH=`158.08` | Weekly POC=`157.87` | Weekly VAL=`157.45`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`158.07` | Low=`157.60`
  * London Session (08:00-16:00 UTC): High=`158.08` | Low=`157.77`
  * New York Session (13:00-21:00 UTC): High=`158.13` | Low=`157.71`
  * Initial Balance (First Hour): IB High=`157.91` | IB Low=`157.80`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `157.28` - `158.54`
  * Optimal Trade Entry (OTE 0.705): `158.23`
  * Structural Invalidation Anchor (0.786): `159.17`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `158.02` | `158.02` | `157.97` | `157.97` | `367` | 57,974.99 USD | -50,170.66 USD | `-86.54%` | -87,365.07 USD | `-1.69` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `157.97` | `157.98` | `157.94` | `157.94` | `350` | 55,280.75 USD | -45,358.56 USD | `-82.05%` | -132,723.64 USD | `-1.38` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `157.94` | `157.98` | `157.94` | `157.98` | `325` | 51,344.15 USD | 46,209.73 USD | `+90.00%` | -86,513.90 USD | `+1.35` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `157.98` | `158.05` | `157.98` | `158.02` | `1,480` | 233,865.16 USD | 63,923.14 USD | `+27.33%` | 30,403.17 USD | `+0.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `158.02` | `158.05` | `158.00` | `158.02` | `1,244` | 196,571.90 USD | -53,416.28 USD | `-27.17%` | -23,013.11 USD | `-0.82` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `158.02` | `158.02` | `157.94` | `157.98` | `1,042` | 164,617.24 USD | -37,208.01 USD | `-22.60%` | -60,221.12 USD | `-0.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `157.87` | `157.97` | `157.81` | `157.96` | `5,932` | 937,018.72 USD | 683,116.87 USD | `+72.90%` | -238,478.95 USD | `+1.52` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `157.96` | `158.05` | `157.94` | `158.02` | `5,363` | 847,439.81 USD | 356,224.70 USD | `+42.04%` | 117,745.75 USD | `+0.85` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `158.02` | `158.04` | `157.92` | `158.02` | `4,719` | 745,682.22 USD | 242,187.39 USD | `+32.48%` | 359,933.14 USD | `+0.65` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `157.97` | `158.00` | `157.60` | `157.82` | `28,963` | 4,570,824.81 USD | -704,091.70 USD | `-15.40%` | -3,349,118.53 USD | `+0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.82` | `157.97` | `157.77` | `157.87` | `20,616` | 3,254,647.92 USD | 426,971.14 USD | `+13.12%` | -2,922,147.39 USD | `+0.38` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `157.87` | `158.08` | `157.81` | `158.06` | `23,822` | 3,765,376.79 USD | 3,094,533.80 USD | `+82.18%` | 172,386.40 USD | `+1.11` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `158.15` | `158.35` | `157.76` | `157.82` | `52,103` | 8,223,051.77 USD | -5,602,130.63 USD | `-68.13%` | -4,035,056.10 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.74` | `158.07` | `157.70` | `157.97` | `16,828` | 2,658,251.85 USD | 1,390,029.27 USD | `+52.29%` | -2,645,026.83 USD | `+0.68` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `157.97` | `158.00` | `157.60` | `157.82` | `28,963` | 4,570,824.81 USD | -704,091.70 USD | `-15.40%` | -3,349,118.53 USD | `+0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.82` | `157.97` | `157.77` | `157.87` | `20,616` | 3,254,647.92 USD | 426,971.14 USD | `+13.12%` | -2,922,147.39 USD | `+0.38` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `157.87` | `158.08` | `157.81` | `158.06` | `23,822` | 3,765,376.79 USD | 3,094,533.80 USD | `+82.18%` | 172,386.40 USD | `+1.11` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `221` | `0x0911...129a` | `SHORT` | 10,451,345.42 USD | `66,223.20` | `156.58` | `157.81` | `167.73` | -82,325.19 USD | `-0.79%` | `20X Isolated` |
| `1149` | `0xec0b...b078` | `SHORT` | 1,991,166.10 USD | `12,617.49` | `158.22` | `157.81` | `162.96` | 5,199.58 USD | `+0.26%` | `20X Isolated` |
| `1236` | `0xbef1...d2e5` | `LONG` | 1,865,635.99 USD | `11,821.29` | `157.63` | `157.81` | `155.52` | 2,275.38 USD | `+0.12%` | `50X Isolated` |
| `1290` | `0xc966...f6b6` | `SHORT` | 1,788,814.22 USD | `11,335.24` | `157.58` | `157.81` | `196.58` | -2,555.09 USD | `-0.14%` | `5X Isolated` |
| `1533` | `0x9dea...d617` | `LONG` | 1,467,118.39 USD | `9,296.15` | `157.69` | `157.81` | `146.11` | 1,201.51 USD | `+0.08%` | `50X Isolated` |
| `1920` | `0x3d89...eb14` | `LONG` | 1,089,027.00 USD | `6,900.00` | `158.17` | `157.81` | `127.36` | -2,362.60 USD | `-0.22%` | `5X Isolated` |

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
| `7D` | `141.72` | 90,440.00 USD | 0.00 USD | 90,440.00 USD | 0.00 USD | 0.00 USD | 164.20 USD |
| `1D` | `141.85` | 14,490.00 USD | 0.00 USD | 14,490.00 USD | 0.00 USD | 0.00 USD | 136.81 USD |
| `7D` | `141.88` | 90,280.00 USD | 0.00 USD | 90,280.00 USD | 0.00 USD | 0.00 USD | 2,090.00 USD |
| `1D` | `142.01` | 14,350.00 USD | 0.00 USD | 14,350.00 USD | 0.00 USD | 0.00 USD | 35.67 USD |
| `7D` | `142.04` | 88,180.00 USD | 0.00 USD | 88,180.00 USD | 0.00 USD | 0.00 USD | 1,100.00 USD |
| `1D` | `142.17` | 14,310.00 USD | 0.00 USD | 14,310.00 USD | 0.00 USD | 0.00 USD | 592.37 USD |
| `7D` | `142.20` | 87,080.00 USD | 0.00 USD | 87,080.00 USD | 0.00 USD | 0.00 USD | 882.31 USD |
| `7D` | `150.04` | 86,200.00 USD | 0.00 USD | 86,200.00 USD | 0.00 USD | 0.00 USD | 46.51 USD |
| `7D` | `150.20` | 86,150.00 USD | 0.00 USD | 86,150.00 USD | 0.00 USD | 0.00 USD | 44.72 USD |
| `7D` | `150.36` | 86,110.00 USD | 0.00 USD | 86,110.00 USD | 0.00 USD | 0.00 USD | 95.97 USD |
| `7D` | `150.52` | 86,010.00 USD | 0.00 USD | 86,010.00 USD | 0.00 USD | 0.00 USD | 516.04 USD |
| `7D` | `150.68` | 85,500.00 USD | 0.00 USD | 85,500.00 USD | 0.00 USD | 0.00 USD | 152.11 USD |
| `7D` | `150.84` | 85,340.00 USD | 0.00 USD | 85,340.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `7D` | `151.00` | 85,330.00 USD | 0.00 USD | 85,330.00 USD | 0.00 USD | 0.00 USD | 55.10 USD |
| `1D` | `151.13` | 13,720.00 USD | 0.00 USD | 13,720.00 USD | 0.00 USD | 0.00 USD | 46.75 USD |
| `7D` | `151.16` | 85,280.00 USD | 0.00 USD | 85,280.00 USD | 0.00 USD | 0.00 USD | 393.33 USD |
| `1D` | `151.29` | 13,680.00 USD | 0.00 USD | 13,680.00 USD | 0.00 USD | 0.00 USD | 339.84 USD |
| `7D` | `151.32` | 84,880.00 USD | 0.00 USD | 84,880.00 USD | 0.00 USD | 0.00 USD | 4,210.00 USD |
| `1D` | `151.45` | 13,340.00 USD | 0.00 USD | 13,340.00 USD | 0.00 USD | 0.00 USD | 91.80 USD |
| `7D` | `151.48` | 80,670.00 USD | 0.00 USD | 80,670.00 USD | 0.00 USD | 0.00 USD | 4,050.00 USD |
| `1D` | `151.61` | 13,240.00 USD | 0.00 USD | 13,240.00 USD | 0.00 USD | 0.00 USD | 1,480.00 USD |
| `7D` | `151.64` | 76,620.00 USD | 0.00 USD | 76,620.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD |
| `7D` | `153.24` | 73,890.00 USD | 0.00 USD | 73,890.00 USD | 0.00 USD | 0.00 USD | 149.62 USD |
| `7D` | `153.40` | 73,740.00 USD | 0.00 USD | 73,740.00 USD | 0.00 USD | 0.00 USD | 32.85 USD |
| `7D` | `153.56` | 73,700.00 USD | 0.00 USD | 73,700.00 USD | 0.00 USD | 0.00 USD | 860.16 USD |
| `7D` | `153.72` | 72,840.00 USD | 0.00 USD | 72,840.00 USD | 0.00 USD | 0.00 USD | 392.58 USD |
| `7D` | `153.88` | 72,450.00 USD | 0.00 USD | 72,450.00 USD | 0.00 USD | 0.00 USD | 275.51 USD |
| `7D` | `154.04` | 72,170.00 USD | 0.00 USD | 72,170.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `7D` | `154.20` | 72,150.00 USD | 0.00 USD | 72,150.00 USD | 0.00 USD | 0.00 USD | 334.38 USD |
| `1D` | `154.33` | 11,760.00 USD | 0.00 USD | 11,760.00 USD | 0.00 USD | 0.00 USD | 230.40 USD |
| `7D` | `154.36` | 71,810.00 USD | 0.00 USD | 71,810.00 USD | 0.00 USD | 0.00 USD | 754.85 USD |
| `1D` | `154.49` | 11,530.00 USD | 0.00 USD | 11,530.00 USD | 0.00 USD | 0.00 USD | 568.79 USD |
| `7D` | `154.52` | 71,060.00 USD | 0.00 USD | 71,060.00 USD | 0.00 USD | 0.00 USD | 10,780.00 USD |
| `1D` | `154.65` | 10,960.00 USD | 0.00 USD | 10,960.00 USD | 0.00 USD | 0.00 USD | 159.61 USD |
| `7D` | `154.68` | 60,280.00 USD | 0.00 USD | 60,280.00 USD | 0.00 USD | 0.00 USD | 5,740.00 USD |
| `1D` | `154.81` | 10,800.00 USD | 0.00 USD | 10,800.00 USD | 0.00 USD | 0.00 USD | 2,960.00 USD |
| `7D` | `154.84` | 54,540.00 USD | 0.00 USD | 54,540.00 USD | 0.00 USD | 0.00 USD | 5,580.00 USD |
| `7D` | `155.00` | 48,960.00 USD | 0.00 USD | 48,960.00 USD | 0.00 USD | 0.00 USD | 65.69 USD |
| `7D` | `155.16` | 48,890.00 USD | 0.00 USD | 48,890.00 USD | 0.00 USD | 0.00 USD | 2,430.00 USD |
| `7D` | `155.32` | 46,460.00 USD | 0.00 USD | 46,460.00 USD | 0.00 USD | 0.00 USD | 548.95 USD |
| `7D` | `155.48` | 45,910.00 USD | 0.00 USD | 45,910.00 USD | 0.00 USD | 0.00 USD | 73.64 USD |
| `7D` | `155.64` | 45,840.00 USD | 0.00 USD | 45,840.00 USD | 0.00 USD | 0.00 USD | 53.53 USD |
| `7D` | `155.80` | 45,780.00 USD | 0.00 USD | 45,780.00 USD | 0.00 USD | 0.00 USD | 1,300.00 USD |
| `1D` | `155.93` | 7,840.00 USD | 0.00 USD | 7,840.00 USD | 0.00 USD | 0.00 USD | 512.51 USD |
| `7D` | `155.96` | 44,480.00 USD | 0.00 USD | 44,480.00 USD | 0.00 USD | 0.00 USD | 8,390.00 USD |
| `1D` | `156.09` | 7,330.00 USD | 0.00 USD | 7,330.00 USD | 0.00 USD | 0.00 USD | 1,400.00 USD |
| `7D` | `156.12` | 36,090.00 USD | 0.00 USD | 36,090.00 USD | 0.00 USD | 0.00 USD | 15,050.00 USD |
| `1D` | `156.25` | 5,930.00 USD | 0.00 USD | 5,930.00 USD | 0.00 USD | 0.00 USD | 3.93 USD |
| `7D` | `156.28` | 21,030.00 USD | 0.00 USD | 21,030.00 USD | 0.00 USD | 0.00 USD | 10,100.00 USD |
| `1D` | `156.41` | 5,920.00 USD | 0.00 USD | 5,920.00 USD | 0.00 USD | 0.00 USD | 5,920.00 USD |
| `7D` | `156.44` | 10,940.00 USD | 0.00 USD | 10,940.00 USD | 0.00 USD | 0.00 USD | 10,940.00 USD |
| `1D` | `157.58` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `157.58` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `157.88` | 186.03 USD | 186.03 USD | 0.00 USD | 0.00 USD | 0.00 USD | 186.03 USD |
| `7D` | `158.04` | 251.72 USD | 251.72 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65.69 USD |
| `7D` | `158.20` | 635.64 USD | 635.64 USD | 0.00 USD | 0.00 USD | 0.00 USD | 383.92 USD |
| `7D` | `158.36` | 2,700.00 USD | 2,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,060.00 USD |
| `7D` | `158.52` | 3,310.00 USD | 3,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 608.44 USD |
| `7D` | `158.68` | 3,360.00 USD | 3,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 53.53 USD |
| `7D` | `158.84` | 3,580.00 USD | 3,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 220.39 USD |
| `7D` | `159.00` | 4,920.00 USD | 4,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,340.00 USD |
| `1D` | `159.13` | 1,270.00 USD | 1,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD |
| `7D` | `159.16` | 18,600.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,680.00 USD |
| `1D` | `159.29` | 1,910.00 USD | 1,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 639.52 USD |
| `7D` | `159.32` | 34,000.00 USD | 34,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,390.00 USD |
| `1D` | `159.45` | 1,930.00 USD | 1,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19.13 USD |
| `7D` | `159.48` | 49,290.00 USD | 49,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,300.00 USD |
| `1D` | `159.61` | 7,840.00 USD | 7,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,910.00 USD |
| `7D` | `159.64` | 49,330.00 USD | 49,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 32.85 USD |
| `7D` | `159.80` | 49,860.00 USD | 49,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 537.21 USD |
| `7D` | `159.96` | 50,550.00 USD | 50,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 686.81 USD |
| `7D` | `160.12` | 50,850.00 USD | 50,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 304.23 USD |
| `7D` | `160.28` | 50,880.00 USD | 50,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `7D` | `160.44` | 50,990.00 USD | 50,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 110.19 USD |
| `1D` | `160.57` | 7,870.00 USD | 7,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.82 USD |
| `7D` | `160.60` | 51,780.00 USD | 51,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 786.66 USD |
| `1D` | `160.73` | 8,610.00 USD | 8,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 741.27 USD |
| `7D` | `160.76` | 59,190.00 USD | 59,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,410.00 USD |
| `1D` | `160.89` | 8,800.00 USD | 8,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 188.75 USD |
| `7D` | `160.92` | 68,300.00 USD | 68,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,120.00 USD |
| `1D` | `161.05` | 8,810.00 USD | 8,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9.56 USD |
| `7D` | `161.08` | 73,770.00 USD | 73,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD |
| `1D` | `161.21` | 11,760.00 USD | 11,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,950.00 USD |
| `7D` | `162.52` | 73,820.00 USD | 73,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 46.51 USD |
| `7D` | `162.68` | 73,850.00 USD | 73,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28.30 USD |
| `7D` | `162.84` | 73,860.00 USD | 73,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16.42 USD |
| `7D` | `163.00` | 74,470.00 USD | 74,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 608.47 USD |
| `7D` | `163.16` | 74,610.00 USD | 74,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 137.24 USD |
| `7D` | `163.32` | 74,630.00 USD | 74,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18.41 USD |
| `7D` | `163.48` | 74,640.00 USD | 74,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `7D` | `163.64` | 74,810.00 USD | 74,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 167.19 USD |
| `1D` | `163.77` | 11,880.00 USD | 11,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 115.19 USD |
| `7D` | `163.80` | 75,150.00 USD | 75,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 342.77 USD |
| `1D` | `163.93` | 12,150.00 USD | 12,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 273.08 USD |
| `7D` | `163.96` | 80,520.00 USD | 80,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,360.00 USD |
| `1D` | `164.09` | 12,240.00 USD | 12,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 90.12 USD |
| `7D` | `164.12` | 83,350.00 USD | 83,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,840.00 USD |
| `1D` | `164.25` | 13,720.00 USD | 13,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,480.00 USD |
| `7D` | `164.28` | 86,090.00 USD | 86,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD |
| `7D` | `171.96` | 86,110.00 USD | 86,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18.60 USD |
| `7D` | `172.12` | 86,120.00 USD | 86,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11.32 USD |
| `7D` | `172.28` | 86,140.00 USD | 86,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23.24 USD |
| `7D` | `172.44` | 86,360.00 USD | 86,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 219.64 USD |
| `7D` | `172.60` | 86,410.00 USD | 86,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 53.48 USD |
| `7D` | `172.76` | 86,420.00 USD | 86,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7.36 USD |
| `7D` | `172.92` | 86,430.00 USD | 86,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.35 USD |
| `7D` | `173.08` | 86,490.00 USD | 86,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 66.88 USD |
| `1D` | `173.21` | 13,750.00 USD | 13,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 30.06 USD |
| `7D` | `173.24` | 86,620.00 USD | 86,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 129.14 USD |
| `1D` | `173.37` | 13,860.00 USD | 13,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 110.07 USD |
| `7D` | `173.40` | 88,700.00 USD | 88,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,080.00 USD |
| `1D` | `173.51` | 13,900.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 35.28 USD |
| `7D` | `173.52` | 89,380.00 USD | 89,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 681.46 USD |

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
  * Current Rate: `-379.53` | Last 24h: `-445.71` | Last 3d: `-623.11` | Last 7d: `-623.11`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0200%` | **USDT BingX** | `-` |
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
| `13:30:00` | `158.04` | `158.04` | `158.04` | `158.04` | `157.98` | 58,158.72 USD | 55,250.78 USD | 2,907.94 USD | 52,342.85 USD | `+90.00%` | `1B / 0S` |
| `13:35:00` | `158.04` | `158.04` | `158.04` | `158.05` | `158.02` | 107,311.88 USD | 69,437.10 USD | 37,874.78 USD | 31,562.32 USD | `+29.41%` | `1B / 0S` |
| `13:40:00` | `158.02` | `158.02` | `158.02` | `158.05` | `158.00` | 68,421.36 USD | 16,748.98 USD | 51,672.38 USD | -34,923.40 USD | `-51.04%` | `0B / 1S` |
| `13:45:00` | `158.03` | `158.03` | `158.03` | `158.05` | `158.02` | 54,205.66 USD | 37,492.25 USD | 16,713.41 USD | 20,778.84 USD | `+38.33%` | `1B / 0S` |
| `13:45:00` | `158.02` | `158.02` | `158.02` | `158.05` | `158.00` | 196,571.90 USD | 71,577.81 USD | 124,994.09 USD | -53,416.28 USD | `-27.17%` | `0B / 1S` |
| `13:50:00` | `158.03` | `158.03` | `158.03` | `158.05` | `158.02` | 70,639.86 USD | 31,164.64 USD | 39,475.21 USD | -8,310.57 USD | `-11.76%` | `0B / 1S` |
| `13:55:00` | `158.02` | `158.02` | `158.02` | `158.03` | `158.00` | 71,739.26 USD | 22,584.58 USD | 49,154.68 USD | -26,570.10 USD | `-37.04%` | `0B / 1S` |
| `14:00:00` | `157.97` | `157.97` | `157.97` | `158.02` | `157.97` | 57,974.99 USD | 3,902.16 USD | 54,072.83 USD | -50,170.66 USD | `-86.54%` | `0B / 1S` |
| `14:00:00` | `158.02` | `158.02` | `158.02` | `158.04` | `157.92` | 745,682.22 USD | 493,934.81 USD | 251,747.42 USD | 242,187.39 USD | `+32.48%` | `1B / 0S` |
| `14:00:00` | `157.98` | `157.98` | `157.98` | `158.02` | `157.94` | 164,617.24 USD | 63,704.62 USD | 100,912.63 USD | -37,208.01 USD | `-22.60%` | `0B / 1S` |

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
  * `2026-10-29 19:41:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:20:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:09:49 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-29 16:50:49 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [bankofengland.co.uk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `157.73` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `157.60` (Risk Distance: `0.1284` pts)
  * +2.5R Take Profit: `158.05`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.13 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `157.98` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `158.11` (Risk Distance: `0.1284` pts)
  * +2.5R Take Profit: `157.66`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.13 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`159.17`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
