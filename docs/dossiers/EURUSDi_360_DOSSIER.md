# 🏛️ SOVEREIGN CANDIDATE DOSSIER: EURUSD
**Canonical Key**: `EURUSD` | **Broker Instrument**: `EURUSD.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 14:23:36 IST` (`2026-10-30 08:53:36 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `1.12` | VWAP Z-Score: `+0.12` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000648` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `54.57` (State: `NEUTRAL`)
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
  * Institutional Anchors: EMA-144=`1.12` | EMA-200=`1.12` (Slope: `+0.0303`) | EMA-233=`1.12`
- **Range Boundaries**: 24H High=`1.12` | 24H Low=`1.11` | Weekly High=`1.12` | Weekly Low=`1.11`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.12` (Distance: `-0.02%`)
  * Point of Control (POC) = `1.12` (Distance: `+0.10%`)
  * Value Area Low (VAL) = `1.12` (Distance: `+0.12%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `1.11` - `1.12`
  * Optimal Trade Entry (OTE 0.705): `1.12`
  * Structural Invalidation Anchor (0.786): `1.13`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `361` | 403.71 USD | -50.46 USD | `-12.50%` | 1,921.11 USD | `-0.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `237` | 265.03 USD | -66.26 USD | `-25.00%` | 1,854.85 USD | `-0.34` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `204` | 228.15 USD | 126.08 USD | `+55.26%` | 1,980.93 USD | `+1.91` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `562` | 628.63 USD | -143.69 USD | `-22.86%` | 8,222.91 USD | `-0.17` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `537` | 600.54 USD | -133.45 USD | `-22.22%` | 8,089.46 USD | `-0.12` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `802` | 896.92 USD | 358.77 USD | `+40.00%` | 8,448.23 USD | `+0.57` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `3,059` | 3,423.27 USD | -1,654.58 USD | `-48.33%` | 10,066.30 USD | `-0.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `1,712` | 1,915.15 USD | -1,141.72 USD | `-59.62%` | 8,924.57 USD | `-0.45` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `2,559` | 2,862.14 USD | -224.88 USD | `-7.86%` | 8,699.69 USD | `-0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `6,284` | 7,036.57 USD | 6,332.91 USD | `+90.00%` | 24,991.26 USD | `+0.01` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `15,119` | 16,913.02 USD | -10,827.76 USD | `-64.02%` | 14,163.50 USD | `-0.99` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `16,460` | 18,426.31 USD | 7,009.22 USD | `+38.04%` | 21,172.72 USD | `+0.27` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.12` | `35,597` | 39,738.71 USD | 24,268.79 USD | `+61.07%` | 10,841.45 USD | `+1.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `14,336` | 16,024.64 USD | 7,816.90 USD | `+48.78%` | 18,658.34 USD | `+0.10` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `6,284` | 7,036.57 USD | 6,332.91 USD | `+90.00%` | 24,991.26 USD | `+0.01` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `15,119` | 16,913.02 USD | -10,827.76 USD | `-64.02%` | 14,163.50 USD | `-0.99` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `16,460` | 18,426.31 USD | 7,009.22 USD | `+38.04%` | 21,172.72 USD | `+0.27` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `217` | `0x0911...129a` | `LONG` | 9,964,976.91 USD | `8,898,889.90` | `1.15` | `1.12` | `1.06` | -257,765.51 USD | `-2.59%` | `20X Isolated` |
| `1136` | `0xe03b...ed11` | `SHORT` | 1,950,532.70 USD | `1,741,858.10` | `1.14` | `1.12` | `1.20` | 42,670.62 USD | `+2.19%` | `50X Isolated` |
| `1752` | `0x3f31...a3d7` | `SHORT` | 1,205,585.90 USD | `1,076,512.10` | `1.11` | `1.12` | `1.13` | -5,654.46 USD | `-0.47%` | `50X Isolated` |
| `1847` | `0x9df2...c665` | `SHORT` | 1,119,829.56 USD | `999,937.10` | `1.12` | `1.12` | `1.46` | 740.28 USD | `+0.07%` | `5X Isolated` |

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
| `7D` | `1.01` | 111,430.00 USD | 0.00 USD | 111,430.00 USD | 0.00 USD | 0.00 USD | 560.68 USD |
| `1D` | `1.01` | 63,030.00 USD | 0.00 USD | 63,030.00 USD | 0.00 USD | 0.00 USD | 1,320.00 USD |
| `7D` | `1.01` | 110,870.00 USD | 0.00 USD | 110,870.00 USD | 0.00 USD | 0.00 USD | 1,360.00 USD |
| `1D` | `1.01` | 61,710.00 USD | 0.00 USD | 61,710.00 USD | 0.00 USD | 0.00 USD | 714.10 USD |
| `7D` | `1.01` | 109,500.00 USD | 0.00 USD | 109,500.00 USD | 0.00 USD | 0.00 USD | 898.29 USD |
| `1D` | `1.01` | 61,000.00 USD | 0.00 USD | 61,000.00 USD | 0.00 USD | 0.00 USD | 109.52 USD |
| `7D` | `1.01` | 108,600.00 USD | 0.00 USD | 108,600.00 USD | 0.00 USD | 0.00 USD | 163.80 USD |
| `1D` | `1.01` | 60,890.00 USD | 0.00 USD | 60,890.00 USD | 0.00 USD | 0.00 USD | 69.13 USD |
| `7D` | `1.01` | 108,440.00 USD | 0.00 USD | 108,440.00 USD | 0.00 USD | 0.00 USD | 130.96 USD |
| `7D` | `1.07` | 108,310.00 USD | 0.00 USD | 108,310.00 USD | 0.00 USD | 0.00 USD | 460.25 USD |
| `7D` | `1.07` | 107,850.00 USD | 0.00 USD | 107,850.00 USD | 0.00 USD | 0.00 USD | 2,100.00 USD |
| `1D` | `1.07` | 60,820.00 USD | 0.00 USD | 60,820.00 USD | 0.00 USD | 0.00 USD | 779.56 USD |
| `7D` | `1.07` | 105,750.00 USD | 0.00 USD | 105,750.00 USD | 0.00 USD | 0.00 USD | 3,180.00 USD |
| `1D` | `1.07` | 60,040.00 USD | 0.00 USD | 60,040.00 USD | 0.00 USD | 0.00 USD | 2,330.00 USD |
| `7D` | `1.07` | 102,580.00 USD | 0.00 USD | 102,580.00 USD | 0.00 USD | 0.00 USD | 2,040.00 USD |
| `1D` | `1.07` | 57,710.00 USD | 0.00 USD | 57,710.00 USD | 0.00 USD | 0.00 USD | 3.76 USD |
| `7D` | `1.07` | 100,530.00 USD | 0.00 USD | 100,530.00 USD | 0.00 USD | 0.00 USD | 1,230.00 USD |
| `1D` | `1.07` | 57,710.00 USD | 0.00 USD | 57,710.00 USD | 0.00 USD | 0.00 USD | 3,320.00 USD |
| `7D` | `1.08` | 99,310.00 USD | 0.00 USD | 99,310.00 USD | 0.00 USD | 0.00 USD | 3,430.00 USD |
| `1D` | `1.08` | 54,400.00 USD | 0.00 USD | 54,400.00 USD | 0.00 USD | 0.00 USD | 1,810.00 USD |
| `7D` | `1.08` | 95,880.00 USD | 0.00 USD | 95,880.00 USD | 0.00 USD | 0.00 USD | 2,370.00 USD |
| `1D` | `1.08` | 52,580.00 USD | 0.00 USD | 52,580.00 USD | 0.00 USD | 0.00 USD | 278.36 USD |
| `7D` | `1.08` | 93,510.00 USD | 0.00 USD | 93,510.00 USD | 0.00 USD | 0.00 USD | 533.13 USD |
| `1D` | `1.08` | 52,310.00 USD | 0.00 USD | 52,310.00 USD | 0.00 USD | 0.00 USD | 172.86 USD |
| `7D` | `1.08` | 92,980.00 USD | 0.00 USD | 92,980.00 USD | 0.00 USD | 0.00 USD | 327.41 USD |
| `7D` | `1.09` | 92,650.00 USD | 0.00 USD | 92,650.00 USD | 0.00 USD | 0.00 USD | 4,580.00 USD |
| `7D` | `1.09` | 88,070.00 USD | 0.00 USD | 88,070.00 USD | 0.00 USD | 0.00 USD | 2,790.00 USD |
| `1D` | `1.09` | 52,130.00 USD | 0.00 USD | 52,130.00 USD | 0.00 USD | 0.00 USD | 2,930.00 USD |
| `7D` | `1.10` | 85,280.00 USD | 0.00 USD | 85,280.00 USD | 0.00 USD | 0.00 USD | 6,350.00 USD |
| `1D` | `1.10` | 49,200.00 USD | 0.00 USD | 49,200.00 USD | 0.00 USD | 0.00 USD | 3,280.00 USD |
| `7D` | `1.10` | 78,930.00 USD | 0.00 USD | 78,930.00 USD | 0.00 USD | 0.00 USD | 4,280.00 USD |
| `1D` | `1.10` | 45,920.00 USD | 0.00 USD | 45,920.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD |
| `1D` | `1.10` | 44,840.00 USD | 0.00 USD | 44,840.00 USD | 0.00 USD | 0.00 USD | 5,630.00 USD |
| `7D` | `1.10` | 74,650.00 USD | 0.00 USD | 74,650.00 USD | 0.00 USD | 0.00 USD | 9,400.00 USD |
| `1D` | `1.10` | 39,200.00 USD | 0.00 USD | 39,200.00 USD | 0.00 USD | 0.00 USD | 3,760.00 USD |
| `7D` | `1.10` | 65,250.00 USD | 0.00 USD | 65,250.00 USD | 0.00 USD | 0.00 USD | 2,920.00 USD |
| `1D` | `1.10` | 35,450.00 USD | 0.00 USD | 35,450.00 USD | 0.00 USD | 0.00 USD | 445.70 USD |
| `7D` | `1.10` | 62,330.00 USD | 0.00 USD | 62,330.00 USD | 0.00 USD | 0.00 USD | 340.94 USD |
| `1D` | `1.10` | 35,000.00 USD | 0.00 USD | 35,000.00 USD | 0.00 USD | 0.00 USD | 245.76 USD |
| `7D` | `1.10` | 61,980.00 USD | 0.00 USD | 61,980.00 USD | 0.00 USD | 0.00 USD | 654.82 USD |
| `7D` | `1.10` | 61,330.00 USD | 0.00 USD | 61,330.00 USD | 0.00 USD | 0.00 USD | 3,330.00 USD |
| `7D` | `1.10` | 58,000.00 USD | 0.00 USD | 58,000.00 USD | 0.00 USD | 0.00 USD | 11,270.00 USD |
| `1D` | `1.10` | 34,750.00 USD | 0.00 USD | 34,750.00 USD | 0.00 USD | 0.00 USD | 5,870.00 USD |
| `7D` | `1.11` | 46,730.00 USD | 0.00 USD | 46,730.00 USD | 0.00 USD | 0.00 USD | 9,710.00 USD |
| `1D` | `1.11` | 28,890.00 USD | 0.00 USD | 28,890.00 USD | 0.00 USD | 0.00 USD | 6,560.00 USD |
| `7D` | `1.11` | 37,020.00 USD | 0.00 USD | 37,020.00 USD | 0.00 USD | 0.00 USD | 6,790.00 USD |
| `1D` | `1.11` | 22,330.00 USD | 0.00 USD | 22,330.00 USD | 0.00 USD | 0.00 USD | 15.06 USD |
| `7D` | `1.11` | 30,230.00 USD | 0.00 USD | 30,230.00 USD | 0.00 USD | 0.00 USD | 4,910.00 USD |
| `1D` | `1.11` | 22,310.00 USD | 0.00 USD | 22,310.00 USD | 0.00 USD | 0.00 USD | 13,260.00 USD |
| `7D` | `1.11` | 25,330.00 USD | 0.00 USD | 25,330.00 USD | 0.00 USD | 0.00 USD | 13,700.00 USD |
| `1D` | `1.11` | 9,050.00 USD | 0.00 USD | 9,050.00 USD | 0.00 USD | 0.00 USD | 7,250.00 USD |
| `7D` | `1.11` | 11,620.00 USD | 0.00 USD | 11,620.00 USD | 0.00 USD | 0.00 USD | 9,490.00 USD |
| `1D` | `1.11` | 1,800.00 USD | 0.00 USD | 1,800.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD |
| `7D` | `1.11` | 2,130.00 USD | 0.00 USD | 2,130.00 USD | 0.00 USD | 0.00 USD | 2,130.00 USD |
| `1D` | `1.11` | 691.45 USD | 0.00 USD | 691.45 USD | 0.00 USD | 0.00 USD | 691.45 USD |
| `1D` | `1.12` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.12` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.13` | 10,080.00 USD | 10,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,080.00 USD |
| `7D` | `1.13` | 14,740.00 USD | 14,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,670.00 USD |
| `1D` | `1.13` | 5,880.00 USD | 5,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,880.00 USD |
| `7D` | `1.13` | 27,440.00 USD | 27,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,690.00 USD |
| `1D` | `1.13` | 12,430.00 USD | 12,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,540.00 USD |
| `7D` | `1.13` | 36,000.00 USD | 36,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,570.00 USD |
| `1D` | `1.13` | 14,590.00 USD | 14,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,170.00 USD |
| `1D` | `1.13` | 25,860.00 USD | 25,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,270.00 USD |
| `7D` | `1.13` | 54,800.00 USD | 54,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18,800.00 USD |
| `1D` | `1.13` | 33,370.00 USD | 33,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,510.00 USD |
| `7D` | `1.13` | 60,650.00 USD | 60,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,850.00 USD |
| `1D` | `1.13` | 34,260.00 USD | 34,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 891.36 USD |
| `7D` | `1.13` | 61,330.00 USD | 61,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 681.89 USD |
| `1D` | `1.14` | 34,750.00 USD | 34,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 491.52 USD |
| `7D` | `1.14` | 62,640.00 USD | 62,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD |
| `7D` | `1.14` | 66,220.00 USD | 66,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,580.00 USD |
| `7D` | `1.14` | 70,010.00 USD | 70,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,790.00 USD |
| `1D` | `1.14` | 37,690.00 USD | 37,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,930.00 USD |
| `7D` | `1.14` | 74,790.00 USD | 74,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,780.00 USD |
| `1D` | `1.14` | 40,970.00 USD | 40,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,280.00 USD |
| `7D` | `1.14` | 78,190.00 USD | 78,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,400.00 USD |
| `1D` | `1.14` | 40,970.00 USD | 40,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7.53 USD |
| `7D` | `1.14` | 80,640.00 USD | 80,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,450.00 USD |
| `1D` | `1.14` | 47,610.00 USD | 47,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,630.00 USD |
| `7D` | `1.14` | 87,490.00 USD | 87,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,850.00 USD |
| `1D` | `1.14` | 51,230.00 USD | 51,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,620.00 USD |
| `7D` | `1.14` | 92,240.00 USD | 92,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,750.00 USD |
| `1D` | `1.14` | 51,790.00 USD | 51,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 556.72 USD |
| `7D` | `1.15` | 93,300.00 USD | 93,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,070.00 USD |
| `1D` | `1.15` | 52,130.00 USD | 52,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 345.73 USD |
| `7D` | `1.15` | 93,960.00 USD | 93,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 654.82 USD |
| `7D` | `1.16` | 96,480.00 USD | 96,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,520.00 USD |
| `1D` | `1.16` | 52,910.00 USD | 52,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 776.05 USD |
| `7D` | `1.16` | 97,640.00 USD | 97,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,170.00 USD |
| `1D` | `1.16` | 54,520.00 USD | 54,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,610.00 USD |
| `7D` | `1.16` | 100,870.00 USD | 100,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,230.00 USD |
| `1D` | `1.16` | 55,240.00 USD | 55,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 716.82 USD |
| `7D` | `1.16` | 102,960.00 USD | 102,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,090.00 USD |
| `1D` | `1.16` | 55,780.00 USD | 55,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 541.39 USD |
| `1D` | `1.17` | 58,600.00 USD | 58,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,820.00 USD |
| `7D` | `1.17` | 107,660.00 USD | 107,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,700.00 USD |
| `1D` | `1.17` | 60,420.00 USD | 60,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `1.17` | 108,880.00 USD | 108,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,220.00 USD |
| `1D` | `1.17` | 60,690.00 USD | 60,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 266.60 USD |
| `7D` | `1.17` | 109,290.00 USD | 109,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 409.49 USD |
| `1D` | `1.17` | 60,820.00 USD | 60,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 134.03 USD |
| `7D` | `1.17` | 109,620.00 USD | 109,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 327.41 USD |
| `7D` | `1.23` | 109,700.00 USD | 109,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 81.33 USD |
| `7D` | `1.23` | 110,640.00 USD | 110,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 941.96 USD |
| `1D` | `1.23` | 61,130.00 USD | 61,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 310.42 USD |
| `7D` | `1.23` | 111,430.00 USD | 111,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 792.91 USD |
| `1D` | `1.23` | 62,060.00 USD | 62,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 926.28 USD |
| `7D` | `1.23` | 112,380.00 USD | 112,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 943.29 USD |
| `1D` | `1.23` | 62,060.00 USD | 62,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.30 USD |
| `7D` | `1.23` | 113,210.00 USD | 113,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 835.18 USD |
| `1D` | `1.23` | 62,280.00 USD | 62,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 216.89 USD |
| `1D` | `1.23` | 63,400.00 USD | 63,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD |
| `7D` | `1.23` | 114,940.00 USD | 114,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,720.00 USD |
| `1D` | `1.23` | 64,120.00 USD | 64,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 718.93 USD |
| `1D` | `1.23` | 64,210.00 USD | 64,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 89.28 USD |
| `7D` | `1.23` | 115,480.00 USD | 115,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 540.85 USD |
| `7D` | `1.24` | 115,640.00 USD | 115,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 163.80 USD |
| `7D` | `1.24` | 115,770.00 USD | 115,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 130.96 USD |

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
  * Current Rate: `584.16` | Last 24h: `658.59` | Last 3d: `761.48` | Last 7d: `828.22`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0719%` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `0.0000%` | **USDT Bitget** | `-0.0678%` |
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
  * `2026-10-30 14:10:12 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:52:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:32:12 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 13:22:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 13:21:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.12` (Risk Distance: `0.000792` pts)
  * +2.5R Take Profit: `1.12`
  * Mathematical Lot Sizing: **`0.12 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.12` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.12` (Risk Distance: `0.000792` pts)
  * +2.5R Take Profit: `1.12`
  * Mathematical Lot Sizing: **`0.12 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.13`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
