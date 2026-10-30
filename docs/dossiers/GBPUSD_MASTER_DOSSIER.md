# 🏛️ SOVEREIGN CANDIDATE DOSSIER: GBPUSD
**Canonical Key**: `GBPUSD` | **Broker Instrument**: `GBPUSD.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 17:19:12 IST` (`2026-10-30 11:49:12 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.34` | **Live Ask Quote**: `1.34` | **Mid Price**: `1.34`
- **Spread Points**: `5.00` | **Spread BPS**: `0.37 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `1.34` | VWAP Z-Score: `+2.08` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.000687` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `69.33` (State: `OVERBOUGHT`)
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
  * Institutional Anchors: EMA-144=`1.34` | EMA-200=`1.34` (Slope: `+0.0640`) | EMA-233=`1.34`
- **Range Boundaries**: 24H High=`1.34` | 24H Low=`1.33` | Weekly High=`1.34` | Weekly Low=`1.33`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.34` (Distance: `+0.11%`)
  * Point of Control (POC) = `1.34` (Distance: `+0.25%`)
  * Value Area Low (VAL) = `1.34` (Distance: `+0.32%`)
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
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `611` | 819.45 USD | 530.24 USD | `+64.71%` | 7,585.80 USD | `+1.07` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `449` | 601.92 USD | -412.85 USD | `-68.59%` | 7,172.94 USD | `-1.21` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `481` | 645.03 USD | 559.46 USD | `+86.73%` | 7,732.40 USD | `+1.15` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `1,358` | 1,820.02 USD | -1,623.26 USD | `-89.19%` | 18,691.49 USD | `-1.54` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `1,187` | 1,591.09 USD | 680.40 USD | `+42.76%` | 19,371.89 USD | `+0.53` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `1,541` | 2,066.50 USD | 850.91 USD | `+41.18%` | 20,222.80 USD | `+0.77` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `4,999` | 6,695.81 USD | 287.71 USD | `+4.30%` | 21,079.99 USD | `-0.08` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `5,391` | 7,226.26 USD | 2,226.27 USD | `+30.81%` | 23,306.26 USD | `+0.28` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `5,515` | 7,398.15 USD | 4,604.44 USD | `+62.24%` | 27,910.71 USD | `+0.70` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `7D` | `1.21` | 46,870.00 USD | 0.00 USD | 46,870.00 USD | 0.00 USD | 0.00 USD | 72.15 USD |
| `7D` | `1.28` | 46,800.00 USD | 0.00 USD | 46,800.00 USD | 0.00 USD | 0.00 USD | 810.32 USD |
| `7D` | `1.28` | 45,980.00 USD | 0.00 USD | 45,980.00 USD | 0.00 USD | 0.00 USD | 28.38 USD |
| `7D` | `1.28` | 45,960.00 USD | 0.00 USD | 45,960.00 USD | 0.00 USD | 0.00 USD | 231.41 USD |
| `7D` | `1.28` | 45,730.00 USD | 0.00 USD | 45,730.00 USD | 0.00 USD | 0.00 USD | 1,590.00 USD |
| `1D` | `1.28` | 3,990.00 USD | 0.00 USD | 3,990.00 USD | 0.00 USD | 0.00 USD | 13.04 USD |
| `7D` | `1.28` | 44,130.00 USD | 0.00 USD | 44,130.00 USD | 0.00 USD | 0.00 USD | 2,340.00 USD |
| `1D` | `1.28` | 3,980.00 USD | 0.00 USD | 3,980.00 USD | 0.00 USD | 0.00 USD | 202.56 USD |
| `7D` | `1.28` | 41,790.00 USD | 0.00 USD | 41,790.00 USD | 0.00 USD | 0.00 USD | 561.05 USD |
| `1D` | `1.28` | 3,770.00 USD | 0.00 USD | 3,770.00 USD | 0.00 USD | 0.00 USD | 5.25 USD |
| `7D` | `1.28` | 41,230.00 USD | 0.00 USD | 41,230.00 USD | 0.00 USD | 0.00 USD | 351.30 USD |
| `1D` | `1.28` | 3,770.00 USD | 0.00 USD | 3,770.00 USD | 0.00 USD | 0.00 USD | 136.90 USD |
| `7D` | `1.29` | 40,880.00 USD | 0.00 USD | 40,880.00 USD | 0.00 USD | 0.00 USD | 104.87 USD |
| `1D` | `1.29` | 3,630.00 USD | 0.00 USD | 3,630.00 USD | 0.00 USD | 0.00 USD | 125.97 USD |
| `7D` | `1.29` | 40,770.00 USD | 0.00 USD | 40,770.00 USD | 0.00 USD | 0.00 USD | 186.86 USD |
| `1D` | `1.29` | 3,500.00 USD | 0.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | 86.06 USD |
| `7D` | `1.30` | 40,580.00 USD | 0.00 USD | 40,580.00 USD | 0.00 USD | 0.00 USD | 1,620.00 USD |
| `7D` | `1.30` | 38,960.00 USD | 0.00 USD | 38,960.00 USD | 0.00 USD | 0.00 USD | 56.74 USD |
| `7D` | `1.31` | 38,910.00 USD | 0.00 USD | 38,910.00 USD | 0.00 USD | 0.00 USD | 366.84 USD |
| `7D` | `1.31` | 38,540.00 USD | 0.00 USD | 38,540.00 USD | 0.00 USD | 0.00 USD | 3,080.00 USD |
| `1D` | `1.31` | 3,420.00 USD | 0.00 USD | 3,420.00 USD | 0.00 USD | 0.00 USD | 26.09 USD |
| `7D` | `1.31` | 35,460.00 USD | 0.00 USD | 35,460.00 USD | 0.00 USD | 0.00 USD | 4,500.00 USD |
| `1D` | `1.31` | 3,390.00 USD | 0.00 USD | 3,390.00 USD | 0.00 USD | 0.00 USD | 405.11 USD |
| `7D` | `1.31` | 30,960.00 USD | 0.00 USD | 30,960.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `1.31` | 2,990.00 USD | 0.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD | 10.50 USD |
| `7D` | `1.31` | 29,500.00 USD | 0.00 USD | 29,500.00 USD | 0.00 USD | 0.00 USD | 743.40 USD |
| `1D` | `1.31` | 2,980.00 USD | 0.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | 249.97 USD |
| `7D` | `1.31` | 28,760.00 USD | 0.00 USD | 28,760.00 USD | 0.00 USD | 0.00 USD | 221.57 USD |
| `1D` | `1.31` | 2,730.00 USD | 0.00 USD | 2,730.00 USD | 0.00 USD | 0.00 USD | 271.03 USD |
| `7D` | `1.31` | 28,540.00 USD | 0.00 USD | 28,540.00 USD | 0.00 USD | 0.00 USD | 373.72 USD |
| `1D` | `1.31` | 2,460.00 USD | 0.00 USD | 2,460.00 USD | 0.00 USD | 0.00 USD | 169.13 USD |
| `1D` | `1.32` | 2,290.00 USD | 0.00 USD | 2,290.00 USD | 0.00 USD | 0.00 USD | 7.71 USD |
| `7D` | `1.32` | 28,160.00 USD | 0.00 USD | 28,160.00 USD | 0.00 USD | 0.00 USD | 3,320.00 USD |
| `7D` | `1.32` | 24,840.00 USD | 0.00 USD | 24,840.00 USD | 0.00 USD | 0.00 USD | 770.79 USD |
| `7D` | `1.32` | 24,070.00 USD | 0.00 USD | 24,070.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD |
| `7D` | `1.32` | 21,450.00 USD | 0.00 USD | 21,450.00 USD | 0.00 USD | 0.00 USD | 4,460.00 USD |
| `1D` | `1.32` | 2,280.00 USD | 0.00 USD | 2,280.00 USD | 0.00 USD | 0.00 USD | 854.55 USD |
| `7D` | `1.32` | 16,990.00 USD | 0.00 USD | 16,990.00 USD | 0.00 USD | 0.00 USD | 10,670.00 USD |
| `1D` | `1.32` | 1,420.00 USD | 0.00 USD | 1,420.00 USD | 0.00 USD | 0.00 USD | 7.88 USD |
| `7D` | `1.32` | 6,310.00 USD | 0.00 USD | 6,310.00 USD | 0.00 USD | 0.00 USD | 514.32 USD |
| `1D` | `1.32` | 1,420.00 USD | 0.00 USD | 1,420.00 USD | 0.00 USD | 0.00 USD | 20.99 USD |
| `7D` | `1.33` | 5,800.00 USD | 0.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | 1,560.00 USD |
| `1D` | `1.33` | 1,400.00 USD | 0.00 USD | 1,400.00 USD | 0.00 USD | 0.00 USD | 634.13 USD |
| `7D` | `1.33` | 4,240.00 USD | 0.00 USD | 4,240.00 USD | 0.00 USD | 0.00 USD | 721.57 USD |
| `1D` | `1.33` | 761.59 USD | 0.00 USD | 761.59 USD | 0.00 USD | 0.00 USD | 551.37 USD |
| `7D` | `1.33` | 3,520.00 USD | 0.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD | 198.75 USD |
| `1D` | `1.33` | 210.22 USD | 0.00 USD | 210.22 USD | 0.00 USD | 0.00 USD | 210.22 USD |
| `7D` | `1.34` | 3,320.00 USD | 0.00 USD | 3,320.00 USD | 0.00 USD | 0.00 USD | 3,320.00 USD |
| `1D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 770.79 USD | 770.79 USD | 0.00 USD | 0.00 USD | 0.00 USD | 770.79 USD |
| `7D` | `1.35` | 3,400.00 USD | 3,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD |
| `7D` | `1.35` | 7,860.00 USD | 7,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,460.00 USD |
| `1D` | `1.35` | 854.55 USD | 854.55 USD | 0.00 USD | 0.00 USD | 0.00 USD | 854.55 USD |
| `7D` | `1.35` | 18,530.00 USD | 18,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,670.00 USD |
| `1D` | `1.35` | 862.43 USD | 862.43 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7.88 USD |
| `7D` | `1.35` | 18,990.00 USD | 18,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 455.86 USD |
| `1D` | `1.35` | 883.42 USD | 883.42 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20.99 USD |
| `7D` | `1.35` | 20,530.00 USD | 20,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,550.00 USD |
| `1D` | `1.35` | 1,450.00 USD | 1,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 564.48 USD |
| `7D` | `1.35` | 21,110.00 USD | 21,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 577.10 USD |
| `1D` | `1.35` | 2,040.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 594.95 USD |
| `7D` | `1.35` | 21,530.00 USD | 21,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 416.40 USD |
| `1D` | `1.35` | 2,280.00 USD | 2,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 236.29 USD |
| `7D` | `1.36` | 23,150.00 USD | 23,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,620.00 USD |
| `7D` | `1.36` | 23,200.00 USD | 23,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 56.74 USD |
| `7D` | `1.36` | 23,570.00 USD | 23,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 366.84 USD |
| `7D` | `1.36` | 26,500.00 USD | 26,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,930.00 USD |
| `1D` | `1.36` | 2,290.00 USD | 2,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.63 USD |
| `7D` | `1.36` | 28,460.00 USD | 28,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,960.00 USD |
| `1D` | `1.36` | 2,710.00 USD | 2,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 417.57 USD |
| `7D` | `1.36` | 32,600.00 USD | 32,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,140.00 USD |
| `1D` | `1.36` | 2,720.00 USD | 2,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10.50 USD |
| `7D` | `1.36` | 32,760.00 USD | 32,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 154.05 USD |
| `1D` | `1.36` | 2,950.00 USD | 2,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 228.71 USD |
| `7D` | `1.37` | 33,510.00 USD | 33,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 755.39 USD |
| `1D` | `1.37` | 3,040.00 USD | 3,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 90.47 USD |
| `7D` | `1.37` | 33,900.00 USD | 33,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 386.42 USD |
| `1D` | `1.37` | 3,390.00 USD | 3,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 352.67 USD |
| `7D` | `1.37` | 33,950.00 USD | 33,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 50.79 USD |
| `1D` | `1.37` | 3,420.00 USD | 3,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25.99 USD |
| `7D` | `1.38` | 34,760.00 USD | 34,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 810.32 USD |
| `7D` | `1.38` | 34,790.00 USD | 34,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28.38 USD |
| `7D` | `1.39` | 34,970.00 USD | 34,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 183.43 USD |
| `7D` | `1.39` | 36,430.00 USD | 36,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `1.39` | 3,420.00 USD | 3,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.29 USD |
| `7D` | `1.39` | 37,420.00 USD | 37,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 980.51 USD |
| `1D` | `1.39` | 3,630.00 USD | 3,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 212.31 USD |
| `7D` | `1.39` | 39,420.00 USD | 39,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,010.00 USD |
| `1D` | `1.39` | 3,640.00 USD | 3,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.25 USD |
| `7D` | `1.39` | 39,560.00 USD | 39,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 139.71 USD |
| `1D` | `1.39` | 3,750.00 USD | 3,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 110.54 USD |
| `7D` | `1.39` | 39,930.00 USD | 39,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 366.19 USD |
| `1D` | `1.39` | 3,800.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 47.99 USD |
| `7D` | `1.39` | 40,130.00 USD | 40,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 204.69 USD |
| `1D` | `1.39` | 3,980.00 USD | 3,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 177.41 USD |
| `7D` | `1.40` | 40,160.00 USD | 40,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25.39 USD |
| `1D` | `1.40` | 3,990.00 USD | 3,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12.99 USD |
| `7D` | `1.46` | 40,480.00 USD | 40,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 324.13 USD |
| `7D` | `1.46` | 40,490.00 USD | 40,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10.24 USD |
| `7D` | `1.47` | 40,560.00 USD | 40,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65.91 USD |
| `7D` | `1.47` | 41,140.00 USD | 41,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 581.37 USD |
| `7D` | `1.47` | 41,470.00 USD | 41,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 327.81 USD |
| `1D` | `1.47` | 4,070.00 USD | 4,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 84.79 USD |
| `7D` | `1.47` | 42,140.00 USD | 42,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 667.63 USD |
| `7D` | `1.47` | 42,180.00 USD | 42,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 40.89 USD |
| `1D` | `1.47` | 4,080.00 USD | 4,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2.10 USD |
| `7D` | `1.47` | 42,320.00 USD | 42,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 139.01 USD |
| `1D` | `1.47` | 4,130.00 USD | 4,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 53.90 USD |
| `7D` | `1.47` | 42,340.00 USD | 42,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23.13 USD |
| `1D` | `1.47` | 4,170.00 USD | 4,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 40.21 USD |
| `7D` | `1.48` | 42,390.00 USD | 42,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 54.87 USD |
| `1D` | `1.48` | 4,190.00 USD | 4,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20.96 USD |

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
| `10:40:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 609.80 USD | 82.91 USD | 526.89 USD | -443.98 USD | `-72.81%` | `0B / 1S` |
| `10:45:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 1,591.09 USD | 1,135.75 USD | 455.34 USD | 680.40 USD | `+42.76%` | `1B / 0S` |
| `10:45:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 457.07 USD | 330.77 USD | 126.30 USD | 204.48 USD | `+44.74%` | `1B / 0S` |
| `10:50:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 478.34 USD | 52.76 USD | 425.58 USD | -372.82 USD | `-77.94%` | `0B / 1S` |
| `10:55:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 655.47 USD | 546.23 USD | 109.25 USD | 436.98 USD | `+66.67%` | `1B / 0S` |
| `11:00:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 7,398.15 USD | 6,001.30 USD | 1,396.85 USD | 4,604.44 USD | `+62.24%` | `1B / 0S` |
| `11:00:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 819.45 USD | 674.85 USD | 144.61 USD | 530.24 USD | `+64.71%` | `1B / 0S` |
| `11:00:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 2,066.50 USD | 1,458.70 USD | 607.79 USD | 850.91 USD | `+41.18%` | `1B / 0S` |
| `11:05:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 601.92 USD | 94.53 USD | 507.38 USD | -412.85 USD | `-68.59%` | `0B / 1S` |
| `11:10:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 645.03 USD | 602.24 USD | 42.78 USD | 559.46 USD | `+86.73%` | `1B / 0S` |

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
  * Execution Entry: `1.34` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1.34` (Risk Distance: `0.000900` pts)
  * +2.5R Take Profit: `1.34`
  * Mathematical Lot Sizing: **`0.11 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.34` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.34` (Risk Distance: `0.000900` pts)
  * +2.5R Take Profit: `1.34`
  * Mathematical Lot Sizing: **`0.11 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.35`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
