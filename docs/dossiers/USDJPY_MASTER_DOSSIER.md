# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USDJPY
**Canonical Key**: `USDJPY` | **Broker Instrument**: `USDJPY.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 08:30:45 IST` (`2026-10-30 03:00:45 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `157.48` | **Live Ask Quote**: `157.48` | **Mid Price**: `157.48`
- **Spread Points**: `2.00` | **Spread BPS**: `0.13 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `157.47` | VWAP Z-Score: `-0.09` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1214` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `40.37` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `157.87` | Lower -3.00σ Band: `157.07`
  * Upper +2.51σ Band: `157.80` | Lower -2.51σ Band: `157.13`
  * Upper +2.01σ Band: `157.73` | Lower -2.01σ Band: `157.20`
  * Upper +2.00σ Band: `157.73` | Lower -2.00σ Band: `157.20`
  * Upper +1.28σ Band: `157.64` | Lower -1.28σ Band: `157.30`
  * Upper +1.00σ Band: `157.60` | Lower -1.00σ Band: `157.34`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`157.49` | EMA-20=`157.56` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`157.69` (Slope: `+0.0000`) | EMA-100=`157.77`
  * Institutional Anchors: EMA-144=`157.80` | EMA-200=`157.81` (Slope: `-0.0242`) | EMA-233=`157.82`
- **Range Boundaries**: 24H High=`158.13` | 24H Low=`157.19` | Weekly High=`158.35` | Weekly Low=`157.19`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `157.65` (Distance: `-0.10%`)
  * Point of Control (POC) = `157.45` (Distance: `+0.03%`)
  * Value Area Low (VAL) = `157.19` (Distance: `+0.19%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`157.99` | POC=`157.87` | VAL=`157.76`
  * Prior Day Extremes: PDH=`158.13` | PDL=`157.60` | PDC=`157.69`
  * Monday Range Blueprint: High=`157.64` | Mid=`157.15` | Low=`156.65`
  * Developing Weekly Value Area: Weekly VAH=`158.07` | Weekly POC=`157.87` | Weekly VAL=`157.46`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`157.90` | Low=`157.19`
  * London Session (08:00-16:00 UTC): High=`158.11` | Low=`156.85`
  * New York Session (13:00-21:00 UTC): High=`158.42` | Low=`156.53`
  * Initial Balance (First Hour): IB High=`157.95` | IB Low=`157.01`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `156.85` - `158.11`
  * Optimal Trade Entry (OTE 0.705): `157.79`
  * Structural Invalidation Anchor (0.786): `158.74`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `157.72` | `157.75` | `157.70` | `157.73` | `429` | 67,664.88 USD | 5,638.74 USD | `+8.33%` | 640,090.47 USD | `+0.01` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `157.73` | `157.75` | `157.72` | `157.73` | `295` | 46,530.35 USD | -6,003.92 USD | `-12.90%` | 634,086.55 USD | `-0.37` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `157.73` | `157.80` | `157.73` | `157.79` | `496` | 78,266.32 USD | 70,439.69 USD | `+90.00%` | 704,526.24 USD | `+1.82` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `157.67` | `157.78` | `157.64` | `157.72` | `1,537` | 242,417.18 USD | 56,275.42 USD | `+23.21%` | 289,055.79 USD | `+0.45` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `157.72` | `157.74` | `157.70` | `157.72` | `756` | 119,239.34 USD | 13,248.82 USD | `+11.11%` | 302,304.61 USD | `+0.18` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `157.72` | `157.80` | `157.70` | `157.79` | `1,220` | 192,509.90 USD | 168,446.16 USD | `+87.50%` | 470,750.77 USD | `+1.25` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `157.64` | `157.70` | `157.64` | `157.65` | `431` | 67,947.58 USD | -13,989.21 USD | `-20.59%` | 131,863.58 USD | `-0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `157.69` | `157.75` | `157.60` | `157.67` | `3,021` | 476,333.15 USD | -14,195.36 USD | `-2.98%` | 117,668.22 USD | `-0.02` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `157.67` | `157.85` | `157.64` | `157.81` | `4,772` | 753,069.32 USD | 465,760.88 USD | `+61.85%` | 583,429.10 USD | `+0.93` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `203` | `0x0911...129a` | `SHORT` | 10,426,180.61 USD | `66,223.20` | `156.58` | `157.48` | `167.72` | -57,160.38 USD | `-0.55%` | `20X Isolated` |
| `1012` | `0x9dea...d617` | `LONG` | 2,135,849.66 USD | `13,566.98` | `157.66` | `157.48` | `149.22` | -3,164.09 USD | `-0.15%` | `50X Isolated` |
| `1091` | `0xec0b...b078` | `SHORT` | 1,986,371.45 USD | `12,617.49` | `158.22` | `157.48` | `162.95` | 9,994.22 USD | `+0.50%` | `20X Isolated` |
| `1115` | `0xc966...f6b6` | `SHORT` | 1,942,750.75 USD | `12,340.41` | `157.61` | `157.48` | `215.27` | 2,165.28 USD | `+0.11%` | `5X Isolated` |
| `1168` | `0xbef1...d2e5` | `LONG` | 1,861,262.11 USD | `11,821.29` | `157.63` | `157.48` | `155.50` | -2,098.50 USD | `-0.11%` | `50X Isolated` |
| `1855` | `0x3d89...eb14` | `LONG` | 1,086,405.00 USD | `6,900.00` | `158.17` | `157.48` | `127.35` | -4,984.60 USD | `-0.46%` | `5X Isolated` |

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
| `02:05:00` | `157.75` | `157.75` | `157.75` | `157.75` | `157.72` | 69,726.38 USD | 63,304.22 USD | 6,422.17 USD | 56,882.05 USD | `+81.58%` | `1B / 0S` |
| `02:10:00` | `157.72` | `157.72` | `157.72` | `157.78` | `157.72` | 48,420.35 USD | 6,443.03 USD | 41,977.32 USD | -35,534.29 USD | `-73.39%` | `0B / 1S` |
| `02:15:00` | `157.72` | `157.72` | `157.72` | `157.74` | `157.70` | 119,239.34 USD | 66,244.08 USD | 52,995.26 USD | 13,248.82 USD | `+11.11%` | `1B / 0S` |
| `02:15:00` | `157.72` | `157.72` | `157.72` | `157.74` | `157.71` | 48,735.79 USD | 21,501.08 USD | 27,234.71 USD | -5,733.62 USD | `-11.76%` | `0B / 1S` |
| `02:20:00` | `157.73` | `157.73` | `157.73` | `157.74` | `157.72` | 43,375.48 USD | 24,645.16 USD | 18,730.32 USD | 5,914.84 USD | `+13.64%` | `1B / 0S` |
| `02:25:00` | `157.72` | `157.72` | `157.72` | `157.74` | `157.70` | 27,128.53 USD | 13,865.69 USD | 13,262.84 USD | 602.86 USD | `+2.22%` | `1B / 0S` |
| `02:30:00` | `157.73` | `157.73` | `157.73` | `157.75` | `157.70` | 67,664.88 USD | 36,651.81 USD | 31,013.07 USD | 5,638.74 USD | `+8.33%` | `1B / 0S` |
| `02:30:00` | `157.79` | `157.79` | `157.79` | `157.80` | `157.70` | 192,509.90 USD | 180,478.03 USD | 12,031.87 USD | 168,446.16 USD | `+87.50%` | `1B / 0S` |
| `02:35:00` | `157.73` | `157.73` | `157.73` | `157.75` | `157.72` | 46,530.35 USD | 20,263.22 USD | 26,267.13 USD | -6,003.92 USD | `-12.90%` | `0B / 1S` |
| `02:40:00` | `157.79` | `157.79` | `157.79` | `157.80` | `157.73` | 78,266.32 USD | 74,353.00 USD | 3,913.32 USD | 70,439.69 USD | `+90.00%` | `1B / 0S` |

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
  * `2026-10-30 08:00:51 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:21:51 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:21:51 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:20:51 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:20:51 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:20:51 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:20:51 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:22:51 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:22:51 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:22:51 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:22:51 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:22:51 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:22:51 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:22:51 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:22:51 IST`: [morningstar.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `157.04` (Risk Distance: `0.1487` pts)
  * +2.5R Take Profit: `157.56`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.15 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `157.65` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `157.80` (Risk Distance: `0.1487` pts)
  * +2.5R Take Profit: `157.28`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.15 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`158.74`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
