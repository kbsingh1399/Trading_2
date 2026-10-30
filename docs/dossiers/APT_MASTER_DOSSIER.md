# 🏛️ SOVEREIGN CANDIDATE DOSSIER: APT
**Canonical Key**: `APT` | **Broker Instrument**: `APTUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 16:33:46 IST` (`2026-10-30 11:03:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.6900` | **Live Ask Quote**: `0.6901` | **Mid Price**: `0.6901`
- **Spread Points**: `0.000138` | **Spread BPS**: `2.00 bps` (Charter Threshold: `12.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE_MAKER_LIMIT_ONLY` | **Order Type Allowed**: `LIMIT_ONLY`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `4` | Point: `0.0001`
  * Point Value (1.0 Lot): `0.00 USD` | Point Value (0.01 Lot): `0.0000 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `0.6901` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.6949` | Lower -3.00σ Band: `0.6852`
  * Upper +2.51σ Band: `0.6939` | Lower -2.51σ Band: `0.6863`
  * Upper +2.01σ Band: `0.6930` | Lower -2.01σ Band: `0.6872`
  * Upper +2.00σ Band: `0.6928` | Lower -2.00σ Band: `0.6873`
  * Upper +1.28σ Band: `0.6920` | Lower -1.28σ Band: `0.6881`
  * Upper +1.00σ Band: `0.6914` | Lower -1.00σ Band: `0.6887`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.6901` | EMA-20=`0.6901` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.6901` (Slope: `+0.0000`) | EMA-100=`0.6901`
  * Institutional Anchors: EMA-144=`0.6901` | EMA-200=`0.6901` (Slope: `+0.0000`) | EMA-233=`0.6901`
- **Range Boundaries**: 24H High=`0.6970` | 24H Low=`0.6832` | Weekly High=`0.7039` | Weekly Low=`0.6763`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.6921` (Distance: `+0.00%`)
  * Point of Control (POC) = `0.6901` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `0.6880` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.6928` | POC=`0.6901` | VAL=`0.6873`
  * Prior Day Extremes: PDH=`0.6942` | PDL=`0.6859` | PDC=`0.6901`
  * Monday Range Blueprint: High=`0.6935` | Mid=`0.6901` | Low=`0.6866`
  * Developing Weekly Value Area: Weekly VAH=`0.6956` | Weekly POC=`0.6901` | Weekly VAL=`0.6845`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.6914` | Low=`0.6887`
  * London Session (08:00-16:00 UTC): High=`0.6928` | Low=`0.6873`
  * New York Session (13:00-21:00 UTC): High=`0.6942` | Low=`0.6859`
  * Initial Balance (First Hour): IB High=`0.6921` | IB Low=`0.6880`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.6873` - `0.6928`
  * Optimal Trade Entry (OTE 0.705): `0.6914`
  * Structural Invalidation Anchor (0.786): `0.6956`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.6236` | `0.6244` | `0.6227` | `0.6232` | `208,790` | 130,165.60 USD | -16,081.84 USD | `-12.35%` | -6,091,587.34 USD | `-0.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.6233` | `0.6237` | `0.6216` | `0.6224` | `124,216` | 77,337.22 USD | 10,410.68 USD | `+13.46%` | -6,081,176.66 USD | `+0.22` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.6223` | `0.6243` | `0.6216` | `0.6243` | `61,505` | 38,303.55 USD | -4,218.99 USD | `-11.01%` | -6,085,395.65 USD | `-0.24` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.6204` | `0.6245` | `0.6200` | `0.6232` | `525,431` | 327,504.62 USD | 20,810.58 USD | `+6.35%` | -6,015,775.26 USD | `+0.35` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.6233` | `0.6285` | `0.6216` | `0.6284` | `569,011` | 355,826.67 USD | 31,167.21 USD | `+8.76%` | -5,984,608.05 USD | `+0.57` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.6283` | `0.6300` | `0.6278` | `0.6291` | `137,101` | 86,239.36 USD | 5,998.86 USD | `+6.96%` | -5,978,609.19 USD | `+0.15` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.6155` | `0.6190` | `0.6117` | `0.6185` | `2,386,347` | 1,467,859.74 USD | -116,724.25 USD | `-7.95%` | -6,168,857.74 USD | `+0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.6185` | `0.6285` | `0.6169` | `0.6284` | `2,012,526` | 1,252,009.29 USD | 170,943.48 USD | `+13.65%` | -5,997,914.26 USD | `+0.60` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.6283` | `0.6300` | `0.6278` | `0.6291` | `137,101` | 86,239.36 USD | 5,998.86 USD | `+6.96%` | -5,991,915.40 USD | `+0.39` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.6162` | `0.6185` | `0.5736` | `0.6161` | `24,927,742` | 14,934,999.44 USD | -377,825.53 USD | `-2.53%` | -5,661,106.76 USD | `+0.75` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.6161` | `0.6301` | `0.6117` | `0.6189` | `10,604,379` | 6,589,336.18 USD | -407,329.97 USD | `-6.18%` | -6,068,436.74 USD | `+0.62` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6189` | `0.6245` | `0.6117` | `0.6243` | `5,992,689` | 3,702,276.29 USD | 43,764.89 USD | `+1.18%` | -6,024,671.85 USD | `+0.82` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6721` | `16,607,110` | 11,368,753.45 USD | -1,468,928.13 USD | `-12.92%` | -1,617,014.88 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6721` | `0.6728` | `0.6003` | `0.6161` | `56,944,695` | 35,933,598.81 USD | -3,666,266.35 USD | `-10.20%` | -5,283,281.24 USD | `-1.31` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6162` | `0.6185` | `0.5736` | `0.6161` | `24,927,742` | 14,934,999.44 USD | -377,825.53 USD | `-2.53%` | -5,661,106.76 USD | `+0.75` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.6161` | `0.6301` | `0.6117` | `0.6189` | `10,604,379` | 6,589,336.18 USD | -407,329.97 USD | `-6.18%` | -6,068,436.74 USD | `+0.62` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6189` | `0.6300` | `0.6117` | `0.6291` | `6,509,612` | 4,026,537.91 USD | 76,521.34 USD | `+1.90%` | -5,991,915.40 USD | `+0.83` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.6901`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:32:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.6489` | 471.08 USD | `-` | `NEWS_INTEL` | `-` | #APT Liquidated Short: 0.47K USD at 0.6489 USD [API] | `2026-10-29 07:17:37` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.7060` (Vol: 90,823.17 USD, Dist: `+2.43%`) | Long MP=`0.6718` (Vol: 39,956.88 USD, Dist: `--2.53%`)
  * 48H Horizon: Short MP=`0.7055` (Vol: 81,903.46 USD, Dist: `+2.36%`) | Long MP=`0.6702` (Vol: 45,046.52 USD, Dist: `--2.77%`)
  * 3D Horizon: Short MP=`0.7210` (Vol: 125,191.03 USD, Dist: `+4.60%`) | Long MP=`0.6703` (Vol: 75,398.81 USD, Dist: `--2.76%`)
  * 7D Horizon: Short MP=`0.8539` (Vol: 187,280.71 USD, Dist: `+24.46%`) | Long MP=`0.6700` (Vol: 92,436.78 USD, Dist: `--2.35%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.1415` | 283.00 USD | 259,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 21,740.00 USD | 258,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 269.27 USD | 237,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1915` | 851.15 USD | 236,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2215` | 229.94 USD | 235,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 238.99 USD | 235,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2415` | 2,730.00 USD | 235,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 1,460.00 USD | 232,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3175` | 1,590.00 USD | 231,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3245` | 105.37 USD | 229,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3305` | 543.58 USD | 229,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3315` | 9,430.00 USD | 229,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3545` | 177.25 USD | 219,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3615` | 362.58 USD | 219,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3675` | 189.99 USD | 219,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3745` | 561.75 USD | 218,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3935` | 312.98 USD | 218,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3955` | 2,640.00 USD | 217,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3995` | 271.06 USD | 215,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4055` | 410.54 USD | 215,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4105` | 5,100.00 USD | 214,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4115` | 288.05 USD | 209,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4125` | 1,070.00 USD | 209,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4135` | 1,600.00 USD | 208,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 630.86 USD | 206,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4255` | 224.96 USD | 205,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4375` | 31,060.00 USD | 205,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4465` | 840.03 USD | 174,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 226.63 USD | 173,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4525` | 27,150.00 USD | 173,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 5,530.00 USD | 146,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4605` | 125.38 USD | 140,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4615` | 901.90 USD | 140,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4625` | 1,100.00 USD | 139,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4645` | 5,170.00 USD | 138,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4685` | 468.50 USD | 133,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4715` | 188.60 USD | 133,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 135.33 USD | 132,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4855` | 181.88 USD | 132,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 3,170.00 USD | 132,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4925` | 10,520.00 USD | 129,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4935` | 1,580.00 USD | 118,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 3,180.00 USD | 117,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4965` | 143.19 USD | 114,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4975` | 836.14 USD | 114,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 429.90 USD | 113,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5075` | 6,970.00 USD | 112,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 102.82 USD | 105,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 248.05 USD | 105,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5135` | 298.60 USD | 105,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 9,440.00 USD | 105,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5185` | 281.56 USD | 95,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5295` | 1,840.00 USD | 95,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5315` | 11,510.00 USD | 93,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5320` | 1,740,000.00 USD | 1,740,000.00 USD | 8,680.00 USD | 0.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5325` | 2,260.00 USD | 82,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5330` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5335` | 163.22 USD | 79,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5350` | 1,720,000.00 USD | 1,720,000.00 USD | 2,440.00 USD | 3,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5370` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 1,550.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5400` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 2,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5410` | 1,710,000.00 USD | 1,710,000.00 USD | 8,600.00 USD | 0.00 USD | 13.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5420` | 1,700,000.00 USD | 1,700,000.00 USD | 7,660.00 USD | 1,290.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5430` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 627.61 USD | 4,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5440` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 523.59 USD | 8,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5445` | 855.28 USD | 79,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5450` | 1,670,000.00 USD | 1,670,000.00 USD | 2,250.00 USD | 0.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5455` | 191.60 USD | 78,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5460` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 3,030.00 USD | 3,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5470` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 795.70 USD | 29.80 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,630.00 USD | 78,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5480` | 1,660,000.00 USD | 1,660,000.00 USD | 2,000.00 USD | 0.00 USD | 4,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5490` | 1,650,000.00 USD | 1,650,000.00 USD | 2,100.00 USD | 474.54 USD | 2,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5500` | 1,600,000.00 USD | 1,600,000.00 USD | 1,410.00 USD | 0.00 USD | 6,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5500` | 1,650,000.00 USD | 1,650,000.00 USD | 3,890.00 USD | 967.07 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5510` | 1,590,000.00 USD | 1,590,000.00 USD | 1,340.00 USD | 0.00 USD | 1,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5510` | 1,640,000.00 USD | 1,640,000.00 USD | 1,730.00 USD | 1,920.00 USD | 1,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5520` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 1,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5520` | 1,630,000.00 USD | 1,630,000.00 USD | 2,380.00 USD | 0.00 USD | 20.49 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5530` | 1,590,000.00 USD | 1,590,000.00 USD | 2,560.00 USD | 1,410.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5530` | 1,630,000.00 USD | 1,630,000.00 USD | 1,650.00 USD | 1,150.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5540` | 1,580,000.00 USD | 1,580,000.00 USD | 5,390.00 USD | 8,430.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5540` | 1,610,000.00 USD | 1,610,000.00 USD | 11,190.00 USD | 8,450.00 USD | 9,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5545` | 47,450.00 USD | 77,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5550` | 1,560,000.00 USD | 1,560,000.00 USD | 2,940.00 USD | 0.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5550` | 1,580,000.00 USD | 1,580,000.00 USD | 7,070.00 USD | 1,920.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5560` | 1,550,000.00 USD | 1,550,000.00 USD | 4,540.00 USD | 686.25 USD | 2,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5560` | 1,570,000.00 USD | 1,570,000.00 USD | 12,540.00 USD | 1,150.00 USD | 7,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5570` | 1,550,000.00 USD | 1,550,000.00 USD | 5,500.00 USD | 2,460.00 USD | 9,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5570` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 812.74 USD | 3,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5580` | 1,530,000.00 USD | 1,530,000.00 USD | 1,750.00 USD | 3,180.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5580` | 1,540,000.00 USD | 1,540,000.00 USD | 6,000.00 USD | 6,010.00 USD | 15,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5585` | 10,520.00 USD | 29,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5590` | 1,520,000.00 USD | 1,520,000.00 USD | 2,530.00 USD | 2,150.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5590` | 1,520,000.00 USD | 1,520,000.00 USD | 2,660.00 USD | 7,220.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5600` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 1,910.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5600` | 1,500,000.00 USD | 1,500,000.00 USD | 1,410.00 USD | 938.63 USD | 104.99 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5610` | 1,510,000.00 USD | 1,510,000.00 USD | 4,180.00 USD | 1,380.00 USD | 4,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5610` | 1,500,000.00 USD | 1,500,000.00 USD | 13,590.00 USD | 4,110.00 USD | 15,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5615` | 258.48 USD | 19,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5620` | 1,500,000.00 USD | 1,500,000.00 USD | 2,630.00 USD | 1,660.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5620` | 1,460,000.00 USD | 1,460,000.00 USD | 12,860.00 USD | 5,460.00 USD | 3,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5630` | 1,490,000.00 USD | 1,490,000.00 USD | 7,800.00 USD | 1,780.00 USD | 8,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5630` | 1,440,000.00 USD | 1,440,000.00 USD | 14,240.00 USD | 2,380.00 USD | 3,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5635` | 244.90 USD | 18,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5640` | 1,470,000.00 USD | 1,470,000.00 USD | 4,020.00 USD | 3,380.00 USD | 10,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5640` | 1,420,000.00 USD | 1,420,000.00 USD | 3,540.00 USD | 0.00 USD | 25.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5650` | 1,450,000.00 USD | 1,450,000.00 USD | 2,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5650` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 1,210.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5655` | 1,920.00 USD | 18,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5660` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 3,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5660` | 1,420,000.00 USD | 1,420,000.00 USD | 11,490.00 USD | 1,780.00 USD | 2,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5665` | 441.75 USD | 16,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5670` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 2,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5675` | 1,450.00 USD | 16,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5680` | 1,400,000.00 USD | 1,400,000.00 USD | 5,100.00 USD | 0.00 USD | 41.99 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5690` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 5,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5690` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 6.78 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5700` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5700` | 1,390,000.00 USD | 1,390,000.00 USD | 1,030.00 USD | 452.37 USD | 1,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5710` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 2,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5710` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 2,850.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5715` | 289.08 USD | 14,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5720` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 832.92 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5720` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 1,520.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5730` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5730` | 1,370,000.00 USD | 1,370,000.00 USD | 2,690.00 USD | 528.82 USD | 5.20 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5740` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 839.21 USD | 3,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5740` | 1,370,000.00 USD | 1,370,000.00 USD | 18,940.00 USD | 574.82 USD | 1,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5745` | 218.30 USD | 14,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5750` | 1,420,000.00 USD | 1,420,000.00 USD | 4,330.00 USD | 840.09 USD | 20,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5750` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 187.30 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5760` | 1,390,000.00 USD | 1,390,000.00 USD | 15,020.00 USD | 2,220.00 USD | 2,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5760` | 1,350,000.00 USD | 1,350,000.00 USD | 2,150.00 USD | 7,300.00 USD | 19.23 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5770` | 1,370,000.00 USD | 1,370,000.00 USD | 16,730.00 USD | 3,970.00 USD | 279.20 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5770` | 1,340,000.00 USD | 1,340,000.00 USD | 21,510.00 USD | 0.00 USD | 222.98 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5780` | 1,350,000.00 USD | 1,350,000.00 USD | 3,070.00 USD | 1,330.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5780` | 1,320,000.00 USD | 1,320,000.00 USD | 19,410.00 USD | 0.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5790` | 1,340,000.00 USD | 1,340,000.00 USD | 11,420.00 USD | 2,690.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5790` | 1,300,000.00 USD | 1,300,000.00 USD | 1,610.00 USD | 0.00 USD | 11,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5800` | 1,310,000.00 USD | 1,310,000.00 USD | 3,310.00 USD | 2,750.00 USD | 1,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5800` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 3,900.00 USD | 16,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5810` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 3,190.00 USD | 16,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5810` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5820` | 1,290,000.00 USD | 1,290,000.00 USD | 2,580.00 USD | 4,510.00 USD | 4,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5820` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5830` | 1,280,000.00 USD | 1,280,000.00 USD | 4,910.00 USD | 819.33 USD | 41.65 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5830` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 108.28 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5840` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 2,190.00 USD | 4,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5840` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5850` | 1,260,000.00 USD | 1,260,000.00 USD | 2,950.00 USD | 0.00 USD | 30,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5850` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 396.16 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5860` | 1,230,000.00 USD | 1,230,000.00 USD | 2,810.00 USD | 2,450.00 USD | 7,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5870` | 1,220,000.00 USD | 1,220,000.00 USD | 12,190.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5870` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 1,400.00 USD | 65.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5880` | 1,200,000.00 USD | 1,200,000.00 USD | 34,650.00 USD | 8,680.00 USD | 7,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5880` | 1,230,000.00 USD | 1,230,000.00 USD | 3,110.00 USD | 14,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5885` | 8,900.00 USD | 14,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5890` | 1,150,000.00 USD | 1,150,000.00 USD | 39,360.00 USD | 11,450.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5890` | 1,210,000.00 USD | 1,210,000.00 USD | 43,020.00 USD | 0.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5900` | 1,090,000.00 USD | 1,090,000.00 USD | 24,340.00 USD | 14,260.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5900` | 1,160,000.00 USD | 1,160,000.00 USD | 61,220.00 USD | 1,560.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5910` | 1,040,000.00 USD | 1,040,000.00 USD | 31,110.00 USD | 17,770.00 USD | 19,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5910` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 15,190.00 USD | 16,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5915` | 5,310.00 USD | 5,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5920` | 967,700.00 USD | 967,700.00 USD | 26,620.00 USD | 6,570.00 USD | 10,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5920` | 1,060,000.00 USD | 1,060,000.00 USD | 11,690.00 USD | 10,620.00 USD | 58,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5930` | 924,470.00 USD | 924,470.00 USD | 12,580.00 USD | 6,710.00 USD | 22,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5930` | 978,040.00 USD | 978,040.00 USD | 25,390.00 USD | 2,880.00 USD | 14,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5940` | 882,800.00 USD | 882,800.00 USD | 25,790.00 USD | 2,040.00 USD | 21,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5940` | 935,650.00 USD | 935,650.00 USD | 5,780.00 USD | 0.00 USD | 144.44 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5950` | 833,910.00 USD | 833,910.00 USD | 37,990.00 USD | 5,270.00 USD | 1,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5950` | 929,730.00 USD | 929,730.00 USD | 13,060.00 USD | 0.00 USD | 301.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5960` | 789,020.00 USD | 789,020.00 USD | 14,970.00 USD | 2,560.00 USD | 12,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5960` | 916,370.00 USD | 916,370.00 USD | 5,120.00 USD | 18,410.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5970` | 759,070.00 USD | 759,070.00 USD | 14,120.00 USD | 811.64 USD | 5,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5970` | 883,130.00 USD | 883,130.00 USD | 5,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5980` | 738,960.00 USD | 738,960.00 USD | 19,780.00 USD | 6,850.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5980` | 877,580.00 USD | 877,580.00 USD | 37,820.00 USD | 5,380.00 USD | 17,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5990` | 703,440.00 USD | 703,440.00 USD | 8,950.00 USD | 3,370.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5990` | 816,560.00 USD | 816,560.00 USD | 3,320.00 USD | 0.00 USD | 52.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6000` | 687,230.00 USD | 687,230.00 USD | 22,910.00 USD | 3,360.00 USD | 10,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6000` | 813,180.00 USD | 813,180.00 USD | 16,110.00 USD | 0.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6010` | 650,090.00 USD | 650,090.00 USD | 6,720.00 USD | 6,370.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6010` | 785,130.00 USD | 785,130.00 USD | 12,110.00 USD | 4,090.00 USD | 50.15 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6020` | 631,970.00 USD | 631,970.00 USD | 11,780.00 USD | 8,040.00 USD | 15,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6020` | 768,880.00 USD | 768,880.00 USD | 8,860.00 USD | 7,150.00 USD | 17,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6030` | 596,840.00 USD | 596,840.00 USD | 40,580.00 USD | 17,840.00 USD | 20,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6030` | 735,450.00 USD | 735,450.00 USD | 38,530.00 USD | 0.00 USD | 18,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6040` | 518,320.00 USD | 518,320.00 USD | 16,550.00 USD | 20,270.00 USD | 7,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6040` | 678,660.00 USD | 678,660.00 USD | 0.00 USD | 30,380.00 USD | 89.59 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6050` | 473,930.00 USD | 473,930.00 USD | 23,200.00 USD | 2,140.00 USD | 13,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6050` | 648,190.00 USD | 648,190.00 USD | 0.00 USD | 0.00 USD | 20,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6060` | 434,890.00 USD | 434,890.00 USD | 25,160.00 USD | 656.96 USD | 18,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6060` | 627,380.00 USD | 627,380.00 USD | 30,590.00 USD | 5,760.00 USD | 28,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6070` | 390,200.00 USD | 390,200.00 USD | 31,540.00 USD | 4,080.00 USD | 25,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6070` | 562,790.00 USD | 562,790.00 USD | 11,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6080` | 329,350.00 USD | 329,350.00 USD | 26,190.00 USD | 7,250.00 USD | 3,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6080` | 551,230.00 USD | 551,230.00 USD | 2,860.00 USD | 0.00 USD | 30,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6090` | 292,840.00 USD | 292,840.00 USD | 18,460.00 USD | 3,030.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6090` | 518,000.00 USD | 518,000.00 USD | 13,920.00 USD | 44,860.00 USD | 44,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6100` | 263,660.00 USD | 263,660.00 USD | 5,960.00 USD | 1,620.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6100` | 415,180.00 USD | 415,180.00 USD | 18,600.00 USD | 2,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6110` | 214,530.00 USD | 214,530.00 USD | 36,980.00 USD | 12,300.00 USD | 17,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6110` | 394,010.00 USD | 394,010.00 USD | 34,870.00 USD | 12,980.00 USD | 48,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6120` | 147,590.00 USD | 147,590.00 USD | 47,950.00 USD | 6,740.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6120` | 297,680.00 USD | 297,680.00 USD | 35,760.00 USD | 16,650.00 USD | 4,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6130` | 85,130.00 USD | 85,130.00 USD | 2,480.00 USD | 6,720.00 USD | 40,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6130` | 241,130.00 USD | 241,130.00 USD | 105,970.00 USD | 9,220.00 USD | 18,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6140` | 35,810.00 USD | 35,810.00 USD | 0.00 USD | 9,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6140` | 107,410.00 USD | 107,410.00 USD | 17,720.00 USD | 6,170.00 USD | 159.06 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6180` | 26,280.00 USD | 26,280.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6180` | 83,360.00 USD | 83,360.00 USD | 0.00 USD | 0.00 USD | 173.29 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6190` | 83,190.00 USD | 83,190.00 USD | 0.00 USD | 0.00 USD | 182.11 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6200` | 24,530.00 USD | 24,530.00 USD | 0.00 USD | 0.00 USD | 50.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6200` | 83,000.00 USD | 83,000.00 USD | 13,870.00 USD | 0.00 USD | 29,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6210` | 40,070.00 USD | 40,070.00 USD | 0.00 USD | 22,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6250` | 24,480.00 USD | 24,480.00 USD | 2,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6260` | 21,950.00 USD | 21,950.00 USD | 0.00 USD | 8,370.00 USD | 13,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6260` | 17,420.00 USD | 17,420.00 USD | 0.00 USD | 0.00 USD | 17,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6270` | 20,260.00 USD | 20,260.00 USD | 0.00 USD | 3,780.00 USD | 16,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6270` | 40,520.00 USD | 40,520.00 USD | 0.00 USD | 3,780.00 USD | 16,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6270` | 26,520.00 USD | 26,520.00 USD | 0.00 USD | 0.00 USD | 26,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6270` | 53,040.00 USD | 53,040.00 USD | 0.00 USD | 0.00 USD | 26,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6280` | 102,730.00 USD | 102,730.00 USD | 10,020.00 USD | 26,790.00 USD | 25,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6280` | 103,970.00 USD | 103,970.00 USD | 0.00 USD | 34,280.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6290` | 153,450.00 USD | 153,450.00 USD | 23,200.00 USD | 7,350.00 USD | 20,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6290` | 152,780.00 USD | 152,780.00 USD | 0.00 USD | 0.00 USD | 48,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6300` | 213,350.00 USD | 213,350.00 USD | 27,730.00 USD | 4,090.00 USD | 28,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6300` | 217,370.00 USD | 217,370.00 USD | 30,590.00 USD | 5,760.00 USD | 28,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6310` | 312,110.00 USD | 312,110.00 USD | 42,960.00 USD | 8,860.00 USD | 46,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6310` | 229,030.00 USD | 229,030.00 USD | 11,560.00 USD | 0.00 USD | 103.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6320` | 387,900.00 USD | 387,900.00 USD | 51,560.00 USD | 10,170.00 USD | 14,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6320` | 229,290.00 USD | 229,290.00 USD | 0.00 USD | 0.00 USD | 265.37 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6330` | 444,550.00 USD | 444,550.00 USD | 21,410.00 USD | 12,370.00 USD | 22,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6330` | 306,410.00 USD | 306,410.00 USD | 57,940.00 USD | 0.00 USD | 19,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6340` | 521,530.00 USD | 521,530.00 USD | 31,400.00 USD | 4,810.00 USD | 40,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6340` | 328,370.00 USD | 328,370.00 USD | 21,840.00 USD | 0.00 USD | 121.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6350` | 617,690.00 USD | 617,690.00 USD | 64,020.00 USD | 10,620.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6350` | 444,340.00 USD | 444,340.00 USD | 69,190.00 USD | 10,770.00 USD | 36,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6360` | 722,090.00 USD | 722,090.00 USD | 53,920.00 USD | 9,200.00 USD | 41,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6360` | 500,940.00 USD | 500,940.00 USD | 0.00 USD | 0.00 USD | 56,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6370` | 731,350.00 USD | 731,350.00 USD | 0.00 USD | 1,730.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6370` | 510,120.00 USD | 510,120.00 USD | 0.00 USD | 0.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6380` | 814,060.00 USD | 814,060.00 USD | 47,080.00 USD | 22,800.00 USD | 12,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6380` | 586,950.00 USD | 586,950.00 USD | 32,220.00 USD | 0.00 USD | 44,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6390` | 887,840.00 USD | 887,840.00 USD | 14,290.00 USD | 6,680.00 USD | 52,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6390` | 648,630.00 USD | 648,630.00 USD | 24,230.00 USD | 15,680.00 USD | 21,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6400` | 1,010,000.00 USD | 1,010,000.00 USD | 65,540.00 USD | 38,500.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6400` | 694,750.00 USD | 694,750.00 USD | 36,980.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6410` | 1,080,000.00 USD | 1,080,000.00 USD | 34,570.00 USD | 19,840.00 USD | 15,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6410` | 725,120.00 USD | 725,120.00 USD | 0.00 USD | 24,060.00 USD | 6,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6420` | 1,160,000.00 USD | 1,160,000.00 USD | 55,390.00 USD | 9,980.00 USD | 15,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6420` | 836,730.00 USD | 836,730.00 USD | 55,350.00 USD | 26,560.00 USD | 29,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6430` | 1,230,000.00 USD | 1,230,000.00 USD | 25,440.00 USD | 11,080.00 USD | 30,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6430` | 895,550.00 USD | 895,550.00 USD | 31,500.00 USD | 10,020.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6435` | 484.24 USD | 484.24 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6440` | 1,340,000.00 USD | 1,340,000.00 USD | 36,680.00 USD | 14,890.00 USD | 61,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6440` | 962,190.00 USD | 962,190.00 USD | 34,270.00 USD | 17,680.00 USD | 14,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6450` | 1,430,000.00 USD | 1,430,000.00 USD | 62,440.00 USD | 14,740.00 USD | 15,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6450` | 1,090,000.00 USD | 1,090,000.00 USD | 81,220.00 USD | 15,560.00 USD | 35,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6460` | 1,490,000.00 USD | 1,490,000.00 USD | 29,100.00 USD | 12,810.00 USD | 13,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6460` | 1,330,000.00 USD | 1,330,000.00 USD | 91,390.00 USD | 31,070.00 USD | 112,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6470` | 1,570,000.00 USD | 1,570,000.00 USD | 54,020.00 USD | 18,030.00 USD | 11,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6470` | 1,380,000.00 USD | 1,380,000.00 USD | 15,220.00 USD | 26,520.00 USD | 9,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6475` | 209.47 USD | 693.71 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6480` | 1,680,000.00 USD | 1,680,000.00 USD | 83,050.00 USD | 12,090.00 USD | 9,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6480` | 1,520,000.00 USD | 1,520,000.00 USD | 94,210.00 USD | 5,380.00 USD | 41,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6490` | 1,750,000.00 USD | 1,750,000.00 USD | 48,180.00 USD | 4,600.00 USD | 15,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6490` | 1,580,000.00 USD | 1,580,000.00 USD | 36,340.00 USD | 0.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6500` | 1,810,000.00 USD | 1,810,000.00 USD | 49,890.00 USD | 9,280.00 USD | 5,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6500` | 1,750,000.00 USD | 1,750,000.00 USD | 53,330.00 USD | 0.00 USD | 122,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6510` | 1,880,000.00 USD | 1,880,000.00 USD | 52,270.00 USD | 0.00 USD | 14,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6510` | 2,020,000.00 USD | 2,020,000.00 USD | 244,480.00 USD | 8,270.00 USD | 18,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6520` | 1,960,000.00 USD | 1,960,000.00 USD | 65,860.00 USD | 13,800.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6520` | 2,190,000.00 USD | 2,190,000.00 USD | 74,540.00 USD | 6,720.00 USD | 86,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6530` | 1,980,000.00 USD | 1,980,000.00 USD | 16,100.00 USD | 3,910.00 USD | 11.74 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6530` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 4,440.00 USD | 47,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6540` | 2,010,000.00 USD | 2,010,000.00 USD | 22,250.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6540` | 2,270,000.00 USD | 2,270,000.00 USD | 15,730.00 USD | 0.00 USD | 14,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6550` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 6,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6550` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 414.15 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6560` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 8,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6560` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 5,380.00 USD | 651.75 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6570` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 4,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6570` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 6,350.00 USD | 447.57 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6580` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 3,310.00 USD | 48.99 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6580` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 21,920.00 USD | 9,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6590` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 5,890.00 USD | 164.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6590` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 11,320.00 USD | 331.05 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6600` | 2,050,000.00 USD | 2,050,000.00 USD | 6,010.00 USD | 9,280.00 USD | 59.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6600` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 7,100.00 USD | 249.08 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6610` | 2,060,000.00 USD | 2,060,000.00 USD | 6,690.00 USD | 835.70 USD | 142.10 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6610` | 2,340,000.00 USD | 2,340,000.00 USD | 8,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6620` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 530.84 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6620` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 128.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6630` | 2,070,000.00 USD | 2,070,000.00 USD | 2,590.00 USD | 0.00 USD | 2,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6630` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 254.70 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6640` | 2,090,000.00 USD | 2,090,000.00 USD | 11,190.00 USD | 837.01 USD | 135.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6640` | 2,390,000.00 USD | 2,390,000.00 USD | 33,660.00 USD | 0.00 USD | 7,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6650` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 3,160.00 USD | 17,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6650` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 6,770.00 USD | 405.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6660` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 839.67 USD | 7,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6660` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 148.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6670` | 2,140,000.00 USD | 2,140,000.00 USD | 18,850.00 USD | 0.00 USD | 66.01 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6670` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 416.46 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6680` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 158.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6680` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 224.19 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6690` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 3,550.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6690` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 448.05 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6695` | 69,660.00 USD | 70,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6700` | 2,180,000.00 USD | 2,180,000.00 USD | 8,830.00 USD | 1,920.00 USD | 24,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6700` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 546.45 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6710` | 2,230,000.00 USD | 2,230,000.00 USD | 41,970.00 USD | 0.00 USD | 5,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6710` | 2,480,000.00 USD | 2,480,000.00 USD | 58,470.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6720` | 2,230,000.00 USD | 2,230,000.00 USD | 1,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6730` | 2,260,000.00 USD | 2,260,000.00 USD | 25,660.00 USD | 3,670.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6730` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 99.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6740` | 2,350,000.00 USD | 2,350,000.00 USD | 64,370.00 USD | 8,170.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6740` | 2,520,000.00 USD | 2,520,000.00 USD | 39,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6750` | 2,390,000.00 USD | 2,390,000.00 USD | 30,000.00 USD | 1,410.00 USD | 14,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6750` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 75,730.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6760` | 2,410,000.00 USD | 2,410,000.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6760` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 2,240.00 USD | 33,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6770` | 2,460,000.00 USD | 2,460,000.00 USD | 19,930.00 USD | 9,080.00 USD | 17,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6770` | 2,730,000.00 USD | 2,730,000.00 USD | 63,600.00 USD | 4,190.00 USD | 21,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6780` | 2,510,000.00 USD | 2,510,000.00 USD | 33,610.00 USD | 8,030.00 USD | 12,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6780` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 14,960.00 USD | 124.93 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6790` | 2,550,000.00 USD | 2,550,000.00 USD | 2,940.00 USD | 18,610.00 USD | 13,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6790` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 16,590.00 USD | 4,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6800` | 2,560,000.00 USD | 2,560,000.00 USD | 4,540.00 USD | 686.25 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6800` | 2,770,000.00 USD | 2,770,000.00 USD | 6,120.00 USD | 1,150.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6810` | 2,580,000.00 USD | 2,580,000.00 USD | 5,500.00 USD | 2,460.00 USD | 17,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6810` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 15,720.00 USD | 145.79 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6820` | 2,630,000.00 USD | 2,630,000.00 USD | 24,350.00 USD | 16,950.00 USD | 9,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6820` | 2,860,000.00 USD | 2,860,000.00 USD | 32,570.00 USD | 37,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6830` | 2,710,000.00 USD | 2,710,000.00 USD | 27,110.00 USD | 15,380.00 USD | 32,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6830` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 17,730.00 USD | 52,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6840` | 2,780,000.00 USD | 2,780,000.00 USD | 45,780.00 USD | 12,210.00 USD | 15,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6840` | 3,080,000.00 USD | 3,080,000.00 USD | 57,890.00 USD | 36,580.00 USD | 54,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6850` | 2,850,000.00 USD | 2,850,000.00 USD | 31,830.00 USD | 7,150.00 USD | 27,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6850` | 3,130,000.00 USD | 3,130,000.00 USD | 24,240.00 USD | 6,860.00 USD | 17,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6860` | 2,910,000.00 USD | 2,910,000.00 USD | 42,880.00 USD | 5,260.00 USD | 15,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6860` | 3,170,000.00 USD | 3,170,000.00 USD | 32,660.00 USD | 9,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6870` | 2,980,000.00 USD | 2,980,000.00 USD | 63,220.00 USD | 1,160.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6870` | 3,190,000.00 USD | 3,190,000.00 USD | 19,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6880` | 3,020,000.00 USD | 3,020,000.00 USD | 20,970.00 USD | 11,390.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6880` | 3,230,000.00 USD | 3,230,000.00 USD | 24,610.00 USD | 17,300.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6890` | 3,030,000.00 USD | 3,030,000.00 USD | 1,180.00 USD | 0.00 USD | 8,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6890` | 3,250,000.00 USD | 3,250,000.00 USD | 4,850.00 USD | 12,670.00 USD | 77.75 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6900` | 3,080,000.00 USD | 3,080,000.00 USD | 18,600.00 USD | 4,990.00 USD | 21,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6900` | 3,280,000.00 USD | 3,280,000.00 USD | 3,540.00 USD | 4,480.00 USD | 16,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6910` | 3,110,000.00 USD | 3,110,000.00 USD | 31,460.00 USD | 1,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6910` | 3,380,000.00 USD | 3,380,000.00 USD | 69,620.00 USD | 2,090.00 USD | 37,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6920` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 24,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6930` | 3,470,000.00 USD | 3,470,000.00 USD | 14,220.00 USD | 0.00 USD | 42,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6950` | 3,510,000.00 USD | 3,510,000.00 USD | 31,450.00 USD | 0.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6960` | 3,540,000.00 USD | 3,540,000.00 USD | 28,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6970` | 3,570,000.00 USD | 3,570,000.00 USD | 21,650.00 USD | 6,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7245` | 364.39 USD | 70,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.7725` | 165.62 USD | 70,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.7945` | 365.88 USD | 71,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8005` | 19,120.00 USD | 90,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8665` | 378.95 USD | 90,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9085` | 21,960.00 USD | 112,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9575` | 16,900.00 USD | 129,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9935` | 166.01 USD | 129,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.02` | 25,970.00 USD | 155,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.04` | 5,200.00 USD | 160,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 82,820.00 USD | 243,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 479.74 USD | 244,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.12` | 2,800.00 USD | 247,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.15` | 650.29 USD | 247,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.17` | 501.44 USD | 248,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 227.46 USD | 248,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 199.98 USD | 248,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 796.83 USD | 249,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1415` | 247,410.00 USD | 0.00 USD | 283.00 USD | `-77.48%` | `2,000.00` |
| `Live` | `Long` | `0.1805` | 247,130.00 USD | 0.00 USD | 802.26 USD | `-71.27%` | `4,444.65` |
| `Live` | `Long` | `0.1875` | 246,320.00 USD | 0.00 USD | 269.27 USD | `-70.15%` | `1,436.09` |
| `Live` | `Long` | `0.2195` | 246,050.00 USD | 0.00 USD | 227.87 USD | `-65.06%` | `1,038.12` |
| `Live` | `Long` | `0.2315` | 245,830.00 USD | 0.00 USD | 232.95 USD | `-63.15%` | `1,006.27` |
| `Live` | `Long` | `0.2325` | 245,590.00 USD | 0.00 USD | 2,620.00 USD | `-62.99%` | `11,284.25` |
| `Live` | `Long` | `0.2425` | 242,970.00 USD | 0.00 USD | 1,460.00 USD | `-61.40%` | `6,000.00` |
| `Live` | `Long` | `0.3175` | 241,520.00 USD | 0.00 USD | 1,590.00 USD | `-49.46%` | `5,000.00` |
| `Live` | `Long` | `0.3245` | 239,930.00 USD | 0.00 USD | 105.37 USD | `-48.34%` | `324.72` |
| `Live` | `Long` | `0.3295` | 239,820.00 USD | 0.00 USD | 9,370.00 USD | `-47.55%` | `28,446.85` |
| `Live` | `Long` | `0.3305` | 230,450.00 USD | 0.00 USD | 1,010.00 USD | `-47.39%` | `3,064.09` |
| `Live` | `Long` | `0.3505` | 229,440.00 USD | 0.00 USD | 278.78 USD | `-44.21%` | `795.38` |
| `Live` | `Long` | `0.3545` | 229,160.00 USD | 0.00 USD | 177.25 USD | `-43.57%` | `500.00` |
| `Live` | `Long` | `0.3555` | 228,980.00 USD | 0.00 USD | 533.25 USD | `-43.41%` | `1,500.00` |
| `Live` | `Long` | `0.3615` | 228,450.00 USD | 0.00 USD | 362.58 USD | `-42.45%` | `1,002.99` |
| `Live` | `Long` | `0.3675` | 228,080.00 USD | 0.00 USD | 189.99 USD | `-41.50%` | `516.98` |
| `Live` | `Long` | `0.3955` | 227,890.00 USD | 0.00 USD | 3,040.00 USD | `-37.04%` | `7,698.71` |
| `Live` | `Long` | `0.3995` | 224,850.00 USD | 0.00 USD | 5,240.00 USD | `-36.41%` | `13,104.64` |
| `Live` | `Long` | `0.4065` | 219,610.00 USD | 0.00 USD | 284.55 USD | `-35.29%` | `700.00` |
| `Live` | `Long` | `0.4125` | 219,330.00 USD | 0.00 USD | 1,070.00 USD | `-34.34%` | `2,600.00` |
| `Live` | `Long` | `0.4135` | 218,260.00 USD | 0.00 USD | 1,600.00 USD | `-34.18%` | `3,868.97` |
| `Live` | `Long` | `0.4185` | 216,660.00 USD | 0.00 USD | 630.86 USD | `-33.38%` | `1,507.44` |
| `Live` | `Long` | `0.4225` | 216,030.00 USD | 0.00 USD | 794.87 USD | `-32.74%` | `1,881.36` |
| `Live` | `Long` | `0.4255` | 215,230.00 USD | 0.00 USD | 224.96 USD | `-32.27%` | `528.69` |
| `Live` | `Long` | `0.4375` | 215,010.00 USD | 0.00 USD | 36,400.00 USD | `-30.36%` | `83,196.32` |
| `Live` | `Long` | `0.4465` | 178,610.00 USD | 0.00 USD | 4,130.00 USD | `-28.92%` | `9,243.24` |
| `Live` | `Long` | `0.4475` | 174,480.00 USD | 0.00 USD | 226.63 USD | `-28.76%` | `506.43` |
| `Live` | `Long` | `0.4525` | 174,250.00 USD | 0.00 USD | 27,150.00 USD | `-27.97%` | `60,000.00` |
| `Live` | `Long` | `0.4605` | 147,100.00 USD | 0.00 USD | 125.38 USD | `-26.70%` | `272.27` |
| `Live` | `Long` | `0.4615` | 146,980.00 USD | 0.00 USD | 901.90 USD | `-26.54%` | `1,954.27` |
| `Live` | `Long` | `0.4625` | 146,080.00 USD | 0.00 USD | 170.64 USD | `-26.38%` | `368.95` |
| `Live` | `Long` | `0.4635` | 145,910.00 USD | 0.00 USD | 927.00 USD | `-26.22%` | `2,000.00` |
| `Live` | `Long` | `0.4645` | 144,980.00 USD | 0.00 USD | 876.05 USD | `-26.06%` | `1,886.00` |
| `Live` | `Long` | `0.4685` | 144,100.00 USD | 0.00 USD | 468.50 USD | `-25.42%` | `1,000.00` |
| `Live` | `Long` | `0.4715` | 143,640.00 USD | 0.00 USD | 188.60 USD | `-24.94%` | `400.00` |
| `Live` | `Long` | `0.4835` | 143,450.00 USD | 0.00 USD | 135.33 USD | `-23.03%` | `279.90` |
| `Live` | `Long` | `0.4855` | 143,310.00 USD | 0.00 USD | 181.88 USD | `-22.72%` | `374.62` |
| `Live` | `Long` | `0.4865` | 143,130.00 USD | 0.00 USD | 3,170.00 USD | `-22.56%` | `6,508.47` |
| `Live` | `Long` | `0.4915` | 139,960.00 USD | 0.00 USD | 166.62 USD | `-21.76%` | `339.00` |
| `Live` | `Long` | `0.4925` | 139,800.00 USD | 0.00 USD | 14,160.00 USD | `-21.60%` | `28,749.20` |
| `Live` | `Long` | `0.4935` | 125,640.00 USD | 0.00 USD | 1,580.00 USD | `-21.44%` | `3,199.85` |
| `Live` | `Long` | `0.4955` | 124,060.00 USD | 0.00 USD | 3,180.00 USD | `-21.12%` | `6,422.59` |
| `Live` | `Long` | `0.4965` | 120,880.00 USD | 0.00 USD | 143.19 USD | `-20.96%` | `288.40` |
| `Live` | `Long` | `0.4975` | 120,730.00 USD | 0.00 USD | 667.49 USD | `-20.81%` | `1,341.68` |
| `Live` | `Long` | `0.4985` | 120,070.00 USD | 0.00 USD | 429.90 USD | `-20.65%` | `862.38` |
| `Live` | `Long` | `0.5075` | 119,640.00 USD | 0.00 USD | 303.42 USD | `-19.21%` | `597.87` |
| `Live` | `Long` | `0.5085` | 119,330.00 USD | 0.00 USD | 102.82 USD | `-19.05%` | `202.20` |
| `Live` | `Long` | `0.5125` | 119,230.00 USD | 0.00 USD | 248.05 USD | `-18.42%` | `484.00` |
| `Live` | `Long` | `0.5135` | 118,980.00 USD | 0.00 USD | 298.60 USD | `-18.26%` | `581.49` |
| `Live` | `Long` | `0.5175` | 118,680.00 USD | 0.00 USD | 9,440.00 USD | `-17.62%` | `18,249.92` |
| `Live` | `Long` | `0.5185` | 109,240.00 USD | 0.00 USD | 281.56 USD | `-17.46%` | `543.02` |
| `Live` | `Long` | `0.5215` | 108,960.00 USD | 0.00 USD | 427.43 USD | `-16.99%` | `819.61` |
| `Live` | `Long` | `0.5295` | 108,530.00 USD | 0.00 USD | 1,840.00 USD | `-15.71%` | `3,467.51` |
| `Live` | `Long` | `0.5305` | 106,690.00 USD | 0.00 USD | 13,260.00 USD | `-15.55%` | `25,000.00` |
| `Live` | `Long` | `0.5315` | 93,430.00 USD | 0.00 USD | 11,510.00 USD | `-15.39%` | `21,664.95` |
| `Live` | `Long` | `0.5325` | 81,920.00 USD | 0.00 USD | 2,260.00 USD | `-15.23%` | `4,240.81` |
| `Live` | `Long` | `0.5335` | 79,660.00 USD | 0.00 USD | 163.22 USD | `-15.07%` | `305.95` |
| `Live` | `Long` | `0.5445` | 79,490.00 USD | 0.00 USD | 855.28 USD | `-13.32%` | `1,570.77` |
| `Live` | `Long` | `0.5475` | 78,640.00 USD | 0.00 USD | 1,630.00 USD | `-12.85%` | `2,968.46` |
| `Live` | `Long` | `0.5545` | 77,010.00 USD | 0.00 USD | 47,450.00 USD | `-11.73%` | `85,578.81` |
| `Live` | `Long` | `0.5585` | 29,560.00 USD | 0.00 USD | 10,520.00 USD | `-11.10%` | `18,834.52` |
| `Live` | `Long` | `0.5615` | 19,040.00 USD | 0.00 USD | 258.48 USD | `-10.62%` | `460.33` |
| `Live` | `Long` | `0.5655` | 18,780.00 USD | 0.00 USD | 1,920.00 USD | `-9.98%` | `3,394.98` |
| `Live` | `Long` | `0.5665` | 16,860.00 USD | 0.00 USD | 441.75 USD | `-9.82%` | `779.79` |
| `Live` | `Long` | `0.5675` | 16,420.00 USD | 0.00 USD | 1,450.00 USD | `-9.66%` | `2,557.95` |
| `Live` | `Long` | `0.5715` | 14,970.00 USD | 0.00 USD | 289.08 USD | `-9.03%` | `505.82` |
| `Live` | `Long` | `0.5745` | 14,680.00 USD | 0.00 USD | 218.30 USD | `-8.55%` | `379.98` |
| `Live` | `Long` | `0.5885` | 14,460.00 USD | 0.00 USD | 8,900.00 USD | `-6.32%` | `15,117.28` |
| `Live` | `Long` | `0.5915` | 5,570.00 USD | 0.00 USD | 5,570.00 USD | `-5.84%` | `9,409.67` |
| `Live` | `Short` | `0.6435` | 484.24 USD | 484.24 USD | 0.00 USD | `+2.44%` | `752.51` |
| `Live` | `Short` | `0.6475` | 693.71 USD | 209.47 USD | 0.00 USD | `+3.07%` | `323.51` |
| `Live` | `Short` | `0.6495` | 4,820.00 USD | 4,130.00 USD | 0.00 USD | `+3.39%` | `6,357.42` |
| `Live` | `Short` | `0.6685` | 74,380.00 USD | 69,560.00 USD | 0.00 USD | `+6.42%` | `104,052.51` |
| `Live` | `Short` | `0.7245` | 74,750.00 USD | 364.39 USD | 0.00 USD | `+15.33%` | `502.96` |
| `Live` | `Short` | `0.7725` | 74,910.00 USD | 165.62 USD | 0.00 USD | `+22.97%` | `214.40` |
| `Live` | `Short` | `0.7945` | 75,280.00 USD | 365.88 USD | 0.00 USD | `+26.47%` | `460.51` |
| `Live` | `Short` | `0.8005` | 94,400.00 USD | 19,120.00 USD | 0.00 USD | `+27.43%` | `23,882.80` |
| `Live` | `Short` | `0.8665` | 94,770.00 USD | 378.95 USD | 0.00 USD | `+37.93%` | `437.33` |
| `Live` | `Short` | `0.9185` | 115,660.00 USD | 20,890.00 USD | 0.00 USD | `+46.21%` | `22,738.59` |
| `Live` | `Short` | `0.9485` | 116,200.00 USD | 537.51 USD | 0.00 USD | `+50.99%` | `566.70` |
| `Live` | `Short` | `0.9905` | 133,680.00 USD | 17,480.00 USD | 0.00 USD | `+57.67%` | `17,648.14` |
| `Live` | `Short` | `0.9935` | 133,840.00 USD | 166.01 USD | 0.00 USD | `+58.15%` | `167.10` |
| `Live` | `Short` | `1.02` | 159,810.00 USD | 25,970.00 USD | 0.00 USD | `+62.61%` | `25,423.72` |
| `Live` | `Short` | `1.04` | 165,000.00 USD | 5,180.00 USD | 0.00 USD | `+65.00%` | `5,000.00` |
| `Live` | `Short` | `1.05` | 245,380.00 USD | 80,380.00 USD | 0.00 USD | `+67.70%` | `76,300.00` |
| `Live` | `Short` | `1.09` | 245,860.00 USD | 479.74 USD | 0.00 USD | `+73.75%` | `439.52` |
| `Live` | `Short` | `1.12` | 248,660.00 USD | 2,800.00 USD | 0.00 USD | `+78.21%` | `2,500.00` |
| `Live` | `Short` | `1.17` | 249,160.00 USD | 501.44 USD | 0.00 USD | `+86.80%` | `427.30` |
| `Live` | `Short` | `1.19` | 249,390.00 USD | 227.46 USD | 0.00 USD | `+88.87%` | `191.71` |
| `Live` | `Short` | `1.19` | 249,590.00 USD | 199.98 USD | 0.00 USD | `+89.19%` | `168.26` |
| `Live` | `Short` | `1.22` | 250,380.00 USD | 796.83 USD | 0.00 USD | `+94.44%` | `652.34` |
| `Live` | `Short` | `1.24` | 250,710.00 USD | 328.76 USD | 0.00 USD | `+97.95%` | `264.38` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.3505` | 217,710.00 USD | 0.00 USD | 340.19 USD | `-44.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4635` | 217,370.00 USD | 0.00 USD | 104.57 USD | `-26.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4955` | 217,270.00 USD | 0.00 USD | 111.62 USD | `-21.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4965` | 217,160.00 USD | 0.00 USD | 111.85 USD | `-20.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 217,050.00 USD | 0.00 USD | 67,850.00 USD | `-20.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5015` | 149,200.00 USD | 0.00 USD | 112.97 USD | `-20.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5065` | 149,090.00 USD | 0.00 USD | 225.65 USD | `-19.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5085` | 148,860.00 USD | 0.00 USD | 101.97 USD | `-19.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5115` | 148,760.00 USD | 0.00 USD | 111.69 USD | `-18.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5125` | 148,650.00 USD | 0.00 USD | 5,380.00 USD | `-18.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 143,270.00 USD | 0.00 USD | 115.47 USD | `-17.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5175` | 143,150.00 USD | 0.00 USD | 116.58 USD | `-17.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5185` | 143,030.00 USD | 0.00 USD | 116.96 USD | `-17.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5205` | 142,920.00 USD | 0.00 USD | 539.96 USD | `-17.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5225` | 142,380.00 USD | 0.00 USD | 117.70 USD | `-16.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5235` | 142,260.00 USD | 0.00 USD | 117.93 USD | `-16.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5305` | 142,140.00 USD | 0.00 USD | 770.19 USD | `-15.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5445` | 141,370.00 USD | 0.00 USD | 8,750.00 USD | `-13.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5455` | 132,620.00 USD | 0.00 USD | 8,150.00 USD | `-13.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5485` | 124,470.00 USD | 0.00 USD | 4,500.00 USD | `-12.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5505` | 119,970.00 USD | 0.00 USD | 7,230.00 USD | `-12.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5515` | 112,740.00 USD | 0.00 USD | 126.71 USD | `-12.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5525` | 112,610.00 USD | 0.00 USD | 126.90 USD | `-12.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5555` | 112,490.00 USD | 0.00 USD | 57,800.00 USD | `-11.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5565` | 54,680.00 USD | 0.00 USD | 173.58 USD | `-11.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5595` | 54,510.00 USD | 0.00 USD | 10,540.00 USD | `-10.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 43,970.00 USD | 0.00 USD | 339.84 USD | `-10.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5625` | 43,630.00 USD | 0.00 USD | 930.52 USD | `-10.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5655` | 42,700.00 USD | 0.00 USD | 127.62 USD | `-9.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5695` | 42,570.00 USD | 0.00 USD | 127.30 USD | `-9.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5705` | 42,450.00 USD | 0.00 USD | 9,410.00 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5715` | 33,030.00 USD | 0.00 USD | 127.63 USD | `-9.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5735` | 32,910.00 USD | 0.00 USD | 151.62 USD | `-8.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5755` | 32,750.00 USD | 0.00 USD | 9,290.00 USD | `-8.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5775` | 23,470.00 USD | 0.00 USD | 1,710.00 USD | `-8.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5785` | 21,750.00 USD | 0.00 USD | 127.36 USD | `-7.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5795` | 21,630.00 USD | 0.00 USD | 780.04 USD | `-7.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5815` | 20,850.00 USD | 0.00 USD | 825.36 USD | `-7.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5835` | 20,020.00 USD | 0.00 USD | 999.65 USD | `-7.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5845` | 19,020.00 USD | 0.00 USD | 533.37 USD | `-6.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5905` | 18,490.00 USD | 0.00 USD | 8,930.00 USD | `-6.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5925` | 9,560.00 USD | 0.00 USD | 265.69 USD | `-5.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5975` | 9,300.00 USD | 0.00 USD | 597.80 USD | `-4.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5995` | 8,700.00 USD | 0.00 USD | 509.04 USD | `-4.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 8,190.00 USD | 0.00 USD | 953.02 USD | `-4.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6045` | 7,240.00 USD | 0.00 USD | 999.99 USD | `-3.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6065` | 6,240.00 USD | 0.00 USD | 1,910.00 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6075` | 4,330.00 USD | 0.00 USD | 389.92 USD | `-3.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6085` | 3,940.00 USD | 0.00 USD | 301.32 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6115` | 3,640.00 USD | 0.00 USD | 214.78 USD | `-2.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6135` | 3,420.00 USD | 0.00 USD | 410.30 USD | `-2.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6175` | 3,010.00 USD | 0.00 USD | 588.19 USD | `-1.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 2,420.00 USD | 0.00 USD | 581.40 USD | `-1.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6225` | 1,840.00 USD | 0.00 USD | 1,000.00 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6265` | 840.71 USD | 0.00 USD | 407.61 USD | `-0.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6275` | 433.11 USD | 0.00 USD | 433.11 USD | `-0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6285` | 469.94 USD | 469.94 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 4,900.00 USD | 4,430.00 USD | 0.00 USD | `+0.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 5,170.00 USD | 269.44 USD | 0.00 USD | `+0.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6335` | 13,560.00 USD | 8,390.00 USD | 0.00 USD | `+0.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6345` | 13,850.00 USD | 292.19 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6395` | 15,050.00 USD | 1,200.00 USD | 0.00 USD | `+1.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6405` | 24,730.00 USD | 9,680.00 USD | 0.00 USD | `+1.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6415` | 32,340.00 USD | 7,600.00 USD | 0.00 USD | `+2.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6425` | 38,210.00 USD | 5,880.00 USD | 0.00 USD | `+2.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6445` | 43,510.00 USD | 5,300.00 USD | 0.00 USD | `+2.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6465` | 53,490.00 USD | 9,980.00 USD | 0.00 USD | `+2.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6505` | 54,060.00 USD | 567.58 USD | 0.00 USD | `+3.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6525` | 54,230.00 USD | 172.51 USD | 0.00 USD | `+3.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6555` | 58,310.00 USD | 4,080.00 USD | 0.00 USD | `+4.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6605` | 58,890.00 USD | 580.23 USD | 0.00 USD | `+5.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6635` | 59,180.00 USD | 289.66 USD | 0.00 USD | `+5.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6645` | 59,440.00 USD | 262.60 USD | 0.00 USD | `+5.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6655` | 59,720.00 USD | 283.50 USD | 0.00 USD | `+5.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6705` | 59,890.00 USD | 162.91 USD | 0.00 USD | `+6.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6735` | 70,750.00 USD | 10,870.00 USD | 0.00 USD | `+7.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6745` | 71,350.00 USD | 598.31 USD | 0.00 USD | `+7.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 71,510.00 USD | 154.30 USD | 0.00 USD | `+7.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6805` | 71,720.00 USD | 214.20 USD | 0.00 USD | `+8.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6815` | 82,280.00 USD | 10,560.00 USD | 0.00 USD | `+8.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6845` | 83,410.00 USD | 1,130.00 USD | 0.00 USD | `+8.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6875` | 83,550.00 USD | 140.41 USD | 0.00 USD | `+9.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6885` | 84,070.00 USD | 514.80 USD | 0.00 USD | `+9.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6915` | 84,170.00 USD | 101.96 USD | 0.00 USD | `+10.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6925` | 85,190.00 USD | 1,020.00 USD | 0.00 USD | `+10.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6945` | 85,800.00 USD | 610.10 USD | 0.00 USD | `+10.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6955` | 85,900.00 USD | 101.38 USD | 0.00 USD | `+10.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6965` | 86,690.00 USD | 789.18 USD | 0.00 USD | `+10.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6985` | 86,800.00 USD | 102.99 USD | 0.00 USD | `+11.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7005` | 86,910.00 USD | 111.08 USD | 0.00 USD | `+11.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7015` | 87,600.00 USD | 694.49 USD | 0.00 USD | `+11.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7095` | 87,730.00 USD | 132.99 USD | 0.00 USD | `+12.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7115` | 87,860.00 USD | 122.04 USD | 0.00 USD | `+13.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7165` | 89,690.00 USD | 1,830.00 USD | 0.00 USD | `+14.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7195` | 89,870.00 USD | 183.26 USD | 0.00 USD | `+14.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7205` | 90,020.00 USD | 147.15 USD | 0.00 USD | `+14.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7265` | 96,310.00 USD | 6,290.00 USD | 0.00 USD | `+15.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7275` | 96,620.00 USD | 309.91 USD | 0.00 USD | `+15.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7325` | 96,790.00 USD | 165.17 USD | 0.00 USD | `+16.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7345` | 97,810.00 USD | 1,030.00 USD | 0.00 USD | `+16.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7405` | 107,540.00 USD | 9,730.00 USD | 0.00 USD | `+17.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7445` | 107,730.00 USD | 185.43 USD | 0.00 USD | `+18.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7455` | 109,890.00 USD | 2,170.00 USD | 0.00 USD | `+18.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7475` | 110,210.00 USD | 318.43 USD | 0.00 USD | `+18.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7505` | 110,350.00 USD | 141.39 USD | 0.00 USD | `+19.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7565` | 114,470.00 USD | 4,120.00 USD | 0.00 USD | `+20.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7575` | 114,980.00 USD | 511.82 USD | 0.00 USD | `+20.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7615` | 115,860.00 USD | 875.23 USD | 0.00 USD | `+21.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7635` | 115,960.00 USD | 103.35 USD | 0.00 USD | `+21.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7665` | 116,090.00 USD | 127.48 USD | 0.00 USD | `+22.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7675` | 116,190.00 USD | 101.61 USD | 0.00 USD | `+22.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7695` | 116,380.00 USD | 186.97 USD | 0.00 USD | `+22.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7705` | 116,480.00 USD | 109.43 USD | 0.00 USD | `+22.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7775` | 116,650.00 USD | 166.70 USD | 0.00 USD | `+23.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7815` | 117,790.00 USD | 1,140.00 USD | 0.00 USD | `+24.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7865` | 124,100.00 USD | 6,310.00 USD | 0.00 USD | `+25.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8125` | 136,170.00 USD | 12,070.00 USD | 0.00 USD | `+29.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8265` | 137,830.00 USD | 1,650.00 USD | 0.00 USD | `+31.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8335` | 138,760.00 USD | 929.08 USD | 0.00 USD | `+32.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8475` | 179,350.00 USD | 40,590.00 USD | 0.00 USD | `+34.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8505` | 196,080.00 USD | 16,740.00 USD | 0.00 USD | `+35.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8515` | 208,810.00 USD | 12,720.00 USD | 0.00 USD | `+35.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8525` | 220,590.00 USD | 11,780.00 USD | 0.00 USD | `+35.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8555` | 220,700.00 USD | 108.85 USD | 0.00 USD | `+36.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8725` | 220,860.00 USD | 159.86 USD | 0.00 USD | `+38.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 221,560.00 USD | 702.20 USD | 0.00 USD | `+43.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 221,750.00 USD | 193.62 USD | 0.00 USD | `+44.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 222,180.00 USD | 424.63 USD | 0.00 USD | `+49.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 224,970.00 USD | 2,790.00 USD | 0.00 USD | `+49.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 225,310.00 USD | 340.54 USD | 0.00 USD | `+51.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 225,420.00 USD | 108.83 USD | 0.00 USD | `+53.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 225,560.00 USD | 145.72 USD | 0.00 USD | `+54.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 227,590.00 USD | 2,030.00 USD | 0.00 USD | `+57.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 227,730.00 USD | 136.10 USD | 0.00 USD | `+59.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 228,280.00 USD | 550.48 USD | 0.00 USD | `+59.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 228,600.00 USD | 314.99 USD | 0.00 USD | `+63.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 229,200.00 USD | 602.17 USD | 0.00 USD | `+67.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 229,560.00 USD | 360.61 USD | 0.00 USD | `+68.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 230,500.00 USD | 942.77 USD | 0.00 USD | `+72.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 230,900.00 USD | 397.19 USD | 0.00 USD | `+75.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 231,420.00 USD | 525.37 USD | 0.00 USD | `+95.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 244,550.00 USD | 13,130.00 USD | 0.00 USD | `+99.06%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.5320` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 8,680.00 USD | 0.00 USD | 10,290.00 USD |
| `7D` | `0.5330` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD |
| `7D` | `0.5350` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 2,440.00 USD | 3,040.00 USD | 0.00 USD |
| `7D` | `0.5370` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 0.00 USD | 1,550.00 USD | 2,940.00 USD |
| `7D` | `0.5400` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 0.00 USD | 2,920.00 USD | 0.00 USD |
| `7D` | `0.5410` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 8,600.00 USD | 0.00 USD | 13.19 USD |
| `7D` | `0.5420` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 7,660.00 USD | 1,290.00 USD | 2,940.00 USD |
| `7D` | `0.5430` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 0.00 USD | 627.61 USD | 4,900.00 USD |
| `7D` | `0.5440` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 0.00 USD | 523.59 USD | 8,730.00 USD |
| `7D` | `0.5450` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 2,250.00 USD | 0.00 USD | 2,060.00 USD |
| `7D` | `0.5460` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 0.00 USD | 3,030.00 USD | 3,240.00 USD |
| `7D` | `0.5470` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 0.00 USD | 795.70 USD | 29.80 USD |
| `7D` | `0.5480` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 2,000.00 USD | 0.00 USD | 4,470.00 USD |
| `7D` | `0.5490` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 2,100.00 USD | 474.54 USD | 2,040.00 USD |
| `1D` | `0.5500` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,410.00 USD | 0.00 USD | 6,650.00 USD |
| `7D` | `0.5500` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 3,890.00 USD | 967.07 USD | 4,670.00 USD |
| `1D` | `0.5510` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 1,340.00 USD | 0.00 USD | 1,850.00 USD |
| `7D` | `0.5510` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 1,730.00 USD | 1,920.00 USD | 1,860.00 USD |
| `1D` | `0.5520` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 0.00 USD | 1,050.00 USD | 0.00 USD |
| `7D` | `0.5520` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 2,380.00 USD | 0.00 USD | 20.49 USD |
| `1D` | `0.5530` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 2,560.00 USD | 1,410.00 USD | 2,300.00 USD |
| `7D` | `0.5530` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 1,650.00 USD | 1,150.00 USD | 16,240.00 USD |
| `1D` | `0.5540` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 5,390.00 USD | 8,430.00 USD | 7,110.00 USD |
| `7D` | `0.5540` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 11,190.00 USD | 8,450.00 USD | 9,490.00 USD |
| `1D` | `0.5550` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 2,940.00 USD | 0.00 USD | 2,800.00 USD |
| `7D` | `0.5550` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 7,070.00 USD | 1,920.00 USD | 5,330.00 USD |
| `1D` | `0.5560` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 4,540.00 USD | 686.25 USD | 2,960.00 USD |
| `7D` | `0.5560` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 12,540.00 USD | 1,150.00 USD | 7,690.00 USD |
| `1D` | `0.5570` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 5,500.00 USD | 2,460.00 USD | 9,460.00 USD |
| `7D` | `0.5570` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 0.00 USD | 812.74 USD | 3,250.00 USD |
| `1D` | `0.5580` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 1,750.00 USD | 3,180.00 USD | 3,140.00 USD |
| `7D` | `0.5580` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 6,000.00 USD | 6,010.00 USD | 15,050.00 USD |
| `1D` | `0.5590` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 2,530.00 USD | 2,150.00 USD | 2,900.00 USD |
| `7D` | `0.5590` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 2,660.00 USD | 7,220.00 USD | 6,250.00 USD |
| `1D` | `0.5600` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 0.00 USD | 1,910.00 USD | 3,830.00 USD |
| `7D` | `0.5600` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 1,410.00 USD | 938.63 USD | 104.99 USD |
| `1D` | `0.5610` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 4,180.00 USD | 1,380.00 USD | 4,390.00 USD |
| `7D` | `0.5610` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 13,590.00 USD | 4,110.00 USD | 15,090.00 USD |
| `1D` | `0.5620` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 2,630.00 USD | 1,660.00 USD | 3,300.00 USD |
| `7D` | `0.5620` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 12,860.00 USD | 5,460.00 USD | 3,660.00 USD |
| `1D` | `0.5630` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 7,800.00 USD | 1,780.00 USD | 8,110.00 USD |
| `7D` | `0.5630` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 14,240.00 USD | 2,380.00 USD | 3,050.00 USD |
| `1D` | `0.5640` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 4,020.00 USD | 3,380.00 USD | 10,730.00 USD |
| `7D` | `0.5640` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 3,540.00 USD | 0.00 USD | 25.29 USD |
| `1D` | `0.5650` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 2,600.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.5650` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 0.00 USD | 1,210.00 USD | 2,250.00 USD |
| `1D` | `0.5660` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 3,580.00 USD |
| `7D` | `0.5660` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 11,490.00 USD | 1,780.00 USD | 2,330.00 USD |
| `7D` | `0.5670` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 2,890.00 USD |
| `7D` | `0.5680` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 5,100.00 USD | 0.00 USD | 41.99 USD |
| `1D` | `0.5690` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 5,100.00 USD |
| `7D` | `0.5690` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 6.78 USD |
| `1D` | `0.5700` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD |
| `7D` | `0.5700` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 1,030.00 USD | 452.37 USD | 1,090.00 USD |
| `1D` | `0.5710` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 2,350.00 USD | 0.00 USD |
| `7D` | `0.5710` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 0.00 USD | 2,850.00 USD | 1,350.00 USD |
| `1D` | `0.5720` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 832.92 USD | 0.00 USD |
| `7D` | `0.5720` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 0.00 USD | 1,520.00 USD | 10,600.00 USD |
| `1D` | `0.5730` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD |
| `7D` | `0.5730` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 2,690.00 USD | 528.82 USD | 5.20 USD |
| `1D` | `0.5740` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 0.00 USD | 839.21 USD | 3,950.00 USD |
| `7D` | `0.5740` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 18,940.00 USD | 574.82 USD | 1,680.00 USD |
| `1D` | `0.5750` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 4,330.00 USD | 840.09 USD | 20,160.00 USD |
| `7D` | `0.5750` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 187.30 USD |
| `1D` | `0.5760` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 15,020.00 USD | 2,220.00 USD | 2,120.00 USD |
| `7D` | `0.5760` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 2,150.00 USD | 7,300.00 USD | 19.23 USD |
| `1D` | `0.5770` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 16,730.00 USD | 3,970.00 USD | 279.20 USD |
| `7D` | `0.5770` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 21,510.00 USD | 0.00 USD | 222.98 USD |
| `1D` | `0.5780` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 3,070.00 USD | 1,330.00 USD | 10,910.00 USD |
| `7D` | `0.5780` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 19,410.00 USD | 0.00 USD | 1,560.00 USD |
| `1D` | `0.5790` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 11,420.00 USD | 2,690.00 USD | 7,750.00 USD |
| `7D` | `0.5790` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 1,610.00 USD | 0.00 USD | 11,160.00 USD |
| `1D` | `0.5800` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 3,310.00 USD | 2,750.00 USD | 1,590.00 USD |
| `7D` | `0.5800` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 0.00 USD | 3,900.00 USD | 16,760.00 USD |
| `1D` | `0.5810` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 0.00 USD | 3,190.00 USD | 16,700.00 USD |
| `7D` | `0.5810` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 3,220.00 USD |
| `1D` | `0.5820` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 2,580.00 USD | 4,510.00 USD | 4,180.00 USD |
| `7D` | `0.5820` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD |
| `1D` | `0.5830` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 4,910.00 USD | 819.33 USD | 41.65 USD |
| `7D` | `0.5830` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 108.28 USD |
| `1D` | `0.5840` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 2,190.00 USD | 4,320.00 USD |
| `7D` | `0.5840` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 21,370.00 USD |
| `1D` | `0.5850` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 2,950.00 USD | 0.00 USD | 30,870.00 USD |
| `7D` | `0.5850` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 396.16 USD |
| `1D` | `0.5860` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 2,810.00 USD | 2,450.00 USD | 7,900.00 USD |
| `1D` | `0.5870` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 12,190.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.5870` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 1,400.00 USD | 65.70 USD |
| `1D` | `0.5880` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 34,650.00 USD | 8,680.00 USD | 7,790.00 USD |
| `7D` | `0.5880` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 3,110.00 USD | 14,610.00 USD | 0.00 USD |
| `1D` | `0.5890` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 39,360.00 USD | 11,450.00 USD | 6,790.00 USD |
| `7D` | `0.5890` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 43,020.00 USD | 0.00 USD | 8,730.00 USD |
| `1D` | `0.5900` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 24,340.00 USD | 14,260.00 USD | 18,380.00 USD |
| `7D` | `0.5900` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 61,220.00 USD | 1,560.00 USD | 9,130.00 USD |
| `1D` | `0.5910` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 31,110.00 USD | 17,770.00 USD | 19,290.00 USD |
| `7D` | `0.5910` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 0.00 USD | 15,190.00 USD | 16,670.00 USD |
| `1D` | `0.5920` | 967,700.00 USD | 0.00 USD | 967,700.00 USD | 26,620.00 USD | 6,570.00 USD | 10,040.00 USD |
| `7D` | `0.5920` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 11,690.00 USD | 10,620.00 USD | 58,970.00 USD |
| `1D` | `0.5930` | 924,470.00 USD | 0.00 USD | 924,470.00 USD | 12,580.00 USD | 6,710.00 USD | 22,390.00 USD |
| `7D` | `0.5930` | 978,040.00 USD | 0.00 USD | 978,040.00 USD | 25,390.00 USD | 2,880.00 USD | 14,120.00 USD |
| `1D` | `0.5940` | 882,800.00 USD | 0.00 USD | 882,800.00 USD | 25,790.00 USD | 2,040.00 USD | 21,060.00 USD |
| `7D` | `0.5940` | 935,650.00 USD | 0.00 USD | 935,650.00 USD | 5,780.00 USD | 0.00 USD | 144.44 USD |
| `1D` | `0.5950` | 833,910.00 USD | 0.00 USD | 833,910.00 USD | 37,990.00 USD | 5,270.00 USD | 1,640.00 USD |
| `7D` | `0.5950` | 929,730.00 USD | 0.00 USD | 929,730.00 USD | 13,060.00 USD | 0.00 USD | 301.29 USD |
| `1D` | `0.5960` | 789,020.00 USD | 0.00 USD | 789,020.00 USD | 14,970.00 USD | 2,560.00 USD | 12,420.00 USD |
| `7D` | `0.5960` | 916,370.00 USD | 0.00 USD | 916,370.00 USD | 5,120.00 USD | 18,410.00 USD | 9,700.00 USD |
| `1D` | `0.5970` | 759,070.00 USD | 0.00 USD | 759,070.00 USD | 14,120.00 USD | 811.64 USD | 5,180.00 USD |
| `7D` | `0.5970` | 883,130.00 USD | 0.00 USD | 883,130.00 USD | 5,560.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.5980` | 738,960.00 USD | 0.00 USD | 738,960.00 USD | 19,780.00 USD | 6,850.00 USD | 8,890.00 USD |
| `7D` | `0.5980` | 877,580.00 USD | 0.00 USD | 877,580.00 USD | 37,820.00 USD | 5,380.00 USD | 17,810.00 USD |
| `1D` | `0.5990` | 703,440.00 USD | 0.00 USD | 703,440.00 USD | 8,950.00 USD | 3,370.00 USD | 3,890.00 USD |
| `7D` | `0.5990` | 816,560.00 USD | 0.00 USD | 816,560.00 USD | 3,320.00 USD | 0.00 USD | 52.70 USD |
| `1D` | `0.6000` | 687,230.00 USD | 0.00 USD | 687,230.00 USD | 22,910.00 USD | 3,360.00 USD | 10,870.00 USD |
| `7D` | `0.6000` | 813,180.00 USD | 0.00 USD | 813,180.00 USD | 16,110.00 USD | 0.00 USD | 11,950.00 USD |
| `1D` | `0.6010` | 650,090.00 USD | 0.00 USD | 650,090.00 USD | 6,720.00 USD | 6,370.00 USD | 5,020.00 USD |
| `7D` | `0.6010` | 785,130.00 USD | 0.00 USD | 785,130.00 USD | 12,110.00 USD | 4,090.00 USD | 50.15 USD |
| `1D` | `0.6020` | 631,970.00 USD | 0.00 USD | 631,970.00 USD | 11,780.00 USD | 8,040.00 USD | 15,300.00 USD |
| `7D` | `0.6020` | 768,880.00 USD | 0.00 USD | 768,880.00 USD | 8,860.00 USD | 7,150.00 USD | 17,420.00 USD |
| `1D` | `0.6030` | 596,840.00 USD | 0.00 USD | 596,840.00 USD | 40,580.00 USD | 17,840.00 USD | 20,110.00 USD |
| `7D` | `0.6030` | 735,450.00 USD | 0.00 USD | 735,450.00 USD | 38,530.00 USD | 0.00 USD | 18,260.00 USD |
| `1D` | `0.6040` | 518,320.00 USD | 0.00 USD | 518,320.00 USD | 16,550.00 USD | 20,270.00 USD | 7,580.00 USD |
| `7D` | `0.6040` | 678,660.00 USD | 0.00 USD | 678,660.00 USD | 0.00 USD | 30,380.00 USD | 89.59 USD |
| `1D` | `0.6050` | 473,930.00 USD | 0.00 USD | 473,930.00 USD | 23,200.00 USD | 2,140.00 USD | 13,690.00 USD |
| `7D` | `0.6050` | 648,190.00 USD | 0.00 USD | 648,190.00 USD | 0.00 USD | 0.00 USD | 20,810.00 USD |
| `1D` | `0.6060` | 434,890.00 USD | 0.00 USD | 434,890.00 USD | 25,160.00 USD | 656.96 USD | 18,880.00 USD |
| `7D` | `0.6060` | 627,380.00 USD | 0.00 USD | 627,380.00 USD | 30,590.00 USD | 5,760.00 USD | 28,240.00 USD |
| `1D` | `0.6070` | 390,200.00 USD | 0.00 USD | 390,200.00 USD | 31,540.00 USD | 4,080.00 USD | 25,230.00 USD |
| `7D` | `0.6070` | 562,790.00 USD | 0.00 USD | 562,790.00 USD | 11,560.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6080` | 329,350.00 USD | 0.00 USD | 329,350.00 USD | 26,190.00 USD | 7,250.00 USD | 3,080.00 USD |
| `7D` | `0.6080` | 551,230.00 USD | 0.00 USD | 551,230.00 USD | 2,860.00 USD | 0.00 USD | 30,370.00 USD |
| `1D` | `0.6090` | 292,840.00 USD | 0.00 USD | 292,840.00 USD | 18,460.00 USD | 3,030.00 USD | 7,680.00 USD |
| `7D` | `0.6090` | 518,000.00 USD | 0.00 USD | 518,000.00 USD | 13,920.00 USD | 44,860.00 USD | 44,040.00 USD |
| `1D` | `0.6100` | 263,660.00 USD | 0.00 USD | 263,660.00 USD | 5,960.00 USD | 1,620.00 USD | 41,540.00 USD |
| `7D` | `0.6100` | 415,180.00 USD | 0.00 USD | 415,180.00 USD | 18,600.00 USD | 2,570.00 USD | 0.00 USD |
| `1D` | `0.6110` | 214,530.00 USD | 0.00 USD | 214,530.00 USD | 36,980.00 USD | 12,300.00 USD | 17,670.00 USD |
| `7D` | `0.6110` | 394,010.00 USD | 0.00 USD | 394,010.00 USD | 34,870.00 USD | 12,980.00 USD | 48,480.00 USD |
| `1D` | `0.6120` | 147,590.00 USD | 0.00 USD | 147,590.00 USD | 47,950.00 USD | 6,740.00 USD | 7,780.00 USD |
| `7D` | `0.6120` | 297,680.00 USD | 0.00 USD | 297,680.00 USD | 35,760.00 USD | 16,650.00 USD | 4,130.00 USD |
| `1D` | `0.6130` | 85,130.00 USD | 0.00 USD | 85,130.00 USD | 2,480.00 USD | 6,720.00 USD | 40,120.00 USD |
| `7D` | `0.6130` | 241,130.00 USD | 0.00 USD | 241,130.00 USD | 105,970.00 USD | 9,220.00 USD | 18,530.00 USD |
| `1D` | `0.6140` | 35,810.00 USD | 0.00 USD | 35,810.00 USD | 0.00 USD | 9,520.00 USD | 0.00 USD |
| `7D` | `0.6140` | 107,410.00 USD | 0.00 USD | 107,410.00 USD | 17,720.00 USD | 6,170.00 USD | 159.06 USD |
| `1D` | `0.6180` | 26,280.00 USD | 0.00 USD | 26,280.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD |
| `7D` | `0.6180` | 83,360.00 USD | 0.00 USD | 83,360.00 USD | 0.00 USD | 0.00 USD | 173.29 USD |
| `7D` | `0.6190` | 83,190.00 USD | 0.00 USD | 83,190.00 USD | 0.00 USD | 0.00 USD | 182.11 USD |
| `1D` | `0.6200` | 24,530.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD | 0.00 USD | 50.92 USD |
| `7D` | `0.6200` | 83,000.00 USD | 0.00 USD | 83,000.00 USD | 13,870.00 USD | 0.00 USD | 29,070.00 USD |
| `7D` | `0.6210` | 40,070.00 USD | 0.00 USD | 40,070.00 USD | 0.00 USD | 22,640.00 USD | 0.00 USD |
| `1D` | `0.6250` | 24,480.00 USD | 0.00 USD | 24,480.00 USD | 2,520.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6260` | 21,950.00 USD | 0.00 USD | 21,950.00 USD | 0.00 USD | 8,370.00 USD | 13,580.00 USD |
| `7D` | `0.6260` | 17,420.00 USD | 0.00 USD | 17,420.00 USD | 0.00 USD | 0.00 USD | 17,420.00 USD |
| `1D` | `0.6270` | 20,260.00 USD | 20,260.00 USD | 0.00 USD | 0.00 USD | 3,780.00 USD | 16,480.00 USD |
| `1D` | `0.6270` | 40,520.00 USD | 40,520.00 USD | 0.00 USD | 0.00 USD | 3,780.00 USD | 16,480.00 USD |
| `7D` | `0.6270` | 26,520.00 USD | 26,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26,520.00 USD |
| `7D` | `0.6270` | 53,040.00 USD | 53,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26,520.00 USD |
| `1D` | `0.6280` | 102,730.00 USD | 102,730.00 USD | 0.00 USD | 10,020.00 USD | 26,790.00 USD | 25,400.00 USD |
| `7D` | `0.6280` | 103,970.00 USD | 103,970.00 USD | 0.00 USD | 0.00 USD | 34,280.00 USD | 16,650.00 USD |
| `1D` | `0.6290` | 153,450.00 USD | 153,450.00 USD | 0.00 USD | 23,200.00 USD | 7,350.00 USD | 20,170.00 USD |
| `7D` | `0.6290` | 152,780.00 USD | 152,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 48,810.00 USD |
| `1D` | `0.6300` | 213,350.00 USD | 213,350.00 USD | 0.00 USD | 27,730.00 USD | 4,090.00 USD | 28,080.00 USD |
| `7D` | `0.6300` | 217,370.00 USD | 217,370.00 USD | 0.00 USD | 30,590.00 USD | 5,760.00 USD | 28,240.00 USD |
| `1D` | `0.6310` | 312,110.00 USD | 312,110.00 USD | 0.00 USD | 42,960.00 USD | 8,860.00 USD | 46,930.00 USD |
| `7D` | `0.6310` | 229,030.00 USD | 229,030.00 USD | 0.00 USD | 11,560.00 USD | 0.00 USD | 103.98 USD |
| `1D` | `0.6320` | 387,900.00 USD | 387,900.00 USD | 0.00 USD | 51,560.00 USD | 10,170.00 USD | 14,060.00 USD |
| `7D` | `0.6320` | 229,290.00 USD | 229,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 265.37 USD |
| `1D` | `0.6330` | 444,550.00 USD | 444,550.00 USD | 0.00 USD | 21,410.00 USD | 12,370.00 USD | 22,870.00 USD |
| `7D` | `0.6330` | 306,410.00 USD | 306,410.00 USD | 0.00 USD | 57,940.00 USD | 0.00 USD | 19,180.00 USD |
| `1D` | `0.6340` | 521,530.00 USD | 521,530.00 USD | 0.00 USD | 31,400.00 USD | 4,810.00 USD | 40,770.00 USD |
| `7D` | `0.6340` | 328,370.00 USD | 328,370.00 USD | 0.00 USD | 21,840.00 USD | 0.00 USD | 121.40 USD |
| `1D` | `0.6350` | 617,690.00 USD | 617,690.00 USD | 0.00 USD | 64,020.00 USD | 10,620.00 USD | 21,520.00 USD |
| `7D` | `0.6350` | 444,340.00 USD | 444,340.00 USD | 0.00 USD | 69,190.00 USD | 10,770.00 USD | 36,010.00 USD |
| `1D` | `0.6360` | 722,090.00 USD | 722,090.00 USD | 0.00 USD | 53,920.00 USD | 9,200.00 USD | 41,270.00 USD |
| `7D` | `0.6360` | 500,940.00 USD | 500,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 56,590.00 USD |
| `1D` | `0.6370` | 731,350.00 USD | 731,350.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD | 7,540.00 USD |
| `7D` | `0.6370` | 510,120.00 USD | 510,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,180.00 USD |
| `1D` | `0.6380` | 814,060.00 USD | 814,060.00 USD | 0.00 USD | 47,080.00 USD | 22,800.00 USD | 12,820.00 USD |
| `7D` | `0.6380` | 586,950.00 USD | 586,950.00 USD | 0.00 USD | 32,220.00 USD | 0.00 USD | 44,610.00 USD |
| `1D` | `0.6390` | 887,840.00 USD | 887,840.00 USD | 0.00 USD | 14,290.00 USD | 6,680.00 USD | 52,810.00 USD |
| `7D` | `0.6390` | 648,630.00 USD | 648,630.00 USD | 0.00 USD | 24,230.00 USD | 15,680.00 USD | 21,780.00 USD |
| `1D` | `0.6400` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 65,540.00 USD | 38,500.00 USD | 18,890.00 USD |
| `7D` | `0.6400` | 694,750.00 USD | 694,750.00 USD | 0.00 USD | 36,980.00 USD | 0.00 USD | 9,130.00 USD |
| `1D` | `0.6410` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 34,570.00 USD | 19,840.00 USD | 15,770.00 USD |
| `7D` | `0.6410` | 725,120.00 USD | 725,120.00 USD | 0.00 USD | 0.00 USD | 24,060.00 USD | 6,310.00 USD |
| `1D` | `0.6420` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 55,390.00 USD | 9,980.00 USD | 15,000.00 USD |
| `7D` | `0.6420` | 836,730.00 USD | 836,730.00 USD | 0.00 USD | 55,350.00 USD | 26,560.00 USD | 29,700.00 USD |
| `1D` | `0.6430` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 25,440.00 USD | 11,080.00 USD | 30,350.00 USD |
| `7D` | `0.6430` | 895,550.00 USD | 895,550.00 USD | 0.00 USD | 31,500.00 USD | 10,020.00 USD | 17,300.00 USD |
| `1D` | `0.6440` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 36,680.00 USD | 14,890.00 USD | 61,110.00 USD |
| `7D` | `0.6440` | 962,190.00 USD | 962,190.00 USD | 0.00 USD | 34,270.00 USD | 17,680.00 USD | 14,690.00 USD |
| `1D` | `0.6450` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 62,440.00 USD | 14,740.00 USD | 15,770.00 USD |
| `7D` | `0.6450` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 81,220.00 USD | 15,560.00 USD | 35,760.00 USD |
| `1D` | `0.6460` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 29,100.00 USD | 12,810.00 USD | 13,550.00 USD |
| `7D` | `0.6460` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 91,390.00 USD | 31,070.00 USD | 112,090.00 USD |
| `1D` | `0.6470` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 54,020.00 USD | 18,030.00 USD | 11,980.00 USD |
| `7D` | `0.6470` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 15,220.00 USD | 26,520.00 USD | 9,470.00 USD |
| `1D` | `0.6480` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 83,050.00 USD | 12,090.00 USD | 9,230.00 USD |
| `7D` | `0.6480` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 94,210.00 USD | 5,380.00 USD | 41,750.00 USD |
| `1D` | `0.6490` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 48,180.00 USD | 4,600.00 USD | 15,000.00 USD |
| `7D` | `0.6490` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 36,340.00 USD | 0.00 USD | 17,650.00 USD |
| `1D` | `0.6500` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 49,890.00 USD | 9,280.00 USD | 5,990.00 USD |
| `7D` | `0.6500` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 53,330.00 USD | 0.00 USD | 122,040.00 USD |
| `1D` | `0.6510` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 52,270.00 USD | 0.00 USD | 14,330.00 USD |
| `7D` | `0.6510` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 244,480.00 USD | 8,270.00 USD | 18,220.00 USD |
| `1D` | `0.6520` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 65,860.00 USD | 13,800.00 USD | 5,780.00 USD |
| `7D` | `0.6520` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 74,540.00 USD | 6,720.00 USD | 86,550.00 USD |
| `1D` | `0.6530` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 16,100.00 USD | 3,910.00 USD | 11.74 USD |
| `7D` | `0.6530` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 4,440.00 USD | 47,250.00 USD |
| `1D` | `0.6540` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 22,250.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `0.6540` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 15,730.00 USD | 0.00 USD | 14,800.00 USD |
| `1D` | `0.6550` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,950.00 USD |
| `7D` | `0.6550` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 414.15 USD |
| `1D` | `0.6560` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,080.00 USD |
| `7D` | `0.6560` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 5,380.00 USD | 651.75 USD |
| `1D` | `0.6570` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,460.00 USD |
| `7D` | `0.6570` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 6,350.00 USD | 447.57 USD |
| `1D` | `0.6580` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 3,310.00 USD | 48.99 USD |
| `7D` | `0.6580` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 21,920.00 USD | 9,580.00 USD |
| `1D` | `0.6590` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 5,890.00 USD | 164.02 USD |
| `7D` | `0.6590` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 11,320.00 USD | 331.05 USD |
| `1D` | `0.6600` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 6,010.00 USD | 9,280.00 USD | 59.63 USD |
| `7D` | `0.6600` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 7,100.00 USD | 249.08 USD |
| `1D` | `0.6610` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 6,690.00 USD | 835.70 USD | 142.10 USD |
| `7D` | `0.6610` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 8,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6620` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 530.84 USD | 7,710.00 USD |
| `7D` | `0.6620` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 128.16 USD |
| `1D` | `0.6630` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 2,590.00 USD | 0.00 USD | 2,310.00 USD |
| `7D` | `0.6630` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 254.70 USD |
| `1D` | `0.6640` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 11,190.00 USD | 837.01 USD | 135.08 USD |
| `7D` | `0.6640` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 33,660.00 USD | 0.00 USD | 7,050.00 USD |
| `1D` | `0.6650` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 3,160.00 USD | 17,470.00 USD |
| `7D` | `0.6650` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 6,770.00 USD | 405.36 USD |
| `1D` | `0.6660` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 839.67 USD | 7,590.00 USD |
| `7D` | `0.6660` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 148.18 USD |
| `1D` | `0.6670` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 18,850.00 USD | 0.00 USD | 66.01 USD |
| `7D` | `0.6670` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 416.46 USD |
| `1D` | `0.6680` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 158.16 USD |
| `7D` | `0.6680` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 224.19 USD |
| `1D` | `0.6690` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 3,550.00 USD | 5,500.00 USD |
| `7D` | `0.6690` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 448.05 USD |
| `1D` | `0.6700` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 8,830.00 USD | 1,920.00 USD | 24,760.00 USD |
| `7D` | `0.6700` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 546.45 USD |
| `1D` | `0.6710` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 41,970.00 USD | 0.00 USD | 5,960.00 USD |
| `7D` | `0.6710` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 58,470.00 USD | 0.00 USD | 30,140.00 USD |
| `1D` | `0.6720` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 1,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6730` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 25,660.00 USD | 3,670.00 USD | 5,560.00 USD |
| `7D` | `0.6730` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 99.42 USD |
| `1D` | `0.6740` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 64,370.00 USD | 8,170.00 USD | 9,210.00 USD |
| `7D` | `0.6740` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 39,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6750` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 30,000.00 USD | 1,410.00 USD | 14,370.00 USD |
| `7D` | `0.6750` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 75,730.00 USD | 3,480.00 USD |
| `1D` | `0.6760` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `0.6760` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 2,240.00 USD | 33,090.00 USD |
| `1D` | `0.6770` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 19,930.00 USD | 9,080.00 USD | 17,950.00 USD |
| `7D` | `0.6770` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 63,600.00 USD | 4,190.00 USD | 21,590.00 USD |
| `1D` | `0.6780` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 33,610.00 USD | 8,030.00 USD | 12,150.00 USD |
| `7D` | `0.6780` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 14,960.00 USD | 124.93 USD |
| `1D` | `0.6790` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 2,940.00 USD | 18,610.00 USD | 13,680.00 USD |
| `7D` | `0.6790` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 4,160.00 USD |
| `1D` | `0.6800` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 4,540.00 USD | 686.25 USD | 5,410.00 USD |
| `7D` | `0.6800` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 6,120.00 USD | 1,150.00 USD | 2,610.00 USD |
| `1D` | `0.6810` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 5,500.00 USD | 2,460.00 USD | 17,010.00 USD |
| `7D` | `0.6810` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 15,720.00 USD | 145.79 USD |
| `1D` | `0.6820` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 24,350.00 USD | 16,950.00 USD | 9,650.00 USD |
| `7D` | `0.6820` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 32,570.00 USD | 37,730.00 USD | 0.00 USD |
| `1D` | `0.6830` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 27,110.00 USD | 15,380.00 USD | 32,700.00 USD |
| `7D` | `0.6830` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 17,730.00 USD | 52,040.00 USD |
| `1D` | `0.6840` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 45,780.00 USD | 12,210.00 USD | 15,180.00 USD |
| `7D` | `0.6840` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 57,890.00 USD | 36,580.00 USD | 54,240.00 USD |
| `1D` | `0.6850` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 31,830.00 USD | 7,150.00 USD | 27,660.00 USD |
| `7D` | `0.6850` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 24,240.00 USD | 6,860.00 USD | 17,680.00 USD |
| `1D` | `0.6860` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 42,880.00 USD | 5,260.00 USD | 15,900.00 USD |
| `7D` | `0.6860` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 32,660.00 USD | 9,830.00 USD | 0.00 USD |
| `1D` | `0.6870` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 63,220.00 USD | 1,160.00 USD | 3,820.00 USD |
| `7D` | `0.6870` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 19,860.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6880` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 20,970.00 USD | 11,390.00 USD | 9,730.00 USD |
| `7D` | `0.6880` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 24,610.00 USD | 17,300.00 USD | 2,970.00 USD |
| `1D` | `0.6890` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 1,180.00 USD | 0.00 USD | 8,480.00 USD |
| `7D` | `0.6890` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 4,850.00 USD | 12,670.00 USD | 77.75 USD |
| `1D` | `0.6900` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 18,600.00 USD | 4,990.00 USD | 21,690.00 USD |
| `7D` | `0.6900` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 3,540.00 USD | 4,480.00 USD | 16,550.00 USD |
| `1D` | `0.6910` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 31,460.00 USD | 1,730.00 USD | 0.00 USD |
| `7D` | `0.6910` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 69,620.00 USD | 2,090.00 USD | 37,650.00 USD |
| `7D` | `0.6920` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,370.00 USD |
| `7D` | `0.6930` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 14,220.00 USD | 0.00 USD | 42,600.00 USD |
| `7D` | `0.6950` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 31,450.00 USD | 0.00 USD | 12,390.00 USD |
| `7D` | `0.6960` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 28,500.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6970` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 21,650.00 USD | 6,030.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `87.79M` | Total OI Tokens: `140,232,255.7 APT`
  * 1h OI Change: `+1.04%` | 4h OI Change: `+0.24%` | 24h OI Change: `-10.82%`
  * Exchange Breakdown: Binance=`15.88M` | Bybit=`17.39M` | OKX=`4.23M` | Hyperliquid=`3.51M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.77K` | Last 24h: `836.23` | Last 3d: `10.58K` | Last 7d: `3.38K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0073%` | **USDT OKX** | `0.0022%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0035%` |
| **USDT MEXC** | `0.0070%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0026%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `APT` | `48.50%` | `51.50%` | `0.94` | 2,930,000.00 USD |
| `15M` | `Binance` | `51.62%` | `48.38%` | `1.07` | 843,090.00 USD |
| `15M` | `OKX` | `63.96%` | `36.04%` | `1.77` | 775,370.00 USD |
| `15M` | `Bybit` | `53.28%` | `46.72%` | `1.14` | 135,130.00 USD |
| `15M` | `KuCoin` | `18.6%` | `81.4%` | `0.23` | 19,620.00 USD |
| `15M` | `Gate` | `63.08%` | `36.92%` | `1.71` | 54,630.00 USD |
| `15M` | `Bitget` | `57.3%` | `42.7%` | `1.34` | 46,950.00 USD |
| `15M` | `BingX` | `45.32%` | `54.68%` | `0.83` | 33,720.00 USD |
| `15M` | `MEXC` | `58.72%` | `41.28%` | `1.42` | 100,500.00 USD |
| `15M` | `Bitunix` | `68.53%` | `31.47%` | `2.18` | 65,940.00 USD |
| `15M` | `Hyperliquid` | `45.03%` | `54.97%` | `0.82` | 8,020.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `47.39%` | `52.61%` | `0.90` | 451,670.00 USD |
| `15M` | `Crypto.com` | `100%` | `0%` | `1.00` | 2.84 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 371,530.00 USD |
| `15M` | `HTX` | `33.28%` | `66.72%` | `0.50` | 3,370.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `24.36%` | `75.64%` | `0.32` | 701.88 USD |
| `15M` | `Aster` | `90.24%` | `9.76%` | `9.25` | 174.66 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `87%` | `13%` | `6.69` | 12,170.00 USD |
| `15M` | `Whale Positions` | `51.62%` | `48.38%` | `1.07` | 843,090.00 USD |
| `15M` | `Global Accounts` | `48.50%` | `51.50%` | `0.94` | 2,930,000.00 USD |
| `1H` | `APT` | `46.75%` | `53.25%` | `0.88` | 10,460,000.00 USD |
| `1H` | `Binance` | `56.03%` | `43.97%` | `1.27` | 3,520,000.00 USD |
| `1H` | `OKX` | `62.17%` | `37.83%` | `1.64` | 1,850,000.00 USD |
| `1H` | `Bybit` | `52.27%` | `47.73%` | `1.10` | 472,600.00 USD |
| `1H` | `KuCoin` | `45.98%` | `54.02%` | `0.85` | 369,310.00 USD |
| `1H` | `Gate` | `69.97%` | `30.03%` | `2.33` | 170,950.00 USD |
| `1H` | `Bitget` | `50.55%` | `49.45%` | `1.02` | 168,360.00 USD |
| `1H` | `BingX` | `16.47%` | `83.53%` | `0.20` | 454,740.00 USD |
| `1H` | `MEXC` | `67.41%` | `32.59%` | `2.07` | 238,100.00 USD |
| `1H` | `Bitunix` | `64.6%` | `35.4%` | `1.82` | 152,500.00 USD |
| `1H` | `Hyperliquid` | `36.6%` | `63.4%` | `0.58` | 84,300.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.84%` | `52.16%` | `0.92` | 1,520,000.00 USD |
| `1H` | `Crypto.com` | `50.04%` | `49.96%` | `1.00` | 22.69 USD |
| `1H` | `WhiteBIT` | `0%` | `100%` | `0.00` | 1,380,000.00 USD |
| `1H` | `HTX` | `56.59%` | `43.41%` | `1.30` | 20,460.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `44.71%` | `55.29%` | `0.81` | 27,650.00 USD |
| `1H` | `Aster` | `46.04%` | `53.96%` | `0.85` | 2,440.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `93.28%` | `6.72%` | `13.88` | 32,410.00 USD |
| `1H` | `Whale Positions` | `56.03%` | `43.97%` | `1.27` | 3,520,000.00 USD |
| `1H` | `Global Accounts` | `46.75%` | `53.25%` | `0.88` | 10,460,000.00 USD |
| `4H` | `APT` | `48.24%` | `51.76%` | `0.93` | 17,010,000.00 USD |
| `4H` | `Binance` | `50.83%` | `49.17%` | `1.03` | 5,580,000.00 USD |
| `4H` | `OKX` | `53.94%` | `46.06%` | `1.17` | 1,510,000.00 USD |
| `4H` | `Bybit` | `53.09%` | `46.91%` | `1.13` | 1,730,000.00 USD |
| `4H` | `KuCoin` | `51.03%` | `48.97%` | `1.04` | 2,020,000.00 USD |
| `4H` | `Gate` | `51.05%` | `48.95%` | `1.04` | 359,320.00 USD |
| `4H` | `Bitget` | `50.82%` | `49.18%` | `1.03` | 739,770.00 USD |
| `4H` | `BingX` | `23.33%` | `76.67%` | `0.30` | 1,920,000.00 USD |
| `4H` | `MEXC` | `48.92%` | `51.08%` | `0.96` | 758,690.00 USD |
| `4H` | `Bitunix` | `38.74%` | `61.26%` | `0.63` | 251,290.00 USD |
| `4H` | `Hyperliquid` | `56.46%` | `43.54%` | `1.30` | 448,800.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.99%` | `50.01%` | `1.00` | 850,420.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `53.62%` | `46.38%` | `1.16` | 745,020.00 USD |
| `4H` | `HTX` | `62.79%` | `37.21%` | `1.69` | 2,860.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `59.51%` | `40.49%` | `1.47` | 9,810.00 USD |
| `4H` | `Aster` | `52.72%` | `47.28%` | `1.12` | 69,140.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `53.23%` | `46.77%` | `1.14` | 12,870.00 USD |
| `4H` | `Whale Positions` | `50.83%` | `49.17%` | `1.03` | 5,580,000.00 USD |
| `4H` | `Global Accounts` | `48.24%` | `51.76%` | `0.93` | 17,010,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.6208` | `0.6182` | `0.6208` | `0.6208` | `0.6153` | 335,089.06 USD | 145,222.32 USD | 189,866.74 USD | -44,644.43 USD | `-13.32%` | `3B / 19S` |
| `5:00 UTC` | `0.6160` | `0.6165` | `0.6160` | `0.6201` | `0.6149` | 344,140.22 USD | 188,669.15 USD | 155,471.07 USD | 33,198.09 USD | `+9.65%` | `14B / 12S` |
| `0:00 UTC` | `0.6158` | `0.6153` | `0.6158` | `0.6177` | `0.6136` | 428,959.14 USD | 201,402.03 USD | 227,557.12 USD | -26,155.09 USD | `-6.10%` | `3B / 7S` |
| `5:00 UTC` | `0.6158` | `0.6152` | `0.6158` | `0.6166` | `0.6136` | 219,959.16 USD | 99,252.63 USD | 120,706.54 USD | -21,453.91 USD | `-9.75%` | `3B / 6S` |
| `0:00 UTC` | `0.6141` | `0.6141` | `0.6141` | `0.6168` | `0.6118` | 465,814.11 USD | 219,511.96 USD | 246,302.16 USD | -26,790.20 USD | `-5.75%` | `11B / 9S` |
| `5:00 UTC` | `0.6133` | `0.6164` | `0.6133` | `0.6190` | `0.6129` | 353,127.32 USD | 155,401.13 USD | 197,726.18 USD | -42,325.05 USD | `-11.99%` | `13B / 7S` |
| `0:00 UTC` | `0.6183` | `0.6185` | `0.6183` | `0.6199` | `0.6169` | 302,468.78 USD | 212,821.71 USD | 89,647.07 USD | 123,174.63 USD | `+40.72%` | `12B / 0S` |
| `5:00 UTC` | `0.6210` | `0.6206` | `0.6210` | `0.6231` | `0.6177` | 266,209.21 USD | 131,000.13 USD | 135,209.07 USD | -4,208.94 USD | `-1.58%` | `17B / 11S` |
| `0:00 UTC` | `0.6236` | `0.6234` | `0.6236` | `0.6246` | `0.6200` | 327,504.62 USD | 174,157.60 USD | 153,347.02 USD | 20,810.58 USD | `+6.35%` | `6B / 7S` |
| `5:00 UTC` | `0.6270` | `0.6253` | `0.6270` | `0.6285` | `0.6217` | 346,332.11 USD | 191,817.90 USD | 154,514.21 USD | 37,303.69 USD | `+10.77%` | `23B / 9S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 21:06` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6898` | 0.00 USD | 0.00 USD |
| `10-28 21:06` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6871` | 68,000.00 USD | 0.00 USD |
| `10-28 21:02` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6867` | 0.00 USD | 0.00 USD |
| `10-28 20:37` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6858` | 33,000.00 USD | 0.00 USD |
| `10-28 20:01` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6782` | 0.00 USD | 0.00 USD |
| `10-28 20:01` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6808` | 79,000.00 USD | 0.00 USD |
| `10-28 19:48` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6764` | 22,000.00 USD | 0.00 USD |
| `10-28 19:46` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6752` | 44,000.00 USD | 0.00 USD |
| `10-28 19:46` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6752` | 44,000.00 USD | 0.00 USD |
| `10-28 19:43` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6771` | 0.00 USD | 0.00 USD |
| `10-28 19:43` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6793` | 39,000.00 USD | 0.00 USD |
| `10-28 19:41` | `Volume 1.0M APT` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6752` | 361,000.00 USD | 0.00 USD |
| `10-28 19:35` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6807` | 0.00 USD | 0.00 USD |
| `10-28 19:31` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6762` | 79,000.00 USD | 0.00 USD |
| `10-28 19:31` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6762` | 79,000.00 USD | 0.00 USD |
| `10-28 19:31` | `Range 0.002` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `0.6762` | 106,000.00 USD | 0.00 USD |
| `10-28 19:21` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6771` | 75,000.00 USD | 0.00 USD |
| `10-28 19:07` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6859` | 121,000.00 USD | 0.00 USD |
| `10-28 18:48` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6796` | 47,000.00 USD | 0.00 USD |
| `10-28 18:44` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6793` | 107,000.00 USD | 0.00 USD |
| `10-28 18:37` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6818` | 0.00 USD | 0.00 USD |
| `10-28 17:54` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6887` | 177,000.00 USD | 0.00 USD |
| `10-28 17:46` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6884` | 112,000.00 USD | 0.00 USD |
| `10-28 17:43` | `Volume 1.0M APT` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6842` | 275,000.00 USD | 0.00 USD |
| `10-28 17:36` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6934` | 22,000.00 USD | 0.00 USD |
| `10-28 17:03` | `Volume 1.0M APT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6995` | 234,000.00 USD | 0.00 USD |
| `10-28 16:15` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6994` | 140,000.00 USD | 0.00 USD |
| `10-28 16:02` | `Volume 1.0M APT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6994` | 223,000.00 USD | 0.00 USD |
| `10-28 14:46` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6950` | 67,000.00 USD | 0.00 USD |
| `10-28 14:31` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6922` | 0.00 USD | 0.00 USD |
| `10-28 14:31` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6896` | 58,000.00 USD | 0.00 USD |
| `10-28 14:31` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6896` | 58,000.00 USD | 0.00 USD |
| `10-28 14:09` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6972` | 0.00 USD | 0.00 USD |
| `10-28 14:06` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6976` | 0.00 USD | 0.00 USD |
| `10-28 14:06` | `Range 0.002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.7006` | 0.00 USD | 0.00 USD |
| `10-28 13:57` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6962` | 0.00 USD | 0.00 USD |
| `10-28 13:33` | `Volume 1.0M APT` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6929` | 351,000.00 USD | 0.00 USD |
| `10-28 12:44` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6912` | 0.00 USD | 0.00 USD |
| `10-28 12:22` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6924` | 0.00 USD | 0.00 USD |
| `10-28 10:16` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6976` | 25,000.00 USD | 0.00 USD |
| `10-28 09:48` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6958` | 18,000.00 USD | 0.00 USD |
| `10-28 09:29` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6985` | 55,000.00 USD | 0.00 USD |
| `10-28 09:11` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.7008` | 0.00 USD | 0.00 USD |
| `10-28 09:04` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.7021` | 0.00 USD | 0.00 USD |
| `10-28 09:00` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.7001` | 27,000.00 USD | 0.00 USD |
| `10-28 08:49` | `Range 0.002` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `0.6966` | 73,000.00 USD | 0.00 USD |
| `10-28 08:31` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6974` | 0.00 USD | 0.00 USD |
| `10-28 07:29` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.7003` | 0.00 USD | 0.00 USD |
| `10-28 07:23` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6977` | 10,000.00 USD | 0.00 USD |
| `10-28 06:12` | `Range 0.002` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.6982` | 122,000.00 USD | 0.00 USD |
| `10-28 05:31` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6963` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -6,550.00 USD | -9,050.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,580.00 USD | 42,180.00 USD | **`ACCUMULATION`** |
| `30m` | 13,140.00 USD | 15,570.00 USD | **`ACCUMULATION`** |
| `1h` | 9,780.00 USD | 199,080.00 USD | **`ACCUMULATION`** |
| `2h` | 38,710.00 USD | 103,630.00 USD | **`ACCUMULATION`** |
| `4h` | -41,420.00 USD | 352,580.00 USD | **`ACCUMULATION`** |
| `6h` | -272,050.00 USD | -12,820.00 USD | **`DISTRIBUTION`** |
| `8h` | -220,060.00 USD | 365,400.00 USD | **`ACCUMULATION`** |
| `12h` | -746,340.00 USD | -1,140,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,210,000.00 USD | -8,080,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,900,000.00 USD | -25,500,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,110,000.00 USD | -105,060,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-6.55K` | 15m=`-1.58K` | 1h=`+9.78K` | 24h=`-1.21M`
* Futures Capital Netflows: 5m=`-9.05K` | 15m=`+42.18K` | 1h=`+199.08K` | 24h=`-8.08M`
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
  * `2026-10-30 16:26:21 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:29:21 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.6880` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-0.5122` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `3.69`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.6921` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.89` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-2.31`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.6956`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
