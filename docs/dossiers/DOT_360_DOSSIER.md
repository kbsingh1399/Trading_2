# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 14:23:36 IST` (`2026-10-30 08:53:36 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9250` | **Live Ask Quote**: `0.9460` | **Mid Price**: `0.9355`
- **Spread Points**: `21.00` | **Spread BPS**: `224.48 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
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
  * Session VWAP: `0.9092` | VWAP Z-Score: `+0.71` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0079` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `47.07` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.9805` | Lower -3.00σ Band: `0.8379`
  * Upper +2.51σ Band: `0.9688` | Lower -2.51σ Band: `0.8495`
  * Upper +2.01σ Band: `0.9569` | Lower -2.01σ Band: `0.8614`
  * Upper +2.00σ Band: `0.9567` | Lower -2.00σ Band: `0.8616`
  * Upper +1.28σ Band: `0.9396` | Lower -1.28σ Band: `0.8788`
  * Upper +1.00σ Band: `0.9329` | Lower -1.00σ Band: `0.8854`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9332` | EMA-20=`0.9307` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9311` (Slope: `+0.0000`) | EMA-100=`0.9428`
  * Institutional Anchors: EMA-144=`0.9508` | EMA-200=`0.9584` (Slope: `-0.3030`) | EMA-233=`0.9618`
- **Range Boundaries**: 24H High=`1.01` | 24H Low=`0.8570` | Weekly High=`1.03` | Weekly Low=`0.8570`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9356` (Distance: `-0.01%`)
  * Point of Control (POC) = `0.9119` (Distance: `+2.59%`)
  * Value Area Low (VAL) = `0.8901` (Distance: `+5.10%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.02` | Weekly POC=`0.9945` | Weekly VAL=`0.9701`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9330` | Low=`0.8570`
  * London Session (08:00-16:00 UTC): High=`0.9480` | Low=`0.9250`
  * New York Session (13:00-21:00 UTC): High=`0.9411` | Low=`0.9299`
  * Initial Balance (First Hour): IB High=`0.9480` | IB Low=`0.9290`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9318` - `0.9392`
  * Optimal Trade Entry (OTE 0.705): `0.9374`
  * Structural Invalidation Anchor (0.786): `0.9430`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9424` | `0.9427` | `0.9385` | `0.9388` | `331,954` | 312,152.44 USD | -118,372.59 USD | `-37.92%` | -5,238,961.86 USD | `-2.29` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.9388` | `0.9406` | `0.9379` | `0.9384` | `147,144` | 138,162.45 USD | -14,014.26 USD | `-10.14%` | -5,252,976.12 USD | `+0.10` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.9384` | `0.9384` | `0.9367` | `0.9378` | `95,637` | 89,665.98 USD | -32,920.10 USD | `-36.71%` | -5,285,896.22 USD | `-0.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9454` | `0.9486` | `0.9441` | `0.9482` | `389,813` | 368,731.69 USD | -12,790.97 USD | `-3.47%` | -4,989,682.40 USD | `+0.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.9481` | `0.9488` | `0.9422` | `0.9424` | `374,250` | 353,543.62 USD | -130,906.87 USD | `-37.03%` | -5,120,589.27 USD | `-0.90` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9424` | `0.9427` | `0.9367` | `0.9371` | `553,363` | 519,945.23 USD | -184,271.02 USD | `-35.44%` | -5,304,860.29 USD | `-1.37` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.9513` | `0.9534` | `0.9401` | `0.9521` | `2,460,195` | 2,328,628.99 USD | -255,772.99 USD | `-10.98%` | -4,766,418.33 USD | `-0.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9521` | `0.9556` | `0.9420` | `0.9454` | `1,900,301` | 1,804,294.23 USD | -93,285.41 USD | `-5.17%` | -4,859,703.74 USD | `+0.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.9454` | `0.9488` | `0.9367` | `0.9377` | `1,339,332` | 1,262,756.82 USD | -309,505.43 USD | `-24.51%` | -5,169,209.17 USD | `-0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,092,983.65 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9603` | `0.9263` | `0.9454` | `10,832,060` | 10,247,507.62 USD | -822,915.31 USD | `-8.03%` | -4,915,898.96 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9454` | `0.9488` | `0.9367` | `0.9371` | `1,317,426` | 1,242,220.54 USD | -327,968.86 USD | `-26.40%` | -5,243,867.82 USD | `+0.30` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -974,642.25 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,499,370.98 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,092,983.65 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9603` | `0.9263` | `0.9454` | `10,832,060` | 10,247,507.62 USD | -822,915.31 USD | `-8.03%` | -4,915,898.96 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9454` | `0.9488` | `0.9367` | `0.9371` | `1,317,426` | 1,242,220.54 USD | -327,968.86 USD | `-26.40%` | -5,243,867.82 USD | `+0.30` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`0.9355`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:22:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9829` | 6,513.94 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale BUY: 6.51K USD at 0.9829 USD [API] | `2026-10-29 09:17:13` |
| `ANNOUNCEMENT` | `INFO` | `0.9837` | 7,192.72 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale SELL: 7.19K USD at 0.9837 USD [API] | `2026-10-29 11:23:13` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.8866` (Vol: 283,500.00 USD, Dist: `--3.43%`)
  * 48H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.8871` (Vol: 412,800.00 USD, Dist: `--3.38%`)
  * 3D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.8871` (Vol: 412,800.00 USD, Dist: `--3.38%`)
  * 7D Horizon: Short MP=`1.06` (Vol: 252,200.00 USD, Dist: `+15.33%`) | Long MP=`0.8862` (Vol: 283,500.00 USD, Dist: `--3.48%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2155` | 107.75 USD | 473,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3135` | 198.32 USD | 473,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3605` | 796.34 USD | 473,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4195` | 5,190.00 USD | 472,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4525` | 1,180.00 USD | 467,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4675` | 146.70 USD | 466,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4705` | 2,590.00 USD | 465,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5025` | 201.35 USD | 463,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5065` | 3,290.00 USD | 463,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 597.13 USD | 459,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5325` | 532.50 USD | 459,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5535` | 145.07 USD | 458,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 14,600.00 USD | 458,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 577.36 USD | 443,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5775` | 228.98 USD | 443,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 683.51 USD | 443,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 137.53 USD | 442,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6055` | 1,480.00 USD | 442,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6075` | 1,810.00 USD | 440,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 105.96 USD | 439,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 147.48 USD | 438,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6295` | 220.32 USD | 438,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 757.80 USD | 438,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 106.00 USD | 437,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 507.86 USD | 437,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 2,090.00 USD | 437,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 20,270.00 USD | 435,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 4,230.00 USD | 414,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 202.47 USD | 410,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6565` | 521.98 USD | 410,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 149.44 USD | 409,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 63,890.00 USD | 409,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6735` | 84,190.00 USD | 345,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 423.10 USD | 261,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 512.97 USD | 261,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6915` | 19,800.00 USD | 260,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 322.62 USD | 240,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7005` | 1,140.00 USD | 240,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7025` | 156.94 USD | 239,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 988.87 USD | 239,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7215` | 1,580.00 USD | 238,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 397.93 USD | 236,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7295` | 291.58 USD | 236,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 2,300.00 USD | 236,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,140.00 USD | 233,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 283.30 USD | 232,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7515` | 32,890.00 USD | 232,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 2,220.00 USD | 199,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 1,140.00 USD | 197,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 144.07 USD | 196,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7565` | 8,860.00 USD | 195,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7595` | 53,930.00 USD | 187,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7635` | 308.00 USD | 133,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7705` | 152.94 USD | 132,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 3,840.00 USD | 132,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7730` | 3,130,000.00 USD | 3,130,000.00 USD | 9,740.00 USD | 39.63 USD | 2,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7750` | 3,120,000.00 USD | 3,120,000.00 USD | 698.40 USD | 0.00 USD | 3,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7775` | 2,490.00 USD | 128,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7790` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 3,100.00 USD | 53.43 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7810` | 3,110,000.00 USD | 3,110,000.00 USD | 436.65 USD | 25.30 USD | 1,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7830` | 3,110,000.00 USD | 3,110,000.00 USD | 114.15 USD | 1,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7850` | 3,100,000.00 USD | 3,100,000.00 USD | 112.95 USD | 2,340.00 USD | 180.30 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7865` | 156.51 USD | 126,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7870` | 3,100,000.00 USD | 3,100,000.00 USD | 5,690.00 USD | 3,090.00 USD | 450.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7890` | 3,090,000.00 USD | 3,090,000.00 USD | 88.75 USD | 0.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 277.39 USD | 126,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7910` | 3,090,000.00 USD | 3,090,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7930` | 3,070,000.00 USD | 3,070,000.00 USD | 20,360.00 USD | 1,560.00 USD | 6,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7935` | 1,760.00 USD | 125,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7950` | 3,040,000.00 USD | 3,040,000.00 USD | 3,290.00 USD | 8,430.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7970` | 3,010,000.00 USD | 3,010,000.00 USD | 10,100.00 USD | 1,130.00 USD | 522.30 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7985` | 210.40 USD | 124,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7990` | 3,000,000.00 USD | 3,000,000.00 USD | 20,360.00 USD | 6,180.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8010` | 2,960,000.00 USD | 2,960,000.00 USD | 5,420.00 USD | 5,300.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8030` | 2,950,000.00 USD | 2,950,000.00 USD | 4,550.00 USD | 2,440.00 USD | 10,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8050` | 2,930,000.00 USD | 2,930,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8070` | 2,910,000.00 USD | 2,910,000.00 USD | 12,160.00 USD | 4,660.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8090` | 2,870,000.00 USD | 2,870,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8110` | 2,870,000.00 USD | 2,870,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8130` | 2,860,000.00 USD | 2,860,000.00 USD | 14,060.00 USD | 2,970.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 123,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8150` | 2,830,000.00 USD | 2,830,000.00 USD | 61,120.00 USD | 7,590.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8170` | 2,740,000.00 USD | 2,740,000.00 USD | 10,780.00 USD | 8,770.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8190` | 2,710,000.00 USD | 2,710,000.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8210` | 2,700,000.00 USD | 2,700,000.00 USD | 7,510.00 USD | 3,290.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 123,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8230` | 2,680,000.00 USD | 2,680,000.00 USD | 29,430.00 USD | 5,100.00 USD | 13,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 749.96 USD | 121,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8250` | 2,630,000.00 USD | 2,630,000.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 2,620,000.00 USD | 2,620,000.00 USD | 4,320.00 USD | 5,770.00 USD | 616.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8290` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8310` | 2,600,000.00 USD | 2,600,000.00 USD | 9,280.00 USD | 1,660.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8330` | 2,590,000.00 USD | 2,590,000.00 USD | 16,220.00 USD | 11,360.00 USD | 77.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8350` | 2,560,000.00 USD | 2,560,000.00 USD | 19,490.00 USD | 0.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 120,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8370` | 2,540,000.00 USD | 2,540,000.00 USD | 15,240.00 USD | 1,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8390` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8410` | 2,510,000.00 USD | 2,510,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,570.00 USD | 120,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8430` | 2,420,000.00 USD | 2,420,000.00 USD | 1,590.00 USD | 4,840.00 USD | 933.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8430` | 2,510,000.00 USD | 2,510,000.00 USD | 11,320.00 USD | 3,840.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8450` | 2,410,000.00 USD | 2,410,000.00 USD | 2,360.00 USD | 7,850.00 USD | 429.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8450` | 2,490,000.00 USD | 2,490,000.00 USD | 1,980.00 USD | 404.64 USD | 474.61 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8470` | 2,400,000.00 USD | 2,400,000.00 USD | 24,110.00 USD | 1,110.00 USD | 165.77 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8470` | 2,490,000.00 USD | 2,490,000.00 USD | 7,900.00 USD | 1,730.00 USD | 2,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8490` | 2,380,000.00 USD | 2,380,000.00 USD | 5,120.00 USD | 2,400.00 USD | 7,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8490` | 2,480,000.00 USD | 2,480,000.00 USD | 22,370.00 USD | 9,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 118,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8510` | 2,360,000.00 USD | 2,360,000.00 USD | 13,560.00 USD | 4,140.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 2,450,000.00 USD | 2,450,000.00 USD | 14,280.00 USD | 991.53 USD | 21,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8530` | 2,330,000.00 USD | 2,330,000.00 USD | 4,680.00 USD | 3,830.00 USD | 5,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 2,410,000.00 USD | 2,410,000.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8550` | 2,310,000.00 USD | 2,310,000.00 USD | 18,270.00 USD | 3,040.00 USD | 5,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 2,400,000.00 USD | 2,400,000.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8570` | 2,290,000.00 USD | 2,290,000.00 USD | 989.11 USD | 1,720.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8570` | 2,400,000.00 USD | 2,400,000.00 USD | 3,540.00 USD | 944.22 USD | 8,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 117,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8590` | 2,280,000.00 USD | 2,280,000.00 USD | 6,870.00 USD | 10,640.00 USD | 6,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8590` | 2,390,000.00 USD | 2,390,000.00 USD | 3,730.00 USD | 0.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8610` | 2,260,000.00 USD | 2,260,000.00 USD | 8,320.00 USD | 855.53 USD | 16,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8610` | 2,380,000.00 USD | 2,380,000.00 USD | 9,960.00 USD | 3,660.00 USD | 35,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8630` | 2,230,000.00 USD | 2,230,000.00 USD | 39,330.00 USD | 12,290.00 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8630` | 2,330,000.00 USD | 2,330,000.00 USD | 758.91 USD | 2,910.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 389.61 USD | 116,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 116,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8650` | 2,180,000.00 USD | 2,180,000.00 USD | 17,640.00 USD | 2,110.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8650` | 2,330,000.00 USD | 2,330,000.00 USD | 47,860.00 USD | 18,930.00 USD | 184.85 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,390.00 USD | 116,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8670` | 2,150,000.00 USD | 2,150,000.00 USD | 11,890.00 USD | 10,090.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8670` | 2,260,000.00 USD | 2,260,000.00 USD | 13,660.00 USD | 3,720.00 USD | 12,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8690` | 2,130,000.00 USD | 2,130,000.00 USD | 41,960.00 USD | 3,780.00 USD | 29,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8690` | 2,230,000.00 USD | 2,230,000.00 USD | 160,750.00 USD | 13,110.00 USD | 46,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 12,590.00 USD | 114,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8705` | 92,480.00 USD | 102,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8710` | 2,060,000.00 USD | 2,060,000.00 USD | 42,250.00 USD | 24,870.00 USD | 28,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8710` | 2,010,000.00 USD | 2,010,000.00 USD | 7,370.00 USD | 23,340.00 USD | 13,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8730` | 1,960,000.00 USD | 1,960,000.00 USD | 54,380.00 USD | 21,510.00 USD | 25,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 8,170.00 USD | 295.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8750` | 1,860,000.00 USD | 1,860,000.00 USD | 36,600.00 USD | 6,900.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 6,380.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 9,560.00 USD | 9,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8770` | 1,800,000.00 USD | 1,800,000.00 USD | 10,480.00 USD | 154.89 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8770` | 1,940,000.00 USD | 1,940,000.00 USD | 1,390.00 USD | 0.00 USD | 30,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8790` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 40.93 USD | 50,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 1,910,000.00 USD | 1,910,000.00 USD | 873.30 USD | 5,580.00 USD | 53,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8810` | 1,740,000.00 USD | 1,740,000.00 USD | 13,820.00 USD | 5,210.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 1,850,000.00 USD | 1,850,000.00 USD | 1,830.00 USD | 240.78 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8830` | 1,710,000.00 USD | 1,710,000.00 USD | 521.60 USD | 5,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8830` | 1,850,000.00 USD | 1,850,000.00 USD | 2,320.00 USD | 10,140.00 USD | 11,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8850` | 1,710,000.00 USD | 1,710,000.00 USD | 5,580.00 USD | 35,520.00 USD | 11,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8850` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 5,800.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8870` | 1,650,000.00 USD | 1,650,000.00 USD | 68,710.00 USD | 18,450.00 USD | 32,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8870` | 1,810,000.00 USD | 1,810,000.00 USD | 271,870.00 USD | 22,320.00 USD | 81,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8890` | 1,530,000.00 USD | 1,530,000.00 USD | 69,440.00 USD | 40,830.00 USD | 4,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8890` | 1,440,000.00 USD | 1,440,000.00 USD | 54,380.00 USD | 73,890.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8910` | 1,420,000.00 USD | 1,420,000.00 USD | 2,150.00 USD | 38,730.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8910` | 1,300,000.00 USD | 1,300,000.00 USD | 75,300.00 USD | 22,240.00 USD | 34,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8930` | 1,360,000.00 USD | 1,360,000.00 USD | 56,810.00 USD | 24,630.00 USD | 37,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8930` | 1,160,000.00 USD | 1,160,000.00 USD | 62,870.00 USD | 23,560.00 USD | 9,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8950` | 1,240,000.00 USD | 1,240,000.00 USD | 4,110.00 USD | 15,420.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8950` | 1,070,000.00 USD | 1,070,000.00 USD | 7,120.00 USD | 37,670.00 USD | 57,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8970` | 1,210,000.00 USD | 1,210,000.00 USD | 4,620.00 USD | 24,510.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8970` | 966,680.00 USD | 966,680.00 USD | 2,140.00 USD | 4,820.00 USD | 56,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8990` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 15,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8990` | 903,390.00 USD | 903,390.00 USD | 0.00 USD | 34,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9005` | 152.27 USD | 152.27 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9010` | 1,150,000.00 USD | 1,150,000.00 USD | 1,970.00 USD | 24,600.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9010` | 869,170.00 USD | 869,170.00 USD | 0.00 USD | 48,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9030` | 1,120,000.00 USD | 1,120,000.00 USD | 8,980.00 USD | 17,560.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9030` | 820,330.00 USD | 820,330.00 USD | 0.00 USD | 16,370.00 USD | 23,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9050` | 1,080,000.00 USD | 1,080,000.00 USD | 19,330.00 USD | 11,600.00 USD | 22,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9050` | 780,030.00 USD | 780,030.00 USD | 0.00 USD | 3,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9070` | 1,030,000.00 USD | 1,030,000.00 USD | 36,650.00 USD | 8,370.00 USD | 33,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9070` | 776,190.00 USD | 776,190.00 USD | 23,910.00 USD | 0.00 USD | 42,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9090` | 947,220.00 USD | 947,220.00 USD | 7,100.00 USD | 9,080.00 USD | 176.94 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9110` | 930,870.00 USD | 930,870.00 USD | 25,560.00 USD | 2,850.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9130` | 900,380.00 USD | 900,380.00 USD | 11,890.00 USD | 9,480.00 USD | 17,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9130` | 710,240.00 USD | 710,240.00 USD | 0.00 USD | 0.00 USD | 20,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9150` | 861,680.00 USD | 861,680.00 USD | 3,760.00 USD | 9,920.00 USD | 18,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9150` | 689,520.00 USD | 689,520.00 USD | 0.00 USD | 515.41 USD | 15,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9170` | 829,120.00 USD | 829,120.00 USD | 0.00 USD | 79.80 USD | 6,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9170` | 673,320.00 USD | 673,320.00 USD | 0.00 USD | 0.00 USD | 33,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9190` | 822,380.00 USD | 822,380.00 USD | 2,860.00 USD | 7,530.00 USD | 7,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9210` | 804,650.00 USD | 804,650.00 USD | 12,850.00 USD | 3,680.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9210` | 640,140.00 USD | 640,140.00 USD | 0.00 USD | 7,760.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9230` | 782,090.00 USD | 782,090.00 USD | 6,600.00 USD | 7,140.00 USD | 21,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9230` | 628,410.00 USD | 628,410.00 USD | 294,370.00 USD | 0.00 USD | 26,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9250` | 746,650.00 USD | 746,650.00 USD | 99,970.00 USD | 63,270.00 USD | 62,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9250` | 307,360.00 USD | 307,360.00 USD | 0.00 USD | 52,780.00 USD | 84,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9270` | 520,880.00 USD | 520,880.00 USD | 39,920.00 USD | 7,040.00 USD | 73,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9270` | 170,510.00 USD | 170,510.00 USD | 44,020.00 USD | 11,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9290` | 400,110.00 USD | 400,110.00 USD | 80,950.00 USD | 20,440.00 USD | 38,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9290` | 114,690.00 USD | 114,690.00 USD | 0.00 USD | 12,750.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9310` | 260,150.00 USD | 260,150.00 USD | 0.00 USD | 7,130.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9330` | 247,620.00 USD | 247,620.00 USD | 11,160.00 USD | 23,770.00 USD | 42,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9330` | 100,340.00 USD | 100,340.00 USD | 37,450.00 USD | 0.00 USD | 31,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9350` | 170,250.00 USD | 170,250.00 USD | 121,410.00 USD | 21,200.00 USD | 27,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9350` | 31,530.00 USD | 31,530.00 USD | 0.00 USD | 11,160.00 USD | 20,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9370` | 76,090.00 USD | 76,090.00 USD | 18,250.00 USD | 39,710.00 USD | 18,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9370` | 152,180.00 USD | 152,180.00 USD | 18,250.00 USD | 39,710.00 USD | 18,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9370` | 84,400.00 USD | 84,400.00 USD | 16,340.00 USD | 19,540.00 USD | 48,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9370` | 168,800.00 USD | 168,800.00 USD | 16,340.00 USD | 19,540.00 USD | 48,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9390` | 153,830.00 USD | 153,830.00 USD | 1,340.00 USD | 309.30 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9390` | 242,960.00 USD | 242,960.00 USD | 39,250.00 USD | 0.00 USD | 34,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9410` | 154,750.00 USD | 154,750.00 USD | 673.54 USD | 239.40 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9410` | 406,010.00 USD | 406,010.00 USD | 161,930.00 USD | 1,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9430` | 156,210.00 USD | 156,210.00 USD | 1,230.00 USD | 224.96 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 430,300.00 USD | 430,300.00 USD | 0.00 USD | 20,890.00 USD | 3,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9470` | 156,660.00 USD | 156,660.00 USD | 0.00 USD | 199.60 USD | 256.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 516,810.00 USD | 516,810.00 USD | 3,540.00 USD | 6,380.00 USD | 76,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9490` | 238,550.00 USD | 238,550.00 USD | 81,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 600,740.00 USD | 600,740.00 USD | 2,770.00 USD | 10,340.00 USD | 70,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9510` | 239,360.00 USD | 239,360.00 USD | 0.00 USD | 813.18 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 892,140.00 USD | 892,140.00 USD | 258,650.00 USD | 28,180.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9530` | 239,980.00 USD | 239,980.00 USD | 0.00 USD | 623.88 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 900,370.00 USD | 900,370.00 USD | 0.00 USD | 8,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9550` | 280,660.00 USD | 280,660.00 USD | 18,000.00 USD | 22,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 920,110.00 USD | 920,110.00 USD | 0.00 USD | 19,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9570` | 292,830.00 USD | 292,830.00 USD | 6,640.00 USD | 5,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 933,270.00 USD | 933,270.00 USD | 1,910.00 USD | 10,300.00 USD | 957.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9590` | 314,510.00 USD | 314,510.00 USD | 14,060.00 USD | 3,680.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 954,340.00 USD | 954,340.00 USD | 1,980.00 USD | 18,220.00 USD | 866.69 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9610` | 371,760.00 USD | 371,760.00 USD | 14,760.00 USD | 11,950.00 USD | 30,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9610` | 979,720.00 USD | 979,720.00 USD | 24,370.00 USD | 0.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9630` | 550,030.00 USD | 550,030.00 USD | 102,030.00 USD | 30,630.00 USD | 45,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 1,150,000.00 USD | 1,150,000.00 USD | 56,160.00 USD | 31,820.00 USD | 84,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9650` | 691,380.00 USD | 691,380.00 USD | 29,080.00 USD | 33,020.00 USD | 79,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 1,260,000.00 USD | 1,260,000.00 USD | 97,600.00 USD | 0.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9670` | 787,810.00 USD | 787,810.00 USD | 53,970.00 USD | 16,730.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9670` | 1,310,000.00 USD | 1,310,000.00 USD | 40,070.00 USD | 5,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9690` | 824,050.00 USD | 824,050.00 USD | 12,270.00 USD | 14,610.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 21,100.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9710` | 926,870.00 USD | 926,870.00 USD | 11,360.00 USD | 15,190.00 USD | 76,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 18,250.00 USD | 31,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9730` | 1,010,000.00 USD | 1,010,000.00 USD | 44,370.00 USD | 6,610.00 USD | 36,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 1,450,000.00 USD | 1,450,000.00 USD | 2,910.00 USD | 9,290.00 USD | 27,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9750` | 1,090,000.00 USD | 1,090,000.00 USD | 25,990.00 USD | 17,610.00 USD | 31,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 1,520,000.00 USD | 1,520,000.00 USD | 2,090.00 USD | 17,230.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9770` | 1,190,000.00 USD | 1,190,000.00 USD | 78,840.00 USD | 14,700.00 USD | 11,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 1,620,000.00 USD | 1,620,000.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9790` | 1,270,000.00 USD | 1,270,000.00 USD | 36,540.00 USD | 11,310.00 USD | 26,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 3,880.00 USD | 85,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9810` | 1,320,000.00 USD | 1,320,000.00 USD | 16,990.00 USD | 6,570.00 USD | 28,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9810` | 1,830,000.00 USD | 1,830,000.00 USD | 540.00 USD | 4,020.00 USD | 119,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9830` | 1,440,000.00 USD | 1,440,000.00 USD | 33,180.00 USD | 27,220.00 USD | 55,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 2,060,000.00 USD | 2,060,000.00 USD | 124,720.00 USD | 15,810.00 USD | 94,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9850` | 1,510,000.00 USD | 1,510,000.00 USD | 46,690.00 USD | 8,800.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 211.77 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9870` | 1,550,000.00 USD | 1,550,000.00 USD | 14,650.00 USD | 6,470.00 USD | 22,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 2,200,000.00 USD | 2,200,000.00 USD | 40,020.00 USD | 0.00 USD | 67,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9890` | 1,620,000.00 USD | 1,620,000.00 USD | 27,890.00 USD | 3,780.00 USD | 30,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9890` | 2,220,000.00 USD | 2,220,000.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9910` | 1,730,000.00 USD | 1,730,000.00 USD | 60,020.00 USD | 5,890.00 USD | 45,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9910` | 2,260,000.00 USD | 2,260,000.00 USD | 3,700.00 USD | 800.44 USD | 35,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9930` | 1,760,000.00 USD | 1,760,000.00 USD | 16,270.00 USD | 7,030.00 USD | 8,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9930` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 36,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9950` | 1,800,000.00 USD | 1,800,000.00 USD | 29,210.00 USD | 2,120.00 USD | 7,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9950` | 2,420,000.00 USD | 2,420,000.00 USD | 63,060.00 USD | 5,380.00 USD | 58,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9970` | 1,860,000.00 USD | 1,860,000.00 USD | 46,950.00 USD | 1,840.00 USD | 13,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 2,520,000.00 USD | 2,520,000.00 USD | 95,130.00 USD | 253.35 USD | 4,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9985` | 852.22 USD | 1,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9990` | 1,920,000.00 USD | 1,920,000.00 USD | 35,220.00 USD | 17,910.00 USD | 10,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 6,490.00 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,990,000.00 USD | 1,990,000.00 USD | 44,580.00 USD | 10,790.00 USD | 13,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,580,000.00 USD | 2,580,000.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,020,000.00 USD | 2,020,000.00 USD | 12,370.00 USD | 9,310.00 USD | 6,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,730,000.00 USD | 2,730,000.00 USD | 107,670.00 USD | 21,850.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,090,000.00 USD | 2,090,000.00 USD | 54,780.00 USD | 5,520.00 USD | 5,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,780,000.00 USD | 2,780,000.00 USD | 32,430.00 USD | 3,970.00 USD | 12,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 4,000.00 USD | 5,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,200,000.00 USD | 2,200,000.00 USD | 50,600.00 USD | 11,770.00 USD | 47,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,840,000.00 USD | 2,840,000.00 USD | 35,710.00 USD | 240.78 USD | 29,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,250,000.00 USD | 2,250,000.00 USD | 30,870.00 USD | 13,790.00 USD | 7,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,870,000.00 USD | 2,870,000.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,280,000.00 USD | 2,280,000.00 USD | 9,660.00 USD | 23,460.00 USD | 265.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,900,000.00 USD | 2,900,000.00 USD | 20,090.00 USD | 17,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,300,000.00 USD | 2,300,000.00 USD | 10,450.00 USD | 1,540.00 USD | 3,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,960,000.00 USD | 2,960,000.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,350,000.00 USD | 2,350,000.00 USD | 14,310.00 USD | 23,780.00 USD | 14,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 26,510.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,370,000.00 USD | 2,370,000.00 USD | 3,990.00 USD | 3,840.00 USD | 16,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,040,000.00 USD | 3,040,000.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,450,000.00 USD | 2,450,000.00 USD | 55,630.00 USD | 4,860.00 USD | 10,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,150,000.00 USD | 3,150,000.00 USD | 17,960.00 USD | 83,360.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,500,000.00 USD | 2,500,000.00 USD | 19,220.00 USD | 9,450.00 USD | 21,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,310,000.00 USD | 3,310,000.00 USD | 61,450.00 USD | 32,840.00 USD | 68,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,590,000.00 USD | 2,590,000.00 USD | 44,780.00 USD | 18,890.00 USD | 34,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,630,000.00 USD | 3,630,000.00 USD | 82,230.00 USD | 86,210.00 USD | 146,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,680,000.00 USD | 2,680,000.00 USD | 44,190.00 USD | 12,640.00 USD | 27,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,740,000.00 USD | 3,740,000.00 USD | 28,320.00 USD | 48,490.00 USD | 37,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,710,000.00 USD | 2,710,000.00 USD | 15,560.00 USD | 10,270.00 USD | 7,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,060,000.00 USD | 4,060,000.00 USD | 161,070.00 USD | 127,000.00 USD | 25,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,770,000.00 USD | 2,770,000.00 USD | 18,290.00 USD | 18,890.00 USD | 25,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,270,000.00 USD | 4,270,000.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,890,000.00 USD | 2,890,000.00 USD | 75,080.00 USD | 9,640.00 USD | 31,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,470,000.00 USD | 4,470,000.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,930,000.00 USD | 2,930,000.00 USD | 17,370.00 USD | 1,590.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,600,000.00 USD | 4,600,000.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,960,000.00 USD | 2,960,000.00 USD | 11,120.00 USD | 18,040.00 USD | 7,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,910,000.00 USD | 4,910,000.00 USD | 259,060.00 USD | 8,290.00 USD | 43,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,020,000.00 USD | 3,020,000.00 USD | 42,410.00 USD | 3,800.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,210,000.00 USD | 5,210,000.00 USD | 193,150.00 USD | 3,330.00 USD | 109,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,040,000.00 USD | 3,040,000.00 USD | 7,640.00 USD | 5,430.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,600,000.00 USD | 5,600,000.00 USD | 239,580.00 USD | 9,010.00 USD | 134,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,060,000.00 USD | 3,060,000.00 USD | 7,100.00 USD | 2,540.00 USD | 13,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,040,000.00 USD | 6,040,000.00 USD | 285,690.00 USD | 2,090.00 USD | 159,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,090,000.00 USD | 3,090,000.00 USD | 14,210.00 USD | 8,400.00 USD | 8,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,240,000.00 USD | 6,240,000.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,100,000.00 USD | 3,100,000.00 USD | 1,340.00 USD | 638.69 USD | 6,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,510,000.00 USD | 6,510,000.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,120,000.00 USD | 3,120,000.00 USD | 7,650.00 USD | 5,890.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,030,000.00 USD | 7,030,000.00 USD | 178,890.00 USD | 96,370.00 USD | 244,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 367.04 USD | 5,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,140,000.00 USD | 3,140,000.00 USD | 4,940.00 USD | 4,010.00 USD | 10,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,230,000.00 USD | 7,230,000.00 USD | 116,030.00 USD | 13,780.00 USD | 77,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,180,000.00 USD | 3,180,000.00 USD | 29,800.00 USD | 73.09 USD | 13,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,550,000.00 USD | 7,550,000.00 USD | 175,350.00 USD | 43,690.00 USD | 96,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,200,000.00 USD | 3,200,000.00 USD | 4,370.00 USD | 937.66 USD | 6,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,750,000.00 USD | 7,750,000.00 USD | 68,010.00 USD | 58,070.00 USD | 74,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,980,000.00 USD | 7,980,000.00 USD | 121,450.00 USD | 33,860.00 USD | 72,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,370,000.00 USD | 8,370,000.00 USD | 218,860.00 USD | 70,160.00 USD | 106,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,830,000.00 USD | 8,830,000.00 USD | 239,650.00 USD | 74,380.00 USD | 145,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,110,000.00 USD | 9,110,000.00 USD | 138,520.00 USD | 56,310.00 USD | 78,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,390,000.00 USD | 9,390,000.00 USD | 140,500.00 USD | 73,690.00 USD | 71,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,590,000.00 USD | 9,590,000.00 USD | 74,870.00 USD | 27,820.00 USD | 91,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 9,670,000.00 USD | 9,670,000.00 USD | 60,290.00 USD | 26,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.08` | 2,230.00 USD | 7,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.11` | 170.02 USD | 7,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.15` | 14,340.00 USD | 22,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 11,730.00 USD | 33,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 239.77 USD | 34,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.38` | 3,900.00 USD | 37,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,200.00 USD | 41,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 120.80 USD | 41,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 176.31 USD | 41,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 1,810.00 USD | 43,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 794.80 USD | 44,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.63` | 2,440.00 USD | 46,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.63` | 238.40 USD | 46,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 8,240.00 USD | 54,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 319.42 USD | 55,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 300.15 USD | 55,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 190.42 USD | 55,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 13,140.00 USD | 68,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 380.81 USD | 69,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 89,290.00 USD | 158,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 208.37 USD | 158,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 24,060.00 USD | 182,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2155` | 473,550.00 USD | 0.00 USD | 107.75 USD | `-77.22%` | `500.00` |
| `Live` | `Long` | `0.3135` | 473,440.00 USD | 0.00 USD | 198.32 USD | `-66.86%` | `632.60` |
| `Live` | `Long` | `0.3605` | 473,240.00 USD | 0.00 USD | 796.34 USD | `-61.90%` | `2,209.00` |
| `Live` | `Long` | `0.4195` | 472,440.00 USD | 0.00 USD | 5,190.00 USD | `-55.66%` | `12,374.00` |
| `Live` | `Long` | `0.4525` | 467,250.00 USD | 0.00 USD | 1,180.00 USD | `-52.17%` | `2,618.10` |
| `Live` | `Long` | `0.4675` | 466,070.00 USD | 0.00 USD | 146.70 USD | `-50.59%` | `313.80` |
| `Live` | `Long` | `0.4705` | 465,920.00 USD | 0.00 USD | 2,590.00 USD | `-50.27%` | `5,500.00` |
| `Live` | `Long` | `0.5025` | 463,330.00 USD | 0.00 USD | 201.35 USD | `-46.89%` | `400.70` |
| `Live` | `Long` | `0.5065` | 463,130.00 USD | 0.00 USD | 3,290.00 USD | `-46.47%` | `6,504.70` |
| `Live` | `Long` | `0.5085` | 459,840.00 USD | 0.00 USD | 597.13 USD | `-46.25%` | `1,174.30` |
| `Live` | `Long` | `0.5325` | 459,240.00 USD | 0.00 USD | 532.50 USD | `-43.72%` | `1,000.00` |
| `Live` | `Long` | `0.5535` | 458,710.00 USD | 0.00 USD | 145.07 USD | `-41.50%` | `262.10` |
| `Live` | `Long` | `0.5655` | 458,560.00 USD | 0.00 USD | 14,600.00 USD | `-40.23%` | `25,816.60` |
| `Live` | `Long` | `0.5695` | 443,960.00 USD | 0.00 USD | 577.36 USD | `-39.81%` | `1,013.80` |
| `Live` | `Long` | `0.5775` | 443,390.00 USD | 0.00 USD | 228.98 USD | `-38.96%` | `396.50` |
| `Live` | `Long` | `0.5845` | 443,160.00 USD | 0.00 USD | 683.51 USD | `-38.22%` | `1,169.40` |
| `Live` | `Long` | `0.5895` | 442,470.00 USD | 0.00 USD | 137.53 USD | `-37.69%` | `233.30` |
| `Live` | `Long` | `0.6055` | 442,340.00 USD | 0.00 USD | 1,480.00 USD | `-36.00%` | `2,448.50` |
| `Live` | `Long` | `0.6075` | 440,850.00 USD | 0.00 USD | 1,810.00 USD | `-35.79%` | `2,971.80` |
| `Live` | `Long` | `0.6125` | 439,050.00 USD | 0.00 USD | 105.96 USD | `-35.26%` | `173.00` |
| `Live` | `Long` | `0.6145` | 438,940.00 USD | 0.00 USD | 147.48 USD | `-35.05%` | `240.00` |
| `Live` | `Long` | `0.6295` | 438,790.00 USD | 0.00 USD | 220.32 USD | `-33.47%` | `350.00` |
| `Live` | `Long` | `0.6315` | 438,570.00 USD | 0.00 USD | 757.80 USD | `-33.25%` | `1,200.00` |
| `Live` | `Long` | `0.6355` | 437,820.00 USD | 0.00 USD | 106.00 USD | `-32.83%` | `166.80` |
| `Live` | `Long` | `0.6365` | 437,710.00 USD | 0.00 USD | 507.86 USD | `-32.73%` | `797.90` |
| `Live` | `Long` | `0.6405` | 437,200.00 USD | 0.00 USD | 2,090.00 USD | `-32.30%` | `3,262.00` |
| `Live` | `Long` | `0.6415` | 435,110.00 USD | 0.00 USD | 20,270.00 USD | `-32.20%` | `31,595.60` |
| `Live` | `Long` | `0.6465` | 414,840.00 USD | 0.00 USD | 4,230.00 USD | `-31.67%` | `6,539.70` |
| `Live` | `Long` | `0.6475` | 410,620.00 USD | 0.00 USD | 202.47 USD | `-31.56%` | `312.70` |
| `Live` | `Long` | `0.6565` | 410,410.00 USD | 0.00 USD | 521.98 USD | `-30.61%` | `795.10` |
| `Live` | `Long` | `0.6595` | 409,890.00 USD | 0.00 USD | 149.44 USD | `-30.29%` | `226.60` |
| `Live` | `Long` | `0.6725` | 409,740.00 USD | 0.00 USD | 63,890.00 USD | `-28.92%` | `95,000.00` |
| `Live` | `Long` | `0.6735` | 345,860.00 USD | 0.00 USD | 84,190.00 USD | `-28.81%` | `125,000.00` |
| `Live` | `Long` | `0.6775` | 261,670.00 USD | 0.00 USD | 423.10 USD | `-28.39%` | `624.50` |
| `Live` | `Long` | `0.6835` | 261,240.00 USD | 0.00 USD | 512.97 USD | `-27.76%` | `750.50` |
| `Live` | `Long` | `0.6915` | 260,730.00 USD | 0.00 USD | 19,800.00 USD | `-26.91%` | `28,635.00` |
| `Live` | `Long` | `0.6965` | 240,930.00 USD | 0.00 USD | 322.62 USD | `-26.38%` | `463.20` |
| `Live` | `Long` | `0.7005` | 240,610.00 USD | 0.00 USD | 1,140.00 USD | `-25.96%` | `1,634.20` |
| `Live` | `Long` | `0.7025` | 239,460.00 USD | 0.00 USD | 156.94 USD | `-25.75%` | `223.40` |
| `Live` | `Long` | `0.7145` | 239,310.00 USD | 0.00 USD | 988.87 USD | `-24.48%` | `1,384.00` |
| `Live` | `Long` | `0.7215` | 238,320.00 USD | 0.00 USD | 1,580.00 USD | `-23.74%` | `2,190.90` |
| `Live` | `Long` | `0.7235` | 236,740.00 USD | 0.00 USD | 397.93 USD | `-23.53%` | `550.00` |
| `Live` | `Long` | `0.7295` | 236,340.00 USD | 0.00 USD | 291.58 USD | `-22.90%` | `399.70` |
| `Live` | `Long` | `0.7305` | 236,050.00 USD | 0.00 USD | 2,300.00 USD | `-22.79%` | `3,143.00` |
| `Live` | `Long` | `0.7335` | 233,750.00 USD | 0.00 USD | 1,140.00 USD | `-22.47%` | `1,557.80` |
| `Live` | `Long` | `0.7395` | 232,610.00 USD | 0.00 USD | 283.30 USD | `-21.84%` | `383.10` |
| `Live` | `Long` | `0.7515` | 232,330.00 USD | 0.00 USD | 32,890.00 USD | `-20.57%` | `43,766.90` |
| `Live` | `Long` | `0.7525` | 199,430.00 USD | 0.00 USD | 2,220.00 USD | `-20.46%` | `2,947.70` |
| `Live` | `Long` | `0.7535` | 197,220.00 USD | 0.00 USD | 1,140.00 USD | `-20.36%` | `1,516.30` |
| `Live` | `Long` | `0.7555` | 196,070.00 USD | 0.00 USD | 144.07 USD | `-20.15%` | `190.70` |
| `Live` | `Long` | `0.7565` | 195,930.00 USD | 0.00 USD | 8,860.00 USD | `-20.04%` | `11,712.10` |
| `Live` | `Long` | `0.7595` | 187,070.00 USD | 0.00 USD | 53,930.00 USD | `-19.72%` | `71,003.30` |
| `Live` | `Long` | `0.7635` | 133,140.00 USD | 0.00 USD | 308.00 USD | `-19.30%` | `403.40` |
| `Live` | `Long` | `0.7705` | 132,830.00 USD | 0.00 USD | 152.94 USD | `-18.56%` | `198.50` |
| `Live` | `Long` | `0.7725` | 132,680.00 USD | 0.00 USD | 3,840.00 USD | `-18.35%` | `4,968.90` |
| `Live` | `Long` | `0.7775` | 128,840.00 USD | 0.00 USD | 2,490.00 USD | `-17.82%` | `3,199.30` |
| `Live` | `Long` | `0.7865` | 126,360.00 USD | 0.00 USD | 156.51 USD | `-16.87%` | `199.00` |
| `Live` | `Long` | `0.7905` | 126,200.00 USD | 0.00 USD | 277.39 USD | `-16.45%` | `350.90` |
| `Live` | `Long` | `0.7935` | 125,920.00 USD | 0.00 USD | 1,760.00 USD | `-16.13%` | `2,214.10` |
| `Live` | `Long` | `0.7985` | 124,160.00 USD | 0.00 USD | 210.40 USD | `-15.60%` | `263.50` |
| `Live` | `Long` | `0.8135` | 123,950.00 USD | 0.00 USD | 647.79 USD | `-14.02%` | `796.30` |
| `Live` | `Long` | `0.8215` | 123,310.00 USD | 0.00 USD | 1,950.00 USD | `-13.17%` | `2,370.70` |
| `Live` | `Long` | `0.8235` | 121,360.00 USD | 0.00 USD | 749.96 USD | `-12.96%` | `910.70` |
| `Live` | `Long` | `0.8365` | 120,610.00 USD | 0.00 USD | 316.70 USD | `-11.59%` | `378.60` |
| `Live` | `Long` | `0.8415` | 120,290.00 USD | 0.00 USD | 1,570.00 USD | `-11.06%` | `1,862.40` |
| `Live` | `Long` | `0.8495` | 118,730.00 USD | 0.00 USD | 1,260.00 USD | `-10.21%` | `1,486.90` |
| `Live` | `Long` | `0.8575` | 117,460.00 USD | 0.00 USD | 620.32 USD | `-9.37%` | `723.40` |
| `Live` | `Long` | `0.8635` | 116,840.00 USD | 0.00 USD | 389.61 USD | `-8.73%` | `451.20` |
| `Live` | `Long` | `0.8645` | 116,450.00 USD | 0.00 USD | 438.30 USD | `-8.63%` | `507.00` |
| `Live` | `Long` | `0.8665` | 116,010.00 USD | 0.00 USD | 1,390.00 USD | `-8.42%` | `1,606.10` |
| `Live` | `Long` | `0.8695` | 114,620.00 USD | 0.00 USD | 12,590.00 USD | `-8.10%` | `14,478.80` |
| `Live` | `Long` | `0.8705` | 102,030.00 USD | 0.00 USD | 92,480.00 USD | `-7.99%` | `106,233.40` |
| `Live` | `Long` | `0.8765` | 9,560.00 USD | 0.00 USD | 9,560.00 USD | `-7.36%` | `10,903.10` |
| `Live` | `Short` | `0.9005` | 152.27 USD | 152.27 USD | 0.00 USD | `-4.82%` | `169.10` |
| `Live` | `Short` | `0.9985` | 1,000.00 USD | 852.22 USD | 0.00 USD | `+5.54%` | `853.50` |
| `Live` | `Short` | `1.01` | 5,000.00 USD | 4,000.00 USD | 0.00 USD | `+6.38%` | `3,970.40` |
| `Live` | `Short` | `1.05` | 5,370.00 USD | 367.04 USD | 0.00 USD | `+10.72%` | `350.40` |
| `Live` | `Short` | `1.08` | 7,600.00 USD | 2,230.00 USD | 0.00 USD | `+14.31%` | `2,064.20` |
| `Live` | `Short` | `1.11` | 7,770.00 USD | 170.02 USD | 0.00 USD | `+17.37%` | `153.10` |
| `Live` | `Short` | `1.15` | 22,110.00 USD | 14,340.00 USD | 0.00 USD | `+21.39%` | `12,482.50` |
| `Live` | `Short` | `1.32` | 33,840.00 USD | 11,730.00 USD | 0.00 USD | `+39.89%` | `8,862.90` |
| `Live` | `Short` | `1.34` | 34,080.00 USD | 239.77 USD | 0.00 USD | `+41.58%` | `179.00` |
| `Live` | `Short` | `1.38` | 37,980.00 USD | 3,900.00 USD | 0.00 USD | `+45.49%` | `2,834.10` |
| `Live` | `Short` | `1.42` | 41,170.00 USD | 3,200.00 USD | 0.00 USD | `+50.14%` | `2,249.30` |
| `Live` | `Short` | `1.52` | 41,290.00 USD | 120.80 USD | 0.00 USD | `+60.60%` | `79.50` |
| `Live` | `Short` | `1.54` | 41,470.00 USD | 176.31 USD | 0.00 USD | `+63.03%` | `114.30` |
| `Live` | `Short` | `1.56` | 43,280.00 USD | 1,810.00 USD | 0.00 USD | `+64.51%` | `1,161.90` |
| `Live` | `Short` | `1.59` | 44,070.00 USD | 794.80 USD | 0.00 USD | `+68.21%` | `499.40` |
| `Live` | `Short` | `1.63` | 46,510.00 USD | 2,440.00 USD | 0.00 USD | `+71.81%` | `1,500.00` |
| `Live` | `Short` | `1.63` | 46,750.00 USD | 238.40 USD | 0.00 USD | `+72.23%` | `146.30` |
| `Live` | `Short` | `1.65` | 54,990.00 USD | 8,240.00 USD | 0.00 USD | `+74.13%` | `5,000.00` |
| `Live` | `Short` | `1.66` | 55,310.00 USD | 319.42 USD | 0.00 USD | `+75.93%` | `191.90` |
| `Live` | `Short` | `1.67` | 55,610.00 USD | 300.15 USD | 0.00 USD | `+76.25%` | `180.00` |
| `Live` | `Short` | `1.73` | 55,800.00 USD | 190.42 USD | 0.00 USD | `+82.80%` | `110.10` |
| `Live` | `Short` | `1.74` | 68,940.00 USD | 13,140.00 USD | 0.00 USD | `+83.54%` | `7,569.10` |
| `Live` | `Short` | `1.77` | 69,320.00 USD | 380.81 USD | 0.00 USD | `+87.56%` | `214.60` |
| `Live` | `Short` | `1.79` | 158,620.00 USD | 89,290.00 USD | 0.00 USD | `+89.67%` | `49,759.80` |
| `Live` | `Short` | `1.86` | 158,820.00 USD | 208.37 USD | 0.00 USD | `+96.12%` | `112.30` |
| `Live` | `Short` | `1.86` | 182,880.00 USD | 24,060.00 USD | 0.00 USD | `+96.86%` | `12,916.90` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.4015` | 397,600.00 USD | 0.00 USD | 120.45 USD | `-57.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 397,480.00 USD | 0.00 USD | 150.15 USD | `-47.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5435` | 397,330.00 USD | 0.00 USD | 186.15 USD | `-42.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 397,150.00 USD | 0.00 USD | 1,150.00 USD | `-30.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 396,000.00 USD | 0.00 USD | 781.90 USD | `-25.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 395,210.00 USD | 0.00 USD | 477.38 USD | `-24.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 394,740.00 USD | 0.00 USD | 341.33 USD | `-23.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 394,400.00 USD | 0.00 USD | 972.82 USD | `-23.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 393,420.00 USD | 0.00 USD | 160.20 USD | `-22.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7385` | 393,260.00 USD | 0.00 USD | 102.58 USD | `-21.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 393,160.00 USD | 0.00 USD | 289.49 USD | `-21.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7615` | 392,870.00 USD | 0.00 USD | 197.53 USD | `-19.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 392,670.00 USD | 0.00 USD | 14,570.00 USD | `-17.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 378,110.00 USD | 0.00 USD | 213.58 USD | `-16.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 377,890.00 USD | 0.00 USD | 274,830.00 USD | `-15.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 103,060.00 USD | 0.00 USD | 108.47 USD | `-15.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8025` | 102,950.00 USD | 0.00 USD | 2,010.00 USD | `-15.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 100,940.00 USD | 0.00 USD | 326.96 USD | `-14.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 100,610.00 USD | 0.00 USD | 405.75 USD | `-14.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 100,210.00 USD | 0.00 USD | 772.84 USD | `-11.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8415` | 99,430.00 USD | 0.00 USD | 2,670.00 USD | `-11.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8495` | 96,760.00 USD | 0.00 USD | 3,470.00 USD | `-10.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 93,290.00 USD | 0.00 USD | 9,180.00 USD | `-10.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 84,110.00 USD | 0.00 USD | 341.94 USD | `-9.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 83,770.00 USD | 0.00 USD | 1,150.00 USD | `-9.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 82,620.00 USD | 0.00 USD | 429.25 USD | `-9.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 82,190.00 USD | 0.00 USD | 223.30 USD | `-9.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 81,970.00 USD | 0.00 USD | 518.51 USD | `-8.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 81,450.00 USD | 0.00 USD | 128.39 USD | `-8.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 81,320.00 USD | 0.00 USD | 1,280.00 USD | `-7.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 80,040.00 USD | 0.00 USD | 205.24 USD | `-7.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 79,840.00 USD | 0.00 USD | 649.66 USD | `-7.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 79,190.00 USD | 0.00 USD | 194.06 USD | `-6.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8845` | 78,990.00 USD | 0.00 USD | 193.35 USD | `-6.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 78,800.00 USD | 0.00 USD | 223.04 USD | `-6.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 78,580.00 USD | 0.00 USD | 10,840.00 USD | `-6.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 67,730.00 USD | 0.00 USD | 4,920.00 USD | `-5.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8915` | 62,820.00 USD | 0.00 USD | 121.15 USD | `-5.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 62,700.00 USD | 0.00 USD | 192.07 USD | `-5.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 62,500.00 USD | 0.00 USD | 195.32 USD | `-5.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8965` | 62,310.00 USD | 0.00 USD | 196.87 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8985` | 62,110.00 USD | 0.00 USD | 2,870.00 USD | `-5.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9005` | 59,240.00 USD | 0.00 USD | 319.05 USD | `-4.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9025` | 58,920.00 USD | 0.00 USD | 398.91 USD | `-4.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9035` | 58,520.00 USD | 0.00 USD | 196.96 USD | `-4.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9045` | 58,320.00 USD | 0.00 USD | 300.38 USD | `-4.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9065` | 58,020.00 USD | 0.00 USD | 198.61 USD | `-4.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9075` | 57,820.00 USD | 0.00 USD | 994.35 USD | `-4.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 56,830.00 USD | 0.00 USD | 363.40 USD | `-3.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9095` | 56,470.00 USD | 0.00 USD | 1,810.00 USD | `-3.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9115` | 54,660.00 USD | 0.00 USD | 397.23 USD | `-3.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9135` | 54,260.00 USD | 0.00 USD | 398.65 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9145` | 53,860.00 USD | 0.00 USD | 399.09 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9155` | 53,460.00 USD | 0.00 USD | 403.92 USD | `-3.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9165` | 53,060.00 USD | 0.00 USD | 198.06 USD | `-3.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9175` | 52,860.00 USD | 0.00 USD | 223.78 USD | `-3.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9185` | 52,640.00 USD | 0.00 USD | 899.85 USD | `-2.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9195` | 51,740.00 USD | 0.00 USD | 900.19 USD | `-2.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 50,840.00 USD | 0.00 USD | 2,920.00 USD | `-2.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9215` | 47,920.00 USD | 0.00 USD | 104.68 USD | `-2.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9225` | 47,810.00 USD | 0.00 USD | 201.94 USD | `-2.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9235` | 47,610.00 USD | 0.00 USD | 1,080.00 USD | `-2.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9245` | 46,520.00 USD | 0.00 USD | 201.45 USD | `-2.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9255` | 46,320.00 USD | 0.00 USD | 817.40 USD | `-2.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9265` | 45,510.00 USD | 0.00 USD | 403.77 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9275` | 45,100.00 USD | 0.00 USD | 2,120.00 USD | `-1.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9285` | 42,980.00 USD | 0.00 USD | 246.05 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9295` | 42,740.00 USD | 0.00 USD | 407.49 USD | `-1.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9305` | 42,330.00 USD | 0.00 USD | 203.97 USD | `-1.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9315` | 42,130.00 USD | 0.00 USD | 263.80 USD | `-1.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9325` | 41,860.00 USD | 0.00 USD | 241.98 USD | `-1.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9335` | 41,620.00 USD | 0.00 USD | 814.76 USD | `-1.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9355` | 40,810.00 USD | 0.00 USD | 201.97 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9365` | 40,600.00 USD | 0.00 USD | 9,680.00 USD | `-1.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9395` | 30,920.00 USD | 0.00 USD | 416.01 USD | `-0.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9405` | 30,500.00 USD | 0.00 USD | 555.18 USD | `-0.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9415` | 29,950.00 USD | 0.00 USD | 997.80 USD | `-0.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9425` | 28,950.00 USD | 0.00 USD | 816.96 USD | `-0.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9435` | 28,130.00 USD | 0.00 USD | 334.28 USD | `-0.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9445` | 27,800.00 USD | 0.00 USD | 27,420.00 USD | `-0.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9455` | 383.87 USD | 0.00 USD | 383.87 USD | `-0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 623.93 USD | 623.93 USD | 0.00 USD | `+0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 29,560.00 USD | 28,930.00 USD | 0.00 USD | `+0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 29,970.00 USD | 414.68 USD | 0.00 USD | `+0.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9525` | 30,350.00 USD | 381.00 USD | 0.00 USD | `+0.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 32,370.00 USD | 2,020.00 USD | 0.00 USD | `+0.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 36,160.00 USD | 3,790.00 USD | 0.00 USD | `+0.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 36,400.00 USD | 236.26 USD | 0.00 USD | `+1.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 36,540.00 USD | 136.83 USD | 0.00 USD | `+1.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 36,940.00 USD | 403.41 USD | 0.00 USD | `+1.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 38,850.00 USD | 1,910.00 USD | 0.00 USD | `+1.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 39,410.00 USD | 568.75 USD | 0.00 USD | `+1.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 39,780.00 USD | 364.58 USD | 0.00 USD | `+1.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 40,600.00 USD | 824.91 USD | 0.00 USD | `+2.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 40,990.00 USD | 385.74 USD | 0.00 USD | `+2.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 43,020.00 USD | 2,030.00 USD | 0.00 USD | `+2.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 43,280.00 USD | 262.52 USD | 0.00 USD | `+2.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 43,670.00 USD | 387.83 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 44,500.00 USD | 830.10 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9745` | 53,250.00 USD | 8,750.00 USD | 0.00 USD | `+3.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 75,210.00 USD | 21,960.00 USD | 0.00 USD | `+3.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 75,610.00 USD | 396.17 USD | 0.00 USD | `+3.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 76,290.00 USD | 676.53 USD | 0.00 USD | `+3.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 84,640.00 USD | 8,350.00 USD | 0.00 USD | `+3.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 86,660.00 USD | 2,030.00 USD | 0.00 USD | `+3.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 87,010.00 USD | 346.13 USD | 0.00 USD | `+3.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 87,270.00 USD | 255.38 USD | 0.00 USD | `+4.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 87,490.00 USD | 223.91 USD | 0.00 USD | `+4.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9865` | 87,600.00 USD | 109.99 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 91,120.00 USD | 3,520.00 USD | 0.00 USD | `+4.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 122,870.00 USD | 31,750.00 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 123,280.00 USD | 403.06 USD | 0.00 USD | `+5.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 123,680.00 USD | 403.28 USD | 0.00 USD | `+5.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 128,820.00 USD | 5,140.00 USD | 0.00 USD | `+5.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 166,130.00 USD | 37,310.00 USD | 0.00 USD | `+5.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 166,630.00 USD | 500.25 USD | 0.00 USD | `+5.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 207,230.00 USD | 40,590.00 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 207,460.00 USD | 235.79 USD | 0.00 USD | `+5.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 208,800.00 USD | 1,340.00 USD | 0.00 USD | `+6.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 209,040.00 USD | 230.39 USD | 0.00 USD | `+6.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 209,160.00 USD | 127.65 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 209,380.00 USD | 218.64 USD | 0.00 USD | `+6.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 209,790.00 USD | 409.86 USD | 0.00 USD | `+6.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 209,900.00 USD | 110.95 USD | 0.00 USD | `+6.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 210,520.00 USD | 615.60 USD | 0.00 USD | `+7.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 211,080.00 USD | 561.17 USD | 0.00 USD | `+7.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 211,290.00 USD | 214.40 USD | 0.00 USD | `+7.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 211,540.00 USD | 249.88 USD | 0.00 USD | `+8.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 211,750.00 USD | 207.97 USD | 0.00 USD | `+8.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 211,960.00 USD | 208.26 USD | 0.00 USD | `+9.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 212,480.00 USD | 516.75 USD | 0.00 USD | `+9.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 212,830.00 USD | 348.86 USD | 0.00 USD | `+9.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 213,220.00 USD | 391.80 USD | 0.00 USD | `+9.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 213,630.00 USD | 413.76 USD | 0.00 USD | `+9.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 213,990.00 USD | 354.91 USD | 0.00 USD | `+9.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 215,890.00 USD | 1,900.00 USD | 0.00 USD | `+10.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 216,100.00 USD | 207.87 USD | 0.00 USD | `+10.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 216,310.00 USD | 207.97 USD | 0.00 USD | `+10.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 216,410.00 USD | 107.99 USD | 0.00 USD | `+11.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 291,250.00 USD | 74,840.00 USD | 0.00 USD | `+12.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 293,420.00 USD | 2,170.00 USD | 0.00 USD | `+15.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 294,960.00 USD | 1,540.00 USD | 0.00 USD | `+15.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 304,880.00 USD | 9,930.00 USD | 0.00 USD | `+15.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 305,760.00 USD | 877.63 USD | 0.00 USD | `+17.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 305,930.00 USD | 171.09 USD | 0.00 USD | `+18.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 308,700.00 USD | 2,770.00 USD | 0.00 USD | `+18.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 310,740.00 USD | 2,040.00 USD | 0.00 USD | `+18.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 310,910.00 USD | 172.32 USD | 0.00 USD | `+19.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 311,100.00 USD | 187.72 USD | 0.00 USD | `+19.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 311,290.00 USD | 188.39 USD | 0.00 USD | `+19.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 313,960.00 USD | 2,670.00 USD | 0.00 USD | `+20.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 314,130.00 USD | 174.23 USD | 0.00 USD | `+20.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 314,300.00 USD | 174.38 USD | 0.00 USD | `+20.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 314,480.00 USD | 174.84 USD | 0.00 USD | `+20.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 314,630.00 USD | 150.90 USD | 0.00 USD | `+21.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 314,780.00 USD | 151.03 USD | 0.00 USD | `+21.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 314,930.00 USD | 151.16 USD | 0.00 USD | `+21.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 316,980.00 USD | 2,050.00 USD | 0.00 USD | `+23.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 317,090.00 USD | 110.00 USD | 0.00 USD | `+23.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 317,570.00 USD | 475.80 USD | 0.00 USD | `+25.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 318,770.00 USD | 1,210.00 USD | 0.00 USD | `+26.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 361,700.00 USD | 42,930.00 USD | 0.00 USD | `+27.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 363,700.00 USD | 2,000.00 USD | 0.00 USD | `+30.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 365,090.00 USD | 1,380.00 USD | 0.00 USD | `+32.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 365,330.00 USD | 245.41 USD | 0.00 USD | `+35.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 373,730.00 USD | 8,390.00 USD | 0.00 USD | `+36.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 374,140.00 USD | 415.25 USD | 0.00 USD | `+37.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 380,660.00 USD | 6,520.00 USD | 0.00 USD | `+37.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 385,460.00 USD | 4,800.00 USD | 0.00 USD | `+38.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 386,110.00 USD | 655.75 USD | 0.00 USD | `+38.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 386,710.00 USD | 596.43 USD | 0.00 USD | `+40.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 388,520.00 USD | 1,810.00 USD | 0.00 USD | `+41.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 402,410.00 USD | 13,880.00 USD | 0.00 USD | `+41.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 403,660.00 USD | 1,250.00 USD | 0.00 USD | `+43.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 405,730.00 USD | 2,070.00 USD | 0.00 USD | `+46.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 405,870.00 USD | 140.05 USD | 0.00 USD | `+48.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 406,030.00 USD | 160.42 USD | 0.00 USD | `+48.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 406,980.00 USD | 954.32 USD | 0.00 USD | `+49.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 441,150.00 USD | 34,170.00 USD | 0.00 USD | `+51.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 442,030.00 USD | 879.84 USD | 0.00 USD | `+57.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 445,090.00 USD | 3,050.00 USD | 0.00 USD | `+60.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 445,390.00 USD | 297.27 USD | 0.00 USD | `+63.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 453,920.00 USD | 8,530.00 USD | 0.00 USD | `+74.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 454,060.00 USD | 143.99 USD | 0.00 USD | `+76.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 454,240.00 USD | 177.05 USD | 0.00 USD | `+87.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 454,670.00 USD | 431.40 USD | 0.00 USD | `+90.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 454,890.00 USD | 220.77 USD | 0.00 USD | `+92.21%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7730` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 9,740.00 USD | 39.63 USD | 2,230.00 USD |
| `7D` | `0.7750` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 698.40 USD | 0.00 USD | 3,460.00 USD |
| `7D` | `0.7790` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 0.00 USD | 3,100.00 USD | 53.43 USD |
| `7D` | `0.7810` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 436.65 USD | 25.30 USD | 1,410.00 USD |
| `7D` | `0.7830` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 114.15 USD | 1,980.00 USD | 0.00 USD |
| `7D` | `0.7850` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 112.95 USD | 2,340.00 USD | 180.30 USD |
| `7D` | `0.7870` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 5,690.00 USD | 3,090.00 USD | 450.49 USD |
| `7D` | `0.7890` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 88.75 USD | 0.00 USD | 2,110.00 USD |
| `7D` | `0.7910` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD |
| `7D` | `0.7930` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 20,360.00 USD | 1,560.00 USD | 6,130.00 USD |
| `7D` | `0.7950` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 3,290.00 USD | 8,430.00 USD | 14,710.00 USD |
| `7D` | `0.7970` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 10,100.00 USD | 1,130.00 USD | 522.30 USD |
| `7D` | `0.7990` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 20,360.00 USD | 6,180.00 USD | 13,950.00 USD |
| `7D` | `0.8010` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 5,420.00 USD | 5,300.00 USD | 2,300.00 USD |
| `7D` | `0.8030` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 4,550.00 USD | 2,440.00 USD | 10,410.00 USD |
| `7D` | `0.8050` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD |
| `7D` | `0.8070` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 12,160.00 USD | 4,660.00 USD | 16,650.00 USD |
| `7D` | `0.8090` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD |
| `7D` | `0.8110` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD |
| `7D` | `0.8130` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 14,060.00 USD | 2,970.00 USD | 9,350.00 USD |
| `7D` | `0.8150` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 61,120.00 USD | 7,590.00 USD | 19,500.00 USD |
| `7D` | `0.8170` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 10,780.00 USD | 8,770.00 USD | 9,670.00 USD |
| `7D` | `0.8190` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD |
| `7D` | `0.8210` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 7,510.00 USD | 3,290.00 USD | 10,030.00 USD |
| `7D` | `0.8230` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 29,430.00 USD | 5,100.00 USD | 13,220.00 USD |
| `7D` | `0.8250` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD |
| `7D` | `0.8270` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 4,320.00 USD | 5,770.00 USD | 616.76 USD |
| `7D` | `0.8290` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD |
| `7D` | `0.8310` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 9,280.00 USD | 1,660.00 USD | 2,450.00 USD |
| `7D` | `0.8330` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 16,220.00 USD | 11,360.00 USD | 77.95 USD |
| `7D` | `0.8350` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 19,490.00 USD | 0.00 USD | 2,290.00 USD |
| `7D` | `0.8370` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 15,240.00 USD | 1,480.00 USD | 0.00 USD |
| `7D` | `0.8390` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD |
| `7D` | `0.8410` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD |
| `1D` | `0.8430` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 1,590.00 USD | 4,840.00 USD | 933.95 USD |
| `7D` | `0.8430` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 11,320.00 USD | 3,840.00 USD | 4,060.00 USD |
| `1D` | `0.8450` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 2,360.00 USD | 7,850.00 USD | 429.42 USD |
| `7D` | `0.8450` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 1,980.00 USD | 404.64 USD | 474.61 USD |
| `1D` | `0.8470` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 24,110.00 USD | 1,110.00 USD | 165.77 USD |
| `7D` | `0.8470` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 7,900.00 USD | 1,730.00 USD | 2,390.00 USD |
| `1D` | `0.8490` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 5,120.00 USD | 2,400.00 USD | 7,940.00 USD |
| `7D` | `0.8490` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 22,370.00 USD | 9,610.00 USD | 0.00 USD |
| `1D` | `0.8510` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 13,560.00 USD | 4,140.00 USD | 16,720.00 USD |
| `7D` | `0.8510` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 14,280.00 USD | 991.53 USD | 21,470.00 USD |
| `1D` | `0.8530` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 4,680.00 USD | 3,830.00 USD | 5,510.00 USD |
| `7D` | `0.8530` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD |
| `1D` | `0.8550` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 18,270.00 USD | 3,040.00 USD | 5,090.00 USD |
| `7D` | `0.8550` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD |
| `1D` | `0.8570` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 989.11 USD | 1,720.00 USD | 6,150.00 USD |
| `7D` | `0.8570` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 3,540.00 USD | 944.22 USD | 8,450.00 USD |
| `1D` | `0.8590` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 6,870.00 USD | 10,640.00 USD | 6,420.00 USD |
| `7D` | `0.8590` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 3,730.00 USD | 0.00 USD | 1,560.00 USD |
| `1D` | `0.8610` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 8,320.00 USD | 855.53 USD | 16,460.00 USD |
| `7D` | `0.8610` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 9,960.00 USD | 3,660.00 USD | 35,340.00 USD |
| `1D` | `0.8630` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 39,330.00 USD | 12,290.00 USD | 2,010.00 USD |
| `7D` | `0.8630` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 758.91 USD | 2,910.00 USD | 1,280.00 USD |
| `1D` | `0.8650` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 17,640.00 USD | 2,110.00 USD | 1,790.00 USD |
| `7D` | `0.8650` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 47,860.00 USD | 18,930.00 USD | 184.85 USD |
| `1D` | `0.8670` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 11,890.00 USD | 10,090.00 USD | 1,110.00 USD |
| `7D` | `0.8670` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 13,660.00 USD | 3,720.00 USD | 12,140.00 USD |
| `1D` | `0.8690` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 41,960.00 USD | 3,780.00 USD | 29,400.00 USD |
| `7D` | `0.8690` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 160,750.00 USD | 13,110.00 USD | 46,230.00 USD |
| `1D` | `0.8710` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 42,250.00 USD | 24,870.00 USD | 28,630.00 USD |
| `7D` | `0.8710` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 7,370.00 USD | 23,340.00 USD | 13,110.00 USD |
| `1D` | `0.8730` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 54,380.00 USD | 21,510.00 USD | 25,960.00 USD |
| `7D` | `0.8730` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 0.00 USD | 8,170.00 USD | 295.31 USD |
| `1D` | `0.8750` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 36,600.00 USD | 6,900.00 USD | 17,890.00 USD |
| `7D` | `0.8750` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 0.00 USD | 6,380.00 USD | 8,950.00 USD |
| `1D` | `0.8770` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 10,480.00 USD | 154.89 USD | 0.00 USD |
| `7D` | `0.8770` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 1,390.00 USD | 0.00 USD | 30,820.00 USD |
| `1D` | `0.8790` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 0.00 USD | 40.93 USD | 50,910.00 USD |
| `7D` | `0.8790` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 873.30 USD | 5,580.00 USD | 53,860.00 USD |
| `1D` | `0.8810` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 13,820.00 USD | 5,210.00 USD | 3,810.00 USD |
| `7D` | `0.8810` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 1,830.00 USD | 240.78 USD | 0.00 USD |
| `1D` | `0.8830` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 521.60 USD | 5,570.00 USD | 0.00 USD |
| `7D` | `0.8830` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 2,320.00 USD | 10,140.00 USD | 11,710.00 USD |
| `1D` | `0.8850` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 5,580.00 USD | 35,520.00 USD | 11,180.00 USD |
| `7D` | `0.8850` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 0.00 USD | 5,800.00 USD | 3,970.00 USD |
| `1D` | `0.8870` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 68,710.00 USD | 18,450.00 USD | 32,750.00 USD |
| `7D` | `0.8870` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 271,870.00 USD | 22,320.00 USD | 81,590.00 USD |
| `1D` | `0.8890` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 69,440.00 USD | 40,830.00 USD | 4,860.00 USD |
| `7D` | `0.8890` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 54,380.00 USD | 73,890.00 USD | 13,880.00 USD |
| `1D` | `0.8910` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 2,150.00 USD | 38,730.00 USD | 20,050.00 USD |
| `7D` | `0.8910` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 75,300.00 USD | 22,240.00 USD | 34,270.00 USD |
| `1D` | `0.8930` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 56,810.00 USD | 24,630.00 USD | 37,920.00 USD |
| `7D` | `0.8930` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 62,870.00 USD | 23,560.00 USD | 9,170.00 USD |
| `1D` | `0.8950` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 4,110.00 USD | 15,420.00 USD | 5,670.00 USD |
| `7D` | `0.8950` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 7,120.00 USD | 37,670.00 USD | 57,420.00 USD |
| `1D` | `0.8970` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 4,620.00 USD | 24,510.00 USD | 16,170.00 USD |
| `7D` | `0.8970` | 966,680.00 USD | 0.00 USD | 966,680.00 USD | 2,140.00 USD | 4,820.00 USD | 56,330.00 USD |
| `1D` | `0.8990` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 15,840.00 USD | 0.00 USD |
| `7D` | `0.8990` | 903,390.00 USD | 0.00 USD | 903,390.00 USD | 0.00 USD | 34,220.00 USD | 0.00 USD |
| `1D` | `0.9010` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 1,970.00 USD | 24,600.00 USD | 2,600.00 USD |
| `7D` | `0.9010` | 869,170.00 USD | 0.00 USD | 869,170.00 USD | 0.00 USD | 48,840.00 USD | 0.00 USD |
| `1D` | `0.9030` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 8,980.00 USD | 17,560.00 USD | 18,230.00 USD |
| `7D` | `0.9030` | 820,330.00 USD | 0.00 USD | 820,330.00 USD | 0.00 USD | 16,370.00 USD | 23,930.00 USD |
| `1D` | `0.9050` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 19,330.00 USD | 11,600.00 USD | 22,050.00 USD |
| `7D` | `0.9050` | 780,030.00 USD | 0.00 USD | 780,030.00 USD | 0.00 USD | 3,840.00 USD | 0.00 USD |
| `1D` | `0.9070` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 36,650.00 USD | 8,370.00 USD | 33,510.00 USD |
| `7D` | `0.9070` | 776,190.00 USD | 0.00 USD | 776,190.00 USD | 23,910.00 USD | 0.00 USD | 42,040.00 USD |
| `1D` | `0.9090` | 947,220.00 USD | 0.00 USD | 947,220.00 USD | 7,100.00 USD | 9,080.00 USD | 176.94 USD |
| `1D` | `0.9110` | 930,870.00 USD | 0.00 USD | 930,870.00 USD | 25,560.00 USD | 2,850.00 USD | 2,080.00 USD |
| `1D` | `0.9130` | 900,380.00 USD | 0.00 USD | 900,380.00 USD | 11,890.00 USD | 9,480.00 USD | 17,320.00 USD |
| `7D` | `0.9130` | 710,240.00 USD | 0.00 USD | 710,240.00 USD | 0.00 USD | 0.00 USD | 20,720.00 USD |
| `1D` | `0.9150` | 861,680.00 USD | 0.00 USD | 861,680.00 USD | 3,760.00 USD | 9,920.00 USD | 18,880.00 USD |
| `7D` | `0.9150` | 689,520.00 USD | 0.00 USD | 689,520.00 USD | 0.00 USD | 515.41 USD | 15,680.00 USD |
| `1D` | `0.9170` | 829,120.00 USD | 0.00 USD | 829,120.00 USD | 0.00 USD | 79.80 USD | 6,650.00 USD |
| `7D` | `0.9170` | 673,320.00 USD | 0.00 USD | 673,320.00 USD | 0.00 USD | 0.00 USD | 33,180.00 USD |
| `1D` | `0.9190` | 822,380.00 USD | 0.00 USD | 822,380.00 USD | 2,860.00 USD | 7,530.00 USD | 7,350.00 USD |
| `1D` | `0.9210` | 804,650.00 USD | 0.00 USD | 804,650.00 USD | 12,850.00 USD | 3,680.00 USD | 6,020.00 USD |
| `7D` | `0.9210` | 640,140.00 USD | 0.00 USD | 640,140.00 USD | 0.00 USD | 7,760.00 USD | 3,970.00 USD |
| `1D` | `0.9230` | 782,090.00 USD | 0.00 USD | 782,090.00 USD | 6,600.00 USD | 7,140.00 USD | 21,700.00 USD |
| `7D` | `0.9230` | 628,410.00 USD | 0.00 USD | 628,410.00 USD | 294,370.00 USD | 0.00 USD | 26,680.00 USD |
| `1D` | `0.9250` | 746,650.00 USD | 0.00 USD | 746,650.00 USD | 99,970.00 USD | 63,270.00 USD | 62,530.00 USD |
| `7D` | `0.9250` | 307,360.00 USD | 0.00 USD | 307,360.00 USD | 0.00 USD | 52,780.00 USD | 84,070.00 USD |
| `1D` | `0.9270` | 520,880.00 USD | 0.00 USD | 520,880.00 USD | 39,920.00 USD | 7,040.00 USD | 73,810.00 USD |
| `7D` | `0.9270` | 170,510.00 USD | 0.00 USD | 170,510.00 USD | 44,020.00 USD | 11,800.00 USD | 0.00 USD |
| `1D` | `0.9290` | 400,110.00 USD | 0.00 USD | 400,110.00 USD | 80,950.00 USD | 20,440.00 USD | 38,560.00 USD |
| `7D` | `0.9290` | 114,690.00 USD | 0.00 USD | 114,690.00 USD | 0.00 USD | 12,750.00 USD | 1,600.00 USD |
| `1D` | `0.9310` | 260,150.00 USD | 0.00 USD | 260,150.00 USD | 0.00 USD | 7,130.00 USD | 5,410.00 USD |
| `1D` | `0.9330` | 247,620.00 USD | 0.00 USD | 247,620.00 USD | 11,160.00 USD | 23,770.00 USD | 42,440.00 USD |
| `7D` | `0.9330` | 100,340.00 USD | 0.00 USD | 100,340.00 USD | 37,450.00 USD | 0.00 USD | 31,370.00 USD |
| `1D` | `0.9350` | 170,250.00 USD | 0.00 USD | 170,250.00 USD | 121,410.00 USD | 21,200.00 USD | 27,640.00 USD |
| `7D` | `0.9350` | 31,530.00 USD | 0.00 USD | 31,530.00 USD | 0.00 USD | 11,160.00 USD | 20,370.00 USD |
| `1D` | `0.9370` | 76,090.00 USD | 76,090.00 USD | 0.00 USD | 18,250.00 USD | 39,710.00 USD | 18,130.00 USD |
| `1D` | `0.9370` | 152,180.00 USD | 152,180.00 USD | 0.00 USD | 18,250.00 USD | 39,710.00 USD | 18,130.00 USD |
| `7D` | `0.9370` | 84,400.00 USD | 84,400.00 USD | 0.00 USD | 16,340.00 USD | 19,540.00 USD | 48,530.00 USD |
| `7D` | `0.9370` | 168,800.00 USD | 168,800.00 USD | 0.00 USD | 16,340.00 USD | 19,540.00 USD | 48,530.00 USD |
| `1D` | `0.9390` | 153,830.00 USD | 153,830.00 USD | 0.00 USD | 1,340.00 USD | 309.30 USD | 0.00 USD |
| `7D` | `0.9390` | 242,960.00 USD | 242,960.00 USD | 0.00 USD | 39,250.00 USD | 0.00 USD | 34,910.00 USD |
| `1D` | `0.9410` | 154,750.00 USD | 154,750.00 USD | 0.00 USD | 673.54 USD | 239.40 USD | 0.00 USD |
| `7D` | `0.9410` | 406,010.00 USD | 406,010.00 USD | 0.00 USD | 161,930.00 USD | 1,130.00 USD | 0.00 USD |
| `1D` | `0.9430` | 156,210.00 USD | 156,210.00 USD | 0.00 USD | 1,230.00 USD | 224.96 USD | 0.00 USD |
| `7D` | `0.9450` | 430,300.00 USD | 430,300.00 USD | 0.00 USD | 0.00 USD | 20,890.00 USD | 3,390.00 USD |
| `1D` | `0.9470` | 156,660.00 USD | 156,660.00 USD | 0.00 USD | 0.00 USD | 199.60 USD | 256.32 USD |
| `7D` | `0.9470` | 516,810.00 USD | 516,810.00 USD | 0.00 USD | 3,540.00 USD | 6,380.00 USD | 76,590.00 USD |
| `1D` | `0.9490` | 238,550.00 USD | 238,550.00 USD | 0.00 USD | 81,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9490` | 600,740.00 USD | 600,740.00 USD | 0.00 USD | 2,770.00 USD | 10,340.00 USD | 70,820.00 USD |
| `1D` | `0.9510` | 239,360.00 USD | 239,360.00 USD | 0.00 USD | 0.00 USD | 813.18 USD | 0.00 USD |
| `7D` | `0.9510` | 892,140.00 USD | 892,140.00 USD | 0.00 USD | 258,650.00 USD | 28,180.00 USD | 4,570.00 USD |
| `1D` | `0.9530` | 239,980.00 USD | 239,980.00 USD | 0.00 USD | 0.00 USD | 623.88 USD | 0.00 USD |
| `7D` | `0.9530` | 900,370.00 USD | 900,370.00 USD | 0.00 USD | 0.00 USD | 8,240.00 USD | 0.00 USD |
| `1D` | `0.9550` | 280,660.00 USD | 280,660.00 USD | 0.00 USD | 18,000.00 USD | 22,670.00 USD | 0.00 USD |
| `7D` | `0.9550` | 920,110.00 USD | 920,110.00 USD | 0.00 USD | 0.00 USD | 19,730.00 USD | 0.00 USD |
| `1D` | `0.9570` | 292,830.00 USD | 292,830.00 USD | 0.00 USD | 6,640.00 USD | 5,530.00 USD | 0.00 USD |
| `7D` | `0.9570` | 933,270.00 USD | 933,270.00 USD | 0.00 USD | 1,910.00 USD | 10,300.00 USD | 957.94 USD |
| `1D` | `0.9590` | 314,510.00 USD | 314,510.00 USD | 0.00 USD | 14,060.00 USD | 3,680.00 USD | 3,930.00 USD |
| `7D` | `0.9590` | 954,340.00 USD | 954,340.00 USD | 0.00 USD | 1,980.00 USD | 18,220.00 USD | 866.69 USD |
| `1D` | `0.9610` | 371,760.00 USD | 371,760.00 USD | 0.00 USD | 14,760.00 USD | 11,950.00 USD | 30,550.00 USD |
| `7D` | `0.9610` | 979,720.00 USD | 979,720.00 USD | 0.00 USD | 24,370.00 USD | 0.00 USD | 1,010.00 USD |
| `1D` | `0.9630` | 550,030.00 USD | 550,030.00 USD | 0.00 USD | 102,030.00 USD | 30,630.00 USD | 45,610.00 USD |
| `7D` | `0.9630` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 56,160.00 USD | 31,820.00 USD | 84,550.00 USD |
| `1D` | `0.9650` | 691,380.00 USD | 691,380.00 USD | 0.00 USD | 29,080.00 USD | 33,020.00 USD | 79,250.00 USD |
| `7D` | `0.9650` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 97,600.00 USD | 0.00 USD | 12,330.00 USD |
| `1D` | `0.9670` | 787,810.00 USD | 787,810.00 USD | 0.00 USD | 53,970.00 USD | 16,730.00 USD | 25,720.00 USD |
| `7D` | `0.9670` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 40,070.00 USD | 5,550.00 USD | 0.00 USD |
| `1D` | `0.9690` | 824,050.00 USD | 824,050.00 USD | 0.00 USD | 12,270.00 USD | 14,610.00 USD | 9,360.00 USD |
| `7D` | `0.9690` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 21,100.00 USD | 30,500.00 USD |
| `1D` | `0.9710` | 926,870.00 USD | 926,870.00 USD | 0.00 USD | 11,360.00 USD | 15,190.00 USD | 76,280.00 USD |
| `7D` | `0.9710` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 18,250.00 USD | 31,370.00 USD |
| `1D` | `0.9730` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 44,370.00 USD | 6,610.00 USD | 36,100.00 USD |
| `7D` | `0.9730` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 2,910.00 USD | 9,290.00 USD | 27,110.00 USD |
| `1D` | `0.9750` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 25,990.00 USD | 17,610.00 USD | 31,740.00 USD |
| `7D` | `0.9750` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 2,090.00 USD | 17,230.00 USD | 51,650.00 USD |
| `1D` | `0.9770` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 78,840.00 USD | 14,700.00 USD | 11,360.00 USD |
| `7D` | `0.9770` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD |
| `1D` | `0.9790` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 36,540.00 USD | 11,310.00 USD | 26,320.00 USD |
| `7D` | `0.9790` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD | 85,420.00 USD |
| `1D` | `0.9810` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 16,990.00 USD | 6,570.00 USD | 28,550.00 USD |
| `7D` | `0.9810` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 540.00 USD | 4,020.00 USD | 119,460.00 USD |
| `1D` | `0.9830` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 33,180.00 USD | 27,220.00 USD | 55,550.00 USD |
| `7D` | `0.9830` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 124,720.00 USD | 15,810.00 USD | 94,290.00 USD |
| `1D` | `0.9850` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 46,690.00 USD | 8,800.00 USD | 18,830.00 USD |
| `7D` | `0.9850` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 211.77 USD | 22,300.00 USD |
| `1D` | `0.9870` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 14,650.00 USD | 6,470.00 USD | 22,410.00 USD |
| `7D` | `0.9870` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 67,950.00 USD |
| `1D` | `0.9890` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 27,890.00 USD | 3,780.00 USD | 30,190.00 USD |
| `7D` | `0.9890` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `0.9910` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 60,020.00 USD | 5,890.00 USD | 45,430.00 USD |
| `7D` | `0.9910` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 3,700.00 USD | 800.44 USD | 35,270.00 USD |
| `1D` | `0.9930` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 16,270.00 USD | 7,030.00 USD | 8,200.00 USD |
| `7D` | `0.9930` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 36,000.00 USD |
| `1D` | `0.9950` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 29,210.00 USD | 2,120.00 USD | 7,140.00 USD |
| `7D` | `0.9950` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 63,060.00 USD | 5,380.00 USD | 58,050.00 USD |
| `1D` | `0.9970` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 46,950.00 USD | 1,840.00 USD | 13,030.00 USD |
| `7D` | `0.9970` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 95,130.00 USD | 253.35 USD | 4,670.00 USD |
| `1D` | `0.9990` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 35,220.00 USD | 17,910.00 USD | 10,720.00 USD |
| `7D` | `0.9990` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 6,490.00 USD | 462.12 USD |
| `1D` | `1.00` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 44,580.00 USD | 10,790.00 USD | 13,680.00 USD |
| `7D` | `1.00` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.00` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 12,370.00 USD | 9,310.00 USD | 6,140.00 USD |
| `7D` | `1.00` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 107,670.00 USD | 21,850.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 54,780.00 USD | 5,520.00 USD | 5,820.00 USD |
| `7D` | `1.00` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 32,430.00 USD | 3,970.00 USD | 12,730.00 USD |
| `1D` | `1.01` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 50,600.00 USD | 11,770.00 USD | 47,170.00 USD |
| `7D` | `1.01` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 35,710.00 USD | 240.78 USD | 29,210.00 USD |
| `1D` | `1.01` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 30,870.00 USD | 13,790.00 USD | 7,610.00 USD |
| `7D` | `1.01` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD |
| `1D` | `1.01` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 9,660.00 USD | 23,460.00 USD | 265.91 USD |
| `7D` | `1.01` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 20,090.00 USD | 17,980.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 10,450.00 USD | 1,540.00 USD | 3,780.00 USD |
| `7D` | `1.01` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD |
| `1D` | `1.01` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 14,310.00 USD | 23,780.00 USD | 14,630.00 USD |
| `7D` | `1.01` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 26,510.00 USD | 7,420.00 USD |
| `1D` | `1.02` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 3,990.00 USD | 3,840.00 USD | 16,780.00 USD |
| `7D` | `1.02` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD |
| `1D` | `1.02` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 55,630.00 USD | 4,860.00 USD | 10,650.00 USD |
| `7D` | `1.02` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 17,960.00 USD | 83,360.00 USD | 11,810.00 USD |
| `1D` | `1.02` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 19,220.00 USD | 9,450.00 USD | 21,100.00 USD |
| `7D` | `1.02` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 61,450.00 USD | 32,840.00 USD | 68,370.00 USD |
| `1D` | `1.02` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 44,780.00 USD | 18,890.00 USD | 34,830.00 USD |
| `7D` | `1.02` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 82,230.00 USD | 86,210.00 USD | 146,060.00 USD |
| `1D` | `1.02` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 44,190.00 USD | 12,640.00 USD | 27,520.00 USD |
| `7D` | `1.02` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 28,320.00 USD | 48,490.00 USD | 37,230.00 USD |
| `1D` | `1.03` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 15,560.00 USD | 10,270.00 USD | 7,260.00 USD |
| `7D` | `1.03` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 161,070.00 USD | 127,000.00 USD | 25,260.00 USD |
| `1D` | `1.03` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 18,290.00 USD | 18,890.00 USD | 25,030.00 USD |
| `7D` | `1.03` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD |
| `1D` | `1.03` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 75,080.00 USD | 9,640.00 USD | 31,790.00 USD |
| `7D` | `1.03` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD |
| `1D` | `1.03` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 17,370.00 USD | 1,590.00 USD | 16,590.00 USD |
| `7D` | `1.03` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD |
| `1D` | `1.03` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 11,120.00 USD | 18,040.00 USD | 7,250.00 USD |
| `7D` | `1.03` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 259,060.00 USD | 8,290.00 USD | 43,700.00 USD |
| `1D` | `1.04` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 42,410.00 USD | 3,800.00 USD | 11,940.00 USD |
| `7D` | `1.04` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 193,150.00 USD | 3,330.00 USD | 109,460.00 USD |
| `1D` | `1.04` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 7,640.00 USD | 5,430.00 USD | 5,470.00 USD |
| `7D` | `1.04` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 239,580.00 USD | 9,010.00 USD | 134,440.00 USD |
| `1D` | `1.04` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 7,100.00 USD | 2,540.00 USD | 13,700.00 USD |
| `7D` | `1.04` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 285,690.00 USD | 2,090.00 USD | 159,500.00 USD |
| `1D` | `1.04` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 14,210.00 USD | 8,400.00 USD | 8,590.00 USD |
| `7D` | `1.04` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD |
| `1D` | `1.04` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 1,340.00 USD | 638.69 USD | 6,170.00 USD |
| `7D` | `1.04` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD |
| `1D` | `1.05` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 7,650.00 USD | 5,890.00 USD | 6,150.00 USD |
| `7D` | `1.05` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 178,890.00 USD | 96,370.00 USD | 244,850.00 USD |
| `1D` | `1.05` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 4,940.00 USD | 4,010.00 USD | 10,810.00 USD |
| `7D` | `1.05` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 116,030.00 USD | 13,780.00 USD | 77,620.00 USD |
| `1D` | `1.05` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 29,800.00 USD | 73.09 USD | 13,090.00 USD |
| `7D` | `1.05` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 175,350.00 USD | 43,690.00 USD | 96,730.00 USD |
| `1D` | `1.05` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 4,370.00 USD | 937.66 USD | 6,160.00 USD |
| `7D` | `1.05` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 68,010.00 USD | 58,070.00 USD | 74,380.00 USD |
| `7D` | `1.05` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 121,450.00 USD | 33,860.00 USD | 72,330.00 USD |
| `7D` | `1.06` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 218,860.00 USD | 70,160.00 USD | 106,380.00 USD |
| `7D` | `1.06` | 8,830,000.00 USD | 8,830,000.00 USD | 0.00 USD | 239,650.00 USD | 74,380.00 USD | 145,170.00 USD |
| `7D` | `1.06` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 138,520.00 USD | 56,310.00 USD | 78,020.00 USD |
| `7D` | `1.06` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 140,500.00 USD | 73,690.00 USD | 71,340.00 USD |
| `7D` | `1.06` | 9,590,000.00 USD | 9,590,000.00 USD | 0.00 USD | 74,870.00 USD | 27,820.00 USD | 91,220.00 USD |
| `7D` | `1.07` | 9,670,000.00 USD | 9,670,000.00 USD | 0.00 USD | 60,290.00 USD | 26,450.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `173.92M` | Total OI Tokens: `185,610,705.4 DOT`
  * 1h OI Change: `-0.69%` | 4h OI Change: `-0.42%` | 24h OI Change: `-15.99%`
  * Exchange Breakdown: Binance=`34.15M` | Bybit=`22.26M` | OKX=`10.09M` | Hyperliquid=`5.81M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-78.70` | Last 24h: `6.26K` | Last 3d: `-7.35K` | Last 7d: `-25.50K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0116%` |
| **USDT Bybit** | `-0.0109%` | **USDT KuCoin** | `-0.0213%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0066%` | **USDT Bitget** | `0.0065%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `49.45%` | `50.55%` | `0.98` | 4,690,000.00 USD |
| `15M` | `Binance` | `57.32%` | `42.68%` | `1.34` | 1,920,000.00 USD |
| `15M` | `OKX` | `44.58%` | `55.42%` | `0.80` | 328,310.00 USD |
| `15M` | `Bybit` | `40.12%` | `59.88%` | `0.67` | 455,890.00 USD |
| `15M` | `KuCoin` | `49.24%` | `50.76%` | `0.97` | 70,150.00 USD |
| `15M` | `Gate` | `26.46%` | `73.54%` | `0.36` | 299,650.00 USD |
| `15M` | `Bitget` | `38.61%` | `61.39%` | `0.63` | 108,300.00 USD |
| `15M` | `BingX` | `51.78%` | `48.22%` | `1.07` | 133,600.00 USD |
| `15M` | `MEXC` | `35.07%` | `64.93%` | `0.54` | 796,070.00 USD |
| `15M` | `Bitunix` | `55.4%` | `44.6%` | `1.24` | 217,700.00 USD |
| `15M` | `Hyperliquid` | `25.71%` | `74.29%` | `0.35` | 41,460.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `37.78%` | `62.22%` | `0.61` | 59,340.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `99.56%` | `0.44%` | `226.27` | 229,820.00 USD |
| `15M` | `HTX` | `0.21%` | `99.79%` | `0.00` | 2,080.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `1.43%` | `98.57%` | `0.01` | 14,400.00 USD |
| `15M` | `Aster` | `0.73%` | `99.27%` | `0.01` | 7,390.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `32.12%` | `67.88%` | `0.47` | 2,880.00 USD |
| `15M` | `Whale Positions` | `57.32%` | `42.68%` | `1.34` | 1,920,000.00 USD |
| `15M` | `Global Accounts` | `49.45%` | `50.55%` | `0.98` | 4,690,000.00 USD |
| `1H` | `DOT` | `45.60%` | `54.40%` | `0.84` | 30,520,000.00 USD |
| `1H` | `Binance` | `47.97%` | `52.03%` | `0.92` | 11,740,000.00 USD |
| `1H` | `OKX` | `39.35%` | `60.65%` | `0.65` | 3,510,000.00 USD |
| `1H` | `Bybit` | `42.8%` | `57.2%` | `0.75` | 2,630,000.00 USD |
| `1H` | `KuCoin` | `48.51%` | `51.49%` | `0.94` | 280,430.00 USD |
| `1H` | `Gate` | `61.13%` | `38.87%` | `1.57` | 1,120,000.00 USD |
| `1H` | `Bitget` | `45.49%` | `54.51%` | `0.83` | 1,040,000.00 USD |
| `1H` | `BingX` | `19.34%` | `80.66%` | `0.24` | 1,840,000.00 USD |
| `1H` | `MEXC` | `44.47%` | `55.53%` | `0.80` | 5,600,000.00 USD |
| `1H` | `Bitunix` | `42.84%` | `57.16%` | `0.75` | 827,670.00 USD |
| `1H` | `Hyperliquid` | `22.06%` | `77.94%` | `0.28` | 446,560.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `61.24%` | `38.76%` | `1.58` | 328,530.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `94.22%` | `5.78%` | `16.30` | 949,760.00 USD |
| `1H` | `HTX` | `39.18%` | `60.82%` | `0.64` | 57,630.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `53.96%` | `46.04%` | `1.17` | 99,570.00 USD |
| `1H` | `Aster` | `32.98%` | `67.02%` | `0.49` | 39,270.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `19.8%` | `80.2%` | `0.25` | 19,000.00 USD |
| `1H` | `Whale Positions` | `47.97%` | `52.03%` | `0.92` | 11,740,000.00 USD |
| `1H` | `Global Accounts` | `45.60%` | `54.40%` | `0.84` | 30,520,000.00 USD |
| `4H` | `DOT` | `49.06%` | `50.94%` | `0.96` | 425,920,000.00 USD |
| `4H` | `Binance` | `51.2%` | `48.8%` | `1.05` | 187,520,000.00 USD |
| `4H` | `OKX` | `46.26%` | `53.74%` | `0.86` | 50,480,000.00 USD |
| `4H` | `Bybit` | `48.25%` | `51.75%` | `0.93` | 54,250,000.00 USD |
| `4H` | `KuCoin` | `55.76%` | `44.24%` | `1.26` | 5,200,000.00 USD |
| `4H` | `Gate` | `53.05%` | `46.95%` | `1.13` | 13,760,000.00 USD |
| `4H` | `Bitget` | `51.67%` | `48.33%` | `1.07` | 26,830,000.00 USD |
| `4H` | `BingX` | `40.14%` | `59.86%` | `0.67` | 15,680,000.00 USD |
| `4H` | `MEXC` | `45.73%` | `54.27%` | `0.84` | 15,890,000.00 USD |
| `4H` | `Bitunix` | `46.16%` | `53.84%` | `0.86` | 8,910,000.00 USD |
| `4H` | `Hyperliquid` | `43.69%` | `56.31%` | `0.78` | 29,370,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.2%` | `50.8%` | `0.97` | 1,920,000.00 USD |
| `4H` | `Crypto.com` | `61.32%` | `38.68%` | `1.59` | 72,350.00 USD |
| `4H` | `WhiteBIT` | `49.07%` | `50.93%` | `0.96` | 11,230,000.00 USD |
| `4H` | `HTX` | `54.04%` | `45.96%` | `1.18` | 544,420.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `51.65%` | `48.35%` | `1.07` | 311,640.00 USD |
| `4H` | `Aster` | `49.96%` | `50.04%` | `1.00` | 1,290,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `46.98%` | `53.02%` | `0.89` | 2,660,000.00 USD |
| `4H` | `Whale Positions` | `51.2%` | `48.8%` | `1.05` | 187,520,000.00 USD |
| `4H` | `Global Accounts` | `49.06%` | `50.94%` | `0.96` | 425,920,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.9472` | `0.9482` | `0.9472` | `0.9508` | `0.9456` | 389,995.41 USD | 191,985.72 USD | 198,009.69 USD | -6,023.97 USD | `-1.54%` | `10B / 6S` |
| `5:00 UTC` | `0.9476` | `0.9498` | `0.9476` | `0.9535` | `0.9458` | 318,218.14 USD | 165,434.86 USD | 152,783.28 USD | 12,651.58 USD | `+3.98%` | `12B / 14S` |
| `0:00 UTC` | `0.9526` | `0.9520` | `0.9526` | `0.9540` | `0.9497` | 614,374.64 USD | 368,145.88 USD | 246,228.76 USD | 121,917.13 USD | `+19.84%` | `12B / 1S` |
| `5:00 UTC` | `0.9526` | `0.9529` | `0.9526` | `0.9549` | `0.9508` | 274,656.73 USD | 129,149.54 USD | 145,507.19 USD | -16,357.65 USD | `-5.96%` | `6B / 6S` |
| `0:00 UTC` | `0.9473` | `0.9490` | `0.9473` | `0.9556` | `0.9421` | 484,699.52 USD | 196,408.58 USD | 288,290.94 USD | -91,882.35 USD | `-18.96%` | `12B / 39S` |
| `5:00 UTC` | `0.9436` | `0.9445` | `0.9436` | `0.9473` | `0.9425` | 430,563.34 USD | 161,800.40 USD | 268,762.94 USD | -106,962.53 USD | `-24.84%` | `2B / 14S` |
| `0:00 UTC` | `0.9446` | `0.9460` | `0.9446` | `0.9486` | `0.9442` | 368,731.69 USD | 177,970.36 USD | 190,761.33 USD | -12,790.97 USD | `-3.47%` | `10B / 4S` |
| `5:00 UTC` | `0.9438` | `0.9447` | `0.9438` | `0.9488` | `0.9423` | 353,543.62 USD | 111,318.38 USD | 242,225.25 USD | -130,906.87 USD | `-37.03%` | `2B / 19S` |
| `0:00 UTC` | `0.9378` | `0.9391` | `0.9378` | `0.9427` | `0.9366` | 674,681.66 USD | 251,815.20 USD | 422,866.46 USD | -171,051.26 USD | `-25.35%` | `2B / 15S` |
| `5:00 UTC` | `0.9367` | `0.9370` | `0.9367` | `0.9375` | `0.9365` | 99,729.45 USD | 40,658.63 USD | 59,070.82 USD | -18,412.19 USD | `-18.46%` | `0B / 1S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:39` | `Volume 1.0M DOT` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 19:19` | `Range 0.005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.9951` | 122,000.00 USD | 0.00 USD |
| `10-28 19:07` | `Volume 1.0M DOT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.01` | 333,000.00 USD | 0.00 USD |
| `10-28 19:01` | `Range 0.005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 18:58` | `Volume 1.0M DOT` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 18:40` | `Volume 1.0M DOT` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.9970` | 0.00 USD | 0.00 USD |
| `10-28 18:31` | `Range 0.005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.9987` | 0.00 USD | 0.00 USD |
| `10-28 18:31` | `Range 0.005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.00` | 219,000.00 USD | 0.00 USD |
| `10-28 18:30` | `Volume 1.0M DOT` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.9987` | 0.00 USD | 0.00 USD |
| `10-28 18:30` | `Volume 1.0M DOT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.00` | 221,000.00 USD | 0.00 USD |
| `10-28 18:19` | `Range 0.005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9972` | 0.00 USD | 0.00 USD |
| `10-28 18:16` | `Volume 1.0M DOT` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9972` | 0.00 USD | 0.00 USD |
| `10-28 17:55` | `Volume 1.0M DOT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.01` | 229,000.00 USD | 0.00 USD |
| `10-28 17:46` | `Range 0.005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.01` | 260,000.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 1.0M DOT` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 1.0M DOT` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `1.00` | 0.00 USD | 0.00 USD |
| `10-28 11:08` | `Range 0.005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.00` | 0.00 USD | 0.00 USD |
| `10-28 09:02` | `Range 0.005` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `1.01` | 363,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 1,640.00 USD | -57,910.00 USD | **`DISTRIBUTION`** |
| `15m` | -50,250.00 USD | -173,790.00 USD | **`DISTRIBUTION`** |
| `30m` | -46,330.00 USD | -431,040.00 USD | **`DISTRIBUTION`** |
| `1h` | -35,850.00 USD | -552,460.00 USD | **`DISTRIBUTION`** |
| `2h` | -18,090.00 USD | -692,590.00 USD | **`DISTRIBUTION`** |
| `4h` | -135,770.00 USD | -1,880,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -85,960.00 USD | -1,620,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 8,130.00 USD | -552,030.00 USD | **`DISTRIBUTION`** |
| `12h` | 63,300.00 USD | -1,050,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,330,000.00 USD | -8,720,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,150,000.00 USD | -24,610,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,710,000.00 USD | -78,850,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+1.64K` | 15m=`-50.25K` | 1h=`-35.85K` | 24h=`-1.33M`
* Futures Capital Netflows: 5m=`-57.91K` | 15m=`-173.79K` | 1h=`-552.46K` | 24h=`-8.72M`
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
  * Execution Entry: `0.8901` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.8491` (Risk Distance: `0.0420` pts)
  * +2.5R Take Profit: `0.9951`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9356` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9766` (Risk Distance: `0.0420` pts)
  * +2.5R Take Profit: `0.8306`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9430`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
