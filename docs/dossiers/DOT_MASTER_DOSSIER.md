# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 14:35:45 IST` (`2026-10-30 09:05:45 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9250` | **Live Ask Quote**: `0.9450` | **Mid Price**: `0.9350`
- **Spread Points**: `20.00` | **Spread BPS**: `213.90 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.9350` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.9415` | Lower -3.00σ Band: `0.9285`
  * Upper +2.51σ Band: `0.9401` | Lower -2.51σ Band: `0.9299`
  * Upper +2.01σ Band: `0.9389` | Lower -2.01σ Band: `0.9311`
  * Upper +2.00σ Band: `0.9387` | Lower -2.00σ Band: `0.9313`
  * Upper +1.28σ Band: `0.9376` | Lower -1.28σ Band: `0.9324`
  * Upper +1.00σ Band: `0.9369` | Lower -1.00σ Band: `0.9331`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9350` | EMA-20=`0.9350` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9350` (Slope: `+0.0000`) | EMA-100=`0.9350`
  * Institutional Anchors: EMA-144=`0.9350` | EMA-200=`0.9350` (Slope: `+0.0000`) | EMA-233=`0.9350`
- **Range Boundaries**: 24H High=`0.9444` | 24H Low=`0.9257` | Weekly High=`0.9537` | Weekly Low=`0.9163`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9447` (Distance: `-0.92%`)
  * Point of Control (POC) = `0.9119` (Distance: `+2.64%`)
  * Value Area Low (VAL) = `0.8986` (Distance: `+4.17%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.02` | Weekly POC=`0.9945` | Weekly VAL=`0.9701`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9330` | Low=`0.8570`
  * London Session (08:00-16:00 UTC): High=`0.9480` | Low=`0.9250`
  * New York Session (13:00-21:00 UTC): High=`0.9406` | Low=`0.9294`
  * Initial Balance (First Hour): IB High=`0.9480` | IB Low=`0.9290`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9313` - `0.9387`
  * Optimal Trade Entry (OTE 0.705): `0.9369`
  * Structural Invalidation Anchor (0.786): `0.9425`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9366` | `0.9403` | `0.9359` | `0.9403` | `146,220` | 137,013.95 USD | -22,094.50 USD | `-16.13%` | -5,222,765.04 USD | `+0.23` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.9400` | `0.9400` | `0.9369` | `0.9375` | `80,318` | 75,382.46 USD | -26,263.68 USD | `-34.84%` | -5,249,028.72 USD | `+0.13` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.9375` | `0.9376` | `0.9358` | `0.9361` | `79,967` | 74,887.36 USD | -42,342.62 USD | `-56.54%` | -5,291,371.34 USD | `-0.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9424` | `0.9427` | `0.9366` | `0.9369` | `718,449` | 674,681.66 USD | -171,051.26 USD | `-25.35%` | -5,181,544.30 USD | `-1.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9370` | `0.9403` | `0.9359` | `0.9375` | `370,546` | 347,308.90 USD | -79,579.90 USD | `-22.91%` | -5,261,124.20 USD | `-0.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.9375` | `0.9376` | `0.9358` | `0.9361` | `79,967` | 74,887.36 USD | -42,342.62 USD | `-56.54%` | -5,303,466.82 USD | `+0.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.9521` | `0.9556` | `0.9420` | `0.9454` | `1,900,301` | 1,804,294.23 USD | -93,285.41 USD | `-5.17%` | -5,022,371.88 USD | `+0.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.9454` | `0.9488` | `0.9359` | `0.9375` | `1,853,058` | 1,744,265.88 USD | -394,329.00 USD | `-22.61%` | -5,416,700.88 USD | `-0.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.9375` | `0.9376` | `0.9358` | `0.9363` | `81,538` | 76,358.65 USD | -40,882.00 USD | `-53.54%` | -5,457,582.88 USD | `+0.25` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,092,983.65 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9603` | `0.9263` | `0.9454` | `10,832,060` | 10,247,507.62 USD | -822,915.31 USD | `-8.03%` | -4,915,898.96 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9454` | `0.9488` | `0.9358` | `0.9361` | `1,933,025` | 1,819,153.24 USD | -436,671.62 USD | `-24.00%` | -5,352,570.58 USD | `+0.25` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -974,642.25 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,499,370.98 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,092,983.65 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9603` | `0.9263` | `0.9454` | `10,832,060` | 10,247,507.62 USD | -822,915.31 USD | `-8.03%` | -4,915,898.96 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9454` | `0.9488` | `0.9358` | `0.9361` | `1,933,025` | 1,819,153.24 USD | -436,671.62 USD | `-24.00%` | -5,352,570.58 USD | `+0.25` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`0.9350`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:32:27 IST` |

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
| `7D` | `Long Liquidation` | `0.7730` | 3,210,000.00 USD | 3,210,000.00 USD | 9,740.00 USD | 39.63 USD | 2,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7750` | 3,200,000.00 USD | 3,200,000.00 USD | 698.40 USD | 0.00 USD | 3,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7775` | 2,490.00 USD | 128,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7790` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 3,100.00 USD | 53.43 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7810` | 3,190,000.00 USD | 3,190,000.00 USD | 436.65 USD | 25.30 USD | 1,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7830` | 3,190,000.00 USD | 3,190,000.00 USD | 114.15 USD | 1,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7850` | 3,190,000.00 USD | 3,190,000.00 USD | 112.95 USD | 2,340.00 USD | 180.30 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7865` | 156.51 USD | 126,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7870` | 3,190,000.00 USD | 3,190,000.00 USD | 5,690.00 USD | 3,090.00 USD | 450.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7890` | 3,180,000.00 USD | 3,180,000.00 USD | 88.75 USD | 0.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 277.39 USD | 126,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7910` | 3,170,000.00 USD | 3,170,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7930` | 3,150,000.00 USD | 3,150,000.00 USD | 20,360.00 USD | 1,560.00 USD | 6,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7935` | 1,760.00 USD | 125,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7950` | 3,120,000.00 USD | 3,120,000.00 USD | 3,290.00 USD | 8,430.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7970` | 3,100,000.00 USD | 3,100,000.00 USD | 10,100.00 USD | 1,130.00 USD | 522.30 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7985` | 210.40 USD | 124,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7990` | 3,080,000.00 USD | 3,080,000.00 USD | 20,360.00 USD | 6,180.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8010` | 3,040,000.00 USD | 3,040,000.00 USD | 5,420.00 USD | 5,300.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8030` | 3,030,000.00 USD | 3,030,000.00 USD | 4,550.00 USD | 2,440.00 USD | 10,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8050` | 3,010,000.00 USD | 3,010,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8070` | 2,990,000.00 USD | 2,990,000.00 USD | 12,160.00 USD | 4,660.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8090` | 2,960,000.00 USD | 2,960,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8110` | 2,950,000.00 USD | 2,950,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8130` | 2,940,000.00 USD | 2,940,000.00 USD | 14,060.00 USD | 2,970.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 123,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8150` | 2,920,000.00 USD | 2,920,000.00 USD | 61,120.00 USD | 7,590.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8170` | 2,830,000.00 USD | 2,830,000.00 USD | 10,780.00 USD | 8,770.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8190` | 2,800,000.00 USD | 2,800,000.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8210` | 2,780,000.00 USD | 2,780,000.00 USD | 7,510.00 USD | 3,290.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 123,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8230` | 2,760,000.00 USD | 2,760,000.00 USD | 29,430.00 USD | 5,100.00 USD | 13,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 749.96 USD | 121,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8250` | 2,710,000.00 USD | 2,710,000.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 2,700,000.00 USD | 2,700,000.00 USD | 4,320.00 USD | 5,770.00 USD | 616.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8290` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8310` | 2,690,000.00 USD | 2,690,000.00 USD | 9,280.00 USD | 1,660.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8330` | 2,670,000.00 USD | 2,670,000.00 USD | 16,220.00 USD | 11,360.00 USD | 77.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8350` | 2,650,000.00 USD | 2,650,000.00 USD | 19,490.00 USD | 0.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 120,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8370` | 2,620,000.00 USD | 2,620,000.00 USD | 15,240.00 USD | 1,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8390` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8410` | 2,600,000.00 USD | 2,600,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,570.00 USD | 120,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 2,480,000.00 USD | 2,480,000.00 USD | 2,800.00 USD | 5,820.00 USD | 933.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8430` | 2,600,000.00 USD | 2,600,000.00 USD | 11,320.00 USD | 3,840.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8440` | 2,470,000.00 USD | 2,470,000.00 USD | 2,360.00 USD | 778.54 USD | 31.90 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8450` | 2,580,000.00 USD | 2,580,000.00 USD | 1,980.00 USD | 404.64 USD | 474.61 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8460` | 2,470,000.00 USD | 2,470,000.00 USD | 16,570.00 USD | 7,340.00 USD | 595.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8470` | 2,570,000.00 USD | 2,570,000.00 USD | 7,900.00 USD | 1,730.00 USD | 2,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8480` | 2,440,000.00 USD | 2,440,000.00 USD | 7,990.00 USD | 951.92 USD | 3,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8490` | 2,560,000.00 USD | 2,560,000.00 USD | 22,370.00 USD | 9,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 118,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 2,430,000.00 USD | 2,430,000.00 USD | 13,780.00 USD | 3,980.00 USD | 6,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 2,530,000.00 USD | 2,530,000.00 USD | 14,280.00 USD | 991.53 USD | 21,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8520` | 2,410,000.00 USD | 2,410,000.00 USD | 8,170.00 USD | 3,840.00 USD | 19,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 2,490,000.00 USD | 2,490,000.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8540` | 2,370,000.00 USD | 2,370,000.00 USD | 3,330.00 USD | 5,480.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 2,490,000.00 USD | 2,490,000.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8560` | 2,360,000.00 USD | 2,360,000.00 USD | 16,770.00 USD | 760.40 USD | 2,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8570` | 2,480,000.00 USD | 2,480,000.00 USD | 3,540.00 USD | 944.22 USD | 8,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 117,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8580` | 2,340,000.00 USD | 2,340,000.00 USD | 2,870.00 USD | 1,040.00 USD | 8,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8590` | 2,470,000.00 USD | 2,470,000.00 USD | 3,730.00 USD | 0.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8600` | 2,330,000.00 USD | 2,330,000.00 USD | 7,990.00 USD | 10,610.00 USD | 18,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8610` | 2,470,000.00 USD | 2,470,000.00 USD | 9,960.00 USD | 3,660.00 USD | 35,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8620` | 2,290,000.00 USD | 2,290,000.00 USD | 12,920.00 USD | 12,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8630` | 2,420,000.00 USD | 2,420,000.00 USD | 758.91 USD | 2,910.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 389.61 USD | 116,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 2,260,000.00 USD | 2,260,000.00 USD | 48,740.00 USD | 2,370.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 116,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8650` | 2,410,000.00 USD | 2,410,000.00 USD | 47,860.00 USD | 18,930.00 USD | 184.85 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8660` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,390.00 USD | 116,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8670` | 2,340,000.00 USD | 2,340,000.00 USD | 13,660.00 USD | 3,720.00 USD | 12,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8680` | 2,210,000.00 USD | 2,210,000.00 USD | 43,000.00 USD | 9,030.00 USD | 11,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8690` | 2,310,000.00 USD | 2,310,000.00 USD | 160,750.00 USD | 13,110.00 USD | 46,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 12,590.00 USD | 114,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8700` | 2,140,000.00 USD | 2,140,000.00 USD | 49,290.00 USD | 3,880.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8705` | 92,480.00 USD | 102,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8710` | 2,090,000.00 USD | 2,090,000.00 USD | 7,370.00 USD | 23,340.00 USD | 13,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8720` | 2,060,000.00 USD | 2,060,000.00 USD | 30,840.00 USD | 34,140.00 USD | 24,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 8,170.00 USD | 295.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 1,970,000.00 USD | 1,970,000.00 USD | 59,650.00 USD | 12,180.00 USD | 33,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 6,380.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 1,860,000.00 USD | 1,860,000.00 USD | 14,770.00 USD | 5,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 9,560.00 USD | 9,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8770` | 2,030,000.00 USD | 2,030,000.00 USD | 1,390.00 USD | 0.00 USD | 30,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8780` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 76.69 USD | 50,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 1,990,000.00 USD | 1,990,000.00 USD | 873.30 USD | 5,580.00 USD | 53,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8800` | 1,790,000.00 USD | 1,790,000.00 USD | 12,990.00 USD | 57.65 USD | 3,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 1,930,000.00 USD | 1,930,000.00 USD | 1,830.00 USD | 240.78 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8820` | 1,770,000.00 USD | 1,770,000.00 USD | 825.04 USD | 10,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8830` | 1,930,000.00 USD | 1,930,000.00 USD | 2,320.00 USD | 10,140.00 USD | 11,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 1,760,000.00 USD | 1,760,000.00 USD | 1,680.00 USD | 16,790.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8850` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 5,800.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8860` | 1,740,000.00 USD | 1,740,000.00 USD | 66,940.00 USD | 27,710.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8870` | 1,900,000.00 USD | 1,900,000.00 USD | 271,870.00 USD | 22,320.00 USD | 81,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8880` | 1,640,000.00 USD | 1,640,000.00 USD | 74,070.00 USD | 14,120.00 USD | 36,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8890` | 1,520,000.00 USD | 1,520,000.00 USD | 54,380.00 USD | 73,890.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8900` | 1,510,000.00 USD | 1,510,000.00 USD | 2,730.00 USD | 51,760.00 USD | 910.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8910` | 1,380,000.00 USD | 1,380,000.00 USD | 75,300.00 USD | 22,240.00 USD | 34,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8920` | 1,460,000.00 USD | 1,460,000.00 USD | 46,090.00 USD | 32,770.00 USD | 56,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8930` | 1,250,000.00 USD | 1,250,000.00 USD | 62,870.00 USD | 23,560.00 USD | 9,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8940` | 1,320,000.00 USD | 1,320,000.00 USD | 13,790.00 USD | 18,130.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8950` | 1,150,000.00 USD | 1,150,000.00 USD | 7,120.00 USD | 37,670.00 USD | 57,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8960` | 1,290,000.00 USD | 1,290,000.00 USD | 5,530.00 USD | 26,420.00 USD | 5,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8970` | 1,050,000.00 USD | 1,050,000.00 USD | 2,140.00 USD | 4,820.00 USD | 56,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8980` | 1,250,000.00 USD | 1,250,000.00 USD | 1,100.00 USD | 26,840.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8990` | 987,790.00 USD | 987,790.00 USD | 0.00 USD | 34,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9000` | 1,210,000.00 USD | 1,210,000.00 USD | 5,080.00 USD | 15,740.00 USD | 682.73 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9005` | 152.27 USD | 152.27 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9010` | 953,570.00 USD | 953,570.00 USD | 0.00 USD | 48,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9020` | 1,190,000.00 USD | 1,190,000.00 USD | 4,110.00 USD | 11,830.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9030` | 904,730.00 USD | 904,730.00 USD | 0.00 USD | 16,370.00 USD | 23,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9040` | 1,170,000.00 USD | 1,170,000.00 USD | 12,290.00 USD | 22,810.00 USD | 28,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9050` | 864,430.00 USD | 864,430.00 USD | 0.00 USD | 3,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9060` | 1,100,000.00 USD | 1,100,000.00 USD | 30,140.00 USD | 10,280.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9070` | 860,590.00 USD | 860,590.00 USD | 23,910.00 USD | 0.00 USD | 42,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9080` | 1,040,000.00 USD | 1,040,000.00 USD | 20,470.00 USD | 10,040.00 USD | 19,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9100` | 987,540.00 USD | 987,540.00 USD | 8,170.00 USD | 3,480.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9120` | 974,170.00 USD | 974,170.00 USD | 27,150.00 USD | 5,580.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9130` | 794,640.00 USD | 794,640.00 USD | 0.00 USD | 0.00 USD | 20,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9140` | 938,510.00 USD | 938,510.00 USD | 9,600.00 USD | 10,190.00 USD | 28,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9150` | 773,920.00 USD | 773,920.00 USD | 0.00 USD | 515.41 USD | 15,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9160` | 890,560.00 USD | 890,560.00 USD | 1,890.00 USD | 6,570.00 USD | 10,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9170` | 757,720.00 USD | 757,720.00 USD | 0.00 USD | 0.00 USD | 33,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9180` | 871,160.00 USD | 871,160.00 USD | 7,300.00 USD | 5,940.00 USD | 9,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9200` | 848,390.00 USD | 848,390.00 USD | 8,570.00 USD | 11,210.00 USD | 5,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9210` | 724,540.00 USD | 724,540.00 USD | 0.00 USD | 7,760.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9220` | 822,880.00 USD | 822,880.00 USD | 13,740.00 USD | 3,470.00 USD | 877.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9230` | 712,810.00 USD | 712,810.00 USD | 294,370.00 USD | 0.00 USD | 26,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9240` | 804,800.00 USD | 804,800.00 USD | 88,170.00 USD | 20,790.00 USD | 43,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9250` | 391,760.00 USD | 391,760.00 USD | 0.00 USD | 52,780.00 USD | 84,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9260` | 652,250.00 USD | 652,250.00 USD | 35,300.00 USD | 51,770.00 USD | 83,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9270` | 254,910.00 USD | 254,910.00 USD | 44,020.00 USD | 11,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9280` | 481,560.00 USD | 481,560.00 USD | 92,240.00 USD | 12,420.00 USD | 66,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9290` | 199,090.00 USD | 199,090.00 USD | 0.00 USD | 12,750.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9300` | 310,340.00 USD | 310,340.00 USD | 5,140.00 USD | 15,160.00 USD | 3,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9320` | 286,200.00 USD | 286,200.00 USD | 7,440.00 USD | 7,530.00 USD | 20,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9330` | 184,740.00 USD | 184,740.00 USD | 37,450.00 USD | 0.00 USD | 31,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9340` | 251,070.00 USD | 251,070.00 USD | 88,620.00 USD | 23,180.00 USD | 38,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9350` | 115,920.00 USD | 115,920.00 USD | 0.00 USD | 11,160.00 USD | 20,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9360` | 100,470.00 USD | 100,470.00 USD | 52,220.00 USD | 15,760.00 USD | 18,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9370` | 84,400.00 USD | 84,400.00 USD | 16,340.00 USD | 19,540.00 USD | 48,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9380` | 13,720.00 USD | 13,720.00 USD | 0.00 USD | 103.28 USD | 13,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9390` | 74,160.00 USD | 74,160.00 USD | 39,250.00 USD | 0.00 USD | 34,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9400` | 2,560.00 USD | 2,560.00 USD | 2,020.00 USD | 548.70 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9410` | 237,210.00 USD | 237,210.00 USD | 161,930.00 USD | 1,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9420` | 3,800.00 USD | 3,800.00 USD | 1,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9440` | 4,020.00 USD | 4,020.00 USD | 0.00 USD | 224.96 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 261,500.00 USD | 261,500.00 USD | 0.00 USD | 20,890.00 USD | 3,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 4,300.00 USD | 4,300.00 USD | 0.00 USD | 199.60 USD | 79.38 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 348,010.00 USD | 348,010.00 USD | 3,540.00 USD | 6,380.00 USD | 76,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9480` | 6,270.00 USD | 6,270.00 USD | 1,790.00 USD | 0.00 USD | 176.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 431,950.00 USD | 431,950.00 USD | 2,770.00 USD | 10,340.00 USD | 70,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 86,450.00 USD | 86,450.00 USD | 80,090.00 USD | 85.68 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 723,340.00 USD | 723,340.00 USD | 258,650.00 USD | 28,180.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 87,800.00 USD | 87,800.00 USD | 0.00 USD | 1,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 731,580.00 USD | 731,580.00 USD | 0.00 USD | 8,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 105,670.00 USD | 105,670.00 USD | 10,150.00 USD | 7,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 751,310.00 USD | 751,310.00 USD | 0.00 USD | 19,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 146,030.00 USD | 146,030.00 USD | 18,010.00 USD | 20,990.00 USD | 1,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 764,470.00 USD | 764,470.00 USD | 1,910.00 USD | 10,300.00 USD | 957.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 164,910.00 USD | 164,910.00 USD | 7,260.00 USD | 9,120.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 785,540.00 USD | 785,540.00 USD | 1,980.00 USD | 18,220.00 USD | 866.69 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 192,820.00 USD | 192,820.00 USD | 17,180.00 USD | 8,190.00 USD | 2,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9610` | 810,930.00 USD | 810,930.00 USD | 24,370.00 USD | 0.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 354,820.00 USD | 354,820.00 USD | 81,730.00 USD | 20,070.00 USD | 60,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 983,460.00 USD | 983,460.00 USD | 56,160.00 USD | 31,820.00 USD | 84,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 532,330.00 USD | 532,330.00 USD | 53,800.00 USD | 43,860.00 USD | 79,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 1,090,000.00 USD | 1,090,000.00 USD | 97,600.00 USD | 0.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 599,750.00 USD | 599,750.00 USD | 16,900.00 USD | 13,350.00 USD | 37,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9670` | 1,140,000.00 USD | 1,140,000.00 USD | 40,070.00 USD | 5,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9680` | 665,880.00 USD | 665,880.00 USD | 44,230.00 USD | 17,940.00 USD | 3,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 21,100.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 736,890.00 USD | 736,890.00 USD | 16,500.00 USD | 11,640.00 USD | 42,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 18,250.00 USD | 31,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 842,310.00 USD | 842,310.00 USD | 31,880.00 USD | 8,520.00 USD | 65,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 1,280,000.00 USD | 1,280,000.00 USD | 2,910.00 USD | 9,290.00 USD | 27,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 908,520.00 USD | 908,520.00 USD | 29,450.00 USD | 8,140.00 USD | 28,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 1,350,000.00 USD | 1,350,000.00 USD | 2,090.00 USD | 17,230.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 1,010,000.00 USD | 1,010,000.00 USD | 54,930.00 USD | 27,390.00 USD | 20,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 1,450,000.00 USD | 1,450,000.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 1,080,000.00 USD | 1,080,000.00 USD | 44,310.00 USD | 4,920.00 USD | 18,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 3,880.00 USD | 85,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 1,160,000.00 USD | 1,160,000.00 USD | 38,280.00 USD | 11,420.00 USD | 31,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9810` | 1,660,000.00 USD | 1,660,000.00 USD | 540.00 USD | 4,020.00 USD | 119,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 1,240,000.00 USD | 1,240,000.00 USD | 32,680.00 USD | 21,930.00 USD | 24,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 1,900,000.00 USD | 1,900,000.00 USD | 124,720.00 USD | 15,810.00 USD | 94,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 1,330,000.00 USD | 1,330,000.00 USD | 13,910.00 USD | 16,870.00 USD | 58,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 211.77 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 1,420,000.00 USD | 1,420,000.00 USD | 59,170.00 USD | 7,150.00 USD | 26,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 2,030,000.00 USD | 2,030,000.00 USD | 40,020.00 USD | 0.00 USD | 67,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9880` | 1,460,000.00 USD | 1,460,000.00 USD | 17,200.00 USD | 3,710.00 USD | 17,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9890` | 2,050,000.00 USD | 2,050,000.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 1,570,000.00 USD | 1,570,000.00 USD | 66,490.00 USD | 7,820.00 USD | 33,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9910` | 2,090,000.00 USD | 2,090,000.00 USD | 3,700.00 USD | 800.44 USD | 35,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 1,610,000.00 USD | 1,610,000.00 USD | 12,580.00 USD | 5,030.00 USD | 31,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9930` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 36,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 1,650,000.00 USD | 1,650,000.00 USD | 25,660.00 USD | 1,250.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9950` | 2,250,000.00 USD | 2,250,000.00 USD | 63,060.00 USD | 5,380.00 USD | 58,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 1,680,000.00 USD | 1,680,000.00 USD | 19,070.00 USD | 3,600.00 USD | 7,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 2,350,000.00 USD | 2,350,000.00 USD | 95,130.00 USD | 253.35 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 1,760,000.00 USD | 1,760,000.00 USD | 54,550.00 USD | 10,730.00 USD | 15,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9985` | 852.22 USD | 1,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9990` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 6,490.00 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,840,000.00 USD | 1,840,000.00 USD | 49,260.00 USD | 18,230.00 USD | 6,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,410,000.00 USD | 2,410,000.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,860,000.00 USD | 1,860,000.00 USD | 16,910.00 USD | 2,030.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,560,000.00 USD | 2,560,000.00 USD | 107,670.00 USD | 21,850.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,890,000.00 USD | 1,890,000.00 USD | 10,790.00 USD | 9,550.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,610,000.00 USD | 2,610,000.00 USD | 32,430.00 USD | 3,970.00 USD | 12,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,030,000.00 USD | 2,030,000.00 USD | 103,670.00 USD | 10,200.00 USD | 25,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 4,000.00 USD | 5,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,670,000.00 USD | 2,670,000.00 USD | 35,710.00 USD | 240.78 USD | 29,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,100,000.00 USD | 2,100,000.00 USD | 23,240.00 USD | 9,330.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,700,000.00 USD | 2,700,000.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,130,000.00 USD | 2,130,000.00 USD | 12,560.00 USD | 17,230.00 USD | 971.85 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,740,000.00 USD | 2,740,000.00 USD | 20,090.00 USD | 17,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,160,000.00 USD | 2,160,000.00 USD | 16,880.00 USD | 15,730.00 USD | 265.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,790,000.00 USD | 2,790,000.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,190,000.00 USD | 2,190,000.00 USD | 7,030.00 USD | 5,790.00 USD | 15,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 26,510.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,230,000.00 USD | 2,230,000.00 USD | 9,410.00 USD | 22,350.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,870,000.00 USD | 2,870,000.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,270,000.00 USD | 2,270,000.00 USD | 26,110.00 USD | 2,060.00 USD | 12,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 2,980,000.00 USD | 2,980,000.00 USD | 17,960.00 USD | 83,360.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,340,000.00 USD | 2,340,000.00 USD | 40,010.00 USD | 9,980.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,150,000.00 USD | 3,150,000.00 USD | 61,450.00 USD | 32,840.00 USD | 68,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,420,000.00 USD | 2,420,000.00 USD | 31,700.00 USD | 17,830.00 USD | 27,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,460,000.00 USD | 3,460,000.00 USD | 82,230.00 USD | 86,210.00 USD | 146,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,500,000.00 USD | 2,500,000.00 USD | 41,760.00 USD | 8,850.00 USD | 34,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,570,000.00 USD | 3,570,000.00 USD | 28,320.00 USD | 48,490.00 USD | 37,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,570,000.00 USD | 2,570,000.00 USD | 36,010.00 USD | 18,210.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 3,890,000.00 USD | 3,890,000.00 USD | 161,070.00 USD | 127,000.00 USD | 25,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,610,000.00 USD | 2,610,000.00 USD | 14,780.00 USD | 8,920.00 USD | 15,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,100,000.00 USD | 4,100,000.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,710,000.00 USD | 2,710,000.00 USD | 65,560.00 USD | 13,340.00 USD | 18,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,300,000.00 USD | 4,300,000.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,780,000.00 USD | 2,780,000.00 USD | 30,500.00 USD | 7,820.00 USD | 32,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,430,000.00 USD | 4,430,000.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,820,000.00 USD | 2,820,000.00 USD | 13,500.00 USD | 9,390.00 USD | 13,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,740,000.00 USD | 4,740,000.00 USD | 259,060.00 USD | 8,290.00 USD | 43,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,840,000.00 USD | 2,840,000.00 USD | 4,560.00 USD | 11,000.00 USD | 6,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,040,000.00 USD | 5,040,000.00 USD | 193,150.00 USD | 3,330.00 USD | 109,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,900,000.00 USD | 2,900,000.00 USD | 45,570.00 USD | 3,700.00 USD | 8,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,430,000.00 USD | 5,430,000.00 USD | 239,580.00 USD | 9,010.00 USD | 134,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,930,000.00 USD | 2,930,000.00 USD | 9,270.00 USD | 6,500.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,870,000.00 USD | 5,870,000.00 USD | 285,690.00 USD | 2,090.00 USD | 159,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,950,000.00 USD | 2,950,000.00 USD | 12,870.00 USD | 7,160.00 USD | 3,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,070,000.00 USD | 6,070,000.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,970,000.00 USD | 2,970,000.00 USD | 3,600.00 USD | 1,900.00 USD | 11,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,340,000.00 USD | 6,340,000.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 2,980,000.00 USD | 2,980,000.00 USD | 5,850.00 USD | 5,000.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 6,860,000.00 USD | 6,860,000.00 USD | 178,890.00 USD | 96,370.00 USD | 244,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 367.04 USD | 5,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,000,000.00 USD | 3,000,000.00 USD | 3,870.00 USD | 900.45 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,070,000.00 USD | 7,070,000.00 USD | 116,030.00 USD | 13,780.00 USD | 77,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,040,000.00 USD | 3,040,000.00 USD | 29,490.00 USD | 4,070.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,380,000.00 USD | 7,380,000.00 USD | 175,350.00 USD | 43,690.00 USD | 96,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,060,000.00 USD | 3,060,000.00 USD | 4,540.00 USD | 937.66 USD | 16,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,060,000.00 USD | 3,060,000.00 USD | 4,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,580,000.00 USD | 7,580,000.00 USD | 68,010.00 USD | 58,070.00 USD | 74,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,810,000.00 USD | 7,810,000.00 USD | 121,450.00 USD | 33,860.00 USD | 72,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,210,000.00 USD | 8,210,000.00 USD | 218,860.00 USD | 70,160.00 USD | 106,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,660,000.00 USD | 8,660,000.00 USD | 239,650.00 USD | 74,380.00 USD | 145,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,940,000.00 USD | 8,940,000.00 USD | 138,520.00 USD | 56,310.00 USD | 78,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,220,000.00 USD | 9,220,000.00 USD | 140,500.00 USD | 73,690.00 USD | 71,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,420,000.00 USD | 9,420,000.00 USD | 74,870.00 USD | 27,820.00 USD | 91,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 9,500,000.00 USD | 9,500,000.00 USD | 60,290.00 USD | 26,450.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.1945` | 463,720.00 USD | 0.00 USD | 333.66 USD | `-79.23%` | `1,715.50` |
| `Live` | `Long` | `0.2135` | 463,390.00 USD | 0.00 USD | 106.75 USD | `-77.21%` | `500.00` |
| `Live` | `Long` | `0.2735` | 463,280.00 USD | 0.00 USD | 173.02 USD | `-70.80%` | `632.60` |
| `Live` | `Long` | `0.3635` | 463,110.00 USD | 0.00 USD | 802.97 USD | `-61.19%` | `2,209.00` |
| `Live` | `Long` | `0.4195` | 462,300.00 USD | 0.00 USD | 2,800.00 USD | `-55.21%` | `6,675.20` |
| `Live` | `Long` | `0.4235` | 459,500.00 USD | 0.00 USD | 2,410.00 USD | `-54.78%` | `5,698.80` |
| `Live` | `Long` | `0.4645` | 457,090.00 USD | 0.00 USD | 1,220.00 USD | `-50.41%` | `2,618.10` |
| `Live` | `Long` | `0.4665` | 455,870.00 USD | 0.00 USD | 547.81 USD | `-50.19%` | `1,174.30` |
| `Live` | `Long` | `0.4685` | 455,330.00 USD | 0.00 USD | 147.02 USD | `-49.98%` | `313.80` |
| `Live` | `Long` | `0.4705` | 455,180.00 USD | 0.00 USD | 2,590.00 USD | `-49.77%` | `5,500.00` |
| `Live` | `Long` | `0.5025` | 452,590.00 USD | 0.00 USD | 201.35 USD | `-46.35%` | `400.70` |
| `Live` | `Long` | `0.5065` | 452,390.00 USD | 0.00 USD | 3,290.00 USD | `-45.92%` | `6,504.70` |
| `Live` | `Long` | `0.5355` | 449,100.00 USD | 0.00 USD | 535.50 USD | `-42.83%` | `1,000.00` |
| `Live` | `Long` | `0.5655` | 448,560.00 USD | 0.00 USD | 14,600.00 USD | `-39.62%` | `25,816.60` |
| `Live` | `Long` | `0.5695` | 433,960.00 USD | 0.00 USD | 577.36 USD | `-39.20%` | `1,013.80` |
| `Live` | `Long` | `0.5845` | 433,380.00 USD | 0.00 USD | 683.51 USD | `-37.59%` | `1,169.40` |
| `Live` | `Long` | `0.5895` | 432,700.00 USD | 0.00 USD | 137.53 USD | `-37.06%` | `233.30` |
| `Live` | `Long` | `0.5915` | 432,560.00 USD | 0.00 USD | 234.53 USD | `-36.85%` | `396.50` |
| `Live` | `Long` | `0.6055` | 432,330.00 USD | 0.00 USD | 1,480.00 USD | `-35.35%` | `2,448.50` |
| `Live` | `Long` | `0.6075` | 430,850.00 USD | 0.00 USD | 1,810.00 USD | `-35.14%` | `2,971.80` |
| `Live` | `Long` | `0.6125` | 429,040.00 USD | 0.00 USD | 105.96 USD | `-34.61%` | `173.00` |
| `Live` | `Long` | `0.6145` | 428,930.00 USD | 0.00 USD | 147.48 USD | `-34.39%` | `240.00` |
| `Live` | `Long` | `0.6295` | 428,790.00 USD | 0.00 USD | 220.32 USD | `-32.79%` | `350.00` |
| `Live` | `Long` | `0.6315` | 428,570.00 USD | 0.00 USD | 757.80 USD | `-32.58%` | `1,200.00` |
| `Live` | `Long` | `0.6355` | 427,810.00 USD | 0.00 USD | 106.00 USD | `-32.15%` | `166.80` |
| `Live` | `Long` | `0.6365` | 427,700.00 USD | 0.00 USD | 507.86 USD | `-32.04%` | `797.90` |
| `Live` | `Long` | `0.6405` | 427,190.00 USD | 0.00 USD | 2,090.00 USD | `-31.62%` | `3,262.00` |
| `Live` | `Long` | `0.6415` | 425,110.00 USD | 0.00 USD | 20,270.00 USD | `-31.51%` | `31,595.60` |
| `Live` | `Long` | `0.6465` | 404,840.00 USD | 0.00 USD | 4,230.00 USD | `-30.98%` | `6,539.70` |
| `Live` | `Long` | `0.6475` | 400,610.00 USD | 0.00 USD | 202.47 USD | `-30.87%` | `312.70` |
| `Live` | `Long` | `0.6595` | 400,410.00 USD | 0.00 USD | 149.44 USD | `-29.59%` | `226.60` |
| `Live` | `Long` | `0.6725` | 400,260.00 USD | 0.00 USD | 63,890.00 USD | `-28.20%` | `95,000.00` |
| `Live` | `Long` | `0.6755` | 336,370.00 USD | 0.00 USD | 84,440.00 USD | `-27.88%` | `125,000.00` |
| `Live` | `Long` | `0.6775` | 251,930.00 USD | 0.00 USD | 423.10 USD | `-27.67%` | `624.50` |
| `Live` | `Long` | `0.6835` | 251,510.00 USD | 0.00 USD | 512.97 USD | `-27.02%` | `750.50` |
| `Live` | `Long` | `0.6915` | 251,000.00 USD | 0.00 USD | 19,800.00 USD | `-26.17%` | `28,635.00` |
| `Live` | `Long` | `0.6965` | 231,190.00 USD | 0.00 USD | 322.62 USD | `-25.64%` | `463.20` |
| `Live` | `Long` | `0.7005` | 230,870.00 USD | 0.00 USD | 1,140.00 USD | `-25.21%` | `1,634.20` |
| `Live` | `Long` | `0.7135` | 229,730.00 USD | 0.00 USD | 159.40 USD | `-23.82%` | `223.40` |
| `Live` | `Long` | `0.7145` | 229,570.00 USD | 0.00 USD | 988.87 USD | `-23.72%` | `1,384.00` |
| `Live` | `Long` | `0.7215` | 228,580.00 USD | 0.00 USD | 1,580.00 USD | `-22.97%` | `2,190.90` |
| `Live` | `Long` | `0.7235` | 227,000.00 USD | 0.00 USD | 397.93 USD | `-22.75%` | `550.00` |
| `Live` | `Long` | `0.7295` | 226,600.00 USD | 0.00 USD | 291.58 USD | `-22.11%` | `399.70` |
| `Live` | `Long` | `0.7305` | 226,310.00 USD | 0.00 USD | 2,300.00 USD | `-22.01%` | `3,143.00` |
| `Live` | `Long` | `0.7335` | 224,010.00 USD | 0.00 USD | 1,140.00 USD | `-21.69%` | `1,557.80` |
| `Live` | `Long` | `0.7395` | 222,870.00 USD | 0.00 USD | 283.30 USD | `-21.05%` | `383.10` |
| `Live` | `Long` | `0.7515` | 222,590.00 USD | 0.00 USD | 32,890.00 USD | `-19.76%` | `43,766.90` |
| `Live` | `Long` | `0.7525` | 189,700.00 USD | 0.00 USD | 2,220.00 USD | `-19.66%` | `2,947.70` |
| `Live` | `Long` | `0.7535` | 187,480.00 USD | 0.00 USD | 1,140.00 USD | `-19.55%` | `1,516.30` |
| `Live` | `Long` | `0.7555` | 186,340.00 USD | 0.00 USD | 144.07 USD | `-19.34%` | `190.70` |
| `Live` | `Long` | `0.7565` | 186,190.00 USD | 0.00 USD | 8,860.00 USD | `-19.23%` | `11,712.10` |
| `Live` | `Long` | `0.7595` | 177,330.00 USD | 0.00 USD | 53,930.00 USD | `-18.91%` | `71,003.30` |
| `Live` | `Long` | `0.7635` | 123,400.00 USD | 0.00 USD | 308.00 USD | `-18.48%` | `403.40` |
| `Live` | `Long` | `0.7705` | 123,100.00 USD | 0.00 USD | 152.94 USD | `-17.74%` | `198.50` |
| `Live` | `Long` | `0.7725` | 122,940.00 USD | 0.00 USD | 3,840.00 USD | `-17.52%` | `4,968.90` |
| `Live` | `Long` | `0.7775` | 119,100.00 USD | 0.00 USD | 2,490.00 USD | `-16.99%` | `3,199.30` |
| `Live` | `Long` | `0.7865` | 116,620.00 USD | 0.00 USD | 156.51 USD | `-16.03%` | `199.00` |
| `Live` | `Long` | `0.7905` | 116,460.00 USD | 0.00 USD | 277.39 USD | `-15.60%` | `350.90` |
| `Live` | `Long` | `0.7935` | 116,180.00 USD | 0.00 USD | 1,760.00 USD | `-15.28%` | `2,214.10` |
| `Live` | `Long` | `0.7985` | 114,430.00 USD | 0.00 USD | 210.40 USD | `-14.75%` | `263.50` |
| `Live` | `Long` | `0.8135` | 114,220.00 USD | 0.00 USD | 647.79 USD | `-13.15%` | `796.30` |
| `Live` | `Long` | `0.8215` | 113,570.00 USD | 0.00 USD | 1,950.00 USD | `-12.29%` | `2,370.70` |
| `Live` | `Long` | `0.8235` | 111,620.00 USD | 0.00 USD | 749.96 USD | `-12.08%` | `910.70` |
| `Live` | `Long` | `0.8365` | 110,870.00 USD | 0.00 USD | 316.70 USD | `-10.69%` | `378.60` |
| `Live` | `Long` | `0.8415` | 110,550.00 USD | 0.00 USD | 1,570.00 USD | `-10.16%` | `1,862.40` |
| `Live` | `Long` | `0.8495` | 108,990.00 USD | 0.00 USD | 1,260.00 USD | `-9.30%` | `1,486.90` |
| `Live` | `Long` | `0.8575` | 107,720.00 USD | 0.00 USD | 620.32 USD | `-8.45%` | `723.40` |
| `Live` | `Long` | `0.8635` | 107,100.00 USD | 0.00 USD | 208.02 USD | `-7.81%` | `240.90` |
| `Live` | `Long` | `0.8645` | 106,900.00 USD | 0.00 USD | 438.30 USD | `-7.70%` | `507.00` |
| `Live` | `Long` | `0.8665` | 106,460.00 USD | 0.00 USD | 1,390.00 USD | `-7.49%` | `1,606.10` |
| `Live` | `Long` | `0.8695` | 105,070.00 USD | 0.00 USD | 12,590.00 USD | `-7.17%` | `14,478.80` |
| `Live` | `Long` | `0.8705` | 92,480.00 USD | 0.00 USD | 92,480.00 USD | `-7.06%` | `106,233.40` |
| `Live` | `Short` | `0.8925` | 665.36 USD | 665.36 USD | 0.00 USD | `-4.71%` | `745.50` |
| `Live` | `Short` | `0.9925` | 4,610.00 USD | 3,940.00 USD | 0.00 USD | `+5.97%` | `3,970.40` |
| `Live` | `Short` | `0.9985` | 5,460.00 USD | 852.22 USD | 0.00 USD | `+6.61%` | `853.50` |
| `Live` | `Short` | `1.03` | 5,610.00 USD | 152.32 USD | 0.00 USD | `+9.81%` | `148.10` |
| `Live` | `Short` | `1.05` | 5,980.00 USD | 367.04 USD | 0.00 USD | `+11.84%` | `350.40` |
| `Live` | `Short` | `1.08` | 8,210.00 USD | 2,230.00 USD | 0.00 USD | `+15.47%` | `2,064.20` |
| `Live` | `Short` | `1.11` | 8,380.00 USD | 170.02 USD | 0.00 USD | `+18.56%` | `153.10` |
| `Live` | `Short` | `1.15` | 22,130.00 USD | 13,750.00 USD | 0.00 USD | `+22.62%` | `11,969.90` |
| `Live` | `Short` | `1.31` | 22,250.00 USD | 126.85 USD | 0.00 USD | `+40.35%` | `96.50` |
| `Live` | `Short` | `1.32` | 33,980.00 USD | 11,730.00 USD | 0.00 USD | `+41.31%` | `8,862.90` |
| `Live` | `Short` | `1.34` | 34,220.00 USD | 239.77 USD | 0.00 USD | `+43.01%` | `179.00` |
| `Live` | `Short` | `1.38` | 38,120.00 USD | 3,900.00 USD | 0.00 USD | `+46.86%` | `2,834.10` |
| `Live` | `Short` | `1.42` | 41,320.00 USD | 3,200.00 USD | 0.00 USD | `+51.66%` | `2,249.30` |
| `Live` | `Short` | `1.54` | 41,440.00 USD | 122.39 USD | 0.00 USD | `+64.37%` | `79.50` |
| `Live` | `Short` | `1.54` | 41,620.00 USD | 176.42 USD | 0.00 USD | `+64.79%` | `114.30` |
| `Live` | `Short` | `1.56` | 43,420.00 USD | 1,810.00 USD | 0.00 USD | `+66.18%` | `1,161.90` |
| `Live` | `Short` | `1.59` | 44,220.00 USD | 795.79 USD | 0.00 USD | `+70.13%` | `499.40` |
| `Live` | `Short` | `1.63` | 46,660.00 USD | 2,440.00 USD | 0.00 USD | `+73.55%` | `1,500.00` |
| `Live` | `Short` | `1.64` | 46,900.00 USD | 240.59 USD | 0.00 USD | `+75.58%` | `146.30` |
| `Live` | `Short` | `1.65` | 55,140.00 USD | 8,240.00 USD | 0.00 USD | `+75.90%` | `5,000.00` |
| `Live` | `Short` | `1.67` | 55,440.00 USD | 300.15 USD | 0.00 USD | `+78.03%` | `180.00` |
| `Live` | `Short` | `1.68` | 56,060.00 USD | 621.35 USD | 0.00 USD | `+79.10%` | `370.40` |
| `Live` | `Short` | `1.68` | 56,380.00 USD | 322.10 USD | 0.00 USD | `+79.21%` | `191.90` |
| `Live` | `Short` | `1.73` | 56,570.00 USD | 190.42 USD | 0.00 USD | `+84.65%` | `110.10` |
| `Live` | `Short` | `1.74` | 69,710.00 USD | 13,140.00 USD | 0.00 USD | `+85.40%` | `7,569.10` |
| `Live` | `Short` | `1.77` | 70,100.00 USD | 380.81 USD | 0.00 USD | `+89.46%` | `214.60` |
| `Live` | `Short` | `1.80` | 159,440.00 USD | 89,340.00 USD | 0.00 USD | `+91.70%` | `49,759.80` |
| `Live` | `Short` | `1.86` | 159,650.00 USD | 208.37 USD | 0.00 USD | `+98.11%` | `112.30` |
| `Live` | `Short` | `1.86` | 183,680.00 USD | 24,030.00 USD | 0.00 USD | `+98.64%` | `12,916.90` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.4015` | 366,680.00 USD | 0.00 USD | 120.45 USD | `-57.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 366,560.00 USD | 0.00 USD | 150.15 USD | `-46.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5435` | 366,410.00 USD | 0.00 USD | 186.15 USD | `-41.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 366,230.00 USD | 0.00 USD | 1,150.00 USD | `-30.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 365,080.00 USD | 0.00 USD | 781.90 USD | `-25.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 364,300.00 USD | 0.00 USD | 477.38 USD | `-24.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 363,820.00 USD | 0.00 USD | 341.33 USD | `-23.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 363,480.00 USD | 0.00 USD | 972.82 USD | `-23.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 362,500.00 USD | 0.00 USD | 160.20 USD | `-22.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7385` | 362,340.00 USD | 0.00 USD | 102.58 USD | `-21.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 362,240.00 USD | 0.00 USD | 289.49 USD | `-20.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7615` | 361,950.00 USD | 0.00 USD | 197.53 USD | `-18.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 361,750.00 USD | 0.00 USD | 14,570.00 USD | `-16.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 347,190.00 USD | 0.00 USD | 213.58 USD | `-16.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 346,970.00 USD | 0.00 USD | 274,830.00 USD | `-14.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 72,140.00 USD | 0.00 USD | 108.47 USD | `-14.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8025` | 72,030.00 USD | 0.00 USD | 2,010.00 USD | `-14.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 70,020.00 USD | 0.00 USD | 326.96 USD | `-13.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 69,690.00 USD | 0.00 USD | 405.75 USD | `-13.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 69,290.00 USD | 0.00 USD | 772.84 USD | `-10.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8415` | 68,510.00 USD | 0.00 USD | 2,670.00 USD | `-10.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8495` | 65,840.00 USD | 0.00 USD | 3,470.00 USD | `-9.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 62,370.00 USD | 0.00 USD | 9,180.00 USD | `-9.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 53,190.00 USD | 0.00 USD | 341.94 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 52,850.00 USD | 0.00 USD | 1,150.00 USD | `-8.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 51,700.00 USD | 0.00 USD | 429.25 USD | `-8.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 51,270.00 USD | 0.00 USD | 223.30 USD | `-8.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 51,050.00 USD | 0.00 USD | 518.51 USD | `-7.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 50,530.00 USD | 0.00 USD | 128.39 USD | `-7.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 50,400.00 USD | 0.00 USD | 1,280.00 USD | `-7.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 49,120.00 USD | 0.00 USD | 205.24 USD | `-6.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 48,920.00 USD | 0.00 USD | 649.66 USD | `-6.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 48,270.00 USD | 0.00 USD | 194.06 USD | `-5.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8845` | 48,080.00 USD | 0.00 USD | 193.35 USD | `-5.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 47,880.00 USD | 0.00 USD | 223.04 USD | `-5.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 47,660.00 USD | 0.00 USD | 10,840.00 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 36,810.00 USD | 0.00 USD | 4,920.00 USD | `-5.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8915` | 31,900.00 USD | 0.00 USD | 121.15 USD | `-4.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 31,780.00 USD | 0.00 USD | 192.07 USD | `-4.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 31,580.00 USD | 0.00 USD | 195.32 USD | `-4.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8965` | 31,390.00 USD | 0.00 USD | 196.87 USD | `-4.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8985` | 31,190.00 USD | 0.00 USD | 2,870.00 USD | `-4.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9005` | 28,320.00 USD | 0.00 USD | 319.05 USD | `-3.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9025` | 28,000.00 USD | 0.00 USD | 398.91 USD | `-3.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9035` | 27,600.00 USD | 0.00 USD | 196.96 USD | `-3.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9045` | 27,400.00 USD | 0.00 USD | 300.38 USD | `-3.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9065` | 27,100.00 USD | 0.00 USD | 198.61 USD | `-3.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9075` | 26,900.00 USD | 0.00 USD | 994.35 USD | `-3.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 25,910.00 USD | 0.00 USD | 363.40 USD | `-3.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9095` | 25,550.00 USD | 0.00 USD | 1,810.00 USD | `-2.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9115` | 23,740.00 USD | 0.00 USD | 397.23 USD | `-2.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9135` | 23,340.00 USD | 0.00 USD | 398.65 USD | `-2.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9145` | 22,940.00 USD | 0.00 USD | 399.09 USD | `-2.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9155` | 22,550.00 USD | 0.00 USD | 403.92 USD | `-2.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9165` | 22,140.00 USD | 0.00 USD | 198.06 USD | `-2.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9175` | 21,940.00 USD | 0.00 USD | 223.78 USD | `-2.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9185` | 21,720.00 USD | 0.00 USD | 899.85 USD | `-1.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9195` | 20,820.00 USD | 0.00 USD | 900.19 USD | `-1.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 19,920.00 USD | 0.00 USD | 2,920.00 USD | `-1.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9215` | 17,000.00 USD | 0.00 USD | 104.68 USD | `-1.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9225` | 16,890.00 USD | 0.00 USD | 201.94 USD | `-1.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9235` | 16,690.00 USD | 0.00 USD | 1,080.00 USD | `-1.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9245` | 15,600.00 USD | 0.00 USD | 201.45 USD | `-1.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9255` | 15,400.00 USD | 0.00 USD | 817.40 USD | `-1.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9265` | 14,590.00 USD | 0.00 USD | 403.77 USD | `-1.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9275` | 14,180.00 USD | 0.00 USD | 2,120.00 USD | `-0.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9285` | 12,060.00 USD | 0.00 USD | 246.05 USD | `-0.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9295` | 11,820.00 USD | 0.00 USD | 407.49 USD | `-0.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9305` | 11,410.00 USD | 0.00 USD | 203.97 USD | `-0.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9315` | 11,210.00 USD | 0.00 USD | 263.80 USD | `-0.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9325` | 10,940.00 USD | 0.00 USD | 241.98 USD | `-0.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9335` | 10,700.00 USD | 0.00 USD | 814.76 USD | `-0.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9355` | 9,890.00 USD | 0.00 USD | 201.97 USD | `-0.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9365` | 9,680.00 USD | 0.00 USD | 9,680.00 USD | `-0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 416.01 USD | 416.01 USD | 0.00 USD | `+0.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 971.19 USD | 555.18 USD | 0.00 USD | `+0.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9415` | 1,970.00 USD | 997.80 USD | 0.00 USD | `+0.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 2,790.00 USD | 816.96 USD | 0.00 USD | `+0.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 3,120.00 USD | 334.28 USD | 0.00 USD | `+0.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 30,540.00 USD | 27,420.00 USD | 0.00 USD | `+0.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 30,920.00 USD | 383.87 USD | 0.00 USD | `+0.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 31,540.00 USD | 623.93 USD | 0.00 USD | `+1.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 60,480.00 USD | 28,930.00 USD | 0.00 USD | `+1.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 60,890.00 USD | 414.68 USD | 0.00 USD | `+1.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9525` | 61,270.00 USD | 381.00 USD | 0.00 USD | `+1.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 63,290.00 USD | 2,020.00 USD | 0.00 USD | `+1.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 67,080.00 USD | 3,790.00 USD | 0.00 USD | `+2.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 67,320.00 USD | 236.26 USD | 0.00 USD | `+2.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 67,460.00 USD | 136.83 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 67,860.00 USD | 403.41 USD | 0.00 USD | `+2.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 69,770.00 USD | 1,910.00 USD | 0.00 USD | `+2.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 70,330.00 USD | 568.75 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 70,700.00 USD | 364.58 USD | 0.00 USD | `+2.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 71,520.00 USD | 824.91 USD | 0.00 USD | `+3.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 71,910.00 USD | 385.74 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 73,940.00 USD | 2,030.00 USD | 0.00 USD | `+3.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 74,200.00 USD | 262.52 USD | 0.00 USD | `+3.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 74,590.00 USD | 387.83 USD | 0.00 USD | `+3.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 75,420.00 USD | 830.10 USD | 0.00 USD | `+3.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 97,390.00 USD | 21,960.00 USD | 0.00 USD | `+4.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 97,780.00 USD | 396.17 USD | 0.00 USD | `+4.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 98,460.00 USD | 676.53 USD | 0.00 USD | `+4.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 106,810.00 USD | 8,350.00 USD | 0.00 USD | `+4.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 108,840.00 USD | 2,030.00 USD | 0.00 USD | `+4.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 109,180.00 USD | 346.13 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 109,440.00 USD | 255.38 USD | 0.00 USD | `+5.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 109,660.00 USD | 223.91 USD | 0.00 USD | `+5.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9865` | 109,770.00 USD | 109.99 USD | 0.00 USD | `+5.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 113,290.00 USD | 3,520.00 USD | 0.00 USD | `+5.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 145,050.00 USD | 31,750.00 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 145,450.00 USD | 403.06 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 145,850.00 USD | 403.28 USD | 0.00 USD | `+6.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 151,000.00 USD | 5,140.00 USD | 0.00 USD | `+6.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 188,300.00 USD | 37,310.00 USD | 0.00 USD | `+6.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 188,800.00 USD | 500.25 USD | 0.00 USD | `+6.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 229,400.00 USD | 40,590.00 USD | 0.00 USD | `+6.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 229,630.00 USD | 235.79 USD | 0.00 USD | `+7.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 230,980.00 USD | 1,340.00 USD | 0.00 USD | `+7.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 231,210.00 USD | 230.39 USD | 0.00 USD | `+7.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 231,340.00 USD | 127.65 USD | 0.00 USD | `+7.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 231,550.00 USD | 218.64 USD | 0.00 USD | `+7.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 231,960.00 USD | 409.86 USD | 0.00 USD | `+7.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 232,080.00 USD | 110.95 USD | 0.00 USD | `+7.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 232,690.00 USD | 615.60 USD | 0.00 USD | `+8.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 233,250.00 USD | 561.17 USD | 0.00 USD | `+8.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 233,470.00 USD | 214.40 USD | 0.00 USD | `+8.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 233,720.00 USD | 249.88 USD | 0.00 USD | `+9.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 233,920.00 USD | 207.97 USD | 0.00 USD | `+9.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 234,130.00 USD | 208.26 USD | 0.00 USD | `+10.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 234,650.00 USD | 516.75 USD | 0.00 USD | `+10.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 235,000.00 USD | 348.86 USD | 0.00 USD | `+10.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 235,390.00 USD | 391.80 USD | 0.00 USD | `+10.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 235,800.00 USD | 413.76 USD | 0.00 USD | `+10.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 236,160.00 USD | 354.91 USD | 0.00 USD | `+11.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 238,060.00 USD | 1,900.00 USD | 0.00 USD | `+11.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 238,270.00 USD | 207.87 USD | 0.00 USD | `+11.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 238,480.00 USD | 207.97 USD | 0.00 USD | `+11.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 238,590.00 USD | 107.99 USD | 0.00 USD | `+12.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 313,420.00 USD | 74,840.00 USD | 0.00 USD | `+13.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 315,590.00 USD | 2,170.00 USD | 0.00 USD | `+16.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 317,130.00 USD | 1,540.00 USD | 0.00 USD | `+16.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 327,060.00 USD | 9,930.00 USD | 0.00 USD | `+16.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 327,930.00 USD | 877.63 USD | 0.00 USD | `+18.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 328,110.00 USD | 171.09 USD | 0.00 USD | `+19.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 330,880.00 USD | 2,770.00 USD | 0.00 USD | `+19.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 332,910.00 USD | 2,040.00 USD | 0.00 USD | `+20.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 333,090.00 USD | 172.32 USD | 0.00 USD | `+20.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 333,270.00 USD | 187.72 USD | 0.00 USD | `+20.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 333,460.00 USD | 188.39 USD | 0.00 USD | `+21.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 336,130.00 USD | 2,670.00 USD | 0.00 USD | `+21.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 336,300.00 USD | 174.23 USD | 0.00 USD | `+21.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 336,480.00 USD | 174.38 USD | 0.00 USD | `+21.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 336,650.00 USD | 174.84 USD | 0.00 USD | `+21.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 336,800.00 USD | 150.90 USD | 0.00 USD | `+22.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 336,950.00 USD | 151.03 USD | 0.00 USD | `+22.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 337,110.00 USD | 151.16 USD | 0.00 USD | `+22.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 339,150.00 USD | 2,050.00 USD | 0.00 USD | `+24.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 339,260.00 USD | 110.00 USD | 0.00 USD | `+25.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 339,740.00 USD | 475.80 USD | 0.00 USD | `+27.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 340,950.00 USD | 1,210.00 USD | 0.00 USD | `+28.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 383,870.00 USD | 42,930.00 USD | 0.00 USD | `+28.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 385,880.00 USD | 2,000.00 USD | 0.00 USD | `+31.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 387,260.00 USD | 1,380.00 USD | 0.00 USD | `+33.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 387,510.00 USD | 245.41 USD | 0.00 USD | `+36.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 395,900.00 USD | 8,390.00 USD | 0.00 USD | `+37.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 396,320.00 USD | 415.25 USD | 0.00 USD | `+38.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 402,830.00 USD | 6,520.00 USD | 0.00 USD | `+39.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 407,630.00 USD | 4,800.00 USD | 0.00 USD | `+39.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 408,290.00 USD | 655.75 USD | 0.00 USD | `+40.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 408,880.00 USD | 596.43 USD | 0.00 USD | `+42.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 410,700.00 USD | 1,810.00 USD | 0.00 USD | `+43.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 424,580.00 USD | 13,880.00 USD | 0.00 USD | `+43.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 425,830.00 USD | 1,250.00 USD | 0.00 USD | `+44.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 427,900.00 USD | 2,070.00 USD | 0.00 USD | `+48.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 428,040.00 USD | 140.05 USD | 0.00 USD | `+49.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 428,200.00 USD | 160.42 USD | 0.00 USD | `+49.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 429,160.00 USD | 954.32 USD | 0.00 USD | `+50.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 463,330.00 USD | 34,170.00 USD | 0.00 USD | `+53.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 464,210.00 USD | 879.84 USD | 0.00 USD | `+59.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 467,260.00 USD | 3,050.00 USD | 0.00 USD | `+61.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 467,560.00 USD | 297.27 USD | 0.00 USD | `+65.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 476,090.00 USD | 8,530.00 USD | 0.00 USD | `+76.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 476,230.00 USD | 143.99 USD | 0.00 USD | `+78.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 476,410.00 USD | 177.05 USD | 0.00 USD | `+89.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 476,840.00 USD | 431.40 USD | 0.00 USD | `+92.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 477,060.00 USD | 220.77 USD | 0.00 USD | `+94.16%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7730` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 9,740.00 USD | 39.63 USD | 2,230.00 USD |
| `7D` | `0.7750` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 698.40 USD | 0.00 USD | 3,460.00 USD |
| `7D` | `0.7790` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 0.00 USD | 3,100.00 USD | 53.43 USD |
| `7D` | `0.7810` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 436.65 USD | 25.30 USD | 1,410.00 USD |
| `7D` | `0.7830` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 114.15 USD | 1,980.00 USD | 0.00 USD |
| `7D` | `0.7850` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 112.95 USD | 2,340.00 USD | 180.30 USD |
| `7D` | `0.7870` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 5,690.00 USD | 3,090.00 USD | 450.49 USD |
| `7D` | `0.7890` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 88.75 USD | 0.00 USD | 2,110.00 USD |
| `7D` | `0.7910` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD |
| `7D` | `0.7930` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 20,360.00 USD | 1,560.00 USD | 6,130.00 USD |
| `7D` | `0.7950` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 3,290.00 USD | 8,430.00 USD | 14,710.00 USD |
| `7D` | `0.7970` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 10,100.00 USD | 1,130.00 USD | 522.30 USD |
| `7D` | `0.7990` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 20,360.00 USD | 6,180.00 USD | 13,950.00 USD |
| `7D` | `0.8010` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 5,420.00 USD | 5,300.00 USD | 2,300.00 USD |
| `7D` | `0.8030` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 4,550.00 USD | 2,440.00 USD | 10,410.00 USD |
| `7D` | `0.8050` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD |
| `7D` | `0.8070` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 12,160.00 USD | 4,660.00 USD | 16,650.00 USD |
| `7D` | `0.8090` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD |
| `7D` | `0.8110` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD |
| `7D` | `0.8130` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 14,060.00 USD | 2,970.00 USD | 9,350.00 USD |
| `7D` | `0.8150` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 61,120.00 USD | 7,590.00 USD | 19,500.00 USD |
| `7D` | `0.8170` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 10,780.00 USD | 8,770.00 USD | 9,670.00 USD |
| `7D` | `0.8190` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD |
| `7D` | `0.8210` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 7,510.00 USD | 3,290.00 USD | 10,030.00 USD |
| `7D` | `0.8230` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 29,430.00 USD | 5,100.00 USD | 13,220.00 USD |
| `7D` | `0.8250` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD |
| `7D` | `0.8270` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 4,320.00 USD | 5,770.00 USD | 616.76 USD |
| `7D` | `0.8290` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD |
| `7D` | `0.8310` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 9,280.00 USD | 1,660.00 USD | 2,450.00 USD |
| `7D` | `0.8330` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 16,220.00 USD | 11,360.00 USD | 77.95 USD |
| `7D` | `0.8350` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 19,490.00 USD | 0.00 USD | 2,290.00 USD |
| `7D` | `0.8370` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 15,240.00 USD | 1,480.00 USD | 0.00 USD |
| `7D` | `0.8390` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD |
| `7D` | `0.8410` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD |
| `1D` | `0.8420` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 2,800.00 USD | 5,820.00 USD | 933.95 USD |
| `7D` | `0.8430` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 11,320.00 USD | 3,840.00 USD | 4,060.00 USD |
| `1D` | `0.8440` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 2,360.00 USD | 778.54 USD | 31.90 USD |
| `7D` | `0.8450` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 1,980.00 USD | 404.64 USD | 474.61 USD |
| `1D` | `0.8460` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 16,570.00 USD | 7,340.00 USD | 595.19 USD |
| `7D` | `0.8470` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 7,900.00 USD | 1,730.00 USD | 2,390.00 USD |
| `1D` | `0.8480` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 7,990.00 USD | 951.92 USD | 3,080.00 USD |
| `7D` | `0.8490` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 22,370.00 USD | 9,610.00 USD | 0.00 USD |
| `1D` | `0.8500` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 13,780.00 USD | 3,980.00 USD | 6,580.00 USD |
| `7D` | `0.8510` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 14,280.00 USD | 991.53 USD | 21,470.00 USD |
| `1D` | `0.8520` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 8,170.00 USD | 3,840.00 USD | 19,940.00 USD |
| `7D` | `0.8530` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD |
| `1D` | `0.8540` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 3,330.00 USD | 5,480.00 USD | 4,800.00 USD |
| `7D` | `0.8550` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD |
| `1D` | `0.8560` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 16,770.00 USD | 760.40 USD | 2,660.00 USD |
| `7D` | `0.8570` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 3,540.00 USD | 944.22 USD | 8,450.00 USD |
| `1D` | `0.8580` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 2,870.00 USD | 1,040.00 USD | 8,640.00 USD |
| `7D` | `0.8590` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 3,730.00 USD | 0.00 USD | 1,560.00 USD |
| `1D` | `0.8600` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 7,990.00 USD | 10,610.00 USD | 18,580.00 USD |
| `7D` | `0.8610` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 9,960.00 USD | 3,660.00 USD | 35,340.00 USD |
| `1D` | `0.8620` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 12,920.00 USD | 12,720.00 USD | 0.00 USD |
| `7D` | `0.8630` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 758.91 USD | 2,910.00 USD | 1,280.00 USD |
| `1D` | `0.8640` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 48,740.00 USD | 2,370.00 USD | 3,790.00 USD |
| `7D` | `0.8650` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 47,860.00 USD | 18,930.00 USD | 184.85 USD |
| `1D` | `0.8660` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD |
| `7D` | `0.8670` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 13,660.00 USD | 3,720.00 USD | 12,140.00 USD |
| `1D` | `0.8680` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 43,000.00 USD | 9,030.00 USD | 11,890.00 USD |
| `7D` | `0.8690` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 160,750.00 USD | 13,110.00 USD | 46,230.00 USD |
| `1D` | `0.8700` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 49,290.00 USD | 3,880.00 USD | 33,390.00 USD |
| `7D` | `0.8710` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 7,370.00 USD | 23,340.00 USD | 13,110.00 USD |
| `1D` | `0.8720` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 30,840.00 USD | 34,140.00 USD | 24,590.00 USD |
| `7D` | `0.8730` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 0.00 USD | 8,170.00 USD | 295.31 USD |
| `1D` | `0.8740` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 59,650.00 USD | 12,180.00 USD | 33,130.00 USD |
| `7D` | `0.8750` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 0.00 USD | 6,380.00 USD | 8,950.00 USD |
| `1D` | `0.8760` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 14,770.00 USD | 5,000.00 USD | 0.00 USD |
| `7D` | `0.8770` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 1,390.00 USD | 0.00 USD | 30,820.00 USD |
| `1D` | `0.8780` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 0.00 USD | 76.69 USD | 50,910.00 USD |
| `7D` | `0.8790` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 873.30 USD | 5,580.00 USD | 53,860.00 USD |
| `1D` | `0.8800` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 12,990.00 USD | 57.65 USD | 3,810.00 USD |
| `7D` | `0.8810` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 1,830.00 USD | 240.78 USD | 0.00 USD |
| `1D` | `0.8820` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 825.04 USD | 10,170.00 USD | 0.00 USD |
| `7D` | `0.8830` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 2,320.00 USD | 10,140.00 USD | 11,710.00 USD |
| `1D` | `0.8840` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 1,680.00 USD | 16,790.00 USD | 8,890.00 USD |
| `7D` | `0.8850` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 0.00 USD | 5,800.00 USD | 3,970.00 USD |
| `1D` | `0.8860` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 66,940.00 USD | 27,710.00 USD | 2,350.00 USD |
| `7D` | `0.8870` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 271,870.00 USD | 22,320.00 USD | 81,590.00 USD |
| `1D` | `0.8880` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 74,070.00 USD | 14,120.00 USD | 36,640.00 USD |
| `7D` | `0.8890` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 54,380.00 USD | 73,890.00 USD | 13,880.00 USD |
| `1D` | `0.8900` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 2,730.00 USD | 51,760.00 USD | 910.96 USD |
| `7D` | `0.8910` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 75,300.00 USD | 22,240.00 USD | 34,270.00 USD |
| `1D` | `0.8920` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 46,090.00 USD | 32,770.00 USD | 56,100.00 USD |
| `7D` | `0.8930` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 62,870.00 USD | 23,560.00 USD | 9,170.00 USD |
| `1D` | `0.8940` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 13,790.00 USD | 18,130.00 USD | 1,980.00 USD |
| `7D` | `0.8950` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 7,120.00 USD | 37,670.00 USD | 57,420.00 USD |
| `1D` | `0.8960` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 5,530.00 USD | 26,420.00 USD | 5,550.00 USD |
| `7D` | `0.8970` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 2,140.00 USD | 4,820.00 USD | 56,330.00 USD |
| `1D` | `0.8980` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 1,100.00 USD | 26,840.00 USD | 16,170.00 USD |
| `7D` | `0.8990` | 987,790.00 USD | 0.00 USD | 987,790.00 USD | 0.00 USD | 34,220.00 USD | 0.00 USD |
| `1D` | `0.9000` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 5,080.00 USD | 15,740.00 USD | 682.73 USD |
| `7D` | `0.9010` | 953,570.00 USD | 0.00 USD | 953,570.00 USD | 0.00 USD | 48,840.00 USD | 0.00 USD |
| `1D` | `0.9020` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 4,110.00 USD | 11,830.00 USD | 3,010.00 USD |
| `7D` | `0.9030` | 904,730.00 USD | 0.00 USD | 904,730.00 USD | 0.00 USD | 16,370.00 USD | 23,930.00 USD |
| `1D` | `0.9040` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 12,290.00 USD | 22,810.00 USD | 28,760.00 USD |
| `7D` | `0.9050` | 864,430.00 USD | 0.00 USD | 864,430.00 USD | 0.00 USD | 3,840.00 USD | 0.00 USD |
| `1D` | `0.9060` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 30,140.00 USD | 10,280.00 USD | 25,120.00 USD |
| `7D` | `0.9070` | 860,590.00 USD | 0.00 USD | 860,590.00 USD | 23,910.00 USD | 0.00 USD | 42,040.00 USD |
| `1D` | `0.9080` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 20,470.00 USD | 10,040.00 USD | 19,510.00 USD |
| `1D` | `0.9100` | 987,540.00 USD | 0.00 USD | 987,540.00 USD | 8,170.00 USD | 3,480.00 USD | 1,730.00 USD |
| `1D` | `0.9120` | 974,170.00 USD | 0.00 USD | 974,170.00 USD | 27,150.00 USD | 5,580.00 USD | 2,940.00 USD |
| `7D` | `0.9130` | 794,640.00 USD | 0.00 USD | 794,640.00 USD | 0.00 USD | 0.00 USD | 20,720.00 USD |
| `1D` | `0.9140` | 938,510.00 USD | 0.00 USD | 938,510.00 USD | 9,600.00 USD | 10,190.00 USD | 28,170.00 USD |
| `7D` | `0.9150` | 773,920.00 USD | 0.00 USD | 773,920.00 USD | 0.00 USD | 515.41 USD | 15,680.00 USD |
| `1D` | `0.9160` | 890,560.00 USD | 0.00 USD | 890,560.00 USD | 1,890.00 USD | 6,570.00 USD | 10,930.00 USD |
| `7D` | `0.9170` | 757,720.00 USD | 0.00 USD | 757,720.00 USD | 0.00 USD | 0.00 USD | 33,180.00 USD |
| `1D` | `0.9180` | 871,160.00 USD | 0.00 USD | 871,160.00 USD | 7,300.00 USD | 5,940.00 USD | 9,530.00 USD |
| `1D` | `0.9200` | 848,390.00 USD | 0.00 USD | 848,390.00 USD | 8,570.00 USD | 11,210.00 USD | 5,730.00 USD |
| `7D` | `0.9210` | 724,540.00 USD | 0.00 USD | 724,540.00 USD | 0.00 USD | 7,760.00 USD | 3,970.00 USD |
| `1D` | `0.9220` | 822,880.00 USD | 0.00 USD | 822,880.00 USD | 13,740.00 USD | 3,470.00 USD | 877.09 USD |
| `7D` | `0.9230` | 712,810.00 USD | 0.00 USD | 712,810.00 USD | 294,370.00 USD | 0.00 USD | 26,680.00 USD |
| `1D` | `0.9240` | 804,800.00 USD | 0.00 USD | 804,800.00 USD | 88,170.00 USD | 20,790.00 USD | 43,600.00 USD |
| `7D` | `0.9250` | 391,760.00 USD | 0.00 USD | 391,760.00 USD | 0.00 USD | 52,780.00 USD | 84,070.00 USD |
| `1D` | `0.9260` | 652,250.00 USD | 0.00 USD | 652,250.00 USD | 35,300.00 USD | 51,770.00 USD | 83,620.00 USD |
| `7D` | `0.9270` | 254,910.00 USD | 0.00 USD | 254,910.00 USD | 44,020.00 USD | 11,800.00 USD | 0.00 USD |
| `1D` | `0.9280` | 481,560.00 USD | 0.00 USD | 481,560.00 USD | 92,240.00 USD | 12,420.00 USD | 66,550.00 USD |
| `7D` | `0.9290` | 199,090.00 USD | 0.00 USD | 199,090.00 USD | 0.00 USD | 12,750.00 USD | 1,600.00 USD |
| `1D` | `0.9300` | 310,340.00 USD | 0.00 USD | 310,340.00 USD | 5,140.00 USD | 15,160.00 USD | 3,840.00 USD |
| `1D` | `0.9320` | 286,200.00 USD | 0.00 USD | 286,200.00 USD | 7,440.00 USD | 7,530.00 USD | 20,160.00 USD |
| `7D` | `0.9330` | 184,740.00 USD | 0.00 USD | 184,740.00 USD | 37,450.00 USD | 0.00 USD | 31,370.00 USD |
| `1D` | `0.9340` | 251,070.00 USD | 0.00 USD | 251,070.00 USD | 88,620.00 USD | 23,180.00 USD | 38,810.00 USD |
| `7D` | `0.9350` | 115,920.00 USD | 0.00 USD | 115,920.00 USD | 0.00 USD | 11,160.00 USD | 20,370.00 USD |
| `1D` | `0.9360` | 100,470.00 USD | 0.00 USD | 100,470.00 USD | 52,220.00 USD | 15,760.00 USD | 18,770.00 USD |
| `7D` | `0.9370` | 84,400.00 USD | 0.00 USD | 84,400.00 USD | 16,340.00 USD | 19,540.00 USD | 48,530.00 USD |
| `1D` | `0.9380` | 13,720.00 USD | 0.00 USD | 13,720.00 USD | 0.00 USD | 103.28 USD | 13,620.00 USD |
| `7D` | `0.9380` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9390` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9390` | 74,160.00 USD | 74,160.00 USD | 0.00 USD | 39,250.00 USD | 0.00 USD | 34,910.00 USD |
| `1D` | `0.9400` | 2,560.00 USD | 2,560.00 USD | 0.00 USD | 2,020.00 USD | 548.70 USD | 0.00 USD |
| `7D` | `0.9410` | 237,210.00 USD | 237,210.00 USD | 0.00 USD | 161,930.00 USD | 1,130.00 USD | 0.00 USD |
| `1D` | `0.9420` | 3,800.00 USD | 3,800.00 USD | 0.00 USD | 1,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9440` | 4,020.00 USD | 4,020.00 USD | 0.00 USD | 0.00 USD | 224.96 USD | 0.00 USD |
| `7D` | `0.9450` | 261,500.00 USD | 261,500.00 USD | 0.00 USD | 0.00 USD | 20,890.00 USD | 3,390.00 USD |
| `1D` | `0.9460` | 4,300.00 USD | 4,300.00 USD | 0.00 USD | 0.00 USD | 199.60 USD | 79.38 USD |
| `7D` | `0.9470` | 348,010.00 USD | 348,010.00 USD | 0.00 USD | 3,540.00 USD | 6,380.00 USD | 76,590.00 USD |
| `1D` | `0.9480` | 6,270.00 USD | 6,270.00 USD | 0.00 USD | 1,790.00 USD | 0.00 USD | 176.94 USD |
| `7D` | `0.9490` | 431,950.00 USD | 431,950.00 USD | 0.00 USD | 2,770.00 USD | 10,340.00 USD | 70,820.00 USD |
| `1D` | `0.9500` | 86,450.00 USD | 86,450.00 USD | 0.00 USD | 80,090.00 USD | 85.68 USD | 0.00 USD |
| `7D` | `0.9510` | 723,340.00 USD | 723,340.00 USD | 0.00 USD | 258,650.00 USD | 28,180.00 USD | 4,570.00 USD |
| `1D` | `0.9520` | 87,800.00 USD | 87,800.00 USD | 0.00 USD | 0.00 USD | 1,350.00 USD | 0.00 USD |
| `7D` | `0.9530` | 731,580.00 USD | 731,580.00 USD | 0.00 USD | 0.00 USD | 8,240.00 USD | 0.00 USD |
| `1D` | `0.9540` | 105,670.00 USD | 105,670.00 USD | 0.00 USD | 10,150.00 USD | 7,720.00 USD | 0.00 USD |
| `7D` | `0.9550` | 751,310.00 USD | 751,310.00 USD | 0.00 USD | 0.00 USD | 19,730.00 USD | 0.00 USD |
| `1D` | `0.9560` | 146,030.00 USD | 146,030.00 USD | 0.00 USD | 18,010.00 USD | 20,990.00 USD | 1,370.00 USD |
| `7D` | `0.9570` | 764,470.00 USD | 764,470.00 USD | 0.00 USD | 1,910.00 USD | 10,300.00 USD | 957.94 USD |
| `1D` | `0.9580` | 164,910.00 USD | 164,910.00 USD | 0.00 USD | 7,260.00 USD | 9,120.00 USD | 2,490.00 USD |
| `7D` | `0.9590` | 785,540.00 USD | 785,540.00 USD | 0.00 USD | 1,980.00 USD | 18,220.00 USD | 866.69 USD |
| `1D` | `0.9600` | 192,820.00 USD | 192,820.00 USD | 0.00 USD | 17,180.00 USD | 8,190.00 USD | 2,550.00 USD |
| `7D` | `0.9610` | 810,930.00 USD | 810,930.00 USD | 0.00 USD | 24,370.00 USD | 0.00 USD | 1,010.00 USD |
| `1D` | `0.9620` | 354,820.00 USD | 354,820.00 USD | 0.00 USD | 81,730.00 USD | 20,070.00 USD | 60,200.00 USD |
| `7D` | `0.9630` | 983,460.00 USD | 983,460.00 USD | 0.00 USD | 56,160.00 USD | 31,820.00 USD | 84,550.00 USD |
| `1D` | `0.9640` | 532,330.00 USD | 532,330.00 USD | 0.00 USD | 53,800.00 USD | 43,860.00 USD | 79,850.00 USD |
| `7D` | `0.9650` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 97,600.00 USD | 0.00 USD | 12,330.00 USD |
| `1D` | `0.9660` | 599,750.00 USD | 599,750.00 USD | 0.00 USD | 16,900.00 USD | 13,350.00 USD | 37,190.00 USD |
| `7D` | `0.9670` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 40,070.00 USD | 5,550.00 USD | 0.00 USD |
| `1D` | `0.9680` | 665,880.00 USD | 665,880.00 USD | 0.00 USD | 44,230.00 USD | 17,940.00 USD | 3,960.00 USD |
| `7D` | `0.9690` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 21,100.00 USD | 30,500.00 USD |
| `1D` | `0.9700` | 736,890.00 USD | 736,890.00 USD | 0.00 USD | 16,500.00 USD | 11,640.00 USD | 42,870.00 USD |
| `7D` | `0.9710` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 18,250.00 USD | 31,370.00 USD |
| `1D` | `0.9720` | 842,310.00 USD | 842,310.00 USD | 0.00 USD | 31,880.00 USD | 8,520.00 USD | 65,030.00 USD |
| `7D` | `0.9730` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 2,910.00 USD | 9,290.00 USD | 27,110.00 USD |
| `1D` | `0.9740` | 908,520.00 USD | 908,520.00 USD | 0.00 USD | 29,450.00 USD | 8,140.00 USD | 28,610.00 USD |
| `7D` | `0.9750` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 2,090.00 USD | 17,230.00 USD | 51,650.00 USD |
| `1D` | `0.9760` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 54,930.00 USD | 27,390.00 USD | 20,220.00 USD |
| `7D` | `0.9770` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD |
| `1D` | `0.9780` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 44,310.00 USD | 4,920.00 USD | 18,070.00 USD |
| `7D` | `0.9790` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD | 85,420.00 USD |
| `1D` | `0.9800` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 38,280.00 USD | 11,420.00 USD | 31,120.00 USD |
| `7D` | `0.9810` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 540.00 USD | 4,020.00 USD | 119,460.00 USD |
| `1D` | `0.9820` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 32,680.00 USD | 21,930.00 USD | 24,670.00 USD |
| `7D` | `0.9830` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 124,720.00 USD | 15,810.00 USD | 94,290.00 USD |
| `1D` | `0.9840` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 13,910.00 USD | 16,870.00 USD | 58,220.00 USD |
| `7D` | `0.9850` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 211.77 USD | 22,300.00 USD |
| `1D` | `0.9860` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 59,170.00 USD | 7,150.00 USD | 26,140.00 USD |
| `7D` | `0.9870` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 67,950.00 USD |
| `1D` | `0.9880` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 17,200.00 USD | 3,710.00 USD | 17,030.00 USD |
| `7D` | `0.9890` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `0.9900` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 66,490.00 USD | 7,820.00 USD | 33,010.00 USD |
| `7D` | `0.9910` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 3,700.00 USD | 800.44 USD | 35,270.00 USD |
| `1D` | `0.9920` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 12,580.00 USD | 5,030.00 USD | 31,930.00 USD |
| `7D` | `0.9930` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 36,000.00 USD |
| `1D` | `0.9940` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 25,660.00 USD | 1,250.00 USD | 10,030.00 USD |
| `7D` | `0.9950` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 63,060.00 USD | 5,380.00 USD | 58,050.00 USD |
| `1D` | `0.9960` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 19,070.00 USD | 3,600.00 USD | 7,450.00 USD |
| `7D` | `0.9970` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 95,130.00 USD | 253.35 USD | 4,670.00 USD |
| `1D` | `0.9980` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 54,550.00 USD | 10,730.00 USD | 15,870.00 USD |
| `7D` | `0.9990` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 6,490.00 USD | 462.12 USD |
| `1D` | `1.00` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 49,260.00 USD | 18,230.00 USD | 6,740.00 USD |
| `7D` | `1.00` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.00` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 16,910.00 USD | 2,030.00 USD | 7,440.00 USD |
| `7D` | `1.00` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 107,670.00 USD | 21,850.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 10,790.00 USD | 9,550.00 USD | 9,410.00 USD |
| `7D` | `1.00` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 32,430.00 USD | 3,970.00 USD | 12,730.00 USD |
| `1D` | `1.01` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 103,670.00 USD | 10,200.00 USD | 25,320.00 USD |
| `7D` | `1.01` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 35,710.00 USD | 240.78 USD | 29,210.00 USD |
| `1D` | `1.01` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 23,240.00 USD | 9,330.00 USD | 30,960.00 USD |
| `7D` | `1.01` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD |
| `1D` | `1.01` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 12,560.00 USD | 17,230.00 USD | 971.85 USD |
| `7D` | `1.01` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 20,090.00 USD | 17,980.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 16,880.00 USD | 15,730.00 USD | 265.91 USD |
| `7D` | `1.01` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD |
| `1D` | `1.01` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 7,030.00 USD | 5,790.00 USD | 15,870.00 USD |
| `7D` | `1.01` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 26,510.00 USD | 7,420.00 USD |
| `1D` | `1.02` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 9,410.00 USD | 22,350.00 USD | 9,680.00 USD |
| `7D` | `1.02` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD |
| `1D` | `1.02` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 26,110.00 USD | 2,060.00 USD | 12,670.00 USD |
| `7D` | `1.02` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 17,960.00 USD | 83,360.00 USD | 11,810.00 USD |
| `1D` | `1.02` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 40,010.00 USD | 9,980.00 USD | 18,380.00 USD |
| `7D` | `1.02` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 61,450.00 USD | 32,840.00 USD | 68,370.00 USD |
| `1D` | `1.02` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 31,700.00 USD | 17,830.00 USD | 27,460.00 USD |
| `7D` | `1.02` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 82,230.00 USD | 86,210.00 USD | 146,060.00 USD |
| `1D` | `1.02` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 41,760.00 USD | 8,850.00 USD | 34,590.00 USD |
| `7D` | `1.02` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 28,320.00 USD | 48,490.00 USD | 37,230.00 USD |
| `1D` | `1.03` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 36,010.00 USD | 18,210.00 USD | 17,280.00 USD |
| `7D` | `1.03` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 161,070.00 USD | 127,000.00 USD | 25,260.00 USD |
| `1D` | `1.03` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 14,780.00 USD | 8,920.00 USD | 15,510.00 USD |
| `7D` | `1.03` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD |
| `1D` | `1.03` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 65,560.00 USD | 13,340.00 USD | 18,360.00 USD |
| `7D` | `1.03` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD |
| `1D` | `1.03` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 30,500.00 USD | 7,820.00 USD | 32,160.00 USD |
| `7D` | `1.03` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD |
| `1D` | `1.03` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 13,500.00 USD | 9,390.00 USD | 13,550.00 USD |
| `7D` | `1.03` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 259,060.00 USD | 8,290.00 USD | 43,700.00 USD |
| `1D` | `1.04` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 4,560.00 USD | 11,000.00 USD | 6,050.00 USD |
| `7D` | `1.04` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 193,150.00 USD | 3,330.00 USD | 109,460.00 USD |
| `1D` | `1.04` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 45,570.00 USD | 3,700.00 USD | 8,740.00 USD |
| `7D` | `1.04` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 239,580.00 USD | 9,010.00 USD | 134,440.00 USD |
| `1D` | `1.04` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 9,270.00 USD | 6,500.00 USD | 16,260.00 USD |
| `7D` | `1.04` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 285,690.00 USD | 2,090.00 USD | 159,500.00 USD |
| `1D` | `1.04` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 12,870.00 USD | 7,160.00 USD | 3,380.00 USD |
| `7D` | `1.04` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD |
| `1D` | `1.04` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 3,600.00 USD | 1,900.00 USD | 11,370.00 USD |
| `7D` | `1.04` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD |
| `1D` | `1.05` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 5,850.00 USD | 5,000.00 USD | 2,980.00 USD |
| `7D` | `1.05` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 178,890.00 USD | 96,370.00 USD | 244,850.00 USD |
| `1D` | `1.05` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 3,870.00 USD | 900.45 USD | 9,870.00 USD |
| `7D` | `1.05` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 116,030.00 USD | 13,780.00 USD | 77,620.00 USD |
| `1D` | `1.05` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 29,490.00 USD | 4,070.00 USD | 8,230.00 USD |
| `7D` | `1.05` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 175,350.00 USD | 43,690.00 USD | 96,730.00 USD |
| `1D` | `1.05` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 4,540.00 USD | 937.66 USD | 16,280.00 USD |
| `1D` | `1.05` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 4,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.05` | 7,580,000.00 USD | 7,580,000.00 USD | 0.00 USD | 68,010.00 USD | 58,070.00 USD | 74,380.00 USD |
| `7D` | `1.05` | 7,810,000.00 USD | 7,810,000.00 USD | 0.00 USD | 121,450.00 USD | 33,860.00 USD | 72,330.00 USD |
| `7D` | `1.06` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 218,860.00 USD | 70,160.00 USD | 106,380.00 USD |
| `7D` | `1.06` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 239,650.00 USD | 74,380.00 USD | 145,170.00 USD |
| `7D` | `1.06` | 8,940,000.00 USD | 8,940,000.00 USD | 0.00 USD | 138,520.00 USD | 56,310.00 USD | 78,020.00 USD |
| `7D` | `1.06` | 9,220,000.00 USD | 9,220,000.00 USD | 0.00 USD | 140,500.00 USD | 73,690.00 USD | 71,340.00 USD |
| `7D` | `1.06` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 74,870.00 USD | 27,820.00 USD | 91,220.00 USD |
| `7D` | `1.07` | 9,500,000.00 USD | 9,500,000.00 USD | 0.00 USD | 60,290.00 USD | 26,450.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `173.93M` | Total OI Tokens: `185,316,830.3 DOT`
  * 1h OI Change: `-0.81%` | 4h OI Change: `-0.82%` | 24h OI Change: `-15.69%`
  * Exchange Breakdown: Binance=`34.17M` | Bybit=`22.27M` | OKX=`10.11M` | Hyperliquid=`5.81M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `366.17` | Last 24h: `6.26K` | Last 3d: `-7.35K` | Last 7d: `-25.50K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0116%` |
| **USDT Bybit** | `-0.0125%` | **USDT KuCoin** | `-0.0215%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0025%` | **USDT Bitget** | `0.0059%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `57.06%` | `42.94%` | `1.33` | 2,920,000.00 USD |
| `15M` | `Binance` | `62.21%` | `37.79%` | `1.65` | 612,340.00 USD |
| `15M` | `OKX` | `67%` | `33%` | `2.03` | 194,320.00 USD |
| `15M` | `Bybit` | `48.99%` | `51.01%` | `0.96` | 160,330.00 USD |
| `15M` | `KuCoin` | `38.19%` | `61.81%` | `0.62` | 25,120.00 USD |
| `15M` | `Gate` | `64.94%` | `35.06%` | `1.85` | 50,900.00 USD |
| `15M` | `Bitget` | `66.99%` | `33.01%` | `2.03` | 56,080.00 USD |
| `15M` | `BingX` | `53.45%` | `46.55%` | `1.15` | 1,000,000.00 USD |
| `15M` | `MEXC` | `88.18%` | `11.82%` | `7.46` | 236,080.00 USD |
| `15M` | `Bitunix` | `66.38%` | `33.62%` | `1.97` | 41,860.00 USD |
| `15M` | `Hyperliquid` | `70.79%` | `29.21%` | `2.42` | 29,470.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `55.22%` | `44.78%` | `1.23` | 323,120.00 USD |
| `15M` | `Crypto.com` | `0.89%` | `99.11%` | `0.01` | 662.67 USD |
| `15M` | `WhiteBIT` | `10.08%` | `89.92%` | `0.11` | 173,320.00 USD |
| `15M` | `HTX` | `74%` | `26%` | `2.85` | 1,270.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `51.55%` | `48.45%` | `1.06` | 4,620.00 USD |
| `15M` | `Aster` | `56.22%` | `43.78%` | `1.28` | 135.67 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `52.76%` | `47.24%` | `1.12` | 5,990.00 USD |
| `15M` | `Whale Positions` | `62.21%` | `37.79%` | `1.65` | 612,340.00 USD |
| `15M` | `Global Accounts` | `57.06%` | `42.94%` | `1.33` | 2,920,000.00 USD |
| `1H` | `DOT` | `47.41%` | `52.59%` | `0.90` | 23,390,000.00 USD |
| `1H` | `Binance` | `49.17%` | `50.83%` | `0.97` | 8,540,000.00 USD |
| `1H` | `OKX` | `47.35%` | `52.65%` | `0.90` | 1,990,000.00 USD |
| `1H` | `Bybit` | `47.29%` | `52.71%` | `0.90` | 2,030,000.00 USD |
| `1H` | `KuCoin` | `58.73%` | `41.27%` | `1.42` | 378,190.00 USD |
| `1H` | `Gate` | `54.35%` | `45.65%` | `1.19` | 857,910.00 USD |
| `1H` | `Bitget` | `47.88%` | `52.12%` | `0.92` | 1,020,000.00 USD |
| `1H` | `BingX` | `11.93%` | `88.07%` | `0.14` | 2,440,000.00 USD |
| `1H` | `MEXC` | `49.56%` | `50.44%` | `0.98` | 3,490,000.00 USD |
| `1H` | `Bitunix` | `53.16%` | `46.84%` | `1.13` | 921,890.00 USD |
| `1H` | `Hyperliquid` | `43.53%` | `56.47%` | `0.77` | 271,920.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.08%` | `51.92%` | `0.93` | 269,040.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `99.54%` | `0.46%` | `216.39` | 958,490.00 USD |
| `1H` | `HTX` | `45.27%` | `54.73%` | `0.83` | 47,660.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `43.67%` | `56.33%` | `0.78` | 161,680.00 USD |
| `1H` | `Aster` | `45.82%` | `54.18%` | `0.85` | 24,550.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `36.17%` | `63.83%` | `0.57` | 6,640.00 USD |
| `1H` | `Whale Positions` | `49.17%` | `50.83%` | `0.97` | 8,540,000.00 USD |
| `1H` | `Global Accounts` | `47.41%` | `52.59%` | `0.90` | 23,390,000.00 USD |
| `4H` | `DOT` | `46.37%` | `53.63%` | `0.86` | 112,400,000.00 USD |
| `4H` | `Binance` | `45.05%` | `54.95%` | `0.82` | 45,840,000.00 USD |
| `4H` | `OKX` | `41.35%` | `58.65%` | `0.71` | 13,590,000.00 USD |
| `4H` | `Bybit` | `47.7%` | `52.3%` | `0.91` | 10,860,000.00 USD |
| `4H` | `KuCoin` | `47.17%` | `52.83%` | `0.89` | 1,490,000.00 USD |
| `4H` | `Gate` | `58.5%` | `41.5%` | `1.41` | 3,060,000.00 USD |
| `4H` | `Bitget` | `48.18%` | `51.82%` | `0.93` | 5,310,000.00 USD |
| `4H` | `BingX` | `23.88%` | `76.12%` | `0.31` | 5,140,000.00 USD |
| `4H` | `MEXC` | `45.57%` | `54.43%` | `0.84` | 15,350,000.00 USD |
| `4H` | `Bitunix` | `50.77%` | `49.23%` | `1.03` | 3,900,000.00 USD |
| `4H` | `Hyperliquid` | `42.67%` | `57.33%` | `0.74` | 1,600,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `57.52%` | `42.48%` | `1.35` | 2,210,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `96.68%` | `3.32%` | `29.12` | 3,170,000.00 USD |
| `4H` | `HTX` | `40.69%` | `59.31%` | `0.69` | 299,360.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `42.27%` | `57.73%` | `0.73` | 170,610.00 USD |
| `4H` | `Aster` | `46.7%` | `53.3%` | `0.88` | 266,940.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `56.83%` | `43.17%` | `1.32` | 135,340.00 USD |
| `4H` | `Whale Positions` | `45.05%` | `54.95%` | `0.82` | 45,840,000.00 USD |
| `4H` | `Global Accounts` | `46.37%` | `53.63%` | `0.86` | 112,400,000.00 USD |


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
| `5:00 UTC` | `0.9365` | `0.9373` | `0.9365` | `0.9404` | `0.9360` | 336,096.68 USD | 126,854.37 USD | 209,242.31 USD | -82,387.94 USD | `-24.51%` | `8B / 13S` |

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
| `5m` | -11,170.00 USD | -66,460.00 USD | **`DISTRIBUTION`** |
| `15m` | -12,140.00 USD | -116,460.00 USD | **`DISTRIBUTION`** |
| `30m` | -42,940.00 USD | -396,660.00 USD | **`DISTRIBUTION`** |
| `1h` | -41,830.00 USD | -600,650.00 USD | **`DISTRIBUTION`** |
| `2h` | 18,100.00 USD | -765,460.00 USD | **`DISTRIBUTION`** |
| `4h` | -143,120.00 USD | -1,730,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -108,870.00 USD | -1,800,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -3,690.00 USD | -671,040.00 USD | **`DISTRIBUTION`** |
| `12h` | -181,610.00 USD | -1,080,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,360,000.00 USD | -8,690,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,080,000.00 USD | -23,920,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,780,000.00 USD | -78,450,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-11.17K` | 15m=`-12.14K` | 1h=`-41.83K` | 24h=`-1.36M`
* Futures Capital Netflows: 5m=`-66.46K` | 15m=`-116.46K` | 1h=`-600.65K` | 24h=`-8.69M`
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
  * `2026-10-30 14:09:50 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:50:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:31:50 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.8986` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-0.3314` (Risk Distance: `1.23` pts)
  * +2.5R Take Profit: `3.97`
  * Mathematical Lot Sizing: **`8.13 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9447` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2.17` (Risk Distance: `1.23` pts)
  * +2.5R Take Profit: `-2.13`
  * Mathematical Lot Sizing: **`8.13 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9425`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
