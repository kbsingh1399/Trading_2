# 🏛️ SOVEREIGN CANDIDATE DOSSIER: EURUSD
**Canonical Key**: `EURUSD` | **Broker Instrument**: `EURUSD.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 08:48:56 IST` (`2026-10-30 03:18:56 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.12` | **Live Ask Quote**: `1.12` | **Mid Price**: `1.12`
- **Spread Points**: `1.00` | **Spread BPS**: `0.09 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `1.12` | VWAP Z-Score: `-0.19` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000630` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `59.68` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.12` | Lower -3.00σ Band: `1.12`
  * Upper +2.51σ Band: `1.12` | Lower -2.51σ Band: `1.12`
  * Upper +2.01σ Band: `1.12` | Lower -2.01σ Band: `1.12`
  * Upper +2.00σ Band: `1.12` | Lower -2.00σ Band: `1.12`
  * Upper +1.28σ Band: `1.12` | Lower -1.28σ Band: `1.12`
  * Upper +1.00σ Band: `1.12` | Lower -1.00σ Band: `1.12`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.12` | EMA-20=`1.12` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.12` (Slope: `+0.0000`) | EMA-100=`1.12`
  * Institutional Anchors: EMA-144=`1.12` | EMA-200=`1.12` (Slope: `+0.0456`) | EMA-233=`1.12`
- **Range Boundaries**: 24H High=`1.12` | 24H Low=`1.11` | Weekly High=`1.12` | Weekly Low=`1.11`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.12` (Distance: `-0.02%`)
  * Point of Control (POC) = `1.12` (Distance: `+0.03%`)
  * Value Area Low (VAL) = `1.12` (Distance: `+0.14%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.12` | POC=`1.11` | VAL=`1.11`
  * Prior Day Extremes: PDH=`1.12` | PDL=`1.11` | PDC=`1.12`
  * Monday Range Blueprint: High=`1.12` | Mid=`1.12` | Low=`1.12`
  * Developing Weekly Value Area: Weekly VAH=`1.12` | Weekly POC=`1.11` | Weekly VAL=`1.11`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.12` | Low=`1.12`
  * London Session (08:00-16:00 UTC): High=`1.12` | Low=`1.12`
  * New York Session (13:00-21:00 UTC): High=`1.13` | Low=`1.11`
  * Initial Balance (First Hour): IB High=`1.12` | IB Low=`1.12`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.12` - `1.12`
  * Optimal Trade Entry (OTE 0.705): `1.12`
  * Structural Invalidation Anchor (0.786): `1.13`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `197` | 220.29 USD | -67.05 USD | `-30.43%` | 2,772.14 USD | `-0.72` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `279` | 311.97 USD | -187.18 USD | `-60.00%` | 2,584.95 USD | `-1.87` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `224` | 250.50 USD | 125.25 USD | `+50.00%` | 2,710.20 USD | `+1.40` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `365` | 408.16 USD | -317.05 USD | `-77.68%` | 8,356.98 USD | `-0.87` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `409` | 457.36 USD | -89.48 USD | `-19.57%` | 8,267.50 USD | `-0.41` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `774` | 865.70 USD | 585.15 USD | `+67.59%` | 8,852.65 USD | `+1.03` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `1,198` | 1,340.67 USD | 1,174.15 USD | `+87.58%` | 9,101.20 USD | `+0.23` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `1,418` | 1,585.66 USD | -1,308.92 USD | `-82.55%` | 7,792.28 USD | `-0.57` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `3,467` | 3,882.21 USD | 3,493.99 USD | `+90.00%` | 11,286.26 USD | `+0.89` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.12` | `35,597` | 39,738.71 USD | 24,268.79 USD | `+61.07%` | 6,924.90 USD | `+1.62` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `14,336` | 16,024.64 USD | 7,816.90 USD | `+48.78%` | 14,741.79 USD | `+0.38` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `6,284` | 7,036.57 USD | 6,332.91 USD | `+90.00%` | 21,074.71 USD | `+0.24` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.11` | `15,359` | 17,108.39 USD | -3,758.66 USD | `-21.97%` | -3,916.55 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.11` | `19,887` | 22,130.25 USD | -13,427.34 USD | `-60.67%` | -17,343.90 USD | `-1.36` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.12` | `35,597` | 39,738.71 USD | 24,268.79 USD | `+61.07%` | 6,924.90 USD | `+1.62` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `14,336` | 16,024.64 USD | 7,816.90 USD | `+48.78%` | 14,741.79 USD | `+0.38` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `6,284` | 7,036.57 USD | 6,332.91 USD | `+90.00%` | 21,074.71 USD | `+0.24` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `213` | `0x0911...129a` | `LONG` | 9,969,426.36 USD | `8,898,889.90` | `1.15` | `1.12` | `1.06` | -253,316.07 USD | `-2.54%` | `20X Isolated` |
| `1112` | `0xe03b...ed11` | `SHORT` | 1,951,403.63 USD | `1,741,858.10` | `1.14` | `1.12` | `1.20` | 41,799.69 USD | `+2.14%` | `50X Isolated` |
| `1712` | `0x3f31...a3d7` | `SHORT` | 1,206,124.16 USD | `1,076,512.10` | `1.11` | `1.12` | `1.13` | -6,192.71 USD | `-0.51%` | `50X Isolated` |
| `1818` | `0x9df2...c665` | `SHORT` | 1,120,229.53 USD | `999,937.10` | `1.12` | `1.12` | `1.46` | 340.30 USD | `+0.03%` | `5X Isolated` |

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
| `7D` | `1.00` | 104,400.00 USD | 0.00 USD | 104,400.00 USD | 0.00 USD | 0.00 USD | 916.19 USD |
| `7D` | `1.00` | 103,480.00 USD | 0.00 USD | 103,480.00 USD | 0.00 USD | 0.00 USD | 552.32 USD |
| `7D` | `1.01` | 102,930.00 USD | 0.00 USD | 102,930.00 USD | 0.00 USD | 0.00 USD | 1,290.00 USD |
| `7D` | `1.01` | 101,640.00 USD | 0.00 USD | 101,640.00 USD | 0.00 USD | 0.00 USD | 835.18 USD |
| `1D` | `1.01` | 29,010.00 USD | 0.00 USD | 29,010.00 USD | 0.00 USD | 0.00 USD | 211.33 USD |
| `7D` | `1.01` | 100,810.00 USD | 0.00 USD | 100,810.00 USD | 0.00 USD | 0.00 USD | 122.77 USD |
| `1D` | `1.01` | 28,800.00 USD | 0.00 USD | 28,800.00 USD | 0.00 USD | 0.00 USD | 2.95 USD |
| `7D` | `1.01` | 100,680.00 USD | 0.00 USD | 100,680.00 USD | 0.00 USD | 0.00 USD | 1,200.00 USD |
| `7D` | `1.01` | 99,480.00 USD | 0.00 USD | 99,480.00 USD | 0.00 USD | 0.00 USD | 417.41 USD |
| `7D` | `1.01` | 99,070.00 USD | 0.00 USD | 99,070.00 USD | 0.00 USD | 0.00 USD | 294.24 USD |
| `7D` | `1.07` | 98,770.00 USD | 0.00 USD | 98,770.00 USD | 0.00 USD | 0.00 USD | 2,520.00 USD |
| `1D` | `1.07` | 28,800.00 USD | 0.00 USD | 28,800.00 USD | 0.00 USD | 0.00 USD | 1,480.00 USD |
| `7D` | `1.07` | 96,250.00 USD | 0.00 USD | 96,250.00 USD | 0.00 USD | 0.00 USD | 2,040.00 USD |
| `1D` | `1.07` | 27,320.00 USD | 0.00 USD | 27,320.00 USD | 0.00 USD | 0.00 USD | 2,090.00 USD |
| `7D` | `1.07` | 94,220.00 USD | 0.00 USD | 94,220.00 USD | 0.00 USD | 0.00 USD | 2,360.00 USD |
| `1D` | `1.07` | 25,230.00 USD | 0.00 USD | 25,230.00 USD | 0.00 USD | 0.00 USD | 15.01 USD |
| `7D` | `1.07` | 91,860.00 USD | 0.00 USD | 91,860.00 USD | 0.00 USD | 0.00 USD | 2,090.00 USD |
| `1D` | `1.08` | 25,220.00 USD | 0.00 USD | 25,220.00 USD | 0.00 USD | 0.00 USD | 524.48 USD |
| `7D` | `1.08` | 89,770.00 USD | 0.00 USD | 89,770.00 USD | 0.00 USD | 0.00 USD | 306.93 USD |
| `1D` | `1.08` | 24,690.00 USD | 0.00 USD | 24,690.00 USD | 0.00 USD | 0.00 USD | 7.37 USD |
| `7D` | `1.08` | 89,460.00 USD | 0.00 USD | 89,460.00 USD | 0.00 USD | 0.00 USD | 3,110.00 USD |
| `7D` | `1.08` | 86,360.00 USD | 0.00 USD | 86,360.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD |
| `7D` | `1.08` | 85,050.00 USD | 0.00 USD | 85,050.00 USD | 0.00 USD | 0.00 USD | 807.58 USD |
| `7D` | `1.09` | 84,240.00 USD | 0.00 USD | 84,240.00 USD | 0.00 USD | 0.00 USD | 1,670.00 USD |
| `1D` | `1.09` | 24,680.00 USD | 0.00 USD | 24,680.00 USD | 0.00 USD | 0.00 USD | 1,550.00 USD |
| `7D` | `1.09` | 82,580.00 USD | 0.00 USD | 82,580.00 USD | 0.00 USD | 0.00 USD | 5,630.00 USD |
| `1D` | `1.09` | 23,130.00 USD | 0.00 USD | 23,130.00 USD | 0.00 USD | 0.00 USD | 3,320.00 USD |
| `7D` | `1.09` | 76,940.00 USD | 0.00 USD | 76,940.00 USD | 0.00 USD | 0.00 USD | 4,170.00 USD |
| `1D` | `1.10` | 19,820.00 USD | 0.00 USD | 19,820.00 USD | 0.00 USD | 0.00 USD | 2,290.00 USD |
| `7D` | `1.10` | 72,770.00 USD | 0.00 USD | 72,770.00 USD | 0.00 USD | 0.00 USD | 4,080.00 USD |
| `1D` | `1.10` | 17,530.00 USD | 0.00 USD | 17,530.00 USD | 0.00 USD | 0.00 USD | 1,060.00 USD |
| `7D` | `1.10` | 68,690.00 USD | 0.00 USD | 68,690.00 USD | 0.00 USD | 0.00 USD | 2,450.00 USD |
| `1D` | `1.10` | 16,470.00 USD | 0.00 USD | 16,470.00 USD | 0.00 USD | 0.00 USD | 14.76 USD |
| `7D` | `1.10` | 66,240.00 USD | 0.00 USD | 66,240.00 USD | 0.00 USD | 0.00 USD | 1,130.00 USD |
| `7D` | `1.10` | 65,110.00 USD | 0.00 USD | 65,110.00 USD | 0.00 USD | 0.00 USD | 6,910.00 USD |
| `7D` | `1.10` | 58,200.00 USD | 0.00 USD | 58,200.00 USD | 0.00 USD | 0.00 USD | 1,550.00 USD |
| `7D` | `1.10` | 56,650.00 USD | 0.00 USD | 56,650.00 USD | 0.00 USD | 0.00 USD | 1,470.00 USD |
| `7D` | `1.10` | 55,180.00 USD | 0.00 USD | 55,180.00 USD | 0.00 USD | 0.00 USD | 10,230.00 USD |
| `1D` | `1.11` | 16,460.00 USD | 0.00 USD | 16,460.00 USD | 0.00 USD | 0.00 USD | 5,900.00 USD |
| `7D` | `1.11` | 44,950.00 USD | 0.00 USD | 44,950.00 USD | 0.00 USD | 0.00 USD | 12,540.00 USD |
| `1D` | `1.11` | 10,550.00 USD | 0.00 USD | 10,550.00 USD | 0.00 USD | 0.00 USD | 8,370.00 USD |
| `7D` | `1.11` | 32,410.00 USD | 0.00 USD | 32,410.00 USD | 0.00 USD | 0.00 USD | 6,100.00 USD |
| `1D` | `1.11` | 2,190.00 USD | 0.00 USD | 2,190.00 USD | 0.00 USD | 0.00 USD | 60.05 USD |
| `7D` | `1.11` | 26,310.00 USD | 0.00 USD | 26,310.00 USD | 0.00 USD | 0.00 USD | 7,140.00 USD |
| `1D` | `1.11` | 2,130.00 USD | 0.00 USD | 2,130.00 USD | 0.00 USD | 0.00 USD | 2,100.00 USD |
| `7D` | `1.11` | 19,180.00 USD | 0.00 USD | 19,180.00 USD | 0.00 USD | 0.00 USD | 1,230.00 USD |
| `1D` | `1.11` | 29.51 USD | 0.00 USD | 29.51 USD | 0.00 USD | 0.00 USD | 29.51 USD |
| `7D` | `1.11` | 17,950.00 USD | 0.00 USD | 17,950.00 USD | 0.00 USD | 0.00 USD | 10,640.00 USD |
| `7D` | `1.11` | 7,310.00 USD | 0.00 USD | 7,310.00 USD | 0.00 USD | 0.00 USD | 7,020.00 USD |
| `7D` | `1.11` | 287.93 USD | 0.00 USD | 287.93 USD | 0.00 USD | 0.00 USD | 287.93 USD |
| `1D` | `1.12` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.12` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.13` | 7,170.00 USD | 7,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,170.00 USD |
| `1D` | `1.13` | 3,100.00 USD | 3,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,100.00 USD |
| `7D` | `1.13` | 14,600.00 USD | 14,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,430.00 USD |
| `1D` | `1.13` | 12,610.00 USD | 12,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,500.00 USD |
| `7D` | `1.13` | 24,310.00 USD | 24,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,710.00 USD |
| `1D` | `1.13` | 14,310.00 USD | 14,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,710.00 USD |
| `7D` | `1.13` | 31,100.00 USD | 31,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,790.00 USD |
| `1D` | `1.13` | 16,430.00 USD | 16,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,110.00 USD |
| `7D` | `1.13` | 36,000.00 USD | 36,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,910.00 USD |
| `1D` | `1.13` | 16,460.00 USD | 16,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.51 USD |
| `7D` | `1.13` | 38,260.00 USD | 38,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,250.00 USD |
| `7D` | `1.13` | 52,080.00 USD | 52,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,820.00 USD |
| `7D` | `1.13` | 55,180.00 USD | 55,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,100.00 USD |
| `7D` | `1.14` | 58,120.00 USD | 58,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD |
| `7D` | `1.14` | 58,530.00 USD | 58,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 406.66 USD |
| `7D` | `1.14` | 63,240.00 USD | 63,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,710.00 USD |
| `1D` | `1.14` | 19,480.00 USD | 19,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `1.14` | 69,590.00 USD | 69,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,350.00 USD |
| `1D` | `1.14` | 23,590.00 USD | 23,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,110.00 USD |
| `7D` | `1.14` | 72,560.00 USD | 72,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,970.00 USD |
| `1D` | `1.14` | 23,620.00 USD | 23,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 30.03 USD |
| `7D` | `1.14` | 76,120.00 USD | 76,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,570.00 USD |
| `1D` | `1.14` | 24,670.00 USD | 24,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,050.00 USD |
| `7D` | `1.14` | 76,740.00 USD | 76,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 613.86 USD |
| `1D` | `1.14` | 24,680.00 USD | 24,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14.76 USD |
| `7D` | `1.14` | 82,060.00 USD | 82,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,320.00 USD |
| `7D` | `1.15` | 85,460.00 USD | 85,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,410.00 USD |
| `7D` | `1.15` | 87,180.00 USD | 87,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,720.00 USD |
| `7D` | `1.16` | 89,080.00 USD | 89,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,900.00 USD |
| `1D` | `1.16` | 25,460.00 USD | 25,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 776.05 USD |
| `7D` | `1.16` | 90,870.00 USD | 90,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,790.00 USD |
| `1D` | `1.16` | 27,840.00 USD | 27,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,380.00 USD |
| `7D` | `1.16` | 93,260.00 USD | 93,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,390.00 USD |
| `1D` | `1.16` | 28,260.00 USD | 28,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 420.25 USD |
| `7D` | `1.16` | 94,960.00 USD | 94,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,700.00 USD |
| `1D` | `1.16` | 28,790.00 USD | 28,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 528.64 USD |
| `7D` | `1.16` | 96,180.00 USD | 96,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,230.00 USD |
| `1D` | `1.17` | 28,800.00 USD | 28,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7.37 USD |
| `7D` | `1.17` | 96,750.00 USD | 96,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 563.48 USD |
| `7D` | `1.17` | 100,010.00 USD | 100,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,260.00 USD |
| `7D` | `1.17` | 100,980.00 USD | 100,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 970.54 USD |
| `7D` | `1.17` | 101,710.00 USD | 101,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 735.60 USD |
| `7D` | `1.23` | 102,720.00 USD | 102,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,010.00 USD |
| `1D` | `1.23` | 29,110.00 USD | 29,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 311.82 USD |
| `7D` | `1.23` | 103,180.00 USD | 103,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 460.89 USD |
| `1D` | `1.23` | 30,060.00 USD | 30,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 950.72 USD |
| `7D` | `1.23` | 104,450.00 USD | 104,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD |
| `1D` | `1.23` | 30,230.00 USD | 30,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 165.39 USD |
| `7D` | `1.23` | 104,820.00 USD | 104,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 366.17 USD |
| `1D` | `1.23` | 30,440.00 USD | 30,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 211.33 USD |
| `7D` | `1.23` | 105,310.00 USD | 105,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 490.53 USD |
| `1D` | `1.23` | 30,440.00 USD | 30,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2.95 USD |
| `7D` | `1.23` | 105,450.00 USD | 105,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 141.49 USD |
| `7D` | `1.23` | 106,630.00 USD | 106,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,180.00 USD |
| `7D` | `1.23` | 106,910.00 USD | 106,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 279.59 USD |

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
  * Current Rate: `0.00` | Last 24h: `95.44` | Last 3d: `198.32` | Last 7d: `265.06`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0000%` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `0.0000%` | **USDT Bitget** | `-0.0472%` |
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
| 15m Bar | Interbank Tick Flow | - | - | - | - | - | - | - | - | 0.00% | Balanced Interbank Imbalance |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| Live | 15m | Tape Flow | NEUTRAL | Orderflow balanced at current level | - | 0.00 USD | 0.00 USD |

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
  * `2026-10-30 08:34:38 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:38 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:00:38 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:35:38 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:36:38 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:36:38 IST`: [investinglive.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1.12` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1.12` (Risk Distance: `0.000771` pts)
  * +2.5R Take Profit: `1.12`
  * Mathematical Lot Sizing: **`0.12 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.12` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.12` (Risk Distance: `0.000771` pts)
  * +2.5R Take Profit: `1.12`
  * Mathematical Lot Sizing: **`0.12 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.13`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
