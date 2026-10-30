# 🏛️ SOVEREIGN CANDIDATE DOSSIER: GBPUSD
**Canonical Key**: `GBPUSD` | **Broker Instrument**: `GBPUSD.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 08:03:31 IST` (`2026-10-30 02:33:31 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.34` | **Live Ask Quote**: `1.34` | **Mid Price**: `1.34`
- **Spread Points**: `1.00` | **Spread BPS**: `0.07 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `1.34` | VWAP Z-Score: `-0.12` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000696` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `60.55` (State: `NEUTRAL`)
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
  * Institutional Anchors: EMA-144=`1.33` | EMA-200=`1.33` (Slope: `+0.0478`) | EMA-233=`1.33`
- **Range Boundaries**: 24H High=`1.34` | 24H Low=`1.33` | Weekly High=`1.34` | Weekly Low=`1.33`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.34` (Distance: `-0.04%`)
  * Point of Control (POC) = `1.34` (Distance: `+0.01%`)
  * Value Area Low (VAL) = `1.34` (Distance: `+0.11%`)
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
  * Initial Balance (First Hour): IB High=`1.34` | IB Low=`1.34`
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
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `302` | 404.27 USD | -258.73 USD | `-64.00%` | 3,756.00 USD | `-2.19` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `249` | 333.28 USD | -272.68 USD | `-81.82%` | 3,483.32 USD | `-1.96` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `221` | 295.82 USD | 147.91 USD | `+50.00%` | 3,631.23 USD | `+0.88` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `274` | 366.74 USD | 194.48 USD | `+53.03%` | 12,887.06 USD | `+0.29` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `582` | 779.14 USD | 217.90 USD | `+27.97%` | 13,104.96 USD | `+0.28` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `772` | 1,033.36 USD | -355.22 USD | `-34.37%` | 12,749.74 USD | `-0.46` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `215` | 287.56 USD | 109.95 USD | `+38.24%` | 15,062.66 USD | `-0.11` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `1,721` | 2,303.95 USD | 1,690.07 USD | `+73.36%` | 16,752.73 USD | `+0.18` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `2,109` | 2,821.44 USD | -2,405.78 USD | `-85.27%` | 14,346.95 USD | `-0.71` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.33` | `1.34` | `1.33` | `1.34` | `40,930` | 54,714.81 USD | 35,923.87 USD | `+65.66%` | 30,685.26 USD | `+1.67` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `16,632` | 22,245.30 USD | 5,841.73 USD | `+26.26%` | 36,526.99 USD | `-0.10` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `9,697` | 12,990.20 USD | 11,691.18 USD | `+90.00%` | 48,218.16 USD | `+0.26` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.33` | `1.33` | `1.33` | `1.33` | `17,831` | 23,736.63 USD | -8,250.46 USD | `-34.76%` | -9,307.04 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.33` | `1.33` | `1.33` | `1.33` | `23,876` | 31,800.92 USD | 4,068.43 USD | `+12.79%` | -5,238.61 USD | `+1.15` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `1.33` | `1.34` | `1.33` | `1.34` | `40,930` | 54,714.81 USD | 35,923.87 USD | `+65.66%` | 30,685.26 USD | `+1.67` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `16,632` | 22,245.30 USD | 5,841.73 USD | `+26.26%` | 36,526.99 USD | `-0.10` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `9,697` | 12,990.20 USD | 11,691.18 USD | `+90.00%` | 48,218.16 USD | `+0.26` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `7D` | `1.20` | 43,420.00 USD | 0.00 USD | 43,420.00 USD | 0.00 USD | 0.00 USD | 47.55 USD |
| `7D` | `1.21` | 43,370.00 USD | 0.00 USD | 43,370.00 USD | 0.00 USD | 0.00 USD | 158.46 USD |
| `1D` | `1.21` | 4,960.00 USD | 0.00 USD | 4,960.00 USD | 0.00 USD | 0.00 USD | 13.85 USD |
| `7D` | `1.21` | 43,210.00 USD | 0.00 USD | 43,210.00 USD | 0.00 USD | 0.00 USD | 41.31 USD |
| `7D` | `1.28` | 43,170.00 USD | 0.00 USD | 43,170.00 USD | 0.00 USD | 0.00 USD | 810.32 USD |
| `7D` | `1.28` | 42,360.00 USD | 0.00 USD | 42,360.00 USD | 0.00 USD | 0.00 USD | 39.55 USD |
| `7D` | `1.28` | 42,320.00 USD | 0.00 USD | 42,320.00 USD | 0.00 USD | 0.00 USD | 220.24 USD |
| `1D` | `1.28` | 4,950.00 USD | 0.00 USD | 4,950.00 USD | 0.00 USD | 0.00 USD | 82.99 USD |
| `7D` | `1.28` | 42,100.00 USD | 0.00 USD | 42,100.00 USD | 0.00 USD | 0.00 USD | 1,590.00 USD |
| `1D` | `1.28` | 4,860.00 USD | 0.00 USD | 4,860.00 USD | 0.00 USD | 0.00 USD | 325.80 USD |
| `7D` | `1.28` | 40,510.00 USD | 0.00 USD | 40,510.00 USD | 0.00 USD | 0.00 USD | 2,800.00 USD |
| `1D` | `1.28` | 4,540.00 USD | 0.00 USD | 4,540.00 USD | 0.00 USD | 0.00 USD | 144.98 USD |
| `7D` | `1.28` | 37,710.00 USD | 0.00 USD | 37,710.00 USD | 0.00 USD | 0.00 USD | 106.24 USD |
| `1D` | `1.28` | 4,390.00 USD | 0.00 USD | 4,390.00 USD | 0.00 USD | 0.00 USD | 114.36 USD |
| `7D` | `1.28` | 37,600.00 USD | 0.00 USD | 37,600.00 USD | 0.00 USD | 0.00 USD | 382.02 USD |
| `1D` | `1.29` | 4,280.00 USD | 0.00 USD | 4,280.00 USD | 0.00 USD | 0.00 USD | 38.46 USD |
| `7D` | `1.29` | 37,220.00 USD | 0.00 USD | 37,220.00 USD | 0.00 USD | 0.00 USD | 162.67 USD |
| `7D` | `1.29` | 37,060.00 USD | 0.00 USD | 37,060.00 USD | 0.00 USD | 0.00 USD | 54.19 USD |
| `7D` | `1.30` | 37,000.00 USD | 0.00 USD | 37,000.00 USD | 0.00 USD | 0.00 USD | 1,620.00 USD |
| `7D` | `1.30` | 35,380.00 USD | 0.00 USD | 35,380.00 USD | 0.00 USD | 0.00 USD | 79.07 USD |
| `7D` | `1.31` | 35,300.00 USD | 0.00 USD | 35,300.00 USD | 0.00 USD | 0.00 USD | 440.48 USD |
| `1D` | `1.31` | 4,240.00 USD | 0.00 USD | 4,240.00 USD | 0.00 USD | 0.00 USD | 165.99 USD |
| `7D` | `1.31` | 34,860.00 USD | 0.00 USD | 34,860.00 USD | 0.00 USD | 0.00 USD | 3,190.00 USD |
| `1D` | `1.31` | 4,070.00 USD | 0.00 USD | 4,070.00 USD | 0.00 USD | 0.00 USD | 651.59 USD |
| `7D` | `1.31` | 31,680.00 USD | 0.00 USD | 31,680.00 USD | 0.00 USD | 0.00 USD | 4,690.00 USD |
| `1D` | `1.31` | 3,420.00 USD | 0.00 USD | 3,420.00 USD | 0.00 USD | 0.00 USD | 284.17 USD |
| `7D` | `1.31` | 26,990.00 USD | 0.00 USD | 26,990.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD |
| `1D` | `1.31` | 3,140.00 USD | 0.00 USD | 3,140.00 USD | 0.00 USD | 0.00 USD | 226.92 USD |
| `7D` | `1.31` | 25,870.00 USD | 0.00 USD | 25,870.00 USD | 0.00 USD | 0.00 USD | 747.13 USD |
| `1D` | `1.31` | 2,910.00 USD | 0.00 USD | 2,910.00 USD | 0.00 USD | 0.00 USD | 82.43 USD |
| `7D` | `1.31` | 25,120.00 USD | 0.00 USD | 25,120.00 USD | 0.00 USD | 0.00 USD | 330.92 USD |
| `1D` | `1.31` | 2,830.00 USD | 0.00 USD | 2,830.00 USD | 0.00 USD | 0.00 USD | 2.13 USD |
| `7D` | `1.31` | 24,790.00 USD | 0.00 USD | 24,790.00 USD | 0.00 USD | 0.00 USD | 119.74 USD |
| `7D` | `1.32` | 24,670.00 USD | 0.00 USD | 24,670.00 USD | 0.00 USD | 0.00 USD | 3,330.00 USD |
| `7D` | `1.32` | 21,340.00 USD | 0.00 USD | 21,340.00 USD | 0.00 USD | 0.00 USD | 759.72 USD |
| `1D` | `1.32` | 2,830.00 USD | 0.00 USD | 2,830.00 USD | 0.00 USD | 0.00 USD | 298.99 USD |
| `7D` | `1.32` | 20,580.00 USD | 0.00 USD | 20,580.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD |
| `1D` | `1.32` | 2,530.00 USD | 0.00 USD | 2,530.00 USD | 0.00 USD | 0.00 USD | 85.16 USD |
| `7D` | `1.32` | 17,950.00 USD | 0.00 USD | 17,950.00 USD | 0.00 USD | 0.00 USD | 6,670.00 USD |
| `1D` | `1.32` | 2,440.00 USD | 0.00 USD | 2,440.00 USD | 0.00 USD | 0.00 USD | 1,770.00 USD |
| `7D` | `1.32` | 11,280.00 USD | 0.00 USD | 11,280.00 USD | 0.00 USD | 0.00 USD | 8,460.00 USD |
| `1D` | `1.32` | 674.32 USD | 0.00 USD | 674.32 USD | 0.00 USD | 0.00 USD | 63.02 USD |
| `7D` | `1.32` | 2,820.00 USD | 0.00 USD | 2,820.00 USD | 0.00 USD | 0.00 USD | 612.00 USD |
| `1D` | `1.33` | 611.30 USD | 0.00 USD | 611.30 USD | 0.00 USD | 0.00 USD | 520.51 USD |
| `7D` | `1.33` | 2,210.00 USD | 0.00 USD | 2,210.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD |
| `1D` | `1.33` | 90.79 USD | 0.00 USD | 90.79 USD | 0.00 USD | 0.00 USD | 90.79 USD |
| `7D` | `1.33` | 480.98 USD | 0.00 USD | 480.98 USD | 0.00 USD | 0.00 USD | 453.06 USD |
| `7D` | `1.33` | 27.92 USD | 0.00 USD | 27.92 USD | 0.00 USD | 0.00 USD | 27.92 USD |
| `7D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 3,330.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,330.00 USD |
| `7D` | `1.34` | 4,090.00 USD | 4,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 759.72 USD |
| `1D` | `1.35` | 298.99 USD | 298.99 USD | 0.00 USD | 0.00 USD | 0.00 USD | 298.99 USD |
| `7D` | `1.35` | 6,720.00 USD | 6,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD |
| `1D` | `1.35` | 384.15 USD | 384.15 USD | 0.00 USD | 0.00 USD | 0.00 USD | 85.16 USD |
| `7D` | `1.35` | 13,380.00 USD | 13,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,670.00 USD |
| `1D` | `1.35` | 2,020.00 USD | 2,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,640.00 USD |
| `7D` | `1.35` | 21,850.00 USD | 21,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,460.00 USD |
| `1D` | `1.35` | 2,220.00 USD | 2,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 191.05 USD |
| `7D` | `1.35` | 22,360.00 USD | 22,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 514.32 USD |
| `1D` | `1.35` | 2,690.00 USD | 2,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 472.89 USD |
| `7D` | `1.35` | 24,100.00 USD | 24,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,740.00 USD |
| `1D` | `1.35` | 2,830.00 USD | 2,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 138.41 USD |
| `7D` | `1.35` | 24,640.00 USD | 24,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 536.69 USD |
| `7D` | `1.35` | 24,670.00 USD | 24,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 27.92 USD |
| `7D` | `1.36` | 26,290.00 USD | 26,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,620.00 USD |
| `7D` | `1.36` | 26,370.00 USD | 26,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 79.07 USD |
| `7D` | `1.36` | 26,810.00 USD | 26,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 440.48 USD |
| `1D` | `1.36` | 2,980.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 155.31 USD |
| `7D` | `1.36` | 29,790.00 USD | 29,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,980.00 USD |
| `1D` | `1.36` | 3,640.00 USD | 3,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 658.33 USD |
| `7D` | `1.36` | 34,290.00 USD | 34,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,500.00 USD |
| `1D` | `1.36` | 3,920.00 USD | 3,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 283.45 USD |
| `7D` | `1.36` | 35,750.00 USD | 35,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `1.36` | 3,930.00 USD | 3,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10.50 USD |
| `7D` | `1.36` | 35,970.00 USD | 35,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 216.01 USD |
| `1D` | `1.37` | 4,220.00 USD | 4,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 288.49 USD |
| `7D` | `1.37` | 36,790.00 USD | 36,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 827.72 USD |
| `1D` | `1.37` | 4,240.00 USD | 4,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17.15 USD |
| `7D` | `1.37` | 37,000.00 USD | 37,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 206.64 USD |
| `7D` | `1.38` | 37,810.00 USD | 37,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 810.32 USD |
| `7D` | `1.38` | 37,850.00 USD | 37,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39.55 USD |
| `7D` | `1.39` | 38,070.00 USD | 38,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 220.24 USD |
| `1D` | `1.39` | 4,320.00 USD | 4,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 77.66 USD |
| `7D` | `1.39` | 39,560.00 USD | 39,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,490.00 USD |
| `1D` | `1.39` | 4,650.00 USD | 4,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 329.16 USD |
| `7D` | `1.39` | 41,810.00 USD | 41,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,240.00 USD |
| `1D` | `1.39` | 4,780.00 USD | 4,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 133.73 USD |
| `7D` | `1.39` | 42,540.00 USD | 42,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 731.61 USD |
| `1D` | `1.39` | 4,790.00 USD | 4,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.22 USD |
| `7D` | `1.39` | 42,640.00 USD | 42,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 96.97 USD |
| `1D` | `1.39` | 4,930.00 USD | 4,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 134.35 USD |
| `7D` | `1.39` | 43,070.00 USD | 43,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 428.86 USD |
| `1D` | `1.39` | 4,950.00 USD | 4,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18.47 USD |
| `7D` | `1.39` | 43,170.00 USD | 43,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 103.32 USD |
| `7D` | `1.46` | 43,490.00 USD | 43,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 324.13 USD |
| `7D` | `1.46` | 43,510.00 USD | 43,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14.71 USD |
| `7D` | `1.47` | 43,570.00 USD | 43,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 61.44 USD |
| `1D` | `1.47` | 4,980.00 USD | 4,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.91 USD |
| `7D` | `1.47` | 44,150.00 USD | 44,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 581.37 USD |
| `1D` | `1.47` | 4,980.00 USD | 4,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8.51 USD |
| `7D` | `1.47` | 44,480.00 USD | 44,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 327.81 USD |
| `1D` | `1.47` | 5,160.00 USD | 5,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 173.44 USD |
| `7D` | `1.47` | 45,150.00 USD | 45,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 667.63 USD |
| `1D` | `1.47` | 5,160.00 USD | 5,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6.31 USD |
| `7D` | `1.47` | 45,190.00 USD | 45,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 47.55 USD |
| `1D` | `1.47` | 5,210.00 USD | 5,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44.74 USD |
| `7D` | `1.47` | 45,340.00 USD | 45,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 148.22 USD |
| `1D` | `1.47` | 5,220.00 USD | 5,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.85 USD |
| `7D` | `1.47` | 45,370.00 USD | 45,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.88 USD |
| `7D` | `1.48` | 45,390.00 USD | 45,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21.67 USD |

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
| `01:40:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 156.60 USD | 138.66 USD | 17.94 USD | 120.71 USD | `+77.08%` | `1B / 0S` |
| `01:45:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 227.58 USD | 215.14 USD | 12.45 USD | 202.69 USD | `+89.06%` | `1B / 0S` |
| `01:45:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 779.14 USD | 498.52 USD | 280.62 USD | 217.90 USD | `+27.97%` | `1B / 0S` |
| `01:50:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 274.48 USD | 215.01 USD | 59.47 USD | 155.54 USD | `+56.67%` | `1B / 0S` |
| `01:55:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 277.12 USD | 29.69 USD | 247.43 USD | -217.73 USD | `-78.57%` | `0B / 1S` |
| `02:00:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 1,033.36 USD | 339.07 USD | 694.29 USD | -355.22 USD | `-34.37%` | `0B / 1S` |
| `02:00:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 2,821.44 USD | 207.83 USD | 2,613.61 USD | -2,405.78 USD | `-85.27%` | `0B / 1S` |
| `02:00:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 404.27 USD | 72.77 USD | 331.50 USD | -258.73 USD | `-64.00%` | `0B / 1S` |
| `02:05:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 333.28 USD | 30.30 USD | 302.98 USD | -272.68 USD | `-81.82%` | `0B / 1S` |
| `02:10:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 295.82 USD | 221.86 USD | 73.95 USD | 147.91 USD | `+50.00%` | `1B / 0S` |

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
  * `2026-10-30 07:16:25 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:52:25 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:52:25 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 07:52:25 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:53:25 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:53:25 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:53:25 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:25 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:53:25 IST`: [sec.gov] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.34` (Risk Distance: `0.000850` pts)
  * +2.5R Take Profit: `1.34`
  * Mathematical Lot Sizing: **`0.11 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.34` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.34` (Risk Distance: `0.000850` pts)
  * +2.5R Take Profit: `1.34`
  * Mathematical Lot Sizing: **`0.11 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.35`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
