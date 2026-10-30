# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USDJPY
**Canonical Key**: `USDJPY` | **Broker Instrument**: `USDJPY.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 16:33:46 IST` (`2026-10-30 11:03:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `157.17` | **Live Ask Quote**: `157.17` | **Mid Price**: `157.17`
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
  * Session VWAP: `157.44` | VWAP Z-Score: `-1.67` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1348` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `40.46` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `157.85` | Lower -3.00σ Band: `157.02`
  * Upper +2.51σ Band: `157.78` | Lower -2.51σ Band: `157.09`
  * Upper +2.01σ Band: `157.71` | Lower -2.01σ Band: `157.16`
  * Upper +2.00σ Band: `157.71` | Lower -2.00σ Band: `157.16`
  * Upper +1.28σ Band: `157.61` | Lower -1.28σ Band: `157.26`
  * Upper +1.00σ Band: `157.57` | Lower -1.00σ Band: `157.30`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`157.31` | EMA-20=`157.37` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`157.48` (Slope: `+0.0000`) | EMA-100=`157.60`
  * Institutional Anchors: EMA-144=`157.66` | EMA-200=`157.71` (Slope: `-0.0332`) | EMA-233=`157.73`
- **Range Boundaries**: 24H High=`158.13` | 24H Low=`157.12` | Weekly High=`158.35` | Weekly Low=`157.12`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `157.60` (Distance: `-0.27%`)
  * Point of Control (POC) = `157.34` (Distance: `-0.11%`)
  * Value Area Low (VAL) = `157.24` (Distance: `-0.04%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`157.99` | POC=`157.87` | VAL=`157.76`
  * Prior Day Extremes: PDH=`158.13` | PDL=`157.60` | PDC=`157.69`
  * Monday Range Blueprint: High=`157.64` | Mid=`157.15` | Low=`156.65`
  * Developing Weekly Value Area: Weekly VAH=`158.03` | Weekly POC=`157.87` | Weekly VAL=`157.39`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`157.90` | Low=`157.12`
  * London Session (08:00-16:00 UTC): High=`157.75` | Low=`157.15`
  * New York Session (13:00-21:00 UTC): High=`157.36` | Low=`157.15`
  * Initial Balance (First Hour): IB High=`157.70` | IB Low=`157.40`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `156.54` - `157.80`
  * Optimal Trade Entry (OTE 0.705): `157.49`
  * Structural Invalidation Anchor (0.786): `158.43`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `157.54` | `157.65` | `157.54` | `157.64` | `522` | 82,285.99 USD | 61,017.16 USD | `+74.15%` | 754,907.59 USD | `+1.25` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `157.63` | `157.67` | `157.61` | `157.63` | `599` | 94,417.97 USD | -30,644.43 USD | `-32.46%` | 724,263.16 USD | `-0.78` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `157.62` | `157.63` | `157.57` | `157.60` | `534` | 84,160.54 USD | -13,358.82 USD | `-15.87%` | 710,904.35 USD | `-0.38` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `157.45` | `157.65` | `157.44` | `157.64` | `1,473` | 232,197.83 USD | 196,558.16 USD | `+84.65%` | -27,377.95 USD | `+0.93` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `157.63` | `157.67` | `157.55` | `157.55` | `1,786` | 281,384.30 USD | -233,711.75 USD | `-83.06%` | -261,089.70 USD | `-1.20` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `157.55` | `157.58` | `157.41` | `157.43` | `2,459` | 387,108.08 USD | -313,373.20 USD | `-80.95%` | -574,462.90 USD | `-1.81` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `157.62` | `157.71` | `157.47` | `157.67` | `8,064` | 1,271,458.94 USD | 557,244.35 USD | `+43.83%` | 2,784,643.74 USD | `+0.73` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `157.67` | `157.75` | `157.44` | `157.55` | `6,987` | 1,100,801.85 USD | -368,732.65 USD | `-33.50%` | 2,415,911.09 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `157.55` | `157.58` | `157.16` | `157.28` | `9,162` | 1,441,036.01 USD | -770,625.97 USD | `-53.48%` | 1,645,285.12 USD | `-1.15` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.64` | `157.90` | `157.31` | `157.36` | `20,459` | 3,219,366.86 USD | -2,125,220.88 USD | `-66.01%` | -2,765,043.25 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.36` | `157.63` | `157.12` | `157.43` | `39,720` | 6,253,000.44 USD | 1,103,833.41 USD | `+17.65%` | -1,661,209.84 USD | `+0.69` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `157.43` | `157.75` | `157.16` | `157.28` | `32,041` | 5,039,536.64 USD | -2,107,047.65 USD | `-41.81%` | -3,768,257.49 USD | `-0.73` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `158.06` | `158.13` | `157.71` | `157.88` | `37,561` | 5,930,280.92 USD | -1,786,229.19 USD | `-30.12%` | 1,308,304.60 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.88` | `157.98` | `157.63` | `157.69` | `20,300` | 3,201,147.60 USD | -1,948,126.97 USD | `-60.86%` | -639,822.37 USD | `-0.74` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.64` | `157.90` | `157.31` | `157.36` | `20,459` | 3,219,366.86 USD | -2,125,220.88 USD | `-66.01%` | -2,765,043.25 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.36` | `157.63` | `157.12` | `157.43` | `39,720` | 6,253,000.44 USD | 1,103,833.41 USD | `+17.65%` | -1,661,209.84 USD | `+0.69` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `157.43` | `157.75` | `157.16` | `157.28` | `32,041` | 5,039,536.64 USD | -2,107,047.65 USD | `-41.81%` | -3,768,257.49 USD | `-0.73` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `201` | `0x0911...129a` | `SHORT` | 10,413,598.20 USD | `66,223.20` | `156.58` | `157.24` | `167.71` | -44,577.97 USD | `-0.43%` | `20X Isolated` |
| `1012` | `0x9dea...d617` | `LONG` | 2,133,271.94 USD | `13,566.98` | `157.66` | `157.24` | `149.21` | -5,741.81 USD | `-0.27%` | `50X Isolated` |
| `1093` | `0xec0b...b078` | `SHORT` | 1,983,974.13 USD | `12,617.49` | `158.22` | `157.24` | `162.94` | 12,391.55 USD | `+0.62%` | `20X Isolated` |
| `1148` | `0xc966...f6b6` | `SHORT` | 1,909,318.15 USD | `12,142.70` | `157.61` | `157.24` | `215.26` | 4,437.70 USD | `+0.23%` | `5X Isolated` |
| `1177` | `0xbef1...d2e5` | `LONG` | 1,858,897.85 USD | `11,821.29` | `157.63` | `157.24` | `155.50` | -4,462.76 USD | `-0.24%` | `50X Isolated` |
| `1876` | `0x3d89...eb14` | `LONG` | 1,084,956.00 USD | `6,900.00` | `158.17` | `157.24` | `127.34` | -6,433.60 USD | `-0.59%` | `5X Isolated` |

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
| `7D` | `141.51` | 90,340.00 USD | 0.00 USD | 90,340.00 USD | 0.00 USD | 0.00 USD | 5.35 USD |
| `1D` | `141.54` | 5,640.00 USD | 0.00 USD | 5,640.00 USD | 0.00 USD | 0.00 USD | 126.49 USD |
| `7D` | `141.67` | 90,340.00 USD | 0.00 USD | 90,340.00 USD | 0.00 USD | 0.00 USD | 161.17 USD |
| `1D` | `141.70` | 5,520.00 USD | 0.00 USD | 5,520.00 USD | 0.00 USD | 0.00 USD | 66.27 USD |
| `7D` | `141.83` | 90,170.00 USD | 0.00 USD | 90,170.00 USD | 0.00 USD | 0.00 USD | 1,360.00 USD |
| `1D` | `141.86` | 5,450.00 USD | 0.00 USD | 5,450.00 USD | 0.00 USD | 0.00 USD | 96.69 USD |
| `7D` | `141.99` | 88,810.00 USD | 0.00 USD | 88,810.00 USD | 0.00 USD | 0.00 USD | 1,890.00 USD |
| `1D` | `142.02` | 5,350.00 USD | 0.00 USD | 5,350.00 USD | 0.00 USD | 0.00 USD | 7.98 USD |
| `7D` | `142.15` | 86,920.00 USD | 0.00 USD | 86,920.00 USD | 0.00 USD | 0.00 USD | 882.31 USD |
| `7D` | `150.47` | 86,040.00 USD | 0.00 USD | 86,040.00 USD | 0.00 USD | 0.00 USD | 544.08 USD |
| `7D` | `150.63` | 85,490.00 USD | 0.00 USD | 85,490.00 USD | 0.00 USD | 0.00 USD | 122.88 USD |
| `7D` | `150.79` | 85,370.00 USD | 0.00 USD | 85,370.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `7D` | `150.95` | 85,360.00 USD | 0.00 USD | 85,360.00 USD | 0.00 USD | 0.00 USD | 55.10 USD |
| `1D` | `150.98` | 5,340.00 USD | 0.00 USD | 5,340.00 USD | 0.00 USD | 0.00 USD | 316.23 USD |
| `7D` | `151.11` | 85,300.00 USD | 0.00 USD | 85,300.00 USD | 0.00 USD | 0.00 USD | 347.81 USD |
| `1D` | `151.14` | 5,030.00 USD | 0.00 USD | 5,030.00 USD | 0.00 USD | 0.00 USD | 172.15 USD |
| `7D` | `151.27` | 84,950.00 USD | 0.00 USD | 84,950.00 USD | 0.00 USD | 0.00 USD | 2,790.00 USD |
| `1D` | `151.30` | 4,860.00 USD | 0.00 USD | 4,860.00 USD | 0.00 USD | 0.00 USD | 253.57 USD |
| `7D` | `151.43` | 82,160.00 USD | 0.00 USD | 82,160.00 USD | 0.00 USD | 0.00 USD | 4,630.00 USD |
| `1D` | `151.46` | 4,600.00 USD | 0.00 USD | 4,600.00 USD | 0.00 USD | 0.00 USD | 21.57 USD |
| `7D` | `151.59` | 77,530.00 USD | 0.00 USD | 77,530.00 USD | 0.00 USD | 0.00 USD | 3,790.00 USD |
| `7D` | `153.51` | 73,740.00 USD | 0.00 USD | 73,740.00 USD | 0.00 USD | 0.00 USD | 199.19 USD |
| `7D` | `153.67` | 73,550.00 USD | 0.00 USD | 73,550.00 USD | 0.00 USD | 0.00 USD | 896.05 USD |
| `7D` | `153.83` | 72,650.00 USD | 0.00 USD | 72,650.00 USD | 0.00 USD | 0.00 USD | 238.69 USD |
| `7D` | `153.99` | 72,410.00 USD | 0.00 USD | 72,410.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `1D` | `154.02` | 4,580.00 USD | 0.00 USD | 4,580.00 USD | 0.00 USD | 0.00 USD | 33.56 USD |
| `7D` | `154.15` | 72,380.00 USD | 0.00 USD | 72,380.00 USD | 0.00 USD | 0.00 USD | 110.19 USD |
| `1D` | `154.18` | 4,550.00 USD | 0.00 USD | 4,550.00 USD | 0.00 USD | 0.00 USD | 651.29 USD |
| `7D` | `154.31` | 72,270.00 USD | 0.00 USD | 72,270.00 USD | 0.00 USD | 0.00 USD | 997.59 USD |
| `1D` | `154.34` | 3,900.00 USD | 0.00 USD | 3,900.00 USD | 0.00 USD | 0.00 USD | 390.14 USD |
| `7D` | `154.47` | 71,280.00 USD | 0.00 USD | 71,280.00 USD | 0.00 USD | 0.00 USD | 7,530.00 USD |
| `1D` | `154.50` | 3,510.00 USD | 0.00 USD | 3,510.00 USD | 0.00 USD | 0.00 USD | 420.07 USD |
| `7D` | `154.63` | 63,750.00 USD | 0.00 USD | 63,750.00 USD | 0.00 USD | 0.00 USD | 9,120.00 USD |
| `1D` | `154.66` | 3,090.00 USD | 0.00 USD | 3,090.00 USD | 0.00 USD | 0.00 USD | 32.03 USD |
| `7D` | `154.79` | 54,630.00 USD | 0.00 USD | 54,630.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD |
| `7D` | `155.11` | 49,160.00 USD | 0.00 USD | 49,160.00 USD | 0.00 USD | 0.00 USD | 954.59 USD |
| `7D` | `155.27` | 48,210.00 USD | 0.00 USD | 48,210.00 USD | 0.00 USD | 0.00 USD | 1,240.00 USD |
| `7D` | `155.43` | 46,970.00 USD | 0.00 USD | 46,970.00 USD | 0.00 USD | 0.00 USD | 477.37 USD |
| `7D` | `155.59` | 46,500.00 USD | 0.00 USD | 46,500.00 USD | 0.00 USD | 0.00 USD | 53.53 USD |
| `1D` | `155.62` | 3,050.00 USD | 0.00 USD | 3,050.00 USD | 0.00 USD | 0.00 USD | 79.53 USD |
| `7D` | `155.75` | 46,440.00 USD | 0.00 USD | 46,440.00 USD | 0.00 USD | 0.00 USD | 529.27 USD |
| `1D` | `155.78` | 2,970.00 USD | 0.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD | 1,290.00 USD |
| `7D` | `155.91` | 45,910.00 USD | 0.00 USD | 45,910.00 USD | 0.00 USD | 0.00 USD | 1,930.00 USD |
| `1D` | `155.94` | 1,680.00 USD | 0.00 USD | 1,680.00 USD | 0.00 USD | 0.00 USD | 920.75 USD |
| `7D` | `156.07` | 43,980.00 USD | 0.00 USD | 43,980.00 USD | 0.00 USD | 0.00 USD | 21,700.00 USD |
| `1D` | `156.10` | 763.75 USD | 0.00 USD | 763.75 USD | 0.00 USD | 0.00 USD | 729.83 USD |
| `7D` | `156.23` | 22,280.00 USD | 0.00 USD | 22,280.00 USD | 0.00 USD | 0.00 USD | 11,350.00 USD |
| `1D` | `156.26` | 33.92 USD | 0.00 USD | 33.92 USD | 0.00 USD | 0.00 USD | 33.92 USD |
| `7D` | `156.39` | 10,940.00 USD | 0.00 USD | 10,940.00 USD | 0.00 USD | 0.00 USD | 10,940.00 USD |
| `1D` | `157.13` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `157.13` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `158.31` | 2,180.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,180.00 USD |
| `7D` | `158.47` | 2,670.00 USD | 2,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 491.52 USD |
| `7D` | `158.63` | 2,720.00 USD | 2,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 53.53 USD |
| `1D` | `158.82` | 1,260.00 USD | 1,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,260.00 USD |
| `7D` | `158.95` | 4,330.00 USD | 4,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,610.00 USD |
| `1D` | `158.98` | 1,900.00 USD | 1,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 638.15 USD |
| `7D` | `159.11` | 7,790.00 USD | 7,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,460.00 USD |
| `1D` | `159.14` | 2,350.00 USD | 2,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 448.42 USD |
| `7D` | `159.27` | 27,930.00 USD | 27,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,140.00 USD |
| `1D` | `159.30` | 3,050.00 USD | 3,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 702.69 USD |
| `7D` | `159.43` | 38,230.00 USD | 38,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,290.00 USD |
| `7D` | `159.59` | 49,160.00 USD | 49,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,940.00 USD |
| `7D` | `159.75` | 49,280.00 USD | 49,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 116.22 USD |
| `7D` | `159.91` | 50,260.00 USD | 50,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 979.02 USD |
| `7D` | `160.07` | 50,500.00 USD | 50,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 238.69 USD |
| `7D` | `160.23` | 50,520.00 USD | 50,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `1D` | `160.26` | 3,090.00 USD | 3,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33.56 USD |
| `7D` | `160.39` | 50,630.00 USD | 50,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 110.19 USD |
| `1D` | `160.42` | 3,690.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 598.91 USD |
| `7D` | `160.55` | 51,330.00 USD | 51,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 695.63 USD |
| `1D` | `160.58` | 4,020.00 USD | 4,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 335.65 USD |
| `7D` | `160.71` | 56,790.00 USD | 56,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,460.00 USD |
| `1D` | `160.74` | 4,530.00 USD | 4,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 509.49 USD |
| `7D` | `160.87` | 66,170.00 USD | 66,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,390.00 USD |
| `1D` | `160.90` | 4,580.00 USD | 4,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 49.48 USD |
| `7D` | `161.03` | 68,280.00 USD | 68,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,110.00 USD |
| `7D` | `161.19` | 73,740.00 USD | 73,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD |
| `7D` | `162.95` | 73,980.00 USD | 73,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 238.64 USD |
| `7D` | `163.11` | 74,290.00 USD | 74,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 308.98 USD |
| `7D` | `163.27` | 74,410.00 USD | 74,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 119.34 USD |
| `7D` | `163.43` | 74,420.00 USD | 74,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `1D` | `163.46` | 4,600.00 USD | 4,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19.11 USD |
| `7D` | `163.59` | 74,480.00 USD | 74,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 55.10 USD |
| `1D` | `163.62` | 4,920.00 USD | 4,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 323.31 USD |
| `7D` | `163.75` | 74,980.00 USD | 74,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 498.79 USD |
| `1D` | `163.78` | 5,120.00 USD | 5,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 195.07 USD |
| `7D` | `163.91` | 78,740.00 USD | 78,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,760.00 USD |
| `1D` | `163.94` | 5,320.00 USD | 5,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 206.09 USD |
| `7D` | `164.07` | 83,300.00 USD | 83,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,560.00 USD |
| `1D` | `164.10` | 5,340.00 USD | 5,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19.94 USD |
| `7D` | `164.23` | 86,040.00 USD | 86,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD |
| `7D` | `172.39` | 86,230.00 USD | 86,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 194.13 USD |
| `7D` | `172.55` | 86,250.00 USD | 86,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22.99 USD |
| `7D` | `172.71` | 86,300.00 USD | 86,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 47.74 USD |
| `7D` | `172.87` | 86,310.00 USD | 86,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.35 USD |
| `1D` | `172.90` | 5,350.00 USD | 5,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7.64 USD |
| `1D` | `172.93` | 5,360.00 USD | 5,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6.56 USD |
| `7D` | `173.03` | 86,330.00 USD | 86,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22.04 USD |
| `7D` | `173.19` | 86,520.00 USD | 86,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 188.22 USD |
| `7D` | `173.25` | 86,540.00 USD | 86,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19.44 USD |

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
  * Current Rate: `0.00` | Last 24h: `-325.46` | Last 3d: `-948.57` | Last 7d: `-948.57`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-0.0137%` | **USDT BingX** | `-` |
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
| `10:15:00` | `157.60` | `157.60` | `157.60` | `157.64` | `157.58` | 72,969.26 USD | 22,722.88 USD | 50,246.38 USD | -27,523.49 USD | `-37.72%` | `0B / 1S` |
| `10:20:00` | `157.48` | `157.48` | `157.48` | `157.60` | `157.45` | 99,684.84 USD | 13,302.54 USD | 86,382.30 USD | -73,079.76 USD | `-73.31%` | `0B / 1S` |
| `10:25:00` | `157.46` | `157.46` | `157.46` | `157.54` | `157.45` | 81,405.27 USD | 19,302.28 USD | 62,102.99 USD | -42,800.71 USD | `-52.58%` | `0B / 1S` |
| `10:30:00` | `157.54` | `157.54` | `157.54` | `157.55` | `157.44` | 72,783.02 USD | 65,835.55 USD | 6,947.47 USD | 58,888.08 USD | `+80.91%` | `1B / 0S` |
| `10:30:00` | `157.64` | `157.64` | `157.64` | `157.65` | `157.44` | 232,197.83 USD | 214,377.99 USD | 17,819.83 USD | 196,558.16 USD | `+84.65%` | `1B / 0S` |
| `10:35:00` | `157.54` | `157.54` | `157.54` | `157.60` | `157.52` | 77,038.04 USD | 29,670.06 USD | 47,367.98 USD | -17,697.93 USD | `-22.97%` | `0B / 1S` |
| `10:40:00` | `157.64` | `157.64` | `157.64` | `157.65` | `157.54` | 82,285.99 USD | 71,651.57 USD | 10,634.42 USD | 61,017.16 USD | `+74.15%` | `1B / 0S` |
| `10:45:00` | `157.63` | `157.63` | `157.63` | `157.67` | `157.61` | 94,417.97 USD | 31,886.77 USD | 62,531.20 USD | -30,644.43 USD | `-32.46%` | `0B / 1S` |
| `10:45:00` | `157.55` | `157.55` | `157.55` | `157.67` | `157.55` | 281,384.30 USD | 23,836.27 USD | 257,548.03 USD | -233,711.75 USD | `-83.06%` | `0B / 1S` |
| `10:50:00` | `157.60` | `157.60` | `157.60` | `157.63` | `157.57` | 84,160.54 USD | 35,400.86 USD | 48,759.68 USD | -13,358.82 USD | `-15.87%` | `0B / 1S` |

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
  * `2026-10-30 16:26:21 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:29:21 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `157.08` (Risk Distance: `0.1633` pts)
  * +2.5R Take Profit: `157.65`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.16 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `157.60` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `157.76` (Risk Distance: `0.1633` pts)
  * +2.5R Take Profit: `157.19`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.16 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`158.43`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
