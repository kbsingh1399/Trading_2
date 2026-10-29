# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USDJPY
**Canonical Key**: `USDJPY` | **Broker Instrument**: `USDJPY.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-29 22:45:59 IST` (`2026-10-29 17:15:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `157.88` | VWAP Z-Score: `+0.08` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1007` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `49.55` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `158.17` | Lower -3.00σ Band: `157.58`
  * Upper +2.51σ Band: `158.12` | Lower -2.51σ Band: `157.63`
  * Upper +2.01σ Band: `158.07` | Lower -2.01σ Band: `157.68`
  * Upper +2.00σ Band: `158.07` | Lower -2.00σ Band: `157.68`
  * Upper +1.28σ Band: `158.00` | Lower -1.28σ Band: `157.75`
  * Upper +1.00σ Band: `157.97` | Lower -1.00σ Band: `157.78`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`157.86` | EMA-20=`157.88` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`157.89` (Slope: `+0.0000`) | EMA-100=`157.89`
  * Institutional Anchors: EMA-144=`157.88` | EMA-200=`157.85` (Slope: `-0.0000`) | EMA-233=`157.83`
- **Range Boundaries**: 24H High=`158.35` | 24H Low=`157.60` | Weekly High=`158.35` | Weekly Low=`157.35`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `157.97` (Distance: `-0.03%`)
  * Point of Control (POC) = `157.87` (Distance: `+0.03%`)
  * Value Area Low (VAL) = `157.75` (Distance: `+0.11%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`158.04` | POC=`157.89` | VAL=`157.79`
  * Prior Day Extremes: PDH=`158.35` | PDL=`157.65` | PDC=`157.82`
  * Monday Range Blueprint: High=`157.64` | Mid=`157.15` | Low=`156.65`
  * Developing Weekly Value Area: Weekly VAH=`158.08` | Weekly POC=`157.87` | Weekly VAL=`157.46`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`158.07` | Low=`157.60`
  * London Session (08:00-16:00 UTC): High=`158.08` | Low=`157.77`
  * New York Session (13:00-21:00 UTC): High=`158.13` | Low=`157.71`
  * Initial Balance (First Hour): IB High=`157.91` | IB Low=`157.80`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `157.28` - `158.54`
  * Optimal Trade Entry (OTE 0.705): `158.22`
  * Structural Invalidation Anchor (0.786): `159.17`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `157.83` | `157.89` | `157.81` | `157.87` | `1,232` | 194,497.07 USD | 108,615.25 USD | `+55.84%` | -263,574.16 USD | `+0.92` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `157.87` | `157.92` | `157.85` | `157.90` | `1,340` | 211,584.66 USD | 74,759.91 USD | `+35.33%` | -188,814.25 USD | `+0.57` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `157.90` | `157.94` | `157.88` | `157.91` | `1,200` | 189,495.60 USD | 46,570.95 USD | `+24.58%` | -142,243.29 USD | `+0.29` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `158.06` | `158.06` | `157.71` | `157.84` | `5,169` | 815,895.64 USD | -351,679.15 USD | `-43.10%` | -943,972.41 USD | `-2.53` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `157.84` | `157.86` | `157.73` | `157.83` | `4,050` | 639,211.50 USD | 152,427.36 USD | `+23.85%` | -791,545.05 USD | `+1.02` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `157.83` | `157.94` | `157.81` | `157.91` | `3,772` | 595,647.84 USD | 390,744.98 USD | `+65.60%` | -400,800.07 USD | `+2.29` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `158.02` | `158.08` | `157.90` | `158.06` | `7,808` | 1,234,155.90 USD | 685,642.17 USD | `+55.56%` | -395,515.57 USD | `+1.39` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `158.06` | `158.13` | `157.71` | `157.83` | `14,919` | 2,354,665.77 USD | -1,168,822.04 USD | `-49.64%` | -1,564,337.61 USD | `-1.91` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `157.83` | `158.01` | `157.81` | `157.86` | `11,030` | 1,741,162.71 USD | -351,663.40 USD | `-20.20%` | -1,916,001.02 USD | `-0.53` | **`BEARISH`** | `BEARISH ABSORPTION` |
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
| `220` | `0x0911...129a` | `SHORT` | 10,453,994.35 USD | `66,223.20` | `156.58` | `157.86` | `167.73` | -84,974.12 USD | `-0.81%` | `20X Isolated` |
| `1156` | `0xec0b...b078` | `SHORT` | 1,991,796.97 USD | `12,617.49` | `158.22` | `157.86` | `162.95` | 4,568.70 USD | `+0.23%` | `20X Isolated` |
| `1174` | `0xc966...f6b6` | `SHORT` | 1,980,127.10 USD | `12,542.77` | `157.61` | `157.86` | `195.70` | -3,318.03 USD | `-0.17%` | `5X Isolated` |
| `1254` | `0xbef1...d2e5` | `LONG` | 1,866,108.84 USD | `11,821.29` | `157.63` | `157.86` | `155.51` | 2,748.23 USD | `+0.15%` | `50X Isolated` |
| `1553` | `0x9dea...d617` | `LONG` | 1,467,490.24 USD | `9,296.15` | `157.69` | `157.86` | `146.11` | 1,573.36 USD | `+0.11%` | `50X Isolated` |
| `1933` | `0x3d89...eb14` | `LONG` | 1,089,234.00 USD | `6,900.00` | `158.17` | `157.86` | `127.36` | -2,155.60 USD | `-0.20%` | `5X Isolated` |

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
| `1D` | `141.94` | 3,720.00 USD | 0.00 USD | 3,720.00 USD | 0.00 USD | 0.00 USD | 123.78 USD |
| `7D` | `141.94` | 3,720.00 USD | 0.00 USD | 3,720.00 USD | 0.00 USD | 0.00 USD | 127.32 USD |
| `1D` | `142.10` | 3,590.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | 0.00 USD | 1.91 USD |
| `7D` | `142.10` | 3,590.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | 0.00 USD | 1.91 USD |
| `1D` | `142.26` | 3,590.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | 0.00 USD | 10.96 USD |
| `7D` | `142.26` | 3,590.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | 0.00 USD | 10.96 USD |
| `1D` | `151.22` | 3,580.00 USD | 0.00 USD | 3,580.00 USD | 0.00 USD | 0.00 USD | 147.37 USD |
| `7D` | `151.22` | 3,580.00 USD | 0.00 USD | 3,580.00 USD | 0.00 USD | 0.00 USD | 138.54 USD |
| `1D` | `151.38` | 3,430.00 USD | 0.00 USD | 3,430.00 USD | 0.00 USD | 0.00 USD | 329.66 USD |
| `7D` | `151.38` | 3,440.00 USD | 0.00 USD | 3,440.00 USD | 0.00 USD | 0.00 USD | 338.51 USD |
| `1D` | `151.54` | 3,100.00 USD | 0.00 USD | 3,100.00 USD | 0.00 USD | 0.00 USD | 7.23 USD |
| `7D` | `151.54` | 3,100.00 USD | 0.00 USD | 3,100.00 USD | 0.00 USD | 0.00 USD | 7.23 USD |
| `1D` | `151.70` | 3,100.00 USD | 0.00 USD | 3,100.00 USD | 0.00 USD | 0.00 USD | 27.40 USD |
| `7D` | `151.70` | 3,100.00 USD | 0.00 USD | 3,100.00 USD | 0.00 USD | 0.00 USD | 27.40 USD |
| `1D` | `154.42` | 3,070.00 USD | 0.00 USD | 3,070.00 USD | 0.00 USD | 0.00 USD | 770.30 USD |
| `7D` | `154.42` | 3,070.00 USD | 0.00 USD | 3,070.00 USD | 0.00 USD | 0.00 USD | 770.31 USD |
| `1D` | `154.58` | 2,300.00 USD | 0.00 USD | 2,300.00 USD | 0.00 USD | 0.00 USD | 188.74 USD |
| `7D` | `154.58` | 2,300.00 USD | 0.00 USD | 2,300.00 USD | 0.00 USD | 0.00 USD | 188.75 USD |
| `1D` | `154.74` | 2,110.00 USD | 0.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD | 64.37 USD |
| `7D` | `154.74` | 2,110.00 USD | 0.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD | 64.37 USD |
| `1D` | `155.86` | 2,050.00 USD | 0.00 USD | 2,050.00 USD | 0.00 USD | 0.00 USD | 187.01 USD |
| `7D` | `155.86` | 2,050.00 USD | 0.00 USD | 2,050.00 USD | 0.00 USD | 0.00 USD | 153.76 USD |
| `1D` | `156.02` | 1,860.00 USD | 0.00 USD | 1,860.00 USD | 0.00 USD | 0.00 USD | 1,360.00 USD |
| `7D` | `156.02` | 1,890.00 USD | 0.00 USD | 1,890.00 USD | 0.00 USD | 0.00 USD | 1,400.00 USD |
| `1D` | `156.18` | 495.96 USD | 0.00 USD | 495.96 USD | 0.00 USD | 0.00 USD | 367.22 USD |
| `7D` | `156.18` | 495.96 USD | 0.00 USD | 495.96 USD | 0.00 USD | 0.00 USD | 367.22 USD |
| `1D` | `156.34` | 128.74 USD | 0.00 USD | 128.74 USD | 0.00 USD | 0.00 USD | 128.74 USD |
| `7D` | `156.34` | 128.74 USD | 0.00 USD | 128.74 USD | 0.00 USD | 0.00 USD | 128.74 USD |
| `1D` | `157.56` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `157.56` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `159.06` | 475.50 USD | 475.50 USD | 0.00 USD | 0.00 USD | 0.00 USD | 475.50 USD |
| `7D` | `159.06` | 459.12 USD | 459.12 USD | 0.00 USD | 0.00 USD | 0.00 USD | 459.12 USD |
| `1D` | `159.22` | 1,670.00 USD | 1,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,200.00 USD |
| `7D` | `159.22` | 1,670.00 USD | 1,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,210.00 USD |
| `1D` | `159.38` | 1,920.00 USD | 1,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 249.06 USD |
| `7D` | `159.38` | 1,920.00 USD | 1,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 249.06 USD |
| `1D` | `159.54` | 2,050.00 USD | 2,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 124.81 USD |
| `7D` | `159.54` | 2,050.00 USD | 2,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 124.81 USD |
| `1D` | `160.66` | 2,340.00 USD | 2,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 294.79 USD |
| `7D` | `160.66` | 2,320.00 USD | 2,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 277.11 USD |
| `1D` | `160.82` | 3,000.00 USD | 3,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 659.35 USD |
| `7D` | `160.82` | 3,000.00 USD | 3,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 677.05 USD |
| `1D` | `160.98` | 3,010.00 USD | 3,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6.86 USD |
| `7D` | `160.98` | 3,010.00 USD | 3,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6.86 USD |
| `1D` | `161.14` | 3,070.00 USD | 3,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 62.41 USD |
| `7D` | `161.14` | 3,070.00 USD | 3,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 62.41 USD |
| `1D` | `163.86` | 3,420.00 USD | 3,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 351.17 USD |
| `7D` | `163.86` | 3,420.00 USD | 3,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 351.19 USD |
| `1D` | `164.02` | 3,550.00 USD | 3,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 128.31 USD |
| `7D` | `164.02` | 3,550.00 USD | 3,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 128.31 USD |
| `1D` | `164.18` | 3,550.00 USD | 3,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4.78 USD |
| `7D` | `164.18` | 3,550.00 USD | 3,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4.78 USD |
| `1D` | `164.34` | 3,580.00 USD | 3,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 27.40 USD |
| `7D` | `164.34` | 3,580.00 USD | 3,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 27.40 USD |
| `1D` | `173.30` | 3,690.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 112.23 USD |
| `7D` | `173.30` | 3,700.00 USD | 3,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 121.32 USD |
| `1D` | `173.46` | 3,760.00 USD | 3,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 62.64 USD |
| `7D` | `173.46` | 3,760.00 USD | 3,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 53.56 USD |
| `1D` | `173.53` | 3,760.00 USD | 3,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.98 USD |
| `7D` | `173.53` | 3,760.00 USD | 3,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.98 USD |

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
  * Current Rate: `-106.38` | Last 24h: `-640.25` | Last 3d: `-882.53` | Last 7d: `-882.53`
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
| `16:30:00` | `157.79` | `157.79` | `157.79` | `158.06` | `157.79` | 237,792.54 USD | 11,889.63 USD | 225,902.92 USD | -214,013.29 USD | `-90.00%` | `0B / 1S` |
| `16:35:00` | `157.73` | `157.73` | `157.73` | `157.84` | `157.71` | 358,360.29 USD | 69,604.59 USD | 288,755.69 USD | -219,151.10 USD | `-61.15%` | `0B / 1S` |
| `16:40:00` | `157.84` | `157.84` | `157.84` | `157.86` | `157.73` | 219,403.16 USD | 200,561.29 USD | 18,841.87 USD | 181,719.41 USD | `+82.82%` | `1B / 0S` |
| `16:45:00` | `157.75` | `157.75` | `157.75` | `157.85` | `157.74` | 229,838.84 USD | 21,223.86 USD | 208,614.98 USD | -187,391.12 USD | `-81.53%` | `0B / 1S` |
| `16:45:00` | `157.83` | `157.83` | `157.83` | `157.86` | `157.73` | 639,211.50 USD | 395,819.43 USD | 243,392.07 USD | 152,427.36 USD | `+23.85%` | `1B / 0S` |
| `16:50:00` | `157.80` | `157.80` | `157.80` | `157.81` | `157.73` | 231,808.20 USD | 192,946.24 USD | 38,861.96 USD | 154,084.27 USD | `+66.47%` | `1B / 0S` |
| `16:55:00` | `157.83` | `157.83` | `157.83` | `157.86` | `157.76` | 177,400.92 USD | 122,406.63 USD | 54,994.29 USD | 67,412.35 USD | `+38.00%` | `1B / 0S` |
| `17:00:00` | `157.87` | `157.87` | `157.87` | `157.89` | `157.81` | 194,497.07 USD | 151,556.16 USD | 42,940.91 USD | 108,615.25 USD | `+55.84%` | `1B / 0S` |
| `17:00:00` | `157.86` | `157.86` | `157.86` | `158.01` | `157.81` | 1,741,162.71 USD | 694,749.65 USD | 1,046,413.06 USD | -351,663.40 USD | `-20.20%` | `0B / 1S` |
| `17:00:00` | `157.91` | `157.91` | `157.91` | `157.94` | `157.81` | 595,647.84 USD | 493,196.41 USD | 102,451.43 USD | 390,744.98 USD | `+65.60%` | `1B / 0S` |

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
  * `2026-10-29 22:05:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [bea.gov] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `157.62` (Risk Distance: `0.1223` pts)
  * +2.5R Take Profit: `158.05`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.12 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `157.97` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `158.09` (Risk Distance: `0.1223` pts)
  * +2.5R Take Profit: `157.67`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.12 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`159.17`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
