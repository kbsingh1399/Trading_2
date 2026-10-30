# 🏛️ SOVEREIGN CANDIDATE DOSSIER: EURUSD
**Canonical Key**: `EURUSD` | **Broker Instrument**: `EURUSD.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 17:22:13 IST` (`2026-10-30 11:52:13 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `1.12` | VWAP Z-Score: `+0.52` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000619` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `53.99` (State: `NEUTRAL`)
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
  * Institutional Anchors: EMA-144=`1.12` | EMA-200=`1.12` (Slope: `+0.0374`) | EMA-233=`1.12`
- **Range Boundaries**: 24H High=`1.12` | 24H Low=`1.11` | Weekly High=`1.12` | Weekly Low=`1.11`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.12` (Distance: `-0.07%`)
  * Point of Control (POC) = `1.12` (Distance: `-0.02%`)
  * Value Area Low (VAL) = `1.12` (Distance: `+0.07%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.12` | POC=`1.11` | VAL=`1.11`
  * Prior Day Extremes: PDH=`1.12` | PDL=`1.11` | PDC=`1.12`
  * Monday Range Blueprint: High=`1.12` | Mid=`1.12` | Low=`1.12`
  * Developing Weekly Value Area: Weekly VAH=`1.12` | Weekly POC=`1.11` | Weekly VAL=`1.11`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.12` | Low=`1.12`
  * London Session (08:00-16:00 UTC): High=`1.12` | Low=`1.12`
  * New York Session (13:00-21:00 UTC): High=`1.12` | Low=`1.12`
  * Initial Balance (First Hour): IB High=`1.12` | IB Low=`1.12`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.11` - `1.12`
  * Optimal Trade Entry (OTE 0.705): `1.12`
  * Structural Invalidation Anchor (0.786): `1.13`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `530` | 593.26 USD | -175.28 USD | `-29.55%` | 3,080.93 USD | `-0.72` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `588` | 658.38 USD | 490.13 USD | `+74.44%` | 3,571.06 USD | `+1.46` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `392` | 438.86 USD | -192.00 USD | `-43.75%` | 3,379.06 USD | `-0.74` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `1,617` | 1,811.09 USD | 1,159.10 USD | `+64.00%` | 11,132.08 USD | `+1.62` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `1,766` | 1,976.79 USD | -1,607.63 USD | `-81.33%` | 9,524.45 USD | `-2.27` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `1,479` | 1,655.68 USD | -0.00 USD | `-0.00%` | 9,524.45 USD | `-0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `4,327` | 4,837.50 USD | -2,007.05 USD | `-41.49%` | 4,797.24 USD | `-0.64` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `5,112` | 5,720.38 USD | 4,735.72 USD | `+82.79%` | 9,532.96 USD | `+1.29` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `6,387` | 7,149.99 USD | 945.45 USD | `+13.22%` | 10,478.42 USD | `+0.06` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `6,284` | 7,036.57 USD | 6,332.91 USD | `+90.00%` | 24,991.26 USD | `+0.01` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `15,119` | 16,913.02 USD | -10,827.76 USD | `-64.02%` | 14,163.50 USD | `-0.99` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `18,385` | 20,581.27 USD | 7,828.95 USD | `+38.04%` | 21,992.45 USD | `+0.33` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.12` | `35,597` | 39,738.71 USD | 24,268.79 USD | `+61.07%` | 10,841.45 USD | `+1.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `14,336` | 16,024.64 USD | 7,816.90 USD | `+48.78%` | 18,658.34 USD | `+0.10` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `6,284` | 7,036.57 USD | 6,332.91 USD | `+90.00%` | 24,991.26 USD | `+0.01` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `15,119` | 16,913.02 USD | -10,827.76 USD | `-64.02%` | 14,163.50 USD | `-0.99` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `18,385` | 20,581.27 USD | 7,828.95 USD | `+38.04%` | 21,992.45 USD | `+0.33` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `213` | `0x0911...129a` | `LONG` | 9,965,866.80 USD | `8,898,889.90` | `1.15` | `1.12` | `1.06` | -256,875.62 USD | `-2.58%` | `20X Isolated` |
| `1122` | `0xe03b...ed11` | `SHORT` | 1,950,358.51 USD | `1,741,858.10` | `1.14` | `1.12` | `1.20` | 42,844.81 USD | `+2.20%` | `50X Isolated` |
| `1739` | `0x3f31...a3d7` | `SHORT` | 1,205,585.90 USD | `1,076,512.10` | `1.11` | `1.12` | `1.13` | -5,654.46 USD | `-0.47%` | `50X Isolated` |
| `1846` | `0x9df2...c665` | `SHORT` | 1,119,729.56 USD | `999,937.10` | `1.12` | `1.12` | `1.46` | 840.27 USD | `+0.08%` | `5X Isolated` |
| `2003` | `0x5e91...76ca` | `SHORT` | 1,004,550.30 USD | `897,000.00` | `1.11` | `1.12` | `1.16` | -4,878.49 USD | `-0.49%` | `20X Isolated` |

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
| `7D` | `1.01` | 108,070.00 USD | 0.00 USD | 108,070.00 USD | 0.00 USD | 0.00 USD | 714.18 USD |
| `7D` | `1.01` | 107,360.00 USD | 0.00 USD | 107,360.00 USD | 0.00 USD | 0.00 USD | 1,480.00 USD |
| `1D` | `1.01` | 63,470.00 USD | 0.00 USD | 63,470.00 USD | 0.00 USD | 0.00 USD | 767.97 USD |
| `7D` | `1.01` | 105,880.00 USD | 0.00 USD | 105,880.00 USD | 0.00 USD | 0.00 USD | 782.93 USD |
| `1D` | `1.01` | 62,700.00 USD | 0.00 USD | 62,700.00 USD | 0.00 USD | 0.00 USD | 170.81 USD |
| `7D` | `1.01` | 105,100.00 USD | 0.00 USD | 105,100.00 USD | 0.00 USD | 0.00 USD | 120.88 USD |
| `1D` | `1.01` | 62,530.00 USD | 0.00 USD | 62,530.00 USD | 0.00 USD | 0.00 USD | 43.98 USD |
| `7D` | `1.01` | 104,970.00 USD | 0.00 USD | 104,970.00 USD | 0.00 USD | 0.00 USD | 130.98 USD |
| `7D` | `1.07` | 104,840.00 USD | 0.00 USD | 104,840.00 USD | 0.00 USD | 0.00 USD | 1,030.00 USD |
| `7D` | `1.07` | 103,810.00 USD | 0.00 USD | 103,810.00 USD | 0.00 USD | 0.00 USD | 1,970.00 USD |
| `1D` | `1.07` | 62,490.00 USD | 0.00 USD | 62,490.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `1.07` | 101,840.00 USD | 0.00 USD | 101,840.00 USD | 0.00 USD | 0.00 USD | 3,080.00 USD |
| `1D` | `1.07` | 61,030.00 USD | 0.00 USD | 61,030.00 USD | 0.00 USD | 0.00 USD | 1,620.00 USD |
| `7D` | `1.07` | 98,770.00 USD | 0.00 USD | 98,770.00 USD | 0.00 USD | 0.00 USD | 1,140.00 USD |
| `1D` | `1.07` | 59,410.00 USD | 0.00 USD | 59,410.00 USD | 0.00 USD | 0.00 USD | 541.39 USD |
| `7D` | `1.07` | 97,630.00 USD | 0.00 USD | 97,630.00 USD | 0.00 USD | 0.00 USD | 1,790.00 USD |
| `1D` | `1.08` | 58,870.00 USD | 0.00 USD | 58,870.00 USD | 0.00 USD | 0.00 USD | 2,820.00 USD |
| `7D` | `1.08` | 95,840.00 USD | 0.00 USD | 95,840.00 USD | 0.00 USD | 0.00 USD | 3,540.00 USD |
| `1D` | `1.08` | 56,050.00 USD | 0.00 USD | 56,050.00 USD | 0.00 USD | 0.00 USD | 1,930.00 USD |
| `7D` | `1.08` | 92,300.00 USD | 0.00 USD | 92,300.00 USD | 0.00 USD | 0.00 USD | 2,180.00 USD |
| `1D` | `1.08` | 54,110.00 USD | 0.00 USD | 54,110.00 USD | 0.00 USD | 0.00 USD | 389.69 USD |
| `7D` | `1.08` | 90,110.00 USD | 0.00 USD | 90,110.00 USD | 0.00 USD | 0.00 USD | 409.49 USD |
| `1D` | `1.08` | 53,730.00 USD | 0.00 USD | 53,730.00 USD | 0.00 USD | 0.00 USD | 164.16 USD |
| `7D` | `1.08` | 89,710.00 USD | 0.00 USD | 89,710.00 USD | 0.00 USD | 0.00 USD | 327.44 USD |
| `7D` | `1.09` | 89,380.00 USD | 0.00 USD | 89,380.00 USD | 0.00 USD | 0.00 USD | 5,090.00 USD |
| `1D` | `1.09` | 53,560.00 USD | 0.00 USD | 53,560.00 USD | 0.00 USD | 0.00 USD | 1,550.00 USD |
| `7D` | `1.09` | 84,290.00 USD | 0.00 USD | 84,290.00 USD | 0.00 USD | 0.00 USD | 3,140.00 USD |
| `1D` | `1.09` | 52,010.00 USD | 0.00 USD | 52,010.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `1.10` | 81,150.00 USD | 0.00 USD | 81,150.00 USD | 0.00 USD | 0.00 USD | 5,600.00 USD |
| `1D` | `1.10` | 47,410.00 USD | 0.00 USD | 47,410.00 USD | 0.00 USD | 0.00 USD | 21.72 USD |
| `7D` | `1.10` | 75,550.00 USD | 0.00 USD | 75,550.00 USD | 0.00 USD | 0.00 USD | 1,720.00 USD |
| `1D` | `1.10` | 47,390.00 USD | 0.00 USD | 47,390.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD |
| `7D` | `1.10` | 73,830.00 USD | 0.00 USD | 73,830.00 USD | 0.00 USD | 0.00 USD | 2,450.00 USD |
| `1D` | `1.10` | 46,280.00 USD | 0.00 USD | 46,280.00 USD | 0.00 USD | 0.00 USD | 5,630.00 USD |
| `7D` | `1.10` | 71,380.00 USD | 0.00 USD | 71,380.00 USD | 0.00 USD | 0.00 USD | 8,560.00 USD |
| `1D` | `1.10` | 40,650.00 USD | 0.00 USD | 40,650.00 USD | 0.00 USD | 0.00 USD | 4,290.00 USD |
| `7D` | `1.10` | 62,810.00 USD | 0.00 USD | 62,810.00 USD | 0.00 USD | 0.00 USD | 3,110.00 USD |
| `1D` | `1.10` | 36,360.00 USD | 0.00 USD | 36,360.00 USD | 0.00 USD | 0.00 USD | 514.60 USD |
| `7D` | `1.10` | 59,710.00 USD | 0.00 USD | 59,710.00 USD | 0.00 USD | 0.00 USD | 604.39 USD |
| `1D` | `1.10` | 35,840.00 USD | 0.00 USD | 35,840.00 USD | 0.00 USD | 0.00 USD | 137.39 USD |
| `7D` | `1.10` | 59,100.00 USD | 0.00 USD | 59,100.00 USD | 0.00 USD | 0.00 USD | 654.88 USD |
| `7D` | `1.10` | 58,450.00 USD | 0.00 USD | 58,450.00 USD | 0.00 USD | 0.00 USD | 6,350.00 USD |
| `7D` | `1.10` | 52,100.00 USD | 0.00 USD | 52,100.00 USD | 0.00 USD | 0.00 USD | 5,650.00 USD |
| `1D` | `1.11` | 35,710.00 USD | 0.00 USD | 35,710.00 USD | 0.00 USD | 0.00 USD | 5,830.00 USD |
| `7D` | `1.11` | 46,450.00 USD | 0.00 USD | 46,450.00 USD | 0.00 USD | 0.00 USD | 13,860.00 USD |
| `1D` | `1.11` | 29,870.00 USD | 0.00 USD | 29,870.00 USD | 0.00 USD | 0.00 USD | 6,490.00 USD |
| `7D` | `1.11` | 32,600.00 USD | 0.00 USD | 32,600.00 USD | 0.00 USD | 0.00 USD | 3,710.00 USD |
| `1D` | `1.11` | 23,380.00 USD | 0.00 USD | 23,380.00 USD | 0.00 USD | 0.00 USD | 2,170.00 USD |
| `7D` | `1.11` | 28,880.00 USD | 0.00 USD | 28,880.00 USD | 0.00 USD | 0.00 USD | 6,440.00 USD |
| `1D` | `1.11` | 21,220.00 USD | 0.00 USD | 21,220.00 USD | 0.00 USD | 0.00 USD | 11,270.00 USD |
| `7D` | `1.11` | 22,440.00 USD | 0.00 USD | 22,440.00 USD | 0.00 USD | 0.00 USD | 14,180.00 USD |
| `1D` | `1.11` | 9,950.00 USD | 0.00 USD | 9,950.00 USD | 0.00 USD | 0.00 USD | 7,640.00 USD |
| `7D` | `1.11` | 8,270.00 USD | 0.00 USD | 8,270.00 USD | 0.00 USD | 0.00 USD | 8,270.00 USD |
| `1D` | `1.11` | 2,310.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD | 1,650.00 USD |
| `1D` | `1.11` | 656.65 USD | 0.00 USD | 656.65 USD | 0.00 USD | 0.00 USD | 656.65 USD |
| `1D` | `1.12` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.12` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.13` | 10,870.00 USD | 10,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,870.00 USD |
| `1D` | `1.13` | 3,100.00 USD | 3,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,100.00 USD |
| `7D` | `1.13` | 16,450.00 USD | 16,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,580.00 USD |
| `1D` | `1.13` | 12,320.00 USD | 12,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,220.00 USD |
| `7D` | `1.13` | 27,650.00 USD | 27,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,200.00 USD |
| `1D` | `1.13` | 12,340.00 USD | 12,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15.06 USD |
| `7D` | `1.13` | 31,100.00 USD | 31,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,450.00 USD |
| `1D` | `1.13` | 14,570.00 USD | 14,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,230.00 USD |
| `7D` | `1.13` | 36,010.00 USD | 36,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,910.00 USD |
| `1D` | `1.13` | 25,830.00 USD | 25,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,260.00 USD |
| `7D` | `1.13` | 53,130.00 USD | 53,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,120.00 USD |
| `1D` | `1.13` | 34,400.00 USD | 34,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,580.00 USD |
| `7D` | `1.13` | 59,340.00 USD | 59,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,210.00 USD |
| `1D` | `1.13` | 35,430.00 USD | 35,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,030.00 USD |
| `7D` | `1.13` | 60,550.00 USD | 60,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,210.00 USD |
| `1D` | `1.14` | 35,710.00 USD | 35,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 274.79 USD |
| `7D` | `1.14` | 61,860.00 USD | 61,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD |
| `7D` | `1.14` | 65,550.00 USD | 65,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,690.00 USD |
| `1D` | `1.14` | 37,260.00 USD | 37,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,550.00 USD |
| `7D` | `1.14` | 70,090.00 USD | 70,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,540.00 USD |
| `1D` | `1.14` | 40,460.00 USD | 40,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,200.00 USD |
| `7D` | `1.14` | 75,520.00 USD | 75,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,430.00 USD |
| `1D` | `1.14` | 41,870.00 USD | 41,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,410.00 USD |
| `7D` | `1.14` | 76,640.00 USD | 76,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD |
| `1D` | `1.14` | 42,950.00 USD | 42,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD |
| `7D` | `1.14` | 79,860.00 USD | 79,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,220.00 USD |
| `1D` | `1.14` | 48,590.00 USD | 48,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,630.00 USD |
| `7D` | `1.14` | 86,950.00 USD | 86,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,090.00 USD |
| `1D` | `1.14` | 52,410.00 USD | 52,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,820.00 USD |
| `7D` | `1.14` | 91,320.00 USD | 91,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,370.00 USD |
| `1D` | `1.15` | 53,210.00 USD | 53,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 802.63 USD |
| `7D` | `1.15` | 91,990.00 USD | 91,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 674.99 USD |
| `1D` | `1.15` | 53,560.00 USD | 53,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 350.63 USD |
| `7D` | `1.15` | 92,790.00 USD | 92,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 798.87 USD |
| `7D` | `1.16` | 93,220.00 USD | 93,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 426.21 USD |
| `7D` | `1.16` | 95,510.00 USD | 95,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,290.00 USD |
| `1D` | `1.16` | 54,340.00 USD | 54,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 776.05 USD |
| `7D` | `1.16` | 96,900.00 USD | 96,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,400.00 USD |
| `1D` | `1.16` | 56,640.00 USD | 56,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,300.00 USD |
| `7D` | `1.16` | 99,700.00 USD | 99,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,800.00 USD |
| `1D` | `1.16` | 56,650.00 USD | 56,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.76 USD |
| `7D` | `1.16` | 100,570.00 USD | 100,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 861.73 USD |
| `1D` | `1.16` | 57,200.00 USD | 57,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 558.28 USD |
| `7D` | `1.16` | 101,790.00 USD | 101,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,230.00 USD |
| `1D` | `1.17` | 60,020.00 USD | 60,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,810.00 USD |
| `7D` | `1.17` | 106,070.00 USD | 106,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,280.00 USD |
| `1D` | `1.17` | 62,070.00 USD | 62,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,050.00 USD |
| `7D` | `1.17` | 107,630.00 USD | 107,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,550.00 USD |
| `1D` | `1.17` | 62,380.00 USD | 62,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 310.64 USD |
| `7D` | `1.17` | 107,930.00 USD | 107,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 302.20 USD |
| `1D` | `1.17` | 62,490.00 USD | 62,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 109.98 USD |
| `7D` | `1.17` | 108,260.00 USD | 108,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 327.44 USD |
| `7D` | `1.23` | 108,580.00 USD | 108,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 319.40 USD |
| `7D` | `1.23` | 109,450.00 USD | 109,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 874.39 USD |
| `1D` | `1.23` | 63,070.00 USD | 63,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 583.46 USD |
| `7D` | `1.23` | 109,900.00 USD | 109,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 445.30 USD |
| `1D` | `1.23` | 63,720.00 USD | 63,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 646.87 USD |
| `7D` | `1.23` | 111,130.00 USD | 111,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240.00 USD |
| `1D` | `1.23` | 63,720.00 USD | 63,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1.51 USD |
| `7D` | `1.23` | 111,360.00 USD | 111,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 227.96 USD |
| `1D` | `1.23` | 63,940.00 USD | 63,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 216.89 USD |
| `7D` | `1.23` | 111,850.00 USD | 111,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 490.93 USD |
| `1D` | `1.23` | 65,060.00 USD | 65,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD |
| `7D` | `1.23` | 113,560.00 USD | 113,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,710.00 USD |
| `1D` | `1.23` | 65,820.00 USD | 65,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 766.14 USD |
| `7D` | `1.23` | 114,110.00 USD | 114,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 554.23 USD |
| `1D` | `1.24` | 65,970.00 USD | 65,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 149.14 USD |
| `1D` | `1.24` | 66,020.00 USD | 66,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 52.31 USD |
| `7D` | `1.24` | 114,230.00 USD | 114,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 120.88 USD |
| `7D` | `1.24` | 114,360.00 USD | 114,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 130.98 USD |

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
  * Current Rate: `617.19` | Last 24h: `658.59` | Last 3d: `761.48` | Last 7d: `828.22`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0775%` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `0.0000%` | **USDT Bitget** | `-0.0492%` |
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
  * `2026-10-30 16:36:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:03 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:49:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.12` (Risk Distance: `0.000758` pts)
  * +2.5R Take Profit: `1.12`
  * Mathematical Lot Sizing: **`0.13 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.12` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.12` (Risk Distance: `0.000758` pts)
  * +2.5R Take Profit: `1.12`
  * Mathematical Lot Sizing: **`0.13 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.13`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
