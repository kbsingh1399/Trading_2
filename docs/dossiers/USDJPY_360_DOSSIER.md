# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USDJPY
**Canonical Key**: `USDJPY` | **Broker Instrument**: `USDJPY.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 09:31:16 IST` (`2026-10-30 04:01:16 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `157.45` | **Live Ask Quote**: `157.45` | **Mid Price**: `157.45`
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
  * Session VWAP: `157.44` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1568` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `45.86` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `157.84` | Lower -3.00σ Band: `157.04`
  * Upper +2.51σ Band: `157.77` | Lower -2.51σ Band: `157.11`
  * Upper +2.01σ Band: `157.71` | Lower -2.01σ Band: `157.18`
  * Upper +2.00σ Band: `157.71` | Lower -2.00σ Band: `157.18`
  * Upper +1.28σ Band: `157.61` | Lower -1.28σ Band: `157.27`
  * Upper +1.00σ Band: `157.57` | Lower -1.00σ Band: `157.31`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`157.42` | EMA-20=`157.50` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`157.65` (Slope: `+0.0000`) | EMA-100=`157.74`
  * Institutional Anchors: EMA-144=`157.78` | EMA-200=`157.80` (Slope: `-0.0312`) | EMA-233=`157.81`
- **Range Boundaries**: 24H High=`158.13` | 24H Low=`157.12` | Weekly High=`158.35` | Weekly Low=`157.12`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `157.59` (Distance: `-0.08%`)
  * Point of Control (POC) = `157.45` (Distance: `+0.01%`)
  * Value Area Low (VAL) = `157.19` (Distance: `+0.17%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`157.99` | POC=`157.87` | VAL=`157.76`
  * Prior Day Extremes: PDH=`158.13` | PDL=`157.60` | PDC=`157.69`
  * Monday Range Blueprint: High=`157.64` | Mid=`157.15` | Low=`156.65`
  * Developing Weekly Value Area: Weekly VAH=`158.07` | Weekly POC=`157.87` | Weekly VAL=`157.45`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`157.90` | Low=`157.12`
  * London Session (08:00-16:00 UTC): High=`158.08` | Low=`156.82`
  * New York Session (13:00-21:00 UTC): High=`158.40` | Low=`156.51`
  * Initial Balance (First Hour): IB High=`157.92` | IB Low=`156.98`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `156.82` - `158.08`
  * Optimal Trade Entry (OTE 0.705): `157.77`
  * Structural Invalidation Anchor (0.786): `158.71`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `157.66` | `157.66` | `157.46` | `157.51` | `1,381` | 217,522.69 USD | -132,930.53 USD | `-61.11%` | 147,902.53 USD | `-1.97` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `157.51` | `157.57` | `157.49` | `157.54` | `1,401` | 220,710.74 USD | 70,845.42 USD | `+32.10%` | 218,747.95 USD | `+1.05` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `157.54` | `157.59` | `157.47` | `157.48` | `1,705` | 268,510.22 USD | -161,794.62 USD | `-60.26%` | 56,953.33 USD | `-2.04` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `157.71` | `157.76` | `157.70` | `157.75` | `1,628` | 256,821.88 USD | 170,545.78 USD | `+66.41%` | -282,698.96 USD | `+1.19` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `157.75` | `157.75` | `157.46` | `157.51` | `2,648` | 417,089.13 USD | -304,687.14 USD | `-73.05%` | -587,386.11 USD | `-1.67` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `157.51` | `157.59` | `157.31` | `157.36` | `5,078` | 799,058.85 USD | -483,185.40 USD | `-60.47%` | -1,070,571.51 USD | `-2.26` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `157.69` | `157.75` | `157.60` | `157.67` | `3,021` | 476,333.15 USD | -14,195.36 USD | `-2.98%` | -332,279.86 USD | `-0.02` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `157.67` | `157.85` | `157.64` | `157.81` | `4,772` | 753,069.32 USD | 465,760.88 USD | `+61.85%` | 133,481.03 USD | `+0.93` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `157.81` | `157.90` | `157.31` | `157.36` | `12,235` | 1,925,262.90 USD | -1,548,081.92 USD | `-80.41%` | -1,414,600.89 USD | `-2.67` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `158.06` | `158.13` | `157.71` | `157.88` | `37,561` | 5,930,280.92 USD | -1,786,229.19 USD | `-30.12%` | 1,031,184.04 USD | `-1.13` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.88` | `157.98` | `157.63` | `157.69` | `20,300` | 3,201,147.60 USD | -1,948,126.97 USD | `-60.86%` | -916,942.93 USD | `-0.96` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.64` | `157.90` | `157.31` | `157.36` | `20,459` | 3,219,366.86 USD | -2,125,220.88 USD | `-66.01%` | -3,042,163.81 USD | `-0.88` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.82` | `157.97` | `157.77` | `157.87` | `20,616` | 3,254,647.92 USD | 426,971.14 USD | `+13.12%` | -277,120.56 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `157.87` | `158.08` | `157.81` | `158.06` | `23,822` | 3,765,376.79 USD | 3,094,533.80 USD | `+82.18%` | 2,817,413.23 USD | `+1.35` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `158.06` | `158.13` | `157.71` | `157.88` | `37,561` | 5,930,280.92 USD | -1,786,229.19 USD | `-30.12%` | 1,031,184.04 USD | `-1.13` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.88` | `157.98` | `157.63` | `157.69` | `20,300` | 3,201,147.60 USD | -1,948,126.97 USD | `-60.86%` | -916,942.93 USD | `-0.96` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.64` | `157.90` | `157.31` | `157.36` | `20,459` | 3,219,366.86 USD | -2,125,220.88 USD | `-66.01%` | -3,042,163.81 USD | `-0.88` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `202` | `0x0911...129a` | `SHORT` | 10,422,869.45 USD | `66,223.20` | `156.58` | `157.40` | `167.72` | -53,849.22 USD | `-0.52%` | `20X Isolated` |
| `1025` | `0x9dea...d617` | `LONG` | 2,135,306.98 USD | `13,566.98` | `157.66` | `157.40` | `149.22` | -3,706.77 USD | `-0.17%` | `50X Isolated` |
| `1109` | `0xec0b...b078` | `SHORT` | 1,985,866.75 USD | `12,617.49` | `158.22` | `157.40` | `162.95` | 10,498.92 USD | `+0.53%` | `20X Isolated` |
| `1145` | `0xc966...f6b6` | `SHORT` | 1,942,257.13 USD | `12,340.41` | `157.61` | `157.40` | `215.27` | 2,658.89 USD | `+0.14%` | `5X Isolated` |
| `1184` | `0xbef1...d2e5` | `LONG` | 1,860,552.83 USD | `11,821.29` | `157.63` | `157.40` | `155.50` | -2,807.78 USD | `-0.15%` | `50X Isolated` |
| `1879` | `0x3d89...eb14` | `LONG` | 1,085,991.00 USD | `6,900.00` | `158.17` | `157.40` | `127.35` | -5,398.60 USD | `-0.50%` | `5X Isolated` |

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
| `7D` | `141.75` | 89,580.00 USD | 0.00 USD | 89,580.00 USD | 0.00 USD | 0.00 USD | 176.77 USD |
| `1D` | `141.76` | 4,050.00 USD | 0.00 USD | 4,050.00 USD | 0.00 USD | 0.00 USD | 72.20 USD |
| `7D` | `141.91` | 89,400.00 USD | 0.00 USD | 89,400.00 USD | 0.00 USD | 0.00 USD | 2,160.00 USD |
| `1D` | `141.92` | 3,980.00 USD | 0.00 USD | 3,980.00 USD | 0.00 USD | 0.00 USD | 129.85 USD |
| `7D` | `142.07` | 87,240.00 USD | 0.00 USD | 87,240.00 USD | 0.00 USD | 0.00 USD | 1,030.00 USD |
| `7D` | `142.23` | 86,210.00 USD | 0.00 USD | 86,210.00 USD | 0.00 USD | 0.00 USD | 882.31 USD |
| `7D` | `150.39` | 85,330.00 USD | 0.00 USD | 85,330.00 USD | 0.00 USD | 0.00 USD | 174.55 USD |
| `7D` | `150.55` | 85,160.00 USD | 0.00 USD | 85,160.00 USD | 0.00 USD | 0.00 USD | 373.07 USD |
| `7D` | `150.71` | 84,780.00 USD | 0.00 USD | 84,780.00 USD | 0.00 USD | 0.00 USD | 137.75 USD |
| `7D` | `150.87` | 84,650.00 USD | 0.00 USD | 84,650.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `7D` | `151.03` | 84,630.00 USD | 0.00 USD | 84,630.00 USD | 0.00 USD | 0.00 USD | 55.10 USD |
| `7D` | `151.19` | 84,580.00 USD | 0.00 USD | 84,580.00 USD | 0.00 USD | 0.00 USD | 490.07 USD |
| `1D` | `151.20` | 3,850.00 USD | 0.00 USD | 3,850.00 USD | 0.00 USD | 0.00 USD | 202.41 USD |
| `7D` | `151.35` | 84,090.00 USD | 0.00 USD | 84,090.00 USD | 0.00 USD | 0.00 USD | 5,430.00 USD |
| `1D` | `151.36` | 3,650.00 USD | 0.00 USD | 3,650.00 USD | 0.00 USD | 0.00 USD | 347.97 USD |
| `7D` | `151.51` | 78,650.00 USD | 0.00 USD | 78,650.00 USD | 0.00 USD | 0.00 USD | 2,780.00 USD |
| `7D` | `151.67` | 75,880.00 USD | 0.00 USD | 75,880.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD |
| `7D` | `153.59` | 73,140.00 USD | 0.00 USD | 73,140.00 USD | 0.00 USD | 0.00 USD | 977.93 USD |
| `7D` | `153.75` | 72,160.00 USD | 0.00 USD | 72,160.00 USD | 0.00 USD | 0.00 USD | 356.00 USD |
| `7D` | `153.91` | 71,810.00 USD | 0.00 USD | 71,810.00 USD | 0.00 USD | 0.00 USD | 36.82 USD |
| `7D` | `154.07` | 71,770.00 USD | 0.00 USD | 71,770.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `7D` | `154.23` | 71,740.00 USD | 0.00 USD | 71,740.00 USD | 0.00 USD | 0.00 USD | 651.38 USD |
| `1D` | `154.24` | 3,300.00 USD | 0.00 USD | 3,300.00 USD | 0.00 USD | 0.00 USD | 6.00 USD |
| `7D` | `154.39` | 71,090.00 USD | 0.00 USD | 71,090.00 USD | 0.00 USD | 0.00 USD | 4,290.00 USD |
| `1D` | `154.40` | 3,300.00 USD | 0.00 USD | 3,300.00 USD | 0.00 USD | 0.00 USD | 828.25 USD |
| `7D` | `154.55` | 66,800.00 USD | 0.00 USD | 66,800.00 USD | 0.00 USD | 0.00 USD | 7,530.00 USD |
| `1D` | `154.56` | 2,470.00 USD | 0.00 USD | 2,470.00 USD | 0.00 USD | 0.00 USD | 266.50 USD |
| `7D` | `154.71` | 59,280.00 USD | 0.00 USD | 59,280.00 USD | 0.00 USD | 0.00 USD | 5,050.00 USD |
| `7D` | `154.87` | 54,230.00 USD | 0.00 USD | 54,230.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD |
| `7D` | `155.03` | 48,760.00 USD | 0.00 USD | 48,760.00 USD | 0.00 USD | 0.00 USD | 39.84 USD |
| `7D` | `155.19` | 48,720.00 USD | 0.00 USD | 48,720.00 USD | 0.00 USD | 0.00 USD | 2,150.00 USD |
| `7D` | `155.35` | 46,580.00 USD | 0.00 USD | 46,580.00 USD | 0.00 USD | 0.00 USD | 482.11 USD |
| `7D` | `155.51` | 46,090.00 USD | 0.00 USD | 46,090.00 USD | 0.00 USD | 0.00 USD | 127.17 USD |
| `7D` | `155.67` | 45,970.00 USD | 0.00 USD | 45,970.00 USD | 0.00 USD | 0.00 USD | 220.39 USD |
| `7D` | `155.83` | 45,750.00 USD | 0.00 USD | 45,750.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD |
| `1D` | `155.84` | 2,200.00 USD | 0.00 USD | 2,200.00 USD | 0.00 USD | 0.00 USD | 11.99 USD |
| `7D` | `155.99` | 44,660.00 USD | 0.00 USD | 44,660.00 USD | 0.00 USD | 0.00 USD | 11,180.00 USD |
| `1D` | `156.00` | 2,190.00 USD | 0.00 USD | 2,190.00 USD | 0.00 USD | 0.00 USD | 1,920.00 USD |
| `7D` | `156.15` | 33,490.00 USD | 0.00 USD | 33,490.00 USD | 0.00 USD | 0.00 USD | 18,340.00 USD |
| `1D` | `156.16` | 270.89 USD | 0.00 USD | 270.89 USD | 0.00 USD | 0.00 USD | 270.89 USD |
| `7D` | `156.31` | 15,150.00 USD | 0.00 USD | 15,150.00 USD | 0.00 USD | 0.00 USD | 6,320.00 USD |
| `7D` | `156.47` | 8,820.00 USD | 0.00 USD | 8,820.00 USD | 0.00 USD | 0.00 USD | 8,820.00 USD |
| `1D` | `157.57` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `157.57` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `158.23` | 698.25 USD | 698.25 USD | 0.00 USD | 0.00 USD | 0.00 USD | 698.25 USD |
| `7D` | `158.39` | 2,190.00 USD | 2,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,490.00 USD |
| `7D` | `158.55` | 2,740.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 551.01 USD |
| `7D` | `158.71` | 2,800.00 USD | 2,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 53.53 USD |
| `7D` | `158.87` | 3,020.00 USD | 3,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 220.39 USD |
| `7D` | `159.03` | 4,700.00 USD | 4,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,690.00 USD |
| `1D` | `159.04` | 632.65 USD | 632.65 USD | 0.00 USD | 0.00 USD | 0.00 USD | 632.65 USD |
| `7D` | `159.19` | 19,590.00 USD | 19,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,890.00 USD |
| `1D` | `159.20` | 1,940.00 USD | 1,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,300.00 USD |
| `7D` | `159.35` | 37,820.00 USD | 37,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18,240.00 USD |
| `1D` | `159.36` | 2,200.00 USD | 2,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 264.37 USD |
| `7D` | `159.51` | 48,760.00 USD | 48,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,940.00 USD |
| `7D` | `159.83` | 49,600.00 USD | 49,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 841.62 USD |
| `7D` | `159.99` | 49,860.00 USD | 49,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 253.62 USD |
| `7D` | `160.15` | 50,130.00 USD | 50,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 275.51 USD |
| `7D` | `160.31` | 50,160.00 USD | 50,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `7D` | `160.47` | 50,270.00 USD | 50,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 110.19 USD |
| `7D` | `160.63` | 51,230.00 USD | 51,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 966.22 USD |
| `1D` | `160.64` | 2,560.00 USD | 2,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 362.44 USD |
| `7D` | `160.79` | 61,850.00 USD | 61,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,610.00 USD |
| `1D` | `160.80` | 3,300.00 USD | 3,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 735.28 USD |
| `7D` | `160.95` | 67,670.00 USD | 67,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,830.00 USD |
| `1D` | `160.96` | 3,300.00 USD | 3,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.03 USD |
| `7D` | `161.11` | 73,140.00 USD | 73,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD |
| `7D` | `162.87` | 73,170.00 USD | 73,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33.40 USD |
| `7D` | `163.03` | 73,690.00 USD | 73,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 513.03 USD |
| `7D` | `163.19` | 73,810.00 USD | 73,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 120.53 USD |
| `7D` | `163.35` | 73,840.00 USD | 73,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31.79 USD |
| `7D` | `163.67` | 74,170.00 USD | 74,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 325.69 USD |
| `1D` | `163.68` | 3,310.00 USD | 3,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.00 USD |
| `7D` | `163.83` | 75,030.00 USD | 75,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 864.26 USD |
| `1D` | `163.84` | 3,720.00 USD | 3,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 413.04 USD |
| `7D` | `163.99` | 80,010.00 USD | 80,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,980.00 USD |
| `1D` | `164.00` | 3,850.00 USD | 3,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 134.34 USD |
| `7D` | `164.15` | 82,600.00 USD | 82,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,590.00 USD |
| `7D` | `164.31` | 85,330.00 USD | 85,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD |
| `7D` | `172.31` | 85,370.00 USD | 85,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 38.39 USD |
| `7D` | `172.47` | 85,550.00 USD | 85,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 178.73 USD |
| `7D` | `172.63` | 85,600.00 USD | 85,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 47.74 USD |
| `7D` | `172.79` | 85,610.00 USD | 85,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12.71 USD |
| `7D` | `173.11` | 85,740.00 USD | 85,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 130.28 USD |
| `1D` | `173.12` | 3,850.00 USD | 3,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1.20 USD |
| `7D` | `173.27` | 85,840.00 USD | 85,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 95.66 USD |
| `1D` | `173.28` | 3,990.00 USD | 3,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 138.74 USD |
| `1D` | `173.35` | 4,030.00 USD | 4,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 35.02 USD |
| `7D` | `173.43` | 87,950.00 USD | 87,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,110.00 USD |
| `7D` | `173.55` | 89,000.00 USD | 89,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,050.00 USD |

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
  * Current Rate: `0.00` | Last 24h: `-624.43` | Last 3d: `-912.05` | Last 7d: `-912.05`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-0.0117%` | **USDT BingX** | `-` |
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
| `03:15:00` | `157.75` | `157.75` | `157.75` | `157.76` | `157.70` | 256,821.88 USD | 213,683.83 USD | 43,138.05 USD | 170,545.78 USD | `+66.41%` | `1B / 0S` |
| `03:20:00` | `157.73` | `157.73` | `157.73` | `157.76` | `157.71` | 92,586.34 USD | 25,838.05 USD | 66,748.29 USD | -40,910.24 USD | `-44.19%` | `0B / 1S` |
| `03:25:00` | `157.75` | `157.75` | `157.75` | `157.76` | `157.72` | 56,791.08 USD | 42,939.60 USD | 13,851.48 USD | 29,088.11 USD | `+51.22%` | `1B / 0S` |
| `03:30:00` | `157.73` | `157.73` | `157.73` | `157.75` | `157.69` | 117,668.07 USD | 60,997.05 USD | 56,671.02 USD | 4,326.03 USD | `+3.68%` | `1B / 0S` |
| `03:30:00` | `157.51` | `157.51` | `157.51` | `157.75` | `157.46` | 417,089.13 USD | 56,200.99 USD | 360,888.14 USD | -304,687.14 USD | `-73.05%` | `0B / 1S` |
| `03:35:00` | `157.66` | `157.66` | `157.66` | `157.73` | `157.65` | 82,142.42 USD | 8,112.83 USD | 74,029.59 USD | -65,916.76 USD | `-80.25%` | `0B / 1S` |
| `03:40:00` | `157.51` | `157.51` | `157.51` | `157.66` | `157.46` | 217,522.69 USD | 42,296.08 USD | 175,226.61 USD | -132,930.53 USD | `-61.11%` | `0B / 1S` |
| `03:45:00` | `157.54` | `157.54` | `157.54` | `157.57` | `157.49` | 220,710.74 USD | 145,778.08 USD | 74,932.66 USD | 70,845.42 USD | `+32.10%` | `1B / 0S` |
| `03:45:00` | `157.36` | `157.36` | `157.36` | `157.59` | `157.31` | 799,058.85 USD | 157,936.72 USD | 641,122.12 USD | -483,185.40 USD | `-60.47%` | `0B / 1S` |
| `03:50:00` | `157.48` | `157.48` | `157.48` | `157.59` | `157.47` | 268,510.22 USD | 53,357.80 USD | 215,152.42 USD | -161,794.62 USD | `-60.26%` | `0B / 1S` |

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
  * `2026-10-30 09:09:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:28:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:29:56 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `157.19` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `157.00` (Risk Distance: `0.1896` pts)
  * +2.5R Take Profit: `157.66`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.19 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `157.59` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `157.78` (Risk Distance: `0.1896` pts)
  * +2.5R Take Profit: `157.11`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.19 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`158.71`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
