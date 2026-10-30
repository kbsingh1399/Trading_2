# 🏛️ SOVEREIGN CANDIDATE DOSSIER: GBPUSD
**Canonical Key**: `GBPUSD` | **Broker Instrument**: `GBPUSD.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 10:31:47 IST` (`2026-10-30 05:01:47 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `1.34` | VWAP Z-Score: `-0.70` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000579` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `52.13` (State: `NEUTRAL`)
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
  * Institutional Anchors: EMA-144=`1.34` | EMA-200=`1.33` (Slope: `+0.0476`) | EMA-233=`1.33`
- **Range Boundaries**: 24H High=`1.34` | 24H Low=`1.33` | Weekly High=`1.34` | Weekly Low=`1.33`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.34` (Distance: `-0.10%`)
  * Point of Control (POC) = `1.34` (Distance: `-0.02%`)
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
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `893` | 1,196.36 USD | -1,076.72 USD | `-90.00%` | 4,779.03 USD | `-2.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `823` | 1,102.40 USD | -618.42 USD | `-56.10%` | 4,160.61 USD | `-1.15` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `609` | 815.46 USD | -733.92 USD | `-90.00%` | 3,426.70 USD | `-1.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `2,902` | 3,888.97 USD | -2,064.15 USD | `-53.08%` | 13,877.64 USD | `-2.45` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `2,325` | 3,113.22 USD | -2,801.90 USD | `-90.00%` | 11,075.74 USD | `-2.53` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `2,056` | 2,753.60 USD | 1,511.78 USD | `+54.90%` | 12,587.52 USD | `+1.25` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `2,109` | 2,821.44 USD | -2,405.78 USD | `-85.27%` | 11,755.81 USD | `-0.71` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `5,652` | 7,571.48 USD | 6,814.33 USD | `+90.00%` | 18,570.14 USD | `+1.18` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `9,820` | 13,151.93 USD | -4,887.05 USD | `-37.16%` | 13,683.08 USD | `-1.25` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `16,632` | 22,245.30 USD | 5,841.73 USD | `+26.26%` | 37,583.56 USD | `-0.22` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `9,697` | 12,990.20 USD | 11,691.18 USD | `+90.00%` | 49,274.74 USD | `+0.13` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `22,744` | 30,452.62 USD | -18,697.60 USD | `-61.40%` | 30,577.14 USD | `-1.40` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.33` | `1.33` | `1.33` | `1.33` | `23,876` | 31,800.92 USD | 4,068.43 USD | `+12.79%` | -4,182.04 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `1.33` | `1.34` | `1.33` | `1.34` | `40,930` | 54,714.81 USD | 35,923.87 USD | `+65.66%` | 31,741.83 USD | `+1.36` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `16,632` | 22,245.30 USD | 5,841.73 USD | `+26.26%` | 37,583.56 USD | `-0.22` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `9,697` | 12,990.20 USD | 11,691.18 USD | `+90.00%` | 49,274.74 USD | `+0.13` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `23,178` | 31,033.72 USD | -17,678.41 USD | `-56.97%` | 31,596.33 USD | `-1.37` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `7D` | `1.21` | 43,510.00 USD | 0.00 USD | 43,510.00 USD | 0.00 USD | 0.00 USD | 168.74 USD |
| `7D` | `1.21` | 43,340.00 USD | 0.00 USD | 43,340.00 USD | 0.00 USD | 0.00 USD | 25.01 USD |
| `1D` | `1.21` | 4,320.00 USD | 0.00 USD | 4,320.00 USD | 0.00 USD | 0.00 USD | 8.04 USD |
| `7D` | `1.28` | 43,310.00 USD | 0.00 USD | 43,310.00 USD | 0.00 USD | 0.00 USD | 19.09 USD |
| `7D` | `1.28` | 43,290.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD | 0.00 USD | 892.20 USD |
| `7D` | `1.28` | 42,400.00 USD | 0.00 USD | 42,400.00 USD | 0.00 USD | 0.00 USD | 181.70 USD |
| `1D` | `1.28` | 4,320.00 USD | 0.00 USD | 4,320.00 USD | 0.00 USD | 0.00 USD | 80.96 USD |
| `7D` | `1.28` | 42,220.00 USD | 0.00 USD | 42,220.00 USD | 0.00 USD | 0.00 USD | 638.02 USD |
| `1D` | `1.28` | 4,230.00 USD | 0.00 USD | 4,230.00 USD | 0.00 USD | 0.00 USD | 327.83 USD |
| `7D` | `1.28` | 41,580.00 USD | 0.00 USD | 41,580.00 USD | 0.00 USD | 0.00 USD | 3,800.00 USD |
| `1D` | `1.28` | 3,910.00 USD | 0.00 USD | 3,910.00 USD | 0.00 USD | 0.00 USD | 5.25 USD |
| `7D` | `1.28` | 37,780.00 USD | 0.00 USD | 37,780.00 USD | 0.00 USD | 0.00 USD | 58.38 USD |
| `1D` | `1.28` | 3,900.00 USD | 0.00 USD | 3,900.00 USD | 0.00 USD | 0.00 USD | 110.54 USD |
| `7D` | `1.28` | 37,730.00 USD | 0.00 USD | 37,730.00 USD | 0.00 USD | 0.00 USD | 131.41 USD |
| `1D` | `1.29` | 3,790.00 USD | 0.00 USD | 3,790.00 USD | 0.00 USD | 0.00 USD | 49.05 USD |
| `7D` | `1.29` | 37,590.00 USD | 0.00 USD | 37,590.00 USD | 0.00 USD | 0.00 USD | 405.46 USD |
| `1D` | `1.29` | 3,740.00 USD | 0.00 USD | 3,740.00 USD | 0.00 USD | 0.00 USD | 42.88 USD |
| `7D` | `1.29` | 37,190.00 USD | 0.00 USD | 37,190.00 USD | 0.00 USD | 0.00 USD | 65.12 USD |
| `7D` | `1.30` | 37,120.00 USD | 0.00 USD | 37,120.00 USD | 0.00 USD | 0.00 USD | 38.18 USD |
| `7D` | `1.30` | 37,090.00 USD | 0.00 USD | 37,090.00 USD | 0.00 USD | 0.00 USD | 1,780.00 USD |
| `7D` | `1.31` | 35,300.00 USD | 0.00 USD | 35,300.00 USD | 0.00 USD | 0.00 USD | 363.39 USD |
| `1D` | `1.31` | 3,700.00 USD | 0.00 USD | 3,700.00 USD | 0.00 USD | 0.00 USD | 161.92 USD |
| `7D` | `1.31` | 34,940.00 USD | 0.00 USD | 34,940.00 USD | 0.00 USD | 0.00 USD | 1,280.00 USD |
| `1D` | `1.31` | 3,540.00 USD | 0.00 USD | 3,540.00 USD | 0.00 USD | 0.00 USD | 654.32 USD |
| `7D` | `1.31` | 33,660.00 USD | 0.00 USD | 33,660.00 USD | 0.00 USD | 0.00 USD | 4,490.00 USD |
| `1D` | `1.31` | 2,880.00 USD | 0.00 USD | 2,880.00 USD | 0.00 USD | 0.00 USD | 6.00 USD |
| `7D` | `1.31` | 29,170.00 USD | 0.00 USD | 29,170.00 USD | 0.00 USD | 0.00 USD | 3,190.00 USD |
| `1D` | `1.31` | 2,880.00 USD | 0.00 USD | 2,880.00 USD | 0.00 USD | 0.00 USD | 6.33 USD |
| `7D` | `1.31` | 25,980.00 USD | 0.00 USD | 25,980.00 USD | 0.00 USD | 0.00 USD | 265.72 USD |
| `1D` | `1.31` | 2,870.00 USD | 0.00 USD | 2,870.00 USD | 0.00 USD | 0.00 USD | 316.56 USD |
| `7D` | `1.31` | 25,720.00 USD | 0.00 USD | 25,720.00 USD | 0.00 USD | 0.00 USD | 789.15 USD |
| `1D` | `1.31` | 2,550.00 USD | 0.00 USD | 2,550.00 USD | 0.00 USD | 0.00 USD | 87.86 USD |
| `7D` | `1.31` | 24,930.00 USD | 0.00 USD | 24,930.00 USD | 0.00 USD | 0.00 USD | 178.80 USD |
| `7D` | `1.32` | 24,750.00 USD | 0.00 USD | 24,750.00 USD | 0.00 USD | 0.00 USD | 76.36 USD |
| `7D` | `1.32` | 24,670.00 USD | 0.00 USD | 24,670.00 USD | 0.00 USD | 0.00 USD | 3,830.00 USD |
| `1D` | `1.32` | 2,470.00 USD | 0.00 USD | 2,470.00 USD | 0.00 USD | 0.00 USD | 291.75 USD |
| `7D` | `1.32` | 20,840.00 USD | 0.00 USD | 20,840.00 USD | 0.00 USD | 0.00 USD | 569.10 USD |
| `1D` | `1.32` | 2,170.00 USD | 0.00 USD | 2,170.00 USD | 0.00 USD | 0.00 USD | 92.40 USD |
| `7D` | `1.32` | 20,270.00 USD | 0.00 USD | 20,270.00 USD | 0.00 USD | 0.00 USD | 4,470.00 USD |
| `1D` | `1.32` | 2,080.00 USD | 0.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD | 1,250.00 USD |
| `7D` | `1.32` | 15,810.00 USD | 0.00 USD | 15,810.00 USD | 0.00 USD | 0.00 USD | 13,220.00 USD |
| `1D` | `1.32` | 830.87 USD | 0.00 USD | 830.87 USD | 0.00 USD | 0.00 USD | 20.99 USD |
| `7D` | `1.32` | 2,590.00 USD | 0.00 USD | 2,590.00 USD | 0.00 USD | 0.00 USD | 284.41 USD |
| `1D` | `1.32` | 809.88 USD | 0.00 USD | 809.88 USD | 0.00 USD | 0.00 USD | 499.97 USD |
| `7D` | `1.33` | 2,300.00 USD | 0.00 USD | 2,300.00 USD | 0.00 USD | 0.00 USD | 1,800.00 USD |
| `1D` | `1.33` | 309.91 USD | 0.00 USD | 309.91 USD | 0.00 USD | 0.00 USD | 223.36 USD |
| `7D` | `1.33` | 503.16 USD | 0.00 USD | 503.16 USD | 0.00 USD | 0.00 USD | 503.16 USD |
| `1D` | `1.33` | 86.55 USD | 0.00 USD | 86.55 USD | 0.00 USD | 0.00 USD | 86.55 USD |
| `1D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 76.36 USD | 76.36 USD | 0.00 USD | 0.00 USD | 0.00 USD | 76.36 USD |
| `7D` | `1.34` | 3,910.00 USD | 3,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,830.00 USD |
| `1D` | `1.35` | 291.75 USD | 291.75 USD | 0.00 USD | 0.00 USD | 0.00 USD | 291.75 USD |
| `7D` | `1.35` | 4,470.00 USD | 4,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 569.10 USD |
| `1D` | `1.35` | 384.15 USD | 384.15 USD | 0.00 USD | 0.00 USD | 0.00 USD | 92.40 USD |
| `7D` | `1.35` | 8,940.00 USD | 8,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,470.00 USD |
| `1D` | `1.35` | 1,640.00 USD | 1,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,250.00 USD |
| `7D` | `1.35` | 22,160.00 USD | 22,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,220.00 USD |
| `1D` | `1.35` | 1,660.00 USD | 1,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20.99 USD |
| `7D` | `1.35` | 22,340.00 USD | 22,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 180.38 USD |
| `1D` | `1.35` | 2,130.00 USD | 2,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 472.89 USD |
| `7D` | `1.35` | 24,170.00 USD | 24,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,830.00 USD |
| `1D` | `1.35` | 2,380.00 USD | 2,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 250.44 USD |
| `7D` | `1.35` | 24,650.00 USD | 24,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 474.91 USD |
| `1D` | `1.35` | 2,470.00 USD | 2,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 86.55 USD |
| `7D` | `1.35` | 24,750.00 USD | 24,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 101.55 USD |
| `7D` | `1.36` | 24,790.00 USD | 24,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 38.18 USD |
| `7D` | `1.36` | 26,570.00 USD | 26,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,780.00 USD |
| `7D` | `1.36` | 26,940.00 USD | 26,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 363.39 USD |
| `1D` | `1.36` | 2,620.00 USD | 2,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 155.31 USD |
| `7D` | `1.36` | 28,210.00 USD | 28,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,280.00 USD |
| `1D` | `1.36` | 3,280.00 USD | 3,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 658.33 USD |
| `7D` | `1.36` | 32,700.00 USD | 32,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,490.00 USD |
| `1D` | `1.36` | 3,280.00 USD | 3,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.94 USD |
| `7D` | `1.36` | 35,840.00 USD | 35,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,140.00 USD |
| `1D` | `1.36` | 3,290.00 USD | 3,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10.50 USD |
| `7D` | `1.36` | 36,090.00 USD | 36,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 249.39 USD |
| `1D` | `1.37` | 3,580.00 USD | 3,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 282.23 USD |
| `7D` | `1.37` | 36,900.00 USD | 36,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 807.43 USD |
| `1D` | `1.37` | 3,670.00 USD | 3,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 94.81 USD |
| `7D` | `1.37` | 37,120.00 USD | 37,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 224.43 USD |
| `1D` | `1.37` | 3,700.00 USD | 3,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 27.87 USD |
| `7D` | `1.38` | 37,140.00 USD | 37,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19.09 USD |
| `7D` | `1.38` | 38,040.00 USD | 38,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 892.20 USD |
| `7D` | `1.39` | 38,150.00 USD | 38,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 113.03 USD |
| `1D` | `1.39` | 3,780.00 USD | 3,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 77.66 USD |
| `7D` | `1.39` | 38,850.00 USD | 38,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 706.69 USD |
| `1D` | `1.39` | 3,910.00 USD | 3,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 131.82 USD |
| `7D` | `1.39` | 40,290.00 USD | 40,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `1.39` | 4,110.00 USD | 4,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 199.31 USD |
| `7D` | `1.39` | 42,670.00 USD | 42,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,380.00 USD |
| `1D` | `1.39` | 4,110.00 USD | 4,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.25 USD |
| `7D` | `1.39` | 42,790.00 USD | 42,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 118.09 USD |
| `1D` | `1.39` | 4,250.00 USD | 4,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 141.12 USD |
| `7D` | `1.39` | 43,190.00 USD | 43,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 402.17 USD |
| `1D` | `1.39` | 4,290.00 USD | 4,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39.71 USD |
| `7D` | `1.39` | 43,310.00 USD | 43,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 120.35 USD |
| `1D` | `1.40` | 4,320.00 USD | 4,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21.64 USD |
| `7D` | `1.46` | 43,320.00 USD | 43,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7.64 USD |
| `7D` | `1.46` | 43,650.00 USD | 43,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 331.52 USD |
| `7D` | `1.47` | 43,710.00 USD | 43,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 62.01 USD |
| `1D` | `1.47` | 4,350.00 USD | 4,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.91 USD |
| `7D` | `1.47` | 43,960.00 USD | 43,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 243.79 USD |
| `1D` | `1.47` | 4,350.00 USD | 4,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8.51 USD |
| `7D` | `1.47` | 44,420.00 USD | 44,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 466.39 USD |
| `1D` | `1.47` | 4,480.00 USD | 4,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 121.74 USD |
| `7D` | `1.47` | 45,320.00 USD | 45,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 897.14 USD |
| `1D` | `1.47` | 4,480.00 USD | 4,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2.10 USD |
| `7D` | `1.47` | 45,330.00 USD | 45,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10.51 USD |
| `1D` | `1.47` | 4,520.00 USD | 4,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44.74 USD |
| `7D` | `1.47` | 45,390.00 USD | 45,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 58.80 USD |
| `1D` | `1.47` | 4,540.00 USD | 4,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16.56 USD |
| `7D` | `1.47` | 45,510.00 USD | 45,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 119.06 USD |
| `1D` | `1.47` | 4,540.00 USD | 4,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2.53 USD |
| `7D` | `1.48` | 45,520.00 USD | 45,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15.89 USD |

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
| `04:15:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 1,429.21 USD | 1,357.75 USD | 71.46 USD | 1,286.29 USD | `+90.00%` | `1B / 0S` |
| `04:20:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 1,198.41 USD | 438.95 USD | 759.46 USD | -320.50 USD | `-26.74%` | `0B / 1S` |
| `04:25:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 1,262.37 USD | 113.82 USD | 1,148.55 USD | -1,034.73 USD | `-81.97%` | `0B / 1S` |
| `04:30:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 1,196.36 USD | 59.82 USD | 1,136.54 USD | -1,076.72 USD | `-90.00%` | `0B / 1S` |
| `04:30:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 3,113.22 USD | 155.66 USD | 2,957.56 USD | -2,801.90 USD | `-90.00%` | `0B / 1S` |
| `04:35:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 1,102.40 USD | 241.99 USD | 860.41 USD | -618.42 USD | `-56.10%` | `0B / 1S` |
| `04:40:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 815.46 USD | 40.77 USD | 774.69 USD | -733.92 USD | `-90.00%` | `0B / 1S` |
| `04:45:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 859.69 USD | 435.22 USD | 424.47 USD | 10.75 USD | `+1.25%` | `1B / 0S` |
| `04:45:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 2,753.60 USD | 2,132.69 USD | 620.91 USD | 1,511.78 USD | `+54.90%` | `1B / 0S` |
| `04:50:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 915.89 USD | 169.61 USD | 746.28 USD | -576.67 USD | `-62.96%` | `0B / 1S` |

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
  * `2026-10-30 09:51:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:29:10 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.34` (Risk Distance: `0.000710` pts)
  * +2.5R Take Profit: `1.34`
  * Mathematical Lot Sizing: **`0.14 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.34` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.34` (Risk Distance: `0.000710` pts)
  * +2.5R Take Profit: `1.34`
  * Mathematical Lot Sizing: **`0.14 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.35`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
