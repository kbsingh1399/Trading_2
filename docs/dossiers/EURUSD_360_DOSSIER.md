# 🏛️ SOVEREIGN CANDIDATE DOSSIER: EURUSD
**Canonical Key**: `EURUSD` | **Broker Instrument**: `EURUSD.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 10:49:58 IST` (`2026-10-30 05:19:58 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `1.12` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0028` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.13` | Lower -3.00σ Band: `1.11`
  * Upper +2.51σ Band: `1.12` | Lower -2.51σ Band: `1.11`
  * Upper +2.01σ Band: `1.12` | Lower -2.01σ Band: `1.11`
  * Upper +2.00σ Band: `1.12` | Lower -2.00σ Band: `1.11`
  * Upper +1.28σ Band: `1.12` | Lower -1.28σ Band: `1.12`
  * Upper +1.00σ Band: `1.12` | Lower -1.00σ Band: `1.12`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.12` | EMA-20=`1.12` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.12` (Slope: `+0.0000`) | EMA-100=`1.12`
  * Institutional Anchors: EMA-144=`1.12` | EMA-200=`1.12` (Slope: `+0.0000`) | EMA-233=`1.12`
- **Range Boundaries**: 24H High=`1.13` | 24H Low=`1.11` | Weekly High=`1.14` | Weekly Low=`1.10`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.12` (Distance: `-0.13%`)
  * Point of Control (POC) = `1.12` (Distance: `-0.10%`)
  * Value Area Low (VAL) = `1.12` (Distance: `+0.01%`)
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
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `345` | 386.22 USD | 78.29 USD | `+20.27%` | 936.13 USD | `+0.37` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `291` | 325.79 USD | 38.58 USD | `+11.84%` | 974.71 USD | `+0.24` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `283` | 316.89 USD | 225.78 USD | `+71.25%` | 1,200.50 USD | `+0.74` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `1,475` | 1,651.37 USD | -1,486.23 USD | `-90.00%` | 6,500.64 USD | `-2.41` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `1,688` | 1,889.58 USD | -984.99 USD | `-52.13%` | 5,515.64 USD | `-1.55` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `919` | 1,029.05 USD | 827.28 USD | `+80.39%` | 6,342.92 USD | `+1.15` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `3,467` | 3,882.21 USD | 3,493.99 USD | `+90.00%` | 10,866.33 USD | `+0.89` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `6,722` | 7,524.74 USD | -4,133.31 USD | `-54.93%` | 6,733.02 USD | `-1.41` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `3,626` | 4,059.81 USD | 829.12 USD | `+20.42%` | 7,562.13 USD | `+0.10` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `14,336` | 16,024.64 USD | 7,816.90 USD | `+48.78%` | 14,899.68 USD | `+0.29` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `6,284` | 7,036.57 USD | 6,332.91 USD | `+90.00%` | 21,232.60 USD | `+0.17` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `15,119` | 16,913.02 USD | -10,827.76 USD | `-64.02%` | 10,404.84 USD | `-0.98` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.11` | `19,887` | 22,130.25 USD | -13,427.34 USD | `-60.67%` | -17,186.01 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.12` | `35,597` | 39,738.71 USD | 24,268.79 USD | `+61.07%` | 7,082.79 USD | `+1.37` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `14,336` | 16,024.64 USD | 7,816.90 USD | `+48.78%` | 14,899.68 USD | `+0.29` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `6,284` | 7,036.57 USD | 6,332.91 USD | `+90.00%` | 21,232.60 USD | `+0.17` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `15,119` | 16,913.02 USD | -10,827.76 USD | `-64.02%` | 10,404.84 USD | `-0.98` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `217` | `0x0911...129a` | `LONG` | 9,957,857.80 USD | `8,898,889.90` | `1.15` | `1.12` | `1.06` | -264,884.62 USD | `-2.66%` | `20X Isolated` |
| `1144` | `0xe03b...ed11` | `SHORT` | 1,949,139.21 USD | `1,741,858.10` | `1.14` | `1.12` | `1.20` | 44,064.11 USD | `+2.26%` | `50X Isolated` |
| `1734` | `0x3f31...a3d7` | `SHORT` | 1,204,617.04 USD | `1,076,512.10` | `1.11` | `1.12` | `1.13` | -4,685.59 USD | `-0.39%` | `50X Isolated` |
| `1852` | `0x9df2...c665` | `SHORT` | 1,118,929.61 USD | `999,937.10` | `1.12` | `1.12` | `1.46` | 1,640.22 USD | `+0.15%` | `5X Isolated` |

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
| `7D` | `1.01` | 119,310.00 USD | 0.00 USD | 119,310.00 USD | 0.00 USD | 0.00 USD | 1,220.00 USD |
| `7D` | `1.01` | 118,090.00 USD | 0.00 USD | 118,090.00 USD | 0.00 USD | 0.00 USD | 560.68 USD |
| `7D` | `1.01` | 117,530.00 USD | 0.00 USD | 117,530.00 USD | 0.00 USD | 0.00 USD | 1,360.00 USD |
| `1D` | `1.01` | 59,410.00 USD | 0.00 USD | 59,410.00 USD | 0.00 USD | 0.00 USD | 711.81 USD |
| `7D` | `1.01` | 116,170.00 USD | 0.00 USD | 116,170.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD |
| `1D` | `1.01` | 58,700.00 USD | 0.00 USD | 58,700.00 USD | 0.00 USD | 0.00 USD | 69.13 USD |
| `7D` | `1.01` | 115,040.00 USD | 0.00 USD | 115,040.00 USD | 0.00 USD | 0.00 USD | 240.69 USD |
| `7D` | `1.01` | 114,800.00 USD | 0.00 USD | 114,800.00 USD | 0.00 USD | 0.00 USD | 130.96 USD |
| `7D` | `1.07` | 114,670.00 USD | 0.00 USD | 114,670.00 USD | 0.00 USD | 0.00 USD | 203.33 USD |
| `1D` | `1.07` | 58,630.00 USD | 0.00 USD | 58,630.00 USD | 0.00 USD | 0.00 USD | 776.05 USD |
| `7D` | `1.07` | 114,470.00 USD | 0.00 USD | 114,470.00 USD | 0.00 USD | 0.00 USD | 2,350.00 USD |
| `1D` | `1.07` | 57,860.00 USD | 0.00 USD | 57,860.00 USD | 0.00 USD | 0.00 USD | 2,350.00 USD |
| `7D` | `1.07` | 112,110.00 USD | 0.00 USD | 112,110.00 USD | 0.00 USD | 0.00 USD | 3,180.00 USD |
| `1D` | `1.07` | 55,500.00 USD | 0.00 USD | 55,500.00 USD | 0.00 USD | 0.00 USD | 35.98 USD |
| `7D` | `1.07` | 108,940.00 USD | 0.00 USD | 108,940.00 USD | 0.00 USD | 0.00 USD | 2,040.00 USD |
| `1D` | `1.07` | 55,470.00 USD | 0.00 USD | 55,470.00 USD | 0.00 USD | 0.00 USD | 528.32 USD |
| `7D` | `1.07` | 106,900.00 USD | 0.00 USD | 106,900.00 USD | 0.00 USD | 0.00 USD | 1,230.00 USD |
| `1D` | `1.08` | 54,940.00 USD | 0.00 USD | 54,940.00 USD | 0.00 USD | 0.00 USD | 2,720.00 USD |
| `7D` | `1.08` | 105,670.00 USD | 0.00 USD | 105,670.00 USD | 0.00 USD | 0.00 USD | 368.34 USD |
| `1D` | `1.08` | 52,210.00 USD | 0.00 USD | 52,210.00 USD | 0.00 USD | 0.00 USD | 1,780.00 USD |
| `7D` | `1.08` | 105,300.00 USD | 0.00 USD | 105,300.00 USD | 0.00 USD | 0.00 USD | 6,150.00 USD |
| `1D` | `1.08` | 50,430.00 USD | 0.00 USD | 50,430.00 USD | 0.00 USD | 0.00 USD | 144.09 USD |
| `7D` | `1.08` | 99,160.00 USD | 0.00 USD | 99,160.00 USD | 0.00 USD | 0.00 USD | 725.37 USD |
| `1D` | `1.08` | 50,290.00 USD | 0.00 USD | 50,290.00 USD | 0.00 USD | 0.00 USD | 33.36 USD |
| `7D` | `1.08` | 98,430.00 USD | 0.00 USD | 98,430.00 USD | 0.00 USD | 0.00 USD | 327.41 USD |
| `7D` | `1.09` | 98,100.00 USD | 0.00 USD | 98,100.00 USD | 0.00 USD | 0.00 USD | 3,790.00 USD |
| `1D` | `1.09` | 50,260.00 USD | 0.00 USD | 50,260.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD |
| `7D` | `1.09` | 94,310.00 USD | 0.00 USD | 94,310.00 USD | 0.00 USD | 0.00 USD | 3,580.00 USD |
| `1D` | `1.10` | 47,320.00 USD | 0.00 USD | 47,320.00 USD | 0.00 USD | 0.00 USD | 3,380.00 USD |
| `7D` | `1.10` | 90,730.00 USD | 0.00 USD | 90,730.00 USD | 0.00 USD | 0.00 USD | 6,350.00 USD |
| `1D` | `1.10` | 43,930.00 USD | 0.00 USD | 43,930.00 USD | 0.00 USD | 0.00 USD | 15.22 USD |
| `7D` | `1.10` | 84,380.00 USD | 0.00 USD | 84,380.00 USD | 0.00 USD | 0.00 USD | 4,280.00 USD |
| `1D` | `1.10` | 43,920.00 USD | 0.00 USD | 43,920.00 USD | 0.00 USD | 0.00 USD | 6,480.00 USD |
| `1D` | `1.10` | 37,430.00 USD | 0.00 USD | 37,430.00 USD | 0.00 USD | 0.00 USD | 3,350.00 USD |
| `7D` | `1.10` | 80,100.00 USD | 0.00 USD | 80,100.00 USD | 0.00 USD | 0.00 USD | 8,640.00 USD |
| `1D` | `1.10` | 34,090.00 USD | 0.00 USD | 34,090.00 USD | 0.00 USD | 0.00 USD | 236.76 USD |
| `7D` | `1.10` | 71,460.00 USD | 0.00 USD | 71,460.00 USD | 0.00 USD | 0.00 USD | 5,020.00 USD |
| `1D` | `1.10` | 33,850.00 USD | 0.00 USD | 33,850.00 USD | 0.00 USD | 0.00 USD | 345.73 USD |
| `7D` | `1.10` | 66,440.00 USD | 0.00 USD | 66,440.00 USD | 0.00 USD | 0.00 USD | 818.97 USD |
| `7D` | `1.10` | 65,620.00 USD | 0.00 USD | 65,620.00 USD | 0.00 USD | 0.00 USD | 654.82 USD |
| `7D` | `1.10` | 64,970.00 USD | 0.00 USD | 64,970.00 USD | 0.00 USD | 0.00 USD | 1,840.00 USD |
| `1D` | `1.10` | 33,500.00 USD | 0.00 USD | 33,500.00 USD | 0.00 USD | 0.00 USD | 3,120.00 USD |
| `7D` | `1.10` | 63,120.00 USD | 0.00 USD | 63,120.00 USD | 0.00 USD | 0.00 USD | 12,760.00 USD |
| `1D` | `1.11` | 30,390.00 USD | 0.00 USD | 30,390.00 USD | 0.00 USD | 0.00 USD | 9,400.00 USD |
| `7D` | `1.11` | 50,370.00 USD | 0.00 USD | 50,370.00 USD | 0.00 USD | 0.00 USD | 8,340.00 USD |
| `1D` | `1.11` | 20,980.00 USD | 0.00 USD | 20,980.00 USD | 0.00 USD | 0.00 USD | 143.97 USD |
| `7D` | `1.11` | 42,030.00 USD | 0.00 USD | 42,030.00 USD | 0.00 USD | 0.00 USD | 8,160.00 USD |
| `1D` | `1.11` | 20,840.00 USD | 0.00 USD | 20,840.00 USD | 0.00 USD | 0.00 USD | 2,110.00 USD |
| `7D` | `1.11` | 33,870.00 USD | 0.00 USD | 33,870.00 USD | 0.00 USD | 0.00 USD | 4,910.00 USD |
| `1D` | `1.11` | 18,730.00 USD | 0.00 USD | 18,730.00 USD | 0.00 USD | 0.00 USD | 10,900.00 USD |
| `7D` | `1.11` | 28,960.00 USD | 0.00 USD | 28,960.00 USD | 0.00 USD | 0.00 USD | 1,470.00 USD |
| `1D` | `1.11` | 7,830.00 USD | 0.00 USD | 7,830.00 USD | 0.00 USD | 0.00 USD | 7,120.00 USD |
| `7D` | `1.11` | 27,490.00 USD | 0.00 USD | 27,490.00 USD | 0.00 USD | 0.00 USD | 23,810.00 USD |
| `1D` | `1.11` | 709.81 USD | 0.00 USD | 709.81 USD | 0.00 USD | 0.00 USD | 435.02 USD |
| `7D` | `1.11` | 3,680.00 USD | 0.00 USD | 3,680.00 USD | 0.00 USD | 0.00 USD | 3,680.00 USD |
| `1D` | `1.11` | 274.79 USD | 0.00 USD | 274.79 USD | 0.00 USD | 0.00 USD | 274.79 USD |
| `1D` | `1.12` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.12` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.13` | 9,160.00 USD | 9,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,160.00 USD |
| `1D` | `1.13` | 5,900.00 USD | 5,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,900.00 USD |
| `7D` | `1.13` | 14,740.00 USD | 14,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,580.00 USD |
| `1D` | `1.13` | 12,650.00 USD | 12,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `1.13` | 27,440.00 USD | 27,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,690.00 USD |
| `1D` | `1.13` | 12,680.00 USD | 12,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 30.43 USD |
| `7D` | `1.13` | 36,000.00 USD | 36,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,570.00 USD |
| `1D` | `1.13` | 25,650.00 USD | 25,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,970.00 USD |
| `1D` | `1.13` | 32,340.00 USD | 32,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,690.00 USD |
| `7D` | `1.13` | 53,280.00 USD | 53,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,280.00 USD |
| `1D` | `1.13` | 32,810.00 USD | 32,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 473.50 USD |
| `7D` | `1.13` | 63,330.00 USD | 63,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,050.00 USD |
| `1D` | `1.13` | 33,500.00 USD | 33,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 691.45 USD |
| `7D` | `1.13` | 64,970.00 USD | 64,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,640.00 USD |
| `7D` | `1.14` | 66,270.00 USD | 66,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD |
| `7D` | `1.14` | 68,410.00 USD | 68,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,130.00 USD |
| `1D` | `1.14` | 35,060.00 USD | 35,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,560.00 USD |
| `7D` | `1.14` | 73,570.00 USD | 73,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,170.00 USD |
| `1D` | `1.14` | 39,780.00 USD | 39,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,720.00 USD |
| `7D` | `1.14` | 78,430.00 USD | 78,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,860.00 USD |
| `1D` | `1.14` | 39,840.00 USD | 39,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 57.18 USD |
| `7D` | `1.14` | 81,820.00 USD | 81,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,400.00 USD |
| `1D` | `1.14` | 40,890.00 USD | 40,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,060.00 USD |
| `7D` | `1.14` | 84,280.00 USD | 84,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,450.00 USD |
| `1D` | `1.14` | 46,340.00 USD | 46,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,450.00 USD |
| `7D` | `1.14` | 85,010.00 USD | 85,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 736.67 USD |
| `1D` | `1.14` | 49,900.00 USD | 49,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,560.00 USD |
| `7D` | `1.14` | 96,920.00 USD | 96,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,900.00 USD |
| `1D` | `1.15` | 50,120.00 USD | 50,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 217.52 USD |
| `7D` | `1.15` | 98,760.00 USD | 98,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,840.00 USD |
| `1D` | `1.15` | 50,260.00 USD | 50,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 137.39 USD |
| `7D` | `1.15` | 99,410.00 USD | 99,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 654.82 USD |
| `7D` | `1.16` | 101,930.00 USD | 101,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,520.00 USD |
| `1D` | `1.16` | 51,730.00 USD | 51,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,480.00 USD |
| `7D` | `1.16` | 103,100.00 USD | 103,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,170.00 USD |
| `1D` | `1.16` | 53,420.00 USD | 53,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,690.00 USD |
| `7D` | `1.16` | 106,270.00 USD | 106,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,170.00 USD |
| `1D` | `1.16` | 53,430.00 USD | 53,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7.60 USD |
| `7D` | `1.16` | 108,410.00 USD | 108,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,140.00 USD |
| `1D` | `1.16` | 56,670.00 USD | 56,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,240.00 USD |
| `1D` | `1.17` | 58,340.00 USD | 58,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,670.00 USD |
| `7D` | `1.17` | 112,730.00 USD | 112,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,320.00 USD |
| `1D` | `1.17` | 58,460.00 USD | 58,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 118.37 USD |
| `7D` | `1.17` | 115,240.00 USD | 115,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,510.00 USD |
| `1D` | `1.17` | 58,630.00 USD | 58,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 172.86 USD |
| `7D` | `1.17` | 115,650.00 USD | 115,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 409.49 USD |
| `7D` | `1.17` | 115,980.00 USD | 115,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 327.41 USD |
| `7D` | `1.23` | 116,060.00 USD | 116,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 81.33 USD |
| `1D` | `1.23` | 58,940.00 USD | 58,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 310.42 USD |
| `7D` | `1.23` | 117,000.00 USD | 117,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 941.96 USD |
| `1D` | `1.23` | 59,220.00 USD | 59,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 280.04 USD |
| `7D` | `1.23` | 117,450.00 USD | 117,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 445.22 USD |
| `1D` | `1.23` | 59,890.00 USD | 59,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 670.99 USD |
| `7D` | `1.23` | 118,740.00 USD | 118,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,290.00 USD |
| `1D` | `1.23` | 59,900.00 USD | 59,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.05 USD |
| `7D` | `1.23` | 119,580.00 USD | 119,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 835.18 USD |
| `1D` | `1.23` | 61,190.00 USD | 61,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,300.00 USD |
| `1D` | `1.23` | 61,860.00 USD | 61,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 669.24 USD |
| `7D` | `1.23` | 121,170.00 USD | 121,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,600.00 USD |
| `1D` | `1.23` | 61,910.00 USD | 61,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 45.52 USD |
| `7D` | `1.23` | 122,060.00 USD | 122,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 891.56 USD |
| `1D` | `1.24` | 61,960.00 USD | 61,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 55.79 USD |
| `7D` | `1.24` | 122,310.00 USD | 122,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 240.69 USD |
| `1D` | `1.24` | 61,980.00 USD | 61,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.34 USD |
| `7D` | `1.24` | 122,440.00 USD | 122,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 130.96 USD |

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
  * Current Rate: `436.46` | Last 24h: `95.44` | Last 3d: `198.32` | Last 7d: `265.06`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0544%` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `0.0000%` | **USDT Bitget** | `-0.0629%` |
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
  * `2026-10-30 09:50:40 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:48:40 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:49:40 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.12` (Risk Distance: `0.0034` pts)
  * +2.5R Take Profit: `1.13`
  * Mathematical Lot Sizing: **`0.02 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.12` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.12` (Risk Distance: `0.0034` pts)
  * +2.5R Take Profit: `1.11`
  * Mathematical Lot Sizing: **`0.02 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.13`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
