# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USDJPY
**Canonical Key**: `USDJPY` | **Broker Instrument**: `USDJPY.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 15:36:16 IST` (`2026-10-30 10:06:16 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `157.28` | **Live Ask Quote**: `157.29` | **Mid Price**: `157.28`
- **Spread Points**: `5.00` | **Spread BPS**: `0.32 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `157.45` | VWAP Z-Score: `-0.82` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1456` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `44.71` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `157.86` | Lower -3.00σ Band: `157.05`
  * Upper +2.51σ Band: `157.79` | Lower -2.51σ Band: `157.11`
  * Upper +2.01σ Band: `157.72` | Lower -2.01σ Band: `157.18`
  * Upper +2.00σ Band: `157.72` | Lower -2.00σ Band: `157.18`
  * Upper +1.28σ Band: `157.62` | Lower -1.28σ Band: `157.28`
  * Upper +1.00σ Band: `157.59` | Lower -1.00σ Band: `157.32`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`157.38` | EMA-20=`157.43` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`157.53` (Slope: `+0.0000`) | EMA-100=`157.63`
  * Institutional Anchors: EMA-144=`157.69` | EMA-200=`157.74` (Slope: `-0.0247`) | EMA-233=`157.75`
- **Range Boundaries**: 24H High=`158.13` | 24H Low=`157.12` | Weekly High=`158.35` | Weekly Low=`157.12`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `157.61` (Distance: `-0.21%`)
  * Point of Control (POC) = `157.44` (Distance: `-0.10%`)
  * Value Area Low (VAL) = `157.26` (Distance: `+0.02%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`157.99` | POC=`157.87` | VAL=`157.76`
  * Prior Day Extremes: PDH=`158.13` | PDL=`157.60` | PDC=`157.69`
  * Monday Range Blueprint: High=`157.64` | Mid=`157.15` | Low=`156.65`
  * Developing Weekly Value Area: Weekly VAH=`158.03` | Weekly POC=`157.87` | Weekly VAL=`157.41`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`157.90` | Low=`157.12`
  * London Session (08:00-16:00 UTC): High=`157.75` | Low=`157.16`
  * New York Session (13:00-21:00 UTC): High=`158.23` | Low=`156.34`
  * Initial Balance (First Hour): IB High=`157.70` | IB Low=`157.40`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `156.66` - `157.91`
  * Optimal Trade Entry (OTE 0.705): `157.60`
  * Structural Invalidation Anchor (0.786): `158.54`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `157.56` | `157.65` | `157.53` | `157.62` | `721` | 113,643.30 USD | 52,969.33 USD | `+46.61%` | 810,042.66 USD | `+0.79` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `157.62` | `157.63` | `157.54` | `157.60` | `811` | 127,812.79 USD | 5,455.42 USD | `+4.27%` | 815,498.08 USD | `-0.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `157.60` | `157.71` | `157.59` | `157.67` | `717` | 113,050.11 USD | 52,626.77 USD | `+46.55%` | 868,124.86 USD | `+0.76` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `157.61` | `157.62` | `157.51` | `157.56` | `1,670` | 263,116.85 USD | -83,617.64 USD | `-31.78%` | 99,032.80 USD | `-0.54` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `157.55` | `157.65` | `157.47` | `157.56` | `2,665` | 419,910.72 USD | 26,532.82 USD | `+6.32%` | 125,565.62 USD | `+0.13` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `157.56` | `157.71` | `157.53` | `157.67` | `2,249` | 354,602.08 USD | 203,054.26 USD | `+57.26%` | 328,619.88 USD | `+1.03` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `157.42` | `157.43` | `157.25` | `157.43` | `6,856` | 1,079,319.51 USD | 536,627.96 USD | `+49.72%` | 1,368,393.41 USD | `+0.73` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `157.43` | `157.70` | `157.40` | `157.62` | `7,828` | 1,233,849.36 USD | 697,124.89 USD | `+56.50%` | 2,065,518.29 USD | `+0.98` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `157.62` | `157.71` | `157.47` | `157.67` | `8,064` | 1,271,458.94 USD | 557,244.35 USD | `+43.83%` | 2,622,762.65 USD | `+0.73` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `202` | `0x0911...129a` | `SHORT` | 10,412,935.97 USD | `66,223.20` | `156.58` | `157.25` | `167.71` | -43,915.74 USD | `-0.42%` | `20X Isolated` |
| `1019` | `0x9dea...d617` | `LONG` | 2,133,271.94 USD | `13,566.98` | `157.66` | `157.25` | `149.21` | -5,741.81 USD | `-0.27%` | `50X Isolated` |
| `1093` | `0xec0b...b078` | `SHORT` | 1,983,974.13 USD | `12,617.49` | `158.22` | `157.25` | `162.94` | 12,391.55 USD | `+0.62%` | `20X Isolated` |
| `1151` | `0xc966...f6b6` | `SHORT` | 1,910,566.63 USD | `12,150.64` | `157.61` | `157.25` | `215.26` | 4,440.60 USD | `+0.23%` | `5X Isolated` |
| `1176` | `0xbef1...d2e5` | `LONG` | 1,858,779.64 USD | `11,821.29` | `157.63` | `157.25` | `155.50` | -4,580.97 USD | `-0.25%` | `50X Isolated` |
| `1884` | `0x3d89...eb14` | `LONG` | 1,084,956.00 USD | `6,900.00` | `158.17` | `157.25` | `127.34` | -6,433.60 USD | `-0.59%` | `5X Isolated` |

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
| `1D` | `141.51` | 6,470.00 USD | 0.00 USD | 6,470.00 USD | 0.00 USD | 0.00 USD | 14.20 USD |
| `7D` | `141.51` | 90,340.00 USD | 0.00 USD | 90,340.00 USD | 0.00 USD | 0.00 USD | 5.35 USD |
| `1D` | `141.67` | 6,460.00 USD | 0.00 USD | 6,460.00 USD | 0.00 USD | 0.00 USD | 173.52 USD |
| `7D` | `141.67` | 90,340.00 USD | 0.00 USD | 90,340.00 USD | 0.00 USD | 0.00 USD | 161.17 USD |
| `1D` | `141.83` | 6,290.00 USD | 0.00 USD | 6,290.00 USD | 0.00 USD | 0.00 USD | 144.73 USD |
| `7D` | `141.83` | 90,170.00 USD | 0.00 USD | 90,170.00 USD | 0.00 USD | 0.00 USD | 1,360.00 USD |
| `1D` | `141.99` | 6,140.00 USD | 0.00 USD | 6,140.00 USD | 0.00 USD | 0.00 USD | 9.89 USD |
| `7D` | `141.99` | 88,810.00 USD | 0.00 USD | 88,810.00 USD | 0.00 USD | 0.00 USD | 1,890.00 USD |
| `7D` | `142.15` | 86,920.00 USD | 0.00 USD | 86,920.00 USD | 0.00 USD | 0.00 USD | 882.31 USD |
| `7D` | `150.47` | 86,040.00 USD | 0.00 USD | 86,040.00 USD | 0.00 USD | 0.00 USD | 544.08 USD |
| `7D` | `150.63` | 85,490.00 USD | 0.00 USD | 85,490.00 USD | 0.00 USD | 0.00 USD | 122.88 USD |
| `7D` | `150.79` | 85,370.00 USD | 0.00 USD | 85,370.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `1D` | `150.95` | 6,130.00 USD | 0.00 USD | 6,130.00 USD | 0.00 USD | 0.00 USD | 316.23 USD |
| `7D` | `150.95` | 85,360.00 USD | 0.00 USD | 85,360.00 USD | 0.00 USD | 0.00 USD | 55.10 USD |
| `1D` | `151.11` | 5,810.00 USD | 0.00 USD | 5,810.00 USD | 0.00 USD | 0.00 USD | 159.54 USD |
| `7D` | `151.11` | 85,300.00 USD | 0.00 USD | 85,300.00 USD | 0.00 USD | 0.00 USD | 347.81 USD |
| `1D` | `151.27` | 5,660.00 USD | 0.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | 286.97 USD |
| `7D` | `151.27` | 84,950.00 USD | 0.00 USD | 84,950.00 USD | 0.00 USD | 0.00 USD | 2,790.00 USD |
| `1D` | `151.43` | 5,370.00 USD | 0.00 USD | 5,370.00 USD | 0.00 USD | 0.00 USD | 113.08 USD |
| `7D` | `151.43` | 82,160.00 USD | 0.00 USD | 82,160.00 USD | 0.00 USD | 0.00 USD | 4,630.00 USD |
| `7D` | `151.59` | 77,530.00 USD | 0.00 USD | 77,530.00 USD | 0.00 USD | 0.00 USD | 3,790.00 USD |
| `7D` | `153.51` | 73,740.00 USD | 0.00 USD | 73,740.00 USD | 0.00 USD | 0.00 USD | 199.19 USD |
| `7D` | `153.67` | 73,550.00 USD | 0.00 USD | 73,550.00 USD | 0.00 USD | 0.00 USD | 896.05 USD |
| `7D` | `153.83` | 72,650.00 USD | 0.00 USD | 72,650.00 USD | 0.00 USD | 0.00 USD | 238.69 USD |
| `1D` | `153.99` | 5,260.00 USD | 0.00 USD | 5,260.00 USD | 0.00 USD | 0.00 USD | 33.56 USD |
| `7D` | `153.99` | 72,410.00 USD | 0.00 USD | 72,410.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `1D` | `154.15` | 5,220.00 USD | 0.00 USD | 5,220.00 USD | 0.00 USD | 0.00 USD | 611.81 USD |
| `7D` | `154.15` | 72,380.00 USD | 0.00 USD | 72,380.00 USD | 0.00 USD | 0.00 USD | 110.19 USD |
| `1D` | `154.31` | 4,610.00 USD | 0.00 USD | 4,610.00 USD | 0.00 USD | 0.00 USD | 331.39 USD |
| `7D` | `154.31` | 72,270.00 USD | 0.00 USD | 72,270.00 USD | 0.00 USD | 0.00 USD | 997.59 USD |
| `1D` | `154.47` | 4,280.00 USD | 0.00 USD | 4,280.00 USD | 0.00 USD | 0.00 USD | 735.00 USD |
| `7D` | `154.47` | 71,280.00 USD | 0.00 USD | 71,280.00 USD | 0.00 USD | 0.00 USD | 7,530.00 USD |
| `1D` | `154.63` | 3,540.00 USD | 0.00 USD | 3,540.00 USD | 0.00 USD | 0.00 USD | 39.91 USD |
| `7D` | `154.63` | 63,750.00 USD | 0.00 USD | 63,750.00 USD | 0.00 USD | 0.00 USD | 9,120.00 USD |
| `7D` | `154.79` | 54,630.00 USD | 0.00 USD | 54,630.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD |
| `7D` | `155.11` | 49,160.00 USD | 0.00 USD | 49,160.00 USD | 0.00 USD | 0.00 USD | 954.59 USD |
| `7D` | `155.27` | 48,210.00 USD | 0.00 USD | 48,210.00 USD | 0.00 USD | 0.00 USD | 1,240.00 USD |
| `7D` | `155.43` | 46,970.00 USD | 0.00 USD | 46,970.00 USD | 0.00 USD | 0.00 USD | 477.37 USD |
| `1D` | `155.59` | 3,500.00 USD | 0.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | 67.12 USD |
| `7D` | `155.59` | 46,500.00 USD | 0.00 USD | 46,500.00 USD | 0.00 USD | 0.00 USD | 53.53 USD |
| `1D` | `155.75` | 3,440.00 USD | 0.00 USD | 3,440.00 USD | 0.00 USD | 0.00 USD | 1,220.00 USD |
| `7D` | `155.75` | 46,440.00 USD | 0.00 USD | 46,440.00 USD | 0.00 USD | 0.00 USD | 529.27 USD |
| `1D` | `155.91` | 2,210.00 USD | 0.00 USD | 2,210.00 USD | 0.00 USD | 0.00 USD | 859.23 USD |
| `7D` | `155.91` | 45,910.00 USD | 0.00 USD | 45,910.00 USD | 0.00 USD | 0.00 USD | 1,930.00 USD |
| `1D` | `156.07` | 1,350.00 USD | 0.00 USD | 1,350.00 USD | 0.00 USD | 0.00 USD | 1,290.00 USD |
| `7D` | `156.07` | 43,980.00 USD | 0.00 USD | 43,980.00 USD | 0.00 USD | 0.00 USD | 21,700.00 USD |
| `1D` | `156.23` | 64.05 USD | 0.00 USD | 64.05 USD | 0.00 USD | 0.00 USD | 64.05 USD |
| `7D` | `156.23` | 22,280.00 USD | 0.00 USD | 22,280.00 USD | 0.00 USD | 0.00 USD | 11,350.00 USD |
| `7D` | `156.39` | 10,940.00 USD | 0.00 USD | 10,940.00 USD | 0.00 USD | 0.00 USD | 10,940.00 USD |
| `1D` | `157.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `157.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `158.31` | 2,180.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,180.00 USD |
| `7D` | `158.47` | 2,670.00 USD | 2,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 491.52 USD |
| `7D` | `158.63` | 2,720.00 USD | 2,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 53.53 USD |
| `1D` | `158.79` | 142.07 USD | 142.07 USD | 0.00 USD | 0.00 USD | 0.00 USD | 142.07 USD |
| `1D` | `158.95` | 1,370.00 USD | 1,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,230.00 USD |
| `7D` | `158.95` | 4,330.00 USD | 4,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,610.00 USD |
| `1D` | `159.11` | 2,600.00 USD | 2,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,230.00 USD |
| `7D` | `159.11` | 7,790.00 USD | 7,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,460.00 USD |
| `1D` | `159.27` | 3,470.00 USD | 3,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 865.66 USD |
| `7D` | `159.27` | 27,930.00 USD | 27,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,140.00 USD |
| `1D` | `159.43` | 3,500.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33.92 USD |
| `7D` | `159.43` | 38,230.00 USD | 38,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,290.00 USD |
| `7D` | `159.59` | 49,160.00 USD | 49,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,940.00 USD |
| `7D` | `159.75` | 49,280.00 USD | 49,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 116.22 USD |
| `7D` | `159.91` | 50,260.00 USD | 50,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 979.02 USD |
| `7D` | `160.07` | 50,500.00 USD | 50,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 238.69 USD |
| `7D` | `160.23` | 50,520.00 USD | 50,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `1D` | `160.39` | 4,140.00 USD | 4,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 632.47 USD |
| `7D` | `160.39` | 50,630.00 USD | 50,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 110.19 USD |
| `1D` | `160.55` | 4,450.00 USD | 4,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 319.07 USD |
| `7D` | `160.55` | 51,330.00 USD | 51,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 695.63 USD |
| `1D` | `160.71` | 4,900.00 USD | 4,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 448.78 USD |
| `7D` | `160.71` | 56,790.00 USD | 56,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,460.00 USD |
| `1D` | `160.87` | 5,260.00 USD | 5,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 351.35 USD |
| `7D` | `160.87` | 66,170.00 USD | 66,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,390.00 USD |
| `7D` | `161.03` | 68,280.00 USD | 68,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,110.00 USD |
| `7D` | `161.19` | 73,740.00 USD | 73,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD |
| `7D` | `162.95` | 73,980.00 USD | 73,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 238.64 USD |
| `7D` | `163.11` | 74,290.00 USD | 74,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 308.98 USD |
| `7D` | `163.27` | 74,410.00 USD | 74,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 119.34 USD |
| `1D` | `163.43` | 5,270.00 USD | 5,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16.78 USD |
| `7D` | `163.43` | 74,420.00 USD | 74,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `1D` | `163.59` | 5,580.00 USD | 5,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 305.90 USD |
| `7D` | `163.59` | 74,480.00 USD | 74,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 55.10 USD |
| `1D` | `163.75` | 5,740.00 USD | 5,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 165.70 USD |
| `7D` | `163.75` | 74,980.00 USD | 74,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 498.79 USD |
| `1D` | `163.91` | 6,110.00 USD | 6,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 367.50 USD |
| `7D` | `163.91` | 78,740.00 USD | 78,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,760.00 USD |
| `1D` | `164.07` | 6,130.00 USD | 6,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19.94 USD |
| `7D` | `164.07` | 83,300.00 USD | 83,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,560.00 USD |
| `7D` | `164.23` | 86,040.00 USD | 86,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD |
| `7D` | `172.39` | 86,230.00 USD | 86,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 194.13 USD |
| `7D` | `172.55` | 86,250.00 USD | 86,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22.99 USD |
| `7D` | `172.71` | 86,300.00 USD | 86,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 47.74 USD |
| `1D` | `172.87` | 6,140.00 USD | 6,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6.71 USD |
| `7D` | `172.87` | 86,310.00 USD | 86,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.35 USD |
| `1D` | `173.03` | 6,260.00 USD | 6,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 119.78 USD |
| `7D` | `173.03` | 86,330.00 USD | 86,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22.04 USD |
| `1D` | `173.19` | 6,320.00 USD | 6,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 66.27 USD |
| `7D` | `173.19` | 86,520.00 USD | 86,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 188.22 USD |
| `1D` | `173.25` | 6,350.00 USD | 6,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 27.24 USD |
| `7D` | `173.33` | 87,540.00 USD | 87,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,020.00 USD |

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
| `09:15:00` | `157.57` | `157.57` | `157.57` | `157.62` | `157.55` | 61,923.83 USD | 12,685.78 USD | 49,238.05 USD | -36,552.26 USD | `-59.03%` | `0B / 1S` |
| `09:20:00` | `157.54` | `157.54` | `157.54` | `157.61` | `157.52` | 78,296.88 USD | 23,015.84 USD | 55,281.04 USD | -32,265.20 USD | `-41.21%` | `0B / 1S` |
| `09:25:00` | `157.56` | `157.56` | `157.56` | `157.56` | `157.51` | 122,892.90 USD | 98,796.25 USD | 24,096.65 USD | 74,699.61 USD | `+60.78%` | `1B / 0S` |
| `09:30:00` | `157.62` | `157.62` | `157.62` | `157.65` | `157.54` | 173,065.66 USD | 131,035.43 USD | 42,030.23 USD | 89,005.20 USD | `+51.43%` | `1B / 0S` |
| `09:30:00` | `157.56` | `157.56` | `157.56` | `157.65` | `157.47` | 419,910.72 USD | 223,221.77 USD | 196,688.95 USD | 26,532.82 USD | `+6.32%` | `1B / 0S` |
| `09:35:00` | `157.57` | `157.57` | `157.57` | `157.64` | `157.49` | 138,502.27 USD | 60,822.54 USD | 77,679.73 USD | -16,857.18 USD | `-12.17%` | `0B / 1S` |
| `09:40:00` | `157.56` | `157.56` | `157.56` | `157.59` | `157.47` | 108,404.72 USD | 70,827.45 USD | 37,577.27 USD | 33,250.19 USD | `+30.67%` | `1B / 0S` |
| `09:45:00` | `157.67` | `157.67` | `157.67` | `157.71` | `157.53` | 354,602.08 USD | 278,828.17 USD | 75,773.91 USD | 203,054.26 USD | `+57.26%` | `1B / 0S` |
| `09:45:00` | `157.62` | `157.62` | `157.62` | `157.65` | `157.53` | 113,643.30 USD | 83,306.32 USD | 30,336.98 USD | 52,969.33 USD | `+46.61%` | `1B / 0S` |
| `09:50:00` | `157.60` | `157.60` | `157.60` | `157.63` | `157.54` | 127,812.79 USD | 66,634.11 USD | 61,178.68 USD | 5,455.42 USD | `+4.27%` | `1B / 0S` |

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
  * `2026-10-30 15:18:36 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:36 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:36 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:37:36 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:36 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:32:36 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `157.26` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `157.07` (Risk Distance: `0.1823` pts)
  * +2.5R Take Profit: `157.71`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.18 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `157.61` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `157.80` (Risk Distance: `0.1823` pts)
  * +2.5R Take Profit: `157.16`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.18 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`158.54`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
