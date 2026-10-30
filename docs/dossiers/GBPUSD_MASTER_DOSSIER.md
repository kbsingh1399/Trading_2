# 🏛️ SOVEREIGN CANDIDATE DOSSIER: GBPUSD
**Canonical Key**: `GBPUSD` | **Broker Instrument**: `GBPUSD.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 16:24:41 IST` (`2026-10-30 10:54:41 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `1.34` | VWAP Z-Score: `+1.86` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000683` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `65.20` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.34` | Lower -3.00σ Band: `1.34`
  * Upper +2.51σ Band: `1.34` | Lower -2.51σ Band: `1.34`
  * Upper +2.01σ Band: `1.34` | Lower -2.01σ Band: `1.34`
  * Upper +2.00σ Band: `1.34` | Lower -2.00σ Band: `1.34`
  * Upper +1.28σ Band: `1.34` | Lower -1.28σ Band: `1.34`
  * Upper +1.00σ Band: `1.34` | Lower -1.00σ Band: `1.34`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.34` | EMA-20=`1.34` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.34` (Slope: `+0.0000`) | EMA-100=`1.34`
  * Institutional Anchors: EMA-144=`1.34` | EMA-200=`1.34` (Slope: `+0.0616`) | EMA-233=`1.33`
- **Range Boundaries**: 24H High=`1.34` | 24H Low=`1.33` | Weekly High=`1.34` | Weekly Low=`1.33`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.34` (Distance: `+0.16%`)
  * Point of Control (POC) = `1.34` (Distance: `+0.27%`)
  * Value Area Low (VAL) = `1.34` (Distance: `+0.35%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `TREND_UP_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.33` | POC=`1.33` | VAL=`1.33`
  * Prior Day Extremes: PDH=`1.34` | PDL=`1.33` | PDC=`1.34`
  * Monday Range Blueprint: High=`1.34` | Mid=`1.34` | Low=`1.33`
  * Developing Weekly Value Area: Weekly VAH=`1.34` | Weekly POC=`1.33` | Weekly VAL=`1.33`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.34` | Low=`1.34`
  * London Session (08:00-16:00 UTC): High=`1.34` | Low=`1.34`
  * New York Session (13:00-21:00 UTC): High=`1.34` | Low=`1.34`
  * Initial Balance (First Hour): IB High=`1.34` | IB Low=`1.34`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.34` - `1.35`
  * Optimal Trade Entry (OTE 0.705): `1.35`
  * Structural Invalidation Anchor (0.786): `1.35`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `455` | 609.80 USD | -443.98 USD | `-72.81%` | 5,799.87 USD | `-1.38` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `341` | 457.07 USD | 204.48 USD | `+44.74%` | 6,004.34 USD | `+0.35` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `357` | 478.34 USD | -372.82 USD | `-77.94%` | 5,631.52 USD | `-1.15` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `1,665` | 2,233.00 USD | 2,009.70 USD | `+90.00%` | 18,739.93 USD | `+1.79` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `1,358` | 1,820.02 USD | -1,623.26 USD | `-89.19%` | 17,116.67 USD | `-1.54` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `1,187` | 1,591.09 USD | 680.40 USD | `+42.76%` | 17,797.07 USD | `+0.53` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `2,941` | 3,938.20 USD | 2,366.38 USD | `+60.09%` | 17,043.65 USD | `+0.31` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `4,999` | 6,695.81 USD | 287.71 USD | `+4.30%` | 17,331.36 USD | `-0.08` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `5,391` | 7,226.26 USD | 2,226.27 USD | `+30.81%` | 19,557.63 USD | `+0.28` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `9,697` | 12,990.20 USD | 11,691.18 USD | `+90.00%` | 57,525.20 USD | `-0.21` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `23,442` | 31,382.04 USD | -22,459.70 USD | `-71.57%` | 35,065.51 USD | `-1.58` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `18,846` | 25,281.16 USD | 19,391.04 USD | `+76.70%` | 54,456.55 USD | `+0.59` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.33` | `1.34` | `1.33` | `1.34` | `40,930` | 54,714.81 USD | 35,923.87 USD | `+65.66%` | 39,992.30 USD | `+1.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `16,632` | 22,245.30 USD | 5,841.73 USD | `+26.26%` | 45,834.02 USD | `-0.65` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `9,697` | 12,990.20 USD | 11,691.18 USD | `+90.00%` | 57,525.20 USD | `-0.21` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `23,442` | 31,382.04 USD | -22,459.70 USD | `-71.57%` | 35,065.51 USD | `-1.58` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `18,846` | 25,281.16 USD | 19,391.04 USD | `+76.70%` | 54,456.55 USD | `+0.59` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `7D` | `1.21` | 43,550.00 USD | 0.00 USD | 43,550.00 USD | 0.00 USD | 0.00 USD | 72.15 USD |
| `1D` | `1.21` | 5,240.00 USD | 0.00 USD | 5,240.00 USD | 0.00 USD | 0.00 USD | 1.54 USD |
| `7D` | `1.28` | 43,480.00 USD | 0.00 USD | 43,480.00 USD | 0.00 USD | 0.00 USD | 810.32 USD |
| `7D` | `1.28` | 42,670.00 USD | 0.00 USD | 42,670.00 USD | 0.00 USD | 0.00 USD | 39.55 USD |
| `7D` | `1.28` | 42,630.00 USD | 0.00 USD | 42,630.00 USD | 0.00 USD | 0.00 USD | 220.24 USD |
| `1D` | `1.28` | 5,240.00 USD | 0.00 USD | 5,240.00 USD | 0.00 USD | 0.00 USD | 72.94 USD |
| `7D` | `1.28` | 42,410.00 USD | 0.00 USD | 42,410.00 USD | 0.00 USD | 0.00 USD | 1,590.00 USD |
| `1D` | `1.28` | 5,160.00 USD | 0.00 USD | 5,160.00 USD | 0.00 USD | 0.00 USD | 121.71 USD |
| `7D` | `1.28` | 40,810.00 USD | 0.00 USD | 40,810.00 USD | 0.00 USD | 0.00 USD | 2,340.00 USD |
| `1D` | `1.28` | 5,040.00 USD | 0.00 USD | 5,040.00 USD | 0.00 USD | 0.00 USD | 199.31 USD |
| `7D` | `1.28` | 38,470.00 USD | 0.00 USD | 38,470.00 USD | 0.00 USD | 0.00 USD | 561.05 USD |
| `1D` | `1.28` | 4,840.00 USD | 0.00 USD | 4,840.00 USD | 0.00 USD | 0.00 USD | 5.25 USD |
| `7D` | `1.28` | 37,910.00 USD | 0.00 USD | 37,910.00 USD | 0.00 USD | 0.00 USD | 363.97 USD |
| `1D` | `1.29` | 4,840.00 USD | 0.00 USD | 4,840.00 USD | 0.00 USD | 0.00 USD | 158.53 USD |
| `7D` | `1.29` | 37,550.00 USD | 0.00 USD | 37,550.00 USD | 0.00 USD | 0.00 USD | 92.20 USD |
| `1D` | `1.29` | 4,680.00 USD | 0.00 USD | 4,680.00 USD | 0.00 USD | 0.00 USD | 137.85 USD |
| `7D` | `1.29` | 37,450.00 USD | 0.00 USD | 37,450.00 USD | 0.00 USD | 0.00 USD | 186.86 USD |
| `1D` | `1.29` | 4,540.00 USD | 0.00 USD | 4,540.00 USD | 0.00 USD | 0.00 USD | 52.55 USD |
| `7D` | `1.30` | 37,270.00 USD | 0.00 USD | 37,270.00 USD | 0.00 USD | 0.00 USD | 1,620.00 USD |
| `7D` | `1.30` | 35,650.00 USD | 0.00 USD | 35,650.00 USD | 0.00 USD | 0.00 USD | 79.07 USD |
| `7D` | `1.31` | 35,570.00 USD | 0.00 USD | 35,570.00 USD | 0.00 USD | 0.00 USD | 440.48 USD |
| `1D` | `1.31` | 4,490.00 USD | 0.00 USD | 4,490.00 USD | 0.00 USD | 0.00 USD | 145.88 USD |
| `7D` | `1.31` | 35,130.00 USD | 0.00 USD | 35,130.00 USD | 0.00 USD | 0.00 USD | 3,190.00 USD |
| `1D` | `1.31` | 4,340.00 USD | 0.00 USD | 4,340.00 USD | 0.00 USD | 0.00 USD | 236.92 USD |
| `7D` | `1.31` | 31,940.00 USD | 0.00 USD | 31,940.00 USD | 0.00 USD | 0.00 USD | 4,690.00 USD |
| `1D` | `1.31` | 4,110.00 USD | 0.00 USD | 4,110.00 USD | 0.00 USD | 0.00 USD | 405.11 USD |
| `7D` | `1.31` | 27,250.00 USD | 0.00 USD | 27,250.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD |
| `1D` | `1.31` | 3,700.00 USD | 0.00 USD | 3,700.00 USD | 0.00 USD | 0.00 USD | 10.50 USD |
| `7D` | `1.31` | 26,140.00 USD | 0.00 USD | 26,140.00 USD | 0.00 USD | 0.00 USD | 715.57 USD |
| `1D` | `1.31` | 3,690.00 USD | 0.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD | 282.23 USD |
| `7D` | `1.31` | 25,430.00 USD | 0.00 USD | 25,430.00 USD | 0.00 USD | 0.00 USD | 209.78 USD |
| `1D` | `1.31` | 3,410.00 USD | 0.00 USD | 3,410.00 USD | 0.00 USD | 0.00 USD | 297.47 USD |
| `7D` | `1.31` | 25,220.00 USD | 0.00 USD | 25,220.00 USD | 0.00 USD | 0.00 USD | 373.72 USD |
| `1D` | `1.31` | 3,110.00 USD | 0.00 USD | 3,110.00 USD | 0.00 USD | 0.00 USD | 118.14 USD |
| `7D` | `1.32` | 24,840.00 USD | 0.00 USD | 24,840.00 USD | 0.00 USD | 0.00 USD | 3,320.00 USD |
| `7D` | `1.32` | 21,530.00 USD | 0.00 USD | 21,530.00 USD | 0.00 USD | 0.00 USD | 770.79 USD |
| `7D` | `1.32` | 20,760.00 USD | 0.00 USD | 20,760.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD |
| `1D` | `1.32` | 2,990.00 USD | 0.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD | 304.93 USD |
| `7D` | `1.32` | 18,130.00 USD | 0.00 USD | 18,130.00 USD | 0.00 USD | 0.00 USD | 6,670.00 USD |
| `1D` | `1.32` | 2,690.00 USD | 0.00 USD | 2,690.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD |
| `7D` | `1.32` | 11,460.00 USD | 0.00 USD | 11,460.00 USD | 0.00 USD | 0.00 USD | 8,460.00 USD |
| `1D` | `1.32` | 1,420.00 USD | 0.00 USD | 1,420.00 USD | 0.00 USD | 0.00 USD | 20.99 USD |
| `7D` | `1.32` | 3,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD | 0.00 USD | 580.88 USD |
| `1D` | `1.32` | 1,400.00 USD | 0.00 USD | 1,400.00 USD | 0.00 USD | 0.00 USD | 457.45 USD |
| `7D` | `1.33` | 2,420.00 USD | 0.00 USD | 2,420.00 USD | 0.00 USD | 0.00 USD | 1,500.00 USD |
| `1D` | `1.33` | 938.27 USD | 0.00 USD | 938.27 USD | 0.00 USD | 0.00 USD | 180.93 USD |
| `7D` | `1.33` | 920.32 USD | 0.00 USD | 920.32 USD | 0.00 USD | 0.00 USD | 721.57 USD |
| `1D` | `1.33` | 757.34 USD | 0.00 USD | 757.34 USD | 0.00 USD | 0.00 USD | 705.37 USD |
| `7D` | `1.33` | 198.75 USD | 0.00 USD | 198.75 USD | 0.00 USD | 0.00 USD | 198.75 USD |
| `1D` | `1.33` | 51.97 USD | 0.00 USD | 51.97 USD | 0.00 USD | 0.00 USD | 51.97 USD |
| `1D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 3,320.00 USD | 3,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,320.00 USD |
| `7D` | `1.34` | 4,090.00 USD | 4,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 770.79 USD |
| `7D` | `1.35` | 6,720.00 USD | 6,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD |
| `1D` | `1.35` | 304.93 USD | 304.93 USD | 0.00 USD | 0.00 USD | 0.00 USD | 304.93 USD |
| `7D` | `1.35` | 13,380.00 USD | 13,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,670.00 USD |
| `1D` | `1.35` | 1,580.00 USD | 1,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD |
| `7D` | `1.35` | 21,850.00 USD | 21,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,460.00 USD |
| `1D` | `1.35` | 1,590.00 USD | 1,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9.31 USD |
| `7D` | `1.35` | 22,330.00 USD | 22,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 485.91 USD |
| `1D` | `1.35` | 1,600.00 USD | 1,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12.66 USD |
| `7D` | `1.35` | 23,900.00 USD | 23,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,570.00 USD |
| `1D` | `1.35` | 2,230.00 USD | 2,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 633.15 USD |
| `7D` | `1.35` | 24,590.00 USD | 24,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 682.94 USD |
| `1D` | `1.35` | 2,940.00 USD | 2,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 709.62 USD |
| `7D` | `1.35` | 24,840.00 USD | 24,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 257.49 USD |
| `1D` | `1.36` | 2,990.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 51.97 USD |
| `7D` | `1.36` | 26,460.00 USD | 26,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,620.00 USD |
| `7D` | `1.36` | 26,540.00 USD | 26,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 79.07 USD |
| `7D` | `1.36` | 26,980.00 USD | 26,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 440.48 USD |
| `1D` | `1.36` | 3,140.00 USD | 3,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 145.88 USD |
| `7D` | `1.36` | 29,820.00 USD | 29,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,830.00 USD |
| `1D` | `1.36` | 3,160.00 USD | 3,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.09 USD |
| `7D` | `1.36` | 34,460.00 USD | 34,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,640.00 USD |
| `1D` | `1.36` | 3,780.00 USD | 3,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 615.94 USD |
| `7D` | `1.36` | 35,930.00 USD | 35,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,470.00 USD |
| `1D` | `1.36` | 3,790.00 USD | 3,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10.50 USD |
| `7D` | `1.36` | 36,110.00 USD | 36,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 185.98 USD |
| `1D` | `1.37` | 4,040.00 USD | 4,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 249.97 USD |
| `7D` | `1.37` | 36,830.00 USD | 36,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 715.50 USD |
| `1D` | `1.37` | 4,310.00 USD | 4,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 271.03 USD |
| `7D` | `1.37` | 37,220.00 USD | 37,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 386.42 USD |
| `1D` | `1.37` | 4,480.00 USD | 4,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 169.13 USD |
| `7D` | `1.37` | 37,270.00 USD | 37,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 50.79 USD |
| `1D` | `1.37` | 4,490.00 USD | 4,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7.71 USD |
| `7D` | `1.38` | 38,080.00 USD | 38,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 810.32 USD |
| `7D` | `1.38` | 38,120.00 USD | 38,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39.55 USD |
| `7D` | `1.39` | 38,290.00 USD | 38,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 172.26 USD |
| `1D` | `1.39` | 4,560.00 USD | 4,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 72.94 USD |
| `7D` | `1.39` | 39,750.00 USD | 39,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `1.39` | 4,570.00 USD | 4,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.04 USD |
| `7D` | `1.39` | 40,730.00 USD | 40,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 980.51 USD |
| `1D` | `1.39` | 4,880.00 USD | 4,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 307.98 USD |
| `7D` | `1.39` | 42,740.00 USD | 42,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,010.00 USD |
| `1D` | `1.39` | 4,890.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.25 USD |
| `7D` | `1.39` | 42,880.00 USD | 42,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 139.71 USD |
| `1D` | `1.39` | 5,010.00 USD | 5,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 118.22 USD |
| `7D` | `1.39` | 43,260.00 USD | 43,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 377.67 USD |
| `1D` | `1.39` | 5,070.00 USD | 5,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 62.61 USD |
| `7D` | `1.39` | 43,450.00 USD | 43,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 193.21 USD |
| `1D` | `1.39` | 5,230.00 USD | 5,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 164.25 USD |
| `7D` | `1.40` | 43,480.00 USD | 43,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25.39 USD |
| `1D` | `1.40` | 5,240.00 USD | 5,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.85 USD |
| `7D` | `1.46` | 43,800.00 USD | 43,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 324.13 USD |
| `7D` | `1.46` | 43,810.00 USD | 43,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10.24 USD |
| `7D` | `1.47` | 43,880.00 USD | 43,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65.91 USD |
| `1D` | `1.47` | 5,270.00 USD | 5,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.18 USD |
| `7D` | `1.47` | 44,460.00 USD | 44,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 581.37 USD |
| `1D` | `1.47` | 5,270.00 USD | 5,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.22 USD |
| `7D` | `1.47` | 44,790.00 USD | 44,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 327.81 USD |
| `1D` | `1.47` | 5,390.00 USD | 5,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 121.74 USD |
| `7D` | `1.47` | 45,450.00 USD | 45,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 667.63 USD |
| `1D` | `1.47` | 5,400.00 USD | 5,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2.10 USD |
| `7D` | `1.47` | 45,500.00 USD | 45,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 40.89 USD |
| `1D` | `1.47` | 5,400.00 USD | 5,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.10 USD |
| `7D` | `1.47` | 45,630.00 USD | 45,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 139.01 USD |
| `1D` | `1.47` | 5,460.00 USD | 5,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 60.76 USD |
| `7D` | `1.47` | 45,660.00 USD | 45,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23.13 USD |
| `1D` | `1.47` | 5,500.00 USD | 5,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 46.11 USD |
| `7D` | `1.48` | 45,710.00 USD | 45,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 54.87 USD |
| `1D` | `1.48` | 5,510.00 USD | 5,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8.10 USD |

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
| **USDT MEXC** | `0.0124%` | **USDT BingX** | `-` |
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
| `10:05:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 588.23 USD | 538.38 USD | 49.85 USD | 488.53 USD | `+83.05%` | `1B / 0S` |
| `10:10:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 538.71 USD | 360.94 USD | 177.78 USD | 183.16 USD | `+34.00%` | `1B / 0S` |
| `10:15:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 663.42 USD | 580.50 USD | 82.93 USD | 497.57 USD | `+75.00%` | `1B / 0S` |
| `10:15:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 2,233.00 USD | 2,121.35 USD | 111.65 USD | 2,009.70 USD | `+90.00%` | `1B / 0S` |
| `10:20:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 867.65 USD | 795.34 USD | 72.30 USD | 723.04 USD | `+83.33%` | `1B / 0S` |
| `10:25:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 701.42 USD | 529.09 USD | 172.33 USD | 356.75 USD | `+50.86%` | `1B / 0S` |
| `10:30:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 1,820.02 USD | 98.38 USD | 1,721.64 USD | -1,623.26 USD | `-89.19%` | `0B / 1S` |
| `10:30:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 686.34 USD | 137.61 USD | 548.73 USD | -411.13 USD | `-59.90%` | `0B / 1S` |
| `10:35:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 524.15 USD | 290.16 USD | 234.00 USD | 56.16 USD | `+10.71%` | `1B / 0S` |
| `10:40:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 609.80 USD | 82.91 USD | 526.89 USD | -443.98 USD | `-72.81%` | `0B / 1S` |

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
  * `2026-10-30 15:50:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.34` (Risk Distance: `0.000880` pts)
  * +2.5R Take Profit: `1.34`
  * Mathematical Lot Sizing: **`0.11 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.34` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.34` (Risk Distance: `0.000880` pts)
  * +2.5R Take Profit: `1.34`
  * Mathematical Lot Sizing: **`0.11 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.35`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
