# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USDJPY
**Canonical Key**: `USDJPY` | **Broker Instrument**: `USDJPY.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 01:17:49 IST` (`2026-10-29 19:47:49 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `157.91` | **Live Ask Quote**: `157.91` | **Mid Price**: `157.91`
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
  * Session VWAP: `157.88` | VWAP Z-Score: `+0.28` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0797` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.32` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `158.16` | Lower -3.00σ Band: `157.60`
  * Upper +2.51σ Band: `158.12` | Lower -2.51σ Band: `157.64`
  * Upper +2.01σ Band: `158.07` | Lower -2.01σ Band: `157.69`
  * Upper +2.00σ Band: `158.07` | Lower -2.00σ Band: `157.69`
  * Upper +1.28σ Band: `158.00` | Lower -1.28σ Band: `157.76`
  * Upper +1.00σ Band: `157.97` | Lower -1.00σ Band: `157.78`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`157.91` | EMA-20=`157.90` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`157.90` (Slope: `+0.0000`) | EMA-100=`157.90`
  * Institutional Anchors: EMA-144=`157.88` | EMA-200=`157.85` (Slope: `+0.0044`) | EMA-233=`157.85`
- **Range Boundaries**: 24H High=`158.13` | 24H Low=`157.60` | Weekly High=`158.35` | Weekly Low=`157.37`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `157.97` (Distance: `-0.04%`)
  * Point of Control (POC) = `157.87` (Distance: `+0.02%`)
  * Value Area Low (VAL) = `157.76` (Distance: `+0.10%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`158.04` | POC=`157.89` | VAL=`157.79`
  * Prior Day Extremes: PDH=`158.35` | PDL=`157.65` | PDC=`157.82`
  * Monday Range Blueprint: High=`157.64` | Mid=`157.15` | Low=`156.65`
  * Developing Weekly Value Area: Weekly VAH=`158.08` | Weekly POC=`157.87` | Weekly VAL=`157.47`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`158.07` | Low=`157.60`
  * London Session (08:00-16:00 UTC): High=`158.08` | Low=`157.77`
  * New York Session (13:00-21:00 UTC): High=`158.13` | Low=`157.71`
  * Initial Balance (First Hour): IB High=`157.91` | IB Low=`157.80`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `157.28` - `158.54`
  * Optimal Trade Entry (OTE 0.705): `158.23`
  * Structural Invalidation Anchor (0.786): `159.17`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `157.85` | `157.88` | `157.83` | `157.85` | `367` | 57,932.05 USD | 0.00 USD | `+0.00%` | -256,033.33 USD | `-0.02` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `157.85` | `157.87` | `157.82` | `157.82` | `268` | 42,297.10 USD | -34,021.58 USD | `-80.43%` | -290,054.91 USD | `-0.58` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `157.83` | `157.88` | `157.82` | `157.88` | `280` | 44,207.24 USD | 39,786.52 USD | `+90.00%` | -250,268.40 USD | `+0.75` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `157.82` | `157.88` | `157.78` | `157.78` | `1,388` | 218,998.64 USD | -139,362.77 USD | `-63.64%` | -1,338,564.42 USD | `-0.68` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `157.78` | `157.85` | `157.76` | `157.85` | `1,148` | 181,211.80 USD | 154,328.73 USD | `+85.16%` | -1,184,235.69 USD | `+0.98` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `157.85` | `157.88` | `157.82` | `157.88` | `915` | 144,462.95 USD | 105,480.88 USD | `+73.02%` | -1,078,754.81 USD | `+0.65` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `157.83` | `158.01` | `157.81` | `157.86` | `11,030` | 1,741,162.71 USD | -351,663.40 USD | `-20.20%` | -2,046,522.99 USD | `-0.53` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `157.86` | `157.91` | `157.77` | `157.82` | `7,013` | 1,106,791.66 USD | -321,457.87 USD | `-29.04%` | -2,367,980.86 USD | `-0.61` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `157.82` | `157.93` | `157.76` | `157.88` | `4,599` | 726,108.52 USD | 298,606.76 USD | `+41.12%` | -2,069,374.10 USD | `+0.57` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `157.82` | `157.97` | `157.77` | `157.87` | `20,616` | 3,254,647.92 USD | 426,971.14 USD | `+13.12%` | -4,489,221.92 USD | `+0.58` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `157.87` | `158.08` | `157.81` | `158.06` | `23,822` | 3,765,376.79 USD | 3,094,533.80 USD | `+82.18%` | -1,394,688.13 USD | `+1.15` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `158.06` | `158.13` | `157.71` | `157.88` | `37,561` | 5,930,280.92 USD | -1,786,229.19 USD | `-30.12%` | -3,180,917.32 USD | `-0.46` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.74` | `158.07` | `157.70` | `157.97` | `16,828` | 2,658,251.85 USD | 1,390,029.27 USD | `+52.29%` | -4,212,101.36 USD | `+1.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `157.97` | `158.00` | `157.60` | `157.82` | `28,963` | 4,570,824.81 USD | -704,091.70 USD | `-15.40%` | -4,916,193.06 USD | `+0.32` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.82` | `157.97` | `157.77` | `157.87` | `20,616` | 3,254,647.92 USD | 426,971.14 USD | `+13.12%` | -4,489,221.92 USD | `+0.58` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `157.87` | `158.08` | `157.81` | `158.06` | `23,822` | 3,765,376.79 USD | 3,094,533.80 USD | `+82.18%` | -1,394,688.13 USD | `+1.15` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `158.06` | `158.13` | `157.71` | `157.88` | `37,561` | 5,930,280.92 USD | -1,786,229.19 USD | `-30.12%` | -3,180,917.32 USD | `-0.46` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `209` | `0x0911...129a` | `SHORT` | 10,452,669.89 USD | `66,223.20` | `156.58` | `157.85` | `167.73` | -83,649.66 USD | `-0.80%` | `20X Isolated` |
| `1144` | `0xec0b...b078` | `SHORT` | 1,991,544.62 USD | `12,617.49` | `158.22` | `157.85` | `162.95` | 4,821.05 USD | `+0.24%` | `20X Isolated` |
| `1167` | `0xc966...f6b6` | `SHORT` | 1,966,448.06 USD | `12,458.49` | `157.61` | `157.85` | `215.28` | -2,921.99 USD | `-0.15%` | `5X Isolated` |
| `1236` | `0xbef1...d2e5` | `LONG` | 1,865,872.41 USD | `11,821.29` | `157.63` | `157.85` | `155.51` | 2,511.80 USD | `+0.13%` | `50X Isolated` |
| `1527` | `0x9dea...d617` | `LONG` | 1,467,304.32 USD | `9,296.15` | `157.69` | `157.85` | `146.10` | 1,387.44 USD | `+0.09%` | `50X Isolated` |
| `1902` | `0x3d89...eb14` | `LONG` | 1,089,096.00 USD | `6,900.00` | `158.17` | `157.85` | `127.36` | -2,293.60 USD | `-0.21%` | `5X Isolated` |

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
| `7D` | `141.85` | 89,320.00 USD | 0.00 USD | 89,320.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `141.95` | 3,450.00 USD | 0.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | 93.18 USD |
| `7D` | `142.01` | 87,310.00 USD | 0.00 USD | 87,310.00 USD | 0.00 USD | 0.00 USD | 842.42 USD |
| `7D` | `142.17` | 86,470.00 USD | 0.00 USD | 86,470.00 USD | 0.00 USD | 0.00 USD | 882.48 USD |
| `7D` | `142.33` | 85,580.00 USD | 0.00 USD | 85,580.00 USD | 0.00 USD | 0.00 USD | 454.97 USD |
| `7D` | `150.49` | 85,130.00 USD | 0.00 USD | 85,130.00 USD | 0.00 USD | 0.00 USD | 546.45 USD |
| `7D` | `150.65` | 84,580.00 USD | 0.00 USD | 84,580.00 USD | 0.00 USD | 0.00 USD | 134.84 USD |
| `7D` | `150.81` | 84,450.00 USD | 0.00 USD | 84,450.00 USD | 0.00 USD | 0.00 USD | 31.79 USD |
| `7D` | `150.97` | 84,420.00 USD | 0.00 USD | 84,420.00 USD | 0.00 USD | 0.00 USD | 55.09 USD |
| `1D` | `151.07` | 3,360.00 USD | 0.00 USD | 3,360.00 USD | 0.00 USD | 0.00 USD | 18.10 USD |
| `7D` | `151.13` | 84,360.00 USD | 0.00 USD | 84,360.00 USD | 0.00 USD | 0.00 USD | 171.31 USD |
| `1D` | `151.23` | 3,340.00 USD | 0.00 USD | 3,340.00 USD | 0.00 USD | 0.00 USD | 220.36 USD |
| `7D` | `151.29` | 84,190.00 USD | 0.00 USD | 84,190.00 USD | 0.00 USD | 0.00 USD | 2,990.00 USD |
| `1D` | `151.39` | 3,120.00 USD | 0.00 USD | 3,120.00 USD | 0.00 USD | 0.00 USD | 241.08 USD |
| `7D` | `151.45` | 81,200.00 USD | 0.00 USD | 81,200.00 USD | 0.00 USD | 0.00 USD | 3,310.00 USD |
| `7D` | `151.61` | 77,890.00 USD | 0.00 USD | 77,890.00 USD | 0.00 USD | 0.00 USD | 3,790.00 USD |
| `7D` | `151.77` | 74,100.00 USD | 0.00 USD | 74,100.00 USD | 0.00 USD | 0.00 USD | 1,140.00 USD |
| `7D` | `153.53` | 72,970.00 USD | 0.00 USD | 72,970.00 USD | 0.00 USD | 0.00 USD | 147.71 USD |
| `7D` | `153.69` | 72,820.00 USD | 0.00 USD | 72,820.00 USD | 0.00 USD | 0.00 USD | 1,190.00 USD |
| `7D` | `153.85` | 71,630.00 USD | 0.00 USD | 71,630.00 USD | 0.00 USD | 0.00 USD | 65.54 USD |
| `7D` | `154.01` | 71,570.00 USD | 0.00 USD | 71,570.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `7D` | `154.17` | 71,540.00 USD | 0.00 USD | 71,540.00 USD | 0.00 USD | 0.00 USD | 334.35 USD |
| `1D` | `154.27` | 2,880.00 USD | 0.00 USD | 2,880.00 USD | 0.00 USD | 0.00 USD | 36.17 USD |
| `7D` | `154.33` | 71,210.00 USD | 0.00 USD | 71,210.00 USD | 0.00 USD | 0.00 USD | 1,580.00 USD |
| `1D` | `154.43` | 2,840.00 USD | 0.00 USD | 2,840.00 USD | 0.00 USD | 0.00 USD | 743.42 USD |
| `7D` | `154.49` | 69,630.00 USD | 0.00 USD | 69,630.00 USD | 0.00 USD | 0.00 USD | 8,920.00 USD |
| `1D` | `154.59` | 2,100.00 USD | 0.00 USD | 2,100.00 USD | 0.00 USD | 0.00 USD | 179.42 USD |
| `7D` | `154.65` | 60,710.00 USD | 0.00 USD | 60,710.00 USD | 0.00 USD | 0.00 USD | 4,320.00 USD |
| `7D` | `154.81` | 56,390.00 USD | 0.00 USD | 56,390.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD |
| `7D` | `154.97` | 50,920.00 USD | 0.00 USD | 50,920.00 USD | 0.00 USD | 0.00 USD | 2,270.00 USD |
| `7D` | `155.13` | 48,640.00 USD | 0.00 USD | 48,640.00 USD | 0.00 USD | 0.00 USD | 1,810.00 USD |
| `7D` | `155.29` | 46,840.00 USD | 0.00 USD | 46,840.00 USD | 0.00 USD | 0.00 USD | 919.37 USD |
| `7D` | `155.45` | 45,920.00 USD | 0.00 USD | 45,920.00 USD | 0.00 USD | 0.00 USD | 73.64 USD |
| `7D` | `155.61` | 45,850.00 USD | 0.00 USD | 45,850.00 USD | 0.00 USD | 0.00 USD | 53.52 USD |
| `7D` | `155.77` | 45,790.00 USD | 0.00 USD | 45,790.00 USD | 0.00 USD | 0.00 USD | 668.68 USD |
| `1D` | `155.87` | 1,920.00 USD | 0.00 USD | 1,920.00 USD | 0.00 USD | 0.00 USD | 230.34 USD |
| `7D` | `155.93` | 45,120.00 USD | 0.00 USD | 45,120.00 USD | 0.00 USD | 0.00 USD | 4,320.00 USD |
| `1D` | `156.03` | 1,690.00 USD | 0.00 USD | 1,690.00 USD | 0.00 USD | 0.00 USD | 1,330.00 USD |
| `7D` | `156.09` | 40,810.00 USD | 0.00 USD | 40,810.00 USD | 0.00 USD | 0.00 USD | 19,380.00 USD |
| `1D` | `156.19` | 354.43 USD | 0.00 USD | 354.43 USD | 0.00 USD | 0.00 USD | 354.43 USD |
| `7D` | `156.25` | 21,420.00 USD | 0.00 USD | 21,420.00 USD | 0.00 USD | 0.00 USD | 5,940.00 USD |
| `7D` | `156.41` | 15,490.00 USD | 0.00 USD | 15,490.00 USD | 0.00 USD | 0.00 USD | 10,940.00 USD |
| `7D` | `156.57` | 4,550.00 USD | 0.00 USD | 4,550.00 USD | 0.00 USD | 0.00 USD | 4,550.00 USD |
| `1D` | `157.64` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `157.64` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `158.17` | 14.43 USD | 14.43 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14.43 USD |
| `7D` | `158.33` | 2,190.00 USD | 2,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,170.00 USD |
| `7D` | `158.49` | 2,730.00 USD | 2,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 539.34 USD |
| `7D` | `158.65` | 2,850.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 127.16 USD |
| `7D` | `158.81` | 3,070.00 USD | 3,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 220.37 USD |
| `1D` | `158.91` | 72.36 USD | 72.36 USD | 0.00 USD | 0.00 USD | 0.00 USD | 72.36 USD |
| `7D` | `158.97` | 3,520.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 448.31 USD |
| `1D` | `159.07` | 435.77 USD | 435.77 USD | 0.00 USD | 0.00 USD | 0.00 USD | 363.41 USD |
| `7D` | `159.13` | 12,120.00 USD | 12,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,600.00 USD |
| `1D` | `159.23` | 1,920.00 USD | 1,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,480.00 USD |
| `7D` | `159.29` | 28,750.00 USD | 28,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,630.00 USD |
| `7D` | `159.45` | 33,160.00 USD | 33,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,410.00 USD |
| `7D` | `159.61` | 48,640.00 USD | 48,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,490.00 USD |
| `7D` | `159.77` | 48,740.00 USD | 48,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 98.29 USD |
| `7D` | `159.93` | 49,740.00 USD | 49,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 994.65 USD |
| `7D` | `160.09` | 50,040.00 USD | 50,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 306.49 USD |
| `7D` | `160.25` | 50,070.00 USD | 50,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `7D` | `160.41` | 50,180.00 USD | 50,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 110.19 USD |
| `1D` | `160.51` | 1,950.00 USD | 1,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 36.17 USD |
| `7D` | `160.57` | 50,410.00 USD | 50,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 224.16 USD |
| `1D` | `160.67` | 2,150.00 USD | 2,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 200.22 USD |
| `7D` | `160.73` | 56,400.00 USD | 56,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,000.00 USD |
| `1D` | `160.83` | 2,880.00 USD | 2,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 722.62 USD |
| `7D` | `160.89` | 63,120.00 USD | 63,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,720.00 USD |
| `7D` | `161.05` | 65,220.00 USD | 65,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,110.00 USD |
| `7D` | `161.21` | 72,970.00 USD | 72,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,740.00 USD |
| `7D` | `162.97` | 73,420.00 USD | 73,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 451.44 USD |
| `7D` | `163.13` | 73,650.00 USD | 73,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 229.85 USD |
| `7D` | `163.29` | 73,670.00 USD | 73,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18.41 USD |
| `7D` | `163.45` | 73,680.00 USD | 73,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `7D` | `163.61` | 73,850.00 USD | 73,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 167.17 USD |
| `1D` | `163.71` | 2,900.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18.10 USD |
| `7D` | `163.77` | 74,040.00 USD | 74,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 188.72 USD |
| `1D` | `163.87` | 3,150.00 USD | 3,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 253.21 USD |
| `7D` | `163.93` | 78,990.00 USD | 78,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,960.00 USD |
| `1D` | `164.03` | 3,360.00 USD | 3,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 208.23 USD |
| `7D` | `164.09` | 81,260.00 USD | 81,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,260.00 USD |
| `7D` | `164.25` | 83,990.00 USD | 83,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD |
| `7D` | `164.41` | 85,130.00 USD | 85,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,140.00 USD |
| `7D` | `172.41` | 85,350.00 USD | 85,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 217.16 USD |
| `7D` | `172.57` | 85,400.00 USD | 85,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 53.46 USD |
| `7D` | `172.73` | 85,410.00 USD | 85,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7.36 USD |
| `7D` | `172.89` | 85,410.00 USD | 85,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.35 USD |
| `7D` | `173.05` | 85,480.00 USD | 85,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 66.87 USD |
| `1D` | `173.15` | 3,360.00 USD | 3,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7.24 USD |
| `7D` | `173.21` | 85,500.00 USD | 85,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23.69 USD |
| `1D` | `173.31` | 3,450.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 84.17 USD |
| `7D` | `173.37` | 87,490.00 USD | 87,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,990.00 USD |
| `1D` | `173.42` | 3,530.00 USD | 3,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 84.45 USD |
| `7D` | `173.53` | 87,920.00 USD | 87,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 421.31 USD |

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
  * Current Rate: `-140.91` | Last 24h: `-640.25` | Last 3d: `-882.53` | Last 7d: `-882.53`
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
| `19:00:00` | `157.87` | `157.87` | `157.87` | `157.88` | `157.81` | 81,462.47 USD | 74,780.00 USD | 6,682.47 USD | 68,097.53 USD | `+83.59%` | `1B / 0S` |
| `19:00:00` | `157.88` | `157.88` | `157.88` | `157.93` | `157.76` | 726,108.52 USD | 512,357.64 USD | 213,750.88 USD | 298,606.76 USD | `+41.12%` | `1B / 0S` |
| `19:05:00` | `157.84` | `157.84` | `157.84` | `157.88` | `157.83` | 68,500.82 USD | 6,915.95 USD | 61,584.88 USD | -54,668.93 USD | `-79.81%` | `0B / 1S` |
| `19:10:00` | `157.78` | `157.78` | `157.78` | `157.84` | `157.78` | 69,107.64 USD | 4,248.42 USD | 64,859.22 USD | -60,610.80 USD | `-87.70%` | `0B / 1S` |
| `19:15:00` | `157.85` | `157.85` | `157.85` | `157.85` | `157.76` | 181,211.80 USD | 167,770.27 USD | 13,441.53 USD | 154,328.73 USD | `+85.16%` | `1B / 0S` |
| `19:15:00` | `157.83` | `157.83` | `157.83` | `157.83` | `157.76` | 63,762.11 USD | 55,127.66 USD | 8,634.45 USD | 46,493.20 USD | `+72.92%` | `1B / 0S` |
| `19:20:00` | `157.81` | `157.81` | `157.81` | `157.84` | `157.79` | 69,438.16 USD | 28,368.03 USD | 41,070.13 USD | -12,702.10 USD | `-18.29%` | `0B / 1S` |
| `19:25:00` | `157.85` | `157.85` | `157.85` | `157.85` | `157.81` | 47,986.40 USD | 44,987.25 USD | 2,999.15 USD | 41,988.10 USD | `+87.50%` | `1B / 0S` |
| `19:30:00` | `157.88` | `157.88` | `157.88` | `157.88` | `157.82` | 144,462.95 USD | 124,971.91 USD | 19,491.03 USD | 105,480.88 USD | `+73.02%` | `1B / 0S` |
| `19:30:00` | `157.85` | `157.85` | `157.85` | `157.88` | `157.83` | 57,932.05 USD | 28,966.03 USD | 28,966.03 USD | 0.00 USD | `+0.00%` | `1B / 0S` |

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
  * `2026-10-30 00:58:08 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:08 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:17:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:09:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:09:08 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:08 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:08 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `157.76` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `157.66` (Risk Distance: `0.0971` pts)
  * +2.5R Take Profit: `158.00`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `157.97` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `158.07` (Risk Distance: `0.0971` pts)
  * +2.5R Take Profit: `157.73`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`159.17`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
