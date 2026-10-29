# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USDJPY
**Canonical Key**: `USDJPY` | **Broker Instrument**: `USDJPY.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-29 23:56:00 IST` (`2026-10-29 18:26:00 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `157.88` | **Live Ask Quote**: `157.88` | **Mid Price**: `157.88`
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
  * Session VWAP: `157.88` | VWAP Z-Score: `-0.32` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0903` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `45.73` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `158.16` | Lower -3.00σ Band: `157.59`
  * Upper +2.51σ Band: `158.12` | Lower -2.51σ Band: `157.64`
  * Upper +2.01σ Band: `158.07` | Lower -2.01σ Band: `157.69`
  * Upper +2.00σ Band: `158.07` | Lower -2.00σ Band: `157.69`
  * Upper +1.28σ Band: `158.00` | Lower -1.28σ Band: `157.75`
  * Upper +1.00σ Band: `157.97` | Lower -1.00σ Band: `157.78`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`157.88` | EMA-20=`157.89` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`157.89` (Slope: `+0.0000`) | EMA-100=`157.89`
  * Institutional Anchors: EMA-144=`157.88` | EMA-200=`157.85` (Slope: `+0.0009`) | EMA-233=`157.84`
- **Range Boundaries**: 24H High=`158.35` | 24H Low=`157.60` | Weekly High=`158.35` | Weekly Low=`157.37`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `157.97` (Distance: `-0.06%`)
  * Point of Control (POC) = `157.87` (Distance: `+0.01%`)
  * Value Area Low (VAL) = `157.75` (Distance: `+0.08%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`158.04` | POC=`157.89` | VAL=`157.79`
  * Prior Day Extremes: PDH=`158.35` | PDL=`157.65` | PDC=`157.82`
  * Monday Range Blueprint: High=`157.64` | Mid=`157.15` | Low=`156.65`
  * Developing Weekly Value Area: Weekly VAH=`158.08` | Weekly POC=`157.87` | Weekly VAL=`157.47`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`158.07` | Low=`157.60`
  * London Session (08:00-16:00 UTC): High=`158.08` | Low=`157.77`
  * New York Session (13:00-21:00 UTC): High=`158.13` | Low=`157.71`
  * Initial Balance (First Hour): IB High=`157.91` | IB Low=`157.80`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `157.25` - `158.51`
  * Optimal Trade Entry (OTE 0.705): `158.19`
  * Structural Invalidation Anchor (0.786): `159.14`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `157.83` | `157.86` | `157.80` | `157.85` | `453` | 71,507.86 USD | 40,781.83 USD | `+57.03%` | -265,585.65 USD | `+0.27` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `157.85` | `157.91` | `157.84` | `157.88` | `531` | 83,836.40 USD | 28,818.76 USD | `+34.37%` | -236,766.88 USD | `+0.24` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `157.88` | `157.88` | `157.80` | `157.81` | `721` | 113,778.13 USD | -102,400.31 USD | `-90.00%` | -339,167.20 USD | `-1.58` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `157.88` | `157.88` | `157.81` | `157.86` | `1,904` | 300,559.73 USD | -18,527.65 USD | `-6.16%` | -796,310.61 USD | `-0.08` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `157.86` | `157.90` | `157.82` | `157.83` | `1,759` | 277,626.49 USD | -130,835.47 USD | `-47.13%` | -927,146.08 USD | `-0.77` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `157.83` | `157.91` | `157.80` | `157.81` | `1,705` | 269,059.23 USD | -142,863.31 USD | `-53.10%` | -1,070,009.39 USD | `-0.77` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `158.06` | `158.13` | `157.71` | `157.83` | `14,919` | 2,354,665.77 USD | -1,168,822.04 USD | `-49.64%` | -2,025,901.24 USD | `-1.91` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `157.83` | `158.01` | `157.81` | `157.86` | `11,030` | 1,741,162.71 USD | -351,663.40 USD | `-20.20%` | -2,377,564.64 USD | `-0.53` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `157.86` | `157.91` | `157.77` | `157.82` | `7,013` | 1,106,791.66 USD | -321,457.87 USD | `-29.04%` | -2,699,022.51 USD | `-0.61` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.82` | `157.97` | `157.77` | `157.87` | `20,616` | 3,254,647.92 USD | 426,971.14 USD | `+13.12%` | -4,489,221.92 USD | `+0.58` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `157.87` | `158.08` | `157.81` | `158.06` | `23,822` | 3,765,376.79 USD | 3,094,533.80 USD | `+82.18%` | -1,394,688.13 USD | `+1.15` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `158.06` | `158.13` | `157.71` | `157.88` | `37,561` | 5,930,280.92 USD | -1,786,229.19 USD | `-30.12%` | -3,180,917.32 USD | `-0.46` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.74` | `158.07` | `157.70` | `157.97` | `16,828` | 2,658,251.85 USD | 1,390,029.27 USD | `+52.29%` | -4,212,101.36 USD | `+1.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `157.97` | `158.00` | `157.60` | `157.82` | `28,963` | 4,570,824.81 USD | -704,091.70 USD | `-15.40%` | -4,916,193.06 USD | `+0.32` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.82` | `157.97` | `157.77` | `157.87` | `20,616` | 3,254,647.92 USD | 426,971.14 USD | `+13.12%` | -4,489,221.92 USD | `+0.58` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `157.87` | `158.08` | `157.81` | `158.06` | `23,822` | 3,765,376.79 USD | 3,094,533.80 USD | `+82.18%` | -1,394,688.13 USD | `+1.15` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `158.06` | `158.13` | `157.71` | `157.88` | `37,561` | 5,930,280.92 USD | -1,786,229.19 USD | `-30.12%` | -3,180,917.32 USD | `-0.46` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `213` | `0x0911...129a` | `SHORT` | 10,449,358.73 USD | `66,223.20` | `156.58` | `157.80` | `167.73` | -80,338.50 USD | `-0.77%` | `20X Isolated` |
| `1142` | `0xec0b...b078` | `SHORT` | 1,990,913.75 USD | `12,617.49` | `158.22` | `157.80` | `162.95` | 5,451.93 USD | `+0.27%` | `20X Isolated` |
| `1152` | `0xc966...f6b6` | `SHORT` | 1,979,123.68 USD | `12,542.77` | `157.61` | `157.80` | `195.70` | -2,314.61 USD | `-0.12%` | `5X Isolated` |
| `1236` | `0xbef1...d2e5` | `LONG` | 1,865,281.35 USD | `11,821.29` | `157.63` | `157.80` | `155.51` | 1,920.74 USD | `+0.10%` | `50X Isolated` |
| `1523` | `0x9dea...d617` | `LONG` | 1,466,839.51 USD | `9,296.15` | `157.69` | `157.80` | `146.10` | 922.63 USD | `+0.06%` | `50X Isolated` |
| `1891` | `0x3d89...eb14` | `LONG` | 1,088,820.00 USD | `6,900.00` | `158.17` | `157.80` | `127.36` | -2,569.60 USD | `-0.24%` | `5X Isolated` |

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
| `7D` | `141.85` | 89,220.00 USD | 0.00 USD | 89,220.00 USD | 0.00 USD | 0.00 USD | 1,470.00 USD |
| `1D` | `141.96` | 3,450.00 USD | 0.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | 87.11 USD |
| `7D` | `142.01` | 87,750.00 USD | 0.00 USD | 87,750.00 USD | 0.00 USD | 0.00 USD | 1,760.00 USD |
| `1D` | `142.12` | 3,360.00 USD | 0.00 USD | 3,360.00 USD | 0.00 USD | 0.00 USD | 0.39 USD |
| `7D` | `142.17` | 85,990.00 USD | 0.00 USD | 85,990.00 USD | 0.00 USD | 0.00 USD | 882.31 USD |
| `7D` | `150.49` | 85,110.00 USD | 0.00 USD | 85,110.00 USD | 0.00 USD | 0.00 USD | 546.43 USD |
| `7D` | `150.65` | 84,560.00 USD | 0.00 USD | 84,560.00 USD | 0.00 USD | 0.00 USD | 134.89 USD |
| `7D` | `150.81` | 84,430.00 USD | 0.00 USD | 84,430.00 USD | 0.00 USD | 0.00 USD | 31.79 USD |
| `7D` | `150.97` | 84,400.00 USD | 0.00 USD | 84,400.00 USD | 0.00 USD | 0.00 USD | 55.10 USD |
| `1D` | `151.08` | 3,360.00 USD | 0.00 USD | 3,360.00 USD | 0.00 USD | 0.00 USD | 18.10 USD |
| `7D` | `151.13` | 84,340.00 USD | 0.00 USD | 84,340.00 USD | 0.00 USD | 0.00 USD | 334.10 USD |
| `1D` | `151.24` | 3,350.00 USD | 0.00 USD | 3,350.00 USD | 0.00 USD | 0.00 USD | 235.51 USD |
| `7D` | `151.29` | 84,010.00 USD | 0.00 USD | 84,010.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD |
| `1D` | `151.40` | 3,110.00 USD | 0.00 USD | 3,110.00 USD | 0.00 USD | 0.00 USD | 225.91 USD |
| `7D` | `151.45` | 80,590.00 USD | 0.00 USD | 80,590.00 USD | 0.00 USD | 0.00 USD | 4,900.00 USD |
| `1D` | `151.56` | 2,880.00 USD | 0.00 USD | 2,880.00 USD | 0.00 USD | 0.00 USD | 0.98 USD |
| `7D` | `151.61` | 75,690.00 USD | 0.00 USD | 75,690.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD |
| `7D` | `153.53` | 72,950.00 USD | 0.00 USD | 72,950.00 USD | 0.00 USD | 0.00 USD | 349.14 USD |
| `7D` | `153.69` | 72,600.00 USD | 0.00 USD | 72,600.00 USD | 0.00 USD | 0.00 USD | 746.10 USD |
| `7D` | `153.85` | 71,860.00 USD | 0.00 USD | 71,860.00 USD | 0.00 USD | 0.00 USD | 304.23 USD |
| `7D` | `154.01` | 71,550.00 USD | 0.00 USD | 71,550.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `7D` | `154.17` | 71,530.00 USD | 0.00 USD | 71,530.00 USD | 0.00 USD | 0.00 USD | 110.19 USD |
| `1D` | `154.28` | 2,880.00 USD | 0.00 USD | 2,880.00 USD | 0.00 USD | 0.00 USD | 178.99 USD |
| `7D` | `154.33` | 71,420.00 USD | 0.00 USD | 71,420.00 USD | 0.00 USD | 0.00 USD | 909.73 USD |
| `1D` | `154.44` | 2,700.00 USD | 0.00 USD | 2,700.00 USD | 0.00 USD | 0.00 USD | 600.58 USD |
| `7D` | `154.49` | 70,510.00 USD | 0.00 USD | 70,510.00 USD | 0.00 USD | 0.00 USD | 10,580.00 USD |
| `1D` | `154.60` | 2,100.00 USD | 0.00 USD | 2,100.00 USD | 0.00 USD | 0.00 USD | 179.43 USD |
| `7D` | `154.65` | 59,930.00 USD | 0.00 USD | 59,930.00 USD | 0.00 USD | 0.00 USD | 5,830.00 USD |
| `1D` | `154.76` | 1,920.00 USD | 0.00 USD | 1,920.00 USD | 0.00 USD | 0.00 USD | 1.96 USD |
| `7D` | `154.81` | 54,100.00 USD | 0.00 USD | 54,100.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD |
| `7D` | `155.13` | 48,630.00 USD | 0.00 USD | 48,630.00 USD | 0.00 USD | 0.00 USD | 1,680.00 USD |
| `7D` | `155.29` | 46,950.00 USD | 0.00 USD | 46,950.00 USD | 0.00 USD | 0.00 USD | 564.68 USD |
| `7D` | `155.45` | 46,390.00 USD | 0.00 USD | 46,390.00 USD | 0.00 USD | 0.00 USD | 551.01 USD |
| `7D` | `155.61` | 45,840.00 USD | 0.00 USD | 45,840.00 USD | 0.00 USD | 0.00 USD | 53.53 USD |
| `7D` | `155.77` | 45,780.00 USD | 0.00 USD | 45,780.00 USD | 0.00 USD | 0.00 USD | 668.76 USD |
| `1D` | `155.88` | 1,920.00 USD | 0.00 USD | 1,920.00 USD | 0.00 USD | 0.00 USD | 376.36 USD |
| `7D` | `155.93` | 45,110.00 USD | 0.00 USD | 45,110.00 USD | 0.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `156.04` | 1,550.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD | 0.00 USD | 1,280.00 USD |
| `7D` | `156.09` | 43,600.00 USD | 0.00 USD | 43,600.00 USD | 0.00 USD | 0.00 USD | 21,560.00 USD |
| `1D` | `156.20` | 263.55 USD | 0.00 USD | 263.55 USD | 0.00 USD | 0.00 USD | 259.62 USD |
| `7D` | `156.25` | 22,040.00 USD | 0.00 USD | 22,040.00 USD | 0.00 USD | 0.00 USD | 11,100.00 USD |
| `1D` | `156.36` | 3.93 USD | 0.00 USD | 3.93 USD | 0.00 USD | 0.00 USD | 3.93 USD |
| `7D` | `156.41` | 10,940.00 USD | 0.00 USD | 10,940.00 USD | 0.00 USD | 0.00 USD | 10,940.00 USD |
| `1D` | `157.56` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `157.56` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `158.17` | 39.84 USD | 39.84 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39.84 USD |
| `7D` | `158.33` | 2,190.00 USD | 2,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,150.00 USD |
| `7D` | `158.49` | 2,730.00 USD | 2,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 539.54 USD |
| `7D` | `158.65` | 2,850.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 127.17 USD |
| `7D` | `158.81` | 3,070.00 USD | 3,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 220.39 USD |
| `1D` | `158.92` | 72.36 USD | 72.36 USD | 0.00 USD | 0.00 USD | 0.00 USD | 72.36 USD |
| `7D` | `158.97` | 4,160.00 USD | 4,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD |
| `1D` | `159.08` | 467.67 USD | 467.67 USD | 0.00 USD | 0.00 USD | 0.00 USD | 395.31 USD |
| `7D` | `159.13` | 12,550.00 USD | 12,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,390.00 USD |
| `1D` | `159.24` | 1,920.00 USD | 1,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,450.00 USD |
| `7D` | `159.29` | 27,600.00 USD | 27,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,050.00 USD |
| `1D` | `159.40` | 1,920.00 USD | 1,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.93 USD |
| `7D` | `159.45` | 37,700.00 USD | 37,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,100.00 USD |
| `7D` | `159.61` | 48,630.00 USD | 48,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,940.00 USD |
| `7D` | `159.77` | 48,830.00 USD | 48,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 199.19 USD |
| `7D` | `159.93` | 49,730.00 USD | 49,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 896.05 USD |
| `7D` | `160.09` | 50,030.00 USD | 50,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 304.23 USD |
| `7D` | `160.25` | 50,060.00 USD | 50,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `7D` | `160.41` | 50,170.00 USD | 50,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 110.19 USD |
| `1D` | `160.52` | 1,960.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 36.17 USD |
| `7D` | `160.57` | 50,840.00 USD | 50,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 668.20 USD |
| `1D` | `160.68` | 2,400.00 USD | 2,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 440.70 USD |
| `7D` | `160.73` | 57,680.00 USD | 57,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,840.00 USD |
| `1D` | `160.84` | 2,880.00 USD | 2,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 482.13 USD |
| `7D` | `160.89` | 65,380.00 USD | 65,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,700.00 USD |
| `1D` | `161.00` | 2,880.00 USD | 2,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1.96 USD |
| `7D` | `161.05` | 68,540.00 USD | 68,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,160.00 USD |
| `7D` | `161.21` | 72,950.00 USD | 72,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,410.00 USD |
| `7D` | `162.97` | 73,370.00 USD | 73,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 420.80 USD |
| `7D` | `163.13` | 73,510.00 USD | 73,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 141.18 USD |
| `7D` | `163.29` | 73,650.00 USD | 73,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 137.75 USD |
| `7D` | `163.45` | 73,660.00 USD | 73,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `7D` | `163.61` | 73,720.00 USD | 73,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 55.10 USD |
| `1D` | `163.72` | 2,910.00 USD | 2,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.41 USD |
| `7D` | `163.77` | 74,150.00 USD | 74,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 430.40 USD |
| `1D` | `163.88` | 3,270.00 USD | 3,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 361.71 USD |
| `7D` | `163.93` | 77,820.00 USD | 77,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,670.00 USD |
| `1D` | `164.04` | 3,360.00 USD | 3,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 91.40 USD |
| `7D` | `164.09` | 82,380.00 USD | 82,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,560.00 USD |
| `1D` | `164.20` | 3,360.00 USD | 3,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.98 USD |
| `7D` | `164.25` | 85,110.00 USD | 85,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD |
| `7D` | `172.41` | 85,330.00 USD | 85,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 216.18 USD |
| `7D` | `172.57` | 85,380.00 USD | 85,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 54.42 USD |
| `7D` | `172.73` | 85,390.00 USD | 85,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7.36 USD |
| `7D` | `172.89` | 85,390.00 USD | 85,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.35 USD |
| `7D` | `173.05` | 85,420.00 USD | 85,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22.04 USD |
| `1D` | `173.16` | 3,370.00 USD | 3,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10.56 USD |
| `7D` | `173.21` | 85,570.00 USD | 85,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 157.33 USD |
| `1D` | `173.31` | 3,460.00 USD | 3,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 84.58 USD |
| `7D` | `173.37` | 87,020.00 USD | 87,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,440.00 USD |
| `7D` | `173.53` | 88,770.00 USD | 88,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,760.00 USD |

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
  * Current Rate: `-101.20` | Last 24h: `-640.25` | Last 3d: `-882.53` | Last 7d: `-882.53`
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
| `17:45:00` | `157.82` | `157.82` | `157.82` | `157.88` | `157.81` | 105,423.09 USD | 8,303.87 USD | 97,119.22 USD | -88,815.34 USD | `-84.25%` | `0B / 1S` |
| `17:50:00` | `157.83` | `157.83` | `157.83` | `157.86` | `157.81` | 99,905.76 USD | 46,035.01 USD | 53,870.75 USD | -7,835.75 USD | `-7.84%` | `0B / 1S` |
| `17:55:00` | `157.86` | `157.86` | `157.86` | `157.88` | `157.82` | 95,187.77 USD | 65,929.23 USD | 29,258.54 USD | 36,670.70 USD | `+38.52%` | `1B / 0S` |
| `18:00:00` | `157.82` | `157.82` | `157.82` | `157.91` | `157.77` | 1,106,791.66 USD | 392,666.89 USD | 714,124.77 USD | -321,457.87 USD | `-29.04%` | `0B / 1S` |
| `18:00:00` | `157.83` | `157.83` | `157.83` | `157.90` | `157.82` | 277,626.49 USD | 73,395.51 USD | 204,230.98 USD | -130,835.47 USD | `-47.13%` | `0B / 1S` |
| `18:00:00` | `157.87` | `157.87` | `157.87` | `157.90` | `157.85` | 105,774.91 USD | 57,214.61 USD | 48,560.30 USD | 8,654.31 USD | `+8.18%` | `1B / 0S` |
| `18:05:00` | `157.83` | `157.83` | `157.83` | `157.88` | `157.82` | 104,480.81 USD | 10,539.73 USD | 93,941.08 USD | -83,401.35 USD | `-79.82%` | `0B / 1S` |
| `18:10:00` | `157.83` | `157.83` | `157.83` | `157.85` | `157.82` | 67,394.26 USD | 38,345.01 USD | 29,049.25 USD | 9,295.76 USD | `+13.79%` | `1B / 0S` |
| `18:15:00` | `157.85` | `157.85` | `157.85` | `157.86` | `157.80` | 71,507.86 USD | 56,144.84 USD | 15,363.02 USD | 40,781.83 USD | `+57.03%` | `1B / 0S` |
| `18:15:00` | `157.81` | `157.81` | `157.81` | `157.91` | `157.80` | 269,059.23 USD | 63,097.96 USD | 205,961.27 USD | -142,863.31 USD | `-53.10%` | `0B / 1S` |

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
  * `2026-10-29 23:31:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:51:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:51:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:52:26 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:52:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `157.75` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `157.64` (Risk Distance: `0.1099` pts)
  * +2.5R Take Profit: `158.03`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.11 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `157.97` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `158.08` (Risk Distance: `0.1099` pts)
  * +2.5R Take Profit: `157.70`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.11 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`159.14`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
