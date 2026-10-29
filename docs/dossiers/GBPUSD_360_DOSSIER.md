# 🏛️ SOVEREIGN CANDIDATE DOSSIER: GBPUSD
**Canonical Key**: `GBPUSD` | **Broker Instrument**: `GBPUSD.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 04:50:10 IST` (`2026-10-29 23:20:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.34` | **Live Ask Quote**: `1.34` | **Mid Price**: `1.34`
- **Spread Points**: `4.00` | **Spread BPS**: `0.30 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `100,000.0` | Digits: `5` | Point: `1e-05`
  * Point Value (1.0 Lot): `1.00 USD` | Point Value (0.01 Lot): `0.0100 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`50.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `1.33` | VWAP Z-Score: `+2.06` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.000629` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `65.04` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.34` | Lower -3.00σ Band: `1.33`
  * Upper +2.51σ Band: `1.34` | Lower -2.51σ Band: `1.33`
  * Upper +2.01σ Band: `1.34` | Lower -2.01σ Band: `1.33`
  * Upper +2.00σ Band: `1.34` | Lower -2.00σ Band: `1.33`
  * Upper +1.28σ Band: `1.34` | Lower -1.28σ Band: `1.33`
  * Upper +1.00σ Band: `1.34` | Lower -1.00σ Band: `1.33`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.34` | EMA-20=`1.34` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.34` (Slope: `+0.0000`) | EMA-100=`1.33`
  * Institutional Anchors: EMA-144=`1.33` | EMA-200=`1.33` (Slope: `+0.0451`) | EMA-233=`1.33`
- **Range Boundaries**: 24H High=`1.34` | 24H Low=`1.33` | Weekly High=`1.34` | Weekly Low=`1.33`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.34` (Distance: `-0.04%`)
  * Point of Control (POC) = `1.34` (Distance: `-0.00%`)
  * Value Area Low (VAL) = `1.34` (Distance: `+0.01%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.33` | POC=`1.33` | VAL=`1.33`
  * Prior Day Extremes: PDH=`1.34` | PDL=`1.33` | PDC=`1.34`
  * Monday Range Blueprint: High=`1.34` | Mid=`1.34` | Low=`1.33`
  * Developing Weekly Value Area: Weekly VAH=`1.34` | Weekly POC=`1.33` | Weekly VAL=`1.33`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.34` | Low=`1.34`
  * London Session (08:00-16:00 UTC): High=`1.34` | Low=`1.33`
  * New York Session (13:00-21:00 UTC): High=`1.35` | Low=`1.33`
  * Initial Balance (First Hour): IB High=`1.34` | IB Low=`1.33`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.33` - `1.34`
  * Optimal Trade Entry (OTE 0.705): `1.34`
  * Structural Invalidation Anchor (0.786): `1.35`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `638` | 853.40 USD | 723.53 USD | `+84.78%` | 2,884.97 USD | `+2.47` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `423` | 565.95 USD | 296.89 USD | `+52.46%` | 3,181.87 USD | `+0.84` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `226` | 302.32 USD | -248.69 USD | `-82.26%` | 2,933.18 USD | `-1.18` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `876` | 1,170.80 USD | -819.56 USD | `-70.00%` | 10,909.93 USD | `-0.88` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `1,531` | 2,048.40 USD | 1,695.02 USD | `+82.75%` | 12,604.95 USD | `+1.79` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `720` | 963.45 USD | 328.13 USD | `+34.06%` | 12,933.08 USD | `+0.27` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `3,990` | 5,331.12 USD | -3,998.34 USD | `-75.00%` | 13,103.14 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `3,136` | 4,191.36 USD | 316.33 USD | `+7.55%` | 13,419.47 USD | `-0.08` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `3,845` | 5,142.69 USD | 1,469.34 USD | `+28.57%` | 14,888.81 USD | `+0.14` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.33` | `1.33` | `1.33` | `1.33` | `23,876` | 31,800.92 USD | 4,068.43 USD | `+12.79%` | -7,908.43 USD | `+1.38` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `1.33` | `1.34` | `1.33` | `1.34` | `40,930` | 54,714.81 USD | 35,923.87 USD | `+65.66%` | 28,015.44 USD | `+1.94` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `16,632` | 22,245.30 USD | 5,841.73 USD | `+26.26%` | 33,857.17 USD | `+0.01` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.33` | `1.33` | `1.33` | `1.33` | `17,244` | 22,969.01 USD | -1,056.57 USD | `-4.60%` | -3,726.39 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.33` | `1.33` | `1.33` | `1.33` | `17,831` | 23,736.63 USD | -8,250.46 USD | `-34.76%` | -11,976.86 USD | `-1.38` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.33` | `1.33` | `1.33` | `1.33` | `23,876` | 31,800.92 USD | 4,068.43 USD | `+12.79%` | -7,908.43 USD | `+1.38` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `1.33` | `1.34` | `1.33` | `1.34` | `40,930` | 54,714.81 USD | 35,923.87 USD | `+65.66%` | 28,015.44 USD | `+1.94` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `16,632` | 22,245.30 USD | 5,841.73 USD | `+26.26%` | 33,857.17 USD | `+0.01` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

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
| `7D` | `1.20` | 44,950.00 USD | 0.00 USD | 44,950.00 USD | 0.00 USD | 0.00 USD | 641.54 USD |
| `7D` | `1.20` | 44,300.00 USD | 0.00 USD | 44,300.00 USD | 0.00 USD | 0.00 USD | 888.61 USD |
| `7D` | `1.20` | 43,420.00 USD | 0.00 USD | 43,420.00 USD | 0.00 USD | 0.00 USD | 50.66 USD |
| `7D` | `1.21` | 43,370.00 USD | 0.00 USD | 43,370.00 USD | 0.00 USD | 0.00 USD | 155.35 USD |
| `7D` | `1.21` | 43,210.00 USD | 0.00 USD | 43,210.00 USD | 0.00 USD | 0.00 USD | 41.31 USD |
| `1D` | `1.21` | 4,950.00 USD | 0.00 USD | 4,950.00 USD | 0.00 USD | 0.00 USD | 0.44 USD |
| `7D` | `1.28` | 43,170.00 USD | 0.00 USD | 43,170.00 USD | 0.00 USD | 0.00 USD | 810.32 USD |
| `7D` | `1.28` | 42,360.00 USD | 0.00 USD | 42,360.00 USD | 0.00 USD | 0.00 USD | 86.09 USD |
| `7D` | `1.28` | 42,270.00 USD | 0.00 USD | 42,270.00 USD | 0.00 USD | 0.00 USD | 242.38 USD |
| `1D` | `1.28` | 4,950.00 USD | 0.00 USD | 4,950.00 USD | 0.00 USD | 0.00 USD | 72.94 USD |
| `7D` | `1.28` | 42,030.00 USD | 0.00 USD | 42,030.00 USD | 0.00 USD | 0.00 USD | 1,520.00 USD |
| `1D` | `1.28` | 4,870.00 USD | 0.00 USD | 4,870.00 USD | 0.00 USD | 0.00 USD | 23.09 USD |
| `7D` | `1.28` | 40,510.00 USD | 0.00 USD | 40,510.00 USD | 0.00 USD | 0.00 USD | 2,800.00 USD |
| `1D` | `1.28` | 4,850.00 USD | 0.00 USD | 4,850.00 USD | 0.00 USD | 0.00 USD | 424.75 USD |
| `7D` | `1.28` | 37,710.00 USD | 0.00 USD | 37,710.00 USD | 0.00 USD | 0.00 USD | 113.97 USD |
| `1D` | `1.28` | 4,430.00 USD | 0.00 USD | 4,430.00 USD | 0.00 USD | 0.00 USD | 32.99 USD |
| `7D` | `1.28` | 37,590.00 USD | 0.00 USD | 37,590.00 USD | 0.00 USD | 0.00 USD | 396.52 USD |
| `1D` | `1.28` | 4,390.00 USD | 0.00 USD | 4,390.00 USD | 0.00 USD | 0.00 USD | 130.13 USD |
| `7D` | `1.29` | 37,200.00 USD | 0.00 USD | 37,200.00 USD | 0.00 USD | 0.00 USD | 180.17 USD |
| `1D` | `1.29` | 4,260.00 USD | 0.00 USD | 4,260.00 USD | 0.00 USD | 0.00 USD | 22.69 USD |
| `7D` | `1.29` | 37,020.00 USD | 0.00 USD | 37,020.00 USD | 0.00 USD | 0.00 USD | 14.46 USD |
| `7D` | `1.30` | 37,000.00 USD | 0.00 USD | 37,000.00 USD | 0.00 USD | 0.00 USD | 1,620.00 USD |
| `7D` | `1.30` | 35,380.00 USD | 0.00 USD | 35,380.00 USD | 0.00 USD | 0.00 USD | 172.14 USD |
| `7D` | `1.31` | 35,210.00 USD | 0.00 USD | 35,210.00 USD | 0.00 USD | 0.00 USD | 484.77 USD |
| `1D` | `1.31` | 4,240.00 USD | 0.00 USD | 4,240.00 USD | 0.00 USD | 0.00 USD | 145.88 USD |
| `7D` | `1.31` | 34,720.00 USD | 0.00 USD | 34,720.00 USD | 0.00 USD | 0.00 USD | 3,050.00 USD |
| `1D` | `1.31` | 4,090.00 USD | 0.00 USD | 4,090.00 USD | 0.00 USD | 0.00 USD | 46.20 USD |
| `7D` | `1.31` | 31,680.00 USD | 0.00 USD | 31,680.00 USD | 0.00 USD | 0.00 USD | 5,600.00 USD |
| `1D` | `1.31` | 4,050.00 USD | 0.00 USD | 4,050.00 USD | 0.00 USD | 0.00 USD | 819.97 USD |
| `7D` | `1.31` | 26,080.00 USD | 0.00 USD | 26,080.00 USD | 0.00 USD | 0.00 USD | 212.47 USD |
| `1D` | `1.31` | 3,230.00 USD | 0.00 USD | 3,230.00 USD | 0.00 USD | 0.00 USD | 95.54 USD |
| `7D` | `1.31` | 25,870.00 USD | 0.00 USD | 25,870.00 USD | 0.00 USD | 0.00 USD | 764.06 USD |
| `1D` | `1.31` | 3,130.00 USD | 0.00 USD | 3,130.00 USD | 0.00 USD | 0.00 USD | 236.43 USD |
| `7D` | `1.31` | 25,100.00 USD | 0.00 USD | 25,100.00 USD | 0.00 USD | 0.00 USD | 325.36 USD |
| `1D` | `1.31` | 2,900.00 USD | 0.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD | 69.21 USD |
| `7D` | `1.31` | 24,780.00 USD | 0.00 USD | 24,780.00 USD | 0.00 USD | 0.00 USD | 108.37 USD |
| `7D` | `1.32` | 24,670.00 USD | 0.00 USD | 24,670.00 USD | 0.00 USD | 0.00 USD | 3,350.00 USD |
| `7D` | `1.32` | 21,310.00 USD | 0.00 USD | 21,310.00 USD | 0.00 USD | 0.00 USD | 733.67 USD |
| `7D` | `1.32` | 20,580.00 USD | 0.00 USD | 20,580.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD |
| `1D` | `1.32` | 2,830.00 USD | 0.00 USD | 2,830.00 USD | 0.00 USD | 0.00 USD | 310.62 USD |
| `7D` | `1.32` | 17,950.00 USD | 0.00 USD | 17,950.00 USD | 0.00 USD | 0.00 USD | 6,670.00 USD |
| `1D` | `1.32` | 2,520.00 USD | 0.00 USD | 2,520.00 USD | 0.00 USD | 0.00 USD | 1,320.00 USD |
| `7D` | `1.32` | 11,280.00 USD | 0.00 USD | 11,280.00 USD | 0.00 USD | 0.00 USD | 8,460.00 USD |
| `1D` | `1.32` | 1,200.00 USD | 0.00 USD | 1,200.00 USD | 0.00 USD | 0.00 USD | 566.87 USD |
| `7D` | `1.32` | 2,820.00 USD | 0.00 USD | 2,820.00 USD | 0.00 USD | 0.00 USD | 612.00 USD |
| `1D` | `1.32` | 632.29 USD | 0.00 USD | 632.29 USD | 0.00 USD | 0.00 USD | 20.99 USD |
| `7D` | `1.33` | 2,210.00 USD | 0.00 USD | 2,210.00 USD | 0.00 USD | 0.00 USD | 1,770.00 USD |
| `1D` | `1.33` | 611.30 USD | 0.00 USD | 611.30 USD | 0.00 USD | 0.00 USD | 607.05 USD |
| `7D` | `1.33` | 435.06 USD | 0.00 USD | 435.06 USD | 0.00 USD | 0.00 USD | 407.14 USD |
| `1D` | `1.33` | 4.25 USD | 0.00 USD | 4.25 USD | 0.00 USD | 0.00 USD | 4.25 USD |
| `7D` | `1.33` | 27.92 USD | 0.00 USD | 27.92 USD | 0.00 USD | 0.00 USD | 27.92 USD |
| `1D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 3,350.00 USD | 3,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,350.00 USD |
| `7D` | `1.35` | 4,090.00 USD | 4,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 733.67 USD |
| `7D` | `1.35` | 6,720.00 USD | 6,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD |
| `1D` | `1.35` | 310.62 USD | 310.62 USD | 0.00 USD | 0.00 USD | 0.00 USD | 310.62 USD |
| `7D` | `1.35` | 13,380.00 USD | 13,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,670.00 USD |
| `1D` | `1.35` | 1,630.00 USD | 1,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,320.00 USD |
| `7D` | `1.35` | 21,850.00 USD | 21,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,460.00 USD |
| `1D` | `1.35` | 2,160.00 USD | 2,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 534.99 USD |
| `7D` | `1.35` | 22,430.00 USD | 22,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 580.88 USD |
| `1D` | `1.35` | 2,220.00 USD | 2,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 52.87 USD |
| `7D` | `1.35` | 24,190.00 USD | 24,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,760.00 USD |
| `1D` | `1.35` | 2,750.00 USD | 2,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 537.40 USD |
| `7D` | `1.35` | 24,640.00 USD | 24,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 453.06 USD |
| `1D` | `1.35` | 2,830.00 USD | 2,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 73.90 USD |
| `7D` | `1.35` | 24,670.00 USD | 24,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 27.92 USD |
| `7D` | `1.36` | 26,290.00 USD | 26,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,620.00 USD |
| `7D` | `1.36` | 26,460.00 USD | 26,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 172.14 USD |
| `7D` | `1.36` | 26,810.00 USD | 26,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 347.41 USD |
| `1D` | `1.36` | 2,970.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 145.88 USD |
| `7D` | `1.36` | 29,990.00 USD | 29,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,190.00 USD |
| `1D` | `1.36` | 3,010.00 USD | 3,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33.74 USD |
| `7D` | `1.36` | 34,680.00 USD | 34,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,690.00 USD |
| `1D` | `1.36` | 3,640.00 USD | 3,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 637.96 USD |
| `7D` | `1.36` | 35,790.00 USD | 35,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD |
| `1D` | `1.36` | 3,930.00 USD | 3,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 290.01 USD |
| `7D` | `1.36` | 36,460.00 USD | 36,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 671.34 USD |
| `1D` | `1.36` | 4,160.00 USD | 4,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 228.71 USD |
| `7D` | `1.37` | 36,860.00 USD | 36,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 397.00 USD |
| `1D` | `1.37` | 4,240.00 USD | 4,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 76.93 USD |
| `7D` | `1.37` | 37,000.00 USD | 37,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 142.41 USD |
| `7D` | `1.38` | 37,810.00 USD | 37,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 810.32 USD |
| `7D` | `1.38` | 37,900.00 USD | 37,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 86.09 USD |
| `7D` | `1.39` | 38,070.00 USD | 38,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 173.70 USD |
| `1D` | `1.39` | 4,310.00 USD | 4,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 72.94 USD |
| `7D` | `1.39` | 39,560.00 USD | 39,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,490.00 USD |
| `1D` | `1.39` | 4,330.00 USD | 4,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.34 USD |
| `7D` | `1.39` | 41,810.00 USD | 41,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `1.39` | 4,650.00 USD | 4,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 322.51 USD |
| `7D` | `1.39` | 42,540.00 USD | 42,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 731.25 USD |
| `1D` | `1.39` | 4,790.00 USD | 4,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 144.98 USD |
| `7D` | `1.39` | 42,650.00 USD | 42,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 108.00 USD |
| `1D` | `1.39` | 4,900.00 USD | 4,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 110.54 USD |
| `7D` | `1.39` | 43,070.00 USD | 43,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 413.85 USD |
| `1D` | `1.39` | 4,950.00 USD | 4,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 41.22 USD |
| `7D` | `1.39` | 43,170.00 USD | 43,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 103.32 USD |
| `1D` | `1.39` | 4,950.00 USD | 4,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1.06 USD |
| `7D` | `1.46` | 43,490.00 USD | 43,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 324.13 USD |
| `7D` | `1.46` | 43,510.00 USD | 43,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14.71 USD |
| `7D` | `1.47` | 43,590.00 USD | 43,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 80.63 USD |
| `7D` | `1.47` | 44,150.00 USD | 44,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 562.18 USD |
| `1D` | `1.47` | 4,980.00 USD | 4,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33.20 USD |
| `7D` | `1.47` | 44,530.00 USD | 44,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 376.19 USD |
| `1D` | `1.47` | 5,110.00 USD | 5,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 126.96 USD |
| `7D` | `1.47` | 45,150.00 USD | 45,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 619.25 USD |
| `1D` | `1.47` | 5,160.00 USD | 5,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 55.91 USD |
| `7D` | `1.47` | 45,200.00 USD | 45,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 50.66 USD |
| `1D` | `1.47` | 5,160.00 USD | 5,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2.10 USD |
| `7D` | `1.47` | 45,340.00 USD | 45,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 145.65 USD |
| `1D` | `1.47` | 5,220.00 USD | 5,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 51.19 USD |
| `1D` | `1.47` | 5,220.00 USD | 5,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7.40 USD |
| `7D` | `1.47` | 45,390.00 USD | 45,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 45.23 USD |
| `7D` | `1.47` | 45,390.00 USD | 45,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.78 USD |

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
  * Current Rate: `0.00` | Last 24h: `0.00` | Last 3d: `0.00` | Last 7d: `0.00`
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
| `22:35:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 271.43 USD | 159.66 USD | 111.76 USD | 47.90 USD | `+17.65%` | `1B / 0S` |
| `22:40:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 335.56 USD | 16.78 USD | 318.78 USD | -302.01 USD | `-90.00%` | `0B / 1S` |
| `22:45:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 1,170.80 USD | 175.62 USD | 995.18 USD | -819.56 USD | `-70.00%` | `0B / 1S` |
| `22:45:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 303.44 USD | 35.01 USD | 268.43 USD | -233.42 USD | `-76.92%` | `0B / 1S` |
| `22:50:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 392.98 USD | 149.33 USD | 243.64 USD | -94.31 USD | `-24.00%` | `0B / 1S` |
| `22:55:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 474.47 USD | 149.83 USD | 324.64 USD | -174.80 USD | `-36.84%` | `0B / 1S` |
| `23:00:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 5,142.69 USD | 3,306.01 USD | 1,836.67 USD | 1,469.34 USD | `+28.57%` | `1B / 0S` |
| `23:00:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 628.38 USD | 506.19 USD | 122.18 USD | 384.01 USD | `+61.11%` | `1B / 0S` |
| `23:00:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 2,048.40 USD | 1,871.71 USD | 176.69 USD | 1,695.02 USD | `+82.75%` | `1B / 0S` |
| `23:05:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 853.40 USD | 788.46 USD | 64.93 USD | 723.53 USD | `+84.78%` | `1B / 0S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `2026-10-28 17:30:00 IST` | `4h` | `BULLISH ABSORPTION` | **`BULLISH`** | GBPUSD Macro Delta Flow: BULLISH ABSORPT | `1.33` | 1,668.59 USD | 1,668.59 USD |

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
  * `2026-10-30 04:15:34 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:40:34 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:34 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1.34` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1.34` (Risk Distance: `0.000815` pts)
  * +2.5R Take Profit: `1.34`
  * Mathematical Lot Sizing: **`0.12 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.34` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.34` (Risk Distance: `0.000815` pts)
  * +2.5R Take Profit: `1.34`
  * Mathematical Lot Sizing: **`0.12 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.35`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
